# Round 203: independent density and complete-remainder seam review

## 1. Result

**Scoped GREEN. No correction required in the reviewed density/remainder algebra, endpoint convention, derivative powers, mixed-term estimates, tail accounting, lower-quadratic control, or target equivalences.** This verdict is conditional wherever the report invokes inherited analytic inputs. It does not validate those inputs' sources, upgrade their candidate status, or prove the proposed target exponent.

Reviewed artifact: `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/actual_density_remainder_attack.md`.

Exact reviewed SHA-256, independently checked before reading:

`09136945693d920615e84dbb1b4223419e1b9896660e1446a37cdbcd169f538c`.

Campaign: `gc-complete-signed-convolution-attack`; round 203; role: bounded independent line/seam audit after completion of the statement-only phase; generated: 2026-09-23 13:21:02 UTC. The reviewed report prints starting graph hash `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`; this review did not inspect or verify the graph. No experiment was performed, and no original report or shared state was edited.

## 2. Exact statement, hypotheses, and scope

Use the reviewed report's definitions of (T\ge2), (U=\lfloor T^{1/2047}\rfloor), the finite complex measure (\mu), its inverse transform (B), the fixed real even Schwartz function (\Psi), the nonzero displaced window (\chi), (w=\chi^2), and (K_T=T\widehat\chi(T\cdot)). Define the continuous area measure (\lambda), the remainder (\eta=\mu-\lambda), and inverse transforms (G,E), so (B=G+E).

The review takes the report's summatory hypothesis (A(x)=\pi x+Q(x)), (Q(x)\ll_\kappa x^{\theta+\kappa}), with the printed (1/4<\theta<1/2), as an input. Its claimed graph/source provenance is outside this review. The coefficient divisor estimate is also an explicitly stated input. Where used, the physical supremum with (\beta=2\theta-1/2), the (q_0=262/27) moment bound, their smoothing interfaces, and the safe-head moment are **conditional inherited inputs**. This review does not treat them as newly accepted theorems.

The tail (L^2) estimate is not needed as an unexamined black box here: its proof in reviewed equation (17) is checked below from the displayed coefficients, Schwartz decay, and the elementary coefficient bound. No stronger arithmetic estimate is assumed.

The audited conclusions are the exact subtraction and Stieltjes formulas, all filtered sixth-power errors, the quadratic lower control, and equivalence of the three target formulations for (\mu^{*6}), (\eta^{*6}), and the phase-derivative integral (J). All references to equation numbers below refer to the reviewed artifact.

## 3. Independent derivation and line audit

### Density normalization and phases: equations (1), (7), (12)

The positive branch initially has amplitude (\tfrac12\pi x^{-3/4}\Psi(\sqrt{x/T})\,dx). Under (x=y^2), (dx=2y\,dy), this becomes (\pi y^{-1/2}\Psi(y/\sqrt T)\,dy), with phase (e(-3/8)). The negative branch has the same positive density in (|y|) and phase (e(3/8)). Thus equation (1) has the correct factor (\pi), both phases, and strict cutoff (|y|>\sqrt U).

The inverse transforms of the paired branches add to twice their real part. Consequently

\[
G(R)=\pi\int_U^\infty x^{-3/4}\Psi(\sqrt{x/T})
\cos(2\pi R\sqrt x-3\pi/4)\,dx
=2\pi\int_{\sqrt U}^\infty y^{-1/2}\Psi(y/\sqrt T)
\cos(2\pi Ry-3\pi/4)\,dy.
\]

Both equalities in (12) are correct. For (b(y)=y^{-1/2}\Psi(y/\sqrt T)), the endpoint and derivative integral are (O(U^{-1/4})). Integration by parts includes the lower endpoint and gives (G(R)=O(|R|^{-1}U^{-1/4})). On (R\asymp T), this yields

\[
\|\chi G^6\|_2\ll T^{1/2}(T^{-1}U^{-1/4})^6
=T^{-11/2}U^{-3/2}.
\]

Thus both powers in (2) pass.

### Inclusive Stieltjes endpoint and restored derivatives: equations (13)-(16)

