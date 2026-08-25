# Conductor Round-161 adjudication

## 1. Result and terminal decision

**Terminal verdict:
hard_top_radical_frequency_coupling_no_go.**

Round 161 does not prove the hard-TOP target or an owner-complete strict
polynomial range. It proves and promotes exactly two narrower results:

1. the literal radical-incidence dictionary, the complete fixed-constant
   long-channel sector \(D\le CL\), and the exact fixed-centre base/atom
   collision classification;
2. a route-scoped obstruction to coefficient-uniform common-test,
   Bessel, large-sieve, Hilbert-projective, and four named primary-source
   continuations on the remaining radical matrix.

The first unresolved physical face is the literal signed close-factor
sum

\[
 \left|\sum_{\substack{D\asymp L^2\\D>1\ {\rm squarefree}}}
 B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{161.A1}
\]

No physical lower bound is proved. Hard TOP, M9--M2, M9--M1, endpoint
uniformity, M9, the bridge, and the quarter theorem remain open. Neither
global exponent changes.

## 2. Exact accepted statements and hypotheses

Retain

\[
 \mathcal T_L^{\rm ns}
 =\sum_{\substack{D>1\\D\ {\rm squarefree}}}\sum_{t\ge1}
 B_D(t)e(tJ\sqrt D),
\tag{161.A2}
\]

\[
 B_D(t)\ne0\Longrightarrow
 c_-L^2\le Dt^2\le c_+L^2,
\tag{161.A3}
\]

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),\qquad
 \sum_t|B_D(t)|\ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{161.A4}
\]

The accepted incidence bijection is

\[
 h=gd_1u^2,\qquad m=gd_2v^2,\qquad
 D=d_1d_2,\qquad t=guv,
\tag{161.A5}
\]

where \(d_1,d_2\) are squarefree,
\((d_1u,d_2v)=1\), \(g,d_1,u\) are odd, and
\(d_2v^2\le d_1u^2\le4d_2v^2\), with every literal profile, endpoint,
support condition, and zero extension retained.

For every fixed \(C>0\),

\[
 \boxed{
 \left|\sum_{\substack{D\le CL\\D>1\ {\rm squarefree}}}
 \sum_tB_D(t)e(tJ\sqrt D)\right|
 \ll_{C,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{161.A6}
\]

This owns every fixed \(t\ge\tau\sqrt L\) sector, but not the whole
scalar for a strict polynomial \(L\)-range.

At one fixed \(J\), at most one channel has \(J\sqrt D\in\mathbb Q\).
The graph of exact base collisions

\[
 J(\sqrt{D_1}-\sqrt{D_2})\in\mathbb Z,\qquad D_1\ne D_2,
\tag{161.A7}
\]

has at most one unordered edge. All exact cross-channel atom relations

\[
 J(t_1\sqrt{D_1}-t_2\sqrt{D_2})=k,\qquad
 D_1\ne D_2,\quad k\ne0,
\tag{161.A8}
\]

use that same possible radical pair, with coefficient triples rationally
proportional. Trivial same-atom loops, nontrivial rational-channel
repetitions, and cross-channel relations are distinct cases. A rational
channel cannot coexist with a cross-channel relation. This is an exact
classification only; it proves no near-collision gap.

On \(t=1\), the literal coefficient is

\[
\begin{aligned}
B_D(1)=\mathbf 1_{D\asymp L^2}
\left(\frac{L^2}{D}\right)^{3/4}
\sum_{\substack{d_1d_2=D\\d_1\ {\rm odd}\\d_2\le d_1\le4d_2}}
&\chi_4(d_1)\eta_L(d_1)
\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right).
\end{aligned}
\tag{161.A9}
\]

The even-\(D\) branch survives through \(d_2\). No nonzero-row density,
lower envelope, or family lower mass is assumed.

## 3. Proof, reproduction, and review synthesis

Summing the second estimate in (161.A4) over \(D\le Z\) gives

\[
 \left|\sum_{D\le Z}\sum_tB_D(t)e(tJ\sqrt D)\right|
 \ll_\varepsilon(Z+L\sqrt Z)L^\varepsilon.
\tag{161.A10}
\]

Taking \(Z=CL\) proves (161.A6). Taking
\(Z=L^{1+\delta}\) instead costs
\(L^{3/2+\delta/2+\varepsilon}\), which confirms that the proof closes
only a sector.

The collision theorem follows from rational linear independence of
distinct squarefree radicals. Eliminating \(J\) between two relations
rules out disjoint pairs and one-index overlaps; a two-index overlap is
only repetition or reversal. The blind post-unmask review found one
statement seam: the first candidate did not explicitly separate
same-atom loops from nontrivial same-channel repetitions or display the
rational-channel shared-endpoint elimination. The candidate and discovery
report were repaired. The statement-only reviewer then rechecked the
local equations and returned GREEN. The repair changes no power or scope.

For \(Q\asymp L^2\) ambient squarefree rows, the \(t=1\) evaluation map

\[
 a\longmapsto(ae(J\sqrt D))_D
\]

has exact norm \(Q^{1/2}\asymp L\). The phase-aligned diagnostic

\[
 A_D(t)=\mathbf1_{t=1}e(-J\sqrt D)
\tag{161.A11}
\]

has nuclear norm \(Q^{1/2}\) and evaluation \(Q\). It obeys the accepted
coarse energy and row-mass scales, so those interfaces plus exact
collision sparsity cannot imply the target for arbitrary coefficients.
For the actual column, positive Cauchy gives only
\(L^2\sqrt{\log(2L)}\), leaving \(L^{1/2-o(1)}\).
The independent norm/power reviewer verified every normalization and
the real-array variant, and explicitly rejected any transfer of
(161.A11) to a physical lower bound for (161.A9).

The source seam independently checked the four primary PDFs:
Montgomery--Vaughan retains one common coefficient vector, including its
weighted clause; Bombieri--Iwaniec is separable and charges absolute
collision forms; Robert--Sargos Theorem 2 is a different real four-root
count, while Theorem 1 restores

\[
 J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2};
\tag{161.A12}
\]

