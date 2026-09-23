# Kernel: hard-TOP \(t=1\) Mellin--Euler reduction and polylogarithmic sector

## Statement

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac{X}{y^2},\qquad
 H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
 \qquad 1\ll L\ll H.
\tag{168.K1}
\]

Retain the complete literal selector-free hard-TOP \(t=1\) scalar

\[
\begin{aligned}
 \mathcal S_{L,1}
 =\sum_{\substack{nm\asymp L^2\\
                  n,m\ {\rm squarefree},\ (n,m)=1\\
                  n\ {\rm odd},\ m\le n\le4m}}
 &\chi_4(n)\left(\frac{L^2}{nm}\right)^{3/4}
 \eta_L(n)\Phi\!\left(\frac{n}{H+1}\right)\\
 &\times W\!\left(\sqrt{\frac{q_Xn}{4m}}\right)
 e(J\sqrt{nm}),
\end{aligned}
\tag{168.K2}
\]

with every accepted half-open shell, real-centre floor, profile value,
cone edge, star, endpoint transition, and zero-extension convention.  Let
\(A_{L,X}(n,m)\) denote its complete bounded non-arithmetic amplitude.

Initially for \(\Re s_1,\Re s_2>1\), put

\[
 D(s_1,s_2)=
 \sum_{\substack{n,m\ {\rm squarefree}\\(n,m)=1\\n\ {\rm odd}}}
 \frac{\chi_4(n)}{n^{s_1}m^{s_2}}.
\tag{168.K3}
\]

Then

\[
 \boxed{D(s_1,s_2)=L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2),}
\tag{168.K4}
\]

where

\[
 G_2=1-2^{-2s_2},\qquad
 G_p=(1+x_p+y_p)(1-x_p)(1-y_p)
\tag{168.K5}
\]

for odd primes \(p\), with
\(x_p=\chi_4(p)p^{-s_1}\) and \(y_p=p^{-s_2}\).  The product for
\(G\) is absolutely and locally uniformly convergent, hence holomorphic,
throughout \(\Re s_1,\Re s_2>1/2\).

For every fixed \(0<\eta<1/4\), there is an exact endpoint-lawful
cardinal Mellin representation satisfying

\[
 \boxed{\mathcal S_{L,1}=R_\zeta+\mathcal I_\eta,}
 \qquad
 R_\zeta\ll_\varepsilon \frac{L^2}{J}X^\varepsilon,
\tag{168.K6}
\]

where, with \(\alpha=1/2+\eta\),

\[
\begin{aligned}
 \mathcal I_\eta=\frac1{(2\pi)^2}\int_{\mathbb R^2}
 &\widehat{\mathcal B}(\alpha+it_1,\alpha+it_2)
 L(\alpha+it_1,\chi_4)\zeta(\alpha+it_2)\\
 &\times G(\alpha+it_1,\alpha+it_2)\,dt_1dt_2.
\end{aligned}
\tag{168.K7}
\]

Thus the polynomial-range \(t=1\) target is reduced, up to the
target-safe residue, to the exact signed two-height estimate

\[
 \mathcal I_\eta\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{168.K8}
\]

On a favorable recombined smooth/BV control component, radial stationarity
lies at

\[
 t_+=t_1+t_2=-2\pi Jr\asymp-JL
\tag{168.K9}
\]

over a band of length \(T\asymp JL\), and the pointwise transform scale
on the shifted lines is

\[
 L^{1+2\eta}T^{-1/2}
 =L^{2\eta}\sqrt{L/J}.
\tag{168.K10}
\]

Triangle inequality after a granted Lindelof-size pointwise arithmetic
majorant, and Cauchy after a granted fixed-angular arithmetic mean square
of size \(TX^\delta\), both have the raw capacity

\[
 L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
\tag{168.K11}
\]

For a requested final exponent \(\varepsilon>0\), choosing
\(0<\eta\le\min(1/8,\varepsilon/4)\) and then \(\delta\) sufficiently
smaller than \(\varepsilon\) absorbs \(L^{2\eta}X^\delta\) into
\(X^\varepsilon\).  The structural deficit remains \(\sqrt J\).
This is a capacity statement only for those two named absolute placements;
it is neither a lower bound nor a no-go for a new signed weighted hybrid
theorem.

For every fixed \(B>0\), the complete full scalar satisfies

