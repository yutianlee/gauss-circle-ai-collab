# Round 96 conductor adjudication

Starting graph SHA-256:
242a5f0c6cb22d2e9a400bca110a91c08aea3b3cc8c537bc17fd73418df88fd1

## Evidence agreement

The isolated blind rederivation, analytic attack, hostile/source audit,
and conductor calculation agree on the exact primitive lattice,
character, moving endpoints, half-integral carrier, and capacity. The
reports were produced independently under their assigned contexts and
each contains the required seven sections.

The strict hygiene scan passes for all three reports:

- seven numbered sections;
- balanced inline and display TeX delimiters;
- no forbidden control or CR bytes;
- no trailing whitespace;
- clean whitespace diff check.

## Accepted kernel

The following scoped theorem is accepted:

1. Fixed-\(m\) legal \(q\)-shifts have step two and character
   autocorrelation \(+1\).
2. Fixed-\(a\) sign-changing shifts produce the exact complete-symbol
   Fejer Gram, not a scalar alternating estimate.
3. A separately estimated diagonal and coefficientwise shifted
   correlations gain at most \(D^{-1/2}\); hard \(D\asymp1\),
   \(\rho\to\infty\) blocks survive.
4. Shift Fourier transform, parity-aware Poisson, and the adjoint
   reciprocal transform return to the original half-frequency /
   transposed two-character row at equal capacity.
5. The full homogeneous phase has a radial null direction, although
   fixed-variable curvature is nonzero.

This is a route obstruction. It is not a lower bound for the complete
actual block and not a proof that a signed Gram theorem is impossible.

## First open kernel

For

\[
 F_a(q)=\mathbf1_{\rm residual}
 \sum_{g,k}\omega(k)W_R(\Lambda_{a,q}/k)
 \mathfrak C^\circ_{a,a+2q,k}(g),
\]

define

\[
 \mathcal G_H^{\rm act}
 =\sum_{a,n}\left|
 \sum_{0\le h<H}(-1)^hF_a(n+h)\right|^2.
\]

The first strict survivor is to prove, for some \(1\le H\ll D\),

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon\frac{H^2}{\rho}E_0,
 \qquad E_0\asymp_{X^\varepsilon}LJD^2,
\]

or an equivalent direct theorem for the complete nonzero-shift
correlation. Its reduced second derivative contains

\[
 \frac{g'}{k'(a+2q+2s)^{3/2}}
 -\frac g{k(a+2q)^{3/2}},
\]

so the next mechanism must treat this actual determinant locus jointly
with the primitive mask, moving \(k,g\) fibres, metric density, and
entry/exit symbols.

## State decision

Create one proved internal obstruction node and one open actual-Gram
node. Add the Round-96 evidence to the canonical density-discrepancy
node, but leave it open. Reject the automatic-alternation,
coefficientwise full-gain, zero-frequency deletion, determinant-only,
and formal-wedge claims. Make no downstream promotion.

