# Best Conditional Proof Draft

## Scope and status

This document consolidates the accepted proof-obligation graph through completed formal Round 8 of `obligation-main`. It is a conditional proof draft, not a proof of the Gauss circle conjecture and not a claim of a new exponent.

The current theorem-level implication is

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

Here H1--H3 are proved internally, H4 is an audited external theorem, R5-Full remains under its separate reconciliation status, and M9 is open. Consequently the desired bound remains open.

Status labels used below:

- **Proved internally:** accepted proof in the repository, with no unresolved external theorem dependency.
- **Conditional:** derived from explicitly named assumptions or source-dependent inputs.
- **External audit required:** the needed theorem form is identified, but its source card is not yet complete and validated.
- **Open:** no proof currently exists in the accepted graph.
- **Proposed:** a precisely formulated possible route, not an established lemma.

## 1. Normalization and theorem target

Let

$$
N(R)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\le R^2\}.
$$

Put

$$
X=R^2,
\qquad
P(X)=N(\sqrt X)-\pi X.
$$

The target is

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

equivalently

$$
N(R)-\pi R^2\ll_\epsilon R^{1/2+\epsilon}.
$$

Let $\chi_4$ be the primitive real character modulo $4$:

$$
\chi_4(n)=
\begin{cases}
0,&2\mid n,\\
1,&n\equiv1\pmod4,\\
-1,&n\equiv3\pmod4.
\end{cases}
$$

The classical identity

$$
r_2(n)=4\sum_{d\mid n}\chi_4(d)
$$

gives

$$
N(\sqrt X)=1+4T(X),
\qquad
T(X)=\sum_{ab\le X}\chi_4(a).
$$

Thus the problem is reduced exactly to estimating $T(X)$.

## 2. Exact balanced arithmetic reduction

### Lemma H1: symmetric hyperbola identity

**Status: proved internally.**

Let

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
S(u)=\sum_{1\le a\le u}\chi_4(a).
$$

Then

$$
T(X)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

**Proof.** Every pair $(a,b)$ with $ab\le X$ has $a\le y$ or $b\le y$. Indeed, if $a,b>y$, then

$$
ab\ge(y+1)^2>X.
$$

The first sum counts the part with $a\le y$, the second counts the part with $b\le y$, and their overlap is the rectangle $a,b\le y$, whose weighted contribution is $yS(y)$. $\square$

### Lemma H2: periodic formula for $S(u)$

**Status: proved internally.**

For real $u\ge0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
-
\left\lfloor\frac{u+1}{4}\right\rfloor.
$$

Define the floor-compatible sawtooth

$$
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12\quad(n\in\mathbb Z).
$$

Then

$$
S(u)
=
\frac12
+\psi_F\left(\frac{u+1}{4}\right)
-\psi_F\left(\frac{u+3}{4}\right).
$$

**Proof.** The first formula counts the two nonzero residue classes of $\chi_4$ in complete blocks modulo $4$. Substituting

$$
\lfloor t\rfloor=t-\psi_F(t)-\frac12
$$

gives the second formula, including at integer endpoints. $\square$

### Lemma H3: balanced sawtooth formula

**Status: proved internally as an $O(1)$ floor-compatible identity.**

For $X\ge1$ and $y=\lfloor X^{1/2}\rfloor$,

$$
\begin{aligned}
P(X)
=&-4\sum_{a\le y}\chi_4(a)\psi_F(X/a)\\
&+4\sum_{b\le y}
\left[
\psi_F\left(\frac{X/b+1}{4}\right)
-
\psi_F\left(\frac{X/b+3}{4}\right)
\right]
+O(1).
\end{aligned}
$$

**Proof.** Insert Lemmas H1 and H2 into $N(\sqrt X)=1+4T(X)$ and use

$$
\left\lfloor\frac Xa\right\rfloor
=
\frac Xa-\psi_F(X/a)-\frac12.
$$

Let $W(X)$ denote the two displayed sawtooth sums. Direct simplification gives the exact residual

$$
P(X)-W(X)
=
1
+4X\left(\sum_{a\le y}\frac{\chi_4(a)}a-\frac\pi4\right)
+2y-2S(y)-4yS(y).
$$

Since $L(1,\chi_4)=\pi/4$, the four residue cases modulo $4$ give

$$
L(1,\chi_4)-\sum_{a\le y}\frac{\chi_4(a)}a
=
\frac{1-2S(y)}{2y}+O(y^{-2}).
$$

Also $X/y=y+O(1)$ and $X/y^2=O(1)$. Substitution into the exact residual cancels the terms of size $y$ and leaves $O(1)$. $\square$

## 3. Dyadic decomposition and short blocks

Choose a bounded smooth dyadic partition $w_D$ on $1\le d\le y$, with $d\asymp D$ on each block. There are $O(\log X)$ blocks.

Blocks with

$$
D<X^{1/4}
$$

are handled before Fourier expansion. Since $|\psi_F|\le1/2$, their total contribution is

$$
O(X^{1/4}).
$$

For the active blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

set

$$
H_D\asymp D X^{-1/4}.
$$

This choice makes the Fejer residual scale

$$
\Delta_D:=\frac{D}{H_D}\asymp X^{1/4}.
$$

## 4. Finite Vaaler approximation

### Audited external theorem H4

**Status: proved external dependency.**

The exact form needed from Vaaler's finite approximation is

$$
\psi_F(t)
=
\sum_{1\le|h|\le H}\alpha_{h,H}e(ht)
+R_H^F(t),
$$

where $e(t)=e^{2\pi i t}$,

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
$$

The residual must satisfy

$$
|R_H^F(t)|
\le
\frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2.
$$

At integers, the finite Fourier polynomial has value $0$, whereas $\psi_F(n)=-1/2$; the majorant covers the jump exactly because

$$
\frac{K_H(0)}{2H+2}=\frac12.
$$

The accepted algebra also records

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
\qquad
\Phi(u)+\Phi(1-u)=1.
$$

The latter identity is important: $\Phi$ is not symmetric about $1/2$.

This normalization is audited in `sources/vaaler_1985.md` against Vaaler's Theorem 6, equations (6.5)--(6.6), equations (7.1)--(7.3), and Theorem 18. Vaaler's midpoint convention is converted to the floor-compatible value at integers by the equality $K_H(0)/(2H+2)=1/2$.

## 5. Fejer residual estimate

### Proposition R5-Full

**Status: proved conditional on H4.**

For every active block $D$ with $H_D\asymp D X^{-1/4}$, the first and shifted Fejer residual blocks are

$$
O_\epsilon(X^{1/4+\epsilon}).
$$

**Proof.** The pointwise Fejer estimate gives

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first sawtooth leg, choose an integer $m$ nearest to $X/d$. Since $d\asymp D$,

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Define

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0,
\end{cases}
\qquad
\Delta=\frac DH\asymp X^{1/4}.
$$

Then

$$
\frac1H K_H(X/d)\ll W_\Delta(X-md).
$$

Grouping by $n=md$ gives multiplicity at most $\tau(n)$. Hence

$$
\begin{aligned}
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
&\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)\\
&\ll_\epsilon
X^\epsilon\sum_{n\in\mathbb Z}W_\Delta(X-n)\\
&\ll_\epsilon X^{1/4+\epsilon}.
\end{aligned}
$$

The last step uses

$$
\sum_{n\in\mathbb Z}W_\Delta(X-n)\ll\Delta+1
$$

and the elementary divisor bound $\tau(n)\ll_\epsilon n^\epsilon$.

For the shifted legs the kernel argument is

$$
\frac{X/d+\rho}{4},
\qquad \rho\in\{1,3\}.
$$

Near-integrality is equivalent to $X\approx d(4m-\rho)$. Grouping by

$$
n=d(4m-\rho)
$$

again has divisor multiplicity at most $\tau(n)$; the congruence condition only removes representations. The same estimate follows. Exact resonances are safe because $W_\Delta(0)=1$. Short blocks were already removed in Section 3. $\square$

## 6. The remaining main sums

Applying H4 blockwise to the two sawtooth legs produces the fixed-coefficient sums

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le|h|\le H_D}
\alpha_{h,H_D}
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d)
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le|h|\le H_D}
\alpha_{h,H_D}C_h
\sum_{d\asymp D}
w_D(d)e(hX/(4d)),
$$

where

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

### Obligation M9

**Status: open.**

Prove, uniformly for every active dyadic block,

$$
\boxed{
\mathcal M_1(D;X),\ \mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
\qquad
X^{1/4}\le D\le X^{1/2}.
}
$$

Both component obligations remain open:

- `M9-M1`: the spatial-character reciprocal sum.
- `M9-M2`: the frequency-character reciprocal sum.

The estimate must use the actual Vaaler coefficients. A theorem for arbitrary bounded coefficients is not being assumed.

## 7. Conditional endpoint theorem

### Theorem

Assume H4 and M9. Then, for every $\epsilon>0$,

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

**Proof.** Lemma H3 expresses $P(X)$ as two balanced sawtooth sums plus $O(1)$. Section 3 bounds all blocks with $D<X^{1/4}$ by $O(X^{1/4})$. On each active block, H4 decomposes each sawtooth into its Vaaler main polynomial and Fejer residual.

Proposition R5-Full bounds every residual block by $O_\epsilon(X^{1/4+\epsilon})$. Assumption M9 gives the same bound for both main blocks. Summing over $O(\log X)$ dyadic blocks and absorbing the logarithm into $X^\epsilon$ yields

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

$\square$

This theorem remains conditional because M9 is open. H4 is now source-validated.

## 8. Accepted analysis of the M2 bottleneck

This section records accepted structure beneath `M9-M2`. None of it proves M9-M2.

### 8.1 Coefficient algebra

Set

$$
S_2(D;X)
=
\sum_{1\le|h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
\mathcal M_2(D;X)=4S_2(D;X),
$$

with

$$
\beta_{h,H}=\alpha_{h,H}C_h.
$$

By the audited H4 normalization,

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))\chi_4(h)}{\pi h}
\mathbf 1_{2\nmid h}.
$$

Because both $h\mapsto h$ and $h\mapsto\chi_4(h)$ are odd on odd integers, $\beta_h$ is real and even. In particular,

$$
|\beta_{h,H}|\ll\frac1{|h|}.
$$

Moreover, Theorem 6 makes $\Phi$ decreasing on $[0,1]$ and $\Phi(1/2)=1/2$, so

$$
|\beta_{1,H}|\ge\frac1{2\pi}
\qquad(H\ge1).
$$

For real $w_D$, the raw two-sided expression may be paired into a positive-frequency real formula. For complex weights the raw two-sided definition is authoritative; shortcuts involving $\operatorname{Re}B_h$ require separate hypotheses.

### 8.2 Fourth-moment expansion

The exact algebraic expansion is

$$
\begin{aligned}
|S_2(D;X)|^4
=
\sum_{\mathbf h,\mathbf d}
&\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
\prod_{j=1}^4w_D(d_j)\\
&\times
e\left(
\frac X4
\left(
\frac{h_1}{d_1}-\frac{h_2}{d_2}
+\frac{h_3}{d_3}-\frac{h_4}{d_4}
\right)
\right).
\end{aligned}
$$

After clearing denominators, the resonance integer is

$$
N
=
h_1d_2d_3d_4
-h_2d_1d_3d_4
+h_3d_1d_2d_4
-h_4d_1d_2d_3.
$$

The coefficient product retains the four frequency-character signs until an absolute-value or Cauchy step removes them.

### 8.3 Exact resonances

**Conditional proposition.** Assuming H4, bounded dyadic weights, and the accepted exact-resonance sublemmas, the total absolute $\beta$-weighted mass of all tuples with $N=0$ is

$$
\ll_\epsilon D^2X^\epsilon
$$

uniformly over the active range.

The accepted proof module proceeds as follows:

1. Reduce each $h_i/d_i$ to a fraction $p_i/q_i$ and organize the equation $N=0$ by reduced-denominator patterns.
2. Bound paired, pair-swapped, semi-diagonal, denominator-paired, and fraction-matching classes using the harmonic convolution estimate
   $$
   \sum_{\substack{1\le|h|\le H\\1\le|h+q|\le H}}
   \frac1{|h||h+q|}
   \ll
   \begin{cases}
   1,&q=0,\\
   \dfrac{\log(2H)}{|q|},&q\ne0.
   \end{cases}
   $$
3. For the unpaired residual class, use participation rigidity and the exact factorization
   $$
   (\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3
   $$
   to reduce representation counts to the divisor bound.
4. Control the remaining residual energy through the accepted URES pair-representation reduction.

This proposition is deliberately scoped to $N=0$. It supplies no estimate for $0<|N|$.

### 8.4 Interval URES infrastructure

**Status: proved internally, but not a full near-collision theorem.**

Let $\mu/Q\ne0$ be reduced. If

$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac\mu Q
\right|\le\eta,
$$

then the exact identity

$$
\begin{aligned}
&(\mu q_1-Qp_1)(\mu q_3-Qp_3)-Q^2p_1p_3\\
&\qquad=
-\mu Qq_1q_3
\left(
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac\mu Q
\right)
\end{aligned}
$$

implies

$$
\left|
(\mu q_1-Qp_1)(\mu q_3-Qp_3)-Q^2p_1p_3
\right|
\le
|\mu|\eta Qq_1q_3.
$$

For fixed nonzero $p_1,p_3$, with

$$
Q\le4D^2,
\quad
|p_i|\le2H_D,
\quad
0\le\eta\le4X^{-1/4},
\quad
q_i\in[1,2D],
$$

and $(p_i,q_i)=1$, the accepted strip count is

$$
\#\left\{(q_1,q_3):
\left|\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac\mu Q\right|\le\eta
\right\}
\ll_\epsilon
X^\epsilon(1+\eta QD^2)+\Delta,
$$

where

$$
\Delta\le4D\mathbf1_{\eta\ge1/(2D)}
$$

is the separated degenerate branch. Applying this to M2 still requires numerator summation, dyadic lifts, parity, $\beta$-weights, tuple classification, and endpoint uniformity.

### 8.5 Validated absolute near-collision obstruction

Let the denominator support lie in a fixed shell $[aD,bD]$, assume $H_D\ge1$, and suppose the actual block weight satisfies

$$
\sum_d|w_D(d)|\ge\lambda D
$$

for a fixed $\lambda>0$. Restricting the fourth-moment tuple to

$$
h_1=h_2=h_3=h_4=1
$$

and applying weighted Cauchy--Schwarz to windows of pair sums $1/d_1+1/d_3$ gives

$$
\Sigma_{\rm abs}(|N|\le M)
\gg \min(D^4,MD).
$$

Assuming the matching exact-resonance closure from Section 8.3, subtraction of the whole $N=0$ mass yields

$$
\boxed{
\Sigma_{\rm abs}(0<|N|\le M)
\ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon.}
$$

For the global fat band $M=D^4/X$,

$$
\Sigma_{\rm abs}(0<|N|\le D^4/X)
\ge cD^5/X-C_\epsilon D^2X^\epsilon.
$$

Consequently, for every fixed $\delta>0$, choosing $0<\epsilon<3\delta$ refutes an upper bound $\Sigma_{\rm abs}\ll_\epsilon D^2X^\epsilon$ when $D\ge X^{1/3+\delta}$. At $D=X^{1/3}$ there is no power contradiction. The earlier $X^{3/8}$ threshold was a nonoptimal bulk-frequency specialization.

The sharp block is the case $w_D\equiv1$. The explicit partition in
Section 8.6D now verifies the sampled $\ell^1$ lower bound for every active
actual block, including the endpoint-truncated block. Thus the W-1
obstruction applies to the chosen actual partition, while retaining its
absolute/unsigned-only scope and its separate exact-$N=0$ hypothesis.

This result applies to absolute or genuinely nonnegative unsigned masses only. It supplies no lower bound for the true signed fourth moment.

### 8.6 Near collisions and signed structure

The open near-collision problem is to control coefficient-weighted tuples with

$$
0<|N|\sim T.
$$

The accepted graph records an H4-dependent obstruction to the former full-range absolute strategy in upper dyadic ranges and therefore prioritizes sign-preserving estimates. The frequency Cauchy step is insufficient because

$$
|C_h|^2=4\mathbf1_{2\nmid h}
$$

retains odd support but erases the sign $\chi_4(h)$.

One signed input is now proved under explicit hypotheses. Define

$$
A_\chi(p/q)
=
\sum_{\substack{gq\in[D,2D)\\1\le|gp|\le H_D}}
\beta_{gp,H_D}w_D(gq),
$$

If $p$ is even, then $A_\chi(p/q)=0$. If $p$ is odd and the sampled odd-lift sequence has uniformly bounded $\chi_4$-twisted discrepancy—in particular, for a fixed scale-normalized BV profile—Abel summation gives

$$
|A_\chi(p/q)|
\ll
\frac1{|p|}\min\left(1,\frac qD\right)
\le \frac{q}{D|p|}.
$$

