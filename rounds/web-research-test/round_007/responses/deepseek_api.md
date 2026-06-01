# Summary
This Stage A output independently executes the main Round 7 tasks assigned to `deepseek_api` by the judge:
- algebraic verification of the C2 Poisson normalization modulo 2 and reconciliation of the $(-1)^m$ and two-coset representations;
- explicit computation of the derivative determinants for the shifted phases $F_{2,1}$ and $F_2$;
- a detailed stationary-phase analysis of the C2 dual integrals, including boundary regimes;
- a plan for numerical stress tests of the three H5r norms (H5r-F, H5r-B, H5r-L1) with square, nonsquare, and near-square $X$;
- a precise audit of the Li--Yang/Bombieri--Iwaniec theorem's applicability to the residual sums $S_{\mathrm{odd}}$ and $S_\rho$;
- identification of the fresh **Fejer spike** as a quantitative failure mode that can break the Vaaler route for square $X$.

All algebraic identities and derivative checks are **proved**. The stationary-phase results are **contingent on a rigorous transition analysis** (now explicitly flagged). The numerical plan is **fully specified but not yet executed**. No improvement of the Gauss circle exponent is claimed; the report sharpens the obstruction map and provides the exact lemmas and stress-test protocols needed to either validate or disqualify the Vaaler route.

# Main claim or direction
Continue the balanced arithmetic hyperbola/Vaaler route as a **reduction and diagnostic framework**, not as a near-complete proof. The central analytical obstacle remains H5r (Fejer-residual reciprocal sums). The new findings confirm that:
- the C2 Poisson transform is algebraically unambiguous and admits two equivalent representations;
- the residual sums are structurally inside the Li--Yang reciprocal-sum class, so any future exponential-sum advance will directly improve the Gauss circle bound;
- a *positive non-negativity* of the Fejer majorant can cause catastrophic alignment when $X$ is a perfect square, potentially destroying the conjectural $O_\epsilon(X^{1/4+\epsilon})$ bound **if** no further cancellation is exploited. This is a concrete, testable failure mode.

# Detailed reasoning

## 1. Conventions and notation
Let $e(t)=e^{2\pi i t}$. The floor-compatible sawtooth is $\psi(t)=t-\lfloor t\rfloor-\frac12$; note $\psi(n)=-\frac12$ for $n\in\mathbb Z$. For a dyadic block $d\sim D$ we use a smooth compactly supported weight $w_D$ with $w_D(x)=0$ for $x\notin[c_1 D, c_2 D]$ and $w_D(x)=1$ for $x$ in a subinterval, with all derivatives uniformly bounded. The Fourier transform is $\widehat f(\xi)=\int_{\mathbb R}f(u)e(-\xi u)\,du$, so Poisson summation reads $\sum_{n\in\mathbb Z}f(n)=\sum_{\ell\in\mathbb Z}\widehat f(\ell)$ when both sides are suitably regularized.

The parameter $X=R^2\ge 1$, $y=\lfloor X^{1/2}\rfloor$. The local Vaaler height for a denominator block of size $D$ is
$$
H_D\asymp D X^{-1/4},\qquad X^{1/4}\le D\le X^{1/2}.
$$

## 2. Algebraic verification of C2 (odd-lattice Poisson transform)
### 2.1 Derivation
Write the odd-index filter as
$$
1_{2\nmid d}= \frac{1-(-1)^d}{2}.
$$
For $k\ge 1$,
$$
S_{\mathrm{odd}}(k,D)=\sum_{d}1_{2\nmid d}w_D(d)e(kX/d)
= \frac12\sum_{d}w_D(d)e(kX/d)-\frac12\sum_{d}(-1)^d w_D(d)e(kX/d).
$$
Define the integral
$$
I(\xi)=\int_{\mathbb R}w_D(u)\,e\!\left(\frac{kX}{u}-\xi u\right)du,\qquad \xi\in\mathbb R.
$$

**First term: all integers.** Apply Poisson summation to $f(d)=w_D(d)e(kX/d)$ (after smoothing for absolute convergence):
$$
\sum_{d}w_D(d)e(kX/d)= \sum_{m\in\mathbb Z} I(m).
$$

**Second term: sign-alternating.** $(-1)^d = e^{\pi i d}$, so $(-1)^d e(kX/d) = e(kX/d+\pi i d)$. The Fourier kernel for $e( (kX/d) + \frac12 d)$ shifted by integer frequencies gives
$$
\sum_{d}(-1)^d w_D(d)e(kX/d)= \sum_{m\in\mathbb Z} I(m-\tfrac12).
$$
Equivalently, letting $\mu=m-\frac12$ run over half-integers,
$$
\sum_{d}(-1)^d w_D(d)e(kX/d)= \sum_{\mu\in\mathbb Z+\frac12} I(\mu).
$$

