# Small-angle collapse attack

- Campaign: m9-m1-lower-radial-small-angle-collapse
- Round: 62
- Task: small_angle_collapse_attack
- Role: discovery
- Status: candidate evidence only; no shared state was edited
- Method allocation: entirely analytic; no numerical experiment

## 1. Result

Put

\[
 R=X^{1/4},\qquad Y=\sqrt X,\qquad y=\lfloor\sqrt X\rfloor,
\qquad d_{n,h}=2h\sqrt{\frac Xn}.
\]

For the accepted exact angular multiplier,

\[
 \Omega_X^*(n,h)=
 \sum_j{\bf1}_{h\leq H_j}
 \Phi\!\left(\frac h{H_j+1}\right)[w_j(d_{n,h})]^*,
\qquad H_j=\left\lfloor\frac{D_j}{R}\right\rfloor,
\]

one has, uniformly for every positive integer \(n\) and every positive
divisor \(h\mid n\),

\[
 \boxed{
 \Omega_X^*(n,h)
 ={\bf1}_{d_{n,h}\leq y}^{\,*}
 +O\!\left(\min\left\{1,\frac nY\right\}\right).}
\tag{1.1}
\]

The nontrivial small-angle assertion is the \(O(n/Y)\) part.  Its exact
geometric proof is valid throughout

\[
 n\leq\frac94Y.
\tag{1.2}
\]

In that range the height cutoff is automatically satisfied on every
nonzero active profile, the inactive bottom is identically zero at
\(d_{n,h}\), and the active profiles telescope to the one-sided hard
cutoff.  Above (1.2), (1.1) remains true with the displayed minimum by
the uniform boundedness of both sides, but it is no longer a small error.

Define

\[
 \rho_X=\frac{4X}{y^2},\qquad
 \mathcal D_X^*(n)=
 \sum_{\substack{h q=n\\q\ {\rm odd}\\q\geq\rho_Xh}}^{*}\chi_4(q)
 =
 \sum_{\substack{q\mid n\\q\ {\rm odd}\\q^2\geq\rho_Xn}}^{*}\chi_4(q).
\tag{1.3}
\]

Then

\[
 \boxed{
 |\mathcal C_X^*(n)-\mathcal D_X^*(n)|
 \ll \tau(n)\min\left\{1,\frac nY\right\}.}
\tag{1.4}
\]

For fixed \(V\in C_c^\infty((a,b))\), \(0<a<b<\infty\), and
\(bN\leq Y\), the normalized radial replacement error is

\[
 \boxed{
 \left|
 \sum_nV(n/N)\{\mathcal C_X^*(n)-\mathcal D_X^*(n)\}
 n^{-3/4}e(\sqrt{Xn})
 \right|
 \ll_V\frac{N^{5/4}\log(2N)}Y.}
\tag{1.5}
\]

Thus the replacement is target-safe for every fixed
\(N=X^\nu\), \(\nu\leq2/5\): it has a power saving for
\(\nu<2/5\), and costs only \(O_V(\log X)\) at \(\nu=2/5\).
The exact power threshold of this unconditional absolute error ledger is
\(2/5\).

The limiting coefficient does not collapse to \(r_2(n)/4\), an Euler
product, or an unsigned divisor count.  Its radial sum is exactly the
one-sided signed product cone in (3.17) below.  A prime subfamily proves
that taking absolute values has power-sized capacity.  No signed
\(O(X^\varepsilon)\) estimate for the limiting cone is proved here.

## 2. Exact statement and hypotheses

Use the accepted denominator partition

\[
 {\bf1}_{1\leq d\leq y}
 =w_0(d)+\sum_{j=1}^{J}w_j(d)+w_{\rm bot}(d),
\tag{2.1}
\]

\[
 D_j=2^{-j}y,\qquad
 w_0(d)={\bf1}_{d\leq y}W(d/y),\qquad
 w_j(d)=W(d/D_j)\quad(j\geq1),
\tag{2.2}
\]

where \(W(t)=\eta(t)-\eta(2t)\) is nonnegative,

\[
 \operatorname {supp}W\subset[1/2,4/3],
\qquad
 w_{\rm bot}(d)=\eta(d/D_{J+1}),
\qquad
 D_{J+1}<R,
\tag{2.3}
\]

and therefore

\[
 \operatorname {supp}w_{\rm bot}\subset[1,4R/3).
\tag{2.4}
\]

