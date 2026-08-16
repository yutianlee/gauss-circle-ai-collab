# Round 78 derivation packet: primitive square-ray resonance mass

Campaign: m9-m2-top-endpoint-square-resonance-mass  
Round: 78  
Starting graph SHA-256:
5afbe1bb7b5c5d943be9438ba02bd9ede1ab6735344174b33b4a99c7de7f9123

## 1. Accepted antecedent

Let

\[
 J=\sqrt X,\qquad 1\leq L\leq H\leq J^{1/2}.
\]

Round 77 proved the complete collar-extracted positive-offset identity

\[
\begin{aligned}
 \mathcal O_L={}&2\Re
 \sum_{\substack{a<b<4a\\a,b\ \mathrm{odd}\\(a,b)=1}}
 \sum_{k\in\mathcal K_{a,b}} e(\alpha)
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(2n+1)e(-n\Lambda/k)\\
 &\quad+O_\varepsilon(L^2X^\varepsilon),             \tag{78.1}
\end{aligned}
\]

where

\[
\begin{gathered}
 \delta=\sqrt b-\sqrt a,\qquad
 \Lambda={X\delta^2\over2},\qquad
 \alpha={b-a\over4}-{X\delta^2\over4k},\\
 \mathcal K_{a,b}=
 \left\{k\geq1:{J\delta\over2\sqrt a}
 <k<{J\delta\over\sqrt b}\right\}.                  \tag{78.2}
\end{gathered}
\]

