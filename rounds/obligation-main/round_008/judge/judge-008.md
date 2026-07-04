## Selected main route

I treated `judge_8.md` as the controlling Stage C prompt for this turn. It requires a conservative judge synthesis with selected route, useful fragments, rejected ideas, gaps, new lemmas, counterexample checks, research strategy adjustment, a JSON-compatible `State Patch`, next-round prompts for A1/A2/A3/A4, round assessment, and confidence.

The selected Round 9 route is now a **scale-bifurcated signed near-collision program**.

The old all-range absolute graded near-collision route is no longer viable. A4's window lower bound shows that, under the H4 beta lower envelope, the fat-band absolute target

$$
\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\ll_\epsilon D^2X^\epsilon
$$

fails for $D>X^{3/8+\delta}$. The lower bound is

$$
\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\gg D^4X^{-3/4},
$$

which exceeds $D^2X^\epsilon$ past the $X^{3/8}$ split. This is not a heuristic uniform-distribution claim; it follows from a window/pigeonhole lower bound using same-window pair-of-pair mass.

Therefore the primary route is:

1. **For lower dyadic scales $D\le X^{3/8+o(1)}$:** continue the absolute/structured interval-URES program, using exact URES arithmetic and the interval strip count as local infrastructure. This does not prove `M9-M2`; it only keeps a corrected absolute subroute alive where lower bounds do not already exceed budget.

2. **For upper dyadic scales $X^{3/8}<D\le X^{1/2}$:** pivot to signed mechanisms that retain the $\chi_4(h)$ structure. The main proposed target is a signed fat-band constant $c_\chi(D;X)$ controlling the signed off-diagonal pair-sum contribution in a smoothed global fourth moment. This target must then be paired with a pointwise large-value theorem or direct endpoint estimate.

The backup route is a **smooth sign-preserving Poisson/B-process endpoint route**. It remains proposed only. It needs a complete stationary-phase formula with exact phase, support, $m=0$ term, boundary terms, support-edge stationary points, nonstationary tails, and then a signed post-transform estimate. A leading-order transform alone does not prove `M9-M2`.

No proof of `M9`, `M9-M1`, `M9-M2`, `GC-target`, or H4 is established in Round 8.

## Useful fragments by source

### From A1

A1's strongest contributions are normalization discipline, the corrected rejection of full-range absolute GNC, and the average-to-pointwise obstruction.

A1 correctly sharpened the beta algebra under H4:

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

and, assuming the Vaaler coefficient convention,

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

This remains `derived_under_assumptions`, because the H4 source card is still incomplete.

A1's derivative propagation calculation is state-useful as negative evidence. If

$$
\int_X^{2X}|S_2(D;t)|^4\,dt\ll_\epsilon XD^2X^\epsilon
$$

and

$$
|S_2'(D;t)|\ll H_D\asymp DX^{-1/4},
$$

then a point value $V=|S_2(D;X_0)|$ satisfies only

$$
V\ll_\epsilon D^{3/5}X^{3/20+\epsilon}.
$$

At $D=X^{1/2}$ this is $X^{9/20+\epsilon}$, far above the target $X^{1/4+\epsilon}$. The judge packet verifies this arithmetic.

A1's interval URES strip identity is safe as pure algebra:

$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|\le\eta
$$

implies

$$
|(\mu q_1-Qp_1)(\mu q_3-Qp_3)-Q^2p_1p_3|
\le
|\mu|\eta Qq_1q_3.
$$

It should be promoted only as an algebraic identity, not as a counting theorem by itself.

### From A2

A2's useful contribution is route pressure toward an absolute-route obstruction and sign-preserving methods. However, A2's proposed `proved_internal` obstruction should not be accepted as stated because its own version relies on a uniform-distribution heuristic. The rigorous state evidence for the obstruction should come from A4's explicit lower-bound mechanisms, especially W-1 and the twin-shift family, not from the heuristic model. The review material explicitly recommends downgrading A2's proof labels and replacing the heuristic basis with A4's window lower bound.

A2's Poisson/B-process calculation is useful at the leading-order scale, but it is not a proof obligation with proved status. It lacks the full stationary-phase theorem and, more importantly, lacks the signed post-transform estimate.

A2 also had a sign/convention issue in one URES interval formulation: the fourth-moment phase is

