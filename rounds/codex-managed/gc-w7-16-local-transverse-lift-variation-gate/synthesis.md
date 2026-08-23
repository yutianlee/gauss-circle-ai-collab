# Round 128 synthesis: the finite coefficient gate passes branchwise

Campaign: `gc-w7-16-local-transverse-lift-variation-gate`

Starting graph SHA-256:
`1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`

## Frozen question

Round 128 tested whether every literal long-lift coefficient on one
reciprocal window has local square variation

\[
 O_\varepsilon(J_B^{1/2}L^{-1}Y^\varepsilon),
 \qquad J_B=1+DQ_B/B^2,
\]

including both endpoint values, continuous profiles, hard samples, stars,
floors, support motion, divisor progressions, and shell ownership.

## Exact outcome

The abstract inference from pointwise size, a birth count, and a displayed
\(\chi _4(g)\) is false.  Fixed-window phase-conjugating and alternating
controls can have full \(G\sqrt N/L\) capacity, and endpoint values alone
can have full \(G/L\) capacity.

The physical coefficient has stronger structure.  The accepted Round-95
formula factors every lift weight into a fixed sampled-BV frequency factor
and a sampled-BV denominator profile \(\omega_D(gb')\).  Decomposing the
latter exactly into moving thresholds, applying interval-uniform Abel
summation to the common lift character, and then using Minkowski proves

\[
 \|U_{i,\rho,\eta}\|_{V^2(I)}
 \ll_\varepsilon J_B^{1/2}L^{-1}Y^\varepsilon
\]

for the two exact M1 quarter-phase branches and the single M2 branch.  The
proof includes every literal profile and boundary package.

The branch qualification is essential.  If the reduced M1 character
\(\chi _4(b')\) remains inside the amplitude, a literal one-lift top-shell
packet has norm \(\gg Q_B^{1/2}/L\) while \(J_B\asymp1\).  Splitting
\(\chi _4(b')\) into \(e(\pm b'/4)\) moves this dense alternation exactly
into the carrier phase and restores the theorem.  The common lift
character remains inside the lift sum.

## Remaining gate and proof status

The next theorem would have to bound the branchwise reciprocal sum by the
proved \(V^2\) norm times the second-derivative curvature factor, without
the generic extra \(N_\rho^{1/2}\).  That joint actual-family inequality is
open.  Consequently the conditional \(Y^{73/96+\varepsilon}\) complete
block bound is not yet a theorem.

Round 128 improves the proof graph by closing one finite coefficient gate,
not by changing a Gauss-circle exponent.  The internal exponent remains
\(1/3\); the audited external benchmark remains
\(0.3144831759740614\ldots\).  M9-M1, M9-M2, endpoint uniformity, M9, and
the quarter target remain open.

Resulting graph SHA-256:
`476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`.
