# Tao--Trudgian--Yang 2025 source card

## Bibliography

Terence Tao, Tim Trudgian, Andrew Yang, *New exponent pairs, zero density
estimates, and zero additive energy estimates: a systematic approach*,
arXiv:2501.16779 (submitted 28 January 2025).

- Abstract page: https://arxiv.org/abs/2501.16779
- Primary source inspected: current arXiv TeX source.

## Statements used by this project

Their definition of an exponent pair \((k,\ell)\) gives, for a model phase
\(F\), \(T\geq N\geq1\), and \(I\subset[N,2N]\),

\[
\sum_{n\in I}e(TF(n/N))
\ll (T/N)^{k+o(1)}N^{\ell+o(1)}.
\]

The theorem labelled `New exponent pairs` states that the following are
exponent pairs:

\[
\left(\frac{89}{1282},\frac{997}{1282}\right),\qquad
\left(\frac{652397}{9713986},\frac{7599781}{9713986}\right),
\]

\[
\left(\frac{10769}{351096},\frac{609317}{702192}\right),\qquad
\left(\frac{89}{3478},\frac{15327}{17390}\right).
\]

The paper derives these via its exponent-sum growth function, exponent-pair
duality, classical exponent-pair processes, and a computer-assisted polytope
optimization over recorded hypotheses.

## Exact project specialization

For

\[
e\!\left(\frac{hX}{4d}\right),\qquad d\asymp D,\quad h\asymp L,
\]

take \(N=D\), \(T\asymp hX/D\), and, after complex conjugation,
\(F(u)=-u^{-1}\). Since \(F'(u)=u^{-2}\), this is a model phase with
source parameter \(\sigma=2\). Then

\[
T/N\asymp hX/D^2.
\]

For a fixed scale-normalized smooth/BV denominator weight, partial summation
transfers the unweighted interval estimate.  The first new pair therefore
gives

\[
B_L(D;X)
\ll_\varepsilon
X^{[89(1+\ell)+819\delta]/1282+\varepsilon},
\qquad D=X^\delta, L=X^\ell.
\]

It reaches the project target \(X^{1/4+\varepsilon}\) precisely when

\[
178\ell+1638\delta\leq463.
\]

## Scope controls

- The theorem is applied only to the reciprocal model phase, which is within
  the source's phase class.
- Weighted transfer requires a uniform normalized BV profile; arbitrary
  bounded weights are not covered.
- The theorem gives a pointwise bound for a single dyadic frequency block.
- It does not close the rest of the M2 parameter triangle and has no direct
  implication for the signed fourth-moment route.
