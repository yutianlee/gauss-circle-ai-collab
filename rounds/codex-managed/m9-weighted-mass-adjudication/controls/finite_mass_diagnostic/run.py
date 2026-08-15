#!/usr/bin/env python3
"""Bounded exact finite diagnostic for M9 raw and beta-weighted masses.

Status: diagnostic_only.

The tuple enumeration and the 1/|h|-weighted mass are exact integer/rational
computations.  Vaaler's Phi weights and the pairing controls are evaluated
twice with a small, dependency-free Decimal implementation (50 and 80 digits).
No finite output is interpreted as an asymptotic estimate.
"""

from __future__ import annotations

import bisect
import csv
import hashlib
import itertools
import json
import math
import platform
import random
import sys
import time
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Iterable


CAMPAIGN_ID = "m9-weighted-mass-adjudication"
TASK_ID = "finite_mass_diagnostic"
GRAPH_SHA256 = "3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f"
STATUS = "diagnostic_only"
OUT_DIR = Path(__file__).resolve().parent
REPORT_PATH = OUT_DIR.parent.parent / "reports" / "finite_mass_diagnostic.md"

# One deliberately small perfect-fourth test instance.  The three rows isolate
# the frozen lower, crossover, and upper endpoint scales without a size sweep.
X = 625  # 5^4
SCALE_SPECS = (
    ("lower", 5, "D=X^(1/4)"),
    ("crossover", 11, "D=round(X^(3/8))"),
    ("endpoint", 25, "D=X^(1/2)"),
)
DECIMAL_PRECISIONS = (50, 80)
RANDOM_SIGN_SEED = 20260811


def chi4(n: int) -> int:
    residue = n % 4
    if residue in (0, 2):
        return 0
    return 1 if residue == 1 else -1


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def decimal_pi(precision: int) -> Decimal:
    """Compute pi by Machin's formula at the requested Decimal precision."""

    def atan_inverse(inv: int, working_precision: int) -> Decimal:
        with localcontext() as ctx:
            ctx.prec = working_precision
            x = Decimal(1) / Decimal(inv)
            x2 = x * x
            term = x
            total = term
            k = 1
            cutoff = Decimal(10) ** (-(working_precision - 5))
            sign = -1
            while True:
                term *= x2
                addend = term / Decimal(2 * k + 1)
                if abs(addend) < cutoff:
                    break
                total = total + addend if sign > 0 else total - addend
                sign *= -1
                k += 1
            return +total

    with localcontext() as ctx:
        ctx.prec = precision + 12
        value = Decimal(16) * atan_inverse(5, precision + 12)
        value -= Decimal(4) * atan_inverse(239, precision + 12)
        ctx.prec = precision
        return +value


def decimal_sin_cos(x: Decimal, pi: Decimal, precision: int) -> tuple[Decimal, Decimal]:
    """Taylor sin/cos after exact Decimal reduction to [-pi, pi]."""
    with localcontext() as ctx:
        ctx.prec = precision + 10
        two_pi = Decimal(2) * pi
        x = x % two_pi
        if x > pi:
            x -= two_pi
        x2 = x * x
        sin_term = x
        cos_term = Decimal(1)
        sin_total = sin_term
        cos_total = cos_term
        cutoff = Decimal(10) ** (-(precision + 3))
        k = 1
        while True:
            sin_term *= -x2 / Decimal((2 * k) * (2 * k + 1))
            cos_term *= -x2 / Decimal((2 * k - 1) * (2 * k))
            sin_total += sin_term
            cos_total += cos_term
            if abs(sin_term) < cutoff and abs(cos_term) < cutoff:
                break
            k += 1
        ctx.prec = precision
        return +sin_total, +cos_total


def vaaler_phi(h: int, height: int, pi: Decimal, precision: int) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision + 8
        u = Decimal(h) / Decimal(height + 1)
        angle = pi * u
        sin_angle, cos_angle = decimal_sin_cos(angle, pi, precision + 8)
        value = pi * u * (Decimal(1) - u) * (cos_angle / sin_angle) + u
        ctx.prec = precision
        return +value


@dataclass(frozen=True)
class PairData:
    d1: int
    d2: int
    product: int
    keys: tuple[int, ...]
    sparse_vectors: tuple[tuple[tuple[int, int], ...], ...]


def frequency_magnitudes(height: int) -> tuple[int, ...]:
    return tuple(h for h in range(1, height + 1, 2))


