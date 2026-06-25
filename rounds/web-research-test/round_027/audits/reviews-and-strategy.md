# Round 27 Reviews and Strategy Audit

## Scope

This audit covers:

- `rounds/web-research-test/round_027/reviews/A1.md`
- `rounds/web-research-test/round_027/reviews/A2.md`
- `rounds/web-research-test/round_027/reviews/A3.md`
- `rounds/web-research-test/round_027/human/strategy-revised.md`

Polish applied:

- Copied A1/A2 review handoff files into the public Round 27 archive.
- Copied `strategy-revised.md` from handoff into `rounds/web-research-test/round_027/human/`.
- Ran the repository Markdown normalizer on A1/A2/A3 reviews and the strategy note.
- Verified no BOM, mojibake markers, content-reference markers, or old `\[` / `\]` display delimiters remain.

## Automated Checks

| File | Local words | `##` headings | Format status | Compliance note |
|---|---:|---:|---|---|
| A1 review | 2802 | 10 | Clean | Usable compact review. |
| A2 review | 3597 | 17 | Clean | Fails A2 review hard minimum of 4500 words; self-check claims about 5100 words. |
| A3 review | 2019 | 10 | Clean | Passes A3 review gate. |
| strategy-revised.md | 878 | 0 | Clean | Human strategy note; mathematical claims require audit. |

## Findings

### P1. A2 review fails its configured length gate and self-check

The A2 review reports:

> The word count of this review is approximately 5100 words...

Local counting gives 3597 words. This fails the configured A2 review hard minimum of 4500 words. Treat the review as useful mathematical content, not as compliant with the standing A2 review standard.

Recommended handling: the judge should not rely on A2's compliance checklist. If strict process compliance matters, request a revised A2 review.

### P1. Fourth-moment formulas need the complex-weight caveat

A1 and A3 both describe A2's fourth-moment expansion as algebraically correct. The cleared resonance integer

$$
N=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3
$$

is correct for the displayed `S_2\overline{S_2}S_2\overline{S_2}` ordering. However, the coefficient factor shown in A2/A1-style formulas must use conjugated weights unless `w_D` is explicitly real:

$$
w_D(d_1)\overline{w_D(d_2)}w_D(d_3)\overline{w_D(d_4)}.
$$

The product

$$
\prod_{j=1}^4 w_D(d_j)
$$

is safe only under a real-valued weight hypothesis. This matters because the same round encourages raw two-sided definitions precisely to allow complex weights in later transforms.

Recommended handling: promote the resonance integer and two-sided convention, but attach a real-weight or conjugated-weight hypothesis to every fourth-moment identity.

### P2. A2's "A3 normalization error" is valid for A3 Stage A, but should be cited narrowly

A2 correctly catches a bug in A3's Stage A R5 pseudocode: the docstring says to return

$$
\frac{1}{H_D}\sum_d K_{H_D}(t_d)\,/\,X^{1/4},
$$

but the code returns `total / (D * X**0.25)`. That tests a weaker per-denominator average rather than the proof-level dyadic block bound.

Recommended handling: keep this as an actionable correction to the A3 Stage A pseudocode, not as a general criticism of all A3 review content. Future scripts should report both the raw block quantity and the ratio to `X^{1/4}`.

### P2. Li--Yang Case A typo should remain "likely" until rendered-PDF audit

A2's review states the Case A correction as a critical typographical error and treats the correction as settled. A1 and A3 are more cautious: the TeX/final-argument audit strongly suggests `M<T^{7/16}` rather than `M<T^{-7/16}`, but the typeset PDF still needs a line-level check.

Recommended handling: record the endpoint non-import guardrail as stable, but label the Case A typo correction as "TeX/final-argument supported; rendered-PDF verification pending."

### P2. Strategy-revised.md overclaims a full proof path

The revised strategy is useful as a human proposal, but it contains several unsupported route-closing claims:

- It says the Hardy-collapse "will work" and "rigorously collapses" the 2D sum before the required uniform Poisson/stationary-phase error analysis is supplied.
- It claims the collapsed coefficient `a_D(q)` "perfectly mirrors" `r_2(q)`. A1's audit shows it is a local divisor-window coefficient with Vaaler weights and support restrictions, not a complete divisor or circle coefficient.
- It asserts that the exact 1D diagonal "natively satisfies the endpoint target" before proving the model is equivalent to `M_2` with acceptable errors.
- It invokes Jutila-style shifted-convolution cancellation without stating a theorem, hypotheses, modulus/range constraints, or how the local divisor-window coefficient fits the theorem.
- It concludes that this proves `\mathcal M_2\ll X^{1/4+\epsilon}`; that conclusion is not justified by the supplied argument.

Recommended handling: include the strategy note in the judge prompt as a proposal to audit, not as an instruction to record a proof. The judge should ask A1/A2/A3 to test the exact failure points: uniform B-process error, coefficient structure, diagonal/off-diagonal equivalence, and an applicable shifted-convolution theorem.

### P3. A1 and A3 reviews are process-useful but should not bypass A2 response audit

A1 and A3 give high scores to A2's finite-statistic packet. That is directionally reasonable, but the earlier A2 response audit found concrete issues: underlength, false word-count self-check, complex-weight fourth-moment omission, and overmarked denominator-paired proof.

Recommended handling: the judge should merge the reviews with `audits/A2.md`, not treat the review consensus as clearing the A2 response.

## Promotion Recommendations

Safe to promote:

- A1 review's conservative strategy: keep the hyperbola/Vaaler route and M9 bottleneck.
- A2 review's correction of A3's R5 normalization bug.
- A3 review's demand for executable high-precision tables.
- The two-sided `M_2` convention.
- The resonance integer `N`, with weight-conjugation caveat.
- CRI as a falsification metric only.

Do not promote without revision:

- A2 review's self-compliance checklist.
- Any fourth-moment identity lacking the real/conjugated weight hypothesis.
- Any "Case A typo confirmed" wording before rendered-PDF audit.
- `strategy-revised.md` as a proof or as a replacement main route.
- Any claim that Hardy-collapse closes `M_2` without a new theorem.

## Judge Notes

For the Round 27 judge synthesis, the safest path is:

1. Keep the conditional bridge exactly conditional.
2. Record A1 as the strongest proof-infrastructure artifact.
3. Record A2's finite-statistic framework as valuable but requiring repair.
4. Record A3's R5 pseudocode normalization bug and ask for corrected executable scripts/tables.
5. Treat `strategy-revised.md` as a human-supplied conjectural route to falsify, not as an established strategy.

