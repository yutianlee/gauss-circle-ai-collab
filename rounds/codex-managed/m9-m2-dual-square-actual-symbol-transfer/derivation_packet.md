# Round 106 derivation packet

Campaign: m9-m2-dual-square-actual-symbol-transfer

Starting graph SHA-256:
2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de

## 1. Frozen actual row

On one residual hard-top block let

\[
 b=a+2q,\qquad a\asymp b\asymp A,\qquad q\asymp D,\qquad
 K\asymp {JD\over A},\qquad G\asymp {L\over A}.
\]

Put

\[
 \delta_q=\sqrt b-\sqrt a,\qquad
 \Lambda_q={X\delta_q^2\over2},\qquad
 I_{a,q}=\left({J\delta_q\over2\sqrt a},
 {J\delta_q\over\sqrt b}\right).
\]

One orientation of the exact zero-extended row has the form

\[
\begin{aligned}
 F_{a,R}^{-}(q)
 ={}&\mathbf1_{\rm own}(a,q)
 \sum_{\substack{g\ {\rm odd}\\g\in\mathcal G_{a,b}}}
 \sum_{\nu\in\mathbb Z}\widehat W_R(\nu)\\
 &\times\sum_{k\in I_{a,q}\cap\mathbb Z}
 B_{a,q,g}^{-}(k)
 e\!\left(\left(\nu-\frac g2\right){\Lambda_q\over k}\right).
\end{aligned} \tag{106.1}
\]

The conjugate orientation uses \(\nu+g/2\). The owner factor includes
the primitive mask, square-ray and exact-centre owners, safe-ratio
owners, original Poisson-mode owners, dyadic blocks, endpoint owners and
all prior one-count complements. The complete metric series, including
\(\nu=0\), is retained.

The centered physical factor inside \(B\) is

\[
 \mathfrak B^\circ_{a,q,k}(g)
 =\int_{\sqrt b/2}^{\sqrt a}
 Q_{a,q,g}(y)
 e\!\left(gk\left(y-{J\delta_q\over2k}\right)^2\right)dy. \tag{106.2}
\]

At fixed \(q\), the accepted complete-Fresnel theorem gives

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname{Var}_k B_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over JD}. \tag{106.3}
\]

It does not by itself give a two-variable stationary expansion or
variation in \(q\).

## 2. Exact primitive carrier

For \(c=\nu-g/2\), set \(n=|2\nu-g|\). The branch \(c=-n/2\) has
scalar carrier

\[
 \Psi(q,k)={q\over2}-{n\Lambda_q\over2k}. \tag{106.4}
\]

Expand

\[
 \mathbf1_{(a,q)=1}
 =\sum_{d\mid a,\,d\mid q}\mu(d),\qquad q=du. \tag{106.5}
\]

Every \(d\mid a\) is odd and \((-1)^{du}=(-1)^u\).
For a maximal subinterval \(I\subset[D,2D)\), the progression amplitude
contains the sharp factor \(\mathbf1_{du\in I}\) together with every
owner in (106.1).

## 3. Scalar two-step stationary map

With Poisson convention \(f(x)-\ell x\), the \(k\)-stationary point and
Hessian factor are

\[
 k_*^2={n\Lambda_{du}\over2\ell},\qquad
 |f''(k_*)|^{-1/2}
 =2^{-3/4}(n\Lambda_{du})^{1/4}\ell^{-3/4}, \tag{106.6}
\]

and the phase becomes

\[
 {du\over2}-J(\sqrt{a+2du}-\sqrt a)\sqrt{n\ell}. \tag{106.7}
\]

For the \(u\)-dual integer \(h\), put \(s=d-2h\). The stationary point,
Hessian factor and value are

\[
 b_*=a+2du_*={4d^2Xn\ell\over s^2}, \tag{106.8}
\]

\[
 |F''(u_*)|^{-1/2}
 ={b_*^{3/4}\over dJ^{1/2}(n\ell)^{1/4}}, \tag{106.9}
\]

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{dn\ell/s}-{1\over2}\sqrt{as/d}\right)^2. \tag{106.10}
\]

