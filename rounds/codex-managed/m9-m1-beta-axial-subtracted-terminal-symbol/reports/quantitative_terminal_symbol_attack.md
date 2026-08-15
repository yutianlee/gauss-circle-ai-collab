# Round 39 discovery report: the terminal symbol must be cellwise and phase removed

Task: `quantitative_terminal_symbol_attack`  
Role: discovery  
Allocation: 100% analytical/algebraic; no computation or external theorem

## 1. Result

The frozen estimate is not yet proved, but its normalization can be made
precise and the first actual quantitative survivor can be isolated.

There are three different objects which must not be denoted by the same
symbol.

1.  On a fixed signed saddle cell, after the full stationary phase has
    been removed, the hard-top/radial two-denominator kernel is a
    **pre-stationary-numerator** symbol.  In the separated model it has
    value and fixed-physical-height derivative of sizes
    \(\lambda^{-2}\) and \(\lambda^{-3}\).
2.  The post-endpoint stationary numerator is exactly
    \((D_j/q)\lambda\).  Multiplication therefore changes the value scale
    to
    \[
      \frac{D_j}{q}\lambda\,\lambda^{-2}
      =\frac{D_j}{q\lambda}
      =\frac{D_j}{q^2\theta_j(x)},
      \qquad \theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j}.
      \tag{39.1}
    \]
3.  Only after (39.1) does one multiply by the actual
    \(h,j,x\)-monomial, \(\chi _4(q)\), floors, stars, contour constants,
    and the external \(X^{1/4}\) normalization.  This is the contribution
    to the physical M1 sum, not the object satisfying the bare
    \(\lambda^{-2}/\lambda^{-3}\) bounds.

The limiting aggregate is summed over \(j,h,q\) and integrated over
\(x\), so it has no single value of
\(\lambda=\pi q\sqrt{Xx}/D_j\).  Moreover, if the exact stationary phase
is left inside a cell symbol, then
\[
 \partial_L\Psi_\pm(L)=\log\frac{|L+\beta|}{\lambda},
 \tag{39.2}
\]
and the derivative of the oscillatory factor is generically order one
on an entry/exit collar.  It cannot obey a \(\lambda^{-3}\) symbol bound
when the underlying value is \(\lambda^{-2}\).  Thus the target is
well typed only for a **cellwise, fully phase-removed** symbol
\(K_{j,h,q,x,\pm}^{\circ}\), not for the limiting aggregate or for the
raw oscillatory cell.

With that correction, the separated hard-top kernel passes, and the
smooth actual spatial Mellin profiles can also be accommodated.  Their
fixed-\(\nu\) derivative has a translated-ridge capacity
\(\asymp_b\lambda^{-4}\) at \(\nu=L-O(1)\).  Pointwise formulation
therefore needs the truncated harmonic weight
\[
 w_{X,b}^{\rm ridge}(\nu)
 \asymp_b \frac{{\bf1}_{1\le |\nu|\le C X}}{1+|\nu|}
       +(1+|\nu|)^{-2},
 \qquad \|w_{X,b}^{\rm ridge}\|_1\ll_b\log(2X).
 \tag{39.3}
\]
This is allowed by the frozen polylogarithmic norm, but it shows that a
fixed, \(X\)-independent profile weight is too strong.  A cleaner and
strictly weaker sufficient interface is the mixed physical-height norm
in (39.22) below.

Conditional on that corrected cellwise mixed norm, every leading
\(h,q,j,x\) sum can be executed.  Before the external \(X^{1/4}\), the
two signed saddles together are \(O(\log^C X)\).  The formal resonance
\(q=2D_j\) is even and hence is annihilated exactly by
\(\chi_4(q)\); the nearest nonzero odd term has
\(|q-2D_j|\ge1\) and capacity \(O((D_j\sqrt X)^{-1})\).  Hence the
leading separated saddle package is target sized after restoring the
external normalization.

