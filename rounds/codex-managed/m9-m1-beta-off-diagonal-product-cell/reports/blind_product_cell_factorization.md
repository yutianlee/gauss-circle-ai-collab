# Round 41 report: frozen product cells close conditionally, but the connector/artificial stratum is not specified

Task: `blind_product_cell_factorization`  
Role actually achieved: `independent_rederivation_contaminated_not_blind`  
Allocation: 100% analytical/algebraic; no computation and no external source

## 1. Result

For a fixed terminal coefficient cell
\((j,h,q,x,\beta,\sigma)\), the supplied formula has an exact product
factorization.  Put

\[
 \zeta_0=a+b,\qquad \kappa=\frac34+\frac{\zeta_0}{2},\qquad
 \alpha=L+\beta,\qquad y=L-\nu,
\]
\[
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
 \tau=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x},
\]
\[
 A(L)=-1-\frac b2-i(L+\beta),\qquad
 D(L,\nu)=A(L)+\frac i2(L-\nu)
 =-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
 \tag{41.1}
\]

On the sign cell \(\sigma\alpha>0\), define the exact stationary phase
and the exact normalized, phase-removed gamma symbol by

\[
 \Theta_\lambda(L)=\alpha\left(\log\frac{|\alpha|}{\lambda}-1\right),
 \tag{41.2}
\]
\[
 \boxed{
 G_{\sigma}(L;\beta,\lambda)
 =\lambda^{-\kappa}e^{-i\Theta_\lambda(L)}
 K_{\zeta_0+iL}\!\left(1-\frac54-i\left(\frac L2+\beta\right)\right)
 e^{\,iL\log(\pi/(2\lambda))}.}
 \tag{41.3}
\]

Also set

\[
 p(\nu)=\widehat\phi(b+i\nu)e^{i\tau\nu}.
 \tag{41.4}
\]

All remaining scalar factors are outside the normalized product cell:

\[
\begin{aligned}
 \mathfrak N_{j,h,q,x,\beta}={}&
 (-\pi i\sqrt X)x^{-3/2-b/2}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 h^{-5/4+\zeta_0/2}q^{-5/4-\zeta_0/2} \\
 &\times e(\sqrt{Xx})e^{-i\beta\log(hqx)}\lambda^\kappa .
 \tag{41.5}
\end{aligned}
\]

The character \(\chi_4(q)\), the contour measures, the outer
\(-4X^{1/4}\operatorname{Re}(e(1/8)\,\cdot)/\pi\), the
\(j,h,q,x\) sums/integral, and the normalized Morse numerator
\(\lambda^{1/2}\) are not in (41.3)--(41.4).  Thus none is silently
absorbed into the claimed bare symbol bound.

After the signed diagonal Cauchy section is removed, the singular
hard-top cell is exactly

\[
 \boxed{
 S_\sigma(L,\nu)=
 \eta_\sigma(L)\,G_\sigma(L)
 \frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)}.}
 \tag{41.6}
\]

Here \(\eta_\sigma\) denotes whichever one-count fixed-ratio/entry-exit
cutoff is used; it must occur once, not once in both the diagonal and
off-diagonal modules.  An ordinary-\(\mu\) smooth top or interior cell is

\[
 \boxed{
 T_{\sigma,j}(L,\nu)=
 \eta_\sigma(L)G_\sigma(L)
 \frac{p(\nu)\mathscr W_j(L-\nu)}{D(L,\nu)}.}
 \tag{41.7}
\]

After restoring the explicitly removed factor \(e^{i\Theta_\lambda(L)}\),
equations (41.5)--(41.7) multiply back to the supplied raw terminal
numerator and radial denominator exactly.  More precisely, on the support
of a one-count cutoff,
\(\eta_\sigma\) times the raw off-diagonal density equals
\(\mathfrak N e^{i\Theta_\lambda}S_\sigma\), and
\(\eta_\sigma\) times the raw smooth density equals
\(\mathfrak N e^{i\Theta_\lambda}T_{\sigma,j}\).
This is an exact phase removal, not a scalar-Fresnel approximation.

