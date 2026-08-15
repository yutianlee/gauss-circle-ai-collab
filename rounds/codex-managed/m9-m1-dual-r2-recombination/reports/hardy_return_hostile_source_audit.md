# Round 14 report: the M1 recombination is angular, while full recombination is the Hardy return map

Campaign: `m9-m1-dual-r2-recombination`  
Task: `hardy_return_hostile_source_audit`  
Role: primary-source and hostile reviewer  
Graph SHA-256 at launch: `ba43cb4e073a06640030a9090df6b57cc4ad8564feada6a0698aa777d1378b14`

## 1. Result

**No-go result, with an exact surviving interface.**  The stationary power in
one RCS block does simplify exactly: after inserting the Vaaler factor (1/h)
and grouping (n=hq), every divisor incidence has the common radial power

\[
 X^{1/4}n^{-3/4}.
\]

The remaining coefficient, however, is not (r_2(n)/4).  It is an angular,
dyadically sampled, floor-height-weighted restricted divisor sum.  The M1
spatial cutoff alone restricts it to roughly (q\geq 4h), and the actual
(\Phi(h/(H_D+1))), the floors (H_D=\lfloor DX^{-1/4}\rfloor), and the
endpoint star prevent the dyadic partition from becoming an (n)-only
multiplier.

If all complementary angular sectors were instead supplied and their symbols
were proved to add to (1), restoring
(\sum_{q\mid n}\chi_4(q)=r_2(n)/4), then the accepted stationary constant
gives exactly the positive-frequency half of the classical Hardy--Voronoi
radial expansion.  At radial truncation (N\asymp X^{1/2}), bounding that
full radial sum by (X^{1/4+\varepsilon}) is equivalent, up to a
target-sized error, to the original Gauss-circle target.  It is not a new
strictly easier analytic obligation.

## 2. Exact statement and hypotheses

Take one positive-frequency M1 shell in the normalization of RCS.  Write its
actual frequency weight as

\[
 u_{L,H_D}(h)=v_L(h)\frac{\Phi(h/(H_D+1))}{h},
 \qquad 1\leq h\leq H_D,
\]

with any already separated fixed leading constant left outside.  Put

\[
 d_{h,q}=2\sqrt{\frac{hX}{q}},\qquad q\ \text{odd}.
\]

Let (\omega_D^*(h,q;X)) denote exactly the spatial factor
(w_D(d_{h,q})), including its support condition and the one-half weight if
the stationary point is an included hard endpoint.  Then, for (n=hq),

\[
\begin{aligned}
 &u_{L,H_D}(h)(hX)^{1/4}q^{-3/4}\\
 &\qquad =X^{1/4}n^{-3/4}
 v_L(h)\Phi\!\left(\frac{h}{H_D+1}\right).
 \tag{2.1}
\end{aligned}
\]

Consequently the exact grouped leading stationary term is

\[
 X^{1/4}\sum_n n^{-3/4}e(\sqrt{Xn})
 \sum_{\substack{hq=n\\q\ \mathrm{odd}}}
 \chi_4(q)v_L(h)
 \Phi\!\left(\frac{h}{H_D+1}\right)
 \omega_D^*(h,q;X).
 \tag{2.2}
\]

If the actual (L)-partition is summed first, define the full M1 angular
symbol

\[
 \Theta_X(h,q)=
 \sum_{D}^{\rm active}
 \mathbf 1_{h\leq H_D}
 \Phi\!\left(\frac{h}{H_D+1}\right)
 \omega_D^*(h,q;X),
 \tag{2.3}
\]

where (\sum_L v_L(h)=1) on the admitted frequency range is understood.
The globally grouped M1 coefficient is therefore

\[
 \boxed{
 C_X^{M1}(n)=
 \sum_{\substack{hq=n\\q\ \mathrm{odd}}}
 \chi_4(q)\Theta_X(h,q).}
 \tag{2.4}
\]

Even divisors need not be added separately, since (\chi_4(q)=0) for even
(q).  Thus the unrestricted identity is indeed

\[
 \sum_{\substack{q\mid n\\q\ \mathrm{odd}}}\chi_4(q)
 =\sum_{q\mid n}\chi_4(q)=\frac{r_2(n)}4.
 \tag{2.5}
\]

But (2.5) can replace (2.4) only after proving both of the following exact
conditions:

1. every divisor incidence (hq=n) occurs with the required endpoint
   multiplicity; and
2. (\Theta_X(h,q)=\sigma_X(n)) is independent of the chosen divisor (h)
   on that full incidence set.

Neither condition holds for the M1 RCS by itself.

## 3. Proof and derivation

### 3.1 The power and the character

Equation (2.1) is algebraic:

\[
 \frac1h(hX)^{1/4}q^{-3/4}
 =X^{1/4}h^{-3/4}q^{-3/4}
 =X^{1/4}(hq)^{-3/4}.
\]

