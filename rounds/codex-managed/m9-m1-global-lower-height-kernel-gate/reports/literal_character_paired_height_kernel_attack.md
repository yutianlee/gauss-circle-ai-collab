# Round 121 report: literal character-paired height-kernel attack

- Campaign: `m9-m1-global-lower-height-kernel-gate`
- Task: `literal_character_paired_height_kernel_attack`
- Role: selected-context discovery/formalization
- Starting graph SHA-256: `54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`
- Status: candidate evidence only; no shared proof state is changed here.

## 1. Result: a corrected flattening lemma, a safe amplitude seam, and an exact no-gain return

The proposed full-profile aggregation is lawful and its mod-four amplitude
seam is target-safe.  More is true after choosing the already-lawful lower
cutoff sufficiently close to zero: the complete floor-perturbed profile can
be flattened to one sharp denominator cone at cost
\(O_{\varepsilon,s_0}(R X^\varepsilon)\).  This validates the main idea of
the conductor candidate, subject to the two explicit repairs recorded below:
the inactive-bottom support constant must be stated, and the claimed
two-variable separation must use a uniformly summable high-regularity
Fourier expansion rather than a bare \(C^1\) assertion.

Put

\[
 R=X^{1/4},\qquad Y=\sqrt X=R^2,\qquad y=\lfloor Y\rfloor,
 \qquad D_j=2^{-j}y,\qquad H_j=\lfloor D_j/R\rfloor,
\]

and omit \(H_j=0\) before forming any height quotient.  For

\[
 a_j(h)={\bf1}_{1\leq h\leq H_j}
 \Phi\!\left({h\over H_j+1}\right),\qquad
 A_X(h,d)=\sum_j a_j(h)w_j(d),
\]

define

\[
 b_X(h,d)=A_X(h,d)V_{\rm low}(4R^2h^2/d^2)
\]

with zero extension at every physical denominator edge.  Then the exact
positive reciprocal antecedent is

\[
 \mathcal B_{\rm low}^+
 =\sum_{h,d\geq1}{\chi_4(d)\over h}b_X(h,d)e(hX/d),
 \tag{1.1}
\]

and

\[
 \mathcal B_{\rm low}^+
 ={e(1/8)\over i}R,G_{\rm low}(X)+O_{s_0}(\log^2(2X)).
 \tag{1.2}
\]

Thus the target is \(\mathcal B_{\rm low}^+\ll R X^\varepsilon\), not
\(X^\varepsilon\); the external \(R\) occurs exactly once.

The exact character pair is

\[
 \mathcal B_{\rm low}^+=\mathcal E_{\rm amp}+\mathcal K_X,
 \tag{1.3}
\]

where

\[
 \mathcal E_{\rm amp}
 =\sum_{d\equiv1(4)}\sum_{h\geq1}
 {b_X(h,d)-b_X(h,d+2)\over h}e(hX/d),
 \tag{1.4}
\]

\[
 \mathcal K_X
 =\sum_{d\equiv1(4)}\sum_{h\geq1}
 {b_X(h,d+2)\over h}e(hX/d)
 \{1-e(-h\Delta_d)\},
 \qquad \Delta_d={2X\over d(d+2)},
 \tag{1.5}
\]

and

\[
 \boxed{\mathcal E_{\rm amp}\ll_{s_0}(1+\log X)^2.}
 \tag{1.6}
\]

For the flattened coefficient

\[
 b_{\rm flat}(h,d)={\bf1}_{d\leq y}
 V_{\rm low}(4R^2h^2/d^2),
 \tag{1.7}
\]

the analogous seam is \(O_{s_0}(\log(2X))\).

There is, however, no estimate of the signed kernel (1.5).  In fact (1.3)
and (1.6) show that a target bound for (1.5) is equivalent, up to a
polylogarithm, to the original lower antecedent.  Local pairing is therefore
an exact return, not a gain.  Its obstruction is especially transparent in
the exact consecutive-odd phase increment

