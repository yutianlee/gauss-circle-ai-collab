# Round 91 report: literal global exponent assembly attack

## 1. Result

**Result: validator-ready theorem candidate, with a sharp direct-menu
optimality statement.**  The literal H1--H4 reduction, the pointwise positive
Fejer product count, and the two elementary direct block estimates prove,
uniformly for real $X\ge 2$,

\[
\boxed{P(X)\ll_\varepsilon X^{1/3+\varepsilon}.}
\tag{1.1}
\]

No instance of `M9`, `M9-M1`, or `M9-M2` is used.  In particular, their
open $X^{1/4+\varepsilon}$ statements are not being smuggled into (1.1).
The proof keeps the literal Vaaler coefficient, the M1 spatial character,
the M2 two-shift factor, the hard top profile, and the floor endpoint.

The exponent $1/3$ is best possible **relative to the accepted four-row
direct menu**, in the precise bookkeeping sense

\[
 \sup_{(\delta,\ell)\in\Omega}
 \min\{E_{\rm T2S},E_{\rm SD},E_{\rm triv},E_{\rm TTY}\}
 =\frac13.
\tag{1.2}
\]

This is not a lower bound for either actual exponential sum.  It says only
that selecting the best recorded direct estimate block by block cannot
certify a uniform exponent smaller than $1/3$.  The witness may be taken
as $(\delta,\ell)=(1/2,1/6)$, and in fact there is a whole witness segment
on $\delta-\ell=1/3$.

## 2. Exact statement and hypotheses

Let

\[
 y=\lfloor\sqrt X\rfloor,
 \qquad
 \psi_F(t)=t-\lfloor t\rfloor-\frac12,
 \qquad
 e(t)=e^{2\pi i t}.
\]

Use the proved exact H1--H3 identity

\[
\begin{aligned}
P(X)=&-4\sum_{d\le y}\chi_4(d)\psi_F(X/d)\\
&+4\sum_{d\le y}\left\{
 \psi_F\!\left(\frac{X/d+1}{4}\right)
 -\psi_F\!\left(\frac{X/d+3}{4}\right)\right\}+O(1).
\end{aligned}
\tag{2.1}
\]

Take the proved telescoping denominator partition from
`M9-M2-dyadic-weight-nondegeneracy`.  Its active scales satisfy

\[
 X^{1/4}\le D\le X^{1/2},\qquad
 H=H_D=\lfloor DX^{-1/4}\rfloor\asymp DX^{-1/4},
\tag{2.2}
\]

and

\[
 \|w_D\|_\infty+\sum_d|w_D(d+1)-w_D(d)|\ll1.
\tag{2.3}
\]

Exactly one active profile is the hard top profile
$W(d/y){\bf1}_{d\le y}$; its sampled discrete BV norm is still $O(1)$.
The one bottom remainder is supported on $d\ll X^{1/4}$.

H4 is the audited Vaaler theorem

