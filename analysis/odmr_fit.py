"""Lorentzian dip fitting for CW ODMR spectra, with synthetic self-test.

Usage:
    python odmr_fit.py --selftest          # validate pipeline on synthetic data
    python odmr_fit.py data/raw/FILE.csv   # fit a real spectrum (freq_hz, signal columns)
"""
import argparse
import numpy as np
from scipy.optimize import curve_fit


def lorentzian_dip(f, f0, gamma, contrast, baseline):
    """Baseline * (1 - contrast * Lorentzian). gamma = HWHM in same units as f."""
    return baseline * (1.0 - contrast * gamma**2 / ((f - f0) ** 2 + gamma**2))


def fit_dip(freq, sig, f0_guess=2.870e9):
    p0 = [f0_guess, 5e6, 0.01, np.median(sig)]
    popt, pcov = curve_fit(lorentzian_dip, freq, sig, p0=p0, maxfev=20000)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr


def selftest(seed=0):
    """Generate a noisy synthetic dip, fit it, and assert parameter recovery."""
    rng = np.random.default_rng(seed)
    true = dict(f0=2.8700e9, gamma=6e6, contrast=0.012, baseline=1.0)
    f = np.linspace(2.82e9, 2.92e9, 801)
    sig = lorentzian_dip(f, **true) + rng.normal(0, 5e-4, f.size)
    (f0, gamma, contrast, baseline), err = fit_dip(f, sig)
    print(f"recovered f0 = {f0/1e9:.6f} GHz (true {true['f0']/1e9:.6f}), "
          f"contrast = {contrast:.4f} (true {true['contrast']:.4f})")
    assert abs(f0 - true["f0"]) < 3 * err[0] + 1e5, "f0 recovery failed"
    assert abs(contrast - true["contrast"]) < 5 * err[2] + 2e-3, "contrast recovery failed"
    print("SELFTEST PASSED")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("datafile", nargs="?", help="CSV with freq_hz,signal columns")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest or not args.datafile:
        selftest()
    else:
        d = np.genfromtxt(args.datafile, delimiter=",", names=True)
        popt, perr = fit_dip(d["freq_hz"], d["signal"])
        print(f"f0 = {popt[0]/1e9:.6f} GHz ± {perr[0]/1e6:.2f} MHz | "
              f"FWHM = {2*popt[1]/1e6:.2f} MHz | contrast = {100*popt[2]:.2f}%")
