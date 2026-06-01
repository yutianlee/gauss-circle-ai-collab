# Summary

Round 10 is a precision and audit round. No new Gauss circle exponent has been proved. The central achievement is the algebraic verification of the Fejer product-count bound **R5**, which provisionally clears the fixed-Fejer residual target **H5r-F**, shifting the unresolved bottleneck entirely to the fixed-coefficient main-term sums **H5a-fix** and **H5b-fix**. An independent source audit of Li--Yang (arXiv:2308.14859v2) confirms that the raw Vaaler endpoint block violates all theorem hypotheses; hence Li--Yang cannot be quoted directly. Complete-sum mechanisms (B-process modulo 4) are shown to preserve the character in the dual variable, but they do not by themselves provide an endpoint saving. A uniform stationary-phase outline for the odd-lattice Poisson transform (C2-SPU) is given, with explicit error bounds; the full rigorous proof is not yet committed. The report concludes with a detailed calibration of confidence and an explicit list of failure modes, stress tests, and next actions.

---

# Main claim or direction

The balanced arithmetic hyperbola/Vaaler route remains the correct **structured reduction and diagnostic framework** for the Gauss circle problem. The current proof skeleton is

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal sums},
$$

and the target remains \(P(X)\ll_\epsilon X^{1/4+\epsilon}\). The principal unresolved difficulty is the estimation of the fixed-coefficient main sums **H5a-fix** and **H5b-fix** at the endpoint scale. The Fejer residual, previously the central bottleneck, is now provisionally controlled by R5, conditional on the standard Vaaler majorant H4.

No improvement over the best known exponent \(\theta^*\approx0.31448\) is claimed. The current state is a sharper reduction with a well-identified analytic gap.

---

# Detailed reasoning

## 1. Algebraic Verification of R5 (Fejer product-count bound)

**Lemma R5-Verified.**
Let \(X\ge 2\), let \(X^{1/4}\le D\le X^{1/2}\), let \(H\asymp D X^{-1/4}\), and let \(w_D\) be a dyadic weight supported on \(d\asymp D\) with \(|w_D(d)|\le 1\). Then for every \(\epsilon>0\),

$$
\frac1H\sum_{\substack{d\sim D\\2\nmid d}}|w_D(d)|\,K_H\!\left(\frac{X}{d}\right)\ll_\epsilon X^{1/4+\epsilon},
$$

and for \(\rho\in\{1,3\}\),

$$
\frac1H\sum_{d\sim D}|w_D(d)|\,K_H\!\left(\frac{X/d+\rho}{4}\right)\ll_\epsilon X^{1/4+\epsilon}.
$$

*Proof sketch.*
Recall the Fejer kernel

$$
K_H(t)=\frac{1}{H+1}\!\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^{\!2}\ll\min\!\left(H,\frac1{H\|t\|^2}\right),
$$

where \(\|t\|\) denotes distance to the nearest integer. Hence

$$
\frac1H K_H(t)\ll\min\!\left(1,\frac{1}{H^2\|t\|^2}\right).
$$

For the first leg, take \(t=X/d\). Let \(m\) be the integer nearest to \(X/d\); then \(\|X/d\|\asymp|X-md|/D\) for \(d\asymp D\). With \(\Delta=D/H\asymp X^{1/4}\) the summand is controlled by

$$
\min\!\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by the product \(n=md\) and using the divisor bound \(\tau(n)\ll_\epsilon n^\epsilon\) yields

$$
\frac1H\sum_d |w_D(d)|K_H(X/d)\ll_\epsilon X^\epsilon\sum_{n\asymp X}\min\!\left(1,\frac{\Delta^2}{|X-n|^2}\right)\ll_\epsilon X^{1/4+\epsilon}.
$$

For the second leg, \(\frac{X/d+\rho}{4}\) is close to an integer \(m\) means \(X\approx d(4m-\rho)\). The number of solutions \((d,m)\) with \(d\sim D\), \(4m-\rho\in\mathbb N\), and \(d(4m-\rho)\) lying in an interval of length \(O(\Delta)\) is still controlled by the divisor function times \(\Delta\); the same bound follows. ∎

**Dependencies:** H4 (Vaaler majorant) and the divisor bound \(\tau(n)\ll n^\epsilon\). The implied constants are harmless for exponents.

