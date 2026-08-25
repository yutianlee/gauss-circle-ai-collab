# Best Conditional Proof Draft

## Scope and status

This document consolidates the accepted proof-obligation graph through
completed Codex-managed Round 162, together with the earlier accepted
infrastructure. It contains an internally proved \(1/3+\epsilon\)
theorem, a narrowly repaired and source-audited external theorem at
exponent \(0.3144831759\ldots\), and the conditional architecture for
the conjectural \(1/4+\epsilon\) target. It is not a proof of the Gauss
circle conjecture.

The strongest theorem proved from the repository's own M1/M2
architecture is

$$
\boxed{P(X)\ll_\epsilon X^{1/3+\epsilon}}
$$

for every real \(X\ge2\). The target-level implication remains

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

Here H1--H3 are proved internally, H4 is an audited external theorem,
R5-Full is now proved internally by the pointwise divisor-product
reconciliation, and M9 is open. Consequently the desired
\(1/4+\epsilon\) bound remains open.

Separately, the completed Li--Yang source audit and independent range
repairs certify the direct external theorem

$$
\boxed{
P(X)\ll_\epsilon X^{\theta_{\rm LY}+\epsilon},\qquad
\theta_{\rm LY}=
\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots .
}
$$

Only the narrow final real-\(X\), inclusive theorem is accepted. The
printed general intermediate ranges are not. This external theorem does
not prove the internal Round-95 cluster estimate, M9-M1, M9-M2, M9, or
the quarter target.

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

**Status: proved internally.**

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
\qquad D=X^\delta,\quad L=X^\ell.
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
\operatorname {Res}_sR_{1,v}(1-s)=+\pi i\sqrt X I_1(0),\qquad
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
 D(n)-D(n-1)=A_{X,\Xi}(n)-c_X,\qquad D(\lfloor X\rfloor)=0.
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
 \ll L\mathcal E_L^\top,\qquad
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

## Round 77 accepted complete actual-symbol interface

Let (1\leq L\leq H\leq J^{1/2}).  In the accepted positive-offset
part of the transposed top-(M2) energy, remove fixed physical collars
at (m=\lceil s/4\rceil) and (m=h).  For the unique primitive
factorisation

\[
 h=ga,\qquad s=gb,\qquad (a,b)=1,
 \qquad a,b,g\ \mathrm{odd},
\]

put

\[
 \delta=\sqrt b-\sqrt a,\qquad
 \Lambda={X\delta^2\over2},\qquad
 \alpha={b-a\over4}-{X\delta^2\over4k}.
\]

For

\[
 {J\delta\over2\sqrt a}<k<{J\delta\over\sqrt b},
\]

retain the complete centred integral

\[
 \mathfrak B_{a,b,k}^{\circ}(g)
 =g\int_{b/4}^{a}A_{ga,gb}^{\circ}(gu)
 e\!\left(g\left[-J\delta\sqrt u+ku
              +{X\delta^2\over4k}\right]\right)du.
\]

With symmetric finite Poisson summation before collar extraction, the
exact aggregate identity is

\[
\begin{aligned}
 \mathcal O_L={}&2\Re
 \sum_{\substack{a<b<4a\\a,b\ \mathrm{odd}\\(a,b)=1}}
 \sum_k e(\alpha)
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B_{a,b,k}^{\circ}(2n+1)e(-n\Lambda/k)\\
 &\quad+O_{M,\eta,\Phi,W}\!\left(L^2\log(2+L)\right).
\end{aligned}
\]

The error owns the two full lattice endpoint samples, both fixed
collars, zero and positive modes, equality modes, and every negative
nonstationary mode.  There is no stationary-expansion error because all
stationary and collar-transition modes remain complete.

The exact symbol factorisation

\[
 A_{ga,gb}(gu)=g^{-3}E_{a,b}(g)P_{a,b}(u),
 \qquad |E'(g)|\ll G^{-1},
\]

retains both exact (W)-arguments and (q_X), which are independent of
(g).  Together with

\[
 -J\delta\sqrt u+ku+{X\delta^2\over4k}
 =k\left(\sqrt u-{J\delta\over2k}\right)^2,
\]

it gives, uniformly through saddle entry and exit,

\[
 |\mathfrak B^\circ(g)|+g|\partial_g\mathfrak B^\circ(g)|
 \ll {J\delta\sqrt G\over k^{3/2}}.
\]

Therefore the endpoint-plus-step-two total variation obeys the same
bound and discrete Abel yields

\[
 \left|\sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ(2n+1)e(-n\Lambda/k)\right|
 \ll {J\delta\sqrt G\over k^{3/2}}
 \min\!\left(N_{a,b},{1\over2\|\Lambda/k\|}\right).
\]

This is an actual-symbol lemma, not a coefficient-uniform theorem.
Alternating adversarial lift coefficients fail its variation hypothesis.
The weighted sum over primitive rays and reciprocal modes is still open,
so the top energy, \(M9\!-\!M2\), and the exponent do not follow.

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/blind_actual_symbol_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/centered_integral_variation_attack.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/actual_symbol_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md.

## Round 78 accepted primitive-square interface

Restrict the accepted Round-77 primitive-ray sum to \(ab=\square\).
Because \((a,b)=1\), write uniquely
\[
a=s^2,\qquad b=t^2,\qquad t=s+2u,\qquad (s,u)=1,
\qquad 1\leq u<s/2.
\]
For an actual odd lift \(g=2n+1\), the exact combined phase is
\[
e(-Xu^2/k)e(-2nXu^2/k)=e(-gXu^2/k),
\]
and the strict reciprocal interval is
\[
\frac{Ju}{s}<k<\frac{2Ju}{t}.
\]

Put \(K=Ju/s\) and
\(B_g(k)=\mathfrak B^\circ_{s^2,t^2,k}(g)\).  The literal complete
smooth-collar coefficient satisfies
\[
\sup_k|B_g(k)|+\operatorname{Var}_kB_g(k)
\ll_\varepsilon X^\varepsilon\sqrt{\frac{gt^2}{K}}.
\]
The proof uses the exact Gaussian multiplier with both physical collars
and all fixed profiles.  A pointwise \(k|B_g'(k)|\) bound at this scale
is false; only the total sampled variation is accepted.

For \(f(k)=-gXu^2/k\),
\[
|f''(k)|\asymp\frac{gt^2}{K}\ll1.
\]
Weighted second-derivative summation gives
\[
\sum_kB_g(k)e(f(k))\ll_\varepsilon(L+1)X^\varepsilon.
\]
Since the number of lifted square triples is \(O(L\log(2+L))\),
\[
\mathcal S_L^\square(X)\ll_\varepsilon L^2X^\varepsilon.
\]

The positive absolute Abel majorant cannot be used:
\[
\mathcal M_L^\square(X)
\asymp_{X^\varepsilon}\sqrt J\,L^{3/2}.
\]
Hence later work must retain signed reciprocal-mode cancellation.
The accepted result removes only exact square/common-squarefree
primitive rays.  The nonsquare resonance union, full top energy,
\(M9\!-\!M2\), \(M9\), and the exponent remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reports/blind_square_resonance_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reports/square_resonance_mass_attack.md;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reports/square_resonance_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reviews/conductor_round78_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/synthesis.md.

## Round 79 accepted nonsquare divisor-strip interface

For primitive odd coprime \(a<b<4a\) with \(ab\) nonsquare, define

\[
 m=\frac{a+b}{2},\qquad q=\frac{b-a}{2},\qquad
 u=\frac{q}{m+\sqrt{m^2-q^2}}.
\]

Then

\[
 \frac{(\sqrt b-\sqrt a)^2}{2}=qu,\qquad
 \Lambda=Xqu,\qquad
 \frac{Ju}{1-u}<k<\frac{2Ju}{1+u}.
\]

On a dyadic block, the metric condition is

\[
 |\Lambda-\ell k|\leq \frac{ck}{R}.
\]

For a fixed ray the integer \(p=\ell k\) lies in an interval of length
\(O(K/R)\), and each \(p\) has \(X^\varepsilon\) divisor
factorizations. Hence

\[
 \mathcal I_{\rm ns}\ll_\varepsilon
 X^\varepsilon\sum_{(a,b)}
 \min\!\left(M_{a,b}(K),1+\frac KR\right)
 \ll_\varepsilon X^\varepsilon\frac{ADK}{R}.
\]

The complete Round-77 coefficient has size

\[
 \mathcal V_{a,b,k}\ll_\varepsilon
 X^\varepsilon\frac{A\sqrt G}{\sqrt{JD}}.
\]

After the Abel weight and standalone Abel-\(1\) term, this proves

\[
 \mathcal A_{\rm ns}\ll_\varepsilon
 X^\varepsilon A\sqrt G\sqrt J D^{3/2}.
\]

Thus all blocks \(AJD^3\ll L^3\) close positively.

Writing \(ab=\mathfrak d r^2\), rational ratios of
\(m-r\sqrt{\mathfrak d}\) force the same primitive ray. At fixed
\(X\), at most one nonsquare ray is exactly resonant, and all of its
divisor modes contribute \(O_\varepsilon(LX^\varepsilon)\).

The factor-\(R\) incidence saving is sharp at ordinary metric density.
Averaging \(X\) on a populated inner cone gives the \(1/R\) population
even after exact equalities are deleted. Therefore the remaining
strict-metric blocks \(AJD^3\gg L^3\) require a signed
complete-coefficient correlation estimate; incidence and algebraic
spacing alone cannot prove it.

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reports/blind_nonsquare_geometry_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reports/nonsquare_reciprocal_incidence_attack.md;
- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reports/nonsquare_resonance_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reviews/conductor_round79_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/synthesis.md.

## Round 80 accepted complete-symbol carrier cancellation

Let

\[
 \theta={X(\sqrt b-\sqrt a)^2\over2k},\qquad
 q={b-a\over2}.
\]

The complete collar-extracted coefficient factors exactly as

\[
 \mathfrak B^\circ_{a,b,k}(g)
 =e(g\theta/2)\mathfrak C^\circ_{a,b,k}(g),
\]

where

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\left[ku-J(\sqrt b-\sqrt a)\sqrt u\right]\right)du.
\]

If \(\theta=\ell+\eta\), \(p=\ell k\), and \(g\) is odd, then

\[
 (-1)^{q+\ell}\mathfrak B^\circ(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^\circ(g).
\]

Thus the quotient sign \((-1)^{p/k}\) cancels against the actual
carrier. For a period-one window

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
\]

the complete-symbol expansion has integer modes

\[
 \mu_R\mathfrak C^\circ(g)
 +\sum_{r\ne0}\widehat W_R(r)e(r\theta)
  \mathfrak C^\circ(g).
\]

The zero-density mode is present. Finally, with \(h=ga\), \(s=gb\),
and \(x=gu\),

\[
 \mathfrak C^\circ(g)
 =\int_{s/4}^{h}A^\circ_{h,s}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx,
\]

and \((-1)^q=\chi_4(h)\chi_4(s)\). This is an exact adjoint return to
the residual transposed two-character energy. It proves a route
obstruction, not the energy estimate. The remaining target is the full
cross-row density--discrepancy kernel on \(AJD^3\gg L^3\).

Accepted evidence:

- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/blind_strict_metric_energy_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/primitive_ray_parity_energy_attack.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/strict_metric_energy_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reviews/conductor_round80_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md.

## Round 81 accepted M1 transition flattening

Let \(J=\sqrt X\), \(Q=J^{2/5}\), \(T=J/Q\), and retain one exact
fixed-smooth-interior order-\(J\) Farey component.  For every alias,
orientation, class \(\kappa\in\{1/4,1/2,1\}\), compatible nonaxial
critical pair, numerator \(b\), and admissible progression
\(c=r\pmod {4b}\), the normalized complete coefficient satisfies

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),
\]

where \(\Gamma\) is the full, oriented half, or zero Gaussian according
as the saddle is inside, on, or outside the limiting Farey interval, and

\[
 \|V\|_\infty+\operatorname {Var}V
 \ll_\varepsilon X^\varepsilon,
 \qquad
 |E(c)|\ll_\varepsilon X^\varepsilon\sqrt{C/J}.
\]

The error contains the exact moving faces, tangential and Morse
corrections, aliases, floors, and neighbor resets.  It is not globally BV.
The audited Bourgain reciprocal exponent pair gives

\[
 \sum_{b\asymp C/T}|S_b|^2
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{C^4\over TJ}\right)
 \le X^\varepsilon{J^2\over T}
\]

for \(C\le J^{13/18}\).  Therefore every fixed-interior conductor
\(T\le C\le J^{13/18}\) is accepted.  The residual
\(J^{13/18}<C\le J\), cone edges, other radial sectors, full
\(M9\!-\!M1\), and every downstream theorem remain open.

Accepted evidence:

- rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reports/blind_transition_flattening_rederivation.md;
- rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reports/farey_transition_flattening_attack.md;
- rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reports/transition_gluing_hostile_audit.md;
- rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reviews/conductor_round81_adjudication.md;
- rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/synthesis.md;
- sources/bourgain_2017_exponent_pair.md.

## Round 152 accepted arithmetic pruning and strict square-root-wave range

At $D=d=L=1$, put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,
\tag{152.1}
$$

and retain the literal zero-extended Round-148 profile
$A_U(\ell)=\mathscr A_{1,M,U}(1,\ell)$ with its actual endpoint
convention.  The accepted Round-151 relation is

$$
 P_U=\sum_{\substack{\ell>0\\\ell\ \mathrm{odd}}}
 \chi_4(\ell)\ell^{-3/4}A_U(\ell)e(\sqrt{N\ell}),
\tag{152.2}
$$

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
\tag{152.3}
$$

where the external row coefficient $B_{1,U}(1)$ remains attached and is
$O_\varepsilon(X^\varepsilon)$.

Let

$$
 k(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad j(\ell)=k(\ell)^2-N\ell,
\tag{152.4}
$$

and write uniquely

$$
 \ell=\tau s^2,
 \qquad \tau\ \mathrm{odd\ and\ squarefree},
 \qquad s\ \mathrm{odd}.
\tag{152.5}
$$

There is no inserted coprimality condition between $\tau$ and $s$.  With
$J=M^{3/4}$ and $S=\lceil M^{1/4}\rceil$, partition the actual support,
in order, as

$$
\begin{aligned}
 \mathcal L_0&=\{j=0\},\\
 \mathcal L_1&=\{0<|j|\le J\},\\
 \mathcal L_2&=\{|j|>J,\ s\ge S\},\\
 \mathcal L_*&=\{|j|>J,\ s<S\}.
\end{aligned}
\tag{152.6}
$$

The nearest integer in (152.4) is unique because a tie would make
$4N\ell$ an odd square.  Write $N=a^2n_0$ with $n_0$ squarefree.  Exact
resonance requires $\tau=n_0$, is present on odd support only when $n_0$
is odd, and has complete actual-weight mass

$$
 |P_{\mathcal L_0}|
 \ll_\varepsilon M^{-1/4}n_0^{-1/2}X^\varepsilon.
\tag{152.7}
$$

For nonzero $j$ define

$$
 \rho_N(j)=\#\{x\bmod N:x^2\equiv j\pmod N\}.
$$

Prime-power analysis, including the two-adic case, gives

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)},
 \qquad
 \sum_{1\le|j|\le J}\rho_N(j)
 \ll_\varepsilon JX^\varepsilon.
\tag{152.8}
$$

The actual $k$ interval has length $O(\sqrt{NM})<N$ because
$M\le R^2\asymp N^{1/2}$.  Thus each root class modulo $N$ gives only
$O(1)$ supported $k$, and fixed $(j,k)$ determines $\ell$.  At
$J=M^{3/4}$ the actual $M^{-3/4}$ weight proves

$$
 |P_{\mathcal L_1}|\ll_\varepsilon X^\varepsilon.
\tag{152.9}
$$

Also

$$
 \sum_{S\le s\ll\sqrt M}\left(1+\frac M{s^2}\right)
 \ll M^{3/4}.
\tag{152.10}
$$

After intersecting this count with $|j|>J$, the third owner is disjoint
and has $|P_{\mathcal L_2}|\ll_\varepsilon X^\varepsilon$.  Hence

$$
 \boxed{P_U=P_U^*+O_\varepsilon(X^\varepsilon),}
\tag{152.11}
$$

where

$$
 P_U^*=\sum_{\substack{\ell=\tau s^2\ \mathrm{retained}\\
 |k(\ell)^2-N\ell|>M^{3/4}\\
 1\le s<\lceil M^{1/4}\rceil}}
 \chi_4(\tau)(\tau s^2)^{-3/4}
 A_U(\tau s^2)e(s\sqrt{N\tau}).
\tag{152.12}
$$

On this survivor $\tau\gg M^{1/2}$.  The $s=1$ odd-squarefree layer
remains, so (152.11) is a strict support reduction and not a bound for
$P_U^*$.

There is also a new source-legal scale range.  Tao--Trudgian--Yang
Lemma 14, Remark 16, and Lemma 15 applied to Bourgain's global pair give

$$
 D(13/84,55/84)=(18/199,593/796).
\tag{152.13}
$$

The maximum in Lemma 14 has no hidden gap, since on
$0\le\alpha\le1/2$ the $D$-line minus its auxiliary line is

$$
 \frac{17-29\alpha}{2388}\ge\frac5{4776}>0.
\tag{152.14}
$$

Remark 16 supplies the symmetry bridge to the upper half.  Applying the
Lemma-13 $B$-process only after this global conclusion gives

$$
 BD(13/84,55/84)=(195/796,235/398).
\tag{152.15}
$$

For a square-root phase an exponent pair $(\kappa,\lambda)$ gives

$$
 |P_U|\ll_\varepsilon
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}X^\varepsilon
\tag{152.16}
$$

after resolving the two residue classes modulo four, applying an
unweighted interval estimate, and inserting the actual BV profile by
Abel summation.  The pair (152.15) therefore yields

$$
 \boxed{
 |P_U|\ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 X^\varepsilon.}
\tag{152.17}
$$

Consequently

$$
 \boxed{M^{449}\gg R^{780}}
\tag{152.18}
$$

is target-safe.  This strictly extends the previous scalar range because

$$
 \frac{780}{449}<\frac{1424}{819},
 \qquad
 \frac{1424}{819}-\frac{780}{449}
 =\frac{556}{367731}>0.
\tag{152.19}
$$

In the source's beta coordinate, the relevant printed line meets the
required line at $\alpha=127/322$, inside its stated Table-1 cell.  Thus
(152.18) is the exact boundary of this audited exponent-pair envelope.

The other tested routes give only scoped no-gain results.  Adjacent odd
pairing retains the full phase difference.  For every legal even shift,

$$
 \chi_4(\ell+2h)\chi_4(\ell)=(-1)^h,
\tag{152.20}
$$

so one $A$-process erases the variable character.  Its exact
second-derivative placement gives no new scale below $M\asymp R^2$.
Mellin inversion has spectral scale $\sqrt{NM}$, root number $+1$, and
unbalanced additive dual length $\sqrt{N/M}$; using its oscillation
reproduces character Poisson and the accepted reciprocal row.  A second
principal $B$-process is the same self-return.  The audited mixed
Burgess, higher-Voronoi, and fixed-parameter nonlinear-twist theorems do
not directly match the literal coefficient, phase, growing parameter,
actual weight, or endpoint class.  None of these statements is a signed
lower bound or a literature-impossibility theorem.

Below $M^{449}\asymp R^{780}$, after the bounded owner is removed, the
first missing estimate is

$$
 |P_U^*|\ll_\varepsilon X^\varepsilon.
\tag{152.21}
$$

The $D>1$ recovery fibre, $L>1$ rows, growing-$M$ generic sector, every
original $t\ge2$ layer, the Round-138 cross owner, remaining M1 and all
M2 owners, endpoint uniformity, M9, bridge, and quarter target remain
open.  The internal global exponent remains $1/3$ and the audited
external exponent remains $(3292+25\sqrt{1717})/13762$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/conductor_round152_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/controls/conductor_round152_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/independent_conductor_round152_math_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/hostile_square_root_pruning_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/source_conductor_round152_final.md;
- sources/tao_trudgian_yang_2025.md;
- sources/bourgain_2017_exponent_pair.md.

## Round 82 accepted M1 residue-offset reduction

Let (J=\sqrt X), (Q=J^{2/5}), (T=J^{3/5}), (B=C/T), and
(J^{13/18}<C\le J^{3/4}).  In the exact transition-flattened smooth
principal row, fixing a residue progression (c=r\pmod{4b}) fixes the
local class, parity, gcd restriction, and exact odd or even local unit.
Thus

\[
 S_b=\sum_{r\in\mathscr R_{\kappa,b}}u(r)R(r),
\]

where

\[
 R(r)=\sum_{\substack{c\asymp C\\c\equiv r\ (4b)}}
 V(c)e\!\left(\pm A_{\kappa,b}/c\right),
 \qquad
 |R(r)|\ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

Expanding the energy in the original row gives

\[
 \sum_{b\asymp B}|S_b|^2
 =\sum_{b,r}|R(r)|^2+
 \sum_b\sum_{r\ne s}u(r)\overline{u(s)}R(r)\overline{R(s)}.
\]

The first term and each one fixed nonzero offset (s-r) are

\[
 \ll_\varepsilon X^\varepsilon B^2T^2Q^{-5/12}
 =X^\varepsilon C^2Q^{-5/12},
\]

which is target-safe for (C\le J^{47/60}).  Hence throughout the first
residual band the only smooth-main survivor is

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_b\sum_{r\ne s}u(r)\overline{u(s)}R(r)\overline{R(s)},
\]

with target

\[
 \mathfrak X_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon J^2/T.
\]

Absolute offset accumulation gives
(X^\varepsilon C^3/(TQ^{5/12})), so no estimate for the survivor or
new conductor range is accepted.  In the odd class, its nonzero-offset
part is exactly the nonzero product-Kloosterman Fourier correlation;
complete Poisson inversion returns to the same residue sum.

Accepted evidence:

- rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/blind_chirped_kloosterman_energy_rederivation.md;
- rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/chirped_residue_energy_attack.md;
- rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reviews/conductor_round82_residue_normalization.md;
- rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reviews/conductor_round82_adjudication.md;
- rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/synthesis.md.

## Round 83 accepted M1 centred dual-difference reduction

Fix one compatible smooth nonaxial component in
\(J^{13/18}<C\le J^{3/4}\). Put \(g_\kappa=4\kappa\),
\(M_\kappa=4b/g_\kappa\), and \(c=g_\kappa x\). The odd and both even
local units have the exact form

\[
 u(g_\kappa x)=\zeta e_{M_\kappa}(K_\kappa\bar x),
 \qquad
 (g_\kappa,M_\kappa,K_\kappa)
 \in\{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\}.
\]

Let

\[
 I_b(n)=\int_{\mathbb R}
 V_{b,gx,k}^{(\kappa)}e\!\left(\pm{A_{\kappa,b}\over gx}\right)
 e\!\left(-{nx\over M}\right)dx.
\]

Exact progression Poisson gives \(M^{-1}\sum_nS(n,K;M)I_b(n)\).
Removing the same-residue offset \(a=0\) exactly once and then splitting
the literal integer difference \(d=0\) yields

\[
 \mathfrak X_C^{(\kappa,k)}
 =\mathfrak Z_C^{(\kappa,k)}+\mathfrak Y_C^{(\kappa,k)},
\]

where

\[
 \mathfrak Y_C^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.                              \tag{83.D1}
\]

Sampled Parseval plus the monotone reciprocal autocorrelation gives

\[
 \sum_n|I_b(n)|^2
 \ll_\varepsilon X^\varepsilon M C/g_\kappa.
\]

Consequently the \(d=0\) slice is target-safe; the purely internal
bound is \(O_\varepsilon(X^\varepsilon B^2C)\), and the standard
complete-sum bound sharpens it to \(O_\varepsilon(X^\varepsilon BC)\).
Nonzero multiples \(d\equiv0\pmod M\) remain in (83.D1).

No estimate for (83.D1), no \(B^{-\delta}\) gain, and no new conductor
range is accepted. Prime-power offset degeneracies preclude a uniform
coefficient-free square-root bound, and complete Fourier transformation
self-returns. The next proof kernel is the actual-weight centred
\(d\ne0\) correlation itself.

Accepted evidence:

- rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reports/inverse_unit_offset_attack.md;
- rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reviews/conductor_round83_dual_normalization.md;
- rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reviews/conductor_round83_adjudication.md;
- rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/synthesis.md.

## Round 84 accepted stationary small-difference interface

In the Round-83 centered correlation, retain only the smooth Round-81
principal coefficient.  For one class put

\[
 g=4\kappa,\qquad M={4b\over g},\qquad
 A=\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2.
\]

The active stationary sign of

\[
 I_b(n)={1\over g}\int V_b(c)
 e\!\left(-{A\over c}-{nc\over4b}\right)dc
\]

has

\[
 c_n=\sqrt{{4bA\over|n|}},\qquad
 \Phi(c_n)=-\eta\left(\sqrt X+{\sqrt{\kappa k}\over b}\right)
 \sqrt{|n|},
\]

Gaussian \(e(-\eta/8)\), and stationary size
\(H=C\sqrt T/J\).  The accepted Round-81 smooth extension and integrated
\(c\)-seminorm give the complete phase-removed entry/exit profile sampled
\(L^\infty+\mathrm{BV}\) norm \(O_\varepsilon(X^\varepsilon H)\).

For every integer \(d\), exact Kloosterman orthogonality gives

\[
 {1\over M^2}\sum_{r\bmod M}
 |S(r+d,K;M)\overline{S(r,K;M)}-c_M(d)|\le2.
\]

On \(n=r+M\ell\asymp Q^2\), the exact square-root difference phase has

\[
 |\Psi''(\ell)|\asymp {M^2|d|\over J}.
\]

Thus, for \(D\le J^{17/30}\),

\[
 \mathfrak Y_{\le D}
 \ll_\varepsilon X^\varepsilon\left(
 C^3J^{-17/10}D^{3/2}
 +C^2TJ^{-3/2}D^{1/2}
 +{DC^2\over T\sqrt{JQ}}
 +{DB^2\over Q^2}\right)
 \ll_\varepsilon X^\varepsilon {J^2\over T}.
\]

This includes both signs, every nonzero modulus multiple in the range,
Ramanujan and gcd modes, entry/exit, and all aggregate errors.  Therefore
the first exact principal survivor is

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{|d|>\lfloor J^{17/30}\rfloor}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

No estimate for this survivor, no whole-range \(B\)-saving, and no new
conductor range is accepted.  Complete stationary summation self-returns,
and prime-power modes prevent a uniform coefficientwise square-root
replacement.

Accepted evidence:

- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reports/stationary_dual_difference_attack.md;
- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reports/dual_difference_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reviews/conductor_round84_stationary_normalization.md;
- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reviews/conductor_round84_adjudication.md;
- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/synthesis.md.

## Round 85 accepted support-edge difference bound

Continue with the smooth Round-81 principal coefficient and the notation
of Round 84. Let \(\mathscr N_b=[N_b^-,N_b^+]\) be its exact active
stationary support, \(\Delta_b=N_b^+-N_b^-\asymp Q^2\), and

\[
 E_*=\lfloor Q^2J^{-1/20}\rfloor=\lfloor J^{3/4}\rfloor.
\]

When \(0\leq\Delta_b-|d|\leq E_*\), the two principal symbols lie at
opposite compact-support endpoints. The accepted normalized derivative
hierarchy through order three gives their product the factor

\[
 \left({\Delta_b-|d|+1\over Q^2}\right)^6.
\]

Exact residue mass therefore yields

\[
 \mathfrak Y_{\rm edge}^{\rm main}
 \ll_\varepsilon X^\varepsilon
 H^2(BE_*+E_*^2)(E_*/Q^2)^6
 \ll_\varepsilon X^\varepsilon J^{13/10},
 \qquad H={C\sqrt T\over J}.
\]

The entry/exit, stationary-remainder, wrong-sign, and nonstationary terms
must be resummed over every integer difference rather than imported from
the small-\(d\) theorem. Their complete contribution is

\[
 \ll_\varepsilon X^\varepsilon(B^2HQ^2+B^3)
 \ll_\varepsilon X^\varepsilon J^{23/20}.
\]

Both powers lie below \(J^2/T=J^{7/5}\). Hence all
\(|d|\geq\Delta_b-E_*\) are target-safe, with both signs, reflected
orientations, modulus multiples, Ramanujan terms, and prime-power gcd
modes included. Combining with Round 84 leaves exactly

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{\lfloor J^{17/30}\rfloor<|d|<\Delta_b-E_*}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

No estimate for this interior correlation is accepted. The exact shifted
physical-row identity preserves the \(Q^{-5/12}\) energy gain, but its
multiplier triangle gives no \(B\)-power; d-differencing leaves a weighted
four-Kloosterman off-diagonal. Raw Farey transitions and axes remain
separately owned. No conductor range or global exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/hybrid_large_difference_attack.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/large_difference_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reviews/conductor_round85_support_edge_normalization.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reviews/conductor_round85_adjudication.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/synthesis.md.

## Round 86 accepted cubic lower-interior difference bound

Continue with the smooth Round-81 principal coefficient and the notation
of Rounds 84--85. Put

\[
 D_1=\lfloor J^{87/140}\rfloor.
\]

For \(e=|d|\le D_1\), both stationary indices remain in one
\(m\asymp Q^2\) band. On \(n=r+M\ell\), translation and reflection
reduce the phase to

\[
 \pm\lambda_b\bigl(\sqrt{m+e}-\sqrt m\bigr),
 \qquad \lambda_b\asymp J,
\]

whose third derivative has fixed sign and size

\[
 \rho_e\asymp {JM^3e\over Q^7}.
\]

The complete phase-removed product has sampled
\(\sup+\operatorname{Var}\ll_\varepsilon X^\varepsilon H^2\),
where \(H=C\sqrt T/J\). Weighted third derivative and

\[
 {1\over M^2}\sum_{r\bmod M}
 \left|S(r+d,K;M)\overline{S(r,K;M)}-c_M(d)\right|\le2
\]

give, after summing \(b\), both signs, and \(D_0<e\le D\),

\[
 \ll_\varepsilon X^\varepsilon\left(
 B^{5/2}J^{3/10}D^{7/6}
 +B^2J^{1/2}D^{5/6}
 +B^3J^{-1/5}D\right).
\]

At \(B\le J^{3/20}\) and \(D=D_1\), the three powers are
\(J^{7/5}\), \(J^{369/280}\), and \(J^{61/70}\). Therefore every

\[
 \lfloor J^{17/30}\rfloor<|d|\le
 \lfloor J^{87/140}\rfloor
\]

is target-safe. Combining Rounds 84--86 leaves exactly

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{D_1<|d|<\Delta_b-E_*}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

The physical \(Q^{-5/12}\) energy factor remains available. Exact
four-Kloosterman completion has prime-power and squarefree
divisor-aligned near-returns of near-quadratic size, so generic
coefficientwise trace estimates do not close this residual aggregate.
No conductor range or global exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/twisted_ambiguity_attack.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/four_kloosterman_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_cubic_shell_normalization.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_adjudication.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/synthesis.md.

## Round 87 accepted full-factor same-group Fejer bound

Continue on one dyadic part of the exact Round-86 deep survivor.  For the
normalized physical row

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \qquad
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24},
\]

factor \(M\) into full prime-power factors.  Each ordered unit pair
\(P=(x,y)\), \(x\ne y\), has a unique nonempty active set

\[
 S(P)=\{q\Vert M:x_q\ne y_q\pmod q\}
\]

and active local ordered-pair label \(\alpha(P)\).  Summing the inactive
diagonal units into \(H_{b,S,\alpha}\), the exact same-group Fejer package
is

\[
 \mathcal P_{\rm exc}(D,U)
 =\sum_{b\asymp B}\int_{\mathbb T}|D_U(\theta)|^2
 \sum_{S,\alpha}|H_{b,S,\alpha}(\theta)|^2\,d\theta.
\]

The sharp deep projection has logarithmic \(L^\infty\) cost.  There are
at most \(m_S^2\) active labels and \(r_S\) inactive units, with
\(m_Sr_S=M\).  Therefore

\[
 \mathcal P_{\rm exc}(D,U)
 \ll_\varepsilon X^\varepsilon UB^3T^4Q^{-5/6}.
\]

Choose \(U=D\).  Since \(B\le J^{3/20}\),

\[
 B^4T^4Q^{-5/6}\le J^{8/3}=J^{14/5-2/15},
\]

and the package lies below the required signed Fejer budget
\((D/B)J^{14/5}\).  The proof is exact for all three classes, full prime
powers and the \(2\)-part, both signs, reflected orientations, the actual
fourfold stationary symbol, the centered Ramanujan algebra, and
same-group stride-\(M\) returns.

The accepted global \(u=0\) diagonal remains owned once.  What remains
open is the cross-group off-diagonal with \(u\ne0\), including partial
lower-conductor returns, bad primes, additional \(2\)-adic periods, and
aperiodic local traces.  This is a strict reduction but proves neither
the full deep bound nor a conductor or global-exponent improvement.

Accepted evidence:

- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/aligned_mode_aggregate_attack.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/blind_exceptional_strata_rederivation.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/exceptional_trace_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_normalization.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_crt_fejer.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md.

## Round 88 accepted cross-group period-depth subaggregate bounds

Continue on one dyadic part of the strict Round-87 cross-group deep
survivor, with the globally owned \(u=0\) term removed by

\[
 \mathcal K_D^\circ(\theta)=|D_D(\theta)|^2-D.
\]

For a divisor \(m\mid M\), write \(R=M/m\) and group each physical
ordered pair by its Round-87 active-set/active-label class after reduction
modulo \(m\), including the empty coarse active set. The exact lift count
gives

\[
 \sum_\gamma |K_{b,m,\gamma}|^2
 \ll_\varepsilon X^\varepsilon
 M^2R^2T^4Q^{-5/6}.
\]

Divisor-lattice differences assign each pair of physical labels a unique
first coarse coincidence quotient \(R_*\). With

\[
 \rho_*=min\!\left(M,
 \left\lfloor J^{11/30}B^{-2}\right\rfloor\right),
\]

all shells \(1<R_*\leq\rho_*\) satisfy

\[
 |\mathcal G_{\rm coarse}(D)|
 \ll_\varepsilon X^\varepsilon
 DB^3\rho_*^2T^4Q^{-5/6}
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5}.
\]

The local period is that of the complete reciprocal masked weight. If
its period modulo \(p^\nu\) is \(p^{\nu-j}\), its completed trace is
supported on \(p^j\mid u\) and descends with factor \(p^{2j}\). For
\(p\geq11\), \(p\nmid K\), and a nonempty mask, put
\(a=\min(j,\nu-j)\). Six-point Vandermonde rigidity gives

\[
 p^a\mid(B_2-A),\qquad p^a\mid AV,
 \qquad p^a\mid AV(V+B_2).
\]

Let \(\mathfrak a\) be the product of these good-prime depths. The
corresponding physical-edge graph has in- and out-degree
\(\ll_\varepsilon X^\varepsilon M^2/\mathfrak a\). Hence, after the
coarse deletion, every complete fibre with

\[
 \mathfrak a\geq M^2/\rho_*^2
\]

is target-safe.

The exact first-band residual now has

\[
 R_*>\rho_*,\qquad
 \mathfrak a<M^2/\rho_*^2,
\]

and retains small-prime masked periods, affine frequency cancellation,
nonunit-\(K\) and \(2\)-adic conductor drops, projection-only depth,
shallow good-prime lifts, and aperiodic traces. Numerator-only period
classification, a \(p^j\) completed-trace descent, and automatic Fejer
saving from frequency sparsity are false. No conductor range or global
exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/period_depth_tensor_attack.md;
- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/blind_cross_group_tensor_rederivation.md;
- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/cross_group_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reviews/conductor_round88_normalization_coarse_count.md;
- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reviews/conductor_round88_masked_period_graph.md;
- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/synthesis.md.

## Round 89 accepted bad-prime cellwise period graph

For a unit local phase, reciprocal periodicity is classified from the
complete mask. The successful raw reduction counts at
\(p=2,3,5,7\) are \(1,15,25,13\). The transverse \(p=3,5\) rays have
exact reciprocal depth one at every lift. Odd nonunit factors and the
full (2)-part have the guaranteed periods recorded in the Round-89
synthesis; these are routing identities only.

For a tensor of selected complete reduction cells, put

\[
 \mathfrak b_\sigma=
 \prod_{p^\nu\in S}{p^2\over\eta_{\omega_p}}.
\]

Separate source and target counts give

\[
 \deg^+(\mathcal E_\sigma),\deg^-(\mathcal E_\sigma)
 \leq {M^2\over\mathfrak b_\sigma}.
\]

Therefore every cell tensor with
\(\mathfrak b_\sigma\geq M^2/\rho_*^2\) is target-safe. A union must
pay the explicit sum of cellwise degrees. The conditional
\(M=3^\nu\), \([1:2:1]\), \(M/3\leq\rho_*<M\) family is a nonempty newly
owned example.

The full nonunit union can retain degree \(M^2\). At top conductor
\(M^2\asymp J^{3/10}\) while \(\rho_*^2=J^{2/15}\), leaving the exact
factor \(J^{1/6}\). Exact \(q=4,8,9\) controls show that period depth
does not remove this physical capacity. The full first band and the
global exponent remain open.

Accepted evidence:

- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_period_graph_attack.md;
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/blind_bad_prime_fibre_rederivation.md;
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reviews/conductor_round89_adjudication.md;
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/synthesis.md.

## Round 90 accepted square-root capacity self-return barrier

Let \(H_{b,D}\) be the complete deep centered physical-pair row and

\[
 \mathcal E_D=\sum_{b\asymp B}\int_{\mathbb T}
 |D_D(\theta)|^2|H_{b,D}(\theta)|^2\,d\theta.
\]

The Fourier coefficients of \(H_{b,D}\) are exactly the centered
Kloosterman-product coefficients from Round 83.  Expanding
\(\mathcal E_D\) gives the complete four-row actual-symbol operator of
Rounds 87--89.  The integer \(u=0\) coefficient is owned once, and the
remaining edge set is partitioned by successive complements into the
Round-87, Round-88, Round-89, and hard packages.

Complete prime-power descent is exactly invertible.  The
\(p^{2j}\) trace factor cancels the quotient-square inverse
normalization, and restricted Fejer shifts retain total mass.  The
finite Toeplitz inequality gives

\[
 \left|\sum_{b\asymp B}H_{b,D}(0)\right|^2
 \ll_\varepsilon X^\varepsilon{B\over D}\mathcal E_D.
\]

