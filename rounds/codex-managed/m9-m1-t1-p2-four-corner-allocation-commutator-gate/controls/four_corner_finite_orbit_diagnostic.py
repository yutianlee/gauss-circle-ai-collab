from __future__ import annotations

from math import gcd, isqrt


def squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def chi4(n: int) -> int:
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def main() -> None:
    hits: list[tuple[object, ...]] = []
    for shell in (40, 60, 80, 120, 160, 240, 320):
        width = isqrt(shell) + (isqrt(shell) ** 2 < shell)
        found = False
        for g in range(1, 18, 2):
            for u in range(max(1, shell // (3 * g)), min(3 * shell // g, 250) + 1):
                if gcd(g, u) > 1:
                    continue
                for v in range(max(1, shell // 3), min(3 * shell, 500) + 1):
                    if gcd(u, v) > 1:
                        continue
                    for w in range(1, min(30, (shell - 1) // 2) + 1):
                        m = v + 2 * w
                        d = g * u
                        if not (
                            shell // 3 <= d <= 3 * shell
                            and shell // 3 <= m <= 3 * shell
                            and 4 * m < d < 16 * m
                        ):
                            continue
                        if gcd(d, m) > 1 or not squarefree(d * m):
                            continue
                        if g * abs(u - v - 2 * w) > width:
                            continue
                        for s in range(1, min(30, (shell - 1) // 2) + 1):
                            d_prime = g * (u + 2 * s)
                            m_prime = v
                            if not (
                                shell // 3 <= d_prime <= 3 * shell
                                and shell // 3 <= m_prime <= 3 * shell
                                and 4 * m_prime < d_prime < 16 * m_prime
                            ):
                                continue
                            if gcd(d_prime, m_prime) > 1 or not squarefree(
                                d_prime * m_prime
                            ):
                                continue
                            height = s * v - u * w
                            shift = 2 * g * height
                            if not (0 < shift < shell):
                                continue
                            if g * abs(u + 2 * s - v) <= width:
                                continue
                            alpha = u
                            beta = u + 2 * s
                            if (
                                gcd(m, beta) > 1
                                or gcd(alpha, m_prime) > 1
                                or gcd(m, m_prime) > 1
                            ):
                                continue
                            if chi4(alpha * m) != -1 or chi4(beta * m_prime) != -1:
                                continue
                            corners = (
                                (d, m, d_prime, m_prime),
                                (g * m, alpha, d_prime, m_prime),
                                (d, m, g * m_prime, beta),
                                (g * m, alpha, g * m_prime, beta),
                            )
                            if not all(
                                (upper_d - lower_d) * (upper_m - lower_m) < 0
                                for lower_d, lower_m, upper_d, upper_m in corners
                            ):
                                continue
                            hits.append(
                                (
                                    shell,
                                    width,
                                    g,
                                    u,
                                    v,
                                    w,
                                    s,
                                    height,
                                    shift,
                                    corners,
                                )
                            )
                            found = True
                            break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break

    print(f"hits={len(hits)}")
    for item in hits:
        print(item[:-1])
        print(item[-1])


if __name__ == "__main__":
    main()
