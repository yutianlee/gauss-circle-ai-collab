# H4 weight and normalization review

- Campaign: `m9-unit-frequency-w1-validation`
- Research round: `2` (`seam_validation`)
- Task: `h4_weight_normalization_review`
- Role: `source_auditor`
- Graph SHA-256 supplied in the brief: `3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f`
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

The Vaaler normalization used by H4 is correct, with one important convention qualification. Vaaler's paper uses the midpoint sawtooth, which is zero at integers. The project's floor-compatible sawtooth is instead −1/2 at integers. Theorem 18 does not state the floor-compatible version verbatim, but its residual inequality extends to that version: the Fourier polynomial vanishes at an integer and the Fejer bound is exactly 1/2 there.

For every integer truncation height $H\geq1$, the exact M2 coefficient satisfies

$$
\beta_{1,H}=-\frac{\Phi(1/(H+1))}{\pi},
\qquad
|\beta_{1,H}|\geq \frac1{2\pi}.
$$

Thus the unit-frequency coefficient cannot be removed by a coefficient adversary. The primary-source part of the proposed W-1 mechanism is verified.

The sharp-block lower bound does **not** transfer from the phrase "bounded smooth dyadic partition" alone. A weakest convenient discrete lower-envelope hypothesis is

$$
\sum_{d}|w_D(d)|\geq \lambda D
$$

with fixed $\lambda>0$, support in a fixed dyadic shell $[aD,bD]$, and (for compatibility with the accepted exact-$N=0$ upper bound) a fixed $\ell^\infty$ bound. No pointwise-positive subinterval and no differentiability are needed for the absolute-mass window argument. A fixed nonzero smooth profile $w_D(d)=W(d/D)$ implies this $\ell^1$ condition, but the current proof draft does not specify the profiles well enough to verify it for every active or endpoint block.

## 2. Primary source, bibliography, and rendered-page audit

