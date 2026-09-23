# Round 173 post-application independent reverse audit

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Role: independent post-application graph and reverse auditor
- Applied patch: rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/state_patch.json
- Authoritative graph: state/proof_obligations.yml
- Verdict: **GREEN**

## 1. Result

The authoritative post-application graph has exactly the reported SHA-256:

04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a.

It passes repository graph validation with zero issues. Relative to the
frozen pre-Round-173 graph, the applied delta is exactly the patch's one
created obligation and two updated obligations. No existing status,
rejected claim, theorem record, exponent record, no-change record, or
non-obligation top-level field changed unexpectedly.

The authoritative graph was reversed only in memory. Removing the one
created obligation and restoring the complete frozen preimage records for
the two updated owners produced a valid graph whose canonical bytes are
exactly equal to the frozen starting bytes. The recovered SHA-256 is:

70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f.

The authoritative graph bytes and hash were identical before and after the
audit.

## 2. Exact statement and hypotheses

The audit froze:

1. the pre-Round-173 graph bytes already authenticated at
   70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f;
2. the applied Round-173 state patch;
3. the current authoritative graph bytes at
   04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a;
   and
4. the repository's canonical graph serialization and validation rules.

The frozen graph has \(376\) obligations. The applied graph has \(377\).
The patch declares:

- one created proved-internal obstruction;
- two updates to already-open hard-TOP owner interfaces;
- zero status-change operations;
- zero reject operations;
- zero corrected-rejected operations; and
- sixteen no-change declarations.

No reversed graph was written to the workspace or to the authoritative
state path.

## 3. Proof or derivation

### 3.1 Current graph validation and exact forward delta

The repository graph validator returned Graph OK for the authoritative
post-application file.

The sole observed added obligation is exactly:

M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction.

Its complete non-metadata content matches the create payload byte-for-field.
Its status is proved_internal, its last_updated_round is \(173\), and its
application timestamp is 2026-08-26T23:36:23.

The only changed pre-existing obligations are exactly:

1. M9-M2-top-endpoint-density-discrepancy-energy; and
2. M9-M2-top-endpoint-signed-cone.

For each, the changed keys are exactly:

- dependencies;
- evidence;
- next_action;
- last_updated_round; and
- last_updated_at.

Each owner received exactly the patch-declared new obstruction dependency,
exactly the six declared inconclusive evidence paths, and no positive or
negative evidence mutation. Neither lost a dependency or evidence path.
Both next_action values match the patch exactly. Both moved from
last-updated round \(172\) to \(173\), with the common application timestamp
2026-08-26T23:36:23.

There is no removed obligation and no changed non-obligation top-level key.
All sixteen no-change obligation records are byte-for-object unchanged.

### 3.2 Status, rejected-claim, theorem, and exponent delta

Among all \(376\) obligations present before application, the number of
status changes is zero. The only new status-bearing record is the created
proved-internal obstruction specified by the patch.

The rejected-claim collection is exactly unchanged:

- added rejected claims: zero;
- removed rejected claims: zero; and
- modified rejected claims: zero.

All five theorem-type records are exactly unchanged:

- GC-target;
- GC-partial-one-third;
- GC-global-real-second-moment-density-one-quarter;
- GC-integer-one-separated-density-one; and
- GC-external-Li-Yang-theta-star.

The three explicit theorem/exponent boundary records compared for closure
are also exactly unchanged:

- GC-partial-one-third;
- GC-external-Li-Yang-theta-star; and
- GC-target.

Thus the internal one-third exponent, accepted external Li--Yang benchmark,
and quarter target receive no field, status, statement, dependency,
evidence, timestamp, or action mutation from Round 173.

### 3.3 In-memory inverse

The inverse was constructed only in memory from the authoritative applied
object, the applied patch, and the frozen preimage records:

1. delete the sole obligation named in the patch's create list;
2. replace the two records named in the patch's update list, at their
   existing list positions, by their complete frozen preimage records;
3. make no rejected-claim edit because the applied patch has no reject or
   corrected-rejected operation;
4. make no no-change edit because those records were not mutated; and
5. serialize the resulting in-memory object with the repository's canonical
   graph dumper.

The reversed obligation count is \(376\). The reversed parsed object equals
the complete frozen starting object. Repository validation of the reversed
in-memory object returns zero issues.

The canonical reversed bytes equal the frozen starting bytes exactly, not
merely modulo parsing or key order. Their SHA-256 is exactly:

70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f.

## 4. First doubtful or unproved step

There is no unresolved graph-integrity or reversibility seam.

This audit is intentionally mechanical. It confirms that the authoritative
application has exactly the declared scope and that the frozen preimage
suffices for an exact rollback. It does not re-adjudicate the mathematical
obstruction or request a rollback.

The applied hash differs from the earlier simulated hash because the graph
writer records the actual application time in last_updated_at. The current
authoritative hash above is therefore the controlling post-Round-173 hash.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| authoritative post-apply SHA-256 | **GREEN** |
| current authoritative graph validation | **GREEN** |
| frozen preimage SHA-256 | **GREEN** |
| created IDs expected versus observed | **GREEN: 1/1 exact** |
| created payload core | **GREEN: exact** |
| created status and round metadata | **GREEN** |
| updated IDs expected versus observed | **GREEN: 2/2 exact** |
| update dependency additions | **GREEN** |
| update evidence additions | **GREEN: 6/6 for each owner** |
| update next_action values | **GREEN** |
| unexpected dependency or evidence removal | **NONE** |
| removed obligations | **NONE** |
| existing status changes | **NONE** |
| rejected-claim changes | **NONE** |
| theorem-record changes | **NONE: 0/5** |
| exponent-boundary record changes | **NONE: 0/3** |
| no-change records mutated | **NONE: 0/16** |
| non-obligation top-level changes | **NONE** |
| reversed graph validation | **GREEN** |
| reversed object equals frozen object | **GREEN** |
| reversed bytes equal frozen bytes | **GREEN** |
| reversed SHA-256 equals starting SHA-256 | **GREEN** |
| authoritative bytes unchanged during audit | **GREEN** |

No numerical mathematical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The audit used only:

1. the authoritative state/proof_obligations.yml after Round-173
   application;
2. the frozen pre-Round-173 graph bytes from the independent pre-apply
   audit;
3. the applied Round-173 state_patch.json;
4. the repository graph loader, validator, and canonical dumper; and
5. in-memory comparison and reversal logic.

No authoritative state mutation, patch reapplication, temporary reversed
file, graph normalization write, or shared-state edit was performed.

## 7. Recommended state effect

The post-application graph and its State Patch are **GREEN for Round-173
closure**. Retain the authoritative graph at:

04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a.

If an exact rollback is ever required, the verified inverse is:

1. remove
   M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction;
2. restore the complete frozen pre-Round-173 records for
   M9-M2-top-endpoint-density-discrepancy-energy and
   M9-M2-top-endpoint-signed-cone; and
3. leave rejected claims, no-change records, all theorem and exponent
   records, and every other graph field untouched.

That in-memory inverse has been verified to recover the exact starting bytes
and hash.

