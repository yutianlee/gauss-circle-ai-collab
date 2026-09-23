# Hard-M1 \(t=1\) high-height dual-frequency projective reduction

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Formal candidate SHA-256:
  123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28
- Evidence status: durable proof kernel after independent
  normalization/projective-power, literal-variation/centered-kernel,
  and blind-post-unmask review
- Numerical theorem evidence: none

## Accepted statement

Fix real \(X\ge2\), a nonempty literal middle or lower residual
hard-M1 shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\tag{189.K1}
\]

On nonzero inherited hard-top support \(L\ll X^{1/4}\). Fix a
nonempty dyadic integer block \(Y<h\le2Y\) with \(Y>Q\), and retain
the exact accepted Round-185 carrier and Round-188 complement:

\[
 \kappa,g,U\ {\rm odd},\quad u=gU,\quad (u,v)=1,\quad
 (U,h)=1,\quad0<2\kappa gh<R_0,
\tag{189.K2}
\]

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad
 Qm<Y,\qquad(a,q)=1.
\tag{189.K3}
\]

Every selector, squarefree and allocation-coprimality deletion,
profile, floor, star, half-weight, hard sample, crossing, endpoint,
conjugation, Fejer factor, square-root phase, sign, positivity
predicate, affine site, orientation, terminal block, and zero
extension remains literal. Since \(U\) is odd, \(m\) and \(q\) are
odd. Since \(q\mid U\mid u\) and \((u,v)=1\), define

\[
 j_q(a,v)=|a\bar v_q|_q,\qquad
 T_Q(m,q;Y)=\min\!\left\{\frac{q-1}{2},
       \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\tag{189.K4}
\]

Let \(\mathscr C_{Y,Q}^{\sigma}\) denote the exact complex
Round-188 \(Qm<Y\) complement. Insert
\(1\le j_q(a,v)\le T_Q(m,q;Y)\) to define
\(\mathscr S_{Y,Q}^{\sigma}\), and insert
\(j_q(a,v)>T_Q(m,q;Y)\) to define
\(\mathscr F_{Y,Q}^{\sigma}\). Then, before any triangle inequality,

\[
 \boxed{\mathscr C_{Y,Q}^{\sigma}
 =\mathscr S_{Y,Q}^{\sigma}+\mathscr F_{Y,Q}^{\sigma}.}
\tag{189.K5}
\]

The complete projectively slow sector is absolutely target-safe:

\[
 \boxed{|\mathscr S_{Y,Q}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{189.K6}
\]

The exact remaining relation is

\[
 \boxed{\Re\mathscr F_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{189.K7}
\]

It remains open under one outer real part over both orientations and
every literal label. No complete high-height relation, complete
original-\(t=1\) residual, small-\(t\) owner, parent, bridge, theorem,
or exponent is asserted.

## Proof of the target-safe sector

For fixed \(a\in(\mathbb Z/q\mathbb Z)^\times\), the projective map

\[
 v\bmod q\longmapsto a\bar v_q\bmod q
\tag{189.K8}
\]

is a bijection on the unit classes. Because \(q\) is odd, for
\(0\le T\le(q-1)/2\) the condition
\(1\le|a\bar v_q|_q\le T\) uses exactly

\[
 2\sum_{\substack{1\le r\le T\\(r,q)=1}}1\le2T
\tag{189.K9}
\]

classes. The two least-residue sides are disjoint. The formula also
handles the empty \(T=0\) case and the saturated
\(T=(q-1)/2\) case.

The literal \(v\)-support has length \(O(u)\). Each residue class
modulo \(q\) occurs \(O(u/q+1)=O(u/q)\) times because \(q\mid u\).
All literal masks only delete values. Thus, at fixed
\((\kappa,u,m,q,a)\),

\[
 \#\{v:1\le j_q(a,v)\le T_Q\}
 \ll\frac{uT_Q}{q}
 \ll\frac{Qum}{Y}.
\tag{189.K10}
\]

There are \(O(Y)\) heights and \(O(1+\kappa)=O(\kappa)\) live affine
sites per oriented row. Round 188 supplies exactly

\[
 c_{mq}(ma)=\frac1m c_q(a),\qquad
 \sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll\log(2q).
\tag{189.K11}
\]

Consequently \(Y\) in the height count cancels \(Y^{-1}\) in
(189.K10), while \(m\) in (189.K10) cancels the exact \(m^{-1}\)
lift weight before any outer positive sum. The fixed
\((\kappa,u,m,q)\) cost is

\[
 \ll_\eta Q\kappa u\log(2q)X^\eta.
\tag{189.K12}
\]

There is no fourth divisor variable. Writing \(u=mqr\),

\[
 \sum_{mq\mid u}\log(2q)
 \le\tau_3(u)\log(2u).
\tag{189.K13}
\]

Elementary triple-divisor summation, \(u\asymp L/\kappa\), and the
inherited live-shell connector give

\[
\begin{aligned}
 |\mathscr S_{Y,Q}^{\sigma}|
 &\ll_\eta QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log(2u)\\
 &\ll_\eta QL^2\log^{O(1)}(2L)X^\eta
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{189.K14}
\]

No positive power of \(Y\) is absorbed. At saturation the fast
complement is empty for that lift. Replacing only the multiplier
\(Q\) in (189.K4) by \(1\) proves the power-neutral baseline
\(j_q(a,v)\le\lfloor U/Y\rfloor\). Any predeclared fixed
polylogarithmic multiplier is handled by the same explicit ledger;
no positive power of \(X\) is absorbed. This proves (189.K6).

## Exact fast interface

For fixed \((\kappa,u,m,q,v,\omega)\), let
\(W_{\kappa,u,mq,v,\omega}^{\sigma}(h)\) be the complete
zero-extended height sequence inherited from the exact complex
aggregate. It includes the dyadic block, \((mq,h)=1\), carrier
inequality, literal endpoint aggregate, and every selector and mask.
Put

\[
 \mathsf V(W)=\sum_{h\in\mathbb Z}|W(h+1)-W(h)|.
\tag{189.K15}
\]

On a dyadic band \(J\le j_q(a,v)<2J\), exact Abel summation gives

\[
 \left|\sum_hW(h)e(\epsilon_\omega a\bar v_qh/q)\right|
 \ll\frac qJ\mathsf V(W).
\tag{189.K16}
\]

Uniformly for every fixed admissible
\(a\in(\mathbb Z/q\mathbb Z)^\times\) with \(m|a|_q>Q\), a
target-scaled sufficient input on each complementary \(J\)-band is

\[
 \boxed{
 \sum_{\substack{\omega,\ v\ {\rm literal}\\
                  J\le j_q(a,v)<2J}}
 \mathsf V(W_{\kappa,u,mq,v,\omega}^{\sigma})
 \ll_\eta\frac{Qm\kappa uJ}{q}X^\eta.}
\tag{189.K17}
\]

Indeed, (189.K16)--(189.K17), the exact \(m^{-1}\) lift weight,
coefficient mass, dyadic-band sum, and (189.K13) reproduce
(189.K14), with only fixed logarithmic losses. A genuinely joint
signed discrepancy estimate with the same final ledger would also
suffice.

No accepted dependency proves (189.K17). Pointwise boundedness and
the \(O(\kappa)\) literal site count give only

\[
 \mathsf V(W)\ll_\eta Y\kappa X^\eta,\qquad
 \sum_{v\ {\rm in\ the\ band}}\mathsf V(W_v)
 \ll_\eta\frac{Y\kappa uJ}{q}X^\eta.
\tag{189.K18}
\]

The precise deficit relative to (189.K17) is \(Y/(Qm)>1\); primitive
lifts retain \(Y/Q\), a non-polylogarithmic height loss. Changing
\(h\) changes the coprimality and squarefree masks, residual selector,
profile, anchors, affine range, endpoints, floors, crossings, Fejer
factor, square-root phase, and terminal zero extension. The exact
first difference contains common-range differences and births and
deaths of literal affine sites. None has a proved improvement over
(189.K18). Periodicity of the displayed exponential does not imply
periodicity or bounded variation of \(W\).

## Centered-kernel and false-mechanism controls

For actual odd \(q\) and unit \(b\bmod q\), put

\[
 K_q(b)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
 c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q.
\tag{189.K19}
\]

Exact-conductor partition and Möbius inversion give

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),\qquad
 K_q^\circ(-b)=-K_q^\circ(b).
\tag{189.K20}
\]

Oddness is essential and is guaranteed by the literal carrier. For
odd prime \(p\),

\[
 K_p^\circ(b)=E_p(b),\qquad
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)=-\frac{p-1}{2}.
\tag{189.K21}
\]

