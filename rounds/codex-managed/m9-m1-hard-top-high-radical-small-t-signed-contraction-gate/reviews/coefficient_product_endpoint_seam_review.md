# Round 183 coefficient/product/endpoint seam review

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: independent seam reviewer
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Review target:
  `reports/literal_small_t_signed_contraction_attack.md`, with the two
  sibling reports used as consistency controls
- Verdict: **GREEN**

## Exact claim reviewed

The review covers only the strict incidence-level sector in equations
(1.6)--(1.7) of the discovery report.  With

\[
 h=Gu,\qquad n=Gv,\qquad (u,v)=1,
\]

put

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{uv/s(u,v)},\qquad
 T_L=\lceil\sqrt L\rceil,
\]

and

\[
 G_0=\lceil L^{1/4}\rceil,\qquad
 \Delta_X(u,v)=\operatorname{dist}
 \left(2\sqrt{Xuv},\mathbb Z+\tfrac12\right),\qquad
 \delta_X=(10\log(2X))^{-1}.
\]

For each literal middle or lower hard-M1 residual shell and each
\(\sigma\in\{+1,-1\}\), the reviewed claim is

\[
\left|
 \sum_{\substack{(u,v)=1,\ v\ \mathrm{odd},\ 4u<v<16u\\
                   s(u,v)>L,\ \Delta_X(u,v)\geq\delta_X}}
 \chi_4(v)
 \sum_{\substack{G\geq G_0,\ G\ \mathrm{odd}\\G\rho(u,v)<T_L}}
 \chi_4(G)a_{L,X}^{\rm lit,\sigma}(Gu,Gv)
 e\!\left(\sigma G\sqrt{Xuv}\right)
\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon .                 \tag{R183.C1}
\]

This is not the complete small-\(t\) owner.  It is a split of the exact
divisor incidences inside that owner; a graph statement must retain that
incidence-level qualification.

## Line-level proof checks

1. **Primitive-ray bijection (report lines 203--229): GREEN.**  Every
   literal incidence has the unique data
   \(G=(h,n),u=h/G,v=n/G\), and conversely \((G,u,v)\) reconstructs that
   incidence.  Since \(n\) is odd, both \(G\) and \(v\) are odd.  As
   \(G^2\) is a square,
   \(\operatorname{sf}(hn)=\operatorname{sf}(uv)\), and
   \(hn=s(u,v)(G\rho(u,v))^2\).  Thus the inherited conditions are exactly
   \(s(u,v)>L\) and \(G\rho(u,v)<T_L\); no multiplicity is lost.

2. **Character and phase algebra (lines 210--228): GREEN.**  Complete
   multiplicativity on the odd integers gives
   \(\chi_4(Gv)=\chi_4(G)\chi_4(v)\), without requiring \((G,v)=1\).
   Also \(\sqrt{Xhn}=G\sqrt{Xuv}\).  Both identities hold signwise and
   preserve the literal coefficient before any absolute value.

3. **Uniform step-two BV (lines 231--269): GREEN.**  This was the critical
   seam and was rederived independently.  Up to a shell normalizer and a
   fixed sign constant, both independent of \(G\), the accepted hard-M1
   stationary symbol on a ray has the form

   \[
   \eta_L(Gu)\Phi\!\left(\frac{Gu}{H+1}\right)
   W\!\left(\sqrt{\frac{4q_Xu}{v}}\right)
   (G^2uv)^{-3/4}
   \]

   times the literal support, residual-label, floor, star, half-weight,
   and endpoint fields.  The \(W\)-argument, ratio tests, hard sample, and
   sign field are constant on a fixed ray.  The accepted dyadic profile
   has normalized integer BV, and sampling it at \(Gu\) for consecutive
   odd \(G\) cannot increase variation:

   \[
   \sum_{G\ \mathrm{odd}}
   |\eta_L((G+2)u)-\eta_L(Gu)|
   \leq \sum_m|\eta_L(m+1)-\eta_L(m)|\ll1.
   \]

   The \(C^1\) bound for \(\Phi\), the facts \(Gu\asymp L\) and
   \(L\leq H\), give

   \[
   \sum_{G\ \mathrm{odd}}
   \left|\Phi\!\left(\frac{(G+2)u}{H+1}\right)
             -\Phi\!\left(\frac{Gu}{H+1}\right)\right|
   \ll {u\over H+1}\left(1+{L\over u}\right)\ll1.
   \]

   The normalized \(G^{-3/2}\) factor is monotone and has endpoint plus
   total variation bounded by its normalized supremum.  Finally,
   \(G\geq G_0\), \(G\rho<T_L\), the frequency shell, and height
   truncation are interval masks on the odd \(G\)-lattice.  Strict
   inequalities merely determine which endpoint is included.  Each mask
   contributes at most two jumps.  The fixed finite collection of star or
   half-weight traces contributes only bounded endpoint jumps.  The
   discrete product rule therefore proves the asserted
   \(\|w_{u,v}^\sigma\|_{BV_2}\ll_\varepsilon X^\varepsilon\).

