**Summary:**
This report provides an independent algebraic audit of the balanced Vaaler/sawtooth route to the Gauss circle conjecture, executing the five concrete tasks assigned to DeepSeek API in Round 8. The main results are:
(i) the odd-lattice Poisson transform C2 is **proved** under the fixed Fourier convention and its two representations are equivalent;
(ii) explicit stationary-phase constants for C2 are derived and reported;
(iii) the boundary regime $D\asymp X^{1/2}, k\asymp 1$ is shown to be handled by a trivial bound $D/H_D\asymp X^{1/4}$, requiring no stationary phase;
(iv) the residual sums $S_{\mathrm{odd}}$ and $S_\rho$ are **structurally mapped** into the Li--Yang reciprocal double-sum class, confirming that the Li--Yang theorem applies but yields only $\theta^*\approx0.31448$, not the conjectural $\theta=1/4$;
(v) the derivative nondegeneracy lemmas N1/N2 are re-verified with all constants.

No new Gauss circle exponent is proved. The work yields a clean numerical-experiment protocol, a sharpened Abel-summation diagnostic (the Fejer weights are positive and monotone, so H5r-F may be essentially as hard as the arbitrary-coefficient target H5r-B), and a set of explicit failure modes and stress tests. The fixed-Fejer residual target H5r-F is confirmed as the minimal analytic requirement, but its sufficiency for an endpoint exponent remains unsupported by known technology.

**Main claim or direction:**
The balanced arithmetic hyperbola / Vaaler route is a **structured reduction**, not a near-proof. The central bottleneck is the Fejer-residual family H5r-F. To advance, one must either bound H5r-F at the endpoint $X^{1/4+\epsilon}$ (which currently seems beyond Li--Yang technology), replace Vaaler with a sign-preserving truncation whose error term avoids character loss, or find a new method that handles the residual without discarding the arithmetic character. The report provides precise algebraic lemmas, stationary-phase constants, a Li--Yang audit, and a numerical test plan that collectively sharpen the obstruction map.

**Detailed reasoning:**

### 1. Notation and assumptions
We work with the accumulated notation from the reading packet. Let
$X=R^2\ge 1$, $P(X)=N(\sqrt X)-\pi X$, $\psi(t)=t-\lfloor t\rfloor-\frac12$ (floor-compatible sawtooth), $y=\lfloor X^{1/2}\rfloor$.
$\chi_4$ is the non-principal Dirichlet character modulo $4$.
The Fourier convention is $e(t)=e^{2\pi i t}$.
Smooth dyadic weight $w_D$ is supported on $[c_1 D, c_2 D]$ with $0<c_1<c_2$ and satisfies derivative bounds.

The balanced sawtooth identity (H3) is:

$$
P(X)= -4\sum_{a\le y}\chi_4(a)\psi(X/a)
      +4\sum_{b\le y}\Bigl[\psi\Bigl(\frac{X/b+1}{4}\Bigr)-\psi\Bigl(\frac{X/b+3}{4}\Bigr)\Bigr] + O(1).
$$

The finite Vaaler approximation (H4) with local height $H_D\asymp D X^{-1/4}$ ($X^{1/4}\le D\le X^{1/2}$) is:

$$
\psi(t)=\sum_{1\le|h|\le H_D}\alpha_h e(ht)+R_{H_D}(t),\qquad
|R_{H_D}(t)|\le\frac{1}{2H_D+2}K_{H_D}(t),
$$
$$
K_{H_D}(t)=\sum_{|k|\le H_D}\Bigl(1-\frac{|k|}{H_D+1}\Bigr)e(kt).
$$

The residual families after inserting $\psi$ into H3 and applying the Vaaler majorant are:

$$
S_{\mathrm{odd}}(k,D)=\sum_{\substack{d\sim D\\2\nmid d}}w_D(d)e(kX/d),\qquad
S_{\rho}(k,D)=e(k\rho/4)\sum_{d\sim D}w_D(d)e(kX/(4d)),\;\rho\in\{1,3\}.
$$

The minimal fixed-Fejer residual target (H5r-F) is

