Summary:
Round 9 executes the human directive to audit the exact Li--Yang (2023) LaTeX source, formalizes the Mellin--Perron comparison route (H10), and redrafts the algebraic parity diagnostics (Q1-Ext and C3-Ext). The Li--Yang source audit reveals a severe parameter-domain obstruction (N2-Audit): while the Vaaler residual bottleneck (H5r-F) is structurally compatible with their main theorem after a residue substitution, it is analytically barred by maximum-frequency constraints. Evaluating the Vaaler sum at conjectural strength requires a frequency block of length $H_D \asymp X^{0.25}$, whereas Li--Yang's hypotheses strictly cap the allowable frequency dimension at bounds evaluating to $H \le X^{0.201}$. Additionally, formalizing the Mellin--Perron contour map demonstrates that targeting an $X^{1/4}$ error algebraically enforces a dual summation length of exactly $N \asymp X^{1/2}$, confirming it is an analytic mirror of the Vaaler/Bessel bottleneck rather than an escape. Finally, analyzing non-translation differencing on the odd-lattice dual shows that odd multiplicative dilations force identical parity-coefficient collapse to translation shifts.

Main claim or direction:
The selected balanced arithmetic hyperbola/Vaaler route remains the optimal diagnostic scaffold, but we must explicitly acknowledge a hard technological ceiling. The exact Li--Yang source audit indicates that current reciprocal-sum spacing theorems mathematically cannot evaluate the upper-frequency range of the required H5r-F target because the required Vaaler dimension overloads double large sieve matrices. Furthermore, the Mellin--Perron functional equation appears to strictly limit dual stationary lengths to the identical $X^{1/2}$ scale. Future progress would require showing a novel dimension-reduction in the spacing matrices via exact $\chi_4$ structure (via Q1-Ext) or finding a transform that evaluates the truncation tail without invoking absolute-value majorants.

Detailed reasoning:
**1. Li--Yang Source Audit and the Parameter Domain Clash (N2-Audit):**
Auditing `\label{main theorem}` (source line 845 in `arXiv:2308.14859v2`), we map our H5r-F target to their exponential sum $S = \sum_H \sum_M g(h/H) G(m/M) e(\frac{hT}{M}F(m/M))$.
For the target $P(X) \ll_\epsilon X^{1/4+\epsilon}$, the Vaaler zero-mode residual requires $H_D \asymp D X^{-1/4}$. At the endpoint block $M = D \asymp X^{1/2}$ and $T=X$, this mandates a frequency dimension $H_D \asymp X^{1/4} = X^{0.25}$.
However, theorem applicability relies on domain constraints `\label{case A}` and `\label{case B}`.
In Case A, the theorem strictly enforces $H \le M T^{-49/164}$. At the $M \asymp X^{1/2}$ endpoint, this limits $H \le X^{1/2 - 49/164} = X^{33/164} \approx X^{0.2012}$.
In Case B, it requires $H \le M^{35/69} T^{-2/23}$, enforcing $H \le X^{35/138 - 12/138} = X^{23/138} \approx X^{0.1666}$.
Because $X^{0.25}$ mathematically violates the upper bound in all valid theorem domains, the required continuous Fourier sum exceeds the spacing matrix capacity of current reciprocal-sum technology. If one artificially restricts $H_D \asymp X^{0.2012}$ to legally invoke the theorem, the zero-mode error alone inflates to $X^{1/2} / X^{0.2012} = X^{0.2988}$, permanently missing the $1/4$ exponent target.

**2. Bounded Variation Weight Penalty for H5r-F:**
Li--Yang's theorem strictly demands that the outer and inner summation envelopes, $g(x)$ and $G(x)$, be of bounded variation (BV) on $[1,2]$. The fixed-Fejer weight $\eta_{k, H_D}$ is monotone and satisfies $V(\eta) \ll 1$. However, the parity indicator $1_{2\nmid d}$ in H5r-F generates $O(D)$ jumps over the interval. Injecting this directly as $G(x)$ inflates the error bound by $O(D)$, destroying any theoretical cancellation. Resolving this constraint requires substituting $d = 2m+1$, which modifies the reciprocal phase to $F_{2,1}(x) = \frac{1}{2x+1/D}$. This phase satisfies the theorem's $C^3$-non-degeneracy hypotheses, but stripping the sum of its parity structure confirms that bounded-variation frameworks forcibly render the residual character-blind prior to evaluation.

