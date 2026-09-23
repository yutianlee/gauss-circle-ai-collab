# Kernel: residual Fejer parity, tangent, gcd, and scale reductions

## Statement

Retain the complete literal residual coefficient

\[
 c_N^{\mathrm{rem}}
 =\sum_{\substack{d\mid N\\ d\ \mathrm{odd}}}
   \chi_4(d)\lambda_N(d),
\tag{165.K1}
\]

where \(\lambda_N(d)\) contains the supported squarefree row,
normalization, neither/both residual selector (or the no-pair value one),
both parity branches, every profile, hard point value, endpoint, and zero
extension.  On nonzero atoms,

\[
 N\asymp L^2,\qquad d,m=N/d\asymp L,
 \qquad |\lambda_N(d)|\ll1.
\tag{165.K2}
\]

Put \(z_N=c_N^{\mathrm{rem}}e(J\sqrt N)\) on the positive literal shell
and \(z_N=0\) at every other integer.  Let a consecutive interval of
cardinality \(M_L\asymp L^2\) contain that shell, and set

\[
 D_L=\sum_N|c_N^{\mathrm{rem}}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{165.K3}
\]

The following conclusions are exact.

### 1. Every Fejer scale and the parity connector

For every positive integer \(R\), define

\[
 \mathfrak E_R={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
 =D_L+2\Re\mathfrak C_R,
\tag{165.K4}
\]

where

\[
 \mathfrak C_R=
 \sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_{\substack{N\ge1\\N,N+r\in\mathcal I_L^{\mathrm{lit}}}}
       c_{N+r}^{\mathrm{rem}}
       \overline{c_N^{\mathrm{rem}}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\tag{165.K5}
\]

Every later abbreviated \(\sum_N\) carrying this phase is understood over
the same positive nonzero pair domain; zero extension is used in the
sliding identities without evaluating a square root off that domain.

Then

\[
 |\mathcal S_{L,1}^{\mathrm{rem}}|^2
 \le {M_L+R-1\over R}\mathfrak E_R.
\tag{165.K6}
\]

For \(\epsilon\in\{0,1\}\), define the absolute-site parity parts

\[
 Y_s^{(\epsilon)}=
 \sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j}.
\]

Put

\[
 \mathfrak E_R^{(2)}={1\over R}\sum_s
 \left(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\right)
 =D_L+2\Re\mathfrak C_R^{(2)},
\tag{165.K7}
\]

where \(\mathfrak C_R^{(2)}\) is (165.K5) restricted to even \(r\).
For odd \(R=2S+1\ge3\), if \(x_n=z_{2n}\), \(y_n=z_{2n+1}\), and
\(\mathcal E_T(w)=T^{-1}\sum_k|\sum_{j=0}^{T-1}w_{k+j}|^2\), then exactly

\[
 \mathfrak E_{2S+1}^{(2)}
 ={S+1\over2S+1}
   \{\mathcal E_{S+1}(x)+\mathcal E_{S+1}(y)\}
 +{S\over2S+1}
   \{\mathcal E_S(x)+\mathcal E_S(y)\}.
\tag{165.K7a}
\]

In particular, the terminal even gap \(2S=R-1\) has exact weight
\(1/R\).  At \(R=1\), directly
\(\mathfrak E_1=\mathfrak E_1^{(2)}=D_L\).  The endpoint-exact inequality

\[
 \boxed{\mathfrak E_R\le2\mathfrak E_R^{(2)}}
\tag{165.K8}
\]

holds for even or odd \(R\).  Equivalently,

\[
 \Re\mathfrak C_R
 \le {D_L\over2}+2\Re\mathfrak C_R^{(2)}.
\tag{165.K9}
\]

Thus at the minimal diagonal-safe scale \(R_0=\lceil L\rceil\), it is
sufficient to bound only the aggregate even shifts.

### 2. Tangent sectors

In the multiplicity-one divisor opening of (165.K5), put

\[
 a=d'-d,\qquad b=m'-m.
\]

Then

\[
 a\equiv0\pmod2,\qquad b\equiv r\pmod2,
\tag{165.K10}
\]

and

\[
 \boxed{
 r=db+am+ab=db+a m',\qquad
 \chi_4(d')\chi_4(d)=(-1)^{a/2}.}
\tag{165.K11}
\]

The complete union over \(1\le r<R_0\) with \(a,b\ge0\) has
\(O(L^2)\) literal atoms.  Consequently,

\[
 \boxed{|\mathfrak C_{R_0,\mathrm{mon}}^{\mathrm{rem}}|
 \ll L^2.}
\tag{165.K12}
\]

The sector \(a,b\le0\), apart from the impossible \((0,0)\), and the
one-zero negative sectors are empty for \(r>0\).  Every remaining tuple
has \(ab<0\).  Combining (165.K8) and (165.K12), the residual scalar
target follows from the single open theorem

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,\mathrm{opp}}^{\mathrm{rem}}
 \ll_\varepsilon L^2X^\varepsilon,}
\tag{165.K13}
\]

where the aggregate retains exactly the even shifts and
\((d'-d)(m'-m)<0\), with no modulus around a shift or tuple.

