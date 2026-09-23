# Blind scaled-orientation involution rederivation

## 1. Result

There is an exact, fixed-point-free, sign-reversing involution on the
opposing, close, (k=1) incidence packet, provided that both orientation
charts are retained and the incidence domain is closed under the map.  If

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g),
\]

then (\tau_g) preserves (N), (N+r), (r), the phase (P_r(N)), and
both close inequalities, while

\[
 \chi_4(gm')\chi_4(gm)=-\chi_4(d')\chi_4(d)
\]

when (r\equiv2\pmod4).  It exchanges the plus primitive chart with the
opposite chart by

\[
 (U,S,v,w)\longmapsto(v,w,U,S).
\]

The two close inequalities have an exact lattice count.  Put

\[
 F_g=\left\lfloor\frac{D}{2g}\right\rfloor.
\]

For fixed (g,\kappa,U), before coprimality, box, determinant, and support
deletions, the allowed triples ((v,S,w)) are parametrized by

\[
 j=\frac{U-v}{2},\qquad
 -J\le j\le K,
\]

where, for (F_g\ge1),

\[
 J=\left\lfloor\frac{F_g-1}{\kappa}\right\rfloor,
 \qquad
 K=\min\left\{J,\frac{U-1}{2}\right\},
\]

and for each such (j) there are exactly

\[
 F_g^2-\kappa^2j^2
\]

positive pairs ((S,w)).  Thus the close-only count is exactly

\[
 \mathcal C_{g,\kappa,U}
 =(J+K+1)F_g^2
 -\frac{\kappa^2}{6}
 \left[J(J+1)(2J+1)+K(K+1)(2K+1)\right].
\]

It is zero when (F_g=0).  This formula includes (U=1), small (U),
and (D\ge U); no assumption (D<U) is used.

The algebra does **not** imply cancellation for abstract bounded
coefficients.  A pair contributes the difference of two unrelated
coefficient products.  Under the additional common-cell and boundary
hypotheses stated below, a triangle-inequality proof at the requested scale
requires common-cell weighted orbit multiplicity

\[
 \mathfrak M_{\rm cell}
 \ll_\varepsilon \frac{L^3}{D}L^\varepsilon
 \asymp LD^3L^\varepsilon,
\]

together with an (O(L^2L^\varepsilon)) weighted boundary-collar charge.
Neither bound follows from the involution alone.

## 2. Exact statement and hypotheses