Therefore the **two-coset representation** is
$$
\boxed{ S_{\mathrm{odd}}(k,D)=\frac12\sum_{m\in\mathbb Z}I(m)-\frac12\sum_{\mu\in\mathbb Z+\frac12}I(\mu). } \tag{2.1}
$$

### 2.2 Reconciliation of the $(-1)^m$ form
Consider the singly-indexed sum
$$
\sum_{n\in\mathbb Z}(-1)^n I(n/2).
$$
When $n$ is even, $n=2m$, $(-1)^{2m}=1$, $I(m)$; when $n$ is odd, $n=2m+1$, $(-1)^{2m+1}=-1$, $I(m+\frac12)$. Hence
$$
\sum_{n\in\mathbb Z}(-1)^n I(n/2)=\sum_{m\in\mathbb Z}I(m)-\sum_{m\in\mathbb Z}I(m+\tfrac12).
$$
The second sum is exactly $\sum_{\mu\in\mathbb Z+\frac12}I(\mu)$. Comparing with (2.1) yields the **single-sum representation**
$$
\boxed{ S_{\mathrm{odd}}(k,D)=\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2). } \tag{2.2}
$$
Both representations are algebraically identical and can be freely interchanged. There is no inherent "obstruction'' in either form; differences arise only when applying subsequent analytic operations (e.g., stationary phase) under different conventions.

### 2.3 Lemma C2 (proved)
> **Lemma C2 (Odd-lattice Poisson transform).**
> For a smooth weight $w_D$ supported on $[c_1 D, c_2 D]\subset(0,\infty)$ and any $k\ge 1$,
> $$
> \sum_{\substack{d\sim D\\2\nmid d}} w_D(d)\,e\!\left(\frac{kX}{d}\right)
> =\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
> =\frac12\sum_{m\in\mathbb Z}I(m)-\frac12\sum_{\mu\in\mathbb Z+\frac12}I(\mu),
> $$
> where $I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du$. Both sides converge absolutely after inserting a Gaussian regulator and letting its width tend to zero.
>
> *Proof.* Direct algebraic manipulation and standard Poisson summation. ∎

## 3. Derivative determinant calculations for $F_{2,1}$ and $F_2$
The Li--Yang (Bombieri--Iwaniec) framework requires a phase $F$ satisfying the non-degeneracy condition
$$
F'(x)F'''(x)-3\bigl(F''(x)\bigr)^2\neq 0
$$
on the relevant interval.

### 3.1 Odd-index residual $C_1$
After isolating $d=2n+1$ and scaling $x=n/D$, the phase becomes
$$
e\!\left(\frac{kX}{2n+1}\right)=e\!\left(\frac{kX}{D}\cdot\frac{1}{(2n+1)/D}\right).
$$
Define $F_{2,1}(x)=1/(x+1/D)$ for $x$ in a compact interval of $(0,\infty)$. Then
$$
F_{2,1}'(x)=-\frac{1}{(x+1/D)^2},\quad
F_{2,1}''(x)=\frac{2}{(x+1/D)^3},\quad
F_{2,1}'''(x)=-\frac{6}{(x+1/D)^4}.
$$
Hence
$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
= \frac{6}{(x+1/D)^6}-\frac{12}{(x+1/D)^6}
= -\frac{6}{(x+1/D)^6}\neq 0.
$$

### 3.2 Frequency-shifted residual $C_{2,\rho}$
The sum is $S_\rho(k,D)=e(k\rho/4)\sum_d w_D(d)e(kX/(4d))$ with $\rho\in\{1,3\}$. Scaling $x=d/D$ gives the phase function $F_2(x)=1/(4x)$. Derivatives:
$$
F_2'(x)=-\frac{1}{4x^2},\quad
F_2''(x)=\frac{1}{2x^3},\quad
F_2'''(x)=-\frac{3}{2x^4}.
$$
Thus
$$
F_2'F_2'''-3(F_2'')^2
= \frac{3}{8x^6}-\frac{3}{4x^6}
= -\frac{3}{8x^6}\neq 0.
$$

### 3.3 Lemma N1 (proved)
> **Lemma N1 (Phase non-degeneracy for residual families).**
> The phase functions $F_{2,1}(x)=1/(x+1/D)$ and $F_2(x)=1/(4x)$ satisfy the Li--Yang non-degeneracy condition uniformly on any compact subinterval of $(0,\infty)$. Consequently the residual sums $C_1$ and $C_{2,\rho}$ belong to the same structural class as the standard reciprocal phase $1/x$.