\[
 g_h(d+2)-g_h(d)={1\over2}-h\Delta_d,
 \qquad g_h(d)={hX\over d}+{d-1\over4}.
 \tag{1.8}
\]

Integer values of \(h\Delta_d\) make the two-point bracket small, whereas
half-integer values make the outer odd-denominator phase resonant and the
bracket maximal.  At the critical singleton height \(h=1\),
\(d\asymp X^{1/3}\), the discrete curvature is order one and there are
\(\asymp X^{1/3}\) distinct aliases.  The coefficient-uniform conductor
capacity is therefore \(X^{1/3}\), missing the \(R=X^{1/4}\) target by
\(X^{1/12}\).  This is the accepted one-variable conductor barrier in the
new coordinates, not a new saving.

One strict package can be removed.  If

\[
 \mathfrak I_R=\{(h,d):d\equiv1\ (4),\ \|h\Delta_d\|\leq R^{-1}\},
\]

then its contribution to (1.5) is

\[
 \mathcal K_X[\mathfrak I_R]\ll_{s_0}R\log(2X)
 \ll_{\varepsilon,s_0}R X^\varepsilon.
 \tag{1.9}
\]

Consequently the smallest exact survivor obtained here is

\[
 \boxed{
 \mathcal K_X^{\rm surv}=
 \sum_{d\equiv1(4)}\sum_{\substack{h\geq1\\
             \|h\Delta_d\|>R^{-1}}}
 {b_X(h,d+2)\over h}e(hX/d)\{1-e(-h\Delta_d)\}.}
 \tag{1.10}
\]

The target for (1.10) remains open.  The result is therefore a rigorous
reduction and scoped no-go, not a proof of the lower owner.

## 2. Exact statement and hypotheses

The preceding conclusions use the following exact hypotheses, all inherited
from the selected context except for making the inactive-bottom constant
explicit.

1. \(X\) is sufficiently large and real.  The active dyadic profiles are
   the accepted nonnegative telescoping partition.  Each active profile has
   fixed shell support
   \(1/2\leq d/D_j\leq3/2\), bounded overlap,
   \(\|w_j\|_\infty+\sum_d|w_j(d+1)-w_j(d)|\leq4\), and exactly one hard
   top sample at \(d=y\).  The inactive bottom is supported in
   \(d\leq C_{\rm bot}R\) for the fixed constant supplied by that partition.

2. The fixed radial cutoff is real and smooth, equals one on
   \([0,s_0]\), and vanishes on \([2s_0,\infty)\).  Choose it so that

   \[
   {3\sqrt{2s_0}\over4}<\frac12,
   \qquad \sqrt{2/s_0}>C_{\rm bot}.
   \tag{2.1}
   \]

   The candidate choice \(s_0\leq1/100\) is sufficient only after the
   exact accepted value of \(C_{\rm bot}\) is cited.  Alternatively (2.1)
   is the invariant formulation.

3. The accepted Vaaler coefficient satisfies
   \(\Phi(u)=1+O(u^2)\) on \(0\leq u\leq1/2\), is bounded there, and the
   exact endpoint \(h=H_j\) is retained.  No height is rounded or replaced.

4. The accepted frequency-first divisor theorem is used only in its exact
   range: a height weight with sampled sup plus variation \(O(1/L)\), an
   actual smooth profile or the one hard truncation, real \(X\), and
   \(1\leq L\leq D\leq Y\), giving
   \(O_\varepsilon(X^\varepsilon(1+D/L))\).

5. Every sum is finite before reordering.  The hard cotangent transform
   boundary, stationary half-stars, outer product half tie, and conjugate
   negative frequency stay at their accepted owners.  The inactive bottom
   is not reintroduced into (1.1).

Under these hypotheses one additionally has the corrected target-scale
flattening statement

\[
 \boxed{
 \mathcal B_{\rm low}^+=\mathcal B_{\rm flat}^+
 +O_{\varepsilon,s_0}(R X^\varepsilon),}
 \tag{2.2}
\]

where

\[
 \mathcal B_{\rm flat}^+
 =\sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
 \tag{2.3}
\]

