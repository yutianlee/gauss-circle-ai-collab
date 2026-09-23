# Conductor Round-195 adjudication

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Starting graph SHA-256: 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89
- Terminal candidate SHA-256: 81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72
- Durable kernel SHA-256: 4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009

## 1. Decision

Round 195 does not prove complete \(P_2\).  It proves and promotes only two
absolute-capacity sectors inside the exact accepted Round-192 core:

1. every physical \(P_2\) atom with \(\kappa\ge D_L\), where
   \(D_L=\lceil\sqrt L\rceil\);
2. every fixed packet with \(\kappa<D_L\) and
   \(\min(Y,D_L)\le H_B\mathfrak m\kappa\).

For the physical large-\(\kappa\) sector,

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D}W)|
 \ll H_B\mathfrak m\kappa uX^\varepsilon,
\qquad
 |\mathscr R_{{\rm core},Y,H_B}^\sigma(P_{2,\ge D}W)|
 \ll L^2X^\varepsilon.
\]

For the small-\(\kappa\) physical complement, the exact positive estimate is

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\]

It proves the second safe packet sector and, through the accepted lift and
divisor ledger, an outer \(O(L^2X^\varepsilon)\) bound for the union of the
two safe sectors.

The exact remaining \(P_2\) packet region is

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

This region remains open.

## 2. Proof selection

The large-\(\kappa\) proof is absolute.  Lower closeness gives \(g=O(1)\).
In the plus chart it gives \(O(D_L)\) values of \(w\), while the determinant
window gives \(O(1)\) values of \(S\); the minus chart transposes these
roles.  Thus

\[
 \sum_{\kappa\ge D_L}D_L(1+L/\kappa)^2
 \ll L^2+LD_L\log(2L)\ll L^2.
\]

At fixed packet there are \(O(D_L)\) atoms per literal row, \(O(uJ/q)\)
rows, and the exact anchor/Abel factor \(q/J\), giving \(O(D_Lu)\).
Terminal and Fejer pieces cost \(O(\kappa u)\).

For \(\kappa<D_L\), lower closeness leaves \(O(1)\) sites per fixed height
and row, giving \(Yu\); the all-height determinant count gives \(D_Lu\).
Taking the minimum and restoring terminal/Fejer gives the displayed
\(u\{\kappa+\min(Y,D_L)\}\) bound.

The physical mask is always imposed before Fourier expansion or height
differencing.  Its transported commutator, births, deaths, carries,
endpoint changes, phases, cells, crossings, and zero extensions remain in
the recomputed core.  The accepted Round-187--192 safe projectors are
deletion-stable when rerun on that physical input.

## 3. Method boundary

For a fixed primitive row the far-defect parity step changes height by
\(v\) or \(U\), comparable with the live height scale, so the row contains
only \(O(1)\) far samples.  The minus retained-mode anchor ratio is one.
The plus retained-mode ratio is

\[
 (-1)^{c_+(h;v)}e(a/q),
\]

with carry \(c_+(h;v)\in\{0,1\}\); the full physical parity flip belongs
only to the recombined pre-Fourier sum.

Same-site current and previous event channels have equal-phase
\(2\times2\) and \(3\times3\) blocks.  Correct signed recombination returns
the original masked jump.  Orthogonalizing event labels merely postpones
the same all-ones summation cost.  A future estimate must control the
actual \(++,+-,-+,--\) cross-row Gram with endpoint products,
square-root phases, Fejer factors, residual masks, carries, births/deaths,
mask commutators, and zero extensions intact.

On nonzero support, \(\kappa gU\) is squarefree, so \(U\) is squarefree and
the minus quadratic congruence has only \(U^\varepsilon\) roots for fixed
\((\kappa,U,h,\delta)\).  This removes the blind squareful false shadow but
does not price the anchor denominator or the actual coefficient Gram.

No capacity is asserted to be literal lower mass, and the open region is
not disproved.

## 4. Review disposition

The terminal candidate and kernel passed independent count/power/operator,
literal Gram/no-go, blind post-unmask, packet-notation, candidate-kernel
consistency, provenance, owner-scope, and exponent-quarantine reviews.
The blind \(U=p^2\) family is rejected as live evidence: it violates
\(u=gU\), the height block, the hard-shell connector, squarefree nonzero
support, and the target normalization.  Its bounded-array construction is
retained only as a mechanism falsifier.

The durable kernel is
proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md.

## 5. Graph and downstream scope

Create one subordinate proved-internal node depending directly on
M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector.  Add it only as
strict-sector evidence to the already-open hard-M1 high-radical small-\(t\)
owner.  Complete \(P_2\), \(P_1\), complete original \(t=1\), every
original \(t\ge2\) range, the large-\(G\) near-resonant complement, smooth
M1, GAR, all M2 owners, endpoint uniformity, M9, both bridges, and the
Gauss-circle target remain open or conditional exactly as before.

The internal exponent remains \(1/3\), the accepted external benchmark
remains \(0.3144831759740614\ldots\), and the target remains \(1/4\).

Round 195 closes under terminal label
strict_p2_absolute_capacity_sectors, subject to a mechanically valid State
Patch, reverse replay, and protected-state audit.

