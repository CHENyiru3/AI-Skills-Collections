# Interface analysis through MCP and CLI/API

Use the current atomic model and chain IDs. The examples below refer to chain A (MCL-1) in `#1.1` and chain B (BIM BH3) in `#1.2`, after a chain split. Before splitting, the same selections were `#1/A` and `#1/B`. Do not use a surface model ID as an atomic selection.

## Four interaction categories

| Category | Evidence to calculate | Interpretation limit |
|---|---|---|
| Hydrogen bonds | Donor/acceptor atom types and geometric criteria, restricted to the two chains | A count depends on coordinates, protonation, alternate conformations, and distance/angle tolerances. It is not an energy measurement. |
| Salt bridges | Charged functional-group pairs; ChimeraX `hbonds saltOnly true` reports its charged-group H-bond subset | Salt bridges are electrostatic interactions and can overlap the H-bond list. State the definition instead of adding category counts together. |
| van der Waals contacts | Interchain atom distances relative to van der Waals radii; separate close clashes from plausible packing | Generic `contacts` includes polar interactions and clashes. A close pair is not proof of attractive van der Waals energy. |
| Electrostatic interactions | Approximate Coulombic potential on a selected surface; atom-level charged contacts if requested | Surface colors do not identify individual interacting pairs or quantify binding affinity. Record potential scale and charge/protonation assumptions. |

Report selections, criteria, atom/residue identities and distances (Å), plus what has and has not been calculated. Use separate named layers for readable displays; do not draw every interaction type at once by default.

## Count hydrogen bonds between A and B

This reports pairs and the total in the ChimeraX log without creating pseudobonds or changing atom visibility:

```text
hbonds (#1.1/A & protein) restrict (#1.2/B & protein) interModel true interSubmodel true makePseudobonds false log true
```

`restrict` is essential: analyzing both chains as one selection can include intrachain bonds. `interSubmodel true` allows interactions between sibling atomic models created by `split`; `interModel true` explicitly permits cross-model interactions. Read the actual logged total and pair list. Do not count screenshot lines or use an assumed result from another structure.

The patched MCP exposes the same options:

```python
find_hbonds(
    target="#1.1/A & protein",
    restrict="#1.2/B & protein",
    inter_model=True,
    inter_submodel=True,
    make_pseudobonds=False,
    log_details=True,
    session_id=actual_rest_port,
)
```

These extra parameters require the local patch described in [failure-lessons.md](failure-lessons.md). With an unpatched server, send the documented native command through `run_command`. For a visible interaction layer, change `makePseudobonds` to `true`, give it a distinct `name`, and use `reveal true` only if displaying the interacting residues is requested.

## Salt bridges and close contacts

For ChimeraX's salt-bridge subset, use the same selections with `saltOnly true`:

```text
hbonds (#1.1/A & protein) restrict (#1.2/B & protein) interModel true interSubmodel true saltOnly true makePseudobonds false log true
```

The MCP equivalent adds `salt_only=True` to the count-only call above. Histidine charge treatment can affect this result; inspect protonation assumptions when it matters.

For a general interchain contact list, ChimeraX's default contact overlap cutoff is −0.4 Å; spell it out for reproducibility:

```text
contacts (#1.1/A & protein) restrict (#1.2/B & protein) interModel true interSubmodel true overlapCutoff -0.4 makePseudobonds false log true
```

Inspect the reported distances and overlaps. Positive overlap indicates atoms closer than the sum of their van der Waals radii; the `clashes` command uses a more restrictive default cutoff (0.6 Å). Do not relabel the entire generic contact list as favorable van der Waals interactions.

## Electrostatic surface for chain A only

```text
surface #1.1/A & protein
coulombic #1.1/A & protein palette red-white-blue range -10,10
```

Red is negative potential, white is near zero, and blue is positive potential. The range is −10 to +10 kcal/(mol·e). Chain B can remain an orange cartoon. With default chain surfaces, each chain's potential is calculated independently from the atoms enclosed by that surface. Treat a calculation using both chains' charges as a different, explicitly specified analysis.

The default Coulombic model uses a distance-dependent dielectric (coefficient 4) and a 1.4 Å surface offset. In structures lacking explicit H atoms, charge assignment uses a protonated in-memory copy; do not claim the displayed structure was explicitly protonated. A requested pH-specific preparation requires a separate justified workflow.

## Headless CLI calculation

When the live GUI has no REST endpoint, compute from the original local file in a separate headless process instead of automating the UI:

```bash
"/Applications/ChimeraX-1.12.app/Contents/MacOS/ChimeraX" --nogui --exit --cmd 'open "/path/to/structure.cif"; hbonds (#1/A & protein) restrict (#1/B & protein) makePseudobonds false log true'
```

Use the executable found on that host. This calculation uses the file's coordinates and current CLI defaults; it does not inspect unsaved edits or alternate-conformation choices in the GUI. If those differ, calculate through the intended session's API instead. No export file is needed.

## Sources

### Verified 2PQK example

On 2026-11-05, ChimeraX 1.12 reported **9 interchain donor–acceptor atom pairs**, spanning **4 residue pairs**, for the downloaded 2PQK CIF with default relaxed criteria (0.4 Å distance tolerance and 20° angle tolerance; no explicit hydrogens in the file). An isolated headless CLI run and the patched MCP full/core profiles agreed, including after splitting the chains. This is an example result, not a fixed expected count for edited structures or other preparation choices.

| Residue pair (author numbering) | H-bond atom pairs |
|---|---:|
| A:Arg248 – B:Glu3 | 3 |
| A:Asn260 – B:Asp15 | 1 |
| A:Arg263 – B:Asp15 | 3 |
| A:Val253 – B:Arg11 | 2 |

### Command documentation

Commands and defaults were checked against the installed ChimeraX 1.12 documentation:

- [Hydrogen bonds and saltOnly](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/hbonds.html)
- [Contacts and clashes](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/clashes.html)
- [Coulombic potential](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/coulombic.html)
- [Splitting models](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/split.html)