Jeffrey D. Vaaler, “Some extremal functions in Fourier analysis,” *Bulletin of the American Mathematical Society (New Series)* **12** (1985), no. 2, 183–216. DOI: [10.1090/S0273-0979-1985-15349-2](https://doi.org/10.1090/S0273-0979-1985-15349-2). MR 0776471 (86g:42005), Zbl 0575.42003. See the [AMS article record](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/) and the [official AMS PDF](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/S0273-0979-1985-15349-2.pdf). An accessible mirror of the same scan is [SciSpace PDF](https://scispace.com/pdf/some-extremal-functions-in-fourier-analysis-1fijhvmlkp.pdf).

I downloaded and rendered the official 34-page AMS PDF. Its SHA-256 was `E606CCEF342E72D7E48B59A7DA7F8577F72FD351CE32989B23DD85E9E8CD4C1A` at audit time. The relevant rendered locations are Theorem 6 on article pp. 192–193, equations (6.5)–(6.6) on p. 206, equations (7.1)–(7.3) on p. 207, and Theorem 18 on pp. 210–211.

### Exact formulas needed here

Vaaler uses $e(u)=e^{2\pi i u}$. Theorem 6, equation (2.28), gives

$$
\widehat J(t)=
\begin{cases}
1,&t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|,&0<|t|<1,\\
0,&1\leq |t|.
\end{cases}
\tag{2.28}
$$

The theorem also states that $\widehat J$ is even, nonnegative, continuously differentiable, and strictly decreasing on $[0,1]$.

Vaaler's Fejer kernel and sawtooth are, on p. 206,

$$
k_N(x)=\sum_{n=-N}^{N}\left(1-\frac{|n|}{N+1}\right)e(nx)
=\frac1{N+1}\left(\frac{\sin\pi(N+1)x}{\sin\pi x}\right)^2,
\tag{6.5}
$$

and

$$
\psi(x)=
\begin{cases}
x-[x]-\frac12,&x\notin\mathbb Z,\\
0,&x\in\mathbb Z.
\end{cases}
\tag{6.6}
$$

Thus Vaaler's convention is the midpoint convention, not the project's floor-compatible convention.

The periodizations in (7.1)–(7.3) are

$$
i_N(x)=\sum_{m\in\mathbb Z}I_{2N+2}(x+m)
=\sum_{n=-N}^{N}\widehat I_{2N+2}(n)e(nx),
\tag{7.1}
$$

$$
j_N(x)=\sum_{m\in\mathbb Z}J_{N+1}(x+m)
=\sum_{n=-N}^{N}\widehat J_{N+1}(n)e(nx),
\tag{7.2}
$$

$$
k_N(x)=\sum_{m\in\mathbb Z}K_{N+1}(x+m)
=\sum_{n=-N}^{N}\widehat K_{N+1}(n)e(nx).
\tag{7.3}
$$

The scaling convention stated earlier in the paper is $F_\delta(x)=\delta F(\delta x)$, so $\widehat F_\delta(t)=\widehat F(\delta^{-1}t)$. Consequently, for $1\leq |n|\leq N$,

$$
\widehat J_{N+1}(n)=\widehat J\!\left(\frac{n}{N+1}\right)
=\Phi\!\left(\frac{|n|}{N+1}\right),
$$

where the project name

$$
\Phi(u):=\pi u(1-u)\cot(\pi u)+u,\qquad 0<u<1,
$$

is not a separate symbol introduced by Vaaler; it is the positive-half-axis restriction of his $\widehat J$.

Theorem 18 defines

$$
p_N(x):=(\psi*j_N)(x)
=\sum_{\substack{-N\leq n\leq N\\n\neq0}}
(-2\pi i n)^{-1}\widehat J_{N+1}(n)e(nx).
$$

Its equations (7.13)–(7.17) are

$$
\operatorname{sgn}(p_N(x))=\operatorname{sgn}(\psi(x)),
\tag{7.13}
$$

$$
|p_N(x)-\psi(x)|\leq (2N+2)^{-1}k_N(x),
\tag{7.14}
$$

$$
|p_N(x)|\leq |\psi(x)|,
\tag{7.15}
$$

and, for every trigonometric polynomial $q_N$ of degree at most $N$ with $q_N\geq\psi$,

$$
\int_{-1/2}^{1/2}(q_N(x)-\psi(x))\,dx\geq(2N+2)^{-1}.
\tag{7.16}
$$

With $E=H-\operatorname{sgn}$ as in Corollary 7, the proof records

$$
(2N+2)^{-1}\sum_{m\in\mathbb Z}E_{N+1}(x+m)
=p_N(x)-\psi(x).
\tag{7.17}
$$

Rendered-source caution: immediately after (7.16), the scan prints the unique extremizing majorant with coefficient $(2N+1)^{-1}k_N$. That coefficient is inconsistent with (7.16) and $\int k_N=1$; the consistent coefficient is $(2N+2)^{-1}$. This apparent typographical error is irrelevant to (7.14), the only extremal inequality used by H4, and the suspect uniqueness line should not be imported.

## 3. Notation map and floor-compatible corollary

| Vaaler | Project | Relation |
|---|---|---|
| $N$ | $H$ | nonnegative integer Fourier degree |
| $\psi$ from (6.6) | midpoint sawtooth | equals $\{x\}-1/2$ off $\mathbb Z$, but is $0$ on $\mathbb Z$ |
| — | $\psi_F(x)=x-\lfloor x\rfloor-1/2$ | equals Vaaler's $\psi$ off $\mathbb Z$, and equals $-1/2$ on $\mathbb Z$ |
| $p_N=\psi*j_N$ | $\sum_{1\leq|h|\leq H}\alpha_{h,H}e(hx)$ | same trigonometric polynomial |
| $\widehat J_{N+1}(h)$ | $\Phi(|h|/(H+1))$ | by (2.28) and scaling |
| $k_N$ | $K_H$ | same normalized Fejer kernel |

Therefore

$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad 1\leq|h|\leq H.
$$

For $x\notin\mathbb Z$, equation (7.14) is already the desired bound. For $x\in\mathbb Z$, pairing $h$ and $-h$ gives $p_H(x)=0$, while

$$
\psi_F(x)=-\frac12,
\qquad
\frac{K_H(x)}{2H+2}
=\frac{H+1}{2H+2}=\frac12.
$$

Hence the exact project corollary is

$$
\psi_F(x)=\sum_{1\leq|h|\leq H}\alpha_{h,H}e(hx)+R_H^F(x),
\qquad
|R_H^F(x)|\leq\frac{K_H(x)}{2H+2}
$$

for every real $x$ and integer $H\geq0$. At an integer, equality holds in the residual bound. Equation (7.13), however, does **not** transfer to $\psi_F$ at integers, since $\operatorname{sgn}(p_H)=0$ there but $\operatorname{sgn}(\psi_F)=-1$.

## 4. Odd-frequency beta algebra and the uniform $\beta_1$ envelope

Put

$$
C_h=e(h/4)-e(3h/4).
$$

Direct evaluation modulo $4$ gives

$$
C_h=
\begin{cases}
2i\chi_4(h),&h\ \text{odd},\\
0,&h\ \text{even}.
\end{cases}
$$

Thus

$$
\begin{aligned}
\beta_{h,H}:=\alpha_{h,H}C_h
&=-\frac{\Phi(|h|/(H+1))\chi_4(h)}{\pi h}\mathbf1_{2\nmid h}\\
&=-\frac{\Phi(|h|/(H+1))\chi_4(|h|)}{\pi|h|}\mathbf1_{2\nmid h}.
\end{aligned}
$$

This is real and even. In particular, $\beta_{1,H}<0$.

Theorem 6 says that $\Phi$ is strictly decreasing on $[0,1]$. Also

$$
\Phi(1/2)=\frac12.
$$

For $H\geq1$, $1/(H+1)\in(0,1/2]$, and therefore

$$
\Phi\!\left(\frac1{H+1}\right)\geq\frac12,
\qquad
\boxed{|\beta_{1,H}|\geq\frac1{2\pi}}.
$$

This also proves positivity of $\Phi$ on $(0,1/2]$. Independently of monotonicity, positivity follows directly there because $\cot(\pi u)\geq0$ and the $+u$ term is positive. The uniform numerical lower envelope uses the source's monotonicity statement. The support condition $H\geq1$ must remain explicit; if an endpoint rounding rule can produce $H_D=0$, the unit-frequency family is absent.

## 5. Dyadic-weight transfer lemma

### Exact statement

Fix $0<a<b<\infty$, $\lambda>0$, and $W<\infty$. Let $D\geq1$, let $w_D$ be supported on

$$
\mathcal D_D=[aD,bD]\cap\mathbb Z_{>0},
$$

and assume

$$
\|w_D\|_\infty\leq W,
\qquad
L_D:=\sum_{d\in\mathcal D_D}|w_D(d)|\geq\lambda D.
\tag{W-L1}
$$

Let $H\geq1$ and $\beta_{1,H}$ be the Vaaler-M2 coefficient above. For $d_i\in\mathcal D_D$, set

$$
N=d_2d_3d_4-d_1d_3d_4+d_1d_2d_4-d_1d_2d_3,
$$

up to the harmless relabeling corresponding to

$$
\frac{N}{d_1d_2d_3d_4}
=\frac1{d_1}-\frac1{d_2}+\frac1{d_3}-\frac1{d_4}.
$$

Then, for every $M>0$, the $h_1=h_2=h_3=h_4=1$ same-window family has absolute weight at least

$$
c_{a,b}\,|\beta_{1,H}|^4\lambda^4\min(D^4,MD).
\tag{W-1w}
$$

Consequently, if the full exact-resonance absolute mass satisfies

$$
\Sigma_{\rm abs}(N=0)\leq C_{\epsilon,W}D^2X^\epsilon,
$$

then

$$
\boxed{
\Sigma_{\rm abs}(0<|N|\leq M)
\geq c_{a,b}\left(\frac{\lambda}{2\pi}\right)^4
\min(D^4,MD)-C_{\epsilon,W}D^2X^\epsilon.
}
\tag{W-transfer}
$$

This concerns the absolute coefficient-weighted mass. It gives no lower bound for the full signed fourth-moment sum.

### Proof

For an ordered pair $(r,s)\in\mathcal D_D^2$, put

$$
u(r,s)=\frac1r+\frac1s,
\qquad
A(r,s)=|w_D(r)w_D(s)|.
$$

All $u(r,s)$ lie in an interval of length $O_{a,b}(D^{-1})$. Partition that interval into windows of width

$$
\eta=\frac{M}{2b^4D^4}.
$$

The number of nonempty or covering windows is

$$
K\leq 1+C_{a,b}\frac{D^3}{M}.
$$

Let $V_j$ be the total $A(r,s)$ in window $j$. Then

$$
\sum_jV_j=L_D^2.
$$

Weighted Cauchy gives

$$
\sum_jV_j^2\geq\frac{L_D^4}{K}
\gg_{a,b}\lambda^4\min(D^4,MD).
$$

Two ordered pairs in one window give a denominator quadruple with

$$
\left|\frac1{d_1}+\frac1{d_3}-\frac1{d_2}-\frac1{d_4}\right|<\eta.
$$

Since $d_1d_2d_3d_4\leq b^4D^4$, its cleared integer satisfies $|N|<M/2$, hence $|N|\leq M$. Multiplying by $|\beta_{1,H}|^4$ proves (W-1w). Removing $N=0$ costs at most the full exact-resonance mass, and $|\beta_{1,H}|\geq1/(2\pi)$ proves (W-transfer).

### Why (W-L1) is the weakest useful smooth lower envelope

The weighted proof uses only $L_D=\sum|w_D|$; it does not use a pointwise lower bound or smoothness. A positive-density subset with $|w_D|\geq\kappa$ is a stronger sufficient condition, because it implies (W-L1) with $\lambda=\rho\kappa$.

For a fixed $W_0\in C_c^1((a,b))$ that is not identically zero and $w_D(d)=W_0(d/D)$,

$$
\sum_d|w_D(d)|
=D\int_a^b|W_0(t)|\,dt+O_{W_0}(1),
$$

so (W-L1) holds for all sufficiently large $D$. For a $D$-dependent family of profiles, it is enough to require a uniform positive $L^1$ norm together with enough uniform regularity to pass from the integral to the sampled sum.

Conversely, "bounded smooth" alone permits $w_D\equiv0$ or $w_D=D^{-A}W_0(d/D)$, for which no $D$-scale lower bound is possible. Moreover, the total absolute fourfold weight is $L_D^4$, so $L_D\gg D$ is necessary for a uniform $D^4$ lower bound when $M\asymp D^3$. Thus (W-L1) is the natural minimal scalar nondegeneracy for the full sharp-block scale.

## 6. Required controls

### `support-and-degeneracy`

- Pass under explicit hypotheses: $H_D\geq1$, support in $[aD,bD]$, and (W-L1).
- The lowest active endpoint needs a stated rounding convention for $H_D\asymp DX^{-1/4}$; asymptotic comparability alone does not literally imply $H_D\geq1$ after integer rounding.
- A top block truncated by $d\leq\lfloor X^{1/2}\rfloor$ may fail (W-L1). The actual partition must be checked block by block or the claim must be restricted to nondegenerate blocks.

### `coefficient-adversary`

- Pass for the Vaaler coefficients: $h=1$ is odd, survives $C_h$, and has $|\beta_{1,H}|\geq1/(2\pi)$.
- Fail for arbitrary coefficients: an adversary may set the unit-frequency coefficient to zero. The obstruction is specific to the sourced Vaaler normalization.
- Even frequencies vanish because $C_h=0$ for even $h$; this does not affect the $h=1$ family.

### `raw-vs-weighted`

- Pass under (W-L1): weighted Cauchy transfers the raw window count directly and loses only the factor $\lambda^4$.
- Fail from boundedness or smoothness alone: scale-degenerate weights destroy the claimed lower bound.
- The character-removed unsigned mass has the same obstruction on the $h=1$ family. The true signed mass remains outside scope because other tuples may cancel this subtotal.

No numerical experiment was used to certify any claim.

## 7. First doubtful step, dependencies, and recommended state effect

### First doubtful or unproved step

The Vaaler coefficient step is no longer doubtful. The first unresolved seam is the actual dyadic-weight normalization: `state/best_proof_draft.md` says only "bounded smooth dyadic partition" and gives no fixed profile, sampled $\ell^1$ lower bound, or endpoint construction. Therefore a lower bound for every actual M2 block is not yet justified. The exact-$N=0$ subtraction is also inherited as an accepted H4-dependent assumption and was not reproved in this source audit.

### Dependencies and exact artifacts used

- Official Vaaler PDF and publisher record linked above, rendered at article pp. 192–193, 206–207, and 210–211.
- `sources/vaaler_1985.md`.
- `state/proof_obligations.yml`.
- `state/best_proof_draft.md`.
- `Gauss circle problem.tex`.
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/conductor_independent_analysis.md`.
- Task brief `rounds/codex-managed/m9-unit-frequency-w1-validation/briefs/h4_weight_normalization_review.md`.

### Recommended state effect

1. **Promote the source audit evidence after conductor validation:** update `sources/vaaler_1985.md` with the bibliography, official links, theorem/equation locations, midpoint convention, floor-compatible endpoint corollary, coefficient sign, Fejer normalization, and $|\beta_{1,H}|\geq1/(2\pi)$. The H4 source blocker can then be reconsidered.
2. **Revise, not unconditionally promote, the W-1 statement:** add $H_D\geq1$, support comparability, and the sampled lower envelope $\sum|w_D|\geq\lambda D$. Alternatively, state the obstruction for one explicitly chosen standard nondegenerate smooth profile.
3. **Retain the scope separation:** the result applies to raw counts after weighted transfer, absolute beta-weighted mass, and the character-removed unsigned mass; it does not apply to the full signed mass.
4. **Do not import the apparent $(2N+1)^{-1}$ uniqueness-line typo** following (7.16); it is unnecessary for H4.

