# Round 40 hostile audit: translation divided difference

## 1. Result

The corrected coordinate identity is exact, but the absolute mixed norm in
the Round-39 formulation is false even for the already separated actual
hard-top (R_1) kernel.  Put (y=L-\nu) and
(F(L,y)=H(L,L-y)).  At fixed physical height,

\[
 \partial_L^{\nu}H=F_L+F_y,
 \qquad (\partial_L+\partial_\nu)H(L,L)=F_L(L,0),
\]

and hence

\[
 \boxed{
 \mathfrak E_H(L,\nu)
 =\int_0^1F_{Ly}(L,ty)\,dt
  +\int_0^1tF_{yy}(L,ty)\,dt .}
 \tag{40H.1}
\]

There is no extra (F_y(L,0)/y) term.  In particular the diagonal limit is

\[
 \mathfrak E_H(L,L)=F_{Ly}(L,0)+\frac12F_{yy}(L,0).
 \tag{40H.2}
\]

However, the other term in the exact singular regularizer,

\[
 K_C(L,\nu)=-\frac{iH(L,L)}{2A(L)D(L,\nu)},
 \tag{40H.3}
\]

has a genuine (1/\nu) tail.  For the actual separated kernel one may take
(H(L,\nu)=f_b(\nu)), and then (40H.3) is exactly the first term of the
accepted displayed (K_{R_1}).  Whenever (f_b(L)\ne0),

\[
 \int_{\mathbb R}|K_C(L,\nu)|\,d\nu=\infty .
 \tag{40H.4}
\]

Generically the corresponding fixed-(\nu) derivative also has a
logarithmically divergent absolute height norm.  Thus neither the singular
regularizer nor its pointwise Morse leading term can be put in the absolute
height norm asserted in Round 39.

This is a splitting obstruction, not a divergence of the finite contour
operator.  On every finite physical section (K_C) has an exact signed
Cauchy primitive.  On both signed saddle cells that primitive has
supremum plus variation

\[
 O_b\!\left(\lambda^{-4}\log(2+\lambda)\right),
 \tag{40H.5}
\]

for the actual cubic-decay hard-top profile, and is therefore much smaller
than the required (X^\varepsilon\lambda^{-2}) scale.  It must be formed
before stationary/Morse localization.  The lawful interface is consequently
hybrid: a signed finite-section norm for the diagonal Cauchy primitive,
and an absolute mixed physical-height norm only for the off-diagonal
divided difference and the smooth ordinary-(\mu) shares.

There is a second hostile warning.  Formula (40H.1) is not a positive
representation.  Taking absolute values of (F_{Ly}) and (F_{yy})
separately loses powers of (\lambda) on a long translation segment.  For
the actual (H=f_b(\nu)) and (y=2L\), the termwise derivative ledger has
size (\gg_b\lambda^{-1}), while the recombined exact divided difference
is (O_b(\lambda^{-5})).  Therefore (40H.1) must be used with its signed
recombination intact; it does not by itself prove the requested mixed norm.

The diagonal signed part is certified.  The complete off-diagonal actual
gamma/profile/connector and Morse bound is not certified by the authorized
artifacts, so the quantitative target remains open after being revised.

## 2. Exact statement and hypotheses

Work on the legal terminal line (c'=5/4), with bounded beta,
(b=1/\log(2X)>0), and one frozen signed cell
((j,h,q,x,\beta,\pm)).  Put

\[
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
 A(L)=-1-\frac b2-i(L+\beta),\qquad
 D(L,\nu)=A(L)+\frac i2(L-\nu).
 \tag{40H.6}
\]

The terminal line has (\Re D=-1-b/2), so (D) never vanishes there.
The crossed artificial residue is a different owned stratum.  The full
stationary phase, (\chi_4(q)), the stationary numerator
((D_j/q)\lambda), the real (h,D_j,x) monomial, radial integration,
floors, stars, and the external (X^{1/4}) normalization stay outside the
pre-numerator kernel.  The two contour measures left after the top
distribution contribute ((2\pi)^{-2}); this fixed factor is also outside
the formulas below and cannot cure an absolute divergence.

For the singular (u^{-1}) hard-top share only, write

\[
 \mathcal R_A[H]
 =K_C+K_\Delta,
 \qquad
 K_\Delta(L,\nu)
 =\frac{H(L,\nu)-H(L,L)}{(L-\nu)D(L,\nu)}.
 \tag{40H.7}
\]

Smooth top remainders and every interior (\widehat W_j) share retain their
ordinary (\mu)-integration; they are not subjected to (40H.7).

For finite heights define

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U]=[p(L),q(L)],
 \tag{40H.8}
