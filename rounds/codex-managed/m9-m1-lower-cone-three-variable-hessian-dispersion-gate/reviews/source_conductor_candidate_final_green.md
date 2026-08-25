# Round 146 terminal source/power verdict

- Candidate: `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`
- Review status: terminal re-read
- Verdict: `NOT_GREEN_exact_source_card_completion_required`

## 1. Result

The revised candidate closes every previously identified power, unmasking, alias-count, notation, layerwise, and endpoint correction. Its central scoped no-go is correct. It is **not yet GREEN**, solely because three abbreviated source cards still omit parts of the exact mappings or scale hypotheses that the prior final audit required.

No power correction is needed. No change is needed to the unmasking reduction, the Cao--Zhai Theorem-6 or Theorem-7 calculations, the alias bounding-box argument, (146.C33), or the no-go calibration.

## 2. Exact statements and hypotheses

### Cao--Zhai Theorem 6: GREEN

The candidate now states \(M_0,M_1,M_2\geq1\), \(A\neq0\), both coefficient bounds,

\[
 \alpha(\alpha-1)(\alpha-2)(\alpha-3)
 \gamma(\gamma-1)\neq0,
 \qquad F=|A|M_0^\alpha M_1^\beta M_2^\gamma\gg M_0,
\]

and the unique placement up to \(d,e\) exchange. The absence of any further restriction on \(\beta\) is correctly reflected by the displayed hypothesis list. The placement

\[
 (m,m_1,m_2)=(d,t,e),\qquad
 (\alpha,\beta,\gamma)=\left(\frac12,1,\frac12\right)
\]

is legal.

The \(F\)-condition is now verified correctly. With \(M_0=D\),

\[
 F\asymp\sqrt{NM},\qquad
 \frac FD\geq\frac{\sqrt{NM}}M
 =\sqrt{\frac NM}\gg_V1.
\]

The candidate writes \(F=\sqrt{NM}\) as the dyadic phase scale; this is harmless scale notation under \(T^2DE\asymp M\).

### Cao--Zhai Theorem 7: GREEN

The candidate now records positive side lengths, \(A>0\), bounded separated coefficients, and

\[
 \frac{\alpha\beta}{\alpha-1}\notin\{0,1,2,\ldots\}.
\]

It correctly verifies the value \(-1\), identifies the missing distinguished-\(d\) coefficient and required \(a(t)b(e)\) split, and computes the second well-defined term as

\[
 R^{-3/2}(F^4T^7E^7)^{1/8}=R^{7/8}.
\]

Only the source's final undefined-symbol term is marked source-inconclusive. This correction is complete.

### Remaining exact-card omissions

The following are the only corrections still required:

1. The Robert--Sargos bullet gives the source hypotheses and variable placement, but the exact phase mapping remains incomplete. Add
   \[
   (\beta,\gamma,\alpha)=\left(1,\frac12,\frac12\right),\qquad
   (H,N_0,M_0)=(T,E,D),\qquad \mathcal X=F.
   \]
2. The Sargos--Wu bullet gives the exponent hypothesis and \((\alpha,\beta)=(1/2,1/2)\), but add the exact scale mapping
   \[
   (M_1,N_1)=(D,E),\qquad Z=F.
   \]
3. The Sargos multidimensional-transform bullet omits the explicit source scale hypothesis
   \[
   \mathcal T,M_1,\ldots,M_p>1.
   \]
   It should say that the theorem assumes a connected bounded open \(\Omega\); positivity is a choice for the target box, not a theorem hypothesis. The existing smoothness, derivative, support-separation, Hessian, injectivity, and amplitude restrictions are otherwise correct.

All primary-source links in Section 5 are valid primary-paper, author-manuscript, publisher-DOI, or primary-preprint links.

## 3. Proof and power verification

Holding the Cao--Zhai placement fixed across the full theorem, the fourteen exponents in (146.C30) recompute to

