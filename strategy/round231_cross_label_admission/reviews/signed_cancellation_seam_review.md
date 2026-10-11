# 1. Result and exact review verdict

Task: Prelaunch231 / nonauthor `signed_cancellation_seam_review`. Reviewer role: the earlier statement-only transport rederiver, now reviewing the conductor's arithmetic and restoration argument. Date: 2026-10-11. Graph provenance supplied by the candidate: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

Candidate reviewed and independently hash-checked:

`strategy/round231_cross_label_admission/conductor_signed_cancellation.md`

SHA256: `6344944f13bf075d3e871358ade9d59289d2c4a5b8fa53a9c313eee3cdbf1fc8`.

**PASS for retention as reviewed evidence, with the source-scope and finite-reference qualifications below.** The arithmetic means, Euler identity, exact pooled-continuum cancellation, entire large-class harmonic tail, complete moment centering, frequency normalization, and forced-cancellation implications are correct under the actual mollifier and the declared accepted inputs. No new complete upper bound follows. The target remains unproved.

The first missing mathematical estimate is the candidate's equation (8), or an equally strong estimate for the signed transform in (7), for the actual arithmetic measure. The preceding identities do not establish it.

The local-discrepancy alternative must use a finite reference and control the variation of the discrepancy measure `mu_T-rho_T dx`, not merely the scalar signed mass of the reference. The candidate's fixed-profile references with polynomially bounded amplitude meet this requirement. Its exact weighted gate (8) does not require a polynomial variation bound beyond finite variation.

# 2. Exact hypotheses and audited claims

The actual definitions needed for this audit are supplied explicitly by the permitted Round216 kernel: `rho` is real, nonnegative, radial, smooth, supported in the unit disk, and has integral one; `Psi(t)=rho-hat(t e_1)` under the minus Fourier convention; `w` is real, nonnegative, smooth, supported in `[1/2,2]`; `T>=2`; `Q=floor(T^{2/5})`. The coefficients are

\[
a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),
\]

and all squarefree classes, harmonics, real cosine phases, and ordered distinct-class tuples are retained. Write `M_p(F)=integral w(R/T)|F(R)|^p dR`. The accepted pointwise parameter satisfies `1/8<beta<13/100`; its more precise value is used only in the candidate's decimal displays.

The review treats the permitted Round204/216 kernels as the declared accepted interfaces. It does not newly authenticate their external Bourgain or qualified Li--Yang source applications or the current proof graph. Similarly, the prior harmonic admission decision supplies its reviewed conclusion `C_harm >> T^{5/2}`; its underlying proofs are outside this review's permitted context.

| Seam | Verdict | Exact scope |
| --- | --- | --- |
| Uniform arithmetic mean in `s,x` | PASS | Fixed `1/2<sigma<1`, every fixed `eta>0`; constants may depend on these and not on `s,x`. |
| `sum_s kappa_s/s^2=pi` | PASS | Absolutely convergent positive Euler product; includes the prime 2 and inert primes. |
| Exact Abel-limit cancellation | PASS | Actual compactly supported real spatial mollifier; positive `R>T^{-1/2}`. |
| Entire large-class harmonic tail | PASS | Uniform one-step integration by parts and an absolutely summable `s`-majorant. |
| `M_11`, `M_12`, centering and restoration | PASS | Uses complete accepted bounds and the complete Round216 repeated-class estimate. |
| Frequency measure and discrepancy gate | PASS | Finite complex measures; conjugate symmetry makes `D` real; reference conditions stated above. |
| Forced signed cancellation | PASS, inherited lower-bound premise | Necessary consequences of the reviewed certificate lower bound and accepted complete upper bound. |
| Target estimate | NOT PROVED | Gate (8) remains new arithmetic work. |

# 3. Independent seam derivations

## Uniform arithmetic means and the exact Euler identity

Put

\[
g(s)=\prod_{p^a\Vert s,\ p\equiv1(4)}(2a+1).
\]

The representation formula gives `r_2(s^2)=4g(s)`. For squarefree `d`, a split prime occurring in `d` contributes the ratio

\[
u_p=\frac{2(a+1)}{2a+1},\qquad a=v_p(s),
\]

