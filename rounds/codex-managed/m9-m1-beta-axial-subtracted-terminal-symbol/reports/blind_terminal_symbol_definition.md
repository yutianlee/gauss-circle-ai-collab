# Round 39 blind report: exact axial-subtracted symbol and a normalization/type obstruction

Task: blind_terminal_symbol_definition  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation or external theorem

## 1. Result

The limiting **aggregate** axial-subtracted terminal symbol is now well
defined, but the requested bare \(\lambda\)-bounds are not yet a
well-typed statement for that symbol.  The aggregate is summed/integrated
over \(j,h,q,x\), while
\(\lambda=\pi q\sqrt{Xx}/D_j\) changes from cell to cell.  Conversely,
the accepted Round-31 \(\lambda^{-2}/\lambda^{-3}\) result concerns the
phase-removed, pre-stationary-numerator divided-difference kernel, not the
fully normalized aggregate with the \(h,D_j,x\) and external factors.

Fix the legal terminal line \(c'=5/4\), put
\[
 L=\mu+\nu,\qquad t=\frac L2+\beta,qquad
 \alpha=L+\beta,qquad
 \rho_0=-1-\frac b2,                                \tag{39.1}
\]
and set
\[
 y=L-\nu=\mu,qquad
 A_\beta(L)=\rho_0-i(L+\beta),qquad
 D_\beta(L,\nu)=A_\beta(L)+\frac{i}{2}y.            \tag{39.2}
\]
Thus \(D_\beta=\rho\).  If \(H(L,\nu;\beta)\) denotes the complete
numerator of one actual terminal cell after common rho recombination but
before the top polar denominator, define the exact regularizer
\[
\boxed{
 \mathcal R_{A}[H](L,\nu)
 :=-\frac{iH(L,L)}{2A(L)D(L,\nu)}
 +\frac{H(L,\nu)-H(L,L)}
 {(L-\nu)D(L,\nu)}.}                               \tag{39.3}
\]
The quotient is extended continuously across \(L=\nu\).  Formula (39.3)
is the unique remainder after removing, as one linear operation, the hard
top delta and its constant-numerator logarithmic/PV partner.

Let \(\mathscr H_{j,h,q,x}^{\pm}\) be the actual numerator specified in
Section 2, and use the one-count saddle/transition partition there.  The
side-collapsed, endpoint-image-free, axial-subtracted symbol is the
\(L^1_\nu\)-limit
\[
\boxed{\begin{aligned}
 K_{\rm term}^{\circ}(L,\nu)
 :=-\frac4\pi X^{1/4}\operatorname {Re}\Bigg{
 e(1/8)\sum_{\pm}\sum_{j,h,q}\chi_4(q)
 \int_{1}^{N_X}\!\int_{\mathbb R}\psi(\beta)
 \left(-\frac{i}{2\pi}\right)
 \mathcal R_{A_\beta}
 [\mathscr H_{j,h,q,x}^{\pm}](L,\nu;\beta)
 \,d\beta\,dx\Bigg}.                             \tag{39.4}
\end{aligned}}\]
The inner integral in (39.4) is the \(\beta\)-integral over
\(\mathbb R\) (effectively over \(\operatorname{supp}\psi\)); the outer
integral is the \(x\)-integral over \([1,N_X]\), and both follow the
displayed finite sums.
Here the endpoint/arithmetic module, radial sides, the full \(v=0\) vector,
connector images assigned to it, combined collisions, and the one corner
have already been removed or reconciled by the accepted operations.  They
are not reinserted into (39.4).  The common artificial germ is contained in
\(\mathscr H\), rather than added as a second rho residue.  Round 38 makes
the limit in (39.4) independent of the prescribed cofinal exhaustion.

There is consequently no single \(\lambda\) with which to interpret
(39.6) for (39.4).  To make the target well typed, one must first freeze
\((\pm,j,h,q,x,\beta)\) and declare an exact factorization
\[
 \mathscr H_{j,h,q,x}^{\pm}
 =\mathfrak N_{j,h,q,x}^{\pm}(X,\beta)
  e^{i\Phi_{j,h,q,x}^{\pm}}
  \widetilde H_{j,h,q,x}^{\pm},                    \tag{39.5a}
\]
specifying which actual coefficient \(\mathfrak N\), phase, character,
and external normalization stay outside the object called
\(K_{\rm term}^{\circ}\).  No permitted accepted statement supplies
(39.5a).  This is the first exact result of the audit: silently applying
the bare target to either the aggregate (39.4) or the raw cell changes its
normalization.

At fixed physical \(\nu\), the exact derivative of (39.3) is (39.13)
below.  Once a coefficient-level normalization is fixed, it exposes the
next missing actual coefficient: the complete second translation divided
difference
\[
 \boxed{
 \mathfrak E_H(L,\nu)
 :=\frac{\partial_LH(L,\nu)-\mathsf D H(L,L)}{L-\nu}
   -\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2},
 \qquad \mathsf D=\partial_L+\partial_\nu.}         \tag{39.5}
\]
The separated \(R_1\) kernel controls (39.5), but no accepted result
controls it for the actual gamma/radial/profile coefficient uniformly
through both saddles, entry/exit, the rho seam, and moving faces.

