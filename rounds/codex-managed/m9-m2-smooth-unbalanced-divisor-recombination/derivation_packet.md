# Round 107 derivation packet: unbalanced smooth divisor recombination

## Accepted inputs

The smooth physical M2 block has the exact Poisson form

\[
 \mathcal B^+_{L,W}
 =-{e(1/8)\over2\pi}X^{1/4}(LK)^{-3/4}
 \mathcal T_{L,K}+O_W(1),
\]

\[
 \mathcal T_{L,K}
 =\sum_{h\asymp L}\sum_{k\asymp K}
 \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk}),
\qquad K={XL\over D^2}.
\]

The estimate \(\mathcal T_{L,K}\ll (LK)^{3/4}X^\varepsilon\)
is equivalent-hard to the positive smooth block target. The residual
unbalanced region is

\[
 {1\over4}\le\delta<{1\over2},\quad
 0\le\ell<\delta-{1\over4},\quad
 178\ell+1638\delta>463,
\]

up to fixed-support boundary cells and with the isolated owned point
removed.

## Product coefficient

Use the exact identity

\[
 \mathcal T_{L,K}
 =\sum_{n\asymp LK}
 \left(\sum_{h\mid n}\chi_4(h)a_{L,K}(h,n/h)\right)
 e(\sqrt{Xn}).
\]

The inner sum is a moving dyadically truncated divisor coefficient.
For a separated Mellin mode it has Dirichlet series
\[
 L(s-it_1,\chi_4)\zeta(s-it_2).
\]
The complete convolution is \(1*\chi_4=r_2/4\), but the literal slanted
symbol, Vaaler taper, height floor, physical scale, signs, profiles and
stars need not assemble into the complete convolution.

## Candidate fork

Try, in order:

1. derive an exact double Mellin representation with rapid height decay;
2. apply the two functional equations on a common contour and track the
   transformed dyadic factor lengths and root numbers;
3. decide whether the returned factor box is the original
   \((L,K)\)-packet, a transposed packet, or a genuinely shorter packet;
4. test whether summing the physical smooth one-count before absolute
   values completes \(r_2/4\) and whether the complementary pieces are
   target-safe;
5. if no gain occurs, state the exact smallest truncated-divisor
   correlation and its capacity deficit.

The conductor's preliminary ledger is
\[
 M={XL^2\over D^2},\qquad F=\sqrt{XM}={XL\over D},
\]
and one-variable curvature is short by \(H_D=DX^{-1/4}\). Any claimed
gain must beat this factor on a nonempty residual cell.

## Prohibited shortcuts

Do not:

- replace the truncated coefficient by \(r_2/4\) without an exact
  compatible partition;
- invoke Popov or Voronoi before mapping both Mellin heights, cutoffs,
  signs and errors;
- use exact-product energy as a signed estimate;
- discard the character before factor regrouping;
- infer a two-dimensional curvature gain from the rank-one Hessian;
- claim a global exponent from a reduction or a proper subpacket.

