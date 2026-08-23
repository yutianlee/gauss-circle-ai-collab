# Conductor Round 116 source-scope audit

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

No external theorem is used below to estimate the Round-116 target.

## 1. Van der Corput transform

Joseph Vandehey, *Error term improvements for van der Corput transforms*,
arXiv:1205.0090, states the one-dimensional B-transform in the form

\[
 \sum g(n)e(f(n))
 =\sum_{f'(x_r)=r}{g(x_r)e(f(x_r)-rx_r+1/8)\over
 \sqrt{f''(x_r)}}+\Delta
\]

under smoothness, positive-curvature, and bounded-variation hypotheses. The
paper explicitly records that the transform is involutive and that applying
it twice in succession yields no gain.

After the literal divisor-progression and gate partition, the Round-116
one-variable phase has positive second derivative
(asymp d^2L^2), and the smooth pieces are plausible inputs to such a
formula. This source does not by itself certify the campaign reduction:
the divisor sum, all short progression pieces, transition endpoints, and
the aggregate error over (O(L^3)) outer triples still have to be priced.
The conductor therefore uses the source only as a transform/error and
involution check, not as an estimate for the signed alias family.

Primary source:
https://arxiv.org/abs/1205.0090

## 2. Generalized double large sieve

Jiamin Li and Jing Ma, *Three-dimensional exponential sums under constant
perturbation*, arXiv:2302.05870, Theorem 1.1 treats a separated
three-variable monomial/reciprocal phase with coefficients
(a(h,m)b(n)), fixed positive exponents, a fixed positive perturbation, and
an explicit parameter inequality. Its Proposition 2.2 is an abstract
double-large-sieve inequality whose application requires two separately
verified spacing energies.

The Round-116 alias coefficient is not of the theorem's stated form. Its
alias lattice depends on a divisor (d); its weight couples (h,k,q) and
the alias through two gcd masks, two slanted symbols, progression residues,
two pair-dependent gate deletions, and boundary kernels; and the target is
uniform for real (X). Neither the separated coefficient hypothesis nor
the required spacing energies have been matched. Theorem 1.1 cannot be
imported. Proposition 2.2 would only rename the open problem until both
literal spacing forms and their diagonal costs are proved.

Primary source:
https://arxiv.org/abs/2302.05870

## 3. Source decision

The first source supports the exact B-process normalization and its
capacity-preserving involution after a separate literal error audit. The
second supplies no direct owner for the present kernel. No source currently
proves the (L^3X^\varepsilon) alias estimate.
