# Round 105 conductor preliminary review

Campaign: m9-m2-polynomial-q-maximal-alternation

Starting graph SHA-256:
f8f20833d2f24fa0b323488e247887ba943b8dffdd3eacb58e5bae773eb5831b

## Maximal-to-Gram implication

Suppose

\[
 \mathcal M_a(D)
 =\sup_{I\subset[D,2D)}
 \left|\sum_{q\in I}(-1)^qF_a(q)\right|
 \ll_\varepsilon X^\varepsilon {L^2\over A}.
 \tag{105.R1}
\]

Choose \(H\asymp D\). After zero extension, only \(O(D)\) starting
points \(n\) have a window intersecting the \(q\)-shell. Each such
window is an interval from (105.R1), so

\[
 \mathcal G_H^{\rm act}
 \ll AD\left(X^\varepsilon{L^2\over A}\right)^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}.
\]

Since

\[
 {H^2L^4\over AD}\asymp {DL^4\over A},
\]

the maximal theorem closes the full fixed-\(a\) Gram exactly. No
additional \(D\)-power is hidden.

## Adjacent transport

For the centered saddle

\[
 r_{q,k}={J(\sqrt{a+2q}-\sqrt a)\over2k},
\]

one has

\[
 \partial_q r_{q,k}={J\over2k\sqrt{a+2q}},
\]

and

\[
 \partial_q e(gk(y-r_{q,k})^2)
 =-(\partial_q r_{q,k})\partial_y
 e(gk(y-r_{q,k})^2).
 \tag{105.R2}
\]

Thus continuous \(q\)-motion of the complete centered phase can be paid
by one physical derivative. This is only one seam: the actual amplitude,
metric factor, integer \(k\)-sample, lift support, primitive mask, and
prior owners also move.

Both reciprocal endpoints are monotone functions of \(q\). Hence, after
zero extension, any fixed integer \(k\) enters and exits the reciprocal
support at most once. This removes a possible combinatorial source of
large variation, but does not estimate the metric phase.

Primitivity has the exact expansion

\[
 \mathbf1_{(a,q)=1}
 =\sum_{\substack{d\mid a\\d\mid q}}\mu(d).
\]

Since \(a\) and every \(d\mid a\) are odd, writing \(q=dr\) preserves
the alternation:

\[
 (-1)^q=(-1)^{dr}=(-1)^r.
\]

The divisor cost is absorbable, but the rescaled moving symbol must still
be controlled on each progression.

## Complete joint phase

For one metric mode, insert the alternation into

\[
 \Psi(q,k)={q\over2}+c{\Lambda_q\over k},
 \qquad c=\nu-{g\over2},
\]

where

\[
 \Lambda_q=X\left(a+q-\sqrt{a(a+2q)}\right).
\]

Let \(t=\sqrt{(a+2q)/a}\). Then

\[
 \Lambda_q={Xa(t-1)^2\over2},\qquad
 \Lambda_q'=X{t-1\over t},\qquad
 \Lambda_q''={X\over at^3}.
\]

The exact Hessian determinant is

\[
\begin{aligned}
 \det\nabla^2_{q,k}\Psi
 &= {c^2\over k^4}
 \left(2\Lambda_q\Lambda_q''-(\Lambda_q')^2\right)\\
 &=-{c^2X^2(t-1)^3\over t^3k^4}
 \asymp -{n^2A\over D},
 \qquad n=|2\nu-g|.
\end{aligned}
 \tag{105.R3}
\]

Thus the opened scalar phase is genuinely full rank in \((q,k)\), even
though earlier larger physical phases had homogeneous null directions.
This does not yet prove a gain: two-dimensional completion may reconstruct
the original physical rows, and the actual hard owner is not a generic
smooth scalar amplitude.

## Adjudication fork

The round must decide between three distinct statements:

1. complete total \(q\)-variation at one-row scale;
2. maximal alternation without total variation, using joint oscillation;
3. self-return or actual coherence leaving a smaller Gram kernel.

An arbitrary sequence \(F_a(q)=(-1)^qL^2/A\) rejects every
coefficient-uniform form but is not an actual-symbol obstruction. No graph
effect follows until the literal owner and resonant-family audits finish.
