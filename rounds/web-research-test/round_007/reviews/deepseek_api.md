# Stage B Cross Review -- Round 7

**Reviewer:** `deepseek_api` (DeepSeek API)
**Role:** Algebra checker, obstruction auditor, and stress tester
**Round:** 7
**Agents reviewed:** `gpt_pro_thinking`, `gemini_deep_think`
**Mandate:** Judge instructions required a norm-level H5r theorem, a corrected C1, a convention-fixed C2 Poisson lemma, a non-majorizing comparison table, a Mellin-Perron development with exact truncation, analysis of the two-coset parity dual, and a rational-collision matrix test. This review evaluates the Stage A outputs against those mandates, identifies hidden assumptions, and proposes a synthesis.

---

## 1. Most Valuable Input from Others

**From `gpt_pro_thinking`:**
- A **precise hierarchy of residual targets**:
  - **H5r-F** -- the minimal fixed-Fejer average, shown to be *exactly sufficient* to bound the Vaaler residual at the conjectural scale (Lemma R1).
  - **H5r-B** -- a stronger, arbitrary-coefficient target, which by duality is essentially equivalent to a dyadic termwise   $L^1$ estimate (Lemma R3).
  - The logical chain $\text{H5r-B} \Rightarrow \text{H5r-F} \Rightarrow \text{Vaaler residual} \ll_\epsilon X^{1/4+\epsilon}$ is proved (Lemmas R1-R3).
- A **corrected conditional diagnostic C1**, with the proper scaling $X^{\max(1/4,\theta)+\epsilon}$ instead of the erroneous $X^{1/4+\theta}$.
- A **convention-fixed C2 Poisson lemma** for the odd-lattice sum, together with two equivalent representations and a preliminary stationary-phase analysis that yields dual length $m \asymp kX/D^2$.
- A **comparison table** of non-majorizing alternatives (Vaaler, signed Fourier, Mellin--Perron) that explicitly records which sign structures are preserved.

**From `gemini_deep_think`:**
- A **quantitative Mellin--Perron diagnostic**: the sharp Perron truncation requires $T \gg X^{3/4-\epsilon}$; any absolute-value treatment of the critical-line integral is $\gg X^{1/2}$ and thus blocks the conjectural endpoint; applying the functional equation regenerates reciprocal sums of length $\asymp X^{1/2}$ -- a structural "isomorphism" to the Vaaler bottleneck.
- A **rational-collision matrix analysis** showing that for exact collisions $(d_1,d_2)$ with $d_1 b = d_2 a$ and $(a,b)=1$, the character product reduces to $\chi_4(ab)$, i.e. a block-constant sign. The observation that character-blindness enters only when *matrix norms take absolute values* is a sharp diagnostic.
- An **algebraic check of the two-coset parity A-process**: writing the dual as half-integer frequencies $\mu = m/2$, the alternating factor $(-1)^{2\mu}$ collapses to $+1$ under a direct differencing shift $\mu \mapsto \mu+q$, confirming that direct A-process destroys the parity oscillation.

Both agents have delivered mathematically useful contributions that are largely complementary.

---

## 2. Detailed Assessment of `gpt_pro_thinking`

### 2.1 Correctness and Rigour

The arithmetic backbone (H1--H3) is used consistently. The floor-compatible sawtooth $\psi(t)=t-\lfloor t\rfloor-\frac12$ is carried through the whole derivation. The Vaaler approximation is invoked with the Fejer majorant:

$$
|R_H(t)|
\le \frac{1}{2H+2} K_H(t),\qquad
K_H(t) = 1 + \sum_{1\le|k|\le H} \eta_{k,H} e(kt),\;
\eta_{k,H}=1-\frac{|k|}{H+1}.
$$

The residual bound for the first leg is derived as

$$
\Bigl|\sum_d \chi_4(d) w_D(d) R_{H_D}(X/d)\Bigr|
\ll \frac{1}{2H_D+2}
\Bigl( S_{\mathrm{odd}}(0,D) + \sum_{1\le|k|\le H_D} \eta_{k,H_D} S_{\mathrm{odd}}(k,D) \Bigr),
$$

where $S_{\mathrm{odd}}(k,D) = \sum_{2\nmid d} w_D(d) e(kX/d)$. The second leg is treated analogously, giving families $S_\rho(k,D)$ for $\rho=1,3$. These algebraic reductions are **exact** under the pointwise majorant and the non-negativity of $w_D$.