If (39.4) is interpreted literally with all actual prefactors inside the
target estimate, the best accepted raw-cell capacity is (39.17), containing
the explicit factor
\(X^{3/4-a/2}D_j^a(H_j+1)^b\lambda^\kappa\),
\(\kappa=3/4+(a+b)/2\), not an \(X^\varepsilon\) coefficient.  Round 38
deliberately hides this in \(C_{X,b}\).  Hence neither
\[
 |K_{\rm term}^{\circ}|\ll X^\varepsilon\lambda^{-2}w(\nu),
 \qquad
 |\partial_LK_{\rm term}^{\circ}|\ll
 X^\varepsilon\lambda^{-3}w(\nu)                  \tag{39.6}
\]
is proved for the complete actual symbol.  Equation (39.6) is therefore
either ill typed for the aggregate or quantitatively open for a declared
coefficient-level normalization.  This is not a claim that the intended
normalized estimate is false.

## 2. Exact statement and hypotheses

Take
\[
 u=a+i(L-\nu),\qquad v=b+i\nu,qquad
 s=\frac54+i\left(\frac L2+\beta\right),
 \qquad |\beta|\le2B_0,                            \tag{39.7}
\]
where \(b=1/\log(2X)\), \(a/2+b<1/4\), and
\(a+b<1/2\).  The derivative required in this round is
\[
 \left.\partial_L\right|_\nu:\quad
 \partial_L\mu=1,\quad \partial_Lt=\frac12,\quad
 \partial_L\alpha=1,\quad \partial_L\beta=0,\quad
 \partial_L\rho=-\frac i2.                        \tag{39.8}
\]
It is not differentiation at fixed \(\mu\).

At the \(x\)-integrand level, remove the top polar factor
\((a+i\mu)^{-1}\) and the radial denominator \(D_\beta^{-1}\).  Up to
the fixed contour constants already displayed in (39.4), the remaining
actual numerator is
\[
\begin{aligned}
 \mathscr H_{j,h,q,x}(L,\nu;\beta)={}&
 h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 (-\pi i\sqrt X)x^{-3/2-b/2}\\
 &\times f_b(\nu)\,\mathscr W_j(L-\nu)\,
 K_{u+v}(1-s)\,e(\sqrt{Xx})\\
 &\times
 \exp\!\left(i(L-\nu)\log\frac{D_j}{2\sqrt X}
 +i\nu\log(H_j+1)-iL\log q-i\beta\log(hq)
 -\frac i2(L+\nu+2\beta)\log x\right).            \tag{39.9}
\end{aligned}
\]
Here \(f_b(\nu)=\widehat\phi(b+i\nu)\).  For the singular top cell
\(\mathscr W_0=1\), because its factor \((a+i\mu)^{-1}\) has already
become the signed distribution.  The regular top remainder and interior
scales use their actual rapidly decreasing Mellin factors in
\(\mathscr W_j\); they do not carry another top delta.  Formula (39.9)
records exactly the coefficient identity
\[
 \left(\frac hq\right)^{(u+v)/2}(hq)^{-s}
 =h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}
 q^{-iL}(hq)^{-i\beta}.                            \tag{39.10}
