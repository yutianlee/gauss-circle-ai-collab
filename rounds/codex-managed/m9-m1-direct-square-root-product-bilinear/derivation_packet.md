# Round 69 packet: direct square-root-product bilinear before Cauchy

## Accepted antecedent and normalization

Let

\[
 J=X^{1/2},\qquad T=X^{1/2-\nu/2},\qquad Q=J/T=X^{\nu/2}.
\]

After the exact signed wavelet filter and Mellin separation of its fixed
smooth ratio profile, the fixed-interior transition is a rapidly
convergent superposition of forms

\[
 \mathcal B=\sum_{k\asymp Q}b_kS_k,
 \qquad
 b_k=Q^{-1}\beta(k/Q),
 \tag{69.1}
\]

where \(\beta\) is a fixed smooth compactly supported mode (with
polynomial seminorm cost absorbed by a Schwartz outer mode weight), and

\[
 S_k=\sum_{j\asymp J}\chi_4(j)\Xi(j/J)e(kX/j).
\tag{69.2}
\]

The accepted positive-frequency B-process and Round-68 actual-symbol
identity give

\[
 S_k=\mathfrak u\left({J\over k}\right)^{1/2}P_k+E_k,
 \qquad |\mathfrak u|=1,
\tag{69.3}
\]

\[
 P_k=\sum_{q\ \mathrm{odd}}\chi_4(q)C(k/q)e(\sqrt{Xkq}),
 \qquad C(y)=y^{3/4}\Xi(2\sqrt y),
\tag{69.4}
\]

on fixed positive ratio support, with the already accepted summed
fixed-interior transform errors. Absorbing \((Q/k)^{1/2}\) into
\(\beta\), the required main bound is therefore equivalent to

\[
 \boxed{
 \mathcal T_Q:=
 \sum_{k\asymp Q}\sum_{q\ \mathrm{odd}}
 \chi_4(q)\beta(k/Q)C(k/q)e(\sqrt{Xkq})
 \ll_{\varepsilon,\beta,C}Q^{3/2}X^\varepsilon.}
\tag{69.5}
\]

Indeed,

\[
 \mathcal B_{\rm main}
 =\mathfrak u\,{\sqrt J\over Q^{3/2}}\,\mathcal T_Q.
\tag{69.6}
\]

At the benchmark \(\nu=2/5\), \(Q=X^{1/5}\), the trivial capacity of
\(\mathcal T_Q\) is \(Q^2\), while the target is \(Q^{3/2}=X^{3/10}\).
Thus the direct theorem asks for only a square-root saving in one
\(Q\)-variable; it is strictly weaker than the lossless second-moment
theorem of Rounds 67--68.

## Exact structural constraints

1. The support inherited from \(\Xi\subset(0,1)\) lies in a fixed
   one-sided cone \(q>4k\), bounded away from both ratio endpoints after
   the fixed-interior cutoff.
2. The phase depends only on the product \(n=kq\). Grouping gives

   \[
    \mathcal T_Q=\sum_{n\asymp Q^2}A_Q(n)e(\sqrt{Xn}),
   \]

   \[
    A_Q(n)=\sum_{kq=n,\ q\ \mathrm{odd}}
    \chi_4(q)\beta(k/Q)C(k/q).
   \tag{69.7}
   \]

   This is a moving central/truncated divisor coefficient, not an
   arbitrary sequence and not the complete \(r_2(n)/4\) coefficient.
3. Round 68 proves that squaring and applying two stationary transforms
   is involutive. A successful direct proof must use information lost by
   Cauchy or introduce cancellation not preserved by that energy duality.
4. All claims remain restricted to a fixed smooth interior sector until
   the wavelet Mellin modes, transform errors, cone edges, and other
   radial sectors are separately recombined.

## Frozen objective

Prove (69.5), find an actual-symbol counterexample, or isolate the
smallest strictly narrower estimate. Explore direct product grouping,
two-dimensional differencing, one-sided divisor/Voronoi structure,
Mellin-functional-equation methods, and lawfully applicable bilinear or
exponent-pair theorems. Do not use the Round-68 energy estimate as an
assumption.

## Mandatory controls

- rederive the factor \(\sqrt J/Q^{3/2}\) in (69.6);
- retain \(q\) odd, \(\chi_4(q)\), and the one-sided ratio support;
- distinguish fixed smooth \(\beta,C\) from arbitrary moving symbols;
- audit exact products, square/fourth-power fibres, and rational saddles;
- compare product grouping with rowwise and two-dimensional estimates;
- track every Poisson/B-process stationary alias and any self-return;
- audit primary-source hypotheses and the exact target exponent;
- make no full-cone, radial-interval, M9-M1, M9, or exponent promotion
  without the missing implication modules.

## Required report contract

Every report has exactly seven semantic sections: result; exact statement
and hypotheses; proof/derivation; first doubtful step; controls;
dependencies and exact artifacts; recommended state effect. Numerical
work is optional and diagnostic only. At least 80 percent of the round is
analytical/algebraic.