With

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12},\qquad
 \mathsf T_{82}=J^2/T,
\]

the full-degree Gram capacity and target satisfy

\[
 \mathsf C_{\rm deep}={D\over B}\mathsf C_{82}^2,
 \qquad
 \mathsf T_{\rm deep}={D\over B}\mathsf T_{82}^2.
\]

Thus the late \(J^{1/6}\) energy gap square-roots exactly to the
Round-82 \(J^{1/12}\) linear gap.  This proves a Gram-level
equal-capacity barrier, not a linear involution and not an estimate of
the hard signed operator.  The \(q=8\) residual cell retains full
directed degree, so further local period peeling cannot provide a
strict gain.  M9-M1 and the global exponent remain open.

Accepted evidence:

- rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/m1_self_return_barrier_attack.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/blind_m1_capacity_rederivation.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/m1_self_return_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/reviews/conductor_round90_normalization.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/reviews/conductor_round90_reassembly.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/synthesis.md.

## Round 91 accepted unconditional one-third theorem

For every literal dyadic M1 or M2 block, including the actual Vaaler
coefficient, the M1 spatial character, the M2 two-shift character
factor, both signs, floors, stars, and the hard-top sampled-BV profile,
the accepted direct estimates give

\[
 B_i(D,L;X)\ll_\varepsilon X^\varepsilon
 \min\!\left\{1+{D\over L},
 1+\left({LX\over D}\right)^{1/2}
   +{D^{3/2}\over(LX)^{1/2}}\right\}.
\]

Write \(R=D/L\). If \(R\le X^{1/3}\), the first row is
\(O(X^{1/3+\varepsilon})\). If \(R\ge X^{1/3}\), then

\[
 (X/R)^{1/2}\le X^{1/3},\qquad
 D(R/X)^{1/2}\le X^{1/4},
\]

because \(R\le D\le X^{1/2}\). Hence every main block is
\(O(X^{1/3+\varepsilon})\). The bottom denominator range is
\(O(X^{1/4})\), and the pointwise Fejer product-count argument gives
\(O(X^{1/4+\varepsilon})\) for every residual block, including exact
products and the two shifted legs. The exact denominator-frequency
assembly costs only \(O(\log^2X)\). Therefore

\[
 \boxed{P(X)\ll_\varepsilon X^{1/3+\varepsilon}}
\]

uniformly for real \(X\ge2\).

This exponent is exact for the accepted direct menu: at
\((\delta,\ell)=(1/2,1/6)\), the T2S and full second-derivative rows
both equal \(1/3\), while the trivial and TTY rows are larger. This is
menu optimality, not a lower bound for the actual sums. Any exponent
below \(1/3\), and in particular the target \(1/4\), requires a new
signed estimate for the residual M1 or M2 hard core.

Accepted evidence:

- rounds/codex-managed/gc-unconditional-exponent-extraction/reports/blind_global_exponent_rederivation.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/reports/global_exponent_assembly_attack.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/reports/global_exponent_hostile_audit.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/reviews/conductor_round91_r5_reconciliation.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/reviews/conductor_round91_assembly.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/synthesis.md.

## Round 92 accepted canonical open cores

Round 92 promotes no estimate.  It replaces two informal survivor chains by
two exact open obligations.

For the first smooth nonaxial M1 residual band
(J^{13/18}<C\leq J^{3/4}), with
(D_1<|d|<\Delta_b-E_*), the exact hard complement of the accepted
Round-87--89 owners must satisfy

\[
 |\mathcal E_{\rm hard}(U)|
 \ll_\varepsilon X^\varepsilon{U\over B}J^{14/5}.
\]

The definition retains every local class and sign, the actual fourfold
stationary symbol, modulus multiples, Ramanujan terms, the full (2)-part,
one global (u=0) owner, and a conjugation-closed hard complement.  The
linear (J^{1/12}) and Gram (J^{1/6}) gaps are the same deficit before
and after the proved Toeplitz square root.

For the residual hard top M2 cone, the exact joint density--discrepancy
target is

\[
 \sum_{A,D_{\rm ray},K_{\rm rec},G,R}
 |\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
 \ll_\varepsilon L^2X^\varepsilon.
\]

It retains the metric density (r=0), all discrepancy modes, the actual
character/profile, both orientations, and one outer (2\Re).  A hard block
has capacity (L^2X^\varepsilon\sqrt\rho), so the missing gain is exactly
(\rho^{-1/2}).  The accepted bridge
(|\mathcal T_{\rm end,L}|^2\ll L\mathcal E_L^\top) then yields the
original top-row target if the energy closes.

Neither obligation closes its outside packets.  Therefore M9-M1, M9-M2,
M9, target-scale endpoint uniformity, and the one-quarter theorem remain
open.

Accepted evidence:

- rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md;
- rounds/codex-managed/m9-canonical-core-formalization/reports/canonical_core_formalization_attack.md;
- rounds/codex-managed/m9-canonical-core-formalization/reports/canonical_core_hostile_hygiene_audit.md;
- rounds/codex-managed/m9-canonical-core-formalization/reviews/conductor_round92_adjudication.md;
- rounds/codex-managed/m9-canonical-core-formalization/synthesis.md.

## Round 93 accepted global mean square and density-one quarter theorem

For a fixed dyadic denominator shell, exact rational-frequency grouping
and a continuous large sieve give

\[
 \int_I|S_{D,H,w}(t)|^2\,dt\ll (|I|+D^2)D.
\]

The coefficient mass is sharp at order \(D\).  Writing
\(\gamma_{h,r}=\beta_{h,r}-\beta_{h,r-1}\), one has
\(|\gamma_{h,r}|\ll r^{-2}\mathbf 1_{0<|h|\le r}\).  Exact reduced-ray
grouping, a binary-prefix maximal large sieve, and a Stieltjes
representation of every fixed-BV profile transfer the same power bound to
the moving height floor, hard top, and endpoint stars with logarithmic loss
only.

Using the fixed-in-\(Y\) partition
\(D_j=2^{-j}\sqrt Y\), the exact moving M1 and M2 blocks, the bottom owner,
R5-Full, and H1--H4 assemble to

\[
 \boxed{\int_Y^{2Y}|P(t)|^2\,dt
 \ll_\varepsilon Y^{3/2+\varepsilon}.}
\]

Consequently, for every fixed \(\eta>0\),

\[
 \boxed{
 \bigl|\{t\in[Y,2Y]:|P(t)|>Y^{1/4+\eta}\}\bigr|
 \ll_{\varepsilon,\eta}Y^{1-2\eta+\varepsilon}.}
\]

This proves the quarter exponent on a density-one set of real parameters.
It does not control a prescribed real, an integer, or a jump point.  It also
does not estimate either Round-92 canonical core, so M9-M1, M9-M2, M9,
endpoint uniformity, and the uniform one-quarter theorem remain open.  The
uniform exponent remains \(1/3\).

Accepted evidence:

- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/blind_m2_moment_rederivation.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/moving_coefficient_moment_attack.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/moment_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reviews/conductor_round93_adjudication.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md.

## Round 94 accepted prescribed-point interfaces

For \(u\ge0\), monotonicity of the inclusive count gives

\[
 P(x+u)\ge P(x)-\pi u,
 \qquad
 P(x-u)\le P(x)+\pi u.
\]

Thus, if \(M=|P(x)|\) and \(Q(Y,W)\) bounds every relevant
length-\(W\) local square integral, then

\[
 \frac{M^2}{4}\min\left(W,\frac{M}{2\pi}\right)\le Q(Y,W),
 \qquad
 M\ll Q^{1/3}+(Q/W)^{1/2}.
\]

For every integer \(n\),

\[
 \int_n^{n+1}P(t)^2dt
 =\left(P(n)-\frac\pi2\right)^2+\frac{\pi^2}{12}.
\]

Consequently

\[
 \sum_{Y\le n\le2Y}|P(n)|^2
 \ll_\varepsilon Y^{3/2+\varepsilon},
\]

and the number of integers with
\(|P(n)|>Y^{1/4+\eta}\) is
\(O_{\varepsilon,\eta}(Y^{1-2\eta+\varepsilon})\).  The same square
sampling estimate holds for every one-separated real sample set.  These
are discrete density-one results, not prescribed-point estimates.

For a fixed exponential polynomial on a window of length \(W\), the
sinc-square kernel gives the exact randomly shifted rational-cell form

\[
 \int_I|S(t)|^2dt
 \le \frac{\pi^2}{4}W\int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}
 a_\lambda e(\lambda c)\right|^2d\vartheta.
\]

The literal frequencies are \(h/d\) for M1 and \(h/(4d)\) for M2.
For \(W\le Y^{1/2}\), the moving floors and hard prefix create only
\(O(\log Y)\) fixed-symbol strata.  At the minimax block
\((D,L)=(Y^{1/2},Y^{1/6})\), the frequency diameter is
\(O(Y^{-1/3})\).  Therefore \(W=Y^\alpha\), \(\alpha<1/3\), is
subcoherent and the cluster form contains \((1-o(1))|S(c)|^2\).

The first genuinely averaging open range is

\[
 1/3<\alpha<1/2.
\]

An actual signed cluster energy \(\ll Y^{1/2+\varepsilon}\) there would
imply \(P(X)\ll X^{1/6+\alpha/3+\varepsilon}<X^{1/3+\varepsilon}\).
No such estimate is proved.  Popov's uniform local second moment retains
an additive \(Y(\log Y)^2\) term and returns exactly exponent \(1/3\).
Thus the certified uniform exponent remains \(1/3\), and both canonical
M9 cores and the quarter target remain open.

Accepted evidence:

- rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reports/blind_pointwise_bridge_rederivation.md;
- rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_persistence_sampling.md;
- rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_local_kernel.md;
- rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_source_scope.md;
- rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_adjudication.md;
- rounds/codex-managed/gc-prescribed-point-local-moment-bridge/synthesis.md.

## Round 95 certified external exponent and internal cluster normal form

The narrowly repaired and source-audited Li--Yang theorem gives, for
real \(X\ge2\),

\[
 P(X)\ll_\varepsilon
 X^{(3292+25\sqrt{1717})/13762+\varepsilon}
 =X^{0.3144831759740614\ldots+\varepsilon}.
\]

This is the strongest certified global pointwise theorem. It is an
external direct route and does not prove either canonical M9 core.

Internally, the fixed \(W=Y^{7/16}\) M1/M2 cluster reduces exactly to a
signed reduced-determinant correlation after all equal lifts are
combined. The equal-frequency diagonal is
\(O_\varepsilon(D/L)\), while coefficient-blind Farey capacity at the
minimax block is \(Y^{43/48+\varepsilon}\), missing the target by
\(Y^{19/48}\). Thus the strongest internally proved exponent remains
\(1/3\).

Accepted evidence:

- rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/synthesis.md;
- sources/li_yang_2023.md.

## Round 96 primitive-ray q-dispersion obstruction

For the residual canonical hard top M2 cone,

\[
 m=(a+b)/2,\qquad q=(b-a)/2,\qquad
 \chi_4(a)\chi_4(b)=(-1)^q.
\]

At fixed \(m\), legal shifts are \(q\mapsto q+2h\), so the character
autocorrelation is \(+1\). At fixed \(a=m-q\), sign-changing shifts
produce the exact complete actual-symbol Fejer Gram, retaining both
moving reciprocal intervals, lift sets, owner masks, entry/exit, and
the joint metric density-discrepancy coefficient.

With

\[
 P\asymp L^2\sqrt\rho,\qquad E_0\asymp LJD^2,
\]

a separately estimated diagonal costs \(P^2/H\), \(H\le D\), and gives
at most \(D^{-1/2}\) linear gain. Hard \(q=1\) Pell rows have
\(D\asymp1\) and \(\rho\to\infty\). Shift Fourier transform and the
adjoint reciprocal transform return to the original half-frequency /
two-character row at equal capacity.

This is a proved route obstruction, not a lower bound for the actual
block. The first open kernel is the complete fixed-\(a\) Gram estimate

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon\frac{H^2}{\rho}E_0,
\]

or an equivalent determinant-weighted off-shift correlation theorem.
No M2, M9, or exponent promotion follows.

Accepted evidence:

- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md;
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/reviews/conductor_round96_adjudication.md.

## 19. Round 97 exact M2 outside-packet assembly

The accepted denominator partition has one bottom remainder, one hard
profile containing \(d=\lfloor\sqrt X\rfloor\), and otherwise smooth
profiles. After R5-Full, terminal T2S, the full second-derivative cell,
and the TTY wedge, the exact residual is

\[
 \mathcal U=
 \{(\delta,\ell)\in\Omega:
 \ell<\delta-1/4,\ 178\ell+1638\delta>463\}
 \setminus\{(1/2,0)\}.
\]

Freeze the physical balanced class by \(1\le K/L\le16\), where
\(K=XL/D^2\). The residual then splits disjointly into hard, smooth
balanced, and smooth unbalanced labels. The exact one-count table proves

\[
 \mathrm{TOP}+\mathrm{BAL}+\mathrm{UNBAL}
 \Longrightarrow\mathrm{M9\!-\!M2},
\]

where

\[
 \mathrm{BAL}:\quad
 \left|\sum_GG\mathscr P_G\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
\]

and

\[
 \mathrm{UNBAL}:\quad
 \mathcal T_{L,K}\ll_\varepsilon(LK)^{3/4}X^\varepsilon.
\]

The hard canonical theorem, BAL, and UNBAL are all open. The smooth
Poisson and balanced gcd identities are proved reductions only. Thus the
canonical hard theorem alone does not imply M9-M2.

Round 97 also removes the circular M9-M2 / near-collision-taxonomy edge
and reclassifies the exact character factor as proved normalization.
No pointwise exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/synthesis.md;
- rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/reviews/conductor_round97_adjudication.md.

## 20. Round 98 exact M1 route-interface assembly

After bottom ownership, R5-Full, the terminal theorem, the full
second-derivative region, and the TTY wedge, the exact direct M1 residual is

\[
 \mathcal U_1=
 \{(\delta,\ell)\in\Omega:
 \ell<\delta-1/4,\ 178\ell+1638\delta>463\}
 \setminus\{(1/2,0)\}.
\]

Lifting this exponent region to literal physical labels and splitting by the
unique profile containing (d=\lfloor\sqrt X\rfloor) gives a disjoint hard
residual and smooth residual. The accepted one-count table proves the exact
conditional implication

\[
 \mathrm{TOP}_{\rm residual}+\mathrm{SMOOTH}_{\rm residual}
 \Longrightarrow \mathrm{M9\!-!M1}.
\]

The canonical first-band M1 Gram is downstream of global angular
recombination and owns only one transition-flattened smooth nonaxial
principal component for (J^{13/18}<C_{\rm cond}\le J^{3/4}). There is no
accepted inverse localization from that Gram to individual physical
((D,L))-blocks. Consequently, even its conjectural proof would not remove
either direct parent above.

For the alternative total-active route, a fixed smooth radial partition has
a proved compact critical interior and two exact open parents: a signed lower
radial aggregate and a sharp upper radial/interface aggregate. The exact
global assembly is

\[
 \mathrm{LOWER}_{\rm radial}+\mathrm{INTERFACE}_{\rm radial}
 \Longrightarrow \mathrm{GAR}.
\]

GAR controls the total active M1 contribution, not each dyadic block. Thus

\[
 H1\!-!H3+H4+R5\text{-Full}+\mathrm{GAR}+\mathrm{M9\!-!M2}
 \Longrightarrow \mathrm{GC\ target}
\]

is an alternative conditional bridge, not a proof of blockwise M9-M1 or M9.
The graph has been rewired accordingly and its dependency cycles removed.
All analytic parents remain open and no exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m1-route-interface-assembly/synthesis.md;
- rounds/codex-managed/m9-m1-route-interface-assembly/reviews/conductor_round98_adjudication.md;
- rounds/codex-managed/m9-m1-route-interface-assembly/reviews/conductor_round98_graph_and_cycle_audit.md.

## 21. Round 99 exact joint four-row self-return

On the literal canonical hard complement, open the complete trace and set

\[
 r=n+d+u,\qquad s=m+d.
\]

Then

\[
 ux+dV+nA-mB_2
 =rx+n(A-x)+s(V-x)+m(x-V-B_2),
\]

and \(M^{-5}\mathfrak T_M\) becomes exactly \(M^{-4}\) times the four
normalized physical rows. On a smooth stationary branch,

\[
 D^2_{d,u}\Psi
 =L^T\operatorname{diag}(\psi_b''(r),-\psi_b''(s))L,
 \qquad L\in GL_2(\mathbb Z).
\]

Thus the nonzero determinant \(\asymp-J^{-2/5}\) consists exactly of the
two one-row curvatures. The Fejer factor becomes a function of
\(r-s+m-n\), and Fourier recompletion is the original centered Toeplitz
four-row Gram. A second B-process gives no independent \(J^{-1/5}\).

Every fixed physical configuration is rank one in \((n,m)\); actual phases
are gauges and telescope on paired closed trace cycles. Ordinary trace
moments are direct sums in conductor row. The exact local identity

\[
 \mathfrak T_8(u,A,B_2,V)=8e_8(K(A-B_2))c_8(u)
\]

retains the coherent nonzero \(u=4\) mode after the unique \(u=0\) owner.
This is a control obstruction, not a global actual-vector lower bound.

The exact remaining analytic obligation is the fixed-vector estimate

\[
 \left|\widehat p_U^*\widehat{\mathcal K}_U\widehat q_U\right|
 \ll_\varepsilon X^\varepsilon
 { (U/B)J^{14/5}\over\mathsf C_U},
\]

whose top scale is \(J^{-1/6}\). All configurations must remain inside the
matrix entry, and any conductor-row cancellation must occur in the scalar
coefficient before taking a uniform norm. This estimate remains open.

Accepted evidence:

- rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/synthesis.md;
- rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/candidates/conductor_joint_four_row_self_return.md;
- rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/reviews/conductor_round99_adjudication.md.

## 22. Round 100 exact \(q=8\) actual-vector cross-projection

On the exact two-primary subfamily

\[
 M=8N,\qquad N\ \mathrm{odd},\qquad
 A\equiv B_2\equiv V\equiv2\pmod8,
\]

CRT and the completed-trace convention give

\[
 {\mathfrak T_M\over M^2}
 ={c_8(u)\over8}{\mathfrak T_N\over N^2}.
\]

The local factor is \(+1/2\) for \(8\mid u\), \(-1/2\) for
\(u\equiv4\pmod8\), and zero otherwise. The unique global \(u=0\) owner
does not remove the nonzero branches. The canonical normalization remains
\(M^{-5}\mathfrak T_M=M^{-3}(\mathfrak T_M/M^2)\), and opening the odd
trace gives exactly four shared local bases, hence \(4/M^4\).

For the literal actual pair sequences on the local order-four orbit,

\[
 \sum_{j\bmod4}F_j\overline{G_{j-1}}
 ={1\over4}\sum_{k\bmod4}e_4(k)
 \widehat F_k\overline{\widehat G_k}.
\]

Thus the generic hard object is a cross-projection. The only structural
alignment \(G=F\) gives a difference of squares, but then the physical pair
labels coincide modulo \(2N\), so \(R_*=4\) and Round 88 already owns it.
The exact residual is the scalar \(\mathscr C_8(U)\), with odd completed
trace, all actual rows, transitions, and conductor sum retained.

No target estimate for \(\mathscr C_8(U)\) is proved. Local trace size and
paired trace mass give neither the missing \(J^{-1/6}\) gain nor a global
actual-vector lower bound. Higher \(2\)-parts and complementary modes remain
open.

Accepted evidence:

- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/synthesis.md;
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/candidates/conductor_q8_actual_vector_cross_projection.md;
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/reviews/conductor_round100_adjudication.md.

## 23. Round 101 full two-adic actual-row convolution

Write

\[
 M=2^\nu N,\qquad N\ \mathrm{odd},\qquad L=2^{\nu-1}.
\]

When the local four-unit mask is nonempty, it is exactly the complete odd
orbit \(x=1+2j\), \(j\bmod L\). For the literal actual pair rows,

\[
 \mathcal C_{2^\nu}(F,G)
 ={1\over L^2}\sum_{k,l\bmod L}e_L(lv)
 \widehat w_{l-k}\widehat F_k\overline{\widehat G_l}.
\]

The normalized matrix \(L^{-1}\widehat w_{l-k}e_L(lv)\) is unitarily
equivalent to multiplication by the unimodular physical weight followed by
a cyclic shift. It has rank \(L\), norm one, and no local spectral gap.

The reciprocal phase has the guaranteed period

\[
 P_\nu=1\quad(\nu\le3),\qquad P_4=2,\qquad
 P_\nu=L/8\quad(\nu\ge5),
\]

so the full weight has affine Fourier support

\[
 \widehat w_r=0\qquad\text{unless}\qquad
 r\equiv u_2\pmod{L/P_\nu}.
\]

This decomposes the operator into permuted unitary blocks and gives no
power saving. Nonunit \(K\) may shorten the period but does not change this
conclusion.

The global integer \(u=0\) is owned once. Full aligned or reversal terms
are deleted only after their odd and two-adic return orders satisfy the
Round-87--89 owner tests. In particular, the Round-100 \(q=8\) aligned
square is prior-owned, but higher two-parts can have return
\(L/\gcd(L,v)>\rho_*\) and remain hard.

The exact survivor is the odd-cofactor and conductor sum
\(\mathscr S_{2\text{-adic}}(U)\), with all actual rows, transitions,
stars, classes, nonunit phases, and nonzero modulus multiples retained
before absolute value. Its \(J^{-1/6}\) fixed-vector estimate remains open.

Accepted evidence:

- rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/synthesis.md;
- rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/candidates/conductor_full_two_adic_orbit_convolution.md;
- rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/reviews/conductor_round101_adjudication.md.

## 24. Round 102 determinant carrier and short-ray ceiling

For the literal fixed-\(a\) primitive-ray row,

\[
 \mathcal G_H^{\rm act}
 =H E_{\rm act}
 +2\Re\sum_{1\le s<H}(H-s)(-1)^s C_s^{\rm act}.
\]

The extracted density carrier has curvature

\[
 -{X\sqrt a\over2}
 \left({g'\over k'(a+2q+2s)^{3/2}}
       -{g\over k(a+2q)^{3/2}}\right).
\]

This is not the complete density-discrepancy determinant. Metric Fourier
expansion replaces \(g,g'\) by \(g-2\ell,g'-2\ell'\); without expansion,
the complete metric and entry/exit coefficient has no accepted
\(q\)-variation theorem.

The density-carrier zero set is exact:

\[
 b=dx^2,\quad b_s=dy^2,\quad
 d(y^2-x^2)=2s,\quad g'kx^3=gk'y^3.
\]

For fixed \(a,s\) it has
\(O_\varepsilon(X^\varepsilon s^\varepsilon GK)\) raw tuples, and the
near ratio count is

\[
 \ll_\varepsilon X^\varepsilon
 \{\eta(GK)^2+GK\}.
\]

These are raw density-mode facts, not a weighted actual-symbol estimate.
Algebraic nonzero spacing is also below the active oscillatory scale.

The residual half-open \(q=1\) block has no nonzero shift. Its exact open
target is

\[
 \sum_a|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.
\]

Thus determinant separation is not a uniform proof mechanism. The
fixed-\(a\) Gram remains open, ordered after the short diagonal and then
the complete longer-row mode-resolved near and separated packages.

Accepted evidence:

- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/synthesis.md;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/candidates/conductor_determinant_split.md;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/reviews/conductor_round102_adjudication.md.

## 25. Round 103 complete singleton actual diagonal

On a residual fixed-\(a\) row containing only \(q=1\), write

\[
 b=a+2,\qquad \delta_a=\sqrt{a+2}-\sqrt a,
 \qquad \Lambda_a={X\delta_a^2\over2},
\]

\[
 I_a=\left({J\delta_a\over2\sqrt a},
            {J\delta_a\over\sqrt{a+2}}\right),
 \qquad K\asymp {J\over A},\qquad G\asymp {L\over A}.
\]

The complete physical coefficient has the exact carrier factorization

\[
 \mathfrak C^\circ_{a,k}(g)
 =e\!\left(-{g\Lambda_a\over2k}\right)
  \mathfrak B^\circ_{a,k}(g).
\]

After \(u=y^2\), the centered factor is a complete quadratic integral.
Every actual profile and both physical endpoint collars remain inside its
amplitude. Uniform complete-Fresnel analysis gives

\[
 \sup_k|B_{a,g}(k)|+\operatorname {Var}_kB_{a,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over J}.
\]

For a complete metric Fourier mode \(\nu\), the total reciprocal phase is

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_a\over k},
 \qquad |f_{\nu,g}''(k)|\asymp {|2\nu-g|A^2\over J}.
\]

Because \(g\) is odd, \(|2\nu-g|\ge1\); the density mode is retained and
is nonstationary in \(k\). Weighted second-derivative cancellation and the
two metric Fourier moments yield

\[
 |F_a(1)|\ll_\varepsilon X^\varepsilon {L^2\over A},
 \qquad
 \boxed{\sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.}
\]

This is an actual-symbol theorem. It is false as a coefficient-uniform
principle and does not estimate a nonzero \(q\)-shift. The complete
longer-row fixed-\(a\) Gram remains open.

Accepted evidence:

- rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/synthesis.md;
- rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/candidates/conductor_q1_sampled_k_closure.md;
- rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/reviews/conductor_round103_adjudication.md.

## 26. Uniform fixed-\(q\) actual rows and the polynomial-shell survivor

Let \(b=a+2q\), \(a\asymp b\asymp A\), and \(q\asymp D\) on one
residual hard top M2 block. Put

\[
 \delta_q=\sqrt{a+2q}-\sqrt a,\qquad
 \Lambda_q={X\delta_q^2\over2},\qquad
 K\asymp {JD\over A},\qquad G\asymp {L\over A}.
\]

The literal complete centered integral has sampled-\(k\) variation

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname{Var}_kB_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over JD}.
\]

This actual-symbol theorem uses the exact homogeneous profile, both fixed
physical collars, all entry/exit data, and

\[
 k\partial_k e(gk(y-r_k)^2)
 ={y+r_k\over2}\partial_y e(gk(y-r_k)^2).
\]

It is uniform as \(b/a\to4^{-}\): the reciprocal interval and physical
saddle path collapse together, and no inverse edge length occurs.

Opening the complete punctured metric factor gives reciprocal frequencies
\(n=|2\nu\pm g|\ge1\), including the density mode, with

\[
 |f_{\nu,g}''(k)|\asymp {nA^2\over JD}.
\]

Weighted second derivative estimation and the two complete Fourier
half-moments yield

\[
 |F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A},
\qquad
 \sum_{a\asymp A}\sum_{q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}.
\]

Consequently

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon {H^2DL^4\over A}.
\]

Against the canonical target \(X^\varepsilon H^2L^4/(AD)\), the exact
rowwise-Cauchy deficit is \(D^2\). It is absorbed for every prescribed
fixed polylogarithmic range \(D\le(\log(2+X))^C\), but no fixed
positive-power shell follows. This is a route ceiling rather than an
actual lower obstruction.

The first remaining M2 core is the complete signed polynomial-shell
cross-\(q\) correlation, with both moving reciprocal fibres, both lift
sets, every owner, the metric density and every discrepancy mode, and all
entry/exit transitions still coupled. No global exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/synthesis.md;
- rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/reviews/conductor_round104_adjudication.md.

## 27. Polynomial-\(q\) transport residual and primitive dual square

The strongest transparent sufficient theorem is

\[
 \sup_{I\subset[D,2D)}
 \left|\sum_{q\in I}(-1)^qF_a(q)\right|
 \ll_\varepsilon X^\varepsilon {L^2\over A}.
\]

At \(H\asymp D\), the exact zero-extended one-count would give the
canonical fixed-\(a\) Gram.  The theorem is unproved: fixed-row control
misses it by \(D\) in amplitude and misses the direct Gram by \(D^2\).

For one complete mode, set

\[
 r_{q,k}={J\delta_q\over2k},\qquad c=\nu-{g\over2}.
\]

The centered material derivative transports the physical saddle, but the
complete phase recouples as

\[
 c{\Lambda_q\over k}+gk(y-r_{q,k})^2
 =\nu{\Lambda_q\over k}+gky^2-gJ\delta_qy.
\]

Thus a residual derivative \(c\Lambda_q'/k\asymp nJ\) remains.  The
density mode is the original physical phase, so neither total variation
nor deletion of a formal zero mode is licensed.

The scalar joint Hessian is exactly

\[
 \det\nabla^2_{q,k}\Psi
 =-{c^2X^2(t-1)^3\over t^3k^4}
 \asymp-{n^2A\over D},
 \qquad t=\sqrt{(a+2q)/a}.
\]

Full rank is not a free gain. Expand primitivity and put \(q=du\),
where \(d\mid a\) is odd. For the branch
\(c=\nu-g/2<0\), successive scalar stationary transforms have odd dual
\(s=d-2h\) and exact phase

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{dn\ell/s}-{1\over2}\sqrt{as/d}\right)^2,
\]

with

\[
 e(-as/(4d))=-i\chi_4(a/d)\chi_4(s).
\]

Hence the alternating primitive lattice returns an odd-character
reciprocal/product square at equal carrier capacity.  This is an exact
reduction and a determinant-only route obstruction, not an
owner-preserving transform theorem: all transformed owners, lifts,
profiles, collars, modes, maximal cutoffs, and stationary errors remain to
be matched.

The complete maximal theorem, every fixed positive-power \(q\)-shell,
the fixed-\(a\) Gram, and all downstream M2 obligations remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/synthesis.md;
- rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/reviews/conductor_round105_adjudication.md;
- rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/controls/conductor_round105_controls.md.

## 28. Signed principal symbol and exact owner conjugation

Round 106 corrects and completes the smooth-interior scalar dictionary.
For either orientation put

\[
 c=\nu-\tau g/2,\qquad n=2|c|,\qquad
 \epsilon=\operatorname {sgn}(c).
\]

Each orientation contains both signs. After \(q=du\), \(d\mid a\) odd,
the signed dual labels and joint saddle are

\[
 m=-\epsilon\ell,\qquad d-2h=-\epsilon r,\qquad
 y_*^2={\ell\over n},\qquad
 k_*^2={n\Lambda_{du}\over2\ell},\qquad
 b_*={4d^2Xn\ell\over r^2}.
\]

The stationary phase is

\[
 \epsilon\left(J\sqrt{dn\ell/r}
       -{1\over2}\sqrt{ar/d}\right)^2.
\]

The physical, \(k\)- and \(u\)-Gaussian units multiply to \(e(1/8)\),
and the strict-interior principal coefficient is

\[
 e(1/8){g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}
 A^\circ_{ga,gb_*}(g\ell/n).
\]

This point value is not a uniform actual symbol. At collars, reciprocal
or maximal endpoints, lift boundaries, hard samples, equalities and the
collapsing edge, the normalized complete Fresnel vector must remain.

There is an exact discrete obstruction to pointwise owner transport. If
\(P_E\) is any literal owner on the finite zero-extended \((u,k)\)-array,
then the Fourier stage gives

\[
 \widetilde P_E=\mathcal F P_E\mathcal F^{-1}.
\]

It preserves norm, rank, complements and one-count and returns exactly
under inversion. Since \(b_*\) is generally nonintegral, evaluating a
sharp integer owner there depends on an arbitrary cardinal interpolation.
The invariant dual object is the nonlocal conjugated owner kernel, not a
pointwise indicator.

The scalar frequency map preserves local \(L^2\) density. Therefore the
complete-Fresnel owner kernel is an equal-capacity reformulation of the
open signed nonzero-shift actual Gram, not a \(D\)-saving. Its denominator
scale and joint \((\ell,r)\) symbol also fail the accepted terminal M1
hypotheses.

Accepted evidence:

- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/synthesis.md;
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/reviews/conductor_round106_signed_stationary_normalization.md;
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/reviews/conductor_round106_owner_conjugation_gate.md;
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/controls/conductor_round106_controls.md.

## 29. Unbalanced smooth divisor regrouping and fixed-centre return

For a literal strict smooth unbalanced M2 component, put

\[
 K={XL\over D^2},\qquad M=LK,\qquad F=\sqrt{XM}={XL\over D}.
\]

The exact product coefficient is

\[
 A_{L,K}(n)=\sum_{hk=n}\chi_4(h)a_{L,K}(h,k),
 \qquad
 \mathcal T_{L,K}=\sum_nA_{L,K}(n)e(\sqrt{Xn}),
\]

with

\[
 \sum_n|A_{L,K}(n)|^2\ll_\varepsilon MX^\varepsilon.
\]

For a separated Mellin mode its Dirichlet series is

\[
 L(s-it_1,\chi_4)\zeta(s-it_2).
\]

The actual coefficient is the full two-height inverse-Mellin
superposition and is not (r_2(n)/4). Complementary divisor incidences
belong to other physical owners.

Both degree-one root numbers are (+1), and the formal reflected factor
lengths are

\[
 {X\over D}\quad\hbox{and}\quad D.
\]

The exact smooth character process has

\[
 h_*={4Xk\over r^2},\qquad
 2\sqrt2\,i,e(-1/8)\chi_4(r)(Xk)^{1/2}r^{-3/2}.
\]

After inserting the literal symbol, the physical normalization leaves
exactly (-i/(2\pi)) times the returned row. Exact (k)-Poisson gives

