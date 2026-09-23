# Round 187 final kernel formalization, provenance, and hygiene review

## 1. Result / verdict

**REPAIR REQUIRED before the current durable-kernel file is promoted.**
The mathematical reduction and its nonpromotion scope are GREEN, but the
frozen kernel at SHA-256

b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74

has concrete TeX and provenance defects. They are presentation/provenance
repairs only: no formula, estimate, hypothesis, dependency, or owner
status needs to change.

The kernel does not exceed the current candidate. Its exact
decomposition, packet estimates, open complement, conductor identities,
and self-return controls match candidate SHA-256

c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89.

## 2. Exact reviewed claim and evidence boundary

Under the inherited carrier (K185.27) and amplitudes
(K185.30)--(K185.35), kernel (K187.8)--(K187.11) asserts exactly

\[
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma+
          \mathscr P_{Y,\le Q}^\sigma+
          \mathscr L_{Y,Q}^{>,\sigma}+
          \mathscr R_{Y,Q}^\sigma\},
\]

\[
 |\mathscr U_{1,Y}^\sigma|
 +|\mathscr P_{Y,\le Q}^\sigma|
 +|\mathscr L_{Y,Q}^{>,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon,
\qquad
 |\mathscr R_{Y,Q}^\sigma|
 \ll_\varepsilon YL^2X^\varepsilon,
\]

while

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon
\tag{K187.11}
\]

is explicitly open. Kernel (K187.12)--(K187.22) matches candidate
(187.K9)--(187.K19), and kernel (K187.23)--(K187.27) matches
candidate (187.K20)--(187.K25).

The evidence boundary is also mathematically correct. The blind report
independently supports the carrier, normalization, \(U=1\) payment,
direct small-modulus/ordinary-edge packet, exact wider complement, and
capacity obstruction. It does not derive the stronger complete
\(q_U(k)\le Q\) packet. That strengthening is supplied by the discovery
and hostile derivations and independently checked by the seam reviews.
No claim in the kernel requires more than that evidence.

## 3. Formalization and reference checks

The following checks pass at the frozen hash:

- strict UTF-8 decoding, no BOM, no NUL or other control character, LF
  line endings, and one terminal line feed;
- 35 display-math openings and 35 closings;
- two aligned environments with matching ends;
- exactly one copy of each tag (K187.1)--(K187.27), with no gap,
  duplicate, or undefined internal K187 reference;
- the external references (K185.27) and
  (K185.30)--(K185.35) exist in the accepted parent kernel;
- every reviewed-evidence path currently listed by the kernel exists;
- the three mode sets are disjoint and exhaustive, \(U=1\) is separate,
  both orientations remain present, and the unique real part stays
  outside the complete open aggregate.

The following exact formalization repairs are required.

1. **Inline TeX delimiters.** The file contains zero valid inline
   \( \backslash( \), \( \backslash) \) delimiter pairs, although it
   contains raw TeX commands in prose. At the frozen line numbers, wrap
   every mathematical span on lines

   1, 5--6, 13, 36, 38, 52--53, 61--62, 82--84, 142, 164, 171,
   187, 194, 218--221, 228--231, 233, 242--244, 260--261,
   268--270, 273--274, 289, 293, 309, 318, 327--328, 343, 345,
   357, 360, and 362

   in valid inline delimiters. Leave plain equation references such as
   (K187.9) as prose references.

2. **Missing TeX command slashes.** In the same repair, restore these
   exact tokens:

   - line 6: sigma to \(\sigma\);
   - lines 61 and 82--84: mathscr to \(\mathscr\);
   - line 171: mathbb to \(\mathbb\);
   - line 318: sum to \(\sum\);
   - line 328: mathcal to \(\mathcal\).

   For example, line 61 should begin
   “Let \(\mathscr U_{1,Y}^{\sigma}\) ...”, not
   “Let (mathscr U...)”.

3. **Explicit symbol definitions.** For durable self-contained
   formalization, add the standard definitions

   \[
   e(x)=e^{2\pi i x},\qquad
   [x]_U\in\{0,\ldots,U-1\},\qquad
   \bar vv\equiv1\pmod U,
   \]

   state
   \(\mathbb U(q)=(\mathbb Z/q\mathbb Z)^\times\) for \(q>1\),
   and identify \(\mu\) and \(\tau\) as the Möbius and divisor
   functions. Also replace the verbal definition of the \(U=1\) piece
   by the exact candidate formula

   \[
   \mathscr U_{1,Y}^{\sigma}
   :=\sum_{\omega\in\{+,-\}}
     \sum_{\substack{\mathfrak f:\,Y<h\le2Y\\U=1}}
     A_{\mathfrak f,\omega}^{\sigma}.
   \]

These repairs only make already inherited or standard notation explicit.

