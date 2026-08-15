# Blind rederivation: subcritical small-angle collapse

## 1. Result

**Small-angle multiplier lemma, sharp triangle threshold, and signed-sum
no-go.**  Fix \(0<\nu<1/2\), let a smooth radial block have
\(n\asymp N=X^\nu\), and put
\[
 d_{n,h}=2h\sqrt{X/n},\qquad
 \kappa_X={y\over2\sqrt X},\qquad
 \lambda_X={1\over\kappa_X^2}={4X\over y^2}.              \tag{1}
\]
For all sufficiently large \(X\), uniformly over every divisor
\(h\mid n\) with \(q=n/h\) odd,
\[
 \boxed{\Omega_X^*(n,h)
 =\mathbf1_{d_{n,h}\le y}^{*}+O_V(n/Y).}                 \tag{2}
\]
Here the star on the indicator means ordinary weight for
\(d_{n,h}<y\), half-weight at the hard stationary equality
\(d_{n,h}=y\), and zero for \(d_{n,h}>y\).  Internal smooth-profile
seams do not create a second star.  The exact active height indicators
are one on every profile that contains \(d_{n,h}\); the bottom profile
is identically absent there; and the floor \(H_j+1\) improves, rather
than worsens, the required bound.

The sharp small-angle estimate is
\[
 1-\Phi(u)=(1-u)(1-\pi u\cot(\pi u))asymp u^2             \tag{3}
\]
uniformly on the actual supported range for large \(X\), with
\[
 \Phi(u)-1=-{\pi^2\over3}u^2+O(u^3).                      \tag{4}
\]
In particular, the exponent two cannot be improved uniformly as
\(u\to0\).

The limiting arithmetic coefficient has the exact forms
\[
 \begin{aligned}
 \mathcal D_X^*(n)
 &=\sum_{\substack{hq=n,\ q\ \operatorname{odd}\\q\ge\lambda_Xh}}^{*}
       \chi_4(q)\\
 &=\sum_{\substack{q\mid n,\ q\ \operatorname{odd}\\
       q\ge2\sqrt{Xn}/y}}^{*}\chi_4(q).                  \tag{5}
 \end{aligned}
\]
If \(n=2^a m\) with \(m\) odd, then more explicitly
\[
 \mathcal D_X^*(2^am)
 =\chi_4(m)
  \sum_{\substack{r\mid m\\
     r\le\kappa_X2^{-a/2}\sqrt m}}^{*}\chi_4(r).         \tag{6}
\]
This is an incomplete, off-diagonal signed divisor sum.  The usual full
divisor-character identity does not remove its moving cutoff, so (6) is
not multiplicative in \(n\).

Writing \(\Delta_X(n)=\mathcal C_X^*(n)-\mathcal D_X^*(n)\),
equation (2) gives
\[
 |\Delta_X(n)|\ll_V\tau(n){n\over Y}.                     \tag{7}
\]
Consequently, for a fixed smooth block,
\[
 \sum_n |V(n/N)|n^{-3/4}|\Delta_X(n)|
 \ll_V {N^{5/4}\log(2N)\over Y}.                          \tag{8}
\]
Thus the exact power threshold of the triangle argument is
\(\nu=2/5\): it gives a power saving for fixed \(\nu<2/5\), gives
\(O_V(\log X)\subset O_{\varepsilon,V}(X^\varepsilon)\) at
\(\nu=2/5\), and fails by a fixed power for \(\nu>2/5\).
The endpoint is therefore included for an \(X^\varepsilon\) target;
the stricter \(N\le X^{2/5-\epsilon_0}\) is needed only if one demands
a genuine power saving.

No signed estimate of size \(X^\varepsilon\) for the limiting sum follows
from the multiplier identity.  Its trivial bound is
\(O_V(N^{1/4}\log(2N))\), and a direct one-variable curvature treatment
returns at best the physical \(R=X^{1/4}\) scale.  A new bilinear or
arithmetic cancellation theorem for (5) is still required.

## 2. Exact statement and hypotheses

Assume the exact nonnegative denominator partition and the angular
coefficient (62.1) in the authorized packet.  Interpret its consistent
stationary star as a linear endpoint functional: at a genuine hard
endpoint it multiplies the stationary value by \(1/2\), while away from
such an endpoint it leaves the value unchanged.  Thus, at a fixed real
stationary denominator \(d\),
\[
 \sum_j[w_j(d)]^*
 =\left[\sum_jw_j(d)\right]^*,                             \tag{9}
\]
and a smooth internal profile overlap does not independently halve a
term.  At \(d=y\), the right side is \(1/2\); at \(d<y\) it is one,
provided the bottom weight is zero.

