# Round 200 launch validation

Campaign: m9-m1-t1-complete-source-coefficient-mask-analysis.
Generated: 2026-09-23. Role: conductor workflow/source control.

Round 199 is closed in the ledger and the current checkout is commit
7a4999a5df90bc2a9f6ea4f84fae3a4aa1b99c39, matching the strategy review.
The starting graph contains 396 obligations. Relevant complete-source
nodes K184 and K185 are proved_internal; the small-t owner, M1, M2, M9,
and GC-target remain open.

The on-disk graph SHA-256 is
2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5.
Normalizing CRLF to LF gives
3073235ad5677b9066f1336ec9d958b0e93b92d99cfa7ebea1d823146c799099,
the Round-199 recorded hash. No graph content discrepancy exists. Round
200 records the actual on-disk hash. The supplied strategy review and
accepted proof draft are separately fingerprinted in starting_state_hashes.json.

Commands: `python -m math_collab.campaigns prepare`, followed after launch
by `python -m math_collab.campaigns validate`. Both succeeded for the new
campaign. Preparation validates the full graph and all task paths, roles,
controls and statement-only context exclusions.

A first initialization guard detected the line-ending hash difference
before writing new workflow state. An accidental prepare of the old
manifest was immediately reversed for the files it regenerated; no
Round-199 report, plan or brief change remains. Initialization was then
rerun with the normalized-content guard and the raw-hash provenance.

Three isolated subagents were launched with no inherited conversation:
complete-source derivation, actual-symbol norm/power audit, and a
statement-only finite-operator rederivation. The blind task excludes the
claim graph, review memorandum and claimant derivations. No numerical
experiments or external theorem imports are planned.

The frozen objective and exit labels are in plan.json and the Round-200
strategy file. This is a workflow launch, with no proof-state promotion.