Boundedness alone, or smoothness without a uniform scaled-variation bound, does not imply this estimate. This is only an individual pair-weight bound.

To state its exact energy capacity, write

$$
S_D(t)=\sum_x A_\chi(x)e(tx/4),
\qquad
R_\chi(r)=\sum_{x+y=r}A_\chi(x)A_\chi(y),
$$

and let $K$ be the Fourier transform of a fixed real nonnegative smooth global weight. Then

$$
\frac1X\int V(t/X)|S_D(t)|^4\,dt
=\sum_{r,s}R_\chi(r)\overline{R_\chi(s)}
K\left(\frac{X(r-s)}4\right).
$$

The exact normalized signed off-diagonal object is

$$
c_\chi^V(D;X)
=D^{-2}\operatorname{Re}
\sum_{r\ne s}R_\chi(r)\overline{R_\chi(s)}
K\left(\frac{X(r-s)}4\right).
$$

B1 and the exact support imply

$$
\|A_\chi\|_1\ll D\log(2H_D),
\qquad
\|A_\chi\|_2^2\ll D.
$$

The pair-representation identity

$$
(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3
$$

and the divisor bound sharpen this to

$$
\sum_r|R_\chi(r)|^2\ll_\varepsilon D^2X^\varepsilon.
$$

Thus the exact pair-sum diagonal is controlled. Rational spacing, however, gives only the global capacity

$$
\frac1X\int V(t/X)|S_D(t)|^4\,dt,
\quad D^2|c_\chi^V(D;X)|
\ll_{\varepsilon,V}
D^2X^\varepsilon\left(1+\frac{D^4}{X}\right).
$$

The remaining factor is genuinely off-diagonal. An even, odd-numerator, exact-support coefficient model satisfying B1 has normalized critical-band mass

$$
\gg \frac{D^3}{X}-O_\varepsilon(X^\varepsilon).
$$

Therefore B1 alone cannot imply a signed fat-band bound by a power for $D\ge X^{1/3+\delta}$. This countermodel is not the actual Vaaler system; it proves that the next argument must use correlations not present in the envelope.

The proposed actual target is

$$
|c_\chi^V(D;X)|\ll_\epsilon X^\epsilon,
$$

with a graded tail or full off-diagonal estimate, at least in the sign-critical upper range. Even this remains a global statement and does not imply pointwise M2 without a separate large-value theorem or direct estimate.

The next analytic interface is the generic single-lift region $D\le q<2D$, where reduction gives exactly

$$
A_\chi(p/q)=\beta_{p,H_D}w_D(q)
$$

for $(p,q)=1$. B1 is sharp there. Any saving must come from the actual numerator character and reciprocal phases across different fractions or pair sums.

The generic pair equation has an exact two-adic sign law. Writing

$$
q_1=da,\qquad q_2=db,\qquad (a,b)=1,
$$

all odd solutions of $p_1q_2+p_2q_1=N$ have the form

$$
p_1=p_1^{(0)}+2ak,\qquad
p_2=p_2^{(0)}-2bk,
$$

and their character product is

$$
\chi_4(p_1)\chi_4(p_2)
=
\chi_4(p_1^{(0)})\chi_4(p_2^{(0)})
(-1)^{k(a+b)}.
$$

Thus unequal denominator $2$-adic valuations give an alternating fiber, while equal valuations give a sign-locked fiber. In particular, all-odd denominator fibers have no automatic numerator-character cancellation.

There is also a genuine but narrow equal-dilation identity. If

$$
b_h=-\frac{\chi_4(|h|)}{\pi|h|}\mathbf1_{2\nmid h},
\qquad b_0=0,
$$

then these are the Fourier coefficients of a $\pm1/2$ square wave, so

$$
\sum_hb_hb_{n-h}=\frac14\mathbf1_{n=0}.
$$

The finite Vaaler coefficients satisfy

$$
\sup_n\left|
\sum_h\beta_{h,H}\beta_{n-h,H}
-\frac14\mathbf1_{n=0}
\right|
\ll H^{-1/2}.
$$

Unequal denominator dilations and coprimality filters prevent a coefficientwise transfer to the generic pair convolution.

### 8.6A Pointwise terminal-frequency estimate

Let $u_L$ be supported on $h\asymp L$ and satisfy

$$
\sup_h|u_L(h)|
+\sum_h|u_L(h+1)-u_L(h)|
\ll L^{-1}.
$$

For $\rho\in\{1,3\}$ and bounded denominator weights,

$$
\boxed{
\left|
\sum_{d\asymp D}w_D(d)
\sum_hu_L(h)
e\left(\frac h4\left(\frac Xd+\rho\right)\right)
\right|
\ll_\varepsilon
X^\varepsilon\left(1+\frac DL\right).}
$$

Indeed, Abel summation bounds the inner geometric sum by

$$
\min\left(1,\frac1{L\|\theta_{d,\rho}\|}\right),
\qquad
\theta_{d,\rho}=\frac14\left(\frac Xd+\rho\right).
$$

For a nearest integer $m$, put $n=d(4m-\rho)$. Then

$$
|X-n|=4d\|\theta_{d,\rho}\|,
$$

and each $n$ has at most $\tau(n)\ll_\varepsilon X^\varepsilon$ participating divisors $d$. Dyadic proximity bins prove the displayed estimate pointwise for real $X$. Endpoint truncation and negative frequencies cause no loss.

The actual Vaaler amplitude has the required BV norm. Hence for the terminal block

$$
L\asymp H_D\asymp DX^{-1/4},
$$

one obtains

$$
\boxed{S_{2,L}(D;X)\ll_\varepsilon X^{1/4+\varepsilon}}
$$

uniformly for every active $D$, including $D=X^{1/2}$. Lower blocks remain open because the bound degrades as $D/L$.

### 8.6B Certified exponent-pair wedge and exact residual corridor

Write

$$
D=X^\delta,\qquad L=X^\ell,\qquad
\frac14\le\delta\le\frac12,\quad
0\le\ell\le\delta-\frac14.
$$

For a normalized-BV denominator profile, the Tao--Trudgian--Yang exponent
pair

$$
(\kappa,\lambda)
=\left(\frac{89}{1282},\frac{997}{1282}\right)
$$

applies to the reciprocal phase after complex conjugation, with

$$
N=D,\qquad T\asymp\frac{hX}{D},\qquad F(u)=-u^{-1},
\qquad F'(u)=u^{-2}.
$$

Thus

$$
\sum_{d\asymp D}w_D(d)e\left(\frac{hX}{4d}\right)
\ll_\varepsilon
X^\varepsilon
\left(\frac{hX}{D^2}\right)^\kappa D^\lambda,
$$

and summing the $1/h$ Vaaler mass over $h\asymp L$ gives

$$
|S_{2,L}(D;X)|
\ll_\varepsilon
X^{[89(1+\ell)+819\delta]/1282+\varepsilon}.
$$

Consequently the conjectural block target is proved in the wedge

$$
\boxed{178\ell+1638\delta\le463.}
$$

This covers the whole frequency section through
$\delta\le1015/3632$ and a nonempty lower slice through
$\delta\le463/1638$. Together with the terminal theorem and the isolated
second-derivative point $(1/2,0)$, the exact unresolved region is

$$
\boxed{
\mathcal U=
\left\{(\delta,\ell):
\frac14\le\delta\le\frac12,\quad
0\le\ell<\delta-\frac14,\quad
178\ell+1638\delta>463
\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.}
$$

The exponent arithmetic is source-certified. Its transfer to every project
block requires the actual dyadic and endpoint profiles to have uniform
discrete BV norm.

The two shifted phases do not cancel each other below the terminal line.
They are exactly an odd-frequency parity projector. Pairing $h$ and $-h$
gives

$$
S_{2,L}
=4\sum_{d\asymp D}w_D(d)\chi_4(r_d)
\sum_{\substack{h>0\\2\nmid h}}
\frac{v_L(h)\Phi(h/(H+1))}{2\pi h}
\sin\left(\frac{\pi h(X-dr_d)}{2d}\right),
$$

where $r_d$ is a nearest odd integer to $X/d$. The kernel vanishes at exact
product resonance, but is of constant size on
$|X-dr_d|\asymp D/L$. A sparse bounded nonnegative denominator weight can
attain $\gg D/L$ with the actual Vaaler amplitudes. Hence no improvement of
the terminal estimate is uniform over arbitrary bounded weights; any
remaining direct theorem must use the prescribed normalized-BV profile.

### 8.6C Smooth Poisson duality

For a fixed $W\in C_c^\infty((a,b))$, Poisson summation and uniform
stationary phase give

$$
\sum_dW(d/D)e\left(\frac{hX}{4d}\right)
=
\frac{e(1/8)(hX)^{1/4}}2
\sum_{k\ge1}
\frac{W(\sqrt{hX/(4kD^2)})}{k^{3/4}}
e(\sqrt{hXk})
+O_W(1).
$$

Put

$$
K=\frac{XL}{D^2},\qquad M=LK=\frac{XL^2}{D^2}.
$$

For the positive-frequency block this yields the exact normalized identity

$$
\mathcal B^+_{L,W}
=-\frac{e(1/8)}{2\pi}
X^{1/4}M^{-3/4}\mathcal T_{L,K}+O_W(1),
$$

where

$$
\mathcal T_{L,K}
=\sum_{h\asymp L}\sum_{k\asymp K}
\chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk})
$$

and $a_{L,K}$ is the actual normalized smooth slanted symbol. Therefore

$$
\mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon
$$

is equivalent-hard to the positive smooth M2 block target. Grouping by
$m=hk$ produces a localized $\chi_4$-divisor coefficient of uncontrolled
variation, so an unweighted one-dimensional derivative estimate does not
apply. The transform is now proved for smooth profiles; the signed dual
estimate in $\mathcal U$ remains open.

### 8.6D Explicit actual dyadic profiles

**Status: proved internally.**

Let $y=\lfloor\sqrt X\rfloor$. There is a fixed nonincreasing smooth step
$\eta$, equal to $1$ on $(-\infty,1]$ and $0$ beyond a fixed number less
than $3/2$, such that

$$
W(t)=\eta(t)-\eta(2t)
$$

is nonnegative, compactly supported in a fixed shell, and equals $1$ on a
fixed subinterval ending at $t=1$. With $D_j=2^{-j}y$, the bands
$W(d/D_j)$, the finite endpoint restriction at $j=0$, and one telescoping
bottom remainder form an exact partition of $1\le d\le y$.

Every active band $D\ge X^{1/4}$ satisfies

$$
\|w_D\|_\infty+\sum_d|w_D(d+1)-w_D(d)|\le4,
\qquad
\sum_d|w_D(d)|\ge D/8,
$$

for all sufficiently large $X$. Moreover

$$
H_D=\lfloor DX^{-1/4}\rfloor,
\qquad
\frac12DX^{-1/4}\le H_D\le DX^{-1/4}.
$$

The inactive remainder is supported on $d\ll X^{1/4}$ and costs
$O(X^{1/4})$ before Fourier expansion. Hence the profile hypotheses for
B1, the weighted W-1 obstruction, the TTY transfer, and the blockwise Fejer
setup are now explicit.

All interior active blocks are full rescalings of the same
$C_c^\infty$ profile. Exactly one top block has continuum profile

$$
W(t)\mathbf1_{t\le1},
$$

which jumps at $t=1$ because $W(1)=1$. Its discrete BV is uniform. The
one-sided endpoint transform in Section 8.6F now supplies the missing
endpoint term; the remaining seam is the transformed signed cone estimate.

Consequently the exponent-pair wedge and the exact residual region in
Section 8.6B are unconditional for this chosen partition. The hard top
block and the estimates inside the residual region remain open.

### 8.6E Smooth balanced small-gcd packet

**Status: exact reduction proved internally; packet estimate open.**

At the balanced smooth endpoint write $R=\sqrt X$ and

$$
\mathcal T_A(R,L)=
\sum_{h,k}\chi_4(h)A(h/L,k/L)e(R\sqrt{hk}),
\qquad 1\le L\le R^{1/2},
$$

for a uniformly smooth fixed-support symbol family. The localized product
multiplicity satisfies

$$
\sum_m r_L(m)^2\ll L^2\log(2L).
$$

Exact square products and products with
$\operatorname{dist}(\sqrt{hk},\mathbb Z)\le R^{-1}$ contribute
$O_\epsilon(L^{1+\epsilon})$ absolutely. The sector
$(h,k)\ge L^{1/2}$ contributes $O(L^{3/2})$ absolutely.

For the remaining sector, use a fixed smooth dyadic partition of
$g=(h,k)$ and write

$$
h=gu,\qquad k=gv,\qquad (u,v)=1,\qquad g\asymp G<L^{1/2}.
$$

Then $\chi_4(h)=\chi_4(g)\chi_4(u)$. Poisson summation in $g$, with
$\widehat F(\xi)=\int F(t)e(-t\xi)\,dt$, gives exactly

$$
\mathcal T_G=\frac{G}{2i}\mathscr P_G,
$$

where $\mathscr P_G$ retains the outer $\chi_4(u)$ and the signed
difference of the $3/4$- and $1/4$-resonance packets. A sharp gcd cutoff is
not interchangeable with this identity unless its boundary terms and
$1/\xi$ Fourier tails are controlled.

The weakest remaining signed small-gcd estimate is

$$
\boxed{
\left|\sum_{G<L^{1/2}}G\mathscr P_G(R,L)\right|
\ll_\epsilon L^{3/2}X^\epsilon.}
$$

This is unproved and is exactly the remaining smooth small-gcd target. The
shellwise estimate $\sum_GG|\mathscr P_G|\ll L^{3/2}X^\epsilon$ is stronger,
not weaker. The hard top denominator block in Section 8.6D is outside this
smooth packet statement.

A related direct no-go is accepted only in scoped form: any fixed one-sign
spatial slice bounded away from the moving endpoint has one-class,
one-sided first-annulus subtotal of average and occasional size $\gg D/L$.
It obstructs absolute or separately localized estimation, but supplies no
lower bound for the whole class sum or the full signed block.

### 8.6F One-sided transform for the top block

**Status: transform proved internally; signed cone estimate open.**

Put

$$
y=\lfloor\sqrt X\rfloor,
\qquad q=X/y^2,
\qquad \nu_h=hX/(4y^2).
$$

For every surviving positive odd $h\le H_y$, one has

$$
\operatorname{dist}(\nu_h,\mathbb Z)\ge1/8
$$

for sufficiently large $X$. The exact minimum differs from $1/4$ by
$O(y^{-1/2})$. The closest stationary point remains
$\gg y^{1/4}$ natural stationary widths from $d=y$, so no endpoint Fresnel
transition occurs.

One-sided Poisson summation for the included integer endpoint gives

$$
\begin{aligned}
\sum_{d\le y}W(d/y)e(hX/(4d))
={}&\frac{e(hX/(4y))}{1-e(hX/(4y^2))}\\
&+\frac{e(1/8)(hX)^{1/4}}2
\sum_{m=\lceil h/4\rceil}^{h}
\frac{W(\sqrt{qh/(4m)})}{m^{3/4}}e(\sqrt{Xhm})
+O_W(\log(2+h)).
\end{aligned}
$$

The first term combines the missing half endpoint weight with the symmetric
principal-value cotangent series of the modewise boundary tails. It is
$O(1)$ on each positive dyadic frequency block and for the actual
two-sided real-even block. The Vaaler-weighted transform errors are
$O_W(\log^2H)$.

After normalization, the exact remaining top-block target is

$$
\boxed{
\mathcal T_L^{\rm end}
=\sum_{\substack{h\asymp L\\h\ \mathrm{odd}}}
\sum_{\lceil h/4\rceil\le m\le h}
\chi_4(h)a^{\rm end}(h,m)e(\sqrt{Xhm})
\ll_\epsilon L^{3/2}X^\epsilon.}
$$

The symbol is smooth in the cone interior and at the upper support edge,
but has a hard affine lower edge where $W(1)=1$. This estimate is not
proved. Endpoint separation closes the transform seam, not the top M2
estimate.

### 8.7 Average-to-pointwise obstruction

For an interval $I$ of length $\delta$, the local fourth-moment kernel satisfies

$$
\frac1{|I|}
\left|
\int_I e\left(\frac{tN}{4Q}\right)dt
\right|
\ll
\min\left(1,\frac{D^4}{\delta|N|}\right),
\qquad Q=d_1d_2d_3d_4\asymp D^4.
$$

On the coherence window

$$
\delta=\frac{X^{1/2}}D,
$$

the local fat band is

$$
|N|\ll D^5X^{-1/2}.
$$

Moreover, every fourth-moment phase frequency

$$
\lambda
=
\frac14\left(
\frac{h_1}{d_1}-\frac{h_2}{d_2}
+\frac{h_3}{d_3}-\frac{h_4}{d_4}
\right)
$$

satisfies

$$
|\lambda|\ll\frac{H_D}{D}\asymp X^{-1/4},
\qquad
\delta|\lambda|\ll\frac{X^{1/4}}D\le1.
$$

