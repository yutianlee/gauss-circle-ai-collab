Summary:

This is the Round 6 Stage A output for `gpt_pro_thinking`. The active Round 6 instruction is to continue from the current state, make concrete progress on the prior judge instructions, and explicitly separate proved claims from proof gaps. The current reading packet says Round 5 downgraded the arithmetic route from a promising proof route to a structured reduction plus obstruction map, with H5r now the central bottleneck.

Concrete progress in this response:

1. I formalize C1 as a conditional proposition, not as a theorem or lower bound.
2. I give the exact H5r-to-Li--Yang dictionary for $C_1$ and $C_{2,\rho}$, including residue splitting, phase functions, local ranges, derivative checks, and absolute-value placement.
3. I prove the core algebraic part of C2 by Poisson summation modulo $2$: the parity residual $1_{2\nmid d}$ dualizes to the factor $(-1)^m$, and direct A-process differencing collapses it to a constant.
4. I compare three truncation frameworks: Vaaler with Fejer majorant, signed Fourier truncation, and Mellin--Perron. The conclusion is that Vaaler makes H5r explicit, signed Fourier moves the problem to uncontrolled high-frequency tails, and Mellin--Perron replaces H5r by moment/subconvexity requirements for $\zeta(s)L(s,\chi_4)$.
5. I keep the Poisson--Bessel calibration route as a secondary proof module, not as a main route.

No exponent improvement is proved.

Main claim or direction:

The main arithmetic route should remain in the repository, but only as a precise reduction and obstruction map:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{local dyadic reciprocal sums}.
$$

Here $X=R^2$, and the conjectural target is

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The current decisive obstruction is H5r. The Vaaler residual produces parity-supported and untwisted reciprocal sums. These are structurally in the same broad reciprocal-sum class as the sums in the Gauss/divisor Bombieri--Iwaniec framework, but they no longer carry the signed $\chi_4$ structure. Li--Yang's paper states that their improvement for both Gauss and divisor uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley's second-spacing work; their exponent is $\theta^*=0.314483\ldots$, while this project's target is $\theta=1/4$.

Therefore the next viable work should split into two parallel tracks:

1. Complete the Vaaler route honestly, with H5r treated as a mandatory endpoint-strength target.
2. Develop non-majorizing or sign-preserving alternatives, and determine exactly what replaces H5r.

Detailed reasoning:

## 1. C1 as a conditional proposition

The current Vaaler route uses the proved floor-compatible identity

$$
P(X)
=
-4\sum_{a\le y}\chi_4(a)\psi(X/a)
+
4\sum_{b\le y}
\left[
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
\right]
+
O(1),
$$

where

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

For dyadic $d\asymp D$, the local Vaaler height is

$$
H_D\asymp D X^{-1/4}
$$

for

$$
X^{1/4}\le D\le X^{1/2}.
$$

The Vaaler residual produces the H5r families

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d),
$$

and

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

Here $v_k$ should be a smooth dyadic Fejer/dyadic weight, not arbitrary signs. The residual contribution has the form

$$
\frac{D}{H_D}
+
\frac{1}{H_D}
\sum_{K_0\le H_D}
\left|C_i(K_0,D;X)\right|
$$

up to harmless logarithmic losses.

**C1, precise conditional form.**
Suppose the only available estimates for the H5r families are character-blind reciprocal-sum bounds of exponent $\theta$, namely

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0 X^{\theta+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le K_0\le H_D.
$$

Then the Vaaler route gives at best, from these inputs,

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon},
$$

assuming the main Vaaler families H5a and H5b are no worse.

Proof: the zeroth Fejer mode contributes

$$
\frac{D}{H_D}\asymp X^{1/4}.
$$

The nonzero residual modes contribute

$$
\frac{1}{H_D}
\sum_{K_0\le H_D}
K_0X^{\theta+\epsilon}
\ll_\epsilon
X^{\theta+\epsilon}
$$

after dyadic summation. Therefore if $\theta>1/4$, the residual blocks the endpoint $X^{1/4+\epsilon}$ within this proof skeleton.

This proves only a conditional limitation of the Vaaler proof route. It does not prove that H5r cannot satisfy the endpoint bound, and it does not prove equivalence to the Dirichlet divisor problem.

## 2. H5r-to-Li--Yang dictionary

The local H5r ranges are

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le K_0\le H_D\asymp D X^{-1/4}.
$$

The relevant reciprocal phase template is