Equation (2.2) covers the entire fixed lower cutoff, including the region
above the \(n\asymp X^{2/5}\) small-angle replacement threshold.  It is not
a bound for (2.3).

## 3. Proof and derivation

### 3.1 Finite profile-first one-count and external normalization

The original \((j,h,d)\)-sum is finite: only finitely many \(H_j\) are
nonzero, every \(h\) satisfies \(h\leq H_j\), and every \(w_j\) has finite
physical support.  Since the lower multiplier is independent of \(j\),
finite reordering gives (1.1) exactly.  The height floor is inside \(a_j\),
the hard sample is inside the unique top \(w_j\), and zero extension is
performed only after this one-count coefficient is formed.

The accepted coefficientwise positive-frequency transform gives (1.2).
Its negative-frequency mate is the real-coefficient conjugate.  Hence a
complex modulus bound for \(\mathcal B_{\rm low}^+\) controls both signs,
and neither a second \(R\) nor a second endpoint owner is inserted.

### 3.2 Corrected proof of target-scale profile flattening

If a summand with profile \(j\) is nonzero, radial support and profile
support give

\[
 {hR\over d}\leq{\sqrt{2s_0}\over2},\qquad
 {1\over2}\leq{d\over D_j}\leq{3\over2}.
\]

Consequently

\[
 {hR\over D_j}\leq{3\sqrt{2s_0}\over4}<\frac12.
 \tag{3.1}
\]

Thus \(D_j/R>2h\), so \(h\leq H_j\) with the exact floor, and

\[
 {h\over H_j+1}<{hR\over D_j}<\frac12.
 \tag{3.2}
\]

Also \(h\geq1\) and radial support imply

\[
 d\geq\sqrt{2/s_0}\,R>C_{\rm bot}R.
 \tag{3.3}
\]

The inactive bottom is therefore absent.  The exact active partition gives
\(\sum_jw_j(d)={\bf1}_{d\leq y}\) on every surviving atom, including the
hard top value.  Replacing \(\Phi\) by one consequently produces (2.3)
with no boundary remainder.  It remains only to price \(\Phi-1\).

Take a smooth dyadic height partition \(h\asymp L\).  On one such shell,

\[
 \left\|{\Phi(h/(H_j+1))-1\over h}\right\|_\infty
 +\operatorname{Var}_h
 \left({\Phi(h/(H_j+1))-1\over h}\right)
 \ll {1\over L}\left({L\over H_j}\right)^2.
 \tag{3.4}
\]

Here and below the shell cutoff is included in the variation.  To justify
the coupled radial multiplier without an unsupported separation claim, put
\(x=h/L\), \(z=d/D_j\), and \(\sigma=RL/D_j\).  After multiplying by fixed
extensions on \(x\asymp1\), \(1/2\leq z\leq3/2\), the family

\[
 Q_\sigma(x,z)=V_{\rm low}(4\sigma^2x^2/z^2)
\]

has uniformly bounded \(C^M\) norms for any fixed sufficiently large
\(M\), uniformly over the allowed \(\sigma\).  A two-dimensional Fourier
series therefore has coefficients \(c_{m,n}(\sigma)\) satisfying, for
example,

\[
 \sum_{m,n}|c_{m,n}(\sigma)|(1+|m|)\ll_{M,s_0}1.
 \tag{3.5}
\]

This is the needed statement; two-dimensional \(C^1\) regularity alone
would not imply the asserted absolute summability.  The \(m\)-factor in
(3.5) prices the height variation, while the denominator Fourier factor is
bounded and preserves the one hard endpoint.  Applying the accepted
frequency-first theorem termwise gives

\[
 E_{j,L}\ll_{\varepsilon,s_0}X^\varepsilon
 \left({L\over H_j}\right)^2\left(1+{D_j\over L}\right).
 \tag{3.6}
\]

On every surviving profile \(H_j\geq1\), and
\(D_j/R<H_j+1\leq2H_j\).  Hence

