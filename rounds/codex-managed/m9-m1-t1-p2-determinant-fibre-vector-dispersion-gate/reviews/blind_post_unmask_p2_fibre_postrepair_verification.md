# Round 195 blind \(P_2\) fibre postrepair verification

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Role: postrepair receipt, live-normalization, and evidence-classification audit
- Status: review evidence only; no candidate, reconciliation, graph, kernel,
  synthesis, or state edit

## 1. Result

**PASS with one notation-only candidate repair before formal promotion.**

The repaired blind report has SHA-256

`29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df`,

exactly matching the current conductor reconciliation. Its only byte
changes from the frozen blind receipt

`f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf`

are ten inserted backslashes before `qquad`. Removing those ten bytes in
memory reconstructs the frozen hash exactly. The final file is strict
UTF-8 without a BOM, invalid control byte, replacement character, bare
`qquad`, or bare `tag{...}` token. No known transport defect in the repaired
class survives.

The transport repair changes no mathematical classification. The blind
report remains usable only for its correct signed fibre identities,
divisor/quadratic-congruence forms, collision equations, joint-vector
formulation, and arbitrary-array mechanism control. Its squareful
\(U=p^2\) family is not live literal support, its claimed
\(\gg\sqrt U\) multiplicity is not a live multiplicity, and its
phase-aligned shadow is not a quantitative obstruction to the fixed-packet
target.

The current candidate correctly incorporates the decisive live repair:
on nonzero literal support \(\kappa gU\) is squarefree, so \(U\) is
squarefree and \((\kappa,U)=1\). The minus fibre then has at most
\(2^{\omega(U)}\ll_\varepsilon U^\varepsilon\) roots modulo \(U\). The
candidate's large-\(\kappa\) and absolute-capacity packet sectors are
upper-bound theorems derived without coefficient cancellation and are
logically independent of the blind false shadow.

The candidate twice writes \(p\in\mathcal P_{\rm cap}\), although
\(\mathcal P_{\rm cap}\) is defined by a condition on \(\kappa\) and no
packet symbol \(p\) is introduced. The intended condition is unambiguous,
but the formal statement should say
\(\kappa\in\mathcal P_{\rm cap}\), or introduce a packet symbol explicitly.
This is notation-only and does not affect the audited inequalities.

## 2. Exact statement and hypotheses

The live normalization suppressed by the isolated blind statement is

\[
 U=\mathfrak m q,\qquad U\mid u,\qquad u=gU,\qquad
 u\asymp v\asymp L/\kappa,\qquad g=O(1),
\tag{2.1}
\]

together with

\[
 Y<h\le2Y,\qquad 0<2\kappa gh<R_0,\qquad
 L\ll X^{1/4},
\tag{2.2}
\]

and all literal shell, hard-cone, squarefree, allocation-coprimality,
residual, endpoint, core, Farey, carry, birth/death, mask-commutator, and
zero-extension predicates. On nonzero support the fixed divisor is
\(\kappa gU\) in the plus or minus endpoint, hence

\[
 \kappa gU\ \text{squarefree}
 \quad\Longrightarrow\quad
 U\ \text{squarefree},\qquad(\kappa,U)=1.
\tag{2.3}
\]

The algebraic blind formulas retained after adjoining (2.1)--(2.3) are

\[
 v(\kappa v+F)=2h-U\delta+\kappa U^2
\quad(+),
\tag{2.4}
\]

and

\[
 \kappa v^2+\delta v+2h\equiv0\pmod U,\qquad
 F=\frac{2h+\delta v+\kappa v^2}{U}-\kappa U
\quad(-).
\tag{2.5}
\]

They count cross-row algebraic candidates. They are not literal vector
inner-product estimates and do not imply lower mass.

The candidate makes the exact physical split

\[
 P_2=P_{2,\ge D}+P_{2,<D},\qquad
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}}.
\tag{2.6}
\]

For the small-\(\kappa\) packet define the predicates

\[
 \mathcal P_{\rm cap}:
 \min(Y,D_L)\le H_B\mathfrak m\kappa,\qquad
 \mathcal P_{\rm rem}:
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\tag{2.7}
\]

