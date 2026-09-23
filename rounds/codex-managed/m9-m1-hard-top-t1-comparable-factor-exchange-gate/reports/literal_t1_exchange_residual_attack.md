# Round 184 report: literal hard-M1 \(t=1\) exchange and residual attack

- Campaign: `m9-m1-hard-top-t1-comparable-factor-exchange-gate`
- Task: `literal_t1_exchange_residual_attack`
- Role: discovery
- Access mode: selected context
- Starting graph SHA-256:
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`
- Status: candidate evidence only; no shared proof-state edit

## 1. Result: a strict literal comparable-prime sector and an exact residual

The complete hard-M1 \(t=1\) target is **not proved**.  The canonical
close opposite-character prime XOR incidence sector is target-safe for the
actual literal coefficient, and its complement is identified exactly.

Fix \(\kappa>0\).  For every squarefree product \(N\) meeting the literal
\(t=1\) support, choose at most one unordered pair of distinct odd prime
divisors \(\{p_N,q_N\}\), canonically from \((N,L,\kappa)\), such that

\[
 \chi _4(p_Nq_N)=-1,
 \qquad
 \left|\log(q_N/p_N)\right|\leq \kappa L^{-1/2}.
\tag{1.1}
\]

The choice is independent of the allocation \(N=uv\).  Let
\(\mathcal T^{\mathrm{cp}}_{L,X,\sigma}\) be the complete subsum of the
frozen \(t=1\) aggregate on which a pair is selected and exactly one of
\(p_N,q_N\) divides the character-bearing leg \(v\).  Then, uniformly for
every real \(X\geq2\), every literal middle or lower residual shell, and
both \(\sigma\in\{+1,-1\}\),

\[
 \boxed{
 |\mathcal T^{\mathrm{cp}}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{1.2}
\]

For a selected pair, the exact residual contains the allocations in which
neither or both selected primes divide \(v\).  For a product with no
selected pair, it contains every allocation.  Thus

\[
 \mathcal T_{L,X,\sigma}
 =\mathcal T^{\mathrm{cp}}_{L,X,\sigma}
  +\mathcal T^{\mathrm{rem}}_{L,X,\sigma}
\tag{1.3}
\]

is an exact incidence identity with no density assertion.  Ordered-divisor
Abel transport and the first diagonal-safe sliding Fejer identity are also
derived below.  The former has coefficient-insensitive \(L^2X^\varepsilon\)
capacity after positivity, and the latter leaves one unproved complete
signed short-shift correlation.  Hence neither continuation proves the
residual target.

## 2. Exact statement and hypotheses

Put \(e(z)=\exp(2\pi iz)\).  In the accepted Round-183 primitive-ray
coordinates, \(t=1\) is equivalent to

\[
 G=\rho=1,\qquad (u,v)=1,\qquad
 uv\ \hbox{squarefree},\qquad v\ \hbox{odd}.
\tag{2.1}
\]

Conversely every incidence in (2.1), with \(4u<v<16u\) and the literal
zero-extended support, is a unique \(t=1\) incidence.  Write

\[
 A_N^\sigma(u,v)=a_{L,X}^{\mathrm{lit},\sigma}(u,v),
 \qquad N=uv,
\tag{2.2}
\]

and extend it by zero to every allocation with \(v\) odd.  This notation
retains, rather than replaces, the exact dyadic frequency cutoff,
\(\Phi(u/(H+1))\),
\(W(\sqrt{4q_Xu/v})\), normalized \(u^{-3/4}v^{-3/4}\) power, floors,
stars, half weights, strict cone and shell edges, hard sample, both signs,
real-\(X\) crossings, and endpoint values.  In particular,

\[
 \mathcal T_{L,X,\sigma}
 =\sum_N\ \sum_{\substack{uv=N,\ (u,v)=1,\ v\ \mathrm{odd}\\
                           N\ \mathrm{squarefree}}}
   \chi_4(v)A_N^\sigma(u,v)e(\sigma\sqrt{XN}),
\tag{2.3}
\]

where zero extension in (2.2) imposes \(4u<v<16u\), \(u\asymp L\),
\(N\asymp L^2\), \(N>L\), and every other literal predicate.  The sum in
(2.3) is over incidences, so no divisor multiplicity is lost.

For definiteness, an allocation-independent canonical selector is obtained
by ordering all unordered eligible pairs \(\{p,q\}\) lexicographically by
\((\min(p,q),\max(p,q))\) and taking the first; label its smaller member
\(p_N\) and its larger member \(q_N\).  If the list is empty, no pair is
selected.  On the complete ambient XOR set define

\[
 \iota_N(u,v)=
 \begin{cases}
  (up_N/q_N,\,vq_N/p_N),&q_N\mid u,\ p_N\mid v,\\
  (uq_N/p_N,\,vp_N/q_N),&p_N\mid u,\ q_N\mid v.
 \end{cases}
\tag{2.4}
\]

The regularity used below is exactly the accepted literal interface in the
assigned packet, not an arbitrary-coefficient hypothesis: the normalized
amplitude is bounded by \(X^\varepsilon\); the dyadic factor has
scale-normalized discrete bounded variation; \(\Phi\) and the fixed
transformed \(W\) have uniform bounded ordinary derivatives; and the
remaining literal hard fields form a fixed finite cell/face ledger (with
harmless logarithmic multiplicity absorbed into \(X^\varepsilon\)).
Nonempty shells have \(L\ll H\).  No lower bound, nondegeneracy, or pair
density is assumed.

For the residual, if a pair is selected put

\[
 \rho_N(v)=1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
               +2\mathbf1_{p_Nq_N\mid v};
\tag{2.5}
\]

if no pair is selected, put \(\rho_N(v)=1\).  Thus \(\rho_N\) is exactly
zero on XOR allocations and exactly one on neither/both allocations.
Define

\[
 c_N^{\mathrm{rem},\sigma}
 =\mu^2(N)\sum_{\substack{v\mid N\\v\ \mathrm{odd}}}
   \rho_N(v)\chi_4(v)A_N^\sigma(N/v,v).
\tag{2.6}
\]

Then the second term in (1.3) is exactly

\[
 \mathcal T^{\mathrm{rem}}_{L,X,\sigma}
 =\sum_N c_N^{\mathrm{rem},\sigma}e(\sigma\sqrt{XN}).
\tag{2.7}
\]

## 3. Proof and derivation

### 3.1 Exact \(t=1\) face and capacity

Round 183 gives \(t=G\rho(u,v)\), where \(G\) and \(\rho\) are positive
integers.  Hence \(t=1\) forces \(G=\rho=1\).  The equality \(G=1\)
is \((u,v)=1\), while \(\rho=1\) says \(uv=\operatorname{sf}(uv)\).
This proves (2.1) and its converse.  Since \(v\) is odd, a possible factor
2 stays on the \(u\)-leg.  The incidence map has multiplicity one.

Literal support puts both \(u\) and \(v\) in fixed \(O(L)\) intervals.
There are therefore \(O(L^2)\) possible ordered pairs, and the normalized
literal amplitude is \(O_\varepsilon(X^\varepsilon)\).  This reproduces
the coefficient-insensitive capacity

\[
 O_\varepsilon(L^2X^\varepsilon)
\tag{3.1}
\]

against the target \(L^{3/2}X^\varepsilon\).  It is a method envelope,
not a lower bound for the literal sum.

### 3.2 Exchange algebra

On an XOR allocation, squarefreeness puts one selected prime on each leg,
so both quotients in (2.4) are integral.  The same selected pair is used
after exchange because \(N,L,\kappa\) do not change.  Direct calculation
gives

\[
 \iota_N^2=1,\qquad u'v'=uv=N.
\tag{3.2}
\]

There is no fixed point because \(p_N\ne q_N\).  Thus (2.4) is a
fixed-point-free multiplicity-one involution of the complete ambient XOR
set.  It preserves squarefreeness, coprimality, the parity of both legs,
the factor 2 on the \(u\)-leg, the fixed \(L\)-label, the product shell,
and the outer phase.  A literal \(u\)-shell or cone membership change is
not suppressed: it is retained by zero extension and charged in Section
3.3.

Since \(\chi_4(r)^{-1}=\chi_4(r)\) for odd \(r\),

\[
 \frac{\chi_4(v')}{\chi_4(v)}
 =\chi_4(p_Nq_N)=-1.
\tag{3.3}
\]

Reindexing the complete ambient XOR set, rather than first restricting to
the physical support, now gives the exact identity

\[
 \sum_{\rm XOR}\chi_4(v)A_N^\sigma(u,v)
 =\frac12\sum_{\rm XOR}\chi_4(v)
  \{A_N^\sigma(u,v)-A_N^\sigma(u',v')\}.
\tag{3.4}
\]

The factor \(1/2\) counts the two orientations of every orbit once.

### 3.3 Actual M1 coefficient difference and every boundary collar

Write \(\theta_N=\log(q_N/p_N)\).  In the two orientations,

\[
 (u',v')=(e^{\pm\theta_N}u,e^{\mp\theta_N}v),
 \qquad |\theta_N|\leq\kappa L^{-1/2}.
\tag{3.5}
\]

Whenever one orbit leg is supported, both legs lie in a fixed
\(\kappa\)-dependent enlargement of an \(O(L)\)-by-\(O(L)\) box, and

\[
 |u'-u|+|v'-v|\ll_\kappa L^{1/2}+1.
\tag{3.6}
\]

The normalized power is a function of \(uv=N\), hence is exactly
invariant.  On a common smooth cell, the \(\Phi\)-argument changes by

\[
 O_\kappa\!\left(\frac{L^{1/2}+1}{H+1}\right)
 =O_\kappa(L^{-1/2}),
\tag{3.7}
\]

and

\[
 \sqrt{4q_Xu'/v'}
 =e^{\pm\theta_N}\sqrt{4q_Xu/v}.
\tag{3.8}
\]

The bounded ordinary derivatives of \(\Phi\) and the fixed \(W\) thus
cost \(O_\kappa(L^{-1/2})\).  All orbit-invariant floors and global
parameters cost zero.

It is unnecessary to strengthen the accepted dyadic bounded variation to
a logarithmic derivative.  If \(\eta_L\) denotes a zero-extended sampled
dyadic factor and \(w\ll_\kappa L^{1/2}+1\), telescoping gives

\[
 |\eta_L(u')-\eta_L(u)|
 \leq\sum_{\min(u,u')\leq k<\max(u,u')}
       |\eta_L(k+1)-\eta_L(k)|.
\tag{3.9}
\]

For a fixed \(k\), an interval in (3.9) can cross \(k\) only when
\(|u-k|\leq w\); there are \(O(wL)\) possible ordered pairs in the
enlarged box.  Therefore the complete dyadic-profile difference costs

\[
 O(wL)\sum_k|\eta_L(k+1)-\eta_L(k)|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{3.10}
\]

This argument also covers any sampled one-variable BV factor and all its
zero-extension jumps.

It remains to count the literal hard faces.  A ratio face
\(v=\lambda u+O(1)\) can be crossed only inside

\[
 |v-\lambda u|\ll_\kappa L^{1/2}+1,
\tag{3.11}
\]

and a vertical or horizontal face has an analogous collar.  Each collar
contains

\[
 O_\kappa\bigl(L(L^{1/2}+1)\bigr)
 =O_\kappa(L^{3/2}+L)
\tag{3.12}
\]

ordered integer pairs.  This ledger includes the strict faces
\(v=4u,16u\), dyadic entries and exits, \(u=H\) when it meets the shell,
the support/plateau faces of
\(W(\sqrt{4q_Xu/v})\), real-\(X\) crossing faces, hard-sample faces, and
zero-extension mismatches.  Exact floor, ceiling, star, tie, and
half-weight loci contain only \(O(L)\) points per face.  The number and
total normalized seminorm of the literal faces are uniform up to
\(X^\varepsilon\).  The product shell and phase do not move at all.
Arithmetic restrictions only delete points.

Away from those collars, the common-cell product rule and (3.7)--(3.10)
give total difference

\[
 \sum_{N}\sum_{\rm XOR}
 |A_N^\sigma(u,v)-A_N^\sigma(u',v')|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{3.13}
\]

Insert (3.13) into (3.4), keep the product phase until after the exact
pairing, and only then use triangle.  This proves (1.2), for both signs
and with every real-\(X\) endpoint retained.

### 3.4 Exact residual and sign-mass controls

Equation (2.5) is one on neither/both allocations and zero on XOR
allocations.  Together with the no-pair convention it proves (1.3),
(2.6), and (2.7) exactly.

Write \(N=2^\nu M_N\), where \(M_N\) is odd and squarefree.  If no pair
is selected, the complete ambient constant-amplitude sign mass is

\[
 \sum_{v\mid M_N}\chi_4(v)
 =\prod_{r\mid M_N}(1+\chi_4(r)).
\tag{3.14}
\]

If \(p_N,q_N\) are selected, the residual constant-amplitude sign mass is

\[
 \sum_{v\mid M_N}\rho_N(v)\chi_4(v)
 =(1+\chi_4(p_Nq_N))
   \prod_{r\mid M_N/(p_Nq_N)}(1+\chi_4(r))=0.
\tag{3.15}
\]

Thus the selected residual has exact total sign balance, but this says
nothing about its truncated physical window.  Conversely, an all-
\(1\pmod4\) odd part has no eligible opposite-character pair and (3.14)
is completely positive.  These are algebraic controls only; no density or
literal lower mass follows.

### 3.5 Ordered-divisor transport: exact identity, \(L^2\) capacity

For a fixed \(N\), order the residual odd divisors as
\(v_1<\cdots<v_r\).  Put

\[
 \epsilon_j=\chi_4(v_j),\qquad
 C_j=\sum_{i\leq j}\epsilon_i,\qquad
 a_j=A_N^\sigma(N/v_j,v_j),
 \qquad a_0=a_{r+1}=C_0=0.
\tag{3.16}
\]

Exact Abel summation gives

\[
 c_N^{\mathrm{rem},\sigma}
 =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j).
\tag{3.17}
\]

Since \(\sum_j(a_{j+1}-a_j)=0\), subtracting the midpoint of the range
of the real partial sums \(C_j\) yields

\[
 |c_N^{\mathrm{rem},\sigma}|
 \leq\frac{\operatorname{osc} C_N}{2}
       \sum_{j=0}^{r}|a_{j+1}-a_j|.
\tag{3.18}
\]

As a function of increasing \(v\), the supported coordinate
\(u=N/v\) is monotone; sampling the accepted literal BV profiles cannot
increase their variation.  The smooth factors and fixed hard faces add
only \(O_\varepsilon(X^\varepsilon)\).  Hence the variation factor in
(3.18) is \(O_\varepsilon(X^\varepsilon)\).

After a positive sum over the \(O(L^2)\) possible products, divisor bounds
give only \(O_\varepsilon(L^2X^\varepsilon)\).  The all-
\(1\pmod4\), no-pair control has \(C_j=j\), so sign balance and bounded
profile variation alone cannot improve this transport envelope.  This is
not a lower bound for the actual residual; it identifies the missing
average signed relation.

### 3.6 Sliding Fejer continuation and the first missing correlation

Abbreviate \(c_N=c_N^{\mathrm{rem},\sigma}\), put
\(z_N=c_Ne(\sigma\sqrt{XN})\) for positive \(N\), and extend \(z_N\) by
zero to all integers outside a containing interval of
\(M_L\asymp L^2\) sites.  For every positive integer \(R\), set

\[
 E_R=\frac1R\sum_{s\in\mathbb Z}
 \left|\sum_{0\leq j<R}z_{s+j}\right|^2.
\tag{3.19}
\]

Expansion before any shiftwise triangle gives the exact identity

\[
\begin{aligned}
 E_R={}&\sum_N|c_N|^2\\
 &+2\operatorname{Re}\!\sum_{1\leq r<R}
   \left(1-\frac rR\right)
   \sum_N c_{N+r}\overline{c_N}
   e\!\left(\sigma\sqrt X(\sqrt{N+r}-\sqrt N)\right).
\end{aligned}
\tag{3.20}
\]

Summing all sliding windows and applying Cauchy only after (3.20) gives

\[
 |\mathcal T^{\mathrm{rem}}_{L,X,\sigma}|^2
 \leq\frac{M_L+R-1}{R}E_R.
\tag{3.21}
\]

The literal divisor bound gives \(\sum_N|c_N|^2\ll_\varepsilon
L^2X^\varepsilon\).  Therefore \(R_0=\lceil L\rceil\) is the first
diagonal-safe scale: its diagonal contribution to the right side of
(3.21) is \(O_\varepsilon(L^3X^\varepsilon)\).  The exact sufficient
connector still missing is the single aggregate estimate

\[
 \operatorname{Re}\!\sum_{1\leq r<R_0}
   \left(1-\frac r{R_0}\right)
   \sum_N c_{N+r}\overline{c_N}
   e\!\left(\sigma\sqrt X(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^2X^\varepsilon.
\tag{3.22}
\]

There is one outer real part in (3.22).  Taking absolute values shift by
shift gives only \(O_\varepsilon(R_0L^2X^\varepsilon)=
O_\varepsilon(L^3X^\varepsilon)\), restores the \(L^2\) scalar capacity,
and loses exactly the required half-power.

### 3.7 One-prime and normalized-involution self-return controls

If an odd \(p\mid N\) is moved alone between the legs, the ratio
\(z=v/u\in(4,16)\) goes to \(zp^2>36\) or \(z/p^2<16/9\).  Hence the
two physical supports are disjoint.  For \(p\equiv3\pmod4\), the exact
sign-reversing half-difference identity therefore doubles \(\ell^1\)
boundary capacity rather than contracting it.

More generally, for any normalized family of allocation-independent
sign-reversing divisor-lattice involutions \(I\), linearity gives

\[
 b_N=\frac12\sum_I\lambda_I
       \sum_{uv=N}\chi_4(v)\{A_N(u,v)-A_N(I(u,v))\},
 \qquad \sum_I\lambda_I=1,
\tag{3.23}
\]

which is exactly the original row coefficient.  Averaging involutions
without a proved close-profile difference is an algebraic self-return.

## 4. First doubtful or unproved step

No unpriced algebraic, coefficient, or endpoint step remains in the
strict sector (1.2), subject to independent review of the accepted literal
regularity interface.  The first unproved step toward the complete
\(t=1\) target is the residual (2.7).

The exact selected-pair sign balance (3.15) controls only a constant
amplitude over the complete divisor cube; it does not control the literal
one-sided cone.  Ordered transport followed by positivity has \(L^2\)
capacity.  The first explicit owner-relevant analytic relation would be
(3.22), or an equally strong cancellation statement that averages the
partial-sum oscillations in (3.18) jointly with the product phase.  Neither
relation follows from pair availability, total sign balance, bounded
variation, one-prime toggling, normalized involution averaging, or a
shiftwise triangle.  No assertion that the residual or full literal sum is
large is made.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_t1_face` | **Pass.** Equation (2.1) proves exactly \(G=\rho=1\), coprime squarefree \(uv\), odd \(v\), strict cone, and multiplicity one. |
| `literal_coefficient_and_zero_extension` | **Pass.** Equations (2.2)--(2.3) use the actual coefficient and place every missing partner, strict edge, floor, star, half weight, crossing, and endpoint under zero extension. |
| `every_shell_both_signs_real_X_endpoints` | **Pass for the strict sector; full face open.** The difference and collar ledger is signwise and uniform in all fixed real-\(X\) parameters. |
| `one_outer_absolute_value` | **Pass.** The sector theorem is one complete signed aggregate.  Positivity is used only after the exact sign-reversing difference (3.4). |
| `capacity_L2_target_L_three_halves` | **Pass.** Equation (3.1) records \(L^2\) capacity and (3.13) earns exactly the missing \(L^{1/2}\) on the XOR sector. |
| `canonical_selector_allocation_independence` | **Pass.** The lexicographic selector uses only \((N,L,\kappa)\). |
| `exchange_integrality_multiplicity_fixed_point` | **Pass.** Squarefreeness and XOR give an integral multiplicity-one involution; distinct primes exclude fixed points. |
| `product_phase_squarefree_coprime_parity_preservation` | **Pass.** Product, phase, arithmetic predicates, and the even factor are invariant.  Literal support changes are retained and priced. |
| `chi4_sign_reversal` | **Pass.** Equation (3.3) is exact. |
| `common_cell_profile_variation` | **Pass.** Equations (3.7)--(3.10) use ordinary derivatives for \(\Phi,W\) and an aggregate BV charging lemma for the dyadic factor; no logarithmic derivative is assumed. |
| `boundary_crossing_collar_count` | **Pass.** Every fixed ratio/vertical/horizontal face costs \(O_\kappa(L^{3/2}+L)\); exact ties cost \(O(L)\). |
| `exact_xor_residual` | **Pass.** Equations (2.5)--(2.7) give no-pair plus neither/both and nothing else. |
| `no_pair_density_inference` | **Pass.** No nonvacuity, density, or positive proportion is used; (3.14) includes empty-selector products. |
| `one_prime_toggle_and_involution_average_self_return` | **Pass/no-go.** Section 3.7 proves disjoint-support one-prime leakage and exact normalized-family self-return. |
| `ordered_divisor_transport_identity` | **Pass algebraically; target open.** Equations (3.17)--(3.18) are exact and leave \(L^2\) positive capacity. |
| `fejer_short_shift_connector` | **Pass as an exact reduction; analytic estimate open.** Equations (3.19)--(3.22) isolate the first diagonal-safe correlation. |
| `no_positive_norm_or_shift_triangle` | **Pass.** No norm is used to prove the strict sector before the signed exchange; the residual discussion explicitly rejects shiftwise triangle as a proof. |
| `t_ge_2_and_near_resonant_quarantine` | **Pass.** The report treats only \(t=1\); all \(t\geq2\) small-\(G\) and large-\(G\) near-resonant incidences remain open. |
| `complete_small_t_owner_quarantine` | **Pass.** Even a full \(t=1\) theorem would not pay the complete Round-183 complement; only a strict \(t=1\) sector is proved here. |
| `downstream_and_exponent_quarantine` | **Pass.** No hard or smooth parent, M9-M1, M2 owner, endpoint-uniformity claim, M9, bridge, theorem, or exponent changes. |
| `no_in_round_pivot` | **Pass.** Every derivation remains inside the frozen literal hard-M1 \(t=1\) face. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

