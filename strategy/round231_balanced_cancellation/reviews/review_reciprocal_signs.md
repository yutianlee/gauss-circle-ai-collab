# 1. Result

Round231 task `review_reciprocal_signs`; nonauthor line review. Generated 2026-10-11T07:35:48Z. The preceding statement-only Hankel report remains frozen and its original isolation is preserved; this separate review uses only the newly authorized context listed in Section 6. No graph or shared-state file was read or modified.

**The reciprocal smooth-rectangle upper estimate passes, with a harmless logarithm endpoint repair. The exact quarter-frequency example passes as a complex-fibre obstruction, but its real leading circle contribution vanishes. A detuned quarter-frequency example does give a real coherent individual fibre. Neither example supplies a lower bound for the full wave or its twelfth moment.**

The adaptive-boundary identity and its quantitative payment pass after the conductor authorized the two predecessor files during this same review cycle. Multiplication by eta preserves the original uniform proper-interval bounded-variation argument for both character placements. The smooth high-norm estimate itself is independently supported by the frozen Hankel derivation.

# 2. Exact statements and hypotheses reviewed

The claimant artifact is `reports/balanced_reciprocal_attack.md`, frozen SHA256 `fa63868418be5c8d24d30284394976fa3e0f1df077117dc3a9227441d55cf61f`. Equation numbers below refer to that artifact unless explicitly introduced here.

The principal upper estimate concerns a smooth real or complex amplitude a(d,m) supported on fixed-ratio positive rectangles d~D, m~M, with D,M>=1/2, DM~N, 1<=N<=T^(3/2), and derivatives bounded by C_jk N^(-3/4)D^(-j)M^(-k). It asserts, for every real T/2<=R<=2T,

\[
 \left|\sum_{d,m\ge1}\chi_4(d)a(d,m)e(R\sqrt{dm})\right|
 \ll_\varepsilon T^\varepsilon
       \left((T/N)^{1/2}+T^{-1/2}\right).
 \tag{R1}
\]

The near-resonance count concerns integer h in a fixed positive interval h~H, where H~RD/sqrt(N), and distances from alpha_h=R^2/(4h) to the two quarter-integer residue classes. Its actual arithmetic hypotheses include the elementary divisor bound for positive integers, in addition to the character identity.

The newly checked real-fibre control is an existential counterexample to a **uniform per-frequency** bound O(A0 D^(1/2+epsilon)) for the actual real stationary contribution, with A0 as in claimant equation (9). It is not a counterexample to (R1), to an estimate after summing h, or to a bound for the physical full moment. Smooth nonnegative rectangle factors may be chosen inside the actual balanced middle range, with the actual norm amplitude positive there.

# 3. Derivation and seam checks

## 3.1. Poisson and stationary phase

With f(v)=R sqrt(dv)-hv, direct calculation gives

\[
 v_h=\frac{R^2d}{4h^2},\quad
 f(v_h)=\frac{R^2d}{4h},\quad
 f''(v_h)=-\frac{2h^3}{R^2d}.
\]

Thus the stationary contribution has the multiplier

\[
 \frac{R\sqrt d}{\sqrt2 h^{3/2}}e(-1/8),
\]

exactly as written. The sign of the curvature is negative. Scaling v=Mu makes the oscillation parameter lambda=R sqrt(N), and the leading size is N^(-3/4)M lambda^(-1/2). The claimed next-order error N^(-3/4)M lambda^(-3/2) is the usual one-dimensional smooth stationary estimate; its stated smooth extension and fixed enlarged h/H interval handle entry and exit of the critical point without a sharp endpoint term. The normalized curvature is bounded away from zero in that interval.

There are O(DH) relevant pairs (d,h). Summing absolute errors gives

\[
 N^{-3/4}DHM\lambda^{-3/2}
   = D R^{-1/2}N^{-1}\ll R^{-1/2}.
\]

Here D/N~1/M is bounded. Also H is at least a constant times T^(1/4), so replacing counts by O(H) introduces no missing small-frequency exception. Outside the stationary interval, the phase derivative is separated from zero by a constant multiple of (lambda+|h|M)/M; repeated integration by parts gives a summable tail. The d-variation estimate for b_h follows because v_h is proportional to d and h~H. **Pass.** No two-dimensional Hessian is used.

## 3.2. Reciprocal near-product count and its summation

The identity chi_4(d)=(e(d/4)-e(-d/4))/(2i) is exact. Applying geometric summation and partial summation to the symbol b_h yields claimant (10).

The resonance condition supplies an integer k with

\[
 |R^2-h(4k-\sigma)|\le C H\delta.
\]