The selected positive estimates are

\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma
       (P_{2,\ge D}W)\right|
 \ll H_B\mathfrak m\kappa uX^\varepsilon,
\tag{2.8}
\]

and

\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma
       (P_{2,<D}W)\right|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\tag{2.9}
\]

Equation (2.9) is target-safe on \(\mathcal P_{\rm cap}\). Its exact
unresolved packet complement is
\(P_{2,<D}\cap\mathcal P_{\rm rem}\).

## 3. Proof and derivation

### 3.1 Byte-exact repair receipt

The repaired report has 22,081 bytes and 573 LF line endings, with no CRLF
conversion and no BOM. The ten repaired separators occur at current lines

\[
 139\ (2),\quad284\ (1),\quad285\ (1),\quad
 378\ (2),\quad379\ (1),\quad396\ (1),\quad
 403\ (1),\quad418\ (1).
\tag{3.1}
\]

Deleting only those ten backslash bytes produces 22,071 bytes and SHA-256

\[
 \texttt{f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf}.
\]

This proves both that the current reconciliation's repaired receipt is
correct and that the repair has no semantic content. A strict scan of the
blind report, reconciliation, and candidate found valid UTF-8, zero
forbidden control bytes, zero replacement characters, zero bare `qquad`
tokens, and zero bare `tag{` tokens in each file.

### 3.2 Live squarefree rejection of the blind large fibre

For every prime \(\ell\mid U\), (2.3) makes \(\kappa\) invertible modulo
\(\ell\). Therefore

\[
 f(v)=\kappa v^2+\delta v+2h
\]

is a genuine quadratic over \(\mathbf F_\ell\) and has at most two roots.
As \(U\) is squarefree, the Chinese remainder theorem gives

\[
 \#\{v\bmod U:f(v)\equiv0\pmod U\}
 \le\prod_{\ell\mid U}2
 =2^{\omega(U)}
 \ll_\varepsilon U^\varepsilon.
\tag{3.2}
\]

The live \(v\)-range has length \(O(u)=O(gU)\), and \(g=O(1)\), so each
residue class modulo \(U\) occurs only \(O(1)\) times. Thus the live minus
cross-row algebraic fibre is \(O_\varepsilon(U^\varepsilon)\) before the
remaining literal deletions. The plus fibre is controlled by the
corresponding divisor bound.

The blind family takes \(g=\kappa=1\) and \(U=p^2\). Its fixed divisor is
then \(p^2\), so the literal squarefree endpoint predicate sets its
coefficient to zero. The squareful modulus is precisely what permits the
displayed \(\sqrt U\) quadratic-root shadow. It is excluded rather than
promoted by the live operator.

### 3.3 No blind quantitative obstruction

The same family also fails the live packet independently:

1. it takes \(u=1\), while (2.1) requires \(u=gU=p^2\);
2. it takes \(Y=2QU\), while its \(h=(p-1)^2/8<Y\), contrary to \(Y<h\);
3. it takes \(L=p^2\) and \(X=p^4\), hence \(L=X^{1/2}\), contrary to
   \(L\ll X^{1/4}\);
4. it does not verify the hard cone or any residual, core, endpoint, Farey,
   carry, birth/death, commutator, or zero-extension survival.

Even if only the row normalization is repaired, its coherent size is
\(n\asymp\sqrt U\), whereas, since \(Q=H_B\),

\[
 K=H_B\mathfrak m\kappa uX^\varepsilon
   =H_B\mathfrak m\kappa gU X^\varepsilon.
\tag{3.3}
\]

Thus \(n\ll K\) and \(n^2\ll K^2\). The blind shadow supplies neither a
fixed-packet violation nor a literal diagonal lower bound.

### 3.4 Candidate absolute-capacity sectors

The candidate's large-\(\kappa\) count is absolute. Lower closeness costs
\(O(D_L)\) choices of the close affine variable, the determinant interval
costs \(O(1)\) choices of its companion, \(g=O(1)\), and
\(U,v=O(1+L/\kappa)\). Therefore

