# Formalized Round-181 hard-M1 squarefree-radical reduction

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `conductor_formalization`
- Role: conductor-owned formal proof kernel candidate
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Exact context files:
  protocol.md; state/proof_obligations.yml; state/active_campaign.yml;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_high_radical_signed_attack.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_radical_connector_capacity_audit.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/blind_hard_m1_radical_rederivation.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/independent_reduction_and_self_return_review.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/literal_scope_capacity_owner_review.md;
  rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/blind_post_unmask_radical_review.md;
  rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_connector_and_route_scope.md;
  and rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md
- Direct dependencies: M9-M1-top-endpoint-transform,
  H4-Phi-regularity, M9-M2-dyadic-weight-nondegeneracy, and
  Divisor-bound-elementary
- Claimant/review status: conductor synthesis; candidate evidence only,
  pending final kernel review and State Patch validation

## 1. Literal cone and exact product coordinates

Fix one residual shell (L) of the unique hard M1 profile and one
frequency sign (\sigma\in\{+1,-1\}). Extend the complete normalized
literal symbol (a_{L,X}^{\sigma}(h,n)) by zero off its exact support and
put

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_{h\asymp L}\sum_{\substack{4h<n<16h\\n\ {\rm odd}}}
 \chi_4(n)a_{L,X}^{\sigma}(h,n)e(\sigma\sqrt{Xhn}),
\]

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                   r/h\ {\rm odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\sigma}(h,r/h).
\]

Then, exactly,

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_r C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})
 =\sum_{\substack{s\ge1\\\mu^2(s)=1}}\sum_{t\ge1}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\tag{181.C1}
\]

The representation (r=st^2), (\mu^2(s)=1), is unique. If
(G=(h,n)), there are unique squarefree (d,e) and positive (a,b)
such that

\[
 h=Gda^2,\qquad n=Geb^2,\qquad
 s=de,\qquad t=Gab,\qquad (da,eb)=1.
\tag{181.C2}
\]

In particular (G\mid t). Since (hn\asymp L^2), every nonzero term
satisfies

\[
 s\asymp \frac{L^2}{t^2},\qquad s\ll L^2,
 \qquad s>L\Longrightarrow t\ll\sqrt L.
\tag{181.C3}
\]

All identities retain both frequency signs, (\chi_4), the Vaaler taper,
the hard denominator profile, normalized powers, strict cone edges,
floors, stars and half weights, the hard sample, real-(X) crossings, and
zero extensions.

## 2. Target-safe sectors and exact complement

The normalized symbol is bounded on the fixed cone, so

\[
 |C_{L,X}^{\sigma}(r)|\ll_\varepsilon X^\varepsilon
\tag{181.C4}
\]

by divisor multiplicity. Therefore

\[
 \sum_{\substack{s\le L\\\mu^2(s)=1}}\sum_t
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\tag{181.C5}
\]

and, with (T_L=\lceil\sqrt L\rceil),

\[
 \sum_{\substack{s>L,\ \mu^2(s)=1\\t\ge T_L}}
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{181.C6}
\]

Indeed, (181.C5) follows from
(\sum_{s\le L}(1+L/\sqrt s)\ll L^{3/2}), while for fixed (t) the
number of possible (s) is (O(1+L^2/t^2)); summing this for
(T_L\le t\ll\sqrt L) proves (181.C6).

Thus the only remaining hard-cone theorem is

\[
 \boxed{
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\1\le t<T_L}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{181.C7}
\]

This complement contains (t=1), for which (G=a=b=1) in (181.C2):
it is the complete coprime squarefree literal cone. Its geometric and
coefficient-uniform capacity is (L^2), so the missing factor remains
(L^{1/2}). This capacity is not a lower bound for the literal sum.

## 3. Exact Möbius and joint-coordinate self-return

Let (F(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})) and

\[
 K_L(b,u)=\sum_{\substack{a\mid u\\a^2b>L}}\mu(a).
\]

Finite Möbius inversion gives

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF(st^2)
 =\sum_{b,u}K_L(b,u)F(bu^2).
\tag{181.C8}
\]

For (b>L), (K_L(b,u)=\mathbf1_{u=1}). For every (L), (181.C8) is

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF(st^2)
 =\mathcal T_{L,\sigma}^{M1}+E_{L,\sigma},
\tag{181.C9}
\]

where, exactly,

\[
 E_{L,\sigma}
 =\sum_{\substack{b\le L\\u\ge1}}K_L(b,u)F(bu^2)
  -\sum_{r\le L}F(r),
 \qquad
 |E_{L,\sigma}|\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{181.C9a}
\]

On product support (bu^2\asymp L^2), so for each (b\le L) there are
(O(1+L/\sqrt b)) possible (u), while
(|K_L(b,u)|\le\tau(u)) and (|F(bu^2)|\ll_\varepsilon X^\varepsilon).
The first sum in (181.C9a) is therefore
(O_\varepsilon(L^{3/2}X^\varepsilon)); the second is
(O_\varepsilon(LX^\varepsilon)) and vanishes on all sufficiently large
nontrivial shells. Thus complete
squarefree Möbius linearization returns the original cone modulo the
already-safe low-radical sector.

Likewise (r\leftrightarrow(s,t)) is a bijection. A joint-(t) lift is a
permutation of product indices and has the same positive-norm capacity;
it creates no independent orthogonality.

For a smooth full-orientation ratio piece, Mellin separation gives

\[
 D_r(\tau)=r^{-i\tau}\prod_{p^k\parallel r}
 \sum_{j=0}^k\chi_4(p)^jp^{2ij\tau}.
\tag{181.C10}
\]

The inner polynomial at (p=2) is (1), while the prefactor retains
(2^{-ik\tau}). An odd (p\equiv3\pmod4) occurring to odd exponent
annihilates the central mode (\tau=0), but already for (k=1) its
noncentral factor is (1-p^{2i\tau}), which is not uniformly small.
Keeping only (\tau=0) is not the literal cone; estimating all remaining
modes positively loses the required direction; recombining them is exact
Mellin inversion. This parks only the central-mode/full-divisor shortcut,
not every possible coefficient-sensitive Mellin theorem.

## 4. Conditional owner connector and scope

Equations (181.C5)--(181.C7) would prove
(\mathcal T_{L,\sigma}^{M1}\ll_\varepsilon
L^{3/2}X^\varepsilon) for every residual hard shell and both signs.
This is exactly M9-M1-top-endpoint-signed-cone. The accepted one-sided
transform would then give the physical hard residual block at
(X^{1/4+\varepsilon}), discharging only the hard child of
M9-M1-physical-one-count-assembly.

Equation (181.C7) is open. The independent smooth direct-M1 parent, GAR,
M9-M1, every M2 parent, endpoint uniformity, M9, both bridges, the quarter
theorem, and every exponent implication remain open.