The B-process dual mode is odd, so its sign is (\chi_4(q)).  Oddness is
not an additional arithmetic saving; it merely makes the even-divisor terms
in the Jacobi sum vanish, exactly as in (2.5).

### 3.2 Exact angular obstruction

Let (y=\lfloor\sqrt X\rfloor).  The global M1 spatial partition covers
only original denominators (d\leq y).  At a stationary incidence,

\[
 d_{h,q}\leq y
 \quad\Longleftrightarrow\quad
 \frac qh\geq \frac{4X}{y^2}.
 \tag{3.1}
\]

For (X=y^2), this is (q\geq4h); because (q) is odd, equality is
impossible.  Thus M1 retains only one angular sector of the divisor
hyperbola.  The omitted factorization (q<h) is not a negligible parity
class: it is exactly what can cancel the retained term when
(n\equiv3\pmod4).

The active lower spatial cutoff and (h\leq H_D) also impose a radial
truncation (n\ll X^{1/2}), with constants depending on the fixed shell
support.  This agrees with the natural Hardy--Voronoi truncation scale, but
does not repair the missing angular sector.

### 3.3 Dyadic partitions do not remove the actual symbol

For the accepted dyadic grid (D_j=2^{-j}y) and a telescoping profile
(w_{D_j}(d)=W(d/D_j)), a bare spatial partition can satisfy
(\sum_jw_{D_j}(d)=1).  After grouping (n=hq), however,

\[
 d_{h,q}=2h\sqrt{\frac Xn},
\]

so an individual summand of (2.3) is

\[
 W\!\left(2^{j+1}h\sqrt{\frac{X}{ny^2}}\right)
 \Phi\!\left(
 \frac{h}{\lfloor2^{-j}yX^{-1/4}\rfloor+1}
 \right).
 \tag{3.2}
\]

The first factor samples the fractional dyadic location of (h), while the
second changes when (j) changes and has discontinuous floor thresholds.
Therefore the telescoping identity for (W) cannot be pulled through
(\Phi).  For fixed (n), changing to a different divisor (h\mid n)
changes (3.2).  Near (h=H_D), replacing the floor height or the (H_D+1)
argument by a continuum approximation may change (\Phi) by order one;
there is no uniform error estimate in the accepted graph that permits that
replacement.

At a hard endpoint (d_{h,q}=y), the star gives half of a stationary term,
whereas the divisor identity (2.5) counts a divisor once.  At an exact square
the parity (q\) odd rules out the formal equality (q=4h), but for general
real (X) endpoint equality can occur.  Hence the top half weight must remain
in (\Theta_X).

### 3.4 Primary-source Hardy--Voronoi audit

