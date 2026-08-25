# Round 141 post-unmask review: source, Mellin, and scalar direction

Campaign: m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate

Task: blind_post_unmask_source_mellin_audit

Role: independent post-unmask source/Mellin and scalar-direction reviewer

Graph at assignment: 072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0

## 1. Result and final verdict

**Final verdict: GREEN.**  The repaired candidate is sufficient on every assigned seam.  The double-Mellin identity, the ratio-smoothing/Perron comparison, both Robert--Sargos specializations, the genuine Sargos--Wu theorem and adjacent general-domain distinction, the Tao--Trudgian--Yang exponent in (141.C36), the Popov/Li--Yang exponent in (141.C37), and the warning about a radial cosine versus one complex branch are all independently reproducible.  The candidate now correctly records that Sargos--Wu Theorem 9 assumes
\[
\alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\ne0
\]
and therefore admits \(\alpha=\beta=1/2\), while the adjacent general-domain lemma has the different rank-one exclusion.  Its balanced conclusion is only \(R^{2/5+\varepsilon}\), exactly as the repaired candidate states.

| Audited seam | Status |
|---|---|
| Double-Mellin factor in (141.C35) | **GREEN** |
| \(O(1)\) smoothing cost, sharp-Perron height, and smooth ratio bandwidth | **GREEN** |
| Robert--Sargos hypotheses and the separated \(R^{1/2}\)/joint \(R^{3/4}\) ledger | **GREEN** |
| Sargos--Wu \(R^{2/5}\) route and adjacent general-domain exclusion | **GREEN** |
| Tao--Trudgian--Yang hypotheses and (141.C36) | **GREEN** |
| Popov/Li--Yang hypotheses and (141.C37) | **GREEN**, only for the repaired complete radial cosine statement |
| Radial cosine versus one complex branch | **GREEN** |
| Banerjee--Khurana, Kaczorowski--Perelli, and Mellin-moment mismatch | **GREEN** |
| Claim that no quoted source closes (141.C38) | **GREEN** |

This review does not assess or certify the candidate's cone, coefficient, phase-cell, or additive-resonance discoveries.

## 2. Exact Mellin and bandwidth statement

Let \(\Psi\) be smooth and compactly supported in a dyadic \(h,r\) block and define
\[
\widetilde\Psi(s,t)=\int_0^\infty\!\!\int_0^\infty
\Psi(u,v)u^sv^t\,\frac{du}{u}\frac{dv}{v},
\qquad u=hr,\quad v=\frac r{4h}.
\]
On contours satisfying \(\Re(s-t)>1\) and \(\Re(s+t)>1\), inversion gives
\[
u^{-s}v^{-t}=4^t h^{-s+t}r^{-s-t}.
\]
Consequently, summing \(h\) and \(\chi_4(r)\) first produces
\[
4^t\zeta(s-t)L(s+t,\chi_4).
\]
The substitution \(t\mapsto-t\) is exactly
\[
4^{-t}\zeta(s+t)L(s-t,\chi_4),
\]
which proves (141.C35).  Parity has not been dropped because \(\chi_4(r)=0\) for even \(r\).  Smooth dyadic weights in \(h,r\) may indeed be written in \((u,v)\), since \(h=\frac12\sqrt{u/v}\) and \(r=2\sqrt{uv}\).  **Mellin seam: GREEN.**

Put \(\delta=H^{-1/2}\).  At fixed \(h\asymp H\), a transition of relative \(v\)-width \(\delta\) changes \(O(h\delta+1)=O(\sqrt H)\) admissible odd \(r\)'s.  There are \(O(H)\) heights, and \((hr)^{-3/4}\asymp H^{-3/2}\) on the balanced transition, so the absolute change is \(O(H\sqrt H\,H^{-3/2})=O(1)\) per block.  A sharp step has nearest admissible ratio \(r/(4h)=1\pm(4h)^{-1}\), hence \(|\log(r/(4h))|\asymp H^{-1}\); a truncated Perron kernel needs \(T|\log v|\gg1\), and therefore \(T\gg H\).  For a smooth transition, integration by parts yields rapid decay once \(|t|\delta\gg1\), hence effective bandwidth
\[
|\Im t|\lesssim\delta^{-1}X^\varepsilon=H^{1/2}X^\varepsilon.
\]
Moreover, the Fourier/Mellin transform of a smoothed step has \(L^1\)-norm \(O(\log(1/\delta))\): it is \(O(1/|t|)\) for \(1\ll|t|\ll\delta^{-1}\) and rapidly decreasing beyond.  Thus separating the smoothed ratio weight costs only \(X^\varepsilon\), not \(H^{1/2}\).  **Smoothing/Perron seam: GREEN.**

