# Conductor Round 189 report reconciliation

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Decision status: candidate selection before seam review
- Numerical theorem evidence: none

## Reports received

1. reports/dual_height_frequency_signed_attack.md, SHA-256
   65636c38a3b0c3dbd4a26839dbc89daa88ef78dee5638d02d0de1192b9bdfd38;
2. reports/height_variation_projective_hostile_audit.md, SHA-256
   b8ec876aebcc6668646880813bad0abf576063f58e71518d29c8e5778d371608;
3. reports/blind_dual_frequency_rederivation.md, SHA-256
   13169505840f9033fb8ddaac6eba62d12988a669127f593a8bc48438543621a3.

All three reports independently prove the projective residue count, the
exact cancellation of the multiplicity factor by the Fourier-lift
factor \(1/m\), and the resulting target-safe slow dual-frequency
sector. They also agree that the fast complement cannot be completed
from pointwise boundedness of the literal endpoint coefficient.

## Selected mathematical kernel

On the exact Round-188 complement put

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\]

and, because \(q\mid U\mid u\) and \((u,v)=1\), define

\[
 j_q(a,v)=|a\bar v_q|_q.
\]

The inherited carrier has \(U\) odd. Consequently \(m\) and \(q\)
are odd as well. For fixed unit \(a\bmod q\), the map
\(v\mapsto a\bar v_q\) is a bijection on the unit classes. Therefore
the cutoff

\[
 T_Q(m,q;Y)=\min\!\left\{\frac{q-1}{2},
             \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}
\]

uses at most \(2T_Q\) residue classes and
\(O(uT_Q/q)=O(Qum/Y)\) literal \(v\)-values. Restoring \(O(Y)\)
heights and \(O(\kappa)\) affine sites, and then using

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),
\]

gives fixed-label cost \(O(Q\kappa u\log(2q)X^\eta)\). Finally

\[
 \sum_{mq\mid u}\log(2q)\le \tau_3(u)\log(2u)
\]

and the inherited live support \(L\ll X^{1/4}\) yield

\[
 |\mathscr S_{Y,Q;Q}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

The floor-zero and saturated cases are literal: at \(T_Q=0\) the
sector is empty, while at \(T_Q=(q-1)/2\) it contains every unit
slope. The same proof works for any predeclared fixed polylogarithmic
factor \(P\). Thus \(U/Y\) is the power-neutral baseline, not a
unique cutoff. The formal candidate records \(P=Q\), the frozen
round choice.

The exact complement is obtained only by inserting
\(j_q(a,v)>T_Q(m,q;Y)\) into the same complex aggregate. Both
orientations and every literal field remain under one outer real part.
On a dyadic band \(J\le j_q(a,v)<2J\), a sufficient actual-coefficient
input is

\[
 \sum_{v\ {\rm in\ the\ band}}\mathsf V(W_v)
 \ll_\eta \frac{Qm\kappa uJ}{q}X^\eta,
\]

or a genuinely joint signed substitute with the same final ledger.
The available pointwise bound gives only

\[
 \sum_{v\ {\rm in\ the\ band}}\mathsf V(W_v)
 \ll_\eta \frac{Y\kappa uJ}{q}X^\eta.
\]

The precise deficit relative to the \(Q\)-budgeted target is therefore
\(Y/(Qm)\); primitive lifts retain \(Y/Q\), which is a full
non-polylogarithmic height loss. The hostile report's stronger
unit-cost condition is sufficient but is not selected as necessary.

## Reconciliation of the blind parity objection

The statement-only report correctly proves that its displayed
exact-conductor identity is false for even conductor. This exposes an
omission in the blind packet, not in the physical carrier. The actual
Round-185 carrier explicitly has \(U\) odd, so every divisor \(q\) of
\(U\) is odd and the identity is valid in the selected scope. The
candidate must state this oddness before invoking the centered kernel.

For actual odd \(q\), Möbius inversion gives

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\]

For odd prime \(p\), \(K_p^\circ(b)=E_p(b)\), and the slope
\(b=-2\) has

\[
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)=-(p-1)/2.
\]

This forbids a uniform polylogarithmic centered-kernel prefix theorem.
It is not a lower bound for the literal aggregate.

## Bounded controls

The conductor reproduced the finite odd-conductor projective count,
kernel identity, and prime bad-slope survivor:

- controls/dual_frequency_projective_check.wls, SHA-256
  481e7054cce6ad9922f818ff33d11c77265c653608acccbb380a804f34870fff;
- controls/conductor_round189_wolfram_dual_frequency_check.md,
  SHA-256
  35bddf8080ceef4acbc6290abe689175f94fc90745a28c707f8147bb5c08adbf.

The independent analytical ledger is
controls/conductor_round189_analytic_controls.md, SHA-256
2ed8b5a67efb51543239467ec55e285b0f9432b5fc245080b387fec267dd7ffd.
The finite run is diagnostic only and supplies no asymptotic theorem
evidence.

## Conductor decision before seam review

Select the smallest common proved kernel: the exact projective
bijection, the complete \(j_q(a,v)\le T_Q\) target-safe sector, its
exact one-real-part complement, the quantitative literal-variation
interface, and the odd-conductor bad-slope no-go. Do not promote the
fast complement, complete high-height relation, complete original
\(t=1\) residual, any original \(t\ge2\) range, parent, bridge,
theorem, or exponent.

Provisional closing label:

strict_dual_height_resonance_sector.

The candidate must receive independent normalization/projective,
literal-power/bad-slope, and blind-post-unmask owner-scope reviews
before a durable kernel or State Patch is written.
