# Round 170 dependency, power, and selection seam review

## 1. Result

**Result: revise; the numerical ledgers and the two top-level proof trees pass, but the selected BAL objective is not owner-complete in the scope claimed.**

The authoritative graph was read and parsed completely at SHA-256

\[
111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae.
\]

The standard quarter tree and the GAR alternative are correctly separated by a logical OR.  The standard tree still requires both direct M1 parents, hard TOP, BAL, UNBAL, endpoint-uniform blockwise assembly, M9, and `Conditional-bridge`.  The GAR tree replaces the blockwise M1 side by the complete GAR-to-total-active-M1 route, still requires all of M9--M2, and proves neither blockwise M9--M1 nor M9.

The BAL energy ledger is also correct: the signed target is \(L^3X^\varepsilon\), the coefficient-uniform positive/adversarial capacity is \(L^4X^\varepsilon\), and the required gain is \(L\), equivalently \(L^{1/2}=X^{1/12}\) at packet-scalar scale when \(L\asymp X^{1/6}\).  The Round-166 correction for K26 is correctly retained: capacity \(L^4X^\varepsilon\), target \(L^3X^\varepsilon\), missing factor \(L\).

The material failure is owner scope.  The selected node `M9-M2-balanced-double-far-oscillatory-remainder` quantifies only persistent \(j=1\) blocks at the critical scale \(L\asymp X^{1/6}\).  The BAL parent quantifies every literal balanced block with \(1\le K/L\le16\).  Round 113 records an additional isolated \(j=2\) block when \(X\) is an exact square and \(K/L=16\); the Round-114, Round-115, and Round-136 owner audits explicitly say that this boundary is not estimated by the persistent-\(j=1\) attack, and the Round-136 full-BAL control says that the rest of BAL remains unchanged.  Therefore the report's claims that (171.BAL) is an “owner-complete” BAL survivor and that its proof “directly closes BAL” are not certified.  The current graph edge from the persistent-\(j=1\) energy node to the all-block BAL parent has a statement-level quantifier mismatch and may not be used as a proof.

There is syntactically exactly one proposed Round-171 objective.  It can remain the sole next task only after being relabelled as a persistent-\(j=1\) child objective and after its downstream claims are narrowed.  If owner-complete BAL closure is required, the objective must instead be widened to all balanced labels, including the exact-square \(j=2\) boundary and every remaining \(j=1\) scale; that is a materially different frozen objective and requires a new ranking review.

## 2. Exact statement and hypotheses

The exact statement verified by the present BAL evidence is the following scoped child theorem.  Let \(B\) be one persistent Round-113 \(j=1\) literal balanced block at \(L\asymp X^{1/6}\), and put

\[
a_B^{<}(h,k)=\chi _4(h)\,
\eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k),
\]

where \(A_B\) is the zero-extended positive-quadrant continuum symbol from Round 113, with its Vaaler taper, slanted support, floors, crossings, and fixed physical block.  For

\[
\Delta=h'k'-hk,\qquad \rho=hk'-h'k,
\qquad
\mathrm{df}=\{|\Delta|>L,\ |\rho|>L\},
\]

define

\[
\mathcal R_{B}^{\mathrm{osc}}
=\sum_{\mathrm{df}}a_B^{<}(h,k)\overline{a_B^{<}(h',k')}
\left[e\!\left(\sqrt X(\sqrt{hk}-\sqrt{h'k'})\right)-1\right].
\tag{2.1}
\]

The lawful scoped objective is

\[
\boxed{|\mathcal R_B^{\mathrm{osc}}|\ll_\varepsilon L^3X^\varepsilon}
\tag{171.BAL\mbox{-}j1}
\]

with both character factors, both low-gcd weights, both literal symbols, all support data, and the fixed-block outer modulus retained.  No shiftwise, residuewise, divisorwise, aliaswise, shellwise, or physical-cell absolute value is allowed.

The proved phase-free identity is

\[
E_{B,\mathrm{df}}=M_B^{(0)}+\mathcal R_B^{\mathrm{osc}},
\qquad |M_B^{(0)}|\ll_\varepsilon L^3X^\varepsilon.
\tag{2.2}
\]

Together with the proved equal-product and two width-\(L\) corridor bounds, (171.BAL-\(j1\)) yields the persistent-\(j=1\) packet energy bound and hence the packet scalar bound \(\ll L^{3/2}X^\varepsilon\) for that fixed block.  The verified implication chain is therefore

