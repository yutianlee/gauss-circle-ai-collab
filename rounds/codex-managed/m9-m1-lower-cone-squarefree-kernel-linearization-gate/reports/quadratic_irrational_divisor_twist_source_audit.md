# Quadratic-irrational divisor-twist source audit

- Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`
- Round: 145
- Role: source auditor
- Graph: `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`
- Status: candidate evidence only; 100% analytic and 0% numerical

Let $e(z)=e^{2\pi iz}$, $R=X^{1/4}$, $N=\lfloor X\rfloor$, and

\[
C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),\quad
k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\quad j_m=k_m^2-Nm.
\]

## 1. Result: strict squarefree-kernel reduction with a source no-go component

The outcome is a component of the campaign exit label

\[
\boxed{\mathsf{strict\_squarefree\_kernel\_reduction}.}
\]

Write $m=st^2$ uniquely with $s$ squarefree. The exact coefficient is

\[
\boxed{
C(st^2)=
\sum_{uv=s}^{\rm ord}
\ \sum_{\substack{g a b=t\\(ua,vb)=1\\gvb\ {\rm odd}\\vb^2>4ua^2}}
\chi_4(gv).}
\tag{1.1}
\]

Equivalently, if $g=c\ell^2$ with $c$ squarefree,

\[
C(st^2)=
\sum_{uv=s}^{\rm ord}
\ \sum_{\substack{c\ell^2 a b=t\\c\ {\rm squarefree}\\(ua,vb)=1\\c\ell vb\ {\rm odd}\\vb^2>4ua^2}}
\chi_4(cv).
\tag{1.2}
\]

No coprimality involving $g,c$, or $\ell$ may be added; $c$ can overlap $u$ or $v$.

For any inherited half-open block $\mathcal I_M\subset[M,2M)$, including the terminal truncation, the literal-profile contribution with $t\geq T$ satisfies

\[
\left|
\sum_{\substack{m\in\mathcal I_M,\ |j_m|>M^{3/4}\\m=st^2,\ s\ {\rm squarefree},\ t\geq T}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\right|
\ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}T.
\tag{1.3}
\]

Thus $T=\lceil M^{1/4}\rceil$ is target-safe per block and after logarithmic dyadic assembly. For $t<M^{1/4}$ one only obtains

\[
s=m/t^2\geq M/t^2>M^{1/2}.
\tag{1.4}
\]

No audited primary theorem closes this small-$t$ scalar uniformly. The first exact mismatch is the coefficient (1.1), which is $t$-dependent, parity-sensitive, and strict-cone incomplete. At $t=1$,

\[
C(s)=\sum_{\substack{uv=s\\v\ {\rm odd}\\v>4u}}\chi_4(v),
\tag{1.5}
\]

with $u,v$ automatically squarefree and coprime. On $M\asymp R^2$, even an optimistically separated Sargos--Wu application leaves $R^{2/5+\varepsilon}$. This is a limitation of that upper bound, not a lower bound for the target.

## 2. Exact hypotheses and primary-source theorem cards

The open owner is

\[
\mathfrak T_N=
\sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm}).
\tag{2.1}
\]

A usable theorem must accept (1.1), every $t<M^{1/4}$ including $t=1$, squarefree $s$, half-open/terminal blocks, literal profile and mask, the individual positive direction, every real centre, and constants uniform in all displayed parameters.

### Uchiyama: complete divisor square-root twists

S. Uchiyama, *On some exponential sums involving the divisor function over arithmetical progressions*, Math. J. Okayama Univ. 16 (1974), 137--146 ([primary PDF](https://www.math.okayama-u.ac.jp/mjou/mjou1-46/mjou_pdf/mjou_16/mjou_16_137.pdf), [DOI](https://doi.org/10.18926/mjou/33763)).

For fixed $k\geq1$, $0\leq l<k$,

\[
U(x,Y;k,l)=\sum_{\substack{n\leq Y\\n\equiv l\pmod k}}
n^{-1/2}d(n)e(x\sqrt n).
\]

Theorem 2 gives $U=O_x(\log Y)$ when $x\neq2\sqrt q/k$ for every positive integer $q$. When $x=2\sqrt q/k$ and $x\geq4k^3$,

\[
U(x,Y;k,l)=
\frac{2(1-i)\sigma(q;k,l)}{k^{3/2}q^{1/4}}Y^{1/4}+O(\log Y).
\tag{2.2}
\]

This is a sharp cutoff and one positive complex direction, but the coefficient is complete $d(n)$ on a fixed progression and the nonresonant constant may depend on fixed $x$. For $k=1$, every even $t$ makes $x=t\sqrt N$ spectral. This source resonance differs from the termwise exact-radical fibre $j_m=0$.

### Kaczorowski--Perelli: standard twists

J. Kaczorowski and A. Perelli, *Twists and resonance of \(L\)-functions, I* ([primary article/PDF](https://ems.press/journals/jems/articles/13843), [arXiv](https://arxiv.org/abs/1304.4734)), define for one fixed extended-Selberg-class $F$ of degree $d$

\[
F(s,\alpha)=\sum_{n\geq1}a(n)e(-\alpha n^{1/d})n^{-s},\qquad
n_\alpha=q_Fd^{-d}\alpha^d.
\]

Theorems 1--2 treat fixed $\alpha$: nonspectral twists are entire, while spectral twists have possible simple poles

\[
s_k=\frac{d+1}{2d}-\frac{k}{d}-i\theta_F.
\tag{2.3}
\]

For $F=\zeta^2$, $n_\alpha=\alpha^2/4$ and the spectrum is $\alpha=2\sqrt q$. Real coefficients permit conjugation to the positive direction. The paper notes weak $\alpha$-uniformity for moving-parameter applications. Formula (1.1) is not a fixed $L$-function coefficient, and $\alpha=t\sqrt N$ grows.

### Sun: genuinely frequency-uniform, but wrong coefficient and power

Q. Sun, *Nonlinear exponential twists of the Liouville function*, Cent. Eur. J. Math. 9 (2011), 328--337 ([primary PDF](https://d-nb.info/1372511547/34), [DOI](https://doi.org/10.2478/s11533-010-0092-6)). Theorem 1.1, uniformly for every real $\alpha\neq0$, states

\[
\begin{aligned}
\sum_{n\sim Y}\lambda(n)e(\alpha\sqrt n)\ll_\varepsilon{}&
Y^{5/6}\log^{7/2}Y
+Y^{3/4}\log^4Y\left(1+\frac1{|\alpha|}\right)^{1/2}\\
&+Y^{3/4}\log^{7/2}Y(1+|\alpha|)^{1/2}
+Y^{1/2+\varepsilon}\left(|\alpha|+\frac1{|\alpha|}\right).
\end{aligned}
\tag{2.4}
\]

It has the correct direction, sharp dyadic support, and no exceptional set, but exactly the Liouville coefficient. At $Y\asymp R^2$, $\alpha\asymp R^2$, (2.4) is worse than triviality; even normalized triviality leaves $R^{1/2}$.

### Schlage-Puchta: squarefree support, wrong phase

J.-C. Schlage-Puchta, *The exponential sum over squarefree integers*, Acta Arith. 115 (2004), 265--268 ([primary manuscript](https://arxiv.org/html/1105.1616v1), [DOI](https://doi.org/10.4064/aa115-3-7)), studies

\[
S(\alpha)=\sum_{n\leq Y}\mu^2(n)e(\alpha n).
\]

On the paper's minor arcs, Theorem 1 gives

\[
S(\alpha)\ll_\varepsilon Y^{1+\varepsilon}Q^{-1}
\quad(\alpha\in\mathfrak m(Q),\ Q\leq Y^{1/2}),
\tag{2.5}
\]

and Theorem 3 gives, under $|\alpha q-a|\leq q^{-1}$,

\[
|S(\alpha)|\ll_\varepsilon Y^{1+\varepsilon}q^{-1}+Y^\varepsilon q.
\tag{2.6}
\]

The coefficient support matches, but the phase is linear in the squarefree variable. Reorienting in $t$ makes the target phase linear, but the coefficient is then $C(st^2)$, the mask is $t$-dependent, and $t$ is not $\mu^2$-supported.

### Duke: fixed quadratic irrational only

W. Duke, *A divisor function with Diophantine properties* ([primary author PDF](https://www.math.ucla.edu/~wdduke/preprints/restricted.pdf)), treats $S(\alpha,y)=\sum_{n\leq y}\psi(n\alpha)$ and its own restricted divisor function. It recalls $S(\alpha,y)=O(\log y)$ for fixed $\alpha$ with bounded partial quotients, including fixed quadratic irrationals. Its Theorem 2 fixes the special fundamental unit $\alpha=(a+\sqrt{a^2-4})/2$ and a Cesàro order $r>3$. It supplies neither the coefficient (1.1) nor uniformity as the quadratic discriminant varies with $N,s$.

### Robert--Sargos and Sargos--Wu: correct monomial, insufficient class/power

Theorem 1 of O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials* ([primary PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), [DOI](https://doi.org/10.1515/CRELLE.2006.012)), assumes $X_1>1$, $|a(h,n)|,|b(m)|\leq1$, $\alpha(\alpha-1)\beta\gamma\neq0$, and proves

\[
S_0\ll_\varepsilon(HN_1M_1)^{1+\varepsilon}
\left\{
\left(\frac{X_1}{HN_1M_1^2}\right)^{1/4}
+(HN_1)^{-1/4}+M_1^{-1/2}+X_1^{-1/2}
\right\}.
\tag{2.7}
\]

It permits one joint coefficient and one separated coefficient. The favorable separated top specialization leaves $R^{1/2+\varepsilon}$; carrying the exact joint mask leaves $R^{3/4+\varepsilon}$.

Theorem 9 of P. Sargos and J. Wu, *Multiple exponential sums with monomials and their applications in number theory*, Acta Math. Hungar. 87 (2000), 333--354 ([primary DOI](https://doi.org/10.1023/A:1006777803163)), assumes separated bounded coefficients, $Z>0$, and

\[
\alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\neq0.
\]

For the bilinear monomial sum, its bound, up to $(ZM_1N_1)^\varepsilon$, is the sum of

\[
\begin{gathered}
(Z^4M_1^{31}N_1^{34})^{1/42},\
(Z^6M_1^{53}N_1^{51})^{1/66},\
(Z^6M_1^{46}N_1^{41})^{1/56},\\
(Z^2M_1^{38}N_1^{29})^{1/40},\
(ZM_1^9N_1^6)^{1/10},\
(Z^2M_1^7N_1^6)^{1/10},\\
(Z^3M_1^{43}N_1^{32})^{1/46},\
(ZM_1^6N_1^6)^{1/8},\
M_1^{1/2}N_1,\ M_1N_1^{1/2},\ Z^{-1/2}M_1N_1.
\end{gathered}
\tag{2.8}
\]

The choice $\alpha=\beta=1/2$ is allowed and the estimate is pointwise in $Z$ and one direction, but the coefficient must be separated and the power is insufficient.

## 3. Proof and derivation

Let $g=(h,r)$, $h=gH$, $r=gK$. Then $(H,K)=1$ and

\[
HK=s(t/g)^2.
\tag{3.1}
\]

Since $g^2\mid st^2$ and $s$ is squarefree, valuations give $g\mid t$. Coprimality allocates every odd-exponent prime to exactly one factor, yielding unique ordered $uv=s$ and

\[
H=ua^2,\qquad K=vb^2,\qquad (ua,vb)=1,\qquad g a b=t.
\]

Conversely these data recover $h,r$. Moreover

\[
r\ {\rm odd}\iff gvb\ {\rm odd},\qquad
\chi_4(r)=\chi_4(gv),\qquad r>4h\iff vb^2>4ua^2.
\]

This proves (1.1); $g=c\ell^2$ gives (1.2). At $t=1$, $g=a=b=1$, proving (1.5).

For fixed $t$, $st^2\in\mathcal I_M$ puts $s$ in $[M/t^2,2M/t^2)$. The number of squarefree $s$ is at most $M/t^2+1$. If nonempty, $t^2<2M$, hence

\[
\#\{s:st^2\in\mathcal I_M\}\leq M/t^2+1\leq3M/t^2.
\tag{3.2}
\]

Using $m^{-3/4}\leq M^{-3/4}$, $|C(m)|\leq d(m)\ll_\varepsilon X^\varepsilon$, and the literal profile sup norm, and dropping mask/cone/phase, gives (1.3). Smallest and terminal blocks obey the same count; exact radicals are absent from the strict mask, while the proof bounds a superset.

For the Diophantine geometry, put $x=t\sqrt{Ns}$ and $k=k_m$. A half-up tie is impossible because a half-integer square is not integral. Thus

\[
j_m=(k-x)(k+x),\quad
\operatorname{sgn}j_m=\operatorname{sgn}(k-x),\quad
\|t\sqrt{Ns}\|>\frac{M^{3/4}}{k+t\sqrt{Ns}}.
\tag{3.3}
\]

Writing $N=dq^2$ with $d$ squarefree, exact $j_m=0$ occurs iff $s=d$. Otherwise $Ns=DA^2$ with $D>1$ squarefree and

\[
j_m=k^2-D(At)^2,\qquad
\left|\frac{k}{At}-\sqrt D\right|
=\frac{|j_m|}{At(k+At\sqrt D)}.
\tag{3.4}
\]

Integrality yields only

\[
|k-At\sqrt D|\geq\frac1{k+At\sqrt D}.
\tag{3.5}
\]

The continued-fraction constant varies with $D$, and generalized Pell norms just above $M^{3/4}$ remain legal.

Finally, in the $t=1$ top box take $M_1=N_1=R$, $Z=R^3$, $\alpha=\beta=1/2$ in (2.8), and multiply by $R^{-3/2}$. The eleven exponents are

\[
\frac13,\ \frac{23}{66},\ \frac38,\ \frac{13}{40},\
\frac3{10},\ \frac25,\ \frac{15}{46},\ \frac38,\ 0,\ 0,\ -1.
\tag{3.6}
\]

Their maximum is $2/5$, proving the capacity statement.

## 4. First doubtful or unproved step

The exact formula, tail, and Pell identities above are proved. The first invalid closure step is replacing $C(st^2)$ by $d(s)$ or another complete fixed-$L$ coefficient. Already (1.5) is a signed, parity-restricted strict factorization cone, and no audited source reconstructs its complement with target-safe error.

Even granting this coefficient seam, (3.6) leaves $R^{2/5+\varepsilon}$. Separately, a fixed-$\alpha$ constant cannot be applied uniformly to $\alpha=t\sqrt N$. The missing result must estimate the individual fixed-centre scalar, not a cosine, mean square, or centre/kernel average.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_C_st2_cone_parity_character_parameterization` | **Pass.** Equations (1.1)--(1.2) retain ordered factors, parity, character, cone, and the only valid coprimality. |
| `large_square_part_t_tail_absolute_ledger` | **Pass.** Fixed $t$ supports at most $3M/t^2$ kernels; (1.3) is target-safe at $T=\lceil M^{1/4}\rceil$. |
| `j_mask_nearest_integer_sign_tie_and_exact_radical` | **Pass.** No tie; sign and threshold are exact; $j_m=0$ iff the kernel is that of $N$. |
| `quadratic_irrational_Pell_and_continued_fraction_exceptions` | **Pass as prohibition.** Equation (3.4) is exact; fixed-$D$ constants are not uniform, and legal near-threshold norms remain. |
| `t_equals_one_and_bounded_t_capacity` | **Fail for closure.** The mandatory (1.5) layer leaves $R^{2/5+\varepsilon}$ under the favorable source bound. |
| `individual_complex_direction_and_fixed_centre` | **Pass as audit, no applicable theorem.** No cosine or centre-average inference was used. |
| `primary_source_coefficient_support_and_frequency_match` | **No-go.** No card matches coefficient, support, phase, mask, direction, and uniformity simultaneously. |
| `full_R_M_s_t_power_and_dyadic_assembly` | **Pass.** The tail assembles at target scale; (3.6) records the full top-layer power ledger. |
| `Round144_owner_and_Round138_cross_term_separation` | **Pass.** Only Round 144's accepted cell/radical ledger is used; the Round-138 cross owner is untouched. |
| `downstream_M1_M2_endpoint_M9_and_exponent_scope` | **Pass.** No lower GAR, M1/M2, endpoint, M9, bridge, quarter, or exponent conclusion is claimed. |

