# Candidate provenance, owner, and graph-scope review

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Artifact reviewed:
  `candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md`
- Starting graph SHA-256:
  `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Verdict: **REPAIR BEFORE FORMALIZATION OR STATE PATCH**
- Audit boundary: definitions, dependency provenance, physical-mask typing,
  exact complement, owner and protected-parent scope, terminal label, graph
  cycles, and exponent quarantine.  The previously assigned algebra and
  power seams remain separate reviews.

## 1. Result

The candidate has the right narrow mathematical scope.  The three Round-197
reports and the conductor reconciliation support, at most, the lower-swap
common-sharp-cell sector (P_{\rm cc}), its exact intersection with the
Round-195 open packets, and a route no-go for extending the current argument
to all of (P_0) or to the whole four-corner rectangle.  They do not support
complete (P_2).

The proposed common-cell sector is conceptually a genuine physical mask and
is not defined by coefficient nonvanishing: it compares two tuples of named
literal predicate/branch data before any spectral operation.  Equality of
those tuples is symmetric under the lower allocation swap, while inequality
has the explicit sharp-face capacity identified in the reports.  Thus it is
not the tautology “retain the atoms on which the desired coefficient bound
holds.”  Nonemptiness is neither assumed nor proved; this is allowed by the
existing strict-sector convention, as already illustrated by the possibly
empty Round-184 selected sector.

The current text is nevertheless not ready for formalization or a State
Patch.  Four repairs are mandatory.

1. The meta-definition “complete sharp literal code” must be replaced by one
   fixed finite tuple of explicit accepted predicates and branch indices.  Its
   dead state must mean failure of named zero-extension predicates, not
   (a=0), (lambda=0), or accidental vanishing of a smooth factor.
2. The Round-184 selector parameter, the packet variables
   ((\kappa,Y,\mathfrak m)), (C_0), the physical atom (W), and the three
   outer operators used in (197.C10)--(197.C34) must be defined without
   relying on prose aliases.
3. The dependency ledger must cite and type the exact Round-184, 185, 193,
   and 195 kernels and the precise interfaces reopened from each.
4. Proposed state effect 7.3 must be removed.  The accepted Round-195 node
   must not be rewritten to depend on the new Round-197 theorem.  The latter
   already depends on Round 195; the reverse edge would create an immediate
   dependency cycle.  The refined remainder belongs in the new node and in
   the open owner's `next_action`, while the Round-195 node remains protected.

Subject to those repairs and the remaining independent seam reviews, the
candidate is eligible for one subordinate strict-sector node.  No owner,
parent, bridge, theorem, or exponent may be promoted.

## 2. Exact definitions and physical-mask audit

On the inherited opened endpoint source, retain

\[
 N=dm,\qquad N+r=d'm',\qquad g=(d,d'),\qquad
 d=g\alpha,\quad d'=g\beta,
\]

with the literal Round-185 endpoint coefficient.  The lower swap is

\[
 \tau_0(g\alpha,m,g\beta,m')=(gm,\alpha,g\beta,m').
\]

On

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1},
\]

the recomputed character-leg gcd is again (g), the reverse cross condition
is ((\alpha,\beta)=1), and the sign condition forces (m) and (\alpha)
to be odd and unequal.  Hence (P_0) is a physical two-cycle domain before
Fourier, height, anchor, or Farey operations.

The intended mask passes the independence test only after the following
formal repair.  Define an explicit finite tuple

\[
 \mathfrak c_{N,\sigma}(u,v)
  =(I_{\rm supp},I_{\rm shell},I_{\rm cone},j_{\rm profile},
    j_{\rm floor},j_{\rm star},j_{1/2},j_{\rm sample},
    j_{\rm cell},j_{\rm crossing},j_{\rm trace},j_{\rm sign},\ldots),
\]

where the ellipsis is replaced in the formal candidate by the remaining
finite list from the accepted literal transform.  Each entry must be a
predicate value or a branch/index value evaluable from
((N,\sigma,u,v,L,X)).  The tuple must explicitly exclude

\[
 a_{L,X}^{\rm lit,\sigma}(u,v),\quad
 \lambda_{N,\sigma}(v),\quad
 \rho_N(v),\quad \eta_L(u),
\]

and every smooth-factor value.  A distinguished dead tuple is permitted only
when its value is determined by the named support/zero-extension predicates.
With that definition,

\[
 C_{\rm lit}
 =\mathbf1_{\mathfrak c_{N,\sigma}(m,g\alpha)
                 =\mathfrak c_{N,\sigma}(\alpha,gm)},
 \qquad P_{\rm cc}=P_0C_{\rm lit}
\]

is symmetric under (\tau_0), is a coordinatewise physical deletion, and
is independent of accidental coefficient vanishing.  It may be empty, but
it is not defined by the conclusion to be proved.

The formal candidate must also fix the Round-184 selected-prime closeness
constant under a noncolliding name such as (K_{\rm sel}>0).  Round 184
defines (\rho_N) from ((N,L,K_{\rm sel})); the present statement fixes no
such parameter and its displayed constants omit that dependence.  Either
declare (K_{\rm sel}) globally fixed once and for all, or write the relevant
implicit constants as depending on it.  Physical inward cross gcd
(\kappa) must not be used for this selector parameter.

Finally, replace the vague factorization in (197.C22) by the exact accepted
Round-184 symbol formula, or an explicitly cited finite product derived from
it.  On a common live code only the scale-normalized (C^1) factor receives
the pointwise (D_L/L) bound.  The zero-extended dyadic profile is summed by
discrete total variation, and the selector is handled by its truth table.
This keeps the mask definition separate from all three analytic estimates.

## 3. Exact complement, operator typing, and first remaining seam

The physical complement in (197.C13)--(197.C14) is exact.  Indeed, first
split (P_2) according to ((m,\beta)>1) or ((m,\beta)=1); on the second
piece split according to (\chi_4(\alpha m)=-1) or not; on (P_0) split
according to (C_{\rm lit}=1) or (0).  This gives the pairwise disjoint
identity

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\rm lit}
       \ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}.
\]

The sign-failure set correctly includes both (\chi_4=+1) and
(\chi_4=0); no even swapped divisor is silently discarded.  The
gcd-failure set is a changed physical allocation and cannot be replaced by
zero extension.  The literal-boundary set contains live/dead transitions and
different branch/cell tuples; none is estimated by the proposed theorem.

After applying the exact linear open-packet operator, the later remainder is

\[
 \begin{aligned}
 &\{\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}\\
 &\qquad\cap
 (P_{\partial\rm lit}\ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}).
 \end{aligned}
\]

This is an exact refinement of the work still left after Round 197, not a
revision of what Round 195 proved.  Only (P_{\rm cc}) is removed.  Complete
(P_2), (P_1), and the other original-(t) incidences remain open.

The candidate must make the operator statement self-contained.  Before
(197.C10)--(197.C12), define the physical inward gcd (\kappa) in both
primitive orientations, the dyadic height (Y), the spectral lift gcd
(\mathfrak m), and fixed (C_0\ge2).  Define
(\mathscr R_{\rm core,out}^{\sigma}) as the exact restored outer aggregate
of the accepted fixed-(Y) cores, and similarly define
(\mathscr R_{\rm cap,out}^{\sigma}) and
(\mathscr R_{\rm open,out}^{\sigma}), including the dyadic partition and
the one-outer-real-part convention.  At present “the complete accepted
Round-192 outer core” is not an exact definition: Round 193 states a
fixed-(Y) operator and Round 195 supplies the fixed-to-outer ledger.  Also
clarify the apparent clash between fixed superscript (\sigma) and the
phrase “both frequency signs restored.”

With these definitions, the operator typing is otherwise sound.  The mask is
inserted as (P_{\rm cc}W) on the physical source.  The Round-193 product
rule retains the transported-mask commutator and affine births/deaths, and
the Round-195 safe packet proof is positive under additional physical
deletion.  Consequently

\[
 \mathscr R_{\rm open,out}(P_{\rm cc}W)
 =\mathscr R_{\rm core,out}(P_{\rm cc}W)
  -\mathscr R_{\rm cap,out}(P_{\rm cc}W)
\]

has the correct linear type.  No packet predicate is inserted into the
physical orbit.

The first unproved extension remains exactly
(P_{\partial\rm lit}=P_0(1-C_{\rm lit})).  The aligned-ratio identity

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}
\]

shows why a generic sharp-face collar can retain all (O(LD_L)) lower-close
pairs and hence the full (D_LL^2X^\varepsilon) envelope.  This is a
capacity no-go for the current route, not nonvanishing or a lower bound for
the literal operator.

## 4. Dependency provenance and statement repairs

The recorded starting hash matches the current SHA-256 of
`state/proof_obligations.yml`.  All four named accepted nodes have status
`proved_internal`.  Their roles should be typed as follows.

1. `M9-M1-hard-top-t1-comparable-factor-exchange-sector`, represented by
   `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`,
   supplies the exact literal symbol ledger (K184.11)--(K184.16), the
   selected-prime rule, and the selector truth table (K184.4).  The new proof
   directly reuses this coefficient calculus even though the graph also
   reaches it transitively.
2. `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`, represented by
   `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
   supplies the total zero-extended endpoint coefficient (K185.1)--(K185.4),
   the multiplicity-one even-shift source (K185.6), the two primitive charts,
   and the absolute monotone/low-height exit theorem (K185.7).
