# 1. Result

**GREEN within the stated scope.** This NONAUTHOR, NONBLIND Round227 review checks `reports/joint_shift_spectral_attack.md` at SHA256 `9df8afa574a54a6d9c7ca587030aeaec00a7daa345594d224116a93e823d3560` in campaign `gc-complete-joint-spectral-remainder`.

The ordered spectral identity, exact density/atom treatment, quantitative finite truncation, inverse-gamma Legendre kernel, scalar stationary phase, and full fallback restoration check out. The report correctly separates the exact ordered representation from a reordered full Legendre expansion whose summation has not been justified there. Its exponentially renormalized theta-pairing norms are not ordinary Parseval norms.

GREEN does not certify the unproved complete inequality (25), an arithmetic cancellation estimate, a new exponent, or a spectral-method impossibility. No correction to the reviewed bytes is required. The first remaining full estimate is exactly the complete finite-contour/finite-height inequality stated by the claimant.

# 2. Exact statement and hypotheses reviewed

All notation and the required real ranges are those of the frozen interface and claimant Section 2: actual signed fixed Schwartz `Psi`, every real `R` comparable to `T`, every dyadic `2<=N<=P`, the literal smooth overlap, all `1<=h<2N`, and the single outer real part. The target is raw remainder `A_J(N)^2 N^(3/2) T^epsilon`.

I checked the report against these exact primary versions:

