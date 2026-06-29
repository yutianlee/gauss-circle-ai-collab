## Summary

Source basis: I treated the uploaded Round 4 judge packet as the controlling Stage C instruction bundle. The packet requires a conservative synthesis with a selected route, state patch, next-round prompts for A1/A2/A3/A4, split scoring, and no promotion of `M9`, `M9-M2`, or `GC-target` without complete endpoint proof.

Round 4 made real but narrow proof-graph progress:

- The H4/Vaaler formula audit is mathematically strong, but the source card still needs to be committed before H4 should be promoted as an external theorem dependency.
- `R5-Full-reconciliation` is now essentially settled conditional on H4: the accepted proof uses the positive Fejer majorant before Fourier expansion and proves a pointwise product-count bound, not merely an averaged or RMS statement.
- The denominator-paired exact $N=0$ weighted fourth-moment subfamily is proved under the H4-dependent coefficient magnitude hypothesis $|\beta_h|\ll 1_{2\nmid h}/|h|$. This should move to `derived_under_assumptions`.
- The harmonic-convolution estimate
$$
L_H(q)=\sum_{\substack{1\le |h|\le H\\1\le |h+q|\le H}}\frac{1}{|h|\,|h+q|}
\ll \frac{\log(2H)}{\max(1,|q|)}
$$
should be registered as a reusable `proved_internal` lemma.
- A2's semi-diagonal and pair-swapped extensions are probably correct and are supported by A4's review, but they should be recorded as a narrow paired-core sublemma, not as proof of the full exact $N=0$ taxonomy.
- A4 identified a serious missing obligation: fourth-moment/near-collision control is not automatically a pointwise bound for the specific $X$ in $P(X)$. The project should add an explicit average-to-pointwise / unsmoothing obligation.

No new Gauss circle exponent is proved. `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` remain open.

## Selected main route

The selected main route remains the balanced hyperbola / floor-compatible sawtooth / finite Vaaler route:

$$
P(X)=N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola}
\longrightarrow
\text{floor-compatible sawtooth}
\longrightarrow
\text{finite Vaaler}
\longrightarrow
\text{fixed-coefficient reciprocal sums}.
$$

The bridge remains conditional:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The primary Round 5 route should be:

1. Finish the exact $N=0$ paired-core bookkeeping in proof-draft-ready form.
2. Preserve the unclassified exact $N=0$ class as open.
3. Add and attack the new average-to-pointwise / unsmoothing obligation for any fourth-moment route.
4. Continue near-collision work only in controlled subfamilies, starting with denominator-paired near-collisions.
5. Run signed-vs-unsigned diagnostics before committing further to an absolute fourth-moment strategy.

### Route comparison

**Primary route: exact resonance plus pointwise bridge.**

Exact lemma already advanced:

$$
T_{\mathrm{dp}}(D;X)
=
\sum_{\substack{
a,b\asymp D\\
1\le |h_i|\le H_D\\
(h_1-h_2)b+(h_3-h_4)a=0
}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\ll_\epsilon D^2X^\epsilon.
$$

This route attacks `M9-near-collision-taxonomy` and `M9-M2-N0-diagonal-core-bound` by replacing broad taxonomy claims with small weighted lemmas. It should continue because it produced a checkable proof this round.

Fast falsification criterion: if A3's exact enumeration shows the unclassified exact $N=0$ weighted mass grows faster than $X^{1+o(1)}$ at active endpoint blocks, the absolute exact-resonance route cannot be sufficient.

**Backup route: direct signed bilinear statistic.**

The backup lemma remains:

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$, by a sign-preserving large-sieve, spacing, or bilinear estimate.

This route attacks the sign-insensitivity of the diagonal/absolute fourth-moment program. It should not be promoted without a named theorem or new spacing lemma. A3's signed-vs-unsigned diagnostics decide whether the route is worth further proof effort.

Fast falsification criterion: if true $\beta_h$ behavior tracks unsigned or adversarial coefficients across endpoint blocks, then the signed route has no visible numerical advantage and should be deprioritized.

**Rejected as primary: black-box Li--Yang import.**

Li--Yang is useful literature context, not an endpoint theorem for this proof graph. The arXiv page identifies the paper by Xiaochun Li and Xuerui Yang and describes their Bombieri--Iwaniec, first-spacing, and Huxley second-spacing framework. Their rendered paper states the record exponent $\theta^*=0.314483\ldots$ and discusses a $5/16$ barrier for existing methods. That is not a proof of the conjectural $1/4$ exponent and cannot be imported without a completed source-card hypothesis audit.

## Useful fragments by source

### A1

A1's most useful infrastructure contribution is the H4 formula audit and R5 pointwise proof.

The H4 audit matches Vaaler's local PDF. Theorem 6 on printed page 192 gives the Fourier transform of $J$:

$$
\widehat J(t)=
\begin{cases}
1, & t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|, & 0<|t|<1,\\
0, & 1\le |t|.
\end{cases}
$$

The local Vaaler PDF page also states that $\widehat J$ is even, nonnegative, continuously differentiable, and decreasing on $[0,1]$. AMS identifies the article as Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12 (1985), 183--216.

A1's R5 proof uses

$$
|R_H^F(t)|\le \frac{1}{2H+2}K_H(t)
$$

and then proves

$$
\frac1H\sum_{d\asymp D}K_H(T_d)
\ll_\epsilon X^{1/4+\epsilon}
$$

for $T_d=X/d$ and $T_d=(X/d+\rho)/4$, $\rho\in\{1,3\}$. The key count is

$$
\#\{d\asymp D:\|X/d\|\le\Delta\}
\ll_\epsilon (1+\Delta D)X^\epsilon.
$$

This is the correct pointwise product-count argument and avoids the old arbitrary-coefficient Fejer-expansion trap. A4's review explicitly confirms that A1's R5 argument controls the right norm.

A1 also correctly records the M2 coefficient algebra, conditional on H4:

$$
C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h},
$$