The primary source used here is D. A. Popov, *Voronoi's formulae and the
Gauss problem*, **Russian Mathematical Surveys 79** (2024), 53--126,
[DOI 10.4213/rm10162e](https://doi.org/10.4213/rm10162e),
[official Math-Net PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=10162&what=fullteng).
Its notation (r(n)) is the project's (r_2(n)), and its (P(x)) is the
closed-disc circle error.

- Equations (14)--(15) give exactly
  (r_2(n)=4\sum_{d\mid n}\chi_4(d)), including the zero value of the
  character on even divisors.
- Theorem 4, equation (4.1), gives
  \[
   \overline P(x)=\sqrt x\sum_{n\geq1}
   \frac{r_2(n)}{\sqrt n}J_1(2\pi\sqrt{nx}),
  \]
  for (x>1), with midpoint counting at jumps.  The series is uniformly
  convergent only on closed intervals avoiding integers represented as two
  squares; it is not an absolutely convergent series that may be regrouped
  without a convergence argument.
- Equation (4.15) records
  \[
   J_1(t)=\left(\frac2{\pi t}\right)^{1/2}
   \cos\!\left(t-\frac{3\pi}{4}\right)+O(t^{-3/2}).
  \]
  Therefore
  \[
   \sqrt X\frac{r_2(n)}{\sqrt n}J_1(2\pi\sqrt{nX})
   =-\frac{X^{1/4}}\pi\frac{r_2(n)}{n^{3/4}}
   \cos\!\left(2\pi\sqrt{nX}+\frac\pi4\right)
   +O\!\left(X^{-1/4}\frac{r_2(n)}{n^{5/4}}\right).
  \]
  The last errors sum absolutely.
- Theorem 5, equations (5.1)--(5.2), is the pointwise truncated formula,
  valid for every (N\geq3) and (x\geq3):
  \[
   P(x)=-\frac{x^{1/4}}\pi\sum_{n\leq N}
   \frac{r_2(n)}{n^{3/4}}
   \cos\!\left(2\pi\sqrt{nx}+\frac\pi4\right)
   +\Delta_NP(x),
  \]
  \[
   \Delta_NP(x)\ll
   \sqrt{\frac xN}\,\overline r(x)+\overline r(N)\log N,
   \qquad
   \overline r(t)=\exp\!\left(\frac{\log t}{\log_2t}\right)=t^{o(1)}.
  \]

Taking (N\asymp X^{1/2}) makes this error
(O_\varepsilon(X^{1/4+\varepsilon})).  Hence a target-sized estimate for
the complete radial cosine sum is equivalent in both directions to the
Gauss-circle target, up to a target-sized term.

Finally, restoring the accepted M1 stationary prefactor from Round 9 gives
the positive exponential coefficient

\[
 -\frac{2e(1/8)}\pi X^{1/4}n^{-3/4}
 \sum_{q\mid n}\chi_4(q)
 =-\frac{e(1/8)}{2\pi}X^{1/4}r_2(n)n^{-3/4}.
\]

Twice its real part is exactly the leading cosine term in Popov's formula.
Thus a hypothetical full (r_2/4) recombination has the Hardy constant and
phase exactly; it is a return map, not merely a structural analogy.

At a representable integer (X), the infinite Bessel identity uses
midpoint counting, so the project's closed-disc (P(X)) differs by
(r_2(X)/2=O_\varepsilon(X^\varepsilon)).  This is target-safe but must be
included in any claimed exact identity.  The pointwise truncated theorem
above is already stated for the closed-disc (P(x)).

## 4. First doubtful or unproved step

The first invalid step is replacing

\[
 \sum_{hq=n}\chi_4(q)\Theta_X(h,q)
 \quad\text{by}\quad
 \sigma_X(n)\sum_{q\mid n}\chi_4(q)
\]

before proving a full angular partition and divisor-independence of
(\Theta_X).  M1 violates the full-angular condition by (3.1), and its
actual (\Phi), floor heights, endpoint star, and dyadic samples violate
divisor-independence.  No theorem or accepted calculation repairs this
seam.

A possible complementary M1--M2 symbol identity is also unproved globally.
If it were proved with total symbol (1), it would reconstruct the full
Hardy--Voronoi sum and hence would still leave an estimate equivalent to the
original target.

## 5. Required hostile control and outcome

Take an exact square (X=y^2) with (y\) sufficiently large and the prime
(n=7\equiv3\pmod4).  The factorization

\[
 (h,q)=(1,7)
\]

has

\[
 d_{1,7}=\frac{2y}{\sqrt7}<y,
\]

lies in active top-scale spatial shells, has (1\leq H_D), and is not an
endpoint.  The nonnegative exact spatial and frequency partitions and
(\Phi(1/(H_D+1))>0) give (\Theta_X(1,7)>0).  Its character is
(\chi_4(7)=-1).

The reflected divisor factorization ((h,q)=(7,1)) has

\[
 d_{7,1}=2\sqrt7,y>y
\]

and is absent from M1.  Therefore

\[
 C_X^{M1}(7)=-\Theta_X(1,7)\ne0,
 \qquad
 \frac{r_2(7)}4=\chi_4(1)+\chi_4(7)=0.
\]

**Outcome: fail.**  This exact-square prime control falsifies the proposed
M1-to-(r_2/4) completion without numerical experimentation.  It also
shows why the omitted angular divisors are essential: for primes
(3\bmod4), they cancel the retained incidence in the full Jacobi sum.

## 6. Dependencies and exact artifacts used

- `protocol.md`.
- `state/proof_obligations.yml`, especially
  `M9-M1-ordered-resonance-cell-decomposition`,
  `M9-M1-ordered-cell-Bprocess-capacity-no-go`, and
  `M9-M1-dual-restricted-convolution-RCS`.
- `state/active_campaign.yml` and the Round 14 campaign plan.
- `state/best_proof_draft.md`.
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/synthesis.md`.
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`.
- `sources/vaaler_1985.md` for the exact (\Phi(h/(H_D+1))/h)
  normalization.
- `sources/tao_trudgian_yang_2025.md` only as inherited phase-diagram
  context; no theorem from it is used here.
- Popov's primary published source and official PDF linked in Section 3.4,
  specifically equations (14)--(15), (4.1), (4.15), and Theorem 5,
  equations (5.1)--(5.2).

No other Round 14 report was read.  No numerical experiment was used.

## 7. Recommended state effect

**Promote** the exact grouped-power identity (2.1) and the exact global M1
angular coefficient (2.4), with all floor, star, and dyadic-symbol factors
retained.

**Reject** the claim that summing the M1 (D,L) partitions alone replaces
the restricted divisor character by (r_2(n)/4).  Record the exact-square
prime (n=7) control as the decisive counterexample.

**Retain open** RCS in its angular restricted-convolution form.  The smallest
noncircular remainder is the divisor-dependent symbol
(\Theta_X(h,q)), or an exact comparison of it with a complementary M2
symbol before summing over divisors.

**Record as a scoped no-go** that any completion producing the full
(r_2(n)n^{-3/4}e(\sqrt{nX})) radial sum with cutoff
(n\asymp X^{1/2}) is, by the audited truncated Voronoi formula,
equivalent to the original Gauss-circle target up to target-sized errors.
It may be globally weaker than separate blockwise estimates in a formal
logical sense, but it is not an independent easier proof interface.