There is a useful conditional theorem.  If the cutoffs have the standard
\(\lambda^{-r}\) derivative bounds, the smooth Mellin profiles have
uniform declared Schwartz seminorms, and
\(1+|\tau|+b^{-1}\ll\log^C(2X)\), then, uniformly on both signed
fixed-ratio cells,

\[
 \sup_L\int_{\mathbb R}|S_\sigma(L,\nu)|\,d\nu
 \ll X^\varepsilon\lambda^{-2},\qquad
 \sup_L\int_{\mathbb R}|\partial_LS_\sigma(L,\nu)|_\nu\,d\nu
 \ll X^\varepsilon\lambda^{-3},
 \tag{41.8}
\]

and (41.7) is smaller, of order \(X^\varepsilon\lambda^{-4}\) in
both the value and the relevant integrated variation ledger.  Moving
physical traces cost at most \(X^\varepsilon\lambda^{-2}\).  Hence a
one-count sum of these specified product cells has sup plus total
variation \(O_\varepsilon(X^\varepsilon\lambda^{-2})\), and the exact
normalized Morse operator, including partial entry and exit, preserves
that bound for either saddle sign.

The complete Round-41 target nevertheless does **not** follow from the
permitted artifacts.  No supplied formula gives the beta-connector term,
its orientation/multiplicity, or the common artificial germ as one
normalized \(G\,p\,\mathscr W/D\) cell.  The only supplied artificial
formula is the different meromorphic coefficient

\[
 \zeta\!\left(\frac34+\frac u2+v\right)
 L\!\left(\frac34-\frac u2,\chi_4\right),
 \qquad \beta_\rho=-\frac\mu2-\nu,
 \tag{41.9}
\]

for which the available estimate is merely a fixed-\(X\) Cauchy-tail
bound.  It has neither the normalization (41.3) nor a declared local
\(\lambda\)-cell.  Consequently the supplied information records at best
\(C_{X,b}\lambda^0\), rather than
\(X^\varepsilon\lambda^{-2}\): the quantitative ledger has a two-power
\(\lambda\)-gap, as well as no control of the \(X\)-constant.  This is an
information gap, not a lower-bound assertion that the missing term
actually attains size \(\lambda^0\).  The report therefore proves
the product-cell lemma conditionally and returns a precise no-go for the
claimed *complete* one-count assembly.

## 2. Exact statement and hypotheses

Fix \(|\beta|\le 2B_0\), \(b=1/\log(2X)\), and the legal terminal
real parts.  Let \(\lambda\ge\lambda_0(B_0)\), and on a signed saddle
cell assume

\[
 c\lambda\le |L+\beta|\le C\lambda,
 \qquad \operatorname{sgn}(L+\beta)=\sigma\in\{+1,-1\}.
 \tag{41.10}
\]

The exact gamma quotient is the one in (41.3), equivalently the product
of the two ratios

\[
 X_\zeta=\pi^{1/2-s+z/2}
 \frac{\Gamma((s-z/2)/2)}{\Gamma((1-s+z/2)/2)},\qquad
 X_4=\left(\frac4\pi\right)^{s+z/2-1/2}
 \frac{\Gamma((1+s+z/2)/2)}{\Gamma((2-s-z/2)/2)},
 \tag{41.11}
\]

where \(z=\zeta_0+iL\) and
\(s=5/4+i(L/2+\beta)\).  Notice that \(X_\zeta\) is exactly
independent of \(L\), because both of its imaginary gamma coordinates
are \(\pm\beta\).  The only large gamma coordinate in \(X_4\) is
\(\alpha=L+\beta\).

For the quantitative product lemma assume, for \(r=0,1,2\),

\[
 |p^{(r)}(t)|\le P\langle t\rangle^{-3},
 \qquad P\ll_\varepsilon X^\varepsilon,
 \tag{41.12}
\]

and for the saddle cutoff

\[
 |\eta_\sigma^{(r)}(L)|\le C_r\lambda^{-r}.
 \tag{41.13}
\]

Formula (41.12) follows from the supplied profile estimate for
\(\widehat\phi\) with

\[
 P\ll b^{-A}(1+|\tau|)^2,
 \tag{41.14}
\]

