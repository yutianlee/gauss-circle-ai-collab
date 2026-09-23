# Conductor candidate: \(t=1\) Mellin--Euler reduction, safe residue, and polylogarithmic sector

## Exact statement

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X={X\over y^2},\qquad
 H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
 \qquad 1\ll L\ll H .
\tag{168.C1}
\]

Retain the complete literal hard-TOP \(t=1\) scalar

\[
\begin{aligned}
 \mathcal S_{L,1}
 =\sum_{\substack{nm\asymp L^2\\
                  n,m\ {\rm squarefree},\ (n,m)=1\\
                  n\ {\rm odd},\ m\leq n\leq4m}}
 &\chi_4(n)\left({L^2\over nm}\right)^{3/4}
 \eta_L(n)\Phi\!\left({n\over H+1}\right)\\
 &\times W\!\left(\sqrt{{q_Xn\over4m}}\right)
 e(J\sqrt{nm}),
\end{aligned}
\tag{168.C2}
\]

with every accepted half-open shell, floor, profile value, cone edge,
star, endpoint transition, and zero-extension convention.  Write
\(A_{L,X}(n,m)\) for the complete bounded non-arithmetic amplitude in
(168.C2).

Then the following assertions hold.

1. Initially for \(\Re s_1,\Re s_2>1\), the intact arithmetic family has
   the exact factorization
   \[
    D(s_1,s_2)
    =L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2),
   \tag{168.C3}
   \]
   where
   \[
   \begin{aligned}
    D(s_1,s_2)
    &=
    \sum_{\substack{n,m\ {\rm squarefree}\\(n,m)=1\\n\ {\rm odd}}}
    {\chi_4(n)\over n^{s_1}m^{s_2}},\\
    G_2&=1-2^{-2s_2},\\
    G_p&=(1+x_p+y_p)(1-x_p)(1-y_p),\qquad
    x_p=\chi_4(p)p^{-s_1},\quad y_p=p^{-s_2}
   \end{aligned}
   \tag{168.C4}
   \]
   for odd \(p\).  The product for \(G\) is absolutely and locally
   uniformly convergent, hence holomorphic, when
   \(\Re s_1,\Re s_2>1/2\).

2. There is an exact endpoint-lawful cardinal Mellin representation.
   For any fixed \(0<\eta<1/4\), shifting it to
   \(\Re s_1=\Re s_2=1/2+\eta\) gives
   \[
    \mathcal S_{L,1}=R_\zeta+\mathcal I_\eta ,
   \tag{168.C5}
   \]
   where \(R_\zeta\) is the only crossed residue and
   \[
    R_\zeta\ll_\varepsilon {L^2\over J}X^\varepsilon.
   \tag{168.C6}
   \]
   Thus the general \(t=1\) target is equivalent, up to a target-safe
   term, to the exact signed two-height estimate
   \[
    \mathcal I_\eta\ll_\varepsilon L^{3/2}X^\varepsilon.
   \tag{168.C7}
   \]

3. Given a requested target exponent \(\varepsilon>0\), choose the
   contour offset \(0<\eta\leq\min(1/8,\varepsilon/4)\).  On a favorable
   recombined smooth/BV control component, radial
   stationarity occurs on
   \[
    t_+=t_1+t_2=-2\pi Jr\asymp-JL
   \tag{168.C8}
   \]
   over a band of length \(T\asymp JL\), and the transform scale on the
   shifted lines is
   \[
    L^{1+2\eta}(JL)^{-1/2}
    =L^{2\eta}\sqrt{L/J}.
   \tag{168.C9}
   \]
   Consequently, even a granted Lindelöf-size pointwise arithmetic
   majorant followed by triangle inequality, or a granted
   fixed-angular mean square of size \(T X^\delta\) followed by
   Cauchy, certifies only
   \[
    L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
   \tag{168.C10}
   \]
   Taking the arithmetic allowance \(\delta\) sufficiently smaller than
   \(\varepsilon\) and using \(L\leq X^{1/4+o(1)}\) places the harmless
   \(L^{2\eta}\) factor inside the final \(X^\varepsilon\).  The
   structural deficit is still \(\sqrt J\).
   These two absolute placements therefore do not prove (168.C7).
   This is a method-capacity statement, not a lower bound and not a
   no-go for a new signed weighted hybrid theorem.

