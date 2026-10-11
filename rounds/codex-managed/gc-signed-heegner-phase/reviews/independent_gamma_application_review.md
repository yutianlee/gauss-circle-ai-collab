# Round228 independent gamma and conditional application review

Campaign: `gc-signed-heegner-phase`  
Role: NONAUTHOR, post-isolation scalar/application reviewer  
Generated: 2026-09-28 00:01:41 UTC  
Reviewed artifact: `rounds/codex-managed/gc-signed-heegner-phase/controls/conductor_gamma_application.md`  
Verified reviewed SHA256: `f90c8dbbd21e4c881259d7026a16ddeb0a635525f741d89eeb715f3ad7659515`  
Frozen earlier isolated report SHA256: `9dcfb60996d011bccde60112c1f8577440b6bf4cc330b808c4e5cc5d2ae4ac4f`  
Graph hash: not accessed in either assignment.

## 1. Result

**GREEN for the stated scalar gamma control and the explicitly conditional functional-equation application. No required repairs.**

The large-pair constant phase, normalized derivative errors, full-axis envelope, both transition centers, and bounded-t coverage are correct. Equations (8)-(9) correctly retain the conditional level factor, the dual coefficient phase, and the extra factor from h = Dm. The report expressly withholds the actual functional equation for the spectral basis, the contour shift and dual-series expansion, uniform transformed-weight bounds, dual support, and spectral cancellation. Its conclusion therefore stays inside its proved or explicitly conditional scope.

This verdict is not an actual-source, oldspace, coefficient-normalization, spectral-pairing, or arithmetic-estimate review.

## 2. Exact hypotheses and reviewed scope

The reviewed scalar claim assumes fixed 0 < eta < 1/2, eta <= sigma <= 1-eta, delta in {0,1}, t >= 2, v real, and R > 0, with s = sigma-it+iv. Positive-real powers use the real logarithm.

For this review use the conductor's notation

\[
 a=(\sigma+\delta)/2,\quad b=(1-\sigma+\delta)/2,
 \quad w=t-v/2,\quad d=1/2-\sigma,
\]
\[
 S_\delta(\sigma,v)=\frac{\Gamma(b-iv/2)}{\Gamma(a+iv/2)}.
\]

The conductor's a and b are interchanged relative to my frozen isolated report, and its d denotes the amplitude exponent, not my earlier Bernoulli correction coefficient. All checks below use the conductor's definitions consistently.

The application additionally assumes, rather than proves,

\[
 L(s)=\omega q^{1/2-s}Q_\delta(s,t)L(1-s),\qquad |\omega|=1,
\]

with q > 0 as the positive level/conductor parameter. It further conditions every contour move and subsequent dual coefficient expansion on their justification. The coefficient scale M0 and the descendant D are positive. No actual spectral family is identified by this review.

## 3. Proof and application audit

### Gamma constants and derivative errors

Direct substitution gives the exact large pair Gamma(b+iw)/Gamma(a-iw) and the exact small pair S_delta. The large-pair logarithm has leading terms

\[
 d\log w+i\left[2w(\log w-1)+\frac{(a+b-1)\pi}{2}\right].
\]

Since a+b = delta+1/2, its constant phase is delta*pi/2-pi/4, exactly the conductor's c_delta. The factor pi^(2 sigma-1) and the phase exp(2i(v-t)log pi) in control equation (1) are also exact.

More explicitly, allowed shifted Stirling yields

\[
 \log\frac{\Gamma(b+iw)}{\Gamma(a-iw)}
 =d\log w+i[2w(\log w-1)+c_\delta]
 -\frac{i[B_2(a)+B_2(b)]}{2w}+O_\eta(w^{-2}),
\]

with fixed-order derivatives of the last error gaining the corresponding inverse powers of w. The arguments stay in fixed vertical sectors with real parts in a positive compact interval. Exponentiating this normalized logarithmic correction proves r^(j)(w) = O_(eta,j)(w^(-1-j)) as asserted in control equation (3). No derivative bound is being imposed on the unnormalized oscillatory gamma quotient.

The exact identity

\[
 2w(\log w-1)=2t(\log t-1)-v\log t+\Psi_t(v)
\]

gives control equation (4) after multiplication by E_R. Its factors and signs agree term by term. The supplied Psi_t has derivatives