4. **Real-\(X\) crossings and zero extension (lines 258--269): GREEN.**
   For each real \(X\), the floors \(y=\lfloor\sqrt X\rfloor\) and \(H\)
   and the value \(q_X\) are fixed.  A crossing can change an interval
   endpoint or the constant ray value of the \(W\)-factor, but cannot
   create repeated \(G\)-oscillation.  Zero extension includes the entry,
   exit, equality, star, and half-weight jumps in the BV norm.  The
   constants above are independent of the location of those jumps, so the
   proof is uniform across crossings and for both signs.

5. **Primitive-ray cancellation (lines 271--308): GREEN.**  For
   \(G=2k+1\),

   \[
   {\chi_4(G+2)e(\sigma(G+2)\alpha)
    \over\chi_4(G)e(\sigma G\alpha)}
   =-e(2\sigma\alpha),\qquad \alpha=\sqrt{Xuv}.
   \]

   Hence the geometric partial sums are bounded by
   \(O(\Delta_X(u,v)^{-1})\).  The distance is unchanged by
   \(\sigma\mapsto-\sigma\).  Abel summation with the verified BV norm
   proves the per-ray bound \(O_\varepsilon(\delta^{-1}X^\varepsilon)\).

6. **Restored power (lines 311--326): GREEN.**  A nonempty ray with
   \(G\geq G_0\) has \(u\ll L/G_0\); the strict cone has only \(O(u)\)
   possible \(v\)'s.  Thus there are
   \(O((1+L/G_0)^2)\) rays.  Taking positivity only after the per-ray
   character-phase saving yields

   \[
   \delta_X^{-1}X^\varepsilon(1+L/G_0)^2
   \ll_\varepsilon L^{3/2}X^\varepsilon.
   \]

   This distinguishes the literal theorem from the arbitrary-coefficient
   incidence capacity \(O(L^2/G_0)=O(L^{7/4})\).

7. **Exact complement and mandatory \(t=1\) face (lines 107--119 and
   372--393): GREEN.**  Inside all original literal conditions, the
   complement of (R183.C1) is exactly

   \[
   \{G<G_0\}\ \dot\cup\
   \{G\geq G_0:\Delta_X(u,v)<\delta_X\}.
   \tag{R183.C2}
   \]

   Equality in the resonance test belongs to the proved sector.  If the
   small-\(t\) range contains \(t=1\), then
   \(t=G\rho=1\) forces \(G=\rho=1\), and \(G<G_0\); hence the entire
   coprime squarefree \(t=1\) face remains in (R183.C2).  For the vacuous
   edge case \(T_L=1\), there is no \(t=1\) summand to assign.

8. **One final absolute value and false controls: GREEN.**  The sector is
   one signed aggregate.  The proof takes a positive ray sum only after
   obtaining the needed actual \(\chi_4(G)\)-phase cancellation on each
   ray.  If \(\chi_4(G)\) is erased, the chosen half-integer
   nonresonance condition does not prevent \(e(2\sigma\alpha)=1\); a
   dechirped arbitrary coefficient also restores capacity.  These are
   mechanism controls, not literal lower bounds.

