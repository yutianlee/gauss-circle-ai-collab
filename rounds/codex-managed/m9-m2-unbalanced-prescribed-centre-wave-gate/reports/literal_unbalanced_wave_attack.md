# Round 118 report: literal unbalanced prescribed-centre wave attack

Campaign: m9-m2-unbalanced-prescribed-centre-wave-gate
Task: literal_unbalanced_wave_attack
Role: discovery
Starting graph SHA-256:
d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb

## 1. Result

The full estimate

\[
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}
\tag{118.1}
\]

is **not proved**, and no target-safe strict residual subrange is found.
There is, however, a quantified literal-phase saving on a nonempty strict
region and a rigorous no-go for the proposed single coherent-run
countermodel.

Put

\[
 a=\delta-\ell,\qquad D=X^\delta,\qquad L=X^\ell .
\]

Throughout the strict unbalanced residual region,

\[
 {1\over4}<a<{1\over2}.
\tag{118.2}
\]

For every fixed flat smooth literal component, with both physical signs
and both quarter branches restored, the prescribed-centre wave satisfies

\[
 \boxed{\;
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^\varepsilon
 \min\left(
 {D\over L},
 \sqrt{XL\over D}+\sqrt{X\over LD}
 \right).
 \;}
\tag{118.3}
\]

Equivalently,

\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^{\beta(a)+\varepsilon},
\qquad
 \beta(a)=\min\left(a,{1-a\over2}\right).
\tag{118.4}
\]

The first entry in (118.3) is the exact sparse-selector/product-window
capacity.  The second is a weighted reciprocal-curvature estimate in the
\(r\)-variable, after resolving the actual \(\chi_4(r)\) into its two
quarter shifts and charging the entire \(k\)-sum.

Thus a positive-power saving is proved exactly when

\[
 a=\delta-\ell>{1\over3}.
\tag{118.5}
\]

There the saving from the absolute capacity is

\[
 X^{(3a-1)/2}.
\tag{118.6}
\]

For example, \((\delta,\ell)=(2/5,0)\) lies in the strict residual
region and (118.3) improves \(X^{2/5+\varepsilon}\) to
\(X^{3/10+\varepsilon}\).  Nevertheless, (118.2) implies
\(\beta(a)>1/4\) at every strict residual point.  Therefore (118.3)
never proves (118.1).

The candidate coherent selector run is also target-safe, even without
assuming in advance that its step is fixed.  Suppose \(U\) consecutive
denominators \(d\asymp D\) select odd \(r_d\) in one fixed class modulo
\(4\), and

\[
 |X-dr_d|\le c{D\over L}
\]

with \(c>0\) sufficiently small in terms of the fixed profiles.  Then

\[
 \boxed{\;
 U\ll
 1+
 \begin{cases}
  (D^3/(XL))^{1/2},&\delta>1/3,\\
  (D^4/(XL))^{1/3},&1/4<\delta\le1/3.
 \end{cases}
\;}
\tag{118.7}
\]

Both branches are target-safe:

\[
 {3\delta-1-\ell\over2}<{1\over4}
 \quad(\delta>1/3),
\qquad
 {4\delta-1-\ell\over3}\le {1\over9}<{1\over4}
 \quad(\delta\le1/3).
\tag{118.8}
\]

for every fixed \(\delta<1/2\), even a completely phase-aligned,
same-character, positive-kernel run is smaller than the target.  A
selected positive run also gives no lower bound for the complete wave
because the signed complement is uncontrolled.  Hence this run mechanism
cannot falsify (118.1).

The smallest remaining object is the complete signed sparse-selector
sum (118.18) below, or equivalently the complete truncated divisor wave
with all products \(|s-X|\ll D/L\) kept jointly.  A further
coefficient-preserving Poisson or B-process inversion is not a new
mechanism.

## 2. Exact statement and hypotheses

Let \(X\ge2\) be real.  Let

\[
 {1\over4}\le\delta<{1\over2},\qquad
 0\le\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463,
\tag{118.9}
\]

and put

\[
 D=X^\delta,\quad L=X^\ell,\quad
 R={X\over D},\quad K={XL\over D^2},\quad
 \Delta={D\over L}.
\tag{118.10}
\]

Fix one strict flat smooth M2 component.  Its literal numerator weight is

\[
 q_L(h)=\eta(h/L)\Phi(h/(H_D+1)),
\qquad H_D=\lfloor DX^{-1/4}\rfloor,
\tag{118.11}
\]

