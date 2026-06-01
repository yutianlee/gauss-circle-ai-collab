# Stage B Cross Review -- Round 8

This review examines the Stage A outputs of `gpt_pro_thinking` and `gemini_deep_think`, the two active agents in Round 8. Both contributions operate within the selected arithmetic-hyperbola/Vaaler reduction framework and address the central residual bottleneck H5r-F. No exponent improvement is claimed; the outputs sharpen the diagnostic map and propose algebraic tools.

The report is organised as follows:

1. Detailed assessment of each agent's output
2. Most valuable contributions
3. Claims that look correct
4. Claims that need proof
5. Possible errors and hidden assumptions
6. Suggested synthesis
7. Score table
8. Correction/verification items (6 explicit)
9. Stress tests (3 explicit)
10. Failure modes (4 explicit)
11. Dedicated confidence-calibration and failure-modes section
12. Next-round recommendations

---

## 1. Detailed Assessment of `gpt_pro_thinking`

### 1.1 Norm hierarchy for the Vaaler residual (H5r-F / B / L1)
The agent correctly isolates three analytic targets for the Fejer-residual families:

* **H5r-F:**
  \[
  \Bigl|\frac{1}{H_D}\sum_{1\le|k|\le H_D}\eta_{k,H_D}S_{\star}(k,D)\Bigr|
  \ll_{\varepsilon} X^{1/4+\varepsilon},
  \qquad \eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
  \]
* **H5r-B:** for all dyadic \(K_0\le H_D\) and \(|v_k|\le1\),
  \[
  \sum_{k\sim K_0}v_k S_{\star}(k,D)\ll_{\varepsilon} K_0 X^{1/4+\varepsilon}.
  \]
* **H5r-L1:** the termwise \(L^1\) average
  \[
  \frac1{H_D}\sum_{1\le|k|\le H_D}|S_{\star}(k,D)|\ll_{\varepsilon} X^{1/4+\varepsilon}.
  \]

The implication chain

\[
\mathrm{H5r{\text-}B}\;\Longrightarrow\;\mathrm{H5r{\text-}F}\;\Longrightarrow\;
\text{Vaaler residual}\ll_{\varepsilon} X^{1/4+\varepsilon}
\]

is correctly established (R1--R3) and the equivalence H5r-B = (dyadic) \(L^1\) control for complex coefficients is a valuable observation.

### 1.2 Abel-summation diagnostic (R4)
For one sign of \(k\) let \(A(t)=\sum_{1\le k\le t}S_{\star}(k,D)\). The agent writes

\[
\sum_{k=1}^{H}\eta_k S_{\star} = \frac{1}{H+1}A(H)+\frac{1}{H+1}\sum_{t=1}^{H-1}A(t).
\]

This is algebraically correct for real or complex \(S_{\star}\) because it is a purely algebraic rearrangement (no absolute values until the final inequality). The two-sided case can be handled by symmetry (the Fejer kernel is even), but the agent omits the explicit extension; a fully rigorous version should verify that the same manipulation works for the negative-\(k\) half and the combined sum.

The diagnostic value is clear: if one proves H5r-F by bounding partial sums \(A(t)\) with a uniform exponent, the feature of fixed Fejer weights is not actually exploited. The lemma does **not** prove equivalence of H5r-F and H5r-B; it only says that a bound on partial sums is sufficient (and therefore a proof that relies only on such bounds does nothing special).

**Recommendation:** Promote R4 to a **verified diagnostic lemma** after completing the two-sided version and including an explicit warning that the inequality does **not** force H5r-F to be as difficult as H5r-B; it only exposes the kind of proof that would not exploit the Fejer structure.

### 1.3 Signed Fourier truncation
The formal representation

\[
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi ih}
\]

is used to write a signed high-frequency tail \(\mathcal T_1(D),\mathcal T_2(D)\) that formally retains \(\chi_4\). The agent correctly notes that this series is not absolutely convergent and that a naive absolute-value tail bound would diverge. However, the write-up still presents the signed truncation as a plausible alternative and says it "preserves \(\chi_4\) better than Vaaler at the formal algebraic level".

**Serious gap:** Without a summability method (e.g. a smoothing kernel) the truncated series is not a legitimate representation of \(\psi\) near discontinuities, and any rigorous completion will introduce an error term that may well be controlled by a positive majorant -- exactly the object the agent wishes to avoid. Until a concrete, non-majorising truncation with a provable endpoint tail estimate is supplied, signed truncation must be recorded as **not a valid lemma**.