Let \(V\) be supported in a fixed compact subinterval of
\((0,\infty)\), so that
\[
 A N\le n\le B N                                           \tag{10}
\]
on the block, with fixed \(0<A<B\).  Use the fixed profile-support
constants implicit in the accepted relation (62.4): if \(w_j(d)\ne0\),
then \(d\asymp D_j\), uniformly in \(j\).  The conclusion (2) holds for
all sufficiently large \(X=X_0(V,\nu)\).  Its implied constant may
depend on the fixed radial and profile supports but not on \(n,h,j,X\).

The exact floor, endpoint, and owner conventions are:

- \(H_j=\lfloor D_j/R\rfloor\), and the coefficient retains
  \(\mathbf1_{h\le H_j}\) exactly;
- the top value \(d=y\) is the only relevant hard denominator endpoint
  and carries its single stationary half-weight;
- prescribed profile or equality stars remain attached to their own
  values, but no coincident owner is silently substituted for another;
- the bottom range is not inserted into \(\Omega_X^*\); it will instead
  be proved disjoint from the subcritical stationary support; and
- the smooth radial multiplier is kept exact.  Estimate (8) measures
  only replacement of \(\Omega_X^*\) by its limiting multiplier.

## 3. Proof and derivation

### Bottom exclusion and active-height floors

From (10) and \(h\ge1\),
\[
 d_{n,h}=2h\sqrt{X/n}
 \ge {2\over\sqrt B}X^{(1-\nu)/2}.                        \tag{11}
\]
Therefore
\[
 {d_{n,h}\over R}
 \ge {2\over\sqrt B}X^{(1-2\nu)/4}\longrightarrow\infty. \tag{12}
\]
Since the bottom weight is supported on \(d<4R/3\), it vanishes at every
such stationary denominator once \(X\) is large.  This also excludes the
lower hard endpoint \(d=1\).

Suppose \(w_j(d_{n,h})\ne0\).  For a fixed support constant \(K\),
\(d_{n,h}\le K D_j\), so
\[
 {h\over D_j/R}
 ={d_{n,h}\over2D_j}\sqrt{n/Y}
 \le {K\over2}\sqrt{n/Y}=o(1).                            \tag{13}
\]
Equations (12) and profile comparability also give
\(D_j/R\to\infty\).  Hence, uniformly for every containing profile and
all large \(X\),
\[
 h\le {1\over2}{D_j\over R}
 \le\left\lfloor{D_j\over R}\right\rfloor=H_j.           \tag{14}
\]
The last inequality holds after enlarging \(X_0\), since
\(D_j/R\ge2\).  Thus every active cutoff in (62.1) equals one; profiles
with \(H_j=0\) cannot contain the stationary point.

Moreover, the exact floor denominator satisfies
\(H_j+1>D_j/R\), whence
\[
 0<u_j={h\over H_j+1}
 <{hR\over D_j}
 \le {K\over2}\sqrt{n/Y}.                                \tag{15}
\]
This proves the uniform small-angle range without replacing
\(H_j+1\) by an asymptotic surrogate.

### Sharp Vaaler multiplier bound

Algebra applied to (62.2) gives the exact identity
\[
 1-\Phi(u)=(1-u)(1-\pi u\cot(\pi u)).                     \tag{16}
\]
The function
\[
 G(u)={1-\Phi(u)\over u^2}
\]
extends continuously to \(u=0\), with
\(G(0)=\pi^2/3\), by the Laurent expansion of \(\cot\).  Hence for
some fixed \(u_0>0\),
\[
 0<c_0u^2\le1-\Phi(u)\le C_0u^2
 \qquad(0<u\le u_0).                                     \tag{17}
\]
Equation (15) puts every supported \(u_j\) in this interval for large
\(X\).  It follows that
\[
 |\Phi(u_j)-1|\ll u_j^2\ll n/Y,                            \tag{18}
\]
and the nonzero limit of \(G(u)\) proves sharpness.  Expanding one term
further gives (4); in particular, the apparent linear term cancels
exactly.

### Partition, stars, and proof of the multiplier identity

For \(d=d_{n,h}\le y\), bottom exclusion, the exact partition, and
linearity of the consistent star give
\[
 \sum_j[w_j(d)]^*=\mathbf1_{d\le y}^*.                    \tag{19}
\]
For \(d>y\), every top/interior profile is zero and both sides vanish.
At \(d=y\), (19) reads one half on both sides.  A smooth profile seam is
already resolved by the telescoping weights from
\(W(t)=\eta(t)-\eta(2t)\), so it does not generate an additional
endpoint factor.

