## Summary

This synthesis treats the uploaded Round 3 packet, including the round-local human audits and the A1/A2/A3 Stage A and Stage B materials, as the authoritative context for this stage.

Round 3 made useful normalization and diagnostic progress, but no proof-level progress on `M9`, `M9-M2`, or the Gauss circle endpoint. The accepted mathematical updates are narrow:

- accept A1's $\mathcal M_2$ algebra under the unresolved H4 source audit;
- accept A3's materialized diagnostics only as `diagnostic_only` evidence;
- reject A2's promotions of exact $N=0$ taxonomy and diagonal-core estimates;
- keep `M9`, `M9-M1`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open;
- add a formal R5-Full reconciliation audit, as required by the human steering notes.

Primary route for the next round: continue the signed fourth-moment program for $\mathcal M_2$, but narrow it to one exact weighted subfamily, preferably the denominator-paired exact $N=0$ family. Backup route: a direct signed bilinear or CRI-style estimate, not A2's current exponent-pair/Poisson proof sketch.

## Selected main route

### Primary route: signed fourth moment for $\mathcal M_2$ with exact weighted resonance control

Keep the current proof framework:

$$
P(X)=N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola}
\longrightarrow
\text{floor-compatible sawtooth}
\longrightarrow
\text{finite Vaaler}
\longrightarrow
\text{fixed-coefficient reciprocal main sums}.
$$

The conditional bridge remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This bridge is not promoted because `M9` remains open.

The primary analytic object is

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
H_D\asymp D X^{-1/4}.
$$

A sufficient target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

The fourth-moment phase has cleared numerator

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

The first exact proof target is not the full taxonomy. It is the denominator-paired weighted bound described below.

### Exact lemma needed for the primary route

Prove a weighted denominator-paired exact-resonance estimate. In the subfamily

$$
d_1=d_2=a,
\qquad
d_3=d_4=b,
$$

the resonance condition becomes

$$
(h_1-h_2)b+(h_3-h_4)a=0.
$$

The needed lemma is:

$$
\sum_{\substack{
a,b\asymp D\\
1\le |h_i|\le H_D\\
(h_1-h_2)b+(h_3-h_4)a=0
}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\prod_{j=1}^4 |w_D(d_j)|
\ll_\epsilon X^{1+\epsilon},
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$, preferably with the sharper expected scale $\ll_\epsilon D^2X^\epsilon$ if true.

### Why this route remains primary

It directly attacks the actual obstruction in `M9-M2-character-factor`: standard $h$-Cauchy replaces $C_h$ by $|C_h|^2=4\,1_{2\nmid h}$ and loses the $\chi_4(h)$ sign. The fourth moment retains the fourfold product of actual coefficients longer than second-moment arguments do.

It is also the best aligned route with the human strategy merge: `strategy-revised1.md` is the primary mathematical workstream, while `strategy-revised4.md` supplies audit guardrails. The broad AI/ML pivot from `strategy-revised2.md` remains exploratory backlog only.

### Primary route falsification criterion

This route should be downgraded if A3's scaled exact enumeration with the true Vaaler $\Phi$ and high precision shows that denominator-paired or unclassified exact $N=0$ mass grows above the $X^{1+o(1)}$ fourth-moment scale without compensating signed cancellation, or if A2 proves a lower-bound construction showing that the actual $\beta_h$ weights cannot suppress that mass.

### Backup route: direct signed bilinear or CRI route

The backup route is not A2's current exponent-pair proof sketch. It is a precisely formulated signed bilinear estimate that preserves $\beta_h$ until the last step:

$$
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}.
$$

A concrete CRI diagnostic version splits positive odd $h$ into $h\equiv1,3\pmod4$ and studies

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}.
$$

This route attacks the same sign-loss obstruction without relying on a full fourth-moment taxonomy. It is the correct backup because it is falsifiable by A3 and does not require accepting A2's unproved exponent-pair and Poisson claims.

### Backup route falsification criterion

If the first rigorous Cauchy, large-sieve, operator-norm, or spacing step transforms the signed statistic into a diagonal conjugation

