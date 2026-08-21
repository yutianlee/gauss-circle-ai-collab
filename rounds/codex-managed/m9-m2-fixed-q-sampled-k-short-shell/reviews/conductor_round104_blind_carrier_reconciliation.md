# Conductor review: carrier cancellation and dephased variation

Campaign: m9-m2-fixed-q-sampled-k-short-shell

## Apparent conflict

The statement-only rederivation correctly observes the exact identity

\[
 e\!\left(-{g\Lambda_q\over2k}\right)
 \mathfrak B^\circ_{a,q,k}(g)
 =
 \int A^\circ_{ga,gb}(v)
 e\!\left(kv-J\delta_q\sqrt{gv}\right)\,dv.
 \tag{104.R1}
\]

Thus, if one expands the centered integral back into the uncentered
Fourier coefficient, the exterior reciprocal carrier cancels and the
remaining \(k\)-phase in the physical integral is linear. This is an
important no-double-count control.

It does not invalidate the actual fixed-\(q\) proof.

## Exact reconciliation

The accepted row contains the complete metric factor. After its Fourier
expansion, one summand is

\[
 \widehat W_R(\nu)
 e\!\left(\left(\nu-{g\over2}\right){\Lambda_q\over k}\right)
 \mathfrak B^\circ_{a,q,k}(g).
 \tag{104.R2}
\]

There are two equivalent ways to view (104.R2).

1. In centered coordinates, the actual theorem proves that
   \(\mathfrak B^\circ_{a,q,k}(g)\), together with the literal remaining
   multiplier, has sampled \(k\)-variation
   \(O_\varepsilon(X^\varepsilon\sqrt{AL/(JD)})\). One may then apply
   the reciprocal second-derivative estimate to the displayed phase.
2. Using (104.R1), the same term becomes
   \(e(\nu\Lambda_q/k)\) times a moving physical Fourier coefficient.
   The carrier oscillation is now inside that coefficient. A direct
   Parseval estimate is valid but weaker; recovering the sharp bound
   requires exactly the dephasing information supplied by the complete
   centered-integral variation theorem.

There is no multiplication of two independent stationary gains. The
complete centered variation is a structural theorem about the literal
coefficient, not a generic pointwise bound. It identifies and removes the
phase already carried by the physical Fourier coefficient before the
remaining metric reciprocal phase is estimated.

## Why the blind report stopped

The blind packet intentionally omitted the actual homogeneous amplitude,
its normalized profile seminorms, the precise owner placement, and the
complete row formula. From that statement-only packet, one cannot prove
that the centered coefficient has small sampled variation; arbitrary
phase-conjugated amplitudes give a valid falsifier of any
coefficient-uniform version.

The discovery proof and hostile audit supplied precisely the missing
literal facts:

- the \(k\)-independent homogeneous physical amplitude;
- the exact differential identity converting \(k\)-motion into a
  physical derivative;
- resolved fixed collars with parameter \(JD/(AL)\);
- all moving metric data opened outside the BV amplitude;
- no surviving jagged exterior owner.

Therefore the blind conclusion is retained as a route control and an
isolation success, while its underdetermination verdict does not apply
after the actual-symbol hypotheses are restored.

## State implication

Reject both overstatements:

- carrier cancellation alone forbids an actual sampled-\(k\) proof;
- reciprocal curvature may be applied to an arbitrary centered
  coefficient.

The certified statement lies strictly between them: the literal actual
centered coefficient has the required variation, and only then may the
complete metric reciprocal modes be estimated.