\[
 \Psi_t'(v)=-\log(1-v/(2t)),\qquad
 \Psi_t^{(j)}(v)=(j-2)!(2t-v)^{1-j}\quad(j\ge2).
\]

Hence the quadratic remainder is O(|v|^3/t^2), its first and second derivatives are O(|v|^2/t^2) and O(|v|/t^2), its third derivative is O(t^-2), and higher fixed derivatives are O_j(t^(1-j)). This includes v = 0. The claimed bounds are correct.

The small pair stays exact. Its modulus is comparable to (1+|v|)^(1/2-sigma), and its j-th derivative is bounded by that modulus times a constant times [1+log(2+|v|)]^j. This follows by compactness near zero and differentiated Stirling only at large |v|. It validates the control's qualitative derivative claim without using small-argument Stirling.

### Full-axis envelope and bounded-t coverage

For any c in the positive compact interval of relevant real parts,

\[
 |\Gamma(c+iy)|\asymp_\eta
 (1+|y|)^{c-1/2}e^{-\pi|y|/2}.
\]

Exponential factors cancel within each pair. Thus the more precisely scaled envelope is

\[
 \pi^{2\sigma-1}
 [(1+|v|/2)(1+|2t-v|/2)]^{1/2-\sigma}.
\]

The fixed factors pi and 2 can be absorbed uniformly because sigma lies in the specified compact interval. This proves the exact comparability stated in control equation (2), including negative values of 1/2-sigma and both transition centers.

For t >= 2, t^(1/3) <= 2t/3: equivalently t^2 >= 27/8, which holds. Both requested windows therefore lie in |v| <= 2t/3, and w >= 2t/3 >= 4/3 throughout. The conductor's expanded window repairs the possible bounded-t overlap issue without requiring another asymptotic regime.

On |v| <= t^(1/3), both the normalized gamma error and the cubic phase error are O_eta(t^-1). On the half window the latter can instead be a nonzero constant times t, so the control correctly retains exact Psi_t there. Replacing w^d by t^d costs O_eta(|v|/t); the separate t^-2/3 warning is correct.

### Conditional functional-equation scalar and descendant mapping

Mellin inversion of the stipulated original coefficient test, where initially justified, has integrand

\[
 M_0^z\widehat a(z)L(z-it).
\]

On z = 1/2+iv one has s = 1/2-it+iv and

\[
 q^{1/2-s}=q^{it-iv}.
\]

Multiplication by E_R and the near-transition formula give, for the functional-equation scalar,

\[
 \omega q^{it-iv}E_RQ_\delta(s,t)
 =\omega e^{it\log(qR^2)}e^{iv\log(\pi^2/(qt))}
       S_\delta(1/2,v)e^{i[c_\delta+\Psi_t(v)]}[1+r(w)].
\]

There is no missing power of w or pi in this line: at sigma = 1/2, both real amplitude exponents vanish. If expansion of L(1-s) is justified in the separately required manner, its n-th coefficient contributes

\[
 n^{-(1-s)}=n^{-1/2-it+iv}.
\]

The factor M0^z also supplies M0^(iv), so the variable oscillations are exactly

\[
 e^{it\log(qR^2/n)}
 e^{iv\log(\pi^2M_0n/(qt))},
\]

as in control equation (9). The real amplitudes M0^(1/2), n^(-1/2), the test transform, the coefficient, and omega are outside this statement of the oscillations, not silently replaced by 1.

For h = Dm, h^(it) = D^(it)m^(it) and M0 = M/D. Thus the first phase becomes exp(it log(q D R^2/n)), while the second uses M/D. This is the claimed descendant mapping. The zero of the displayed elementary v-linear frequency alone is n = qt/(pi^2 M0); describing its scale as n comparable to qt/M0 is correct because pi^2 is fixed. The factor S_delta and the curvature phase remain, so this calculation by itself gives no support theorem or localization estimate.

Finally, substituting the control's expressly stated size t comparable to T M/sqrt(N) into qt/M0 gives q D T/sqrt(N). This last substitution is algebraic under that size assumption. I have not independently established that the round's actual spectral variables satisfy it.

## 4. First gap or unsupported extension

