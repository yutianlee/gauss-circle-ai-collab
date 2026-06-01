# DeepSeek API Stage A -- Round 9

## 1. Introduction and scope

Round 9 tasks, as assigned by the judge, are:

1. Run numerical tests comparing H5r-F, H5r-B, and H5r-L1 for square, nonsquare, and near-square $X$.
2. Verify the C2 Fourier signs and stationary-phase constants under the convention $e(t)=e^{2\pi i t}$.
3. Investigate the boundary regime $D\asymp X^{1/2}$, $k\asymp 1$, where the dual length is $O(1)$.
4. Audit the exact Li--Yang/Bombieri--Iwaniec theorem and determine whether it applies to $S_{\mathrm{odd}}$ and $S_\rho$ with the weights and absolute values required by H5r.
5. Recheck N1/N2 with all constants and parameter dependencies.

The present report addresses each task in depth, adds a plan for numerical experiments, supplies exact algebraic verifications, conducts a source-audit of Li--Yang's main theorem, identifies parameter mismatches, lists updated lemmas, and calibrates confidence. No improvement of the Gauss-circle exponent is claimed.

**Main claim or direction.**
The balanced arithmetic/Vaaler reduction remains the most precise diagnostic platform. The central residual target H5r-F is unchanged. The new contributions solidify the algebraic and structural foundations (C2, N1, small-$k$ boundary) and expose a crucial mismatch: the raw double sum for the critical dyadic block does **not** satisfy the hypotheses of Li--Yang's main exponential-sum theorem. A full Bombieri--Iwaniec dissection would be required to bring the residual into the theorem's scope, and even then the best published exponent would be $\theta^*=0.31448\ldots$, not the conjectural $\frac14$. The road to $X^{1/4+\epsilon}$ therefore demands either a new analytic insight that bypasses the Fejer-majorant bottleneck, or an improvement of the first- or second-spacing estimates beyond the current Li--Yang level.

---

## 2. Detailed reasoning

### 2.1 Numerical-test plan for H5r-F, H5r-B, H5r-L1

Because no interactive numerical environment is available inside this reasoning step, a precise recipe is supplied. Its execution should happen before the next cross-review.

**Parameters.**
Choose three types of $X$:
- perfect square $X=n^2$,
- integer non-square,
- near-square $X=n^2\pm 0.1$.

For each $X$, pick two dyadic blocks: $D\approx X^{1/2}$ (the critical block) and $D\approx X^{3/8}$ (an intermediate block). Define $H_D=\lfloor D X^{-1/4}\rfloor$. Let $w_D(d)$ be a compactly supported smooth weight, e.g. a non-negative bump supported in $[D,2D]$ with integral $D$.

For each $(X,D)$ compute the three residual families:
- $S_{\mathrm{odd}}(k,D)=\sum_{2\nmid d} w_D(d)\,e(kX/d)$,
- $S_{1}(k,D)=e(k/4)\sum_{d} w_D(d)\,e(kX/(4d))$,
- $S_{3}(k,D)=e(3k/4)\sum_{d} w_D(d)\,e(kX/(4d))$.

Then compute:

$$
R_F(D)=\Bigl|
\frac1{H_D}\sum_{1\le |k|\le H_D}\eta_{k,H_D}S_\star(k,D)
\Bigr|,
$$

