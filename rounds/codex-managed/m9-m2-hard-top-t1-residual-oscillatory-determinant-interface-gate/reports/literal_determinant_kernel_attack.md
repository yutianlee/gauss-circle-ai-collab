# Literal determinant-kernel attack on the K17a residual

## 1. Result

The literal K17a opening admits both an exact multiplicity-one determinant
dictionary and an exact joint endpoint-kernel representation.  Neither
representation, with the presently accepted inputs, proves

\[
 \Re\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil .
\tag{167.1}
\]

More precisely:

1. Every ordered residual divisor incidence maps bijectively to

   \[
   A=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
   \qquad \det A=d'm'-dm=r.
   \tag{167.2}
   \]

   For each factorization \(r=hk\), with
   \(k=2^{v_2(r)}\) and \(h\) odd, the further decomposition into left
   \(\Gamma_2(4,1)\)-orbits is also multiplicity preserving.  The action is
   free because \(r\ne0\).

2. If the literal residual selector, \(\chi _4\)-twist, and square-root
   phase are placed in one endpoint vector, while the determinant,
   even-shift, Fejer, opposing-displacement, and low-\(g\) conditions are
   placed in one directed kernel, then the complete K17a aggregate is one
   quadratic form with one outer real part.  This is the requested joint
   selector-aware oscillatory variable-determinant transform.

3. The exact endpoint transform has Schur upper capacity
   \(L^3X^\varepsilon\).  Schur's test gives no more than

   \[
   \|T_{R_0,\gamma}\|_{2\to2}\ll_\varepsilon LX^\varepsilon,
   \qquad
   \|u_L\|_2^2\ll_\varepsilon L^2X^\varepsilon,
   \tag{167.3}
   \]

   hence \(\left|\langle T_{R_0,\gamma}u_L,u_L\rangle\right|
   \ll L^3X^\varepsilon\).  The missing factor \(L\) must therefore come
   from genuine signed cancellation of the actual vector, not from a
   positive kernel majorant or the accepted energy alone.

4. The Grimmelt--Merikoski 2024 Theorem 10.1 placement stops first at the
   coefficient interface: no admissible left-automorphic coefficient, or
   common \(C^7_\delta\) smooth weight, has been constructed for

   \[
   \lambda_{d'm'}(d')\,\overline{\lambda_{dm}(d)}
   \mathbf 1_{\mathrm{opp}}\mathbf 1_{(d,d')<\gamma L}
   \tag{167.4}
   \]

   with its squarefree rows, selected-prime data, profiles, hard faces,
   endpoints, and zero extension.  The determinant, two-adic source-gcd,
   and fixed \(\chi _4\) seams pass before this failure.

5. The exact source \(\mathcal R_0\) factor on comparable matrix scales
   has base size

   \[
   (\mathsf A\mathsf D)^{1/2}\|\beta\xi\|_2
   \mathcal R_0^{\rm src}\asymp L\|\beta\xi\|_1,
   \tag{167.3a}
   \]

   not unconditionally \(L^2\).  In the explicitly optimistic dense
   top-block model
   \(\|\beta\xi\|_1\asymp H\asymp L/k\), and with the separately
   unproved input
   \(\mathcal K_+^{1/2}\ll k^{1/2}X^\varepsilon\), the summed
   \(\mathcal R_0\) contribution is target-sized before smoothness,
   whereas the source-audited \(\mathcal R_2\) route retains
   \(L^{2+\theta_4+\varepsilon}\).  The phase requires
   \(\delta^{-1}\gtrsim1+Jr/L\), and the published error retains
   \(\delta^{-O(1)}\).  Thus the published bound has no certified slack
   after its smoothness and correlation factors.  No unconditional
   negative-power requirement on \(\mathcal K_+\) is asserted.

6. For the bare source coefficient

   \[
   \alpha_{\rm bare}(A)=\chi_4(a)\chi_4(b),
   \tag{167.3b}
   \]

   the induced source character is principal, but the finite principal
   orbit sum is exactly zero for every \(k=2^v\).  Hence the bare 2024
   main term vanishes.  Any selector-dependent automorphic coefficient
   changes that orbit sum and requires a new calculation; a Part-I model
   has its own principal component.

7. Grimmelt--Merikoski 2025 Part I does not repair the gap.  Its general
   theorem could accept the endpoint data only after an exact relative
   automorphic-kernel realization of the raw directed literal kernel, with
   no extra orbit pairs or cross terms.  No such realization is proved.
   The theorem formally permits a complex oscillatory \(C^{10}_\delta\)
   function, but pays its derivatives through
   \(\delta^{-O(1)}\).  It also separates a principal component and leaves
   two nonnegative selector/phase discrepancy autocorrelations.  The
   accepted energy does not supply their missing factor \(L\); no exact
   theorem-side \(L^3\) return is claimed before the kernel is constructed.

Thus this report proves an exact opening and a route-scoped no-go, not
K17a.  The sole terminal label is
**oscillatory_determinant_interface_no_go**.

## 2. Exact statement and hypotheses

Assume the accepted hard-TOP residual setting:

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil ,
\tag{167.5}
\]

and fix \(0<\gamma<1\).  For squarefree
\(N=2^{\nu_N}M_N\asymp L^2\), \(M_N\) odd, let

\[
 \rho_N(d)=
 \begin{cases}
  1,&\text{if no pair is selected},\\
  1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
       +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d},
       &\text{if }p_N,q_N\text{ are selected},
 \end{cases}
\tag{167.6}
\]

and retain the accepted exact coefficient

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}\chi_4(d)\lambda_N(d).
\tag{167.7}
\]

Here \(\lambda_N(d)\) contains the supported squarefree row,
\((L^2/N)^{3/4}\), the neither/both selector, all parity branches,
profiles, hard-point values, literal endpoints, and zero extension.
On every nonzero incidence,

\[
 d,m=N/d\asymp L,\qquad |\lambda_N(d)|\ll1,
\tag{167.8}
\]