\[
\begin{aligned}
 &\frac38-\frac{5\tau}8,\quad
 \frac38-\tau,\quad
 \frac{11}{29}-\frac{43\tau}{58},\quad
 \frac{41}{108}-\frac{41\tau}{54},\\
 &\frac{37}{98}-\frac{37\tau}{49},\quad
 \frac{11}{29}-\frac{23\tau}{29},\quad
 \frac{127}{336}-\frac{125\tau}{168},\quad
 \frac{115}{304}-\frac{115\tau}{152},\\
 &\frac{127}{336}-\frac{131\tau}{168},\quad
 \frac{33}{100}-\frac{181\tau}{200},\quad
 \frac{123}{368}-\frac{167\tau}{184},\\
 &\frac{33}{100}-\frac{19\tau}{20},\quad
 \frac13-\frac{5\tau}{6},\quad
 \frac14-\frac{9\tau}{8}.
\end{aligned}
\]

All fourteen match the candidate. Term 1 is

\[
 R^{-3/2}(FD^5T^7E^7)^{1/8}
 =R^{3/8-5\tau/8},
\]

so it is \(R^{1/16}\) at \(\tau=1/2\) and becomes target-sized only at \(\tau\geq3/5\). The statement remains correctly calibrated as a limitation of the displayed upper bound.

The comparison powers also recompute exactly:

\[
 \text{Robert--Sargos: }R^{1/2-\tau/2},
 \qquad
 \text{Sargos--Wu: }R^{2/5-3\tau/10},
\]

both \(R^{1/4}\) at the formal endpoint.

The revised stationary-transform argument now has a genuine bounding-box upper count,

\[
 \#\{\text{aliases}\}\ll
 (1+F/T)(1+F/D)(1+F/E)\ll F^3/(TDE),
\]

while reserving a boundary estimate only for an asymptotic count. The transform remains explicitly phase-level after alias-orthant reversal and does not claim amplitude self-return. This correction is complete.

## 4. First doubtful or unproved step

No mathematical seam remains in the promoted conclusions themselves. The first open mathematical step is still an owner-complete, bounded-norm separation or a genuinely sign-sensitive estimate for the literal coefficient. The candidate does not claim either.

The only present defect is documentary source completeness: without the three mappings/scale hypotheses in Section 2, the Robert--Sargos, Sargos--Wu, and Sargos cards are not yet exact enough to satisfy the final-audit contract, even though every conclusion drawn from them is correct.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| \(k_m\) definition and \(k_m=k_{s,t}\) | **GREEN** |
| Masked scalar \(\mathfrak S_N^{<,>}\), full \(\mathfrak T_N\), and two-step comparison | **GREEN** |
| Per-block large-\(t\) estimate and \(O(\log X)\) assembly | **GREEN** |
| Strict/complementary mask inequalities and exact radicals | **GREEN** |
| Half-open upper endpoint \(B_M\) treated as excluded | **GREEN** |
| Cao--Zhai Theorem-6 exact hypotheses and \(F\gg D\) | **GREEN** |
| Fixed placement and all fourteen powers | **GREEN** |
| Cao--Zhai Theorem-7 coefficient mismatch and \(R^{7/8}\) term | **GREEN** |
| Robert--Sargos numerical power | **GREEN**, source mapping still incomplete in prose |
| Sargos--Wu numerical power | **GREEN**, scale mapping still incomplete in prose |
| Alias bounding-box qualification | **GREEN** |
| Phase-level self-return after orthant reversal | **GREEN** |
| Layerwise qualification of (146.C33) and allowance for cross-\(t\) cancellation | **GREEN** |
| Source links | **GREEN** |
| Exact source-card completeness | **NOT GREEN** for the three omissions in Section 2 |
| No-go calibration and downstream scope | **GREEN** |

## 6. Dependencies and exact artifacts used

This terminal re-read used:

- the revised `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`;
- `reviews/source_conductor_candidate_final_audit.md`;
- `reports/multidimensional_monomial_source_audit.md`.

The candidate was read directly after revision. Its source links were compared with the already audited primary cards, and every displayed power was recomputed algebraically.

## 7. Recommended state effect

**Revise only the three source-card sentences in Section 5, then rerun this terminal check.** Do not mark the candidate GREEN before those exact mappings and the Sargos scale/domain distinction are present.

No other correction or mathematical change is recommended.
