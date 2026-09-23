# Round 178 dependency, power, and selection seam review

- Campaign: `full-proof-round175-177-strategy-literature-review`
- Round: 178
- Role: independent dependency/power/selection seam reviewer
- Starting graph SHA-256:
  `47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`
- Review mode: post-unmask comparison by exact graph and mechanism
  availability; no source claim and no vote

## 1. Result

**Verdict: GREEN.**

The authoritative graph, the two accepted kernels, and the three Round-178
reports agree on the two lawful quarter-proof trees, the status of every
analytic parent, the power ledgers, and the residual-only scope of `K17a`
and `K26`.  No analytic theorem, parent, bridge, quarter result, or exponent
has been promoted.

The blind report selects the `K26` literal upper endpoint, whereas the
full-graph report selects the high-conductor `K17a` block (177.K34).  This
is not resolved by counting reports.  After unmasking the accepted kernels,
the decisive distinction is mechanism availability:

- Round 175 proves that the proposed `K26` stopped-scale variable is an
  exact coboundary.  The whole chain is only
  \(Q_M^*-Q_{R_0}^*\), the lower endpoint is target-safe, and every
  scale-only Abel/Haar/martingale or coefficient-independent positive
  closure restores the missing factor \(L\).  A direct actual-symbol
  endpoint theorem remains logically possible, but no unspent scale
  coordinate or concrete contraction is left.
- Round 177 isolates the exact final additive conductor
  \(q=u_0/(\ell,u_0)\), pays every fixed-polylogarithmic conductor and every
  physical lift, and leaves one explicit signed high-\(q\) block.  Rank-one
  \(TT^*\), positive Parseval, one square-root saving, lift erasure, and
  termwise orientation pairing are parked, but the joint signed average in
  (177.K34) across the retained divisor, alias, conductor and orientation
  labels has not been reduced to any of them.

Accordingly, the one recommended Round-179 objective is

\[
\boxed{\text{the complete high-conductor signed `K17a` block (177.K34).}}
\]

The stronger aliaswise statement (177.K35) is not selected.  This is a
strategy choice only.  Its strongest possible immediate consequence is the
complete `K17a` sufficient route for the **residual hard-`TOP` \(t=1\)
scalar** after the already accepted sectors and seams are joined.  It does
not close the complete residual scalar automatically, full \(t=1\), another
few-point channel, hard `TOP`, `M9-M2`, `M9`, either bridge, the quarter
theorem, or any exponent.

The appropriate overall Round-178 closing label is
`strategy_frontier_retained`, relative to the exact frontier left by Round
177.  Source-ledger corrections are ancillary provenance updates and do not
change this analytic label.

## 2. Exact statement and hypotheses

### 2.1 Mechanically verified lawful proof trees

Let

\[
 \mathcal I=\{\mathrm{H1\!-!H3},\mathrm{H4},\mathrm{R5\!-!Full}\},
\]

all of which are accepted.

The **standard tree** is

\[
\begin{aligned}
 &\bigl(\mathrm{M1\!-!TOP}_{\rm direct}
    \wedge\mathrm{M1\!-!SMOOTH}_{\rm direct}\bigr)
   \xRightarrow{\mathrm{M9\!-!M1\ physical\ assembly}}
   \mathrm{M9\!-!M1},\\
 &\bigl(\mathrm{TOP}_{\rm M2}
    \wedge(\mathrm{BAL}_{\rm crit}\wedge\mathrm{BAL}_{\rm rest})
    \wedge\mathrm{UNBAL}\bigr)
   \xRightarrow{\mathrm{M9\!-!M2\ physical\ assembly}}
   \mathrm{M9\!-!M2},\\
 &\mathcal I\wedge\mathrm{M9\!-!M1}\wedge\mathrm{M9\!-!M2}
   \wedge\mathrm{M9\!-!endpoint\!-!uniformity}
   \Longrightarrow\mathrm{M9}
   \xRightarrow{\mathrm{Conditional\!-!bridge}}
   \mathrm{GC\!-!target}.
\end{aligned}
\tag{178.Rstd}
\]

