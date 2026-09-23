# Round 173 independent pre-apply reversibility audit

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Role: independent pre-apply patch and reverse auditor
- Patch: rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/state_patch.json
- Authoritative graph: state/proof_obligations.yml
- Verdict: **GREEN**

## 1. Result

The authoritative starting graph has exactly the required SHA-256:

70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f.

The patch passes the repository patch validator for Round 173. Applying it
to a private temporary copy also passes post-application graph validation
and produces the simulation-specific SHA-256:

77fcbd69553a5d1bd606a89093f8b0590a8233c772dcb30e09493514a37752ba.

The observed mutation is exactly one created obligation and two updated
obligations. A mechanical inverse removed the created obligation and
restored the complete preimage records for the two updated obligations.
After canonical serialization, the reversed file was byte-for-byte equal to
the starting file and recovered the exact starting SHA-256:

70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f.

No authoritative state file was modified.

## 2. Exact statement and hypotheses

The audit froze these inputs:

1. starting graph bytes from state/proof_obligations.yml;
2. the Round-173 state_patch.json bytes;
3. round index \(173\); and
4. the repository's own load, validation, application, graph-validation,
   and canonical-dump functions.

The patch declares:

- one create operation:
  M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction;
- two update operations:
  M9-M2-top-endpoint-density-discrepancy-energy and
  M9-M2-top-endpoint-signed-cone;
- zero reject operations;
- zero corrected-rejected operations; and
- sixteen no-change declarations.

The starting graph contains \(376\) obligations and is already byte-identical
to the repository's canonical JSON dump. This last fact is necessary for a
canonical mechanical reversal to be tested at the byte level rather than
only at the parsed-object level.

## 3. Proof or derivation

### 3.1 Pre-apply validation

The repository validator was run without its apply flag against the
authoritative graph and the Round-173 patch. It returned Patch OK.

The authoritative graph SHA-256 was checked immediately before simulation
and again after all simulation work; both values were the required starting
hash.

### 3.2 Private simulated application

Two private copies of the starting bytes were made in a newly generated
system temporary directory: one immutable comparison copy and one simulated
graph. The repository validator then applied the patch only to the simulated
copy with round index \(173\).

The validator reported exactly:

- created: one named obstruction;
- updated: the two named hard-TOP owner interfaces;
- no-change: sixteen named existing obligations;
- rejected: none; and
- corrected rejected claims: none.

The validator's post-apply graph check passed. A separate graph-only
validation of the simulated result also returned Graph OK.

The simulated graph contained \(377\) obligations. Relative to the starting
parsed graph, the exact observed structural delta was:

1. one added ID, exactly the declared created ID;
2. two changed existing IDs, exactly the declared update IDs;
3. no removed obligation;
4. no changed non-obligation top-level key; and
5. no mutation of any of the sixteen no-change records.

For each updated owner, the only changed keys were:

- dependencies;
- evidence;
- next_action;
- last_updated_round; and
- last_updated_at.

Each received exactly the declared new dependency and six inconclusive
evidence paths. Each moved from last-updated round \(172\) to \(173\).
The automatically generated simulation timestamp was
2026-08-26T23:28:11.

### 3.3 Mechanical inverse

The inverse was derived from the patch operation classes and the frozen
preimage, not by copying the starting file over the simulated result:

1. remove from the applied obligation list the sole ID appearing in the
   patch's create list;
2. for each ID in the patch's update list, replace the applied record at the
   same list position by its complete frozen preimage record, thereby
   restoring dependencies, evidence, next_action, last_updated_round, and
   last_updated_at together;
3. perform no rejected-claim inverse because both reject lists are empty;
4. perform no inverse for no-change declarations because the application
   engine does not mutate those records; and
5. serialize with the repository's canonical graph writer.

The reversed parsed object equalled the starting parsed object. The reversed
graph passed repository graph validation with zero issues. Its obligation
count returned from \(377\) to \(376\).

Most importantly,

\[
 \text{reversed bytes}=\text{starting bytes}
\]

exactly, and both SHA-256 values equal

70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f.

## 4. First doubtful or unproved step

There is no unresolved reversibility seam in this patch.

The simulated applied hash is not a prediction of the future authoritative
applied hash. The application engine inserts the current wall-clock value
into last_updated_at for the created and updated records. A later real
application will therefore normally have different bytes and a different
result hash even when every logical mutation is identical. The actual
post-apply hash must be recorded after authoritative application.

This audit establishes mechanical validity, graph validity, mutation scope,
and exact invertibility from a frozen preimage. It does not independently
re-adjudicate the mathematical theorem or authorize a different graph
effect.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| required starting SHA-256 | **GREEN** |
| authoritative graph unchanged during simulation | **GREEN** |
| repository dry patch validation | **GREEN** |
| private-copy application | **GREEN** |
| post-apply graph validation | **GREEN** |
| simulated result hash recorded | **GREEN** |
| expected created IDs versus observed | **GREEN: 1/1 exact** |
| expected updated IDs versus observed | **GREEN: 2/2 exact** |
| unexpected removed IDs | **NONE** |
| unexpected top-level mutations | **NONE** |
| no-change records mutated | **NONE: 0/16** |
| reject operations | **NONE** |
| corrected-rejected operations | **NONE** |
| inverse restores created-node absence | **GREEN** |
| inverse restores both complete owner preimages | **GREEN** |
| reversed object equals starting object | **GREEN** |
| reversed graph validation | **GREEN** |
| reversed bytes equal starting bytes | **GREEN** |
| reversed SHA-256 equals starting SHA-256 | **GREEN** |

No numerical mathematical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The audit used only:

1. state/proof_obligations.yml;
2. the Round-173 state_patch.json;
3. math_collab.validate_state_patch;
4. the graph load, validate, apply, and canonical-write implementation in
   math_collab/proof_obligations.py; and
5. private temporary copies outside the workspace.

The temporary simulation contained no authoritative path. The private
directory was used only for the start copy, simulated application, and
reversed copy.

## 7. Recommended state effect

The patch is **GREEN for authoritative application**, subject to the normal
final conductor decision and a fresh immediate starting-hash check.

After a real application, record its actual result hash, rerun graph
validation, and retain the following exact inverse recipe:

1. remove
   M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction;
2. restore the complete pre-Round-173 records for
   M9-M2-top-endpoint-density-discrepancy-energy and
   M9-M2-top-endpoint-signed-cone; and
3. leave rejected claims, no-change obligations, and every other graph
   field untouched.

This recipe was mechanically demonstrated to recover the exact starting
bytes and hash.