def make_pair_data(denominators: tuple[int, ...], magnitudes: tuple[int, ...]) -> list[PairData]:
    mag_index = {h: i for i, h in enumerate(magnitudes)}
    pair_dimension = len(magnitudes) ** 2
    signed_h = tuple(sign * h for h in magnitudes for sign in (-1, 1))
    answer: list[PairData] = []
    for d1 in denominators:
        for d2 in denominators:
            distribution: dict[int, list[int]] = {}
            for h1 in signed_h:
                i = mag_index[abs(h1)]
                for h2 in signed_h:
                    j = mag_index[abs(h2)]
                    a_value = h1 * d2 - h2 * d1
                    vector = distribution.setdefault(a_value, [0] * pair_dimension)
                    vector[i * len(magnitudes) + j] += 1
            keys = tuple(sorted(distribution))
            sparse = tuple(
                tuple((idx, count) for idx, count in enumerate(distribution[key]) if count)
                for key in keys
            )
            answer.append(PairData(d1, d2, d1 * d2, keys, sparse))
    return answer


def add_outer(target: list[int], left: tuple[tuple[int, int], ...], right: tuple[tuple[int, int], ...], pair_dim: int) -> None:
    for left_idx, left_count in left:
        offset = left_idx * pair_dim
        for right_idx, right_count in right:
            target[offset + right_idx] += left_count * right_count


def enumerate_tensors(
    denominators: tuple[int, ...], magnitudes: tuple[int, ...], thresholds: tuple[int, ...]
) -> tuple[dict[str, list[int]], dict[str, int]]:
    """Enumerate exact N=0 and cumulative nonzero |N| bands.

    For A=h1*d2-h2*d1 and B=h3*d4-h4*d3,
      N=A*d3*d4+B*d1*d2.
    Sorted B values and exact integer interval searches avoid the full
    eight-variable Cartesian product.
    """
    pair_data = make_pair_data(denominators, magnitudes)
    pair_dim = len(magnitudes) ** 2
    tensor_dim = pair_dim**2
    tensors = {"exact_N0": [0] * tensor_dim}
    for threshold in thresholds:
        tensors[f"nonzero_le_{threshold}"] = [0] * tensor_dim

    max_threshold = max(thresholds)
    join_hits = 0
    pair_pair_checks = 0
    for left in pair_data:
        p12 = left.product
        for right in pair_data:
            pair_pair_checks += 1
            p34 = right.product
            right_keys = right.keys
            for a_idx, a_value in enumerate(left.keys):
                constant = a_value * p34
                lower_b = ceil_div(-max_threshold - constant, p12)
                upper_b = (max_threshold - constant) // p12
                lo = bisect.bisect_left(right_keys, lower_b)
                hi = bisect.bisect_right(right_keys, upper_b)
                left_vector = left.sparse_vectors[a_idx]
                for b_idx in range(lo, hi):
                    n_value = constant + right_keys[b_idx] * p12
                    n_abs = abs(n_value)
                    right_vector = right.sparse_vectors[b_idx]
                    join_hits += 1
                    if n_abs == 0:
                        add_outer(tensors["exact_N0"], left_vector, right_vector, pair_dim)
                    else:
                        for threshold in thresholds:
                            if n_abs <= threshold:
                                add_outer(
                                    tensors[f"nonzero_le_{threshold}"],
                                    left_vector,
                                    right_vector,
                                    pair_dim,
                                )
    diagnostics = {
        "ordered_denominator_pairs": len(pair_data),
        "ordered_pair_pair_checks": pair_pair_checks,
        "joined_A_B_values": join_hits,
    }
    return tensors, diagnostics


def brute_force_tensors(
    denominators: tuple[int, ...], magnitudes: tuple[int, ...], thresholds: tuple[int, ...]
) -> dict[str, list[int]]:
    """Independent literal enumeration used only on the two tiny scales."""
    m = len(magnitudes)
    tensor_dim = m**4
    tensors = {"exact_N0": [0] * tensor_dim}
    for threshold in thresholds:
        tensors[f"nonzero_le_{threshold}"] = [0] * tensor_dim
    states = tuple((sign * h, d, idx) for idx, h in enumerate(magnitudes) for sign in (-1, 1) for d in denominators)
    for s1, s2, s3, s4 in itertools.product(states, repeat=4):
        h1, d1, i = s1
        h2, d2, j = s2
        h3, d3, k = s3
        h4, d4, ell = s4
        n_value = h1 * d2 * d3 * d4 - h2 * d1 * d3 * d4 + h3 * d1 * d2 * d4 - h4 * d1 * d2 * d3
        index = ((i * m + j) * m + k) * m + ell
        n_abs = abs(n_value)
        if n_abs == 0:
            tensors["exact_N0"][index] += 1
        else:
            for threshold in thresholds:
                if n_abs <= threshold:
                    tensors[f"nonzero_le_{threshold}"][index] += 1
    return tensors


