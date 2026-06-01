# Stage B Cross Review -- Round 9

**Reviewer:** `deepseek_api` (algebra checker, obstruction auditor, and stress tester)

This review evaluates the Stage A outputs from `gpt_pro_thinking` and `gemini_deep_think` for Round 9.
The task is a referee-style assessment: identify correct claims, flag gaps, detect hidden assumptions, propose synthesis, and assign scores.
The review is **not** a continuation of the proof.

---

## 1. Most valuable input from others

### From `gpt_pro_thinking`

* **Li--Yang source audit (L9.1).**
  The output correctly reads the actual LaTeX source and identifies the exact theorem hypotheses (`\label{definition of S}`, `\label{condition on F 1}`, `\label{condition on F 2}`, `\label{goal}`).
  The audit shows that Li--Yang's final circle/divisor application uses a truncation height $H\le M T^{-\theta^*}$, which at the critical denominator block $D\asymp X^{1/2}$ becomes $H\lesssim X^{0.1855...}$, far below the Vaaler endpoint height $H_D\asymp X^{1/4}$.
  Moreover, Li--Yang's theorem gives an exponent $\theta^*\approx0.31448 > 1/4$, so even if the range were extended, it does **not** supply the conjectural exponent.
  The audit also correctly notes that the theorem uses bounded-variation weights $g,G$, not arbitrary coefficients $v_k$; therefore it cannot imply the stronger residual norms H5r-B or H5r-L1.
  This is a decisive negative import result: **Li--Yang (2023) cannot be used as a black-box endpoint theorem for the Vaaler residual**.

* **Lemma R5 -- fixed-Fejer residual via product-counting.**
  This is the most original and potentially route-changing contribution of Round 9.
  The key idea is to evaluate the positive Fejer-kernel majorant of the Vaaler residual directly, without expanding it into dyadic arbitrary-coefficient reciprocal sums.
  The proof sketch uses the standard pointwise bound
  \[
  \frac1H K_H(t) \ll \min\!\Bigl(1,\frac1{H^2\|t\|^2}\Bigr),
  \]
  converts the sum over $d$ into a sum over product-pairs $(m,d)$ with $md\approx X$, exploits the divisor bound $\tau(n)\ll_\epsilon n^\epsilon$, and obtains the required $X^{1/4+\epsilon}$ bound.
  If this argument can be made rigorous (and the dependencies are only the Fejer-kernel estimate and the divisor bound), then **H5r-F is demolished as a bottleneck**.
  This is a major simplification of the proof sketch.

* **Norm overstrengthening of H5a/H5b recognised.**
  The output points out that the existing H5a/H5b targets assume arbitrary bounded coefficients $u_h$, while the actual Vaaler main-term coefficients satisfy $|\alpha_h|\ll 1/|h|$ with a definite sign pattern.
  This is a valuable corrective: the proof should work with the **exact fixed-coefficient** forms, not with the artificially stronger arbitrary-coefficient versions.  It may open the door to estimates that exploit the $1/h$ decay without requiring the full Li--Yang machinery.

### From `gemini_deep_think`

* **Li--Yang parameter-domain obstruction (N2-Audit).**
  Gemini goes further than the gpt audit by extracting the **domain restrictions** of Li--Yang's main theorem, namely Case A $H\le M T^{-49/164}$ and Case B $H\le M^{35/69}T^{-2/23}$.
  At the endpoint $M\asymp X^{1/2},\ T=X$, these force $H\le X^{33/164}\approx X^{0.2012}$ (Case A) and $H\le X^{23/138}\approx X^{0.1666}$ (Case B).  Since the Vaaler requirement is $H_D\asymp X^{1/4}=X^{0.25}$, the theorem's **hypothesis domain** is violated; it is not merely that Li--Yang gives a weaker exponent -- the theorem cannot even be legally invoked for the full Vaaler frequency range.
  This sharpens the obstruction and should be recorded as a permanent guardrail.

* **Mellin--Perron dual-length conservation (H10-M).**
  Gemini provides a step-by-step contour-shift and stationary-phase argument showing that targeting an $X^{1/4}$ error via a smoothed Perron integral of $4\zeta(s)L(s,\chi_4)$ forces a dual Voronoi-type sum with length $\asymp X^{1/2}$ and the degenerate phase $2\pi\sqrt{nX}$.  This formalises earlier diagnostic intuitions: the Mellin--Perron route **is not an escape**; it reconstructs the same reciprocal-Bessel obstacle.
  The argument is plausible and consistent with standard analytic-number-theory lore; it should be kept as a comparison lemma.

