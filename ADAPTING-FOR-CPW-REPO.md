# Adapting this skeleton for the CPW resonator repo

Duplicate the structure as `cpw-resonators-77k`; change:
- README: goals → Q-extraction pipeline, 77 K copper study, YBCO f0(T)/Q(T) transition; safety → LN2 (cryo gloves, face shield, ventilation, no sealed containers) instead of laser.
- MILESTONES: Aug 1 boards ordered · Aug 23 fit pipeline validated on synthetic data · Sep 13 RT characterization · Oct 4 77 K dataset · Oct 25 YBCO transition · Nov 8 freeze (v1.0).
- analysis/: replace odmr_fit.py with `s21_circlefit.py` (Probst-style Qi/Qc circle fit + `--selftest` on synthetic notch data), `qvst.py` for the warm-up sweep.
- hardware/: kicad panel dirs per revision; add `stackup.md` (FR-4 vs RO4350B params used in design).
- data sidecar config keys: vna, cal_date, temperature_K, substrate, coupling_gap_um, ybco_spacer_mm.
- docs/PRIOR_ART.md: NanoVNA resonator labs, YBCO surface-resistance literature; the student-budget combination appears undocumented — note carefully, claim cautiously.
Delete this file from both repos once done.