and

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

### A2

A2 independently gives the denominator-paired gcd parameterization:

$$
d_1=d_2=a,\qquad d_3=d_4=b,
$$

so

$$
N=ab\big((h_1-h_2)b+(h_3-h_4)a\big).
$$

With $g=(a,b)$, $a=ga'$, $b=gb'$, $(a',b')=1$, exact resonance implies

$$
h_1-h_2=ta',
\qquad
h_3-h_4=-tb'.
$$

A2's denominator-paired proof core is valid. Its broader claims require trimming. In particular, A2's R5 discussion uses an averaged or $L^2$ norm and should not be used as the state proof for `R5-Full`; A1's positive Fejer product-count proof is the accepted R5 argument. A4's review flags this wrong-norm issue clearly.

A2's semi-diagonal and pair-swapped extensions are useful. The semi-diagonal family

$$
d_1=d_3=a,\qquad d_2=d_4=b
$$

gives

$$
(h_1+h_3)b-(h_2+h_4)a=0,
$$

and the pair-swapped family

$$
d_1=d_4=a,\qquad d_2=d_3=b
$$

gives

$$
(h_1-h_4)b+(h_3-h_2)a=0.
$$

A4 verifies that these reduce to the same harmonic-convolution bound. I accept this as a narrow paired-core extension under H4, not as a proof of the full exact $N=0$ taxonomy.

### A3

A3's contribution is mainly diagnostic design. The proposed checks are the right ones: raw-vs-paired formulas, complex-weight cosine pairing, denominator-paired enumeration, exact $N=0$ binning, near-collision binning, R5 diagnostics, and signed/unsigned/adversarial coefficient comparisons. A1's review correctly notes that A3 is well calibrated in keeping this `diagnostic_only`, but the visible artifact bundle is not yet state-positive evidence because the code is incomplete or placeholder-like.

A3 should next produce actually executable diagnostics with command lines, versions, precision logs, table schemas, and pass/fail assertions. No theorem status should depend on A3 computations.

### A4

A4 gives the strongest proof-surgeon contribution. The reusable harmonic lemma is

$$
L_H(q)
=
\sum_{\substack{1\le |h|\le H\\1\le |h+q|\le H}}
\frac{1}{|h|\,|h+q|},
$$

with

$$
L_H(0)\ll1,\qquad
L_H(q)\ll\frac{\log(2H)}{|q|}\quad(q\ne0).
$$

Together with

$$
h_1-h_2=ta',
\qquad
h_3-h_4=-tb',
$$

this gives the sharp scale

$$
T_{t=0}\asymp D^2,
\qquad
T_{t\ne0}\ll D(\log 2H_D)^2,
\qquad
T\ll D^2X^\epsilon.
$$

A4 also correctly states that this is unsigned, sign-insensitive, and insufficient by itself to prove `M9-M2`.