$$
\Bigl|\frac1{H_D}\sum_{1\le|k|\le H_D}\eta_{k,H_D}S_\star(k,D)\Bigr|\ll_\epsilon X^{1/4+\epsilon},
\qquad \eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
$$

The stronger arbitrary-coefficient target (H5r-B) requires the same bound for all choices $|v_k|\le1$, and H5r-L1 is termwise $L^1$.

We are to verify C2, derive its stationary phase, handle the boundary regime, audit Li--Yang applicability, recheck N1/N2, and design numerical tests.

### 2. Algebraic verification of the odd-lattice Poisson transform (C2)

We fix the Fourier transform convention: $\widehat f(\xi)=\int_{\mathbb R} f(u)e(-\xi u)\,du$ where $e(\theta)=e^{2\pi i\theta}$.
Define $F(u)=w_D(u)e(kX/u)$ and $I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du$.

**Lemma C2-verified (Poisson transform for odd lattice).**
For compactly supported smooth $w_D$,

$$
\sum_{\substack{d\sim D\\2\nmid d}} w_D(d)e(kX/d)
= \frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
= \frac12\sum_{m\in\mathbb Z} I(m)-\frac12\sum_{\mu\in\mathbb Z+1/2} I(\mu).
$$

*Proof.* The indicator of odd integers is $\frac12(1-(-1)^d)$. The first term gives the ordinary Poisson sum $\sum_{d} f(d)=\sum_{m}\widehat f(m)= \sum_m I(m)$. The second term includes $(-1)^d = e(-d/2)$. By the modulation property $\sum_d f(d)e(-\xi_0 d)=\sum_n \widehat f(n+\xi_0)$. With $\xi_0=1/2$ we obtain $\sum_{d}(-1)^d f(d) = \sum_{n} I(n+1/2)$. Hence the two-coset representation follows.

For the alternating representation, write $d=2m+1$ and apply Poisson to $g(m)=F(2m+1)$. A change of variable yields $\sum_m g(m)=\frac12\sum_n e(n/2) I(n/2) = \frac12\sum_n (-1)^n I(n/2)$. Splitting the sum into even and odd $n$ recovers the two-coset form, confirming equivalence. ∎

Thus C2 is algebraically correct and independent of any convention ambiguity once the Fourier transform is fixed as above. The active dual frequencies appear for negative $\xi$ (see next section).

### 3. Stationary-phase constants for C2 (C2-SP)

The integral $I(\xi)$ has phase $\phi(u)=\frac{kX}{u}-\xi u$. A stationary point exists only when $\xi<0$. Write $\xi=-m$ with $m>0$. The stationary point is

$$
u_0=\sqrt{\frac{kX}{m}},\qquad
\phi''(u_0)=\frac{2kX}{u_0^3}= \frac{2m}{u_0}.
$$

The phase at stationary point is $\phi(u_0)=2\sqrt{kX m}$. Using the standard stationary phase formula for $\int w_D(u)e^{2\pi i\phi(u)}du$ (note $e(ht)=e^{2\pi i h t}$), the leading asymptotic is

$$
I(-m)\sim
\frac{w_D(u_0)}{\sqrt{\phi''(u_0)}} e^{2\pi i\cdot 2\sqrt{kX m}+ \frac{\pi i}{4}}
= \frac{w_D(u_0)}{\sqrt{2m/u_0}} e^{4\pi i\sqrt{kX m}+ \frac{\pi i}{4}}.
$$

**Lemma C2-SP (Stationary phase for C2).**
For $m>0$ such that $u_0=\sqrt{kX/m}\in\operatorname{supp} w_D$ and $kX/D^2\gg1$,

$$
I(-m)=\frac{w_D(u_0)}{\sqrt{2m/u_0}} e^{4\pi i\sqrt{kX m}+\pi i/4}
\bigl(1+O\bigl((kX/D^2)^{-1/2}\bigr)\bigr).
$$

The amplitude order is $|I(-m)|\asymp D^{3/2}(kX)^{-1/2}$. For $m$ outside the stationary range (i.e., $|m|\not\asymp kX/D^2$), integration-by-parts gives rapid decay.

