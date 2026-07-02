## Selected main route

Round 5 should be synthesized as proof-graph consolidation plus a pivot in the M2 fourth-moment route. No output proves `M9`, `M9-M2`, `M9-M1`, or `GC-target`. The useful state-safe progress is narrower:

1. A4's elementary average-to-pointwise interpolation lemma is valid as a standalone calculus lemma.
2. Its application to $S_2(D;X)$ is conditional on a strong local fourth-moment hypothesis and does not prove `M9-M2`.
3. A4's denominator-paired near-collision analysis is a useful scoping result, but it depends on the H4/beta odd-frequency support when used in the M2 graph.
4. A2's pair-swapped proof is useful evidence for the paired-core subfamilies under H4; A2's fraction-matching proof should be renamed and separated from the official denominator-pattern "semi-diagonal" terminology unless definitions are reconciled.
5. A3 supplied a strong diagnostic design, but it remains `diagnostic_only` until materialized, compiled, executed, and archived.

This synthesis follows the Round 5 judge packet and Stage B review record, especially the recommendations that the AP lemma be accepted only as an elementary interpolation lemma, that `M9-M2-fourth-moment-average-to-pointwise` remain open with the fattened local band recorded, that A3's computation remain diagnostic until executed, and that A2's continuous $L^4$ orthogonality route be rejected as stated.

### Primary route for Round 6

Primary route: **unpaired exact and near-collision analysis for the M2 fourth moment**, with the local fourth-moment obstruction explicitly separated.

The object remains

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
H_D\asymp DX^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

The exact fourth-moment resonance numerator is

$$
N=
h_1d_2d_3d_4
-h_2d_1d_3d_4
+h_3d_1d_2d_4
-h_4d_1d_2d_3.
$$

The primary proof obligation is now:

$$
\sum_{\substack{
1\le |h_i|\le H_D,\ d_i\asymp D\\
N=0\\
\text{not already in pair-equality, denominator-paired, pair-swapped, or fraction-matching classes}
}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\ll_\epsilon D^2X^\epsilon
$$

or else construct a lower-bound family showing that the scale is larger.

Why this route is selected: denominator-paired and paired-core work has reached diminishing returns. A4's DP scoping suggests that the critical remaining exact and near-collision mass lies in unpaired-denominator configurations, while A2/A4 both show that paired or fraction-matching subfamilies do not exhaust exact $N=0$.

Fast falsification criterion: if A3's exact-integer enumeration finds an unpaired or unclassified family with absolute beta-weighted mass growing faster than $D^2X^{o(1)}$ and not explained by fraction-matching/coprime-rigidity, then the absolute exact-resonance route must be revised or replaced by a signed route.

### Backup route

Backup route: **direct sign-preserving bilinear / reciprocal-spacing estimate**.

The theorem-shaped target is still

$$
S_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly in the active dyadic range, while retaining the $\chi_4(h)$ sign in

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

A4's proposed sign-preserving discrepancy route and A3's signed-vs-unsigned diagnostics should be kept alive, but not promoted. The bounded-coefficient version is false by an adversarial-sign mechanism, so any theorem must exploit the actual smooth dyadic weight and the specific reciprocal sequence.

Fast falsification criterion: if A3's true $\beta_h$ statistics track unsigned, random-sign, or adversarial-sign variants across endpoint blocks, deprioritize the signed route.

## Useful fragments by source

### A1

A1 contributed proof-infrastructure consolidation: H4 source-card content, the R5 positive-Fejer product-count proof, official M1/M2 definitions, and the raw/cosine/real-paired M2 formulas. This remains source-audit/proof-draft material, not a new analytic estimate.

Useful retained formulas:

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

For M2,

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

and, under H4,

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

The complex-weight cosine pairing is algebraic; the false shortcut is replacing the cosine sum by $\operatorname{Re}B_h$ for complex $w_D$.

### A2

A2's pair-swapped exact-resonance proof is useful. With

$$
d_1=d_4=a,\qquad d_2=d_3=b,
$$

the resonance equation is

$$
(h_1-h_4)b+(h_3-h_2)a=0,
$$

which is mapped to the denominator-paired equation by the involution $h_2\leftrightarrow h_4$, preserving the absolute reciprocal weight.

A2's fraction-matching proof is also useful but must be renamed. The family

$$
\frac{h_1}{d_1}=\frac{h_2}{d_2},
\qquad
\frac{h_3}{d_3}=\frac{h_4}{d_4}
$$

has plausible mass $O(D^2)$ by the parameterization $h_i=k_i u$, $d_i=k_i v$, dyadic harmonic sums $\sum_{k\asymp D/v}1/k\ll1$, and a convergent $\sum_{u\ne0}u^{-2}$. The Stage B review correctly warns that this is not necessarily the official denominator-pattern semi-diagonal family.

A2's continuous $L^4$ orthogonality proposal is rejected as stated. Orthogonality over $[0,1]$ does not isolate rational non-integer frequencies; one would need an integerized kernel based on the cleared numerator $N$, which changes the problem.

### A3

A3's diagnostic design is valuable: raw-vs-paired regression, exact $N=0$ binning, denominator-paired identity checks, near-collision bins, signed-vs-unsigned tests, and average-to-pointwise diagnostics. However, the submitted bundle is still a code-and-command plan using placeholder $\Phi$ in visible snippets; it is not positive theorem evidence until scripts exist, compile, run, and produce CSV/log/report outputs.

A3 must separate three M2 formula tests:

$$
\text{raw two-sided formula},
$$

$$
\text{complex-weight cosine pairing},
$$

and

$$
\operatorname{Re}B_h\text{ shortcut}.
$$

For complex weights, the cosine pairing using the same complex weight in the $h$ and $-h$ raw terms is valid; the $\operatorname{Re}B_h$ shortcut is the false formula.

### A4

A4 supplied the strongest analytic contribution. The elementary lemma is:

For $F\in C^1(I)$, $|I|=\delta$, and $X_0\in I$,

$$
|F(X_0)|^4
\le
\frac1\delta\int_I |F|^4
+
4\sup_I |F'|\delta^{1/4}
\left(\int_I |F|^4\right)^{3/4}.
$$

This is accepted as `proved_internal` as a standalone calculus lemma.

Applied to $S_2(D;X)$ with

$$
\delta=\frac{X^{1/2}}D,
$$

the interpolation step is formally exponent-lossless if one already has a local fourth-moment estimate of strength $X^{1+\epsilon}$ on every such window. But the local moment must control the much fatter band

$$
|N|\ll \frac{D^4}{\delta}=D^5X^{-1/2},
$$

not merely the global pointwise band $|N|\ll D^4/X$; it must hold on every local window; and at $D=X^{1/2}$ the window length is $\asymp1$, so averaging buys essentially nothing.

A4's denominator-paired near-collision observation is also useful. In the DP class,

$$
d_1=d_2=a,\qquad d_3=d_4=b,
$$

one has

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a.
$$

Since $\beta_h$ is supported on odd $h$, both differences are even, so nonzero $L$ has $|L|\ge2$ up to dyadic conventions. This gives an emptiness criterion for the thin band away from the top range, but it is H4/beta-dependent when used in the M2 proof graph.

## Rejected or risky ideas

1. **No endpoint promotion.** Reject any promotion of `M9`, `M9-M2`, `M9-M1`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

2. **No full taxonomy claim.** Pair-swapped, denominator-paired, and fraction-matching families do not exhaust exact $N=0$.

3. **A2's continuous $L^4$ exactness claim is invalid as stated.** Rational-frequency orthogonality over $[0,1]$ does not isolate the reciprocal collision equation. A corrected circle-method route must use an integer frequency, likely involving the cleared numerator $N$.

4. **A2's "semi-diagonal" label is unsafe.** If the official semi-diagonal family is denominator-pattern based, A2's proof did not discharge it.

5. **A3's bundle is not yet state evidence.** It is a plan or artifact specification until the files are materialized and run.

6. **A4's AP lemma does not prove the local fourth moment.** It only shows that a sufficiently strong local fourth moment would imply a pointwise bound.

7. **A4's DP near-collision result should not be unconditional in the M2 graph.** Its parity input uses the odd support of actual $\beta_h$, which depends on H4/beta algebra.

8. **Fraction-collision mass $\asymp D^2$ is a sharpness benchmark, not an obstruction to the target.** Since $D^2\le X$ in the active range, this mass is compatible with the fourth-moment scale $X^{1+\epsilon}$.

9. **No black-box import of Vaaler, Li--Yang, Huxley, Bombieri--Iwaniec, Guth--Maldague, or Bourgain-Watt beyond source-audited statements.** The Round 5 record explicitly keeps such uses as source-audit or literature-anchor material.

## Known gaps

1. `H4-source-audit` is still not physically complete. It should now also include the regularity needed for the $H_D$-freezing discussion, especially a verified Lipschitz or derivative bound for $\Phi$ on the relevant interval.

2. `R5-Full` remains conditional on H4. A1's product-count proof is good infrastructure but should not become `proved_internal` until H4/source-card validation is complete.

3. The local fourth-moment hypothesis `(LFM)` is open. A global fourth moment does not imply it because $[X,2X]$ contains about $DX^{1/2}$ coherence-length windows.

4. At the endpoint $D=X^{1/2}$, the AP bridge degenerates: $\delta\asymp1$.

5. The unpaired exact $N=0$ class is not bounded.

6. The unpaired near-collision band is not bounded.

7. A3's exact taxonomy classifier is not yet synchronized with the terms `semi-diagonal`, `fraction-matching`, `fraction-collision`, `mixed`, and `unclassified`.

8. `M9-M1` remains untouched analytically.

9. `M9-endpoint-uniformity` remains open and should be attached to every proposed analytic estimate.

## New lemmas to add

### Lemma AP: local average-to-pointwise interpolation

Status: `proved_internal`.

For $F\in C^1(I)$, $|I|=\delta$, and $X_0\in I$,

$$
|F(X_0)|^4
\le
\frac1\delta\int_I |F|^4
+
4\sup_I |F'|\delta^{1/4}
\left(\int_I |F|^4\right)^{3/4}.
$$

This is a pure real-analysis lemma. It does not depend on H4.

### Local fourth-moment hypothesis for $S_2$

Status: `open`.

For every active $D$ and every interval $I$ of length

$$
\delta=X^{1/2}/D,
$$

prove

$$
\frac1\delta\int_I |S_2(D;t)|^4\,dt
\ll_\epsilon X^{1+\epsilon},
$$

with actual $\beta_h$ coefficients and with the local resonance band

$$
|N|\ll D^5X^{-1/2}
$$

controlled. This is the missing analytic hypothesis behind the AP bridge.

### Denominator-paired near-collision scoping lemma

Status: `derived_under_assumptions`.

In the DP class,

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a.
$$

Under the H4-dependent odd support of $\beta_h$, nonzero $L$ is even, so the thin band is empty unless

$$
D\ge \sqrt{2X/C_0'}
$$

with constants depending on the dyadic convention. Where nonempty, the thin DP mass should be bounded by a harmonic-convolution argument. This removes DP near-collisions from the main critical path, after validator-ready dyadic bookkeeping.

### Coprime-rigidity normal form

Status: `proved_internal`.

A pure rational normal form should be recorded for exact $N=0$ after reducing fractions $h_i/d_i$ to lowest terms. It should be used to search systematically for unpaired exact and near-collision configurations.

### Fraction-matching weighted exact-resonance family

Status: `derived_under_assumptions`.

For the family

$$
h_1/d_1=h_2/d_2,\qquad h_3/d_3=h_4/d_4,
$$

the absolute reciprocal-weighted mass is $\ll D^2X^\epsilon$ under H4/beta magnitude assumptions. Its lower-bound or sharpness role should be kept separate from identification with A3's unclassified bin.

### Reciprocal signed discrepancy / SPD proposal

Status: `proposed`.

A possible direct signed route is a smooth-weighted discrepancy estimate for truncated sawtooth sums at reciprocal points

$$
\vartheta_d^{(\rho)}=\frac{X+\rho d}{4d},
\qquad
\rho\in\{1,3\}.
$$

This remains exploratory and should be tested by A3 before receiving proof-graph emphasis.

## Counterexample checks to run

1. **Terminology/classifier audit.** Freeze definitions of `semi-diagonal`, `fraction-matching`, `fraction-collision`, `mixed`, and `unclassified`.

2. **A2 continuous orthogonality falsification.** Explicitly compute a nonzero rational-frequency case such as

$$
\int_0^1 e(\alpha/2)\,d\alpha\ne0.
$$

3. **Fraction-collision overlap test.** A3 should test whether A4's fraction-collision construction is classified as semi-diagonal, fraction-matching, or unclassified.

4. **Unpaired exact enumeration.** Enumerate exact $N=0$ tuples with exact integer arithmetic and compare unpaired mass against $D^2$, $D^2\log^A D$, $D^{5/2}$, and $D^3$.

5. **Local fourth-moment windows.** For $\delta=X^{1/2}/D$, compute local fourth moments over many windows and compare against global fourth moment concentration.

6. **Endpoint AP failure mode.** At $D=X^{1/2}$, test whether the AP inequality gives anything beyond direct pointwise fourth-power control.

7. **DP near-collision constants.** Verify the parity dichotomy under the exact dyadic convention $D\le d<2D$ or the chosen smooth support.

8. **Raw-vs-paired M2 regression.** Verify raw two-sided, complex-weight cosine pairing, real-weight paired formula, and failure of the complex-weight $\operatorname{Re}B_h$ shortcut.

9. **Signed-vs-unsigned tests.** Compare true $\beta_h$, $|\beta_h|$, random signs, and adversarial signs at $D=X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

10. **H4 regularity check.** Confirm from the Vaaler source card that the $\Phi$ regularity needed for freezing $H_D$ is available.

## Research strategy adjustment

The next round should pivot from paired-core exact-resonance bookkeeping to unpaired configurations and local fourth-moment structure.

Route comparison:

| Route | Status after Round 5 | Why keep or demote | Fast falsification |
|---|---:|---|---|
| Unpaired exact/near-collision taxonomy | Primary | Paired-core and DP are no longer the main critical path; unpaired mass is the unresolved obstruction. | A3 finds unpaired mass above $D^2X^{o(1)}$ or a low-dimensional family exceeding target scale. |
| Local fourth-moment bridge | Secondary | AP lemma is valid, but it requires `(LFM)` on every coherence window and a fatter band. | Endpoint $D=X^{1/2}$ or exceptional windows make local control equivalent to pointwise control. |
| Direct signed bilinear/SPD | Backup | May exploit $\chi_4(h)$ where absolute fourth moments cannot. | True signs behave like unsigned/adversarial signs in A3 diagnostics. |
| Black-box Li--Yang/Huxley/BI import | Not selected | Source cards and parameter ranges remain incomplete; known exponents do not reach $1/4$. | Any missing theorem hypothesis fails at $D=X^{1/2}$ or $H_D=X^{1/4}$. |
| Continuous $L^4$ orthogonality over $[0,1]$ | Rejected as stated | Rational non-integer phases are not orthogonal on $[0,1]$. | Direct rational-frequency integral counterexample. |

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "M9-M2-average-to-pointwise-AP-lemma",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Elementary local average-to-pointwise interpolation lemma",
        "status": "proved_internal",
        "statement_tex": "For F in C^1(I), |I|=delta, and X0 in I, |F(X0)|^4 <= delta^(-1) int_I |F|^4 + 4 sup_I |F'| delta^(1/4) (int_I |F|^4)^(3/4).",
        "dependencies": [],
        "implies": [
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A4-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Insert the AP lemma into the lemma bank as a standalone calculus lemma; keep all S2 applications separate and conditional."
      },
      {
        "id": "M9-M2-local-fourth-moment-LFM",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Everywhere-local fourth-moment estimate for S2 on coherence windows",
        "status": "open",
        "statement_tex": "For active D and every interval I of length delta=X^(1/2)/D near X, prove delta^(-1) int_I |S_2(D;t)|^4 dt <<_epsilon X^(1+epsilon) with actual beta_h coefficients. The local expansion must control the fattened band |N| << D^5 X^(-1/2).",
        "dependencies": [
          "M9-M2-fourth-moment-expansion",
          "M9-M2-average-to-pointwise-AP-lemma",
          "M9-endpoint-uniformity"
        ],
        "implies": [
          "M9-M2-fourth-moment-average-to-pointwise"
        ],
        "blockers": [
          "M9-near-collision-estimate",
          "M9-endpoint-uniformity"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A4-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "owner": "A4",
        "next_action": "State and attack a local fourth-moment estimate on every interval of length X^(1/2)/D; include the fattened resonance band, exceptional-window issue, and endpoint D=X^(1/2) subcase."
      },
      {
        "id": "M9-M2-DP-near-collision-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Denominator-paired near-collision scoping bound",
        "status": "derived_under_assumptions",
        "statement_tex": "In the denominator-paired class d1=d2=a, d3=d4=b, N=ab L with L=(h1-h2)b+(h3-h4)a. Under the H4 beta support on odd h, nonzero L is even. Hence the thin band 0<|N|<=C0 D^4/X is empty unless D >= sqrt(2X/C0') up to dyadic constants; where nonempty its absolute beta-weighted mass is bounded by a harmonic-convolution estimate, and the full DP class is harmless at X^(1+epsilon) scale.",
        "dependencies": [
          "H4",
          "M9-M2-beta-algebra",
          "M9-M2-harmonic-convolution-LH",
          "M9-M2-denominator-paired-weighted-bound"
        ],
        "implies": [
          "M9-near-collision-estimate",
          "M9-near-collision-taxonomy"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "owner": "A4",
        "next_action": "Write validator-ready dyadic proof with constants, parity support, t=0 and t!=0 cases, and exact dependence on C0; do not use it to promote full near-collision estimates."
      },
      {
        "id": "M9-M2-coprime-rigidity-normal-form",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Coprime-rigidity normal form for exact reciprocal resonances",
        "status": "proved_internal",
        "statement_tex": "After reducing h_i/d_i to lowest terms, exact N=0 reciprocal resonances can be organized by denominator identities and a corresponding linear numerator equation. This is a pure rational normal-form lemma for classifying exact N=0 configurations.",
        "dependencies": [],
        "implies": [
          "M9-near-collision-taxonomy"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ],
          "negative": [],
          "inconclusive": [
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "owner": "A4",
        "next_action": "Write the normal form in proof-draft-ready notation and use it to define unpaired exact N=0 families."
      },
      {
        "id": "M9-M2-fraction-matching-weighted-bound",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Fraction-matching exact resonance bound",
        "status": "derived_under_assumptions",
        "statement_tex": "For the exact N=0 family h1/d1=h2/d2 and h3/d3=h4/d4, with d_i asymp D and 1<=|h_i|<=H_D, the absolute beta-weighted mass is <<_epsilon D^2 X^epsilon under the H4 beta magnitude hypothesis. This is a fraction-matching subfamily and should not be identified with the denominator-pattern semi-diagonal family until terminology is reconciled.",
        "dependencies": [
          "H4",
          "M9-M2-beta-algebra",
          "M9-M2-fourth-moment-expansion"
        ],
        "implies": [
          "M9-near-collision-taxonomy"
        ],
        "blockers": [
          "H4-source-audit"
        ],
        "evidence": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A2-005.md",
            "rounds/obligation-main/round_005/responses/A4-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A2",
        "next_action": "Rename consistently as fraction-matching or fraction-collision; verify endpoint truncations and prevent accidental promotion of the official semi-diagonal denominator-pattern subcase."
      },
      {
        "id": "M9-M2-reciprocal-SPD-route",
        "type": "lemma",
        "track": "M9_analytic",
        "title": "Sign-preserving reciprocal discrepancy route for M2",
        "status": "proposed",
        "statement_tex": "A sign-preserving discrepancy or first-spacing theorem for smooth-weighted truncated sawtooth sums at reciprocal points theta_d=(X+rho d)/(4d), rho in {1,3}, strong enough to imply S_2(D;X)<<_epsilon X^(1/4+epsilon) uniformly over active D.",
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
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ]
        },
        "owner": "A4",
        "next_action": "State the exact spacing statistic P(D,H;X), run A3 signed-vs-unsigned and first-spacing diagnostics, and audit Li-Yang only as a source guardrail."
      }
    ],
    "update": [
      {
        "id": "M9-M2-fourth-moment-average-to-pointwise",
        "status": "open",
        "blockers_added": [
          "M9-M2-local-fourth-moment-LFM"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A4-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A1-005.md"
          ]
        },
        "next_action": "Use the AP lemma only as an interpolation module. To advance this obligation, prove the everywhere-local fourth-moment estimate on windows delta=X^(1/2)/D, control the fattened band |N|<<D^5 X^(-1/2), handle exceptional windows, and split off the endpoint D=X^(1/2)."
      },
      {
        "id": "M9-near-collision-estimate",
        "status": "proposed",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "next_action": "Treat denominator-paired near-collisions as scoped by M9-M2-DP-near-collision-bound after proof-draft verification. Shift the main analytic target to unpaired-denominator near-collisions with exact beta weights."
      },
      {
        "id": "M9-near-collision-taxonomy",
        "status": "open",
        "blockers_added": [
          "M9-M2-local-fourth-moment-LFM"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A2-005.md",
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ],
          "negative": [
            "rounds/obligation-main/round_005/reviews/A1.md"
          ],
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A3-005.md"
          ]
        },
        "next_action": "Preserve mixed and unclassified exact N=0 classes. Reconcile semi-diagonal versus fraction-matching terminology, then prove or refute the unpaired exact N=0 mass bound."
      },
      {
        "id": "M9-M2-paired-core-weighted-bound",
        "status": "derived_under_assumptions",
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A2-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "next_action": "Keep paired-core families treated under H4, but do not use them to promote full exact N=0 taxonomy. Separate fraction-matching from official semi-diagonal terminology."
      },
      {
        "id": "M9-M2-N0-diagonal-core-bound",
        "status": "open",
        "blockers_added": [
          "M9-M2-fraction-matching-weighted-bound",
          "M9-M2-local-fourth-moment-LFM"
        ],
        "evidence_added": {
          "positive": [
            "rounds/obligation-main/round_005/responses/A2-005.md",
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ],
          "negative": [
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "next_action": "Do not promote from paired or fraction-matching subfamilies. Prove or refute mixed and unpaired exact N=0 mass before any status change."
      },
      {
        "id": "M9-fourth-moment-enumeration",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A3-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "next_action": "Materialize and run executable artifacts with exact integer arithmetic for N, official phases, true Phi after H4, raw/cosine/ReB_h formula tests, fraction-matching overlap tests, unpaired exact N=0 tables, local-window diagnostics, and signed-vs-unsigned comparisons."
      },
      {
        "id": "M9-regression-raw-vs-paired",
        "status": "diagnostic_only",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A3-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "next_action": "Rerun after materialization with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, complex-weight cosine pairing, real-weight Re B_h formula, and explicit failure of Re B_h for complex weights. Archive script, command, table, precision log, and report."
      },
      {
        "id": "H4-source-audit",
        "status": "source_audit_required",
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A1-005.md",
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ]
        },
        "next_action": "Commit sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, and the Phi regularity or Lipschitz fact needed for freezing H_D."
      },
      {
        "id": "M9-M2-direct-signed-bilinear-lemma",
        "status": "proposed",
        "blockers_added": [
          "M9-M2-reciprocal-SPD-route"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A4-005.md",
            "rounds/obligation-main/round_005/responses/A3-005.md"
          ]
        },
        "next_action": "Recast as a precise sign-preserving discrepancy or spacing theorem. Require A3 signed-vs-unsigned evidence before allocating major proof effort."
      },
      {
        "id": "M9-M2",
        "status": "open",
        "blockers_added": [
          "M9-M2-local-fourth-moment-LFM"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/obligation-main/round_005/responses/A1-005.md",
            "rounds/obligation-main/round_005/responses/A2-005.md",
            "rounds/obligation-main/round_005/responses/A3-005.md",
            "rounds/obligation-main/round_005/responses/A4-005.md",
            "rounds/obligation-main/round_005/reviews/A1.md"
          ]
        },
        "next_action": "Do not promote from AP, DP scoping, or paired/fraction subfamilies. Supply a pointwise M2 estimate, a local fourth-moment estimate valid at endpoint, or a sign-preserving direct estimate with uniformity."
      },
      {
        "id": "M9-endpoint-uniformity",
        "status": "open",
        "evidence_added": {
          "negative": [
            "rounds/obligation-main/round_005/responses/A4-005.md"
          ]
        },
        "next_action": "Require each M2 route to isolate the endpoint D=X^(1/2), where the AP/local-average bridge degenerates to pointwise control."
      }
    ],
    "reject": [
      {
        "id": "A2-R5-continuous-L4-rational-orthogonality",
        "reason": "Rejected because integral over alpha in [0,1] of e(alpha theta) does not vanish for arbitrary nonzero rational theta; the proposed continuous L4 identity does not exactly detect reciprocal exact resonance."
      },
      {
        "id": "A2-R5-semi-diagonal-terminology-promotion",
        "reason": "Rejected because A2's fraction-matching proof may not be the official denominator-pattern semi-diagonal family; it must be renamed or reconciled before being used as that subcase."
      },
      {
        "id": "A2-R5-full-exact-N0-taxonomy-promotion",
        "reason": "Rejected because paired and fraction-matching subfamilies do not exhaust exact N=0; unpaired and mixed classes remain open."
      },
      {
        "id": "A3-R5-unexecuted-artifact-positive-evidence",
        "reason": "Rejected because a code-and-command plan is not positive diagnostic evidence until files exist, compile, run, and produce tables, logs, and report output."
      },
      {
        "id": "A4-R5-AP-implies-M9-M2",
        "reason": "Rejected because Lemma AP only converts an everywhere-local fourth-moment hypothesis into a pointwise bound; it does not prove that local fourth-moment hypothesis."
      }
    ],
    "no_change": [
      {
        "id": "M9",
        "reason": "No uniform endpoint estimates for both M1 and M2 were proved."
      },
      {
        "id": "M9-M1",
        "reason": "Round 5 did not supply an analytic estimate for M1."
      },
      {
        "id": "GC-target",
        "reason": "The final Gauss circle target remains open because M9 is open."
      },
      {
        "id": "Conditional-bridge",
        "reason": "The bridge remains conditional on H4, R5-Full, and M9."
      },
      {
        "id": "R5-Full",
        "reason": "R5-Full remains derived_under_assumptions pending H4 source-card validation."
      },
      {
        "id": "H4",
        "reason": "H4 remains source_audit_required until the Vaaler source card is physically completed and validated."
      },
      {
        "id": "Li-Yang-source-audit",
        "reason": "Li-Yang remains a source-audit guardrail; no theorem is imported as a dependency for endpoint M9."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 5,
    "idea_quality_score": 8,
    "state_evidence_score": 5,
    "calibration_score": 7,
    "reason": "Round 5 adds a valid elementary AP interpolation lemma, sharpens the average-to-pointwise obstruction, scopes denominator-paired near-collisions, and isolates fraction-matching as a separate subfamily. It does not prove M9, M9-M2, M9-M1, the full exact N=0 taxonomy, or the final Gauss circle target."
  }
}