4. For each fixed \(B>0\), the complete literal sector
   \[
    L\leq(\log X)^B
   \tag{168.C11}
   \]
   satisfies
   \[
    \boxed{\mathcal S_{L,1}
    \ll_{\varepsilon,B}L^{3/2}X^\varepsilon.}
   \tag{168.C12}
   \]
   For every fixed \(\kappa>0\), let
   \(\mathcal S_{L,1;\kappa}^{\rm rem}\) be the remainder in the
   accepted canonical \(\kappa\)-dependent close-opposite-prime XOR
   decomposition.  Then
   \[
    \mathcal S_{L,1;\kappa}^{\rm rem}
    \ll_{\varepsilon,B,\kappa}L^{3/2}X^\varepsilon
   \]
   in the same fixed-polylogarithmic-\(L\) sector.

No polynomial-\(L\) full scalar, general residual, other hard-TOP channel,
hard TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint theorem, M9, bridge,
quarter theorem, or exponent is proved.

## Proof

### 1. Euler algebra

At \(p=2\), oddness of \(n\) permits \(2\) only in \(m\), so

\[
 D_2=1+2^{-s_2}.
\]

At every odd prime, squarefreeness and coprimality permit exactly the
three states: the prime divides neither leg, only \(n\), or only \(m\).
Thus

\[
 D_p=1+\chi_4(p)p^{-s_1}+p^{-s_2}=1+x_p+y_p.
\]

After removing the local factors of \(L(s_1,\chi_4)\zeta(s_2)\),

\[
 G_p
 =1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2.
\tag{168.C13}
\]

On compact subsets of \(\Re s_j>1/2\),

\[
 |G_p-1|
 \ll p^{-2\Re s_1}+p^{-\Re s_1-\Re s_2}
       +p^{-2\Re s_2}+p^{-3\min(\Re s_1,\Re s_2)}.
\]

The prime sum converges, proving (168.C3)--(168.C4).  No nonvanishing of
\(G\) is asserted.

### 2. Exact cardinal interpolation and the pole

Choose
\(\psi\in C_c^\infty((-1/3,1/3))\) with \(\psi(0)=1\), and define

\[
 \mathcal B(x,z)
 =e(J\sqrt{xz})
  \sum_{n,m}A_{L,X}(n,m)\psi(x-n)\psi(z-m).
\tag{168.C14}
\]

The sum is finite and its cells are disjoint.  Therefore

\[
 \mathcal B(n,m)=A_{L,X}(n,m)e(J\sqrt{nm})
\tag{168.C15}
\]

at every positive integer pair, including every literal hard value.  With

\[
 \widehat{\mathcal B}(s_1,s_2)
 =\int_0^\infty\!\int_0^\infty
 \mathcal B(x,z)x^{s_1-1}z^{s_2-1}\,dx\,dz,
\tag{168.C16}
\]

ordinary Mellin inversion and absolute convergence on \(c_1,c_2>1\)
give

\[
 \mathcal S_{L,1}
 ={1\over(2\pi i)^2}
 \int_{(c_1)}\int_{(c_2)}
 \widehat{\mathcal B}(s_1,s_2)D(s_1,s_2)\,ds_2\,ds_1.
\tag{168.C17}
\]

The transform is entire and rapidly decreasing on every fixed vertical
strip, so rectangular contour motion is valid.  Inside the direct
holomorphy region of \(G\), the only crossed pole is \(s_2=1\).

The residue coefficient series is explicit.  For odd \(p\),

\[
 L_p(s,\chi_4)G_p(s,1)
 =(1-p^{-2})+(1-p^{-1})\chi_4(p)p^{-s},
\]

and the factor at \(2\) is \(1-2^{-2}\).  Hence

