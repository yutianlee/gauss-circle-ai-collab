# Hostile audit of intermediate-h discrete-curvature resonance averaging

- Campaign: m9-m1-top-block-intermediate-h-resonance
- Research round: 56 (intermediate_h_discrete_curvature_resonance)
- Task: resonance_spacing_hostile_audit
- Role: seam_reviewer
- Graph SHA-256 supplied in the brief: 7d2604d4c686e45d0348b1087741c812bb8943ee141db1d05aab22f84cb1dd11
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

**The proposed averaged discrete-quadratic-curvature closure is not
certified and, as presently specified, has no valid resonance majorant to
average.** On the residual large-curvature range \(h>\sqrt R\), each fixed
\(h\) interval contains

\[
 M_h\ll \frac Rh+1<\sqrt R+1
\tag{56.1}
\]

odd-\(q\) terms. After \(q=4m+\rho\), consecutive samples in one residue
fibre have product spacing \(4h\). Hence for \(h>R/4\) each residue fibre
contains at most one sample (apart from the endpoint convention at
\(4h=R\)); its second-difference parameter is vacuous. In the whole range
\(\sqrt R<h\le R/2\), the corrected third
derivative gives a locally almost constant real curvature, but a large
real value of that curvature says nothing on the integer lattice without
choosing a rational approximation (including its denominator) and proving
an \(h\)-averaged counting theorem for that exact parameter.

For \(q=4m+\rho\), \(\rho\in\{1,3\}\), the exact phase is

\[
 F_{h,\rho}(m)=\sqrt{Xh(4m+\rho)},
\tag{56.2}
\]

and its exact first and second differences are

\[
 \Delta F_{h,\rho}(m)
 =\frac{4\sqrt{Xh}}
 {\sqrt{4m+\rho+4}+\sqrt{4m+\rho}},
\tag{56.3}
\]

\[
 \Delta^2F_{h,\rho}(m)
 =-\frac{32\sqrt{Xh}}
 {\bigl(\sqrt{q+8}+\sqrt q\bigr)
  \bigl(\sqrt{q+8}+\sqrt{q+4}\bigr)
  \bigl(\sqrt{q+4}+\sqrt q\bigr)},
 \qquad q=4m+\rho.
\tag{56.4}
\]

Thus \(|\Delta^2F|\asymp h^2/R\), but only
\(\|\Delta^2F\|_{\mathbb R/\mathbb Z}\) or an explicitly selected rational
approximant can govern a discrete quadratic estimate. Perfect fourth powers
give exact first-difference resonances inside the actual range: with
\(X=K^4\), any odd \(K\), any odd \(a\ge3\), and

\[
 h=a^2,\qquad q_-=(K-a)^2,\qquad q_+=(K+a)^2,
\tag{56.5}
\]

one has \(q_+-q_-=4Ka\), both \(q_\pm\) odd, and

\[
 \sqrt{Xhq_+}-\sqrt{Xhq_-}=2K^2a^2\in\mathbb Z.
\tag{56.6}
\]

Hence the two endpoint phases are exactly coherent, although the
continuous curvature is large. Here \(Y=K^2\) and \(R\asymp K\). Choosing
\(a\asymp K^{1/4}=R^{1/4}\) puts \(h=a^2\asymp K^{1/2}=\sqrt R\) at the
large-curvature threshold, and the product separation
\(h(q_+-q_-)\asymp K^{7/4}\gg R\); therefore no single length-\(R\) product
window contains both points. This is a sharp warning against using global
\(q\)-completion or a macroscopic fixed-\(h\) resonance count as though it
were local to one product window. It is not a signed lower bound for
\(W_J^{\rm core}\).

The only theorem certified here is the narrow geometric reduction:
\(h\le L\) is the margin explicitly removed by Round 55. The new
large-curvature issue begins at \(h>\sqrt R\). Its upper portion
\(R/4<h\le R/2\), the maximum permitted by actual support, consists of
at-most-singleton residue fibres and requires a different signed incidence
argument. No
\(O_\varepsilon(X^\varepsilon\sqrt R)\) unweighted aggregate is proved.

## 2. Exact statement and hypotheses

Let \(I_Y\subset[cY,CY]\cap\mathbb Z\), with
\(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), and let
\(J\subseteq I_Y\) be consecutive with \(|J|\le R\). Retain the exact
physical coefficient

