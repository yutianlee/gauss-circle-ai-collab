# Round 173 post-application graph scope verification

- Campaign: `m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate`
- Round: 173
- Role: independent post-application graph, exact-delta, and theorem-quarantine auditor
- Expected authoritative SHA-256: `04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`
- Observed authoritative SHA-256: `04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`
- Allocation: 100% analytical/algebraic; 0% numerical
- Verdict: **GREEN**

## 1. Result

The authoritative graph is exactly the intended post-Round-173 graph. Its
hash equals the expected hash, and graph validation returns zero issues.
Relative to the independently reconstructed Round-172 starting graph, the
applied delta is exactly:

1. one created `proved_internal` obstruction,
   `M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction`;
2. two and only two changed pre-existing obligations,
   `M9-M2-top-endpoint-density-discrepancy-energy` and
   `M9-M2-top-endpoint-signed-cone`; and
3. no removed obligation, no rejected-claim change, no pre-existing status
   change, and no theorem or exponent mutation.

The post-application graph has 377 obligations and 1,389 rejected claims.
The reconstructed starting graph has 376 obligations and the same 1,389
rejected claims.

## 2. Exact applied statement and owner records

The created node has the exact required state fields:

- `type: obstruction`;
- `track: M9_analytic`;
- `status: proved_internal`;
- dependencies exactly on the accepted Round-164 residual transport,
  Round-165 parity/gcd/scale reduction, and Round-172 maximal-Fejer
  positive-transform obstruction;
- `implies: []`;
- `blockers: []`;
- `owner: Codex conductor`; and
- `last_updated_round: 173`.

Its statement retains the full literal residual coefficient class, exact
even-gap tangent domain, target-safe bandpass commutator, adjacent-sum
self-return, once-only short correction, coefficient-uniform positive
capacity boundary, nonliteral phase-adapted control, literal no-pair support
warning, and narrow method scope. It expressly keeps K26 open.

Each of the two endpoint owners contains the new obstruction exactly once as
a dependency, contains all six prescribed Round-173 paths exactly once under
`evidence.inconclusive`, contains none of those paths under positive or
negative evidence, remains `open`, and has the exact new next action from the
accepted patch. Both owner records and the created node share the applied
timestamp `2026-08-26T23:36:23`.

## 3. Exact reverse derivation and cycle audit

I reconstructed the starting graph in memory by reversing only the declared
Round-173 operations:

1. remove the created obstruction;
2. remove that dependency from the two owners;
3. remove exactly the six added inconclusive evidence paths from each owner;
4. restore the two exact Round-172 `next_action` values from the accepted
   Round-172 State Patch; and
5. restore their Round-172 update metadata, using the common accepted
   Round-172 timestamp carried by the Round-172 obstruction.

Canonical serialization of that inverse has SHA-256

`70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`,

exactly the certified Round-173 starting hash. The inverse graph also
validates with zero issues. Structured comparison then shows that the only
changed keys on either old owner are `dependencies`, `evidence`,
`next_action`, `last_updated_round`, and `last_updated_at`, exactly as the
patch application requires.

With dependency edges oriented prerequisite to dependent, the reconstructed
starting graph and authoritative post-application graph each have the same
three nontrivial strongly connected components. After adding implication
edges in source-to-consequence orientation, each has the same four nontrivial
components. Membership is identical, and the new Round-173 obstruction is in
no cycle.

## 4. First doubtful or unproved step

There is no unresolved application, reference, owner-direction, cycle,
status, or theorem-scope seam. The first unproved mathematical step remains
the complete literal signed K26 stopped-chain shifted-convolution estimate
before every modulus, with all selectors, masks, parity branches, profiles,
endpoints, phases, one outer real part, and cross-link cancellation retained.

The applied obstruction neither proves nor disproves K26. The target-safe
commutator is not a standalone owner because its exact complement is the open
remainder, equivalent to K26 modulo already paid terms.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| authoritative file identity | **GREEN.** Observed SHA-256 exactly matches `04090ef6...0d962a`. |
| post-application graph validation | **GREEN.** Zero issues. |
| exact reverse hash | **GREEN.** Canonical inverse is exactly `70592c10...c0d962b7f`. |
| reverse graph validation | **GREEN.** Zero issues. |
| obligation delta | **GREEN.** One create, two changed old records, no removal. |
| rejected ledger | **GREEN/no change.** Exactly 1,389 records before and after. |
| pre-existing statuses | **GREEN/no change.** No status changes. |
| created-node dependencies | **GREEN.** Exactly the three accepted prerequisites; all resolve. |
| implication and blocker fields | **GREEN.** Both empty. |
| owner evidence direction | **GREEN.** Six inconclusive additions per open owner; no positive/negative promotion. |
| evidence path resolution | **GREEN.** Thirty patch references reduce to 18 distinct paths; all exist. |
| evidence duplication | **GREEN.** No prescribed path is duplicated within either owner bucket. |
| dependency SCCs | **GREEN.** Same three components before and after; new node acyclic. |
| combined logical SCCs | **GREEN.** Same four components before and after. |
| theorem sentinels | **GREEN/no change.** `GC-target`, both bridges, `M9`, `M9-M1`, `M9-M2`, and endpoint uniformity are structurally identical. |
| exponent sentinels | **GREEN/no change.** Internal (1/3), external (0.3144831759740614\ldots), and target (1/4) are unchanged. |
| unintended mutation search | **GREEN.** No structured delta exists outside the one create and two updates. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This audit used:

1. authoritative `state/proof_obligations.yml`;
2. the accepted Round-173 `state_patch.json`;
3. the durable Round-173 tangent-Fejer self-return kernel;
4. the Round-173 adjudication and prior State-Patch scope/cycle review;
5. the accepted Round-172 State Patch for the exact pre-Round-173 owner
   actions;
6. the certified Round-172 post-application graph facts and starting hash;
   and
7. the repository graph validator and canonical serializer for read-only
   in-memory checks.

All eighteen distinct evidence artifacts named by the patch resolve. The
initial blind report is accompanied by its repaired packet verification and
is evidence for the exact self-return obstruction, not for the superseded
broad coefficient hypotheses.

## 7. Recommended state effect

Retain the authoritative graph without repair. The applied Round-173 node is
properly scoped as a proved internal method obstruction; the two endpoint
owners correctly receive only inconclusive route evidence and remain open.
No reverse dependency, standalone commutator sector, implication, blocker,
rejected claim, parent promotion, bridge change, theorem change, or exponent
change is present.

K26, the complete residual scalar, every other hard-TOP channel, hard TOP,
BAL, UNBAL, M9--M2, both M1 routes, endpoint uniformity, M9, both bridges,
the internal one-third result, the accepted external benchmark, and the
quarter target remain exactly at their pre-Round-173 statuses.

**Final verdict: GREEN.**