### 1.4 Poisson--Bessel calibration
The derivation of

\[
E(R)\ll R\delta+R^{1/2}\delta^{-1/2},\qquad
\delta=R^{-1/3}\;\Rightarrow\;E(R)\ll R^{2/3},
\]

is standard and correctly executed. The smoothing sandwich, Fourier transform of the disk, Bessel bound \(J_1(t)\ll t^{-1/2}\), and the radial lattice-sum estimate are properly invoked. This module is a useful secondary sanity check.

### 1.5 Other observations
* The Vaaler majorant constant \((2H+2)^{-1}\) is used without a bibliographic reference; this must be checked against a standard source.
* The sufficiency proof R1 is sketched but not fully detailed; it needs explicit summation over all dyadic \(D\), both residual families, both signs of \(k\), and the \(1/(2H+2)\) prefactor.

---

## 2. Detailed Assessment of `gemini_deep_think`

### 2.1 Near-collision character factorization (Q1-Ext)

The lemma states:

> Let \(a,b\) be coprime positive integers, \(d_1,d_2\) odd integers with \(d_1b-d_2a=\Delta\). Then
> * If \(a,b\) both odd, \(\Delta\) is even and \(\displaystyle \chi_4(d_1)\chi_4(d_2) = \chi_4(ab)\,(-1)^{\Delta/2}\).
> * If \(a\) even, \(b\) odd, then \(d_1\equiv b(a+\Delta)\pmod4\) is frozen; thus \(\chi_4(d_1)\) is constant and the product tracks \(\pm\chi_4(d_2)\).
> * The symmetric case follows.

**Algebraic verification:**
The step \(d_1b \equiv d_2a+\Delta\pmod4\), multiply by \(b\) (since \(b^2\equiv1\)): \(d_1\equiv d_2ab+\Delta b\). Multiply by \(d_2\): \(d_1d_2\equiv d_2^2 ab + \Delta b d_2\). Because \(d_2\) is odd, \(d_2^2\equiv1\). Because \(\Delta\) is even, \(\Delta b d_2\equiv\Delta\) (since an even number times an odd integer stays the same modulo 4). Hence \(d_1d_2\equiv ab+\Delta\pmod4\).
Using \(\chi_4(n+2k)=(-1)^k\chi_4(n)\) (valid because \(\chi_4\) is primitive mod 4), one obtains the stated factorisation. The even/odd cases are handled by similar residue-freezing arguments, all of which are exact.

**Value:** The lemma shows that \(\chi_4\) never behaves as random noise on near-collision rays; it is either constant or strictly alternating. This can be exploited in signed Bombieri--Iwaniec spacing matrices.

**Caveat:** The lemma only deals with the product of characters; it does **not** incorporate the smooth weights \(w_D\) or the phase factors \(e(kX/d)\). Whether the alternating sign survives subsequent matrix norms (e.g. a double-large-sieve estimate) depends on whether the method can preserve the sign before taking absolute values. The claim "proves that Bombieri--Iwaniec ... naturally preserve the character" is too strong -- it is a **necessary algebraic input**, not a **sufficient estimate**.

### 2.2 Two-coset parity collapse (C3-Ext)

The agent writes the odd-lattice dual as

\[
\sum_{\xi\in\frac12\mathbb Z} \sigma(\xi) I(\xi),\qquad
\sigma(\xi)=\tfrac12(-1)^{2\xi},
\]

and considers a translation \(q=\xi_1-\xi_2\). The product \(\sigma(\xi_1)\sigma(\xi_2)\) simplifies to \(\frac14(-1)^{2q}\), independent of \(\xi_2\). Hence, under a translation-invariant A-process, the coefficient-level alternating sign factors out, and the internal summation variable carries no parity oscillation.

**Assessment:** The algebra is flawless. The conclusion that **translation-invariant differencing strips the parity sign** is therefore proved for the coefficient part. However, the agent's phrasing ("ends the debate on two-coset spacing") overshoots.

* The conclusion only applies to **translation-invariant** A-process methods; multiplicative shifts, spectral large-sieve methods, or non-translation-based differencing may behave differently.
* Even without the parity sign, the phase \(I(\xi)\) retains non-degenerate oscillation (its derivative does not vanish), so spacing information can still exist. The lemma only eliminates the parity **coefficient**; it does **not** prove that the whole sum becomes character-blind.

**Recommendation:** Downgrade C3-Ext from "obstruction" to **"translation-invariant parity-collapse diagnostic"**, and explicitly state the limits.

