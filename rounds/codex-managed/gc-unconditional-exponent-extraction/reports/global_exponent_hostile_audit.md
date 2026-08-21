# Round 91 hostile audit: unconditional one-third exponent

## 1. Result

**Certification lemma, with one required proof-state repair.**  The literal
accepted hyperbola--Vaaler decomposition, the actual fixed M1 and M2
coefficients, the pointwise positive-Fejer product count, and the direct
frequency-first/second-derivative estimates prove, for every
\(\varepsilon>0\) and every real \(X\ge 2\),

\[
 P(X)=N(\sqrt X)-\pi X\ll_\varepsilon X^{1/3+\varepsilon}.
\]

The direct block menu has exact minimax exponent \(1/3\).  Thus it does not
prove any uniform exponent strictly smaller than \(1/3\) without a new
estimate or cancellation between blocks.  This is only menu optimality, not
a lower bound for either actual reciprocal sum.

The mathematics is noncircular, but the current authoritative graph is not
yet in a state from which the theorem may be declared proved:
`R5-Full` lists `R5-Full-reconciliation` as a blocker, while
`R5-Full-reconciliation` lists `R5-Full` as a dependency, and both are still
`derived_under_assumptions`.  Section 3 below gives a direct proof from H4
and elementary divisor counting, so that cycle can and must be removed by a
conductor-owned State Patch.  Until that patch is validated, this report is
candidate evidence rather than an authoritative theorem promotion.

## 2. Exact statement and hypotheses

Let \(y=\lfloor\sqrt X\rfloor\), use the accepted exact telescoping
denominator partition of \(1\le d\le y\), and put

\[
 H_D=\lfloor D X^{-1/4}\rfloor
 \asymp D X^{-1/4}
 \quad (X^{1/4}\le D\le X^{1/2}).
\]

For a dyadic frequency block \(1\le L\le H_D\), write
\(D=X^\delta\), \(L=X^\ell\).  Thus

\[
 \Omega=\{(\delta,\ell):1/4\le\delta\le1/2,
             \ 0\le\ell\le\delta-1/4\}.
\]

The literal block statement audited here is the following.  For either
frequency sign, the M1 block has coefficient
\(\alpha_{h,H_D}\), spatial factor \(\chi _4(d)w_D(d)\), and phase
\(e(hX/d)\).  The M2 block has coefficient

\[
 \alpha_{h,H_D}C_h,\qquad
 C_h=e(h/4)-e(3h/4),
\]

and phase \(e(hX/(4d))\); equivalently, before combining, it is the
difference of the two literal shifts \(\rho=1,3\).  On every such full
block,

\[
 |B_i(D,L;X)|\ll_\varepsilon X^\varepsilon
 \min\!\left\{
  1+\frac DL,
  1+\sqrt{\frac{LX}{D}}+\frac{D^{3/2}}{\sqrt{LX}},
  D,
  X^{[89(1+\ell)+819\delta]/1282}
 \right\},                                      \tag{91.H1}
\]

where the last entry is optional and, in its complete exponent-pair form,
also has the harmless companion exponent \(2\delta-1-\ell\le0\) on
\(\Omega\).  The first two entries alone imply

\[
 B_i(D,L;X)\ll_\varepsilon X^{1/3+\varepsilon}  \tag{91.H2}
\]

uniformly on \(\Omega\), including \(L=1\), the final possibly short
frequency block, and the one-sided top denominator block
\(d\le\lfloor\sqrt X\rfloor\).

The hypotheses are exactly the accepted H1--H3 arithmetic identity, the
audited H4 Vaaler formula, the accepted \(C^1\) regularity of \(\Phi\), the
actual profile certificate
\(\|w_D\|_\infty+\sum_d|\Delta w_D(d)|\ll1\), and the elementary divisor
bound.  No M9, M9-M1, M9-M2, transformed cone estimate, average in \(X\),
or record circle exponent is assumed.

## 3. Proof or derivation

**Literal second-derivative block.**  On a fixed frequency \(|h|\asymp L\),
the denominator phase has

\[
 |f_h''(d)|\asymp \lambda_h:=\frac{|h|X}{D^3}.
\]