provided the actual range gives \(|\tau|\ll\log^C(2X)\).  The latter
range statement is required explicitly; it is not a consequence of the
abstract symbol \(H_j+1\) alone.

For a smooth cell, a sufficient actual hypothesis is

\[
 Q_j:=\max_{r\le1}\sup_y
 \langle y\rangle^6|\mathscr W_j^{(r)}(y)|
 \ll_\varepsilon X^\varepsilon.
 \tag{41.15}
\]

Any scale factor removed in obtaining (41.15) has to be displayed in
\(\mathfrak N\).  Merely calling \(\mathscr W_j\) rapidly decreasing
does not give uniformity in \(j\) or \(X\).

For a physical finite section use

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U]=[p_-(L),p_+(L)].
 \tag{41.16}
\]

On each affine regime the endpoints have slope in \(\{0,1\}\); at a
switch the two formulas agree, and an empty section contributes zero.
The desired section amplitude is formed from (41.6)--(41.7) before Morse
localization.

## 3. Proof or derivation

### Exact product algebra and phase removal

The phase in the supplied numerator separates as

\[
\begin{aligned}
 &i(L-\nu)\log\frac{D_j}{2\sqrt X}
 +i\nu\log(H_j+1)-iL\log q-i\beta\log(hq)
 -\frac i2(L+\nu+2\beta)\log x\\
 &\quad=
 iL\log\frac{\pi}{2\lambda}+i\tau\nu
 -i\beta\log(hqx).
 \tag{41.17}
\end{aligned}
\]

Substitution of (41.3)--(41.5) and (41.17) into the raw numerator proves
the factorization.  For the hard-top singular share
\(\mathscr W_0=1\).  Splitting its regularizer into the already removed
diagonal term and the residual difference gives (41.6).  A regular top
or interior transform retains ordinary \(y=\mu\) integration and hence
gives (41.7), with no second \(1/y\) factor and no second Plemelj
subtraction.

The two-sided Stirling formula in the permitted context gives the leading
phase of \(X_4\) as

\[
 \alpha\left(\log\frac{2|\alpha|}{\pi}-1\right)
 +\sigma\frac\pi4.
 \tag{41.18}
\]

Adding the \(L\)-phase in (41.17) leaves (41.2), up to an
\(L\)-independent phase.  Differentiated Stirling on (41.10) therefore
gives

\[
 |G_\sigma(L)|\ll1,\qquad
 |G_\sigma'(L)|\ll\lambda^{-1},\qquad
 |G_\sigma''(L)|\ll\lambda^{-2}.
 \tag{41.19}
\]

The proof is identical for \(\sigma=+1\) and \(-1\): the modulus power
is \(|\alpha|^\kappa\), the subtracted phase derivative is
\(\log(|\alpha|/\lambda)\), and every remaining log derivative is
\(O(|\alpha|^{-1})\).  Multiplication by (41.13) preserves (41.19),
including saddle-entry and saddle-exit collars.

### The fixed-height endpoint divided difference

Define

\[
 r(L,\nu)=\frac{p(\nu)-p(L)}{L-\nu},
 \tag{41.20}
\]

continuously at \(L=\nu\).  At fixed physical \(\nu\), its derivative
must be kept in the endpoint form

