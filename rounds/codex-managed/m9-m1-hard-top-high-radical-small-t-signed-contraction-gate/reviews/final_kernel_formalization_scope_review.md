# Round 183 final kernel formalization and scope review

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: independent final formalization/scope reviewer
- Generated: `2026-08-27T20:16:05.3821441+08:00`
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Evidence status: review evidence only; no shared proof-state edit

## 1. Result and verdict

**REPAIR, provenance-only; mathematical statement and owner scope are
GREEN.**  Every mathematical assertion in the conductor candidate and
durable kernel is contained in the three Round-183 GREEN seam results.
The sector is explicitly and consistently an incidence-level sector, its
exact complement contains the complete (t=1) face, capacity is never
converted into literal lower mass, fixed-row correlation remains an
unproved stronger sufficient condition, partial Mobius remains a scoped
self-return mechanism, and no parent, bridge, theorem, or exponent is
promoted.

The sole repair is formal provenance in the durable kernel.  Unlike the
conductor candidate, the durable kernel does not record its exact direct
graph dependencies or the candidate and GREEN reviews from which it was
formalized.  Protocol section 4 requires each artifact to record exact
context, dependencies, and claimant/reviewer status.  The kernel records
campaign, task, role, graph hash, and pending status, but omits the first two
required provenance lists.  No mathematical text needs alteration.

## 2. Exact statement and hypotheses reviewed

Both files consistently freeze real (X\geq2), one literal middle or
lower residual shell (L) of the unique hard-M1 profile, one sign
(\sigma\in\{+1,-1\}), the exact zero-extended coefficient
(C_{L,X}^{\sigma}), and (T_L=\lceil\sqrt L\rceil).  They expand the
coefficient into literal divisor incidences before any sector split.

The promoted positive statement is exactly the large-gcd nonresonant
incidence sum with

\[
 G=(h,n),\quad h=Gu,\quad n=Gv,\quad (u,v)=1,
\]

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{uv/s(u,v)},\qquad t=G\rho(u,v),
\]

\[
 G_0=\lceil L^{1/4}\rceil,\qquad
 \delta_X=(10\log(2X))^{-1},\qquad
 \Delta_X(u,v)=\operatorname{dist}
 \left(2\sqrt{Xuv},\mathbb Z+\tfrac12\right),
\]

and restrictions (G\geq G_0), (G\rho<T_L), and
(\Delta_X\geq\delta_X).  Its bound is

\[
 |\mathcal A^{\mathrm{ray,nr}}_{L,X,\sigma}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The exact incidence complement is

\[
 \{G<G_0\}\ \dot\cup\
 \{G\geq G_0:\Delta_X(u,v)<\delta_X\},
\]

inside every original literal predicate.  Equality in the resonance test
belongs to the proved sector.  Since (t=1) forces (G=\rho=1), the
complete (t=1) face lies in the first open component whenever nonempty.

The mechanism statement is also exact:

\[
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a),
\]

with both strict inequalities retained.  It equals
(\mathbf1_{u=1}) on (b>L,u<T); the full small-(t) sum and its
(a<T) core therefore self-return to the full literal product wave modulo
(O_\varepsilon(L^{3/2}X^\varepsilon)), while the (a\geq T) tail is
target-safe.  This is not a theorem that the literal owner fails.

## 3. Formalization-fidelity derivation

| Candidate/kernel assertion | Containing GREEN evidence | Fidelity decision |
|---|---|---|
| Incidence bijection (h=Gu,n=Gv), (s=\operatorname{sf}(uv)), (t=G\rho) | Coefficient/product/endpoint review, checks 1--2 | **GREEN.** Multiplicity, oddness, character, phase, and strict small-(t) cutoff are unchanged. |
| Uniform step-two BV of the zero-extended literal ray weight | Coefficient/product/endpoint review, checks 3--4 | **GREEN.** The candidate supplies the full lemma; the durable proof is a faithful compression. |
| Character-geometric partial sum and Abel estimate | Coefficient/product/endpoint review, check 5 | **GREEN.** The same half-integer distance and both signs occur. |
| Ray count and (G_0=L^{1/4}) restored power | Coefficient review, check 6; power review, section 3.5 | **GREEN.** The positive sum occurs only after actual character-phase cancellation. |
| Incidence envelope (O(L^{7/4})) | Discovery report and both mathematical seam reviews | **GREEN.** It is explicitly an upper capacity envelope, not literal mass. |
| Exact small-(G)/near-resonant complement and all (t=1) | All three seam reviews | **GREEN.** Both files repeatedly state that the complete owner remains open. |
| Two-cutoff Mobius kernel and (u=1) identity | Power/self-return review, sections 3.1--3.3; blind post-unmask review | **GREEN.** Both inequalities and the ceiling are retained. |
| Low-(b), large-(u), and large-(a) target-safe powers | Power/self-return review, equations (3.8), (3.9), and (3.13) | **GREEN.** Every correction is (O(L^{3/2}X^\varepsilon)) and the transformed large-(t) region is paid once. |
| Small-(a) self-return to the full product wave | Power/self-return review, equation (3.16) | **GREEN.** It refines only the existing mechanism obstruction. |
| Fixed-row Fejer connector | Power/self-return review, section 3.4; blind review | **GREEN as conditional text only.** The candidate marks the brace estimate unproved at (t=1); the durable kernel mentions it only in scope. |
| Separation from old PSC | Power/self-return review, section 4 | **GREEN.** No equivalence, necessity, or theorem transfer is claimed. |
| One-prime orientation observation | Coefficient/product/endpoint review, check 9 | **GREEN.** The candidate preserves the condition that a suitable (p\equiv3\pmod4) divides the fibre; the durable kernel does not promote it. |
| State and exponent scope | Blind post-unmask review, sections 6--7 | **GREEN.** No complete owner, hard cone, smooth M1, GAR, M9-M1, M2, endpoint, M9, bridge, target, or exponent is inferred. |