Only the assigned packet was used:

- `protocol.md`;
- `state/proof_obligations.yml`, at graph hash
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`;
- `state/active_campaign.yml`;
- `strategy/round184_m1_hard_top_t1_comparable_factor_exchange_strategy.md`;
- `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`;
- `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reports/literal_small_t_signed_contraction_attack.md`;
- `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/conductor_round183_adjudication.md`;
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`, used only as a method reference and rederived with the M1 cone and coefficient; and
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/profile_boundary_power_seam_review.md`, used only to identify seams that were then checked in the M1 normalization.

The task brief itself fixed the output contract and controls.  The proof is
finite exchange algebra, literal profile variation, lattice-collar
counting, Abel summation, and an exact Fejer expansion.

## 7. Recommended state effect

**Recommend `strict_hard_m1_t1_comparable_factor_sector`.**  After
independent selector/character and coefficient/profile/endpoint seam
review, promote only (1.1)--(1.2) as a subordinate strict incidence-sector
fact.  Record (2.5)--(2.7) as its exact residual and retain (3.17)--(3.23)
as scoped mechanism evidence: positive ordered transport has \(L^2\)
capacity, while the complete one-outer-real-part correlation (3.22) is
unproved.

Keep `M9-M1-hard-top-high-radical-small-t-residual-estimate` open.  Make no
claim for the rest of \(t=1\), any \(t\geq2\) incidence, the large-\(G\)
near-resonant complement, the complete small-\(t\) owner, a hard or smooth
M1 parent, any M2 obligation, M9, either bridge, the quarter theorem, or an
exponent.