The graph records both physical assemblies as proved conditional reductions,
with exactly the displayed open analytic blockers.  The direct M1 blockers
are `M9-M1-top-endpoint-signed-cone` and
`M9-M1-direct-smooth-residual-blockwise-estimate`.  The M2 blockers are the
hard-`TOP` density/discrepancy energy, full `BAL`, and `UNBAL`; full `BAL`
itself has the independent critical and remaining-label leaves.

The **alternative tree** is

\[
\begin{aligned}
 &\mathrm{LOWER}_{\rm radial}^{\rm open}
  \wedge\mathrm{NONLOWER/INTERFACE}_{\rm radial}^{\rm proved}
  \Longrightarrow\mathrm{GAR}^{\rm open}
  \xRightarrow{\mathrm{GAR\ total\!-!active\ equivalence}^{\rm proved}}
  \mathrm{M1}_{\rm total},\\
 &\mathrm{TOP}_{\rm M2}
  \wedge(\mathrm{BAL}_{\rm crit}\wedge\mathrm{BAL}_{\rm rest})
  \wedge\mathrm{UNBAL}
  \Longrightarrow\mathrm{M9\!-!M2},\\
 &\mathcal I\wedge\mathrm{M1}_{\rm total}\wedge\mathrm{M9\!-!M2}
  \xRightarrow{\mathrm{GC\!-!global\!-!M1\!-!alternative\!-!bridge}}
  \mathrm{GC\!-!target}.
\end{aligned}
\tag{178.Ralt}
\]

`GAR` has an implication only to the total-active alternative bridge.  It
has no implication to blockwise `M9-M1` or to `M9`.  The M2 tree is shared
unchanged by both routes, and its literal real-centre/endpoints remain in
its own parent statements.  Thus the top connector is exactly

\[
 \mathrm{STANDARD}\ \mathbf{OR}\ \mathrm{GAR\!-!ALTERNATIVE},
\]

not an AND and not a hybrid assembled from selected leaves of both routes.

### 2.2 Exact selected interface

Freeze

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\},
\]

fixed \(0<\delta<1/2\), \(0<\gamma<1\), and
\(Q_B=(\log(2X))^B\) for one fixed \(B>0\).  Retain the exact Round-176
two-orientation identity on

\[
 R_{\log}<2\kappa n<R_0,\qquad
 \kappa<\delta L,\qquad (u,n)<\gamma L,qquad
 u\asymp v\asymp L/\kappa,\qquad(u,v)=1.
\]

Write

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,
 \qquad(n_0,u_0)=1,
\]

and for \(\ell\bmod u_0\) put

\[
 q=\frac{u_0}{(\ell,u_0)}.
\]

With the exact amplitudes, phases, two orientations, physical lifts,
selected/no-pair residual field, squarefree and coprimality masks, Fejer
weight, opposing-displacement gates, floors, stars, hard values, endpoint
conjugations and full-line zero extension retained inside
\(\mathcal H_{\kappa,u,u_0,\ell}\), the selected theorem is

\[
\boxed{
 \left|
 \sum_{u_0\mid u}
 \sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)>Q_B}}
 c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
 \right|
 \ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon
}
\tag{177.K34}
\]

uniformly for every supported odd \((\kappa,u)\).  The outer absolute value
is taken only after all displayed divisor and alias labels and both
orientations are recombined.

The exact supporting ledger is

\[
 \#\{\text{literal atoms at fixed }(\kappa,u,u_0)\}\ll u_0L,
\]

\[
 \sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
 \times(\text{literal capacity})
 \ll Lq\log(2q),
\]

and a proved local \(O(LX^\varepsilon)\) estimate sums as

\[
 \sum_{\kappa<\delta L}\sum_{u\asymp L/\kappa}L
 \ll L^2\log(2L)\ll_\varepsilon L^2X^\varepsilon.
\]

### 2.3 Verified target/capacity/missing-power ledger

Here “capacity” is a proved positive, absolute, or
coefficient-insensitive upper ledger, not literal lower mass.