*Proof.* By direct differentiation. ∎

## 4. Stationary-phase analysis of the C2 dual integrals
### 4.1 Correct sign and stationary points
The integral $I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du$ has phase derivative $-kX/u^2-\xi$, which is *negative for all $u$* when $\xi>0$. Therefore **stationary points exist only for $\xi<0$**. Write $\xi=-m$ with $m>0$:
$$
J(m):=I(-m)=\int w_D(u)\,e\!\left(\frac{kX}{u}+m u\right)du.
$$
The stationary phase condition is
$$
-\frac{kX}{u^2}+m=0\;\Longrightarrow\; u_0=\sqrt{\frac{kX}{m}}.
$$
For $u_0$ to lie inside the support of $w_D$ (size $\asymp D$) we need
$$
m\asymp \frac{kX}{D^2}. \tag{4.1}
$$
If $m$ is much smaller or larger, $u_0$ is outside the support or the quadratic approximation fails, and the integral must be estimated by other means.

### 4.2 Asymptotic expansion (formal)
Near $u_0$, expand $f(u)=kX/u+mu$:
$$
f(u_0)=2\sqrt{kX m},\qquad
f''(u_0)=\frac{2kX}{u_0^3}=\frac{2 m^{3/2}}{\sqrt{kX}}.
$$
Applying the standard stationary-phase formula,
$$
J(m)\sim w_D(u_0)\, e^{2\pi i(2\sqrt{kX m}+1/8)} \sqrt{\frac{2\pi}{|f''(u_0)|}} \Bigl(1+O(m^{-1})\Bigr).
$$
The amplitude is $\approx D^{3/2}(kX)^{-1/2}$ up to constants.

### 4.3 Boundary regime $D\asymp X^{1/2},\; k\asymp 1$
Then $m\asymp 1$. The stationary point $u_0\approx\sqrt{kX}$ is comparable to the upper end of the $d$-range ($D\sim X^{1/2}$), so it may lie at or beyond the edge of the effective support. A uniform asymptotic expansion requires a more delicate analysis (Fresnel-type integrals) or a separate treatment (direct A-process). This regime **cannot** be handled by a naive stationary-phase lemma; it is a known fragile point.

### 4.4 Non-stationary bounds
For $m$ outside a constant multiple of the critical range, standard integration by parts gives $|J(m)|\ll_A (|m|+1)^{-A}$ for any $A>0$.

### 4.5 Lemma C2-SP (stationary-phase parameters, provisional)
> **Lemma C2-SP (Dual stationary phase).**
> Let $m>0$ and assume $w_D$ is smooth, compactly supported on $[c_1 D, c_2 D]$, and $D$ is large.
> (i) If $c_1 \frac{kX}{D^2}\le m\le c_2\frac{kX}{D^2}$, then the stationary point $u_0=\sqrt{kX/m}$ lies in the effective support, and
> $$
> |J(m)| \asymp \frac{D^{3/2}}{\sqrt{kX}}.
> $$
> (ii) If $m$ is outside this range by a factor $>c>1$, then $|J(m)|\ll_A (|m|+1)^{-A}$.
> (iii) When $m\asymp 1$ and $D\asymp X^{1/2}$, no uniform asymptotic can be asserted without additional information about the support of $w_D$; the estimate must be obtained by a direct analysis (e.g., A-process or explicit evaluation).
>
> *Proof.* Standard stationary phase and integration by parts; the boundary case requires separate handling. ∎

## 5. Numerical stress-test methodology for the three H5r norms
We propose an explicit computational protocol to measure the size of the residual families. Because the full range $X\to\infty$ is inaccessible, the tests should be performed for moderately large $X$ (e.g., $10^6$--$10^8$) and for several dyadic blocks $D$. The required quantities are:

**Definition of the norms.** For a given residual family $S_\star(k,D)$ (either $S_{\mathrm{odd}}$ or $S_\rho$), set $H_D=\lfloor D X^{-1/4}\rfloor$ and $\eta_{k,H_D}=1-\frac{|k|}{H_D+1}$. Define:
- H5r-F (fixed Fejer):
$$
  \mathcal E_F(D,X)=\frac{1}{H_D}\Bigl|\sum_{1\le |k|\le H_D}\eta_{k,H_D}S_\star(k,D)\Bigr|.
$$
- H5r-B (worst-case bounded coefficients):
$$
  \mathcal E_B(D,X)=\max_{K_0\le H_D}\frac{1}{K_0}\sup_{|v_k|\le 1}\Bigl|\sum_{k\sim K_0}v_k S_\star(k,D)\Bigr|,
