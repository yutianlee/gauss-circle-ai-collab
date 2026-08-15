# Round 40 discovery report: an unremoved signed radial Cauchy tail defeats the absolute mixed norm

Task: complete_translation_difference_attack  
Role: discovery  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result

The proposed \(F_{Ly}/F_{yy}\) identity is correct, and it controls the
complete second translation divided difference when its two terms are
kept recombined. It does **not** prove the frozen mixed norm. The mixed
norm is false already in the value term of the exact singular hard-top
regularizer.

For one nonzero phase-removed singular cell, write

\[
 A(L)=-1-\frac b2-i(L+\beta),\qquad
 D(L,\nu)=A(L)+\frac i2(L-\nu),
 \tag{40.1}
\]

and let \(H^\circ\) be its numerator, with the hard-top and radial
denominators omitted. The exact Round-39 regularizer splits as

\[
 \mathcal R_A[H^\circ](L,\nu)
 =\underbrace{-\frac{iH^\circ(L,L)}{2A(L)D(L,\nu)}}_{K_{\rm C}(L,\nu)}
 +\underbrace{\frac{H^\circ(L,\nu)-H^\circ(L,L)}
 {(L-\nu)D(L,\nu)}}_{K_{\rm dd}(L,\nu)}.
 \tag{40.2}
\]

The second term is an absolutely integrable divided-difference symbol
with the requested value, derivative, moving-trace, and normalized-Morse
capacity. The first term is a signed radial Cauchy tail. Since

\[
 D(L,\nu)=-\frac{i\nu}{2}+O(1+|L|),\qquad |\nu|\to\infty,
 \tag{40.3}
\]

one has, for fixed \(L\),

\[
 \mathcal R_A[H^\circ](L,\nu)
 =\frac{H^\circ(L,L)}{A(L)\nu}+O_{L,X,b}(|\nu|^{-2}).
 \tag{40.4}
\]

The actual height profile satisfies

\[
 \widehat\phi(b+iL)
 =\frac{\Phi''(1)+o(1)}{(b+iL)(b+1+iL)(b+2+iL)},
 \qquad \Phi''(1)=\frac{2\pi^2}{3},
 \tag{40.5}
\]

and the normalized phase-removed gamma factor is bounded above and below
on either saddle cell. Thus, for any ordinary beta cell on which its mask
is nonzero and all sufficiently large \(\lambda\),

\[
 |H^\circ(L,L)|\asymp_b \lambda^{-3},\qquad |A(L)|\asymp\lambda
 \quad (|L+\beta|\asymp\lambda).
 \tag{40.6}
\]

Consequently

\[
 \int_{-V}^{V}|\mathcal R_A[H^\circ](L,\nu)|\,d\nu
 \asymp_b \lambda^{-4}\log\!\frac{V}{\lambda}+O_b(\lambda^{-4})
 \quad (V/\lambda\to\infty),
 \tag{40.7}
\]

up to the permitted polylogarithmic factors coming from \(b\) and the
unit-modulus radial powers. In particular the integral over
\(\mathbb R_\nu\) is infinite. This is not a power loss in \(\lambda\):
it is a sharp, nonuniform outside-height logarithm, and no
\(X^\varepsilon\) constant can absorb it as \(V\to\infty\) with \(X\)
fixed.

There is no contradiction with the accepted Round-38 Cauchy theorem. The
tail is signed, and

\[
 \int_{-V}^{V}\frac{d\nu}{D(L,\nu)}
 =2i\{\Log D(L,V)-\Log D(L,-V)\}\longrightarrow -2\pi
 \tag{40.8}
\]

for the continuous left-half-plane branch
\(\operatorname {Arg}\in(\pi/2,3\pi/2)\). Round 38 proves precisely a
signed Cauchy limit, not absolute \(L^1(d\nu)\).

