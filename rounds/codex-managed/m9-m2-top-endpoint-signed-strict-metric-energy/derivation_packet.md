# Round 80 derivation packet

This packet is self-contained. It states accepted inputs and the frozen
residual target; it does not promote any new theorem.

## 1. Normalization and exact accepted sum

Let

\[
 J=\sqrt X,\qquad 1\leq L\leq H\leq J^{1/2}.
\]

For primitive odd coprime \(a<b<4a\), put

\[
 q=\frac{b-a}{2},\qquad
 \delta=\sqrt b-\sqrt a,\qquad
 \Lambda=\frac{X\delta^2}{2}.
\]

The literal reciprocal range is

\[
 \frac{J\delta}{2\sqrt a}<k<\frac{J\delta}{\sqrt b}. \tag{80.1}
\]

For each actual odd lift \(g=2n+1\in\mathcal G_{a,b}\), the accepted
complete collar-extracted coefficient is

\[
 \mathfrak B^\circ_{a,b,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\left[-J\delta\sqrt u+ku
              +\frac{X\delta^2}{4k}\right]\right)\,du.       \tag{80.2}
\]

It retains the exact \(W\)-profiles, \(\Phi\), \(q_X\), floors, stars,
finite lift support, fixed physical collars, and all saddle entry/exit
transitions. The accepted aggregate identity is