*Proof.* Standard stationary phase; the error constant depends on derivatives of $w_D$ and the phase. ∎

This lemma is conditional until the error bounds are fully written, but it is precise enough for scaling arguments.

### 4. The boundary regime $D\asymp X^{1/2}$, $k\asymp1$

For $D\asymp X^{1/2}$, the local Vaaler height is $H_D\asymp D X^{-1/4}\asymp X^{1/4}$. The terms with small $|k|$ (any fixed constant) appear in the H5r-F average with weight $\eta_{k,H_D}\approx 1$. Their contribution is

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|
\le \frac{1}{H_D} D \asymp \frac{X^{1/2}}{X^{1/4}} = X^{1/4}.
$$

The same holds for $S_\rho$. Therefore the trivial bound already yields the conjectural $X^{1/4}$ scale. No cancellation is needed, and stationary phase is not required.

**Lemma B-Boundary.**
For $D\asymp X^{1/2}$ and $|k|\le C$ (any constant $C$),

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|\ll X^{1/4},\qquad
\frac{\eta_{k,H_D}}{H_D}|S_{\rho}(k,D)|\ll X^{1/4}.
$$

*Proof.* $|S_{\mathrm{odd}}(k,D)|\le\sum_{d\sim D}|w_D(d)|\ll D$, and similarly for $S_\rho$. The factor $1/H_D$ together with $H_D\asymp D X^{-1/4}$ gives the bound. ∎

Thus the boundary regime is benign. The real difficulty lies at intermediate $k$ where $k\asymp H_D$ and $kX/D^2\asymp X^{1/4}$ (or larger), where stationary phase or other cancellation estimates are required.

### 5. Audit of Li--Yang/Bombieri--Iwaniec applicability to H5r

The Li--Yang (2023) theorem treats double sums of the shape

$$
\mathscr{S}(H,M,T)=\sum_{h\sim H}\sum_{m\sim M} a_h b_m\, e\bigl(T F(m/M) h\bigr),
$$

with $F$ smooth and nondegenerate ($F'F'''-3(F'')^2\neq0$), and coefficients $|a_h|,|b_m|\le1$. The theorem gives an estimate $O_\epsilon(H M X^{\theta^*+\epsilon})$ with $\theta^*=0.314483\ldots$ in the $X$-aspect (here $X$ in their notation corresponds to our parameter $X$ for the circle problem).

The residual sum $S_{\mathrm{odd}}(k,D)$ appears in H5r-B as the inner sum over $d$. Indeed,

$$
\sum_{k\sim K_0} v_k S_{\mathrm{odd}}(k,D) =
\sum_{k\sim K_0} \sum_{d\sim D} v_k (1_{2\nmid d}w_D(d))\, e(kX/d).
$$

Writing $1_{2\nmid d}=\frac12(1-(-1)^d)$ splits it into two sums, each of which has bounded coefficients. The phase is $kX/d = kX\cdot\frac{1}{d}$, so with $M=D$, $F(x)=1/x$, and $T=X$, we obtain a Li--Yang-type double sum. The nondegeneracy condition for $F(x)=1/x$ is satisfied (see Section 6). The shifted family $S_\rho$ uses $F(x)=1/(4x)$, which also satisfies the condition. The coefficients $v_k$ and $1_{2\nmid d}w_D(d)$ are bounded by $1$.

Thus **the Li--Yang theorem directly applies** to the H5r-B double sums, yielding the best known exponent $\theta^*\approx0.31448$ in the $X$-aspect, not the conjectural $1/4$. This means that if one relies solely on the current Li--Yang technology, the Vaaler route cannot surpass $\theta^*$ without additional input.

**Lemma N2-audit (Li--Yang compatibility).**
The sums appearing in H5r-B (and consequently H5r-F, which is a special case of H5r-B with particular coefficients) are finite linear combinations of double sums of the form

$$
\sum_{k\sim K_0}\sum_{d\sim D} a_k b_d\, e\bigl(kX F_\nu(d/D)\bigr),
$$