Using (14), insert and subtract one in each Vaaler factor:
\[
 \begin{aligned}
 \Omega_X^*(n,h)
 &=\sum_j[w_j(d)]^*
   +\sum_j(\Phi(u_j)-1)[w_j(d)]^* .                       \tag{20}
 \end{aligned}
\]
The weights are nonnegative, their starred sum is at most one, and (18)
is uniform in every containing profile.  Therefore the second sum is
\(O(n/Y)\); (19) proves (2).  If multiple smooth profiles overlap, their
nonnegative partition weights average the individual errors rather than
adding a logarithmic multiplicity.

### Exact arithmetic cutoff

The hard condition is exactly
\[
 d_{n,h}\le y
 \iff h\le\kappa_X\sqrt n
 \iff q={n\over h}\ge\lambda_X h,                         \tag{21}
\]
including the factor \(y/\sqrt X\).  Equality in any line carries the
same single star.  This proves (5).  Notice
\[
 0<\kappa_X\le{1\over2},\qquad \lambda_X\ge4,              \tag{22}
\]
with equality precisely when \(\sqrt X\) is an integer.

If \(n=2^am\), \(m\) odd, the condition that \(q=n/h\) be odd forces
\(h=2^ar\), \(r\mid m\), and \(q=m/r\).  Equation (21) becomes
\[
 r\le\kappa_X2^{-a/2}\sqrt m.                             \tag{23}
\]
Complete multiplicativity of \(\chi_4\) on odd integers gives
\(\chi_4(m/r)=\chi_4(m)\chi_4(r)\), proving (6).  Without (23), the
full divisor sum \(\sum_{r\mid m}\chi_4(r)\) has the familiar
multiplicative simplification.  The asymmetric moving cutoff (23) is
not invariant under \(r\leftrightarrow m/r\), so that simplification
does not determine \(\mathcal D_X^*\).

### Total radial replacement error and the two-fifths threshold

For each \(n\), there are at most \(\tau(n)\) admissible divisors \(h\).
Taking absolute values in (2) proves (7).  Since
\[
 \sum_{n\le T}\tau(n)
 =\sum_{ab\le T}1
 \le T\sum_{a\le T}{1\over a}
 \ll T\log(2T),                                           \tag{24}
\]
partial summation, or simply \(n^{1/4}\asymp N^{1/4}\) on the block,
gives
\[
 {1\over Y}\sum_{n\asymp N}|V(n/N)|\tau(n)n^{1/4}
 \ll_V {N^{5/4}\log(2N)\over Y},                         \tag{25}
\]
which is (8).  If \(N=X^\nu\), its power is
\[
 X^{(5\nu-2)/4}\log X.                                   \tag{26}
\]
For fixed \(\nu<2/5\), this has a genuine negative power after absorbing
the logarithm.  At \(\nu=2/5\), it is \(O_V(\log X)\), hence admissible
under every \(X^\varepsilon\) target but not uniformly \(O(1)\) by this
argument.  For fixed \(\nu>2/5\), (26) has positive power; only signed
cancellation in the error could improve it.  More generally, if
\(N=X^{2/5}L(X)\), the bound is
\(O_V(L(X)^{5/4}\log X)\), so any polylogarithmic displacement remains
\(X^\varepsilon\)-safe although it changes the explicit logarithm.

### Signed limiting sum and capacity check

The exact reparametrization of (62.9) is
\[
 \mathcal S_V(N)=
 \sum_{\substack{h\ge1,\ q\ge\lambda_Xh\\q\ \operatorname{odd}}}^{*}
 \chi_4(q)V(hq/N)(hq)^{-3/4}e(\sqrt{Xhq}).                \tag{27}
\]
Absolute summation gives only
\[
 |\mathcal S_V(N)|\ll_V N^{1/4}\log(2N),                 \tag{28}
\]
which is a fixed power for every fixed \(\nu>0\).

For completeness, fixing \(h\), putting \(Q\asymp N/h\), and applying
the standard second-derivative estimate on each odd residue class to
\(f_h(q)=\sqrt{Xhq}\) uses
\[
 |f_h''(q)|\asymp {X^{1/2}h^2\over N^{3/2}}.              \tag{29}
\]
After the weight \((hq)^{-3/4}\), its two terms sum over
\(h\ll\sqrt N\) to
\[
 \mathcal S_V(N)\ll_{\varepsilon,V}X^{1/4+\varepsilon}.  \tag{30}
\]
This is no better than the physical \(R\)-scale and is weaker than (28)
throughout \(N\le Y\).  Thus elementary divisor identities, triangle
summation, and one-variable curvature do not provide the normalized
\(X^\varepsilon\) signed bound.  Equation (27) exposes the required new
interface: cancellation must couple the truncated hyperbola variables
or exploit arithmetic beyond the full divisor-character identity.