### 3. Dual gcd normal forms and an actual high-gcd sector

The character-divisor-gcd form is

\[
 g=(d,d'),\quad d=gu,\quad d'=gv,\quad (u,v)=1,
 \quad r=gh,
\tag{165.K14}
\]

with

\[
 vm'-um=h,\qquad
 m=m_0+vt,\qquad m'=m'_0+ut.
\tag{165.K15}
\]

Writing \(A=gu m_0\) and \(K_d=guv=dd'/g\), one has

\[
 N(t)=A+K_dt,\qquad N(t)+r=A+r+K_dt,
 \qquad \chi_4(d')\chi_4(d)=\chi_4(uv).
\tag{165.K16}
\]

The geometric row has \(O(1+g)\) points before literal arithmetic
deletions.  If \(\mathfrak C_{R_0,g\ge G_0}^{\mathrm{rem}}\) denotes the
complete opened divisor-incidence sector restricted only by
\((d,d')=g\ge G_0\), then

\[
 \boxed{
 |\mathfrak C_{R_0,g\ge G_0}^{\mathrm{rem}}|
 \ll_\varepsilon {L^3\over G_0}X^\varepsilon
 \qquad(1\le G_0<R_0).}
\tag{165.K17}
\]

Hence, for each fixed \(\gamma>0\), the owner-complete actual sector
\((d,d')\ge\gamma L\) is target-safe.
Combining this with (165.K13), it is enough to prove the still smaller
open theorem

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,\mathrm{opp},\,g<\gamma L}^{\mathrm{rem}}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{165.K17a}
\]

Here the gcd split is made after the exact divisor opening, so it is
owner-complete for divisor incidences rather than a unique partition of
product rows.

The cofactor-gcd form is

\[
 s=(m,m'),\quad m=su,\quad m'=sv,\quad (u,v)=1,
 \quad r=sh,
\tag{165.K18}
\]

with \(vd'-ud=h\).  After fixing one solution and imposing that both
divisors are odd, all solutions are

\[
 d=D_0+2vk,\qquad d'=D'_0+2uk,
\tag{165.K19}
\]

and

\[
 N(k)=N_0+K_sk,\qquad N(k)+r=N_0+r+K_sk,
 \qquad K_s=2suv={2mm'\over s}.
\tag{165.K20}
\]

The geometric row has \(O(1+s)\) points and

\[
 \boxed{
 \chi_4(d(k))\chi_4(d'(k))
 =\sigma_0(-1)^{(r\bmod2)k}.}
\tag{165.K21}
\]

For even shifts the character is therefore frozen along every cofactor
row.  This includes the squarefree even-even branch: there
\(\nu_2(s)=1\), \(u,v\) are odd, \(4\mid r\), and \(h=r/s\) is even.

### 4. Exact phase ledger and route-scoped obstruction

For either arithmetic row let \(K\) be its actual product increment, put
\(x(t)=x_0+Kt\), and define

\[
 \Psi(t)=J(\sqrt{x(t)+r}-\sqrt{x(t)}).
\]

Then

\[
\begin{aligned}
 \Psi'(t)&={JK\over2}\{(x+r)^{-1/2}-x^{-1/2}\},\\
 \Psi''(t)&={JK^2\over4}\{x^{-3/2}-(x+r)^{-3/2}\},\\
 \Psi'''(t)&={3JK^3\over8}\{(x+r)^{-5/2}-x^{-5/2}\}.
\end{aligned}
\tag{165.K22}
\]

On a cofactor row, \(K=K_s\asymp L^2/s\), \(r=sh\), and

\[
 |\Psi'|\asymp {Jh\over L},\qquad
 \Psi''\asymp {Jh\over sL},\qquad
 |\Psi'''|\asymp {Jh\over s^2L}.
\tag{165.K23}
\]

The effective phase is \(\Psi(k)+(r\bmod2)k/2\).  A first-difference
argument therefore needs the distance to an integer of

\[
 J\{\Delta_r(x+K)-\Delta_r(x)\}+{r\bmod2\over2},
 \qquad \Delta_r(x)=\sqrt{x+r}-\sqrt x.
\tag{165.K24}
\]

No such uniform separation is proved.  Since
\(\Psi''\asymp Jh/(sL)\gg1\), the classical real second-derivative
expression is worse than the trivial row bound.  On a smooth full
divisor-gcd row, completing and then taking absolute values of all
stationary dual modes is likewise adverse.  These are route-scoped
statements only: coupled dual modes, higher-order methods, joint
\((r,N)\) transforms, signed spectral formulas, and bespoke actual
arithmetic remain open.

### 5. A distinct maximal-scale alternative

The choice \(R_0=\lceil L\rceil\) is minimal diagonal-safe, not mandatory.
At \(R=M_L\), Cauchy pays all shifts \(1\le r<R_0\):

\[
 \sum_{1\le r<R_0}\left(1-{r\over M_L}\right)
 \left|\sum_Nc_{N+r}^{\mathrm{rem}}
 \overline{c_N^{\mathrm{rem}}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\right|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{165.K25}
\]

Consequently the residual scalar target also follows from the distinct
open theorem

\[
 \boxed{
 \Re\sum_{\substack{R_0\le r<M_L\\2\mid r}}
 \left(1-{r\over M_L}\right)
 \sum_Nc_{N+r}^{\mathrm{rem}}
 \overline{c_N^{\mathrm{rem}}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{165.K26}
\]

Thus failure of the minimal-scale short-shift estimate does not terminate
the Fejer strategy: (165.K26) moves the required cancellation to the
aggregate even medium/long shifts.

## Proof

For (165.K4), expand the full-line sliding-window square.  A pair at gap
\(r<R\) occurs in exactly \(R-r\) windows.  Every supported coefficient
occurs in exactly \(R\) windows, while the containing interval supplies
exactly \(M_L+R-1\) available window starts.  Cauchy's inequality proves
(165.K6); gaps in the literal shell only turn some windows into zero.

Split each window into its absolute even and odd sites.  Direct reindexing
of the four subsequence-window sums proves (165.K7a), including the final
weight \(1/R\).  The inequality
\(|A+B|^2\le2(|A|^2+|B|^2)\) proves (165.K8).  On the right, a pair
survives exactly when its gap is even, and it is still counted in
\(R-r\) windows.  This proves (165.K7)--(165.K9) without an endpoint
rounding term.

The tangent map is bijective because a tuple uniquely determines
\((a,b,d,m)\), and the inverse is \((d',m')=(d+a,m+b)\).  Direct
expansion proves (165.K11), while
\(\chi_4(d+2q)=(-1)^q\chi_4(d)\) proves its character identity.  On
literal support all four factors are at least \(\kappa L\) for a fixed
\(\kappa>0\).  If \(a,b\ge0\), then
\(r=db+a m'\ge\kappa L(a+b)\), so only \(O(1)\) pairs \((a,b)\) occur.
For each pair there are \(O(L^2)\) possible \((d,m)\), and \(r\) is then
determined.  This proves (165.K12) across all shifts.  The sign of
\(db+a m'\) proves the empty-sector assertions.  Equations (165.K8),
(165.K12), (165.K3), and (165.K6) prove the sufficiency of (165.K13).

Dividing the product-shift equation by \(g=(d,d')\) proves
(165.K14)--(165.K16), including multiplicity and the fixed character.
For fixed \(g\), the ranges contain
\(O(L/g)\) choices for each of \(u,v,h\), and each row has \(O(g)\)
points.  Therefore

\[
 \sum_{g\ge G_0}O\!\left((L/g)^3g\right)
 \ll {L^3\over G_0},
\]

which proves (165.K17); every literal restriction only deletes atoms.

The same Diophantine argument with \(s=(m,m')\) proves
(165.K18)--(165.K20).  Oddness selects one parity class of the primitive
solution parameter.  Advancing \(k\) changes the character product by
\((-1)^{u+v}\).  Opposite product parities occur exactly for odd \(r\),
whereas on supported even shifts the reduced \(u,v\) are both odd.  This
proves (165.K21), including the even-even ledger.

Direct differentiation proves (165.K22), and the physical scales give
(165.K23).  Equation (165.K24) is the exact discrete resonance after the
character is absorbed.  Its absent modulo-one separation, the vacuous
positive second-derivative expression, and the adverse absolute dual-mode
ledger prove only the stated route obstructions.

Finally, fixed-shift Cauchy bounds the modulus of each inner correlation
by \(D_L\).  Summing the first \(R_0-1\) shifts proves (165.K25).  Apply
(165.K8) at \(R=M_L\): the diagonal, the paid short even shifts, and
(165.K26) give
\(\mathfrak E_{M_L}^{(2)}\ll L^3X^\varepsilon\).
Then (165.K8) and (165.K6), with
\((2M_L-1)/M_L<2\), give
\(|\mathcal S_{L,1}^{\mathrm{rem}}|^2\ll_\eta L^3X^\eta\).
Apply (165.K3), (165.K25), and the open hypothesis (165.K26) with
\(\eta=2\varepsilon\) before taking the square root.  This proves
\(|\mathcal S_{L,1}^{\mathrm{rem}}|
\ll_\varepsilon L^{3/2}X^\varepsilon\).

## Status and scope

Equations (165.K4)--(165.K12), (165.K14)--(165.K17),
(165.K18)--(165.K25), and the implications
from the boxed open estimates are proved internally.  The monotone
displacement sector (165.K12) and the fixed-proportion high-common-divisor
sector from (165.K17) are genuine owner-complete, target-safe strict
sectors.  Equation (165.K17a) is the sharpest minimal-scale open theorem,
while (165.K26) is the distinct maximal-scale alternative.  Neither has
been proved; (165.K13) is a broader sufficient minimal-scale statement.

The terminal label is `strict_residual_short_shift_sector`.  Nothing here
proves the complete residual, the full \(t=1\) face, another few-point
channel, either hard-TOP parent, BAL, UNBAL, a smooth M2 packet, M9--M2,
M9--M1, endpoint uniformity, M9, the bridge, the quarter theorem, or a
better global exponent.