For the specified N range, H/R^2=O(T^(-1/4)). Consequently q=4k-sigma is positive and hq is comparable to R^2 for sufficiently large T; bounded T is absorbed in the constant. There are O(H delta+1) possible positive integers hq, and each admits at most T^epsilon relevant positive divisors h. This proves claimant (11) for every real R, with the +1 paying exact and extremely close resonances. Dyadic distance bands then give H log(2+D)+D, with the logarithm absorbed into T^epsilon. **Count and exponent bookkeeping pass.**

There is one literal endpoint error in claimant (13): `H log(2D)+D` cannot hold as written at D=1/2, since log(2D)=0 while the sum of min(D,||...||^(-1)) over h~H is of order H. The sentence about bounded D does not repair that displayed expression. Replace it by

\[
 \sum_{h\asymp H}\min(D,\|\alpha_h+\sigma/4\|^{-1})
 \ll_\varepsilon T^\varepsilon\{H\log(2+D)+D\}.
 \tag{R2}
\]

Equivalently use H(1+log(2D))+D. This does not change (R1), any exponent, or any downstream conclusion. Finally A0 H~R^(1/2)N^(-1/2) and A0 D~R^(-1/2) check exactly.

## 3.3. Exact quarter frequency: complex and real statements differ

Take L positive with L=1 modulo 4, T=R=L, and h=L. Then alpha_h=L/4 and, for odd d,

\[
 \chi_4(d)e(Ld/4)=i.
\]

For a nonnegative stationary symbol the complex d fibre is therefore i times a positive sum of size A0 D. This correctly refutes a uniform complex-fibre square-root bound.

The actual real circle wave, however, is formed by multiplying the complex sum by e(-3/8) and taking the real part. Stationary phase already contributed e(-1/8), so the combined fixed factor is

\[
 e(-3/8)e(-1/8)=e(-1/2)=-1.
\]

At exact resonance its real leading contribution is consequently

\[
 \Re\left[-i\sum_{d\ {m odd}}b_h(d)\right]=0.
 \tag{R3}
\]

This is not a contradiction to the claimant, whose displayed obstruction explicitly concerns the magnitude of the transformed complex d sum. It does forbid presenting that exact example as a coherent lower bound for an individual **real leading** circle fibre. Subleading stationary errors are not asserted to vanish. This distinction should be added to its scope statement.

## 3.4. Detuning gives a real coherent fibre

Fix any c with 0<c<1/8. For the same integer L and h=L, choose instead

\[
 T=L,\qquad R^2=L^2+\frac{4Lc}{D}.
 \tag{R4}
\]

Then R lies in [T/2,2T] for large T, R-L=2c/D+O(1/(LD^2)), and

\[
 \alpha_h=\frac L4+\frac cD,\qquad
 v_h=\left(\frac14+\frac c{LD}\right)d.
\]

Choose fixed smooth nonnegative rectangle factors supported on D<d<2D, M<m<2M with M=D/4, and positive on a smaller rectangle containing a fixed interior portion of v=d/4. The small displacement in v_h remains inside that interior. Then b_h(d)>=0 throughout its support and b_h(d) is bounded below by a positive constant times A0 on a fixed-length fraction of the d interval.

For each odd d, the actual real stationary summand is

\[
 \Re[-\chi_4(d)b_h(d)e(\alpha_hd)]
   =b_h(d)\sin(2\pi c d/D).
 \tag{R5}
\]

On D<d<2D, its argument lies strictly between 2 pi c and 4 pi c, within (0,pi/2). Hence there is no cancellation of these real leading terms, and

\[
 \Re\left[-\sum_d\chi_4(d)b_h(d)e(\alpha_hd)\right]
       \asymp_c A_0D.
 \tag{R6}
\]

The summed stationary error for this single h is smaller by O(lambda^(-1)), because the leading size is D N^(-3/4)M lambda^(-1/2) and the error is D N^(-3/4)M lambda^(-3/2). Thus the real contribution of this individual Poisson frequency itself has size comparable to A0 D for sufficiently large parameters, not merely its formal leading term.

The conductor's subsequent attachment `conductor_seam_repairs.md`, Sections 2--3, was read during this same review cycle. Its endpoint repair agrees with (R2), and its choice c=1/32 makes the positive sine lower bound exactly sin(pi/16) on [D,2D]. Its stated relative fixed-h error O(H^(-1)) is valid: lambda=HM and M>=1/2 imply lambda^(-1)<=2H^(-1), so the stronger error just computed implies that formulation. Its alternative central scale N~T^(2/3) also lies between X0 and Y and above the adaptive factor threshold. Both localized attachment sections **pass**; no full-moment obstruction follows.

This example can use the actual circle norm amplitude inside the central balanced owner. For instance take D=2T^(3/10), M=D/4, so N=DM=T^(3/5), and use a(d,m)=(dm)^(-3/4)Psi(sqrt(dm/T)) times the fixed nonnegative rectangle factors. On its support Psi tends uniformly to Psi(0)=1. The norm lies strictly between X0=T^(52/125) and Y=T^(99/125) for large T. Moreover

