# Round 79 derivation packet: residual nonsquare reciprocal resonances

Campaign: `m9-m2-top-endpoint-generic-reciprocal-resonance`  
Round: 79  
Starting graph SHA-256:
`5e5c01114e46fcb3079a6e1427f8155421f7ec9a45c9599cbd8aa8c94cf0bac2`

## 1. Accepted antecedent and ownership

Let

\[
 J=\sqrt X,\qquad 1\leq L\leq H\leq J^{1/2}.
\]

The accepted collar-extracted positive-offset identity has primitive odd
coprime rays

\[
 \mathscr P_L=\{(a,b):a<b<4a,\ a,b\ {m odd},\ (a,b)=1,
                   \ \mathcal G_{a,b}\ne\varnothing\}.
\]

For \((a,b)\in\mathscr P_L\), put

\[
 \delta=\sqrt b-\sqrt a,\qquad
 \Lambda={X\delta^2\over2},\qquad
 \alpha={b-a\over4}-{X\delta^2\over4k},             \tag{79.1}
\]

and

\[
 \mathcal K_{a,b}=
 \left\{k\in\mathbb Z_{\geq1}:
 {J\delta\over2\sqrt a}<k<{J\delta\over\sqrt b}\right\}.
                                                               \tag{79.2}
\]

If \(N_{a,b}=\#\mathcal G_{a,b}\) and \(G_{a,b}\asymp L/b\), then
\(N_{a,b}\ll G_{a,b}\).  The complete actual coefficient obeys the
accepted step-two variation estimate

\[
 \mathcal V_{a,b,k}\ll_\varepsilon
 X^\varepsilon{J\delta\sqrt{G_{a,b}}\over k^{3/2}},              \tag{79.3}
\]

and discrete Abel gives

\[
 \left|\sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(2n+1)e(-n\Lambda/k)\right|
 \leq \mathcal V_{a,b,k}
 \min\!\left(N_{a,b},{1\over2\|\Lambda/k\|}\right).          \tag{79.4}
\]

The complete coefficient contains the literal profiles, floors, stars,
finite lift interval, two fixed physical collars, and both saddle
transitions.  It may not be replaced by its first stationary value or by
an arbitrary bounded coefficient.

The primitive algebraic family \(ab=\square\) is already removed.  Since
\((a,b)=1\), it is exactly \(a=s^2,b=t^2\); its complete signed
contribution is graph-accepted at \(O_\varepsilon(L^2X^\varepsilon)\).
Round 79 concerns only

\[
 \mathscr P_L^{\rm ns}=\{(a,b)\in\mathscr P_L:ab\ne\square\}.    \tag{79.5}
\]

## 2. Exact metric-window formulation

For any integer \(N\geq1\) and \(\theta\in\mathbb R/\mathbb Z\),

\[
 \min\!\left(N,{1\over2\|\theta\|}\right)
 \ll 1+\sum_{\substack{R\leq N\\R\ {m dyadic}}}
 R\,\mathbf 1_{\{\|\theta\|\leq c/R\}},                      \tag{79.6}
\]

for one absolute \(c>0\).  Thus every large Abel factor is represented
by a dyadic metric window

\[
 \left\|{\Lambda\over k}\right\|\leq {c\over R},
 \qquad 1\leq R\leq N_{a,b}.                                  \tag{79.7}
\]

Equation (79.7) is exactly equivalent to the existence of
\(\ell\in\mathbb Z_{\geq0}\) such that

\[
 |\Lambda-\ell k|\leq {ck\over R}.                            \tag{79.8}
\]

The orientation and factor \(1/2\) in (79.1) are fixed.  Counting only
solutions of \(\Lambda=\ell k\) is insufficient: \(X\) is real and the
full window (79.8) is part of the theorem.

For blockwise analysis one may further impose

\[
 a\asymp A,\qquad b-a\asymp D,\qquad k\asymp K,
 \qquad G_{a,b}\asymp G,\qquad R\asymp R_0,                    \tag{79.9}
\]

where (79.2) forces \(K\asymp JD/A\) up to fixed-ratio factors when
\(D\ll A\), with the literal formula (79.2) governing all other blocks.

## 3. Frozen incidence and inverse objects

Define the residual block incidence

\[
\begin{aligned}
 \mathcal I_{\rm ns}(A,D,K,G;R)
 :={}&\#\biggl\{(a,b,k,\ell):
 (a,b)\in\mathscr P_L^{\rm ns},\ (79.9)\ {m holds},\\
 &\hspace{35mm}|\Lambda-\ell k|\leq {ck\over R}\biggr\}.
                                                               \tag{79.10}
\end{aligned}
\]