The sum in \(\Omega_X^*\) is over the active top and interior profiles
only; the bottom is removed before Fourier expansion and is already
target-safe on the physical scale.

The star in this report is the accepted stationary endpoint convention.
For the collapsed cutoff it means exactly

\[
 {\bf1}_{d\leq y}^{\,*}=
 \begin{cases}
 1,&d<y,\\
 1/2,&d=y,\\
 0,&d>y.
 \end{cases}
\tag{2.5}
\]

Artificial smooth support endpoints contribute zero because \(W=0\)
there.  The only nonzero hard stationary endpoint is \(d=y\), owned by
the top profile with \(w_0(y)=1\).  The separate one-sided cotangent
boundary is not part of \(\Omega_X^*\) and is not altered by (1.1).

The Vaaler profile is

\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,\qquad 0<u<1,
\tag{2.6}
\]

with its accepted continuous endpoint values \(\Phi(0)=1\),
\(\Phi(1)=0\).  Only terms with \(h\leq H_j\) occur, so every sampled
argument belongs to \([0,1)\).

For (1.5), the support constants of \(V\) are fixed, \(N\geq1\), and
\(bN\leq Y\).  For every fixed \(\nu<1/2\) this hypothesis holds for all
sufficiently large \(X\); at \(\nu=2/5\) it is automatic.

## 3. Proof or derivation

### 3.1 Uniform quadratic Vaaler expansion

The Laurent expansion of the cotangent gives

\[
 \cot(\pi u)=\frac1{\pi u}-\frac{\pi u}{3}+O(u^3),
\]

and hence

\[
 \Phi(u)=1-\frac{\pi^2}{3}u^2
 +\frac{\pi^2}{3}u^3+O(u^4)
\qquad(u\to0).
\tag{3.1}
\]

The function

\[
 G(u)=\frac{\Phi(u)-1}{u^2}
\]

extends continuously to \([0,1]\): its values at the two endpoints are
\(G(0)=-\pi^2/3\) and \(G(1)=-1\).  Therefore

\[
 C_\Phi:=\sup_{0\leq u\leq1}|G(u)|<\infty,
\qquad
 \boxed{|\Phi(u)-1|\leq C_\Phi u^2\quad(0\leq u\leq1).}
\tag{3.2}
\]

This is uniform on the complete actual coefficient range, not merely on
a formal asymptotic subinterval.

### 3.2 Floors, active cutoff, bottom, and telescope

Suppose first that \(n\leq9Y/4\) and that
\([w_j(d_{n,h})]^*\neq0\).  Since

\[
 H_j+1>\frac{D_j}{R},
\]

the exact floor gives

\[
 \frac h{H_j+1}
 <\frac{hR}{D_j}
 =\frac{d_{n,h}}{2D_j}\sqrt{\frac nY}.
\tag{3.3}
\]

For every interior profile with a nonzero value,
\(d_{n,h}/D_j<4/3\); for the top profile it is at most \(1\).
Consequently

\[
 \frac h{H_j+1}
 <\frac23\sqrt{\frac nY}\leq1.
\tag{3.4}
\]

Because \(h,H_j\) are integers, (3.4) implies \(h\leq H_j\).  Thus the
active cutoff in \(\Omega_X^*\) deletes no nonzero profile contribution.
This also handles the floor exactly; no replacement of \(H_j\) by
\(D_j/R\) has been made.

For every \(h\geq1\),

\[
 d_{n,h}\geq2\sqrt{\frac Xn}\geq\frac43R.
\tag{3.5}
\]

Equations (2.3)--(2.4) therefore give
\[
 w_{\rm bot}(d_{n,h})=0.
\tag{3.6}
\]
The finite identity
\[
 \sum_{j=0}^{J}W(2^jt)
 =\eta(t)-\eta(2^{J+1}t)
\]
holds for every real \(t>0\), not only at integer denominator samples.
After adding the bottom profile and applying the one-sided top cutoff, the
exact partition therefore holds at the generally nonintegral stationary
point \(d_{n,h}\).  It now yields

\[
 \sum_{j\ {\rm active}}[w_j(d_{n,h})]^*
 ={\bf1}_{d_{n,h}\leq y}^{\,*}.
\tag{3.7}
\]

For \(d_{n,h}<y\), this is the ordinary telescoping sum \(1\).  At
\(d_{n,h}=y\), every interior profile is zero, the top value is \(1\),
and its stationary half-weight gives \(1/2\).  For \(d_{n,h}>y\), every
active profile is zero.  Thus (3.7) retains the top, the bottom owner,
and every star without double counting.

