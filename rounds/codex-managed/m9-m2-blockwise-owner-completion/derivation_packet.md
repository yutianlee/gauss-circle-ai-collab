# Round 109 derivation packet: blockwise owner completion

Campaign: m9-m2-blockwise-owner-completion

Starting graph SHA-256:
f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d

## 1. Scope

This is a deliverable and reconciliation round.  It does not seek a
new scalar transform.  It tests the exact one-count and norm seam left
by the Round-108 metaplectic return.

The canonical hard top energy is

\[
 \mathcal E_L^\top
 =\mathcal E_{\mathrm{owned},L}
  +2\Re\sum_{A,D,K,G,R}\mathfrak Q_{A,D,K,G,R},
\qquad
 \mathcal E_{\mathrm{owned},L}
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.1}
\]

The target on the residual blocks is

\[
 \sum_{A,D,K,G,R}|\mathfrak Q_{A,D,K,G,R}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.2}
\]

Round 108 showed that a formal completed two-character representation
does not by itself estimate (109.2).  It also isolated a prior seam:
the accepted aggregate owner theorem does not state a blockwise
add--transform--subtract norm.

## 2. Literal hard block

For primitive odd \(a<b<4a\), put

\[
 q=(b-a)/2,\qquad
 \Lambda={X(\sqrt b-\sqrt a)^2\over2},
\tag{109.3}
\]

and retain the open reciprocal interval

\[
 {J(\sqrt b-\sqrt a)\over2\sqrt a}<k<
 {J(\sqrt b-\sqrt a)\over\sqrt b}.
\tag{109.4}
\]

On one block,

\[
 a\asymp A,\quad b-a\asymp D,\quad
 k\asymp K\asymp JD/A,\quad
 |\mathcal G_{a,b}|\asymp G\asymp L/A,
\tag{109.5}
\]

\[
 \rho={AJD^3\over L^3}\gg1.
\tag{109.6}
\]

The complete density and discrepancy multiplier is retained.  The
literal centered coefficient is

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)\,dx.
\tag{109.7}
\]

No owner may be evaluated at a noninteger stationary sample.

## 3. Accepted owner information

The following accepted results are distinct and must not be conflated.

### Round-77 transform error

After fixed physical collars are removed, symmetric finite Poisson
summation gives a complete negative-mode normal form with aggregate
error

\[
 O(L^2\log(2+L)).
\tag{109.8}
\]

The error owns full lattice endpoint samples, removed collars, original
zero and positive modes, equality modes, and negative nonstationary
tails.  Stationary and collar-transition modes remain exact centered
integrals.  The word aggregate in (109.8) is one object of this audit:
does its proof already sum absolute dyadic block contributions, or can
it use cancellation across blocks?

### Round-78 square rays

The complete signed primitive-square/common-squarefree contribution
satisfies

\[
 |\mathcal S_L^\square(X)|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.9}
\]

The corresponding absolute Abel majorant is false and has capacity
\(\sqrt J\,L^{3/2}\).  The proof of (109.9) uses cancellation in \(k\).
The audit must decide whether the block decomposition in (109.2)
preserves that cancellation or destroys it by outside absolute values.

### Round-79 nonsquare and safe blocks

Exact nonsquare centres contribute
\(O_\varepsilon(LX^\varepsilon)\).  Positive incidence closes blocks
with \(AJD^3\ll L^3\), equivalently \(\rho\ll1\).  These are excluded
from the residual hard region.  The audit must display their literal
blockwise scalar norm and ownership boundary.

### Rounds 103--104 short rows

The singleton theorem gives

\[
 \sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon{L^4\over A}.
\tag{109.10}
\]

Uniform fixed-\(q\) sampled variation gives

