# A1 Round 3 Polish And Audit

Source: `handoff/obligation-main/round_003/responses/A1.md`

Archived copy: `rounds/obligation-main/round_003/responses/A1-003.md`

## Polish Notes

- Normalized the copied Markdown and archived the response.
- Repaired a corrupted indicator in the proposed state-patch reason: `1_{2 notmid h}` now replaces the mojibake fragment.
- Repaired two stale evidence paths from `A1.md` to `A1-003.md`.

## Polished Digest

A1 gives a calibrated proof-draft contribution for the Round 3 M2 obligations. The response should be used as proof infrastructure, not as an endpoint estimate.

Main usable content:

1. A1 keeps the H4-dependent coefficient convention explicit:

```text
C_h = e(h/4) - e(3h/4) = 2i chi_4(h) 1_{2 notmid h}
```

and

```text
beta_{h,H} = alpha_{h,H} C_h
            = - Phi(|h|/(H+1)) chi_4(|h|) 1_{2 notmid h} / (pi |h|).
```

Thus `beta_{-h,H}=beta_{h,H}` is real and even, conditional on the unresolved H4 source audit.

2. A1 records the raw two-sided M2 formula as the canonical formula and scopes the paired-real formula to real dyadic weights.

3. A1 records the corrected fourth-moment phase and cleared numerator

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4 + h3 d1 d2 d4 - h4 d1 d2 d3.
```

4. A1 proves only a narrow pair-equality exact-resonance core and explicitly keeps the full `M9-M2-N0-diagonal-core-bound` obligation open.

5. A1 gives useful route proposals: fourth-moment exact/near-collision taxonomy, CRI/residue interference, and direct signed bilinear estimates. These are framed as routes with falsification tests rather than as completed proofs.

## Audit

### Strengths

- The character-factor and beta-algebra normalization is consistent with the Round 2 judge synthesis.
- The H4 dependency is not hidden.
- The raw two-sided formula remains canonical; paired formulas are not overused outside the real-weight hypothesis.
- The fourth-moment numerator matches the current graph convention.
- The pair-equality core is correctly separated from the full diagonal-core obligation.
- The proposed state patch mostly follows the conservative graph policy: keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open.

### Caveats

1. `M9-M2-beta-algebra` remains `derived_under_assumptions`, not proved independent of H4.

2. The H4 source-card work is still incomplete. A1 cites source locations, but this is not a rendered-page theorem audit.

3. The narrow pair-equality core does not prove `M9-M2-N0-diagonal-core-bound`. The full obligation still needs explicit family definitions, overlap handling, actual beta weights, and bounded dyadic weights.

4. The proposed state patch is useful prose but not validator-ready as-is. It uses a custom `proposed_updates` layout rather than the exact structured patch schema expected from the judge.

5. The direct signed bilinear route is still a route proposal. It needs a stated theorem with parameter ranges and a proof or a falsifying computation.

## Recommended Use

For Stage B reviewers:

- Accept A1's formulas as the working convention under H4.
- Use A1's open statement of `M9-M2-N0-diagonal-core-bound` as the standard against which A2 should be judged.
- Do not promote any endpoint estimate from A1.
- Preserve A1's warnings about real weights and unresolved H4 normalization.

## Bottom Line

A1 is the strongest calibrated Stage A response. It supplies clean algebra and a useful proof-draft target while resisting overpromotion.
