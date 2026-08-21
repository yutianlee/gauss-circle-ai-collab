# Round 105 synthesis: maximal \(q\)-alternation and the dual-square return

Campaign: m9-m2-polynomial-q-maximal-alternation

Starting graph SHA-256:
f8f20833d2f24fa0b323488e247887ba943b8dffdd3eacb58e5bae773eb5831b

Resulting graph SHA-256 after the validated State Patch:
2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de

## Frozen objective

The round asked whether the complete fixed-\(a\) row satisfies

\[
 \mathcal M_a(D)=\sup_{I\subset[D,2D)}
 \left|\sum_{q\in I}(-1)^qF_a(q)\right|
 \ll_\varepsilon X^\varepsilon {L^2\over A},
\]

or whether an exact adjacent-transport or joint-phase analysis could close
any fixed positive-power \(q\)-shell.

## Exact logical ledger

The maximal theorem would close the fixed-\(a\) Gram exactly.  For
\(H\asymp D\), zero extension leaves \(O(D)\) nonzero windows for each of
\(O(A)\) bases, hence

\[
 \mathcal G_H^{\rm act}
 \ll AD\left(X^\varepsilon {L^2\over A}\right)^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}
 \asymp X^\varepsilon {H^2L^4\over AD}.
\]

The accepted fixed-row theorem alone gives maximal capacity
\(DL^2/A\) and direct-Cauchy Gram capacity \(H^2DL^4/A\).  Its exact
deficits are \(D\) in amplitude and \(D^2\) in energy.  Even generic
square-root cancellation would leave a factor \(D\) in the Gram.

Total adjacent variation is sufficient but not necessary.  The exact
Gram is the weaker signed shift aggregate

\[
 \sum_{|r|<H}(H-|r|)(-1)^r
 \sum_{a,q}F_a(q)\overline{F_a(q+r)}.
\]

## What adjacent transport controls

Put

\[
 r_{q,k}={J\delta_q\over2k},\qquad
 c=\nu-{g\over2}.
\]

The centered saddle obeys

\[
 \partial_q e(gk(y-r_{q,k})^2)
 =-r'_{q,k}\partial_y e(gk(y-r_{q,k})^2),
\]

including the exact moving-boundary terms after differentiation of the
physical integral.  Both reciprocal endpoints are monotone in \(q\), so
each fixed integer \(k\) enters and exits at most once.

The complete mode, however, recouples exactly as

\[
 c{\Lambda_q\over k}+gk(y-r_{q,k})^2
 =\nu{\Lambda_q\over k}+gky^2-gJ\delta_qy.
\]

Thus centered transport leaves the residual
\(c\Lambda_q'/k\asymp nJ\), where \(n=|2\nu-g|\).  The density mode
\(\nu=0\) is the original physical phase, not a removable zero mode.
Consequently smooth material transport alone does not prove small total
\(q\)-variation.

There is also no uniform derivative gap.  At the simultaneous open
reciprocal/physical saddle corner,

\[
 {\Lambda_q'\over k_+(q)}=J.
\]

Fourth-power parity can make the scalar derivative integral.  The corner
is flat-collarized and therefore gives no actual lower bound, but it
rejects a gap-based shortcut.

## Full Hessian and exact primitive dual square

With \(t=\sqrt{(a+2q)/a}\), the scalar phase

\[
 \Psi(q,k)={q\over2}+c{\Lambda_q\over k}
\]

has

\[
 \det\nabla^2_{q,k}\Psi
 =-{c^2X^2(t-1)^3\over t^3k^4}
 \asymp-{n^2A\over D}.
\]

This full rank is representation-induced rather than a free gain.  Expand
primitivity exactly,

\[
 \mathbf1_{(a,q)=1}
 =\sum_{d\mid a,\,d\mid q}\mu(d),\qquad q=du.
\]

Every \(d\mid a\) is odd, so alternation is preserved.  A scalar
\(k\)-process followed by a scalar \(u\)-process has odd dual
\(s=d-2h\) and exact phase

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{dn\ell/s}-{1\over2}\sqrt{as/d}\right)^2.
\]

Moreover

\[
 e(-as/(4d))=-i\chi_4(a/d)\chi_4(s).
\]

The alternating lattice therefore returns an odd-character reciprocal
and square-root-product carrier.  A determinant-only theorem or another
absolute transform estimate merely changes representation at equal
capacity.

This statement is deliberately carrier-level.  The transformed actual
owners, finite lift fibres, profiles, collars, floors, stars, metric
modes, maximal cutoff, and aggregate stationary remainders have not been
matched into one complete dual theorem.  Hence it is not an
owner-preserving self-return theorem and not an actual-symbol lower bound.

## Primitive mask and hostile controls

The primitive mask itself is benign:

\[
 \left|\sum_{q\in I}(-1)^q\mathbf1_{(a,q)=1}\right|
 \le\tau(a).
\]

Its raw variation can nevertheless be of order \(D\), confirming that
total variation is an unnecessary strengthening.  Multiplication by the
moving metric coefficient is exactly the open step.

Coherent arbitrary coefficients can violate the maximal theorem by a
factor \(D\), but they do not satisfy the actual Fresnel/profile structure.
Square, Pell, near-square, and fourth-power rows rule out generic
Diophantine and derivative-gap shortcuts; prior square owners, punctured
exact centers, and flat collars prevent them from supplying a certified
lower bound for the residual actual sum.

No audited external theorem accepts the coupled maximal actual amplitude.
The accepted terminal M1 divisor theorem requires a separable fixed-shell
BV symbol and does not apply to the transformed
\((a,d,n,\ell,s)\)-dependent amplitude with its radial factor.

## Conductor decision

Promote only the exact transport residual, endpoint monotonicity, scalar
Hessian, and primitive dual-square character reduction as a scoped
internal lemma and route obstruction.

Retain open:

- the bounded maximal theorem and every fixed positive-power \(q\)-shell;
- the complete fixed-\(a\) actual Gram;
- the canonical hard density-discrepancy energy and signed cone;
- both smooth M2 packets;
- M9-M2, M9-M1, endpoint uniformity, M9, and the quarter target.

The statement-only report is mathematically useful but not exposure-free:
it accidentally saw the campaign manifest and proof-graph tail before
quarantining them.  It is therefore supporting evidence, not the sole
promotion gate.

No global exponent changes.  The certified external exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

and the strongest internal uniform exponent remains \(1/3\).

## Next interface

The smallest literal survivor is the complete actual-vector version of
the primitive dual square above.  The next round should first derive its
full amplitude, owner, support, collar, maximal-cutoff, and stationary
error dictionary.  Only then should it test a reciprocal-character
estimate or return to the weaker original weighted shift aggregate.  A
successful estimate must recover the full factor \(D\); another generic
square-root or determinant gain is insufficient.