Thus the coherence-window multiplier supplies no power saving.

The elementary derivative estimate is

$$
|S_2'(D;t)|\ll H_D\asymp D X^{-1/4}.
$$

If a global fourth moment supplied only

$$
\int_X^{2X}|S_2(D;t)|^4dt
\ll_\epsilon XD^2X^\epsilon,
$$

then a point value $V=|S_2(D;X_0)|$ persists on an interval of length $\gg V/H_D$. Consequently

$$
\frac{V^5}{H_D}\ll_\epsilon XD^2X^\epsilon,
$$

and hence only

$$
V\ll_\epsilon D^{3/5}X^{3/20+\epsilon}.
$$

At $D=X^{1/2}$ this becomes

$$
V\ll X^{9/20+\epsilon},
$$

which is much weaker than $X^{1/4+\epsilon}$. Therefore a global fourth moment, even if established, still needs a stronger large-value theorem or a direct signed pointwise estimate.

## 9. Current route portfolio

The accepted graph keeps the following routes distinct.

### Primary M2 direction

Preserve $\chi_4(h)$ and seek a signed near-collision, signed energy, signed spacing, or direct bilinear estimate that is uniform through $D=X^{1/2}$.

### Structured lower-range direction

Use the interval URES identity and count for restricted denominator or near-collision classes. Character-blind absolute control is power-obstructed for $D\ge X^{1/3+\delta}$, and no theorem currently assembles the lower-range local counts into M9-M2.

### Backup transform direction

The smooth Poisson/B-process transformation in $d$ is now proved with its
leading constant, zero and nonstationary modes, smooth support crossings,
and uniform $O(1)$ block error. Its actual-symbol $M^{3/4}$ dual target is
equivalent to the original smooth positive block. The remaining task is the
signed product-phase estimate, not completion of the transform.

### M1 direction

The hard top M1 denominator block now has an exact one-sided transform. With

$$
B_h=\sum_{d\le y}\chi_4(d)W(d/y)e(hX/d),
$$

one has

$$
\begin{aligned}
B_h={}&E_h^\chi(X)\\
&+\frac{e(1/8)(hX)^{1/4}}{i}
\sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
\frac{\chi_4(n)W(\sqrt{4qh/n})}{n^{3/4}}
e(\sqrt{Xhn})+O_W(\log(2+h)),
\end{aligned}
$$

where

$$
E_h^\chi(X)=\frac1{2i}
\left\{
\frac{e(hX/y+y/4)}{1-e(hq-1/4)}-
\frac{e(hX/y+3y/4)}{1-e(hq-3/4)}
\right\}.
$$

The endpoint denominators are uniformly separated. After the actual
two-sided Vaaler weights, the boundary is $O(1)$ and the transform errors are
$O_W(\log^2H)$. The remaining normalized M1 cone target is

$$
\sum_{h\asymp L}\sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
\chi_4(n)a_{M1}(h,n)e(\sqrt{Xhn})
\ll_\varepsilon L^{3/2}X^\varepsilon.
$$

After swapping variables, this cone is adjacent to the top M2 cone for
outer $r\le H$. Their exact leading constants have the same sign, however,
and the actual Vaaler factors lie on different coordinates. Moreover, M1 has
an unmatched $H<r<16H$ wing. Thus the cones reinforce rather than cancel,
and no symmetric-divisor involution closes either block.

M9-M1 remains open over the full active dyadic range. Its next route is a
direct frequency phase diagram using bounded partial sums of $\chi_4(d)$
before applying Poisson; success on M2 alone cannot prove M9.

The direct M1 phase diagram is now established. If

$$
B_1(D,L;X)=
\sum_{h\asymp L}\frac{\Phi(h/(H_D+1))}{h}
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
$$

then frequency-first Abel summation followed by nearest-product divisor
grouping proves

$$
\boxed{B_1(D,L;X)\ll_\varepsilon
X^\varepsilon\left(1+\frac DL\right).}
$$

Thus the entire terminal line $L\asymp H_D\asymp DX^{-1/4}$ is
$O_\varepsilon(X^{1/4+\varepsilon})$, including the hard top endpoint.
Resolving $\chi_4(d)$ into the two odd residue classes and applying the
audited Tao--Trudgian--Yang exponent pair also proves the wedge

$$
178\ell+1638\delta\le463,
\qquad D=X^\delta,quad L=X^\ell.
$$

Together with the isolated second-derivative point $(1/2,0)$, the exact
remaining set relative to these direct estimates is