\[
 \mathscr R_{D,L}(X)=
 \sum_s\sum_{\substack{r\mid s\\r\ \mathrm{odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \int_0^\infty {q_L(h)\over h}
 e\!\left({hr(X-s)\over4X}\right)dh.
\]

It is rapidly supported on

\[
 |s-X|\lesssim {D\over L}.
\]

On a fixed flat smooth component the aggregate stationary error is
(O(KF^{-1/2})), hence (O(L^{-1})) after physical normalization.
Sharp clipped, starred, hard, or arithmetic-owner boundaries retain their
exact endpoint kernels.

The absolute capacity is ((D/L)X^\varepsilon), so the exact missing
factor against the physical target is

\[
 {D\over LX^{1/4}}={H_D\over L}.
\]

It vanishes only on the already owned terminal line. A sliding-window
outside-absolute correlation of the exact (A_{L,K}) is sufficient for
the three-quarter target, but that signed estimate remains open.

Accepted evidence:

- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md;
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_hb_kpoisson_return.md;
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_recombination_and_capacity.md;
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/controls/conductor_round107_controls.md.

## 30. Complete metric functional calculus and equal capacity

For the complete punctured metric multiplier, the normalized quadratic
kernel \(T_\alpha\) has Fourier multiplier \(e(\alpha y^2)\). Therefore

\[
 \sum_r\widehat W_R(r)T_{rc}
 =\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F
\]

exactly, including the density mode. Its operator norm is
\(\|W_R\|_\infty\), independent of the apparent resonance parameter.
The transform is equal-capacity and the primitive character cancels in
the fixed-\(a\) Gram. This is a proved obstruction, not an estimate.

Accepted evidence:

- rounds/codex-managed/m9-m2-metaplectic-two-character-energy/synthesis.md.

## 31. Blockwise scalar owner completion

With \(V_R(t)=\eta(R\|t\|)\) and \(W_R=V_R-V_{2R}\),

\[
 1_{t\notin\mathbb Z}
 =\sum_{1\le R<G_*}W_R(t)+V_{G_*}(t)-1_{t\in\mathbb Z}
\]

pointwise on the dyadic metric lattice. Using one orientation and one outer
\(2\Re\), the literal first-applicable owner partition gives

\[
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}-sum_\nu\mathfrak O_{B,\nu},
 \qquad
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.
\]

This is a scalar linear connector only. It supplies no Fejer or Gram cross
energy.

Accepted evidence:

- rounds/codex-managed/m9-m2-blockwise-owner-completion/synthesis.md.

## 32. Global completed real-part self-return

Let

\[
 \mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 =\sum_B\mathfrak Q_B^{\mathrm{comp}}.
\]

The accepted owner identity and the original Round-75 row identity are

\[
 \mathcal E_L^{\mathrm{top}}
 =\widetilde{\mathcal E}_{\mathrm{owned},L}
  +2\Re\mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 =\mathcal D_L+2\Re\mathfrak C_L^{\mathrm{off}},
\]

with
\(|\widetilde{\mathcal E}_{\mathrm{owned},L}|+\mathcal D_L
\ll_\varepsilon L^2X^\varepsilon\). Hence

\[
 \Re\bigl(
 \mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 -\mathfrak C_L^{\mathrm{off}}
 \bigr)=O_\varepsilon(L^2X^\varepsilon).
\]

The one-sided bound for the completed real part is therefore the minimal
hard-energy target and is equivalent to the original signed off-diagonal.
There is no certified complex self-return or smaller kernel. With
\(s=h+2r\), the remaining exact signed presentation is

\[
 \mathfrak C_L^{\mathrm{off}}
 =\sum_{a,r}\bigl(F_{L,a}(2r)-F_{L,a}(2r+1)\bigr),
\]

where every moving owner and support seam remains. Its target estimate is
open.

Accepted evidence:

- rounds/codex-managed/m9-m2-global-signed-completed-directional/synthesis.md;
- rounds/codex-managed/m9-m2-global-signed-completed-directional/reviews/conductor_round110_recombination_and_orientation.md.

## 33. Adjacent transport and the bulk discrete-lattice obstruction

For the exact finite zero-extended primitive-ray row,

\[
 2\sum_q(-1)^qF_{L,a}(q)
 =\sum_q(-1)^q\{F_{L,a}(q)-F_{L,a}(q+1)\}.
\]

This signed high-pass retains the cutoff endpoint and uses one orientation
with one outer \(2\Re\). Total variation, maximal, energy, modulus, and
Gram bounds are stronger.

Put

\[
 \delta_q=\sqrt{a+2q}-\sqrt a,\qquad
 \lambda_q=\left({\delta_q\over\delta_{q+1}}\right)^2.
\]

The map \((x,k)\mapsto(\lambda_qx,k/\lambda_q)\) has determinant one and
preserves the radical phase, \(kx\), and \(\Lambda_q/k\). For a compact
cardinal extension \(H\), however,

\[
 \lambda_q\sum_nH(\lambda_qn)-\sum_nH(n)
 =\sum_r\{\widehat H(r/\lambda_q)-\widehat H(r)\}.
\]

On any positive interval of length \(K\), the integer comb and pulled-back
scaled comb have coefficient-blind total-variation distance \(\asymp K\)
for every \(\lambda_q\ne1\), rational or irrational.

In a noncollapsed block

\[
 a\asymp A,\quad q\asymp D,\quad g\asymp L/A,\quad
 K\asymp JD/A,
\]

the reciprocal slabs have width \(K/D=J/A\), the physical slabs have
width \(L/D\), and the common-band carrier displacement is

\[
 {Xg(\delta_{q+1}^2-\delta_q^2)\over4k}\asymp {JL\over A}.
\]

The coefficient-blind bulk capacity is \(DL^2\); the separate endpoint
bound is \(L^2\sqrt\kappa\), with \(\kappa=JD/(AL)\ge D\). Hence
phase-preserving transport proves no positive-power shell. A first-failure
Boolean partition nevertheless owns every simultaneous arithmetic and
support jump exactly once.

This is a route obstruction, not an actual-symbol lower bound. The live
theorem is cancellation in the complete actual signed common-band
scaled-comb correlation, jointly with its one-count slabs when needed.

Accepted evidence:

- rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/synthesis.md;
- rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/reviews/conductor_round111_highpass_and_one_count.md;
- rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/reviews/conductor_round111_transport_lattice_and_capacity.md.

## 34. Balanced smooth quarter-packet normalization and literal seam

For one fixed real smooth balanced physical block \(B=(X,D,L,+)\), write
\[
R=\sqrt X,\qquad K=\frac{XL}{D^2},\qquad 1\le K/L\le16.
\]
Let \(\Omega_B\) contain only bounded internal subdivisions of this block,
and let \(G\) index a fixed smooth partition of \(g=(h,k)\). With
\(h=gu,\ k=gv,\ (u,v)=1\), the exact character identity and Poisson
summation give
\[
T_{B,\mathrm{small}}^{+,\mathrm{full}}
=\frac1{2i}\sum_{\omega\in\Omega_B}\sum_G
GQ_{B,\omega,G}^{\mathrm{full}}(R)+E_{B,\mathrm{gcd\text{-}bd}},
\]
where \(Q^{\mathrm{full}}\) is the \(\chi_4(u)\)-weighted \(1/4\) packet
minus the \(3/4\) packet. For real profiles,
\[
Q^{\mathrm{full}}(-R)=-\overline{Q^{\mathrm{full}}(R)},
\]
so the physical frequency blocks are conjugate after the factor
\(1/(2i)\).

The smooth packet is the full small-gcd transform. Exact-square and
\(R^{-1}\)-near-square prior owners therefore enter through explicit
signed subtraction terms; their arithmetic complement is not a smooth
\(g/G\)-profile. The required open norm has one modulus outside the
complete internal \((\omega,G)\)-sum for each fixed physical block.
Shellwise \(\ell^1\), product-fibre absolute values, and Gram bounds are
stronger.

The first remaining formal seam is the coefficientwise finite atom
dictionary: literal denominator and frequency profiles, floors, stars,
support crossings, transform errors, and their exact one-count identity
are named but not instantiated in the frozen artifacts. Once that
dictionary is supplied, the first analytic gap is
\[
\left|\sum_{\omega,G}GQ_{B,\omega,G}^{\mathrm{full}}(R)\right|
\ll_\varepsilon L^{3/2}X^\varepsilon.
\]
The present envelope still loses at most \(X^{1/12}\), maximally at
\(L=X^{1/6}\). No exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reviews/conductor_round112_normalization_and_symbol.md;
- rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reviews/conductor_round112_owner_norm_capacity.md.

## 35. Literal balanced smooth dictionary and exact physical one-count

Round 113 removes the remaining formal seam in the balanced smooth M2
packet. With (y=\lfloor\sqrt X\rfloor), (D_j=2^{-j}y),
(H=\lfloor DX^{-1/4}\rfloor), and (L_r=2^{-r}H), the denominator and
frequency profiles telescope exactly. Only (j=0) and (r=0) are
clipped; the frequency bottom is explicit; (H=1,2) have no full smooth
residual label. The entire (d=0) summand is defined as zero.

For a full smooth block (B=(X,j,r,+)), put

\[
 K={XL\over D^2},\qquad M=LK,
\]

and define the positive-quadrant continuum symbol

\[
 A_B(x,z)=W(x/L)\Phi(x/(H+1))
 \left({M\over xz}\right)^{3/4}
 W\!\left(\sqrt{{xX\over4zD^2}}\right).
\]

Its zero extension is real and smooth, agrees with every integer
coefficient, and has uniform rescaled seminorms. The exact physical
normalization is

\[
 \mathcal B_B^+=-c_B\mathcal T_B+E_{B,\mathrm{tr}},\qquad
 c_B={e(1/8)\over2\pi}X^{1/4}M^{-3/4},\qquad
 B_{2,B}=8\Re\mathcal B_B^+,
\]

with (|E_{B,\mathrm{tr}}|\ll1).

The exact ratio

\[
 {K\over L}=4^j{X\over\lfloor\sqrt X\rfloor^2}
\]

leaves (j=1) as the persistent balanced family. The (j=2) label is
balanced only at exact-square (X), where (K/L=16); all (j\ge3)
are unbalanced.

The explicit gcd telescope has low weight
(\eta(g/(\sqrt L/2))), an exact scale-one integer bottom, and high owner
(1-\eta(g/(\sqrt L/2))). On each low shell, Poisson gives

\[
 \mathcal T_B^{\mathrm{low}}
 ={1\over2i}\sum_\sigma G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(\sqrt X),
\]

where (Q^{\mathrm{full}}) is the (\chi_4(u))-weighted (1/4) packet
minus the (3/4) packet. High gcd is owned first; exact squares and
nonsquare (X^{-1/2})-near-squares are explicit signed low-part
corrections. Therefore

\[
 \mathcal T_B=\mathcal T_B^{\mathrm{hi}}
 +\mathcal S_B^{\mathrm{sq}}+\mathcal S_B^{\mathrm{near}}
 +\mathcal T_B^{\mathrm{res}},
\]

and

\[
 B_{2,B}=8\Re\!\left[-c_B(\mathcal T_B^{\mathrm{hi}}
 +\mathcal S_B^{\mathrm{sq}}+\mathcal S_B^{\mathrm{near}}
 +\mathcal T_B^{\mathrm{res}})+E_{B,\mathrm{tr}}\right].
\]

The first open analytic estimate is exactly

\[
 \left|\sum_\sigma G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(\sqrt X)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
\]

for each fixed physical block. The dictionary is capacity-preserving; the
worst remaining loss is still (X^{1/12}). No global exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/reviews/conductor_round113_dictionary_and_normalization.md;
- rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/reviews/conductor_round113_ownership_and_scope.md.

## 36. Full-product energy and the exact balanced double-far survivor

For one fixed persistent balanced block, put

\[
 a_B^{<}(h,k)=\chi_4(h)\,
 \eta\!\left({(h,k)\over \sqrt L/2}\right)A_B(h,k),
 \qquad
 Z_B(R)=2i\sum_{h,k}a_B^{<}(h,k)e(R\sqrt{hk}).
\]

Writing

\[
 c_B(n)=\sum_{hk=n}a_B^{<}(h,k)
\]

gives the exact full-product diagonal \(hk=h'k'\) and

\[
 \sum_n|c_B(n)|^2\ll_\varepsilon L^2X^\varepsilon.
\]

Thus the diagonal has one factor \(L\) of room inside the required
\(L^3X^\varepsilon\) energy budget. For

\[
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k,
\]

the two literal corridor counts are

\[
 \sum_{\substack{h,k,h',k'\\|\Delta|\le U}}
 |a_B^{<}(h,k)a_B^{<}(h',k')|
 \ll_\varepsilon L^2(U+1)X^\varepsilon
\]

and

\[
 \sum_{\substack{h,k,h',k'\\|\rho|\le Q}}
 |a_B^{<}(h,k)a_B^{<}(h',k')|
 \ll_\varepsilon L^2(Q+1)X^\varepsilon.
\]

Consequently both width-\(L\) corridors are target-safe. The exact
ray-defect identity, for \(h'=h+p\), \(k'=k+q\), is

\[
 \sqrt{h'k'}-\sqrt{hk}
 -{1\over2}\sqrt{k/h}\,p-{1\over2}\sqrt{h/k}\,q
 =
 -{\rho^2\over
 4(hk)^{3/2}\bigl(P+\sqrt{Q_0}\bigr)},
\]

where

\[
 P=1+\frac12\left({p\over h}+{q\over k}\right),
 \qquad
 Q_0=\left(1+{p\over h}\right)\left(1+{q\over k}\right).
\]

It does not by itself estimate the complement. The old full-symbol
mean-square target

\[
 \sum_{h\asymp L}
 \left|\sum_{k\asymp K}A_B(h,k)e(R\sqrt{hk})\right|^2
 \ll_\varepsilon L^{1/2}K^{3/2}X^\varepsilon
\]

is a valid sufficient connector to the balanced packet after Cauchy and
high-gcd subtraction. It is stronger than the scalar target and remains
unproved.

Up to the two target-safe corridors, the exact remaining energy is

\[
 E_{B,\mathrm{df}}
 =
 \sum_{|r|>L}\sum_n e\!\left(R(\sqrt n-\sqrt{n+r})\right)
 \!\!\!\sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}.
\]

The balanced estimate is therefore equivalent, modulo proved
target-safe terms, to

\[
 |E_{B,\mathrm{df}}|\ll_\varepsilon L^3X^\varepsilon.
\]

The phase is constant on each fixed \((n,r)\)-fibre, and an arbitrary
phase-adapted bounded coefficient has \(L^4\) double-far capacity.
Therefore neither large determinant alone nor a coefficient-uniform
broad estimate can close this line. Any continuation must exploit the
actual \(\chi_4\)-twisted slanted symbol. No M2 parent or global exponent
is proved here.

Accepted evidence:

- rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reviews/conductor_round114_energy_and_corridors.md;
- rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reviews/conductor_round114_norm_owner_and_mean_square.md.

## 37. Phase-free double-far mode and the zero-subtracted survivor

For the Round-114 double-far energy, write

\[
 h'=h+p,\qquad k'=k+q,\qquad
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k.
\]

Then the exact increment chart is

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q).
\]

Nonzero character factors force (p=2s), and on that fixed shift

\[
 \chi_4(h)\chi_4(h+p)=(-1)^s=e(s/2).
\]

Thus the character is constant along a fixed shift fibre; in a Poisson
description it displaces the dual lattice by one half rather than deleting
the nonzero aliases.

Define the fully assembled phase-free double-far mode by

\[
 M_B^{(0)}=
 \sum_{\substack{|h'k'-hk|>L\\|hk'-h'k|>L}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}.
\]

Expanding one low-gcd mask over divisors and applying Abel summation in
the remaining character variable, with both far gates and both literal
symbols retained, gives

\[
 |M_B^{(0)}|\ll_\varepsilon L^3X^\varepsilon.
\]

An independent exact-gcd and Möbius argument gives the same estimate.
This saving holds only after the complete signed assembly; taking
residuewise, shiftwise, divisorwise, or shellwise absolute values is not
licensed.

Consequently

\[
 E_{B,\mathrm{df}}=M_B^{(0)}+\mathcal R_B^{\mathrm{osc}},
\]

where

\[
 \mathcal R_B^{\mathrm{osc}}
 =\sum_{\mathrm{df}}a_B^{<}(h,k)
 \overline{a_B^{<}(h',k')}
 \left[e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)-1\right].
\]

The remaining balanced target is therefore equivalent, modulo the proved
phase-free term, to

\[
 |\mathcal R_B^{\mathrm{osc}}|
 \ll_\varepsilon L^3X^\varepsilon.
\]

The bracket is not pointwise small. The exact Fejer prefactor
((N_B+H-1)/H), with (N_B\asymp L^2), amplifies either already
target-saturating corridor to

\[
 O_\varepsilon\!\left((L^5/H+L^3)X^\varepsilon\right)
\]

for (H\ge L), so existing corridor owners do not certify a fixed-power
shortening (H\le L^{2-\delta}). The critical outer B-process also has
dual length (\asymp L^2) and unit stationary amplitude. These are scoped
mechanism obstructions, not lower bounds for the actual signed remainder.
The nonzero half-shifted aliases remain open, and no M2 parent or exponent
is proved.

Accepted evidence:

- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reviews/conductor_round115_identity_and_zero_mode.md;
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reviews/conductor_round115_dispersion_and_source_scope.md.

## 38. Literal divisor-progressive aliases and the parked one-alias mechanism

Expand the second low-gcd mask in the Round-115 exponential double-far
sum. For every odd divisor (d\mid h',k'), choose (s_d\pmod d) with
(h+2s_d\equiv0\pmod d) and write

\[
 h'=h+2s=d(\ell_d+2t),\qquad s=s_d+dt.
\]

Poisson summation in (t) has the literal dual variables

\[
 \mu={1\over2}-m\in\mathbb Z+{1\over2},\qquad
 \lambda={\mu\over d}.
\]

At an interior stationary point,

\[
 h'={Xk'\over\lambda^2},
\]

and the exact phase is

\[
 R\sqrt{hk}-{Xk'\over2\lambda}-{\lambda h\over2}
 +s_d(1/2-\lambda)
 =-{h(\lambda-R\sqrt{k/h})^2\over2\lambda}
  -{Xq\over2\lambda}+s_d(1/2-\lambda).
\]

The two far gates become

\[
 \rho={hk'\over\lambda^2}(\lambda^2-\lambda_0^2),
 \qquad
 \Delta={hk\over\lambda^2}(\lambda_r^2-\lambda^2).
\]

There are (dL^3) aliases of size ((dL)^{-1}). Finite Poisson on the
literal integer runs, with signed boundary tails and incomplete Fresnel
transitions retained, has total aggregate error
(O_\varepsilon(L^3X^\varepsilon)). Thus the open remainder is reduced
to the complete signed lifted bulk kernel.

This transform gives no estimate by itself. Aliaswise (\ell^1) has
(L^5) global capacity at (d=1). Writing (k'=dv) gives reciprocal
frequency (Xd^2/(2\mu)); optimal product-window counting returns only
(L^4) capacity. Since (dL^3) frequencies are sampled only (L/d)
times, spacing forces (d^2L^2)-sized clusters and a full-length
large-sieve diagonal. A second B-process has phase

\[
 -dR\sqrt{v(\ell_d+2n)},
\]

which exactly restores the original progression, character, Jacobian,
and range. The positive row-energy proposal is also a stronger replicated
Gram that would force the unrestricted scalar sum to be (O(L)).

These are scoped mechanism obstructions. They do not bound the actual
signed kernel and do not disprove BAL. The complete bulk
(O_\varepsilon(L^3X^\varepsilon)) estimate remains open, and all M9 and
global exponent claims are unchanged.

Accepted evidence:

- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reviews/conductor_round116_literal_alias_and_errors.md;
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reviews/conductor_round116_norm_involution_and_scope.md.

## Round 117 certified W=Y^(7/16) determinant progress

For one complete fixed M1 or M2 block at \(W=Y^{7/16}\), direct
geometric summation in the original numerator followed by a real-centre
integer-product window count gives

\[
 \mathcal C_i(c),\ |\mathfrak O_i|
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon.
\]

At the minimax block \((D,L)=(Y^{1/2},Y^{1/6})\), this is
\(Y^{37/48+\varepsilon}\), a factor \(Y^{1/8}\) below the accepted
coefficient-blind capacity \(Y^{43/48}\). The proof is before ray grouping,
so every lift, sign, profile, floor, hard top, and star is retained.

On the bounded-lift reduced-denominator shell \(b,b'\asymp D\), put

\[
 Q_*=\min\left(D,{D^2\over WL}\right),\qquad
 \lambda={YL\over D^3}.
\]

Finite-lift BV, Möbius inversion, and reciprocal second-derivative
summation prove

\[
 |\mathfrak O_{i,B\asymp D}|\ll_\varepsilon
 D\min\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right)Y^\varepsilon.
\]

At minimax this is \(Y^{35/48+\varepsilon}\), a factor \(Y^{1/6}\)
saving. The proof does not extend to \(B<D\), where the complete lift
length grows.

The two-dimensional determinant phase has exact Legendre dual

\[
 {ca\over\kappa_i b}+au+bv+{(c/\kappa_i)v\over u},
\]

so a character half-shift followed by coefficient-blind Cauchy,
Plancherel, or large sieve retains the \(Y^{43/48}\) diagonal; a second
transform returns the primal phase. The cellwise product transform is also
involutive, and its two literal truncated divisor orientations equal
\(r_2/4\) only after all profiles and truncations are deleted.

These results are certified partial estimates and scoped obstructions. The
complete \(Y^{1/2}\) determinant target, the \(5/16\) conditional local
moment consequence, both M9 components, endpoint uniformity, M9, and the
quarter theorem remain open. The internally proved exponent stays \(1/3\).

Accepted evidence:

- rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/synthesis.md;
- rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_actual_savings.md;
- rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_involution_product_and_source.md.

## Round 118 prescribed-centre wave envelope and coherent controls

For every frozen flat smooth unbalanced M2 component, the accepted
fixed-centre wave satisfies

\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^\varepsilon
 \min\left\{{D\over L},
 \sqrt{XL/D}+\sqrt{X/(LD)}\right\}.
\]

The first term is the literal real-centre product-window capacity. The
second follows from weighted reciprocal curvature before the outer
\(k\)-triangle. If \(a=\delta-\ell\), its exponent is

\[
 \min\left(a,{1-a\over2}\right).
\]

It saves a power over absolute capacity exactly for \(a>1/3\), but remains
strictly above \(1/4\) at every strict residual point.

A consecutive central-lobe selector in one odd residue class has the
uniform actual-scale bound

\[
 U\ll1+
 \begin{cases}
 (D^3/(XL))^{1/2},&D^3\ge C_0X,\\
 (D^4/(XL))^{1/3},&D^3<C_0X.
 \end{cases}
\]

Both branches are target-safe. On a uniformly smooth interior stationary
cell, the complete phase-one sector for integer \(X=bA^2\) is also
target-safe: it has \(O_\varepsilon(\sqrt M X^\varepsilon)\) modes and
contributes \(O_\varepsilon(\sqrt{D/L}X^\varepsilon)\). For square \(X\),
the literal \(\chi_4\)-weighted count is \(O(\sqrt M)\).

These are scoped upper bounds and countermodel obstructions. They do not
control disconnected runs, other coherent phases for real \(X\), the
nonsquare signed complement, or endpoint and transition kernels. The
complete joint \((r,k)\) selector before the \(k\)-triangle remains open,
as do complete UNBAL and all downstream M9 obligations. There is no
pointwise exponent change.

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/reviews/conductor_round118_curvature_run_and_scope.md;
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/reviews/conductor_round118_square_sector_seam.md.

## Round 119 separate direct-M1 parent minimax

For a residual M1 block put (a=\delta-\ell). On the active triangle the
accepted direct capacity exponent is

\[
 \min\left\{a,{1-a\over2},
 {89(1+\ell)+819\delta\over1282}\right\}.
\]

The elementary envelope is at most (1/3), with equality only at
(a=1/3). This global menu statement now has separate literal witnesses
on both open physical parents. Let (y=\lfloor\sqrt X\rfloor). The unique
hard profile (D_0=y) and the first smooth profile (D_1=y/2) each have
a full nonterminal frequency shell (L\asymp X^{1/6}). Their exponent
coordinates tend to ((1/2,1/6)), both remain strictly in
(\mathcal U_1), the two elementary rows are (X^{1/3+o(1)}), and the
TTY row tends to

\[
 {770\over1923}={1\over3}+{43\over641}.
\]

Hence the accepted direct-menu limsup is (1/3) separately on the hard
parent and the smooth parent. This is optimality of proved upper-bound
formulas, not a lower bound for either signed sum.

On the hard shell, the accepted transform has physical factor
(X^{1/4}L^{-3/2}). Thus normalized coefficient-blind capacity (L^2)
becomes physical (X^{1/4}L^{1/2}), while normalized target (L^{3/2})
becomes physical (X^{1/4}). At (L\asymp X^{1/6}), both the hard and
smooth parents miss by (X^{1/12}=L^{1/2}).

The exact adjacent-profile telescope retains the scale-dependent Vaaler
height differences and both boundary owners. Original physical scale
atoms have nonnegative scale weights multiplying a common character phase,
so equal deficits and raw profile addition supply no cancellation. The
canonical Gram has no block-local inverse, and GAR remains a total-active
alternative requiring both its lower-radial and radial/interface parents.

Both direct M1 analytic parents, both GAR parents, M9-M1, M9-M2, endpoint
uniformity, M9, and the quarter theorem remain open. The internal exponent
stays (1/3).

Accepted evidence:

- rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md;
- rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_capacity_and_labels.md;
- rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_connector_and_route_scope.md.

## Round 120 terminal-height completion of the nonlower radial sector

Put \(R=X^{1/4}\), \(Y=\sqrt X\),
\(D_j=2^{-j}\lfloor Y\rfloor\), and
\(H_j=\lfloor D_j/R\rfloor\). Fix \(0<s_0<8\), set
\(\kappa=\sqrt{s_0}/4\), and insert a fixed smooth factor
\(\vartheta(h/H_j)\), zero for \(h/H_j\leq\kappa/2\) and one for
\(h/H_j\geq\kappa\), into every nonempty literal \((j,h)\)-atom of the
global coefficient. Denote the result by \(\mathcal C_{T,X}^*(n)\).

The resulting reciprocal frequency weight is supported on
\(h\asymp_{s_0}H_j\) and has sampled sup-plus-variation
\(O_{s_0}(H_j^{-1})\). Since

\[
 {D_j\over2R}\leq H_j\leq{D_j\over R},
\]

the proved terminal divisor theorem bounds its positive antecedent by
\(O_{\varepsilon,s_0}(RX^\varepsilon)\). The coefficientwise positive
smooth and one-sided hard transforms give

\[
 \mathcal B_T^+
 ={e(1/8)\over i}R
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})+O_{s_0}(\log^2(2X)).
\]

The transform error is summed absolutely over the terminal heights, and
the hard cotangent boundary has \(O_{s_0}(1)\) weighted mass. Therefore

\[
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})\ll_{\varepsilon,s_0}X^\varepsilon.
\tag{120.1}
\]

For a nonzero stationary atom put \(s=n/Y\) and

\[
 t={2h\sqrt{X/n}\over D_j},\qquad
 {hR\over D_j}={t\sqrt s\over2}.
\]

The certified closed support is \(1/2\leq t\leq3/2\). Exact floor
inequalities then give

\[
 \mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)quad(s\geq s_0),
 \qquad
 \mathcal C_{T,X}^*(n)=0quad(s<s_0/144).
\tag{120.2}
\]

Let \(V_{\rm low}=1\) on \([0,s_0]\) and zero on
\([2s_0,\infty)\). An auxiliary fixed multiplier compact inside
\((0,16)\), inserted already on the reciprocal antecedent, makes the
\(V_{\rm low}\)-weighted terminal coefficient Mellin-admissible. The same
terminal and transform argument proves that weighted sum is
\(O_\varepsilon(X^\varepsilon)\). Since

\[
 (1-V_{\rm low})\mathcal C_X^*
 =(1-V_{\rm low})\mathcal C_{T,X}^*
\]

coefficientwise, including every floor, star and hard incidence, (120.1)
gives

\[
 \boxed{
 \sum_{n\leq N_X}^{*}(1-V_{\rm low}(n/Y))
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,s_0}X^\varepsilon.}
\tag{120.3}
\]

This is the whole nonlower complement. For the Round-98
lower--compact-critical--interface partition, exact subtraction of the
already proved compact critical cells yields the old sharp interface
owner. The physical endpoint prefix has constant endpoint phase and is not
identified with the radial collar. Endpoint-boundary and \(R_1\) modules
belong to an alternative route and occur zero times here.

Thus `M9-M1-global-radial-interface-estimate` is proved internally. The
sole remaining analytic GAR parent is the exact lower-radial signed
aggregate. GAR, blockwise M9-M1, every M9-M2 parent, endpoint uniformity,
M9, and the quarter theorem remain open, and the internal exponent stays
\(1/3\).

Accepted evidence:

- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/synthesis.md;
- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/reviews/conductor_round120_terminal_height_adjudication.md;
- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/reports/literal_radial_interface_reconciliation.md;
- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/reports/radial_interface_hostile_scope_audit.md.

## Round 121 full lower-profile flattening and sharp discrepancy return

Retain the Round-120 lower cutoff, chosen sufficiently small relative to
the certified fixed inactive-bottom support. With

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,
 \qquad D_j=2^{-j}y,\qquad H_j=\lfloor D_j/R\rfloor,
\]

the exact positive lower reciprocal antecedent is

\[
 \mathcal B_{\rm low}^+
 =\sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
\tag{121.1}
\]

On its joint radial/profile support, \(hR/D_j<1/2\), so the literal
floor has \(h\leq H_j\), the Vaaler argument obeys
\(h/(H_j+1)<1/2\), and the inactive bottom is absent. Replacing
\(\Phi\) by one therefore telescopes the active profiles exactly to the
sharp cutoff \({\bf1}_{d\leq y}\), including the one-sided hard sample.

The error uses

\[
 |\Phi(u)-1|\ll u^2,\qquad |\Phi'(u)|\ll u.
\]

On a dyadic shell \(h\asymp L\) its height BV is
\(O(L^{-1}(L/H_j)^2)\). A uniform high-regularity two-variable Fourier
separation of the coupled lower multiplier and the accepted
frequency-first theorem give

\[
 E_{j,L}\ll_{\varepsilon}X^\varepsilon
 (L/H_j)^2(1+D_j/L).
\]

Summing the height shells and profiles proves, for both signs,

\[
 \boxed{\mathcal B_{\rm low}^{\pm}
 =\mathcal B_{\rm flat}^{\pm}+O_\varepsilon(RX^\varepsilon),}
\tag{121.2}
\]

where

\[
 \mathcal B_{\rm flat}^+
 =\sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
\tag{121.3}
\]

This reduction covers the whole fixed lower radial cutoff. It retains the
accepted normalization

\[
 \mathcal B_{\rm low}^+={e(1/8)\over i}R G_{\rm low}(X)
 +O(\log^2X),
\]

so the reciprocal target is \(RX^\varepsilon\).

Let \(N=\lfloor X\rfloor\), changing only the phase. Absolute summation
over the supported heights gives

\[
 \mathcal B_{\rm flat}^+(X)
 =\mathcal B_{\rm flat}^{(N)}(X)+O(R).
\tag{121.4}
\]

Fix a sample-exact periodic interpolant

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t}
\]

on the small positive arc. For all integers \(m,k\), with \(d\mid0\),
put

\[
 A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d),
 \qquad c_y=\sum_{d\leq y}{\chi_4(d)\over d},
\]

and

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left(\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right).
\tag{121.5}
\]

Then exact finite Fourier completion, density subtraction, and two-sided
Abel summation give

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}D_N(k)
 \{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\}.}
\tag{121.6}
\]

The interpolation seminorms grow with \(y\), so fixed-\(X\) Schwartz
decay proves convergence but no uniform estimate. Equations
(121.2)--(121.6) are a bidirectional target-scale equivalence.

Exact adjacent mod-four pairing separately gives

\[
 \mathcal B_{\rm low}^+=\mathcal E_{\rm amp}+\mathcal K_X,
 \qquad \mathcal E_{\rm amp}\ll\log^2X,
\]

where

\[
 \mathcal K_X=\sum_{d\equiv1(4)}\sum_h{b_X(h,d+2)\over h}e(hX/d)
 \left\{1-e\!\left(-{2hX\over d(d+2)}\right)\right\}.
\tag{121.7}
\]

The flat amplitude seam is \(O(\log X)\). The narrow integer-increment
sector is target-safe, but for fourth powers \(X=R^4\), disjoint
half-integer resonance tubes with \(d\asymp R^2\) and
\(R^{4/5}\leq h\leq cR\) have total post-tube-modulus capacity
\(\gg R^{3/2}\). Hence local, pairwise, or resonance-tubewise absolute
closure loses \(R^{1/2}\). This is not a signed lower bound; the missing
theorem is joint cancellation across all heights and resonance labels.

Thus the exact lower-radial signed estimate remains open and is the sole
GAR analytic parent. GAR, both direct M1 parents, all three M2 parents,
endpoint uniformity, M9, and the quarter theorem remain open. The internal
exponent stays \(1/3\).

Accepted evidence:

- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/reviews/conductor_round121_flattening_and_pairing_adjudication.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/reports/blind_lower_height_kernel_rederivation.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/reports/literal_character_paired_height_kernel_attack.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/reports/lower_height_kernel_hostile_audit.md.

## Round 122: localized low-two-adic survivor and complement no-go

For the exact Round-121 difference wavelet, put

\[
 W(k)=\widehat J(k)-\widehat J(k+1),\qquad
 K_\delta=yX^\delta,\qquad 0<\delta<\frac18.
\]

The removable-pole kernel (J(t)(1-e(-t))) has the uniform envelope

\[
 |W(k)|\ll_A\frac1{R+|k|}
 \left(1+\frac{|k|}{y}\right)^{-A},
\quad
 \sum_k|W(k)|\ll\log X,
\quad
 \sum_k|kW(k)|\ll y.
\tag{122.1}
\]

The far range (|k|>K_\delta), central range (|k|\leq R), all
cumulative increments with (v_2\geq A_0=\lceil\log_2R\rceil), and the
odd positive-character central divisor correction are each
(O_{\varepsilon,\delta}(RX^\varepsilon)).

For (m=2^an>0), (n) odd, define

\[
 a(n)=\sum_{d\mid n}\chi_4(d)=\frac{r_2(m)}4,\qquad
 T_z(n)=\sum_{\substack{q\mid n\\q<z}}\chi_4(q).
\]

The complete boundary-exact complement is

\[
 \boxed{A_y(2^an)=a(n)-\chi_4(n)T_{n/y}(n).}
\tag{122.2}
\]

For (chi_4(n)=-1), (a(n)=0) and (A_y=T_{n/y}), an exact
self-return.  For (chi_4(n)=1), the identity leaves one half of the
full (r_2/4) coefficient plus its exact central band.  At (n=y^2),
the fixed divisor is counted once:

\[
 2A_y(y^2)=a(y^2)+\chi_4(y).
\tag{122.3}
\]

Define, on the positive localized window,

\[
 \mathscr V_\delta(2^an)=
 \begin{cases}
  a(n)/2,&a=0,\ \chi_4(n)=1,\\
  T_{n/y}(n),&a=0,\ \chi_4(n)=-1,\\
  a(n)-\chi_4(n)T_{n/y}(n),&1\leq a<A_0,\\
  0,&a\geq A_0.
 \end{cases}
\]

With (mathcal I_k) the exact oriented interval from (N) to (N+k),
all centering and overlap seams give

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}
 W(k)\mathcal I_k\mathscr V_\delta
 +O_{\varepsilon,\delta}(RX^\varepsilon).}
\tag{122.4}
\]

The survivor in (122.4) remains unestimated and has absolute capacity
(R^2).  Completing the full circle coefficient and subtracting the
complement reconstructs the original sharp cone.  Thus Round 122 proves a
strict reduction and a mechanism no-go, not the lower-radial estimate.
GAR, both direct M1 parents, all M2 parents, endpoint uniformity, M9, and
the quarter theorem remain open.  The internal exponent remains (1/3).

Accepted evidence:

- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md;
- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reviews/conductor_round122_complement_adjudication.md;
- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reports/blind_near_square_divisor_involution.md;
- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reports/literal_two_adic_complementary_divisor_attack.md;
- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reports/near_square_complement_hostile_audit.md.

## Round 123: integer-centred shifted near-alias reduction

For one literal flat-smooth strict-UNBAL row, write

\[
 \mathscr R_X=
 \sum_{r\ \mathrm{odd}}\chi_4(r)W(X/(rD))
 \sum_k\frac{q_L(4Xk/r^2)}{k}e(Xk/r),
\]

where \(D=X^\delta\), \(L=X^\ell\), \(R=X/D\), and
\(K=XL/D^2\).  If \(\mathscr R_M^\sharp\) changes only the phase centre
to an integer \(M\asymp X\), while every amplitude and the physical
denominator \(4X\) remain frozen, then

\[
 |\mathscr R_X-\mathscr R_M^\sharp|
 \ll_\varepsilon(1+|M-X|)X^\varepsilon.
\tag{123.1}
\]

The proof differentiates the physical product kernel.  Its \(L/D\) cost
is paired with a uniform divisor layer cake of effective length \(D/L\),
including zero-product and negative-product tails.  A reciprocal
termwise perturbation, which may cost \(K\), is not used.

For the unique nearest alias \(j\), define

\[
 E=M(s-r)-jrs,\qquad u=M-jr,\qquad v=M+js.
\]

There is no half-integer tie, and for \(M=2^tM_0\), \(M_0\) odd,

\[
 M(1/r-1/s)=j+\frac{E}{rs},\qquad
 uv-M^2=jE,\qquad
 \chi_4(r)\chi_4(s)=(-1)^{(jrs+E)/2^{t+1}}.
\tag{123.2}
\]

For \(j\ne0\), the factor map is exact only with all congruences,
orientations, supports, and literal profiles retained.  It degenerates at
\(j=0\).  Across every nonzero alias, all exact collisions \(E=0\) total
only \(O_\varepsilon(X^\varepsilon)\); defects beyond
\(X^{1+\rho}/L\) are rapidly small.

In the exact shifted length-\(H\) block square, the ordered-pair kernel
satisfies

\[
 |\Gamma_{M,H}(r,s)|\ll_A
 \psi_H(M/r)\psi_H(M/s)
 \left(1+K\|M(1/r-1/s)\|\right)^{-A},
\tag{123.3}
\]

where \(\psi_H(x)=\min(1,(H\|x\|)^{-1})\), and

\[
 \sum_{r\asymp R}\psi_H(M/r)^2
 \ll_\varepsilon(1+R/H)X^\varepsilon.
\tag{123.4}
\]

Therefore the complete \(j=0\) sector, including all shifted
self-correlations and off-diagonal zero aliases, is

\[
 \sum_{j(r,s)=0}|\Gamma_{M,H}(r,s)|
 \ll_\varepsilon(1+R/H)X^\varepsilon.
\tag{123.5}
\]

At \(H_0=\lceil X^{1/2}/D\rceil\), this reaches the shifted square
target.  It follows that for each fixed \(\eta>0\), any violation
\(|\mathscr R_X|\geq X^{1/4+\eta}\) forces a positive-real contribution
\(\gg X^{1/2+2\eta}\) in the complete actual-sign sector

\[
 j\ne0,\qquad E\ne0,\qquad |E|\leq X^{1+\eta/10}/L.
\tag{123.6}
\]

Both reciprocal selectors, all shifts, profiles, endpoints, alias
orientations, and character signs remain in (123.6).  This is one-way and
fixed-power; it does not prove the threshold estimate.

Finally, transverse Poisson summation has active modes
\(\nu=m-\sigma/4\asymp L\).  In the opposite character channel,

\[
 \partial_r\Phi+m=-\frac{Mh+\nu(s^2-r^2)}{r^2}.
\tag{123.7}
\]

For a nonempty alias range, an allowed \(|h|<H_0\) makes (123.7) vanish
at an interior point with second derivative \(\asymp L|j|/X\).  This
rejects the uniform fixed-alias Kusmin--Landau premise but supplies no
modal or global lower bound.  The remaining theorem is the complete
signed nonzero, nonexact near-alias aggregate in (123.6).

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/conductor_round123_integerization_gram_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/hostile_shifted_zero_alias_addendum.md;
- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/hostile_alias_curve_no_go_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reports/blind_integer_gram_rederivation.md;
- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reports/signed_alias_product_attack.md.

## Round 124: unmasked double-character stationary off-product reduction

For the complete unmasked zero-extended flat-smooth row at the Round-123
integer centre, define

\[
 \widetilde A(k)=e(-1/8)M^{1/4}k^{-3/4}
 \sum_{p>0\atop p\text{ odd}}\chi_4(p)p^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)
 q_L((X/M)p)e(\sqrt{Mkp}).
\]

Character Poisson and uniform scalar stationary phase, with all smooth
entries, exits, inactive modes, and the exact block zero extension, give

\[
 \mathcal F_{M,H_0}[A]
 =\mathcal F_{M,H_0}[\widetilde A]+O(1).
\tag{124.1}
\]

The transformed phase is

\[
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\}.
\tag{124.2}
\]

Its complete principal product-equality sector is exactly
\(p=q,h=0\), and its mass is \(O(X^{1/2})\).  Let
\(\mathcal S_{\rm eq}^{\ne0}\) denote the full actual-sign sector
\(p=q,h\ne0\), and let \(\mathcal S_{\rm neq}\) denote \(p\ne q\).
If \(\mathcal Q_{\rm safe}\) is the complete Round-123 physical safe
package, then

\[
 \mathcal V_{M,H_0}
 =\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
  +(\mathcal D_0-\mathcal Q_{\rm safe})+O(1),
 \qquad
 \mathcal Q_{\rm safe}\ll_\varepsilon X^{1/2+\varepsilon}.
\tag{124.3}
\]

Therefore the physical survivor is target-equivalent, modulo accepted
packages, to one complete dual off-product aggregate.  Every fixed-power
violation forces that aggregate and hence at least one of its two complete
sectors.  This is an inverse reduction, not their estimate.

The phase product defect and gradient numerator are distinct:

\[
 \mathcal N=p(k+h)-qk,\qquad
 \mathcal G=pk-q(k+h)=\mathcal N-(p+q)h,
\]

\[
 \partial_k\Theta
 =\frac{\sqrt M\,\mathcal G}
 {2\sqrt{k(k+h)}\{\sqrt{pk}+\sqrt{q(k+h)}\}}
 =M(1/r_*-1/s_*).
\tag{124.4}
\]

Thus, for an integer alias \(j\),

\[
 E_*=M(s_*-r_*)-jr_*s_*
 =r_*s_*\{\partial_k\Theta-j\}.
\tag{124.5}
\]

Every exact \(k\)-saddle has \(E_*=0\), while the physical \(E\ne0\)
projector is a coupled discrete collar and is not transported termwise by
rowwise Poisson.  Equation (124.3) is the lawful connector.

On fixed \((k,h)\)-interiors the joint Hessian is nondegenerate and the
Legendre phase is

\[
 \Theta-jk-dh=jk+dh
 =\frac M4\left(\frac p d-\frac q{d-j}\right),
\tag{124.6}
\]

returning the primal reciprocal phase.  Its unsigned principal capacities
\(D^2\) and \(D^2/L\) are only diagnostics; no lower bound or complete
joint endpoint transform is accepted.  The remaining target is

\[
 \mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
 \ll_\varepsilon X^{1/2+\varepsilon}.
\tag{124.7}
\]

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reviews/conductor_round124_stationary_lattice_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reports/blind_joint_stationary_lattice_rederivation.md;
- rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reports/double_poisson_product_defect_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reports/joint_stationary_lattice_hostile_audit.md.

