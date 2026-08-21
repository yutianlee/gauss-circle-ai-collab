# Round 105 conductor two-step transform normalization

Campaign: m9-m2-polynomial-q-maximal-alternation

## Scalar phase

For the orientation with \(g-2\nu=n>0\), write

\[
 \Phi(q,k)={q\over2}-{n\over2}{\Lambda_q\over k},
 \qquad
 \Lambda_q={X(\sqrt{a+2q}-\sqrt a)^2\over2}.
 \tag{105.T1}
\]

This review tracks only the scalar stationary phase. It does not claim
that the complete actual symbol may be replaced by its leading term.

## First stationary transform

Poisson or a \(B\)-process in \(k\), with positive dual integer
\(\ell\), has saddle

\[
 k_*=\sqrt{n\Lambda_q\over2\ell}.
\]

At the saddle,

\[
 -{n\Lambda_q\over2k_*}-\ell k_*
 =-2\sqrt{n\Lambda_q\ell\over2}
 =-J(\sqrt{a+2q}-\sqrt a)\sqrt{n\ell}.
\]

Thus the reduced \(q\)-phase is

\[
 F(q)={q\over2}
 -J(\sqrt{a+2q}-\sqrt a)\sqrt{n\ell}.
 \tag{105.T2}
\]

## Second stationary transform

Pair \(F\) with \(e(-rq)\). Its saddle equation is

\[
 {1\over2}-{J\sqrt{n\ell}\over\sqrt{a+2q}}-r=0.
\]

Set \(s=1-2r\), an odd positive integer in the relevant orientation.
Then

\[
 b_*=a+2q_*={4Xn\ell\over s^2}. \tag{105.T3}
\]

At this saddle,

\[
\begin{aligned}
 F(q_*)-rq_*
 &= {s(b_*-a)\over4}
 -J\sqrt{n\ell b_*}+J\sqrt{an\ell}\\
 &=-{Xn\ell\over s}-{sa\over4}+J\sqrt{an\ell}\\
 &=-\left(J\sqrt{n\ell\over s}-{\sqrt{as}\over2}\right)^2.
\end{aligned}
 \tag{105.T4}
\]

The alternating \(q\)-factor has become the odd dual variable \(s\), and
the phase is again a centered quadratic square.

## Interpretation gate

Equations (105.T1)--(105.T4) strongly suggest that a black-box
two-dimensional Hessian or successive stationary transform will
self-return to an actual centered row after all amplitudes and owners are
restored. This is not yet a theorem:

- the complete metric Fourier sum has both orientations;
- stationary entry, exit, and collars must remain complete;
- the primitive mask and prior owners move under the transforms;
- the two Gaussian units and Jacobians must be checked;
- nonstationary and endpoint remainders must aggregate at target scale.

Therefore the identity is a mandatory no-double-count control. It does
not disprove the maximal alternating theorem, which might still use
cancellation across the returned odd \(s\)-rows rather than absolute
summation.