Because (A(x)) includes the jump at (x=U), whereas the tail sum excludes that jump, the correct Stieltjes domain is ((U,\infty)), and integration by parts uses the right-continuous value (Q(U)). For (H=F_T\cos\phi_R),

\[
\int_{(U,\infty)}H\,dQ=-Q(U)H(U)-\int_U^\infty Q(x)H'(x)\,dx.
\]

Replacing (Q(U)) by (Q(U^-)) would incorrectly retain the excluded atom. The report uses (Q(U)), correctly. Schwartz decay removes the upper boundary.

The derivatives are

\[
F_T'=-\tfrac34x^{-7/4}\Psi(\sqrt{x/T})
+\frac1{2\sqrt T}x^{-5/4}\Psi'(\sqrt{x/T}),
\qquad \phi_R'=\pi Rx^{-1/2}.
\]

Hence (-\int QH') has the reported positive phase term

\[
+\pi R\int_U^\infty Q(x)x^{-5/4}\Psi(\sqrt{x/T})\sin\phi_R(x)\,dx.
\]

There is no missing factor two, no sign error, and no missing (R). For (0<\kappa<3/4-\theta), the endpoint and first amplitude derivative are (O(U^{\theta-3/4+\kappa})). Substituting (x=Tz^2) into the second amplitude derivative gives

\[
O\!\left(T^{\theta-3/4+\kappa}
\int_{\sqrt{U/T}}^\infty z^{2\theta-3/2+2\kappa}|\Psi'(z)|\,dz\right)
=O(T^{\theta-3/4+\kappa}).
\]

The integral is bounded; evenness also supplies (\Psi'(z)=O(z)) near zero. Since the exponent of (T) is negative and (U\le T), this is bounded by the asserted (U)-power. The same substitution in the phase derivative gives (O(|R|T^{\theta-1/4+\kappa})=O(T^{\theta+3/4+\kappa})). Equations (13)-(16) therefore pass, including the interpretation that the last absolute estimate is ineffective.

### Tail second moment: equation (17)

For real coefficients, the cosine-product formula gives the difference-frequency diagonal

\[
\frac T2\widehat w(0)\sum_{n>U}a_n(T)^2.
\]

At (n\le V=T^{1+\alpha}), (0<\alpha<1), nonzero difference frequencies satisfy

\[
T|\sqrt m-\sqrt n|\ge\tfrac12T^{(1-\alpha)/2}|m-n|.
\]

Thus the off-diagonal absolute row sum is at most (C_NT^{-N(1-\alpha)/2}\) for any chosen (N>1). Using (2|a_ma_n|\le a_m^2+a_n^2) bounds the entire difference off-diagonal. Sum frequencies are bounded away from zero, and their contributions are likewise arbitrarily small after allowing polynomial coefficient variation. The restoration of (n>V), checked separately below, is also arbitrarily small. Consequently the (O_K(T^{-K})) error in (17) is justified for each fixed (K), without any unproved cancellation between coefficients.

The divisor estimate gives the diagonal upper bound (\sum_{n>U}a_n^2\ll_\varepsilon T^\varepsilon U^{-1/2}). Adding the much smaller weighted (L^2) norm of (G) then proves (18) for (E). These checks also establish that the main-term coefficient in (17) is (T/2), as required for the lower control.

### Every density/remainder stratum: equations (19)-(23)

The convolution-binomial identity and Plancherel give all seven terms exactly:

\[
\|K_T*(\lambda^{*(6-j)}*\eta^{*j})\|_2
=\|\chi G^{6-j}E^j\|_2,\qquad 0\le j\le6.
\]

For (1\le j\le5), taking (6-j) density factors and (j-1) remainder factors in the supremum, and one remainder in weighted (L^2), gives precisely

\[
T^{1/2-(6-j)+(j-1)\beta+\varepsilon}U^{-(7-j)/4}.
\]

For clarity, all seven strata have the following costs under the stated inputs; the fixed binomial coefficients do not affect the powers.

| (j) | Bound before optional (q_0) improvement |
|---|---|
| 0 | (T^{-11/2}U^{-3/2}) |
| 1 | (T^{-9/2+\varepsilon}U^{-3/2}) |
| 2 | (T^{-7/2+\beta+\varepsilon}U^{-5/4}) |
| 3 | (T^{-5/2+2\beta+\varepsilon}U^{-1}) |
| 4 | (T^{-3/2+3\beta+\varepsilon}U^{-3/4}) |
| 5 | (T^{-1/2+4\beta+\varepsilon}U^{-1/2}) |
| 6 | (T^{1/2+5\beta+\varepsilon}U^{-1/4}) |

The (j=5) row dominates (j\le5); (j=6) is the pure remainder and is explicitly retained. Equation (3) follows.

For the optional interpolation, set (q=q_0) and (a=(q-2j)/(q-2)). When (1\le j\le4), Hölder gives

\[
\int w|E|^{2j}\le
\left(\int w|E|^2\right)^a
\left(\int w|E|^q\right)^{1-a}.
\]

This produces exactly the additional cutoff power (-(q-2j)/(4(q-2))) in (21). For (j=5), (10>q), and using the supremum only for the excess power (10-q) gives (22). Since (10-q_0=8/27), its exponent is exactly (-1/2+(4/27)\beta). The (j=6) analogue uses (12-q_0=62/27), yielding the conditional norm exponent (1/2+(31/27)\beta) in (5). The corresponding norm gap is exactly ((31/27)\beta-2/25). All displayed decimal powers are consistent with these exact formulas.

The argument accounts for every sixth-power mixed term. It estimates their sum in (L^2), so no unproved orthogonality or discarded cross inner product is involved.

### All upper tails and head cross terms: equations (24)-(26)

Schwartz decay and the divisor bound give

\[
\|\mu_{n>V}\|_{\rm TV}+\|\lambda_{|y|>\sqrt V}\|_{\rm TV}
\ll T^{M/2}V^{1/4+\kappa-M/2}
\]

for sufficiently large chosen decay order (M); smaller indicated orders also follow by increasing the Schwartz order. With (V\asymp T^{1+\alpha}), (M) can make the tail (O(T^{-K})) for any fixed (K). Floors and bounded values of (T) affect only constants.

Each sixth-product difference contains at least one such tail and at most five full factors of variation (O(T^{1/4+\kappa})). Since (\|K_T\|_2=T^{1/2}\|\chi\|_2), the cost is (T^{7/4+5\kappa-K}), exactly (25). For each twelfth-product integral there are at most eleven full factors and a window of mass (O(T)), giving (T^{15/4+11\kappa-K}). These estimates include mixed density/remainder factors, all signs, and all discarded upper-tail placements.

Conditionally on the safe-head twelfth moment, Hölder with the target tail moment (T^{29/25+\varepsilon}) gives exponent

\[
\frac{12-j}{12}+\frac{29j}{300}=1+\frac j{75},
\]

as in (26). Replacing the target by the inherited moment exponent gives (1+(12-q_0)\beta j/12). These are complete conditional head/tail cost statements, not a proof of the tail target.

### Actual lower-(L^2) control and target equivalences: equations (27)-(28)

For sufficiently large (U), the summatory hypothesis with exponent below one gives

\[
\sum_{U<n\le2U}r_2(n)=\pi U+O(U^{\theta+\kappa})\gg U.
\]

Because (U/T\to0), continuity and (\Psi(0)=1) give (\Psi(\sqrt{n/T})\ge1/2) uniformly on that block for large (T). Cauchy-Schwarz on its (U) integers gives (\sum a_n^2\gg U^{-1/2}). The positive diagonal coefficient in (17), with its negligible error, yields

\[
\|\chi B\|_2\gg T^{1/2}U^{-1/4},\qquad
\|\chi G\|_2\ll T^{-1/2}U^{-1/4}.
\]

The reverse triangle inequality proves (28). On the weighted measure (w(R/T)dR), whose mass is (\asymp T), Hölder further gives

\[
\|\chi E^6\|_2
\ge (T\!\int w)^{-5/2}\|\chi E\|_2^6
\gg T^{1/2}U^{-3/2}.
\]

This confirms the report's stated lower scale and its scope: it prohibits dropping the actual quadratic remainder but is below the proposed sixth-power upper target.

The difference bound (3) is strictly below (T^{29/50+\varepsilon}), so reverse triangle proves equivalence of the (\mu^{*6}) and (\eta^{*6}) norm targets. In fact the same equivalence already follows using the elementary supremum exponent (1/4): its (j=5) mixed bound is (T^{1/2+\varepsilon}U^{-1/2}), still below target. Thus the logical equivalence need not rely on the stronger inherited smoothing supremum, although the sharper displayed cost (3) does.

Finally (E=J+L), with (\int w|L|^{12}\ll T), and weighted (L^{12}) triangle inequalities prove equivalence of (4) and (27). Squaring the sixth-power norm doubles its exponent; arbitrary epsilon parameters can be renamed. Hence the target moment exponent is (29/25), and the moment gap is exactly twice the norm gap (6). This checks both directions of the target equivalence without assuming that any mixed (L/J) product vanishes.

## 4. First doubtful or unproved step

No new algebraic or analytic gap was found within the audited elementary derivation and the explicitly conditional cost accounting.

The first new unproved estimate remains the target for the pure remainder, equation (4), equivalently the oscillatory twelfth-moment estimate (27). The absolute summatory estimate produces (16), not (27). The optional inherited supremum and (q_0) inputs give the stated (0.648072478\ldots) norm benchmark, leaving the stated positive gap to (29/50).

Separately, the source and full hypothesis validity of the inherited smoothing, endpoint moment, safe-head, and summatory claims were not audited here. A scoped GREEN for this report cannot be used to certify those dependencies or to promote the target.

## 5. Required controls and outcomes

1. **Exact artifact control — PASS.** The read artifact matches the assigned SHA-256.
2. **Density and phase control — PASS.** The Jacobian cancels the original half-factor, leaving density (\pi|y|^{-1/2}\) on each branch and transform (2\pi\) times the positive-(y) cosine integral.
3. **Endpoint control — PASS.** The strict (n>U) tail requires inclusive (Q(U)); the report uses it.
4. **Derivative control — PASS.** Both amplitude derivatives and the (\pi Rx^{-1/2}) phase derivative are present with correct signs and powers.
5. **Complete sixth-power control — PASS.** Every (j=0,\ldots,6) stratum is retained; (j=6) remains the unresolved target. Optional (q_0) interpolation powers also check.
6. **Tail and cross-term control — PASS.** The arbitrary upper-tail decay, sixth-product error (7/4), twelfth-product error (15/4), and conditional head/tail exponent (1+j/75) all check.
7. **Actual-coefficient and implication control — PASS.** The actual block mass yields the claimed lower quadratic remainder, while its induced sixth-power lower scale remains below target. Both target equivalences are valid and do not assert a new exponent.

All checks were analytical. No numerical experiment, external source import, or new empirical evidence was used.

## 6. Dependencies and exact artifacts used

Read in the preceding isolated phase:

- `protocol.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/briefs/blind_filter_statement.md`.

Additional artifact read for this audit only:

- `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/actual_density_remainder_attack.md`, SHA-256 `09136945693d920615e84dbb1b4223419e1b9896660e1446a37cdbcd169f538c`.

No graph, manifest, strategy, additional report, or source file cited by the claimant was opened. The completed statement-only reasoning is prior independent control, not newly inherited claimant context. The elementary proof tools used here are Fourier inversion/Plancherel, integration by parts for a right-continuous Stieltjes integrator, Schwartz decay, convolution identities, Cauchy-Schwarz, Hölder, and triangle inequalities. The analytic claims identified in Section 2 retain explicitly conditional status.

## 7. Recommended state effect

Record this immutable artifact's elementary density/remainder and complete-error seam as **GREEN within the stated conditional scope**. No correction to the reviewed report is requested.

Retain its conclusion `complete_analytic_attempt_no_new_bound` and its obstruction to omitting the pure remainder. Do not promote any new exponent, inherited interface, or parent obligation based on this review. Authoritative graph changes, validation-matrix entries, and round closure remain the conductor's responsibility.
