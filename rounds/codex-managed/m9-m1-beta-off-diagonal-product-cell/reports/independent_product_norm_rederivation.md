# Round 41 report: independent product-norm rederivation

Task: `independent_product_norm_rederivation`  
Role: statement-only independent validator (replacement gate)  
Allocation: 100% analytical/algebraic; no computation and no external source

## 1. Result

The proposed terminal product lemma is **proved in its routed, hybrid
scope**.  More precisely, on either signed cell

\[
 c_0\lambda\le |L|\le C_0\lambda,\qquad
 |\beta|\le2B_0,\qquad \lambda\ge1,                 \tag{41.1}
\]

after the signed diagonal Cauchy section has been removed, the raw
numerator has the exact form

\[
 \mathscr H(L,\nu;\beta)=\mathcal E_{j,h,q,x,a,b,\beta}
 e^{i\Phi_\sigma(L)}G_\sigma(L,\beta)\,p(\nu),       \tag{41.2}
\]

where every factor in \(\mathcal E\) is external to the terminal symbol,

\[
 p(\nu)=e^{i\gamma\nu}\widehat\phi(b+i\nu),qquad
 \gamma=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x},       \tag{41.3}
\]

and on the branch \(\operatorname {sgn}(L+\beta)=\sigma\) the canonical
signed-coordinate phase is

\[
 \Phi_\sigma(L)=(L+\beta)\log\frac{|L+\beta|}{\lambda}
 -(L+\beta)+\sigma\lambda,
 \quad \Phi_\sigma'(L)=\log\frac{|L+\beta|}{\lambda},
 \quad \Phi_\sigma''(L)=\frac1{L+\beta}.           \tag{41.4}
\]

The normalization of \(G_\sigma\) is chosen so that, for \(r=0,1,2\),

\[
 \boxed{
  |(\lambda\partial_L)^rG_\sigma(L,\beta)|
  \ll_{r,B_0,a,b,c_0,C_0}1 }                       \tag{41.5}
\]

on both signs.  The harmless powers of \(2,\pi\), the exact bounded-beta
gamma quotient, and the constant unit-modulus branch factor are included
in \(G_\sigma\); the large-alpha power
\(\kappa=3/4+(a+b)/2\) and its value at \(|L|=\lambda\) are divided out.

For

\[
 D(L,\nu)=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right),
                                                               \tag{41.6}
\]

\[
 K_\Delta=G(L)\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)},\qquad
 K_W=G(L)\frac{p(\nu)W(L-\nu)}{D(L,\nu)},           \tag{41.7}
\]

the direct value, the derivative at fixed physical \(\nu\), all moving
endpoint traces, and the exact normalized Morse remainder are

\[
 \boxed{\ \ll_\varepsilon X^\varepsilon\lambda^{-2}\ }        \tag{41.8}
\]

uniformly through saddle interior, entry, and exit on both signs.  The
long-translation part of the derivative is bounded only after being
recombined as an endpoint second divided difference.  The fixed dyadic
profiles supply the required spatial-Mellin seminorm.

Finally, the accepted post-routing ownership is sufficient.  There is no
additional connector or artificial product cell inside (41.7).  This
conclusion is conditional on using the same finite operator for
\(G=E_1+R_1\) and on performing the stated global routing before freezing
the terminal cell; a hybrid ownership would create a new defect and is
not covered.

## 2. Exact statement and hypotheses

Use the lawful lines

\[
 c'=\frac54,qquad b=\frac1{\log(2X)},\qquad
 0<a\le \min\{b,\tfrac14-b\}.                     \tag{41.9}
\]

Freeze \((j,h,q,x,\beta,\sigma)\), put

\[
 u=a+i(L-\nu),\quad v=b+i\nu,\quad
 s=\frac54+i\left(\frac L2+\beta\right),\quad
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j},              \tag{41.10}
\]