and Miller requires coefficients of one fixed \(\mathrm{GL}(3)\) cusp
form. With \(N_0=1\), the exact Robert--Sargos phase normalization is
\(\Xi=JL/2\), hence \(\Xi\asymp JL\); (161.A12) is unchanged. Since
\(L\ll J^{1/2}\), its first term is at least \(L^2\). These facts park
only the named interfaces.

The downstream graph reviewer returned GREEN for exactly two new nodes
and updates to exactly the two open hard-TOP parents. It rejected reverse
edges into accepted Round-137 nodes and every downstream promotion.

## 4. First doubtful or unproved step

Equation (161.A1) is the first open physical statement. There is no
nontrivial \(t\)-sum on that face, exact spacing is irrelevant to the
one-coordinate test, and close semiprime singleton fibres provide no
family lower mass. A proof must exploit the actual \(\chi_4\)-weighted
close-factor structure of (161.A9), or establish an equivalent
alignment-sensitive theorem that fails on (161.A11).

Even a proof of (161.A1) would leave the compatible
\(L\ll D\ll L^2\), \(t\ll\sqrt L\) few-point channels and their
near-collision collars. No assigned artifact closes either layer.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Radical and incidence bijection | GREEN independently in discovery and statement-only reports. |
| Parity, cone, profiles, support, zero extension | GREEN; even \(D\) and even \(t\) retained. |
| Global energy and fixed-channel normalization | GREEN with no missing \(L,J,H,X\) power. |
| Long-channel sector | GREEN by (161.A10); explicitly not a strict owner range. |
| Exact collision classification | GREEN after loop/shared-endpoint repair and blind recheck. |
| Near collisions | OPEN; exact algebra supplies no gap or density estimate. |
| Literal \(t=1\) formula | GREEN; no physical density or lower mass inferred. |
| Projective/Bessel power | GREEN as a coefficient-interface obstruction only. |
| Primary-source hypotheses and powers | GREEN after exact PDF and parameter-map review. |
| Named-source versus global scope | GREEN quarantine; bespoke and unexamined routes remain open. |
| State graph direction | GREEN; two new nodes feed two open parents without cycles. |
| Numerical allocation | GREEN; 100% analytic/algebraic/source work, 0% experiment. |
| Downstream scope | GREEN; no target, range, M2, M1, endpoint, M9, bridge, or exponent promotion. |

## 6. Dependencies and exact artifacts used

The selected proof kernel is
proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md.

Primary reports:

- reports/literal_radical_frequency_attack.md;
- reports/blind_radical_frequency_rederivation.md;
- reports/square_root_spacing_source_hostile_audit.md.

Selected candidate and controls:

- candidates/conductor_round161_radical_control_and_obstruction.md;
- controls/conductor_round161_radical_capacity_controls.md.

Independent reviews:

- reviews/blind_post_unmask_radical_collision_review.md;
- reviews/blind_post_repair_radical_collision_review.md;
- reviews/projective_power_scope_review.md;
- reviews/source_power_seam_review.md;
- reviews/downstream_scope_graph_review.md.

Accepted antecedents are the Round-137 truncated-divisor
energy/radical-control node and its existing transform, character, and
square-sector dependencies. No computation or unreviewed source theorem
is used.

## 7. State decision and next action

Apply the validated State Patch as follows.

1. Create
   M9-M2-hard-top-radical-long-channel-exact-collision-control.
2. Create
   M9-M2-hard-top-radical-frequency-common-test-source-obstruction.
3. Add both as dependencies and Round-161 as inconclusive evidence only
   to M9-M2-top-endpoint-signed-cone and
   M9-M2-top-endpoint-density-discrepancy-energy; narrow their next
   actions to (161.A1) followed by the remaining few-point channels.
4. Reject the stronger readings listed in the State Patch.
5. Leave every accepted Round-137 node and every downstream theorem
   unchanged.

The next admissible round should freeze (161.A1) itself: the literal
\(\chi_4\)-weighted, squarefree, coprime, close-factor bilinear sum at one
fixed centre, with all profiles and hard endpoints retained. It must prove
that face, a genuinely owner-complete sector, or the first exact
character/Poisson/bilinear/source restored-power obstruction.
