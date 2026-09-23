# Formalized Round-183 hard-M1 small-t primitive-ray sector and self-return

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Task: `conductor_formalization`
- Role: conductor-owned formal proof-kernel candidate
- Generated: `2026-08-27T20:10:40.7471107+08:00`
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Evidence status: candidate evidence only; pending final kernel review and
  State Patch validation
- Numerical work: none

## 1. Exact literal setup

Fix real \(X\geq2\), put

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
 \tag{183.C0}
\]

and fix one literal middle or lower residual shell \(L\) of the unique
hard M1 profile and one sign \(\sigma\in\{+1,-1\}\).  Extend
the complete literal symbol \(a_{L,X}^{\mathrm{lit},\sigma}(h,n)\) by zero
off every one of its original support, profile, strict-edge, floor, star,
half-weight, hard-sample, crossing, and endpoint conditions.  Define

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                   r/h\ \mathrm{odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h),
 \tag{183.C1}
\]

\[
 \mathcal A_{L,X,\sigma}^{\mathrm{st}}
 =\sum_{\substack{s>L,\ \mu^2(s)=1\\
                    1\leq t<T_L}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}),
 \qquad T_L=\lceil\sqrt L\rceil .
 \tag{183.C2}
\]

Equation (183.C2) is the still-open Round-181 small-\(t\) owner.  Every
split below is made only after expanding (183.C1) into its literal divisor
incidences; it is not a split of product indices or a substitute
coefficient.

## 2. Primitive-ray coordinates and the strict sector

For each literal incidence put

\[
 G=(h,n),\qquad h=Gu,\qquad n=Gv,\qquad (u,v)=1.
 \tag{183.C3}
\]

Since \(n\) is odd, \(G\) and \(v\) are odd.  Define

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{uv/s(u,v)}\in\mathbb N.
 \tag{183.C4}
\]

Then exactly

\[
 hn=s(u,v)(G\rho(u,v))^2,\qquad
 s=s(u,v),\qquad t=G\rho(u,v).
 \tag{183.C5}
\]

Thus the inherited high-radical and small-multiplier restrictions are
respectively \(s(u,v)>L\) and \(G\rho(u,v)<T_L\).  The map between literal
incidences and triples \((u,v,G)\) satisfying these conditions and the
zero-extended literal support is bijective, so it preserves multiplicity.
Moreover

\[
 \chi_4(Gv)=\chi_4(G)\chi_4(v),\qquad
 e(\sigma\sqrt{Xhn})=e(\sigma G\sqrt{Xuv}).
 \tag{183.C6}
\]

Put

\[
 G_0=\lceil L^{1/4}\rceil,\qquad
 \delta_X=\frac1{10\log(2X)},\qquad
 \Delta_X(u,v)=\operatorname{dist}
 \left(2\sqrt{Xuv},\mathbb Z+\tfrac12\right).
 \tag{183.C7}
\]

The strict incidence sector is

\[
\begin{aligned}
 \mathcal A^{\mathrm{ray,nr}}_{L,X,\sigma}
 ={}&\sum_{\substack{(u,v)=1,\ v\ \mathrm{odd},\ 4u<v<16u\\
                      s(u,v)>L,\ \Delta_X(u,v)\geq\delta_X}}
 \chi_4(v)
 \sum_{\substack{G\geq G_0,\ G\ \mathrm{odd}\\
                   G\rho(u,v)<T_L}}
 \chi_4(G)a_{L,X}^{\mathrm{lit},\sigma}(Gu,Gv)
 e(\sigma G\sqrt{Xuv}).
\end{aligned}
 \tag{183.C8}
\]

All undeclared predicates in (183.C8) are imposed through the
zero-extended literal symbol.

### Lemma 1: uniform step-two variation

Let \(\eta_L(m)\) denote the accepted scale-normalized-BV dyadic
frequency profile, including its literal shell endpoint weights, and set

\[
 \Psi_{H,L}(m)=
 \mathbf1_{1\leq m\leq H}\eta_L(m)
 \Phi\!\left(\frac m{H+1}\right),
 \qquad m\in\mathbb Z,
 \tag{183.C9a}
\]

with zero extension outside \([1,H]\).  The remaining literal frequency
masks and residual labels are retained separately in the full symbol.

For fixed \((u,v)\), define on the odd integers

\[
 w_{u,v}^{\sigma}(G)=
 \mathbf1_{G\geq G_0}\mathbf1_{G\rho(u,v)<T_L}
 a_{L,X}^{\mathrm{lit},\sigma}(Gu,Gv),
 \tag{183.C9}
\]