$$
\mathcal U_1=
\left\{(\delta,\ell):0\le\ell<\delta-\frac14,
178\ell+1638\delta>463\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.
$$

Naive Abel summation against bounded partial sums of $\chi_4$ costs total
phase variation $hX/D$, not the one-step derivative $hX/D^2$, and supplies
no additional active target region. M9-M1 therefore remains open precisely
on the nonempty corridor $\mathcal U_1$ relative to the accepted direct
menu.

The residual block now has an exact nearest-product form. Define

$$
\mathcal V_{L,H}(z)=\frac4\pi
\sum_{h>0}v_L(h)\frac{\Phi(h/(H+1))}{h}\sin(2\pi hz),
$$

and set $m_X(d)=\lfloor X/d+1/2\rfloor$, $n_X(d)=dm_X(d)$. Then the
two-sided M1 block is exactly

$$
\mathcal M_{1,L}(D;X)
=\sum_n\sum_{d:n_X(d)=n}
\chi_4(d)w_D(d)
\mathcal V_{L,H}\left(\frac{X-n}{d}\right).
$$

The conditions $n_X(d)=n$ are equivalently

$$
d\mid n,\qquad -d/2\le X-n<d/2,
$$

with the fixed nearest-integer tie convention. Because the paired kernel is
odd,

$$
\mathcal V_{L,H}(0)=0,
$$

so exact products are not the obstruction.

The target on $\mathcal U_1$ requires cancellation between distinct nearby
products. Three simpler replacements are now rigorously excluded:

- freezing the kernel to an $n$-only coefficient on a whole dyadic
  denominator shell has order-one error per representation at
  $|X-n|\asymp D/L$;
- one divisor fiber can be singleton or sign-locked under $\chi_4$, so no
  uniform fiberwise character saving exists;
- prime-product families give grouped $\ell^1$ mass and squared $\ell^2$
  mass $\gg(D/L)/(\log X)^2$ at suitable centers, so coefficient-norm or
  post-grouping triangle arguments miss the target by a power at fixed
  interior points.

These controls do not obstruct the total signed M1 sum. At exact-square
endpoints there are explicit ordered-denominator families on which
$\chi_4$ cancels across different products. The first open lemma is therefore
a cross-product odd-kernel discrepancy estimate with the actual profile and
the full divisor-dependent argument retained.

Round 12 tested the most direct cross-product idea and resolved its algebra.
For a nearest half-lattice center $c\in\frac12\mathbb Z$, replacing $X$ by
$c$ in the phase costs only

$$
O_w(L+X^\epsilon),
$$

including the hard top block. The exact lower and upper product fibers at
offset $u>0$ are

$$
\mathcal F_-(u)=\{d:d\mid c-u,\ d>2u\},\qquad
\mathcal F_+(u)=\{d:d\mid c+u,\ d>2u\},
$$

with the actual support and profile understood. They are disjoint: a common
denominator would divide $2u$ while also exceeding $2u$. More importantly,
divisibility reverses the kernel sign on the upper fiber, so its outer
oddness minus sign reverses again. The paired expression therefore
reconstructs the centered M1 sum instead of cancelling it.

Thus naive opposite-offset reflection, same-denominator matching, rank
pairing, and separate fiber norms are rejected. The precise surviving
annular interface is a signed paired shifted-divisor correlation (PSC) with
the absolute value outside both disjoint fibers and with the full
divisor-dependent symbol retained. On the critical annulus it still needs
the factor $H/L$ beyond the divisor bound. No point of $\mathcal U_1$ is
closed by this reindexing. The next active mechanism is ordered-denominator
cancellation, motivated by the exact-square control rather than by product
reflection.

Round 13 derives the ordered-denominator mechanism exactly. For odd $d$,

$$
\chi_4(d)=-i e(d/4),\qquad
g_h(d+2)-g_h(d)=\frac12-\frac{2hX}{d(d+2)}.
$$

The bad cells are the half-integral resonances of the second term. Exact
cell counting and nonresonant summation give

$$
B_{1,L}(D;X)\ll_\varepsilon X^\varepsilon
\min\left(D,\sqrt{LX/D}\right),
$$

which reaches the target only at the accepted point $(1/2,0)$ and the lower
active edge. The cells are exactly the odd-frequency modes of the M1
$B$-process transform. The remaining signed dual sum is

$$
\sum_{h\asymp L}u_{L,H}(h)(hX)^{1/4}
\sum_q^*\chi_4(q)q^{-3/4}w_D(2\sqrt{hX/q})e(\sqrt{Xhq}),
$$

with odd $q$ and the actual support conditions. Its phase has rank-one
Hessian and is constant on every product fiber $hq=n$; cellwise absolute
summation therefore reproduces the same loss. This exact restricted
convolution is recorded as RCS and remains open.

Round 14 proves the exact global recombination. After grouping $n=hq$, the
stationary amplitude and Vaaler $1/h$ factor simplify to

$$
(hX)^{1/4}q^{-3/4}\frac{\Phi(h/(H_D+1))}{h}
=X^{1/4}n^{-3/4}\Phi(h/(H_D+1)).
$$

The frequency-shell partition disappears, but the denominator-scale sum
retains the exact angular multiplier

$$
\Omega_X^*(n,h)=\sum_j\mathbf1_{h\le H_j}
\Phi\left(\frac h{H_j+1}\right)
\left[w_j\left(2h\sqrt{\frac Xn}\right)\right]^*.
$$

Thus the total active M1 contribution is a radial square-root phase weighted
by the floor-perturbed angular divisor coefficient

$$
\mathcal C_X^*(n)=
\sum_{hq=n,\ q\text{ odd}}\chi_4(q)\Omega_X^*(n,h).
$$

The corresponding single global real-part estimate is strictly weaker than
uniform blockwise M9-M1, but remains open. At $X=y^2,n=7$, the active
factorization $(h,q)=(1,7)$ survives while $(7,1)$ is outside $d\le y$;
therefore $\mathcal C_X^*(7)\ne0$ although $r_2(7)/4=0$. M1 alone does not
collapse to $r_2/4$. Popov's audited truncated Voronoi formula shows that a
full angular completion would reproduce the Hardy radial sum and hence be
equivalent to the target up to target-sized errors.

Rounds 15--16 separate and reflect the remaining angular coefficient. The
exact arithmetic modes are

$$
\tau_{\chi_4,z}(n)=\sum_{hq=n,q\text{ odd}}\chi_4(q)h^{-z},
\qquad
\sum_n\tau_{\chi_4,z}(n)n^{-s}=\zeta(s+z)L(s,\chi_4).
$$

They satisfy the accepted centered functional equation

$$
\Lambda_z(s)=\Lambda_{-z}(1-s).
$$

At finite contour height, returning the reflected mode to common positive
Mellin contours crosses the zeta, height, and hard-top Perron poles. The
root number is $+1$. Moreover symmetric Perron reflection completes rather
than cancels:

$$
\mathscr P(F)+\mathscr P(F(-\cdot))=\sum_\nu c_\nu.
$$

Actual angular reflection would require $D\mapsto4X/D$, outside the active
scale range, together with reflected height floors and Vaaler profiles. The
remaining accepted candidate is therefore a maximal actual-profile
angular-sign radial correlation. Its proof is open. Round 17 tests whether
the coefficient-level relation between $a_z(n)$ and $a_{-z}(n)$, including
the prime $2$, decomposes that kernel into a simpler exact eigenspace.

Round 17 proves the exact local law

$$
a_{-z}(2^km)=\chi_4(m)2^{kz}a_z(2^km),\qquad m\text{ odd},
$$

and an exact norm-one projection of the maximal kernel onto its matching
profile eigenspace. This structure removes neither the generic pair of
arithmetic poles nor the separate spatial and height Mellin axes; only the
joint antisymmetric residue vanishes. Conditional on a termwise uniform
$O(\log X)$ bound for the post-residue scalar profile kernel, the range
$v_2(n)\ge\lceil\log_2(2X^{1/8})\rceil$ is absolutely target-sized. The
scalar bound is now the isolated Round-18 validation seam.

Round 18 resolves that seam with a scope correction. The direct physical
profile has the proved scalar estimate

$$
\sup_{T,h,q}|\mathcal H^{\rm prof}_{T,X}(h,q)|\ll_W\log(2X),
$$

but the post-functional-equation remainder is not scalar: its gamma and
radial transforms remain coupled in $(s,u,v)$ and introduce a dual radial
index. Therefore the full reflected high-$2$-adic tail is still conditional.
Round 19 derives the actual finite vector Hankel kernel and its complex-shift
phase diagram.

Round 19 completes that finite derivation. The exact reflected operator has
a dual radial index, retained arithmetic and axial residues, and finite
horizontal sides. Its conductor

$$
4(1+|t+\eta/2|)(1+|t-\eta/2|)
$$

has swept transition strips at $t=\pm\eta/2$. Bounded $\eta$ gives only the
known near-product return, while no uniform large-shift or horizontal-side
estimate is proved. Round 20 attacks the diagonal transition coordinates and
nested contour exhaustion.

Round 20 proves the exact diagonal single-transition normal forms. It also
shows that faster nesting alone cannot delete the radial sides absolutely:
the hard radial endpoints produce only $S^{-1}$ decay, and the hard top
transition traces remain nonintegrable in absolute value. Round 21 therefore
renormalizes the radial Mellin transform by subtracting its endpoint
asymptotic series and tests the resulting signed boundary/residue operator.

Round 21 proves that arbitrary-order subtraction removes the renormalized
radial sides. It also fixes full endpoint weights, upper/lower orientations,
and artificial-pole cancellation. What remains is a finite explicit endpoint
boundary operator plus the two diagonal transition traces. Round 22 freezes
$M=1$ and applies finite Cauchy algebra to identify that boundary operator in
original arithmetic variables.

Round 22 completes that identification. For each physical radial endpoint,
the terminal line plus oriented sides and artificial residue equals an
original-sector finite Perron term minus the arithmetic residue share. The
lower endpoint is target-safe. After the profile limit the upper endpoint is

$$
e(\sqrt{XN_X})\sum_{n\le N_X}^{*}\mathcal C_X^*(n)n^{-3/4},
$$

so it has the same angular coefficient as GAR but lacks GAR's internal
$e(\sqrt{Xn})$ oscillation. Triangle inequality gives only physical size
$X^{3/8}\log^2X$. Round 23 proves the fixed-scale sampled-variation
estimate and then applies period-four Abel summation in $q$. The normalized
upper endpoint is $O_W(1)$, hence its physical M1 contribution is
$O_W(X^{1/4})$. Both radial endpoints are now target-safe. This statement
begins after the accepted physical symmetric-profile limit; it does not
provide a uniform finite-top-Mellin estimate. The next exact survivor is
the recombined $R_1$ arithmetic residue, followed by the two diagonal
transition traces.

Round 24 resolves that recombined $R_1$ arithmetic residue. The exact
physical return uses $1/\delta=\int_0^1r^{\delta-1}dr$ and $y=xr$.
Fixed-$y$ sampled BV and Abel summation in the $\chi_4(q)$ variable prove
a normalized $O_W(1)$ bound, hence $O_W(X^{1/4})$ physically. The radial
endpoint/residue package is now complete; the two diagonal transition
traces remain the smallest transformed survivor.

Round 25 proves the exact finite factor-by-factor reformulation. Put
\(A=s-z/2\) and \(B=s+z/2\), so their terminal reflected heights are
\(\beta\) and \(\alpha\). The two pointwise mixed factors are

$$
\zeta(1-A)X_4(B)L(B,\chi_4),
\qquad
X_\zeta(A)\zeta(A)L(1-B,\chi_4).
$$

Thus the \(\beta\)-bounded branch is character-high and the
\(\alpha\)-bounded branch is zeta-high. This finite substitution crosses
no pole and retains the masks, actual profiles and floors, radial remainder,
outside sides, residue ledger, and physical normalization. It does not
estimate either trace. Absolute height capacity still grows polynomially;
the pure sine/cosine kernels have coherent resonances that invalidate naive
coefficientwise Abel summation; and moving a transition-restricted contour
creates Cauchy--Pompeiu or strip-edge connectors. The arithmetic pole met by
a beta-branch shift is \(A=0\), already represented by the closed
\(R_1\) residue. The apparent \(A=1\) zero-pole pair is removable. The
smallest transformed survivor is therefore the connector-completed pair of
mixed traces coupled to radial integration and the symmetric top Hilbert
operator.

Round 26 fixes the beta-connector algebra. If (A=s-z/2=x+iy),
(R=[x_1,x_0]\times[-T,T]), and (Theta(y;z)) is the prescribed height
mask, then positive rectangle orientation gives

$$
V_{x_0}=V_{x_1}+H_+-H_-+2\pi i\sum_{p\in R}\Theta(\Im p;z)
\operatorname{Res}_{A=p}\mathcal F
-\iint_R\partial_y\Theta(y;z)\mathcal F(x+iy;z)\,dx\,dy.
$$

For the disjoint choice
(Theta_\beta=\psi(\beta)(1-\psi(\alpha))), the area multiplier is

$$
\psi'(\beta)(1-\psi(\alpha))-\psi(\beta)\psi'(\alpha),
$$

and the (A=0) residue has weight (1-\psi(\Im z)). It is therefore not
controlled separately by the unmasked Round-24 (R_1) theorem. Moreover,
the artificial (E_1/R_1) pole must remain recombined through this shift.

Round 27 corrects the operator scope of the following stationary
normalization. The positive-alpha stationary point satisfies

$$
\alpha_0=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
|\Psi''(\alpha_0)|=\alpha_0^{-1}.
$$

For the unsplit radial transform (G=E_1+R_1), the gamma power, arithmetic
coefficient, and stationary Hessian factor combine to (q^0). Thus its
leading character kernel is

$$
D_M^\chi(\theta)=\sum_{q\le M}\chi_4(q)e^{-iq\theta},
\qquad \theta=\frac{\pi\sqrt{Xx}}{D_j},
$$

with

$$
\sup_{M\le Q}|D_M^\chi(\theta)|
\ll\min(Q,1+|\cos\theta|^{-1}),\qquad
\int_0^{2\pi}\sup_{M\le Q}|D_M^\chi(\theta)|d\theta\ll\log(2Q).
$$

This finite kernel lemma remains accepted, but it is not the correct
normalization for the post-endpoint (R_1) survivor. The hierarchical
partition

$$
1=\psi(\beta)+(1-\psi(\beta))\psi(\alpha)
+(1-\psi(\beta))(1-\psi(\alpha))
$$

assigns the double-bounded box to the beta branch. Carrying (G) through
the displacement and then removing the complete same-mask endpoint image
gives the exact artificial-pole-safe identity

$$
R_1=\omega G+(1-\omega)R_1-\omega E_1.
$$

At a separated positive-alpha saddle, the explicit (1/\rho) factor in
(R_1) contributes one inverse (q). For the hard top, the symmetric
physical split

$$
(a+i\mu)^{-1}\longrightarrow
\pi\delta_0(\mu)-i\operatorname{PV}(1/\mu)
$$

and the signed two-denominator convolution contribute another inverse
frequency. On fixed (\Re v=b>0), away from saddle entry, saddle exit, and
the artificial-(\rho) seam, the resulting local coefficient is
(O_b(q^{-2})) up to the recorded scale, radial, and polylogarithmic
factors. Pointwise complete-profile (q)-BV before this signed split is
false at an actual top-pole sample.

The accepted gain is strictly local. Uniform saddle-transition patching,
the double-bounded kernel, complete scale/height/radial summation,
endpoints, and finite outside-height limits remain open.

Round 28 resolves the local transition geometry but finds a finite-height
obstruction. The exact signed Stirling phase has two saddles,

$$
\alpha=\pm\frac{\pi q\sqrt{Xx}}{D_j},
$$

with opposite Hessian signs. Conditional on a scale-normalized
(C^2) bound for the complete recombined signed amplitude, an exact Morse
coordinate gives incomplete Fresnel factors uniformly through entry and
exit; an endpoint saddle has the expected half-Fresnel coefficient and
loses no extra power of (q).

At finite (v)-height, however, the moving hard-top pole creates

$$
\int_{-V}^{V}\frac{H_b(\nu)}
 {a+i(L-\nu)}\,d\nu
=-iH_b(V)\log(1/a)+O(1),\qquad L=V,
$$

whenever the actual height amplitude is nonzero at the edge. Thus the
truncated vertical cannot be replaced uniformly by a whole-line PV
operator before its oriented outside-(v) sides are included. The next
exact kernel is their finite-contour reconciliation, together with the
axial/top/corner ledger. The beta trace remains open.

Round 29 corrects that proposed reconciliation. For upward verticals and
both horizontal sides written left-to-right, positive orientation gives

$$
{\cal V}_b={\cal V}_\ell+{\cal S}_+-{\cal S}_-
+2\pi i\sum\operatorname {Res}.
$$

The edge-log coefficients of the retained sides agree with those of the
original vertical, so the sides reproduce or transfer the logarithm rather
than cancel it. They are contour connectors, not the omitted
((|\nu|>V)) height tails, and the physical top limit moves the
(u)-line rather than the (v)-line.

Restoring the exact polytope nevertheless resolves the apparent divergence.
With (mu=L-\nu), the signed finite box satisfies

$$
\begin{aligned}
\lim_{a\downarrow0}\int_{-V}^{V}\int_{-U}^{U}
\frac{F(\mu,\nu)}{a+i\mu}\,d\mu\,d\nu
={}&\pi\int_{-V}^{V}F(0,\nu)\,d\nu\\
&-i\int_{-V}^{V}\operatorname {PV}\!\int_{-U}^{U}
\frac{F(\mu,\nu)}{\mu}\,d\mu\,d\nu.
\end{aligned}
$$

Its fixed-(L) sections have locally integrable logarithmic singularities,
although their first two pointwise derivatives are singular. Thus the
Round-28 scaled-(C^2) Fresnel tool remains valid only away from moving
faces. The new open interface is a distribution-first logarithmic-amplitude
two-saddle estimate, followed by height exhaustion and all arithmetic and
profile sums. The beta trace remains open.

### Complete finite beta axial ledger (Rounds 33--34)

Global three-mask recombination must precede the accepted unmasked endpoint
module. At fixed finite contours, the beta mask
\(\Theta_\beta=\psi(t-(\mu+\nu)/2)\) then satisfies the exact two-axis
product-Cauchy--Green identity

$$
\begin{aligned}
F_uF_v+F_uP_v+P_uF_v+P_uP_v
&+\tfrac12(F_uA_v+P_uA_v+A_uF_v+A_uP_v)[\psi'Q]\\
&+\tfrac14A_uA_v[\psi''Q].
\end{aligned}
$$

Here \(F_j\) is the final vertical plus upper-minus-lower horizontals,
\(P_j\) is the coordinate-axis residue, and \(A_j\) is positive area
integration. Expanding the \(F_j\) gives sixteen strata; the two transfer
orders agree, the joint corner occurs once, and a common transfer preserves
the \(G=E_1+R_1\) artificial-pole cancellation. This applies to the full
actual finite pre-limit vector with every profile, floor, star, character,
and normalization retained.

This is not yet the post-module physical axial vector. The accepted
endpoint and arithmetic estimates occur only after physical profile limits,
while renormalized radial-side deletion uses a prescribed nested exhaustion.
The graph now isolates two exact commutation obligations: transfer through
the radial-side exhaustion and transfer through the physical
endpoint/arithmetic modules. The axial-subtracted terminal symbol remains
undefined until both close.

Round 35 closes the first of these two obligations. Since the fixed beta
mask is supported in \([-2B_0,2B_0]\), on the reflected radial sides
\(|\beta|\ge S-(U+V)/2\). Once
\(S>(U+V)/2+2B_0\), \(\psi\), \(\psi'\), and \(\psi''\) vanish on the
entire finite side cell complex. Hence every one of the sixteen transferred
side strata is exactly zero, including all axes, connector residues,
collisions, mixed area, and the corner. The radial-side limit therefore
commutes with beta transfer, with \(M=1\) already sufficient. The sole
remaining boundary interface is the physical endpoint/arithmetic module.

Round 36 closes that second boundary interface without a termwise limit
theorem. For the three hierarchical masks \(\Theta_\beta,\Theta_\alpha,
\Theta_o\), sum every finite two-axis transfer stratum before taking any
physical limit. The masks sum to one, and their first and mixed derivatives
sum to zero after every face, axis, collision, and corner restriction.
Hence all mask connectors cancel. The ordinary unmasked cells remain, but
their complete finite Stokes sum is exactly the original positive-line
module

$$
\mathfrak M_{\rm fin}
=\sum_{\xi\in\{1,N_X\}}D_{\xi;U,V,S}
 +\mathfrak R^{\rm ar}_{U,V,S}[R_1].
$$

Using the original fixed-\(w\) meromorphic representative is essential;
freezing the shifted off-centred Perron path would omit moving boundary
terms. After exact finite routing, the licensed symmetric physical limits
give normalized \(O_W(\log X)\), and therefore physical
\(O_W(X^{1/4}\log X)\), with every star, profile, floor, character, and
artificial-pole cancellation retained. This proves both boundary-module
compatibility interfaces. It does not prove termwise masked limits or the
limit of the exact endpoint-free complement
\(\mathfrak V_{\rm pre}^{\rm fin}-\mathfrak M_{\rm fin}\); that is the
next proof obligation before the axial-subtracted terminal symbol can be
estimated.

Round 37 identifies that complement exactly. On the same fixed-$w$ finite
antecedent and under common artificial-pole ownership,

$$
\mathfrak V_{\rm ef}^{\rm fin}
=\mathfrak T[R_1]+\mathfrak S[R_1]+\mathfrak P_\rho[R_1].
$$

Compact beta support annihilates the complete transferred
\(\mathfrak S[R_1]\) cell complex. The terminal/artificial remainder has
the sixteen accepted product Cauchy--Green strata, including both axial
families, every first connector, the mixed \(\psi''/4\) area, one combined
collision coefficient, and one corner. At fixed finite \(U,V,S\), its top
boundary is canonically

$$
\frac1{2\pi}(0^++i\mu)^{-1}
=\frac12\delta_0(\mu)-\frac{i}{2\pi}\operatorname{PV}\frac1\mu.
$$

The associated moving-face logarithms are locally integrable. After the
complete optional outside cells are recombined by finite Stokes, the sole
remaining existence condition is the signed positive-line tail

$$
-\frac4\pi X^{1/4}\Re\!\left\{
e(1/8)\frac1{2\pi}
\int_{V_1<|\nu|\le V_2}
\mathcal F^{\rm ef}_{b;U,S}(\nu)\,d\nu\right\}\longrightarrow0
$$

uniformly along the prescribed height and physical-profile net. This
Cauchy-tail theorem is open. Finite Plemelj convergence, compact beta-mask
Fourier decay, and local moving-log control do not imply it without a joint
height majorant or an actual-kernel signed cancellation theorem. Hence the
limiting endpoint-free axial vector and its local terminal symbol remain
undefined.

Round 38 proves the missing global tail and therefore defines the limiting
vector. Choose \(c'=5/4\), \(b=1/\log(2X)>0\), and put

$$
t=\frac{\mu+\nu}{2}+\beta,
\qquad
\alpha=\mu+\nu+\beta,
\qquad
\eta=\frac\mu2+\nu+\beta.
$$

The change has Jacobian one. The bounded-beta completed factor contributes
no tangent growth, whereas the other gamma quotient has exponent

$$
\kappa=\frac34+\frac{a+b}{2}<1.
$$

The exact terminal coefficient is

$$
h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}
q^{-i(\mu+\nu)}(hq)^{-i\beta},
$$

so its \(h,q\) sum and one logarithmic derivative converge absolutely.
Moreover

$$
\rho=-1-\frac b2-i\eta,
\qquad
|R_1|+|\partial_\mu R_1|\ll_X(1+|\eta|)^{-1}.
$$

Keeping

$$
\frac12\delta_0(\mu)-\frac{i}{2\pi}\operatorname{PV}\frac1\mu
$$

intact before taking absolute values, the tangent convolution is bounded by

$$
(1+|\nu|)^{\kappa-1}\log(2+|\nu|).
$$

The cubic decay of the physical height profile therefore gives

$$
|\mathcal F_T(\nu)|\ll_{X,b}
(1+|\nu|)^{\kappa-4}\log(2+|\nu|).
$$

On the separate artificial-pole cell, the terminal coefficient expansion
is outside its absolute chamber and is not used. The exact recombined
factor \(\zeta(1-A)L(1-B,\chi_4)\), compact beta support, and period-four
Abel summation yield \(O_{X,b}((1+|\nu|)^{-3})\). These majorants are
integrable and uniform in the symmetric height cutoffs. Compact beta
support makes the radial-side stage eventually constant. Consequently
\(\mathfrak V_{\rm ef}^{\rm fin}\) has a unique physical/outside-height
limit, and the connector-completed mask--endpoint--axial decomposition is
now rigorous.

This is an existence theorem with unrestricted fixed-\(X\) constants. It
does not prove the weighted \(\lambda^{-2}/\lambda^{-3}\) bounds for the
axial-subtracted terminal symbol.

Round 39 corrects the formulation of that quantitative interface. The
limiting vector is already summed over (j,h,q) and integrated over (x),
so it has no single

$$
\lambda_{j,q,x}=\frac{\pi q\sqrt{Xx}}{D_j}.
$$

The quantitative symbol must be frozen cell by cell, with the complete
stationary phase removed and the stationary numerator
((D_j/q)\lambda), character, coefficient monomial, contour factors,
radial integral, floors, stars, and external (X^{1/4}) factor kept
outside. Only the singular (u^{-1}) hard-top share uses the signed
Plemelj regularizer. With

$$
A=-1-\frac b2-i(L+\beta),\qquad
D=A+\frac i2(L-\nu),
$$

its exact regular part is

$$
\mathcal R_A[H]=-\frac{iH(L,L)}{2AD}
+\frac{H(L,\nu)-H(L,L)}{(L-\nu)D}.
$$

Smooth top remainders and interior profiles retain ordinary
(\mu)-integration. At fixed physical (\nu), differentiation exposes
the first unproved actual coefficient

$$
\mathfrak E_H=
\frac{\partial_LH(L,\nu)-(\partial_L+\partial_\nu)H(L,L)}{L-\nu}
-\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2}.
$$

The required statement is a mixed value/derivative/moving-trace norm of
size (X^\varepsilon\lambda^{-2}), augmented by the exact normalized
Morse remainder through both signed saddles and entry/exit. The separated
kernel already has this scale, and smooth translated profiles cost only a
polylogarithmic harmonic weight. The complete coefficient remains open.

Conditional on that mixed norm, the remaining leading arithmetic and
radial sums close. Writing (r=5/4-(a+b)/2), the post-stationary
coefficient before the external normalization is

$$
|\chi_4(q)|h^{-r}q^{-2}D_j^{2-r}X^{r/2-1/2+b/4}
x^{-r/2-b/2-5/4}.
$$

Radial integration contributes
(\min(1,(\sqrt X|2\mp q/D_j|)^{-1})). The formal exact resonance
(q=2D_j) is even and hence has coefficient zero under (\chi_4); all
remaining (q,h,j) sums are polylogarithmic. Thus the leading large-alpha
package is (O(X^{1/4+\varepsilon})) once the mixed symbol lemma is proved.
Bounded-alpha, double-bounded, and full beta assembly remain separate open
interfaces.

## 10. Exact remaining gaps

1. **Top signed cones.** Prove the exact M2 estimate in Section 8.6F and
the M1 product-phase cone estimate recorded above, or close a top block by a
stronger direct argument. Both one-sided transforms, endpoint half-weights,
boundary series, and summed errors are complete. Exact M1/M2 cone
complementarity does not provide cancellation.

2. **M9-M1 angular/RCS/PSC discrepancy.** Prove the exact RCS restricted
convolution, or equivalently the annular PSC/odd-kernel sum on
$\mathcal U_1$. The terminal line, TTY wedge, and $(1/2,0)$ are solved.
Fiberwise, frozen-kernel, opposite-offset, and cellwise-absolute shortcuts
are ruled out. The Round-14 global angular real-part estimate is a weaker
sufficient object for total active M1 but remains unproved. The exact Mellin
separation and finite-height reflection are complete, but they leave a
maximal actual-profile angular-sign kernel; Round 17 tests its local
reflection eigenspaces. Their exact algebra is complete; Round 18 tests the
pointwise post-residue profile-kernel bound needed to remove the high
$2$-adic tail. Round 18 proves that bound only for the direct profile and
rejects the scalar post-FE formulation; the open survivor is now the
vector-valued Hankel operator.

3. **M9-M2.** Prove a sign-preserving pointwise estimate on the explicit residual corridor $\mathcal U$.

4. **Near-collision bands.** Extend the exact-$N=0$ module to a coefficient-weighted estimate for $0<|N|\sim T$ without discarding the useful character sign.

5. **Endpoint uniformity.** Every argument must remain valid at $D=X^{1/2}$, where $H_D=X^{1/4}$ and coherence windows have length $O(1)$.

6. **Average-to-pointwise upgrade.** Supply a large-value theorem or direct pointwise argument strong enough to overcome the derivative loss.

7. **Signed fat-band definition and estimate.** Fix one normalization of $c_\chi$, prove the required signed bound, and state exactly how it feeds a pointwise theorem.

8. **Post-transform signed estimate.** For smooth interior blocks, prove
the outside-absolute small-gcd quarter-packet estimate in Section 8.6E, or
prove an equivalent actual-symbol $M^{3/4}$ product-phase bound in a new
part of $\mathcal U$. The transform and packet identity are complete; the
cancellation estimate is not.

9. **Literature source audits.** The Tao--Trudgian--Yang exponent pair is a validated dependency. Li--Yang, Huxley, and Bourgain--Watt remain comparison material rather than proof dependencies until their exact hypotheses are transcribed.

## 11. Resolved Round 9 weighted-mass issue

The old formal Round 9 did not complete its review and judge stages. The Codex-managed Round 1 adjudication and Round 2 seam validation have now resolved its count-versus-weighted-mass dispute through a validated State Patch.

The proposed upper bound $D+D^4/X$ for the actual absolute beta-weighted mass is false. The fixed unit-frequency family has constant-size Vaaler weight and weighted same-window energy $\gg MD$. After exact-resonance subtraction it gives the lower bound in Section 8.5 and the sharper $X^{1/3}$ crossover, subject to the actual block's sampled $\ell^1$ nondegeneracy.

Nothing in Sections 1--7 depends on this obstruction, so the conditional endpoint reduction is otherwise unaffected.

Round 40 corrects the terminal norm itself. If
\(y=L-\nu\) and \(F(L,y)=H(L,L-y)\), then

$$
\mathfrak E_H
=\int_0^1F_{Ly}(L,ty)\,dt
+\int_0^1tF_{yy}(L,ty)\,dt.
$$

This is signed algebra and its two terms cannot be bounded independently.
The complete singular regularizer also contains

$$
K_C(L,\nu)=-\frac{iH(L,L)}{2A(L)D(L,\nu)}
=\frac{H(L,L)}{A(L)\nu}+O_L(\nu^{-2}),
$$

so it is not an absolute \(L^1(d\nu)\) symbol. Its exact physical-section
primitive is

$$
C_{U,V}[H](L)=\frac{H(L,L)}{A(L)}
\{\Log D(L,q(L))-\Log D(L,p(L))\},
$$

where \([p(L),q(L)]=[-V,V]\cap[L-U,L+U]\). For the separated actual
profile,
\(\|C\|_\infty+\operatorname{Var}C
\ll_b\lambda^{-4}\log(2+\lambda)\), and the same target-safe capacity
holds under incomplete-Fresnel localization when the section is formed
first. Thus the separated finite-section BV/local \(q^{-2}\) conclusion
remains valid, but its old pointwise integrable-weight proof is retracted.

The surviving large-alpha lemma is hybrid: control the diagonal by this
signed section and prove the absolute mixed norm only for the complete
off-diagonal divided difference and smooth ordinary-\(\mu\) shares, with
long translations recombined into endpoint differences and with all
connector, moving-face, and exact Morse terms retained. That complete
product-cell estimate is still open.

Round 41 proves this hybrid large-alpha lemma. Freeze one signed
post-routing cell and set

$$
\lambda=\frac{\pi q\sqrt{Xx}}{D_j},
\qquad
p(\nu)=e^{i\gamma\nu}\widehat\phi(b+i\nu),
\qquad
\gamma=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}.
$$

After removing the canonical phase

$$
\Psi'(L)=\log\frac{|L+\beta|}{\lambda},
\qquad \Psi''(L)=\frac1{L+\beta},
$$

the lower exact Stirling corrections remain in a normalized symbol
\(G\) satisfying
\(\partial_L^mG\ll_\varepsilon X^\varepsilon\lambda^{-m}\) for
\(m\leq2\). The actual profile has integrable derivatives and genuine
cubic height decay. With

$$
D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right),
$$

