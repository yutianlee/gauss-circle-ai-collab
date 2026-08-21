# Uniform fixed-q sampled-k attack and short-shell consequence

Campaign: `m9-m2-fixed-q-sampled-k-short-shell`
Round: 104
Task: `fixed_q_sampled_k_attack`
Role: analytic discovery
Starting graph SHA-256: `d2502a33224fbcb1fe3b8ffe0ea1227b953112fa0c98216597e8b0ccfa887372`

## 1. Result

**Uniform literal fixed-q theorem.**  The proposed general-q
extension is valid for the complete actual centered coefficient.  On every
active residual block, uniformly for

\[
 b=a+2q,\qquad a\asymp b\asymp A,\qquad q\asymp D,
\]

and every actual odd lift \(g\asymp G\asymp L/A\), the zero-extended
centered \(k\)-coefficient satisfies

\[
 \boxed{
 \sup_k |B_{a,q,g}(k)|+
 \operatorname {Var}_{k\in\mathbb Z} B_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon
 \sqrt{\frac{AL}{JD}}.}                              \tag{104.1}
\]

Here \(B_{a,q,g}\) contains the literal actual profiles, floors, stars,
fixed physical collars, finite-support endpoint convention, signs,
orientation, and every remaining bounded-variation \(k\)-profile.  Only
the centered carrier and the complete punctured metric member are kept
outside it, because those two factors are subsequently coupled exactly by
Fourier expansion.  No arbitrary \(k\)-coefficient is allowed in
(104.1).

For one metric mode put \(n=|2\nu-g|\) (or
\(n=|2\nu+g|\) in the conjugate orientation).  Then

\[
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 B_{a,q,g}(k)
 e\!\left(\left(\nu-\frac g2\right)\frac{\Lambda_q}{k}\right)
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{\frac LA}\,n^{-1/2}\right).       \tag{104.2}
\]

Every \(g\) is odd, hence \(n\ge1\).  This includes the metric
density mode \(\nu=0\), for which \(n=g\); the density is estimated,
not deleted.  Summing every density and discrepancy mode and then every
literal odd lift gives the uniform row estimate

\[
 \boxed{|F_a(q)|\ll_\varepsilon X^\varepsilon\frac{L^2}{A}.} \tag{104.3}
\]

Consequently

