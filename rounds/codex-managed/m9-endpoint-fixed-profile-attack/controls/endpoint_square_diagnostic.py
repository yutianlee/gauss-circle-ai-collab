"""Diagnostic only: fixed-profile M2 blocks at X=4D^2.

This finite computation cannot prove an asymptotic estimate. It tests the
specific falsification hypothesis that the exact-square endpoint forces a
coherent block of size comparable to sqrt(D L).
"""

from __future__ import annotations

import math
import numpy as np


def phi(t: float) -> float:
    if not 0 < t < 1:
        return 0.0
    return math.pi * t * (1 - t) / math.tan(math.pi * t) + t


def run() -> None:
    for d_scale in (1024, 2048, 4096, 8192, 16384, 32768):
        x = 4 * d_scale * d_scale
        h_max = int(math.sqrt(d_scale / 2))
        denominators = np.arange(d_scale, 2 * d_scale, dtype=float)
        weight = np.sin(np.pi * (denominators / d_scale - 1)) ** 2
        for frequency in (4, 8, 16, 32, 64, 128):
            if 2 * frequency > h_max:
                continue
            values = np.zeros(len(denominators))
            for h in range(frequency, 2 * frequency):
                if h % 2 == 0:
                    continue
                chi4 = 1 if h % 4 == 1 else -1
                beta = -phi(h / (h_max + 1)) * chi4 / (math.pi * h)
                values += 2 * beta * np.cos(
                    2 * math.pi * h * x / (4 * denominators)
                )
            block = float(np.sum(weight * values))
            print(
                f"D={d_scale:6d} L={frequency:3d} H={h_max:3d} "
                f"|B|/sqrt(D)={abs(block) / math.sqrt(d_scale):.9f} "
                f"|B|/sqrt(DL)={abs(block) / math.sqrt(d_scale * frequency):.9f}"
            )


if __name__ == "__main__":
    run()