3. `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`, represented by
   `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`,
   supplies the exact physical-mask evaluation convention and transported
   mask product rule (193.C19b)--(193.C21).  Its double-close collar
   (193.C31) is not a theorem for the one-close (P_2) face and must not be
   cited as one.
4. `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`, represented by
   `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`,
   supplies the fixed-(\kappa) physical count (195.C14)--(195.C17), the
   deletion-stable masked-operator passage (195.C18), the packet bound
   (195.C20), the fixed-to-outer ledger (195.C20b), and the exact safe/open
   split (195.C5a).

The candidate's unqualified phrase “direct accepted interfaces” should be
replaced by this typed ledger.  It is acceptable for a State Patch either to
record all four direct edges, because all four proofs are explicitly
reopened, or to use the graph's minimal transitive edge convention; in the
latter case the omitted edges must remain explicit interface provenance in
the theorem artifact.  No Round-197 report is an accepted dependency.  The
three reports and
`reviews/conductor_round197_report_reconciliation.md` are claimant evidence
only.  The blind report supports the algebraic/support no-go, not the outer
masked-core theorem by itself.  No computation is theorem evidence.

The first formalization defect is the open-ended definition of
\(\mathfrak c\), followed immediately by the unsupported shorthand “up to a
fixed finite product” in (197.C22).  Until the tuple and exact symbol product
are enumerated, a formalizer cannot verify that code equality implies one
common sharp multiplier while excluding coefficient values.  This is a
statement-completeness defect, not evidence that the intended common-cell
theorem is false.  The missing selector parameter and undefined packet/outer
operator notation are the next defects.  They must all be repaired before a
formal proof artifact is generated.

