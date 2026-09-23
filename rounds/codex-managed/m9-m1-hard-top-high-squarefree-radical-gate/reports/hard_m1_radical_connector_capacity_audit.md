# Hostile audit: hard-M1 radical reduction, capacity, and connector

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Round: `181`
- Task: `hard_m1_radical_connector_capacity_audit`
- Role: `barrier_no_go`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Generated: `2026-08-27T08:01:37.561951+00:00`
- Evidence status: candidate only; no shared proof-state edit is authorized.

## 1. Result

**Exact reduction lemma and capacity no-go.**  The product-fibre regrouping and the decomposition of every positive product into its squarefree kernel are exact, multiplicity preserving, and compatible with every literal hard-profile field when the literal coefficient is zero-extended before regrouping.  If

\[
 \mathcal T_{L}^{\sigma}(X)
 =\sum_{h\asymp L}\sum_{\substack{4h<n<16h\\ n\ \mathrm{odd}}}
 \chi _4(n)a_{L,X}^{\mathrm{lit},\sigma}(h,n)
 e\!\left(\sigma\sqrt{Xhn}\right),\qquad \sigma\in\{+1,-1\},
\]

and

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\r/h\ \mathrm{odd},\ 4h<r/h<16h}}
 \chi _4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h),
\]

then, exactly,

\[
 \mathcal T_L^{\sigma}(X)
 =\sum_{r\geq1}C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})
 =\sum_{\substack{s\geq1\\\mu ^2(s)=1}}
   \sum_{t\geq1}C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\tag{1.1}
\]

On nonzero literal support, (st^2\asymp L^2), hence

\[
 s\ll L^2,\qquad t\asymp {L\over\sqrt s},\qquad
 s>L\Longrightarrow t\ll\sqrt L.
\tag{1.2}
\]

Moreover, for every incidence (hn=st^2),

\[
 (h,n)\mid t.
\tag{1.3}
\]

The normalized literal symbol is uniformly bounded on the fixed cone.  Therefore divisor incidence gives the target-safe absolute estimate

\[
 \sum_{\substack{s\leq L\\\mu ^2(s)=1}}
 \sum_{t\geq1}|C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{1.4}
\]

Thus the squarefree split is a **strict, exact, owner-compatible reduction**: it is neither a false partition nor a self-return.  It removes a proved target-safe sector and leaves the exact complement (s>L).  It is nevertheless **capacity preserving on that complement**.  Coefficient-insensitive summation there is only

\[
 \sum_{\substack{s>L\\\mu ^2(s)=1}}\sum_t
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^2X^\varepsilon,
\tag{1.5}
\]

against the required (L^{3/2}X^\varepsilon).  The exact (t=1) face consists of squarefree, coprime (h,n) and already retains (L^2) incidence capacity, or (L^{2-o(1)}) distinct-product capacity, in the geometric/adversarial class.  Hence neither (1.3), square-multiplier averaging, product-fibre triangle, coefficient-uniform TT\(^*\), character erasure, nor a multiplicative/full-divisor surrogate can supply the missing (L^{1/2}).  At (L\asymp X^{1/6}), this is precisely (X^{1/12}).

No estimate for the complete literal high-radical scalar is proved here.  The first genuinely new required input remains a fixed-literal-direction signed correlation theorem, valid in particular at (t=1), before every positive norm.

## 2. Exact statement and hypotheses

Fix a real (X\geq2), one literal middle or lower residual frequency shell (L) of the unique hard M1 profile, and one frequency sign \(\sigma\).  Let \(\mathcal H_L\) be its exact integer (h)-support.  There are fixed profile constants (0<c_0<c_1<\infty), independent of (L,X), such that

\[
 c_0L\leq h\leq c_1L\qquad(h\in\mathcal H_L).
\tag{2.1}
\]

The coefficient (a_{L,X}^{\mathrm{lit},\sigma}) contains, without replacement or smoothing, the actual factor (\Phi(h/(H+1))), the hard sample (W(\sqrt{4q_Xh/n})), all normalized powers, the literal dyadic shell, strict cone edges, height and endpoint floors, stars or half weights, the sign tag, real-(X) support crossings, and zero extensions.  Its only analytic property used below is the literal normalized bound

