# Final source/capacity audit of the Round-145 conductor candidate

- Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`
- Candidate: `candidates/conductor_round145_squarefree_kernel_reduction.md`
- Review seam: primary-source hypotheses, capacity powers, coefficient/frequency/direction exceptions, and terminal scope
- Allocation: 100% analytic/source verification; 0% numerical

## 1. Result

\[
\boxed{\mathsf{GREEN}.}
\]

Candidate Section 5 accurately and conservatively summarizes the audited primary results. The $R^{2/5+\varepsilon}$, $R^{1/2+\varepsilon}$, and $R^{3/4+\varepsilon}$ ledgers recompute correctly. The growing-frequency, coefficient-class, individual-direction, and exceptional-family qualifications are retained. Formula (145.C6) is an exact alternative packaging and does not conflict with the full-gcd formula (145.C8). The source no-go is correctly a component of the terminal label

\[
\mathsf{strict\_squarefree\_kernel\_reduction},
\]

not an alternate label or a claim that the target estimate is false.

## 2. Exact statements and hypotheses audited

The source summaries in candidate Section 5 have the following exact scope.

1. **Uchiyama.** The underlying theorem is for the complete coefficient $d(n)$ on a fixed arithmetic progression, a sharp cutoff, and one positive complex direction. Its nonresonant $O_x(\log Y)$ constant may depend on the fixed frequency $x$; at $x=2\sqrt q/k$ it has the stated resonant branch. Describing it as complete-divisor/fixed-frequency input that does not accept $C(st^2)$ is correct. The candidate does not confuse source spectral resonance with the termwise $j=0$ fibre.
2. **Kaczorowski--Perelli.** The standard twist uses coefficients of one fixed extended-Selberg-class $L$-function and treats fixed $\alpha$, with weak moving-$\alpha$ uniformity. For the degree-two complete divisor specialization, its spectrum is $\alpha=2\sqrt q$. Candidate Section 5 correctly uses it only as a complete-coefficient resonance comparison.
3. **Sun.** The theorem is genuinely uniform for every nonzero real $\alpha$, treats the individual complex direction, and has exactly the Liouville coefficient. The candidate correctly records both the coefficient mismatch and the lack of target power when $Y\asymp|\alpha|\asymp R^2$.
4. **Schlage-Puchta.** The theorem is for $\mu^2(n)e(\alpha n)$ with a linear phase in the squarefree variable and explicit major/minor-arc rational-approximation conditions. Candidate Section 5 correctly explains why neither the nonlinear-$s$ orientation nor the linear-$t$ orientation matches the actual coefficient and mask.
5. **Fixed quadratic irrational input.** Duke's relevant statements are fixed-$\alpha$ statements; they do not give a constant uniform in the varying discriminant $q_s$. The candidate uses them only to prohibit a uniform bounded-partial-quotient inference.
6. **Robert--Sargos and Sargos--Wu.** The former has one bounded joint coefficient and one separated coefficient; the latter requires separated bounded coefficients. Both treat individual monomial phases pointwise, but neither theorem natively accepts the exact joint squarefree/coprime/cone/mask coefficient. Candidate Section 5 explicitly grants favorable smoothing/separation only for a capacity test.

No source is used beyond its coefficient, support, smoothing, frequency, exceptional-set, or direction hypotheses.

## 3. Derivation and power checks

### 3.1 Compatibility of (145.C6) and (145.C8)

For each prime $p$, put $A=v_p(h)$ and $B=v_p(r)$. In (145.C6):

- $p\mid\gamma$ exactly when $A$ and $B$ are both odd;
- $p\mid d$ exactly when $A$ is odd and $B$ even;
- $p\mid e$ exactly when $A$ is even and $B$ odd.

Hence $\gamma,d,e$ are pairwise coprime and squarefree, $de=s$, and

\[
h=\gamma d a^2,\qquad r=\gamma e b^2,\qquad t=\gamma ab
\]

with multiplicity one. The conditions $\gamma\mid t$, $(\gamma,s)=1$, and $\gamma$ squarefree are therefore exact. Odd $r$ is exactly $\gamma,e,b$ odd, the character is $\chi_4(\gamma)\chi_4(e)$, and the strict cone is $eb^2>4da^2$. No coprimality on $a,b$ or between them and $\gamma$ is legal or asserted.

In (145.C8), $G=(h,r)$ contains the full common prime power, while $\gamma$ contains only the common odd-parity part of the squarefree kernels. Thus the squarefree kernel $c={\rm sf}(G)$ may overlap the quotient variables in (145.C8), exactly as the candidate states. The two formulas encode different allocations of common square powers and do not conflict.

### 3.2 Sargos--Wu

On the balanced $t=1$ top box,

\[
M_1=N_1=R,\qquad Z=R^3,\qquad \alpha=\beta=\frac12,
\]

and the target weight is $R^{-3/2}$. The eleven terms of Theorem 9 give normalized exponents

\[
\frac13,\ \frac{23}{66},\ \frac38,\ \frac{13}{40},\
\frac3{10},\ \frac25,\ \frac{15}{46},\ \frac38,\ 0,\ 0,\ -1.
\]

The maximum is $2/5$, so (145.C22) is correct.

### 3.3 Robert--Sargos

For the favorable separated specialization $(H,N_1,M_1)=(R,1,R)$ with $X_1\asymp R^3$, Theorem 1 gives raw size $R^{2+\varepsilon}$ from its first term; after $R^{-3/2}$ this is $R^{1/2+\varepsilon}$. For the dummy-variable specialization $(H,N_1,M_1)=(R,R,1)$ capable of carrying the exact joint coefficient, the first term is raw $R^{9/4+\varepsilon}$, hence normalized $R^{3/4+\varepsilon}$. Both candidate powers are correct.

### 3.4 Growing frequency and exceptional family

For fixed or bounded $t$, the twist frequency in the $s$-sum is $\alpha=t\sqrt N$, so it still grows; the candidate never treats bounded $t$ as fixed source frequency. Its family (145.C17)--(145.C18) is used only to refute a uniform frequency gap or partial-quotient bound. It is not used as an aggregate lower bound, a source theorem, or a replacement for the signed estimate. That calibration is correct.

## 4. First doubtful or unproved step

No source-level or power-ledger defect was found.

The first unproved analytic estimate remains exactly the small-$t$ scalar (145.C2), with the $t=1$ requirement isolated in (145.C23). The candidate correctly does not infer that this estimate fails from a positive source upper-bound power. It also does not infer an individual positive-direction estimate from a cosine, conjugate pair, or centre average.

## 5. Control outcomes

| Audit item | Outcome |
|---|---|
| Exact primary-source coefficient/support hypotheses | **GREEN.** All summaries are narrower than or equal to the source statements. |
| Growing-frequency uniformity | **GREEN.** Fixed/weakly uniform inputs are not promoted to $\alpha=t\sqrt N$ uniformity; Sun's genuinely uniform theorem is separately power-audited. |
| Individual complex direction | **GREEN.** The target remains the positive direction, and no real/cosine or averaged substitute is used. |
| Exceptional/spectral/Pell families | **GREEN.** Exact radical, complete-divisor spectral resonance, and varying Pell/continued-fraction families remain distinct. |
| Sargos--Wu $R^{2/5}$ ledger | **GREEN.** Recomputed exactly. |
| Robert--Sargos $R^{1/2}$ and $R^{3/4}$ ledgers | **GREEN.** Recomputed exactly. |
| Formula (145.C6) versus full-gcd (145.C8) | **GREEN.** Both are multiplicity-one parametrizations with different common-square allocations. |
| Capacity versus signed lower bound | **GREEN.** All positive powers are stated only as limitations of available upper bounds. |
| Terminal label and source-no-go calibration | **GREEN.** The no-go is a component of `strict_squarefree_kernel_reduction`. |
| Downstream scope | **GREEN.** No M1/M2, endpoint, M9, bridge, quarter, or exponent promotion is claimed. |

## 6. Dependencies and artifacts used

- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/candidates/conductor_round145_squarefree_kernel_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reports/quadratic_irrational_divisor_twist_source_audit.md`;
- the primary sources and exact theorem cards linked in that finalized source report.

No numerical experiment was performed, and no candidate or shared-state file was edited.

## 7. Recommended state effect

**GREEN:** accept the candidate's Section 5 source/capacity component and its use in the terminal label `strict_squarefree_kernel_reduction`. This review recommends no correction to the candidate and no independent downstream promotion beyond the candidate's stated scope.
