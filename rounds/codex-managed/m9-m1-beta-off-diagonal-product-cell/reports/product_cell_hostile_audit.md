# Round 41 hostile audit: off-diagonal and smooth product cells

Task: `product_cell_hostile_audit`  
Role: seam reviewer  
Allocation: 100% analytical/algebraic; no computation and no web source

## 1. Result

The frozen off-diagonal theorem survives the hostile audit.  After the
already accepted signed diagonal Cauchy section is set aside, the exact
terminal numerator has only the following two normalized product types on
one signed large-\(\alpha\) cell:

\[
 K_\Delta(L,\nu)
 =G(L)\,{p(\nu)-p(L)\over (L-\nu)D(L,\nu)},               \tag{41H.1}
\]

and, for each smooth top or interior spatial share,

\[
 K_W(L,\nu)
 ={G(L)p(\nu)W(L-\nu)\over D(L,\nu)}.                    \tag{41H.2}
\]

Here

\[
 \alpha=L+\beta,\qquad y=L-\nu,\qquad
 D(L,\nu)=-1-{b\over2}-{i\over2}(L+\nu+2\beta),          \tag{41H.3}
\]

\(|\alpha|\asymp\lambda\), and \(G\) is the exact
phase-removed, \(\lambda\)-normalized one-large-gamma symbol.  The actual
height profile is not merely \(f_b(\nu)\): it includes the remaining
unit-modulus physical-height phase,

\[
 p(\nu)=e^{i\gamma\nu}f_b(\nu),\qquad
 \gamma=\log {2\sqrt X\,(H_j+1)\over D_j\sqrt x}.         \tag{41H.4}
\]

Keeping (41H.4) is an important phase-ownership control.  On the actual
ranges, \(|\gamma|\ll\log(2X)\), so it costs only powers of \(\log X\),
not a power of \(\lambda\), \(b^{-1}\), or \(X\).

Put

