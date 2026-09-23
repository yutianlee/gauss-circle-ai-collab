# Round 194 hostile State Patch post-repair verification

## 1. Result

**Verdict: PASS.**

The repaired State Patch is mechanically valid, contains no undefined
`mfrak` token, decodes to exactly two occurrences of `\mathfrak m` in the
new `next_action`, and preserves the physical cofactor \(m\) separately in
the masks `d-gm` and `d'-gm'`.  The full hostile production-apply,
deep-equality, and reverse audit passes with no graph mutation during this
verification.

- Repaired State Patch SHA-256:
  `918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`
- Starting graph SHA-256:
  `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`

## 2. Exact repaired notation

The raw JSON now contains the two escaped strings

```text
H_B \\mathfrak m kappa u
Y/(H_B \\mathfrak m)
```

and the decoded `next_action` contains exactly

```text
H_B \mathfrak m kappa u
Y/(H_B \mathfrak m)
```

The decoded counts are:

- `\mathfrak m`: exactly 2;
- undefined `mfrak`: 0;
- physical `d-gm`: exactly 1;
- physical `d'-gm'`: exactly 1.

Thus the spectral Fourier-lift gcd \(\mathfrak m\) and physical cofactor
\(m\) are distinct exactly as required by the Round-194 reconciliation and
synthesis.  The reversibility payload retains the byte-exact old
Round-193 `next_action`, as it must for exact reversal.

## 3. Production scope derivation

The repository validator returns `Patch OK`.  An in-memory call to the
production `apply_state_patch` function with `round_index=194` gives the
unchanged operation census:

| Operation | Count |
|---|---:|
| `create` | 0 |
| `update` | 1 |
| `correct_rejected` | 0 |
| `reject` | 20 |
| `no_change` | 26 |

Among all 394 pre-existing obligations, the only changed object is
`M9-M1-hard-top-high-radical-small-t-residual-estimate`, and its only diff
paths are:

- `evidence.inconclusive`;
- `next_action`;
- `last_updated_round`;
- `last_updated_at`.

All ten added evidence paths exist and are classified only as
inconclusive.  Exactly twenty new rejected-claim records are appended; no
existing rejected claim is modified.  Post-application graph validation
returns no issue.

## 4. First doubtful or unproved step

No patch defect remains.  The first unproved mathematical step is still the
complete fixed-packet \(P_2\) determinant-fibre estimate stated in the
repaired `next_action`.  The patch records that objective as strategy; it
does not assert the estimate, a parent, a bridge, a theorem, or an exponent.

## 5. Hostile controls and outcomes

| Control | Outcome |
|---|---|
| Repaired hash and JSON | **PASS.** Exact hash above; JSON parses. |
| Repository dry validator | **PASS.** `Patch OK`. |
| Undefined-token scan | **PASS.** No `mfrak`. |
| Decoded spectral notation | **PASS.** Exactly two `\mathfrak m` occurrences. |
| Physical/spectral distinction | **PASS.** Physical `d-gm`, `d'-gm'` remain separate. |
| Mutation surface | **PASS.** Only the declared open owner and new rejected records change. |
| Protected graph fields | **PASS.** No status, dependency, implies, blocker, statement, owner, parent, endpoint, bridge, theorem, or exponent drift. |
| `no_change` set | **PASS.** All 26 IDs are unique and deeply equal after simulated apply. |
| Evidence paths/classification | **PASS.** 10 of 10 exist; all inconclusive. |
| Existing rejection preservation | **PASS.** No existing rejection changes. |
| Reverse reconstruction | **PASS.** Deep-equal and canonical-hash-equivalent to the starting graph. |
| Synthesis repairs | **PASS.** P2 selection, exact target/deficit, GAR bypass, BAL normalization, source scope, downstream scope, and exponent quarantine remain accurately encoded. |

## 6. Dependencies and exact artifacts used

- `state/proof_obligations.yml` at the starting hash above;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json` at the repaired hash above;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/synthesis.md`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_report_reconciliation.md`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/controls/preapply_hostile_state_patch_scope_audit.md`;
- `math_collab/proof_obligations.py`;
- `math_collab/validate_state_patch.py`.

All application, validation, diff, and reversal checks were read-only or
in-memory.  No graph, patch, synthesis, campaign, ledger, or other shared
state was edited.

## 7. Recommended state effect

**Approve the repaired State Patch at SHA-256
`918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`
for conductor application.**

It remains a strategy-only patch: one open owner's inconclusive evidence,
next action, and metadata may change, and the twenty exact rejected
overclaims may be recorded.  No analytic status, parent, endpoint result,
bridge, theorem, global result, or exponent is promoted.
