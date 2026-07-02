## Selected main route

Source basis: I treat the uploaded Round 6 judge packet from 2026-07-02 as the controlling Stage C instruction bundle. The packet identifies the active Round 6 targets as `M9-M2-character-factor`, `M9-near-collision-taxonomy`, and `M9-regression-raw-vs-paired`, and it reiterates the do-not-claim rules for `M9`, `M9-M2`, and the final Gauss circle target.

### Primary route: URES residual plus global moment re-scoping

The selected primary route for the next round is:

$$
\text{exact-resonance residual structure}
+
\text{graded global near-collision estimates}
+
\text{endpoint signed-discrepancy backup}.
$$

The immediate proof-graph target is not `M9-M2` itself. It is the residual exact-resonance problem left after A4's Round 6 reductions:

$$
\sum_{r\ne0} R(r)^2 \ll D^2X^\epsilon,
$$

where $R(r)$ is the representation-weighted count for pairs of reduced fractions summing to $r$, restricted to exact $N=0$ tuples whose reduced-denominator multiset is not of the form $\{q,q,q',q'\}$. This class is nonempty, with the witness family

$$
\frac1{6k}+\frac1{10k}
=
\frac1{15k}+\frac1{5k}.
$$

The reason to select this route is narrow proof-graph safety. A4 has supplied a DP suite, NF-1/NF-2 rigidity, and reduced-paired exact-resonance bounds that plausibly reduce exact $N=0$ to a named residual class. The URES target is sharply stated, falsifiable, and directly connected to the current blocker `M9-near-collision-taxonomy`.

This route does not claim `M9-M2`. Even a complete exact $N=0$ classification would still leave near-collision bands, signed cancellation, and pointwise endpoint control.

### Backup route: sign-preserving discrepancy / SPD

The backup route is A4's sign-preserving reciprocal discrepancy route. The desired endpoint statement is a direct bound

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

A first falsifiable spacing statistic is

$$
P(D,H;X)
=
\#\left\{
d_1\ne d_2:
\left\|
\frac{X}{4d_1}-\frac{X}{4d_2}
\right\|\le \frac1H
\right\}.
$$

The backup route should be pursued only if A3's signed-vs-unsigned diagnostics show visible true-sign cancellation for the actual $\beta_h$ signs at endpoint and near-endpoint blocks.

### Route explicitly downgraded: local `(LFM)` as a relaxed bridge

Round 6 shows that coherence-window local fourth moments are not a relaxed average target. On windows

$$
\delta=X^{1/2}/D,
$$

the fourth-moment frequency obeys

$$
|\lambda|\ll H_D/D\asymp X^{-1/4},
\qquad
\delta|\lambda|\ll X^{1/4}/D\le O(1).
$$

Thus the window multiplier gives no power-scale decay across the active range. A4's stronger subcoherence formulation supersedes A1's endpoint-only degeneracy calculation: local averaging on the coherence window does not produce meaningful $t$-oscillatory gain, and `(LFM)` at the target threshold is essentially pointwise at proof strength.

`(LFM)` should remain in the graph as a conditional target, but no longer as the primary route.

## Useful fragments by source

### A1

A1 supplied useful infrastructure rather than endpoint proof.

First, A1's $\Phi$ calculation is accepted as a calculus lemma conditional on the Vaaler formula:

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

The expansions at $u=0$ and $u=1$ give

$$
\Phi(0)=1,\qquad \Phi(1)=0,\qquad \Phi'(0)=\Phi'(1)=0.
$$

This supports coefficient-stability bookkeeping, but it does not promote `H4` while the Vaaler source card is still physically incomplete.

Second, A1 restated the raw/two-sided and paired $\mathcal M_2$ formulas correctly under H4. Assuming

$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

one gets

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

and hence

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

The raw two-sided formula and the complex-weight cosine pairing should be inserted into the proof draft before any further computation is trusted.

Third, A1's local fourth-moment kernel calculation is accepted:

$$
\left|
\delta^{-1}\int_I e\left(\frac{tN}{4d_1d_2d_3d_4}\right)\,dt
\right|
\ll
\min\left(1,\frac{D^4}{\delta |N|}\right).
$$

With $\delta=X^{1/2}/D$, the local band is

$$
|N|\ll D^5X^{-1/2}.
$$

At $D\asymp X^{1/2}$, all fourth-moment tuples satisfy $|N|\ll X^{7/4}\ll X^2$, so the local kernel gives no endpoint spacing discrimination. This is a scoped obstruction, not a disproof of `(LFM)`.

### A2

A2's strongest accepted contribution is terminology separation. Fraction-matching

$$
\frac{h_1}{d_1}=\frac{h_2}{d_2},
\qquad
\frac{h_3}{d_3}=\frac{h_4}{d_4}
$$

is not the official denominator-pattern semi-diagonal family

$$
d_1=d_3,\qquad d_2=d_4,\qquad
d_2(h_1+h_3)=d_1(h_2+h_4).
$$

This distinction should be added to `M9-near-collision-taxonomy`.

A2's integer detector observation is also useful but only diagnostic: $\int_0^1 e(\alpha N)\,d\alpha$ detects integer $N=0$, but it does not factor into a simple one-variable $L^4$ norm of the original reciprocal sum.

A2's unpaired exact $N=0$ mass bound is not accepted. The claimed $\ll X^\epsilon$ scale undercounts or fails to account for lifting variables, dyadic constraints, overlap classes, and residual families. It may be revisited only after a lift-corrected proof using NF-2.