The zero-mode term is $\asymp D/H_D \asymp X^{1/4}$. Hence the required **residual target** is the fixed-Fejer average of the nonzero modes:

$$
\boxed{\text{H5r-F: } \Bigl| \frac1{H_D} \sum_{1\le|k|\le H_D} \eta_{k,H_D} S_\star(k,D) \Bigr| \ll_\epsilon X^{1/4+\epsilon}}.
$$

This is a genuine **minimum requirement**; Lemma R1 proves that if H5r-F holds for every dyadic $D$ in $[X^{1/4},X^{1/2}]$, then the total Vaaler residual is $O_\epsilon(X^{1/4+\epsilon})$.

Lemmas R2 and R3 establish the implications

$$
\text{H5r-B} \;\Longrightarrow\; \text{H5r-F}, \qquad
\text{H5r-B} \;\Longleftrightarrow\; \text{dyadic } L^1 \text{ estimate}.
$$

These are elementary but crucial for clarifying what the proof actually needs.

The corrected C1 diagnostic states:

$$
P(X) \ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

under the assumption that the only available H5r bounds are character-blind reciprocal estimates at exponent $\theta$. This is logically sound; the "max" correctly reflects the zero-mode floor.

The C2 Poisson lemma is presented with a clear Fourier convention $\widehat F(\xi)=\int F(u)e(-\xi u)du$ and shown to have two equivalent forms. The stationary-phase sketch correctly identifies the active dual length $|m|\asymp kX/D^2$ and the phase shape $\sqrt{2kXm}$.

**Overall, the reasoning is transparent and logically rigorous. There are no over-reaching claims.**

### 2.2 Potential Issues or Hidden Assumptions

1. **Vaaler reference unverified.** The majorant constant $\frac1{2H+2}$ is plausible but should be checked against a standard source (Montgomery--Vaughan, *Multiplicative Number Theory I*, §6.2, or Vaaler, *Bull. AMS* 12 (1985), 183--216). The exact coefficient formula for the main terms (needed for H5a/H5b) also needs auditing.
2. **Dyadic partition non-negativity.** The residual majorant argument uses $w_D(d)\ge0$ to pass absolute values inside the sum. If a signed dyadic partition is used in the main terms, one must either replace it by $|w_D|$ in the residual or provide an additional bound. This is a minor technical point but must be recorded in the lemma bank.
3. **Stationary-phase constants.** The phase constant $e(1/8)$ is given without derivation; the amplitude prefactor is not spelled out. A complete stationary-phase lemma would need those together with uniform error terms. This is a known gap and is acknowledged.
4. **Boundary ranges.** The cases $D\asymp X^{1/2}$ with $k\asymp1$ (dual length $O(1)$) and $D\asymp X^{1/4}$ with $H_D\asymp1$ are noted but not treated quantitatively. They form a genuine analytical gap.
5. **Absolute-value placement in H5r-F.** The Fejer average is taken with a single outer absolute value after summation over $k$. This is the correct level for the Vaaler route; it is weaker than termwise absolute values and may permit cancellation between Fejer modes. The agent correctly distinguishes this from H5r-L1.

None of these issues invalidate the main contributions; they are implementational details.

---

## 3. Detailed Assessment of `gemini_deep_think`

### 3.1 Correctness and Rigour

The agent provides a series of diagnostic computations that are **largely correct** under their stated hypotheses.

- **Mellin--Perron truncation:** The sharp Perron formula with error $O(X^{1+\epsilon}/T)$ is standard, and the requirement $T\gg X^{3/4-\epsilon}$ for the endpoint error is correct.
- **Critical-line barrier:** Shifting to $\Re(s)=1/2$ and bounding the vertical integral by $X^{1/2}\int_{-T}^T |Z(1/2+it)| dt/(1+|t|)$ is sound. Even under Lindelof, this is $\gg X^{1/2}$, demonstrating that an absolute-value treatment fails by a large margin.
- **Functional-equation isomorphism:** The argument that applying the asymmetric functional equation for $4\zeta(s)L(s,\chi_4)$ and using stationary phase regenerates reciprocal sums of length $\sim T^2/X$, which for $T=X^{3/4}$ gives length $\sim X^{1/2}$, is a correct *heuristic*. It shows that the Mellin--Perron route is structurally tied to the same reciprocal-sum bottleneck.
- **Two-coset parity A-process:** Writing the dual as a sum over half-integers $\mu=m/2$ with coefficient $c_\mu=(-1)^{2\mu}$, the product $c_\mu c_{\mu+q}=(-1)^{2q}$ is indeed constant. Hence a direct Weyl differencing eliminates the alternating factor. Algebraically this is correct.
- **Rational-collision exact-collision sign:** For $d_1=ac$, $d_2=bc$ with $(a,b)=1$, oddness of $a,b,c$ forces $c$ to be odd, so $\chi_4(c)^2=1$ and $\chi_4(d_1)\chi_4(d_2)=\chi_4(ab)$. This is elementary and correct.