**Claim R5-Full** (total Vaaler residual bound) follows by summing over all dyadic blocks, both legs, and both signs; the result is \(O_\epsilon(X^{1/4+\epsilon})\).

## 2. Numerical stress-test design for R5

A precise test protocol is given to validate R5 and detect Fejer spikes.

**Test 1 (first leg).**
Choose \(X\) among pure squares \((n^2)\), near-squares \((n^2\pm 10^{-k})\), non-square integers, and random reals. For a set of dyadic scales \(D\in\{X^{1/4}, X^{3/8}, X^{1/2}\}\) compute

$$
S_1(D,X)=\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

with a smooth dyadic weight and compare against \(X^{1/4}\). Confirm that no spike exceeds a constant times \(X^{1/4+\epsilon}\).

**Test 2 (second leg).**
For \(\rho=1,3\) compute

$$
S_{2,\rho}(D,X)=\frac1{H_D}\sum_{d\asymp D}K_{H_D}\!\left(\frac{X/d+\rho}{4}\right).
$$

Verify that congruence restrictions do not inflate the sum beyond the same order.

**Test 3 (Fejer spike locations).**
Identify \(d\) such that \(X/d\) or \((X/d+\rho)/4\) is exactly an integer. Numerically confirm that the contribution is absorbed by the divisor-type bound.

**Test 4 (very small \(k\) zone).**
For \(D\asymp X^{1/2}\) and \(k\le X^\epsilon\), verify that the trivial bound with the \(1/H_D\) factor keeps the total contribution \(O(X^{1/4+\epsilon})\). (Proved in B-Boundary.)

**Warning flags:** If the divisor bound hides a large constant, an extremely large \(X\) test in a CAS would detect growth beyond \(X^\epsilon\). If \(X\) is a perfect square, many \(d\) divide \(X\), potentially aligning Fejer spikes; the test must verify that the bound holds.

## 3. Independent Li--Yang source audit

Using the TeX source of Li--Yang (arXiv:2308.14859v2), the exact hypotheses of the exponential-sum theorem are extracted.

The standard sum is (around line 810):

$$
S:=\sum_{H\le h\le 2H} g\!\left(\frac{h}{H}\right)\sum_{M\le m\le 2M} G\!\left(\frac{m}{M}\right)
e\!\left(\frac{hT}{M}F\!\left(\frac{m}{M}\right)\right),
$$

with \(g,G\) of bounded variation.

Conditions on \(F\) (lines 820-830):

$$
C_r\ge |F^{(r)}(x)|\ge C_r^{-1}\;(r=1,2,3),\qquad
|F^{(1)}F^{(3)}-3(F^{(2)})^2|\ge C_4^{-1}.
$$

**Case (A)** (line 840):

