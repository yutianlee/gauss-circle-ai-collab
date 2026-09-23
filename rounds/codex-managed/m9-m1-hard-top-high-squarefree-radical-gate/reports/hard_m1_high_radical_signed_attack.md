# Round 181 report: hard-M1 high-radical signed attack

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `hard_m1_high_radical_signed_attack`
- Role: discovery
- Access mode: `selected_context`
- Generated brief: `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/briefs/hard_m1_high_radical_signed_attack.md`
- Brief generated: `2026-08-27T08:01:37.561951+00:00`
- Brief graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Status: candidate evidence only; no shared proof-state edit

## 1. Result: a strict sector and a mechanism-scoped self-return

The complete high-squarefree-radical estimate (181.HR) is **not proved**.
Two exact reductions and one strict target-safe sector are proved.

First, if (hn=st^2), with (s) squarefree, and (G=(h,n)), then there
are unique variables

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
\tag{1.1}
\]

where (d,e) are squarefree, ((da,eb)=1), and (Geb) is odd.  In
particular,

\[
 \boxed{(h,n)=G\mid t.}
\tag{1.2}
\]

This keeps the literal character as
(\chi_4(n)=\chi_4(Ge)).  The high-radical condition gives
(t\ll \sqrt L), hence (G\ll\sqrt L), but this is not a power-saving
restriction: the mandatory (t=1) face is exactly (G=a=b=1), and is the
full coprime squarefree cone.

Second, the genuine high-radical sector

\[
 t\geq T_L:=\lceil \sqrt L\rceil
\tag{1.3}
\]

is target-safe by literal incidence counting:

\[
 \boxed{
 \sum_{\substack{s>L,\ \mu^2(s)=1\\t\geq T_L}}
 \left|C_{L,X}(st^2)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon .}
\tag{1.4}
\]

The exact retained complement is (1\leq t<T_L), including (t=1).
Likewise the sub-sector ((h,n)\geq\sqrt L) is target-safe, but it is
contained in the same boundary-scale phenomenon and leaves (G=1).

Third, complete squarefree Möbius linearization preserves the actual
(C_{L,X}) direction but returns to the original hard product wave modulo
a target-safe correction.  If

\[
 F(r):=C_{L,X}(r)e(\sqrt{Xr}),\qquad
 K_L(b,u):=\sum_{\substack{a\mid u\\a^2b>L}}\mu(a),
\tag{1.5}
\]

then, exactly on the finite literal support,

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_{t\geq1}F(st^2)
 =\sum_{b,u\geq1}K_L(b,u)F(bu^2).
\tag{1.6}
\]

For (b>L), (K_L(b,u)=\sum_{a\mid u}\mu(a)=\mathbf1_{u=1}).  Since
the literal product support has (r\asymp L^2>L) (bounded (L) being
trivial), (1.6) becomes

\[
 \boxed{
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF(st^2)
 =\mathcal T_L^{M1}+E_L,\qquad
 |E_L|\ll_\varepsilon L^{3/2}X^\varepsilon .}
\tag{1.7}
\]

Thus this genuinely coefficient-preserving Möbius route is an exact
self-return, not the missing (L^{1/2}) contraction.

The two additional proposed resources also fail at their first exact
seam.  The condition ((h,n)\mid t) leaves (t=G=1) at (L^2)
coefficient-insensitive capacity.  Mellin separation of a smooth ratio
piece gives the exact local factor

\[
 D_r(\tau)=r^{-i\tau}
 \prod_{p^k\parallel r}\sum_{j=0}^k
       \chi_4(p)^j p^{2ij\tau}.
\tag{1.8}
\]

At (\tau=0), a prime (p\equiv3\pmod4) in the squarefree kernel makes
its local factor vanish.  But the literal cone is the complete inverse
Mellin integral.  For (k=1) that local factor is
(1-p^{2i\tau}), which is generically of order one away from the single
central frequency.  There is no central residue and no deletion of the
noncentral modes.  Estimating those modes positively erases the actual
direction; recombining them gives back the literal cone.  Hence central
(1*\chi_4) cancellation supplies neither a uniform (L^{-1/2}) nor a
strict power range.