## Rejected or risky ideas

1. **Reject any promotion of `M9`, `M9-M2`, or `GC-target`.** No endpoint estimate for the fixed reciprocal main sums has been proved.

2. **Reject treating denominator-paired as full taxonomy.** It is one exact $N=0$ subfamily. Even the paired-core extension does not cover mixed or unclassified exact resonances.

3. **Reject A2's broad `proved_internal` status labels.** The denominator-paired proof depends on the H4 coefficient magnitude, and H4's source card remains pending. The correct status is `derived_under_assumptions`.

4. **Reject A2's R5 RMS/L2 proof as a proof of `R5-Full`.** `R5-Full` is pointwise in $X$. A mean-square or RMS statement does not imply the required supremum bound. The accepted R5 proof is A1's positive Fejer product-count proof.

5. **Reject any claim that A3 computation proves asymptotics.** It can find errors, support diagnostics, and guide route selection; it cannot promote theorem obligations.

6. **Reject importing Li--Yang as a theorem dependency.** Its exact theorem hypotheses and parameter ranges still require a source-card audit, and its exponent is not the conjectural endpoint.

7. **Treat absolute fourth-moment progress as sign-insensitive.** The diagonal/paired-core program uses $|\beta_h|$ and therefore cannot exploit the $\chi_4$ sign. This may be necessary bookkeeping but is unlikely to prove `M9-M2` alone.

8. **Reject near-collision optimism at $D=X^{1/2}$ without proof.** The threshold $D^4/X$ is large at the upper endpoint, and absolute near-collision mass may exceed the desired fourth-moment scale.

## Known gaps

1. **H4 source-card gap.** A1's formula-level audit is strong, but `sources/vaaler_1985.md` still needs bibliographic data, local path, theorem/equation transcript, notation translation, residual convention, and endpoint convention.

2. **R5 proof-draft gap.** A1's pointwise R5 product-count proof should be inserted into `best_proof_draft.md`; until then, keep H4 dependency visible.

3. **Average-to-pointwise / unsmoothing gap.** Fourth-moment or near-collision bounds usually control an average over $X$ unless a pointwise mechanism is supplied. `M9-M2` requires a pointwise bound for the specific $X$ in $P(X)$. This needs a new proof obligation.

4. **Unclassified exact $N=0$ mass.** The paired families do not exhaust exact resonance. A3 must enumerate and A2/A4 must attempt a proof or counterexample for the mixed/unclassified class.

5. **Near-collision estimate.** The project still lacks a proved theorem for

$$
0<|N|\le C_0D^4/X
$$

with actual coefficient weights.

6. **M1 remains open.** Round 4 focuses on M2. `M9` cannot move until both `M9-M1` and `M9-M2` are uniformly bounded.

7. **Li--Yang source audit remains open.** It should stay a guardrail until Case A/B ranges, weights, $S/H$ normalization, and absolute-value placement are recorded.

8. **A3 execution gap.** The requested diagnostic bundle has not yet become positive state evidence.

## New lemmas to add

### Lemma 1: harmonic-convolution bound

Status: `proved_internal`.

For $H\ge1$ and integer $q$,

$$
L_H(q)
=
\sum_{\substack{1\le |h|\le H\\1\le |h+q|\le H}}
\frac{1}{|h|\,|h+q|}
$$

satisfies

$$
L_H(0)\ll1,
\qquad
L_H(q)\ll \frac{\log(2H)}{\max(1,|q|)}.
$$

This is the reusable engine for denominator-paired, semi-diagonal, and pair-swapped exact-resonance estimates.

### Lemma 2: denominator-paired exact M2 resonance bound

Status: `derived_under_assumptions`.

Assume H4 gives

$$
|\beta_{h,H_D}|\ll \frac{1_{1\le |h|\le H_D}}{|h|}.
$$

Then for $X^{1/4}\le D\le X^{1/2}$ and bounded weights,