\[
 \sum_{L\ {
m dyadic}}E_{j,L}
 \ll X^\varepsilon\left{
 \sum_L(L/H_j)^2+{D_j\over H_j^2}\sum_LL\right}
 \ll R X^\varepsilon.
 \tag{3.7}
\]

There are \(O(\log X)\) active profiles, absorbed by \(X^\varepsilon\).
This proves (2.2).  It also proves that all height floors and the inactive
bottom disappear from the flat main term for a geometric reason, not by an
unlicensed telescope.

### 3.3 Exact mod-four pair and the full-profile amplitude seam

Define

\[
 F_X(d)=\sum_{h\geq1}{b_X(h,d)\over h}e(hX/d)
\]

and extend it by zero outside the literal support.  Every positive odd
integer is exactly one member of a pair \((4m+1,4m+3)\), including a pair
whose other member has zero amplitude at a top or bottom edge.  Therefore

\[
 \mathcal B_{\rm low}^+=\sum_{d\equiv1(4)}\{F_X(d)-F_X(d+2)\}.
 \tag{3.8}
\]

Since

\[
 e(hX/(d+2))=e(hX/d)e(-h\Delta_d),
\]

adding and subtracting the \(d+2\) amplitude at the \(d\)-phase proves
(1.3)--(1.5).

It remains to prove (1.6).  For fixed \((j,h)\), set

\[
 c_{j,h}(d)=w_j(d)V_{\rm low}(4R^2h^2/d^2)
\]

with zero extension.  The argument of \(V_{\rm low}\) is monotone in
positive \(d\), so the fixed smooth multiplier has \(O_{s_0}(1)\) total
variation.  The product variation inequality and the accepted profile BV
give

\[
 \sum_{d\equiv1(4)}|c_{j,h}(d)-c_{j,h}(d+2)|\ll_{s_0}1.
 \tag{3.9}
\]

The hard top jump, the last active/bottom edge, and zero partners are part
of (3.9); none is discarded.  If \(a_j(h)\ne0\), then
\(h\leq H_j\leq D_j/R\), hence \(D_j\geq Rh\).  Thus the number of possible
profiles at fixed \(h\) is

\[
 \#\{j:a_j(h)\ne0\}\ll1+\log^+(R/h),
 \qquad 1\leq h\leq H_0\leq R.
 \tag{3.10}
\]

Using boundedness of \(\Phi\), (3.9), and (3.10),

\[
 |\mathcal E_{\rm amp}|
 \ll_{s_0}\sum_{h\leq R}{1+\log^+(R/h)\over h}
 \ll_{s_0}(1+\log X)^2.
\]

For (1.7) there is only one cutoff sequence in \(d\), so the same proof
has no profile count and gives \(O(\log X)\).

### 3.4 Integer-pair deletion and the complementary half-integer resonance

The elementary inequality

\[
 |1-e(-t)|\leq2\pi\|t\|
\]

and bounded overlap of the exact profiles give

\[
 |\mathcal K_X[\mathfrak I_R]|
 \ll R^{-1}\sum_{d\ll Y}\sum_{h\leq R}{1\over h}
 \ll R^{-1}Y\log(2R),
\]

which is (1.9).  The complementary kernel (1.10) remains signed.

Now write an odd denominator as \(d=2r+1\).  Since
\(\chi_4(2r+1)=(-1)^r=e(r/2)\), its combined phase is

\[
 \varphi_h(r)={hX\over2r+1}+{r\over2}.
\]

The exact first difference is (1.8), while on a dyadic denominator block
\(d\asymp D\),

\[
 \varphi_h''(r)\asymp\lambda_{h,D}:={hX\over D^3}.
 \tag{3.11}
\]

The first difference sweeps

\[
 N_{\rm alias}(h,D)\asymp1+{hX\over D^2}
 \tag{3.12}
\]

integer aliases.  A natural stationary cell has width
\(\lambda_{h,D}^{-1/2}\).  Resonant cells plus the complementary
first-difference intervals therefore have the familiar coefficient-blind
capacity