Using (3.2)--(3.4), nonnegativity, and (3.7),

\[
 \begin{aligned}
 \left|\Omega_X^*(n,h)-{\bf1}_{d_{n,h}\leq y}^{\,*}\right|
 &\leq
 C_\Phi\sum_j
 \left(\frac h{H_j+1}\right)^2[w_j(d_{n,h})]^*\\
 &\leq\frac{4C_\Phi}{9}\frac nY
 \sum_j[w_j(d_{n,h})]^*
 \ll\frac nY.
 \end{aligned}
\tag{3.8}
\]

This proves the nontrivial assertion on the full clean geometric range
(1.2).  For arbitrary \(n\), the cutoff \(h\leq H_j\) puts the argument
of \(\Phi\) in \([0,1)\), \(\Phi\) is bounded there, and every selected
active profile is part of the nonnegative partition (2.1).  Hence

\[
 |\Omega_X^*(n,h)|+{\bf1}_{d_{n,h}\leq y}^{\,*}\ll1.
\tag{3.9}
\]

Combining (3.8) for \(n\leq Y\) with (3.9) for \(n>Y\) proves the
stronger uniform form (1.1).  The interval \(Y<n\leq9Y/4\) still enjoys
the exact ownership identities (3.4)--(3.7), although the error there is
only of constant size.

### 3.3 Coefficient and radial error

The hard cutoff is equivalent, with no asymptotic replacement, to

\[
 2h\sqrt{\frac Xn}\leq y
 \Longleftrightarrow
 q\geq\frac{4X}{y^2}h
 \Longleftrightarrow
 q^2\geq\frac{4X}{y^2}n.
\tag{3.10}
\]

Equality in any of these conditions carries the half-weight.  Summing
(1.1) over the incidences \(hq=n\), \(q\) odd, and using
\(|\chi_4(q)|=1\), proves (1.4).

On the support of \(V(n/N)\), \(n\asymp_VN\).  The elementary divisor
hyperbola count gives

\[
 \sum_{n\leq Z}\tau(n)
 =\sum_{ab\leq Z}1
 \leq Z\sum_{a\leq Z}\frac1a
 \ll Z\log(2Z).
\tag{3.11}
\]

Therefore, for \(bN\leq Y\),

\[
 \begin{aligned}
 \sum_n|V(n/N)|n^{-3/4}
 |\mathcal C_X^*(n)-\mathcal D_X^*(n)|
 &\ll_V\frac1Y
 \sum_{n\asymp_VN}\tau(n)n^{1/4}\\
 &\ll_V\frac{N^{5/4}\log(2N)}Y.
 \end{aligned}
\tag{3.12}
\]

This proves (1.5).  If \(N=X^\nu\), its power is

\[
 X^{(5\nu-2)/4}\log X.
\tag{3.13}
\]

For fixed \(\nu<2/5\), (3.13) has a strict power saving.  At
\(\nu=2/5\), it is \(O(\log X)\), hence \(O_\varepsilon(X^\varepsilon)\).
For \(\nu>2/5\), this unconditional triangle ledger loses the positive
power \((5\nu-2)/4\).  If a literal \(O(1)\), rather than
\(O(X^\varepsilon)\), replacement is desired, (3.12) asks
\[
 N\ll\left(\frac{Y}{\log(2Y)}\right)^{4/5};
\tag{3.14}
\]
polylogarithmic changes do not alter the power threshold \(2/5\).
Restoring the Round-14 external factor \(R\) exactly once turns the
endpoint \(O(\log X)\) into the physical target
\(O_\varepsilon(RX^\varepsilon)\).

### 3.4 Exact arithmetic form and the limiting cone

Write \(n=2^am\), with \(m\) odd.  In (1.3), every odd divisor is
\(q=m/s\), where \(s\mid m\), and \(h=2^as\).  Complete
multiplicativity of \(\chi_4\) on odd integers gives

\[
 \boxed{
 \mathcal D_X^*(2^am)=
 \chi_4(m)
 \sum_{\substack{s\mid m\\
 s\leq\sqrt{m/(\rho_X2^a)}}}^{*}\chi_4(s).}
\tag{3.15}
\]

Thus the coefficient is a one-sided character-divisor prefix.  It is not
multiplicative.  For example, for \(y\geq9\), one has
\(\rho_X<5\), and direct divisor inspection gives