A2's Poisson/B-process or sign-preserving Poisson-Voronoi route is retained as `proposed`, not as evidence. It needs exact stationary phase, boundary terms, dual ranges, and a post-transform signed estimate.

### A3

A3 supplied a broad diagnostic design, but no executed artifact. The diagnostic plan is useful: exact integer arithmetic for $N$, raw-vs-paired regression, complex-weight failure tests, local-window diagnostics, DP parity checks, URES enumeration, and signed-vs-unsigned comparisons.

No A3 computation should be positive state evidence this round. A3's bundle was not executed, used placeholder $\Phi$ in places, and had formula/classification risks. Before execution, A3 must correct the $d=7$ imaginary-part sign, the complex-weight relation $B_{-1}=(1+i)\overline{\Sigma}$, and the envelope $\sup_I |S_2'|\ll H_D$. It remains `diagnostic_only`.

### A4

A4 produced the strongest Round 6 proof-graph material.

A4's denominator-paired suite is accepted under the H4 beta-support and beta-magnitude hypotheses. In the DP class

$$
d_1=d_2=a,\qquad d_3=d_4=b,
$$

one has

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a.
$$

Single-parity support of $\beta_h$ forces $L$ even. Therefore either $N=0$ or

$$
|N|\ge 2ab\gg D^2.
$$

The thin DP band

$$
0<|N|\le C_0D^4/X
$$

is empty except near the upper endpoint, and the nonempty thin DP mass is bounded by

$$
\Sigma_{\mathrm{DP}}^{\mathrm{thin}}
\ll C_0D\log^2(2H)
$$

up to fixed coefficient constants. The full DP total is

$$
\Sigma_{\mathrm{DP}}^{\mathrm{full}}
\ll D^2\log^4 X.
$$

These should update `M9-M2-DP-near-collision-bound`, still as `derived_under_assumptions`.

A4's NF-2 participation rigidity is accepted as a proved internal integer lemma. If $r=\mu/Q$ is reduced, $\mu\ne0$, and $x_1=p_1/q_1$ is reduced with $x_3=r-x_1\ne0$ of reduced denominator $q_3$, set

$$
g=\gcd(Q,q_1),\qquad
\widehat Q=Q/g,\qquad
\widehat q_1=q_1/g,\qquad
M=\mu\widehat q_1-p_1\widehat Q.
$$

Then

$$
q_3=\frac{g\widehat Q\widehat q_1}{\gcd(g,M)}
\ge
\widehat Q\widehat q_1
=
\frac{Qq_1}{g^2}.
$$

If $q_3\le2D$, this forces

$$
\gcd(Q,q_1)\ge \left(\frac{Qq_1}{2D}\right)^{1/2}.
$$

This is the main rigidity input for URES.

A4's reduced-paired exact-resonance bounds are accepted under H4: exact $N=0$ tuples whose reduced-denominator multiset has the form $\{q,q,q',q'\}$ have absolute beta-weighted mass

$$
\ll D^2X^\epsilon.
$$

The remaining exact-resonance problem is URES. A4's explicit witness family shows URES cannot be emptied, only bounded.

A4's subcoherence-window equivalence is the main strategic correction. It converts `(LFM)` from a candidate relaxed bridge into a pointwise-strength obstruction.

## Rejected or risky ideas

