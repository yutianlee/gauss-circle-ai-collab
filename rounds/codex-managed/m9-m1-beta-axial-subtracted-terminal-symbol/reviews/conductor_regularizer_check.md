# Conductor check: axial regularizer and fixed-height derivative

Campaign: m9-m1-beta-axial-subtracted-terminal-symbol  
Role: exact algebra seam  
Allocation: analytical/algebraic only

Let \(y=L-\nu\), \(A=A(L)\), and \(D=A+iy/2\). After the signed top
limit, subtract the diagonal constant numerator \(H_0=H(L,L)\). The
ordinary remainder is

\[
 \mathcal R_A[H]=-\frac{iH_0}{2AD}
 +\frac{H(L,\nu)-H_0}{yD}.                         \tag{C39.5}
\]

This follows exactly from

\[
 \frac1y\left(\frac1D-\frac1A\right)=-\frac{i}{2AD}.
\]

At fixed physical \(\nu\), the beta-slab relations give

\[
 A'=-i,\qquad y'=1,\qquad D'=-\frac i2,
 \qquad H_0'=(\partial_L+\partial_\nu)H(L,L).
\]

Termwise differentiation therefore yields

\[
\begin{aligned}
 \partial_L\mathcal R_A[H]={}&
 -\frac{iH_0'}{2AD}+\frac{H_0}{2A^2D}+\frac{H_0}{4AD^2}\\
 &+\frac{\partial_LH(L,\nu)-H_0'}{yD}
 -\frac{H(L,\nu)-H_0}{y^2D}
 +\frac{i\{H(L,\nu)-H_0\}}{2yD^2}.               \tag{C39.6}
\end{aligned}
\]

The signs and coefficients agree with the blind identity. Taylor
expansion at \(y=0\) cancels each apparent singularity. The nontrivial
translation term is

\[
 \frac{\partial_LH(L,\nu)-H_0'}y
 -\frac{H(L,\nu)-H_0}{y^2},                        \tag{C39.7}
\]

which is a second divided difference. This calculation certifies the
algebra only. It gives no uniform bound for the complete actual numerator
through entry/exit, moving faces, or the common artificial germ.

One normalization caveat remains for an aggregate formula: the original
three contour measures, beta-slab Jacobian, and the signed top distribution
leave fixed \(2\pi\)-constants in the residual \((\beta,\nu)\) density.
They must be displayed or absorbed into a declared global constant before
the aggregate definition is promoted. This does not affect any power
estimate but is part of the exact identity.

There is also a type restriction: \(\mathcal R_A\) is the regularizer of
the singular hard-top \(1/u\) share only. The smooth top remainder and
every interior \(\widehat W_j(u)\) retain an ordinary \(\mu\)-integral;
they cannot be placed under the Plemelj regularizer merely by writing
\(\mathscr W_0=1\). An exact aggregate definition must split

\[
 K_{\rm term}^{\circ}=K_{\rm top,sing}^{\circ}
 +K_{\rm top,reg}+K_{\rm interior},
\]

apply (C39.5) only to the first summand, and keep the other two with their
actual rapidly decaying Mellin amplitudes. Their bounds may be easier, but
that is a separate estimate.