\[
 \frac{\sqrt N}{D_T(N)}
   =T^{533/5250}N^{13/84}\longrightarrow\infty,
\]

and x(n)~n, so both divisor factors are well above the actual adaptive threshold. The amplitude is fixed as R varies; no R-dependent coefficient choice is made.

For any fixed epsilon<1/2, (R6) rules out a uniform bound A0 D^(1/2+epsilon) for every individual **real** reciprocal fibre in this class. It does not establish a matching lower bound for the sum over h, for an entire norm rectangle, for W_lo, or for any moment. In particular it does not show the absolute-frequency upper certificate is sharp in its H term. **Detuned real control passes with this limited scope.**

## 3.5. Smooth tail, adaptive restoration, and moment arithmetic

The factor partitions, the summation of the smooth-block estimate, and the absolute Schwartz tail above Z are compatible with (R1). They prove the smooth full high-tail bound. This is also independently proved, with both real phases and all dual tails, in the frozen Hankel report. **Pass.**

The identity W_hi=B_hi-U_hi-E_hi is algebraically exact since eta kills the head, and u_*+w_*=r_2 on the original interval. It retains the sharp adaptive equality conventions. The moment computation at gamma=13/125 is also correct: 10 gamma=26/25, while 1+20 gamma/13=29/25. Finite L^12 inequalities pay the finite sum of owners without a missing mixed-term estimate. **Identity and exponent arithmetic pass.**

The quantitative bound for U_hi is not a consequence of the bare accepted bound for U_* in the supplied interface. The conductor therefore authorized the two predecessor files during this same review cycle. Their fixed-divisor proof supplies the necessary stronger input, uniform over every proper interval in the ambient m range m~N/d:

\[
 \left|\sum_{m\in I}e(R\sqrt{dm})\right|
 \ll T^\varepsilon\left[
 T^{13/84}N^{97/168}d^{-1/2}+\frac{N^{1/2}}{Td}\right].
 \tag{R7}
\]

For the quotient-character placement, split into m=1 and m=3 modulo 4 with their actual signs. The predecessor grants the same proper-interval estimate for these shifted monomial phases. For the other placement chi_4(d) is constant in the fibre. These are the two actual character placements, with no arbitrary inner sign sequence.

Let g(m) be the original smooth norm amplitude on the shell. The predecessor gives

\[
 \|g\|_\infty+\operatorname{Var}(g)
 \ll_L N^{-3/4}(1+N/T)^{-L}.
\]

For each d,Y, the extra multiplier satisfies

\[
 \|\eta(dm/Y)\|_\infty\le1,\qquad
 \operatorname{Var}_{I}\eta(dm/Y)
 \le\int_1^2|\eta'(t)|\,dt=:V_\eta.
 \tag{R8}
\]

This follows by the change of variable t=dm/Y and is uniform even when the cutoff transition crosses the interval. The product-variation inequality therefore preserves the original amplitude bound, with a fixed factor depending only on V_eta. Restricting to the actual proper interval adds at most two jumps of that same size. An empty interval, singleton, shortened endpoint piece, or cutoff equality causes no extra loss. Restriction to each odd residue class does not increase total variation.

Partial summation with (R7), followed by absolute summation over d<=C D_T(N), now gives exactly

\[
 |U_{\rm hi,N}(R)|\ll T^\varepsilon(1+N/T)^{-L}
 \left[T^{13/84}N^{-29/168}D_T(N)^{1/2}
             +T^{-1}N^{-1/4}\right].
 \tag{R9}
\]

The first divisor sum uses sum d^(-1/2)<<D_T(N)^(1/2); the second contributes only a logarithm from sum d^(-1), absorbed in T^epsilon. Since D_T(N)=T^(-533/5250)N^(29/84), its first term is exactly T^(13/125). Monotonicity of x(n) and D_T makes each original fixed-divisor admissible set a single proper interval, so no number-of-patches factor appears. Summing the shells and the decaying upper tail proves claimant (17). **Quantitative adaptive payment passes relative to the inherited accepted proper-interval input (R7); this review imports no new exponent-pair source and does not invoke a generic masking principle.**

# 4. First doubtful or unproved step

The first literal correction in the smooth-rectangle proof is the D=1/2 logarithm endpoint in claimant (13), repaired by (R2). There is no resulting exponent gap.

The initially unavailable dependency in claimant (17) was resolved by the conductor-authorized predecessor reads and the explicit bounded-variation argument (R7)--(R9). No additional gap remains in that multiplier transfer relative to the inherited proper-interval theorem. The raw bound for U_* alone would not have been sufficient.

For the real-fibre obstruction, the exact-resonance leading real part is zero. Detuning as in (R4) repairs any attempted real-fibre interpretation, but does not repair or prove a global moment lower bound. The genuinely open gain remains cancellation after summing reciprocal frequencies and restoring the actual sharp owner.