\[
 \boxed{
 C(h,D)={1\over h}\min\left\{D,
 \sqrt{hX/D}+{D^{3/2}\over\sqrt{hX}}\right\}.}
 \tag{3.13}
\]

This is also the direct second-derivative estimate after Abel summation
with the actual block BV.  It is a method capacity, not a lower bound for
the signed sum.

At \(h=1\), \(D=X^{1/3}\), one has \(\lambda_{1,D}\asymp1\),
\(N_{\rm alias}\asymp D\), and

\[
 C(1,X^{1/3})\asymp X^{1/3}.
 \tag{3.14}
\]

The pair factor is largest, not smallest, at the corresponding
half-integer aliases.  Since the \(h=1\) row has no internal height
cancellation, a frequency-by-frequency height-first norm leaves precisely
this reciprocal character sum.  A target proof must therefore use a new
joint signed inequality, potentially cancellation between distinct
heights, rather than local pair smallness or a rowwise height bound.

There is also a literal post-pair absolute obstruction.  Take a fixed small
interval of \(d/Y\) around \(u_*=\sqrt{4/5}\).  Then uniformly on a smaller
such interval

\[
 \Delta_d={2X\over d(d+2)}={2\over(d/Y)^2}+o(1)
\]

is close to \(5/2\), so \(|1-e(-\Delta_d)|\gg1\).  On this top-scale
interval, \(A_X(1,d+2)=1+o(1)\), the lower multiplier equals one, and there
are \(\asymp Y\) admissible \(d\equiv1\pmod4\).  Therefore

\[
 \sum_{d\equiv1(4)}|b_X(1,d+2)\{1-e(-\Delta_d)\}|\gg Y=R^2.
 \tag{3.15}
\]

This rigorously falsifies every post-pair termwise-absolute proof at the
\(R\) target.  It is not a signed lower bound.

The capacity ledger is:

| package | coefficient-blind capacity | required budget | outcome |
|---|---:|---:|---|
| full paired kernel, direct \(\ell^1\) | \(O(Y\log X)\), with actual \(h=1\) mass \(\gg Y\) | \(R X^\varepsilon\) | fails by at least \(R\) |
| integer-pair cells \(\|h\Delta_d\|\leq R^{-1}\) | \(O(R\log X)\) | \(R X^\varepsilon\) | target-safe |
| \(h=1,d\asymp R\), trivial | \(R\) | \(R X^\varepsilon\) | target-safe endpoint |
| \(h=1,d\asymp X^{1/3}\), alias/conductor | \(X^{1/3}\) | \(X^{1/4+\varepsilon}\) | misses by \(X^{1/12}\) |
| \(h=1,d\asymp Y\), stationary width | \(R\) | \(R X^\varepsilon\) | target-safe endpoint |
| complete surviving joint kernel (1.10) | no accepted signed bound | \(R X^\varepsilon\) | open |

### 3.5 Integerization and the corrected finite Fourier return

The conductor candidate's integerization is valid.  Put \(N=\lfloor X\rfloor\)
and change only the phase in (2.3).  Since

\[
 |e(hX/d)-e(hN/d)|\ll h/d
\]

and radial support permits \(O_{s_0}(d/R)\) heights for fixed \(d\),

\[
 |\mathcal B_{\rm flat}^+(X)-\mathcal B_{\rm flat}^{(N)}(X)|
 \ll\sum_{d\leq y}{1\over d}{d\over R}\ll {Y\over R}=R.
 \tag{3.16}
\]

For the exact discrete Fourier identity, the auxiliary function should be
specified rather than asserted.  Choose a smooth periodic \(\eta_y\) on the
positive arc which is zero for \(0\leq t\leq(2y)^{-1}\), equals one for
\(t\geq y^{-1}\) as long as the radial multiplier can be nonzero, and is
supported before the opposite side of the circle.  Set

\[
 J_{R,y}(t)=\eta_y(t){V_{\rm low}(4R^2t^2)\over t}
\]

