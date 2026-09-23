# Round 184 residual transport, correlation, owner, and scope review

- Campaign: `m9-m1-hard-top-t1-comparable-factor-exchange-gate`
- Task: `round184_residual_owner_scope_review`
- Role: independent seam reviewer
- Starting graph SHA-256:
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`
- Candidate SHA-256 audited:
  `609EB3BFA2EEE1566D913F63CBF4997E48AC7A7D6FD927213529C01528B8FC6E`
- Note: the brief's earlier expected hash
  `A59E49252026A88F589DEDFDAABA2039B7626C7BC645A7D8D55B0F60FA865947`
  was superseded by the conductor's announced repair of one corrupted
  `\rm` control byte in (184.C14); the current hash was independently
  reproduced before review.
- Allocation: 100% analytical/algebraic, 0% numerical

## 1. Result

**GREEN** for the residual-transport/correlation and owner/exponent
scope seams.

The Boolean mask (184.C17), the ordered-divisor Abel inequality
(184.C21), the normalized sliding Fejer identity (184.C22)--(184.C23),
the endpoint-free Cauchy connector (184.C24), and the one-outer-real-part
sufficient condition (184.C25) are exact.  At
\(R=\lceil L\rceil\), the diagonal and Cauchy prefactor restore exactly
to the target square \(L^3X^\varepsilon\).  Taking moduli shift by shift
instead restores only the scalar capacity \(L^2X^\varepsilon\).

The stated controls correctly show that fixed-product local exchange does
not cover the residual.  They do not prove residual mass, do not disprove
the literal sum, and do not imply nonemptiness of the selected sector.
The only positive candidate is the possibly empty strict XOR incidence
sector (184.C16); it is not the complete \(t=1\) face.  No complete
small-\(t\) owner, parent, bridge, theorem, or exponent is discharged.

## 2. Exact statement and hypotheses

Fix one literal hard-M1 shell \(L\), real \(X\ge2\), and
\(\sigma\in\{\pm1\}\).  For squarefree \(N\), let the canonical selected
pair, when it exists, be \(\{p_N,q_N\}\), depending only on
\((N,L,\kappa)\), with

\[
 \chi_4(p_Nq_N)=-1,
 \qquad |\log(q_N/p_N)|\le \kappa L^{-1/2}.
\]

With the literal coefficient zero-extended off every physical predicate,
the exact residual coefficient is

\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{v\mid N,\ v\ {\rm odd}}
 \chi_4(v)\rho_N(v)
 a_{L,X}^{\mathrm{lit},\sigma}(N/v,v),
\]

where \(\rho_N(v)=1\) if there is no selected pair and otherwise

\[
 \rho_N(v)=1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
               +2\mathbf1_{p_Nq_N\mid v}.
\]

Thus \(\rho_N\) has truth table \((1,0,0,1)\) on the selected-prime bits
\((00,10,01,11)\).  It leaves precisely every no-pair allocation and the
neither/both allocations of a selected product.  This is an exact
partition; it assumes no pair existence, density, or positive
proportion.

The transport statements require only the accepted literal support
\(N\) in a containing interval of cardinality \(M_L\asymp L^2\), the
normalized coefficient bound and divisor estimate

\[
 |c_{N,\sigma}^{\rm rem}|\ll_\varepsilon
 \tau(N)X^\varepsilon,
\]

and full-line zero extension.  The Abel statement additionally orders
the retained residual odd divisors of one fixed \(N\) and includes both
zero endpoints.  No positivity, small consecutive-divisor gap, or
character-partial-sum theorem is assumed.

## 3. Proof or derivation

For fixed \(N\), order the residual odd character legs
\(v_1<\cdots<v_s\), put \(\epsilon_j=\chi_4(v_j)\),
\(C_j=\sum_{i\le j}\epsilon_i\), \(C_0=0\), and absorb the residual mask
into \(a_j\).  With \(a_0=a_{s+1}=0\), exact summation by parts is

\[
 \sum_{j=1}^s\epsilon_ja_j
 =-\sum_{j=0}^s C_j(a_{j+1}-a_j).
\]

Because \(\sum_{j=0}^s(a_{j+1}-a_j)=0\), one may subtract from every
\(C_j\) the midpoint of its range.  Triangle then gives

\[
 \left|\sum_{j=1}^s\epsilon_ja_j\right|
 \le {1\over2}\operatorname{osc}(C_N)
       \sum_{j=0}^s|a_{j+1}-a_j|,
\]

which is exactly (184.C21).  Bounded amplitude variation and the divisor
bound do not control the weighted average of
\(\operatorname{osc}(C_N)\); after a positive sum over \(O(L^2)\)
product rows they give only \(L^2X^\varepsilon\).

Now set

\[
 z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN})
\]

and extend \(z_N\) by zero on the full line.  Expanding

\[
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
\]

counts every diagonal term in exactly \(R\) windows and a pair at gap
\(r<R\) in exactly \(R-r\) windows.  Therefore, with no endpoint term,

\[
\begin{aligned}
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={}&\sum_N|c_{N,\sigma}^{\rm rem}|^2\\
 &+2\Re\sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N+r}+\sqrt N}\right).
\end{aligned}
\]

The phase is exact because
\(\sqrt{N+r}-\sqrt N=r/(\sqrt{N+r}+\sqrt N)\).  This verifies the
normalization, endpoints, phase, and the single real part in
(184.C22)--(184.C23).

If \(W_s=\sum_{j<R}z_{s+j}\), then
\(\sum_sW_s=R\sum_Nz_N\), while at most \(M_L+R-1\) windows meet the
containing interval.  Cauchy gives

\[
 R^2\left|\sum_Nz_N\right|^2
 \le (M_L+R-1)\sum_s|W_s|^2,
\]

and hence exactly

\[
 \left|\mathcal T_{L,X,\sigma}^{\rm rem}\right|^2
 \le {M_L+R-1\over R}\mathfrak E_{R,\sigma}^{\rm rem}.
\]

Furthermore,

\[
 D_{L,\sigma}:=\sum_N|c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

At \(R=\lceil L\rceil\), the Cauchy prefactor is \(O(L)\), so the
diagonal contributes \(O(L^3X^\varepsilon)\) to the target square.
Consequently the one-sided aggregate bound (184.C25), with one real part
outside the entire weighted shift sum, is sufficient for

\[
 |\mathcal T_{L,X,\sigma}^{\rm rem}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

By contrast, Cauchy on each shift gives modulus at most
\(D_{L,\sigma}\).  Summing \(R\asymp L\) such moduli yields
\(\mathfrak E_R\ll L^3X^\varepsilon\); the outer prefactor then gives
only \(|\mathcal T^{\rm rem}|\ll L^2X^\varepsilon\).  This verifies the
claimed shiftwise-triangle capacity and the missing scalar factor
\(L^{1/2}\).

## 4. First doubtful or unproved step

The first missing analytic relation is exactly (184.C25):

\[
 \Re\sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad R=\lceil L\rceil.
\]

Neither the strict XOR theorem, ordered-divisor Abel summation, the
accepted M2 transport kernel, nor a positive shift estimate proves this
actual-direction signed correlation.  The candidate marks it unproved
and draws no residual conclusion from it.  There is no earlier defect in
(184.C17)--(184.C24) on the assigned seam.

## 5. Required control tests and outcomes

- **One-prime toggle: PASS as a no-go.** Moving an odd prime between the
  legs multiplies \(v/u\in(4,16)\) by \(p^{\pm2}\).  Since \(p\ge3\),
  the image is outside the cone in either orientation.  Its physical
  support is disjoint, so it supplies no local contraction.

- **Semiprime: PASS.** For an odd supported semiprime, its two legs are
  its two primes and their ratio exceeds four.  Hence their logarithmic
  gap exceeds \(\log4\), excluding (184.C3) once
  \(\kappa L^{-1/2}<\log4\).  If \(2\mid N\), there are not two distinct
  odd primes to select.  This is only an uncovered-site control, not a
  density theorem.

- **All odd primes \(1\pmod4\): PASS.** No pair has
  \(\chi_4(pq)=-1\), and every odd divisor sign is \(+1\).  Fixed-product
  character reversal cannot treat such a product.  No physical
  occurrence or lower mass is inferred.

- **Normalized full-involution averaging: PASS as self-return.** An
  average of exact full divisor-lattice reindexings remains an exact
  rewriting unless an independent contraction or coverage estimate is
  proved.  Canonical selection removes multiplicity but does not create
  residual coverage.

- **Ordered Abel: PASS algebraically, OPEN analytically.** The identity
  introduces the weighted partial-sum oscillation in (184.C21); neither
  small ordered-divisor gaps nor its target-weighted average is proved.

- **Sliding Fejer: PASS algebraically, OPEN analytically.** Full-line
  zero extension removes endpoint errors, and one aggregate real part is
  retained.  Shiftwise absolute values return the \(L^2X^\varepsilon\) scalar
  capacity.

- **Nonemptiness/full-face control: PASS.** The selector is allowed to
  choose no pair for every supported product.  Thus the strict sector may
  be empty.  The exact residual contains all no-pair products and all
  selected-pair neither/both allocations, so (184.C16) does not prove the
  complete \(t=1\) statement.

## 6. Dependencies and exact artifacts used

This review used only the assigned artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`, restricted to the Round-184 owners,
   their downstream graph, and the named exponent nodes;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md`;
5. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/conductor_round184_report_reconciliation.md`;
6. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/m2_transfer_transport_capacity_audit.md`;
7. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/blind_complete_t1_exchange_rederivation.md`; and
8. `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`.