**Overall, the diagnostic computations are rigorous within their stated assumptions.** However, the interpretation occasionally crosses from " diagnostic" to "theorem" language, which needs careful demotion.

### 3.2 Potential Issues or Over-interpretations

1. **Near-collision sign behaviour.** The exact-collision analysis does **not** automatically apply to the actual Bombieri--Iwaniec setting, where one has $|d_1 b - d_2 a| \le \Delta$. The character product may well depend on the residues and could average to zero over a near-collision block. The claim that the character "forms a uniform, block-constant sign" for the *entire* collision trajectory is **unverified for near-collisions** and must be demoted to a **conjecture** until a near-collision lemma is proved.
2. **Two-coset A-process over-interpretation.** The algebraic collapse proves only that a *direct uniform differencing* destroys the alternating factor. It does **not** rule out bilinear or spacing arguments that exploit the parity structure before differencing. The conclusion should remain a **conditional diagnostic**, not a proof of analytic sterility.
3. **Mellin--Perron "structural isomorphism".** The path from the functional equation to Voronoi/Bessel reciprocal sums is well-known, but the statement that it "reconstructs the exact same reciprocal-sum bottlenecks" is an **informal equivalence**. A rigorous translation would require mapping the contour integral to a dyadic sum with explicit weights and proving equivalence in difficulty. The current phrasing can be misread as a theorem.
4. **Smoothed Perron parameter.** The claim that a smoothed Mellin transform with transition width $\asymp X^{1/4}$ requires effective support $T\asymp X^{3/4}$ is plausible but needs a precise lemma (e.g., using the exponential integral or a kernel with rapid decay). Currently it is only sketched.
5. **Lack of alignment with H5r-F.** The agent does not discuss the new H5r norm hierarchy, which is the central topic of Round 7. This limits direct synthesis with `gpt_pro_thinking`'s work, but it is not an error per se; the agent followed a different strand of the judge instructions.

---

## 4. Claims that Look Correct

- **H5r-F** is the correct minimal residual target for the current Vaaler route (derived correctly by `gpt_pro_thinking`).
- **Lemma R1**: $\text{H5r-F} \Rightarrow$ Vaaler residual $\ll_\epsilon X^{1/4+\epsilon}$ (proof sound).
- **Lemma R2**: $\text{H5r-B} \Rightarrow$ H5r-F (elementary, correct).
- **Lemma R3**: $\text{H5r-B}$ is equivalent (for complex $v_k$) to the dyadic $L^1$ estimate $\sum_{k\sim K_0}|S_\star(k,D)| \ll_\epsilon K_0 X^{1/4+\epsilon}$.
- **C1 corrected diagnostic**: $P(X) \ll_\epsilon X^{\max(1/4,\theta)+\epsilon}$ under character-blind H5r inputs (scaling now standard).
- **C2 Poisson formula**: the two equivalent representations of the odd-lattice sum are valid under the stated Fourier convention.
- **Dual length from C2**: $|m| \asymp kX/D^2$ is correct from stationary phase.
- **Mellin--Perron truncation**: $T\gg X^{3/4-\epsilon}$ is necessary for endpoint error; critical-line absolute-value integral is $\gg X^{1/2}$.
- **Exact-collision character product**: $\chi_4(d_1)\chi_4(d_2) = \chi_4(ab)$ when $d_1 b = d_2 a$ and $(a,b)=1$, with $a,b,c$ odd.
- **Dual-parity A-process algebra**: $c_\mu c_{\mu+q}=(-1)^{2q}$ is constant for shift $q$, showing collapse under direct differencing.

These claims are mathematically solid and should be promoted to the lemma bank with appropriate statuses.

---

## 5. Claims that Need Proof

