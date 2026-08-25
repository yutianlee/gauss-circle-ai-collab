# Discovery cross-audit of the multidimensional monomial source report

- Campaign: m9-m1-lower-cone-three-variable-hessian-dispersion-gate
- Round: 146
- Reviewed artifact: reports/multidimensional_monomial_source_audit.md
- Reviewer role: discovery/source-power cross-review
- Starting graph SHA-256: 7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d
- Status: review evidence only; no shared proof-state edit

## 1. Verdict

\[
\boxed{\mathsf{CONDITIONAL\ GREEN:\ all\ quoted\ power\ arithmetic\ checks,\ with\ two\ local\ corrections\ and\ two\ source\ qualifications.}}
\]

The Cao--Zhai Theorem-6 variable placement and all fourteen balanced normalized exponents are correct. In particular, term 1 is

\[
 R^{(3-5\tau)/8},
 \qquad \eta_1(1/2)=\frac1{16},
\]

not a target-sized term. The Robert--Sargos top-box power is also correct, and the Sargos--Wu sixth term is correctly normalized to

\[
 R^{2/5-3\tau/10},
 \qquad R^{1/4}\ \text{at}\ \tau=\frac12.
\]

The exact coefficient-class mismatches are genuine, and the report's final conclusion is properly a no-go for direct use of the audited black-box estimates, not a lower bound for the signed scalar.

Two local corrections are required.

1. The instruction to choose the larger of \(D,E\) as the Cao--Zhai distinguished variable is correct **for term 1 only**. A single placement must be used in the whole fourteen-term sum, and other terms can prefer the opposite placement. The balanced obstruction is unchanged.
2. Sargos self-return must be stated as a **phase-level** coefficient involution \(c\mapsto-2/c\), after reversal of the alias orthant. It is not an amplitude-level two-step Poisson identity. Alias count and \(\mathcal F^{3/2}\) are upper-capacity statements unless the relevant lattice count is separately supplied.

There are also two source-verification qualifications. The primary Cao--Zhai and Robert--Sargos PDFs were independently checked and match the report. The original Sargos--Wu Theorem 9 and Sargos 2015 Theorem 5.2 full texts were not independently retrievable in this review. Their quoted formulas are therefore audited algebraically but remain conditional on the source auditor's transcription; no missing theorem hypothesis is guessed below.

## 2. Cao--Zhai Theorem 6: legal placement and coefficient scope

The primary statement defines

\[
 S_I(M,M_1,M_2)
 =\sum_{m\sim M}\sum_{m_1\sim M_1}\sum_{m_2\sim M_2}
 a(m)b(m_1,m_2)e(A m^\alpha m_1^\beta m_2^\gamma)
\]

and imposes

\[
 \alpha(\alpha-1)(\alpha-2)(\alpha-3)\gamma(\gamma-1)\ne0,
 \qquad |a|,|b|\le1,
 \qquad F=|A|M^\alpha M_1^\beta M_2^\gamma\gg M.
\]

There is no displayed restriction on \(\beta\). For the exponent multiset

\[
 t^1d^{1/2}e^{1/2},
\]

the exponent \(1\) cannot occupy either the \(\alpha\)-slot or the \(\gamma\)-slot. Hence \(t\) must occupy the \(\beta\)-slot, while \(d,e\) occupy the other two slots. Up to swapping \(d,e\), the unique legal placement is therefore

\[
 (m,m_1,m_2)=(d,t,e),\qquad
 (\alpha,\beta,\gamma)=\left(\frac12,1,\frac12\right),\qquad
 (M,M_1,M_2)=(D,T,E),
\]

with

\[
 F=\sqrt N\,T\sqrt{DE}=\mathcal F.
\]

On the balanced top box \(\mathcal F=R^3\) and \(D=E=R^{1-\tau}\), so the size hypothesis \(F\gg M\) passes by a large power. This placement audit is GREEN.

The coefficient audit is also GREEN and adverse. The theorem accepts only

\[
 a(d)b(t,e)
 \quad\text{or, after swapping,}\quad
 a(e)b(t,d).
\]

The literal coefficient contains \(de\) squarefree, \((d,e)=1\), the conditions \(\gamma\mid t\) and \((\gamma,de)=1\), the factorization \(ab=t/\gamma\), the moving cone \(eb^2>4da^2\), parity and character conditions, and the joint product profile. It is not literally of either source form. The divisor-size loss may be absorbed into \(R^\varepsilon\), but separability cannot; it requires a new bounded-projective-norm decomposition.