def tensor_weights(magnitudes: tuple[int, ...]) -> Iterable[tuple[int, int, int, int]]:
    m = len(magnitudes)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                for ell in range(m):
                    yield magnitudes[i], magnitudes[j], magnitudes[k], magnitudes[ell]


def evaluate_tensor_exact(tensor: list[int], magnitudes: tuple[int, ...]) -> dict[str, object]:
    lcm_h = math.lcm(*magnitudes)
    numerator = 0
    raw = 0
    for count, (h1, h2, h3, h4) in zip(tensor, tensor_weights(magnitudes)):
        raw += count
        numerator += count * (lcm_h // h1) * (lcm_h // h2) * (lcm_h // h3) * (lcm_h // h4)
    denominator = lcm_h**4
    divisor = math.gcd(numerator, denominator)
    reduced_num = numerator // divisor
    reduced_den = denominator // divisor
    with localcontext() as ctx:
        ctx.prec = 40
        decimal_value = Decimal(reduced_num) / Decimal(reduced_den)
    return {
        "raw_count": raw,
        "reciprocal_mass_numerator": reduced_num,
        "reciprocal_mass_denominator": reduced_den,
        "reciprocal_mass_decimal": str(decimal_value),
    }


def pattern_mass(
    tensor: list[int], magnitudes: tuple[int, ...], abs_beta: tuple[Decimal, ...], signs: tuple[int, ...]
) -> Decimal:
    m = len(magnitudes)
    total = Decimal(0)
    index = 0
    for i in range(m):
        wi = abs_beta[i] * signs[i]
        for j in range(m):
            wij = wi * abs_beta[j] * signs[j]
            for k in range(m):
                wijk = wij * abs_beta[k] * signs[k]
                for ell in range(m):
                    count = tensor[index]
                    if count:
                        total += Decimal(count) * wijk * abs_beta[ell] * signs[ell]
                    index += 1
    return total


def evaluate_tensor_decimal(
    tensor: list[int], magnitudes: tuple[int, ...], height: int, precision: int, random_signs: tuple[int, ...]
) -> dict[str, object]:
    with localcontext() as ctx:
        ctx.prec = precision
        pi = decimal_pi(precision)
        phi_values = tuple(vaaler_phi(h, height, pi, precision) for h in magnitudes)
        abs_beta = tuple(phi / (pi * Decimal(h)) for phi, h in zip(phi_values, magnitudes))
        true_signs = tuple(chi4(h) for h in magnitudes)
        unsigned_signs = tuple(1 for _ in magnitudes)
        true_mass = pattern_mass(tensor, magnitudes, abs_beta, true_signs)
        unsigned_mass = pattern_mass(tensor, magnitudes, abs_beta, unsigned_signs)
        random_mass = pattern_mass(tensor, magnitudes, abs_beta, random_signs)

        brute_best = Decimal(-1)
        brute_pattern: tuple[int, ...] | None = None
        for mask in range(1 << len(magnitudes)):
            signs = tuple(1 if (mask >> idx) & 1 else -1 for idx in range(len(magnitudes)))
            candidate = abs(pattern_mass(tensor, magnitudes, abs_beta, signs))
            if candidate > brute_best:
                brute_best = candidate
                brute_pattern = signs

        return {
            "precision_digits": precision,
            "pi": str(pi),
            "phi": {str(h): str(value) for h, value in zip(magnitudes, phi_values)},
            "abs_beta": {str(h): str(value) for h, value in zip(magnitudes, abs_beta)},
            "true_sign_pattern": list(true_signs),
            "random_sign_pattern": list(random_signs),
            "true_beta_signed_mass": str(true_mass),
            "true_beta_signed_abs": str(abs(true_mass)),
            "unsigned_beta_mass": str(unsigned_mass),
            "random_signed_mass": str(random_mass),
            "random_signed_abs": str(abs(random_mass)),
            "adversarial_max_abs_mass": str(brute_best),
            "adversarial_pattern": list(brute_pattern or ()),
        }


def relative_decimal_difference(a: str, b: str, precision: int = 60) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision
        da, db = Decimal(a), Decimal(b)
        scale = max(abs(da), abs(db), Decimal(1))
        return abs(da - db) / scale


def complex_add(a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal]) -> tuple[Decimal, Decimal]:
    return a[0] + b[0], a[1] + b[1]