* **Algebraic parity-collapse diagnostics (C3-Mult).**
  The new observation that multiplicative (non-translation) differencing with odd dilations collapses the parity coefficient in the two-coset dual formulation is a nice algebraic fact.  It strengthens the H7/C3 family of obstructions: both translation and odd-rational-dilation differencing erase the character oscillation.  Even dilations survive formally, but they do not reduce the derivative order of the phase and are unlikely to provide spacing gains.

---

## 2. Claims that look correct

1. **Li--Yang source audit (both agents).**
   The statements about the final truncation height $Y=MT^{-\theta^*}$ and the domain constraints $H\le M T^{-49/164}$ are faithfully extracted from the LaTeX source and correctly evaluated numerically.  The conclusion that Li--Yang's theorem does not apply to the endpoint Vaaler height $X^{1/4}$ is therefore solid.

2. **R5 -- product-counting bound.**
   The overall structure of the argument is correct.
   The Fejer-kernel bound is standard.
   The change of variables $d\mapsto (m_d,d)$ and grouping by the product $n=m_d d$ is legitimate, because
   \[
   \|X/d\| = \frac{|X-m_d d|}{d} \asymp \frac{|X-n|}{D},
   \]
   and the number of divisor pairs $(m,d)$ with $md=n$ is at most $\tau(n)$.
   The subsequent dyadic-annulus estimate for $\sum_n \tau(n)\min(1,\Delta^2/|X-n|^2)$ with $\Delta=D/H\asymp X^{1/4}$ yields $O_\epsilon(X^{1/4+\epsilon})$; no subtle cancellation is required.
   Therefore, **if the Vaaler residual truly takes the form $\frac{C}{H}\sum_{d} |w_D(d)| K_H(X/d)$** (with $C$ absolute), then R5 proves H5r-F.

3. **Norm overstrengthening correction.**
   The identification that the actual Vaaler main-term coefficients are $\alpha_h\ll 1/|h|$ and not arbitrary bounded $u_h$ is mathematically correct and important.

4. **Gemini's Case-A/B extraction (N2-Audit).**
   The numbers $49/164$, $35/69$, $2/23$ are present in the LaTeX source (as earlier summarised in the reading packet) and the computed exponents $0.2012$ and $0.1666$ are accurate.

5. **Mellin--Perron dual length (H10-M).**
   The scaling argument that a truncation height $T\asymp X^{3/4}$ implies a dual length $N\asymp X^{1/2}$ is a standard consequence of Stirling's formula for the Gamma-ratio in the functional equation.  The phase $2\pi\sqrt{nX}$ is correctly derived.

6. **C3-Mult parity collapse for odd dilations.**
   The algebra $\sigma(\xi)=\frac12(-1)^{2\xi}$ and $\xi_2=a\xi_1$ with $a$ odd gives $2\xi_1(1+a)$ even, hence $\sigma(\xi_1)\sigma(a\xi_1)=1/4$.  This is a simple, provable congruence fact.

---

## 3. Claims that need proof (or further verification)

### 3.1 Lemma R5 -- complete rigorous proof

The gpt output gives a convincing sketch, but several details must be written down before the lemma can be promoted to "proved".

