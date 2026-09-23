# Conductor extraction of the inherited hard-M1 shell range

- Campaign: m9-m1-t1-high-h-imprimitive-lift-gcd-gate
- Round: 188
- Starting graph SHA-256:
  be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff
- Status: extracted accepted support connector pending independent review

## Exact accepted inputs

The authoritative proved-internal node
M9-M1-top-endpoint-transform fixes

\[
 y=\lfloor\sqrt X\rfloor,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\tag{188.S1}
\]

and its statement is uniform only over the literal Vaaler frequencies

\[
 1\le h\le H.
\tag{188.S2}
\]

The accepted Round-184 hard-M1 kernel defines the literal dyadic
frequency symbol with factor

\[
 \eta_L(u)\Phi\!\left(\frac{u}{H+1}\right)
\tag{188.S3}
\]

and zero extension off every original frequency and height predicate.
On a nonempty \(L\)-shell its frequency coordinate satisfies
\(u\asymp L\) and (188.S2). Thus, with only fixed dyadic support
constants,

\[
 L\ll H+1.
\tag{188.S4}
\]

For \(X\ge2\),

\[
 H\le yX^{-1/4}\le X^{1/4},
\tag{188.S5}
\]

and \(1\ll X^{1/4}\). Combining (188.S4)--(188.S5) gives

\[
 \boxed{L\ll X^{1/4}}
\tag{188.S6}
\]

on every nonzero literal hard-M1 shell. Off the original frequency
range, the zero extension makes the relevant coefficient and hence the
Round-188 aggregate empty.

## Provenance

The support extraction uses:

1. the authoritative M9-M1-top-endpoint-transform node in
   state/proof_obligations.yml at starting graph hash
   be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff;
2. proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md,
   SHA-256
   3387615b5522deeb4c63021fbdf4a665afa2c405052f2ff0868bed40338e602f;
3. the already accepted Round-187 power-scope review
   rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/power_literal_scope_self_return_seam_review.md,
   SHA-256
   470737a35629b58ae82753f67ce12f26c449619a6e8a6bdc4ea17d2642562d7d;
4. the already accepted Round-187 final power/owner review
   rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/final_kernel_power_owner_scope_review.md,
   SHA-256
   06b78ac063a5c2f0886b0ca5315f6e931143c48cf5a8428878e422823f8bb301.

The latter two reviews explicitly record (188.S6) and the zero-extension
alternative. The first two items provide the direct accepted derivation.

## Scope

This connector supplies only the polynomial relation needed to rebudget
fixed logarithmic powers in a literal hard-M1 shell. It supplies no
factor \(Y\), no signed cancellation, no estimate for the Round-188
primitive complement, and no change to any owner, theorem, bridge, or
exponent.
