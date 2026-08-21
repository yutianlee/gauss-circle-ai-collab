from fractions import Fraction


def inv(z: int, p: int) -> int:
    return pow(z % p, -1, p)


def normalize(triple: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    if triple == (0, 0, 0):
        return triple
    for value in triple:
        if value % p:
            scale = inv(value, p)
            return tuple((scale * item) % p for item in triple)
    raise AssertionError("unreachable")


def allowed(a: int, b: int, v: int, p: int) -> list[int]:
    poles = {0, a % p, v % p, (v + b) % p}
    return [x for x in range(p) if x not in poles]


def derivative_zero(a: int, b: int, v: int, p: int) -> bool:
    domain = allowed(a, b, v, p)
    if not domain:
        return False
    for x in domain:
        value = (
            -inv(x, p) ** 2
            + inv(x - a, p) ** 2
            + inv(x - v, p) ** 2
            - inv(x - v - b, p) ** 2
        ) % p
        if value:
            return False
    return True


def main() -> None:
    expected_raw = {2: 1, 3: 15, 5: 25, 7: 13}
    expected_rays = {2: 1, 3: 8, 5: 7, 7: 3}
    for p in (2, 3, 5, 7):
        raw = []
        rays = set()
        for a in range(p):
            for b in range(p):
                for v in range(p):
                    if derivative_zero(a, b, v, p):
                        raw.append((a, b, v))
                        rays.add(normalize((a, b, v), p))
        assert len(raw) == expected_raw[p], (p, len(raw))
        assert len(rays) == expected_rays[p], (p, len(rays))
        print(f"p={p}: raw={len(raw)}, normalized={len(rays)}, rays={sorted(rays)}")

    # At the top first-band conductor B=J^(3/20), the full graph degree
    # is M^2=J^(3/10), whereas the target degree is rho_*^2=J^(2/15).
    full_degree = Fraction(3, 10)
    target_degree = Fraction(2, 15)
    assert full_degree - target_degree == Fraction(1, 6)
    print(f"top full-degree deficit: J^({full_degree - target_degree})")


if __name__ == "__main__":
    main()