the singular off-diagonal and smooth cells are

$$
K_\Delta=G(L)\frac{p(\nu)-p(L)}{(L-\nu)D},
\qquad
K_W=G(L)p(\nu)\frac{W(L-\nu)}D.
$$

At fixed physical height, the derivative of the divided difference is
formed before absolute values. A four-region height decomposition then
controls values, integrated derivatives, moving traces, both signed
saddles, entry/exit, and the exact normalized Morse remainder by
\(O_\varepsilon(X^\varepsilon\lambda^{-2})\). The diagonal factor
\(H(L,L)=C(\beta)G(L)p(L)\) is integrated as the exact signed logarithmic
Cauchy section before the same Morse passage. This proves the complete
large-alpha hybrid symbol.

Multiplying by the retained stationary numerator and invoking the exact
coefficient ledger gives, before the external normalization,

$$
|\chi_4(q)|h^{-r}q^{-2}D_j^{2-r}
X^{r/2-1/2+b/4}x^{-r/2-b/2-5/4},
\qquad r=\frac54-\frac{a+b}{2}.
$$

The radial integral contributes
\(\min(1,(\sqrt X|2\mp q/D_j|)^{-1})\); the formal resonance
\(q=2D_j\) is even and hence killed by \(\chi_4\). The remaining
\(h,q,j\) sums are polylogarithmic. Restoring the external factor proves

$$
\mathfrak B_{\beta,\mathrm{large}\text{-}\alpha}(X)
\ll_\varepsilon X^{1/4+\varepsilon}.
$$

This is only the complete large-alpha beta package. The bounded-alpha,
double-bounded cell, complete beta transition, and alpha-bounded branch
remain open.

Round 42 fixes the exact compact-cell reduction. With

$$
\Theta_{\rm db}(L,\beta)=\psi(\beta)\chi_0(L+\beta),
$$

both \(\beta\) and \(\alpha=L+\beta\) are compact, hence so is \(L\).
The exact gamma quotient retains the unit phase
\(e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}\). Put

$$
A=-1-\frac b2-i(L+\beta),\qquad
D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
$$

After the physical top limit, the singular compact functional is exactly

$$
\frac{g(L,\beta)p_x(L)}{A}
-\frac{ig(L,\beta)}{2\pi}
\int_{\mathbb R}\frac{p_x(\nu)-p_x(L)}{(L-\nu)D}\,d\nu.
$$

The signed diagonal is formed before absolute values. Its exact radial
derivative is governed by

$$
x\partial_x\{g(L,\beta)p_x(\nu)\}
=-i\left(\frac{L+\nu}{2}+\beta\right)g(L,\beta)p_x(\nu).
$$

The accepted theorem in this round is conditional: if the complete
post-routing compact amplitude obeys

$$
\sup_x|\mathcal A(x)|+\int_1^{N_X}|\mathcal A'(x)|\,dx
\ll_\varepsilon X^\varepsilon,
$$

then

$$
\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})\mathcal A(x)\,dx
\ll_\varepsilon X^\varepsilon.
$$

This follows by exact radial integration by parts. Its endpoint
coefficients are full; only pre-existing profile or inverse-Mellin stars
can carry half-values. The beta-masked endpoints are to be bounded
locally, not identified with the global unmasked endpoint module.

Discovery and hostile audits prove the needed compact-amplitude estimate,
including absolute \(h,q\) convergence and the dyadic scale ledger. The
isolated statement packet did not enumerate the complete finite
connector/profile one-count family, so the graph retains that final
compact-cell estimate as an open validation obligation. Thus the beta
transition and all downstream claims remain open.

Round 43 refines that open interface. On the full inherited contour

$$
0\le a,\qquad a+b<\frac12,\qquad \frac a2+b<\frac14,
$$

and with \(x\partial_xM_\tau\) included in the multiplier seminorm, the
displayed abstract compact family satisfies

$$
\sup_x\{|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\}
\ll\log^C(2X).
$$

This is not yet an accepted actual-cell theorem. The isolated proof was
contaminated by graph exposure, and the formula omits both the \(j=0\)
regular-top/\(j\ge1\) interior selectors and the finite ownership map from
the product Cauchy--Green ledger. Alpha recombination cancels the
\(\chi_0'\) and \(\chi_0''\) terms but leaves

$$
\frac14A_uA_v[\psi''(\beta)Q_T],
$$

whose compact type and module ownership have not been named. The graph
therefore keeps the double-bounded cell and complete beta transition open
at this exact selector/ownership certificate.

Round 44 corrects that interface. At fixed finite contour height, the
sixteen product Cauchy--Green terms obey one complete Stokes identity

$$
\sum_{k=1}^{16}\mathcal C_k[\psi Q_{\rm ef}]
=R_uR_v[\psi(\beta)Q_{\rm ef}].
$$

No individual \(\mathcal C_k\) has a licensed physical limit. Hence a
rowwise \(\tau\)-type or physical-module label is not merely missing; it
is the wrong operator type. The correct compact/large-alpha split is made
on the positive-line right side:

$$
R_uR_v[\psi Q_{\rm ef}]
=R_uR_v[\psi\chi_0Q_{\rm ef}]
+R_uR_v[\psi(1-\chi_0)Q_{\rm ef}].
$$

If these localized pieces are transferred again, all connector terms
reappear. In particular, the positive mixed
\(A_uA_v[\psi''Q]/4\) term is encoded in the whole-vector identity and
cannot be deleted termwise. The central positive-line terminal contains
the \(j=0\) singular Plemelj share, the \(j=0\) regular top, and the
\(j\ge1\) interior profiles, with all original floors, stars, character,
and normalization.

The replacement certificate remains open at the oriented artificial-pole
coefficient and the exact match of the positive-line complement to the
accepted large-alpha theorem. On the artificial pole the radial factor has
the exact candidate simplification

$$
\pi i\sqrt X\,I_1(0)
=e(\sqrt{XN_X})-e(\sqrt X),
$$

which removes the crude \(O_X(1)\) loss and makes a target-safe residue
bound plausible. It has not yet passed the independent gate, so the
double-bounded cell and all downstream claims remain open.

Round 45 proves the previously open compact and artificial pieces. On the
returned positive lines, the central terminal is the exact three-selector
functional and satisfies

$$
\sup_x\bigl(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\bigr)
\ll\log^C(2X).
$$

The signed Plemelj diagonal is formed before absolute values, and the
complete x-phase gives the bounded multiplier

$$
\frac{(L+\nu)/2+\beta}
{-1-b/2-i((L+\nu)/2+\beta)}.
$$

Absolute (h,q) convergence and the dyadic scale ledger are
polylogarithmic, so the accepted radial-BV reduction gives a physical
(O(X^{1/4}\log^C X)) central contribution. At the artificial pole,

$$
\operatorname {Res}_sR_{1,v}(1-s)=+\pi i\sqrt X I_1(0),qquad
\pi i\sqrt X I_1(0)=e(\sqrt{XN_X})-e(\sqrt X).
$$

The zeta factor has compact beta height away from its pole, while
period-four Abel summation and cubic height decay make both alpha shares
polylogarithmic. The graph now accepts this scoped compact/artificial
lemma.

The aggregate certificate nevertheless remains open. The Round-41 node
proves signed saddle, entry, and exit cells, but no accepted artifact yet
exhibits an identical-antecedent finite partition summing to
(1-\chi _0\) and bounds every nonsaddle remainder. That is now the only
large-alpha complement seam; it must not be inferred from the word
“complete” in a theorem title.

Round 46 supplies the missing exact partition, but not the missing
estimate. With \(t=|\alpha|/\lambda\), choose smooth nonnegative
\(c_0+c_1+c_\infty=1\) so that

$$
\operatorname{supp}c_0\subset[0,3/4],\qquad
\operatorname{supp}c_1\Subset(2/3,3/2),\qquad
\operatorname{supp}c_\infty\subset[4/3,\infty),
$$

and \(c_1=1\) on \([3/4,4/3]\). Multiplying these cutoffs by the
preliminary normalized partition and by a signed partition whose
transition lies in \(1-\chi_0=0\) gives a finite smooth nonnegative
refinement summing exactly to \(1-\chi_0\). On the grouped nonsaddle
pieces,

$$
|\Psi'|=\left|\log\frac{|\alpha|}{\lambda}\right|
\ge\log(4/3).
$$

This is an accepted reduction only. The complete beta localization still
requires global value, phase-conjugated x-derivative, moving-trace, and
outer-limit estimates for the actual signed Plemelj section under the raw
\(q^{-p}\) ledger, plus literal Round-41 middle-cell coverage or cutoff
invariance.

Round 47 now supplies those estimates.  On dyadic intrinsic-height cells
\(R\asymp1+|\alpha|\), the exact returned positive-line section satisfies

$$
 |\mathcal P|+R|\partial_L\mathcal P|
 \ll \log^C(2X)R^{\kappa-2},
$$

$$
 |\mathcal Q|+R|\partial_L\mathcal Q|
 \ll \log^C(2X)R^{\kappa-1}.
$$

The signed diagonal logarithm is evaluated before absolute values and is
smaller by two powers.  The phase-conjugated radial derivative retains

$$
 \frac{\eta p(\nu)-\alpha p(L)}{L-\nu}
 =\alpha\frac{p(\nu)-p(L)}{L-\nu}-\frac12p(\nu).
$$

Since \(\kappa<1\), one nonsaddle phase integration by parts is summable,
moving faces vanish under symmetric exhaustion, and the true outer
boundary terms vanish.  Absolute convergence of the untouched
\(h^{-r}q^{-p}\) ledger and the radial-BV identity then give
\(O(X^{1/4}\log^C X)\) for the inner and outer sectors.

Smooth scaled-cutoff invariance of the accepted Round-41 theorem covers
the repaired middle sector.  Therefore the central compact cell,
artificial residue, middle saddle package, and both nonsaddle sectors form
one exact target-safe positive-line beta partition.  This proves the
positive-line localization certificate and aggregate double-bounded cell;
it does not prove the separate alpha-bounded branch, M9-M1, M9, or the
Gauss-circle target.

Round 48 now consolidates that accepted partition into the complete beta
transition.  At finite \((U,V,S)\), the three hierarchical masks and all
sixteen product Cauchy--Green strata are summed before physical limits.
The derivative connectors cancel, endpoint and recombined \(R_1\)
arithmetic modules return once, compact beta support removes the
renormalized radial sides, and the endpoint-free vector receives its
signed Plemelj and joint height limit.  Only then is the positive-line
alpha partition inserted.  With compact, artificial, middle, and
nonsaddle owners as above,

$$
 \mathcal R_\beta^{U,V,S}
 =\mathcal B_\beta^{U,V,S}-\mathcal M_{\rm phys}^{U,V,S}
 -\mathcal E_{\rm c}^{U,V,S}
 -\mathcal A_{\rho,0}^{U,V,S}-\mathcal A_{\rho,\infty}^{U,V,S}
 -\sum\mathcal E_{{\rm mid},k}^{U,V,S}
 -\sum\mathcal E_{{\rm ns},k}^{U,V,S}=0.
$$

Thus the normalized beta-bounded character-high trace is
\(O_\varepsilon(X^\varepsilon)\), and its physical image is
\(O_\varepsilon(X^{1/4+\varepsilon})\) after the external factor is
restored once.  This promotes the complete physical-height, hybrid regular
finite-part, logarithmic two-saddle, and connector beta wrappers.  It does
not alter the rejected all-absolute diagonal or rowwise-mask claims.

The remaining mixed trace is the alpha-bounded zeta-high operator

$$
 X_\zeta(A)\zeta(A)L(1-B,\chi_4),
 \qquad A=s-z/2,\quad B=s+z/2.
$$

Its unsigned high coefficients, transition connectors, outside sides,
\(A=0\) arithmetic reconciliation, and axial/top/corner strata require a
new joint estimate.  No downstream vector or Gauss-circle claim follows
until that separate branch and the remaining post-FE interfaces close.

Round 49 supplies the exact distributional architecture of this branch.
For compact smooth Mellin tests,

$$
 \frac1{2\pi i}\int_{(c)}X_\zeta(A)\zeta(A)Y^{-A}\,dA
 =\begin{cases}
 \sum_{n\ge1}\delta(Y-n),&c<0,\\
 \sum_{n\ge1}\delta(Y-n)-1
 =2\sum_{h\ge1}\cos(2\pi hY),&c>0.
 \end{cases}
$$

The line change crosses only \(A=0\), whose residue is \(-1\); \(A=1\)
is removable.  With the actual hierarchical alpha mask

$$
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),
$$

multiplication in \(\beta\) becomes logarithmic-Mellin convolution, and
the finite Cauchy--Pompeiu/strip-edge, outside-face, axis, and corner
strata must remain.  Flatness of \(\psi\) at zero implies that
\(\Theta_\alpha\) and its first and mixed outside-axis derivatives vanish
at \(A=0\).  Consequently alpha owns no new arithmetic residue; the
constant mode is already in the accepted \(R_1\) module.