$$
v^*U^*KUv
$$

and then estimates by an absolute-value, Frobenius, Schur, Gershgorin, trace, or operator-norm bound, the route has lost the character and should be treated as sign-blind. A3 should compare signed, unsigned, and adversarial-coefficient statistics at endpoint blocks.

## Useful fragments by source

### From A1

A1 supplied the most reliable proof-infrastructure contribution.

Accept under H4:

$$
C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h},
$$

and

$$
\beta_{h,H}
=
\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Thus $\beta_{-h,H}=\beta_{h,H}$ is real and even. This is algebraically sound, but depends on the H4 Vaaler coefficient convention.

Accept A1's raw two-sided formula:

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Accept A1's paired real formula only under the real-weight hypothesis:

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Also accept A1's narrow pair-equality core bound: the two pair-equality exact resonance families contribute $\ll D^2\le X$. This is not the full `M9-M2-N0-diagonal-core-bound`.

### From A2

A2's useful contributions are strategic and diagnostic, not state-promotable proof evidence.

Useful:

- A2 kept focus on the exact resonance equation
  $h_1/d_1+h_3/d_3=h_2/d_2+h_4/d_4$.
- A2 correctly emphasized that denominator-paired and semi-diagonal families are dangerous.
- A2's unweighted denominator-paired count heuristic, roughly $D^4X^{-3/4}\log D$ and $X^{5/4}\log X$ at $D=X^{1/2}$, is a valuable stress test. It should not be recorded as a proved theorem without a complete count.
- A2's Gallagher derivative-loss discussion is a warning about a continuous-relaxation route, not a route-closing theorem.
- A2's direct bilinear/exponent-pair idea remains a backup route only after being rewritten with exact theorem hypotheses.

Rejected:

- total exact $N=0$ mass $O(D^2)$ is not proved;
- denominator-paired mass $O(D\log^4 X)$ is not proved;
- taxonomy is not resolved;
- the direct exponent-pair/Poisson route does not prove `M9-M2`.

### From A3

A3 produced useful computation-track progress. The human Stage A audit reports that the diagnostic bundle was materialized and executed locally, producing:

- `outputs/table_small.csv`;
- `computations/m9_regression/precision.log`;
- `computations/m9_regression/report.md`;
- round-local archive copies under `rounds/obligation-main/round_003/artifacts/m9_regression/`.

Accept these only as `diagnostic_only` evidence.

Most important diagnostic: the finite table has nonzero `N0_unclass` mass, reported as `0.0127084` in the human audit. Therefore the exact $N=0$ taxonomy is not resolved.

A3 should next replace provisional coefficient code with the true Vaaler $\Phi$ after H4 source audit and scale the exact $N=0$ and near-collision tables.

### Human steering and strategy notes

The merged strategy notes give the correct combined stance:

- use `strategy-revised1.md` as the primary analytic program;
- use `strategy-revised4.md` as proof-hygiene and R5 audit overlay;
- keep `strategy-revised2.md` as exploratory backlog only.

The R5-Full disagreement should be resolved conservatively. Do not downgrade R5-Full merely because earlier H5r/DDP-trap concerns existed. Do not treat it as fully settled merely because later product-count arguments appear to work. Add an explicit reconciliation obligation.

### External source status

Vaaler's paper is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12(2), 183--216, April 1985. Project Euclid and AMS identify the article metadata.

The local Vaaler PDF includes Theorem 6, equation (2.28), giving the Fourier transform of $J$ as

$$
\widehat J(t)=\pi t(1-|t|)\cot(\pi t)+|t|,\qquad 0<|t|<1,
$$

and Theorem 18 supplies the periodic sawtooth approximation and Fejer residual majorant.

Li--Yang's arXiv page identifies Xiaochun Li and Xuerui Yang's paper as using the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results. The local PDF states their Theorem 1.2 with exponent $\theta^*=0.314483\cdots$ and explicitly discusses the apparent $5/16$ barrier for existing methods. This is guardrail evidence only; Li--Yang is not imported as a black-box theorem for endpoint `M9`.

## Rejected or risky ideas

