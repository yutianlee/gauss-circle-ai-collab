# Round 65 derivation packet: local character-hyperbola discrepancy

## Accepted input

Let \(e(t)=e^{2\pi i t}\), \(N=X^\nu\),
\(T=\sqrt{X/N}\), and fix
\(\Xi\in C_c^\infty((0,1))\). Round 64 proves, for

\[
 A_{X,\Xi}(n)=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X),
 \qquad
 K(\xi)=\widehat g(\xi),
 \qquad
 g(t)=\mathbf 1_{t>0}\frac{V(t^2)}t,
\tag{65.1}
\]

the fixed-interior reciprocal identity

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\geq1}A_{X,\Xi}(n)
 K\!\left(\frac{n-X}{2T}\right)+O_B(X^{-B}).
\tag{65.2}
\]

Once \(2T\) exceeds the support radius of \(g\), the sampled kernel
annihilates every polynomial exactly:

\[
 \sum_{n\in\mathbb Z}(n-X)^r
 K\!\left(\frac{n-X}{2T}\right)=0
 \qquad(r=0,1,2,\ldots).
\tag{65.3}
\]

The required normalized bound is

\[
 \boxed{\mathcal R_{X,N}[V,\Xi]
 \ll_{\varepsilon,V,\Xi}X^{1/4+\varepsilon}.}
\tag{65.4}
\]

The primary benchmark is \(\nu=2/5\), where \(T=X^{3/10}\) and
the missing gain over absolute summation is \(X^{1/20}=H/L\). A proof
on any fixed nonempty interval ending at or below \(2/5\) is useful, but
no radial or exponent promotion is allowed without the omitted sharp
saddle and full-cone modules.

## Exact Abel reduction

Put

\[
 c_X=\sum_{j\geq1}\frac{\chi_4(j)}j\Xi(j/\sqrt X),
 \qquad
 B_X(y)=\sum_{n\leq y}A_{X,\Xi}(n)
 =\sum_{j\geq1}\chi_4(j)\Xi(j/\sqrt X)
 \left\lfloor\frac yj\right\rfloor.
\tag{65.5}
\]

Elementary period-four Abel summation gives \(c_X\ll_\Xi X^{-1/2}\)
(smooth Poisson may sharpen this, but no sharpening is needed). Let
\(n_0=\lfloor X\rfloor\), and for integral \(n\geq1\) define

\[
 \mathfrak D_X(n;n_0)
 =B_X(n)-B_X(n_0)-c_X(n-n_0)
\tag{65.6}
\]

so that exactly

\[
 \mathfrak D_X(n;n_0)
 =\sum_{j\geq1}\chi_4(j)\Xi(j/\sqrt X)
 \left(
 \left\lfloor\frac nj\right\rfloor
 -\left\lfloor\frac {n_0}j\right\rfloor
 -\frac{n-n_0}{j}
 \right).
\tag{65.7}
\]

Extend \(A_{X,\Xi}(n)\) by zero to \(n\leq0\), and extend
\(\mathfrak D_X(n;n_0)\) to all integral \(n\) by requiring
\(\mathfrak D_X(n_0;n_0)=0\) and

\[
 \mathfrak D_X(n;n_0)-\mathfrak D_X(n-1;n_0)
 =A_{X,\Xi}(n)-c_X.
\tag{65.7a}
\]

Thus the extension is affine on \(n\leq0\); it is not obtained by
inserting negative \(n\) into the floor formula (65.7). With
\(W_n=K((n-X)/(2T))\), discrete summation by parts and
\(\sum_{n\in\mathbb Z}W_n=0\) give

\[
 \boxed{
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\geq1}\mathfrak D_X(n;n_0)(W_n-W_{n+1})
 +O_B(X^{-B}).}
\tag{65.8}
\]

The displayed error is the Schwartz-negligible nonpositive \(n\) tail;
the affine main term vanishes exactly by the sampled zero mode. Also

\[
 \sum_n|W_n-W_{n+1}|\ll_{V}1.
\tag{65.9}
\]

Consequently the strong local discrepancy estimate