9. **One-prime orientation identity (lines 328--370): GREEN at its stated
   scope.**  For a chosen odd \(p\equiv3\pmod4\) dividing a squarefree
   \(t=1\) fibre, moving \(p\) between the two factors reverses the
   character.  It sends \(z=n/h\in(4,16)\) to either \(z/p^2<4\) or
   \(zp^2>16\), so the two zero-extended supports are disjoint and the
   half-difference identity is exact.  It is a local self-return
   observation, not a universal estimate for fibres lacking such a prime.

## Sibling-report consistency controls

- The exact Möbius kernel and self-return in
  `partial_mobius_shifted_correlation_barrier_audit.md` preserve both
  strict cutoffs and do not conflict with the incidence split above.  Its
  target-safe transformed tail is not a disjoint literal sector and is not
  being promoted by this review.
- The statement-only report independently recovers the product flattening,
  \(L^2\) arbitrary-coefficient capacity, mandatory \(t=1\) obstruction,
  exact Möbius kernel, and fixed-row connector.  As it explicitly lacked
  the literal coefficient formula, it neither proves nor refutes the BV
  seam; the direct verification above supplies that missing check.

## First unproved seam

No defect was found in (R183.C1).  The first unproved seam toward the
frozen owner is exactly (R183.C2): the small-gcd part contains the entire
\(t=1\) cone, and the large-gcd near-half-integer-resonant part has no
proved literal metric or signed correlation estimate.  Therefore the
complete estimate (183.ST) remains open.

## Control outcomes

| Control | Outcome |
|---|---|
| Exact zero-extended divisor coefficient | **Pass.** No envelope or separable substitute is introduced. |
| Product regrouping and multiplicity | **Pass.** The incidence-to-ray map is bijective. |
| Squarefree coordinates and small-\(t\) cutoff | **Pass.** \(s=\operatorname{sf}(uv)\), \(t=G\rho\), and \(G\rho<T_L\) exactly. |
| \(\chi_4\) factorization | **Pass.** Both factors are odd and complete multiplicativity applies. |
| Uniform literal step-two BV | **Pass.** All varying factors and zero-extension jumps are controlled as above. |
| Strict cone and shell endpoints | **Pass.** Their equality conventions are retained by interval masks. |
| Floors, stars, half weights, and real-\(X\) crossings | **Pass.** Fixed or finite endpoint traces; no hidden ray oscillation. |
| Both signs | **Pass.** The same resonance distance controls \(\sigma=\pm1\). |
| Exact sector complement | **Pass at incidence level.** Equation (R183.C2) is disjoint and exhaustive. |
| Mandatory \(t=1\) | **Pass/open.** It is retained wholly in the unproved complement whenever nonvacuous. |
| One outer absolute value | **Pass.** Positivity is used only after target-strength ray cancellation. |
| Owner and exponent scope | **Pass.** The full owner, all parents, bridges, and exponent claims remain untouched. |

No numerical experiment and no external theorem were used.

## Dependencies and exact artifacts used

The review used the assigned brief; `protocol.md`;
`state/proof_obligations.yml`; `state/active_campaign.yml`;
`strategy/round183_m1_hard_top_high_radical_small_t_signed_contraction_strategy.md`;
`proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`;
and all three Round-183 reports.  To reproduce the literal ray factorization
rather than accept it by name, the review also checked the accepted graph
evidence containing the exact hard-M1 stationary formula and normalized-BV
frequency profile:
`rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_algebra.md`
and
`rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`.

## Narrowest allowed state effect

Subject to the remaining independent Round-183 seams, the narrowest
permissible promotion is a subordinate **proved internal incidence-level
strict sector** recording (R183.C1), together with the exact complement
(R183.C2).  It must not be restated as a theorem for a subset of product
indices unless the split coefficient is defined explicitly.

Keep `M9-M1-hard-top-high-radical-small-t-residual-estimate` open.  Do not
promote `M9-M1-top-endpoint-signed-cone`, the smooth M1 parent, M9--M1, any
M2 node, endpoint uniformity, M9, either bridge, the Gauss-circle target,
or any exponent.  At this seam the compatible round label is
`strict_hard_m1_small_t_sector`.