## Round 125: one-sided actual-character energy and sectorization obstruction

For the literal Round-124 zero-extended dual rows, put

\[
 B_{p,n}=\sum_{a=0}^{H-1}b_{p,n+a},\qquad
 \mathcal E_{\rm eq}=C_H\sum_{p,n}|B_{p,n}|^2,
\]

\[
 \mathcal E_\chi=C_H\sum_n
 \left|\sum_{p>0\atop p\text{ odd}}\chi_4(p)B_{p,n}\right|^2.
\]

Exact Fejer expansion, with every entry and exit handled by zero
extension, gives

\[
 \mathcal E_{\rm eq}=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0},
 \qquad
 \mathcal E_\chi=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
 +\mathcal S_{\rm neq}.
\tag{125.1}
\]

Hence

\[
 \mathcal S_{\rm off}=\mathcal E_\chi-\mathcal D_0,
 \qquad
 \mathcal S_{\rm neq}=\mathcal E_\chi-\mathcal E_{\rm eq}.
\tag{125.2}
\]

Since $\mathcal E_\chi\ge0$ and
$\mathcal D_0\ll X^{1/2}$, the negative side of the complete dual
survivor is target-safe. Its absolute square-target estimate is equivalent
to the single positive upper bound

\[
 \boxed{\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{125.3}
\]

Together with Round 124,

\[
 \mathcal V_{M,H}=\mathcal E_\chi-\mathcal Q_{\rm safe}+O(1),
 \qquad
 \mathcal Q_{\rm safe}\ll_\varepsilon X^{1/2+\varepsilon}.
\tag{125.4}
\]

Thus any fixed-power failure of this flat-smooth physical owner is
positive and is an excess of (125.3), modulo proved packages. This is a
target-equivalent sign localization, not the missing estimate.

The two dual sectors cannot be separated coefficient-blindly. Two
identical long smooth rows supported on opposite $\chi_4$-classes can
have

\[
 |\mathcal S_{\rm eq}^{\ne0}|,
 |\mathcal S_{\rm neq}|\gg H\mathcal D_0,
 \qquad
 \mathcal S_{\rm off}=-\mathcal D_0.
\tag{125.5}
\]

This is a structural adversary, not a physical counterexample. It proves
that Fejer positivity, support, coefficient sizes, zero extension, and
character magnitudes alone cannot justify separate target estimates.

The complete elementary fixed-row estimate is

\[
 \mathcal E_{\rm eq}
 \ll_\varepsilon X^\varepsilon
 \min\left\{\frac XD,\frac{D^2}{L}\right\}
 =X^{1/2+\varepsilon}\min\{H,Q\}.
\tag{125.6}
\]

Both $H$ and $Q=D^2/(L\sqrt X)$ tend to infinity. The reciprocal
$Q$-loss is the better elementary ledger only for $Q\le H$; in the
opposite regime the original $H$-term triangle is smaller.

On strict block interiors, the $k$-B-process has principal coefficient
$-2i/p$, returned profile $W(Xd/(DM))q_L((X/M)p)$, and $Q$
dual labels. A second B-process returns the original block. Odd-$p$
coherence in the squared reciprocal packet requires

\[
 E_d^*=M(d'-d)-2Add',
\]

\[
 e\!\left(\frac{Mp(d'-d)}{4dd'}\right)
 =(-1)^Ae\!\left(\frac{pE_d^*}{4dd'}\right),
 \qquad
 (M-2Ad)(M+2Ad')-M^2=2AE_d^*.
\tag{125.7}
\]

The former $4a$ lattice misses odd half-integer aliases. At fixed
$(n,d,d')$, the literal saddle selectors leave a $p$-window of
length $D^2H/X\asymp1/H$, not $L$. Summing $n$ first creates a
moving floor overlap with unpriced faces and aggregate errors. Therefore
the proposed far deletion and complete nonzero-near defect survivor are
not proved, and the reciprocal formula remains a strict-interior
principal module rather than an endpoint-complete transform.

The exact parked flat-smooth UNBAL survivor is (125.3). Its upper bound,
every other UNBAL owner, hard TOP, BAL, complete M9-M2, both M1 routes,
endpoint uniformity, M9, and the quarter theorem remain open. The internal
exponent remains $1/3$.

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reviews/conductor_round125_dual_sector_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reports/blind_dual_offproduct_sector_rederivation.md;
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reports/actual_symbol_dual_sector_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reports/dual_offproduct_hostile_audit.md.

## Round 126: a power-safe square-entry sector and parity-spectral obstruction

Let (A_L) be the literal hard-TOP matrix

\[
 A_L(m,h)=1_{h\in\mathscr H_L}1_{m\le h\le4m}
 a_{\rm end}(h,m)e(\sqrt{Xhm}),
\]

so that

\[
 \mathcal E_L^{\rm top}=\|A_L\chi\|_2^2,
 \qquad \mathcal D_L=\|A_L\|_{\rm HS}^2\ll L^2.
\]

The genuinely noninvertible square-product entry projection

\[
 A_L^{\square}(m,h)=1_{hm\text{ is a square}}A_L(m,h)
\]

is target-safe with a power margin.  Uniformly for (|c_h|\le1),

\[
 \boxed{\|A_L^{\square}c\|_2^2
 \ll_\varepsilon L^{3/2}X^\varepsilon,}
 \tag{126.1}
\]

and

\[
 \|A_L^{\square}\|_{\rm HS}^2
 \ll_\varepsilon L\log(2L)X^\varepsilon.
 \tag{126.2}
\]

Indeed, writing (m=du^2) with (d) squarefree forces (h=dv^2),
and the hard cone gives (u\le v\le2u).  Summing the squared row
cardinalities gives (L^{3/2}\sum_dd^{-3/2}\).  This condition is on
individual entries before the energy expansion and is distinct from the
previously owned primitive (ab=\square) off-diagonal family.

The lawful reduction is only

\[
 \|A_L\chi\|_2
 \le \|A_L^{\square}\chi\|_2
      +\|A_L^{\rm ns}\chi\|_2,
 \qquad A_L^{\rm ns}=A_L-A_L^{\square}.
 \tag{126.3}
\]

The two entry projections are not orthogonal after application to the
character, so no energy cross term is deleted.

Enumerate odd heights by (h=h_0+2t) and put (z_t=v_h).  Then

\[
 \mathcal E_L^{\rm top}=\|\widehat z(\pi)\|_2^2,
 \qquad
 {1\over2\pi}\int_0^{2\pi}\|\widehat z(\theta)\|_2^2d\theta
 =\mathcal D_L.
 \tag{126.4}
\]

The exact high-pass

\[
 2\sum_t(-1)^tz_t=\sum_t(-1)^t(z_t-z_{t+1})
\]

has multiplier (1-e^{i\theta}), of modulus (2) at the selected
frequency (pi).  Its selected energy is therefore exactly
(4\mathcal E_L^{\rm top}), not a contraction.  Any finite height-only
filter either retains (pi) and is equivalent on the target mode, or
kills (pi) and requires a separate estimate.

With (V e_h=v_h), (G=V^*V), (N=|\mathscr H_L|), and
(u_\chi=N^{-1/2}\chi),

\[
 \mathcal E_L^{\rm top}=N\langle Gu_\chi,u_\chi\rangle,
 \qquad \mathcal D_L=\operatorname {tr}G.
 \tag{126.5}
\]

Column multiplication by (operatorname {diag}(\chi_4(h))) is unitary,
so ambient operator, Schatten, Frobenius, Schur, and coefficient-uniform
Bessel estimates do not see character insertion.  The missing theorem is
the fixed actual-direction estimate

\[
 \langle Gu_\chi,u_\chi\rangle
 \ll_\varepsilon {L^2X^\varepsilon\over N},
 \tag{126.6}
\]

on the nonsquare complement, or the equivalent one-sided global real
scalar.  A common-interior bounded adversary attains diagonal capacity
(L^2) and parity energy (L^3); it is a method obstruction, not a
physical lower bound.

Finally, if

\[
 \Delta=\mathcal E_L^{\rm top}-\mathcal D_L>0,
\]

then one complete dyadic physical-offset shell has real signed mass at
least (Delta/O(\log L)).  A separate direct partition yields the same
statement for a primitive-(q) shell.  Every lift, ceiling, reciprocal
interval, collar, floor, star, metric centre, entry, exit, and one-count
slab remains joint.  This is a one-way inverse localization and proves no
bound on the selected shell.  Round 110 is only a global real-part
completion connector, not a shellwise one.

The square-entry sector is closed, but the nonsquare hard-TOP vector,
complete hard TOP, BAL, every UNBAL owner, M9-M2, both M1 routes,
endpoint uniformity, M9, and the quarter theorem remain open.  The internal
exponent remains (1/3).

Accepted evidence:

- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/synthesis.md;
- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/reviews/conductor_round126_adjudication.md;
- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/reports/blind_hard_top_vector_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/reports/hard_top_parity_spectral_operator_attack.md;
- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/reports/hard_top_actual_vector_hostile_audit.md.

## Round 127: frontier selection and a conditional local-lift connector

The full-proof strategy selection gate compared the exact nonsquare
hard-TOP vector, the Round-122 lower-GAR wavelet, and the
\(W=Y^{7/16}\) graded determinant correlation.

At the hard-TOP statement interface, support, joint phase, and bounded
coefficients cannot yield the missing factor.  For row supports \(S_m\),
arbitrary phases \(\phi_{m,h}\), and a unit direction \(c_h\),

\[
 \sup_{|a_{m,h}|\le1}
 \sum_m\left|\sum_{h\in S_m}a_{m,h}e(\phi_{m,h})c_h\right|^2
 =\sum_m|S_m|^2.
\]

This remains \(\asymp L^3\) on a hard-cone rectangle after deleting all
\(hm=\square\) entries.  Product-fibre averaging is noninvertible but
fixes \(F(m,h)=f(mh)\), so it does not contract the aligned component.
This is a coefficient-interface obstruction, not a physical lower bound.

For lower GAR, the uncentered square function is false: the actual drift
\(kc_y\) gives energy \(\gg y^3\) on \(K\asymp y\).  Centering is
mandatory and scalar-equivalent because the wavelet's full first moment
vanishes.  The centered \(k\)-energy that would imply the target is a
stronger separated norm.  Its exact reduced-Farey expansion has a
target-safe equal-fraction diagonal, but the prescribed-centre nonzero
determinant still asks for the entire missing factor \(y\).  The ambient
canonicalization supplies no gain.

At the graded critical block, the scalar-cell continuation gives exactly
\(Y^{37/48+\varepsilon}\) and is parked.  A new conditional connector is
available.  If the literal complete lift coefficient over one moving
reciprocal window satisfies

\[
 \|U_{i,\rho}\|_{V^2(I)}
 \ll_\varepsilon \frac{J_B^{1/2}}{L}Y^\varepsilon,
 \qquad J_B=1+\frac{DQ_B}{B^2},
\]

and if the unseparated reciprocal sum satisfies the corresponding
\(V^2\)-weighted curvature inequality without a window-length square-root
loss, then the complete correlation is

\[
 O_\varepsilon(Y^{73/96+\varepsilon}),
\]

a strict \(Y^{1/96}\) fixed-block improvement.  Both hypotheses are
open.  Even their success gives persistence exponent
\(115/288>1/3\), so it would not improve the global theorem.

Round 128 therefore tests only the literal local lift-coefficient
variation first.  No M1 or M2 parent, endpoint uniformity, M9, global
exponent, or quarter theorem changes in Round 127.

Accepted evidence:

- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/synthesis.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/blind_hard_top_nonsquare_feasibility.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/lower_gar_wavelet_feasibility.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md.

## Round 128: character-split local lift square variation

The finite coefficient half of the Round-127 connector is now proved.  Let
\(P\) be a zero-extended sampled-BV frequency factor supported on
\(g\asymp G\), let \(w\) be a zero-extended sampled-BV denominator
profile supported on \(d\asymp D\), and assume \(|a|G\asymp L\).  On a
progression \(b'=\rho v\asymp B\) contained in a physical window of
\(b'\)-length \(Q\), set

\[
 R(v)={1\over a}\sum_g{\chi_4(g)\over g}P(g)w(g\rho v).
\]

Interval-uniform Abel summation gives

\[
 \sup_J\left|\sum_{g\in J}{\chi_4(g)\over g}P(g)\right|
 \ll G^{-1}.
\]

Writing \(c_t=w(t)-w(t+1)\), the exact discrete Stieltjes identity

\[
 w(d)=\sum_{t\ge d}c_t,
 \qquad \sum_t|c_t|=\operatorname {Var}(w)
\]

expresses \(R\) as a bounded-mass superposition of partial lift sums with
endpoint \(\lfloor t/(\rho v)\rfloor\).  This floor changes on at most
\(O(1+DQ/B^2)\) steps.  Each value and each nonzero difference is
\(O(L^{-1})\) by the interval Abel bound.  Minkowski in the vector of the
left endpoint, consecutive differences, and right endpoint proves

\[
 \|R\|_{V^2(I)}
 \ll {1\over L}\left(1+{DQ\over B^2}\right)^{1/2}.
 \tag{128.1}
\]

The accepted Round-95 M1/M2 coefficients have exactly this separable
form: \(P=\Phi v_L\) is frequency-only and \(w=\omega_{i,D}\) is
denominator-only, with every literal support, hard sample, and star
included.  The determinant taper and half-open reduced-denominator shell
are bounded-BV multipliers, and divisor progressions cost only
\(Y^\varepsilon\).  Thus (128.1), with
\(Q=Q_B\) and \(J_B=1+DQ_B/B^2\), holds for the two M1 quarter-phase
branches and the one M2 branch.

The branch qualification is mandatory.  Leaving the reduced M1 character
\(\chi_4(b')\) inside the amplitude gives a literal top-shell one-lift
norm \(\gg Q_B^{1/2}/L\) while \(J_B\asymp1\).  The exact identity
\(\chi_4(b')=(e(b'/4)-e(-b'/4))/(2i)\) transfers this dense alternation
to the two carrier phases.  Conversely, the common lift character must
remain inside the lift sum; pointwise size, a birth count, and character
notation alone admit phase-conjugating fixed-window countermodels.

The joint branchwise reciprocal-curvature inequality remains open.  A
generic partial-summation/Cauchy proof inserts \(N_\rho^{1/2}\), so the
proved coefficient norm does not imply the conditional
\(Y^{73/96+\varepsilon}\) correlation bound.  No global exponent or M9
status changes.

Accepted evidence:

- rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/synthesis.md;
- rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reviews/conductor_round128_literal_v2_adjudication.md;
- rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/blind_local_v2_feasibility.md;
- rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/literal_lift_coefficient_variation_attack.md;
- rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/local_variation_hostile_audit.md.

## Round 129: direct Stieltjes birth-block curvature and complete all-shell saving

The completed-\(V^2\)-norm formulation is false.  Its exact dual is the
variance of all prefix sums, equivalently the Dirichlet path Green kernel

\[
 (L_N^{-1})_{jk}={\min(j,k)(N+1-\max(j,k))\over N+1}.
\]

A real one-lift triangular sampled-BV profile centered at a reciprocal
integer-derivative alias violates \(|S(U)|\ll\|U\|_{V^2}K\) by
\(Y^{1/48}\), with both endpoint values zero.  The two M1 quarter shifts
do not remove the obstruction.

The physical sum has a different direct proof.  Put

\[
 \Lambda_\rho=\lambda_B\rho^2,\quad
 N_\rho\asymp Q_B/\rho,\quad
 K_\rho=\min\!\left(N_\rho,
 N_\rho\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2}\right).
\]

For each exact M1/M2 branch and divisor progression,

\[
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right)\right|
 \ll_\varepsilon {K_\rho\over L}Y^\varepsilon.
 \tag{129.1}
\]

Freeze one exact Stieltjes threshold, Abel-sum the common lift character
before a modulus, and partition by the literal floor
\(\lfloor t/(\rho v)\rfloor\).  Weighted second-derivative summation on
these plateaux costs
\(N_\rho\sqrt{\Lambda_\rho}+J_B\Lambda_\rho^{-1/2}\).  The identities

\[
 N_\rho\Lambda_\rho\asymp L\rho(J_B-1),
 \qquad N_\rho\Lambda_\rho\ge D/W
\]

absorb every nonconstant plateau endpoint.  Recombine thresholds only
after this estimate, using their bounded total mass.  Equality stars are
divisor-many; taper, floors, clipping, stationary aliases, M1 quarter
phases, the M2 character, Möbius progressions, and shell owners are all
included.

The divisor sum gives inner cost \(K_B/L\), where

\[
 K_B=\min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right).
\]

The accepted outer ledger gives \((LD)L L^{-1}(K_B/L)=DK_B\).  Uniformly
for \(1/3\le\log_YB\le1/2\), \(K_B\ll Y^{11/48}\), and therefore

\[
 |\mathfrak O_i|\ll_\varepsilon Y^{35/48+\varepsilon}.
 \tag{129.2}
\]

This extends the old top-shell exponent to the complete block and improves
the former complete \(Y^{37/48}\) envelope by \(Y^{1/24}\).  It remains
\(Y^{11/48}\) above target and persists only to \(7/18>1/3\), so no
global exponent or M9 status changes.

Accepted evidence:

- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/synthesis.md;
- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reviews/conductor_round129_direct_curvature_adjudication.md;
- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reports/actual_stieltjes_reciprocal_sum_attack.md;
- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reports/blind_structured_v2_curvature_feasibility.md;
- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reports/reciprocal_curvature_hostile_audit.md;
- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reviews/hostile_birth_block_curvature_addendum.md;
- rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reviews/post_blind_absolute_curvature_outer_ledger.md.

## Round 130: shell support refinement and the exact top-shell residual

The Round-129 inner theorem combines with a sharper physical support
count.  On a half-open reduced-denominator shell $b'\asymp B$, an exact
Stieltjes-recombined complete-lift coefficient is nonzero only when

\[
 gb'\asymp D,
 \qquad g|a'|\asymp L.
\]

Hence

\[
 g\asymp D/B,
 \qquad |a'|\asymp LB/D,
 \qquad \#\{a'\}\ll LB/D.
\]

The support statement is made after threshold recombination, not for each
separate Stieltjes atom.  The accepted outer coefficient bounds give

\[
 \sum_r|A_i(r)|
 \le (LD)^{1/2}(D/L)^{1/2}\ll D.
\]

Applying the numerator and outer triangles only after the fixed-
$(r,a')$ estimate $K_B/L$ yields

\[
 |\mathfrak O_{i,B}^{+}|
 \ll_\varepsilon
 D{LB\over D}{K_B\over L}Y^\varepsilon
 =BK_BY^\varepsilon.
\tag{130.1}
\]

Thus every lower shell gains $B/D$.  Since
$K_B=Y^{11/48+o(1)}$ throughout $D/L\le B\le D$, the smallest shell
costs $Y^{9/16+o(1)}$, while the top shell remains
$Y^{35/48+o(1)}$.  Consequently (129.2) remains the complete best bound,
but its entire exponent-critical residual is now localized to
$B\asymp D$.

The remaining positive-energy normalization is exact but stronger than
the physical scalar.  If $H$ is the literal post-inner incidence map,

\[
 F=H\mathbf1,
 \qquad E_{\rm res}=\mathbf1^*H^*H\mathbf1.
\]

After physical primitive reassembly the same resolved energy is
$b^*K_{B,+}^*K_{B,+}b$.  The complete symmetric triangular operator
$G$ instead satisfies $\lVert Gb\rVert_2^2=b^*G^2b$.  Shell, orientation,
diagonal, and mixed cross terms prevent any automatic identification or
positive-order comparison.  A support- and norm-matched aligned control
has energy $LDK_B^2$ and scalar size $DK_B$, proving that marginal norms
alone cannot supply the missing factor.  This is not a lower bound for the
actual coefficient.

For one fixed primitive top-shell outer ray, put $a'=a+p$, $b'=b+q$.
Then

\[
 n=ab'-a'b=aq-bp,
 \qquad n\equiv-bp\pmod {|a|},
 \qquad b'={b(a+p)+n\over a}.
\tag{130.2}
\]

When the physical $p$-support has span $O(|a|)$, fixed $n$ has $O(1)$
admissible $p$-lifts.  This is a fixed-outer-ray, primitive top-shell
statement after Möbius reassembly.  It rejects an independent square-root
gain from $p$, but does not prove cancellation of the induced M1/M2
residue weights.

Exact Stieltjes, Möbius, and complete-lift inversion restores the original
all-owner product wave: M1 returns $\chi_4(d')$, and M2 retains
$\epsilon_{\rm sgn}\chi_4(|h'|)$.  The accepted complete product-window
theorem then gives only $Y^{37/48+\varepsilon}$.  On the isolated top
shell, $p$-first modulus gives $D^2/L=Y^{40/48}$, while an aliaswise
two-variable unit-Hessian transform gives $DQ_*=Y^{43/48}$.  These
positive-norm continuations are parked.

The first open graded assertion is therefore the literal signed
$B\asymp D$ scalar with all outer coefficients, determinant residue
weights, thresholds, reciprocal aliases, characters, and owners retained.
Any fixed saving is new local progress; the full target requires
$Y^{11/48}$.  No global exponent or M9 status changes.

Accepted evidence:

- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/synthesis.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/conductor_round130_post_inner_adjudication.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reports/actual_numerator_increment_recombination_attack.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reports/blind_outer_bilinear_dual_feasibility.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reports/outer_ray_bilinear_hostile_audit.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/independent_shell_refinement_and_inversion_audit.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/blind_post_unmask_outer_gram_seam.md;
- rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/hostile_determinant_residue_gram_addendum.md.

## Round 131: fixed-lift primitive residue kernel and terminal cross-ray residual

Fix one primitive top-shell outer ray \((a,b)\), one physical increment
\(p\), put \(m=a+p\), and write \(n=aq-bp\). After physical primitive
support is established, let \(M=|m|_{\rm odd}\). The stripped M1
support-character mask

\[
w_{1,m}(q)=\chi_4(b+q)\mathbf1_{(M,b+q)=1}
\]

has minimal \(q\)-period \(4\operatorname{rad}(M)\), admits completion
modulus \(4M\), and has normalized transform

\[
\widehat w_{1,m}(k)=
{e(kb/(4M))\over4M}G_{4,M}(k)c_M(k).
\tag{131.1}
\]

The fixed mod-four Gauss factor vanishes for even \(k\) and has magnitude
two for odd \(k\). In particular,

\[
\widehat w_{1,m}(0)=0,
\qquad
|\widehat w_{1,m}(M)|=|\widehat w_{1,m}(3M)|
={\varphi(M)\over2M}.
\tag{131.2}
\]

The two strong coefficients give the determinant quarter frequencies
\(1/(4a)\) and \(3/(4a)\); all other odd Ramanujan modes remain.

For active odd \(m\), the stripped M2 mask has transform

\[
\widehat w_{2,m}(k)=
{\epsilon_{\rm sgn}\chi_4(|m|)\over|m|}
e(kb/|m|)c_{|m|}(k),
\tag{131.3}
\]

and its fixed-\(p\), \(q\)-arithmetic zero coefficient is

\[
\widehat w_{2,m}(0)=
\epsilon_{\rm sgn}\chi_4(|m|){\varphi(|m|)\over|m|}.
\tag{131.4}
\]

This is a Fourier coefficient, not the determinant point \(n=0\). Both
normalized Fourier \(\ell^1\) costs are divisor-sized.

These are stripped support-mask identities only. The weighted physical
Möbius atoms retain \(\rho\)-dependent profiles, stars, and owners, so the
bare primitive-incidence identity does not factor the full coefficient.
After post-reassembly support expansion, the weakest determinant atom periods
are \(|a|\operatorname{lcm}(4,\rho)\) for M1 and \(|a|\rho\) for M2.
Since \(m=a+p\) varies and natural numerator order is permuted in determinant
order, no common \(4|a|\)-periodic, target-cost BV factorization is proved.

For active M2, the interlaced outer/inner character product becomes a single
quarter mode only when \(b\) is odd and \(q\bmod4\) is fixed. Even \(b\)
retains an extra two-adic coordinate whose completion factor may be a power
of \(Y\). Hence there is no universal M2 shifted mode.

The legal one-sided same-denominator packets have \(n>0\) and length
\(R=D/W=Y^{3/48}\). One packet has capacity \(Y^{30/48+o(1)}\); the
\(O(1+WL/D)\) packet cover returns \(Y^{35/48+o(1)}\) only as worst-case
upper capacity. These packets refute character-forced per-ray vanishing but
do not align the actual outer family. The statement-only \(p=q=n=0\)
construction is outside the one-sided scalar and is rejected.

The exact finite arithmetic is fixed-modulus-four Gauss-times-Ramanujan, not
a growing quadratic-Gauss or Salié sum. Even ideal one-term-per-ray collapse
reaches only \(DK_D/L=Y^{27/48}=Y^{9/16}\). A strict global improvement
therefore needs a genuine cross-ray power, and the determinant target needs
an additional \(Y^{-1/16}\) after that ideal per-ray collapse.

The first open object remains the actual signed variable-modulus family
scalar with every threshold, profile, reciprocal alias, taper, star, cell,
and owner retained. The complete bound stays \(Y^{35/48+\varepsilon}\),
and no global exponent or M9 status changes.

Accepted evidence:

- rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/synthesis.md;
- rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reviews/conductor_round131_residue_mode_adjudication.md;
- rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reviews/blind_post_unmask_primitive_period_scope_audit.md;
- rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reviews/discovery_post_unmask_fourier_capacity_audit.md;
- rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reviews/hostile_post_unmask_literal_weight_audit.md;
- proofs/kernels/gc_w7_16_primitive_residue_fourier.md.

## Round 132: exact hyperbolic chart and direct decoupling obstruction

For a top-shell ray \(r=(a,b)\), define

\[
 \xi={b\over D},\qquad \eta=-{Da\over Lb},\qquad
 \zeta=-{a\over L}.
\]

Then \(\zeta=\xi\eta\) exactly.  If \(n=ab'-a'b>0\) and
\(P_i=cL/(\kappa_iD)\), then

\[
 {ca\over\kappa_i b}-{ca'\over\kappa_i b'}
 =P_i(\eta_{r'}-\eta_r),
 \qquad
 \eta_{r'}-\eta_r={Dn\over Lbb'}.
\tag{132.1}
\]

Thus \(P_i\asymp Y^{32/48}\), while the determinant support has width at
most \(h_*\asymp\kappa_iD/(WL)=Y^{-5/48+o(1)}\).  On a dyadic \(h\)-band,
after localizing absolute \(\eta\), the exact recentered map

\[
 X=\xi-\xi_0,\qquad H={\eta-\eta_0\over h},\qquad
 Z={\zeta-\eta_0\xi-\xi_0\eta+\xi_0\eta_0\over h}
\]

satisfies \(Z=XH\).  The reciprocal evaluation scale becomes
\(R_h=P_ih\); at the widest band,

\[
 R_{h_*}={c\over W}=Y^{27/48+o(1)}.
\tag{132.2}
\]

Equation (132.2) is physical scale bookkeeping, not an automatically
licensed decoupling radius.  A widest-band broad patch must have both

\[
 {|b-b'|\over D}\asymp1,
 \qquad {Wn\over\kappa_i bb'}\asymp1.
\tag{132.3}
\]

Same-denominator pairs fail the first condition exactly and remain
hyperbolic rulings.

The official Demeter--Wu v2 source requires two already-constructed
functions on patches separated in both surface coordinates.  Its bilinear
and refined bilinear right sides are positive cap or packet norms; its
linear and pointwise narrow mechanisms retain horizontal and vertical
rectangle terms.  The literal physical pair coefficient remains joint in
the two rays through variable primitive moduli, Stieltjes/Mobius profiles,
thresholds, taper, stars, aliases, cells, signs, and owners.  No affordable
owner-preserving projective factorization is proved.  Row or SVD
factorization gives an uncontrolled positive energy.

For an already-factorized transverse product, a fixed Fourier reproducing
kernel gives a pointwise consequence of the global bilinear theorem, but
only in terms of positive cap square functions and with no negative power.
The ruling term separately lacks a signed arithmetic estimate.  Therefore
the direct Demeter--Wu import is closed as a scoped source-level no-go.

The complete fixed-block bound remains \(Y^{35/48+\varepsilon}\), the
persistence threshold remains \(Y^{27/48+\varepsilon}\), and the determinant
target remains \(Y^{24/48+\varepsilon}\).  The internally proved global
exponent remains \(1/3\), the repaired external Li--Yang benchmark remains
\(0.314483175974\ldots\), and every M9 parent and the quarter target remain
open.

Accepted evidence:

- rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/synthesis.md;
- rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reviews/conductor_round132_hyperbolic_decoupling_adjudication.md;
- rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reports/demeter_wu_exact_source_card.md;
- rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reviews/source_post_chart_normalization_audit.md;
- rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reviews/blind_post_unmask_scope_audit.md;
- rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reviews/discovery_post_unmask_capacity_audit.md.

## Round 133: exact Li--Yang one-wave dictionary and direct BI pair obstruction

For one positive-numerator top-shell reciprocal wave,

\[
 h=a,\qquad m=b,\qquad H=L,\qquad M=D,\qquad
 T={c\over\kappa_i},\qquad F(z)=z^{-1}
\]

gives the exact source phase

\[
 {hT\over M}F(m/M)={ca\over\kappa_i b}.
\tag{133.1}
\]

Both Li--Yang phase conditions hold uniformly:

\[
F'=-z^{-2},\quad F''=2z^{-3},\quad F'''=-6z^{-4},
\quad F'F'''-3(F'')^2=-6z^{-6}.
\tag{133.2}
\]

Negative numerators are handled by conjugation after a sign split. The M1
denominator-quarter carrier has an \(O(1)\) source decomposition: split
\(b=4u+r\), make the carrier constant on each progression, and use
\(F_r(z)=1/(4z+r/M')\). The M2 character has the two-term Fourier
decomposition of \(\chi_4(a)\), absorbed by constant shifts of \(F\).
Neither carrier costs a power of \(Y\).

At \(T\asymp Y\), \(H=Y^{1/6}\), \(M=Y^{1/2}\), the repaired Case-A and
restricted small-cap hypotheses pass. The source parameters are

\[
N_A=Y^{67/300+o(1)},\qquad
R=Y^{83/600+o(1)},\qquad
\eta=Y^{-17/150+o(1)}.
\tag{133.3}
\]

At \(Q=R\),

\[
L_{\rm sp}=Y^{17/600+o(1)},\qquad
K_{\rm sp}=Y^{17/200+o(1)}.
\tag{133.4}
\]

The optimized source choice and exponent are

\[
q_*={250+10\sqrt{170}\over91},\qquad
\Phi(-1/3)={29+5\sqrt{170}\over300}
=0.313973413506755\ldots .
\tag{133.5}
\]

The source audit finds a fifth required repair. Lemma 4.1 condition (4.6),
using the Case-A \(N\) defined in (4.8), has quotient

\[
{N_A^{6-q}\over H^{2q-6}(M^3/T)^{4-q}}
\asymp
\left({M\over H}\right)^{(34q-54)/25}
T^{(106-51q)/100}(\log T)^{(969/14000)(6-q)}.
\tag{133.6}
\]

This is not printed (4.9); the two purported conditions differ by
\(T^2/M^6\) after common-power comparison. At the critical scale the
original condition has margin \(17(6-q)/300>0\), while (4.9) fails.
Corrected source (5.23) is exactly the strict-power test for original
(4.6), so the final narrow theorem is repaired by bypassing (4.9).
The external exponent remains

\[
\theta_{\rm LY}
={3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots .
\tag{133.7}
\]

General printed Theorem 4.2 remains uncertified. A future direct DLS use
must also resolve the v2 first-spacing mismatch: the exact norm and
introduction begin with coordinate \(l\), while the Section-4 sketch
prints \(k\).

The one-wave dictionary does not extend to the literal pair scalar. Its
coefficient remains joint through the one-sided moving determinant wedge,
taper, primitive lifts, Möbius/Stieltjes profiles, thresholds, aliases,
stars, cells, signs, and owners. No owner-preserving projective source norm
is proved. The source takes arcwise absolute values and returns positive
spacing quantities; it gives no reverse signed operator inequality.

Project rays are original source summation variables, not the derivative
approximants created after short-interval localization. The project
determinant supplies none of the four source second-spacing conditions.
Even granting a rank-one connector, projection, taper, and all owners at
zero cost, two independent normalized source bounds give only

\[
Y^{2\Phi(-1/3)+\varepsilon}
=Y^{0.6279468270\ldots+\varepsilon}
=Y^{30.1414\ldots/48+\varepsilon}>Y^{27/48}.
\tag{133.8}
\]

This is a scoped factor-first obstruction, not a universal impossibility
for a new joint Bombieri--Iwaniec theorem. The formal collapse
\(h=n,m=bb'\) is also unavailable because it has a product-fibre
coefficient and violates the source large-\(M\) Case-A range.

The complete bound remains \(Y^{35/48+\varepsilon}\), the persistence
threshold remains \(Y^{27/48+\varepsilon}\), and the determinant target
remains \(Y^{24/48+\varepsilon}\). The internal global exponent remains
\(1/3\); M9-M1, M9-M2, endpoint uniformity, M9, the bridge, and the
quarter target remain open.

Accepted evidence:

- rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/synthesis.md;
- rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/reviews/conductor_round133_bi_adjudication.md;
- rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/reports/li_yang_bi_exact_source_card.md;
- rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/reviews/blind_post_unmask_source_condition_seam.md;
- rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/reviews/source_post_unmask_parameter_and_scope_audit.md;
- rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/reviews/discovery_post_unmask_capacity_and_owner_audit.md;
- sources/li_yang_2023.md.

## Round 134: sharp folded Fejer majorant and its exact endpoint obstruction

For the endpoint-complete flat-smooth strict-UNBAL energy, form

\[
A(k)=\sum_{p\ {
m odd}}\chi_4(p)b_{p,k},
\qquad
\mathcal E_\chi=C_H\int_{\mathbb T}|D_H(\alpha)|^2
|\widehat A(\alpha)|^2\,d\alpha.
\tag{134.1}
\]

Round 134 solves the finite one-sided-majorant problem exactly. If
\(1\le N\le H\), \(H=mN+s\), \(0\le s<N\), then every real
degree-((N-1)) polynomial \(T\ge|D_H|^2\) has

\[
\widehat T(0)\ge
\mu_N(H)=(N-s)m^2+s(m+1)^2
=\frac{H^2}{N}+s\left(1-\frac{s}{N}\right).
\tag{134.2}
\]

The bound is sharp, attained by

\[
T^*_{H,N}=|mD_N+D_s|^2,
\tag{134.3}
\]

because, with \(z=e(\alpha)\),

\[
|1-z|^2(T^*_{H,N}-|D_H|^2)
=|1-z^N|^2\sum_{a=0}^{m-1}(m-a)|1-z^{s+aN}|^2\ge0.
\tag{134.4}
\]

Writing (n_j=m+1) for (j<s) and (n_j=m) otherwise gives the
endpoint-exact global inequality

\[
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
\le
\sum_n\left|\sum_{j=0}^{N-1}n_jA(n+j)\right|^2.
\tag{134.5}
\]

Its exact mass factor is

\[
\rho(H,N)=\mu_N(H)/H\ge H/N,
\tag{134.6}
\]

and its Fourier coefficient \(\ell^1\)-mass is (H^2). Thus a
fixed-power bandwidth contraction pays the reciprocal fixed power in
zeroth mass; choosing (N\le H/\min(H,Q)) to remove the old positive-row
deficit returns that same deficit. Lagwise modulus returns the full factor
(H).

This is a method obstruction, not a lower bound for the literal array. The
zeroth term retains the complete signed cross-(p) norm, and cross-lag
cancellation remains possible. Exact character Poisson returns the same
reciprocal actual-character Gram with the folded weights; only the exact
integrals or the principal Gram plus every weighted remainder are
endpoint-complete. No target-scale signed folded-Gram estimate is proved.

The positive-energy majorant surface is parked. The next distinct M2
UNBAL interface is the physical prescribed-centre truncated-divisor
wavelet with a genuine modulus-aspect signed dispersion theorem. The
internal exponent remains (1/3), the repaired external Li--Yang exponent
remains (0.3144831759740614\ldots), and every M9 parent and the quarter
target remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reviews/conductor_round134_majorant_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/blind_bandlimited_quadratic_majorant_feasibility.md;
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reviews/discovery_post_unmask_folded_majorant_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reviews/hostile_post_unmask_exact_majorant_and_poisson_audit.md.

## Round 135: exact prescribed-centre source maps and scoped dispersion obstruction

For a flat-smooth strict-UNBAL packet, put

\[
R=X/D,\qquad K=XL/D^2,\qquad
\Delta=R/K=D/L,\qquad F=XK/R,
\tag{135.1}
\]

and write every real centre as \(X=N_0+\xi\), with
\(N_0=\lfloor X\rfloor\) and \(0\le\xi<1\). After scaling
\(k=Ku\), \(r=Rv\), the factor

\[
e(\xi k/r)=e\!\left(\xi\Delta^{-1}u/v\right)
\tag{135.2}
\]

belongs to the uniformly smooth coefficient tensor. Buffered
Fourier--Mellin separation has \(O(1)\) integrated projective mass. Thus
all source phases may use the integral frequency \(N_0\), for every real
\(X\), without altering the literal fibre norms

\[
\|\alpha\|_2=1,\qquad
\|\beta\|_2\asymp R^{1/2},\qquad
\|\nu\|_2\asymp K^{-1/2}.
\tag{135.3}
\]

The direct Bettin--Chandee dictionary \((a,m,n)=(k,1,r)\) gives

\[
F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon,
\tag{135.4}
\]

and Wright's decisive fifth term gives

\[
R^{11/8}F^{1/4}X^\varepsilon.
\tag{135.5}
\]

Across the entire strict-UNBAL polytope, the three exponent margins over
the absolute capacity \(\Delta=X^{\delta-\ell}\) are respectively
strictly greater than \(3/10\), \(1/4\), and \(5/16\). Wright's growing
fixed-factor option is unavailable in this map because the source length
\(M=1\) forces \(R_0=O(1)\).

There is also an exact nonconstant inverse connector on coprime rows:

\[
a=j^2,\qquad j=m=k,\qquad
m^2\overline m\equiv m\pmod r.
\tag{135.6}
\]

The diagonal coefficient \(m^{-1}\mathbf1_{j=m}\) has sharp projective
norm \(\asymp1\), obtained from

\[
\mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt.
\tag{135.7}
\]

At source lengths \((A,M,N)=(K^2,K,R)\), both audited source theorems
still exceed \(\Delta\) by the same fixed margins.

The two natural completion orders are not interchangeable. Completing
the original smooth \(k\)-weight first gives coefficients

\[
|\widehat b_{g,n}(h)|
\ll_B R^{-1}\left(1+\|h\|_n/\Delta\right)^{-B}.
\tag{135.8}
\]

Inversion permutes the units, so the complete inner sum is Ramanujan; the
non-coprime form is an ordinary additive delta. Restoring every gcd
stratum returns exactly

\[
|\mathscr R_{D,L}(X)|\ll\Delta X^\varepsilon,
\tag{135.9}
\]

with no strict saving. Completing the rough inverse selector first instead
produces the genuine joint matrix

\[
\sum_h\widehat g_r(h)S(N_0,h;r),\qquad
\sum_h|\widehat g_r(h)|^2\ll(rK)^{-1},
\tag{135.10}
\]

and exact Kloosterman second moments give positive outer cost
\(R\sqrt\Delta X^\varepsilon\), worse than the accepted envelope.

In the physical form, \(s=N_0+t\) gives the exact fixed residue
\(t\equiv-N_0\pmod r\). Wright's dispersion corollary nevertheless does
not apply: the literal scalar lacks the required independent convolution,
uniform coprimality, size range, principal subtraction, and
modulus-by-modulus absolute-discrepancy structure. For
\(\tau=N_0-dr\ne0\), Bettin--Chandee Corollary 1 accepts the determinant
dictionary

\[
(m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
m_1n_2-m_2n_1=-\tau,
\tag{135.11}
\]

but its main terms aggregate only to \(\Delta X^\varepsilon\), while its
error per determinant is

\[
X^{3/5+\varepsilon}R^{17/20},
\tag{135.12}
\]

whose exponent exceeds \(41/40\). The zero determinant is
divisor-bounded.

Therefore the audited Bettin--Chandee/Wright trilinear, completion,
dispersion, and fixed-determinant interfaces do not improve the accepted
flat-wave envelope and do not prove the quarter estimate. This is a
source-method obstruction only: it is neither a lower bound for the
literal signed wave nor a no-go for a new fixed-centre
\(\chi_4\)-signed coefficient-matrix theorem.

M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, and the
quarter target remain open. The internal exponent remains \(1/3\); the
audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/conductor_round135_kloosterman_dispersion_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/bettin_chandee_wright_kloosterman.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md.

## Round 136: balanced alias character restoration and broad--narrow obstruction

In the accepted balanced divisor-progressive alias chart,

\[
h+2s_d=d\ell_d,\qquad \mu=\frac12-m,\qquad
\lambda=\frac\mu d,
\]

the combined linear and residue phase has the exact character form

\[
\boxed{
e\!\left(-\frac{\lambda h}{2}
+s_d\left(\frac12-\lambda\right)\right)
=-i(-1)^m\chi_4(d)\chi_4(h).}
\tag{136.1}
\]

Indeed,

\[
-\frac{\lambda h}{2}+s_d\left(\frac12-\lambda\right)
=\frac{s_d}{2}-\frac{\mu\ell_d}{2},
\]

and the odd mod-four congruences give (136.1). If
\(2\lambda=a/b\) is reduced, with \(a,b\) odd, every literal lift is

\[
(d,\mu)=(bc,ac/2),\qquad c\ \mathrm{odd},
\tag{136.2}
\]

and

\[
(-1)^m\chi_4(d)=\chi_4(ab).
\tag{136.3}
\]

Consequently the complete phase-character carrier is

\[
-i\chi_4(h)\chi_4(ab)
e\!\left(R\sqrt{hk}-\frac{Xbk'}a\right),
\tag{136.4}
\]

independent of the lift multiplier \(c\). Since
\(x_*=Xk'/\lambda^2\), the two determinant gates \(\rho\) and
\(\Delta\) are also common across these lifts. Their
\(\gamma_{bc}\), progression, \(J\)-condition, support, and literal
amplitude remain distinct. Equal-rational lifts are therefore
carrier-coherent but may neither be merged nor assumed to add positively.

The Round-136 broad--narrow audit distinguishes three geometric objects.
With \(r=\sqrt{k/h}\), \(z=\lambda/R\), the unfactored and gauged
gradient surfaces are

\[
\Sigma_0=(r-z,r^{-1},-z^{-1}),
\qquad
\Sigma_1=(r,r^{-1},-z^{-1}).
\tag{136.5}
\]

Determinants of three gradient vectors, determinants of normals to these
surfaces, and the one-body transform Hessian are inequivalent. The raw and
gauged surface normals are proportional to \((1,r^2,z^2)\) and
\((1,r^2,0)\). Thus the chosen gauged surface-normal broad class is empty,
but this is not an intrinsic statement that every arithmetic or
gradient-vector broad class is empty. Because (136.1) is an exact
unit-modulus coefficient gauge, raw surface-normal curvature is not a
representation-independent sufficient certificate for a
coefficient-uniform theorem. No audited determinant has a proved
owner-preserving inequality returning the missing factor \(L\) to the
fixed scalar.

There is an exact narrow control common to both gauges. Put

\[
c=\frac{\lambda}{R}\sqrt{\frac hk},\qquad
Q=\frac{\mu^2h}{d^2k}=Xc^2,\qquad A=\frac{k'}k.
\]

For fixed \(c\), both gradient families satisfy \(G_2+cG_3=0\), so
every three-gradient determinant on the ruling vanishes. The two gates are

\[
\rho=hk'\frac{c^2-1}{c^2},
\qquad
\Delta=hk\frac{A^2-c^2}{c^2}.
\tag{136.6}
\]

They remove only collars and do not remove the fixed-\(Q\) ruling; for
\(k'=k\), \(\Delta=-\rho\). Fixed-slice same-parity clusters of
cardinality \(\gg d^2L^2\) also remain, but their weighted masses are
only upper or adversarial capacities. The \(L^5\) aliaswise and
\(L^4\) positive-square ledgers are not physical lower bounds and cannot
replace the \(L^3\) signed scalar target.

Therefore the standard coefficient-uniform determinant, positive-cap,
one-frequency spacing, and canonical second-B mechanisms do not prove the
balanced bulk estimate. The smallest owner-complete survivor remains the
complete signed \((h,k,k',d,\mu,J)\) kernel with both gates and every
literal profile. This is a scoped method obstruction, not a disproof of
BAL or of a future gauge-sensitive actual-symbol theorem.

The balanced remainder, actual energy, and quarter packet remain open, as
do hard TOP, every required UNBAL owner, M9-M2, both M9-M1 routes, endpoint
uniformity, M9, and the quarter target. The internal exponent remains
\(1/3\), and the audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/conductor_round136_broad_narrow_adjudication.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/candidates/conductor_round136_character_gauge_ruling_obstruction.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/blind_post_unmask_gauge_and_scalar_interface_audit.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/discovery_post_unmask_ruling_and_capacity_audit.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/hostile_post_unmask_determinant_and_character_audit.md.

## Round 137: hard-TOP product fibres, radical control, and transform self-return

After removing the already controlled square-entry sector, the nonsquare
hard-TOP scalar has the exact product-fibre form

\[
 T_L^{\rm ns}=L^{3/2}
 \sum_{\substack{n\asymp L^2\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n),
\tag{137.1}
\]

where

\[
 C_L(n)=
 \sum_{\substack{h\mid n,\ h\ {\rm odd}\\
 \sqrt n\le h\le2\sqrt n}}
 \chi_4(h)\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
\tag{137.2}
\]

This preserves the ceiling in the original cone because
\(\lceil h/4\rceil\le m\le h\) is equivalent, after \(n=hm\), to
\(\sqrt n\le h\le2\sqrt n\). Expanding the square and parameterizing
equal products by

\[
 h_1=ga,\qquad h_2=gb,\qquad m_1=bt,\qquad m_2=at,
 \qquad(a,b)=1,
\]

gives the accepted upper envelope

\[
 \boxed{\sum_n|C_L(n)|^2\ll L^2\log(2L).}
\tag{137.3}
\]

It is only an upper bound. Cauchy over the \(O(L^2)\) product values still
has size \(L^{2+o(1)}\), leaving the required
\(L^{1/2-o(1)}\) saving unproved.

There is stronger control on a fixed squarefree radical. If
\(B_L(n)=L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}\), then for every
squarefree \(D>1\),

\[
 \boxed{
 \sum_{\operatorname{sf}(n)=D}|B_L(n)|
 \ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.}
\tag{137.4}
\]

Writing \(n=Dt^2\), exact phase one is precisely
\((J\sqrt D)t\in\mathbb Z\). If \(J\sqrt D=p/q\) in lowest terms, the
exact points have \(q\mid t\); if it is irrational, there are none. The
whole channel has phase one exactly when \(J\sqrt D\in\mathbb Z\),
equivalently when \(XD\) is an integral square. Distinct squarefree
kernels cannot both satisfy this at one fixed centre, so the entire exact
nonsquare phase-one set is target-safe by (137.4). Near resonances are not
controlled, and summing (137.4) over all \(D\) returns
\(L^{2+o(1)}\) capacity.

Resolving divisibility lawfully by

\[
 1_{h\mid n}=\frac1h\sum_{a\bmod h}e(an/h),\qquad r=kh-a,
\]

and applying the stationary transform gives

\[
 x_{h,r}=\frac{Xh^2}{4r^2},\qquad
 \phi(x_{h,r})=\frac{Xh}{4r},\qquad
 x_{h,r}^{-3/4}|\phi''(x_{h,r})|^{-1/2}=2J^{-1/2}.
\tag{137.5}
\]

Thus its stationary principal family is

\[
 2e(-1/8)L^{3/2}J^{-1/2}
 \sum_{h\ {\rm odd}}
 \frac{\chi_4(h)\eta_L(h)\Phi(h/(H+1))}{h}
 \sum_{J/2\le r\le J}^{\star}
 W(r/y)e\!\left(\frac{Xh}{4r}\right).
\tag{137.6}
\]

This is exactly the original reciprocal hard-TOP principal family. The
direct \(m\)-process agrees at principal level, and a second canonical
transform returns the square-root phase. Equation (137.6) is not a full
finite identity: endpoints, zero and nonstationary modes, remainders,
crossings, and square restoration retain their existing owners.
Complementary-divisor switching is likewise an involution, while the split
\(C_L=r_2/4-R_L\) introduces an uncontrolled complement and cannot import
the desired circle estimate.

Accordingly, hard TOP remains open at the fixed-centre signed
additive-twist estimate for the literal coefficient (137.2), requiring an
\(L^{1/2-o(1)}\) saving. BAL, all required UNBAL owners, M9-M2, both
M9-M1 routes, endpoint uniformity, M9, the conditional quarter bridge, and
the Gauss-circle target remain open. The strongest internal exponent stays
\(1/3\); the audited external Li--Yang exponent stays
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/synthesis.md;
- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md;
- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md;
- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/blind_post_unmask_energy_resonance_audit.md;
- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/discovery_post_unmask_coefficient_and_self_return_audit.md;
- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/hostile_post_unmask_completion_and_radical_audit.md.

## Round 138: exact lower signed Farey residual

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

\[
 L_\chi(T)=\sum_{g\le T}\frac{\chi_4(g)}g,\qquad
 \lambda_b=\frac{\chi_4(b)}bL_\chi(y/b).
\]

On the certified small positive arc, the integerized flat lower cone is
termwise

\[
 \mathcal F_N=
 \sum_{\substack{2\le b\le y\\b\ {\rm odd}}}\lambda_b
 \sum_{\substack{1\le a<b\\(a,b)=1}}
 e(aN/b)J_{R,y}(a/b).
\tag{138.1}
\]

Indeed, reducing \(h/d=a/b\), with \(h=ag,d=bg\), aggregates all odd
lifts before a norm:

\[
 \sum_{g\le y/b}\frac{\chi_4(bg)}{ag}
 V_{\rm low}(4R^2a^2/b^2)
 =
 \frac{\chi_4(b)L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2).
\tag{138.2}
\]

The primitive numerator and every profile value are retained, and
\(J_{R,y}(0)=0\) kills the \(b=1\) class. Round 121 separately owns the
\(O(R)\) change from the original \(e(hX/d)\) cone to this
\(e(hN/d)\) cone.

At every rational sample put

\[
 c_{a,b}=\frac{L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2),\qquad
 \theta_{a,b}=\frac{Na}{b},\qquad
 \phi_{a,b}=\frac{Na}{b}+\frac{b-1}{4}\pmod1.
\tag{138.3}
\]

Then

\[
 \mathcal F_N=\sum_{a,b}c_{a,b}e(\phi_{a,b}),\qquad
 |c_{a,b}|\ll\frac1a,\qquad a\ll\frac bR.
\tag{138.4}
\]

The entire same-denominator sector is one row square:

\[
 \sum_b\left|\sum_ac_{a,b}e(\phi_{a,b})\right|^2
 \ll y\log^2(2X).
\tag{138.5}
\]

This includes the \(O(y)\) equality diagonal and every unequal-numerator
pair on one denominator.

For a fixed reduced ordinary carrier \(u/q\), every denominator is
\(b=qg\), where

\[
 g\mid N,\qquad q,g\ {\rm odd},\qquad
 (N/g,q)=1,
\]

and the numerator belongs to one residue class modulo \(q\). Thus one
ordinary carrier fibre has absolute mass
\(O(\tau(N)\log(2X))\), while the total coefficient mass is
\(O(y\log(2X))\). Since
\(\chi_4(b)=e((b-1)/4)\), one physical \(\phi\)-fibre is a union of at
most two restricted ordinary fibres. Rational spacing therefore gives,
for either carrier,

\[
 \sum_{\|z-z'\|\le\delta}M(z)M(z')
 \ll y\tau(N)\log^2(2X)(1+\delta y^2).
\tag{138.6}
\]

Define the real, conjugation-closed residual

\[
 \mathcal R_\delta=
 \sum_{\substack{(a,b),(a',b')\\b\ne b'\\
 \|\theta_{a,b}-\theta_{a',b'}\|>\delta\\
 \|\phi_{a,b}-\phi_{a',b'}\|>\delta}}
 c_{a,b}\overline{c_{a',b'}}
 e(\phi_{a,b}-\phi_{a',b'}).
\tag{138.7}
\]

Equations (138.5)--(138.6) prove

\[
 \boxed{
 |\mathcal F_N|^2
 =\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).}
\tag{138.8}
\]

Consequently the scalar target is equivalent, after renaming epsilon, to

\[
 \boxed{
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.}
\tag{138.9}
\]

This last estimate is open. The residual still has
\(y^{2+o(1)}\) absolute capacity.

The exact determinant chart explains why a direct fibre modulus does not
finish (138.9). If \(b=Gr,b'=Gs,(r,s)=1\), then

\[
 \Delta=G\delta_0,\qquad
 \delta_0=as-a'r,\qquad
 a=a_0+r\ell,\quad a'=a'_0+s\ell.
\tag{138.10}
\]

The determinant phase and denominator character are constant in
\(\ell\). The partial fraction

\[
 \frac1{aa'}=\frac1{\delta_0}
 \left(\frac{s}{a'}-\frac r a\right)
\]

retains unavoidable endpoint/aspect terms. A variable odd-\(S\)
reciprocal-kernel family has contribution \(1\) while
\(\log X/(S-1)\to0\), ruling out an aspect-free gain from this identity.

Exact character Poisson on the inclusive hard interval retains a
half-endpoint and all dual integrals. Its interior stationary principal
factor is

\[
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\tag{138.11}
\]

whose complete principal absolute capacity is
\(O(R^{3/2}\log X)\), above target \(R\). The clean principal family is
not the full scalar: hard-endpoint transitions, nonstationary modes,
profile and stationary crossings, remainders, small heights, both
branches, floors, lift reassembly, and the conjugate sign remain.

If \(N=Ds^2\), with \(D\) squarefree, the unique exact variable
phase-one channel is \(hr=Dt^2\). Its bounded principal/transition mass
is

\[
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{138.12}
\]

Near radicals and every nonprincipal owner remain open. Fourth-power
Farey packets have target-scale internal residual capacity, and the
accepted paired tubes have \(R^{3/2}\) capacity only after a forbidden
partial modulus; neither is a lower bound. A second Legendre step returns
the reciprocal phase, and exact Fourier completion returns the flat
discrepancy.

Thus lower GAR remains open precisely at (138.9). Both direct blockwise
M1 parents remain open, as do M9-M1, all M2 parents, endpoint uniformity,
M9, the conditional quarter bridge, and the target. The strongest
internal exponent remains \(1/3\), while the audited external Li--Yang
exponent remains
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/conductor_round138_signed_farey_adjudication.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/candidates/conductor_round138_scalar_rows_and_resonance_fibres.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/blind_post_unmask_scalar_fibre_audit.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/discovery_post_unmask_transform_and_scope_audit.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/hostile_post_unmask_owner_and_capacity_audit.md.

## Round 139 accepted exact displacement-curvature reduction

Retain the Round-138 notation

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\leq q\leq2y.
\]

The exact substitution \(d=y-v\) gives, for
\(\sigma\in\{\pm1\}\),

\[
 \mathcal F_N^\sigma
 =\sum_{h\geq1}{1\over h}\sum_{0\leq v<y}
 \chi_4(y-v)
 V_{\rm low}\!\left({4R^2h^2\over(y-v)^2}\right)
 e\!\left(\sigma h{q+v^2\over y-v}\right).
\tag{139.1}
\]

If \(p_y\equiv y-1\pmod2\), every nonzero term has \(v=p_y+2n\) and
\(\chi_4(y-v)=e((y-v-1)/4)\).  Fix \(0<\rho<1/8\) and put

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor.
\tag{139.2}
\]

Let \(\mathcal C_N^\sigma\) be (139.1) restricted to
\(0\leq v\leq L_h\), and let \(\mathcal S_N^\sigma\) be its literal
complement.  On the parity lattice the complete physical phase has exact
curvature

\[
 {d^2\over dn^2}\left\{
 \sigma h{q+(p_y+2n)^2\over y-p_y-2n}
 +{y-p_y-2n-1\over4}\right\}
 =\sigma{8hN\over(y-p_y-2n)^3}.
\tag{139.3}
\]

Throughout the collar, \(y-v\asymp_\rho y\), so (139.3) has constant
sign and size \(h/y\), uniformly in \(q\), both parities, both signs,
and every real floor interval.  The number of parity points is at most
\(1+L_h/2\), and the sampled literal profile has bounded variation.
The weighted second-derivative estimate therefore gives one row as

\[
 \ll\sqrt y+\sqrt{y/h}.
\tag{139.4}
\]

The profile support has \(h\ll R\).  Restoring \(h^{-1}\) and summing
(139.4) yields

\[
 \boxed{
 |\mathcal C_N^\sigma|\ll R\log(2X),\qquad
 \mathcal F_N^\sigma
 =\mathcal S_N^\sigma+O(R\log(2X)).}
\tag{139.5}
\]

Hence

\[
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.
\tag{139.6}
\]

The second equivalence uses (138.8).  Equation (139.6) is only a chain
of target statements.  The cutoff depends on the unreduced lift and the
collar--tail square cross term is uncontrolled, so no filtered sub-square
of \(\mathcal R_{y^{-2}}\) has been deleted.

The prescribed-centre quadratic core has exact correction

\[
 E_{h,q,y}(v)=h{v(q+v^2)\over y(y-v)}.
\tag{139.7}
\]

The window \(v\ll(y^2/h)^{1/3}\) has bounded correction variation and
is target-safe by ordinary quadratic Gauss completion modulo \(2y\),
with complete-sum bound

\[
 |G_{2y}(8h,B)|
 \leq\{2y(16h,2y)\}^{1/2}
 \ll\sqrt{y(h,y)}.
\tag{139.8}
\]

This smaller Taylor window does not extend globally.  At odd fourth
powers, \(q=0,h=1\), a fixed literal plateau interval has

\[
 \operatorname{Var}_{v\equiv p_y(2)}e(E_{1,0,y}(v))\gg y.
\tag{139.9}
\]

Exact full completion is therefore an invertible Fourier correlation of
the correction coefficients with ordinary additive Gauss sums, not a
Salié sum.  Coefficient-blind \(L^2\) gives no improvement over \(y\);
exact character-Poisson retains \(R^{3/2}\) full-alias capacity; and a
second Legendre transform returns the reciprocal phase.

The first open estimate is the literal tail bound in (139.6).  Its
absolute capacity remains \(y^{1+o(1)}\).  Lower GAR, both direct M1
parents, M9-M1, all M2 parents, endpoint uniformity, M9, the quarter
bridge, and the target remain open.  The internal exponent remains
\(1/3\), and the audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reviews/conductor_round139_displacement_adjudication.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reviews/blind_post_unmask_curvature_rederivation.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reviews/hostile_post_unmask_curvature_and_directionality_audit.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reviews/discovery_post_unmask_quadratic_completion_audit.md.

## Round 140 accepted smoothed far-height-alias reduction

Retain the Round-139 notation and choose fixed
\(0<\rho_1<\rho_2<1/8\).  Put

\[
 L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,\qquad
 D_{i,h}=y-L_{i,h}-1,
\tag{140.1}
\]

and let \(r_{2,h}\) be the least positive odd integer satisfying

\[
 r_{2,h}\ge {4Nh\over D_{2,h}^2}
\tag{140.2}
\]

on each nonempty active row.  Then the exact sharp displacement tail
left by Round 139 satisfies

\[
 \boxed{
 \mathcal S_{N,\rho_1}^{\pm}
 =\mathcal P_{\rho_2}^{\pm}
 +O(R\log^C(2X)),}
\tag{140.3}
\]

where

\[
 \begin{split}
 \mathcal P_{\rho_2}^{+}
 ={}&e(-1/8)N^{1/4}
 \sum_h\sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),\\
 \mathcal P_{\rho_2}^{-}
 ={}&\overline{\mathcal P_{\rho_2}^{+}}.
 \end{split}
\tag{140.4}
\]

The hard character-Poisson formula itself is only branchwise
principal-value convergent.  If its upper endpoint sample is nonzero,
then

\[
 I_{h,r}^{\sharp}
 ={A_h(D_{1,h})e(Nh/D_{1,h}+rD_{1,h}/4)
   \over2\pi i(r/4-Nh/D_{1,h}^2)}
 +O_h(r^{-2}),
\tag{140.5}
\]

so the absolute odd-alias sum diverges.  The half-endpoint and symmetric
branch ordering cannot be discarded.

To prove (140.3), choose a fixed flat step \(\eta\) and set

\[
 \Delta_h=D_{1,h}-D_{2,h}+1,\qquad
 W_h(x)=\eta\!\left({D_{1,h}+1-x\over\Delta_h}\right).
\tag{140.6}
\]

At integer samples, sharp minus smooth is supported exactly on
\(L_{1,h}<y-d\le L_{2,h}\).  The accepted exact-curvature collar
therefore prices this signed difference by \(O(R\log X)\) before
Poisson summation.  For
\[
 \widetilde A_h(x)
 ={1\over h}V_{\rm low}(4R^2h^2/x^2)W_h(x),
\]
flatness at both ends and rescaling give

\[
 \|\widetilde A_h\|_\infty+\|\widetilde A_h'\|_1\ll h^{-1},
\qquad
 \|\widetilde A_h''\|_1
 \ll {1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\tag{140.7}
\]

The smooth rowwise \(B\)-process has error
\(O(h^{-1}\log^2(2X))\).  On a physical block \(x\asymp Z\), its
stationary-alias count \(P\), Gaussian width \(w\), and cubic parameter
are

\[
 P={Nh\over Z^2},\qquad
 w=\left({Z^3\over Nh}\right)^{1/2},\qquad
 \epsilon_3=\sqrt{Z\over Nh}.
\]

The counted cubic and fixed-profile errors are

\[
 {Pw\epsilon_3\over h}\ll h^{-1},\qquad
 {Pw^2\over hZ}\ll h^{-1}.
\tag{140.8}
\]

The derivative of \(W_h\) is supported only on the
\(O(1+\sqrt h)\) smoothing-ramp aliases, where

\[
 \sqrt h\,{w^2\over h\Delta_h}\ll h^{-1}.
\tag{140.9}
\]

All remote positive and negative aliases are integrated twice, and the
flat endpoints remove their boundary terms.  Summing the row errors
over \(h\ll R\) costs \(O(\log^3 X)\).  The ramp aliases and
\(r_{2,h}\) cost \(O(R\log X)\).  For \(r\ge r_{2,h}+2\), the saddle
is many Gaussian widths inside \(W_h=1\), and stationary phase gives
the coefficient in (140.4), with all local and off-saddle remainders
target-safe.  This proves (140.3).

Grouping the clean family by \(m=hr\) gives

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm}),
\tag{140.10}
\]

\[
 A_{\rho_2}(m)
 =\sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                   r\ge r_{2,h}+2}}\chi_4(r).
\tag{140.11}
\]

The Hessian of \(\sqrt{Nhr}\) has determinant zero and rank one, also
after \(r=4h+s\).  Coefficient-blind modulus has matching
\(R^{3/2+o(1)}\) absolute capacity: the upper bound follows from
\(|A_{\rho_2}(m)|\le\tau(m)\), and the \(h=1\) profile plateau has the
same sum of term moduli.  The mask does not force character
cancellation.  At sufficiently large odd fourth-power centres, for
supported \(m=p^{2a}\) with \(p\equiv1\pmod4\),

\[
 A_{\rho_2}(p^{2a})=a.
\tag{140.12}
\]

This is an internal fibre statement, not a signed scalar lower bound.
If \(N=Du^2\), \(D\) squarefree, the exact radical channel
\(m=Dt^2\) has absolute mass

\[
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{140.13}
\]

Near radicals and nonsquare incomplete fibres remain open.  A second
Legendre step returns the reciprocal phase, while completion of the
fibre returns \(r_2(m)/4\).

Thus the first open estimate is

\[
 \boxed{
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.}
\tag{140.14}
\]

Equation (140.3) is an unsquared scalar equivalence only.  It does not
control the collar--tail cross term or delete a Round-138 residual
sub-square.  Lower GAR, both direct M1 parents, M9-M1, every M2 parent,
endpoint uniformity, M9, the bridge, and the quarter target remain
open.  The strongest internal exponent remains \(1/3\), and the
audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/conductor_round140_height_alias_adjudication.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/candidates/conductor_round140_smoothed_far_alias_reduction.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/blind_post_unmask_smoothed_connector_rederivation.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/hostile_post_unmask_owner_complete_far_alias_audit.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/discovery_post_unmask_rank_product_directionality_audit.md.

## Round 141 accepted cone and microscopic nearest-square reduction

Retain the notation and the exact incomplete coefficient
\(A_\rho(m)\) of Round 140, and define

\[
 C(m)=\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r>4h}}\chi_4(r).
\tag{141.1}
\]

If \(r_h\) is the least positive odd integer at least
\(4Nh/D_h^2\), then for odd \(r\)

\[
 r\ge r_h+2
 \Longleftrightarrow
 (r-2)D_h^2\ge4Nh.
\tag{141.2}
\]

Since \(N\ge y^2>D_h^2\), every exact far pair lies in \(r>4h\).
Writing

\[
 E_N(m)=
 \sum_{\substack{hr=m,\ r\ \mathrm{odd}\\4h<r\le r_h}}\chi_4(r),
\]

one has \(A_\rho=C-E_N\) exactly.  Moreover

\[
 {4Nh\over D_h^2}-4h
 \ll_\rho1+\sqrt h+{h\over y},
\]

and therefore

\[
 \sum_m m^{-3/4}|E_N(m)|
 |V_{\rm low}(R^2m/N)|
 \ll_{\rho,V}\log(2X).
\tag{141.3}
\]

Thus all height floors may be replaced by the constant cone at target
cost.

On the disjoint powers-of-two blocks
\(\mathcal I_M=[M,2M)\cap[1,C_VN/R^2]\), define

\[
 k_m=\left\lfloor\sqrt{Nm}+{1\over2}\right\rfloor,
 \qquad j_m=k_m^2-Nm.
\tag{141.4}
\]

There are no half-integer ties.  The real nearest-\(k\) cell is

\[
 \left[{(k-1/2)^2\over N},{(k+1/2)^2\over N}\right)
\]

and has length \(2k/N\ll R^{-1}<1\); hence it contains at most one
integer \(m\).  For \(j\ne0\), prime-power lifting and the Chinese
remainder theorem give

\[
 \#\{k\bmod N:k^2\equiv j\pmod N\}
 \ll_\varepsilon N^\varepsilon|j|^{1/2}.
\tag{141.5}
\]

Because \(k_m<N\) on the effective support and
\(m=(k_m^2-j_m)/N\), (141.5) implies

\[
 \#\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\}
 \ll_\varepsilon N^\varepsilon M^{3/4}.
\tag{141.6}
\]

After the weight \(m^{-3/4}|A_\rho(m)|\), every such block is
target-safe.  The exact radicals \(j_m=0\) are \(m=Dt^2\) when
\(N=Du^2\), \(D\) squarefree, and are target-safe separately.
Consequently

\[
 \boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_\varepsilon(X^\varepsilon).}
\tag{141.7}
\]

The survivor in (141.7) remains open.  The elementary congruence method
prices a wider window \(|j|\le J\) by
\(M^{-3/4}J^{3/2}X^\varepsilon\), so it exhausts its target-safe power
at \(J=\sqrt M\).

There are three accepted no-go controls.  First, writing
\(m=2^\nu n\), \(n\) odd, and pairing the odd factors gives

\[
 \sigma_{\chi_4}(n)
 =(1+\chi_4(n))A_\nu(n)+B_\nu(n).
\tag{141.8}
\]

For \(\chi_4(n)=-1\), both the complete and central coefficients vanish
and the far coefficient survives untouched.  For
\(\chi_4(n)=1\), the identity returns
\(r_2(2^\nu n)/4\) together with an exact owner-sized central band.

Second, the exact coefficient has a full additive quarter mode:

\[
 \sum_{m\le M}A_\rho(m)e(m/4)
 ={i\pi\over8}M+O_{\rho,c_0}(M^{3/4}),
\tag{141.9}
\]

\[
 \sum_{m\le M}m^{-3/4}A_\rho(m)e(m/4)
 ={i\pi\over2}M^{1/4}+O_{\rho,c_0}(\log(2M)).
\tag{141.10}
\]

Hence the coefficient has linear variation on every sufficiently large
supported plateau range.  This rejects uniform additive cancellation
and low-variation hypotheses but is not a lower bound for the nonlinear
fixed-centre scalar.

Third, after target-safe ratio smoothing, the dyadic cone sum has exact
double-Mellin arithmetic factor

\[
 4^{-t}\zeta(s+t)L(s-t,\chi_4).
\tag{141.11}
\]

The repaired source ledger gives only positive powers:
Robert--Sargos \(R^{1/2+\varepsilon}\) after separation and
\(R^{3/4+\varepsilon}\) for a direct joint mask; Sargos--Wu
\(R^{2/5+\varepsilon}\); and rowwise Tao--Trudgian--Yang
\(R^{267/641+\varepsilon}\).  The complete Popov/Li--Yang radial
cosine has the wrong coefficient and controls only one real
combination, while moment bounds used by Mellin Cauchy remain
polynomial.  No audited theorem closes (141.7).

The first open estimate is therefore exactly

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.
\tag{141.12}
\]

This is an unsquared scalar interface.  Lower GAR, both direct M1
parents, M9-M1, every M2 parent, endpoint uniformity, M9, the bridge,
and the quarter target remain open.  The strongest internal exponent
remains \(1/3\), and the audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/conductor_round141_incomplete_fibre_adjudication.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/discovery_post_unmask_cone_quarter_mode_audit.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/source_post_unmask_phase_pairing_audit.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/blind_post_unmask_source_mellin_audit.md.

## Round 142 accepted rational-spectrum and reconstruction obstruction

Retain the Round-141 cone coefficient

\[
C(m)=\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r>4h}}\chi_4(r).
\tag{142.1}
\]

For every reduced rational \(a/q\), \(q\ge1\), and every real
\(M\ge2\), one has the uniform additive transform

\[
\boxed{
\sum_{m\le M}C(m)e(am/q)
=\mathbf1_{4\mid q}{i\pi\chi_4(a)\over2q}M
+O((\sqrt M+q)\log(2q)).}
\tag{142.2}
\]

The proof retains the strict height condition \(4h^2<M\), the first
odd row entry \(4h+1\), and the upper floor.  A row mean exists exactly
when \(4\mid q\).  If \(q=4Q\), the two resonant height classes are
\(Q,3Q\pmod{4Q}\), with means
\((i/2)\chi_4(a)\) and \(-(i/2)\chi_4(a)\).  Reciprocal root spacing
over complete height periods gives the displayed all-\(q\) error.
The simpler condition \(q\log(2q)=o(\sqrt M)\) is sufficient for the
main term to dominate.  Partial summation gives

\[
\sum_{m\le M}m^{-3/4}C(m)e(am/q)
=\mathbf1_{4\mid q}{2i\pi\chi_4(a)\over q}M^{1/4}
+O(q\log(2q)+1).
\tag{142.3}
\]

For each fixed height,

\[
\mathbf1_{h\mid m}\chi_4(m/h)
=-{i\over2h}
\sum_{\substack{b\ ({\rm mod}\ 4h)\\b\ {\rm odd}}}
\chi_4(b)e(bm/(4h)).
\tag{142.4}
\]

Thus \(C(m)=\sum_{4h^2<m}g_h(m)\) has an exact finite rational
expansion with a moving height boundary.  For a height cutoff
\(h\le H\), the reduced coefficient at positive frequency \(a/q\)
is

\[
-{2i\chi_4(a)\over q}
\sum_{\substack{t\le4H/q\\t\ {\rm odd}}}{\chi_4(t)\over t}
=-{i\pi\chi_4(a)\over2q}+O(H^{-1}).
\tag{142.5}
\]

The limiting absolute coefficient mass through denominator \(Q\) is
\(\asymp Q\), while its squared mass is \(\asymp\log Q\).  Moreover,
every finite reduced-mode cutoff leaves a nonzero linear mean at every
omitted denominator divisible by four.  Hence finite projection and
unregularized limiting-spectrum arguments do not give a rationally
mean-zero residual.

The exact arithmetic reconstruction is as follows.  Put

\[
\mathcal G_d(m)=
\sum_{\substack{c\ ({\rm mod}\ 4d)\\(c,4d)=1}}
\chi_4(c)e(cm/(4d)).
\]

Then

\[
\mathcal G_d(m)=2i\sum_{\ell\mid(d,m)}
\ell\mu(d/\ell)\chi_4(d/\ell)\chi_4(m/\ell),
\tag{142.6}
\]

and the hard denominator cutoff is

\[
P_Q(m)={\pi\over4}\sum_{\ell\mid m}\chi_4(m/\ell)
\sum_{\substack{k\le Q/(4\ell)\\k\ {\rm odd}}}
{\mu(k)\chi_4(k)\over k}.
\tag{142.7}
\]

If complete numerator sets are grouped before damping the denominator
by \(d^{-\eta}\), \(\eta>0\), absolute convergence gives

\[
P_\eta(m)={\pi\over4L(1+\eta,\chi_4)}
\sum_{\ell\mid m}\chi_4(m/\ell)\ell^{-\eta}
\longrightarrow
\sigma_{\chi_4}(m)={r_2(m)\over4}.
\tag{142.8}
\]

The canonical Abel completion therefore returns the complete radial
coefficient, not \(C\).  If \(m=2^\nu n\), \(n\) odd, and
\(\chi_4(n)=-1\), then \(\sigma_{\chi_4}(m)=0\), so the residual
\(C-\sigma_{\chi_4}\) equals \(C\) exactly on that sector.

On \(M\le m<2M\), freezing \(4h^2<M\) leaves the exact wedge

\[
\sum_{\substack{h\mid m,\ r=m/h\ \mathrm{odd}\\M\le4h^2<m}}
\chi_4(r),
\]

whose unsigned \(m^{-3/4}\)-weighted incidence is
\(\asymp M^{1/4}\).  It is owner-sized at the top scale and cannot be
deleted by modulus.

For \(\Phi(m)=\sqrt{Nm}\) on \(m\asymp M\), the natural curvature
cell length and derivative range are

\[
L_M\asymp{M^{3/4}\over R},
\qquad K_M\asymp{R^2\over\sqrt M}.
\tag{142.9}
\]

Farey arcs of order \(L_M\) have raw thickened overlap \(O(L_M)\).
After the exact cell count and \(M^{-3/4}\) weight, a rational-mode
residual would need the short-interval norm

\[
\max_{q\le L_M,\ |J|\le L_M}
\left|\sum_{m\in J}D(m)e(am/q)\right|
\ll_\varepsilon X^\varepsilon{\sqrt M\over R}.
\tag{142.10}
\]

Equation (142.2) has a \(\sqrt M\)-scale prefix error and does not
imply (142.10).  The Round-141 condition
\(|k_m^2-Nm|>\sqrt M\) concerns phase values.  Integrality gives only

\[
\left|\Phi'(m)-{u\over q}\right|
\gg {1\over q^2\sqrt{NM}},
\tag{142.11}
\]

far smaller than the natural derivative-arc width \(L_M^{-1}\).

A coefficient-free smooth periodic branch satisfies the rigorous bound

\[
\ll\min\{M^{1/4},RM^{-1/2}+R^{-1}\},
\tag{142.12}
\]

but its full denominator assembly remains owner-sized.  The first
stationary principal symbol has reciprocal phase \(Nh/z\), exact
amplitude \(2N^{-1/4}\), and Gaussian unit \(e(-1/8)\).  The matching
second saddle reproduces the original square-root phase, character,
amplitude, and formal strict-cone condition.  This is principal-symbol
self-return only: no branchwise first- or second-stage remainder, hard
endpoint, or Fresnel transition is accepted.  The Round-140 endpoint
and remainder ledger applies only after complete reassembly.

The first open estimate remains exactly

\[
\sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.
\tag{142.13}
\]

This is an unsquared scalar interface.  Lower GAR, both direct M1
parents, M9-M1, every M2 parent, endpoint uniformity, M9, the bridge,
and the quarter target remain open.  The strongest internal exponent
remains \(1/3\), and the audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/conductor_round142_rational_spectrum_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/candidates/conductor_round142_rational_spectrum_self_return.md;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/blind_post_unmask_rational_reconstruction_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/source_post_unmask_abel_bprocess_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/discovery_post_unmask_source_bprocess_audit.md.

## Round 143 accepted level-four arithmetic embedding and spectral-matrix obstruction

Let \(X=N_0+\xi\), \(r=gn\), \(k=gj\), and \((j,n)=1\).  Retain the
literal profile and real-centre factor in

\[
b_{g,n}(j)=
\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n).
\tag{143.1}
\]

For \(\Gamma_0(4)\), primitive \(\chi_4\), weight parity
\(\kappa=1\), cusps \((\infty,0)\), and

\[
\sigma_\infty=I,\qquad
\sigma_0=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\]

the internally proved fixed-modulus identity is

\[
\boxed{
S^{\chi_4}_{\infty0}(4N_0,h;2n)
=\chi_4(n)S(N_0,h;n),\qquad n\ \mathrm{odd}.}
\tag{143.2}
\]

The allowed generalized moduli are exactly \(2n\), and (143.2) holds
for every \(h\) and every \((N_0,n)\), with no modulus-dependent root in
the fixed translation convention.  Hence the full gcd-restored
inverse-first owner is

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
\chi_4(g)W\!\left(\frac{X}{gnD}\right)
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)
S^{\chi_4}_{\infty0}(4N_0,h;2n).
\tag{143.3}
\]

Every gcd stratum, profile, entry, exit, unit selector, and real-centre
factor remains literal.  The degenerate class satisfies

\[
\mathscr R_{h=0}\ll_\varepsilon X^\varepsilon,
\tag{143.4}
\]

so the strict unresolved object is the centered \(h\ne0\) matrix.

Kıral--Young's matching switched-cusp formula assumes an even character
in weight zero and does not certify \(\chi_4\).  The legal
odd-character source implementation is the Blomer--Milićević identity

\[
\sum_{n\ \mathrm{odd}}\chi_4(n)S(N_0,h;n)\omega(n)
=\frac{\chi_4(M_0)}{\tau(\chi_4)}
\left(\sum_{4\mid C}-\sum_{8\mid C}\right)
S_{\chi_4}(M_0,16uh;C)\omega(C/4),
\tag{143.5}
\]

where \(u=2^{v_2(N_0)}\), \(M_0=N_0/u\), and
\(\tau(\chi_4)=2i\).  Its weight-one same-sign spectral ledger is
\(H+M+E\), including all exceptional Maaß parameters, every singular-cusp
Eisenstein term, and the level-\(4\) oldclasses on the level-\(8\) side.
No unsupported opposite-sign transform, residual term, or holomorphic
weight-one limit is accepted.

Centered zero padding and Parseval give

\[
\|A_g\|_{S_2}^2\ll_\varepsilon
\frac{X^\varepsilon}{gK},\qquad
\|A_g\|_{S_1}\ll_\varepsilon
\frac{\sqrt\Delta}{g}X^\varepsilon.
\tag{143.6}
\]

The conditional cross-cusp \(S/c\) samples are \(2nA_g(n,h)\); the
source-certified standard-cusp \(S/C\) samples are \(4nA_g(n,h)\).
Their automatic norm prices are

\[
\|B_g\|_{S_2}\ll_\varepsilon
\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,\qquad
\|B_g\|_{S_1}\ll_\varepsilon
\frac{R\sqrt\Delta}{g^2}X^\varepsilon.
\tag{143.7}
\]

These are upper bounds only.  The frozen controls prove no owner-saving
common smooth test, common coefficient sequence, or vector-valued norm for
the literal matrix.  The same-sign Linnik comparison range is

\[
H_{\rm Lin}(g)\asymp
\frac{X}{D^2g^2}=\frac{K}{Lg^2}.
\tag{143.8}
\]

Its discrete coverage is at most \(O(1/(Dg))\) of a row and is asymptotic
to that ratio only in the many-integer range.  For
\(g\gg\sqrt{K/L}\), no nonzero integer is covered; Parseval supplies no
localization and the audited sources print no complementary-range uniform
theorem.

The exact complete Kloosterman second moment yields only

\[
|\mathscr R_{D,L}(X)|
\ll_\varepsilon R\sqrt\Delta\,X^\varepsilon
=X^{1-(\delta+\ell)/2+\varepsilon}.
\tag{143.9}
\]

If \(a=\delta-\ell\), the exponent in (143.9) exceeds both accepted
envelope branches \(a\) and \((1-a)/2\) by more than \(1/4\) at every
strict point, and is greater than \(5/8\).  This positive closure works
for arbitrary row phases and is not character cancellation.  Moreover,

\[
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
=\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
\tag{143.10}
\]

is exact self-return to the original reciprocal row.

Thus the level-four/eight scalar trace-formula route is parked under the
current coefficient controls.  Reopen it only with a genuinely new theorem
for the literal centered nonzero-frequency matrix, including controlled
modulus smoothness or vector norm, the long Linnik complement, all spectral
pieces, profiles, and endpoints.  The flat strict-UNBAL target, all other
M2 owners, both remaining M1 parents, endpoint uniformity, M9, and the
quarter target remain open.  No global exponent changes.

Accepted evidence:

- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/conductor_round143_level_four_matrix_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/controls/conductor_round143_controls.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/blind_joint_matrix_spectral_feasibility.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/discovery_conductor_candidate_green_confirmation.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_conductor_candidate_final_green.md.

## Round 144 accepted gcd-averaged cell reduction and completed-Appell self-return

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),
\]

and, on each disjoint half-open active dyadic block \(\mathcal I_M\),

\[
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,
 \qquad j_m=k_m^2-Nm.
\tag{144.1}
\]

For nonzero \(j\), the accepted prime-power root calculation gives

\[
 \rho_N(j)=\#\{k\bmod N:k^2\equiv j\pmod N\}
 \ll_\varepsilon N^\varepsilon\sqrt{(N,j)}.
\tag{144.2}
\]

Retaining the gcd through the displacement average yields

\[
 \sum_{1\leq |j|\leq J}\sqrt{(N,j)}
 \leq2J\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon.
\tag{144.3}
\]

The active range has \(k_m<N\), so for fixed \(j\) the identity
\(m=(k_m^2-j)/N\) injects the relevant \(m\)'s into the roots in
(144.2).  Consequently

\[
 \#\{m\in\mathcal I_M:0<|j_m|\leq J\}
 \ll_\varepsilon JX^\varepsilon
 \qquad(J\geq1).
\tag{144.4}
\]

If \(N=Du^2\), with \(D\) squarefree, then \(j_m=0\) exactly when
\(m=Dt^2\).  This channel is separately target-safe, and for all
\(J\geq0\),

\[
 \#\{m\in\mathcal I_M:|j_m|\leq J\}
 \ll_\varepsilon(J+\sqrt M+1)X^\varepsilon.
\tag{144.5}
\]

Using \(|C(m)|\leq\tau(m)\), the nonzero \(J\)-window has weighted
price \(M^{-3/4}JX^\varepsilon\).  Thus the Round-142 formula with
threshold \(\sqrt M\) is superseded by the sharper exact reduction

\[
\boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).}
\tag{144.6}
\]

The exponent \(3/4\) is maximal only for this absolute root-count plus
divisor-bound ledger.  Equation (144.6) is a strict arithmetic support
reduction, not an estimate of its survivor.

For the completed automorphic interface, put

\[
 F(\tau)=\sum_{m\geq1}C(m)e(m\tau),\qquad
 \mathcal H(\tau)=\frac12\widehat A_4(1/2,-3\tau;2\tau).
\tag{144.7}
\]

The audited completed Jacobi laws, specialized by the internally checked
elliptic-shift calculation, give

\[
 \mathcal H(\tau)=F(\tau)+\frac14+
 \sum_{a=0}^{3}\frac i4(-1)^a
 \vartheta((2a-3)\tau+3/2;8\tau)
 R_{\rm Zw}(1/2+(3-2a)\tau;8\tau),
\tag{144.8}
\]

and

\[
 \mathcal H(\gamma\tau)=\chi_4(d)(c\tau+d)\mathcal H(\tau),
 \qquad
 \gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(4).
\tag{144.9}
\]

The residual integral exponential is
\(e[-c(d+3b)/4]=1\).  This is a derived scalar specialization of the
external completed laws, not a verbatim source theorem or a new discovery
of the Round-63 Appell identity.  The holomorphic part \(F\) is not
modular alone, the constant and all four corrections are compulsory, the
full modular group moves a characteristic orbit, and no harmonic-Maass
property or coefficient bound is asserted.

For \(w\in C_c^\infty((0,\infty))\), the exact character-Poisson identity
is

\[
\begin{aligned}
 \sum_{m\geq1}C(m)w(m)
 ={}&\frac12\sum_{h\geq1}w(4h^2)\\
 &+\frac i2\sum_{h\geq1}\sum_{j\ne0}\chi_4(j)
 \left\{\frac1h\int_{4h^2}^{\infty}
 w(u)e\!\left(-\frac{ju}{4h}\right)du
 -\frac{2w(4h^2)}{\pi i j}\right\},
\end{aligned}
\tag{144.10}
\]

with the bracketed double sum retained in its accepted symmetric,
absolutely convergent recombination.  After the target-safe cells are
restored globally, the positive-\(j\) interior principal family for
\(0<j<\sqrt N\) has full factor

\[
 e(1/8)N^{-1/4}\frac{\chi_4(j)}h
 V_{\rm low}(4R^2h^2/j^2)
 \psi_M(4Nh^2/j^2)e(Nh/j).
\tag{144.11}
\]

The equality \(j=\sqrt N\), when integral, belongs to the
endpoint/Fresnel ledger, and \(j>\sqrt N\) has no interior saddle.  Once
the half-boundary, subtraction, negative alias, collar, entry/exit,
profile, and remainder owners are reassembled, (144.11) is inverse to the
accepted Round-140 factor \(e(-1/8)N^{1/4}\).  The completed transform
therefore returns the same reciprocal height--alias owner.

The Round-142 denominator-Abel reconstruction still returns \(r_2/4\),
not \(C\), and leaves the negative-character sector and moving wedge.  The
top cone capacity \(R^{1/2+o(1)}\) and reciprocal capacity
\(N^{1/4}\asymp R\) are upper prices, not signed lower bounds.  The wider
phase-value gap is only \(R^{-3}\) times the natural derivative-cell
width and excludes no arbitrary Farey slope.

Hence the first open lower-radial estimate is

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon,
\tag{144.12}
\]

equivalently, after complete owner restoration,
\(\mathcal S_{\rm recip}^{+}\ll_{\varepsilon,\rho,V}RX^\varepsilon\).
No accepted completion or source theorem proves this estimate.

M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, and the
quarter target remain open.  The internally proved exponent remains
\(1/3\), and the separately audited external exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/conductor_round144_appell_completion_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/candidates/conductor_round144_appell_completion_and_cell_reduction.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/controls/conductor_round144_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/source_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/blind_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/discovery_conductor_candidate_final_green.md.

## Round 145 accepted squarefree-kernel reduction and linearization obstruction

Write every \(m\) uniquely as

\[
 m=st^2,\qquad s\ \mathrm{squarefree},\qquad t\geq1.
\tag{145.1}
\]

For the inherited coefficient

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),
\]

there are two accepted multiplicity-one parametrizations.  If
\(\gamma=\gcd({\rm sf}(h),{\rm sf}(r))\), then

\[
\boxed{
C(st^2)=
\sum_{\substack{\gamma\mid t\\
                  \gamma\ {\rm squarefree}\\
                  (\gamma,s)=1\\
                  \gamma\ {\rm odd}}}
\chi_4(\gamma)
\sum_{\substack{de=s\\e\ {\rm odd}}}\chi_4(e)
\sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\
                  eb^2>4da^2}}1.}
\tag{145.2}
\]

Equivalently, with \(G=(h,r)\),

\[
\boxed{
C(st^2)=
\sum_{de=s}^{\rm ord}
\sum_{\substack{Gab=t\\(da,eb)=1\\
                 Geb\ {\rm odd}\\eb^2>4da^2}}
\chi_4(Ge).}
\tag{145.3}
\]

In (145.2), \(h=\gamma da^2\), \(r=\gamma eb^2\), and
\(t=\gamma ab\); there is no additional coprimality condition on
\(a,b\), or between \(\gamma\) and them.  In (145.3),
\(h=Gda^2\), \(r=Geb^2\), and \(Gab=t\).  If \(G=c\ell^2\), the
squarefree factor \(c\) may overlap the quotient variables.  The two
formulas package common prime powers differently and are not to be
mixed.

Let the literal block be
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\leq2M\).  For fixed
\(t\),

\[
 \#\{s:st^2\in\mathcal I_M\}\leq {M\over t^2}+1
 \ll {M\over t^2}
\tag{145.4}
\]

whenever the set is nonempty.  Hence, using
\(|C(m)|\ll_\varepsilon X^\varepsilon\) on the active range, the
portion with \(t\geq T\) has block price

\[
 \mathcal L_M(T)
 \ll_{\varepsilon,V}X^\varepsilon {M^{1/4}\over T}.
\tag{145.5}
\]

Taking \(T=M^{1/4}\), retaining the literal profile and terminal
endpoint until the triangle inequality, and summing the dyadic blocks
proves the strict target-equivalence

\[
\boxed{
 \mathfrak T_N=
 \sum_M\sum_{1\leq t<M^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
 |k_{s,t}^2-Nst^2|>M^{3/4}}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
 C(st^2)e(t\sqrt{Ns})
 +O_{\varepsilon,V}(X^\varepsilon),}
\tag{145.6}
\]

where \(k_{s,t}=\lfloor t\sqrt{Ns}+1/2\rfloor\).  The retained
support satisfies

\[
 s>M^{1/2}.
\tag{145.7}
\]

Thus every \(t\geq\lceil M^{1/4}\rceil\) fibre is discharged, but
the bounded-\(t\) layers remain.

The inherited mask has the exact form

\[
 x=t\sqrt{Ns},\quad \delta=k_{s,t}-x,\quad
 j_{st^2}=\delta(2x+\delta),\quad
 \|t\sqrt{Ns}\|={|j_{st^2}|\over k_{s,t}+t\sqrt{Ns}}.
\tag{145.8}
\]

The half-integer tie is impossible.  If \(N=Dw^2\), \(D\)
squarefree, then \(s=D\) is the exact-radical fibre and is absent from
the strict mask.  All other fibres are generalized Pell norms; the
large-displacement condition removes small norms but gives no uniform
continued-fraction bound as the discriminant varies.

This failure is literal.  For squarefree \(s>1\), let

\[
 N=X=sL^2+1,\qquad
 \sqrt{Ns}=sL+\rho,\qquad
 \rho={1\over\sqrt{L^2+1/s}+L}.
\tag{145.9}
\]

Whenever \(t\rho<1/2\), the nearest integer is \(sLt\) and

\[
 j_{st^2}=-st^2=-m,\qquad e(t\sqrt{Ns})=e(t\rho).
\tag{145.10}
\]

Taking \(L=s\) and \(1\leq t\leq c s^{1/4}\), with \(c\) fixed
inside the flat profile range, gives genuine small-\(t\),
large-displacement survivor terms whose phases rotate arbitrarily
slowly.  This refutes a uniform frequency-gap or bounded-partial-
quotient argument; it is not a signed lower bound.  The \(t=1\) layer
is also nonvacuous:

\[
 C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi_4(e),
 \qquad C(p)=\chi_4(p)\ne0\quad(p>4\ \mathrm{prime}).
\tag{145.11}
\]

No audited complete-divisor, standard-twist, Liouville-twist,
linear-squarefree, fixed-quadratic, Robert--Sargos, or Sargos--Wu
theorem accepts simultaneously the coefficient (145.2) or (145.3),
the fixed centre, the individual positive complex direction, the
mask/profile, and the target power.  Even favorable model
specializations leave positive powers of \(R\); those are upper-price
limitations, not lower bounds.

The first open estimate is precisely the scalar in (145.6).  Already
its \(t=1\) layer needs a signed saving across \(s\), unless a genuinely
joint estimate cancels different \(t\)-layers.  The independent
Round-138 cross owner, lower GAR, both direct M1 parents, M9-M1, all M2
owners, endpoint uniformity, M9, the bridge, and the quarter theorem
remain open.  The internally proved exponent remains \(1/3\), and the
separately audited external exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reviews/conductor_round145_squarefree_kernel_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/candidates/conductor_round145_squarefree_kernel_reduction.md;
- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/controls/conductor_round145_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reviews/discovery_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reviews/blind_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reviews/source_conductor_candidate_final_green.md.

## Round 146 accepted unmasking reduction and three-variable dispersion obstruction

Let \(\mathfrak S_N^{<,>}\) denote the masked scalar in (145.6), and
let \(\mathfrak U_N^<\) be the same sum with the nearest-square mask
removed. The ambient squarefree-kernel support is the exact disjoint
partition

\[
\{t<M^{1/4},|j|>M^{3/4}\}
\dot\cup
\{t<M^{1/4},|j|\leq M^{3/4}\}
\dot\cup
\{t\geq\lceil M^{1/4}\rceil\}.
\tag{146.1}
\]

The middle set is a subset of the accepted Round-144 absolute cell
owner, and the last set is the accepted Round-145 unmasked tail.
Consequently,

\[
\boxed{
\mathfrak T_N=\mathfrak S_N^{<,>}+
O_{\varepsilon,V}(X^\varepsilon)
=\mathfrak U_N^<+O_{\varepsilon,V}(X^\varepsilon),}
\tag{146.2}
\]

where

\[
\boxed{
\mathfrak U_N^<=
\sum_M\sum_{1\leq t<M^{1/4}}
\sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M}}
(st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
C(st^2)e(t\sqrt{Ns}).}
\tag{146.3}
\]

Thus the nearest-square mask is no longer part of the first open
lower-cone estimate.

Using the squarefree-common-kernel parametrization, the literal
\(t,d,e\) coefficient is

\[
\kappa_t(d,e)=
1_{\mu^2(de)=1}1_{e\ {\rm odd}}\chi_4(e)
\sum_{\substack{\gamma\mid t,\ \mu^2(\gamma)=1\\
                 (\gamma,de)=1,\ \gamma\ {\rm odd}}}
\chi_4(\gamma)
\sum_{\substack{ab=t/\gamma,\ b\ {\rm odd}\\
                 eb^2>4da^2}}1.
\tag{146.4}
\]

It retains squarefree support, pairwise coprimality, parity, character,
and the strict cone. In general it is not a product of one-variable or
two-block coefficients.

On a dyadic box \(t\asymp T,d\asymp D,e\asymp E\), one has
\(T^2DE\asymp M\) and the coefficient-blind price

\[
\mathfrak U_{M,T,D,E}
\ll_{\varepsilon,V}X^\varepsilon {M^{1/4}\over T}.
\tag{146.5}
\]

For \(f(t,d,e)=\sqrt N\,t\sqrt{de}\), the scaled Hessian is

\[
f^{-1}\operatorname{diag}(t,d,e)\nabla^2f
\operatorname{diag}(t,d,e)=
\begin{pmatrix}
0&1/2&1/2\\
1/2&-1/4&1/4\\
1/2&1/4&-1/4
\end{pmatrix},
\quad
\det={1\over4},
\tag{146.6}
\]

with eigenvalues \(-1/2,\pm1/\sqrt2\). This algebraic
nondegeneracy does not itself yield a sum estimate. The \(t=1\) and
\(D=1\) faces are mandatory and rank one; \(E=1\) is empty, while
bounded \(E\) is terminal-safe. A \(t\)-difference has a constant
diagonal at shift zero and the rank-one phase
\(h\sqrt{Nde}\) at nonzero shift, together with an unproved exact
coefficient correlation.

The full smooth stationary phase is

\[
-{2u\sqrt{vw}\over\sqrt N},
\tag{146.7}
\]

so after reversing the second alias orthant the transform returns the
same monomial only at phase level. The amplitude, support, and
coefficient do not return as an accepted identity, and bounding the
whole alias box by triangle inequality is adverse.

The strongest favorable audited source test is Cao--Zhai Theorem 6.
Its only legal variable placement is
\((d,t,e)\) with monomial exponents \((1/2,1,1/2)\), but it requires
the unavailable coefficient factorization \(a(d)b(t,e)\). Even
granting that factorization, its dominant balanced top-block term is

\[
R^{3/8-5\tau/8+\varepsilon},
\tag{146.8}
\]

which leaves \(R^{1/16+\varepsilon}\) at the formal
\(\tau=1/2\) endpoint. The audited Robert--Sargos and Sargos--Wu
bounds leave \(R^{1/4+\varepsilon}\) there. These are limitations of
the displayed upper bounds, not signed lower bounds.

The exact unmasked scalar (146.3) remains open. In particular, its
\(t=1\) face requires a sign-sensitive two-variable squarefree-cone
estimate unless a new joint theorem couples the \(t\)-layers while
retaining (146.4).

The independent Round-138 cross owner, lower GAR, both direct M1
parents, M9-M1, all M2 owners, endpoint uniformity, M9, the bridge,
and the quarter theorem remain open. The internally proved exponent
remains \(1/3\), and the separately audited external exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reviews/conductor_round146_three_variable_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md;
- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/controls/conductor_round146_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reviews/discovery_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reviews/blind_conductor_candidate_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reviews/source_conductor_candidate_final_green_v2.md.

## Round 147 accepted fixed-order \(t=1\) Voronoi reduction and squarefree-\(H\) obstruction

For the mandatory \(t=1\) face, put

\[
C(s)=\sum_{\substack{de=s\\e\ {
m odd}\\e>4d}}\chi _4(e).
\tag{147.1}
\]

If \(s=2^\nu n\), where \(\nu\in\{0,1\}\) and \(n\) is odd and
squarefree, then exactly

\[
\boxed{C(2^\nu n)=
\sum_{\substack{e\mid n\\e>2^{1+\nu/2}\sqrt n}}\chi _4(e).}
\tag{147.2}
\]

Pairing \(e\) with \(n/e\) retains a complete
positive-total-character sector and a mandatory antisymmetric
negative-total-character tail. Thus the strict cone coefficient cannot
be replaced by a complete nonnegative divisor coefficient.

A collar \(|e-4d|\leq\sqrt D\) costs \(D^{3/2}=M^{3/4}\) before the
physical \(M^{-3/4}\) weight and is target-safe. On the complement, a
local \(d\asymp D\) Mellin partition gives

\[
d^{-it}(e/d)^{i\tau}
=(de)^{-it/2}(e/d)^{i(\tau+t/2)},
\qquad z=i(\tau+t/2),
\tag{147.3}
\]

with radial twist \(s^{-it/2}\), external factor
\(D^{it}4^{-i\tau}\), and smooth bandwidth
\(|\tau|\lesssim D^{1/2}X^\varepsilon\). A hard Perron realization
instead needs height comparable with \(D\) and retains its zero
residue.

Define

\[
A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z,
\qquad B_z(n)=\mu^2(n)A_z(n).
\tag{147.4}
\]

Then

\[
B_z=h_z*A_z,
\qquad
\sum_{n\geq1}{A_z(n)\over n^w}
=\zeta(w+z)L(w-z,\chi _4).
\tag{147.5}
\]

The exact two-adic and odd local factors of \(H\) make \(h_z\)
powerful-supported. They also give the corrected refactorization

\[
H(w,z)=
{\mathscr K(w,z)\over
 \zeta(2w+2z)\zeta(2w-2z)L(2w,\chi _4)},
\tag{147.6}
\]

where, at an odd prime with local variables \(a,b\),

\[
\mathscr K_p=
{1+a+b\over(1+a)(1+b)(1-ab)}
=1+{a^2b+ab^2+a^2b^2\over(1+a)(1+b)(1-ab)}.
\tag{147.7}
\]

Hence \(\mathscr K\) is absolutely convergent for
\(\Re w>(1+|\Re z|)/3\). This does not license a residue-free shift
through zeros of the reciprocal zeta and \(L\) factors.

For every fixed \(|\Re z|<1/4\) and compact-smooth radial test, the
conductor-four transform has scalar \(\pi4^z\), one polar term, the
reflected coefficient \(A_{-z}\), and all \(J/Y/K\) branches at
argument \(2\pi\sqrt{mx}\). If
\(K_F=\lfloor\sup\operatorname{supp}F\rfloor\), its physical
squarefree convolution is finite in \(k\leq K_F=O(M)\); for every
\(k>K_F\), the polar and dual zero contributions cancel for that same
\(k\).

At fixed order the negative Bessel branch resonates at

\[
\boxed{m=kN+O\!\left(k\sqrt{N/M}\right),}
\tag{147.8}
\]

and one resonant term has raw size \(M^{3/4}/(kR)\), hence physical
size \(1/(kR)\). A theorem uniform through the growing unitary cone
orders and every moving prefix is not yet proved.

Even granting that analytic theorem, termwise primal/dual optimization
followed by modulus over powerful \(k\) has physical capacity

\[
X^\varepsilon
\begin{cases}
M^{1/4},&M\leq R^{4/3},\\
R^{1/2}M^{-1/8},&R^{4/3}\leq M\leq R^2.
\end{cases}
\tag{147.9}
\]

It loses \(R^{1/3}\) at \(M=R^{4/3}\) and \(R^{1/4}\) at the top.
These are adverse upper-bound capacities, not signed lower bounds.

The separate elementary estimate

\[
\sum_{q\asymp Q}\left|\sum_{d\asymp D}e(Nd/q)\right|
\ll_\varepsilon (Q+D)(NQ)^\varepsilon,
\qquad Q\leq N/4,
\tag{147.10}
\]

is exact for the bare reciprocal average. Expanding \(\mu^2(d)\) and
taking triangle gives only \(QD^{1/2}+D\), before the remaining
coprimality, parity, character, cone, and prefix conditions.

Thus, for the separate-\(t=1\) route, the first open analytic seam is
uniform growing-order and moving-prefix control of every \(J/Y/K\)
regime. Granting it, the first open arithmetic seam is the signed
physical correlation

\[
\sum_{\substack{k\leq K_F\\k\ {
m powerful}}}{h_z(k)\over k}
\sum_{|j|\lesssim k\sqrt{N/M}}
A_{-z}(kN+j)\mathcal W_{k,z,U}(j)
\ll_\varepsilon X^\varepsilon,
\tag{147.11}
\]

integrated over the actual cone orders, or an equivalent
squarefree/coprime strengthening of (147.10). A separate \(t=1\)
estimate is sufficient for a layerwise proof, but is not necessary for
a theorem using cancellation across \(t\)-layers.

The separate \(t=1\) target, every \(t\geq2\) layer, and the independent
Round-138 cross owner remain open. So do lower GAR, both direct M1
parents, M9-M1, every M2 owner, endpoint uniformity, M9, the bridge, and
the quarter theorem. The internal exponent remains \(1/3\); the audited
external exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reviews/conductor_round147_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/controls/conductor_round147_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reviews/source_conductor_round147_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reviews/blind_conductor_round147_final_green.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reviews/discovery_conductor_round147_final_green_v2.md.

## Round 148 accepted squarefree reciprocal transform and scoped dispersion obstruction

Let (R=X^{1/4}), (N=lfloor X
floor),
(DEasymp Mleq R^2), and (Dleqsqrt M). After the accepted
product and cone collars, define the exact finite progression set

$$
 \mathcal P(d)=\{(\alpha,b):\alpha,b\ {\rm odd},\ b\mid d,
 \ \mu(\alpha)\mu(b)\ne0,\ \alpha^2\leq e_+\ll E,
 \ \mathscr A(d,[\alpha^2,b]n)\ne0\text{ for some }n\geq1\}.
\tag{148.1}
$$

Put (ell=[alpha^2,b]) and

$$
 Q=2\sqrt{ND/E}\asymp D\sqrt{N/M}.
\tag{148.2}
$$

The retained (t=1) squarefree-cone box has the exact one-sided
reciprocal presentation

$$
 \mathcal S_{D,E,U}
 =\frac{e(1/8)}{N^{1/4}D}\mathcal T_{D,E,U}
 +O_{\varepsilon,V}(X^\varepsilon),
\tag{148.3}
$$

where

$$
\begin{aligned}
 \mathcal T_{D,E,U}={}&
 \sum_d\mu^2(d)\frac Dd
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \mu(\alpha)\mu(b)\frac{\chi_4(\ell)}{\ell}\\
 &\quad\times
 \sum_{\substack{q>0\\q\ {\rm odd}}}
 \chi_4(q)\mathscr W_{d,\ell,U}(q)
 e\!\left(\frac{Nd\ell}{q}\right),
\end{aligned}
\tag{148.4}
$$

with

$$
 \mathscr W_{d,\ell,U}(q)
 =\mathscr A\!\left(d,\frac{4Nd\ell^2}{q^2}\right),
 \qquad q\asymp\ell Q.
\tag{148.5}
$$

The character-Poisson factor is (i/2). The positive saddle has

$$
 x_0=\frac{4Nd\ell}{q^2},\qquad
 e_0=\frac{4Nd\ell^2}{q^2},\qquad
 \lambda=\frac{Nd\ell}{q},
\tag{148.6}
$$

and the exact substitution (x=x_0(1+u)^2) makes its phase
(lambda(1-u^2)). Thus the leading integral has unit
(e(-1/8)), and multiplication by (i/2) produces the global
(e(1/8)) in (148.3).

The (K=6) stationary and nonstationary expansion is uniform after
summing the finite mass

$$
 \sum_d\sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q:q\asymp\ell Q\}
 \ll_\varepsilon DQ\sqrt E\,X^\varepsilon.
\tag{148.7}
$$

The four frequency ranges, scaled tail derivative, dyadic
(2^{-5v}) tail, complementary Taylor subtraction, extended-domain
tail, lower symbols, negative frequencies, and endpoint buffer have
total cost (O_{\varepsilon,V}(X^\varepsilon)). Hence the exact
remaining target is

$$
 \boxed{|\mathcal T_{D,E,U}|\ll_{\varepsilon,V}RD X^\varepsilon.}
\tag{148.8}
$$

This estimate is not proved.

If (g=(ell,q)), (L=ell/g), and (q_0=q/g), then the correct
reduced phase and resonance coordinate are

$$
 e(Nd\ell/q)=e(NLd/q_0),\qquad
 j=NL-Aq_0,\qquad q_0\mid NL-j.
\tag{148.9}
$$

The bare coordinate (j=N-Aq) applies only to the unexpanded
(ell=1) cell. The fully reduced additive denominator is

$$
 q_*=\frac q{(q,\ell N)}=\frac{q_0}{(q_0,N)}.
\tag{148.10}
$$

The (j=0) family and the aggregate (q_*\leq Y\leq R) stratum are
target-safe; the complete nonzero-(j) signed family remains open.

There is a rigorous obstruction to one specific proof placement. On a
long interior prefix, the literal (b=1) cells have absolute mass

$$
 \mathscr L\asymp Q\sqrt E.
\tag{148.11}
$$

If those cells remain unrecombined, coefficient-weighted Cauchy is
applied, and the (d_1=d_2) contribution is then majorized separately
and positively, every positive weighting has diagonal capacity at least

$$
 \sqrt D\,\mathscr L
 \asymp Q\sqrt M=\sqrt N\,D=R(RD).
\tag{148.12}
$$

This factor-(R) loss is a method capacity, not a lower bound for the
signed scalar. It does not exclude pre-Cauchy Euler recombination,
signed cross-cell energy, common-divisor effects, or the additional
(N)-dependent alignment congruence

$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2}.
\tag{148.13}
$$

The audited progression, variance, inverse-square, inverse-fraction,
and separable large-sieve results do not supply the required
varying-(q), coefficient-coupled estimate. The exact-denominator
Schlage--Puchta specialization is nonexhaustive. There is also no
termwise identification of the lcm index (ell) with the powerful
Round-147 (H)-index: the reciprocal (j)-band is a factor (D)
wider than the formal (H)-band.

The first open arithmetic seam is therefore a joint signed estimate for
(148.4) before any separately positive diagonal, or an exact Euler
recombination followed by a signed theorem for the Round-147
(H)-correlation. Every (t\geq2) layer and the independent Round-138
cross owner remain open. So do lower GAR, both direct M1 parents,
M9--M1, every M2 owner, endpoint uniformity, M9, the bridge, and the
quarter theorem. The internal exponent remains (1/3); the audited
external exponent remains ((3292+25\sqrt{1717})/13762).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/conductor_round148_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/controls/conductor_round148_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/source_conductor_round148_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/blind_conductor_round148_candidate_final_v2.md.

## Round 149 accepted gcd-lift compression and moving-row energy boundary

Retain the Round-148 notation

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
\tag{149.1}
$$

For squarefree \(d\), put \(d_{\mathrm o}=d/(d,2)\).  Summing every
odd squarefree Möbius pair with the same lcm gives

$$
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&
  n=uv^2,\quad u\mid d_{\mathrm o},\quad
  u,v\ {\rm odd},\quad \mu^2(uv)=1,\quad(v,d)=1,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{149.2}
$$

At an odd prime \(p\mid d_{\mathrm o}\), the exponent-two
contributions are \(-1,+1\) and cancel.  The prime \(2\) is absent
from the lcm ledger, even when \(d\) is even.

Let \(\kappa_{d,U}(n)\) be the exact finite indicator that the
original \(n\)-progression meets the clipped amplitude.  With
\(\ell=gL\), \(q=gq_0\), and \((L,q_0)=1\), define

$$
 B_{d,U}(L)=
 \sum_{\substack{g\geq1\\g\ {\rm odd}}}
 \frac{C_d(gL)\kappa_{d,U}(gL)}g.
\tag{149.3}
$$

This is an exact finite regrouping because
\(\chi_4(g)^2=1\), the phase and profile depend only on \(L/q_0\),
and \(q\asymp\ell Q\) is equivalent to \(q_0\asymp LQ\).  Hence

$$
 \mathcal T_{D,E,U}
 =\sum_{d\asymp D}\mu^2(d)\frac Dd\,G_U(d),
\tag{149.4}
$$

$$
 G_U(d)=
 \sum_{\substack{L,q_0\geq1\ {\rm odd}\\
                 (L,q_0)=1\\q_0\asymp LQ}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)e(NdL/q_0).
\tag{149.5}
$$

The exact prefix may be irregular.  Nevertheless,

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon X^\varepsilon.
\tag{149.6}
$$

Indeed, if \(L=ts^2\), \(a=(t,d_{\mathrm o})\), and \(r=t/a\),
the exact lift parameterization gives
\(|B_{d,U}(L)|\ll_\varepsilon X^\varepsilon/r\).  The two norms
then reduce respectively to convergent \(r^{-3}\) and \(r^{-2}\)
ledgers, with the divisor price
\(\sum_{a\mid d_{\mathrm o}}a^{-1}\ll X^\varepsilon\).

There are \(O(LQ)\) admissible \(q_0\) for each \(L\), so the literal
equal-cell contribution to the joint energy is

$$
 \mathscr E_{\rm diag}
 \ll_\varepsilon DQX^\varepsilon
 \leq R^2DX^\varepsilon.
\tag{149.7}
$$

All exact \(N\)-dependent phase classes are also target-safe.  For

$$
 q_1=HA,\qquad q_2=HB,\qquad(A,B)=1,\qquad
 \delta=L_1B-L_2A,
\tag{149.8}
$$

a distinct exact alignment satisfies

$$
 HAB\mid N\delta,\qquad
 AB\mid N,\qquad H\mid(N/AB)\delta.
\tag{149.9}
$$

The distinct exact off-diagonal is
\(O_\varepsilon(DX^\varepsilon)\); including the literal diagonal,
all exact phase classes are
\(O_\varepsilon(DQX^\varepsilon)\).  This retains common factors,
imprimitive denominators, \(q_0\mid N\), and even squarefree rows.

The sufficient energy estimate

$$
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \stackrel{?}{\ll_\varepsilon}R^2DX^\varepsilon
\tag{149.10}
$$

is not proved.  For nonexact cells, write
\(q_{0,i}=hr_i\), \((r_1,r_2)=1\),
\(\delta=L_1r_2-L_2r_1\), and

$$
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\leq hr_1r_2/2.
\tag{149.11}
$$

The first open collar is

$$
 0<|\rho|\leq \frac{hr_1r_2}{D}.
\tag{149.12}
$$

Its \(d\)-kernel retains both \(B_{d,U}\)'s, both moving profiles,
both exact prefixes, squarefreeness, and the mod-four signs.
Montgomery--Vaughan's primal and dual large sieves require one common
coefficient vector and do not apply verbatim.  The audited
squarefree-progression, inverse-fraction, and partially fixed-modulus
theorems have different coefficients, phases, averages, separability,
diagonals, or ranges.  Even the illegal fixed-vector unwrapped-spacing
diagnostic has capacity \(Q(D+M)X^\varepsilon\), losing
\(\sqrt M\) in energy.  This is a method capacity, not a signed lower
bound.

The first open theorem is therefore the nonexact moving-coefficient
near/generic correlation, or a complete Euler recombination producing
a genuinely source-legal signed family.  Every \(t\geq2\) layer and
the independent Round-138 cross owner remain open.  So do lower GAR,
both direct M1 parents, M9--M1, every M2 owner, endpoint uniformity,
M9, the bridge, and the quarter theorem.  The internal exponent
remains \(1/3\); the audited external exponent remains
\((3292+25\sqrt{1717})/13762\).

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reviews/conductor_round149_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/controls/conductor_round149_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reviews/blind_conductor_round149_math_review_v2.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reviews/source_conductor_round149_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reviews/discovery_source_conductor_round149_review.md.

## Round 150 accepted fixed-wrap collar range and large-wrap boundary

Retain

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

Write a squarefree row as $d=\eta m$, where
$\eta\in\{1,2\}$ and $m=d_{\mathrm o}$ is odd squarefree.  For
$L_i=t_is_i^2$, expand $a_i\mid t_i$, put $c_i=t_i/a_i$, and retain
the literal $u_i,v_i$ and prefix sums.  The arithmetic dependence of
the two-row divisibility masks is exactly

$$
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m},
$$

where

$$
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
$$

At fixed $(L_1,L_2)$ this arithmetic incidence expansion has scalar
projective norm $O_\varepsilon(X^\varepsilon)$.  The two exact prefix
values and two samples of $\mathscr W_{d,U}$ remain joint row-cell
functions; the projective statement does not include them.

The closed Round-149 coefficient formula gives the further
prefix-uniform estimate

$$
 \sum_{L\ll E}\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.
$$

Indeed, if $L=acs^2$ with $a\mid d_{\mathrm o}$, then
$|B_{d,U}(L)|\ll X^\varepsilon/c$, and the norm is bounded by

$$
 X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}a^{-1/2}
 \sum_{c\ge1}c^{-3/2}
 \sum_{s\le\sqrt E}s^{-1}
 \ll_\varepsilon X^\varepsilon.
$$

For two reduced cells put

$$
 q_i=hr_i,\qquad (r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
$$

and choose the centered integer $k$ so that

$$
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\le hr_1r_2/2.
$$

In the nonexact collar $0<|\rho|\le hr_1r_2/D$, fix
$L_1,L_2,h,k,r_1$ and set $S=NL_1-khr_1$,
$\alpha=hr_1/D$.  Every supported solution has
$r_i\asymp L_iQ/h$, $S\asymp NL_1$, and
$\alpha/S\ll Q/(DN)$.  Hence the possible $r_2$ lie in an interval
of length

$$
 \ll\frac{L_2Q^2}{hDN}=\frac{4L_2}{hE}\ll1.
$$

The symmetric count gives

$$
 \mathcal N_k(L_1,L_2;h)
 \ll\frac{Q\min(L_1,L_2)}h.
$$

After the literal $1/(L_1L_2)$ weights, the harmonic $h$ sum, and the
half-weight norm, every fixed wrap contributes

$$
 \mathcal A_{k,U}\ll_\varepsilon DQX^\varepsilon.
$$

Therefore any selected wrap packet with

$$
 |\mathcal K|\ll1+\frac{R^2}{Q}
 \asymp1+\frac{\sqrt M}{D}
$$

satisfies

$$
 \mathcal A_{\mathcal K,U}
 \ll_\varepsilon R^2DX^\varepsilon.
$$

This includes the complete nonexact $k=0$ collar and a symmetric
small-wrap packet.  The proof is absolute, is uniform for all
$L_i\ll E$, and includes even squarefree rows, common factors,
imprimitive denominators, denominators dividing $N$, and every exact
finite prefix.  It does not assert that the full centered collar has
only this many wraps.

If $M$ is bounded absolutely, then $D,E,L=O(1)$ and $Q\asymp R^2$.
The accepted Round-148 actual-profile factorization and derivative
ledger give bounded $q$-variation.  On each allowed residue class
modulo $4L$, the phase $NdL/q$ has one-sign second derivative
$\asymp R^{-2}$ on $O(R^2)$ integers.  The weighted second-derivative
estimate and Abel summation yield

$$
 |G_U(d)|\ll_\varepsilon RX^\varepsilon,
 \qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2DX^\varepsilon.
$$

This bounded-scale result uses the actual profile, not an arbitrary
bounded smooth function.  The same placement has first term
$RM^{1/4}$ for growing $M$ and proves no all-scale row bound.

For $k\ne0$, one has

$$
 (NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh\rho,
$$

$$
 r_2(NL_1-khr_1)=NL_2r_1+\rho,\qquad
 r_1(NL_2+khr_2)=NL_1r_2-\rho.
$$

Both factors are positive on the collar.  Fixed
$(L_1,L_2,h,k,\rho)$ has divisor multiplicity $X^\varepsilon$, but
separately summing all legal shifts gives adverse raw capacity

$$
 \frac{NL_1L_2Q}{D}X^\varepsilon,
$$

which exceeds trivial pair capacity by
$N/(DQ)\asymp R^2\sqrt M/D^2\ge R$.  This is a no-go for separate
absolute per-shift summation, not a signed lower bound.

The first open collar is the growing-$M$ symmetric large-wrap band
outside $|k|\ll1+R^2/Q$.  The full wrap range has size $N/Q$, a
factor $R^2$ larger than the owned packet.  At $D=1,L_1=L_2=1$, the
residual is the literal $\chi_4$ reciprocal sum with no row average.
The audited double-large-sieve, quadratic-divisor, determinant,
inverse-fraction, and fixed-shift squarefree theorems do not directly
match its coefficient, separability, shifts, local cluster forms, or
powers.  A joint signed wrap theorem or further exact recombination is
still needed.  The growing-$M$ generic non-collar remains separate.

Every $t\ge2$ layer and the independent Round-138 cross owner remain
open.  So do lower GAR, both direct M1 parents, M9--M1, every M2
owner, endpoint uniformity, M9, the bridge, and the quarter theorem.
The internal exponent remains $1/3$; the audited external exponent
remains $(3292+25\sqrt{1717})/13762$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/conductor_round150_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/controls/conductor_round150_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/blind_fixed_wrap_lemma_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/independent_conductor_round150_math_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/source_conductor_round150_final.md.

## Round 151 accepted large-wrap character ranges and reciprocal boundary

Retain the Round-150 compressed row and put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
\tag{151.1}
$$

For $q_i=hr_i$, $(r_1,r_2)=1$, write

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
 \qquad |\rho|\le hr_1r_2/2.
\tag{151.2}
$$

In the nonexact collar $0<|\rho|\le hr_1r_2/D$, assume $k\ne0$,
put $j=\nu_2(|k|)$, and define

$$
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
\tag{151.3}
$$

The exact identities

$$
 AB=N^2L_1L_2+kh\rho,
\tag{151.4}
$$

$$
 r_2A=NL_2r_1+\rho,\qquad
 r_1B=NL_1r_2-\rho
\tag{151.5}
$$

make both shifted factors positive on support, including when a
denominator divides $N$.  If $k=2^j\kappa$ with $\kappa$ signed odd,
then

$$
 x=\frac{NL_1-A}{2^j}=\kappa hr_1,\qquad
 y=\frac{B-NL_2}{2^j}=\kappa hr_2
\tag{151.6}
$$

are odd, nonzero, and have the same sign.  Therefore

$$
 \boxed{\chi_4(L_1L_2r_1r_2)=\chi_4(L_1L_2xy)}.
\tag{151.7}
$$

This holds for both signs of $k$ and every parity of $N$.  The shifted
factors $A,B$ themselves may be even and are not lawful character
arguments.

The inverse map has a compulsory divisor fibre.  Given $A,B,j,L_1,L_2$,
let

$$
 g=(|x|,|y|),\qquad \epsilon=\operatorname {sgn}x,
 \qquad r_1=|x|/g,\quad r_2=|y|/g.
\tag{151.8}
$$

Every preimage is indexed by an admissible positive odd divisor $h\mid g$
with

$$
 k=\epsilon2^jg/h,\qquad kh=\epsilon2^jg.
\tag{151.9}
$$

All original support, coprimality, centeredness, collar, packet, prefix,
and profile tests must be reimposed.  Although the fibre has
$O_\varepsilon(X^\varepsilon)$ elements, it cannot be suppressed because
$q_i=hr_i$, $k$, both profile samples, and the phase denominator vary with
$h$.

Support and centering give $|k|\ll N/Q$.  Choose
$2^{J_*}\asymp N/R^2\asymp R^2$.  The wraps with
$\nu_2(|k|)\ge J_*$ occupy only

$$
 O\!\left(1+\frac{N}{Q2^{J_*}}\right)
 =O(1+R^2/Q)
\tag{151.10}
$$

classes.  The accepted arbitrary fixed-wrap theorem therefore gives the
complete absolute contribution

$$
 \ll_\varepsilon DQ(1+R^2/Q)X^\varepsilon
 \ll_\varepsilon R^2DX^\varepsilon.
\tag{151.11}
$$

There is also an all-scale actual-profile variation theorem.  On writing
$q=LQy$, the physical sample is

$$
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\tag{151.12}
$$

The Round-148 factorization has bounded bulk variation, radial derivative
$O(M^{1/2})$ on normalized width $O(M^{-1/2})$, and cone derivative
$O(D^{1/2})$ on width $O(D^{-1/2})$.  Finite products and components
therefore give

$$
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname {Var}_q\mathscr W_{d,U}(L/q)
 \ll_\varepsilon X^\varepsilon
\tag{151.13}
$$

at every allowed scale.  Hard collars keep their prior owners, and the
exact prefix in $B_{d,U}(L)$ is independent of $q$.

Resolve $(L,q)=1$ by Mobius inversion, write $q=c(4n+a)$, and use an
unweighted interval estimate before Abel summation.  The progression
length and phase parameter satisfy

$$
 H_c\asymp LQ/c,\qquad
 \mathcal T_c\asymp Nd/Q,\qquad
 \mathcal T_c/H_c\asymp cE/L.
\tag{151.14}
$$

For an audited exponent pair $(\kappa,\lambda)$ this gives

$$
 |S_{d,L}|\ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda X^\varepsilon.
\tag{151.15}
$$

The fixed comparable edge $\mathcal T_c<H_c$ is covered separately by a
second-derivative estimate.  Bourgain's Theorem 6, unlike the narrower
direct Theorem-4 calculation, is a global exponent-pair statement for the
standard derivative class.  With $(\kappa,\lambda)=(13/84,55/84)$ and the
accepted half-weight coefficient norm,

$$
 |G_U(d)|\ll_\varepsilon
 E^{13/84}Q^{55/84}X^\varepsilon.
\tag{151.16}
$$

Its energy is target-safe exactly in the corridor

$$
 \boxed{D^{84}R^{52}\ll M^{29}.}
\tag{151.17}
$$

At $M\asymp R^2$, this permits $D\ll R^{1/14}$.  For $D=1$, every
centered nonexact pair is a collar pair, so subtracting the accepted exact
and packet owners yields the complete large-wrap collar in this range.
For $D>1$, this is a whole-row theorem controlling collar and generic
pieces jointly, not an isolated signed collar estimate.

The Tao--Trudgian--Yang pair $(89/1282,997/1282)$ gives, for $L\le L_0$,

$$
 |G_{U,\le L_0}(d)|\ll_\varepsilon
 E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon,
\tag{151.18}
$$

with target-safe low-low energy under

$$
 \boxed{M^{819}\gg R^{1424}D^{1816}L_0^{534}.}
\tag{151.19}
$$

For $D=L_0=1$, this begins at $M\gg R^{1424/819}$.  At
$M\asymp R^2$, it is $D^{1816}L_0^{534}\ll R^{214}$.  The
$L>L_0$ square and low-high cross term are not included.

Finally, at $D=d=L=1$, retain
$\widetilde S_U=B_{1,U}(1)S_U$ and

$$
 S_U=\sum_{q>0}\chi_4(q)
 \mathscr A_{1,M,U}(1,4N/q^2)e(N/q).
\tag{151.20}
$$

Extending the compact actual profile by zero and using

$$
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
\tag{151.21}
$$

gives the boundary-complete transform

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
\tag{151.22}
$$

$$
 P_U=\sum_{\substack{\ell>0\\\ell\ \mathrm{odd}}}
 \chi_4(\ell)\ell^{-3/4}
 \mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell}).
\tag{151.23}
$$

A second stationary transform returns the reciprocal phase and principal
symbol, but not every lower symbol or endpoint term.  The elementary
capacities are

$$
 \min\{R^2M^{-1/2},RM^{1/4}\}X^\varepsilon,
\tag{151.24}
$$

so a bare iteration gives no intermediate-scale gain.  Outside the strict
ranges, the first missing endpoint estimate is
$|P_U|\ll_\varepsilon X^\varepsilon$.  In general the first isolated
survivor is the low-two-adic recovered $h\mid g$ sum outside the row
corridors.  The growing-$M$ generic sector, all $t\ge2$ layers, and the
Round-138 cross owner remain open.

No downstream theorem or exponent changes.  The internal exponent remains
$1/3$, and the audited external exponent remains
$(3292+25\sqrt{1717})/13762$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/conductor_round151_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/candidates/conductor_round151_character_ranges_and_bprocess_boundary.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/controls/conductor_round151_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/independent_conductor_round151_math_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/source_conductor_round151_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/independent_bprocess_candidate_final.md;
- sources/bourgain_2017_exponent_pair.md.

## Round 153 accepted complete-Mobius recombination obstruction

This section records only the accepted node
`M9-M1-lower-cone-t1-d1-squarefree-mobius-collapse-obstruction`. It does
not estimate the remaining scalar.

Retain

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad S=\lceil M^{1/4}\rceil,
\tag{153.1}
$$

and the literal direct large-defect weight

$$
 F_U(n)={\bf1}_{n\ \mathrm{odd}}
 {\bf1}_{|k(n)^2-Nn|>J}
 \chi_4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}),