\[
 \mathcal D_X^*(5)=1,\qquad
 \mathcal D_X^*(101)=1,\qquad
 \mathcal D_X^*(505)=2.
\tag{3.16}
\]

The limiting smooth radial sum is exactly

\[
 \boxed{
 \mathcal L_{X,V}(N)=
 \sum_{\substack{h\geq1,\ q\geq1,\ q\ {\rm odd}\\
 q\geq\rho_Xh}}^{*}
 \chi_4(q)(hq)^{-3/4}V(hq/N)e(\sqrt{Xhq}).}
\tag{3.17}
\]

This is a one-sided product cone, not a one-variable coefficient with a
known multiplicative factorization.  Its Dirichlet generating function
has the exact Perron form

\[
 \boxed{
 \sum_{n\geq1}\frac{\mathcal D_X^*(n)}{n^w}
 =\frac1{2\pi i}\int_{(c)}
 \rho_X^{-z}\zeta(w+z)L(w-z,\chi_4)\frac{dz}{z},}
\tag{3.18}
\]

where \(\operatorname {Re}w>1+c\), \(c>0\), and the integral is taken in
the symmetric Perron sense so equality receives weight \(1/2\).
Indeed expanding the two Dirichlet series produces
\(h^{-w-z}\chi_4(q)q^{-w+z}\), and Perron projects exactly
\(q/(\rho_Xh)\geq1\).

The unrestricted product would instead have coefficient
\[
 \sum_{q\mid n}\chi_4(q)=\frac{r_2(n)}4
\]
and Dirichlet series \(\zeta(w)L(w,\chi_4)\).  The projection in (3.18)
cannot be removed.  For every odd prime \(p>\rho_X\),
\[
 \mathcal D_X^*(p)=\chi_4(p),
\tag{3.19}
\]
whereas \(r_2(p)/4=1+\chi_4(p)\); in particular primes
\(p\equiv3\pmod4\) give \(\mathcal D_X^*(p)=-1\) but \(r_2(p)=0\).
This rules out importing the completed Hardy--Voronoi coefficient.

There is also a sharp scoped capacity obstruction before grouping product
fibres.  For a permissible fixed \(V\) that equals \(1\) on \([1,2]\),
restrict \(h\leq\sqrt{N/(2\rho_X)}\) and
\(N/h\leq q\leq2N/h\), \(q\) odd.  The cone condition is then automatic,
and elementary counting gives

\[
 \sum_{\substack{N\leq hq\leq2N\\q\ {\rm odd}\\q\geq\rho_Xh}}
 (hq)^{-3/4}
 \gg N^{-3/4}\sum_{h\leq\sqrt{N/(2\rho_X)}}\frac Nh
 \gg N^{1/4}\log N.
\tag{3.20}
\]

Thus taking absolute values at the \((h,q)\)-incidence level loses a
power.  Even grouping into the actual coefficient does not make an
absolute-value strategy target-sized: (3.19) and the classical dyadic
prime lower bound give

\[
 \sum_{N\leq n\leq2N}
 |\mathcal D_X^*(n)|n^{-3/4}
 \geq\sum_{N\leq p\leq2N}p^{-3/4}
 \gg\frac{N^{1/4}}{\log N}.
\tag{3.21}
\]

Thus coefficientwise absolute values, the divisor bound, or an unsigned
replacement miss the normalized target by a power for every fixed
\(N=X^\nu\), \(\nu>0\).  Equation (3.20) does not refute cancellation in
the actual \(\chi_4(q)e(\sqrt{Xhq})\) sum; it identifies exactly where a
proof must spend the sign and radial phase.

## 4. First doubtful or unproved step

The collapse (1.1), coefficient comparison (1.4), total error (1.5), and
arithmetic identities (3.15)--(3.18) have no unproved step beyond the
accepted partition, coefficient, and star conventions.

The first unproved analytic statement is

\[
 \boxed{\mathcal L_{X,V}(N)\ll_{\varepsilon,V}X^\varepsilon}
\tag{4.1}
\]

uniformly in a lower radial range.  For \(\nu\leq2/5\), (4.1) together
with (1.5) would close the corresponding smooth lower-radial contribution.
Neither the prefix identity (3.15) nor the Perron factorization (3.18)
supplies (4.1): the former retains an incomplete divisor interval, while
the latter retains the coupled Perron variable and the one-sided cone.
The capacities (3.20)--(3.21) prove that a successful argument cannot take
absolute values before exploiting \(\chi_4\) and the product phase.

