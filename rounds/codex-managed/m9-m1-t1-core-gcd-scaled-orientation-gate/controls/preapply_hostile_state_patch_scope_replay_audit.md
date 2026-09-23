# Round 193 preapplication hostile State Patch scope/replay audit

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- State Patch:
  `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/state_patch.json`
- State Patch SHA-256:
  `dda2bc4af723b3e1d20c850904c6cca64360708927c80f836c0c857d91c4057a`
- Frozen starting-graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Audit mode: bounded read-only canonical validation, inverse, apply, and replay;
  no shared-state mutation and no full test suite

## 1. Result: PASS

**Verdict: PASS.**  The patch has exactly the declared
create/update/correct-rejected/reject/no-change scope

\[
 \boxed{1/1/0/15/25}.
\]

Its one created obligation depends only on an already
`proved_internal` Round-192 node.  The updated owner remains `open`.
All 25 `no_change` obligations are deeply identical before and after
application.  The 23 unique evidence paths all exist as files.  The
reversibility payload reconstructs the frozen graph exactly, and a
canonical in-memory apply/inverse/replay returns byte-canonical hashes
and deep equality in both directions.

At audit time the shared graph on disk already reflected the patch.  No
conclusion below treats a duplicate-create response from applying a
preapplication patch to that postapplication graph as a defect.  Instead,
the supplied inverse was executed only in memory; its canonical dump has
exactly the frozen hash above, and the canonical patch validator on that
reconstructed preimage returns no issue.  The audit wrote no shared state.

## 2. Exact statement and hypotheses audited

Let \(P\) be the JSON State Patch at SHA-256
`dda2bc4af723b3e1d20c850904c6cca64360708927c80f836c0c857d91c4057a`.
Let \(G_0\) be the frozen canonical graph with SHA-256
`7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`.
The requested checks are:

1. exact operation counts and unique IDs;
2. existence and status of the created node's dependency;
3. preservation of the open owner status and quarantine of every larger
   owner, bridge, theorem, and exponent;
4. deep equality for every `no_change` node;
5. existence of every unique evidence path;
6. completeness of `reversibility.restore_next_action` and
   `reversibility.restore_metadata`; and
7. canonical in-memory validation, application, inverse, and replay.

The canonical application parameters are Round 193 and judge reference

`rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/conductor_round193_adjudication.md`.

The wall-clock field was frozen in memory to the already observed
application timestamp `2026-08-30T02:10:41` only when testing exact
postimage equality.  This removes the canonical applicator's sole
nondeterministic field; it changes no graph semantics.

## 3. Proof and derivation

### 3.1 Exact patch scope

Parsing through the repository's own `_patch_ops` normalization gives:

| Operation | Count | Unique IDs | Exact effect |
|---|---:|---:|---|
| `create` | 1 | 1 | Create `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`. |
| `update` | 1 | 1 | Add one dependency, 23 inconclusive evidence paths, and replace `next_action` on the existing hard small-\(t\) residual owner. |
| `correct_rejected` | 0 | 0 | No correction of an existing rejected record. |
| `reject` | 15 | 15 | Add 15 new Round-193 rejected-overclaim records; no obligation is assigned status `rejected`. |
| `no_change` | 25 | 25 | Record scope decisions only; canonical application mutates none of them. |

The five ID sets are internally unique.  The updated owner is not also
listed under `no_change`.  The created ID and all 15 reject IDs are
absent from \(G_0\); in particular, no pre-existing obligation or
rejected-claim record is overwritten.

The created node has status `proved_internal` and the single dependency

`M9-M1-hard-top-t1-rho-large-farey-covector-reduction`.

That dependency exists in \(G_0\) with status `proved_internal`.  The
created node has no `implies` edge and no blocker.  The only new edge to
an existing owner is the one dependency appended to
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

### 3.2 Evidence census and path existence

The created node classifies 13 paths as positive and 10 as
inconclusive.  The owner update adds the same 23 paths as inconclusive
strict-sector evidence.  Hence the patch contains 46 evidence
references but exactly 23 unique paths.  A root-relative `is_file`
check gives

\[
 \boxed{23\text{ unique paths},\quad23\text{ files present},\quad0\text{ missing}.}
\]

Every evidence path is relative to the repository, contains no parent
escape, and resolves inside the workspace.  The diagnostic program and
its output remain in the `inconclusive` bucket; neither is promoted to
asymptotic proof evidence.

### 3.3 Owner status and no-change deep equality

Before application the updated owner has status `open`; after canonical
application it still has status `open`.  Its exact changed-key set is

\[
 \{\texttt{dependencies},\texttt{evidence},\texttt{next_action},
   \texttt{last_updated_round},\texttt{last_updated_at}\}.
\]

No status, title, statement, owner, type, track, implication, blocker, or
positive/negative evidence field changes.  The new dependency occurs
exactly once and was absent in \(G_0\).

Every one of the 25 `no_change` IDs exists in \(G_0\), and each complete
node dictionary is deeply equal in the canonical postimage:

\[
 \boxed{25/25\text{ exact deep equalities}.}
\]