### 2.3 Mellin--Perron mapping (H10-A, H10-B)

**H10-A:** The agent claims that sharp Perron truncation requires \(T\asymp X^{3/4}\) to obtain an error \(\ll X^{1/4+\varepsilon}\). This scaling is a heuristic based on the standard error term \(O(X^c/T)\) (with \(c\) near 1) plus bounds for horizontal segments. It is plausible but not proved here; the agent labels it a "proved conditional reduction" but provides no proof.
**H10-B:** By shifting the contour to \(\Re(s)=-1/2\) and applying the functional equation of \(4\zeta(s)L(s,\chi_4)\), the agent claims that the resulting oscillatory integral reconstructs exactly the phase \(\sqrt{Xhd}\), thereby mapping the Perron route onto the Hessian-degenerate B-process phase (H9). This is labelled a "proved diagnostic mapping", but the derivation is entirely heuristic: no explicit treatment of the gamma-function asymptotics, the cross-terms from the functional equation, or the incomplete integration near the truncation height is given.

**Assessment:** The qualitative picture (Perron → Voronoi → square-root phase) is plausible and consistent with classical Voronoi summation. However, H10-A and H10-B should be re-classified as **proposed diagnostic lemmas** -- they are **not yet theorems** because the rigorous derivation is missing.

### 2.4 Overclaims and language
In line with the guardrails established in earlier rounds, the following phrases need correction:

* "proves that Bombieri--Iwaniec rational spacing matrices naturally preserve the character" → "provides an exact algebraic description of the character product on collision rays, which can be used to construct signed spacing estimates."
* "ends the debate on two-coset spacing" → "demonstrates that translation-invariant A-process eliminates the parity sign from the summation variable; spacing information may still reside in the geometric phase."
* "Mellin--Perron ... acts as an analytic isomorphism, not a geometric bypass" → the isomorphism direction is plausible, but the wording should stress that the mapping is at the heuristic/asymptotic level until a complete theorem is supplied.

The algebraic content is strong; the packaging occasionally exceeds the rigour available.

---

## 3. Most Valuable Contributions

* **From `gpt_pro_thinking`:**
  -- The precise norm hierarchy (H5r-F / B / L1) and the conditional reduction R1-R3 turn a vague "residual is hard" into a concrete, testable question.
  -- The Abel-summation diagnostic R4 clarifies exactly what kind of proof would **not** exploit the fixed Fejer weights.
  -- The non-majorising comparison table, while incomplete, systematically catalogues the error terms incurred by various truncation methods.

* **From `gemini_deep_think`:**
  -- Q1-Ext is a genuinely useful algebraic lemma that can be plugged into signed Bombieri--Iwaniec matrices.
  -- C3-Ext provides a rigorous analysis of the parity-sign collapse under translation-invariant differencing, settling one part of the odd-lattice dual debate.
  -- The heuristic mapping of the Mellin--Perron route to the square-root phase (H10-A/B) is a valuable diagnostic, provided it is not over-stated.

---

## 4. Claims That Look Correct

1. Implication chain H5r-B ⇒ H5r-F ⇒ Vaaler residual \(\ll X^{1/4+\varepsilon}\) (R1--R3, gpt).
2. Equivalence of complex H5r-B with dyadic termwise \(L^1\) (Lemma R3, gpt).
3. Abel-summation identity (R4, gpt) for one-sided positive frequencies -- algebra correct.
4. Poisson--Bessel derivation of \(E(R)\ll R^{2/3}\) (gpt) -- standard and correct.
5. Lemma Q1-Ext (gemini) -- modular arithmetic is exact; the factorisation holds.
6. Coefficient-level parity collapse under translation differencing (C3-Ext, gemini) -- algebraic verification is sound.
7. The heuristic that sharp Perron truncation requires \(T\asymp X^{3/4}\) for endpoint error (gemini, H10-A) -- plausible under standard Perron-formula bounds.
8. The observation that the contour-shift plus functional equation leads to phases of the form \(\sqrt{Xhd}\) (gemini, H10-B) -- consistent with classical Voronoi summation; the qualitative picture is correct.

---

## 5. Claims That Need Proof or Further Work