The first unproved actual coefficient is the phase-removed complete
second translation divided difference (39.17), with its moving traces,
on the hard-top entry/exit and common artificial-ownership cells.  Round
38 proves that its signed height limit exists with a fixed-\(X\)
constant; it supplies neither the mixed \(O(X^\varepsilon\lambda^{-2})\)
norm nor the extra inverse \(\lambda\) required for its fixed-\(\nu\)
derivative.  This is a scoped survivor, not a failure of the intended
beta strategy.

## 2. Exact statement and hypotheses

Fix the legal terminal line and the actual physical line
\[
 \sigma=c'=\frac54,
 \qquad b=\frac1{\log(2X)},
 \qquad 0\le a<a_0,
 \qquad a+b<\frac12,
 \qquad \frac a2+b<\frac14.
 \tag{39.4}
\]
Put
\[
 \zeta=a+b,\qquad
 r=\sigma-\frac\zeta2,\qquad
 p=\sigma+\frac\zeta2,\qquad
 \kappa=p-\frac12=\frac34+\frac\zeta2<1.
 \tag{39.5}
\]
Thus \(1<r<2\).  In beta-slab coordinates,
\[
 u=a+i(L-\nu),\qquad v=b+i\nu,qquad
 s=\sigma+i\left(\frac L2+\beta\right),
 \qquad \alpha=L+\beta,
 \tag{39.6}
\]
and \(|\beta|\le2B_0\).  The Jacobian from
\((t,\mu,\nu)\) to \((\beta,L,\nu)\) is one.  At fixed physical height,
\[
 \left.\partial_L\right|_\nu:\quad
 \partial_L\mu=1,\quad \partial_Lt=\frac12,\quad
 \partial_L\alpha=1,\quad \partial_L\beta=0.
 \tag{39.7}
\]

The original contour measure is not optional:
\[
 \frac{ds\,du\,dv}{(2\pi i)^3}
   =\frac{dt\,d\mu\,d\nu}{(2\pi)^3}.
 \tag{39.8}
\]
For the singular spatial top profile, the \(u\)-measure and \(1/u\)
factor combine as
\[
 \frac1{2\pi}\frac1{0^++i\mu}
 =\frac12\delta_0(\mu)-\frac{i}{2\pi}
   \operatorname {PV}\frac1\mu.
 \tag{39.9}
\]
The top distribution consumes only the \(u\)-measure.  The \(s\)- and
\(v\)-measures leave an additional factor \((2\pi)^{-2}\).  Therefore
the ordinary PV density has coefficient
\(-i/(2\pi)^3\), before multiplication by the radial coefficient
\(-\pi i\sqrt X\).  A formula displaying only \(-i/(2\pi)\) for the
complete beta-slab density is short by exactly \((2\pi)^{-2}\).

For a fixed \((j,h,q,x,\beta,\pm)\), set
\[
 \theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j},\qquad
 \lambda=q\theta_j(x),\qquad
 A_\beta(L)=\rho_0-i(L+\beta),\qquad
 \rho_0=-1-\frac b2,
 \tag{39.10}
\]
and, with \(y=L-\nu\),
\[
 D_\beta(L,\nu)=A_\beta(L)+\frac{i}{2}y.
 \tag{39.11}
\]
On the terminal line \(D_\beta\) is the actual radial denominator
\(\rho\).  The earlier artificial residue is owned by the common
\(G=E_1+R_1\) ledger and has already been extracted; it is not inserted
again into (39.11).

If \(H(L,\nu;\beta)\) is the complete phase-removed numerator of one
hard-top cell, with the top and radial denominators omitted, define
\[
 \boxed{
 \mathcal R_A[H](L,\nu)
 =-\frac{iH(L,L)}{2A_\beta(L)D_\beta(L,\nu)}
 +\frac{H(L,\nu)-H(L,L)}
 {(L-\nu)D_\beta(L,\nu)}.}
 \tag{39.12}
\]
The divided difference has its continuous diagonal value.  This is what
remains after removing exactly once the combined top delta and
constant-numerator PV/log term.  In the separated model
\(H(L,\nu)=f_b(\nu)=\widehat\phi(b+i\nu)\), (39.12) is
\[
 K_{R_1}^{\circ}(L,\nu)=
 -\frac{i f_b(L)}{2A_\beta\{A_\beta+i(L-\nu)/2\}}
 +\frac{f_b(\nu)-f_b(L)}
 {(L-\nu)\{A_\beta+i(L-\nu)/2\}}.
 \tag{39.13}
\]