# 5. Controls and pass/fail outcomes

| Seam/control | Outcome |
| --- | --- |
| Curvature sign, 1/sqrt(2) amplitude, e(-1/8) shift | Pass by direct differentiation |
| Absolute sum of stationary errors and nonstationary h tail | Pass; total O(R^(-1/2)) |
| Real-R near-product count including exact resonances | Pass; integer products near the real number R^2 are counted |
| D=1/2 in claimant (13) | Fail literally; replace log(2D) by log(2+D) |
| Exact alpha=1/4 complex coherence | Pass, magnitude comparable to A0 D |
| Exact alpha=1/4 real leading coherence | Fails if claimed; the leading real part is exactly zero |
| Detuned alpha=L/4+c/D real coherence | Pass; positive sine in (R5), actual balanced-middle example available |
| Conductor repair attachment Sections 2--3 | Pass, including its O(H^(-1)) relative fixed-h error |
| Smooth high tail and all norm tails | Pass, also independently supported by frozen Hankel report |
| Adaptive ownership identity and moment exponents | Pass |
| Quantitative U_hi boundary payment | Pass after authorized predecessor check and (R7)--(R9) |
| Full-wave/moment lower-bound inference from one h | Rejected; no such inference is valid or needed |

All controls are analytic. No numerical experiment or empirical asymptotic certification is used. The conductor was alerted to the logarithm repair, real-phase distinction, detuned control, and initially missing boundary dependency; after authorizing the predecessor reads, the conductor was informed that (R7)--(R9) close that seam before this report was frozen.

# 6. Dependencies and exact artifacts used

New context read for this review:

- `strategy/round231_balanced_cancellation/briefs/review_reciprocal_signs.md`: `0ce70910b38d66cff79d90aaca2afc4343eec96ba221fe4d11b0f3d1bf0defb2`.
- `strategy/round231_balanced_cancellation/reports/balanced_reciprocal_attack.md`: `fa63868418be5c8d24d30284394976fa3e0f1df077117dc3a9227441d55cf61f`.
- `strategy/round231_balanced_cancellation/briefs/balanced_interface.md`: `cb6f283b2de16774ff946c450acabd61001b39c39ba58c6e2ab719c14050e055`.

Previously completed isolated assignment context retained:

- `protocol.md`: `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `strategy/round231_balanced_cancellation/briefs/blind_hankel_tail.md`: `2ddfd24dce000b9df886cc80a97d9a0642bae04bad621d342be627a234b8a25c`.
- `strategy/round231_balanced_cancellation/briefs/isolated_hankel_statement.md`: `94bc32e3dd2e4e0f060b1385388ebe5cc12932263f9e75f308cb401772f1bc2a`.
- Frozen independent output `strategy/round231_balanced_cancellation/reports/blind_hankel_tail.md`: `03b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5`.

Additional predecessor context expressly authorized by the conductor during this review:

- `strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md`: `02727c91e64931a13d3707ca15df021418d3e96510e35894e0d96a70182506fa`. Its text was displayed; the dependency used here is its Section 3 monotone proper-interval and adaptive-cutoff calculation.
- `strategy/round231_residual_saving/reports/actual_residual_attack.md`: `0d18fa59d915809427e1758ee478ba439303748738e8ec1f86d7e95060dd0bc5`. A bounded text search located the relevant material, then Section 3.1 was read. Only its fixed-divisor proper-interval estimate, amplitude variation, and two character placements are mathematical dependencies here.
- `strategy/round231_balanced_cancellation/conductor_seam_repairs.md`: `e4dc22c726eb241e24a4e7c485202ea6b6b567ecc4e16a3708d435ddc82eab14`. Only authorized Sections 2--3 were read and checked; Sections 4--6 were not read.

No linked Round205/208 section, graph, active campaign, or additional sibling artifact was read. No new external source was imported for this review. The predecessor treats its proper-interval exponent-pair theorem as already accepted; this review checks the eta insertion and summation, not a new audit of that theorem's external source. The source citations already recorded in the frozen Hankel report support only that report's Bessel identities.

# 7. Recommended state effect

Retain the reciprocal rectangle estimate and the no-complete-gain conclusion, subject to the local logarithm correction. Clarify that the exact quarter-frequency example obstructs a complex-fibre estimate only; retain (R4)--(R6) as the separate analytic control showing that detuned real individual fibres can also be coherent.

Do not infer any full moment lower bound or newly improved exponent. The adaptive quantitative seam may be marked passed by this review relative to its inherited accepted proper-interval theorem: (R7)--(R9) supply the missing explicit multiplier argument. No graph, proof draft, validation matrix, synthesis, or frozen claimant report is changed here, and no successor round is initiated.