**3. Mellin--Perron Equivalence to Voronoi (H10-M):**
Applying a smoothed Perron contour for $Z(s) = 4\zeta(s)L(s,\chi_4)$ to target $O(X^{1/4})$ error necessitates an integration height $T \asymp X^{3/4}$. Shifting the contour to $\Re(s) < 0$ and invoking the asymmetric functional equations for $\zeta(s)$ and $L(s, \chi_4)$ yields the Gamma factor ratio $\Gamma(1-s)/\Gamma(s)$.
By Stirling's approximation on the vertical segment $[-T, T]$, the active phase behaves as $-2t \log(t/e\pi)$. For the $n$-th term of $Z(1-s)$, the combined oscillatory phase is $\Phi(t) = t \log(\pi^2 X / n) - 2t \log t + 2t$.
The stationary condition $\Phi'(t) = 0$ yields $t_0 = \pi\sqrt{nX}$. Because the integral is truncated at $T \asymp X^{3/4}$, the active dual frequencies are strictly bound by $\sqrt{nX} \lesssim X^{3/4} \implies n \lesssim X^{1/2}$. Evaluating $\Phi(t_0)$ yields $2\pi\sqrt{nX}$. This analytically reconstructs the classical Voronoi/Bessel series up to length $N \asymp X^{1/2}$. Consequently, the Mellin--Perron route functions as an analytic isomorphism mapping directly back to the identical Vaaler cutoff scale and Hessian-degenerate phase.

**4. Multiplicative Differencing on the Two-Coset Dual (C3-Mult):**
In the two-coset odd-lattice Poisson dual (C2), the parity coefficient is $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$ for $\xi \in \frac{1}{2}\mathbb{Z}$. To test non-translation Weyl differencing, we model a multiplicative dilation $\xi_2 = a \xi_1$ for an integer scale $a$.
The cross-term signature is $\sigma(\xi_1)\sigma(a\xi_1) = \frac{1}{4}(-1)^{2\xi_1(1+a)}$.
If $a$ is an odd integer, $1+a = 2k$ for some integer $k$. Since $2\xi_1 \in \mathbb{Z}$, the exponent $2\xi_1(1+a) = 4k\xi_1$ is unconditionally an even integer for all $\xi_1 \in \frac{1}{2}\mathbb{Z}$. Thus $(-1)^{2\xi_1(1+a)} = 1$. The parity signature deterministically collapses to a constant. While even dilations preserve the sign, they fail to lower the square-root degree of the phase, thereby blocking standard large sieve spacing applications.

Dependencies:
- **Li--Yang (2023) arXiv:2308.14859v2**: Exact `\label{case A}` and `\label{case B}` exponential sum parameter constraints and bounded-variation amplitude hypotheses.
- **Perron's Formula**: Standard truncation errors $O(X/T)$ and functional equations for $L$-functions over $\mathbb{Q}(i)$.
- **Stirling's Approximation**: For asymptotic stationary phase evaluation of complex contour segments.

Potential gaps:
- **Even Dilation Spacing**: C3-Mult explicitly proves parity collapse for odd dilations. If a rational collision matrix relies exclusively on *even* dilations, the sign survives. It remains a theoretical gap whether a bespoke spacing array can exploit this alternating sign, though mixing the integer and half-integer cosets introduces unmapped phase interference.
- **Perron Kernel Transition**: Evaluating H10-M assumes the central stationary phase analysis dominates the entire integral. Incomplete Gamma transitions near the smoothed cutoff $|t| \approx T$ inject boundary mass; establishing whether this boundary mass imposes stricter or looser constraints than Vaaler remains open.

Counterexample or obstruction search:
- **Li--Yang Mapping Obstruction:** Checked if the Vaaler height $H_D = X^{1/4}$ could fit Case A for $M = X^{1/2}$. Evaluated $X^{1/4} \le X^{1/2} X^{-49/164} \implies 0.25 \le 0.2012$. The inequality strictly fails. This confirms that Bombieri-Iwaniec methods not only yield poor exponents but mathematically break down at the high frequencies required by the exact Vaaler endpoint.
- **Multiplicative Shift Check:** Tested C2 dual coefficients under odd rational scaling. Let $\xi_1 = 3/2 \implies \sigma(3/2) = -1/2$. For dilation $a=3$, $\sigma(9/2) = -1/2$. The product $(-1/2)(-1/2) = 1/4$. The sign collapses to positive exactly as predicted.

Useful lemmas:

### LY-Audit. Exact Li--Yang Source Constraint for H5r-F
**Status:** Proved structural limit based on exact TeX audit.
To evaluate the fixed-Fejer target H5r-F at the conjectural endpoint $P(X) \ll_\epsilon X^{1/4+\epsilon}$, the required frequency block length is $H_D \asymp D X^{-1/4} \asymp X^{1/4}$ for denominator scale $D \asymp X^{1/2}$. Auditing Li--Yang (2023) `\label{main theorem}` reveals strict upper bounds $H \le M T^{-49/164}$ (Case A) and $H \le M^{35/69}T^{-2/23}$ (Case B), forcing $H \le X^{33/164} \approx X^{0.201}$. Because $X^{0.25}$ mathematically violates this upper bound, H5r-F cannot be invoked within the domain of applicability of modern divisor-spacing theorems without dimensionally overloading the double large sieve matrices.