\[
 \sum_{\kappa\ge D_L}D_L(1+L/\kappa)^2\ll L^2.
\tag{3.4}
\]

At a fixed packet the same count, followed by the accepted row and
anchor/Abel ledger, costs \(O(D_LuX^\varepsilon)\); the inherited
terminal/Fejer term costs \(O(\kappa uX^\varepsilon)\). Since
\(\kappa\ge D_L\), this proves (2.8) without cancellation.

For \(\kappa<D_L\), the close window meets only \(O(1)\) sites in its one
legal residue class. The fixed-height and all-height counts give,
respectively, \(YuX^\varepsilon\) and \(D_LuX^\varepsilon\). Taking their
minimum and adding the terminal/Fejer term gives (2.9). If
\(\min(Y,D_L)\le H_B\mathfrak m\kappa\), both terms are bounded by the
target, proving the exact absolute-capacity packet sector. Nothing in this
argument uses the blind large fibre, arbitrary coefficients, phase
cancellation, or a separate orientation norm.

### 3.5 No unsupported literal mass

The blind phase-conjugated all-ones array is valid only as a false control
against claims uniform over arbitrary bounded arrays. It does not identify
the actual Vaaler/profile endpoint values, show their nonvanishing, or
control their radical, anchor, Fejer, carry, event, and mask-commutator
phases. Likewise, the exact same-site \(2\times2\) and \(3\times3\)
all-ones event blocks in the reconciliation establish within-site
self-return after signed recombination; they do not give a cross-row
positive lower bound. All quantitative statements retained by the
candidate are upper-capacity estimates.

## 4. First doubtful or unproved step

The first unproved mathematical step remains the coefficient-sensitive
joint \(++,+-,-+,--\) cross-row Gram estimate on

\[
 P_{2,<D}\cap\mathcal P_{\rm rem}
 =
 \left\{\kappa<D_L,\ 
 \min(Y,D_L)>H_B\mathfrak m\kappa\right\}.
\tag{4.1}
\]

It must retain actual endpoint products, square-root and anchor phases,
Fejer factors, residual masks, unequal translations, carries,
births/deaths, the physical-mask commutator, cross-event terms, common zero
extensions, both orientations and frequency signs, and one outer real part.
Neither the repaired blind report, the squarefree root count, nor the
same-site self-return proves this estimate.

Before formal promotion, the candidate should also replace the two
undefined occurrences of \(p\in\mathcal P_{\rm cap}\) by
\(\kappa\in\mathcal P_{\rm cap}\), or define a packet symbol. This is a
statement-hygiene repair, not an additional mathematical gap.

## 5. Exact controls and outcomes

