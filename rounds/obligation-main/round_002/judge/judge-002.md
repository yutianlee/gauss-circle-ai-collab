## Selected main route

Keep the current M9-focused route, with $\mathcal M_2$ as the immediate analytic bottleneck. Round 2 did not prove `M9`, `M9-M2`, `M9-near-collision-taxonomy`, or the Gauss circle target. The main safe progress is algebraic: the exact $\mathcal M_2$ coefficient normalization, the bounded-scope $h$-Cauchy sign-loss diagnostic, and the corrected two-sided fourth-moment numerator.

The primary route for Round 3 should be:

$$
\mathcal M_2
\longrightarrow
\text{two-sided fourth moment}
\longrightarrow
\text{exact } N=0 \text{ taxonomy}
\longrightarrow
\text{near-collision estimate}.
$$

The central object is

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

where

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

conditional on the current H4 Vaaler coefficient convention. The sufficient target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

The fourth-moment phase is

$$
\frac{X}{4}
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

This is the selected route because it preserves the fourfold frequency-character product before absolute-value majorization. The human Stage B audit explicitly recommends accepting this algebraic core, while keeping the near-collision taxonomy open and rejecting promotion of `M9`, `M9-M2`, and the final target.

The backup route is a direct fixed-coefficient signed bilinear or residue-interference route for $\mathcal M_2$. The exact lemma would be

$$
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}.
$$

It attacks the same sign-loss obstruction without passing first through a positive $h$-second moment. It is not yet a theorem. Its fast falsification test is whether the first serious proof step replaces $\beta_h$ by $|\beta_h|$, or reduces to a character-blind matrix/operator norm. A2's proposed gradient

$$
\nabla f(h,d)=
\left(\frac{X}{4d},-\frac{hX}{4d^2}\right)
$$

is a useful starting diagnostic for this backup route, but no double-large-sieve theorem has been matched to the endpoint hypotheses.

## Useful fragments by source

### From A1

A1 supplied the most reliable algebraic normalization for this round. The accepted identities are

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

and, under the current H4 convention,

$$
\beta_{h,H}
=
\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Thus

$$
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

A1 also correctly separated the raw two-sided $\mathcal M_2$ formula from the paired real formula. The paired real formula is valid only when the dyadic weight $w_D$ is real-valued. For complex weights, the identity

$$
B_{-h}=\overline{B_h}
$$

generally fails.

A1's $h$-Cauchy diagnostics are also accepted with narrow scope. Weighted $|\alpha_h|$-Cauchy gives acceptable diagonal size but replaces $C_h$ by

$$
|C_h|^2=4\,1_{2\nmid h},
$$

thereby losing the $\chi_4(h)$ sign. Unweighted $h$-Cauchy has diagonal size

$$
D H_D\asymp D^2X^{-1/4},
$$

which is $X^{3/4}$ at $D\asymp X^{1/2}$, above the squared endpoint scale $X^{1/2+\epsilon}$. These are diagnostics, not global no-go theorems.

### From A2

A2's useful contribution is the decision to focus on the two-sided fourth-moment object with the corrected numerator $N$. That is the right algebraic object for `M9-near-collision-taxonomy`.

A2 also identified important exact-resonance families: direct diagonal, pair-swapped, sign-symmetric, reduced-fraction or semi-diagonal, denominator-paired, and unclassified cases. The direct diagonal, pair-swapped, and sign-symmetric families are genuine exact $N=0$ families. Their total mass is compatible with the fourth-moment target at the level

$$
O(D^2)\le O(X),
$$

under bounded dyadic weights and $|\beta_h|\ll 1/|h|$.

However, A2 overstates proof status. A2 labels the exact taxonomy complete even though it contains an unclassified class, and gives conflicting diagonal-capacity constants: the body calculation gives a factor $3/16$, while the boxed statement uses $1/16$. The judge state should record only the coarse compatibility

$$
O(D^2)\le O(X),
$$

not the incorrect constant.

A2's dual-length observation is useful only as a route diagnostic. For a Poisson transform of the $d$-sum, the dual length scale

$$
K\asymp X^{3/4}D^{-1}
$$

