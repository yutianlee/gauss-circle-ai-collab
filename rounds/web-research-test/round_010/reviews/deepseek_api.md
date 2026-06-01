### Stage B Cross Review: Round 10 -- DeepSeek API Referee Report

**Author:** DeepSeek API (acting as algebra checker, obstruction auditor, and cross-reviewer)
**Date:** 2026-06-01 (Round 10)

---

## 1. Introduction and Scope

This review evaluates the Stage A reasoning artifacts produced by **`gpt_pro_thinking`** and **`gemini_deep_think`** for Round 10. Both outputs are assessed from the perspective of mathematical soundness, hidden assumptions, and the reliability of diagnostic arguments. The review does **not** generate new Stage A content or a judge synthesis; it is a strict cross-review according to the protocol's Stage B schema.

The Round 9 state conditionally cleared the fixed-Fejer Vaaler residual via the product-counting bound `R5` and shifted the analytic burden to the fixed-coefficient main sums `M9`. The two Stage A outputs build on that foundation.

The remainder of this report contains:

- Individual detailed assessments of each agent's output,
- A synthesis of complementary insights,
- Explicit correction/verification items (≥ 6),
- Identified failure modes (≥ 4),
- Concrete stress tests (≥ 3),
- A score table for each other active agent,
- A dedicated "Confidence calibration and failure modes" section,
- A concise next-round recommendation.

---

## 2. Assessment of `gpt_pro_thinking`'s Output

### 2.1 Most Valuable Contributions

The gpt output provides a **rigorous, self-contained reduction** that advances the research state in several concrete ways:

1. **Explicit Vaaler theorem (`H4`)**
   The coefficient function
$$
   \alpha_{h,H}= -\frac{\Phi\bigl(h/(H+1)\bigr)}{2\pi i h},\qquad
   \Phi(u)=\pi u(1-|u|)\cot(\pi u)+|u|,
$$
   together with the residual majorant
$$
   |R_H(t)|\le \frac{1}{2H+2}K_H(t)
$$
   is the most precise formulation of `H4` seen so far. This resolves a long-standing ambiguity about the exact Vaaler coefficients and provides a clear target for the required source audit.

2. **Complete `R5` proof with the second leg**
   The product-counting argument for the shifted second-leg Fejer residuals
$$
   \frac1H\sum_{d\sim D}K_H\!\left(\frac{X/d+\rho}{4}\right),\qquad \rho\in\{1,3\},
$$
   is handled by introducing the integer \(\ell=4m-\rho\) and grouping by \(n=d\ell\). The use of the divisor bound \(\tau(n)\ll_\epsilon n^\epsilon\) is clean and handles the congruence restriction effortlessly. Together with the first-leg proof, this strongly supports the conditional clearance of `H5r-F`.

3. **Shift from arbitrary-coefficient to fixed-coefficient main targets**
   The over-strong arbitrary-coefficient dyadic targets `H5a`/`H5b` are correctly demoted. The new targets
$$
   \mathcal M_1(D;X)=\sum_{1\le|h|\le H_D}\alpha_{h,H_D}\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$
$$
   \mathcal M_2(D;X)=\sum_{1\le|h|\le H_D}\alpha_{h,H_D}\chi_4(h)\sum_{d\sim D}w_D(d)e(hX/(4d)),
$$
   are identified as the genuine remaining analytic obstacles. This honest reduction avoids imposing unnecessary strength on future estimates.

4. **Li--Yang comparison with precise gaps**
   The output distinguishes structural phase compatibility from theorem-level applicability. It records the raw-endpoint mismatch (Case A height \(H\le X^{33/164}\) vs. required \(X^{1/4}\)) and flags the shifted-frequency issue for `H5b-fix` as a theorem-extension gap.

### 2.2 Claims That Look Correct

- The Fejer kernel pointwise bound \(K_H(t)\ll \min\bigl(H,1/(H\|t\|^2)\bigr)\) is standard and correctly applied.
- The estimate \(\sum_{n\in\mathbb Z}\min\bigl(1,\Delta^2/|X-n|^2\bigr)\ll \Delta+1\) is elementary and valid for all real \(X\).
- The zero-mode contribution \(D/H_D\asymp X^{1/4}\) is properly accounted for.
- The handling of short blocks \(D<X^{1/4}\) via trivial bounds is safe and adds only a harmless \(O(X^{1/4})\) term.
- The overall conditional implication
$$
  \text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}\Longrightarrow P(X)\ll_\epsilon X^{1/4+\epsilon}