1. **Reject any promotion of `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.** No uniform endpoint estimate is proved.

2. **Reject local `(LFM)` as the main route.** It remains a conditional formulation, but coherence windows provide no power-saving multiplier. A proof of `(LFM)` must supply the same $h,d$-space cancellation as pointwise `M9-M2`.

3. **Reject A2's unpaired exact $N=0$ mass bound.** The bound is not proved and should not be recorded as `derived_under_assumptions`.

4. **Reject A2's cleared-phase nonseparability as a route-closing theorem.** It is a diagnostic record for the failed continuous $L^4$ route, not a theorem blocking all integer-kernel methods.

5. **Reject A2's Poisson-Voronoi sketch as state evidence.** It remains `proposed`.

6. **Reject A3's unexecuted artifact bundle as positive evidence.** It is useful planning only.

7. **Reject A3's proposed pass/fail rule for unclassified mass.** Unclassified or URES mass is a mathematical object to bound, not a code failure.

8. **Reject black-box Li--Yang import.** Li--Yang remains a source-audit guardrail; no theorem should be imported without an exact source card and hypothesis match.

9. **Reject any computation-to-proof promotion.** Computations may falsify, test, and calibrate. They do not prove asymptotic lemmas.

## Known gaps

1. **H4 source-card gap.** `sources/vaaler_1985.md` still needs exact theorem transcription, equation numbers, coefficient sign, Fejer normalization, residual constant, and endpoint convention.

2. **Proof-draft gap.** `state/best_proof_draft.md` must be populated with H1--H4, R5, M1/M2 definitions, raw/two-sided formulas, AP, local kernel, subcoherence obstruction, DP suite, NF-1/NF-2, reduced-paired bounds, and URES.

3. **URES gap.** The residual exact $N=0$ class is now named and nonempty. Its mass is open.

4. **Overlap bookkeeping gap.** The U-2, SS, anti-paired, and fraction-matching coverage for $\{q,q,q',q'\}$ patterns should be verified set-theoretically before using it downstream.

5. **Near-collision gap.** The exact $N=0$ work does not prove graded bounds for

$$
0<|N|\le M.
$$

6. **Endpoint signed-cancellation gap.** The endpoint $D\asymp X^{1/2}$ still needs a direct signed or specialized endpoint argument.

7. **M1 gap.** Round 6 does not estimate `M9-M1`.

8. **A3 execution gap.** The diagnostic bundle must be materialized and run.

9. **Constant-control gap in equivalence.** The subcoherence equivalence uses frozen height and derivative bounds with constants. The proof draft must track constants well enough to ensure the $O(X^{1/4})$ drift is target-scale, not larger by an uncontrolled parameter.

10. **External theorem gap.** Vaaler and Li--Yang remain source-audit constrained.

## New lemmas to add

### Lemma 1: `H4-Phi-regularity`

Status: `derived_under_assumptions`.

Assuming Vaaler's formula

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1,
$$

the function $\Phi$ extends to $C^1([0,1])$ with

$$
\Phi(0)=1,\quad \Phi(1)=0,\quad \Phi'(0)=\Phi'(1)=0.
$$

This is source-card support, not a promotion of H4.

### Lemma 2: `M9-M2-local-fourth-moment-kernel`

Status: `proved_internal`.

For the local fourth-moment expansion over an interval $I$ of length $\delta$,

$$
\left|
\delta^{-1}
\int_I e\left(\frac{tN}{4d_1d_2d_3d_4}\right)dt
\right|
\ll
\min\left(1,\frac{D^4}{\delta |N|}\right).
$$

With $\delta=X^{1/2}/D$, the fat band is

$$
|N|\ll D^5X^{-1/2}.
$$

### Lemma 3: `M9-M2-LFM-endpoint-degeneracy`

Status: `proved_internal`.

At $D\asymp X^{1/2}$,

$$
|N|\ll H_DD^3\asymp X^{7/4},
$$

while

$$
D^5X^{-1/2}\asymp X^2.
$$

Thus every tuple lies inside the local non-oscillatory band. This is the endpoint specialization of the whole-range subcoherence-window obstruction, not a separate averaging route. It blocks absolute local $N$-spacing as a complete endpoint proof, not all possible endpoint proofs.

### Lemma 4: `M9-M2-subcoherence-window-multiplier`

Status: `proved_internal`.

For every fourth-moment tuple on a coherence window,

$$
|\lambda|
=
\left|
\frac14\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
\right|
\ll H_D/D
\asymp X^{-1/4},
$$

and hence

$$
\delta|\lambda|
\ll X^{1/4}/D
\le O(1).
$$

### Lemma 5: `M9-M2-LFM-pointwise-equivalence`

Status: `derived_under_assumptions`.

Under the H4 beta-magnitude hypothesis, bounded dyadic weights, and frozen local height, `(LFM)` at threshold $X^{1+\epsilon}$ on coherence windows is pointwise-strength: the window multiplier gives no power saving, and the derivative drift over the window is $O(X^{1/4})$. Any proof must supply full $h,d$-space cancellation.

### Lemma 6: `M9-M2-NF-participation-rigidity`

Status: `proved_internal`.

Use the exact statement given above for $r=\mu/Q$, $x_1=p_1/q_1$, and $x_3=r-x_1$. This is a pure integer lemma and should be inserted into the lemma bank.

### Lemma 7: `M9-M2-unpaired-reduced-paired-bound`

Status: `derived_under_assumptions`.

Under H4 beta magnitude, exact $N=0$ tuples whose reduced-denominator multiset has form $\{q,q,q',q'\}$ have absolute beta-weighted mass

$$
\ll_\epsilon D^2X^\epsilon.
$$

This covers the reduced-paired patterns only. It does not cover URES.

### Lemma 8: `M9-M2-unpaired-residual-URES`

Status: `open`.

For the remaining exact-resonance class, prove

$$
\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon.
$$

The class is nonempty, so the goal is a bound, not emptiness.

### Lemma 9: `M9-M2-sign-preserving-poisson-voronoi-route`

Status: `proposed`.

A sign-preserving Poisson/B-process transformation in $d$ may lead to a dual signed sum. It is useful only after exact stationary phase, boundary terms, $k=0$ terms, dual ranges, and a signed post-transform estimate are supplied.

## Counterexample checks to run

1. **DP parity assertion.** Enumerate DP tuples and assert that active beta support has no tuple with

$$
0<|N|<2D^2.
$$

2. **DP thin mass.** Compare enumerated thin-DP mass to

$$
C_0D\log^2(2H)
$$

for bottom, middle, and endpoint dyadic blocks.

3. **URES enumeration.** Enumerate exact $N=0$ tuples whose reduced-denominator multiset is not $\{q,q,q',q'\}$, including the $(6,10,15,5)k$ witness family.

4. **URES $R(r)^2$ concentration.** Report the distribution of $R(r)$ and the sum $\sum_{r\ne0}R(r)^2$.

5. **Subcoherence diagnostic.** For active $D$, compute

$$
\max_{\mathbf h,\mathbf d}\delta|\lambda|
$$

and compare local fourth-moment averages to local suprema.

6. **Raw-vs-paired regression.** Verify raw two-sided M2 equals complex-weight cosine pairing for complex weights, and equals the $\operatorname{Re}B_h$ formula only for real weights.

7. **Fourth-moment sign convention.** Check raw expansion of $|S_2|^4$ against

$$
N=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

8. **SPD statistic.** Compute $P(D,H;X)$ and compare true beta signs with unsigned, random signs, and adversarial signs at

$$
D=X^{0.3},\quad X^{0.4},\quad X^{0.5}.
$$

9. **Endpoint Poisson test.** If pursued, verify the stationary phase for

$$
\int w_D(y)e(hX/(4y)-ky)\,dy
$$

with exact sign of $k$, stationary point, main amplitude, boundary terms, and dual range

$$
m\asymp hX/D^2.
$$

10. **H4 parity regression.** Verify that the M2 $\rho=1,3$ combination produces single-parity $h$-support. A mixed-parity support would break DP-0/DP-1 as stated.

## Research strategy adjustment

Round 7 should pivot away from local `(LFM)` as the leading analytic route.

Recommended allocation:

- **A1:** proof-draft and source-card consolidation. Incorporate Round 6 lemmas into `best_proof_draft.md` and `state/lemma_bank.md`. Keep H4 source-audit required.
- **A2:** attack URES or give a rigorous lower-bound obstruction. Use NF-2; do not revisit DP exact resonance or write another broad taxonomy essay.
- **A3:** execute the diagnostic bundle. The first deliverable must be actual files, commands, tables, precision logs, and a report.
- **A4:** produce validator-ready versions of DP-0..DP-3, NF-1/NF-2, subcoherence, and U-2/SS/anti-paired, then develop SPD as the backup route.

The backup route should be SPD/sign-preserving discrepancy, not black-box Li--Yang. Poisson/B-process is allowed as a proposed exploratory route only if exact stationary-phase and boundary-control obligations are stated.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "H4-Phi-regularity",
        "type": "lemma",
        "track": "source_audit",
        "title": "Regularity of Vaaler's Phi coefficient function",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming Vaaler's Theorem 6 coefficient formula Phi(u)=pi u(1-u)cot(pi u)+u for 0<u<1, Phi extends to C^1([0,1]) with Phi(0)=1, Phi(1)=0, Phi'(0)=Phi'(1)=0, and sup_[0,1]|Phi'(u)|<infty. This supports coefficient-stability bookkeeping and freezing H_D on local windows; it does not by itself validate H4.",
        "dependencies": [
          "H4-source-audit"
        ],
        "implies": [],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A1-006.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "next_action": "After the Vaaler source card is validated, move this calculus lemma into the lemma bank and cite it in H4 coefficient-stability notes."
      },
      {
        "id": "M9-M2-local-fourth-moment-kernel",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Local fourth-moment kernel and fat N-band",
        "status": "proved_internal",
        "statement_tex": "For the S_2 fourth-moment expansion over an interval I of length delta, a tuple with cleared numerator N and denominator product Q=d_1d_2d_3d_4 satisfies |I|^(-1)|int_I e(tN/(4Q))dt| << min(1,D^4/(delta |N|)). For delta=X^(1/2)/D the local fat band is |N| << D^5 X^(-1/2).",
        "dependencies": [
          "M9-M2-fourth-moment-expansion"
        ],
        "implies": [
          "M9-M2-local-fourth-moment-LFM",
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A1-006.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "next_action": "Insert the kernel calculation into the lemma bank and use it only as algebraic infrastructure, not as an M2 estimate."
      },
      {
        "id": "M9-M2-LFM-endpoint-degeneracy",
        "type": "obstruction",
        "track": "M9_analytic",
        "title": "Endpoint corollary of whole-range subcoherence obstruction",
        "status": "proved_internal",
        "statement_tex": "At D asymp X^(1/2), H_D asymp X^(1/4), and delta=X^(1/2)/D asymp 1, every fourth-moment tuple has |N| << H_D D^3 asymp X^(7/4), while the local fat-band threshold D^5 X^(-1/2) is asymp X^2. Thus the local fourth-moment kernel gives no N-spacing discrimination at the endpoint. This is the endpoint specialization of the whole-range subcoherence-window obstruction, not a separate averaging route; it obstructs absolute local N-spacing proofs at the endpoint, not all possible endpoint proofs.",
        "dependencies": [
          "M9-M2-local-fourth-moment-kernel",
          "M9-M2-subcoherence-window-multiplier",
          "M9-endpoint-uniformity"
        ],
        "implies": [
          "M9-M2-local-fourth-moment-LFM",
          "M9-M2-fourth-moment-average-to-pointwise",
          "M9-endpoint-uniformity"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A1-006.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "next_action": "Fold this endpoint statement into the whole-range subcoherence-window multiplier when writing the lemma bank; do not maintain it as an independent relaxed-LFM route. Any endpoint proof must supply signed cancellation or another mechanism not based only on absolute N-spacing."
      },
      {
        "id": "M9-M2-subcoherence-window-multiplier",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Subcoherence multiplier bound on local windows",
        "status": "proved_internal",
        "statement_tex": "For every S_2 fourth-moment tuple with |h_i|<=H_D and d_i asymp D, lambda=(1/4)(h_1/d_1-h_2/d_2+h_3/d_3-h_4/d_4) satisfies |lambda| << H_D/D asymp X^(-1/4). On coherence windows delta=X^(1/2)/D, delta |lambda| << X^(1/4)/D <= O(1) throughout the active range X^(1/4)<=D<=X^(1/2). Thus the window multiplier has no power-scale decay.",
        "dependencies": [
          "M9-M2-fourth-moment-expansion"
        ],
        "implies": [
          "M9-M2-LFM-pointwise-equivalence",
          "M9-M2-local-fourth-moment-LFM",
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Insert this multiplier lemma into the lemma bank and use it to re-scope LFM away from a relaxed local-averaging route."
      },
      {
        "id": "M9-M2-LFM-pointwise-equivalence",
        "type": "obstruction",
        "track": "M9_analytic",
        "title": "Coherence-window LFM is pointwise-strength at target scale",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming the H4 beta magnitude |beta_h|<<1/|h|, bounded dyadic weights, and frozen H_D, the derivative drift of S_2 over a coherence window delta=X^(1/2)/D is O(X^(1/4)) while the window multiplier has no power decay. Therefore the LFM estimate delta^(-1) int_I |S_2(D;t)|^4 dt << X^(1+epsilon) is equivalent at target precision to pointwise control on I; any LFM proof must supply full h,d-space cancellation.",
        "dependencies": [
          "H4",
          "M9-M2-beta-algebra",
          "M9-M2-subcoherence-window-multiplier",
          "M9-M2-average-to-pointwise-AP-lemma"
        ],
        "implies": [
          "M9-M2-local-fourth-moment-LFM",
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md",
            "rounds/obligation-main/round_006/reviews/A2.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Use this as a scoped obstruction. Do not treat LFM as a relaxed route unless a stronger averaging mechanism or global moment plus large-value propagation is supplied."
      },
      {
        "id": "M9-M2-NF-participation-rigidity",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Participation rigidity for reduced reciprocal resonances",
        "status": "proved_internal",
        "statement_tex": "Let r=mu/Q be reduced with mu nonzero, and let x_1=p_1/q_1 be reduced with x_3=r-x_1 nonzero of reduced denominator q_3. Put g=gcd(Q,q_1), Qhat=Q/g, qhat_1=q_1/g, and M=mu qhat_1-p_1 Qhat. Then gcd(Qhat qhat_1,M)=1 and q_3=g Qhat qhat_1/gcd(g,M) >= Q q_1/g^2. Consequently, if q_3<=2D, then gcd(Q,q_1)>=sqrt(Q q_1/(2D)) and gcd(g,M)>=Q q_1/(2D g).",
        "dependencies": [
          "M9-M2-coprime-rigidity-normal-form"
        ],
        "implies": [
          "M9-M2-unpaired-residual-URES",
          "M9-near-collision-taxonomy"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A2.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_006/reviews/A1.md"
          ]
        },
        "owner": "A4",
        "next_action": "Write NF-2 in lemma-bank notation and use it as the first tool for URES; do not cite randomized checks as proof."
      },
      {
        "id": "M9-M2-unpaired-reduced-paired-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Reduced-paired exact-resonance bound outside fraction matching",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming the H4 beta magnitude and bounded dyadic weights, exact N=0 tuples whose reduced-denominator multiset has form {q,q,q',q'} have total absolute beta-weighted mass <<_epsilon D^2 X^epsilon. This combines the value-unpaired U-2/SS/anti-paired classes with the existing fraction-matching bound and does not cover the URES residual class.",
        "dependencies": [
          "H4",
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion",
          "M9-M2-harmonic-convolution-LH",
          "M9-M2-fraction-matching-weighted-bound",
          "M9-M2-coprime-rigidity-normal-form"
        ],
        "implies": [
          "M9-M2-N0-diagonal-core-bound",
          "M9-near-collision-taxonomy"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A2.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_006/reviews/A1.md"
          ]
        },
        "owner": "A4",
        "next_action": "Transcribe U-2, SS, anti-paired, and fraction-matching coverage in set-theoretic form; verify overlap bookkeeping before using this lemma in any full taxonomy claim."
      },
      {
        "id": "M9-M2-unpaired-residual-URES",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "URES residual exact-resonance bound",
        "status": "open",
        "statement_tex": "For the residual exact N=0 class whose reduced-denominator multiset is not of the form {q,q,q',q'}, prove sum_{r nonzero} R(r)^2 <<_epsilon D^2 X^epsilon for the representation-weighted pair-sum function R(r). The residual is nonempty, for example by 1/(6k)+1/(10k)=1/(15k)+1/(5k).",
        "dependencies": [
          "M9-M2-coprime-rigidity-normal-form",
          "M9-M2-NF-participation-rigidity",
          "M9-M2-unpaired-reduced-paired-bound"
        ],
        "implies": [
          "M9-M2-N0-diagonal-core-bound",
          "M9-near-collision-taxonomy"
        ],
        "blockers": [],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md",
            "rounds/obligation-main/round_006/reviews/A2.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ]
        },
        "owner": "A2",
        "next_action": "Use NF-2 to prove the R(r)^2 bound or produce a lower-bound family exceeding the D^2 X^epsilon budget. A3 should enumerate this residual first."
      },
      {
        "id": "M9-M2-sign-preserving-poisson-voronoi-route",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Sign-preserving Poisson or B-process route for M2",
        "status": "proposed",
        "statement_tex": "A proposed sign-preserving transformation of S_2(D;X) in the d-variable, retaining the chi_4(h) beta structure through stationary phase or a Poisson-Voronoi type formula, followed by a signed dual estimate strong enough to imply S_2(D;X)<<_epsilon X^(1/4+epsilon) uniformly over active D. No estimate is currently proved.",
        "dependencies": [
          "M9-M2-beta-algebra",
          "M9-M2-character-factor",
          "M9-endpoint-uniformity"
        ],
        "implies": [
          "M9-M2-direct-signed-bilinear-lemma",
          "M9-M2"
        ],
        "blockers": [
          "H4-source-audit",
          "Li-Yang-source-audit"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A2-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md"
          ]
        },
        "owner": "A2",
        "next_action": "State exact stationary phase, boundary terms, k=0 terms, dual m-range m asymp hX/D^2, amplitudes, and the first sign-preserving post-transform estimate; keep as proposed until then."
      }
    ],
    "update": [
      {
        "id": "H4-source-audit",
        "status": "source_audit_required",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A1-006.md"
          ]
        },
        "next_action": "Commit sources/vaaler_1985.md with bibliographic data, DOI 10.1090/S0273-0979-1985-15349-2, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, and the M2 single-parity support check."
      },
      {
        "id": "M9-M2-DP-near-collision-bound",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md",
            "rounds/obligation-main/round_006/reviews/A2.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ]
        },
        "next_action": "Transcribe DP-0 through DP-3 into best_proof_draft.md with dyadic constants, C0 dependence, exact H4 parity/magnitude dependencies, and edge cases. Keep H4-source-audit as blocker."
      },
      {
        "id": "M9-M2-coprime-rigidity-normal-form",
        "status": "proved_internal",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A4-006.md"
          ]
        },
        "next_action": "Attach A4's NF-1 compact statement to the lemma bank and use NF-2 for URES."
      },
      {
        "id": "M9-M2-local-fourth-moment-LFM",
        "status": "open",
        "blockers_added": [
          "M9-M2-local-fourth-moment-kernel",
          "M9-M2-subcoherence-window-multiplier",
          "M9-M2-LFM-pointwise-equivalence"
        ],
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_006/responses/A1-006.md",
            "rounds/obligation-main/round_006/responses/A4-006.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_006/reviews/A1.md",
            "rounds/obligation-main/round_006/reviews/A2.md",
            "rounds/obligation-main/round_006/reviews/A3.md"
          ]
        },
        "next_action": "Do not treat coherence-window LFM as a relaxed average route. Any proof must provide full h,d-space cancellation, replace LFM by global moment plus large-value propagation, or split off endpoint blocks with a direct signed estimate."
      },
      {
        "id": "M9-M2-fourth-moment-average-to-pointwise",
        "status": "open",
        "blockers_added": [
          "M9-M2-subcoherence-window-multiplier",
          "M9-M2-LFM-pointwise-equivalence"
        ],
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_006/responses/A4-006.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A1-006.md"
          ]
        },
        "next_action": "Keep AP as a calculus interpolation module. Re-scope average-to-pointwise around subcoherence: local windows give no power saving, so pursue either global moment plus large-value propagation away from endpoint or direct signed endpoint control."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "blockers_added": [
          "M9-M2-unpaired-residual-URES",
          "M9-M2-unpaired-reduced-paired-bound",
          "M9-M2-NF-participation-rigidity"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A2-006.md",
            "rounds/obligation-main/round_006/responses/A4-006.md"
          ],
          "negative": [
            "rounds/obligation-main/round_006/reviews/A1.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A3-006.md"
          ]
        },
        "next_action": "Record fraction-matching versus official semi-diagonal terminology. Treat reduced-paired exact resonances under H4, then attack URES; do not promote full taxonomy until mixed and residual exact N=0 are bounded."
      },
      {
        "id": "M9-near-collision-estimate",
        "status": "proposed",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md"
          ]
        },
        "next_action": "Recast as a graded global estimate: prove or refute Sigma_abs(0<|N|<=M) <<_epsilon D^2 max(1, M X/D^4) X^epsilon for all relevant M, with signed variants separately marked. Do not infer this from DP or exact N=0 subfamilies."
      },
      {
        "id": "M9-fourth-moment-enumeration",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A3-006.md"
          ]
        },
        "next_action": "Before execution fix the d=7 imaginary-part sign, the complex-weight relation B_{-1}=(1+i)conj(Sigma), and the envelope sup_I |S_2'| << H_D. Then materialize and run exact integer diagnostics for DP parity, DP thin mass, URES residual including (6,10,15,5)k, reduced-paired overlap, local-window equivalence, and signed-vs-unsigned beta comparisons. Archive script, command, tables, precision log, report, and assertions."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A3-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md"
          ]
        },
        "next_action": "Fix the complex-weight B_{-1} relation before running. Then execute the raw two-sided M2, complex-weight cosine pairing, real-weight Re B_h formula, and deliberate complex-weight Re B_h failure tests with exact Phi or explicitly marked surrogate Phi until H4 validates Phi."
      },
      {
        "id": "M9-M2-reciprocal-SPD-route",
        "status": "proposed",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A4-006.md",
            "rounds/obligation-main/round_006/reviews/A1.md"
          ]
        },
        "next_action": "State the exact sign-preserving spacing theorem required for theta_d=X/(4d), define P(D,H;X), and require A3 to compare true beta signs with unsigned, random, and adversarial signs before further proof investment."
      },
      {
        "id": "M9-M2-beta-algebra",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_006/responses/A1-006.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_006/responses/A3-006.md"
          ]
        },
        "next_action": "After H4 source-card validation, insert beta_h formula, raw two-sided M2 formula, complex-weight cosine pairing, real-weight Re B_h formula, and single-parity support into best_proof_draft.md."
      }
    ],
    "reject": [
      {
        "id": "A2-R6-unpaired-exact-N0-mass-bound-derived",
        "reason": "Rejected because the claimed unpaired exact N=0 mass bound is not lift-corrected and does not control URES, overlap classes, dyadic lifts, or beta-weighted multiplicities."
      },
      {
        "id": "A2-R6-cleared-phase-non-separability-route-closing",
        "reason": "Rejected as a proved route-closing obstruction. The integer detector e(alpha N) records why the old continuous rational L4 route fails to factor, but it does not rule out all integer-kernel or delta-method approaches."
      },
      {
        "id": "A2-R6-poisson-voronoi-as-proof-evidence",
        "reason": "Rejected as state evidence because no uniform stationary-phase formula, boundary analysis, dual-range control, or signed post-transform estimate is supplied."
      },
      {
        "id": "A3-R6-unexecuted-artifact-positive-evidence",
        "reason": "Rejected because the diagnostic bundle was not executed and computation may only be diagnostic even when executed."
      },
      {
        "id": "A3-R6-unclassified-mass-pass-fail",
        "reason": "Rejected because unclassified or URES mass is a mathematical target to bound, not a code failure condition."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform endpoint estimates for both M1 and M2 are proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 6 does not estimate M1."
      },
      {
        "id": "M9-M2",
        "reason": "Round 6 adds obstruction and subfamily structure but no pointwise S2 estimate, local estimate with endpoint control, or signed endpoint theorem."
      },
      {
        "id": "GC-target",
        "reason": "The final Gauss circle target remains conditional on M9."
      },
      {
        "id": "Conditional-bridge",
        "reason": "The bridge remains H1-H3 + H4 + R5-Full + M9, and M9 plus H4-source-audit remain blockers."
      },
      {
        "id": "H4",
        "reason": "H4 remains source_audit_required until the Vaaler source card is physically updated and validated."
      },
      {
        "id": "R5-Full",
        "reason": "R5 remains derived_under_assumptions conditional on H4; Round 6 adds no independent promotion."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a source-audit and guardrail obligation; no theorem is imported as a black-box dependency."
      },
      {
        "id": "M9-M2-character-factor",
        "reason": "The character factor remains open as an obstruction/requirement; Round 6 reinforces but does not close M2."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 4,
    "idea_quality_score": 8,
    "state_evidence_score": 6,
    "calibration_score": 8,
    "reason": "Round 6 makes modest proof-graph-safe progress by adding the local kernel, the whole-range subcoherence obstruction with endpoint degeneration as a corollary, a validator-ready DP update, NF-2 rigidity, reduced-paired exact-resonance control under H4, and a precise URES residual target. It does not prove M9, M9-M2, M9-M1, the full taxonomy, near-collision estimates, or the final target."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `H4-source-audit`, `H4-Phi-regularity`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-local-fourth-moment-kernel`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`, proof-draft maintenance.

Objectives:

1. Physically draft or commit `sources/vaaler_1985.md`. Include:
   - bibliographic data and DOI;
   - local PDF path;
   - Theorem 6 equation (2.28);
   - Section 7 equations (7.1)--(7.3);
   - Theorem 18 equations (7.13)--(7.17);
   - coefficient sign;
   - Fejer normalization;
   - residual constant;
   - floor-compatible endpoint convention;
   - $\Phi$ regularity;
   - the M2 single-parity support check from the $\rho=1,3$ difference.

2. Insert into `state/best_proof_draft.md`:
   - H1--H3;
   - H4 as source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - M1/M2 definitions;
   - beta algebra;
   - raw two-sided, complex-weight cosine, and real-weight paired M2 formulas;
   - fourth-moment numerator $N$;
   - local kernel;
   - endpoint degeneracy;
   - subcoherence-window multiplier and LFM-pointwise equivalence;
   - DP-0 through DP-3;
   - NF-1/NF-2;
   - reduced-paired bound;
   - URES residual target.

3. Write a proof-draft note explaining that `(LFM)` is no longer the primary relaxed route: coherence windows provide no power-saving multiplier, and endpoint control must come from signed pointwise or global-moment/large-value propagation.

4. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `GC-target`, and `H4` unpromoted.

Exploratory allocation: compare three route maps in one page:
- URES exact-resonance route;
- graded global near-collision/moment route;
- SPD or sign-preserving Poisson endpoint route.

For each, state the exact theorem needed and one falsification test.

### For A2

Target obligations: `M9-M2-unpaired-residual-URES`, `M9-near-collision-taxonomy`, `M9-M2-sign-preserving-poisson-voronoi-route`.

Objectives:

1. Attack URES only. Do not re-prove denominator-paired, pair-swapped, or fraction-matching subfamilies.

2. Use NF-2 explicitly. For each reduced value $r=\mu/Q$, bound the possible reduced fractions $x_1=p_1/q_1$ with $x_3=r-x_1$ and $q_3\le2D$ using

$$
q_3\ge \frac{Qq_1}{\gcd(Q,q_1)^2}.
$$

3. Produce one of:
   - a proof of $\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon$;
   - a lower-bound family exceeding the budget;
   - a rigorous reduction to a smaller divisor-sum problem with all lifts and beta weights stated.

4. If using the Poisson/B-process route, supply the exact transformed object:
   - sign of the dual variable;
   - stationary point;
   - amplitude;
   - boundary terms;
   - $k=0$ terms;
   - dual range $m\asymp hX/D^2$;
   - the first signed theorem that would imply `M9-M2`.

5. Do not label any unpaired mass bound `derived_under_assumptions` unless all lifts, signs, reduced denominators, overlaps, and dyadic endpoints are handled.

Exploratory allocation: write one sign-preserving endpoint lemma for the top block $D\asymp X^{1/2}$ using the expansion $d=\lfloor X^{1/2}\rfloor+m$, but keep it `proposed` unless fully proved.

### For A3

Target obligations: `M9-fourth-moment-enumeration`, `M9-regression-raw-vs-paired`, `M9-M2-local-fourth-moment-LFM` diagnostics, `M9-M2-reciprocal-SPD-route`.

Objectives:

1. Execute, not plan. Required deliverables:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - `python -m py_compile` result;
   - precision log;
   - CSV schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Use exact integer arithmetic for $N$ and exact rational reduction for $h_i/d_i=p_i/q_i$.

3. First required tables:
   - DP parity/no-small-nonzero-$N$ check;
   - DP thin mass compared to $C_0D\log^2(2H)$;
   - URES residual enumeration including $(6,10,15,5)k$;
   - $R(r)^2$ concentration;
   - reduced-paired versus residual exact mass.

4. Formula regression:
   - raw two-sided M2;
   - complex-weight cosine pairing;
   - real-weight $\operatorname{Re}B_h$ pairing;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

5. Local-window diagnostics:
   - compute $\max \delta|\lambda|$;
   - compare $\delta^{-1}\int_I |S_2|^4$ to local sup;
   - include $D=X^{1/4},X^{3/8},X^{1/2}$.

6. Before running any diagnostic, fix the $d=7$ imaginary-part sign, the complex-weight relation $B_{-1}=(1+i)\overline{\Sigma}$, and the envelope $\sup_I |S_2'|\ll H_D$.

7. SPD diagnostics:
   - compute $P(D,H;X)$;
   - compare true beta signs, unsigned signs, random signs, and adversarial signs.

All outputs remain `diagnostic_only`.

### For A4

Target obligations: `M9-M2-DP-near-collision-bound`, `M9-M2-coprime-rigidity-normal-form`, `M9-M2-NF-participation-rigidity`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-unpaired-residual-URES`, `M9-M2-reciprocal-SPD-route`.

