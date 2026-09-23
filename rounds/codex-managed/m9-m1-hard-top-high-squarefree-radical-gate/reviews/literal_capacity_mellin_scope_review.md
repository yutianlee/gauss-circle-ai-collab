# Round 181 literal-capacity, Möbius, and Mellin scope review

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `high_radical_actual_direction_and_capacity`
- Role: conductor hostile mechanism/scope review
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Context: all Round-181 reports and reviews, the formal candidate, the
  repaired durable kernel, and the earlier product-fibre, rank-one,
  ordered-cell, lower-squarefree, and canonical-Gram obstructions
- Review status: **GREEN for mechanism-scoped obstruction; literal target
  remains open**

## 1. Result

The exact all-(L) Möbius identity returns the complete literal
high-radical aggregate to the original hard product wave modulo a
target-safe correction. The joint ((s,t)) lift is a permutation of
product indices. Coefficient-uniform capacity is (L^2X^\varepsilon),
already on (t=1), but this is not literal lower mass. Central Mellin
cancellation controls only one full-divisor mode and not the truncated
literal cone. These are rigorous boundaries for the named mechanisms, not
a disproof of a new coefficient-sensitive signed theorem.

## 2. Exact statement and hypotheses

Put

\[
 F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr}),\qquad
 K_L(b,u)=\sum_{\substack{a\mid u\\a^2b>L}}\mu(a).
\]

All sums are finite after literal zero extension. Then

\[
 \mathcal H_{L,\sigma}:=
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF_\sigma(st^2)
 =\sum_{b,u}K_L(b,u)F_\sigma(bu^2).
\tag{181.S1}
\]

For every (L),

\[
 \mathcal H_{L,\sigma}=\mathcal T_{L,\sigma}^{M1}+E_{L,\sigma},
\]

\[
 E_{L,\sigma}=
 \sum_{\substack{b\leq L\\u\geq1}}K_L(b,u)F_\sigma(bu^2)
 -\sum_{r\leq L}F_\sigma(r),
 \qquad
 E_{L,\sigma}\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{181.S2}
\]

## 3. Proof and scope

Insert (mu^2(s)=\sum_{a^2\mid s}\mu(a)), write (s=a^2b), and set
(u=at). This proves (181.S1). When (b>L), every divisor (a\mid u)
is admitted, so (K_L(b,u)=\sum_{a\mid u}\mu(a)=\mathbf1_{u=1}).
Adding and subtracting (sum_{r\leq L}F_\sigma(r)) gives (181.S2).
On support (bu^2\asymp L^2), so (u\asymp L/\sqrt b), while
(|K_L(b,u)|\leq\tau(u)) and
(|F_\sigma(bu^2)|\ll_\varepsilon X^\varepsilon). Summation over
(b\leq L) proves the displayed error bound. This repairs the only
large-shell shortcut in the initial candidate.

The map (r\leftrightarrow(s,t)) is bijective, so a positive joint-(t)
norm has unchanged capacity. At (t=1), the exact parametrization forces
(G=a=b=1); an odd squarefree-coprime interior cone has positive density.
Sitewise dechirping attains (L^2) for arbitrary bounded coefficients.
It does not describe the fixed literal coefficient.

For a full smooth divisor orientation, the Mellin fibre is

\[
 D_r(\tau)=r^{-i\tau}\prod_{p^k\parallel r}
 \sum_{j=0}^k\chi_4(p)^jp^{2ij\tau}.
\]

An odd (p\equiv3\pmod4) exponent kills the central mode only. The
literal ratio cutoff requires all inverse-Mellin modes and endpoint
pieces; exact recombination restores the original coefficient. Thus only
central-mode-only, positive remainder, or complete inversion/recombination
closures are parked.

## 4. First doubtful or unproved step

No literal (L^{1/2}) contraction is proved for the small-(t) residual,
especially (t=1). A uniform fixed-(t) bound of size
((L^2/t^2)^{3/4}X^\varepsilon) would suffice after summing (t), but it
is not a consequence of support or coefficient size and is stronger than
the required aggregate theorem.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact all-(L) Möbius correction | **PASS.** Includes the (-\sum_{r\leq L}F(r)) term. |
| Joint-(t) orthogonality | **FAIL as automatic mechanism.** It is a reindexing. |
| (G\mid t) gain | **FAIL as automatic mechanism.** The (t=1) cone remains full-dimensional. |
| Arbitrary-coefficient/dechirped capacity | **PASS as a method control only.** No literal lower bound. |
| Character erasure | **FAIL for literal proof.** It discards the only possible arithmetic direction. |
| Central Mellin zero | **PASS at \(\tau=0\) only; FAIL as a literal-cone theorem.** |
| Fixed-(t) (3/4) estimate | **PASS as sufficient bookkeeping; unproved.** |
| No-repeat and downstream scope | **PASS.** No parent or exponent promotion. |

No numerical experiment or external theorem is used.

## 6. Dependencies and artifacts

This review uses the formal candidate, repaired durable kernel, all three
reports, the independent and blind seam reviews, and the accepted
`M9-M1-near-product-fiber-capacity-no-go`,
`M9-M1-ordered-cell-Bprocess-capacity-no-go`,
`M9-M1-lower-cone-squarefree-linearization-obstruction`,
`M9-M1-canonical-Gram-route-scope-obstruction`, and direct minimax ledger.

## 7. Recommended state effect

Promote one subordinate mechanism-scoped obstruction containing (181.S1)--
(181.S2), joint-coordinate self-return, central-Mellin scope, and universal
(t=1) capacity. Do not mark the literal residual false. Reject only the
named automatic closures and preserve all broader open owners.