\[
 |F_a(q)|\ll_\varepsilon X^\varepsilon{L^2\over A},
\qquad
 \sum_{a,q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon{DL^4\over A}.
\tag{109.11}
\]

It closes prescribed polylogarithmic \(D\), not a positive-power
shell.  These are row-energy statements.  They enter a scalar owner
completion only through an explicit bridge to the oriented pair sum.

## 4. Proposed completion identity

Let \(\mathcal B_L\) be the literal dyadic block family, including
orientation and zero-extension tags.  Let
\(\mathcal O=\{77,78,79,103,104\}\), refined as needed into disjoint
owner atoms.  The proposed identity is

\[
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}
  -\sum_{\nu\in\mathcal O}\mathfrak O_{B,\nu}.
\tag{109.12}
\]

The required norm gate is

\[
 \boxed{
 \sum_{B\in\mathcal B_L}\sum_{\nu\in\mathcal O}
 |\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.
 }
\tag{109.13}
\]

The algebraic identity and the analytic norm are separate claims.
If both hold, then

\[
 \sum_B|\mathfrak Q_B^{\mathrm{res}}|
 \leq \sum_B|\mathfrak Q_B^{\mathrm{comp}}|
      +O_\varepsilon(L^2X^\varepsilon).
\tag{109.14}
\]

A total signed estimate for \(\sum_{B,\nu}\mathfrak O_{B,\nu}\) does
not imply (109.13).  Nor does positivity of
\(\mathcal E_{\mathrm{owned},L}\) identify the individual oriented
block contributions.

## 5. Exact separation costs

Smooth \(b-a\) localization has bounded Fourier \(L^1\)-cost:

\[
 \psi((b-a)/D)
 =\int\widehat\psi(\xi)e(-\xi a/D)e(\xi b/D)\,d\xi.
\tag{109.15}
\]

Primitivity has exact Möbius expansion

\[
 1_{(a,b)=1}=\sum_{d\mid a,\ d\mid b}\mu(d),
\tag{109.16}
\]

and the actual \(a^{-3/4}b^{-3/4}\) weights make the scalar divisor
cost \(\sum_d d^{-3/2}<\infty\).  Finite orientations and dyadic block
counts cost \(X^\varepsilon\).

These facts handle smooth projective factors.  They do not control a
pair-dependent owner such as \(ab\) square, an exact reciprocal centre,
or a moving endpoint graph.  Such an owner may still be subtractable
by its own scalar theorem; otherwise its projective norm must be
computed rather than assumed.

## 6. Mandatory controls

1. Distinguish the original Poisson zero mode from the metric density
   mode.  The latter remains in the completed coefficient.
2. Keep the physical hard profile distinct from smooth top-scale
   denominator profiles.
3. Preserve open reciprocal endpoints, half weights, floors, stars,
   both orientations, saddle entry/exit, and zero extension.
4. Prove literal disjointness and one-count ownership before summing.
5. Distinguish scalar signed estimates, scalar outside-absolute block
   estimates, row-energy estimates, and positive Gram estimates.
6. Test square/fourth-power and Pell families, empty/singleton fibres,
   q=1, exact centres, and \(\rho=1\) boundaries.
7. Give an abstract finite countermodel showing why an aggregate owner
   bound alone is insufficient, but do not mistake it for an
   actual-symbol obstruction.
8. Do not infer commutation with the Fejér operator.
9. Do not infer a \(\rho\)-gain from completion.  Round 108 proves the
   complete Gaussian metric functional calculus has equal capacity.
10. Leave smooth balanced/unbalanced packets, M9-M2, M9-M1, endpoint
    uniformity, M9, and the exponent unchanged unless every exact
    dependency is proved.

## 7. Exit fork

The round succeeds by one of the following:

- prove (109.12)--(109.13) for every literal owner, thereby promoting
  the fixed-\(K\) blockwise completion interface;
- prove them for a strict disjoint subfamily and name the exact
  remainder;
- prove a rigorous no-go showing that a named accepted owner theorem
  cannot furnish (109.13), and isolate the smallest replacement norm
  or directional estimate.

No outcome estimates the completed directional two-character vector
unless that separate theorem is actually proved.