$$
x_1-x_2+x_3-x_4=(x_1+x_3)-(x_2+x_4),
$$

so the target pair sum must be normalized consistently. The A1/A4 integer-defect formulation is the safer state statement.

### From A3

A3's diagnostic design is useful but not proof evidence. The judge material requests endpoint $c_\chi$ diagnostics, unsigned analogues, UNC/TS/W-1 spot checks, structured-vs-generic denominator splits, and exact URES identity checks. It also stresses that diagnostic outputs remain `diagnostic_only` and require execution, commands, tables, precision logs, and reports before they can even be attached as diagnostic evidence.

The complex-weight regression must be corrected. The algebraic cosine pairing can remain valid for complex $d$-weights if the same complex weight is used in the $h$ and $-h$ terms. The expected failure is the shortcut through $\operatorname{Re}B_h$, not the cosine-paired identity.

### From A4

A4 supplies the core Round 8 mathematical progress.

First, A4's interval URES count gives a proved arithmetic lemma, with hypotheses. For reduced $\mu/Q\ne0$, fixed nonzero $p_1,p_3$, $Q\le4D^2$, $|p_i|\le2H_D$, and $0\le\eta\le4X^{-1/4}$, the count of pairs $(q_1,q_3)\in[1,2D]^2$ satisfying

$$
\gcd(p_i,q_i)=1,
\qquad
\left|\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}\right|\le\eta
$$

is

$$
\ll_\epsilon X^\epsilon(1+\eta QD^2)+\Delta,
$$

where the degenerate branch is separated and satisfies

$$
\Delta\le4D\mathbf 1_{\eta\ge1/(2D)}.
$$

The proof is a divisor count over the shifted hyperbolic strip, with the degenerate $uv=0$ branch isolated.

Second, A4's W-1 window lower bound refutes the absolute fat-band target past $D=X^{3/8}$. The essential calculation is:

$$
\sum_i m_i^2
\ge
\frac{(\sum_i m_i)^2}{K}
\asymp
D^4\eta X^{1/4}.
$$

Pairs in the same window satisfy $|N|\le16D^4\eta$, so with $M=16D^4\eta$ the near-collision mass is

$$
\gg MX^{1/4}-D^2X^\epsilon.
$$

At $M=D^4/X$, this is $\gg D^4X^{-3/4}$, exceeding the target once $D>X^{3/8+\delta}$.

Third, A4's signed lift-cancellation lemma B-1 is a promising H4-dependent signed input. Its use depends on $\Phi$ regularity and source-card completion. It should be recorded as `derived_under_assumptions`, not unconditional.

Fourth, A4's signed global moment identity and $c_\chi$ target are the right upper-range direction, but the actual bound on $c_\chi$ is open.

## Rejected or risky ideas

1. **Reject full-range absolute GNC-Abs.** The estimate

$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon
$$

cannot hold across the full active range. A1's full-support lower-bound check already rejects the largest $M$ range, and A4's W-1 rejects the fat band for $D>X^{3/8+\delta}$.

2. **Reject A1's GNC-low as a global all-$D$ target.** A1's restricted low-band version is still false for $D>X^{3/8+\delta}$ at $Y\asymp1$, by W-1. It may survive only with an explicit dyadic restriction such as $D\le X^{3/8+o(1)}$, for structured classes, or after replacing absolute weights by signed weights.

3. **Reject A2's `M9-M2-absolute-mass-obstruction` as `proved_internal`.** The conclusion is useful, but the proof basis must be A4's explicit lower-bound families and W-1, and the status must be H4-dependent.

4. **Reject A2's Poisson/B-process transform as proved.** The leading stationary phase model is not enough. The endpoint proof requires a full smooth transform and a signed dual sum estimate.

5. **Reject computations as proof.** A3 diagnostics can add `diagnostic_only` evidence after execution, but not theorem proof.

6. **Reject importing Vaaler, Li--Yang, Huxley, Bourgain-Watt, or exponent-pair estimates as dependencies without source cards.** The local Vaaler PDF supports the formula for $\widehat J$ in Theorem 6 and its monotonicity/positivity properties, but H4 remains source-audit-blocked until the source card is complete. Li--Yang proves the record exponent $\theta^*=0.314483\ldots$ and discusses the $5/16$ barrier; it is guardrail context, not an endpoint theorem for this proof graph.

