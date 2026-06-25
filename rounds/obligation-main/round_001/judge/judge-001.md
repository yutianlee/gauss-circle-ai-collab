## Selected main route

Source basis: `judge_1.md` asks for a Round 1 Stage C judge synthesis, requires the Stage C schema, and states that the `State Patch` block is the only mechanism for mutating `state/proof_obligations.yml`.

Continue the current `M9-M2-character-factor` route, but only at the level of exact coefficient algebra and finite-sum transformations. Do **not** claim `M9`, `M9-M2`, `M9-near-collision-taxonomy`, or the Gauss circle target.

The selected route for the next round is:

$$
\mathcal M_2
\longrightarrow
\text{exact } C_h \text{ and } \beta_h \text{ algebra}
\longrightarrow
\text{Cauchy sign-loss diagnostics}
\longrightarrow
\text{two-sided fourth-moment expansion}
\longrightarrow
\text{corrected near-collision taxonomy}.
$$

The current bridge remains conditional:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The active bottleneck remains `M9`, especially `M9-M2`. No Round 1 output supplies a uniform estimate for either $\mathcal M_1(D;X)$ or $\mathcal M_2(D;X)$ over

$$
X^{1/4}\le D\le X^{1/2}.
$$

## Useful fragments by source

### From A1

A1's main useful contribution is the narrow coefficient algebra for the $\mathcal M_2$ frequency factor.

For

$$
C_h=e(h/4)-e(3h/4),
$$

one has

$$
C_h=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

Assuming the H4 Vaaler coefficient convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

the actual $\mathcal M_2$ coefficient

$$
\beta_{h,H}=\alpha_{h,H}C_h
$$

is

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)\,1_{2\nmid h}.
$$

Thus $\beta_{h,H}$ is real and even. This corrects the ambiguity around complex conjugation and is the strongest safe algebraic progress of the round. The A1 review also records this as the synthesis to keep: add a narrow beta-algebra lemma, a Cauchy sign-loss diagnostic, and an algebraic fourth-moment expansion while keeping `M9` and `M9-M2` open.

A1 also correctly identifies the bounded-scope Cauchy diagnostic. A positive-weight $h$-Cauchy step replaces

$$
C_h\overline{C_h}
$$

by

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

The sign $\chi_4(h)$ is lost, and only odd-frequency support remains. This is not a no-go theorem for all $\mathcal M_2$ approaches; it is a warning about the standard second-moment route.

The fourth-moment expansion supplied by A1 should be kept as algebra. In the two-sided convention,

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_d w_D(d)e(hX/(4d)),
$$

the phase in $|S_2|^4$ is

$$
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right),
$$

with cleared numerator

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

This should become the official object for `M9-near-collision-taxonomy`.

### From A2

A2's useful fragment is the decision to attack `M9-M2-character-factor` through exact $C_h$ algebra and fourth moments. A2 correctly identifies the base identity for $C_h$, and it is right that the fourth moment is the first standard moment where the $\chi_4(h)$ sign can survive longer than in a second-moment Cauchy step.

However, A2 overstates several claims. A2.md proposes promoting `M9-M2-character-factor` to `proved_internal`, marking `M9-near-collision-taxonomy` as blocked, and adding a Gallagher obstruction; its proposed patch includes a false or unsupported cross-parity claim involving $16(-1)^{N/2}$ and an unsupported Gallagher aliasing blocker. The Stage B review correctly rejects these overpromotions and says the useful synthesis is only the narrow coefficient lemma plus finite fourth-moment algebra.

The A2-2 response is supplemental only. It contains a frequency-only congruence idea, but it pivots to a Poisson-dual model and claims a `M9-Poisson-diagonal-capacity` lemma marked `proved_internal` and implying `M9`. That is not acceptable as a state mutation. The diagonal capacity computation is, at most, an exploratory model; it does not prove the actual reciprocal $\mathcal M_2$ bound.

### From A3

A3's useful contribution is the insistence that `M9-regression-raw-vs-paired` should become an executable diagnostic with scripts, commands, tables, precision notes, and a report. That matches the existing computation obligation.

A3's output should not be promoted, however. It says the actual $\mathcal M_2$ weights satisfy

$$
\beta_{-h}=-\overline{\beta_h},
$$

but the correct relation is

$$
\beta_{-h}=\beta_h=\overline{\beta_h}
$$

under the H4 coefficient convention. The Stage B review also notes that A3's surrogate kernel is not adequate state evidence and that the paired formula should be exact for real dyadic weights after the coefficient algebra is fixed.

