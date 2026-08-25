# Round 163 terminal State Patch scope audit

Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
Role: independent terminal patch-scope reviewer
Generated: 2026-08-25T23:32:44+08:00
Validator context supplied by conductor: dry patch validator and campaign validator both pass

## 1. Result

**GREEN: apply the State Patch as written.** The patch is based on the exact current graph hash, creates one fresh proved-internal strict-sector node, updates only the two open hard-TOP parents, introduces no new dependency cycle, and quarantines every density, complement, full-\(t=1\), downstream, and exponent overclaim.

The exact operation ledger is:

| Patch array | Entries | Effect |
|---|---:|---|
| create | \(1\) | one proof-obligation node |
| update | \(2\) | the two open hard-TOP parents |
| correct_rejected | \(0\) | no rejected claim is rewritten |
| reject | \(16\) | sixteen fresh scoped overclaims |
| no_change | \(19\) | nineteen explicit quarantine declarations |

Thus the patch has \(19\) mutating graph/ledger entries—one creation, two updates, and sixteen rejection insertions—and \(19\) declarative no-change entries, for \(38\) listed operation entries. The separate round-assessment object contains four scores and one reason and creates no graph edge.

The current graph contains \(367\) proof obligations and \(1227\) rejected claims. After application it will contain \(368\) obligations and \(1243\) rejected claims.

## 2. Exact statement and hypotheses

The current SHA-256 of state/proof_obligations.yml is

\[
\texttt{700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358},
\]

exactly the starting hash in state/active_campaign.yml. Round 163 permits the terminal label strict_t1_prime_toggle_sector, and the patch uses precisely that scope.

The fresh node is

\[
\texttt{M9-M2-hard-top-t1-close-opposite-prime-exchange-sector}.
\]

It has type lemma, track M9_analytic, status proved_internal, no implication edge, and no blocker. Its exact claim is only the \(O_\kappa(L^{3/2})\) bound for the complete canonical close-opposite-prime XOR incidence subsum. Its statement expressly excludes:

- eligible-pair density, per-block nonemptiness, positive proportion, or polynomial coverage;
- no-pair products and neither-prime or both-prime incidences;
- the full \(t=1\) scalar and remaining few-point channels;
- either hard-TOP parent, either smooth M2 packet, M9-M2, M9, the bridge, the quarter target, or either global exponent.

Its three dependencies are:

1. M9-M2-hard-top-t1-character-poisson-product-collar-obstruction;
2. M9-M2-top-endpoint-actual-symbol-variation;
3. H4-Phi-regularity.

All three exist in the starting graph and have status proved_internal. They supply, respectively, the literal squarefree \(t=1\) coefficient and conventions, the fixed actual-symbol profile interface, and bounded \(C^1\) regularity of \(\Phi\).

The only updated nodes are M9-M2-top-endpoint-signed-cone and M9-M2-top-endpoint-density-discrepancy-energy. Both are open before the patch and remain open. Each receives the new node as one dependency, nine Round-163 artifacts as inconclusive evidence, and a residual-focused next action. Neither statement, status, blocker list, nor implication list is changed.

## 3. Proof or derivation

### Operation and identifier audit

All five operation arrays have unique IDs internally. The new obligation ID is absent from the \(367\) existing obligation IDs. Both update targets and all nineteen no-change targets exist. All sixteen rejection IDs are distinct and collide with neither an existing obligation nor any of the \(1227\) existing rejected-claim IDs. No correction operation is needed.

Each parent update adds exactly:

\[
1\ \text{dependency}
 +9\ \text{inconclusive evidence references}
 +1\ \text{replacement next action}.
\]

The added dependency and evidence references were not already present in either parent, so application creates no duplicate list entry.

### Dependency and evidence audit

The new node has three valid proved-internal antecedents, nine positive evidence files, zero negative files, and one inconclusive file. The inconclusive file is the original statement-only blind report; this classification is exact because that report lacked the accepted profile interface. The post-unmask blind review, profile/boundary/power review, downstream scope review, kernel, candidate, two substantive reports, conductor control, and adjudication are positive evidence for the strict child theorem.

Across the new node and both parent updates, the patch names \(28\) evidence references, representing \(10\) unique paths. Every path exists. The two parent lists correctly classify all nine additions as inconclusive: those artifacts prove or validate the child sector but do not prove either larger parent.

The accepted kernel and conductor adjudication agree exactly on the canonical XOR set, sign reversal, multiplicity one, even-\(N\) parity, common-cell \(L^{-1/2}\) difference, \(O(L^{3/2}+L)\) hard collars, absence of density, and open residual. All three seam reviews are green on their assigned interfaces.

### Cycle audit

In dependency orientation, the patch adds

\[
\text{each open parent}\longrightarrow\text{new sector}
\longrightarrow\text{three proved antecedents}.
\]