$$
  is logically sound if each component is proved.

### 2.3 Claims That Need Proof

- **`H4` normalization** -- The exact constant \(\frac{1}{2H+2}\) and the formula for \(\Phi(u)\) must be verified against a primary source (Vaaler 1985 or a trusted modern exposition). The behaviour at integers (\(\psi(n)=-1/2\)) must be shown to be absorbed by the residual; this is plausible but should be checked explicitly.
- **`R5` second-leg rounding** -- An explicit inequality showing that the constructed \(\ell\) satisfies \(|X-d\ell|\le 2D/H\) (or similar) would remove any lingering doubt about the grouping argument.
- **`H5b-fix` as a valid Bombieri--Iwaniec object** -- The claim that a fixed fractional shift \(\beta\) in the phase \(e((h+\beta)X/d)\) can be handled without new hypotheses is plausible but unproven. It should be added as a pending gap.
- **Full `R5-Full` dyadic summation** -- The bridging lemma is mechanically straightforward, but a complete write-up with explicit constants and covering both signs of \(k\) would solidify confidence.

### 2.4 Possible Errors or Hidden Assumptions

- The nearest-integer choice for the second leg could in principle give \(\ell=0\) or negative for very small \(X/d\), but in the relevant range \(d\gg 1\) this does not happen. No fatal error.
- The product grouping uses the divisor bound on \(n=d\ell\); because \(\ell\) is unconstrained modulo the congruence class, the bound \(\tau(n)\) is still an upper bound for the number of representations. This is safe but a brief justification would be helpful.
- The residual is bounded via the absolute value of \(w_D\); since the Fejer majorant is already non-negative, no sign cancellation is lost. The argument is internally consistent.

---

## 3. Assessment of `gemini_deep_think`'s Output

### 3.1 Most Valuable Contributions

Gemini's output operates as an **obstacle finder** and supplies a set of sharp diagnostic lemmas that complement the forward-looking reduction of gpt:

1. **`Q1-Spectral` -- Spectral Norm Character Blindness**
   The argument that applying Cauchy--Schwarz over the outer \(h\)-sum in a standard Bombieri--Iwaniec framework leads to a quadratic form \(v^*Kv\) whose bound via the spectral norm is invariant under unitary multiplication of the test vector by \(\operatorname{diag}(\chi_4(d))\) is a mathematically clean statement. It explains why generic large-sieve estimates cannot exploit the character sign -- a crucial diagnostic.

2. **Li--Yang Parameter Mismatch Table**
   The tabular audit of the Li--Yang Te X source, listing the specific mismatches (exponent \(\theta^*\) vs. \(1/4\), height constraints, bounded-variation requirements), is directly useful for the repository's gap register.

3. **`C3-Affine` / `C3-Rational` -- Parity Collapse / Survival**
   The algebraic analysis of the two-coset parity coefficient \(\sigma(\xi)=\frac12(-1)^{2\xi}\) under translation and rational affine transformations is precise. The conclusion that even-fractional dilations can preserve parity oscillation, while integer translations destroy it, is a valuable addition to the `C2`/`C3` diagnostic set.

4. **`H10-Dual` -- Mellin--Perron Isomorphism**
   The derivation of the exact functional equation for \(Z(s)=4\zeta(s)L(s,\chi_4)\) and the subsequent stationary-phase calculation, leading to dual length \(N\asymp X^{1/2}\) and phase \(2\pi\sqrt{nX}\), is a rigorous (modulo error-term control) demonstration that the contour method reconstructs the classical Hardy--Voronoi--Bessel structure. This confirms that the Mellin--Perron route is not a genuine escape.

### 3.2 Claims That Look Correct

- The algebraic computation of \(\chi_4(d_1)\chi_4(d_2)\) for near-collisions (`Q1-Ext`) is correct.
- The parity collapse lemma `C3-Affine` is elementary and correctly shows that integer translation yields a constant sign product.
- The arithmetic of `C3-Rational` is sound: for \(\xi_2=\frac{a}{b}\xi_1\) with \(a\) even, \(b\) odd, the product \(\sigma(\xi_1)\sigma(\xi_2)\) retains the parity of \(\xi_1\).
- The Li--Yang Case A/B inequalities are accurately extracted from the arXiv source.
- The positioning of the Mellin--Perron route as a comparative dictionary rather than a solution is appropriate.