\]
Every floor \(H_j+1\), actual scale, hard-top convention, character, and
eventual symmetric star is retained.  Stars are licensed by the already
completed physical inversion; no finite-height star is inserted into the
antecedent.

The notation \(\mathscr H^{\pm}\) means (39.9) restricted by a smooth
one-count partition into the positive and negative saddle cells
\(|\alpha|\asymp\lambda\), their entry/exit collars, bounded-alpha cell,
rho/collision cell, moving-face cells, and the remaining nonsaddle tails,
where
\[
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j}.               \tag{39.11}
\]
The cutoffs sum to one before any estimate.  On the rho cell the expression
is interpreted through the common analytic identity
\(\omega G+(1-\omega)R_1-\omega E_1=R_1\); an isolated
\(1/\rho\) term is forbidden.

The full \(v=0\) Cauchy vector, including its connector-axis and collision
shares, is extracted once before (39.4).  This is axial subtraction.  It is
not the pointwise replacement of \(f_b\) by
\(f_b-(b+i\nu)^{-1}\).  The latter would change the contour operation.

## 3. Proof or derivation

The physical top identity is
\[
 \frac1{2\pi}\frac1{0^++iy}
 =\frac12\delta_0(y)-\frac{i}{2\pi}
 \operatorname {PV}\frac1y.                       \tag{39.12}
\]
Multiplying (39.12) by \(H(L,\nu)/D(L,\nu)\), add and subtract
\(H(L,L)/(A(L)y)\) in the PV part.  Since
\[
 \frac1y\left(\frac1D-\frac1A\right)
 =-\frac i{2AD},
\]
the remaining ordinary density is exactly
\((-i/2\pi)\mathcal R_A[H]\).  The removed part is the single delta
\(H(L,L)\delta_0(y)/(2A)\) plus its constant-numerator PV/log partner.
This proves (39.3)--(39.4) and prevents a second top or axial subtraction.

Write \(H_0(L)=H(L,L)\),
\(\dot H_0=(\partial_L+\partial_\nu)H(L,L)\).  Because
\(A'=-i\), \(y'=1\), and \(D'=-i/2\) at fixed \(\nu\), direct
differentiation gives
\[
\boxed{\begin{aligned}
 \left.\partial_L\mathcal R_A[H]\right|_\nu={}&
 -\frac{i\dot H_0}{2AD}
 +\frac{H_0}{2A^2D}+\frac{H_0}{4AD^2}\\
 &+\frac{\partial_LH(L,\nu)-\dot H_0}{yD}
 -\frac{H(L,\nu)-H_0}{y^2D}
 +\frac{i\{H(L,\nu)-H_0\}}{2yD^2}.
                                                               \tag{39.13}
\end{aligned}}\]
All apparent singularities at \(y=0\) cancel by Taylor expansion.  The
middle two terms contain precisely (39.5).  This is the fixed-physical-
height ledger; replacing it by \(\mathsf D\mathcal R_A\) is the rejected
fixed-\(\mu\) shortcut.

For the separated model \(H(L,\nu)=f_b(\nu)\), (39.3) becomes the accepted
kernel
\[
 -\frac{if_b(L)}{2A\{A+iy/2\}}
 +\frac{f_b(\nu)-f_b(L)}{y\{A+iy/2\}}.             \tag{39.14}
\]
On \(|A|\asymp|L|\asymp\lambda\), divided differences of the actual
height profile prove the \(\lambda^{-2}\) value and
\(\lambda^{-3}\) fixed-\(\nu\) derivative bounds with an integrable
polylogarithmic weight.  Thus the top subtraction itself is not the gap.

For the complete numerator, split the gamma quotient into its bounded-beta
and tangent factors.  With
\(\kappa=3/4+(a+b)/2<1\), two-sided Stirling gives
\[
 |K_{u+v}(1-s)|\asymp_{a,b,\beta}(1+|\alpha|)^\kappa.             \tag{39.15}
\]
At fixed \(\nu\), the logarithmic derivative of the complete oscillatory
coefficient in (39.9) has leading term
\[
 \partial_L\log\mathscr H
 =i\log\frac{|\alpha|}{\lambda}
 +O_{a,b,B_0}\!\left(\frac1{1+|\alpha|}\right)
 +\partial_L\log\mathscr W_j,                     \tag{39.16}
\]
on either Stirling side.  Indeed, the tangent gamma phase contributes
\(i\log(2|\alpha|/\pi)\); the scale, coefficient, and radial phases
contribute
\(i\log(D_j/(2\sqrt X))-i\log q-(i/2)\log x\).
Their sum is \(i\log(|\alpha|/\lambda)\).  This exact cancellation is
favorable at the saddle, but the accepted context supplies no uniform
entry/exit or moving-face bound turning (39.16) into \(O(\lambda^{-1})\)
on a complete cell.

The full modulus ledger before the \(j,h,q,x\) sums is
\[
\begin{array}{c|c}
\text{factor}&\text{capacity on }|\alpha|\asymp\lambda\\ \hline
\text{external normalization}&X^{1/4}\\
\text{radial numerator}&\sqrt X\,x^{-3/2-b/2}\\
\text{scale/profile real part}&
 (D_j/(2\sqrt X))^a(H_j+1)^b\\
\text{arithmetic real part}&
 h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}\\
\text{gamma quotient}&\lambda^\kappa\\
\text{regularized top/rho value}&\lambda^{-2}w_b(\nu)\\
\text{denominator part of fixed-\nu derivative}&
 \lambda^{-3}w_b(\nu)\\
\text{coefficient part of fixed-\nu derivative}&
 \lambda^{-2}\{|\log(|\alpha|/\lambda)|+O(\lambda^{-1})\}
 w_b(\nu).
\end{array}                                                       \tag{39.17}
\]
Thus the raw value capacity is
\[
 X^{3/4-a/2}D_j^a(H_j+1)^b
 h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}
 x^{-3/2-b/2}\lambda^{\kappa-2}w_b(\nu),           \tag{39.18}
