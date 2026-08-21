# Conductor review: joint physical--reciprocal--ray stationary normalization

Campaign: m9-m2-dual-square-actual-symbol-transfer

Starting graph SHA-256:
2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de

## Scope

This review checks only the smooth interior principal branch. It does not
license any owner, cutoff or transition transport.

Fix \(c=\nu-g/2=-n/2\), \(n>0\), expand \(q=du\), and open the centered
physical integral with \(y=\sqrt x\). After the \(k\)- and \(u\)-Poisson
dual integers \(\ell,h\), the full phase is

\[
\begin{aligned}
 \Phi(y,k,u)
 ={}&{du\over2}-hu-\ell k
 +gky^2-gJ(\sqrt{a+2du}-\sqrt a)y\\
 &+{\nu\Lambda_{du}\over k}.
\end{aligned} \tag{106.R1}
\]

This is the correct object for checking whether the centered integral may
be treated as a scalar amplitude.

## Joint saddle

The \(y\)-equation gives

\[
 y_*={J\delta\over2k_*}.
\]

Substitution into the \(k\)-equation gives

\[
 \ell={n\Lambda\over2k_*^2},
 \qquad
 k_*^2={n\Lambda\over2\ell},
 \qquad
 y_*^2={\ell\over n}. \tag{106.R2}
\]

The \(u\)-equation then gives, with \(s=d-2h\),

\[
 b_*=a+2du_*={4d^2Xn\ell\over s^2}. \tag{106.R3}
\]

The exact stationary value is

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}. \tag{106.R4}
\]

Thus the sequential scalar saddle is also the genuine joint saddle of
the opened physical integral.

## Hessian and Gaussian unit

For fixed \(u\), the \((y,k)\)-Hessian at the saddle has determinant

\[
 \det
 \begin{pmatrix}
 2gk_*&2gy_*\\
 2gy_*&2\nu\Lambda/k_*^3
 \end{pmatrix}
 =-{2gn\Lambda\over k_*^2}. \tag{106.R5}
\]

It has one positive and one negative eigenvalue, hence Gaussian unit
one. The physical \(e(1/8)\) and scalar \(k\)-process \(e(-1/8)\)
are not independent gains; they are the two one-dimensional factors of
this signature-zero saddle.

After eliminating \((y,k)\), the reduced \(u\)-curvature is

\[
 {d^2J\sqrt{n\ell}\over b_*^{3/2}}>0, \tag{106.R6}
\]

so the full three-variable Gaussian unit is \(e(1/8)\).

## Principal amplitude

The opened physical amplitude is

\[
 Q_{a,du,g}(y)=2gy\,A^\circ_{ga,g(a+2du)}(gy^2).
\]

Using (106.R5),

\[
 {Q(y_*)\over\sqrt{|\det H_{y,k}|}}
 =\sqrt{g/n}\,
 A^\circ_{ga,gb_*}(g\ell/n). \tag{106.R7}
\]

Multiplication by the reduced \(u\)-Hessian factor from (106.R6) gives

\[
 \boxed{
 e(1/8)\,
 {g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}\,
 A^\circ_{ga,gb_*}(g\ell/n).} \tag{106.R8}
\]

Therefore the candidate principal normalization in the derivation packet
is correct on the smooth interior. A proof still needs uniform all-orders
or exact-Fresnel control through the physical and arithmetic transitions.

## Hyperbolic change of variables

Write

\[
 H={a\over d},\qquad M=dn\ell,\qquad r=s.
\]

Then

\[
 a\,n\ell=HM,\qquad
 {dXn\ell\over s}={XM\over r},
\]

and the phase becomes

\[
 -{XM\over r}-{Hr\over4}+J\sqrt{HM}. \tag{106.R9}
\]

Since \(H,r\) are odd,

\[
 e(-Hr/4)=-i\chi_4(H)\chi_4(r). \tag{106.R10}
\]

The dual carrier is therefore an exact two-character reciprocal/product
kernel

\[
 \chi_4(H)\chi_4(r)
 e(-XM/r+J\sqrt{HM}), \tag{106.R11}
\]

with a moving actual symbol. This makes the resemblance to the original
top M2 transposed row literal at carrier level. It also shows why the
terminal one-dimensional M1 theorem cannot be invoked before the
\(M\)-weight, congruence, and owner dependence are audited.

## Capacity check

On a noncollapsing interior box,

\[
 \ell\asymp nA,\qquad
 \#\{\ell\}\asymp nA,\qquad
 \#\{s\ {\rm per}\ \ell\}\asymp {dnJD\over A}.
\]

The principal point size from (106.R8) is

\[
 \asymp {\sqrt{L/J}\over dn}.
\]

Hence one fixed \((d,g,\nu)\) packet has

\[
 \#\text{ points}\asymp dn^2JD,
 \qquad
 \ell^2\text{ capacity}\asymp\sqrt{LD/d}. \tag{106.R12}
\]

The \(d=1\) packet is \(\sqrt D\) larger than one-row
\(\sqrt L\) capacity. Even ideal square-root cancellation on the dual
points therefore does not supply the full maximal theorem or the
factor-\(D\) Gram gain.

## Decision

Equations (106.R2)--(106.R12) pass as an interior normalization and
capacity review. They do not prove a complete transform, a terminal M1
specialization, a strict polynomial range, or an owner-preserving
self-return. Those remain the Round-106 gates.
