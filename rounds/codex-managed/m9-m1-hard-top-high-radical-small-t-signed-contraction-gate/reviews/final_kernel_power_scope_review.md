# Final Round 183 kernel power and scope review

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: independent final power/scope reviewer
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Candidate SHA-256:
  `e23d4135401c81c263026fddf19df4d46536eaabaa33fa9a7a0d8b287ea82f91`
- Durable-kernel SHA-256:
  `f8898d48d1d8db3fcb767399b9825568d27a0fd32bb45b1b3de02a51154692d1`
- Review status: **GREEN**

## 1. Result and verdict

The conductor candidate and durable kernel are **GREEN** on the requested
power, identity, and scope seams.

The candidate correctly separates three mathematical outputs:

1. a proved, actual-coefficient, incidence-level primitive-ray sector;
2. an exact truncated-Mobius self-return obstruction; and
3. an unproved fixed-row Fejer correlation condition that is sufficient
   but stronger than the frozen owner.

The durable kernel preserves precisely the two proved outputs and mentions
the correlation route only in conditional scope. It does not turn a
sufficient norm into an owner.

The exact surviving owner is the incidence complement

\[
 \{G<G_0\}\ \dot\cup\
 \{G\ge G_0:\Delta_X(u,v)<\delta_X\},
 \qquad
 G_0=\lceil L^{1/4}\rceil ,
 \tag{1.1}
\]

with all original predicates retained. It contains the complete \(t=1\)
face. Consequently neither the complete small-\(t\) estimate nor any
hard-M1 parent is proved.

There is one nonblocking reading qualification. The candidate's opening
sentence that splits are made after literal incidence expansion should be
read as a coefficient-preservation convention. The primitive-ray split is
an incidence partition; the Mobius split is an exact auxiliary
representation split of the unchanged product coefficient. The formulas
themselves state this correctly, so no mathematical repair is required.

## 2. Exact statements and hypotheses checked

Fix real \(X\ge2\), one literal middle or lower residual hard-M1 shell
\(L\), one sign \(\sigma\in\{+1,-1\}\), and

\[
 T=\lceil\sqrt L\rceil,\qquad
 F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr}).
 \tag{2.1}
\]

The coefficient is the exact zero-extended literal divisor coefficient.
The inherited support and divisor bound are

\[
 F_\sigma(r)\ne0\Longrightarrow r\asymp L^2,
 \qquad
 |F_\sigma(r)|\ll_\varepsilon X^\varepsilon .
 \tag{2.2}
\]

The frozen open scalar is

\[
 \mathcal A^{\mathrm{st}}_{L,X,\sigma}
 =
 \sum_{\substack{s>L,\ \mu^2(s)=1\\1\le t<T}}
 F_\sigma(st^2).
 \tag{2.3}
\]

For the primitive-ray sector, each literal incidence has

\[
 h=Gu,\qquad n=Gv,\qquad G=(h,n),\qquad (u,v)=1,
 \tag{2.4}
\]

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{uv/s(u,v)},\qquad
 t=G\rho(u,v),
 \tag{2.5}
\]

and the character-phase factorization

\[
 \chi_4(Gv)e(\sigma\sqrt{XG^2uv})
 =
 \chi_4(v)\chi_4(G)e(\sigma G\sqrt{Xuv}).
 \tag{2.6}
\]

The candidate and kernel retain oddness, coprimality, \(s>L\),
\(G\rho<T\), both signs, strict cone edges, shell support, floors, stars,
half weights, hard samples, real-\(X\) crossings, endpoints, and zero
extension. The positive theorem is explicitly incidence-level rather
than a theorem for a product subset.

## 3. Proof and power audit

### 3.1 Primitive-ray threshold and power

On one nonresonant ray, the accepted literal step-two BV estimate and the
exact odd-\(G\) character progression give

\[
 \left|
 \sum_{G\ {\rm odd}}
 \chi_4(G)w^\sigma_{u,v}(G)e(\sigma G\sqrt{Xuv})
 \right|
 \ll_\varepsilon \delta_X^{-1}X^\varepsilon,
 \tag{3.1}
\]

where

\[
 \delta_X=(10\log(2X))^{-1},\qquad
 \Delta_X(u,v)=
 \operatorname{dist}(2\sqrt{Xuv},\mathbb Z+\tfrac12),
 \tag{3.2}
\]

