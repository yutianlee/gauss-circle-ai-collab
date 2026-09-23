# Round-195 postapplication scope/protected-state audit

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Verdict: **PASS**
- Applied graph SHA-256: `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Recovered starting graph SHA-256: `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`
- State Patch SHA-256: `8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e`
- Exact applied scope (`create/update/correct_rejected/reject/no_change`): **1/1/0/23/27**
- Shared-state mutation during this audit: none

## 1. Result

**PASS.** Exact inversion of the applied Round-195 operations recovers the
declared starting graph at SHA-256
`815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.
Reapplying the patch in memory with the actual application timestamp
`2026-08-30T04:40:21` and the adjudication judge reference reproduces the live
graph byte-for-byte at SHA-256
`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`.

The only mathematical-state footprint is the declared one: one new
proved-internal two-sector \(P_2\) node, the five declared owner-field classes,
and 23 appended rejected shadow-claim records. All 27 no-change obligations are
deep-equal to their recovered starting versions. The hard small-\(t\) owner
remains `open`, and complete \(P_2\), complete original \(t=1\), every parent
and bridge, the target theorem, and all exponent records are unchanged.

## 2. Exact statement and hypotheses

The postapplication comparison uses the current live graph, the current patch,
and the patch's inverse payload. The permitted delta is exactly:

1. create
   `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors` with status
   `proved_internal`, sole dependency
   `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`, and empty `implies`
   and `blockers`;
2. update only
   `M9-M1-hard-top-high-radical-small-t-residual-estimate` by adding the new
   dependency, adding the 20 declared evidence paths as inconclusive evidence,
   replacing `next_action`, and refreshing round/time metadata;
3. append exactly 23 new rejected shadow claims; and
4. leave the 27 named no-change obligations deeply unchanged.

The new node proves only the two safe physical-\(P_2\) sectors

\[
 P_2\mathbf 1_{\{\kappa\ge D_L\}},
\]

and

\[
 P_2\mathbf 1_{\{1\le\kappa<D_L\}}
 \mathbf 1_{\{\min(Y,D_L)\le H_B\mathfrak m\kappa\}},
\]

where

\[
 P_2=\mathbf 1_{\{|d-gm|\le D_L\}}
     \mathbf 1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil.
\]

It records as open the exact remaining packet region

\[
 P_{\rm rem}=P_2\mathbf 1_{\{1\le\kappa<D_L\}}
 \mathbf 1_{\{\min(Y,D_L)>H_B\mathfrak m\kappa\}}.
\]

The accepted state therefore does not contain a complete-\(P_2\) or
complete-original-\(t=1\) promotion.

## 3. Proof or derivation

### 3.1 Exact inverse and replay

Starting from the live graph, the audit removed the one created obligation,
removed the 23 patch rejection IDs, removed the declared dependency and evidence
additions from the owner, restored the prior owner `next_action`, and restored
`last_updated_round: 194` and `last_updated_at: 2026-08-30T02:58:26`. Canonical
serialization then had exactly the patch's declared starting hash. Both the
recovered graph and live graph pass graph validation with no issue.

Applying the unmodified patch to that recovered object at round 195, with the
actual judge reference and actual timestamp, returned exact operation counts
`1/1/0/23/27`. Its canonical serialization is byte-identical to the live graph.
This proves that no unrecorded application or formatting delta is hidden in the
postapplication bytes.

### 3.2 Complete obligation diff

The recovered/live obligation-index comparison gives:

- created: exactly
  `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`;