The durable kernel is a shorter projection of the conductor candidate, not
a mathematically enlarged version.  Its statement, proof, and scope agree
with the candidate on every overlapping formula.  Omitting the candidate's
full conditional correlation formula and local orientation discussion from
the durable kernel narrows that artifact and creates no inconsistency.

## 4. First doubtful or defective step

There is no doubtful mathematical step remaining inside the promoted
strict-sector theorem or scoped self-return after the three GREEN seam
reviews.  The first unproved analytic step toward the frozen owner remains
the exact incidence complement, especially the complete (t=1) cone.
The fixed-row brace estimate is also unproved already at (t=1), and both
files say so.

The first formalization defect is the durable kernel's missing dependency
and validation-provenance block.  A reader cannot determine from that file
alone that its BV lemma depends on `H4-Phi-regularity`,
`M9-M1-frequency-phase-diagram-R10`, and
`M9-M1-top-endpoint-transform`, or that its support/self-return uses
`M9-M1-hard-top-squarefree-radical-sector-reduction` and
`Divisor-bound-elementary`.  Nor does it name the conductor candidate and
three GREEN reviews that authorize the compression.  This is the first and
only repair required.

## 5. Required controls and scan outcome

| Control | Outcome |
|---|---|
| Incidence-level qualification | **PASS.** Both files explicitly deny a product-index sector interpretation. |
| Exact complement and mandatory (t=1) | **PASS/open.** All (t=1) remains in (G<G_0). |
| Capacity versus literal mass | **PASS.** (O(L^{7/4})) is only an arbitrary-coefficient incidence envelope. |
| Character-erased/adversarial false analogue | **PASS.** Actual (\chi_4(G))-phase cancellation is named; no coefficient-uniform theorem is asserted. |
| Partial Mobius mechanism scope | **PASS.** Self-return refines an obstruction and does not disprove the owner. |
| Fixed-row correlation scope | **PASS.** It is unproved, sufficient, rowwise stronger, and not PSC. |
| Downstream and exponent quarantine | **PASS.** Every named downstream node and all three exponent entries remain unchanged. |
| Candidate versus durable statement | **PASS.** No contradiction, widened range, weakened hypothesis, or stronger implication was found. |
| UTF-8/control-byte scan | **PASS.** Both files have zero forbidden control characters and zero replacement characters. |
| TeX delimiter/environment scan | **PASS.** Candidate: display delimiters 33/33, inline delimiters 83/83, environments 2/2, braces 216/216, brackets 34/34, parentheses 218/218. Kernel: display 11/11, inline 43/43, environments 1/1, braces 69/69, brackets 11/11, parentheses 97/97. |
| Whitespace/diff scan | **PASS.** `git diff --check` reports no error for either file. |
| Durable dependency provenance | **REPAIR.** Exact direct dependencies, source candidate, and GREEN validation reviews are absent. |

The candidate reviewed has SHA-256
`69662a1b8489d6a4daf326e39de88bb9c36e693cadc94fcb20020644adaeec59`;
the durable kernel reviewed has SHA-256
`214078f6c412f9ba3591da00d6920933be6e3c794d9a734be5b0f2b6b12d5c84`.

## 6. Dependencies and exact artifacts used

This review used exactly:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/candidates/formalized_hard_m1_small_t_primitive_ray_sector_and_self_return.md`;
3. `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`;
4. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/coefficient_product_endpoint_seam_review.md`;
5. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/power_self_return_psc_seam_review.md`;
6. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/blind_post_unmask_owner_scope_review.md`.

The mathematical seam review hashes were respectively
`30239761d7b1055e4d7a86efbee12c5a104e8aa2a3edd6462276b16d718e4af9`,
`9e562c8c60d7f336131fb5ec7e75e5af2b26dfcd2eaba376f73840cc00aa8405`,
and
`d81bb22fdf5ebd98134c485624b68c9a067c347d0d1c94c40dcbc3d2385b87f3`.
No graph state, synthesis, candidate, or durable kernel was edited.

## 7. Recommended state effect

Do not validate or apply the State Patch from the current durable-kernel
revision.  Repair only its provenance by adding an exact dependency and
validation block naming:

- direct graph dependencies:
  `M9-M1-hard-top-squarefree-radical-sector-reduction`,
  `M9-M1-top-endpoint-transform`,
  `M9-M1-frequency-phase-diagram-R10`, `H4-Phi-regularity`, and
  `Divisor-bound-elementary`;
- the exact conductor candidate path and its hash above; and
- the three GREEN review paths and hashes above.

Then rerun this bounded final formalization review against the repaired
kernel hash.  If those provenance fields are added without changing the
mathematics, the appropriate verdict is GREEN and the narrow state effect
remains: promote only one subordinate `proved_internal` incidence-sector
lemma, refine only the existing partial-Mobius/Mellin obstruction, retain
fixed-row correlation as inconclusive mechanism evidence, keep the exact
complement as the open next action, and change no parent, bridge, theorem,
or exponent.
