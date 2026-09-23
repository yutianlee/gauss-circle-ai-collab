# Round 165 downstream graph and State Patch scope review

## 1. Result

**Verdict: GREEN for one new proved-internal reduction node, one refinement
of the Round-164 reduction, and inconclusive-only attachment to the two open
hard-TOP parents.**

The exact recommended State Patch has:

- **one create**:
  `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`;
- **three updates**:
  the Round-164 residual Fejer reduction and the two open hard-TOP parents
  `M9-M2-top-endpoint-signed-cone` and
  `M9-M2-top-endpoint-density-discrepancy-energy`;
- **no correction** to an accepted theorem;
- the explicit rejected-claim list in Section 7; and
- no status change outside the new reduction node.

The new node may be `proved_internal` because its owners are exact
identities, exact reductions, and two strict target-safe incidence sectors:
the monotone tangent sector and the fixed-proportion high
character-divisor-gcd sector. The estimates

\[
 \Re\mathfrak C_{R_0,2,\mathrm{opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon
 \tag{165.K17a}
\]

and

\[
 \Re\sum_{\substack{R_0\le r<M_L\\2\mid r}}
 \left(1-\frac r{M_L}\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon
 \tag{165.K26}
\]

must remain explicitly **open sufficient theorems** inside that proved
reduction. Neither is a proved child node.

The proposed obligation ID and all rejected-claim IDs listed below are
fresh in the current graph. The dependency insertion is acyclic. No result
transfers to the complete residual, full \(t=1\), the other few-point
channels, either hard-TOP parent, BAL, UNBAL, M9--M2, M9--M1, endpoint
uniformity, M9, the bridge, the quarter target, or either global exponent.

## 2. Exact statement and hypotheses

### 2.1 New node

Create the following obligation.

**ID**

`M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`

**Type, track, status, and title**

\[
\begin{array}{ll}
\text{type}:&\texttt{reduction},\\
\text{track}:&\texttt{M9\_analytic},\\
\text{status}:&\texttt{proved\_internal},\\
\text{title}:&
\text{Hard-TOP \(t=1\) residual Fejer parity, tangent, gcd, and scale reduction}.
\end{array}
\]

**Proposed statement**

Retain the complete literal residual coefficient after the accepted
close-opposite-prime XOR sector, with supported squarefree rows, odd
character-bearing divisors, both complementary parity branches, neither/both
or no-pair selector, actual profiles, hard values, endpoints, and zero
extension. Let \(M_L\asymp L^2\) be the cardinality of a containing
interval and
\(D_L=\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon\).
For every positive integer \(R\), the exact sliding identity and endpoint
inequality are

\[
 \mathfrak E_R
 ={1\over R}\sum_s\left|\sum_{j<R}c_{s+j}^{\rm rem}
 e(J\sqrt{s+j})\right|^2
 =D_L+2\Re\mathfrak C_R,
 \qquad
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le {M_L+R-1\over R}\mathfrak E_R.
\]

Splitting every window into absolute even and odd sites gives the
endpoint-exact parity connector

\[
 \mathfrak E_R\le2\mathfrak E_R^{(2)},\qquad
 \Re\mathfrak C_R\le D_L/2+2\Re\mathfrak C_R^{(2)},
\]

where the right side keeps exactly the even shifts; for odd \(R=2S+1\)
the exact convex mixture of length-\(S\) and length-\(S+1\) subsequence
energies gives the terminal weight \(1/R\).

At the minimal diagonal-safe scale \(R_0=\lceil L\rceil\), the
multiplicity-one tangent coordinates

\[
 a=d'-d,\quad b=m'-m,\quad
 r=db+am+ab=db+a m',\quad
 \chi_4(d')\chi_4(d)=(-1)^{a/2}
\]

show that the complete \(a,b\ge0\) union has \(O(L^2)\) literal atoms,
the nonpositive and one-zero-negative sectors are empty, and every
remaining tuple has \(ab<0\). The character-divisor gcd
\(g=(d,d')\) gives

\[
 d=gu,\quad d'=gv,\quad r=gh,\quad
 vm'-um=h,\quad N=A+guv\,t,
\]

with fixed row character \(\chi_4(uv)\), row length \(O(1+g)\), and

\[
 |\mathfrak C_{R_0,g\ge G_0}^{\rm rem}|
 \ll_\varepsilon L^3G_0^{-1}X^\varepsilon.
\]

Thus the monotone sector and every fixed-fraction sector
\(g\ge\gamma L\) are strict owner-complete target-safe
divisor-incidence sectors. The residual target would follow from the open
even-shift, opposing-displacement, low-\(g\) theorem (165.K17a).

The cofactor gcd \(s=(m,m')\) gives a second multiplicity-one progression
with actual product step \(2mm'/s\) and character
\(\sigma_0(-1)^{(r\bmod2)k}\); in particular the character is frozen on
every even-shift row, including the squarefree even-even branch. The exact
phase derivatives have scales

\[
 |\Psi'|\asymp Jh/L,\qquad
 \Psi''\asymp Jh/(sL),\qquad
 |\Psi'''|\asymp Jh/(s^2L).
\]

Large real derivatives give no modulo-one separation. Classical positive
second-derivative placement and smooth full-row Poisson followed by
absolute dual modes are adverse only in their stated placements; coupled
dual modes, higher-order, joint \((r,N)\), signed spectral, and bespoke
actual-arithmetic methods remain open.

Finally, \(R_0\) is minimal diagonal-safe, not mandatory. At \(R=M_L\),
fixed-shift Cauchy pays all \(r<R_0\) within the \(L^3X^\varepsilon\)
energy budget, so the distinct open even medium/long theorem (165.K26)
also suffices. Neither (165.K17a) nor (165.K26) is proved. No residual,
full-\(t=1\), other-channel, hard-TOP-parent, smooth-packet, M9--M2,
M9--M1, endpoint, M9, bridge, quarter, or exponent conclusion follows.

**Graph fields**

\[
\begin{aligned}
 \text{dependencies}&=[
 \texttt{M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction}],\\
 \text{implies}&=[],\\
 \text{blockers}&=[].
\end{aligned}
\]

Use owner `Codex conductor`, `last_updated_round: 165`, and terminal label
`strict_residual_short_shift_sector`.

The next action should be:

> At the minimal scale, prove (165.K17a) with one outer real part and all
> literal weights retained; alternatively prove the maximal-scale even
> medium/long theorem (165.K26). Do not treat failure of the shortest
> shifts as terminal, and do not transfer either strict sector to another
> channel or parent.

### 2.2 Positive evidence for the new node

The new node's positive evidence should contain exactly the following
current proof artifacts:

1. `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_gcd_parity_progression_reduction.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_variable_scale_fejer_bypass.md`;
4. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/actual_residual_short_shift_attack.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/blind_fejer_short_shift_rederivation.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/short_shift_arithmetic_hostile_audit.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/parity_connector_high_gcd_review.md`;
8. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/tangent_gcd_parity_seam_review.md`;
9. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/variable_scale_fejer_bypass_review.md`; and
10. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/downstream_graph_state_scope_review.md`.

Use empty negative and inconclusive evidence lists on the new reduction
node. Open estimates are quarantined in its statement and next action,
not misclassified as positive theorems.

## 3. Proof of graph placement and exact updates

### 3.1 Round-164 reduction update

Keep the following fields of
`M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction`
unchanged:

- `type: reduction`;
- `track: M9_analytic`;
- `status: proved_internal`;
- all current dependencies, implies, and blockers.

Append to its statement:

> The full-line sliding identity and endpoint inequality hold for every
> positive integer window length \(R\). The choice
> \(R=\lceil L\rceil\) is the minimal diagonal-safe scale, not the unique
> Fejer continuation. The parity, tangent, dual-gcd, strict-sector, and
> maximal-scale refinements are recorded in
> `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`; their two
> printed sufficient aggregate estimates remain open.

Append the new terminal kernel and the variable-scale review to this
node's positive evidence. Replace its next action by:

> Use the Round-165 refinement. At \(R_0=\lceil L\rceil\), prove the
> even-shift, opposing-displacement, low-character-divisor-gcd aggregate
> (165.K17a), or at \(R=M_L\) prove the even medium/long aggregate
> (165.K26). Preserve the actual selectors, squarefree masks, profiles,
> endpoints, parity branches, and one outer real part. Failure of the
> minimal short-shift route is not terminal.

Set `last_updated_round: 165`. Do **not** add the new node as a dependency
of the Round-164 node; that would reverse the mathematical order and create
a two-node cycle once the new node depends on Round 164.

### 3.2 Updates to the two open hard-TOP parents

For each of

- `M9-M2-top-endpoint-signed-cone`; and
- `M9-M2-top-endpoint-density-discrepancy-energy`,

append
`M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`
to `dependencies`.

Append the ten artifacts in Section 2.2 to
`evidence.inconclusive`, not to positive or negative evidence. Keep each
parent's type, title, statement, status, implies, blockers, and next action
unchanged. Set only the ordinary Round-165 update metadata.

This placement is exact. The terminal kernel proves strict residual
subsectors and sufficient connectors, but neither parent estimate. It is
therefore positive evidence for the new reduction and only inconclusive
route evidence for the two open parents.

### 3.3 Acyclicity

Reading arrows from prerequisite to consumer, the new edges are

\[
\begin{array}{c}
\text{Round-164 residual reduction}\\
\downarrow\\
\text{Round-165 parity/gcd/scale reduction}\\
\swarrow\qquad\searrow\\
\text{density-discrepancy parent}\quad
\text{signed-cone parent},
\end{array}
\]

with the existing edge from density-discrepancy to signed-cone retained.
Farther downstream, signed-cone feeds the physical M2 assembly, then
M9--M2, M9, the conditional bridge, and the target.

The new node depends only on the Round-164 node and has no dependency on
either parent or any downstream theorem. The Round-164 node does not gain
a dependency on the new node. Therefore no directed cycle is created.
The proposed obligation ID is absent from both the current obligations and
rejected-claim IDs.

## 4. First doubtful or unproved step

The sharpest open minimal-scale statement is (165.K17a). It asks for one
aggregate real-part estimate on even shifts, opposing tangent
displacements, and low character-divisor gcd, with all literal arithmetic
weights retained. The maximal-scale alternative (165.K26) is also open.

The exact parity connector does not estimate the even aggregate. The
monotone-sector count and high-gcd count leave the low-gcd opposing sector.
Large real phase derivatives do not control their distance from integers,
and positive rowwise dualization loses the signed interaction between
fibres or modes.

Accordingly:

- the complete residual is open;
- the accepted XOR scalar cannot be substituted for an XOR Fejer-energy
  theorem;
- completing the residual would still require a separate assembly before
  claiming the full \(t=1\) face;
- the other \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels and near collars are
  untouched; and
- neither hard-TOP parent is proved by a strict residual subsector.

No source theorem or numerical experiment supplies either missing
aggregate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Fresh obligation ID | **GREEN.** The proposed reduction ID occurs in neither current obligations nor rejected claims. |
| Strict sector versus open target | **GREEN.** The new node proves connectors and strict sectors; (165.K17a) and (165.K26) remain labelled open. |
| Parity connector | **GREEN.** It is endpoint-exact for even or odd \(R\) and introduces no odd-shift estimate. |
| Monotone sector ownership | **GREEN.** \(O(L^2)\) is across the complete shift union, not per shift. |
| High-gcd ownership | **GREEN.** It partitions opened divisor incidences, not product rows, and is target-safe only at fixed fractional threshold. |
| Variable-scale refinement | **GREEN.** All-\(R\) Fejer is exact; \(R_0\) is minimal diagonal-safe, while \(R=M_L\) yields a distinct open route. |
| Acyclicity | **GREEN.** New node depends on Round 164; parents depend on the new node; no reverse edge is added. |
| Parent evidence polarity | **GREEN.** Round-165 artifacts are positive only for the reduction and inconclusive for both parents. |
| Residual/full-\(t=1\) scope | **GREEN quarantine.** Neither is promoted. |
| Other few-point channels | **GREEN quarantine.** Their coefficients, fibres, and ranges are absent. |
| BAL/UNBAL | **GREEN quarantine.** Both smooth M2 parents are independent and unchanged. |
| M9--M2 and M9--M1 | **GREEN quarantine.** Neither fixed-coefficient reciprocal-sum theorem closes. |
| Endpoint, M9, bridge, quarter target | **GREEN quarantine.** All existing blockers remain. |
| Global exponent | **GREEN quarantine.** Internal \(1/3\) and external Li--Yang \(\theta_\ast\) remain unchanged. |
| Hostile arrays | **GREEN diagnostic scope.** They reject coefficient-uniform inference and give no literal physical lower bound. |
| Additive versus multiplicative geometry | **GREEN.** The gcd progressions are not the character-Poisson product collar. |
| Numerical experimentation | **NOT USED.** Review is entirely graph-theoretic and analytic. |

## 6. Dependencies and exact artifacts used

This review used the current terminal kernel, all Round-165 reports,
reviews, and proof candidates, the Round-164 terminal Fejer kernel/report,
and the relevant graph nodes in `state/proof_obligations.yml`. In
particular, the inspected graph nodes were:

- `M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction`;
- `M9-M2-top-endpoint-signed-cone`;
- `M9-M2-top-endpoint-density-discrepancy-energy`;
- `M9-M2-smooth-balanced-quarter-packet-estimate`;
- `M9-M2-smooth-unbalanced-three-quarter-estimate`;
- `M9-M2-physical-one-count-assembly`;
- `M9-M2`;
- `M9-M1`;
- `M9-endpoint-uniformity`;
- `M9`;
- `Conditional-bridge`;
- `GC-target`;
- `GC-partial-one-third`; and
- `GC-external-Li-Yang-theta-star`.

No shared proof state was edited. No external source, web search,
computation, or numerical experiment was used.

## 7. Recommended State Patch

### 7.1 Rejected claims

Add the following fresh rejected-claim records, each at Round 165 and with
the terminal kernel and this scope review as evidence:

1. `Round165-parity-connector-proves-residual-target`:
   the connector only replaces the full energy by a constant multiple of
   the even-gap energy; it does not estimate that energy.
2. `Round165-monotone-sector-cost-is-L2-per-shift`:
   the \(O(L^2)\) atom count is for the complete union over all shifts;
   adding a further factor \(R\) is double counting.
3. `Round165-strict-sectors-prove-complete-residual-or-full-t1`:
   the even, opposing, low-gcd aggregate remains open, and full-\(t=1\)
   assembly is not supplied.
4. `Round165-high-gcd-bound-proves-all-gcd-scales`:
   \(L^3/G_0\) reaches target size only for a fixed-fraction threshold
   \(G_0\asymp L\); the low-gcd complement remains.
5. `Round165-high-gcd-is-a-unique-product-row-partition`:
   the gcd split is owner-complete for opened divisor incidences; one
   product row can contain several divisor incidences.
6. `Round165-cofactor-character-alternates-on-even-shifts`:
   it is frozen on every even-shift row, including the squarefree
   even-even branch.
7. `Round165-large-real-derivative-gives-modulo-one-separation`:
   real derivative size does not bound distance to integers or
   half-integers.
8. `Round165-positive-row-Poisson-saves-the-target`:
   making the stationary modes positive is no better than the trivial row
   bound in the inherited range.
9. `Round165-positive-row-Poisson-no-go-rules-out-all-dual-methods`:
   the no-go covers only smooth row completion followed by absolute dual
   modes; coupled, signed, higher-order, and joint transforms remain open.
10. `Round165-odd-shift-alternation-proves-the-even-frontier`:
    the parity connector removes the need to estimate odd shifts and
    leaves the frozen-character even frontier.
11. `Round165-even-gap-energy-is-the-XOR-sector-energy`:
    it is an energy of the complete residual subsequences, not the
    accepted XOR scalar, and scalar smallness does not imply Fejer-energy
    control.
12. `Round165-XOR-scalar-bound-transfers-to-Fejer-energy`:
    a small scalar can have sliding energy \(\asymp M_LR\); a new energy
    connector would be required.
13. `Round165-variable-scale-identity-proves-the-medium-long-theorem`:
    the identity proves only that (165.K26) is sufficient; (165.K26) is
    open.
14. `Round165-short-shift-failure-terminates-the-Fejer-route`:
    the maximal-scale route pays the shortest shifts and moves the open
    cancellation requirement to medium/long even shifts.
15. `Round165-all-R-identity-makes-sub-L-windows-diagonal-safe`:
    the identity is valid for every \(R\), but the accepted diagonal
    reaches the target-square budget first at \(R\asymp L\).
16. `Round165-additive-gcd-fibres-equal-the-multiplicative-product-collar`:
    \(d'm'-dm=r\) is an additive physical product shift; the earlier
    character-Poisson collar is a different transformed geometry.
17. `Round165-hostile-arrays-disprove-the-literal-residual-target`:
    the cosine/sine and phase-aligned arrays are diagnostics outside the
    literal coefficient and prove no physical lower bound.
18. `Round165-K17a-or-K26-is-proved`:
    both displayed estimates are open sufficient theorems.
19. `Round165-strict-sector-proves-hard-TOP-or-M9-M2`:
    the complete residual, other few-point channels, BAL, and UNBAL remain
    open.
20. `Round165-reduction-proves-M9-or-quarter-target`:
    M9--M1, all three M9--M2 parents, endpoint uniformity, M9, and an
    unconditional bridge remain incomplete.
21. `Round165-reduction-improves-a-global-exponent`:
    no parent theorem or bridge closes, so neither the internal
    one-third theorem nor the external Li--Yang benchmark changes.

### 7.2 Explicit no-change list

Apart from the new reduction and the three scoped updates above, apply no
graph mutation. In particular:

| Obligation or interface | Required state after Round 165 |
|---|---|
| Round-164 residual Fejer reduction | Remains `proved_internal`; only its all-\(R\) refinement/evidence/next action changes. |
| `M9-M2-top-endpoint-signed-cone` | Remains `open`; only dependency and inconclusive evidence are appended. |
| `M9-M2-top-endpoint-density-discrepancy-energy` | Remains `open`; only dependency and inconclusive evidence are appended. |
| Complete residual and full \(t=1\) face | Open; no separate promotion. |
| Other hard-TOP few-point channels | Open and unchanged. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` | Remains `open`. |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | Remains `open`. |
| `M9-M2-physical-one-count-assembly` | Remains a proved reduction with all three analytic parents still required. |
| `M9-M2` | Remains `open`. |
| `M9-M1` | Remains `open`. |
| `M9-endpoint-uniformity` | Remains `open`. |
| `M9` | Remains `open`. |
| `Conditional-bridge` | Remains `derived_under_assumptions`. |
| `GC-target` | Remains `open`. |
| `GC-partial-one-third` | Remains the internal \(1/3\) theorem. |
| `GC-external-Li-Yang-theta-star` | Remains the external benchmark \((3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\). |

No evidence from Round 165 should be attached as positive evidence to any
node in this table except the new reduction and the refined Round-164
reduction. The two hard-TOP parents receive it only as inconclusive
evidence. No BAL, UNBAL, M9--M2, M9--M1, endpoint, M9, bridge, target, or
exponent evidence list should be changed.