1. **Reject A2's promotion of `M9-M2-N0-diagonal-core-bound` to `proved_internal`.** The total exact $N=0$ additive-energy estimate is not proved.

2. **Reject A2's promotion of `M9-near-collision-taxonomy` to a resolved or derived status.** The finite diagnostics have nonzero unclassified exact mass, and no complete taxonomy is supplied.

3. **Reject A2's denominator-paired negligibility claim.** The proposed $O(D\log^4X)$ bound is not established by a complete gcd summation with all singular cases.

4. **Reject A2's direct exponent-pair/Poisson route as proof of `M9-M2`.** It lacks a named theorem convention, exact derivative parameters, boundary terms, outer $h$-sum handling, actual $\beta_h$ weights, and endpoint uniformity. Its endpoint dual-length claim is also suspect: for a fixed $h$, the dual length is $m\asymp hX/D^2$, giving $m\asymp X^{1/4}$ at $D=X^{1/2}$ and $h\asymp H_D$, not length $1$.

5. **Reject a route-closing Gallagher obstruction.** The derivative penalty is a warning about one continuous extraction method, not a theorem ruling out discrete fourth moments, signed bilinear estimates, or CRI.

6. **Reject black-box Li--Yang/Bombieri--Iwaniec import.** The theorem hypotheses, ranges, weights, and absolute-value placement remain unaudited for the exact M9 endpoint.

7. **Reject treating A3 computations as theorem evidence.** They support formula normalization and obstruction search only.

8. **Reject broad AI/ML optimization as a current proof direction.** It may remain in a backlog, but it has no theorem-level bridge to `M9`.

## Known gaps

1. **H4 source audit.** The source card still needs rendered page and equation checks for Vaaler's Theorem 6, Section 7 definitions, Theorem 18, coefficient sign, residual constant, Fejer normalization, and integer convention.

2. **R5-Full reconciliation.** The proof draft must reconcile older H5r/DDP-trap concerns with the later product-count proof. The correct order of operations appears to be: use the positive Fejer majorant before Fourier expansion, then reduce to product/divisor counts. This must be written explicitly.

3. **Best proof draft remains missing.** `best_proof_draft.md` is still not carrying the accepted H1-H4, R5-Full, M9, and blocker definitions.

4. **Full exact $N=0$ taxonomy.** Pair-equality exact resonances are controlled, but denominator-paired, semi-diagonal, mixed, truncation-edge, and unclassified exact resonances remain open.

5. **Weighted denominator-paired bound.** The next proof must exploit actual reciprocal $\beta_h$ weights, not only unweighted counts.

6. **Near-collision estimate.** The project still lacks an exact theorem for

$$
0<|N|\lesssim D^4/X.
$$

7. **Endpoint uniformity.** All estimates must hold uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

8. **M1 remains untouched analytically.** The round focused on $\mathcal M_2$ normalization and diagnostics. `M9-M1` remains open.

9. **Computation still provisional.** A3's tests must be rerun with true Vaaler $\Phi$, official formulas, high precision, exact resonance handling, and larger tables.

10. **Complex-weight paired formula.** A1's real-weight paired formula is correct under real weights. For complex weights, the exact positive-$h$ paired implementation should use the cosine form

$$
4\sum_{h=1}^{H_D}\beta_h
\sum_d w_D(d)\left(e(hX/(4d))+e(-hX/(4d))\right)
=
8\sum_{h=1}^{H_D}\beta_h
\sum_d w_D(d)\cos(2\pi hX/(4d)),
$$

provided the same complex weight $w_D(d)$ is used in both $h$ and $-h$ raw terms. This should be tested by A3.

## New lemmas to add

### Lemma 1: weighted denominator-paired exact-resonance bound

**Status:** open.

Statement:

For $X^{1/4}\le D\le X^{1/2}$, $H_D\asymp DX^{-1/4}$, bounded dyadic weights $w_D$, and actual H4-dependent $\beta_h$ coefficients,