A3's next useful role is implementation: test raw two-sided formulas against paired real formulas for real weights, and deliberately show paired real formulas fail outside their hypotheses, especially for complex weights. The current A3 response is a plan, not executed diagnostic evidence.

## Rejected or risky ideas

1. **Reject any promotion of `M9`, `M9-M2`, or the Gauss circle target.** No uniform endpoint estimate is proved.

2. **Reject A2's claim that `M9-M2-character-factor` is proved as written.** The correct algebra is useful, but the proposed $16(-1)^{N/2}$ rule is false or at least unsupported for the cleared denominator numerator.

3. **Reject A2's full near-collision taxonomy.** The taxonomy is incomplete. Exact $N=0$ and $0<|N|\sim T$ cases remain open.

4. **Reject A2's Gallagher aliasing obstruction as an official blocker.** No precise Gallagher lemma, hypotheses, transition inequality, or counterexample construction is supplied. It may be kept only as a possible audit question.

5. **Reject A2's Voronoi/J-Bessel pivot as proof-ready.** It omits truncation, smoothing, endpoint, coefficient-growth, and transformation-error bookkeeping.

6. **Reject A2-2's `M9-Poisson-diagonal-capacity` state patch.** It analyzes a transformed model and a diagonal capacity, not the full original reciprocal $\mathcal M_2$ problem.

7. **Reject A3's proposed promotion of `M9-regression-raw-vs-paired` to `diagnostic_only` until actual files exist.** A plan is not evidence.

8. **Reject A3's surrogate kernel as official computation.** The official regression must use the actual M1/M2 raw formulas and the actual Vaaler coefficients.

9. **Reject the claim that paired formulas fail for real weights.** For real $w_D$, the paired formulas should be exact after the coefficient convention is corrected. Complex weights are the intended failure-of-hypotheses test.

## Known gaps

1. **H4 source audit remains open.** The coefficient convention for $\alpha_{h,H}$ is treated conditionally until the Vaaler source card is completed.

2. **`M9-M2` remains open.** No estimate

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

is proved uniformly over active $D$.

3. **`M9-M1` remains open.** The round focused on $\mathcal M_2$ and does not prove the $\mathcal M_1$ fixed-coefficient estimate.

4. **Near-collision taxonomy remains open.** The correct fourth-moment numerator $N$ is available, but exact $N=0$ families and $0<|N|\sim T$ bands are not classified or bounded.

5. **Endpoint uniformity remains open.** Every future estimate must explicitly cover

$$
X^{1/4}\le D\le X^{1/2}.
$$

6. **Raw-vs-paired regression is not executed.** A3 must produce actual files and tables.

7. **Complex-weight failure test is missing.** Paired real formulas require real dyadic weights. This must be tested explicitly.

8. **A2's sign-rule and parity-sieve claims need falsification tests before any reuse.**

## New lemmas to add

### M9-M2-beta-algebra

Status: `derived_under_assumptions`.

Assuming H4's coefficient convention,

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

one has

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

and

$$
\beta_{h,H}:=\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Thus $\beta_{h,H}\in\mathbb R$ and $\beta_{-h,H}=\beta_{h,H}$.

### M9-M2-h-cauchy-sign-loss

Status: `derived_under_assumptions`.

For

$$
S_2=\sum_h\alpha_hC_hB_h,
$$

a positive $|\alpha_h|$-weighted $h$-Cauchy step replaces the character factor by

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

Therefore that route loses the $\chi_4(h)$ sign. This is a bounded-scope diagnostic only.

### M9-M2-fourth-moment-expansion

Status: `derived_under_assumptions`.

For

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_d w_D(d)e(hX/(4d)),
$$

the two-sided fourth moment expands with phase

$$
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right),
$$

and cleared resonance integer

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

This is algebraic only. It does not prove a fourth-moment estimate.

## Counterexample checks to run

1. **Coefficient algebra check.** For multiple $H$ and $h$, compute $\alpha_{h,H}$, $C_h$, and $\beta_h$. Verify that $\beta_h=0$ for even $h$, $\beta_h$ is real for odd $h$, and $\beta_{-h}=\beta_h$.

2. **A2 sign-rule falsification.** Test

$$
h_1=h_2=h_3=h_4=1,
\qquad
(d_1,d_2,d_3,d_4)=(1,3,1,1).
$$

For A2's plus-plus-minus-minus numerator, $N=-2$, so $(-1)^{N/2}=-1$, but the $h$-character product is positive. This falsifies the deterministic sign rule in that form.

3. **A2 parity-sieve falsification.** With all $h_i$ odd and

$$
(d_1,d_2,d_3,d_4)=(2,4,6,1),
$$