while the prime 2 contributes ratio one and an inert prime in `d` makes the representation count zero. The local factors for the squarefree series are therefore `1+u_p X`, `1+X`, and `1`, respectively. Dividing by the local factors of the series of `r_2` yields exactly the candidate's polynomials

\[
(1+u_pX)(1-X)^2,\qquad 1-X^2,\qquad 1-X^2.
\]

The leading coefficient is handled correctly by

\[
\mu(d)^2r_2(ds^2)=g(s)(h_s*r_2)(d).
\]

For split `p` not dividing `s`, the local polynomial is `1-3X^2+2X^3`, so its absolute Euler factor converges for `sigma>1/2`. Modified split primes have uniformly bounded coefficients, including their possible degree-one term. The product over primes dividing `s`, together with `g(s)`, is `O_{sigma,eta}(s^eta)` by the elementary divisor bound, with the input exponent divided between the finitely many factors as needed. Thus

\[
g(s)\sum_m |h_s(m)|m^{-\sigma}\ll_{\sigma,\eta}s^\eta.
\]

Here is the full residue-tail check omitted from the candidate's compressed derivation. Convolving the area estimate gives

\[
A_s(x)=g(s)\sum_{m\le x}h_s(m)
\left[\pi x/m+O((x/m)^{1/2}+1)\right].
\]

Since `x/m>=1`, the error inside the sum is `O((x/m)^sigma)`. The omitted residue tail is bounded by

\[
g(s)x\sum_{m>x}\frac{|h_s(m)|}{m}
\le g(s)x^\sigma\sum_{m>x}|h_s(m)|m^{-\sigma},
\]

using `sigma<1`. Both errors are `O(s^eta x^sigma)`. This is uniform for real `x>=1`; no integer-endpoint exception is required.

At a modified split prime, the ratio of the residue to the `s=1` residue is

\[
(2a+1)\frac{1+u_p/p}{1+2/p}
=1+\frac{2a(p+1)}{p+2},
\]

which proves the displayed `kappa_s`. The base split factor is
`(1-p^{-1})^2(1+2p^{-1})=1-3p^{-2}+2p^{-3}`. The prime 2 and inert factors are exactly `1-p^{-2}`.

For a transparent Euler check, put `t=p^{-1}` at a split prime. Then

\[
K_p=\frac1{1-t^2}
+\frac{2(1+t)t^2}{(1+2t)(1-t^2)^2}
=\frac1{(1-t)^2(1+2t)}.
\]

Indeed the numerator after combining the first two terms is
`(1-t^2)(1+2t)+2(1+t)t^2=(1+t)^2`. The split factors cancel exactly. For 2 and inert primes, `(1-p^{-2}) sum_{a>=0}p^{-2a}=1`. Absolute convergence follows either from the factors or from `kappa_s<<_eta s^eta` with `eta<1`. This proves the full identity `sum_s kappa_s/s^2=pi` without random-label averaging.

## Exact pooled continuum: amplitude, Abel regularization, and phase

Under `y=s sqrt(x)`, the complete measure-amplitude transformation is

\[
s^{-3/2}x^{-3/4}\,dx=2s^{-2}y^{-1/2}\,dy.
\]

The sum of absolute integrals is finite because `sum_s kappa_s/s^2=pi` and `y^{-1/2}Psi(y/sqrt(T))` is integrable at zero and infinity. Therefore the pooling gives the candidate's exact expression

\[
\mathcal B_T(R)=2\pi\operatorname{Re}
\left[e(-3/8)\int_0^\infty y^{-1/2}\Psi(y/\sqrt T)e(Ry)\,dy\right].
\]

Let `v(u)=integral rho(u,t)dt`. It is real, smooth, and supported in `[-1,1]`, and `Psi(y/sqrt(T))=integral v(u)e(-uy/sqrt(T))du`. For `lambda>0`, the additional factor `exp(-lambda y)` makes the interchange with `v` absolutely integrable. For `b=R-u/sqrt(T)>0`, the elementary gamma integral on the continuous principal branch gives

\[
\int_0^\infty y^{-1/2}e^{-\lambda y}e(by)\,dy
=\sqrt\pi(\lambda-2\pi i b)^{-1/2}
\longrightarrow\frac{e^{i\pi/4}}{\sqrt{2b}}.
\]