\[
\text{persistent-\(j1\) oscillatory remainder}
\Longrightarrow
\text{persistent-\(j1\) double-far energy}
\Longrightarrow
\text{persistent-\(j1\) fixed-block packet}.
\tag{2.3}
\]

It does **not** yet imply the universally quantified `M9-M2-smooth-balanced-quarter-packet-estimate`.  A separate owner/quantifier connector must discharge the isolated exact-square \(j=2\) boundary and every other balanced label not covered by \(L\asymp X^{1/6}\).

The two lawful quarter trees, after this repair, are:

\[
\begin{aligned}
\mathsf T_{\rm std}:\quad
&\{\text{M1 hard},\text{ M1 smooth},\text{ TOP},\text{ full BAL},
\text{ UNBAL},\text{ endpoint uniformity}\}\\
&\Longrightarrow \mathrm{M9}\Longrightarrow
\mathrm{Conditional\mbox{-}bridge}\Longrightarrow\mathrm{GC\mbox{-}target},\\[1mm]
\mathsf T_{\rm GAR}:\quad
&\{\text{complete GAR lower owner},\text{ full M9--M2}\}
\Longrightarrow\mathrm{GC\mbox{-}global\mbox{-}M1\mbox{-}alternative\mbox{-}bridge}
\Longrightarrow\mathrm{GC\mbox{-}target}.
\end{aligned}
\tag{2.4}
\]

The braces are conjunctions, and the two displayed trees are alternatives.

## 3. Proof or derivation

### Tree and owner audit

The graph statements certify the standard chain

\[
\begin{gathered}
\{mathrm{M1\ hard},\mathrm{M1\ smooth}\}
\Rightarrow\mathrm{M9\mbox{-}M1},\\
\{\mathrm{TOP},\mathrm{BAL},\mathrm{UNBAL}\}
\Rightarrow\mathrm{M9\mbox{-}M2},\\
\{\mathrm{M9\mbox{-}M1},\mathrm{M9\mbox{-}M2},
\mathrm{endpoint\ uniformity}\}\Rightarrow\mathrm{M9}.
\end{gathered}
\]

The alternative bridge depends on `M9-M1-GAR-total-active-equivalence` and M9--M2.  That equivalence depends on GAR and expressly denies an implication to blockwise M9--M1 or M9.  Thus the report's top-level logical separation is correct.

The BAL child-to-parent seam is different.  Round 113 proves

\[
\frac KL=4^j\frac{X}{\lfloor\sqrt X\rfloor^2}.
\tag{3.1}
\]

Consequently \(j=1\) is persistently balanced, while \(j=2\) belongs to BAL exactly for square \(X\), at \(K/L=16\).  The BAL parent ranges over every such block.  In contrast, the current oscillatory-remainder and actual-energy statements say “persistent \(j=1\)” and “\(L\asymp X^{1/6}\).”  Round 114 says the \(j=2\) boundary remains a separate control and is not declared estimated; Round 115 leaves that boundary unchanged; and the Round-136 `full_BAL_owner_and_downstream_scope` control says the result concerns only one persistent \(j=1\) bulk owner, while the exact-square \(j=2\) boundary and the rest of BAL remain unchanged.  Hence the all-block parent cannot follow from the scoped child without a missing theorem.  This is a quantifier failure, not a disagreement about naming.

### Power audit

For one critical block, the complete packet scalar has coefficient-blind envelope \(L^2\) and target \(L^{3/2}\).  Squaring gives energy capacity \(L^4\) and target \(L^3\).  Thus the missing factor is \(L^{1/2}\) at scalar scale and \(L\) at energy scale.  Since \(L\asymp X^{1/6}\), this is \(X^{1/12}\).  The \(L^4\) quantity is only a positive/adversarial capacity: it is neither a lower bound for the physical scalar nor an equivalent formulation of the signed target.  The frontier report observes this distinction correctly.

For K26, fixed-shift Cauchy over \(O(M_L)=O(L^2)\) shifts and per-shift mass \(D_L\asymp L^2X^\varepsilon\) gives \(L^4X^\varepsilon\).  The sufficient K26 target is \(L^3X^\varepsilon\).  The frontier's boxed correction and missing-factor ledger therefore pass.

### Mechanism and no-go audit

The proposed two-defect commutator is not explicitly excluded by the accepted BAL no-gos, provided it is a genuinely non-positive scalar identity on the complete actual coefficient.  The accepted failures remain binding:

- fixed-\((\Delta,\rho)\) divisor-bounded multiplicity does not save \(L\) after summing the full two-dimensional defect range;
- the phase is constant on fixed \((n,\Delta)\) fibres;
- for \(p=2s\), \(\chi_4(h)\chi_4(h+p)=(-1)^s\) is constant on the fixed-\(p\) fibre, so no inner-\(h\) character cancellation is available;
- determinant size, continuous Hessian nondegeneracy, and fixed-\(Q\) broad transversality do not give a discrete scalar bound;
- positive cap/row energies and coefficient-uniform inequalities stop at the \(L^4\) shadow;
- aliaswise \(\ell^1\), spacing-only large sieve, and a second B-process return at capacity or self-return.

Thus novelty passes only conditionally.  A valid commutator must create cancellation across the recombined shift/alias family, not inside a fixed shift, and must visibly fail for phase-adapted arbitrary bounded coefficients.  The axial sectors \(p=0\) or \(q=0\), which are compatible with both far gates, must be isolated and paid at \(O(L^3X^\varepsilon)\) or incorporated into the exact identity; the two factorizations cannot simply be divided by \(p\) and \(q\).

### Promotion-gate repair

The five proposed gates are directionally sound but incomplete.  A valid Round-171 promotion packet must add:

1. an explicit fixed-\(p\) control showing where cancellation occurs despite the constant gauge \((-1)^s\);
2. an axial \(p=0\)/\(q=0\) ledger and a multiplicity proof for every nonaxial chart;
3. a check that the commutator is not merely the rejected fixed-defect divisor bound in different notation; and
4. an owner-quantifier gate.  Either promotion stops at the persistent-\(j1\) remainder and energy nodes, or a separate proof covers the exact-square \(j=2\) boundary and all remaining balanced labels before the BAL parent is touched.

The report's other downstream and exponent nonimplications are correct: even complete BAL leaves TOP and UNBAL before M9--M2; the standard route also leaves both M1 parents and endpoint uniformity, while the alternative leaves complete GAR.  Neither a BAL child nor full BAL changes the internally proved \(1/3\) exponent or imports the external Li--Yang benchmark into an internal node.

## 4. First doubtful or incorrect step

The first incorrect step occurs before the speculative commutator estimate: it is the assertion that (171.BAL), as stated only for persistent \(j=1\), is owner-complete for BAL and would promote `M9-M2-smooth-balanced-quarter-packet-estimate`.  The child and parent quantifiers do not match, and the exact owner audits explicitly preserve the \(j=2\) boundary and the rest of BAL.

The mandatory repair is one of the following, with no silent mixture:

- **Scoped repair (recommended):** rename the objective (171.BAL-\(j1\)); delete every claim that it closes full BAL; list the exact-square \(j=2\) boundary and any noncritical balanced labels as remaining owners; split or quarantine the invalid child-to-parent edge; and recompute the owner-leverage ranking with this objective treated as a strict BAL descendant.
- **Owner-complete repair:** widen the theorem to every literal balanced block covered by the parent, prove uniformity at the isolated \(j=2\), \(K/L=16\) square endpoint and all remaining \(j=1\) scales, and re-audit the commutator, capacity, and restoration ledgers there.  This is a new frozen objective, not a cosmetic edit.