\[
 \psi_F(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
 \qquad
 |R_H^F(t)|\le \frac{K_H(t)}{2H+2},
\tag{2.4}
\]

where

\[
 \alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
 \qquad 0\le\Phi\le1,
\tag{2.5}
\]

and $\Phi\in C^1[0,1]$.  Choose an exact dyadic partition
$\sum_L v_L(|h|)=1$ of $1\le |h|\le H$, including its truncated top
piece.  On $h\asymp L$,

\[
 \left\|v_L(h)\frac{\Phi(h/(H+1))}{h}\right\|_\infty
 +\operatorname{Var}_h\left(v_L(h)\frac{\Phi(h/(H+1))}{h}\right)
 \ll L^{-1}.
\tag{2.6}
\]

The literal fully weighted frequency blocks are

\[
\begin{aligned}
B_1(D,L;X)
 &=-4\sum_{1\le|h|\le H}v_L(|h|)\alpha_{h,H}
   \sum_d\chi_4(d)w_D(d)e(hX/d),\\
B_2(D,L;X)
 &=4\sum_{1\le|h|\le H}v_L(|h|)\alpha_{h,H}C_h
   \sum_dw_D(d)e(hX/(4d)),
\end{aligned}
\tag{2.7}
\]

with

\[
 C_h=e(h/4)-e(3h/4)
 =2i\chi_4(h){\bf1}_{2\nmid h}.
\tag{2.8}
\]

The theorem proved here is: under (2.1)--(2.8), for every
$\varepsilon>0$, both blocks in (2.7) are
$O_\varepsilon(X^{1/3+\varepsilon})$, uniformly for every active $(D,L)$
and real $X\ge2$; all residual blocks are
$O_\varepsilon(X^{1/4+\varepsilon})$; hence (1.1) follows after the two
dyadic assemblies.

## 3. Proof or derivation

**Literal direct estimates.**  The frequency-first argument applied to
(2.7) gives, for $i=1,2$,

\[
 \boxed{|B_i(D,L;X)|\ll_\varepsilon
 X^\varepsilon\left(1+\frac DL\right).}
\tag{3.1}
\]

For M1, apply (2.6) at each fixed $d$, retain
$\chi_4(d)w_D(d)$, and use the geometric-sum bound

\[
 \left|\sum_h u_{L,H}(h)e(h\theta)\right|
 \ll\min\left(1,\frac1{L\|\theta\|}\right).
\]

If $m$ is a nearest integer to $X/d$ and $n=dm$, then
$\|X/d\|=|X-n|/d$.  Each fixed positive integer $n\asymp X$ has at
most $\tau(n)$ participating divisors.  The participating products also
satisfy $|X-n|\ll D$.  Therefore

\[
 \sum_d\min\left(1,\frac1{L\|X/d\|}\right)
 \ll_\varepsilon X^\varepsilon
 \sum_{|n-X|\ll D}\min\left(1,\frac{D/L}{|X-n|}\right)
 \ll_\varepsilon X^\varepsilon\left(1+\frac DL\right).
\tag{3.2}
\]

The value at $X=n$ is interpreted as $1$, so exact products are
included.  A nearest-integer tie may be resolved arbitrarily.

For M2 one must not Abel-sum the oscillating coefficient $C_h$.  Instead
use its exact origin before estimating:

\[
 C_he(hX/(4d))
 =e\!\left(\frac h4(X/d+1)\right)
  -e\!\left(\frac h4(X/d+3)\right).
\tag{3.3}
\]

Apply (2.6) separately to the two shifted legs.  If $m$ is nearest to
$(X/d+\rho)/4$, then

\[
 4d\left\|\frac{X/d+\rho}{4}\right\|
 =|X-d(4m-\rho)|,
 \qquad \rho\in\{1,3\}.
\]

The same divisor grouping proves (3.1).  Thus the actual M2 character has
been retained through the exact two-shift identity, rather than erased by
an inadmissible coefficient replacement.

For the full second-derivative estimate, the hard top causes no problem.
For M2 use (2.3) directly.  For M1 split $d$ into the two odd residue
classes modulo $4$; $\chi_4$ is constant on each class and the sampled
profile, including the top truncation, has $O(1)$ BV.  On either class
the phase has one-signed curvature

\[
 |f_h''|\asymp\lambda_h:=\frac{|h|X}{D^3}.
\]

The weighted second-derivative theorem, with the small-curvature term kept,
gives

\[
 \sum_{d\asymp D}a_D(d)e(f_h(d))
 \ll D\lambda_h^{1/2}+\lambda_h^{-1/2}+1.
\]

Summing with the actual $1/|h|$ Vaaler magnitude on $h\asymp L$, and
using $|C_h|\le2$ for M2, yields literally for both blocks

\[
 \boxed{|B_i(D,L;X)|
 \ll
 \left(\frac{LX}{D}\right)^{1/2}
 +\frac{D^{3/2}}{(LX)^{1/2}}+1.}
\tag{3.4}
\]

No cancellation of $\chi_4(d)$ or $\chi_4(h)$ is asserted in (3.4).

Put $D=X^\delta,L=X^\ell$, and $x=\delta-\ell$.  Up to harmless
$X^\varepsilon$ factors from dyadic constants, the exact exponent table
is

| menu row | literal bound | exponent | region used for $1/3$ |
|---|---:|---:|---:|
| frequency first / T2S | $1+D/L$ | $x=\delta-\ell$ | $x\le1/3$ |
| full second derivative, first term | $(LX/D)^{1/2}$ | $(1+\ell-\delta)/2=(1-x)/2$ | $x\ge1/3$ |
| full second derivative, small-curvature term | $D^{3/2}(LX)^{-1/2}$ | $(3\delta-1-\ell)/2=(2\delta+x-1)/2$ | $x\ge1/3$ |
| trivial | $D$ | $\delta$ | not needed |
| audited TTY | as in the source card | $[89(1+\ell)+819\delta]/1282$ | not needed |

Here

\[
 \Omega=\{(\delta,\ell):1/4\le\delta\le1/2,
                 0\le\ell\le\delta-1/4\},
 \qquad 1/4\le x\le\delta\le1/2.
\]

If $x\le1/3$, (3.1) is at most $X^{1/3+\varepsilon}$.  If
$x\ge1/3$, then

\[
 \frac{1-x}{2}\le\frac13,
 \qquad
 \frac{2\delta+x-1}{2}\le\frac14,
\tag{3.5}
\]

where the second inequality uses $x\le\delta\le1/2$.  The inequalities
are inclusive, so $x=1/3$, $L=1$, $D=X^{1/2}$, and every boundary of
$\Omega$ are covered.  Equivalently, in literal scales, when
$D/L\ge X^{1/3}$, the two terms in (3.4) are at most $X^{1/3}$ and
$X^{1/4}$, respectively.

**Pointwise Fejer residual.**  Write

\[
 F_H(t)=\frac{K_H(t)}{2H+2},
 \qquad
 \Delta=\frac{D}{H+1}\asymp X^{1/4}.
\]

Uniformly also at an integer argument,

\[
 F_H(t)\ll
 \min\left(1,\frac1{(H+1)^2\|t\|^2}\right).
\tag{3.6}
\]

For the first leg, with $m$ nearest to $X/d$ and $n=dm$, (3.6)
is bounded by

\[
 W_\Delta(X-n):=
 \begin{cases}
 1,&X=n,\\
 \min(1,\Delta^2/|X-n|^2),&X\ne n.
 \end{cases}
\]

The multiplicity of each product is at most $\tau(n)$.  For $X$ large,
every participating $n$ is positive and $n\asymp X$; bounded $X$ is
absorbed in the implied constant.  Hence, pointwise for real $X$,

\[
 \sum_d|w_D(d)|F_H(X/d)
 \ll_\varepsilon X^\varepsilon
 \sum_{n\in\mathbb Z}W_\Delta(X-n)
 \ll_\varepsilon X^{1/4+\varepsilon}.
\tag{3.7}
\]

For a shifted leg choose $m$ nearest to $(X/d+\rho)/4$ and group by
$n=d(4m-\rho)$.  Then

\[
 \left\|\frac{X/d+\rho}{4}\right\|
 =\frac{|X-n|}{4d},
\]

so (3.7) applies with $4\Delta$.  The odd congruence on $4m-\rho$
only reduces multiplicity.  This includes both shifts, exact shifted
products, half-open denominator shells, and the top cutoff $d\le y$.
As a separate far-tail check,

\[
 \frac{D}{(H+1)^2}\asymp\frac{X^{1/2}}D\le X^{1/4}.
\tag{3.8}
\]

At an exact integer input, H4 is also exact at the jump:
$\psi_F(n)=-1/2$, the Fourier polynomial is $0$, and
$K_H(0)/(2H+2)=1/2$.  Thus (3.7) is a pointwise proof, not a mean-square
substitute, and it closes the mathematical content of
`R5-Full-reconciliation`.

**Direct-menu optimality.**  Let $E(\delta,\ell)$ be the minimum of the
four menu exponents, interpreting the second-derivative row as the maximum
of its two displayed powers and $0$.  The preceding case split proves
$E\le1/3$ everywhere.  On the line $x=1/3$, where
$\ell=\delta-1/3$ and $1/3\le\delta\le1/2$,

\[
 E_{\rm T2S}=E_{\rm SD}=\frac13,
 \qquad
 E_{\rm triv}=\delta,
 \qquad
 E_{\rm TTY}=\frac{178+2724\delta}{3846}.
\tag{3.9}
\]

The TTY exponent equals $1/3$ at
$\delta=92/227$ and is larger thereafter.  Consequently

\[
 E(\delta,\delta-1/3)=\frac13
 \quad\left(\frac{92}{227}\le\delta\le\frac12\right).
\]

At the requested endpoint witness $(\delta,\ell)=(1/2,1/6)$, the four
rows are

\[
 \frac13,\qquad
 \max\left\{\frac13,\frac16,0\right\}=\frac13,
 \qquad
 \frac12,
 \qquad
 \frac{770}{1923}>\frac13.
\tag{3.10}
\]

Thus neither TTY nor the trivial row lowers the menu maximum.

**End-to-end assembly and implication diagram.**  The exact ownership is

```text
H1--H3  ----------------------------------------------> exact formula (2.1)
proved denominator partition ----> bottom remainder --> O(X^(1/4))
                         |
                         +--> active D, H_D, hard top profile
                                  |
audited H4 ------------------------+--> Fejer residuals
                                  |       |
                                  |       +--> pointwise product count --> O(X^(1/4+eps))
                                  |
                                  +--> literal M1/M2 main blocks
                                           |
                                           +--> T2S if D/L <= X^(1/3)
                                           +--> full SD if D/L >= X^(1/3)
                                                    |
                                                    +--> O(X^(1/3+eps)) per block

frequency dyadic sum + denominator dyadic sum + (2.1)
                                      ----------------> P(X) << X^(1/3+eps)
```

There are $O(\log X)$ denominator scales and $O(\log X)$ frequency
scales per active denominator.  Apply the block bounds with, say,
$\varepsilon/3$, and absorb both logarithms into the remaining
$X^\varepsilon$.  The denominator partition is exact, so the bottom
remainder and active blocks are not double-counted.  The proof remains in
the original reciprocal blocks; transformed endpoint cones and their
equality stars are not invoked.  The only physical equality endpoint is
the already-owned $d=y=\lfloor\sqrt X\rfloor$ sample in the hard top
profile.

## 4. First doubtful or unproved step

No mathematical inequality in the displayed one-third assembly remains
unproved once the elementary weighted second-derivative theorem and the
accepted divisor bound are admitted.  The first non-closed step is instead
**proof-state acceptance**: the authoritative graph still records both
`R5-Full` and `R5-Full-reconciliation` as
`derived_under_assumptions`, and it has no standalone node stating that
(3.1) and (3.4) act on the literal blocks (2.7) at exponent $1/3$.

Accordingly, (1.1) must remain candidate evidence until an independent
validator checks the residue-class BV transfer in (3.4), the pointwise
product grouping in (3.7), and then applies a State Patch.  This is the
first state seam; it is not an invocation of an open analytic conjecture.
The $X^{1/4+\varepsilon}$ M1 and M2 estimates remain genuinely unproved.

## 5. Control tests and outcomes

| required control | outcome |
|---|---|
| `exact_block_normalization` | **PASS.**  The literal blocks are (2.7), including $\alpha_{h,H}$, $w_D$, constants, both signs, $\chi_4(d)$, and $C_h$. |
| `one_third_region_optimization` | **PASS.**  The inclusive split (3.5) covers all of $\Omega$; (3.9)--(3.10) prove menu-optimality. |
| `second_derivative_small_curvature` | **PASS.**  The $\lambda_h^{-1/2}$ term is retained and contributes at most $X^{1/4}$; $L=1$ and $D=X^{1/2}$ are included. |
| `actual_M1_M2_coefficients` | **PASS.**  M1 is split only by the actual spatial residue classes.  M2 T2S uses the exact two-shift identity (3.3); M2 SD uses only the legitimate inequality $|C_h|\le2$. |
| `R5_pointwise_product_count` | **PASS.**  Equation (3.7) is pointwise in real $X$ and uses positivity before any Fourier expansion. |
| `exact_product_and_floor_endpoint` | **PASS.**  Exact products receive weight $1$; nearest ties are harmless; $\psi_F(n)=-1/2$ and $K_H(0)/(2H+2)=1/2$ are explicit. |
| `hard_top_BV` | **PASS.**  The one-sided top weight has uniform sampled BV; its mod-$4$ samples do too.  No smooth-Poisson hypothesis is used. |
| `small_denominator_owner` | **PASS.**  The unique pre-Vaaler bottom remainder has $O(X^{1/4})$ terms and is disjoint from the active partition. |
| `dyadic_frequency_and_denominator_assembly` | **PASS.**  Exact/bounded-overlap partitions give at most $O(\log^2X)$, absorbed into $X^\varepsilon$. |
| `real_X_uniformity` | **PASS.**  All nearest-product arguments group around a real center $X$; only the products $n$ are integers.  Bounded $X$ is absorbed separately. |
| `dependency_status_and_source_map` | **PASS AS A PROOF; PATCH REQUIRED IN THE GRAPH.**  H1--H3, H4, coefficient regularity, the profile, and the divisor bound are accepted; the two R5 nodes still need status reconciliation. |
| `downstream_scope` | **PASS.**  Only a new one-third envelope and partial Gauss theorem are proposed.  No $1/4$-scale M9 node is promoted. |

The controls were analytical; no numerical experiment was used.

## 6. Dependencies and exact artifacts used

The dependency/status map used by the proof is:

| dependency | graph status | exact role |
|---|---|---|
| `H1-H3` | `proved_internal` | exact real-$X$, floor-compatible identity (2.1) |
| `H4`, `H4-source-audit` | `proved_external_dependency` | exact $\alpha_{h,H}$, positive Fejer residual, integer jump |
| `H4-Phi-regularity` | `proved_internal` | frequency coefficient BV (2.6) |
| `Divisor-bound-elementary` | `proved_internal` | product multiplicities in (3.2) and (3.7) |
| `M9-M2-dyadic-weight-nondegeneracy` | `proved_internal` | exact denominator partition, bottom owner, hard-top BV, height floor |
| `M9-M2-top-frequency-two-shift-T2S` | `proved_internal` | the $1+D/L$ estimate; here used at its stated full $1\le L\le H$ strength, not extrapolated to a $1/4$ conclusion |
| `M9-M1-terminal-frequency-divisor-bound` | `proved_internal` | the M1 $1+D/L$ estimate, likewise used at its stated all-$L$ strength |
| M1/M2 frequency phase-diagram reductions | `proved_internal` | recorded direct exponent normalization; (3.4) is rederived literally here |
| M1/M2 TTY wedge | `proved_external_dependency` | used only to test menu-optimality, not to prove (1.1) |
| `R5-Full`, `R5-Full-reconciliation` | `derived_under_assumptions` | mathematical proof completed in (3.6)--(3.8); graph promotion still required |
| `M9-M1`, `M9-M2`, `M9`, `GC-target` | `open` | not used |

Exact artifacts consulted and used were:

- `protocol.md` and `state/active_campaign.yml` for authority, scope, and
  the Round 91 gates;
- `state/proof_obligations.yml` for every status in the preceding table;
- `state/best_proof_draft.md`, Sections 1--7 and the direct-block/profile
  sections, for the literal H1--H4 and block conventions;
- `strategy/conductor_0817_full_proof_strategy.md` for the mandated
  partial-theorem scope;
- `rounds/codex-managed/gc-unconditional-exponent-extraction/derivation_packet.md`
  for the frozen Round 91 interface;
- `rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md` and
  `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md` for the
  two direct menus and literal coefficient conventions;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/synthesis.md` for
  the hard-top profile and endpoint warning;
- `rounds/obligation-main/round_004/responses/A1-004.md`,
  `rounds/obligation-main/round_004/reviews/A4.md`, and
  `rounds/web-research-test/round_027/judge/judge-027.md` for the pointwise
  R5 proof, its wrong-norm control, and exact edge-case list;
- `sources/vaaler_1985.md` for H4 and
  `sources/tao_trudgian_yang_2025.md` only for the TTY menu row.

No unlisted source theorem, record exponent, mean-square upgrade, or web
claim is used.

## 7. Recommended state effect

Apply no state mutation until independent validation.  If the literal
normalization and R5 seams are rechecked, the proposed graph effect is:

| graph item | proposed effect | exact scope/dependencies |
|---|---|---|
| `R5-Full-reconciliation` | promote to `proved_internal` | pointwise proof (3.6)--(3.8), depending on H4, its source audit, the exact profile, and the divisor bound |
| `R5-Full` | promote to `proved_internal` | all first and shifted residual blocks, including exact products and the hard top |
| new `M9-direct-one-third-envelope` | add as `proved_internal` | the literal M1 and M2 main sums are $O_\varepsilon(X^{1/3+\varepsilon})$ uniformly in active $D$ and real $X$, by (3.1)--(3.5) |
| new `M9-direct-menu-one-third-optimality` | add as `proved_internal` | (1.2) only; explicitly not a lower bound for the sums |
| new `GC-partial(1/3)` | add as `proved_internal` theorem | H1--H3 + H4 + proved R5 + `M9-direct-one-third-envelope` imply (1.1) |

Retain without change `M9-M1`, `M9-M2`, `M9`,
`M9-endpoint-uniformity` at the $1/4$ target, `Conditional-bridge`, and
`GC-target`.  In particular, this report does not estimate the canonical
hard M1 Gram operator, the M2 signed cross-row energy, or any endpoint core
at exponent $1/4$.