For each `R>T^{-1/2}`, the support of `v` gives a strictly positive lower bound for `b`, so this limit passes through the compact `u` integral. On the original `y` side, integrability of `y^{-1/2}Psi(y/sqrt(T))` removes the Abel factor by dominated convergence. Since

\[
e(-3/8)e^{i\pi/4}=-i
\]

and `integral v(u)/sqrt(2(R-u/sqrt(T)))du` is real, the real part is zero. This proves exact cancellation. It applies on the full physical window for `T>=2`, since `T/2>T^{-1/2}`.

The actual spatial support and realness are essential hypotheses. Merely assuming an arbitrary real even Schwartz `Psi` would not give this exact support-based conclusion. The permitted Round216 definition supplies the necessary stronger hypothesis.

## Entire harmonic tail in the large-class continuum

For the `s`th term the lower endpoint is `y_0=s sqrt(Q)`. Write `a(y)=y^{-1/2}Psi(y/sqrt(T))`. Directly,

\[
|a(y_0)|+\int_{y_0}^\infty |a'(y)|\,dy
\le C_\Psi y_0^{-1/2}.
\]

The derivative of `y^{-1/2}` contributes at most `||Psi||_infinity y_0^{-1/2}`. The other contribution is bounded by

\[
T^{-1/2}\int_{y_0}^\infty y^{-1/2}|\Psi'(y/\sqrt T)|\,dy
\le y_0^{-1/2}\int_0^\infty|\Psi'(u)|\,du.
\]

The upper boundary is zero. Integration by parts against `e(Ry)` therefore bounds the entire `s`th term by

\[
C_\Psi R^{-1}\kappa_s s^{-5/2}Q^{-1/4}.
\]

The harmonic sum converges uniformly because `sum_s kappa_s s^{-5/2}<=pi`. Hence

\[
\|\mathcal Z_{T,Q}\|_{L^\infty([T/2,2T])}
\ll T^{-1}Q^{-1/4}\ll T^{-11/10}.
\]

The floor in `Q` changes only a constant. Every harmonic is included; no sharp truncation or unestimated tail remains.

## Complete moment centering and repeated-class restoration

The accepted complete estimate for `B_T` gives `M_12(B_T)<<T^{10 beta+epsilon}`. Round216 pays `M_12(L_Q)<<T^{15/13+epsilon}`. The scalar twelfth-power inequality therefore gives the candidate's complete bound
`M_12(Z_Q)<<T^{10 beta+epsilon}`, since `15/13<10 beta`.

Round216 also gives `M_10(Z_Q)<<T^{8 beta+epsilon}`, with the possible `T` term dominated because `8 beta>1`. Cauchy--Schwarz with respect to `w(R/T)dR` now yields

\[
M_{11}(Z_Q)\le M_{10}(Z_Q)^{1/2}M_{12}(Z_Q)^{1/2}
\ll T^{9\beta+\epsilon}.
\]

For `D=Z_Q-mathcal Z`, the pointwise power-difference estimate gives

\[
|M_{12}(D)-M_{12}(Z_Q)|
\ll \|\mathcal Z\|_\infty M_{11}(Z_Q)
+T\|\mathcal Z\|_\infty^{12}
\ll T^{9\beta-11/10+\epsilon}+T^{-61/5}.
\]

The second term is harmless. The claimed exponent in (4) is therefore correct. Since

\[
(9\beta-11/10)-(8\beta-1/5)=\beta-9/10<0,
\]

Round216's complete repeated-class estimate yields (5) with exactly the stated error. It is not necessary to assume positivity of the distinct-class integral: the accepted absolute error bound supplies both directions.

If `M_12(D)<<T^{29/25+epsilon}` were obtained, this identity would give the corresponding bound for `I_12`; the accepted equivalences restore `M_12(Z_Q)` and `M_12(B_T)`. The head cost remains below the target because `29/25-15/13=2/325`. All mixed terms are paid by the complete norm inequalities. This is a conditional restoration, not a new estimate for `D`.

## Frequency-measure normalization, variation, and discrepancy

The candidate's positive and negative atoms have weights

\[
\tfrac12 a_{ds^2}e(-3/8),\qquad
\tfrac12 a_{ds^2}e(3/8),
\]

at `s sqrt(d)` and `-s sqrt(d)`. Their Fourier transform with `e(Rx)` is exactly the required real cosine. The factors `1/2`, the two phases, and the negative-frequency sign are correct.