\[
 \boxed{
 L\le(\log X)^B
 \quad\Longrightarrow\quad
 \mathcal S_{L,1}\ll_{\varepsilon,B}L^{3/2}X^\varepsilon.}
\tag{168.K12}
\]

For fixed \(\kappa>0\), let
\(\mathcal S^{\rm cp}_{L,1;\kappa}\) and
\(\mathcal S^{\rm rem}_{L,1;\kappa}\) be the accepted canonical
close-opposite-prime XOR sector and its exact complement.  Then

\[
 \mathcal S_{L,1}
 =\mathcal S^{\rm cp}_{L,1;\kappa}
  +\mathcal S^{\rm rem}_{L,1;\kappa},
 \qquad
 \mathcal S^{\rm cp}_{L,1;\kappa}\ll_\kappa L^{3/2},
\tag{168.K13}
\]

and hence, for every fixed \(B,\kappa>0\),

\[
 L\le(\log X)^B
 \quad\Longrightarrow\quad
 \mathcal S^{\rm rem}_{L,1;\kappa}
 \ll_{\varepsilon,B,\kappa}L^{3/2}X^\varepsilon.
\tag{168.K14}
\]

No polynomial-\(L\) full scalar, general residual, other hard-TOP channel,
hard TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint theorem, M9, bridge,
quarter theorem, or exponent is proved.

## Proof

### 1. Euler algebra

At \(p=2\), oddness of the first leg permits \(2\) only in the second,
so \(D_2=1+2^{-s_2}\).  At an odd prime, squarefreeness and coprimality
permit exactly three states: the prime divides neither leg, only the first,
or only the second.  Thus \(D_p=1+x_p+y_p\).  Removing the local factors
of \(L(s_1,\chi_4)\zeta(s_2)\) gives (168.K5), and

\[
 G_p
 =1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2.
\tag{168.K15}
\]

On compact subsets of \(\Re s_1,\Re s_2>1/2\),

\[
 |G_p-1|\ll
 p^{-2\Re s_1}+p^{-2\Re s_2}
 +p^{-\Re s_1-\Re s_2}
 +p^{-3\min(\Re s_1,\Re s_2)}.
\]

The prime sum converges, proving (168.K4)--(168.K5).  No nonvanishing of
\(G\) is asserted or used.

### 2. Exact cardinal interpolation and residue

Choose \(\psi\in C_c^\infty((-1/3,1/3))\) with \(\psi(0)=1\), and set

\[
 \mathcal B(x,z)=e(J\sqrt{xz})
 \sum_{n,m}A_{L,X}(n,m)\psi(x-n)\psi(z-m).
\tag{168.K16}
\]

The sum is finite and its cells are disjoint.  Therefore

\[
 \mathcal B(n,m)=A_{L,X}(n,m)e(J\sqrt{nm})
\tag{168.K17}
\]

at every positive integer pair, including every literal hard value.
Define

\[
 \widehat{\mathcal B}(s_1,s_2)
 =\int_0^\infty\!\int_0^\infty
 \mathcal B(x,z)x^{s_1-1}z^{s_2-1}\,dx\,dz.
\tag{168.K18}
\]

This transform is entire and rapidly decreasing on every fixed vertical
strip.  Mellin inversion and absolute convergence on initial lines
\(c_1,c_2>1\) give

\[
 \mathcal S_{L,1}
 =\frac1{(2\pi i)^2}\int_{(c_1)}\!\int_{(c_2)}
 \widehat{\mathcal B}(s_1,s_2)D(s_1,s_2)\,ds_2ds_1.
\tag{168.K19}
\]

Move the \(s_2\)-line first while \(\Re s_1=c_1>1\), and then move the
remaining \(s_1\)-line.  In the direct holomorphy region of \(G\), the
only crossed pole is \(s_2=1\).  For odd primes,

\[
 L_p(s,\chi_4)G_p(s,1)
 =(1-p^{-2})+(1-p^{-1})\chi_4(p)p^{-s},
\]

while the factor at \(2\) is \(1-2^{-2}\).  Hence, initially for
\(\Re s>1\),

\[
 L(s,\chi_4)G(s,1)
 =\frac1{\zeta(2)}
 \sum_{\substack{n\ge1\\n\ {\rm odd,\ squarefree}}}
 \frac{\chi_4(n)}{n^s}
 \prod_{p\mid n}(1+p^{-1})^{-1}.
\tag{168.K20}
\]