$$
\sum_{k\sim K_0}g(k/K_0)
\sum_{m\sim M}G(m/M)
e\left(\frac{kX}{M}F(m/M)+\mu k\right),
$$

with $M\asymp D$ and $F$ smooth on a fixed compact subinterval of $(0,\infty)$.

Li--Yang describe double exponential sums of this general reciprocal type as standard in the circle and divisor problems, using the Bombieri--Iwaniec method and spacing estimates.

### 2.1 Dictionary for $C_1$

Start with

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d).
$$

Split the parity condition as $d=2m+1$. Put $M=D/2$ and $m\asymp M$. Then

$$
\frac{kX}{d}
=
\frac{kX}{D}
F_{2,1}\left(\frac{m}{M}\right),
$$

where, taking $D=2M$ for notation,

$$
F_{2,1}(x)=\frac{D}{2Mx+1}
=
\frac{1}{x+1/D}.
$$

Thus

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_{m\sim M}W(m/M)
e\left(\frac{kX}{D}F_{2,1}(m/M)\right).
$$

Derivative check:

$$
F_{2,1}'(x)=-(x+1/D)^{-2},
$$

$$
F_{2,1}''(x)=2(x+1/D)^{-3},
$$

$$
F_{2,1}'''(x)=-6(x+1/D)^{-4}.
$$

Therefore

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
6(x+1/D)^{-6}
-
12(x+1/D)^{-6}
=
-6(x+1/D)^{-6},
$$

which is uniformly bounded away from zero on fixed dyadic support away from $0$.

So $C_1$ is structurally a Li--Yang/Bombieri--Iwaniec reciprocal sum after parity splitting. The obstruction is not malformed phase geometry. The obstruction is that $C_1$ is character-blind except for parity support.

### 2.2 Dictionary for $C_{2,\rho}$

Start with

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

This already has no denominator congruence condition. It fits the same template with

$$
\frac{kX}{4d}
=
\frac{kX}{D}
F_2(d/D),
$$

where

$$
F_2(x)=\frac{1}{4x}.
$$

The factor $e(k\rho/4)$ is a harmless additive phase in the $k$ variable; it may be absorbed into the outer weight if the theorem allows smooth or bounded-variation oscillatory $k$-weights, or treated as a fixed phase shift.

Derivative check:

$$
F_2'(x)=-\frac{1}{4}x^{-2},
$$

$$
F_2''(x)=\frac{1}{2}x^{-3},
$$

$$
F_2'''(x)=-\frac{3}{2}x^{-4}.
$$

Then

$$
F_2'F_2'''-3(F_2'')^2
=
\frac{3}{8}x^{-6}
-
\frac{3}{4}x^{-6}
=
-\frac{3}{8}x^{-6},
$$

again uniformly nonzero on fixed dyadic support.

Thus both $C_1$ and $C_{2,\rho}$ fit the same broad reciprocal phase class as the main terms. The distinction is arithmetic: H5r lacks the signed $\chi_4$ structure.

### 2.3 Absolute-value placement

The intended H5r formulation should use block-level absolute values:

$$
\frac{1}{H_D}
\sum_{K_0\le H_D}
\left|
C_i(K_0,D;X)
\right|.
$$

It should not use termwise absolute values in $k$:

$$
\frac{1}{H_D}
\sum_{k\le H_D}
\left|
\sum_d c_d w_D(d)e(kX/d)
\right|.
$$

The termwise version discards the two-variable structure and activates the one-dimensional H6 obstruction too early. The blockwise version still asks for endpoint-strength double-sum estimates.

## 3. C2: Poisson calculation for the parity residual

Let

$$
S_{\mathrm{odd}}(k,D)
=
\sum_d 1_{2\nmid d}w(d/D)e(kX/d).
$$

Set

$$
f(u)=w(u/D)e(kX/u).
$$

Using Poisson summation on the residue class $d\equiv 1\pmod 2$ gives

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{n\in\mathbb Z}
e(n/2)
\int_{\mathbb R}
w(u/D)e(kX/u-nu/2)\,du.
$$

Since

$$
e(n/2)=(-1)^n,
$$

the parity condition has become a dual alternating factor.

The phase is

$$
\phi_n(u)=\frac{kX}{u}-\frac{nu}{2}.
$$

A stationary point occurs only for $n<0$. Write $n=-m$ with $m>0$. Then

$$
\phi_{-m}(u)=\frac{kX}{u}+\frac{mu}{2},
$$

and

