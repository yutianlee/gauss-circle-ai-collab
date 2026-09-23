# Hard-M1 small-t primitive-ray sector and truncated-Mobius self-return

- Source campaign:
  `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Source task: `conductor_formalization`
- Role: durable proved-kernel candidate
- Generated: `2026-08-27T20:10:40.7471107+08:00`
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Direct graph dependencies:
  `M9-M1-hard-top-squarefree-radical-sector-reduction`,
  `M9-M1-top-endpoint-transform`,
  `M9-M1-frequency-phase-diagram-R10`, `H4-Phi-regularity`, and
  `Divisor-bound-elementary`
- Exact source candidate:
  `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/candidates/formalized_hard_m1_small_t_primitive_ray_sector_and_self_return.md`
  (SHA-256
  `e23d4135401c81c263026fddf19df4d46536eaabaa33fa9a7a0d8b287ea82f91`)
- Exact GREEN validation evidence:
  `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/coefficient_product_endpoint_seam_review.md`
  (SHA-256
  `30239761d7b1055e4d7a86efbee12c5a104e8aa2a3edd6462276b16d718e4af9`);
  `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/power_self_return_psc_seam_review.md`
  (SHA-256
  `9e562c8c60d7f336131fb5ec7e75e5af2b26dfcd2eaba376f73840cc00aa8405`);
  and
  `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/blind_post_unmask_owner_scope_review.md`
  (SHA-256
  `d81bb22fdf5ebd98134c485624b68c9a067c347d0d1c94c40dcbc3d2385b87f3`)
- Claimant/reviewer status: conductor formalization; the three named
  mathematical seams are GREEN; pending bounded post-repair provenance
  verification and State Patch validation

## Statement

Fix real \(X\geq2\), put

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]

fix one literal middle or lower residual hard-M1 shell \(L\), and let
\(\sigma\in\{+1,-1\}\).  Zero-extend the actual literal symbol
and expand the exact coefficient

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\r/h\ \mathrm{odd}\\
                   4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h)
\]

inside the high-radical small-\(t\) aggregate.  For each literal incidence
write \(h=Gu,n=Gv\), where \(G=(h,n)\) and \((u,v)=1\), and put

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{uv/s(u,v)},\qquad
 t=G\rho(u,v).
\]

Let

\[
 T_L=\lceil\sqrt L\rceil,\quad
 G_0=\lceil L^{1/4}\rceil,\quad
 \delta_X=(10\log(2X))^{-1},\quad
 \Delta_X(u,v)=\operatorname{dist}
 (2\sqrt{Xuv},\mathbb Z+\tfrac12).
\]

Then the literal incidence sector

\[
\begin{aligned}
 \sum_{\substack{(u,v)=1,\ v\ \mathrm{odd},\ 4u<v<16u\\
                   s(u,v)>L,\ \Delta_X(u,v)\geq\delta_X}}
 \chi_4(v)
 \sum_{\substack{G\geq G_0,\ G\ \mathrm{odd}\\G\rho(u,v)<T_L}}
 \chi_4(G)a_{L,X}^{\mathrm{lit},\sigma}(Gu,Gv)
 e(\sigma G\sqrt{Xuv})
\end{aligned}
\]

is \(O_\varepsilon(L^{3/2}X^\varepsilon)\), uniformly for both signs and
all literal endpoints.  Its exact incidence complement is

\[
 \{G<G_0\}\ \dot\cup\
 \{G\geq G_0:\Delta_X(u,v)<\delta_X\},
\]

with every original predicate retained; it contains the complete
\(t=1\) face.

Moreover, if
\(F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})\) and
\(T=T_L\), then the exact small-\(t\) Mobius kernel is

\[
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a).
\]

It equals \(\mathbf1_{u=1}\) on \(b>L,u<T\).  Hence the complete
small-\(t\) aggregate and also its \(a<T\) Mobius core equal the full
literal product wave \(\sum_rF_\sigma(r)\), modulo
\(O_\varepsilon(L^{3/2}X^\varepsilon)\); the \(a\geq T\) tail is
target-safe.  This is a scoped self-return, not a disproof of the remaining
literal estimate.

## Proof

The incidence map is bijective and gives

\[
 hn=G^2uv=s(u,v)(G\rho(u,v))^2,
 \quad
 \chi_4(Gv)=\chi_4(G)\chi_4(v),
 \quad
 e(\sigma\sqrt{Xhn})=e(\sigma G\sqrt{Xuv}).
\]

On a fixed ray, the ratio-dependent transformed weight and support are
constant.  Let \(\eta_L\) be the accepted scale-normalized-BV dyadic
profile, including its literal shell endpoint weights, and define

\[
 \Psi_{H,L}(m)=\mathbf1_{1\leq m\leq H}\eta_L(m)
 \Phi\!\left(\frac m{H+1}\right)
\]

on the integers, with zero extension.  The normalized power has monotone
\(G^{-3/2}\) variation.  On the active interval, \(Gu\asymp L\),
\(L\leq H\), and

\[
 \sum_{\substack{G\ \mathrm{odd}\\
                   Gu,(G+2)u\in[1,H]}}
 \left|\Phi\!\left(\frac{(G+2)u}{H+1}\right)
 -\Phi\!\left(\frac{Gu}{H+1}\right)\right|
 \ll \frac{u}{H+1}\left(1+\frac Lu\right)\ll1.
\]

Sampling the normalized-BV profile cannot increase variation; the
discrete product rule and the two zero-extension boundary jumps give

\[
 \sum_{G\ \mathrm{odd}}
 |\Psi_{H,L}((G+2)u)-\Psi_{H,L}(Gu)|\ll1.
\]

All remaining literal fields are fixed on the ray or contribute only the
entry and exit jumps of a fixed finite interval partition.  Thus the
complete zero-extended ray weight has step-two
\(BV\ll_\varepsilon X^\varepsilon\).  Consecutive odd \(G\)'s in the
character-phase progression have ratio

\[
 -e(2\sigma\sqrt{Xuv}),
\]

so Abel summation gives
\(O_\varepsilon(\delta_X^{-1}X^\varepsilon)\) per nonresonant ray.  A
nonempty ray with \(G\geq G_0\) has \(u\ll L/G_0\) and \(v\asymp u\),
so there are \(O((1+L/G_0)^2)=O(L^{3/2})\) such rays.  Since
\(\delta_X^{-1}\ll_\varepsilon X^\varepsilon\), the claimed sector bound
follows.  Splitting at \(G_0\) and at the strict resonance inequality gives
the exact complement; \(t=1\) forces \(G=\rho=1\).

For the Mobius identity, expand
\(\mu^2(s)=\sum_{a^2\mid s}\mu(a)\), write \(s=a^2b\), and put \(u=at\).
This gives the displayed kernel.  When \(b>L,u<T\), every divisor of
\(u\) passes both cutoffs, proving
\(K_{L,T}(b,u)=\sum_{a\mid u}\mu(a)=\mathbf1_{u=1}\).  Product support
\(bu^2\asymp L^2\), the divisor bound, and

\[
 \sum_{b\leq L}(1+L/\sqrt b)\ll L^{3/2},
 \qquad L^2\sum_{u\geq T}u^{-2}\ll L^{3/2}
\]

show that the other two regions are target-safe.  If the Mobius divisor is
first split at \(a=T\), the large part is

\[
 \ll_\varepsilon X^\varepsilon L^2
 \sum_{a\geq T}a^{-2}\sum_{t\geq1}t^{-2}
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

while the small-part kernel still equals \(\mathbf1_{u=1}\) on
\(b>L,u<T\).  Hence the small core self-returns to the full product wave.

## Scope

The positive theorem is an incidence-level strict sector, not a theorem
for a subset of products.  Its coefficient-insensitive capacity is only
bounded by \(O(L^{7/4})\), while the actual character-phase argument earns
the target bound.  The small-gcd and near-half-integer-resonant complement,
including all \(t=1\), remains open.  A fixed-row Fejer correlation theorem
would be sufficient but is unproved and stronger than the owner; its
quadratic radical-shift interface is not the old centered linear-fibre PSC.

No hard parent, smooth M1 parent, GAR, M9-M1, M2 obligation, endpoint
uniformity, M9, bridge, theorem, or exponent follows from this kernel.