More explicitly, the continuum positive-frequency density is

\[
e(-3/8)y^{-1/2}\Psi(y/\sqrt T)
\sum_{s\sqrt Q\le y}\frac{\kappa_s}{s^2},\qquad y>0,
\]

with the conjugate reflected density at negative frequencies. Choices at the endpoints affect no continuous mass. Subtract this measure from the atomic one to obtain `tau_T`. The atomic variation is at most

\[
\sum_n r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|\ll T^{1/4},
\]

by the area estimate and a rapidly decaying dyadic sum. The continuous variation is at most

\[
2\pi\int_0^\infty y^{-1/2}|\Psi(y/\sqrt T)|\,dy
=O_\Psi(T^{1/4}).
\]

Therefore `||tau_T||_TV=O(T^{1/4})`, and `mu_T=tau_T^{*12}` has variation `O(T^3)`. Conjugate symmetry implies `F_tau=D` is real. Thus `F_mu=D^{12}=|D|^{12}`, which verifies that the candidate represents the absolute twelfth moment rather than a different complex power:

\[
M_{12}(D)=T\int\widehat w(-Tx)\,d\mu_T(x).
\]

For a finite reference density, set `nu_T=mu_T-rho_T dx` and `H_T(x)=nu_T((-infinity,x])`. The frozen independent identity has derivative `K'_T(x)=-T^2 what'(-Tx)`, hence

\[
\mathcal L_T(\nu_T)=T\int\widehat w'(-u)[H_T(u/T)-c]\,du.
\]

Atoms, nonzero total mass, and arbitrary constant baselines are legal; the boundary kernel vanishes. Taking the absolute value outside the integral and then applying the triangle inequality yields exactly (8) as a sufficient hypothesis, with the exponent increase `1+4/25=29/25`.

For precision, the local alternative has remainder

\[
C_{w,N}T\big(\|\mu_T-\rho_Tdx\|_{\rm TV}+|c|\big)W^{-N},
\qquad W=T^\delta.
\]

Thus it is valid when the discrepancy variation and baseline have polynomial bounds, in particular `O(T^3)` for the intended fixed-profile reference. It cannot be read as an assertion for an arbitrary reference with uncontrolled variation merely because its signed transform is negligible. The exact weighted gate (8) is unaffected by this qualification. The broad fixed-profile and exact low-frequency smoothing examples in the frozen report meet the stated finite-measure requirements.

## Forced cancellation and its exact scope

Every `J_d` is real, and
`sum_d^* |J_d| <= integral w(R/T)(sum_{d>Q}A_d(T))^{12}dR < infinity`.
Therefore the positive and negative decompositions satisfy exactly

\[
C_++C_-=\mathcal C_{\rm harm},\qquad
C_+-C_-=I_{12}.
\]

Using the inherited reviewed lower bound `C_harm>=cT^{5/2}` and the accepted complete upper bound `|I_12|<<T^{10 beta+epsilon}` gives, for sufficiently small fixed epsilon and large `T`,

\[
C_+,C_-\ge \tfrac c4T^{5/2},\qquad
\frac{|C_+-C_-|}{C_++C_-}\ll T^{10\beta-5/2+\epsilon}.
\]

The exponent equals the candidate's `-1.2103364805...`. The target would imply the necessary ratio `O(T^{-67/50+epsilon})`. A ratio bound at this exponent alone is not sufficient when the denominator has only a lower bound; the candidate explicitly observes this. The remaining saving in the accepted complete upper bound is exactly `10 beta-29/25`, and none of these manipulations establishes it. No signed lower bound for the complete moment follows from the certificate lower bound.

# 4. First doubtful or unproved step

The first unproved target step is equation (8) for the actual centered twelvefold frequency measure. It remains unproved after all the validated arithmetic means, Euler pooling, Abel cancellation, harmonic tails, and restoration costs have been paid. Equation (7) is an exact reformulation and equation (8) is an absolute sufficient certificate; neither is automatically a target-sized estimate.

The only formulation qualification needed for the transport alternatives is explicit finite-reference control: for the local-to-global version, bound the variation of `mu_T-rho_Tdx` and the chosen baseline. A bound on total signed mass is insufficient. This qualification is already present in the frozen independent report and is satisfied by the candidate's intended fixed-profile and smoothing references.