| Claim | Source | Reason |
|-------|--------|--------|
| H5r-F sufficiency (R1) over the full Vaaler residual | gpt | Schematic proof needs explicit Vaaler constants, two-sided \(k\) treatment, and summation over all dyadic blocks. |
| Signed Fourier truncation provides a valid error term | gpt | No summability method or tail bound is supplied; the formal series does not converge. This is a severe gap. |
| H5r-B ⇒ H5r-F **without** noting that the proof is valid only if one can already bound the partial sums (R2) | gpt | The statement is correct as a conditional implication, but the underlying assumption that H5r-B holds for the fixed Fejer coefficients is trivial if the same coefficients are used. The real point is that H5r-B is a **stronger hypothesis** and R2 shows that fixing it suffices; this is well-stated but must not be confused with a proof that H5r-F is actually easier. |
| C3-Ext "ends the debate on two-coset spacing" | gemini | Only translation-invariant A-process is treated; the conclusion is too broad. |
| H10-A/B as proved theorems | gemini | The derivations are heuristic; no rigorous stationary-phase analysis or full error treatment is given. |
| R4 two-sided extension (negative \(k\)) | gpt | The one-sided analysis must be extended to the full Fejer average, including possible complex-conjugate symmetry. |
| Compatibility of Q1-Ext with smooth weights and spacing matrices | gemini | The lemma isolates the character product; interaction with oscillatory phases and smooth cut-offs has not been examined. |

---

## 6. Possible Errors and Hidden Assumptions

* **Vaaler constant unchecked:** Both agents use the majorant \(|R_H(t)|\le \frac{1}{2H+2}K_H(t)\). The precise constant may differ (e.g. \(\frac{1}{H+1}\) instead of \(\frac{1}{2H+2}\)) depending on the exact Vaaler polynomial. This needs verification from a standard reference. A wrong constant could affect the size of the zero-mode and the required exponent.

* **Signed Fourier truncation convergence:** The function \(\psi(t)=t-\lfloor t\rfloor-\frac12\) is piecewise linear; its Fourier series converges conditionally (pointwise at non-integers and to the average at integers). Truncating the series without any smoothing does not give a function that can be pointwise bounded by a simple tail; the Gibbs phenomenon and the conditional convergence make it impossible to bound the tail by a termwise absolute-value sum. Any rigorous approach would need to replace the sharp truncation by a smoothed one, which would likely introduce a positive kernel error. The agent's claim that signed truncation "preserves \(\chi_4\) better" is therefore premature.

* **Absolute-value placement in H5r-F:** The fixed-Fejer target uses a single absolute value outside the sum. This is crucial: it allows the sign of \(S_{\star}\) to be used inside the average. Any subsequent estimate that pushes the absolute value inside (e.g. by the triangle inequality) would revert to H5r-B/L1-type difficulty. The agent explicitly recognises this, but it must be guarded throughout the proof draft -- a hidden slip here is a common failure mode.

* **Mellin--Perron truncation cross-terms:** H10-B assumes that the contour integral can be shifted to \(\Re(s)=-1/2\) and then the functional equation can be applied. However, the integral along the lines \(\Re(s)=c\) and \(\Re(s)=-1/2\) and the horizontal segments require uniform bounds that are not provided. Moreover, the stationary-phase expansion on the resulting Voronoi series is not carried out; the claim that it "perfectly reconstructs" the phase \(\sqrt{Xhd}\) is an overstatement. Lower-order terms from incomplete Gamma functions or boundary effects may be relevant at the endpoint scale.

* **Two-coset parity collapse only for translation-invariant differencing:** The C3-Ext derivation uses a translation \(q\) and the identity \(\sigma(\xi)\sigma(\xi+q)=\frac14(-1)^{2q}\). This is valid for translation-invariant A-process (like Weyl differencing). However, some spacing methods (e.g. multiplicative shifts, or spectral large-sieve methods that do not rely on translation) may not succumb to the same collapse. The agent's conclusion that the "debate is ended" is therefore too sweeping.

* **Equivalence of H5r-B and dyadic \(L^1\):** R3 is correct if one can choose \(v_k\) to match the conjugate phase of \(S_{\star}(k,D)\) for **each** \(k\). This is allowed because H5r-B is required for **all** complex coefficients \(|v_k|\le 1\). However, note that in the actual Vaaler residual, the coefficients are **not** arbitrary; they are fixed Fejer weights. So the equivalence only says that if one proves the stronger arbitrary-coefficient estimate, one has effectively done \(L^1\). This is a warning that H5r-B is a much stronger hypothesis than H5r-F.

---

## 7. Suggested Synthesis

The two outputs can be combined into a sharper research map:

1. **Keep H5r-F as the official minimal residual target.** State the norm hierarchy (R1--R3) as a conditional reduction, with the caveat that H5r-B is stronger and may be too destructive.
2. **Promote R4 to a verified diagnostic lemma** after extending to two-sided Fejer averages. This lemma should be accompanied by an explicit comment: it does **not** force H5r-F ≡ H5r-B; it only shows that any proof of H5r-F that passes through generic partial-sum bounds does not exploit the Fejer structure.
3. **Incorporate Q1-Ext** into a potential signed Bombieri--Iwaniec estimate for H5a/H5b. The lemma shows that on spacing rays the character product is deterministic; the next step is to test whether Li--Yang-type spacing estimates can accept such signed coefficients without an unacceptable loss (e.g. without taking absolute values prematurely).
4. **Downgrade C3-Ext** to a **translation-invariant parity-collapse diagnostic** and explicitly limit its scope. Explore whether non-translation differencing (multiplicative shifts, etc.) can evade the collapse.
5. **Re-label H10-A/B** as **proposed diagnostics** rather than proved theorems. The qualitative mapping to the square-root phase is useful, but it must be backed by a complete theorem before it can be used as an argument in the proof attempt.
6. **Abandon signed Fourier truncation** as a near-term route: without a concrete summability method, it is not a valid alternative. Record it as a failed candidate in the gap register.
7. **Insert the Poisson--Bessel calibration module** as a secondary sanity check; do not let it distract from the main H5r bottleneck.
8. **Require a reference-checked statement of the Vaaler theorem** (exact coefficients, kernel normalisation, discontinuity convention) before H4 is marked as fully imported.

---

## 8. Score by Agent

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|:---|:---:|:---|:---|
| `gpt_pro_thinking` | 9 | Precise norm hierarchy, honest gap acknowledgement, clear diagnostic framing. The signed-truncation section is too optimistic for its current state. | Exact Vaaler constants; two-sided Abel-summation extension; signed-truncation convergence gap. |
| `gemini_deep_think` | 7 | Q1-Ext is a sharp algebraic tool; C3-Ext correctly captures translation-invariant parity collapse. However, the output overclaims (Mellin--Perron "theorems", C3 "obstruction", "ends debate") and several lemmas are labelled as proved when they are still diagnostics. | Convert H10-A/B into conditional diagnostics; provide exact Perron-to-Voronoi derivation; test Q1-Ext with smooth weights. |

---

## 9. Correction/Verification Items (6 explicit)

1. **Verify the Vaaler theorem from a standard reference.** Extract the exact coefficient formula, the Fejer-majorant constant, and the discontinuity convention. Compare with the form used in the proof draft.
2. **Extend the Abel-summation diagnostic (R4) to the full two-sided Fejer average.** Write the formula for the complete sum over \(1\le|k|\le H\) with symmetric Fejer weights, and confirm that the inequality still holds.
3. **Complete the sufficiency proof R1.** Starting from the Vaaler majorant, write the explicit expression for the total residual over all dyadic \(D\), both residual families, and both signs of \(k\); then bound it using H5r-F.
4. **Test Q1-Ext on small numerical examples.** Verify with concrete congruences that the frozen/alternating signs match the algebraic predictions for a variety of \(a,b,d_1,d_2\).
5. **Audit the Li--Yang theorem** to determine whether its spacing estimates can accommodate signed coefficients that alternate as dictated by Q1-Ext, without taking absolute values prematurely.
6. **Compute the signed Fourier truncation tail for a smooth test function** (e.g. a compactly supported bump) to measure its magnitude and see whether any cancellation survives or whether it quickly exceeds the permitted bound. This will objectively assess the viability of signed truncation.

---

## 10. Stress Tests (3 explicit)

1. **Fixed-Fejer vs. \(L^1\) gap test.** For representative square and near-square \(X\), compute the three residual norms H5r-F, H5r-B, H5r-L1 numerically. A persistent large gap would indicate that the Fejer averaging preserves cancellation unavailable to termwise \(L^1\) bounds; comparable sizes would support the Abel-summation bottleneck concern.
2. **Fejer spike test.** Choose \(X,d\) such that several of the arguments \(X/d,\;(X/d+\rho)/4\) are close to integers. Evaluate the residual majorant and check whether the scalar residual bound \(D/H_D\) grossly underestimates the true contribution. This tests the necessity of the full H5r analysis.
3. **Q1-Ext collision matrix test.** Construct a small dyadic matrix of phases and character products on near-collision rays, and apply a standard Bombieri--Iwaniec spacing bound first with absolute values, then with signed coefficients using the Q1-Ext alternation. Measure the loss. The outcome will reveal whether the signed structure can survive in a realistic estimate.

