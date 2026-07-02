## Selected main route

Source basis: Round 7 judge prompt, Round 7 A1 reasoning/review files, and the embedded Round 7 A2/A3/A4 outputs and reviews in `judge_7.md`. The judge instructions require a conservative Stage C synthesis, a JSON-compatible `State Patch`, route comparison, next-round prompts for A1/A2/A3/A4, and no promotion of `M9`, `M9-M2`, or `GC-target` without complete endpoint proof.

### Primary route: close exact \(N=0\) under H4, then pivot to near-collision bands

The selected main route is to accept A4's exact-resonance closure as the main Round 7 proof-graph advance, subject to H4/source-card dependency discipline, and to make Round 8 primarily about near-collision estimates.

The core Round 7 identity is the URES divisor factorization. For fixed reduced \(r=\mu/Q\neq0\) and fixed nonzero integers \(p_1,p_3\), exact equality

$$
\frac{p_1}{q_1}+\frac{p_3}{q_3}=\frac{\mu}{Q}
$$

implies

$$
(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3.
$$

This gives a divisor-bound count for denominator pairs \((q_1,q_3)\). The map from a solution to the ordered factor pair is injective, since

$$
q_1=\frac{A+Qp_1}{\mu},
\qquad
q_3=\frac{B+Qp_3}{\mu}.
$$

Integrality, positivity, dyadic range, and reducedness only thin the set of possible pairs. The Stage B reviews converge that this is the strongest new analytic contribution of Round 7 and that it likely closes the exact \(N=0\) absolute-mass arm under the H4 beta-magnitude hypothesis.

The proof-obligation impact is narrow but real:

- create a pure rational divisor-bound lemma for URES;
- update `M9-M2-unpaired-residual-URES` from `open` to `derived_under_assumptions`, blocked by `H4-source-audit`;
- create `M9-M2-exact-N0-total-mass`, also `derived_under_assumptions`, stating that exact \(N=0\) beta-weighted fourth-moment mass is \(\ll_\epsilon D^2X^\epsilon\);
- keep `M9`, `M9-M2`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, and `GC-target` unpromoted.

This does **not** prove `M9-M2`. Exact resonances are only one part of the fourth-moment problem. The active analytic bottleneck becomes

$$
0<|N|\le M
$$

with particular emphasis on the global or local near-collision scale

$$
M\asymp D^4/X
$$

and on whether such estimates can be turned into pointwise bounds at the endpoint.

### Backup route: sign-preserving endpoint Poisson/SPD

The backup route is the sign-preserving endpoint route, either through reciprocal discrepancy or through Poisson/B-process in the \(d\)-variable. Its required theorem remains a direct bound

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for \(X^{1/4}\le D\le X^{1/2}\), without erasing the \(\chi_4(h)\) sign.

A2's Poisson calculation supplies useful structural data:

$$
m\asymp \frac{hX}{D^2},
$$

and at the endpoint \(D\asymp X^{1/2}\) this gives \(m\asymp h\). This coincidence may be relevant, but no signed post-transform estimate has been proved. The Poisson route remains `proposed`, not proof evidence.

Fast falsification for the backup route: if the first serious norm step reduces the signed object to an operator norm, Frobenius norm, Schur/Gershgorin bound, trace bound, or absolute-value matrix, the \(\chi_4\) sign has probably been erased. A3's true-beta versus unsigned/random/adversarial diagnostics should be the go/no-go gate.

### Rejected as main route: local coherence-window LFM

The local fourth-moment route on windows

$$
\delta=X^{1/2}/D
$$

is not a relaxed averaging route. Round 6 and Round 7 confirm that the multiplier has no power-scale decay throughout the full active range; on such windows, the fat \(N\)-band contains the natural range. Therefore LFM must provide full \(h,d\)-space cancellation and is essentially pointwise-strength at the target scale. It should not be treated as a shortcut around endpoint pointwise control.

## Useful fragments by source

### A1

A1's main Round 7 contributions are proof-draft discipline and route filtering.

A1 correctly keeps H4, R5, beta algebra, and \(\Phi\)-regularity conditional on `H4-source-audit`. The coefficient calculation remains:

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
\beta_{h,H}
=
\alpha_{h,H}(e(h/4)-e(3h/4))
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)
\mathbf 1_{2\nmid h}.
$$