where $F_\nu(x)=1/(x+1/D)$ (after residue shift) or $F_\nu(x)=1/(4x)$, both satisfying the Bombieri--Iwaniec derivative nondegeneracy condition. The coefficients satisfy $|a_k|,|b_d|\le 1$. Hence the Li--Yang theorem provides a bound with exponent $\theta^*=0.314483\ldots$ (in $X$-notation), which is strictly larger than $1/4$.

*Status:* The structural mapping is proved; the exponent claim is conditional on the correctness of the Li--Yang theorem as stated in their paper.

This audit confirms that the Vaaler residual is not a new phase class, but it also highlights that bridging the gap from $\theta^*$ to $1/4$ is the essential difficulty.

### 6. Derivative nondegeneracy re-checked (N1/N2)

We verify the nondegeneracy condition for the two modified reciprocal functions that arise after splitting the odd lattice into residue classes mod $2$ or after shifting the second leg.

**Lemma N1-verified (Derivative nondegeneracy).**

1. For $F_{2,1}(x)=\frac{1}{x+1/D}$, with $z=x+1/D$, we have

$$
   F_{2,1}'(x)=-z^{-2},\;
   F_{2,1}''(x)=2z^{-3},\;
   F_{2,1}'''(x)=-6z^{-4},
$$
$$
   F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2 = 6z^{-6}-12z^{-6}=-6z^{-6}\neq0.
$$

2. For $F_2(x)=\frac{1}{4x}$,

$$
   F_2'(x)=-\tfrac14 x^{-2},\;
   F_2''(x)=\tfrac12 x^{-3},\;
   F_2'''(x)=-\tfrac32 x^{-4},
$$
$$
   F_2'F_2'''-3(F_2'')^2 = (-\tfrac14)(-\tfrac32)x^{-6}-3(\tfrac14 x^{-6}) = \tfrac38 x^{-6} - \tfrac34 x^{-6} = -\tfrac38 x^{-6}\neq0.
$$

On compact subintervals of $(0,\infty)$ the expressions are bounded away from zero, satisfying the nondegeneracy hypothesis required by Bombieri--Iwaniec and Li--Yang.

### 7. Numerical stress-test design for H5r-F vs H5r-B vs H5r-L1

Because we cannot execute code, we provide a detailed protocol that a future collaborator (or an arithmetic-capable agent) can implement. The goal is to compare the three residual norms and detect whether the fixed Fejer weights allow cancellation beyond that achievable with arbitrary bounded coefficients.

**Parameters.**
Choose $X$ of moderate size (e.g., $X=10^2, 10^3, 10^4$; also squares $X=n^2$, near-squares $n^2\pm1$, and non-squares). For each $X$, set up dyadic blocks $D$ between $X^{1/4}$ and $X^{1/2}$ (e.g., $D=2^j$). Compute $H_D=\lfloor D X^{-1/4}\rfloor$. For the sum $S_{\mathrm{odd}}(k,D)$, take the integer interval $[D,2D)$ and restrict to odd $d$. Use a smooth weight $w_D(d)$ (for simplicity one may take $w_D=1$ on the interval, but a bump function is safer to avoid endpoint discontinuities).

**Quantities to compute for each block:**

- $R_F = \Bigl|\frac{1}{H_D}\sum_{1\le |k|\le H_D}\eta_{k,H_D} S_{\mathrm{odd}}(k,D)\Bigr|$,
- $R_{L1} = \frac{1}{H_D}\sum_{1\le |k|\le H_D} |S_{\mathrm{odd}}(k,D)|$,
- $R_{B}^{\max} = \max_{v_k\in\{e^{i\theta}\}} \frac{1}{H_D}\Bigl|\sum_{1\le |k|\le H_D} v_k S_{\mathrm{odd}}(k,D)\Bigr|$ (obtained by random search or by taking the $L^1$ norm, since H5r-B is essentially $L^1$).

**Stress test 1 (Fejer spike detection).**
For $X$ a perfect square, identify $d$ such that $X/d$ is near an integer. Record $k$ for which the Fejer kernel $K_{H_D}(X/d)$ is large. Verify whether the Fejer-weighted residual $R_F$ exceeds $X^{1/4+\epsilon}$.