Before the patch, none of the three antecedents has a dependency path to either updated parent. In forward theorem-flow orientation, neither parent has a path back to any antecedent. Therefore no added edge closes a directed cycle. An independent strongly connected component check leaves the new node in a singleton component in both dependency-only and dependency-plus-implies orientations; the patch creates no new cyclic component.

The child has \(\mathrm{implies}=[]\). Hence adding it as a parent dependency cannot be mistaken mechanically for proof of a parent or downstream theorem.

### Scope and quarantine audit

The sixteen rejections partition correctly:

- two exclude density/nonemptiness and a full-\(t=1\) conclusion;
- ten quarantine one-prime toggles, partner rules, perfect matching, cycles/averages, odd and even complements, full-divisor completion, logarithmic sparsity, and diagnostic counts;
- four exclude remaining hard TOP, smooth M2 transfer, M9/quarter-target transfer, and exponent improvement.

The nineteen no-change entries preserve eight local antecedent or previously accepted hard-TOP nodes and eleven downstream objects: physical assembly, BAL, UNBAL, M9-M2, M9-M1, endpoint uniformity, M9, Conditional-bridge, the internal one-third theorem, the external Li–Yang benchmark, and GC-target.

This is the correct graph direction. The new result may be subtracted only from the two larger open parents. It supplies no blocker removal and no implication to them. The exact residual

\[
\mathcal S_{L,1}^{\rm rem}
=\mathcal S_{L,1}-\mathcal S_{L,1}^{\rm cp}
\]

remains the next \(t=1\) obligation, followed by the other few-point channels.

## 4. First doubtful or unproved step

No invalid patch operation was found. The first unproved mathematical step is the bound for \(\mathcal S_{L,1}^{\rm rem}\), consisting of all no-pair products and all neither-prime and both-prime incidences. Neither density of the selector nor a raw incidence count proves that weighted, arbitrary-real-centre scalar bound.

Even a future residual \(t=1\) estimate would not close hard TOP: the \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels and near collars would remain. The first invalid graph step would therefore be to interpret the new dependency as an implication, remove a parent blocker, or propagate the sector to smooth M2, M9-M2, M9, the bridge, GC-target, or either exponent. The patch expressly does none of these.

The hash precondition is presently exact. If the authoritative graph changes before application, the patch must be dry-validated again against the new hash.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Starting graph identity | PASS: current graph hash equals the Round-163 starting hash exactly. |
| Exact operation counts | PASS: \(1/2/0/16/19\) for create/update/correct/reject/no-change. |
| Fresh and unique IDs | PASS: one fresh node, sixteen fresh rejection IDs, no duplicate operation IDs. |
| Target existence | PASS: both update targets and all nineteen no-change targets exist. |
| Dependency validity | PASS: all three child dependencies exist and are proved_internal. |
| Evidence validity | PASS: \(28\) references, \(10\) unique paths, zero missing; child and parent classifications match the adjudication. |
| Duplicate additions | PASS: neither parent already contains the added dependency or any added inconclusive evidence path. |
| Cycle safety | PASS: no antecedent-to-parent return path; the new node remains a singleton strongly connected component. |
| Density and complement quarantine | PASS: excluded in the node statement, next action, and explicit rejections. |
| Parent scope | PASS: two open parents receive dependency plus inconclusive evidence only; statements, statuses, blockers, and implications remain unchanged. |
| Downstream quarantine | PASS: nineteen no-change entries and four downstream rejections prevent any global consequence. |
| Validator agreement | PASS: the independent audit agrees with the supplied Patch OK and campaign-validator pass. |

## 6. Dependencies and exact artifacts used

- protocol.md.
- state/proof_obligations.yml, parsed in full at the stated SHA-256.
- state/active_campaign.yml.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/state_patch.json.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/conductor_round163_adjudication.md.
- proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/blind_post_unmask_close_pair_sector_review.md.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/profile_boundary_power_seam_review.md.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/downstream_graph_scope_review.md.

Patch-referenced evidence paths not listed above were checked for existence only; their contents were not imported into this audit. No state file, patch, kernel, adjudication, or prior review was edited.

## 7. Recommended state effect

**Apply the patch unchanged.** Create exactly the one proved-internal close-opposite-prime XOR sector node; add it only as a dependency and inconclusive evidence source to the two open hard-TOP parents; append the sixteen scoped rejections; preserve all nineteen no-change declarations; and close Round 163 only under strict_t1_prime_toggle_sector.

Do not create a second graph node for the general toggle/matching/complement route evidence. Do not infer selector density, complementary-incidence control, the full \(t=1\) target, a hard-TOP parent, smooth M2, M9-M2, M9, a bridge, the quarter theorem, or an exponent change. The next mathematical action is the literal residual \(\mathcal S_{L,1}^{\rm rem}\), followed by the remaining few-point channels.