The complete integral retains the exact fixed profiles, floors, stars,
finite support, and saddle transitions.  If
\(N_{a,b}=\#\mathcal G_{a,b}\) and \(G\asymp L/b\), its accepted
step-two variation is

\[
 \mathcal V_{a,b,k}
 \ll_\varepsilon X^\varepsilon
 {J\delta\sqrt G\over k^{3/2}}.                      \tag{78.3}
\]

Hence discrete Abel gives

\[
\left|\sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ(2n+1)e(-n\Lambda/k)\right|
\leq \mathcal V_{a,b,k}
\min\!\left(N_{a,b},{1\over2\|\Lambda/k\|}\right).   \tag{78.4}
\]

Equation (78.4) is a legal raywise bound.  Taking its absolute sum over
all primitive rays and reciprocal modes is not an accepted theorem.

## 2. Exact square/common-squarefree parameterization

The algebraically rational primitive rays are those with \(ab\) a
square.  Since \((a,b)=1\),

\[
 ab=\square\quad\Longleftrightarrow\quad
 a=s^2,\quad b=t^2                                      \tag{78.5}
\]

for coprime odd \(s<t<2s\).  Write

\[
 t=s+2u,\qquad u\geq1,\qquad (s,u)=1.                 \tag{78.6}
\]

Then

\[
\begin{gathered}
 \delta=2u,\qquad
 {b-a\over4}=u(s+u)\in\mathbb Z,\qquad
 \Lambda=2Xu^2,\\
 \alpha=u(s+u)-{Xu^2\over k},\qquad
 e(\alpha)=e(-Xu^2/k),                               \tag{78.7}\\
 {Ju\over s}<k<{2Ju\over t},\qquad
 G\asymp {L\over t^2}.                               \tag{78.8}
\end{gathered}
\]

The offset sign is inert on every such ray because
\((b-a)/2=2u(s+u)\) is even.  In the original variables, pairs with a
common squarefree kernel are exactly the lifts of these primitive square
rays: the squarefree part is carried by the odd lift \(g\).

## 3. Frozen square-family objects

Define the exact signed square contribution

\[
\begin{aligned}
 \mathcal S_L^\square(X)
 :={}&2\Re
 \sum_{\substack{s<t<2s\\s,t\ \mathrm{odd}\\(s,t)=1}}
 \sum_{\substack{k\geq1\\Ju/s<k<2Ju/t}}
 e(-Xu^2/k)\\
 &\times
 \sum_{2n+1\in\mathcal G_{s^2,t^2}}
 \mathfrak B^\circ_{s^2,t^2,k}(2n+1)
 e(-2nXu^2/k),\qquad u={t-s\over2}.                 \tag{78.9}
\end{aligned}
\]

This is a literal finite sub-sum of (78.1), not a leading-term model.
The first candidate target is

\[
 \boxed{\quad
 |\mathcal S_L^\square(X)|
 \ll_\varepsilon L^2X^\varepsilon.
 \quad}                                               \tag{78.10}
\]

Separately define the stronger absolute Abel majorant

\[
\begin{aligned}
 \mathcal M_L^\square(X)
 :={}&
 \sum_{\substack{s<t<2s\\s,t\ \mathrm{odd}\\(s,t)=1}}
 \sum_{\substack{k\geq1\\Ju/s<k<2Ju/t}}
 {2Ju\sqrt{G_{s,t}}\over k^{3/2}}\\
 &\times
 \min\!\left(
 N_{s^2,t^2},
 {1\over2\|2Xu^2/k\|}
 \right).                                             \tag{78.11}
\end{aligned}
\]

At exact resonance the second argument in the minimum is \(+\infty\).
The reports must determine whether

\[
 \mathcal M_L^\square(X)
 \ll_\varepsilon L^2X^\varepsilon                    \tag{78.12}
\]

is true or false.  Failure of (78.12) does not by itself refute (78.10)
or the full nonnegative energy; it proves that raywise absolute Abel is
too lossy on the structured family.

## 4. Required analytic distinctions

The reciprocal resonance is

\[
 \left\|{2Xu^2\over k}\right\|.                       \tag{78.13}
\]

For arithmetic \(X\), exact or divisor-structured \(k\) may occur.  For
general real \(X\), near-resonant \(k\) form a metric set that must be
counted at the actual window \(N_{s^2,t^2}^{-1}\).  A proof must retain
the outer phase \(e(-Xu^2/k)\), the complete lift coefficient, and any
cancellation across \(k,s,u\) before concluding (78.10).

The fourth-power family

\[
 X=T^4,\qquad 13\mid T,\qquad (s,t)=(9,11),\qquad
 k={2T^2\over13}                                      \tag{78.14}
\]

is an exact coherent control with both actual \(W\)-weights equal to
one.  It tests that no in-ray character cancellation is invented.

The phrase “common squarefree kernel” introduces no second primitive
family beyond (78.5).  Near-square nonsquare rays belong to the later
generic/inverse-theorem stage unless a report proves a precise
structured enlargement and estimates its actual coefficient.

## 5. Required controls

Every report must test:

1. the external normalization and one-count \(2\Re\);
2. (78.5)--(78.8), including parity and the exact open \(k\)-interval;
3. the complete Round-77 integral, actual profiles, floors, stars, and
   finite lift interval;
4. exact versus metric reciprocal resonances;
5. the distinction between (78.10) and (78.12);
6. the fourth-power coherent family (78.14);
7. small \(s,u\), one-point lift intervals, and \(k\)-interval endpoints;
8. possible cancellation over \(k\) and across square rays;
9. the unsigned/adversarial coefficient analogue;
10. the rank-one reciprocal self-return;
11. separation from nonsquare generic rays, the full energy, M2, M9,
    endpoint uniformity, and the exponent.

## 6. Forbidden shortcuts and false analogues

Do not:

- replace \(\mathfrak B^\circ\) by its first stationary value;
- infer (78.10) from (78.12), or infer failure of (78.10) merely from
  failure of (78.12);
- treat a single coherent ray as a lower bound for the full energy;
- assume \(X\) is an integer, square, or fourth power in a uniform claim;
- count only exact divisors and omit metric near-resonances;
- take absolute values before testing the actual \(k\)- and cross-ray
  phases;
- count a second reciprocal transform as a new gain;
- use a theorem valid for arbitrary bounded coefficients as if it
  exploited the actual sign/profile structure.

## 7. Exit rule

A successful round proves (78.10), proves a corrected target-sized
structured theorem, or gives a rigorous actual-symbol obstruction to
separate square-family closure.  A sharp proof or counterexample for
(78.12) is independently promotable as a route theorem.  Promotion
requires a clean statement-only rederivation, analytic proof, hostile
audit, controls, conductor adjudication, and a valid State Patch.

The round cannot promote the generic resonance theorem, full transposed
energy, signed top cone, \(M9\!-\!M2\), \(M9\), endpoint uniformity, or
the global exponent.