Thus the first exact survivor is earlier than
\(\mathfrak E_H\): it is \(K_{\rm C}\) in (40.2). The viable replacement
is a hybrid interface: keep \(K_{\rm C}\) as an explicitly integrated
signed Cauchy module, and impose the absolute mixed norm only on
\(K_{\rm dd}\) and the smooth ordinary-\(\mu\) shares. Sections
3.2--3.4 prove this corrected hybrid cell theorem, including moving
sections and the exact incomplete-Morse operator. The already closed
\((h,q,x,j)\) sum was not repeated.

## 2. Exact statement and hypotheses

Use the lawful terminal line and parameters

\[
 \sigma=\frac54,\qquad b=\frac1{\log(2X)},\qquad
 \zeta=a+b,\qquad
 \kappa=\frac34+\frac\zeta2<1,
 \tag{40.9}
\]

with \(a+b<1/2\) and \(a/2+b<1/4\). Freeze one actual cell
\((j,h,q,x,\beta,\pm)\), put

\[
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
 \alpha=L+\beta,\qquad y=L-\nu,
 \tag{40.10}
\]

and restrict to one signed saddle/entry/exit interval \(I_\lambda\), on
which \(|\alpha|\asymp\lambda\) and \(|I_\lambda|\ll\lambda\). The
stationary points are \(L_\pm=\pm\lambda-\beta\). Also

\[
 \eta=\frac{L+\nu}{2}+\beta,\qquad
 \rho=-1-\frac b2-i\eta=D(L,\nu).
 \tag{40.11}
\]

The exact diagonal gamma factors from the beta normal form are

\[
 R_\alpha(\alpha)=
 \frac{\Gamma((1+\sigma+\zeta/2)/2+i\alpha/2)}
 {\Gamma((2-\sigma-\zeta/2)/2-i\alpha/2)},
 \quad
 R_\beta(\beta)=
 \frac{\Gamma((\sigma-\zeta/2)/2+i\beta/2)}
 {\Gamma((1-\sigma+\zeta/2)/2-i\beta/2)}.
 \tag{40.12}
\]

At the frozen \(x\)-integrand level, \(I_1(\rho)/\rho\) contributes
\(x^{\rho-1/2}/\rho\). Its real power \(x^{-3/2-b/2}\), the radial
integration, and the radial oscillation independent of \(L,\nu\) are
outside the symbol, while its exact unit-modulus factor splits into an
\(L\)-phase and a \(\nu\)-phase. The coefficient phases
\(q^{-iL}(hq)^{-i\beta}\), the unit-modulus parts of the spatial scale
and floor powers, and the explicit \(2,\pi\) powers in the exact gamma
factorization split in the same way. Remove their complete \(L\)-phase,
including the signed gamma phase, and extract the real
\(\lambda^\kappa\) factor. This defines exactly

\[
 \mathcal G_\pm^\circ(L;\lambda)
 :=\lambda^{-\kappa}e^{-i\Psi_\pm(L)}
 \{\text{the full \(L\)-dependent product in (40.12) and the
 retained unit-modulus powers}\},
 \tag{40.13}
\]

where \(\Psi_\pm\) is the complete stationary phase of that displayed
product, not an additional approximation. All remaining
\(\nu\)-dependent unit powers form

\[
 p_{j,x,b}(\nu)=\widehat\phi(b+i\nu)e^{i\omega_{j,x}\nu},
 \qquad |\omega_{j,x}|\ll\log(2X).
 \tag{40.14}
\]

The bounded factor \(C_{j,h,q,x,\beta,\pm}\) contains the exact compact
\(R_\beta\) factor, beta mask or beta-connector value, and the remaining
fixed unit phases. Hence the singular \(u^{-1}\) numerator factors
**exactly** as

\[
 \boxed{H^\circ_\pm(L,\nu)
 =C_{j,h,q,x,\beta,\pm}
  \mathcal G_\pm^\circ(L;\lambda)p_{j,x,b}(\nu).}
 \tag{40.15}
\]