every term in the cleared numerator is even. This contradicts the "one or three even denominators imply odd $N$" claim.

4. **Weighted $h$-Cauchy sign-loss check.** Expand the second moment and verify that $C_h\overline{C_h}=4\,1_{2\nmid h}$.

5. **Raw-vs-paired regression.** For real $w_D$, verify equality between raw two-sided complex formulas and paired real formulas. For complex $w_D$, verify paired real formulas fail unless modified.

6. **Fourth-moment binning.** Enumerate small finite ranges and classify $N=0$ into diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified bins. Do not infer asymptotics from tiny data.

7. **A2-2 Poisson model check.** Test whether the Poisson-dual variables and diagonal-capacity model actually arise from the project's reciprocal $\mathcal M_2$ definition with the same weights, constants, truncation, and endpoint ranges. Until then, it remains exploratory.

## Research strategy adjustment

The next round should be narrow and conservative.

A1 should consolidate the algebra into the proof graph and keep all theorem claims conditional on H4 and M9. A1 should not expand the proof graph with broad obstruction claims.

A2 should repair the fourth-moment taxonomy using the actual coefficient

$$
\beta_h=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

the two-sided convention, and the corrected numerator

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

A3 should execute the regression obligation with actual formulas. No further protocol-only response should be accepted as evidence. The expected outputs are a script, command, table, precision log, and report.