For M1, split the odd denominators into \(d=4n+1\) and \(d=4n+3\).
The character is then constant and the second derivative with respect to
\(n\) is still comparable to \(|h|X/D^3\).  Sampling a bounded-variation
profile on either progression preserves bounded variation.  For M2 the
factor \(C_h\) is independent of \(d\); each quarter shift is also a
constant in \(d\).  Weighted partial summation and the second-derivative
estimate therefore give, for either literal inner sum,

\[
 \sum_{d\asymp D}a_d e(f_h(d))
 \ll \sqrt{\frac{|h|X}{D}}
       +\frac{D^{3/2}}{\sqrt{|h|X}}+1.             \tag{91.H3}
\]

This is uniform for the hard top profile: its cutoff contributes one
bounded BV jump.  It is also uniform at smallest curvature.  Indeed
\(D\le X^{1/2}\), \(|h|\ge1\) imply
\(\lambda_h\ge D^{-1}\); equality in scale occurs at
\(D=X^{1/2},|h|=1\), where the two derivative terms are both
\(X^{1/4}\).  If \(\lambda_h>1\), the trivial estimate is already bounded
by the first term in the usual second-derivative expression, so no hidden
small- or large-curvature range is omitted.

The actual coefficients satisfy
\(|\alpha_{h,H_D}|\ll |h|^{-1}\) and
\(|C_h|\le2\).  Summing (91.H3), rather than bounding merely one inner
sum, gives

\[
 \begin{aligned}
 |B_i(D,L;X)|
 &\ll \sum_{|h|\asymp L}\frac1{|h|}
 \left(\sqrt{\frac{|h|X}{D}}
       +\frac{D^{3/2}}{\sqrt{|h|X}}+1\right)\\
 &\ll 1+\sqrt{\frac{LX}{D}}
       +\frac{D^{3/2}}{\sqrt{LX}}.                 \tag{91.H4}
 \end{aligned}
\]

Thus (91.H4) is a bound for the fully weighted M1 or M2 block, not for an
unweighted inner denominator sum.  It retains both frequency signs.  The
M1 spatial character is handled by its two residue classes, while the M2
frequency character is retained in \(C_h\) before the harmless inequality
\(|C_h|\le2\).

**Literal frequency-first block.**  The dyadic Vaaler coefficient without
the M2 shift factor has

\[
 \|u_{L,H}\|_\infty+\sum_h|\Delta u_{L,H}(h)|\ll L^{-1}.
\]

Frequency-first Abel summation and nearest-product grouping give
\(B_i(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L)\).  For M2 this step must
be applied to the \(\rho=1\) and \(\rho=3\) shifted sums separately;
multiplication by the alternating \(\chi _4(h)\) and a claim that the
combined \(\beta_h\) has the same BV norm would be false.  The accepted
two-shift formulation avoids that error and recombines the two estimates
afterward.  For M1, \(|\chi _4(d)|\le1\) is retained throughout the
product count.  Hence the T2S exponent for the literal block is
\(\delta-\ell\).

**Exact optimization.**  Put \(x=\delta-\ell\).  On \(\Omega\),
\(1/4\le x\le\delta\le1/2\).  If \(x\le1/3\), T2S has exponent
\(x\le1/3\).  If \(x\ge1/3\), the two terms in (91.H4) have exponents

\[
 a=\frac{1-x}{2}\le\frac13,
 \qquad
 b=\frac{2\delta+x-1}{2}\le\frac{x}{2}\le\frac14.
\]

The additional constant has exponent zero.  This proves (91.H2) on both
closed regions and on their common boundary.  The fact that (91.H4) is a
sum of two terms costs only a fixed factor because both exponents have
been bounded separately.

The menu cannot yield a smaller uniform exponent.  At

\[
 (\delta,\ell)=\left(\frac12,\frac16\right),
 \qquad x=\frac13,
\]

the complete menu is

\[
\begin{array}{c|c}
\text{estimate}&\text{exponent(s)}\\ \hline
\text{T2S}&1/3\\
\text{full second derivative}&1/3,\ 1/6,\ 0\\
\text{trivial}&1/2\\
\text{TTY main term}&
\dfrac{89(7/6)+819/2}{1282}=\dfrac{770}{1923}>1/3\\
\text{TTY companion}&2\delta-1-\ell=-1/6
\end{array}
\]