$$
\sum_{\substack{
a,b\asymp D\\
1\le |h_i|\le H_D\\
(h_1-h_2)b+(h_3-h_4)a=0
}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\ll_\epsilon D^2X^\epsilon
\le X^{1+\epsilon}.
$$

### Lemma 3: paired-core exact resonance bound

Status: `derived_under_assumptions`.

Under the same H4 coefficient bound, the following exact $N=0$ paired families have total absolute beta-weighted mass $\ll_\epsilon D^2X^\epsilon$:

- pair-equality;
- denominator-paired;
- pair-swapped;
- semi-diagonal.

This lemma must explicitly state that mixed/unclassified exact resonances remain outside its scope.

### Lemma 4: fourth-moment average-to-pointwise obligation

Status: `open`.

A fourth-moment or near-collision estimate for $S_2(D;X)$ is useful for `M9-M2` only if it implies a pointwise bound at each $X$. A candidate obligation is:

For every active $D$ and every $X_0$, prove an inequality of the form

$$
|S_2(D;X_0)|^4
\ll
\frac1{|I|}
\int_I |S_2(D;X)|^4\,dX
+
\mathcal E(D,X_0,I),
$$

where $I$ is a short interval containing $X_0$, and $\mathcal E$ is bounded by $O_\epsilon(X_0^{1+\epsilon})$ after optimizing $|I|$.

This obligation may require derivative bounds for $S_2(D;X)$:

$$
\frac{d}{dX}S_2(D;X)
=
\frac{2\pi i}{4}
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)\frac{h}{d}e(hX/(4d)),
$$

with all endpoint and dyadic-height dependence tracked.

### Lemma 5: denominator-paired near-collision bound

Status: `open`.

For denominator-paired tuples,

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a.
$$

The near-collision condition

$$
0<|N|\le C_0D^4/X
$$

becomes

$$
0<|L|\ll C_0D^2/X.
$$

Since $D\le X^{1/2}$, this is a bounded-width integer condition. This should be attacked before the full near-collision theorem.

## Counterexample checks to run

1. **Exact denominator-paired identity check.** A3 should verify that direct enumeration matches the gcd/harmonic formula

$$
\sum_{a,b\asymp D}\sum_t L_H(ta')L_H(tb').
$$

2. **Paired-core bins.** Enumerate pair-equality, denominator-paired, pair-swapped, semi-diagonal, mixed, and unclassified exact $N=0$ masses separately.

3. **Unclassified growth exponent.** For increasing feasible $D,H$, fit the unclassified absolute weighted mass against $D^2$, $D^2\log^A D$, $D^{5/2}$, and $D^3$.

4. **Near-collision endpoint bins.** For $D=X^{1/4},X^{3/8},X^{1/2}$, bin

$$
0<|N|\le C_0D^4/X
$$

and report signed and absolute beta-weighted mass.

5. **Denominator-paired near-collision.** Use the normalized condition

$$
0<|(h_1-h_2)b+(h_3-h_4)a|
\ll C_0D^2/X
$$

and compare against exact $N=0$ mass.

6. **Raw-vs-paired formulas.** Verify raw two-sided, real-weight paired, and complex-weight cosine formulas. Deliberately show failure of the $\operatorname{Re}B_h$ shortcut for complex weights.

7. **Signed-vs-unsigned route test.** Compare actual $\beta_h$, unsigned $|\beta_h|$, random signs, and adversarial signs for $S_2(D;X)$ over active dyadic blocks.

8. **R5 product-count stress test.** Test first and shifted residual legs for square, nonsquare, near-square, and divisor-rich $X$, while keeping results `diagnostic_only`.

9. **Average-to-pointwise feasibility test.** Numerically measure local oscillation of $S_2(D;X)$ over short $X$ windows and compare local sup to local fourth-moment averages and derivative bounds.

## Research strategy adjustment

Round 5 should not re-prove denominator-paired exact resonance. It should treat that as settled under H4 and move to three concrete workstreams:

1. **Proof infrastructure.** A1 should commit the Vaaler source card, insert the H4/R5/M2 formulas into `best_proof_draft.md`, and formulate the average-to-pointwise obligation precisely.

2. **Exact-resonance taxonomy.** A2 and A4 should split tasks:
   - A2 writes validator-ready semi-diagonal and pair-swapped proofs using $L_H$.
   - A4 attacks the unclassified exact $N=0$ family or the average-to-pointwise bridge.

3. **Executed diagnostics.** A3 should produce runnable scripts and tables, prioritizing signed-vs-unsigned and unclassified exact $N=0$ growth.

