# Round 184 conductor strategy: hard-M1 t=1 comparable-factor exchange

- Round: 184
- Starting graph:
  a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd
- Selected owner:
  M9-M1-hard-top-high-radical-small-t-residual-estimate
- Frozen component: the complete literal t=1 face of the exact
  Round-183 small-gcd complement
- Planned allocation: 100% analytical/algebraic, 0% numerical theorem
  evidence
- Scheduled strategy checkpoint: Round 186, after analytic Rounds
  183--185

## 1. Conductor frontier comparison

Round 183 paid the large-gcd non-half-integer-resonant primitive-ray
incidences. Its exact complement is

\[
 \{G<\lceil L^{1/4}\rceil\}\ \dot\cup\
 \{G\geq\lceil L^{1/4}\rceil:
   \Delta_X(u,v)<(10\log(2X))^{-1}\}.
\]

The live choices are not equivalent.

1. The complete t=1 face lies in G=1 and carries the full
   coefficient-insensitive L^2 capacity against the L^(3/2) target. It is
   the first explicit failed seam of Round 183: one-prime orientation
   transfer has disjoint supports, while a comparable two-factor exchange
   is the first relation not yet tested for the hard-M1 coefficient.
2. The rest of the small-G component also carries L^2 capacity, but its
   prime-power and t>=2 geometry adds an extra interface before the t=1
   obstruction has been understood.
3. The large-G near-resonant component has only an L^(7/4) incidence
   envelope, but no uniform metric count exists for arbitrary real X and
   the G-progression is maximally coherent there. A density-only estimate
   would not supply a power saving.
4. Smooth direct M1 has comparable parent leverage but receives no new
   structure from Round 183. GAR has a much longer unresolved lower-radial
   chain. K17a and K26 affect only subordinate hard-M2 residual routes and
   their latest automatic mechanisms self-return.

The smallest fresh interface with both necessary owner content and an
untested literal sign mechanism is therefore the complete hard-M1 t=1
face. Round 184 does not claim that t=1 is the whole small-G component.

## 2. Frozen owner and target

Put e(z)=exp(2 pi i z). For each real X>=2, each literal middle or lower
hard-M1 residual shell L, and each sign sigma, let
a_(L,X)^(lit,sigma)(h,n) be the exact zero-extended coefficient from the
accepted hard transform. It retains chi_4, the dyadic cutoff, Phi, W,
normalized powers, floors, stars and half weights, strict cone and shell
edges, the hard sample, real-X crossings, endpoint values, and both sign
branches.

The complete t=1 face is

\[
 \mathcal T_{L,X,\sigma}
 =
 \sum_{\substack{u,v\geq1,\ (u,v)=1,\ v\ {\rm odd}\\
                  4u<v<16u,\ uv\ {\rm squarefree}}}
 \chi_4(v)a_{L,X}^{\rm lit,\sigma}(u,v)
 e(\sigma\sqrt{Xuv}),
\tag{184.1}
\]

where zero extension enforces h=u asymp L, every literal profile and
endpoint, and hence uv asymp L^2 and uv>L. This is exactly G=rho=t=1
inside the Round-183 complement, counted with multiplicity one.

The frozen target is

\[
 \boxed{
 |\mathcal T_{L,X,\sigma}|
 \ll_\varepsilon L^{3/2}X^\varepsilon}
\tag{184.T1}
\]

for both signs and every literal shell, with one absolute value after the
complete t=1 sum. Its coefficient-insensitive capacity is
L^2 X^epsilon, so the missing signed factor is L^(1/2).

A proof of (184.T1) pays only the t=1 face. The remaining t>=2 small-G
incidences and the large-G near-resonant component remain separate.

## 3. Fresh comparable-factor mechanism

For a supported squarefree product N=uv, fix kappa>0 and choose
canonically at most one unordered pair of distinct odd prime factors
p_(N,L,kappa), q_(N,L,kappa) satisfying

\[
 \chi_4(pq)=-1,\qquad
 \left|\log(q/p)\right|\leq\kappa L^{-1/2}.
\tag{184.2}
\]

The selector may depend on N, L, and kappa but not on the allocation
N=uv. Let the XOR incidence sector contain exactly those allocations for
which exactly one of p,q divides the character-bearing leg v.

Exchange p and q between u and v. On the two XOR orientations this is the
integral fixed-point-free involution

\[
 (u,v)\longmapsto
 \begin{cases}
  (up/q,\ vq/p),&q\mid u,\ p\mid v,\\
  (uq/p,\ vp/q),&p\mid u,\ q\mid v.
 \end{cases}
\tag{184.3}
\]

It preserves N, squarefreeness, coprimality, oddness of v, the shell and
outer phase, while