so the best exponent supplied at this admissible block is exactly
\(1/3\).  This proves only optimality of the listed menu.

**Pointwise R5.**  From H4,

\[
 |R_H^F(t)|\le\frac{K_H(t)}{2H+2},\qquad
 \frac1H K_H(t)\ll
 \min\!\left(1,\frac1{H^2\|t\|^2}\right).
\]

Let \(\Delta=D/H\asymp X^{1/4}\).  For the first leg choose a nearest
integer \(m_d\) to \(X/d\) and put \(n=dm_d\).  Grouping by the integer
\(n\), with at most \(\tau(n)\) participating divisors, gives directly for
real \(X\)

\[
 \frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
 \ll_\varepsilon X^\varepsilon
 \sum_{n\in\mathbb Z}
 \min\!\left(1,\frac{c\Delta^2}{|X-n|^2}\right)
 \ll_\varepsilon X^{1/4+\varepsilon}.              \tag{91.H5}
\]

At \(X=n\) the summand is defined as one.  For a shifted leg choose a
nearest integer to \((X/d+\rho)/4\) and put
\(n=d(4m-\rho)\), \(\rho\in\{1,3\}\).  This changes only the fixed
constant in \(\Delta\), and the congruence restriction reduces the divisor
multiplicity.  For large \(X\) these quotients are positive; bounded \(X\)
is absorbed into the implied constant.  This proof is pointwise, includes
exact products, and never expands the positive Fejer kernel into arbitrary
Fourier coefficients.  Equivalently, the far-tail contribution is
\(DH^{-2}\asymp X^{1/2}/D\le X^{1/4}\).

**One-count assembly.**  The inactive bottom remainder contains
\(O(X^{1/4})\) denominators in total and is bounded before Vaaler, so it is
not counted again among either main terms or residuals.  Every active
denominator occurs in the exact telescoping partition, the top term
\(d=y\) occurs in its one prescribed top profile, and each frequency
\(1\le |h|\le H_D\) occurs in a bounded-overlap dyadic frequency partition.
There are \(O(\log X)\) denominator blocks and \(O(\log X)\) frequency
blocks per denominator scale.  Summing (91.H2) costs at most
\(O(\log^2X)\), while (91.H5) costs at most another denominator logarithm;
all are absorbed by first using a smaller epsilon in the block bounds.
H1--H3 then gives the asserted one-third theorem.  The original direct
blocks use the literal upper limit \(d\le y\), so transformed endpoint
cones and their stationary stars are not invoked.  Floors in \(y,H_D\),
the equality term \(d=y\), and the sawtooth value at integral arguments are
all retained.

## 4. First doubtful or unproved step

The first genuinely dangerous mathematical step was the phrase “full
second-derivative bound”: if it bounded only one denominator sum, the outer
\(h\)-sum could have lost a factor \(L\).  Equations (91.H3)--(91.H4) resolve
that seam with the actual \(1/h\) Vaaler coefficient.  A second dangerous
shortcut would be to give the combined M2 coefficient \(\beta_h\) a false
smooth BV norm; the proof instead uses the two quarter shifts separately
for T2S and uses only \(|C_h|\le2\) for the denominator-first estimate.