$$
R_{L1}(D)=\frac1{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|,
$$

and for each dyadic $K_0$ (say $K_0=2^j\le H_D$) the dyadic-$L^1$ norm

$$
R_{L1}^{\rm dy}(K_0,D)=\sum_{k\sim K_0}|S_\star(k,D)|.
$$

**Diagnostic criteria.**
- If $R_F(D)$ is significantly smaller than $R_{L1}(D)$ (by a factor like $H_D^{-c}$), the fixed Fejer coefficients exploit cancellations invisible to termwise $L^1$. This would keep alive the hope that H5r-F is genuinely easier.
- If $R_F(D)$ and $R_{L1}(D)$ are comparable, the Abel-summation trap (R4) is empirically active, and any proof of H5r-F will likely need H5r-B-strength estimates.
- Comparing $R_{L1}^{\rm dy}(K_0,D)$ with $K_0 X^{1/4}$ tests whether the residual sits near the conjectural scale.

---

### 2.2 Algebraic verification of C2 Poisson transform

Adopt the convention $e(t)=e^{2\pi i t}$ and the Fourier transform
$$
\widehat f(\xi)=\int_{\mathbb R} f(u)\,e(-\xi u)\,du .
$$

Define $f(u)=w_D(u)\,e(kX/u)$. The odd-lattice sum is

$$
S_{\mathrm{odd}}(k,D)=\sum_{\substack{d\\2\nmid d}} f(d)
=\frac12\sum_{d\in\mathbb Z}\bigl(1-(-1)^d\bigr)f(d) .
$$

Since $(-1)^d=e(d/2)$, the second part is $\sum_d f(d)\,e(d/2)$. Poisson summation yields

$$
\sum_{d} f(d)=\sum_{m\in\mathbb Z}\widehat f(m),\qquad
\sum_{d} f(d)e(d/2)=\sum_{m\in\mathbb Z}\widehat f(m-\tfrac12).
$$

Therefore

$$
S_{\mathrm{odd}}(k,D)
=\frac12\sum_{m\in\mathbb Z}\widehat f(m)-\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu). \tag{1}
$$

Now note that for $\xi\in\mathbb Z$, $(-1)^{2\xi}=1$, and for $\xi\in\mathbb Z+1/2$, $(-1)^{2\xi}=-1$. Hence the right-hand side of (1) can be written as

$$
\frac12\sum_{\xi\in\frac12\mathbb Z}(-1)^{2\xi}\widehat f(\xi)
\;=\; \frac12\sum_{n\in\mathbb Z}(-1)^n\,\widehat f(n/2). \tag{2}
$$

Thus both the two-coset and the alternating-series representations are equivalent and correct. No sign errors are present.

**Claim C2-Alg (proved).**
Under the above Fourier convention,
$$
\sum_{\substack{d\\2\nmid d}} w_D(d)\,e(kX/d)
=\frac12\sum_{m\in\mathbb Z}\widehat f(m)-\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

### 2.3 Leading stationary phase (C2-SP)

For $\xi=-m<0$, the integral is

$$
\widehat f(-m)=\int w_D(u)\,e\bigl(kX/u+mu\bigr)\,du.
$$

The phase $\phi(u)=kX/u+mu$ has

$$
\phi'(u)=-\frac{kX}{u^2}+m,\qquad
\phi''(u)=\frac{2kX}{u^3}>0.
$$

The unique stationary point is $u_0=\sqrt{kX/m}$. In the interior regime $m\asymp kX/D^2$, we have $u_0\asymp D$. The second derivative is $\phi''(u_0)=2m/u_0$. Standard stationary phase (e.g. Hormander, Theorem 7.7.5) gives the leading term

$$
\widehat f(-m)=
e\bigl(\phi(u_0)+1/8\bigr)\,
\frac{w_D(u_0)}{\sqrt{\phi''(u_0)}}
\;+\; O\bigl( (kX)^{-1} D^{3/2} \bigr),
$$

with the main amplitude

$$
\frac{1}{\sqrt{\phi''(u_0)}}\asymp
\frac{D^{3/2}}{\sqrt{kX}}.
$$

The error estimate distinguishes two large parameters after scaling $u=Dv$:

$$
\Lambda\asymp\frac{kX}{D},\qquad
M\asymp\frac{kX}{D^2}.
$$

A fully uniform lemma must treat the transition region $M\asymp1$ (where stationary phase fails) and the boundary where $u_0$ approaches the edge of the weight support. This is recorded as a gap in the lemma bank.

**Claim C2-SP (leading term accepted, uniform error deferred).**
For $m>0$ with $m\asymp kX/D^2$,
$$
\widehat f(-m)
\sim
\frac{w_D(\sqrt{kX/m})}{\sqrt{2m/\sqrt{kX/m}}}\;
e\bigl(2\sqrt{kXm}+1/8\bigr),
\qquad
\bigl|\widehat f(-m)\bigr|
\asymp D^{3/2}(kX)^{-1/2}.
$$

---

### 2.4 Boundary regime $D\asymp X^{1/2},\;k\asymp 1$

For very small $k$ (say $|k|\le X^\epsilon$) the dual length $M=kX/D^2\asymp 1$; stationary phase cannot be employed. Instead, bound the primal sum trivially:

$$
|S_{\mathrm{odd}}(k,D)|
\le \sum_{d\sim D}|w_D(d)|
\ll D.
$$

Since $H_D\asymp D X^{-1/4}$, the contribution of a single such $k$ to the Fejer average is

$$
\frac{\eta_{k,H_D}}{H_D}\,|S_{\mathrm{odd}}(k,D)|
\ll \frac{D}{H_D}
\asymp X^{1/4}.
$$

Summing over $O(X^\epsilon)$ frequencies still stays within $X^{1/4+\epsilon}$. The same holds for $S_\rho$. Thus the small-$k$ boundary is harmless and Lemma B-Boundary is confirmed.

**Claim B-Boundary (proved).**
For $D\asymp X^{1/2}$ and $1\le|k|\le X^\epsilon$,
$$
\frac{\eta_{k,H_D}}{H_D}\,|S_\star(k,D)|
\ll X^{1/4+\epsilon}.
$$

---

### 2.5 Li--Yang theorem-level audit

The human directive instructs us to audit the theorem around `\label{main theorem}` in the Li--Yang TeX source (arXiv:2308.14859v2). I extract the crucial points.

#### 2.5.1 Form of the exponential sum

Li--Yang study

$$
S=\sum_{H\le h\le 2H} g\Bigl(\frac{h}{H}\Bigr)
    \sum_{M\le m\le 2M} G\Bigl(\frac{m}{M}\Bigr)
    e\Bigl(\frac{hT}{M}F\Bigl(\frac{m}{M}\Bigr)\Bigr),
\tag{S}
$$

where $F\in C^3([1,2])$, $g,G$ have bounded variation, and the derivatives satisfy

$$
C_r\ge |F^{(r)}(x)|\ge C_r^{-1}\;(r=1,2,3),\qquad
|F^{(1)}(x)F^{(3)}(x)-3F^{(2)}(x)^2|\ge C_4^{-1}. \tag{D}
$$

#### 2.5.2 Our phase functions

- $F(z)=1/z$: clearly satisfies (D) with $F'F'''-3(F'')^2 = -6z^{-6}$.
- $F_{2,1}(z)=\frac1{z+1/D}$: $F'F'''-3(F'')^2 = -6(z+1/D)^{-6}$. Uniformly non-degenerate for $D\ge X^{1/4}$, since $z+1/D\in[1,2+o(1)]$.
- $F_2(z)=\frac1{4z}$: $F'F'''-3(F'')^2 = -\frac38 z^{-6}$, non-vanishing on $[1,2]$.

Thus the phase functions of H5r belong to the same derivative class.

#### 2.5.3 Weight functions

For H5r-F the outer weights are $\eta_{k,H_D}$, positive, monotone, and smooth on $[1,H_D]$, hence of bounded variation. The inner weights are $w_D(d)$ (smooth) multiplied by parity indicators; after residue splitting each piece is a smooth function on a linearly transformed interval, hence BV. Therefore the **weight regularity condition matches** the theorem's hypothesis for H5r-F.

For H5r-B the arbitrary complex coefficients do **not** automatically have bounded variation; a smoothing step would be required. Hence the theorem is not directly applicable to H5r-B without additional justification.

#### 2.5.4 Parameter ranges -- direct application fails

Attempt to apply the theorem to the double sum

$$
\widetilde S = \sum_{1\le |k|\le H_D} \eta_{k,H_D}
               \sum_{d\sim D} (\text{parity factor})\,w_D(d)\,e(kX/d),
$$

with $T=X$, $M=D$, $H=H_D$. Li--Yang requires that the parameters belong to **Case A** or **Case B**.

- **Case A** demands $H\le M T^{-49/164}$.
  With $D\sim X^{1/2}$, $M T^{-49/164}\asymp X^{1/2 - 0.29878}\approx X^{0.20122}$.
  But $H_D\asymp D X^{-1/4}\approx X^{0.25}$, which exceeds the bound. **Case A fails**.

- **Case B** demands
  $H\le\min\{M^{35/69}T^{-2/23},\, B_0 M^{3/2}T^{-1/2}\}$.
  $M^{35/69}T^{-2/23}\asymp X^{35/138-12/138}=X^{1/6}\approx X^{0.1667}$,
  $B_0 M^{3/2}T^{-1/2}\asymp X^{3/4-1/2}=X^{0.25}$.
  The minimum is $\asymp X^{1/6}$, while $H_D\asymp X^{0.25}$. **Case B also fails**.