\[
 \boxed{
 \sum_{a\asymp A}\sum_{q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon\frac{DL^4}{A}.}       \tag{104.4}
\]

The exact zero-extended Cauchy bridge gives only

\[
 \boxed{
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon
 \frac{H^2DL^4}{A},\qquad 1\le H\le D.}           \tag{104.5}
\]

The required Gram target is

\[
 X^\varepsilon\frac{H^2E_0}{\rho}
 \asymp X^\varepsilon\frac{H^2L^4}{AD}.
\]

Thus (104.5) has an **exact factor \(D^2\) route deficit**.  It proves the
target for \(D\) bounded by any fixed power of \(\log X\) (and, with
the usual prescribed-family interpretation, for \(D=X^{o(1)}\)) after
renaming \(\varepsilon\).  It supplies no range \(D\le X^\theta\)
with fixed \(\theta>0\).  This is a failure of the rowwise
Cauchy-to-Gram route, not a counterexample to the literal actual Gram.

## 2. Exact statement and hypotheses

Let \(J=\sqrt X\), \(1\le L\le J^{1/2}\), and work on one literal
residual half-open dyadic block.  The variables obey

\[
 a,b\ {\rm odd},\qquad b=a+2q,\qquad
 a<b<4a,\qquad (a,b)=1,\qquad
 a\asymp b\asymp A,\qquad q\asymp D,
\]

\[
 K\asymp\frac{JD}{A},\qquad
 G\asymp\frac LA,\qquad
 \rho=\frac{AJD^3}{L^3}>1.                           \tag{104.6}
\]

All assertions are uniform in real \(X\), in the actual top profile,
and in every active block.  A nonempty odd lift fibre has \(G\gg1\), so
\(A\ll L\); combined with \(L^2\le J\), this will give the collar
resolution inequality below.  If a lift fibre is empty, its contribution is
defined to be zero.

Put

\[
 \delta_q=\sqrt b-\sqrt a
 =\frac{2q}{\sqrt b+\sqrt a},\qquad
 \Lambda_q=\frac{X\delta_q^2}{2},                    \tag{104.7}
\]

and retain the literal open reciprocal interval

\[
 I_{a,q}=\left(
 \frac{J\delta_q}{2\sqrt a},
 \frac{J\delta_q}{\sqrt b}\right).                  \tag{104.8}
\]

Every \(k\in I_{a,q}\) has \(k\asymp K\).  No lower bound on the
length of \(I_{a,q}\) is assumed.  Indeed

\[
 \frac{\sup I_{a,q}}{\inf I_{a,q}}
 =\frac{2\sqrt a}{\sqrt b}\downarrow1
 \quad\hbox{as } b/a\uparrow4,                       \tag{104.9}
\]

so the interval can collapse at the cone edge.  The proof uses only its
location \(k\asymp K\), the upper bound \(|I_{a,q}|\ll K\), and the
monotone saddle map

\[
 r_k=\frac{J\delta_q}{2k}:
 I_{a,q}\longrightarrow
 \left(\frac{\sqrt b}{2},\sqrt a\right).             \tag{104.10}
\]

Thus cone-edge collapse shortens both the \(k\)-interval and the physical
saddle path and cannot worsen any estimate.  If the two fixed physical
collars overlap, the collarized main profile is empty or is one bounded
transition piece; if \(I_{a,q}\cap\mathbb Z\) is empty or a singleton,
the zero or one-term estimate is used directly.

The complete physical and centered integrals are

\[
 \mathfrak C^\circ_{a,q,k}(g)
 =g\int_{b/4}^{a} A^\circ_{ga,gb}(gu)
 e\!\left(g[ku-J\delta_q\sqrt u]\right)\,du,          \tag{104.11}
\]

\[
 \mathfrak B^\circ_{a,q,k}(g)
 =g\int_{b/4}^{a} A^\circ_{ga,gb}(gu)
 e\!\left(gk\left(\sqrt u-
       \frac{J\delta_q}{2k}\right)^2\right)\,du.     \tag{104.12}
\]

Completing the square gives the exact carrier identity

\[
 \mathfrak C^\circ_{a,q,k}(g)
 =e\!\left(-\frac{g\Lambda_q}{2k}\right)
  \mathfrak B^\circ_{a,q,k}(g).                      \tag{104.13}
\]

With \(u=y^2\), define the literal \(k\)-independent physical
amplitude

\[
 Q_{a,q,g}(y)=2gy\,A^\circ_{ga,gb}(gy^2),\qquad
 \mathfrak B^\circ_{a,q,k}(g)
 =\int_{\sqrt b/2}^{\sqrt a}
 Q_{a,q,g}(y)e\!\left(gk(y-r_k)^2\right)dy.           \tag{104.14}
\]

The accepted actual homogeneity
\(A_{ga,gb}(gu)=g^{-3}E_{a,b}(g)P_{a,b}(u)\), the actual smooth
profiles, and the fixed physical collars give the uniform complete-Fresnel
amplitude ledger

\[
 \|Q_{a,q,g}\|_{\rm CF}
 \ll_\varepsilon X^\varepsilon g\sqrt A.             \tag{104.15}
\]

The norm in (104.15) includes supremum, total physical variation, the
normalized derivatives of each actual profile member, and the two collar
pieces.  The narrowest physical collar has

\[
 w_g\asymp\frac1{g\sqrt A},\qquad
 gK w_g^2\asymp\frac{K}{gA}
 \asymp\frac{JD}{AL}\gg1.                            \tag{104.16}
\]

For a nonempty fibre, \(A\ll L\) and \(L^2\le J\), so the last
quantity is \(\gg D\ge1\).  This is uniform as \(b/a\to4\).

Let \(B_{a,q,g}(k)\) denote (104.14) multiplied by every remaining
literal smooth dyadic \(k\)-profile, with zero extension outside the open
interval (104.8).  The primitive mask, square-ray owner, residual
\(\rho\)-safe owner, finite odd-lift support, half-open base and
\(q\)-blocks, exact-center puncture, original Poisson-mode owners, and
all previously discharged boundary owners are retained.  These masks are
fixed once \((a,q)\) and the block are fixed; none inserts a rapidly
varying \(k\)-sequence.  The complete punctured metric member is

\[
 W_R(t)=\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)e(\nu t),\qquad
 |\widehat W_R(\nu)|\ll_N
 R^{-1}(1+|\nu|/R)^{-N},\qquad 1\le R\le G.       \tag{104.17}
\]

