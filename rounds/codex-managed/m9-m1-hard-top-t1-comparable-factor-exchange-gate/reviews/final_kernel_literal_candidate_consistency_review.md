# Round 184 final-kernel literal/candidate consistency review

- Campaign: `m9-m1-hard-top-t1-comparable-factor-exchange-gate`
- Kernel SHA-256 reviewed:
  `E5DCDDBD34B9DF5D9FBBB9723CF0D4D9909B2F713BBB49F4AA8EC40D71CA5758`
- Repaired candidate SHA-256 compared:
  `C514B10BED4C673618179C158258C362373696730C691900D250ED43E379E97F`
- Role: independent final-kernel consistency reviewer
- Evidence status: review evidence only; no kernel, candidate, or shared-state edit
- Numerical work: none

## 1. Result: GREEN

**Verdict: GREEN.**

The durable kernel is mathematically and literally consistent with the
repaired candidate at the assigned seam.  It preserves:

1. the exact hard-M1 factorization and its normalized product power;
2. the repaired, \(\tau_N\)-closed active set and its zero-extension
   semantics;
3. the aggregate discrete-BV multiplicity proof and the complete finite
   face/collar ledger;
4. both frequency signs, real-\(X\) crossings, and every literal endpoint;
5. the exact strict XOR-sector theorem; and
6. the exact residual and one-outer-real-part Fejer reduction, with its
   required correlation estimate expressly left open.

No literal coefficient field is deleted.  No existence, density,
positive-proportion, complete-\(t=1\), residual, parent, bridge, or exponent
conclusion is added.  The kernel therefore introduces no accidental
strengthening of the repaired candidate.

## 2. Exact statement and hypotheses

The kernel fixes real \(X\geq2\), one literal middle or lower residual
hard-M1 shell \(L\), \(\sigma\in\{+1,-1\}\), and fixed \(\kappa>0\), with

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor.
\]

Its coefficient \(a_{L,X}^{\mathrm{lit},\sigma}(u,v)\) is the complete
normalized stationary hard-M1 symbol, zero-extended off every original
shell, height, strict-cone, profile, floor, star, half-weight,
hard-sample, crossing, and endpoint predicate.  The complete \(t=1\)
face is exactly

\[
 \mathcal T_{L,X,\sigma}
 =\sum_{\substack{(u,v)=1,\ v\ \mathrm{odd},\ 4u<v<16u\\
                   uv\ \mathrm{squarefree}}}
 \chi_4(v)a_{L,X}^{\mathrm{lit},\sigma}(u,v)
 e(\sigma\sqrt{Xuv}).
\tag{K184.1}
\]

For each squarefree product \(N\), the selector chooses at most one
unordered pair of distinct odd prime divisors \(\{p_N,q_N\}\), as a
function only of \((N,L,\kappa)\), satisfying

\[
 \chi_4(p_Nq_N)=-1,
 \qquad |\log(q_N/p_N)|\leq\kappa L^{-1/2}.
\tag{K184.2}
\]

The proved sector consists precisely of selected-product allocations for
which exactly one selected prime divides the odd character-bearing leg
\(v\).  The theorem is

\[
 |\mathcal T^{\mathrm{cp}}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{K184.3}
\]

Equations (K184.4)--(K184.6) retain the exact complement: every
allocation of a no-pair product and the neither/both allocations of a
selected product.  At \(R=\lceil L\rceil\), (K184.7) is stated only as a
sufficient, still-open residual correlation estimate, with one real part
outside the complete weighted sum.

## 3. Proof and consistency derivation

### 3.1 Exact \(t=1\) and exchange algebra

The kernel uses the accepted coordinate identity

\[
 t=G\sqrt{uv/\operatorname{sf}(uv)}.
\]

Thus \(t=1\) is exactly \(G=1\), \((u,v)=1\), and \(uv\) squarefree,
with multiplicity one.  The exchange (K184.8) moves the two selected
primes between \(u\) and \(v\).  Squarefreeness and coprimality make the
quotients integral, and the map is a fixed-point-free,
multiplicity-one involution.  It preserves \(N=uv\), phase, parity,
squarefreeness, coprimality, and the allocation-independent selector,
while

