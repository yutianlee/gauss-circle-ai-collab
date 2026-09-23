# Round 184 final-kernel power, residual, owner, and scope review

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Task: round184_residual_owner_scope_review, bounded final-kernel pass
- Role: independent final-kernel seam reviewer
- Starting graph SHA-256:
  a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd
- Kernel SHA-256 audited:
  E5DCDDBD34B9DF5D9FBBB9723CF0D4D9909B2F713BBB49F4AA8EC40D71CA5758
- Repaired source-candidate SHA-256 audited:
  C514B10BED4C673618179C158258C362373696730C691900D250ED43E379E97F
- Allocation: 100% analytical/algebraic, 0% numerical

## 1. Result

**GREEN.**

Equations (K184.4)--(K184.21) preserve the repaired candidate's exact
residual partition, ambient sign-mass warning, ordered-divisor Abel
connector, sliding Fejer normalization, phase, endpoints, Cauchy
prefactor, and restored powers.  Equation (K184.7) retains one outer real
part and is explicitly marked open.  At \(R=\lceil L\rceil\), its
\(L^2X^\varepsilon\) right side combines with the
\(O(L)\) Cauchy prefactor to give the target square
\(L^3X^\varepsilon\); shiftwise moduli instead give energy
\(L^3X^\varepsilon\) and only the scalar capacity
\(L^2X^\varepsilon\).

The Section-3 active-domain repair in (K184.13) restricts only the
coefficient-difference estimate to exchange orbits on which at least one
literal coefficient is nonzero.  It neither changes the ambient exchange
identity nor removes, adds, or reweights any residual allocation.
Accordingly it has no effect on (K184.4)--(K184.7) or
(K184.17)--(K184.21).

The proved theorem remains only the possibly empty strict XOR incidence
sector (K184.3).  It proves neither selector nonemptiness nor the complete
\(t=1\) face and licenses no downstream or exponent promotion.

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), one literal middle or lower hard-M1 residual shell
\(L\), \(\sigma\in\{\pm1\}\), and \(\kappa>0\).  The literal coefficient
is extended by zero off all original support, profile, floor, star,
half-weight, hard-sample, crossing, and endpoint predicates.  For each
squarefree product \(N\), select at most one pair of distinct odd prime
divisors \(\{p_N,q_N\}\), canonically from \((N,L,\kappa)\), with

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\le\kappa L^{-1/2}.
\]

The residual mask is exactly

\[
 \rho_N(v)=
 \begin{cases}
  1,&\text{if no pair is selected},\\
  1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
    +2\mathbf1_{p_Nq_N\mid v},&\text{if a pair is selected}.
 \end{cases}
\]

Thus its selected-bit truth table is \(1,0,0,1\) on
\(00,10,01,11\), and the exact residual coefficient is

\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{v\mid N,\ v\ {\rm odd}}
 \chi_4(v)\rho_N(v)
 a_{L,X}^{\mathrm{lit},\sigma}(N/v,v).
\]

It contains all allocations of every no-pair product and exactly the
neither/both allocations of every selected product.  No existence,
density, positive-proportion, or literal lower-mass hypothesis is used.

For the Fejer connector, extend
\(z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN})\) by zero outside a
containing interval of \(M_L\asymp L^2\) integer product sites.  The
coefficient bound and divisor estimate give

\[
 \sum_N|c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

No signed shift theorem is among the dependencies.  The only such
statement displayed in the kernel is the open sufficient relation
(K184.7).

## 3. Proof or derivation

The truth table of (K184.4) vanishes exactly on XOR and is one exactly
on neither/both.  Together with the convention \(\rho_N=1\) for a
no-pair product, this proves the disjoint identity

\[
 \mathcal T_{L,X,\sigma}
 =\mathcal T^{\rm cp}_{L,X,\sigma}
  +\sum_Nc_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}).
\]

If \(M_N\) is the odd part of \(N\), summing the residual signs over the
full divisor cube gives

\[
 \sum_{v\mid M_N}\chi_4(v)\rho_N(v)
 =
 \begin{cases}
  \prod_{r\mid M_N}(1+\chi_4(r)),&\text{no pair},\\
  (1+\chi_4(p_Nq_N))
  \prod_{r\mid M_N/(p_Nq_N)}(1+\chi_4(r))=0,
  &\text{selected pair}.
 \end{cases}
\]

This verifies (K184.17).  Its second line is only ambient balance:
physical profiling and the one-sided cone need not preserve the paired
divisors.

