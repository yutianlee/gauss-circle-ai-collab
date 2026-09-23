# Conductor candidate: determinant endpoint kernel and polylogarithmic shift sector

## 1. Exact statement

Assume the accepted hard-TOP residual setting

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad 0<\gamma<1.
\tag{167.C1}
\]

For every supported product (N=dm\asymp L^2), with (d) odd, retain
the complete literal residual atom

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}),
\tag{167.C2}
\]

where \(\lambda\) contains the squarefree row, normalization,
neither/both selector or no-pair value, both parity branches, profiles,
hard values, endpoints, and zero extension.  On nonzero atoms,
\(|\lambda_{dm}(d)|\ll1\) and (d,m\asymp L).

For (x=(d,m)), (y=(d',m')), and (n(x)=dm), define

\[
\begin{aligned}
 T_{R_0,\gamma}(y,x)={}&
 \left(1-\frac{n(y)-n(x)}{R_0}\right)
 \mathbf1_{0<n(y)-n(x)<R_0}
 \mathbf1_{2\mid n(y)-n(x)}\\
 &\times\mathbf1_{(d'-d)(m'-m)<0}
 \mathbf1_{(d,d')<\gamma L}.
\end{aligned}
\tag{167.C3}
\]

Then the following statements hold.

1. Every ordered literal incidence is represented with multiplicity one by

   \[
   A(y,x)=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
   \qquad \det A=d'm'-dm.
   \tag{167.C4}
   \]

   If (r=hk), (k=2^{v_2(r)}), and (h) is odd, decomposition into
   left \(\Gamma_2(4,1)\)-orbits is also multiplicity preserving.

2. With the convention

   \[
   (Tu)(x)=\sum_yT(y,x)u(y),\qquad
   \langle Tu,u\rangle=\sum_x(Tu)(x)\overline{u(x)},
   \]

   the complete open aggregate has the exact endpoint identity

   \[
   \boxed{
   \mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}
   =\langle T_{R_0,\gamma}u_L,u_L\rangle.}
   \tag{167.C5}
   \]

   In particular, one real part remains outside the complete variable-shift
   aggregate.

3. The present positive capacity of this identity is

   \[
   \|u_L\|_2^2\ll_\varepsilon L^2X^\varepsilon,
   \qquad
   \|T_{R_0,\gamma}\|_{2\to2}
   \ll_\varepsilon LX^\varepsilon,
   \tag{167.C6}
   \]

   and hence

   \[
   |\mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}|
   \ll_\varepsilon L^3X^\varepsilon.
   \tag{167.C7}
   \]

   This is an upper-capacity statement, not a lower bound.  It leaves the
   required factor (L) of signed cancellation open.

4. For every fixed (B>0), put

   \[
   R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\}.
   \tag{167.C8}
   \]

   The complete literal restricted-shift sector is target-safe:

   \[
   \boxed{
   |\mathfrak C^{\rm rem}_{r\le R_{\log}}|
   \ll_{\varepsilon,B}L^2X^\varepsilon.}
   \tag{167.C9}
   \]

   This closes all shifts only when (R_0\le(\log X)^B+1).  At a genuine
   power-scale (L), it covers only (X^{o(1)}) shifts and does not prove
   the full target.

5. The direct applications audited in Round 167 do not prove the remaining
   aggregate.  This is the scoped terminal conclusion

   \[
   \boxed{\texttt{oscillatory\_determinant\_interface\_no\_go}.}
   \tag{167.C10}
   \]

   It applies only to the literal black-box 2024 placement, its fixed-shift
   triangle variant, and the presently available 2025 Part-I placement.  It
   does not rule out a new selector-aware signed determinant theorem,
   controlled-rank decomposition, or another joint method.

## 2. Multiplicity, endpoint identity, and capacity

Given a term at products (N) and (N+r), put

\[
 m=N/d,\qquad m'=(N+r)/d'.
\]

Then (167.C4) follows immediately.  Conversely the four matrix entries
recover

\[
 N=dm,\qquad N+r=d'm',\qquad r=d'm'-dm.
\]

The divisors are ordered by the lower and upper products, so there is no
transpose, divisor-order, projective, or sign quotient.  This proves the
bijection.  A nonzero-determinant matrix is invertible over \(\mathbb Q\).
Thus, if \(\Gamma_2(4,1)\le{\rm SL}_2(\mathbb Z)\) acts on the left and
\(\gamma A=A\), then \(\gamma=I\); the action is free.  Choosing one
representative per orbit therefore introduces no stabilizer multiplicity.

Expanding the right side of (167.C5) gives

