# Hostile audit of top-block low-leg curvature

- Campaign: m9-m1-top-block-low-leg-curvature
- Research round: 55 (top_block_low_leg_curvature)
- Task: top_margin_hostile_audit
- Role: seam_reviewer
- Graph SHA-256 supplied in the brief: 4efbecf244fa2c1f071a7fd2fe5c1eda0ba2596d51c4c873eefc0b47ffca211f
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

**The proposed low-leg margin estimate is valid in its stated linear
\(H+Q\) form.** Let \(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), and let
\(J\subseteq I_Y\) be any consecutive product interval of length at most
\(R\), including a window truncated by a radial hard endpoint. Then

\[
 \left|\sum_{n\in J}^{*}
 A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon X^\varepsilon\frac{H+Q}{\sqrt Y}.
\tag{55.1}
\]

The implied constant depends only on the fixed compact radial block, the
profile seminorms, and the fixed Vaaler profile. It is uniform in the
positions of \(J\), all height floors, angular equality stars, and \(X\),
including \(X=K^4\). Consequently the accepted moving-window implication
gives

\[
 S_{Y;H,Q}\ll_\varepsilon X^\varepsilon(H+Q).
\tag{55.2}
\]

The key fixed-leg bound is \(O(\sqrt R)\), not
\(O(\sqrt R/\ell+\sqrt\ell)\). For a fixed leg \(\ell=h\) or \(q\), the
second-derivative test gives

\[
 \left(\frac R\ell+1\right)\frac\ell{\sqrt R}
 +\frac{\sqrt R}{\ell}
 =\sqrt R+\frac\ell{\sqrt R}+\frac{\sqrt R}{\ell},
\tag{55.3}
\]

which is \(O(\sqrt R)\) for \(1\leq\ell\leq\sqrt R\). For
\(\ell>\sqrt R\), the trivial length is
\(R/\ell+O(1)=O(\sqrt R)\). Thus the packet's crossover at
\(\ell\asymp\sqrt R\) is the lawful one. Restoring
\(n^{-3/4}\asymp Y^{-3/4}\) turns \(\sqrt R\asymp Y^{1/4}\) into exactly
\(Y^{-1/2}\) per fixed leg, yielding (55.1).

The theorem is unaffected by integer or half-integer first-derivative
resonances: its hypothesis is nonzero one-signed curvature, which remains
valid. The low-margin union is owned disjointly by

\[
 \{h\leq H\}\ \dot\cup\ \{h>H,\ q\leq Q\}.
\tag{55.4}
\]

The exact complement, and the first genuinely two-variable problem, is

\[
 h>H,\qquad q>Q,\qquad q\text{ odd},\qquad hq\in I_Y.
\tag{55.5}
\]

## 2. Exact statement and hypotheses

Assume \(I_Y\subset[cY,CY]\cap\mathbb Z\) is consecutive for fixed
\(0<c<C\), \(Y\asymp\sqrt X\), and \(R\asymp\sqrt Y\). Retain exactly

\[
 \Omega_X^*(hq,h)=
 \sum_j {\bf1}_{h\leq H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2\sqrt{\frac{Xh}{q}}\right)\right]^*,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor,
\tag{55.6}
\]

and the coefficient in the packet, with \(q\) odd and the factor
\(\chi_4(q)\). The permitted profile hypotheses are: dyadic supports with
bounded overlap; uniformly bounded normalized \(C^1\) seminorms for
interior profiles; one separately retained one-sided hard-top jump; and
bounded profile values. Also \(\Phi\in C^1[0,1]\) with bounded norm and
derivative. A profile equality star changes only its equality value; it is
not identified with the hard jump. A radial endpoint star is multiplied
outside the angular coefficient.

On any ordered fixed-leg lattice interval \(K\), write

\[
 \|a\|_{\mathrm{SBV}(K)}
 :=\sup_{u\in K}|a_u|+
 \sum_{u,u^+\in K}|a_{u^+}-a_u|.
\tag{55.7}
\]

Here \(u^+\) is the next lattice point; for fixed \(h\) and a split
residue class it is the next \(q\equiv1\) or \(3\pmod4\). The required
amplitude assertion is

\[
 \|\Omega_X^*(hq,h)\|_{\mathrm{SBV}(K)}\ll1
\tag{55.8}
\]

both as \(q\) varies with \(h\) fixed and as \(h\) varies with odd \(q\)
fixed. Section 3 derives (55.8), rather than assuming it.

The analytic input is the finite-interval second-derivative estimate: if
\(f''\) has one sign and \(\lambda\leq|f''|\leq C_0\lambda\), then, uniformly
on every subinterval,

\[
 \left|\sum_{m\in K}e(f(m))\right|
 \ll_{C_0}|K|\lambda^{1/2}+\lambda^{-1/2}.
\tag{55.9}
\]

Partial summation transfers (55.9) through an amplitude with bounded
sampled sup-plus-variation. No first-derivative separation from integers is
a hypothesis.

## 3. Proof or derivation

Put

