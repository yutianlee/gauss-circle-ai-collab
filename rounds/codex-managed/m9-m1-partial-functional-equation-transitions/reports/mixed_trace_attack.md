# Mixed one-factor transition attack

## 1. Result

Both one-factor reductions are exact, but neither transition is closed by
the proposed elementary mechanism.  On the \(\beta\)-bounded trace the
low zeta functional equation can be undone, leaving one high
\(\chi_4\)-factor.  Its physical degree-one kernel is a sine kernel; at
accessible odd-integer frequencies it cancels \(\chi_4\) rather than
benefiting from it.  Uniform fixed-profile sampled BV therefore fails.

On the \(\alpha\)-bounded trace, undoing the low character factor leaves a
high zeta cosine kernel.  After the already-ledgered pole share is removed,
Euler summation represents the remainder using a bounded periodic
function, but with a factor of the high Mellin variable.  Integer
frequencies give coherent cosine sums.  Thus no bounded-partial-sum gain
survives the top Hilbert limit.

## 2. Exact statement and hypotheses

Put
\[
 r_-=s-\frac z2,\qquad r_+=s+\frac z2,\qquad z=u+v,
\]
so \(\Im r_-=\beta\), \(\Im r_+=\alpha\). Define
\[
 X_\zeta(r)=\pi^{1/2-r}
 \frac{\Gamma(r/2)}{\Gamma((1-r)/2)},\qquad
 X_\chi(r)=\left(\frac4\pi\right)^{r-1/2}
 \frac{\Gamma((r+1)/2)}{\Gamma((2-r)/2)}. \tag{1}
\]
Then the exact terminal arithmetic factor is
\[
 K_z(1-s)F_{-z}(s)
 =X_\zeta(r_-)\zeta(r_-)\,
 X_\chi(r_+)L(r_+,\chi_4). \tag{2}
\]
Use finite \(u,v,s\) segments, fixed smooth trace cutoffs
\(\Theta_\beta(\beta)\), \(\Theta_\alpha(\alpha)\), and the accepted
endpoint-renormalized radial factor \(\mathcal G_v^{\rm ren}(1-s)\).
All outside horizontal segments and axial residues remain in their
finite ledger.  The closed physical endpoints and \(R_1\) arithmetic
residue are not inserted again.

## 3. Proof, two mixed formulas, and obstruction

The component functional equations are
\[
 X_\zeta(r)\zeta(r)=\zeta(1-r),\qquad
 X_\chi(r)L(r,\chi_4)=L(1-r,\chi_4). \tag{3}
\]
Therefore the two finite mixed traces are exactly
\[
\boxed{\begin{aligned}
\mathfrak T_{\chi{\rm -high}}
={}&\sum_j\frac1{(2\pi i)^3}\iiint
\Theta_\beta\,\mathcal A_j(u,v)\mathcal G_v^{\rm ren}(1-s)\\
&\quad\times\zeta(1-r_-)\,
X_\chi(r_+)L(r_+,\chi_4)\,ds\,dv\,du ,
\end{aligned}} \tag{4}
\]
and
\[
\boxed{\begin{aligned}
\mathfrak T_{\zeta{\rm -high}}
={}&\sum_j\frac1{(2\pi i)^3}\iiint
\Theta_\alpha\,\mathcal A_j(u,v)\mathcal G_v^{\rm ren}(1-s)\\
&\quad\times L(1-r_+,\chi_4)\,
X_\zeta(r_-)\zeta(r_-)\,ds\,dv\,du .
\end{aligned}} \tag{5}
\]
These are meromorphic identities on the original finite contours; they
cross no new pole.