$$
\phi_{-m}'(u)
=
-\frac{kX}{u^2}+\frac{m}{2}.
$$

Thus

$$
u_0=\sqrt{\frac{2kX}{m}}.
$$

On support $u\asymp D$, the dual length is

$$
m\asymp \frac{kX}{D^2}.
$$

The main stationary phase has leading phase

$$
\phi_{-m}(u_0)
=
\sqrt{2kXm},
$$

up to the fixed eighth-root phase coming from stationary phase. The amplitude scale is

$$
|\phi_{-m}''(u_0)|^{-1/2}
\asymp
\frac{D^{3/2}}{(kX)^{1/2}},
$$

since

$$
\phi_{-m}''(u)=\frac{2kX}{u^3}.
$$

The nonstationary terms $n\ge 0$, and terms with $|n|$ outside the stationary window $m\asymp kX/D^2$, are bounded by repeated integration by parts. The zero-frequency term $n=0$ has phase derivative of size $kX/D^2$ with respect to $u$, and in the local range this produces no special main term after integration by parts; more explicitly, after scaling $u=Dv$, the phase parameter is $kX/D$, which is at least $X^{1/2}$ for $D\le X^{1/2}$ and $k\ge 1$.

So the expected B-process form is

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\asymp kX/D^2}
(-1)^m
A_m(k,D)
e\left(\sqrt{2kXm}+\frac18\right)
+
\text{nonstationary error},
$$

where $A_m(k,D)$ is a smooth stationary-phase amplitude of size roughly

$$
A_m(k,D)\asymp \frac{D^{3/2}}{(kX)^{1/2}}.
$$

This proves the core C2 mechanism modulo standard uniform stationary phase.

Now apply a direct A-process in the dual variable. The alternating factor satisfies

$$
(-1)^m(-1)^{m+q}=(-1)^q,
$$

which is independent of $m$.

Therefore C2 should be recorded as follows.

**C2. Dual parity degeneration for H5r.**
Status: algebraically proved after standard Poisson normalization; analytic use requires uniform stationary phase.

The parity-supported residual $1_{2\nmid d}$ dualizes under Poisson modulo $2$ to an alternating factor $(-1)^m$. Direct Weyl differencing in the dual variable collapses this factor to the constant $(-1)^q$. Hence B-process-first does not create a durable arithmetic character for H5r under a sequential B-process then A-process strategy.

This is not a proof that H5r cannot be bounded. It proves only that one natural attempt to recover character cancellation from the parity residual fails.

## 4. Non-majorizing truncation comparison

The current route uses Vaaler because it gives a pointwise controlled finite Fourier approximation to the floor-compatible sawtooth. Its cost is the positive Fejer majorant, which produces H5r.

The next route comparison should be recorded as H10.

### 4.1 Vaaler with Fejer majorant

Vaaler gives

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
$$

with

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

Error replacing H5r:

There is no replacement. The error is precisely H5r:

$$
C_1(K_0,D;X),
\qquad
C_{2,\rho}(K_0,D;X).
$$

Advantage: pointwise control, correct at discontinuities.

Disadvantage: positive majorant removes signed $\chi_4$ from the first residual and produces divisor-like parity/untwisted sums.

### 4.2 Signed finite Fourier truncation

Use the formal Fourier expansion away from discontinuities:

$$
\psi(t)
=
-\sum_{h\neq 0}\frac{e(ht)}{2\pi i h}.
$$

A signed truncation would write

$$
\psi(t)
=
-\sum_{1\le |h|\le H}\frac{e(ht)}{2\pi i h}
+
\mathcal T_H(t),
$$

where $\mathcal T_H$ is the signed high-frequency tail.

For the first sawtooth leg, the replacement error is no longer parity-supported:

$$
\mathcal E_{\mathrm{sign},1}(D)
=
\sum_{d\asymp D}
\chi_4(d)w_D(d)\mathcal T_H(X/d).
$$

Formally,

$$
\mathcal E_{\mathrm{sign},1}(D)
\sim
-\sum_{|h|>H}
\frac{1}{2\pi i h}
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d).
$$

This preserves the $\chi_4$ sign, which is the main attraction.

But this is not a proof route yet. The tail is not pointwise controlled, convergence at discontinuities is delicate, and high frequencies $|h|>H_D$ are unbounded unless one proves strong estimates over all dyadic $h$ ranges. Thus signed Fourier truncation replaces H5r by high-frequency character-twisted reciprocal sums:

$$
\sum_{H_1>H_D}\frac{1}{H_1}
B_1(H_1,D;X),
$$

plus discontinuity errors. This may be better arithmetically than H5r, but it asks for estimates beyond the local Vaaler range.

### 4.3 Mellin--Perron formula

The Dirichlet series is

$$
\sum_{n\ge 1}\frac{r_2(n)}{n^s}
=
4\zeta(s)L(s,\chi_4).
$$

For $c>1$ and suitable truncation height $T$,

$$
\sum_{n\le X}r_2(n)
=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\text{Perron truncation error}.
$$

Shifting the contour crosses the pole at $s=1$, whose residue gives $\pi X$. The remaining integral is a complex-analytic replacement for the sawtooth/Vaaler error.

The replacement error is not H5r. It is a combination of:

1. vertical-line integrals of $4\zeta(s)L(s,\chi_4)X^s/s$;
2. horizontal integrals from the contour shift;
3. Perron truncation errors near the cutoff;
4. possible smoothing errors if a smoothed Perron kernel is used.

To reach

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

one would need very strong cancellation or moment bounds for $\zeta(s)L(s,\chi_4)$ on shifted contours. A naive absolute-value bound on the critical line gives a factor $X^{1/2}$ and is far too large. Shifting to $\operatorname{Re}s=1/4+\epsilon$ would require control of the product of $L$-functions in a range where functional-equation growth and horizontal integrals are nontrivial. Thus Mellin--Perron avoids the positive Fejer majorant, but it imports a difficult $L$-function moment/subconvexity problem. This is likely comparable in depth to the original circle/divisor endpoint.

Dependencies:

The proved arithmetic reductions depend on:

1. Jacobi's identity

$$
r_2(n)=4\sum_{d\mid n}\chi_4(d).
$$

2. The exact symmetric hyperbola identity H1.

3. The exact periodic partial-sum formula H2.

4. The balanced floor-compatible sawtooth identity H3.

5. The convention

$$
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

The Vaaler route depends on:

1. Vaaler's finite trigonometric approximation with Fejer residual majorant.
2. Smooth dyadic partitioning.
3. Local cutoff

$$
H_D\asymp D X^{-1/4}.
$$

4. Endpoint-strength bounds for H5a, H5b, and H5r.

The H5r-to-Li--Yang comparison depends on:

1. Residue splitting of parity conditions.
2. The phase dictionary

$$
T=X,
\qquad
M\asymp D,
\qquad
F(x)\asymp 1/x.
$$

3. Uniform derivative and nondegeneracy checks for $F$.
4. A theorem permitting smooth or bounded-variation $k$ and $d$ weights, including Fejer/dyadic weights.

The C2 B-process calculation depends on:

1. Poisson summation on residue classes modulo $2$.
2. Uniform stationary phase for

$$
\int w(u/D)e(kX/u-nu/2)\,du.
$$

3. Integration-by-parts estimates for nonstationary frequencies.
4. Careful treatment of transition ranges where the stationary point approaches the support boundary.

The Mellin--Perron route depends on:

1. Perron's formula for $4\zeta(s)L(s,\chi_4)$.
2. Residue computation at $s=1$.
3. Truncation-error bounds.
4. Moment or subconvexity estimates for $\zeta(s)L(s,\chi_4)$ strong enough to beat the known divisor-type barrier.

Potential gaps:

1. **C1 is only conditional.**
   It says what the Vaaler route obtains if H5r is bounded only by character-blind exponent-$\theta$ estimates. It is not a lower bound and not an equivalence to the divisor problem.

2. **H5r weights must match actual theorem hypotheses.**
   Li--Yang-type estimates may have restrictions on smoothness, bounded variation, compact support, or coefficient structure. The Fejer/dyadic weights should be checked against the exact theorem used.

3. **Absolute-value placement is fragile.**
   Blockwise absolute values preserve some two-variable structure. Termwise absolute values in $k$ reduce the problem to one-dimensional estimates and are too crude.

4. **C2 requires a uniform stationary-phase lemma.**
   The algebraic dual factor $(-1)^m$ is clear, but using the dual expansion analytically requires uniform control of stationary, nonstationary, and boundary terms.

5. **Signed Fourier truncation has uncontrolled tails.**
   It preserves $\chi_4$ in the first-leg residual, but it replaces H5r by estimates over high Fourier frequencies $H_1>H_D$. Those estimates may be as hard as, or harder than, H5r.