The pure cosine comb is not an estimate.  Its Abel regularization is
coherent at every integer, and the minus radial phase has the stationary
point \(x=Xt^2/(4h^2)\).  The unmasked lattice has normalized absolute
capacity \(X^{1/8+o(1)}\), while the terminal height capacity retains the
positive power \(U^{c'-1/2-\Re z/2}\).  The exact remaining obligation is
therefore the signed, connector-completed logarithmic projection of the
comb/GAR return.  No swept, post-FE, M9-M1, M9, or target conclusion
follows from this reduction.

Round 50 tests the zero-mass high-pass suggested by that projection.  The
coupled multiplier is

$$
 m_\lambda(\beta)=(1-\psi(\beta))\psi(\beta+\lambda),
 \qquad \lambda=\mu+\nu.
$$

Its inverse log kernel has mass zero.  However, if the support of
\(\psi\) lies in \([-M,M]\) and \(|\lambda|>2M\), then

$$
 m_\lambda(\beta)=\psi(\beta+\lambda).
$$

Thus the high-pass is identically one on the bounded-alpha packet.  The
inverse is a moving modulation of the fixed low-pass kernel and has fixed
nonzero \(L^1\) norm.  A lattice atom retains that packet mass, a hard
floor or product-star step retains fixed variation, and \(N\) separated
jumps retain order-\(N\) response.  Zero mass and classical BV alone
therefore cannot save the normalized \(X^{1/8+o(1)}\) capacity.

Finite connectors are rowwise contour identities: they redistribute a
jump trace among line, area/edge, face, axis, mixed, and corner strata.
Their cancellation requires a new theorem for the complete signed row
response after the top Plemelj combination.  That local signed seam
identity, followed by a uniform outside-height Cauchy theorem, is now the
first open alpha interface.  The Round-50 result is a scoped no-go, not a
lower bound for the full signed operator.

Round 51 derives the universal signed jump-incidence ledger.  For a
generic seam \(W_s=W_-+\Delta W S^*(L_s-L_0)\), first connector
derivatives produce \(\delta(L_s-L_0)\) traces, while the mixed connector
also produces a \(\delta'(L_s-L_0)\) trace.  The complete sixteen-cell
finite Stokes expansion reconstructs the original right-line seam with
relative coefficient \(+1\); connector labels do not sum to a scalar
zero.

No actual floor, product-star, profile-edge, or radial-endpoint coefficient
can yet be evaluated.  The accepted graph does not supply a common finite
alpha numerator, a non-overloaded primal seam coordinate, the complete
jump, face/axis pullbacks and velocities, or a collision rule with the
signed Plemelj distribution.  An equality star gives a half point value
but a full distributional jump.  Therefore Round 51 promotes only a
specification/no-go lemma and leaves the alpha estimate open.

Round 52 resolves the first alleged seam.  The Vaaler height

$$
H_j=\lfloor D_jX^{-1/4}\rfloor
$$

is fixed under every alpha and beta contour displacement, and hence has no
moving-face delta.  Its exact discrete unit-height variation is nevertheless
sharp.  With

$$
a_H(h)=\mathbf1_{h\le H}\Phi\left(\frac h{H+1}\right),
$$

one has

$$
\|a_{H+1}-a_H\|_1=\frac12,
\qquad
\sum_h\frac{|a_{H+1}(h)-a_H(h)|}{h}\sim\frac1{H+1}.
$$

All increments have the same sign; the quadratic taper at the new endpoint
does not cancel the bulk retuning of old frequencies.  Moreover

$$
H_{j+1}=\left\lfloor\frac{H_j}{2}\right\rfloor,
\qquad
\|a_K-a_H\|_1=\frac{|K-H|}{2}.
$$

Thus an actual dyadic step retains (H_j)-sized coefficient capacity and
also changes the denominator profile, support, star, scale powers, radial
terms, and normalization.  A future alpha argument must estimate this
complete coupled dyadic difference; neither floor-seam incidence nor a
coefficient-only unit-step Abel transform is admissible.

Round 53 proves that the complete dyadic difference is an obstruction, not
a saving mechanism.  On adjacent interior scales,

$$
\mathcal A_{j+1}-\mathcal A_j
=\widehat W(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
\left\{2^{-u}\left(\frac{H_{j+1}+1}{H_j+1}\right)^v-1\right\}.
$$

The final factor has order-one size at a bounded imaginary $v$-height.  In
physical coordinates, zero extension gives

$$
\mathscr B_{j+1}-\mathscr B_j
=(P_{j+1}-P_j)F_{j+1}+P_j(F_{j+1}-F_j),
$$

and the exact $W=\eta-\eta(2\cdot)$ Abel identity retains the hard top,
inactive bottom, and every coherent height difference.  Fixed-$(h,q)$
original scale terms have one common character-phase and nonnegative scale
weights.

There is an actual star-free plateau witness in the penultimate active
interior pair with $h=1$ and odd $q\asymp\sqrt X$ for which exactly one
scale is nonzero and

$$
\sum_q q^{-3/4}|\mathscr B_{j+1}(1,q)-\mathscr B_j(1,q)|
\gg X^{1/8}.
$$

Hence the external $X^{1/4}$ restores the full $X^{3/8}$ absolute
capacity.  This is not a signed lower bound, but it rigorously excludes
scale-only telescoping, adjacent differencing, and profile BV as sources of
the missing power.  The next admissible mechanism must preserve signed
cancellation between distinct post-scale arithmetic fibers.

Round 54 makes the post-scale shifted-correlation interface exact. On a
consecutive radial block \(I\) of length \(L\), with the exact endpoint
weight included, finite Fejer differencing gives

$$
\left|\sum_{n\in I}c_n\right|^2
\le \frac{L+R-1}{R}\left\{Q_I+2\Re\sum_{1\le r<R}
\left(1-\frac rR\right)\mathcal C_{I,r}\right\},
$$

and the braced form is nonnegative. Expanding the actual angular
coefficients retains \(h_1q_1-h_2q_2=r\) with both characters, floors,
scale profiles, angular stars, and the square-root difference phase.

For \(n\asymp Y\), the exact sufficient target is

$$
\mathfrak F_{Y,R}\ll_\varepsilon X^\varepsilon\frac RY.
$$

Since the diagonal is \(O(X^\varepsilon Y^{-1/2})\), for
\(R\ge Y^{1/2}\) the same \(R/Y\) bound for the absolute value of the full
signed Fejer shift average is sufficient. At
\(Y\asymp\sqrt X\), \(R\asymp X^{1/4}\), this asks for an
\(X^{-1/4}\) quadratic gain, whose square root is the missing normalized
\(X^{-1/8}\).

The differencing step supplies none of that gain by itself. Termwise
absolute correlations return \(Y^{1/4}\) per block and \(X^{1/8}\)
globally; both a bounded adversarial coefficient and an actual star-free
expanded incidence show sharp capacity in their stated scopes. Smooth
radial curvature without coefficient control loses the same square root or
returns the shifted-product kernel. Existing audited spectral and
shifted-divisor theorems do not match the moving angular coefficient. The
signed theorem and its connector-completed alpha transfer remain open.

### Round 55: target-safe low-angular margin

On the critical block \(Y\asymp\sqrt X\), let \(R\asymp\sqrt Y\).
For every product window \(J\) of length at most \(R\), including edge
windows, the exact low-leg coefficient satisfies

$$
 \left|\sum_{n\in J}^{*}A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon X^\varepsilon{H+Q\over\sqrt Y}.
$$

Indeed, a fixed leg \(\ell=h\) or \(q\) has complementary interval
length \(O(R/\ell+1)\) and curvature \(\asymp\ell^2/R\), giving
\(O(\sqrt R)\) by the second-derivative estimate below \(\sqrt R\) and
by the trivial length above it. The exact sampled amplitude has bounded
variation because a short product window meets only \(O(1)\) dyadic
profiles; height floors, hard top, and stars contribute separately
bounded jumps. Exact window propagation yields full-block size
\(O_\varepsilon(X^\varepsilon(H+Q))\).

Moreover active support implies \(q\ge4h\), hence \(q\ge2\sqrt n\) and
\(h\le\sqrt n/2\). The polylogarithmic low-\(q\) margin is empty. After
removing \(h\le(\log X)^B\), the unresolved top-block core is

$$
 (\log X)^B<h\le\sqrt n/2,\qquad q=n/h\ge2\sqrt n.
$$

This scoped result does not estimate that core or transfer through the
alpha connector complex.

### Round 56: fixed-fibre resonance obstruction

For \(q=4m+\rho\), the exact second phase difference is

$$
 \Delta^2F_{h,\rho}(m)
 =-{32\sqrt{Xh}\over
 (\sqrt{q+8}+\sqrt{q+4})(\sqrt{q+4}+\sqrt q)
 (\sqrt{q+8}+\sqrt q)}.
$$

Its size is \(h^2/R\), while its third difference is \(h^3/R^3\).
The relevant discrete parameter is therefore the accumulated curvature
modulo one, not its real magnitude. Nonetheless, any nonnegative fixed-
\(h\) Fejer/Weyl closure already loses \(\sqrt H\) on a shell
\(h\asymp H\), since its diagonal aggregates to \(\sqrt{RH}\).

For \(R/4<h\le R/2\), each residue fibre has at most one sample. An
explicit strict fourth-power top-profile window realizes
\(\sum_{h,\rho}|T_{h,\rho}|\gg R\), while the target is \(\sqrt R\).
Thus fixed-residue absolute resonance averaging cannot close the top core.
The result is not a signed lower bound; cancellation across the two
character residue classes and across \(h\) remains open.

### Round 57: exact adjacent-odd pairing obstruction

For a length-\(R\) product window and \(R/4<h\le R/2\), the odd
denominators in one row number at most two. When two occur they are
\(q,q+2\), and their exact contribution is

$$
 \chi_4(q)e(\sqrt{Xhq})
 \left\{\mathcal A_X(h,q)-
 \mathcal A_X(h,q+2)e(\Theta_h(q))\right\},
 \qquad
 \Theta_h(q)={2\sqrt{Xh}\over\sqrt{q+2}+\sqrt q}.
$$

One-point rows remain full unmatched terms. The smooth part of
\(\mathcal A_X(h,q+2)-\mathcal A_X(h,q)\) totals \(O(1)\), but
\(1-e(\Theta_h(q))\) need not be small and profile/star seams remain.
Moreover, an infinite fourth-power family contains a strict top-profile
window with \(\gg R\) unmatched rows, each of amplitude at least
\(1/2\). Hence every closure taking absolute values after adjacent
pairing retains \(R\) capacity, while the target is \(\sqrt R\).

This does not disprove signed cancellation. The remaining high-shell
kernel is the complete signed matched-plus-unmatched cross-\(h\)
hyperbola-floor sum. The lower shell and alpha transfer remain separate.

### Round 58: exact floor/Fourier reduction and endpoint residual

For \(Y=R^2\asymp\sqrt X\), a length-\(R\) product window
\(J=[A,B]\), and \(R/4<h\le R/2\), set

\[
 L_h={A+h-1\over2h},\qquad U_h={B+h\over2h},\qquad
 q_h=2\lfloor L_h\rfloor+1,
\]

\[
 \nu_h=\lfloor U_h\rfloor-\lfloor L_h\rfloor\in\{0,1,2\}.
\]

Then, with the actual starred amplitude,

\[
 P_J=\sum_h(-1)^{\lfloor L_h\rfloor}
 \left\{I_1(\nu_h)F_h(q_h)-I_2(\nu_h)F_h(q_h+2)\right\},
\]

where \(I_1(v)=v(3-v)/2\) and \(I_2(v)=v(v-1)/2\). This is exact at
both artificial window edges and at every inherited equality star.

The floor-compatible sawtooth separates the character zero mode from the
geometric selector mode \(\ell/(2h)\). For every endpoint argument
\(t_h=(N+ch)/(dh)\), the divisor-incidence estimate

\[
 \#\{h:\|t_h\|\le\delta\}
 \ll_\varepsilon X^\varepsilon(\delta R+1)
\]

implies

\[
 \sum_h\kappa_T(t_h)
 \ll_\varepsilon X^\varepsilon(R/T+1).
\]

Consequently \(T=\lceil\sqrt R\rceil\) makes the entire endpoint and
integer-jump Vaaler residual target-sized. The finite core is precisely

\[
 \sum_{n=A}^{B}e(\sqrt{Xn})
 \sum_{\substack{h\mid n,\ R/4<h\le R/2\\ n/h\ \mathrm{odd}}}
 \chi_4(n/h)\widetilde{\mathcal A}_X(h,n/h).
\]

Every fixed-floor branch and fixed-denominator fibre is too short for a
separate derivative estimate, while taking absolute values retains \(R\)
capacity. The required bound is \(X^\varepsilon\sqrt R\). Thus the
endpoint approximation is closed, but the genuinely signed short
twisted-divisor theorem remains open.

### Round 59: exact quadratic completion and symbol self-return

The divisor-character incidence has the pointwise Fourier projector

\[
 \mathbf1_{h\mid n}\chi_4(n/h)
 =-{i\over2h}\sum_{a\bmod4h}\chi_4(a)e(an/(4h)).
\]

On a smooth interior radial piece, set \(r=4hk-a\) after Poisson
summation in \(n\). The saddle data are

\[
 n_*={4Xh^2\over r^2},\qquad
 f(n_*)-kn_*={Xh\over r},\qquad
 f''(n_*)=-{r^3\over32Xh^3},
\]

and the complete leading coefficient is

\[
 2\sqrt2\,e(1/8)\chi_4(r)
 {X^{1/2}h^{1/2}\over r^{3/2}}.
\]

Moreover \(2h\sqrt{X/n_*}=r\), so the transformed amplitude is exactly

\[
 \sum_j\mathbf1_{h\le H_j}\Phi(h/(H_j+1))[w_j(r)]^*.
\]

The completion therefore restores, rather than smooths away, every actual
M1 profile, height floor, hard endpoint, and equality star. At the critical
scales the coefficient is \(R^{-1/2}\), but a length-\(R\) window gives
an \(R\times R\) raw strip. The missing theorem is a signed raw
\(O_\varepsilon(RX^\varepsilon)\) estimate together with a uniform
hard-symbol B-process ledger.

For \(r=4Kh+s\), the exact reciprocal Hessian satisfies

\[
 \det\nabla^2{Xh\over4Kh+s}=-{X^2\over r^4}\asymp-1,
\]

with opposite order-one eigenvalues. This does not prove lattice
cancellation: \(e(uv)=1\) on \(\mathbb Z^2\) despite Hessian determinant
\(-1\). The next admissible shortcut is instead to test whether the full
fixed-relative-width critical radial sector, unlike the short strip, is
already covered by the proved terminal-frequency divisor theorem.

### Round 60: smooth critical radial terminal theorem

Let \(R=X^{1/4}\), \(Y=\sqrt X\), and let
\(V\in C_c^\infty((c,C))\), \(0<c<C<16\). Define

\[
 \mathcal G_V(X)=\sum_{n\le16Y}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn}).
\]

The stationary relation \(n=4Xh^2/d^2\) forces every supported primal
frequency into \(h\asymp H_j\), with the exact upper owner
\(h\le H_j\). Mellin inversion gives

\[
 u_{j,t}(h)=\eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}h^{2it},
 \qquad a_{j,t}(d)=\chi_4(d)w_j(d)d^{-2it},
\]

where

\[
 \|u_{j,t}\|_\infty+\sum_h|\Delta u_{j,t}(h)|
 \ll_V{1+|t|\over H_j},\qquad |a_{j,t}(d)|\le1.
\]

The accepted terminal theorem bounds the summed positive antecedent by
\(O_{\varepsilon,V}(RX^\varepsilon)\). At the accepted stationary
denominator \(d_*=2\sqrt{hX/q}\),

\[
 (4X/Y)^{it}h^{2it}d_*^{-2it}=(hq/Y)^{it},
\]

so the unpaired interior/top transforms give exactly

\[
 \sum_j\mathcal B_{j,V}
 ={e(1/8)\over i}R\mathcal G_V(X)+O_V(\log^2X).
\]

The hard-top cotangent term is \(O_V(1)\), and floors, profiles, hard
samples, and equality stars retain their accepted ownership. Therefore

\[
 \boxed{|\mathcal G_V(X)|\ll_{\varepsilon,V}X^\varepsilon.}
\]

Pairing frequency signs recovers the real GAR projection with external
factor \(-4R/\pi\). This theorem covers fixed smooth critical sectors,
not the endpoint \(n=16Y\), sharp windows, or \(n/Y\to0\).

### Round 61: exact lower-radial phase diagram

For a smooth block \(n\asymp N=X^\nu\), write
\(d\asymp D=X^\delta\) and \(h\asymp L=X^\ell\). The stationary
identity \(n=4Xh^2/d^2\) gives
\[
 \ell=\delta+\frac{\nu-1}{2},\qquad
 \frac{1-\nu}{2}\leq\delta\leq\frac12.
\]
The accepted TTY wedge becomes \(1816\delta+89\nu\leq552\). It first
meets active support at
\[
 (\nu,\delta,\ell)=
 \left(\frac{356}{819},\frac{463}{1638},0\right),
\]
but closes only a low-denominator prefix. The terminal line is exactly
\(\nu=1/2\), and V2 is exactly \((\nu,\delta)=(0,1/2)\). Hence only
\(\nu=0,1/2\) are closed at every active denominator scale by the
current menu.

For every \(0<\nu<1/2\), the hard-top block
\[
 (\delta,\ell)=\left(\frac12,\frac{\nu}{2}\right)
\]
survives. On a residual block, the exact excess above \(X^{1/4}\) for
the best accepted estimate is
\[
 \min\left\{
 \frac{1-2\nu}{4},\
 \frac{1816\delta+89\nu-552}{2564},\
 \delta-\frac14,\
 \frac{\nu}{4}
 \right\}.
\]
At the hard top it is
\(\min\{\nu/4,(1-2\nu)/4\}\), crossing at \(\nu=1/3\). This diagram
proves no new cancellation estimate; it identifies the exact
lower-radial target.

### Round 62: subcritical small-angle collapse

Put \(Y=\sqrt X\), \(y=\lfloor\sqrt X\rfloor\), and
\(d_{n,h}=2h\sqrt{X/n}\).  The exact floor-perturbed angular multiplier
satisfies

\[
 \Omega_X^*(n,h)=\mathbf1_{d_{n,h}\le y}^{*}
 +O\!\left(\min\{1,n/Y\}\right).
\]

The proof retains \(H_j+1\), every active cutoff, the inactive-bottom
owner, the hard top, and the single stationary star.  On every fixed
subcritical block \(n\asymp N=X^\nu\), \(0<\nu<1/2\), parity removes
the floor perturbation and equality case, giving exactly

\[
 \mathcal D(n)=
 \sum_{\substack{hq=n\\q\ \mathrm{odd}\\q>4h}}\chi_4(q)
 =\sum_{\substack{q\mid n\\q\ \mathrm{odd}\\q>2\sqrt n}}\chi_4(q).
\]

For fixed smooth \(V\), the total normalized replacement error is

\[
 \sum_n |V(n/N)|n^{-3/4}
 |\mathcal C_X^*(n)-\mathcal D(n)|
 \ll_V \frac{N^{5/4}\log(2N)}{Y}.
\]

This is power-saving for \(\nu<2/5\) and only logarithmic, hence
\(X^\varepsilon\)-safe, at \(\nu=2/5\).  The exact remaining target is

\[
 \sum_nV(n/N)\mathcal D(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,V}X^\varepsilon.
\]

That signed estimate is open.  Prime coefficients give polynomial
absolute mass, and the asymmetric cutoff prevents replacement by
\(r_2(n)/4\).  The collapse is therefore a proved reduction, not a
lower-radial bound or an exponent improvement.

### Round 63: exact Appell completion and reciprocal character return

The exact one-sided coefficient has generating series

\[
 \mathscr F(z)=\sum_{n\geq1}\mathcal D(n)z^n
 =\sum_{h\geq1}\frac{z^{4h^2+h}}{1+z^{2h}}.
\]

With \(z=e^{\pi i\tau}\), direct bilateral pairing gives the exact
level-four Appell identity

\[
 K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)=\frac12+2\mathscr F(z).
\]