$$
\sum_{\substack{
a,b\asymp D\\
1\le |h_i|\le H_D\\
(h_1-h_2)b+(h_3-h_4)a=0
}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\prod_{j=1}^4 |w_D(d_j)|
\ll_\epsilon X^{1+\epsilon}.
$$

This lemma is the first nontrivial exact $N=0$ subcase after pair-equality.

### Lemma 2: exact complex-weight cosine pairing for $\mathcal M_2$

**Status:** derived algebraically under H4, but only an implementation formula.

If the same complex dyadic weight appears in the $h$ and $-h$ raw terms and $\beta_{-h}=\beta_h$, then

$$
\sum_{1\le |h|\le H}\beta_h\sum_d w(d)e(hX/(4d))
=
2\sum_{h=1}^H\beta_h\sum_d w(d)\cos(2\pi hX/(4d)).
$$

For real weights this equals the $\operatorname{Re}B_h$ formula. For complex weights it does not equal $\operatorname{Re}B_h$ in general.

### Lemma 3: signed bilinear M2 backup lemma

**Status:** proposed.

Prove, with exact coefficient hypotheses and a named theorem or new signed-spacing estimate,

$$
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over active $D$.

The first step is not to apply exponent pairs informally; it is to freeze the exact matrix, spacing norm, or bilinear form whose bound would imply the lemma.

### Lemma 4: R5-Full reconciliation audit

**Status:** open proof-infrastructure task.

Compare the old H5r/DDP-trap analysis with the later R5-Full product-count proof. Write either the accepted proof with all edge cases or a downgrade proposal. This is an audit obligation, not a downgrade by itself.

## Counterexample checks to run

1. **Denominator-paired exact $N=0$ stress test.** Enumerate $d_1=d_2=a$, $d_3=d_4=b$ with exact resonance equation, and report unweighted count, absolute weighted mass, signed mass, and mass normalized by $D^2$ and $X$.

2. **Unclassified exact $N=0$ scaling.** Repeat A3's `N0_unclass` binning for increasing $H$ and $D$ after H4. Track whether unclassified mass is stable, grows like $D^2$, or exceeds fourth-moment scale.

3. **Near-collision band test.** Bin

$$
0<|N|\le cD^4/X
$$

for several constants $c$ and active endpoint/intermediate dyadic scales.

4. **R5 residual exact-resonance tests.** Test first leg and shifted legs $\rho=1,3$ for square, near-square, nonsquare, and divisor-rich $X$, with exact resonance and nearest-integer tie handling.

5. **Complex-weight pairing regression.** Verify that the generalized cosine pairing matches the raw two-sided formula for complex weights, while the $\operatorname{Re}B_h$ formula fails as expected.

6. **CRI and signed bilinear falsification.** Compare fixed $\beta_h$ signs against unsigned and adversarial coefficient variants. If signed statistics track unsigned statistics, deprioritize the backup route.

7. **Poisson/B-process dual-length check.** For $D=X^\delta$, verify the dual length

$$
m\asymp hX/D^2
$$

and record endpoint behavior at $D=X^{1/2}$.

## Research strategy adjustment

The next round should not attempt another broad taxonomy essay. It should produce one proof-level sublemma or a clear falsification.

Allocation:

- about 60% to the primary $\mathcal M_2$ fourth-moment route, specifically the denominator-paired weighted exact-resonance subcase;
- about 25% to H4/R5 proof-draft and source-audit hygiene;
- about 15% to diagnostic computation and the direct signed bilinear backup.

Do not pivot `obligation-main` to an incremental-exponent goal unless the project owner explicitly changes the objective. Do not let Li--Yang, B-process, ML/optimization, or spectral alternatives affect the proof graph without exact theorem statements and bridges to `M9`.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "R5-Full-reconciliation",
        "type": "infrastructure",
        "track": "proof_infrastructure",
        "title": "R5-Full product-count reconciliation audit",
        "status": "open",
        "statement_tex": "Reconcile the older H5r/DDP-trap analysis with the later R5-Full product-count proof. The accepted outcome must either write the Fejer residual product-count proof with all edge cases or give a validator-ready downgrade proposal.",
        "dependencies": [
          "R5-Full",
          "H4",
          "H4-source-audit"
        ],
        "implies": [
          "R5-Full",
          "Conditional-bridge"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_003/human/00-strategy-evaluations-judge-merge.md",
            "rounds/obligation-main/round_003/human/strategy-revised4-audit.md",
            "rounds/obligation-main/round_003/human/strategy-revised-judge-merge.md"
          ]
        },
        "owner": "A1",
        "next_action": "Compare the older H5r/DDP-trap concern with the later R5-Full-R18 through R5-Full-R27 product-count entries, then write the accepted proof or downgrade proposal into best_proof_draft.md."
      },
      {
        "id": "M9-M2-denominator-paired-weighted-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Weighted denominator-paired exact M2 resonance bound",
        "status": "open",
        "statement_tex": "For X^(1/4) <= D <= X^(1/2), H_D asymp D X^(-1/4), actual beta_h coefficients, and bounded dyadic weights, the exact N=0 subfamily d_1=d_2=a, d_3=d_4=b, equivalently (h_1-h_2)b+(h_3-h_4)a=0, has total absolute beta-weighted fourth-moment mass <<_epsilon X^(1+epsilon), preferably <<_epsilon D^2 X^epsilon if true.",
        "dependencies": [
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion",
          "H4"
        ],
        "implies": [
          "M9-M2-N0-diagonal-core-bound",
          "M9-near-collision-taxonomy"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_003/responses/A2-003.md",
            "rounds/obligation-main/round_003/reviews/A1.md",
            "rounds/obligation-main/round_003/reviews/A2.md",
            "rounds/obligation-main/round_003/reviews/A3.md",
            "rounds/obligation-main/round_003/human/stage-b-review-audit.md"
          ]
        },
        "owner": "A2",
        "next_action": "Prove the weighted gcd-sum bound with actual beta_h weights, signs, equality cases h_i=h_j, truncation edges, and uniformity in D; otherwise provide a counterexample or downgrade."
      },
      {
        "id": "M9-M2-direct-signed-bilinear-lemma",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Direct signed bilinear estimate for M2",
        "status": "proposed",
        "statement_tex": "A direct signed bilinear estimate for S_2(D;X)=sum_{1<=|h|<=H_D} beta_{h,H_D} sum_{d asymp D} w_D(d)e(hX/(4d)) giving S_2(D;X) <<_epsilon X^(1/4+epsilon) uniformly over X^(1/4)<=D<=X^(1/2), without erasing the chi_4 frequency sign by character-blind norms.",
        "dependencies": [
          "M9-M2-beta-algebra",
          "M9-M2-character-factor",
          "M9-endpoint-uniformity"
        ],
        "implies": [
          "M9-M2"
        ],
        "blockers": [],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_003/responses/A1-003.md",
            "rounds/obligation-main/round_003/responses/A2-003.md",
            "rounds/obligation-main/round_003/reviews/A1.md",
            "rounds/obligation-main/round_003/reviews/A3.md"
          ]
        },
        "owner": "A2",
        "next_action": "Rewrite as a precise theorem with coefficient class, dyadic ranges, exact bilinear or spacing norm, named external theorem if used, and a fast falsification test comparing signed and unsigned statistics."
      }
    ],
    "update": [
      {
        "id": "M9-M2-beta-algebra",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_003/responses/A1-003.md",
            "rounds/obligation-main/round_003/reviews/A2.md",
            "rounds/obligation-main/round_003/reviews/A3.md"
          ]
        },
        "next_action": "After H4 source audit, insert the beta_h algebra, raw two-sided formula, paired real formula, and complex-weight cosine pairing into best_proof_draft.md."
      },
      {
        "id": "M9-M2-fourth-moment-expansion",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_003/responses/A1-003.md",
            "rounds/obligation-main/round_003/reviews/A2.md",
            "rounds/obligation-main/round_003/reviews/A3.md"
          ]
        },
        "next_action": "Use the expansion only as algebraic infrastructure for exact N=0 and near-collision estimates; do not infer an analytic bound without weighted mass estimates."
      },
      {
        "id": "M9-M2-N0-diagonal-core-bound",
        "status": "open",
        "blockers_added": [
          "M9-M2-denominator-paired-weighted-bound"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_003/responses/A1-003.md",
            "rounds/obligation-main/round_003/responses/A2-003.md",
            "rounds/obligation-main/round_003/reviews/A1.md",
            "rounds/obligation-main/round_003/reviews/A3.md"
          ]
        },
        "next_action": "Keep the narrow pair-equality O(D^2) calculation as a subclaim only. Prove the denominator-paired and semi-diagonal weighted masses with actual beta_h weights before promoting the full diagonal-core obligation."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "blockers_added": [
          "M9-M2-denominator-paired-weighted-bound"
        ],
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_003/human/stage-a-response-audit.md",
            "rounds/obligation-main/round_003/human/stage-b-review-audit.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_003/responses/A2-003.md",
            "rounds/obligation-main/round_003/artifacts/m9_regression/report.md"
          ]
        },
        "next_action": "Preserve the unclassified exact N=0 class. First prove or refute the denominator-paired weighted bound, then define semi-diagonal and mixed families with exact equations and mass bounds."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "diagnostic_only",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_003/artifacts/m9_regression/run.py",
            "rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv",
            "rounds/obligation-main/round_003/artifacts/m9_regression/precision.log",
            "rounds/obligation-main/round_003/artifacts/m9_regression/report.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_003/responses/A3-003.md",
            "rounds/obligation-main/round_003/human/stage-a-response-audit.md",
            "rounds/obligation-main/round_003/human/stage-b-review-audit.md"
          ]
        },
        "next_action": "After H4 source audit, rerun with the exact Vaaler Phi, official raw M1/M2 formulas, high precision, complex-weight cosine pairing, larger exact N=0 tables, and near-collision bins. Keep all output diagnostic_only."
      },
      {
        "id": "R5-Full",
        "status": "derived_under_assumptions",
        "blockers_added": [
          "R5-Full-reconciliation"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_003/human/00-strategy-evaluations-judge-merge.md",
            "rounds/obligation-main/round_003/human/strategy-revised4-audit.md"
          ]
        },
        "next_action": "Do not downgrade solely from strategy skepticism. Complete R5-Full-reconciliation and H4 source audit, then insert the product-count proof with all edge cases into best_proof_draft.md."
      },
      {
        "id": "H4-source-audit",
        "status": "source_audit_required",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_003/responses/A1-003.md",
            "rounds/obligation-main/round_003/reviews/A3.md"
          ]
        },
        "next_action": "Verify from rendered Vaaler pages: Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, Fejer normalization, residual constant, and integer endpoint convention."
      },
      {
        "id": "M9-M2",
        "status": "open",
        "blockers_added": [
          "M9-M2-denominator-paired-weighted-bound"
        ],
        "next_action": "Retain the two-sided convention and actual beta_h weights. Attack the denominator-paired weighted exact-resonance sublemma first; keep direct signed bilinear estimates as backup only."
      }
    ],
    "reject": [
      {
        "id": "A2-R3-total-exact-N0-OD2-proof-promotion",
        "reason": "Rejected because the asserted total additive-energy estimate for exact N=0 resonances is not proved and is challenged by the Stage B reviews."
      },
      {
        "id": "A2-R3-near-collision-taxonomy-resolved",
        "reason": "Rejected because the exact N=0 taxonomy is not resolved and Round 3 diagnostics report nonzero unclassified exact N=0 mass."
      },
      {
        "id": "A2-R3-denominator-paired-negligibility-proved",
        "reason": "Rejected because the claimed O(D log^4 X) denominator-paired estimate lacks a complete gcd-sum proof with actual beta_h weights and singular cases."
      },
      {
        "id": "A2-R3-Gallagher-derivative-route-closing",
        "reason": "Rejected as a route-closing theorem. The derivative-loss calculation is a diagnostic for one continuous relaxation, not a proof that discrete fourth moments or signed bilinear methods fail."
      },
      {
        "id": "A2-R3-direct-exponent-pair-M2-proof",
        "reason": "Rejected because the exponent-pair/Poisson sketch lacks exact theorem hypotheses, derivative scales, boundary terms, coefficient treatment, outer h-sum handling, and endpoint uniformity."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform endpoint estimate for both M1 and M2 was proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 3 did not supply an analytic estimate for M1."
      },
      {
        "id": "M9-near-collision-estimate",
        "reason": "The near-collision theorem is still not formulated with exact coefficient weights, ranges, and proof."
      },
      {
        "id": "M9-endpoint-uniformity",
        "reason": "Every proposed estimate still needs explicit uniformity for X^(1/4)<=D<=X^(1/2)."
      },
      {
        "id": "GC-target",
        "reason": "The final Gauss circle target remains conditional because M9 is open."
      },
      {
        "id": "H4",
        "reason": "H4 remains source_audit_required until the rendered Vaaler theorem and notation translation are completed."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a guardrail; no theorem is imported as a black-box dependency for endpoint M9."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 4,
    "idea_quality_score": 7,
    "state_evidence_score": 5,
    "calibration_score": 6,
    "reason": "Round 3 improved M2 algebra, route selection, and diagnostic evidence, and it created a sharper denominator-paired target. It did not prove M9, resolve exact N=0 taxonomy, or close any endpoint estimate."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `H4-source-audit`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, and proof-draft consolidation.

Objectives:

1. Complete the rendered-source H4 audit from Vaaler 1985. Verify:
   - Theorem 6, equation (2.28), for $\widehat J(t)$;
   - Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, equations (7.13)--(7.17), especially (7.14);
   - coefficient sign in
$$
     \alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h};
$$
   - residual constant $(2H+2)^{-1}$;
   - Fejer normalization;
   - integer endpoint convention.

2. Write `R5-Full-reconciliation` into `best_proof_draft.md`. Compare the old H5r/DDP-trap concern with the product-count proof. The output must state exactly why using the positive Fejer majorant before Fourier expansion avoids the older arbitrary-coefficient trap, or else propose a downgrade.

3. Insert into `best_proof_draft.md`:
   - H1-H3 statement;
   - H4 statement, still source-audit-dependent;
   - R5-Full proof or reconciliation gap;
   - conditional bridge;
   - official M9 definitions;
   - $\mathcal M_2$ raw two-sided, paired real, and complex-weight cosine formulas;
   - fourth-moment numerator $N$;
   - open blockers.

4. State the first near-collision theorem exactly:
$$
   0<|N|\lesssim D^4/X
$$
   with coefficient weights, dyadic ranges, threshold convention, and whether the estimate is signed or absolute.

5. Do not promote `M9`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Verification tasks:

- Cite exact rendered pages and equations.
- Preserve the floor-compatible convention $\psi_F(n)=-1/2$.
- Explicitly distinguish proof, conditional infrastructure, diagnostic computation, and open estimates.

Exploratory allocation:

- Write a one-page comparison between the denominator-paired fourth-moment route and the direct signed bilinear backup. Include one precise falsification criterion for each.

### For A2

Target obligations: `M9-M2-denominator-paired-weighted-bound`, `M9-M2-N0-diagonal-core-bound`, and `M9-near-collision-taxonomy`.

Objectives:

1. Prove or refute the weighted denominator-paired exact resonance lemma. Work in the subfamily
$$
   d_1=d_2=a,\qquad d_3=d_4=b,
$$
   where
$$
   (h_1-h_2)b+(h_3-h_4)a=0.
$$

2. Use the fixed two-sided convention:
$$
   1\le |h|\le H_D,
   \qquad
   H_D\asymp D X^{-1/4}.
$$

3. Use the actual H4-dependent coefficient class:
$$
   \beta_{h,H_D}
   =
   -\frac{\Phi(|h|/(H_D+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h}.
$$

4. Give a complete gcd decomposition. At minimum, set $g=(a,b)$, $a=ga'$, $b=gb'$, and parameterize frequency differences from
$$
   (h_1-h_2)b'=-(h_3-h_4)a'.
$$
   Track equality cases $h_1=h_2$, $h_3=h_4$, sign choices, endpoint truncation, and odd-frequency support.

5. Produce a bound for the absolute weighted mass. If the desired bound fails, give a counterexample construction and state the corrected obstruction.

6. Include a taxonomy table only for families actually treated this round. Mark all other families open.

7. Referee R5-Full against the older DDP-trap concern in one section, but do not make it the main proof unless A1's source audit exposes a real contradiction.

8. Any direct exponent-pair or Poisson alternative must be a proposed route only. It must include a named theorem statement, derivative scale, dual length $m\asymp hX/D^2$, boundary terms, actual $\beta_h$ weights, and uniformity over active $D$.

Verification tasks:

- Use only the allowed status labels.
- Do not label a central claim `[PROVED]` unless the proof is complete.
- Numerical examples are diagnostic only.
- The exact output should make clear whether the denominator-paired weighted bound is proved, refuted, or still open.

Exploratory allocation:

- If the weighted denominator-paired estimate stalls, formulate the smallest signed bilinear statistic that would imply M2, and state a fast A3 falsification test.

### For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-M2-denominator-paired-weighted-bound` diagnostics, `R5-Full-reconciliation` diagnostics.

Objectives:

1. Verify the committed Round 3 artifacts:
   - `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`;
   - `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`;
   - `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`;
   - `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`.

2. Update the raw-vs-paired script to include:
   - official $\mathcal M_1$ formula with $\chi_4(d)$;
   - official $\mathcal M_2$ raw two-sided formula;
   - paired real formula;
   - complex-weight cosine pairing;
   - explicit failure of the $\operatorname{Re}B_h$ formula for complex weights.

3. After A1 completes H4, replace any provisional kernel by the exact
$$
   \Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

4. Scale the exact fourth-moment enumeration. Report:
   - total exact $N=0$ mass;
   - pair-equality mass;
   - denominator-paired mass;
   - semi-diagonal mass if classified;
   - unclassified exact $N=0$ mass;
   - near-collision mass for $0<|N|\le cD^4/X$;
   - signed and absolute versions;
   - normalization by $D^2$ and $X$.

5. Build a denominator-paired-only diagnostic table matching A2's variables $a,b,g,a',b'$ and frequency-difference parameter.

6. Run R5 residual product-count diagnostics for first leg and shifted legs $\rho=1,3$, with square, near-square, nonsquare, and divisor-rich $X$, and exact resonance handling.

7. Continue CRI and gradient-spacing diagnostics, but label all results `diagnostic_only`.

Verification tasks:

- Record command line, Python version, precision, exact table schema, pass/fail assertions, and H4 coefficient status.
- Use high precision near Fejer spikes and exact integer arithmetic for $N$.
- Do not infer asymptotic proof from finite tables.

Exploratory allocation:

- Compare fixed $\beta_h$ coefficients against unsigned, random-sign, and adversarial coefficients to test whether the signed route has visible structure.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 8.0 | 9.0 | Strong algebraic normalization, conservative proof-state handling, useful route proposals, and correct separation of pair-equality core from full diagonal-core obligation. |
| A2 | 7.0 | 2.0 | 3.0 | Useful focus on denominator-paired and alternative direct routes, but central claims were overpromoted and several `[PROVED]` labels lacked complete proof. |
| A3 | 7.0 | 6.5 | 8.0 | Useful executed diagnostic artifacts and good diagnostic-only calibration; quantitative outputs remain provisional until H4 and larger runs. |

Overall mathematical-progress score is conservative: Round 3 sharpened the target and created usable diagnostic evidence, but it did not prove any endpoint estimate or complete a taxonomy.

## Confidence

High confidence in accepting A1's $\mathcal M_2$ algebra under H4.

High confidence in accepting A3's artifacts as `diagnostic_only` evidence.

High confidence in rejecting A2's proof promotions.

Moderate confidence that the signed fourth-moment route remains the best primary M2 route.

Moderate confidence that the denominator-paired weighted subcase is the right next narrow proof target.

Low confidence that A2's current direct exponent-pair/Poisson sketch proves the endpoint as stated.

No new Gauss circle exponent is proved in Round 3.
