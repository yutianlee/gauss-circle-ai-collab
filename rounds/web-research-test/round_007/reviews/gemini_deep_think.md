This is a Stage B cross review for Round 7.

### Most valuable input from others

The most valuable input from `gpt_pro_thinking` is the meticulous formalization of the normative dependency chain for the Vaaler residual: H5r-B $\implies$ H5r-F $\implies O_\epsilon(X^{1/4+\epsilon})$. By isolating the zero-mode contribution ($D/H_D \asymp X^{1/4}$) from the oscillatory nonzero modes, the agent correctly re-normalizes the conditional C1 diagnostic to an additive limit $P(X) \ll_\epsilon X^{\max(1/4, \theta)+\epsilon}$. This structural clarity prevents dangerous multiplicative scaling overshoots in future estimates and establishes the exact analytic minimum required by the positive-majorant Vaaler truncation. Additionally, the observation that the arbitrary-coefficient H5r-B target is structurally equivalent to a dyadic termwise $L^1$ estimate via duality perfectly crystallizes the analytic bottleneck: targeting arbitrary bounded coefficients appears to mathematically equate to discarding phase cancellation across the frequency variable $k$.

The most valuable input from `deepseek_api` is the definitive algebraic reconciliation of the odd-lattice Poisson formulations. By verifying that the two-coset representation (integer minus half-integer dual frequencies) and the alternating-sign representation ($(-1)^m$ coefficient) are mathematically identical up to parametrization, the agent removes representation ambiguity. Furthermore, the rigorous calculation of the derivative non-degeneracy condition for the shifted residual phases ($F_{2,1}(x)$ and $F_2(x)$) confirms that the H5r residual sums structurally reside within the known Bombieri-Iwaniec / Li-Yang reciprocal-sum phase class, anchoring the problem to known geometry.

### Claims that look correct

**The H5r Dependency Hierarchy:** The assertion by `gpt_pro_thinking` that H5r-B implies H5r-F via dyadic block decomposition and pointwise multiplication by bounded weights $\eta_{k,H_D}$ appears algebraically and logically sound. The deduction that arbitrary-coefficient H5r-B is essentially equivalent to dyadic termwise $L^1$ via duality is also correct and provides a crucial limitation on character-blind estimation techniques.

**The C1 Diagnostic Scaling:** The maximum scaling $\max(1/4, \theta)$ perfectly models the additive components of the Vaaler residual under the given hypotheses. Because the zero-mode evaluates to exactly $X^{1/4}$ and the oscillatory modes are bounded by $X^\theta$, the total error naturally scales additively rather than multiplicatively. This correction is mathematically robust.

**The Equivalence of C2 Representations:** The proof by `deepseek_api` linking the two-coset Poisson transform to the $(-1)^m$ formulation via the $d=2n+1$ substitution is flawless. This demonstrates that the parity dual factor is an intrinsic property of the B-process acting on $S_{\mathrm{odd}}$, rather than merely an artifact of Fourier convention.

**The Boundary Regime Breakdown:** Both agents correctly evaluate the stationary phase parameters, locating the stationary point at $u_0 \asymp \sqrt{kX/\ell}$ and determining the active dual length to be $\ell \asymp kX/D^2$. They correctly identify that for the critical endpoint block where $D \asymp X^{1/2}$ and $k \asymp 1$, the dual length drops to $\ell = O(1)$. Under these hypotheses, continuous B-process and uniform spacing lemmas fail unconditionally, as the integrals lack sufficient oscillation.

### Claims that need proof

**The H5r-F Analytic Escape Hypothesis:** Both agents suggest that H5r-F serves as the minimal target and might be easier to bound than H5r-B because it retains fixed, known Fejer coefficients $\eta_{k,H_D}$. However, the precise mechanism by which exponential sum techniques can exploit these slowly varying, monotonic Fejer coefficients to achieve a bound strictly stronger than arbitrary block sums requires explicit proof. As discussed below, Abel summation presents a significant hurdle to this hypothesis.

**Uniformity of Li-Yang Spacing for Shifted Phases:** `deepseek_api` applies the Li-Yang (2023) bounds directly to the phase $F_{2,1}(x) = 1/(x+1/D)$. While the derivative non-degeneracy condition formally holds for fixed parameters, robust proof is needed to show that the implicit spacing matrices in Bombieri-Iwaniec theories maintain uniform, non-degrading bounds as the geometric shift $1/D \asymp X^{-1/2}$ becomes microscopically small near the integration boundary.

**The Signed Fourier Truncation High-Frequency Tail:** `gpt_pro_thinking` lists signed Fourier truncation as a potential non-majorizing alternative (H10). Using this alternative would require showing that its high-frequency tail is either absolutely convergent or analytically bounded without reverting to absolute values. If absolute values are required to bound the tail, it would discard the $\chi_4$ character and recreate the exact Fejer trap we are trying to escape.

### Possible errors or hidden assumptions