| Frontier | Exact target | Verified capacity | Missing power and exact scope |
|---|---:|---:|---|
| high-\(q\) `K17a` | (177.K34): \(L\) per \((\kappa,u)\), hence \(L^2X^\varepsilon\) after summation | \(Lq\log(2q)\) at exact conductor | conductor power \(q\) up to logarithms; one square root leaves \(L\sqrt q\log q\); residual-route complement only |
| `K26` endpoint | \(Q_M^*\ll L^3X^\varepsilon\) | \(Q_M^*\ll L^4X^\varepsilon\) by coefficient-independent positivity | exactly \(L\); residual-route alternative only |
| complete displayed \(t=1\) scalar | \(L^{3/2}X^\varepsilon\) | \(\min\{L^2,\sqrt{JL}\}X^\varepsilon=L^{3/2}\min\{L^{1/2},H/L+O(L^{-1})\}X^\varepsilon\) | \(\min\{L^{1/2},H/L\}\); other few-point channels/collars still independent |
| complete hard `TOP` | scalar \(L^{3/2}\), equivalently energy \(L^2\) | scalar \(L^2\), equivalently coefficient-insensitive energy \(L^3\) | \(L^{1/2}\) linearly or \(L\) in energy; one M2 parent only |
| critical `BAL` | \(L^3X^\varepsilon\) for the actual energy or zero-subtracted remainder | \(L^4X^\varepsilon\) | exactly \(L\); closes only the persistent critical \(j=1\) leaf |
| remaining-label `BAL` | \(L^{3/2}X^\varepsilon\) per literal quarter packet | worst positive packet \(L^2X^\varepsilon\) | \(L^{1/2}\), equivalently worst physical \(X^{1/12}\); critical `BAL` remains separate |
| `UNBAL` | \(M^{3/4}X^\varepsilon\), \(M=LK\), \(K/L>16\) | raw positive \(M\) | \(M^{1/4}\); in the graph's \(a\)-parameter, \(\mu(a)=a-1/4\) for \(1/4<a\le1/3\), and \((1-2a)/4\) for \(1/3\le a<1/2\) |
| direct hard M1 | normalized \(L^{3/2}\), physical \(X^{1/4}\) | normalized \(L^2\), physical \(X^{1/3+o(1)}\) at \(L=X^{1/6}\) | \(L^{1/2}=X^{1/12}\); hard parent only |
| direct smooth M1 | physical \(X^{1/4}\) uniformly on all smooth labels | first minimax profile \(X^{1/3+o(1)}\) | \(X^{1/12}\); smooth parent only |
| `GAR` lower owner | normalized global \(X^\varepsilon\), equivalently \(\mathcal B_{\rm low}\ll RX^\varepsilon\), \(R=X^{1/4}\) | scalar \(R^2\); deepest root-defect face raw \(M\) | \(R\) globally; deepest face \(M^{1/4}\) versus target \(M^{3/4}\); must include every lower layer and cross owner |
| graded \(W=Y^{7/16}\) lane | \(Y^{1/2+\varepsilon}=Y^{24/48+\varepsilon}\) | coefficient-blind \(Y^{43/48}\); best complete accepted \(Y^{35/48}\) | \(Y^{11/48}\) to the local target; strict sub-\(1/3\) needs a complete bound below \(Y^{27/48}\), hence a saving strictly beyond \(Y^{1/6}\) from the current bound |
| endpoint, `M9`, bridges | no independent analytic target beyond exact uniform assembly | inherit the worst open parent | no independent missing power; unavailable until their antecedents are proved |

The table agrees with the full-graph and source reports.  The blind report's
unspecified entries are a consequence of statement-only isolation, not a
contradiction.

## 3. Proof or derivation

### 3.1 Graph integrity and dependency derivation

The canonical state file hashes exactly to the campaign's starting hash.
It contains 380 obligation records and 1,456 rejected-claim records, with no
duplicate obligation IDs and no dangling dependency, blocker, or implication
references.

The relevant graph records verify:

1. `M9-M1` is open, depends on the proved physical one-count assembly, and
   has exactly the hard and smooth direct blockers.
