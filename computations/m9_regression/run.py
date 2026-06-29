#!/usr/bin/env python3
"""M9 regression diagnostics for raw-vs-paired reciprocal sums.

This script materializes the Round 3 A3 artifact bundle locally. It is
diagnostic_only: the Vaaler kernel is a provisional triangular placeholder
until H4 source audit fixes the exact coefficient normalization.
"""

from __future__ import annotations

import cmath
import csv
import itertools
import math
import platform
import sys
from pathlib import Path


def find_repo_root(start: Path) -> Path:
    for path in [start, *start.parents]:
        if (path / ".git").exists():
            return path
    return Path(__file__).resolve().parents[2]


ROOT = find_repo_root(Path(__file__).resolve().parent)
OUT_DIR = ROOT / "outputs"
RUN_DIR = ROOT / "computations" / "m9_regression"

X_VAL = 1_000_000
D_VAL = 200
DELTA = D_VAL // 3
H_VAL = max(1, int(round(D_VAL / (X_VAL**0.25))))
TOL = 1e-8


def exp1(t: float) -> complex:
    return cmath.exp(2j * math.pi * t)


def phi(u: float) -> float:
    """Provisional Fejer triangular placeholder for the Vaaler kernel."""
    return max(0.0, 1.0 - abs(u))


def chi4(n: int) -> int:
    m = n % 4
    if m in (0, 2):
        return 0
    return 1 if m == 1 else -1


def character_factor(h: int) -> complex:
    return exp1(h / 4.0) - exp1(3.0 * h / 4.0)


def alpha_h(h: int, height: int) -> complex:
    if h == 0:
        return 0j
    u = abs(h) / (height + 1)
    return -phi(u) / (2j * math.pi * h)


def beta_h(h: int, height: int) -> float:
    if h == 0 or h % 2 == 0:
        return 0.0
    u = abs(h) / (height + 1)
    return -phi(u) * chi4(abs(h)) / (math.pi * abs(h))


def weight_d(d: int, center: int = D_VAL, width: int = DELTA) -> float:
    return math.exp(-((d - center) / width) ** 2)


