# Round 4 Stage A Response Audit

## Scope

This audit covers the polished Stage A reasoning responses archived at:

- `rounds/obligation-main/round_004/responses/A1-004.md`
- `rounds/obligation-main/round_004/responses/A2-004.md`
- `rounds/obligation-main/round_004/responses/A3-004.md`
- `rounds/obligation-main/round_004/responses/A4-004.md`

The copied web responses were normalized with `python -m math_collab.normalize_markdown`. The normalized archive copies are now the public evidence files for Stage A. The handoff copies remain temporary local transfer files.

## Executive Assessment

Round 4 Stage A produced one state-promotable narrow result, conditional on H4:

`M9-M2-denominator-paired-weighted-bound` should be considered for promotion from `open` to `derived_under_assumptions`.

The cleanest evidence is A4's proof. A1 supplies an independent compatible proof. A2 also gives a proof for the same subfamily, but overlabels it `[PROVED]` despite the H4 source dependency and extends the conclusion too broadly. A3 supplies useful diagnostic plans but no fully materialized executable artifacts in this round.

No response proves `M9-M2`, `M9`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

## A1 Audit

### Useful Fragments

A1 gives the broadest proof-infrastructure packet. The useful parts are:

- formula-level H4 source audit claims for Vaaler Theorem 6, Section 7 definitions, and Theorem 18;
- a proof-draft-ready statement of the M2 coefficient convention;
- a conditional R5-Full reconciliation argument;
- an independent denominator-paired exact-resonance proof;
- an exact proposed near-collision theorem statement with threshold $0<|N|\le C_0D^4/X$.

A1's denominator-paired proof agrees with A4's route: write $a=ga'$, $b=gb'$, $(a',b')=1$, parametrize

$$
h_1-h_2=t a',
\qquad
h_3-h_4=-t b',
$$

then bound the frequency sums by harmonic convolutions. This is good independent support for the narrow denominator-paired obligation.

### Caveats

A1 overstates the source-audit endpoint if read as a final status change. The response may be enough to update the Vaaler source card, but `H4-source-audit` should not be treated as fully complete until `sources/vaaler_1985.md` is updated with page/equation checks and the project verifies the rendered-page transcription.

A1's R5-Full reconciliation is valuable but still needs to be inserted into `state/best_proof_draft.md` and audited against exact residual formulas. It should not be used to promote final theorem-level claims.

A1 proposes promoting the denominator-paired bound to `proved_internal` once H4 is accepted. In the current graph state, the safer status is `derived_under_assumptions` because the beta coefficient magnitude depends on `H4`/`H4-source-audit`.

## A2 Audit

### Useful Fragments

A2 supplies a gcd proof for the denominator-paired family that is broadly consistent with A1/A4:

$$
(h_1-h_2)b+(h_3-h_4)a=0
$$

with $a=ga'$, $b=gb'`, $(a',b')=1$, and

$$
h_1-h_2=k a',
\qquad
h_3-h_4=-k b'.
$$

The resulting split into $k=0$ and $k\ne0$ gives the correct scale:

$$
O(D^2)+O(D\log^2 H_D)\ll D^2X^\epsilon.
$$

A2 also correctly preserves the unclassified exact $N=0$ mass as open.

### Problems

A2's labels are not calibrated. The denominator-paired bound should not be labelled `[PROVED]` without qualification because it uses the H4-dependent coefficient bound $|\beta_h|\ll1/|h|`. The correct state label is at most `derived_under_assumptions`.

A2's extension to semi-diagonal and pair-swapped families is plausible for some specifically defined paired families, but it is not enough to promote `M9-M2-N0-diagonal-core-bound`. The response does not classify all exact $N=0$ families and explicitly leaves unclassified mass open.

A2's empirical claim that unclassified exact mass appears $O(D^2\log^2D)$ is not proof-level evidence unless backed by committed scripts/tables. Treat it as diagnostic-only or inconclusive.

A2's R5-Full/DDP-trap discussion is useful but too compressed. It should not by itself close `R5-Full-reconciliation`; the proof must be checked against the exact residual expression and H4 source convention.

## A3 Audit

### Useful Fragments

A3 stays correctly calibrated: it labels its material `diagnostic_only` and does not claim proof progress. It proposes useful diagnostic scope:

- raw two-sided versus paired real/complex cosine checks;
- exact $N=0$ binning;
- denominator-paired diagnostic tables;
- near-collision bands;
- R5 product-count diagnostics;
- signed/unsigned/random/adversarial coefficient comparisons.