2. `M9-M2` is open, depends on its proved physical one-count assembly, and
   has exactly the hard-`TOP` density energy, balanced parent, and unbalanced
   parent as blockers.
3. The balanced parent has exactly the critical actual-energy child and the
   independent remaining-label/exact-square child.
4. `M9` remains open with `M9-M1`, `M9-M2`, and endpoint uniformity
   unresolved; the standard conditional bridge remains derived only under
   `M9`.
5. `GAR` remains open only at the complete lower-radial signed owner.  The
   proved total-active equivalence implies the alternative bridge and has no
   edge to blockwise `M9-M1` or `M9`.
6. The alternative bridge still depends on complete `M9-M2`; it does not
   replace any M2 parent.

These facts give (178.Rstd)--(178.Ralt) without adding or deleting an edge.

### 3.2 `K26` power and mechanism audit

The Round-175 kernel proves exactly

\[
 \sum_j\mathcal N_{R_j,R_{j+1}}=Q_M^*-Q_{R_0}^*,
\]

and, after restoring the ordinary-zero and once-only short sectors,

\[
 \sum_j\mathcal N_{R_j,R_{j+1}}
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M}.
\]

Both \(B_{\rm short}\) and \(\mathcal Z_{R_0,M}\) are
\(O(L^3X^\varepsilon)\), and

\[
 0\le Q_{R_0}^*\ll L^3X^\varepsilon.
\]

Therefore

\[
 Q_M^*-Q_{R_0}^*\ll L^3X^\varepsilon
 \quad\Longleftrightarrow\quad
 Q_M^*\ll L^3X^\varepsilon.
\]

Fejer positivity and \(\sum_\epsilon\|Z_{\epsilon,*}\|_2^2\ll L^2\)
give only \(Q_M^*\ll ML^2\ll L^4\).  The coherent controls prove that
support, parity, Fejer positivity and scale geometry cannot uniformly do
better, while explicitly not proving literal lower mass.  The selector
audit also supplies no automatic \(L^{-1}\): the selected/no-pair mask is
Boolean, selected divisor supports are disjoint, allowed no-pair rows may
have constant character, and the complete profile has variation \(O(1)\).

Thus the blind report is right that the remaining K26 theorem is exact and
has only one factor \(L\) missing.  After unmasking, however, the scale
variable it proposed to exploit has no remaining interior degree of freedom.
“Actual-symbol sensitivity” is an admissible theorem class, not a currently
isolated mechanism.

### 3.3 `K17a` power and mechanism audit

The Round-177 kernel proves the exact fold

\[
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell),
 \qquad
 c_{u_0}(\ell)=\frac q{u_0}c_q(a),
\]

with no gcd loss, and the exact coefficient mass

\[
 \sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
 \ll\frac q{u_0}\log(2q).
\]

The literal atom count \(u_0L\) already includes the \(v\)-, \(n_0\)- and
fibre-site lifts.  Multiplication gives \(Lq\log(2q)\), and the accepted
low-\(q\) summation proves every \(q\le Q_B\) packet.  Primitive near-half
aliases have \(q=u_0\) and coefficient of order one, so the strict high-\(q\)
sector is genuine.

One reciprocal square root leaves \(L\sqrt q\log q\); exact rank-one alias
\(TT^*\) reconstructs the physical block; positive Parseval returns bucket
energy; and completion modulo \(q\) may not erase the paid lifts.  These
facts reject several mechanisms, but they leave (177.K34) itself as one
joint signed average over all retained labels.  Selecting (177.K34), rather
than the aliaswise (177.K35), preserves precisely the cancellations not
covered by the no-go statements.

### 3.4 Post-unmask selection reconciliation

The blind choice is based on three correct observations: K26 is an exact
equivalence, its deficit is only \(L\), and the lower seams are paid.  Those
facts establish numerical attractiveness, not mechanism availability.