## 3. Independent fourteen-term Cao--Zhai ledger

Put

\[
 Q=R^2,\qquad T=R^\tau,\qquad D=E=R^{1-\tau},\qquad
 \mathcal F=R^3,\qquad Q^{-3/4}=R^{-3/2}.
\]

For a source contribution

\[
 \mathcal B=(\mathcal F^aD^bT^cE^c)^{1/q},
\]

direct substitution gives the normalized exponent

\[
 Q^{-3/4}\mathcal B
 =R^{\eta(\tau)},
 \qquad
 \eta(\tau)=\frac{3a+b+c-b\tau}{q}-\frac32.                 \tag{3.1}
\]

Applying (3.1) independently to the fourteen displayed terms gives:

| \(i\) | \((a,b,c;q)\) | independently computed \(\eta_i(\tau)\) | \(\eta_i(1/2)\) |
|---:|---:|---:|---:|
| 1 | \((1,5,7;8)\) | \((3-5\tau)/8\) | \(1/16\) |
| 2 | \((0,8,7;8)\) | \(3/8-\tau\) | \(-1/8\) |
| 3 | \((4,43,54;58)\) | \((22-43\tau)/58\) | \(1/116\) |
| 4 | \((7,82,100;108)\) | \((41-82\tau)/108\) | \(0\) |
| 5 | \((3,37,46;49)\) | \((37-74\tau)/98\) | \(0\) |
| 6 | \((3,46,54;58)\) | \((11-23\tau)/29\) | \(-1/58\) |
| 7 | \((29,250,294;336)\) | \((127-250\tau)/336\) | \(1/168\) |
| 8 | \((25,230,266;304)\) | \((115-230\tau)/304\) | \(0\) |
| 9 | \((25,262,294;336)\) | \((127-262\tau)/336\) | \(-1/84\) |
| 10 | \((-1,181,188;200)\) | \((66-181\tau)/200\) | \(-49/400\) |
| 11 | \((-1,334,344;368)\) | \((123-334\tau)/368\) | \(-11/92\) |
| 12 | \((-4,190,188;200)\) | \((66-190\tau)/200\) | \(-29/200\) |
| 13 | \((0,5,6;6)\) | \((2-5\tau)/6\) | \(-1/12\) |
| 14 | \((-1,9,8;8)\) | \((2-9\tau)/8\) | \(-5/16\) |

Thus every entry in the report's table is exact. For term 1 specifically,

\[
\begin{aligned}
R^{-3/2}
 (R^3R^{5(1-\tau)}R^{7\tau}R^{7(1-\tau)})^{1/8}
 &=R^{(3-5\tau)/8},\\
\eta_1(1/2)&=\frac{3-5/2}{8}=\frac1{16}.
\end{aligned}
\]

Terms 1, 3, and 7 remain positive at the formal endpoint, and term 1 is the largest. Since the source right side is a sum, its term 1 is part of the black-box upper bound and cannot be deleted. This proves only that the displayed theorem does not itself deliver the target; it does not prove that the actual signed sum is large.

There is one asymmetric-placement correction. If \(d\) is distinguished, term 1 is indeed

\[
 Q^{-3/4}(\mathcal F D^5T^7E^7)^{1/8}
 =R^{1/4}Q^{-1/16}T^{-3/8}E^{1/4},                 \tag{3.2}
\]

so term 1 alone is minimized by making the larger of \(D,E\) distinguished. But term 2 becomes

\[
 Q^{-3/4}(D^8T^7E^7)^{1/8}
 =Q^{1/4}T^{-9/8}E^{-1/8},                         \tag{3.3}
\]

which prefers the opposite choice. Therefore replace “thus one chooses the larger” by “for term 1 alone one chooses the larger”; one legal placement must be held fixed through the entire source sum. Equations (3.2)--(3.3) do not affect the balanced-box no-go because \(D=E\).

## 4. Robert--Sargos and Sargos--Wu top-box powers

### Robert--Sargos Theorem 1

The primary theorem statement and coefficient class in the report are exact. With

\[
 (H,N_0,M_0)=(T,E,D),\qquad \mathcal X=\mathcal F=R^3,\qquad
 HN_0M_0=R^{2-\tau},
\]

the four brace terms, after multiplication by \(R^{-3/2}\), have exponents

\[
 \boxed{
 \frac12-\frac\tau2,\qquad
 \frac14-\tau,\qquad
 -\frac\tau2,\qquad
 -1-\tau.}                                             \tag{4.1}
\]