and extend it by zero.  Then

\[
 \|w_{u,v}^{\sigma}\|_{BV_2}:=
 \sup_{G\ \mathrm{odd}}|w_{u,v}^{\sigma}(G)|
 +\sum_{G\ \mathrm{odd}}
 |w_{u,v}^{\sigma}(G+2)-w_{u,v}^{\sigma}(G)|
 \ll_\varepsilon X^\varepsilon .
 \tag{183.C10}
\]

**Proof.**  On a fixed primitive ray, \(n/h=v/u\) is constant.  Hence
the transformed \(W\)-factor, strict ratio tests, hard sample, sign field,
and every ratio-dependent endpoint field are constant.  The accepted
frequency profile has scale-normalized integer bounded variation; sampling
it at \(Gu\) along odd \(G\) cannot increase that variation.  The
normalized power varies monotonically as \(G^{-3/2}\), with endpoint plus
total variation bounded by its normalized supremum on \(Gu\asymp L\).
On the active interval, the accepted \(C^1\) regularity of \(\Phi\),
together with \(Gu\asymp L\) and \(L\leq H\), gives

\[
 \sum_{\substack{G\ \mathrm{odd}\\
                   Gu,(G+2)u\in[1,H]}}
 \left|\Phi\!\left(\frac{(G+2)u}{H+1}\right)
       -\Phi\!\left(\frac{Gu}{H+1}\right)\right|
 \ll \frac{u}{H+1}\left(1+\frac Lu\right)\ll1.
 \tag{183.C11}
\]

The discrete product rule, normalized BV of \(\eta_L\), and at most two
zero-extension boundary jumps therefore give

\[
 \sum_{G\ \mathrm{odd}}
 |\Psi_{H,L}((G+2)u)-\Psi_{H,L}(Gu)|\ll1.
 \tag{183.C11a}
\]

The remaining shell, height, \(G\geq G_0\), and \(G\rho<T_L\) restrictions are
interval masks on the odd lattice.  Strict inequalities choose endpoints
but do not add variation.  Floors are fixed at fixed \(X\), while stars,
half weights, real-\(X\) crossings, and zero extension contribute only the
entry and exit jumps of the fixed finite literal partition.  The discrete
product rule applied to the complete symbol, `H4-Phi-regularity`,
`M9-M1-frequency-phase-diagram-R10`, and
`M9-M1-top-endpoint-transform` now give (183.C10), uniformly in every
declared parameter and both signs. \(\square\)

### Lemma 2: character-geometric ray cancellation

For \(\alpha=\sqrt{Xuv}\), consecutive odd values of \(G\) satisfy

\[
 \frac{\chi_4(G+2)e(\sigma(G+2)\alpha)}
      {\chi_4(G)e(\sigma G\alpha)}
 =-e(2\sigma\alpha).
 \tag{183.C12}
\]

Consequently, on any consecutive odd interval \(J\),

\[
 \left|\sum_{G\in J,\ G\ \mathrm{odd}}
 \chi_4(G)e(\sigma G\alpha)\right|
 \ll \min\bigl(|J|,\Delta_X(u,v)^{-1}\bigr).
 \tag{183.C13}
\]

The distance is the same for both signs.  Discrete Abel summation with
(183.C10) therefore yields, whenever \(\Delta_X(u,v)\geq\delta\),

\[
 \left|\sum_{G\ \mathrm{odd}}
 \chi_4(G)w_{u,v}^{\sigma}(G)e(\sigma G\sqrt{Xuv})\right|
 \ll_\varepsilon \delta^{-1}X^\varepsilon .
 \tag{183.C14}
\]

This gain uses the actual character and phase.  It is false as a
coefficient-uniform or character-erased assertion. \(\square\)

### Proposition 3: target-safe nonresonant large-gcd sector

Uniformly in the literal shell, real \(X\geq2\), and both signs,