Objectives:

1. Write validator-ready statements and proofs for:
   - DP-0 parity;
   - DP-1 thin-band emptiness;
   - DP-2 thin DP mass;
   - DP-3 full DP total mass;
   - exact H4 dependency split.

2. Insert NF-1 and NF-2 in lemma-bank form. NF-2 must include all definitions:

$$
g=\gcd(Q,q_1),\quad
\widehat Q=Q/g,\quad
\widehat q_1=q_1/g,\quad
M=\mu\widehat q_1-p_1\widehat Q.
$$

3. Verify overlap bookkeeping for U-2, SS, anti-paired, and fraction-matching coverage of all exact $N=0$ tuples with reduced-denominator multiset $\{q,q,q',q'\}$.

4. Attack URES jointly with A2:
   - attempt a proof of $\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon$;
   - or produce a counterexample/lower-bound family;
   - or reduce it to a named divisor-sum inequality.

5. Develop SPD only as backup. State the exact theorem required for reciprocal points $\theta_d=X/(4d)$ and give A3 a falsification threshold.

Exploratory allocation: formulate a global-moment/large-value propagation map for sub-endpoint ranges $D\le X^{1/2-\eta}$, with all assumptions marked as proposed or diagnostic unless proved.

## Round Assessment

Round 6 produced real proof-graph progress, but not endpoint proof.