Keep Li--Yang as a guardrail only. Do not import it as an endpoint theorem. Keep Voronoi/Bessel or Poisson-dual alternatives as exploratory unless they supply an exact reduction to the active M9 formulas.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "M9-M2-beta-algebra",
        "type": "normalization",
        "track": "M9_analytic",
        "title": "Exact beta_h coefficient algebra for M2",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming the H4 Vaaler coefficient convention alpha_{h,H}=-Phi(|h|/(H+1))/(2 pi i h), the M2 coefficient beta_{h,H}=alpha_{h,H}(e(h/4)-e(3h/4)) equals -Phi(|h|/(H+1)) chi_4(|h|) 1_{2 not divides h}/(pi |h|). Hence beta_{h,H} is real and even.",
        "dependencies": [
          "H4"
        ],
        "implies": [
          "M9-M2-character-factor"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/round_001/responses/A1_reasoning_1.md",
            "rounds/round_001/reviews/A1_review_1.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/round_001/responses/A2.md",
            "rounds/round_001/responses/A3.md"
          ]
        },
        "owner": "A1",
        "next_action": "Verify the exact H4 coefficient convention from the Vaaler source card and then insert the beta_h algebra into the proof draft."
      },
      {
        "id": "M9-M2-h-cauchy-sign-loss",
        "type": "obstruction",
        "track": "M9_analytic",
        "title": "Weighted h-Cauchy loses the M2 frequency character sign",
        "status": "derived_under_assumptions",
        "statement_tex": "For S_2=sum_h alpha_h C_h B_h, the positive |alpha_h|-weighted h-Cauchy step replaces C_h by |C_h|^2=4 1_{2 not divides h}; therefore the chi_4(h) sign is lost and only odd-frequency support remains. This is a bounded-scope diagnostic for that Cauchy normalization.",
        "dependencies": [
          "M9-M2-beta-algebra"
        ],
        "implies": [
          "M9-M2-character-factor"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/round_001/responses/A1_reasoning_1.md",
            "rounds/round_001/reviews/A1_review_1.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/round_001/responses/A2.md",
            "rounds/round_001/responses/A3.md"
          ]
        },
        "owner": "A1",
        "next_action": "Use this only as a diagnostic. A2 should test fourth moments, CRI, or direct signed bilinear estimates rather than treating this as a no-go theorem."
      },
      {
        "id": "M9-M2-fourth-moment-expansion",
        "type": "reduction",
        "track": "M9_analytic",
        "title": "Algebraic fourth-moment expansion for M2 with retained character product",
        "status": "derived_under_assumptions",
        "statement_tex": "For S_2(D;X)=sum_{1<=|h|<=H_D} beta_h sum_d w_D(d)e(hX/(4d)), the two-sided fourth moment has phase X/4*(h_1/d_1-h_2/d_2+h_3/d_3-h_4/d_4) and cleared resonance integer N=h_1 d_2 d_3 d_4-h_2 d_1 d_3 d_4+h_3 d_1 d_2 d_4-h_4 d_1 d_2 d_3. The coefficient product retains the fourfold h-character before absolute-value majorization.",
        "dependencies": [
          "M9-M2-beta-algebra"
        ],
        "implies": [
          "M9-near-collision-taxonomy"
        ],
        "blockers": [
          "M9-near-collision-estimate"
        ],
        "evidence": {
          "positive": [
            "rounds/round_001/responses/A1_reasoning_1.md",
            "rounds/round_001/reviews/A1_review_1.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/round_001/responses/A2.md"
          ]
        },
        "owner": "A2",
        "next_action": "Classify exact and near-collision configurations using this N, actual beta_h weights, and a fixed two-sided convention."
      }
    ],
    "update": [
      {
        "id": "M9-M2-character-factor",
        "status": "open",
        "evidence_added": {
          "positive": [
            "rounds/round_001/responses/A1_reasoning_1.md"
          ],
          "negative": [
            "rounds/round_001/reviews/A1_review_1.md"
          ],
          "inconclusive": [
            "rounds/round_001/responses/A2.md",
            "rounds/round_001/responses/A2-2.md",
            "rounds/round_001/responses/A3.md"
          ]
        },
        "next_action": "Use M9-M2-beta-algebra, M9-M2-h-cauchy-sign-loss, and M9-M2-fourth-moment-expansion to decide whether the next M2 attack should use fourth moments, CRI, or direct signed bilinear estimates. Do not promote M9-M2 without a uniform endpoint estimate."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "evidence_added": {
          "positive": [],
          "negative": [
            "rounds/round_001/reviews/A1_review_1.md"
          ],
          "inconclusive": [
            "rounds/round_001/responses/A2.md",
            "rounds/round_001/responses/A2-2.md"
          ]
        },
        "next_action": "Repair the taxonomy using the corrected two-sided fourth-moment numerator N and actual beta_h weights. Classify exact N=0 and 0<|N|~T configurations with counterexample-tested sign rules only."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "proposed",
        "evidence_added": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round_001/responses/A3.md",
            "rounds/round_001/reviews/A1_review_1.md"
          ]
        },
        "next_action": "Produce computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and report.md using the actual M1/M2 raw formulas and actual Vaaler coefficients. Verify real-weight paired equality and complex-weight failure of the paired real formulas. Mark all evidence diagnostic_only."
      }
    ],
    "reject": [
      {
        "id": "A2-M9-M2-character-factor-proved-internal-claim",
        "reason": "A2's proposed promotion overstates the coefficient algebra and relies on the false or unproved cross-parity claim 16(-1)^{N/2}."
      },
      {
        "id": "A2-M9-near-collision-taxonomy-blocked-claim",
        "reason": "The taxonomy is not complete, and the Gallagher aliasing obstruction is not proved."
      },
      {
        "id": "A2-M9-Gallagher-Aliasing-Derivative-Block",
        "reason": "No precise Gallagher lemma, hypotheses, transition inequality, or counterexample construction is supplied."
      },
      {
        "id": "A2-2-M9-Poisson-diagonal-capacity",
        "reason": "The Poisson diagonal-capacity computation is an exploratory transformed-model calculation and does not prove M9 or the actual reciprocal M2 estimate."
      },
      {
        "id": "A3-M9-regression-diagnostic-only-promotion",
        "reason": "The response supplies a plan and surrogate-kernel script design, not committed executable files or actual M1/M2 raw-vs-paired output."
      },
      {
        "id": "A3-M9-regression-script-duplicate",
        "reason": "The existing obligation M9-regression-raw-vs-paired already requires the script, command, table, precision log, and report."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform endpoint estimates for both M1 and M2 were proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 1 did not address or prove the M1 fixed-coefficient estimate."
      },
      {
        "id": "M9-M2",
        "reason": "Only algebraic and diagnostic reductions were produced; no uniform M2 estimate was proved."
      },
      {
        "id": "M9-endpoint-uniformity",
        "reason": "No proposed estimate was shown uniformly for all active dyadic D."
      },
      {
        "id": "GC-target",
        "reason": "The final theorem remains conditional on M9."
      },
      {
        "id": "H4",
        "reason": "The Vaaler theorem still requires source audit before being used as a fully verified external dependency."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a guardrail/source-audit item only."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 4,
    "reason": "Round 1 made useful algebraic progress on the M2 coefficient and clarified Cauchy/fourth-moment diagnostics, but A2 and A3 overpromoted claims and no analytic endpoint estimate was proved."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `M9-M2-beta-algebra`, `M9-M2-h-cauchy-sign-loss`, and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Write a proof-draft-ready coefficient-normalization note using the actual H4 coefficient convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

2. Prove

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h}
$$

and

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

3. State the paired real $\mathcal M_2$ formula for real dyadic weights only, and explicitly state why complex weights are outside that formula's hypotheses.

4. Write the weighted $h$-Cauchy sign-loss diagnostic and the unweighted $h$-Cauchy endpoint diagonal check as bounded-scope diagnostics, not no-go theorems.

5. Insert the corrected two-sided fourth-moment expansion and cleared numerator $N$ into the proof draft.

6. Do not promote `M9`, `M9-M2`, or `M9-near-collision-taxonomy`.

Exploratory allocation: give a one-page comparison of fourth moment, CRI, and direct signed bilinear routes for $\mathcal M_2$, with one falsification criterion for each.

### For A2

Target obligations: `M9-near-collision-taxonomy` and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Rewrite the fourth-moment taxonomy using the actual $\Phi$-weighted coefficient $\beta_h$, not a Fejer-linear surrogate.

2. Use exactly one convention: preferably the two-sided convention

$$
1\le |h|\le H_D.
$$

3. Use the corrected phase

$$
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
$$

and the corrected numerator

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

4. Classify exact $N=0$ families: exact diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified.

5. For every claimed class, give either a proof, a counterexample, or a status label from the allowed reasoning labels: `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, `[LIKELY-FALSE]`.

6. Remove or repair the Gallagher obstruction. If retained, state a precise theorem with hypotheses and explain exactly how the M2 variables violate it.

7. Do not claim that A2-2's Poisson diagonal-capacity model proves M9. If used, restate it as exploratory and connect it back to the actual reciprocal $\mathcal M_2$ formula.

Exploratory allocation: define one CRI statistic under the two-sided convention and state what numerical behavior would falsify CRI as a serious route.

### For A3

Target obligation: `M9-regression-raw-vs-paired`.

Objectives:

1. Produce actual files, not only a protocol:

- `computations/m9_regression/run.py`
- `outputs/table_small.csv`
- a precision log
- `computations/m9_regression/report.md`

2. Use the actual raw two-sided M1/M2 formulas and actual Vaaler coefficients.

3. For real dyadic weights, verify raw two-sided sums equal the paired formulas to numerical precision.

4. For complex dyadic weights, verify that the paired real formulas fail unless modified.

5. Include explicit checks for

$$
C_h=2i\chi_4(h)1_{2\nmid h},
\qquad
|C_h|=2 \text{ for odd } h,
\qquad
\beta_{-h}=\beta_h.
$$

6. Include a weighted $h$-Cauchy sign-loss regression showing that $|C_h|^2=4\,1_{2\nmid h}$.

7. Include a small fourth-moment binning routine using the corrected $N$ formula. Label results diagnostic only.

8. Do not use surrogate kernels as official evidence. Toy kernels may appear only in a separate exploratory appendix.

Exploratory allocation: add one complex-weight failure test and one small exact-bin enumeration for A2's corrected taxonomy.

## Round Assessment

Round 1 is useful but not proof-progress at the endpoint. The correct state update is narrow:

- Accept the exact $C_h$ and $\beta_h$ algebra, conditional on H4.
- Accept the weighted $h$-Cauchy sign-loss diagnostic.
- Accept the fourth-moment expansion and corrected numerator as algebraic reductions.
- Keep `M9`, `M9-M2`, and `M9-near-collision-taxonomy` open.
- Keep `M9-regression-raw-vs-paired` proposed until actual files exist.
- Reject A2's and A2-2's broad state promotions.
- Reject A3's algebraic premise about $\beta_{-h}$ and its surrogate-kernel evidence.

Scores for the reviewed non-judge agents, using the Stage B assessment:

| Agent | Score | Reason |
|---|---:|---|
| A2 | 5.0 | Correct base $C_h$ direction and useful fourth-moment instinct, but several central claims are false or unsupported, including the $16(-1)^{N/2}$ rule, denominator parity sieve, Gallagher obstruction, and state-patch promotions. |
| A3 | 5.5 | Correctly targets executable diagnostics, but the main premise about $\beta_{-h}$ is wrong, the official computation is not executed, and the surrogate kernel is not state evidence. |

## Confidence

High confidence in the $C_h$ identity, beta-coefficient algebra conditional on H4, paired real formula under real weights, and the weighted $h$-Cauchy sign-loss diagnostic.

High confidence that no Round 1 output proves `M9`, `M9-M2`, `M9-near-collision-taxonomy`, or the Gauss circle target.

Moderate confidence that the corrected fourth-moment expansion is the right next finite object for `M9-near-collision-taxonomy`.

Low confidence in A2's Gallagher obstruction, A2's Voronoi/J-Bessel pivot, and A2-2's Poisson diagonal-capacity route as currently stated.

No confidence claim is made for a new Gauss circle exponent.