and restrict to a fixed-ratio signed saddle component (41.1).  All
cutoffs defining the component have a fixed scale-normalized \(C^2\)
norm.  For the hard singular top take \(\mathscr W_0=1\) and remove its
already proved signed diagonal Cauchy section before any absolute norm or
Morse localization.  For a smooth top/interior share, \(W(y)\) denotes
the ordinary-\(\mu\) Mellin profile in translation height \(y=L-\nu\).

The exact seminorm used below is

\[
\begin{split}
 \mathfrak P_3(p)&=
 \sum_{r=0}^{3}\left\{\|p^{(r)}\|_{L^1(\mathbb R)}+
 \sup_{t\in\mathbb R}(1+|t|)^3|p^{(r)}(t)|\right\},\\
 \mathfrak S_6(W)&=
 \sum_{r=0}^{3}\int_{\mathbb R}(1+|t|)^{6-r}|W^{(r)}(t)|\,dt,\\
 \mathfrak S_{\rm sp}&=\mathfrak P_3(p)+
 \sup_j\mathfrak S_6(W_j)+\mathfrak S_6(W_{0,r}).   \tag{41.11}
\end{split}
\]

Here \(W_{0,r}\) is the regular Mellin remainder of the hard top.  We
require

\[
 \mathfrak S_{\rm sp}\ll_\varepsilon X^\varepsilon.             \tag{41.12}
\]

The spatial power six is deliberately more than needed.  Vertical-line
integration by parts gives arbitrary polynomial decay for every derivative
of the fixed smooth interior transforms and of \(W_{0,r}\).  In contrast,
the actual Vaaler height transform has a genuine cubic leading tail; no
stronger height moment is asserted.  Its accepted bounds give, for
\(0\le r\le3\), both \(L^1\) control and
\(|\widehat\phi^{(r)}(b+it)|\ll b^{-A_r}(1+|t|)^{-3-r}\).
Differentiating the modulation in (41.3) costs only powers of
\(|\gamma|\ll\log(2X)\), so \(\mathfrak P_3(p)\) has the same
polylogarithmic capacity.  Since
\(b^{-1}=\log(2X)\), every finite loss is \(O_\varepsilon(X^\varepsilon)\),
which proves (41.12).

The symbol norm meant by (41.8), on any affine finite-height section
\(I(L)=[-V,V]\cap[L-U,L+U]=[P(L),Q(L)]\), is

\[
\begin{split}
 \|K\|_{\rm mix}:={}&
 \sup_L\int_{I(L)}|K(L,\nu)|\,d\nu
 +\int_{J}\int_{I(L)}|\partial_LK(L,\nu)|_{\nu}\,d\nu\,dL\\
 &+\sum_{R=P,Q}\int_J |K(L,R(L))|\,|R'(L)|\,dL
 +\mathcal R_{\rm Morse}[K],                       \tag{41.13}
\end{split}
\]

where \(J\) is a fixed-ratio signed \(L\)-cell (including an entry or
exit truncation).  In the exact Morse coordinate of the signed phase,
write the integrated section as \(A(L)=\mathcal A(L/\lambda)\).  Then

\[
 \mathcal R_{\rm Morse}[K]
 :=\lambda^{-1/2}\left|
 \sqrt\lambda\int_{\tau_P}^{\tau_Q}
 \tau\frac{g(\tau)-g(0)}{\tau}e^{i\tau^2/2}\,d\tau
 \right|,                                         \tag{41.14}
\]

with \(g=\mathcal A/\zeta'\) pulled back by the exact signed Morse map.
Thus (41.14), not a scalar full-Fresnel surrogate, is the normalized exact
remainder.  The standard integration by parts in \(\tau\) bounds it by
the scale-normalized \(C^2\)/BV quantity already present in the first
three terms of (41.13), uniformly as either endpoint crosses zero.

The character \(\chi_4(q)\), stationary numerator
\((D_j/q)\lambda\), real coefficient monomial, the radial \(x\)-integral,
two remaining contour measures, all constants, floors, stars, and the
external \(X^{1/4}\) are not included in \(G,p,K_\Delta,K_W\).

## 3. Proof or derivation

### Exact phase removal

Substitution of (41.10) into the raw exponential gives

\[
\begin{split}
 &iL\left(\log\frac{D_j}{2\sqrt X}-\log q-\frac12\log x\right)
 +i\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}\\
 &\hspace{30mm}-i\beta\log(hqx).                  \tag{41.15}
\end{split}
\]