\[
 \chi_4(v')=\chi_4(v)\chi_4(p_Nq_N)=-\chi_4(v).
\]

Consequently the zero-extended identity (K184.10), including its factor
\(1/2\), is exactly the repaired candidate's complete ambient pairing.
Physical support invariance is neither assumed nor needed.

### 3.2 Exact M1 factorization and normalization

The kernel reproduces the candidate's full moving-factor ledger:

\[
 \eta_L(u)\Phi\!\left(\frac{u}{H+1}\right)
 W\!\left(\sqrt{\frac{4q_Xu}{v}}\right)
 \left(\frac{L^2}{uv}\right)^{3/4}.
\tag{K184.11}
\]

Only allocation-independent shell and sign constants of
\(O_\varepsilon(X^\varepsilon)\), together with the fixed finite literal
masks and endpoint traces, are suppressed in this displayed ledger.
There is no lost \(H\)-, \(X\)-, \(L\)-, or ratio-dependent power.  Since
the exchange fixes \(uv=N\), the normalized factor
\((L^2/(uv))^{3/4}\) is exactly invariant.  The two genuinely moving
smooth factors have \(O_\kappa(L^{-1/2})\) changes on common cells, and
\(O(L^2)\) active pairs therefore cost
\(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).

### 3.3 Repaired active set and aggregate BV charge

The kernel retains the repair verbatim in substance:

\[
 \mathscr B_{L,X,\sigma,\kappa}
 =\{(N,u,v):(u,v)\in\mathscr A_N^\oplus,\
 a(u,v)\ne0\ \text{or}\ a(\tau_N(u,v))\ne0\}.
\tag{K184.13}
\]

The disjunction is invariant under \(\tau_N\), so \(\mathscr B\) is
orbit-closed.  Outside \(\mathscr B\), both coefficient terms in
(K184.10) vanish.  Inside it, at least one leg is in literal support,
where \(u,v\asymp L\); the close-prime hypothesis and

\[
 (u',v')=(e^{\pm\theta_N}u,e^{\mp\theta_N}v),
 \qquad |\theta_N|\leq\kappa L^{-1/2},
\]

place both legs in one fixed enlarged \(O(L)\)-by-\(O(L)\) box and give
displacement \(O_\kappa(L^{1/2}+1)\).

For a fixed discrete increment \(m\), only
\(O_\kappa(L^{1/2}+1)\) values of \(u\) can cross \(m\), and there are
\(O(L)\) possible \(v\)'s in the enlarged box.  The ordered pair fixes
\(N\), and the canonical selector supplies at most one partner.  With
the accepted normalized variation
\(\sum_m|\eta_L(m+1)-\eta_L(m)|\ll1\), this proves exactly

\[
 \sum_{\mathscr B}|\eta_L(u')-\eta_L(u)|
 \ll_\kappa L^{3/2}.
\tag{K184.14}
\]

There is no extra product-row, divisor, orientation, or selector
multiplicity.

### 3.4 Literal faces, endpoints, and final power

The kernel's collar ledger is exhaustive relative to the candidate.  It
names the strict \(4,16\) cone, frequency and height entries/exits,
profile support and plateau edges, real-\(X\) ratio crossings, and missing
partners.  It separately retains exact floor, star, tie, half-weight,
and sampled endpoint traces.  A fixed face has an
\(O_\kappa(L^{1/2}+1)\)-wide collar and therefore
\(O_\kappa(L^{3/2}+L)\) ordered pairs; an exact trace has \(O(L)\) sites.

The active-set disjunction keeps every supported-to-cemetery orbit, so
zero-extension leakage is not deleted.  Combining common-cell smooth
changes, (K184.14), and the coefficient-weighted collar bound
(K184.15) gives (K184.16), and inserting it into the exact
character-reversing identity proves (K184.3).  The conclusion is stated
uniformly for real \(X\), every literal endpoint, and both signs.  No
step converts the \(L^2\) coefficient-insensitive capacity into the
target without the audited \(L^{-1/2}\) smooth/BV/collar saving.

### 3.5 Theorem and residual scope

The residual truth table in (K184.4) is exactly \(1,0,0,1\), so
(K184.5)--(K184.6) are a disjoint identity, not an estimate.  The Abel
identity and sliding Fejer identities (K184.18)--(K184.21) retain all
literal residual coefficients and have no endpoint error.  The kernel
then explicitly says that (K184.7) is open and that shiftwise absolute
values return the \(L^2X^\varepsilon\) scalar capacity.

The theorem is consequently no stronger than the repaired candidate: it
proves only a possibly empty strict incidence sector.  Its mechanism
controls are not promoted to density, lower-mass, or impossibility
theorems.  The omission from the kernel's direct-dependency list of the
candidate's contextual
`M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector` is not a hidden
strengthening: no conclusion of that sector is invoked in (K184.1)--
(K184.21); the exact \(t=1\) coordinate identity is supplied by
`M9-M1-hard-top-squarefree-radical-sector-reduction`.  All dependencies
actually used by the durable proof are retained.

## 4. First doubtful or unproved step

No doubtful step remains in the durable proof of the strict sector
(K184.3).

The first unproved owner-relevant assertion is (K184.7), the complete
residual one-outer-real-part short-shift correlation at
\(R=\lceil L\rceil\).  It is labeled sufficient and open in both the
statement and the proof.  Nothing in the kernel estimates the no-pair or
selected neither/both residual at the target scale.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| exact artifact identity | **GREEN.** The kernel and repaired-candidate SHA-256 values equal the assigned hashes. |
| theorem parity with candidate | **GREEN.** (K184.3) is the same canonical selected-pair XOR sector and the same \(L^{3/2}X^\varepsilon\) bound. |
| no selector strengthening | **GREEN.** At most one pair is selected from \((N,L,\kappa)\); no pair existence or density is asserted. |
| exchange/multiplicity | **GREEN.** The involution is integral, fixed-point-free, multiplicity one, product preserving, and character reversing. |
| exact M1 ledger | **GREEN.** \(\eta_L\), \(\Phi\), \(W\), and \((L^2/(uv))^{3/4}\) are unchanged, with no hidden moving power. |
| repaired active set | **GREEN.** The OR-definition is \(\tau_N\)-closed; double-zero orbits vanish and one-supported/one-cemetery orbits remain. |
| BV multiplicity | **GREEN.** A fixed increment receives \(O_\kappa((L^{1/2}+1)L)\) charges, and normalized BV yields \(L^{3/2}\). |
| literal face ledger | **GREEN.** Cone, shell/height/frequency, profile, floor, star, tie, half-weight, hard-sample, real-\(X\) crossing, endpoint, and missing-partner fields are retained. |
| collar power | **GREEN.** Finite face collars cost \(O(L^{3/2})\), and exact traces cost only \(O(L)\). |
| signs and endpoints | **GREEN.** The argument is signwise and uniform for real \(X\) and all literal endpoint conventions. |
| residual identity | **GREEN.** The neither/both/no-pair complement and the one-outer-real-part Fejer energy are exact. |
| open-estimate quarantine | **GREEN.** (K184.7) is twice identified as unproved; no full residual or full \(t=1\) conclusion follows. |
| no M2 transfer | **GREEN.** M2 kernels appear only as method controls; the M1 estimate is proved from the actual M1 coefficient. |
| scope quarantine | **GREEN.** All larger M1/M2 owners, endpoints, bridges, M9, the Gauss-circle target, and exponent ledgers remain unchanged. |

No numerical experiment, symbolic computation, or external theorem was
used to certify the result.

## 6. Dependencies and exact artifacts used

This bounded verification used:

1. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`,
   SHA-256
   `E5DCDDBD34B9DF5D9FBBB9723CF0D4D9909B2F713BBB49F4AA8EC40D71CA5758`;
2. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md`,
   SHA-256
   `C514B10BED4C673618179C158258C362373696730C691900D250ED43E379E97F`;
3. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/coefficient_profile_endpoint_power_post_repair_verification.md`;
4. `protocol.md`, `state/proof_obligations.yml`, and
   `state/active_campaign.yml` for the governing proof-state and scope
   rules; and
5. the already reconciled exact factorization, endpoint, residual, and
   transport evidence named by the candidate and kernel.

The durable proof's direct mathematical dependencies are exactly the
squarefree-radical coordinate reduction, the M1 endpoint transform, the
M1 frequency/phase diagram, uniform \(C^1\) control of \(\Phi\), the
accepted normalized dyadic-weight BV fact, and the elementary divisor
bound.  M2 close-pair and residual kernels are controls only.  No artifact
other than this assigned review was edited.

## 7. Recommended state effect

**GREEN: accept the durable kernel as faithful to the repaired
candidate.**  No kernel repair is required at the literal
coefficient/profile/endpoint/power seam.

The maximum supported state effect is promotion of the exact,
possibly empty, strict hard-M1 \(t=1\) canonical comparable-prime XOR
incidence sector and its exact residual/Fejer reduction.  Keep (K184.7),
the complete residual, the complete \(t=1\) face, all \(t\geq2\) small-\(G\)
incidences, the large-\(G\) near-resonant complement, the complete
small-\(t\) owner, both M1 parents, every M2 owner, endpoint uniformity,
M9, both bridges, the Gauss-circle target, and every exponent unchanged.
