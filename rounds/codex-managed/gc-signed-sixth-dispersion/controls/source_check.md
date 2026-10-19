# Round235 Bessel source check

Conductor, checked12 October2026; mathematical source only, not a new circle estimate. The archived earlier Hankel report is also explicitly reviewed in the actual-bridge seam.

[NIST DLMF10.17.1–3](https://dlmf.nist.gov/10.17) gives the fixed-order expansion. At order0 its first coefficient is−1/8, so

J0(z)=sqrt(2/(pi z))[cos(z-pi/4)+(1/(8z))sin(z-pi/4)]+O(z^(-5/2)).

[DLMF10.17(iii)](https://dlmf.nist.gov/10.17#iii) bounds the two truncated remainders on the positive real axis. Here nu=0 and one term is retained in each series; both truncation conditions hold. Our z=2pi v u, v>=1, u comparable to sqrt(N) tends to infinity uniformly on the smooth compact annulus. Hence the displayed error is uniform and its dual sum converges after both terms are retained. No complex-order or transition theorem is invoked.

[DLMF10.9.1](https://dlmf.nist.gov/10.9.E1) supplies the order-zero integral representation for radial Fourier normalization. No source here proves the arithmetic S6 hypothesis. All Li–Yang and sharp-circle source qualifications remain those of the accepted graph.
