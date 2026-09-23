# Conductor Round 189 adjudication

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Durable kernel SHA-256:
  31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58
- Closing label: strict_dual_height_resonance_sector
- Numerical theorem evidence: none

## 1. Result and conductor decision

Round 189 closes with one proved subordinate reduction. On the exact
Round-188 complement

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\]

put

\[
 j_q(a,v)=|a\bar v_q|_q,\qquad
 T_Q(m,q;Y)=
 \min\!\left\{\frac{q-1}{2},
       \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\]

The inherited carrier has \(U\) odd, hence \(m,q\) odd. The complete
sector \(1\le j_q(a,v)\le T_Q(m,q;Y)\) has absolute size

\[
 O_{B,\varepsilon}(L^2X^\varepsilon).
\]

This includes the required power-neutral baseline
\(j_q(a,v)\le\lfloor U/Y\rfloor\) and a fixed-polylogarithmic
\(Q\)-enlargement. The complement
\(j_q(a,v)>T_Q(m,q;Y)\) is retained exactly under one outer real part
over both orientations and every literal field. Its target estimate
is open.

## 2. Proof and exact power ledger

For fixed unit \(a\bmod q\), the map
\(v\mapsto a\bar v_q\) is a unit-class bijection. The slow set uses
at most \(2T_Q\) classes. Since the literal \(v\)-range has length
\(O(u)\) and \(q\mid u\), it contains

\[
 O(uT_Q/q)=O(Qum/Y)
\]

slow values. Restoring \(O(Y)\) heights and \(O(\kappa)\) affine
sites and using

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q)
\]

cancels \(Y\) and \(m\) before outer positivity. The fixed
\((\kappa,u,m,q)\) cost is
\(O(Q\kappa u\log(2q)X^\eta)\), and

\[
 \sum_{mq\mid u}\log(2q)\le\tau_3(u)\log(2u).
\]

The inherited \(L\ll X^{1/4}\) support absorbs only \(Q\) and fixed
logarithms into a fresh epsilon budget. No positive power of \(Y\) is
absorbed. The floor-zero and fully saturated cases are exact.

## 3. First open relation

Let \(W_v(h)\) be the complete zero-extended literal height sequence.
On \(J\le j_q(a,v)<2J\), Abel summation gives

\[
 \left|\sum_hW_v(h)e(\epsilon_\omega a\bar v_qh/q)\right|
 \ll(q/J)\mathsf V(W_v).
\]

Uniformly for fixed admissible \(a\), a sufficient target-scaled
input is

\[
 \sum_{\substack{\omega,v\\J\le j_q(a,v)<2J}}
 \mathsf V(W_v)
 \ll_\eta \frac{Qm\kappa uJ}{q}X^\eta.
\]

The accepted pointwise information gives only

\[
 \sum_{v\ {\rm in\ band}}\mathsf V(W_v)
 \ll_\eta \frac{Y\kappa uJ}{q}X^\eta.
\]

The exact deficit is \(Y/(Qm)>1\); primitive lifts retain \(Y/Q\).
The literal coprimality and squarefree masks, residual selector,
profiles, anchors, affine births/deaths, endpoints, Fejer factor,
square-root phase, and zero extension all vary with height. No
accepted dependency bounds their total variation at the sufficient
scale.

## 4. Kernel no-go and parity reconciliation

The statement-only report correctly found that the proposed conductor
identity is false for even \(q\). The actual carrier supplies the
missing hypothesis: \(U,m,q\) are odd. In that scope,

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\]

For odd prime \(p\),

\[
 K_p^\circ(b)=E_p(b),\qquad
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)=-(p-1)/2.
\]

This falsifies a uniform polylogarithmic centered-kernel prefix
estimate. It is not literal lower mass. Likewise, arbitrary bounded
arrays can dephase the displayed oscillation, but need not equal the
actual endpoint coefficient. Positive completion, large-sieve,
Poisson, alias energy, and selector-blind sieve opening are therefore
mechanism controls, not proofs or disproofs of the open literal
aggregate.

## 5. Evidence and independent controls

The discovery, hostile, and statement-only reports independently
agree on the promoted projective count and slow-sector ledger. The
formal candidate received GREEN reviews for normalization/projective
multiplicity, literal variation and centered-kernel scope, and blind
post-unmask owner scope. A one-line fixed-\(a\), dyadic-\(J\)
quantifier clarification was independently reverse-verified by all
three reviewers. The durable kernel then received three further GREEN
reviews for candidate consistency, power/literal owner scope, and
formalization/provenance hygiene.

The final kernel reviews are:

- reviews/final_kernel_candidate_consistency_review.md, SHA-256
  ef069ca04efa6f0f8913dc75ea6faad6648b891b7d710d61e24565e5a0fcc684;
- reviews/final_kernel_power_literal_owner_scope_review.md, SHA-256
  e19a1a0f3a23e14bfb40636425cbd698a5b5fef2d4707d1b21c08ca19e3d1354;
- reviews/final_kernel_formalization_provenance_hygiene_review.md,
  SHA-256
  d4e2667a8bf41c35fd6f646338e688d1982afd06809e5d7a67a7bd850baff69e.

The bounded Wolfram run checked finite odd-conductor projective counts,
kernel identities, and prime bad slopes. It is diagnostic only and
supplies no asymptotic theorem evidence.

## 6. Dependencies and exact scope

Direct accepted dependencies are:

- M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction;
- Divisor-bound-elementary.

Even a future proof of the exact fast complement would close only the
inherited original-\(t=1\) residual. Every original \(t\ge2\)
small-\(G\) incidence, the large-\(G\) near-resonant complement,
complete hard and smooth M1 parents, GAR, every M2 parent, endpoint
uniformity, M9, both bridges, the quarter target, and every exponent
claim remain open.

## 7. Recommended state effect

Create one proved-internal subordinate node for the strict
dual-frequency projective reduction. Add it only as a dependency and
evidence item to the still-open hard-M1 small-\(t\) residual owner.
Narrow that owner's next action to the exact fast complement
\(j_q(a,v)>T_Q(m,q;Y)\), with the displayed actual-coefficient
variation/discrepancy relation as the first sufficient interface.

Reject unique-maximal-cutoff, missing-\(1/m\), assumed-BV,
uniform-centered-prefix, positive-energy, and literal-lower-mass
overclaims. Make no status or exponent change to any complete
high-height, original-\(t=1\), small-\(t\), M1, M2, endpoint,
M9, bridge, or theorem owner.