\[
 L(s,\chi_4)G(s,1)
 ={1\over\zeta(2)}
 \sum_{\substack{n\geq1\\n\ {\rm odd,\ squarefree}}}
 {\chi_4(n)\over n^s}
 \prod_{p\mid n}(1+p^{-1})^{-1}.
\tag{168.C18}
\]

Taking the \(s_1\)-line initially to the right of one, using (168.C18),
and applying one-variable Mellin inversion in \(x\) gives

\[
 R_\zeta
 ={1\over\zeta(2)}
 \sum_{\substack{n\geq1\\n\ {\rm odd,\ squarefree}}}
 \chi_4(n)\prod_{p\mid n}(1+p^{-1})^{-1}
 \int_0^\infty\mathcal B(n,z)\,dz.
\tag{168.C19}
\]

At \(x=n\), disjointness in (168.C14) gives

\[
 \mathcal B(n,z)
 =e(J\sqrt{nz})\sum_m A_{L,X}(n,m)\psi(z-m).
\]

On every nonzero cell \(n,m\asymp L\), and

\[
 {d\over dz}\bigl(2\pi J\sqrt{nz}\bigr)
 =\pi J\sqrt{n/z}\asymp J.
\]

One integration by parts, using the compact support of \(\psi\), gives

\[
 \int\psi(z-m)e(J\sqrt{nz})\,dz\ll J^{-1}
\tag{168.C20}
\]

uniformly in the literal centre.  There are \(O(L^2)\) cells and the
residue coefficients have modulus at most one.  Equations
(168.C19)--(168.C20) prove (168.C6).

Shifting the remaining two contours gives

\[
\begin{aligned}
 \mathcal I_\eta
 ={1\over(2\pi)^2}\int_{\mathbb R^2}
 &\widehat{\mathcal B}(\alpha+it_1,\alpha+it_2)
 L(\alpha+it_1,\chi_4)\zeta(\alpha+it_2)\\
 &\times G(\alpha+it_1,\alpha+it_2)\,dt_1dt_2,
 \qquad \alpha={1\over2}+\eta .
\end{aligned}
\tag{168.C21}
\]

This proves the exact reduction (168.C5)--(168.C7).  The cardinal
interpolation is an identity device: its \(O(L^2)\) unit-cell complexity
is not asserted to provide analytic smoothing.

For comparison, the statement-only report
`reports/blind_mellin_euler_rederivation.md` independently proves an exact
mixed-difference/Perron realization, whose \(s_2=1\) residue telescopes
instead to

\[
 R_\zeta^{\rm St}
 =\sum_{n,m}\rho(n)
 A_{L,X}(n,m)e(J\sqrt{nm}),
 \qquad
 \sum_n\rho(n)n^{-s}=L(s,\chi_4)G(s,1),
\tag{168.C22}
\]

because \(m\asymp L>1\).  It is a discrete sum and is not automatically
small.  Equations (168.C19) and (168.C22) belong to different exact
interpolations; they must not be conflated.

### 3. Radial spectral capacity

The following calculation tests only the favorable recombined
smooth/BV model.  It is not a stationary estimate for one unit cardinal
cell.  Put

\[
 x=rw,\qquad z=r/w,\qquad
 t_+=t_1+t_2,\qquad t_-=t_1-t_2.
\]

The radial phase is

\[
 2\pi Jr+t_+\log r.
\]

Its stationary equation is (168.C8); as \(r\) crosses a fixed-relative
shell \(r\asymp L\), the stationary band has length \(T\asymp JL\).
Stationary phase on the lines
\(\Re s_1=\Re s_2=1/2+\eta\) gives (168.C9), times the angular transform
and its literal seminorms.

Granting, with a separate auxiliary exponent \(\delta>0\), the
stronger-than-known pointwise estimate

\[
 |L(\alpha+it_1,\chi_4)\zeta(\alpha+it_2)
 G(\alpha+it_1,\alpha+it_2)|\ll X^\delta
\]

and an optimistic \(O(1)\) angular range, triangle inequality gives

\[
 L^{2\eta}\sqrt{L/J}\,T X^\delta
 =L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
\]
Alternatively, the radial transform has \(L^2\)-norm of scale
\(L^{1+2\eta}\), while a granted fixed-angular arithmetic mean square
\(T X^\delta\) has norm \(T^{1/2}X^\delta\).  Cauchy gives

