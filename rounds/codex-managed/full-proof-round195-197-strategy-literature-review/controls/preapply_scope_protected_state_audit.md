# Round 198 independent pre-apply protected-scope audit

- Campaign: full-proof-round195-197-strategy-literature-review
- Round: 198
- Control: preapply_scope_protected_state_audit
- Starting graph SHA-256:
  8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69
- Verdict: GREEN for the declared strategy-only patch
- Execution: read-only simulation; shared state was not edited

## 1. Result

The Round-198 State Patch passes the independent protected-scope audit.
Its exact operation counts are

\[
(\mathrm{create},\mathrm{update},\mathrm{correct\_rejected},
 \mathrm{reject},\mathrm{no\_change})
=(0,1,0,23,30).
\]

The only proof obligation changed by a literal dry apply is

\[
\text{M9-M1-hard-top-high-radical-small-t-residual-estimate}.
\]

That node remains status \(open\).  The patch appends eleven
inconclusive evidence paths, replaces only its strategy next action, and
sets last_updated_round to \(198\).  It changes no statement, status,
dependency, blocker, implication, owner, or analytic result.

All 30 protected no-change IDs exist exactly once.  Their preimage and
simulated-postimage objects are deep-equal and byte-equal under the
repository's canonical per-object serialization.  The before/after
protected manifest SHA-256 is identically

\[
\texttt{E0E6C4D825018C382E14B012096FE99FE87FCFEC47569FDCFE5B28D0FF257C79}.
\]

All 23 proposed rejected-claim IDs are mutually unique, absent from the
1797 starting rejected claims, disjoint from all 396 proof-obligation
IDs, and have nonempty reasons.  All eleven evidence paths exist as
files, are unique, and are absent from the target node's starting
inconclusive bucket.

No analytic promotion occurs.  The graph topology and the exponent
records are quarantined.

## 2. Exact patch scope and protected objects

### 2.1 Sole update

The update object contains exactly four keys:

\[
\{\mathrm{id},\mathrm{evidence\_added},
  \mathrm{next\_action},\mathrm{last\_updated\_round}\}.
\]

Its evidence addition has only the inconclusive bucket.  The target
node's inconclusive-evidence count changes from \(275\) to \(286\).
The target's protected interface remains

- status: open;
- dependencies: the same 12 accepted hard-\(M1\) reductions/sectors;
- blockers: empty;
- implies:
  M9-M1-top-endpoint-signed-cone.

The patch creates no node, corrects no old rejected claim, adds no
dependency, and supplies no field capable of changing status, blockers,
implies, theorem statement, or exponent.

### 2.2 Thirty declared no-change IDs

All 30 IDs exist and retain the following status distribution and exact
objects.

| Status | Count | Protected IDs |
|---|---:|---|
| proved_internal | 14 | M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors; M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector; M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector; M9-M1-hard-top-t1-rho-large-farey-covector-reduction; M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction; M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction; M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction; M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction; M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction; M9-M1-hard-top-t1-comparable-factor-exchange-sector; M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector; M9-M1-physical-one-count-assembly; GC-partial-one-third; Divisor-bound-elementary |
| open | 13 | M9-M1-top-endpoint-signed-cone; M9-M1-direct-smooth-residual-blockwise-estimate; M9-M1-global-lower-radial-signed-estimate; M9-M1-global-angular-radial-estimate; M9-M1; M9-M2-top-endpoint-signed-cone; M9-M2-top-endpoint-density-discrepancy-energy; M9-M2-smooth-balanced-quarter-packet-estimate; M9-M2-smooth-unbalanced-three-quarter-estimate; M9-M2; M9-endpoint-uniformity; M9; GC-target |
| derived_under_assumptions | 2 | Conditional-bridge; GC-global-M1-alternative-bridge |
| proved_external_dependency | 1 | GC-external-Li-Yang-theta-star |

The dry apply also compared every proof obligation, not only these 30.
Exactly one of 396 obligation objects changes; the other 395 are
deep-equal.

### 2.3 Rejections and evidence

The simulated rejected-claim count is

\[
1797+23=1820,
\]

and all 1820 resulting rejected IDs are unique.  The new records reject
strategy, source-import, scope, norm-placement, and exponent overclaims;
they do not assert an analytic theorem.

