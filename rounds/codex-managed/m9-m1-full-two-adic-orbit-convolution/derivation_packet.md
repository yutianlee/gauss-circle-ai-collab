# Round 101 derivation packet

## 1. Accepted input

Round 100 proves the exact \(v_2(M)=3\) formula. Its local weight is constant
on the four odd bases when \(4\mid u\), and the fixed actual rows form a
\(\mathbb Z/4\mathbb Z\) cross-projection. The only aligned square has
\(R_*=4\) and is already coarse-owned.

## 2. Full two-power factor

Write

\[
 M=2^\nu N,\qquad N\ \mathrm{odd},\qquad L=2^{\nu-1}.
\]

For every nonempty local mask, use \(x=1+2j\), \(A=2a\),
\(B_2=2c\), \(V=2v\), \(j\bmod L\). Retain the complete weight

\[
 w_j=e_{2^\nu}\!\left(u(1+2j)+K\Phi_{2a,2c,2v}(1+2j)\right).
\]

The physical local coupling is

\[
 \sum_{j\bmod L}w_jF_j^a\overline{G_{j-v}^c}.
\]

Derive its exact DFT-convolution form; do not assume \(w_j\) is constant,
a character, or low-period.

## 3. Mandatory owners

- The global integer \(u=0\) is owned exactly once.
- Round-87 same-group, Round-88 coarse and good-prime, and Round-89 certified
  cells are removed successively before the hard survivor.
- A lower local period is an exact routing identity, not automatically a
  physical power saving.
- Aligned or reversal slices must be tested against the coarse quotient and
  prior group labels before being called hard.

## 4. Mandatory symbol scope

Retain every local and odd-cofactor inverse phase, nonunit \(K\), modulus
multiple, all four \(I_b\)-rows, dyadic multiplier, signs, aliases,
reflections, entry/exit, stars, and zero extension. Treat all three accepted
class moduli and their actual valuations.

## 5. Quantitative scope

This round succeeds by producing an exact graph-ready full-two-part normal
form and a one-count owner map, or by proving that no simple low-rank
projector survives. It is not required or permitted to infer the missing
\(J^{-1/6}\) estimate from finite Fourier sparsity.

## 6. Downstream scope

Do not infer the canonical hard estimate, GAR, blockwise M9-M1, M9-M2,
endpoint uniformity, M9, or an exponent.