Equations (39.9) and (39.12)--(39.13) apply **only** to the singular
\(j=0\) share \(\widehat W_+(u)=u^{-1}+\widehat W_{+,r}(u)\), and only
to its \(u^{-1}\) summand.  The smooth remainder
\(\widehat W_{+,r}\) and every interior \(\widehat W_j\) retain their
ordinary \(d\mu/(2\pi)\) integration.  They are not put through
\(\mathcal R_A\) and acquire no delta, PV, or second top-log subtraction.
For them, \(\mathcal K^\circ\) in (39.14a)--(39.14b) denotes the ordinary
phase-removed factor (39.19).  Thus the canonical notation is the
disjoint pair
\[
 \mathcal K^\circ=
 \begin{cases}
   \mathcal R_A[H_0],&
     j=0,\ \text{singular }u^{-1}\text{ share},\\[2mm]
   f_b(\nu)\widehat W_j(a+i(L-\nu))/D_\beta(L,\nu),&
     j\ge1\text{ or the smooth top remainder}.
 \end{cases}
 \tag{39.13a}
\]
The second line keeps all three ordinary contour measures
\((2\pi)^{-3}d\beta\,d\mu\,d\nu\); the first line uses (39.9), with the
remaining \((2\pi)^{-2}\) as stated above.

