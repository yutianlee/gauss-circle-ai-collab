# Round 183 final-kernel post-repair verification

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: bounded independent post-repair reviewer
- Generated: `2026-08-27T20:24:41.2037703+08:00`
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Candidate SHA-256:
  `e23d4135401c81c263026fddf19df4d46536eaabaa33fa9a7a0d8b287ea82f91`
- Durable-kernel SHA-256:
  `f8898d48d1d8db3fcb767399b9825568d27a0fd32bb45b1b3de02a51154692d1`

## 1. Result and verdict

**GREEN.**  Both requested repairs are complete.  The durable kernel now
has exact dependency and validation provenance, and the candidate and
kernel now state the zero-extended frequency-profile/Fejer variation seam
exactly.  The frozen hashes match those supplied for review.  No new
mathematical, provenance, owner-scope, exponent-scope, byte, or TeX defect
was found.

## 2. Exact repair verification

The provenance repair is complete:

- all five named graph dependencies exist and are `proved_internal`;
- the durable kernel names the exact conductor candidate and its current
  hash;
- it names all three GREEN seam reviews and their current hashes; and
- it records claimant/reviewer status and keeps State Patch validation
  pending.

The BV exactness repair is also complete.  Both artifacts now define

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]

and isolate the accepted dyadic profile in the zero-extended product

\[
 \Psi_{H,L}(m)=\mathbf1_{1\le m\le H}\eta_L(m)
 \Phi\!\left(\frac{m}{H+1}\right).
\]

The interior (\Phi)-variation is summed only when both samples lie in
([1,H]); normalized BV of (\eta_L), the discrete product rule, and the
two zero-extension boundary jumps then give the full step-two variation.
The remaining literal masks and endpoint fields are retained separately.
The durable proof is a faithful compression of candidate equations
(183.C9a), (183.C11), and (183.C11a).

## 3. Candidate/kernel consistency

The two artifacts agree on every promoted mathematical interface:

1. the split occurs only after expansion into literal divisor incidences;
2. (h=Gu,n=Gv), (s=\operatorname{sf}(uv)), and
   (t=G\rho(u,v)) preserve multiplicity, character, phase, and cutoffs;
3. the proved piece is the actual-coefficient incidence sector
   (G\ge\lceil L^{1/4}\rceil),
   (\Delta_X(u,v)\ge(10\log(2X))^{-1}), bounded by
   (O_\varepsilon(L^{3/2}X^\varepsilon));
4. its exact incidence complement is the disjoint small-(G) and
   near-resonant union and contains all (t=1);
5. the (O(L^{7/4})) quantity is only a coefficient-insensitive incidence
   envelope, never literal lower mass;
6. the two-cutoff Mobius kernel, target-safe large-divisor tail, and
   small-core self-return are mechanism-scoped; and
7. fixed-row correlation remains an unproved stronger sufficient route,
   distinct from PSC.

The kernel omits the candidate's detailed conditional correlation formula
and local orientation discussion; that is a narrowing, not an
inconsistency.  Neither file promotes the complete small-(t) owner or any
downstream claim.

## 4. First doubtful or unproved step

No formalization defect remains.  The first mathematical step still
unproved is the exact small-(G)/near-resonant incidence complement,
especially the complete (t=1) face.  The fixed-row Fejer brace is also
unproved already for (t=1).  Both artifacts state these limitations
explicitly, so neither is a repair blocker for the narrow strict-sector
lemma or scoped self-return.

## 5. Control and hygiene outcomes

| Control | Outcome |
|---|---|
| Frozen hashes | **PASS.** Candidate and kernel hashes equal the supplied values. |
| Dependency existence/status | **PASS.** All five exact dependencies exist and are `proved_internal`. |
| Candidate provenance | **PASS.** Recorded path and hash match the current file. |
| Three GREEN reviews | **PASS.** All recorded paths and hashes match. |
| Incidence-level scope | **PASS.** Neither artifact restates the theorem as a product-index sector. |
| Exact complement / all (t=1) | **PASS/open.** Retained wholly outside the proved sector. |
| Capacity quarantine | **PASS.** No adversarial capacity is treated as literal mass. |
| Correlation and Mobius scope | **PASS.** Conditional mechanism and scoped self-return only. |
| Downstream/exponent quarantine | **PASS.** No hard parent, smooth M1, GAR, M9-M1, M2, endpoint, M9, bridge, target, or exponent follows. |
| UTF-8/control bytes | **PASS.** Both files are strict UTF-8 with zero forbidden controls and zero replacement characters. |
| TeX balance | **PASS.** Candidate: display 36/36, inline 87/87, environments 2/2, braces 228/228, brackets 39/39, parentheses 230/230. Kernel: display 14/14, inline 46/46, environments 1/1, braces 78/78, brackets 15/15, parentheses 111/111. |
| Whitespace | **PASS.** `git diff --check` reports no error for either artifact. |

## 6. Dependencies and exact artifacts used

This bounded verification used:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/candidates/formalized_hard_m1_small_t_primitive_ray_sector_and_self_return.md`;
3. `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`;
4. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/final_kernel_formalization_scope_review.md`;
5. the three GREEN Round-183 mathematical seam reviews named in the
   durable kernel; and
6. `state/proof_obligations.yml` only to verify the five dependency IDs and
   their statuses.

No reviewed artifact or shared state was edited.

## 7. Recommended state effect

The final formalization gate is GREEN at the two frozen hashes.  A State
Patch may promote only the subordinate `proved_internal` incidence-sector
lemma and refine only the existing partial-Mobius/Mellin obstruction.  It
must retain the complete small-(t) owner and its exact complement as open,
keep fixed-row correlation as inconclusive mechanism evidence, and change
no hard parent, smooth M1 parent, GAR, M9-M1, M2 obligation, endpoint
uniformity, M9, bridge, Gauss-circle theorem, or exponent.