$$
  which can be upper-bounded by $\max_{K_0}\frac{1}{K_0}\sum_{k\sim K_0}|S_\star(k,D)|$ (the termwise-$L^1$ per block).
- H5r-L1 (global mean absolute value):
$$
  \mathcal E_{L1}(D,X)=\frac{1}{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

**Test scenarios.** We must examine at least the following cases:
1. **Square $X$:** $X=n^2$. Then many $d$ divide $X$, and $X/d$ is integer, causing the exponential sum to be large. The Fejer kernel $K_H(t)$ attains its maximum $H+1$ at integers, so the residual majorant can spike.
2. **Non-square integer $X$:** e.g., $X=n^2+1$.
3. **Near-square $X$:** $X=n^2+\delta$ with $\delta=\pm1,\pm2,\dots$, to test how quickly the spike subsides.
4. **Large $D$ vs. small $D$.** Evaluate for $D\approx X^{1/2}$, $D\approx X^{1/3}$, $D\approx X^{1/4}$.

**Implementation outline (pseudocode).**
For a chosen $X$, loop over dyadic $D$. For each $D$, construct a smooth weight $w_D$ (e.g., a bump function with support $[D/2,2D]$). Compute $H_D$. For each $k=1,\dots,H_D$, compute $S_\star(k,D)$ exactly by summation over $d$ (trivial summation is feasible for moderate $D$). Then compute the three norms. Compare to the target $C X^{1/4}$ with $C$ a reasonable constant. For square $X$, also record the contribution of the $d$ that divide $X$ separately.

**Heuristic expectations.** For generic $X$, the exponential sums should exhibit square-root cancellation, so $|S_\star(k,D)|\lesssim \sqrt{D}$. Then $\mathcal E_{L1}\lesssim\sqrt{D}\approx X^{1/4}$ in the critical range, meeting the target. However, for square $X$, the terms with $d\mid X$ are purely additive, potentially giving $|S_\star(k,D)|\gg D^\alpha$ with $\alpha>1/2$ when $k$ aligns. This could make $\mathcal E_{L1}\gg X^{1/4}$. The stress test must determine whether the Fejer weights $\eta_{k,H_D}$ and the averaging over $k$ suppress these spikes sufficiently. **If they do not**, the Vaaler route is invalid for square $X$ unless a separate argument is supplied.

## 6. Audit of the Li--Yang/Bombieri--Iwaniec theorem applicability
### 6.1 Statement of the relevant theorem (Li--Yang 2023, simplified)
Li and Yang (arXiv:2308.14859) prove, among other results, that for $T\ge 1$,
$$
\sum_{h\sim H}\sum_{m\sim M} a_h b_m\, e\!\left(\frac{h T}{m}\right)
\ll_\epsilon T^{\theta^*+\epsilon}\bigl(H M\bigr)^{\frac12},
$$
with $\theta^*=0.314483\dots$, under suitable conditions: $|a_h|,|b_m|\le 1$, smooth weights, $H,M$ in certain ranges, and the phase must satisfy the non-degeneracy conditions (which it does). The theorem is stated for dyadic blocks and requires the weights to be smooth and supported away from $0$.

### 6.2 Mapping of our residual sums
**First residual $C_1=S_{\mathrm{odd}}$.** After substituting $d=2n+1$, the sum becomes
$$
\sum_{n\asymp D/2} w_{D,1}(n)\, e\!\left(\frac{kX}{2n+1}\right).
$$
We can absorb the shift into the weight and the phase: set $M=D$, $T=X$, $h=k$, $m=n$, and $F(x)=\frac{1}{x+1/D}$ (or effectively $1/x$ after a small change of variable). The coefficients $v_k$ are bounded by $1$, and the inner weight $w_{D,1}$ is smooth. All derivative non-degeneracy conditions are satisfied by Lemma N1. The absolute value in H5r-B is taken only after dyadic blocking in $k$, which is compatible with standard bilinear applications (Cauchy--Schwarz in $k$ reduces the $|\sum v_k S|$ to an $L^2$ mean over $k$; the resulting triple sum can be handled by spacing inequalities).

**Second residual $C_{2,\rho}=S_\rho$.** Here
$$
S_\rho(k,D)=e(k\rho/4)\sum_{d\sim D} w_D(d)\, e\!\left(\frac{kX}{4d}\right).
$$
After scaling $d=Dx$, the inner sum is of the form
$$
\sum_{x} e\!\left(\frac{k (X/4)}{D x}\right),
$$
so it fits the Li--Yang framework with $T=X/4$, $M=D$, and an extra factor $e(k\rho/4)$ that can be absorbed into the coefficient $v_k$. The phase $F_2(x)=1/(4x)$ is non-degenerate (Lemma N1).

### 6.3 Hypotheses check
The Li--Yang theorem assumes:
- Coefficients $a_h,b_m$ are complex with $|a_h|,|b_m|\le 1$. Our $v_k$ satisfy this.
- The sums are over dyadic intervals with smooth weights. Our $w_D$ can be chosen smooth.
- The double sum is over $h\sim H$, $m\sim M$ with $H,M$ in a permissible range (typically $X^\varepsilon\le H,M\le X^{1-\varepsilon}$). Our ranges: $k\sim K_0\le H_D\asymp D X^{-1/4}\le X^{1/4}$ (for $D\sim X^{1/2}$ this is $X^{1/4}$), and $d\sim D\le X^{1/2}$. These are inside the allowed range for large $X$.
- The theorem delivers a bound of the form $O_\epsilon(T^{\theta+\epsilon}(HM)^{1/2})$. The exponent $\theta^*$ is the best known. The factor $(HM)^{1/2}$ is the trivial $\ell^2$ bound; the improvement is in the power of $T$.

### 6.4 Gap in exponent
For our required H5r target, we need the double sum to be $\ll K_0 X^{1/4+\epsilon}$. Even after applying the Li--Yang bound with $\theta^*\approx0.3145$, the resulting estimate for $P(X)$ would be $\approx X^{0.3145+\epsilon}$, not $X^{1/4}$. Thus the theorem does **not** reach the conjectural endpoint; it only confirms that the residual sums belong to a class where progress is possible. The gap is quantitative, not structural.

> **Lemma N2 (Li--Yang compatibility).**
> The residual sums $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$ can be represented as instances of the bilinear phases treated by Li--Yang (2023) after a smooth dyadic decomposition. All required derivative hypotheses are satisfied (Lemma N1). A direct application of Li--Yang's theorem yields an exponent $\theta^*\approx0.31448$ for $P(X)$, which is above $1/4$.

## 7. Fejer spike: a quantitative failure mode
### 7.1 Mechanism
The Vaaler residual majorant is $|R_H(t)|\le \frac{1}{2H+2}K_H(t)$ with
$$
K_H(t)=\sum_{|k|\le H}\Bigl(1-\frac{|k|}{H+1}\Bigr)e(kt)
      =\frac{1}{H+1}\Bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\Bigr)^2.
