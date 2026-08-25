# Round 160 strategy: M2 UNBAL inverse-selector reciprocity gate

Date: 2026-08-25

Authoritative starting graph SHA-256:
`4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

This strategy evaluates:

- `strategy/round160_m2_unbal_graph_frontier_audit.md`;
- `strategy/round160_m2_unbal_majorant_history_audit.md`;
- `strategy/round160_m2_unbal_wavelet_dispersion_audit.md`;
- the accepted Round-134, Round-135, and Round-143 graph state; and
- the Round-159 closed proof state.

It changes no mathematical status.

## 1. Selection

The generic one-sided-majorant surface is rejected as a repeat of Round
134.  The generic prescribed-centre dispersion or scalar Kuznetsov surface
is rejected as a repeat of Rounds 107, 118, 123--125, 135, and 143.  Those
rounds already prove the optimal folded-majorant mass obstruction, the
fixed-centre wave self-return, the exact centered nonzero-frequency
Kloosterman matrix, and the insufficiency of scalar fixed-index, rowwise
Parseval, full-frequency inversion, and positive complete-energy closures.

One exact interface has not been tested inside the accepted centered
matrix: additive reciprocity in the moving inverse-selector coefficient,
before a positive modulus norm.  It changes the nonsmooth dependence from
an inverse modulo (n) to a strictly shorter modulus (j\asymp K/g<n\asymp
R/g).  Round 160 freezes only that reciprocity/projective question.

This is not another transform round.  Additive reciprocity itself is
elementary and cannot be promoted.  The possible gain, or the possible new
no-go, lies in the complete price of the resulting (n\bmod j) classes,
common tests, long (h)-range, level-(4/8) spectral pieces, moving support,
and endpoint remainders.

## 2. Frozen object

Write

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor,\qquad
 D=X^\delta,\quad L=X^\ell,
\]

\[
 R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac RK=\frac DL,
\tag{160.S1}
\]

under

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\tag{160.S2}
\]

For (r=gn), (k=gj), ((j,n)=1), retain

\[
 b_{g,n}(j)=
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
\tag{160.S3}
\]

with its literal moving support, profiles, entries, exits, and zero
extension.  If (gamma_{g,n}(m)=b_{g,n}(\overline m_n)) on the supported
unit inverses and is zero otherwise, put

\[
 \widehat\gamma_{g,n}(h)=
 \frac1n\sum_{m\bmod n}\gamma_{g,n}(m)e(-hm/n).
\tag{160.S4}
\]

The accepted centered survivor is

\[
 \mathscr R^\circ_{D,L}(X)=
 \sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi_4(g)W\!\left(\frac{X}{gnD}\right)
 \sum_{1\le h<n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n),
\tag{160.S5}
\]

after the accepted (h=0) term is removed once.  Its target is

\[
 \boxed{\mathscr R^\circ_{D,L}(X)
 \ll_\varepsilon X^{1/4+\varepsilon}.}
\tag{160.S6}
\]

This is equivalent, on the frozen flat-smooth owner, to

\[
 \mathcal T_{L,K}\ll_\varepsilon(LK)^{3/4}X^\varepsilon.
\tag{160.S7}
\]

## 3. Exact new interface

For every coprime (j,n), including even (j),

\[
 e\!\left(-\frac{h\overline j_n}{n}\right)
 =e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right).
\tag{160.S8}
\]

Therefore

\[
 \widehat\gamma_{g,n}(h)=
 \frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
 e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right).
\tag{160.S9}
\]

The round must preserve every (1\le h<n), all odd (g,n), both character
directions, arbitrary ((N_0,n)), all two-adic classes, the moving
(j)-support, and every literal profile and boundary term.  Summing all
(h\bmod n) reconstructs the original reciprocal row and is a hostile
self-return control.

## 4. Power gate

Let (a=\delta-\ell\).  The accepted flat envelope has exponent

\[
 \beta(a)=\min\left(a,\frac{1-a}{2}\right)>\frac14.
\tag{160.S10}
\]

Every proposed class or projective decomposition must save at least

\[
 X^{\beta(a)-1/4}=
 \begin{cases}
 X^{a-1/4},&1/4<a\le1/3,\\
 X^{(1-2a)/4},&1/3\le a<1/2.
 \end{cases}
\tag{160.S11}
\]

At (a=1/3), the missing factor is (X^{1/12}).  A displayed shorter
modulus, a fixed-(h) estimate, or a result only after positive row norms is
not progress unless its complete restored ledger beats (160.S11).

## 5. Task decomposition

1. A statement-only rederiver verifies (160.S8)--(160.S9), every parity and
   representative convention, exact reconstruction, target normalization,
   and the first capacity seam.
2. A discovery task attacks the full signed ((g,n,j,h)) scalar.  It must
   construct and price any (n\bmod j) common-test or projective
   decomposition, test direct summation alternatives, and prove the target,
   a strict owner-complete range, or the exact capacity restoration.
3. A hostile source/power auditor tests primitive (g=1), all long
   frequencies, residue-class inflation, modulus smoothness, level-(4/8)
   pieces, endpoint remainders, and every invoked vector large-sieve or
   trace theorem.

## 6. No-repeat and scope rules

Do not reopen:

- universal Beurling--Selberg, Vaaler, or Fejér majorants;
- diagonal, lag-count, lagwise-absolute, or separate positive-row closure;
- product regrouping, functional equations, or another (h)-process plus
  (k)-Poisson return;
- direct or square-connector Bettin--Chandee/Wright;
- smooth-first or inverse-first completion as a gain by itself;
- scalar fixed-index Kuznetsov, row Parseval/SVD, point interpolation,
  complete Kloosterman second moment, or short Linnik coverage;
- summing all (h) and calling Fourier inversion a saving; or
- a theorem name without an exact source card and literal parameter map.

Nothing from this flat-smooth packet transfers automatically to sharp,
clipped, starred, transition, arithmetic-owner, balanced, hard-TOP,
endpoint-uniformity, M9, bridge, quarter-target, or exponent owners.

## 7. Exit labels

Close under exactly one label:

- `inverse_selector_reciprocity_target`;
- `strict_reciprocity_matrix_range`; or
- `inverse_selector_projective_capacity_no_go`.

If the third label occurs, park strict flat UNBAL again and rotate to a
different mandatory M2 owner.  Do not convert a scoped projective-capacity
failure into a signed lower bound or universal impossibility theorem.