\[
 \Omega_X^*(hq,h)=\sum_j\mathbf 1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2\sqrt{Xh/q}\right)\right]^*,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor,
\tag{56.7}
\]

all profile and radial stars, and the actual support

\[
 q\ge4h,\qquad q\ge2\sqrt{hq},\qquad
 L<h\le\frac12\sqrt{hq}\asymp\sqrt Y=R.
\tag{56.8}
\]

For fixed \(h\), the condition \(hq\in J\) restricts \(q\) to one
interval of geometric length at most \(R/h\), hence to
\(O(R/h+1)\) integers. After either residue split it restricts \(m\) to
one interval with \(O(R/h+1)\) integers. Differentiating (56.2)
on this interval gives, with the packet's corrected normalization,

\[
 |F''_{h,\rho}(m)|\asymp\frac{h^2}{R},
 \qquad
 |F'''_{h,\rho}(m)|\asymp\frac{h^3}{R^3}.
\tag{56.9}
\]

Consequently

\[
 \sup_{m,m'\in K_h}|F''(m)-F''(m')|
 \ll \frac{h^2}{R^2},
\tag{56.10}
\]

and the relative change of curvature is \(O(1/R)\). This justifies a
constant-curvature approximation in the real topology; it does not select
a canonical representative modulo one or a rational denominator.

Any proposed quadratic Weyl/completion lemma must therefore state at
least: the exact finite interval; whether it uses the coefficient
\(F''/2\), the discrete difference \(\Delta^2F\), or another normalized
quantity; a coprime rational approximation \(a/b\) and its allowed
denominator range relative to \(M_h\); the perturbation tolerance including
(56.10); and every endpoint term introduced by completion. Without these
hypotheses, a symbol such as \(\|h^2/R\|^{-1}\) is not a lawful bound for
the original exponential sum.

The target after removing \((hq)^{-3/4}\asymp Y^{-3/4}\) remains

\[
 \left|\sum_{\substack{hq\in J,\ q\ {\rm odd}\\h>L}}
 \chi_4(q)\Omega_X^*(hq,h)e(\sqrt{Xhq})\right|
 \ll_\varepsilon X^\varepsilon\sqrt R.
\tag{56.11}
\]

For amplitude counterexamples one needs more than support and BV: one must
display a fixed subinterval on which an actual profile and its Vaaler taper
are bounded below, while avoiding every equality and hard edge. The graph
certifies active-profile sampled mass, height comparability, and
\(C^1\) Vaaler regularity, but the selected theorem statements do not give
the literal full-amplitude plateau, exact owner scale, and endpoint
inequalities needed to certify such a witness without importing an
unlisted construction. Accordingly this audit certifies only the
singleton-residue method capacity and does not claim an actual-profile signed
or absolute lower bound.

## 3. Proof or derivation

The identities (56.3)--(56.4) follow by rationalizing successive square
roots. Indeed, with \(A=\sqrt{q+8}\), \(B=\sqrt{q+4}\), and
\(C=\sqrt q\),

\[
 A-2B+C=(A-B)-(B-C)=\frac4{A+B}-\frac4{B+C}
 =-\frac{32}{(A+C)(A+B)(B+C)}.
\]

This proves the exact odd-lattice discrete phase and in particular shows
that the character split has changed the lattice step from one to four;
one may not use an unsplit \(q\)-difference normalization afterward.

For \(hq\asymp Y\) one has \(q\asymp Y/h\), so (56.4) has magnitude
\(\asymp\sqrt{Xh}\,q^{-3/2}\asymp h^2/R\). Taylor's theorem gives
(56.9). Since the \(m\)-interval has length \(O(R/h+1)\), the corrected
third derivative yields

\[
 |K_h|\sup|F'''|
 \ll \left(\frac Rh+1\right)\frac{h^3}{R^3}
 \ll\frac{h^2}{R^2}
\]

for \(h\le R\), proving (56.10). In particular, the earlier
\(h^3/R^2\) normalization would have overstated the curvature drift by a
factor \(R\).

The fibre geometry alone now splits the residual core into

\[
 L<h\le\sqrt R,\qquad
 \sqrt R<h\le R/4,\qquad
 R/4<h\le R/2.
\tag{56.12}
\]

