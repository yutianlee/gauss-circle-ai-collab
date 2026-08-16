# Round 82 derivation packet: transition-flattened Kloosterman energy

## 1. Accepted starting point

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J/Q=J^{3/5},
 \qquad B=C/T.
\]

Round 81 proves every fixed-smooth-interior M1 Farey block with
\(T\le C\le J^{13/18}\).  In the first residual band

\[
 J^{13/18}<C\le J^{3/4},                     \tag{82.1}
\]

the exact transition error and both axes are already target-safe.  Thus
only the globally smooth nonaxial Gaussian main remains.

Fix one endpoint orientation, one alias, one local class
\(\kappa\in\{1/4,1/2,1\}\), and one compatible nonaxial pair
\(k=\rho\sigma=O(1)\).  The finite family can be restored after the
fixed-component estimate.  Put

\[
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2.
\]

The exact main row is

\[
 S_{b,k}^{(\kappa)}(C)
 =\sum_{\substack{c\asymp C\\
                   (b,c)=1\\ c\in\mathcal C_\kappa}}
 U_{b,c,k}^{(\kappa)}V_{b,c,k}^{(\kappa)}
 e\!\left(\pm{A_{\kappa,b}\over c}\right),
 \qquad b\asymp B,                              \tag{82.2}
\]

with the exact local unit \(U\), all parity/gcd restrictions, and the
neighbor-independent critical coefficient \(V\).  The amplitude has a
continuous smooth extension in \(c\), and

\[
 \sup|V|+\int_C^{2C}|\partial_cV|\,dc
 \ll_\varepsilon X^\varepsilon.                 \tag{82.3}
\]

The frozen target is

\[
 \boxed{
 \mathfrak E_C^{(\kappa,k)}
 :=\sum_{b\asymp B}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon{J^2\over T}.}    \tag{82.4}
\]

No estimate for transition errors or axes is needed inside (82.1); they
must nevertheless remain separately owned and may not be absorbed into
the main.

## 2. Exact odd-class transform

In the odd class \(\kappa=1/4\), after the accepted reciprocity and local
normalization,

\[
 U_{b,c,k}^{(1/4)}=u_{b,k},e_{4b}(k\overline c),
 \tag{82.5}
\]

where \(u_{b,k}\) is a fixed unit and \((c,4b)=1\).  With \(q=4b\),
Poisson summation in the globally smooth complete row gives

\[
 S_{b,k}^{(1/4)}(C)
 ={u_{b,k}\over q}\sum_n S(n,k;q)I_{b,n}
   +\mathcal R_b,                                \tag{82.6}
\]

\[
 I_{b,n}=\int W_b(x)
 e\!\left(-{A_{1/4,b}\over x}-{nx\over q}\right)dx.
\]

The sign-reflected alias has the correspondingly reflected stationary
frequency.  On the retained stationary branch

\[
 n\asymp {A_{1/4,b}q\over C^2}\asymp Q^2,       \tag{82.7}
\]

and the exact leading phase is

\[
 {I_{b,n}\over q}
 =J^{1/2}n^{-3/4}
 e\!\left(-J\sqrt n-\frac{\sqrt{kn}}{2b}\right)
 V_{b,n}+\text{complete lower terms}.            \tag{82.8}
\]

All stationary lower terms, moving support, and nonstationary \(n\)-tails
must be summed at the energy level.  Round 81 removes the previous
Farey-transition gluing obstruction to (82.6); it does not prove (82.4).

The two even classes have different exact cusp/local units.  A proof may
derive their generalized Kloosterman transforms separately, but it may not
infer them from (82.6) by changing a sign.

## 3. Capacity ledger

For the odd leading coefficient

\[
 a_{b,n}=J^{1/2}n^{-3/4}
 e\!\left(-J\sqrt n-\frac{\sqrt{kn}}{2b}\right)V_{b,n},
 \qquad n\asymp Q^2,
\]

one has

\[
 \sum_{n\asymp Q^2}|a_{b,n}|^2
 \ll_\varepsilon X^\varepsilon{J\over Q}
 =X^\varepsilon T.                              \tag{82.9}
\]

The original energy diagonal is

\[
 \ll_\varepsilon X^\varepsilon BC
 =X^\varepsilon{C^2\over T}
 \le X^\varepsilon{J^2\over T}.                \tag{82.10}
\]

An ordinary coefficient-blind Kloosterman large sieve applied to (82.6)
has capacity

\[
 X^\varepsilon BQ^2T=X^\varepsilon CQ^2,        \tag{82.11}
\]

which exceeds (82.4) by the factor

\[
 {CQ^2\over J^2/T}={C\over T}=B.                \tag{82.12}
\]

Thus Round 82 needs a phase-sensitive energy gain of \(B\), or an
equivalent \(B^{1/2}\) norm gain.  Weil followed by Cauchy, an ordinary
large sieve, or taking absolute values in \(b,n\) cannot close the band.

Expanding the energy gives the exact off-diagonal core

\[
 \sum_{n_1,n_2\asymp Q^2}
 e\!\left(-J(\sqrt{n_1}-\sqrt{n_2})\right)
 \sum_{b\asymp B}
 S(n_1,k;4b)\overline{S(n_2,k;4b)}
 \mathcal W_b(n_1,n_2),                         \tag{82.13}
\]

with the extra reciprocal-square-root phase and exact actual symbol inside
\(\mathcal W_b\).  The diagonal and every fixed easy degeneracy are to be
removed once; the signed remainder is the target.

## 4. Known self-return

Expanding a Kloosterman sum in (82.6) and applying the one-dimensional
\(B\)-process to the \(n\)-chirp produces a dual length \(T\) and returns
to the original \((c,b)\) reciprocal row.  Likewise the ideal
Kuznetsov--Voronoi route localizes a dual coefficient at
\(m=X/4+O(T)\) and retains the known \(X^{1/20}\)-scale short-sum deficit.

A transformed proof counts only if it establishes a new signed inequality
for (82.13), not if it merely reconstructs (82.2), replaces the target by
a conjectural pointwise GL(2) short-sum bound, or multiplies gains obtained
after incompatible absolute-value steps.

## 5. Frozen completion rule

Round 82 succeeds if it does one of the following.

1. Proves (82.4) for every class and alias throughout (82.1), including
   all transformed errors.
2. Proves a nonempty polynomial subrange beyond \(J^{13/18}\) with an
   exact endpoint and a graph-safe all-class implication.
3. Gives a rigorous actual-symbol no-go and reduces (82.13) to a strictly
   smaller named correlation with an exact required saving.

No result may promote cone edges, other radial sectors, full `M9-M1`,
`M9`, or the Gauss-circle exponent.

## 6. Required controls

- exact row normalization and energy target;
- odd local unit and Poisson sign;
- both even cusp classes;
- global transition flattening versus pointwise remainder;
- stationary \(n\)-range and complete lower terms;
- diagonal, zero modes, gcds, and exceptional moduli;
- ordinary-large-sieve capacity (82.11)--(82.12);
- phase-sensitive off-diagonal and short-Hecke self-return;
- proper smoothness in both \(b\) and \(n\);
- perfect-square/fourth-power and phase-conjugating controls;
- source hypotheses and current-version audit;
- downstream scope.
