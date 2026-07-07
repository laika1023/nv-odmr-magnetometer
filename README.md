# Open-Source NV-Center ODMR Magnetometer

![Apparatus](media/hero.jpg)

**A benchtop optically detected magnetic resonance (ODMR) magnetometer built on nitrogen-vacancy centers in diamond — designed, funded, and built independently by an undergraduate for under $2,000, with full replication documentation.**

> **Status:** 🔨 In progress — Phase 1 (optics & photoluminescence). See [MILESTONES.md](MILESTONES.md).

## Headline result

<!-- Replace with ODMR spectrum / Zeeman calibration figure when available -->
*First ODMR spectrum targeted Sep 30, 2026.*

## What this is

The NV⁻ center in diamond is a room-temperature electron-spin qubit. Green light polarizes the spin; microwaves near 2.870 GHz drive spin transitions; the spin state is read out via red fluorescence. Sweeping the microwave frequency while monitoring fluorescence yields a resonance dip whose Zeeman splitting measures magnetic field at 2×2.8 MHz/gauss. This repo contains everything needed to reproduce the instrument: hardware designs, firmware, analysis code, raw data, and a technical report.

**Design goals distinguishing this build from prior teaching-lab designs** (see [docs/PRIOR_ART.md](docs/PRIOR_ART.md)):
1. Calibrated, uncertainty-quantified magnetometry validated against an independent Hall sensor
2. A VNA-characterized resonant PCB antenna, with a controlled contrast comparison vs. an untuned loop
3. A reusable open-source software lock-in / ODMR control package
4. (Stretch) Pulsed ODMR / Rabi oscillations on a hobby budget

## Repository map

| Path | Contents |
|---|---|
| `log/` | Dated build log — every session, including failures |
| `hardware/` | BOM, KiCad projects, CAD/STLs, optical layout |
| `firmware/` | Pi Pico code: synthesizer control, modulation, ADC logging |
| `analysis/` | Python package + notebooks; regenerates every figure from raw data |
| `data/` | Raw and processed datasets with metadata sidecars |
| `report/` | LaTeX source and released PDF of the technical report |
| `media/` | Photos and video |
| `docs/` | Decision log, prior-art survey, safety notes |

## Quick start (analysis)

```bash
pip install -r analysis/requirements.txt
python analysis/odmr_fit.py --selftest   # validates fit pipeline on synthetic data
```

## Safety

This build uses a Class 3R/3B laser and RF electronics. See [docs/SAFETY.md](docs/SAFETY.md). Do not replicate the optical path without wavelength-rated laser eyewear.

## License & citation

Code: MIT. Hardware & documentation: CC-BY-4.0 (see [LICENSES.md](LICENSES.md)). If you use this work, please cite via [CITATION.cff](CITATION.cff).

## Author

Julius Hochberg — Engineering & Physics, Brown University. Contact: julius_hochberg@brown.edu