The first range remains part of the aggregate problem; Round 55 removed
only \(h\le L\). In the middle range, a residue fibre has between \(O(1)\)
and \(O(\sqrt R)\) samples, so a discrete quadratic estimate could in
principle act, but only with its rational-approximation dependence exposed.
In the last range, \(4h>R\); each residue fibre has at most one sample,
with exact occupancy depending on endpoint convention and alignment. No
second-difference cancellation exists there. There are \(O(R)\) possible
\(h\)'s in the full supported range, so the available pointwise/trivial
ledger for the singleton-residue sector permits capacity as large as
\(R\), a factor \(\sqrt R\) above (56.11). This is an upper-method
obstruction, not a lower bound asserting that one fixed window realizes
\(R\) actual singleton incidences. Thus an averaged curvature argument
that treats \(R/4<h\le R/2\) by within-residue curvature cannot close the
target.

The perfect-fourth-power family (56.5) is exact. Both \(q_\pm\) are odd
when \(K,a\) are odd, and

\[
 \sqrt{Xhq_\pm}=K^2a(K\pm a),
\]

so (56.6) follows. Moreover, for \(a<K/3\),
\(q_-/h=((K-a)/a)^2>4\), hence \(q_\pm\ge4h\); and
\(h=a^2\le\frac12 a(K-a)=\frac12\sqrt{hq_-}\) once \(K\ge3a\).
Thus these are genuine support incidences. They can be placed away from
the top denominator boundary by taking \(a=o(K)\). But their product
separation is

\[
 h(q_+-q_-)=4Ka^3.
\tag{56.13}
\]

For \(a\asymp K^{1/4}\), \(R\asymp K\) and (56.13) is
\(\asymp K^{7/4}\gg R\). Thus the resonance is real on a completed or
macroscopic fixed-\(h\) interval and absent from every single allowed
short product window containing only one endpoint. Completion across that
gap introduces artificial endpoints; their weights are full cutoff
weights unless a separate symmetric inversion theorem supplies a half
weight. Inherited angular and radial stars cannot be reassigned to them.

On the actual amplitude, Round 55 supplies bounded sampled variation only
for each already truncated product window. It does not license global
variation after completing the \(q\)-interval or after pooling all
\(h\)-fibres. Any completion must retain (56.7), charge the two artificial
window boundaries, each encountered height/profile edge, the unique hard
top jump, and the independent inherited stars. The packet contains no
theorem bounding the aggregate of those completed boundary terms by
\(O(\sqrt R)\).

## 4. First doubtful or unproved step

The first unproved step is the passage from the exact real curvature
(56.4) to a fixed-\(h\) bound \(\mathcal R_X(h;J)\) whose rational or
modulo-one loss is explicit and uniform in the moving interval. Neither
the packet nor the accepted context states such a bound. In particular:

1. large \(|\Delta^2F|\) is not a discrete nonresonance hypothesis;
2. distance to the nearest integer alone does not cover rational
   coefficients with small denominator;
3. a Weyl bound requires the denominator and approximation error to be
   compared with the actual length \(M_h\), which itself depends on \(h\)
   and may be one;
4. completion beyond the physical interval creates boundary sums not
   controlled by the local sampled-BV statement.

Only after proving that fixed-fibre theorem could one formulate the next
missing statement: an average over \(\sqrt R<h\le R/4\) of its exact
rational-approximation loss, with the true \(h\)-dependent endpoints and
amplitudes. It would still need to be combined with the unresolved
\(L<h\le\sqrt R\) aggregate. Even that would leave the singleton-residue
range \(R/4<h\le R/2\), which needs
cancellation across distinct \(h\), products, or shifted incidences rather
than curvature within one fibre.

## 5. Control tests and outcomes

- **odd_q_discrete_phase -- pass.** Splitting \(q=4m+\rho\) makes
  \(\chi_4\) constant. Equations (56.3)--(56.4) are the exact step-four
  differences; an unsplit step-one curvature would have the wrong
  normalization.

- **large_curvature_mod_one -- fail as a proposed inference.** The real
  magnitude \(|\Delta^2F|\asymp h^2/R>1\) for \(h>\sqrt R\) does not imply
  cancellation. An explicit rational approximant and denominator-sensitive
  inequality are missing.