\]

where

\[
 p(L)=\max(-V,L-U),\qquad q(L)=\min(V,L+U).
\]

Equivalently, in (\mu=L-\nu),

\[
 [a(L),d(L)]
 =[\max(-U,L-V),\min(U,L+V)].
 \tag{40H.9}
\]

The letter (d) is used for the upper section endpoint here to avoid
confusing it with the denominator (D(L,\nu)).  Let
(\Log_{\mathrm L}) denote a continuous logarithm on the open left
half-plane, chosen consistently along the vertical line
(A+i\mathbb R/2).

The corrected sufficient hybrid target is of the form

\[
\begin{aligned}
 \mathfrak M^{\rm hyb}_\lambda(H):={}&
 \|C_{U,V}[H]\|_{L^\infty(I_\lambda)}
 +\operatorname{Var}_{I_\lambda}C_{U,V}[H]
 +\mathfrak R^{\rm Morse}_\lambda(C_{U,V}[H])\\
 &+\mathfrak M^{\rm abs}_\lambda(K_\Delta)
 +\sum_{\rm smooth}\mathfrak M^{\rm abs}_\lambda(K_{\rm sm}),
 \tag{40H.10}
\end{aligned}
\]

where

\[
 C_{U,V}[H](L)=\int_{I_{U,V}(L)}K_C(L,\nu)\,d\nu
 \tag{40H.11}
\]

is a signed integral, and (\mathfrak M^{\rm abs}) is the Round-39 mixed
value/derivative/moving-trace norm.  The diagonal part of (40H.10) must
retain the same face-log, delta, star, and collision ownership as the
finite Plemelj decomposition.  The claim audited here is not that all of
(40H.10) has been proved, but that (40H.10), unlike the all-absolute norm,
is correctly typed.

## 3. Proof or derivation

### Coordinate identity and its non-positive character

Since (H(L,\nu)=F(L,L-\nu)), differentiating at fixed (\nu) gives
(\partial_L^\nu H=F_L+F_y).  Along the diagonal,

\[
 \frac d{dL}H(L,L)=(\partial_L+\partial_\nu)H(L,L)=F_L(L,0).
\]

Therefore

\[
\begin{aligned}
 \mathfrak E_H
 &={F_L(L,y)-F_L(L,0)+F_y(L,y)\over y}
   -{F(L,y)-F(L,0)\over y^2}\\
 &=\int_0^1F_{Ly}(L,ty)\,dt
   +{F_y(L,y)-\int_0^1F_y(L,ty)\,dt\over y}.
\end{aligned}
\]

Fubini on the last numerator gives

\[
 {1\over y}\int_0^1\{F_y(L,y)-F_y(L,ty)\}\,dt
 =\int_0^1tF_{yy}(L,ty)\,dt,
\]

which proves (40H.1)--(40H.2).

For the exact separated hard-top numerator (H(L,\nu)=f_b(\nu)),

\[
 F_{Ly}(L,y)=-f_b''(L-y),\qquad
 F_{yy}(L,y)=f_b''(L-y),
\]

and hence

