# Kernel: residual determinant endpoint representation and polylogarithmic shifts

## Statement

Retain the accepted hard-TOP residual coefficient in the range

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad 0<\gamma<1.
\tag{167.K1}
\]

For every supported product (N=dm\asymp L^2), with (d) odd, let

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}),
\tag{167.K2}
\]

where \(\lambda_N(d)\) retains the complete literal squarefree row,
normalization, residual selector, parity branch, profile, hard value,
endpoint, and zero extension.  On nonzero atoms,

\[
 d,m\asymp L,qquad |\lambda_{dm}(d)|\ll1.
\tag{167.K3}
\]

Let \(\mathcal E_L\) be the set of these nonzero endpoint atoms and set
\(n(d,m)=dm\).  For (x=(d,m)), (y=(d',m')), define

\[
\begin{aligned}
 T_{R_0,\gamma}(y,x)={}&
 \left(1-\frac{n(y)-n(x)}{R_0}\right)
 \mathbf1_{0<n(y)-n(x)<R_0}
 \mathbf1_{2\mid n(y)-n(x)}\\
 &\times\mathbf1_{(d'-d)(m'-m)<0}
 \mathbf1_{(d,d')<\gamma L}.
\end{aligned}
\tag{167.K4}
\]

Use

\[
 (Tu)(x)=\sum_{y\in\mathcal E_L}T(y,x)u(y),qquad
 \langle Tu,u\rangle=\sum_x(Tu)(x)\overline{u(x)}.
\tag{167.K5}
\]

Then the complete even-shift, opposing-displacement, low-divisor-gcd
residual aggregate has the exact identity

\[
 \boxed{
 \mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}
 =\langle T_{R_0,\gamma}u_L,u_L\rangle.}
\tag{167.K6}
\]

Every ordered divisor incidence in this form corresponds bijectively to

\[
 A(y,x)=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad \det A=d'm'-dm.
\tag{167.K7}
\]

For (r=hk), (k=2^{v_2(r)}), (h) odd, any further decomposition into
left \(\Gamma_2(4,1)\)-orbits is multiplicity preserving.

The currently available positive endpoint estimate is

\[
 \|u_L\|_2^2\ll_\varepsilon L^2X^\varepsilon,
 \qquad
 \|T_{R_0,\gamma}\|_{2\to2}
 \ll_\varepsilon LX^\varepsilon,
\tag{167.K8}
\]

and hence

\[
 |\mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{167.K9}
\]

This is only an upper capacity.  The target still needs one factor (L)
of signed cancellation.

For every fixed (B>0), define

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\}.
\tag{167.K10}
\]

The complete literal restricted-shift sector satisfies

\[
 \boxed{
 |\mathfrak C^{\rm rem}_{r\le R_{\log}}|
 \ll_{\varepsilon,B}L^2X^\varepsilon.}
\tag{167.K11}
\]

Thus all shifts are closed if (R_0\le(\log X)^B+1).  If (L) is a
genuine power of (X), this is only an (X^{o(1)})-shift strict sector
and does not prove the complete K17a estimate.

## Proof

### 1. Incidence and determinant multiplicity

An ordered term at products (N) and (N+r) selects odd divisors
\(d\mid N\) and \(d'\mid N+r\).  Put

\[
 m=N/d,qquad m'=(N+r)/d'.
\]

Then

\[
 d'm'-dm=(N+r)-N=r,
\]

which proves (167.K7).  Conversely, the four entries recover

\[
 N=dm,qquad N+r=d'm',qquad r=d'm'-dm.
\]

The divisors are ordered by their lower and upper products.  There is no
transpose, divisor-order, sign, projective, or stabilizer quotient, so the
map is a bijection.

Let \(\Gamma_2(4,1)\le{\rm SL}_2(\mathbb Z)\) act on the left.  It
preserves the determinant.  Since (r\ne0), the matrix (A) is invertible
over \(\mathbb Q\); hence \(\gamma A=A\) implies \(\gamma=I\).  The
action is free.  Choosing one representative for every orbit and then
restricting the inner group sum to literal matrices therefore counts
every literal incidence exactly once, even though literal support need not
be orbit invariant.

### 2. Exact endpoint identity

For (x=(d,m)) and (y=(d',m')),

\[
\begin{aligned}
u_L(y)\overline{u_L(x)}={}&
\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}\\
&\times e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\end{aligned}
\tag{167.K12}
\]

Multiplication by (167.K4) inserts exactly the Fejer factor, positive even
gap, opposing displacement, and low-divisor-gcd restriction.  Membership
of (x,y) in \(\mathcal E_L\) retains the full literal atom support and
zero extension.  Summing ordered endpoint pairs proves (167.K6).

Different endpoints may have the same product, but they are precisely the
different divisor incidences in the intended double divisor sum.  The
vector contains individual \(\lambda_N(d)\) atoms, not a second copy of
the already summed coefficient \(c_N^{\rm rem}\), so no coefficient term
is duplicated.  The identity also preserves one real part outside the
complete variable-shift sum.

### 3. Schur capacity

Fix (x) and a gap (r).  The product of (y) is (n(x)+r), and every
divisor (d'\mid n(x)+r) determines at most one (m').  All remaining
literal conditions only delete endpoints, while the Fejer weight has
modulus at most one.  Hence, for an auxiliary exponent \(\eta>0\),

\[
 \sup_x\sum_y|T(y,x)|
 \ll_\eta R_0X^\eta
 \ll_\eta LX^\eta.
\tag{167.K13}
\]

The same argument backwards from (y) gives

\[
 \sup_y\sum_x|T(y,x)|\ll_\eta LX^\eta.
\tag{167.K14}
\]

Schur's test proves the operator estimate in (167.K8).  Moreover,

\[
 \|u_L\|_2^2
 \le\sum_{N\in\mathcal I_L^{\rm lit}}
 \sum_{d\mid N}1
 \le\sum_{N\in\mathcal I_L^{\rm lit}}\tau(N)
 \ll_\eta L^2X^\eta.
\tag{167.K15}
\]

The literal product shell contains (O(L^2)) integers.  Choosing all
auxiliary divisor exponents sufficiently small in terms of the final
\(\varepsilon\), (167.K13)--(167.K15) give (167.K8)--(167.K9).

### 4. Polylogarithmic shifts

Every literal atom, selector, character, phase, and Fejer factor has
modulus at most one.  Taking one modulus outside the complete sector
restricted by (r\le R_{\log}) gives

\[
 |\mathfrak C^{\rm rem}_{r\le R_{\log}}|
 \le
 \sum_{\substack{r\le R_{\log}\\2\mid r}}
 \sum_N\tau(N)\tau(N+r).
\tag{167.K16}
\]

Fix the desired final \(\varepsilon>0\).  Since (N,N+r\ll X), use

\[
 \tau(N),\tau(N+r)\ll_\varepsilon X^{\varepsilon/4},
 \qquad
 (\log X)^B\ll_{\varepsilon,B}X^{\varepsilon/2}.
\]

There are (O(L^2)) possible products (N), so (167.K16) proves
(167.K11).  All literal restrictions are imposed before the majorization;
therefore the result owns every divisor incidence in the selected shift
sector rather than a model or filter-erased subset.

## Status and scope

Equations (167.K6)--(167.K11) are proved internally.  The complete target

\[
 \Re\mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon
\]

remains open outside the polylogarithmic sector.  The kernel proves no
complete residual scalar, full (t=1) face, other hard-TOP channel, hard
TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint theorem, M9, bridge, quarter
theorem, or improved global exponent.