$$
This kernel is non-negative and, crucially, **equals $H+1$ when $t\in\mathbb Z$**. For the first leg, the residual feeds on $t=X/d$. If $X$ is a perfect square, many $d\le y$ divide $X$, making $X/d$ an integer. Then $K_{H_D}(X/d)=H_D+1$, and the residual majorant gives a contribution of order $O(H_D)$ rather than the average $O(1/H_D)$.

### 7.2 Impact on the sum over $d$
After expanding the majorant, the Fejer-weighted residual for the first leg becomes (schematically)
$$
\frac{1}{2H_D+2}\sum_{d\le y} \Bigl|\chi_4(d)\Bigr| K_{H_D}(X/d)
$$
(or something similar after accounting for signs). The term-by-term contribution at the divisors $d\mid X$ can be as large as $O(1)$ per divisor (since $K_{H_D}/(2H_D+2)\approx 1/2$ at integer points). There are roughly $X^{o(1)}$ divisors, but they may accumulate to a noticeable effect. More importantly, the **Fourier expansion of the majorant reintroduces the reciprocal sums $S_{\mathrm{odd}}$ etc. with Fejer weights**; but the spike phenomenon means that *even the optimal bound for those residual sums* might be larger at square $X$ because the Fejer weights heavily emphasize frequencies where the primal sum is large.

