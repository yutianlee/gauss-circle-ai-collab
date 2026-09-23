# Round 191 hard-M1 fast height-jump coboundary strategy

## Purpose and authority

Round 191 is the first analytic round after the Round-190 full-proof and
current-literature checkpoint. It starts from authoritative graph
306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa
and attacks only the exact Round-189 projectively fast complement. It may
prove the full complement, prove a strict target-safe subpacket with an
exact remainder, or establish a rigorous scoped no-go. It may not pivot
to another proof owner or exponent.

Campaign: m9-m1-t1-fast-height-jump-coboundary-gate. The accepted
context is the Round-185 tangent-gcd carrier, the Round-187 inverse-residue
Fourier reduction, the Round-188 unique lift, the Round-189 projective
reduction, and the Round-190 adjudication.

## Frozen packet

Put

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,
 \qquad Y<h\le 2Y,\qquad Y>Q.
\]

Retain the exact primitive carrier and literal amplitudes
(K185.27), (K185.30)--(K185.35). On the remaining Fourier packet write

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\]

with \(U\mid u\), \(g=u/U\), and

\[
 j_q(a,v)=|a\bar v_q|_q,\qquad
 T_Q=\min\left\{\frac{q-1}{2},
                 \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\]

Only the fast sector \(j_q(a,v)>T_Q\) is in scope. For a nonempty
dyadic band \(J\le j_q(a,v)<2J\), define

\[
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q),
 \qquad \Delta^-W_v(h)=W_v(h)-W_v(h-1),
\]

where \(W_v(h)\) is the complete zero-extended literal height sequence.
The endpoint-exact Abel identity is

\[
 \sum_hW_v(h)z_{\omega,v}^h
 =\frac1{1-z_{\omega,v}}
  \sum_h\Delta^-W_v(h)z_{\omega,v}^h.
\]

The frozen sufficient seam is

\[
 \boxed{
 \left|\sum_{\substack{\omega,v\ {\rm literal}\\
 J\le j_q(a,v)<2J}}
 \frac1{1-z_{\omega,v}}
 \sum_h\Delta^-W_v(h)z_{\omega,v}^h\right|
 \ll_{B,\varepsilon}Qm\kappa uX^\varepsilon.}
\tag{191.S}
\]

The absolute-value placement is part of the theorem. There is one modulus
after the complete signed sum over height, projective rows, and both
orientations.

## Exact deficit and promotion gate

On the band,

\[
 |1-z_{\omega,v}|^{-1}\asymp q/J.
\]

Replacing the jump sum by individual total variations would require

\[
 \sum_{\omega,v}\mathsf V(W_v)
 \ll \frac{Qm\kappa uJ}{q}X^\varepsilon,
\]

while the accepted pointwise ledger gives only

\[
 \sum_{\omega,v}\mathsf V(W_v)
 \ll \frac{Y\kappa uJ}{q}X^\varepsilon.
\]

Thus positive variation misses exactly \(Y/(Qm)\), primitive \(Y/Q\).
Equation (191.S) is promotable only if that complete factor is recovered
from the actual jointly signed family before a positive norm. The exact
\(m^{-1}c_q(a)\) lift, coefficient mass, divisor sums, and dyadic bands
then reproduce the \(L^2X^\varepsilon\) target with no hidden positive
power.

## Decomposition to be tested

For each fixed literal row compare height \(h\) with \(h-1\) on the union
of their zero-extended affine index sets. The jump must be partitioned,
without overlap or omission, into:

1. common-range changes of the two endpoint coefficients, Fejer factor,
   and square-root phase;
2. births and deaths caused by the canonical anchors and positivity range;
3. changes of \((U,h)=1\), squarefree, allocation-coprimality, and residual
   selector masks;
4. dyadic-profile, floor, star, half-weight, hard-sample, real-\(X\)
   crossing, and endpoint changes; and
5. terminal zero-extension changes.

The discovery task must price each class. Smooth common-range terms may
use only derivatives actually established for the literal factors.
Arithmetic discontinuities may be opened by divisors or residue classes
only if the resulting coefficients and absolute-value placement remain
lawful. Birth/death terms may use a coarea or boundary count only after
the exact multiplicity is proved.

The orthogonal hostile task tests a joint \(h,v\) transform. The map
\(v\mapsto a\bar v_q\) is a unit-class bijection because \(q\mid u\), but
the literal \(v\)-interval, masks, affine sites, and endpoints are not free
coefficients. Reindexing by the projective slope is useful only if it
creates a signed theorem for these actual jump surfaces. A positive
large-sieve, completion, Poisson, or alias-energy estimate that returns
the \(Y\)-scale is a self-return, not progress.

## False controls and stop rule

Stop and record a scoped no-go if an argument:

- moves an absolute value inside the complete jump packet;
- separately absolutizes the two orientations;
- calls zero extension or Abel summation cancellation;
- assumes masks are height-invariant or replaces them by a free smooth
  weight;
- asserts an orientation involution or neighboring-projective-slope
  difference without a literal identity;
- implies the already false uniform polylogarithmic centered-kernel prefix
  theorem at odd-prime slope \(-2\);
- uses an arbitrary bounded-array estimate contradicted by dephasing;
- self-returns through positive completion, large sieve, or alias energy;
- leaves any fixed positive power of \(Y/(Qm)\); or
- imports an unverified source theorem or changes owner in-round.

A strict-sector result is useful only if it is nonempty, exactly stated,
target-safe after the full outer ledger, and leaves a single exact
one-outer-real-part complement. A no-go is useful only if it identifies
the exact theorem class refuted and does not claim a lower bound for the
literal packet unless one is actually proved.

## Computation policy and downstream scope

Mathematica or Python may check finite anchor changes, exact Abel signs,
projective-band counts, saturated cases, proposed pairings, and adversarial
operator capacity. Such checks are diagnostic only. At least 95% of the
round is analytical or algebraic.

Even a proof of the complete fast packet closes at most the exact original
\(t=1\) residual after the accepted connectors. Original \(t\ge2\)
small-\(G\) incidences, the large-\(G\) near-resonant complement, the hard
and smooth M1 parents, GAR, every M2 parent, endpoint uniformity, M9, both
bridges, and the Gauss-circle target remain separate. The internal
exponent stays \(1/3\), the accepted external benchmark stays
\(0.3144831759740614\ldots\), and the target stays \(1/4\) unless every
required downstream owner is later closed.