7. **Reject any change to `M9`, `M9-M1`, `M9-M2`, `GC-target`, `H4`, or `R5-Full`.** Round 8 supplies obstruction and infrastructure, not a pointwise endpoint estimate.

## Known gaps

1. **H4 source audit.** Beta formula, beta lower envelopes, parity support, and $\Phi$ regularity remain blocked by `H4-source-audit`.

2. **Signed fat-band bound.** The proposed $c_\chi(D;X)$ bound is the central open target. No proof currently shows the necessary signed cancellation at $D>X^{3/8}$.

3. **Pointwise upgrade.** Even a smoothed global fourth moment would not imply `M9-M2` by crude derivative propagation. A large-value theorem or direct signed endpoint estimate is required.

4. **Coefficient freezing.** The signed global moment identity uses frozen coefficients and fixed $H_D$. If coefficients vary with $t$ across an $X$-window, a stability lemma is needed.

5. **Absolute lower-D upper bound.** The fact that absolute estimates fail for $D>X^{3/8}$ does not prove they work for $D\le X^{3/8}$. The corrected upper-bound half remains open.

6. **Interval URES count is not the full near-collision theorem.** U-3$\eta$ counts one reduced-fraction representation strip with hypotheses and degenerate branch separation. It must still be assembled with dyadic lifts, tuple classification, signs, and active ranges.

7. **M1 remains open.** Round 8 continues to focus on M2. `M9` cannot move without both `M9-M1` and `M9-M2`.

8. **Diagnostics not executed.** A3's plan is not yet data.

## New lemmas to add

### Lemma 1: interval URES strip identity

Status: `proved_internal`.

For reduced $\mu/Q\ne0$ and reduced nonzero $p_i/q_i$ with $q_i>0$, if

$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|\le\eta,
$$

then

$$
|(\mu q_1-Qp_1)(\mu q_3-Qp_3)-Q^2p_1p_3|
\le
|\mu|\eta Qq_1q_3.
$$

This is algebra only and has no counting implication by itself.

### Lemma 2: interval URES strip count

Status: `proved_internal`, scoped.

For reduced $\mu/Q\ne0$, nonzero $p_1,p_3$, $Q\le4D^2$, $|p_i|\le2H_D$, $0\le\eta\le4X^{-1/4}$, and $q_i\in[1,2D]$, the number of reduced denominator pairs satisfying the interval inequality is

$$
\ll_\epsilon X^\epsilon(1+\eta QD^2)+\Delta,
$$

with

$$
\Delta\le4D\mathbf 1_{\eta\ge1/(2D)}
$$

for the degenerate branch. The degenerate branch must be routed separately in fourth-moment taxonomy.

### Lemma 3: absolute near-collision lower bounds

Status: `derived_under_assumptions`.

Assuming H4 beta lower envelopes and exact $N=0$ mass closure, absolute near-collision mass exceeds the old target in upper dyadic ranges. In particular, the absolute fat-band bound

$$
\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\ll_\epsilon D^2X^\epsilon
$$

fails for $D>X^{3/8+\delta}$. The statement should separately record UNC large-$M$ lower bounds, TS constructive fat-band mass, and W-1 window/pigeonhole lower bounds.

### Lemma 4: signed lift cancellation B1

Status: `derived_under_assumptions`.

Under H4 beta algebra, $\Phi$ regularity, and suitable smooth/bounded-variation lift weights, the signed dyadic lift weight

$$
A_\chi(p/q)
=
\sum_{\substack{gq\in[D,2D)\\1\le |gp|\le H_D}}
\beta_{gp,H_D}w_D(gq)
$$

has cancellation beyond the absolute envelope, for example of the shape

$$
|A_\chi(p/q)|\ll \frac{q}{D|p|}
$$

in the stated B-1 regime. Exact smoothness, endpoint, and parity hypotheses must be included in the proof draft.

### Lemma 5: signed fat-band constant

Status: `proposed`.

Define a signed off-diagonal constant $c_\chi(D;X)$ for the smoothed global fourth moment, normalized by $D^2$. The target is

$$
|c_\chi(D;X)|\ll_\epsilon X^\epsilon
$$

uniformly, or at least for $X^{3/8}<D\le X^{1/2}$, with actual $\beta_h$ coefficients and frozen-coefficient conventions stated. This target does not imply `M9-M2` without a pointwise large-value theorem or direct endpoint control.