For one orientation the exact mode-resolved row is therefore of the form

\[
 F_{a,R}^{-}(q)=\mathbf1_{\rm owners}
 \sum_{\substack{g\ {\rm odd}\\g\in\mathcal G_{a,b}}}
 \sum_{\nu\in\mathbb Z}\widehat W_R(\nu)
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 B_{a,q,g}^{-}(k)
 e\!\left(\left(\nu-\frac g2\right)
               \frac{\Lambda_q}{k}\right).          \tag{104.18}
\]

The conjugate orientation has \(\nu+g/2\), and all actual signs and
finite orientation multiplicities remain in \(B^\pm\).  Formula
(104.18) is not a density-discrepancy separation: every \(\nu\),
including \(0\), is present in the same exact Fourier series.

## 3. Proof or derivation

First prove the new sampled-\(k\) statement.  Extend \(k\) continuously
inside (104.8) and write \(c=J\delta_q/2\), \(r_k=c/k\).  The phase
in (104.14) has the exact differential identity

\[
 k\,\partial_k e\!\left(gk(y-r_k)^2\right)
 =\frac{y+r_k}{2}\,
   \partial_y e\!\left(gk(y-r_k)^2\right).           \tag{104.19}
\]

This is the \(k\)-analogue of retaining the complete centered integral:
the potentially large motion of the saddle becomes one physical derivative
of the actual amplitude, with no uncancelled carrier derivative.

For clarity, localize \(Q_{a,q,g}\) into its finitely or
logarithmically many actual physical profile pieces.  Give a piece physical
width \(w\) and normalized amplitude size \(Q_w\).  The actual
profile ledger (104.15) says
\(\sum_wQ_w\ll_\varepsilon X^\varepsilon g\sqrt A\), while every
piece has \(gKw^2\gg1\); (104.16) is the worst, collar-scale case.
In the exact coordinate

\[
 z=\sqrt{gk}(y-r_k),                                 \tag{104.20}
\]

the complete integral over such a piece has supremum
\(\ll Q_w/\sqrt{gK}\).  When the saddle meets the piece, (104.19),
integration by parts in \(y\), and the rescaling (104.20) give

\[
 \int_{k\asymp K}|\partial_k B_w(k)|\,dk
 \ll \frac{Q_w}{\sqrt{gK}}.                          \tag{104.21}
\]

One can see the cancellation of all scale factors directly.  The saddle
crosses a width-\(w\) piece during a \(k\)-interval of length
\(\ll Kw/\sqrt A+1\), since
\(|r_k'|\asymp\sqrt A/K\).  The differentiated amplitude in
(104.19) costs at most \(\sqrt A/w\), while division by the outer
\(k\asymp K\) and the complete Fresnel factor
\((gK)^{-1/2}\) return \(Q_w/\sqrt{gK}\).  The possible one-step
term is no larger because \(gKw^2\gg1\).  Off the saddle-crossing
interval, one physical integration by parts, repeated on dyadic
complements, gives the same summable bound.  Both collar crossings are
therefore included; no leading stationary approximation or frozen endpoint
is used.

Summing (104.21), multiplying by the actual bounded-variation dyadic
\(k\)-profile, and charging the two open-interval zero-extension jumps
by the endpoint supremum gives

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname {Var}_{k\in\mathbb Z}B_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon
 \frac{g\sqrt A}{\sqrt{gK}}
 \asymp X^\varepsilon\sqrt{\frac{AL}{JD}},            \tag{104.22}
\]