on that arc and zero elsewhere.  Every nonzero physical sample has
\(1/y\leq h/d<1\), so this agrees with the desired value at every sample.
For fixed \(X\), \(J_{R,y}\) is smooth.  With

\[
 \widehat J_{R,y}(k)=\int_0^1J_{R,y}(t)e(-kt)\,dt,
\]

Fourier inversion and root-of-unity orthogonality give

\[
 {1\over d}\sum_{h\bmod d}J_{R,y}(h/d)e(Nh/d)
 =\sum_{k:\ d\mid N+k}\widehat J_{R,y}(k).
 \tag{3.17}
\]

There is no missing factor of \(d\): at a physical sample,
\(J(h/d)/d=V_{\rm low}(4R^2h^2/d^2)/h\).  Define, for every integer \(m\),

\[
 A_y(m)=\sum_{\substack{1\leq d\leq y\\d\mid m}}\chi_4(d),
 \tag{3.18}
\]

where positive divisors are used for negative \(m\), and every positive
\(d\leq y\) divides \(m=0\).  Then

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}\widehat J_{R,y}(k)A_y(N+k).}
 \tag{3.19}
\]

Let \(c_y=\sum_{d\leq y}\chi_4(d)/d\).  Since Fourier inversion at zero
gives \(\sum_k\widehat J_{R,y}(k)=J_{R,y}(0)=0\),

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_k\widehat J_{R,y}(k)\{A_y(N+k)-c_y\}.
 \tag{3.20}
\]

Define the two-sided discrepancy by \(D_N(0)=0\) and

\[
 D_N(k)-D_N(k-1)=A_y(N+k)-c_y
\]

for all \(k\in\mathbb Z\), with the recurrence read backwards for negative
\(k\).  Since \(\widehat J\) is Schwartz for fixed \(X\) and \(D_N(k)\) has
at most polynomial growth, summation by parts has no boundary term and gives

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_kD_N(k)\{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\}.}
 \tag{3.21}
\]

Equations (3.19)--(3.21) are exact.  They provide no uniform Fourier norm:
the artificial transition below \(1/y\) has \(y\)-dependent derivatives.
Different lawful choices of \(\eta_y\) give different but exactly
equivalent Fourier representatives.  Thus (3.21) is an exact return to the
truncated character-divisor discrepancy, but it should not be called a
canonically smallest normed survivor until those cutoff-dependent norms are
priced.

## 4. First doubtful or unproved step

The first unproved analytic step is

\[
 \mathcal K_X^{\rm surv}\ll_{\varepsilon,s_0}R X^\varepsilon,
 \tag{4.1}
\]

equivalently, after (2.2), (3.16), and (3.19)--(3.21), a target bound for
the actual truncated character-divisor discrepancy against the full
lower-radial wavelet.  No estimate in this report reaches (4.1).

The exact obstruction is not an omitted boundary: integer pair cells are
already target-safe, the full amplitude seam is polylogarithmic, and real
\(X\) can be integerized for \(O(R)\).  The first missing inequality must
couple denominator aliases and heights while preserving the actual
\(\chi_4\) sign.  Rowwise height cancellation cannot see \(h=1\), and
aliaswise or termwise absolute values encounter (3.14)--(3.15).

For the conductor candidate specifically, (2.2) is proved only after these
two textual corrections are made explicit in its statement: replace the
unsupported numerical bottom claim by (2.1), and replace “absolutely
summable \(C^1\) coefficient norm” by the uniform high-regularity Fourier
estimate (3.5).  The finite Fourier identities are exact, but any later
analytic use must price the \(y\)-dependent cutoff norms.

## 5. Control tests and outcomes

### Required campaign controls

