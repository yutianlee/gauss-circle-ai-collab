# Best Conditional Proof Draft

## Scope and status

This document consolidates the accepted proof-obligation graph through
completed Codex-managed Round 95, together with the earlier accepted
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
 K={XL\over D^2},\qquad M=LK,qquad F=\sqrt{XM}={XL\over D}.
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
 a(n)=\sum_{d\mid n}\chi_4(d)=\frac{r_2(m)}4,qquad
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
 E=M(s-r)-jrs,qquad u=M-jr,qquad v=M+js.
\]

There is no half-integer tie, and for \(M=2^tM_0\), \(M_0\) odd,

\[
 M(1/r-1/s)=j+\frac{E}{rs},\qquad
 uv-M^2=jE,qquad
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
 j\ne0,qquad E\ne0,qquad |E|\leq X^{1+\eta/10}/L.
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
