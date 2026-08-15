# Hostile audit of the Vaaler height floor

- Campaign: `m9-m1-alpha-vaaler-height-floor`
- Research round: `52` (`alpha_vaaler_height_floor_type_and_variation`)
- Task: `vaaler_floor_hostile_audit`
- Role: `seam_reviewer`
- Graph SHA-256 supplied in the brief: `76a480a78ae30353d4f9cbe26c0e17337c1b89318c4a15758a6ffe0c34051fea`
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

**Typed discrete-height lemma, together with an actual-scale no-go.** For fixed
\(X,D_j,H_j\), the integer

\[
H_j=\lfloor D_jX^{-1/4}\rfloor
\]

has zero velocity with respect to every contour height
\(\mu,\nu,\alpha,\beta\). It is therefore not a moving alpha-contour seam and
produces no seam delta in the finite Cauchy--Green ledger. The factor
\((H_j+1)^v\) is a smooth/holomorphic contour multiplier whose derivative
produces \(\log(H_j+1)\), not a derivative of the floor.

There is nevertheless an exact and useful *discrete* adjacent-height identity.
For \(H\geq1\),

\[
\Delta_Ha(h)=
\begin{cases}
\displaystyle
\Phi\!\left(\frac h{H+2}\right)
-\Phi\!\left(\frac h{H+1}\right),&1\leq h\leq H,\\[6pt]
\displaystyle
\Phi\!\left(\frac{H+1}{H+2}\right),&h=H+1,\\
0,&\text{otherwise}.
\end{cases}
\tag{52.1}
\]

Every displayed nonzero term is positive, and

\[
\boxed{\ \|\Delta_Ha\|_{\ell^1_h}=\frac12\ }
\tag{52.2}
\]

exactly. Thus the right-end taper makes the *new endpoint* only
\(O(H^{-2})\), but it does not make the full unweighted unit-height change
\(o(1)\): the old frequencies contribute the missing mass. With the Vaaler
coefficient's \(1/h\), the exact order improves to

\[
\sum_{h\geq1}\frac{|\Delta_Ha(h)|}{h}\asymp \frac1{H+1},
\qquad
\sum_{h\geq1}|\alpha_{h,H+1}-\alpha_{h,H}|\asymp\frac1{H+1}.
\tag{52.3}
\]

More generally, for each fixed \(p\geq-1\), the power-weighted norm has the
sharp order

\[
\sum_{h\geq1}h^p|\Delta_Ha(h)|\asymp_p(H+1)^p.
\tag{52.4}
\]

The hostile conclusion is that (52.1)--(52.4) cannot be promoted into an
actual dyadic-scale or alpha-trace estimate. The physical coefficient
\(\Omega_X^*\) contains \(a_H\), not \(a_H/h\), and an abstract unit change
of \(H\) is not an adjacent dyadic-scale change. In fact, for any integers
\(K>H\),

\[
\boxed{\ \|a_K-a_H\|_{\ell^1_h}=\frac{K-H}{2}\ }.
\tag{52.5}
\]

Consequently, a scale change for which \(|K-H|\asymp H\) has coefficient-only
variation \(\asymp H\), despite the \(1/2\) unit-step identity. This is a
rigorous counterexample to transferring the unit-height bound to a dyadic
block change. Simultaneous changes in \(D_j,w_j\), supports, the profile star,
the powers \((D_j/(2\sqrt X))^u(H_j+1)^v\), and external normalization remain
unaccounted for. No alpha capacity bound follows.

## 2. Exact statement and hypotheses

Let

\[
\Phi(u)=\pi u(1-u)\cot(\pi u)+u\qquad(0<u<1)
\]

with its endpoint extension \(\Phi(0)=1\), \(\Phi(1)=0\). Use the accepted
source-audited facts that \(\Phi\in C^1[0,1]\) and is strictly decreasing.
For an integer \(H\geq1\), extend

\[
a_H(h)={\bf1}_{1\leq h\leq H}\Phi\!\left(\frac h{H+1}\right)
\]

by zero to all positive integers. Put

\[
V_p(H)=\sum_{h\geq1}h^p|a_{H+1}(h)-a_H(h)|.
\]

Then the following assertions hold.

1. If \(X,D_j\), and the discrete block label \(j\) are fixed while the
   contour variables vary, then
   \(\partial_\mu H_j=\partial_\nu H_j=\partial_\alpha H_j
   =\partial_\beta H_j=0\), in both the classical and distributional senses.
   Hence there is no contour-seam delta attached to \(H_j\).
