# Hardware

- `BOM.csv` — the living bill of materials. Update `price_paid` and `received` as orders land; this file IS your grant budget report.
- `kicad/` — PCB projects. One directory per board revision: `antenna-v1/`, `antenna-v2/` with a `CHANGELOG.md` line per revision explaining what changed and why.
- `cad/` — 3D-print files. Commit both editable source (.step/.f3d/.scad) and exported .stl.
- `optical-layout/` — labeled diagram of the beam path (photo + annotated SVG/PNG), beam height, element positions on the breadboard grid.
- `signal-chain.md` — block diagram: laser → diamond → filters → PD → ADC; synth → switch → PA → antenna. Keep current; this is Fig. 1 of the report.