**The Abel Summation (Monotonicity) Trap:** There appears to be a severe hidden assumption that H5r-F genuinely offers an analytic advantage over H5r-B. The Fejer weights $\eta_{k,H} = 1 - |k|/(H+1)$ are strictly decreasing and positive. By applying Abel summation (summation by parts), the Fejer sum transforms into a weighted average of partial sums. Consequently, bounding the Fejer sum appears to reduce to bounding the supremum of the partial sums. Because a partial sum is merely a special case of H5r-B evaluated with step-function coefficients, H5r-F seems structurally bottlenecked by the exact same exponent barrier as H5r-B for any character-blind method.

**The Two-Coset A-Process Fallacy:** `deepseek_api` posits that the two-coset formulation of C2 might survive an A-process (Weyl differencing) better than the $(-1)^m$ formulation. This appears to rely on a hidden assumption that cross-terms vanish cleanly. Squaring the two-coset sum yields $|\hat{F}(m) - \hat{F}(m-1/2)|^2$, which generates a cross-term $-2\Re(\hat{F}(m)\overline{\hat{F}(m-1/2)})$. Applying an A-process to this cross-term produces an amplitude modulation, but it does not inherently reconstruct an off-diagonal spacing advantage over standard integer-lattice divisor sums.

### Explicit Lemma Audits

$$\text{\bf Lemma Box 1: Summation-by-Parts Equivalence of H5r-F and H5r-B}$$

> **Status:** Proposed algebraic constraint.
> **Statement:** Let $\eta_{k,H} = 1 - k/(H+1)$ for $1 \le k \le H$. By summation by parts, the Fejer-weighted residual sum $\sum_{k=1}^H \eta_{k,H} S(k,D)$ is analytically bounded by the maximal partial sum $\sup_{K \le H} |\sum_{k=1}^K S(k,D)|$. This maximal partial sum exactly matches the structure of H5r-B with a step-function coefficient.
> **Significance:** Escaping the H5r-B barrier ($\theta^* \approx 0.314$) by appealing to H5r-F would require demonstrating that the Fejer weights induce a specific phase correlation not present in raw partial sums, which appears highly unlikely for character-blind estimates.

$$\text{\bf Lemma Box 2: Equivalence of Parity Dual Representations (C2)}$$

> **Status:** Proved algebraic identity.
> **Statement:** For $F(u) = w_D(u)e(kX/u)$, the two-coset formulation $\frac{1}{2}\sum_m [\widehat{F}(m) - \widehat{F}(m-1/2)]$ and the alternating sign formulation $\frac{1}{2}\sum_m (-1)^m \int F(u)e(-mu/2)du$ are exact algebraic equivalents under the substitution $d = 2n+1$. Any A-process parity collapse acting on the $(-1)^m$ coefficient necessarily manifests as an identical phase-interference obstruction in the two-coset model.

$$\text{\bf Lemma Box 3: Shifted-Phase Derivative Non-Degeneracy}$$

> **Status:** Proved arithmetic check.
> **Statement:** The phase $F_{2,1}(x) = 1/(x+1/D)$ for $x \asymp 1$ possesses derivatives satisfying the Bombieri-Iwaniec non-degeneracy condition $F'_{2,1}F'''_{2,1} - 3(F''_{2,1})^2 = -6(x+1/D)^{-6} \neq 0$.
> **Significance:** Consequently, the parity residual is not blocked by a vanishing continuous Hessian, embedding it firmly in the classical Dirichlet Divisor Problem spacing class. However, uniform bounds over the parameter $D$ must still be verified.

$$\text{\bf Lemma Box 4: Boundary Dual Length Degeneration}$$

> **Status:** Proved asymptotic limit.
> **Statement:** For the dyadic block $D \asymp X^{1/2}$ and frequencies $k \le c_0$, the dual Poisson variable $\ell \asymp kX/D^2$ satisfies $\ell = O(1)$.
> **Significance:** Under these hypotheses, the error term in the continuous stationary phase expansion fails to decay relative to the main term, requiring the problem to be estimated via exact discrete partial summation or primal exponent pairs in this specific boundary regime.

### Confidence calibration and failure modes

**Confidence: High** that the Vaaler residual bottleneck (H5r) structurally reduces to a known reciprocal-sum/divisor-problem barrier. The algebraic equivalence derivations are exact.
**Confidence: Low** that H5r-F provides an analytical escape route from the H5r-B limit. This is due to the monotonicity of the Fejer kernel under Abel summation, which suggests that fixed weights offer no deep cancellation advantage.
**Confidence: Low** that uniform continuous stationary phase arguments succeed without severe modification in the $D \asymp X^{1/2}$ boundary range.

The analytic route faces the following concrete failure modes:

1. **The Abel Summation Collapse (Failure Mode 1):** Any attempt to exploit H5r-F over H5r-B fails if summation-by-parts transforms the Fejer-weighted sum directly into an average of partial sums. If known technology cannot bound the raw partial sums (step-function bounded coefficients) below $X^{0.314}$, the Fejer sum definitively cannot reach the conjectural $X^{1/4}$ endpoint.
2. **The Short-Dual Boundary Obstruction (Failure Mode 2):** The proof skeleton relies heavily on dualizing the residual to exploit dual oscillation. If $D \asymp X^{1/2}$ and $k \asymp 1$, the dual phase is non-oscillatory ($\ell \asymp 1$). The dual method provides no statistical cancellation here, forcing a fallback to trivial primal bounds which may unconditionally exceed $X^{1/4+\epsilon}$.
3. **Parameter-Shift Spacing Degeneration (Failure Mode 3):** The Bombieri-Iwaniec spacing lemma bounds rational points near the curve $y = F'(x)$. For $F_{2,1}(x) = 1/(x+1/D)$, the curve geometry depends strongly on $D$. If the rational curvature bounds degrade as the shift $1/D$ alters the domain, the quoted $\theta^* \approx 0.314$ may not be uniformly attainable across all dyadic blocks, potentially pulling the exponent even higher.

### Concrete counterexample or stress-test checks

1. **Abel Summation Monotonicity Verification (Symbolic/Numerical):**
Compute the exact discrete Fejer residual $R_F = \left| \frac{1}{H_D} \sum_{k=1}^{H_D} \eta_{k, H_D} S_{\mathrm{odd}}(k, D) \right|$ for $X=1000, D=30$. Compare this to the partial sum supremum $R_P = \max_{1 \le K \le H_D} \left| \frac{1}{K} \sum_{k=1}^K S_{\mathrm{odd}}(k, D) \right|$. Check whether $R_F \asymp R_P$ uniformly over a range of parameter values. If they scale identically, it empirically validates Lemma Box 1 and suggests that fixed Fejer weights offer no analytic salvation over arbitrary step weights.
2. **Boundary Phase Integral Evaluation:**
Numerically integrate $I_m = \int_{D/2}^{2D} w_D(u) e(X/(2u^2) - mu/2) du$ for $X=100, D=10, k=1, m=-1, -2$. Compare the exact numerical integral against the $D^{3/2}/(kX)^{1/2}$ stationary phase prediction. This will accurately measure the precise magnitude of the asymptotic breakdown where the dual length $\ell \asymp 1$, verifying the severity of Failure Mode 2.

### Suggested synthesis

The Round 7 outputs provide a complete and rigorous map of the Vaaler residual bottleneck. The arithmetic route is fully reduced to evaluating shifted reciprocal sums (H5r) that belong structurally to the Li-Yang phase class. Because summation-by-parts forces H5r-F to be bounded by the maximum of partial sums, the positive-majorant Vaaler route appears to offer no cancellation advantage over arbitrary step-coefficients, leaving it strictly stalled at the Dirichlet Divisor Problem barrier ($\theta^* \approx 0.31448$).

The synthesis should formalize the equivalence of H5r-F and H5r-B (via Abel summation) as a diagnostic lemma to prevent circular attempts to bound the Fejer majorant. The repository state must explicitly recognize that the positive-majorant Vaaler-based arithmetic route is analytically bottlenecked at current technology levels.

For the next round, the research effort should pivot aggressively to the non-majorizing alternatives (H10). We must explicitly formulate the Mellin-Perron contour integrals and functional equations for $4\zeta(s)L(s, \chi_4)$ to determine whether their resulting Voronoi error terms retain the arithmetic $\chi_4$ character or suffer the same positive-majorant sign-degeneration.

### Score by agent

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
| --- | --- | --- | --- |
| `gpt_pro_thinking` | 9 | Superb logical stratification of H5r-B vs H5r-F, precise isolation of the zero mode, and accurate additive correction of the C1 scaling. | Evaluate the high-frequency tail of signed Fourier truncation explicitly to check absolute convergence. |
| `deepseek_api` | 9 | Flawless algebraic reconciliation of the C2 Poisson representations and rigorous validation of derivative non-degeneracy for shifted reciprocal phases. | Check if the two-coset cross-terms genuinely evade the A-process parity collapse or simply modulate the amplitude. |

### Next-round recommendation

1. **For `gpt_pro_thinking`:** Formalize the "Abel Summation Equivalence" (Lemma Box 1), demonstrating that H5r-F appears analytically trapped by the bounds on H5r-B partial sums. Then, shift focus to H10: specify the exact high-frequency tail of a sign-preserving Fourier truncation and verify if it can be bounded without taking absolute values.
2. **For `deepseek_api`:** Investigate the boundary regime $D \asymp X^{1/2}, k \asymp 1$ where the dual length is $O(1)$. Determine if standard one-dimensional exponent pairs applied directly to the primal sum can theoretically satisfy $3\kappa + 2\lambda \le 1$ to bypass the stationary phase breakdown.
3. **For `gemini_deep_think` (Self-Correction/Next Steps):** Fully develop the Mellin-Perron contour approach. Write out the exact shifted contour, the residues, and the Voronoi-style functional equation for $4\zeta(s)L(s,\chi_4)$ to see if the oscillating $\chi_4$ sign survives truncation and contour shifting, or if it reverts to a classical Bessel obstruction.