| control | outcome | reason |
|---|---|---|
| `literal_lower_reciprocal_antecedent` | pass | (1.1) is the exact positive antecedent before any norm. |
| `external_R_normalization` | pass | (1.2) retains exactly one external \(R\); the hard transform error is separate. |
| `global_profile_height_kernel` | pass | \(A_X(h,d)\) is formed by finite reordering with exact \(H_j\), then flattened only at target-sized proved cost. |
| `mod_four_pairing_identity` | pass | (3.8) uses zero extension and pairs every positive odd denominator exactly once. |
| `amplitude_seam_BV` | pass | Full profile: \(O(\log^2X)\); flat cone: \(O(\log X)\); hard and bottom edges are included. |
| `phase_increment_joint_height_kernel` | pass as an exact reduction; estimate open | (1.5) remains signed until the explicitly target-safe deletion (1.9). |
| `resonant_nonresonant_capacity` | pass/no-go | (1.8), (3.11)--(3.14), and the capacity table price integer and half-integer cells. |
| `floor_star_hard_bottom_boundaries` | pass after bottom-constant correction | Floors disappear from the flat main term by (3.1)--(3.3), not by rounding. Stars and the hard sample stay at their owners. |
| `old_return_map_nonduplication` | pass/no-gain | The Fourier discrepancy is identified as a return; no transform identity is credited as an estimate. |
| `unsigned_adversarial_control` | pass (falsifies unsigned route) | The actual \(h=1\) absolute mass (3.15) is \(\gg Y\); arbitrary phase alignment is at least as bad. |
| `full_lower_range_scope` | pass for the reduction; bound open | (2.2) is valid on the fixed full lower cutoff, including above \(X^{2/5}\).  The critical test slice alone is not a full proof. |
| `one_count_downstream_scope` | pass | No GAR, blockwise M1, M2, endpoint, M9, or exponent conclusion is inferred. |

### Mandatory Round-57 comparison

The present pair is not literally the Round-57 pair.

| seam | Round 57 | Round 121 |
|---|---|---|
| location | after stationary transform | before transform, in the physical reciprocal antecedent |
| variables and phase | two-point product row \((h,q),(h,q+2)\), phase \(e(\sqrt{Xhq})\) | full-profile physical denominators \((d,d+2)\), phase \(e(hX/d)\) |
| pair availability | only some moving product windows have two points; \(\gg R\) actual rows are unmatched | every odd denominator belongs to a zero-extended pair; boundary zero partners are retained in the amplitude seam |
| proved amplitude fact | smooth row difference is small, but profile/star seams and unmatched rows survive | complete profile-first amplitude seam is \(O(\log^2X)\), and after flattening \(O(\log X)\) |
| analytic survivor | unmatched signed hyperbola rows plus unsaved phase increment | complete signed height/denominator increment (1.10), or exactly the discrepancy (3.21) |

Thus profile-first aggregation genuinely repairs the amplitude bookkeeping
that was unavailable in Round 57.  It does not evade the Round-57 analytic
no-go: in both cases \(\chi_4(q+2)=-\chi_4(q)\) creates a difference but the
phase factor has no automatic mod-one smallness.  Any claimed gain obtained
by taking the two-point bracket in absolute value would be the same forbidden
local-pairing argument, and (3.15) explicitly falsifies it here.

### Comparison with the other accepted returns

- The Round-63 Appell and one-sided Poisson maps apply to the subcritical
  one-sided cone and return to a reciprocal phase.  Equations (2.3) and
  (1.5) start at that reciprocal side and cover the larger fixed lower
  cutoff; no Appell transformation is used as an inequality.
- Round 64 inverse product-wavelet Poisson reconstructs the reciprocal cone.
  Equations (3.19)--(3.21) are its sharp full-lower analogue and are openly
  labelled an exact return.
- Round 65 period-four crossing pairing leaves a signed symmetric
  difference.  The discrepancy \(D_N\) in (3.21) retains exactly that type
  of unmatched arithmetic information; it is not canceled by flattening.
- Round 66 shows that one-variable modes do not recover the missing factor.
  The alias saturation (3.14) gives the same warning before applying a
  Fourier norm.
- The conductor capacity (3.13) is the accepted one-variable
  second-derivative/conductor mechanism.  At the critical singleton it
  reproduces the \(X^{1/12}\) deficit rather than proving a new saving.