### 7.3 A concrete worst-case scenario
Suppose $X=Q^2$ is a large square. Take $D=Q$ (the maximum $d$). For every $k$, $kX/d = kQ$ is integer, so $S_{\mathrm{odd}}(k,D) = \sum_{2\nmid d\sim D} w_D(d)$ (all phases aligned). This sum is $\asymp D$ (weighted length). Then $\mathcal E_{L1}\approx D / H_D \approx X^{1/2}/X^{1/4}=X^{1/4}$, which matches the target! Wait, let's check: if all phases are 1, then $S_{\mathrm{odd}}(k,D)\approx D/2$ (tight bound). Then $\mathcal E_{L1}\approx (D/2) H_D/H_D = D/2 \approx X^{1/2}/2$, far exceeding $X^{1/4}$. Actually the residual target H5r-F is an average of $S_{\mathrm{odd}}$ with Fejer weights; if each $S_{\mathrm{odd}}\approx D$, then the average $\approx D$, which is $X^{1/2}$, not $X^{1/4}$. That would be fatal for the Vaaler route. However, the Fejer residual majorant is applied *before* summing over $d$ in the original proof skeleton. The Vaaler step is done inside the sum over $a$ or $b$. That is: we approximate $\psi(X/a)$ by a finite Fourier series plus residual, and then sum over $a$. The residual bound is $|R_H(X/a)|\le \frac{1}{2H+2}K_H(X/a)$. So the total residual contribution from the first leg is
$$
\Bigl|\sum_{a\le y}\chi_4(a)R_{H_D}(X/a)\Bigr|
\le \frac{1}{2H_D+2}\sum_{a\le y} K_{H_D}(X/a).
$$
Because $K_H$ is non-negative, we cannot exploit any further sign cancellation. Therefore the residual contribution from all $a$ that are divisors of $X$ (or near divisors) could be enormous. In the square case $X=Q^2$, we have $a=Q$ itself giving a spike. But there are many other $a$ such that $X/a$ is integer: all divisors. The number of divisors is $\ll X^{o(1)}$, but each such $a$ contributes about $O(1)$ from the majorant. The remaining $a$ produce smaller values. So the total residual could be as large as $\gg \tau(X)\approx X^{o(1)}$, still possibly harmless because $X^{o(1)}\ll X^{1/4}$. However, the spike may be more severe for the *Fourier* expansion of $K_H$: the residual after inserting the Fejer expansion yields sums like $C_1$ where the $k$-weights are not uniform but heavily concentrate near $k=0$ because of the Fejer shape. This requires a detailed quantitative estimate. I will formulate a precise failure scenario:

**Failure mode F1:** If for square $X$ the Fejer-weighted average $\frac{1}{H_D}\sum_{|k|\le H_D}\eta_{k,H_D} S_{\mathrm{odd}}(k,D)$ is not $\ll X^{1/4}$ but rather $\gg X^{1/4+\delta}$ for some $\delta>0$, then the Vaaler route **fails** for those $X$ (and hence cannot prove the uniform bound unless those $X$ are excluded or a separate treatment is found). This is testable by numerical experiments.

## 8. Character-aware vs. character-blind stress test
To assess the value of $\chi_4$, we propose to compare two versions of the main dyadic target H5a:
- Version A: $B_1^{\chi}(H_0,D;X)=\sum_{h\sim H_0}u_h\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d)$.
- Version B: $B_1^{\mathrm{abs}}(H_0,D;X)=\sum_{h\sim H_0}u_h\sum_{d\sim D}w_D(d)e(hX/d)$ (i.e., replacing $\chi_4(d)$ by $1$).

Compute both for moderate $X$ and typical $h$-ranges. The ratio of their magnitudes will indicate whether the character provides any cancellation beyond generic square-root behavior. Since H7 shows A-process eliminates the character, the advantage must be exploited before differencing. This test gives a baseline for how much "free'' saving can be expected from the mere presence of $\chi_4$.

## 9. Additional failure modes
We list five distinct failure modes that could derail the arithmetic/Vaaler route.

1. **Fejer spike for square $X$ (F1).** As described in §7, the non-negative Fejer majorant yields an uncontrollable residual when $X$ is a square, because many $X/d$ values are integers. Without a supplementary cancellation mechanism (e.g., an alternating sign of $\chi_4$ that survives the residual bound), the proof cannot achieve $O(X^{1/4})$ for all $X$.

2. **Insufficient stationary-phase control at boundary (F2).** For $D\asymp X^{1/2}$ and $k\asymp 1$, the dual C2 integral is not amenable to uniform stationary phase. Any proof relying on asymptotic expansions must provide an alternative estimate for this region; otherwise the bound fails.

3. **The H5r residual matches the divisor problem's true size (F3).** The sums $C_1$ and $C_{2,\rho}$ are structurally identical to the sums appearing in the Dirichlet divisor problem after residue splitting. If the divisor problem's error term genuinely requires an exponent $>1/4$ (which is generally believed to be false, but the *known* bounds are larger), then H5r cannot be improved without a breakthrough in the divisor problem itself.

4. **Character-blind methods cannot reach $\theta=1/4$ (F4).** H6 states that a simple one-dimensional exponent-pair approach would need $3\kappa+2\lambda\le 1$. The best known exponent pair gives $>1/4$. If every method that respects the Fejer majorant's loss of sign effectively reduces to a character-blind estimate, then the Vaaler route inherits this barrier.