## Counterexample checks to run

1. **W-1 verification.** A3 should compute pair-sum window masses for toy active scales and compare actual absolute mass with

$$
MX^{1/4}-D^2X^\epsilon.
$$

2. **Fat-band threshold.** A3 should test the ratio

$$
\frac{\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)}{D^2}
$$

for $D=X^\delta$ with $\delta$ straddling $3/8$.

3. **UNC and TS checks.** A3 should enumerate the UNC and twin-shift families separately and verify their predicted $N$ formulas, parity, dyadic support, and mass scaling.

4. **Signed versus unsigned fat band.** A3 should compute signed $c_\chi$, unsigned analogue, random-sign analogue, and adversarial-sign analogue at endpoint toy scales.

5. **Interval URES strip count.** A2 and A3 should test U-3$\eta$ in the small-slope and degenerate branches, verifying the $\Delta$ term and the $1+\eta QD^2$ scaling.

6. **Complex-weight regression.** A3 should fix the test so that cosine pairing is expected to hold under shared complex $d$-weights, while the $\operatorname{Re}B_h$ shortcut fails.

7. **Poisson/B-process sanity.** A2 should compute the exact stationary point, $m$-range, amplitude, boundary terms, and endpoint cases for $D=X^\delta$ before proposing any theorem-level transform.

8. **Large-value theorem falsification.** A1/A4 should determine what large-value theorem would be needed to convert a signed global fourth moment to pointwise `M9-M2`, and whether known derivative/coherence constraints immediately rule out naive versions.

## Research strategy adjustment

Round 9 should pivot from the old absolute GNC route to a **signed upper-range program with a lower-range absolute subroute**.

Route comparison:

| Route | Status | Why keep it | Fast falsification |
|---|---:|---|---|
| Signed fat-band constant $c_\chi$ | Primary | It directly attacks the $D>X^{3/8}$ obstruction using $\chi_4(h)$ rather than absolute values. | A3 finds $|c_\chi|$ grows like a positive power and tracks unsigned/adversarial signs. |
| Absolute interval URES for $D\le X^{3/8}$ | Secondary | U-3$\eta$ gives real arithmetic infrastructure, and lower bounds do not yet disprove this restricted range. | A2/A4 construct a lower-bound family exceeding $D^2X^\epsilon$ below $X^{3/8}$. |
| Smooth Poisson/B-process | Backup | It may expose signed dual cancellation not visible in pair-sum energy. | Stationary phase plus endpoint terms reduce to unsigned-scale sums or no post-transform signed bound exists. |
| Global fourth moment plus derivative propagation | Rejected as sufficient | It gives only $D^{3/5}X^{3/20+\epsilon}$. | Already falsified for pointwise target by A1's calculation. |

