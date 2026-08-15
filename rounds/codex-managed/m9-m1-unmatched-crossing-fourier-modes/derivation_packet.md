# Round 66 packet: Fourier modes of the unmatched crossing functional

## Accepted input

Let (n_0=\lfloor X\rfloor), (J=\sqrt X),
(T=\sqrt{X/N}=X^{1/2-\nu/2}), and
(\Xi\in C_c^\infty((0,1))). Round 65 reduces the fixed-interior
reciprocal cone to the signed unmatched crossing discrepancy

\[
 \mathfrak D_X(v)=\sum_j\chi_4(j)\Xi(j/J)
 \left(\{n_0/j\}-\{(n_0+v)/j\}\right),
\tag{66.1}
\]

for integral (v), followed by an exact wavelet-difference average. The
target is (X^{1/4+\varepsilon}); at \(\nu=2/5\), the absolute capacity
(T=X^{3/10}) misses by (X^{1/20}=H/L).

## Exact smoothed Fourier interface

Fix a floor-compatible Vaaler truncation height (K\geq1). Away from
the explicit Fejer residual and integer endpoint convention, the signed
main modes have the form

\[
 \mathcal S_k(v)
 =\sum_{j\geq1}\chi_4(j)\Xi(j/J)
 e(kn_0/j)\{1-e(kv/j)\},
 \qquad 1\leq |k|\leq K,
\tag{66.2}
\]

weighted by coefficients (\asymp1/k\). Because \(|v|\ll TX^\eta\)
and (j\asymp J\),

\[
 1-e(kv/j)\ll\min(1,|k|T/J).
\tag{66.3}
\]

The phase (kn_0/j\) has derivative size (kX/J^2\asymp k) and
curvature size (kX/J^3\asymp k/J\). Character splitting gives two
step-four reciprocal sums, but does not by itself make (66.2) small.

## Frozen objective

Prove the full Vaaler main-plus-residual contribution to the exact
wavelet-weighted Round-65 functional is (O(X^{1/4+\varepsilon})), or
derive the sharpest rigorous mode theorem/no-go. In particular:

1. optimize (K), using the exact endpoint Fejer count rather than a
   pointwise residual bound;
2. apply the strongest lawfully matched reciprocal-phase exponent pair,
   van der Corput, large-sieve, or bilinear estimate to the jointly summed
   (j,k,v) functional;
3. preserve the factor (1-e(kv/j)), which may be the source of the
   required (T/J) gain at low modes;
4. distinguish pointwise LCD from the weaker wavelet-weighted target;
5. calculate the exact exponent at \(\nu=2/5\) and any nonempty radial
   interval that closes.

The accepted Tao--Trudgian--Yang pair
((89/1282,997/1282)) may be used only after auditing its one-variable
phase hypotheses. A bilinear or large-sieve theorem must match the
moving amplitude and prescribed center exactly.

## Required controls

- floor-compatible Vaaler coefficients and positive Fejer residual;
- (k=0), exact integers, squares, and fourth powers;
- signs for positive and negative (v) and (k);
- cutoff derivatives and step-four residue classes;
- low, transition, and high (k) regimes around (J/T=X^{\nu/2});
- exact wavelet weighting before any absolute value in (v);
- diagonal terms in any (k)- or (v)-mean square;
- target power and optimization in (K);
- primary-source hypotheses and full-cone scope.

## Promotion gate

A mode estimate may be promoted if independently rederived and hostilely
audited. A radial interval additionally requires summing all modes and
the Fejer residual in the exact wavelet functional. No exponent changes
without the sharp saddle and the remaining full-cone modules.