For fixed \(N\), order retained residual odd divisors \(v_1<\cdots<v_s\),
put \(\epsilon_i=\chi_4(v_i)\),
\(C_j=\sum_{i\le j}\epsilon_i\), \(C_0=0\), and include the residual
mask in \(a_i\).  With \(a_0=a_{s+1}=0\), exact Abel summation is

\[
 \sum_{i=1}^s\epsilon_i a_i
 =-\sum_{j=0}^sC_j(a_{j+1}-a_j).
\]

The increments telescope to zero.  Subtracting the midpoint of the
range of \(C_j\) and taking triangle gives precisely

\[
 \left|\sum_i\chi_4(v_i)a_i\right|
 \le {1\over2}\operatorname{osc}(C_N)
       \sum_j|a_{j+1}-a_j|.
\]

This is (K184.18).  No target-sized weighted average of the partial-sum
oscillation is proved, so positive productwise closure remains at
\(L^2X^\varepsilon\).

Expanding the normalized energy

\[
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
\]

counts every diagonal term in \(R\) windows and every pair at positive
gap \(r<R\) in \(R-r\) windows.  Full-line zero extension removes all
endpoint errors.  Since

\[
 \sqrt{N+r}-\sqrt N
 ={r\over\sqrt{N+r}+\sqrt N},
\]

the exact expansion is (K184.20), including its coefficient
\(1-r/R\), its phase, its factor \(2\), and one real part outside the
complete weighted shift aggregate.

Let \(W_s=\sum_{j<R}z_{s+j}\).  Then
\(\sum_sW_s=R\sum_Nz_N\), and at most \(M_L+R-1\) windows meet the
containing interval.  Hence

\[
 R^2\left|\sum_Nz_N\right|^2
 \le (M_L+R-1)\sum_s|W_s|^2,
\]

which, after using
\(\sum_s|W_s|^2=R\mathfrak E_{R,\sigma}^{\rm rem}\), gives exactly
(K184.21):

\[
 |\mathcal T^{\rm rem}_{L,X,\sigma}|^2
 \le {M_L+R-1\over R}\mathfrak E_{R,\sigma}^{\rm rem}.
\]

At \(R=\lceil L\rceil\), the prefactor is \(O(L)\).  The diagonal is
\(O_\varepsilon(L^2X^\varepsilon)\), and the one-sided upper bound
(K184.7) gives the same size for the aggregate off-diagonal term.
Therefore the energy is target-square safe and the residual scalar is
\(O_\varepsilon(L^{3/2}X^\varepsilon)\), conditionally on (K184.7).

If instead each shifted inner product is replaced by its modulus,
Cauchy bounds it by the diagonal.  Summing \(R\asymp L\) shifts gives
\(\mathfrak E_R\ll_\varepsilon L^3X^\varepsilon\).  Multiplication by
the outer \(O(L)\) prefactor yields an \(L^4X^\varepsilon\) square and
only the \(L^2X^\varepsilon\) scalar capacity.  All restored powers in
the kernel are therefore correct.

Finally, (K184.13) is \(\tau_N\)-closed and contains exactly the exchange
orbits for which the difference in (K184.10) may be nonzero.  Outside it
both coefficient values vanish.  Restricting the variation and collar
estimates to this set repairs the Section-3 domain count without changing
(K184.10).  Since the residual is defined by the allocation truth table,
not by \(\mathscr B_{L,X,\sigma,\kappa}\), this repair cannot alter any
residual or Fejer formula.

## 4. First doubtful or unproved step

The first unproved residual analytic step remains exactly (K184.7):

\[
 \Re\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad R=\lceil L\rceil.
\]

Neither ordered-divisor Abel summation, ambient selected-pair balance,
the strict XOR theorem, M2 method controls, nor shiftwise positivity
proves this actual-direction signed correlation.  The kernel correctly
states that (K184.7) is open and does not claim the complete residual or
complete \(t=1\) target.

One wording in the prior GREEN review is corrected here for exact state
hygiene: its combined phrase that
M9-M1-physical-one-count-assembly and M9-M1 were
“unchanged/open” was imprecise.  The authoritative graph has
M9-M1-physical-one-count-assembly as proved_internal (a conditional
assembly lemma with open dependencies), while M9-M1 is open.  This
wording issue is not present in the kernel and does not alter the prior
mathematical seam verdict.

## 5. Required control tests and outcomes

- **One-prime toggle: PASS as a no-go.** Moving an odd prime between
  legs multiplies \(v/u\in(4,16)\) by \(p^{\pm2}\); for \(p\ge3\) the
  image leaves the cone.  The two physical supports are disjoint.

