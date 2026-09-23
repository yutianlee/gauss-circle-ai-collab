# Round 187 preapplication State Patch scope, path, and reverse second audit

## 1. Result

**Verdict: GREEN.**

The State Patch at SHA-256

bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd

applies cleanly in memory to the canonical starting graph at SHA-256

d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a.

The exact operation inventory is

\[
 (\mathrm{create},\mathrm{update},\mathrm{correct\_rejected},
   \mathrm{reject},\mathrm{no\_change})
 =(1,1,0,14,20).
\]

The repository patch validator and graph validator return no issue. All
18 distinct evidence/judge paths exist and are nonempty. The only
inherited obligation changed by the simulation is the named hard-M1
small-\(t\) residual owner, and it remains open. No inherited status,
statement, implication, blocker, owner field, bridge, theorem, or
exponent changes.

With the application timestamp frozen at
2026-08-29T16:00:00 and the Round-187 adjudication used as judge
reference, the temporary patched graph hashes to

2721d097c940c64e0e6596a0c50d50aa768fdf33ad47e7e1c636c3b5dc6d3f04.

The prescribed inverse reproduces the starting graph byte-for-byte and
at its exact starting hash. Reapplying with the same frozen timestamp
reproduces the temporary patched bytes and hash exactly. The simulation
used deep-copied in-memory data and did not write the shared graph.

## 2. Frozen inputs and exact inventory

The audited authoritative inputs are:

| Artifact | SHA-256 |
|---|---|
| state/proof_obligations.yml | d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a |
| Round-187 state_patch.json | bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd |
| durable high-height kernel | a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2 |
| formal candidate | c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89 |
| report reconciliation | b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705 |
| final kernel/candidate verification | 3e9412b4404ca8399ed2350f459117b6b8b84fe479820a4e12a39da7bad1bb4d |
| final power/owner verification | 602a56c4ece7fce4a9e415eb9e95ce7e089dd690630e52fc2f28b16b4c08c0cc |
| final formalization/provenance verification | 5f3679b342a9210a2e0baa5c27ff82fc1fa5804bc662c8ea6e9c56886e0e417e |
| conductor adjudication | c6949ba7089e5d70c377c658771ef4bcf6be1ad603b453739de615cf91862ef5 |
| synthesis | 4e65ce906acbd0e1b7de18d5a6b728e560c7e3641ee4bbc349443566574a37e1 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |

The starting graph is already in the repository's canonical JSON
serialization: parse and canonical reserialization are byte-identical.
It contains 388 obligations and 1,600 rejected-claim records. The
temporary patched graph contains 389 obligations and 1,614 rejected
records.

The operation lists contain no duplicate or cross-class ID. The created
obligation is absent from the starting obligation set. All 14 rejected
claim IDs are absent from both starting obligations and starting
rejected claims. The update target and all 20 no-change IDs exist.

The patch creates exactly

M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction

with status proved_internal, direct dependencies

- M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction; and
- Divisor-bound-elementary,

and empty implication and blocker lists. It updates exactly

M9-M1-hard-top-high-radical-small-t-residual-estimate.

The created node receives 15 positive evidence paths and three
diagnostic/inconclusive paths from the patch; the adjudication judge
reference is additionally placed in its inconclusive bucket by the
standard applicator. The still-open owner receives exactly 16 new
inconclusive evidence paths. Each of the 14 new rejected-claim records
receives Round-187 metadata and the adjudication judge reference.

## 3. Path and hash audit

Every distinct path named by the create/update evidence and judge
reference exists. Current exact hashes are:

| Evidence path | SHA-256 |
|---|---|
| proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md | a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2 |
| candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md | c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89 |
| controls/conductor_round187_wolfram_inverse_residue_check.md | 032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113 |
| controls/inverse_residue_exact_check.wls | e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd |
| reports/blind_high_h_rederivation.md | abaf181178b56925bec5fa6b624ddd79be528f4e419e2bff7f22adf9593b9992 |
| reports/deletion_resonance_capacity_audit.md | 5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a |
| reports/literal_height_fourier_attack.md | 4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298 |
| reviews/blind_post_unmask_owner_scope_seam_review.md | 38601b87edfb4706a5206bbd7a7fb704e35b14f0c85d6b8704c698c81ce3ed44 |
| reviews/candidate_normalization_post_tex_repair_verification.md | b357dc049f9ebf0a8b21b6ed1d816426e166fa78347e2b124822342f48b2b458 |
| reviews/conductor_round187_adjudication.md | c6949ba7089e5d70c377c658771ef4bcf6be1ad603b453739de615cf91862ef5 |
| reviews/conductor_round187_report_reconciliation.md | b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705 |
| reviews/final_kernel_candidate_consistency_final_hash_verification.md | 3e9412b4404ca8399ed2350f459117b6b8b84fe479820a4e12a39da7bad1bb4d |
| reviews/final_kernel_formalization_provenance_hygiene_review.md | 2b59a686404540dc6a5f566e7118fcd605a0ce0d72ec966964a64f6df030383a |
| reviews/final_kernel_formalization_provenance_post_repair_verification.md | 5f3679b342a9210a2e0baa5c27ff82fc1fa5804bc662c8ea6e9c56886e0e417e |
| reviews/final_kernel_power_owner_scope_post_repair_verification.md | 602a56c4ece7fce4a9e415eb9e95ce7e089dd690630e52fc2f28b16b4c08c0cc |
| reviews/inverse_residue_normalization_multiplicity_post_repair_verification.md | 4fa37825aedfa940bb7ca55b0b4f75145770dc4bb007dc68bf5ee69005ea6739 |
| reviews/power_literal_scope_post_tex_repair_verification.md | 52c2397a88577001fe54c1541a5c831e89e29522320bdefc4ce9c4b1c37b57f8 |
| synthesis.md | 4e65ce906acbd0e1b7de18d5a6b728e560c7e3641ee4bbc349443566574a37e1 |

Paths shortened in this table after the first row are relative to
rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/.
All files are nonempty. The kernel's source-candidate,
reconciliation, and diagnostic hashes agree with the named files. The
adjudication and synthesis both bind the current durable kernel hash
a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2.
The three final reviews are GREEN at that same kernel hash.

## 4. Apply simulation and scope delta

The official patch validator returns no issue against the frozen
starting graph. The official graph validator returns no issue after the
in-memory application. Every dependency, implication, and blocker
reference resolves.

Dependency edges change from 1,382 to 1,385. The only additions are:

1. M9-M1-hard-top-high-radical-small-t-residual-estimate
   \(\to\)
   M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction;
2. M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction
   \(\to\)
   M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction; and
3. M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction
   \(\to\) Divisor-bound-elementary.

There is no removed dependency edge. Implication edges remain exactly
326, blocker edges remain exactly 70, and neither set has an addition
or removal. The dependency-cycle strongly connected component set is
identical before and after application: three inherited cyclic
components and no new cycle.

Among all 388 inherited obligations, only the hard-M1 small-\(t\)
owner changes. Its changed fields are exactly:

- dependencies;
- evidence;
- next_action;
- last_updated_round; and
- last_updated_at.

Its status stays open. Its statement, title, type, track, implications,
blockers, owner, and every other field remain unchanged. The added
dependency is exactly the new subordinate node. All 16 evidence
additions go only to the inconclusive bucket. Its next action narrows
to the exact one-sided complement

\[
 U>4H_B,\qquad q_U(k)>H_B,\qquad |k|_U>H_B,
\]

with both orientations and all \(h,v,t,k\), selectors, endpoints,
phases, and zero extensions retained under one outer real part. It
explicitly preserves every \(t\ge2\) and large-\(G\) near-resonant
remainder.

