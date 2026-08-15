# Round 50 derivation packet: alpha high-pass log-dilation commutator

This is the complete statement-only packet.  It freezes one possible
mechanism and does not assert that the mechanism succeeds.

## 1. Exact accepted alpha reduction

Put

\[
 A=s-z/2,\qquad B=s+z/2,
 \qquad \beta=\Im A,\quad \alpha=\Im B.
\]

The alpha arithmetic factor is

\[
 X_\zeta(A)\zeta(A)L(1-B,\chi_4),
\]

with unsigned high coefficients \(h^{-A}\).  Against compact smooth
Mellin tests,

\[
 \frac1{2\pi i}\int_{(c)}X_\zeta(A)\zeta(A)Y^{-A}\,dA
 =\begin{cases}
 \sum_{n\ge1}\delta(Y-n),&c<0,\\
 \sum_{n\ge1}\delta(Y-n)-1
 =2\sum_{h\ge1}\cos(2\pi hY),&c>0.
 \end{cases}
\tag{50.1}
\]

The difference is

\[
 \operatorname*{Res}_{A=0}\zeta(1-A)=-1.
\tag{50.2}
\]

The actual hierarchical mask is

\[
 \Theta_\alpha(\alpha,\beta)
 =(1-\psi(\beta))\psi(\alpha),
\tag{50.3}
\]

where \(\psi\in C_c^\infty(\mathbb R)\), \(\psi=1\) near zero.  The
alpha branch owns no new \(A=0\) residue because its mask and the first
and mixed connector derivatives vanish there.

## 2. Fourier convention and candidate commutator

Use

\[
 \widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
 \qquad
 f(t)=\frac1{2\pi}\int_{\mathbb R}\widehat f(\xi)e^{it\xi}\,d\xi.
\tag{50.4}
\]

If \(k=(2\pi)^{-1}\widehat\psi\), then the inverse transform of
\(1-\psi(\beta)\) is the distribution

\[
 \delta_0-k(r),
 \qquad \int_{\mathbb R}k(r)\,dr=\psi(0)=1.
\tag{50.5}
\]

Hence, for a sufficiently regular logarithmic amplitude \(F(L)\), the
high-pass factor suggests the exact formal commutator

\[
 \mathcal H_\psi F(L)
 =F(L)-\int_{\mathbb R}k(r)F(L-r)\,dr
 =\int_{\mathbb R}k(r)\{F(L)-F(L-r)\}\,dr.
\tag{50.6}
\]

The sign of \(r\) depends on the precise Mellin exponential and must be
rederived, not assumed.  In the actual alpha operator, \(\psi(\alpha)\)
couples \(\beta\) to the outside heights through
\(\alpha=\beta+\mu+\nu\); therefore (50.6) is not yet a scalar
commutator on the comb.

## 3. Mandatory finite ownership

Begin with one common finite \((u,v,s)\) antecedent and one common Abel
regularization.  Retain:

1. the masked terminal bulk;
2. the smooth Cauchy--Pompeiu area connector or both sharp strip edges;
3. every finite \(u\)- and \(v\)-face;
4. the positive \(u=0\) and \(v=0\) axes and one joint corner;
5. connector-face, connector-axis, and mixed connector terms;
6. the signed top Plemelj operation before absolute values;
7. the radial \(R_1\) factor, actual dyadic scales, \(H_j+1\) floors,
   profiles, product stars, and one external \(X^{1/4}\) factor;
8. the already accepted global routing of the \(A=0\) constant mode.

Only after the complete finite sum is formed may one take Abel and joint
outside-height limits.

## 4. Required quantitative gain and controls

The pure Abel cosine tower is coherent at integers:

\[
 2\sum_{h\ge1}r^h\cos(2\pi hn)=\frac{2r}{1-r}.
\tag{50.7}
\]

The minus radial phase has stationary point

\[
 x=\frac{Xt^2}{4h^2}.
\tag{50.8}
\]

For an active scale, the unmasked lattice has normalized all-absolute
capacity

\[
 X^{1/8+o(1)},
\tag{50.9}
\]

and the original alpha height integral has capacity

\[
 U^{c'-1/2-\Re z/2}.
\tag{50.10}
\]

Any successful commutator theorem must save these losses after the signed
height operation.  It must be tested at exact lattice points, dyadic
profile edges, height-floor jumps, product-star equalities, and radial
endpoints.  A BV estimate for a smooth surrogate does not certify the
actual amplitude.

## 5. Target and strict scope

Derive the exact finite analogue of (50.6) for the complete alpha
operator and prove its normalized size is

\[
 O_\varepsilon(X^\varepsilon),
\]

including a Cauchy outside-height limit, or isolate the first exact
actual-profile term that prevents this.  A rigorous obstruction to the
zero-mass mechanism is successful progress.

Do not reopen the beta branch.  Do not promote the alpha estimate, swept
operator, post-FE vector kernel, M9-M1, M9, or the Gauss-circle target
from a bulk-only or smooth-surrogate commutator.
