# Round 128 conductor adjudication: the character-split coefficient gate passes

Campaign: `gc-w7-16-local-transverse-lift-variation-gate`

Starting graph SHA-256:
`1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`

## 1. Decision

Promote the local coefficient estimate only in its exact character-split
form.  For the two M1 quarter-phase branches and the single M2 branch,

\[
 \|U_{i,\rho,\eta}\|_{V^2(I)}
 \ll_\varepsilon {J_B^{1/2}\over L}Y^\varepsilon,
 \qquad
 J_B=1+{DQ_B\over B^2}.
 \tag{128.J1}
\]

The proof is the discrete-Stieltjes/character-Abel argument below.  It
includes both displayed endpoint values, the smooth denominator profile,
hard top, prescribed star, floors, support entry and exit, the determinant
taper, divisor progressions, and half-open shell ownership.

Reject the unsplit M1 formulation.  If \(\chi _4(b')\) is left in the
amplitude, its dense transverse alternation gives

\[
 \|\chi _4(\rho\,\cdot)R_1(a',\rho\,\cdot)\|_{V^2}
 \gg {Q_B^{1/2}\over L}
 \tag{128.J2}
\]

on an interior one-lift top-shell packet, whereas \(J_B\asymp1\).  The
literal identity

\[
 \chi _4(b')={e(b'/4)-e(-b'/4)\over2i}
\]

moves this factor into the two already prescribed quarter-linear carrier
phases.  This is exact algebra, not a weakening of the physical sum.

The subsequent joint \(V^2\)-weighted reciprocal-curvature inequality is
still open.  Therefore the conditional \(Y^{73/96+\varepsilon}\) complete
block bound is not promoted, and no global exponent or M9 status changes.

## 2. Literal dictionary and the restricted hostile review

The accepted Round-95 source gives, before any norm,

\[
 \begin{aligned}
 A_1(a,b)&={2\chi _4(b)\over\pi ia}
  \sum_g{\chi _4(g)\over g}
  \Phi(g|a|/(H+1))v_L(g|a|)\omega_{1,D}(gb),\\
 A_2(a,b)&=-{4\chi _4(|a|)\over\pi|a|}
  \sum_g{\chi _4(g)\over g}
  \Phi(g|a|/(H+1))v_L(g|a|)\omega_{2,D}(gb).
 \end{aligned}
 \tag{128.J3}
\]

All literal support indicators and the star are included in this formula.
On a fixed moving-symbol stratum, \(H\), the prefix, and every time floor
are fixed.  Consequently the lift weight factors into a frequency-only
sampled-BV sequence and a denominator-only sampled-BV sequence.  There is
no residual support coupling \(ga'\) and \(gb'\).

The hostile report correctly found that the shorthand
\(I_{i,\rho}(v),\omega_i(g,a',\rho v)\) in the Round-127 candidate was not
itself a literal dictionary.  Under its restricted context, refusal to
certify was mandatory.  The conductor supplied the exact Round-95 source
to the discovery audit and checked it directly.  Formula (128.J3) meets
the hostile report's necessary character-BV criterion, while (128.J2)
confirms its warning about dense M1 parity.  Thus the final decision is not
a vote against the hostile review: its abstract no-go is promoted, and
its missing hypothesis is verified from the accepted literal formula.

## 3. BV-threshold proof

The finite analytic kernel is the following lemma.  Let \(P\) be supported
on \(g\asymp G\), let \(w\) be supported on \(d\asymp D\), and suppose
their zero extensions have bounded supremum plus discrete variation.  If
\(|a|G\asymp L\), \(b'=\rho v\asymp B\), and the physical \(b'\)-window
has length at most \(Q\), set

\[
 R(v)={1\over a}\sum_g{\chi _4(g)\over g}P(g)w(g\rho v).
 \tag{128.J4}
\]

Bounded partial sums of \(\chi _4\) and Abel summation give, for every
integer interval \(J\subset[g\asymp G]\),

\[
 \left|\sum_{g\in J}{\chi _4(g)\over g}P(g)\right|
 \ll G^{-1}.
 \tag{128.J5}
\]

Zero-extend \(w\), put \(c_t=w(t)-w(t+1)\), and use the exact identity

\[
 w(d)=\sum_{t\ge d}c_t,
 \qquad \sum_t|c_t|=\operatorname {Var}(w).
 \tag{128.J6}
\]

Then

\[
 R(v)=\sum_t c_t R_t(v),\qquad
 R_t(v)={1\over a}
 \sum_{g\le t/(\rho v)}{\chi _4(g)\over g}P(g).
 \tag{128.J7}
\]

Both endpoint values of \(R_t\) are \(O(L^{-1})\).  The monotone floor
\(\lfloor t/(\rho v)\rfloor\) changes on at most

\[
 O\!\left(1+{tQ\over B^2}\right)
 =O\!\left(1+{DQ\over B^2}\right)
 \tag{128.J8}
\]

consecutive \(v\)-steps.  Each difference is one interval sum, even when
one progression step skips several lift integers, and hence is again
\(O(L^{-1})\) by (128.J5).  It follows that

\[
 \|R_t\|_{V^2(I)}\ll {1\over L}
 \left(1+{DQ\over B^2}\right)^{1/2}.
\]

Minkowski in the vector consisting of the left endpoint, all consecutive
differences, and the right endpoint, followed by (128.J6), proves the same
bound for \(R\).  This exact threshold superposition is why the smooth
profile is controlled by \(J_B\); the birth count alone would not control
an arbitrary moving coefficient.

Multiplication by a scalar \(b'\)-weight with bounded supremum and total
variation preserves the result.  The one-sided determinant taper is such
a weight on each clipped interval, and zero-extension adds only two
bounded jumps.  A physical window meets only \(O(1)\) half-open reduced
denominator shells.  The estimate is uniform in each \(\rho\mid a'\), and
the later absolute divisor sum costs only \(Y^\varepsilon\).

Applying the lemma to (128.J3), with
\(G=D/B\), \(|a'|G\asymp L\), \(Q=Q_B\), proves (128.J1).

## 4. False controls and normalization

The statement-only audit constructs a fixed-window adversary
\(\omega_v(g)=L^{-1}\chi _4(g)(-1)^v\), for which the outside
\(\chi _4(g)\) is conjugated and the norm can be
\(\asymp G\sqrt N/L\) with zero births.  A constant-in-\(v\) version
already violates the two endpoint terms.  These controls prove that
support size, pointwise scale, a common character, and a birth count do
not imply (128.J1).

The physical factor in (128.J3) cannot realize that lift conjugation: its
frequency factor has bounded sampled variation, so (128.J5) applies before
the modulus.  In contrast, the reduced M1 factor really does oscillate at
every transverse step.  It is therefore extracted exactly into the two
carrier phases.  The common lift character stays inside the lift sum;
interchanging these two ownership decisions would invalidate the proof.

## 5. Remaining theorem and capacity

The only live hypothesis in the Round-127 connector is now

\[
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right)\right|
 \ll_\varepsilon
 \|U_{i,\rho,\eta}\|_{V^2(I)}
 \min\!\left(N_\rho,
 N_\rho\sqrt{\lambda_B\rho^2}
 +(\lambda_B\rho^2)^{-1/2}\right)Y^\varepsilon.
 \tag{128.J9}
\]

This is not a generic consequence of the \(V^2\) norm.  Partial summation
and Cauchy insert an extra \(N_\rho^{1/2}\), and an arbitrary amplitude
can adapt to the phase.  A continuation must use the joint
Stieltjes/character/reciprocal structure of the actual family and must not
separate the complete lift transform before the \(v\)-sum.

If (128.J9) is eventually proved, the connector gives the complete fixed
block \(Y^{73/96+\varepsilon}\), a strict \(Y^{1/96}\) improvement over
\(Y^{37/48+\varepsilon}\).  Its persistence exponent is
\(115/288>1/3\), so even that conditional success would not improve the
current global theorem.

## 6. Conductor state decision

Promote the branchwise BV-threshold coefficient lemma and the abstract plus
unsplit-M1 normalization obstruction.  Revise the conditional connector so
only (128.J9) remains open.  Retain the determinant correlation, M9-M1,
M9-M2, endpoint uniformity, M9, the conditional bridge, and the Gauss
circle target as open.  No numerical experiment or external theorem is
used.