and the literal product shell has cardinality \(O(L^2)\).  The accepted
coefficient energy is

\[
 D_L=\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{167.9}
\]

The frozen object is

\[
\begin{aligned}
\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
=
\sum_{\substack{1\le r<R_0\\2\mid r}}
\left(1-\frac r{R_0}\right)
\sum_{\substack{N,N+r\in\mathcal I_L^{\rm lit}}}
&e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\\
\times
\sum_{\substack{d\mid N,\ d'\mid N+r\\d,d'\ {\rm odd}\\
(d'-d)(m'-m)<0\\(d,d')<\gamma L}}
&\chi_4(d')\chi_4(d)
\lambda_{N+r}(d')\overline{\lambda_N(d)},
\end{aligned}
\tag{167.10}
\]

where \(m=N/d\), \(m'=(N+r)/d'\).  Equivalently, after eliminating
\(N\) and \(r\), the one outer real part in (167.1) surrounds exactly

\[
\sum_{\substack{d,d'\ {\rm odd},\ m,m'\ge1\\
r=d'm'-dm\in2\mathbb Z,\ 0<r<R_0\\
(d'-d)(m'-m)<0,\ (d,d')<\gamma L}}
\left(1-\frac r{R_0}\right)
\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\tag{167.11}
\]

All support restrictions are literal; no absolute value is inserted
inside the shift, divisor, determinant, selector, cell, or endpoint
sum.

Define the endpoint incidence set

\[
\mathcal E_L=
\{x=(d,m):d\ {\rm odd},\ dm\in\mathcal I_L^{\rm lit},
\ d,m\asymp L,\ \lambda_{dm}(d)\ne0\},
\tag{167.12}
\]

with product map \(n(x)=dm\), and set

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}).
\tag{167.13}
\]

For \(x=(d,m)\), \(y=(d',m')\), define the real directed kernel

\[
\begin{aligned}
T_{R_0,\gamma}(y,x)
=&
\left(1-\frac{n(y)-n(x)}{R_0}\right)
\mathbf1_{\,0<n(y)-n(x)<R_0}
\mathbf1_{\,2\mid n(y)-n(x)}\\
&\times\mathbf1_{\,(d'-d)(m'-m)<0}
\mathbf1_{\,(d,d')<\gamma L}.
\end{aligned}
\tag{167.14}
\]

Use the convention

\[
 (Tu)(x)=\sum_{y\in\mathcal E_L}T(y,x)u(y),\qquad
 \langle Tu,u\rangle=\sum_x(Tu)(x)\overline{u(x)}.
\tag{167.15}
\]

Then the exact joint transform claimed in Section 1 is

\[
 \boxed{
 \mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
 =\langle T_{R_0,\gamma}u_L,u_L\rangle .
 }
\tag{167.16}
\]

The proposed source placement uses
\[
 r=hk,\qquad k=2^{v_2(r)},\qquad h\ {\rm odd},
\qquad q_1=4,\quad q_2=1,\quad q=4,
\tag{167.17}
\]
and the matrix in (167.2).  Its ambient source set and group are

\[
\mathcal M^{\rm src}_{2,h,k}=
\left\{
\begin{pmatrix}a&b\\c&d_0\end{pmatrix}\in M_2(\mathbb Z):
ad_0-bc=hk,\ (a,c,k)=(b,d_0,k)=1
\right\},
\tag{167.17a}
\]

\[
\Gamma=\Gamma_2(4,1)=
\left\{
\begin{pmatrix}p&q\\s&t\end{pmatrix}\in{\rm SL}_2(\mathbb Z):
4\mid q
\right\}.
\tag{167.17b}
\]

The claim below is only that the exact
dictionary and preliminary arithmetic seams fit the source skeleton,
not that the source theorem applies.

## 3. Proof and derivation

### 3.1 Literal opening and multiplicity

Expanding (167.7) at \(N\) and \(N+r\) gives one ordered pair of odd
divisors \((d,d')\) for every term.  Put \(m=N/d\) and
\(m'=(N+r)/d'\).  Then

\[
 d'm'-dm=(N+r)-N=r.
\tag{167.18}
\]

Conversely, any positive quadruple \((d',d,m,m')\) satisfying all
conditions in (167.11) determines exactly
\[
 N=dm,\quad N+r=d'm',\quad r=d'm'-dm,
\tag{167.19}
\]
and hence exactly one ordered divisor-incidence term in (167.10).
There is no divisor-ordering quotient: \(d\) belongs to the lower
product and \(d'\) to the upper product.  Therefore

\[
 (d',d,m,m')\longleftrightarrow
 \begin{pmatrix}d'&d\\m&m'\end{pmatrix}
\tag{167.20}
\]
is a bijection from literal ordered incidences to literal matrices of
determinant \(r\).  Reading the four entries is the inverse map.  This
proves exact multiplicity one.

For later source notation write
\[
 (a,b,c,d_0)=(d',d,m,m').
\tag{167.21}
\]
For fixed \(h,k\), let \(\mathscr M^{\rm lit}_{h,k}\) be the subset of
\(\mathcal M^{\rm src}_{2,h,k}\) whose entries form a matrix in
(167.20), including every indicator and zero-extension condition in
(167.11).  The source column-primitivity conditions do not delete a
literal matrix: \(k\) is a power of \(2\), while \(a=d'\) and \(b=d\)
are odd.  Its literal weight is

\[
\begin{aligned}
W_{h,k}(A)=&
\left(1-\frac{hk}{R_0}\right)
\chi_4(a)\chi_4(b)
\lambda_{ad_0}(a)\overline{\lambda_{bc}(b)}
e\!\left(J(\sqrt{ad_0}-\sqrt{bc})\right)\\
&\times
\mathbf1_{(a-b)(d_0-c)<0}
\mathbf1_{(a,b)<\gamma L}.
\end{aligned}
\tag{167.22}
\]

All shell, squarefree, parity, profile, hard-face, and endpoint data in
this display remain inside the two \(\lambda\)'s and the definition of
\(\mathscr M^{\rm lit}_{h,k}\).

The group \(\Gamma\le{\rm SL}_2(\mathbb Z)\) in (167.17b) preserves the
determinant and the gcd of the entries of each column, hence acts on
\(\mathcal M^{\rm src}_{2,h,k}\).  Its left action is free.  Indeed, if
\(\sigma A=A\), then \(A\) is invertible over \(\mathbb Q\), so
multiplying by \(A^{-1}\) gives \(\sigma=I\).  Choose one representative
\(A_{\mathcal O}\) for every orbit in
\(\Gamma\backslash\mathcal M^{\rm src}_{2,h,k}\).  Freeness and
(167.20) give the exact orbit opening

\[
\sum_{A\in\mathscr M^{\rm lit}_{h,k}}W_{h,k}(A)
=
\sum_{\mathcal O\in\Gamma\backslash\mathcal M^{\rm src}_{2,h,k}}
\ \sum_{\substack{\sigma\in\Gamma\\
\sigma A_{\mathcal O}\in\mathscr M^{\rm lit}_{h,k}}}
W_{h,k}(\sigma A_{\mathcal O}).
\tag{167.23}
\]

No stabilizer factor and no orbit multiplicity occur.  In particular,
the target remains

\[
\Re\sum_{\nu\ge1}
\sum_{\substack{h\ge1\ {\rm odd}\\h2^\nu<R_0}}
\sum_{\mathcal O}
\sum_{\substack{\sigma\in\Gamma\\
\sigma A_{\mathcal O}\in\mathscr M^{\rm lit}_{h,2^\nu}}}
W_{h,2^\nu}(\sigma A_{\mathcal O}),
\tag{167.24}
\]
with the real part outside every \(h,k\), orbit, and matrix sum.

### 3.2 Parity, source gcd, and character seams

Since \(d,d'\) are odd and \(r\) is even, \(N\) and \(N+r\) have the
same parity.  On squarefree support there are only two branches:

- odd--odd, where \(m,m'\) are odd;
- even--even, where \(m,m'\) are exactly twice an odd number.

In the second branch both products are \(2\bmod4\), so \(4\mid r\).
With \(k=2^{v_2(r)}\) and \(h=r/k\), \(h\) is odd and
\((h,kq)=1\) for \(q=4\).  Moreover,

\[
 (a,c,k)=(d',m,k)=1,\qquad
 (b,d_0,k)=(d,m',k)=1,
\tag{167.25}
\]
because \(a=d'\) and \(b=d\) are odd.  These are precisely the
preliminary source gcd conditions in the determinant skeleton.  They
must not be confused with the target filter
\[
 g=(d,d')=(b,a)<\gamma L,
\tag{167.26}
\]
which is a separate rough cross-entry condition and is not supplied by
(167.25).

The fixed twist
\(\alpha_{\rm bare}(A)=\chi_4(a)\chi_4(b)\) is compatible with the
\((q_1,q_2)=(4,1)\) congruence skeleton.  If
\(\bigl(\begin{smallmatrix}p&4q\\s&t\end{smallmatrix}\bigr)\) is an
allowed left multiplier, then

\[
\chi_4(pa+4qc)\chi_4(pb+4qd_0)
=\chi_4(p)^2\chi_4(a)\chi_4(b)
=\alpha_{\rm bare}(A).
\tag{167.26a}
\]

Thus the induced source character is \(\chi_4^2\), hence principal.
Nevertheless, its finite principal orbit coefficient vanishes.  The six
left cosets in
\(\Gamma\backslash{\rm SL}_2(\mathbb Z)\cong
\mathbb P^1(\mathbb Z/4\mathbb Z)\) have top-row representatives

\[
(x,1)\ (x=0,1,2,3),\qquad(1,0),\ (1,2),
\tag{167.26b}
\]

and the left Hermite classes in
\({\rm SL}_2(\mathbb Z)\backslash\mathcal M^{\rm src}_{2,1,k}\)
are represented by

\[
\sigma_\ell=\begin{pmatrix}1&\ell\\0&k\end{pmatrix},
\qquad \ell\bmod k,\quad(\ell,k)=1,
\tag{167.26c}
\]

with \(\ell=0\) for \(k=1\).  A top row \((x,y)\) becomes
\((x,x\ell+yk)\).  Directly, the six terms sum to zero for \(k=1\);
for \(k=2\), the four \((x,1)\) classes contribute \(-2\) and the last
two contribute \(+2\); and for \(4\mid k\), each odd \(\ell\) contributes
\(4\chi_4(\ell)\), whose sum over units modulo \(k\) is zero.  Hence

\[
\boxed{
\sum_{\tau\in\Gamma\backslash\mathcal M^{\rm src}_{2,1,k}}
\alpha_{\rm bare}(\tau)=0
\qquad(k=2^v).}
\tag{167.26d}
\]

This exact cancellation applies only while the source coefficient
remains \(\alpha_{\rm bare}\).  It must be recomputed for any
selector-dependent automorphic coefficient and does not settle a
Part-I principal component.

### 3.3 The joint endpoint-kernel transform and its capacity

Substituting (167.13) and (167.14) into (167.15) gives

\[
\begin{aligned}
\langle T_{R_0,\gamma}u_L,u_L\rangle
=\sum_{x=(d,m)}\sum_{y=(d',m')}
&\left(1-\frac{d'm'-dm}{R_0}\right)
\mathbf1_{\rm literal\ K17a}(y,x)\\
&\times\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\end{aligned}
\tag{167.27}
\]
which is exactly (167.11).  Thus (167.16) is proved, with one outer real
part and all even shifts handled simultaneously.  The associated
determinant is

\[
 A(y,x)=\begin{pmatrix}d_y&d_x\\m_x&m_y\end{pmatrix},
 \qquad \det A(y,x)=n(y)-n(x).
\tag{167.28}
\]

The endpoint energy is incidence energy, not the coefficient energy
\(D_L\); independently of any cancellation inside \(c_N^{\rm rem}\),

\[
\begin{aligned}
\|u_L\|_2^2
&=\sum_{N\in\mathcal I_L^{\rm lit}}
  \sum_{\substack{d\mid N\\d\ {\rm odd}}}|\lambda_N(d)|^2\\
&\ll \sum_{N\in\mathcal I_L^{\rm lit}}\tau(N)
\ll_\varepsilon L^2X^\varepsilon.
\end{aligned}
\tag{167.29}
\]

For a fixed \(x\) and fixed \(r\), there are at most \(\tau(n(x)+r)\)
possible endpoints \(y\); every literal filter only deletes endpoints.
Consequently

\[
 \sup_x\sum_y|T_{R_0,\gamma}(y,x)|
 \ll_\varepsilon R_0X^\varepsilon
 \ll_\varepsilon LX^\varepsilon.
\tag{167.30}
\]

The same argument backwards from \(y\) gives

\[
 \sup_y\sum_x|T_{R_0,\gamma}(y,x)|
 \ll_\varepsilon LX^\varepsilon.
\tag{167.31}
\]

For explicit epsilon relabelling, fix the final \(\varepsilon>0\) and
apply the divisor bound in (167.29)--(167.31) with
\(\eta=\varepsilon/2\).  Schur's test gives
\(\|T_{R_0,\gamma}\|_{2\to2}\ll LX^\eta\), while
\(\|u_L\|_2^2\ll L^2X^\eta\).  Hence

\[
 |\langle T_{R_0,\gamma}u_L,u_L\rangle|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{167.32}
\]

This reproduces the accepted direct opened-incidence upper capacity.  It is a
factor \(L\) above (167.1).  Since the kernel is directed and not made
positive by symmetrization, (167.32) is only a positive majorant; it
does not move the real part inward and does not falsify K17a.

### 3.4 Attempted Grimmelt--Merikoski 2024 placement

Theorem 10.1 of Grimmelt--Merikoski 2024 estimates one full
\((h,k)\)-aggregate of determinant orbits.  In the notation imported by
the Round-166 primary-source audit, its error has the form

\[
 Z^{O(\eta)}\delta^{-O(1)}
 (\mathsf A\mathsf D)^{1/2}
 \|\beta\xi\|_2\mathcal K_+^{1/2}
 \left(\mathcal R_0^{\rm src}
       +\min(\mathcal R_1^{\rm src},\mathcal R_2^{\rm src})\right),
\tag{167.33}
\]

where

\[
 \mathcal R_0^{\rm src}
 =\frac{\|\beta\xi\|_1\mathsf A^{1/2}}
 {\|\beta\xi\|_2q_1^{1/2}\mathsf C^{1/2}},
\tag{167.34}
\]

\(\delta\) is the source smoothness parameter, \(\mathcal K_+\) is its
short-kernel autocorrelation input, and a principal-character main term
is separate.  The symbols \(\mathsf A,\mathsf C,\mathsf D\) are source
scale parameters, not entries of (167.2).

The exact weight (167.22) cannot presently be placed in the theorem.
If the rough factor is placed in the source coefficient \(\alpha\), one
must prove the prescribed left-automorphy for

\[
 \lambda_{ad_0}(a)\overline{\lambda_{bc}(b)}
 \mathbf1_{(a-b)(d_0-c)<0}
 \mathbf1_{(a,b)<\gamma L}.
\tag{167.35}
\]

That expression depends on both cross-corner products, on selected
primes attached separately to those products, and on sharp literal
support.  No accepted identity makes it a member of the source class
\(\mathcal A(4,1,\chi,\xi)\).  If instead it is placed in the test
function, the squarefree masks, selector jumps, gcd cutoff, hard faces,
and zero-extension endpoints are not a single \(C^7_\delta\) weight.
No exact cell/Möbius decomposition with total target-safe norm has been
proved.  This is the first source-call failure.

For \(0<\gamma<1/2\), even the direct placement of the low-top-row-gcd
factor has an explicit ambient obstruction.  Choose odd
\(\gamma L\le G<L/2\), odd \(T\asymp L\), and put

\[
A_0=\begin{pmatrix}G&3G\\T&3T+2\end{pmatrix},
\qquad
u=\begin{pmatrix}1&4\\0&1\end{pmatrix}\in\Gamma.
\tag{167.35a}
\]

Then \(\det A_0=2G<R_0\), both \(A_0\) and \(uA_0\) have opposing
displacements, and

\[
(G,3G)=G\ge\gamma L,\qquad
(G+4T,3G+12T+8)=1.
\tag{167.35b}
\]

The second equality follows because the gcd divides \(8\) and both
entries are odd.  Thus
\(\alpha_{\rm bare}\mathbf1_{(a,b)<\gamma L}\) is not left
\(\Gamma\)-invariant.  This is a global source-coefficient witness, not
a proof that both matrices lie in the exact squarefree/profile support.
It does not rule out an automorphic extension agreeing only on literal
support.  If \(\gamma\ge1/2\), then \(g=(d,d')\mid r\), \(g\) is odd,
and \(r/g\) is even, so \(g\le r/2<L/2\le\gamma L\); the cutoff is
identically one and this witness is irrelevant.  The residual-selector
and phase gaps remain for every \(0<\gamma<1\).

The oscillatory phase creates an independent quantitative failure after
one conditionally smooths the rough data.  Since \(ad_0-bc=r\), write

\[
 \Phi_r(a,d_0)
 =J\{\sqrt{ad_0}-\sqrt{ad_0-r}\}.
\tag{167.36}
\]

Direct differentiation gives

\[
 \partial_a\Phi_r
 =-\frac{Jd_0r}
 {2\sqrt{ad_0}\sqrt{ad_0-r}
  \{\sqrt{ad_0}+\sqrt{ad_0-r}\}},
\tag{167.37}
\]

and the analogous formula with \(a\) in the numerator for
\(\partial_{d_0}\Phi_r\).  On the literal scale all four entries are
\(\asymp L\), so

\[
 L|\partial_a\Phi_r|+L|\partial_{d_0}\Phi_r|
 \asymp \frac{Jr}{L}.
\tag{167.38}
\]

Already the first normalized derivative therefore forces

\[
 \delta^{-1}\gtrsim1+\frac{Jr}{L}.
\tag{167.39}
\]

On a block \(r\asymp L\), this becomes
\(\delta^{-1}\gtrsim J\).  The assumption \(L\le J^{1/2}\) gives
\(J\ge L^2\), so any fixed positive uncompensated power of this
seminorm is not an \(X^\varepsilon\) loss.  The published theorem leaves
that final power inside \(\delta^{-O(1)}\), rather than exposing a
numerical exponent.

The Fejer factor is not the first difficulty: on a localized
\((h,k)\)-block,
\[
 1-\frac{hk}{R_0}=1-\frac{h}{R_0}k
\tag{167.40}
\]
is a sum of two separable weights, and the \(2\)-adic \(k\)-blocks cost
only \(O(\log L)\).  The phase is different.  In normalized variables

\[
x=\frac a{\sqrt r},\qquad y=\frac c{\sqrt r},\qquad
z=\frac{d_0}{\sqrt r},\qquad
\frac b{\sqrt r}=\frac{xz-1}{y},
\tag{167.40a}
\]

it is

\[
e\!\left(J\sqrt r\,G(x,z)\right),\qquad
G(x,z)=G_0(xz),\qquad G_0(t)=\sqrt t-\sqrt{t-1}.
\tag{167.40b}
\]

If on a common open normalized cell it factored as a determinant
coefficient times one common \(f(x,y,z)\) for distinct
\(r_1,r_2\), their ratio would be

\[
e\!\left(J(\sqrt{r_1}-\sqrt{r_2})G(x,z)\right),
\tag{167.40c}
\]

which is nonconstant because
\(G_0'(t)=(2\sqrt t)^{-1}-(2\sqrt{t-1})^{-1}\ne0\).
Thus the natural continuous phase family
is not rank one in determinant and archimedean variables.  This does
not exclude a specially constructed \(C^7\) interpolant on the discrete
literal samples, whose normalized supports need not intersect, nor a
controlled-rank expansion.  No such interpolation or expansion with a
target-safe seminorm has been proved.

Freezing \(r\), applying the source theorem separately, and summing its
errors would move absolute values inside the \(r\)-sum.  The cited source
provides no target-size bound for that absolute error sum, so this is not
a proof of (167.1); it is not asserted that every such sum must lose an
exact factor \(L\).

### 3.5 Restored source power ledger

On comparable source scales
\(\mathsf A,\mathsf C,\mathsf D\asymp L\), the exact
\(\mathcal R_0^{\rm src}\) algebra gives

\[
\begin{aligned}
(\mathsf A\mathsf D)^{1/2}
\|\beta\xi\|_2\mathcal R_0^{\rm src}
&=
\frac{\mathsf A\mathsf D^{1/2}}
{q_1^{1/2}\mathsf C^{1/2}}\|\beta\xi\|_1\\
&\asymp L\|\beta\xi\|_1.
\end{aligned}
\tag{167.41}
\]

This is the general base ledger.  It is \(L^2\) only under an additional
dense-weight hypothesis \(\|\beta\xi\|_1\asymp L\).  The literal shell,
selector, opposing sector, and low-\(g\) filter do not prove that any
particular \(k=2\), \(h\asymp L\) block is nonempty or dense.  Therefore
neither \(L^2\) nor any compensating negative power of
\(\mathcal K_+\) is an unconditional consequence of (167.41).

For comparison with the published source power only, impose the
explicitly optimistic model

\[
\mathsf A=\mathsf C=\mathsf D\asymp L,\quad
k=2^v,\quad \mathsf H\asymp L/k,\quad
|\beta_h\xi_h|\asymp1\ \hbox{on }\asymp\mathsf H\hbox{ indices},
\quad
\mathcal K_+^{1/2}\ll k^{1/2}X^\varepsilon.
\tag{167.42}
\]

Then

\[
\|\beta\xi\|_2\asymp\mathsf H^{1/2},\qquad
\frac{\|\beta\xi\|_1}{\|\beta\xi\|_2}
\asymp\mathsf H^{1/2},\qquad
\mathcal R_0^{\rm src}\asymp\mathsf H^{1/2}.
\tag{167.43}
\]

Ignoring the adjustable \(Z^{O(\eta)}\) factor, the
\(\mathcal R_0^{\rm src}\) branch of the source upper bound is

\[
E^{(0)}_{\mathsf H,k}
\ll_\varepsilon
\delta^{-O(1)}
L\mathsf H k^{1/2}X^\varepsilon
\asymp
\delta^{-O(1)}L^2k^{-1/2}X^\varepsilon.
\tag{167.44}
\]

The source-audited exceptional-spectrum factors satisfy, at the same
top scale,

\[
\mathcal R_2^{\rm src}
\asymp L^{1/2+\theta_4}k^{-1/2},
\qquad
\mathcal R_1^{\rm src}
\asymp L^{1/2+\vartheta_4+\theta_4}
k^{-1/2-\vartheta_4},
\tag{167.45}
\]

up to lower-order \(1+\) terms and fixed level factors.  Thus the
displayed route through
\(\min(\mathcal R_1^{\rm src},\mathcal R_2^{\rm src})\) has size

\[
E^{(2)}_{\mathsf H,k}
\ll_\varepsilon
\delta^{-O(1)}L^{2+\theta_4}k^{-1/2}X^\varepsilon.
\tag{167.46}
\]

Because \(\sum_{k=2^v}k^{-1/2}\ll1\), the conditional
\(\mathcal R_0\) terms sum at \(L^2\) if
\(\delta^{-O(1)}\) is harmless, while the displayed
\(\mathcal R_2\) route certifies only
\(\delta^{-O(1)}L^{2+\theta_4+\varepsilon}\).  The published
unconditional exponent \(\theta_4\le7/64\) does not certify
\(\theta_4=0\).

This is an upper-bound certification ledger, not a lower bound on the
literal sum.  Its assumed \(\mathcal K_+\) estimate is not proved for
the residual selector, and the final exponent in
\(\delta^{-O(1)}\) is not exposed by the source.  Equation (167.39)
shows that a fixed positive uncompensated seminorm power is not
\(X^\varepsilon\)-safe; it does not force an unconditional
negative-power \(\mathcal K_+\) estimate or exclude a new compensating
mechanism.

The 2024 main-term ledger is more favorable for the bare coefficient:
equation (167.26d) makes its finite orbit coefficient zero for every
two-power \(k\), so the bare principal main term vanishes exactly.  If
the project selectors are incorporated into a different legal
automorphic coefficient, the orbit sum must be recomputed.  If it is
then nonzero, the integral core has dimensional scale
\(\mathsf A\mathsf D/(\mathsf H\mathsf K)\), but no nonzero lower bound
or target-size estimate follows from that capacity calculation.

Finally, the source placement has not priced:

- Möbius opening of both squarefree conditions;
- selected-prime and no-pair cells on both products;
- the target cutoff \((a,b)<\gamma L\);
- the sharp opposing-displacement boundary;
- literal shell and hard-profile crossings;
- zero-extension endpoints and completion.

The finite number of hard faces is not an \(O(1)\) contribution: a face
can carry \(O(L^2X^\varepsilon)\) divisor incidences.  Smoothing a face
also feeds its transition width into the same
\(\delta^{-O(1)}\) loss.  The exact endpoint transform (167.16) avoids
creating these errors, but its presently available bound is only
(167.32).

### 3.6 Attempted 2025 Part-I kernel placement

The endpoint factorization in (167.27) is the natural way to exploit the
arbitrary compactly supported linear functionals allowed by
Grimmelt--Merikoski 2025 Part I: use the actual endpoint vector \(u_L\)
on both sides, and ask a raw relative automorphic kernel \(K_F\) to
supply \(T_{R_0,\gamma}(y,x)\), where
\(K_F=\mathcal K_{\Gamma,\chi}F\).  This first requires an embedding

\[
\iota:\mathcal E_L\longrightarrow G={\rm SL}_2(\mathbb R)
\tag{167.47a}
\]

and the compactly supported finite functional

\[
\langle\varphi\rangle_{\alpha_u}
=\sum_{x\in\mathcal E_L}u_L(x)\varphi(\iota(x)).
\tag{167.47b}
\]

One must then construct \(F\) with the correct orientation such that

\[
(K_F)(\iota(x),\iota(y))=T_{R_0,\gamma}(y,x)
\tag{167.47c}
\]

for every literal endpoint pair and with no other relative-orbit
contributions.  The resulting raw identity would be

\[
 \langle\alpha_u\mid K_F\mid\alpha_u\rangle
 =\langle T_{R_0,\gamma}u_L,u_L\rangle
\tag{167.48}
\]

with the determinant interval, even parity, Fejer factor, opposing
displacements, target gcd, literal endpoints, and zero outside the shell
all represented, and with no unwanted relative-orbit pairs or cross
terms.

No such \(\iota,F\) are constructed.  The theorem controls the
discrepancy kernel rather than the raw kernel.  Even if (167.48) were
granted, one must separate

\[
\langle\alpha_u\mid K_F\mid\alpha_u\rangle
=\langle\alpha_u\mid\Delta F\mid\alpha_u\rangle
+\frac{\mathbf1_{\chi\ {\rm principal}}}{|\Gamma\backslash G|}
\left|\langle1\rangle_{\alpha_u}\right|^2\int_G F(g)\,dg
\tag{167.48a}
\]

and estimate the principal component.  The bare 2024 orbit calculation
(167.26d) does not automatically evaluate this different Part-I model.
The general Part-I bound then contains two nonnegative
automorphic-kernel discrepancy quadratic forms of the endpoint
functionals.  For the intended endpoint data they are selector/phase
autocorrelations.  The accepted incidence energy controls their diagonal
mass but supplies no K17a-specific factor-\(L\) saving.  Before an exact
kernel is constructed, the source does not certify that these forms have
exactly \(L^3X^\varepsilon\) capacity; they are simply new unproved
positive correlations.

Part I formally permits a complex oscillatory function \(F\).  The word
“non-oscillatory” in the paper title is not a theorem hypothesis.  If
the square-root phase is placed in \(F\), however, its ten derivatives
are charged through \(C^{10}_\delta\) and the final
\(\delta^{-O(1)}\) factor.  Moving the phase to endpoint functionals
avoids that archimedean derivative cost only after the raw identity
(167.48) is proved.  The determinant corollary is not a shortcut,
because it restores left invariance and an admissible
\(C^{10}_\delta\) weight.

### 3.7 A small-shift control sector

For any fixed \(B>0\), put
\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\}.
\tag{167.49}
\]
The complete literal sector of (167.11) with \(r\le R_{\log}\) is
target-safe by direct counting:

\[
\begin{aligned}
\left|\mathfrak C^{\rm rem}_{r\le R_{\log}}\right|
&\le
\sum_{\substack{r\le R_{\log}\\2\mid r}}
\sum_{N\in\mathcal I_L^{\rm lit}}
\tau(N)\tau(N+r).
\end{aligned}
\tag{167.49a}
\]

Every selector, parity, opposing-displacement, low-\(g\), endpoint, and
Fejer condition only deletes or weights these literal incidences.
For explicit epsilon relabelling, fix the desired final
\(\varepsilon>0\).  Since \(N,N+r\ll X\), use

\[
\tau(n)\ll_\varepsilon X^{\varepsilon/4},
\qquad
(\log X)^B\ll_{\varepsilon,B}X^{\varepsilon/2}.
\tag{167.49b}
\]

There are \(O(L^2)\) product sites, so (167.49a) gives

\[
\boxed{
\left|\mathfrak C^{\rm rem}_{r\le R_{\log}}\right|
\ll_{\varepsilon,B}L^2X^\varepsilon.}
\tag{167.50}
\]

Equation (167.50) is an owner-complete sanity sector.  It covers only
\(X^{o(1)}\) shifts when \(L\) is a genuine power scale and supplies no
fixed-power advance toward the required \(r\asymp L\) stratum.  If
\(R_0-1\le(\log X)^B\), it instead covers the full shift interval by
the same estimate.  It is not the terminal result and does not alter the
no-go label.

## 4. First doubtful or unproved step

The first unproved step is not the determinant map, orbit multiplicity,
two-adic split, source gcd, fixed character, or Fejer separability.
It is the following exact source-to-literal interface.

**Missing lemma \(\operatorname{ODK}_{\rm K17a}(L,J,R_0,\gamma)\).**
There is an \(X^\varepsilon\)-cost family of source-admissible orbit
pieces \(\tau\) whose signed sum is exactly (167.24), with:

1. a coefficient in the required left-automorphic class, or an exact
   Part-I relative-kernel realization, retaining the two actual
   \(\lambda\)'s and producing no extra matrix pairs;
2. one common variable-determinant aggregate over all even \(r<R_0\),
   so that no fixed-\(r\) absolute value is introduced;
3. a bounded- or \(X^{o(1)}\)-rank family of smooth functions carrying
   the square-root phase, Fejer factor, shell, opposing displacement,
   target gcd, and literal endpoints with their true seminorms, or a
   target-safe discrete interpolation of those data; and
4. the total bound

\[
\begin{aligned}
\sum_\tau\Bigl(
 |{\rm MT}_\tau|
 &+Z_\tau^{O(\eta)}\delta_\tau^{-O(1)}
 (\mathsf A_\tau\mathsf D_\tau)^{1/2}
 \|\beta_\tau\xi_\tau\|_2
 \mathcal K_{\tau,+}^{1/2}\\
 &\quad\times
 \{\mathcal R_{\tau,0}^{\rm src}
 +\min(\mathcal R_{\tau,1}^{\rm src},
       \mathcal R_{\tau,2}^{\rm src})\}
 +{\rm Boundary}_\tau+{\rm Completion}_\tau
 \Bigr)
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{167.51}
\]

No accepted theorem proves item 1.  This is the first exact failure.
Items 2--4 show that merely postulating item 1 would still not close the
target: (167.39) and the conditional ledger (167.41)--(167.46) leave
the published seminorm, orbit-correlation, exceptional-spectrum, cell,
and boundary powers uncertified.  On pieces retaining
\(\alpha_{\rm bare}\), the 2024 main term is zero by (167.26d); every
modified automorphic coefficient requires a new orbit-sum calculation.

For the Part-I formulation, the corresponding first missing statement is
the raw identity (167.48), followed by separation of (167.48a) and
target-size bounds for both nonnegative discrepancy autocorrelations.
Calling the general theorem without these facts is circular: those
autocorrelations retain new selector/phase correlations that are not
bounded by the accepted endpoint energy.

This is a route-scoped no-go.  It rules out direct black-box closure by
the audited 2024 Theorem 10.1 placement, its fixed-\(r\) triangle
variant, the presently available 2025 Part-I positive-autocorrelation
placement, and Schur control of the exact endpoint kernel.  It does not
rule out a bespoke signed determinant trace formula, a new
selector-aware orbit-correlation theorem, or another joint
variable-determinant mechanism.

## 5. Required control tests and outcomes

1. **literal_residual_selector_and_multiplicity — PASS.**  Equations
   (167.6)--(167.11) retain the no-pair value and the selected
   neither/both incidences exactly.  The matrix inverse reads its four
   entries, proving multiplicity one.

2. **determinant_two_adic_gcd_character_dictionary — PASS FOR THE
   PRELIMINARY SKELETON.**  Equations (167.17), (167.20), and
   (167.25) give the exact determinant and source gcd conditions.
   Equations (167.17a)--(167.17b) define the ambient determinant set and
   acting group.  The fixed \(\chi_4\)-twist is compatible.  The target gcd
   \((d,d')<\gamma L\) remains a distinct rough filter and is not
   silently identified with a source gcd hypothesis.

3. **one_outer_real_part_and_variable_r_aggregate — PASS FOR THE EXACT
   TRANSFORM; FAIL FOR THE SOURCE CALL.**  Equations (167.16) and
   (167.24) retain one outer real part.  The source has no proved common
   rank-one continuous test function or target-safe discrete
   interpolation for the \(hk\)-dependent phase; fixed-\(r\) triangle
   summation is not used.

4. **oscillatory_phase_C7_seminorm — RED AS A SOURCE CERTIFICATE.**  The exact derivative
   calculation (167.37)--(167.39) requires
   \(\delta^{-1}\gtrsim1+Jr/L\), reaching \(J\) for \(r\asymp L\).
   A fixed positive uncompensated seminorm power is not target-safe, while
   the published exponent in \(\delta^{-O(1)}\) is not explicit.

5. **automorphic_or_smooth_coefficient_class — RED, FIRST FAILURE.**
   The cross-product selector multiplier (167.35) has neither a proved
   left-automorphic realization nor a single admissible smooth
   realization.

6. **principal_main_term_and_K_plus — BARE MAIN TERM PASS; MODIFIED
   INTERFACE RED.**  Equation (167.26d) proves exact vanishing of the
   bare 2024 orbit coefficient for every \(k=2^v\).  A
   selector-dependent automorphic coefficient or Part-I model requires
   recomputation.  No K17a estimate proves the source
   \(\mathcal K_+\) hypothesis.

7. **orbit_correlation_and_residual_norms — RED.**  The endpoint norm
   is (167.29), but it does not estimate the source orbit correlation or
   the two Part-I discrepancy autocorrelations with the missing
   factor \(L\).  Ambient selector balance does not estimate the actual
   weighted cross-product correlations.

8. **cells_Mobius_boundaries_and_completion — RED.**  The exact kernel
   retains them without error, but no source-admissible decomposition
   with total cost \(X^\varepsilon\) is proved.  Hard faces may each
   support target-many incidences.

9. **phase_aligned_filter_erased_control — RED AS A CANCELLATION
   CLAIM, PASS AS A FALSE-CONTROL CHECK.**  With a selected pair, the
   unweighted ambient residual character mass is zero, but unequal
   amplitudes and disjoint physical supports prevent transfer of that
   identity to (167.11).  With no selected pair and all odd primes
   \(1\bmod4\), the ambient mass is wholly positive.  Moreover, on
   accepted even cofactor rows the \(\chi_4\)-product is frozen.  Hence
   no accepted identity shows that the literal selector defeats a
   phase-aligned, filter-erased positive-capacity control.  Conversely,
   an arbitrary aligned product-site array is not a literal K17a
   counterexample because it has no exact opposing-displacement and
   low-\(g\) incidence lift.  No counterexample is claimed here.

10. **minimal_scale_power_ledger — RED FOR THE PROPOSED CLOSURE.**
    The exact capacity is \(L^3X^\varepsilon\) versus target
    \(L^2X^\varepsilon\).  The general source
    \(\mathcal R_0\) base is \(L\|\beta\xi\|_1\), not automatically
    \(L^2\).  Under the explicit dense-block and optimistic
    \(\mathcal K_+\) assumptions, its \(\mathcal R_0\) part is
    target-sized before smoothness, while the displayed
    \(\mathcal R_2\) route retains \(L^{\theta_4}\) and
    \(\delta^{-O(1)}\).
    The polylogarithmic shift sector (167.50) is target-safe but carries
    no fixed-power fraction of the open shift range.

11. **endpoint_and_real_centre — PASS FOR THE EXACT TRANSFORM; RED FOR
    SOURCE COMPLETION.**  Equations (167.12)--(167.16) preserve sharp
    endpoints, zero extension, and the fixed real value \(J=\sqrt X\).
    No average over the centre is introduced.  Smooth source completion
    is unpriced.

12. **downstream_scope_and_no_exponent_promotion — PASS.**  No parent
    claim, quarter theorem, or exponent improvement is inferred.
    K17a remains open.

13. **no_in_round_pivot — PASS.**  The report does not invoke K26,
    another hard-TOP channel, BAL, UNBAL, M1, GAR, or endpoint assembly
    as a replacement objective.

No numerical experiment was used.  The allocation was entirely
analytical/algebraic.

## 6. Dependencies and exact artifacts used

The graph hash frozen by the generated brief is
\(9d93f058c3623b7b278aa1ccba99adcf264c2e1d45af95ffbf993a123cfa1f76\).
The initial derivation used the permitted Round-167 context and its
generated brief:

- protocol.md;
- state/proof_obligations.yml, specifically the accepted residual
  transport and Fejer parity/gcd/scale nodes and the Round-166 rejected
  overpromotions;
- state/active_campaign.yml;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
- strategy/conductor_0826_full_proof_strategy.md;
- strategy/round167_m2_hard_top_t1_residual_oscillatory_determinant_strategy.md;
- rounds/codex-managed/full-proof-round164-166-strategy-literature-review/synthesis.md;
- rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/current_primary_literature_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/barrier_packet.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/briefs/literal_determinant_kernel_attack.md.

The post-review repair additionally used:

- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/oscillatory_source_power_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/literal_kernel_capacity_polylog_seam_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/source_orbit_phase_power_seam_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/literal_source_interface_reconciliation_review.md.

The exact source hypotheses and theorem shapes used in Sections 3--5
were imported from the primary-literature audit and the repaired hostile
source audit, which record
Grimmelt--Merikoski 2024, Theorem 10.1
(arXiv:2404.08502v2), and Grimmelt--Merikoski 2025 Part I, Theorem 1.1
and Corollary 1.5 (arXiv:2505.00489v2).  This report does not claim an
independent source verification beyond those audited records and does
not use the announced, unavailable oscillatory Part II.

## 7. Recommended state effect

**Retain K17a as open; retain the accepted graph and exponent unchanged.**

Promote only the following candidate evidence if the independent seam
reviews agree:

- the exact multiplicity-one determinant/orbit opening
  (167.20)--(167.24);
- the exact selector-aware endpoint-kernel identity (167.16);
- the scoped positive-capacity bound (167.32);
- the exact bare-character orbit cancellation (167.26d);
- the scoped low-\(g\) ambient nonautomorphy witness
  (167.35a)--(167.35b);
- the phase derivative (167.37)--(167.39), continuous rank-one
  nonseparability (167.40a)--(167.40c), and explicitly conditional
  source-power ledger (167.41)--(167.46);
- the auxiliary owner-complete polylogarithmic shift bound (167.50);
- the first missing interface \(\operatorname{ODK}_{\rm K17a}\) in
  (167.51).

Reject direct promotion of Grimmelt--Merikoski 2024 Theorem 10.1 or the
2025 Part-I theorem to K17a.  The first failed hypothesis is the
selector-dependent automorphic/smooth coefficient class; the subsequent
seminorm, variable-\(r\), \(\mathcal K_+\), modified-coefficient or
Part-I principal component, positive autocorrelation, boundary, and
completion ledgers independently remain open.  The bare 2024 main term
itself vanishes and is not an obstruction.

This no-go is confined to the tested determinant-source interfaces.
It neither disproves K17a nor licenses an in-round move to K26.  Even a
future proof of K17a would close only the complete residual scalar
through the already accepted connector; the other \(t=1\) channels and
near collars, hard TOP, both direct M1 parents, BAL, UNBAL, GAR,
endpoint uniformity, the full standard proof, the full GAR proof, the
quarter theorem, and every sub-\(1/3\) exponent route would remain
separate graph obligations.