- **H5r-F is endpoint-strength and unproved** -- it is a target, not a theorem. The repo must treat it as an open problem.
- **Near-collision block-constant sign** (gemini's exact-collision extension to $|\Delta|>0$). Needs a lemma with error term.
- **Mellin--Perron functional-equation mapping** -- requires a rigorous lemma translating the contour integral to explicit dyadic reciprocal sums, with error bounds and coefficient formulas.
- **Smoothed Perron effective support** -- needs a precise statement linking transition width to required truncation height.
- **C3 two-coset spacing viability** -- no proof yet that the half-integer dual phases retain usable spacing information after a B-process or other transform.
- **Stationary-phase constants for C2** -- the $e(1/8)$ phase and amplitude prefactor need derivation and verification.
- **Boundary regimes ($D\asymp X^{1/2}$, $k\asymp1$; $D\asymp X^{1/4}$)** -- these require separate analysis, not yet supplied.
- **Fejer average vs. dyadic $L^1$ separation** -- while the implication chain is proved, the question of whether H5r-F is *strictly easier* than H5r-B is an open empirical / theoretical question that needs stress testing.

---

## 6. Possible Errors or Hidden Assumptions

1. **Vaaler majorant constant.** The agent uses $\frac{1}{2H+2}$; a standard reference (e.g., Montgomery--Vaughan, p. 117) gives the Fejer kernel as $\frac{1}{H+1}\bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\bigr)^2$, and the majorant constant is often $\frac{1}{H+1}$. The factor 2 difference is harmless for asymptotics, but must be checked to avoid constants that might accumulate across $O(\log X)$ blocks.
2. **Positivity assumption for dyadic weights.** $w_D(d)\ge0$ is used in majorizing the residual. If the actual dyadic decomposition uses signed weights, the bound fails. Usually one can take $|w_D|$ for the residual argument, but this must be stated.
3. **Floor-compatible $\psi$ versus Fourier-centered sawtooth.** The discontinuous $\psi$ is approximated by a continuous Vaaler polynomial plus a residual. The agent's argument retains the residual pointwise, so the half-jump at integers is absorbed in the Fejer majorant. This is safe **provided** the sum over $d$ is taken before applying absolute values to the residual -- which is exactly what is done.
4. **Gemini's claim on "reconstructs the exact same reciprocal-sum bottlenecks".** This is a heuristic, not a rigorous theorem. If taken as a proven impossibility, it would be an overstatement.
5. **Over-promotion of parity A-process collapse.** The algebra shows only that direct differencing kills the alternating factor. A bilinear or matrix method might still exploit the parity before applying such a transform. This nuance is often lost in summary.
6. **Incomplete engagement with H5r-F by `gemini_deep_think`.** The judge instructions implicitly required all agents to address the new norm hierarchy, but `gemini` did not do so. This is a gap in coverage, not an error in the mathematics presented.
7. **Potential misuse of the term "isomorphism"** for the Mellin--Perron ↔ Voronoi connection. Without explicit coefficient-for-coefficient mapping, it remains a structural analogy.

Each of these should be explicitly flagged in the next round's reading packet.

---

## 7. Explicit Correction / Verification Items

1. **Vaaler theorem audit** -- retrieve the exact statement from a standard reference, verify the majorant constant and the coefficient formula for $\alpha_{h,H}$. Record as H4 in the lemma bank with source.
2. **Fourier convention check for C2** -- derive the $\frac12\sum_{m}(-1)^m$ formula step-by-step from the Poisson summation formula with the chosen $\widehat F(\xi)=\int F(u)e(-\xi u)du$. Verify equivalence with the two-coset representation.
3. **Stationary-phase constants** -- for $I_{-\ell} = \int w_D(u)e(kX/u + \ell u/2) du$, compute $u_0$, $\phi''(u_0)$, amplitude, and phase shift, including the $1/8$ term. Compare with a known theorem (e.g., Stein, *Harmonic Analysis*, §VIII.7) and test numerically.
4. **H5r-B ↔ dyadic $L^1$ equivalence proof (Lemma R3)** -- write the precise duality argument: for any $S_\star$, $\sup_{|v_k|\le1} |\sum_{k\sim K_0} v_k S_\star(k,D)| = \sum_{k\sim K_0} |S_\star(k,D)|$. Confirm that the Fejer coefficients $\eta_{k,H_D}$ are real and satisfy $|\eta_{k,H_D}|\le1$.
5. **Near-collision character product lemma** -- for $d_1 = a c + r$, $d_2 = b c + s$ with small $|r|,|s|$, derive $\chi_4(d_1)\chi_4(d_2)$ explicitly in terms of $\chi_4(ab)$, the residues $r,s$, and the parity of $c$. Determine under what range the block-sign remains stable.
6. **Mellin--Perron rigorous mapping** -- write the functional equation for $4\zeta(s)L(s,\chi_4)$ and perform the contour shift to $\Re(s)=\frac12$ with explicit error analysis. Derive the resulting dual sum and compare its structure (length, phase, coefficient class) with H5a/H5b/H5r.
7. **Numerical stress tests** (see Section 9) -- implement and report results.

