# Round 167 conductor adjudication

## 1. Result and terminal decision

Round 167 closes under

\[
 \boxed{\texttt{oscillatory\_determinant\_interface\_no\_go}.}
\]

The complete K17a estimate is not proved.  The round nevertheless proves
one homogeneous internal reduction and one owner-complete strict sector:

\[
 \mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}
 =\langle T_{R_0,\gamma}u_L,u_L\rangle,
\tag{167.A1}
\]

with exact ordered determinant multiplicity, and, for each fixed (B>0),

\[
 |\mathfrak C^{\rm rem}_{r\le
 \min(R_0-1,\lfloor(\log X)^B\rfloor)}|
 \ll_{\varepsilon,B}L^2X^\varepsilon.
\tag{167.A2}
\]

The full finite endpoint form has only the positive estimate

\[
 |\langle T_{R_0,\gamma}u_L,u_L\rangle|
 \ll_\varepsilon L^3X^\varepsilon,
\tag{167.A3}
\]

so the non-polylogarithmic range still needs one factor (L) of actual
signed cancellation.

The terminal no-go is deliberately narrow.  It rejects the audited direct
black-box 2024 placement, its fixed-shift triangle variant, and the
presently available 2025 Part-I placement.  It is not a no-go for all
determinant, spectral, automorphic, or oscillatory methods.

## 2. Accepted internal kernel

For an endpoint (x=(d,m)), let

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}).
\]

The real directed kernel (T_{R_0,\gamma}(y,x)) carries exactly the Fejer
weight, positive even gap below (R_0), opposing displacement, and
low-divisor-gcd condition.  The endpoint sets retain every squarefree,
selector, parity, profile, hard-value, shell, endpoint, and zero-extension
condition.

Every ordered endpoint pair maps bijectively to

\[
 \begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad \det=d'm'-dm.
\tag{167.A4}
\]

The inverse reads the entries and recovers (N=dm), (N+r=d'm').
The left action of \(\Gamma_2(4,1)\) is free on nonzero-determinant
matrices, so an orbit opening adds no stabilizer multiplicity.  Expanding
the endpoint quadratic form proves (167.A1) without duplicating the
coefficient sums and with one real part outside all shifts.

For fixed (x,r), the upper product is fixed and there is at most one
endpoint per divisor.  The row and column degrees are
\(O_\varepsilon(LX^\varepsilon)\); endpoint incidence energy is
\(O_\varepsilon(L^2X^\varepsilon)\).  Schur's test proves (167.A3).

For the restricted shifts in (167.A2), one exterior modulus gives at most

\[
 \sum_{r\le(\log X)^B}\sum_N\tau(N)\tau(N+r).
\]

The two divisor factors cost (X^{\varepsilon/4}) each, the logarithmic
shift count costs (X^{\varepsilon/2}), and the product shell has
\(O(L^2)) sites.  This proves (167.A2) with exact epsilon relabelling.

## 3. Source-interface adjudication

The 2024 determinant skeleton accepts

\[
 (a,b,c,d_0)=(d',d,m,m'),\qquad
 r=hk,quad k=2^{v_2(r)},quad h\text{ odd}.
\]

The bare coefficient \(\alpha_{\rm bare}=\chi_4(a)\chi_4(b)\) belongs
to the required principal source class.  Contrary to the first claimant
draft, its finite principal orbit coefficient is exactly zero for every
(k=2^v).  This was independently recomputed from the six
\(\mathbb P^1(\mathbb Z/4\mathbb Z)\) rows and the Hermite
representatives \(\bigl(\begin{smallmatrix}1&b\\0&k\end{smallmatrix}\bigr)\).
If the coefficient is changed to absorb a literal selector, the orbit sum
changes and must be recalculated.

The first direct-call failure is the selector/common-function interface.
For (0<\gamma<1/2), a global unipotent witness proves that the low-gcd
indicator cannot simply multiply the bare coefficient and remain left
automorphic.  The witness is not asserted to consist of two literal
project incidences.  For \(\gamma\ge1/2\), the low-gcd condition is
automatic; the residual selector still has no proved source automorphy or
target-safe interpolation for any \(\gamma\).

The normalized phase is continuously rank-one nonseparable across two
distinct determinants.  This does not exclude a discrete interpolant or a
controlled-rank expansion, but none with target-safe norms is proved.  On
a nonzero interior cell its scaled derivative requires

\[
 \delta^{-1}\gtrsim1+Jr/L.
\tag{167.A5}
\]

The source retains only an unspecified \(\delta^{-O(1)}\).  Under the
explicitly optimistic dense-block and orbit-correlation assumptions, the
\(\mathcal R_0\) branch is target-sized before losses, while the displayed
\(\mathcal R_2\) route retains (L^{\theta_4}).  This is a conditional
source-certification ledger, not a literal lower bound or a demand for a
negative power of \(\mathcal K_+\).

Part I formally allows complex oscillatory (C^{10}_\delta) weights, but
charges their derivatives.  No endpoint embedding and exact raw
automorphic-kernel identity for (T_{R_0,\gamma}) is proved.  Even after
one, the principal component and two nonnegative discrepancy-kernel
autocorrelations remain separate open estimates.  Fixed-shift theorem
errors summed absolutely likewise do not preserve the one outer real part.

## 4. First doubtful or unproved step

After removing (167.A2), the first open range is

\[
 (\log X)^B<r<R_0
\]

whenever it is nonempty.  The missing statement remains

\[
 \Re\langle T_{R_0,\gamma}u_L,u_L\rangle
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{167.A6}
\]

A future determinant implementation would need a target-safe literal
selector representation, joint variable-determinant phase treatment, and
complete orbit-correlation, principal-component, seminorm, cell, boundary,
endpoint, and completion estimates.  Round 167 supplies none of those
missing cancellations.

## 5. Required controls and outcomes

Every control is recorded in
`controls/conductor_round167_controls.md`.  The determinant multiplicity,
endpoint identity, Schur capacity, polylogarithmic sector, source
hypothesis audit, statement-only independence, and downstream scope are
green.  The source coefficient/common-function realization,
orbit-correlation, non-polylogarithmic power, boundary, and completion
controls remain red.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The internal reduction is formalized in
`proofs/kernels/m9_m2_hard_top_t1_residual_determinant_endpoint_polylog_shift_reduction.md`.
It depends only on the accepted Round-164 residual transport and Round-165
parity/gcd/scale reductions.

The source-route adjudication uses all three Round-167 reports, their three
cross-reviews, the conductor candidate, and the independent mathematical
and source-scope reviews of that candidate.  Source-dependent claims are
kept as route-audit evidence and rejected-route records rather than mixed
into the proved-internal node's statement.

## 7. Recommended state effect

Create one proved-internal reduction node containing only the determinant
endpoint identity, Schur capacity, and fixed-(B) polylogarithmic sector.
Record the bare orbit calculation as source-skeleton audit evidence and the
terminal source-interface no-go as rejected-route evidence.  Keep K17a,
the complete residual, all hard-TOP/BAL/UNBAL and M1 owners, endpoint
uniformity, M9, both bridges, the quarter theorem, and both exponent ledgers
unchanged.