At \(\tau=1/2\), these are \(1/4,-1/4,-1/4,-3/2\). The first is dominant throughout \(0\le\tau\le1/2\), so the report's \(R^{1/2-\tau/2}\) and endpoint \(R^{1/4}\) are correct. The theorem permits only \(a(t,e)b(d)\), or its analogous legal swaps, and therefore does not accept the literal joint coefficient.

### Sargos--Wu Theorem 9

Conditional on the report's transcription of the original theorem, a fixed \(t\)-row has \(Z=\mathcal F=R^3\), \(D=E=R^{1-\tau}\), and the row sum and radial weight contribute \(R^{\tau-3/2}\). The eleven displayed terms then have normalized exponents

| term | exponent | value at \(\tau=1/2\) |
|---:|---:|---:|
| 1 | \((14-23\tau)/42\) | \(5/84\) |
| 2 | \((23-38\tau)/66\) | \(2/33\) |
| 3 | \((21-31\tau)/56\) | \(11/112\) |
| 4 | \((13-27\tau)/40\) | \(-1/80\) |
| 5 | \((3-5\tau)/10\) | \(1/20\) |
| 6 | \((4-3\tau)/10\) | \(1/4\) |
| 7 | \((15-29\tau)/46\) | \(1/92\) |
| 8 | \((3-4\tau)/8\) | \(1/8\) |
| 9 | \(-\tau/2\) | \(-1/4\) |
| 10 | \(-\tau/2\) | \(-1/4\) |
| 11 | \(-1-\tau\) | \(-3/2\) |

The sixth term is largest on the whole interval \(0\le\tau\le1/2\), and it is exactly

\[
 \frac{4-3\tau}{10}=\frac25-\frac{3\tau}{10}.
\]

Thus the report's Sargos--Wu power is correct and, at the formal endpoint, leaves \(R^{1/4}\). At fixed \(t\), the literal \(d,e\)-coefficient still contains joint squarefreeness/coprimality and the moving cone, so it is not the separated \(a_d b_e\) coefficient quoted from the theorem.

The exact original Theorem-9 hypothesis line was not independently available in this review. In particular, the condition

\[
 \alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\ne0
\]

should remain attached to the source auditor's primary transcription rather than be promoted from this cross-review alone. If that transcription is exact, \(\alpha=\beta=1/2\) passes it.

## 5. Sargos transform: scope, aliases, and self-return

For the smooth bare phase \(f_c(t,d,e)=c\,t\sqrt{de}\), direct differentiation and inversion give

\[
 u=c\sqrt{de},\qquad
 v=\frac{ct}{2}\sqrt{e/d},\qquad
 w=\frac{ct}{2}\sqrt{d/e},
\]

\[
 t=\frac{2\sqrt{vw}}c,\qquad
 d=\frac uc\sqrt{w/v},\qquad
 e=\frac uc\sqrt{v/w}.
\]

Since \(f_c\) is homogeneous of degree \(2\), Sargos's sign convention yields

\[
 f_c^*(u,v,w)=-\frac2c\,u\sqrt{vw}.                    \tag{5.1}
\]

Equation (5.1) is exact. Its iteration needs a sign qualification: starting from \(c>0\), the first aliases lie in the positive gradient orthant and the dual coefficient is negative. The second gradient lies in the opposite alias orthant. After reflecting that orthant, the phase coefficient satisfies

\[
 c\longmapsto-\frac2c\longmapsto c.                   \tag{5.2}
\]

Thus (5.2) is a phase-monomial involution after alias sign reversal. It is not a literal identity for the transformed amplitude, support, Maslov factor, boundary contribution, or arithmetic coefficient.

The alias power also checks. Put \(P=TDE\). The dual side lengths are

\[
 \frac{\mathcal F}{T},\qquad
 \frac{\mathcal F}{D},\qquad
 \frac{\mathcal F}{E}.
\]

For a fixed smooth interior gradient image,

\[
 \#\{\text{dual aliases}\}\ll\frac{\mathcal F^3}{P};              \tag{5.3}
\]

an asymptotic requires a positive-volume interior and the corresponding lattice-boundary estimate. The stationary prefactor is \(P/\mathcal F^{3/2}\), so aliaswise triangle inequality gives the upper price

\[
 \frac{P}{\mathcal F^{3/2}}
 \#\{\text{aliases}\}
 \ll \mathcal F^{3/2}.                              \tag{5.4}
\]