\tag{153.2}
$$

where the actual profile is extended by zero with its accepted support,
endpoint, and transition conventions. The external coefficient
$B_{1,U}(1)$ remains outside this scalar. The Round-152 survivor is

$$
 P_U^*=\sum_{\substack{s<S\\s\ \mathrm{odd}}}
 \sum_{\tau\ \mathrm{odd}}\mu^2(\tau)F_U(\tau s^2).
\tag{153.3}
$$

Insert the exact finite identity

$$
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),
 \qquad \tau=a^2b,
\tag{153.4}
$$

and put $r=as$. No coprimality is introduced among $\tau,s,a,b$. Since
the complete summand depends on $(a,s)$ only through $r$, define

$$
 C_S(r)=\sum_{\substack{a\mid r\\r/a<S}}\mu(a)
 \qquad(r\ \mathrm{odd}).
\tag{153.5}
$$

Finite reordering gives the exact identity

$$
 P_U^*=\sum_{r\ \mathrm{odd}}C_S(r)
 \sum_{b\ \mathrm{odd}}F_U(r^2b).
\tag{153.6}
$$

If $r<S$, every divisor $a\mid r$ satisfies $r/a<S$, and therefore

$$
 C_S(r)=\sum_{a\mid r}\mu(a)
 =\begin{cases}1,&r=1,\\0,&1<r<S.\end{cases}