This proves (41.3), including the previously easy-to-miss
\(-\tfrac12\nu\log x\).  The beta term and the \(L\)-linear term are
absorbed respectively into the external constant and the full stationary
phase.

Let \(z=u+v=a+b+iL\).  The exact gamma quotient is

\[
 K_z(1-s)=2^{2s+z-1}\pi^{1-2s}
 \frac{\Gamma((s-z/2)/2)\Gamma((1+s+z/2)/2)}
 {\Gamma((1-s+z/2)/2)\Gamma((2-s-z/2)/2)}.         \tag{41.16}
\]

Its first ratio depends only on the bounded height \(\beta\); the second
is the large signed ratio.  Uniform differentiated Stirling on
\(|L+\beta|\asymp\lambda\) gives, with
\(\kappa=3/4+(a+b)/2\),

\[
 K_z(1-s)=C_\beta |L+\beta|^\kappa
 e^{i\vartheta^{\rm main}_\sigma(L)}
 \left(1+\frac{c_{1,\sigma}(\beta)}{L+\beta}
 +O_{B_0}(|L+\beta|^{-2})\right),                 \tag{41.17}
\]

and the expansion may be differentiated twice with the expected extra
factor \(|L+\beta|^{-1}\) each time.  Here
\(\vartheta^{\rm main}_\sigma\) is the canonical Stirling main phase,
not the full exact gamma argument: after adding the linear term in
(41.15), its derivative is exactly (41.4).  Every lower Stirling phase
correction remains in the symbol.  Define

\[
 G_\sigma(L,\beta)=\lambda^{-\kappa}
 e^{-i\Phi_\sigma(L)}e^{iL c_{j,q,x}}K_z(1-s),      \tag{41.18}
\]

where \(c_{j,q,x}\) is exactly the coefficient of \(iL\) in (41.15),
and absorb the fixed nonzero bounded-beta normalizing value into
\(\mathcal E\).  Equations (41.17)--(41.18) give (41.5), including both
signs and two differentiated symbol bounds.  In particular, the
stationary points remain the canonical \(L+\beta=\pm\lambda\); absorbing
the full exact gamma argument into \(\Phi_\sigma\) would spuriously shift
them and is not done.  This proves (41.2).

### Denominator and product calculus

Put \(y=L-\nu\).  Since

\[
 |D|\asymp 1+|L+\nu|,\qquad
 |\partial_LD|=|\partial_\nu D|=\frac12,           \tag{41.19}
\]

the four physical-height regions are:

\[
 |\nu|\le |L|/2,\qquad |y|\le |L|/2,\qquad
 |L+\nu|\le |L|/2,\qquad
 \max(|\nu|,|y|,|L+\nu|)\gg|L|.                  \tag{41.20}
\]

They respectively give an inverse \(D\), cubic profile decay at \(\nu\),
cubic profile decay at \(\nu\simeq-L\), or simultaneous tail decay.  No
weighted height moment beyond cubic decay and the \(L^1\) norms in
\(\mathfrak P_3(p)\) is used.  Taylor's
formula at \(y=0\) removes the apparent singularity:

\[
 \frac{p(\nu)-p(L)}{L-\nu}
 =-\int_0^1p'(L-ty)\,dt.                           \tag{41.21}
\]

