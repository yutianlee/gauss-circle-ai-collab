# Round 97 conductor review: physical partition and normalization

Starting graph SHA-256:
a2b3387c43d467aaa2223ecb31807cd09cf0d429dcebd9b7bde0db6f14cf3657

## Exact coefficient and phase diagram

The literal M2 coefficient is

\[
 \beta_{h,H}
 =-\frac{\Phi(|h|/(H+1))}{\pi |h|}
 \chi_4(|h|)\mathbf 1_{2\nmid h}.
\]

Indeed, for odd \(h\),

\[
 e(h/4)-e(3h/4)=2i\chi_4(h),
\]

and the difference is zero for even \(h\). This is an algebraic
normalization already contained in the proved beta identity; it is not
an open analytic estimate.

The active power triangle and the complement of the accepted direct
owners are exactly

\[
 \Omega=\{1/4\le\delta\le1/2,\ 0\le\ell\le\delta-1/4\},
\]

\[
 \mathcal U=
 \{(\delta,\ell)\in\Omega:
 \ell<\delta-1/4,\ 178\ell+1638\delta>463\}
 \setminus\{(1/2,0)\}.
\]

The owner order is bottom, Fejer residual, terminal T2S, the full
second-derivative cell, the TTY wedge, and only then \(\mathcal U\).
This makes the terminal/TTY boundaries and the isolated point
one-count.

## Physical hard/smooth split

The physical denominator partition, rather than the limiting exponent,
selects the endpoint owner. There is exactly one band containing the
jump at \(d=y=\lfloor\sqrt X\rfloor\). Every other active band is a full
smooth rescaling. For the model labels

\[
 D_j=2^{-j}\sqrt X,\qquad \frac KL=\frac X{D_j^2}=4^j,
\]

every fixed \(j\) has exponent \(1/2+o(1)\), but only \(j=0\) is hard.
Consequently no statement phrased only as “\(\delta=1/2\)” can own the
endpoint.

For a literal exhaustive smooth split, freeze once and for all

\[
 C_{\rm bal}=16.
\]

A smooth residual label is called balanced when
\(1\le K/L\le C_{\rm bal}\), with the boundary assigned to the balanced
side. After a bounded number of dyadic subdivisions, the actual symbol
then has the accepted form \(A(h/L,k/L)\) with support and normalized
derivatives in one fixed compact set. Thus the accepted balanced gcd
reduction applies uniformly. Every remaining smooth label has
\(K/L>C_{\rm bal}\) and is unbalanced. The value \(16\) is not
arithmetically special; it is a fixed conductor convention which makes
the already accepted fixed-comparability reduction and its complement
literal and disjoint.

## Nonempty survivor controls

The unbalanced survivor is nonempty: \((\delta,\ell)=(1/3,0)\) lies
strictly in \(\mathcal U\) and has \(K/L=X^{1/3}\).

The balanced smooth survivor is also nonempty. Take a smooth band
\(D\asymp \frac12\sqrt X\), so \(K/L\asymp4\), and take
\(L\asymp X^{1/8}\). It is nonterminal, violates the TTY inequality by
a fixed power margin, and is not the unique hard profile. Hence a hard
canonical estimate leaves both smooth classes genuinely unowned.

## Endpoint and one-count controls

The bottom is removed before Fourier expansion. R5-Full owns every
active Fejer residual once, including floors, exact products, shifted
legs, jumps, and the hard top. Smooth Poisson errors and support
crossings are attached to their parent smooth label. The one-sided
principal endpoint, half weight, principal-value convention, and
stationary errors are attached to the unique hard label.

Half-open denominator and frequency labels, with the final frequency
block clipped at \(H_D=\lfloor DX^{-1/4}\rfloor\), give one-count
ownership for real \(X\). There are \(O(\log^2X)\) labels, absorbed by
the usual epsilon shrink.

## Review decision

The exact physical partition passes. The canonical hard-top theorem
alone is insufficient. With the fixed balanced convention above, the
three residual families are disjoint and exhaustive:

\[
 \mathcal U_{\rm hard},\qquad
 \mathcal U_{\rm sm,bal},\qquad
 \mathcal U_{\rm sm,unbal}.
\]

No estimate for any of these three families is proved in Round 97.