6. **Mellin--Perron may only relocate the barrier.**
   It avoids the positive Fejer majorant, but it requires strong control of $\zeta(s)L(s,\chi_4)$. Without a precise moment/subconvexity input, it is only a route proposal.

7. **No current endpoint theorem is known in this workflow.**
   The current Li--Yang exponent cited in the research state is $\theta^*=0.314483\ldots$, while the conjectural endpoint is $\theta=1/4$. The arXiv abstract confirms that Li--Yang's improvement uses Bombieri--Iwaniec plus first- and second-spacing inputs, not an endpoint result.

Counterexample or obstruction search:

1. **C1 stress test.**
   Numerically compare the signed residual

$$
S_{\mathrm{true}}(X,D)
=
\sum_{d\asymp D}\chi_4(d)w_D(d)R_{H_D}(X/d)
$$

with the Vaaler majorant

$$
S_{\mathrm{maj}}(X,D)
=
\frac{1}{2H_D+2}
\sum_{d\asymp D}1_{2\nmid d}w_D(d)K_{H_D}(X/d).
$$

If the majorant is routinely much larger, this supports C1 as a practical obstruction, but still not as a theorem.

2. **H5r-to-Li--Yang dictionary check.**
   For $C_1$ and $C_{2,\rho}$, explicitly record $F(x)$, $F'$, $F''$, $F'''$, and $F'F'''-3(F'')^2$. Verify that all weights satisfy the theorem being invoked.

3. **C2 Poisson check.**
   Verify the formula

$$
\sum_d1_{2\nmid d}w(d/D)e(kX/d)
=
\frac12
\sum_n(-1)^n
\int w(u/D)e(kX/u-nu/2)\,du.
$$

Then check the stationary point, dual length, main phase, and nonstationary estimates.

4. **Dual A-process collapse check.**
   After C2, verify

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

This confirms that direct differencing cannot recover nontrivial arithmetic oscillation from the parity residual.

5. **Signed Fourier truncation test.**
   Compare the signed high-frequency tail

$$
\sum_{H_1>H_D}\frac{1}{H_1}B_1(H_1,D;X)
$$

with H5r. This tests whether preserving $\chi_4$ is worth the loss of local frequency truncation.

6. **Mellin--Perron barrier test.**
   Write down a concrete contour shift and compute exactly which bound for

$$
\zeta(s)L(s,\chi_4)
$$

would be needed to obtain $X^{1/4+\epsilon}$. This should be done before treating the complex route as viable.

7. **Boundary block test for C2.**
   In the local range

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le k\le D X^{-1/4},
$$

the dual length is

$$
M_D\asymp \frac{kX}{D^2}.
$$

Test the edge cases:

$$
D\asymp X^{1/2},\ k\asymp 1,
\qquad
D\asymp X^{1/2},\ k\asymp X^{1/4},
\qquad
D\asymp X^{1/4},\ k\asymp 1.
$$

Useful lemmas:

## H1. Exact symmetric hyperbola identity

Status: proved.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$, and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a),
$$

one has

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

## H2. Exact periodic formula for $S(u)$

Status: proved.

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
-
\left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right).
$$

## H3. Balanced sawtooth formula

Status: proved as an $O(1)$ floor-compatible identity.

For $X\ge 1$,

$$
P(X)
=
-4\sum_{a\le y}\chi_4(a)\psi(X/a)
+
4\sum_{b\le y}
\left[
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
\right]
+
O(1).
$$

## H4. Finite Vaaler with Fejer residual

Status: external theorem dependency.

Use

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
$$

with

$$
\alpha_h\ll |h|^{-1},
$$

and

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

The proof draft must keep the Fejer residual, not replace it by a scalar.

## H5a. Spatial-character local dyadic target

Status: sufficient endpoint target; not known.

For

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4},
$$

prove