The post-unmask selection rule asks for the smallest owner-complete theorem
with an analytically unexhausted interface.  K17a and K26 have equal
residual-only downstream scope.  K26 has the smaller raw deficit, but its
only proposed new scale resource is proved to self-return and its surviving
actual-symbol theorem has no finer frozen variable.  K17a has a larger
conductor deficit, but Rounds 176--177 have produced a strict, literal,
lift-priced high-\(q\) packet and an outside-absolute signed aggregation
which none of the parked positive mechanisms controls.  It is also more
falsifiable: failure can be localized to a gcd fold, conductor, lift,
orientation, endpoint, or restored-power seam.

Mechanism availability therefore breaks the tie in favor of (177.K34).
This agrees with the full-graph report and explains, rather than overrides,
the statement-only result.

### 3.5 Residual-only implication boundary

Both accepted kernels state their boundary explicitly.  Neither currently
proves its target.  If (177.K34) were later proved and joined to the already
accepted fixed-proportion and low-conductor sectors, the immediate result
would be the complete K17a sufficient estimate for the residual route.  A
separate connector and conductor-owned State Patch would still be required
for any residual-scalar update.

Even a completed residual scalar leaves the rest of the displayed \(t=1\)
aggregate, independent few-point channels, near-collision collars and the
complete hard-`TOP` parent.  Hence no chain from (177.K34) or the K26
endpoint to `M9-M2`, `M9`, a bridge, `GC-target`, or a global exponent may
be inserted.

## 4. First doubtful or unproved step

The first doubtful step is exactly the analytic inequality (177.K34).
Everything used to state it is already accepted:

- the two opposing orientations and half-frequency character;
- stability of the original gcd;
- the exact fold \(u\to u_0=u/(u,n)\);
- the conductor \(q=u_0/(\ell,u_0)\);
- the coefficient identity and exact-\(q\) mass;
- the \(O(u_0L)\) lift count;
- the fixed-proportion cross-gcd sector; and
- every \(q\le(\log(2X))^B\) packet.

What is not proved is a full conductor saving, two coupled square-root
savings, or an equivalent signed average across the retained gcd, alias,
determinant, fibre and orientation labels before positive recombination.
No variation, factorization, Fourier-norm, residue-bucket or orientation
theorem for the literal selected/no-pair coefficient is available in the
accepted artifacts.

The first graph-theoretic step after a hypothetical proof is also not
automatic promotion: the local theorem must be globally summed, joined to
the previously proved sectors, reviewed at the residual connector, and
then applied by a conductor-owned State Patch.  This review proves none of
those future analytic or state-changing steps.

## 5. Required control test and outcome

| Control | Review test | Outcome |
|---|---|---|
| `both_lawful_quarter_routes` | reconstructed standard and GAR-alternative dependencies directly from graph records | **PASS**; top connector is OR; M2 is common to both |
| `open_owner_and_dependency_status` | checked status, dependencies, blockers and implication edges for M1, M2, endpoint, M9, both bridges and target | **PASS**; no leaf or connector is silently closed |
| `target_capacity_missing_power` | reconciled every table row with graph statements and the two kernels | **PASS**; all normalizations and missing powers in Section 2.3 are consistent |
| `K26_and_K17a_exact_Round175_177_frontiers` | checked (175.C7), (175.C15), (175.C17b), (177.K10)--(177.K14), and (177.K34)--(177.K35) | **PASS**; K26 is one endpoint; K17a is only the high-\(q\) complement |
| `K17a_K26_residual_only_scope` | traced possible implications after either local target | **PASS**; neither is a hard-`TOP`, M2, M9, bridge, quarter, or exponent theorem |
| `hard_TOP_remaining_channels` | compared the residual routes with the complete \(t=1\) and hard-`TOP` owners | **PASS**; other channels and collars remain independent |
| `critical_and_remaining_BAL_scopes` | checked both blockers of the balanced parent | **PASS**; neither leaf implies the other |
| `UNBAL_literal_vector_owner` | checked target and scalar/positive capacity | **PASS**; full varying-modulus signed matrix vector remains required |
| `direct_M1_and_GAR_separation` | checked graph implication edges | **PASS**; GAR reaches only total-active alternative bridge |
| `endpoint_and_bridge_scope` | checked downstream prerequisites | **PASS**; no independent cancellation or premature assembly |
| `graded_sub_one_third_lane` | checked \(35/48\), \(27/48\), \(24/48\), and persistence scope | **PASS**; no exponent is promoted |
| `blind_post_unmask_frontier_selection` | compared K26 and K17a by surviving mechanism rather than deficit or vote | **PASS**; (177.K34) is uniquely selected |
| `strategy_only_no_analytic_promotion` | checked report conclusions against graph status | **PASS**; all proof statuses and exponents remain unchanged |
| graph integrity | recomputed hash, record counts, duplicate IDs and dangling references | **PASS**; expected hash, 380/1,456 records, zero duplicates, zero dangling references |