- **Normalized involution average: PASS as self-return.** Averaging exact
  full divisor-lattice reindexings remains an exact rewriting unless an
  independent contraction or coverage estimate is supplied.

- **All-\(1\bmod4\) products: PASS.** No selected pair can have
  \(\chi_4(pq)=-1\), and every odd divisor has positive character.  This
  blocks fixed-product character reversal but proves neither density nor
  literal lower mass.

- **Semiprime: PASS.** An odd supported semiprime has prime-leg ratio
  greater than four and therefore cannot satisfy the close-pair
  condition when \(\kappa L^{-1/2}<\log4\).  An even semiprime has fewer
  than two odd primes and is likewise ineligible.  No occurrence count
  is asserted.

- **Ordered Abel: PASS algebraically, OPEN analytically.** It introduces
  the uncontrolled weighted partial-sum oscillation and no small
  consecutive-divisor-gap theorem.

- **Fejer connector: PASS algebraically, OPEN analytically.** The
  normalization, endpoints, phase, one real part, diagonal, and Cauchy
  prefactor are exact.  Equation (K184.7) remains open.

- **False unsigned/adversarial analogue: PASS.** The strict sector earns
  its saving only after the exact \(\chi_4\)-reversing exchange turns an
  orbit into a coefficient difference.  Erasing the character produces
  a sum instead of a difference, while dechirped all-\(1\bmod4\) residual
  products can reinforce.  The kernel does not claim either false
  analogue.

- **Nonemptiness and full-face scope: PASS.** The selector may choose
  nothing on every supported product.  The no-pair plus neither/both
  residual remains exact and open, so (K184.3) proves neither sector
  nonemptiness nor the full \(t=1\) estimate.

## 6. Dependencies and exact artifacts used

The kernel's direct accepted dependencies are exact and sufficient:

1. M9-M1-hard-top-squarefree-radical-sector-reduction;
2. M9-M1-top-endpoint-transform;
3. M9-M1-frequency-phase-diagram-R10;
4. H4-Phi-regularity;
5. M9-M2-dyadic-weight-nondegeneracy; and
6. Divisor-bound-elementary.

The squarefree-radical reduction already contains the exact
multiplicity-preserving \(t=1\) coprime-squarefree cone, so the separate
Round-183 nonresonant primitive-ray sector need not be a direct
dependency of this kernel.  The M2 close-pair and residual Fejer kernels
are correctly retained as method controls only, not theorem
dependencies.

The exact artifacts used in this final review were:

1. protocol.md;
2. state/proof_obligations.yml, restricted to the named owners,
   downstream graph, dependencies, and exponent nodes;
3. proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md;
4. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md; and
5. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/residual_transport_correlation_owner_scope_review.md.

No external source, numerical experiment, candidate edit, kernel edit,
or shared-state edit was used.

## 7. Recommended state effect

The kernel is suitable for promotion as one new subordinate
proved_internal strict-sector node, subject to the conductor's
mechanically valid State Patch and remaining validation gates.  The new
node must have no implication edge to a complete owner.  The exact
residual and Fejer identities may be retained as algebraic
infrastructure, with (K184.7) explicitly open.

Leave the authoritative graph scopes unchanged as follows:

- M9-M1-hard-top-high-radical-small-t-residual-estimate remains open;
- M9-M1-top-endpoint-signed-cone remains open;
- M9-M1-direct-smooth-residual-blockwise-estimate remains open;
- M9-M1-physical-one-count-assembly remains proved_internal with its
  open dependencies, and M9-M1 remains open;
- M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector and
  M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction remain their
  already proved, separately scoped statements;
- all \(t\ge2\) small-\(G\) incidences and the large-\(G\)
  near-resonant complement remain open;
- every M2 owner, including the M2 close-pair and residual-Fejer nodes,
  remains unchanged, and M9-M2 remains open;
- M9-endpoint-uniformity and M9 remain open;
- Conditional-bridge and GC-global-M1-alternative-bridge remain
  derived_under_assumptions;
- GC-target remains open at exponent \(1/4\);
- GC-partial-one-third remains proved_internal at exponent \(1/3\); and
- GC-external-Li-Yang-theta-star remains proved_external_dependency at
  exponent \(0.3144831759740614\ldots\).

Thus the kernel changes no complete owner, bridge, theorem, or certified
exponent, and the Section-3 domain repair has no residual or downstream
scope effect.