The eleven evidence additions are all existing campaign reports, reviews,
controls, or the synthesis.  Their ordered path/hash/size manifest has
SHA-256

\[
\texttt{F4EF4E1438909E3D9EE1EF6040B3119B795AA2AF1EDEAC0F83FB9121805FF68D}.
\]

The files total 219423 bytes and contain no embedded low control byte.
Because none was already on the target node, unique append is
information-preserving and the declared inverse removal is unambiguous.

## 3. Proof or derivation

### 3.1 Independent simulated apply

The audit performed these read-only steps.

1. Decode the graph and patch as strict UTF-8 JSON while rejecting
   duplicate object keys.
2. Verify the raw graph SHA-256 against the patch's declared starting
   hash.
3. Deep-copy the graph.
4. Append the eleven inconclusive evidence values uniquely to the sole
   update target, replace its next action, and set last_updated_round to
   \(198\).
5. Append the 23 rejected records.
6. Compare every proof-obligation object, every protected projection
   \((\mathrm{status},\mathrm{dependencies},\mathrm{blockers},
   \mathrm{implies})\), and every declared no-change object.

The resulting diagnostics are:

| Test | Result |
|---|---|
| Starting raw graph hash equals patch declaration | PASS |
| Duplicate JSON keys in graph / patch | \(0/0\) |
| Obligation count before / after | \(396/396\) |
| Rejected count before / after | \(1797/1820\) |
| Changed obligation IDs | exactly the one declared update target |
| Changed status/dependency/blocker/implies projections | none |
| Missing or duplicated protected IDs | none |
| Protected per-object byte/deep mismatches | none |
| New rejected-ID collisions | none |
| Missing or pre-existing evidence additions | none |

For reproducibility, a deterministic dry postimage that applies only the
fields present in the patch and leaves the old timestamp in place has
SHA-256

\[
\texttt{6AC6380E20BA69BFB13A6FE271E6DF9E640033B6E5349AA6C6E896839D78E8C3}.
\]

An actual applier may replace last_updated_at with its application time,
so that diagnostic postimage hash is not prescribed as the future live
graph hash.

### 3.2 Exact reverse

The stored restore_next_action matches the starting target string
character for character.  The stored restore metadata exactly equals

\[
(\mathrm{last\_updated\_round},\mathrm{last\_updated\_at})
=(197,\text{2026-08-31T00:13:15}).
\]

Starting from the dry postimage, the audit removed exactly the eleven
added evidence paths and 23 new rejected records, restored the next
action and metadata, and obtained:

- full-object deep equality with the starting graph;
- exact canonical byte equality with the raw starting file; and
- rollback SHA-256
  8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69.

Thus the proposed mutation is reversible without touching any protected
node.

### 3.3 Status, topology, and exponent quarantine

No update or create operation contains a status, dependencies, blockers,
implies, statement, or exponent field.  The complete 396-node projection
onto status/dependencies/blockers/implies is identical before and after
the simulation.  With no edge addition or deletion, the patch cannot
introduce a new dependency cycle or hidden implication.

The complete objects for GC-partial-one-third,
GC-external-Li-Yang-theta-star, and GC-target are byte/deep-equal.  Hence
the internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) records are unchanged.
Both bridges remain derived_under_assumptions; M9-M1, M9-M2,
endpoint uniformity, M9, and GC-target remain open.

## 4. First doubtful or unproved step

The first remaining uncertainty is operational, not mathematical: this
audit did not run the real state applier.  The application-time
last_updated_at value is intentionally nondeterministic.  The simulated
postimage hash therefore cannot be required of the future live file.
The protected-object comparisons do not depend on that timestamp, and the
patch stores the exact old timestamp needed for reversal.

The per-object byte test uses the repository's canonical compact JSON
serialization.  A whole-file apply may move byte offsets by appending
evidence and reserializing the graph, but the 30 protected values remain
byte-identical as JSON objects and deep-identical as data.

No analytic claim is tested here.  The next-action text selects the
Round-199 complete three-piece theorem-or-no-go gate; it does not prove
that estimate.  Actual post-apply hash, lifecycle, reverse/replay, and
protected-scope checks remain required after application.

## 5. Required control tests and outcomes

### 5.1 Scope controls

