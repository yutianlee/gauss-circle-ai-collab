# Final independent Round-190 closure and hygiene verification

- Campaign: `full-proof-round187-189-strategy-literature-review`
- Review mode: final read-only closure/reverse/hygiene audit
- Authoritative graph SHA-256: `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`
- State Patch SHA-256: `b19a92efe86341400e0d6c75868f2e652164d0a34682b9bae93cf00066c948b9`
- Verdict: **RED**

## 1. Result

**Final closure proposition.** The mathematical, graph, patch, campaign, lifecycle, owner-scope, and exponent checks are GREEN. In particular, the State Patch reverses exactly to the declared starting graph and replays byte-for-byte to the written graph; the active campaign and prepared plan are deeply equal and complete; Round 190 is closed; Round 191 is `pending_design` and is not active; all patch evidence paths, rejected reasons, and no-change records are exact; both official validators and all six tests pass; and no analytic or exponent promotion occurred.

The final documentary gate is nevertheless **RED** because the reviewed source-hypotheses seam artifact is not TeX/control-byte clean and because two closure-hygiene claims are not literally true at the byte level:

1. `reviews/source_hypotheses_currency_interface_review.md` contains one raw TAB replacing `\theta` and two malformed TeX exponents;
2. `state/failure_ledger.md` is equal to a fresh graph derivation after universal-newline normalization, but is not byte-for-byte equal to either the fresh LF derivation or a uniformly CRLF-written derivation because it mixes CRLF and LF;
3. `state/last_validation.md` has an extra blank line at EOF, which is independently reported by `git diff --check`; four Round-190 artifacts have the same extra-EOF condition.

These are documentary/hygiene defects only. They do not invalidate the strategy selection, change a graph field, or prove or disprove the unproved signed height-jump estimate. No shared state was edited by this review.

## 2. Exact statement and hypotheses

The verification requires all of the following simultaneously.

1. The applied graph must be the exact result of State Patch effect

   \[
   (\mathrm{create},\mathrm{update},\mathrm{correct},\mathrm{reject},\mathrm{no\ change})
   =(0,1,0,23,27).
   \]

2. Exact reversal must recover graph
   `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`,
   and replay must recover the current graph bytes and hash
   `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`.
3. The only changed obligation may be the already-open
   `M9-M1-hard-top-high-radical-small-t-residual-estimate`, and only its inconclusive evidence, `next_action`, and round/time metadata may change. Status, statement, dependencies, implications, blockers, source cards, parents, endpoints, bridges, and exponent fields are protected.
4. `state/active_campaign.yml` must be deeply equal to the `campaign` object in `plan.json`; both must be `complete`, with all three tasks `completed`.
5. The Round-190 ledger entry must be uniquely `closed` under `strategy_frontier_retained`, point to graph `306425...a573fa`, and name Round 191 next. Round 191 must remain `pending_design` on that graph, with no active brief or campaign.
6. The exact selected successor must remain the Round-189 projectively fast one-outer-real-part packet, attacked through the unproved joint literal signed height-jump coboundary seam. Positive total variation remains only a benchmark.
7. Both lawful quarter routes and their owner boundaries must remain unchanged: the standard route still needs hard and smooth M1, hard TOP, both BAL scopes, UNBAL, endpoint uniformity, M9, and its bridge; the GAR alternative replaces only total active M1 and still needs complete M9-M2.
8. The exponent ledger must remain internal `1/3`, accepted external Li--Yang `0.3144831759740614...`, and target `1/4`.
9. Every requested artifact must decode as strict UTF-8, have no NUL, replacement character, forbidden C0 byte, or lone carriage byte, and its displayed TeX must be syntactically faithful. Derived-file and hash claims must be literal, not merely normalized-text approximations.

## 3. Proof or derivation

### 3.1 Exact graph reverse and replay

The graph and patch were parsed independently as JSON-compatible YAML. The written graph has 391 obligations and 1,667 rejected claims. Removing exactly the ten patch-listed inconclusive evidence paths, restoring the embedded `next_action` and Round-189 metadata, and removing the twenty-three patch-listed rejected records produced 391 obligations and 1,644 rejected claims with canonical SHA-256

