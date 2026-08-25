# Round 146 terminal source/power verdict v2

- Campaign: `m9-m1-lower-cone-three-variable-hessian-dispersion-gate`
- Candidate: `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`
- Review role: independent terminal source reviewer
- Starting graph SHA-256: `7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d`
- Verdict: `GREEN_terminal_source_card_complete`

## 1. Result

The candidate is **terminal GREEN on the source and power seam**. The three exact-card omissions identified by the preceding terminal review are now repaired:

1. the Robert--Sargos exponent, length, and phase-scale mapping is explicit;
2. the Sargos--Wu length and phase-scale mapping is explicit;
3. the Sargos multidimensional-transform card now states the strict source scale hypothesis \(\mathcal T,M_1,\ldots,M_p>1\) and correctly distinguishes the theorem's connected bounded open domain \(\Omega\) from the positive compact box chosen for the target phase.

Every earlier source, power, notation, alias-count, endpoint, and scope correction remains present. No source correction remains.

This verdict certifies only the candidate's scoped theorem-interface and displayed-upper-bound no-go. It does not certify the target estimate, an impossibility theorem for the exact signed scalar, or any exponent improvement.

## 2. Exact statements and hypotheses

### Robert--Sargos Theorem 1

The candidate retains the source assumptions of positive integer side lengths, \(\mathcal X>1\), bounded coefficients \(a(h,n),b(m)\), and

\[
 \alpha(\alpha-1)\beta\gamma\neq0.
\]

It now gives the exact target placement

\[
 (h,n,m)=(t,e,d),\qquad
 (\beta,\gamma,\alpha)=\left(1,\frac12,\frac12\right),\qquad
 (H,N_0,M_0)=(T,E,D),\qquad \mathcal X=F.
\]

This matches the audited primary card exactly and retains the correct coefficient-class failure \(a(t,e)b(d)\).

### Sargos--Wu Theorem 9

The candidate retains \(Z>0\), bounded separated coefficients, and

\[
 \alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\neq0.
\]

After freezing \(t\), it now states the complete mapping

\[
 (m,n)=(d,e),\qquad
 (\alpha,\beta)=\left(\frac12,\frac12\right),\qquad
 (M_1,N_1)=(D,E),\qquad Z=F.
\]

This matches the audited primary card and retains the correct failure of separatedness for the fixed-\(t\) coprimality-and-cone coefficient.

### Sargos multidimensional transform

The candidate now states fixed \(p>1\), \(k>p+5\),

\[
 \mathcal T,M_1,\ldots,M_p>1,
\]

a connected bounded open \(\Omega\), the required \(C^k\) phase and compactly supported \(C^k\) amplitude, derivative control, support separation from \(\Omega^c\), Hessian nonvanishing, and gradient injectivity. It then says that, for the target phase, one chooses a compact positive box inside such an \(\Omega\). Thus positivity is correctly presented as a target-domain choice, not as a theorem hypothesis. The arithmetic-amplitude mismatch remains explicit.

## 3. Proof or derivation

The repaired cards were compared term by term with the exact cards in `reports/multidimensional_monomial_source_audit.md` and the required additions in the two preceding source reviews.

The Robert--Sargos first contribution under the fixed mapping remains

\[
 R^{-3/2}(TED)
 \left(\frac{F}{TED^2}\right)^{1/4}
 =R^{1/2-\tau/2},
\]

and the Sargos--Wu sixth contribution, after trivial summation over fixed-\(t\) rows, remains

\[
 R^{-3/2}T(F^2D^7E^6)^{1/10}
 =R^{2/5-3\tau/10}.
\]

Both equal \(R^{1/4}\) at the formal \(\tau=1/2\) endpoint. The candidate therefore keeps the exact numerical conclusions attached to the now-complete mappings.

All earlier corrections also survive the revision:

- the Cao--Zhai Theorem-6 card contains the side-length, phase, coefficient, exponent, and \(F\gg D\) hypotheses, the fixed legal placement, and all fourteen unchanged powers;
- Cao--Zhai Theorem 7 retains the exact coefficient mismatch, the independent \(R^{7/8}\) well-defined term, and marks only its final printed undefined-symbol term source-inconclusive;
- the alias argument retains the explicit bounding-box upper count and reserves a boundary-lattice estimate for an asymptotic count;
- the stationary transform remains a phase-level self-return after alias-orthant reversal, not an amplitude identity;
- \(k_m\), \(k_m=k_{s,t}\), the masked scalar, the inherited full scalar, the disjoint unmasking comparison, the logarithmic block assembly, and the excluded half-open upper endpoint remain explicit;
- the \(t=1\) estimate is required only for routes that own that layer separately, while cross-\(t\) cancellation remains allowed;
- every no-go statement is still calibrated as a limitation of the audited mechanisms or displayed upper bounds, never as a lower bound for the signed scalar.

## 4. First doubtful or unproved step

The first open mathematical step is unchanged: one needs either an owner-complete bounded-norm separation of the literal three-variable coefficient or a genuinely sign-sensitive estimate that handles its squarefree, coprimality, parity, character, divisor, cone, profile, and endpoint correlations. None of the audited sources supplies that input, and the candidate does not claim it.

There is no remaining doubtful source-card step in the candidate.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| Robert--Sargos exponent/length/scale mapping | **GREEN** |
| Robert--Sargos coefficient class and comparison power | **GREEN** |
| Sargos--Wu variable/length/scale mapping | **GREEN** |
| Sargos--Wu coefficient class and comparison power | **GREEN** |
| Sargos \(\mathcal T,M_i>1\) source hypothesis | **GREEN** |
| Connected bounded open \(\Omega\) versus chosen positive target box | **GREEN** |
| Cao--Zhai Theorems 6--7 exact cards and power ledger | **GREEN** |
| Alias bounding-box and boundary-count qualification | **GREEN** |
| Phase-only transform self-return | **GREEN** |
| Formal notation, unmasking, endpoint, and layerwise qualifications | **GREEN** |
| No-go calibration and downstream scope | **GREEN** |
| Exact source-card completeness | **TERMINAL GREEN** |

## 6. Dependencies and exact artifacts used

This review used exactly:

- `protocol.md`;
- `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`;
- `reports/multidimensional_monomial_source_audit.md`;
- `reviews/source_conductor_candidate_final_audit.md`;
- `reviews/source_conductor_candidate_final_green.md`.

The current candidate was reread in full after the three repairs. The exact mappings were compared with the primary-source cards already audited in the source report, and the two comparison powers were recomputed algebraically. No numerical experiment was used.

## 7. Recommended state effect

**Promote on the source seam only.** Subject to the conductor's remaining independent seam reviews and graph validation, the source review supports promotion of:

- the exact unmasking reduction;
- the literal source coefficient-class mismatch;
- the displayed Cao--Zhai, Robert--Sargos, and Sargos--Wu power obstructions;
- the short-face and phase-level transform diagnostics.

Do not promote a lower bound, a universal impossibility theorem, a target estimate, a downstream owner, or any exponent change.
