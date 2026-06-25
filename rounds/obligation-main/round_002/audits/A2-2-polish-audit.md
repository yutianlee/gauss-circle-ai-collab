# A2 Official Round 2 Polish And Audit

Source: `handoff/obligation-main/round_002/responses/A2-2.md`

Official handoff copy: `handoff/obligation-main/round_002/responses/A2.md`

Official archived copy: `rounds/obligation-main/round_002/responses/A2-002.md`

## Polished Digest

A2 official is the cleaner of the two A2 responses. It focuses on the exact `N=0` core, diagonal capacity, dual-length obstruction, CRI statistic, and a direct signed bilinear alternative. Its strongest contribution is the observation that the obvious diagonal families are compatible with the fourth-moment target; its weakest point is that it promotes diagnostic and numerical claims as proved without attaching reproducible code or controlling the unclassified/off-diagonal mass.

Main usable content:

1. The two-sided M2 formula is taken as

$$
\mathcal M_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\sim D}
w_D(d)e\left(\frac{hX}{4d}\right),
$$

with real-even coefficient

$$
\beta_h
=
-\frac{\Phi(|h|/(H_D+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

2. The alternating fourth-moment numerator is the same corrected numerator used by A1 and A3:

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

3. A2-2 correctly separates the easiest exact-resonance core:

- exact diagonal;
- pair-swapped;
- sign-symmetric.

For each of these named families, the product of coefficients is a square-like positive product. Their total weighted capacity is `O(D^2)`, hence compatible with the desired fourth-moment scale `X^(1+epsilon)` when `D <= X^(1/2)`.

4. The diagonal-capacity constant should be polished:

$$
\sum_{1\le |h|,\;2\nmid h}\frac1{\pi^2h^2}=\frac14.
$$

Thus one diagonal-type family is bounded by about `D^2/16`; the union of three core families is bounded by about `3D^2/16` before overlap corrections. The important conclusion is `O(D^2)`, not the exact displayed `1/16` constant for the whole core.

5. The dual-length observation is useful:

$$
K\asymp \frac{H_DX}{D^2}
\asymp \frac{X^{3/4}}{D}.
$$

Therefore `K > D` when `D < X^(3/8)`. This is a real obstruction to naive Poisson/stationary-phase smoothing in the lower and middle dyadic ranges. The response sometimes says `D << X^(1/3)`; that is a sufficient subrange, not the actual crossover.

6. The CRI statistic

$$
C(N,M)=
\sum_{\substack{h_i,d_i\\\operatorname{num}=N,\;\operatorname{den}=M}}
\prod_i \beta_{h_i}w_D(d_i)
$$

is a useful bookkeeping object for off-diagonal tests. It is not yet an estimate.

## Audit

### Strengths

- Cleaner than A2.md and closer to the strengthened prompt.
- Keeps the raw two-sided convention rather than relying only on a one-sided paired formula.
- Correctly identifies that the obvious `N=0` diagonal core does not by itself kill the fourth-moment route.
- Gives a concrete correction to vague Gallagher-style language through the dual-length `K` calculation.
- Proposes a useful CRI coefficient ledger for off-diagonal mass.
- Offers a plausible direct signed bilinear alternative that retains the `chi_4` twist.

### Caveats

1. The statement "the taxonomy consists of six mutually exclusive classes" is formal rather than substantive.

It becomes true only because the last class is "unclassified" and earlier classes are defined with exclusions. It does not prove that the unclassified class is small.

2. The diagonal constant is misstated for the full core.

`D^2/16` bounds one square-type family. The union of exact diagonal, pair-swapped, and sign-symmetric families is `O(D^2)` and can be bounded by `3D^2/16` before overlap corrections. This does not affect endpoint compatibility.

3. The denominator-paired claim is not proved.

A2-2 reports numerical negativity and `O(D log H_D)` behavior, but no script or proof is attached. Treat this as a computational hypothesis for A3, not a proved lemma.

4. The dual-length threshold needs correction.

From `K ~ X^(3/4)/D`, the natural crossover is `D ~ X^(3/8)`, not `X^(1/3)`. The `D << X^(1/3)` statement is only a narrower sufficient range.

5. "Code-first verification" is not auditable yet.

The response quotes counts and weighted sums, but the repository has no script, seed, table, or exact convention file for these tests. A3 should reproduce before the judge credits them.

6. The proposed state patch is not validator-ready.

It uses a list of updates rather than the required `proof_obligations.update/no_change/reject` structure. It should not be pasted directly into the judge patch.

## Recommended Use In The Round

### For A1

Use A2-2 as the better A2 route artifact. The key synthesis sentence should be: "The named diagonal `N=0` families are compatible with the target; the proof bottleneck is the unclassified exact resonance and the near-collision/off-diagonal bands."

### For A3

Reproduce A2-2's numerical claims in committed code before any promotion:

- exact `N=0` family counts for small `H,D`;
- signed and absolute mass by family;
- denominator-paired mass scaling;
- `K/D` dual-length table for dyadic `D`;
- CRI coefficient table for small `N,M` bins.

### For The Judge

Likely graph treatment:

- Accept diagonal-core compatibility as a bounded diagnostic or supporting note under `M9-near-collision-taxonomy`.
- Keep `M9-M2-fourth-moment-expansion` at `derived_under_assumptions`.
- Do not promote denominator-paired negligibility, global taxonomy, CRI, or the signed bilinear route beyond `proposed`/`diagnostic_only`.
- Preserve the direct signed bilinear route as a real next-round alternative.

## Bottom Line

A2 official should score higher than the secondary A2 response for focus and usefulness. It gives a good route clarification: diagonal `N=0` is probably not the obstruction; unclassified exact resonances and near-collision bands are. It still needs A3 reproduction and a formal proof of the denominator-paired and off-diagonal estimates.