The stronger whole-graph control also passes: apart from the single
updated owner, all 392 pre-existing obligation dictionaries are deeply
identical.  In particular, `M9-M1`, `M9-M2`, `M9`, endpoint uniformity,
both bridges, `GC-target`, the internal \(1/3\) result, and the accepted
external benchmark keep their exact prepatch states.

### 3.4 Reversibility payload

The payload's inverse rule covers every canonical mutation:

1. remove the one created obligation;
2. remove the 15 newly appended rejected-claim records;
3. remove the one `dependencies_added` value;
4. remove the 23 `evidence_added.inconclusive` values;
5. restore the owner's prior `next_action`; and
6. restore `last_updated_round: 192` and
   `last_updated_at: 2026-08-30T00:29:16`.

The stored `restore_next_action` is exactly equal to the \(G_0\) value,
and `restore_metadata` is exactly equal to the two \(G_0\) metadata
fields.  No status or other direct field requires restoration.  The
judge-reference evidence attached by canonical application lives only
on the newly created node and the 15 new rejected records, all of which
the inverse removes wholesale.

Applying this inverse to the observed postimage produces 393 obligations
and 1,697 rejected records.  Its canonical serialization has SHA-256

`7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`,

exactly the patch's frozen starting hash.

### 3.5 Canonical apply, inverse, and replay

The repository routines `validate_patch_against_graph`,
`apply_state_patch`, `validate_graph`, and `dump_graph` were called only
on in-memory objects.  The results are:

1. \(G_0\) graph validation: zero issues;
2. \(P\) against \(G_0\): zero issues, independently reproducing the
   official `Patch OK` condition;
3. canonical apply input: deeply unchanged, because the applicator works
   on a deep copy;
4. returned operation arrays: exact patch order and exact counts
   \(1/1/0/15/25\);
5. postimage graph validation: zero issues;
6. replayed postimage: deeply equal to the observed applied graph;
7. observed and replayed canonical postimage SHA-256:
   `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`;
8. inverse of the replayed postimage: deeply equal to \(G_0\); and
9. replay-inverse canonical SHA-256:
   `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`.

Thus both compositions pass:

\[
 P^{-1}(P(G_0))=G_0,
 \qquad
 P(P^{-1}(G_1))=G_1,
\]

with deep object equality and canonical byte hashes, not merely matching
node counts.

## 4. First doubtful or unproved step

None within the bounded preapplication scope.  The only operational
qualification is chronological: the shared graph was already the
postimage when this independent audit ran.  Exact recovery of the frozen
hash, zero canonical validation issues on that recovered preimage, and
exact two-sided replay remove any ambiguity caused by that timing.  No
evidence artifact's mathematical contents were re-adjudicated here;
this control verifies patch scope, existence, reversibility, and graph
semantics only.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| State Patch SHA-256 | **PASS:** `dda2bc4af723b3e1d20c850904c6cca64360708927c80f836c0c857d91c4057a`. |
| Frozen graph reconstruction | **PASS:** canonical hash `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`. |
| Official/canonical dry validation | **PASS:** zero patch issues on the exact frozen preimage. |
| Exact operation scope | **PASS:** `1/1/0/15/25`, with unique IDs and exact returned arrays. |
| Created dependency | **PASS:** exists and is `proved_internal`. |
| Created-node status | **PASS:** `proved_internal`, with one accepted dependency and no implication edge. |
| Owner status | **PASS:** `open` before and after; no status promotion. |
| Owner mutation boundary | **PASS:** only dependency, inconclusive evidence, next action, and last-update metadata change. |
| No-change nodes | **PASS:** 25/25 exact deep equality. |
| All other existing obligations | **PASS:** 392/392 exact deep equality. |
| Evidence paths | **PASS:** 23/23 unique paths exist; zero missing. |
| New rejected records | **PASS:** 15 new records; no existing obligation or rejected record overwritten. |
| Reversibility payload | **PASS:** exact prior next action and metadata; complete inverse coverage. |
| Canonical apply/replay | **PASS:** exact postimage deep equality and hash. |
| Canonical inverse/replay | **PASS:** exact preimage deep equality and frozen hash. |
| Shared-state mutation by this audit | **PASS:** none. |
| Full test suite | **NOT RUN, as required.** |

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, parsed and traversed in full in memory;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/state_patch.json` at the exact patch hash above;
5. `math_collab/proof_obligations.py` for the canonical parser,
   validator, applicator, indexer, and serializer semantics;
6. `math_collab/validate_state_patch.py` for the official dry-run
   contract; and
7. the 23 evidence paths enumerated by the patch, checked only for file
   existence.

No web source, numerical theorem experiment, State Patch write, graph
write, validation-matrix write, proof-draft write, or full test suite was
used.

## 7. Recommended state effect

Accept this preapplication scope/replay gate as **PASS** for State Patch
SHA-256
`dda2bc4af723b3e1d20c850904c6cca64360708927c80f836c0c857d91c4057a`.
The patch lawfully creates one strict `proved_internal` subordinate node,
adds it only as a dependency and inconclusive evidence to an owner that
remains `open`, records 15 rejected overclaims, and leaves the 25 declared
nodes unchanged.  This audit itself authorizes and performs no further
shared-state mutation.
