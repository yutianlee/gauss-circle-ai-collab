# Round 93 conductor review: frozen moment

## Claim reviewed

For fixed \(H\), a fixed denominator set
\(\mathscr D_D\subset[c_0D,c_1D]\), and \(|w(d)|\leq1\),

\[
 S(t)=\sum_{0<|h|\leq H}\beta_{h,H}
      \sum_{d\in\mathscr D_D}w(d)e\!\left(\frac{ht}{4d}\right)
\]

satisfies

\[
 \int_I|S(t)|^2\,dt\ll_{c_0,c_1}(|I|+D^2)D.
 \tag{R93.F1}
\]

## Local reproduction

Write \(h=ka,d=kb\), where \(k\geq1\), \(b>0\), and
\((|a|,b)=1\). Exact equality classes, including signed \(a\), give

\[
 A_{a,b}=\sum_{\substack{k:\,kb\in\mathscr D_D\\|ka|\leq H}}
 \beta_{ka,H}w(kb).
\]

Because \(kb\) lies in a fixed-ratio interval and
\(|\beta_{ka,H}|\leq(\pi k|a|)^{-1}\),

\[
 |A_{a,b}|\ll |a|^{-1},
 \qquad
 \sum_{a,b}|A_{a,b}|^2\ll D.
\]

Distinct reduced frequencies \(a/(4b)\) are separated by
\(\gg D^{-2}\). The triangular majorant proved in the blind report gives

\[
 \int_I\left|\sum_\lambda c_\lambda e(\lambda t)\right|^2dt
 \ll (|I|+\delta^{-1})\sum_\lambda|c_\lambda|^2
\]

for a \(\delta\)-separated real frequency set. This proves (R93.F1)
without importing an external theorem.

## Controls

- Equality is grouped before spacing; repeated rational representations
  never enter the separation parameter.
- Positive and negative frequencies remain distinct.
- The exact \(\chi_4(h)\) factor remains inside \(A_{a,b}\).
- Partial shells and support endpoints only shorten the fixed-ratio
  harmonic sum.
- The actual Vaaler coefficient has
  \(|\beta_{1,H}|\geq1/(2\pi)\). On a full shell the \(h=\pm1\)
  no-multiplicity zone gives coefficient energy \(\gg D\), conditional
  only on nontrivial denominator \(\ell^2\)-mass.

## Decision

The frozen moment, its single-block Chebyshev bound, and the all-dyadic
union are proved internally. At \(D\asymp\sqrt Y\) and threshold
\(Y^{1/4}\), Chebyshev gives ambient measure \(O(Y)\), so there is no
pointwise or zero-margin exceptional-set consequence.