- **resonance_spacing_average -- open/no certified majorant.** Before an
  \(h\)-average can be audited, the resonance parameter and its fixed-fibre
  bound must be stated. The range \(R/4<h\le R/2\) has at most one sample
  per residue fibre, and the current pointwise ledger permits
  capacity \(R\); this is not an actual lower bound for a fixed window.

- **actual_profile_amplitude -- local pass, completion fail.** The exact
  coefficient has bounded sampled variation on each physical length-\(R\)
  product window by Round 55. That result does not supply global BV or
  completed boundary control across many \(h\)-dependent intervals. Nor
  does the selected context identify a star-free full-amplitude plateau
  adequate for a lower-bound witness.

- **hyperbola_window_edges -- fail for uncharged completion.** Each fixed
  \(h\) intersection is an interval, often of zero or one point. Enlarging
  it to a common or periodic interval introduces full artificial cutoff
  endpoints; inherited stars do not give them half weight.

- **perfect_fourth_power -- obstruction to phase-gap reasoning.** The
  actual-support family (56.5)--(56.6) has exact coherent endpoint phases.
  At \(a\asymp K^{1/4}\) it also proves that a macroscopic resonance may be
  separated by far more than the permitted product-window length, so it
  cannot be counted as a local two-point obstruction.

- **target_exponent_ledger -- fail/open.** The target is \(\sqrt R\)
  unweighted. The available trivial ledger in the singleton-residue sector
  permits \(R\), and no cross-fibre cancellation theorem is supplied.
  Nothing in the current resonance proposal recovers the missing factor
  \(\sqrt R\).

- **low_leg_overlap -- pass.** Round 55 removes exactly \(h\le L\). A
  large-curvature average begins at \(h>\sqrt R\), while a full core
  theorem must also own \(L<h\le\sqrt R\) exactly once.

- **alpha_scope -- no transfer.** This is a physical radial audit.
  Alpha masks, finite connectors, Plemelj order, and outside-height limits
  do not occur in the proof and receive no estimate.

- **downstream_scope -- no implication.** The report proves neither the
  residual window bound, the full signed shifted correlation, GAR, M9-M1,
  M9, nor a Gauss-circle exponent.

No numerical, symbolic, web, or unlisted-source experiment was used.

## 6. Dependencies and exact artifacts used

This report used only the brief and its permitted selected context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/derivation_packet.md, with the conductor's corrected \(|F'''|\asymp h^3/R^3\);
- rounds/codex-managed/m9-m1-top-block-low-leg-curvature/synthesis.md;
- rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md;
- the Round-56 hostile-audit brief.

The imported facts were the exact physical coefficient and support, the
Round-55 short-window sampled-BV and low-leg theorem, the target
normalization, and the Round-54 shifted-correlation scope. The exact
odd-lattice differences, fibre split, corrected curvature-drift estimate,
fourth-power resonance family, locality test, and exponent obstruction
were derived directly. No other Round-56 report, proof draft, legacy
artifact, or external theorem was read.

## 7. Recommended state effect

**Do not promote an averaged-resonance estimate or the residual-core
bound.** Retain (56.3)--(56.4) as an exact discrete-phase reduction and
record the following scoped obstruction:

1. large real curvature beyond \(\sqrt R\) is not a lattice cancellation
   theorem without a denominator-sensitive rational approximation;
2. the corrected third derivative is \(h^3/R^3\), so curvature is nearly
   constant on one physical fibre, but that does not remove rational
   resonances;
3. actual support ends at \(h\asymp R/2\), and for \(R/4<h\le R/2\)
   each residue fibre is at most a singleton, so within-fibre quadratic
   curvature cannot act;
4. the explicit fourth-power family (56.5) gives exact phase coherence on
   actual support, while (56.13) shows why a global resonance cannot be
   silently localized to a length-\(R\) product window;
5. completion requires new full boundary owners and cannot borrow half
   weights from inherited stars.

The next prerequisite, if this mechanism is retained, is a precisely
stated denominator-sensitive fixed-fibre Weyl lemma for
\(\sqrt R<h\le R/4\), followed by a proof of its \(h\)-averaged loss and a
compatible estimate for \(L<h\le\sqrt R\); this report does not begin that
next round. Keep the singleton-residue range, residual
core, full shifted correlation, GAR, alpha transfer, M9-M1, M9, and the
Gauss-circle target open.
