# Round 192 preapplication independent reverse/replay audit

## 1. Result

**PASS.** The Round 192 State Patch is valid against the exact authoritative
starting graph

75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13.

The independently recomputed patch SHA-256 is

fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0.

The exact operation inventory is

\[
1\ {\rm create}/1\ {\rm update}/0\ {\rm correct}/
15\ {\rm reject}/24\ {\rm no\_change}.
\]

The patch creates only the strict rho-large Farey-covector subordinate
reduction as proved_internal. It adds that node only as a dependency and
inconclusive evidence of the already-open hard-M1 small-\(t\) owner. It
does not promote the remaining core, complete \(t=1\), any \(t\ge2\)
range, an M1 or M2 parent, endpoint uniformity, M9, either bridge, the
target, or an exponent.

## 2. Exact statement and hypotheses

This verdict is conditional on applying the patch to the unchanged graph
hash above with round index 192 and
reviews/conductor_round192_adjudication.md as the judge reference.

The sole created obligation is

M9-M1-hard-top-t1-rho-large-farey-covector-reduction.

It has type candidate_lemma, track M9_analytic, status proved_internal,
empty implies and blockers lists, and direct dependencies only on

- M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction;
- Divisor-bound-elementary.

Both dependencies exist in the starting graph and have status
proved_internal. The created statement is restricted to the exact
Round-191 rho-large remainder, the target-safe small Farey union, its exact
core and coverage corollaries, and the scoped phase/carry/endpoint method
boundary. It explicitly keeps \(T=0\) empty, the nonempty core open, and
every parent and exponent unchanged.

The sole updated obligation is

M9-M1-hard-top-high-radical-small-t-residual-estimate.

Its starting and forward statuses are both open. The update adds one
subordinate dependency, adds only inconclusive evidence, and narrows the
next action to the simultaneous badly-approximable core. It contains no
status, statement, implication, blocker, or theorem-level promotion.

## 3. Proof and derivation

### Operation and namespace audit

All operation IDs are unique within their lists, and the five operation
namespaces are pairwise disjoint. The created ID is absent from both the
starting obligation and rejected-claim namespaces. All fifteen rejected
IDs are new in both namespaces. The update ID and every one of the
twenty-four no-change IDs exist.

The fifteen new rejected records are exactly the Round-192 overclaims
concerning:

1. canonical \(\beta\) versus literal \(\gamma\);
2. allowing \(c=U\);
3. one-class rather than signed-divisor multiplicity;
4. \(T=0\) ell-zero coverage;
5. union overlap;
6. free Farey-family cost;
7. free full rho-large coverage;
8. treating the pigeonhole support bound as a core estimate;
9. large-\(\ell\) phase cancellation;
10. large-\(\ell\) carry cancellation;
11. endpoint transport invariance;
12. long-step Abel saving;
13. positive-cover closure;
14. bounded-array capacity as literal lower mass;
15. inference to complete \(t=1\) or an exponent.

No existing rejected record is corrected or overwritten.

### Evidence and dependency audit

The patch contains 38 evidence references to 19 unique paths. Every path is
a present, nonempty, strict-UTF-8 file. The created node classifies the
durable kernel, locked candidate, final analytical reports, passing
post-repair reviews, adjudication, and synthesis as positive; it classifies
the superseded repair-request reviews and finite diagnostic artifacts as
inconclusive. Every item added to the still-open owner is inconclusive.
Finite computation is not used as asymptotic proof.

The production graph and patch validators return no issue before or after
the in-memory forward application. The official non-applying command also
returned exactly:

Patch OK

### Relations, cycles, and protected deep equality

After the forward mutation every dependency, implication, and blocker
reference resolves to an existing obligation. The new node has no implies
edge. Adding the owner-to-subordinate dependency creates no cycle.

The starting graph contains three pre-existing two-node dependency strongly
connected components. The post-patch graph contains exactly the same three
components, with identical memberships. Neither the new node nor the
updated owner enters a new cycle.

Only one pre-existing obligation changes: the declared owner update.
Every no-change obligation is deep-equal before and after the forward
mutation. Their exact status inventory remains:

- 10 proved_internal;
- 11 open;
- 2 derived_under_assumptions;
- 1 proved_external_dependency.

