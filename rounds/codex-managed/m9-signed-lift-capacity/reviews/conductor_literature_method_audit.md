# Conductor primary-literature method audit

## Decision

The Bombieri--Iwaniec interface in Li--Yang is structurally relevant and admits an exact phase map for each of the two M2 shifts.  It is not presently a black-box proof of M2: the largest active frequency block violates the theorem's displayed Case A and Case B height conditions throughout the project range.  The useful architectural transfer is to keep the two shifted sums separate and require a parameter-feasibility certificate before any theorem import.

## Primary sources checked

- Xiaochun Li and Xuerui Yang, [*An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*](https://arxiv.org/abs/2308.14859), arXiv:2308.14859.  The local primary TeX audited here is `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`.
- Jean Bourgain and Nigel Watt, [*Mean square of zeta function, circle problem and divisor problem revisited*](https://arxiv.org/abs/1709.04340), arXiv:1709.04340.  This remains a structural reference for the double-large-sieve/spacing architecture, not a theorem dependency for M2.
- Jeffrey D. Vaaler, [*Some extremal functions in Fourier analysis*](https://doi.org/10.1090/S0273-0979-1985-15349-2), used through the completed project source card `sources/vaaler_1985.md`.

## Exact shifted-phase map

The M2 coefficient factor is

\[
C_h=e(h/4)-e(3h/4).
\]

Therefore an M2 dyadic frequency block \(L\le |h|<2L\) is the difference of two shifted sums with phases

\[
e\!\left(\frac h4\left(\frac Xd+\rho\right)\right),
\qquad \rho\in\{1,3\}.
\]

Li--Yang's Section 4 sum is

\[
S=\sum_{\mathsf H\le h\le2\mathsf H}g(h/\mathsf H)
\sum_{\mathsf M\le m\le2\mathsf M}G(m/\mathsf M)
e\!\left(\frac{h\mathsf T}{\mathsf M}F(m/\mathsf M)\right).
\]

The exact project map is

\[
\mathsf H=L,\qquad
\mathsf M=D,\qquad
\mathsf T=X/4,\qquad
F_\rho(u)=u^{-1}+\rho D/X.
\]

Indeed,

\[
\frac{h\mathsf T}{\mathsf M}F_\rho(d/D)
=\frac h4\left(\frac Xd+\rho\right).
\]

This map preserves the useful M2 sign without presenting \(\chi_4(h)\) as an arbitrary coefficient: the character is converted exactly into the difference of the \(\rho=1\) and \(\rho=3\) phases.

The derivative hypotheses also match.  The added constant \(\rho D/X\) changes no derivative, and for \(F(u)=u^{-1}\) on \([1,2]\),

\[
F'=-u^{-2},\quad F''=2u^{-3},\quad F'''=-6u^{-4},
\quad F'F'''-3(F'')^2=-6u^{-6},
\]

so all displayed Li--Yang nondegeneracy bounds hold with absolute constants.

On the block \(h\asymp L\), Vaaler's coefficient can be written as a prefactor \(L^{-1}\) times a uniformly bounded-variation function of \(h/L\):

\[
\frac{\Phi(h/(H_D+1))}{h}
=\frac1L\frac{\Phi((L/(H_D+1))(h/L))}{h/L}.
\]

Thus the project wants precisely an estimate for \(S/\mathsf H\), the normalized quantity displayed in Li--Yang's main estimate.

## Parameter-feasibility obstruction

The largest project frequency block has

\[
L\asymp H_D\asymp D X^{-1/4}.
\]

Li--Yang Case B requires, among other conditions,

\[
\mathsf H\le
\min\bigl(\mathsf M^{35/69}\mathsf T^{-2/23},
c\mathsf M^{3/2}\mathsf T^{-1/2}\bigr).
\]

Writing \(D=X^\delta\), the two required height exponents are

\[
\frac{35}{69}\delta-\frac{2}{23},
\qquad
\frac32\delta-\frac12,
\]

whereas the largest project height has exponent \(\delta-1/4\).  Domination by the first Case B height requires \(\delta\lesssim0.3306\), while domination by the second requires \(\delta\ge1/2\).  These conditions do not overlap.  Hence Case B never contains the largest M2 frequency block for any

\[
\frac14\le\delta\le\frac12.
\]

Li--Yang Case A also requires

\[
\mathsf H\le\mathsf M\mathsf T^{-49/164}.
\]

Under the exact map, its right side is \(D X^{-49/164}\), smaller than \(H_D=D X^{-1/4}\) by the fixed power

\[
X^{49/164-1/4}=X^{2/41}.
\]

Thus Case A also excludes the largest block, before its additional lower-height and auxiliary conditions are considered.

This is a theorem-applicability failure, not evidence that the Li--Yang method cannot be adapted.  Smaller \(h\)-blocks may enter the allowed ranges, but the missing top-frequency segment is a power-sized part of the project and cannot be discarded by harmonic decay: a dyadic block with \(h\asymp L\) carries coefficient size \(1/L\) across \(L\) frequencies, hence order-one \(\ell^1\) mass.

## Consequences for Round 3

1. The B1 reduced-lift route and the shifted-phase Bombieri--Iwaniec route are complementary, not interchangeable.  B1 exploits exact \(\chi_4(g)\) cancellation in the lift index; Li--Yang absorbs the M2 character into two phase shifts before spacing analysis.
2. Any Li--Yang import must be preceded by a table for \((\mathsf H,\mathsf M,\mathsf T,F,g,G)\), Case A/B inequalities, auxiliary \(N,q\) conditions, and the desired bound for \(S/\mathsf H\).
3. Existing Li--Yang bounds may be useful for lower frequency blocks, but a new endpoint-height estimate is still required for \(L\asymp D X^{-1/4}\).
4. Bourgain--Watt and small-cap decoupling estimates that are uniform over arbitrary coefficients cannot by themselves certify the sign-sensitive bridge.  The exact two-shift decomposition is the structural feature that must survive any transformation.
5. A global spacing or fourth-moment result still needs an independent pointwise or large-value bridge; Round 3 must not merge these obligations.

No numerical experiment was used.