---

## 8. Failure Modes

1. **H5r-F intractable** -- if the fixed-Fejer average proves to be as hard as the divisor-problem $L^1$ estimate, the current Vaaler route cannot reach $1/4$. The project would then need a sign-preserving truncation or a fundamentally different method.
2. **Near-collision sign randomness** -- if the character product $\chi_4(d_1)\chi_4(d_2)$ averages to zero for typical near-collisions, the block-constant sign escape hatch closes, and H5a/H5b must be treated as character-blind (or effectively character-blind after matrix norms).
3. **Discontinuity handling oversight** -- if the proof fails to account for the half-jump of $\psi$ at integers in a future streamlined version (e.g., by omitting the residual), the entire estimate could silently break. The current majorant approach is safe, but any simplification must retain the residual.
4. **Fejer majorant constants accumulation** -- if the dyadic partition and majorant constants are not controlled uniformly, the implicit logarithm may hide a larger constant that prevents a clean $X^{1/4+\epsilon}$ bound. This is unlikely to create an asymptotic obstruction but could affect small-$X$ explicit bounds.
5. **Gemini's "isomorphism" taken as a proof of impossibility** -- if the repo treats the Mellin--Perron circularity as a theorem, it might prematurely discard a viable pathway. The correct status is "strong diagnostic, not a theorem".
6. **C2/C3 over-promotion** -- if the parity collapse is interpreted as a proof that B-process-first always fails, the project might miss a spacing-based resolution of H5r using the two-coset formulation. This would be a false exclusion.

---

## 9. Stress Tests

1. **Fixed-Fejer versus termwise $L^1$ separation.** For moderate $X$ (e.g., $X=10^5$), $D\approx X^{1/2}$, $H_D = D X^{-1/4}$, compute:

$$
F_D = \frac1{H_D}\Bigl|\sum_{1\le|k|\le H_D} \eta_{k,H_D} S_{\text{odd}}(k,D)\Bigr|,\qquad
L_D = \frac1{H_D}\sum_{1\le|k|\le H_D} |S_{\text{odd}}(k,D)|.
$$

If $F_D \ll L_D$, then H5r-F is genuinely easier than $L^1$, justifying further work on the Fejer-weighted target. If $F_D \approx L_D$, the distinction is academic for practical purposes.

2. **C2 stationary-phase validation.** Use a smooth bump $w_D$ with $D=100$, $k=10$, $X=10^4$, and numerically evaluate $I_{-\ell}$ for $\ell$ around $kX/D^2$. Compare the amplitude and phase with the stationary-phase prediction. Check the $e(1/8)$ constant and verify that non-stationary $\ell$ give rapid decay. This tests the correctness of the derived dual-length formula and the phase constant.

3. **Near-collision sign bias test.** Fix $D=500$, $a=1$, $b=3$. For each small $\Delta \in [-5,5]$, collect all odd $d_1,d_2\sim D$ with $|3 d_1 - d_2| = \Delta$ and compute the empirical mean $\mathbb{E}[\chi_4(d_1)\chi_4(d_2)]$. A persistent nonzero mean would support the block-constant conjecture; rapid averaging to zero would indicate that the character acts like random noise at the near-collision scale.

4. **Mellin--Perron integral size.** Integrate numerically $I(T)=\int_1^T |\zeta(1/2+it)L(1/2+it,\chi_4)| dt / t$ for $T$ up to $10^5$. Verify that $I(T)$ does not decay and is consistent with $\gg \log T$ or constant, confirming the critical-line barrier.

---

## 10. Suggested Synthesis

The Round 7 outputs together sharpen the research state as follows:

- The **Vaaler route** is now fully specified: the exact residual target is **H5r-F**. No further ambiguity remains about which norm is required. The route is **logically complete** once H5r-F is supplied.
- The **Mellin--Perron diagnostic** correctly identifies that contour methods face the same reciprocal-sum bottleneck after the functional equation; thus it does not provide an escape, but it serves as a useful mirror.
- The **rational-collision block-sign property** suggests a potential new tool: if near-collisions also preserve a block-constant character sign, one might estimate the *signed* bilinear form directly, bypassing the Fejer majorant's sign-loss. This could either **replace H5r-F** with a signed truncation residual, or **strengthen** the H5a estimate.
- The **parity dual (C2/C3)** remains a diagnostic, not a closed door. While direct A-process collapses the alternating factor, the two-coset formulation may retain usable phase spacing.