Therefore the **raw double sum does not satisfy the hypotheses for the critical block**. The theorem cannot be quoted directly on the Vaaler residual.

#### 2.5.5 Required Bombieri--Iwaniec dissection

Li--Yang themselves never apply their main theorem to a raw $(M,H)$; they first cut the $m$-interval into short pieces of length $N$, perform rational approximation, apply Poisson summation, and only then invoke estimates that lead to their main theorem. Consequently, to bring H5r-F under the theorem's umbrella, one must carry out the full Bombieri--Iwaniec reduction on the Vaaler residual. This would introduce auxiliary parameters (dissection length $N$, minor-arc ranges, effective inner lengths $K,L$, etc.) and would transform the problem into exactly the form treated by Li--Yang. The structural compatibility of the initial phase class makes it highly plausible that such a reduction is possible. However:

1. The reduction has not been performed in the repo.
2. Even after a successful reduction, the best published exponent is $\theta^*=0.31448\ldots$, not $\frac14$.
3. The Fejer weights $\eta_{k,H}$ are monotone and non-negative; it is unclear whether they introduce technical obstacles in the double large sieve or first-spacing steps that do not appear with the indicator weights used by Li--Yang.

**Claim LY-Audit (structural compatibility, theorem-level mismatch).**
The phase functions of H5r satisfy the derivative non-degeneracy (D). The Fejer weights $\eta_{k,H_D}$ are BV. Hence the double sums are structurally inside the Li--Yang/Bombieri--Iwaniec class.
**However**, with the natural choices $M=D$, $H=H_D$, the raw sum does **not** satisfy the Case A or Case B conditions required by the theorem. A full dissection must be provided before the theorem can be invoked. Moreover, current Li--Yang technology yields only $\theta^*\approx0.31448$, not the conjectural $1/4$.

---

### 2.6 Derivative non-degeneracy N1/N2 -- recheck

Already confirmed in §2.5.2. Additional explicit constants:

- $F(z)=1/z$: $|F'F'''-3(F'')^2| = 6z^{-6}\ge 6\cdot 2^{-6}=3/32$ on $[1,2]$.
- $F_{2,1}(z)=1/(z+1/D)$: same expression with $z$ replaced by $z+1/D$, uniformly bounded below by a positive constant for $D\ge X^{1/4}$.
- $F_2(z)=1/(4z)$: $|F'F'''-3(F'')^2| = \frac38 z^{-6}\ge \frac38\cdot 2^{-6}=3/512$.

Thus N1 is proved with explicit constants. N2 remains a structural mapping; theorem-level applicability requires further verification (see §2.5).

**Claim N1 (proved with constants).**
For $F_{2,1}$ and $F_2$ as above, $|F'F'''-3(F'')^2|\ge c>0$ uniformly for $D\ge X^{1/4}$, $x\in[1,2]$.

---

### 2.7 Abel-summation identity R4

The identity

$$
\sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr)a_k
= \frac1{H+1}\sum_{j=1}^{H}A(j),\qquad
A(j)=\sum_{k=1}^{j}a_k,
$$

is exact for every sequence $a_k$. Applied to $a_k=S_\star(k,D)$, it shows that any bound on H5r-F obtained via partial-sum estimates is equivalent to an H5r-B-type estimate. This is an algebraic fact, not a conjecture. Its diagnostic force is that a proof of H5r-F must either avoid partial-sum methods or exploit a special structure of the Fejer average that is invisible at the partial-sum level.

**Claim R4 (proved algebraic identity).**
For any complex sequence $a_k$,
$$
\sum_{k=1}^{H}\eta_{k,H}\,a_k = \frac1{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j}a_k,\qquad
\eta_{k,H}=1-\frac{k}{H+1}.
$$

---

### 2.8 Fejer spike analysis

The Fejer kernel

$$
K_H(t)=\sum_{|k|\le H}\Bigl(1-\frac{|k|}{H+1}\Bigr)e(kt)
= \frac1{H+1}\Bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\Bigr)^2
$$

