# A2 Round 3 Polish And Audit

Source: `handoff/obligation-main/round_003/responses/A2.md`

Archived copy: `rounds/obligation-main/round_003/responses/A2-003.md`

## Polish Notes

- Normalized the copied Markdown and archived the response.
- No mojibake or citation-marker cleanup was needed.

## Polished Digest

A2 contributes useful obstruction-finding and route-generation ideas, but it again overpromotes several claims. The response should be used as a source of candidate lemmas and stress tests, not as proof-graph closure.

Main useful content:

1. A2 uses the current two-sided convention, the real even beta coefficient, and the corrected numerator `N`.

2. A2 corrects the whole diagonal-core constant away from the earlier erroneous `1/16 D^2` claim and argues that the direct, pair-swapped, and sign-symmetric core has total scale about `3/16 D^2`, subject to overlap conventions and H4 coefficient bounds.

3. A2 attempts a denominator-paired estimate of size `O(D log^4 X)`. This is a useful target, but the proof remains incomplete at graph level.

4. A2 proposes bounding the entire exact `N=0` mass through an additive-energy estimate for fractions `h/d`.

5. A2 identifies a Gallagher/derivative penalty as a warning against extracting pointwise endpoint bounds from a continuous fourth-moment integral too naively.

6. A2 proposes a direct signed bilinear/exponent-pair route as an alternative to the fourth-moment route.

## Audit

### Strengths

- The response engages the exact Round 3 bottleneck: `N=0` taxonomy and the diagonal-core bound.
- The correction to the diagonal-core union constant is directionally useful.
- The denominator-paired subproblem is now stated in a form that can be attacked.
- The Gallagher derivative discussion is a useful warning against a continuous relaxation.
- The direct bilinear route is worth testing as a backup route.

### Caveats

1. The claimed total exact `N=0` bound `O(D^2)` is not proved in the response.

A2 invokes an unproved additive-energy estimate:

```text
# {h1/d1 + h3/d3 = h2/d2 + h4/d4}
  = O((H1 H2 H3 H4)^(1/2) D^2)
```

No exact theorem statement, hypotheses, source, boundary cases, or proof is supplied. This cannot close the unclassified residue.

2. The denominator-paired `O(D log^4 X)` estimate remains provisional.

The gcd/multiples counting step is plausible, but the response does not provide the full weighted summation proof with singular cases such as zero differences, overlaps with pair-equality families, and sign conventions.

3. The numerical verification is not repository evidence by itself.

A2 reports toy numbers but supplies no script, command, table, precision log, or committed output. Treat those numbers as anecdotal until A3/Codex materializes an executable diagnostic.

4. The Gallagher derivative penalty is diagnostic, not a route-closing theorem.

It warns that a continuous `L^4` to `L^\infty` extraction is lossy. It does not rule out discrete spacing, signed cancellation, exact arithmetic taxonomy, or a refined bilinear argument.

5. The direct signed bilinear route is underproved.

The small-D exponent-pair substitution, the Poisson transition, the endpoint `V=1` claim, and the phrase that higher exponent pairs cover the remaining interval all require exact estimates with beta weights, dyadic weights, stationary phase errors, and endpoint uniformity.

6. The proposed state patch is too aggressive.

Do not promote `M9-M2-N0-diagonal-core-bound` to `proved_internal`; do not mark `M9-near-collision-taxonomy` resolved; and do not add an implication from a proposed direct exponential-sum lemma to `M9-M2` without a complete theorem.

## Recommended Use

For Stage B reviewers:

- Extract A2's additive-energy bound as a precise theorem request.
- Ask A2 to prove or downgrade the denominator-paired estimate with all singular cases.
- Treat the direct bilinear route as `proposed`.
- Reject the proposed promotions for `M9-M2-N0-diagonal-core-bound` and `M9-near-collision-taxonomy` unless a reviewer supplies the missing proof.

## Bottom Line

A2 has better mathematical aim than in earlier rounds, but the calibration problem persists. The ideas are worth pursuing; the stated proof status is not.