No numerical experiment was performed.

## 6. Dependencies and exact artifacts used

The complete permitted context used was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/sqrt_divisor_twist_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reports/rational_shift_sqrt_twist_source_audit.md`;
- the exact task brief.

Primary sources are linked in Section 2. The sibling squarefree-fibre report was read only after this report's coefficient derivation and served only as a post-derivation cross-check. This report is therefore not offered as the campaign's independent blind seam.

No secondary theorem was used to claim applicability, no computation was used, and no shared state, synthesis, validation, plan, or graph file was edited.

## 7. Recommended state effect

**Promote only after conductor/seam review** the exact coefficient formulas (1.1)--(1.2) and the target-safe deletion $t\geq\lceil M^{1/4}\rceil$ as auxiliary components of `strict_squarefree_kernel_reduction`.

**Retain open** the small-$t$, especially $t=1$, fixed-centre scalar. **Reject as closure mechanisms:** complete-$d(n)$ substitution; treating bounded $t$ as bounded frequency; a uniform partial-quotient assertion for varying $\sqrt D$; applying a linear squarefree theorem to the nonlinear-$s$ phase; direct Robert--Sargos/Sargos--Wu import at target scale; or inference from a cosine or average.

The source no-go is a component of `strict_squarefree_kernel_reduction`, not an alternate terminal label. No downstream state changes.