and (3.1) is used only when \(\Delta_X\ge\delta_X\).

A nonempty ray with \(G\ge G_0\) has \(Gu\asymp L\), so
\(u\ll L/G_0\); the cone \(4u<v<16u\) leaves \(O(u)\) possible \(v\)'s.
Thus

\[
 \#\{\text{possible primitive rays}\}
 \ll
 \sum_{u\ll L/G_0}u
 \ll
 \left(1+\frac L{G_0}\right)^2.
 \tag{3.3}
\]

With \(G_0=\lceil L^{1/4}\rceil\),

\[
 \left(1+\frac L{G_0}\right)^2\ll L^{3/2},
 \qquad
 \delta_X^{-1}\ll_\varepsilon X^\varepsilon.
 \tag{3.4}
\]

Therefore the candidate's sector is
\(O_\varepsilon(L^{3/2}X^\varepsilon)\). The ceiling and restriction to
odd \(G\) introduce no loss. The corresponding positive incidence
envelope is only

\[
 \sum_{G\ge G_0}O(L^2G^{-2})
 \ll \frac{L^2}{G_0}
 \ll L^{7/4}.
 \tag{3.5}
\]

Hence the theorem earns \(L^{1/4}\) on this proper sector. It does not
earn the full \(L^{1/2}\) missing from the complete \(L^2\)-capacity
owner. The candidate and kernel state that distinction correctly.

The complement (1.1) is disjoint and exhaustive within the original
incidence predicates, with equality \(\Delta_X=\delta_X\) assigned to
the proved side. When (2.3) is nonempty, \(t=1\) forces
\(G=\rho=1<G_0\), so no part of the mandatory \(t=1\) face is silently
paid.

### 3.2 Exact two-cutoff Mobius kernel

Expanding \(\mu^2(s)\), writing \(s=a^2b\), and setting \(u=at\) gives

\[
 \mathcal A^{\mathrm{st}}_{L,X,\sigma}
 =
 \sum_{b,u\ge1}K_{L,T}(b,u)F_\sigma(bu^2),
 \tag{3.6}
\]

\[
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a).
 \tag{3.7}
\]

Both inequalities are exact and strict. The first retains \(s>L\); the
second is precisely the integer condition \(t\le T-1\). On
\(b>L,\ u<T\), every divisor \(a\mid u\) satisfies both cutoffs, hence

\[
 K_{L,T}(b,u)=\sum_{a\mid u}\mu(a)=\mathbf1_{u=1}.
 \tag{3.8}
\]

In particular, for the nonempty range,
\(K_{L,T}(b,1)=\mathbf1_{b>L}\). This is the full
\(a=t=u=1\) product wave, not merely the squarefree \(t=1\) face, and it
cannot be deleted.

The exact disjoint partition is

\[
 \begin{aligned}
 \mathcal A^{\mathrm{st}}_{L,X,\sigma}
 ={}&\sum_{b>L}F_\sigma(b)\\
 &+\sum_{\substack{b\le L\\u\ge1}}
 K_{L,T}(b,u)F_\sigma(bu^2)\\
 &+\sum_{\substack{b>L\\u\ge T}}
 K_{L,T}(b,u)F_\sigma(bu^2).
 \end{aligned}
 \tag{3.9}
\]

The two transformed corrections have the exact capacities

\[
 \sum_{b\le L}\left(1+\frac L{\sqrt b}\right)
 \ll L^{3/2},
 \tag{3.10}
\]

\[
 L^2\sum_{u\ge T}u^{-2}
 \ll \frac{L^2}{T}
 \ll L^{3/2}.
 \tag{3.11}
\]

The kernel divisor factor is absorbed into \(X^\varepsilon\). Since

\[
 \sum_{b>L}F_\sigma(b)
 =
 \sum_rF_\sigma(r)-\sum_{b\le L}F_\sigma(b),
 \qquad
 \sum_{b\le L}|F_\sigma(b)|
 \ll_\varepsilon LX^\varepsilon,
 \tag{3.12}
\]

the candidate's identity

\[
 \mathcal A^{\mathrm{st}}_{L,X,\sigma}
 =
 \sum_rF_\sigma(r)
 {}+O_\varepsilon(L^{3/2}X^\varepsilon)
 \tag{3.13}
\]

is correct. The \(u\ge T\) term is an internal correction in this
alternative regrouping and is not a second copy of the already accepted
original large-\(t\) sector.