\[
 d(h,q)=2\sqrt{\frac{Xh}{q}}=2h\sqrt{\frac X{hq}}.
\tag{55.10}
\]

On a product window \(hq\in J\subset[cY,CY]\) of length at most \(R\),
the variable product changes relatively by \(O(R/Y)\). Hence, for either
fixed leg, \(d(h,q)\) is monotone and

\[
 \frac{d_{\max}}{d_{\min}}=1+O(R/Y).
\tag{55.11}
\]

The dyadic supports are separated by a fixed ratio, so the union of all
profile indices encountered along this short path has cardinality \(O(1)\).
For each such index, monotone composition with a normalized \(C^1\) profile
has bounded sampled variation. The top profile contributes its one full
hard jump. Each starred profile equality can alter at most one value per
boundary on a monotone path and therefore adds only \(O(1)\) variation.

For fixed \(h\), every factor
\({\bf1}_{h\leq H_j}\Phi(h/(H_j+1))\) is constant in \(q\). For fixed
odd \(q\), extend

\[
 b_j(h)={\bf1}_{h\leq H_j}\Phi(h/(H_j+1))
\]

by zero past \(H_j\). Its smooth part has variation at most
\(\|\Phi'\|_\infty\), and the transition from \(H_j\) to \(H_j+1\) adds
one bounded full jump. Thus \(\|b_j\|_{\mathrm{SBV}}\ll1\), uniformly in
the floor \(H_j\). The product variation inequality and the \(O(1)\)
encountered indices prove (55.8) in both directions. This also shows why a
hard top edge, a height floor, and an equality star must be counted as
three distinct owners even though all cost only a constant here.

Now fix \(h\leq\sqrt R\). Split the odd \(q\)'s into the two classes
\(q=4m+\rho\), \(\rho\in\{1,3\}\), so that \(\chi_4(q)\) is constant.
The \(m\)-interval has length \(N_h\ll R/h+1\), and

\[
 F_{h,\rho}(m)=\sqrt{Xh(4m+\rho)},
 \qquad |F_{h,\rho}''(m)|\asymp\frac{h^2}{R}
\tag{55.12}
\]

with one sign. Applying (55.9) on every partial interval gives

\[
 |T_h|
 \ll \left(\frac Rh+1\right)\frac h{\sqrt R}
       +\frac{\sqrt R}{h}
 \ll\sqrt R.
\tag{55.13}
\]

Partial summation and (55.8) preserve this estimate. If
\(h>\sqrt R\), the number of admissible \(q\)'s is
\(O(R/h+1)=O(\sqrt R)\), so the trivial estimate gives (55.13) without
using curvature.

For fixed odd \(q\leq\sqrt R\), the \(h\)-interval has length
\(N_q\ll R/q+1\) and

\[
 G_q(h)=\sqrt{Xqh},
 \qquad |G_q''(h)|\asymp\frac{q^2}{R}.
\tag{55.14}
\]

The same computation gives \(|T_q|\ll\sqrt R\). For \(q>\sqrt R\),
trivial summation does so. Multiplication by the monotone radial weight and
any radial endpoint half-star changes the sampled norm by
\(O(Y^{-3/4})\). Therefore each fixed leg contributes

\[
 \ll Y^{-3/4}\sqrt R\asymp Y^{-1/2}.
\tag{55.15}
\]

Use the disjoint owner (55.4): first sum (55.15) over at most \(H\)
fixed-\(h\) legs, then over at most \(Q\) fixed-\(q\) legs subject to
\(h>H\). This proves (55.1), without an overlap term. Finally partition
\(I_Y\) into at most \(\lceil |I_Y|/R\rceil\ll Y/R\asymp\sqrt Y\)
consecutive intervals of length at most \(R\). The last interval may be an
edge interval and is already covered. Summing (55.1) over this exact
partition proves (55.2). This direct triangle-inequality transfer has the
same exponent ledger as the accepted moving-window implication and avoids
claiming an additional Fejer estimate.

At \(X=K^4\), the resonance threat is real but harmless. If \(K\) is odd,
\((h,q)=(1,K^2)\) lies on the top product \(hq=K^2=\sqrt X\) and

\[
 \frac{\partial}{\partial q}\sqrt{Xhq}=\frac K2
\]

is half-integral. If \(K=2L\) with \(L\) odd, then
\((h,q)=(4,L^2)\) has the same top product and the derivative is
\(4L\), an integer. In the fixed-\(q\) direction, \(q=1,h=K^2\) gives
derivative \(K/2\), half-integral for odd \(K\) and integral for even
\(K\). Also \(e(\sqrt{XK^2})=e(K^3)=1\). These examples rule out a
uniform first-derivative-gap proof. They do not affect (55.12) or (55.14),
whose second derivatives remain nonzero and one-signed on the entire
window.

## 4. First doubtful or unproved step

The first unproved step after (55.1) is cancellation in the exact balanced
core (55.5). Fixed-leg curvature alone is not summable over all
\(h,q\asymp Y\) incidences at target size: it gives \(O(\sqrt R)\) per
leg, and the balanced range contains polynomially many legs. A new signed
bilinear, character-sensitive, or shifted-correlation theorem is required
there.

This physical top-block margin estimate also does not provide the separate
finite connector/Plemelj and outside-height argument required for the alpha
operator. Nor does it estimate the complete Round-54 shifted correlation;
it permits the original radial sum to be decomposed into a controlled
margin plus the balanced core before that correlation problem is attacked.

No step inside the scoped low-margin theorem remains unproved under the
profile and Vaaler hypotheses frozen in the packet.

## 5. Control tests and outcomes

- **fixed_leg_phase -- pass.** On fixed \(h\), splitting
  \(q\equiv1,3\pmod4\) makes \(\chi_4\) constant and retains the exact
  square-root phase. On fixed odd \(q\), the character is already constant.
  Equations (55.12) and (55.14) have the required one-signed curvature.

- **curvature_trivial_crossover -- pass.** Formula (55.3), not a
  \(\sqrt\ell\) term, is the lawful curvature ledger. It is
  \(O(\sqrt R)\) up to \(\ell=\sqrt R\); above that point the interval
  length is \(O(\sqrt R)\). The packet's threshold is correct.

- **sampled_profile_BV -- pass on every length-\(R\) product window.**
  Monotonicity, (55.11), dyadic separation, bounded overlap, and normalized
  profile variation imply that only \(O(1)\) bounded-variation pieces are
  encountered. No macroscopic fixed-leg BV claim is used.

- **height_floor_and_stars -- pass with separate owners.** On fixed
  \(h\), height factors are constant. On fixed \(q\), each encountered
  floor contributes at most one full cutoff jump and a bounded \(C^1\)
  taper. A profile equality changes one sampled value; the hard-top cutoff
  contributes a full jump. Neither is conflated with a radial half-star.

- **moving_window_edges -- pass.** Every fixed-leg intersection with
  \(J\) is an interval, and (55.9) is uniform on all subintervals. A radial
  endpoint star changes at most an endpoint value per fixed leg. The final
  remainder in the partition of \(I_Y\) is covered by the same estimate.

- **perfect_fourth_power -- pass for curvature; derivative-gap route
  falsified.** The explicit top-product examples above realize integer and
  half-integer derivatives, and even an integral phase, while the second
  derivative stays of size \(h^2/R\) or \(q^2/R\).

- **H_Q_ledger -- pass.** Each of at most \(H+Q\) disjoint fixed legs costs
  \(Y^{-3/4}\sqrt R\asymp Y^{-1/2}\), proving exactly the linear ledger in
  (55.1). For \(H+Q\leq(\log(2X))^B\), (55.2) is absorbed by
  \(X^\varepsilon\).

- **double_counting -- pass.** The disjoint rule (55.4) assigns every
  \(h\)-low/\(q\)-low overlap to the \(h\)-low family exactly once.

- **balanced_core_scope -- open and exact.** The remaining pairs are
  precisely (55.5), with the original character, profile sum, floors, and
  stars retained.

- **downstream_scope -- no implication.** The result does not close the
  balanced shifted correlation, GAR, the alpha transfer, M9-M1, M9, or the
  Gauss-circle target.

No numerical, symbolic, or web experiment was used.

## 6. Dependencies and exact artifacts used

This report used only the task brief and its permitted selected context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-top-block-low-leg-curvature/derivation_packet.md;
- rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md;
- rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/reports/coupled_scale_hostile_audit.md;
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md;
- the Round-55 task brief.

The imported facts were the exact angular coefficient, the accepted
dyadic profile support/overlap and hard-top ownership, the Vaaler
\(C^1\) bound and height floors, the distinct physical stars, and the
accepted moving-window target. The sampled-BV lemma, fixed-leg estimates,
resonance examples, crossover, exponent ledger, and disjoint overlap owner
were derived directly. The only general analytic input was the standard
finite-interval second-derivative estimate (55.9). No other Round-55 report,
external source, or unlisted artifact was read.

## 7. Recommended state effect

**Promote the scoped top-block low-leg margin theorem (55.1)--(55.2).** Its
state statement should retain all of the following:

1. \(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), and uniformity over every
   length-at-most-\(R\) product window, including edge windows;
2. the exact sampled-BV input (55.8), with height floors, equality stars,
   the hard-top jump, and the radial star separately owned;
3. curvature only for a fixed leg at most \(\sqrt R\), and the trivial
   interval bound beyond that crossover;
4. the exact linear \((H+Q)/\sqrt Y\) window ledger and the disjoint owner
   (55.4);
5. immunity to fourth-power and integer/half-integer first-derivative
   resonances.

Promote no claim about the balanced core (55.5). Retain the complete
Round-54 shifted-correlation theorem, GAR, the finite alpha transfer,
M9-M1, M9, and the Gauss-circle target as open. This theorem proves no new
global discrepancy exponent by itself; it rigorously removes only the
polylogarithmic low-leg margins from the critical top block.