The corresponding coefficient-scale positive diagnostic is

\[
 \mathcal A_{\rm ns}(R)=
 \sum_{(a,b)\in\mathscr P_L^{\rm ns}}
 \sum_{k\in\mathcal K_{a,b}}
 \mathcal V_{a,b,k}\,R\,
 \mathbf 1_{\{\|\Lambda/k\|\leq c/R\}}.                     \tag{79.11}
\]

Neither (79.10) nor (79.11) is the signed top energy.  In particular,
the false target-sized absolute Abel majorant on the removed square
family shows that incidence bounds must be used before, not instead of,
the actual signed reciprocal-mode estimate.

A successful inverse theorem may take either of the following forms.

1. A high-multiplicity block in (79.10) forces a precisely parameterized
   algebraic family \(\mathfrak S\), with the primitive-square family
   excluded and with the actual coefficient-weighted mass of
   \(\mathfrak S\) separately controlled.
2. Outside explicit structured families, a quantitative spacing or
   energy inequality is proved with all powers of \(A,D,K,G,R\) stated,
   and its insertion into the later signed primitive-ray argument is
   demonstrated without an absolute sum over all rays or modes.

A rigorous construction showing that no such classification follows
from (79.7) alone is also a successful no-go result.

## 4. Algebraic coordinates and mandatory controls

Write

\[
 d=b-a,\qquad
 \delta={d\over\sqrt a+\sqrt b},\qquad
 \Lambda={Xd^2\over2(\sqrt a+\sqrt b)^2}.                       \tag{79.12}
\]

Since \(a,b\) are odd, \(d\) is even.  Any rationalization, determinant,
root-spacing, or Diophantine approximation must retain the coprimality,
the fixed-ratio cone \(a<b<4a\), the open interval (79.2), and the
metric error \(k/R\).

Every proposed theorem must test:

- near-square nonsquare pairs with \(d\ll a\);
- products with large square factors but \(ab\ne\square\);
- perfect-square and fourth-power choices of \(X\);
- one-point and empty \(k\)-intervals;
- \(R=1\), \(R\asymp G\), and intermediate metric windows;
- exact integer resonances and nonintegral metric resonances;
- saddle entry/exit, endpoint stars, and fixed collars;
- arbitrary or phase-conjugated coefficient analogues;
- the rank-one reciprocal-transform self-return.

## 5. Required quantitative ledger

Any bound for (79.10) must be carried through the accepted local scale

\[
 \mathcal V_{a,b,k}
 \asymp_{X^\varepsilon}{J\delta\sqrt G\over k^{3/2}}            \tag{79.13}
\]

on the block where it is used.  The report must state:

1. the trivial incidence and coefficient capacities;
2. the exact saving supplied by the theorem;
3. whether that saving is uniform in all allowed \(L,A,D,K,G,R\);
4. whether it controls only a positive exceptional set or genuinely
   supplies an input to a signed \(TT^*\), large-sieve, or primitive-ray
   estimate;
5. the smallest remaining signed correlation after the geometry is used.

No graph implication follows from a qualitative phrase such as
“generic roots are separated.”

## 6. Forbidden shortcuts

Do not:

- reinclude or reprove the accepted primitive-square contribution;
- identify \(ab\ne\square\) with a quantitative root-separation bound;
- replace (79.8) by exact divisibility;
- assume \(X\) is integral, square, or generic;
- discard metric resonances, one-point intervals, stars, or moving
  profile transitions;
- take absolute values over the complete primitive-ray union;
- use coefficient-blind decoupling or incidence as the final signed
  estimate;
- count a reciprocal Poisson/B-process self-return as a new saving;
- import a source without matching variables, lengths, smoothness,
  characters, endpoints, and uniformity.

## 7. Exit rule

Round 79 succeeds if it proves a quantitative residual nonsquare inverse
or incidence theorem with a valid coefficient ledger, isolates and
controls a new structured family, or proves a sharp no-go that changes
the strategy.  A merely heuristic spacing claim or a theorem for exact
divisors alone does not pass.

This round does not promote the complete signed cone, the full transposed
energy, \(M9\!-!M2\), \(M9\), endpoint uniformity, or the global
exponent unless the exact signed energy is unexpectedly established and
independently reviewed.