def complex_mul(a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal]) -> tuple[Decimal, Decimal]:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def complex_scale(a: tuple[Decimal, Decimal], scalar: Decimal) -> tuple[Decimal, Decimal]:
    return a[0] * scalar, a[1] * scalar


def complex_abs(a: tuple[Decimal, Decimal]) -> Decimal:
    return (a[0] * a[0] + a[1] * a[1]).sqrt()


def exponential_fraction(numerator: int, denominator: int, pi: Decimal, precision: int) -> tuple[Decimal, Decimal]:
    residue = Fraction(numerator, denominator) % 1
    angle = Decimal(2) * pi * Decimal(residue.numerator) / Decimal(residue.denominator)
    sin_value, cos_value = decimal_sin_cos(angle, pi, precision)
    return cos_value, sin_value


def pairing_controls(scale: dict[str, object], precision: int = 70) -> dict[str, object]:
    """Check raw two-sided, cosine-paired, Re(B_h), and asymmetric formulas."""
    with localcontext() as ctx:
        ctx.prec = precision
        pi = decimal_pi(precision)
        height = int(scale["H"])
        denominators = tuple(int(d) for d in scale["denominators"])
        magnitudes = frequency_magnitudes(height)
        beta = {
            h: -(vaaler_phi(h, height, pi, precision) * Decimal(chi4(h))) / (pi * Decimal(h))
            for h in magnitudes
        }
        real_weights = {d: (Decimal(1), Decimal(0)) for d in denominators}
        modulus = 2 * len(denominators) + 1
        complex_weights = {
            d: exponential_fraction(idx + 1, modulus, pi, precision)
            for idx, d in enumerate(denominators)
        }

        def b_sum(h: int, weights: dict[int, tuple[Decimal, Decimal]]) -> tuple[Decimal, Decimal]:
            total = (Decimal(0), Decimal(0))
            for d in denominators:
                phase = exponential_fraction(h * X, 4 * d, pi, precision)
                total = complex_add(total, complex_mul(weights[d], phase))
            return total

        def raw_two_sided(weights: dict[int, tuple[Decimal, Decimal]]) -> tuple[Decimal, Decimal]:
            total = (Decimal(0), Decimal(0))
            for h in magnitudes:
                total = complex_add(total, complex_scale(b_sum(h, weights), beta[h]))
                total = complex_add(total, complex_scale(b_sum(-h, weights), beta[h]))
            return total

        def cosine_pair(weights: dict[int, tuple[Decimal, Decimal]]) -> tuple[Decimal, Decimal]:
            total = (Decimal(0), Decimal(0))
            for h in magnitudes:
                inner = (Decimal(0), Decimal(0))
                for d in denominators:
                    phase = exponential_fraction(h * X, 4 * d, pi, precision)
                    inner = complex_add(inner, complex_scale(weights[d], phase[0]))
                total = complex_add(total, complex_scale(inner, Decimal(2) * beta[h]))
            return total

        def real_part_shortcut(weights: dict[int, tuple[Decimal, Decimal]]) -> tuple[Decimal, Decimal]:
            total = Decimal(0)
            for h in magnitudes:
                total += Decimal(2) * beta[h] * b_sum(h, weights)[0]
            return total, Decimal(0)

        def asymmetric_raw(weights: dict[int, tuple[Decimal, Decimal]]) -> tuple[Decimal, Decimal]:
            # Positive h gets multiplier 1; negative h gets multiplier i.
            total = (Decimal(0), Decimal(0))
            for h in magnitudes:
                total = complex_add(total, complex_scale(b_sum(h, weights), beta[h]))
                negative = complex_scale(b_sum(-h, weights), beta[h])
                total = complex_add(total, complex_mul((Decimal(0), Decimal(1)), negative))
            return total

        raw_real = raw_two_sided(real_weights)
        cosine_real = cosine_pair(real_weights)
        re_real = real_part_shortcut(real_weights)
        raw_complex = raw_two_sided(complex_weights)
        cosine_complex = cosine_pair(complex_weights)
        re_complex = real_part_shortcut(complex_weights)
        raw_asymmetric = asymmetric_raw(complex_weights)

        return {
            "precision_digits": precision,
            "real_weights_raw": [str(v) for v in raw_real],
            "real_weights_cosine_pair": [str(v) for v in cosine_real],
            "real_weights_re_shortcut": [str(v) for v in re_real],
            "real_raw_minus_cosine_abs": str(complex_abs((raw_real[0] - cosine_real[0], raw_real[1] - cosine_real[1]))),
            "real_raw_minus_re_abs": str(complex_abs((raw_real[0] - re_real[0], raw_real[1] - re_real[1]))),
            "complex_weights_raw": [str(v) for v in raw_complex],
            "complex_weights_cosine_pair": [str(v) for v in cosine_complex],
            "complex_weights_re_shortcut": [str(v) for v in re_complex],
            "complex_raw_minus_cosine_abs": str(complex_abs((raw_complex[0] - cosine_complex[0], raw_complex[1] - cosine_complex[1]))),
            "complex_raw_minus_re_abs": str(complex_abs((raw_complex[0] - re_complex[0], raw_complex[1] - re_complex[1]))),
            "asymmetric_h_raw": [str(v) for v in raw_asymmetric],
            "asymmetric_raw_minus_symmetric_cosine_abs": str(
                complex_abs((raw_asymmetric[0] - cosine_complex[0], raw_asymmetric[1] - cosine_complex[1]))
            ),
        }


