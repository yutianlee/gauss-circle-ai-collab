# Hostile Round-173 selection audit

- Starting graph SHA-256:
  70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f
- Role: independent hostile frontier selector
- Resource recommendation: 100% analytic/algebraic; 0% numerical
- State effect: none

## 1. Result and selection

**Select one final K26 identity-or-no-go round, but do not repeat the
Round-172 positive common-frequency experiment.** Freeze instead the exact
**tangent-character / Fejer-bandpass commutator** below. It is the smallest
current gate which

1. acts on the complete literal coefficient before every positive norm;
2. has an explicit finite operator and multiplicity-one domain;
3. uses the actual character law rather than a coefficient-uniform norm;
4. produces the missing factor \(L\) on one exact commutator term; and
5. leaves one named, owner-complete actual-symbol difference remainder whose
   target bound or self-return can be decided in one round.

This selection is hostile. The alternating-difference identity is a
tautology for arbitrary finite sequences and is not itself a saving. If the
surviving literal difference retains \(L^4X^\varepsilon\) capacity after all
selectors and no-pair rows are restored, Round 173 should close with a
scoped no-go. It must not rename that remainder as a theorem.

BAL, UNBAL, the Round-169 collar, K17a, and M1 are deferred. Each presently
requires either a theorem with no exact new operator, an owner-incomplete
sector, or a return to a parked transform. The mandatory full-proof and
current-literature review after Round 173 is the proper place to rotate
owners again.

## 2. Exact literal operator and frozen gate

Let \(R<T\le 2R\) be one Round-172 stopped-chain link. Extend its one-sided
Fejer-difference coefficient by zero:

\[
 \beta_{R,T}(r)=
 \begin{cases}
  r(T-R)/(RT),&0<r<R,\\
  1-r/T,&R\le r<T,\\
  0,&r\le0\text{ or }r\ge T.
 \end{cases}
\tag{173.1}
\]

It is continuous at every break point and \(O(R^{-1})\)-Lipschitz. Open both
literal residual coefficients with multiplicity one,

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi_4(d)\lambda_N(d),
\tag{173.2}
\]

where every selected/no-pair value, squarefree and coprimality mask,
two-adic branch, profile, floor, star, crossing, hard endpoint, point value,
and zero-extension value remains in \(\lambda_N(d)\).

For one opened pair write

\[
 N=dm,\qquad d'=d+2s,\qquad m'=m+v,\qquad
 N_s'=(d+2s)(m+v),
\tag{173.3}
\]

and

\[
 r_s=N_s'-N=dv+2s(m+v).
\tag{173.4}
\]

On the even-shift aggregate \(v\) is even. Define on the full integer
\(s\)-line