Agent scores:

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 7.0 | 9.0 | Strong source-card draft, $\Phi$ regularity, M2 formulas, local kernel, and endpoint degeneracy. Correctly avoided endpoint overclaim. A4's subcoherence result supersedes the endpoint-only framing. |
| A2 | 7.2 | 3.8 | 5.8 | Good terminology separation and useful exploratory Poisson/B-process idea. The unpaired mass bound is not proved, and the nonseparability obstruction is over-scoped if treated as route-closing. |
| A3 | 7.0 | 2.5 | 7.5 | Useful diagnostic architecture and correct diagnostic-only attitude, but no executed artifact. Formula and classifier issues must be fixed before evidence is positive. |
| A4 | 9.0 | 8.0 | 8.5 | Strongest analytic contribution: DP suite, NF-2, subcoherence-window equivalence, reduced-paired exact-resonance bounds, and URES residual definition. Some overlap bookkeeping still needs proof-draft verification. |

Split round scores:

- idea quality: 8/10;
- state evidence: 6/10;
- calibration: 8/10;
- mathematical progress: 5/10.

The proof graph gains narrower lemmas and a better obstruction map. It does not gain `M9-M2`, `M9`, or the final theorem.

## Confidence

Confidence: 0.84.

High confidence:
- A1's $\Phi$ regularity calculation is correct conditional on the Vaaler formula.
- The local fourth-moment kernel and endpoint degeneracy calculations are correct.
- A4's DP parity and thin-band scoping are correct under H4 beta support.
- The subcoherence-window multiplier correctly downgrades local `(LFM)` as a primary route.
- No endpoint theorem or Gauss circle exponent is proved.

Moderate confidence:
- NF-2 is ready for `proved_internal` after proof-draft transcription.
- The reduced-paired bound is valid under H4, pending overlap bookkeeping verification.
- URES is the right next exact-resonance target.

Low-to-moderate confidence:
- URES can actually be bounded at $D^2X^\epsilon$ without a new idea.
- SPD will show enough true-sign cancellation at the endpoint.
- Any existing Li--Yang/Bombieri--Iwaniec theorem can be imported without substantial adaptation.

No new Gauss circle exponent is proved in Round 6.