with the inherited nonnegative smooth profile and Vaaler taper.  The
denominator profile \(W\) is the literal fixed smooth profile.  All
normalized smooth seminorms are uniform.  The proved statement does not
replace either profile by a rectangular cutoff.

The two exact forms of the wave are

\[
 \mathscr R_{D,L}(X)
 =
 \sum_s\sum_{\substack{r\mid s\\r\ {\rm odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \mathcal Q_L\!\left({r(X-s)\over4X}\right),
\tag{118.12}
\]

\[
 \mathcal Q_L(y)=
 \int_0^\infty {q_L(h)\over h}e(hy)\,dh,
\tag{118.13}
\]

and

\[
 \mathscr R_{D,L}(X)
 =
 \sum_{\substack{r\asymp R\\r\ {\rm odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\asymp K}
 {q_L(4Xk/r^2)\over k}e(Xk/r),
\tag{118.14}
\]

up to the already accepted rapidly decaying Poisson tail.  Equations
(118.12) and (118.14) are coefficientwise equivalent.  The physical
normalization is the accepted

\[
 \mathcal B^+_{L,W}
 =-{i\over2\pi}\mathscr R_{D,L}(X)+O_W(1)
\tag{118.15}
\]

on a flat smooth component; the aggregate stationary remainder is
target-safe.  Negative physical frequency is the conjugate component.

Sharp clipped profiles, prescribed stars, the hard band, and arithmetic
owner boundaries have their own exact Fresnel or endpoint kernels.  They
are not included in (118.3) and are not declared errors.  Thus (118.3) is
a proper flat-smooth result, not closure of the complete UNBAL parent.

## 3. Proof or derivation

### Product window and sparse selector

For fixed \(r\asymp R\), the \(k\)-weight in (118.14) has support length
\(O(K)\), supremum \(O(K^{-1})\), and total variation \(O(K^{-1})\).
Abel summation gives

\[
 \left|
 \sum_k {q_L(4Xk/r^2)\over k}e(Xk/r)
 \right|
 \ll
 \min\left(1,{1\over K\|X/r\|}\right).
\tag{118.16}
\]

If \(\|X/r\|<\eta\), an integer \(d\asymp D\) satisfies

\[
 |X-rd|\ll \eta R.
\tag{118.17}
\]

The possible integer products \(rd\) lie in a real interval containing
\(O(1+\eta R)\) integers, and each has \(O_\varepsilon(X^\varepsilon)\)
divisor pairs.  Dyadic layer-cake summation from \(\eta=K^{-1}\) to
\(1/2\) proves

\[
 \sum_{r\asymp R}
 \min\left(1,{1\over K\|X/r\|}\right)
 \ll_\varepsilon {R\over K}X^\varepsilon
 ={D\over L}X^\varepsilon.
\tag{118.18}
\]

This proves the first entry in (118.3).  It also makes the selector
literal: at fixed \(r\), its \(d\)-width is
\[
 {\Delta\over R}={1\over K},
\]
so only \(O(1)\) denominators occur; globally there are
\(\Delta X^\varepsilon\) weighted incidences.  No divisor orientation is
completed to \(r_2/4\).

### Reciprocal curvature

For a fixed \(k\asymp K\), write

\[
 \chi_4(r)={e(r/4)-e(-r/4)\over2i}.
\tag{118.19}
\]

The two phases are

\[
 f_\pm(r)={Xk\over r}\pm{r\over4},
\qquad
 |f_\pm''(r)|={2Xk\over r^3}
 \asymp {LD\over X}.
\tag{118.20}
\]

The linear quarter shift does not change the curvature.  For fixed \(k\),
the amplitude

\[
 w_k(r)={1\over k}
 W\!\left({X\over rD}\right)q_L(4Xk/r^2)
\]

has

\[
 \|w_k\|_\infty+\operatorname{Var}_r(w_k)\ll K^{-1}.
\tag{118.21}
\]

This includes support entry and exit because the flat profiles vanish
smoothly at their collars.  The inherited Vaaler taper changes on scale
at least \(L\), and therefore obeys the same normalized variation bound.

The elementary weighted second-derivative estimate

\[
 \left|\sum_{n\in I}w(n)e(f(n))\right|
 \ll
 (\|w\|_\infty+\operatorname{Var}w)
 \left(N\sqrt\lambda+\lambda^{-1/2}\right)
\tag{118.22}
\]

holds when \(f''\asymp\lambda\) is monotone on an interval of length
\(N\).  It follows from Weyl differencing with
\(H=\min(N,\lceil\lambda^{-1/2}\rceil)\), followed by Abel summation.
Apply (118.22) with

\[
 N\asymp R={X\over D},\qquad
 \lambda\asymp {LD\over X}.
\]

For each \(k\),

\[
 \left|
 \sum_{r\ {\rm odd}}\chi_4(r)w_k(r)e(Xk/r)
 \right|
 \ll {1\over K}
 \left(\sqrt{XL\over D}+\sqrt{X\over LD}\right).
\tag{118.23}
\]

There are \(O(K)\) values of \(k\).  Taking the \(k\)-triangle after,
not before, the signed reciprocal \(r\)-sum proves the second entry in
(118.3).  No Cauchy factor is used.  A second B-process is deliberately
not applied: the accepted Round-107 identity shows that it restores the
physical packet and its coefficient capacity.

Since \(a=\delta-\ell\), the first term in the curvature bound has
exponent \((1-a)/2\), while the second has exponent
\((1-\delta-\ell)/2\le(1-a)/2\).  Comparison with the absolute exponent
\(a\) proves (118.4)--(118.6).  Because \(1/4<a<1/2\),

\[
 \min\left(a,{1-a\over2}\right)>{1\over4},
\]

which proves that this mechanism has no target-safe strict subrange.

### Exact centre, near-centre sign, and arithmetic controls

If \(X\notin\mathbb Z\), there is no exact-centre term.  If \(X=N\) is
an integer, the central contribution is

\[
 \mathcal Q_L(0)
 \sum_{\substack{r\mid N\\r\ {\rm odd}}}
 \chi_4(r)W\!\left({N\over rD}\right)
 \ll_\varepsilon X^\varepsilon,
\tag{118.24}
\]

since \(\mathcal Q_L(0)\ll1\).  It is always target-safe.  If two
integers tie around the real centre, then
\(\mathcal Q_L(-y)=\overline{\mathcal Q_L(y)}\), but their truncated
divisor sets and profiles differ, so no cancellation or positivity is
forced.  Each tied product remains divisor-bounded.

Because \(q_L(h)/h\ge0\), there is a constant \(c_0>0\), depending only
on the fixed nondegenerate profile, such that

\[
 \Re\mathcal Q_L\!\left({r(X-s)\over4X}\right)>0
\tag{118.25}
\]

whenever
\[
 |X-s|\le c_0{D\over L},\qquad r\asymp{X\over D}.
\]
Indeed, then \(h\,r(X-s)/(4X)\) stays in a sufficiently short interval
on which the cosine is positive.  This certifies the sign of a genuinely
near-centre subpacket, but not the sign of its complement.

For \(N=p\) prime, the strict active orientation
\(r\asymp N/D\) contains neither central divisor \(1\) nor \(p\).
For a prime square, the only new divisor \(\sqrt N\) lies on the
\(D\asymp\sqrt X\) hard boundary, not in a fixed strict
\(\delta<1/2\) component.  For a prime fourth power, the possible
intermediate exact orientations occur only on the terminal or hard
power boundaries.  General squares, fourth powers, and divisor-rich
integers can contain active divisors, but (118.24) is still
\(X^\varepsilon\).  None is a literal central countermodel.

### Coherent-run no-go

Let \(d\) run through \(U\) consecutive integers in a fixed dyadic
interval \(d\asymp D\).  Assume that every selected \(r_d\) lies in one
fixed odd residue class modulo \(4\) and

\[
 |X-dr_d|\le c\Delta
\tag{118.26}
\]

with \(c>0\) sufficiently small.  Then

\[
 \left|r_d-{X\over d}\right|
 \le {C c\over L}.
\tag{118.27}
\]

All finite differences of \(r_d\) are multiples of \(4\).  On the other
hand, for \(f(x)=X/x\),

\[
 |\Delta^2 f(d)|\ll {X\over D^3},\qquad
 |\Delta^3 f(d)|\ll {X\over D^4}.
\tag{118.28}
\]

The error in the second and third finite differences contributed by
(118.27) is at most \(4Cc/L\) and \(8Cc/L\), respectively.  Choose
\(c\) smaller than an absolute constant depending on the fixed dyadic
support.

If \(\delta>1/3\), then \(X/D^3=o(1)\).  For sufficiently large \(X\),
\(\Delta^2r_d\), a multiple of \(4\), has absolute value below \(2\);
hence

\[
 \Delta^2r_d=0
\tag{118.29}
\]

throughout the run, so \(r_d\) is affine.  Comparing the values of
\(X/d-r_d\) at the two endpoints and midpoint, convexity and
\(f''(x)\asymp X/D^3\) give

\[
 {XU^2\over D^3}\ll {1\over L}.
\tag{118.30}
\]

If \(1/4<\delta\le1/3\), then \(X/D^4=o(1)\).  The same lattice-gap
argument gives

\[
 \Delta^3r_d=0,
\tag{118.31}
\]

so \(r_d\) is quadratic.  Comparing four equally spaced points, or
using the third divided difference and
\(|f'''(x)|\asymp X/D^4\), gives

\[
 {XU^3\over D^4}\ll {1\over L}.
\tag{118.32}
\]

Equations (118.30)--(118.32) prove the two branches of (118.7).  This
also treats ties: the central-lobe constant makes the error smaller than
half the spacing \(4\), so a tied choice cannot switch between two
same-residue lattice values.

On an interior part of the fixed \(W\)-profile, (118.25) and the fixed
residue class of \(r_d\) make every selected real part point in the same
direction.  Its total size is nevertheless \(O(UX^\varepsilon)\), which
is \(o(X^{1/4})\) by (118.8).  Thus even the strongest same-residue
central-lobe run is target-safe.  Moreover, this is only a bound on the
selected run; no sign is known for all remaining products.  It cannot
serve as a lower bound for the complete wave.

## 4. First doubtful or unproved step

The first unproved analytic assertion after (118.3) is cancellation in
the complete sparse selector beyond both one-dimensional envelopes:

\[
 \sum_{\substack{r\asymp X/D\\r\ {\rm odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
\sum_k {q_L(4Xk/r^2)\over k}e(Xk/r)
\ll_\varepsilon X^{1/4+\varepsilon}.
\tag{118.33}
\]

In the saving region \(a>1/3\), the remaining excess is

\[
 X^{(1-2a)/4}
\tag{118.34}
\]

over the target.  A proof must exploit the joint dependence of the
sparse selector on \(r\) and \(k\), or an inverse theorem controlling
all coherent selector components and their signed complement.  Taking
the \(k\)-triangle as in (118.23) loses precisely that joint information.

Outside the flat smooth scope, the earlier seam is the exact endpoint
kernel.  A sharp, starred, hard, or arithmetic-owner term cannot be
absorbed into (118.21); its one-sided Fresnel kernel and owner must remain
attached.  Therefore even a proof of (118.33) for every flat smooth
component would not by itself close hard TOP, BAL, or all UNBAL
boundaries.

The exact centre, positive near-centre core, prime powers, divisor-rich
centres, and a single coherent run do not falsify (118.33).  They are
all target-safe or fail to control the complete signed complement.

## 5. Control tests and outcomes

| Control | Exact test and charged factors | Outcome |
|---|---|---|
| Literal wave and physical normalization | Use (118.12)--(118.15), including the accepted factor \(-i/(2\pi)\) and target-safe flat-smooth stationary remainder. | Pass.  No physical scale is changed. |
| Product/reciprocal equivalence | Apply the accepted \(k\)-Poisson identity coefficientwise. | Pass.  (118.12) and (118.14) retain the same profiles and character orientation. |
| Exact centre and tie | Evaluate \(s=X\) only when \(X\) is integral; use conjugacy for tied residuals without equating their divisor sets. | Pass.  Central and tied contributions are divisor-bounded, not obstructive. |
| Near-centre kernel sign | Use nonnegativity of \(q_L/h\) and restrict \(|X-s|\le c_0D/L\). | Pass for the selected core.  The complement has no certified sign. |
| Prime, square, fourth power, divisor-rich | List the active exact divisors and compare with strict terminal/hard orientations. | Pass.  Exact-centre mass is always \(X^\varepsilon\); no countermodel results. |
| Coherent selector run | Use the mod-\(4\) lattice gap with the second finite difference for \(\delta>1/3\) and the third finite difference for \(\delta\le1/3\). | Pass as a no-go: both branches of (118.7) are \(o(X^{1/4})\). |
| Coherent complement | Compare the selected run with all other active \((r,d)\) incidences. | Fail for a lower-bound proof: the complement is uncontrolled and may cancel it. |
| Character and both signs | Resolve \(\chi_4(r)\) exactly as (118.19); restore the conjugate physical frequency. | Pass.  The quarter shifts are retained and do not alter curvature. |
| Profile support | Prove (118.21) from the literal flat profiles and Vaaler taper. | Pass only for flat smooth components. |
| Endpoint kernels | Test a sharp/starred/hard entry against the BV extension used in (118.21). | Out of scope, retained as an exact separate survivor; it is not declared target-safe. |
| Selector capacity | Use (118.16)--(118.18), including every divisor multiplicity. | Pass: \(D/L\), with no hidden Cauchy or rectangle factor. |
| Curvature capacity | Charge \(R\sqrt{LD/X}+\sqrt{X/(LD)}\), the \(K^{-1}\) amplitude, and \(K\) outer values. | Pass: the second entry in (118.3). |
| Capacity comparison | Put \(a=\delta-\ell\). | Pass: saving \(X^{(3a-1)/2}\) for \(a>1/3\), but \(\beta(a)>1/4\) throughout the strict region. |
| Actual versus unsigned/adversarial | Remove \(\chi_4\), then phase-conjugate the \(r,k\) coefficient. | The curvature estimate also bounds the literal unsigned phase sum, but not an arbitrary coefficient: phase conjugation deletes (118.20) and can restore selector capacity \(D/L\). |
| Second transform | Apply a second coefficient-preserving B/Poisson step after (118.23). | Scoped fail: Round 107 returns the original packet and supplies no additional norm gain. |
| Round-117 transfer | Compare only the product-window algebra, then recompute \(R,K,\Delta\). | Pass in scope.  No \(Y^{1/8}\) or \(Y^{1/6}\) exponent is imported. |
| Strict residual region | Intersect (118.5) with (118.9), for example \((2/5,0)\). | Nonempty quantified-saving region; no target-safe region. |
| Downstream scope | Compare the flat smooth component with the complete M2 conjunction. | No implication to endpoint packets, hard TOP, BAL, all UNBAL, M9-M2, M9, uniformity, or the quarter theorem. |

All tests are analytic.  No numerical experiment, Cauchy step, or
external theorem is used.

## 6. Dependencies and exact artifacts used

This report used every context file assigned in the task brief:

1. protocol.md, for graph authority, signed/unsigned separation, and the
   seven-section report contract;
2. state/proof_obligations.yml, for the exact status and statements of
   the unbalanced three-quarter estimate, the fixed-centre return,
   M9-M2, and the downstream target;
3. state/active_campaign.yml, for the frozen wave, strict residual
   region, controls, promotion threshold, and graph hash;
4. strategy/conductor_0821_full_proof_strategy.md, for the prescribed
   falsification gate and the prohibition on another unpriced inversion;
5. rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md,
   for the accepted physical normalization, wave width, transform
   capacity, and owner scope;
6. rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reports/truncated_r2_recombination_attack.md,
   for the exact literal profiles, reciprocal row, product wave, and
   stationary-error ledger;
7. rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_recombination_and_capacity.md,
   for the accepted no-completion result and missing factor;
8. rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/synthesis.md,
   for the product-window lemma and the exact nontransfer scope;
9. rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/derivation_packet.md,
   for the selector, coherent-run, curvature, and promotion diagnostics;
   and
10. rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/candidates/conductor_wave_probe.md,
    for the proposed reciprocal-run falsification control.

The only added analytic inputs are Abel summation, the elementary divisor
bound, the product-window layer cake, the weighted second-derivative
estimate proved in Section 3, and the exact quadratic run calculation.
No sibling Round-118 report, web source, or computation was used.

## 7. Recommended state effect

**Promote after independent seam review** the combined flat-smooth bound
(118.3)--(118.4).  Record the nonempty quantified-saving region
\(\delta-\ell>1/3\), with exact gain \(X^{(3(\delta-\ell)-1)/2}\)
and remaining target excess \(X^{(1-2(\delta-\ell))/4}\).  Record
explicitly that this does not close any strict residual point.

**Promote after seam review** the scoped coherent-run no-go
(118.7)--(118.8): any consecutive same-\(\chi_4\) central-lobe selector
run is forced affine for \(\delta>1/3\), quadratic for
\(\delta\le1/3\), and has length \(o(X^{1/4})\); a
positive selected run cannot lower-bound the complete signed wave without
its complement.

**Retain open** M9-M2-smooth-unbalanced-three-quarter-estimate.  Its
smallest flat-smooth survivor is the complete joint selector (118.33),
not the exact centre, an \(r_2/4\) completion, or one coherent run.
Retain the exact endpoint kernels as separate open seams outside this
flat-smooth statement.

**Reject** the proposed single coherent-run countermodel, positivity of a
near-centre subset as a lower bound, clean divisor completion, a second
coefficient-preserving transform followed by a norm, and direct import of
the Round-117 exponents.

**No change** is licensed for hard TOP, balanced M2, the complete UNBAL
parent, M9-M2, M9-M1, endpoint uniformity, M9, the certified pointwise
exponent, or the Gauss-circle quarter target.