\[
 G_{d,m,v}(s)=
 \begin{cases}
 \lambda_{N_s'}(d+2s)\overline{\lambda_{dm}(d)}
 e\!\left(J(\sqrt{N_s'}-\sqrt{dm})\right),
 &\text{if both opened atoms are on positive literal support},\\
 0,&\text{otherwise}.
 \end{cases}
\tag{173.5}
\]

This piecewise convention never evaluates a square root off positive
support. The chart
\((N,d;N',d')\leftrightarrow(d,m,v,s)\) is multiplicity one, and

\[
 \chi_4(d+2s)\chi_4(d)=(-1)^s.
\tag{173.6}
\]

Consequently the complete physical link is

\[
 \Delta_{R,T}
 =2\Re\!\sum_{\substack{d\ {\rm odd},\ m\ge1\\
                         v\in2\mathbb Z,\ s\in\mathbb Z}}
 (-1)^s\beta_{R,T}(r_s)G_{d,m,v}(s).
\tag{173.7}
\]

For every finitely supported sequence \(H\),

\[
 2\sum_s(-1)^sH(s)
 =\sum_s(-1)^s\{H(s)-H(s+1)\}.
\tag{173.8}
\]

Apply (173.8) only after the complete link has been formed. With
\(D_sG(s)=G(s)-G(s+1)\), one obtains

\[
 \boxed{
 \begin{aligned}
 \Delta_{R,T}&=\mathcal C_{R,T}+\mathcal R_{R,T},\\
 \mathcal C_{R,T}
 &=\Re\sum(-1)^s
   \{\beta_{R,T}(r_s)-\beta_{R,T}(r_{s+1})\}G(s),\\
 \mathcal R_{R,T}
 &=\Re\sum(-1)^s\beta_{R,T}(r_{s+1})D_sG(s).
 \end{aligned}}
\tag{173.9}
\]

Every sum in (173.9) is over the complete domain in (173.7). Boundary,
birth, death, selector, squarefree, parity, and endpoint jumps are inside
\(D_sG\); none is discarded as an error.

Let \(R_{j+1}=\min(2R_j,M)\), \(R_0=\lceil L\rceil\), with repetitions
removed. The sole Round-173 analytic gate should be

\[
 \boxed{
 \sum_j\mathcal R_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon .}
\tag{173.10}
\]

There is one outer real part and no modulus on an individual link,
\(s\)-fibre, physical shift, divisor row, selector class, or transformed
mode. Cross-link cancellation remains licensed. An absolute bound for the
complete sum is sufficient but stronger than necessary.

Round 173 must prove (173.10), isolate an owner-complete target-safe
complement, or prove the first exact no-go for this displayed operator.
Merely rewriting \(D_sG\), invoking an unnamed correlation theorem, or
taking its positive norm does not pass the gate.

## 3. Derivation and power ledger

The restored ledger is:

| object | available size | target/status |
|---|---:|---|
| coefficient energy \(D_L\) | \(L^2X^\varepsilon\) | proved |
| maximal positive link | \(RD_L\), up to \(L^4X^\varepsilon\) | misses by \(L\) |
| short correction and first link | \(L^3X^\varepsilon\) | already paid |
| collectively recombined ordinary-zero sector | \(L^3X^\varepsilon\) | already paid |
| commutator \(\mathcal C_{R,T}\) | \(L^3X^\varepsilon\) | target-safe |
| difference remainder \(\mathcal R_{R,T}\) | up to \(L^4X^\varepsilon\) by triangle | open |

On literal support,

\[
 r_{s+1}-r_s=2(m+v)=2m'\asymp L,
\]

so

\[
 |\beta_{R,T}(r_{s+1})-\beta_{R,T}(r_s)|
 \ll \frac{L}{R}.
\tag{173.11}
\]

The complete opened absolute incidence mass for a link is
\(O_\varepsilon(RL^2X^\varepsilon)\): there are \(O(R)\) product gaps,
\(O(L^2)\) product sites, and only divisor-power multiplicity. Therefore

\[
 |\mathcal C_{R,T}|
 \ll_\varepsilon \frac{L}{R}\,RL^2X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\tag{173.12}
\]

The \(O(\log L)\) links are absorbed into \(X^\varepsilon\). This is the
nonformal reason to test (173.9): moving \(s\) by one moves the product gap
by \(\asymp L\), whereas the top bandpass varies on scale \(R\). At
\(R\asymp L^2\), the commutator supplies exactly the missing factor \(L\).

No gain is automatic for \(\mathcal R_{R,T}\). Taking
\(|D_sG|\le |G(s)|+|G(s+1)|\) restores \(RL^2\), hence \(L^4\) at the top
scale. Thus (173.10) needs signed actual-symbol recombination, or the route
must close.

## 4. Bypass of prior no-gos

The bypass is narrow and explicit.

1. **Round 164 transport.** Round 164 paired divisors inside one fixed
   product and then used positive BV/transport. Here the second divisor
   varies across different products and Fejer shifts after the full link is
   assembled. No per-product modulus or BV norm is taken. In particular, a
   fixed-product fibre antisymmetrizer with a large multiplicative toggle is
   not selected: its cells can be disjoint, its off-support leakage has no
   small multiplier, and its positive no-pair complement is owner-incomplete.
2. **Round 165 rowwise differencing.** On a fixed even-shift cofactor row the
   character is frozen. Here \(r_s\) moves with \(s\) inside the dyadic
   bandpass, and (173.6) is the exact alternating direction.
3. **Round 167 fixed-shift routes.** The operator acts across shifts before a
   fixed-\(r\) triangle, so it does not sum theorem errors shiftwise.
4. **Rounds 162, 169, and 172 positive transforms.** The difference is formed
   in physical incidence variables before Poisson, product-cell opening, or
   a positive dual norm. A later transform is allowed only on the complete
   signed remainder.
5. **Round 171 commutators.** That BAL placement required a second,
   uncharactered difference and incurred a length-\(L\) ramp. The present
   gate uses one bounded alternating primitive and an existing bandpass
   slope. No BAL statement transfers.

These distinctions prove no estimate. Equation (173.8) can still become a
shift tautology, and \(D_sG\) can still carry full capacity. That possible
self-return is the falsifiable outcome.

## 5. First doubtful step and hostile stop conditions

The first unproved step is (173.10). The difference \(D_sG\) changes the
second product by \(2m'\asymp L\), its selector, squarefree/coprimality
membership, profiles, hard faces, and phase. Its phase ratio contains

\[
 J\{\sqrt{N_s'+2m'}-\sqrt{N_s'}\},
\tag{173.13}
\]

which has no proved uniform smallness modulo one. Selector and no-pair
supports can jump by order one. Neither smooth variation nor the real size
of (173.13) gives a pointwise \(L^{-1}\) bound.

Stop with a scoped no-go at the first of:

1. a multiplicity, parity, or zero-extension failure;
2. failure of the commutator estimate (173.11)--(173.12);
3. an \(L^4X^\varepsilon\) no-pair or support-jump survivor;
4. normalization which cancels the multiplier and returns the original
   scalar;
5. a modulus before the complete \(j,d,m,v,s\) assembly;
6. return to the Round-162/169 collar or Round-172 positive dual capacity;
7. control of only one selector class, endpoint regime, parity peak, or
   other owner-incomplete sector.

No pivot is allowed inside Round 173.

## 6. Required controls and outcomes

1. **Finite alternating identity.** Check (173.8) on intervals, singletons,
   and nonzero endpoint data. All endpoint terms must lie in zero-extended
   \(D_sG\).
2. **Multiplicity and parity.** Reconstruct
   \((N,d;N',d')\) from \((d,m,v,s)\), including negative \(s,v\), both
   two-adic branches, and \(v\equiv r\pmod2\). Every even-gap atom must occur
   once.
3. **Bandpass slope.** Check both linear pieces, \(r=0\), the cusp \(r=R\),
   \(r=T\), and the final non-doubling link. Equation (173.11) must have no
   hidden jump.
4. **Constant-\(G\) control.** On an interval where \(G\) is constant, the
   remainder vanishes and only the target-safe commutator remains.
5. **Phase-adapted adversary.** An abstract array with
   \(G(s)=(-1)^s\) has positive alternating mass and a full-capacity
   remainder. Every claimed estimate must fail for this erased-structure
   array.
6. **Positive no-pair control.** If all odd prime factors are
   \(1\pmod4\), active pairs can force \(s\) even. The apparent alternating
   sign is then constant on literal support and \(D_sG\) records jumps through
   missing odd sites. This family must remain inside (173.10).
7. **Phase-increment control.** Large real size in (173.13) is not distance
   from an integer.
8. **One-real-part and cross-link control.** Compare the exact sum of
   (173.9) over the stopped chain with (172.K5). Pay the short correction
   once and insert no linkwise modulus.
9. **Owner scope.** Even success closes only K26 and the residual scalar
   through the accepted connector.

All controls are analytic. Computation may check finite reindexing but cannot
certify (173.10).

## 7. Owner scope, alternatives, dependencies, and recommendation

The gate is owner-complete for each physical link because (173.7) retains
selected and no-pair rows, monotone and opposing displacements, both parity
branches, every gcd size, profiles, hard faces, and endpoints. No first-link,
zero-mode, selected-row, or nonexceptional-row sector is promoted separately.

If (173.10) is proved, (173.9), (173.12), and the accepted stopped-chain
identity prove K26 up to the paid short correction. This closes only the
residual \(t=1\) scalar. Other \(t=1\) and few-point hard-TOP channels, full
hard TOP, critical and remaining-label BAL, UNBAL, M9--M2, both direct M1
parents or GAR, endpoint uniformity, M9, both bridges, and the quarter
theorem remain open. No exponent changes locally.

Alternative rulings:

- **Critical BAL: defer.** No complete nonlocal operator controls the
  surviving \((++)\) complement, fixed-\(Q\) rulings, ramp faces, aliases,
  gcd holes, and endpoints.
- **Remaining-label BAL: defer.** It is a heterogeneous universal owner; a
  strict exact-square or noncritical sector is owner-incomplete without a
  target-safe complement.
- **UNBAL: defer.** The next need is a new signed literal-matrix vector
  theorem, not a narrower exact operator.
- **Round-169 nonzero collar: defer.** Its aggregate is exact, but a bespoke
  signed theorem rather than a new operation is missing.
- **K17a: defer.** The determinant dictionary, fixed-polylog sector,
  fixed-shift triangle, and audited direct placements are parked.
- **M1/GAR: defer.** The D=1 variable-mask wave is exact, but the obvious
  Fourier, Abel, reciprocal, and positive matrix placements have returned
  to known barriers.

**Final recommendation: SELECT** the K26 tangent-character /
Fejer-bandpass commutator gate (173.9)--(173.10), with target or exact scoped
no-go as its only mathematical exits. **DEFER** every other owner to the
mandatory post-173 strategy and literature review.

Accepted artifacts used:

- protocol.md;
- state/proof_obligations.yml at the stated graph hash;
- state/failure_ledger.md;
- rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reviews/conductor_round170_adjudication.md;
- rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/synthesis.md;
- proofs/kernels/m9_m2_balanced_two_defect_commutator_ramp_obstruction.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/synthesis.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md; and
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md.

No candidate report or computation is treated as accepted mathematics.