\]
up to fixed constants.  The \(h,q\) exponents are absolutely summable,
including one logarithmic derivative.  The height profile obeys
\(\|f_b\|_1\ll\log(2/b)\) and its differentiated polar contribution is
\(O(b^{-1})\); with \(b=1/\log(2X)\), these are polylogarithmic.  Neither
fact removes the explicit \(X,D_j,x,\lambda^\kappa\) coefficient in
(39.18), nor controls (39.5) across the nonseparated cells.

Round 38 proves that the signed sum of these cells has an integrable
\(\nu\)-tail with a constant \(C_{X,b}\).  Existence of that sum does not
upgrade (39.18) to an \(X^\varepsilon\) cell symbol or supply the extra
\(\lambda^{-1}\) in (39.13).

## 4. First doubtful or unproved step

The first missing datum is definitional: the accepted artifacts do not say
which factor in (39.18) is the “stationary numerator” removed from the bare
symbol.  The aggregate (39.4) has many values
\(\lambda_{j,q,x}\), so (39.6) cannot literally be its pointwise bound.
The raw cell does have one \(\lambda\), but then its exact capacity is
(39.18), not a bare \(X^\varepsilon\lambda^{-2}\).  Thus the project must
first freeze (39.5a), including whether \(X^{1/4}\), \(\chi_4(q)\), the
real \(h,q,D_j,x\) weights, and the tangent gamma power live in
\(\mathfrak N\) or in the symbol.

After that normalization is declared, the first unproved quantitative
datum is an \(O(X^\varepsilon)\),
\(L^1_\nu\)-polylogarithmic bound for the phase-reduced coefficient.  No
permitted theorem gives it; Round 38 explicitly leaves its constants as
\(C_{X,b}\).  No downstream \(j,h,q,x\) summation is performed in this
report.

Even conditional on that zeroth-order normalization, the first derivative
survivor is (39.5), equivalently the complete physical-height coefficient
\[
 \partial_\nu(\partial_L+\partial_\nu)
 \mathscr H_{\rm complete},                        \tag{39.19}
\]
after translation and moving-face recombination.  Formula (39.16) shows
why a termwise product-rule estimate is insufficient: the phase derivative
is small only after the exact saddle cancellation and is not uniformly
\(O(\lambda^{-1})\) on the entry/exit and face collars from any accepted
statement.  The rho cell additionally requires the common analytic germ,
not the separated \(1/\rho\) calculation.

