# Round 194 preapplication hostile State Patch scope audit

## 1. Result

**Verdict: REPAIR.**

The patch is mechanically valid and its mutation scope is otherwise exact:
it updates one already-open obligation only in inconclusive evidence,
`next_action`, and last-updated metadata; appends twenty new rejected-claim
records; and changes no other pre-existing graph object.  All twenty-six
declared `no_change` obligations remain deeply equal under a production
in-memory application.

One literal repair is required before application.  The new `next_action`
twice writes the undefined token `mfrak` where the Round-194 reconciliation,
adjudication, and synthesis explicitly require the spectral Fourier-lift gcd
\(\mathfrak m\), distinct from the physical cofactor \(m\).  This is the
notation ambiguity that Round 194 specifically repaired, so the State Patch
does not yet reflect the synthesis exactly.

- State Patch SHA-256:
  `b9dfa81fe6b9461b78c37a0e203ca0bfb45df8655766db6a613342f4c3d7651d`
- Starting graph SHA-256:
  `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`
- Authoritative-state mutation during this audit: none

## 2. Exact patch scope

The operation census is:

| Operation | Count | Scope |
|---|---:|---|
| `create` | 0 | No proof obligation created. |
| `update` | 1 | `M9-M1-hard-top-high-radical-small-t-residual-estimate` only. |
| `correct_rejected` | 0 | No prior rejection changed. |
| `reject` | 20 | Twenty new rejected-claim records; no existing obligation is rejected. |
| `no_change` | 26 | All IDs exist, are unique, and remain deeply equal. |

For the sole updated obligation, the production diff has exactly four paths:

1. `evidence.inconclusive` -- ten Round-194 artifacts are appended;
2. `next_action` -- the complete \(P_2\) Round-195 objective replaces the
   prior two-mask action;
3. `last_updated_round` -- becomes 194; and
4. `last_updated_at` -- is supplied by the production applicator.

Its `status` remains `open`.  Its `id`, `type`, `track`, `title`,
`statement_tex`, `dependencies`, `implies`, `blockers`, positive evidence,
negative evidence, and `owner` remain deeply equal.  Across all 394
pre-existing obligations, no other object changes.  No existing rejected
claim changes; exactly twenty new IDs are appended.

Thus there is no status, dependency, implication, blocker, statement,
parent, endpoint, bridge, theorem, or exponent drift.  `round_assessment`
is assessment payload and does not mutate the proof graph.

## 3. Proof and replay derivation

The repository validator returned `Patch OK` against the exact starting
graph.  I then called the production `apply_state_patch` function in memory
with `round_index=194` and a diagnostic judge reference.  The result was:

- created: 0;
- updated: 1;
- corrected rejections: 0;
- new rejected claims: 20;
- declared no-change objects: 26;
- post-application graph validation issues: 0.

All ten `evidence_added.inconclusive` paths exist.  No positive or negative
evidence is added.  The twenty rejected IDs are absent from both the starting
obligation index and the starting rejected-claim index, so production apply
creates records rather than changing statuses or overwriting prior controls.

The simulated graph was then inverted only from the declared reversibility
payload: remove the twenty introduced rejected records, remove the ten
introduced inconclusive evidence strings, restore the old `next_action`, and
restore Round-193 metadata.  The reversed object is deeply equal to the
starting graph.  Its canonical sorted-JSON SHA-256 is
`48db76f437bfd342649d23ea11b5bb8f3d2b51b2fa9c1c985960fc8a11103bc1`
both before application and after reversal.

## 4. First defect and exact repair

The first defect is in the update's `next_action`:

```text
|R_core,fix^sigma(P_2W)|<<H_B mfrak kappa u X^epsilon
...
Y/(H_B mfrak)
```

`mfrak` is not a graph symbol.  It is neither the spectral \(\mathfrak m\)
nor the physical \(m\), and it defeats the explicit Round-194 notation
repair.  In raw JSON, replace the two occurrences by an escaped TeX token:

```text
H_B \\mathfrak m kappa u
Y/(H_B \\mathfrak m)
```

After JSON parsing these become `H_B \mathfrak m kappa u` and
`Y/(H_B \mathfrak m)`, matching the synthesis.  No other patch field should
change.  Recompute the patch SHA and rerun the dry validator after this
two-token repair.

## 5. Hostile controls and outcomes

| Control | Outcome |
|---|---|
| Exact graph hash | **PASS.** Matches `starting_graph_sha256`. |
| JSON and repository validator | **PASS.** `Patch OK`. |
| Update owner and status | **PASS.** Correct already-open hard-M1 small-\(t\) owner; status stays open. |
| Evidence classification | **PASS.** Ten paths, all existing and all inconclusive. |
| Protected structural fields | **PASS.** Status/dependencies/implies/blockers/statement/owner and every downstream theorem field are unchanged. |
| Rejected-claim isolation | **PASS.** Twenty new records; no existing rejection or obligation status is altered. |
| `no_change` deep equality | **PASS.** 26 of 26. |
| Reverse reconstruction | **PASS.** Deep-equal canonical recovery. |
| P1/P2 adjudication | **PASS.** Boolean-first-failure and report-vote overclaims are rejected; complete P2 is frozen by its close-coordinate geometry. |
| Relative-mass normalization | **PASS.** Proportional contraction is rejected as an equivalent owner target. |
| Operator and false-control quarantine | **PASS.** Post-expansion masking, separate orientation norms, width widening, static Farey refinement, coefficient-blind involution, and arbitrary coefficients are rejected. |
| GAR hierarchy | **PASS.** The patch records that the alternative route bypasses blockwise M9-M1 and M9. |
| Remaining-label BAL normalization | **PASS.** The critical \(L^4\)-to-\(L^3\) ledger is not assigned to the \(L^{3/2}\) remaining-label packet owner. |
| Source scope | **PASS.** The no-match is explicitly dated and corpus-limited. |
| Parent/bridge/theorem/exponent quarantine | **PASS.** P2 is not allowed to close P1, complete original \(t=1\), M9-M1, M9, a bridge, the target, or an exponent. |
| Spectral-gcd notation | **REPAIR.** Replace both `mfrak` tokens by `\\mathfrak m` in raw JSON. |

Apart from that notation defect, the patch reflects the repaired synthesis
exactly and introduces no hidden analytic promotion.

## 6. Dependencies and exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml` at the starting hash above;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json` at the patch hash above;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/synthesis.md`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_report_reconciliation.md`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`;
- `math_collab/proof_obligations.py`;
- `math_collab/validate_state_patch.py`.

All application, diff, no-change, validation, and reverse checks were
read-only or in-memory.  No graph, patch, campaign, synthesis, ledger, or
other shared-state file was edited.

## 7. Recommended state effect

**Do not apply the current hash.**  Repair only the two `mfrak` occurrences
in `next_action`, recompute the State Patch SHA-256, and rerun the repository
dry validator.  The operation counts, evidence list, rejected records,
reversibility payload, no-change set, round assessment, and every other
field should remain byte-for-byte unchanged.

After that literal repair and a clean dry validation, the patch is
scope-safe for application.  It may add strategy/source evidence and a
Round-195 action, but it promotes no analytic statement and changes no
status, parent, endpoint result, bridge, theorem, or exponent.
