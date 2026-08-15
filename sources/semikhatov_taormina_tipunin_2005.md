# Source card: higher-level Appell transformations

## Source

A. M. Semikhatov, A. Taormina, and I. Yu. Tipunin,
*Higher-Level Appell Functions, Modular Transformations, and
Characters*, Communications in Mathematical Physics 255 (2005),
469--512.

- Primary preprint: https://arxiv.org/abs/math/0311314
- DOI: https://doi.org/10.1007/s00220-004-1280-7

Companion normalization/completion source used by the Round-63 audit:
S. Zwegers' higher-level Appell convention as reproduced with its exact
completion and Jacobi laws in Bringmann--van Ittersum--Kaszian,
https://arxiv.org/abs/2401.02820, equations (2.12)--(2.15).

## Exact imported statements

Semikhatov--Taormina--Tipunin define, for integer \(\ell>0\),
\(\tau\in\mathbb H\), and
\(\nu+\mu\notin\mathbb Z\tau+\mathbb Z\),

\[
 K_\ell(\tau,\nu,\mu)=
 \sum_{m\in\mathbb Z}
 \frac{e^{\pi i\ell m^2\tau+2\pi i\ell m\nu}}
 {1-e^{2\pi i(\nu+\mu+m\tau)}}.
\]

Their Theorem 1.1 gives the \(S\)-transformation as a transformed
\(K_\ell\) plus a sum over \(0\le a<\ell\) of theta functions times an
explicit Mordell-type \(\Phi\) integral.  At \(\ell=4\), all four terms
must be retained.

The completed higher-level Appell function \(\widehat A_\ell\) in the
companion convention has an explicit sum of \(\ell\) theta-times-
\(R\) corrections and satisfies exact elliptic and modular Jacobi laws.

## Round-63 specialization

The exact one-sided kernel uses

\[
 K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right),
\]

for which \(\nu+\mu=1/2\), so the pole exclusion is satisfied on
\(\mathbb H\).  Direct algebra, not the source theorem, proves

\[
 K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)
 =\frac12+2\sum_{h\ge1}rac{z^{4h^2+h}}{1+z^{2h}},
 \qquad z=e^{\pi i\tau}.
\]

The tempting \(K_4(\tau,0,1/2)\) specialization is different: bilateral
pairing collapses it to an ordinary theta half-sum.

## Hypothesis and scope audit

- The meromorphic bilateral definition and transformation theorem apply.
- The paper's double-cone expansion requires
  \(|q|<|e^{2\pi i(\nu+\mu)}|<1\); it does not apply here because the
  middle modulus is one.
- The moving section is stabilized under \(\Gamma(2)\) only after exact
  elliptic shifts, and only the completed function transforms.
- The four Mordell/nonholomorphic corrections are not error terms and
  cannot be omitted.
- Neither source proves a uniform convolution estimate against
  \(e(\sqrt{Xn})\), a reciprocal character sum, or any Gauss-circle
  exponent.

## Project status

The source is accepted for the exact Appell transformation and
completion ledger only.  Its applicability to the required signed
square-root radial estimate is rejected absent a new correlation
theorem.