\tag{153.7}
$$

The strict ceiling is exact: an admissible odd equality $r=S$ belongs to
the boundary. On the zero-extended support, $r^2b\asymp M$,
$|C_S(r)|\le d(r)\ll_\varepsilon X^\varepsilon$, there are
$O(1+M/r^2)$ possible positive odd $b$, and
$|F_U(r^2b)|\ll_\varepsilon M^{-3/4}X^\varepsilon$. Hence

$$
\begin{aligned}
 \left|\sum_{\substack{r\ge S\\r\ \mathrm{odd}}}
 C_S(r)\sum_{b\ \mathrm{odd}}F_U(r^2b)\right|
 &\ll_\varepsilon M^{-3/4}X^\varepsilon
 \sum_{S\le r\ll\sqrt M}\left(1+\frac M{r^2}\right)\\
 &\ll_\varepsilon
 \left(M^{-1/4}+\frac{M^{1/4}}S\right)X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{153.8}
$$

Therefore

$$
 \boxed{P_U^*=\sum_{b\ \mathrm{odd}}F_U(b)
 +O_\varepsilon(X^\varepsilon).}
\tag{153.9}
$$

The independent seam review identifies the boundary exactly as the
negative of the accepted Round-152 large-square-factor sector. Restoring
the accepted exact- and small-defect owners gives