**Stress test 2 (Norm comparison).**
For several $X$ and $D$, compute $R_F$, $R_{L1}$, and $R_{B}^{\max}$. If $R_F$ is significantly smaller (by a factor $> X^{\epsilon}$) than $R_{L1}$ or $R_{B}^{\max}$, this suggests that the fixed Fejer coefficients exploit cancellation not captured by arbitrary-coefficient bounds. If they are comparable, the Abel-summation trap (see Section 9) is numerically supported.

**Stress test 3 (Tail vs. main).**
For $D\asymp X^{1/2}$ and varying $k$, separate the small-$k$ (constant) from the large-$k$ ($k\asymp H_D$) contributions to $R_F$. Confirm that small-$k$ terms are bounded by $X^{1/4}$ trivially, and identify the $k$-range that dominates the residual.

**Stress test 4 (Sensitivity to weight smoothness).**
Replace the smooth weight by a sharp cutoff and recompute $R_F$, $R_{L1}$ to measure the effect of endpoint discontinuities. This tests the necessity of smooth weights for the Vaaler majorant argument.

These tests, even at moderate scale, provide empirical evidence for the difficulty of H5r-F.

### 8. Expansion of the Vaaler residual and the H5r-F norm

We explicitly derive how the Vaaler residual gives rise to the H5r-F form. For a dyadic block $d\asymp D$, after applying the Vaaler approximation to $\psi(X/d)$ in the first leg (and similarly for the second leg), the error from the residual $R_{H_D}$ is bounded by

$$
\Bigl|\sum_{d\sim D}\chi_4(d)R_{H_D}(X/d)\Bigr|
\le \frac{1}{2H_D+2}\sum_{d\sim D}|\chi_4(d)|\,K_{H_D}(X/d).
$$

Expanding the Fejer kernel $K_{H_D}(t)=\sum_{|k|\le H_D}\eta_{k,H_D}e(kt)$ and interchanging sums yields

$$
\frac{1}{2H_D+2}\sum_{|k|\le H_D}\eta_{k,H_D}\sum_{d\sim D}|\chi_4(d)| e(kX/d).
$$

For the first leg, $|\chi_4(d)|=\mathbf 1_{2\nmid d}$, giving exactly $S_{\mathrm{odd}}(k,D)$. The second leg, after absorbing the shift $e(k/4)-e(3k/4)$, produces $S_{\rho}(k,D)$ with similar structure. The constant factor $1/(2H_D+2)$ is $\asymp 1/H_D$. The zero mode ($k=0$) contributes $D/H_D\asymp X^{1/4}$. Hence the nonzero part of the residual is exactly a fixed-Fejer combination of $S_{\mathrm{odd}}$ and $S_\rho$, scaled by $1/H_D$. Therefore the minimal requirement to bound the Vaaler residual is indeed H5r-F.

**Lemma ALG-1 (Vaaler residual leads to H5r-F).**
After applying the finite Vaaler approximation with the Fejer majorant, the total residual contribution from each dyadic block is, up to a multiplicative constant $\le 1$, a linear combination of $S_{\mathrm{odd}}(k,D)$ and $S_{\rho}(k,D)$ with fixed positive weights $\eta_{k,H_D}/H_D$. Consequently, proving H5r-F suffices to control the Vaaler residual, without requiring arbitrary coefficients.

### 9. The Abel-summation trap for H5r-F

A crucial observation: the Fejer weights $\eta_{k,H}=1-|k|/(H+1)$ are positive and monotone decreasing for $k\ge0$. By Abel summation (or simply the convolution structure of the Fejer kernel),

$$
\sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr) a_k
= \frac{1}{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j} a_k.
$$

**Lemma R4-precise (Fejer averaging identity).**
For any sequence $\{a_k\}$,

$$
\sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr) a_k
= \frac{1}{H+1}\sum_{j=1}^{H}A(j),\qquad A(j)=\sum_{k=1}^{j} a_k.
$$