\[
 \boxed{
 \left.\partial_Lr(L,\nu)\right|_\nu
 =\frac{p(L)-p(\nu)-(L-\nu)p'(L)}{(L-\nu)^2}.}
 \tag{41.21}
\]

Consequently

\[
\boxed{
\begin{aligned}
 \left.\partial_LS_\sigma\right|_\nu={}&
 (\eta_\sigma G_\sigma)'\frac{r}{D}
 +\eta_\sigma G_\sigma
 \frac{p(L)-p(\nu)-(L-\nu)p'(L)}{(L-\nu)^2D}\\
 &+\frac i2\eta_\sigma G_\sigma\frac{r}{D^2}.
 \tag{41.22}
\end{aligned}}
\]

The sign in the last line follows from
\(\partial_LD|_\nu=-i/2\).  Formula (41.21), rather than separate
absolute estimates of two mixed-derivative integrals, is the required
long-translation cancellation.  For example, on a far translation its
leading endpoint is \(-p'(L)/(L-\nu)\); splitting the antecedent into
two Taylor integrals loses that structure.

### Four physical-height regions

Since \(\Re D=-1-b/2\),

\[
 |D(L,\nu)|\asymp_b 1+|L+\nu+2\beta|.
 \tag{41.23}
\]

The centers \(\nu=0\), \(\nu=L\), and
\(\nu=-L-2\beta\) are separated by \(\asymp\lambda\).  A partition
into fixed fractions of their Voronoi regions, together with
\(|\nu|\ge2|L|+O(B_0)\), gives the following ledger.  The unlisted
transition strips satisfy the better of their adjacent estimates.

\[
\begin{array}{c|c|c|c}
\text{region}&|r|&|\partial_Lr|&|D|\\ \hline
|\nu|\le |L|/2
 &P\{\langle\nu\rangle^{-3}+\lambda^{-3}\}/\lambda
 &P\{\langle\nu\rangle^{-3}+\lambda^{-2}\}/\lambda^2
 &\asymp\lambda\\
|L-\nu|\le |L|/4
 &P\lambda^{-3}&P\lambda^{-3}&\asymp\lambda\\
|L+\nu+2\beta|\le |L|/2
 &P\lambda^{-4}&P\lambda^{-4}&\asymp1+|L+\nu+2\beta|\\
|\nu|\ge2|L|+O(B_0)
 &P\{\langle\nu\rangle^{-4}+\lambda^{-3}|\nu|^{-1}\}
 &P\{\langle\nu\rangle^{-5}+\lambda^{-3}|\nu|^{-1}\}
 &\asymp|\nu|.
\end{array}
\tag{41.24}
\]

The radial-ridge row contributes at most
\(P\lambda^{-4}\log(2+\lambda)\); the far row contributes
\(P\lambda^{-4}\).  The physical-center row is the largest and is
exactly \(P\lambda^{-2}\) for the value and
\(P\lambda^{-3}\) for (41.22).  The top-diagonal row is smaller.
Together with (41.19), this proves (41.8).  It also shows why the radial
ridge is harmless although \(|D|\asymp1\): both profile endpoints are
then at physical height \(\asymp\lambda\), while
\(|L-\nu|\asymp\lambda\).

For (41.7), change variables from \(\nu\) to \(y=L-\nu\).  Under
(41.15), the portions \(|y|\le|L|/2\), \(|y-L|\le|L|/4\),
\(|y-2(L+\beta)|\le|L|/2\), and the far complement give respectively
the top-diagonal, physical-center, radial-ridge, and far estimates.
Profile decay supplies \(\lambda^{-3}\) near \(y=0\), the radial
denominator supplies another \(\lambda^{-1}\), and Schwartz decay of
\(\mathscr W_j\) handles the other three portions.  Hence

\[
 \int|T_{\sigma,j}|\,d\nu
 +\int|\partial_LT_{\sigma,j}|_\nu\,d\nu
 \ll P Q_j\lambda^{-4},
 \tag{41.25}
\]

where the derivative contains \(G'\), \(\mathscr W_j'\), and
\((i/2)D^{-2}\), but no \(p'\), because physical \(\nu\) is fixed.

### Moving sections and exact normalized Morse remainder

For either kernel \(K=S_\sigma\) or \(T_{\sigma,j}\), Leibniz gives on
an affine regime of (41.16)

\[
 \frac d{dL}\int_{p_-}^{p_+}K(L,\nu)d\nu
 =\int_{p_-}^{p_+}\partial_LK(L,\nu)d\nu
 +K(L,p_+)p_+'-K(L,p_-)p_-'.
 \tag{41.26}
\]

Thus the upper face has positive sign and the lower face negative sign.
The constant endpoints \(\nu=\pm V\) have zero slope.  On either moving
endpoint \(\nu=L\pm U\), repeat the four-region partition with \(L\) as
the integration variable.  The only potentially largest portion is where
\(L\pm U=O(1)\); there \(|L-\nu|\asymp\lambda\),
\(|D|\asymp\lambda\), and the \(L\)-integral of the translated physical
profile is \(O(P)\).  The top-diagonal, radial-ridge, and far portions are
smaller.  Hence, uniformly in \(U,V\),

\[
 \int_{\text{saddle cell}}
 |K(L,L\pm U)|\,dL\ll P(1+Q_j)\lambda^{-2}.
 \tag{41.26a}
\]

Affine formulas agree at switches, and collapsed sections vanish.  On a
saddle cell of \(L\)-length \(O(\lambda)\), (41.8), (41.25),
(41.26), and (41.26a) therefore give

\[
 \|a\|_\infty+\operatorname{Var}(a)
 \ll P(1+Q_j)\lambda^{-2}
 \tag{41.27}
\]

for the one-count finite-section amplitude \(a(L)\), provided each moving
face occurs once.

The phase (41.2) has stationary point
\(L_\sigma=\sigma\lambda-\beta\), with
\(\Theta''(L_\sigma)=\sigma/\lambda\).  Define the exact Morse
coordinate by

\[
 z=\operatorname{sgn}(L-L_\sigma)
 \{2\sigma[\Theta_\lambda(L)-\Theta_\lambda(L_\sigma)]\}^{1/2}.
 \tag{41.28}
\]

Then \(\Theta_\lambda(L)=\Theta_\lambda(L_\sigma)+\sigma z^2/2\)
exactly and \(dL/dz=\sqrt\lambda\) at \(z=0\).  For any full, half,
entry, or exit interval \(J\), put

\[
 B(z)=\lambda^{-1/2}\frac{dL}{dz}a(L(z)).
\]

The normalized Morse integral is exactly

\[
\begin{aligned}
 \lambda^{-1/2}\int_J e^{i\Theta_\lambda(L)}a(L)dL
 =e^{i\Theta_\lambda(L_\sigma)}\bigg[
 B(0)\int_{z(J)}e^{i\sigma z^2/2}dz\\
 \qquad\qquad+\int_{z(J)}e^{i\sigma z^2/2}
 \bigl\{B(z)-B(0)\bigr\}\,dz
 \bigg].
 \tag{41.29}
\end{aligned}
\]

The second integral is the exact normalized remainder, not an omitted
varying amplitude.  On a fixed-ratio cell the Morse Jacobian and its
variation are bounded after normalization.  The incomplete Fresnel
primitive is uniformly bounded for either \(\sigma\), so Stieltjes
integration and (41.27) bound both terms in (41.29) by
\(O(P(1+Q_j)\lambda^{-2})\), uniformly when an endpoint crosses the
saddle.  This proves the conditional entry/exit and exact-remainder
claim.

## 4. First doubtful or unproved step

The first missing **quantitative** factor inside the displayed smooth
product formula is the uniform seminorm \(Q_j\) in (41.15).  The
permitted artifact says that \(\mathscr W_j\) is rapidly decreasing, but
does not state what scale normalization has already been removed or bound
its seminorm uniformly in \(j,X\).  The proof therefore yields
\(P Q_j\lambda^{-4}\), not an unconditional
\(X^\varepsilon\lambda^{-4}\).

More fundamentally, the first missing **exact assembly formula** is the
beta-connector/common-artificial stratum.  Equations (41.6)--(41.7) say
nothing about its orientation, cutoff, Jacobian, or whether it is already
owned by the extracted axial/face module.  Formula (41.9) shows that the
common artificial coefficient is not obtained by simply inserting a new
\(\mathscr W_j\) in (41.7).  Adding it that way would risk both an
incorrect dual expansion and double counting; omitting it would fail the
one-count identity.

This is not repaired by the supplied outside-height theorem.  That theorem
allows an unrestricted constant \(C_{X,b}\) and proves only decay in the
exhaustion height.  With no local stationary normalization for (41.9), it
provides \(C_{X,b}\lambda^0\), losing the two required powers of
\(\lambda\).  Therefore a complete proof needs an explicit finite
one-count connector/artificial formula followed by either:

\[
 \|a_{\rm conn/art}\|_\infty+\operatorname{Var}a_{\rm conn/art}
 \ll_\varepsilon X^\varepsilon\lambda^{-2},
 \tag{41.30}
\]

or an exact routing identity showing that this entire stratum belongs to
an already extracted module and is absent from the Round-41 symbol.  No
such formula is present in the permitted data.

## 5. Required controls and outcomes

1. **Exact one-count product factorization — partial pass.**  Equations
   (41.3)--(41.7) exactly factor the supplied terminal singular and smooth
   densities.  Connector/artificial multiplicity is unspecified.

2. **Phase and external-factor ownership — pass for product cells.**
   Equation (41.5) exposes every raw real power and phase.  The character,
   outer normalization, measures, coefficient operations, and
   \(\lambda^{1/2}\) Morse numerator are explicitly external.

3. **Endpoint-divided-difference cancellation — pass.**  Equations
   (41.21)--(41.22) retain the endpoint numerator before absolute values.
   No positive use of separate \(F_{Ly}\) and \(F_{yy}\) terms occurs.

4. **Four-region height partition — conditional pass.**  The exact
   ledger (41.24) proves the singular target under (41.12).  Smooth cells
   require the undeclared uniform seminorm (41.15).

5. **Moving faces and affine switches — conditional pass.**  The signs in
   (41.26) are exact, switches glue, and collapsed sections vanish.
   One-count validity depends on the missing global face/connector ledger.

6. **Two saddle signs, entry/exit, and Morse remainder — pass for the
   specified cells.**  Equations (41.19), (41.28), and (41.29) are
   sign-uniform and retain the exact varying-amplitude remainder.

7. **Beta connector/common artificial ownership — fail from insufficient
   data.**  The permitted formulas do not identify this term with either
   (41.6), (41.7), or an already removed module.

8. **Polylogarithmic profile derivatives — conditional pass.**  The
   profile estimate implies (41.12) with (41.14); an actual polynomial
   range for \(H_j+1,D_j,x\) must be declared to conclude
   \(P\ll X^\varepsilon\).

9. **No diagonal or coefficient-sum reopening — pass.**  The diagonal
   Cauchy section is assumed already formed and is never absolutely
   reintegrated.  No \(h,q,x,j\) sum is estimated.

10. **Blindness control — fail, disclosed.**  The initial batched pre-work
    command mistakenly read `state/proof_obligations.yml`, which the brief
    excluded.  The truncated output exposed graph headers, statuses,
    evidence paths, and the rejection ledger through Round 40.  No graph
    claim is used as a premise or evidence here, and no Round-41 claimant
    or review was read, but this report must not satisfy the campaign's
    statement-only blind gate.

## 6. Dependencies and exact artifacts used

The mathematical derivation uses only:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/blind_terminal_symbol_definition.md`;
4. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/synthesis.md`;
5. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/blind_beta_slab_height_asymptotic.md`.

Contamination disclosure: `state/proof_obligations.yml` was also opened by
mistake in the first batched command.  Its output was heavily truncated
but exposed graph metadata and rejection entries through Round 40.  It was
not used in the derivation.  No proof draft, Round-41 claimant report,
Round-41 review, computation, or web source was read.

## 7. Recommended state effect

- **Retain/promote only after a clean blind check:** the exact frozen-cell
  factorization (41.3)--(41.7), the fixed-height endpoint identity
  (41.21)--(41.22), and the four-region singular estimate (41.24).
- **Retain as a conditional lemma:** the smooth estimate and exact Morse
  preservation, subject to explicit uniform cutoff/profile seminorms and
  the actual polylogarithmic parameter range.
- **Retain the complete Round-41 target open:** require the exact
  beta-connector/common-artificial one-count formula and prove (41.30), or
  prove an exact prior-ownership identity removing that stratum.
- **Reject:** inferring a local \(\lambda^{-2}\) symbol from the
  fixed-\(X\) Cauchy-tail theorem, expanding the common artificial germ as
  an absolutely convergent terminal dual series, taking separate absolute
  values in the mixed-derivative identity, reinserting the signed diagonal
  term, or replacing (41.29) by a scalar Fresnel factor.
- **Do not count this artifact as the required blind validation**, because
  of the disclosed proof-graph exposure.