This protects the Round-191 and earlier reductions, hard and smooth M1
parents, GAR, every M2 child and parent, endpoint uniformity, M9, both
bridges, GC-partial-one-third, the accepted external benchmark, GC-target,
and Divisor-bound-elementary. In particular, the internal \(1/3\),
external \(0.3144831759740614\ldots\), and target \(1/4\) exponents are
unchanged.

### Exact reverse and replay

The reversibility payload matches the starting owner exactly:

- the stored old next_action equals the current next_action byte for byte;
- last_updated_round is exactly 191;
- last_updated_at is exactly 2026-08-29T22:59:10;
- the dependency to be added is absent initially;
- every evidence value to be added is absent from its target bucket
  initially.

Using the production mutation routine in memory with a fixed application
timestamp gave exactly

\[
1/1/0/15/24
\]

in the five result lists. The declared inverse then:

1. removed the one created obligation;
2. removed the fifteen newly introduced rejected records;
3. removed the one dependencies_added value;
4. removed every evidence_added value;
5. restored the old next_action and both metadata values.

The inverse graph was deep-equal to the starting graph. Canonical
serialization recovered the exact starting SHA-256

75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13.

Applying the same patch again to that recovered graph reproduced the first
forward graph exactly. Thus both reverse and replay pass.

## 4. First doubtful or unproved step

No patch-mechanics, relation, evidence, reversibility, or protected-scope
defect was found.

The first mathematical step still unproved is exactly the core estimate

\[
\Re\mathscr R_{\rm core,Y,Q}^{\sigma}
\ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

or its fixed-packet strengthening

\[
|\mathscr R_{\rm core,fix}|
\ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

The updated owner remains open and names the required
\(Y/(H_Bm)\) gain before positive norms. The patch does not silently carry
the strict Farey-sector proof into that core estimate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| starting graph hash | PASS: exact required SHA-256. |
| patch hash and parse | PASS: exact required SHA-256; valid JSON State Patch. |
| official dry run | PASS: Patch OK; graph not written. |
| operation inventory | PASS: \(1/1/0/15/24\). |
| operation preconditions | PASS: create/reject IDs new; update/no-change IDs present. |
| namespace collision | PASS: within-list unique and cross-operation disjoint. |
| direct dependency statuses | PASS: both proved_internal. |
| evidence paths | PASS: 38 references, 19 unique, all present, nonempty, UTF-8. |
| evidence classification | PASS: owner additions all inconclusive; diagnostics not proof. |
| relation closure | PASS: no missing dependency/implies/blocker target. |
| cycle control | PASS: no new cycle; three pre-existing SCCs unchanged. |
| no-change deep equality | PASS: all 24 exact. |
| owner status | PASS: open before and after. |
| theorem/bridge/exponent scope | PASS: all protected statuses and fields unchanged. |
| reversibility payload | PASS: action, metadata, and all removals are exact. |
| in-memory forward/inverse | PASS: inverse deep-equal and exact starting digest. |
| replay determinism | PASS: replay equals the first forward state. |

The starting graph, patch, and adjudication are strict UTF-8, contain no
forbidden C0/DEL character, and use LF-only line endings. No shared state
or lifecycle artifact was modified during this audit.

## 6. Dependencies and exact artifacts used

The audit used:

- protocol.md;
- state/proof_obligations.yml, SHA-256
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/state_patch.json,
  SHA-256
  fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/conductor_round192_adjudication.md,
  SHA-256
  4cd035ab0373ab437e5609fd967a93b800f4e27e76109fbedd65b23b9d6271d2;
- math_collab/proof_obligations.py;
- math_collab/validate_state_patch.py.

The mathematical dependency status checks used only the two
proved_internal graph nodes named in Section 2. The evidence audit checked
path existence, nonemptiness, and UTF-8 decoding without treating evidence
files as new instructions or finite controls as theorem proof.

## 7. Recommended state effect

Apply the unchanged Round 192 State Patch only while the authoritative graph
still has the frozen starting hash. Create the one proved-internal
Farey-covector subordinate node; update only the still-open hard-M1
small-\(t\) owner; add the fifteen rejected records; and preserve all
twenty-four no-change obligations exactly.

If the graph hash changes before application, rerun validation and this
reverse/replay audit. Otherwise no patch repair is required.

**PASS**