*Proof.* Expand the RHS: $\frac{1}{H+1}\sum_{j=1}^H\sum_{k=1}^j a_k = \frac{1}{H+1}\sum_{k=1}^H a_k\sum_{j=k}^H 1 = \sum_{k=1}^H a_k\frac{H+1-k}{H+1}$. ∎

Applying this to $a_k=S_{\mathrm{odd}}(k,D)$ (and negative $k$ separately) shows that bounding the Fejer average is equivalent to bounding the average of partial sums. If one only has a bound of the form $|A(J)|\ll J X^{\theta}$ for all $J\le H_D$, then the Fejer average inherits the same exponent $\theta$.

**Diagnostic D1 (Abel-summation trap).**
Unless the sequence $S_{\mathrm{odd}}(k,D)$ exhibits sign patterns that cancel beyond what is captured by the partial-sum magnitudes, any estimate of H5r-F that proceeds via partial sums will, at best, achieve the same exponent as a character-blind bound for arbitrary coefficients. This strongly suggests that H5r-F is not automatically easier than H5r-B; the fixed Fejer weights do **not** provide an obvious escape from the partial-sum difficulty. However, this is a diagnostic, not a theorem; it remains possible that a method could directly bound the Fejer average without controlling partial sums with arbitrary signs.

### 10. Character obstruction audit

We compile the current status of character exploitation across all families.

- **H5a (spatial character):** The sum $\sum\chi_4(d)e(hX/d)$ retains the signed character. H7 (proved) shows that direct Weyl differencing collapses the character product to a parity indicator, blocking a naive A-process savings.
- **H5b (frequency character):** The sum $\sum\chi_4(h)e(hX/(4d))$ carries the character on the frequency side. The B-process-first route (H8) transfers it to a dual character, but then the dual phase has zero Hessian (H9) and differencing again hits H7.
- **H5r (residual):** The Fejer majorant replaces $\chi_4$ by the parity indicator $1_{2\nmid d}$ (or no character), completely losing the signed character. Thus H5r is a **character-blind** family.

Consequently, the Vaaler route appears to strip the useful character from the error term, while the main terms resist character-based improvement due to H7--H9. This constitutes a systemic obstruction. Any successful proof must either overcome H5r without relying on character-blind bounds, or replace Vaaler by a truncation that preserves the character in the error term.

### 11. Additional algebraic verifications

**Vaaler majorant check.** The Fejer kernel representation $K_H(t)=\frac{1}{H+1}\bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\bigr)^2$ is standard and follows from the identity $\sum_{k=-H}^H (1-|k|/(H+1))e(kt)= \frac{1}{H+1}\frac{\sin^2\pi(H+1)t}{\sin^2\pi t}$. The bound $|R_H(t)|\le\frac{1}{2H+2}K_H(t)$ is a known Vaaler theorem; we mark it as **pending external reference verification** but accept it for the proof scaffold.

**Discontinuity handling.** The floor-compatible $\psi$ equals $-1/2$ at integers, whereas the Vaaler trigonometric polynomial approximates a centered sawtooth. The difference is absorbed by $R_H(t)$, which is large near integers. The Fejer majorant controls this discrepancy in an $L^1$-average sense. The numerical tests should specifically check points $X/d$ near integers.

### 12. Obstruction summary and failure modes

We now list explicit failure modes that could derail the Vaaler route:

1. **Fejer spike overload.** For squares $X$, many $d$ may have $X/d$ near integers, causing $K_{H_D}(X/d)$ to reach $\approx H_D$. Without strong cancellation in the $d$-sum, the Fejer-weighted residual could exceed $X^{1/4+\epsilon}$ by a large power. This is testable numerically.

2. **H5r-F too hard.** The required endpoint bound for the fixed-Fejer average may simply be unprovable with current technology. The Li--Yang gap shows that even the arbitrary-coefficient version H5r-B is stuck at $\theta^*>1/4$. If H5r-F is essentially equivalent, the route fails.

3. **Abel-summation trap realises.** If numerical tests show $R_F\approx R_{L1}$, then H5r-F offers no advantage, and the route is limited by character-blind divisor-type bounds.

