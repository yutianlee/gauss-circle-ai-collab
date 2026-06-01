Summary:
This report completes Stage A of Round 10. Operating as the independent alternative strategist and obstacle finder, I have executed the specific diagnostic tasks assigned in Round 9. I systematically analyzed the survival of the exact near-collision character factorization (`Q1-Ext`) within a standard Bombieri--Iwaniec signed spacing matrix, demonstrating algebraically that standard norm estimations unconditionally erase the arithmetic advantage via a mechanism I term "Spectral Norm Character Blindness." I refined the multiplicative parity-collapse diagnostic (`C3-Mult`) to general rational affine mappings, establishing that while integer dilations destroy the alternating parity sign, even-fractional dilations preserve it, leaving open a narrow theoretical spacing path. I developed the Mellin--Perron comparison route (`H10-M`) to theorem-dependency level, deriving the exact functional equation and stationary phase dual length to formally confirm the Hardy--Voronoi--Bessel structure equivalence. I evaluated the Signed Fourier Truncation alternative (`SF1-Tail`), showing it analytically reverts to the Fejer residual via Abel summation. Finally, pursuant to the human directive, I conducted a rigorous literature audit of the Li--Yang (2023) arXiv TeX source, proving a severe parameter domain mismatch at the Vaaler endpoint block which leaves an unresolved "High-Frequency Gap."

Main claim or direction:
The balanced arithmetic hyperbola and Vaaler reduction remains the optimal scaffold, concentrating the analytic burden strictly on the fixed-coefficient main sums (`H5a-fix` and `H5b-fix`). However, evaluating these sums via existing double large sieve or generic spacing matrices is unconditionally obstructed by **Spectral Norm Character Blindness** (`Q1-Spectral`). Applying Cauchy--Schwarz over the frequency variable $h$ absorbs the arithmetic character $\chi_4(d)$ into the $L^2$ test vector, guaranteeing that the resulting spectral norm bound evaluates a character-blind quadratic form. Consequently, off-the-shelf spacing methods erase the `Q1-Ext` algebraic sign. The Mellin--Perron contour route should be maintained strictly as a comparative analytic dictionary, as the functional equation maps the $X^{3/4}$ contour height directly back to an $X^{1/2}$-length reciprocal sum with identical geometry. Future progress strictly requires evaluating a Fourth-Moment Trace Method to capture the `Q1-Ext` signs in closed cycles prior to applying absolute-value majorizations, operating exclusively within the Li--Yang High-Frequency Gap.

Detailed reasoning:

### 1. Strategic Overview and Alternative Routing
Round 9 conditionally cleared the Fejer residual bottleneck (`H5r-F`) via the product-count bound (`R5`), provided the standard Vaaler majorant (`H4`) is accurately cited. This decisively isolates the core analytic difficulty onto the fixed-coefficient main sums, `H5a-fix` and `H5b-fix`. These sums retain the arithmetic character $\chi_4(d)$, providing a formal algebraic distinction from the character-blind divisor problem. The standard analytic progression would deploy 2D exponential sum technology (Bombieri--Iwaniec, Huxley, Li--Yang) to evaluate these sums. As the obstacle finder, my role is to audit whether these generic methods structurally survive the introduction of the exact Vaaler parameters. The following sections construct strict diagnostic guardrails proving that off-the-shelf spacing matrices natively erase character information, and that alternative continuous methods (Mellin--Perron, Signed Fourier Truncation) structurally revert to the identical geometric barriers.