The appropriate task-level conclusion is therefore
`hard_m1_high_radical_capacity_or_self_return_no_go`, scoped only to
gcd pruning, squarefree Möbius linearization, central-Mellin cancellation,
and treating (t) as an independent averaging variable.  It is not a
disproof of (181.HR).

## 2. Exact statement and hypotheses

Let (X\geq2), (y=\lfloor\sqrt X\rfloor),
(q_X=X/y^2), and (H=\lfloor yX^{-1/4}\rfloor).  Fix one literal
middle or lower residual dyadic frequency shell (I_{L,X}) of the unique
hard M1 profile.  All already owned terminal and isolated
second-derivative sites are absent.  For either literal frequency sign
(\sigma\in\{+1,-1\}), extend the exact normalized symbol
(a_{L,X}^\sigma(h,n)) by zero off its literal support and set

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_{h\in I_{L,X}}
   \sum_{\substack{4h<n<16h\\n\ {\rm odd}}}
   \chi_4(n)a_{L,X}^\sigma(h,n)
   e(\sigma\sqrt{Xhn}),
\tag{2.1}
\]

\[
 C_{L,X}^\sigma(r)=
 \sum_{\substack{h\mid r,\ h\in I_{L,X}\\
                   r/h\ {\rm odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^\sigma(h,r/h).
\tag{2.2}
\]

The superscript is suppressed below.  The graph normalization used in
the Round-181 ledger gives (|a_{L,X}^{\rm lit}(h,n)|\ll1) on each
literal piece; the fixed finite decomposition and harmless logarithms are
absorbed into (X^\varepsilon).  Formula (2.2), rather than a divisor
envelope, is retained until a sector has already been shown target-safe.

There are fixed constants (0<c_0<C_0), independent of the shell, such
that

\[
 h\asymp L,\quad 4h<n<16h
 \quad\Longrightarrow\quad
 c_0L^2<hn<C_0L^2.
\tag{2.3}
\]

All half-open choices, stars, floors, strict cone edges,
(\Phi(h/(H+1))), (W(\sqrt{4q_Xh/n})), normalized powers, real-(X)
support crossings, hard-profile sample, and zero extensions remain inside
(I_{L,X}) and (a_{L,X}^\sigma).  No endpoint is smoothed or moved in
the exact identities below.

Writing (r=st^2) uniquely with (\mu^2(s)=1), define

\[
 \mathcal H_{L,\sigma}
 :=\sum_{\substack{s>L\\\mu^2(s)=1}}
   \sum_{t\geq1}C_{L,X}^\sigma(st^2)
   e(\sigma t\sqrt{Xs}).
\tag{2.4}
\]

The proved assertions are:

1. the multiplicity-one parametrization (1.1) and exact coefficient
   formula (3.2) below;
2. (s\ll L^2), (t\ll L/\sqrt s\ll\sqrt L), and (G\mid t);
3. the fixed-(t) coefficient-insensitive ledger

   \[
   \sum_{\substack{s>L\\\mu^2(s)=1}}
   |C_{L,X}(st^2)|
   \ll_\varepsilon {L^2\over t^2}X^\varepsilon;
   \tag{2.5}
   \]
4. the stronger absolute-mass strict-sector estimate (1.4), hence the signed estimate for either frequency sign;
5. the exact self-return (1.6)--(1.7);
6. the central-Mellin factorization (1.8) for every smooth ratio piece,
   with all nonsmooth literal seams retained as separate pieces.

No assertion is made that the literal sum has (L^2) lower mass.  Every
(L^2) statement below is a coefficient-insensitive upper capacity or an
explicit nonliteral dechirped control.

## 3. Proof and derivation

### 3.1 Product fibres and the unique squarefree coordinates

Regrouping (2.1) by (r=hn) gives, with multiplicity one,

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_rC_{L,X}^\sigma(r)e(\sigma\sqrt{Xr}).
\tag{3.1}
\]

For a contributing pair put (G=(h,n)), (h=Gu), (n=Gv), so
((u,v)=1).  Write uniquely (u=da^2) and (v=eb^2), where (d,e)
are squarefree.  Coprimality gives ((da,eb)=1), hence (de) is
squarefree, and

\[
 hn=G^2de,a^2b^2=(de)(Gab)^2.
\]

Uniqueness of the squarefree kernel therefore forces (s=de) and
(t=Gab).  Conversely these data reconstruct (h,n) and their gcd, so
there is no overcount.  Since (n=Geb^2) is odd,
(G,e,b) are odd and
(\chi_4(n)=\chi_4(Ge)).  Consequently the exact, actual-direction
factorization is

\[
\boxed{
 C_{L,X}(st^2)=
 \sum_{\substack{de=s}}^{\rm ord}
 \sum_{\substack{Gab=t,\ (da,eb)=1\\
                  Geb\ {\rm odd}\\
                  Gda^2\in I_{L,X}\\
                  4da^2<eb^2<16da^2}}
 \chi_4(Ge)
 a_{L,X}^{\rm lit}(Gda^2,Geb^2).}
\tag{3.2}
\]

Every floor, star, endpoint, crossing, and removed owner is still tested
by the zero-extended symbol on the right.  The cone inequalities are
strict and (G) cancels from them exactly.

For (t=1), (3.2) has only (G=a=b=1):

\[
 C_{L,X}(s)=
 \sum_{\substack{de=s,\ e\ {\rm odd}\\
                   d\in I_{L,X},\ 4d<e<16d}}
 \chi_4(e)a_{L,X}^{\rm lit}(d,e).
\tag{3.3}
\]

Thus the first layer is the complete coprime squarefree literal cone.  It
has no (G)-, (a)-, (b)-, or (t)-average from which to obtain the
missing power.

### 3.2 Support, incidence, and the strict large-(t) sector

From (2.3) and (st^2=hn),

\[
 s\asymp {L^2\over t^2}.
\tag{3.4}
\]

Hence (s\ll L^2).  On (s>L), (3.4) gives (t\ll\sqrt L).
Also (1.1) gives (G\mid t), proving the gcd consequence without losing
the character.

Each product (r) has at most (\tau(r)) literal divisor incidences, so

\[
 |C_{L,X}(r)|\ll\tau(r)\ll_\varepsilon X^\varepsilon
\tag{3.5}
\]

on the finite hard support.  For fixed (t), the number of possible
integers (s) in (3.4) is (O(1+L^2/t^2)).  In the nonempty
high-radical range the second term dominates, and (2.5) follows.

Now sum (2.5) for \(t\geq T\):

\[
 \sum_{\substack{s>L,\ \mu^2(s)=1\\t\geq T}}
 |C_{L,X}(st^2)|
 \ll_\varepsilon
 L^2X^\varepsilon\sum_{t\geq T}t^{-2}
 \ll_\varepsilon {L^2\over T}X^\varepsilon.
\tag{3.6}
\]

Taking (T=T_L=\lceil\sqrt L\rceil) proves the absolute-mass statement (1.4), and therefore its signed consequence.  This is an actual
literal-sector estimate; character erasure is harmless only because the
sector has already reached target size.  The complement is exactly
(1\leq t<T_L).

The same calculation in gcd coordinates gives

\[
 \#\{(h,n):h,n\asymp L,\ (h,n)\geq G_0\}
 \ll L^2\sum_{G\geq G_0}G^{-2}
 \ll {L^2\over G_0}.
\tag{3.7}
\]

Thus (G\geq\sqrt L) is target-safe.  For (G<\sqrt L), however, the
sum of the same capacities is (\asymp L^2); in particular (G=1)
remains.  The exact fact (G\mid t) therefore gives no gain on the
mandatory layer.

For comparison, the low-radical calculation is

\[
 \sum_{\substack{s\leq L\\\mu^2(s)=1}}\sum_t
 |C_{L,X}(st^2)|
 \ll_\varepsilon X^\varepsilon
 \sum_{s\leq L}\left(1+{L\over\sqrt s}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{3.8}
\]

This also verifies the absolute correction size used below.

### 3.3 Fixed-(t) power ledger

Put (S_t=L^2/t^2).  The optional stronger Round-181 target asks for
(S_t^{3/4}X^\varepsilon).  Formula (2.5) supplies only
(S_tX^\varepsilon), leaving

\[
 {S_t\over S_t^{3/4}}=S_t^{1/4}
 \asymp {L^{1/2}\over t^{1/2}}.
\tag{3.9}
\]

At (t=1) this is exactly the missing (L^{1/2}).  Summing the desired
fixed-(t) bounds would be lawful because

\[
 \sum_{t\geq1}S_t^{3/4}
 \asymp L^{3/2}\sum_{t\geq1}t^{-3/2}
 \ll L^{3/2},
\tag{3.10}
\]

but (3.9), not (3.10), is the unproved step.  Factoring (t=Gab) in
(3.2) gives only (O_\varepsilon(X^\varepsilon)) divisor layers and no
power; at (t=1) even those layers disappear.

### 3.4 Exact Möbius self-return

All sums below are finite because (F) is zero-extended.  Insert

\[
 \mu^2(s)=\sum_{a^2\mid s}\mu(a)
\]

into the high-radical aggregate and write (s=a^2b), (u=at).  Then

\[
\begin{aligned}
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF(st^2)
 &=\sum_{a,b,t:\ a^2b>L}\mu(a)F\bigl(b(at)^2\bigr)\\
 &=\sum_{b,u}F(bu^2)
   \sum_{\substack{a\mid u\\a^2b>L}}\mu(a),
\end{aligned}
\tag{3.11}
\]

which is (1.6).  If (b>L), every divisor (a\mid u) is admitted, so
the inner sum is (\mathbf1_{u=1}).  The remaining correction has
(b\leq L).  On (bu^2\asymp L^2), one has
(u\asymp L/\sqrt b), while

\[
 |K_L(b,u)|\leq\tau(u),\qquad |F(bu^2)|\ll_\varepsilon X^\varepsilon.
\]

Therefore

\[
 \sum_{b\leq L}\sum_u|K_L(b,u)F(bu^2)|
 \ll_\varepsilon X^\varepsilon
 \sum_{b\leq L}\left(1+{L\over\sqrt b}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{3.12}
\]

For every nontrivial residual shell and all sufficiently large (L),
the product support lies above (L), so the (u=1,b>L) term is exactly
(\sum_rF(r)=\mathcal T_L^{M1}).  Bounded (L) is absorbed trivially.
This proves (1.7).  The calculation never replaces (C_{L,X}) by an
arbitrary coefficient: it is an exact actual-direction self-return, and
only its already target-safe correction is estimated absolutely.

### 3.5 Central Mellin character cancellation

Fix (r) and one smooth ratio component of the zero-extended literal
symbol.  Since (h=\sqrt{r/z}), (n=\sqrt{rz}) when (z=n/h), every
fixed-(r) profile factor can be included in a compactly supported
function (A_r(z)).  Mellin inversion writes its fibre as an integral of

\[
 D_r(\tau):=\sum_{hn=r}\chi_4(n)(n/h)^{i\tau}.
\tag{3.13}
\]

The divisor sum is multiplicative and equals (1.8).  At (p=2) the
inner polynomial in (1.8) is (1), since (\chi_4(2^j)=0) for
(j\geq1); the full local contribution nevertheless retains
(2^{-ik\tau}) from the prefactor (r^{-i\tau}) when
(2^k\parallel r).  If
(r=st^2), an odd prime (p\equiv3\pmod4) lies in (s) exactly when
(v_p(r)) is odd.  At (\tau=0), its local sum
(\sum_{j=0}^{v_p(r)}(-1)^j) then vanishes.

This cancellation is exact but confined to the complete central divisor
mode.  Already for the squarefree local exponent (k=1),

\[
 1+\chi_4(p)p^{2i\tau}=1-p^{2i\tau}
\tag{3.14}
\]

for (p\equiv3\pmod4).  It is not small uniformly off (\tau=0).
The compact ratio cutoff has a full inverse Mellin integral, not a delta
mass or a residue at zero.  The strict cone and the dyadic (h)-shell are
precisely what require the noncentral modes.  Therefore:

- retaining only (\tau=0) does not equal the literal coefficient;
- taking absolute values or an (L^2) norm over the remaining modes has
  no proved (L^{-1/2}) actual-direction gain; and
- recombining every mode is exactly Mellin inversion and returns (2.2).

Nonsmooth edge, star, and crossing terms are not silently assigned to the
central mode; they remain literal boundary pieces.  Thus the central
(1*\chi_4) observation is a one-mode cancellation/self-return, not a
proof of (181.HR).

### 3.6 Why joint-(t) averaging is not a new dimension

On the graph of the unique map (r\leftrightarrow(s,t)),

\[
 e(t\sqrt{Xs})=e(\sqrt{Xr}).
\tag{3.15}
\]

The lift from an (r)-indexed vector to its unique squarefree coordinates
is a permutation isometry.  Consequently a complete joint-(t)
(TT^*) kernel has phase

\[
 e\!\left(\sqrt X(\sqrt{r_1}-\sqrt{r_2})\right),
\tag{3.16}
\]

and is unitarily the original product-index kernel restricted by
({\rm sf}(r)>L).  It creates no independent (t)-orthogonality.
Applying a positive norm after this lift gives the same
coefficient-insensitive (L^2X^\varepsilon) capacity; using only
large (t) gives the already proved sector (1.4); and (t=1) remains.
This is recorded only as the required rank-one no-repeat control, not as
a renewed square-root-wave or second-(B)-process route.

## 4. First doubtful or unproved step

After removing the low-radical sector (3.8), the large-(t) sector
(1.4), and equivalently any large-gcd boundary sector, the first unproved
step is still the complete actual-direction estimate on
(1\leq t<\sqrt L).  Its mandatory first face is

\[
 \boxed{
 \sum_{\substack{de\ {\rm squarefree}\\
                  d\in I_{L,X},\ e\ {\rm odd}\\
                  4d<e<16d}}
 \chi_4(e)a_{L,X}^{\rm lit}(d,e)
 e(\sqrt{Xde})
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{4.1}
\]

Here squarefree (de) already implies ((d,e)=1), and the high-radical
condition is automatic on the hard product support for large (L).
Neither (G\mid t), averaging square multipliers, nor the central Mellin
factor acts on (4.1).  A valid continuation needs a theorem that keeps,
before every positive norm, the simultaneous interaction of
(\chi_4(e)), squarefree/coprime support, the literal cone/profile, and
the fixed centre (X).  No such theorem is derived here.

The optional layerwise estimate (S_t^{3/4}X^\varepsilon) is also open;
its first missing factor is (3.9).  The capacity calculations do not show
that (4.1) is false, and they are not lower bounds for its literal value.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_product_fibre_identity` | **Pass.** Equation (3.1) is a finite multiplicity-one regrouping; no modulus is taken. |
| `unique_squarefree_kernel_decomposition` | **Pass.** Equations (1.1) and (3.2) are bijective in both directions. |
| `literal_product_support` | **Pass.** Equation (2.3) gives (r\asymp L^2), hence (s\asymp L^2/t^2), (s\ll L^2), and (t\ll\sqrt L) on (s>L). |
| `low_radical_incidence_bound` | **Pass.** Equation (3.8) rederives (L^{3/2}X^\varepsilon). |
| `high_radical_capacity_ledger` | **Pass as capacity only.** Equations (2.5) and (3.9) give (L^2X^\varepsilon) total positive capacity and the exact (L^{1/2}) deficit at (t=1). No literal lower mass is claimed. |
| `fixed_t_power_summation` | **Open at the correct seam.** Equation (3.10) verifies that the proposed (S_t^{3/4}) bounds would sum correctly, while (3.9) records the missing factor. |
| `joint_t_aggregate_scope` | **Pass/no-go.** Equations (3.15)--(3.16) show that the complete lift is a permutation of product indices; only the large-(t) strict sector is paid. |
| `perfect_square_centre_control` | **Pass.** If (X=y^2), exact-square products have (s=1) and lie in (3.8). No oscillation claim is used on them. This does not assert a uniform gap for high (s), especially for arbitrary real (X). |
| `high_radical_t1_control` | **Pass.** Equation (3.3) retains the entire (t=1), (G=1) coprime squarefree cone, and (4.1) is explicitly left open. |
| `complex_dechirped_control` | **Pass/falsifies coefficient-uniform claims.** Replacing the literal symbol on an interior cone by (a^{\rm adv}(h,n)=\overline{\chi_4(n)e(\sqrt{Xhn})}) makes all terms positive and restores (L^2) support capacity. This is nonliteral and is used only to reject arbitrary-coefficient contraction. |
| `arbitrary_coefficient_control` | **Pass.** No bound in the open small-(t) sector is asserted after replacing (C_{L,X}) by a bounded sequence. |
| `character_erasure_control` | **Pass.** The exact factorization retains (\chi_4(Ge)), and Mellin separation retains every local factor. Character is erased only in already target-safe incidence estimates; any such erasure on the complement is declared insufficient. |
| `one_site_one_fibre_controls` | **Pass.** Each ((h,n)) maps to one ((r,s,t,G,d,e,a,b)); a one-incidence fibre is allowed and no fibre cancellation is presumed. |
| `hard_endpoint_and_zero_extension` | **Pass.** The shell, strict (4h<n<16h) edges, floors, stars, crossings, removed owners, and hard sample stay inside the zero-extended literal symbol in every exact identity. Mellin analysis is explicitly confined to smooth pieces and does not delete boundary pieces. |
| `both_frequency_signs_and_hard_sample` | **Pass.** The derivation is signwise for (\sigma=\pm1); the physical two-sided combination costs only its fixed outer combination. The hard-profile sample keeps its original multiplicity. |
| `rank_one_square_root_wave_no_repeat` | **Pass/stopped.** Equation (3.16) identifies the exact self-return, and no second process, Hessian argument, or product-wave rescan is attempted. |
| `literal_unknown_quarantine` | **Pass.** The strict sector is a literal upper bound; every (L^2) obstruction is labelled capacity or nonliteral control, not an actual lower bound. |
| `downstream_scope` | **Pass.** The report closes neither the residual small-(t) hard cone nor the hard parent. Smooth M1, GAR, M9-M1, M2, endpoint uniformity, M9, and both bridges remain outside scope. |
| `exponent_quarantine` | **Pass.** No global exponent improvement or quarter theorem is claimed. |

## 6. Dependencies and exact artifacts used

The derivation used only the permitted packet:

- `protocol.md`;
- `state/proof_obligations.yml`, especially
  `M9-M1-top-endpoint-transform`,
  `M9-M1-top-endpoint-signed-cone`,
  `M9-M1-direct-hard-smooth-separate-one-third-minimax`, and
  `M9-M1-physical-one-count-assembly`;
- `state/active_campaign.yml`;
- `strategy/round181_selection/conductor_round181_selection_decision.md`;
- `strategy/round181_m1_hard_top_high_squarefree_radical_strategy.md`;
- `strategy/round181_selection/m1_gar_frontier_selection.md`;
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`;
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`;
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/briefs/hard_m1_high_radical_signed_attack.md`.

No web theorem, source import, or numerical experiment was used.  The
argument is entirely finite algebra, incidence counting, and exact
transform-scope analysis.

## 7. Recommended state effect

**Recommended effect: retain (181.HR) open and record a scoped no-go.**

After independent seam review, the conductor may promote as subordinate
facts the exact parametrization (3.2), (G\mid t), the target-safe
(t\geq\sqrt L) and (G\geq\sqrt L) sectors, and the actual-coefficient
Möbius self-return (1.7).  Record that neither gcd pruning nor the
central (1*\chi_4) Mellin mode provides the missing (L^{1/2}), and
that complete joint-(t) lifting is only product reindexing.

The complete high-radical target, its small-(t) complement, and in
particular (4.1) remain unproved.  Accordingly this report recommends the
Round-181 exit label
`hard_m1_high_radical_capacity_or_self_return_no_go`, not promotion of
`M9-M1-top-endpoint-signed-cone` and not any downstream or exponent
claim.