After those repairs, no mathematical step of the scoped one-third theorem
remains unproved in the permitted packet.  The first remaining obstruction
is proof-state ownership: the circular R5 dependency and conditional status
must be corrected by the conductor before the theorem can enter the
authoritative graph.  This report does not itself make that patch.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_block_normalization` | **Pass.** The outer \(1/h\) coefficient is summed in (91.H4); constants \(-4,4\), signs, and bounded dyadic cutoffs are harmless. |
| `one_third_region_optimization` | **Pass.** The closed split \(x\le1/3\) / \(x\ge1/3\) covers every boundary of \(\Omega\).  The block \((1/2,1/6)\) proves menu optimality. |
| `second_derivative_small_curvature` | **Pass.** \(\lambda_h\ge D^{-1}\); the extremal \((D,h)=(X^{1/2},1)\) gives two \(X^{1/4}\) terms, not a degeneration. |
| `actual_M1_M2_coefficients` | **Pass.** M1 is split into its two spatial character classes.  M2 retains \(C_h\); T2S is applied before combining the two shifts. |
| `R5_pointwise_product_count` | **Pass.** (91.H5) is a supremum-valid pointwise estimate for each real \(X\), not an RMS statement. |
| `exact_product_and_floor_endpoint` | **Pass.** Exact products use the summand value one; H4 covers \(\psi_F(n)=-1/2\) exactly through \(K_H(0)/(2H+2)=1/2\). |
| `hard_top_BV` | **Pass.** The one-sided sampled top profile has uniformly bounded discrete variation, sufficient for both partial summations and derivative estimates. |
| `small_denominator_owner` | **Pass.** The entire inactive remainder is bounded once, pre-Vaaler, by its \(O(X^{1/4})\) cardinality. |
| `dyadic_frequency_and_denominator_assembly` | **Pass.** Exact/bounded-overlap partitions cost \(O(\log^2X)\), absorbed in \(X^\varepsilon\); no denominator or frequency is silently omitted. |
| `real_X_uniformity` | **Pass.** All estimates use distances from a real \(X\) to integer products; \(y=\lfloor\sqrt X\rfloor\) and all height floors are retained. |
| `dependency_status_and_source_map` | **Pass mathematically; State Patch required.** H4 is fully audited.  R5 is rederived without M9, but its current graph cycle/status must not be ignored. |
| `downstream_scope` | **Pass.** The result is a new one-third envelope only.  It proves none of the open one-quarter M9 component targets or `GC-target`. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The proof uses the following accepted dependencies: `H1-H3`
(`proved_internal`); `H4` and `H4-source-audit`
(`proved_external_dependency`); `H4-Phi-regularity`,
`M9-M2-beta-algebra`, `M9-M2-dyadic-weight-nondegeneracy`,
`M9-M2-top-frequency-two-shift-T2S`,
`M9-M1-terminal-frequency-divisor-bound`, and
`Divisor-bound-elementary` (`proved_internal`).  The two phase-diagram
syntheses supply the accepted direct exponent formulas.  The TTY nodes and
source card are used only to test whether the menu can improve on one third,
not in the proof of the upper bound.

Exact artifacts consulted, and no others, were:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/best_proof_draft.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/gc-unconditional-exponent-extraction/derivation_packet.md`;
- `rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md`;
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/synthesis.md`;
- `rounds/obligation-main/round_004/responses/A1-004.md`;
- `rounds/obligation-main/round_004/reviews/A4.md`;
- `rounds/web-research-test/round_027/judge/judge-027.md`;
- `sources/vaaler_1985.md`;
- `sources/tao_trudgian_yang_2025.md`.

The open nodes `M9-M1`, `M9-M2`, `M9`, `M9-endpoint-uniformity`, and
`GC-target` were inspected for scope and status but are not proof
dependencies.

## 7. Recommended state effect

**Promote after conductor validation.**  Remove the circular dependency of
`R5-Full-reconciliation` on `R5-Full`; make its direct dependencies H4,
H4-source-audit, the actual dyadic-profile certificate, and the elementary
divisor bound.  Then promote `R5-Full-reconciliation` and `R5-Full` to
`proved_internal`, with (91.H5) and the integer/shift/top-endpoint checks as
the reason.

Add a separate proved-internal node for the uniform direct one-third M1/M2
block envelope, depending on the literal T2S and second-derivative block
proofs plus the coefficient/profile nodes, but **not** on M9-M1 or M9-M2.
Add a separate unconditional theorem node

\[
 P(X)\ll_\varepsilon X^{1/3+\varepsilon}
\]

depending on H1--H3, H4, the reconciled R5-Full, the one-third direct
envelope, small-denominator ownership, and dyadic assembly.  Record
\((\delta,\ell)=(1/2,1/6)\) as the certificate that \(1/3\) is optimal for
this menu only.

**Retain without promotion** `M9-M1`, `M9-M2`, `M9`,
`M9-endpoint-uniformity`, `M9-M2-character-factor`, the conditional
one-quarter bridge, and `GC-target`.  Nothing here proves the one-quarter
endpoint, closes either hard core, or licenses a claim below one third.