A sufficient missing lemma is therefore an actual, phase-reduced,
two-saddle patching theorem which proves, with translated face traces,
\[
 |\mathcal R_A[\mathscr H_{\rm complete}]|
 \ll X^\varepsilon\lambda^{-2}w_b(\nu),\qquad
 |\partial_L\mathcal R_A[\mathscr H_{\rm complete}]|_\nu
 \ll X^\varepsilon\lambda^{-3}w_b(\nu),           \tag{39.20}
\]
and \(\|w_b\|_1\ll\log^C(2X)\), uniformly in the actual scale and
endpoint data.  Equation (39.20) is exactly the desired theorem, not a
consequence of tail convergence.

## 5. Required controls and outcomes

### Limiting definition and one-count ownership

**Pass.**  Equation (39.4) is formed only after aggregate endpoint and
arithmetic routing, exact radial-side deletion, full axial extraction, and
the Round-38 Cauchy limit.  Artificial/collision germs and the one corner
are assigned once; no boundary module is reinserted.

### Fixed physical height, not fixed top height

**Pass.**  The derivative rules (39.8) and formula (39.13) keep \(\nu\)
fixed.  They expose (39.5); no fixed-\(\mu\) product rule is substituted.

### Exact \(X\)/\(\lambda\) ledger

**Pass as a type/normalization obstruction.**  Equations (39.10),
(39.15), and (39.17)--(39.18) retain every real power and the external
\(X^{1/4}\) factor.  They show both that the aggregate has no single
\(\lambda\), and the precise raw-cell coefficient that must be assigned by
(39.5a).  No coefficient or scale sum is executed.

### Signed top and axial subtraction

**Pass.**  Delta and constant-numerator PV/log terms are removed together
before absolute values.  Axial subtraction is the full \(v=0\) vector,
not a pointwise polar deletion.

### Two saddles, entry/exit, rho, and moving faces

**Definition pass; quantitative open.**  The cells form a one-count
partition and the two Stirling signs have the same power.  No accepted
uniform estimate supplies (39.20) on entry/exit, rho, or moving-face cells.

### Separated \(R_1\) control versus complete kernel

**Separated pass; complete open.**  Formula (39.14) satisfies the target.
The actual coefficient and its second translation divided difference
(39.5) are the first complete-kernel survivors.

### Weighted profile and normalization

**Profile pass, global coefficient open.**  The accepted \(b\)-dependence
is polylogarithmic and the \(h,q\) real powers are summable.  The scale,
radial, gamma, and external-normalization coefficient in (39.18) has no
accepted \(X^\varepsilon\) reduction.

### No existence-to-estimate or downstream overreach

**Pass.**  The Round-38 existence theorem is not used as a pointwise or
derivative estimate.  No finite-section BV conclusion, beta-transition
bound, or Gauss-circle estimate is asserted.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md`;
4. `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md`;
5. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`.

No proof graph, proof draft, excluded report, Round-39 report, computation,
or web source was read or used.

## 7. Recommended state effect

- **Promote** the exact limiting **aggregate** axial-subtracted symbol
  definition (39.3)--(39.4), with its one-count endpoint, side, axial,
  artificial, collision, connector, and corner ownership.
- **Promote** the fixed-physical-height derivative identity (39.13), the
  exact actual-factor ledger (39.17)--(39.18), and the identification of
  the complete second translation divided difference (39.5).
- **Revise before estimating** the bare weighted terminal-symbol statement:
  it is ill typed for the aggregate because \(\lambda\) is cell-dependent.
  Freeze the coefficient-level phase/stationary-numerator factorization
  (39.5a).  Then retain open the \(X^\varepsilon\) value normalization and
  the uniform derivative bound for (39.5)/(39.19) through entry/exit, rho,
  and moving faces.
- **Reject** inferring (39.6) from Cauchy-tail existence, applying the
  separated kernel termwise to the complete symbol, differentiating at
  fixed \(\mu\), inserting a second axial/artificial share, or invoking
  the downstream BV lemma as proof of the beta transition.