The proof graph should now record that the absolute route is not merely "unproved" near the endpoint; it is **provably over budget** under H4 lower envelopes.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "M9-M2-interval-URES-strip-identity",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Interval URES strip identity",
        "status": "proved_internal",
        "statement_tex": "For reduced mu/Q != 0 and reduced nonzero fractions p1/q1, p3/q3 with q1,q3>0, if |p1/q1 + p3/q3 - mu/Q| <= eta, then |(mu q1 - Q p1)(mu q3 - Q p3) - Q^2 p1 p3| <= |mu| eta Q q1 q3. This is algebra only and gives no counting bound by itself.",
        "dependencies": [],
        "implies": [
          "M9-near-collision-taxonomy",
          "M9-near-collision-estimate"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A1-008-revision.md",
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "next_action": "Use this identity only as algebraic infrastructure; route any counting assertion through M9-M2-interval-URES-strip-count."
      },
      {
        "id": "M9-M2-interval-URES-strip-count",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Interval URES strip count with degenerate branch separated",
        "status": "proved_internal",
        "statement_tex": "For reduced mu/Q != 0, fixed nonzero p1,p3, Q <= 4D^2, |p_i| <= 2H_D, 0 <= eta <= 4X^(-1/4), and q_i in [1,2D] with gcd(p_i,q_i)=1, the number of pairs satisfying |p1/q1 + p3/q3 - mu/Q| <= eta is <<_epsilon X^epsilon (1 + eta QD^2) + Delta, where Delta <= 4D 1_{eta >= 1/(2D)} is the degenerate branch. This is a representation-strip count, not a full M2 near-collision estimate.",
        "dependencies": [
          "Divisor-bound-elementary",
          "M9-M2-interval-URES-strip-identity"
        ],
        "implies": [
          "M9-near-collision-taxonomy",
          "M9-near-collision-estimate"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A2.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Apply only with the stated nondegenerate/degenerate split; next assemble dyadic lifts and parity restrictions without losing the statement's hypotheses."
      },
      {
        "id": "M9-near-collision-absolute-lower-bounds",
        "type": "obstruction",
        "track": "M9_analytic",
        "title": "Absolute near-collision lower bounds obstruct endpoint GNC",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming H4 beta lower envelopes and exact N=0 mass closure, the old full-range absolute GNC target is false in upper dyadic ranges. The absolute graded estimate is refuted for large M in the UNC range, and the fat-band target Sigma_abs(0<|N|<=D^4/X) << D^2 X^epsilon is false for D >= X^(3/8+delta) by the W-1 window lower bound. These are obstructions to absolute or unsigned routes only, not to signed estimates.",
        "dependencies": [
          "H4",
          "H4-Phi-regularity",
          "M9-M2-beta-algebra",
          "M9-M2-exact-N0-total-mass"
        ],
        "implies": [
          "M9-near-collision-estimate",
          "M9-M2-local-fourth-moment-LFM",
          "M9-M2-LFM-endpoint-degeneracy"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md",
            "rounds/obligation-main/round_008/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Separate UNC, TS, and W-1 in the proof draft, including parity, dyadic support, beta lower envelope, and exact M,D,X ranges."
      },
      {
        "id": "M9-M2-signed-lift-cancellation-B1",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Signed dyadic lift cancellation for M2 pair weights",
        "status": "derived_under_assumptions",
        "statement_tex": "Under H4 beta algebra, Phi regularity, parity support, and suitable smooth or bounded-variation dyadic lift weights, the signed lift weight A_chi(p/q)=sum_{gq in [D,2D), 1<=|gp|<=H_D} beta_{gp,H_D} w_D(gq) satisfies a cancellation envelope of the form |A_chi(p/q)| << q/(D|p|) in the stated B1 regime. This is a pair-weight lemma only and does not prove M9-M2.",
        "dependencies": [
          "H4",
          "H4-Phi-regularity",
          "M9-M2-beta-algebra"
        ],
        "implies": [
          "M9-M2-character-factor",
          "M9-M2-signed-fat-band-constant"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Write the proof with exact weight smoothness, endpoint, parity, and Phi-regularity hypotheses; test whether this bound is strong enough for c_chi."
      },
      {
        "id": "M9-M2-signed-fat-band-constant",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Signed fat-band constant for M2 global fourth moment",
        "status": "proposed",
        "statement_tex": "Define the signed off-diagonal pair-sum constant c_chi(D;X) in the frozen-coefficient smoothed global fourth moment for S2(D;X). Prove |c_chi(D;X)| <<_epsilon X^epsilon uniformly, at least for X^(3/8)<D<=X^(1/2), or construct a signed lower-bound obstruction. This does not imply M9-M2 without a pointwise large-value theorem or direct endpoint estimate.",
        "dependencies": [
          "M9-M2-beta-algebra",
          "M9-M2-character-factor",
          "M9-M2-signed-lift-cancellation-B1",
          "M9-M2-fourth-moment-expansion",
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "implies": [
          "M9-M2-GM4-from-exact-plus-graded",
          "M9-near-collision-estimate"
        ],
        "blockers": [
          "H4-source-audit",
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md",
            "rounds/obligation-main/round_008/reviews/A2.md"
          ]
        },
        "owner": "A2",
        "next_action": "State the exact frozen-coefficient identity, define c_chi and its unsigned analogue, and prove a bound or produce signed diagnostic evidence showing failure."
      }
    ],
    "update": [
      {
        "id": "M9-near-collision-estimate",
        "status": "proposed",
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_008/responses/A1-008-revision.md",
            "rounds/obligation-main/round_008/responses/A2-008.md"
          ]
        },
        "next_action": "Replace the old full-range absolute GNC target. For D <= X^(3/8+o(1), audit restricted absolute or structured estimates using interval URES. For D > X^(3/8), pursue signed mechanisms such as c_chi or a sign-preserving Poisson/B-process estimate. Keep exact N=0, absolute lower bounds, signed estimates, and pointwise upgrade as separate obligations."
      },
      {
        "id": "M9-M2-GM4-from-exact-plus-graded",
        "status": "proposed",
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_008/responses/A1-008-revision.md",
            "rounds/obligation-main/round_008/responses/A4-008.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Do not use exact N=0 plus an absolute graded estimate to promote M9-M2. The absolute fat-band target is false for D > X^(3/8+delta), and a global L4 estimate plus crude derivative propagation gives only D^(3/5)X^(3/20+epsilon). Any viable route now needs signed fat-band control and a large-value or direct pointwise theorem."
      },
      {
        "id": "M9-M2-fourth-moment-average-to-pointwise",
        "status": "open",
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_008/responses/A1-008-revision.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Record the frozen-coefficient derivative obstruction: global L4 plus |S2'| << H_D gives only |S2(D;X0)| << D^(3/5) X^(3/20+epsilon), equal to X^(9/20+epsilon) at D=X^(1/2). Require a stronger large-value theorem, local signed cancellation theorem, or direct signed pointwise estimate."
      },
      {
        "id": "M9-M2-exact-N0-total-mass",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_008/responses/A1-008-revision.md"
          ]
        },
        "next_action": "Keep exact N=0 closure scoped strictly to exact resonances and conditional on H4. Use it in lower-bound subtraction only with H4 and beta-envelope dependencies visible."
      },
      {
        "id": "M9-M2-URES-representation-divisor-bound",
        "status": "proved_internal",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Transcribe the exact divisor factorization and its interval analogue into the lemma bank with notation Q reserved consistently."
      },
      {
        "id": "M9-M2-URES-energy-reduction",
        "status": "proved_internal",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Record the ordered-pair convention for R_res(r) and distinguish absolute R from signed R_chi."
      },
      {
        "id": "M9-M2-unpaired-residual-URES",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Treat exact URES residual as conditionally settled under H4. For near-collisions, use interval URES strip identity/count and keep degenerate branches separate."
      },
      {
        "id": "M9-M2-character-factor",
        "status": "open",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_008/responses/A4-008.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Use the signed lift-cancellation B1 lemma and c_chi target to preserve the chi_4(h) structure in upper-range near-collision analysis. Do not use character-blind absolute norms past D=X^(3/8)."
      },
      {
        "id": "M9-fourth-moment-enumeration",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_008/responses/A3-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Execute diagnostics with exact integer N, corrected complex-weight regression, c_chi and unsigned analogues, UNC/TS/W-1 family checks, D around X^(3/8), endpoint D=X^(1/2), precision logs, command line, tables, and report. Keep output diagnostic_only."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_008/responses/A3-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Correct the complex-weight test: cosine pairing can hold for shared complex d-weights, while the Re B_h shortcut fails. Execute and archive script, command, table, precision log, and report."
      },
      {
        "id": "H4-source-audit",
        "status": "source_audit_required",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_008/responses/A1-008.md",
            "rounds/obligation-main/round_008/reviews/A1.md"
          ]
        },
        "next_action": "Finalize sources/vaaler_1985.md with DOI, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, beta lower envelope, and M2 parity support."
      }
    ],
    "reject": [
      {
        "id": "A1-R8-global-GNC-low-for-all-D",
        "reason": "Rejected as a global all-D target because A4's W-1 lower bound refutes the fat-band case for D > X^(3/8+delta). It may be replaced only by a restricted lower-D, structured, or signed target."
      },
      {
        "id": "A1-R8-full-range-GNC-Abs",
        "reason": "Rejected over the full support. A1's full-support mass calculation and A4's lower-bound families show the old full-range absolute cumulative estimate is false."
      },
      {
        "id": "A2-R8-M9-M2-absolute-mass-obstruction-proved-internal",
        "reason": "Rejected at proved_internal status because A2's uniform-distribution heuristic is not a proof. The obstruction conclusion should be recorded only as H4-dependent and based on A4's explicit UNC, TS, and W-1 lower bounds."
      },
      {
        "id": "A2-R8-URES-interval-factorization-as-written",
        "reason": "Rejected as written because the target pair-sum sign convention must be corrected. Use the A1/A4 integer-defect formulation and separate the degenerate uv=0 branch."
      },
      {
        "id": "A2-R8-Poisson-B-Process-Transform-proved",
        "reason": "Rejected as proved. The leading stationary-phase calculation lacks full boundary, m=0, support-edge, nonstationary, smoothing/unsmoothing, and post-transform signed-sum estimates."
      },
      {
        "id": "A3-R8-diagnostics-as-proof",
        "reason": "Rejected because computations are diagnostic_only and require executed artifacts before even diagnostic evidence is positive."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform pointwise estimates for both M1 and M2 were proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 8 did not provide an M1 estimate."
      },
      {
        "id": "M9-M2",
        "reason": "The round produced obstruction and signed targets, not a pointwise M2 endpoint bound."
      },
      {
        "id": "M9-endpoint-uniformity",
        "reason": "Endpoint D=X^(1/2) remains the hardest range; signed upper-range control is still open."
      },
      {
        "id": "GC-target",
        "reason": "The final theorem remains conditional on open M9 and H4 source audit."
      },
      {
        "id": "Conditional-bridge",
        "reason": "The bridge remains conditional; no downstream endpoint estimate changed status."
      },
      {
        "id": "H4",
        "reason": "H4 remains source_audit_required until the source card is completed and validated."
      },
      {
        "id": "R5-Full",
        "reason": "Round 8 did not alter R5-Full."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a guardrail and source-audit obligation, not a proof dependency."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "idea_quality_score": 8,
    "state_evidence_score": 7,
    "calibration_score": 8,
    "reason": "Round 8 makes real proof-graph-safe progress by refuting the old absolute near-collision route in upper dyadic ranges, adding interval URES strip infrastructure, and defining the signed fat-band target. It does not prove M9, M9-M2, M9-M1, H4, or the Gauss circle endpoint."
  }
}