## Next-round prompts by agent

### For A1

Target obligations: `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, and proof-draft maintenance.

Objectives:

1. Complete or draft `sources/vaaler_1985.md` physically. Include the earlier required data plus the new Round 5 item: a source-card check for the regularity of

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u
$$

sufficient to justify freezing $H_D$ across windows of length $\delta=X^{1/2}/D$.

2. Insert into `state/best_proof_draft.md`:
   - H1-H3 statement;
   - H4 statement, still source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - official M1/M2 definitions;
   - M2 raw two-sided, complex-weight cosine, and real-weight paired formulas;
   - fourth-moment numerator $N$;
   - AP lemma;
   - local fourth-moment hypothesis `(LFM)`;
   - list of open endpoint and unpaired near-collision blockers.

3. Write a short proof-draft note explaining why AP is not a proof of `M9-M2`: it needs `(LFM)` on every interval of length $\delta=X^{1/2}/D$, the local expansion controls $|N|\ll D^5X^{-1/2}$, and the endpoint $D=X^{1/2}$ degenerates.

4. Reconcile terminology:
   - denominator-pattern semi-diagonal;
   - pair-swapped;
   - fraction-matching/fraction-collision;
   - mixed;
   - unclassified.

5. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Exploratory allocation: compare the absolute unpaired-exact route, the local fourth-moment `(LFM)` route, and the direct signed/SPD route. State for each the exact needed theorem and a one-line falsification test.

### For A2

Target obligations: `M9-near-collision-taxonomy`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-fraction-matching-weighted-bound`, and unpaired exact $N=0$ mass.