* [HKLDW1705.04771v3](https://arxiv.org/html/1705.04771v3), especially equations (3.3), (3.4), (3.7), (3.9), (3.10), Lemma 3.4, and the Fourier convention immediately before Theorem 3.3.
* [HKLDW1703.10347v3, Lemma 6.1 and proof](https://arxiv.org/html/1703.10347v3#S6). The Fourier-coefficient estimate in its proof concerns the fixed level-four Maaß basis and does not involve the theta power `k`. Its separate exponentially decaying theta-pairing assertion does involve that paper's regularization and is not imported for the present `k=2` vector.
* [AH2607.13518v1](https://arxiv.org/html/2607.13518v1), Sections 2.1 and 2.4 and Theorems 1.2--1.3, with the [exact PDF](https://arxiv.org/pdf/2607.13518v1) printing qualifications retained from my preceding source audit.

This review does not source or presume a corrected version of AH's collective large-sieve display. It also does not treat the external statements as accepted graph nodes merely because their application is being reviewed.

# 3. Independent proof and seam checks

## Ordered identity, center, and spectrum

For `q_h(y)=W_h(Ny-h)`, Mellin inversion gives

\[
 \frac1{2\pi i}\int_{(2)}N^s\widehat q_h(s)(n+h)^{-s}\,ds=W_h(n).
 \tag{R1}
\]

Also
\(h^{1-s}/(s-1)=\int_h^\infty v^{-s}dv\), so its pairing in (R1) is exactly `integral W_h`, not an approximate main term. The `n=0` atom is removed before finite truncation. Its full transform is zero because `W_h(0)=0`; the finite transform generally is not zero. Keeping `-Z_L` is therefore necessary and correct.

Set `z=it` in source (3.10). Since `dz=i dt`, its `1/i` contributes no remaining measure factor. The printed continuous factor becomes exactly claimant (3), and the source pairing is `v_a(t)=<V,E_a(.,1/2+it)>`. The separate `1/(4pi)` in spectral Parseval is already absorbed into the source coefficient calculation; inserting another one into claimant (6) would be an error. All three cusps are present. The constant form's Poincare coefficient vanishes, as source (3.9) states.

Although Theorem 3.3 introduces its formula initially for sufficiently large real part, using `sigma=2` is legitimate. The Dirichlet series and the centered arithmetic bracket converge there. The spectral formula converges normally on compact subsets to the right of the possible gamma poles, using the source Fourier bound, ordinary Parseval, and the exponential gamma decay. The identity thus continues from the initial right half-plane to `sigma=2` without crossing the pole at 1 or any continuous/discrete residue. No unlisted contour motion is involved.

## Quantitative finite tails

The claimed Dirichlet-series estimate follows directly by splitting the `n` sum at `h`:

\[
 \sum_{n\ge1}\frac{r_2(n)r_2(n+h)}{(n+h)^2}
 \ll_\eta h^{-1+\eta}.
 \tag{R2}
\]

The atom and density have the same adequate envelope. On the fixed logarithmic support of `q_h`, each derivative costs at most a power of `1+Lambda_h`. Integrating the resulting `|tau|^{-B}` tail and summing `h^{-1+eta}` proves claimant (7), after relabeling the small exponent.

I also checked that claimant (8) needs only ordinary Parseval. For `|tau|<=L`, `t>=U>=4L`, Stirling gives, on `sigma=2`,

\[
 |G(2+i\tau,it)|\ll (1+t)^2 e^{-\pi t+\pi L},
 \tag{R3}
\]

with a harmless fixed polynomial in `1+L` if desired. On a spectral band `K<=t<=2K`, the additional source supplies

\[
 \sum e^{-\pi t_j}|\rho_j(h)|^2
 \ll_\epsilon h^{2\Theta+\epsilon}K^{2+\epsilon}.
 \tag{R4}
\]

Cauchy using `sum |v_j|^2<=||V||_2^2` therefore bounds the band by a fixed polynomial in `K` times
\(h^{\Theta+\epsilon}e^{-\pi K/2+\pi L}\).
The outside factor in claimant (5) has modulus `N^2 h^(-3/2)`. Its shift sum converges with the `h^(Theta+epsilon)` factor because `Theta<1/2`. Integrating the finite contour costs at most a further factor `L`. This proves the shape in (8) with a fixed polynomial exponent `C`; its existence does not depend on an exponentially weighted bound for `v_j`.

For the continuous part, source (3.3) and the gamma factor imply
\(e^{-\pi|t|/2}|c_{a,h}(t)|\ll h^\epsilon\log(2+|t|)\).
Ordinary continuous Parseval and (R3) give the same exponential conclusion. The factor `h^it` has modulus one. The inverse zeta factor on the line `Re(2s)=1` contributes only logarithmic growth; near zero the reciprocal vanishes rather than producing a singularity. The three cusps are summed separately, with fixed constants.

For the claimant's choice `L=T^Q(1+Lambda_max)`, the Mellin error becomes
\[
 O\bigl(A^2N^{2+\eta}(1+\Lambda_{\max})T^{-Q(B-1)}\bigr).
\]
Here `N<=2T^(3/2)` and `Lambda_max<<T^(7/4)`. Fixed sufficiently large `Q,B` therefore give any requested negative power of `T`; the spectral error with `U=4L` is exponentially smaller. This verifies the finite approximation to the complete quantity, including the intermediate range below `4L` that the claimant explicitly retains.

## Inverse gamma identity and all powers

I independently recover claimant (9) without relying on its abbreviated inverse-kernel notation. Put `a=1/2-it`. Pfaff's transformation of the Euler integral gives

\[
 P_{-1/2+it}(2u-1)=u^{-a}
 {}_2F_1(a,a;1;1-u^{-1}).
\]

With `z=1-u^(-1)`, integrating the power series first where convergence is absolute yields

\[
\begin{aligned}
 \int_1^\infty P_{-1/2+it}(2u-1)u^{-s}\,du
 &=\int_0^1(1-z)^{s+a-2}{}_2F_1(a,a;1;z)\,dz\\
 &=\frac{\Gamma(s+a-1)\Gamma(s-a)}{\Gamma(s)^2}
 =G(s,it).
\end{aligned}
 \tag{R5}
\]

Both sides continue throughout `Re s>1/2` for fixed real `t`; the Legendre integral is absolutely convergent there. Pairing this identity against the compact smooth test in claimant (5) gives

\[
 h^{1/2}\int_1^\infty P_{-1/2+it}(2u-1)W_h(hu-h)\,du
 =h^{-1/2}\int_0^\infty W_h(x)P_{-1/2+it}(1+2x/h)\,dx.
 \tag{R6}
\]

This confirms every `N` and `h` power in claimant (10); no `2pi` factor enters this Mellin inversion. At the continued parameter `t=i/2`, `P_{-1}=1` and `G=1/(s-1)`, correctly reproducing the density control.

The argument proves a fixed-mode identity. It does not by itself permit passing the `L` limit through an infinite spectral sum or integral. The claimant's ordering distinction is analytically substantive and correctly maintained.

## Global scalar stationary and endpoint checks

On the literal overlap, `r=2 asinh sqrt(x/h)` is at least `log 3`. Its support length is bounded, its smoothly zero-extended amplitude has bounded fixed-order derivatives after extracting `A^2`, and `dx=sqrt(x(x+h)) dr`. These facts are uniform when an overlap shrinks or `h/N` tends to zero.

The exact Mehler integral in the report has value 1 at `r=0`: replacing `cosh r-cosh u` by `(r^2-u^2)/2` makes its limit immediate. It satisfies the Legendre equation. Its even extension removes the artificial endpoint at zero. Expanding the square-root singularities at the two outer endpoints gives the two symbols in claimant (12), uniformly on `r>=log 3`. The boundedness of `coth r` and all derivatives supplies the large-`r` uniformity needed here.

The positive branch's derivative is
\(t-\pi R\sqrt h e^{-r/2}\), and its second derivative on support is comparable to `Lambda_h`. The negative branch's derivative never vanishes. Thus stationary spectral height is exactly
\(t=\pi R(\sqrt{x+h}-\sqrt x)\).
At that point the phase is `2t+t log(pi^2 R^2 h/t^2)`, confirming both the spectral twist `h^it` and the common spectral phase.

For the leading coefficient, write `a_x=sqrt(x(x+h))`. The positive exponential in the cosine contributes amplitude
\(g(x+h)g(x)a_x/\sqrt{2\pi t\sinh r}\).
Multiplying by the stationary factor `sqrt(4pi/t)` and using `sinh r=2a_x/h` gives exactly
\(g(x+h)g(x)\sqrt{h a_x}/t\).
The two quarter-turn phases cancel. This verifies claimant (14), including its coefficient and its next-order size on the stated padded interior regime.

Second-derivative estimation proves the global bound (15), independently of whether the stationary point is in the support. Repeated nonstationary integration gives the printed exterior-band estimates; for bounded `t`, the exact Legendre function has the familiar extra logarithmic factor bounded by `log(2N)`, which the report retains. Its amplitude and derivatives cost at most that factor after the displayed normalization. Smooth endpoint vanishing eliminates hard boundary contributions. These scalar estimates do not justify dropping any finite-contour region of (24), and the claimant does not do so.

## Norm ledger and complete restoration

Writing `V_j=e^(pi t_j/2)v_j` and `alpha_j(h)=e^(-pi t_j/2)rho_j(h)` preserves the coefficient product exactly. Cauchy therefore yields the actual joint product `2pi V_K U_(K,M,L)`. Replacing the kernel by its individual-mode Legendre counterpart is a separately labeled norm calculation, not an asserted global interchange.

Combining (R4) with `|J_h|/sqrt(h)<<A^2 sqrt(N)/K` and summing the shift norms gives
\(U_{K,M}\ll A^2\sqrt N M^{1+\Theta+\epsilon}\).
For one continuous cusp its coefficient norm is `O(h^epsilon K^(1/2+epsilon))`, giving
\(U_{a,K,M}\ll A^2\sqrt N M^{1+\epsilon}K^{-1/2}\).
Both prices agree with claimant (18). On `K<=t<=2K`, ordinary Parseval gives only
\(\mathcal V_K\le e^{\pi K}\|\mathcal V\|_2\), not a polynomial weighted norm. The report correctly excludes the higher-dimensional theta-pairing bound from the new source.

Dividing the discrete raw certificate by `N^(3/2)` gives claimant (21). Its proposed `V_K<<N^(-Theta)` condition at `M~N` is expressly sufficient for that particular positive norm procedure; it is not asserted necessary for the signed target. A fixed-coefficient large sieve cannot absorb `h^(it_j)` or the remaining spectral-dependent amplitudes without a priced decomposition.

The final arithmetic fallback is independent of these unproved weighted norm entries. Actual coefficient triangle gives raw `A^2 N^(2+epsilon)`; the complete density costs `A^2 N^(3/2+epsilon) T^(-1) log(2N)`. The diagonal is `A^2 N^(1+epsilon)`, and the exact Fejer prefactor stays bounded. Consequently the shell modulus is `A N^(1/4+epsilon)`. Summing the complete partition, including the singleton and full original Schwartz tail beyond `P`, gives complex exponent `1/4` and physical exponent `3/8`. Conditional (F) would instead give complex exponent zero and physical quarter. The inherited real `beta` was not used for a complex block, and the separate inherited complex `13/56` cap is accurately described as prior evidence.

# 4. First doubtful or unproved step

No unresolved error was found in the reviewed identity, scalar estimates, source-bound application, or finite-truncation ledger. The first unproved complete arithmetic assertion is claimant (25), for the full finite spectral expression (24). Its quantitative tails are paid, so it has no hidden complementary shift or height range.

For the alternative termwise full Legendre expansion, the earlier interchange/weighted-pairing seam is explicitly unproved in this report. The ordinary Parseval statement, the fixed-mode transform, and the scalar stationary bound do not close it. The subsequent joint vector norm is also unproved. GREEN covers this accurate localization of the missing work; it supplies none of those estimates.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact target bytes | Assigned SHA256 verified before reading. |
| Source Fourier normalization | Same fixed level-four `sqrt(y) K` convention in both HKLDW sources; coefficient second moment independent of theta dimension. |
| Density and atom | Exact Mellin centering; finite atom retained; full atom zero. |
| All spectra | All three continuous cusps and cuspidal modes retained; constant treatment matches source. |
| Finite contour and height tails | Independent Cauchy/Stirling derivation above validates (7)--(8) without weighted Parseval. |
| Inverse transform powers | Independent calculation (R5)--(R6), plus constant-mode control. |
| Stationary phase | Exact locus, curvature, leading coefficient, phase, and both branch signs reproduced. |
| Empty/support endpoints | Smooth zero extension uniform; discrete-empty and continuous-empty cases remain distinct. |
| Weighted norm versus Parseval | Exponential renormalization visible and not silently bounded polynomially. |
| AH literal statement issues | Empty range/missing cutoff and Whittaker coefficient issue remain fenced; no repaired sieve imported. |
| Complete restoration | Full shift range, dyadic reconstruction, diagonal, singleton, tails, and real/complex distinction preserved. |
| Upper certificate versus actual value | No loss is used as a lower bound or actual no-go result. |
| Fixed moments/full quarter | No parent or quarter promotion; fixed-order alternatives remain open. |
| Experiments | None; source inspection and analytical/algebraic checks only. |

# 6. Dependencies and provenance

Reviewer is the author of the separately frozen `reports/heegner_joint_norm_audit.md`, SHA256 `cc921c6d04fb7015e68915000badffa82ff284734460e0be57b2260197443909`. This is a NONAUTHOR review of the different target report, not a fresh-context or statement-only review. My prior exact Legendre/Heegner derivation and source history were available; they are disclosed rather than claimed as blinded corroboration.

Current target: `rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/joint_shift_spectral_attack.md`, SHA256 `9df8afa574a54a6d9c7ca587030aeaec00a7daa345594d224116a93e823d3560`.

Prior authorized context: protocol, authoritative graph/manifest, Round227 frozen strategy and complete interface, the September23 strategy, closed226 checkpoint/source report/source review/synthesis, accepted complete-square-root moment kernel, proof-draft scope, and closed225 synthesis. Exact primary bindings are in Section 2. The new review source inspection of HKLDW1703.10347v3 was restricted to the assigned coefficient/polynomial-growth seam; no new mathematical theorem beyond the target's cited interfaces was introduced.

No current blind report, blind packet, sibling review, or conductor control was read. No frozen claimant or own-report byte was changed. The only file written in this review task is this assigned review.

# 7. Recommended state effect

Retain the claimant as **GREEN candidate evidence at the exact reviewed hash**, within its explicit no-new-bound scope. No repair requested.

No change to the authoritative graph, proof draft, exponents, moments, M1/M2/GAR/endpoints, or quarter claim. Claimant (25) remains unproved. Freeze this review at its externally reported final SHA256 and stop; only the conductor closes the round.