which is (104.1).  At the cone edge \(b/a\to4\), (104.10) makes the
saddle-crossing interval shorter.  No inverse power of
\(2\sqrt a-\sqrt b\) occurs in (104.19)--(104.22).  Empty fibres are
zero, and a singleton is bounded by the supremum in (104.22), so neither
edge collapse nor an integer endpoint creates an omitted term.

Now expand the complete metric member in (104.18).  For the displayed
orientation put \(n=|2\nu-g|\).  Since \(g\) is odd,
\(n\) is an odd positive integer.  On the exact moving interval,

\[
 f_{\nu,g}(k)=\left(\nu-\frac g2\right)\frac{\Lambda_q}{k},\qquad
 |f_{\nu,g}''(k)|
 =\frac{n\Lambda_q}{k^3}
 \asymp\frac{nA^2}{JD}.                              \tag{104.23}
\]

Here \(\delta_q\asymp D/\sqrt A\),
\(\Lambda_q\asymp J^2D^2/A\), and
\(k\asymp JD/A\).  The second-derivative estimate, uniformly on
every partial subinterval used in Abel summation, yields

\[
 \sup_{I'\subseteq I_{a,q}}
 \left|\sum_{k\in I'\cap\mathbb Z}e(f_{\nu,g}(k))\right|
 \ll K\sqrt{\frac{nA^2}{JD}}
      +\sqrt{\frac{JD}{nA^2}}.                       \tag{104.24}
\]

Only \(|I'|\ll K\) is used, so (104.24) remains valid under
cone-edge collapse.  Partial summation with (104.22) gives

\[
\begin{aligned}
 &\left|\sum_{k\in I_{a,q}\cap\mathbb Z}
 B_{a,q,g}(k)e(f_{\nu,g}(k))\right|\\
 &\quad\ll_\varepsilon X^\varepsilon
 \sqrt{\frac{AL}{JD}}
 \left(\frac{JD}{A}\sqrt{\frac{nA^2}{JD}}
       +\sqrt{\frac{JD}{nA^2}}\right)\\
 &\quad= X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{\frac LA}\,n^{-1/2}\right),
\end{aligned}                                         \tag{104.25}
\]

proving (104.2).  This displays the exact cancellation of every \(D\)
power in a fixed row.

It remains to sum the whole metric Fourier series.  From (104.17),
\(R\le G\), and \(g\asymp G\), splitting first where
\(|\nu|\ll G\) and then near the half-integer \(g/2\) gives

\[
 \sum_{\nu\in\mathbb Z}|\widehat W_R(\nu)|
 |2\nu-g|^{1/2}\ll\sqrt G,\qquad
 \sum_{\nu\in\mathbb Z}|\widehat W_R(\nu)|
 |2\nu-g|^{-1/2}\ll G^{-1/2}.                       \tag{104.26}
\]

For the second estimate, the possible near-resonant distances are positive
odd integers and
\(G^{-1}\sum_{1\le m\ll G}m^{-1/2}\ll G^{-1/2}\) when
\(R\asymp G\); if \(R\ll G\), Fourier decay makes the
near-resonant region smaller still.  The first estimate follows similarly,
and the remote tails converge after choosing \(N>3\).  In particular,
the density coefficient \(\widehat W_R(0)\) is present and is charged
with \(n=g\).

Combining (104.25)--(104.26), one actual odd lift contributes

\[
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{AL}\sqrt G+\sqrt{L/A}\,G^{-1/2}\right)
 \ll_\varepsilon X^\varepsilon(L+1).                 \tag{104.27}
\]

There are \(O(G)\) literal odd lifts.  For a nonempty fibre
\(G\gg1\), and \(L\ge1\), hence

\[
 |F_a(q)|
 \ll_\varepsilon X^\varepsilon G(L+1)
 \ll_\varepsilon X^\varepsilon\frac{L^2}{A}.         \tag{104.28}
\]

The logarithmically many metric members and profiles and the fixed finite
orientation ledger are absorbed into \(X^\varepsilon\).  This proves
(104.3) with every owner retained.

There are \(O(A)\) bases and at most \(O(D)\) integers in the
half-open \(q\)-shell.  Squaring (104.28), with the usual renaming of
\(\varepsilon\), proves (104.4).  Finally, zero extension gives the
literal direct inequality

\[
\begin{aligned}
 \mathcal G_H^{\rm act}
 &=\sum_{a,n}\left|\sum_{0\le h<H}(-1)^hF_a(n+h)\right|^2\\
 &\le H\sum_{a,n}\sum_{0\le h<H}|F_a(n+h)|^2\\
 &\le H^2\sum_{a,q}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon\frac{H^2DL^4}{A}.
\end{aligned}                                         \tag{104.29}
\]

Boundary rows are counted at most \(H\) times; no periodic extension is
made.  Since

\[
 E_0\asymp LJD^2,\qquad
 \frac{H^2E_0}{\rho}
 \asymp\frac{H^2L^4}{AD},                             \tag{104.30}
\]

the quotient of (104.29) by (104.30) is exactly \(D^2\).  For each
fixed \(C\), if \(D\le(\log(2+X))^C\), apply (104.29) with
\(\varepsilon/2\) and use \(D^2\le X^{\varepsilon/2}\) for
large \(X\).  This proves the target in every fixed/polylogarithmic
short shell.  If \(D=X^\theta\) with fixed \(\theta>0\), the
route loses \(X^{2\theta}\), so no polynomial \(q\)-range follows
without a genuine signed \(q\)-correlation or a stronger average-row
theorem.

## 4. First doubtful or unproved step

The first seam that required proof, rather than formal scaling, was the
uniform actual amplitude assertion (104.15)--(104.22).  A pointwise
stationary estimate does not imply sampled \(k\)-variation, and a sharp
physical endpoint would create a false large-variation Fresnel tail.  The
literal accepted symbol avoids that problem in exactly two ways: its
physical endpoint pieces are the fixed smooth collars, resolved because
\(gKw_g^2\gg1\), and its complete centered phase satisfies the exact
differential identity (104.19).  The actual homogeneous profile is
\(k\)-independent; the only exterior \(k\)-profile has bounded
variation; the metric member and carrier are excluded from the amplitude
and then recoupled exactly in (104.18).  Hence the seam is closed for the
literal symbol uniformly in \(q\), including \(b/a\to4\).

The corresponding theorem would fail if a previously unrecorded rapidly
moving \(k\)-owner were inserted outside (104.14).  The supplied owner
formula contains no such factor.  Thus no mathematical step in the
fixed-\(q\) row theorem remains open on the stated interface; this
specific multiplier audit is the first item for independent seam review.

The first genuinely unproved downstream step is the polynomial-length
fixed-\(a\) Gram.  Equations (104.29)--(104.30) show that fixed-row
control has no mechanism to recover \(D^2\).  The alternating sign in
the Gram was deliberately not discarded inside a claimed theorem: Cauchy
discards it and leaves the quantified deficit.  Closing a polynomial
\(D\)-range requires a new signed \(q\)-shift theorem for the full
mode-resolved actual coefficient, with the primitive and owner masks,
independent moving reciprocal fibres, density and discrepancy modes, and
entry/exit all still coupled.

## 5. Required control tests and outcomes

- **`general_q_reciprocal_geometry` -- passed.**  Equation (104.7) gives
  \(\delta_q\asymp D/\sqrt A\) and
  \(\Lambda_q\asymp J^2D^2/A\); (104.8)--(104.10) retain the exact
  open interval and saddle map.  The \(b/a\to4\) collapse is explicit:
  only an upper length bound is used, and no cone-edge denominator appears.
- **`K_G_VD_normalization` -- passed.**  With
  \(K\asymp JD/A\) and \(G\asymp L/A\), (104.22) is exactly
  \(V_D=\sqrt{AL/(JD)}\).
- **`complete_centered_integral` -- passed.**  Equations
  (104.11)--(104.14) retain the whole integral and the exact carrier.  No
  leading Gaussian or stationary correction is substituted.
- **`sampled_k_BV_through_collars` -- passed.**  The complete-Fresnel
  estimate follows from (104.19)--(104.22).  Both fixed physical collars
  have resolution \(JD/(AL)\gg1\); overlapping cone-edge collars and
  shortened saddle paths are harmless.
- **`odd_metric_frequency` -- passed.**  The total frequencies are
  \(2\nu-g\) and \(2\nu+g\), positive in absolute value because
  \(g\) is odd.  No formal quotient-parity or half-frequency deletion
  is used.
- **`density_and_discrepancy_modes` -- passed.**  The complete Fourier
  series (104.17)--(104.18) is summed.  The mean \(\nu=0\) has
  \(n=g\) and is estimated by the same curvature argument.  At an
  exact metric center the full punctured Fourier series vanishes; its mean
  is not separately erased.
- **`reciprocal_second_derivative` -- passed.**  The exact derivative is
  \(n\Lambda_q/k^3\asymp nA^2/(JD)\), leading to (104.24)--(104.25)
  with complete \(D\)-cancellation.
- **`Fourier_half_moments` -- passed.**  Both moments, including the
  near-\(g/2\) modes and remote tails, are proved in (104.26).  Oddness
  prevents a singular term.
- **`primitive_and_prior_owners` -- passed.**  The literal
  \((a,b)=1\) mask is retained; unlike \(q=1\), it is not declared
  automatic.  The square-ray, residual/\(\rho\)-safe, exact-center,
  original-mode, diagonal, positive-safe, boundary, and all other prior
  masks are fixed before the \(k\)-sum and never replaced by a smooth
  fiction.
- **`profiles_floors_stars_orientations` -- passed.**  The actual
  \(\eta,\Phi,W,q_X\) profiles, finite supports, floors, starred
  endpoint conventions, signs, and both conjugate orientations stay in
  (104.14) and (104.18).  The second orientation uses
  \(|2\nu+g|\) and has the identical estimate.
- **`entry_exit_and_zero_extension` -- passed.**  The equalities at both
  ends of (104.8) are excluded.  The saddle enters and exits through the
  complete collar pieces, and extension by zero costs exactly the two
  endpoint suprema in (104.22).  The Gram uses zero, not periodic,
  extension.
- **`empty_and_singleton_fibres` -- passed.**  Empty \(k\)- or
  \(g\)-fibres contribute zero.  A singleton \(k\)-fibre is bounded
  by (104.22), and a singleton lift is included in the \(O(G)\) finite
  ledger.  Cone-edge collapse therefore creates no exceptional case.
- **`Pell_near_square_and_fourth_power` -- passed.**  The proof uses no
  Diophantine lower bound for \(\|\Lambda_q/k\|\).  Thus the primitive
  near-square Pell ray \((25,27)\), its fourth-power strict-metric
  recurrent specializations from the accepted singleton control, general
  near-square rays, and exact or near reciprocal centers all obey the same
  upper estimate.  Previously owned square rays remain excluded rather
  than silently reintroduced.
- **`G_one_and_small_K` -- passed.**  For \(G\asymp1\), the lift count
  and both Fourier moments are constant-sized.  Empty or one-point short
  \(k\)-intervals are handled directly.  On a nonempty resolved fibre,
  \(K/(gA)\asymp JD/(AL)\gg1\), so the collar argument never requires
  an unlicensed large-\(K\) lower bound beyond the accepted geometry.
- **`arbitrary_coefficient_false_shadow` -- rejected, as required.**  A
  phase-conjugated multiplier can align
  \(e((\nu-g/2)\Lambda_q/k)\) and can make its discrete variation as
  large as the sum of pointwise masses.  It violates (104.15), (104.19),
  and the bounded-variation owner ledger.  Equation (104.1) is an
  actual-symbol theorem, not a coefficient-uniform theorem.
- **`unsigned_false_shadow` -- rejected, as required.**  Replacing the
  inner sum by \(\sum_k|B(k)|\) deletes (104.24) and may cost the full
  reciprocal-fibre length.  No unsigned analogue follows.
- **`row_energy_D_count` -- passed.**  The exact counts \(O(A)\) and
  \(O(D)\) give \(DL^4/A\), not \(L^4/(AD)\), in (104.4).
- **`Cauchy_to_Gram_D_squared_deficit` -- passed.**  Equation (104.29)
  counts each zero-extended row entry at most \(H\) times and gives
  \(H^2DL^4/A\).  Against (104.30), the loss is exactly \(D^2\).
- **`polylog_absorption` -- passed.**  For every fixed \(C\), the
  \(D^2\) loss is absorbed when
  \(D\le(\log(2+X))^C\) by applying the row theorem with a smaller
  epsilon.  The same holds along any prescribed \(D=X^{o(1)}\) family;
  no uniform positive power is hidden in this notation.
- **`polynomial_q_survivor` -- no polynomial survivor from this route.**
  If \(D=X^\theta\) with fixed \(\theta>0\), Cauchy loses
  \(X^{2\theta}\).  The proved strict survivors are the already owned
  singleton and the new bounded/polylogarithmic short-shell range.  This is
  not a lower-bound obstruction to a future signed actual Gram.
- **`primary_source_hypothesis_map` -- passed by nonuse.**  No external
  theorem or web source is invoked.  In particular, no source is credited
  with polynomial \(q\)-cancellation for the moving actual symbol.
- **`downstream_and_exponent_scope` -- passed.**  The result proves a
  fixed-\(q\) row theorem and its fixed/polylogarithmic short-shell Gram
  consequence only.  It does not close the polynomial-length fixed-\(a\)
  Gram, canonical density-discrepancy energy, hard signed cone, another M2
  packet, M9-M2, M9-M1, M9, endpoint uniformity, the quarter target, or any
  global exponent.

No numerical experiment and no external source were used.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/derivation_packet.md`
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/briefs/fixed_q_sampled_k_attack.md`
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/synthesis.md`
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/reports/q1_stationary_energy_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md`
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`
- `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/synthesis.md`
- Live Round-104 conductor normalization message requiring the explicit
  \(b/a\to4\) cone-edge, zero-extension, and \(D^2\) Gram audits.

No sibling Round-104 report, shared synthesis, validation artifact, proof
draft, external source, or computational artifact was used.

## 7. Recommended state effect

**Promote after independent seam review** the scoped uniform actual-symbol
sampled-\(k\) theorem (104.1), its literal row bound (104.3), and the
fixed/polylogarithmic short-shell consequence of (104.5).  Record explicitly
that the mechanism is the complete centered identity (104.19), resolved
fixed physical collars, the odd total metric frequency, and reciprocal
\(k\)-curvature.  Record equally explicitly that the theorem is false as
a coefficient-uniform or unsigned assertion.

Retain `M9-M2-primitive-ray-fixed-a-actual-Gram` as open for every
polynomial-length \(q\)-row.  The row theorem supplies a new input to that
obligation but misses its target by exactly \(D^2\) after direct Cauchy.
Retain `M9-M2-top-endpoint-density-discrepancy-energy` as open, and retain
the already proved `M9-M2-primitive-ray-q1-actual-diagonal-energy` as a
disjoint singleton owner.  Do not infer the hard signed cone, another M2
packet, M9-M2, M9-M1, M9, endpoint uniformity, the quarter target, or an
exponent.