## Next-round prompts by agent

### For A1

Primary objectives:

1. Write the Round 9 proof-draft update reflecting the route bifurcation:
   - exact $N=0$ arm remains conditionally closed under H4;
   - absolute near-collision estimates are refuted for $D>X^{3/8+\delta}$ in the fat band;
   - absolute/structured estimates remain only a lower-range or class-restricted subroute;
   - signed $c_\chi$ becomes the upper-range primary target.

2. Complete `H4-source-audit` if possible. The source card must include Vaaler 1985 metadata, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, endpoint convention, $\Phi$ regularity, beta lower envelope, and M2 parity support.

3. Formalize the pointwise upgrade gap:
   - restate A1's derivative obstruction;
   - define the exact large-value theorem needed after a signed global moment;
   - specify separated points, threshold $V$, active $D$, and what bound would imply $V\ll X^{1/4+\epsilon}$.

4. Audit the State Patch after validation. If `M9-M2-interval-URES-strip-count` is accepted, insert it as a scoped arithmetic lemma, not as a near-collision theorem.

Exploratory allocation: formulate one signed large-sieve or spacing theorem that would imply the $c_\chi$ bound, with an immediate falsification test.

### For A2

Primary objectives:

1. Audit A4's lower-bound families in proof-detail:
   - UNC large-$M$ family;
   - TS twin-shift family;
   - W-1 window/pigeonhole lower bound;
   - parity, dyadic support, $N\ne0$, $1\le |h_i|\le H_D$, beta lower envelope, and exact $M,D,X$ ranges.