Let (mathcal I) contain incidences from the statement-only packet with
(d,d'>0) odd, (r>0) even, (g=(d,d')), (k=(m,m')=1), and both close
inequalities.  For the sign-reversing assertion impose
(r\equiv2\pmod4).  To use (\tau_g) inside a sum, one must additionally
require:

1. (mathcal I) contains both the plus and minus orientation charts;
2. the literal box/profile domain is (\tau_g)-closed, or has been enlarged
   to a closed union with the amplitudes zero-extended there;
3. the same (P_r(N)) is attached to both members of an orbit, which holds
   because it depends only on (N,N+r,r); and
4. a canonical primitive normalization is specified.

For the displayed plus chart, the needed canonical normalization can be
taken as

\[
 \kappa=(d/g,m'),\qquad
 U=\frac{d/g}{\kappa},\qquad
 v=\frac{m'}{\kappa},
\]

so that ((U,v)=1).  The remaining primitive conditions forced by
((d/g,d'/g)=1) and (k=1) are

\[
 (\kappa U,2S)=1,qquad (\kappa v,2w)=1.
\]

In particular (g,\kappa,U,v) are odd.  Without the cross-gcd definition
of (kappa), the displayed coordinates need not be a unique canonical
description.

For the conditional estimate, write

\[
 B_x=A_{N+r}(d')\overline{A_N(d)}
\]

for an incidence (x), normalize or retain explicitly the weight
(|P_r(N)|), and decompose the two-element (\tau_g)-orbits into common-cell
orbits and boundary-collar orbits.  Assume:

\[
 |B_x-B_{\tau_gx}|\ll \frac DL
 \quad\text{on every common-cell orbit},
\]

the coefficient profiles have uniformly bounded scale-normalized discrete
BV so that no cell-length factor is lost, and each profile has only
(O(1)) literal boundary collars.  These are extra coefficient/support
hypotheses, not consequences of the arithmetic identities.

## 3. Proof and derivation

### Integrality, gcd, parity, and involution

Since (g\mid d,d'), all four coordinates of (\tau_gx) are positive
integers.  Moreover

\[
 (gm,gm')=g(m,m')=g,
 \qquad
 (d/g,d'/g)=1.
\]

Thus the image again has divisor gcd (g) and cofactor gcd (1).  Applying
the same construction twice gives

\[
 \tau_g^2(d,m,d',m')=(d,m,d',m').
\]

Because (d,d') are odd and (r=d'm'-dm) is even, (m,m') have the same
parity.  The condition ((m,m')=1) rules out the even case, so both are
odd.  Hence (gm,gm') are admissible odd divisor variables.

The close conditions are preserved exactly:

\[
 |gm-g(d/g)|=|gm-d|,
 \qquad
 |gm'-g(d'/g)|=|gm'-d'|.
\]

### Products, phase, character sign, and fixed points

The two products are unchanged:

\[
 (gm)(d/g)=dm=N,
 \qquad
 (gm')(d'/g)=d'm'=N+r.
\]

Consequently (r) and (P_r(N)) are unchanged.  On odd integers,
(chi_4) is completely multiplicative.  If

\[
 a=\chi_4(d),\quad b=\chi_4(d'),\quad
 c=\chi_4(m),\quad e=\chi_4(m'),
\]

then (r\equiv2\pmod4) gives (be=-ac).  Therefore

\[
 (ab)(ce)=(ac)(be)=-1,
\]

and, since (chi_4(g)^2=1),

\[
 \chi_4(gm')\chi_4(gm)=ce=-ab
 =-\chi_4(d')\chi_4(d).
\]

There can be no fixed point: a fixed point would equate two nonzero
character products which the same identity says are negatives of one
another.

### Primitive coordinate transport and orientation

The plus coordinates give

\[
 r=d'm'-dm=2\kappa g(Sv-Uw)=2\kappa gh.
\]

Since (r\equiv2\pmod4) and (g,\kappa) are odd, (h) is odd.  As
(U,v) are odd, this also says that (S) and (w) have opposite parity.

Under (\tau_g),

\[
 \widetilde d=g(\kappa v+2w),\quad
 \widetilde d'=g\kappa v,\quad
 \widetilde m=\kappa U,\quad
 \widetilde m'=\kappa U+2S.
\]

This is not another plus chart with all auxiliary variables positive:
the divisor ordering and cofactor ordering have both reversed.  In the
minus chart put

\[
 (\widetilde U,\widetilde S,
   \widetilde v,\widetilde w)=(v,w,U,S).
\]

Then

\[
 \widetilde d'=\kappa g\widetilde U,\quad
 \widetilde d=g(\kappa\widetilde U+2\widetilde S),\quad
 \widetilde m=\kappa\widetilde v,\quad
 \widetilde m'=\kappa\widetilde v+2\widetilde w,
\]

and the positive minus determinant is

\[
 \widetilde U\widetilde w-\widetilde S\widetilde v
 =vS-wU=h.
\]

The cross-gcd normalization is preserved because

\[
 (\widetilde d'/g,\widetilde m)=(m',d/g)=\kappa.
\]

The two primitive coprimality relations are merely interchanged.  An
orientation tag and the cross-gcd rule are therefore essential for a
canonical primitive involution.

### Exact close count, floors, and determinant range

Since (U,v) are odd, put (j=(U-v)/2\in\mathbb Z).  Direct substitution
gives

\[
 d-gm=2g(\kappa j-w),
 \qquad
 d'-gm'=2g(\kappa j+S).
\]

The two close inequalities are therefore exactly

\[
 |\kappa j-w|\le F_g,qquad
 |\kappa j+S|\le F_g,qquad
 F_g=\left\lfloor\frac D{2g}\right\rfloor.
\]

If (F_g=0), positivity of (S,w) makes the system empty.  If
(F_g\ge1), write (x=\kappa j).  Positivity gives

\[
 -F_g+1\le x\le F_g-1,qquad v=U-2j>0.
\]

For fixed (j), the exact intervals are

\[
 1\le w\le F_g+x,qquad
 1\le S\le F_g-x,
\]

which proves the count in Section 1.  It also gives the sharp close-only
consequences

\[
 S+w\le2F_g,qquad
 |U-v|\le2\left\lfloor\frac{F_g-1}{\kappa}\right\rfloor.
\]

The asymmetric truncation
(K=\min(J,(U-1)/2)) is required when (U) is small.  In particular, the
negative-(j) side remains present even when (D\ge U); discarding it by
assuming (D<U) would be invalid.

There is also an exact determinant bound.  Since (r) is an integer and
(0<r<\lceil L\rceil),

\[
 0<r<L,qquad
 1\le h\le
 H_{g,\kappa}:=
 \left\lfloor\frac{\lceil L\rceil-1}{2\kappa g}\right\rfloor.
\]

For completeness, the strongest count after imposing this (h)-window,
but before coprimality, box, support, and (h)-parity deletions, is

\[
 \sum_{j=-J}^{K}\ \sum_{S=1}^{F_g-\kappa j}
 \left[
 \min\left\{F_g+\kappa j,
       \left\lfloor\frac{S(U-2j)-1}{U}\right\rfloor\right\}
 -\max\left\{1,
       \left\lceil\frac{S(U-2j)-H_{g,\kappa}}{U}\right\rceil\right\}
 +1
 \right]_+.
\]

The opposing condition further retains only odd
(h=S(U-2j)-Uw).  All primitive coprimalities and literal boxes can only
decrease these counts.

Neither (k=1) nor (r\equiv2\pmod4) enters the raw close-inequality
count as a density input.  The condition (k=1) is needed for oddness,
primitive admissibility, preservation of the same gcd (g), and
(\tau_g^2=1) under canonical recomputation.  The congruence
(r\equiv2\pmod4) is needed for character sign reversal.  If parity and
the displayed coordinates are supplied separately, removing either
condition does not strengthen the close count; the corresponding gcd or
congruence restriction merely deletes rows.

### Coefficient no-go and the conditional multiplicity ledger

Choose one representative (x) of a two-element orbit.  Its paired
contribution is exactly

\[
 \chi_4(d')\chi_4(d)P_r(N)
 \left[
 A_{N+r}(d')\overline{A_N(d)}
 -A_{N+r}(gm')\overline{A_N(gm)}
 \right].
\]

For abstract bounded arrays the bracket is arbitrary.  For example, one
may support an array on one member of an orbit and set it to zero on the
other.  Thus sign reversal alone proves no cancellation, density bound,
or nontrivial estimate.

Under the explicit common-cell hypotheses of Section 2, define weighted
orbit multiplicities

\[
 \mathfrak M_{\rm cell}
 =\sum_{\mathcal O\ {\rm common\ cell}}|P_r(N)|,
\]

and let (\mathfrak B) be the total weighted discrete-BV charge of the
finitely many boundary collars.  Pairwise summation gives the exact ledger

\[
 |\Sigma|
 \ll \frac DL\mathfrak M_{\rm cell}+\mathfrak B.
\]

Consequently the triangle/BV mechanism yields
(O(L^2L^\varepsilon)) provided

\[
 \boxed{
 \mathfrak M_{\rm cell}\ll_\varepsilon
       \frac{L^3}{D}L^\varepsilon,qquad
 \mathfrak B\ll_\varepsilon L^2L^\varepsilon.}
\]

Because (D=\lceil L^{1/2}\rceil), the first scale is equivalently
(LD^3L^\varepsilon), up to an absolute constant.  If every boundary
orbit also satisfies the common-cell (O(D/L)) difference, it may instead
be included in the first multiplicity.  The packet does not supply the
global base-variable, weight, or collar ledger needed to prove these
bounds.

## 4. First doubtful or unproved step

The first unproved analytic step is not an identity: it is the assertion
that the literal (\tau_g)-partners lie in a common support cell and that
their actual coefficient products differ by (O(D/L)).  Zero extension
makes both products well-defined, but it does not make them close; a
partner can cross a box edge, an arithmetic mask, or a support boundary.

Even after imposing common-cell closeness and scale-normalized BV, the
packet does not prove the weighted multiplicity
(\mathfrak M_{\rm cell}\ll L^3D^{-1}L^\varepsilon) or the boundary charge
(\mathfrak B\ll L^2L^\varepsilon).  This is the first place where a
literal coefficient/support theorem and a complete summation ledger are
needed.  No parent estimate follows before those seams are closed.

## 5. Required control test and outcome

A bounded exact enumeration was performed using only the statement-only
definitions.

- For (0\le F_g\le8), odd (1\le\kappa\le7), and odd
  (1\le U\le9), 180 parameter cases were enumerated.  Direct counting of
  positive odd (v) and positive (S,w) agreed with the closed formula in
  all 180 cases; failures: 0.  This includes (F_g=0,1), (U=1), and
  (F_g\ge U) cases.
- For odd (d,d'\le15) and positive (m,m'\le15), all 784 cases with
  (k=1), (r>0), and (r\equiv2\pmod4) passed product preservation,
  gcd preservation, oddness, (\tau_g^2=1), and character sign reversal;
  failures: 0.

Three hand controls separate the hypotheses:

1. With (L=10,D=4),
   ((d,m,d',m')=(1,3,5,1)) has (r=2) and maps to
   ((3,1,1,5)); products and phase are fixed and the character product
   changes sign.
2. ((d,m,d',m')=(1,5,3,3)) has (k=1,r=4) and satisfies the same
   close-count algebra, but its character product does not change sign.
   Thus (r\equiv2\pmod4) is unnecessary for the count and necessary for
   antisymmetry.
3. With (L=50,D=8), ((1,9,5,3)) has (k=3,r=6) and satisfies the
   close inequalities.  It is counted by the raw lattice formula, but the
   transformed divisor gcd is (3g), so canonical involutivity with the
   same (g) fails.  Thus (k=1) is structural for the involution, not a
   source of the close-count bound.

These finite checks can falsify signs, floors, small-variable truncation,
and the count, but they are diagnostic only and cannot prove an asymptotic
estimate.

## 6. Dependencies and exact artifacts used

The only files consulted were:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/blind_statement.md`.

This is not a pristine fresh-context blind run because I previously
performed a through-Round-192 proof-status audit.  That audit was completed
before the Round-193 launch, and I received no Round-193 claimant strategy,
report, candidate, review, control, kernel, source, graph, or campaign
content.  The derivation and finite controls above use only the two listed
artifacts and the self-contained definitions in the blind packet.

## 7. Recommended state effect

**Retain for seam validation; no automatic graph change.**  The exact
integrality/gcd/parity identities, fixed-point-free orientation-reversing
involution, product/phase invariance, character antisymmetry, primitive
coordinate swap, determinant bound, and close-lattice count are suitable
as a candidate finite kernel once the conductor independently checks the
canonical cross-gcd and two-orientation conventions.

Do not promote any cancellation or asymptotic parent.  The abstract-array
no-go should be retained, and any analytic promotion must separately prove
literal support closure, the (O(D/L)) common-cell coefficient difference,
the scale-normalized BV/collar hypotheses, and the two multiplicity bounds
in Section 3.