Duplication and reflection give the exact inverse Mellin kernels
\[
 \frac1{2\pi i}\int X_\chi(r)Y^{-r}\,dr
 =\sin\frac{\pi Y}{2},\qquad
 \frac1{2\pi i}\int X_\zeta(r)Y^{-r}\,dr
 =2\cos(2\pi Y), \tag{6}
\]
initially in their fundamental strips and thereafter by continuation
against the compact physical profiles. Thus expanding the high factor in
(4) produces a one-dimensional kernel
\[
 \sum_{q\ge1}\chi_4(q)b(q)
 \sin\!\left(\frac{\pi qY}{2}\right). \tag{7}
\]
The remaining spatial inversion makes a fixed multiplicative convolution
of (7), but the one-sided top jump retains its boundary sine term.
For every odd integer \(Y\),
\[
 \chi_4(q)\sin(\pi qY/2)=\pm1\qquad(q\ {\rm odd}). \tag{8}
\]
Such frequencies occur in the physical radial range: on the top scale,
the unsmoothed argument \(Y=2\sqrt X\sqrt x/D_0\) attains any fixed odd
\(Y\ge3\) at
\(x=(YD_0/(2\sqrt X))^2\in[1,N_X]\). Hence character partial sums in
(7) can have full block length. Equivalently, including the sine in the
sampled amplitude gives variation of full block capacity, not the
inverse-support-length variation used in Rounds 23--24. This refutes the
uniform character-Abel lemma; it is not a lower bound for the fully
integrated signed trace.

For (5), split before shifting
\[
 \zeta(r)=\frac1{r-1}+\zeta^\circ(r). \tag{9}
\]
The first term, together with the zero of \(X_\zeta\) at \(r=1\), is the
finite pole share and must be assigned to the existing zeta-residue
ledger; it is not a second residue. For \(\Re r>0\), exactly
\[
 \zeta^\circ(r)=\frac12-r\int_1^\infty
 \bigl(\{y\}-\tfrac12\bigr)y^{-r-1}\,dy . \tag{10}
\]
The integrand in (10) is bounded, but the prefactor \(r\) restores the
high-height loss. The physical kernel from (6) contains
\(\sum_n c(n)\cos(2\pi nY)\); at integral \(Y\) its partial sums are
coherent. The eta identity merely moves this obstruction into
\((1-2^{1-r})^{-1}\) and a dyadic difference; it creates no uniform
height decay.

Finally, partial reduction does not improve the accepted raw top
capacity. On \(|\beta|\le B\), truncation at high height \(U\) has
absolute capacity
\[
 U^{\,c'-1/2+\zeta/2}, \tag{11}
\]
while on \(|\alpha|\le B\) the pole-subtracted branch has
\[
 U^{\,c'-1/2-\zeta/2}. \tag{12}
\]
These follow from the one-large gamma powers
\(c'-1/2\pm\zeta/2\), the top \(1/u\), and integration in the remaining
high variable. Since \(c'>1+\zeta/2\), both grow polynomially. Equations
(8) and (10) show why the suggested Abel representations do not supply
the missing inverse power.

## 4. First doubtful or unproved step

The first open step is a joint estimate using the radial \(x\)-integration,
the multiplicative spatial convolution, and the symmetric top Hilbert
transform across the resonant sets in (8) and the integer cosine sets.
Neither coefficientwise Abel summation nor pole subtraction controls this
coupled operator.

## 5. Required control test and outcome

At bounded \(r_-\), (4) has high character, not high zeta; at bounded
\(r_+\), (5) has high zeta.  This orientation check passes.  At \(Y=1\),
(8) becomes \(\chi_4(q)^2=1\) on odd \(q\), exactly falsifying a uniform
period-four saving. At integral \(Y\), the zeta cosine kernel is constant.
The pole term in (9), endpoints, \(R_1\), and radial sides are each counted
once. No numerical or external theorem was used.

## 6. Dependencies and exact artifacts used

Used only the protocol, proof graph, active campaign, Round-19--21 and
Round-24 syntheses, and the assigned Round-25 brief. No other Round-25
report or web source was read.

## 7. Recommended state effect

Promote (1)--(6), the exact branch orientation, and the scoped resonance
obstructions (8)--(12). Retain as the smallest survivor the sum of the
pole-reconciled mixed operators (4)--(5), restricted to their resonant
physical kernels and coupled to the symmetric top Hilbert transform.
Do not promote either trace estimate, the full post-FE vector kernel, GAR,
M9-M1, M9-M2, M9, or the target.
