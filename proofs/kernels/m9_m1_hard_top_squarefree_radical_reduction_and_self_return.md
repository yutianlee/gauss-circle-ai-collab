# Hard-M1 squarefree-radical sector reduction and self-return

- Source campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Source task: `conductor_formalization`
- Role: durable proved-kernel candidate
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Exact context files:
  protocol.md; state/proof_obligations.yml; state/active_campaign.yml;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/candidates/formalized_hard_m1_squarefree_radical_reduction.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_high_radical_signed_attack.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_radical_connector_capacity_audit.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/blind_hard_m1_radical_rederivation.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/independent_reduction_and_self_return_review.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/literal_scope_capacity_owner_review.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/blind_post_unmask_radical_review.md;
  rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_connector_and_route_scope.md;
  and rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md
- Direct dependencies: `M9-M1-top-endpoint-transform`,
  `H4-Phi-regularity`, `M9-M2-dyadic-weight-nondegeneracy`, and
  `Divisor-bound-elementary`
- Claimant/review status: conductor synthesis; pending final kernel review
  and State Patch validation

## Statement

For a literal residual shell of the unique hard M1 profile and a fixed
frequency sign \(\sigma\in\{+1,-1\}\), write

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_{h\asymp L}\sum_{\substack{4h<n<16h\\n\ {\rm odd}}}
 \chi_4(n)a_{L,X}^{\rm lit,\sigma}(h,n)e(\sigma\sqrt{Xhn})
 =\sum_{\substack{s\ge1\\\mu^2(s)=1}}\sum_{t\ge1}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}),
\]

where (r=st^2) is the unique squarefree-kernel decomposition and the
complete literal symbol is zero-extended before product regrouping. Then:

1. if (G=(h,n)), uniquely
   (h=Gda^2), (n=Geb^2), (s=de), (t=Gab), with (d,e)
   squarefree and ((da,eb)=1); hence (G\mid t);
2. (st^2\asymp L^2), so (s\ll L^2), and (s>L) implies
   (t\ll\sqrt L);
3. the union of (s\le L) and
   (s>L, t\ge\lceil\sqrt L\rceil) is target-safe by absolute
   incidence counting at (O_\varepsilon(L^{3/2}X^\varepsilon));
4. the exact complement is (s>L) and
   (1\le t<\lceil\sqrt L\rceil), whose (t=1) face is the complete
   coprime squarefree literal cone;
5. complete squarefree Möbius linearization equals the original hard cone
   plus an (O_\varepsilon(L^{3/2}X^\varepsilon)) low-radical correction;
   joint ((s,t)) lifting is only a permutation of product indices; and
6. central full-divisor Mellin cancellation at primes
   (3\bmod4) does not control the noncentral modes required by the
   literal truncated cone.

Thus the remaining small-(t) theorem still needs the full factor
(L^{1/2}) at (t=1). The reduction and self-return are exact, but the
remaining literal signed estimate is open.

## Proof

Group the finite cone by (r=hn). Prime-exponent parity gives the unique
(r=st^2). After removing (G=(h,n)), write the coprime factors uniquely
as (h/G=da^2), (n/G=eb^2), with (d,e) squarefree. This proves the
parametrization and (G\mid t). The fixed cone has (hn\asymp L^2),
giving the support relations.

The bounded normalized symbol and divisor multiplicity give
(|C_{L,X}^{\sigma}(r)|\ll_\varepsilon X^\varepsilon). For (s\le L), there
are (O(1+L/\sqrt s)) possible (t), hence total capacity
(O_\varepsilon(L^{3/2}X^\varepsilon)). For fixed (t), there are
(O(1+L^2/t^2)) possible (s); summing over
(\lceil\sqrt L\rceil\le t\ll\sqrt L) proves the second safe sector.

For the Möbius identity put
(F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})). Since
(\mu^2(s)=\sum_{a^2\mid s}\mu(a)), the high-radical sum is

\[
 \sum_{b,u}F_\sigma(bu^2)
 \sum_{\substack{a\mid u\\a^2b>L}}\mu(a).
\]

For (b>L) the inner sum is (\mathbf1_{u=1}). Hence the exact all-(L)
self-return is

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF_\sigma(st^2)
 =\mathcal T_{L,\sigma}^{M1}+E_{L,\sigma},
 \qquad
 E_{L,\sigma}=\sum_{\substack{b\le L\\u\ge1}}K_L(b,u)F_\sigma(bu^2)
      -\sum_{r\le L}F_\sigma(r),
\]

where (K_L(b,u)=\sum_{a\mid u,\ a^2b>L}\mu(a)). On the product support,
(u\asymp L/\sqrt b), while (|K_L(b,u)|\le\tau(u)) and
(|F_\sigma(bu^2)|\ll_\varepsilon X^\varepsilon). Thus
(E_{L,\sigma}\ll_\varepsilon L^{3/2}X^\varepsilon); the last sum is only
(O_\varepsilon(LX^\varepsilon)) and vanishes on sufficiently large
nontrivial shells. This proves the self-return without an implicit
large-(L) shortcut.
The joint-coordinate and Mellin statements follow from the unique
product reindexing and the finite local factor

\[
 r^{-i\tau}\prod_{p^k\parallel r}
 \sum_{j=0}^k\chi_4(p)^jp^{2ij\tau}.
\]

At (p\equiv3\pmod4) an odd exponent kills only (\tau=0); the full
inverse Mellin integral retains noncentral frequencies. No target bound
for the literal small-(t) complement follows.

## Scope

The strict sectors are proved internally and the named automatic
mechanisms are parked. Coefficient-uniform capacity and dechirped controls
are not literal lower bounds. A bound for the exact small-(t) complement
for every hard shell and both signs would first prove
M9-M1-top-endpoint-signed-cone; the accepted transform would then discharge
only the hard residual child of M9-M1-physical-one-count-assembly. That
complement, the hard signed-cone owner, the independent smooth direct-M1
parent, GAR, M9-M1, M9-M2, endpoint uniformity, M9, both bridges, the
quarter theorem, and all exponents remain unchanged.