5. **Mellin--Perron routes are circular (F5).** The Mellin--Perron alternative, while avoiding Fejer positivity, reintroduces exponential sums through the functional equation that are as hard as the original problem. If no new "non-majorizing'' truncation can be found that provides a genuinely better error term, the entire arithmetic route collapses back to the classical Voronoi/Hardy difficulties.

## 10. Useful lemmas
We collect the precise lemma statements that are either proved in this report or upgraded to proved status.

### Lemma C2 (Proved)
> Under the conventions of §1, for any $k\ge 1$,
> $$
> \sum_{\substack{d\sim D\\2\nmid d}} w_D(d)\,e\!\left(\frac{kX}{d}\right)
> =\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
> =\frac12\sum_{m\in\mathbb Z}I(m)-\frac12\sum_{\mu\in\mathbb Z+\frac12}I(\mu),
> $$
> with $I(\xi)=\int_{\mathbb R} w_D(u)e(kX/u-\xi u)\,du$. The identities hold after inserting a Gaussian regulator and letting its width tend to zero.

### Lemma C2-SP (Stationary-phase parameters, conditional)
> For $m>0$, let $J(m)=I(-m)$.
> (i) If $c_1\frac{kX}{D^2}\le m\le c_2\frac{kX}{D^2}$, then $|J(m)|\asymp D^{3/2}(kX)^{-1/2}$.
> (ii) If $m$ is outside this range by a constant factor, $|J(m)|\ll_A(|m|+1)^{-A}$.
> (iii) For $m\asymp 1$ and $D\asymp X^{1/2}$, no uniform asymptotic expansion is valid without further restrictions on the support.
> **Status:** Part (i) and (ii) are standard; (iii) is a warning that the boundary requires separate treatment.

### Lemma N1 (Proved)
> The functions $F_{2,1}(x)=1/(x+1/D)$ and $F_2(x)=1/(4x)$ satisfy $F'F'''-3(F'')^2\neq 0$ on any compact subinterval of $(0,\infty)$.

### Lemma N2 (Li--Yang compatibility, structural)
> The sums $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$ can be written as bilinear sums of the type treated by Li--Yang (2023) after a smooth dyadic decomposition and scaling. All derivative hypotheses are satisfied. A direct application of Li--Yang's theorem to the residual blocks would give $P(X)\ll_\epsilon X^{\theta^*+\epsilon}$ with $\theta^*\approx0.31448$, which does **not** reach $1/4$.

### Lemma H5r-F (Fixed Fejer target, exact)
> For $H_D\asymp D X^{-1/4}$ and $\eta_{k,H_D}=1-\frac{|k|}{H_D+1}$, the exact requirement forced by the Vaaler majorant is
> $$
> \Bigl|\frac{1}{H_D}\sum_{1\le|k|\le H_D} \eta_{k,H_D} S_\star(k,D)\Bigr|
> \ll_\epsilon X^{1/4+\epsilon},
> $$
> where $S_\star$ represents either $S_{\mathrm{odd}}$ or $S_\rho$. The zero-frequency term ($k=0$) already contributes $D/H_D\asymp X^{1/4}$ and need not be inside the sum.

### Lemma H5r-B (Bounded coefficient target, sufficient)
> For all $|v_k|\le 1$ and dyadic $K_0\le H_D$,
> $$
> \Bigl|\sum_{k\sim K_0} v_k S_\star(k,D)\Bigr|
> \ll_\epsilon K_0 X^{1/4+\epsilon}.
> $$
> This implies H5r-F after dyadic decomposition.

### Lemma H5r-L1 (Termwise $L^1$ target, sufficient but crude)
> $$
> \frac{1}{H_D}\sum_{1\le|k|\le H_D} |S_\star(k,D)|
> \ll_\epsilon X^{1/4+\epsilon}.
> $$

### Lemma H7 (Proved, A-process degeneracy)
> For every integer $q$,
> $$
> \chi_4(d)\chi_4(d+q)=
> \begin{cases}
> 1_{2\nmid d},& q\equiv0\pmod4,\\
> -1_{2\nmid d},& q\equiv2\pmod4,\\
> 0,& q\equiv1,3\pmod4.
> \end{cases}
> $$

These lemmas augment the bank; their statuses are as indicated.