The exact artifacts used by this review are:

- `AGENTS.md`, `protocol.md`, `state/proof_obligations.yml`, and
  `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md`;
- the three Round-197 reports
  `reports/literal_four_corner_allocation_commutator_attack.md`,
  `reports/four_corner_orbit_power_hostile_audit.md`, and
  `reports/blind_four_corner_commutator_rederivation.md` under that campaign;
- `reviews/conductor_round197_report_reconciliation.md` under that campaign;
- the four kernel paths enumerated above; and
- for patch-shape comparison only,
  `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/state_patch.json`
  and
  `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/final_candidate_provenance_owner_scope_review.md`.

No web source, external theorem, numerical computation, proof draft,
validation matrix, or unlisted candidate was used.

## 5. Graph-cycle, terminal-label, and protected-scope audit

The relevant accepted ancestor cone has the order

\[
 \text{Round 195}\longrightarrow\text{Round 193}
 \longrightarrow\cdots\longrightarrow\text{Round 185}
 \longrightarrow\text{Round 184},
\]

where arrows point from a node to its prerequisites.  The open hard small-
(t) owner already depends on all four.  A new Round-197 node depending on
these accepted interfaces, followed by adding that new node as a dependency
of the open owner, introduces no cycle in this relevant cone: the new node
does not reach the owner.

Proposed state effect 7.3 is unsafe as written.  If the accepted Round-195
node is updated so that its refined remainder theorem logically depends on
the new Round-197 node, then

\[
 \text{Round 197 node}\to\text{Round 195 node}
 \to\text{Round 197 node}
\]

is an immediate two-cycle.  Omitting the dependency while rewriting the
Round-195 statement would merely hide the same circular provenance and would
also rewrite the historical scope of a protected theorem.  Leave the
Round-195 status, statement, dependencies, evidence classification, and
terminal label unchanged.  Put the refined remainder only in the new node
and in the open owner's next action.  Reverse/replay validation should compare
the relevant cycle set before and after the patch and certify that no new
cycle is introduced; unrelated pre-existing graph cycles are outside this
round and remain protected no-change state.

The terminal label passes.  The active campaign freezes exactly

`p2_four_corner_orbit_boundary_self_return_no_go`

as one allowed exit, and the candidate uses it.  This truthfully records that
the full rectangle forces (\kappa=1), misses every open packet
(2\le\kappa<D_L), and that the lower-only repair stops at the literal-face
boundary.  The non-frozen report phrase
`strict_p2_common_cell_allocation_commutator_sector` may describe the
subordinate node informally but must not replace the round terminal label.
The frozen label `strict_p2_four_corner_allocation_commutator_sector` must not
be used, because the whole rectangle is not proved target-safe.

The downstream owner is exactly
`M9-M1-hard-top-high-radical-small-t-residual-estimate`, and it remains
`open`.  The new result removes only one physical common-cell part of the
Round-195 open (P_2) packets.  It does not close the remainder in Section 3,
all of (P_1), complete original (t=1), any original (t\ge2) incidence,
or the large-(G) near-resonant complement.

