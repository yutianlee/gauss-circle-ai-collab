# Conductor candidate: the direct one-third theorem

## 1. Candidate result

For every \(\varepsilon>0\) and every real \(X\geq2\), the accepted
hyperbola--Vaaler route and direct block menu imply

\[
 P(X)\ll_\varepsilon X^{1/3+\varepsilon}.              \tag{C91.1}
\]

This is a candidate until the Round-91 blind and hostile gates close. It
does not prove the target exponent \(1/4\).

## 2. Uniform block lemma

Let \(X^{1/4}\leq D\leq X^{1/2}\), \(1\leq L\leq
DX^{-1/4}\), and let \(\mathcal B_i(D,L;X)\) be an actual M1 or M2
dyadic frequency block. The accepted estimates are

\[
 \mathcal B_i\ll_\varepsilon X^\varepsilon(1+D/L)       \tag{C91.2}
\]

and

\[
 \mathcal B_i\ll_\varepsilon X^\varepsilon
 \left\{\left({LX\over D}\right)^{1/2}
       +{D^{3/2}\over(LX)^{1/2}}\right\}.              \tag{C91.3}
\]

Put \(R=D/L\). If \(R\leq X^{1/3}\), (C91.2) proves the
\(X^{1/3+\varepsilon}\) bound. If \(R>X^{1/3}\), then

\[
 \left({LX\over D}\right)^{1/2}=\left({X\over R}\right)^{1/2}
 \leq X^{1/3},                                        \tag{C91.4}
\]

while \(D\leq X^{1/2}\) and \(R\leq D\leq X^{1/2}\) give

\[
 {D^{3/2}\over(LX)^{1/2}}=D\left({R\over X}\right)^{1/2}
 \leq X^{1/4}.                                        \tag{C91.5}
\]

Thus every actual block is \(O_\varepsilon(X^{1/3+\varepsilon})\).

## 3. Menu optimality

The exponent \(1/3\) is the best uniform output of the accepted direct
menu. At

\[
 (\delta,\ell)=\left({1\over2},{1\over6}\right),       \tag{C91.6}
\]

T2S and the first second-derivative term both have exponent \(1/3\), the
second second-derivative term has exponent \(1/6\), and the trivial term
has exponent \(1/2\). The audited TTY exponent is

\[
 {89(1+1/6)+819/2\over1282}={770\over1923}>{1\over3}. \tag{C91.7}
\]

This proves only optimality of this estimate menu, not a lower bound for
the actual sum.

## 4. Pointwise Fejer residual

For \(H_D\asymp DX^{-1/4}\) and
\(\Delta=D/H_D\asymp X^{1/4}\), positivity and nearest-product grouping
give

\[
 {1\over H_D}\sum_{d\asymp D}|w_D(d)|K_{H_D}(X/d)
 \ll_\varepsilon X^\varepsilon
 \sum_{n\asymp X}\min\left(1,{\Delta^2\over|X-n|^2}\right)
 \ll_\varepsilon X^{1/4+\varepsilon}.                 \tag{C91.8}
\]

Each \(n\) has at most \(\tau(n)\) participating products. Exact products
use the value \(1\). The two quarter-shifted legs replace \(n=dm\) by
\(n=d(4m-\rho)\), \(\rho=1,3\), so the same count applies. The far tail,
top truncation, and integer sawtooth convention are already included.

## 5. Dyadic assembly

The inactive bottom denominator range costs \(O(X^{1/4})\) before the
Vaaler expansion. Each active denominator shell has \(O(\log X)\)
frequency blocks, and there are \(O(\log X)\) active denominator shells.
Sections 2 and 4 therefore give

\[
 \sum_D\bigl(|\mathcal M_1(D;X)|+|\mathcal M_2(D;X)|
              +\mathrm{FejerResidual}(D)\bigr)
 \ll_\varepsilon X^{1/3+\varepsilon}.                 \tag{C91.9}
\]

All logarithms are absorbed by the arbitrary \(\varepsilon\).

## 6. Controls requiring independent certification

The Round-91 gates must confirm that (C91.2)--(C91.3) are the literal
fully weighted M1 and M2 blocks, including both signs, the spatial
\(\chi_4(d)\), the M2 \(\chi_4(h)\), quarter shifts, and the hard top
sampled-BV profile. They must also confirm that (C91.8) is pointwise for
real \(X\), owns exact products and floors, and does not use M9 or the
open transformed endpoint cones.

## 7. Proposed state effect

If the gates pass, promote R5-Full-reconciliation and R5-Full, create
M9-direct-one-third-envelope and GC-partial-one-third, and keep
M9-M1, M9-M2, M9, M9-endpoint-uniformity, and GC-target open.
