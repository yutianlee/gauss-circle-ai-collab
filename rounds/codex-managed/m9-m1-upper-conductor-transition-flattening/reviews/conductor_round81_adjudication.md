# Round 81 conductor adjudication

Campaign: `m9-m1-upper-conductor-transition-flattening`
Round: 81
Starting graph SHA-256:
`f69da71546e5a6fd1d48c7fa561e17b62ce6669fb4a29c497f74f748e7379635`

## Decision

Promote the complete-symbol transition-flattening lemma and the resulting
fixed-interior conductor extension

\[
 T\le C\le J^{13/18}.
\]

The three independent reports and the conductor normalization review agree
on the exact finite antecedent, stationary constants and remainders,
moving Farey faces, hostile sawtooth, source range, and energy arithmetic.
No numerical experiment is used.

The promotion is scoped.  The remaining M1 fixed-interior range is

\[
 J^{13/18}<C\le J.
\]

For \(J^{13/18}<C\le J^{3/4}\), the pointwise transition error and the
axes remain target-safe, so only the globally smooth nonaxial main energy
is missing.  For \(J^{3/4}<C\le J\), the main, transition error, and axes
all require a new signed argument.  Cone edges, other radial sectors, full
\(M9\!-\!M1\), \(M9\!-\!M2\), \(M9\), and the global exponent remain
open.

## Promoted lemma

Fix a smooth interior one-sided ratio block, an endpoint orientation, an
offset-Poisson alias, \(\kappa\in\{1/4,1/2,1\}\), a compatible nonaxial
pair \((\rho,\sigma)\), \(b\asymp C/T\), and an admissible progression
\(c=r\pmod {4b}\).  Put \(\Lambda=J/c\) and
\(z_*^2=\kappa\rho\sigma\).  The exact normalized coefficient is

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),
\]

where \(\Gamma\) is the full Gaussian for \(-1<z_*<1\), the correctly
oriented half Gaussian for \(z_*=\pm1\), and zero for \(|z_*|>1\), and

\[
 \|V\|_\infty+\operatorname {Var}V
 \ll_\varepsilon X^\varepsilon,qquad
 |E(c)|\ll_\varepsilon X^\varepsilon\sqrt{C/J}.  \tag{81.A}
\]

The error contains both exact Farey-face displacements, the complete
tangential stationary correction, the one-dimensional Morse correction,
nonstationary pieces, floors, aliases, and every neighbor reset.  It is not
asserted to have bounded variation.

Using Bourgain's audited reciprocal exponent pair and proper-subinterval
uniformity gives

\[
 \sum_{b\asymp C/T}|S_b|^2
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{C^4\over TJ}\right)
 \le X^\varepsilon{J^2\over T}
\]

for \(C\le J^{13/18}\).  Together with the accepted low-conductor and
third-derivative blocks, every fixed-smooth-interior conductor
\(T\le C\le J^{13/18}\) is target-safe.

## Blind-gate reconciliation

The blind task first rejected the packet because it did not define the
complete finite coefficient or a quantitative amplitude class.  The
conductor then supplied the exact-integral addendum (81.A1)--(81.A3),
extracted from the accepted Round 71 finite Farey identity.  The blind
agent rederived the result without reading claimant reports and changed
its verdict to promote.  This is a valid repaired statement-only gate;
the superseded countermodel is excluded precisely by the now-explicit
neighbor-independent amplitude and integrated \(c\)-seminorm.

## Rejected shortcuts

The following stronger claims are false or unlawful.

1. The raw incomplete-Gaussian transition has
   \(O(X^\varepsilon)\) total variation across a progression.
2. One may apply Bourgain separately on every Farey-neighbor cell without
   paying a cell-count loss.
3. At a boundary saddle both standardized Farey faces are
   \(O(\Lambda^{-1/2})\).
4. Simultaneous left/right neighbor switches cancel the boundary
   sawtooth.

The valid proof instead separates a globally BV principal symbol from a
pointwise-small transition remainder and uses the remote-face oscillatory
tail.

## State decision

Create one audited external source node for Bourgain's reciprocal
exponent-pair interface and one proved internal node for the transition-
flattened subrange.  Add the latter to the M1 dependency chain and narrow
the residual upper-conductor reduction to \(J^{13/18}<C\le J\).

Keep the status of `M9-M1`, `M9-M2`, `M9`, and `GC-target` unchanged.
This is genuine local range progress, not a global exponent improvement.