- Completing the coefficient to \(r_2/4\) is still forbidden by Round 14;
  \(A_y\) is a truncated character-divisor coefficient, not \(r_2/4\).

### Line audit of the conductor candidate

| candidate item | verdict | correction or proof note |
|---|---|---|
| (C3), automatic heights | pass | (3.1)--(3.2) prove \(h\leq H_j\) with the exact floor. |
| (C3), inactive bottom | revise statement | cite the exact \(C_{\rm bot}\), or choose \(s_0\) by (2.1); “\(d>4R/3\)” alone is not the accepted bottom-support statement in the supplied context. |
| (C3), two-variable separation | pass after repair | use the uniform \(C^M\) Fourier estimate (3.5); bare two-dimensional \(C^1\) does not imply absolute coefficient summability.  Then (C10) is valid. |
| displayed line after (C10) | typographical correction | replace `\left{left(` by `\left(`. |
| (C13) | pass | (3.16) proves \(O(Y/R)=O(R)\) while changing the phase only. |
| (C17) | pass after definitions | specify \(J\) as above and define divisibility for negative and zero arguments; the \(1/d\) normalization is correct. |
| (C18) | pass | use Fourier inversion at zero; subtraction of \(c_y\) is exact because \(J(0)=0\). |
| (C19)--(C20) | pass after boundary note | define the negative side of \(D_N\); fixed-\(X\) Schwartz decay removes the boundary term. |
| “smallest discrepancy survivor” | revise scope | it is an exact, cutoff-dependent return.  No uniform Fourier norm or canonical minimality follows until the artificial \(1/y\)-scale cutoff is priced. |

No numerical test was used.  The controls are analytical and algebraic.

## 6. Dependencies and exact artifacts used

This report used only the selected campaign context plus the conductor's
mandatory Round-57 and candidate follow-ups:

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`
- `rounds/codex-managed/m9-m1-lower-radial-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md`
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/synthesis.md`
- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/synthesis.md`
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/synthesis.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/derivation_packet.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md`

The precise accepted graph inputs used were the exact global angular
recombination, Vaaler \(\Phi\) regularity, actual dyadic profile
nondegeneracy/BV, typed height variation, terminal frequency-first divisor
bound, terminal-height nonlower completion, global radial one-count
assembly, and GAR-to-total-active-M1 scope.  No new external source and no
unlisted analytic theorem was imported.

## 7. Recommended state effect

**Recommend promote**, after the conductor checks the exact inactive-bottom
constant and incorporates the stated corrections, the following narrowly
scoped facts:

1. the full-lower target-scale profile-flattening lemma (2.2), for a fixed
   \(s_0\) satisfying (2.1);
2. the exact full-profile mod-four split (1.3)--(1.5) and amplitude bound
   (1.6), with the flat \(O(\log X)\) refinement;
3. the target-safe integer-pair deletion (1.9) and real-\(X\)
   integerization (3.16);
4. the exact finite Fourier/discrepancy identities (3.19)--(3.21), with an
   explicit warning that their cutoff norms are unpriced;
5. the scoped obstruction that local denominator pairing is
   capacity-preserving: half-integer aliases retain the accepted conductor
   deficit and post-pair absolute values have actual mass \(\gg Y\).

**Retain open** `M9-M1-global-lower-radial-signed-estimate`.  Its smallest
exact survivor from this report is (1.10), equivalently the flattened and
integerized discrepancy functional (3.21) up to target-safe errors.  A new
joint signed inequality is still required.

No result here proves `M9-M1-global-angular-radial-estimate` (GAR), either
direct blockwise M9-M1 parent, blockwise `M9-M1`, any part of `M9-M2`,
endpoint uniformity, `M9`, or the Gauss-circle quarter theorem.  Even a
future proof of the survivor would give GAR only through the already proved
radial one-count assembly; it would remain an alternative total-M1 theorem
with no inverse implication to blockwise M9-M1.  The accepted internal
\(1/3\) exponent and the audited external
\(0.3144831759740614\ldots\) benchmark are unchanged.
