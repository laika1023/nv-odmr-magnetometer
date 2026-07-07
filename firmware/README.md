# Firmware (Raspberry Pi Pico)

Planned modules — one file each, with a header comment stating wiring/pinout:
- `synth_adf4351.py` — register programming + frequency sweep
- `modulate.py` — TTL on/off keying of MW (via synth enable or HMC349) at the lock-in frequency
- `adc_log.py` — ADS1115/ADS1256 sampling, timestamped CSV output
- `sweep_odmr.py` — orchestrates: for each MW frequency, toggle modulation, record PD samples

Convention: every data-producing script writes a metadata JSON sidecar (see `data/README.md`).