\[
 \chi_4(v')=-\chi_4(v).
\tag{184.4}
\]

After zero extension, the exact paired identity is

\[
 \sum_{\rm XOR}\chi_4(v)A_N(u,v)
 =\frac12\sum_{\rm XOR}\chi_4(v)
 \{A_N(u,v)-A_N(u',v')\}.
\tag{184.5}
\]

The intended strict-sector proof must verify, rather than assume, that the
actual hard-M1 coefficient changes by O_kappa(L^(-1/2)X^epsilon) on every
common smooth cell and that every cone, shell, profile, floor, star,
endpoint, crossing, or zero-extension mismatch lies in finitely many
O_kappa(L^(1/2)+1)-width lattice collars with total
O_kappa(L^(3/2)X^epsilon) incidence cost.

If this succeeds, the canonical XOR sector is target-safe. Its exact
residual consists of every no-pair product and the neither/both
allocations for a selected pair. No density or positive-proportion claim
is permitted.

## 4. Complete-residual continuation

The round must not stop analytically at an unquantified sparse sector
without also identifying its exact residual and testing an owner-relevant
continuation. Two continuations are allowed inside the frozen t=1 face.

1. Order the retained divisors of each N and derive the exact Abel/transport
   identity for the chi_4 partial sums and the zero-extended literal
   amplitude. Decide whether the actual coefficient, unlike an arbitrary
   bounded-variation sequence, supplies a target-sized weighted transport
   bound.
2. Extend the residual row coefficient c_N by zero and derive the exact
   sliding Fejer energy at the first diagonal-safe scale R=ceil(L). Test
   the complete one-outer-real-part shifted product correlation before
   any absolute value over shifts or divisor orientations.

The analogous hard-M2 Round-163/164 kernels are method references only.
Their coefficient, cone, parity branches, normalization, and owner are
different. No M2 theorem transfers until every hard-M1 hypothesis and
power is checked literally.

## 5. Earlier obstructions that must be bypassed

The mechanism is fresh only if it avoids all of the following proved
barriers.

- A one-prime p congruent to 3 mod 4 transfer sends the hard ratio cone to
  a disjoint support and doubles boundary capacity.
- Complete or target-truncated squarefree Mobius recombination self-returns
  to the original product wave and retains t=1.
- Positive joint-t lifting is only a permutation of product indices.
- Central-Mellin cancellation does not control noncentral modes and literal
  endpoints.
- A second bare B-process or coefficient-preserving product Poisson
  transform reconstructs the original rank-one product wave.
- Fixed-row correlation followed by triangle is stronger than the owner
  and remains unproved at t=1.
- Character erasure, dechirping, arbitrary coefficients, product triangle,
  canonical positive Gram, or an early positive norm restores L^2
  capacity.

Comparable exchange is admitted because it preserves the product and
phase while moving both divisor legs only O(L^(1/2)); it must earn its
saving from the actual profile difference before positivity.

## 6. Mandatory controls and stop rules

1. Exact t=1 incidence identity: G=rho=t=1, uv squarefree, (u,v)=1,
   v odd, and all original supports retained.
2. Both signs and every real-X crossing and endpoint.
3. Selector independence from the divisor allocation.
4. Integral, multiplicity-one, fixed-point-free exchange and exact
   chi_4 reversal.
5. Product, phase, squarefree, coprime, parity, shell, and zero-extension
   preservation.
6. Common-cell ordinary/logarithmic derivative ledger for every literal
   factor.
7. Complete crossing-collar count, including strict edges, floors, stars,
   half weights, and missing partner legs.
8. Exact residual: no pair plus neither/both, with no density inference.
9. Prime and all-1-mod-4 controls, which may have no qualifying pair.
10. One-prime toggle self-return and full-involution averaging control.
11. M2-to-M1 hypothesis and restored-power audit.
12. Complete residual transport or shifted-correlation connector, if used,
    with one outer real part and no shiftwise triangle.
13. Capacity is a method envelope, not literal lower mass.
14. No statement for t>=2, the near-resonant component, the complete
    small-t owner, a hard or smooth parent, GAR, M9-M1, any M2 owner,
    endpoint uniformity, M9, either bridge, the quarter theorem, or an
    exponent without a separate proved connector.

Stop at the first deleted literal field, allocation-dependent selector,
nonintegral exchange, double count, unpriced boundary collar, unproved
eligible-pair density, positive norm before the signed relation, or
restored power above L^(3/2)X^epsilon. A rigorous exact no-go is a
successful round result.

## 7. Orthogonal task decomposition

### Task A: literal t=1 exchange and residual attack

Prove (184.T1), prove the canonical XOR sector by (184.2)--(184.5) and
derive its exact residual, or isolate the first actual-coefficient seam.
Continue far enough to test whether the residual admits a complete
transport or signed short-shift estimate.

### Task B: cross-track transfer and capacity audit

Independently map every hypothesis and power of the accepted M2 close-pair
and residual-transport kernels to the hard-M1 coefficient. Verify the
involution, collars, residual mass, Abel identity, Fejer connector, prime
controls, and all failure modes. Produce either a sufficient literal M1
connector or the narrowest exact transfer/self-return obstruction.

### Task C: statement-only t=1 rederivation

From a self-contained finite packet, independently derive the t=1
capacity, all false controls, the canonical exchange identity and residual,
and the first missing relation. It may prove the full target, a strict
sector, or a no-go, but must quarantine the opaque literal coefficient.

## 8. Promotion and exit gates

The unique allowed terminal labels are:

- hard_m1_t1_target;
- strict_hard_m1_t1_comparable_factor_sector; or
- hard_m1_t1_exchange_transport_capacity_or_self_return_no_go.

A strict sector may create one subordinate proved node and add only
inconclusive evidence/dependency information to the open t=1/small-t
owner. A complete proof of (184.T1) still cannot promote the complete
small-t node because t>=2 and the large-G near-resonant component remain.
No State Patch is applied without independent seam reviews, exact graph
reverse/replay, and GREEN validation.

Round 185 is not designed until Round 184 closes. Round 186 is the next
mandatory full-proof strategy and current-primary-literature checkpoint
after analytic Rounds 183--185.
