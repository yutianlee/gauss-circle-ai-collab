# Round 195 final kernel/blind-evidence consistency review

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Role: final candidate-kernel, blind-evidence, sector, and transport audit
- Status: review evidence only; no kernel, candidate, report, reconciliation,
  graph, state, or synthesis edit

## 1. Result

**PASS. Promotion verdict: promote the final kernel through the
blind-evidence consistency gate.**

The final kernel

`proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`

has SHA-256

`4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.

Its embedded formal-candidate receipt is

`81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72`,

which exactly matches the current candidate. A direct file comparison
shows that the mathematical body is identical: the only differences are
the title/status metadata and the Section 7 heading and introductory
proof-state wording. The Section 7 state-effect list itself agrees.

The kernel qualifies the blind evidence correctly. It uses the blind report
only for the signed fibre algebra and the scoped method boundary after the
live post-unmask repairs. It expressly denies that the blind report proves
the positive estimate or literal lower mass. The squareful \(U=p^2\)
family is excluded on nonzero literal support and cannot enter either safe
sector as positive evidence.

The exact safe sectors are

\[
 P_{2,\ge D_L}
 \quad\text{and}\quad
 P_{2,<D_L}\cap\mathcal P_{\rm cap},
\]

with exact open complement

\[
 P_{2,<D_L}\cap\mathcal P_{\rm rem}.
\]

The repaired blind report, final candidate, final kernel, and reconciliation
are strict UTF-8 and have no surviving bare `qquad` or `tag{...}` formula
token. The bare strings occurring in the two reviews are quoted descriptions
of the repaired token class, not TeX defects.

The first blind post-unmask review remains correct on evidence
classification, but its earlier coarse \(P_{2,<D_L}\) open seam and partial
transport-location inventory are superseded by the current reconciliation
and the postrepair review. Neither supersession changes its rejection of
the squareful shadow.

## 2. Exact statement and hypotheses

For a fixed packet

\[
 p=(\kappa,u,\mathfrak m,q,a,J,Y,\sigma),
\]

the kernel defines

\[
 \mathcal P_{\rm cap}
 =\{p:\kappa<D_L,\ \min(Y,D_L)\le H_B\mathfrak m\kappa\},
\tag{2.1}
\]

\[
 \mathcal P_{\rm rem}
 =\{p:\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}.
\tag{2.2}
\]

Together with

\[
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}},
\tag{2.3}
\]

these give the exact disjoint safe/open packet partition. The positive
statements are

\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma
 (P_{2,\ge D}W)\right|
 \ll H_B\mathfrak m\kappa uX^\varepsilon,
\tag{2.4}
\]

and

\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma
 (P_{2,<D}W)\right|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon,
\tag{2.5}
\]

so (2.5) is target-safe exactly on \(\mathcal P_{\rm cap}\).

The blind fibre algebra retained by the kernel is, with positive far defect
\(\eta\),

\[
 2h=v\eta+U\delta-\kappa(U^2-v^2)\quad(+),
\tag{2.6+}
\]

\[
 2h=U\eta-v\delta+\kappa(U^2-v^2)\quad(-),
\tag{2.6-}
\]

and, in the minus chart,

\[
 \kappa v^2+\delta v+2h\equiv0\pmod U.
\tag{2.7}
\]

These formulas are used only under the live hypotheses omitted from the
isolated blind packet, including

\[
 U\mid u,\qquad u=gU,\qquad
 u\asymp v\asymp L/\kappa,\qquad
 Y<h\le2Y,\qquad L\ll X^{1/4},
\tag{2.8}
\]

plus every literal shell, hard-cone, squarefree, coprimality, residual,
endpoint, core, Farey, carry, event, commutator, and zero-extension
predicate. On nonzero literal support,

\[
 \kappa gU\ \text{is squarefree},
 \qquad U\ \text{is squarefree},
 \qquad(\kappa,U)=1.
\tag{2.9}
\]

## 3. Proof and derivation

### 3.1 Candidate-kernel identity

The final kernel records the current candidate hash exactly. A direct
candidate-versus-kernel diff has only two nonmathematical hunks:

1. the title and candidate/kernel status metadata, including the candidate
   hash receipt; and
2. the Section 7 heading plus one introductory sentence changing a proposed
   state effect into a kernel proof-state boundary.

Sections 1--6, equations (195.C1)--(195.C22), the safe/rem sector
definitions, and the four-item state-effect list are otherwise byte-identical.
In particular the current exact remaining seam
\(P_{2,<D_L}\cap\mathcal P_{\rm rem}\) is present in both.

### 3.2 Qualification of the blind algebra

The plus identity in (2.6+) is the rearranged divisor fibre

\[
 v(\kappa v+\eta)=2h-U\delta+\kappa U^2,
\]

and (2.6-) rearranges to (2.7). Thus the algebra imported from the blind
report is correct. The kernel does not import the blind interpretation of
the squareful example.

Indeed, by (2.9), for each prime \(\ell\mid U\), \(\kappa\) is invertible
modulo \(\ell\). The quadratic in (2.7) has at most two roots modulo
\(\ell\). Since \(U\) is squarefree, the Chinese remainder theorem gives

\[
 \#\{v\bmod U:(2.7)\}\le2^{\omega(U)}
 \ll_\varepsilon U^\varepsilon.
\tag{3.1}
\]

The blind example instead takes \(g=\kappa=1\) and \(U=p^2\), so its fixed
divisor \(\kappa gU=p^2\) violates literal squarefreeness and its endpoint
coefficient is zero. Its \(\sqrt U\) root count is therefore a squareful
algebraic shadow, exactly as the kernel states.

The remaining live failures are independent: the example takes \(u=1\)
instead of \(u=gU=p^2\), violates \(Y<h\), violates
\(L\ll X^{1/4}\), and never proves survival of the other literal masks.
After restoring only \(u=gU\), its \(O(\sqrt U)\) coherent size is below
the fixed target \(H_B\mathfrak m\kappa uX^\varepsilon\asymp U
H_B\mathfrak m\kappa X^\varepsilon\). Hence there is no blind quantitative
obstruction.

### 3.3 No leakage into positive evidence

The large-\(\kappa\) proof counts close and determinant variables
absolutely and obtains

\[
 \sum_{\kappa\ge D_L}D_L(1+L/\kappa)^2\ll L^2.
\tag{3.2}
\]

The small-\(\kappa\) proof combines the independent fixed-height and
all-height upper counts to obtain (2.5). Neither proof uses the blind
\(p^2\) family, its quadratic collisions, phase alignment, or any lower
bound. Literal restrictions only delete candidates; even an intermediate
overcount of a zero-weight squareful tuple could only enlarge an upper
bound and cannot become positive mass.

The root bound (3.1) appears later in the method-boundary discussion. The
kernel expressly says it supplies no missing power by itself. It also says
that the same-site all-ones \(2\times2\) and \(3\times3\) blocks recombine
to the original masked jump and that the coefficient-sensitive cross-row
Gram remains open. These statements prohibit interpreting either the blind
arbitrary-array block or the live self-return block as literal lower mass.

### 3.4 Exact safe/rem partition

Within \(\kappa<D_L\), the inequalities in (2.1)--(2.2) are exact
complements: equality belongs to \(\mathcal P_{\rm cap}\), while the strict
reverse belongs to \(\mathcal P_{\rm rem}\). Therefore

\[
 P_2=
 P_{2,\ge D_L}
 \ \dot\cup\
 (P_{2,<D_L}\cap\mathcal P_{\rm cap})
 \ \dot\cup\
 (P_{2,<D_L}\cap\mathcal P_{\rm rem}).
\tag{3.3}
\]

The first two pieces are exactly the proved safe union. The third is
exactly the kernel's declared open seam. No dyadic far-defect subfamily or
proper submask is promoted as complete \(P_2\).

### 3.5 Receipt and TeX audit

The repaired blind SHA in the current reconciliation is exactly

`29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df`.

Its ten restored separator backslashes are transport-only; deleting those
ten bytes reconstructs the frozen pre-repair SHA

`f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf`.

Strict scans of the final kernel, candidate, repaired blind report, and
reconciliation found valid UTF-8, no forbidden control or replacement
character, and no bare `qquad` or bare `tag{` token. All formula separators
in those artifacts are repaired.

The first post-unmask review identified the initial line groups but did not
enumerate the four later-found bare separators. The postrepair review
records the full ten-byte repair and supersedes that transport inventory.
This is a receipt refinement only; both reviews agree on the mathematical
evidence classification.

## 4. First doubtful or unproved step

No blind/kernel consistency gap remains. The first unproved mathematical
step is still the coefficient-sensitive joint \(++,+-,-+,--\) cross-row
Gram estimate on

\[
 P_{2,<D_L}\cap\mathcal P_{\rm rem},
\]

retaining the actual endpoint products, radical and anchor phases, Fejer
factors, residual masks, carries, births/deaths, physical-mask commutator,
cross-event terms, common zero extensions, both orientations and frequency
signs, and one outer real part.

This open seam does not invalidate the two safe sectors. Graph acceptance
and any `proved_internal` mutation remain conditional on the conductor's
mechanically valid State Patch.

## 5. Exact controls and outcomes

| Control | Outcome |
|---|---|
| `final_kernel_candidate_receipt` | **PASS.** Kernel receipt `81198f...6d72` equals the final candidate hash. |
| `candidate_kernel_mathematical_identity` | **PASS.** Only title/status and Section 7 proof-state wording differ; the theorem body and state-effect list agree. |
| `blind_algebra_qualified` | **PASS.** Only the correct signed fibre identities and scoped method boundary are retained under live hypotheses. |
| `literal_squarefree_nonzero_support` | **PASS.** The kernel conditions the root bound on squarefree \(\kappa gU\). |
| `squareful_false_shadow_quarantine` | **PASS.** \(U=p^2\) forces zero literal endpoint weight and is named a false shadow. |
| `no_blind_quantitative_obstruction` | **PASS.** Restored packet normalization places \(O(\sqrt U)\) below the target. |
| `no_unsupported_literal_mass` | **PASS.** Arbitrary arrays and same-site self-return are method controls, never lower bounds. |
| `absolute_positive_evidence_independence` | **PASS.** Safe-sector proofs are deletion-stable upper counts independent of blind cancellation. |
| `exact_safe_rem_partition` | **PASS.** Equation (3.3) gives the exact safe union and strict open complement. |
| `no_width_Farey_or_proper_submask_escape` | **PASS.** \(D_L\) and all strict core predicates are unchanged; no submask is called full \(P_2\). |
| `one_outer_real_part_and_joint_orientations` | **PASS.** The kernel retains both orientations and frequency signs in the physical operator. |
| `transport_only_tex_backslash_hygiene` | **PASS.** Final mathematical artifacts have no surviving bare separator or tag token. |
| `earlier_review_supersession` | **PASS with clarification.** The postrepair review supersedes only the earlier transport inventory and coarse pre-capacity seam. |
| `capacity_vs_literal_lower_mass` | **PASS.** All promoted quantitative statements are upper-capacity bounds. |
| `exponent_quarantine` | **PASS.** Complete \(P_2\), every parent/bridge, the Gauss-circle target, and all exponent records remain unchanged. |
| `diagnostic_only_computation` | **PASS.** Only deterministic hash, diff, and byte scans were used. |

## 6. Dependencies and exact artifacts used

1. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` —
   `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`;
3. `candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md` —
   `81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72`;
4. `reports/blind_p2_determinant_fibre_rederivation.md` —
   `29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df`;
5. `reviews/blind_post_unmask_p2_fibre_review.md` —
   `4a106d64368506bb3d901fcf4feaec7ff3ddbe4dfd5bc88f09878175b21f0099`;
6. `reviews/blind_post_unmask_p2_fibre_postrepair_verification.md` —
   `66f746af08188ea250bebb694d5ef37fccbe9f8c649f3401977e0f8cb83bab01`;
7. `reviews/conductor_round195_report_reconciliation.md` —
   `3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436`.

The frozen pre-repair blind receipt
`f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf`
was used only for the exact transport reversal check. No web source or
mathematical computation was used. No artifact other than this review was
edited.

## 7. Recommended state effect

**Promote the final kernel through this review gate.** It consistently
supports only:

1. the whole \(P_{2,\ge D_L}\) sector;
2. the exact small-\(\kappa\) absolute-capacity sector
   \(P_{2,<D_L}\cap\mathcal P_{\rm cap}\);
3. their fixed-packet and accepted outer upper bounds; and
4. the scoped coefficient-blind/within-row method boundary.

Retain \(P_{2,<D_L}\cap\mathcal P_{\rm rem}\) as the exact open seam.
Retain the blind report only as qualified algebraic and mechanism evidence.
Reject every squareful-family live multiplicity, quantitative obstruction,
literal nonvanishing, rank-one literal block, or lower-mass inference.

No complete \(P_2\), hard-M1 owner, M9-M1, M9, endpoint theorem, bridge,
Gauss-circle target, or exponent may be promoted from this review alone.