2. Replace the A2 heuristic absolute-mass obstruction with the W-1 proof. Do not label any heuristic uniform-distribution argument as `proved_internal`.

3. Audit the interval URES count:
   - verify the integer-defect convention;
   - verify nondegenerate $uv\ne0$ divisor count;
   - verify the degenerate $uv=0$ branch;
   - decide how the degenerate branch maps into paired or participation-degenerate fourth-moment classes.

4. Work on `M9-M2-signed-fat-band-constant`:
   - define $c_\chi(D;X)$ precisely;
   - state the required signed bound;
   - identify whether B-1 signed lift cancellation is strong enough, or what additional cancellation is needed.

Exploratory allocation: keep Poisson/B-process only as a backup. Supply a full theorem-shaped stationary-phase statement if pursuing it; otherwise do not promote it.

### For A3

Primary objectives:

1. Execute diagnostics, not just specify them. Required artifacts:
   - script path;
   - `python -m py_compile` log;
   - exact command;
   - Python/package versions;
   - precision settings;
   - exact dyadic convention;
   - output tables;
   - `report.md`;
   - pass/fail assertions.

2. Prioritize diagnostics that match the new $X^{3/8}$ split:
   - compute $\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)/D^2$ for $D=X^\delta$ around $\delta=3/8$;
   - compare with W-1 lower-bound prediction $D^4X^{-3/4}$;
   - test UNC and TS formula families separately.

