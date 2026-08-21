# Conductor review: divisor regrouping, Mellin capacity, and signed survivor

## Exact product algebra

For the literal finite packet,

\[
 \mathcal T_{L,K}
 =\sum_n A_{L,K}(n)e(\sqrt{Xn}),\qquad
 A_{L,K}(n)=\sum_{hk=n}\chi_4(h)a_{L,K}(h,k)
\]

is an exact regrouping. Fibrewise Cauchy--Schwarz gives

\[
 \sum_n|A_{L,K}(n)|^2\ll_\varepsilon LKX^\varepsilon.
\]

This energy controls exact products only. Global Cauchy--Schwarz returns the
trivial \(LK\) scale and does not imply the \((LK)^{3/4}\) target.

For a separated mode, absolute convergence in \(\Re s>1\) gives

\[
 \sum_{n\ge1}{1\over n^s}
 \sum_{hk=n}\chi_4(h)h^{it_1}k^{it_2}
 =L(s-it_1,\chi_4)\zeta(s-it_2).
\]

Double Mellin inversion retains the full slanted symbol. It does not select
the zero Mellin mode and therefore does not replace the coefficient by
\(r_2(n)/4\).

## Failure of automatic radial completion

The identity

\[
 {r_2(n)\over4}=\sum_{h\mid n}\chi_4(h)
\]

requires all divisors with unit weight. A prime \(p\equiv3\pmod4\) gives
an exact control: a literal unbalanced cell may contain \((h,k)=(1,p)\)
without the complementary incidence, so its coefficient is nonzero while
\(r_2(p)/4=0\). The missing incidences belong to terminal, TTY, balanced,
hard, boundary, or otherwise separately owned packets. They cannot be
silently inserted into the residual unbalanced cell.

Even a hypothetical compatible completion is not an imported estimate.
At radial cutoff

\[
 M={XL^2\over D^2},
\]

Popov's audited truncated Voronoi remainder has size

\[
 \sqrt{X/M}\,X^{o(1)}={D\over L}X^{o(1)}.
\]

It is target-sized only when \(L\asymp DX^{-1/4}\), the previously owned
terminal line. Extending the cutoff to \(X^{1/2}\) recovers the complete
Hardy--Voronoi radial sum, which is equivalent to the Gauss-circle target
up to target-sized errors.

## Functional-equation capacity

Put

\[
 F=\sqrt{X M}={XL\over D}.
\]

The radial Mellin integral is concentrated at height \(F\). The two
degree-one functional equations therefore have formal dual factor scales

\[
 L^*\asymp {F\over L}={X\over D},\qquad
 K^*\asymp {F\over K}=D,qquad L^*K^*\asymp X.
\]

Both completed factors have root number \(+1\). Hence no antisymmetric
root-number cancellation occurs. A complete contour argument must still
retain the zeta pole, the double height tails, every transformed owner, and
all horizontal and endpoint errors.

The formal resonant packet has centre of scale \(X\), width

\[
 \Delta={X\over F}={D\over L},
\]

and kernel size \(M^{3/4}X^{-1/4}\) per dual integer. Even granting the
strongest routine uniform transform and divisor bounds, absolute summation
gives

\[
 |\mathcal T_{L,K}|
 \ll_\varepsilon M^{3/4}X^{-1/4}\Delta X^\varepsilon.
\]

The exact excess over the target is

\[
 {\Delta\over X^{1/4}}
 ={D\over LX^{1/4}}={H_D\over L}.
\]

This conditional capacity agrees with the independently derived
character-(B)-process/fixed-centre return. It is not promoted as a full
literal-symbol functional-equation theorem.

## Exact signed correlation criterion

Let

\[
 z_n=A_{L,K}(n)e(\sqrt{Xn})
\]

be extended by zero outside an interval of length \(N\ll M\), and set

\[
 C(q)=\sum_n z_{n+q}\overline{z_n}.
\]

The sliding-window identity and Cauchy--Schwarz give, for every integer
\(1\le Q\le N\),

\[
 Q^2\left|\sum_nz_n\right|^2
 \le (N+Q)\left(
 Q\sum_n|z_n|^2
 +2\sum_{q=1}^{Q-1}(Q-q)\Re C(q)\right).
\]

Consequently, with \(Q\asymp M^{1/2}\), the outside-absolute condition

\[
 \Re\sum_{q=1}^{Q-1}\left(1-{q\over Q}\right)C(q)
 \ll_\varepsilon MX^\varepsilon
\]

is sufficient for the three-quarter target. This is an exact implication;
it does not assert the correlation bound. Expanding \(C(q)\) gives the
literal four-factor condition \(h_1k_1-h_2k_2=q\), with the two characters,
actual symbols, and square-root phase retained. The exact-product case
\(q=0\) is owned by the proved energy bound.

## Decision

The round certifies the regrouping, its Mellin interface, failure of an
automatic \(r_2/4\) completion, the exact signed-correlation implication,
and the strict-interior principal fixed-centre return. It does not certify
the full contour transform, aggregate \(h\)-process error, the signed
correlation, or the required fixed-centre estimate. The open analytic
problem may be stated equivalently as either of the following:

\[
 \mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon,
\]

or, after complete owner-preserving transformation,

\[
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon},
\]

where \(\mathscr R_{D,L}\) is the actual length-\(D/L\) prescribed-centre
truncated \(\chi_4\)-divisor wavelet. No downstream pointwise exponent is
changed.