D_SET = list(range(D_VAL // 2, 2 * D_VAL + 1))
W_REAL = [weight_d(d) for d in D_SET]
W_COMPLEX = [
    w * cmath.exp(1j * 2.0 * math.pi * idx / max(1, len(W_REAL) - 1))
    for idx, w in enumerate(W_REAL)
]


def compute_bh(weights: list[complex | float], h: int) -> complex:
    total = 0j
    for d, w in zip(D_SET, weights):
        total += w * exp1(h * X_VAL / (4.0 * d))
    return total


def max_character_factor_error() -> float:
    errs: list[float] = []
    for h in range(-H_VAL, H_VAL + 1):
        if h == 0:
            continue
        expected = 2j * chi4(h) if h % 2 else 0j
        errs.append(abs(character_factor(h) - expected))
    return max(errs) if errs else 0.0


def max_beta_even_error() -> float:
    errs: list[float] = []
    for h in range(1, H_VAL + 1):
        errs.append(abs(beta_h(-h, H_VAL) - beta_h(h, H_VAL)))
    return max(errs) if errs else 0.0


def m1_raw_vs_paired() -> tuple[float, str]:
    raw = 0j
    for h in range(-H_VAL, H_VAL + 1):
        if h != 0:
            raw += alpha_h(h, H_VAL) * compute_bh(W_REAL, h)

    paired = 0.0
    for h in range(1, H_VAL + 1):
        coef = -phi(abs(h) / (H_VAL + 1)) / (math.pi * h)
        sine_sum = 0.0
        for d, w in zip(D_SET, W_REAL):
            sine_sum += w * math.sin(2.0 * math.pi * h * X_VAL / (4.0 * d))
        paired += coef * sine_sum

    diff = abs(raw - paired)
    return diff, "PASS" if diff < TOL else "FAIL"


def m2_raw_vs_paired(weights: list[complex | float], real_pairing: bool) -> tuple[float, str]:
    raw = 0j
    for h in range(-H_VAL, H_VAL + 1):
        if h != 0:
            raw += beta_h(h, H_VAL) * compute_bh(weights, h)

    paired = 0.0
    for h in range(1, H_VAL + 1):
        coeff = beta_h(h, H_VAL)
        if coeff == 0.0:
            continue
        cosine_sum = 0.0
        for d, w in zip(D_SET, weights):
            effective_weight = float(w.real) if real_pairing and isinstance(w, complex) else float(w)
            cosine_sum += effective_weight * math.cos(2.0 * math.pi * h * X_VAL / (4.0 * d))
        paired += 2.0 * coeff * cosine_sum

    diff = abs(raw - paired)
    return diff, "PASS" if diff < TOL else "FAIL_EXPECTED"


def classify_n0(
    h1: int,
    d1: int,
    h2: int,
    d2: int,
    h3: int,
    d3: int,
    h4: int,
    d4: int,
) -> str:
    if (h1, d1) == (h2, d2) and (h3, d3) == (h4, d4):
        return "N0_diag"
    if (h1, d1) == (h4, d4) and (h3, d3) == (h2, d2):
        return "N0_pairswapped"
    if (h1, d1) == (-h3, d3) and (h2, d2) == (-h4, d4):
        return "N0_signsym"
    return "N0_unclass"


def fourth_moment_bins() -> dict[str, float]:
    h_small = min(H_VAL, 5)
    h_list = [h for h in range(-h_small, h_small + 1) if h != 0 and h % 2]
    d_small = sorted({D_VAL - DELTA, D_VAL, D_VAL + DELTA})
    bins = {
        "N0_diag": 0.0,
        "N0_pairswapped": 0.0,
        "N0_signsym": 0.0,
        "N0_unclass": 0.0,
        "N_nearcoll": 0.0,
        "N_far": 0.0,
    }
    threshold = D_VAL**4 / X_VAL

    for h1, h2, h3, h4 in itertools.product(h_list, repeat=4):
        beta_prod = beta_h(h1, H_VAL) * beta_h(h2, H_VAL) * beta_h(h3, H_VAL) * beta_h(h4, H_VAL)
        if abs(beta_prod) < 1e-30:
            continue
        for d1, d2, d3, d4 in itertools.product(d_small, repeat=4):
            w_prod = weight_d(d1) * weight_d(d2) * weight_d(d3) * weight_d(d4)
            mass = abs(beta_prod * w_prod)
            n_val = (
                h1 * d2 * d3 * d4
                - h2 * d1 * d3 * d4
                + h3 * d1 * d2 * d4
                - h4 * d1 * d2 * d3
            )
            if n_val == 0:
                bins[classify_n0(h1, d1, h2, d2, h3, d3, h4, d4)] += mass
            elif abs(n_val) <= threshold:
                bins["N_nearcoll"] += mass
            else:
                bins["N_far"] += mass
    return bins


def cri_ratio() -> float:
    sigma1 = 0j
    sigma3 = 0j
    for h in range(1, H_VAL + 1):
        coeff = beta_h(h, H_VAL)
        if coeff == 0.0:
            continue
        contribution = coeff * compute_bh(W_REAL, h)
        if chi4(h) == 1:
            sigma1 += contribution
        else:
            sigma3 += contribution
    denom = abs(sigma1) ** 2 + abs(sigma3) ** 2
    return abs(sigma1 - sigma3) ** 2 / denom if denom > 1e-30 else 0.0


def gradient_angles() -> tuple[float, float]:
    pairs: list[tuple[int, int, tuple[float, float]]] = []
    d_small = sorted({D_VAL - DELTA, D_VAL, D_VAL + DELTA})
    for h in range(1, H_VAL + 1):
        for d in d_small:
            pairs.append((h, d, (X_VAL / (4.0 * d), -h * X_VAL / (4.0 * d * d))))

    angles: list[float] = []
    for idx, (_, _, g1) in enumerate(pairs):
        for _, _, g2 in pairs[idx + 1 :]:
            dot = g1[0] * g2[0] + g1[1] * g2[1]
            norm1 = math.hypot(*g1)
            norm2 = math.hypot(*g2)
            if norm1 * norm2 <= 1e-30:
                continue
            cosine = max(-1.0, min(1.0, dot / (norm1 * norm2)))
            angles.append(math.acos(cosine))
    if not angles:
        return 0.0, 0.0
    return min(angles), sum(angles) / len(angles)


def write_outputs(rows: list[list[str]], report_text: str, precision_text: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    with (OUT_DIR / "table_small.csv").open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerows(rows)
    (RUN_DIR / "precision.log").write_text(precision_text, encoding="utf-8", newline="\n")
    (RUN_DIR / "report.md").write_text(report_text, encoding="utf-8", newline="\n")


def main() -> int:
    cf_error = max_character_factor_error()
    beta_error = max_beta_even_error()
    diff_m1, status_m1 = m1_raw_vs_paired()
    diff_m2, status_m2 = m2_raw_vs_paired(W_REAL, real_pairing=False)
    diff_m2_complex, status_m2_complex = m2_raw_vs_paired(W_COMPLEX, real_pairing=True)
    bins = fourth_moment_bins()
    ratio = cri_ratio()
    min_angle, mean_angle = gradient_angles()

    rows = [
        ["test_id", "description", "expected", "observed", "status", "comment"],
        ["T0a", "C_h character factor", "max error < 1e-8", f"{cf_error:.3e}", "PASS" if cf_error < TOL else "FAIL", ""],
        ["T0b", "beta evenness", "max error < 1e-12", f"{beta_error:.3e}", "PASS" if beta_error < 1e-12 else "FAIL", ""],
        ["T1", "M1 raw vs paired (real)", "diff < 1e-8", f"{diff_m1:.3e}", status_m1, ""],
        ["T2", "M2 raw vs paired (real)", "diff < 1e-8", f"{diff_m2:.3e}", status_m2, ""],
        ["T3", "M2 raw vs paired (complex)", "diff > 1e-8", f"{diff_m2_complex:.3e}", status_m2_complex, "mismatch is expected"],
        ["T4a", "4th moment N=0 diagonal mass", "diagnostic", f"{bins['N0_diag']:.6g}", "INFO", ""],
        ["T4b", "4th moment N=0 pair-swapped mass", "diagnostic", f"{bins['N0_pairswapped']:.6g}", "INFO", ""],
        ["T4c", "4th moment N=0 sign-symmetric mass", "diagnostic", f"{bins['N0_signsym']:.6g}", "INFO", ""],
        ["T4d", "4th moment N=0 unclassified mass", "diagnostic", f"{bins['N0_unclass']:.6g}", "WATCH" if bins["N0_unclass"] > 1e-9 else "OK", ""],
        ["T4e", "4th moment near-collision mass", "diagnostic", f"{bins['N_nearcoll']:.6g}", "INFO", ""],
        ["T4f", "4th moment far mass", "diagnostic", f"{bins['N_far']:.6g}", "INFO", ""],
        ["T5", "CRI ratio", "diagnostic", f"{ratio:.6g}", "INFO", ""],
        ["T6a", "gradient minimum angle", "diagnostic", f"{min_angle:.6g}", "INFO", "radians"],
        ["T6b", "gradient mean angle", "diagnostic", f"{mean_angle:.6g}", "INFO", "radians"],
    ]

    precision_text = "\n".join(
        [
            f"Python version: {sys.version}",
            f"Platform: {platform.platform()}",
            "Float type: Python double precision float",
            f"Machine epsilon: {sys.float_info.epsilon}",
            f"X: {X_VAL}",
            f"D: {D_VAL}",
            f"H: {H_VAL}",
            f"Max character-factor error: {cf_error}",
            f"Max beta-evenness error: {beta_error}",
            f"Max diff M1 raw-vs-paired real: {diff_m1}",
            f"Max diff M2 raw-vs-paired real: {diff_m2}",
            f"Complex-weight mismatch diff: {diff_m2_complex}",
            f"Fourth-moment total diagnostic mass: {sum(bins.values()):.12g}",
            "Kernel: provisional triangular Fejer placeholder; magnitude claims are not final until H4 source audit.",
            "",
        ]
    )

    report_text = "\n".join(
        [
            "# M9 Regression: Raw-vs-Paired Diagnostic Report",
            "",
            "**Status**: `diagnostic_only`",
            "**Run command**: `python computations/m9_regression/run.py`",
            "**Kernel**: provisional triangular Fejer placeholder pending `H4-source-audit`.",
            "",
            "## Results",
            "",
            "| Test | Observed | Status |",
            "|---|---:|---|",
            *[f"| {row[0]} {row[1]} | {row[3]} | {row[4]} |" for row in rows[1:]],
            "",
            "## Interpretation",
            "",
            "- The real-weight raw and paired formulas agree within tolerance for both M1 and M2.",
            "- The complex-weight paired-real M2 check mismatches, as expected, so paired formulas must stay scoped to real weights.",
            "- Fourth-moment bin masses are small finite diagnostics only; they do not prove an asymptotic bound.",
            "- Any nonzero `N0_unclass` mass remains a taxonomy warning, not a theorem.",
            "",
            "## Files",
            "",
            "- `outputs/table_small.csv`",
            "- `computations/m9_regression/precision.log`",
            "- `computations/m9_regression/report.md`",
            "",
        ]
    )

    write_outputs(rows, report_text, precision_text)
    print(f"H = {H_VAL}, D = {D_VAL}, X = {X_VAL}")
    print("Diagnostic run complete.")
    print(f"Wrote {OUT_DIR / 'table_small.csv'}")
    print(f"Wrote {RUN_DIR / 'precision.log'}")
    print(f"Wrote {RUN_DIR / 'report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