exceeds $D$ for $D<X^{3/8}$. A2's stated subrange $D\ll X^{1/3}$ is a valid smaller subrange, but not the natural threshold. This observation does not close the fourth-moment route and should not be entered as a theorem obstruction.

### From A3

A3's useful contribution is the computational-regression plan: raw two-sided versus paired real formulas, complex-weight paired failure, checks for $C_h$, $\beta_{-h}=\beta_h$, $h$-Cauchy sign loss, and toy fourth-moment binning with the corrected $N$. These are the right diagnostics for `M9-regression-raw-vs-paired`.

A3's evidence is not yet state evidence. The current obligation requires an actual script, command, table, precision log, and report; prose, expected output, or unexecuted code does not satisfy that requirement. A3 also uses a provisional tent kernel for $\Phi$, and some formulas in the response normalize M1/M2 differently from the official raw formulas. Those tests may be useful after correction, but they cannot be recorded as positive evidence until actual repository artifacts exist and the official formulas are used.

### External source status

Vaaler's paper is the correct H4 source: Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bulletin of the American Mathematical Society* 12(2), 183--216, 1985; the uploaded PDF title page identifies the article and journal metadata. The relevant source-audit anchors from later local audits remain Vaaler Theorem 6 for the coefficient function and Theorem 18 for the periodic sawtooth residual, but H4 is still `source_audit_required` until the page/equation translation is finalized.

Li--Yang remains a comparison guardrail only. The arXiv record identifies Xiaochun Li and Xuerui Yang's paper and states that it uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley's second-spacing results. No Round 2 output supplies a theorem-hypothesis match that would import Li--Yang at the endpoint.

## Rejected or risky ideas

1. **Reject promotion of `M9-near-collision-taxonomy`.**
   A2's taxonomy is incomplete. It has an unclassified residue, denominator-paired and semi-diagonal classes are not rigorously estimated, and near-collision bands are entirely open.

2. **Reject A2's exact diagonal constant for the whole core.**
   The accepted statement is only that the named core diagonal families are compatible with the target:

$$
   O(D^2)\le O(X).
$$

   Do not record $\frac{1}{16}D^2$ as the union bound. A2's own calculation indicates a factor $3/16$ for three named positive families, and overlaps still require clean bookkeeping.

3. **Reject denominator-paired negligibility as proved.**
   A2 reports small numerical examples suggesting $O(D\log H)$, but no reproducible script or divisor/gcd proof is supplied. Numerical scaling is not proof.

4. **Reject the dual-length explosion as a route-closing theorem.**
   It is a diagnostic for one Poisson/continuous-relaxation route. It does not rule out fourth moments, direct signed bilinear estimates, residue interference, or a tailored spacing argument.

5. **Reject A3's proposed evidence patch until artifacts exist.**
   `M9-regression-raw-vs-paired` remains `proposed`. The required outputs are script, command, table, precision log, and report; a prose plan or unexecuted code is not enough.

6. **Reject any promotion of `M9`, `M9-M2`, `M9-near-collision-estimate`, `GC-target`, `H4`, or `Li-Yang-source-audit`.**
   No uniform endpoint estimate is proved, H4 remains source-audit-dependent, and Li--Yang remains an audited comparison source rather than a dependency.

## Known gaps

1. **H4 source audit.**
   The coefficient formula and residual majorant are used in the current normalization, but final proof-draft status still depends on the Vaaler source card.

2. **Exact $N=0$ taxonomy.**
   Direct diagonal, pair-swapped, and sign-symmetric families are identified. Reduced-fraction/semi-diagonal, denominator-paired, mixed, truncation-edge, and unclassified classes still need proof-level classification or explicit open status.

3. **Near-collision estimate.**
   The fourth-moment route needs bounds for

$$
   0<|N|\lesssim D^4/X
$$

   and for larger oscillatory bands. No such estimate is proved.

4. **Coefficient-weighted counting.**
   Any exact or near-collision count must use the actual

$$
   \beta_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h},
$$

   not a Fejer-linear surrogate or arbitrary bounded coefficients.

