# Round 41 discovery report: the off-diagonal and smooth product cells close at the target scale

Task: `off_diagonal_mixed_norm_attack`  
Role: discovery  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result

After the already proved signed diagonal Cauchy section is excluded, the
remaining large-\(|\alpha|\) terminal product cells satisfy the requested
absolute mixed physical-height norm.  The result is uniform on both signed
saddle cells and their entry/exit collars.  It also includes the actual
moving physical faces and the exact normalized Morse remainder; no scalar
Fresnel replacement is made.

More precisely, freeze one actual cell
\((j,h,q,x,\beta,\pm,\tau)\), put

\[
 \lambda={\pi q\sqrt{Xx}\over D_j},\qquad
 y=L-\nu,\qquad
 A(L)=-1-{b\over2}-i(L+\beta),
 \tag{41.1}
\]

and

\[
 D(L,\nu)=A(L)+{iy\over2}
 =-1-{b\over2}-i\left({L+\nu\over2}+\beta\right).
 \tag{41.2}
\]

Here \(\tau\) records an ordinary beta-mask or beta-connector cell; all
endpoint, radial-side, axial, collision, connector-axis, corner, and
artificial-residue shares have already been routed by the accepted global
ownership operation.  The exact remaining singular numerator and every
smooth numerator have finite one-count product forms

\[
 H^\circ_\tau(L,\nu)
 =\sum_{\ell=1}^{M_\tau}
 C_{\tau\ell}(\beta)G_{\tau\ell,\pm}(L;\lambda)
 p_{\tau\ell}(\nu),
 \tag{41.3}
\]

and

\[
 H^\circ_{\tau,\mathrm{sm}}(L,\nu)
 =\sum_{\ell=1}^{M_\tau}
 C_{\tau\ell}(\beta)G_{\tau\ell,\pm}(L;\lambda)
 p_{\tau\ell}(\nu)W_{\tau\ell}(L-\nu),
 \tag{41.4}
\]