---

## 11. Failure Modes (4 explicit)

1. **Fejer averaging yields no extra cancellation.** If numerical experiments show that H5r-F is essentially as large as H5r-L1, then the fixed-Fejer target does not provide any structural advantage, and the Vaaler route becomes equivalent to bounding divisor-like reciprocal sums -- the known technology for which stays above \(\theta=1/4\).
2. **Signed Fourier tail cannot be rigorously controlled.** Any attempt to justify the signed truncation introduces a smoothing kernel, whose error term is itself a positive majorant that recreates H5r-B. This would confirm that positive majorants are unavoidable in Fourier-based truncation, ruling out the signed alternative.
3. **Signed character factorization destroyed by matrix norms.** Even though Q1-Ext shows the character is deterministic, standard large-sieve or Cauchy--Schwarz estimates apply triangle inequalities to the coefficient matrix, erasing the signed oscillation. A fundamentally new signed matrix norm would be required, and its existence is unclear.
4. **Mellin--Perron rebuilds the same divisor-type sums.** If the contour shift fully converts the Perron integral into a truncated Voronoi/Hardy series with dual length \(X^{1/2}\) and no new structural advantage, then this route is an analytic reformulation that does not improve the exponent, confirming the "circularity" diagnostic.

---

## 12. Confidence Calibration and Failure Modes

This section consolidates confidence across the route and individual lemmas, and ties failure modes to the overall assessment.

**Confidence calibration:**

* **High confidence** in the arithmetic reduction H1--H3 and the necessity of H5r.
* **High confidence** in the norm hierarchy R1--R3 and the implication chain.
* **High confidence** in the algebraic correctness of Q1-Ext (modular arithmetic) and the translation-invariant parity collapse of C3-Ext (coefficient part).
* **Moderate-to-high confidence** in the Abel-summation diagnostic R4, pending full two-sided extension.
* **Moderate confidence** that the Mellin--Perron route maps back to the Hessian-degenerate phase; however, the rigour of the mapping is currently only heuristic.
* **Low confidence** that signed Fourier truncation can be turned into a viable alternative; the convergence gap is severe.
* **Low confidence** that any existing route in the repository can currently prove the conjectural exponent. The present contribution is a much sharper map of the bottleneck and a set of concrete algebraic tools, **not** a new upper bound.

**Failure modes** (re-stated for completeness):

1. Fejer averaging yields no extra cancellation → Vaaler route equivalent to divisor-problem difficulty.
2. Signed Fourier tail uncontrollable → route invalid.
3. Signed character factorisation erased by matrix norms → algebraic advantage lost.
4. Mellin--Perron reconstructs the same reciprocal sums → no escape.

Any of these failure modes would confirm that the current framework cannot reach \(\theta=1/4\) without a fundamentally new insight.

---

## 13. Next-Round Recommendations

**For `gpt_pro_thinking`:**
* Produce a complete, reference-checked statement of H4 (Vaaler theorem) with exact constants.
* Rigorously prove R1--R3 with the exact Vaaler constants and the full two-sided Fejer decomposition.
* Formalise R4 as a diagnostic lemma covering the full complex Fejer average; explicitly note that it does not force H5r-F ≡ H5r-B.
* Demote signed Fourier truncation to "failed candidate" until a summability method is provided.
* Insert the Poisson--Bessel calibration module as a secondary proof block without distracting from H5r.

**For `gemini_deep_think`:**
* Package Q1-Ext as a lemma with a precise statement (include the assumption that \(d_1,d_2\) are odd) and then attempt to incorporate it into a signed spacing matrix estimate.
* Redraft C3-Ext as a "translation-invariant parity-collapse diagnostic" and provide a counterexample-type check for a non-translation based method (e.g. multiplicative shift) to show the limits of the conclusion.
* Write H10-A/B with explicit error terms; label them as "proposed diagnostics" and remove the "theorem" status until a full proof is supplied.
* Test the two-coset formulation with non-translation differencing to see if any phase-spacing difference survives.

**For the joint synthesis (judge):**
* Merge the norm hierarchy (gpt) with the character factorisation (gemini) into a unified proof draft.
* Initiate numerical tests (perhaps via `deepseek_api` or human assistance) comparing H5r-F, H5r-B, H5r-L1, and the Fejer-spike cases.
* Keep the Mellin--Perron route as a secondary comparison module, not a primary escape path.

---

*End of Stage B review for Round 8.*