$$
 \boxed{P_U^*=P_U+O_\varepsilon(X^\varepsilon).}
\tag{153.10}
$$

Thus complete squarefree Mobius inversion followed by complete
recombination returns the original direct large-defect wave. The dyadic
$a$- and $s$-pieces are not independent owners: for $1<r<S$, their signed
preimages cancel exactly. The boundary $r\ge S$ is target-safe.

This is a route-scoped obstruction. It does not rule out a future
coefficient-sensitive signed estimate before recombination. Cauchy
diagonals, algebraic spacing counts, ambient pigeonhole capacities, and
positive terms on an external theorem's upper-bound right-hand side are not
signed lower bounds. The Round-152 exact- and small-defect masks may be
removed at scalar level before Cauchy, with divisor-bounded expanded
multiplicity, but may not be deleted inside a signed correlation.

The first open estimate remains

$$
 \left|\sum_{b\ \mathrm{odd}}F_U(b)\right|
 \ll_\varepsilon X^\varepsilon
 \qquad(M^{449}\ll R^{780}).
\tag{153.11}
$$

The best licensed one-variable source bound remains

$$
 \ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon
 +X^\varepsilon,
\tag{153.12}
$$

so Round 153 gives no new range. The $D>1$ and $L>1$ lower-cone owners,
generic $t=1$, every original $t\ge2$ layer, the cross owner, remaining
M1 and all M2 owners, endpoint uniformity, M9, the bridge, and the quarter
target remain open. The internal exponent stays $1/3$, and the audited
external Li--Yang exponent stays
$(3292+25\sqrt{1717})/13762$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/candidates/conductor_round153_mobius_boundary_collapse.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reviews/independent_round153_mobius_collapse_math_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reviews/hostile_round153_bilinear_scope_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reviews/source_conductor_round153_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reviews/conductor_round153_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/controls/conductor_round153_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/synthesis.md.

## Round 154 accepted root-defect collar and completion obstruction

This section records only the accepted nodes
`M9-M1-lower-cone-t1-d1-root-defect-logarithmic-collar-reduction`,
`M9-M1-d1-theta-kloosterman-source-audit`, and
`M9-M1-lower-cone-t1-d1-root-dispersion-obstruction`. It does not prove
the remaining direct wave.

Retain

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad K=\sqrt{NM},\qquad 1\ll M\le R^2,
\tag{154.1}
$$

and the literal zero-extended profile
$w_U(n)=n^{-3/4}A_U(n)$, with

$$
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{154.2}
$$

The external factor $B_{1,U}(1)$ remains outside the scalar. Put

$$
 Q_U=\sum_{\substack{n>0,\ n\ \mathrm{odd}\\
 |k(n)^2-Nn|>J}}
 \chi_4(n)w_U(n)e(\sqrt{Nn}),\qquad
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor.
\tag{154.3}
$$

There is no half-integer tie. With $j=k^2-Nn$, the exact nearest cell and
its converse give the bijection

$$
 \boxed{
 Q_U=\sum_{\substack{k\ge1,\ -k\le j\le k-1,\ |j|>J\\
 N\mid k^2-j,\ (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right).}
\tag{154.4}
$$

On literal support, $k\asymp K$, the total $k$-span is $O(K)<N$,
$2k<N$, and the selected map has multiplicity one for sufficiently large
$X$. The phase identity

$$
 -\frac{j}{k+\sqrt{k^2-j}}
 =-\frac{j}{2k}
 -\frac{j^2}{2k(k+\sqrt{k^2-j})^2}
\tag{154.5}
$$

holds throughout the exact cell. Pricing it only on the selected
$O(M)$-point graph, replacement by $e(-j/(2k))$ costs

$$
 O_\varepsilon\!\left(N^{-1/2}M^{-1/4}X^\varepsilon\right).
\tag{154.6}
$$

For $j\ne0$, let
$\rho_N(j)=\#\{x\bmod N:x^2\equiv j\pmod N\}$. The all-parity bound

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)},\qquad
 \sum_{0<|j|\le H}\rho_N(j)\ll_\varepsilon HX^\varepsilon
 \quad(1\le H<N)
\tag{154.7}
$$

and the actual weight prove that, for every fixed $A>0$, the complete
collar

$$
 M^{3/4}<|j|\le M^{3/4}(\log(2X))^A
\tag{154.8}
$$

contributes $O_{\varepsilon,A}(X^\varepsilon)$. Hence $Q_U$ equals the
same literal signed wave restricted to
$|j|>M^{3/4}(\log(2X))^A$, with the linearized phase, up to a target-safe
error. This is a fixed-polylogarithmic collar only. Replacing the collar
factor by $M^\delta$ leaves an unabsorbed $M^\delta$ for every fixed
$\delta>0$.

For every integer $t$, the exact quotient selector is

$$
 {\bf1}_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi_4(h)e\!\left(\frac{ht}{4N}\right).
\tag{154.9}
$$

After $t=Nn$ has already been selected, its unnormalized odd rows are
$iQ_U$ or $-iQ_U$, and therefore normalized $h$-Cauchy is the equality

$$
 \frac1{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}|T_h|^2
 =|Q_U|^2.
\tag{154.10}
$$

This rank collapse is post-selection only. In the lawful ambient array the
rows remain distinct. Put $q=4N$, $d=(h,N)$, and $q'=q/d$. Exact finite
$k$-completion, including the imprimitive Gauss factor, gives the fully
normalized family

$$
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{q'}
 \sum_{v\bmod(q'/2)}
 \widehat B_j(2dv)K(-v^2,-j;q').
\tag{154.11}
$$

Here $K$ is the Duke--Friedlander--Iwaniec theta-multiplier Kloosterman
sum. Since $q'\equiv0\pmod4$, their Lemma 6.1 applies exactly:

$$
 |K(m,n;c)|\le(m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{154.12}
$$

Restoring every gcd stratum, nonzero dual mode, zero mode, defect sign,
profile endpoint, and outer $j$-sum yields, on
$V<|j|\le2V$,

$$
 |Q_U(V)|\ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{154.13}
$$

This certifies fixed or polylogarithmic first collars, but at
$V\asymp K$ its first term is $N^{1/2}M^{-1/4}$. It is an upper bound,
not a signed lower bound.

If the accepted exact and small defects are restored at scalar level, the
full nearest cells partition the positive integers. For the centered row
$h=4N-a$, the principal saddle has

$$
 n_*=\frac{4N}{a^2},\qquad e(\Psi_*)=e(N/a),
\tag{154.14}
$$

and symbol

$$
 e(1/8)N^{-1/4}\chi_4(a)A_U(4N/a^2).
\tag{154.15}
$$

With the accepted Round-152 transition, endpoint, and remainder ledger,
this is exactly the previously accepted reciprocal row. The principal
full-cell transform therefore self-returns and supplies no new gain.

The first open input is a signed outer-defect estimate for the normalized
family in (154.11), throughout

$$
 M^{3/4}(\log(2X))^A\lesssim V\lesssim\sqrt{NM},
\tag{154.16}
$$

or an equivalent selected cross-fibre theorem for $e(-j/(2k))$, retaining
both signs, every gcd stratum, the zero mode, actual profile, mask, and
cell endpoints. For odd $N$, $\chi_4((k^2-j)/N)$ is constant within a
fixed-$j$ root fibre, so any character cancellation must survive the
outer $j$-ordering.

The $D>1$ recovery fibre, $L>1$ rows, growing-$M$ generic $t=1$ sector,
every original $t\ge2$ layer, the Round-138 cross owner, remaining M1 and
all M2 owners, endpoint uniformity, M9, the bridge, and the quarter target
remain open. The internal exponent remains $1/3$, and the audited external
Li--Yang exponent remains $(3292+25\sqrt{1717})/13762$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/large_defect_root_dispersion_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/blind_quadratic_root_wave_feasibility.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/quadratic_root_completion_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/math_conductor_round154_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/hostile_conductor_round154_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/source_conductor_round154_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/conductor_round154_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/controls/conductor_round154_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/synthesis.md.

## Round 155: complete theta-frequency inversion and the remaining zero row

Fix $A>0$ and retain the Round-154 signed linearized defect blocks on

$$
 J_A=M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM}.
\tag{155.1}
$$

For the exact pre-linearization ambient completion, put

$$
 q=4N,\qquad d\mid N\ \mathrm{odd},\qquad
 c=q/d,\qquad H=c/2.
\tag{155.2}
$$

With the literal coefficient $B_j$ and the DFI theta sum, one has the
pointwise identity

$$
 \boxed{
 \begin{aligned}
 &\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &\quad=\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
 \end{aligned}}
\tag{155.3}
$$

Indeed, for every unit $a\bmod c$,

$$
 \sum_{v\bmod H}e_c(-\bar a v^2-2xv)
 =\frac{1-i}{2}\epsilon_a
 \left(\frac ca\right)\sqrt c\,e_c(ax^2).
\tag{155.4}
$$

The half-period is exact because $4\mid c$. The multiplier already in
$K$ squares to $\chi_4(a)$. Restoring the exterior completion factor gives

$$
 -\frac{i(1+i)}{2Nq}d\sqrt c\,
 \frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\frac{dc}{q}=-\frac{i}{2N}.
\tag{155.5}
$$

Every odd $h\bmod4N$ has the unique decomposition
$d=(h,N)$, $h=da$, even when $d$ and $N/d$ are not coprime. Summing
these strata therefore restores the original quotient selector. Complete
dual resummation is exactly the inverse of the quadratic Gauss completion
and supplies no second square-root gain.

For later norm placements, sampled Parseval is

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}
 \left|\sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x)\right|^2.
\tag{155.6}
$$

The folds have period $H=2N/d$, not only the physical diagonal, and

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 \ll_\varepsilon
 \left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\tag{155.7}
$$

The mandatory zero row satisfies only the upper bound

$$
 |\mathcal T_{0,U}(V)|\ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon,
\tag{155.8}
$$

while the nonzero termwise ledger remains
$M^{-3/4}VX^\varepsilon$. At $V=K$, the first zero-row term is
$M^{1/4}$. This is an upper capacity, not a lower bound.

For a proper dual cutoff $\eta$, square completion gives

$$
 \sum_{v\bmod H}\eta(v)e_c(-\bar a v^2-2xv)
 =e_c(ax^2)\sum_{u\bmod H}\eta(u-ax)e_c(-\bar a u^2).
\tag{155.9}
$$

Thus every incomplete transform retains joint $(a,x)$ dependence. A
hypothetical square-root gain over the selected defect incidences has
capacity $M^{-3/4}V^{1/2}X^\varepsilon$, which is target-sized only for
$V\le M^{3/2}$; no such estimate is proved.

The flat selected phase has only $O(V/K)$ variation. Its exact expansion
localizes at most to the circular reciprocal arc

$$
 \left\|\frac ac+\frac1{2\sqrt{x^2-j}}\right\|_{\mathbb R/\mathbb Z}
 \ll\frac1V,
\tag{155.10}
$$

of capacity $O(1+c/V)$. The arc wraps through zero, so both its near-zero
and near-$c$ representatives must remain. This localization gives no
cancellation by itself.

The first source-unproved input is now the signed fixed-modulus row

$$
 \sum_{V<|j|\le2V}\widehat B_j(0)K(0,-j;4N/d),
\tag{155.11}
$$

uniformly in every odd $d\mid N$, both signs, the actual profile, and all
endpoints. After that comes the incomplete nonzero matrix or the equivalent
selected cross-fibre partial-sum theorem. Current DFI and Sun spectral
formulas average the modulus and exclude the zero shifted frequency; the
fixed-modulus bilinear matches have the wrong kernel or separated
coefficients. This is a direct-interface no-match, not an impossibility
theorem.

The fixed-polylogarithmic collar remains the last proved defect range.
No positive-power range, $M$-boundary, downstream theorem, endpoint
assembly, or exponent changes. The internal global exponent remains
$1/3$, and the separately audited external Li--Yang exponent remains
$(3292+25\sqrt{1717})/13762$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/candidates/conductor_round155_theta_dispersion_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/outer_defect_spectral_dispersion_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/blind_linearized_cross_fibre_feasibility.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/theta_bilinear_spectral_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/independent_inverse_gauss_math_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/independent_spectral_source_review.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/hostile_conductor_round155_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/controls/conductor_round155_controls.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/synthesis.md.

## Round 156: exact signed cancellation of the complete theta zero row

Retain the Round-155 notation

$$
 q=4N,\qquad c=\frac{4N}{d},\qquad
 M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM}.
\tag{156.1}
$$

For the literal zero Fourier coefficient
$A_j=\widehat B_j(0)$, including the zero-extended real profile, exact
ambient residual phase, asymmetric nearest cell, strict block mask,
transitions, and endpoints, one has on each signed block

$$
 \sup_j|A_j|+\operatorname {Var}_j A_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{156.2}
$$

For fixed physical $x$, the profile argument $(x^2-j)/N$ is monotone, so
sampling contracts the total variation of the actual real profile. The
exact phase identity

$$
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x,\qquad
 \left|\partial_j(\sqrt{x^2-j}-x)\right|\ll K^{-1}
\tag{156.3}
$$

costs only $O(V/K)\le O(1)$ variation. Zero extension charges every
transition and boundary jump, and summing over the $O(KX^\varepsilon)$
physical representatives proves (156.2). Ordered arithmetic
subsequences do not increase variation.

Define the exact quotient-character root function

$$
 \mathscr S_N(j)=
 \sum_{x\bmod4N}{\bf1}_{N\mid x^2-j}
 \chi_4\!\left(\frac{x^2-j}{N}\right).
\tag{156.4}
$$

The quotient projector, the unique partition $d=(h,N)$ of every odd
frequency $h\bmod4N$, and the complete even quadratic Gauss sum give

$$
 \boxed{
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c).}
\tag{156.5}
$$

Equivalently,

$$
 \mathscr S_N(j)=
 \rho_{4N}(j+N)-\rho_{4N}(j+3N),
\tag{156.6}
$$

so no imprimitive divisor or two-adic root stratum has been averaged
away. Its finite Fourier transform vanishes at even frequencies, while
for odd $h$

$$
 \left|\widetilde{\mathscr S}_N(h)\right|
 =2\sqrt{8N(h,N)}.
\tag{156.7}
$$

Finite Fourier inversion, the geometric-series bound, and divisor
grouping therefore prove, for every consecutive interval $I$ with
$|I|\le4N$,

$$
 \sup_I\left|\sum_{j\in I}\mathscr S_N(j)\right|
 \ll \sqrt N\,\tau(N)\log(2N).
\tag{156.8}
$$

By (156.5), the normalized mandatory zero row is exactly

$$
 \mathcal Z_U(V)=
 \frac1{4N}\sum_{V<|j|\le2V}A_j\mathscr S_N(j).
\tag{156.9}
$$

Discrete Abel summation on the two sign intervals, (156.2), and (156.8)
give the full frozen-range estimate

$$
 \boxed{
 \mathcal Z_U(V)\ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.}
\tag{156.10}
$$

This is a signed improvement over the Round-155 absolute upper capacity,
which contained $M^{1/4}$ at the top. An independent fixed-$d$ check
opens the nonzero additive unit frequencies and proves

$$
 \sup_I\left|\sum_{j\in I}K(0,-j;c)\right|
 \ll c\log(2c),
\tag{156.11}
$$

giving the same final power after restoring all odd $d\mid N$.

For completeness, if $m=N/d=u^2r$ with $r$ squarefree, the two real
characters in $K(0,-j;4m)$ have fundamental discriminants

$$
 \Delta_+=
 \begin{cases}r,&r\equiv1\pmod4,\\4r,&r\equiv2,3\pmod4,\end{cases}
 \qquad
 \Delta_-=
 \begin{cases}-r,&r\equiv3\pmod4,\\-4r,&r\equiv1,2\pmod4.\end{cases}
\tag{156.12}
$$

For a primitive constituent $\chi$ of conductor $f$ induced to
$c=fL$, its exact transform is

$$
 G_{c,\chi}(n)=\tau(\chi)
 \sum_{\substack{e\mid R_f\\L/e\mid n}}
 \mu(e)\chi(e)\frac Le\,
 \overline\chi\!\left(\frac{n}{L/e}\right),
 \qquad
 R_f=\prod_{\substack{p\mid c\\p\nmid f}}p.
\tag{156.13}
$$

The accepted local ledger includes every odd prime power, conductors
$1$, $4$, and $8$, the conductor-one Ramanujan shells, exact phases, and
the two-adic half-support. These formulas validate all arithmetic strata;
the target proof itself uses their exact recombination rather than their
absolute support capacity.

The first open term is now the incomplete nonzero matrix

$$
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\tag{156.14}
$$

The zero-row interval identities do not estimate this coupled
$(j,v)$-matrix. Consequently the fixed-polylogarithmic collar remains
the last proved range for the complete D=1 wave, and the boundary
$M^{449}\asymp R^{780}$ is unchanged. Every $D>1$, $L>1$, generic
$t=1$, original $t\ge2$, cross, remaining M1, and M2 owner remains
separate. Endpoint uniformity, M9, the bridge, and the quarter theorem
remain open. The internal global exponent remains $1/3$, and the audited
external Li--Yang exponent remains
$(3292+25\sqrt{1717})/13762=0.3144831759740614\ldots$.

Accepted evidence:

- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_target.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/zero_mode_local_factor_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/blind_zero_mode_character_rederivation.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/zero_mode_character_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/independent_recombination_math_round156.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/independent_source_round156_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/hostile_profile_endpoint_round156_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/conductor_round156_adjudication.md;
- proofs/kernels/m9_m1_d1_theta_zero_row.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/synthesis.md.

## Round 157: exact nonzero centering and target-safe Nyquist fold

Retain

$$
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,
\tag{157.1}
$$

and, for every odd \(d\mid N\),

$$
 c=\frac{4N}{d},\qquad H=\frac c2,\qquad n=\frac Nd.
\tag{157.2}
$$

Put

$$
 G_N(t)=\mathbf{1}_{N\mid t}\chi_4(t/N),\qquad
 A_j=\widehat B_j(0),\qquad
 B_j^\circ(x)=B_j(x)-\frac{A_j}{4N}.
\tag{157.3}
$$

The complete half-period identity from Round 155 and the exact zero-row
recombination from Round 156 imply

$$
 \boxed{
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}
 B_j^\circ(x)G_N(x^2-j).}
\tag{157.4}
$$

Thus the centering constant is exactly \(1/(4N)\).  The global constant
tail is the single closed zero row; it has zero sampled Fourier
coefficient at every nonzero mode and is not discarded by a pointwise
smallness shortcut.

Because \(K(-v^2,-j;c)\) is invariant under \(v\mapsto H-v\), every
two-element nonzero orbit has the exact contribution

$$
 \left(\widehat B_j(2dv)+\widehat B_j(-2dv)\right)
 K(-v^2,-j;c),
 \qquad 1\le v<H/2.
\tag{157.5}
$$

The coefficient \(B_j\) is complex, so no conjugacy is used.  The unique
nonzero fixed point is

$$
 v=\frac H2=n,\qquad 2dv=\frac q2.
\tag{157.6}
$$

For the literal zero-extended profile, exact residual phase, asymmetric
cell, transitions, and endpoints, monotone profile sampling and

$$
 \left|
 \frac{\partial}{\partial x}
 \left(\sqrt{x^2-j}-x\right)
 \right|
 \ll\frac V{K^2}
\tag{157.7}
$$

give

$$
 \sup_x|B_j(x)|+\operatorname {Var}_x B_j
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{157.8}
$$

Partial sums of \((-1)^x\) are bounded, so complex Abel summation proves

$$
 C_j:=\widehat B_j(q/2)
 =\sum_{x\bmod q}(-1)^xB_j(x)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{157.9}
$$

On either signed block put \(D_j=(-1)^jC_j\).  Crude variation gives

$$
 \sup_j|D_j|+\operatorname {Var}_jD_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{157.10}
$$

Opening the theta kernel after this demodulation yields

$$
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 =
 \sum_{u\bmod c}^{*}
 \epsilon_u\left(\frac cu\right)e_c(-\bar u n^2)
 \sum_{j\in I}e_c((c/2-u)j).
\tag{157.11}
$$

For every unit \(u\bmod c\), \(c/2-u\) is a nonzero unit.  Complete
periods vanish, including when \(|I|>c\), and finite geometric
summation gives

$$
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{157.12}
$$

Restoring the full exterior factor and every odd divisor stratum yields

$$
\begin{aligned}
 |\mathcal F_U(V)|
 &\ll_\varepsilon
 \frac{K M^{-3/4}}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon\\
 &\ll_\varepsilon M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{157.13}
$$

This proves the unique nonzero Nyquist row target-sized for arbitrary
\(N\), all odd \(d\mid N\), both defect signs, the complex phase,
transitions, strict endpoints, and the edge case \(c=4\).

The selected-incidence capacity is also corrected.  On
\(j=k^2-Nm\), the nearest-cell intervals

$$
 k^2-k+1\le Nm\le k^2+k
\tag{157.14}
$$

partition the positive integers as \(k\) varies.  Hence each positive
\(m\) determines one \((k,j)\), and

$$
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{157.15}
$$

Conditional on a future genuine signed square-root theorem, its
coefficient cost would be

$$
 M^{-3/4}L_U(V)^{1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon
\tag{157.16}
$$

for every selected \(V\).  Equation (157.15) is unsigned support
cardinality and proves no cancellation or new range.

The accepted one-variable BV data do not imply the ideal mixed
rectangular norm: the moving-cell boundary has a diagonal atomic trace,
and the control class permits mixed absolute capacity
\(VM^{-3/4}X^\varepsilon\).  Ordinary centered completion proves only

$$
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll \sqrt N\,\tau(N)(\log(2N))^2,
\tag{157.17}
$$

which restores \(N^{1/2}M^{-3/4}X^\varepsilon\) even under the ideal
mixed norm.  The audited fixed-frequency, Fourier-\(L^1\), sampled
Parseval, and generic operator/nuclear-norm placements likewise retain
positive powers.  These are route-scoped capacity statements, not lower
bounds or impossibility theorems.

No audited primary theorem through 25 August 2026 matches the fixed
arbitrary-even-composite theta multiplier with the entrywise coefficient
\(\widehat B_j(2dv)\), all divisor strata, folds, signs, and endpoints.
DFI Lemma 6.1 remains the exact pointwise kernel theorem.  The source
conclusion is a cutoff-dated direct-interface no-match.

The first open object is the paired interior matrix

$$
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{1\le v<H/2}
 \left(\widehat B_j(2dv)+\widehat B_j(-2dv)\right)
 K(-v^2,-j;c).
\tag{157.18}
$$

It requires a joint mask-preserving signed theorem, or an exactly
equivalent selected signed incidence theorem, retaining the diagonal
cell trace, literal profile, complex phase, signs, transitions,
endpoints, all odd divisor strata, and the external scalar seam.

Consequently the fixed-polylogarithmic collar remains the last proved
range for the complete \(D=1\) wave.  Every \(D>1\), \(L>1\), generic
\(t=1\), original \(t\ge2\), cross, remaining M1, and M2 owner remains
separate.  Endpoint uniformity, M9, the bridge, and the quarter theorem
remain open.  The internal global exponent remains \(1/3\), and the
audited external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/centered_nonzero_root_discrepancy_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/candidates/conductor_round157_nyquist_fold_target.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/independent_centered_math_round157.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/independent_nyquist_fold_round157.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/hostile_profile_scope_round157.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/independent_source_round157.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/conductor_round157_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/state_patch_scope_round157.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/synthesis.md.

## Round 158: exact paired-interior cell-trace reduction

Retain the Round 157 normalization and put, for every odd (d\mid N),

$$
 q=4N,\qquad c=\frac qd,\qquad H=\frac c2,\qquad
 n=\frac H2=\frac Nd.
\tag{158.1}
$$

On the exact positive and negative blocks write

$$
 B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x),
 \qquad\lambda_+(j)=j+1,\qquad\lambda_-(j)=-j,
\tag{158.2}
$$

where (F_j) retains the literal zero-extended profile, complex
residual phase, asymmetric cell, component transitions, half-open
choices, and hard endpoints.  Define