| Control | Outcome |
|---|---|
| Exact operation counts | PASS: \(0/1/0/23/30\) |
| One obligation changes | PASS: only the hard high-radical small-\(t\) residual owner |
| Thirty no-change IDs exist | PASS: 30 distinct IDs, each found exactly once |
| Thirty no-change objects protected | PASS: byte/deep-equal; identical manifest hash before and after |
| Status quarantine | PASS: all 396 statuses unchanged |
| Dependency quarantine | PASS: no dependency added, removed, or reordered |
| Blocker/implies quarantine | PASS: all blockers and implication lists unchanged |
| Exponent quarantine | PASS: the three exponent-bearing records are exact no-change objects |
| Rejected-ID uniqueness | PASS: \(23/23\) new unique, no collision; all 1820 postimage IDs unique |
| Evidence provenance | PASS: \(11/11\) unique files exist and are fresh to the target bucket |
| Evidence polarity | PASS: additions are inconclusive only |
| Reversibility | PASS: inverse is deep- and canonical-byte-exact |
| Analytic promotion | PASS: none |
| Shared-state mutation during audit | PASS: none |

### 5.2 Hash and byte-hygiene controls

| Artifact | SHA-256 | Byte result |
|---|---|---|
| protocol.md | F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A | strict UTF-8; 135 structural CRLF pairs; no orphan CR, NUL, or other low control |
| state/proof_obligations.yml | 8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69 | strict UTF-8; no CR, NUL, or forbidden low control |
| state_patch.json | 70AABC822CF23A1FC3F70953BBD3455B9CC9E73E10983578773CCF1EECECC279 | strict UTF-8; no CR, NUL, or forbidden low control |
| conductor_round198_adjudication.md | 905EFB8375E684337D0A10E7ED2457FBD543CE699AF33B96649F1DF4AF9DD745 | strict UTF-8; clean |
| synthesis.md | AC05CF84483D619FE8153C7ABBDF7C1CDF06A50B50E7C423025E6D47E2490A6A | strict UTF-8; clean |
| dependency_power_selection_seam_review.md | 772B87331F6090A7BFCE641E9FA5FCD1CE36205935D30B31E85D5EE090A634A4 | strict UTF-8; clean |
| source_hypotheses_currency_interface_review.md | E63CBDBB80C0865BA113543416D1E21F37FE2FA6E5C4AEC5EAB166F9512C2ED8 | strict UTF-8; clean |
| blind_post_unmask_frontier_selection_review.md | 2E8EFB63D2E7D6FA595B8A549908D87B27111D2E5C6D2EFBF7352C77DFD68078 | strict UTF-8; clean |

All eleven evidence files also pass strict UTF-8 and embedded-control
checks.  The CR bytes in protocol.md are paired line terminators, not an
embedded control defect.

## 6. Dependencies and exact artifacts used

This audit read completely:

1. protocol.md;
2. state/proof_obligations.yml;
3. rounds/codex-managed/full-proof-round195-197-strategy-literature-review/state_patch.json;
4. rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/conductor_round198_adjudication.md;
5. rounds/codex-managed/full-proof-round195-197-strategy-literature-review/synthesis.md;
6. rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/dependency_power_selection_seam_review.md;
7. rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md;
8. rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/blind_post_unmask_frontier_selection_review.md.

The graph was parsed through all 396 obligations and 1797 rejected claims.
The eleven evidence paths named by the patch were checked directly for
existence, uniqueness, file type, hashability, UTF-8 validity, and
embedded-control hygiene.  No source theorem, web result, numerical
experiment, proof draft, validation matrix, active campaign, or shared
state writer was used.

## 7. Recommended state effect

**Recommended effect: approve this exact patch for the conductor's
controlled apply, subject to the remaining lifecycle controls.**

The application must preserve the audited scope:

- append only the eleven inconclusive evidence values;
- replace only the selected open owner's next action and update its
  Round-198 metadata;
- append only the 23 new rejected claims;
- leave all 30 declared no-change nodes, every other obligation, every
  status and graph edge, both bridges, the target, and all exponent
  records unchanged.

The patch remains strategy-only.  It does not launch Round 199, prove the
three-piece \(P_2\) estimate, promote a parent or endpoint theorem, close a
bridge, or improve a global exponent.  If the applied graph differs from
this scope, the conductor should reject or reverse it rather than repair
shared state inside this audit.
