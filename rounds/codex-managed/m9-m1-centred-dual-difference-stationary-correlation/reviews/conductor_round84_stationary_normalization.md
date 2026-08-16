# Round 84 conductor stationary-normalization review

Campaign: `m9-m1-centred-dual-difference-stationary-correlation`

Starting graph SHA-256:
`b744aa885442ec9be13913782471cf65a94cd794579f8c6a8fbb2854ce52e271`

## Decision

The scoped small-dual-difference deletion passes.  For the smooth
neighbor-independent principal coefficient from Round 81, every

\[
 0<|d|\leq D_0:=\lfloor J^{17/30}\rfloor
\]

is target-safe in the complete centered correlation, in all three local
classes and both orientations.  This is a strict reduction of the
survivor, not a fixed power of \(B\), a conductor extension, or an
estimate for the remaining differences.

The statement-only report correctly warns that bounded variation alone
does not justify a leading stationary symbol.  The promoted proof does
not make that inference: it uses the accepted Round-81 exact smooth
extension (81.A2)--(81.A3), transferred through the monotone saddle map.

## Exact saddle and normalization

Use the class-independent \(c\)-coordinate.  With

\[
 g\in\{1,2,4\},\qquad M={4b\over g},\qquad
 A=\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2,
\]

the Fourier integral is

\[
 I_b(n)={1\over g}\int V_b(c)
 e\!\left(-{A\over c}-{nc\over4b}\right)dc.
 \tag{84.N1}
\]

For the stationary sign and \(m=|n|>0\),

\[
 c_m=\sqrt{{4bA\over m}},\qquad
 \lambda_b=\sqrt{{A\over b}}
 =\sqrt X+{\sqrt{\kappa k}\over b},
 \tag{84.N2}
\]

and the exact critical phase is

\[
 -\lambda_b\sqrt m.
\]

The stationary coefficient is

\[
 \Delta_m={A^{1/4}M^{3/4}\over
 \sqrt2\,g^{1/4}m^{3/4}}
 \asymp H:={C\sqrt T\over J}.
 \tag{84.N3}
\]

The exact Morse coordinate gives Gaussian \(e(-1/8)\) for one
orientation and its conjugate for the reflected orientation.  The
stationary scale is \(m\asymp Q^2\), and the large parameter is

\[
 \Lambda={A\over C}\asymp JQ=J^{7/5}.
 \tag{84.N4}
\]

The discovery report retains the incomplete Gaussian as the saddle
enters and leaves each fixed smooth support chart.  Round 81's principal
coefficient has the neighbor-independent extension (81.A2)--(81.A3);
its pointwise-small Farey transition remainder is a different object and
is not transformed here.

## Sampled profile and error seam

The saddle map

\[
 m={4bA\over c_m^2},\qquad {dc_m\over dm}=-{c_m\over2m}
\]

is monotone.  On one progression \(m=r+M\ell\), a fixed point of the
\(c\)-support lies in at most

\[
 O\!\left(1+{Q^2\over M\sqrt\Lambda}\right)
\]

sampled Morse neighborhoods.  Fubini applied to (81.A3), together with
the one-pass variation of the exact incomplete Gaussian, therefore gives

\[
 \|\mathcal W\|_\infty+operatorname {Var}_\ell\mathcal W
 \ll_\varepsilon X^\varepsilon H.
 \tag{84.N5}
\]

For the product of two profiles separated by \(|d|\leq D_0=o(Q^2)\),
the aggregate profile-remainder ledger on a progression is

\[
 \ll_\varepsilon X^\varepsilon
 {H^2Q^2\over M\sqrt\Lambda}.
 \tag{84.N6}
\]

Wrong-sign and far nonstationary tails are summable.  After the residue,
\(b\), and \(d\) sums, (84.N6) and the far tails contribute respectively

\[
 X^\varepsilon {DC^2\over T\sqrt{JQ}},\qquad
 X^\varepsilon {DB^2\over Q^2},
 \tag{84.N7}
\]

both strictly below \(J^2/T\) for \(D\leq D_0\).  This checks the first
seam identified by the blind report: the proof uses actual smooth
antecedent regularity, not arbitrary BV data.

## Arithmetic coefficient mass

For every integer \(d\), exact orthogonality gives

\[
 \sum_{r\bmod M}|S(r,K;M)|^2=M\varphi(M).
\]

Consequently

\[
 {1\over M^2}\sum_{r\bmod M}
 \left|S(r+d,K;M)\overline{S(r,K;M)}-c_M(d)\right|
 \leq2.
 \tag{84.N8}
\]

This identity has no hidden gcd loss and does not require \((K,M)=1\).
It includes the two even local classes, prime powers, negative \(d\), and
nonzero multiples \(d\equiv0\pmod M\).  Literal \(d=0\) remains removed
exactly once.

## Curvature and exponent ledger

For \(n=r+M\ell\asymp Q^2\), the exact difference phase is

\[
 \Psi_{b,d}(n)=-\lambda_b(\sqrt{n+d}-\sqrt n),
\]

and, uniformly for \(0<|d|\leq D_0\),

\[
 |\Psi''(\ell)|\asymp {M^2|d|\over J}.
 \tag{84.N9}
\]

The second-derivative estimate on a progression of length
\(O(Q^2/M)\), followed by (84.N5) and (84.N8), gives per \(b,d\)

\[
 \ll_\varepsilon X^\varepsilon H^2
 \left(J^{3/10}|d|^{1/2}
 +{J^{1/2}\over M|d|^{1/2}}\right).
 \tag{84.N10}
\]

Summing \(b\asymp B\) and both signs of \(d\) yields

\[
 \mathfrak Y_{\leq D}
 \ll_\varepsilon X^\varepsilon\left(
 C^3J^{-17/10}D^{3/2}
 +C^2TJ^{-3/2}D^{1/2}
 +{DC^2\over T\sqrt{JQ}}
 +{DB^2\over Q^2}\right).
 \tag{84.N11}
\]

At \(C=J^{3/4}\) and \(D=J^{17/30}\), the first term is exactly
\(J^{7/5}=J^2/T\); the other three are smaller.  Integer derivative
crossings and perfect powers are allowed because (84.N9), rather than a
derivative-gap assertion, supplies the cancellation.

## Scope and next survivor

The exact remaining principal correlation is the Round-83 centered sum
restricted to

\[
 |d|>\lfloor J^{17/30}\rfloor.
\]

Completion of the full \(d\)-sum self-returns to the original rank-one
progression form.  Current prime-field trace results do not cover the
composite prime-power family with the actual joint weight, and explicit
prime-power Fourier modes rule out a uniform coefficientwise square-root
substitute.  No claim is made for the large-difference survivor, a new
conductor interval, \(C>J^{3/4}\), cone edges, other radial sectors,
full `M9-M1`, `M9`, or the global exponent.
