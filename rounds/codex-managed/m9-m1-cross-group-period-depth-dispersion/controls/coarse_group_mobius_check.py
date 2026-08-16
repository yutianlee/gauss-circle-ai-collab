"""Diagnostic-only finite check of the Round-88 coarse-group lattice."""

from itertools import product
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_power_factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            q = 1
            while n % p == 0:
                n //= p
                q *= p
            out.append(q)
        p += 1
    if n > 1:
        out.append(n)
    return out


def group_label(pair, modulus):
    x, y = pair
    label = []
    for q in prime_power_factors(modulus):
        xq, yq = x % q, y % q
        if xq == yq:
            label.append((q, "D"))
        else:
            label.append((q, "A", xq, yq))
    return tuple(label)


def check(M):
    units = [x for x in range(M) if gcd(x, M) == 1]
    pairs = [(x, y) for x in units for y in units if x != y]
    ds = divisors(M)

    exact = {R: 0 for R in ds}
    for P, P2 in product(pairs, repeat=2):
        admissible_m = [m for m in ds if group_label(P, m) == group_label(P2, m)]
        m_star = max(admissible_m)
        exact[M // m_star] += 1

    for R in ds:
        m = M // R
        groups = {}
        for P in pairs:
            groups.setdefault(group_label(P, m), 0)
            groups[group_label(P, m)] += 1
        coarse = sum(v * v for v in groups.values())
        asserted = sum(exact[s] for s in ds if R % s == 0)
        if coarse != asserted:
            raise AssertionError((M, R, coarse, asserted))
        if coarse > M * M * R * R:
            raise AssertionError(("count", M, R, coarse, M * M * R * R))
    return len(pairs), exact


if __name__ == "__main__":
    for modulus in (12, 18, 27, 40, 72):
        count, shells = check(modulus)
        print(modulus, count, shells)

    q = 27
    x = 2
    p1 = ((x - 1) % q, x)
    p2 = ((x - (1 + q // 3)) % q, x)
    assert group_label(p1, q) != group_label(p2, q)
    assert group_label(p1, q // 3) == group_label(p2, q // 3)
    print("hostile_R3", p1, p2, group_label(p1, q // 3))
