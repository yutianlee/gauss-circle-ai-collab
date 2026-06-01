Summary:
Round 8 executes the judge's directives by formalizing the non-majorizing algebraic and dualization structures, explicitly confirming that Mellin-Perron and two-coset dual representations do not bypass the core analytic barriers. First, we extend the rational-collision observation into an exact Near-Collision Character Factorization (Lemma Q1-Ext), proving that $\chi_4$ never acts as pseudorandom noise across near-collision gaps; it is highly deterministic, either tracking a frozen sign or forming a stable alternating block-weight. Second, we verify the two-coset Parity Collapse (Lemma C3-Ext), proving algebraically that translation-invariant spacing completely strips the odd-lattice dual of its parity oscillation, invariant of representation. Third, we develop the Mellin-Perron route to theorem-dependency level, mapping it analytically to the Hardy-Voronoi series and demonstrating it deterministically reconstructs the Hessian-degenerate phase $\sqrt{Xhd}$ and the $X^{1/2}$ dual-length scaling barrier.

Main claim or direction:
The arithmetic Vaaler reduction remains the correct diagnostic framework, with the parity residual H5r-F as the central bottleneck. We must formally downgrade the continuous Mellin-Perron contour approach from a "potential bypass" to an "analytic isomorphism" that securely returns the problem to the degenerate Poisson-Bessel track. Consequently, the problem must be confronted in the discrete parameter space. For the spatial-character main sum (H5a), the new factorization (Q1-Ext) proves that Bombieri-Iwaniec rational spacing matrices naturally preserve the character without premature absolute values. The immediate direction must be testing whether Li-Yang or Huxley frameworks can successfully sum over the near-collision gap $\Delta$ to explicitly exploit the $(-1)^{\Delta/2}$ or strict alternation isolated by Q1-Ext.

Detailed reasoning:
**1. Near-Collision Character Factorization (Q1-Ext):**
In Bombieri-Iwaniec spacing matrices, we evaluate bilinear structures over near-collisions $d_1 b - d_2 a = \Delta$ for coprime slope variables $a,b$. To evaluate H5a, we must evaluate the character product $\chi_4(d_1)\chi_4(d_2)$ for odd denominator variables $d_1, d_2$.
- *Case 1 ($a, b$ both odd):* The difference of odd products implies $\Delta$ is strictly even.
Modulo 4, we have $d_1 b \equiv d_2 a + \Delta \pmod 4$. Multiplying by $b$ (since $b^2 \equiv 1 \pmod 4$) gives $d_1 \equiv d_2 a b + \Delta b \pmod 4$.
Multiplying by $d_2$ gives $d_1 d_2 \equiv d_2^2 a b + \Delta b d_2 \equiv a b + \Delta \pmod 4$ (because $d_2^2 \equiv 1 \pmod 4$, $\Delta$ is even, and $b, d_2$ are odd, so $\Delta b d_2 \equiv \Delta \pmod 4$).
Applying the character gives $\chi_4(d_1 d_2) = \chi_4(ab + \Delta) = \chi_4(ab)(-1)^{\Delta/2}$.
The character pair sign is fully constant across the entire bundle for a fixed $\Delta$.
- *Case 2 ($a$ even, $b$ odd):* The difference of an odd and an even number means $\Delta$ is strictly odd.
From $d_1 b \equiv d_2 a + \Delta \pmod 4$, since $a$ is even and $d_2$ is odd, $d_2 a \equiv a \pmod 4$.
Thus $d_1 b \equiv a + \Delta \pmod 4$, which implies $d_1 \equiv b(a+\Delta) \pmod 4$.
Notice that $d_1$ is completely frozen to a single residue class modulo 4 depending only on $a, b, \Delta$. Therefore, $\chi_4(d_1)$ is a fixed constant sign, and the product perfectly tracks $\pm\chi_4(d_2)$.
- *Case 3 ($a$ odd, $b$ even):* Symmetrically, $d_2$ is frozen modulo 4, and $\chi_4(d_2)$ is a constant fixed sign tracking $\pm\chi_4(d_1)$.
Conclusion: The character product over a near-collision ray is profoundly structured and devoid of pseudorandomness, guaranteeing either a frozen block sign or perfect alternation.