**Recommended synthesis for the next round:**
- Promote the H5r norm hierarchy (Lemmas R1-R3, C1, C2) to the lemma bank with cleared statuses.
- Simultaneously pursue **two experimental lines**:
  1. **Numerical stress tests** on H5r-F vs. H5r-B/L1, Fejer spikes, and C2 stationary phase.
  2. **Theoretical development of the near-collision sign lemma**: can we prove that $\chi_4(d_1)\chi_4(d_2) \approx \chi_4(ab)$ for typical near-collisions? If positive, this could feed into a signed matrix estimate.
- Keep the Mellin--Perron route as a secondary diagnostic, but do not invest heavy effort unless a new contour idea (e.g., non-vertical paths, double-integrals) emerges.

---

## 11. Score by Agent

| Agent reviewed | Score (0--10) | Main reason | Must verify next |
|---|---:|---|---|
| **gpt_pro_thinking** | 9 | Highly detailed, rigorous norm hierarchy, clean implications, no overclaims. | Vaaler reference, stationary-phase constants, H5r-F numerical tests. |
| **gemini_deep_think** | 7 | Valuable structural diagnostics (Mellin--Perron, rational-collision); some claims need demotion (near-collision block-sign, parity A-process as full obstruction) and missing engagement with H5r-F hierarchy. | Near-collision sign lemma, rigorous Mellin--Perron mapping, two-coset spacing viability, align with H5r-F. |

---

## 12. Next-Round Recommendation

1. **Update lemma bank** with H5r-F, H5r-B, H5r-L1 and the implication lemmas R1-R3, C1, C2. Mark C3 as diagnostic only.
2. **Audit the Vaaler theorem** and commit H4 (with precise reference) to the lemma bank.
3. **Conduct numerical stress tests** (Fejer-average vs. L1, C2 stationary-phase, near-collision sign bias) and report the results.
4. **Task `gemini_deep_think`** to:
   - Formalise the rational-collision observation into a conditional lemma with error term for near-collisions.
   - Write a rigorous mapping from the Perron integral to dyadic reciprocal sums via the functional equation, with explicit constants and error bounds.
   - Downgrade the language of "isomorphism" and "sterile" to diagnostic status.
5. **Task `gpt_pro_thinking`** to:
   - Extend the non-majorizing comparison table with a column for "character preservation".
   - Explore whether a signed Vaaler-type polynomial (or signed Fourier truncation) could yield a residual that retains $\chi_4$, i.e., a signed residual target that might be easier than H5r-F.
   - Incorporate the Poisson-Bessel calibration proof as a secondary sanity check.
6. **Retain the Mellin--Perron route** as a secondary mirror, but avoid spending primary effort on it unless a novel contour idea is found.

---

## 13. Confidence Calibration and Failure Modes

- **H5r-F as the minimal target:** *High confidence* that this is the correct analytic requirement for the Vaaler route. *Low confidence* that it can be proved without a breakthrough, because it is an endpoint-strength reciprocal-sum input.
- **Mellin--Perron circularity:** *Moderate-high confidence* that the functional equation regenerates reciprocal sums of length $\asymp X^{1/2}$; this is a strong obstruction, but not yet a theorem that *all* Perron-type methods are doomed. New contour ideas could, in principle, avoid this.
- **Rational-collision block-sign:** *Low-to-moderate confidence* that the sign stability extends to near-collisions; the exact collision algebra is correct, but the transition to the required Bombieri--Iwaniec spacing regime is a major open gap.
- **Parity dual C2/C3:** *Moderate confidence* that direct A-process kills the alternating factor; *low confidence* that this precludes all spacing-based gains because the two-coset formulation may still encode useful phase shifts.
- **Overall project status:** The repo now has a crystal-clear proof skeleton and a precisely formulated central bottleneck. No exponent improvement has been proved; the present work is a high-quality **reduction and diagnostic map**.

**Potential catastrophic failure mode:** If H5r-F turns out to be strictly equivalent (in difficulty) to the full divisor-problem conjecture, then the Vaaler route adds no advantage over a direct attack on the divisor problem. The project would then need to hunt for a sign-preserving truncation or a different global method. The numerical stress tests are crucial to gauge this risk.

---

*End of Stage B Cross Review -- Round 7*