5. **Paired formula hypothesis.**
   The paired real formula is valid for real $w_D$ only. Complex weights must use the raw two-sided formula.

6. **A3 formula normalization.**
   A3's computational plan must use the official M1/M2 phases and outer constants, or explicitly state that it is testing normalized internal sums.

7. **Li--Yang theorem applicability.**
   Structural similarity of reciprocal phases is not enough. Any future invocation must match the theorem's exact $F,g,G,H,M,T$ hypotheses, coefficient class, weights, absolute-value placement, and endpoint height.

## New lemmas to add

### Lemma L-R2-1: exact $\mathcal M_2$ beta coefficient

Status: already `derived_under_assumptions`; keep H4 dependency.

Statement:

$$
C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h},
$$

and, assuming

$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

one has

$$
\beta_{h,H}
=
\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Thus $\beta_{-h,H}=\beta_{h,H}\in\mathbb R$.

### Lemma L-R2-2: bounded-scope weighted $h$-Cauchy sign loss

Status: already `derived_under_assumptions`; keep as diagnostic.

Statement:

For

$$
S_2=\sum_h \alpha_h C_h B_h,
$$

the positive $|\alpha_h|$-weighted Cauchy step gives

$$
|S_2|^2
\le
\left(\sum_h|\alpha_h|\right)
\sum_h|\alpha_h||C_h|^2|B_h|^2,
$$

and

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

Hence the $\chi_4(h)$ sign is lost in that normalization.

### Lemma L-R2-3: two-sided fourth-moment expansion

Status: already `derived_under_assumptions`; keep algebra-only.

Statement:

For

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

the two-sided fourth moment has phase

$$
\frac{X}{4}
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right),
$$

with numerator

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

No analytic estimate follows from this expansion alone.

### Lemma L-R2-4: diagonal-core compatibility sublemma

Status: create as `open`.

Statement:

For the actual $\beta_h$ coefficients and bounded dyadic weights, the direct diagonal, pair-swapped, and sign-symmetric exact $N=0$ families in the $\mathcal M_2$ fourth moment have total weighted mass

$$
O_\epsilon(D^2)
$$

and hence

$$
O_\epsilon(X)
$$

in the active range $D\le X^{1/2}$.

This should be proved carefully by A2, with overlap conventions and the exact coefficient bound from H4.

## Counterexample checks to run

1. **Complex-weight paired-formula failure.**
   Use a non-real dyadic weight and verify that the paired real formula fails while the raw two-sided formula remains correct.

2. **Raw-vs-paired real-weight regression.**
   Use the actual Vaaler coefficient $\Phi$, official M1/M2 phases, and real dyadic weights. Report absolute and relative errors.

3. **Exact $N=0$ enumeration.**
   Enumerate small ranges using the corrected numerator. Report diagonal, pair-swapped, sign-symmetric, semi-diagonal, denominator-paired, mixed, truncation-edge, and unclassified bins.

4. **Unclassified residue investigation.**
   Reproduce A2's reported unclassified $N=0$ cases and either classify them, bound them, or preserve them as an explicit open class.

5. **Denominator-paired singular test.**
   Produce a reproducible script and a proof-oriented parameterization. Numerical evidence alone is insufficient.

6. **Near-collision bands.**
   Bin configurations by

$$
   |N|\le cD^4/X
$$

   and by dyadic ranges of $|N|$. Report signed mass, absolute mass, and coefficient-weighted mass.

7. **CRI ratio.**
   For real weights, compute

$$
   R_{\rm CRI}
   =
   \frac{|\Sigma_1-\Sigma_3|^2}
   {|\Sigma_1|^2+|\Sigma_3|^2}.
$$

   Values near $0$ support further CRI investigation; values near $1$ are neutral; values near $2$ are adverse.

8. **Direct signed bilinear gradient spacing.**
   Compute local spacing of

$$
   \nabla f(h,d)
   =
   \left(
   \frac{X}{4d},
   -\frac{hX}{4d^2}
   \right)
$$

   in endpoint and intermediate blocks. Compare signed, unsigned, and absolute-majorant matrix statistics.

