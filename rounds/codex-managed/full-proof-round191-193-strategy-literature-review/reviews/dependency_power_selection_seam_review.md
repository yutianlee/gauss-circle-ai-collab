# Round 194 dependency, power, and selection seam review

## 1. Result

**Verdict: REPAIR.**

I independently compared full_graph_frontier_reconstruction_after_round193.md at SHA-256

265884e29f9fcd562dd9dbcc04dbc486bee9fa7440c1886b51a8c4c3a3e1c807

with the frozen authoritative graph at SHA-256

cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e.

The exact Round-191--193 residual, the physical \(P_{\rm cl},P_1,P_2\) partition, both \(T\)-branches, the fixed-packet target and deficit, the owner quarantine, the unique \(P_2\) selection, its false controls, and the exponent quarantine are correct. The report nevertheless fails the “two exact dependency trees” and “every live frontier with target/capacity/missing power” deliverables in two repairable places:

1. the alternative GAR tree mis-types two direct graph dependencies; and
2. the frontier table omits the open local-moment node and presents several graph-unquantified deficits as prose in a “missing power” column without saying that no complete power is certified.

These are formal reconstruction defects, not evidence against the selected \(P_2\) strategy. No claimant agreement was used as proof.

## 2. Exact statement and hypotheses

This verdict is conditional only on the frozen Round-194 graph and campaign. It does not adjudicate a new analytic estimate.

The standard route is lawfully summarized as
\[
\mathrm{GC\mbox{-}target}
\leftarrow \mathrm{Conditional\mbox{-}bridge}
\leftarrow (H1\mbox{-}H3,H4,R5\mbox{-}Full,M9),
\]
with
\[
M9\leftarrow(M9\mbox{-}M1,M9\mbox{-}M2),
\]
and with the direct hard/smooth M1 owners and hard-TOP/BAL/UNBAL M2 owners remaining open. The report correctly types \(M9\)-endpoint-uniformity as an open blocker. In the graph it is a blocker of, and has an implies edge to, \(M9\); it is not a member of the direct dependencies array of \(M9\). Its tree edge must therefore remain explicitly blocker-typed rather than be promoted to an ordinary dependency edge.

The alternative bridge has direct dependencies
\[
H1\mbox{-}H3,\ H4,\ R5\mbox{-}Full,\ 
M9\mbox{-}M1\mbox{-}GAR\mbox{-}total\mbox{-}active\mbox{-}equivalence,\ M9\mbox{-}M2.
\]
The exact GAR sub-DAG is:

- M9-M1-GAR-total-active-equivalence depends directly on both M9-M1-global-angular-recombination and M9-M1-global-angular-radial-estimate;
- M9-M1-global-angular-radial-estimate depends directly on M9-M1-global-radial-one-count-assembly and M9-M1-terminal-height-nonlower-radial-completion;
- M9-M1-global-radial-one-count-assembly depends directly on global angular recombination, smooth critical radial terminal transfer, the lower-radial phase diagram, the open global lower-radial signed estimate, and the proved radial interface estimate;
- the radial interface estimate itself depends, among other proved inputs, on terminal-height/nonlower radial completion.

This is a DAG with reused proved nodes, not the nesting printed in report lines 68--75.

## 3. Proof or derivation

### 3.1 Round-191--193 residual audit

The report preserves the accepted normalization
\[
Q=H_B,\qquad
T=\min\!\left\{\frac{U-1}{2},
\left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
\qquad
A=\min\{U-1,\lfloor Q^{C_0}\rfloor\}.
\]
At \(T=0\), the Farey projector is empty and the core is the whole inherited rho-large remainder. At \(T\ge1\), the report requires every strict covector inequality
\[
|c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A)
\]
simultaneously and also
\[
|\rho|\ge (A+1)(T+1).
\]
No branch or covector is silently deleted.