\[
\begin{aligned}
 \mathcal O_L
 ={}&2\Re\sum_{a,b}\sum_k
 e\!\left(\frac q2-\frac{\Lambda}{2k}\right)
 \sum_{g=2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(g)e(-n\Lambda/k)\\
 &\quad+O\!\left(L^2\log(2+L)\right).                \tag{80.3}
\end{aligned}
\]

Because \(g=2n+1\), the two phases combine exactly:

\[
 e\!\left(\frac q2-\frac{\Lambda}{2k}\right)e(-n\Lambda/k)
 =(-1)^q e\!\left(-\frac{g\Lambda}{2k}\right).       \tag{80.4}
\]

The outer factor \(2\Re\) and the error in (80.3) occur once.

The complete coefficient obeys

\[
 |\mathfrak B^\circ(g)|+
 g|\partial_g\mathfrak B^\circ(g)|
 \ll_\varepsilon X^\varepsilon
 \frac{J\delta\sqrt{G_{a,b}}}{k^{3/2}},
 \qquad G_{a,b}\asymp\frac Lb,                       \tag{80.5}
\]

uniformly through saddle and collar transitions. This is an
actual-symbol step-two variation theorem, not a theorem for arbitrary
bounded coefficients.

## 2. Exact removals before Round 80

Round 80 contains none of the following.

1. Primitive square rays \(ab=\square\); their full signed contribution
   is \(O_\varepsilon(L^2X^\varepsilon)\).
2. Exact nonsquare centers \(\|\Lambda/k\|=0\); at fixed \(X\) there is
   at most one primitive nonsquare ray, and all its divisor modes
   contribute \(O_\varepsilon(LX^\varepsilon)\).
3. Nonsquare dyadic blocks
   \[
      a\asymp A,\quad b-a\asymp D,\quad
      k\asymp K,\quad G_{a,b}\asymp G
   \]
   satisfying
   \[
      AJD^3\ll L^3.                                   \tag{80.6}
   \]
   Their positive contribution is target-sized.
4. The already accepted endpoint/collar error in (80.3).

On every residual nonempty block,

\[
 K\asymp\frac{JD}{A},\qquad
 G\asymp\frac LA,\qquad
 AJD^3\gg L^3.                                      \tag{80.7}
\]

The sharp positive divisor-strip theorem gives only

\[
 \mathcal I_{\rm ns}(A,D,K,G;R)
 \ll_\varepsilon X^\varepsilon\frac{ADK}{R}.        \tag{80.8}
\]

The \(1/R\) density is generically present and exactly cancels the Abel
weight \(R\). No second positive incidence theorem can close (80.7).

## 3. Strict-metric one-count sum

Choose a fixed smooth dyadic partition of the punctured circle distance.
For \(1\leq R\leq N_{a,b}\ll G\), its \(R\)-piece is supported where

\[
 0<c_1/R\leq \|\Lambda/k\|\leq c_2/R<1/2,           \tag{80.9}
\]

with a fixed tie convention in the bounded \(R\) pieces. Let
\(\ell=\ell_{a,b,k}\) be the nearest integer and put

\[
 \theta=\frac{\Lambda}{k},\qquad
 \eta=\theta-\ell,\qquad
 p=\ell k.                                         \tag{80.10}
\]

Then

\[
 |\Lambda-p|\asymp\frac KR,\qquad k\mid p,          \tag{80.11}
\]

and, because \(g\) is odd,

\[
 (-1)^q e(-g\theta/2)
 =(-1)^{q+\ell}e(-g\eta/2)
 =(-1)^{q+p/k}e(-g\eta/2).                         \tag{80.12}
\]

The literal block sum is therefore

\[
\boxed{
\begin{aligned}
 \mathcal S_{A,D,K,G,R}^{\rm hard}
 =\sum_{\substack{a,b,k\ {\rm residual}\\
                   AJD^3\gg L^3\\
                   |\eta|\asymp R^{-1}}}
 (-1)^{q+\ell}
 \sum_{g\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(g)e(-g\eta/2).
\end{aligned}}                                      \tag{80.13}
\]

The frozen target is

\[
 \sum_{A,D,K,G,R}
 |\mathcal S_{A,D,K,G,R}^{\rm hard}|
 \ll_\varepsilon L^2X^\varepsilon,                 \tag{80.14}
\]

or an equivalent one-count signed estimate before dyadic triangle
inequality. Powers of \(\log X\) are absorbed in \(X^\varepsilon\).
No absolute value may be inserted inside the primitive-ray or
reciprocal-mode sum.

The accepted pointwise Abel estimate is only

\[
 \left|\sum_g\mathfrak B^\circ(g)e(-g\eta/2)\right|
 \ll_\varepsilon X^\varepsilon
 \frac{J\delta\sqrt G}{K^{3/2}}\,R,                 \tag{80.15}
\]

and leads back to the nonclosing positive capacity
\(A\sqrt G\sqrt J D^{3/2}\).

## 4. Exact fiber and Fourier identities available for use

The product-fiber description (80.11) is exact. On a fiber \(p\), the
outer sign is

\[
 (-1)^{q+p/k}.                                      \tag{80.16}
\]

Thus any divisor-fiber proof must retain the parity of the quotient
\(p/k\), not merely count \(k\mid p\).

Alternatively, let \(W_R\) be a smooth period-one window adapted to
(80.9), with mean \(\mu_R\asymp1/R\). Its exact Fourier series is

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad
 |\widehat W_R(r)|
 \ll_A R^{-1}(1+|r|/R)^{-A}.                        \tag{80.17}
\]

Multiplication by a nonzero Fourier mode shifts the odd lift frequency:

\[
 e(-g\theta/2)e(r\theta)
 =e(-(g-2r)\theta/2).                               \tag{80.18}
\]

After reindexing, the coefficient is
\(\mathfrak B^\circ(g'+2r)\) and the finite lift support is translated.
Any cancellation based on (80.18) must include the resulting coefficient
differences and both support endpoints. Step-two variation alone does
not automatically cancel the density term \(\mu_R\).

The density and centered discrepancy in (80.17) must be bounded
together. A theorem only for excess incidence does not imply (80.14).

## 5. Required hostile controls

Every proposed proof must pass all of the following.

1. Exact nonsquare centers have already been removed; they cannot be
   used as the hard model.
2. Near-square rays \(b=a+2\) remain unless (80.6) closes their block.
3. The Pell family \(a=s^2,\ b=3t^2=a+2\) is a common-squarefree-kernel
   nonsquare control.
4. Metric recurrences persist along squares and fourth powers even
   though rational \(X\) has no exact nonsquare center.
5. Empty and singleton reciprocal intervals keep their full endpoint
   ownership.
6. The complete coefficient may vanish or change phase; its variation
   scale is not a pointwise lower bound.
7. Phase-conjugated arbitrary coefficients are forbidden and show why a
   coefficient-uniform theorem is false.
8. Reciprocal Poisson or divisor re-enumeration that restores the same
   product fibers is a self-return, not a second saving.
9. Floors, stars, both physical collars, and every saddle transition
   remain owned exactly once.

## 6. Lawful outcomes

A report may:

- prove (80.14);
- prove a new explicit hard subrange and state the exact remaining
  range;
- derive a smaller complete-coefficient \(TT^*\), fiber, or
  density-discrepancy correlation and prove a rigorous no-go for the
  proposed closure route;
- identify an actual-symbol counterexample to (80.14), in which case the
  earlier transposed-energy architecture must be revisited.

It may not promote \(M9\!-\!M2\), \(M9\), endpoint uniformity, or the
global exponent unless the entire residual signed energy and every
declared seam close.