* **Exact Vaaler majorant constant.**
  The statement $|R_H(t)|\le \frac{1}{2H+2} K_H(t)$ must be verified against a standard reference (e.g., Vaaler's original paper or a textbook).  The proof draft should cite the precise theorem, including the normalisation of $K_H$ (often $K_H(t)=\frac{1}{H+1}\bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\bigr)^2$).  Minor differences in constants do not affect the $X^{1/4+\epsilon}$ target, but a careful check is needed for the exact residual bound.

* **Handling of the second-leg residual.**
  The gpt sketch says "the same argument works for $K_H((X/d+\rho)/4)$ with $n=(4m-\rho)d$".  A precise lemma should state:
  \[
  \frac1H\sum_{d\sim D} K_H\!\Bigl(\frac{X/d+\rho}{4}\Bigr) \ll_\epsilon X^{1/4+\epsilon},
  \]
  with a short proof that the congruence restriction on $m$ does not increase the divisor count beyond $2\tau(n)$.  This is elementary but should be explicit.

* **Divisor-bound uniformity.**
  The use of $\tau(n)\ll_\epsilon n^\epsilon$ in a sum over $n\asymp X$ is standard, but one must note that the implied constant in $\ll_\epsilon$ may depend on $\epsilon$; the final $X^\epsilon$ absorbs it.  A clean write-up will state: for any $\epsilon>0$, there exists $C(\epsilon)$ such that $\tau(n)\le C(\epsilon)n^\epsilon$ for all $n\ge1$.  Then the sum $\sum_{n\asymp X}\tau(n)\min(1,\Delta^2/|X-n|^2)\le C(\epsilon)X^\epsilon\sum_{n} \min(1,\Delta^2/|X-n|^2) \ll C(\epsilon)X^\epsilon\Delta$.  This requires that the $n$-range is $O(X)$, which is true because $md\asymp X$.  Good.

* **Non-negativity of the dyadic partition.**
  The proof uses $|w_D(d)|\le 1$; if the smooth dyadic partition includes complex-valued weights, the bound still holds with absolute values.  If the weight is allowed to be larger than $1$ on the overlap, the constant must be adjusted but does not affect the exponent.

* **Integration of R5 into the full proof skeleton.**
  The gpt correctly states that R5 implies H5r-F.  However, the full residual over all dyadic blocks, both signs of $k$, and the zero-mode must be explicitly summed.  The logarithmic number of blocks introduces $O(\log X)$ which is absorbed in $X^\epsilon$.  This needs a short bridging lemma.

### 3.2 Gemini's bounded-variation penalty for parity

Gemini claims that the odd-indicator $1_{2\nmid d}$ has $O(D)$ jumps and therefore violates Li--Yang's bounded-variation hypothesis if inserted directly as $G(m/M)$.
While technically correct, the gpt audit already removes the need to use Li--Yang on the residual, so this point loses its force.  Nevertheless, it should be recorded as a caution: **if** someone later attempts to feed $S_{\mathrm{odd}}$ into Li--Yang, they must first substitute $d=2m+1$ to restore continuity of the coefficient.  The substitution is possible and does not alter the essential difficulty, but the bounded-variation remark is not a fundamental obstruction.

### 3.3 Gemini's claim that "Li--Yang's hypotheses strictly cap ... mathematically cannot evaluate"

The wording "mathematically cannot evaluate" is slightly too strong.  The theorem as currently proved contains parameter restrictions; it does not prove that **no** Bombieri--Iwaniec argument could ever be extended to larger $H$.  A better formulation is: "the Li--Yang (2023) theorem, in its published form, imposes an upper bound $H\le M T^{-49/164}$ (Case A) or $H\le M^{35/69}T^{-2/23}$ (Case B); at the endpoint $M\asymp X^{1/2}$ these bounds are $X^{0.2012}$ and $X^{0.1666}$, respectively, and therefore the theorem cannot be invoked for the Vaaler height $H_D\asymp X^{1/4}$.  Whether a future generalisation could relax these bounds is an open research question, but no such theorem currently exists."  This qualifier prevents a false claim of absolute impossibility.

### 3.4 Mellin--Perron boundary transitions

The H10-M sketch assumes the stationary-phase analysis on the vertical contour dominates the integral.  In practice, the transition near the truncation cutoff $|t|\approx T$ (incomplete Gamma functions) and the possible contributions from horizontal segments after contour shifting must be checked.  The gist of the argument is standard, but before H10-M is entered as a lemma, a careful statement with error terms should be provided.  Until then, it remains a diagnostic.

### 3.5 C3-Mult even-dilation case

Gemini states that even dilations might preserve the sign but are not useful because they do not reduce the degree of the phase.  The claim about phase degree is plausible but not proved in the output; a more detailed analysis of the transformed phase under even multiplicative shifts would be needed to make this a rigorous obstruction lemma.  Currently it is a heuristic.

---

## 4. Possible errors or hidden assumptions

### 4.1 R5: Are we majorising away useful cancellation?

The residual bound uses the absolute-value form $|R_H(t)|\le \frac{C}{H}K_H(t)$, which is a **positive majorant**.  If the actual residual $R_H(t)$ takes both positive and negative values, summing the absolute kernel over a dyadic block might overestimate the total error.  However, an absolute upper bound on $P(X)$ is sufficient for proving $P(X)\ll X^{1/4+\epsilon}$; we do not need a sharp estimate, only an upper bound.  Therefore using a positive majorant is safe -- it may give a looser constant but does not falsify the desired inequality.  The only risk is if the constant $C$ is extremely large, but it is absolute (e.g. $1/(2H+2)$) and cannot break the power saving.

### 4.2 R5: Double-counting when $m_d$ is not unique

If $X/d$ is exactly halfway between two integers, there are two nearest integers.  The bound $\|X/d\|=1/2$ then $\min(1,\Delta^2/\|t\|^2)$ works with either choice, and both choices lead to the same $|X-md| = d/2$.  When summing over $d$, pairing both possibilities could artificially double the sum.  This is harmless because it at most doubles the constant, still absorbed into $X^\epsilon$.  The rigorous proof can avoid ambiguity by selecting the smaller $m$ (or any deterministic tie-break), and the bound still holds because $\|X/d\|\le |X-md|/d$ for any integer $m$; picking the nearest integer makes the inequality $\|X/d\| \le |X-md|/d$ true with equality up to the constant $1/2$?  Actually, $\|t\|$ is the distance to the nearest integer, so if $m$ is one of the two nearest integers, $|X/d - m|$ is either $\|X/d\|$ or $1-\|X/d\|$?  Wait: if $X/d = 5.5$, then distance to nearest integer $5$ is $0.5$, and to $6$ is $0.5$.  So both give $|X-md|=d/2$.  The inequality $\|X/d\| \le \frac{|X-md|}{d}$ is always true because $\|X/d\| = \min_{m\in\mathbb Z}|X/d - m|$.  So picking any integer $m$ gives $|X-md|/d \ge \|X/d\|$.  In the Fejer bound we use $\|X/d\|$, not $|X-md|/d$ directly.  The gpt argument uses $\|X/d\|\asymp |X-md|/d$ relying on the fact that for the nearest integer $|X-md| \le d/2$, so $\|X/d\| = |X-md|/d$.  That's correct.  If there are two nearest integers, both give the same value $|X-md| = d/2$, which is not "close" but it's not a problem because the Fejer kernel is large there anyway.  So no hidden error.

### 4.3 R5: The assumption that $d$ and $m$ are interchangeable with divisor pairs

When $d$ runs over a dyadic block, $m$ runs over integers around $X/D$.  For a given $n$, the number of representations $n=md$ with $d\sim D$ and $m$ an integer is bounded by $\tau(n)$, but we must also ensure that $m$ is the nearest integer to $X/d$ for that $d$.  However, in the sum we are free to choose $m$ as the nearest integer; for each $d$ we get a unique $m=m(d)$.  Then the map $d\mapsto n = m(d)d$ is many-to-one.  For each $n$, the set of $d$ such that $m(d)d=n$ is a subset of the divisors of $n$, hence of size $\le \tau(n)$.  So the inequality $\sum_{d} f(d) \le \sum_n \tau(n) \max$?  Actually we have $\sum_d \min(1,\frac{\Delta^2}{|X-m(d)d|^2}) = \sum_n \bigl( \sum_{d: m(d)d=n} \min(1,\frac{\Delta^2}{|X-n|^2}) \bigr) \le \sum_n \tau(n) \min(1,\frac{\Delta^2}{|X-n|^2})$.  This is valid.  The fact that $m(d)$ is not arbitrary but the nearest integer does not matter; we only need the bound, not equality.

### 4.4 Gemini's bounded-variation comment: potential confusion

Gemini says: "the parity indicator ... inflates the error bound by $O(D)$".  Actually, if one tries to apply Li--Yang's theorem with $G(d/D)=1_{2\nmid d}$, the theorem's proof would break because the Poisson summation step requires control of the Fourier transform; the indicator's many jumps produce large Fourier tails.  However, the theorem's hypothesis "$G$ is of bounded variation" is a sufficient condition; if the total variation of $G$ is $V$, then the error term usually involves $V$.  For $1_{2\nmid d}$ on interval $[M,2M]$, the total variation is $O(M)$, which is huge, so the bound would be too weak.  So indeed, using the indicator directly is invalid.  The resolution (substituting $d=2m+1$) absorbs the parity into the domain; the coefficient becomes $w_D(2m+1)$, which is smooth.  The phase becomes $F_{2,1}(x)= \frac{1}{2x+1/D}$ which is smooth.  So the theorem could then be applied.  Thus the "penalty" is not fatal; it just forces a change of variable.  Gemini's formulation might give the impression that the residuals cannot be evaluated at all, which is not true.  I will note this nuance in the review.

### 4.5 The claim that $X^{1/4}$ is an "endpoint" relative to Li--Yang

The gpt output says "Li--Yang's final range ... is far below the endpoint height".  The phrasing "endpoint" might be misinterpreted as "Li--Yang cannot handle any sum with $H$ that large".  But Li--Yang's theorem is designed for a specific parameter regime; it is possible that a different configuration of the Bombieri--Iwaniec machinery (e.g., different choice of $N$, $q$, or even a different decomposition) could extend the range.  However, the bound $H\le M T^{-49/164}$ is derived from the structure of the second spacing problem and the choice of $q$-ranges in their optimisation; it seems deeply embedded.  So the obstruction is strong, but it's still a theorem-specific restriction, not an absolute mathematical law.  The review should reflect this nuance.

---

## 5. Suggested synthesis

The most important outcome of Round 9 is the **potential elimination of the residual bottleneck** via R5.  The research direction should therefore shift:

**Previous state:**
The Vaaler residual H5r-F was considered the central hard target; every path seemed to require either Li--Yang-type reciprocal-sum estimates (not available at the endpoint) or a sign-preserving truncation (undemonstrated).  This created a gloomy outlook.

**Post-R5 state:**
If R5 is verified, then the fixed-Fejer residual can be bounded by a simple divisor-product argument, without any high-powered exponential-sum technology.  Consequently, the residual ceases to be the bottleneck.  The proof skeleton then depends **only** on:

* H1--H3 (balanced sawtooth reduction) -- already proved;
* H4 (finite Vaaler with Fejer majorant) -- reference check needed;
* R5 (product-counting for the residual) -- to be written rigorously;
* The **main Vaaler sums** H5a/H5b with exact coefficients -- the new central unsolved problem.

The main sums now become the sole analytic obstacle.  They have the form
\[
S_1 = \sum_{1\le|h|\le H_D} \alpha_h \sum_{d\sim D} \chi_4(d) w_D(d) e(hX/d),
\qquad
S_2 = \sum_{1\le|h|\le H_D} \alpha_h \chi_4(h) \sum_{d\sim D} w_D(d) e(hX/(4d)),
\]
with $H_D\asymp D X^{-1/4}$, $X^{1/4}\le D\le X^{1/2}$, and $|\alpha_h|\ll 1/|h|$.  The earlier arbitrary-coefficient targets H5a-B / H5b-B are **not required**; they should be retained only as stress-test norms.  The proof can aim for estimates that exploit the specific $\alpha_h$ decay and, if possible, the arithmetic of $\chi_4$, without having to control worst-case coefficients.

The Li--Yang theorem remains relevant **only** for the lower part of the $h$-range (perhaps $h\lesssim D X^{-0.3145}$) where it may be legally applied, but the high-frequency part $h\in [D X^{-0.3145}, D X^{-1/4}]$ needs a new idea -- possibly signed Bombieri--Iwaniec matrices incorporating Q1-Ext, or a B-process-first dualisation that avoids the A-process collapse (H7) while still giving some spacing gain.

**Synthesis proposal:**

1. **Promote R5** to a "proposed lemma, pending rigorous write-up and numerical validation".
2. **Downgrade H5r-F** from central bottleneck to "resolved conditional on R5".
3. **Rewrite H5a/H5b** as fixed-coefficient targets (call them H5a-fix, H5b-fix).
4. **Formalise the Li--Yang domain obstruction** (N2-Audit) as a permanent guardrail lemma, combined with the gpt L9.1.
5. **Keep the Mellin--Perron and signed Fourier truncation** as comparison routes, but do not allow them to distract from the main-sum challenge.
6. **Update the best proof draft** to reflect this new dependency tree.

---

## 6. Lemma / claim boxes (for auditing)

**Lemma R5 (Fejer-product residual bound).**
*Hypotheses:* $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, $w_D$ a dyadic weight with $|w_D(d)|\le1$, $K_H(t)=\sum_{|k|\le H}(1-\frac{|k|}{H+1})e(kt)\ge0$, and the Vaaler residual satisfies $|R_H(t)|\le \frac{C}{H}K_H(t)$ for some absolute $C$.
*Conclusion:* $\frac1H \sum_{\substack{d\sim D\\2\nmid d}} |w_D(d)| K_H(X/d) \ll_\epsilon X^{1/4+\epsilon}$, and similarly for the shifted kernel $K_H((X/d+\rho)/4)$, $\rho=1,3$.
*Status:* Proposed; sketch given, full proof needs exact constant and rigorous divisor-sum estimate.

**Lemma N2-Audit (Li--Yang domain clash).**
*Statement:* In the Li--Yang (2023) exponential-sum theorem, the hypothesis includes $H\le M T^{-49/164}$ (Case A) or $H\le M^{35/69}T^{-2/23}$ (Case B).  For $M\asymp X^{1/2}$ and $T=X$, these force $H\le X^{0.2012}$ and $H\le X^{0.1666}$, respectively. The Vaaler endpoint $H\asymp X^{1/4}=X^{0.25}$ violates these bounds; hence the theorem cannot be applied to the full Vaaler frequency range without a new proof.  *Status:* Proved source-audit conclusion.

**Lemma L9.1 (Li--Yang non-import for residual).**
The Vaaler residual H5r-F/B/L1 cannot be directly deduced from Li--Yang (2023) because (i) the required $H$-range exceeds the theorem's domain, (ii) the theorem's exponent $\theta^*>1/4$, and (iii) the theorem's weight hypotheses (bounded variation) do not cover arbitrary coefficients or termwise $L^1$ norms.  *Status:* Proved from source.

**Lemma C3-Mult (Multiplicative parity collapse).**
In the two-coset dual, $\sigma(\xi)=\frac12(-1)^{2\xi}$.  For an integer $a$, $\sigma(\xi)\sigma(a\xi)=\frac14(-1)^{2\xi(1+a)}$.  If $a$ is odd, $2\xi(1+a)$ is an even integer for all $\xi\in\frac12\mathbb Z$; hence the product is identically $1/4$.  Thus odd-dilation differencing erases parity signs.  *Status:* Proved algebraic diagnostic.

**Lemma H10-M (Mellin--Perron dual length).**
For the smoothed Perron integral of $4\zeta(s)L(s,\chi_4)$ with truncation height $T\asymp X^{3/4}$, shifting the contour and applying Stirling's formula localises the active dual variable to $N\asymp X^{1/2}$ and yields a Voronoi/Bessel phase $2\pi\sqrt{nX}$.  Hence the Mellin--Perron route does not avoid the fundamental reciprocal-sum difficulty.  *Status:* Diagnostic scaling argument; explicit kernel and transition estimates needed for full lemma.

---

## 7. Failure modes (explicit enumeration)

1. **R5 fails because the Vaaler majorant constant is too large or not of the simple Fejer form.**
   If the actual Vaaler theorem in H4 uses a different kernel (e.g., a Dirichlet kernel with worse pointwise bound), the product-counting argument might need adjustment.  However, the Fejer-kernel form is standard for Cesaro means; as long as the majorant is still a non-negative kernel with $K_H(t)\ll \min(H, 1/(H\|t\|^2))$, the method works.

2. **R5 underestimates the influence of the second-leg difference.**
   The bound uses $|R_H(t_1)-R_H(t_2)|\le |R_H(t_1)|+|R_H(t_2)|$, which is safe.  If the two residuals cancel partially, the bound might be slightly weaker, but still a valid upper bound.  The $X^{1/4}$ target is unaffected.

3. **The divisor-bound argument implicitly assumes $n$ ranges over integers near $X$, but $m_d$ might be chosen such that $|X-m_d d|$ is not $|X-n|$ because $n=m_d d$ but $m_d$ may not be the integer nearest to $X/d$ in the strict sense?**  Already addressed: choosing the nearest integer ensures $\|X/d\| = |X-m_d d|/d$.  If there is a tie, either $m$ gives the same distance; the product $n$ may differ, but then $|X-n|$ is the same.  So the mapping to $n$ is well-defined up to a harmless finite multiplicity.  The argument remains valid.

4. **The main Vaaler sums H5a-fix cannot be estimated by any known method, and the entire route stalls.**
   This is not a failure of R5, but of the overall proof strategy.  The gpt output acknowledges that the main sums are the remaining hard problem, and that Li--Yang cannot cover the full range.  So this is a known gap, not a hidden error.

5. **Over-reliance on Li--Yang's domain bound may obscure the possibility that the same method could be adapted to larger $H$ by a different choice of $N$ or $Q$.**
   The Bombieri--Iwaniec framework has many adjustable parameters.  It is conceivable that a future paper could extend the range, but until such a paper exists, it is fair to say the current theorem is inapplicable.  The repo should record this as a "theorem-domain obstruction", not a "mathematical impossibility".

6. **C3-Mult's even-dilation case might be exploited in a way Gemini did not consider.**
   This is a theoretical possibility, but Gemini already notes that even dilations do not lower the phase degree, so they are unlikely to yield a spacing gain.  This remains an open sub-question, but not a high-risk failure for the current route.

---

## 8. Concrete stress tests (numerical)

1. **R5 Fejer-product simulation.**
   Write a small script that, for $X$ in a range (e.g., $10^6$ to $10^8$), computes
   \[
   R_F(D) = \frac{1}{H_D} \sum_{d\sim D} K_{H_D}(X/d)
   \]
   (with $H_D = \lfloor D X^{-1/4}\rfloor$, using the explicit Fejer kernel) and compare with $X^{1/4}$.  Do this for several $D$ values, including $D\approx X^{1/2}$, and for $X$ both square and non-square.  Check that the ratio $R_F(D)/X^{1/4}$ does not grow with $X$.

2. **Spike test near rational $X/d$.**
   For a fixed $X$, choose $d$ such that $X/d$ is extremely close to an integer (e.g., $X$ divisible by $d$).  Evaluate $K_H(X/d)$ termwise and see if the product-counting bound is tight or if the positive kernel causes an unexpectedly large contribution from many divisors.  This tests the divisor-bound pessimisation.

3. **Second-leg residual example.**
   Compute the average of $K_H((X/d+\rho)/4)$ over $d$ for a moderate $X$ and verify the bound numerically; pay special attention to $\rho$ that cause alignment with integers.

4. **Abel-summation diagnostic for H5r-F.**
   To test the strength of Fejer averaging versus $L^1$, compute
   \[
   L_1 = \frac1H\sum_{k}|S_\star(k,D)|,\qquad
   A_F = \sum_{k}\eta_{k,H}S_\star(k,D)
   \]
   for a model sum and see if $A_F$ is significantly smaller.  This can inform whether the fixed-Fejer target is genuinely weaker, as suggested by the odd-indicator example $a_k=(-1)^k$.

---

## 9. Confidence calibration and failure modes

* **Confidence in R5 as a correct bound:**
  **High** -- provided the Fejer-kernel majorant is correctly stated.  The product-counting method is elementary and robust; the divisor bound is a well-known theorem.  I see no fatal flaw.

* **Confidence that R5 eliminates H5r-F as a bottleneck:**
  **Moderate-to-High** -- the argument appears to directly bound the fixed-Fejer residual at the required scale.  Once the proof is written and checked against H4, this should be secure.  The only risk is an unforeseen constant factor that leaves a logarithmic loss, but $X^\epsilon$ can absorb logarithms.

* **Confidence that the Li--Yang theorem cannot be applied to the endpoint Vaaler range:**
  **High** -- the source code explicitly contains the parameter restrictions; the numerical violation is clear.  This should be recorded as a permanent lemma.

* **Confidence that the main Vaaler sums are the sole remaining obstacle:**
  **Moderate** -- after the residual is removed, the proof reduces to estimating those sums.  However, it is still possible that the Vaaler main-term decomposition introduces other technical issues (e.g., handling the dyadic partition of the range $D<X^{1/4}$, or the $O(1)$ term from H3).  Those are likely manageable.  The central difficulty is indeed the main reciprocal sums with $\chi_4$.

* **Confidence that the signed Fourier or Mellin--Perron routes provide an alternative:**
  **Low** -- both appear to reproduce the same fundamental obstacles.  They may serve as comparison diagnostics, but not as present proof strategies.

* **Overall confidence that Round 9 has improved the proof status:**
  **High** -- the residual bottleneck is much better understood and plausibly resolved.  This does not yet prove the conjectural bound, but it sharply focuses the effort.

---

## 10. Score by agent

| Agent reviewed        | Score (0--10) | Main reason | Must verify next |
|-----------------------|--------------|-------------|------------------|
| `gpt_pro_thinking`    | 9 | Provides the breakthrough R5 lemma that could remove the central residual bottleneck; precise Li--Yang audit; correct norm correction for H5a/H5b.  Clear, well-structured, and mathematically sound. | Full rigorous proof of R5 (product-counting steps, exact Vaaler majorant reference), numerical stress tests. |
| `gemini_deep_think`   | 7.5 | Supplies a sharper Li--Yang domain obstruction (Case A/B), a useful Mellin--Perron diagnostic, and new parity-collapse lemmas.  However, some statements slightly overstate impossibility and the bounded-variation penalty is not a fundamental barrier.  Less constructive than gpt on the main forward path. | Exact parameter bound extraction from source; clarify that even-dilation case is not proved impossible. |

**Score justification:**

* `gpt_pro_thinking` receives a high score because the R5 idea is genuinely original within the context of this multi-round research log, and if verified, it simplifies the problem dramatically.  The audit and norm recalibration are also useful.  The only minor deduction is for not fully expanding the residual transformation for the second leg, but the sketch is sufficient for Stage A.

* `gemini_deep_think` provides valuable confirmatory analysis, but its constructive forward-moving content is less impactful.  The Li--Yang domain analysis is a refinement of the gpt audit, but it is essentially a deeper investigation of the same obstruction.  The Mellin--Perron equivalence is useful but already conjectured in earlier rounds.  The parity-collapse lemmas are nice algebra but do not currently open a new avenue.  The slight overstatement of impossibility detracts from precision.  Nonetheless, solid work, earning a 7.5.

---

## 11. Next-round recommendation

The next round should focus on **consolidating the residual resolution and attacking the main sums**.  Specific tasks:

1. **For `gpt_pro_thinking`:**
   - Write a complete, rigorous proof of R5, including the exact Fejer-kernel constants, the handling of the second-leg shifts, and the divisor-bound summation.
   - Insert R5 into the best proof draft and explicitly demote H5r-B/L1 to optional stress-test norms.
   - Formulate the fixed-coefficient main-term targets (H5a-fix, H5b-fix) with the actual Vaaler coefficients $\alpha_h$ and the required ranges.
   - Compare these targets with Li--Yang's theorem for the sub-range where it applies ($H\le D X^{-0.3145}$) and identify the uncovered high-frequency gap $H\in [D X^{-0.3145},\, D X^{-1/4}]$.

2. **For `deepseek_api` (this agent):**
   - Run the numerical stress tests proposed in Section 8 to gain empirical confidence in R5.
   - Independently verify the Li--Yang domain constraints from the uploaded TeX source and compare with the range needed for the main sums.
   - Algebraically audit the candidate main-sum estimates: can residue-splitting plus Weil/Deligne complete sums give any saving in the high-frequency region?  Check if the character $\chi_4$ can be used through a finite field extension (e.g., Gaussian integers) to create a genuine complete character sum.

3. **For `gemini_deep_think`:**
   - Soften the impossibility rhetoric where appropriate.
   - Develop a more precise lemma for the Mellin--Perron route with explicit error terms.
   - Analyse whether the even-dilation case in C3-Mult can be turned into a spacing matrix that preserves sign and yields some cancellation; if impossible, explain the technical obstruction (e.g., the phase Hessian remains degenerate).
   - Examine the possibility of a "hybrid" method that applies Bombieri--Iwaniec spacing to the main sums with the exact coefficients and uses Q1-Ext signs to improve matrix norm bounds.

4. **General:**
   - Update the lemma bank and gap register to reflect the new status.
   - Keep the Poisson--Bessel calibration module as a secondary sanity check, but do not let it distract from the main arithmetic route.

**End of Review**
