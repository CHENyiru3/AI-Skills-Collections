#!/usr/bin/env python3
"""Read-only PDF baseline inventory with optional rendered review previews.

Does not edit input PDFs or certify alignment/scientific correctness.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

import pdfplumber
from pypdf import PdfReader
from pypdf.generic import IndirectObject


def resource_audit(page):
    seen, images, forms, inline = set(), set(), set(), []

    def visit(resources, context):
        if resources is None:
            return
        xobjects = resources.get_object().get('/XObject')
        if xobjects is None:
            return
        for name, reference in xobjects.get_object().items():
            obj = reference.get_object()
            key = ((reference.idnum, reference.generation)
                   if isinstance(reference, IndirectObject) else ('direct', id(obj)))
            if not isinstance(reference, IndirectObject):
                inline.append(f'{context}/{name}')
            if key in seen:
                continue
            seen.add(key)
            if obj.get('/Subtype') == '/Image':
                images.add(key)
            elif obj.get('/Subtype') == '/Form':
                forms.add(key)
                visit(obj.get('/Resources'), f'{context}/{name}')

    visit(page.get('/Resources'), 'page')
    return {'unique_image_objects': len(images), 'unique_form_objects': len(forms),
            'direct_xobject_references': inline}


def inspect(path):
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    reader = PdfReader(path)
    result = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': before,
              'pypdf_page_count': len(reader.pages), 'pages': [], 'issues': []}
    with pdfplumber.open(path) as document:
        result['pdfplumber_page_count'] = len(document.pages)
        if len(document.pages) != len(reader.pages):
            result['issues'].append('Parser page counts disagree; investigate PDF structure.')
        for index, page in enumerate(reader.pages):
            item = {'page': index + 1, 'media_box': list(map(float, page.mediabox)),
                    'crop_box': list(map(float, page.cropbox)), 'rotation': page.get('/Rotate', 0),
                    'resources': resource_audit(page)}
            if index < len(document.pages):
                extracted = document.pages[index]
                fonts = Counter((c['fontname'], round(c['size'], 3)) for c in extracted.chars)
                item['text_characters'] = len(extracted.chars)
                item['extracted_font_summary'] = [
                    {'font': font, 'reported_size': size, 'characters': count}
                    for (font, size), count in sorted(fonts.items())]
            result['pages'].append(item)
    if hashlib.sha256(path.read_bytes()).hexdigest() != before:
        raise RuntimeError(f'Input changed during inventory: {path}')
    return result


def render_previews(paths, directory, executable):
    from PIL import Image, ImageDraw
    directory.mkdir(parents=True, exist_ok=True)
    previews = []
    for index, path in enumerate(paths, 1):
        # A fresh staging directory prevents older page previews entering a new
        # contact sheet if the author's revised PDF has fewer pages.
        with tempfile.TemporaryDirectory(prefix='figure-review-', dir=directory) as temporary:
            staging = Path(temporary)
            run = subprocess.run([executable, '-png', '-r', '120', str(path), str(staging / 'page')],
                                 capture_output=True, text=True)
            if run.returncode:
                raise RuntimeError(f'Rendering failed for {path}: {run.stderr.strip()}')
            if run.stderr.strip():
                print(f'Render messages for {path.name}: {run.stderr.strip()}')
            for file in sorted(staging.glob('page-*.png')):
                page_number = file.stem.rsplit('-', 1)[-1]
                destination = directory / f'{index:02d}_{path.stem}-{page_number}.png'
                shutil.copy2(file, destination)
                previews.append((path.name + ' / ' + page_number, destination))
    if not previews:
        return
    cols = min(3, len(previews)); width, height = 420, 570
    sheet = Image.new('RGB', (cols * width, ((len(previews) + cols - 1) // cols) * height), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, (label, file) in enumerate(previews):
        x, y = (i % cols) * width, (i // cols) * height
        draw.text((x + 8, y + 6), label, fill='black')
        with Image.open(file) as image:
            image = image.convert('RGB'); image.thumbnail((width - 16, height - 32))
            sheet.paste(image, (x + (width - image.width) // 2, y + 26))
    sheet.save(directory / 'contact_sheet.png')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdfs', nargs='+', type=Path)
    parser.add_argument('--out', type=Path, required=True, help='Inventory JSON path; never an input PDF.')
    parser.add_argument('--render-dir', type=Path, help='Optional directory for PNG review previews and a contact sheet.')
    parser.add_argument('--pdftoppm', default=shutil.which('pdftoppm'), help='Poppler executable; uses PATH by default.')
    args = parser.parse_args()
    paths = [p.expanduser().resolve(strict=True) for p in args.pdfs]
    out = args.out.expanduser().resolve()
    if out in paths or out.suffix.lower() == '.pdf':
        parser.error('--out must be a JSON report path, not an input/PDF path.')
    for path in paths:
        if path.suffix.lower() != '.pdf':
            parser.error(f'Not a PDF: {path}')
    report = {'purpose': 'Read-only figure baseline; human visual and scientific review remains necessary.',
              'font_note': 'Extracted sizes can be projections for rotated/transformed text; verify text matrices before editing.',
              'figures': [inspect(path) for path in paths]}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + '\n')
    if args.render_dir:
        if not args.pdftoppm:
            parser.error('PNG previews require pdftoppm; supply --pdftoppm or run inventory alone.')
        render_previews(paths, args.render_dir.expanduser().resolve(), args.pdftoppm)
    for figure, path in zip(report['figures'], paths):
        if hashlib.sha256(path.read_bytes()).hexdigest() != figure['sha256']:
            raise RuntimeError(f'Input changed during review: {path}')
    print(f'Inventoried {len(paths)} PDF(s): {out}')


if __name__ == '__main__':
    main()
