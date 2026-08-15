# Round 67 packet: signed reciprocal large sieve at a target-sized diagonal

## Accepted input

Write (J=X^{1/2}), (Q=J/T=X^{\nu/2}), and let
(a_j=\chi_4(j)\Xi(j/J)). Round 66 shows that the exact wavelet-filtered
transition of the Round-65 discrepancy is, after harmless Mellin
separation of a fixed smooth ratio profile, a bilinear form

\[
 \mathcal B
 =\sum_{k\asymp Q}b_k\sum_{j\asymp J}a_j e(kX/j),
 \qquad |b_k|\ll Q^{-1},
 \qquad \sum_k|b_k|^2\ll Q^{-1}.
\tag{67.1}
\]

The exact target is

\[
 \boxed{|\mathcal B|\ll_\varepsilon J^{1/2}X^\varepsilon
 =X^{1/4+\varepsilon}.}
\tag{67.2}
\]

The Fejer residual is already target-safe and is not part of this round's
new estimate.

## Exact energy interface

For a fixed nonnegative (w\in C_c^\infty((0,\infty))), define

\[
 \mathcal E
 =\sum_k w(k/Q)
 \left|\sum_j a_j e(kX/j)\right|^2.
\tag{67.3}
\]

Cauchy gives (67.2) from

\[
 \boxed{\mathcal E\ll_\varepsilon QJX^\varepsilon.}
\tag{RSLS}
\]

The diagonal (j_1=j_2) is

\[
 Q\widehat w(0)\sum_j|a_j|^2\asymp QJ,
\tag{67.4}
\]

so (RSLS) is optimally scaled. Poisson summation in (k) gives the
exact signed off-diagonal

\[
 Q\sum_{j_1,j_2}a_{j_1}\overline{a_{j_2}}
 \sum_{m\in\mathbb Z}
 \widehat w\!\left(Q\left[m-X\left(\frac1{j_1}-\frac1{j_2}\right)\right]\right).
\tag{67.5}
\]

Because (j_1,j_2) are odd,

\[
 \chi_4(j_1)\chi_4(j_2)=(-1)^{(j_2-j_1)/2}.
\tag{67.6}
\]

This sign must be retained before estimating the near-integer reciprocal
spacing in (67.5).

## Equivalent B-process return to audit

Using

\[
 \chi_4(j)=\frac{e(j/4)-e(3j/4)}{2i},
\]

Poisson/B-process in (j) converts each fixed-(k) sum into dual
frequencies (r\asymp k\) with phase

\[
 2\sqrt{kX(r-\rho/4)},\qquad \rho\in\{1,3\},
\tag{67.7}
\]

and stationary amplitude of scale ((J/Q)^{1/2}=T^{1/2}). Grouping
(kr) risks returning to the accepted lower-radial square-root product
phase. The exact constant, residue shift, symbol, errors, and whether this
is a strict self-return must be audited rather than assumed.

## Frozen objective

Prove (RSLS), or prove the sharpest rigorous obstruction/self-return. A
positive route may use:

1. the alternating difference sign in (67.6);
2. a signed double-large-sieve estimate for reciprocal points;
3. B-process followed by a square-root product-spacing theorem;
4. grouping near-integer values of
   (X(j_2-j_1)/(j_1j_2)) with full character;
5. exact completion at perfect-square/fourth-power centers.

## Required controls

- exact Cauchy normalization and diagonal constant;
- Mellin separation of the (k/j) profile and uniform (t)-cost;
- Poisson sign, aliases, and (m=0\) versus (m\ne0);
- same/different residue classes and equation (67.6);
- near-diagonal reciprocal clustering at (j\asymp\sqrt X);
- square and fourth-power centers;
- B-process constants, endpoints, and stationary range;
- square-product fibers and Robert--Sargos-type spacing;
- comparison with GAR/PSC without circular promotion;
- primary-source hypotheses and the exact (QJ\) target.

## Promotion gate

(RSLS) requires a clean independent rederivation and hostile audit. Even
if proved, it closes only the fixed-interior transition and still requires
the sharp saddle and remaining full-cone modules before an exponent can
change.