2. Formula (52.1) holds, \(\Delta_Ha(h)>0\) for \(1\leq h\leq H+1\), and
   \(V_0(H)=1/2\) exactly.
3. If \(N=H+1\), then
   \[
   \frac1{2N}\leq V_{-1}(H)\leq\frac{C_\Phi}{N}
   \tag{52.6}
   \]
   for every \(H\geq1\), with an absolute constant depending only on
   \(\|\Phi'\|_\infty\). More sharply,
   \[
   NV_{-1}(H)\longrightarrow1.
   \tag{52.7}
   \]
4. For every fixed \(p\geq-1\),
   \[
   \frac{V_p(H)}{N^p}\longrightarrow
   c_p:=\int_0^1x^{p+1}[-\Phi'(x)]\,dx>0.
   \tag{52.8}
   \]
   Here \(c_{-1}=1\), while for \(p>-1\),
   \[
   c_p=(p+1)\int_0^1x^p\Phi(x)\,dx.
   \tag{52.9}
   \]
   Therefore constants \(0<c_p^-\leq c_p^+<\infty\) exist such that
   \(c_p^-N^p\leq V_p(H)\leq c_p^+N^p\) uniformly down to \(H=1\).
5. For integers \(K>H\), \(a_K(h)\geq a_H(h)\) pointwise and (52.5) holds.
   If
   \(T_H=\sum_{h=1}^Ha_H(h)/h\), then
   \[
   T_H=\log H+C_\Phi'+o(1),
   \tag{52.10}
   \]
   so for \(K/H\to\rho>1\),
   \[
   \sum_h\frac{|a_K(h)-a_H(h)|}{h}\longrightarrow\log\rho.
   \tag{52.11}
   \]

Assertions (52.5) and (52.11) concern the coefficient family with every other
factor frozen. They are an obstruction to a false transfer, not an identity
for two actual dyadic blocks. The latter have not been placed on a common
support or common star convention in the permitted context.

## 3. Proof or derivation

**Variable type.** In the frozen antecedent, \(X,D_j,H_j\) are parameters and
the contour heights are integration variables. The displayed definition of
\(H_j\) contains none of \(\mu,\nu,\alpha,\beta\), proving the four zero
derivatives. Although

\[
\partial_v(H_j+1)^v=\log(H_j+1)(H_j+1)^v,
\]

this is an ordinary derivative of an entire exponential multiplier. It is
not a moving boundary and creates no delta distribution. A floor jump can
occur only after a separate physical parameter such as \(X\) or \(D\) is
varied, or after one declares a discrete comparison of two heights.

**Endpoint algebra.** Directly from
\(\cot(\pi(1-u))=-\cot(\pi u)\),

\[
\Phi(u)+\Phi(1-u)=1.
\tag{52.12}
\]

The cotangent expansion at zero gives

\[
\Phi(t)=1-\frac{\pi^2}{3}t^2+\frac{\pi^2}{3}t^3+O(t^4),
\]

and hence

\[
\Phi(1-t)=\frac{\pi^2}{3}t^2-\frac{\pi^2}{3}t^3+O(t^4).
\tag{52.13}
\]

Thus the new term in (52.1) is

\[
\Phi\!\left(\frac{H+1}{H+2}\right)
=\frac{\pi^2}{3(H+2)^2}+O(H^{-3}).
\tag{52.14}
\]

It is full-weight, not half-weight. The indicator \(h\leq H\) is the Fourier
degree cutoff; the star in \(\Omega_X^*\) belongs to the dyadic profile
evaluation and is a different object.

**Exact adjacent mass.** For \(1\leq h\leq H\), increasing \(H\) decreases
the argument of the decreasing function \(\Phi\), while \(h=H+1\) is a new
positive term. This proves positivity in (52.1). Pairing \(h\) with
\(H+1-h\) and using (52.12) gives, for every \(H\geq1\),

\[
\sum_{h=1}^H\Phi\!\left(\frac h{H+1}\right)=\frac H2.
\tag{52.15}
\]

Because all adjacent differences have one sign,

\[
V_0(H)=\sum_h a_{H+1}(h)-\sum_h a_H(h)
=\frac{H+1}{2}-\frac H2=\frac12.
\]

This also identifies the hostile mechanism: (52.14) accounts for only
\(O(H^{-2})\) of the exact mass \(1/2\); the bulk adjustment of the old
frequencies accounts for the rest.

**Weighted bounds.** For \(1\leq h\leq H\), the mean-value theorem and
\(M=\|\Phi'\|_\infty\) give

\[
0<\frac{\Delta_Ha(h)}h
\leq \frac{M}{(H+1)(H+2)}.
\tag{52.16}
\]

The new endpoint contributes at most \(1/(H+1)\) after division by \(h\).
Summing proves the upper bound in (52.6). The exact unweighted mass and
\(h\leq H+1\) give

\[
V_{-1}(H)\geq\frac1{H+1}V_0(H)=\frac1{2(H+1)},
\]

including \(H=1\).

For sharp power weights, write \(N=H+1\). For \(h<N\),

\[
\Delta_Ha(h)
=\int_{h/(N+1)}^{h/N}[-\Phi'(x)]\,dx.
\tag{52.17}
\]

After division by \(N^p\), (52.17) is a Riemann sum for
\(x^{p+1}[-\Phi'(x)]\). The new endpoint is \(O(N^{-2})\) after that
normalization by (52.14). For \(p\geq-1\), the endpoint behavior
\(\Phi'(x)=O(x)\) at zero makes the limiting integrand continuous or
integrable, proving (52.8). Positivity follows from strict decrease. Integration
by parts proves (52.9), while \(c_{-1}=\Phi(0)-\Phi(1)=1\). The asymptotic
and the positivity of each of the finitely many remaining small-\(H\) norms
give the stated all-\(H\) comparability. For \(p=0\), (52.8) agrees with the
stronger exact identity \(V_0=1/2\).

At the smallest allowed height,

\[
\begin{aligned}
\Delta_1a(1)&=\frac{2\pi}{9\sqrt3}-\frac16,\\
\Delta_1a(2)&=\frac23-\frac{2\pi}{9\sqrt3},\\
V_0(1)&=\frac12,\\
V_{-1}(1)&=\frac16+\frac{\pi}{9\sqrt3}.
\end{aligned}
\tag{52.18}
\]

Thus no hidden \(H\geq2\) assumption is required.

**Long changes and the dyadic counterexample.** Pointwise monotonicity extends
from adjacent heights to \(K>H\). Applying (52.15) at the two endpoints gives

\[
\sum_h|a_K(h)-a_H(h)|
=\sum_ha_K(h)-\sum_ha_H(h)=\frac{K-H}{2},
\]

which proves (52.5). In particular, telescoping \(O(H)\) unit floor events
has \(O(H)\), not \(O(1)\), total unweighted variation; there is no internal
sign cancellation because every increment is nonnegative.

For the \(1/h\)-weighted comparison,

\[
T_H=\sum_{h=1}^H\frac1h
+\frac1{H+1}\sum_{h=1}^H
\frac{\Phi(h/(H+1))-1}{h/(H+1)}.
\]

The second summand is a Riemann sum for the finite integral
\(\int_0^1(\Phi(x)-1)x^{-1}\,dx\), since (52.13) makes the integrand
continuous at zero. This proves (52.10) and (52.11).

Finally, even a lawful discrete comparison of the Mellin antecedent is not
just \(\Delta_Ha\). Its height-dependent part changes as

\[
\begin{aligned}
&(H+2)^v a_{H+1}(h)-(H+1)^v a_H(h)\\
&\quad=(H+1)^v\Delta_Ha(h)
+\big((H+2)^v-(H+1)^v\big)a_{H+1}(h).
\end{aligned}
\tag{52.19}
\]

The second term is a bulk term. Uniformly in a high imaginary contour height,
the relative factor is controlled only by
\(\min(2,O(|v|/(H+1)))\), not by \(O(H^{-1})\). A change of \(D_j\) adds the
analogous \(D_j^u\) change, while \(w_j\), its support and its star also move.
Thus the abstract calculation cannot be relabelled as an actual alpha seam or
actual adjacent-scale identity.

## 4. First doubtful or unproved step

The first unproved step in any proposed alpha application is the map from an
abstract integer change \(H\mapsto H+1\) to an actual varied physical
coordinate. The permitted context supplies no path

\[
t\longmapsto(X(t),D_j(t),H_j(t),w_{j,t},\text{support}_t,\text{star}_t)
\]

on which the two one-sided traces are written in one common finite alpha
antecedent. It also supplies no reindexing rule when the dyadic partition
changes. Without that map, the sign and size of the full jump, its face/axis
pullbacks, and any collision with a Plemelj pole are undefined.

Even after such a path is supplied, (52.19) shows that the coefficient-only
increment is not the whole Mellin jump. For an adjacent dyadic block, the new
height need not differ by one; a factor-scale change can change it by order
\(H\), and (52.5) then restores \(H\)-sized unweighted variation. For variation
in \(X\) at fixed \(D\), one may cross unit floor thresholds, but all those
events over a macroscopic range telescope to the same obstruction. Therefore
the first missing theorem is a complete coupled adjacent-trace identity, not
another estimate of \(\Delta_Ha\).

## 5. Control tests and outcomes

1. **`variable_type` -- pass/no-go.** At fixed \(X,D_j,j\), \(H_j\) is a
   contour-external integer parameter. All alpha-contour velocities are zero.
   The floor is not a moving Cauchy--Green seam.
2. **`exact_Phi_formula` -- pass.** The audit uses
   \(\Phi(u)=\pi u(1-u)\cot(\pi u)+u\), the true complementary identity
   \(\Phi(u)+\Phi(1-u)=1\), and monotonicity. It never uses the false symmetry
   \(\Phi(1-u)=\Phi(u)\).
3. **`right_endpoint_taper` -- pass with hostile correction.** The new endpoint
   is \(\pi^2/(3(H+2)^2)+O(H^{-3})\), but the total adjacent \(\ell^1\) mass is
   exactly \(1/2\). Endpoint taper alone does not make the physical coefficient
   change small.
4. **`adjacent_height_identity` -- pass.** Formula (52.1) includes every old
   frequency and the new frequency \(h=H+1\). All terms have one sign.
5. **`weighted_norms` -- pass.** The exact unweighted norm, the uniform
   \(1/h\)-weighted bounds down to \(H=1\), and the sharp fixed-power law
   (52.8) are proved. A factor-size height change is governed instead by
   (52.5) and (52.11).
6. **`actual_scale_coupling` -- fail for transfer.** No actual varied-scale map
   is supplied. Equation (52.19), changes in \(D_j^u,w_j\), support, and
   normalization are mandatory. A dyadic scale change is not generally a unit
   height change.
7. **`star_ownership` -- pass as a separation control.** The cutoff
   \(h\leq H\) has full equality ownership. The star in \(\Omega_X^*\) belongs
   to the profile evaluation and cannot halve either (52.1) or the derivative
   of a floor step.
8. **`alpha_capacity_scope` -- fail for promotion.** The \(1/h\)-weighted
   family has adjacent variation \(O(H^{-1})\), but the displayed physical
   \(\Omega_X^*\) uses the unweighted \(a_H\), whose adjacent norm is \(1/2\)
   and whose factor-scale norm can be \(\asymp H\). No signed profile or lattice
   cancellation is proved.
9. **`downstream_scope` -- pass.** The lemma neither estimates the projected
   alpha trace nor supplies its outside-height Cauchy limit. It has no direct
   implication for the swept operator, M9-M1, M9, or the Gauss-circle target.

No numerical, symbolic, or web experiment was used.

## 6. Dependencies and exact artifacts used

This audit used only its task brief and the permitted context:

- `protocol.md`;
- `state/proof_obligations.yml`, specifically the accepted H4,
  `H4-Phi-regularity`, and Round-49--51 alpha nodes and barriers;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/derivation_packet.md`;
- `rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`;
- `rounds/codex-managed/m9-m1-alpha-signed-jump-incidence/reports/jump_incidence_hostile_audit.md`;
- task brief
  `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/briefs/vaaler_floor_hostile_audit.md`.

The only imported facts about \(\Phi\) were its audited exact formula,
endpoint extension, \(C^1\) regularity, and monotonicity. All discrete
variation identities and estimates above were derived directly. No other
Round-52 report or external source was read.

## 7. Recommended state effect

**Promote only the narrow typed discrete-height lemma and retain a no-go for
the proposed seam application.** The graph may record that \(H_j\) has zero
alpha-contour velocity, that (52.1)--(52.4) hold, and that the unit-height
unweighted variation is exactly \(1/2\) while the \(1/h\)-weighted variation
is \(\asymp H^{-1}\). It should also record (52.5) as the explicit barrier to
identifying a unit height change with an actual dyadic-scale change.

Revise the alpha target so that an \(H_j\)-floor event is not sent through the
continuous alpha seam-incidence ledger. Any future use must first freeze an
actual physical parameter path and write the complete two-sided finite
antecedent, including (52.19), the \(D_j^u\) factor, the moving profile and
support, the profile star, all normalizations, and any collision rule. Only a
subsequent signed theorem for that coupled difference could affect alpha
lattice capacity.

Keep `M9-M1-alpha-bounded-zeta-high-transition-bound` open. The present lemma
is coefficient algebra and a type correction; it proves neither the projected
alpha trace estimate nor the outside-height limit.