\[
 \sup_{h,n}|a_{L,X}^{\mathrm{lit},\sigma}(h,n)|\ll_W1.
\tag{2.2}
\]

This follows at the counting interface because (\Phi) and the fixed profile are bounded, the normalized monomials are bounded on (h,n\asymp L), stars have modulus at most one, and floors, crossings, and zero extension only select or delete sites.  No derivative, Mellin decay, multiplicativity, positivity, or sign regularity of the literal coefficient is assumed.

Under (2.1)--(2.2), the conclusions are:

1. The identities (1.1), support relations (1.2), and divisibility (1.3) hold without error.
2. The low-radical estimate (1.4) holds uniformly in every literal endpoint choice and both signs.
3. The high-radical coefficient-blind bound is (1.5).  For fixed (t), its coefficient-blind capacity is
   \[
    \ll_\varepsilon {L^2\over t^2}X^\varepsilon.
   \tag{2.3}
   \]
4. The stronger fixed-(t) theorem
   \[
    \left|\sum_{\substack{s>L\\\mu ^2(s)=1}}
    C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
    \ll_\varepsilon (L^2/t^2)^{3/4}X^\varepsilon
   \tag{2.4}
   \]
   uniformly for every supported (t), would imply the complete high-radical target by summation in (t).  Statement (2.4) is not proved.
5. Conditional on the complete high-radical target, (1.4) restores the whole literal hard cone at (L^{3/2}X^\varepsilon), and the accepted one-sided transform then restores the physical hard block at (X^{1/4+\varepsilon}).  This implication reaches only the hard residual child.

## 3. Proof or derivation

### 3.1 Exact product-fibre identity

Extend (a_{L,X}^{\mathrm{lit},\sigma}(h,n)) by zero off its exact literal support.  The map

\[
 (h,n)\longmapsto r=hn
\]

is finite-to-one.  For a fixed (r), its preimages are exactly (h\mid r) with (n=r/h), subject to the same shell, oddness, and strict cone conditions.  The phase is constant on this fibre:

\[
 e(\sigma\sqrt{Xhn})=e(\sigma\sqrt{Xr}).
\]

Summing the coefficients over the fibre gives (C_{L,X}^{\sigma}(r)), proving the first equality in (1.1).  No absolute value, completion, endpoint alteration, or multiplicity factor has entered.

### 3.2 Unique squarefree kernel, support, and the common-divisor constraint

Write (r=\prod_pp^{\nu_p(r)}), and set

\[
 t=\prod_pp^{\lfloor\nu_p(r)/2\rfloor},\qquad
 s=\prod_pp^{\nu_p(r)\bmod2}.
\tag{3.1}
\]

Then (r=st^2), (\mu^2(s)=1), and prime valuations show uniqueness.  Since (X>0) and (t\geq1),

\[
 \sqrt{Xr}=\sqrt{Xst^2}=t\sqrt{Xs},
\]

which proves the second equality in (1.1), sign by sign.

From (2.1) and (4h<n<16h),

\[
 4c_0^2L^2<r<16c_1^2L^2.
\tag{3.2}
\]

Consequently every nonzero (C(st^2)) satisfies

\[
 {2c_0L\over\sqrt s}<t<{4c_1L\over\sqrt s},
\tag{3.3}
\]

up to harmless endpoint conventions already contained in the zero extension.  This proves (s\ll L^2), (t\asymp L/\sqrt s), and especially

\[
 s>L\quad\Longrightarrow\quad t<4c_1\sqrt L.
\tag{3.4}
\]

For (1.3), put (g=(h,n)).  If (p^a\Vert h) and (p^b\Vert n), then

\[
 v_p(g)=\min(a,b)\leq\left\lfloor{a+b\over2}\right\rfloor=v_p(t).
\]

Thus (g\mid t).  This implication is one-way: (t/g) also contains square factors lying wholly in (h/g) or wholly in (n/g).  In particular, (g\mid t) is not a parametrization of the product fibre.  At (t=1), however, it forces (g=1), and (hn=s) squarefree then forces both (h,n) squarefree.  The mandatory (t=1) face is therefore the squarefree-coprime face.