### 3.3 Partial-core self-return

Splitting the original Mobius divisor at \(a<T\) and \(a\ge T\), product
support gives the tail

\[
 |\mathcal A_{\ge T}|
 \ll_\varepsilon
 X^\varepsilon L^2
 \sum_{a\ge T}a^{-2}\sum_{t\ge1}t^{-2}
 \ll_\varepsilon
 \frac{L^2}{T}X^\varepsilon
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{3.14}
\]

The small-divisor kernel is

\[
 K^<_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a<T\\a^2b>L\\u/a<T}}\mu(a).
 \tag{3.15}
\]

For \(b>L,\ u<T\), every divisor \(a\mid u\) already has \(a<T\).
Therefore

\[
 K^<_{L,T}(b,u)=\mathbf1_{u=1}.
 \tag{3.16}
\]

Repeating (3.9)--(3.12) proves

\[
 \mathcal A_{<T}
 =
 \sum_rF_\sigma(r)
 {}+O_\varepsilon(L^{3/2}X^\varepsilon),
 \qquad
 \mathcal A_{\ge T}
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{3.17}
\]

Thus the proposed target-scale truncation removes a safe tail but returns
the complete product wave in its core. This is a proved mechanism
obstruction, not a counterexample to the literal owner.

### 3.4 Fixed-row Fejer connector

For one nonempty row, let \(z(s)\) be zero-extended on an ambient interval
of length \(N=N_t\), let \(1\le Q\le N\), and define the exact
correlations

\[
 R(q)=\sum_s z(s+q)\overline{z(s)}.
 \tag{3.18}
\]

The moving-block Cauchy identity gives

\[
 |S_t|^2
 \le
 \frac{N+Q-1}{Q}
 \left[
 R(0)+2\Re\sum_{1\le q<Q}
 \left(1-\frac qQ\right)R(q)
 \right].
 \tag{3.19}
\]

The constants \(N+Q-1\), \(Q^{-1}\), the range \(1\le q<Q\), and the
Fejer weights are correct. In the candidate,

\[
 R_{t,\sigma}(q)
 =
 \sum_s
 \mathbf1_{s>L}\mathbf1_{s+q>L}
 \mu^2(s)\mu^2(s+q)
 C^\sigma((s+q)t^2)\overline{C^\sigma(st^2)}
 e\!\left(
 \sigma t\sqrt X(\sqrt{s+q}-\sqrt s)
 \right),
 \tag{3.20}
\]

with both high-radical indicators and both zero-extended literal supports
present. After incidence expansion,

\[
 h_1n_1-h_0n_0=t^2q.
 \tag{3.21}
\]

For \(Q=Q_t=\lceil\sqrt{N_t}\rceil\),

\[
 \frac{N_t+Q_t-1}{Q_t}\le2\sqrt{N_t},
 \qquad
 R_{t,\sigma}(0)\ll_\varepsilon N_tX^\varepsilon.
 \tag{3.22}
\]

The brace is the nonnegative quantity
\(Q_t^{-1}\sum_m|B_m|^2\). The **unproved** signed estimate

\[
 R_{t,\sigma}(0)+2\Re\sum_{1\le q<Q_t}
 \left(1-\frac q{Q_t}\right)R_{t,\sigma}(q)
 \ll_\varepsilon N_tX^\varepsilon
 \tag{3.23}
\]

would imply

\[
 |S_{t,\sigma}|
 \ll_\varepsilon
 N_t^{3/4}X^\varepsilon
 \ll_\varepsilon
 L^{3/2}t^{-3/2}X^\varepsilon.
 \tag{3.24}
\]

Summing \(\sum_{t\ge1}t^{-3/2}\) then gives the frozen target. The
candidate correctly labels (3.23) unproved already at \(t=1\). The
rowwise estimate followed by triangle in \(t\) is sufficient but strictly
stronger than the one-absolute-value aggregate, and the durable kernel
does not promote it.

The interface is not the old PSC. The old statement uses a fixed
half-lattice center and a linear signed difference of two nearest-product
divisor fibres. Equation (3.20) uses a moving midpoint, a radical shift,
two product coefficients, two squarefree indicators, and the quadratic
product relation (3.21). No implication in either direction is proved.
The common \(L^{1/2}\) loss on the present hard-top shell is only a power
diagnostic, not an equivalence or an imported delta/Kloosterman theorem.

## 4. First open seam