4. **Main-term character unusability.** Even if H5r were controlled, the main families H5a/H5b require endpoint-strength bounds. H7 blocks the simplest A-process, H9 blocks generic two-dimensional decoupling of the dual phase, and no explicit signed B-process estimate has been proved. The character may therefore give no saving anywhere.

5. **Non-majorizing alternatives also fail.** Signed Fourier truncation may have a tail that demands absolute values, recreating H5r. Mellin--Perron applies functional equations that reconstruct Voronoi/Bessel sums of length $\approx X^{1/2}$, which are essentially as hard as the original divisor problem; moreover, controlling the truncation error seems to require $T\gg X^{3/4}$, importing a moment/subconvexity problem.

6. **Undeveloped stationary phase.** The C2 stationary phase derivation is formal; endpoint errors, transition ranges, and uniformity over the local parameter range are not yet rigorously established. A flawed stationary-phase application could invalidate any dual-side estimate.

7. **Boundary $D\asymp X^{1/4}$ with $H_D\asymp1$.** For very small denominator blocks, the Vaaler height is $O(1)$, and the residual $D/H_D$ is $O(X^{1/4})$, but the number of such blocks is $\ll\log X$, safe. However, the transition between trivial and Vaaler-applied blocks must be handled carefully.

### 13. Useful lemmas collected

We list the lemmas verified or formulated in this report. They are presented as formal claim boxes.

> **Lemma C2-verified (Odd-lattice Poisson transform).**
> Let $w_D$ be smooth, $I(\xi)=\int w_D(u)e(kX/u-\xi u)du$. Then
> $$
> \sum_{2\nmid d} w_D(d)e(kX/d)=\frac12\sum_n(-1)^n I(n/2)=\frac12\sum_m I(m)-\frac12\sum_{\mu\in\mathbb Z+1/2} I(\mu).
> $$

> **Lemma C2-SP (Stationary phase for C2).**
> For $m>0$ with $u_0=\sqrt{kX/m}\in\operatorname{supp}w_D$,
> $$
> I(-m)=\frac{w_D(u_0)}{\sqrt{2m/u_0}} e^{4\pi i\sqrt{kX m}+\pi i/4}\bigl(1+O((kX/D^2)^{-1/2})\bigr),
> $$
> amplitude $\asymp D^{3/2}(kX)^{-1/2}$.

> **Lemma B-Boundary (Small-$k$ regime).**
> For $D\asymp X^{1/2}$ and $|k|\le C$, $\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|\ll X^{1/4}$ (trivial bound).

> **Lemma N1-verified (Derivative nondegeneracy).**
> $F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2 = -6(x+1/D)^{-6}\neq0$, $F_2'F_2'''-3(F_2'')^2 = -\tfrac38 x^{-6}\neq0$.

> **Lemma N2-audit (Li--Yang compatibility).**
> The sums $S_{\mathrm{odd}}$ and $S_\rho$ are finite combinations of Li--Yang-type double sums; the Li--Yang theorem applies but gives exponent $\theta^*=0.31448\ldots$, not $1/4$.

> **Lemma R4-precise (Fejer averaging identity).**
> $$
> \sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr) a_k = \frac{1}{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j} a_k.
> $$

> **Lemma ALG-1 (Vaaler residual leads to H5r-F).**
> The Vaaler residual is exactly a fixed-Fejer combination of $S_{\mathrm{odd}}$ and $S_\rho$ up to a bounded constant factor.

> **Diagnostic D1 (Abel-summation trap).**
> H5r-F is equivalent to controlling the average of partial sums; thus any proof that bounds partial sums cannot be easier than H5r-B unless sign patterns are exploited.

### 14. Counterexample / obstruction search

We have not found a counterexample that falsifies the route entirely, because the route is not yet a proof. However, we have identified specific numerical and structural obstructions:

- **Fejer spikes** could produce a counterexample to the scalar residual bound. The stress tests are designed to search for this.
- **The Li--Yang exponent gap** is a structural obstruction: current technology is provably insufficient, so any claim of reaching $X^{1/4}$ must introduce a new idea not present in Li--Yang.
- **Character degeneracy H7/H9** shows that standard tools (A-process, full-rank stationary phase) fail to exploit $\chi_4$; this is an obstruction that any new method must circumvent.

### 15. What should be tested next (prioritized)

1. **Obtain a precise Vaaler theorem reference** and fix the coefficient formula.
2. **Run the numerical stress tests** (Fejer spike, norm comparison, smooth vs. sharp) using a computing environment; these results are crucial for gauging whether H5r-F is genuinely easier.
3. **Resolve the two-coset A-process question:** perform symbolic differencing on the full two-coset dual expression to see if spacing information survives, or if it collapses exactly as the one-sequence model suggests.
4. **Develop the Mellin--Perron alternative** to a comparable lemma level, including exact truncation errors and functional-equation reconstruction of the dual sums.
5. **Formalize the Abel-summation trap as a conditional theorem:** prove that if a method bounds H5r-F via partial sums, then the exponent achievable is at least that of the corresponding character-blind reciprocal-sum bound.
6. **Insert the verified lemmas C2, C2-SP, N1, N2-audit into the lemma bank** to solidify the algebraic foundation.

### Dependencies

- H1--H3 (proved identities) are assumed correct.
- H4 (Vaaler approximation) is an external theorem dependency; the proof uses only the majorant form, which must be verified from a standard reference.
- Li--Yang theorem is taken as a black-box result; its applicability is structurally confirmed, but the exact exponent depends on their published statement.
- Stationary phase lemmas rely on standard asymptotic analysis; the formal error bounds require additional smoothness and uniformity checks.

### Potential gaps

- The Vaaler reference has not been checked; a mismatch in the majorant constant could affect the final constant but not the exponent, provided $H_D\asymp D X^{-1/4}$.
- The equivalence of the two C2 representations is proven, but the stationary phase derivation assumed $kX/D^2\gg1$; the transition region where this is of order 1 needs a separate, more delicate analysis. However, the boundary lemma covers the case where it is small.
- The Fejer-weighted residual includes both signs of $k$; the decomposition into one-sided sums and the application of Abel summation must respect complex conjugation.
- The character $\chi_4$ disappears in H5r; if a signed truncation alternative is pursued, one must bound the high-frequency tail absolutely, which may still force a character-blind estimate.

### Confidence calibration and failure modes

After the above audit, our confidence levels are:

- **Very high** in the algebraic correctness of C2, N1, and the formal Li--Yang mapping.
- **High** in the stationary phase constants up to standard error terms, and in the trivial boundary bound.
- **Moderate** that H5r-F is the true minimal target (the derivation is sound, but the Vaaler reference must be confirmed).
- **Low** that the Vaaler route can improve the exponent beyond $\theta^*$ without a fundamentally new idea, because:
  - H5r is character-blind and structurally a divisor-problem sum;
  - Li--Yang's best exponent is $\theta^*>1/4$;
  - the Abel-summation trap suggests H5r-F is not obviously easier than H5r-B;
  - main-term character exploitation is obstructed by H7--H9.
- **Low** that signed Fourier or Mellin--Perron currently avoid the same difficulty; they are undeveloped and likely recreate hard reciprocal sums.

The primary failure mode is that the Fejer residual simply cannot be bounded at the conjectural scale with known or foreseeable technology. Secondary failure modes include the Abel-summation trap (if true, H5r-F ≈ H5r-B ≈ divisor problem) and the possibility that even if H5r were solved, H5a/H5b remain out of reach because the character cannot be used.

The research stage is that of a **structured reduction with a clearly identified bottleneck**, not a proof of any new bound. Numerical experiments and further theoretical work on non-majorizing truncations are the most promising next steps to clarify the situation.

**Confidence:** No improvement to the Gauss circle exponent has been proved. The report provides a sharper algebraic audit, explicit stationary-phase parameters, a Li--Yang map, and a numerical test plan. Confidence in the route as a viable path to the conjecture is low; confidence in the derived lemmas (excepting the Vaaler reference) is high.