Hence exact-conductor centering alone cannot supply a uniform
polylogarithmic height-prefix theorem. This is a full-kernel
falsifier, not literal lower mass: the open packet retains the
ordinary-frequency deletion, projective fast split, endpoint
coefficient, masks, and both orientations.

An abstract bounded array can dephase the displayed height,
affine-parity, and square-root phases and attain carrier capacity.
This excludes a coefficient-uniform proof from support and boundedness
alone, but is not a physical lower bound. Positive completion, large
sieve, Poisson, alias energy, and selector-blind sieve opening return
positive capacity and do not establish (189.K17).

## Scope and dependencies

The proved content is only the projective bijection and capped count,
the complete \(j_q(a,v)\le T_Q\) absolute sector, its exact
one-real-part complement, and the scoped variation and centered-kernel
controls.

Even a future proof of (189.K7) closes only the exact inherited
original-\(t=1\) residual through the accepted Round-184/185/187/188
connectors. Every original \(t\ge2\) small-\(G\) incidence, the
large-\(G\) near-resonant complement, complete hard and smooth M1
parents, GAR, every M2 parent, endpoint uniformity, M9, both bridges,
the quarter target, and every exponent claim remain open.

Direct accepted dependencies are:

- M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction;
- Divisor-bound-elementary.

The decisive independent reviews are:

- reviews/dual_frequency_normalization_projective_power_seam_review.md,
  SHA-256
  5af4ffb3fd3da05287cf217a9ffad412dd888aea716686466bd76fe90c4b8b95;
- reviews/literal_variation_centered_kernel_scope_seam_review.md,
  SHA-256
  7b9bd94ba4e229d76b1eca96a0e7d25aa98d6e66c4c81e5c40e07d85c8744d3e;
- reviews/blind_post_unmask_owner_scope_seam_review.md, SHA-256
  37cee21325ed7b1e4892aff6e433f642cac9936cf10ce42e25c53496fd712a93;
- reviews/final_candidate_normalization_post_quantifier_verification.md,
  SHA-256
  2b85de501fb60e34eadb212c94843b40e8abcde124ef4fe40aecfecfe9ae25e0;
- reviews/final_candidate_literal_formalization_post_quantifier_verification.md,
  SHA-256
  c2c7135ad43bc98c8b4b26f98779cd5b3601892cca018d3659a0367efdc997ad;
- reviews/blind_post_unmask_quantifier_post_repair_verification.md,
  SHA-256
  3594bef3890c41d26eb36bdfcae4b5a8f761a5b203b5289ba2889eae91382dda.

The bounded Wolfram check is diagnostic only and supplies no
asymptotic theorem evidence.