One-variable Mellin inversion on that initial line gives

\[
 R_\zeta=\frac1{\zeta(2)}
 \sum_{\substack{n\ge1\\n\ {\rm odd,\ squarefree}}}
 \chi_4(n)\prod_{p\mid n}(1+p^{-1})^{-1}
 \int_0^\infty\mathcal B(n,z)\,dz.
\tag{168.K21}
\]

At \(x=n\), disjointness yields

\[
 \mathcal B(n,z)=e(J\sqrt{nz})
 \sum_m A_{L,X}(n,m)\psi(z-m).
\]

On each nonzero cell \(n,m\asymp L\),

\[
 \frac d{dz}\bigl(2\pi J\sqrt{nz}\bigr)
 =\pi J\sqrt{n/z}\asymp J.
\]

One integration by parts has no boundary term and gives

\[
 \int\psi(z-m)e(J\sqrt{nz})\,dz\ll J^{-1}
\tag{168.K22}
\]

uniformly.  There are \(O(L^2)\) cells and the coefficients in
(168.K21) have modulus at most one.  This proves the residue estimate in
(168.K6).  Since \(L\ll J^{1/2}\), it is smaller than the target.
The remaining shifted integral is exactly (168.K7).

The cardinal interpolation is only an identity device.  It has
\(O(L^2)\) unit-cell complexity, and no analytic smoothing is inferred
from it.

### 3. Radial capacity

This calculation concerns only a favorable recombined smooth/BV control
component, not one cardinal cell.  Put

\[
 x=rw,\qquad z=r/w,\qquad t_+=t_1+t_2,
 \qquad t_-=t_1-t_2.
\]

The radial phase is \(2\pi Jr+t_+\log r\).  Its stationary equation and
band length are (168.K9), and stationary phase gives (168.K10).  The
pointwise-triangle placement therefore gives (168.K11).  The radial
transform has \(L^2\)-norm of scale \(L^{1+2\eta}\), while the granted
fixed-angular arithmetic mean square has norm \(T^{1/2}X^\delta\);
Cauchy gives (168.K11) again.  The epsilon ordering stated after
(168.K11) is therefore valid, but neither absolute placement supplies
the missing structural factor \(\sqrt J\).

No exact coefficient bridge from factorwise functional equations or
approximate functional equations to the accepted Round-162 collar is
asserted.  If the original projector is deliberately reopened by its
accepted Mobius identity and positive physical Poisson is then used, the
accepted collar capacity remains \(\sqrt{JL}X^\varepsilon\), with

\[
 \frac{\sqrt{JL}}{L^{3/2}}
 =\frac{\sqrt J}{L}
 =\frac HL+O(L^{-1}).
\tag{168.K23}
\]

This imported comparison supplies no AFE self-return theorem.

### 4. Fixed-polylogarithmic sector

The normalization and fixed profiles in (168.K2) are bounded on a support
of \(O(L^2)\) ordered pairs, so \(|\mathcal S_{L,1}|\ll L^2\).  If
\(L\le(\log X)^B\), then

\[
 L^{1/2}\le(\log X)^{B/2}\ll_{\varepsilon,B}X^\varepsilon,
\]

which proves (168.K12).  Equations (168.K13)--(168.K14) then follow by
the accepted exact XOR decomposition and triangle inequality.

## First open interface

The exact remaining theorem is (168.K8), or an equivalent endpoint-lawful
physical estimate.  The favorable smooth control needs cancellation
between the stationary phase and the two L-functions before absolute
values; the exact cardinal transform additionally carries its unit-cell
complexity.  The two named absolute placements and the accepted
Mobius-opened positive collar do not provide the target.

The general full scalar and residual remain open, as do all other
few-point channels and collars, hard TOP, BAL, UNBAL, M9--M2, both direct
M1 parents, GAR, endpoint assembly, M9, both bridges, the quarter theorem,
and both exponent ledgers.

## Provenance

The exact scalar and positive collar comparison are inherited from
`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.  The
fixed-\(\kappa\) XOR connector is inherited from
`M9-M2-hard-top-t1-close-opposite-prime-exchange-sector`.  The literal
bounded symbol and endpoint/profile conventions are inherited from
`M9-M2-top-endpoint-actual-symbol-variation` and `H4-Phi-regularity`.
All Euler, cardinal, residue, radial-capacity, and polylogarithmic
arguments above are internal finite or analytic deductions.