At the top, \(\mathcal F=R^3\), and (5.4), after the physical weight \(R^{-3/2}\), is \(R^3\). In the ideal full-interior count, \(R_0\asymp1\); with only (5.3), one should state \(R_0\ll1\). The quoted first transform error is then an available upper term of size at most \(\mathcal F\), namely \(R^{3/2}\) after radial normalization. Neither (5.4) nor that error is a lower bound.

The theorem's smooth-amplitude scope does not include the literal arithmetic coefficient. The remarks about \(\mathcal F/M_i^2\) describe when a \(B\)-transform is expected to shorten the problem; they are not to be listed as formal theorem hypotheses unless the exact source passage is supplied. Here their failure is a useful non-shortening diagnostic, while the rigorous direct-route obstructions are the amplitude mismatch and the displayed upper-power ledger.

The exact regularity thresholds and error exponents quoted from Sargos 2015 were not independently source-certified in this review because the full primary text was unavailable. The phase calculation (5.1), alias scaling (5.3), and capacity (5.4) are independent of that uncertainty.

## 6. Source uncertainty and no-go calibration

The following source checks are GREEN.

- Cao--Zhai Theorems 6--7 were checked in the [primary Acta Arithmetica PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9231.pdf). Theorem 6, its fourteen terms, and its coefficient class match the report. Theorem 7 really does end with the printed term \(F^{-1/2}MNH\), while \(N,H\) are not defined in that theorem; the report correctly calls that term source-inconclusive and does not use it.
- Robert--Sargos Theorem 1 was checked in the [primary Crelle PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf). The phase, coefficient split, hypothesis \(\alpha(\alpha-1)\beta\gamma\ne0\), and four-term bound match the report.

The following remain AMBER only at the independent-source layer.

- The [original Sargos--Wu publisher page](https://link.springer.com/article/10.1023/A%3A1006777803163) exposed only a preview in this review. The bound list is consistent with later published quotations, but a secondary quotation is not a substitute for the original theorem statement.
- The full [Sargos 2015 theorem text](https://doi.org/10.7169/facm/2015.52.1.11) was not independently accessible. Its quoted theorem card should retain the source auditor's provenance and should not be represented as independently double-checked here.

These source-access qualifications do not alter the audited arithmetic. Nor do they weaken the correctly scoped no-go:

1. no verified source theorem accepts the literal joint coefficient without a new decomposition;
2. even granting ideal coefficient separation, the Cao--Zhai displayed bound contains the positive balanced term \(R^{(3-5\tau)/8}\);
3. Robert--Sargos and the quoted Sargos--Wu bound are still weaker on the same top boxes;
4. Sargos's transform followed by aliaswise modulus has only the adverse upper-capacity ledger above.

These statements rule out the cited black-box routes as target proofs. They do not rule out a new theorem exploiting the actual signs, do not prove any lower bound, and do not show the desired scalar estimate false. The report's label three_variable_dispersion_no_go is acceptable only with this method/source scope.

## 7. Recommended corrections and state effect

Before synthesis, make the following local edits to the reviewed report or carry them explicitly in the conductor's synthesis.

1. In Section 3.3, change “Thus one chooses the larger of \(D,E\) for the distinguished slot” to “For term 1 alone, the larger of \(D,E\) is the favorable distinguished slot; a single placement must be retained for the full fourteen-term sum.”
2. In Sections 1 and 3.5, qualify the second Sargos transform as a phase-level involution after alias-orthant reversal, not an amplitude-level Poisson self-return.
3. Keep \(\#\text{aliases}\ll\mathcal F^3/P\) and the \(\mathcal F^{3/2}\) triangle price as upper ledgers; use \(\asymp\) only for a stated full smooth interior model with a lattice-count justification.
4. Treat \(\mathcal F/M_i^2\ll1\) only as a usefulness regime, not as a hypothesis of the quoted transform theorem.
5. Preserve explicit source uncertainty for Cao--Zhai Theorem 7's undefined final symbols and, unless primary captures are archived, for the exact Sargos--Wu and Sargos theorem statements.

After these local corrections, **retain** the report as GREEN obstruction evidence for direct Cao--Zhai, Robert--Sargos, fixed-row Sargos--Wu, and smooth \(B\)-process routes. Do not promote a target estimate, a lower bound, or a no-go for every possible sign-sensitive theorem. No change is licensed for the independent Round-138 cross owner, either direct M1 parent, any M2 owner, endpoint uniformity, M9, the bridge, or any global exponent.