Objectives:

1. Do not re-prove denominator-paired exact resonance or pair-swapped exact resonance.

2. Reconcile terminology. If the official semi-diagonal family is

$$
d_1=d_3,\qquad d_2=d_4,\qquad d_2(h_1+h_3)=d_1(h_2+h_4),
$$

then either prove this exact denominator-pattern family or state explicitly that Round 5's fraction-matching proof is a different subfamily.

3. Write one proof-draft-ready lemma for an unpaired exact $N=0$ family. Choose one:
   - an upper bound $\ll D^2X^\epsilon$ for a well-defined unpaired class; or
   - a lower-bound construction showing a larger scale; or
   - a normal-form reduction that leaves a smaller explicit subproblem.

4. Repair or discard the continuous $L^4$ route. If repaired, use an integer frequency based on the cleared numerator $N$ and state the exact kernel. Do not use rational-frequency orthogonality over $[0,1]$.

5. Keep `M9`, `M9-M2`, and `M9-near-collision-taxonomy` open.

Exploratory allocation: propose one sign-preserving analytic inequality that would exploit $\chi_4(h)$ without Cauchy erasing the sign.

### For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-fourth-moment-enumeration`, `M9-M2-local-fourth-moment-LFM`, and signed-vs-unsigned/SPD diagnostics.