9. **H4 coefficient bound audit.**
   Verify from Vaaler's source that the required coefficient bound, e.g. $|\Phi(u)|\le C$, is sufficient for all diagonal-capacity arguments.

## Research strategy adjustment

Round 3 should continue the M9/M2 track. Do not pivot to a different global decomposition.

Route comparison:

| Route | Role | Exact lemma needed | Why it might work | Fast falsification |
|---|---|---|---|---|
| Fourth moment for $\mathcal M_2$ | Primary | $|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}$ uniformly in $D$ | Retains the fourfold $\beta_h$ character product before absolute-value loss | Exact plus near-collision bins have signed or absolute mass $\gg X^{1+c}$ with no remaining oscillation |
| CRI/residue interference | Diagnostic/secondary | $|\Sigma_1-\Sigma_3|\ll_\epsilon X^{1/4+\epsilon}$ with favorable cross-correlation | Directly tests cancellation between $h\equiv1$ and $h\equiv3\pmod4$ | $R_{\rm CRI}$ persistently near $1$ or $2$ in endpoint blocks |
| Direct signed bilinear estimate | Backup | Fixed-coefficient reciprocal bilinear estimate for $\beta_h$ weights | Avoids immediate weighted $h$-Cauchy sign loss | First proof step replaces $\beta_h$ by $|\beta_h|$ or by a character-blind operator norm |