is non-negative and peaks sharply at integers $t$. In the Vaaler residual, the argument $t$ equals either $X/d$, $(X/d+1)/4$, or $(X/d+3)/4$. When $X$ is a perfect square or near a square, many $d\approx X^{1/2}$ can make $X/d$ close to an integer, causing a spike. The residual majorant

$$
|R_{H_D}(t)|\le\frac{1}{2H_D+2}K_{H_D}(t)
$$

then amplifies certain frequencies $k$. A term-by-term bound $|R_{H_D}(t)|\ll 1/H_D$ would be false in the spike regime.

**Failure mode FM1 (Fejer spikes).**
If no special treatment is given to the spike-aligned $X$, the Vaaler residual could be larger than the scalar $D/H_D$ by a power of $X$. The proof draft must ensure that the Fejer-weighted reciprocal sums adequately capture these spikes; the numerical test plan should include explicit spike-rich $X$.

---

### 2.9 Additional algebraic lemmas (Q1-Ext, C3-Ext)

- **Q1-Ext** (near-collision character factorization) is a proved congruence lemma. Its analytic force depends on whether the sign $\chi_4(ab)(-1)^{\Delta/2}$ survives after the first Cauchy--Schwarz or double-large-sieve step inside a Bombieri--Iwaniec matrix. This remains untested.

- **C3-Ext** (two-coset coefficient collapse) is proved for translation-invariant differencing. It shows that the coefficient parity sign factors out of the location variable; hence direct A-process on the one-sequence model yields no oscillation. It does **not** rule out two-coset spacing gains that exploit the phase difference between integer and half-integer dual transforms.

---

### 2.10 Potential gaps

1. **Vaaler residual must be kept** -- any proof discarding H5r is incomplete.
2. **Fejer positivity erases character signs** -- the signed $\chi_4$ information on the main terms is lost in the residual.
3. **Li--Yang parameter mismatch** -- raw double sum does not meet the theorem's hypotheses.
4. **Li--Yang record exponent $\theta^*>1/4$** -- even after a successful reduction, the conjectural bound is not reached.
5. **Abel-summation trap** -- many natural proofs of H5r-F will silently use partial-sum bounds and encounter H5r-B strength.
6. **Spike alignment** -- square and near-square $X$ may cause oversized residuals.
7. **Non-majorizing alternatives undeveloped** -- signed Fourier and Mellin--Perron lack endpoint estimates.
8. **Numerical evidence absent** -- no numerical stress-tests have been run.

---

### 2.11 Failure modes (detailed)

- **FM1 (Fejer spike blow-up).** Square or near-square $X$ align many $d$ with integer arguments of $K_H$, creating spikes that invalidate scalar residual bounds. Mitigation: explicit Fejer-weighted sum must be bounded; not yet done.
- **FM2 (Abel-summation lock).** Because $\eta_{k,H}$ is positive and monotone, any bound that proceeds via partial sums $A(j)=\sum_{1\le k\le j}S_\star(k,D)$ effectively requires $A(j)\ll j X^{1/4+\epsilon}$, i.e. H5r-B. Unless a direct method avoids partial sums, H5r-F is as hard as H5r-B.
- **FM3 (Li--Yang inapplicability without dissection).** If a proof writer simply invokes "Li--Yang" on the raw double sum, the hypothesis check fails for the endpoint block. This is a concrete false-proof trap.
- **FM4 (Li--Yang exponent ceiling).** Even after a perfect reduction, the best exponent obtained is $\theta^*$, not $1/4$. Thus the Vaaler route cannot exceed Li--Yang's current technology without a new first- or second-spacing idea.
- **FM5 (Signed Fourier tail unbounded).** The formal signed tail preserves $\chi_4$, but no endpoint-strength estimate exists. If absolute values are introduced to bound the tail, the route recreates an H5r-like obstacle.

---

### 2.12 Counterexample / obstruction search (stress tests)

1. **Fejer spike stress test.**
   Take $X=n^2$, choose $d$ near $\sqrt X$ such that $X/d$ is exactly integer or very close. Compute $K_{H_D}(X/d)$ for $H_D\sim X^{1/4}$; compare the resulting residual with $X^{1/4}$.