Objectives:

1. Materialize and execute the diagnostic bundle. Required outputs:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - `python -m py_compile` result;
   - precision log;
   - CSV schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Use exact integer arithmetic for $N$ and for all exact $N=0$ classification.

3. Implement and separately test:
   - raw two-sided M2;
   - complex-weight cosine pairing;
   - real-weight paired formula;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

4. Replace placeholder $\Phi$ with the audited Vaaler $\Phi$ once H4 is available. Until then, separate classification results from coefficient-magnitude results.

5. Taxonomy tests:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - official denominator-pattern semi-diagonal;
   - fraction-matching/fraction-collision;
   - mixed;
   - unclassified.

6. Test whether A4's fraction-collision family accounts for the previously unclassified exact mass.

7. Local fourth-moment diagnostics:
   - use $\delta=X^{1/2}/D$;
   - sample many windows;
   - report local fourth moment, global fourth moment, exceptional-window concentration, and the ratio to the AP-derived bound;
   - include endpoint $D=X^{1/2}$.

8. Near-collision diagnostics:
   - compare thin band $|N|\ll D^4/X$ and local fat band $|N|\ll D^5X^{-1/2}$;
   - split denominator-paired and unpaired-denominator cases.

9. Signed-vs-unsigned/SPD diagnostics:
   - true $\beta_h$;
   - unsigned $|\beta_h|$;
   - random signs;
   - adversarial signs;
   - reciprocal spacing statistic $P(D,H;X)$ if feasible.