No additional gap was found in equations (1)--(9) under their actual hypotheses and declared inherited inputs. The source restrictions in Section 6 prevent this review from certifying either external analytic sources or the previous harmonic obstruction proof anew.

# 5. Required controls and outcomes

* **Prime classes:** At split primes the residue ratio and local cancellation were rederived as rational identities. At 2 and inert primes the separate factors cancel exactly. PASS; no missing local factor or normalization by 4.
* **Uniform endpoints:** The mean-law proof uses the exact inner count at real `x/m` and bounds both the finite convolution error and residue tail. PASS for all real `x>=1` and integer `s>=1`.
* **Abel phase:** The limiting square-root phase is `exp(i pi/4)` for positive `b`; multiplying by `e(-3/8)` gives `-i`, whose real part is zero. PASS. The proof deliberately does not assert the same cancellation for negative `b` or arbitrary Schwartz multipliers.
* **Infinite harmonic tail:** The `s`-majorant is `kappa_s s^{-5/2}`, dominated termwise by the absolutely summable `kappa_s s^{-2}`. PASS without any harmonic cutoff.
* **Centering exponents:** The exact error is `T^{9 beta-11/10+epsilon}+T^{-61/5}`; it is dominated by the accepted repeated-class cost. PASS for the entire permitted beta interval.
* **Atomic Fourier normalization:** A single real cosine reproduces the two candidate atoms with their half-weights and conjugate phases. Its twelfth power is represented by convolution, including all mixed terms. PASS.
* **Coherent modulation:** The frozen independent control has twelve factors of mass `T^{1/4}`, each with CDF error of order `T^{-5/4}`, but their convolution has integrated contribution of order `T^{5/2}`. It therefore excludes an inference from coarse one-factor laws to (8). PASS as an abstract information-content control only; it does not have the actual arithmetic supports or coefficients.
* **Fixed local window:** An atom just outside `|Tx|<=W` can have zero local CDF discrepancy and a window integral of order `T^4` for mass `T^3`. PASS as a falsification of the fixed-window shortcut; the growing-window tail estimate avoids it.
* **Forced-cancellation direction:** The certificate lower bound yields cancellation and a necessary relative-error statement, but no signed moment lower bound or sufficient target estimate. PASS.

These controls are analytical and algebraic. No numerical experiment was used, and the candidate's Wolfram diagnostics are not treated as proofs.

# 6. Dependencies, exact artifacts, and source limits

Permitted artifacts used in this review:

1. `protocol.md`, already read for the isolated assignment and retained as the governing protocol.
2. `strategy/round231_cross_label_admission/reports/blind_signed_transport.md`, preserved unchanged and hash-verified at `47b6e84139f14a9e85e15200f51de0ae6a05eacb3b4443c71c51f394bea7186e`.
3. `strategy/round231_cross_label_admission/conductor_signed_cancellation.md`, hash-verified at `6344944f13bf075d3e871358ade9d59289d2c4a5b8fa53a9c313eee3cdbf1fc8`.
4. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
5. `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`.
6. `strategy/round231_harmonic_admission/conductor_decision.md`.

The review did not read current sibling reports, the candidate's referenced complete-target brief, the proof graph, source cards, or the prior harmonic proof/review files. The actual fixed functions and normalization needed here are fully specified in the permitted Round216 kernel. The accepted external-source qualifications in Round204/216 are inherited rather than independently rechecked. The prior harmonic admission decision is evidence of the reviewed lower-bound premise; this report audits its subsequent use, not its original proof.

The earlier report remains a statement-only rederivation at its frozen hash. This new report is a nonauthor line-and-seam review of the conductor candidate and does not claim continued statement-only isolation after reading it. No other report or authoritative state file was edited.

# 7. Recommended state effect

Retain the exact reviewed candidate as evidence, with the finite-reference/tail interpretation made explicit wherever the local discrepancy alternative is reused. The narrow identities and complete centering reductions pass this review; the fine-scale arithmetic estimate does not exist in the reviewed material.

No target promotion, accepted-graph mutation, proof-draft update, or analytic Round231 launch is justified by this candidate. Any later admission must add a proved arithmetic estimate controlling equation (7) or (8), or a different complete signed estimate with a better restored exponent. This report stops at the assigned review and does not design a successor round.