3. Compute signed objects:
   - $c_\chi(D;X)$;
   - unsigned analogue;
   - random-sign analogue;
   - adversarial-sign analogue;
   - endpoint $D\asymp X^{1/2}$ sign ratios.

4. Fix formula regressions:
   - cosine pairing may hold for shared complex $d$-weights;
   - $\operatorname{Re}B_h$ shortcut should fail for complex weights;
   - exact integer arithmetic must be used for $N$ and rational identities.

Exploratory allocation: implement U-3$\eta$ strip enumeration, including the degenerate branch, to compare empirical counts with $X^\epsilon(1+\eta QD^2)+\Delta$.

### For A4

Primary objectives:

1. Formalize `M9-M2-signed-fat-band-constant` in lemma-bank style:
   - define the smoothed global fourth moment;
   - define signed pair weights;
   - define $c_\chi(D;X)$;
   - state all frozen-coefficient and smooth-weight hypotheses;
   - isolate diagonal/exact $N=0$ and off-diagonal contributions.

2. Expand B-1:
   - state exact assumptions on $\Phi$, $w_D$, parity, and endpoint support;
   - prove the signed lift bound with constants and error terms;
   - state clearly whether it is enough for $c_\chi$ or only a first saving.

3. Separate lower-bound families:
   - write UNC, TS, and W-1 as standalone obstruction lemmas;
   - specify which one refutes large-$M$ GNC and which one refutes the fat band;
   - include exact ranges and beta lower-envelope dependencies.

4. If time remains, attempt the lower-range absolute upper half:
   - for $D\le X^{3/8}$, decide whether U-3$\eta$ plus lift bookkeeping can prove a restricted absolute estimate;
   - isolate any class where the bound fails.

Exploratory allocation: examine whether the sign-preserving Poisson route and $c_\chi$ route are actually the same dual obstruction in different variables.

## Round Assessment

Agent scores:

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 7.0 | 8.5 | Strong normalization and derivative-propagation obstruction; correctly rejected full-range GNC. The low-band target needed the W-1 correction and must now be $D$-restricted or signed. |
| A2 | 7.5 | 4.0 | 5.5 | Useful obstruction pressure and Poisson exploration, but over-promoted heuristic and transform claims. Needs to replace heuristics with A4's explicit lower-bound proof. |
| A3 | 7.0 | 2.5 | 7.5 | Good diagnostic design and formula-awareness, but no executed evidence yet. Must run code and target the new $X^{3/8}$ split. |
| A4 | 9.5 | 8.5 | 8.5 | Round's strongest contribution: U-3$\eta$ strip count, W-1 fat-band refutation, signed lift direction, and $c_\chi$ target. H4 dependencies and signed-bound gaps remain. |

State evidence is substantial for arithmetic infrastructure and obstruction, but not for endpoint estimates. The `mathematical_progress_score` is kept at 6 because the round narrows the proof graph and rejects a false route but does not prove `M9-M2`.

## Confidence

Confidence: 0.84.

High confidence:
- Full-range absolute GNC-Abs is false.
- Absolute fat-band target fails for $D>X^{3/8+\delta}$ under H4 lower envelopes.
- Global $L^4$ plus crude derivative propagation cannot yield pointwise `M9-M2`.
- `M9`, `M9-M1`, `M9-M2`, `GC-target`, and H4 must remain unpromoted.

Moderate confidence:
- U-3$\eta$ is state-promotable as a scoped arithmetic strip count.
- B-1 signed lift cancellation is useful after H4/Phi audit.
- $c_\chi$ is the right primary upper-range target.

Low confidence:
- The lower-range absolute estimate for $D\le X^{3/8}$ is true.
- The signed fat-band constant can be bounded by current methods.
- A smooth Poisson/B-process route can reach the endpoint without a new signed spacing theorem.