2. **H5r norm comparison (numerical).**
   As described in §2.1; compare $R_F$, $R_{L1}^{\rm dy}$, and $R_{L1}$ for several $X,D$. A large gap between $R_F$ and $R_{L1}$ would challenge the Abel-summation trap; a small gap would confirm it.

3. **Li--Yang hypothesis test for the dissected sum.**
   Formally carry out the Bombieri--Iwaniec dissection on the Vaaler residual: choose a dissection length $N$, define minor arcs, compute the effective $H_{\rm eff},M_{\rm eff}$. Check whether after optimisation the Li--Yang conditions can be satisfied. This is a pen-and-paper obstruction check.

4. **C2 two-coset spacing test.**
   Apply both translation differencing and a non-translation multiplicative shift to the two-coset dual expression. Record whether the phase difference between integer and half-integer transforms survives after the first Cauchy--Schwarz step.

---

### 2.13 Dependencies

- **External theorems:**
  - Vaaler's finite Fourier approximation with Fejer majorant (H4) -- still needs an exact reference and coefficient formula.
  - Li--Yang's main theorem (`\label{main theorem}`) -- hypotheses reviewed; raw application fails; full dissection pending.
  - Standard stationary phase (Hormander, Stein) -- for C2-SP.
  - Elementary Poisson summation modulo 2 -- for C2-Alg.

- **Internal lemmas:** H1--H3 (proved), H7 (proved), H9 (proved), R4 (proved identity), C2-Alg (proved), C2-SP (leading term accepted), B-Boundary (proved), N1 (proved), Q1-Ext (proved), C3-Ext (proved for translation differencing).

---

### 2.14 Useful lemmas drafted in this round

> **Lemma C2-Alg (Odd-lattice Poisson transform -- algebraic)** -- *Status: proved.*
> Under $e(t)=e^{2\pi i t}$ and $\widehat f(\xi)=\int f(u)e(-\xi u)du$,
> $$
> \sum_{\substack{d\\2\nmid d}} w_D(d)e(kX/d)
> =\frac12\sum_{m\in\mathbb Z}\widehat f(m)-\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
> =\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
> $$

> **Lemma C2-SP (Stationary phase for C2, leading order)** -- *Status: leading term accepted; uniform error deferred.*
> For $m>0$ and $\phi(u)=kX/u+mu$, the stationary point is $u_0=\sqrt{kX/m}$, $\phi(u_0)=2\sqrt{kXm}$, $\phi''(u_0)=2m/u_0$. The leading term is
> $$
> \widehat f(-m)= \frac{w_D(u_0)}{\sqrt{2m/u_0}} e(2\sqrt{kXm}+1/8)+O\bigl((kX)^{-1}D^{3/2}\bigr),
> $$
> with $|\widehat f(-m)|\asymp D^{3/2}(kX)^{-1/2}$ when $m\asymp kX/D^2$.

> **Lemma B-Boundary (small-$k$ residual bound)** -- *Status: proved.*
> For $D\asymp X^{1/2}$ and $|k|\le X^\epsilon$,
> $$
> \frac{\eta_{k,H_D}}{H_D}|S_\star(k,D)|\ll X^{1/4+\epsilon}.
> $$

> **Lemma LY-Phase (Derivative non-degeneracy for H5r phases)** -- *Status: proved.*
> The functions $1/z$, $1/(z+1/D)$, and $1/(4z)$ satisfy Li--Yang's condition (D) on $[1,2]$ for $D\ge X^{1/4}$.

> **Lemma LY-Raw-Mismatch (Raw parameter failure)** -- *Status: proved.*
> For $D\sim X^{1/2}$, $H_D\sim D X^{-1/4}$, the double sum with $M=D$, $H=H_D$ does **not** satisfy Case A or Case B of Li--Yang's main theorem. A full Bombieri--Iwaniec dissection is required.

> **Lemma R4 (Abel summation for Fejer weights)** -- *Status: elementary identity.*
> $\sum_{k=1}^{H}(1-\frac{k}{H+1})a_k = \frac1{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j}a_k$.

> **Lemma Q1-Ext (Near-collision character factorisation)** -- *Status: proved congruence lemma.*
> As previously recorded; no analytic use until inserted into a spacing matrix.

