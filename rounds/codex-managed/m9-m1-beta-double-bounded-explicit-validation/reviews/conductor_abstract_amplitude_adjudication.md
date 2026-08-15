# Conductor adjudication: corrected abstract compact amplitude

Campaign: `m9-m1-beta-double-bounded-explicit-validation`

## Decision

The finite-family analytic estimate is valid after restoring two hypotheses
already present in the actual contour/profile construction:

\[
0\le a,\qquad a+b<\frac12,\qquad \frac a2+b<\frac14,
\]

and

\[
 |M_\tau|+|x\partial_xM_\tau|+|\partial_LM_\tau|
 \ll \log^C(2Xhq).
\]

It is not valid as a theorem of the literal frozen packet, which printed
only the two upper contour inequalities. In particular the packet admits
negative \(a\); then either the absolute \(q\)-series diverges or the last
active dyadic scale has polynomial size. The actual project contour has
\(a\ge0\), so this is a statement defect rather than an obstruction to the
method.

## Local proof check

On the compact \((L,\beta)\)-support,

\[
 |A|\asymp1,\qquad |D|\asymp1+|\nu|.
\]

For the singular share the recombined divided difference obeys

\[
 \int_{\mathbb R}
 \frac{|p(\nu)-p(L)|}{|L-\nu|\,|D|}\,d\nu
 \ll \log^C(2X).
\]

The near-diagonal part uses \(p'\); the complement uses the displayed
\(L^1\), first-moment, and cubic-tail bounds. Differentiation in \(x\)
must include all three phase contributions and the multiplier derivative:

\[
 x\partial_x\{M_\tau E(L,\beta,x)p_{j,x}(\nu)\}
 =E\{x\partial_xM_\tau-i((L+\nu)/2+\beta)M_\tau\}p_{j,x}(\nu).
\]

At \(\nu=L\) the corresponding divided-difference numerator vanishes.
The smooth shares follow by ordinary absolute convolution with their fixed
Schwartz profiles.

With \(r=5/4-(a+b)/2\), \(p=5/4+(a+b)/2\), the actual contour gives
\(r-1>b/2\) and \(p\ge5/4\), so the \(h,q\) sums, including fixed
logarithmic weights, cost only a power of \(\log X\). Moreover

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b\ll1
\]

on every active scale, including \(H_j=1\), and there are \(O(\log X)\)
scales. Thus the corrected abstract family satisfies

\[
 \sup_x\{|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\}
 \ll\log^C(2X).
\]

This review does not promote that statement because the assigned strict
statement-only run was contaminated by graph exposure, and because the
abstract family has not yet been proved equal to the actual one-count
operator.

## Controls

- Signed top constant and PV orientation: pass.
- Full \(x\)-derivative, including \(x\partial_xM_\tau\): pass after repair.
- Absolute \(h,q\) and exact active-scale sums: pass for the actual
  \(a\ge0\) contour; fail for the literal packet.
- Radial endpoint coefficients: full, not half.
- External \(X^{1/4}\) normalization: owned once only after the actual
  operator identity is established.

## State recommendation

Retain the actual compact-cell obligation as open. Carry the corrected
analytic lemma into a new packet only after supplying selectors and the
complete ownership table, and obtain a genuinely isolated rederivation.