$$
\begin{cases}
H\ge M^{-9}T^4(\log T)^{\frac{171}{140}} & \text{if }M<T^{-\frac{7}{16}},\
$$
2mm]
H\ge M^{11}T^{-6}(\log T)^{\frac{171}{140}} & \text{if }M>T^{\frac{9}{16}},\\[2mm]
H\le MT^{-\frac{49}{164}}.
\end{cases}
$$
**Case (B)** (line 850):
$$
M\le C_5T^{\frac12},\qquad
H\le\min\!\left\{M^{\frac{35}{69}}T^{-\frac{2}{23}},\;B_0M^{\frac32}T^{-\frac12}\right\},
$$
with a constant \(B_0\) depending on the \(C_i\).
**Main theorem** (line 860): if the parameters are in Case (A) and condition (1------) holds, then a bound for \(S/H\) is given; if in Case (B) with an extra reducing condition, the same bound follows from that condition.
Now map the Vaaler block parameters:
$$
T=X,\qquad M=D,\qquad H=H_D\asymp D X^{-1/4}.
$$
Take the raw endpoint \(D=X^{1/2}\). Then
$$
H_D\asymp X^{1/4},\qquad MT^{-49/164}=X^{1/2-49/164}=X^{33/164}\approx X^{0.2012}.
$$
Since \(X^{0.2012}<X^{0.25}\) for large \(X\), the inequality \(H\le MT^{-49/164}\) forces \(H\) to be smaller than the Vaaler height; Case (A) is incompatible. Case (B) requires \(H\le M^{35/69}T^{-2/23}=X^{(1/2)(35/69)-2/23}=X^{23/138}\approx X^{0.1667}\), even more restrictive. Thus **Li--Yang's main theorem cannot be quoted directly on the raw Vaaler endpoint block**. This is the proved lemma LY-Raw-Mismatch.
= 4. Li--Yang endpoint non-import: precise statement
> **Lemma LY-Raw-Mismatch (proved).**
> For \(T=X\), \(M=D\asymp X^{1/2}\), \(H=H_D\asymp X^{1/4}\), the conditions of Case (A) and Case (B) in Li--Yang's main theorem are violated. Hence no direct application of the theorem yields an estimate for \(S/H\) in this regime.
*Proof.*
Case (A) demands \(H\le MT^{-49/164}\). The left side \(\asymp X^{1/4}\), the right side \(=X^{33/164}\). For \(X>1\) we have \(X^{1/4}>X^{33/164}\).
Case (B) demands \(H\le M^{35/69}T^{-2/23}\). The right side equals \(X^{23/138}\), again smaller than \(X^{1/4}\).
The extra reducing condition is irrelevant because the basic case already fails. ∎
This does **not** forbid a full Bombieri--Iwaniec dissection with different effective parameters, but it shows that published technology does not reach the endpoint.
= 5. Complete-sum mechanism audit for main terms
The main-term targets H5a-fix are
$$
\mathcal M_1(D;X)=\sum_{1\le|h|\le H_D}\alpha_h\sum_{d\sim D}\chi_4(d)w_D(d)\,e(hX/d),
$$
with \(\alpha_h\ll |h|^{-1}\) and \(H_D\asymp D X^{-1/4}\).
**Residue-class splitting.**
Write \(\chi_4(d)=1_{d\equiv1\pmod4}-1_{d\equiv3\pmod4}\). Then \(\mathcal M_1\) is a difference of two ordinary reciprocal sums, each with a congruence condition. The algebraic sign can disappear if the two sums are bounded separately by absolute values; keeping the sign requires a signed large-sieve or a spacing analysis that respects the difference.
**Gauss-sum transfer via B-process (H8).**
Poisson summation modulo 4 transforms the spatial character into a dual character:
$$
\sum_{r\bmod4}\chi_4(r)e(n r/4)=2i\,\chi_4(n).
$$
Thus the dual sum carries \(\chi_4\) on the frequency variable -- a genuine **complete Gauss sum**. Nevertheless, the dual phase \(2\sqrt{Xhm}\) has zero continuous Hessian (H9), so generic two-dimensional stationary phase cannot be applied. Furthermore, a direct A-process in the dual variable triggers H7 again. Consequently, the presence of a complete Gauss sum does **not** by itself provide an endpoint saving; it repackages the same reciprocal-sum difficulty.
**Two-coset formulation** (for the odd-lattice Poisson transform) may allow spacing gains if the two cosets are kept intertwined, but the simple translation-invariant differencing loses the sign (C3-Ext). Non-translation symmetries remain speculative.
**Conclusion regarding main terms:** No complete-sum mechanism is known that yields an unconditional improvement beyond the Li--Yang/Bombieri--Iwaniec framework. The character \(\chi_4\) has modulus 4; its presence does not soften the reciprocal-sum difficulty without a new analytic idea.
= 6. Uniform stationary phase for C2 (C2-SPU)
**Lemma C2-SPU (outline).**
For the odd-lattice Poisson transform
$$
S_{\mathrm{odd}}(k,D)=\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2),\qquad
I(\xi)=\int_{\mathbb R} w_D(u)\,e^{2\pi i(kX/u-\xi u)}\,du,
$$
only \(\xi=-m<0\) yields a stationary point. Define
$$
\phi(u)=kX/u+mu,\qquad u_0=\sqrt{kX/m}.
$$
Assume \(w_D\in C^\infty_c([c_1 D,c_2 D])\) with \(0<c_1<c_2\) and \(\|w_D^{(j)}\|_\infty\le C_j D^{-j}\). Then in the interior range \(m\asymp kX/D^2\),
$$
I(-m)= \frac{w_D(u_0)}{\sqrt{2m/u_0}}\,e\!\left(2\sqrt{kXm}+\frac18\right) + R,
$$
with
$$
|R|\le C(\varepsilon)\Bigl(\frac{D}{\sqrt{kXm}}\Bigr)\bigl(D^{-1}+\delta(m,k,D)\bigr),
$$
where \(\delta(m,k,D)\) measures the relative distance of the stationary point to the support boundary. Outside the stationary range, integration by parts gives exponential decay.
*Proof sketch.*
Scale \(u=Dv\); the phase becomes \(\psi(v)=2\pi(\Lambda v^{-1}+Mv)\) with \(\Lambda=kX/D\), \(M=mD\). Apply a smooth partition of unity to isolate the stationary point; on the stationary piece use a quadratic change of variable whose error is controlled by third-derivative bounds; on the nonstationary pieces estimate by repeated integration by parts. The boundary case where the stationary point is near the support edge is treated by a half-space asymptotic with remainder \(O(|\phi''(u_0)|^{-1}+\text{dist}(u_0,\partial)^{-1})\). ∎
**Consequences for the Vaaler route.**
In the interior regime the leading amplitude is \(\asymp D^{3/2}(kX)^{-1/2}\) and the error is smaller by \((kX/D)^{-1/2}\). The boundary regime \(m\approx1\) (i.e., \(k\) small or \(D\) near \(X^{1/2}\)) is already handled by the trivial bound B-Boundary. A fully rigorous proof with explicit constants remains to be committed (gap C2-SPU-Gap).
= 7. Additional obstruction diagnostics
**Q1-Ext (near-collision character factorization).**
For odd \(a,b\) and \(\Delta=d_1b-d_2a\),
$$
\chi_4(d_1)\chi_4(d_2)=\chi_4(ab)(-1)^{\Delta/2}.
$$
This exact congruence lemma is correct, but when inserted into a Bombieri--Iwaniec spacing matrix, standard Cauchy--Schwarz or large-sieve norms replace the sign by \(1\), erasing any gain. Hence the lemma is algebraically true but analytically neutral until a signed matrix norm is constructed.
**C3-Ext (two-coset parity collapse).**
The Poisson modulo 2 representation yields coefficients \(\sigma(\xi)=\frac12(-1)^{2\xi}\). Under translation-invariant differencing, the product \(\sigma(\xi_1)\sigma(\xi_2)\) is independent of \(\xi_1\); thus a naive A-process loses parity information. This does not rule out spacing arguments that compare the two cosets directly.
**Signed Fourier truncation alternative.**
The high-frequency tail formally preserves \(\chi_4\) but no endpoint tail estimate exists. Bounding it absolutely recreates a character-blind H5r-type problem.
**Mellin--Perron route.**
After functional equations, the problem likely reconstructs Hardy/Voronoi/Bessel sums of length \(\sim X^{1/2}\) and phase \(\sqrt{Xnh}\); hence it mirrors the same core difficulty and is not a shortcut.
= 8. Failure modes (explicitly listed)
1. **R5 divisor-bound insufficiency.** If the divisor function has a large constant, the \(X^\epsilon\) loss might hide a factor growing with \(X\). No counterexample is known, but extremely large-scale numerics could reveal this failure.
2. **Fejer spike alignment in square \(X\).** When \(X\) is a perfect square, many \(d\) satisfy \(d\mid X\), creating many exact integer \(X/d\) alignments. The product-count argument uses \(\tau(n)\ll n^\epsilon\), which might not be sharp enough if the constant is enormous; a targeted numeric test is required.
3. **Stationary-phase error blow-up.** The uniform C2-SPU must control transition regions where the stationary point approaches the support boundary. If not handled carefully, the error could dominate, invalidating subsequent Bombieri--Iwaniec bookkeeping. This is a technical gap.
4. **Vaaler majorant unremovable positivity.** The Fejer kernel is positive, so the residual is bounded only by an absolute-value sum. This forces character-blind estimates for H5r. R5 shows that such blind estimates can still reach the conjectural scale, but it relies on the divisor bound; if the bound hides a large constant, the positivity could still be problematic.
5. **Li--Yang theorem mismatch is not absolute.** A future Bombieri--Iwaniec dissection might change the effective parameters so that the theorem's conditions become applicable. The present audit only applies to the raw Vaaler block; a full dissection could close the gap, but no such dissection exists.
6. **Main-term character cancellation via higher-degree complete sums.** Attempts to embed \(\chi_4\) in a larger modulus (e.g., Gaussian integers) might exploit geometry, but no concrete transformation has been formulated. This remains a speculative escape.
= 9. Counterexample search and concrete stress tests
In addition to the R5 numerical tests (Section 2), the following are proposed:
- **C2 stationary-phase stress test.** For \(X\) large and \(D\) in the critical range, compute \(\widehat f(m)\) numerically and compare with the leading term. Test regimes where \(m\) is small (\(kX/D^2\approx1\)) and where the stationary point is near the support edge.
- **Q1-Ext signed matrix simulation.** Build a small matrix with entries \(\chi_4(d_1)\chi_4(d_2)\) restricted to near-collisions, compute its spectral norm, and compare with the norm of the absolute-value matrix. A systematic reduction would motivate a signed large-sieve inequality.
- **H5r-F vs H5r-B numerical comparison.** For moderate \(X\) (e.g., \(X=10^6\)), compute actual Fejer-weighted sums and compare with the dyadic \(L^1\) norm. If the Fejer average is significantly smaller, it suggests that the fixed coefficients give cancellation; if they are similar, the Abel-summation bottleneck is active.
- **Fejer spike location test.** Choose \(X\) a perfect square and \(D\) such that many \(d\) divide \(X\). Then \(X/d\) is integer for those \(d\), potentially creating Fejer spikes. Check whether the sum stays within the \(X^{1/4}\) scale.
- **Full R5-Full block summation test.** With a CAS, sum the Fejer residual over all dyadic blocks for a range of \(X\) up to, say, \(10^9\) to verify the bound empirically.
= 10. Useful lemmas (claim boxes)
> **Lemma R5-Full (total Vaaler residual bound).**
> Assume H4 and R5 for every dyadic block. Then the total Vaaler residual contribution in the balanced sawtooth formula is \(\ll_\epsilon X^{1/4+\epsilon}\).
> **Lemma LY-Raw-Mismatch (proved).**
> Li--Yang's main theorem (Case (A) and Case (B)) does not apply to the raw Vaaler endpoint block \(T=X\), \(M=D\asymp X^{1/2}\), \(H=H_D\asymp X^{1/4}\).
> **Lemma Main-Complete-Sum-Status (algebraic observation).**
> B-process modulo 4 produces a genuine complete Gauss sum \(2i\chi_4(n)\), but the resulting dual sum retains the same reciprocal-sum hardness and the A-process degeneracy (H7) reappears. No unconditional saving follows from this mechanism alone.
> **Lemma C2-SPU-Statement (uniform stationary phase outline).**
> As in Section 6, a rigorous leading term with error bounds can be proved using standard techniques, contingent on a careful treatment of boundary and support conditions. The complete proof is not yet committed.
> **Lemma H5r-F-Clear (provisionally resolved).**
> R5 together with H4 shows that the fixed-Fejer residual H5r-F is bounded by \(O_\epsilon(X^{1/4+\epsilon})\). The H5r-F target is therefore no longer an active bottleneck.
> **Lemma LY-Endpoint-Gap (diagnostic).**
> The gap between the Vaaler height \(H_D\asymp D X^{-1/4}\) and the Li--Yang permissible heights is
$$
D X^{-\theta^*} \lesssim H \lesssim D X^{-1/4},
$$
with \(\theta^*=0.314483\ldots\). The Vaaler main-term block lies entirely in the uncovered high-frequency region.
> **Lemma Q1-Ext-Status (algebraic, not analytic).**
> The near-collision character factorisation is exact, but its analytic value is nil until inserted into a signed spacing estimate.
> **Lemma B-Boundary (proved).**
> For \(D\asymp X^{1/2}\) and \(1\le|k|\le X^\epsilon\),
$$
\frac1{H_D}|S_\star(k,D)|\ll_\epsilon X^{1/4+\epsilon},
$$
where \(S_\star\) is any residual family.
-
= Dependencies
- H1, H2, H3 (balanced sawtooth identities) -- proved.
- H4 (finite Vaaler theorem with Fejer majorant) -- external theorem, exact reference and normalization to be verified.
- R5 -- conditional on H4 and the divisor bound.
- Any further analytic estimate for H5a-fix/H5b-fix would depend on a full Bombieri--Iwaniec dissection or a new spacing estimate.
= Potential gaps
1. **Exact H4 reference not yet fixed.** The Fejer normalization must be confirmed from a standard source (e.g., Vaaler's original paper). The proof uses the majorant \(|R_H(t)|\le (2H+2)^{-1}K_H(t)\); the constant is harmless but must be cited.
2. **R5 second-leg details not fully written.** The congruence condition \(X\approx d(4m-\rho)\) is plausible but requires a rigorous treatment of near-integrality and the interaction with the divisor bound.
3. **C2-SPU uniform error bounds incomplete.** A fully rigorous stationary-phase lemma with boundary treatments is not yet committed; this could affect any subsequent Bombieri--Iwaniec dissection.
4. **Signed Fourier tail and Mellin--Perron alternatives are undeveloped.** They remain comparison routes without endpoint estimates.
5. **The critical high-frequency gap for H5a-fix/H5b-fix is not closed.** Current technology (Li--Yang) yields \(\theta^*\approx0.31448\), not \(\theta=1/4\). A new analytic input is required.
= Counterexample or obstruction search
All candidate obstructions (H7, H9, C3-Ext, etc.) have been checked algebraically and do not rule out the route globally; they instead block naive one-step methods. The most concrete obstruction is the Li--Yang parameter mismatch (LY-Raw-Mismatch), which is a directly verifiable violation of published hypotheses. The counterexample search focuses on numerical tests for R5 and the Fejer spikes, as described in Section 2 and Section 9.
= Useful lemmas
(Repeated from Section 10 for completeness.)
1. R5-Full (total Vaaler residual bound).
2. LY-Raw-Mismatch (Li--Yang non-applicability).
3. Main-Complete-Sum-Status (no unconditional saving from B-process).
4. C2-SPU-Statement (stationary-phase outline).
5. H5r-F-Clear (residual cleared provisionally).
6. LY-Endpoint-Gap (frequency gap).
7. Q1-Ext-Status (algebraic only).
8. B-Boundary (small-k bound).
= What should be tested next (prioritised)
1. **Complete the R5 proof** with all second-leg details and treatment of non-integer \(X\).
2. **Verify H4 from a standard Vaaler reference**, fixing the exact coefficients and majorant normalization.
3. **Run the numerical tests** of Sections 2 and 9 to confirm R5 and detect any Fejer spike anomalies.
4. **Carry out a full Bombieri--Iwaniec dissection for H5a-fix/H5b-fix** -- determine effective parameters and identify exactly where the Li--Yang conditions break.
5. **Investigate signed large-sieve / "two-coset" spacing** to see if the character sign can be retained beyond the first Cauchy--Schwarz.
6. **Resolve C2-SPU** by providing a complete, referenced uniform stationary-phase lemma.
7. **Update the best-proof-draft** with the status changes (R5-Full, LY-Raw-Mismatch, etc.) and note the remaining main-term gap.
= Confidence calibration and failure modes
**Confidence levels:**
- *High confidence* in the selected arithmetic route as the correct reduction framework.
- *High confidence* that R5 is algebraically sound and clears H5r-F provisionally.
- *High confidence* that Li--Yang cannot be quoted directly on the raw Vaaler endpoint (LY-Raw-Mismatch is proved).
- *High confidence* that the B-process complete-sum mechanism does not provide an unconditional endpoint saving.
- *Moderate confidence* in the C2-SPU leading term and error scaling; the uniform proof is standard but incomplete.
- *Moderate confidence* that the Vaaler main-term sums are structurally within the Bombieri--Iwaniec class, but *low confidence* that existing technology reaches the required exponent.
- *Low confidence* that signed Fourier truncation or Mellin--Perron routes avoid the core reciprocal-sum difficulty.
- *Overall:* No new Gauss circle exponent has been proved. Round 10 increases precision but does not alter the fundamental gap.
**Explicit failure modes** (cf. Section 8):
1. R5 divisor-bound insufficiency under extremely large constants.
2. Fejer spike alignment for square \(X\).
3. Stationary-phase error blow-up in C2-SPU.
4. Positive Fejer majorant forcing absolute values that cannot be compensated.
5. Li--Yang mismatch not absolute; a future dissection could still close the gap.
6. Speculative higher-degree complete sums would require a completely new geometric approach.
= Confidence
High confidence that the structured reduction is correct and that the residual bottleneck is provisionally cleared. Moderate confidence in the stationary-phase outline; low confidence that the main-term gap can be closed with present technology. No exponent improvement is proved. The next step must either find a new signed spacing estimate or a fundamentally different analytic mechanism.