\[
\begin{aligned}
\sum_{d,m,d',m'}&
 \left(1-\frac{d'm'-dm}{R_0}\right)
 \mathbf1_{\rm literal\ K17a}\\
&\quad\times
 \chi_4(d')\chi_4(d)
 \lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\end{aligned}
\]

which is exactly the opened K17a expression.  Multiple endpoints may have
the same product, but they are precisely the individual divisor incidences
in the intended double divisor sum; no coefficient sum is duplicated.

For a fixed (x) and gap (r), the product of (y) is fixed, and each
divisor of that product determines at most one endpoint (y).  Hence

\[
 \sup_x\sum_y|T(y,x)|\ll_\eta R_0X^\eta,
 \qquad
 \sup_y\sum_x|T(y,x)|\ll_\eta R_0X^\eta.
\]

Schur's test gives the operator bound in (167.C6).  Separately,

\[
 \|u_L\|_2^2
 \le\sum_{N\in\mathcal I_L^{\rm lit}}\tau(N)
 \ll_\eta L^2X^\eta.
\]

Choose the divisor-bound exponents small enough in terms of the final
\(\varepsilon\).  This proves (167.C6)--(167.C7).

## 3. The strict polylogarithmic sector

All literal selectors and the Fejer weight have modulus at most one.
Therefore

\[
 |\mathfrak C^{\rm rem}_{r\le R_{\log}}|
 \le
 \sum_{\substack{r\le R_{\log}\\2\mid r}}
 \sum_N\tau(N)\tau(N+r).
\tag{167.C11}
\]

Fix the final \(\varepsilon>0\).  Since (N,N+r\ll X), apply
\(\tau(n)\ll_\varepsilon X^{\varepsilon/4}\) to both factors and
\((\log X)^B\ll_{\varepsilon,B}X^{\varepsilon/2}\).  The literal product
shell contains (O(L^2)) integers (N).  Equation (167.C11) proves
(167.C9).  Every parity, squarefree, selector, opposing-displacement,
low-gcd, profile, endpoint, and zero-extension restriction is retained
before this majorization, so the sector is owner-complete.

## 4. Exact source seams and their first failures

Write

\[
 (a,b,c,d_0)=(d',d,m,m'),\qquad
 r=hk,\quad k=2^{v_2(r)},\quad h\text{ odd}.
\tag{167.C12}
\]

Since (a,b) are odd, the preliminary column-primitivity and two-adic
conditions in the 2024 determinant skeleton hold.  The bare coefficient

\[
 \alpha_{\rm bare}(A)=\chi_4(a)\chi_4(b)
\tag{167.C13}
\]

satisfies the full source law
\(\alpha_{\rm bare}\in\mathcal A(4,1,\chi_0,1)\), where \(\chi_0\)
is principal; in particular it is left invariant under
\(\Gamma_2(4,1)\).  Principality does not make its finite orbit
coefficient nonzero.  In fact, it vanishes exactly for every (k=2^v).
Indeed, for every allowed
\(g=\bigl(\begin{smallmatrix}p&4q\\s&t\end{smallmatrix}\bigr)\) with
\((\det g,4)=1\), the integer (p) is odd and
\(\alpha_{\rm bare}(gA)=\chi_4(p)^2\alpha_{\rm bare}(A)
=\alpha_{\rm bare}(A)\).

Represent

\[
 \Gamma_2(4,1)\backslash{\rm SL}_2(\mathbb Z)
 \cong\mathbb P^1(\mathbb Z/4\mathbb Z)
\]

by top rows

\[
 (x,1),\quad x=0,1,2,3,\qquad (1,0),\ (1,2),
\]

and the determinant-(k) Hermite classes by

\[
 \sigma_b=\begin{pmatrix}1&b\\0&k\end{pmatrix},
 \qquad b\pmod k,\quad(b,k)=1,
\]

with (b=0) for (k=1).  A top row ((x,y)) becomes
\((x,xb+yk)\).  Direct summation gives zero at (k=1); at (k=2),
the four ((x,1)) classes contribute (-2) and the last two contribute
(+2); and for (4\mid k), each odd (b) contributes
(4\chi_4(b)), whose unit sum is zero.  Thus

\[
 \sum_{\tau\in\Gamma_2(4,1)\backslash\mathcal M_{2,1,k}}
 \alpha_{\rm bare}(\tau)=0
 \qquad(k=2^v).
\tag{167.C14}
\]

This cancellation is conditional on leaving every selector outside
\(\alpha_{\rm bare}\).  A selector-dependent automorphic coefficient has
a different orbit sum and requires a new calculation.

The literal selector multiplier has no proved source-class realization.
For (0<\gamma<1/2), even the globally defined low-gcd factor cannot
simply multiply (167.C13): choose odd (G,T\asymp L) with
\(\gamma L\le G<L/2\), and put

\[
 A=\begin{pmatrix}G&3G\\T&3T+2\end{pmatrix},\qquad
 v=\begin{pmatrix}1&4\\0&1\end{pmatrix}.
\]

Then \(\det A=2G<L\), while the top-row gcd changes from (G) to one
under (A\mapsto vA).  Hence the low-gcd indicator is not globally left
invariant.  This witness is not asserted to consist of two literal
project incidences, and for \(\gamma\ge1/2\) the low-gcd cutoff is
identically one on K17a.  For every \(\gamma\), however, the remaining
residual selector still has no proved automorphy law or target-safe smooth
interpolation.

The phase gives a separate interface obstruction.  On determinant (r),
normalize (x=a/\sqrt r), (z=d_0/\sqrt r).  It becomes

\[
 e\!\left(J\sqrt r\{\sqrt{xz}-\sqrt{xz-1}\}\right).
\tag{167.C15}
\]

For two distinct determinants, the quotient of these phase functions is
nonconstant on every common open cell.  Thus the natural family is not a
determinant coefficient times one common analytic (f).  This proves
continuous rank-one nonseparability, not impossibility of a discrete
interpolant or controlled-rank decomposition; no target-safe such
construction is currently proved.

Moreover, for

\[
 \phi_r(a,d_0)=J\{\sqrt{ad_0}-\sqrt{ad_0-r}\},
\]

direct differentiation on a nonzero interior cell, with entries of size
\(L\) and with the remaining amplitude not cancelling the phase
derivative, gives

\[
 L|\partial_a\phi_r|+L|\partial_{d_0}\phi_r|
 \asymp\frac{Jr}{L}.
\tag{167.C16}
\]

Absorbing the phase into a smooth source weight therefore requires
\(\delta^{-1}\gtrsim1+Jr/L\).  A fixed positive uncompensated polynomial
seminorm loss is not (X^\varepsilon)-safe in the full range.  This does
not rule out new compensating oscillatory decay.

Under the explicitly optimistic source-scale assumptions

\[
 A=C=D\asymp L,\quad H\asymp L/k,\quad
 |\beta_h|\asymp1\text{ on }\asymp H\text{ indices},\quad
 K_+^{1/2}\ll k^{1/2}X^\varepsilon,
\tag{167.C17}
\]

the 2024 \(\mathcal R_0\) contribution sums over two-powers at the target
scale (L^2X^\varepsilon) before smoothness, while the displayed
\(\mathcal R_2\) route certifies only

\[
 \delta^{-O(1)}L^{2+\theta_4+\varepsilon}.
\tag{167.C18}
\]

The source supplies only \(\theta_4\le7/64\), not \(\theta_4=0\), and
retains an unspecified \(\delta^{-O(1)}\).  Equation (167.C17) is a
hypothetical dense-block audit; literal nonemptiness or density is not
asserted.  The orbit-correlation input (K_+\), smoothness, cells,
boundaries, endpoints, and completion remain separate obligations.  No
negative-power (K_+\) estimate is inferred.

For the 2025 Part-I interface, complex oscillatory (C^{10}_\delta)
weights are formally allowed, but their frequency is charged through
\(\delta^{-O(1)}\).  More fundamentally, no embedding of the literal
endpoints into the source group and no exact raw automorphic-kernel
identity producing (167.C3) without extra relative pairs has been proved.
Even after such an identity, the principal component must be separated
and two nonnegative discrepancy-kernel autocorrelations remain unbounded
at the target scale.  Accepted endpoint energy alone does not supply the
missing factor (L).

Applying either source separately for fixed (r) and summing theorem
errors absolutely would move the absolute value inside the shift aggregate.
It therefore does not prove the one-outer-real-part bound.

## 5. First open step and scope

The exact open estimate remains

\[
 \Re\langle T_{R_0,\gamma}u_L,u_L\rangle
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{167.C19}
\]

After the polylogarithmic sector, the unproved range is
\((\log X)^B<r<R_0\) whenever it is nonempty.  A future determinant
argument must supply a multiplicity-preserving, target-safe realization
of the literal selector and variable-(r) phase, retain the single outer
real part, and prove every orbit-correlation, main/principal component,
seminorm, cell, boundary, endpoint, and completion cost.

Nothing here proves the complete residual scalar, the full (t=1) face,
another hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, either direct M1
parent, GAR, endpoint uniformity, M9, either bridge, the quarter theorem,
or a better global exponent.

## 6. Dependencies and state recommendation

This candidate depends on the accepted Round-164 residual transport kernel
and Round-165 parity/gcd/scale kernel.  Its evidentiary basis is the three
Round-167 reports and the three independent Round-167 seam reviews.

Recommended effect: create one homogeneous proved-internal reduction node
containing only (167.C4)--(167.C9).  Retain (167.C14) as finite
source-skeleton audit evidence and (167.C10) as a source-dependent
rejected-route record, rather than mixing either into that internal node's
statement.  Retain K17a and every parent as open, and record no exponent
change.