## 4. Provenance and computation checks

The mathematical provenance is sound but should be made explicit in the
kernel itself. Add a provenance header containing:

- campaign m9-m1-t1-high-h-inverse-residue-fourier-gate, Round 187;
- starting graph SHA-256
  d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a;
- exact source candidate path and SHA-256
  c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89;
- reconciliation path and SHA-256
  b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705;
- evidence status “durable proof-kernel candidate; pending repaired-hash
  replay and State Patch validation”; and
- numerical theorem evidence “none”.

Add the exact diagnostic provenance to Reviewed evidence:

- controls/conductor_round187_wolfram_inverse_residue_check.md,
  SHA-256
  032d8039636b0e4e2040caed7c0d2ade570761812aed85711930ba37300b176a;
- controls/inverse_residue_exact_check.wls, SHA-256
  e818367a710c4051f9259966133ca48b9496dfc3d5b8b18d559072cfac4a7d83.

The control used bounded WolframScript calculations for finite
normalization, inversion, orientation, and alias-fold identities. Its
record explicitly says diagnostic only, and the kernel likewise uses no
computation as asymptotic theorem evidence.

Add one blind-attribution sentence to Reviewed evidence: the blind
report proves the direct small-modulus/edge packet but not the complete
small exact-conductor grouping; the latter rests on the discovery and
hostile derivations plus independent seam review. This prevents the
collective evidence list from being read as attributing the stronger
packet to the blind report.

No external theorem or web result is imported. “Unit Ramanujan sum” in
(K187.24) is the elementary internally derived identity already proved
in the candidate and hostile report.

During this audit, the uncited collateral review
reviews/final_kernel_candidate_consistency_review.md was found to
contain one U+0008 byte and several missing TeX backslashes. The
conductor mechanically repaired only that review. Its current SHA-256 is
3bf3aed9ce946bd70d518fb62a43b871a58f28a5dfcdf8c8fbdb3f9fc50af090,
it now has zero control characters, and the repair is non-mathematical.
The kernel remained byte-identical at the frozen b911...27c74 hash.

## 5. First doubtful or unproved step

There is no new doubtful mathematical step in the durable reduction.
The first unproved step remains exactly (K187.11), requiring the full
factor \(Y\) from a jointly signed property of the actual literal
amplitude in \((h,v,t,k)\) before positive recombination.

The defects found here do not supply or remove any mathematical
hypothesis. They prevent a GREEN formalization/provenance verdict for
the current bytes only.

## 6. Dependencies and hashes

Key frozen artifacts are:

| Artifact | SHA-256 |
|---|---|
| Durable kernel under review | b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74 |
| Parent tangent-gcd kernel | 4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160 |
| Current formal candidate | c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89 |
| Conductor reconciliation | b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705 |
| Discovery report | 4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298 |
| Hostile report | 5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a |
| Blind report | abaf181178b56925bec5fa6b624ddd79be528f4e419e2bff7f22adf9593b9992 |
| Normalization seam | 4c5296a91be66f3e370598d6f9853acc42fd173212f262c309140bdddf01e486 |
| Power/scope seam | 470737a35629b58ae82753f67ce12f26c449619a6e8a6bdc4ea17d2642562d7d |
| Blind post-unmask seam | 38601b87edfb4706a5206bbd7a7fb704e35b14f0c85d6b8704c698c81ce3ed44 |
| Repaired final candidate-consistency review | 3bf3aed9ce946bd70d518fb62a43b871a58f28a5dfcdf8c8fbdb3f9fc50af090 |
| Final power/owner replay | 06b78ac063a5c2f0886b0ca5315f6e931143c48cf5a8428878e422823f8bb301 |
| Proof graph | d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a |
| Active campaign | aadf701b1725cdd0004bb29e1fc625754e391e5475130df3a08a2a2e18d761d3 |

The direct mathematical dependencies remain exactly
M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction and
Divisor-bound-elementary.

## 7. Recommended state effect

Do not promote the current kernel bytes as the final durable artifact.
Apply only the delimiter, symbol-definition, and provenance repairs
listed in Sections 3--4, compute the new kernel hash, and rerun a bounded
byte/TeX/reference/provenance verification. No repeat mathematical
proof review is needed if the delta is exactly those repairs.

After that hygiene replay, the reduction may be promoted as
M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction with
proved_internal status and the sole exit label
strict_high_h_inverse_residue_fourier_sector.

Keep (K187.11), the complete high-height target, the complete
original-\(t=1\) residual, every original \(t\ge2\) and large-\(G\)
incidence, both M1 parents, GAR, all M2 parents, endpoint uniformity,
M9, both bridges, the quarter target, and every exponent claim open.
Do not edit the graph, synthesis, candidate, validation matrix, proof
draft, or any state file from this review.