All 20 no-change obligations remain object-identical. In particular,
the following protected objects are byte-structure identical before
and after the simulation:

- M9-M1: open;
- M9-M2: open;
- M9: open;
- Conditional-bridge: derived_under_assumptions;
- GC-global-M1-alternative-bridge: derived_under_assumptions;
- GC-partial-one-third: proved_internal;
- GC-external-Li-Yang-theta-star: proved_external_dependency; and
- GC-target: open.

There is no inherited status drift and no inherited statement drift.
Thus the internal \(1/3\) result, external
\(0.3144831759740614\ldots\) result, and \(1/4\) target boundary remain
exactly unchanged.

## 5. New-node statement and overclaim audit

The created node statement matches the durable kernel and adjudication.
It proves only:

1. the exact inverse-residue Fourier decomposition on the inherited
   Round-185 carrier;
2. the absolute target-safe transformed packet consisting of the
   complete \(U=1\) contribution, every exact conductor \(q\le H_B\),
   every remaining mode with \(U\le4H_B\), and every remaining ordinary
   edge mode \(0<|k|_U\le H_B\);
3. the exact high-conductor complement with positive capacity
   \(O(YL^2X^\varepsilon)\); and
4. centered-conductor, prime-\(U\), and high-mode-energy mechanism
   controls.

The statement explicitly says that the one-sided
\(O(L^2X^\varepsilon)\) estimate for the complement is open. It also
states that the controls are not literal lower mass and denies every
complete high-height, complete \(t=1\), small-\(t\) owner, parent,
bridge, theorem, and exponent conclusion. Its implication and blocker
lists are empty.

The new node is therefore a proved subordinate reduction, not an owner
closure. Updating the parent only by an inconclusive dependency and
evidence preserves this distinction. The 14 rejected-claim records
exactly quarantine zero/low-mode overcoverage, positive-capacity,
centering, orientation, energy, physical-sector, cutoff-maximality,
complete-\(t=1\), parent, and exponent overclaims. No rejected operation
changes an existing obligation status.

## 6. Reverse and replay

The reverse simulation performed exactly the patch's declared inverse:

1. remove the one created obligation;
2. remove the 14 appended rejected-claim records;
3. remove the one owner dependency;
4. remove the 16 owner evidence additions;
5. restore the owner next action; and
6. restore the owner metadata.

The frozen starting owner has

\[
 \mathrm{last\_updated\_round}=186,\qquad
 \mathrm{last\_updated\_at}=\text{2026-08-28T09:12:29}.
\]

These values match the patch's reverse metadata exactly. The graph's
949-byte prior next action and the patch's restore value are identical;
both have SHA-256

85f47b99fa5ae3b17fc7145a939990f94b4bffd9d46bc524639db06c4bb7b785.

After reversal, the object equals the parsed starting graph and its
canonical bytes equal the original 2,025,313-byte graph file. The
reversed SHA-256 is exactly

d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a.

Reapplying the same patch with Round 187, the adjudication judge
reference, and the same frozen application timestamp reproduces the
temporary patched graph byte-for-byte at

2721d097c940c64e0e6596a0c50d50aa768fdf33ad47e7e1c636c3b5dc6d3f04.

A real application at another second will have a different graph hash
only because last-updated timestamps are serialized. Its structural
delta must remain the exact audited \(1/1/0/14/20\) inventory.

## 7. Recommended state effect

Permit the conductor to apply exactly the frozen Round-187 State Patch
at SHA-256

bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd

to the starting graph at SHA-256

d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a.

Permit only the one subordinate creation, the one still-open owner
update, and the 14 new rejected-claim records described above. Do not
alter any other obligation, status, statement, implication, blocker,
owner, M9-M1/M9-M2/M9 node, bridge, GC theorem, target, or exponent
boundary. This audit authorizes no graph mutation by the auditor and
edits only this assigned control report.