## 11. Dependencies
- The entire arithmetic reduction relies on **H1--H3** (proved floor-compatible identities).
- The Vaaler step relies on **H4**, which references an external theorem (Vaaler's approximation with Fejer majorant). The exact statement of that theorem must be verified against a standard reference; here we assume its validity.
- The analytic targets **H5a, H5b, H5r** are currently not known; the present work only formulates them precisely and checks their compatibility with existing technology.
- The Li--Yang theorem (or Bombieri--Iwaniec spacing method) is the most advanced known technique for such sums; our audit depends on its published statement.

## 12. Potential gaps
1. **The Fejer spike for square $X$** is a concrete gap: no proof has been given that the residual remains $O(X^{1/4})$ in that case.
2. **Boundary stationary-phase region** for $D\asymp X^{1/2}$, $k\asymp 1$ is untreated.
3. **The Li--Yang theorem's exact exponent** is insufficient, and no path to improve it has been identified.
4. **Signed Fourier truncation** has not been developed into a viable alternative with better error.
5. **Numerical evidence** for H5r is completely absent; the feasibility of the conjectural bounds is unverified.
6. **The B-process route (H8)** still suffers from Hessian degeneracy (H9) and does not currently offer a new estimate.

## 13. Counterexample or obstruction search
- **Square $X$:** we formally predict that $P(X)$ might exhibit larger than expected error due to Fejer spikes. Computational search for small squares ($X\le 10^4$) can test this.
- **Rational collisions in the primal sum:** when $kX/d$ is near a rational with small denominator, the sum can peak. Our stress tests should scan for such $k,d$ pairs.
- **Parity-only sums:** the odd-lattice sum without $\chi_4$ may behave similarly to the divisor sum; known $\Omega$-results suggest that an exponent $\le 1/4$ is plausible but not proven. Thus H5r may be fundamentally as hard as the divisor problem, which would mean the Vaaler route has not simplified the problem.

## 14. What should be tested next
1. **Numerical H5r norms** for square, nonsquare, and near-square $X$ using the protocol of §5.
2. **Fejer spike scenario** specifically for $X$ a perfect square, with $D$ set to the maximal divisor $D=X^{1/2}$.
3. **Stationary-phase boundary** by direct integration for $D\sim X^{1/2}$, $k=1$, and compare with the asymptotic formula.
4. **Character-aware vs. character-blind** comparison for H5a to quantify the benefit of $\chi_4$.
5. **Exact Li--Yang theorem audit** with full hypotheses written out, verifying that our $v_k$ and $w_D$ satisfy all smoothness and support conditions.

## 15. Confidence calibration and failure modes
**Overall confidence in the arithmetic reduction (H1--H3):** High. The identities are algebraic and have been verified.

**Confidence in the necessity of H5r:** High. The Vaaler residual cannot be simplified to a scalar error.

**Confidence in the algebraic lemmas C2, N1, H7:** High; they are proved by direct calculation.

**Confidence in the stationary-phase analysis (C2-SP):** Moderate for the asymptotic regime, low at the boundary; rigorous transition estimates are missing.

**Confidence that the Li--Yang framework applies structurally:** High; the mapping is explicit. Confidence that it can yield $X^{1/4}$: Very low; it currently gives $>0.314$.

**Confidence that the Fejer spike is a real obstruction:** Moderate-high; it is a clear mechanism by which the Vaaler route could fail for square $X$. Numerical tests will either confirm or refute its severity.

**Confidence that a non-majorizing truncation can circumvent H5r:** Low; currently no alternative has been formulated with a provably better error term.

**Main failure modes (ranked by severity):**
1. Fejer spike for square $X$ (quantifiable, testable).
2. Boundary stationary-phase gap (requires additional analysis).
3. Character-blind residual (H5r) is as hard as the divisor problem and cannot be proved with known technology.
4. Mellin--Perron is circular and offers no advantage.
5. B-process first fails to break the character parity degeneracy.

## 16. Prioritized next-action list
1. **Run numerical stress tests** (§5) for H5r-F, H5r-B, H5r-L1 on squares and near-squares; report the measured exponent.
2. **Formulate a rigorous lemma** for the C2 integral in the boundary regime $m\asymp 1$ (either by a direct A-process or by exact evaluation with Fresnel integrals).
3. **Complete the Li--Yang theorem audit** by extracting the precise hypotheses from the paper and matching our residual sums exactly.
4. **Develop a signed Fourier truncation** with explicit error estimates and compare its residual to the Vaaler residual.
5. **Propose a new mechanism** (if any) that could avoid the Fejer spike, e.g., by exploiting cancellation across different $k$ modes before applying the majorant.
6. **Integrate the Poisson--Bessel calibration module** into the repo as a secondary check, to stabilize notation and provide the classical $R^{2/3}$ baseline.

**No improvement of the Gauss circle exponent is proved.** The present report serves as a precise diagnostic and a foundation for the next round of targeted computational and analytic tests.
