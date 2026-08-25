# Round 161 downstream and graph-scope review

## 1. Result and verdict

**Verdict: GREEN.** The narrowest legitimate proof-state effect is to
create exactly two proved internal nodes:

1. a hard-TOP radical long-channel and exact-collision control lemma;
2. a hard-TOP radical-frequency common-test and named-source route
   obstruction.

Only the two existing open hard-TOP owners
`M9-M2-top-endpoint-signed-cone` and
`M9-M2-top-endpoint-density-discrepancy-energy` may receive both new
nodes as dependencies, the Round-161 artifacts as **inconclusive** parent
evidence, and narrowed `next_action` text. Their statements, statuses,
blockers, and implication edges remain unchanged.

The first new node proves an owner-complete **sector**: every fixed
\(D\le CL\), equivalently every fixed \(t\ge \tau\sqrt L\), sector is
target-safe, and every nontrivial exact collision is confined to at most
one radical pair. It does not prove an owner-complete strict polynomial
range of \(L\). The second node proves only that coefficient-uniform
common-test/projective/Bessel placement and the named audited source
interfaces do not close the remaining scalar from the accepted positive
controls. It is not a lower bound for the literal coefficient and not a
global impossibility theorem.

No hard-TOP target, M9-M2 parent, downstream theorem, or exponent changes.

## 2. Exact statement and hypotheses

Retain one literal nonsquare polynomial-intermediate hard-TOP block, with

\[
 J=\sqrt X,\qquad 1\ll L\ll H,
\]

and

\[
 \mathcal T_L^{\rm ns}
 =\sum_{D>1\ {\rm squarefree}}\sum_{t\ge1}
 B_D(t)e(tJ\sqrt D),
 \qquad
 B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2)
 \mathbf 1_{Dt^2\asymp L^2}.
\tag{G.1}
\]

There are fixed support constants \(0<c_-<c_+\) such that

\[
 B_D(t)\ne0\Longrightarrow c_-L^2\le Dt^2\le c_+L^2,
\tag{G.2}
\]

and the accepted Round-137 controls are

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),
 \qquad
 \sum_t|B_D(t)|\ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{G.3}
\]

No positivity, lower envelope, density of nonzero rows, common coefficient
vector, bounded variation, near-collision separation, or Diophantine
hypothesis on the arbitrary fixed real centre \(J\) is assumed.

The proposed first node should state the following and no more.

* The literal incidence map is bijective:
  \[
  h=gd_1u^2,\quad m=gd_2v^2,\quad D=d_1d_2,\quad t=guv,
  \tag{G.4}
  \]
  where \(d_1,d_2\) are squarefree,
  \((d_1u,d_2v)=1\), \(g,d_1,u\) are odd, and
  \(d_2v^2\le d_1u^2\le4d_2v^2\), with all literal profiles,
  endpoints, support, and zero extension retained.
* For every fixed \(C>0\),
  \[
  \left|\sum_{D\le CL\ {\rm sf}}\sum_t
  B_D(t)e(tJ\sqrt D)\right|
  \ll_{C,\varepsilon}L^{3/2}X^\varepsilon.
  \tag{G.5}
  \]
  By (G.2), this contains every fixed \(t\ge\tau\sqrt L\) sector,
  and conversely \(D\le CL\) forces
  \(t\ge\sqrt{c_-/C}\sqrt L\).
* At most one radical channel has \(J\sqrt D\in\mathbb Q\). The base
  collision graph
  \(J(\sqrt{D_1}-\sqrt{D_2})\in\mathbb Z\), \(D_1\ne D_2\),
  has at most one unordered edge. All exact cross-channel atom relations
  \[
  J(t_1\sqrt{D_1}-t_2\sqrt{D_2})=k,
  \qquad D_1\ne D_2,\quad k\ne0,
  \tag{G.6}
  \]
  use at most one unordered radical pair, and their integer triples are
  rational multiples of one primitive relation after orientation. A
  rational channel cannot coexist with such a cross-channel relation.
  A same-channel equality with \(t_1=t_2\) is the trivial loop; a
  nontrivial same-channel repetition requires the unique possible
  rational channel. Every channel occurring in this exact classification
  is target-safe by (G.3). No near-collision conclusion is included.

