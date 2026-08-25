# Round 147 synthesis

Round 147 closes under

\[
\boxed{\mathsf{squarefree\_H\_resonance\_no\_go}.}
\]

The round does not prove the separate \(t=1\) target. It proves the
exact fixed-parameter interface and localizes the next two genuine
seams.

For squarefree \(s=2^\nu n\), \(n\) odd,

\[
C(2^\nu n)=
\sum_{\substack{e\mid n\\e>2^{1+\nu/2}\sqrt n}}\chi_4(e).
\]

Divisor pairing retains the complete positive-total-character sector
and a mandatory antisymmetric negative-total-character tail. A
target-safe \(\sqrt D\) cone collar gives smooth ratio bandwidth
\(D^{1/2}X^\varepsilon\). Including a local \(d\asymp D\) partition
puts the complete coefficient on the exact unitary order
\(z=i(\tau+t/2)\), with the required radial twist and external
constants; the hard Perron zero mode remains explicit.

The squarefree coefficient factors as

\[
B_z=h_z*A_z,\qquad
\sum_n A_z(n)n^{-w}=\zeta(w+z)L(w-z,\chi_4).
\]

The Euler correction has exact two-adic and odd factors, is supported
on powerful integers, and refactors as

\[
H(w,z)=
\frac{\mathscr K(w,z)}
{\zeta(2w+2z)\zeta(2w-2z)L(2w,\chi_4)},
\]

where the corrected mixed-monomial identity proves
\(\mathscr K\) absolutely convergent for
\(\Re w>(1+|\Re z|)/3\). The reciprocal factors still carry
unowned zero poles, so this is not a free contour shift.

For every fixed order, the conductor-four compact-smooth Voronoi
identity has scalar \(\pi4^z\), one pole, the reflected coefficient,
and all \(J/Y/K\) branches. In the physical finite \(H\)-convolution,
only \(k\le K_F=O(M)\) occurs. The fixed-order resonance is

\[
m=kN+O\!\left(k\sqrt{N/M}\right),
\]

with raw one-term size \(M^{3/4}/(kR)\).

Even granting the missing uniform-order estimate, absolute
channelwise optimization gives physical loss

\[
\begin{cases}
M^{1/4},&M\le R^{4/3},\\
R^{1/2}M^{-1/8},&R^{4/3}\le M\le R^2.
\end{cases}
\]

It is \(R^{1/3}\) at the intermediate crossover and \(R^{1/4}\) at
the top. Separately, the exact bare reciprocal average has size
\(Q+D\), but expanding \(\mu^2\) under triangle gives only
\(QD^{1/2}+D\). Both are method limitations, not signed lower bounds.

The first open analytic seam is uniform growing-order and
moving-prefix control of every Bessel regime. Granting it, the first
open arithmetic seam is signed aggregation of

\[
h_z(k)A_{-z}(kN+j),
\qquad k\le K_F,\qquad
|j|\lesssim k\sqrt{N/M},
\]

over the actual cone orders, or an equivalent squarefree/coprime
strengthening of the bare reciprocal lemma.

A separate \(t=1\) estimate is sufficient for a layerwise route but
not necessary for a route exploiting cross-\(t\) cancellation. The
independent Round-138 owner and all \(t\ge2\) layers remain open.

There is no change to M9-M1, M9-M2, endpoint uniformity, M9, the
bridge, or the quarter target. The internally proved exponent remains
\(1/3\); the separately audited external exponent remains

\[
\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots.
\]

