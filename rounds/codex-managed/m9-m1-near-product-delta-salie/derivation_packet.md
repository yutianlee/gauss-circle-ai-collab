# Round 70 packet: delta/Salié attack on the signed product wavelet

## Accepted antecedent

Let

\[
 J=X^{1/2},\qquad T={J\over Q},\qquad Q=X^{1/5}
\]

at the benchmark. Round 69 reduces the missing direct estimate to

\[
 \boxed{\mathcal D_{J,T}(X):=
 \sum_{\substack{m,n\asymp J\\n\ \mathrm{odd}}}
 \chi_4(n)W(m/n)K\!\left({mn-X\over T}\right)
 \ll J^{1/2}X^\varepsilon.}
 \tag{70.1}
\]

Here (W) is fixed smooth and compactly supported in one fixed
one-sided central ratio sector. The actual wavelet (K) is Schwartz;
after a finite fixed Mellin decomposition it is the Fourier transform of
a smooth compactly supported function away from zero and has all
continuous moments zero. Absolute product grouping gives only

\[
 \mathcal D_{J,T}(X)\ll TX^\varepsilon,
 \qquad T=X^{3/10},quad J^{1/2}=X^{1/4}.
\]

Thus the exact deficit is (X^{1/20}).

## Exact offset form

Put (N=\lfloor X\rfloor) and (\vartheta=X-N\). Then

\[
 \mathcal D_{J,T}(X)=
 \sum_{s\in\mathbb Z}K\!\left({s-\vartheta\over T}\right)
 \sum_{\substack{mn=N+s\\m,n\asymp J\\n\ \mathrm{odd}}}
 \chi_4(n)W(m/n).
 \tag{70.2}
\]

This is the only permitted delta constraint. The central coefficient is
truncated by the actual ratio sector; it is not (d(N+s)), not
(r_2(N+s)/4), and not an arbitrary coefficient sequence.

## Proposed new mechanism

Insert a finite circle/delta-symbol resolution of (mn-N-s=0), sum the
actual (s)-wavelet before absolute values, and apply Poisson/Voronoi in
the two product variables only if the full character and ratio symbol
are retained. Determine whether the resulting complete sums are
Kloosterman, Salié, Gauss, or a degenerate return. Audit the exact modulus
range, dual lengths, zero frequencies, gcd factors, and Weil/spectral
normalization.

This round must not count the Round-69 two-dimensional Poisson return as
a new estimate. A successful result must exploit arithmetic cancellation
created by the finite delta moduli or prove a genuinely stronger theorem
for (70.1).

## Mandatory controls

- retain (n) odd, (chi_4(n)), (W(m/n)), (K), and the real-centre
  shift (artheta);
- state the exact delta-symbol identity and modulus cutoff before any
  asymptotic estimate;
- compute every complete exponential sum, its modulus, gcd dependence,
  and zero-frequency term;
- keep the (s)-sum signed until its transform is explicit;
- audit exact products, square/fourth powers, and rational stationary
  aliases;
- derive the full (J,T,Q) power ledger and the required (J^{1/2})
  bound;
- audit primary Kuznetsov, Kloosterman/Salié, divisor-short-interval, and
  delta-method sources theorem by theorem;
- distinguish a transform identity from an estimate and record any
  self-return;
- make no full-cone, M9--M1, M9, or exponent promotion.

## Required report contract

Every report has exactly seven semantic sections: result; exact statement
and hypotheses; proof/derivation; first doubtful step; controls;
dependencies and exact artifacts; recommended state effect. Numerical
work is optional and diagnostic only. At least 80 percent of the round is
analytical/algebraic.