The next round should allocate most A2 effort to a proof-draft-ready exact $N=0$ taxonomy and most A3 effort to executable diagnostics. A1 should keep source-card discipline and state mutation conservative.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "M9-M2-N0-diagonal-core-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Diagonal-core bound for exact M2 fourth-moment resonances",
        "status": "open",
        "statement_tex": "For the actual beta_h coefficients and bounded dyadic weights, the direct diagonal, pair-swapped, and sign-symmetric exact N=0 families in the M2 fourth moment have total weighted mass O_epsilon(D^2), hence O_epsilon(X) for D <= X^(1/2).",
        "dependencies": [
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion",
          "H4"
        ],
        "implies": [
          "M9-near-collision-taxonomy"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_002/responses/A2-002.md",
            "rounds/obligation-main/round_002/reviews/A1.md",
            "rounds/obligation-main/round_002/human/stage-b-review-audit.md"
          ]
        },
        "owner": "A2",
        "next_action": "Prove the bound with actual beta_h weights, bounded dyadic weights, explicit overlap conventions, and the H4 coefficient bound; do not use the incorrect 1/16 constant for the whole union."
      }
    ],
    "update": [
      {
        "id": "M9-M2-character-factor",
        "status": "open",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_002/responses/A1-002.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_002/responses/A2-002.md",
            "rounds/obligation-main/round_002/responses/A3-002.md",
            "rounds/obligation-main/round_002/reviews/A1.md"
          ]
        },
        "next_action": "Use the exact beta_h algebra and the h-Cauchy sign-loss diagnostic to pursue the M2 fourth-moment route first; keep CRI and direct signed bilinear estimates as secondary diagnostics."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "blockers_added": [
          "M9-M2-N0-diagonal-core-bound"
        ],
        "evidence_added": {
          "positive": [],
          "negative": [
            "rounds/obligation-main/round_002/reviews/A1.md",
            "rounds/obligation-main/round_002/human/stage-b-review-audit.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_002/responses/A2-002.md"
          ]
        },
        "next_action": "Complete the exact N=0 taxonomy using the corrected numerator N and actual beta_h weights. Resolve or explicitly preserve the unclassified class, prove or downgrade denominator-paired estimates, and formulate near-collision bands using |N| lesssim D^4/X."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "proposed",
        "evidence_added": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_002/responses/A3-002.md",
            "rounds/obligation-main/round_002/reviews/A1.md"
          ]
        },
        "next_action": "Produce committed or repository-ready artifacts: computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and computations/m9_regression/report.md. Use the official M1/M2 raw formulas and actual Vaaler coefficients; label all evidence diagnostic_only."
      },
      {
        "id": "M9-M2-fourth-moment-expansion",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_002/responses/A1-002.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_002/responses/A2-002.md"
          ]
        },
        "next_action": "Use this only as an algebraic expansion. A2 should classify exact and near-collision configurations with actual beta_h weights; do not infer an analytic estimate from the expansion alone."
      }
    ],
    "reject": [
      {
        "id": "A2-R2-near-collision-taxonomy-promotion",
        "reason": "Rejected because the proposed taxonomy contains an unclassified class, denominator-paired and semi-diagonal estimates are not proved, and near-collision bands are open."
      },
      {
        "id": "A2-R2-denominator-paired-negligibility-proved",
        "reason": "Rejected because the claim is supported only by small numerical examples without a reproducible script or a divisor/gcd proof."
      },
      {
        "id": "A2-R2-dual-length-explosion-route-closing",
        "reason": "Rejected as a route-closing theorem. The dual-length calculation is a diagnostic for one Poisson or continuous-relaxation path, not an obstruction to all fourth-moment, CRI, or signed bilinear methods."
      },
      {
        "id": "A2-R2-diagonal-core-one-sixteenth-union-constant",
        "reason": "Rejected because A2's own calculation for three positive core families gives a factor 3/16 before overlap bookkeeping, not 1/16 for the whole union. The safe state-level claim is only O(D^2) <= O(X)."
      },
      {
        "id": "A3-R2-artifact-evidence-without-files",
        "reason": "Rejected because M9-regression-raw-vs-paired requires actual script, command, table, precision log, and report. A prose plan or unexecuted code is not positive evidence."
      },
      {
        "id": "A3-R2-official-formula-normalization-unverified",
        "reason": "Rejected as state evidence until the computation uses the official raw M1/M2 formulas and the actual Vaaler coefficient Phi rather than provisional or normalized surrogate formulas."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform endpoint estimates for both M1 and M2 were proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 2 did not address the M1 endpoint estimate."
      },
      {
        "id": "M9-M2",
        "reason": "The M2 endpoint estimate remains open; only algebraic reductions and diagnostics were refined."
      },
      {
        "id": "M9-near-collision-estimate",
        "reason": "No estimate for near-collision bands was proved."
      },
      {
        "id": "M9-endpoint-uniformity",
        "reason": "No new uniform-in-D estimate was proved."
      },
      {
        "id": "GC-target",
        "reason": "The final theorem remains conditional on M9."
      },
      {
        "id": "H4",
        "reason": "Vaaler source audit remains required."
      },
      {
        "id": "H4-source-audit",
        "reason": "No final rendered-page source card was completed in Round 2."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a source-audit guardrail and is not used as a proof dependency."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 3,
    "idea_quality_score": 7,
    "state_evidence_score": 3,
    "calibration_score": 6,
    "reason": "Round 2 made useful algebraic and strategic progress on M2 and identified the fourth-moment route as primary, but no endpoint estimate, complete taxonomy, near-collision bound, or executable computation evidence was supplied."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, `M9-M2-N0-diagonal-core-bound`, and state maintenance.

Objectives:

1. Insert the proof-draft-ready $\mathcal M_2$ coefficient normalization into the proof draft, preserving H4 dependency:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   \beta_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h}.
$$

2. State the raw two-sided formula and the paired real formula, with the real-weight hypothesis explicit.

3. Write the fourth-moment expansion using the exact coefficient product and corrected numerator $N$.

4. Add a small lemma-bank entry for `M9-M2-N0-diagonal-core-bound` as open, not proved. State exactly what A2 must prove.

5. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open.

6. Exploratory allocation: compare fourth moment, CRI, and direct signed bilinear routes in one page, with one falsification criterion for each.

Verification tasks:

- Check H4 source-card dependency before any coefficient bound such as $|\Phi(u)|\le C$ is used.
- Confirm that any paired implementation formula is labelled invalid for complex weights.

### For A2

Target obligations: `M9-near-collision-taxonomy`, `M9-M2-N0-diagonal-core-bound`, and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Use one fixed two-sided convention:
$$
   1\le |h|\le H_D.
$$

2. Use the actual $\beta_h$ coefficients and the corrected numerator
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

3. Prove or explicitly mark open the `M9-M2-N0-diagonal-core-bound` lemma. Do not use the incorrect $\frac{1}{16}D^2$ constant for the whole core.

4. Produce a taxonomy table with columns:
   - family name;
   - defining equations;
   - proof that $N=0$;
   - coefficient product;
   - mass bound;
   - status;
   - remaining edge cases.

5. Resolve or preserve as open the unclassified exact $N=0$ residue reported in the small enumeration.

6. Downgrade denominator-paired negligibility unless a proof is supplied.

7. Define near-collision bands using
$$
   |N|\lesssim D^4/X
$$
   and state the first exact theorem needed to bound them.

8. Repair or alternative route: formulate the direct signed bilinear route as a precise lemma with coefficient class, matrix or spacing norm, dependency on a named theorem if any, and a fast falsification test.

Verification tasks:

- Supply either proof or reproducible computation for every numerical claim.
- Label central claims only as `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

### For A3

Target obligation: `M9-regression-raw-vs-paired`.

Objectives:

1. Produce actual repository-ready artifacts, not only a protocol:
   - `computations/m9_regression/run.py`;
   - `outputs/table_small.csv`;
   - `computations/m9_regression/precision.log`;
   - `computations/m9_regression/report.md`.

2. Use the official raw two-sided M1/M2 formulas and actual Vaaler coefficients. If H4 source audit is not final, clearly mark the coefficient as provisional and separate structural tests from quantitative tests.

3. For real dyadic weights, verify raw two-sided sums equal the paired real formulas.

4. For complex weights, verify paired real formulas fail unless modified.

5. Include explicit checks:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   |C_h|^2=4\,1_{2\nmid h},
   \qquad
   \beta_{-h}=\beta_h.
$$

6. Implement small exact fourth-moment binning with the corrected $N$ and actual $\beta_h$ weights. Report exact $N=0$ bins, unclassified bins, and near-collision bands.

7. Compute CRI ratios:
$$
   R_{\rm CRI}
   =
   \frac{|\Sigma_1-\Sigma_3|^2}
   {|\Sigma_1|^2+|\Sigma_3|^2}.
$$

8. Compute one bilinear gradient-spacing diagnostic using
$$
   \nabla f(h,d)=
   \left(
   \frac{X}{4d},
   -\frac{hX}{4d^2}
   \right).
$$

Verification tasks:

- Record command line, Python version, precision settings, table schema, and pass/fail assertions.
- Label all output `diagnostic_only`.
- Do not use surrogate kernels as official evidence; put any toy kernel in a separate exploratory appendix.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.0 | 7.0 | 8.0 | Strong algebraic normalization and conservative state handling. Best basis for the judge synthesis. |
| A2 | 7.5 | 3.0 | 4.5 | Strong route ideas and useful fourth-moment focus, but overpromotes incomplete taxonomy, numerical claims, and unproved denominator-paired estimates. |
| A3 | 6.5 | 2.5 | 6.0 | Good diagnostic design, but evidence is not committed/executed and uses provisional or possibly non-official normalizations. |

Overall, Round 2 is useful but not proof-level endpoint progress. The fourth-moment route is now the primary M2 research direction. The direct signed bilinear route remains the backup. Computation remains diagnostic only until actual files and outputs exist.

## Confidence

High confidence in the accepted algebraic identities for $C_h$, $\beta_h$, and the fourth-moment numerator $N$ under the stated H4 convention.

High confidence that weighted $h$-Cauchy loses the $\chi_4(h)$ sign and that unweighted $h$-Cauchy has an endpoint diagonal problem.

High confidence that `M9`, `M9-M2`, `M9-near-collision-taxonomy`, and `GC-target` should not be promoted.

Moderate confidence that the fourth-moment route is the best current primary route for $\mathcal M_2$.

Moderate confidence that the direct signed bilinear route is a useful backup after it is formulated as a precise theorem.

Low confidence in A2's claimed complete taxonomy, denominator-paired bound, and exact constants.

Low confidence in A3's computation as state evidence until actual scripts, command lines, tables, logs, and reports are present.