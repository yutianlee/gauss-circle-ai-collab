# Round 138 statement-only problem: exact signed lower-GAR Farey scalar

This file is the complete mathematical input for the statement-only task.
It contains no strategy history, proof graph, or sibling reasoning.

## 1. Literal parameters and profiles

Let (X\ge2) be real and put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad N=\lfloor X\rfloor.
\]

Let \(\chi_4\) be the primitive real character modulo (4). Fix the
literal smooth lower-radial multiplier \(V_{\rm low}\). Choose a fixed
smooth \(\eta\) with \(\eta(u)=0\) for \(u\le1/2\) and \(\eta(u)=1\)
for \(u\ge1\), and define on the small positive arc

\[
 J_{R,y}(t)=\eta(yt)\frac{V_{\rm low}(4R^2t^2)}{t},
\tag{138.B1}
\]

extended smoothly by zero and periodically. Thus \(J_{R,y}(0)=0\),
its positive support lies in

\[
 \frac1{2y}<t<\frac{C}{R}
\tag{138.B2}
\]

for a fixed support constant (C), and
\(|J_{R,y}(t)|\ll 1/t\). Every rational sample used below is literal;
do not replace this profile by a sharp model unless the error is proved.

Define

\[
 L_\chi(T)=\sum_{g\le T}\frac{\chi_4(g)}g,
 \qquad
 \lambda_b=\frac{\chi_4(b)}bL_\chi(y/b).
\tag{138.B3}
\]

The alternating-series bound gives \(|L_\chi(T)|\le1\).

## 2. Exact scalar and target

The one-sign flat lower-radial scalar is exactly

\[
 \boxed{
 \mathcal F_N=
 \sum_{\substack{2\le b\le y\\b\ {\rm odd}}}\lambda_b
 \sum_{\substack{1\le a<b\\(a,b)=1}}
 e(aN/b)J_{R,y}(a/b).}
\tag{138.B4}
\]

It is also exactly

\[
 \mathcal F_N=
 \sum_{d\le y}\chi_4(d)\sum_{h\ge1}\frac1h
 V_{\rm low}(4R^2h^2/d^2)e(hN/d).
\tag{138.B5}
\]

Indeed, additive completion modulo (d), followed by reducing each
nonzero residue (h/d=a/b) with (d=bg), gives (138.B4); the (b=1)
term vanishes because (J_{R,y}(0)=0). The opposite sign is the complex
conjugate. The required estimate is

\[
 \boxed{|\mathcal F_N|\ll_\varepsilon RX^\varepsilon}
\tag{138.T}
\]

uniformly for every real (X). Proving (138.T) closes the lower-radial
analytic estimate through already established reductions, but it does not
by itself prove any blockwise parent, the M2 estimates, or the final
Gauss-circle theorem.

## 3. Exact scalar square

Squaring the actual scalar before taking any partial modulus gives

\[
 |\mathcal F_N|^2=
 \sum_{a,b}\sum_{a',b'}
 \lambda_b\overline{\lambda_{b'}}
 e\!\left(\frac{N(ab'-a'b)}{bb'}\right)
 J_{R,y}(a/b)\overline{J_{R,y}(a'/b')},
\tag{138.B6}
\]

with the reduced supports in (138.B4). Put

\[
 \Delta=ab'-a'b.
\tag{138.B7}
\]

Because both fractions are reduced, \(\Delta=0\) is exactly equality of
the two fractions. From (138.B2), \(|L_\chi|\le1\), and
\(|J(t)|\ll1/t\), the literal diagonal is expected at the target-square
scale

\[
 \sum_{a,b}|\lambda_bJ_{R,y}(a/b)|^2\ll yX^\varepsilon=R^2X^\varepsilon.
\tag{138.B8}
\]

This elementary estimate must be checked, not assumed. The remaining
question is whether the complete actual-coefficient \(\Delta\ne0\) scalar
in (138.B6) is also \(O_\varepsilon(yX^\varepsilon)\), or admits a strict
smaller exact signed survivor.

Unlike a dyadic positive square function in an auxiliary Fourier index,
(138.B6) is the exact square of the original scalar and retains all
cross-index phases. It is permissible to use this identity. It is not
permissible to replace its coefficient by arbitrary arrays or to take
moduli separately in (a,b,b',\Delta), residue, valuation, or lift
labels without pricing the resulting capacity.

## 4. Required decision and controls

Prove (138.T), derive a strictly smaller owner-complete signed survivor,
or identify the first rigorous scalar obstruction. Any Poisson,
stationary-phase, reciprocity, determinant-fibre, character-pairing, or
large-sieve step must retain the exact \(\lambda_b\), primitive numerator,
profile, floors (N,y), both scalar signs, and all boundary terms.

At minimum test:

- the exact reduction (138.B5) to (138.B4), including lift multiplicity;
- the (b=1) centre and the diagonal (138.B8);
- same-denominator but unequal-numerator terms;
- exact and near phase-one conditions
  \(N\Delta/(bb')\in\mathbb Z\) and
  \(\|N\Delta/(bb')\|\ll1\);
- fourth-power centres, denominators near (y), and divisors of (N);
- numerator endpoints forced by the literal support;
- character pairing and any stationary dual modes;
- whether a transform gives a genuine contraction or returns (138.B5);
- coefficient directionality, real-centre uniformity, and downstream scope.

The report must have exactly seven numbered sections: result; exact
statement and hypotheses; proof or derivation; first doubtful or unproved
step; required controls and outcomes; dependencies and exact artifacts;
recommended state effect.