- removed: none;
- changed among pre-existing obligations: exactly
  `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
- all other pre-existing obligations changed: none.

For the owner, the changed keys are exactly `dependencies`, `evidence`,
`next_action`, `last_updated_round`, and `last_updated_at`. The protected fields
`id`, `type`, `track`, `title`, `status`, `statement_tex`, `implies`, `blockers`,
`owner`, and `required_output` are deeply equal. In particular, the owner status
is `open` before and after application.

The new node is exactly the patch-created object after automatic metadata and
judge-evidence handling. It has no implication edge, so it cannot promote a
parent indirectly. Its statement explicitly quarantines complete \(P_2\),
\(P_1\), complete original \(t=1\), all \(t\ge2\) ranges, the owner, parents,
endpoint theorem, bridges, target, and exponent.

### 3.3 All 27 no-change obligations

The deep-comparison result for all 27 declared no-change IDs is the empty set.
This covers:

- the ten accepted Round-187--193 reductions and safe sectors;
- the open complete-original-\(t\) endpoint owner, open smooth direct-\(M_1\)
  parent, and conditional direct-\(M_1\) assembly;
- GAR, \(M9\)-\(M1\), the three \(M9\)-\(M2\) channels and their parent,
  endpoint uniformity, and \(M9\);
- both derived-under-assumptions bridges;
- the internal one-third theorem, external Li--Yang benchmark, open quarter
  target, and elementary divisor bound.

Consequently the complete-\(t=1\) node remains open; analytic parents and both
bridges retain their starting statuses, statements, dependencies, blockers,
and evidence; `GC-target` remains open; and neither the internal one-third
record nor the external benchmark changes.

### 3.4 Rejected-claim diff

The rejected-claim list changes from 1732 to 1755 records. The 23 added IDs are
exactly the patch's 23 `reject` IDs; none collides with a live obligation or a
starting rejected claim. No starting rejection is changed or removed. All 23
new records have `last_updated_round: 195`, timestamp
`2026-08-30T04:40:21`, and the adjudication evidence reference.

Their reasons reject only false shadow promotions: full \(P_2\), extension of
the large-\(\kappa\) or capacity arguments, capacity as literal lower mass,
incorrect anchor/event/orientation simplifications, invalid squareful and
root-count Gram arguments, post-expansion mask substitutions, dropping the mask
commutator or \(T=0\), hidden fibre/height assertions, closure of original
\(t=1\), closure of owners/parents/bridges/target, and an exponent improvement.
Appending these records changes no analytic obligation status.

### 3.5 Non-obligation protected state

Outside `proof_obligations` and `rejected_claims`, every top-level graph key is
deep-equal between the recovered and live graphs. Thus schema, allowed statuses,
tracks, collaboration metadata, and round selection are untouched.

## 4. First doubtful or unproved step

There is no failed application or protected-state step. The first mathematical
step that remains unproved is exactly

\[
 \kappa<D_L,
 \qquad \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

The unresolved seam is the coefficient-sensitive cross-row
\(++,+-,-+,--\) Gram after exact same-site event recombination. The applied
graph does not infer literal lower mass from capacity and does not claim that
within-row multiplicity, anchor characters, separate orientation norms, or
squarefree root bounds resolve this remainder.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Live file and canonical live-object hashes | PASS: both `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2` |
| Exact inverse to declared starting graph | PASS: `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89` |
| Fixed-metadata replay to live graph | PASS: byte-identical, hash `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2` |
| Live, recovered, and replay graph validation | PASS: no issues |
| Exact operation scope | PASS: `1/1/0/23/27` |
| Created/removed/changed-existing obligations | PASS: `1/0/1`, with the declared IDs only |
| Owner changed-key set | PASS: dependency, evidence, next action, and two metadata keys only |
| Owner protected fields and open status | PASS |
| All 27 no-change obligations deep-equal | PASS |
| Starting rejections modified or removed | PASS: none |
| Exactly 23 declared rejections added | PASS |
| Top-level state outside obligations/rejections | PASS: deeply unchanged |
| P2/full-\(t=1\)/parent/bridge/target/exponent quarantine | PASS |
| Shared-state mutation during audit | PASS: none |

## 6. Dependencies and exact artifacts used

- `state/proof_obligations.yml` — SHA-256 `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/state_patch.json` — SHA-256 `8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e`.
- Recovered canonical starting graph — SHA-256 `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.
- `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` — SHA-256 `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_adjudication.md` — SHA-256 `fc6422ac07a165b3e8c9ba0fbbe79dc3aa77f2af74a1823b79f8d58665b198b4`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/synthesis.md` — SHA-256 `fdcf6ebed7455745034caaa7a30453ed9b84ff4c48440d61b720679d4d06e168`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/controls/preapply_hostile_scope_protected_state_audit.md` — SHA-256 `a1bf146b057da7078bbe2056a9c08f8287f47184b698339ed203b6e75b1bbb5e`.
- `math_collab/proof_obligations.py` — SHA-256 `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437`.

## 7. Recommended state effect

**Retain the applied graph unchanged.** The live graph is exactly the declared
Round-195 application and passes the postapplication protected-state audit. Keep
the new node limited to its two absolute-capacity sectors, keep the hard
small-\(t\) owner open, retain the exact strict \(P_{\rm rem}\) seam, and make no
promotion to complete \(P_2\), complete original \(t=1\), any parent or bridge,
the target theorem, or any exponent.
