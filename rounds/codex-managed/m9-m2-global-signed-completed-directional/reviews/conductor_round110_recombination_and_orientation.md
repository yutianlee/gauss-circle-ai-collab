# Conductor review: completed real-part self-return and orientation

Campaign: m9-m2-global-signed-completed-directional

Starting graph SHA-256:
33bf8e043cb8a1e0852b7f98941ee6186f798ed40124525de3d0373269019397

## Certified finite object

The object certified without any new merger convention is the tagged finite
sum

\[
 \mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 =\sum_{B=(A,D,K,G,R)}\mathfrak Q_B^{\mathrm{comp}}.
\tag{110.C6}
\]

Every tag keeps its inherited half-open scale cell, fixed \(k\)-lattice,
open reciprocal interval, terminal metric member, exact-centre atom,
collar, floor, star, equality convention, and entry/exit data. Finiteness
allows reordering, but does not identify two atoms or replace their
block-dependent coefficient by a new scale-free symbol.

The formalizer's displayed formula (2.10) is useful notation for this tagged
sum only when all omitted owner and transform tags are understood as part of
the inherited atom dictionary. It is not promoted as a separate untagged
kernel formula.

## Exact physical comparison

Round 109 and the accepted energy identity give

\[
 \mathcal E_L^{\mathrm{top}}
 =\widetilde{\mathcal E}_{\mathrm{owned},L}
  +2\Re\mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}},
 \qquad
 |\widetilde{\mathcal E}_{\mathrm{owned},L}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{110.C7}
\]

The original Round-75 row expansion is

\[
 \mathcal E_L^{\mathrm{top}}
 =\mathcal D_L+2\Re\mathfrak C_L^{\mathrm{off}},
 \qquad
 \mathcal D_L\ll_\varepsilon L^2X^\varepsilon.
\tag{110.C8}
\]

Subtracting these two accepted identities proves, without relying on a
simplified merged formula,

\[
 \boxed{
 \Re\!\left(
 \mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 -\mathfrak C_L^{\mathrm{off}}
 \right)
 ={\mathcal D_L-\widetilde{\mathcal E}_{\mathrm{owned},L}\over2}
 =O_\varepsilon(L^2X^\varepsilon).}
\tag{110.C9}
\]

This is a real-part identity. Neither accepted energy formula controls the
imaginary part of the difference, so no complex equality or modulus bound
is certified.

## Minimal target

From (110.C7), the hard energy upper bound is equivalent, up to changed
constants, to

\[
 \Re\mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 \ll_\varepsilon L^2X^\varepsilon.
\tag{110.C10}
\]

Positivity of \(\mathcal E_L^{\mathrm{top}}\) supplies the lower real-part
bound automatically. Hence the one-sided real-part estimate is the minimal
physical scalar target. Complex modulus, blockwise absolute mass, row
energy, and a fixed-\(a\) Gram are strictly stronger and require separate
bridges.

Equation (110.C9) also shows that (110.C10) is equivalent to the original
Round-75 one-orientation off-diagonal estimate. Global completion has not
created a lower-capacity object.

## Orientation correction

The exact convention is one representative orientation \(h<s\), or
equivalently \(a<b\), followed by one outer \(2\Re\). The stale graph phrase
"both conjugate orientations, and one outer \(2\Re\)" double counts the
off-diagonal and must be replaced. The diagonal remains separate.

## Smallest live presentation

Writing \(s=h+2r\) gives

\[
 \chi_4(h)\chi_4(h+2r)=(-1)^r.
\]

Equivalently, with the literal zero-extended moving row \(F_{L,a}(q)\),

\[
 \mathfrak C_L^{\mathrm{off}}
 =\sum_{a,r}\bigl(F_{L,a}(2r)-F_{L,a}(2r+1)\bigr).
\tag{110.C11}
\]

This is an exact signed reindexing, not an estimate. Shifting \(q\) changes
coprimality, lift support, ceilings, reciprocal intervals, collars,
entry/exit profiles, and metric centres. No accepted bounded-variation or
adjacent-ray theorem controls those simultaneous changes.

## Decision

Promote only (110.C7)--(110.C11) as an exact connector/obstruction. Retain
the one-sided estimate open. Reject a complex self-return, a strictly
smaller completed kernel, automatic character orthogonality at fixed
\(q\), and any implication to blockwise absolute or Gram norms. No hard
cone, smooth packet, M9 component, endpoint theorem, or exponent changes.