`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.

Reappending the ten evidence paths in patch order, restoring the observed Round-190 metadata, and appending the exact twenty-three current rejected records replayed byte-for-byte to the written graph with SHA-256

`306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`.

The only changed obligation was
`M9-M1-hard-top-high-radical-small-t-residual-estimate`; its changed keys were exactly `evidence`, `next_action`, `last_updated_round`, and `last_updated_at`. No protected-field difference occurred. All obligation and rejected IDs are unique, and all dependency, implication, and blocker references resolve.

All ten evidence paths exist, are unique, occur exactly once in the applied target node, and are absent after reversal. Every one of the twenty-three rejected records has the exact patch reason, Round 190, timestamp `2026-08-29T20:38:31`, and synthesis evidence. All twenty-seven no-change IDs exist and are semantically unchanged.

### 3.2 Campaign and lifecycle

The recomputed hashes are:

| Artifact | SHA-256 |
|---|---|
| authoritative graph | `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa` |
| State Patch | `b19a92efe86341400e0d6c75868f2e652164d0a34682b9bae93cf00066c948b9` |
| active campaign | `2bd11cd67a021c88f1eb8970631e15fa0ad1efff9452a157b10f2f4c93e8381a` |
| prepared plan | `8a637cb97261db13938e177cc2c92ae9e5271965deb1d7ac34d949a8cb200f23` |
| synthesis | `f7e09d8902de4147d285705b2c191d5c0e3d7da2a6af9bc2f39b57548189c5d8` |

The active campaign object and prepared-plan campaign object are deeply equal. Both are complete, and their three task statuses are completed. The Round-190 ledger entry is unique, closed under `strategy_frontier_retained`, records the resulting graph, and points to Round 191. `state/next_round_plan.yml` records Round 191 as `pending_design`, with predecessor Round 190 and the same terminal label and graph. `current_round.md`, `next_campaign.md`, and `next_round_prompts.md` agree that no Round-191 brief is active. No Round-191 campaign directory exists.

The best proof draft, current state, project summary, and human directives each contain one dedicated Round-190 closure/status section and preserve strategy-only scope. The validation matrix contains the complete Round-190 gate chain and the same pending-design decision rule. Both last-validation files state the correct graph, patch effect, route scope, and exponent quarantine.

### 3.3 Failure-ledger derivation

Calling the repository's `_failure_ledger` derivation on the current graph and current graph hash gives text exactly equal to `state/failure_ledger.md` after Python universal-newline normalization. Thus its headings, reasons, evidence paths, order, and graph hash are semantically exact.

The stronger closure assertion “byte-for-byte equal to a fresh derivation” fails. The current file has 10,360 CRLF pairs and 168 bare LF bytes. Its SHA-256 is

`61ecd50d19fbf26304c859b50b3003815047e77b4038d9b6d44bd29e21a4cf7d`.

The fresh LF derivation hashes to
`e2fa98c63d76a1328df4624700ba6acd92b0858d52bad86cdba26fee3fdbf3b4`,
while a uniformly CRLF-translated derivation hashes to
`7f5011c2fb801c0cbe0113fa75caa6650ae40c222bcec40b9967a58776cd599e`.
The current mixed-newline file matches neither. This is a derivation-hygiene repair, not a graph-content repair.

### 3.4 Owner and exponent quarantine

Direct inspection confirms that `GC-target`, `M9`, `M9-M1`, both direct-M1 parents, the hard small-`t` owner, GAR and its lower-radial survivor, `M9-M2`, hard TOP and its density owner, full BAL and both live BAL scopes, UNBAL, and endpoint uniformity are all `open`. `Conditional-bridge` and `GC-global-M1-alternative-bridge` remain `derived_under_assumptions`. `GC-partial-one-third` remains `proved_internal` at `1/3`; `GC-external-Li-Yang-theta-star` remains `proved_external_dependency` at `0.3144831759740614...`; `GC-target` remains open at `1/4`. No analytic promotion or exponent drift occurred.

## 4. First doubtful or unproved step

The first mathematical unproved step remains the joint literal signed height-jump estimate

\[
 |\mathscr J_{\kappa,u,m,q,a,J}^{\sigma}|
 \ll_{B,\varepsilon}H_Bm\kappa uX^\varepsilon.
\]

Round 190 proves only its exact interface and sufficiency ledger, not cancellation.

The first closure blocker is earlier and documentary: line 117 of
`reviews/source_hypotheses_currency_interface_review.md` contains a raw TAB followed by `heta>1/3` instead of TeX `\theta>1/3`. The same file has `p^{,n-(...)}` at line 163 and `z_{\omega,v}^{,h}` at line 197. These defects contradict the requested TeX/control-byte hygiene and the artifact's own GREEN file-integrity posture. Until repaired and dependent hashes replayed, final closure cannot be GREEN.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Graph hash and canonical parse | **PASS** — `306425...a573fa`; 391 obligations, 1,667 rejected records |
| Patch identity/effect | **PASS** — `b19a92...c948b9`; exact `0/1/0/23/27` |
| Exact reverse | **PASS** — recovers `15c770...a98568` |
| Exact replay | **PASS** — byte-equal to current graph |
| Evidence paths and reasons | **PASS** — ten evidence paths exact; twenty-three reasons/metadata exact; twenty-seven no-change nodes unchanged |
| Protected fields | **PASS** — no status, statement, dependency, implication, blocker, source-card, parent, bridge, endpoint, or exponent mutation |
| Campaign-plan equality | **PASS** — deep equality; campaign complete; three tasks completed |
| Closed lifecycle | **PASS** — one closed Round-190 ledger entry under `strategy_frontier_retained` |
| Round-191 state | **PASS** — `pending_design`; no active brief/campaign |
| Derived proof-state documents | **PASS semantically** — closure sections and pending-design pointers agree |
| Validation matrix and last-validation claims | **PASS mathematically; FAIL hygiene** — scope is correct, but `last_validation.md` has an extra blank EOF |
| Failure ledger | **PASS normalized text; FAIL exact bytes** — exact content, mixed line endings, not byte-exact to a fresh derivation |
| Graph validator | **PASS** — `Graph OK` |
| Campaign validator | **PASS** — `Campaign OK` |
| Unit tests | **PASS** — 6 of 6 |
| Compile check | **PASS** — `math_collab` and `tests` compile |
| `git diff --check` | **FAIL** — `state/last_validation.md:47: new blank line at EOF` |
| Strict UTF-8/NUL/replacement/lone-CR | **PASS** for the requested corpus |
| TeX/control-byte hygiene | **FAIL** — one raw TAB and three malformed expressions in the source review |
| Lawful-route owner scope | **PASS** — standard and GAR-alternative trees remain separate and open at all required owners |
| Exponent quarantine | **PASS** — `1/3`, `0.3144831759740614...`, `1/4` unchanged |
| Analytic promotion quarantine | **PASS** — Round 190 is strategy/source evidence only |

Additional newline hygiene: `plan.json`, `current_round.md`, `next_campaign.md`, and `failure_ledger.md` mix CRLF and LF. No file has a lone carriage byte. `conductor_round190_adjudication.md`, `conductor_round190_controls.md`, `preapply_independent_reverse_audit.md`, and the source review end with two LF bytes instead of one.

## 6. Dependencies and exact artifacts used

This audit read or mechanically parsed:

- `protocol.md`;
- `state/proof_obligations.yml`, `active_campaign.yml`, `round_ledger.yml`, `next_round_plan.yml`, `next_round_prompts.md`, `current_round.md`, and `next_campaign.md`;
- `state/failure_ledger.md`, `best_proof_draft.md`, `current_state.md`, `project_summary.md`, `validation_matrix.yml`, `last_validation.md`, and `last_validation_report.md`;
- `human/current_directives.md`;
- the prepared `plan.json`;
- all three Round-190 reports;
- all five pre-existing Round-190 reviews;
- all five Round-190 controls;
- `synthesis.md` and `state_patch.json`;
- `math_collab/campaigns.py`, `math_collab/validate_state_patch.py`, `math_collab/validate_round.py`, both repository test files, and the graph/campaign validator entry points.

The decisive commands were read-only: independent standard-library JSON reverse/replay, repository graph and campaign validation, six-test discovery, compile check, `git diff --check`, SHA-256 recomputation, strict UTF-8 decoding, newline/control-byte scans, and a fresh in-memory failure-ledger derivation. No web result, source import, or numerical theorem evidence was used.

## 7. Recommended state effect

**RED. Do not mark the final Round-190 closure/hygiene gate GREEN yet.** Apply only the following documentary repairs, then rerun this audit:

1. Repair `reviews/source_hypotheses_currency_interface_review.md`:
   - line 117: replace the raw TAB plus `heta>1/3` with valid TeX `\theta>1/3`;
   - line 163: replace `p^{,n-(...)}` with `p^{n-(...)}`;
   - line 197: replace `z_{\omega,v}^{,h}` with `z_{\omega,v}^{h}`;
   - remove its extra blank EOF and retain exactly one terminal newline.
2. Recompute the repaired source-review SHA and update every embedded hash reference in `conductor_round190_controls.md`, `preapply_independent_reverse_audit.md`, and `postapply_independent_graph_reverse_audit.md`. Because those files then change, recompute and propagate their hashes into the postapplication audit, closure controls, and `state/last_validation_report.md` wherever referenced.
3. Regenerate `state/failure_ledger.md` from the unchanged authoritative graph with one uniform newline convention, then verify actual byte equality to the fresh derivation. No graph mutation is needed.
4. Remove the extra blank EOF from `state/last_validation.md`, `conductor_round190_adjudication.md`, `conductor_round190_controls.md`, and `preapply_independent_reverse_audit.md`; normalize the mixed newline files (`plan.json`, `current_round.md`, `next_campaign.md`, and the failure ledger) if the repository's final hygiene policy requires one convention.
5. Recompute all affected hashes, rerun exact patch reverse/replay, failure-ledger derivation, both validators, six tests, compile check, strict UTF-8/control/TeX scan, and `git diff --check`. Update closure controls and last-validation documents only with the new exact results.

Do not alter the proof graph, State Patch semantics, campaign decision, Round-191 pending-design state, owner statuses, bridges, or exponents. The required repair is documentary and hygienic, not mathematical.