## 3. Independent primary-source hypothesis audit

**Robert--Sargos: GREEN.**  Theorem 1 of [Robert--Sargos](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf) assumes \(X_1>1\), bounded coefficients, and
\(\alpha(\alpha-1)\beta\gamma\ne0\), and proves
\[
S_0\ll_\varepsilon(HN_1M)^{1+\varepsilon}
\left\{\left(\frac{X_1}{HN_1M^2}\right)^{1/4}
+(HN_1)^{-1/4}+M^{-1/2}+X_1^{-1/2}\right\}.
\]
All monomial exponents \(1/2\) satisfy the nondegeneracy condition.  The theorem permits one arbitrary joint coefficient \(a(h,n)\), while its better \(R^{1/2}\) specialization puts the two long variables in the separated coefficient slots and therefore requires the already-proved smoothing/Mellin separation.  The repaired candidate states both cases with this qualification.

**Sargos--Wu: GREEN.**  The accessible exact restatement in Lemma 5.1 of [On a Diophantine inequality over primes](https://doi.org/10.1016/j.jnt.2019.01.008) says explicitly that it is Theorem 9 of the [original Sargos--Wu paper](https://doi.org/10.1023/A:1006777803163) and assumes
\[
\alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\ne0
\]
for a sum with separated bounded coefficients \(a(m)b(n)\).  The immediately following Lemma 5.2 is the general-domain derivative-comparability estimate with
\(\alpha\beta(\alpha+\beta-1)(\alpha+\beta-2)\ne0\).  The older official [Kumchev paper](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/89/4/110759/a-diophantine-inequality-involving-prime-powers) independently records the former statement as Sargos--Wu Theorem 9.  The repaired candidate now states the correct dichotomy: Sargos--Wu accepts the square-root monomial but only separated coefficients; the general-domain lemma accepts a joint domain but excludes this rank-one exponent.  Neither closes the target.

**Tao--Trudgian--Yang: GREEN.**  Definition 11 and Theorem 20 of [Tao--Trudgian--Yang](https://arxiv.org/pdf/2501.16779) give
\[
\sum_{n\in I}e(TF(n/N_1))
\ll_\varepsilon (T/N_1)^{\kappa+\varepsilon}N_1^{\lambda+\varepsilon}
\]
for the stated model-phase class and \(T\ge N_1\ge1\), and list
\((\kappa,\lambda)=(89/1282,997/1282)\).  The phase \(u^{1/2}\) lies in the class; splitting \(\chi_4\) into its two odd residue classes and partial summation preserve the hypotheses.

**Popov/Li--Yang: GREEN with the recorded repair.**  Popov's Theorem 5 in the [official Math-Net paper](https://www.mathnet.ru/eng/rm10162) is a complete \(r_2(n)\)-weighted cosine formula.  The Li--Yang input is certified only in the repaired narrow form recorded in sources/li_yang_2023.md; this review does not import their printed general theorem beyond that repair.

**Other quoted sources: GREEN as obstructions.**  Banerjee--Khurana Theorems 4.3--4.4 have an odd primitive character, nonintegral endpoints, an analytic test function, the complete generalized-divisor coefficient, and the strict strip \(0<\Re\nu<1/2\), so \(\nu=0\) and the incomplete mask are unavailable.  Kaczorowski--Perelli study a fixed standard-twist parameter \(\alpha\), whereas here \(\alpha=\sqrt{N_0}\asymp R^2\) grows and \(A_\rho\) is not the coefficient sequence of the fixed \(L\)-function.  Bourgain and Petrow--Young supply individual pointwise \(L\)-bounds; Müller supplies the product mean square only at zero opposite shift; Heap allows shifts \(O(1/\log U)\) and Dirichlet-polynomial length \(U^{1/11-\varepsilon}\), not the required \(|v|\lesssim U^{1/6}\).  These hypothesis mismatches are genuine.

## 4. Complete \(R\)-power and scalar-direction audit

At \(H\asymp K\asymp R\), \(N_0\asymp R^4\), the phase scale is
\[
X_1\asymp\sqrt{N_0HK}\asymp R^3,
\qquad (HK)^{-3/4}\asymp R^{-3/2}.
\]

For Robert--Sargos, the separable smoothed specialization
\((H,N_1,M)=(R,1,R)\) has raw size \(R^2\), hence normalized size
\(R^{1/2+\varepsilon}\).  In contrast, the direct exact-joint specialization
\((H,N_1,M)=(R,R,1)\) has a first term
\[
R^2\left(\frac{R^3}{R^2}\right)^{1/4}=R^{9/4},
\]
and therefore gives \(R^{3/4+\varepsilon}\), not \(R^{1/2+\varepsilon}\).  Thus the repaired candidate's \(R^{1/2}\) for the smoothed/separated cone and \(R^{3/4}\) for the exact-joint dummy-variable output are both correct.

For the genuine Sargos--Wu Theorem 9, substituting \(X=R^3\), \(M=N=R\), and then the weight \(R^{-3/2}\) gives, term by term,
\[
\frac13,\quad\frac{23}{66},\quad\frac38,\quad\frac{13}{40},
\quad\frac3{10},\quad\frac25,\quad\frac{15}{46},\quad\frac38,
\quad0,\quad0,\quad-1
\]
as the exponents of \(R\).  The maximum is \(2/5\), so after smooth Mellin separation this source yields only
\[
R^{2/5+\varepsilon}.
\]
It is stronger than the quoted rowwise exponent-pair result but remains polynomial.

For a fixed \(h\), Tao--Trudgian--Yang gives
\(R^{2\kappa+\lambda+\varepsilon}\).  Summing \(R\) rows and multiplying by \(R^{-3/2}\) gives
\[
R^{2\kappa+\lambda-1/2+\varepsilon},\qquad
2\frac{89}{1282}+\frac{997}{1282}-\frac12
=\frac{267}{641}.
\]
Thus (141.C36) is **GREEN**.

Popov gives, with \(x=N_0\asymp R^4\) and cutoff \(M\asymp R^2\),
\[
\sum_{n\le M}r_2(n)n^{-3/4}
\cos(2\pi\sqrt{nx}+\pi/4)
=-\pi x^{-1/4}P(x)+\text{target-safe remainder}.
\]
Using the repaired
\(\theta_*=(3292+25\sqrt{1717})/13762\) gives
\[
x^{\theta_*-1/4}=R^{4\theta_*-1}
=R^{(50\sqrt{1717}-297)/6881}.
\]
The outer \(x^{1/4}\asymp R\) was indeed removed here and must be restored in the original formula.  Thus (141.C37) is **GREEN**.

For the Mellin ledger, \(M=HK\asymp R^2\) and
\(U=\sqrt{N_0M}\asymp R^3\).  Pointwise Bourgain plus Petrow--Young gives
\[
M^{-1/4}U^{1/2+13/84+1/6+\varepsilon}
=R^{55/28+\varepsilon},
\]
while even the postulated uniform shifted mean square followed by Cauchy gives
\[
M^{-1/4}U^{1/2+\varepsilon}=R^{1+\varepsilon}.
\]
Both powers are arithmetically correct and nonclosing.

Finally, if
\[
S_+(x)=\sum_{n\le M}r_2(n)n^{-3/4}e(\sqrt{nx}),
\]
then Popov controls only
\[
\Re\!\left(e(1/8)S_+(x)\right)
=\frac12\left(e(1/8)S_+(x)+e(-1/8)\overline{S_+(x)}\right).
\]
A bound for this one real projection does not bound \(S_+(x)\) or either conjugate branch; a second independent sine projection would be required.  Changing \(x\) does not automatically provide it because every \(n\)-phase and the cutoff change.  The complete coefficient \(r_2\) also differs from the incomplete cone coefficient.  **Scalar-direction seam: GREEN.**

## 5. First doubtful or unproved step

No doubtful source or Mellin step remains before (141.C38) on the assigned seams.  The first genuinely unproved mathematical estimate is exactly (141.C38).  None of the verified source theorems supplies an \(R^\varepsilon\) estimate for its fixed-centre, signed, incomplete, nonresonant scalar.  In particular, the genuine Sargos--Wu route stops at \(R^{2/5+\varepsilon}\), and the numerically smaller Popov/Li--Yang exponent applies to the wrong coefficient and only one real combination.

## 6. Required controls, outcomes, and dependencies

The required controls all have determinate outcomes:

1. **Mellin-sign control: PASS.**  Deriving the factor before \(t\mapsto-t\) gives \(4^t\zeta(s-t)L(s+t,\chi_4)\), so (141.C35) has the correct signs and factor \(4^{-t}\).
2. **Transition-count control: PASS.**  \(H\) heights times \(O(\sqrt H)\) changed \(r\)'s times weight \(H^{-3/2}\) is \(O(1)\).
3. **Perron-resolution control: PASS.**  The closest odd \(r\) is \(4h\pm1\), forcing sharp height \(T\gg H\); smooth width \(H^{-1/2}\) has bandwidth \(H^{1/2}X^\varepsilon\) and only logarithmic Mellin \(L^1\)-cost.
4. **Source-numbering control: PASS.**  The repaired candidate distinguishes the exact Sargos--Wu Theorem 9 restatement from the adjacent general-domain lemma and assigns their different hypotheses and coefficient geometries correctly.
5. **Power-substitution control: PASS.**  Direct substitution gives Robert--Sargos \(R^{3/4}\) for the exact joint slot, \(R^{1/2}\) after separable smoothing, Sargos--Wu \(R^{2/5}\), TTY \(R^{267/641}\), Popov/Li--Yang \(R^{(50\sqrt{1717}-297)/6881}\), pointwise Mellin \(R^{55/28}\), and ideal mean-square/Cauchy \(R\).
6. **Complex-direction control: PASS.**  One real projection can vanish while the orthogonal imaginary projection is arbitrarily large, so no individual-branch estimate follows.
7. **Closure control: PASS as a no-go.**  Every applicable quoted theorem retains a positive power or has the wrong coefficient, parameter uniformity, shift range, or scalar direction.

Exact local artifacts used were protocol.md; state/proof_obligations.yml; state/active_campaign.yml; rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md; rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/sqrt_divisor_twist_source_audit.md; sources/popov_2024_voronoi_gauss.md; sources/li_yang_2023.md; sources/banerjee_khurana_2023.md; and sources/papers/banerjee_khurana_2023.txt.  Primary checks used the Robert--Sargos PDF, the Sargos--Wu DOI together with the exact 2019 restatement and official Kumchev restatement, the Tao--Trudgian--Yang PDF, the Popov Math-Net paper, Li--Yang's arXiv record as constrained by its repaired local card, Banerjee--Khurana arXiv 2306.12399, Kaczorowski--Perelli's EMS paper, Bourgain arXiv 1408.5794, Petrow--Young's Annals paper, Müller's Cambridge paper, and Heap arXiv 1211.2182.  No numerical experiment was used.

## 7. Recommended state effect

**PROMOTE the repaired source/Mellin/scalar-direction paragraph on the assigned seams.**  Retain (141.C35), the smoothing/Perron bandwidth conclusion, the separated and exact-joint Robert--Sargos powers, the two distinct Sargos--Wu/general-domain obstructions, (141.C36), (141.C37), the scalar-direction warning, and the statement that (141.C38) remains open.  The repaired paragraph now matches the independent source and power audit without qualification.  Make no state effect on the cone/additive-resonance discoveries outside the assigned seams.