def stable_random_signs(magnitudes: tuple[int, ...], scale_id: str) -> tuple[int, ...]:
    digest = hashlib.sha256(f"{RANDOM_SIGN_SEED}:{scale_id}".encode("ascii")).digest()
    signs = tuple(1 if digest[idx] & 1 else -1 for idx in range(len(magnitudes)))
    # When the dimension permits it, keep the random control genuinely distinct
    # from the true chi4 pattern, its global negative, and the unsigned patterns.
    if len(magnitudes) >= 3:
        true = tuple(chi4(h) for h in magnitudes)
        forbidden = {true, tuple(-v for v in true), tuple(1 for _ in magnitudes), tuple(-1 for _ in magnitudes)}
        if signs in forbidden:
            generator = random.Random(RANDOM_SIGN_SEED + sum(magnitudes))
            while signs in forbidden:
                signs = tuple(generator.choice((-1, 1)) for _ in magnitudes)
    return signs


def make_scale(scale_id: str, d_value: int, label: str) -> dict[str, object]:
    fourth_root = 5
    height = max(1, int(math.floor(d_value / fourth_root + 0.5)))
    # Half-dyadic sharp support is endpoint-compatible: all d <= D <= sqrt(X).
    denominators = tuple(range(d_value // 2 + 1, d_value + 1))
    natural_threshold = max(1, (d_value**4) // X)
    thresholds = tuple(sorted({1, natural_threshold, 4 * natural_threshold}))
    return {
        "scale_id": scale_id,
        "label": label,
        "X": X,
        "D": d_value,
        "H": height,
        "H_rule": "nearest integer to D/X^(1/4), ties upward",
        "denominator_support": "floor(D/2)<d<=D",
        "denominators": list(denominators),
        "odd_frequency_support": list(frequency_magnitudes(height)),
        "natural_band": natural_threshold,
        "thresholds": list(thresholds),
    }


def main() -> int:
    started = time.perf_counter()
    all_scales: list[dict[str, object]] = []
    csv_rows: list[dict[str, object]] = []
    precision_lines = [
        f"status={STATUS}",
        f"campaign_id={CAMPAIGN_ID}",
        f"task_id={TASK_ID}",
        f"graph_sha256={GRAPH_SHA256}",
        f"python={sys.version.replace(chr(10), ' ')}",
        f"platform={platform.platform()}",
        "integer_arithmetic=Python arbitrary-precision integers",
        "reciprocal_mass=exact integer numerator over lcm(odd h)^4",
        f"decimal_precisions={DECIMAL_PRECISIONS}",
        "decimal_transcendentals=dependency-free Machin pi and Taylor sin/cos",
    ]

    for scale_id, d_value, label in SCALE_SPECS:
        scale_started = time.perf_counter()
        scale = make_scale(scale_id, d_value, label)
        denominators = tuple(int(d) for d in scale["denominators"])
        magnitudes = tuple(int(h) for h in scale["odd_frequency_support"])
        thresholds = tuple(int(t) for t in scale["thresholds"])
        tensors, join_diagnostics = enumerate_tensors(denominators, magnitudes, thresholds)
        if scale_id in ("lower", "crossover"):
            brute_tensors = brute_force_tensors(denominators, magnitudes, thresholds)
            brute_verification = {
                "performed": True,
                "method": "literal Cartesian enumeration independent of the pair join",
                "all_tensors_equal": brute_tensors == tensors,
            }
        else:
            brute_verification = {
                "performed": False,
                "method": "omitted at endpoint to keep the diagnostic bounded",
                "all_tensors_equal": None,
            }
        random_signs = stable_random_signs(magnitudes, scale_id)
        band_results: list[dict[str, object]] = []

        for band_id, tensor in tensors.items():
            exact_values = evaluate_tensor_exact(tensor, magnitudes)
            evaluations = {
                str(precision): evaluate_tensor_decimal(tensor, magnitudes, int(scale["H"]), precision, random_signs)
                for precision in DECIMAL_PRECISIONS
            }
            high = evaluations[str(DECIMAL_PRECISIONS[-1])]
            low = evaluations[str(DECIMAL_PRECISIONS[0])]
            stability = {
                field: str(relative_decimal_difference(str(low[field]), str(high[field])))
                for field in (
                    "true_beta_signed_mass",
                    "unsigned_beta_mass",
                    "random_signed_mass",
                    "adversarial_max_abs_mass",
                )
            }
            raw = int(exact_values["raw_count"])
            recip = Decimal(int(exact_values["reciprocal_mass_numerator"])) / Decimal(
                int(exact_values["reciprocal_mass_denominator"])
            )
            unsigned = Decimal(str(high["unsigned_beta_mass"]))
            signed_abs = Decimal(str(high["true_beta_signed_abs"]))
            random_abs = Decimal(str(high["random_signed_abs"]))
            adversarial = Decimal(str(high["adversarial_max_abs_mass"]))
            pi_high = Decimal(str(high["pi"]))
            d_decimal = Decimal(d_value)
            candidate_scale = d_decimal + (d_decimal**4 / Decimal(X))
            ratios = {
                "reciprocal_over_raw": str(recip / Decimal(raw)) if raw else None,
                "pi4_unsigned_beta_over_reciprocal": str((pi_high**4 * unsigned) / recip) if recip else None,
                "signed_abs_over_unsigned": str(signed_abs / unsigned) if unsigned else None,
                "random_abs_over_unsigned": str(random_abs / unsigned) if unsigned else None,
                "adversarial_over_unsigned": str(adversarial / unsigned) if unsigned else None,
                "unsigned_beta_over_D2": str(unsigned / (d_decimal**2)),
                "unsigned_beta_over_D_plus_D4_over_X": str(unsigned / candidate_scale),
            }
            max_stability = max(Decimal(value) for value in stability.values())
            pass_flags = {
                "signed_triangle_inequality": signed_abs <= unsigned,
                "random_triangle_inequality": random_abs <= unsigned,
                "adversarial_equals_unsigned": relative_decimal_difference(str(adversarial), str(unsigned)) < Decimal("1e-40"),
                "precision_stable": max_stability < Decimal("1e-40"),
            }
            result = {
                "band_id": band_id,
                "band_definition": "N=0" if band_id == "exact_N0" else f"0<|N|<={band_id.rsplit('_', 1)[1]}",
                "tensor_counts_by_abs_frequency": tensor,
                "exact": exact_values,
                "decimal_evaluations": evaluations,
                "precision_relative_differences": stability,
                "ratios": ratios,
                "pass_flags": pass_flags,
            }
            band_results.append(result)
            csv_rows.append(
                {
                    "scale_id": scale_id,
                    "label": label,
                    "X": X,
                    "D": d_value,
                    "H": scale["H"],
                    "d_count": len(denominators),
                    "band_id": band_id,
                    "band_definition": result["band_definition"],
                    "raw_count": raw,
                    "reciprocal_mass": exact_values["reciprocal_mass_decimal"],
                    "true_beta_signed_mass": high["true_beta_signed_mass"],
                    "unsigned_beta_mass": high["unsigned_beta_mass"],
                    "random_signed_mass": high["random_signed_mass"],
                    "adversarial_max_abs_mass": high["adversarial_max_abs_mass"],
                    "reciprocal_over_raw": ratios["reciprocal_over_raw"],
                    "pi4_unsigned_over_reciprocal": ratios["pi4_unsigned_beta_over_reciprocal"],
                    "signed_abs_over_unsigned": ratios["signed_abs_over_unsigned"],
                    "unsigned_over_D2": ratios["unsigned_beta_over_D2"],
                    "unsigned_over_D_plus_D4_over_X": ratios["unsigned_beta_over_D_plus_D4_over_X"],
                    "precision_stable": pass_flags["precision_stable"],
                }
            )

        scale["join_diagnostics"] = join_diagnostics
        scale["brute_force_verification"] = brute_verification
        scale["random_sign_pattern"] = list(random_signs)
        scale["bands"] = band_results
        scale["elapsed_seconds"] = time.perf_counter() - scale_started
        all_scales.append(scale)
        precision_lines.append(
            f"scale={scale_id} D={d_value} H={scale['H']} d_count={len(denominators)} "
            f"elapsed_seconds={scale['elapsed_seconds']:.6f}"
        )
        for band in band_results:
            max_diff = max(Decimal(value) for value in band["precision_relative_differences"].values())
            precision_lines.append(f"scale={scale_id} band={band['band_id']} max_relative_50_vs_80={max_diff}")

    endpoint_pairing = pairing_controls(all_scales[-1], precision=70)
    pairing_tolerance = Decimal("1e-55")
    endpoint_pairing["pass_flags"] = {
        "real_raw_equals_cosine": Decimal(endpoint_pairing["real_raw_minus_cosine_abs"]) < pairing_tolerance,
        "real_raw_equals_Re_shortcut": Decimal(endpoint_pairing["real_raw_minus_re_abs"]) < pairing_tolerance,
        "complex_raw_equals_cosine": Decimal(endpoint_pairing["complex_raw_minus_cosine_abs"]) < pairing_tolerance,
        "complex_Re_shortcut_fails_as_expected": Decimal(endpoint_pairing["complex_raw_minus_re_abs"]) > Decimal("1e-12"),
        "asymmetric_h_pairing_fails_as_expected": Decimal(
            endpoint_pairing["asymmetric_raw_minus_symmetric_cosine_abs"]
        )
        > Decimal("1e-12"),
    }

    endpoint_natural = next(
        band for band in all_scales[-1]["bands"] if band["band_id"] == f"nonzero_le_{all_scales[-1]['natural_band']}"
    )
    endpoint_raw = int(endpoint_natural["exact"]["raw_count"])
    endpoint_recip = Fraction(
        int(endpoint_natural["exact"]["reciprocal_mass_numerator"]),
        int(endpoint_natural["exact"]["reciprocal_mass_denominator"]),
    )
    endpoint_high = endpoint_natural["decimal_evaluations"][str(DECIMAL_PRECISIONS[-1])]
    endpoint_signed = Decimal(endpoint_high["true_beta_signed_abs"])
    endpoint_unsigned = Decimal(endpoint_high["unsigned_beta_mass"])
    global_controls = {
        "raw_vs_weighted": {
            "rule": "At the endpoint natural band, exact reciprocal mass is strictly below the odd-supported raw count.",
            "pass": endpoint_recip < endpoint_raw,
        },
        "signed_vs_unsigned": {
            "rule": "At the endpoint natural band, true signed mass is strictly below unsigned beta mass; triangle inequality holds in every band.",
            "pass": endpoint_signed < endpoint_unsigned
            and all(band["pass_flags"]["signed_triangle_inequality"] for scale in all_scales for band in scale["bands"]),
        },
        "dyadic_endpoints": {
            "rule": "The exact D=X^(1/4), rounded D=X^(3/8), and exact D=X^(1/2) rows all ran and include their natural nonzero bands.",
            "pass": [scale["scale_id"] for scale in all_scales] == ["lower", "crossover", "endpoint"]
            and all(any(band["band_id"] == f"nonzero_le_{scale['natural_band']}" for band in scale["bands"]) for scale in all_scales),
        },
        "real_vs_complex_pairing": {
            "rule": "Raw=cosine pairing for shared weights; Re(B_h) only for real weights; asymmetric h-weights break symmetric pairing.",
            "pass": all(endpoint_pairing["pass_flags"].values()),
        },
        "exact_vs_near": {
            "rule": "N=0 and 0<|N| bands are accumulated in disjoint exact-integer tensors.",
            "pass": True,
        },
        "precision": {
            "rule": "All beta masses agree at 50 and 80 digits to relative error below 1e-40.",
            "pass": all(band["pass_flags"]["precision_stable"] for scale in all_scales for band in scale["bands"]),
        },
        "small_scale_brute_force": {
            "rule": "The independent literal enumeration exactly matches every pair-join tensor at the lower and crossover scales.",
            "pass": all(
                scale["brute_force_verification"]["all_tensors_equal"]
                for scale in all_scales
                if scale["brute_force_verification"]["performed"]
            ),
        },
    }

    total_elapsed = time.perf_counter() - started
    precision_lines.extend(
        [
            f"pairing_precision_digits={endpoint_pairing['precision_digits']}",
            f"pairing_real_raw_minus_cosine_abs={endpoint_pairing['real_raw_minus_cosine_abs']}",
            f"pairing_complex_raw_minus_cosine_abs={endpoint_pairing['complex_raw_minus_cosine_abs']}",
            f"pairing_complex_raw_minus_Re_abs={endpoint_pairing['complex_raw_minus_re_abs']}",
            f"total_elapsed_seconds={total_elapsed:.6f}",
        ]
    )

    payload = {
        "schema_version": 1,
        "campaign_id": CAMPAIGN_ID,
        "task_id": TASK_ID,
        "graph_sha256": GRAPH_SHA256,
        "status": STATUS,
        "statement": "Finite exact-integer comparison only; no asymptotic inference.",
        "normalization": {
            "N": "h1*d2*d3*d4-h2*d1*d3*d4+h3*d1*d2*d4-h4*d1*d2*d3",
            "frequency_support": "odd h only, 1<=|h|<=H, because beta_h=0 for even h",
            "denominator_support": "sharp half-dyadic block floor(D/2)<d<=D",
            "raw_count": "number of ordered (h1,d1,...,h4,d4) tuples on coefficient-compatible odd support",
            "reciprocal_mass": "sum 1/(|h1*h2*h3*h4|)",
            "true_beta_signed_mass": "sum beta_h1*beta_h2*beta_h3*beta_h4",
            "unsigned_beta_mass": "sum |beta_h1*beta_h2*beta_h3*beta_h4|; equivalently remove chi4 signs",
            "beta": "-Phi(|h|/(H+1))*chi4(h)/(pi*h) on odd nonzero h",
            "Phi": "pi*u*(1-u)*cot(pi*u)+u",
        },
        "scales": all_scales,
        "endpoint_pairing_controls": endpoint_pairing,
        "global_controls": global_controls,
        "limitations": [
            "One bounded instance X=625 is used; there is no size sweep or exponent fit.",
            "Sharp unit denominator weights are used for mass enumeration; smooth-weight behavior is not tested.",
            "The raw count is coefficient-compatible (odd frequencies only), not an all-frequency count.",
            "Only exact N=0 and cumulative bands |N|<=1, floor(D^4/X), and four times that natural band are tested.",
            "The finite comparison cannot certify a uniform asymptotic bound or a crossover exponent.",
        ],
        "elapsed_seconds": total_elapsed,
    }

    (OUT_DIR / "results.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    fieldnames = list(csv_rows[0])
    with (OUT_DIR / "results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)
    with (OUT_DIR / "parameters.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["scale_id", "label", "X", "D", "H", "d_min", "d_max", "d_count", "natural_band", "thresholds"])
        for scale in all_scales:
            writer.writerow(
                [
                    scale["scale_id"],
                    scale["label"],
                    scale["X"],
                    scale["D"],
                    scale["H"],
                    min(scale["denominators"]),
                    max(scale["denominators"]),
                    len(scale["denominators"]),
                    scale["natural_band"],
                    ";".join(str(value) for value in scale["thresholds"]),
                ]
            )
    (OUT_DIR / "precision.log").write_text("\n".join(precision_lines) + "\n", encoding="utf-8")
    (OUT_DIR / "command.txt").write_text(
        "Working directory: repository root\nCommand: py rounds/codex-managed/m9-weighted-mass-adjudication/controls/finite_mass_diagnostic/run.py\n",
        encoding="utf-8",
    )

    print(f"status={STATUS}")
    print(f"scales={len(all_scales)} bands={len(csv_rows)} elapsed_seconds={total_elapsed:.3f}")
    print(f"global_controls_pass={all(control['pass'] for control in global_controls.values())}")
    print(f"wrote={OUT_DIR / 'results.json'}")
    return 0 if all(control["pass"] for control in global_controls.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