All outputs remain `diagnostic_only`.

### For A4

Target obligations: `M9-M2-DP-near-collision-bound`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-coprime-rigidity-normal-form`, and unpaired near-collision search.

Objectives:

1. Write validator-ready proofs for:
   - DP parity emptiness with exact dyadic constants;
   - thin DP near-collision mass bound;
   - full DP-total mass bound;
   - dependence on H4/beta odd support.

2. Write the coprime-rigidity normal form in a compact lemma format suitable for `state/lemma_bank.md`.

3. Develop the `(LFM)` obstruction:
   - prove exactly how the local window creates the band $|N|\ll D^5X^{-1/2}$;
   - isolate whether an exceptional-window argument can convert a global fourth moment into `(LFM)` outside a small exceptional set;
   - state why the endpoint $D=X^{1/2}$ still requires separate control.

4. Attack one unpaired near-collision or exact-resonance subproblem using the coprime-rigidity normal form. Provide either a proof, a counterexample family, or a sharply reduced equation.

5. Keep the SPD/sign-preserving route exploratory. State the needed first-spacing statistic and the exact falsification test for A3.

Do not claim `M9-M2`, `M9`, or `GC-target`.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.0 | 7.5 | 8.5 | Strong infrastructure consolidation: H4/R5/M2 definitions, formulas, and average-to-pointwise obstruction. No endpoint overclaim. Needs physical source-card/proof-draft commits. |
| A2 | 7.2 | 5.6 | 6.2 | Pair-swapped and fraction-matching material is useful under H4. Calibration weaker because "semi-diagonal" terminology is unsafe and the continuous $L^4$ orthogonality route is false as stated. |
| A3 | 7.6 | 3.8 | 7.2 | Good diagnostic design and correct `diagnostic_only` framing, but no positive state evidence until scripts are materialized and executed; placeholder $\Phi$ must be replaced after H4. |
| A4 | 8.8 | 7.8 | 8.4 | Strongest analytic progress: AP lemma, local-fourth-moment obstruction, DP near-collision scoping, coprime-rigidity, and fraction-collision calibration. Some M2 applications remain H4-dependent and require dyadic proof-draft verification. |

Overall Round 5 assessment: moderate but real proof-graph progress. The main gain is not an M2 estimate; it is a sharper map of what any M2 fourth-moment proof must still supply.

## Confidence

Confidence: 0.82.

High confidence:
- `M9`, `M9-M1`, `M9-M2`, and `GC-target` remain open.
- Lemma AP is valid as an elementary calculus lemma.
- AP does not prove `M9-M2` without an everywhere-local fourth-moment estimate.
- A2's continuous $L^4$ exact-resonance identity is invalid as stated.
- A3's computations remain diagnostic until executed.

Moderate confidence:
- A2's fraction-matching $O(D^2)$ proof is correct after renaming and endpoint checks.
- A4's DP near-collision scoping is correct after dyadic-constant verification.
- Coprime-rigidity and fraction-collision are useful for the next unpaired taxonomy round.

Low confidence:
- Absolute fourth-moment taxonomy alone will reach endpoint M2.
- Existing Li--Yang/Guth--Maldague/Huxley/Bombieri--Iwaniec machinery can be imported without a much more exact source-card and parameter audit.