### 3.3 Low-radical ledger

By (2.2), for every supported (r\ll L^2),

\[
 |C_{L,X}^{\sigma}(r)|
 \leq \sum_{h\mid r}|a_{L,X}^{\mathrm{lit},\sigma}(h,r/h)|
 \ll_W \tau(r)
 \ll_\varepsilon X^\varepsilon.
\tag{3.5}
\]

The last step uses the elementary divisor bound and the physical fact that (L) is at most a fixed power of (X); an (\varepsilon/2) relabelling absorbs (r\ll L^2).  For fixed squarefree (s), (3.3) leaves at most

\[
 O\!\left(1+{L\over\sqrt s}\right)
\tag{3.6}
\]

integer square multipliers.  Hence

\[
\begin{aligned}
 \sum_{\substack{s\leq L\\\mu^2(s)=1}}\sum_t|C(st^2)|
 &\ll_\varepsilon X^\varepsilon
   \sum_{s\leq L}\left(1+{L\over\sqrt s}\right)\\
 &\ll_\varepsilon X^\varepsilon
   \left(L+L\int_0^L u^{-1/2}\,du\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\end{aligned}
\tag{3.7}
\]

This proof is absolute and therefore survives every literal deletion, crossing, half weight, sign, or sharp boundary.  It proves (1.4) without using any unproved cancellation.

### 3.4 High-radical and fixed-(t) capacity

The same argument on (L<s\ll L^2) gives

\[
\begin{aligned}
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_t|C(st^2)|
 &\ll_\varepsilon X^\varepsilon
 \sum_{L<s\ll L^2}\left(1+{L\over\sqrt s}\right)\\
 &\ll_\varepsilon L^2X^\varepsilon.
\end{aligned}
\tag{3.8}
\]

For fixed (t), (3.2) places (s) in a fixed-ratio interval of length (O(L^2/t^2)), yielding (2.3).  Comparing (2.3) with (2.4), the required fixed-(t) saving is

\[
 \left({L^2\over t^2}\right)^{1/4}
 =L^{1/2}t^{-1/2}.
\tag{3.9}
\]

At (t=1), this is the entire missing (L^{1/2}).  If (2.4) were available uniformly, (3.4) and the convergent power sum would give

\[
 \sum_{t\ll\sqrt L}(L^2/t^2)^{3/4}
 =L^{3/2}\sum_{t\ll\sqrt L}t^{-3/2}
 \ll L^{3/2}.
\tag{3.10}
\]

Thus the fixed-(t) proposal is arithmetically sufficient but strictly stronger than the aggregate theorem: it places an absolute value outside each (s)-sum and then uses triangle in (t).  Nothing in the squarefree decomposition proves (2.4).

The exact condition ((h,n)\mid t) does not improve (3.8) by a power.  Splitting by a common divisor costs only divisor factors, and the (t=1) slice has ((h,n)=1) identically.  Coprime squarefree pairs have positive density in every fixed interior cone rectangle, so the common-divisor restriction removes no power-sized part of that face.

### 3.5 Perfect-square and (t=1) controls

Perfect-square products are exactly (s=1).  They contribute absolutely

\[
 \sum_t|C(t^2)|\ll_\varepsilon LX^\varepsilon,
\tag{3.11}
\]

which is below target even when (X) is a square and every phase (e(t\sqrt X)) equals one.  More generally, if (Xs) is a perfect square for one squarefree (s>L), its entire aligned (t)-ray has length (O(L/\sqrt s)\ll\sqrt L).  Distinct squarefree (s)'s cannot both satisfy (Xs\in\mathbb Z^2), since their ratio would be a rational square.  Exact perfect-square centres therefore do not create the missing high-radical mass and do not provide its saving either.

The (t=1) face cannot be discarded.  On it (r=s=hn) is squarefree and (h,n) are coprime squarefree integers.  In every fixed interior cone rectangle, elementary Möbius inclusion--exclusion gives \(\gg L^2\) such incidences: for each odd prime the local allowed density is

\[
 (1-1/p)^2(1+2/p)=1-3p^{-2}+2p^{-3},
\]

whose product is positive, and the parity condition at \(2\) also has positive density.  Since each product has at most \(L^{o(1)}\) divisor incidences, these give \(L^{2-o(1)}\) distinct product fibres.  This is a geometric/adversarial capacity statement, not a lower bound for the literal signed sum.

Indeed, on any such set an arbitrary bounded coefficient shadow can be chosen as

\[
 b(h,n)=\chi_4(n)e(-\sigma\sqrt{Xhn}),
\]

so every summand equals one.  It produces (L^{2-o(1)}) size and falsifies any (L^{3/2}X^\varepsilon) theorem uniform over arbitrary bounded coefficients.  The same control can be made with real signs after a common phase rotation.  This simultaneously shows that erasing (\chi_4), absorbing it into arbitrary coefficients, or asking for product-fibre cancellation on singleton fibres cannot prove the literal target.  It does **not** refute the fixed literal coefficient, which is not phase adaptable.

### 3.6 Literal multiplicativity and Mellin audit

The exact coefficient is an incomplete, (X,L)-dependent divisor sum:

\[
 C_{L,X}(r)=\sum_{h\mid r}
 \chi_4(r/h)\,
 1_{h\asymp L}\,1_{4h<r/h<16h}\,
 a_{L,X}^{\mathrm{lit}}(h,r/h).
\tag{3.12}
\]

It is not multiplicative in (r).  The shell (h\asymp L), the ratio cone, (\Phi(h/(H+1))), the hard sample (W(\sqrt{4q_Xh/(r/h)})), floors, stars, and real-(X) support crossings do not factor under (r=r_1r_2) with ((r_1,r_2)=1).  The identity ((h,n)\mid t) does not repair this: after writing (h=ga,n=gb), (t/g) still contains the independent square parts of the coprime integers (a,b), while all literal ratio and endpoint fields remain joint.

If all divisor restrictions and literal weights were removed, a surrogate such as

\[
 \sum_{h\mid r}\chi_4(r/h)=(1*\chi_4)(r)
\]

would be multiplicative.  That is a full-divisor surrogate, not (3.12).  Mellin inversion of a smooth ratio factor can represent part of (3.12) as a continuous superposition of separated powers, but it leaves incomplete (L)-dependent divisor polynomials, sharp/stared boundary pieces, floor transitions, and the high-radical truncation (s>L).  No Euler product or literal finite-sum identity results.  A lawful Mellin continuation would have to restore all such pieces and prove, after integration over its transform norm, a net (L^{-1/2}) saving (or (L^{-1/2}t^{1/2}) relative to (2.3)).  No such estimate is contained in the permitted packet.  Treating the smooth/full-divisor model as the literal coefficient is therefore the first false seam.

### 3.7 No-repeat mechanisms and exact connector

Taking triangle after product grouping is exactly (3.8) and leaves (L^2).  A coefficient-uniform Gram has the same capacity: on a fixed-(t) set of (N_t\asymp L^2/t^2) sites, the phase row has \(\ell^2\)-operator norm (N_t^{1/2}), while the divisor bound gives coefficient \(\ell^2\)-size (N_t^{1/2}X^\varepsilon); their product is (N_tX^\varepsilon), not (N_t^{3/4}X^\varepsilon).  The phase-adapted control makes this sharp in the adversarial class.  Any useful Gram theorem must therefore be a fixed-literal-vector estimate before a uniform norm.  The accepted canonical global M1 Gram cannot be imported because it has summed away the physical (L)-partition and has no localization map to this hard cone.

For the coefficient-free fixed-(t) phase (f_t(s)=t\sqrt{Xs}), the first (B)-process has stationary relation

\[
 k=f_t'(s)={t\sqrt X\over2\sqrt s},\qquad
 s={t^2X\over4k^2},\qquad
 f_t(s)-ks={t^2X\over4k}.
\tag{3.13}
\]

Thus the principal dual is a reciprocal phase.  A second bare (B)-process returns the square-root phase.  At the critical shell (L\asymp X^{1/6}), the (t=1) primal and derivative ranges are both of order (L^2); there is no length contraction.  More importantly, (C(st^2)) is a discontinuous divisor-incidence coefficient with no proved BV hypothesis authorizing a scalar coefficient-preserving transform.  Repeating the second-(B)-process or rank-one square-root-wave route is therefore a self-return, not a source of (3.9).

The combined top M1/M2 cone is also unavailable: its exact symbol is piecewise, it has an unmatched M1 wing, and the accepted graph supplies no implication from a combined estimate to the separate hard M1 child.  M2 cancellation cannot be borrowed to prove this owner.

Finally, suppose the literal high-radical estimate is proved for every residual hard shell and both signs.  Adding (1.4) yields

\[
 \mathcal T_L^{M1}\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{3.14}
\]

The accepted hard transform is

\[
 \mathcal M^+_{1,\mathrm{end},L}
 =-{2e(1/8)\over\pi}X^{1/4}L^{-3/2}\mathcal T_L^{M1}
 +O_\varepsilon(X^{1/4+\varepsilon}).
\tag{3.15}
\]

Equations (3.14)--(3.15), followed by the already accepted conjugate-sign restoration and logarithmic shell sum, close exactly `M9-M1-top-endpoint-signed-cone`, equivalently the middle/lower hard residual child in `M9-M1-physical-one-count-assembly`.  They do not close the independent smooth residual child, so they do not prove `M9-M1`.

## 4. First doubtful or unproved step

The first unproved step is precisely a bound for the complete literal high-radical direction before positivity:

\[
 \left|\sum_{\substack{s>L\\\mu^2(s)=1}}\sum_t
 C_{L,X}^{\mathrm{lit}}(st^2)e(t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\tag{4.1}
\]

or a valid stronger family such as (2.4).  The product identity, squarefree uniqueness, support, (s>L\Rightarrow t\ll\sqrt L), ((h,n)\mid t), and the low ledger all precede (4.1) and are proved.  None yields cancellation at (t=1).

The earliest invalid substitute is to assert that (C_{L,X}^{\mathrm{lit}}(st^2)) is a multiplicative, smoothly varying, or arbitrary-coefficient sequence to which a scalar Mellin, (B)-process, large-sieve, or operator-norm estimate applies.  It is none of these.  A future proof must exhibit an exact literal relation that survives the (t=1) squarefree-coprime face, (\chi_4), every hard symbol field, and the final outside absolute value, and it must be priced to save (L^{1/2}) there.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_product_fibre_identity` | **Pass.** Exact finite regrouping, with fibre multiplicity preserved and no triangle inequality. |
| `unique_squarefree_kernel_decomposition` | **Pass.** Formula (3.1) is prime-by-prime unique and preserves the phase exactly. |
| `literal_product_support` | **Pass.** Equations (3.2)--(3.4) give (s\ll L^2), (t\asymp L/\sqrt s), and (s>L\Rightarrow t\ll\sqrt L). |
| `gcd_divides_t` | **Pass.** Prime valuations prove ((h,n)\mid t); the converse is false and the fact gives no power on (t=1). |
| `low_radical_incidence_bound` | **Pass.** Equation (3.7) proves the full low sector absolutely at (L^{3/2}X^\varepsilon). |
| `high_radical_capacity_ledger` | **Pass as a ledger, not an estimate.** Equation (3.8) is (L^2X^\varepsilon), leaving (L^{1/2}). |
| `fixed_t_power_summation` | **Pass conditionally.** The proposed (3/4)-power bounds sum by (\sum t^{-3/2}<\infty); the fixed-(t) input remains unproved and needs saving (3.9). |
| `perfect_square_centre_control` | **Pass.** (s=1) costs (O(LX^\varepsilon)); any one aligned high-(s) ray costs (O(\sqrt L X^\varepsilon)). |
| `high_radical_t1_control` | **Pass as an obstruction.** (t=1) is squarefree-coprime, has (L^2) incidence and (L^{2-o(1)}) distinct-product adversarial capacity, and receives no (t)-average. |
| `arbitrary_coefficient_control` | **Pass; the arbitrary analogue is falsified.** Phase-adapted bounded coefficients produce (L^{2-o(1)}), so a coefficient-uniform (L^{3/2}) theorem is false. |
| `character_erasure_control` | **Pass; erasure is rejected.** (\chi_4) is inside (C) and is absorbable by the adversarial shadow; any proof that erases it has only the false coefficient-uniform interface. |
| `one_site_one_fibre_controls` | **Pass.** An arbitrary shadow supported on one allowed incidence makes its product fibre a singleton, so there is no support-forced within-fibre cancellation or partner involution. |
| `hard_endpoint_and_zero_extension` | **Pass.** All identities are at fixed real (X); floors, stars, crossings, and hard samples remain coefficient values, while zero extension makes regrouping exact. |
| `mellin_product_fibre_multiplicativity` | **Pass as a hostile seam.** The literal incomplete divisor coefficient is not multiplicative; smooth/full-divisor Euler products are surrogates and have no exact hard-endpoint connector. |
| `product_triangle_no_repeat` | **Pass.** Product-fibre triangle is exactly the nonclosing (L^2) ledger. |
| `second_B_process_no_repeat` | **Pass.** Formula (3.13) gives the reciprocal principal phase and a second bare transform returns; no (t=1) contraction appears. |
| `canonical_Gram_no_repeat` | **Pass.** Coefficient-uniform Gram capacity is (L^2), and the accepted global canonical Gram has no localization to this hard shell. |
| `combined_M1_M2_no_repeat` | **Pass.** The combined cone has a piecewise symbol, unmatched M1 wing, and no separate-owner implication. |
| `hard_parent_connector` | **Pass conditionally and exactly.** High target plus (1.4) gives (3.14); (3.15) closes only the hard residual child. |
| `literal_unknown_quarantine` | **Pass.** Adversarial capacities are not asserted as literal lower mass; the actual high-radical scalar remains open. |
| `downstream_scope` | **Pass.** Smooth M1, GAR, M9-M1, M2, endpoint uniformity, M9, and both bridges remain outside the conclusion. |
| `exponent_quarantine` | **Pass.** The ledger records (L^{1/2}=X^{1/12}) at (L\asymp X^{1/6}); it proves no exponent improvement. |

No numerical or experimental evidence was used.

## 6. Dependencies and exact artifacts used

This report uses only the assigned brief and its permitted packet:

1. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/briefs/hard_m1_radical_connector_capacity_audit.md`;
2. `protocol.md`;
3. `state/proof_obligations.yml` at SHA-256 `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`;
4. `state/active_campaign.yml`;
5. `strategy/round181_selection/conductor_round181_selection_decision.md`;
6. `strategy/round181_m1_hard_top_high_squarefree_radical_strategy.md`;
7. `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_capacity_and_labels.md`;
8. `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`;
9. `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/synthesis.md`.

The exact graph interfaces used are `H4-Phi-regularity`, `M9-M1-top-endpoint-transform`, `M9-M1-top-endpoint-signed-cone`, `M9-M1-direct-hard-smooth-separate-one-third-minimax`, `M9-M1-physical-one-count-assembly`, `M9-M1-near-product-fiber-capacity-no-go`, `M9-M1-ordered-cell-Bprocess-capacity-no-go`, `M9-M1-canonical-Gram-route-scope-obstruction`, and `M9-top-combined-piecewise-cone`.  No external theorem, web source, or sibling Round-181 report was used.

## 7. Recommended state effect

**Promote only the exact reduction package** consisting of the product-fibre identity, unique squarefree-kernel split, support and common-divisor relations, and the target-safe low-radical estimate.  Record the complement exactly as (s>L), (t\ll\sqrt L), with the mandatory (t=1) squarefree-coprime face.

**Retain the complete high-radical target open.**  Record the (L^2) coefficient-insensitive capacity, the fixed-(t) saving requirement (L^{1/2}t^{-1/2}), the arbitrary-coefficient falsifier, and the nonmultiplicativity/Mellin seam as mechanism-scoped barriers, never as literal lower bounds.

If no sibling report proves a larger literal sector, the mathematically accurate Round-181 exit is `strict_hard_m1_radical_sector`: the low sector is a genuine target-safe reduction, while the exact high complement remains at full leading capacity.  Do not promote `hard_m1_high_radical_target`, do not close `M9-M1-top-endpoint-signed-cone`, and do not infer any smooth-M1, GAR, M2, bridge, theorem, or exponent claim.