Here \(s>0\) is odd and

\[
 e(-as/(4d))=-i\chi_4(a/d)\chi_4(s). \tag{106.11}
\]

The Gaussian units of (106.6) and (106.9) are \(e(-1/8)\) and
\(e(1/8)\). Their product is one. This scalar statement does not include
the positive-curvature Gaussian inside the centered physical integral.

The reciprocal support gives

\[
 {nb\over4}<\ell<na,\qquad
 {J\delta_q\over2k_*}=\sqrt{\ell/n}. \tag{106.12}
\]

The maximal \(q\)-interval becomes the condition
\(b_*\in a+2I\), plus transition terms at its two endpoints.

## 4. Candidate complete principal symbol

If the centered integral (106.2) is first reduced by its complete
positive Gaussian branch, then at the joint saddle

\[
 y_*=\sqrt{\ell/n}.
\]

Combining that physical Gaussian, (106.6), and (106.9) formally gives
the principal amplitude

\[
 e(1/8)\,
 {g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}\,
 A^\circ_{ga,gb_*}(g\ell/n), \tag{106.13}
\]

times the literal profiles, metric Fourier coefficient, Möbius factor,
owner complement and transformed cutoff. Formula (106.13) is a candidate
normalization to prove or correct. It may not be used until the complete
centered integral, overlapping collars, and all stationary corrections
are handled uniformly.

## 5. Required complete theorem

The desired deliverable is an identity, uniformly for every maximal
subinterval \(I\),

\[
\begin{aligned}
 \sum_{q\in I}(-1)^qF_a(q)
 ={}&\sum_{d\mid a}\mu(d)
 \sum_{g,\nu,\ell,s}
 \widetilde{\mathcal A}_{a,d,g,\nu,I}(\ell,s)\\
 &\times e\!\left(
 -\left(J\sqrt{dn\ell/s}
 -{1\over2}\sqrt{as/d}\right)^2\right)
 +\mathcal E_{a,I}, \tag{106.14}
\end{aligned}
\]

with both orientations, exact support, and

\[
 \mathcal E_{a,I}\ll_\varepsilon X^\varepsilon L^2/A \tag{106.15}
\]

after all profiles and blocks are assembled. The task may instead prove
that a literal owner or collar prevents (106.14), in which case it must
state the correct exact transform and the smallest surviving correlation.

The target estimate is

\[
 \sup_I|\text{right side of (106.14)}|
 \ll_\varepsilon X^\varepsilon L^2/A. \tag{106.16}
\]

The natural mode-level dual packet is larger than one-row size by
\(\sqrt D\); generic square-root cancellation is therefore insufficient
for the full Gram, which needs the full factor \(D\) over rowwise
capacity.

## 6. Owner and error ledger

The complete audit must treat separately:

- sharp maximal interval endpoints;
- the moving reciprocal interval and its integer entry/exit;
- the finite odd lift fibre and lift endpoints;
- the whole metric Fourier series and both orientations;
- physical lower and upper collars, including overlap at \(b/a\to4\);
- all floors, stars, hard top profiles and dyadic cutoffs;
- primitive Möbius progressions;
- square-ray, exact-centre, safe-ratio, original-mode, diagonal and
  boundary owners;
- empty and singleton \(k\)-, \(u\)-, \(\ell\)- and \(s\)-fibres;
- nonstationary modes and equality/transition saddles;
- the aggregate depth required for stationary remainders;
- Pell, near-square, square and fourth-power controls;
- exact and near metric centres;
- transform inversion and one-count ownership;
- the literal hypothesis map for any imported theorem.

## 7. Completion rule

Promote the polynomial fixed-\(a\) Gram only if (106.14)--(106.16), or
an equivalent direct weighted-shift theorem, is proved with every owner.
Otherwise promote only an exact complete transfer, a strict disjoint
polynomial subrange, or a rigorous owner-preserving equal-capacity
obstruction. Do not infer the hard signed cone, either smooth M2 packet,
M9-M2, M9-M1, endpoint uniformity, M9, the quarter target or a new
exponent without the exact dependency chain.
