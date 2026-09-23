# Conductor Round 189 candidate TeX byte repair

## Result

Before any seam review completed, the conductor detected that the first
generated candidate and reconciliation had lost TeX delimiter
backslashes and had interpreted a carriage-return escape inside
\({\rm odd}\). All three reviews were interrupted before returning a
verdict. Neither file had been used in a durable kernel, State Patch,
proof graph, synthesis, or proof draft.

The two draft files were replaced in full by strict UTF-8/LF versions.
The repaired formal candidate is

rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/candidates/formalized_hard_m1_t1_high_h_dual_frequency_projective_reduction.md

at SHA-256

03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b.

The repaired reconciliation is

rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_report_reconciliation.md

at SHA-256

f7486ccf02a7fb43e1bde82e94e7da410a1d691fc8b629f2b877bc40ca6a902e.

The superseded unreviewed hashes were
92ddfb87450ef5bca0a0c9e30a04606abf90591ea8287664a2058b16656d0ebd
and
9d811b32c939a71a4c2f3469656ea9196795a9ef39432d158330875635fae295.
They are not proof evidence.

After the repaired candidate received its first review suite, one
review requested only an explicit fixed-\(a\), dyadic-\(J\) quantifier
before the unproved sufficient relation (189.K18). That single
clarification produced the final candidate SHA-256
123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28.
Three focused reviews independently reversed exactly that insertion to
the prior 03d5... bytes and found no other drift.

## Controls

- Both repaired files decode as strict UTF-8.
- Neither repaired file contains C0 control bytes other than line feed.
- The candidate visibly retains \(\(...\)\), \(\[...\]\), and all
  mathematical command backslashes.
- Each restarted reviewer was instructed to discard the interrupted
  draft and audit only the repaired candidate at its frozen hash.
- state/proof_obligations.yml remained at the Round-189 starting hash
  throughout the repair.

## State effect

No graph effect. This is an artifact-hygiene repair and audit trail,
not mathematical evidence.