$$
 P^+_{d,v}(j)=\sum_{s=a_+}^{j}K(-v^2,-s;c),\qquad
 P^-_{d,v}(j)=\sum_{s=j}^{b_-}K(-v^2,-s;c).
\tag{158.3}
$$

The exact coefficient differences are

$$
\begin{aligned}
 \widehat B_{j+1}(2dv)-\widehat B_j(2dv)
 ={}&-F_j(j+1)e_c(-2v(j+1))\\
 &+\sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx)
\end{aligned}
\tag{158.4}
$$

on the positive block, and

$$
\begin{aligned}
 \widehat B_j(2dv)-\widehat B_{j-1}(2dv)
 ={}&F_j(-j)e_c(2vj)\\
 &+\sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx)
\end{aligned}
\tag{158.5}
$$

on the negative block.  Hence finite Abel summation puts the moving
atom in with a positive sign on both sides.  It also exposes the exact
positive right outer endpoint
(widehat B_{b_+}(2dv)P^+_{d,v}(b_+)), the negative left outer
endpoint (widehat B_{a_-}(2dv)P^-_{d,v}(a_-)), and two
profile-difference remainders.  Those four terms are not part of the
isolated moving-cell trace and remain open.

The accepted half-period inverse identity is

$$
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =\frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)).
\tag{158.6}
$$

Since

$$
 -\frac{i(1+i)}{2Nq}\frac{1-i}{2}dc=-\frac{i}{2N},
\tag{158.7}
$$

the all-odd-divisor recombination gives the full-frequency physical
trace

$$
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
   \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
   \sum_{s=j}^{b_-}G_N(j^2-s).
\end{aligned}
\tag{158.8}
$$

Let (mathcal Z_{\mathrm{tr}}) and
(mathcal F_{\mathrm{tr}}) denote the individual (v=0) and
(v=H/2) Abel-trace pieces.  Opening the actual theta kernel and
summing every nonzero additive unit frequency geometrically proves

$$
 \sup_I\left|\sum_{s\in I}K(-v^2,-s;c)\right|
 \ll c\log(2c).
\tag{158.9}
$$

Restoring all divisors and exterior factors therefore gives, separately,

$$
 |\mathcal Z_{\mathrm{tr}}|+|\mathcal F_{\mathrm{tr}}|
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\tag{158.10}
$$

This is a direct trace-level proof, not a transfer of the complete zero
or Nyquist row theorem.  In particular,

$$
 \mathcal C_{\mathrm{int},U}
 =\mathcal C_+^{\mathrm{full}}+\mathcal C_-^{\mathrm{full}}
  -\mathcal Z_{\mathrm{tr}}-\mathcal F_{\mathrm{tr}}.
\tag{158.11}
$$

The endpoint (s=j) produces (j^2+j+1) and (j(j-1)).  The second
polynomial has exactly two roots modulo every prime power.  For the
first polynomial, there is no (2)-adic root; the unique root modulo
(3) does not lift modulo (9); and for (p\ne2,3) there are two
simple roots modulo every (p^\nu) exactly when
(p\equiv1\pmod3).  The Chinese remainder theorem gives only
(O_\varepsilon(N^\varepsilon)) endpoint atoms in either block, so

$$
 |\mathcal E_{\mathrm{full}}|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{158.12}
$$

Delete this endpoint face and put

$$
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell.
\tag{158.13}
$$

The exact strict selectors are

$$
\begin{aligned}
 \eta_+(\ell)&=
 \mathbf 1_{a_++1\le\kappa(\ell)\le b_+}
 \mathbf 1_{a_+\le r(\ell)\le\kappa(\ell)-2},\\
 \eta_-(\ell)&=
 \mathbf 1_{-b_-\le\kappa(\ell)\le-a_--1}
 \mathbf 1_{-\kappa(\ell)+1\le r(\ell)\le b_-}.
\end{aligned}
\tag{158.14}
$$

Their boundary-frozen weights are

$$
\begin{aligned}
 W_+(k)&=
 w_U\!\left(\frac{k^2-k+1}{N}\right)
 e(\sqrt{k^2-k+1}-k),\\
 W_-(k)&=
 w_U\!\left(\frac{k^2+k}{N}\right)
 e(\sqrt{k^2+k}-k).
\end{aligned}
\tag{158.15}
$$

The character is evaluated at the selected quotient (ell), whereas
the two profile arguments in (158.15) lie strictly below and above
(ell), respectively.  They cannot be replaced by one common
(w_U(\ell)), identified by conjugacy, or paired automatically.

The accepted exact reduction is

$$
 \boxed{
 \mathcal C_{\mathrm{int},U}(V)
 =\sum_{\ell\ge1}\chi_4(\ell)
 \left[\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\right]
 +O_\varepsilon(M^{-1/4}X^\varepsilon).}
\tag{158.16}
$$

The nearest-cell partition gives

$$
 L_{\mathrm{str}}(V)
 \ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{158.17}
$$

Literal boundary support also proves that the moving trace is zero
unless (V\asymp K=\sqrt{NM}).  On this only possibly nonzero range,
(V\gg M), so (158.17) can still have size (M).  With atom size
(M^{-3/4}X^\varepsilon), absolute summation gives only
(M^{1/4}X^\varepsilon).

The frozen scalar target is (O_\varepsilon(X^\varepsilon)).  Thus
the first open trace theorem is the raw estimate

$$
 \left|\sum_{\ell\asymp M}\chi_4(\ell)
 \left[\eta_+(\ell)\widetilde W_+(\kappa(\ell))
      +\eta_-(\ell)\widetilde W_-(\kappa(\ell))\right]\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{158.18}
$$

after removing the atom scale.  Raw square-root cancellation would be
sufficient but is stronger than necessary.

An explicit dyadic family produces a strict arithmetic selected point
whose endpoint polynomial is nonresonant.  It is a survivor control,
conditional on the literal profile being nonzero at the displayed
boundary argument, not a lower bound for (158.18).

The named second-derivative discrepancy, classical exponent-pair, and
incomplete-quadratic placements reach the raw threshold only at
(M\ge N^{2/3}), outside (M\le N^{1/2}).  Even after favorable
fixed-endpoint, unit-BV, and residual-phase-BV grants, the most favorable
stated transformed exponent-pair line in the Round 158 source audit
requires

$$
 M\ge N^{390/703}>N^{1/2}.
\tag{158.19}
$$

No audited primary theorem through 25 August 2026 accepts the literal
root-indexed coefficient, both moving strict selectors, arbitrary even
composite modulus, quotient sign, and restored target.  The residual
boundary phase remains (k)-dependent inside the coefficient; it is not
a fixed Fourier-frequency shift.  These are qualified upper capacities
and a cutoff-dated source no-match, not a lower bound or impossibility
theorem.

Consequently the strict trace (158.18), both Abel outer endpoints, and
both profile-bulk remainders remain open before the full paired interior
matrix can close.  The fixed-polylogarithmic collar is still the last
proved range for the complete (D=1) wave.  Every other M1 and M2
owner, endpoint uniformity, M9, the bridge, and the quarter theorem
remain open.  The internal global exponent remains (1/3), and the
audited external Li--Yang exponent remains
((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots).

Accepted evidence:

- proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reports/sign_adapted_cell_trace_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/candidates/conductor_round158_strict_survivor_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/independent_blind_reconciliation_round158.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/independent_trace_math_round158.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/hostile_profile_power_round158.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reports/cell_trace_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/independent_source_round158.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/conductor_round158_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/state_patch_scope_round158.md.

## Round 159: full Abel recombination and common-profile self-return

Round 158 isolated the moving-cell trace, but it did not recombine the two
outer endpoints and two literal profile-difference terms.  Round 159 closes
that algebraic seam before making any estimate.

Set (N=\lfloor X\rfloor), (q=4N), (K=\sqrt{NM}), and retain

$$
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\tag{159.1}
$$

For each odd (d\mid N), put (c=q/d), (H=c/2), and (n=H/2=N/d).
Let

$$
 B_j(x)=\mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right)
\tag{159.2}
$$

on the inherited complete nonwrapping physical lift, with all profile
components zero-extended.  Write

$$
 a=\lfloor V\rfloor+1,\qquad b=\lfloor2V\rfloor,
$$

and define empty reversed sums to be zero.  For fixed ((d,v)), abbreviate

$$
 A_j=\widehat B_j(2dv),\qquad K_j=K(-v^2,-j;c),
$$

and put

$$
 P^+(j)=\sum_{s=a}^{j}K_s,\qquad
 P^-(j)=\sum_{s=j}^{-a}K_s.
\tag{159.3}
$$

The exact pointwise differences are

$$
\begin{aligned}
 B_j-B_{j+1}&=T_j^++R_j^+,\\
 T_j^+(x)&=\mathbf1_{x=j+1}F_j(x),\\
 R_j^+(x)&=\mathbf1_{x\ge j+2}(F_j(x)-F_{j+1}(x)),
\end{aligned}
\tag{159.4}
$$

and

$$
\begin{aligned}
 B_j-B_{j-1}&=T_j^-+R_j^-,\\
 T_j^-(x)&=\mathbf1_{x=-j}F_j(x),\\
 R_j^-(x)&=\mathbf1_{x\ge-j+1}(F_j(x)-F_{j-1}(x)).
\end{aligned}
\tag{159.5}
$$

Finite prefix and suffix summation therefore give

$$
\begin{aligned}
 \sum_{j=a}^{b}A_jK_j
 ={}&A_bP^+(b)
 +\sum_{j=a}^{b-1}P^+(j)\widehat T_j^+(2dv)
 +\sum_{j=a}^{b-1}P^+(j)\widehat R_j^+(2dv),\\
 \sum_{j=-b}^{-a}A_jK_j
 ={}&A_{-b}P^-(-b)
 +\sum_{j=-b+1}^{-a}P^-(j)\widehat T_j^-(2dv)
 +\sum_{j=-b+1}^{-a}P^-(j)\widehat R_j^-(2dv).
\end{aligned}
\tag{159.6}
$$

Both moving atoms have positive sign.  More importantly, the positive
outer, moving, and profile-difference lines reconstruct the original
positive row, and the three negative lines reconstruct the original
negative row, separately for every (d) and (v).  No individual line is
estimated in this assertion.

The accepted inverse identity and exterior factor give

$$
 -\frac{i(1+i)}{2Nq}\chi_4(d)d\sqrt c
 \cdot\frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\chi_4(d).
\tag{159.7}
$$

The map (h=du\pmod{4N}), with (d=(h,N)), partitions the odd residues,
so the full divisor and frequency sum restores

$$
 G_N(t)=\mathbf1_{N\mid t}\chi_4(t/N).
\tag{159.8}
$$

Let (\mathcal Z_U(V)) and (\mathcal F_U(V)) denote the whole zero and
Nyquist rows.  Recombining all six Abel lines before inversion proves

$$
 \boxed{
 \mathcal T_{\mathrm{int},U}(V)
 =\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal F_U(V),}
\tag{159.9}
$$

where

$$
 \mathcal S_U(V)=
 \sum_{V<|j|\le2V}\sum_{x\in\mathcal L_U}
 B_j(x)G_N(x^2-j),
\tag{159.10}
$$

and

$$
 |\mathcal Z_U(V)|+|\mathcal F_U(V)|
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\tag{159.11}
$$

The two whole special rows are subtracted exactly once.  The special pieces
of the isolated Round-158 trace are not subtracted again.

If (x^2-j=N\ell), the literal cell is

$$
 x^2-x+1\le N\ell\le x^2+x.
\tag{159.12}
$$

These integer intervals partition the positive integers.  Fixed-dilation
support and the inherited compatible lift contain their unique nonwrapping
root hull.  Thus

$$
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell
\tag{159.13}
$$

give the unique selected pair, and

$$
 \boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf1_{V<|r(\ell)|\le2V}.}
\tag{159.14}
$$

Using (w_U(\ell)=\ell^{-3/4}A_U(\ell)), this is exactly the accepted
Round-154 hard dyadic common-profile root-defect block.  It is not a new
analytic object.  The two boundary-frozen profiles of the isolated
Round-158 trace remain distinct; the quotient profile is restored only by
the full six-line telescope.

Write (w_U=M^{-3/4}\widetilde w_U).  The desired normalized bound is
(O_\varepsilon(X^\varepsilon)), equivalently the still-open raw estimate

$$
 \left|
 \sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf1_{V<|r(\ell)|\le2V}
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{159.15}
$$

For (\delta=\sqrt{N\ell}-\kappa(\ell)),

$$
 r=-\delta(2\kappa+\delta).
\tag{159.16}
$$

The mask has four moving endpoints, a strict inner (V)-edge, a closed
outer (2V)-edge, and centered-cell clipping.  It is not a fixed
fractional interval.  Fourier frequency (h) changes the built-in phase to
frequency (h+1).  The exceptional (h=-1) coefficient retains
(\chi_4); bounded coefficient variation and character Abel summation give
a raw (O_\varepsilon(X^\varepsilon)) bound.  This closes only one mode.

The complete ordinary discrepancy ledger is

$$
 \left(\frac M Q+\sqrt{KQ}+\frac M{\sqrt K}+1\right)X^\varepsilon,
\tag{159.17}
$$

and reaches the raw target only for (M\ge N^{2/3}).  The literal
Vaaler--Fejér/root-incidence error is

$$
 E_J\ll_\varepsilon
 \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon.
\tag{159.18}
$$

At (J=KM^{-3/4}), the favorable transformed pair
((195/796,235/398)) has raw capacity

$$
 N^{195/796}M^{1295/3184+\varepsilon},
\tag{159.19}
$$

which reaches the target only if (M^{1093}\ge N^{780}).  The older
(M^{703}\ge N^{390}) condition belongs only to a favorable fixed-boundary
model with an unproved (M/J) surrogate.

For shifted frequency (q_1=h+1\ne0), the convention-independent
stationary data are

$$
 d=4m\mp1,\qquad
 \ell_{q_1,d}=\frac{4q_1^2N}{d^2},\qquad
 e\!\left(\frac{q_1^2N}{d}\right).
\tag{159.20}
$$

The (q_1=\pm1) branches return the accepted reciprocal carrier, and
general (q_1) supplies no automatic gain.  Favorable incomplete-quadratic
completion has raw capacity (N^{1/2}X^\varepsilon) and again needs
(M\ge N^{2/3}).  These are route-scoped upper capacities, not lower bounds
or impossibility theorems.

Consequently the full paired-interior Abel presentation has no remaining
algebraic seam, but (159.15) remains open uniformly on
(M^{449}\ll R^{780}), (R=X^{1/4}), beyond the accepted
fixed-polylogarithmic collar.  For the named Fourier route, the first
missing input is signed hard-boundary incidence when (V>M^{3/2}), or a
joint estimate for all nonzero moving modes when (V\le M^{3/2}).

Nothing here transfers to (D>1), (L>1), generic (t=1), original
(t\ge2), cross terms, another M1 or M2 owner, endpoint uniformity, M9, the
bridge, or the quarter theorem.  The internal global exponent remains
(1/3); the audited external Li--Yang exponent remains
((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots).

Accepted evidence:

- proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reports/full_abel_commutator_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reports/common_profile_mask_method_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reviews/independent_lift_normalization_round159.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reviews/independent_kernel_line_round159.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reviews/hostile_power_source_round159.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reviews/conductor_round159_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reviews/state_patch_scope_round159.md.

## Round 160: inverse-selector reciprocity and scalar projective obstruction

Round 160 returns to the flat-smooth strict-UNBAL M2 owner after the
centered nonzero-frequency reduction. Put

$$
 X=N_0+\xi,\qquad D=X^\delta,\qquad L=X^\ell,\qquad
 R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac DL,
\tag{160.1}
$$

under the frozen strict hypotheses. For odd (g,n), (gn\asymp R), retain
the literal moving support and define

$$
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
 \qquad
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_{(j,n)=1}b_{g,n}(j)e(-h\overline j_n/n).
\tag{160.2}
$$

For every coprime (j,n), arbitrary inverse representatives, every integer
(h), and even or odd (j),

$$
 \boxed{
 e(-h\overline j_n/n)
 =e(h\overline n_j/j-h/(jn)).}
\tag{160.3}
$$

Indeed, (j\overline j_n+n\overline n_j-1) is divisible by (jn).
After the accepted switched-cusp identity, the centered quadruple summand
is exactly

$$
 \frac{\chi_4(g)\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}+\frac{h\overline n_j}{j}
                 -\frac{h}{jn}\right)S(N_0,h;n),
\tag{160.4}
$$

with all (1\le h<n), profiles, support entries and exits, real-centre
factors, gcd strata, and both character directions retained.

Complete (h\bmod n) orthogonality gives

$$
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
 =\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n),
\tag{160.5}
$$

which is the original reciprocal row. Thus complete frequency summation
is a self-return, not a saving. The accepted Ramanujan row is precisely
(h=0\pmod n) and is removed once.

The new finite kernel statement is exact. For
(A\subseteq U_j=(\mathbb Z/j\mathbb Z)^\times), (M=|A|), set

$$
 F_{j,A}(u,h)=e(h\overline u_j/j),
 \qquad u\in A,\quad1\le h\le j-1.
\tag{160.6}
$$

Then

$$
 \boxed{F_{j,A}F_{j,A}^*=jI_M-\mathbf1\mathbf1^*.}
\tag{160.7}
$$

The singular values are (\sqrt j) with multiplicity (M-1) and
(\sqrt{j-M}) once, so

$$
 \|F_{j,A}\|_{S_1}=(M-1)\sqrt j+\sqrt{j-M},
 \qquad
 \|F_{j,A}\|_{S_2}^2=M(j-1).
\tag{160.8}
$$

The nuclear norm is the infimum of the Hilbert projective mass over exact
rank-one decompositions. Consequently exact scalarization followed
termwise by triangle costs, for all unit classes,

$$
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
 \asymp\sqrt{\varphi(j)}=j^{1/2-o(1)}.
\tag{160.9}
$$

Here (j/\varphi(j)\le2^{\omega(j)}\le d(j)\ll_\varepsilon j^\varepsilon).
Adding the positive column (h=j) and normalizing by (j^{-1/2}) gives
orthonormal rows. Hence the deletion of (h=0\pmod n) does not remove the
positive frequencies (h=j,2j,\ldots), which are zero only modulo (j).

Writing (h=qj+s) also shows that reciprocity makes only the inverse phase
periodic. The exact residue-compression operator obeys

$$
 \boxed{
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}
 \asymp\sqrt\Delta.}
\tag{160.10}
$$

This is sharp. On (h=mj<n), the inverse phase equals one and the correction
is (e(-m/n)=1+O(1/j)). Equations (160.9)--(160.10) are positive operator
capacities, not lower bounds for the (S(N_0,h;n))-weighted signed vector.

Let (a=\delta-\ell). The missing saving is

$$
 \mu(a)=
 \begin{cases}
 a-1/4,&1/4<a\le1/3,\\
 (1-2a)/4,&1/3\le a<1/2.
 \end{cases}
\tag{160.11}
$$

At (g=1), (j\asymp K=X^{1-\delta-a}), and

$$
 \frac{1-\delta-a}{2}-\mu(a)
 =\begin{cases}
 (3-2\delta-6a)/4,&a\le1/3,\\
 (1-2\delta)/4,&a\ge1/3,
 \end{cases}
 \quad>0.
\tag{160.12}
$$

Also (a/2-\mu(a)>0). Thus both the exact scalar projective price and the
long-block capacity exceed the entire missing factor at every fixed strict
point. There is no margin uniform up to the open face (\delta=1/2).

The additive common-test formula

$$
 \mathbf1_{(n,j)=1}e(h\overline n_j/j)
 =\frac1j\sum_{t\bmod j}S(h,-t;j)e(tn/j)
\tag{160.13}
$$

is a full-rank change of basis. A fixed proportion of its joint Fourier
mass occurs at (|t|\asymp j), which is a finite bandwidth diagnostic only.
The audited scalar Bettin--Chandee/Wright, Blomer--Milićević,
Deshouillers--Iwaniec, Assing--Blomer--Li, and level-four/eight interfaces
do not accept the complete moving coefficient matrix at an owner-saving
norm. Character expansion produces a large projective price and growing
levels, and the available short Linnik range covers only a vanishing
portion of the physical frequency row.

This proves a deliberately narrow obstruction: exact unweighted Hilbert
rank-one scalarization followed termwise by triangle, and the named audited
scalar realizations, are not low-cost continuations of additive
reciprocity. The frozen hypotheses provide no nonzero lower profile buffer
with complete unit-class coverage, so the unweighted nuclear lower price is
not transferred to the literal weighted matrix. Even such a future buffer
would not show that entrywise multiplication by the Kloosterman matrix
preserves the lower price. A bespoke signed vector theorem acting on the
complete weighted ((g,n,j,h)) array before positive norms remains open.

Consequently the flat smooth strict-UNBAL target, both other mandatory M2
parents, M9-M2, every M1 owner, endpoint uniformity, M9, the bridge, and
the quarter theorem remain open. No strict range is gained. The internal
global exponent remains (1/3), and the audited external Li--Yang exponent
remains ((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots).

Accepted evidence:

- proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/inverse_selector_reciprocity_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/blind_reciprocity_matrix_rederivation.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/reciprocity_projective_source_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/exact_kernel_power_review.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/source_level_seam_review.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/conductor_round160_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/state_patch_scope_round160.md.

## Round 161: hard-TOP radical long channels and exact collision control

For the literal nonsquare hard-TOP scalar, write uniquely

$$
 \mathcal T_L^{\rm ns}
 =\sum_{\substack{D>1\\D\ {\rm squarefree}}}\sum_{t\ge1}
 B_D(t)e(tJ\sqrt D),
\qquad
 B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2),
\tag{161.1}
$$

with fixed support constants

$$
 B_D(t)\ne0\Longrightarrow
 c_-L^2\le Dt^2\le c_+L^2.
\tag{161.2}
$$

The accepted Round-137 estimates are

$$
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),\qquad
 \sum_t|B_D(t)|\ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{161.3}
$$

The literal incidence map is bijective. If \(g=(h,m)\), then uniquely

$$
 h=gd_1u^2,\qquad m=gd_2v^2,\qquad
 D=d_1d_2,\qquad t=guv,
\tag{161.4}
$$

where \(d_1,d_2\) are squarefree,
\((d_1u,d_2v)=1\), \(g,d_1,u\) are odd, and

$$
 d_2v^2\le d_1u^2\le4d_2v^2.
\tag{161.5}
$$

The converse reconstructs the original pair and every literal profile,
endpoint, support condition, parity branch, and zero extension. In
particular, an even \(D\) survives through \(d_2\), and an even \(t\)
may survive through \(v\).

For \(Z\ge2\), (161.3) gives

$$
 \left|\sum_{\substack{D\le Z\\D>1\ {\rm squarefree}}}
 \sum_tB_D(t)e(tJ\sqrt D)\right|
 \ll_\varepsilon(Z+L\sqrt Z)L^\varepsilon.
\tag{161.6}
$$

Hence, for every fixed \(C>0\),

$$
 \boxed{
 \left|\sum_{\substack{D\le CL\\D>1\ {\rm squarefree}}}
 \sum_tB_D(t)e(tJ\sqrt D)\right|
 \ll_{C,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{161.7}
$$

By (161.2), this owns every fixed \(t\ge\tau\sqrt L\) sector. It is not
an owner-complete strict polynomial range: using
\(Z=L^{1+\delta}\) in (161.6) costs
\(L^{3/2+\delta/2+\varepsilon}\).

Square roots of distinct positive squarefree integers are linearly
independent over \(\mathbb Q\). Consequently the base collision graph

$$
 J(\sqrt{D_1}-\sqrt{D_2})\in\mathbb Z,\qquad D_1\ne D_2,
\tag{161.8}
$$

has at most one unequal unordered edge. Every exact cross-channel atom
relation

$$
 J(t_1\sqrt{D_1}-t_2\sqrt{D_2})=k,\qquad
 D_1\ne D_2,\quad k\ne0,
\tag{161.9}
$$

uses that same possible radical pair, and the coefficient triples of all
such relations are rational multiples of one primitive relation. At most
one channel has \(J\sqrt D\in\mathbb Q\). A same-channel equality with
\(t_1=t_2\) is a trivial loop; a nontrivial repetition requires that
unique rational channel. A rational channel cannot coexist with a
cross-channel relation. Every exact channel named here is target-safe by
(161.3). These algebraic statements provide no positive lower bound for a
nonzero modulo-one gap and no near-collision estimate.

The mandatory short-channel endpoint is \(t=1\):

$$
\begin{aligned}
B_D(1)=\mathbf 1_{D\asymp L^2}
\left(\frac{L^2}{D}\right)^{3/4}
\sum_{\substack{d_1d_2=D\\d_1\ {\rm odd}\\d_2\le d_1\le4d_2}}
&\chi_4(d_1)\eta_L(d_1)
\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right).
\end{aligned}
\tag{161.10}
$$

On \(Q\asymp L^2\) ambient squarefree rows, the one-column common-test
evaluation norm is exactly \(Q^{1/2}\asymp L\). The phase-aligned
diagnostic

$$
 A_D(t)=\mathbf1_{t=1}e(-J\sqrt D)
\tag{161.11}
$$

has nuclear norm \(Q^{1/2}\) and evaluation \(Q\asymp L^2\), while
obeying the accepted coarse energy and row-mass scales. Thus support,
positive energy, fixed-channel capacity, exact-collision sparsity, and a
coefficient-uniform common-test, large-sieve, Bessel, or
Hilbert-projective theorem do not imply the target. For the actual column,
positive Cauchy also gives only

$$
 \left|\sum_D B_D(1)e(J\sqrt D)\right|
 \ll L^2\sqrt{\log(2L)}.
\tag{161.12}
$$

Equations (161.11)--(161.12) are route capacities, not lower bounds for
the literal coefficient (161.10). Close-semiprime singleton fibres prove
no family density or lower mass.

The audited Montgomery--Vaughan, Bombieri--Iwaniec, Robert--Sargos, and
Miller interfaces do not supply the missing coefficient theorem.
Montgomery--Vaughan uses one common vector; Bombieri--Iwaniec is separable
and charges absolute collision forms; Robert--Sargos' four-root count is
not the fixed-centre circular pair problem; and Miller requires one fixed
automorphic coefficient sequence. Even after fictitious cost-one
separation, the direct Robert--Sargos theorem restores

$$
 J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2},
\tag{161.13}
$$

whose best combination with triviality is still \(L^2\) for
\(L\ll J^{1/2}\). This is a no-match for the four named routes, not a
global literature or method impossibility theorem.

The first open physical statement is therefore

$$
 \boxed{
 \left|\sum_{\substack{D\asymp L^2\\D>1\ {\rm squarefree}}}
 B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{161.14}
$$

It needs the actual \(\chi_4\)-weighted close-factor structure, or an
equivalent alignment-sensitive theorem that fails on (161.11). The
remaining \(L\ll D\ll L^2\), \(t\ll\sqrt L\) few-point channels and
near-collision collars remain open even after (161.14).

Consequently hard TOP, BAL, UNBAL, M9--M2, every M9--M1 owner, endpoint
uniformity, M9, the bridge, and the quarter theorem remain open. The
internal global exponent remains \(1/3\), and the separately audited
external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/literal_radical_frequency_attack.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/blind_radical_frequency_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/square_root_spacing_source_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/blind_post_repair_radical_collision_review.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/projective_power_scope_review.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/source_power_seam_review.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/downstream_scope_graph_review.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/conductor_round161_adjudication.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/state_patch_scope_round161.md.

## Round 162: literal (t=1) character-Poisson product-collar obstruction

The first open physical face from Round 161 is the literal close-factor
scalar

$$
\begin{aligned}
\mathcal S_{L,1}=\sum_{\substack{d_1d_2\asymp L^2\\
d_1,d_2\ \mathrm{squarefree},\ (d_1,d_2)=1\\
d_1\ \mathrm{odd},\ d_2\le d_1\le4d_2}}
&\chi_4(d_1)\left(\frac{L^2}{d_1d_2}\right)^{3/4}
\eta_L(d_1)\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
e(J\sqrt{d_1d_2}),
\end{aligned}
\tag{162.1}
$$

where (J=\sqrt X), (y=\lfloor J\rfloor), (q_X=X/y^2),
(H=\lfloor yX^{-1/4}\rfloor), and every literal hard support and
endpoint convention is retained.

The squarefree/coprime projector has the exact opening

$$
\mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}
=\sum_{a^2\mid d_1}\mu(a)
 \sum_{b^2\mid d_2}\mu(b)
 \sum_{c\mid(d_1,d_2)}\mu(c).
\tag{162.2}
$$

For

$$
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\quad d_2=Rn,
\tag{162.3}
$$

only (Q,m) are forced odd; (R,n) may be even.  Thus the even-(d_2)
branch survives and
(\chi_4(Qm)=\chi_4(Q)\chi_4(m)).

With (\widehat g(\xi)=\int g(x)e(-\xi x)\,dx), exact character Poisson
is

$$
\boxed{
 \sum_m\chi_4(m)g(m)
 =\frac i2\sum_{s\ \mathrm{odd}}\chi_4(s)\widehat g(s/4).}
\tag{162.4}
$$

For one opening, the positive saddle in the character leg is

$$
 m_s=\frac{4XQd_2}{s^2},\qquad
 d_1^*=\frac{4XQ^2d_2}{s^2},\qquad
 F_s(m_s)=\frac{XQd_2}{s},
\tag{162.5}
$$

with (JQ\le s\le2JQ), literal profile (W(XQ/(ys))), and normalized
stationary factor

$$
 \frac{2L^{3/2}J^{-1/2}}{Qd_2}.
\tag{162.6}
$$

The leading signed unit is (e(1/8)\chi_4(Q)\chi_4(s)).  The transform
is exactly involutive: if (h(s)=\widehat g(s/4)), then
(\widehat h(\xi)=4g(-4\xi)), and the two (i/2) factors, Fourier
scaling, and odd character reflection return the original sum.  A second
bare transform supplies no contraction.

The Hessian of (J\sqrt{xz}) has determinant zero and radial null vector.
For a compact smooth interior cell, simultaneous dualization gives

$$
 s\ell=XQR,\qquad Q\ell\le Rs\le4Q\ell.
\tag{162.7}
$$

The physical radial length broadens the resonant product to

$$
\boxed{|s\ell-XQR|\ll QRJ/L.}
\tag{162.8}
$$

At most

$$
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon
\tag{162.9}
$$

factor pairs occur.  One smooth-interior coefficient has scale

$$
 \frac{L^{3/2}}{QR\sqrt J}.
\tag{162.10}
$$

Therefore the (QR)-decay is exactly repaid by the collar width, and
termwise positive control has capacity

$$
 \sqrt{JL}\,(XQR)^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)(XQR)^\varepsilon.
\tag{162.11}
$$

On the favorable single-opening model, the coefficient-insensitive
comparison is

$$
 \min\{L^2,\sqrt{JL}\}
 =L^{3/2}\min\{L^{1/2},H/L\}(1+o(1)).
\tag{162.12}
$$

This is a route capacity only.  It is not an upper bound for the complete
Möbius sum, physical mass, or a lower bound.

Grouping by (N=s\ell) yields the moving near-square window

$$
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s).
\tag{162.13}
$$

Completing it to
(\sum_{s\mid N}\chi_4(s)=r_2(N)/4) adds an uncontrolled complementary
divisor window.  Standard differencing also gives no automatic character
gain because

$$
 \chi_4(d+2h)\chi_4(d)=(-1)^h
\tag{162.14}
$$

for odd (d), which becomes constant after a positive norm.

The named source placements remain insufficient.  Bombieri--Iwaniec
requires separated coefficients.  Even after granting fictitious
cost-one separation, Kowalski--Robert--Wu and Robert--Sargos restore,
respectively,

$$
 J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+J^{-1/2}L^{3/2}
\tag{162.15}
$$

and

$$
 J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2}.
\tag{162.16}
$$

The fixed-modulus/fixed-integral DFI and DRZ cards have no uniform literal
placement for the arbitrary-real ordinary reciprocal (e(XQd_2/s)).
Bettin--Chandee has a formal integral-subcase one-point-inverse placement,
but its printed parameter factor is already ((JL)^{1/2}) before the
remaining powers and physical normalization.  These conclusions park only
the named placements, not future or bespoke coefficient-sensitive
theorems.

The accepted result deliberately leaves literal hard edges open.  Nonzero
zero-extension endpoints can have only reciprocal-frequency decay, and a
saddle meeting a hard edge is a separate transition.  Individual opened
terms also need not inherit cancellations present only after the physical
projector is recombined.

The first open affirmative statement is a target-strength bound for the
full signed Möbius-coupled family whose smooth principal interface is

$$
\frac{L^{3/2}}{\sqrt J}
\sum_{a,b,c}\frac{\mu(a)\mu(b)\mu(c)\chi_4(Q)}{QR}
\sum_{N\approx XQR}
\sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
\sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
\chi_4(s)\mathcal K_{Q,R}(N;s),
\tag{162.17}
$$

with arbitrary-real-centre uniformity, the even-(d_2) branch, all
profiles, hard boundaries, floors, stars, endpoint transitions,
nonstationary pieces, and collar tails retained before every positive
norm.  It must recover the factor
(\min\{L^{1/2},H/L\}).

Round 162 therefore proves a scoped transform-and-source obstruction, not
the (t=1) target.  The other
(L\ll D\ll L^2,t\ll\sqrt L) few-point channels remain open.  Hard TOP,
BAL, UNBAL, M9--M2, every M9--M1 owner, endpoint uniformity, M9, the
bridge, and the quarter theorem remain open.  The internal global exponent
remains (1/3), and the audited external Li--Yang exponent remains
((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots).

Accepted evidence:

- proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reports/literal_t1_character_poisson_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reports/blind_t1_close_factor_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reports/t1_bilinear_source_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/blind_post_unmask_character_collar_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/power_involution_and_physical_scope_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/source_and_downstream_graph_scope_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/conductor_round162_adjudication.md;
- rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/state_patch_scope_round162.md.

## Round 163 accepted close-opposite-prime exchange sector

Retain the literal squarefree \(t=1\) product scalar and extend its
amplitude by zero outside every physical shell, cone, dyadic, profile,
endpoint, floor, and star condition.  For fixed \(\kappa>0\), and for
each supported squarefree \(N\), select canonically at most one pair of
distinct odd prime divisors

\[
 p=p_{N,L,\kappa},\qquad q=q_{N,L,\kappa},
 \qquad
 \chi_4(pq)=-1,\qquad
 |\log(q/p)|\leq\kappa L^{-1/2},
\tag{163.1}
\]

using only \((N,L,\kappa)\), not a divisor allocation.  Let
\(\mathscr D_N^\oplus\) be the divisors \(d\mid N\) for which \(d\) is
odd and exactly one of \(p,q\) divides \(d\).  Define

\[
 T_Nd=
 \begin{cases}
 dq/p,&p\mid d,\ q\nmid d,\\
 dp/q,&q\mid d,\ p\nmid d.
 \end{cases}
\tag{163.2}
\]

Squarefreeness makes \(T_N\) an integral fixed-point-free involution of
\(\mathscr D_N^\oplus\).  It preserves \(N=d(N/d)\), coprimality,
oddness, the even-\(N\) branch, the product phase \(e(J\sqrt N)\), and
all product-only normalizations, while

\[
 \chi_4(T_Nd)=\chi_4(d)\chi_4(pq)=-\chi_4(d).
\tag{163.3}
\]

If \(A_N(d)\) denotes the complete zero-extended literal amplitude, then
the exact pairing identity is

\[
 \sum_{d\in\mathscr D_N^\oplus}\chi_4(d)A_N(d)
 =
 \frac12\sum_{d\in\mathscr D_N^\oplus}
 \chi_4(d)\{A_N(d)-A_N(T_Nd)\}.
\tag{163.4}
\]

On every common smooth cell, the ordinary \(O(L^{-1})\) derivative of
the accepted dyadic profile, bounded \(C^1\) regularity of \(\Phi\) and
\(W\), the condition \(L\ll H\), and
\(|T_Nd-d|\ll_\kappa L^{1/2}\) give

\[
 |A_N(d)-A_N(T_Nd)|\ll_\kappa L^{-1/2}.
\tag{163.5}
\]

There are \(O(L^2)\) ambient divisor-complement incidences.  Every place
where one leg crosses a cone, dyadic, profile, endpoint, star, ceiling,
or zero-extension boundary lies in one of finitely many lattice collars
of width \(O_\kappa(L^{1/2}+1)\), hence contains altogether
\(O_\kappa(L^{3/2}+L)\) incidences.  The literal amplitude is bounded on
those collars.  Consequently the complete selected incidence sector
satisfies, uniformly in the real centre,

\[
 \boxed{|\mathcal S_{L,1}^{\mathrm{cp}}|
 \ll_\kappa L^{3/2}.}
\tag{163.6}
\]

This is a genuine target-safe physical sector but has no asserted
density.  It may be empty in a block.  Products with no selected pair
and, when a pair exists, incidences containing neither or both selected
primes remain in

\[
 \mathcal S_{L,1}^{\mathrm{rem}}
 =\mathcal S_{L,1}-\mathcal S_{L,1}^{\mathrm{cp}},
\tag{163.7}
\]

for which no target estimate is proved.

The same audit closes several tempting shortcuts.  A single
\(p\equiv3\pmod4\) toggle has disjoint physical supports because the
upper divisor interval has multiplicative width two and \(p\geq3\).
Normalized averaging over all such toggles, or over sign-reversing
full-divisor-lattice involutions, returns the original coefficient
exactly.  A general exchange graph is complete bipartite by character
sign, but a perfect matching requires equality of the two sign classes;
cycles merely rewrite literal profile gradients and unmatched terms.
Odd complementation enters the excluded lower window.  For \(N=2M\),
the physical complement is even and the odd-part complement lies in
\([\sqrt N/4,\sqrt N/2]\).  Full-divisor character vanishing therefore
replaces the physical truncation by an uncontrolled profiled complement
rather than estimating it.

Round 163 proves no eligible-pair density, full \(t=1\) bound, remaining
few-point estimate, hard-TOP parent, smooth M2 packet, M9--M2, M9--M1,
endpoint uniformity, M9, bridge, quarter theorem, or exponent
improvement.  The internally proved exponent remains \(1/3\), and the
audited external benchmark remains
\((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\).

Accepted evidence:

- proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/literal_near_square_divisor_involution_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/prime_toggle_complement_leakage_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/blind_post_unmask_close_pair_sector_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/profile_boundary_power_seam_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/downstream_graph_scope_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/conductor_round163_adjudication.md;
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/state_patch_scope_round163.md.