\[
 L^{1+2\eta}\sqrt T\,X^\delta
 =L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
\]

For a requested final exponent \(\varepsilon>0\), take
\(0<\eta\leq\min(1/8,\varepsilon/4)\) and then take \(\delta>0\)
sufficiently smaller than \(\varepsilon\).  Since
\(L\leq X^{1/4+o(1)}\), this places \(L^{2\eta}X^\delta\) inside
\(X^\varepsilon\).  The capacity still misses the target by the
structural factor \(\sqrt J\).

This proves (168.C10) as the capacity of only those named absolute
placements.  Literal BV angular tails make their bookkeeping no better.
A successful continuation needs cancellation between the stationary
phase and the two L-functions before absolute values.

The exact source report
`reports/hybrid_zeta_l_source_hostile_audit.md` checks Topacogullari
Theorems 2.1, 2.2, 1.5--1.6, and 2.7, Bourgain's published p. 206
pointwise consequence, Ramana--Ramare Theorem 2.1 and Corollary 2.2, and
Durkan--Karak--Mahatab Theorem 1.1.  These are negative interface checks,
not inputs to (168.C6), (168.C10), or (168.C12).  They confirm that the
inspected pointwise, absolute first-moment, positive second-moment,
common-height approximate functional equation, exact Perron, and
conditional positive shifted-moment theorems do not supply the signed
two-height estimate.  No exact
coefficient bridge from factorwise functional equations or approximate
functional equations to the accepted Round-162 collar has been proved.
The only lawful collar comparison is the prior accepted statement: if one
deliberately reopens the original projector by its Möbius identity and
then uses positive physical Poisson control, the accepted capacity is
\(\sqrt{JL}X^\varepsilon\), with

\[
 {\sqrt{JL}\over L^{3/2}}
 ={\sqrt J\over L}
 ={H\over L}+O(L^{-1}).
\tag{168.C23}
\]

Round 168 adds no AFE self-return theorem.

### 4. Fixed-polylogarithmic \(L\)

The normalization and fixed profiles in (168.C2) are bounded on their
support, which contains \(O(L^2)\) ordered pairs.  Thus, with an
auxiliary exponent,

\[
 |\mathcal S_{L,1}|\ll L^2X^{\varepsilon/2}.
\]

For fixed \(B\), (168.C11) gives

\[
 L^{1/2}\leq(\log X)^{B/2}
 \ll_{\varepsilon,B}X^{\varepsilon/2},
\]

which proves (168.C12).

For fixed \(\kappa>0\), the accepted close opposite-prime sector satisfies
\(\mathcal S_{L,1;\kappa}^{\rm cp}\ll_\kappa L^{3/2}\) and

\[
 \mathcal S_{L,1}
 =\mathcal S_{L,1;\kappa}^{\rm cp}
  +\mathcal S_{L,1;\kappa}^{\rm rem}
\tag{168.C24}
\]

exactly.  Subtracting (168.C24) proves the fixed-polylogarithmic residual
corollary with implied constant depending on \(\kappa\), and nothing
beyond it.

## First open interface and route scope

The exact remaining theorem is the signed two-height estimate (168.C7)
for the endpoint-lawful transform, or an equivalent physical statement.
On the favorable smooth control its required gain is \(\sqrt J\) over
the optimistic absolute capacity.  Pointwise Lindelöf followed by
triangle inequality, the stated fixed-angular mean square followed by
Cauchy, an exact Perron formula without its local correction, and the
already parked Möbius-opened positive collar do not provide it.

This is a scoped interface no-go.  It is not a physical lower bound, not a
no-go for every weighted hybrid or functional-equation method, and not a
claim that the exact cardinal integral itself has the favorable
smooth-model norm.

The general full scalar and residual remain open, as do all other
few-point channels and collars, hard TOP, BAL, UNBAL, M9--M2, both direct
M1 parents, GAR, endpoint assembly, M9, both bridges, the quarter theorem,
and both exponent ledgers.