With \(D_L=\lceil\sqrt L\rceil\), the masks are imposed on the original physical opposing incidences before Fourier expansion or height differencing:
\[
P_{\rm cl}
=\mathbf 1_{|d-gm|\le D_L}\mathbf 1_{|d'-gm'|\le D_L},
\]
\[
P_1=\mathbf 1_{|d-gm|>D_L},\qquad
P_2=\mathbf 1_{|d-gm|\le D_L}\mathbf 1_{|d'-gm'|>D_L}.
\]
They are disjoint and exhaustive. The accepted absolute ledger
\[
LD\log L+LD^2
\]
is target-safe at \(D=\sqrt L\) and loses power upon widening. The report correctly assigns no accepted estimate to \(P_1\) or \(P_2\), retains both orientations and the complete anchor Fourier aggregate under one outer real part, and keeps the subsidiary scaled involution below the uncontrolled actual-coefficient commutator.

The fixed-packet target
\[
Q\mathfrak m\kappa uX^\varepsilon,
\]
positive capacity
\[
Y\kappa uX^\varepsilon,
\]
and missing factor
\[
\frac{Y}{Q\mathfrak m}
\]
are exact. The outer \(L^2X^\varepsilon\) consequence is also correctly scoped. Completion of \(P_2\) would remove only that first-failure mask; it would not remove \(P_1\), any original \(t\ge2\) small-\(G\) incidence, the large-\(G\) near-resonant complement, smooth M1, GAR, or any M2 owner.

### 3.2 Target, capacity, and missing-power audit

The following entries are consistent with the accepted graph and Round-190--193 records:

- \(P_1\) and \(P_2\): fixed target \(Q\mathfrak m\kappa u\), positive capacity \(Y\kappa u\), missing factor \(Y/(Q\mathfrak m)\);
- remaining hard-M1 owner scale: \(L^{3/2}\) target versus \(L^2\) positive capacity, missing \(L^{1/2}\);
- smooth direct M1: \(X^{1/4}\) target versus \(X^{1/3+o(1)}\), missing \(X^{1/12}\);
- hard M2 TOP: scalar \(L^{3/2}\), equivalently energy \(L^2\), versus row-positive energy \(L^3\), missing \(L^{1/2}\) at scalar level or \(L\) at energy level;
- critical \(j=1\) BAL: \(L^3\) energy target versus \(L^4\), missing \(L\);
- endpoint fallback: \(X^{1/4}\) target versus \(X^{1/3}\), missing \(X^{1/12}\) in addition to the unresolved parents;
- the \(W=Y^{7/16}\) determinant node: \(Y^{1/2}\) target versus \(Y^{35/48}\), missing \(Y^{11/48}\).

The table is incomplete because the graph also contains the distinct open node GC-nonsubcoherent-actual-cluster-local-moment. It is named in report line 82 but has no comparison row. At \(W=Y^{7/16}\), its literal cluster target is \(Y^{1/2+\varepsilon}\), the first complete-block accepted capacity is \(Y^{37/48+\varepsilon}\), and the missing factor is \(Y^{13/48}\). Its target would feed the persistence exponent \(1/6+\alpha/3\), hence \(5/16\) at \(\alpha=7/16\); it is a sub-one-third stepping stone and has no implication edge to a quarter route.

For GAR, remaining-label BAL, and the complete UNBAL owner, the frozen graph does not certify a single complete monomial capacity from which an exact global missing power can be subtracted. The report is right not to invent one, and its audited \(\sqrt\Delta\) UNBAL loss is correctly labeled “at least,” but the table must explicitly say “no complete graph-certified capacity; exact missing power unquantified.” Phrases such as “complete non-polylogarithmic owner saving” and “full missing packet estimate” describe the task, not a certified missing power.

The hard-M1 \(t\ge2\)/near-resonant summary row is lawful only as the frozen frontier category. Those incidences remain separate from the original-\(t=1\) \(P_1/P_2\) residual and must not be converted into an accepted joint dependency or silently closed by the \(P_2\) theorem.

### 3.3 Selection, controls, and quarantine

The report selects exactly one objective, the complete physical \(P_2\) mask. Its proposed defect-scale signed endpoint-commutator seam acts on the full selected complement and is not represented as an accepted theorem. The promotion gate requires both \(T\)-branches, both orientations, all literal coefficients/endpoints, the fixed-packet estimate, and outer assembly. The stop rule forbids an in-round pivot.