\[
 \boxed{|\mathcal A^{\mathrm{ray,nr}}_{L,X,\sigma}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
 \tag{183.C15}
\]

**Proof.**  If a ray in (183.C8) is nonempty, then \(Gu\asymp L\).
Since \(G\geq G_0\), one has \(u\ll L/G_0\); and \(4u<v<16u\)
allows \(O(u)\) values of \(v\).  Hence the number of possible primitive
rays is

\[
 \ll\sum_{u\ll L/G_0}u
 \ll\left(1+\frac L{G_0}\right)^2.
 \tag{183.C16}
\]

Coprimality, squarefreeness, small \(t\), and literal support only reduce
this count.  Apply (183.C14) ray by ray and only then take a positive ray
sum.  Since \(G_0=\lceil L^{1/4}\rceil\) and
\(\delta_X^{-1}=10\log(2X)\ll_\varepsilon X^\varepsilon\), (183.C16)
gives (183.C15). \(\square\)

The coefficient-insensitive incidence envelope of the same sector is
only

\[
 \sum_{G\geq G_0}O(L^2/G^2)
 \ll L^2/G_0\ll L^{7/4}.
 \tag{183.C17}
\]

Thus (183.C15) is a genuine signed actual-coefficient gain, but only on a
proper sector.

### Exact complement

Within every original predicate of (183.C2), the incidence complement of
(183.C8) is exactly

\[
 \boxed{\{G<G_0\}\ \dot\cup\
 \{G\geq G_0:\Delta_X(u,v)<\delta_X\}.}
 \tag{183.C18}
\]

Equality in the nonresonance test belongs to the proved sector.  The split
is disjoint and exhaustive only at the literal-incidence level.  When the
small-\(t\) range is nonempty, \(t=1\) forces \(G=\rho=1\), so the whole
\(t=1\) cone lies in the first, still-open part of (183.C18).  Therefore
(183.C15) does not prove (183.C2).

## 3. Exact truncated-Mobius self-return

Put

\[
 F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr}),
 \qquad T=T_L.
 \tag{183.C19}
\]

The accepted product support and divisor bound give

\[
 F_\sigma(r)\ne0\Longrightarrow r\asymp L^2,
 \qquad |F_\sigma(r)|\ll_\varepsilon X^\varepsilon.
 \tag{183.C20}
\]

Expanding \(\mu^2(s)=\sum_{a^2\mid s}\mu(a)\), writing \(s=a^2b\),
and then setting \(u=at\) gives the finite exact identity

\[
 \mathcal A_{L,X,\sigma}^{\mathrm{st}}
 =\sum_{b,u\geq1}K_{L,T}(b,u)F_\sigma(bu^2),
 \tag{183.C21}
\]

where

\[
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a).
 \tag{183.C22}
\]

Both strict inequalities in (183.C22) are essential.  On \(b>L,u<T\),
every divisor \(a\mid u\) is admitted, and hence

\[
 K_{L,T}(b,u)=\sum_{a\mid u}\mu(a)=\mathbf1_{u=1}.
 \tag{183.C23}
\]

Partitioning (183.C21) into \(b>L,u<T\), \(b\leq L\), and
\(b>L,u\geq T\), and using \(|K_{L,T}(b,u)|\leq\tau(u)\), gives

\[
 \sum_{b\leq L}\left(1+\frac L{\sqrt b}\right)
 \ll L^{3/2},
 \qquad
 L^2\sum_{u\geq T}u^{-2}\ll L^2/T\ll L^{3/2}.
 \tag{183.C24}
\]

Writing \(\mathcal P_{L,\sigma}=\sum_rF_\sigma(r)\), one also has
\(\sum_{r\leq L}|F_\sigma(r)|\ll_\varepsilon LX^\varepsilon\).
Therefore

\[
 \boxed{\mathcal A_{L,X,\sigma}^{\mathrm{st}}
 =\mathcal P_{L,\sigma}
 +O_\varepsilon(L^{3/2}X^\varepsilon).}
 \tag{183.C25}
\]

Now split the original Mobius divisor at \(a<T\) and \(a\geq T\).  The
large divisor tail satisfies, absolutely,

\[
 |\mathcal A_{\geq T}|
 \ll_\varepsilon X^\varepsilon L^2
 \sum_{a\geq T}a^{-2}\sum_{t\geq1}t^{-2}
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{183.C26}
\]

For the small-divisor core the kernel is

\[
 K^{<}_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a<T\\a^2b>L\\u/a<T}}\mu(a).
 \tag{183.C27}
\]

Again, on \(b>L,u<T\), every divisor of \(u\) has \(a<T\), and

\[
 K^{<}_{L,T}(b,u)=\mathbf1_{u=1}.
 \tag{183.C28}
\]

The same partition and bounds prove

\[
 \boxed{\mathcal A_{<T}=\mathcal P_{L,\sigma}
 +O_\varepsilon(L^{3/2}X^\varepsilon),\qquad
 \mathcal A_{\geq T}\ll_\varepsilon L^{3/2}X^\varepsilon.}
 \tag{183.C29}
\]

Thus target-scale partial Mobius truncation removes a safe tail but leaves
the original full product wave, including \(a=t=u=1\), modulo target size.
This is a mechanism-scoped self-return, not a no-go theorem for the literal
owner.

## 4. Conditional fixed-row connector and PSC separation