The completed moving section has four theta--Mordell correction terms.
The holomorphic part is not an ordinary modular theta, and the standard
double-cone series is unavailable at this section because its middle
modulus equals one.

For compactly supported smooth \(w\), character Poisson summation also
gives the exact identity

\[
 \sum_{h\geq1}\sum_{k\geq1}\chi_4(k)w(4h^2+hk)
 =\frac12\sum_{h\geq1}w(4h^2)
 +\frac{i}{2}\sum_{h\geq1}\sum_{j\ne0}\chi_4(j)
 \left\{\frac1h\int_{4h^2}^{\infty}w(u)e\!\left(-\frac{ju}{4h}\right)du
 -\frac{2w(4h^2)}{\pi i j}\right\}.
\]

For \(w(u)=V(u/N)u^{-3/4}e(\sqrt{Xu})\), the positive-\(j\)
interior saddle is

\[
 \frac{2X^{-1/4}}h\chi_4(j)
 V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j-1/8).
\]

The half-boundary is target-safe. The reciprocal signed cone, its
stationary entry and exit, and the exact periodized Appell pairing remain
open. Absolute Fourier or stationary summation retains polynomial
capacity, so these identities prove no subcritical radial bound and no
new discrepancy exponent.

### Round 64: exact reciprocal product wavelet

Fix \(\Xi\in C_c^\infty((0,1))\) and put \(T=\sqrt{X/N}\),
\(g(t)=\mathbf1_{t>0}V(t^2)/t\), \(K=\widehat g\). Poisson summation
in the reciprocal frequency gives

\[
 \sum_{h,j\ge1}\frac{\chi_4(j)\Xi(j/\sqrt X)}h
 V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j)
 =\sum_{n\ge1}A_{X,\Xi}(n)K\!\left(\frac{n-X}{2T}\right)
 +O_B(X^{-B}),
\]

where

\[
 A_{X,\Xi}(n)=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X).
\]

All continuous moments of \(K\) vanish. Moreover, once \(2T\) exceeds
the support radius of \(g\), Poisson summation proves the exact sampled
identities

\[
 \sum_{n\in\mathbb Z}(n-X)^rK((n-X)/(2T))=0
 \qquad(r\ge0).
\]

These cancellations remove polynomial main terms, not the atomic moving
divisor coefficient. Exact products survive through
\(K(0)A_{X,\Xi}(X)\), and inverse Poisson returns exactly to the original
reciprocal cone. The absolute bound is \(TX^\varepsilon\); reaching the
required \(X^{1/4+\varepsilon}\) needs
\(X^{1/4-\nu/2}=H/L\), including \(X^{1/20}\) at \(\nu=2/5\).
The corresponding signed short-product discrepancy and the omitted sharp
saddle/full-cone pieces remain open.

### Round 65: affine Abel form and the unmatched crossing functional

Extend the Round-64 coefficient by zero to nonpositive integers and put

\[
 c_X=\sum_j\frac{\chi_4(j)}j\Xi(j/\sqrt X),\qquad
 D(n)-D(n-1)=A_{X,\Xi}(n)-c_X,qquad D(\lfloor X\rfloor)=0.
\]

The sampled zero mode gives the exact identity

\[
 \sum_nA_{X,\Xi}(n)W_n
 =\sum_nD(n)(W_n-W_{n+1}),
 \qquad W_n=K((n-X)/(2T)).
\]

Period-four Abel summation gives (c_X\ll X^{-1/2}). For an integral
positive displacement shorter than every supported denominator,

\[
 D(n_0+v)=\sum_r\Xi((4r+1)/\sqrt X)
 \{C_{4r+1}(v)-C_{4r+3}(v)\}
 +O_\Xi(1+v/\sqrt X),
\]

where (C_j(v)) indicates a multiple of (j) in
((n_0,n_0+v]). Thus character pairing removes matched rows but leaves
an exact signed unmatched-row correlation. Its wavelet-weighted
(X^{1/4+\varepsilon}) bound is the weakest current sufficient local
claim. No such bound is proved; at (\nu=2/5) it requires the remaining
(X^{1/20}=H/L) gain.

### Round 66: reciprocal Fourier transition and capacity

The floor-compatible Vaaler expansion of the Round-65 discrepancy has
main modes

\[
 \sum_j\chi_4(j)\Xi(j/J)e(kn_0/j)\{1-e(kv/j)\}
\]

with coefficient (O(1/|k|)). The exact wavelet average localizes
(k\asymp J/T=X^{\nu/2}). Hence an exponent pair
((\kappa,\lambda)) yields (J^\lambda(J/T)^\kappa), not an extra
independent (T/J) saving. At \(\nu=2/5\), all audited one-variable
bounds are worse than the original (X^{3/10+\varepsilon}) product
capacity. The Fejer residual is (O(X^\varepsilon(1+J/K))). The next
open interface is a joint signed (j,k) off-diagonal theorem with an
exactly target-sized diagonal.

### Round 67: target-diagonal reciprocal energy

For \(J=X^{1/2}\), \(Q=J/T\), and
\(a_j=\chi_4(j)\Xi(j/J)\), the accepted reciprocal modes reduce by
weighted Cauchy to

\[
 \mathcal E=\sum_k w(k/Q)\left|\sum_j a_je(kX/j)\right|^2.
\]

Poisson summation gives an exact diagonal \(\asymp QJ\) and signed
off-diagonal

\[
 Q\sum_{j_1\ne j_2}a_{j_1}\overline{a_{j_2}}
 \sum_m\widehat w\!\left(Q[m-X(1/j_1-1/j_2)]\right),
\]

with \(\chi_4(j_1)\chi_4(j_2)=(-1)^{(j_2-j_1)/2}\). The accepted
fixed-interior B-process is equivalent to a shifted square-root-product
second moment of target size \(Q^2X^\varepsilon\). Its diagonal is
already \(\asymp Q^2\). The complete signed off-diagonal remains open;
reciprocal spacing and termwise character pairing do not prove it. Thus
Round 67 is a proved reduction only and changes no exponent.

### Round 68: actual ratio symbol and exact energy self-return

The fixed-interior square-root-product row has the exact form

\[
 P_k=\sum_{q\ \mathrm{odd}}\chi_4(q)C(k/q)e(\sqrt{Xkq}),
 \qquad C(y)=y^{3/4}\Xi(2\sqrt y),
\]

with bounded logarithmic symbol seminorms and a Schwartz Mellin
transform. Expanding the energy and setting \(q_1=q+2d\), the character
product is \((-1)^d\). Stationary Poisson in \(d\) produces odd \(j\),
the saddle \(q_1^*=4Xk/j^2\), and phase

\[
 \left(\sqrt{Xk/j}-{1\over2}\sqrt{jq}\right)^2.
\]

A second stationary transform on the odd \(q\)-lattice produces odd
\(s\), saddle \(q^*=4Xk/s^2\), and phase
\(Xk(1/j-1/s)\). The stationary amplitudes multiply to \(k/J\), the
Gaussian units cancel, and the half-density restores
\((-1)^{(j-s)/2}=\chi_4(j)\chi_4(s)\). Therefore the complete
stationary main is exactly \((k/J)|S_k|^2\).

This is a proved fixed-interior stationary-main reduction, not a bound.
The signed union of difference shells and the aggregate nonstationary,
transition, and endpoint errors are open. No exponent changes.

### Round 69: direct Poisson gain and product-wavelet return

For the direct fixed-interior form

\[
 \mathcal T_Q=\sum_{k,q\ \mathrm{odd}}
 \chi_4(q)\beta(k/Q)C(k/q)e(\sqrt{Xkq}),
\]

the antecedent normalization is
(\mathcal B_{\mathrm{main}}=\mathfrak u\sqrt JQ^{-3/2}\mathcal T_Q).
Direct ordinary Poisson in (k), character Poisson in (q), and the
uniform angular stationary expansion return a signed central product
wavelet of length (T=J/Q), with leading scale
(Q^{3/2}J^{-1/2}). Every stationary correction remains Schwartz in the
product displacement, so

\[
 \mathcal T_Q\ll
 Q^{3/2}J^{-1/2}(1+J/Q)X^\varepsilon.
\]

At \(Q=X^{1/5}\), this proves \(X^{7/20+\varepsilon}\). The required
\(X^{3/10+\varepsilon}\) is equivalent to a signed product-wavelet bound
of size (J^{1/2}X^\varepsilon), still missing (X^{1/20}). The full
Hessian determinant is zero, perfect-power fibres are subtarget, and no
audited source theorem supplies the missing fixed-centre saving.

## 12. Do-not-claim boundary

At the present state:

- The Gauss circle conjectural exponent is not proved.
- No new unconditional Gauss circle exponent is proved.
- M9, M9-M1, and M9-M2 are open.
- H4 is a validated external dependency; this does not prove M9.
- Exact $N=0$ control does not imply control of near collisions.
- Computations and finite enumerations are diagnostic only.
- Structural similarity to Li--Yang or Bombieri--Iwaniec sums is not theorem applicability.

## Evidence base

This draft is consolidated from:

- `state/proof_obligations.yml` — authoritative accepted claim graph.
- `manifests/reading_packet.md` — compact state after formal Round 8.
- `rounds/web-research-test/round_027/judge/judge-027.md` — stabilized H4/R5/M9 normalization.
- `rounds/obligation-main/round_007/judge/judge-007.md` — exact-resonance module.
- `rounds/obligation-main/round_008/judge/judge-008.md` — latest applied strategy and interval-URES infrastructure.
- `rounds/codex-managed/m9-unit-frequency-w1-validation/synthesis.md` — validated W-1 obstruction, Vaaler source audit, and $X^{1/3}$ crossover.
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md` — exact top M1 transform, combined piecewise cone, and rejection of cross-cone cancellation.
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md` — terminal M1 divisor estimate, certified TTY wedge, and exact residual direct-method corridor.
- `rounds/codex-managed/m9-m1-near-product-character-kernel/synthesis.md` — exact two-sided near-product kernel and capacity obstructions to fiberwise closure.
- `rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md` — target-sized half-lattice centering, exact disjoint offset fibers, and rejection of naive reflection cancellation.
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/synthesis.md` — exact half-integral resonance cells, their optimal elementary capacity, and the dual RCS interface.
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md` — exact global angular recombination, the weaker GAR interface, and the Hardy-return obstruction.
- `rounds/codex-managed/m9-m1-angular-mellin-separation/synthesis.md` — exact double-Mellin modes, centered functional equation, and angular-reflection return map.
- `rounds/codex-managed/m9-m1-reflected-mode-correlation/synthesis.md` — exact finite-height reflection, crossed residues, Perron completion law, and maximal angular-sign kernel.
- `rounds/codex-managed/m9-m1-local-reflection-eigenspaces/synthesis.md` — exact (2)-adic reflection cocycle, matching profile projection, axial-pole obstruction, and conditional high-(2)-adic tail.
- `rounds/codex-managed/m9-m1-post-residue-kernel-formalization/synthesis.md` — direct scalar Perron/BV bound and the obstruction replacing the post-FE scalar kernel by a vector Hankel operator.
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md` — exact finite vector kernel, residue/horizontal-side ledger, and swept archimedean transition diagram.
- `rounds/codex-managed/m9-m1-diagonal-transition-exhaustion/synthesis.md` — exact diagonal transition normal forms and scoped absolute nested-exhaustion obstruction.
- `rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md` — exact endpoint subtraction, artificial-pole ledger, renormalized side removal, and explicit boundary operator.
- `rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md` — exact finite endpoint Cauchy return, target-safe lower endpoint, and dephased upper-prefix obstruction.
- `rounds/codex-managed/m9-m1-upper-endpoint-character-abel/synthesis.md` — fixed-scale sampled BV, period-four character Abel summation, and the target-safe physical upper endpoint.
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md` — exact physical return and target-sized character-Abel bound for the recombined $R_1$ arithmetic residue.
- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/synthesis.md` — exact moving level-four Appell identification, four-term completion ledger, and boundary-explicit reciprocal character-Poisson return.
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md` — exact local product wavelet, sampled polynomial annihilation, inverse-Poisson self-return, and the precise remaining (H/L) deficit.
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md` — corrected all-integer Abel reduction, exact unmatched period-four crossing functional, and the persistent H/L deficit.
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md` — exact reciprocal-mode transition, Fejer residual count, and no-go for one-variable exponent-pair closure.
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/synthesis.md` — exact target-diagonal reciprocal energy and its square-root-product reduction.
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/synthesis.md` — exact actual ratio symbol, two-step stationary involution, and the remaining signed shell union.
- `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/synthesis.md` — strict direct (X^{7/20}) bound, coefficient-preserving product-wavelet return, and the remaining (X^{1/20}) deficit.
- `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/synthesis.md` — exact finite mixed-factor reduction, residue correction, and scoped no-go for side-free shifts and coefficientwise Abel closure.
- `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md` — exact beta-mask Cauchy--Green connector, corrected (q^0) stationary normalization, and finite character Dirichlet-kernel interface.
- `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md` — hierarchical recombination, corrected post-endpoint (q^{-1}) normalization, scoped signed hard-top (q^{-2}) gain, and the uniform-patching interface.
- `rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/synthesis.md` — exact two-saddle Fresnel geometry, finite-height logarithmic obstruction, and outside-(v)-side reconciliation target.
- `rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/synthesis.md` — exact side orientation, rejection of side cancellation, signed finite-box Plemelj limit, and the distribution-first logarithmic two-saddle kernel.
- `rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/synthesis.md` — sharp moving-logarithm Fresnel estimate, exact finite-section Plemelj decomposition, local q^(-4) height-face control, and the remaining complete-symbol BV interface.
- `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md` — physical-height finite-section BV lemma, separated regular R1 local q^(-2), cutoff-derivative cancellation, and the common recombined-kernel survivor.
- `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md` — boundary-first contour architecture, all-order rho cancellation, rejection of a type-wrong all-strata symbol, and the endpoint/axial compatibility plus reduced-terminal targets.
- `rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/synthesis.md` — finite masked endpoint identity, global three-mask endpoint recombination, local zero rho defect, and the connector-completed axial-vector survivor.
- `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md` — complete finite sixteen-stratum product-Cauchy--Green ledger, actual pre-limit application, and the two module-limit commutators.
- `rounds/codex-managed/m9-m1-beta-axial-side-exhaustion/synthesis.md` — exact compact-support annihilation of every transferred radial-side stratum and closure of the side commutator.
- `rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md` — exact aggregate finite routing of the endpoint and recombined \(R_1\) physical module, and isolation of the endpoint-free remainder limit.
- `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md` — exact large-alpha product-cell factorization, hybrid signed-diagonal/off-diagonal norm, exact Morse passage, and the target-sized complete large-alpha beta package.
- `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/synthesis.md` — exact subordinate complement partition and the corrected global nonsaddle signed-section interface.
- `sources/banerjee_khurana_2023.md` and `sources/kiral_zhou_2016.md` — scoped primary-source audits for twisted-divisor Voronoi architecture.
- `sources/popov_2024_voronoi_gauss.md` — audited truncated Voronoi formula and normalization.
- `state/last_validation_report.md` — latest accepted state-patch report.
- rounds/codex-managed/m9-m1-critical-radial-terminal-return/synthesis.md — target-sized modulus theorem for fixed smooth critical radial sectors.
- rounds/codex-managed/m9-m1-lower-radial-phase-diagram/synthesis.md — exact lower-radial coverage map, hard-top survivor, and best-current saving ledger.
- rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md — exact subcritical symbol collapse, one-sided divisor coefficient, and inclusive two-fifths replacement threshold.
## Round 70 accepted reduction