### Problems

A3 says it cannot inspect Round 3 artifacts, even though they are available locally to the repository workflow. As an API response this is understandable, but for state evidence the result remains a plan, not an executed artifact.

The artifact bundle in A3's response is incomplete as committed execution evidence. It says the complete script is available on request and omits the full report template. Therefore it should not be counted as satisfying the computation obligation's required output fields.

The proposed new computation obligation may be useful, but the judge should avoid accepting new computation obligations unless they are backed by actual files or a complete script body.

## A4 Audit

### Useful Fragments

A4 is the strongest Round 4 Stage A contribution for the narrow M9 subproblem. It gives a focused, calibrated proof of the denominator-paired bound:

$$
T\ll D^2(\log 2H_D)^2\ll D^2X^\epsilon\ll X^{1+\epsilon},
$$

and then sharpens the decomposition to

$$
T_{t=0}\ll D^2,
\qquad
T_{t\ne0}\ll D(\log 2H_D)^2.
$$

The proof uses:

1. gcd splitting $a=ga'$, $b=gb'`, $(a',b')=1`;
2. the exact parametrization
   $h_1-h_2=t a'$, $h_3-h_4=-t b'`;
3. harmonic convolution
   $L_H(q)\ll1$ for $q=0$ and
   $L_H(q)\ll\log(2H)/|q|$ for $q\ne0`;
4. dyadic reciprocal sums
   $\sum_{a'\asymp D/g}1/a'\ll1`;
5. summation over $g\ll D`.

A4 also correctly states that the result does not prove `M9-M2`, the full diagonal core, or the final Gauss target.

### Caveats

A4 marks the status as `derived_under_assumptions`, which is correct. The proof depends on the H4/Vaaler coefficient magnitude bound for $\beta_h`.

The proof assumes bounded dyadic weights $|w_D|\le1`. This matches the current target statement but should remain explicit in the state entry.

The result is an absolute bound for one exact-resonance subfamily. It does not supply cancellation for near-collisions or for the main M2 sum.

## Recommended State Treatment

### Accept For Judge Consideration

Promote:

- `M9-M2-denominator-paired-weighted-bound`: `open` -> `derived_under_assumptions`.

Reason:

A1, A2, and especially A4 independently support the same gcd/harmonic-convolution proof. The correct proof statement should mention:

$$
T_{dp}(D;X)\ll D^2X^\epsilon\ll X^{1+\epsilon}
$$

for $X^{1/4}\le D\le X^{1/2}$, $H_D\asymp DX^{-1/4}$, bounded dyadic weights, and the H4-dependent coefficient bound $|\beta_h|\ll1_{2\nmid h}/|h|`.

### Keep Open

Do not promote:

- `M9-M2`
- `M9`
- `M9-M2-N0-diagonal-core-bound`
- `M9-near-collision-taxonomy`
- `M9-near-collision-estimate`
- `GC-target`

Reason:

The denominator-paired proof handles only one exact $N=0$ family. Unclassified exact resonances and near-collisions remain open. No uniform main-sum estimate is proved.

### Keep Source-Dependent

Do not promote `H4` to `proved_external_dependency` until the source card is updated and independently checked. A1's source audit should be used as evidence for `H4-source-audit`, not as a silent final dependency.

### Keep Diagnostic

A3's Round 4 material should remain `diagnostic_only` or `inconclusive` until actual files are committed and run.

## Review-Prompt Implications

Stage B should ask all four agents to review A4 explicitly.

Recommended emphasis:

- A1 should verify whether A4's proof is ready for a `derived_under_assumptions` state update and whether it belongs in `best_proof_draft.md`.
- A2 should check the harmonic-convolution bound, endpoint $H_D$ behavior, and whether its own semi-diagonal extension is overbroad.
- A3 should design a small exact enumeration to isolate $t=0$ and $t\ne0$ denominator-paired mass and confirm the predicted $D^2$ and $D\log^2H$ scaling.
- A4 should review A1/A2/A3 and defend or repair its denominator-paired proof under peer critique.

## Suggested Judge Summary

Round 4 Stage A likely produced a genuine narrow proof-graph improvement: the denominator-paired exact-resonance subcase is controlled conditionally on H4. The safest next state action is to add A4 evidence and promote only `M9-M2-denominator-paired-weighted-bound` to `derived_under_assumptions`, while keeping every broader M9 obligation open.