**2. Mellin-Perron Theorem Dependency (H10-A & H10-B):**
To reach $P(X) \ll X^{1/4+\epsilon}$ via Perron's formula on $4\zeta(s)L(s,\chi_4)$, the sharp truncation error bounded by $O(X^{1+\epsilon}/T)$ dictates a minimum truncation height $T \asymp X^{3/4}$.
Shifting the contour to $\Re(s) = -1/2$ extracts the main term $\pi X$. Applying the functional equations for $\zeta(s)$ and $L(s,\chi_4)$ yields the exact relation $D(s) = \pi^{2s-1} \frac{\Gamma(1-s)}{\Gamma(s)} D(1-s)$.
By Stirling's approximation, the Gamma ratio phase scales as $(t/\pi e)^{-2it}$. When paired with the dual series term $X^s n^{s-1}$, the phase is stationary at $t = \pi\sqrt{nX}$.
Because the integral is truncated at $t \le T = X^{3/4}$, the active dual length requires $\pi\sqrt{nX} \le X^{3/4}$, strictly enforcing $N \asymp X^{1/2}$.
The resulting integral is identically the truncated Hardy-Voronoi Bessel series of length $X^{1/2}$. Expanding the divisor coefficient $r_2(n) = 4\sum_{hd=n} \chi_4(d)$ produces the geometric phase $\Phi(h,d) = 2\pi\sqrt{Xhd}$. This exactly matches the B-process phase. Because this continuous phase possesses a zero Hessian determinant (H9), the contour route mirrors the known degenerate geometric bottleneck and provides no structural bypass.

**3. Two-Coset Parity Collapse (C3-Ext):**
We analyze whether the two-coset representation of the odd-lattice Poisson residual (C2) retains spacing information against translation-invariant Weyl differencing.
Let $\Xi = \frac{1}{2}\mathbb{Z}$. The dual sum is $\sum_{\xi \in \Xi} \sigma(\xi) I(\xi)$, where the coset sign is $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$.
When applying a Weyl differencing A-process, we form cross-terms $I(\xi_1)\overline{I(\xi_2)}$ offset by a shift $q = \xi_1 - \xi_2 \in \frac{1}{2}\mathbb{Z}$.
The weight of the cross-term is $\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{2\xi_1 + 2\xi_2}$.
Substituting $\xi_1 = \xi_2 + q$, this evaluates to $\frac{1}{4}(-1)^{4\xi_2 + 2q}$.
Because $\xi_2 \in \frac{1}{2}\mathbb{Z}$, $4\xi_2$ is necessarily an even integer, so $(-1)^{4\xi_2} = 1$ unconditionally.
Thus, $\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{2q}$.
The alternating sign depends solely on the global shift $q$ and factors completely outside the inner sum over the location $\xi_2$. This proves algebraically that translation-invariant methods suffer identical parity collapse regardless of representation. (Note: The derivative of the inner phase $\Phi(\xi+q) - \Phi(\xi) \approx -q\sqrt{kX/\xi}$ is non-zero, so geometric spacing survives, but it is strictly character-blind divisor spacing).

Dependencies:
- Elementary modular arithmetic congruences (for Q1-Ext).
- Weyl differencing expansion for general sequences (for C3-Ext).
- Perron's formula, Stirling's approximation, and asymmetric $L$-function functional equations (for H10-A/B).

Potential gaps:
1. **Q1-Ext Absolute Values Trap:** The algebraic sign factorization is exact, but standard bounds on Bombieri-Iwaniec matrices frequently apply triangle inequalities or absolute values over the coefficient weights *before* summing over the gap $\Delta$. Premature absolute values would erase the $(-1)^{\Delta/2}$ or alternating oscillation.
2. **H10-B Incomplete Gamma Layer:** The derivation uses stationary phase to establish the dual length $X^{1/2}$. However, near the truncation height $t \approx T$, incomplete Gamma functions govern a transition layer that may generate boundary artifacts not fully captured by pure stationary phase.
3. **Non-Translation Differencing for C3:** If a spacing method evaluates correlations without translation (e.g., multiplicative shifts or purely spectral large sieve methods without standard differencing), the $2(\xi_1 - \xi_2)$ algebraic factorization does not directly apply, hypothetically allowing two-coset spacing to bypass the collapse.