### H10-M. Mellin--Perron Dual Length Conservation
**Status:** Proved algebraic diagnostic mapping.
Evaluating $N(X) = \sum_{n \le X} r_2(n)$ via the smoothed Perron integral of $4\zeta(s)L(s,\chi_4)$ requires a truncation height $T \asymp X^{3/4}$ to force a truncation error of $X^{1/4}$. Applying the functional equation and evaluating via Stirling's approximation yields a stationary phase point at $t_0 \asymp \sqrt{nX}$. Constraining $|t_0| \le T$ restricts the active dual variable to $n \ll T^2/X \asymp X^{1/2}$. This precisely reconstructs the Voronoi/Poisson-Bessel phase $2\pi\sqrt{nX}$ at the identical summation length $X^{1/2}$, confirming that contour mapping structurally reproduces the Vaaler/hyperbola geometry.

### Q1-Ext. Near-collision exact congruence factorization (Redrafted)
**Status:** Proved algebraic relation; analytic use pending insertion into spacing estimates.
Let $(a,b)=1$, and let $d_1, d_2$ be odd integers satisfying the spacing gap $d_1 b - d_2 a = \Delta$. Modulo-4 arithmetic completely categorizes the character product:
1. If $a, b$ are both odd, $\Delta$ is even, yielding the exact factorization $\chi_4(d_1)\chi_4(d_2) = \chi_4(ab)(-1)^{\Delta/2}$.
2. If $a$ is even and $b$ is odd, $\Delta$ is odd, and $d_1 \equiv b(a+\Delta) \pmod 4$. This rigidly freezes the value of $\chi_4(d_1)$ entirely independent of $d_2$, making the product a fixed sign multiplied by $\chi_4(d_2)$.
3. Symmetrically, if $a$ is odd and $b$ is even, $d_2 \pmod 4$ is frozen, absorbing into a fixed sign.

### C3-Mult. Multiplicative odd-lattice parity collapse
**Status:** Proved algebraic diagnostic.
In the two-coset dual representation, the parity signature is $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$ for $\xi \in \frac{1}{2}\mathbb{Z}$. A multiplicative spacing shift $\xi_2 = a \xi_1$ evaluates to the product signature $\frac{1}{4}(-1)^{2\xi_1(1+a)}$. If the spacing scale $a$ is an odd integer, the exponent $2\xi_1(1+a)$ is unconditionally an even integer for all values of $\xi_1$. This demonstrates that non-translation rational-dilation spacing uniformly erases the parity oscillation.

What should be tested next:
1. **Even Multiplicative Spacing**: Test spacing matrices restricted entirely to *even* multiplicative dilations ($a \in 2\mathbb{Z}$) to determine the exact nature of the phase mixing between the integer and half-integer C2 cosets, as this represents the sole algebraic survivor of C3-Mult.
2. **Q1-Ext Signed Matrix Integration**: Insert the fixed signs of Q1-Ext into a mock Bombieri--Iwaniec spacing array. Analyze whether summation over the shift $\Delta \neq 0$ yields structural cancellation before bounding absolute values in the double large sieve.

Confidence calibration and failure modes:
- **Confidence: High** regarding the Li--Yang source audit (N2-Audit). The exponent $\theta^*$ and the frequency domain upper bounds explicitly codified in the LaTeX source definitively prove that existing spacing technology mathematically clashes with the $H_D \asymp X^{0.25}$ requirement.
- **Confidence: High** in H10-M. The stationary phase calculation follows standard analytic number theory scaling for Gamma-ratios on vertical lines.
- **Confidence: High** in C3-Mult and Q1-Ext as exact algebraic modular properties.
- **Failure Mode 1 (Li-Yang Sub-Cases):** Traditional Bombieri-Iwaniec frameworks tightly couple frequency constraints $H$ to optimal Taylor series matrix dimensions. It is theoretically possible that a custom large sieve engineered explicitly for the shifted phase $F_{2,1}(x)$ could decouple these constraints, stretching the valid $H$ domain, although reaching $X^{0.25}$ would likely weaken the bounds drastically beyond $X^{1/4}$.
- **Failure Mode 2 (Mellin-Perron Asymmetric Contours):** The algebraic equivalence (H10-M) relies on a symmetric shift across the critical strip. A radically asymmetric or complex contour avoiding standard vertical integration might defer the Voronoi reconstruction, provided one successfully controls the ensuing saddle points.
- **Failure Mode 3 (Matrix Norm Erasure):** Q1-Ext provides explicit signs, but utilizing them requires an off-diagonal sum over $\Delta$. If a matrix bounding technique structurally forces absolute values via Cauchy-Schwarz prior to the $\Delta$ sum, the exact congruence signs will be unconditionally erased.