### 3.3 Claims That Need Proof

- **`Q1-Spectral`'s full applicability** -- The argument assumes that the standard Bombieri--Iwaniec method bounds the quadratic form by \(\|K\|_{\text{op}}\) and that this norm is invariant under the unitary transformation. The exact matrix \(K\) and the specific large-sieve inequality must be identified. In many treatments, the bound already takes absolute values of the coefficients, making the character-blindness immediate; the unitary-invariance proof is then an elaboration rather than an essential step. The claim should be refined to avoid overstatement.
- **Signed Fourier truncation tail equivalence** -- The assertion that the signed tail bound reverts to the Fejer kernel majorant via Abel summation is only heuristic. The bound \(|\sum_{|h|>H} h^{-1}e(ht)|\ll 1/(H\|t\|)\) is standard, but the squared distance in the Fejer majorant is of a different shape. The precise relationship should be clarified; as it stands, the equivalence is not proved.
- **Mellin--Perron stationary-phase uniformity** -- The derivation uses Stirling's approximation for the Gamma ratio; the error terms (typically \(O(|t|^{-1})\)) need to be controlled uniformly for \(t\) up to \(X^{3/4}\) and \(n\) up to \(X^{1/2}\) to confirm that the saddle point dominates and no hidden polynomial factors spoil the dual-length bound.

### 3.4 Possible Errors or Hidden Assumptions

- The claim that the contour from \(X^{1/2}\) to \(X^{3/4}\) is "devoid of saddle points" is an oversimplification. The saddle point \(t_0=\pi\sqrt{nX}\) moves with \(n\); for \(n\) near \(X^{1/2}\), \(t_0\) is near \(\pi X^{3/4}\), i.e. inside the integration range. Contributions from near-saddle regions could be significant. The conclusion that the dual sum length is at most \(X^{1/2}\) is robust, but the language should be tempered.
- The parity survival lemma `C3-Rational` is algebraically correct; however, the crucial step of realizing the fractional dilation as a spacing relation in the actual Poisson-dual sum is not shown. The lemma is therefore a model-level diagnostic, not a guarantee of practical utility.
- The term "unconditionally" used in several lemmas (e.g., "unconditionally erase") is too strong; the arguments are conditional on the use of certain standard bounding techniques.

---

## 4. Synthesis and Complementarity

The two outputs are highly complementary. gpt *proves* the residual bound and **precisely isolates** the remaining fixed-coefficient main sums. Gemini *diagnoses* why standard analytic machinery will be blind to the character and why alternative routes (Mellin--Perron, signed Fourier) do not circumvent the core difficulty.

The united picture:

- The Fejer residual is provisionally controlled (conditional on a routine Vaaler citation).
- The official remaining targets are the fixed-coefficient sums `M9`.
- Standard double large sieve / spacing-matrix estimates will be **character-blind** (as argued by `Q1-Spectral`) unless a trace-cycle or fourth-moment method that preserves the cyclic product of character signs is developed.
- Current Li--Yang technology cannot cover the endpoint Vaaler height, leaving an explicit high-frequency gap.
- The Mellin--Perron route is structurally equivalent to the Poisson--Bessel route and offers no new path.

The repository's proof skeleton now has a clearly isolated open problem: prove the fixed-coefficient main-term bounds `M9`, ideally by a method that exploits the exact Vaaler coefficients \(\alpha_{h,H_D}\) and the arithmetic character \(\chi_4\).

---

## 5. Detailed Correction and Verification Items

1. **Vaaler theorem reference (`H4`)** -- The exact formula for \(\alpha_{h,H}\) and the constant \(\frac{1}{2H+2}\) must be verified against Vaaler's original paper or a trusted exposition. The floor-compatible value \(\psi(n)=-1/2\) must be checked to be covered by the residual.

2. **`R5` second-leg integer congruence** -- Provide an explicit bound \(|X-d\ell|\le 2D/H\) (or similar) to justify the rounding and product grouping.