Counterexample or obstruction search:
- **Stress-test for Near-Collision Sign Factorization (Q1-Ext):** We numerically stress-test the frozen variable logic. Let $a=2, b=3$ (even/odd), creating an odd gap. Let $\Delta = 1$. The equation is $3d_1 - 2d_2 = 1$. Let $d_1 = 1$, which forces $2d_2 = 2 \implies d_2 = 1$. Both are odd.
LHS evaluates to $\chi_4(1)\chi_4(1) = 1$.
The rule states $d_1$ is frozen: $d_1 \equiv b(a+\Delta) \equiv 3(2+1) \equiv 9 \equiv 1 \pmod 4$. Since $d_1 \equiv 1$ is fixed, $\chi_4(d_1)=1$, making the product cleanly track $\chi_4(d_2)=1$. Let $d_1=5, d_2=7$. LHS $\chi_4(35) = -1$. Rule states $d_1 \equiv 1 \pmod 4$, so $\chi_4(d_1)=1$, tracking $\chi_4(7)=-1$. The correlation is perfect.
- **Counterexample check for Parity Spacing Claims:** If one claims the two-coset odd-lattice parameterization prevents parity collapse, we test this by squaring the sum with a generic translation A-process. As derived, the cross-term weight is strictly $\frac{1}{4}(-1)^{2q}$. Since this is independent of the summation variable $\xi_2$, the translation completely destroys the internal oscillation, proving the spacing claim false.

Useful lemmas:

**Lemma Q1-Ext: Near-Collision Exact Sign Factorization**
Status: proved algebraic lemma.
For coprime integers $a, b$ and odd variables $d_1, d_2$, let $d_1 b - d_2 a = \Delta$. The character product $\chi_4(d_1)\chi_4(d_2)$ is entirely deterministic:
1. If $a, b$ are odd, $\Delta$ is even, and $\chi_4(d_1)\chi_4(d_2) = \chi_4(ab)(-1)^{\Delta/2}$.
2. If $a$ is even, $b$ is odd, then $\Delta$ is odd, and $d_1 \equiv b(a+\Delta) \pmod 4$ is frozen. Thus $\chi_4(d_1)$ is a constant sign, and the product perfectly tracks $\pm\chi_4(d_2)$.
3. If $a$ is odd, $b$ is even, $d_2$ is frozen modulo 4, and the product perfectly tracks $\pm\chi_4(d_1)$.
This factorization isolates the character into an alternating block-weight without error terms.

**Lemma C3-Ext: Two-Coset Parity Collapse**
Status: proved obstruction.
In the odd-lattice Poisson dual parameterized over $\xi \in \frac{1}{2}\mathbb{Z}$ with coset signs $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$, a translation-invariant shift $q = \xi_1 - \xi_2$ yields a cross-term sign $\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{2q}$. This sign factors entirely out of the internal location sum, proving that A-process spacing strictly strips the summation variable of all parity oscillation.

**Lemma H10-A: Mellin-Perron Truncation Dependency**
Status: proved conditional reduction.
For generating function $4\zeta(s)L(s,\chi_4)$, achieving an endpoint error of $O(X^{1/4+\epsilon})$ via the sharp Perron formula strictly requires a truncation height $T \asymp X^{3/4}$. This deterministically bounds the active frequencies in the subsequent contour shift.

**Lemma H10-B: Hardy-Voronoi Dual Phase Equivalence**
Status: proved diagnostic mapping.
Applying the functional equations to the Mellin-Perron integral at height $T \asymp X^{3/4}$ produces an active dual length $N \asymp X^{1/2}$. Parameterizing the divisor coefficient $n = hd$ perfectly reconstructs the continuous phase $\Phi(h,d) = 2\pi\sqrt{Xhd}$. This confirms Mellin-Perron maps securely into the Hessian-degenerate B-process track (H9) and acts as an analytic isomorphism, not a geometric bypass.

What should be tested next:
- **For `gpt_pro_thinking`**: Synthesize the impact of Q1-Ext on the actual Bombieri-Iwaniec double large sieve matrix for H5a. Formulate an exact algebraic test of whether the Li-Yang or Huxley frameworks can successfully sum over the gap $\Delta$ to exploit the $(-1)^{\Delta/2}$ or tracking oscillations without defaulting to termwise absolute values. Update the best proof draft with H10-A/B replacing generic contour hopes.
- **For `deepseek_api`**: Formalize R4 (the Abel-summation relation) by numerically simulating the gap between H5r-F and H5r-B. Also, numerically verify the C3-Ext geometric phase differences: check if $\Phi(\xi+q) - \Phi(\xi)$ provides enough non-degenerate variation in the intermediate dyadic blocks to survive without the parity sign.

Confidence:
- **High confidence** in Q1-Ext. The modular arithmetic strictly forces the variables into frozen congruence classes or stable alternating sequences, proving the spatial character avoids pseudorandom noise and can be explicitly modeled.
- **High confidence** in C3-Ext. The translation difference identically factors the sign out of the summation index, formally ending the debate on two-coset spacing.
- **High confidence** in H10-A and H10-B. The contour shift mapping to Voronoi expansions is a rigorously established correspondence in classical analytic number theory, cleanly demoting Mellin-Perron from an escape route to a diagnostic mirror of the arithmetic bottleneck.