\[
 \mathfrak E_{f_b}
 =-\int_0^1(1-t)f_b''(L-ty)\,dt
 =-{f_b'(L)\over y}-{f_b(L-y)-f_b(L)\over y^2}.
 \tag{40H.12}
\]

This gives an actual-factor falsifier for a termwise absolute proof.  Take
(y=2L), (|L|\asymp\lambda\), and a compact interval (E) on which
(f_b'') is not identically zero.  Changing variables
(z=L-2Lt) shows

\[
 \int_0^1(1-t)|f_b''(L-2Lt)|\,dt
 ={1\over4L^2}\int_{-L}^{L}(L+z)|f_b''(z)|\,dz
 \gg_b \lambda^{-1}.
 \tag{40H.13}
\]

By contrast, cubic profile decay and its differentiated form give from the
right side of (40H.12)

\[
 |\mathfrak E_{f_b}(L,-L)|\ll_b\lambda^{-5}.
 \tag{40H.14}
\]

Thus the cancellation between the two mixed derivatives in (40H.1) saves
four pointwise powers on this translated ridge.  If the axial polar part is
left in (f_b), (40H.13) also carries the expected polynomial (b^{-1})
loss; with (b^{-1}\asymp\log X) that loss is polylogarithmic but the lost
power of (\lambda) remains.  The same calculation with a phase-removed
gamma multiplier (g(L)) reads

\[
 \mathfrak E_{g f_b}
 =-g'(L)\int_0^1f_b'(L-ty)\,dt
  -g(L)\int_0^1(1-t)f_b''(L-ty)\,dt,
 \tag{40H.15}
\]

so the two integrals must again be evaluated or recombined before absolute
values.  Formula (40H.1) is an exact cancellation identity, not an
absolute mixed-derivative majorant.

### Exact diagonal obstruction

For (|\nu|\to\infty) with (L) fixed, (y=L-\nu) and
(D=i y/2+O_L(1)).  Consequently

\[
 K_C(L,\nu)
 =-{H(L,L)\over A(L)(L-\nu)}+O_L(|\nu|^{-2}).
 \tag{40H.16}
\]

The second term of (40H.7) is (O_L(|\nu|^{-2})) when the actual physical
profile decays, so it does not cancel (40H.16).  In particular the exact
accepted separated formula

\[
 K_{R_1}(L,\nu)
 =-\frac{i f_b(L)}{2A\{A+i(L-\nu)/2\}}
  +\frac{f_b(\nu)-f_b(L)}{(L-\nu)\{A+i(L-\nu)/2\}}
 \tag{40H.17}
\]

violates any pointwise majorization by an (L^1(d\nu)) weight whenever
(f_b(L)\ne0).  The actual profile is nonconstant and analytic, so such
points occur in every nontrivial range; the continuum radial variable lets
the saddle pass through them.  More precisely,

\[
 \int_{|\nu|\le T}|K_C(L,\nu)|\,d\nu
 ={2|H(L,L)|\over|A(L)|}\log T+O_L(1).
 \tag{40H.18}
\]

Writing (c(L)=-H(L,L)/A(L)), fixed-(\nu) differentiation of
(c(L)/(L-\nu)) also gives (c'(L)/(L-\nu)+O(\nu^{-2})).  Unless
(c'\) vanishes identically, the derivative height norm diverges in the
same way.  This agrees with the first two (1/D) terms in the exact
derivative of (\mathcal R_A[H]).

The source of the tail is transparent from

\[
 {1\over yD}={1\over Ay}-{i\over2AD}.
 \tag{40H.19}
\]

The explicit constant-numerator face log and (K_C) have opposite
(1/y) tails; their unsplit sum is (O(y^{-2})).  Removing the face-log
operator and then demanding an absolute height norm of (K_C) destroys
that cancellation.  The face log may still be estimated separately near
a saddle-face collision, but its exact Cauchy primitive must remain paired
with (40H.3) through height exhaustion.

### Signed primitive, variation, and moving-face signs

In the (\mu)-section (40H.9), direct integration gives

\[
 \boxed{
 C_{U,V}[H](L)
 =-{H(L,L)\over A(L)}
 \left\{\Log_{\mathrm L}\!\left(A+{i d(L)\over2}\right)
       -\Log_{\mathrm L}\!\left(A+{i a(L)\over2}\right)\right\}.}
 \tag{40H.20}
\]

No absolute integration was used.  Along the prescribed symmetric
exhaustion (U=V=T), the logarithmic difference has a finite limit of
(-i\pi) (with the stated left-half-plane branch).  Thus

\[
 C_{T,T}[H](L)\longrightarrow {i\pi H(L,L)\over A(L)}.
 \tag{40H.21}
\]

On either saddle (L=\pm\lambda+O(1)), the actual profile gives

\[
 |H(L,L)|\ll_b\lambda^{-3},\qquad
 \left|{d\over dL}H(L,L)\right|\ll_b\lambda^{-4},qquad
 |A(L)|\asymp\lambda,
 \tag{40H.22}
\]

after the full stationary phase is removed.  Section geometry implies

\[
 \left|\Log_{\mathrm L}(A+i d/2)
       -\Log_{\mathrm L}(A+i a/2)\right|
 \ll_b\log(2+\lambda)
 \tag{40H.23}
\]

uniformly in the symmetric section.  On each affine face cell, the
derivative of either logarithm is a bounded numerator divided by a
left-half-plane affine function.  Its (L^1) norm on an
(O(\lambda)) saddle/entry/exit cell is (O_b(\log(2+\lambda))).
Equations (40H.20)--(40H.23) prove (40H.5), for both signs and including
entry/exit.

The exact physical-height Leibniz signs are

\[
\begin{aligned}
 {d\over dL}C_{U,V}[H](L)
 ={}&\int_{p(L)}^{q(L)}\partial_L^\nu K_C(L,\nu)\,d\nu\\
 &+\mathbf1_{\{q=L+U\}}K_C(L,L+U)
  -\mathbf1_{\{p=L-U\}}K_C(L,L-U).
 \tag{40H.24}
\end{aligned}
\]

Thus the moving upper physical face has plus sign and the moving lower
physical face has minus sign.  In (\mu)-coordinates the equivalent
formula is

\[
 {dC\over dL}=\int_a^d\partial_L^\mu\widetilde K_C\,d\mu
 +\mathbf1_{\{d=L+V\}}\widetilde K_C(L,d)
 -\mathbf1_{\{a=L-V\}}\widetilde K_C(L,a).
 \tag{40H.25}
\]

For (U=V=T), (L>0) has the moving lower physical face and contributes
(-K_C(L,L-T)); (L<0) has the moving upper physical face and contributes
(+K_C(L,L+T)).  Affine switches create no jump because the endpoint
values agree, and section collapse contributes zero.  These signs are
required for (40H.20); taking their absolute values before the primitive
recreates the false logarithmic tail.

### Gamma, profiles, connectors, and Morse seam

After complete phase removal, the signed gamma symbol on
(|L+\beta|\asymp\lambda) has the same relative
(O(\lambda^{-k})) derivative capacity for the positive and negative
saddles.  The physical profile contributes (f_b(L-y)); its first and
second (y)-derivatives may cost powers of (b^{-1}), hence only powers of
(\log X), but (40H.13) shows that they must not be absolutized along a
long translation.  Interior (\widehat W_j(a+iy)) factors and the smooth
top remainder remain ordinary (\mu)-shares.  Their translated ridge can
cost one harmonic logarithm, as in Round 39, but it has no diagonal Cauchy
tail.  Beta masks and connector coefficients are bounded on compact
support.  All (\omega') and higher ownership terms cancel only in the
common (G-E_1-R_1=0) combination; estimating one such term is not a valid
factor ledger.  The terminal (D)-ridge has no pole because
(\Re D<0), and when (|D|=O(1)) it lies at
(\nu=-L+O(1)), where the actual height profile supplies cubic decay.

These capacities expose no new power loss after signed recombination, but
the authorized artifacts do not write one complete phase-removed numerator
for every singular, smooth, connector, and moving-face stratum.  Therefore
they do not prove the off-diagonal part of (40H.10).

In particular, an asserted exact factorization
\(H^\circ(L,\nu)=G^\circ(L)p_b(\nu)\) has only a narrow scope.  It is
available for the separated singular hard-top numerator after the radial
\(x\)-phase and every declared external factor have genuinely been taken
outside.  It is not an exact factorization of the complete terminal
package: a smooth share contains
\(\widehat W_j(a+i(L-\nu))\), and the radial, connector-axis, and moving
restriction strata must first be shown to have the same ownership and
phase removal.  The graph records no formula performing that operation.
Even in the narrow factorized singular share, (40H.18) refutes the
all-absolute norm and (40H.13) refutes a termwise mixed-derivative proof.

Likewise, (40H.20) does justify a uniform finite-section logarithm estimate
for the *signed diagonal operator* on the common affine boxes: section
geometry bounds the ratio of the two endpoint denominators by
\(O_b(1+\lambda)\), and (40H.24)--(40H.25) give its variation.  It does
not justify a uniform absolute \(L^1_\nu\) bound for \(K_C\), a mixed norm
for \(K_\Delta\), or the pointwise-in-\(\nu\) exact Morse remainder.

Finally, Morse localization does not repair (40H.4).  Pointwise in (\nu),
the leading saddle value of (K_C) is (c(L_\pm)/\nu+O(\nu^{-2})).  In the
exact normalized varying-amplitude remainder,

\[
 \lambda^{-1/2}\int e^{\pm i\tau^2/2}
 \{K_C(L(\tau),\nu)J_\pm(\tau)
   -K_C(L_\pm,\nu)\sqrt\lambda\}\,d\tau,
 \tag{40H.26}
\]

the coefficient of (1/\nu) is generically nonzero.  Hence both the
pointwise leading term and (40H.26) fail an absolute (L^1_\nu) test.
The lawful order is first (40H.20), then the accepted incomplete-Fresnel
leading term plus exact Morse remainder applied to the signed section
amplitude (C_{U,V}[H](L)).  Its bound (40H.5) is stable through full,
half-, entry-, and exit-Fresnel cells.  Compact beta connectors merely
multiply this estimate; common artificial ownership remains separate.

## 4. First doubtful or unproved step

The first false step is earlier than a difficult mixed-derivative estimate:
it is the placement of the diagonal term (K_C) inside an absolute
(L^1(d\nu)) mixed norm.  Equations (40H.16)--(40H.18) are an exact
actual-profile counterexample.  This also invalidates the factorized
integrable-weight assertion currently attached to the separated
(K_{R_1}) kernel, although its finite-section supremum/BV conclusion can
be recovered by the signed primitive (40H.20).

After revising the type, the first analytic gap is the hybrid
off-diagonal bound.  Formula (40H.1) is exact, but a proof that separately
majorizes all (F_{Ly}) and (F_{yy}) product-rule terms is invalid by
(40H.13)--(40H.15).  The full phase-removed gamma/radial/profile numerator
must be recombined first, the long-translation derivatives evaluated as
endpoint divided differences, and only then may absolute physical-height
bounds be taken.  The same recombination has to persist through beta
connectors, moving traces, and the exact Morse remainder.

No authorized artifact supplies that complete recombined formula and its
hybrid norm.  Thus neither the complete terminal-symbol obligation nor the
large-alpha beta package is proved in this round.

## 5. Required control tests and outcomes

1. **Coordinate conversion:** pass.  Fixed physical height gives
   (\partial_L^\nu H=F_L+F_y) and proves (40H.1).  Both provisional
   formulas with an extra diagonal term are false.
2. **Diagonal:** fail for the all-absolute norm.  The exact separated
   (R_1) factor has the logarithmic divergence (40H.18).  Pass for the
   signed primitive (40H.20)--(40H.21).
3. **Termwise mixed derivatives:** fail.  The actual profile control
   (40H.13) loses four pointwise powers against the recombined endpoint
   expression (40H.14).  The identity must remain signed.
4. **Two saddles and entry/exit:** pass for the diagonal primitive.  Since
   (|A|\asymp\lambda) and the diagonal profile is cubic on both signs,
   (40H.5) holds through full and half Fresnel cells.  The complete
   off-diagonal Morse norm remains open.
5. **Moving faces:** pass only with the signs (40H.24)--(40H.25).  Upper
   moving physical faces are positive and lower moving faces negative.
   Absolutizing before forming the primitive fails.
6. **Beta connectors and common ownership:** no new diagonal loss.
   Compact mask derivatives are bounded, and common
   (G-E_1-R_1=0) ownership removes cutoff derivatives.  A stratumwise
   complete off-diagonal estimate is not present.
7. **Artificial and axial seams:** terminal (D) is separated in real
   part; the crossed artificial residue remains separately owned.  Axial
   profile derivatives cost at most polylogarithmic powers for the actual
   (b), but their termwise translation norm is not a valid estimate.
8. **Contour and external factors:** pass.  The remaining
   ((2\pi)^{-2}), stationary numerator, character, coefficient monomial,
   radial integration, and external (X^{1/4}) stay outside.  None changes
   the (1/\nu) type obstruction.
9. **Morse remainder:** fail if applied pointwise to (K_C), by
   (40H.26).  Pass in scope after the signed finite section is formed;
   (40H.5) then supplies a safe BV amplitude.
10. **Closed coefficient sum:** not repeated and not used to assume the
    missing norm.

## 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`,
`rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/reports/terminal_symbol_hostile_audit.md`,
`rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/synthesis.md`,
`rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/reports/regular_symbol_hostile_audit.md`,
`rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reports/complete_kernel_hostile_audit.md`, and
`rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/cauchy_tail_hostile_audit.md`.
No Round-40 claimant report, numerical experiment, web source, or unlisted
project artifact was used.  The audit is entirely analytic.

## 7. Recommended state effect

**Revise; do not promote the complete target.**  Promote only the exact
coordinate identity (40H.1), the exact signed diagonal primitive
(40H.20) with its moving-face signs and saddle bound (40H.5), and the
actual-form no-go results (40H.18) and (40H.13).

Revise `M9-M1-beta-axial-subtracted-terminal-symbol-bound` to the hybrid
operator norm (40H.10).  Revise the separated-(R_1) node: its claimed
pointwise domination by an integrable physical-height weight is false, but
its finite-section sup/BV and local (q^{-2}) conclusion may be retained
after replacing that proof by the signed (K_C) primitive plus an absolute
off-diagonal estimate.  Keep the explicit constant-numerator face log and
(K_C) under common finite-section ownership through height exhaustion.

Do not apply the exact Morse operator pointwise in physical height to
(K_C), and do not bound the two integrals in (40H.1) separately.  The
next viable attack is to form the signed diagonal section first and to
prove the remaining off-diagonal/smooth mixed norm from endpoint divided
differences of the complete phase-removed actual product.  No change to
the bounded-alpha share, double-bounded share, complete beta transition,
M9-M1, M9, or the Gauss-circle target is licensed.
