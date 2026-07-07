# Analysis

Importable Python modules + thin notebooks. **Every figure in the report must regenerate from raw data with one command.**

- `odmr_fit.py` — Lorentzian dip fitting with uncertainties; `--selftest` validates recovery on synthetic data BEFORE first hardware data.
- `lockin.py` — software lock-in demodulation of OOK-modulated PD samples.
- `zeeman.py` — splitting → field conversion, calibration curve, Hall-sensor comparison.
- `make_figures.py` — regenerates every report figure into `report/figures/`.

Run `pip install -r requirements.txt` first.