No return to \(r_2/4\) is lawful.  Conversely, a B-process applied
formally to one leg of (3.17) returns to the same reciprocal M1 geometry;
the authorized context contains no new signed theorem at that interface.
This report therefore stops at the exact signed cone rather than claiming
a cancellation estimate.

## 5. Required control tests and outcomes

1. **Phi_quadratic_expansion — pass.**  Equations (3.1)--(3.2) prove a
   uniform \(O(u^2)\) bound on the entire actual interval \(0\leq u\leq1\).
2. **height_floor_ratio — pass.**  Equation (3.3) uses the strict exact
   inequality \(H_j+1>D_j/R\); no floor is discarded.
3. **active_cutoff — pass.**  On the clean range, (3.4) and integrality
   imply \(h\leq H_j\) for every nonzero active profile.
4. **partition_telescope — pass.**  Equation (3.7) follows from the exact
   finite partition after the bottom is shown to vanish.
5. **bottom_support — pass.**  Equations (3.5)--(3.6) give zero bottom
   stationary mass for \(n\leq9Y/4\).  Its separate pre-Fourier
   \(O(R)\) owner is unchanged.
6. **hard_top_and_star — pass.**  Equation (2.5) retains half weight at
   \(d=y\); all artificial smooth endpoints have zero profile value.
   The cotangent boundary remains separate.
7. **divisor_error_sum — pass.**  The incidence count is at most
   \(\tau(n)\), and the elementary average (3.11) gives the exact
   \(N^{5/4}\log(2N)/Y\) ledger.
8. **two_fifths_threshold — pass.**  Equation (3.13) is power-saving
   below \(2/5\), logarithmic at \(2/5\), and power-losing above it.
9. **one_sided_divisor_identity — pass.**  Equations (1.3), (3.10),
   (3.15), and (3.18) retain the exact \(y/\sqrt X\) factor and equality
   star.
10. **signed_radial_capacity — obstruction proved.**  Equations
    (3.19)--(3.21) rule out incidence-wise, coefficientwise absolute, or unsigned closure,
    but do not rule out the actual signed theorem (4.1).
11. **downstream_scope — pass.**  A target-safe replacement error is not
    a bound for \(\mathcal L_{X,V}\).  No full lower GAR, full GAR,
    blockwise M9-M1, M9, or Gauss-circle exponent follows.

## 6. Dependencies and exact artifacts used

Only the Round-62 selected context was used:

- protocol.md
- state/proof_obligations.yml, specifically the accepted Phi-regularity,
  dyadic-profile, global-recombination, V2, critical-radial, and
  lower-radial nodes
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/derivation_packet.md
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md
- rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md
- rounds/codex-managed/m9-m1-lower-radial-phase-diagram/synthesis.md

The explicit profile report supplies the exact telescope, support
constants, bottom owner, height floor, top jump, and nonnegativity.
Round 14 supplies the exact angular coefficient, parity, star, external
\(R\), and the warning against an \(r_2/4\) collapse.  Round 61 supplies
the lower-radial scope.  The dyadic prime lower bound used only in the
scoped capacity control (3.20) is the classical elementary Chebyshev
bound; no new analytic theorem for (3.17) and no web source was used.

## 7. Recommended state effect

Promote, after independent validation, a scoped
M9-M1-subcritical-small-angle-collapse lemma containing:

1. the uniform multiplier comparison (1.1), with the exact clean
   floor/telescope range \(n\leq9Y/4\);
2. the coefficient comparison (1.4);
3. the smooth radial error (1.5) and its exact power threshold
   \(\nu=2/5\), including the logarithmic endpoint;
4. the exact one-sided coefficient and cone identities
   (1.3), (3.15), (3.17), and (3.18);
 5. the absolute-capacity obstructions (3.20)--(3.21).

For every smooth block with \(\nu\leq2/5\), revise the lower-radial
obligation to the single signed target (4.1); the replacement error is
already target-safe there.  Keep (4.1), the range \(2/5<\nu<1/2\), full
GAR, blockwise M9-M1, M9, and the final exponent open.  Reject any
identification of \(\mathcal D_X^*\) with \(r_2/4\), any deletion of the
one-sided Perron projector, and any proof based only on absolute
coefficient mass.