\[
 Q_0(L,\nu)={p(\nu)-p(L)\over L-\nu},\qquad
 Q_1(L,\nu)
 ={-p'(L)(L-\nu)-p(\nu)+p(L)\over(L-\nu)^2}.              \tag{41H.5}
\]

Both are continued across \(\nu=L\), with
\(Q_0(L,L)=-p'(L)\) and \(Q_1(L,L)=-p''(L)/2\).  The exact
fixed-physical-height derivative is

\[
 \boxed{
 \partial_L^\nu K_\Delta
 ={G'Q_0+GQ_1\over D}+{iGQ_0\over2D^2}.}                  \tag{41H.6}
\]

Thus the dangerous long translation is evaluated as the endpoint second
difference \(Q_1\), before absolute values.  No separate estimate of the
two mixed-derivative integrals from Round 40 is used.

Uniformly on both signed saddle, entry, and exit cells, there is a fixed
\(C\) such that

\[
\begin{aligned}
 \sup_L\int_{\mathbb R}|K_\Delta(L,\nu)|\,d\nu
   &\ll \log^C(2X)\lambda^{-2},\\
 \sup_L\int_{\mathbb R}|\partial_L^\nu K_\Delta(L,\nu)|\,d\nu
   &\ll \log^C(2X)\lambda^{-3},                          \tag{41H.7}\\
 \sup_{U\ge0}\sum_{\pm}\int_{I_{\sigma,\lambda}}
   |K_\Delta(L,L\pm U)|\,dL
   &\ll \log^C(2X)\lambda^{-2}.
\end{aligned}
\]

Every normalized smooth share satisfies the same bounds, in fact with at
least one spare inverse power of \(\lambda\).  Since a signed cell has
length \(O(\lambda)\), (41H.7) gives value plus integrated
fixed-\(\nu\) derivative plus all moving physical traces

\[
 \ll \log^C(2X)\lambda^{-2}
 \ll_\varepsilon X^\varepsilon\lambda^{-2}.              \tag{41H.8}
\]

The exact Morse change of variables preserves this mixed BV norm.  Its
leading term is the incomplete Fresnel factor times the actual saddle
value, and its exact varying-amplitude remainder is bounded by the same
right side of (41H.8).  At an entry or exit exactly through the saddle the
leading coefficient is one half of the corresponding full Fresnel
coefficient, for both Hessian signs.  No scalar-Fresnel replacement of a
varying cell is made.

No actual-form \(\lambda\), height-exhaustion, trace, or \(b^{-1}\)
obstruction remains.  Harmonic logarithms occur only on the radial ridge
with an extra \(\lambda^{-2}\) reserve, and all powers of \(b^{-1}\) and
the height modulation in (41H.4) are polylogarithmic in \(X\).

## 2. Exact statement and hypotheses

Work on the legal terminal line \(c'=5/4\), with

\[
 b={1\over\log(2X)}>0,\qquad a+b<{1\over2},\qquad
 {a\over2}+b<{1\over4},
\]

and freeze \((j,h,q,x,\beta,\sigma)\), where
\(\sigma\in\{+1,-1\}\), \(|\beta|\le2B_0\),

\[
 \lambda={\pi q\sqrt{Xx}\over D_j},
 \qquad c_0\lambda\le \sigma(L+\beta)\le C_0\lambda,     \tag{41H.9}
\]

and \(\lambda\ge\lambda_0(B_0,c_0)\).  The excluded bounded-\(\alpha\)
cell is a different obligation.

### Exact raw-cell factorization

Set

\[
 r={5\over4}-{a+b\over2},\qquad
 \kappa={3\over4}+{a+b\over2}<1,
\]

and

\[
 c_L=\log {D_j\over2q\sqrt{Xx}},\qquad
 \gamma=\log {2\sqrt X\,(H_j+1)\over D_j\sqrt x}.        \tag{41H.10}
\]

The exact exponential in the authorized terminal numerator splits as

\[
\begin{aligned}
 &\exp\!\left(i(L-\nu)\log{D_j\over2\sqrt X}
 +i\nu\log(H_j+1)-iL\log q-i\beta\log(hq)
 -{i\over2}(L+\nu+2\beta)\log x\right)\\
 &\hspace{20mm}=e^{iLc_L}e^{i\gamma\nu}
                 e^{-i\beta\log(hqx)}.                  \tag{41H.11}
\end{aligned}
\]

On either sign, exact gamma factorization followed by signed Stirling
normalization gives the identity

\[
 e^{iLc_L}K_{a+b+iL}(1-s)
 =e^{i\Psi_{\sigma,\lambda}(L)}
   \lambda^\kappa G_{\sigma,\lambda}(L,\beta),           \tag{41H.12}
\]

where the leading phase is chosen so that

\[
 \Psi'_{\sigma,\lambda}(L)=\log {|L+\beta|\over\lambda},
 \qquad
 \Psi''_{\sigma,\lambda}(L)={1\over L+\beta},           \tag{41H.13}
\]

and the exact remainder is a symbol:

\[
 |\partial_L^mG_{\sigma,\lambda}(L,\beta)|
 \le C_m\lambda^{-m},\qquad 0\le m\le2.                 \tag{41H.14}
\]

This is uniform for both signs.  The bounded-\(\beta\) gamma quotient is
kept exact in \(G\); it is not subjected to a false second large-height
Stirling expansion.  Smooth scaled saddle cutoffs may also be included in
\(G\), since their \(m\)-th derivatives are \(O(\lambda^{-m})\).

Consequently the authorized raw numerator is exactly

\[
\begin{aligned}
 \mathscr H={}&\mathfrak A_{j,h,q,x}(X,a,b)
 e(\sqrt{Xx})e^{-i\beta\log(hqx)}
 e^{i\Psi_{\sigma,\lambda}(L)}\lambda^\kappa\\
 &\hspace{25mm}\times
 G_{\sigma,\lambda}(L,\beta)p(\nu)\mathscr W(L-\nu),  \tag{41H.15}\\
 \mathfrak A_{j,h,q,x}(X,a,b)={}&
 (-\pi i\sqrt X)x^{-3/2-b/2}
 h^{-r}q^{-5/4-(a+b)/2}
 \left({D_j\over2\sqrt X}\right)^a(H_j+1)^b .          \tag{41H.16}
\end{aligned}
\]

For the singular hard-top share, \(\mathscr W=1\) and only
\(K_\Delta\) in (41H.1) is audited here.  The diagonal \(K_C\) is the
already accepted signed Cauchy module and is not reopened.  For a smooth
top remainder or interior spatial share, \(\mathscr W=W\) is its actual
normalized Mellin factor and (41H.2) applies.  After its dyadic scale
phase is extracted as in (41H.11), the finite family of actual \(W\)'s
satisfies, for every needed \(N\),

\[
 |W^{(m)}(y)|\le C_{m,N}(1+|y|)^{-N},\qquad 0\le m\le2.   \tag{41H.17}
\]

The cell symbol is (41H.1) or (41H.2), not the raw expression (41H.15).
The following remain outside it exactly once: \(\chi_4(q)\), the real
coefficient (41H.16), \(\lambda^\kappa\) as algebraically incorporated
into the accepted stationary numerator \((D_j/q)\lambda\), the radial
\(x\)-integration, \(D_j,H_j+1\), floors and stars, the two residual
\((2\pi)^{-1}\) contour measures, and the external
\(-(4/\pi)X^{1/4}\operatorname{Re}(e(1/8)\,\cdot)\).  Formula
(41H.15) is the raw ledger showing that none of these factors is hidden in
the norm.

### Actual profile hypothesis

The accepted positive-line profile and (41H.4) obey, for \(0\le m\le3\),

\[
 \|p^{(m)}\|_1+
 \sup_{|t|\ge1}|t|^3|p^{(m)}(t)|
 \le P_X,\qquad P_X\ll\log^C(2X).                       \tag{41H.18}
\]

Near the axial point, derivatives may cost powers of \(b^{-1}\); since
\(b^{-1}=\log(2X)\), they are included in \(P_X\).  At large height the
underlying \(f_b\) has cubic decay.  Multiplication by
\(e^{i\gamma\nu}\) preserves that decay and adds only powers of
\(|\gamma|\ll\log(2X)\).  The line \(b>0\) remains fixed; no passage
through \(b=0\) is used.

### One-count ownership

The surviving terminal bulk carries the single compact factor
\(\psi(\beta)\) and one signed-saddle partition.  The Cauchy--Green beta
connector has the already accepted orientation \(-\psi'(\beta)\), and
the internal \(\psi'(\alpha)\) connectors cancel between the two
hierarchical pieces.  In the endpoint-free axial-subtracted terminal
vector those connector/axis images have already been assigned once to the
boundary/axial ledger; they are not a second copy of (41H.1) or
(41H.2).  If the bounded multiplier \(-\psi'(\beta)\) is retained while
checking a finite connector antecedent, the estimates below are unchanged.

Likewise, the common artificial germ is simplified before estimation:

\[
 \omega G_{\rm raw}+(1-\omega)R_1-\omega E_1=R_1,
 \qquad G_{\rm raw}-E_1-R_1=0.                            \tag{41H.19}
\]

Thus every \(\omega'\) and higher cutoff term cancels under identical
masks, sections, stars, and endpoint ownership.  The crossed artificial
residue is separately owned, while the terminal denominator in (41H.3)
has real part \(-1-b/2\) and no pole.  No connector or artificial factor
is silently estimated twice.

## 3. Proof or derivation

### Gamma and profile symbols

The exact gamma quotient has one bounded-\(\beta\) ratio and one
large-\(\alpha\) ratio.  For the latter, the real-part difference of the
two gamma arguments is \(\kappa=3/4+(a+b)/2\).  On either half-line,
signed Stirling expansion therefore gives

\[
 R_\alpha=e^{i\phi_\sigma(\alpha)}
 \left({|\alpha|\over2}\right)^\kappa
 \{g_{\sigma,0}(\alpha)+O_N(|\alpha|^{-N})\},
\]

with the usual differentiated symbol bounds.  Combining the exact
linear powers of \(2,\pi,D_j,q,X,x\) gives (41H.12)--(41H.14).  In
particular, differentiating the removed phase would create the forbidden
\(\log(|\alpha|/\lambda)\) term, while differentiating the retained
symbol costs \(\lambda^{-1}\).  This verifies the phase seam on both
sides without replacing the bounded gamma ratio by Stirling.

Equation (41H.11) verifies the other phase seam.  The \(L\)-linear phase
belongs to \(\Psi\); the \(\nu\)-linear phase belongs to the actual
profile (41H.4); and the compact \(\beta\)-phase is a unit-modulus
external cell coefficient.  Hence no derivative in the audited norm
produces an undeclared \(\log q\) or algebraic scale factor.

### Cancellation-preserving singular derivative

Since \(p(\nu)\) is fixed when \(L\) is differentiated at fixed physical
height,

\[
 \partial_L^\nu Q_0=Q_1.
\]

This proves (41H.6).  It is also exactly the product specialization of the
Round-40 identity: for \(H(L,\nu)=G(L)p(\nu)\), the complete second
translation coefficient is

\[
 \mathfrak E_H=G'Q_0+GQ_1.                               \tag{41H.20}
\]

Formula (41H.20), rather than separate absolute bounds for
\(F_{Ly}\) and \(F_{yy}\), is used everywhere below.  In particular, on
the long translated segment \(y\asymp2L\),

\[
 |Q_0|\ll P_X\lambda^{-4},\qquad
 |Q_1|\ll P_X\lambda^{-4},                               \tag{41H.21}
\]

even though a termwise mixed-derivative integral can be as large as
\(\lambda^{-1}\).

### Four-region physical-height estimate

Write

\[
 R=L+\nu+2\beta=2\alpha-y.
\]

Then \(|D|\asymp1+|R|\), and \(y+R=2\alpha\) prevents the top
diagonal and radial ridge from colliding on a large-\(\alpha\) cell.
Choose a small fixed \(\delta>0\) and partition physical height into

\[
 \mathcal P=\{|\nu|\le\delta\lambda\},\quad
 \mathcal T=\{|y|\le\delta\lambda\},\quad
 \mathcal R=\{|R|\le\delta\lambda\},                    \tag{41H.22}
\]

and the remaining comparable-height region and far tails.  The three
displayed neighborhoods are disjoint after reducing \(\delta\), up to
harmless bounded overlaps.

On \(\mathcal P\), both \(|y|\) and \(|R|\) are \(\asymp\lambda\).
Using (41H.18),

\[
 |Q_0|\ll {|p(\nu)|+P_X\lambda^{-3}\over\lambda},
 \qquad
 |Q_1|\ll {P_X\lambda^{-3}\over\lambda}
          +{|p(\nu)|+P_X\lambda^{-3}\over\lambda^2}.
\]

Integration gives respectively \(P_X\lambda^{-2}\) for the value and
\(P_X\lambda^{-3}\) for (41H.6).  This is the only region that reaches
the target value scale.

On \(\mathcal T\), both \(L\) and every point between \(L\) and \(\nu\)
have magnitude \(\asymp\lambda\), while \(|D|\asymp\lambda\).  Local
Taylor formulas give \(|Q_0|+|Q_1|\ll P_X\lambda^{-3}\).  Its value
and derivative masses are \(O(P_X\lambda^{-3})\).  At \(y=0\) the
continuous values in (41H.5) show explicitly that no top pole remains.

On \(\mathcal R\), \(|y|\asymp\lambda\) and
\(|\nu|\asymp|L|\asymp\lambda\).  The endpoint formulas, not an
absolute mixed-derivative representation, give (41H.21).  Hence

\[
 \int_{\mathcal R}|K_\Delta|\,d\nu
 \ll P_X\lambda^{-4}\log(2+\lambda),
\]

and the derivative has the same capacity, with the \(D^{-2}\) term even
smaller.  The radial logarithm therefore has two spare powers relative to
the target and is uniform despite \(|D|\) becoming \(O(1)\).

In the remaining comparable-height region, \(|\nu|,|y|,|R|\gg\lambda\)
in the relevant combinations, so the contribution is
\(O(P_X\lambda^{-4})\).  For \(|\nu|\gg\lambda\), the constant endpoint
\(p(L)\) leaves a \(P_X\lambda^{-3}|\nu|^{-2}\) tail after the two
denominators; its integral is again \(O(P_X\lambda^{-4})\).  This proves
the first two lines of (41H.7), including uniform height exhaustion.

### Moving traces and affine switches

For the physical section

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U]=[p_{U,V}(L),q_{U,V}(L)],
\]

the exact Leibniz rule is

\[
\begin{aligned}
 {d\over dL}\int_{p_{U,V}(L)}^{q_{U,V}(L)}K\,d\nu
 ={}&\int_{p_{U,V}}^{q_{U,V}}\partial_L^\nu K\,d\nu\\
 &+{\bf1}_{\{q_{U,V}=L+U\}}K(L,L+U)
  -{\bf1}_{\{p_{U,V}=L-U\}}K(L,L-U).             \tag{41H.23}
\end{aligned}
\]

Thus the moving upper physical face has positive sign and the moving
lower face negative sign.  Fixed \(\nu=\pm V\) faces have zero velocity.

To bound either moving trace, fix \(u\ge0\) and put \(y=\pm u\).  Along
the trace,

\[
 |D|\asymp1+|L+\beta-y/2|.                              \tag{41H.24}
\]

There are only three possible large contributions: \(L-y\) can cross the
physical center, \(y=0\) can meet the top diagonal, or
\(L+\beta-y/2\) can meet the radial ridge.  The first occurs with
\(|D|\asymp\lambda\) and contributes
\(P_X\lambda^{-2}\|p\|_1/P_X\).  At the second, the continuous
difference quotient is \(-p'(L)\).  At the third, both profile endpoints
have size \(O(P_X\lambda^{-3})\), so the trace is only
\(O(P_X\lambda^{-4}\log(2+\lambda))\).  These centers cannot coincide
on (41H.9).  Outside them there are two large denominators.  This proves
the last line of (41H.7), uniformly in \(U,V\) and for both signs.

At a max/min switch the two formulas for an endpoint agree, so there is no
jump measure.  If the section collapses, its two endpoint contributions
cancel.  Scaled saddle cutoffs contribute \(O(\lambda^{-1})\) derivatives,
and hard entry/exit restrictions are included exactly as the traces in
(41H.23).

### Smooth translated ridges

For (41H.2), fixed-\(\nu\) differentiation gives

\[
 \partial_L^\nu K_W
 ={G'pW+GpW'\over D}+{iGpW\over2D^2}.                    \tag{41H.25}
\]

The ridge \(W(L-\nu)\) is centered at \(\nu=L\), where
\(|p(\nu)|\ll P_X\lambda^{-3}\) and \(|D|\asymp\lambda\).
At the physical center and radial ridge, \(|L-\nu|\asymp\lambda\), so
(41H.17) supplies arbitrary decay.  Equations (41H.14), (41H.17), and
(41H.18) therefore give

\[
 \sup_L\int(|K_W|+|\partial_L^\nu K_W|)\,d\nu
 \ll P_X\lambda^{-4},                                  \tag{41H.26}
\]

and every moving trace is \(O(P_X\lambda^{-3})\).  These estimates are
uniform across the finite family of normalized smooth shares.  No second
Plemelj subtraction is applied to them.

### Exact Morse remainder, both signs, and entry/exit

Let \(z=\sigma\alpha/\lambda>0\) and use the exact Morse coordinate

\[
 \zeta(z)=\operatorname{sgn}(z-1)
 \sqrt{2(z\log z-z+1)},\qquad \tau=\sqrt\lambda\,\zeta(z).
                                                                    \tag{41H.27}
\]

Then the phase difference is exactly
\(\sigma\tau^2/2\).  After the accepted stationary numerator is
extracted, write the transformed, still varying amplitude as
\(B(\tau,\nu)\).  On every full, truncated, entry, or exit interval the
identity is

\[
 \int e^{i\sigma\tau^2/2}B(\tau,\nu)\,d\tau
 =B(0,\nu)\int e^{i\sigma\tau^2/2}\,d\tau
  +\int e^{i\sigma\tau^2/2}{B(\tau,\nu)-B(0,\nu)\}\,d\tau.          \tag{41H.28}
\]

The second integral is the exact normalized Morse remainder.  The
indefinite Fresnel primitive is uniformly bounded, so Stieltjes
integration by parts bounds it by

\[
 C\{\|B(\cdot,\nu)\|_\infty+\operatorname{Var}_\tau B(\cdot,\nu)\}.
\]

Composition with (41H.27) preserves variation.  Differentiating the
Morse Jacobian adds only \(\lambda^{-1}|K|\).  After integration in
physical height, (41H.7), (41H.23), and (41H.26) therefore bound the
leading term and exact remainder by \(O(P_X\lambda^{-2})\).  Moving
top faces give precisely the traces already audited; fixed radial and
saddle-partition faces are controlled by the value norm.  This also
handles every affine entry/exit switch.

For \(\sigma=+1\) the full Gaussian coefficient has phase
\(e^{i\pi/4}\), and for \(\sigma=-1\) it has phase
\(e^{-i\pi/4}\).  If the saddle is exactly an interval endpoint,
(41H.28) contains exactly one half of the corresponding full Fresnel
integral.  Orientation reversal on the negative saddle is compensated by
the reversed \(\alpha\)-parameter, so no extra minus sign or double star
appears.  This verifies the half-Fresnel seam without replacing
\(B(\tau,\nu)\) by a scalar.

Finally, \(P_X\ll\log^C(2X)\) implies (41H.8) for every fixed
\(\varepsilon>0\).  No estimate in this proof uses the coefficient sum or
the signed diagonal term.

## 4. First doubtful or unproved step

There is no surviving doubtful step inside the frozen off-diagonal and
smooth large-\(\alpha\) product-cell theorem.  The two earlier candidate
failures are explicitly avoided:

1. the physical-height modulation in (41H.4) is retained, rather than
   silently replacing the actual profile by \(f_b\); and
2. the long translation is estimated through \(Q_1\) in (41H.5), rather
   than by separately absolutizing \(F_{Ly}\) and \(F_{yy}\).

The first unproved steps are outside this theorem: composition with the
already owned signed diagonal section must be checked by the conductor's
State Patch, and the bounded-\(\alpha\), double-bounded, and final complete
beta-transition assemblies remain separate obligations.  This report also
does not rederive the accepted arithmetic/radial coefficient sum.

## 5. Required controls and outcomes

1. **Exact one-count product factorization: pass.**  Equations
   (41H.11)--(41H.17) recover the raw authorized cell and distinguish the
   singular off-diagonal product from every smooth ordinary-\(\mu\) share.
2. **Phase and external ownership: pass.**  The \(L\)-phase is removed,
   the physical-height phase is retained in \(p\), and every character,
   real monomial, contour measure, stationary numerator, radial integral,
   floor, star, and external normalization is listed outside the symbol.
3. **Endpoint divided-difference cancellation: pass.**  The exact
   derivative is (41H.6); the long translation uses \(Q_1\), not the
   non-positive mixed-derivative representation.
4. **Four-region height partition: pass.**  Physical center gives the
   target \(P_X\lambda^{-2}\); top diagonal is continuous; the radial
   ridge is \(P_X\lambda^{-4}\log(2+\lambda)\); and far tails are
   absolutely summable.
5. **Moving faces and affine switches: pass.**  The signs in (41H.23) are
   correct, trace integrals are target-safe uniformly in \(U,V\), switches
   create no jump, and collapsed sections vanish.
6. **Both saddles, entry/exit, and exact Morse remainder: pass.**  The
   signed exact coordinate (41H.27) gives the two Fresnel phases, exact
   half coefficients, and the varying-amplitude remainder (41H.28), all
   bounded by the mixed BV norm.
7. **Smooth translated ridges: pass.**  Equation (41H.26) has a spare
   inverse power and no diagonal Cauchy tail.
8. **Beta connectors and common artificial ownership: pass.**  The sole
   beta connector has coefficient \(-\psi'(\beta)\); internal connectors
   and all \(\omega\)-derivative terms cancel under common ownership.
   Already routed connector/axis images are not reinserted.
9. **Polylogarithmic \(b\) and profile derivatives: pass.**  All
   \(b^{-1}\) and height-modulation costs lie in
   \(P_X\ll\log^C(2X)\).
10. **No diagonal or coefficient-sum reopening: pass.**  \(K_C\) and the
    downstream \(h,q,j,x\) summation are not used to prove (41H.7).

## 6. Dependencies and exact artifacts used

This audit used only:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/blind_terminal_symbol_definition.md`;
5. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/reports/translation_difference_hostile_audit.md`;
6. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/synthesis.md`;
7. `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/reports/regular_symbol_hostile_audit.md`.

The Round-41 discovery report and blind report were not read.  No
numerical experiment, computer algebra, or external source was used.

## 7. Recommended state effect

**Promote** the exact phase-removed product-cell factorization
(41H.11)--(41H.17), including the actual modulated height profile
(41H.4), and the cancellation-preserving endpoint derivative
(41H.5)--(41H.6).

**Promote** the singular off-diagonal and smooth direct mixed norm
(41H.7)--(41H.8), with the moving-face signs, uniform height exhaustion,
both saddle signs, entry/exit half-Fresnel normalization, and exact Morse
remainder proved above.  In combination with the already accepted signed
diagonal module, this supplies the missing large-\(\alpha\) hybrid
product-cell input to
`M9-M1-beta-axial-subtracted-terminal-symbol-bound`, subject to the
conductor's independent blind/seam reconciliation.

Do **not** infer the bounded-\(\alpha\), double-bounded, complete beta
transition, M9-M1, M9, or Gauss-circle target from this cell lemma.  Do not
reinsert routed beta connectors or artificial residues, do not put the
signed diagonal kernel under an absolute height norm, and do not invoke
the conditional coefficient sum before the graph accepts this product
cell.