The first open mathematical seam is the exact incidence complement (1.1).
It has two parts:

1. the small-gcd range \(G<G_0\), containing the complete \(t=1\)
   coprime-squarefree cone; and
2. the large-gcd half-integer near-resonant range
   \(\Delta_X(u,v)<\delta_X\).

Neither the truncated-Mobius identities nor the conditional Fejer
connector estimates this complement. At the correlation interface, the
first missing assertion is (3.23) for \(t=1\). At the divisor-orientation
interface, the one-prime transfer has disjoint supports and self-returns;
it does not supply contraction.

The complete small-\(t\) coefficient-insensitive capacity remains \(L^2\)
against target \(L^{3/2}\). No literal lower bound or refutation of the
owner is proved.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact literal and zero-extended coefficient | **PASS.** No substitute coefficient enters the candidate or kernel. |
| Primitive-ray bijection | **PASS.** Multiplicity, oddness, character, phase, \(s\), and \(t\) are exact. |
| \(G_0\) power | **PASS.** Ray count is \(O((1+L/G_0)^2)=O(L^{3/2})\). |
| Primitive-sector positive capacity | **PASS.** It is only upper-bounded by \(O(L^{7/4})\); no lower mass is claimed. |
| Exact complement | **PASS.** Disjoint and exhaustive at incidence level; equality goes to the proved side. |
| \(t=1\) retention | **PASS.** The entire face lies in \(G<G_0\) and \(a=t=u=1\) remains in both Mobius cores. |
| Two-cutoff kernel | **PASS.** Both \(a^2b>L\) and \(u/a<T\) are present and strict. |
| Kernel partition | **PASS.** The three regions in (3.9) are disjoint and exhaustive. |
| \(b\le L\) correction | **PASS.** \(O(L^{3/2}X^\varepsilon)\). |
| \(b>L,u\ge T\) correction | **PASS.** \(O(L^2/T)=O(L^{3/2})\). |
| \(a\ge T\) tail | **PASS.** \(O(L^2/T)=O(L^{3/2})\). |
| \(a<T\) self-return | **PASS.** It retains \(\mathbf1_{u=1}\) and the full product wave modulo target size. |
| Large-\(t\) counted once | **PASS.** The transformed correction is not added as a second independent sector. |
| Fejer constants and diagonal | **PASS.** \(N+Q-1\), \(Q^{-1}\), weights, shifts, and \(R(0)\) are correct. |
| Fejer status | **PASS.** The brace estimate is conditional, stronger than the owner, and unpromoted. |
| PSC distinction | **PASS.** Different coordinates, coefficients, center, and outer operation; no theorem transfer. |
| Owner and exponent scope | **PASS.** No parent, bridge, theorem, or exponent is inferred. |

No numerical computation or external theorem was used.

## 6. Dependencies and exact artifacts used

This final review used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, especially
   `M9-M1-hard-top-high-radical-small-t-residual-estimate`,
   `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction`, and
   `M9-M1-shifted-divisor-correlation-PSC`;
3. `candidates/formalized_hard_m1_small_t_primitive_ray_sector_and_self_return.md`;
4. `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`; and
5. `reviews/power_self_return_psc_seam_review.md`.

The accepted mathematical dependencies remain
`M9-M1-hard-top-squarefree-radical-sector-reduction`,
`M9-M1-top-endpoint-transform`,
`M9-M1-frequency-phase-diagram-R10`,
`H4-Phi-regularity`, and `Divisor-bound-elementary`.

## 7. Recommended state effect

The narrowest justified State Patch is:

1. create one subordinate `proved_internal` incidence-sector node for the
   large-gcd, non-half-integer-resonant primitive-ray sector, with (1.1)
   recorded as the exact complement;
2. refine only
   `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction` by adding
   the two-cutoff kernel, the \(a\ge T\) target-safe tail, and the
   \(a<T\) core self-return; and
3. retain the fixed-row Fejer statement only as an unproved sufficient
   route and inconclusive evidence, not as an owner or as PSC.

Keep `M9-M1-hard-top-high-radical-small-t-residual-estimate`,
`M9-M1-top-endpoint-signed-cone`, the independent smooth M1 parent, GAR,
M9-M1, every M2 obligation, endpoint uniformity, M9, both bridges, and the
Gauss-circle theorem open. The internal exponent remains \(1/3\), the
accepted external benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).