Indeed, in the physical-center region \(|D|^{-1}\ll\lambda^{-1}\) and
the divided difference has \(L^1(d\nu)\) size
\(O(\mathfrak P_3(p)\lambda^{-1})\); in the diagonal region
\(|p(L)|+|p'(L)|\ll\mathfrak P_3(p)\lambda^{-3}\); in the ridge
\(\nu=-L+O(1)\) the same cubic bound applies to \(p(\nu)\), while
\(|L-\nu|\asymp\lambda\); and in the far region cubic pointwise decay is
integrable.  Thus (41.5), (41.11), and (41.19)--(41.21) yield

\[
 \sup_L\int|K_\Delta|d\nu
 +\sup_L\int|K_W|d\nu
 \ll \mathfrak S_{\rm sp}\lambda^{-2}.            \tag{41.22}
\]

For \(K_W\), the second inverse power comes either from \(D^{-1}\) and
the translation localization/moment of \(W\), or from physical-profile
decay in the ridge \(L+\nu=O(1)\).  The same partition with one derivative
of (41.19), (41.21), \(G\), or a profile proves the fixed-height and trace
bounds.  Affine switches cause no extra term: upper faces enter with the
positive Leibniz sign and lower faces with the negative sign; when
\(P=Q\), both traces cancel.

The only non-termwise step is the long translation in
\(\partial_LK_\Delta|_\nu\).  Set

\[
 F(L,y)=G(L)p(L-y).
\]

Its dangerous coefficient is exactly

\[
 \mathfrak E_F(L,y)=
 \frac{(F_L+F_y)(L,y)-F_L(L,0)}y-
 \frac{F(L,y)-F(L,0)}{y^2},                        \tag{41.23}
\]

because \(dy/dL=1\) at fixed physical \(\nu\), while the moving diagonal
derivative is \((\partial_L+\partial_\nu)H(L,L)=F_L(L,0)\).
Algebraically this is the recombined endpoint second divided difference

\[
 \mathfrak E_F(L,y)=
 \frac{y\{(F_L+F_y)(L,y)-F_L(L,0)\}
       -\{F(L,y)-F(L,0)\}}{y^2}.                    \tag{41.24}
\]

Equivalently it equals the two parameter integrals of \(F_{Ly}\) and
\(F_{yy}\), but those integrals are not estimated separately.  Inserting
\(F=Gp(L-y)\) directly in (41.24) preserves the cancellation of the two
endpoint profile values.  For \(|y|\le1\), Taylor gives a bounded second
derivative; for \(1<|y|\le |L|/2\), the endpoint formula gives
\(O(\mathfrak S_{\rm sp}|y|^{-2})\); and in the two long regions of
(41.20), the decaying endpoint is used before the remaining absolute
value.  Division by \(D\) and integration gives

\[
 \int_J\int |\partial_LK_\Delta|_\nu\,d\nu\,dL
 +\text{all traces}\ll
 \mathfrak S_{\rm sp}\lambda^{-2}.                \tag{41.25}
\]

This is exactly where separate absolute estimates of \(F_{Ly}\) and
\(F_{yy}\) would lose the required long-translation powers.

Finally, pull the already integrated section through the exact signed
Morse coordinate.  Differentiated (41.22)--(41.25), together with
(41.5), gives
\(\|B\|_\infty\ll\mathfrak S_{\rm sp}\lambda^{-5/2}\) and
\(\|B'\|_\infty\ll\mathfrak S_{\rm sp}\lambda^{-3}\) in the notation
of the exact remainder.  Integration by parts in (41.14) therefore gives

\[
 \mathcal R_{\rm Morse}[K_\Delta]
 +\mathcal R_{\rm Morse}[K_W]
 \ll\mathfrak S_{\rm sp}\lambda^{-2},             \tag{41.26}
\]

with no change when an endpoint passes through the saddle.  Equations
(41.12), (41.22), (41.25), and (41.26) prove (41.8).

### Ownership

The accepted global three-mask recombination removes endpoint, side, and
arithmetic modules before the cell is frozen.  The complete two-axis
ledger assigns axes, connector axes, collision, corner, and artificial
residues once.  Moreover, under the same finite domains, masks, stars,
endpoint convention, and regularization,

\[
 \mathcal H[G]-\mathcal H[E_1]-\mathcal H[R_1]
 =\mathcal H[G-E_1-R_1]=0                         \tag{41.27}
\]

meromorphically and after fixed-physical-height differentiation.  Hence
all cutoff derivatives and all artificial Laurent coefficients cancel
before estimation.  What remains in the post-routing terminal cell is
exactly the singular off-diagonal (plus its already removed diagonal
section) and the smooth ordinary-\(\mu\) product (41.7).  Thus no further
connector/artificial cell remains.

## 4. First doubtful or unproved step

Within the stated routed cell, no mathematical gap remains.  The first
step not proved by this report is the assembly outside its scope:
bounded-\(\alpha\), the complete double-bounded share, and the global beta
transition/sums.

There is one sharp ownership caveat.  Equation (41.27) fails as an
interface statement if one uses an unmasked endpoint theorem on only one
of \(G,E_1,R_1\), changes a finite face, or omits a connector axis.  The
resulting constant artificial coefficient and its physical \(L\)
derivative would be an additional cell.  The accepted post-routing graph
explicitly rules out that hybrid, so it is not present here.

## 5. Required controls and outcomes

### Exact phase and external-factor ownership

**Pass.**  Equation (41.15) gives the true modulation (41.3).  Character,
stationary numerator, monomial, radial integral, contours, floors, stars,
and external \(X^{1/4}\) never enter the symbol.

### Two signed gamma symbols

**Pass.**  Exact factorization (41.16), followed by twice-differentiated
uniform Stirling, gives (41.4)--(41.5) on both fixed-ratio signs.

### Four-region product norm

**Pass.**  The physical center, diagonal, radial ridge, and far-height
partition (41.20), with (41.21), proves value, derivative, and trace
bounds at \(X^\varepsilon\lambda^{-2}\).

### Long translation

**Pass.**  It is evaluated as (41.24) before absolute values.  Separate
absolute bounds on the two mixed-derivative integrals are not used.

### Entry, exit, and exact Morse remainder

**Pass.**  Equation (41.26) uses the exact Morse remainder (41.14), not a
full scalar Fresnel replacement, and is uniform when either face crosses
the saddle on both signs.

### Profile seminorm

**Pass.**  The spatial part of (41.11) follows by vertical-line integration
by parts for every fixed compact dyadic profile and the top regular
remainder.  The height part deliberately asks only for \(L^1\) derivatives
and the genuine cubic tail.  Modulation costs powers of \(b^{-1}\) and
\(\log X\), hence (41.12); no false higher height moment is used.

### Diagonal and ownership scope

**Pass.**  The singular diagonal section is not reopened or estimated
absolutely.  Equation (41.27) eliminates common artificial/cutoff defects,
and the accepted sixteen-stratum ledger places all connector and axial
modules outside this product lemma exactly once.

## 6. Dependencies and exact artifacts used

Only the permitted files were read:

1. `protocol.md`;
2. `state/proof_obligations.yml` (accepted statements only; no evidence
   path or graph status was used as proof);
3. `state/active_campaign.yml`;
4. this task brief;
5. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/synthesis.md`;
6. `rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/reports/blind_uniform_saddle_statement.md`;
7. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/blind_beta_slab_height_asymptotic.md`.

Exact isolation compliance: no active Round-41 report, review, candidate,
control, or synthesis was read; neither Round-40 discovery nor hostile
report was read; the superseded contaminated report was not read.  No
proof draft, validation matrix, computation, or web source was used.

## 7. Recommended state effect

- **Promote**, after conductor seam review, the exact phase-removed
  factorization (41.2)--(41.5), including the true modulation (41.3).
- **Promote** the routed off-diagonal/smooth mixed norm (41.8), with the
  exact seminorm (41.11), endpoint second divided difference (41.24), and
  exact normalized Morse remainder (41.14).
- **Close** the post-routing connector/artificial question: no additional
  terminal product cell remains under common ownership (41.27).
- **Retain open** bounded-alpha, the double-bounded share, complete beta
  transition assembly, all global sums not already conditional, M9-M1,
  M9, and the Gauss-circle target.