$$
B_1(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5b. Frequency-character local dyadic target

Status: sufficient endpoint target; not known.

For the same range, prove

$$
B_2(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5r. Fejer-residual local dyadic targets

Status: required endpoint target; not known.

For smooth Fejer/dyadic weights, prove

$$
C_1(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon},
$$

and

$$
C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

## H6. Conditional one-dimensional exponent-pair diagnostic

Status: diagnostic, not theorem.

Under the standard reciprocal-phase convention $T\asymp hX/D$, a method that treats $h$ trivially and applies only a one-dimensional exponent-pair estimate in $d$ must satisfy

$$
3\kappa+2\lambda\le 1
$$

at the endpoint block.

## H7. A-process modulus degeneracy for $\chi_4$

Status: proved.

For every integer $q$,

$$
\chi_4(d)\chi_4(d+q)
=
\begin{cases}
1_{2\nmid d},& q\equiv 0\pmod 4,\\
-1_{2\nmid d},& q\equiv 2\pmod 4,\\
0,& q\equiv 1,3\pmod 4.
\end{cases}
$$

## H8. B-process-first character-dualization

Status: partially derived; not yet a proof input.

For smooth compact support away from zero,

$$
\sum_d\chi_4(d)w(d/D)e(hX/d)
$$

has a Poisson-dual form with dual character $\chi_4(n)$ and dual length

$$
|n|\asymp hX/D^2.
$$

It preserves the character but does not prove cancellation.

## H9. B-process dual Hessian degeneracy

Status: proved diagnostic.

For

$$
\Phi(h,m)=\sqrt{Xhm},
$$

one has

$$
\det\nabla^2\Phi=0.
$$

Generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly to this dual phase.

## C1. Fejer Majorant DDP Trap

Status: conditional diagnostic, not theorem.

If H5r is bounded only by character-blind reciprocal-sum estimates with exponent $\theta$, then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs. This is not a lower bound.

## C2. Dual parity degeneration for H5r

Status: algebraically proved modulo standard Poisson normalization; analytic use requires uniform stationary phase.

Poisson summation modulo $2$ sends $1_{2\nmid d}$ to $(-1)^m$ in the dual variable. A direct A-process then collapses

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

## H10. Non-majorizing truncation comparison

Status: proposed strategic route.

Compare:

1. Vaaler with Fejer majorant, whose error is H5r.
2. Signed Fourier truncation, whose error is a high-frequency signed reciprocal tail.
3. Mellin--Perron, whose error is a contour-integral/moment problem for $4\zeta(s)L(s,\chi_4)$.

## B1. Poisson--Bessel calibration module

Status: secondary proof module.

Retain the smoothed Poisson--Bessel formula and smoothing sandwich to recover the classical sanity bound

$$
E(R)\ll R^{2/3}.
$$

What should be tested next:

For `gpt_pro_thinking`:

1. Turn C1 into a compact lemma-bank entry with the exact proof above.
2. Write the H5r-to-Li--Yang dictionary into the reading packet, including $F_{2,1}$ and $F_2$.
3. State H10 as a three-column comparison: Vaaler, signed Fourier, Mellin--Perron.
4. Insert the C2 Poisson formula as a proposed lemma requiring stationary-phase audit.

For `gemini_deep_think`:

1. Complete C2 with a formal stationary-phase lemma for the parity residual.
2. Develop the Mellin--Perron alternative to theorem-dependency level: Perron formula, contour shift, residues, truncation error, and required $L$-function estimates.
3. Test whether signed Fourier truncation can preserve $\chi_4$ without requiring impossible high-frequency estimates.

For `deepseek_api`:

1. Algebraically verify the C2 Poisson normalization modulo $2$.
2. Check the derivative and nondegeneracy calculations for $F_{2,1}$ and $F_2$.
3. Run small numerical tests comparing $S_{\mathrm{true}}$ and $S_{\mathrm{maj}}$ for H5r.
4. Stress-test the C2 dual length formula $m\asymp kX/D^2$ in the boundary regimes listed above.

Confidence:

High confidence in C1 as a conditional diagnostic.

High confidence that H5r is structurally Li--Yang/Bombieri--Iwaniec-type after residue splitting, but character-blind or parity-supported.

High confidence in the C2 Poisson factor $(-1)^n$ and in the dual A-process collapse $(-1)^m(-1)^{m+q}=(-1)^q$.

Moderate confidence in the C2 stationary-phase asymptotic; constants, support transitions, and error terms still need a formal lemma.

Moderate confidence that signed Fourier truncation is the most direct way to preserve $\chi_4$ in the truncation error, but low confidence that its high-frequency tails are easier than H5r.

Low confidence that Mellin--Perron reaches $X^{1/4+\epsilon}$ without importing estimates as hard as the original problem.

No new exponent has been proved. The Round 6 gain is a sharper diagnostic: H5r is not only necessary, but also precisely mapped to a divisor-like reciprocal-sum family; B-process on the parity residual preserves only an alternating factor that collapses under direct differencing; and non-majorizing alternatives now have explicit replacement error terms to analyze.