For the fixed-interior signed product wavelet with
\(J=X^{1/2}\), \(T=J/Q\), exact offset Poisson localizes the circle
variable to \(\|\alpha\|\asymp T^{-1}\). A Farey dissection at the
natural order \(R=Q<T\) therefore has only its \(0/1\) cell and is an
exact Fourier self-return.

At conductor order \(J\), every nonzero contributing fraction has
\(T\ll c\ll J\) and numerator length \(A_c\asymp c/T\). Since
\(c\leq J<T^2\), one has \(A_c<\sqrt c\). The complete local residue
is ordinary Kloosterman for odd \(c\) and conductor-\(4\) twisted for
even \(c\), only after counterfactual completion. The double zero
vanishes, while axial modes and gcd factors remain.

Consequently termwise completion plus Weil and standard complete-sum
Kuznetsov do not prove the target. The first open estimate is a joint
short-numerator/modulus/dual-frequency bound saving
\(T/J^{1/2}=X^{1/20}\). This accepted reduction is fixed-interior and
does not change the final exponent.

## Round 71 accepted low-conductor refinement

For the exact order-(J) Farey representation, retain both offset
aliases, the real center, the neighbor-dependent cell endpoints, every
odd/even local factor, and the surviving axes.  On (c\asymp C), the
scaling

\[
 x=Ju,\qquad y=Jv,\qquad \tau=\beta J^2,
 \qquad \tau=(J/c)z
\]

turns the beta--space phase into

\[
 \frac Jc\left\{z(uv-1)-\rho u-\frac{c}{[c,4]}\sigma v\right\}.
\]

The compatible nonaxial saddle is nondegenerate.  The (d\tau)
measure and three-dimensional stationary phase contribute
((c/J)^{1/2}), including a uniformly bounded incomplete-Fresnel
factor at a Farey edge.  The nonstationary dual tails are summable, and
both surviving axes have no triple critical point.  Thus

\[
 \mathcal D_C
 \ll_\varepsilon X^\varepsilon\frac{C^{3/2}}{\sqrt J}.
\]

Every block (T\leq C\leq J^{2/3}), equivalently
(X^{3/10}\leq C\leq X^{1/3}), is therefore target-safe.  The
remaining order-(J) conductor range is (J^{2/3}<C\leq J).

For the odd nonaxial stationary main, reciprocity gives a
linear-plus-inverse reciprocal-square phase.  Poisson summation in the
long conductor followed by the matching (B)-process in the resulting
Kloosterman index returns exactly to that phase with adjoint amplitude.
Accordingly this one-variable transform loop is an accepted
self-return, not an upper-conductor estimate.  Current spectral and
bilinear source theorems do not accept the complete actual weight and
level-four/axial ledger.  The fixed-interior wavelet, (M9\!-!M1),
and the final exponent remain open.

Accepted evidence:

- `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/conductor_farey_stationary_low_conductor.md`;
- `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/blind_short_numerator_large_sieve.md`;
- `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/short_numerator_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reviews/conductor_round71_adjudication.md`;
- `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/synthesis.md`.

## Round 72 accepted third-derivative conductor extension

Let \(Q=J^{2/5}\), \(T=J/Q\), and \(b\asymp C/T\).  For every exact
nonaxial local class, fixing \(c\bmod4b\) freezes the arithmetic unit and
leaves phase

\[
 e\!\left(\pm A_{\kappa,b}/c\right),
 \qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\kappa\rho\sigma/b}\right)^2,
 \qquad \kappa\in\{1/4,1/2,1\}.
\]

The exact Farey-neighbor numerators partition a fixed-\(b\) row into
\(O(Q)\) pieces.  On every piece the complete normalized stationary symbol,
including incomplete-Fresnel entry and exit, has
\(O_\varepsilon(X^\varepsilon)\) sup plus sampled variation.  In the
progression variable,

\[
 |f'''|\asymp J^2/T^4=Q^{-1}.
\]

The weighted third-derivative estimate and piecewise Cauchy summation give

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \{CQ^{-1/6}+C^{1/2}Q^{2/3}+Q\}
 \ll_\varepsilon X^\varepsilon CQ^{-1/6}.
\]

Consequently

\[
 \sum_{b\asymp C/T}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon\frac{C^3}{TQ^{1/3}},
\]

which is at most \(J^2/T\) exactly for
\(C\leq J^{32/45}=X^{16/45}\).  The two axes are
\(O_\varepsilon(X^\varepsilon C^2/J)\); endpoints, gcds, dual tails,
stationary errors, both orientations, and all three parity classes are
retained.

Combining Rounds 71 and 72, every exact fixed-interior order-\(J\) Farey
block \(T\leq C\leq J^{32/45}\) is target-safe.  The range
\(J^{32/45}<C\leq J\), cone edges, full \(M9\!-\!M1\), \(M9\!-\!M2\),
\(M9\), and the global exponent remain open.

Accepted evidence:

- `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_reciprocal_energy_attack.md`;
- `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_third_derivative_seam_review.md`;
- `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reviews/conductor_round72_adjudication.md`;
- `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/synthesis.md`.

## Round 73 accepted residual off-diagonal reduction

For (J^{32/45}<C\leq J), retain the exact half-open one-count cell set
\(\mathcal Z_b\), every local unit, both Farey-neighbor transitions, and
all finite ownership conventions.  Writing

\[
 c_{b,z}=r+4b\ell,
 \qquad
 a_{b,z}=u_{b,r,k}^{(\kappa)}w_{b,r,\nu,k}^{(\kappa)}(\ell),
\]

the exact energy splits as

\[
 \mathcal E_{C,k}^{(\kappa)}
 =\mathcal D_{C,k}^{(\kappa)}
 +\mathfrak H_{C,k}^{(\kappa)}.
\]

The diagonal satisfies

\[
 \mathcal D_{C,k}^{(\kappa)}
 =\sum_b\sum_z|a_{b,z}|^2
 \ll_\varepsilon X^\varepsilon\frac{C^2}{T}
 \leq X^\varepsilon\frac{J^2}{T}.
\]

The same absolute capacity holds for each fixed nonzero denominator-offset
layer.  Thus the complete residual nonaxial problem is exactly the coherent
signed estimate

\[
 \mathfrak H_{C,k}^{(\kappa)}
 =\sum_b\sum_{z\ne z'}a_{b,z}\overline{a_{b,z'}}
 e\!\left(\pm A_{\kappa,b}
 (c_{b,z}^{-1}-c_{b,z'}^{-1})\right)
 \ll_\varepsilon X^\varepsilon\frac{J^2}{T}.
\]

One further (A)-process, continuous Hessian nondegeneracy, cellwise
Bourgain exponent-pair input, and the ideal phase-matched
Kuznetsov--Voronoi chain do not prove this bound.  The last chain returns to
a length-(T), centre-(X), level-four short coefficient sum and preserves
the exact (X^{1/20}) deficit.  Consequently the accepted conductor
endpoint remains (C=J^{32/45}=X^{16/45}), and the global exponent is
unchanged.

Accepted evidence:

- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_residue_energy_attack.md`;
- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/blind_hybrid_energy_rederivation.md`;
- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_spectral_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reviews/conductor_round73_adjudication.md`;
- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/synthesis.md`.

## Round 74 accepted top-\(M2\) row-correlation reduction

For the exact top-endpoint affine cone, put
\(b_h=\lceil h/4\rceil\) and retain the actual normalized symbol
\(a(h,m)\).  For every fixed \(K_0\geq1\), outer \(h\)-Cauchy gives

\[
 |\mathcal T_L^{\rm end}|^2
 \ll L\{D+\mathcal C_{\ne}\},
 \qquad D\ll L^2,
\]

and exact one-sided expansion gives

\[
 \mathcal C_{\ne}
 =\mathcal C_{\rm core}+O_{K_0}(L^2),
\]

\[
 \mathcal C_{\rm core}
 =2\Re\sum_h\sum_{k=K_0+1}^{h-b_h}
 \sum_{m=b_h+1}^{h-k-1}
 a(h,m)\overline{a(h,m+k)}
 e\!\left(\sqrt{Xh}(\sqrt m-\sqrt{m+k})\right).
\]

Thus the diagonal, every fixed-width near-diagonal, and every pair
touching either moving endpoint are target-safe.  The upper bound

\[
 \mathcal C_{\rm core}\ll_\varepsilon L^2X^\varepsilon
\]

is sufficient for
\(\mathcal T_L^{\rm end}\ll_\varepsilon L^{3/2}X^\varepsilon\).
It is not necessary: this Cauchy step deletes \(\chi_4(h)\).  The same
argument closes only the epsilon-trivial range
\(L\leq(\log(2+X))^A\), not a polynomial intermediate range.

A character-preserving rank-one Poisson candidate was also isolated.  It
maps the smooth interior to a fixed-centre near-product wavelet supported
on \(|X-jl|\ll\sqrt X/L\), whose required bound is
\(X^{1/4+\varepsilon}\).  Poisson in the uncharactered leg gives a
reciprocal energy with diagonal \(L\sqrt X\), while Poisson in the
character leg returns to the original top \(M2\) reciprocal block.
Because this candidate did not receive a statement-only rederivation in
Round 74, it remains unpromoted pending Round 75.

Kowalski--Robert--Wu Proposition 5 gives no new accepted bound: it is
nontrivial only where the existing two-shift estimate is already no
larger.  The full cone, \(M9\!-\!M2\), \(M9\!-\!M1\), \(M9\), and the
global exponent remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reports/blind_m2_cone_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reports/m2_cone_source_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reviews/conductor_round74_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md.

## Round 75 accepted character-preserving top-\(M2\) energy reduction

Let \(\mathscr H_L\) be the exact finite odd frequency support and retain
the actual top-endpoint symbol \(a(h,m)\).  Regroup the cone by its
uncharactered variable:

\[
 R_m=
 \sum_{\substack{h\in\mathscr H_L\\m\leq h\leq4m}}
 \chi_4(h)a(h,m)e(\sqrt{Xhm}).
\]

The ceiling is exact, so

\[
 \mathcal T_L^{\rm end}=\sum_mR_m,\qquad
 |\mathcal T_L^{\rm end}|^2
 \ll L\mathcal E_L^\top,qquad
 \mathcal E_L^\top=\sum_m|R_m|^2.
\]

The diagonal is \(O(L^2)\).  Writing the second odd index as \(h+2r\)
gives the exact off-diagonal

\[
\begin{aligned}
 \mathcal E_L^\top-\mathcal E_{L,\rm diag}^\top
 ={}&2\Re\sum_{r\geq1}(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a(h,m)\overline{a(h+2r,m)}\\
 &\hspace{23mm}\times
 e\!\left(-\frac{2r\sqrt{Xm}}
 {\sqrt h+\sqrt{h+2r}}\right).
\end{aligned}
\]

Here
\(\chi_4(h)\chi_4(h+2r)=(-1)^r\).  Consequently

\[
 \mathcal E_L^\top\ll_\varepsilon L^2X^\varepsilon
\]

is sufficient for the top-cone target.  Unlike outer \(h\)-Cauchy, this
reduction preserves the character and both hard affine edges.

The Round-74 frozen leading-wavelet formula is not an all-orders
identity.  Quadratic stationary phase has the generally nonzero next
term \(g''(t_0)/(8\pi ixl)\), only \(J^{-1}\) below the leading
normalized symbol on the narrowest collar.  An exact Fresnel or
all-orders moving symbol can repair the representation, but is not an
accepted estimate.

Periodized Parseval gives the reciprocal diagonal \(LJ\).  Its active
modes are \(k=-m<0\), and the high-character B-process returns, at
principal-symbol level, to the same \(R_m\) with factor
\(e(-1/8)\sqrt{J/L}\).  The transform is therefore an adjoint return,
not a new saving.  The alternating offset energy, the polynomial
intermediate \(L\)-range, the full top cone, \(M9\!-\!M2\), \(M9\), and
the global exponent remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/blind_near_product_energy_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/reciprocal_energy_attack.md;
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/near_product_energy_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reviews/conductor_round75_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md.

## Round 76 accepted odd-lift resonance obstruction

In the positive-offset energy, write

\[
 h=ga,\qquad h+2r=gb,\qquad (a,b)=1.
\]

All of \(g,a,b\) are odd.  Put \(q=(b-a)/2\) and

\[
 \beta_{a,b,k}={X(\sqrt b-\sqrt a)^2\over4k},\qquad
 \alpha_{a,b,k}={q\over2}-\beta_{a,b,k}.
\]

At a negative \(m\)-Poisson stationary mode, the exact character-phase
factor is

\[
 (-1)^r e(-g\beta_{a,b,k})
 =(-1)^q e(-g\beta_{a,b,k})=e(g\alpha_{a,b,k}).
\]

Thus the offset character is constant along each primitive odd-lift ray.
Consecutive admissible lifts differ by two, and their ratio is

\[
 e(2\alpha_{a,b,k})
 =e\!\left(-{X(\sqrt b-\sqrt a)^2\over2k}\right).
\]

Consequently a step-two Abel estimate is governed by

\[
 \left\|2\alpha_{a,b,k}\right\|
 =\left\|{X(\sqrt b-\sqrt a)^2\over2k}\right\|,
\]

not by \(\|\alpha_{a,b,k}\|\).  The old criterion misses every
half-integer \(\alpha\) resonance.

This omission occurs with the actual plateau profile.  Let \(X=T^4\),
\(J=T^2\), where \(T\) is odd and divisible by \(13\), and take

\[
 (a,b)=(81,121),\qquad k={2J\over13}.
\]

Then \(x_*/g=169/4\) lies strictly between \(b/4\) and \(a\), while

\[
 \alpha_{81,121,k}=10-{13J\over2}\in\mathbb Z+{1\over2}.
\]

The two actual \(W\)-arguments are \(9/13\) and \(11/13\), so both
weights equal one.  Every odd lift is phase-coherent.  This is a route
falsifier, not a lower bound for the full energy, because the remaining
support weights and cancellation across primitive pairs and reciprocal
modes are not controlled.

A fixed primal collar at the two \(m\)-endpoints has
\(O(L^2X^\varepsilon)\) grouped capacity.  After removing it, real-affine
cutoffs have no ceiling parity and the retained interior is structurally
step two.  If the sharp lower endpoint remains inside the transform, then

\[
 \left\lceil{gb\over4}\right\rceil
 ={gb\over4}+{1\over2}+{\chi_4(gb)\over4}
\]

forces a mod-four split and the conservative resonance \(\|4\alpha\|\).
The larger set belongs only to the sharp endpoint representation.

The lift phase is radial and rank one.  Transforming the reciprocal
variable back restores the original \(-C\sqrt m\) phase with cancelling
Gaussian units and reciprocal Jacobians.  Hence radial Poisson is a
self-return and supplies no independent saving.

The complete collar-extracted centred-integral formula and quantitative
step-two variation asserted by the discovery report remain candidate
evidence pending an independent seam proof.  The corrected resonant union,
the top cone, \(M9\!-!M2\), \(M9\), and the global exponent remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/blind_signed_offset_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/gcd_lift_resonance_attack.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/signed_offset_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reviews/conductor_round76_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/synthesis.md.
