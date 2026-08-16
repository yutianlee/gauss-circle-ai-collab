# Round 79 conductor preliminary algebra

Status: conductor calculation and route diagnostic, not accepted graph
mathematics.

## 1. Half-angle coordinates

For primitive odd \(a<b<4a\), put

\[
 m={a+b\over2},\qquad q={b-a\over2}.
\]

Then \((m,q)=1\), \(m,q\) have opposite parity, and \(0<q<3m/5\).
With

\[
 u={q\over m+\sqrt{m^2-q^2}}
   ={\sqrt b-\sqrt a\over\sqrt b+\sqrt a},          \tag{C79.1}
\]

one has the exact identities

\[
 {\delta^2\over2}=m-\sqrt{m^2-q^2}=qu,qquad
 \Lambda=Xqu,                                       \tag{C79.2}
\]

and

\[
 {Ju\over1-u}<k<{2Ju\over1+u}.                     \tag{C79.3}
\]

Moreover \(u\) satisfies

\[
 qu^2-2mu+q=0.                                      \tag{C79.4}
\]

Thus the removed primitive-square family is exactly the rational branch
\(m^2-q^2=ab=\square\); every residual \(u\) is a genuine quadratic
irrational.  This observation is exact but does not itself give a useful
metric lower bound at the window \(R^{-1}\).

## 2. Exact injectivity and weak norm spacing

Write uniquely

\[
 ab=D r^2,
\]

with \(D>1\) squarefree.  Then

\[
 {\Lambda\over X}=m-r\sqrt D.                       \tag{C79.5}
\]

If two primitive nonsquare triples satisfy

\[
 {m_1-r_1\sqrt{D_1}\over k_1}
 ={m_2-r_2\sqrt{D_2}\over k_2},                    \tag{C79.6}
\]

linear independence of distinct squarefree radicals first forces
\(D_1=D_2\).  Rational and irrational parts then give

\[
 k_2m_1=k_1m_2,\qquad k_2r_1=k_1r_2.
\]

Since \(q_i^2=m_i^2-D r_i^2\), the same rational factor carries
\(q_1\) to \(q_2\).  The primitive identities \((m_i,q_i)=1\) force
that factor to be one.  Hence the two triples are identical.  The
residual normalized frequencies are exactly injective.

This exact result is much weaker than the required metric statement.
For different squarefree fields, taking the biquadratic norm gives only
a lower bound of the shape

\[
 \left|{m_1-r_1\sqrt{D_1}\over k_1}
       -{m_2-r_2\sqrt{D_2}\over k_2}\right|
 \gg (KB)^{-3}K^{-2},                               \tag{C79.7}
\]

on \(m_i\asymp B\), \(k_i\asymp K\).  This is far below the active
metric scale after multiplication by \(X\), in the difficult ranges.
Exact injectivity therefore does not imply sparse metric incidence.

## 3. Random-density metric baseline

Fix constants \(1<\rho_0<\rho_1<2\).  Let \(Y\) be large and choose
primitive odd pairs

\[
 a\asymp B,\qquad \rho_0a<b<\rho_1a.                \tag{C79.8}
\]

For each pair define the stable reciprocal interval

\[
 \mathcal K^*_{a,b}(Y)=
 \left({\sqrt{2Y}\,\delta\over2\sqrt a},
       {\sqrt Y\,\delta\over\sqrt b}\right)\cap\mathbb Z.
                                                               \tag{C79.9}
\]

Because \(\rho_1<2\), this interval has \(\asymp\sqrt Y\) points and
is contained in the exact \(k\)-interval for every \(X\in[Y,2Y]\).
For

\[
 c_{a,b,k}={\delta^2\over2k}\asymp {B\over\sqrt Y},             \tag{C79.10}
\]

and \(0<\eta\leq1/4\), elementary period counting gives

\[
 \int_Y^{2Y}{\bf1}_{\{\|Xc_{a,b,k}\|\leq\eta\}}\,dX
 =2\eta Y+O(c_{a,b,k}^{-1}).                         \tag{C79.11}
\]

There are \(\asymp B^2\) primitive odd pairs in (C79.5) and
\(\asymp B^2\sqrt Y\) stable triples.  Primitive square rays contribute
only \(O(B^{1+\varepsilon})\) pairs and are negligible.  Summing (C79.8)
over the residual nonsquare triples gives main term

\[
 \asymp \eta B^2Y^{3/2}                              \tag{C79.12}
\]

and total endpoint error

\[
 \ll BY.                                             \tag{C79.13}
\]

Consequently, for every \(R\leq Y^{1/4}\) with \(\eta=1/R\), some
\(X\in[Y,2Y]\) satisfies

\[
 \#\left\{(a,b,k):ab\ne\square,
       \left\|{X(\sqrt b-\sqrt a)^2\over2k}\right\|
       \leq{1\over R}\right\}
 \gg {B^2\sqrt Y\over R}.                          \tag{C79.14}
\]

This is the full random-density baseline, not a sparse algebraic
exception.

## 4. Coefficient-scale consequence

If the dyadic lift profile has a fixed positive interior on which
\(N_{a,b}\asymp G\asymp L/B\), choose \(R\leq cG\).  On the fixed-ratio
block,

\[
 \mathcal V_{a,b,k}asymp_{X^\varepsilon}
 {J\sqrt B\sqrt G\over J^{3/2}}
 =\sqrt{L/J}.                                        \tag{C79.15}
\]

Multiplying the random incidence (C79.11) by the dyadic Abel weight
\(R\) therefore leaves positive diagnostic capacity

\[
 \asymp B^2\sqrt{LJ},                                \tag{C79.16}
\]

independent of \(R\).  An incidence theorem can at best isolate excess
over (C79.11); it cannot make the ordinary metric population disappear.
The next energy theorem must retain cancellation across \(k\) or
primitive rays.

## 5. Scope and first seam

The averaging proof is unconditional for the geometric set.  Its use at
the literal Abel scale \(R\leq N_{a,b}\) additionally needs a stated
positive-interior lower bound \(N_{a,b}\asymp L/b\) for the selected
actual profile block.  The accepted packet records only
\(N_{a,b}\ll G\).  Without that lower-support statement, (C79.11) is a
route no-go for coefficient-blind incidence, not yet an actual-symbol
lower bound.

The preliminary conclusion is that Round 79 should formulate any
inverse theorem for *excess incidence above the random baseline*, not
for every metric resonance.  Even such an excess theorem remains only
an input to the signed primitive-ray energy.