\[
 \boxed{
 \sup_{|v|\leq T X^\eta}
 |\mathfrak D_X(n_0+v;n_0)|
 \ll_{\varepsilon,\eta,\Xi}X^{1/4+\varepsilon}}
\tag{LCD}
\]

for some fixed \(0<\eta<\nu/2\), together with the Schwartz tail, is
sufficient for (65.4). The exact weighted estimate obtained by replacing
the supremum in (LCD) with the right side of (65.8) is weaker and is also
admissible.

## Thin hyperbola form

For \(0<v<\min\operatorname{supp}(\Xi)\sqrt X\), every supported
\(j\) contributes at most one multiple, and

\[
 \mathfrak D_X(n_0+v;n_0)
 =\sum_j\chi_4(j)\Xi(j/\sqrt X)
 \left(
 \mathbf 1_{\{\exists m:\ n_0<jm\leq n_0+v\}}
 -\frac vj
 \right).
\tag{65.10}
\]

Equivalently, without any size restriction on \(v\),

\[
 \mathfrak D_X(n_0+v;n_0)
 =\sum_j\chi_4(j)\Xi(j/\sqrt X)
 \left(
 \left\{\frac{n_0}{j}\right\}
 -\left\{\frac{n_0+v}{j}\right\}
 \right),
\tag{65.11}
\]

where \(v\) is integral in this discrete formula. If a real displacement
is desired, replace \(n_0+v\) everywhere by its chosen integral endpoint;
the resulting discrepancy changes only by the explicitly retained linear
term. In particular, (65.10) is to be read for integral \(v>0\).

Thus the first new theorem is a signed discrepancy for a width-\(T\)
hyperbolic boundary with the divisor leg constrained to
\(j\asymp\sqrt X\) and twisted by \(\chi_4(j)\). Its unweighted
capacity is \(T X^{o(1)}\), while the target is \(X^{1/4+\varepsilon}\).

## Frozen objective

Prove (LCD), prove the weaker weighted form sufficient in (65.8), or
derive a sharp self-return/countermodel showing that period-four pairing,
Fourier expansion of the sawtooth, a second hyperbola decomposition, or
currently available short-divisor theorems cannot supply the missing
\(H/L\) factor.

A positive route may use:

1. exact \(j\bmod4\) pairing before absolute values;
2. Fourier/Vaaler expansion of (65.11) with a jointly summed
   reciprocal phase \(kX/j\);
3. a two-dimensional large-sieve, spectral, or exponent-pair estimate
   whose hypotheses match the moving thin hyperbola;
4. cancellation in the signed crossing sequence as \(v\) varies;
5. the full weighted wavelet form if pointwise (LCD) is unnecessarily
   strong.

## Required controls

- exact Abel sign and index shift in (65.8);
- sampled zero mode, nonpositive tail, and the real-to-integer center;
- the period-four estimate for \(c_X\);
- positive and negative \(v\), exact products, squares, and fourth powers;
- unmatched rows under \(j,j+2\) or \(j,j+4\) pairing;
- Vaaler/Fejer truncation residual if a sawtooth expansion is used;
- uniformity in \(v\), \(\nu\), and the fixed cutoff \(\Xi\);
- target power \(X^{1/4}\) and missing factor \(T/X^{1/4}\);
- comparison with PSC without claiming equivalence;
- source hypotheses and the omitted sharp-saddle/full-cone modules.

## Forbidden shortcuts and promotion gate

Do not replace the moving truncated divisor coefficient by a complete
divisor function or \(r_2/4\). Do not infer discrepancy from zero moments
alone. Do not take absolute values over the crossing set and call the
result cancellation. A bound for a smoothed additive shift, a fixed
shift, or complete automorphic coefficients is not applicable until its
exact hypotheses are matched.

A local-discrepancy lemma may be promoted only after a clean independent
rederivation and hostile seam/source audit. A radial interval additionally
requires inserting it into (65.8), controlling the wavelet tails, and
then completing the sharp \(j=\sqrt X\) saddle, lower \(j\) pieces,
entry/exit, negative frequencies, and subtraction exactly once. No
Gauss-circle exponent changes in this round unless all those gates close.