Beta is fixed under \(\partial_L|_\nu\). On the terminal vertical
\(\Re\rho=-1-b/2\), so the artificial-pole cutoff has no terminal pole;
the common \(G-E_1-R_1=0\) ownership derivatives cancel, and its already
extracted residue is not inserted in (40.15). Saddle entry and exit alter
the \(L\)-integration interval, not (40.15).

Stirling with one and two logarithmic derivatives, on either signed
branch, gives

\[
 |\partial_L^m\mathcal G_\pm^\circ(L;\lambda)|
 \ll_m \lambda^{-m},\qquad m=0,1,2,
 \tag{40.16}
\]

uniformly on fixed-ratio entry/exit collars. The actual profile gives,
for \(0\le k\le2\),

\[
 |p_{j,x,b}^{(k)}(\nu)|
 \ll b^{-C}(1+\log(2X))^k(1+|\nu|)^{-3},
 \quad
 \|p_{j,x,b}^{(k)}\|_1\ll b^{-C}(1+\log(2X))^k.
 \tag{40.17}
\]

Every factor on the right of (40.16)--(40.17) is
\(O_\varepsilon(X^\varepsilon)\).

Only (40.2) is subjected to the Plemelj regularizer. A smooth top
remainder or interior profile instead has the exact ordinary-\(\mu\)
form

\[
 K_{j,\mathrm{sm}}^\circ(L,\nu)=
 C\mathcal G_\pm^\circ(L;\lambda)
 \frac{p_{j,x,b}(\nu)\widehat W_j(a+i(L-\nu))}{D(L,\nu)}.
 \tag{40.18}
\]

The character \(\chi_4(q)\), stationary numerator
\((D_j/q)\lambda\), exact real \(h,D_j,x\) monomial, the remaining two
contour factors \((2\pi)^{-2}\) for the singular share (and all three
ordinary factors for (40.18)), radial integration, floors, stars, and the
external \(-4X^{1/4}\Re\{e(1/8)\,\cdot\}/\pi\) are not hidden in
\(H^\circ\) or \(K^\circ\).

## 3. Proof or derivation

### 3.1 Fixed-physical-height coordinates and the exact identity

Set

\[
 F(L,y)=H^\circ(L,L-y).
 \tag{40.19}
\]

At fixed physical \(\nu\), \(y=L-\nu\) has derivative one, so

\[
 \partial_LH^\circ(L,\nu)=F_L(L,y)+F_y(L,y),
 \qquad
 (\partial_L+\partial_\nu)H^\circ(L,L)=F_L(L,0).
 \tag{40.20}
\]

The fundamental theorem of calculus, used twice, gives

\[
\begin{aligned}
 \mathfrak E_H(L,\nu)
 &:=\frac{\partial_LH^\circ(L,\nu)
 -(\partial_L+\partial_\nu)H^\circ(L,L)}{y}
 -\frac{H^\circ(L,\nu)-H^\circ(L,L)}{y^2}\\
 &=\int_0^1F_{Ly}(L,ty)\,dt
   +\int_0^1tF_{yy}(L,ty)\,dt.
 \tag{40.21}
\end{aligned}
\]

This sign and weight can be checked without any estimate: for
\(F(L,y)=a(L)y+b(L)y^2/2\), the \(y\)-part of the left side is \(b/2\),
as is \(\int_0^1tF_{yy}\,dt\). A formula containing
\(-F_y(L,0)/y-\int_0^1(1-t)F_{yy}\,dt\) would give
\(-a/y-b/2\) and is not equal to the declared \(\mathfrak E_H\).

For the exact factorization (40.15), abbreviate
\(G= C\mathcal G_\pm^\circ\) and \(p=p_{j,x,b}\). Then

\[
 F(L,y)=G(L)p(L-y),\quad
 F_{Ly}=-G'p'-Gp'',\quad F_{yy}=Gp'',
 \tag{40.22}
\]

