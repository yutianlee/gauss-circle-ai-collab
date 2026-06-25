# A2 Secondary Round 2 Polish And Audit

Source: `handoff/obligation-main/round_002/responses/A2-secondary.md`

Archived copy: `rounds/obligation-main/round_002/responses/A2-secondary-002.md`

## Polished Digest

A2-secondary gives a broad analytic referee response for the active `M9-M2-fourth-moment-expansion` and `M9-near-collision-taxonomy` obligations. The useful core is the corrected two-sided convention, the cleared fourth-moment numerator, a more explicit exact-resonance taxonomy, and a warning that continuous absolute-value majorization is too crude near the endpoint. The response should be used as a route-selection and obstruction artifact, not as a proof of an endpoint estimate.

Main usable content:

1. Under the current H4-dependent convention

$$
\beta_{h,H_D}
=
-\frac{\Phi(|h|/(H_D+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

the coefficient is real and even:

$$
\beta_{-h,H_D}=\beta_{h,H_D}.
$$

This supports the raw two-sided convention and the paired-cosine implementation when the dyadic weights are real.

2. The fourth-moment phase is correctly centered on

$$
\frac X4
\left(
\frac{h_1}{d_1}
-
\frac{h_2}{d_2}
+
\frac{h_3}{d_3}
-
\frac{h_4}{d_4}
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

3. The exact diagonal and pair-swapped classes are safe named families. With the actual reciprocal `h` weights, each has mass `O(D^2)`, hence is compatible with the target when `D <= X^(1/2)`.

4. The semi-diagonal, mixed, truncation-edge, sign-symmetric, and unclassified classes are useful bins, but their bounds are not yet complete. They should remain taxonomy objects for A3 enumeration and A1 synthesis.

5. The Montgomery-Vaughan spacing discussion is a useful diagnostic warning: a continuous mean-value or large-sieve relaxation sees a spacing penalty of size about `D^4` in the fourth-moment rational phase. At `D ~ X^(1/2)` this becomes about `X^2`, so any proof route that replaces arithmetic counting by a smooth continuous metric needs a separate justification.

6. The Type-II bilinear Farey-spacing route is worth preserving as the main alternative route. Its first useful test is the shifted reciprocal phase

$$
\sum_{d\sim D}
e\left(
\frac{Xh}{4}
\left(
\frac1d-\frac1{d+\ell}
\right)
\right).
$$

## Audit

### Strengths

- The two-sided `beta_h` parity calculation is correct under the current H4 convention.
- The corrected numerator `N` matches A1 and A3's algebraic conventions.
- The response directly addresses the strengthened route-proposal requirement.
- The exact diagonal and pair-swapped capacity checks are useful and should be retained.
- The prime-denominator collapse argument is a useful bounded subcase for the unclassified bin.
- The continuous-spacing warning is a helpful guardrail against absolute-value smoothing.
- The proposed A3 tests are concrete enough to become executable diagnostics.

### Caveats

1. The response overuses `[PROVED]`.

Only the algebraic identities and the simplest named-family checks should be treated as internally proved. The global taxonomy, near-collision obstruction, and new aliasing claim are not proved at graph level.

2. The reality of `S_2(D;X)` assumes real spatial weights.

If `w_D(d)` is complex, the paired-cosine formula and the statement that `S_2` is real need modification. Keep the raw two-sided formula as canonical.

3. The denominator-paired sign claim is unsafe.

A2 claims the product of `chi_4(|h_i|)` is uniformly `+1` on the denominator-paired surface. This is not reliable in the full two-sided frequency domain. Negative `h` can break the simple mod-4 parity argument, and A2-2's own numerical discussion reports negative denominator-paired sums. Do not promote this claim.

4. The near-collision constructive-obstruction paragraph is too strong.

The fact that `N=1` gives a very small phase at `D ~ X^(1/2)` shows that oscillation may be weak in some bands. It does not by itself prove that the weighted tuple count exceeds the endpoint target.

5. The Montgomery-Vaughan spacing analysis is diagnostic, not a theorem-level obstruction.

The `delta^{-1} ~ D^4` penalty explains why a smooth continuous relaxation is dangerous. It does not rule out arithmetic counting, signed cancellation, bilinear estimates, or a refined large-sieve setup.

6. The proposed state patch is not validator-ready.

It uses a list format and proposes a new `M9-discrete-aliasing-transition` obligation without the required graph patch schema. If the judge keeps this, it should be rewritten as a diagnostic obstruction with conservative status.

## Recommended Use In The Round

### For A1

Use A2's `N` and exact-family bins as taxonomy scaffolding. Reject the denominator-paired `+1` sign claim unless A2 supplies a proof that covers negative frequencies.

### For A3

Prioritize:

- exact enumeration of `N=0` bins with signed `h`;
- a counterexample check for the denominator-paired sign claim;
- weighted mass estimates for exact diagonal, pair-swapped, and sign-symmetric bins;
- small-band `0<|N|<=T` tables with signed and absolute masses;
- one shifted-reciprocal bilinear diagnostic for the proposed Type-II route.

### For The Judge

Likely graph treatment:

- `M9-M2-beta-algebra`: no change; already `derived_under_assumptions`.
- `M9-M2-fourth-moment-expansion`: keep as algebraically useful; do not promote beyond `derived_under_assumptions`.
- `M9-near-collision-taxonomy`: update notes with A2's bins and caveats; keep open or `derived_under_assumptions`, not proved.
- New aliasing/continuous-spacing note: if added, mark as `diagnostic_only` or `proposed`, not `proved_internal`.

## Bottom Line

A2-secondary is useful but too assertive. It strengthens the taxonomy agenda and gives a plausible alternative Type-II route, but it does not close `M9-M2`, does not prove the near-collision estimate, and contains a likely false denominator-paired sign assertion.