The proposed second node should retain the exact \(t=1\) face

\[
\begin{aligned}
B_D(1)={}&\mathbf 1_{D\asymp L^2}
\left(\frac{L^2}{D}\right)^{3/4}
\sum_{\substack{d_1d_2=D\\d_1\ \text{odd}\\d_2\le d_1\le4d_2}}
 \chi_4(d_1)\eta_L(d_1)
 \Phi\!\left(\frac{d_1}{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right),
\end{aligned}
\tag{G.7}
\]

including the even-\(D\) branch through \(d_2\), and state only this
route obstruction:

* on \(Q\asymp L^2\) ambient squarefree rows, the one-column common-test
  evaluation norm is exactly \(Q^{1/2}\asymp L\);
* the phase-aligned diagnostic
  \(A_D(t)=\mathbf1_{t=1}e(-J\sqrt D)\) has nuclear norm
  \(Q^{1/2}\asymp L\) and saturates the resulting \(L^2\) capacity;
* therefore support, (G.3), exact-collision sparsity, and a
  coefficient-uniform common-test/projective/Bessel theorem do not imply
  the \(L^{3/2}X^\varepsilon\) target;
* the audited Montgomery--Vaughan, Bombieri--Iwaniec,
  Robert--Sargos, and Miller interfaces do not legally supply the missing
  literal coefficient theorem. Even after a fictitious cost-one
  separation, direct Robert--Sargos restores
  \(X^{1/8}L^{3/2}+L^{7/4}\), whose best combination with triviality is
  still \(L^2\) for \(L\ll H\).

The diagnostic array is not (G.7), and the source conclusion is limited
to those named theorem statements and parameter maps.

## 3. Proof, graph derivation, and scope audit

From (G.3), for \(Z\ge2\),

\[
 \left|\sum_{D\le Z\ {\rm sf}}\sum_t
 B_D(t)e(tJ\sqrt D)\right|
 \le L^\varepsilon\sum_{D\le Z}
 \left(1+\frac L{\sqrt D}\right)
 \ll (Z+L\sqrt Z)L^\varepsilon.
\tag{G.8}
\]

Taking \(Z=CL\) proves (G.5). Taking
\(Z=L^{1+\delta}\) instead gives only the upper capacity
\(L^{3/2+\delta/2+\varepsilon}\). It neither proves that the physical
sum is large nor closes the complete scalar for a strict polynomial
range of \(L\). Thus the target-safe sector and an owner-complete
strict \(L\)-range are different graph claims.

The exact collision theorem follows from rational linear independence of
distinct squarefree radicals. Eliminating \(J\) between two collision
relations produces a rational relation among four, three, or two
radicals. Disjoint pairs and one-endpoint overlaps are impossible; a
two-endpoint overlap is repetition or reversal. The repaired atom
statement separately treats trivial loops, nontrivial rational-channel
repetitions, and cross-channel relations with nonzero collision integer.
This algebra is qualitative. It supplies no positive lower bound for a
nonzero modulo-one distance and hence no estimate for a collar at the
moving resolution \(1/|I_D|\).

For the route obstruction, the one-column operator sends
\(a\in\mathbb C\) to \((ae(J\sqrt D))_D\), so its norm is exactly
\(Q^{1/2}\), independently of frequency spacing. The aligned diagnostic
has the same coarse support, \(L^2\)-energy scale, and unit channel mass
per row permitted by (G.3), and it makes the Hilbert-projective/Bessel
inequality sharp at \(Q\asymp L^2\). This proves a theorem-interface
capacity obstruction. It does not show that the literal values in (G.7)
are nonzero on \(Q\) rows, have large energy, align with the phase, or
produce a scalar lower bound. Route capacity and physical lower mass must
remain separate in the graph.

The source audit is similarly one-directional. Montgomery--Vaughan tests
one common coefficient vector; Bombieri--Iwaniec and the relevant
Robert--Sargos interfaces require separable coefficients and charge
positive collision/projective norms; Robert--Sargos' four-root count is
not the fixed-centre modulo-one collision statement; Miller requires the
Fourier coefficients of a fixed automorphic form. These are exact
no-matches for the named uses. They do not exclude a new signed theorem
for (G.7), a bespoke vector theorem acting on the literal matrix before
positive norms, or another future source with matching hypotheses.

For graph acyclicity, the first new node should depend only on the
accepted Round-137 truncated-divisor energy/radical-control node (whose
existing dependencies already own the transform and square removal).
The second should depend on that Round-137 node and the first new node.
Neither new node should depend on either open parent to which it is
attached. No reverse edge into an accepted Round-137 node is needed.

## 4. First doubtful or unproved step

After the long-channel sector and the finitely many exact-collision
channels are removed, the first unproved physical estimate is

\[
 \boxed{
 \left|\sum_{D\asymp L^2\ {\rm sf}}
 B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{G.9}
\]

The literal coefficient here is (G.7), not an arbitrary row factor.
The accepted energy and positive outer Cauchy give only
\(L^{2+o(1)}\), while exact collision sparsity is irrelevant to a
one-coordinate test. No physical lower mass is known, so (G.9) remains
a possible theorem. Even a proof of (G.9) would leave the compatible
few-point sector \(L\ll D\ll L^2\), \(t\ll\sqrt L\), including its
near-collision collars.

At graph level, the first impermissible step would be to treat either new
node as implying the open signed cone or completed density-discrepancy
estimate. The latter remains connected to the product-fibre scalar only
through its already accepted one-count and real-part owners. Adding a
dependency records a required structural control; it does not create a
new implication or close the parent.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Target-safe sector versus strict \(L\)-range | **Green separation.** \(D\le CL\), equivalently fixed \(t\gtrsim\sqrt L\), is complete only as a channel sector. Every polynomial intermediate block still contains \(D\gg L\), including \(t=1,D\asymp L^2\). |
| Exact versus near collisions | **Green exact/open near.** The global exact graph has at most one unequal edge and one rational channel, with the repaired loop split. No gap, local-density, or collar theorem follows. |
| Route capacity versus physical lower bound | **Green quarantine.** The \(L^2\) one-column saturation concerns an adversarial coefficient interface. It gives no density, lower energy, sign alignment, or scalar lower bound for (G.7). |
| Named-source no-match versus global impossibility | **Green quarantine.** Only the audited Montgomery--Vaughan, Bombieri--Iwaniec, Robert--Sargos, and Miller maps are parked. Bespoke coefficient-sensitive or vector theorems remain logically open. |
| Literal normalization and parity | **Green.** The \((L^2/D)^{3/4}\) factor, hard cone, profiles, zero extension, even \(D\) through \(d_2\), and even \(t\) through \(v\) are retained. |
| Missing power | **Green as route capacity.** Positive common-test placement stops at \(L^{2+o(1)}\), leaving \(L^{1/2-o(1)}\); this is not a physical lower bound. |
| Parent evidence classification | **Green.** Round-161 artifacts are positive evidence for the two new proved nodes but only inconclusive evidence for the still-open hard-TOP parents. |
| Dependency direction and cycles | **Green.** New nodes point from accepted Round-137 controls toward the two open parents; no parent-to-child or reverse accepted-node mutation is required. |
| Downstream quarantine | **Green.** The result is restricted to the one nonsquare polynomial-intermediate hard-TOP block. |

No numerical or symbolic experiment is needed for this graph decision.

## 6. Dependencies and exact artifacts used

This review read `AGENTS.md`, `protocol.md`,
`state/proof_obligations.yml`, and `state/active_campaign.yml`, together
with every currently completed Round-161 candidate, report, control, and
review:

- `candidates/conductor_round161_radical_frequency_seed.md`;
- `candidates/conductor_round161_radical_control_and_obstruction.md`;
- `reports/literal_radical_frequency_attack.md`;
- `reports/blind_radical_frequency_rederivation.md`;
- `reports/square_root_spacing_source_hostile_audit.md`;
- `controls/conductor_round161_radical_capacity_controls.md`;
- `reviews/blind_post_unmask_radical_collision_review.md`;
- `reviews/blind_post_repair_radical_collision_review.md`;
- `reviews/projective_power_scope_review.md`.

The Round-137 accepted graph nodes read were
`M9-M2-hard-top-truncated-divisor-energy-and-radical-control`,
`M9-M2-hard-top-product-fibre-transform-self-return`,
`M9-M2-hard-top-product-fibre-mean-obstruction`, and
`M9-M2-hard-top-square-product-entry-sector`, together with the two open
hard-TOP parent nodes. Their accepted evidence was checked through the
Round-137 discovery, blind, and hostile reports; the three post-unmask
reviews; the conductor candidate and adjudication; the synthesis; and the
applied State Patch. No web lookup, external computation, or shared-state
edit was made.

## 7. Recommended state effect

Create the following two nodes, with no `implies` edge and no blocker
change elsewhere.

1. `M9-M2-hard-top-radical-long-channel-exact-collision-control`
   (`lemma`, `proved_internal`). Its statement should be exactly the
   incidence bijection, (G.5), the base/atom exact-collision
   classification, the target-safe absolute capacity of the involved
   channels, and the explicit exclusion of near collisions. Its minimal
   dependency is
   `M9-M2-hard-top-truncated-divisor-energy-and-radical-control`.
2. `M9-M2-hard-top-radical-frequency-common-test-source-obstruction`
   (`obstruction`, `proved_internal`). Its statement should be exactly
   (G.7), the one-column evaluation/nuclear-norm capacity, the
   nonphysical diagnostic qualification, the named-source hypothesis and
   restored-power no-matches, and the explicit allowance for a future
   actual-coefficient or bespoke vector theorem. Its dependencies should
   be the preceding new node and
   `M9-M2-hard-top-truncated-divisor-energy-and-radical-control`.

Use the Round-161 discovery and blind reports, repaired conductor
candidate, controls, source-audit report, GREEN post-repair and
projective reviews, and this review as positive evidence for the
appropriate new node. Retain the original pre-repair collision review as
superseded repair provenance rather than as a green terminal review.

Update only these open nodes:

* `M9-M2-top-endpoint-signed-cone`: add both new dependencies and add
  the Round-161 artifacts as inconclusive evidence. Narrow `next_action`
  to the literal fixed-centre signed estimate (G.9), then the remaining
  \(D\gg L,t\ll\sqrt L\) few-point channels and their near-collision
  collars; park coefficient-uniform common tests and the named audited
  source routes.
* `M9-M2-top-endpoint-density-discrepancy-energy`: add both new
  dependencies and the same evidence classification. Its `next_action`
  must preserve the existing one-count/real-part connector and require a
  coefficient-sensitive signed theorem for the remaining short channels
  before any transfer back to the completed energy. Do not call the
  long-channel sector or the obstruction an estimate for the completed
  real part.

Record or preserve rejections of the following stronger readings:

* the long-channel sector is an owner-complete strict polynomial
  \(L\)-range;
* exact collision sparsity controls near-collision collars;
* the one-column/projective capacity is a physical lower bound for
  \(B_D(1)\);
* the named-source no-match rules out every future joint theorem;
* the direct Robert--Sargos ledger gives a strict hard-TOP range; or
* this route obstruction closes hard TOP, M9-M2, or improves an exponent.

Leave unchanged the statements and statuses of the accepted Round-137
nodes and the square-entry owner. Also leave unchanged
`M9-M2-physical-one-count-assembly`, both smooth M2 packet estimates,
`M9-M2`, every M9-M1 owner, `M9-endpoint-uniformity`, `M9`,
`Conditional-bridge`, `GC-target`, `GC-partial-one-third`, and
`GC-external-Li-Yang-theta-star`. No full hard-TOP bound, BAL or UNBAL
bound, endpoint assembly, quarter theorem, internal exponent, or external
benchmark is promoted.