No repair is required within the reviewed scope. The first unproved application step is exactly the one the control withholds: identifying an actual spectral series satisfying its equation (8), with the specified level factor, gamma parity, root number, and coefficients. Even after that identification, the contour move, treatment of any crossed singularities, dual expansion or continuation, and uniform transformed-test estimates require proofs.

In particular, the displayed v-linear phase cannot certify that all dual coefficients outside n comparable to qt/M0 are negligible. The exact small gamma ratio has additional transform behavior, and the full real v axis contains both transition centers. Neither critical-line unit modulus nor removal of one common phase establishes cancellation in the complete spectral expression. The control explicitly makes all of these limitations clear.

The shorthand in its inversion control is valid on the critical line, as specified in its earlier symmetry statement. Away from that line, s -> 1-s changes sigma to 1-sigma as well as reflecting v -> 2t-v. The full meromorphic inversion formula printed in the control is correct; no sigma-preserving off-critical inversion is used in its derivation.

## 5. Required controls and outcomes

- **Exact substitution:** all four gamma arguments and pi factors match. PASS.
- **Phase constant:** c_0 = -pi/4 and c_1 = pi/4; the signs from the negative-imaginary denominator are correct. PASS.
- **v = 0:** S_delta(sigma,0) = Gamma(b)/Gamma(a), and E_R leaves phase 2t log R+c_delta with normalized O_eta(t^-1) error. PASS.
- **Critical line:** a = b, so each gamma ratio has unit modulus; conjugation and Q(s,t)Q(1-s,t) = 1 give reflected-v inversion. PASS.
- **Derivative errors:** they apply to the normalized remainder; exact Psi_t derivatives give all asserted orders. PASS.
- **Both transitions and full axis:** v = 0 and v = 2t, with a two-sided envelope valid through both. PASS.
- **Small bounded t:** |v| <= t^(1/3) is inside the adopted 2t/3 window for every t >= 2. PASS.
- **Larger window:** no quadratic-only uniform small error is claimed. PASS.
- **Conditional FE and descendant phases:** every q, D, M0, n, pi and t factor in equations (8)-(9) has the correct sign and location. PASS within the explicit hypotheses.
- **No support/cancellation promotion:** dual support, transform bounds, actual coefficient identification and spectral cancellation are expressly ungranted. PASS.

All controls were analytic. Hash verification was an artifact-integrity check, not a mathematical experiment.

## 6. Dependencies and exact isolation disclosure

This is a new, post-isolation review. It does not retain statement-only status, because the conductor control was deliberately read for review. The earlier isolated report remains frozen and was not edited.

The permitted earlier context retained from my own assignment consists of:

1. `protocol.md`.
2. `rounds/codex-managed/gc-signed-heegner-phase/briefs/blind_gamma_transition_statement.md`.
3. My own derivation and report `rounds/codex-managed/gc-signed-heegner-phase/reports/blind_gamma_transition.md`, frozen at SHA256 `9dcfb60996d011bccde60112c1f8577440b6bf4cc330b808c4e5cc5d2ae4ac4f`.

The only newly read mathematical artifact was:

4. `rounds/codex-managed/gc-signed-heegner-phase/controls/conductor_gamma_application.md`, verified at SHA256 `f90c8dbbd21e4c881259d7026a16ddeb0a635525f741d89eeb715f3ad7659515` before review.

The optional full interface was not needed and was not read. No current A/B reports, sibling reviews, graph, campaign manifest, source cards, historical artifacts, or external sources were accessed. The conductor control contains provenance references to other artifacts; those references were not followed and their mathematical contents were not assumed. No experiment was run.

This review's functional-equation calculation is conditional on the formula stated in the reviewed control. It supplies no external-source certification and no audit of actual oldspace data. Only this assigned review path was written during the new assignment.

## 7. Recommended state effect

Mark the nonauthor gamma/application seam **GREEN**, bound strictly to reviewed SHA256 `f90c8dbbd21e4c881259d7026a16ddeb0a635525f741d89eeb715f3ad7659515`.

Retain the control as elementary scalar and conditional application evidence. This verdict does not justify a graph promotion of an arithmetic bound, a proof-draft change, a completed dual transform, or closure of any complete spectral owner. The conductor retains responsibility for all state decisions. No next-round work is proposed or undertaken.
