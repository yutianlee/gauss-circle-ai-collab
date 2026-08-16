# Round 83 synthesis

## Objective and outcome

Round 83 asked whether the coherent nonzero M1 residue offsets gain a
fixed power of (B=C/T) in the first upper-conductor residual band.
They do not, with the currently audited methods.  The round nevertheless
removes one complete dual slice and identifies a strictly smaller exact
survivor.

## All-class normal form

After the class-dependent rescaling (c=g_\kappa x), the odd and both
even local units are

\[
 u(g_\kappa x)=\zeta e_{M_\kappa}(K_\kappa\bar x),
 \qquad
 (g_\kappa,M_\kappa,K_\kappa)
 \in\{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\}.
\]

Thus the exact smooth principal row is

\[
 {1\over M}\sum_{n\in\mathbb Z}S(n,K;M)I_b(n),
\]

where (I_b) is the Fourier transform of the actual reciprocal symbol.
Finite orthogonality removes the same-residue mode once and gives the
remaining energy as a literal (d=0) slice plus

\[
 \mathfrak Y_C^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.                              \tag{83.S1}
\]

## New target-safe slice

Sampled Parseval and the reciprocal autocorrelation phase prove

\[
 \sum_n|I_b(n)|^2
 \ll_\varepsilon X^\varepsilon M C/g_\kappa.
\]

The literal (d=0) contribution is therefore target-safe.  A purely
internal bound is

\[
 \ll_\varepsilon X^\varepsilon B^2C
 =X^\varepsilon C^3/T^2
 \ll X^\varepsilon J^2/T,
\]

and the standard complete Kloosterman bound sharpens it to
(O_\varepsilon(X^\varepsilon BC)).  Nonzero multiples
(d\equiv0\pmod M) remain in (83.S1).

## Obstructions and sources

Prime-power offsets make a coefficient-free pointwise square-root bound
false: the zero additive-frequency rational sum can have sizes
(q^{3/4+o(1)}) and (q^{7/8+o(1)}).  These sparse examples do not
refute a gcd-sensitive actual-weight average.

The all-offset kernel is rank one before the actual reciprocal symbol is
used.  Complete Fourier or Poisson transforms therefore self-return.
No audited current theorem for trace correlations, products of
Kloosterman sums, incomplete inverse sums, or varying-modulus dispersion
accepts the literal composite moduli and joint weights.  Optimistic
square-root cancellation over the offsets would give only
(B^{-1/2}), short of the full-band (B^{-5/9}).

## State decision

Promote the exact all-class dual-difference reduction, but no conductor
extension.  Keep (83.S1), `M9-M1`, `M9-M2`, `M9`, endpoint uniformity,
and the Gauss-circle exponent open.

The next proof target is the centred (d\ne0) Kloosterman-product
correlation with the actual stationary Fourier weights retained.