3. **`Q1-Spectral` unitary-invariance step** -- Identify the exact large-sieve inequality used in the Bombieri--Iwaniec framework. Show whether it already involves absolute values of the coefficients; if so, the character-blindness is immediate and the unitary-invariance argument is an unnecessary embellishment.

4. **`H5b-fix` fractional shift extension** -- Either prove that the Bombieri--Iwaniec method tolerates a non-integer constant shift \((h+\beta)X/d\) without degrading the exponent, or explicitly label this as a pending gap.

5. **Mellin--Perron stationary-phase error control** -- Formulate a lemma (`H10-SP-Uniform`) that bounds the error from Stirling's approximation uniformly over the relevant parameter regime, confirming that the saddle-point contribution indeed dominates.

6. **Signed Fourier tail bound precision** -- Upgrade the Abel-summation estimate to a clear statement of the form

$$
   \Bigl|\sum_{|h|>H}\frac{e(ht)}{h}\Bigr| \le \frac{C}{H\|t\|},
$$

   and then show how the sum over \(d\) compares to the Fejer residual. Clarify that the bound does not *prove* equivalence, but that the difficulty is of the same type.

7. **C2/C3 convention reconciliation** -- Ensure that the Fourier and Poisson sign conventions used in the C3 lemmas match those in the official `C2-Alg` lemma.

8. **Numerical stress-test execution** -- Both agents propose numerical tests; the repo should commit to a concrete test framework (e.g., Python scripts) and publish results. The absence of numerical data is itself a methodological gap.

---

## 6. Identified Failure Modes

1. **Fejer residual underestimation for divisor-rich \(n\)** -- The R5 proof relies on the divisor bound \(\tau(n)\ll_\epsilon n^\epsilon\). While this is asymptotically correct, the implied constant could be large for moderate \(X\). This risk is standard and usually absorbed into the \(\epsilon\) exponent, but it should be noted.

2. **Loss of character sign through Cauchy--Schwarz** -- If the proof of `M9` applies Cauchy--Schwarz over the \(h\)-variable (as in typical Bombieri--Iwaniec), the sign pattern of \(\alpha_h\) and \(\chi_4\) is irretrievably lost. This failure mode is what `Q1-Spectral` diagnoses; it blocks a direct general-coefficient route.

3. **Unbridgeable Li--Yang height gap** -- If the current first-spacing (decoupling) technology cannot push the allowable height beyond \(H\lesssim MT^{-0.314...}\), then no amount of dissection within the Li--Yang framework will reach \(H\asymp MT^{-1/4}\). This would prevent reaching the conjectural exponent via that route.

4. **Mellin--Perron actually reconstructs the classical bound** -- If the functional-equation and stationary-phase analysis is made rigorous, it may show that the dual sum after contour shift is exactly the Poisson--Bessel series, which itself only gives an exponent \(\gg 1/2\) under trivial estimates. In that case the Mellin--Perron route is not only not an escape, but is provably worse.

---

## 7. Proposed Stress Tests

1. **R5 numerical test for squares and near-squares** -- For \(X = 10^6, 10^7\), compute
$$
   \frac1{H_D}\sum_{d\sim D} K_{H_D}(X/d),\qquad D=\lfloor X^{1/2}\rfloor,
$$
   and compare with \(C X^{1/4}\). Test near-square values \(X = n^2\pm 1\) as well.

2. **Spectral norm invariance test** -- Build a small-scale model of the spacing matrix \(K_{d_1,d_2} = \sum_{h=1}^{H} e(h\alpha(1/d_1-1/d_2))\) and compute its spectral norm with and without a diagonal sign matrix \(U=\operatorname{diag}(\chi_4(d))\). Numerically verify whether the norms coincide; if they do, the character-blindness claim is supported.

3. **Parity survival in two-coset Poisson transform** -- For a compactly supported test weight, compute numerically both the alternating-sum representation and the two-coset representation of `C2`. Then apply integer translation differencing and examine whether any parity oscillation persists in the phase after the coefficient collapse.

4. **Mellin--Perron truncation error test** -- For a moderate \(X\), evaluate the Perron integral with a sharp cutoff at \(T=cX^{3/4}\) and compare the error with the conjectural \(X^{1/4}\) scale.

---

## 8. Score by Agent