After that scope repair, the first genuinely unproved analytic step is the existence of an exact owner-preserving two-direction commutator identity whose complement is \(O(L^3X^\varepsilon)\) and whose estimate saves \(L\) without a positive norm.  No such identity or estimate is presently proved.  Its first hostile test is the fixed-\(p\) constancy of the character gauge, followed by the axial sectors and the fixed-defect-capacity no-go.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `authoritative_dependency_tree` | **Pass at the top level; fail at the BAL child-to-parent seam.** Both quarter trees and their mandatory top-level leaves are correct, but the persistent-\(j1\) node does not discharge the all-block BAL parent. |
| `standard_vs_GAR_logical_or` | **Pass.** GAR is confined to the alternative total-M1 bridge and is not used to prove blockwise M9--M1 or M9. |
| `BAL_owner_scope` | **Fail, material.** Round 113 includes the isolated exact-square \(j=2\) boundary; Rounds 114--115 leave it separate; Round 136 says the rest of BAL is unchanged. |
| `exact_BAL_remainder_definition` | **Pass for the scoped persistent-\(j1\) child.** The two far gates, product coefficient, zero subtraction, and fixed-block outer norm agree with the graph. |
| `BAL_implication_chain` | **Pass only through the fixed persistent-\(j1\) packet; fail as written into full BAL.** The phase-free and corridor reductions are valid within scope. |
| `BAL_L3_vs_L4` | **Pass.** \(L^3\) is the signed energy target and \(L^4\) is a coefficient-uniform positive/adversarial capacity, not a physical lower bound. |
| `K26_L4_vs_L3_correction` | **Pass.** Capacity \(L^4\), target \(L^3\), missing \(L\). |
| `rejected_mechanism_bypass` | **Conditional pass with repair.** A complete actual-symbol commutator is not ruled out, but it must address fixed-\(p\) character constancy, axial sectors, fixed-defect summation, fixed-\(Q\) rulings, and every positive/self-return no-go. |
| `promotion_gates` | **Fail pending repair.** The existing gates omit the parent-quantifier seam and do not name the fixed-\(p\) and axial controls explicitly. |
| `downstream_and_exponent_nonimplications` | **Pass after deleting the full-BAL promotion claim.** TOP, UNBAL, M1/GAR, endpoint, M9, both bridges, and the quarter theorem remain open; no exponent changes. |
| `single_Round171_objective` | **Pass syntactically.** Retain exactly (171.BAL-\(j1\)) if the scoped repair is adopted; no fallback objective may be started in-round. |
| `no_status_or_exponent_overpromotion` | **Pass for present statuses, with a mandatory future guard.** No node is presently promoted, but a future proof may not use the invalid edge to promote full BAL. |
| `no_in_round_analytic_pivot` | **Pass.** The proposed stop rule forbids movement to competing frontiers. |

No numerical experiment was required.  The algebraic spot checks \(\Delta\pm\rho=q(2h+p),p(2k+q)\) and \(\chi_4(h)\chi_4(h+2s)=(-1)^s\) pass; they do not supply the missing commutator estimate.

## 6. Dependencies and exact artifacts used

The following were read completely where required by the brief:

1. `protocol.md`;
2. `state/proof_obligations.yml`, parsed completely at the hash above, including all 373 obligation nodes and the rejected-claim ledger;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`;
5. `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/synthesis.md` (Round 113);
6. `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md` and `reviews/conductor_round114_norm_owner_and_mean_square.md`;
7. `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md` and `reviews/conductor_round115_identity_and_zero_mode.md`;
8. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/synthesis.md` and the exact `full_BAL_owner_and_downstream_scope` control in `reports/joint_cluster_defect_broad_narrow_attack.md` (Round 136); and
9. `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/synthesis.md` for the authoritative K26 correction.

The exact graph nodes audited were the two bridges; M9, M9--M1, M9--M2, their physical one-count assemblies and analytic parents; the GAR lower/interface/nonlower chain; the BAL normalization, dictionary, corridor, phase-free, remainder, actual-energy, alias, and broad--narrow obstruction nodes; `GC-partial-one-third`; and `GC-external-Li-Yang-theta-star`.  The Round-113--116 and Round-136 rejected claims were checked for mechanism scope.  No web source or numerical computation was used.

## 7. Recommended state effect

**Recommended effect: `revise`; no proof status, dependency, exponent, or theorem promotion.**

Do not accept the current owner-completeness sentence or a State Patch that promotes full BAL from the persistent-\(j1\) remainder.  Repair the graph seam by splitting the scoped critical child from the universally quantified BAL parent, or supply a separately validated all-balanced-label connector.

Subject to that repair, retain exactly one Round-171 objective:

\[
\boxed{\text{prove (171.BAL-j1) for every persistent critical }j=1\text{ block}.}
\]

It must use the complete actual coefficient, pass the augmented commutator, fixed-\(p\), axial, multiplicity, missing-power, literal-restoration, and false-coefficient controls, and stop with a scoped no-go at the first failure.  It must not pivot to another frontier.

If successful, the lawful immediate effect is limited to the persistent-\(j1\) oscillatory-remainder and actual-energy children, after independent seam validation.  The isolated exact-square \(j=2\) boundary and every other uncovered balanced label still block the full BAL parent; hard TOP and UNBAL still block M9--M2; both direct M1 parents and endpoint uniformity still block the standard route; complete GAR still blocks the alternative route.  The internal exponent remains \(1/3\), the external Li--Yang benchmark remains separate, and the quarter target remains open.
