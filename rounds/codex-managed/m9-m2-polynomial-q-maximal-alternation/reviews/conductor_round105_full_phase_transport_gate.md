# Round 105 conductor full-phase transport gate

Campaign: m9-m2-polynomial-q-maximal-alternation

## Exact recoupling

For one orientation, put

\[
 r_{q,k}={J\delta_q\over2k},\qquad
 \Lambda_q={J^2\delta_q^2\over2},\qquad
 c=\nu-{g\over2}.
\]

The centered carrier and the metric mode satisfy the exact identity

\[
 c{\Lambda_q\over k}+gk(y-r_{q,k})^2
 =\nu{\Lambda_q\over k}+gky^2-gJ\delta_qy. \tag{105.F1}
\]

Thus the half-integral carrier is not an independent oscillation.  It
recouples with the centered integral to give the literal uncentered
physical phase.  In particular, the density mode \(\nu=0\) remains a
genuine physical oscillation; it is neither absent nor a formal zero
frequency.

## Transport residual

The exact centered transport identity gives

\[
 \partial_q e\!\left(gk(y-r_{q,k})^2\right)
 =-r_{q,k}'\partial_y
 e\!\left(gk(y-r_{q,k})^2\right).
\]

After the metric mode is restored, however,

\[
 \partial_q e\!\left(c{\Lambda_q\over k}
          +gk(y-r_{q,k})^2\right)
 =-r_{q,k}'\partial_y e(\cdots)
  +2\pi i\,c{\Lambda_q'\over k}e(\cdots). \tag{105.F2}
\]

On the active scales,

\[
 \left|c{\Lambda_q'\over k}\right|\asymp nJ,
 \qquad n=|2\nu-g|.
\]

Consequently the physical derivative in (105.F2) can control the motion
of the centered saddle and all smooth collars, but it does not prove the
transported total-variation estimate (105.4).  The remaining term is
exactly the full metric oscillation that a signed \(q\)-argument must
estimate.  Bounding it by absolute differentiation loses a positive
power much larger than the allowed one-row scale.

This is a route obstruction, not a lower bound for the actual maximal
sum: the residual may still cancel after summing \(q,k,g,\nu\).

## Boundary resonance control

At the upper reciprocal endpoint

\[
 k_+(q)={J\delta_q\over\sqrt{a+2q}},
\]

one has the exact identity

\[
 {\Lambda_q'\over k_+(q)}=J. \tag{105.F3}
\]

Hence the alternating scalar phase has integral derivative at the
simultaneous physical-saddle corner whenever the relevant parity of
\(nJ\) matches.  This is a mandatory hostile control against any claimed
uniform derivative gap.  The corner itself lies on the open reciprocal
endpoint and on the smooth physical collar, so (105.F3) alone is not an
actual-symbol counterexample: a lower bound would have to retain the
literal collar amplitude and its zero-extension convention.

## Consequence for adjudication

Round 105 can promote a polynomial shell only from a genuinely signed
maximal or Gram estimate for the complete recoupled phase (105.F1).
Smooth adjacent transport by itself controls only the moving centered
integral.  A black-box total-variation proof that differentiates the
exterior metric multiplier, or a derivative-gap proof that discards the
corner (105.F3), is not sufficient.