where the arguments of \(p',p''\) are \(L-y\). Consequently (40.21)
is the exact combined expression

\[
 \boxed{
 \mathfrak E_H
 =G'(L)\frac{p(\nu)-p(L)}{y}
 -G(L)\frac{p'(L)}{y}
 -G(L)\frac{p(\nu)-p(L)}{y^2}.}
 \tag{40.23}
\]

This also exposes a necessary warning. Bounding the two integrals in
(40.21) separately destroys the cancellation of the \(Gp''\) terms. In
the physical-center regime \(|\nu|=O(1)\),
\(|L|\asymp|y|\asymp\lambda\), separate absolute bounds cost
\(1/\lambda\), whereas their combination in (40.23) costs
\(1/\lambda^2\). The integral identity is useful only before this
cancellation is discarded.

### 3.2 Mixed-derivative ledger for the absolutely integrable part

For \(K_{\rm dd}\) in (40.2), fixed-\(\nu\) differentiation gives

\[
 \partial_LK_{\rm dd}
 =\frac{\mathfrak E_H}{D}
 +\frac{i\{H^\circ(L,\nu)-H^\circ(L,L)\}}{2yD^2}.
 \tag{40.24}
\]

All apparent diagonal singularities are continuous by (40.23). Split
the \(\nu\)-line into the physical center \(|\nu|\le |L|/2\), the top
diagonal \(|L-\nu|\le |L|/2\), the radial ridge
\(|L+\nu+2\beta|\le |L|/2\), and their complement. Equations
(40.16)--(40.17) give respectively:

* in the physical center, \(|y|,|D|\asymp\lambda\), so the \(p(\nu)\)
  terms in (40.2), (40.23), and (40.24) have \(L^1(d\nu)\) sizes
  \(O_\varepsilon(X^\varepsilon\lambda^{-2})\) and
  \(O_\varepsilon(X^\varepsilon\lambda^{-3})\);
* on the top diagonal, \(D\asymp\lambda\) and the integral divided
  differences are bounded by \(p'\) and \(p''\); the cubic height tail
  gives the same or a smaller bound;
* on the radial ridge, \(y\asymp\lambda\), while
  \(p(\nu),p(L)=O_\varepsilon(X^\varepsilon\lambda^{-3})\);
  integration of \(1/|D|\) costs at most one logarithm and is smaller
  than the target;
* on the complement, both denominators or the height profile supply
  summable decay.

It follows that

\[
 \sup_{L\in I_\lambda}\int_{\mathbb R}|K_{\rm dd}(L,\nu)|\,d\nu
 \ll_\varepsilon X^\varepsilon\lambda^{-2},
 \tag{40.25}
\]

and

\[
 \int_{I_\lambda}\int_{\mathbb R}
 |\partial_LK_{\rm dd}(L,\nu)|\,d\nu\,dL
 \ll_\varepsilon X^\varepsilon\lambda^{-2}.
 \tag{40.26}
\]

The same decomposition after substitution on every affine moving face
gives

\[
 \sum_\gamma\int_{I_\lambda}
 |K_{\rm dd}(L,\gamma(L))|\,dL
 \ll_\varepsilon X^\varepsilon\lambda^{-2}.
 \tag{40.27}
\]

The exact normalized Morse remainder also has this capacity for
\(K_{\rm dd}\). Indeed, if \(L=L(\tau)\), \(J=dL/d\tau\), and
\(J(0)=\sqrt\lambda\), its amplitude is

\[
 \frac{J(\tau)}{\sqrt\lambda}K_{\rm dd}(L(\tau),\nu)
 -K_{\rm dd}(L_\pm,\nu).
 \tag{40.28}
\]

The incomplete Fresnel BV estimate bounds (40.28) by its saddle value,
its \(\tau\)-variation, and its endpoint traces. Since
\(J\asymp\sqrt\lambda\), conversion of its first variation back to \(L\)
is exactly (40.26), while the Jacobian variation is bounded on the exact
Morse chart. Equations (40.25)--(40.27) therefore give

\[
 \mathfrak R_\lambda^{\rm Morse}(K_{\rm dd})
 \ll_\varepsilon X^\varepsilon\lambda^{-2},
 \tag{40.29}
\]

uniformly for either Hessian sign and for incomplete entry/exit intervals.

For a smooth share (40.18), fixed-\(\nu\) differentiation is simply

\[
 \partial_LK_{j,\mathrm{sm}}^\circ
 =C p(\nu)\left\{
 \frac{G'\widehat W_j+G\partial_y\widehat W_j}{D}
 +\frac{iG\widehat W_j}{2D^2}\right\}.
 \tag{40.30}
\]

Rapid vertical decay of \(\widehat W_j(a+iy)\),
(40.16)--(40.17), and the same three-ridge decomposition prove
(40.25)--(40.29), in fact with one spare inverse power in the integrated
derivative. No Plemelj or second logarithmic subtraction is used on
(40.18).

### 3.3 Exact obstruction from the signed Cauchy part

For \(|\nu|\ge 4(|L|+|\beta|+1)\), (40.3) is uniform. Equation (40.17)
gives \(H^\circ(L,\nu)=O_{L,X,b}(|\nu|^{-3})\), whereas
\(H_0^\circ(L):=H^\circ(L,L)\) is independent of \(\nu\). Therefore

\[
 K_{\rm dd}(L,\nu)=O_{L,X,b}(|\nu|^{-2}),\qquad
 K_{\rm C}(L,\nu)=\frac{H_0^\circ(L)}{A(L)\nu}
 +O_{L,X,b}(|\nu|^{-2}),
 \tag{40.31}
\]

which proves (40.4). Formula (40.5), the absence of gamma zeros, and
(40.16) prove (40.6) on any nonzero ordinary beta mask cell. The
\(O(|\nu|^{-2})\) term cannot cancel a nonzero \(1/\nu\) coefficient.
Integrating (40.31) proves the sharp logarithm (40.7).

Fixed-\(\nu\) differentiation has the analogous tail

\[
 \partial_L\mathcal R_A[H^\circ](L,\nu)
 =\frac{\partial_L\{H_0^\circ(L)/A(L)\}}{\nu}
 +O_{L,X,b}(|\nu|^{-2}).
 \tag{40.32}
\]

The derivative coefficient is generically
\(O_\varepsilon(X^\varepsilon\lambda^{-4})\), because the residual
\(\nu\)-unit phase in (40.14), evaluated at \(\nu=L\), may cost
\(O(\log X)\). Thus a \(V\)-truncated derivative norm has capacity up
to \(O_\varepsilon(X^\varepsilon\lambda^{-3}\log V)\) after the
\(L\)-integration. The value divergence (40.7) already disproves the
frozen norm without any genericity assertion about (40.32).

By contrast, the coefficient

\[
 c_{\rm C}(L):=-\frac{iH_0^\circ(L)}{2A(L)}
 \tag{40.33}
\]

satisfies

\[
 \|c_{\rm C}\|_{L^\infty(I_\lambda)}
 \ll_\varepsilon X^\varepsilon\lambda^{-4},\qquad
 \operatorname {Var}_{I_\lambda}c_{\rm C}
 \ll_\varepsilon X^\varepsilon\lambda^{-3}.
 \tag{40.34}
\]

Together with the exact logarithm (40.8), (40.34) shows why this is a
small, target-safe **signed** module even though it is not an absolute
symbol.

### 3.4 Exact finite-section BV and Morse control of the Cauchy module

The signed module can be completed quantitatively, rather than merely
left as a proposed repair. For the actual physical section put

\[
 p_{U,V}(L)=\max(-V,L-U),\qquad
 q_{U,V}(L)=\min(V,L+U)
 \tag{40.35}
\]

when \(p_{U,V}<q_{U,V}\), and define

\[
\begin{aligned}
 J_{U,V}(L)
 &:=\int_{p_{U,V}(L)}^{q_{U,V}(L)}
       \frac{d\nu}{D(L,\nu)}\\
 &=2i\{\Log D(L,q_{U,V}(L))
          -\Log D(L,p_{U,V}(L))\}.
 \tag{40.36}
\end{aligned}
\]

There are only the four affine endpoint choices
\(\gamma(L)\in\{-V,V,L-U,L+U\}\). In each case

\[
 D(L,\gamma(L))
 =-1-\frac b2-\frac i2\{L+\gamma(L)+2\beta\},
 \tag{40.37}
\]

and direct comparison of the two endpoint distances gives

\[
 \left|\log\frac{|D(L,q_{U,V})|}{|D(L,p_{U,V})|}\right|
 \ll \log(2+\lambda).
 \tag{40.38}
\]

This is uniform in \(U,V\): if one endpoint is within \(O(1)\) of the
radial center, the intersection constraints put the other within
\(O(1+|L|)\); if neither is close, their distance ratio is bounded by
\(1+O(|L|)\). The argument difference in (40.36) is at most \(\pi\).
Hence

\[
 \|J_{U,V}\|_\infty\ll\log(2+\lambda).
 \tag{40.39}
\]

On any affine cell, \(\gamma'\in\{0,1\}\) and

\[
 \frac d{dL}\Log D(L,\gamma(L))
 =-\frac{i(1+\gamma')}{2D(L,\gamma(L))}.
 \tag{40.40}
\]

The real part of \(D\) is \(-1-b/2\), and the imaginary part in (40.37)
is affine with slope \(1/2\) or \(1\). Therefore

\[
 \int_{I_\lambda}\frac{dL}{|D(L,\gamma(L))|}
 \ll\log(2+\lambda).
 \tag{40.41}
\]

The min/max switches agree in value and a collapsed section has
\(J_{U,V}=0\). Summing the finitely many affine cells yields

\[
 \|J_{U,V}\|_\infty+\operatorname {Var}_{I_\lambda}J_{U,V}
 \ll\log(2+\lambda),
 \tag{40.42}
\]

uniformly in both height cutoffs. Combining (40.34) and (40.42),

\[
\begin{aligned}
 \left\|c_{\rm C}J_{U,V}\right\|_\infty
 +\operatorname {Var}_{I_\lambda}(c_{\rm C}J_{U,V})
 &\ll_\varepsilon
 X^\varepsilon\lambda^{-3}\log(2+\lambda)\\
 &\ll_\varepsilon X^\varepsilon\lambda^{-2}.
 \tag{40.43}
\end{aligned}
\]

Thus the diagonal Cauchy tail is target-safe after its exact signed
\(\nu\)-integration. Under the prescribed symmetric exhaustion,
\(J_{U,V}(L)\to-2\pi\), uniformly with its affine-cell BV control, so the
limit is
\(-2\pi c_{\rm C}(L)=i\pi H_0^\circ(L)/A(L)\).

Finally apply the exact Morse map only to the scalar physical-height
amplitude \(c_{\rm C}(L)J_{U,V}(L)\), not to
\(|c_{\rm C}(L)/D(L,\nu)|\). The elementary incomplete-Fresnel BV bound

\[
 \left|\int_a^b e^{\pm i\tau^2/2}a(\tau)\,d\tau\right|
 \ll \|a\|_\infty+\operatorname {Var}a
 \tag{40.44}
\]

and the exact Jacobian conversion used in (40.28) show from (40.43) that
both the leading half/full Fresnel term and the normalized
varying-amplitude Morse remainder are
\(O_\varepsilon(X^\varepsilon\lambda^{-2})\), uniformly through entry
and exit. This proves the signed Cauchy part of the corrected hybrid
cell theorem, including its moving-section and Morse seams.

### 3.5 Saddles, entry/exit, connectors, ownership, traces and Morse scope

The obstruction is unchanged on the negative saddle: (40.3) is
independent of the saddle sign in modulus, and (40.5) holds at both
infinite ends. Entry and exit truncate the \(L\)-interval but do not
truncate the outside-\(\nu\) tail. Half-Fresnel values therefore do not
repair (40.7).

Beta masks and beta connectors only multiply (40.33) by a bounded factor
at fixed beta. Some connector cells may vanish at special beta values,
but the uniform theorem includes ordinary nonzero mask cells, so such
zeros cannot repair it. On the terminal line the common artificial
ownership identity cancels cutoff derivatives exactly. Its separately
extracted artificial residue is \(O_{X,b}((1+|\nu|)^{-3})\), and axial
and corner shares have bounded physical-height support. None has a
matching \(1/\nu\) coefficient which could cancel (40.31) inside a
frozen absolute cell norm.

The affine traces of \(K_{\rm dd}\) and all smooth shares pass (40.27).
Traces of \(K_{\rm C}\) are also small coefficientwise, but the interior
absolute value integral remains infinite. Equations (40.35)--(40.44)
show the correct order: integrate the exact Cauchy logarithm over the
physical section first, then apply the Morse operator to the resulting
BV amplitude. An \(L^1(d\nu)\) Morse norm for the unintegrated
\(K_{\rm C}\) is neither true nor needed.

This completes every requested seam at the point where the frozen norm
fails. The failure occurs before, and independently of, the downstream
coefficient and resonance sum.

## 4. First doubtful or unproved step

The first failed step is the assertion that the complete singular
regularizer \(\mathcal R_A[H^\circ]\) belongs to
\(L^1(\mathbb R_\nu)\) at fixed \(L\). It does not. Its exact first
survivor is

\[
 \boxed{K_{\rm C}(L,\nu)
 =-\frac{iH^\circ(L,L)}{2A(L)D(L,\nu)},}
 \tag{40.45}
\]

with sharp truncated absolute capacity
\(X^\varepsilon\lambda^{-4}\log(V/\lambda)\). This precedes the second
translation divided difference. The \(F_{Ly}/F_{yy}\) calculation
successfully controls \(K_{\rm dd}\), but cannot alter (40.45).

The smallest viable replacement theorem is the hybrid decomposition

\[
 \mathcal R_A[H^\circ]=\frac{c_{\rm C}(L)}{D(L,\nu)}+K_{\rm dd},
 \qquad
 \mathfrak M_\lambda(K_{\rm dd})
 \ll_\varepsilon X^\varepsilon\lambda^{-2},
 \tag{40.46}
\]

together with the signed finite-section and exact-Morse theorem
(40.35)--(40.44) for \(c_{\rm C}(L)/D\). Thus the corrected **hybrid**
cell theorem is proved here. What fails is only the stronger demand that
the unintegrated complete regularizer itself have an absolute
\(L^1(d\nu)\) mixed norm. Composing the corrected cell theorem with the
already accepted one-count global ledger belongs to the conductor; it
does not require reopening the coefficient sum.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Exact phase-removed cell factorization | Pass. Equations (40.12)--(40.15) separate the exact gamma, frozen radial \(x^\rho/\rho\), height, beta, and unit-phase factors. The stationary numerator and all physical prefactors remain outside. |
| Fixed-\(\nu\) to \((L,y)\) conversion | Pass. Equation (40.20) retains the diagonal derivative \(\partial_L+\partial_\nu\). |
| Second divided-difference identity | Pass only in combined form. Equations (40.21)--(40.23) are exact; separate absolute estimates of \(F_{Ly}\) and \(F_{yy}\) lose one power by destroying their \(p''\) cancellation. |
| Singular versus smooth shares | Pass. Only (40.2) is regularized. Smooth shares keep the ordinary-\(\mu\) formula (40.18) and satisfy the mixed estimates by (40.30). |
| Gamma, radial, and profile derivative ledger | Pass. Phase removal gives (40.16); the actual radial unit phase costs at most powers of \(\log X\); the height bundle satisfies (40.17). |
| Full absolute mixed norm | **Fail.** The exact Cauchy term (40.45) has the nonzero \(1/\nu\) tail (40.31), hence (40.7). |
| Both saddles and entry/exit | Fail in the same way on both signs. Entry/exit changes only the \(L\)-interval, and half-Fresnel coefficients do not remove the outside-height tail. |
| Moving faces and exact Morse remainder | Pass for \(K_{\rm dd}\) and smooth shares by (40.27)--(40.29). The Cauchy term passes after the exact signed integration (40.35)--(40.43), followed by the scalar BV Morse bound (40.44); an absolute \(L^1(d\nu)\) Morse remainder for the unintegrated tail remains false. |
| Beta connectors and common ownership | No repair. They multiply the tail coefficient, while extracted artificial/axial/corner modules have \(O(|\nu|^{-3})\) or compact height support and cannot cancel \(1/\nu\) cellwise. |
| \(b\) and height uniformity | Pass at polylogarithmic cost for the renormalized and smooth parts. The failure is logarithmic in the exhaustion \(V\), not a power of \(b^{-1}\), \(X\), or \(\lambda\). |
| External normalization and downstream scope | Pass. No character, stationary numerator, coefficient monomial, contour constant, radial sum, floor, star, or external \(X^{1/4}\) factor was hidden in the symbol. The closed \(h,q,x,j\) sum was neither repeated nor assumed to prove the missing norm. |

## 6. Dependencies and exact artifacts used

Only the assigned context was used:

1. protocol.md;
2. state/proof_obligations.yml;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/quantitative_terminal_symbol_attack.md;
5. rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/terminal_symbol_hostile_audit.md;
6. rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/synthesis.md;
7. rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md;
8. rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md;
9. rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md;
10. the Round-40 task brief and the conductor's retraction confirming
    the chain-rule identity (40.21).

Imported accepted facts are the exact beta gamma factorization, the
cellwise phase-removal and external-factor ownership, the singular/smooth
split, the signed Plemelj regularizer, the actual cubic height asymptotic,
the exact Morse normal form, the common artificial/axial ownership, and
the fixed-\(X\) signed Cauchy existence theorem. Equations
(40.19)--(40.46), including the sharp \(1/\nu\) survivor and its exact
signed finite-section/Morse repair, were derived
here. No numerical experiment, literature theorem, or unlisted project
artifact was used.

## 7. Recommended state effect

**Reject the frozen full absolute mixed-norm statement as written.** A
nonzero singular hard-top cell contains the exact signed Cauchy term
(40.45), whose physical-height absolute integral diverges logarithmically.
Round-38 signed existence cannot be upgraded to that absolute norm.

**Revise and promote the corrected hybrid cell theorem.** Replace the
singular part of the target by the hybrid decomposition (40.46):

* promote, after conductor verification, the exact coordinate identity
  (40.21), its cancellation-preserving product formula (40.23), and the
  mixed estimates (40.25)--(40.30) for \(K_{\rm dd}\) and the smooth
  ordinary-\(\mu\) shares;
* promote, after conductor verification, \(c_{\rm C}(L)/D(L,\nu)\) as a
  signed Cauchy module with coefficient bounds (40.34), exact
  finite-section sup/BV bounds (40.35)--(40.43), and incomplete-Morse
  control (40.44);
* record the sharp rejected shortcut: the complete Plemelj regularizer is
  not an \(L^1(d\nu)\) symbol merely because its signed Cauchy limit
  exists;
* do not change the already proved conditional coefficient-sum reduction,
  and do not promote the complete beta transition, M9-M1, M9, or the
  Gauss-circle target.