Required false controls for the selected objective:

1. **Near-half primitive alias:** \(q=u_0\),
   \(|c_{u_0}(\ell)|\asymp1\).  A proof treating every alias as
   \(u_0^{-1}\)-sized is rejected.
2. **Premature absolute value:** the gcd fold must occur before absolute
   values.  Paying the \(g\) lifts separately is rejected.
3. **Rank-one/Parseval return:** exact alias \(TT^*\) and positive Parseval
   do not contract the physical block.  Either alone is rejected.
4. **One-square-root boundary:** a restored result
   \(L\sqrt q\log q\) is not partial promotion.
5. **Lift erasure:** a completion modulo \(q\) must reproduce all physical
   multiplicities; otherwise it is rejected.
6. **Orientation antisymmetry:** complementary divisors leave the literal
   upper near-square support or the character-bearing parity class; a
   termwise pairing is rejected.
7. **Endpoint deletion:** a smooth-interior theorem without hard values,
   entries/exits, stars and zero extensions is rejected.
8. **Owner overreach:** any conclusion beyond the residual K17a route is
   rejected at this seam.

No numerical experiment was performed.  All checks were exact graph,
algebra, and exponent bookkeeping.

## 6. Dependencies and exact artifacts used

Only the files authorized by the review brief were read:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round178_full_proof_strategy_current_literature_review.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/blind_round179_frontier_selection.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md`.

The three reports each contain the repository's seven required sections.
The source report was used only to verify that no imported theorem changes
the dependency/power selection; this review makes no independent source
claim.  The graph was parsed in full for a read-only integrity and edge
audit.  The allocation was 100% analytic, algebraic, and graph-theoretic,
with no web search and no numerical theorem evidence.

No report, kernel, graph, strategy, source card, validation artifact, proof
draft, or synthesis was edited.  This review writes only its assigned file.

## 7. Recommended state effect

**GREEN; retain every proof status and exponent.**

Freeze Round 179 on the one theorem (177.K34), with the exact hypotheses in
Section 2.2.  Promotion in a later analytic round requires:

1. the uniform \(O(LX^\varepsilon)\) bound for every supported
   \((\kappa,u)\), with the complete literal coefficient, both orientations,
   high-\(q\) cutoff, all lifts and endpoints retained;
2. independent verification of the gcd fold, conductor, exact-\(q\)
   coefficient mass, lift multiplicity, local target and global
   \(O(L^2X^\varepsilon)\) summation;
3. all false controls in Section 5; and
4. a separate connector review and conductor-owned State Patch before any
   residual-scalar status change.

The Round-179 stop rule is to stop at the first literal selector,
orientation, gcd, conductor, lift, parity, determinant-range, endpoint, or
restored-power failure.  Stop if the proof returns to rank-one \(TT^*\),
positive Parseval/bucket energy, one reciprocal square root, lift-erasing
completion, or complementary-divisor pairing, or if the restored capacity
is \(L\sqrt q\), \(Lq\), \(Lu_0\), or \(Lu\) rather than \(L\) up to
\(X^\varepsilon\).  Record such a failure as a scoped no-go; do not pivot
in-round to another owner.

The strategy-only closing effect is
`strategy_frontier_retained`.  The internal exponent remains \(1/3\), the
accepted repaired external benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).