A1 also correctly identifies the global-moment plus derivative obstruction: a global fourth moment at scale \(X^{2+\epsilon}\), combined only with \(|S_2'|\ll H_D\), gives a pointwise exponent around \(X^{9/20+\epsilon}\), far above \(X^{1/4+\epsilon}\). This supports the new proposed route-tracking obligation for global moments plus large-value propagation, but it does not prove an endpoint bound.

A1's review recommends promoting the A4 exact-resonance suite only under H4 and explicitly says not to change `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `GC-target`, or `H4`.

### A2

A2 contributes useful endpoint and Poisson structure, but its URES obstruction is not accepted.

Useful A2 items:

1. The stationary relation

$$
m\asymp \frac{hX}{D^2}
$$

and leading dual phase \(\sqrt{hXm}\) are structurally relevant for the sign-preserving Poisson backup route.

2. The endpoint algebraic phase identity is a valid algebraic coordinate change near \(d\approx \sqrt X/2\). It should be recorded as internal algebraic infrastructure with no implication to `M9-endpoint-uniformity`.

Rejected or revised A2 items:

1. A2's claimed obstruction to the URES absolute bound is not reliable. The line "choose \(q_1=Q\)" violates \(q_1\le2D\) for most \(Q\le4D^2\). With that constraint respected, the reviewed divisor object is at \(D^2X^\epsilon\)-scale rather than \(D^4\)-scale.

2. A2's Poisson boundary estimate is not `proved_internal`. It requires smooth weights, nonstationary analysis, stationary points near support edges, \(k=0\) terms, and uniform error terms.

3. A2's endpoint algebraic identity does not imply endpoint uniformity. It is an identity, not an estimate.

### A3

A3 supplies useful diagnostic design, but no state-positive computation in Round 7.

The diagnostic targets are the correct ones: raw-vs-paired formula regression, exact URES identity checks, \(R(r)^2/D^2\) concentration, DP thin-band tests, subcoherence arithmetic, and true-beta versus unsigned/random/adversarial comparisons.

However, A3's code bundle is not accepted as positive evidence. The review identifies likely syntax/indentation problems, an ineffective fake-complex failure test, inconsistent dyadic conventions, and a claim of exact arithmetic while using floating division in one place. Diagnostic output should not be accepted until `python -m py_compile` passes, execution succeeds, and tables/logs/reports are archived.

### A4

A4 gives the strongest Round 7 mathematical contribution.

The URES-D identity gives a divisor-bound proof for fixed reduced \(r\), and the associated lift-weight bookkeeping plausibly yields

$$
R(r)\ll_\epsilon X^\epsilon
$$

for the weighted ordered-pair representation function. Consequently,

$$
\sum_{r\neq0}R(r)^2\ll_\epsilon D^2X^\epsilon
$$

under the H4 beta-magnitude hypothesis. This closes the exact residual resonance class at the same scale as the paired/reduced-paired exact classes.

A4's DP/NF/OB bookkeeping is also useful:

- DP-0 through DP-3 refine denominator-paired exact and thin-band bookkeeping.
- NF-0 through NF-2 give proof-bank versions of reduced rational normal forms and participation rigidity.
- OB-1 records overlap and coverage bookkeeping for reduced-paired exact classes.

The remaining caveat is not mathematical scope but dependency discipline: any actual beta-weighted conclusion is blocked by `H4-source-audit`.

## Rejected or risky ideas

1. **Reject promotion of `M9`, `M9-M1`, `M9-M2`, or `GC-target`.** Round 7 proves no pointwise reciprocal main-sum estimate.

2. **Reject treating exact \(N=0\) closure as near-collision closure.** Exact resonance and \(0<|N|\le M\) are distinct. The latter remains the main fourth-moment counting problem.

3. **Reject A2's `URES absolute bound failure` as a theorem.** The displayed obstruction drops the critical \(q_1\le2D\) constraint and is superseded by A4's divisor factorization.

4. **Reject A2's `Poisson-Boundary-Bound` as `proved_internal`.** The transform is a proposed smooth stationary-phase route, not a completed estimate.

5. **Reject A2's endpoint algebraic phase identity as implying `M9-endpoint-uniformity`.** It has no such implication.

6. **Reject A3's `M9-M2-regression-verified` if proposed.** The diagnostic bundle is not executed and not compile-verified.

7. **Reject A3's fake-complex failure test as designed.** Symmetric artificial coefficients do not break the relation needed to show failure of the real-weight \(\operatorname{Re}B_h\) shortcut.

8. **Reject local-window LFM as a relaxed route.** It may still be a valid target, but any proof must supply target-strength cancellation.

9. **Keep Li--Yang as guardrail only.** Li and Yang's paper states an improved exponent \(\theta^*=0.3144831759741\cdots\) and uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley second-spacing input, but it is not an endpoint theorem for this fixed-Vaaler M9 problem.

10. **Keep H4 source-audit discipline.** Vaaler's Theorem 6 supplies the \(\widehat J\) formula, and Section 7/Theorem 18 supply the finite approximation infrastructure, but the project source card still needs physical completion before H4-dependent statements become external dependencies.

## Known gaps

1. **H4 source card remains incomplete.** H4 stays `source_audit_required`.

2. **Exact \(N=0\) closure is conditional on H4.** The rational/divisor part is internal, but beta weights require the H4 coefficient magnitude and parity support.

3. **Near-collision estimates are open.** The next target is a graded bound such as

$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon,
$$

or a signed analogue with a clear pointwise implication.

4. **Average-to-pointwise remains open.** Global or local moments do not automatically prove pointwise \(M9\).

5. **Endpoint \(D\asymp X^{1/2}\) remains structurally hard.** At that endpoint, local windows are pointwise-strength and Poisson dual length satisfies \(m\asymp h\).

6. **M1 remains open.** Even a future proof of M2 would not prove M9 without M1.

7. **A3 diagnostics remain non-evidence until executed.** They can guide falsification but cannot mutate theorem statuses.

8. **Poisson/SPD routes need exact smooth-weight stationary phase and signed post-transform estimates.** Algebraic transforms alone are insufficient.

## New lemmas to add

### Lemma 1: elementary divisor bound

Status: `proved_internal`.

For every \(\epsilon>0\),

$$
d(n)\ll_\epsilon n^\epsilon.
$$

A proof can be supplied internally from prime factorization. Write \(n=\prod p_i^{a_i}\), \(d(n)=\prod(a_i+1)\), split prime powers at a fixed threshold depending on \(\epsilon\), and absorb the finite small-prime contribution into \(n^\epsilon\) with an \(\epsilon\)-dependent constant.

### Lemma 2: URES representation divisor bound

Status: `proved_internal`.

For fixed reduced \(r=\mu/Q\ne0\) and fixed nonzero \(p_1,p_3\), the number of denominator pairs \((q_1,q_3)\) satisfying

$$
\frac{p_1}{q_1}+\frac{p_3}{q_3}=\frac{\mu}{Q}
$$

is

$$
O_\epsilon((Q^2|p_1p_3|)^\epsilon).
$$

The exact mechanism is

$$
(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3.
$$

### Lemma 3: URES energy reduction

Status: `proved_internal` as an abstract rational-energy reduction.

For an abstract reduced-fraction weight \(A(p/q)\) satisfying the lift-envelope required by the actual beta coefficients, the URES exact-resonance energy is bounded by the second moment of the pair-representation function

$$
R(r)=\sum_{x+y=r}A(x)A(y).
$$

Combined with the URES representation divisor bound, this gives the expected exact-resonance energy scale. Instantiating it for actual M2 beta weights remains H4-dependent.

### Lemma 4: exact \(N=0\) total mass

Status: `derived_under_assumptions`.

Assuming H4 beta magnitude and bounded dyadic weights,

$$
\Sigma^{\mathrm{abs}}_{N=0}
\ll_\epsilon
D^2X^\epsilon
$$

uniformly for \(X^{1/4}\le D\le X^{1/2}\). This bundles paired-core, denominator-paired, reduced-paired, and URES residual exact resonances. It does not include near-collision bands.

### Lemma 5: endpoint algebraic phase identity

Status: `proved_internal`.

Let

$$
D_0=\left\lfloor \frac{\sqrt X}{2}\right\rfloor,
\qquad
\frac{\sqrt X}{2}=D_0+\delta.
$$

For \(d=D_0+m\),

$$
\frac{hX}{4d}
=
h(D_0-m)
+
h\frac{m^2+2D_0\delta+\delta^2}{D_0+m}.
$$

Modulo integers, the phase can be replaced by the second term. This is algebraic infrastructure only; it does not imply endpoint uniformity.

### Lemma 6: global moment plus graded near-collision route

Status: `proposed`.

A future route may combine exact \(N=0\) closure, a graded near-collision estimate, and a large-value theorem stronger than derivative propagation to recover pointwise control. The fourth moment plus crude derivative bound alone is insufficient.

## Counterexample checks to run

1. **URES-D algebra.** Generate valid exact resonances and verify

$$
(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3.
$$

2. **Injectivity.** Verify that factor pairs recover \(q_1,q_3\) uniquely via

$$
q_1=\frac{A+Qp_1}{\mu},
\qquad
q_3=\frac{B+Qp_3}{\mu}.
$$

3. **Lift weights.** Check symbolically and numerically that for reduced \(p/q\),

$$
\sum_{gq\in[D,2D)}|\beta_{gp,H_D}|
\ll \frac{X^\epsilon}{|p|}
$$

under H4 beta magnitude.

4. **\(R(r)^2\) concentration.** Enumerate toy models with surrogate beta weights and test whether

$$
\sum_{r\neq0}R(r)^2/D^2
$$

remains bounded up to \(X^\epsilon\)-growth.

5. **A2 obstruction correction.** Recompute A2's divisor-sum stress test with \(q_1\le2D\) and all other constraints preserved.

6. **Near-collision interval analogue.** Replace exact equality by

$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|
\le \eta
$$

and test whether a divisor/lattice interval bound survives.

7. **DP thin-band test.** Enumerate denominator-paired tuples with

$$
0<|N|\le C_0D^4/X
$$

and compare against the expected \(D\log^2(2H)\)-type scale in the thin regime.

8. **A3 compile gate.** Require `python -m py_compile` before accepting any diagnostic bundle.

9. **Correct complex-weight regression.** Use genuinely complex \(d\)-weights or asymmetric \(h\)-weights to show where the real-weight \(\operatorname{Re}B_h\) formula fails.

10. **Endpoint sign diagnostic.** Compare true beta signs, unsigned coefficients, random signs, and adversarial signs at \(D\asymp X^{1/2}\).

11. **Poisson smooth-weight test.** Derive and test stationary phase first with a smooth compactly supported dyadic weight, not a sharp cutoff.

## Research strategy adjustment

Round 8 should pivot from exact \(N=0\) taxonomy to near-collision and pointwise-upgrade work.

The exact-resonance arm should be treated as conditionally closed under H4, pending proof-draft transcription and source-card completion. The next mathematical bottleneck is the near-collision estimate and the pointwise endpoint mechanism.

Recommended allocation:

- **A1:** proof-draft integration and source discipline. Insert A4's exact-resonance suite, write the elementary divisor-bound lemma, and keep all H4-dependent statements conditional.
- **A2:** interval version of A4's factorization and pointwise-upgrade analysis. Correct the URES obstruction and state a smooth Poisson theorem only with complete error terms.
- **A3:** executable diagnostics only. Repair the code, standardize dyadic conventions, run URES/DP/sign tests, and archive tables/logs.
- **A4:** extend URES-D from equality to short intervals or isolate the obstruction.

Backup work on sign-preserving Poisson/SPD should continue at low allocation until A3's sign diagnostics show that true beta signs outperform unsigned/random/adversarial controls.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "Divisor-bound-elementary",
        "type": "lemma",
        "track": "proof_infrastructure",
        "title": "Elementary divisor-function epsilon bound",
        "status": "proved_internal",
        "statement_tex": "For every epsilon > 0, the divisor function satisfies d(n) <<_epsilon n^epsilon for all n >= 1.",
        "dependencies": [],
        "implies": [
          "M9-M2-URES-representation-divisor-bound"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_007/judge/judge-007.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A1",
        "next_action": "Insert a short prime-factorisation proof into the lemma bank."
      },
      {
        "id": "M9-M2-URES-representation-divisor-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "URES representation divisor bound",
        "status": "proved_internal",
        "statement_tex": "For fixed reduced r=mu/Q != 0 and fixed nonzero p1,p3, the number of denominator pairs q1,q3 satisfying p1/q1 + p3/q3 = mu/Q is O_epsilon((Q^2 |p1 p3|)^epsilon). The proof uses the exact factorization (mu q1 - Q p1)(mu q3 - Q p3)=Q^2 p1 p3 and the elementary divisor bound.",
        "dependencies": [
          "Divisor-bound-elementary"
        ],
        "implies": [
          "M9-M2-unpaired-residual-URES",
          "M9-M2-exact-N0-total-mass"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Transcribe the factorization, injectivity, and divisor-bound proof into the lemma bank."
      },
      {
        "id": "M9-M2-URES-energy-reduction",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "URES energy reduction to pair-representation second moment",
        "status": "proved_internal",
        "statement_tex": "For abstract reduced-fraction weights A(p/q) satisfying the dyadic lift envelope used in the M2 exact-resonance analysis, the URES exact-resonance contribution is controlled by sum_{r != 0} R_res(r)^2, where R_res(r)=sum_{x+y=r} A(x)A(y) over the residual reduced-fraction class.",
        "dependencies": [
          "M9-M2-coprime-rigidity-normal-form",
          "M9-M2-NF-participation-rigidity",
          "M9-M2-URES-representation-divisor-bound"
        ],
        "implies": [
          "M9-M2-unpaired-residual-URES"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Reconcile the exact definition of R_res(r) with the Round 6 state notation and record the ordered-pair convention."
      },
      {
        "id": "M9-M2-exact-N0-total-mass",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Total exact N=0 absolute mass for M2 fourth moment",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming H4 beta magnitude |beta_h| << 1/|h|, parity support, and bounded dyadic weights, the total absolute beta-weighted mass of all exact N=0 M2 fourth-moment tuples is <<_epsilon D^2 X^epsilon uniformly for X^(1/4) <= D <= X^(1/2). This is scoped strictly to exact resonances and does not include near-collision bands.",
        "dependencies": [
          "H4",
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion",
          "M9-M2-paired-core-weighted-bound",
          "M9-M2-denominator-paired-weighted-bound",
          "M9-M2-fraction-matching-weighted-bound",
          "M9-M2-unpaired-reduced-paired-bound",
          "M9-M2-unpaired-residual-URES",
          "M9-M2-URES-energy-reduction"
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
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_007/reviews/A3.md"
          ]
        },
        "owner": "A4",
        "next_action": "Insert the exact-resonance closure proof into the proof draft and keep the H4 blocker explicit."
      },
      {
        "id": "M9-M2-endpoint-algebraic-phase",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Endpoint algebraic phase identity near d approximately sqrt(X)/2",
        "status": "proved_internal",
        "statement_tex": "Let D0=floor(sqrt(X)/2) and sqrt(X)/2=D0+delta. For d=D0+m, hX/(4d)=h(D0-m)+h(m^2+2D0 delta+delta^2)/(D0+m). Hence the exponential phase may be replaced modulo integers by the second term. This is algebraic infrastructure only and has no implication to endpoint uniformity.",
        "dependencies": [],
        "implies": [],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A2-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "next_action": "Use only as a coordinate identity for possible endpoint SPD or Poisson exploration; do not cite it as an estimate."
      },
      {
        "id": "M9-M2-GM4-from-exact-plus-graded",
        "type": "reduction",
        "track": "M9_analytic",
        "title": "Global fourth-moment route from exact resonance plus graded near-collision",
        "status": "proposed",
        "statement_tex": "A proposed route in which exact N=0 closure is combined with a graded estimate for Sigma_abs(0<|N|<=M) and a large-value theorem strong enough to imply pointwise S2(D;X0) <<_epsilon X0^(1/4+epsilon). The crude derivative bound plus a fourth moment is insufficient.",
        "dependencies": [
          "M9-M2-exact-N0-total-mass",
          "M9-near-collision-estimate",
          "M9-M2-fourth-moment-average-to-pointwise",
          "M9-endpoint-uniformity"
        ],
        "implies": [
          "M9-M2"
        ],
        "blockers": [
          "M9-near-collision-estimate",
          "M9-M2-LFM-pointwise-equivalence"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A1-007.md",
            "rounds/obligation-main/round_007/responses/A4-007.md"
          ]
        },
        "owner": "A1",
        "next_action": "Determine the exact moment or large-value theorem needed beyond derivative propagation; do not use this route to promote M9-M2."
      }
    ],
    "update": [
      {
        "id": "M9-M2-unpaired-residual-URES",
        "status": "derived_under_assumptions",
        "blockers_added": [
          "H4-source-audit"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_007/reviews/A3.md"
          ]
        },
        "next_action": "Treat the exact URES residual class as conditionally settled under H4. Next attempt the interval or near-collision analogue rather than another exact N=0 taxonomy pass.",
        "reason_for_promotion": "Round 7 supplies an exact factorization and divisor-bound argument for URES pair representations, plus lift-weight bookkeeping under the H4 beta-magnitude hypothesis."
      },
      {
        "id": "M9-M2-N0-diagonal-core-bound",
        "status": "derived_under_assumptions",
        "blockers_added": [
          "H4-source-audit"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "next_action": "Use M9-M2-exact-N0-total-mass as the exact-resonance closure under H4. Do not infer M9-M2; near-collision and pointwise upgrade remain open.",
        "reason_for_promotion": "Exact N=0 beta-weighted mass is now controlled under H4 by paired-core, reduced-paired, and URES divisor-bound arguments."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A1-007.md"
          ]
        },
        "next_action": "Record that the exact N=0 arm is conditionally closed under H4. Keep the obligation open for 0<|N|~T near-collision bands, endpoint uniformity, and pointwise upgrade."
      },
      {
        "id": "M9-near-collision-estimate",
        "status": "proposed",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A1-007.md",
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Attack the graded interval analogue of URES-D: bound the beta-weighted mass with 0<|N|<=M, especially M near D^4/X, and separate absolute and signed variants."
      },
      {
        "id": "M9-M2-DP-near-collision-bound",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Transcribe A4's DP-0 through DP-3 class-level statements with dyadic constants, parity support, C0 dependence, and H4 beta-magnitude dependency."
      },
      {
        "id": "M9-M2-coprime-rigidity-normal-form",
        "status": "proved_internal",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Replace the compact Round 6 statement with the Round 7 NF-0/NF-1 lemma-bank version."
      },
      {
        "id": "M9-M2-NF-participation-rigidity",
        "status": "proved_internal",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Transcribe NF-2 participation rigidity in final lemma-bank notation and use it as support for interval near-collision attempts."
      },
      {
        "id": "M9-M2-unpaired-reduced-paired-bound",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Attach OB-1 coverage and overlap bookkeeping; keep H4-source-audit as blocker."
      },
      {
        "id": "M9-M2-reciprocal-SPD-route",
        "status": "proposed",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A1-007.md",
            "rounds/obligation-main/round_007/responses/A4-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "State the exact SPD-1 discrepancy theorem and SPD-J jump/near-jump convention; separate integer-X exact jumps from real-X near-jumps; require A3 true-vs-unsigned-vs-random-vs-adversarial diagnostics before major proof investment."
      },
      {
        "id": "M9-M2-sign-preserving-poisson-voronoi-route",
        "status": "proposed",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A2-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Restate as a smooth-weight stationary-phase obligation with exact constants, boundary terms, k=0 terms, nonstationary ranges, support-edge stationary points, and a signed post-transform estimate."
      },
      {
        "id": "M9-fourth-moment-enumeration",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A3-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md",
            "rounds/obligation-main/round_007/reviews/A2.md"
          ]
        },
        "next_action": "Before accepting any output, require py_compile success, execution, exact rational arithmetic for N and lambda, standardized dyadic convention, corrected complex-weight test, tables, precision log, report, and pass/fail assertions."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A3-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Repair the complex-weight failure test using genuinely complex d-weights or asymmetric h-weights. Then execute raw two-sided, complex-weight cosine, real-weight Re B_h, and deliberate complex-weight failure regressions."
      },
      {
        "id": "H4-source-audit",
        "status": "source_audit_required",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_007/responses/A1-007.md",
            "rounds/obligation-main/round_007/reviews/A1.md"
          ]
        },
        "next_action": "Commit sources/vaaler_1985.md with DOI, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, and M2 parity support."
      }
    ],
    "reject": [
      {
        "id": "A2-R7-URES-absolute-bound-failure",
        "reason": "Rejected because the displayed obstruction drops or violates the q1<=2D constraint for most Q, and constraint-respecting checks point to D^2 X^epsilon scale rather than a D^4 obstruction."
      },
      {
        "id": "A2-R7-Poisson-Boundary-Bound-proved",
        "reason": "Rejected because the boundary estimate is not proved for sharp dyadic cutoffs and lacks smooth-weight assumptions, endpoint stationary-point analysis, k=0 terms, nonstationary tails, and uniform error terms."
      },
      {
        "id": "A2-R7-endpoint-algebraic-phase-implies-uniformity",
        "reason": "Rejected because the endpoint algebraic phase identity is exact algebra on a coordinate patch but does not imply any uniform bound over active D."
      },
      {
        "id": "A3-R7-regression-verified",
        "reason": "Rejected because the diagnostic bundle is not accepted until code compiles, runs, and produces the required tables, logs, and report."
      },
      {
        "id": "A3-R7-fake-complex-failure-test",
        "reason": "Rejected because the proposed symmetric fake-complex setup preserves the conjugacy relation it was supposed to violate; the test must use genuinely complex d-weights or asymmetric h-weights."
      },
      {
        "id": "A3-R7-Mellin-Perron-route",
        "reason": "Rejected as a state mutation because the exploratory Mellin-Perron discussion contains a formal application error and no theorem-level bridge to M9."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "Round 7 does not prove uniform endpoint bounds for both M1 and M2."
      },
      {
        "id": "M9-M1",
        "reason": "Round 7 supplies no M1 fixed-coefficient reciprocal-sum estimate."
      },
      {
        "id": "M9-M2",
        "reason": "Exact N=0 mass is not a pointwise M2 estimate; near-collision, endpoint uniformity, and pointwise upgrade remain open."
      },
      {
        "id": "M9-endpoint-uniformity",
        "reason": "No route proves uniform endpoint control over X^(1/4)<=D<=X^(1/2)."
      },
      {
        "id": "GC-target",
        "reason": "The final theorem remains open because M9 remains open."
      },
      {
        "id": "Conditional-bridge",
        "reason": "The bridge remains conditional on H4, R5-Full, and M9."
      },
      {
        "id": "H4",
        "reason": "H4 remains source_audit_required until the source card is physically completed and validated."
      },
      {
        "id": "R5-Full",
        "reason": "R5 remains derived_under_assumptions, blocked by H4-source-audit."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a guardrail and source-audit obligation, not a black-box dependency for endpoint M9."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 6,
    "idea_quality_score": 8,
    "state_evidence_score": 7,
    "calibration_score": 8,
    "reason": "Round 7 makes significant proof-graph-safe progress by conditionally closing the exact N=0 fourth-moment mass through A4's URES divisor factorization, while correctly leaving M9, M9-M2, near-collision estimates, endpoint uniformity, H4, and the final Gauss circle target open."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `H4-source-audit`, `M9-M2-exact-N0-total-mass`, `M9-M2-URES-representation-divisor-bound`, `M9-M2-URES-energy-reduction`, `M9-M2-unpaired-residual-URES`, `M9-near-collision-estimate`, proof-draft maintenance.

Objectives:

1. Insert the Round 7 exact-resonance suite into `state/best_proof_draft.md` and the lemma bank:
   - `Divisor-bound-elementary`;
   - `M9-M2-URES-representation-divisor-bound`;
   - `M9-M2-URES-energy-reduction`;
   - `M9-M2-exact-N0-total-mass`;
   - updated NF/DP/OB statements.

2. Reconcile the exact definition of \(R(r)\) with the Round 6 state:
   - ordered versus unordered pairs;
   - signed versus absolute weights;
   - reduced-fraction support;
   - dyadic lift convention \(h=gp,d=gq\);
   - parity restriction from beta support.

3. Write the short divisor-bound proof explicitly.

4. Keep all actual beta-weighted exact-resonance conclusions blocked by `H4-source-audit`.

5. Finalize `sources/vaaler_1985.md` with:
   - DOI;
   - local PDF path;
   - Theorem 6 equation (2.28);
   - Section 7 equations (7.1)--(7.3);
   - Theorem 18 equations (7.13)--(7.17);
   - coefficient sign;
   - Fejer normalization;
   - residual constant;
   - floor-compatible endpoint convention;
   - \(\Phi\) regularity;
   - M2 single-parity support.

6. State the next near-collision theorem in proof-draft-ready form:
$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon,
$$
or explain why this absolute version should be replaced by a signed variant.

7. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `GC-target`, or `H4`.

Exploratory allocation: write a one-page route map comparing the graded near-collision/global-moment route against the sign-preserving Poisson/SPD endpoint route.

### For A2

Target obligations: `M9-near-collision-estimate`, `M9-M2-GM4-from-exact-plus-graded`, `M9-M2-sign-preserving-poisson-voronoi-route`, `M9-M2-endpoint-algebraic-phase`.

Objectives:

1. Retract or repair the Round 7 URES obstruction:
   - explicitly include \(q_1\le2D\);
   - identify where the \(D^4\) or \(D^6\) inflation entered;
   - state the corrected divisor-sum estimate.

2. Attack the interval analogue of URES-D. Replace exact equality by
$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|
\le \eta.
$$
Derive the resulting inequality after multiplying denominators and identify the divisor/lattice-count theorem needed.

3. Determine whether the graded estimate
$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon
$$
is plausible for URES-type residual classes.

4. Restate the Poisson/B-process route as a smooth-weight theorem:
   - exact Fourier convention;
   - stationary point;
   - phase;
   - amplitude;
   - \(m\asymp hX/D^2\);
   - boundary terms;
   - \(k=0\) terms;
   - support-edge stationary points;
   - signed post-transform estimate required.

5. Keep `M9-M2-endpoint-algebraic-phase` as an identity only. Do not use it to imply endpoint uniformity.

Exploratory allocation: compare the sign-preserving endpoint route with the graded near-collision route and state one falsification test for each.

### For A3

Target obligations: `M9-fourth-moment-enumeration`, `M9-regression-raw-vs-paired`, `M9-M2-reciprocal-SPD-route` diagnostics.

Objectives:

1. Materialize executable diagnostics. The first line of the report must include:
   - command line;
   - Python version;
   - dependency versions;
   - precision settings;
   - exact dyadic convention;
   - H4 coefficient status.

2. Require `python -m py_compile` to pass before running.

3. Use exact rational arithmetic for \(N\), \(\lambda\), and URES factorization checks whenever exactness is claimed.

4. Standardize dyadic convention across all diagnostics, preferably \(d\in[D,2D)\), and state it in every table.

5. Correct the complex-weight regression:
   - raw two-sided formula;
   - complex-weight cosine pairing;
   - real-weight \(\operatorname{Re}B_h\) formula;
   - deliberate failure using genuinely complex \(d\)-weights or asymmetric \(h\)-weights.

6. Run URES-D tests:
   - random exact-resonance identities;
   - injectivity recovery of \(q_1,q_3\);
   - \(R(r)^2/D^2\) concentration for increasing toy ranges;
   - include the \((6,10,15,5)k\) family.

7. Run DP thin-band tests:
$$
0<|N|\le C_0D^4/X.
$$

8. Run endpoint sign diagnostics:
   - true beta;
   - unsigned beta;
   - random signs;
   - adversarial signs.

9. Archive script, command, tables, precision log, report, and pass/fail assertions. Keep all output `diagnostic_only`.

Exploratory allocation: one smooth-weight Poisson numerical sanity check near \(D\asymp X^{1/2}\), but only after the exact formula-regression bundle is complete.

### For A4

Target obligations: `M9-near-collision-estimate`, `M9-M2-URES-representation-divisor-bound`, `M9-M2-exact-N0-total-mass`, `M9-M2-unpaired-residual-URES`.

Objectives:

1. Transcribe the URES-D proof in lemma-bank form:
   - exact factorization;
   - injectivity;
   - divisor-bound count;
   - zero/nonzero numerator cases;
   - reducedness constraints;
   - dyadic denominator constraints.

2. Verify the lift-weight summation for actual beta magnitudes:
$$
\sum_{gq\in[D,2D)}|\beta_{gp,H_D}|
\ll_\epsilon \frac{X^\epsilon}{|p|}.
$$

3. Extend URES-D to a short-interval inequality if possible. Starting from
$$
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|
\le \eta,
$$
derive the corresponding near-factorization or lattice-strip condition.

4. Identify the first obstruction to proving
$$
\Sigma_{\mathrm{abs}}(0<|N|\le M)
\ll_\epsilon
D^2\max(1,MX/D^4)X^\epsilon.
$$

5. If the absolute near-collision estimate fails, construct a concrete lower-bound family with beta-weighted mass above budget. If it does not fail, propose the next exact divisor/lattice lemma.

6. Keep all exact \(N=0\) claims conditional on H4 when actual beta weights are used.

Exploratory allocation: formulate a signed variant of the near-collision estimate only after the absolute interval analogue has a clear obstruction.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.4 | 7.3 | 9.0 | Strong source-discipline, beta algebra, R5/LFM route filtering, and accurate no-promotion stance. The main value is synthesis and proof-draft maintenance rather than a new analytic lemma. |
| A2 | 7.1 | 4.2 | 6.2 | Useful Poisson and endpoint-coordinate structure, but the URES obstruction is rejected and several Poisson/boundary claims were over-statused. |
| A3 | 7.1 | 2.5 | 7.4 | Good diagnostic design and some useful formula-audit instincts, but no accepted execution evidence; code/regression design must be repaired. |
| A4 | 9.6 | 9.0 | 8.8 | Strongest Round 7 contributor. The URES divisor factorization and exact \(N=0\) mass closure are proof-graph-safe under H4, with good scope discipline. |

Overall Round 7 assessment: substantial exact-resonance progress, no endpoint theorem. The state may gain conditional exact \(N=0\) closure, but not `M9-M2`, `M9`, or the final Gauss circle bound.

## Confidence

High confidence in rejecting A2's URES obstruction as stated.

High confidence that A3 has not supplied positive diagnostic evidence yet.

High confidence in A4's URES representation divisor identity.

Moderately high confidence that the exact \(N=0\) absolute beta-weighted mass is conditionally settled under H4.

Moderate confidence that the next best analytic target is the interval/near-collision analogue of URES-D.

Low confidence that global fourth moments plus derivative propagation can reach endpoint pointwise control.

Low-to-moderate confidence that the sign-preserving Poisson/SPD route is easier than `M9-M2`; it remains the best backup because it attacks endpoint sign loss directly.

No new Gauss circle exponent is proved in Round 7.