For a fixed \(1\leq t<T\), set

\[
 z_{t,\sigma}(s)=\mathbf1_{s>L}\mu^2(s)
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}),
 \tag{183.C30}
\]

zero-extended on an ambient interval of length \(N_t\ll L^2/t^2\), and
put \(Q_t=\lceil\sqrt{N_t}\rceil\).  The exact Fejer block identity gives

\[
 |S_{t,\sigma}|^2\leq
 \frac{N_t+Q_t-1}{Q_t}
 \left[R_{t,\sigma}(0)+2\Re\sum_{1\leq q<Q_t}
 \left(1-\frac q{Q_t}\right)R_{t,\sigma}(q)\right],
 \tag{183.C31}
\]

where

\[
\begin{aligned}
 R_{t,\sigma}(q)=\sum_s&\mathbf1_{s>L}\mathbf1_{s+q>L}
 \mu^2(s)\mu^2(s+q)\\
 &\times C_{L,X}^{\sigma}((s+q)t^2)
 \overline{C_{L,X}^{\sigma}(st^2)}
 e\!\left(\sigma t\sqrt X(\sqrt{s+q}-\sqrt s)\right),
\end{aligned}
 \tag{183.C32}
\]

with both literal supports retained.  The diagonal is
\(R_{t,\sigma}(0)\ll_\varepsilon N_tX^\varepsilon\).  The still-unproved
signed brace estimate

\[
 R_{t,\sigma}(0)+2\Re\sum_{1\leq q<Q_t}
 \left(1-\frac q{Q_t}\right)R_{t,\sigma}(q)
 \ll_\varepsilon N_tX^\varepsilon
 \tag{183.C33}
\]

would imply \(|S_{t,\sigma}|\ll N_t^{3/4}X^\varepsilon\); summing
\(L^{3/2}t^{-3/2}\) would prove (183.C2).  But (183.C33) is unproved
already at \(t=1\), and rowwise control followed by triangle in \(t\) is
strictly stronger than the one-absolute-value owner.

After expanding both coefficients, (183.C32) has
\(h_1n_1-h_0n_0=t^2q\), two characters, two literal symbols, two
squarefree indicators, and a radical phase difference.  It is not the
old centered linear-fibre `M9-M1-shifted-divisor-correlation-PSC`; no
implication in either direction is proved.  The common missing
\(L^{1/2}\) at the current hard-top shell is only a power diagnostic.

## 5. Divisor-orientation seam

On the squarefree \(t=1\) fibre, moving an odd prime \(p\) from one side
of \(hn=r\) to the other multiplies \(n/h\) by \(p^{\pm2}\).  Since
\(4<n/h<16\), every \(p\geq3\) sends the ratio outside the literal cone.
For \(p\equiv3\pmod4\), the character reverses, so the exact half-difference
identity pairs disjoint supports.  It is a self-return, not a contraction.
This observation is conditional on such a prime dividing the fibre and is
not an estimate for all fibres.

## 6. Scope and state recommendation

The narrow proved result is only (183.C15), an actual-coefficient,
incidence-level, large-gcd nonresonant sector.  The exact complement
(183.C18), including all \(t=1\), remains open.  Equations (183.C25) and
(183.C29) refine only the existing Mobius/Mellin mechanism obstruction.
Equation (183.C33) remains an inconclusive sufficient condition.

Accordingly, a State Patch may create one subordinate
`proved_internal` strict-sector node, refine the existing self-return
obstruction, and narrow the open owner's next action to (183.C18).  It
must not promote the complete small-\(t\) owner, the hard signed cone, the
independent smooth M1 parent, GAR, M9-M1, any M2 node, endpoint uniformity,
M9, either bridge, the Gauss-circle target, or any exponent.

## 7. Exact dependencies and reviewed evidence

Direct accepted dependencies:

- `M9-M1-hard-top-squarefree-radical-sector-reduction`;
- `M9-M1-top-endpoint-transform`;
- `M9-M1-frequency-phase-diagram-R10`;
- `H4-Phi-regularity`; and
- `Divisor-bound-elementary`.

Round evidence used:

- `reports/literal_small_t_signed_contraction_attack.md`;
- `reports/partial_mobius_shifted_correlation_barrier_audit.md`;
- `reports/blind_complete_small_t_rederivation.md`;
- `reviews/coefficient_product_endpoint_seam_review.md`;
- `reviews/power_self_return_psc_seam_review.md`; and
- `reviews/blind_post_unmask_owner_scope_review.md`.

The three seam reviews are GREEN.  No external theorem or numerical
experiment is used.