## 4. First doubtful or unproved step

Under the packet's accepted exact partition and consistent stationary
star, the multiplier identity (2), its floors and endpoint ownership,
the arithmetic formulas (5)--(6), the radial error (8), and the inclusive
\(2/5\) threshold are proved above.  If “star” were not a linear common
hard-endpoint convention, (9) would need an additional definition; the
packet's single-star notation and exact partition are used in precisely
that standard sense.

The first genuinely unproved step is an \(X^\varepsilon\) signed estimate
for (27).  The cutoff \(q\ge\lambda_Xh\) prevents replacement by a full
multiplicative divisor sum, and the available elementary bounds stop at
(28), while direct curvature returns (30).  For \(\nu>2/5\), a signed
estimate for the coefficient-replacement error is additionally required,
because its triangle bound already exceeds the normalized target.

No conclusion about the original GAR sector follows merely from the
pointwise multiplier approximation unless all transform remainders and
the separately target-safe bottom owner are recombined with their exact
normalizations.  The packet supplies no new signed theorem that would
perform that final step.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| multiplier_identity | **Pass.** Equations (18)--(20), nonnegativity, and the exact partition prove (2) with no profile-count loss. |
| Phi_uniformity | **Pass and sharp.** Equations (16)--(18) give \(|\Phi(u)-1|\asymp u^2\) on the actual range and recover the coefficient \(-\pi^2/3\). |
| active_cutoff | **Pass.** Equations (11)--(14) exclude bottom-scale profiles and prove every containing active indicator equals one. |
| floor_Hplus1 | **Pass.** The exact inequality \(H_j+1>D_j/R\) yields (15); no replacement by \(H_j\) is needed. |
| hard_top_and_stars | **Pass under the accepted common-star convention.** Equation (19) gives one half at \(d=y\), one in the interior, and no duplicate star at smooth seams. |
| bottom_owner | **Pass.** Equation (12) makes the stationary denominator exceed \(4R/3\) uniformly for every fixed \(\nu<1/2\). |
| arithmetic_form | **Pass.** Equations (5)--(6) retain the exact \(y/\sqrt X\) factor and show why the incomplete sum is not multiplicative. |
| radial_error | **Pass.** Equation (25) gives \(N^{5/4}\log(2N)/Y\) by an elementary divisor mean. |
| two_fifths_threshold | **Pass with inclusive endpoint.** Fixed \(\nu<2/5\) gives power decay; \(\nu=2/5\) gives only a logarithm but is \(X^\varepsilon\)-safe; fixed \(\nu>2/5\) is not triangle-safe. |
| signed_estimate | **No-go for elementary routes.** Trivial summation gives (28), and one-variable second derivative gives only (30); a new coupled cancellation input is needed. |
| downstream_scope | **Pass.** No full GAR, M9-M1, M9, or final Gauss-circle exponent is asserted. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The exact denominator partition, angular coefficient, Vaaler profile,
   support relation, and bottom-owner statement in the authorized
   Round-62 packet.
2. Elementary Taylor/Laurent expansion of \(\cot\), divisor counting,
   Mellin-free absolute summation, and the standard one-variable
   second-derivative estimate used only for the capacity check.

Isolation ledger:

- Read exactly
  `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/briefs/blind_small_angle_rederivation.md`
  and
  `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/derivation_packet.md`.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  any other brief, any other Round-62 report, validation matrices, or
  shared proof state.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared-state edit.

## 7. Recommended state effect

**Promote the small-angle collapse through the inclusive two-fifths
triangle threshold; retain the signed sum as open.**  Promote (2), the
sharp \(u^2\) multiplier estimate, the exact active-floor and bottom
exclusion lemmas, the arithmetic forms (5)--(6), and the total error
bound (8).  Record that \(\nu=2/5\) is admissible for an
\(X^\varepsilon\) target with a logarithmic loss, whereas a fixed
positive gap below \(2/5\) is needed for power decay.

Do not promote an elementary simplification or an
\(X^\varepsilon\) estimate for (62.9): the truncated divisor condition is
the remaining arithmetic obstruction, and (28)--(30) do not close it.
For \(\nu>2/5\), also retain the signed multiplier-error estimate as a
separate need.  Make no shared-state change toward full GAR, M9-M1, M9,
or the final exponent without those new signed estimates.
