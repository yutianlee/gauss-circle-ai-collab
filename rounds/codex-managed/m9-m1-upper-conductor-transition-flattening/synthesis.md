# Round 81 synthesis

## Objective and outcome

Round 81 asked whether the neighbor-dependent Farey transition could be
removed from the Abel weight without deleting the exact moving boundary.
The answer is yes, after a necessary distinction:

- the neighbor-independent critical coefficient is globally BV;
- the exact incomplete-Gaussian transition is only pointwise small and
  can have large total variation.

This distinction extends the accepted fixed-interior M1 conductor range
from \(C\le J^{32/45}\) to

\[
 C\le J^{13/18}.
\]

## Exact result

For every fixed nonaxial critical component, parity class, alias,
orientation, numerator, and admissible progression,

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),
\]

with

\[
 \|V\|_\infty+\operatorname {Var}V
 \ll_\varepsilon X^\varepsilon,qquad
 |E(c)|\ll_\varepsilon X^\varepsilon\sqrt{C/J}.
\]

The proof uses the exact phase identity

\[
 \phi(z,u,v)=-z-{\kappa\rho\sigma\over z}
             +z\left(u-{\kappa\sigma\over z}\right)
                \left(v-{\rho\over z}\right),
\]

followed by tangential stationary phase and an exact one-dimensional Morse
coordinate.  The first omitted tangential and Morse terms are explicitly
inside \(E\).  At a boundary saddle the adjacent Farey face has
standardized displacement \(O(\sqrt{C/J})\); the remote face is at
distance \(\asymp\sqrt{J/C}\) and contributes the same size through its
oscillatory tail.

## Sawtooth and energy

The exact fixed-residue neighbor sawtooth has about \(J/C\) resets, each
of standardized size \(\sqrt{C/J}\).  Its raw variation can therefore be
\(\sqrt{J/C}\), and simultaneous left/right reset cancellation is absent.
This falsifies the raw-BV route.  It does not affect the proof because the
sawtooth belongs to \(E\).

Bourgain's audited exponent pair gives a proper-subinterval reciprocal
sum of size \(TQ^{-5/24}X^\varepsilon\).  One global Abel summation for
\(V\), plus triangle summation for \(E\), yields

\[
 \sum_{b\asymp C/T}|S_b|^2
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{C^4\over TJ}\right).
\]

The two terms are safe through \(J^{13/18}\) and \(J^{3/4}\),
respectively, so \(J^{13/18}\) is the binding range.

## Remaining M1 corridor

The fixed-interior residual is now

\[
 J^{13/18}<C\le J.
\]

It naturally splits at \(J^{3/4}\): below that point only the smooth
nonaxial main energy is open; above it the transition error and axes also
need cancellation.  Cone edges and other radial sectors remain separately
owned.

## State decision

Promote the scoped transition-flattening lemma, its external source audit,
and the range extension.  Reject raw transition BV, cellwise Bourgain with
no piece cost, the two-small-faces assertion, and simultaneous-switch
cancellation.

Keep full `M9-M1`, `M9-M2`, `M9`, endpoint uniformity, `R5-Full`, and the
Gauss-circle target open.  No global exponent has changed.

