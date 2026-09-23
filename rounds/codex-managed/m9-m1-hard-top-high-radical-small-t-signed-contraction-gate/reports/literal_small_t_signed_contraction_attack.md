# Round 183 report: literal small-t signed contraction attack

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Task: `literal_small_t_signed_contraction_attack`
- Role: discovery
- Access mode: selected context
- Generated: `2026-08-27T19:43:25.4109560+08:00`
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Status: candidate evidence only; no shared proof-state edit

## 1. Result: a target-safe literal nonresonant primitive-ray sector

The complete frozen estimate (183.ST) is **not proved**.  A strict new
actual-coefficient sector inside it is proved.

For an integer (m), let

\[
 \operatorname{sf}(m)=\prod_{v_p(m)\ {\rm odd}}p.
\]

Expand a contributing literal incidence by

\[
 h=Gu,\qquad n=Gv,\qquad (u,v)=1.
\tag{1.1}
\]

Since (n) is odd, (G) and (v) are odd.  Put

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{\frac{uv}{s(u,v)}}.
\tag{1.2}
\]

Then (\rho(u,v)) is an integer and, exactly,

\[
 hn=G^2uv=s(u,v)\bigl(G\rho(u,v)\bigr)^2,
 \qquad s=s(u,v),\quad t=G\rho(u,v).
\tag{1.3}
\]

Thus (s>L) is independent of (G), while the small-(t) cutoff is the
literal interval condition

\[
 G\rho(u,v)<T_L,\qquad T_L=\lceil\sqrt L\rceil.
\tag{1.4}
\]

Define the sign-independent half-integer resonance distance

\[
 \Delta_X(u,v)
 =\operatorname{dist}\!\left(2\sqrt{Xuv},\,\mathbb Z+\tfrac12\right),
 \qquad
 \delta_X=\frac1{10\log(2X)},
\tag{1.5}
\]

and (G_0=\lceil L^{1/4}\rceil).  Let

\[
\begin{aligned}
 \mathcal A^{\rm ray,nr}_{L,X,\sigma}
 ={}&\sum_{\substack{(u,v)=1,\ v\ {\rm odd}\\
                         4u<v<16u\\
                         s(u,v)>L\\
                         \Delta_X(u,v)\geq\delta_X}}
       \chi_4(v)
       \sum_{\substack{G\geq G_0,\ G\ {\rm odd}\\
                         G\rho(u,v)<T_L}}
       \chi_4(G)a_{L,X}^{\rm lit,\sigma}(Gu,Gv)
       e\!\left(\sigma G\sqrt{Xuv}\right).
\end{aligned}
\tag{1.6}
\]

The literal symbol in (1.6) is zero-extended, so its exact dyadic shell,
profile, strict cone, floor, star, hard-sample, crossing, and endpoint
conditions are all still imposed.  Uniformly for every real (X\geq2),
every literal middle or lower hard-M1 residual shell, and both signs,

\[
 \boxed{
 |\mathcal A^{\rm ray,nr}_{L,X,\sigma}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{1.7}
\]

This is not an absolute-capacity statement.  The corresponding
coefficient-insensitive incidence capacity is

\[
 L^2\sum_{G\geq G_0}G^{-2}
 \ll \frac{L^2}{G_0}\asymp L^{7/4},
\tag{1.8}
\]

whereas the signed primitive-ray argument gives (L^2/G_0^2=L^{3/2}),
up to logarithms.  The saving is produced before positivity by the actual
(chi_4(G)) and product phase.

The exact complementary incidence sector in the frozen aggregate is

\[
 \boxed{
 \{G<G_0\}\ \cup\
 \{G\geq G_0:\Delta_X(u,v)<\delta_X\}.}
\tag{1.9}
\]

All original (s>L), (G\rho<T_L), literal-support, and sign conditions
remain on both pieces.  In particular (t=1) has (G=\rho=1) and lies
wholly in the first part of (1.9).  No estimate for (1.9), and hence no
proof of (183.ST), is claimed.

## 2. Exact statement and hypotheses

Fix (X\geq2), a literal middle or lower residual shell (L) of the
unique hard M1 profile, and
(sigma\in\{+1,-1\}).  Use exactly the zero-extended coefficient
(a_{L,X}^{\rm lit,\sigma}(h,n)) from (183.1).  Its factors are the
literal dyadic frequency cutoff, (Phi(h/(H+1))),
(W(\sqrt{4q_Xh/n})), the normalized (h^{-3/4}n^{-3/4}) powers, and
the fixed profile, floor, star, half-weight, strict-edge, sign,
hard-sample, crossing, and endpoint data.

Thus, with no divisor envelope,

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                   r/h\ {\rm odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\rm lit,\sigma}(h,r/h),
\tag{2.0a}
\]