The backup signed bilinear route should receive about 20% of attention. Its viability depends on A3's signed-vs-unsigned data and on a future theorem-level spacing or large-sieve statement.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "M9-M2-harmonic-convolution-LH",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Harmonic convolution bound for reciprocal beta weights",
        "status": "proved_internal",
        "statement_tex": "For H>=1 and integer q, L_H(q)=sum_{1<=|h|<=H, 1<=|h+q|<=H} 1/(|h||h+q|) satisfies L_H(0)<<1 and L_H(q)<<log(2H)/max(1,|q|).",
        "dependencies": [],
        "implies": [
          "M9-M2-denominator-paired-weighted-bound"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A4-004.md",
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Reuse this lemma in paired exact-resonance and denominator-paired near-collision estimates."
      },
      {
        "id": "M9-M2-paired-core-weighted-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Weighted paired-core exact M2 resonance bound",
        "status": "derived_under_assumptions",
        "statement_tex": "Assuming the H4 beta coefficient magnitude |beta_h|<<1_{1<=|h|<=H_D}/|h| and bounded dyadic weights, the pair-equality, denominator-paired, pair-swapped, and semi-diagonal exact N=0 paired families in the M2 fourth moment have total absolute beta-weighted mass <<_epsilon D^2 X^epsilon uniformly for X^(1/4)<=D<=X^(1/2). This does not cover mixed or unclassified exact resonances.",
        "dependencies": [
          "H4",
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion",
          "M9-M2-harmonic-convolution-LH",
          "M9-M2-denominator-paired-weighted-bound"
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
            "rounds/obligation-main/round_004/responses/A2-004.md",
            "rounds/obligation-main/round_004/responses/A4-004.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_004/reviews/A1.md"
          ]
        },
        "owner": "A2",
        "next_action": "Write the pair-swapped and semi-diagonal proofs in proof-draft-ready form; keep mixed and unclassified exact N=0 classes open."
      },
      {
        "id": "M9-M2-fourth-moment-average-to-pointwise",
        "type": "obstruction",
        "track": "M9_analytic",
        "title": "Average-to-pointwise upgrade for M2 fourth-moment estimates",
        "status": "open",
        "statement_tex": "Any fourth-moment or near-collision estimate for S_2(D;X) used to prove M9-M2 must yield the pointwise bound |S_2(D;X_0)|<<_epsilon X_0^(1/4+epsilon) for each active X_0, not only an average over an X-window. A candidate proof must control local fourth moments plus derivative or unsmoothing losses uniformly over X^(1/4)<=D<=X^(1/2).",
        "dependencies": [
          "M9-M2-fourth-moment-expansion",
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
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "owner": "A4",
        "next_action": "Formulate an exact local-sup-from-average inequality for S_2(D;X), including derivative bounds, window length optimization, and endpoint D-uniformity."
      },
      {
        "id": "M9-fourth-moment-enumeration",
        "type": "computation",
        "track": "computation",
        "title": "Exact and near-collision fourth-moment enumeration for M2",
        "status": "diagnostic_only",
        "statement_tex": "Executable diagnostics should enumerate exact N=0 and near-collision M2 fourth-moment tuples with actual beta_h weights, classified into pair-equality, denominator-paired, pair-swapped, semi-diagonal, mixed, and unclassified bins; output signed and absolute masses normalized by D^2 and X.",
        "dependencies": [
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion",
          "M9-regression-raw-vs-paired"
        ],
        "implies": [],
        "blockers": [],
        "accepted_evidence_level": "diagnostic_only",
        "required_output": [
          "script",
          "command",
          "table",
          "precision log",
          "report.md",
          "pass/fail assertions"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_004/responses/A3-004.md",
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "owner": "A3",
        "next_action": "Produce a runnable artifact bundle with exact integer arithmetic for N, true Phi coefficients after H4, signed-vs-unsigned comparisons, and unclassified exact N=0 growth tables."
      }
    ],
    "update": [
      {
        "id": "H4-source-audit",
        "status": "source_audit_required",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Commit sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, Fejer normalization, residual constant, and floor-compatible endpoint convention."
      },
      {
        "id": "H4",
        "status": "source_audit_required",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md"
          ]
        },
        "next_action": "Promote only after the Vaaler source card is physically updated and validated; until then use H4-dependent lemmas as derived_under_assumptions."
      },
      {
        "id": "R5-Full-reconciliation",
        "status": "derived_under_assumptions",
        "reason_for_promotion": "Round 4 supplies a pointwise positive-Fejer product-count proof conditional on H4, with A1 as the main proof source and A4 confirming the norm and dependency.",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ],
          "negative": [
            "rounds/obligation-main/round_004/responses/A2-004.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_004/reviews/A1.md"
          ]
        },
        "next_action": "Insert A1's positive Fejer product-count proof into best_proof_draft.md; reject the RMS/L2 argument as a pointwise proof; keep H4 dependency visible."
      },
      {
        "id": "R5-Full",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Use the pointwise product-count proof conditional on H4; do not promote to proved_internal until H4/source-card validation is complete."
      },
      {
        "id": "M9-M2-beta-algebra",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Insert beta_h algebra, raw two-sided formula, real-weight paired formula, and complex-weight cosine pairing into best_proof_draft.md after H4 source-card update."
      },
      {
        "id": "M9-M2-denominator-paired-weighted-bound",
        "status": "derived_under_assumptions",
        "reason_for_promotion": "A1, A2, and A4 independently derive the denominator-paired exact-resonance bound under the H4 beta-coefficient magnitude hypothesis, and A1/A4 reviews agree it is state-promotable only under assumptions.",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/responses/A2-004.md",
            "rounds/obligation-main/round_004/responses/A4-004.md",
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Treat denominator-paired exact resonance as settled under H4. Use it as a sublemma only; do not infer M9-M2 or full taxonomy."
      },
      {
        "id": "M9-M2-N0-diagonal-core-bound",
        "status": "open",
        "blockers_added": [
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A2-004.md",
            "rounds/obligation-main/round_004/responses/A4-004.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Record paired-core families as treated under assumptions, but prove or refute mixed and unclassified exact N=0 mass before promoting this obligation."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "blockers_added": [
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/responses/A2-004.md",
            "rounds/obligation-main/round_004/responses/A4-004.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_004/responses/A3-004.md",
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Preserve the unclassified exact N=0 class. Next prove or refute mixed/unclassified exact resonances and start denominator-paired near-collision with the normalized L-condition."
      },
      {
        "id": "M9-near-collision-estimate",
        "status": "proposed",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "First attack the denominator-paired near-collision condition 0<|(h_1-h_2)b+(h_3-h_4)a|<<D^2/X, then decide whether absolute or signed estimates are viable."
      },
      {
        "id": "M9-M2",
        "status": "open",
        "blockers_added": [
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_004/responses/A1-004.md",
            "rounds/obligation-main/round_004/responses/A2-004.md",
            "rounds/obligation-main/round_004/responses/A4-004.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Do not promote from exact-resonance sublemmas. Supply pointwise control, near-collision estimates, and endpoint-uniformity before any status change."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_004/responses/A3-004.md",
            "rounds/obligation-main/round_004/reviews/A1.md",
            "rounds/obligation-main/round_004/reviews/A4.md"
          ]
        },
        "next_action": "Rerun with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, real paired formula, complex-weight cosine formula, and explicit failure of Re B_h for complex weights. Produce executable artifacts."
      }
    ],
    "reject": [
      {
        "id": "A2-R4-R5-L2-or-RMS-proves-pointwise-R5",
        "reason": "Rejected because R5-Full is a pointwise residual bound in X. An L2 or RMS residual estimate over X does not prove the pointwise product-count statement required by the conditional bridge."
      },
      {
        "id": "A2-R4-full-exact-N0-taxonomy-proved",
        "reason": "Rejected because paired families do not exhaust exact N=0 resonances; mixed and unclassified classes remain open."
      },
      {
        "id": "A2-R4-M9-M2-N0-diagonal-core-proved",
        "reason": "Rejected because the paired-core estimates are only subfamilies and the unclassified exact N=0 mass has not been bounded."
      },
      {
        "id": "A3-R4-unexecuted-artifacts-as-positive-proof-evidence",
        "reason": "Rejected because diagnostic computations require materialized scripts, commands, tables, precision logs, reports, and pass/fail assertions; unexecuted or placeholder code is diagnostic planning only."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform endpoint estimates for both M1 and M2 were proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 4 did not prove an M1 fixed-coefficient reciprocal-sum estimate."
      },
      {
        "id": "M9-endpoint-uniformity",
        "reason": "Every proposed analytic estimate still needs explicit uniformity for X^(1/4)<=D<=X^(1/2)."
      },
      {
        "id": "GC-target",
        "reason": "The final target remains open because M9 is open."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a source-audit and guardrail obligation; no theorem is imported as a dependency."
      },
      {
        "id": "Conditional-bridge",
        "reason": "The bridge remains conditional on H4, R5-Full, and M9; no final theorem follows."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 5,
    "idea_quality_score": 8,
    "state_evidence_score": 6,
    "calibration_score": 7,
    "reason": "Round 4 proves a narrow but real H4-dependent denominator-paired exact-resonance bound, validates a reusable harmonic-convolution lemma, and largely reconciles R5-Full pointwise under H4. It does not prove M9, resolve unclassified exact N=0 mass, prove near-collision estimates, or bridge average fourth-moment control to pointwise M2."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, and proof-draft consolidation.

Objectives:

1. Commit or draft the exact Vaaler source card `sources/vaaler_1985.md`. Include:
   - bibliographic data for Vaaler 1985;
   - local PDF path;
   - Theorem 6, equation (2.28), for $\widehat J(t)$;
   - Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, equations (7.13)--(7.17), especially the residual inequality;
   - coefficient sign
$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h};
$$
   - Fejer normalization $K_H(0)=H+1$;
   - floor-compatible endpoint convention $\psi_F(n)=-1/2$.

2. Insert A1's R5 product-count proof into `best_proof_draft.md`. The proof must use the positive Fejer majorant before Fourier expansion and must prove pointwise bounds for:
$$
T_d=X/d,
\qquad
T_d=(X/d+\rho)/4,\quad \rho\in\{1,3\}.
$$

3. Insert official M9 definitions:
$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_d w_D(d)e(hX/(4d)).
$$

4. Insert raw two-sided, real-weight paired, and complex-weight cosine formulas for $\mathcal M_2$.

5. Formulate the new `M9-M2-fourth-moment-average-to-pointwise` obligation precisely. Include a candidate local inequality, derivative estimate for $S_2(D;X)$, window length variable, and expected loss.

6. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Exploratory allocation:

- Write a short comparison of three routes: absolute exact-resonance taxonomy, average-to-pointwise fourth moment, and direct signed bilinear estimate. State the proof obligation and falsification criterion for each.

### For A2

Target obligations: `M9-M2-paired-core-weighted-bound`, `M9-M2-N0-diagonal-core-bound`, and `M9-near-collision-taxonomy`.

Objectives:

1. Do not re-prove the denominator-paired subcase except as a cited sublemma.

2. Write proof-draft-ready proofs for the pair-swapped and semi-diagonal exact $N=0$ families.

For pair-swapped:

$$
d_1=d_4=a,\qquad d_2=d_3=b,
$$

derive the exact equation and reduce it to the same $L_H$ convolution.

For semi-diagonal:

$$
d_1=d_3=a,\qquad d_2=d_4=b,
$$

derive

$$
(h_1+h_3)b-(h_2+h_4)a=0,
$$

and handle the $t=0$ case correctly:

$$
h_1=-h_3,\qquad h_2=-h_4.
$$

3. State the exact paired-core theorem:

$$
T_{\mathrm{paired}}(D;X)
\ll_\epsilon D^2X^\epsilon.
$$

Make clear that mixed and unclassified exact $N=0$ families remain open.

4. Start the mixed/unclassified exact $N=0$ analysis. Either:
   - propose a rigorous parameterization, or
   - construct a lower-bound obstruction showing why absolute counting may fail.

5. Treat R5-Full only as an infrastructure note. Do not use RMS or $L^2$ estimates as pointwise proof.

6. Include a section on average-to-pointwise implications: explain whether the exact-resonance proof is pointwise, averaged over $X$, or merely a component of an averaged fourth moment.

Exploratory allocation:

- Formulate the smallest signed bilinear statistic that could prove `M9-M2` if absolute fourth moments fail. Give one theorem-shaped estimate and one A3 falsification test.

### For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-fourth-moment-enumeration`, `M9-M2-fourth-moment-average-to-pointwise` diagnostics, and signed-vs-unsigned diagnostics.

Objectives:

1. Produce a complete executable artifact bundle. Include:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - precision log;
   - CSV table schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Fix formula and API issues before execution:
   - define $e(t)=\exp(2\pi i t)$ explicitly;
   - use the official M1 phase $e(hX/d)$;
   - use the official M2 phase $e(hX/(4d))$;
   - parse integer parameters exactly for fourth-moment numerator calculations;
   - use high precision near Fejer spikes.

3. Run raw-vs-paired checks:
   - raw two-sided M2;
   - real-weight paired formula;
   - complex-weight cosine formula;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

4. Run exact $N=0$ enumeration with true beta weights:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - semi-diagonal;
   - mixed;
   - unclassified.

Report absolute weighted mass and signed mass normalized by $D^2$ and $X$.

5. Run denominator-paired identity checks using:
$$
a=ga',
\qquad
b=gb',
\qquad
h_1-h_2=ta',
\qquad
h_3-h_4=-tb'.
$$

6. Run near-collision bins:
$$
0<|N|\le C_0D^4/X
$$

at $D=X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

7. Run signed-vs-unsigned tests:
   - true $\beta_h$;
   - unsigned $|\beta_h|$;
   - random signs;
   - adversarial signs.

8. Run average-to-pointwise diagnostics:
   - local sup of $|S_2(D;X)|$ over short $X$ windows;
   - local fourth-moment average;
   - numerical derivative bound;
   - ratio of local sup to average-based upper bound.

All outputs remain `diagnostic_only`.

### For A4

Target obligations: `M9-M2-fourth-moment-average-to-pointwise`, `M9-near-collision-estimate`, and unclassified exact $N=0$ obstruction search.

Objectives:

1. Treat the harmonic-convolution lemma and denominator-paired bound as settled. Do not spend the round re-proving them.

2. Formulate a proof-level average-to-pointwise lemma for $S_2(D;X)$. Start from

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Derive a rigorous candidate inequality relating $|S_2(D;X_0)|^4$ to an average over $X\in I$ plus derivative loss. Track:
   - $|I|$;
   - $\sup_I |S_2|$;
   - $\sup_I |S_2'|$;
   - active range $X^{1/4}\le D\le X^{1/2}$;
   - $H_D\asymp DX^{-1/4}$;
   - whether the resulting bound can reach $X^{1+\epsilon}$ at fourth-moment scale.

3. Attack denominator-paired near-collisions. Use

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a,
$$

so

$$
0<|N|\le C_0D^4/X
$$

implies

$$
0<|L|\ll C_0D^2/X.
$$

Since $D^2/X\le1$, determine whether this is just finitely many shifted exact linear equations and prove the corresponding weighted bound if possible.

4. If time remains, begin a structural obstruction search for mixed/unclassified exact $N=0$ solutions. State one exact parameterization attempt or one lower-bound construction.

5. Keep all claims calibrated. Do not claim `M9-M2`, `M9`, or `GC-target`.

Exploratory allocation:

- Propose one sign-preserving spacing or large-sieve theorem that would imply the direct signed bilinear estimate. State its exact variables and falsification test.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 8.0 | 8.5 | Strong H4 formula audit, correct R5 pointwise product-count proof, useful M2 algebra, and good route framing. Slight overpromotion risk if H4/source-card completion is treated as already committed. |
| A2 | 7.5 | 6.5 | 5.5 | Correct denominator-paired proof core and useful paired-family extensions. Calibration is weaker because several `[PROVED]` labels overreach, and the R5 RMS discussion uses the wrong norm for pointwise R5. |
| A3 | 7.0 | 3.0 | 8.0 | Diagnostic design is well targeted and appropriately labeled `diagnostic_only`, but the artifact bundle is not yet executable state-positive evidence. |
| A4 | 8.5 | 8.0 | 9.0 | Best narrow analytic contribution: clean harmonic-convolution proof, correct H4 dependency, sharp scale $T\asymp D^2$, and important identification of the average-to-pointwise gap. |

Overall progress is moderate but real. The proof graph gains one reusable internal lemma and one H4-dependent exact-resonance sublemma. It does not gain an endpoint M2 estimate.

## Confidence

Confidence: 0.84.

High confidence:
- The denominator-paired exact-resonance bound is correct under the H4 coefficient magnitude hypothesis.
- The harmonic-convolution lemma is correct and reusable.
- A1's R5 product-count proof is the correct pointwise route conditional on H4.
- `M9`, `M9-M2`, and `GC-target` must remain open.

Moderate confidence:
- The paired-core extension to pair-swapped and semi-diagonal families is correct after a proof-draft rewrite.
- The average-to-pointwise gap is essential for any averaged fourth-moment route.
- The signed bilinear route is the right backup, but its feasibility is unknown.

Low confidence:
- Absolute near-collision bounds will suffice at the endpoint.
- Existing Li--Yang/Bombieri--Iwaniec technology can be imported to prove the project's endpoint `M9`.
- A finite diagnostic table can reliably predict unclassified exact $N=0$ asymptotics without much larger runs.

No new Gauss circle exponent is proved in Round 4.
