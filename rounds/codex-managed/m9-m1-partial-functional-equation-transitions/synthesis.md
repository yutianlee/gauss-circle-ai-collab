# Round 25 synthesis: exact mixed factors, but no transition estimate

Campaign: `m9-m1-partial-functional-equation-transitions`  
Round type: partial functional-equation transitions  
Graph SHA-256 before patch: `d4d8ef8a1b506d1d33fe245c26c741fe96307f0035ed92590c39c19c9e4c1d96`

## Conductor decision

Promote the exact finite one-factor functional-equation reduction, with a
scope correction.  It is a pointwise meromorphic identity on the original
finite contours, not a side-free shifted mixed chamber and not a transition
estimate.  Keep both diagonal trace estimates, their cutoff seams, and their
outside-height limits open.

All three independent reports agree on the reflected factor assignment and
coefficient placement.  The hostile reviews also agree that the proposed
elementary estimates do not close either branch.  Round 25 used no numerical
experiment or external theorem and was therefore 100 percent
analytical/algebraic.

## Exact finite reduction

Put

\[
 A=s-\frac z2,\qquad B=s+\frac z2,
 \qquad \operatorname{Im}A=\beta,\quad \operatorname{Im}B=\alpha.
\]

For the terminal reflected kernel,

\[
 K_z(1-s)F_{-z}(s)
 =X_\zeta(A)\zeta(A)X_4(B)L(B,\chi_4),                 \tag{25.1}
\]

where

\[
 X_\zeta(A)\zeta(A)=\zeta(1-A),\qquad
 X_4(B)L(B,\chi_4)=L(1-B,\chi_4).                     \tag{25.2}
\]

Hence the exact pointwise substitution on the \(\beta\)-bounded trace is

\[
 \boxed{\zeta(1-A)X_4(B)L(B,\chi_4)},                 \tag{25.3}
\]

so the high factor carries \(\chi_4(q)q^{-B}\).  On the
\(\alpha\)-bounded trace it is

\[
 \boxed{X_\zeta(A)\zeta(A)L(1-B,\chi_4)},             \tag{25.4}
\]

so the high coefficients are the unsigned \(h^{-A}\).  The substitution
itself moves no contour and crosses no pole.  It preserves the finite trace
mask, the actual scale profiles and floors, the accepted \(R_{1,v}(1-s)\)
radial remainder, every outside side and axial/top/corner term, and the
physical normalization

\[
 -\frac4\pi X^{1/4}\operatorname{Re}
 \{e(1/8)(\mathfrak T_\chi+\mathfrak T_\zeta)\}.       \tag{25.5}
\]

This is the promoted reduction.  The unreflected completion has the
opposite verbal height assignment; (25.1)--(25.4) concern the terminal
reflected factor \(F_{-z}\), which removes that ambiguity.

## Why the proposed estimates fail

On the terminal line, after the hard top transform supplies its single
inverse high-height factor, absolute capacity is still

\[
 U^{c'-1/2+\operatorname{Re}z/2}
 \quad\hbox{on the character-high branch},
 \qquad
 U^{c'-1/2-\operatorname{Re}z/2}
 \quad\hbox{on the zeta-high branch}.                  \tag{25.6}
\]

Both grow in the required range.  This is an absolute-method obstruction,
not a lower bound for the signed coupled operator.

The standalone inverse Mellin kernels of \(X_4\) and \(X_\zeta\) are the
sine and cosine kernels.  At odd integral kernel argument,

\[
 \chi_4(q)\sin(\pi qY/2)
\]

is constant in sign on odd \(q\); at integral argument the zeta cosine
kernel is coherent.  Thus coefficientwise period-four Abel summation and
the analogous unsigned cosine estimate are not uniform.  A transition mask
convolves these pure kernels, so this resonance is a falsifier of the naive
coefficientwise lemma, not a lower bound for the fully integrated trace.

Nor is a transition-restricted contour displacement an ordinary Cauchy
shift.  A compact smooth mask is nonholomorphic in \(s\) and creates a
Cauchy--Pompeiu area term; a sharp mask creates internal strip-edge
connectors.  In the \(\beta\) branch, shifting into the arithmetic chamber
also crosses \(A=0\), the already-ledgered moving arithmetic pole whose
\(R_1\) residue was closed in Round 24.  In the \(\alpha\) branch there is
no common chamber satisfying both \(\operatorname{Re}A>1\) and
\(\operatorname{Re}(1-B)>0\).

## Residue correction

The mixed-trace attack described the split pole of \(\zeta(A)\) at
\(A=1\) as part of the existing arithmetic-residue ledger.  That wording is
not accepted.  In the full product
\(X_\zeta(A)\zeta(A)=\zeta(1-A)\), \(A=1\) is removable by the zero of
\(X_\zeta\).  The existing moving arithmetic pole is \(A=0\), equivalently
\(s=z/2\), and any shifted formula must reconcile it with Round 24 rather
than count it again.

## Smallest surviving operator

The open object is the pole-reconciled pair of masked mixed traces
(25.3)--(25.4), coupled jointly to the radial integration, multiplicative
spatial convolution, symmetric top Hilbert transform, cutoff connector or
area terms, finite outside sides, and axial residues.  The required bound is
\(O_\varepsilon(X^\varepsilon)\) on the normalized M1 scale.

The next round should isolate the connector-completed \(\beta\) branch:
freeze one smooth \(\beta\)-mask, shift \(A\) on finite boxes, reconcile the
\(A=0\) residue exactly with the closed \(R_1\) term, retain the
Cauchy--Pompeiu/strip-edge operator, and then physicalize the resulting
mask-convolved \(\chi_4\) kernel with the symmetric top Hilbert factor.
The \(\alpha\) branch remains recorded but is deferred until this connector
seam is understood.

## State effect

- promote the exact finite partial-functional-equation reduction;
- reject side-free transition shifts and coefficientwise Abel closure;
- reject a new ledgered residue at \(A=1\);
- retain both transition estimates and all outside-height limits as open;
- leave the full vector kernel, GAR/RCS/PSC, M9-M1, M9-M2, M9, and the
  Gauss-circle target open.

