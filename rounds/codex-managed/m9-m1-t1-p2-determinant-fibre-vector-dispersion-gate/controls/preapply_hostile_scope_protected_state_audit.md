# Round-195 preapplication hostile scope/protected-state audit

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Verdict: **PASS**
- State Patch SHA-256: `8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e`
- Starting graph SHA-256: `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`
- Exact operation scope (`create/update/correct_rejected/reject/no_change`): **1/1/0/23/27**
- Shared-state mutation during this audit: none

## 1. Result

**PASS.** The repaired current patch validates against the live graph and is
scope-exact. Its one new proved-internal node records only two absolute-capacity
subsectors of the physical \(P_2\) region and the exact strict packet remainder.
It does not claim complete \(P_2\), complete original \(t=1\), the hard-\(M_1\)
owner, any parent or bridge, the target theorem, or an exponent improvement.

An in-memory canonical application produced exactly one created obligation, one
updated obligation, no corrected rejected claim, 23 new rejected shadow claims,
and 27 no-change acknowledgements. Graph validation after that application
returned no issue. The hard small-\(t\) owner remains `open`; no protected
analytic field of any pre-existing obligation changes directly or indirectly.

The repaired bytes also pass the notation check: every new occurrence uses the
required JSON-escaped `\\mathfrak m`; no unescaped substitute remains.

## 2. Exact statement and hypotheses

The created node is
`M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`. It depends only on
the accepted Round-193 node
`M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`, has status
`proved_internal`, and has empty `implies` and `blockers` lists. It fixes the
accepted Round-192 physical core, both orientations and signs, both \(T\)
branches, all literal endpoint/event data, the physical-mask commutator, zero
extensions, and one outer real part. With

\[
 P_2=\mathbf 1_{\{|d-gm|\le D_L\}}
     \mathbf 1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil,
\]

the node asserts target-safe fixed-packet and outer bounds only on

\[
 \mathcal S_1=P_2\mathbf 1_{\{\kappa\ge D_L\}},
\]

and

\[
 \mathcal S_2=P_2\mathbf 1_{\{1\le\kappa<D_L\}}
   \mathbf 1_{\{\min(Y,D_L)\le H_B\mathfrak m\kappa\}}.
\]

It records, without promoting, the exact residual packet region

\[
 P_{\rm rem}=P_2\mathbf 1_{\{1\le\kappa<D_L\}}
   \mathbf 1_{\{\min(Y,D_L)>H_B\mathfrak m\kappa\}}.
\]

The statement retains the proved large-\(\kappa\) count
\(\sum_{\kappa\ge D_L}D_L(1+L/\kappa)^2\ll L^2\), the small-\(\kappa\)
capacity \(u\{\kappa+\min(Y,D_L)\}\), the carry-dependent plus-mode ratio,
the unit minus ratio, exact same-site event recombination, and the limitation of
squarefree-root multiplicity. Its terminal sentence explicitly quarantines
complete \(P_2\), \(P_1\), complete original \(t=1\), all \(t\ge2\) ranges,
the owner, parents, endpoint theorem, bridges, target, and exponent.

The sole existing-node update is to
`M9-M1-hard-top-high-radical-small-t-residual-estimate`: add the new node as a
dependency, add the 20 Round-195 evidence paths as inconclusive evidence, and
replace `next_action` by the exact two-sector/open-remainder handoff. Automatic
round/time metadata is the only other change. No status promotion is requested.

## 3. Proof or derivation

### 3.1 Exact application footprint

The official validator returned `Patch OK`. Independent in-memory application
and deep comparison gave:

- changed top-level graph keys: only `proof_obligations` and
  `rejected_claims`;
- created obligations: exactly the new capacity-sector node;
- removed obligations: none;
- changed pre-existing obligations: exactly the hard small-\(t\) owner;
- owner status: `open` before and `open` after;
- owner changed keys: only `dependencies`, `evidence`, `next_action`,
  `last_updated_round`, and `last_updated_at`;
- owner protected-field differences across `id`, `type`, `track`, `title`,
  `status`, `statement_tex`, `implies`, `blockers`, `owner`, and
  `required_output`: none;
- no-change obligation differences: none;
- rejected-claim count: \(1732\to1755\), exactly the 23 requested new records;
- rejection-ID collision with either a live obligation or a prior rejected
  claim: none.

Because the new node has `implies: []`, its creation cannot promote a parent.
The only new dependency arrows are the new node to the accepted Round-193 node
and the still-open owner to the new node. The 23 `reject` operations append
shadow-claim records; none targets an obligation, so no analytic status is
changed to `rejected`. Thus there is no indirect protected-state mutation.

### 3.2 Two-sector and remainder calibration

The node, kernel, adjudication, and synthesis agree on the same partition
\(\mathcal S_1\sqcup\mathcal S_2\sqcup P_{\rm rem}\) inside physical \(P_2\).
The small-\(\kappa\) inequality is described as a packet selector, never as a
replacement physical mask. The node also says that \(P_2\) is applied before
Fourier expansion or height differencing and that the transported commutator,
birth/death terms, and zero extensions are recomputed. This prevents an
operatorial promotion from a post-expansion scalar deletion.

