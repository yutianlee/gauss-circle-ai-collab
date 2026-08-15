"""Diagnostic-only finite check of the Round-70 odd-modulus residue identity."""

import cmath
import math


def chi4(n: int) -> int:
    residue = n % 4
    return 1 if residue == 1 else -1 if residue == 3 else 0


for modulus in (3, 5, 7, 9, 11):
    lam = (modulus * modulus - 1) // 4
    for numerator in range(1, modulus):
        if math.gcd(numerator, modulus) != 1:
            continue
        inverse = pow(numerator, -1, modulus)
        for h_dual in range(modulus):
            for k_dual in range(1, 4 * modulus, 2):
                lhs = 0j
                for x_residue in range(modulus):
                    for y_residue in range(4 * modulus):
                        lhs += chi4(y_residue) * cmath.exp(
                            2j
                            * math.pi
                            * x_residue
                            * (numerator * y_residue + h_dual)
                            / modulus
                        ) * cmath.exp(
                            2j * math.pi * k_dual * y_residue / (4 * modulus)
                        )
                rhs = (
                    2j
                    * modulus
                    * chi4(k_dual * modulus)
                    * cmath.exp(
                        2j
                        * math.pi
                        * lam
                        * k_dual
                        * h_dual
                        * inverse
                        / modulus
                    )
                )
                assert abs(lhs - rhs) < 1e-7, (
                    modulus,
                    numerator,
                    h_dual,
                    k_dual,
                    lhs,
                    rhs,
                )

print("odd-modulus residue identity: PASS")