> **Lemma C3-Ext (Two-coset coefficient collapse)** -- *Status: proved for translation-invariant differencing.*
> $\sigma(\xi)=\frac12(-1)^{2\xi}$; for $q=\xi_1-\xi_2$, $\sigma(\xi_1)\sigma(\xi_2)=\frac14(-1)^{2q}$, independent of $\xi_1+\xi_2$.

---

## 3. What should be tested next (prioritised list)

1. **Numerical H5r-norm comparison** -- Execute the plan of §2.1 for several $X,D$. Report $R_F$, $R_{L1}$, and dyadic $L^1$ bounds. This is the highest-priority empirical test.
2. **Bombieri--Iwaniec dissection for H5r-F** -- Write a detailed sketch: choose a dissection length $N$ for the $d$-sum, perform rational approximation, Poisson summation, and map the resulting parameters to Li--Yang's $M,H,T$. Determine whether the conditions of the main theorem can be satisfied after optimal choice of $N$, and compute the resulting $q$-dependent bound.
3. **Fejer spike simulation** -- For square $X$, evaluate $K_{H_D}(X/d)$ at $d$ making $X/d$ near an integer; compare the total residual after summation over $d$ with the scalar $D/H_D$.
4. **Signed Fourier tail numerical test** -- For a few $X,D$, compute the high-frequency tail $\mathcal T_1(D)$ and $\mathcal T_2(D)$ after truncating the signed Fourier series of $\psi$ at $H_D$. Measure whether the tail is smaller than the Fejer residual.
5. **Two-coset spacing test** -- Using the explicit C2 dual, apply both translation and multiplicative differencing and record whether the phase difference between the two cosets produces cancellation that survives a Cauchy--Schwarz bound.

---

## 4. Confidence calibration and failure modes

| Claim | Confidence | Remarks |
|-------|------------|---------|
| C2-Alg is exact under stated convention | High | Algebraic consequence of Poisson summation; verified. |
| C2-SP leading stationary phase constants | High | Standard stationary phase; constants checked. |
| Small-$k$ boundary harmless ($\ll X^{1/4}$) | High | Trivial bound; confirmed. |
| Derivative non-degeneracy for H5r phases (N1) | High | Exact differentiation; constants supplied. |
| Li--Yang phase class structurally compatible | High | Derivative checks pass. |
| Raw double sum fails Li--Yang Case A and B for $D\sim X^{1/2}$ | High | Numerical inequality verified. |
| Li--Yang's record exponent is $\theta^*>1/4$; the theorem does **not** prove H5r-F endpoint | High | Direct from Li--Yang paper. |
| A Bombieri--Iwaniec dissection could bring H5r-F into scope, but would give $\theta^*$ | Moderate | Requires constructing the dissection; plausible but not yet written. |
| H5r-F is genuinely weaker than H5r-B (i.e. Fejer averaging helps) | Moderate | Pending numerical test; R4 indicates potential equivalence. |
| Fejer spike risk is controlled by the Fejer-weighted residual sums | Low--Moderate | Needs numerical verification; spikes could exceed scalar bound. |
| Signed Fourier tail can be bounded without absolute values | Low | No known endpoint estimate; tail likely recreates H5r difficulty. |
| Mellin--Perron avoids the same bottleneck | Low | Functional-equation route reproduces Voronoi/Bessel structure; not a proven escape. |
| Current technology can reach $X^{1/4}$ via the Vaaler route | Low | Multiple obstructions (H5r, Abel trap, Li--Yang ceiling) are unresolved. |

**Principal failure modes:**

- **FM1** Fejer spikes for square $X$ cause residual much larger than $X^{1/4}$.
- **FM2** Abel-summation trap: any proof of H5r-F via partial sums reduces to H5r-B, which is equivalent to dyadic $L^1$ and known to be a divisor-type obstacle.
- **FM3** Incorrect invocation of Li--Yang on the raw double sum (hypothesis violation).
- **FM4** Even after a perfect Bombieri--Iwaniec reduction, Li--Yang's technology yields $\theta^*$, not $1/4$; a new first- or second-spacing result is required.
- **FM5** The signed Fourier tail cannot be controlled without absolute values, forcing a return to H5r-like estimates.

**Overall confidence in the route as a reduction framework:** High.
**Confidence that the route leads to a proof of the conjectural bound without a fundamentally new idea:** Low.

---

*End of Stage A report.*