and the frozen owner is

\[
 \mathcal A_{L,X,\sigma}^{\rm st}
 =\sum_{\substack{s>L,\ \mu^2(s)=1\\1\leq t<T_L}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\tag{2.0b}
\]

The decomposition in (1.6), (1.9) is an exact divisor-incidence
decomposition of (2.0b), not a replacement of its coefficient.

The following step-two variation fact is part of the proof, not an added
arbitrary-weight hypothesis.  For every fixed primitive pair ((u,v)),
put

\[
 w_{u,v}^{\sigma}(G)=
 \mathbf 1_{G\geq G_0}\mathbf 1_{G\rho(u,v)<T_L}
 a_{L,X}^{\rm lit,\sigma}(Gu,Gv)
\quad(G\ {\rm odd}),
\tag{2.1}
\]

and extend it by zero to all odd (G).  Then

\[
 \|w_{u,v}^{\sigma}\|_{BV_2}
 :=\sup_{G\ {\rm odd}}|w_{u,v}^{\sigma}(G)|
   +\sum_{G\ {\rm odd}}
       |w_{u,v}^{\sigma}(G+2)-w_{u,v}^{\sigma}(G)|
 \ll_\varepsilon X^\varepsilon.
\tag{2.2}
\]

The constant is uniform in the shell, (u,v), every real-(X) support
crossing, and both signs.  The proof of (2.2) is given below and uses only
the literal factors just listed and the accepted (C^1) regularity of
(Phi).

With (2.2), the more general quantitative sector bound is

\[
 |\mathcal A^{\rm ray}_{L,X,\sigma}(G_0,\delta)|
 \ll_\varepsilon
 \delta^{-1}X^\varepsilon
 \left(1+\frac{L}{G_0}\right)^2
\tag{2.3}
\]

for (0<\delta\leq1/2), where the sector has
(G\geq G_0) and (Delta_X(u,v)\geq\delta).  Equation (1.7) is
(2.3) with (G_0=\lceil L^{1/4}\rceil) and the fixed,
(\varepsilon)-independent threshold
(delta_X=(10\log(2X))^{-1}); the logarithm is absorbed into
(X^\varepsilon).

## 3. Proof and derivation

### 3.1 Exact primitive-ray regrouping

Expand the coefficient (C_{L,X}^{\sigma}(st^2)) in the frozen sum by
its literal divisor incidences (h n=st^2).  For each incidence take
(G=(h,n)) and define (u=h/G), (v=n/G).  This is a bijection between
literal incidences and triples ((u,v,G)) satisfying (1.1), the literal
support, and (G,v) odd.  Conversely (h=Gu,n=Gv) reconstructs the
incidence and its multiplicity exactly.

Write uniquely (u=da^2), (v=eb^2), with (d,e) squarefree.  Since
((u,v)=1), (de) is squarefree and
(\rho(u,v)=ab).  This proves (1.2)--(1.4), including both strict
cutoffs.  Complete multiplicativity on odd integers gives

\[
 \chi_4(n)=\chi_4(Gv)=\chi_4(G)\chi_4(v),
\tag{3.1}
\]

and the phase is

\[
 e(\sigma\sqrt{Xhn})
 =e\!\left(\sigma G\sqrt{Xuv}\right).
\tag{3.2}
\]

Equations (3.1)--(3.2) prove the exact regrouping (1.6).  No (s)-,
(t)-, divisor-, Mellin-, or Gram norm has been taken.

### 3.2 Uniform step-two variation of the literal ray symbol

On a fixed ray the ratio (n/h=v/u) is constant.  Consequently
(W(\sqrt{4q_Xh/n})=W(\sqrt{4q_Xu/v})) and every strict ratio-support
test is constant along the ray.  The normalized power factor varies as
(G^{-3/2}); on its shell (Gu\asymp L), its endpoint plus total
step-two variation is bounded by a constant times its normalized
supremum.

The Vaaler factor has

\[
 \sum_{G\ {\rm odd}}
 \left|
 \Phi\!\left(\frac{(G+2)u}{H+1}\right)
 -\Phi\!\left(\frac{Gu}{H+1}\right)
 \right|
 \ll \frac{u}{H+1}\left(1+\frac{L}{u}\right)
 \ll 1,
\tag{3.3}
\]

because the residual shell has (L\leq H) and
(|\Phi'\|_\infty<\infty).  The exact dyadic frequency profile has its
accepted scale-normalized bounded variation, including on the hard profile,
by `M9-M1-frequency-phase-diagram-R10`; the exact transformed \(W\),
power, and endpoint fields are those of
`M9-M1-top-endpoint-transform`.  The floors \(y,H\) are fixed once
\(X\) and the shell are fixed.  The hard sample and sign multiplier are
constant on a ray.  The \(W\)-support and strict cone tests depend only on
\(v/u\), hence are also constant on a ray.  The remaining dyadic shell
entries and exits, endpoint stars and half weights, real-\(X\) crossing
equalities, the lower cutoff \(G\geq G_0\), and the upper cutoff
\(G\rho<T_L\) each give only the endpoint jumps of a fixed finite interval
partition.  Zero extension is important here: it includes, rather than
deletes, every such jump.  Together with `H4-Phi-regularity`, these exact
accepted regularity dependencies give (2.2) by the discrete product rule;
the fixed finite literal decomposition and harmless logarithms are
absorbed by \(X^\varepsilon\), signwise.

### 3.3 Character-geometric cancellation on a primitive ray

Write (G=2k+1) and (alpha=\sqrt{Xuv}).  Since
(chi_4(2k+1)=(-1)^k), consecutive odd-(G) terms have the exact ratio

\[
 \frac{\chi_4(G+2)e(\sigma(G+2)\alpha)}
      {\chi_4(G)e(\sigma G\alpha)}
 =-e(2\sigma\alpha).
\tag{3.4}
\]

Therefore every unweighted partial sum over consecutive odd (G) is
bounded by

\[
 \left|
 \sum_{G\in J,\ G\ {\rm odd}}
 \chi_4(G)e(\sigma G\alpha)
 \right|
 \ll
 \min\!\left(|J|,
 \operatorname{dist}(2\sigma\alpha,
                      \mathbb Z+\tfrac12)^{-1}\right).
\tag{3.5}
\]

The distance in (3.5) equals (Delta_X(u,v)) for both signs.  Discrete
Abel summation with (2.2) consequently gives, on every ray with
(Delta_X(u,v)\geq\delta),

\[
 \left|
 \sum_{G\ {\rm odd}}\chi_4(G)w_{u,v}^{\sigma}(G)
 e\!\left(\sigma G\sqrt{Xuv}\right)
 \right|
 \ll_\varepsilon \delta^{-1}X^\varepsilon.
\tag{3.6}
\]

Only after obtaining (3.6) is a positive sum over primitive rays taken.

If a ray in (1.6) is nonempty, the literal shell gives
(Gu\asymp L).  The condition (G\geq G_0) hence implies
(u\ll L/G_0), while (4u<v<16u).  Thus the number of possible
primitive rays is at most

\[
 \sum_{u\ll L/G_0}O(u)
 \ll \left(1+\frac{L}{G_0}\right)^2.
\tag{3.7}
\]

Coprimality, oddness, (s(u,v)>L), (G\rho<T_L), nonresonance, and
literal support only reduce this count.  Summing (3.6) by (3.7) proves
(2.3), and hence (1.7).

### 3.4 Divisor-orientation and noncentral-Mellin stopping seam

The mandatory (t=1) face cannot use the preceding (G)-sum.  Here
(G=a=b=1), so (h,n) are coprime and (hn) is squarefree.  Fix an odd
prime (p\mid hn) and let (iota_p) move (p) from its current side of
((h,n)) to the other side.  It preserves (hn) and the phase.  If
(z=n/h\in(4,16)), then

\[
 z\longmapsto z/p^2<16/9<4
 \quad\hbox{or}\quad
 z\longmapsto zp^2>36>16.
\tag{3.8}
\]

Thus the literal ratio cone and its one-prime translate are disjoint for
every (p\geq3).  If \(p\equiv3\pmod4\), the character changes sign and,
on this squarefree \(t=1\) fibre \(r=hn\), the zero-extended fibre
amplitude \(A_r(h,n)\) satisfies the exact identity

\[
 \sum_{\substack{hn=r\\r\ {\rm squarefree}}}\chi_4(n)A_r(h,n)
 =\frac12\sum_{hn=r}\chi_4(n)
       \bigl(A_r(h,n)-A_r(\iota_p(h,n))\bigr).
\tag{3.9}
\]

But (3.8) makes the two supports in the difference disjoint.  Hence this
local character differencing doubles the (ell^1) boundary capacity
(and multiplies the (ell^2) norm by (\sqrt2)); (3.9) is an exact
self-return, not a contraction.

This is the physical-space form of the noncentral Mellin obstruction.  A
zero of the complete local Euler factor at the single central mode assumes
both (p)-orientations.  The literal cone contains at most one endpoint of
every such local edge, and inverse Mellin recombination restores (3.9).
An internal product-preserving partner can exist only by simultaneously
exchanging factors (p\mid n), (q\mid h), which changes
(z) to (z(q/p)^2).  It requires comparable (p,q) and changes the
literal (Phi), shell, and (W) weights.  No signed comparable-factor
exchange estimate with these weights and all endpoints is proved in the
permitted packet.  This is the first exact failed divisor-orientation seam;
no central-mode-only or positive noncentral-mode estimate is used.

## 4. First doubtful or unproved step

The first unproved step toward the complete owner is the exact complement
(1.9).  It has two qualitatively different parts.

1.  The small-gcd part (G<G_0) contains the entire (G=1), (t=1)
    coprime-squarefree cone.  At (G=1) every primitive ray has only one
    site, so the (chi_4(G)) geometric progression supplies no saving.
    Even an (O(1)) bound per ray leaves (O(L^2)) ray capacity.
2.  On (G\geq G_0), the near-resonant condition
    (Delta_X(u,v)<(10\log(2X))^{-1}) permits the character and phase in
    (3.4) to be coherent across the full available (G)-interval.  No
    literal metric count or signed correlation across these primitive
    products is available at target power.

For (t=1), the first additional structural relation would have to be a
weighted signed estimate across comparable two-factor exchanges (or an
equivalent noncentral-Mellin theorem) that retains
(chi_4(n)), squarefree/coprime support, the literal ratio/profile, the
fixed real centre (X), and all endpoints before positivity.  The
one-prime transfer (3.9) cannot provide it.  Capacity does not show that the
literal complement is large or that (183.ST) is false.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_complete_small_t_aggregate` | **Pass for decomposition; target open.** Equations (1.1)--(1.4) reindex every literal incidence in the frozen aggregate. Only the strict sector (1.6) is estimated. |
| `literal_coefficient_definition_and_zero_extension` | **Pass.** The proof uses (a_{L,X}^{\rm lit,\sigma}(Gu,Gv)) itself. Zero extension owns every support entry, exit, strict edge, and missing site. |
| `every_shell_both_signs_real_X_endpoints` | **Pass.** The BV proof is shellwise and signwise; (3.5) has the same resonance distance for both signs. Real-(X) crossings and endpoint jumps are included in (2.2). |
| `one_outer_absolute_value` | **Pass.** The sector is defined as one signed sum in (1.6). A positive ray sum is taken only after the actual (chi_4(G))-phase gain (3.6). |
| `mandatory_t1_face` | **Pass/open.** Equation (1.9) explicitly retains all of (t=1); no estimate for it is claimed. |
| `capacity_L2_target_L_three_halves` | **Pass.** The complete capacity remains (L^2X^\varepsilon). The new sector has absolute capacity (L^{7/4}) and signed bound (L^{3/2}X^\varepsilon); this is not literal lower mass. |
| `fixed_t_is_stronger_not_owner` | **Pass.** No fixed-(t) three-quarter estimate or rowwise substitute is asserted. |
| `joint_t_no_positive_norm` | **Pass.** Equations (1.1)--(1.4) are a bijective primitive-ray regrouping. Positivity appears only after the character-geometric saving. |
| `divisor_orientation_and_character_retention` | **Pass.** The successful sector uses the exact factor (chi_4(G)chi_4(v)). Equations (3.8)--(3.9) locate the first failed local-orientation seam without erasing the character. |
| `noncentral_Mellin_not_central_mode_only` | **Pass/no-go.** The central zero is not used as an estimate. The disjoint-support transfer identity explains why full noncentral inversion self-returns. |
| `complex_and_real_dechirped_controls` | **Pass as falsifiers.** A nonliteral complex multiplier that cancels (chi_4(G)e(\sigma G\sqrt{Xuv})), or a real sign chosen from its real part, destroys (3.6) and restores row capacity. No arbitrary-coefficient theorem is claimed. |
| `unsigned_and_character_erasure_controls` | **Pass/fail for the false analogue.** Without (chi_4(G)), the ratio in (3.4) is (e(2\sigma\alpha)); the condition (Delta_X\geq\delta_X) does not keep it from (1) (for example (alpha\in\mathbb Z)). Thus (1.7) is genuinely character-dependent. |
| `one_site_one_fibre_and_square_centre_controls` | **Pass.** A one-site ray is bounded by (O(1)) and is counted in (3.7), not presumed to cancel. If (X=y^2), (s(u,v)>L) excludes (uv) square, but no uniform Diophantine gap is asserted; near-resonant rays remain in (1.9). |
| `no_second_B_process_or_canonical_positive_Gram_repeat` | **Pass.** Neither mechanism is invoked. |
| `strict_sector_exact_complement` | **Pass.** Equations (1.6) and (1.9) are disjoint and exhaustive at the divisor-incidence level, with equality assigned to the nonresonant sector. |
| `hard_signed_cone_connector_only` | **Pass.** The result is a subordinate strict sector of the hard small-(t) residual only. It does not estimate the full hard signed cone. |
| `downstream_and_exponent_quarantine` | **Pass.** Smooth M1, GAR, M9--M1, all M2 parents, endpoint uniformity, M9, both bridges, the quarter theorem, and every exponent are unchanged. |
| `no_in_round_pivot` | **Pass.** The report remains on the frozen literal small-(t) owner. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The report used only the assigned packet:

- `protocol.md`;
- `state/proof_obligations.yml`, especially
  `M9-M1-top-endpoint-transform`, `H4-Phi-regularity`,
  `M9-M1-frequency-phase-diagram-R10`,
  `M9-M1-hard-top-squarefree-radical-sector-reduction`,
  `M9-M1-hard-top-high-radical-small-t-residual-estimate`, and
  `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction`;
- `state/active_campaign.yml`;
- `strategy/round183_m1_hard_top_high_radical_small_t_signed_contraction_strategy.md`;
- `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`;
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/candidates/formalized_hard_m1_squarefree_radical_reduction.md`;
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_high_radical_signed_attack.md`;
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/literal_capacity_mellin_scope_review.md`;
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/synthesis.md`; and
- the assigned Round-183 task brief.

The derivation is finite algebra, discrete variation, and a geometric
progression estimate.  No web source or unlisted prior-round artifact was
used.

## 7. Recommended state effect

**Recommended effect: promote only the strict sector (1.6)--(1.7), after
independent coefficient/BV, endpoint, and complement review.**

A subordinate graph fact may record that the complete literal small-(t)
aggregate is target-safe on

\[
 (h,n)=G\geq\lceil L^{1/4}\rceil,
 \qquad
 \operatorname{dist}\!\left(
 2\sqrt{X(h/G)(n/G)},\mathbb Z+\tfrac12\right)
 \geq\frac1{10\log(2X)},
\]

with all original conditions retained.  Record the exact complement
(1.9), the full (t=1) face inside it, and the local one-prime
orientation/Mellin self-return (3.8)--(3.9).

Keep `M9-M1-hard-top-high-radical-small-t-residual-estimate` open.  Do not
promote `M9-M1-top-endpoint-signed-cone`, any M1 or M2 parent, M9, a
bridge, the target theorem, or an exponent.  The appropriate task-level
Round-183 exit recommendation is
`strict_hard_m1_small_t_sector`.