respectively, where \(M_\tau=O(1)\).  An ordinary mask or pure
\(\psi'(\beta)\) connector has \(M_\tau=1\).  A mixed beta connector is
the finite Leibniz expansion of the same exact product and may have
\(M_\tau>1\); its factors obey the same bounds (41.23) below, with only
additional polylogarithmic constants.  Formulae (41.3)--(41.4) are exact
after the complete stationary \(L\)-phase and the real factor
\(\lambda^\kappa\) have been removed.  In particular, they are not a
factorization of the already summed terminal vector.

For one summand of (41.3)--(41.4), suppressing its index \(\ell\), the
singular off-diagonal density and a smooth ordinary-\(\mu\) density are
therefore

\[
 \boxed{
 K_{\Delta,\tau}(L,\nu)
 =C_\tau G_\pm(L;\lambda)
 {p(\nu)-p(L)\over (L-\nu)D(L,\nu)}}
 \tag{41.5}
\]

and

\[
 \boxed{
 K_{\mathrm{sm},\tau}(L,\nu)
 =C_\tau G_\pm(L;\lambda)
 {p(\nu)W_\tau(L-\nu)\over D(L,\nu)}.}
 \tag{41.6}
\]

Only (41.5) is the remainder of the singular Plemelj share.  Formula
(41.6) retains ordinary \(d\mu/(2\pi)\) integration and receives no
delta, PV, or second top-log operation.  The complete density is the
finite sum of these displayed terms, so the estimate follows by
linearity once it is proved for one term.

Let \(I_\lambda^\pm\) be any fixed-ratio signed saddle, entry, or exit
interval, so that

\[
 c_0\lambda\le |L+\beta|\le C_0\lambda,
 \qquad |I_\lambda^\pm|\le C_0\lambda.
 \tag{41.7}
\]

For \(K=K_{\Delta,\tau}\), and separately for every
\(K_{\mathrm{sm},\tau}\), one has

\[
\begin{aligned}
 &\sup_{L\in I_\lambda^\pm}\int_{\mathbb R}|K(L,\nu)|\,d\nu
 +\int_{I_\lambda^\pm}\int_{\mathbb R}
       |\partial_L^\nu K(L,\nu)|\,d\nu\,dL\\
 &\quad+
 \sup_{U,V}\sum_{\gamma\in\Gamma_{U,V}^{\rm mov}}
       \int_{I_\lambda^\pm}|K(L,\gamma(L))|\,dL
 +\|\mathfrak r^{\rm Morse}_{\lambda,\pm}[K]\|_{L^1(d\nu)}
 \ll_\varepsilon X^\varepsilon\lambda^{-2}.
 \tag{41.8}
\end{aligned}
\]

Here \(\Gamma_{U,V}^{\rm mov}\) consists exactly of the active moving
physical faces \(\nu=L-U\) and \(\nu=L+U\) in
\([-V,V]\cap[L-U,L+U]\).  Fixed faces \(\nu=\pm V\) have zero
Leibniz speed and do not create a trace.  At a min/max switch the two
endpoint formulae agree, and a collapsed section contributes zero.

The proof of (41.8) uses the exact endpoint quotients

\[
 Q(L,\nu)={p(\nu)-p(L)\over L-\nu},\qquad
 R(L,\nu)={p(L)-p(\nu)-p'(L)(L-\nu)\over(L-\nu)^2},
 \tag{41.9}
\]

before absolute values.  Thus it preserves the Round-40 cancellation:
it never majorizes the two \(F_{Ly}\) and \(F_{yy}\) integrals
separately.

The signed diagonal term

\[
 K_C=-{iH^\circ(L,L)\over2A(L)D(L,\nu)}
 \tag{41.10}
\]

is not used in (41.8).  It remains under the proved signed
finite-section logarithmic module, and Morse localization is applied to
it only after that signed section is formed.  Combining that accepted
module with (41.8) proves the corrected hybrid norm for every
large-\(|\alpha|\) terminal product cell.  It does not prove the
bounded-\(\alpha\), double-bounded, or complete beta-transition
assembly.

## 2. Exact statement and hypotheses

Use the legal terminal parameters

\[
 \sigma={5\over4},\qquad b={1\over\log(2X)},\qquad
 \zeta=a+b,\qquad
 r=\sigma-{\zeta\over2},\qquad
 p_*=\sigma+{\zeta\over2},\qquad
 \kappa=p_*-{1\over2}<1,
 \tag{41.11}
\]

where \(a+b<1/2\) and \(a/2+b<1/4\).  The beta variable lies in a
fixed compact set.  The beta-slab coordinates are

\[
 u=a+i(L-\nu),\qquad v=b+i\nu,\qquad
 s=\sigma+i\left({L\over2}+\beta\right),
 \qquad \alpha=L+\beta.
 \tag{41.12}
\]

The exact gamma factors are

\[
 R_\alpha(\alpha)=
 {\Gamma((1+\sigma+\zeta/2)/2+i\alpha/2)
  \over
  \Gamma((2-\sigma-\zeta/2)/2-i\alpha/2)},
 \tag{41.13}
\]

\[
 R_\beta(\beta)=
 {\Gamma((\sigma-\zeta/2)/2+i\beta/2)
  \over
  \Gamma((1-\sigma+\zeta/2)/2-i\beta/2)}.
 \tag{41.14}
\]

Write the fixed \(2,\pi\)-factor in the exact beta-normal-form gamma
identity as \(c_{\sigma,\zeta}\), so that the gamma quotient in the raw
terminal numerator is exactly
\(c_{\sigma,\zeta}R_\alpha(\alpha)R_\beta(\beta)\).
Collecting the phases in the assigned raw formula gives

\[
 \omega_L=\log{D_j\over2\sqrt X}-\log q-{1\over2}\log x,
 \qquad
 \omega_\nu=-\log{D_j\over2\sqrt X}
 +\log(H_j+1)-{1\over2}\log x.
 \tag{41.15}
\]

Thus, before phase removal, one actual spatial share is exactly

\[
\begin{aligned}
 \mathscr H_{\tau}^{\rm raw}(L,\nu)
 ={}&\mathfrak a_{j,h,q,x},
 c_{\sigma,\zeta}R_\beta(\beta)c_\tau^{\rm mask}(\beta)
 e^{-i\beta\log(hqx)}\\
 &\times R_\alpha(L+\beta)e^{i\omega_LL}
 \{\widehat\phi(b+i\nu)e^{i\omega_\nu\nu}\}
 W_\tau(L-\nu),
 \tag{41.16}
\end{aligned}
\]

where

\[
 \mathfrak a_{j,h,q,x}
 =(-\pi i\sqrt X)e(\sqrt{Xx})
 h^{-r}q^{-p_*}
 \left({D_j\over2\sqrt X}\right)^a
 (H_j+1)^b x^{-3/2-b/2}.
 \tag{41.17}
\]

For the singular \(u^{-1}\) hard-top share, \(W_\tau=1\); for the
smooth top remainder and interior shares, \(W_\tau(y)\) is the actual
normalized Mellin profile.  The dyadic construction gives, uniformly in
the spatial cell,

\[
 |\partial_y^mW_\tau(y)|\ll_{m,N}(1+|y|)^{-N}
 \quad(m\le2,\ N\ge0).
 \tag{41.18}
\]

On a signed interval (41.7), let \(\Psi_\pm(L)\) be the canonical
signed Stirling main phase, including the exact linear phase
\(\omega_LL\), normalized by

\[
 \Psi_\pm'(L)=\log {|L+\beta|\over\lambda},
 \qquad \Psi_\pm''(L)={1\over L+\beta}.
 \tag{41.18a}
\]

Keep the exact Stirling correction, including its continuous residual
argument, in the symbol and define

\[
 G_\pm(L;\lambda)
 =\lambda^{-\kappa}e^{-i\Psi_\pm(L)}
 R_\alpha(L+\beta)e^{i\omega_LL},
 \qquad
 p(\nu)=\widehat\phi(b+i\nu)e^{i\omega_\nu\nu},
 \tag{41.19}
\]

\[
 C_\tau(\beta)=c_{\sigma,\zeta}R_\beta(\beta)
 c_\tau^{\rm mask}(\beta)e^{-i\beta\log(hqx)}.
 \tag{41.20}
\]

Equations (41.16), (41.19), and (41.20) prove the exact factorization

\[
 \mathscr H_\tau^{\rm raw}
 =\mathfrak a_{j,h,q,x}\lambda^\kappa e^{i\Psi_\pm(L)}
 C_\tau(\beta)G_\pm(L;\lambda)p(\nu)W_\tau(y).
 \tag{41.21}
\]

Equation (41.21) is the generating one-count product formula.  An
ordinary beta mask has \(c_\tau^{\rm mask}=\psi\); a pure beta-face
connector replaces it by one of the finitely many fixed compactly
supported mask derivatives and fixed connector constants.  Since beta is
held fixed under \(\partial_L^\nu\), those factors belong to (41.20).

When an accepted mixed connector differentiates another factor in
(41.21), apply its finite product rule before estimating.  This gives the
exact finite-rank expansion

\[
 \boxed{
 H^\circ_\tau(L,\nu)
 =\sum_{\ell=1}^{M_\tau}C_{\tau\ell}(\beta)
 G_{\tau\ell,\pm}(L;\lambda)p_{\tau\ell}(\nu)
 W_{\tau\ell}(L-\nu),}
 \tag{41.21a}
\]

with \(W_{\tau\ell}=1\) for the singular hard-top share.  Derivatives
fall only on the compact beta factor, the gamma/scale factor, the height
factor, or the normalized spatial Mellin factor.  Thus each
\(G_{\tau\ell}\) is a fixed normalized derivative of the phase-removed
gamma/scale product, each \(p_{\tau\ell}\) is a fixed derivative of
\(p\), and each \(W_{\tau\ell}\) is a fixed derivative of \(W\).
Stirling and the profile estimates below show that this finite expansion
has exactly the same symbol class as its generating term.  This is the
mixed-connector factorization left unwritten in Round 40; treating a
connector as an unspecified multiplier would not suffice.

The common artificial cutoff creates no further mixed product.  On the
terminal line its three jointly owned terms obey the exact algebra

\[
 \omega G_{\rm com}+(1-\omega)R_1-\omega E_1=R_1,
 \qquad G_{\rm com}=E_1+R_1.
 \tag{41.22}
\]

Consequently all derivatives of the cutoff cancel before a cell is
estimated.  Estimating any of the three summands in (41.22) separately
would not be a one-count factorization.  The already extracted
artificial residue, axial vector, connector-axis images, collisions, and
corner are not reinserted into (41.21).

Stirling after exact phase removal, the finite connector product rule,
and the actual profile estimates give, for \(m=0,1,2\) and every
\(\ell\),

\[
 |\partial_L^mG_{\tau\ell,\pm}(L;\lambda)|
 \le P_X\lambda^{-m},
 \qquad
 |p_{\tau\ell}^{(m)}(t)|\le P_X(1+|t|)^{-3},
 \tag{41.23}
\]

where \(P_X\ll b^{-C}(1+\log(2X))^C\), and hence
\(P_X\ll_\varepsilon X^\varepsilon\).  The same estimates hold on the
positive and negative branches and up to the exact entry/exit endpoints.

All factors not displayed in (41.5)--(41.6) remain external.  In the
post-stationary normalization they are

\[
 \chi_4(q)\,\mathcal B_{j,h,x}{D_j\over q}\lambda,
 \qquad
 \mathcal B_{j,h,x}
 =h^{-r}\left({D_j\over2\sqrt X}\right)^a(H_j+1)^b
 \theta_j(x)^{p_*}x^{-\sigma-3/4-b/2},
 \tag{41.24}
\]

with \(\theta_j(x)=\pi\sqrt{Xx}/D_j\).  Also external are the exact
Fresnel phase, radial and beta integrations, two remaining contour
factors for the singular top share (three ordinary factors for a smooth
share), floors, stars, the character, and
\(-4X^{1/4}\operatorname {Re}\{e(1/8)\,\cdot\}/\pi\).
No coefficient or arithmetic sum is performed below.

## 3. Proof or derivation

### 3.1 Cancellation-preserving endpoint calculus

Abbreviate \(G=G_\pm\), suppress the bounded factor \(C_\tau\), and
define \(Q,R\) by (41.9), using their continuous diagonal values

\[
 Q(L,L)=-p'(L),\qquad R(L,L)=-{1\over2}p''(L).
 \tag{41.25}
\]

Then

\[
 K_\Delta={GQ\over D}.
 \tag{41.26}
\]

At fixed physical \(\nu\), both \(y=L-\nu\) and \(L\) vary.  Direct
differentiation, before any absolute value, gives

\[
 \boxed{
 \partial_L^\nu K_\Delta
 ={G'Q+GR\over D}+{iGQ\over2D^2}.}
 \tag{41.27}
\]

The numerator \(G'Q+GR\) is exactly

\[
 G'{p(\nu)-p(L)\over y}
 -G{p'(L)\over y}
 -G{p(\nu)-p(L)\over y^2},
 \tag{41.28}
\]

which is the recombined Round-40 second translation divided difference.
In particular, (41.27) is not obtained by separately estimating
\(F_{Ly}\) and \(F_{yy}\).

Put \(\ell=1+|L|\asymp\lambda\).  Since beta is bounded,

\[
 |A(L)|\asymp\ell,
 \qquad
 |D(L,\nu)|\asymp 1+|L+\nu+2\beta|.
 \tag{41.29}
\]

Choose a small fixed \(\delta>0\) and split the height line into the
following disjoint regions, assigning overlaps in the displayed order:

\[
\begin{array}{ll}
 \Omega_P:& |\nu|\le\delta\ell \quad\hbox{(physical center)},\\
 \Omega_T:& |L-\nu|\le\delta\ell \quad\hbox{(top diagonal)},\\
 \Omega_R:& |L+\nu+2\beta|\le\delta\ell
                    \quad\hbox{(radial ridge)},\\
 \Omega_F:& \hbox{the complement}.
\end{array}
 \tag{41.30}
\]

The three centers \(0,L,-L-2\beta\) are separated by
\(\asymp\ell\) on either signed cell.  The endpoint form (41.9), the
Taylor forms

\[
 Q=-\int_0^1p'(L-ty)\,dt,\qquad
 R=-\int_0^1(1-t)p''(L-ty)\,dt
 \tag{41.31}
\]

used only on \(\Omega_T\), and (41.23) give the following integral
ledger:

\[
\begin{array}{c|c|c|c}
 &\displaystyle\int {|Q|\over|D|}\,d\nu
 &\displaystyle\int {|R|\over|D|}\,d\nu
 &\displaystyle\int {|Q|\over|D|^2}\,d\nu\\ \hline
 \Omega_P& O(P_X\ell^{-2})&O(P_X\ell^{-3})&O(P_X\ell^{-3})\\
 \Omega_T& O(P_X\ell^{-3})&O(P_X\ell^{-3})&O(P_X\ell^{-4})\\
 \Omega_R& O(P_X\ell^{-4}\log(2+\ell))
          &O(P_X\ell^{-4}\log(2+\ell))&O(P_X\ell^{-4})\\
 \Omega_F& O(P_X\ell^{-2})&O(P_X\ell^{-3})&O(P_X\ell^{-3}).
\end{array}
 \tag{41.32}
\]

For completeness, on \(\Omega_P\), both \(|y|\) and \(|D|\) are
\(\asymp\ell\); the \(p(\nu)\) term is integrated in \(L^1\), while
\(p(L),p'(L)=O(P_X\ell^{-3})\).  On \(\Omega_T\), the whole segment
\(L-ty\) remains of size \(\asymp\ell\), which licenses (41.31).
On \(\Omega_R\), \(|y|\asymp\ell\), both endpoint profile values have
cubic decay, and integration of \(|D|^{-1}\) costs only
\(\log(2+\ell)\).  On \(\Omega_F\) use the endpoint form and

\[
 \int_{\Omega_F}{d\nu\over
 |L-\nu|\{1+|L+\nu+2\beta|\}}
 \ll {\log(2+\ell)\over\ell};
 \tag{41.33}
\]

the terms containing \(p(\nu)\) gain the additional integrable cubic
profile.  These observations prove every entry of (41.32) without
integrating an absolute \(p''\) along a long translation.

Equations (41.23), (41.26), (41.27), and (41.32) now yield the stronger
per-\(L\) estimates

\[
 \int_{\mathbb R}|K_\Delta(L,\nu)|\,d\nu
 \ll P_X\lambda^{-2},
 \qquad
 \int_{\mathbb R}|\partial_L^\nu K_\Delta(L,\nu)|\,d\nu
 \ll P_X\lambda^{-3}.
 \tag{41.34}
\]

Taking the supremum in the first estimate and integrating the second over
an interval of length \(O(\lambda)\) proves the first two terms of
(41.8).

### 3.2 Smooth ordinary-\(\mu\) shares

For (41.6), fixed-height differentiation is the ordinary product rule

\[
 \partial_L^\nu K_{\rm sm}
 =C_\tau p(\nu)\left{
 {G'W(y)+G W'(y)\over D}+{iGW(y)\over2D^2}
 \right\}.
 \tag{41.35}
\]

No Plemelj operation occurs.  In \(y\)-coordinates the main translated
ridge is \(|y|=O(1)\), where \(|\nu|=|L-y|\asymp\lambda\), so cubic
profile decay and \(|D|\asymp\lambda\) give

\[
 \int_{\mathbb R}|K_{\rm sm}(L,\nu)|\,d\nu
 \ll P_X\lambda^{-4},
 \qquad
 \int_{\mathbb R}|\partial_L^\nu K_{\rm sm}(L,\nu)|\,d\nu
 \ll P_X\lambda^{-4}.
 \tag{41.36}
\]

When \(\nu\) is near the physical center, \(|y|\asymp\lambda\) and
\(W(y)\) is rapidly decreasing.  At the radial ridge,
\(|y|\asymp2\lambda\), the same spatial decay combines with the cubic
height decay.  The far region is summable by (41.18).  This proves
(41.36), uniformly for the smooth top remainder and all normalized
interior profiles.  Its integrated derivative is
\(O(P_X\lambda^{-3})\), one power better than required.

### 3.3 Moving faces and affine switches

For a moving physical face write \(\nu=L-c\), where
\(c=U\) or \(c=-U\).  Its singular quotient is

\[
 Q_c(L)=
 \begin{cases}
 [p(L-c)-p(L)]/c,&c\ne0,\\
 -p'(L),&c=0,
 \end{cases}
 \tag{41.37}
\]

and

\[
 |D(L,L-c)|\asymp1+|L-c/2+\beta|.
 \tag{41.38}
\]

If \(|c|\le\delta\lambda\), the mean-value segment stays in the cubic
tail, so \(|Q_c|\ll P_X\lambda^{-3}\) and the denominator in (41.38)
is \(\asymp\lambda\).  If \(|c|>\delta\lambda\), use the endpoint
quotient and the elementary separated-center convolution

\[
 \int_{\mathbb R}{(1+|L-c|)^{-3}\over
 1+|L-c/2+\beta|}\,dL
 \ll {1\over1+|c|}.
 \tag{41.39}
\]

Together with \(|p(L)|\ll P_X\lambda^{-3}\) on the saddle interval,
this proves, uniformly in the cutoff,

\[
 \int_{I_\lambda^\pm}
 |K_\Delta(L,L-c)|\,dL
 \ll P_X\lambda^{-2}.
 \tag{41.40}
\]

For a smooth share,

\[
 K_{\rm sm}(L,L-c)
 =C_\tau G(L)p(L-c){W(c)\over D(L,L-c)}.
 \tag{41.41}
\]

If \(|c|\le\delta\lambda\), cubic profile decay gives a trace
\(O(P_X\lambda^{-3})\).  If \(|c|>\delta\lambda\), combine (41.39)
with rapid decay of \(W(c)\).  Hence its trace is also bounded by the
right side of (41.40).

For the section
\([p_{U,V}(L),q_{U,V}(L)]=[-V,V]\cap[L-U,L+U]\), Leibniz gives

\[
 {d\over dL}\int_{p_{U,V}}^{q_{U,V}}K\,d\nu
 =\int_p^q\partial_L^\nu K\,d\nu
 +\mathbf1_{\{q=L+U\}}K(L,L+U)
 -\mathbf1_{\{p=L-U\}}K(L,L-U).
 \tag{41.42}
\]

Thus (41.40) has exactly the required upper-plus and lower-minus moving
face signs.  At each affine min/max switch both endpoint descriptions
give the same value, so no jump measure is created.  If the section
collapses, the integral is zero.  Fixed faces \(\pm V\) have derivative
zero.  Equations (41.34), (41.36), and (41.40)--(41.42) prove all
finite-section variation and moving-trace terms in (41.8).

### 3.4 Exact Morse remainder and both saddle signs

Let \(L=L_\pm(\tau)\) be the exact signed Morse coordinate on a full,
entry, or exit cell, and let \(J_\pm=dL/d\tau\).  The accepted exact
chart has

\[
 \left\|{J_\pm\over\sqrt\lambda}\right\|_\infty
 +\operatorname {Var}_\tau\left({J_\pm\over\sqrt\lambda}\right)
 \ll1,
 \tag{41.43}
\]

on every fixed-ratio subinterval.  The normalized varying-amplitude
remainder is exactly

\[
 \mathfrak r^{\rm Morse}_{\lambda,\pm}[K](\nu)
 =\int_{\tau_P}^{\tau_Q}e^{\pm i\tau^2/2}
 \left\{{J_\pm(\tau)\over\sqrt\lambda}
 K(L_\pm(\tau),\nu)-K(L_\pm(0),\nu)\right\}\,d\tau.
 \tag{41.44}
\]

The Fresnel primitive is uniformly bounded on every real interval.
The BV form of Dirichlet's estimate and (41.43) therefore give

\[
 \|\mathfrak r^{\rm Morse}_{\lambda,\pm}[K]\|_{L^1(d\nu)}
 \ll
 \sup_{L\in I_\lambda^\pm}\|K(L,\cdot)\|_{L^1(d\nu)}
 +\int_{I_\lambda^\pm}
    \|\partial_L^\nu K(L,\cdot)\|_{L^1(d\nu)}\,dL.
 \tag{41.45}
\]

Indeed, for each \(\nu\), the supremum of the amplitude is bounded by
its saddle value plus its \(L\)-variation; integrating in \(\nu\)
produces exactly the right side of (41.45).  Jacobian variation is
absorbed by (41.43).  If a physical endpoint changes branch inside the
Morse interval, (41.42) and (41.40) supply the induced endpoint trace.

Applying (41.34) or (41.36) to (41.45) proves the last term of (41.8).
The proof is identical for the two Hessian signs.  At exact entry or exit
the integration interval has the saddle at one endpoint, so the leading
Fresnel coefficient is the exact half coefficient; (41.44)--(41.45)
remain unchanged.  This is an exact leading-plus-remainder calculation,
not scalar Fresnel factorization of a varying amplitude.

### 3.5 Composition with the signed diagonal and ownership modules

The proof above never takes an absolute value of (41.10).  Its signed
section, common logarithm branch, moving-face signs, and post-section
Morse estimate are already proved.  The explicit constant-numerator face
log remains paired with that module through finite-height exhaustion.
Adding its scalar finite-section BV amplitude to the absolute bounds
(41.8) is therefore lawful and gives the complete hybrid large-alpha
cell estimate.

The common artificial identity (41.22) is applied before this addition.
Pure beta connectors change only the compact coefficient (41.20), while
mixed connectors use the finite exact expansion (41.21a); the number of
terms does not change a power.  Smooth shares stay
under their three ordinary measures, while the singular top distribution
leaves exactly two.  Hence no endpoint, axial, artificial, connector,
corner, contour, character, floor, star, radial, stationary-numerator, or
external-normalization factor is counted twice or hidden in (41.8).

## 4. First doubtful or unproved step

No analytic step remains open in the stated large-\(|\alpha|\)
off-diagonal/smooth product-cell theorem, relative to the accepted exact
gamma normal form, normalized spatial-profile seminorms, one-count
ownership ledger, signed diagonal section, and exact Morse chart.

The first unproved step is downstream and outside the frozen theorem:
one must assemble the large-alpha hybrid cells with the separately owned
bounded-\(\alpha\) and double-bounded cells into the complete beta
transition.  The present proof also does not rederive the already closed
\((h,q,x,j)\) coefficient sum.  That sum may be invoked only after the
conductor and independent reviews accept (41.8).

The first step that would become doubtful if the hypotheses were changed
is (41.21a): an isolated artificial-cutoff summand does not have that
factorization.  It is valid only after the common identity (41.22) is
formed.  Likewise, an axial connector or extracted collision share may
not be inserted into (41.3); those objects are already owned by other
modules.  Within the actual post-routing terminal cell, neither issue is
present.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Exact one-count product-cell factorization | **Pass.** Equations (41.16)--(41.21a) derive the singular and smooth products from the assigned raw terminal numerator. Mixed connectors are expanded by the finite exact product rule; the common artificial cutoff collapses by (41.22) before estimation. |
| Phase and external-factor ownership | **Pass.** The complete exact \(L\)-phase and \(\lambda^\kappa\) are removed in (41.19). Equation (41.24) leaves the character, stationary numerator, real monomial, contour measures, radial and beta integrations, floors, stars, and external \(X^{1/4}\) outside. |
| Endpoint divided-difference cancellation | **Pass.** Equations (41.27)--(41.28) use the recombined endpoint quotients. Formula (41.31) is used only on the short top-diagonal segment; no long translated \(|p''|\) integral occurs. |
| Four-region physical-height partition | **Pass.** The physical center, top diagonal, radial ridge, and far region are controlled in (41.30)--(41.34), including the only radial logarithm. |
| Singular versus smooth shares | **Pass.** Only \(K_\Delta\) is the Plemelj off-diagonal remainder. Smooth top/interior shares keep ordinary \(\mu\)-integration and satisfy the stronger estimates (41.35)--(41.36). |
| Moving faces, signs, and affine switches | **Pass.** The uniform trace convolution is (41.37)--(41.40); (41.42) gives upper-plus and lower-minus signs. Switch values agree, fixed faces have zero speed, and collapsed sections vanish. |
| Two saddles, entry/exit, and exact Morse remainder | **Pass.** Exact phase removal gives the same derivative bounds on both branches. Equations (41.43)--(41.45) control the normalized varying-amplitude remainder on full, half, entry, and exit intervals. |
| Beta connectors and common artificial ownership | **Pass.** Pure mask connectors alter (41.20), and mixed connectors have the finite symbol expansion (41.21a). All \(\omega\)-derivative terms cancel in the common identity (41.22); no isolated artificial residue or connector-axis image is reintroduced. |
| Polylogarithmic \(b\) and profile derivatives | **Pass.** The gamma and height bounds (41.23) cost only \(P_X\ll_\varepsilon X^\varepsilon\). Cubic physical-height decay is retained at the diagonal and radial ridges. |
| Signed diagonal exclusion | **Pass.** The nonintegrable \(K_C\) is never placed in (41.8) or localized pointwise by Morse. It remains under its proved signed logarithmic section with common face-log ownership. |
| No coefficient-sum or downstream reopening | **Pass.** No \(h,q,x,j\) summation is repeated. Bounded-alpha, double-bounded, complete beta transition, M9-M1, M9, and the Gauss-circle target are not asserted. |

## 6. Dependencies and exact artifacts used

Only the assigned context was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/blind_terminal_symbol_definition.md`;
5. `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/quantitative_terminal_symbol_attack.md`;
6. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/reports/complete_translation_difference_attack.md`;
7. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/reports/translation_difference_hostile_audit.md`;
8. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/synthesis.md`;
9. the Round-41 task brief.

Imported accepted facts are the beta-slab gamma normal form, raw terminal
factor ledger, cellwise exact phase-removal rule, cubic physical-height
profile bounds, uniform normalized smooth Mellin seminorms, signed
diagonal Cauchy section, one-count endpoint/axial/artificial ownership,
and exact signed Morse chart.  Equations (41.16)--(41.45), including the
one-count factorization, cancellation-preserving four-region estimate,
moving-face convolution, and exact off-diagonal/smooth Morse bound, are
derived here.  No computation, web source, or external theorem was used.

## 7. Recommended state effect

**Promote, after the blind and hostile seams validate the formulae, the
complete large-alpha off-diagonal/smooth product-cell lemma (41.8).**
Compose it with the already proved signed diagonal Cauchy section to
promote the large-alpha scope of
`M9-M1-beta-axial-subtracted-terminal-symbol-bound` in its corrected
hybrid form.

Retain the cellwise phase-removed normalization and conditional
coefficient-sum reductions unchanged.  The latter can now be invoked for
the complete large-alpha saddle/entry/exit package once the conductor
accepts the present seam; it need not be recalculated.

Retain bounded-alpha, double-bounded, and full beta-transition assembly as
open.  Reject any return to an all-absolute norm for \(K_C\), separate
absolute bounds on the two terms of the Round-40 translation identity,
pointwise Morse localization before the signed Cauchy section, or
stratumwise estimation of an artificial cutoff before the common
identity (41.22) is formed.