Protected no-change nodes include the four accepted dependencies above,
`M9-M1-top-endpoint-signed-cone`,
`M9-M1-direct-smooth-residual-blockwise-estimate`,
`M9-M1-physical-one-count-assembly`,
`M9-M1-global-angular-radial-estimate`, `M9-M1`, every M2 parent,
`M9-endpoint-uniformity`, `M9`, `Conditional-bridge`,
`GC-global-M1-alternative-bridge`, `GC-partial-one-third`,
`GC-external-Li-Yang-theta-star`, and `GC-target`.

## 6. Required controls and outcomes

| Control | Outcome |
|---|---|
| starting graph hash | **PASS.** The candidate hash equals the current proof-state hash. |
| common-cell mask is physical | **PASS AFTER DEFINITION REPAIR.** It is evaluated from the two lower physical allocations before spectral operations. |
| independence from coefficient nonvanishing | **PASS IN INTENT; REPAIR FORMALLY.** Enumerate the finite code and exclude (a), (\lambda), (\rho), (\eta), and smooth-factor values. |
| non-tautological sector | **PASS.** Code inequality has an explicit unresolved complement and aligned-face capacity; no theorem-validity predicate occurs in the mask. |
| nonemptiness/density | **NOT CLAIMED, correctly.** No mass inference is licensed. |
| selector provenance | **REPAIR.** Fix (K_{\rm sel}), avoid collision with physical (\kappa), and state constant dependence. |
| exact physical complement | **PASS.** (197.C13)--(197.C14) are disjoint and exhaustive on (P_2). |
| exact open-packet complement | **PASS AFTER NOTATION REPAIR.** Intersect the Round-195 open packet set with (P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}). |
| physical/open operator distinction | **PASS IN LOGIC; REPAIR DEFINITIONS.** Define (W,\kappa,Y,\mathfrak m,C_0) and all outer operators exactly. |
| coefficient/BV provenance | **REPAIR.** Cite the exact K184 formula and give the finite product; only the (C^1) factor has pointwise (D_L/L). |
| Round-193 mask passage | **PASS.** The transported-mask commutator, births, deaths, both (T) branches, anchors, and zero extensions remain in the recomputed core. |
| Round-195 subtraction | **PASS.** It is performed after the physical estimate and uses the deletion-stable safe packet union. |
| exact dependency typing | **REPAIR.** Separate direct logical use, reopened connector interfaces, transitive provenance, and claimant evidence. |
| graph cycle | **FAIL AS PROPOSED IN 7.3; REPAIR.** Do not make Round 195 depend on the new node or rewrite its accepted statement. |
| owner scope | **PASS.** Only a subordinate strict sector of the open hard small-(t) owner is affected. |
| frozen terminal label | **PASS.** Use `p2_four_corner_orbit_boundary_self_return_no_go`. |
| protected parents | **PASS subject to an explicit no-change list in the State Patch.** |
| exponent quarantine | **PASS.** No internal, external-benchmark, target, parent, bridge, or theorem exponent changes. |
| diagnostic-only computation | **PASS.** No numerical result is used as theorem evidence. |

The first doubtful step in the present artifact is therefore not the orbit
algebra but the formal implication from equality of an undefined “complete
code” to the exact common-cell symbol factorization.  The required control
is an explicit finite code/symbol table checked against K184.11 and K185.2.
Outcome on the current text: **not mechanically checkable**.  Outcome after
the prescribed enumeration: the mask, its complement, and its independence
from coefficient nonvanishing become mechanically checkable.

## 7. Recommended state effect

**Revise, then re-review.**  After the definition, notation, provenance, and
cycle repairs, the strongest permissible patch shape is:

1. create one subordinate `proved_internal` node for the explicitly defined
   common-cell lower allocation commutator sector, its outer core estimate,
   its intersection with the exact Round-195 open packets, the disjoint
   complement, the (\kappa=1) full-rectangle restriction, and the aligned-
   face route no-go;
2. give that node only accepted prerequisite edges, with the four reopened
   kernel interfaces typed as in Section 4, and `implies: []`;
3. update only
   `M9-M1-hard-top-high-radical-small-t-residual-estimate` by adding the new
   node as a subordinate dependency/evidence item and by replacing its
   `next_action` with the exact remaining (P_2) set from Section 3, while
   keeping the owner status `open`;
4. leave the Round-184, Round-185, Round-193, and Round-195 nodes unchanged;
5. record rejected overclaims for a nonempty/dense common-cell sector, a
   target-safe whole rectangle or whole (P_0), a proved complement, a
   changed-gcd zero-extension shortcut, a Round-195 reverse dependency, any
   owner or parent closure, and any exponent improvement; and
6. close Round 197 under
   `p2_four_corner_orbit_boundary_self_return_no_go`.

This patch would preserve the exact mathematical gain without rewriting an
accepted ancestor, enlarging the downstream owner, creating a new relevant
cycle, or changing any exponent.
