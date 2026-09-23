# Round 184 synthesis

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Round: 184
- Generated: 2026-08-27T22:25:38.7436539+08:00
- Starting graph:
  a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd
- Closing label: strict_hard_m1_t1_comparable_factor_sector
- Role: conductor synthesis; State Patch evidence, not self-authorizing
  state
- Numerical work: none; 100% analytical/algebraic

## Outcome

Round 184 proves a genuine actual-coefficient strict sector of the
hard-M1 \(t=1\) face.  For each squarefree product \(N=uv\), select
canonically and allocation-independently at most one close pair of
distinct odd prime factors \(p_N,q_N\) with opposite \(\chi_4\)-product.
On allocations where exactly one selected prime lies in the odd
character-bearing leg, exchanging the two primes is an integral,
fixed-point-free, multiplicity-one involution that preserves the product
and phase and reverses \(\chi_4(v)\).

The exact zero-extended pairing converts the sector to coefficient
differences.  The invariant product power, \(O(L^{-1/2})\) common-cell
smooth variation, normalized dyadic BV, and all physical boundary collars
together give

\[
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\]

The active-domain repair is essential: all BV and collar charges are made
only on the orbit-closed enlarged support box where at least one of the
two literal coefficients is nonzero.

## Exact residual

The complementary mask is

\[
 \rho_N(v)=1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
 +2\mathbf1_{p_Nq_N\mid v}
\]

for a selected pair and is \(1\) for a no-pair product.  Hence the
residual is exactly all allocations of no-pair products plus the
neither/both allocations of selected products.  No pair-density,
nonemptiness, positive-proportion, or literal lower-mass statement is
proved.

Sliding Fejer energy reduces the residual target to one exact signed
short-shift correlation of size \(L^2X^\varepsilon\) at
\(R=\lceil L\rceil\), with one real part outside the full weighted shift
sum.  That correlation remains open.  Taking absolute values shift by
shift returns the \(L^2X^\varepsilon\) scalar capacity.

## Proof status

The strict sector can be empty and does not prove the complete \(t=1\)
face.  Even a complete \(t=1\) result would leave all \(t\geq2\)
small-\(G\) incidences and the large-\(G\) near-resonant complement open.
Therefore the complete small-\(t\) owner and hard signed cone remain open.
The independent smooth M1 parent, GAR, M9-M1, all M2 parents, endpoint
uniformity, M9, both bridges, and the quarter theorem also remain open.

There is no global exponent improvement: the strongest internally proved
exponent remains \(1/3\); the accepted external benchmark remains
\(0.3144831759740614\ldots\); and the target remains \(1/4\).

## State decision

The proposed patch creates one proved subordinate strict-sector node and
updates only the open small-\(t\) owner with that dependency, the exact
residual evidence, and a narrowed next action.  It rejects the audited
coverage, transfer, correlation, parent, and exponent overclaims and
changes no complete owner, theorem, bridge, or exponent.