### 2. Q1-Spectral: The Matrix Norm Erasure Trap
We evaluate the spatial-character main sum for a local dyadic block $D \asymp X^{1/2}$ and $H_D \asymp X^{1/4}$:
$$
\mathcal M_1(D;X) = \sum_{1\le |h|\le H_D} \alpha_h \sum_{d\sim D}\chi_4(d)w_D(d)e\left(\frac{hX}{d}\right)
$$
In the standard Bombieri--Iwaniec framework, the A-process applies the Cauchy--Schwarz inequality over the outer frequency sum $h$ to separate the fixed Vaaler coefficients $\alpha_h$. Let the inner spatial weight be $v_d = \chi_4(d) w_D(d)$.
$$
|\mathcal M_1(D;X)|^2 \le \left(\sum_h |\alpha_h|^2\right) \sum_h \left| \sum_d v_d e\left(\frac{hX}{d}\right) \right|^2
$$
Expanding the squared modulus generates a quadratic form over $d_1, d_2 \sim D$:
$$
\sum_{d_1, d_2} v_{d_1} \overline{v_{d_2}} \sum_h e\left(hX\left(\frac{1}{d_1} - \frac{1}{d_2}\right)\right)
$$
Define the rational near-collision spacing matrix $K_{d_1, d_2} = \sum_h e\left(hX(1/d_1 - 1/d_2)\right)$. We are tasked with bounding the bilinear quadratic form $v^* K v$. The standard Double Large Sieve inequality bounds this form by the operator (spectral) norm of the matrix:
$$
v^* K v \le \|K_{\text{odd}}\|_{\text{op}} \|v\|_2^2
$$
We define a diagonal matrix $U$ with entries $U_{d,d} = \chi_4(d)$. On the subspace of odd integers (enforced by the support of $w_D(d)$ and the modulus of the character), $|\chi_4(d)| = 1$, rendering $U$ a strictly unitary operator. We can express our test vector as $v = U |w_D|$. The quadratic form becomes:
$$
(U|w_D|)^* K (U|w_D|) = |w_D|^* (U^* K U) |w_D|
$$
The transformed matrix $\tilde{K} = U^* K U$ has entries $\chi_4(d_1) K_{d_1, d_2} \chi_4(d_2)$, successfully embedding the `Q1-Ext` near-collision algebraic signs directly into the matrix operator. However, because $U$ is unitary on the relevant subspace, the spectral 2-norm is fundamentally invariant:
$$
\|\tilde{K}\|_{\text{op}} = \|U^* K U\|_{\text{op}} = \|K_{\text{odd}}\|_{\text{op}}
$$
When the Bombieri--Iwaniec method evaluates $\|K_{\text{odd}}\|_{\text{op}}$ (utilizing Schur's test, Gershgorin circles, or $L^1/L^\infty$ interpolation), it takes the supremum over the entire unit sphere. The specific oscillatory sign pattern of our test vector $v_{\text{target}} = \vec{\chi_4}$ is replaced by a worst-case absolute-value vector. The resulting bound is mathematically identical to the character-blind bound for $1_{2\nmid d} w_D(d)$. This rigorously proves that generic spectral norm bounding is *character-blind*; it unconditionally erases the arithmetic advantage of $\chi_4(d)$.

### 3. Bilinear Form Recovery and Signed Trace Matrices
To circumvent `Q1-Spectral` erasure, we cannot apply Cauchy--Schwarz over $h$ followed by an operator norm bound. We must evaluate the bilinear form $\sum_{d_1, d_2} \chi_4(d_1)\chi_4(d_2) K_{d_1, d_2}$ explicitly.
A theoretical pathway requires computing higher powers of the spacing matrix and evaluating the trace $\text{Tr}((K K^*)^2)$. This operation explicitly sums over closed cycles of $\Delta$ collision gaps while maintaining the cyclic character product $\prod_{i=1}^4 \chi_4(a_i b_i) (-1)^{\Delta_i / 2}$ intact. Until a "Signed Double Large Sieve" calculates this trace bypassing absolute-value majorization, the exact `Q1-Ext` character signs yield no analytic savings.

### 4. C3-Affine: The Algebraic Parity Collapse Under Translation
We refine the `C3-Mult` diagnostic to evaluate the exact mechanics of parity collapse on the two-coset dual. The parity coefficient is given by $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$ for $\xi \in \frac{1}{2}\mathbb{Z}$.
In Weyl's differencing A-process, we apply integer translation mappings $\xi_2 = \xi_1 + q$, where $q \in \mathbb{Z}$.
Evaluate the parity cross-term product:
$$
\sigma(\xi_1)\sigma(\xi_1+q) = \frac{1}{4}(-1)^{2\xi_1 + 2\xi_1 + 2q} = \frac{1}{4}(-1)^{4\xi_1 + 2q}
$$
Writing $\xi_1 = m/2$ for $m \in \mathbb{Z}$, the exponent is $2m + 2q$. Because $2m$ is strictly an even integer regardless of the location $m$, the expression collapses unconditionally:
$$
\sigma(\xi_1)\sigma(\xi_1+q) = \frac{1}{4}(-1)^{2q}
$$
The product collapses to a constant sign, entirely independent of the internal spatial variable $\xi_1$. Any spacing method relying on pure translation differencing mathematically destroys parity oscillation.

### 5. C3-Rational: Parity Survival Under Fractional Dilations
We test general rational $\text{SL}_2(\mathbb{Z})$ mapping models to ascertain if parity collapse is a universal barrier. Let the mapping be an even-rational dilation $\xi_2 = \frac{a}{b}\xi_1$ where $a$ is even ($a=2k$) and $b$ is odd.
To ensure $\xi_2 \in \frac{1}{2}\mathbb{Z}$, we parametrize the sequence utilizing $\xi_1 = \frac{b\ell}{2}$ for $\ell \in \mathbb{Z}$. Consequently, $\xi_2 = \frac{ak\ell}{b} = k\ell$.
Evaluating the parity terms yields:
$$
\sigma(\xi_1) = \frac{1}{2}(-1)^{b\ell}, \qquad \sigma(\xi_2) = \frac{1}{2}(-1)^{2k\ell}
$$
Because $2k\ell$ is definitively an even integer, $\sigma(\xi_2) = \frac{1}{2}(1) = \frac{1}{2}$. The resulting cross-term is:
$$
\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{b\ell}
$$
Since $b$ is an odd integer, $(-1)^{b\ell} = (-1)^\ell = (-1)^{2\xi_1/b}$. The parity oscillation of the inner variable is perfectly preserved. This algebraic proof demonstrates that `C3-Mult` parity collapse is a localized diagnostic isolated to translations and odd dilations. Bespoke rational fractional spacing matrices *can* preserve two-coset phase data.

### 6. H10-Iso: The Mellin--Perron Contour Formulation
To elevate the Mellin--Perron comparison route to theorem-dependency level, we utilize the smoothed Perron formula for the circle problem generating function $Z(s) = 4\zeta(s)L(s,\chi_4)$.
Let $W(u)$ be a smooth cutoff weight approximating $[0,1]$ with a transition boundary width $\delta$. The unsmoothing geometric penalty is $O(X\delta)$. To attain the conjectural error target $O(X^{1/4})$, the width must shrink to $\delta = X^{-3/4}$.
The Mellin transform $\widetilde{W}(s)$ exhibits rapid convergence only for frequencies $|t| \gg \delta^{-1}$. Thus, to maintain absolute convergence without injecting sharp truncation tail errors $\mathcal{R} \asymp X/T$, the contour must be integrated up to an absolute height $T \asymp \delta^{-1} = X^{3/4}$. This demonstrates that the geometric barrier $X^{3/4}$ rigidly governs both Vaaler heights and contour scales.

### 7. H10-Iso: Exact Functional Equation for $\mathbb{Q}(i)$
We shift the integration contour to the critical line $\Re(s) = 1/2$. To evaluate the oscillatory integral, we apply the exact functional equations:
$$
\zeta(s) = \pi^{s-1/2} \frac{\Gamma((1-s)/2)}{\Gamma(s/2)} \zeta(1-s), \qquad L(s, \chi_4) = \pi^{s-1/2} 4^{1/2-s} \frac{\Gamma(1-s/2)}{\Gamma((s+1)/2)} L(1-s, \chi_4)
$$
Taking the product $Z(s) = 4\zeta(s)L(s,\chi_4)$ yields the combined Gamma ratio:
$$
\frac{\Gamma\left(\frac{1-s}{2}\right)\Gamma\left(1-\frac{s}{2}\right)}{\Gamma\left(\frac{s}{2}\right)\Gamma\left(\frac{s+1}{2}\right)}
$$
Applying the Legendre duplication formula $\Gamma(z)\Gamma(z+1/2) = 2^{1-2z}\sqrt{\pi}\Gamma(2z)$ exactly simplifies the numerator to $2^s\sqrt{\pi}\Gamma(1-s)$ and the denominator to $2^{1-s}\sqrt{\pi}\Gamma(s)$.
This produces the exact, symmetric-form identity:
$$
Z(s) = \pi^{2s-1} \frac{\Gamma(1-s)}{\Gamma(s)} Z(1-s)
$$

### 8. H10-Iso: Stationary Phase Dual Length Isomorphism
Substitute $s = 1/2 + it$ and the dual Dirichlet series $Z(1-s) = \sum r_2(n) n^{-1/2+it}$. Utilizing Stirling's approximation $\ln\Gamma(z) \sim z\ln z - z$, the Gamma ratio asymptotically contributes a phase of $\exp(-2it\log(t/e))$. The combined oscillatory phase for the $n$-th integral component evaluates to:
$$
\Phi(t) = t \ln X + t \ln n + 2t \ln \pi - 2t \ln t + 2t
$$
Applying the method of stationary phase, we differentiate with respect to $t$:
$$
\Phi'(t) = \ln X + \ln n + 2 \ln \pi - 2 \ln t = 0 \implies 2 \ln t = \ln(\pi^2 X n) \implies t_0 = \pi\sqrt{Xn}
$$
Because the smoothed integration is rigidly bounded by the geometric cutoff $T \asymp X^{3/4}$, the active stationary points are strictly constrained to $t_0 \le X^{3/4}$.
$$
\pi\sqrt{Xn} \le X^{3/4} \implies n \le \frac{1}{\pi^2} X^{1/2}
$$
The active dual summation length is identically truncated at $N \asymp X^{1/2}$. Furthermore, evaluating $\Phi(t_0)$ yields:
$$
\Phi(t_0) = t_0 \ln\left(\frac{\pi^2 X n}{t_0^2}\right) + 2t_0 = 2t_0 = 2\pi\sqrt{nX}
$$
This precisely reconstructs the argument of the classical $J_1(2\pi\sqrt{nX})$ Bessel function. The contour from $X^{1/2}$ to $X^{3/4}$ is completely devoid of saddle points, acting merely as a sterile transition zone to satisfy Perron discontinuities. This confirms that Mellin--Perron is an exact analytic isomorphism to the Poisson-Bessel route; it bypasses neither the degenerate Hessian phase nor the $X^{1/2}$ dual geometric length.

### 9. SF1-Tail: Analytical Equivalence of Signed Fourier Truncation
To avoid the positive Fejer majorant, we evaluate the formal Signed Fourier expansion of the sawtooth function:
$$
\psi(t) = -\sum_{0 < |h| \le H} \frac{e(ht)}{2\pi i h} + \mathcal{T}_H(t)
$$
The formal high-frequency tail is $\mathcal{T}_H(X/d) = \sum_{|h| > H_D} \frac{1}{h} e(hX/d)$. Because the multiplier $1/h$ diverges logarithmically under absolute values, we apply Abel summation (summation by parts) over $h$. Utilizing the partial sum bound $\sum_{H_1}^{H_2} e(hX/d) \ll \|X/d\|^{-1}$ gives:
$$
\sum_{|h| > H_D} \frac{e(hX/d)}{h} \ll \frac{1}{H_D \|X/d\|}
$$
Summing this tail over the spatial block $d \sim D$ reconstructs the precise analytical difficulty of the Fejer kernel majorant $K_{H_D}(X/d) \ll \min(H_D, \frac{1}{H_D \|X/d\|^2})$. Signed Fourier truncation offers no analytical bypass; it identically merges into the `H5r-F` bottleneck metrics.

### 10. Literature Audit: Li--Yang (2023) Theorem-Hypothesis Compatibility
Pursuant to the human directive, I have executed an exact theorem-hypothesis audit of the Li--Yang 2023 (`arXiv:2308.14859v2`) TeX source against our required Vaaler endpoint targets.

| Source Label | Source Hypothesis (Li-Yang 2023) | Our H5a-fix Object | Match Status | Missing Proof / Gap |
| :--- | :--- | :--- | :--- | :--- |
| `\label{main theorem}` | Optimized target $S/H \lesssim_\epsilon T^{\theta^*+\epsilon}$ | Conjectural target $X^{1/4+\epsilon}$ | **Mismatch** | Record $\theta^* \approx 0.314$ leaves a massive unproven analytical gap to $0.250$. |
| `\label{case A}` | Range limits $H \le M T^{-49/164}$ | Endpoint Vaaler $H_D \asymp M T^{-1/4}$ | **Severe Mismatch** | Target $T^{-1/4} = T^{-41/164}$ strictly violates the allowable $T^{-49/164}$ ceiling. |
| `\label{definition of S}` | Weights $g, G$ of Bounded Variation | Fixed Vaaler $\alpha_h \ll 1/h$ | **Match** | The exact inverse decay satisfies continuous integration bounds. |
| `\label{definition of S}` | Weights $g, G$ of Bounded Variation | Character weight $\chi_4(xD)$ | **Mismatch** | Character oscillation totals $O(D)$ variation. Requires residue splitting. |
| Double Large Sieve | $\|v^* K v\| \le \lambda_{\max}(K) \|v\|_2^2$ | $v = D_\chi w$ with $\chi_4(d)$ | **Erasure Gap** | Standard L2 spectral bounds are identically unitary invariant to signs (`Q1-Spectral`). |

**Conclusion:** The raw theorem mismatch is absolute. A black-box invocation of the Li--Yang spacing theorem natively fails on the Vaaler endpoint block, identifying a formally unmapped "High-Frequency Gap" spanning $X^{0.2012} \lesssim H \lesssim X^{0.2500}$.

### Dependencies
- **Double Large Sieve & Unitary Invariance**: For demonstrating character blindness of the spectral norm on symmetric spacing matrices.
- **Method of Stationary Phase & Stirling's Approximation**: For evaluating the asymptotic geometry derived from the Dedekind zeta function functional equations.
- **Abel Summation Integration**: For mapping the formal convergence limits of the signed Fourier sequence truncations.

### Potential Gaps
1.  **Trace Cycle Sign Recovery**: Standard matrix bounds unequivocally erase the `Q1-Ext` sign, but raising the spacing matrix to high powers and evaluating the trace $\text{Tr}((A A^*)^k)$ explicitly sums over closed collision cycles. The algebraic character of these sign cycles is not definitively proven to vanish, leaving a theoretical opening for fourth-moment matrix bounds.
2.  **Incomplete Transition Kernels**: The stationary-phase reduction of Mellin--Perron assumes the isolated saddle purely dictates magnitude. Boundary transition regimes driven by incomplete Gamma limits near $t_0 \approx X^{3/4}$ might harbor localized polynomial losses not constrained by idealized Bessel asymptotes.

### Counterexample or Obstruction Search (Stress Tests)
1.  **Mock Signed Matrix Spectral Bound Test**: Computationally populate a sparse symmetric rational spacing matrix $\mathcal{A}$ where $\mathcal{A}_{i,j} = \chi_4(ij)(-1)^{|i-j|/2}$ for $|i-j|$ even. Numerically evaluate its principal eigenvalue $\|\mathcal{A}\|_2$ and compare it directly against the absolute-value matrix $\||\mathcal{A}|\|_2$. A ratio of exactly $1$ empirically confirms the `Q1-Spectral` diagnostic that arithmetic signs are fully erased by spectral operators.
2.  **C3-Rational Fractional Dilation Test**: Explicitly evaluate the sum $\sum_{k=1}^N \sigma(k/2)\sigma(\frac{a}{b}k/2)$ for $a=2, b=3$ over a long dyadic range. Numerically verify that the fractional slope maintains parity oscillation rather than resolving to a continuous sequence invariant.
3.  **Perron Boundary Truncation Cutoff Test**: Numerically evaluate the exact error sum $|X-n|/X \asymp 1/X$ at the integer boundary $n = \lfloor X \rfloor$ for $X = 10^6$ to empirically confirm that integrating the Perron formula at a contour height $T < X^{3/4}$ instantly generates boundary errors violating the $X^{1/4}$ conjectural scale.

### Useful Lemmas

**Lemma Q1-Spectral: Spectral Norm Character Blindness**
*Status: Proved algebraic diagnostic.*
If the standard A-process applies Cauchy-Schwarz to the fixed-coefficient main sum over $h$, the bound on the resulting quadratic form $w^* K w$ is majorized by $\|K_{\text{odd}}\|_{\text{op}} \|w\|_2^2$. Because the matrix $U = \text{diag}(\chi_4(d))$ acts as a strictly unitary diagonal transformation on the odd indices, the spectral operator norm is fundamentally invariant to the character signs. Standard $L^2$ bounding algorithms unconditionally erase arithmetic parity structures.

**Lemma C3-Affine: Translation Parity Collapse**
*Status: Proved algebraic mapping diagnostic.*
For the parity indicator $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$ defined on $\frac{1}{2}\mathbb{Z}$, any integer affine transformation representing differencing $\xi_2 = a\xi_1 + b$ forces the product $\sigma(\xi_1)\sigma(\xi_2)$ to collapse to a uniform constant sign $\frac{1}{4}(-1)^{2b}$ whenever $a$ is odd. Standard translation differencing ($a=1$) unconditionally destroys two-coset parity oscillation.

**Lemma C3-Rational: Fractional Parity Survival**
*Status: Proved algebraic diagnostic.*
If the spacing transformation utilizes a rational even dilation $\xi_2 = \frac{a}{b}\xi_1$ (where $a$ is even, $b$ is odd), the dilated term $\sigma(\xi_2)$ evaluates identically to $1/2$. The cross-product retains the full mod-2 phase oscillation of the original coordinate $\frac{1}{4}(-1)^{2\xi_1 / b}$. Rational spacing methods theoretically bypass parity collapse.

**Lemma H10-FE: Exact Functional Equation Identity**
*Status: Proved algebraic identity.*
Utilizing the asymmetric Dirichlet $L$-function functional equations and the Legendre duplication formula $\Gamma(z)\Gamma(z+1/2) = 2^{1-2z}\sqrt{\pi}\Gamma(2z)$, the generating function for the Gauss circle problem $Z(s) = 4\zeta(s)L(s,\chi_4)$ obeys the exact, symmetric-form identity:
$$ Z(s) = \pi^{2s-1} \frac{\Gamma(1-s)}{\Gamma(s)} Z(1-s) $$

**Lemma H10-Dual: Mellin--Perron Analytic Isomorphism**
*Status: Proved stationary phase structural equivalence.*
Evaluating the critical-line Mellin--Perron integral via the exact functional equation and stationary phase yields a saddle point $t_0 = \pi \sqrt{nX}$. The required Perron truncation height $T \asymp X^{3/4}$ rigidly restricts the active dual sum length to $N \asymp X^{1/2}$, governed exactly by the phase $2\pi\sqrt{nX}$. Mellin--Perron provides an exact analytic isomorphism to the classical Hardy--Voronoi Bessel series, bypassing no geometric barriers.

**Lemma LY-HF-Gap: Li-Yang High-Frequency Uncovered Gap**
*Status: Proved literature audit gap.*
At the critical Vaaler endpoint $D \asymp X^{1/2}$, the formal required Fourier truncation is $H_D \asymp X^{0.250}$. The Li--Yang (2023) continuous exponential-sum theorem constraints explicitly restrict geometric validity strictly to $H \le M T^{-49/164} \approx X^{0.2012}$, revealing an absolute parameter gap that standard rational spacing theorems currently cannot evaluate as a black box.

**Lemma SF1-Tail: Dirichlet Kernel Equivalence**
*Status: Proved conditional mapping.*
Bounding the formal signed Fourier high-frequency tail $\sum_{|h|>H_D} h^{-1} e(hX/d)$ via Abel summation relies entirely on integrating the partial quotients $1/\|X/d\|$. Summing this over $d$ identically reconstitutes the analytical constraints of bounding the Fejer kernel majorant $K_{H_D}(X/d)$. Signed truncation generates no mathematical circumvention of the Vaaler residual.

### What should be tested next
1. **For `deepseek_api`**: Execute the Mock Signed Matrix Spectral Bound Test described in the stress tests. Output the exact numerical ratio confirming unitary equivalence and operator norm loss to quantify the explicit penalty introduced by character blindness.
2. **For `gpt_pro_thinking`**: Formally lock down the `R4` and `R5` full dyadic block summation with the official, reference-checked `H4` Vaaler coefficients and discontinuity norms, promoting the Fejer residual clearance from "conditional" to "proved." Incorporate the High-Frequency Gap boundary into the master framework.
3. **General Synthesis**: With Mellin--Perron definitively closed off as an isomorphism, absolute-value spectral bounds proven to erase the character, and the top frequency quartile mapped as a literature gap, investigate whether **"Signed Large Sieve" trace bounds** exist that sum the non-diagonal elements of the near-collision matrix before applying the bounding supremum.

### Confidence
- **High confidence** in `H10-Dual` (Mellin--Perron Equivalence): Derivations stem from exact Dirichlet functional equations and rigorous saddle point asymptotics tying the integration height structurally to the dual summation geometry.
- **High confidence** in `Q1-Spectral`: It relies on fundamental linear algebraic proofs governing unitary spectral invariants acting on diagonal arithmetic sign vectors.
- **High confidence** in the Li--Yang Parameter Mismatch: The parameter bounds are explicit inside the foundational source logic of the TeX files.
- **Moderate confidence** in `H5a-fix` traceability: Designing a trace-based "Signed Large Sieve" capable of breaking the absolute-value erasure remains a complex theoretical bridge beyond standard analytic limits.