No source theorem, web result, numerical experiment, candidate edit, or
shared-state edit was used.

## 7. Recommended state effect

**Promote only the strict subordinate XOR-sector theorem after the other
required seams and State Patch validation are also GREEN.**  The new
sector node must have no implication edge to a complete owner.  Retain
the exact residual and Fejer formulas as proved algebraic infrastructure,
with (184.C25) explicitly open.

In exact graph terms, leave the following unchanged:

- `M9-M1-hard-top-high-radical-small-t-residual-estimate`: **open**;
- `M9-M1-top-endpoint-signed-cone`: **open**;
- `M9-M1-direct-smooth-residual-blockwise-estimate`: **open**;
- `M9-M1-physical-one-count-assembly`: unchanged/`proved_internal`;
- `M9-M1`: unchanged/open;
- `M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector` and
  `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction`:
  unchanged as their already proved, disjointly scoped statements;
- every \(t\ge2\) small-\(G\) incidence and the large-\(G\)
  near-resonant complement: open;
- `M9-M2-hard-top-t1-close-opposite-prime-exchange-sector` and
  `M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction`:
  unchanged M2 method references, with no M2-to-M1 theorem edge;
- `M9-M2`, `M9-endpoint-uniformity`, and `M9`: unchanged/open;
- `Conditional-bridge` and `GC-global-M1-alternative-bridge`:
  unchanged conditional reductions;
- `GC-target`: open at exponent \(1/4\);
- `GC-partial-one-third`: unchanged `proved_internal` at exponent
  \(1/3\); and
- `GC-external-Li-Yang-theta-star`: unchanged
  `proved_external_dependency` at
  \(0.3144831759740614\ldots\).

Accordingly, the strict sector proves neither nonemptiness nor the full
\(t=1\) face, closes no complete owner, and changes no certified exponent.