| Control | Outcome |
|---|---|
| `postrepair_receipt_exactness` | **PASS.** Current blind SHA is `29ae2a...35df` and matches the reconciliation. Removing exactly ten repaired bytes reconstructs `f19700...0adf`. |
| `transport_only_tex_backslash_hygiene` | **PASS.** No bare `qquad` or `tag{` token survives; strict UTF-8 and byte scans are clean. |
| `blind_evidence_classification` | **PASS.** Retain fibre algebra and the scoped method control only; no blind positive theorem or literal lower bound is used. |
| `inherited_U_divides_u_and_u_equals_gU` | **PASS after unmasking.** The live target uses \(u=gU\); the blind \(u=1,U=p^2\) shadow is rejected. |
| `live_height_carrier_shell_normalization` | **PASS after rejection.** The blind \(Y,h,L,X\) choices are not treated as a live packet. |
| `literal_squarefree_nonzero_support` | **PASS.** Nonzero support forces \(\kappa gU\) and hence \(U\) squarefree with \((\kappa,U)=1\). |
| `determinant_fibre_multiplicity` | **PASS after repair.** The live minus root bound is (3.2); the squareful \(\sqrt U\) family is not live. |
| `capacity_vs_literal_lower_mass` | **PASS.** Equations (2.8)--(2.9) are upper bounds; no capacity-to-mass implication is asserted. |
| `unsigned_character_erased_adversarial_controls` | **PASS only as mechanism falsifiers.** Arbitrary phase alignment proves no actual endpoint nonvanishing or mass. |
| `Gram_diagonal_and_phase_collisions` | **PASS with scope.** Same-site all-ones blocks prove recombination/self-return only; the literal cross-row Gram remains open. |
| `exact_round193_P2_physical_mask` | **PASS.** The candidate uses the exact split (2.6), and the strict open complement is retained. |
| `absolute_large_kappa_sector` | **PASS as candidate evidence.** The count (3.4) is absolute and independent of blind cancellation. |
| `absolute_capacity_packet_sector` | **PASS as candidate evidence.** Equation (2.9) is target-safe exactly under \(\mathcal P_{\rm cap}\). |
| `candidate_packet_membership_notation` | **REVISE.** Replace undefined \(p\) by \(\kappa\), or define a packet symbol, before promotion. |
| `no_width_Farey_or_proper_submask_escape` | **PASS.** \(D_L\) is unchanged and no strict submask is promoted as complete \(P_2\). |
| `actual_endpoint_coefficient_vectors` | **OPEN on (4.1).** No arbitrary array is substituted into the literal theorem. |
| `one_outer_real_part_and_joint_orientations` | **PASS in the candidate; required in (4.1).** No separate-orientation closure is licensed. |
| `fixed_packet_to_outer_power_ledger` | **NO BLIND SUPPORT.** The candidate relies on the accepted nonblind ledger, not the blind report. |
| `exponent_quarantine` | **PASS.** No complete \(P_2\), parent theorem, bridge, Gauss-circle target, or exponent is promoted. |
| `diagnostic_only_computation` | **PASS.** Only deterministic byte/hash scans were run; no numerical evidence is used for mathematics. |

## 6. Dependencies and exact artifacts used

This verification used exactly:

1. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `reports/blind_p2_determinant_fibre_rederivation.md` —
   `29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df`;
3. `reviews/conductor_round195_report_reconciliation.md` —
   `3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436`;
4. `candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md` —
   `cd0230f22b31f3454c975cf8b8625026687adba97a0d180e2556156bd990d0d7`;
5. `reviews/blind_post_unmask_p2_fibre_review.md` —
   `4a106d64368506bb3d901fcf4feaec7ff3ddbe4dfd5bc88f09878175b21f0099`.

For transport provenance, the frozen pre-repair blind SHA is
`f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf`,
and the six-byte intermediate SHA is
`73de8ef51dbe33b90f87fdf3bbb21beec623ef147423214db0a74ab53de77e88`.

No web source or mathematical computation was used. No candidate,
reconciliation, report other than this verification, kernel, graph, state,
proof draft, validation matrix, synthesis, or control artifact was edited.

## 7. Recommended state effect

**Retain the post-unmask classification and current candidate boundary;
revise only receipt/notation hygiene.**

1. Replace the old blind receipt wherever necessary by the final repaired
   SHA `29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df`.
   The conductor reconciliation already does so correctly.
2. Retain the blind plus/minus fibre identities, collision equations, joint
   Gram requirement, and arbitrary-array false control only as algebraic
   and method-boundary evidence under the live hypotheses.
3. Reject the blind \(p^2\) family as live support, reject its
   \(\sqrt U\) live multiplicity, and reject every claimed target violation,
   rank-one literal block, literal nonvanishing, or lower mass derived from
   it.
4. Retain the candidate's squarefree-\(U\) root bound, whole
   \(P_{2,\ge D_L}\) sector, and exact \(\mathcal P_{\rm cap}\) sector as
   candidate evidence independent of the blind report.
5. Correct \(p\in\mathcal P_{\rm cap}\) notation before formal promotion,
   while leaving the exact open complement (4.1) unchanged.
6. Keep the coefficient-sensitive cross-row four-block Gram on (4.1) as
   the first missing theorem.

No complete \(P_2\), original-\(t=1\) owner, M9-M1, M9, endpoint theorem,
bridge, Gauss-circle target, or exponent change is supported by this
verification.