The canonical post-stationary normalization is a leading-term template,
not an exact product formula for the whole \(L\)-integrated cell.  Put
\(L_\pm=\pm\lambda-\beta\).  If \(\tau\) is the exact signed Morse
coordinate, \(J_\pm(\tau)=dL/d\tau\), and
\(J_\pm(0)=\sqrt\lambda\), define the normalized exact remainder
\[
 \mathfrak r_{\lambda,\pm}^{\rm Morse}[K](\nu)
 :=\lambda^{-1/2}\!\int_{\tau_P}^{\tau_Q}
 e^{\pm i\tau^2/2}
 \{K(L(\tau),\nu)J_\pm(\tau)
       -K(L_\pm,\nu)\sqrt\lambda\}\,d\tau .
 \tag{39.14a}
\]
Writing
\(\mathfrak F_\pm(P,Q)=\int_{\tau_P}^{\tau_Q}
e^{\pm i\tau^2/2}\,d\tau\), the exact Morse decomposition, in this
normalization, is
\[
 \boxed{\begin{aligned}
 \mathcal C_{j,h,q,x,\pm}^{\rm lead}(\nu)
  &:={\mathfrak F_\pm}\,\chi_4(q)\,\mathcal B_{j,h,x}
     \frac{D_j}{q}\lambda\,
     \mathcal K_{j,h,q,x,\pm}^{\circ}(L_\pm,\nu),\\
 \mathcal C_{j,h,q,x,\pm}(\nu)
  &=\mathcal C_{j,h,q,x,\pm}^{\rm lead}(\nu)
    +\chi_4(q)\mathcal B_{j,h,x}\frac{D_j}{q}\lambda\,
      \mathfrak r_{\lambda,\pm}^{\rm Morse}[\mathcal K^\circ](\nu).
 \end{aligned}}
 \tag{39.14b}
\]
The second line, not its first summand alone, is the whole stationary
cell.  At exact entry or exit \(\mathfrak F_\pm\) is one half of the
full signed Fresnel coefficient when the other endpoint is remote.  The
full phase \(e^{i\Psi_\pm}\) has been removed from
\(\mathcal K^\circ\), and
\[
 \mathcal B_{j,h,x}
 =h^{-r}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \theta_j(x)^p x^{-\sigma-3/4-b/2}.
 \tag{39.15}
\]
No \(q\)-power is hidden in \(\mathcal B\).  The factor
\((D_j/q)\lambda\) is precisely the Round-27 stationary numerator.
The full physical contribution is obtained from (39.14b) using the
remaining exact beta/radial integrations and contour constants, followed
once by
\[
 -\frac4\pi X^{1/4}
 \operatorname {Re}\{e(1/8)\,\cdot\}.
\]
The endpoint and arithmetic modules, radial sides, the full \(v=0\)
vector, its connector-axis shares, combined collisions, and the one
corner are absent from \(\mathcal K^\circ\), because they have already
been assigned by the accepted global ownership identity.  Beta
connectors \(\psi'(\beta)\), and mixed connector factors when present,
remain in \(H\); beta is fixed under (39.7).

## 3. Proof or derivation

### 3.1 The exact regularizer and fixed-height derivative

Apply (39.9) before taking absolute values.  In the PV term add and
subtract \(H(L,L)/(A_\beta y)\).  The identity
\[
 \frac1y\left(\frac1{D_\beta}-\frac1{A_\beta}\right)
 =-\frac{i}{2A_\beta D_\beta}
\]
gives (39.12).  Thus the removed delta and logarithmic terms are one
linear operation; no second top or axial subtraction is permitted.

Let \(H_0(L)=H(L,L)\) and
\(\dot H_0=(\partial_L+\partial_\nu)H(L,L)\).  Since
\(A_\beta'=-i\), \(D_\beta'=-i/2\), and \(y'=1\) at fixed \(\nu\),
direct differentiation yields
\[
\begin{aligned}
 \left.\partial_L\mathcal R_A[H]\right|_\nu={}&
 -\frac{i\dot H_0}{2A_\beta D_\beta}
 +\frac{H_0}{2A_\beta^2D_\beta}
 +\frac{H_0}{4A_\beta D_\beta^2}\\
 &+\frac{\partial_LH(L,\nu)-\dot H_0}{yD_\beta}
 -\frac{H(L,\nu)-H_0}{y^2D_\beta}
 +\frac{i\{H(L,\nu)-H_0\}}{2yD_\beta^2}.
 \tag{39.16}
\end{aligned}
\]
All diagonal singularities cancel by Taylor expansion.  The exact new
coefficient in the middle of (39.16) is
\[
 \boxed{
 \mathfrak E_H(L,\nu)=
 \frac{\partial_LH(L,\nu)-(\partial_L+\partial_\nu)H(L,L)}{L-\nu}
 -\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2}.}
 \tag{39.17}
\]
For \(H=f_b(\nu)\), (39.16) is exactly the already accepted separated
calculus and gives \(\lambda^{-3}w_b(\nu)\).  For the complete
phase-removed numerator, (39.17), together with translated face traces,
is the first coefficient for which no accepted quantitative theorem is
available.

The phase-removal qualification is essential.  If
\(H=e^{i\Psi_\pm}\widetilde H\), then (39.16) contains
\(i\Psi_\pm'\mathcal R_A[\widetilde H]\).  Equation (39.2) is order one
on a fixed-ratio entry/exit collar, producing \(\lambda^{-2}\), not
\(\lambda^{-3}\).  The exact stationary phase belongs to the oscillatory
operator and its incomplete-Fresnel analysis, not to the amplitude
symbol being differentiated.

### 3.2 Reconciliation of the terminal-line and Round-27 ledgers

At the \(x\)-integrand level, the actual terminal coefficient before
stationary phase has real powers
\[
 h^{-r}q^{-p}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \sqrt X\,x^{-3/2-b/2}\lambda^\kappa.
 \tag{39.18a}
\]
Including the external normalization, the radial \(\pi\sqrt X\), the
factor \(2^{-a}\) from the spatial scale, and the PV contour measures,
its exact contour/radial/scale constant is
\(4\,2^{-a}/(2\pi)^3\), before the bounded beta mask and normalized
gamma/Fresnel symbols.  Hence the raw capacity is
\[
 \frac{4\,2^{-a}}{(2\pi)^3}
 X^{3/4-a/2}D_j^a(H_j+1)^b
 h^{-r}q^{-p}x^{-3/2-b/2}\lambda^\kappa
 \times |\hbox{top/radial kernel}|.
 \tag{39.18b}
\]
This explains the unrestricted \(X\)-factor hidden in the fixed-\(X\)
Round-38 tail constant.  It is a pre-stationary raw-cell ledger, not a
contradiction to the post-stationary normalization (39.14a)--(39.14b).

Indeed stationary phase contributes the ordinary \(\lambda^{1/2}\)
width, and \(\kappa+1/2=p\).  Therefore
\[
 q^{-p}\lambda^{\kappa+1/2}=q^{-p}(q\theta_j)^p
 =\theta_j^p.
\]
Moreover the exact radial identity is
\[
 \pi\sqrt X\,x^{-3/2-b/2}\theta_j^p
 =\frac{D_j}{q}\lambda\,\theta_j^p
   x^{-2-b/2}.
\]
These two identities convert (39.18a) exactly into the common
post-stationary prefactor
\(\mathcal B_{j,h,x}(D_j/q)\lambda\).  The exact \(L\)-integration then
splits into the saddle value and the Morse remainder in (39.14b).  Thus
the apparently different terminal-line capacity and Round-27 numerator
are the pre- and post-stationary descriptions of the same cell, without
discarding the varying-amplitude remainder.

### 3.3 Smooth actual profiles and the translated ridge

For an interior spatial profile, or the smooth remainder of the top
profile, the phase-removed height factor has the form
\[
 S_j(L,\nu)=
 \frac{f_b(\nu)\widehat W_j(a+i(L-\nu))}
 {A_\beta(L)+i(L-\nu)/2}.
 \tag{39.19}
\]
It carries no second top delta.  The actual Vaaler profile has
\(\Phi(1)=\Phi'(1)=0\) and
\(\Phi''(1)=2\pi^2/3\).  Three integrations by parts give, with
\(z=b+i\nu\),
\[
 f_b(\nu)=
 \frac{\Phi''(1)+o(1)}{z(z+1)(z+2)}
 \qquad (|\nu|\to\infty).
 \tag{39.20}
\]
In particular \(|f_b(\nu)|\asymp_b|\nu|^{-3}\) for sufficiently large
\(|\nu|\).

Because a nonzero compact smooth \(W_j\) has a nonconstant Mellin
transform tending to zero on vertical lines, there is a real \(\mu_0\)
with \(\partial_\mu|\widehat W_j(a+i\mu_0)|\ne0\).  Set
\(\nu=L-\mu_0\) on a positive saddle cell \(L\asymp\lambda\).  Then
\[
 |D_\beta(L,L-\mu_0)|\asymp\lambda,\qquad
 \left|\partial_L S_j(L,L-\mu_0)\right|
 \asymp_b\lambda^{-4}.
 \tag{39.21}
\]
The denominator derivative and the derivative of the phase-removed gamma
amplitude are \(O_b(\lambda^{-5})\) there, so (39.21) is the sharp
translated-profile capacity.  The negative saddle is identical with
\(L,\nu<0\).

Since \(q\le N_X\le16\sqrt X\), \(x\le N_X\le16\sqrt X\), and
\(D_j\ge X^{1/4}\), the actual range has
\(\lambda\le64\pi X\).  Thus (39.21) is bounded
by \(\lambda^{-3}w_{X,b}^{\rm ridge}(\nu)\) with (39.3), and that weight
costs exactly one logarithm.  Rapid vertical decay of
\(\widehat W_j\) handles \(|\nu-L|\gg1\), including the tangent-rho
location \(\nu\asymp-L\).  Thus smooth profiles are not an algebraic
obstruction, but they show why the most natural sufficient hypothesis is
the mixed norm
\[
\boxed{\begin{aligned}
 \mathfrak M_\lambda(K):={}&
 \sup_{L\in I_\lambda}\int_{\mathbb R}|K(L,\nu)|\,d\nu
 +\int_{I_\lambda}\int_{\mathbb R}
       |\partial_LK(L,\nu)|\,d\nu\,dL\\
 &+\sum_{\substack{\gamma\ \mathrm{moving}\\ \mathrm{face}}}
       \int_{I_\lambda}|K(L,\gamma(L))|\,dL
 +\mathfrak R_\lambda^{\rm Morse}(K),
 \qquad
 \mathfrak M_\lambda(K)\ll X^\varepsilon\lambda^{-2}.
 \tag{39.22}
\end{aligned}}
\]
Here \(\mathfrak R_\lambda^{\rm Morse}(K)\) is the
\(L^1(d\nu)\) norm of the exact normalized remainder (39.14a), together
with its induced moving-endpoint trace norms.  Thus (39.22) does not
replace the varying amplitude by its saddle value.
Here \(I_\lambda\) has length \(O(\lambda)\).  This is exactly what the
Leibniz BV argument uses.  A factorized pointwise \(w(\nu)\) is a
convenient sufficient condition for (39.22), not a necessary one.
For (39.19), the derivative part of (39.22) is in fact
\(O_b(\lambda^{-3})\).

### 3.4 Complete conditional power and summation ledger

Assume (39.22) for the hard-top phase-removed cell, including entry/exit
and regular moving traces.  Insert the value scale from (39.1) into
(39.15).  The exact floor is kept until the inequality
\[
 H_j+1\le D_jX^{-1/4}+1\le2D_jX^{-1/4}
 \tag{39.23}
\]
is used.  Apart from fixed powers of \(2\) and \(\pi\), the resulting
coefficient before the external \(X^{1/4}\) is
\[
 \boxed{
 |\chi_4(q)|h^{-r}q^{-2}D_j^{2-r}
 X^{r/2-1/2+b/4}
 x^{-r/2-b/2-5/4}.}
 \tag{39.24}
\]
All exponents follow algebraically from (39.15); in particular no
\(D_j/q\), \(\sqrt X\), or \(H_j+1\) factor has been discarded.

The two stationary phases are
\[
 \exp\!\left(i\pi\sqrt{Xx}\left(2\mp\frac q{D_j}\right)\right).
 \tag{39.25}
\]
With \(y=\sqrt x\), one integration by parts gives
\[
 \left|\int_1^{N_X}x^{-r/2-b/2-5/4}
 e^{i\pi\sqrt{Xx}(2\mp q/D_j)}\,dx\right|
 \ll
 \min\!\left(1,
 \frac1{\sqrt X|2\mp q/D_j|}\right).
 \tag{39.26}
\]
The endpoint and derivative amplitudes are integrable because \(r>1\).

For the plus frequency in (39.26), \(|2+q/D_j|\ge2\).  For the
minus frequency, split \(q\) into \(q\asymp D_j\) and its complement.
The harmonic sum around \(q=2D_j\) gives
\[
 \sum_{q\ge1}q^{-2}
 \min\!\left(1,
 \frac1{\sqrt X|2-q/D_j|}\right)
 \ll X^{-1/2}\log(2X).
\tag{39.27}
\]
Every \(D_j\) is an integer, so the formal zero-denominator value
\(q=2D_j\) is even and its coefficient is exactly
\(\chi_4(2D_j)=0\).  The nearest nonzero odd \(q\) has
\(|q-2D_j|\ge1\), and therefore contributes at most
\[
 q^{-2}\frac{D_j}{\sqrt X|q-2D_j|}
 \ll\frac1{D_j\sqrt X}\le X^{-3/4}.
 \tag{39.27a}
\]
The product cutoff \(hq\le N_X\), the remaining zeros of \(\chi_4\),
and every star only reduce the absolute estimate.

Since \(r>1\), \(\sum_hh^{-r}\ll1\).  Equations (39.24)--(39.27) give
for one scale
\[
 \ll D_j^{2-r}X^{r/2-1+b/4}\log(2X).
 \tag{39.28}
\]
As \(2-r>0\) and \(D_j\le\sqrt X\), the maximum of (39.28) is
\(X^{b/4}\log(2X)=O(\log X)\).  The actual number of dyadic scales is
\(O(\log X)\).  Consequently the complete leading separated saddle sum
is \(O(\log^C X)\) before the external normalization and
\[
 O\!\left(X^{1/4}\log^C X\right)
 \tag{39.29}
\]
after applying \(-4X^{1/4}\operatorname {Re}\{e(1/8)\cdot\}/\pi\).
The explicit height-face logarithm has the already accepted
\(q^{-4}\log(2+\lambda)\) coefficient and is smaller than (39.24).
Incomplete Fresnel entry/exit factors and exact half-stars are bounded by
one, but their remainders still require the missing mixed symbol estimate;
(39.29) is therefore conditional, not a promotion of the beta branch.

### 3.5 Exhaustive ownership and transition scope

The one-count partition is as follows.

- Both signed large-\(|\alpha|\) cells use the phase in (39.2) and the
  exact leading-plus-remainder Morse decomposition
  (39.14a)--(39.14b).
- Saddle entry and exit remain in the same phase-removed cell; the exact
  endpoint saddle has half the full Fresnel coefficient.
- The bounded-\(\alpha\) cell is the already separated central box and
  carries no artificial \(\lambda\)-claim.
- The explicit moving top-face log is removed once and handled by the
  accepted \(q^{-4}\) lemma.  Its regular trace remains in (39.22).
- On the terminal line \(\Re\rho=-1-b/2\).  The crossed artificial
  residue, its collisions, and its corner have already been assigned.
  Common rho ownership makes every omega-derivative coefficient a
  derivative of \(G-E_1-R_1=0\); no isolated artificial term is added to
  \(K^\circ\).
- The full \(v=0\) vector and its connector-axis images are subtracted as
  a contour vector.  One does not replace \(f_b\) pointwise by
  \(f_b-(b+i\nu)^{-1}\).
- Smooth spatial profiles obey the ridge ledger (39.19)--(39.22).
- Round 38 gives existence of the remaining signed tails.  Its
  \(C_{X,b}\) is not substituted for the quantitative norm (39.22).

## 4. First doubtful or unproved step

The first correction is definitional.  The aggregate limiting vector has
many \(\lambda_{j,q,x}\), and the raw cell includes the stationary phase.
The bare derivative bound must therefore be attached to the cellwise,
phase-removed, pre-numerator object in (39.14a)--(39.14b).  Attaching it to the
aggregate is ill typed; attaching it to the oscillatory cell is false on
entry/exit collars by (39.2).

After this correction, the first genuinely unproved actual estimate is
\[
 \mathfrak M_\lambda\!\left(
   \mathcal R_A[H_{\rm complete}^{\rm phase\,removed}]
 \right)
 \ll X^\varepsilon\lambda^{-2},
 \tag{39.30}
\]
uniformly through both signs, saddle entry/exit, common rho ownership,
and all translated regular faces.  Infinitesimally its smallest new
coefficient is \(\mathfrak E_H\) in (39.17), equivalently the complete
\(\partial_\nu(\partial_L+\partial_\nu)H\) coefficient after translation
and face recombination.  The separated profile proves (39.30), and the
smooth-profile ridge costs only (39.3), but no accepted artifact proves
(39.30) for the complete gamma/radial/beta-connector numerator with its
exact incomplete-Fresnel remainders.

The sharp presently available raw capacity is (39.18b) times
\(\lambda^{-2}\) for value.  If the phase is not removed, the
fixed-\(\nu\) derivative has the same \(\lambda\)-power on entry/exit,
rather than one extra inverse power.  Round 38 bounds the signed tail only
by an unrestricted \(C_{X,b}\), so it cannot repair this loss.  Once
(39.30) is proved, the remaining leading coefficient sums are already
closed by (39.24)--(39.29); the next work should target (39.17), not
repeat the scale summation.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Limiting symbol and one-count ownership | Pass after a type correction. Boundary modules, radial sides, the axial vector, artificial share, collisions, and corner are removed once. The quantitative symbol must be cellwise rather than the already summed aggregate. |
| Fixed \(\nu\), not fixed \(\mu\) | Pass. Equations (39.7), (39.16), and (39.17) use the physical derivative and retain the translated diagonal derivative \(\partial_L+\partial_\nu\). |
| Contour measure and normalization | Pass with a correction. The top distribution consumes one of three \((2\pi)^{-1}\) factors; \((2\pi)^{-2}\) remains. The PV density is \(-i/(2\pi)^3\) before the radial \(-\pi i\sqrt X\). |
| Three normalization levels | Pass. Equations (39.13), (39.1), and (39.14a)--(39.15) distinguish the pre-numerator symbol, stationary numerator, exact Morse remainder, and physical aggregate. |
| Exact \(X,D_j,h,q,x,\lambda,b\) ledger | Pass. Equations (39.18a)--(39.18b) give the raw terminal capacity; (39.24) is the post-stationary coefficient. The algebra relating them is explicit. |
| Both saddles and entry/exit | Phase and power pass; complete remainder open. The derivative (39.2) is the same on both signs after \(|\alpha|\), Hessians have opposite signs, and the half-Fresnel endpoint is retained. |
| Actual profiles and weighted height | Pass for separated and smooth profiles. The hard separated kernel has the accepted weight; the smooth translated ridge forces the sharp harmonic weight (39.3), still of polylogarithmic norm. |
| Rho, axial, connectors, and collisions | Ownership pass; quantitative common numerator open. The terminal rho real part is fixed negative, omega derivatives cancel under common ownership, and extracted axial/collision/corner shares are not reinserted. Beta connector factors remain in \(H\). |
| Moving faces and tails | Explicit face log passes with local \(q^{-4}\). Regular translated traces belong to (39.22). Round-38 tail existence passes, but its \(X\)-uniform quantitative version remains open. |
| Floors, stars, character, and actual sums | Conditional pass. The exact floor is retained through (39.23), stars have modulus at most one, and \(\chi_4(2D_j)=0\) removes the sole formal resonance; no cancellation among nonzero character values is used. Equations (39.27)--(39.29) execute every leading coefficient and scale sum. |
| External normalization and downstream scope | Pass. The internal sum is polylogarithmic only conditionally on (39.30); the external factor then gives (39.29). No finite-section BV, full beta transition, M9-M1, M9, or Gauss-circle conclusion is promoted. |

## 6. Dependencies and exact artifacts used

The derivation used the following assigned artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md`;
5. `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md`;
6. `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md`;
7. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/actual_cauchy_tail_attack.md`;
8. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/cauchy_tail_hostile_audit.md`;
9. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`;
10. the Round-39 task brief.

Imported facts are the accepted endpoint/side/axial ownership, exact
terminal density, actual profile decay and pole convention, separated
kernel, two signed saddles, stationary numerator, face-log estimate, and
Round-38 Cauchy existence.  Equations (39.8), (39.16)--(39.18), the
translated-ridge audit, and the conditional complete sum
(39.24)--(39.29) are derived here.  No numerical experiment or external
source was used.

## 7. Recommended state effect

**Revise, do not promote, the frozen terminal-symbol node.**  Replace the
single aggregate notation by the cellwise normalization and exact
leading-plus-remainder decomposition (39.14a)--(39.14b), state
that the full exact stationary phase is removed before the fixed-\(\nu\)
derivative is taken, and distinguish the three levels in Section 1.

**Promote as narrow bookkeeping lemmas, after conductor verification:**

- the contour-measure correction (39.8)--(39.9);
- the raw-to-stationary reconciliation (39.18a)--(39.18b);
- the exact fixed-height derivative and survivor (39.16)--(39.17);
- the smooth-profile harmonic ridge weight (39.3), or preferably the
  mixed norm (39.22); and
- the conditional complete leading sum (39.24)--(39.29), including both
  saddle signs and the exact resonance.

Retain the quantitative terminal-symbol obligation open precisely at
(39.30).  The next proof should estimate the phase-removed complete
translation divided difference (39.17) and its moving traces through
entry/exit and common rho ownership.  If (39.30) is established, the
leading \(h,q,j,x\) and external-normalization ledger no longer presents
an exponent obstruction.  Do not infer (39.30) from Round-38 existence,
do not differentiate the stationary phase as part of the symbol, and do
not apply the downstream finite-section BV lemma before this remaining
mixed norm is proved.