### 3.3 All 27 no-change reasons

Every no-change entry was checked against the live graph and the Round-195
artifacts.

- Entries 1--10 are the accepted Round-187--193 reduction/sector chain. Their
  statements and statuses are unchanged and are used only as dependencies.
- Entries 11--12 remain the open hard original-\(t\) endpoint owner and open
  smooth direct-\(M_1\) parent. Entry 13 remains a conditional
  `proved_internal` assembly whose two analytic parents are not completed.
- Entries 14--21 (GAR, \(M9\)-\(M1\), all three \(M9\)-\(M2\) components and
  parent, endpoint uniformity, and \(M9\)) retain their live open statuses and
  unresolved dependencies.
- Entries 22--23 remain derived-under-assumptions bridge claims with their live
  blockers. Entries 24--27 retain, respectively, the internal one-third result,
  the external Li--Yang benchmark, the open quarter target, and the elementary
  divisor bound.

The in-memory deep-equality check independently confirmed that all 27 objects
are byte-for-byte equal as parsed graph objects before and after application.

### 3.4 All 23 rejection reasons

The rejection list is calibrated to the proved boundary. Entries 1--3 and
20--23 reject completion, parent/bridge/theorem, and exponent overclaims;
entry 4 rejects converting capacity into literal lower mass; entries 5--8 reject
the false fixed-plus ratio, single-mode parity transport, channel orthogonality,
and separated-orientation norms; entries 9--13 reject the squareful blind
family, its restored-target shadow, root-count/Gram promotion, determinant-only
multiplicity, and a hidden \(q/J\) loss; entries 14--19 reject retyping the packet
condition as a physical mask, post-expansion masking, dropping the commutator or
\(T=0\), a long within-row fibre, and a hidden height factor. Each reason is
supported by the kernel/adjudication/synthesis boundary and none rejects a
stronger true statement.

### 3.5 Evidence and reversibility scope

The mirrored created-node/owner evidence lists contain 40 entries representing
20 unique paths; all 20 exist. The judge path exists. The reversibility payload
correctly records that the created node and 23 shadow rejections were absent,
that the added dependency was absent, the exact prior owner `next_action`, and
the prior metadata (`last_updated_round: 194`, `last_updated_at:
2026-08-30T02:58:26`). Reject IDs and no-change IDs are separately unique.

## 4. First doubtful or unproved step

There is no failed State Patch step at the current repaired hash. The first
mathematical step deliberately left unproved is the strict region

\[
 \kappa<D_L,
 \qquad \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

The exact first obstruction is the coefficient-sensitive cross-row
\(++,+-,-+,--\) Gram after same-site event recombination. Within-row determinant
multiplicity, the anchor character, arbitrary bounded arrays, separate
orientation norms, or squarefree root multiplicity do not control the actual
endpoint products and square-root phases. The patch states this as the next
research seam and does not convert it into a proof or a literal-mass claim.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Current patch hash equals the repaired assigned hash | PASS: `8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e` |
| Starting hash equals the live graph | PASS: `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89` |
| Official dry validation at round 195 with the adjudication judge reference | PASS: `Patch OK` |
| Exact operation scope | PASS: `1/1/0/23/27` |
| Post-apply in-memory graph validation | PASS: no issues |
| Owner remains open and protected analytic fields are invariant | PASS |
| Only the owner changes among pre-existing obligations | PASS |
| All 27 no-change objects are deeply equal | PASS |
| All 23 rejections are new shadow IDs, with no live-node collision | PASS |
| New node has no implication edge and no blocker mutation | PASS |
| Evidence paths and judge reference exist | PASS: 20/20 unique evidence paths |
| Repaired `\\mathfrak m` encoding with no unescaped substitute | PASS |
| Shared-state mutation during audit | PASS: none |

## 6. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/state_patch.json` — SHA-256 `8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e`.
- `state/proof_obligations.yml` — SHA-256 `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.
- `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` — SHA-256 `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_adjudication.md` — SHA-256 `fc6422ac07a165b3e8c9ba0fbbe79dc3aa77f2af74a1823b79f8d58665b198b4`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/synthesis.md` — SHA-256 `fdcf6ebed7455745034caaa7a30453ed9b84ff4c48440d61b720679d4d06e168`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md` — SHA-256 `81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72`.
- `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_report_reconciliation.md` — SHA-256 `3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436`.
- `math_collab/proof_obligations.py` — SHA-256 `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437`.
- `math_collab/validate_state_patch.py` — SHA-256 `cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8`.

## 7. Recommended state effect

**Promote the patch to the ordinary independent reverse/replay and application
controls.** At the current repaired hash, apply exactly the requested
`1/1/0/23/27` scope. Create only the two-sector capacity lemma, keep the hard
small-\(t\) owner open, append only the 23 calibrated shadow rejections, and
leave all 27 named obligations unchanged. Do not promote complete \(P_2\),
complete original \(t=1\), any owner or parent, either bridge, the target
theorem, or any exponent.
