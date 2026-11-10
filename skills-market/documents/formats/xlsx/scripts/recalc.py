"""Recalculate an XLSX working copy with an isolated LibreOffice profile."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time
from zipfile import BadZipFile
from xml.sax.saxutils import escape

from openpyxl import load_workbook


def setup_libreoffice_macro(profile: Path, workbook: Path, marker: Path) -> None:
    """Write only to a new, task-owned profile; never touch user macros."""
    basic = profile / "user/basic"
    standard = basic / "Standard"
    standard.mkdir(parents=True, exist_ok=True)
    (basic / "script.xlc").write_text('''<?xml version="1.0" encoding="UTF-8"?>
<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
<library:library library:name="Standard" library:link="false"/>
</library:libraries>''')
    (standard / "script.xlb").write_text('''<?xml version="1.0" encoding="UTF-8"?>
<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Standard" library:readonly="false" library:passwordprotected="false">
<library:element library:name="Module1"/>
</library:library>''')
    code = f'''Sub RecalculateAndSave
    On Error GoTo Failed
    Dim props(2) As New com.sun.star.beans.PropertyValue
    props(0).Name = "Hidden"
    props(0).Value = True
    props(1).Name = "MacroExecutionMode"
    props(1).Value = 0
    props(2).Name = "UpdateDocMode"
    props(2).Value = 0
    doc = StarDesktop.loadComponentFromURL("{workbook.as_uri()}", "_blank", 0, props())
    doc.calculateAll()
    doc.store()
    doc.close(True)
    Open ConvertFromURL("{marker.as_uri()}") For Output As #1
    Print #1, "ok"
    Close #1
    StarDesktop.terminate()
    Exit Sub
Failed:
    Open ConvertFromURL("{marker.as_uri()}") For Output As #1
    Print #1, "error: " & Error$
    Close #1
    StarDesktop.terminate()
End Sub'''
    (standard / "Module1.xba").write_text('''<?xml version="1.0" encoding="UTF-8"?>
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="Module1" script:language="StarBasic">'''+escape(code)+'</script:module>')


def inspect_values(filename: Path) -> dict:
    """Inspect actual error cells, not strings mentioning an Excel error."""
    values = load_workbook(filename, data_only=True)
    formulas = load_workbook(filename, data_only=False)
    errors: dict[str, list[str]] = {}
    count = 0
    missing = []
    try:
        for sheet in formulas:
            for row in sheet:
                for cell in row:
                    cached = values[sheet.title][cell.coordinate]
                    location = f"{sheet.title}!{cell.coordinate}"
                    if cell.data_type == "f":
                        count += 1
                        # A cached empty string is valid; an absent numeric cache isn't.
                        if cached.value is None and cached.data_type not in {"s", "str", "inlineStr"}:
                            missing.append(location)
                    if cached.data_type == "e":
                        errors.setdefault(str(cached.value), []).append(location)
        return {
            "status": "errors_found" if errors or missing else "success",
            "total_errors": sum(map(len, errors.values())),
            "total_formulas": count,
            "missing_formula_values": missing,
            "error_summary": {key: {"count": len(v), "locations": v[:20]} for key, v in errors.items()},
        }
    finally:
        values.close()
        formulas.close()


def run_process(cmd: list[str], env: dict, timeout: float) -> str | None:
    """Drain output and stop the task-owned process group on timeout."""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env, start_new_session=True)
    try:
        _, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGKILL)
        else:
            process.kill()
        process.communicate()
        return "Recalculation timed out; input was not replaced."
    if process.returncode != 0:
        return f"LibreOffice exited {process.returncode}: {stderr.strip()}"
    return None


def formula_cells(filename: Path) -> set[tuple[str, str]]:
    workbook = load_workbook(filename, data_only=False)
    try:
        return {(sheet.title, cell.coordinate) for sheet in workbook for row in sheet for cell in row if cell.data_type == "f"}
    finally:
        workbook.close()


def recalc(filename: str, timeout: float = 30) -> dict:
    source = Path(filename).resolve()
    if not source.is_file():
        return {"error": f"File does not exist: {source}"}
    if source.suffix.lower() != ".xlsx":
        return {"error": "This helper supports XLSX working copies only; use a feature-preserving engine for other formats."}
    if timeout <= 0:
        return {"error": "timeout must be positive"}
    executable = shutil.which("soffice")
    if executable is None:
        return {"error": "LibreOffice soffice is unavailable; choose an installed calculation engine."}
    try:
        expected_formulas = formula_cells(source)
        # Same filesystem permits atomic replacement after successful calculation.
        with tempfile.TemporaryDirectory(prefix=".xlsx-recalc-", dir=source.parent) as work:
            work = Path(work)
            staged = work / source.name
            shutil.copy2(source, staged)
            profile, marker = work / "profile", work / "completed.txt"
            env = os.environ.copy()
            env["SAL_USE_VCLPLUGIN"] = "svp"
            deadline = time.monotonic() + timeout
            # Initialize this private profile before replacing its starter macro.
            init = [executable, f"-env:UserInstallation={profile.as_uri()}", "--headless", "--terminate_after_init"]
            init_result = run_process(init, env, timeout)
            if init_result is not None:
                return {"error": init_result}
            setup_libreoffice_macro(profile, staged, marker)
            cmd = [executable, f"-env:UserInstallation={profile.as_uri()}", "--headless", "--norestore", "--nodefault", "vnd.sun.star.script:Standard.Module1.RecalculateAndSave?language=Basic&location=application"]
            process_error = run_process(cmd, env, max(0.01, deadline - time.monotonic()))
            if process_error is not None:
                return {"error": process_error}
            if not marker.is_file() or marker.read_text().strip() != "ok":
                return {"error": "Calculation/save completion was not confirmed; input was not replaced."}
            result = inspect_values(staged)
            if formula_cells(staged) != expected_formulas:
                return {"error": "Formula locations changed during conversion; input was not replaced."}
            if result["missing_formula_values"]:
                result["input_replaced"] = False
                return result
            os.replace(staged, source)
            result["input_replaced"] = True
            result["engine"] = "LibreOffice; workbook macros and external-link updates disabled"
            return result
    except (OSError, ValueError, KeyError, BadZipFile) as exc:
        return {"error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("excel_file", help="XLSX working copy; replaced only after confirmed recalculation")
    parser.add_argument("timeout_seconds", type=float, nargs="?", default=30)
    args = parser.parse_args()
    result = recalc(args.excel_file, args.timeout_seconds)
    print(json.dumps(result, indent=2))
    return 0 if result.get("status") == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