| Agent reviewed       | Score (0-10) | Main reason | Must verify next |
|----------------------|:-----------:|-------------|------------------|
| **`gpt_pro_thinking`** | 8           | Clear, rigorous reduction; explicit `R5` proof correctly clears the Fejer residual; accurately isolates the fixed-coefficient main targets; provides a careful Li--Yang audit with identified gaps. | Vaaler theorem source verification (`H4`); `R5` second-leg rounding details; `H5b-fix` fractional shift extension. |
| **`gemini_deep_think`** | 7           | Valuable diagnostic obstacles (`Q1-Spectral`, `C3-Affine`/`Rational`, Li--Yang mismatch table) that sharpen the obstruction map; some claims are overstrong and need more precise support (e.g., "unconditional erasure", Mellin--Perron isomorphism). | `Q1-Spectral` unitary invariance under the actual matrix; Mellin--Perron stationary-phase error uniformity; `C3-Rational` mapping realizability. |

---

## 9. Confidence Calibration and Failure Modes

**Confidence in the selected route:**
The balanced arithmetic hyperbola/Vaaler route remains the most transparent reduction framework. The Fejer residual is now controlled to a high degree of confidence, conditional only on a routine Vaaler theorem citation. The main unresolved difficulty is the fixed-coefficient main sums `M9`; all diagnostic evidence indicates that standard Bombieri--Iwaniec/Li--Yang methods cannot reach the endpoint without new input, and that the Mellin--Perron and signed-Fourier alternatives are not genuine bypasses.

**Failure mode analysis:**

- **R5 residual under-estimation:** The product-counting argument is classic and robust; the risk of a mistake is low. The divisor-function bound is unconditional, and the grouping is sound.
- **M9 main-term obstacle:** The greatest risk is that no method can exploit the fixed Vaaler coefficients to gain the needed cancellation. The `Q1-Spectral` barrier indicates that any approach that first applies Cauchy--Schwarz over \(h\) will lose the character. A different decomposition (e.g., completing the \(h\)-sum before applying the large sieve, or using signed large sieve / trace methods) would be required, but such techniques are not yet available in the repository. The route may stall indefinitely at `M9`.
- **Li--Yang gap:** Even if a signed large sieve is developed, the current spacing bounds may still restrict the allowable height below \(X^{1/4}\). The high-frequency gap is a concrete parameter range where existing first-spacing estimates are insufficient; a new decoupling or spacing estimate would be needed.
- **Misapplication of the Vaaler residual:** The proof draft must retain the Fejer residual as a separate target; any future attempt to discard it as a scalar would be a fatal error. The present `R5-Full` lemma should prevent this, but the repository must enforce its inclusion.

**Overall confidence in current progress:**
High that the residual bottleneck is cleared; moderate that the remaining analytic targets are correctly identified; low that the main-term estimates can be proved with current technology. **No exponent improvement has been achieved.**

---

## 10. Next-Round Recommendation

1. **Solidify `H4` and `R5-Full`:** Verify the Vaaler theorem from a primary source and incorporate `R5-Full` into the best proof draft as a proved conditional lemma. This will officially move the residual off the critical path.

2. **Investigate sign-preserving strategies for `M9`:** Avoid premature Cauchy--Schwarz over the frequency variable. Explore partial summation over \(h\) using the specific \(\alpha_h\), or attempt a completion over \(h\) to create a different type of exponential sum before applying large-sieve or spacing arguments.

3. **Develop a signed large-sieve or trace-cycle model:** Gemini's suggestion of evaluating \(\operatorname{Tr}((KK^*)^2)\) to capture cyclic character products is a promising theoretical escape route. The next round could begin formulating a concrete lemma (e.g., `H12`) that expresses such a trace in terms of sums over \(\Delta\) with the `Q1-Ext` sign factors, and then investigate bounding that sum without absolute values.

4. **Audit Li--Yang's first-spacing dependencies systematically:** With the high-frequency gap identified, check exactly what parameter ranges in the small-cap decoupling theorem would need to improve to allow \(H\) up to \(X^{1/4}\). This will determine whether the gap is bridgeable with a refined first-spacing estimate or requires a fundamentally new idea.

5. **Run the planned numerical tests:** Execute the stress tests proposed by both agents and append the results to the gap register. Empirical evidence will anchor the theoretical claims.

---

*End of Stage B Cross Review.*
