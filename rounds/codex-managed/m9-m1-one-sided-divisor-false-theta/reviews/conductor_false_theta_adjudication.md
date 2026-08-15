# Round 63 conductor adjudication

Campaign: `m9-m1-one-sided-divisor-false-theta`

## Decision

Promote the exact Appell and Poisson reductions.  Retain the signed
radial estimate, every positive subcritical radial interval, M9-M1,
M9, and the final exponent as open.

## Exact generating and Appell kernel

For

\[
 \mathcal D(n)=\sum_{hq=n,\ q\ {m odd},\ q>4h}\chi_4(q),
\]

absolute convergence on \(|z|<1\) gives

\[
 \mathscr F(z)=\sum_{n\ge1}\mathcal D(n)z^n
 =\sum_{h\ge1}\frac{z^{4h^2+h}}{1+z^{2h}}.
\]

With \(z=e^{\pi i\tau}\), direct bilateral pairing proves

\[
 A_4\!\left(\frac12,-\frac{3\tau}{2};\tau\right)
 =K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)
 =\frac12+2\mathscr F(z).
\]

The moving section is pole-free.  The audited completion carries four
theta--Mordell/nonholomorphic correction terms.  Under \(\Gamma(2)\)
the completed section returns modulo explicit elliptic shifts; the
holomorphic part alone is not modular.

## Exact character-Poisson return

The statement-only report gives, and the conductor independently
recomputed, the following formula.  For smooth compactly supported
\(w\),

\[
\begin{aligned}
 \sum_{h\ge1}\sum_{k\ge1}\chi_4(k)w(4h^2+hk)
 &=\frac12\sum_{h\ge1}w(4h^2)\\
 &\quad+\frac{i}{2}\sum_{h\ge1}\sum_{j\ne0}\chi_4(j)
 \left\{\frac1h\int_{4h^2}^{\infty}
 w(u)e\!\left(-\frac{ju}{4h}\right)du
 -\frac{2w(4h^2)}{\pi i j}\right\}.
\end{aligned}
\]

The subtracted double sum is absolutely convergent.  The half-boundary
has the positive sign because
\(\sum_{j\ne0}\chi_4(j)/j=\pi/2\).

For
\(w(u)=V(u/N)u^{-3/4}e(\sqrt{Xu})\), the positive-\(j\) interior
stationary term is

\[
 \frac{2X^{-1/4}}h\chi_4(j)
 V\!\left(\frac{4Xh^2}{j^2N}\right)
 e\!\left(\frac{Xh}{j}-\frac18\right).
\]

The boundary squares contribute only \(O_V(N^{-1/4})\), but the
reciprocal stationary cone has \(X^{1/4}\) termwise capacity.  Its
signed estimate and its entry/exit transitions are open.

## Capacity and source adjudication

At Abel radius \(e^{-1/N}\), elementary Cauchy--Parseval control returns
\(N^{1/4+\varepsilon}\).  If one separates the periodized radial kernel
into continuous Fourier translates before taking absolute values, the
cost is \(X^{1/4}N^{-1/2}\).  These are failures of two specific
absolute routes, not lower bounds for the exact periodized pairing.

The source audit confirms that unary and positive-definite rank-two
false-theta theorems have the wrong hypotheses.  The applicable Appell
transformation carries four correction terms and supplies no uniform
square-root-phase convolution bound.  Perfect-fourth examples rule out
a generic phase-gap argument but do not disprove the signed target.

## Next interface

The smallest concrete survivor is the complete reciprocal-character
cone, including stationary entry/exit and the Poisson subtraction.  The
next round should exploit the linear \(h\)-phase \(e(Xh/j)\), the
period-four character in \(j\), and hyperbola proximity
\(|X-jm|\), while testing whether every such route simply returns the
accepted M1 kernel.