The false shadows are correctly chosen: arbitrary bounded height arrays, adversarial or phase-conjugating endpoint coefficients, deletion of the character or signs, separate orientation norms, post-expansion scalar masking, the scaled involution alone, another static Farey refinement, and positive defect counting. These are prospective Round-195 falsification controls, not claimed analytic outcomes.

No route mixing occurs in the prose scope. The internal exponent remains \(1/3\), the accepted external benchmark remains \(0.3144831759740614\ldots\), and the target remains \(1/4\). The open graded \(5/16\) implication is not promoted.

## 4. First doubtful or unproved step

The **first exact defect in the report** is line 69 of the alternative tree, continued at line 75. It makes GAR the sole child of M9-M1-GAR-total-active-equivalence and places exact global angular recombination below GAR. The graph instead makes global angular recombination and GAR sibling direct dependencies of the equivalence node. The same displayed tree places terminal/nonlower completion directly below radial one-count assembly, whereas it is a direct dependency of GAR and a dependency of the radial interface node, not a direct dependency of the assembly node.

Thus the control assertion at report line 217 that both dependency trees pass is too strong until the displayed alternative sub-DAG is repaired. The first genuinely unproved analytic seam remains the report's proposed \(P_2\) signed commutator saving by \(Y/(Q\mathfrak m)\); this review neither proves nor refutes it.

## 5. Required controls and outcomes

- Frozen graph hash and statuses: **PASS**.
- Standard route and hard/smooth M1, hard-TOP/BAL/UNBAL owner separation: **PASS**, with endpoint uniformity retained as a typed blocker/implies edge rather than an ordinary direct dependency.
- Alternative route scope: **REPAIR** the direct GAR dependency edges stated above; the no-blockwise-M1/no-route-mixing prose is otherwise correct.
- \(P_{\rm cl},P_1,P_2\), physical pre-operator masking, width boundary, and deletion stability: **PASS**.
- \(T=0\) and \(T\ge1\) branches and simultaneous strict covectors: **PASS**.
- Fixed target, positive capacity, and \(Y/(H_B\mathfrak m)\) deficit: **PASS**.
- Every-live-frontier power table: **REPAIR** by adding the local-moment row and explicitly typing graph-unquantified capacities/missing powers.
- Unique \(P_2\) objective, promotion gate, false shadows, stop rule, and no in-round pivot: **PASS**.
- Strategy-only status and exponent quarantine: **PASS**.
- Claimant-consensus control: **PASS**; the verdict follows from graph edges, accepted kernels/syntheses, and frozen powers, not agreement among reports.

## 6. Dependencies and exact artifacts used

- protocol.md;
- state/proof_obligations.yml at SHA-256 cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e;
- state/active_campaign.yml for frozen Round 194;
- state/best_proof_draft.md and state/project_summary.md for accepted owner/exponent scope;
- strategy/round194_full_proof_strategy_current_literature_review.md;
- rounds/codex-managed/full-proof-round187-189-strategy-literature-review/synthesis.md;
- the Round-191, Round-192, and Round-193 syntheses named in the task packet;
- proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md;
- the reviewed Round-194 report at the hash stated in Section 1.

No numerical evidence, web-source claimant consensus, blind-report agreement, or unaccepted candidate was used as proof.

## 7. Recommended state effect

**Repair the Round-194 report only; make no proof-state change.** Replace the alternative GAR sub-DAG by the exact direct dependencies above, add the omitted local-moment frontier with \(Y^{1/2}\), \(Y^{37/48}\), and \(Y^{13/48}\), and label unavailable complete capacities/missing powers as graph-unquantified.

After those repairs, retain \(P_2\) as the unique Round-195 strategy objective and retain the exit label strategy_frontier_retained. Promote no analytic node, parent, endpoint theorem, bridge, global theorem, or exponent. All current graph statuses and the \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) exponent quarantine remain unchanged.
