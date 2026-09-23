# Partial-Möbius and shifted-correlation barrier audit

- Campaign: m9-m1-hard-top-high-radical-small-t-signed-contraction-gate
- Round: 183
- Task: partial_mobius_shifted_correlation_barrier_audit
- Role: barrier_no_go
- Access mode: selected_context
- Starting graph SHA-256:
  5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833
- Evidence status: candidate evidence only; no shared proof-state edit is
  authorized

## 1. Result

There are two exact conclusions.

**Truncated-Möbius self-return.** Put

\[
 T=T_L=\lceil\sqrt L\rceil,\qquad
 F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr}).
\]

For the frozen small-\(t\) aggregate

\[
 \mathcal A_{L,\sigma}^{\rm st}
 =\sum_{\substack{s>L\\ \mu^2(s)=1}}
   \sum_{1\le t<T}F_\sigma(st^2),
\tag{1.1}
\]

finite Möbius expansion gives exactly

\[
 \mathcal A_{L,\sigma}^{\rm st}
 =\sum_{b,u\ge1}K_{L,T}(b,u)F_\sigma(bu^2),
 \qquad
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a).
\tag{1.2}
\]

Both strict inequalities and the ceiling in \(T\) are literal. On the
quadrant \(b>L,\ u<T\), every divisor of \(u\) is admitted, and hence

\[
 K_{L,T}(b,u)=\sum_{a\mid u}\mu(a)=\mathbf 1_{u=1}.
\tag{1.3}
\]

The two complementary transformed regions \(b\le L\) and
\(b>L,\ u\ge T\) have total coefficient-insensitive mass
\(O_\varepsilon(L^{3/2}X^\varepsilon)\). Consequently, if

\[
 \mathcal P_{L,\sigma}=\sum_{r\ge1}F_\sigma(r)
\tag{1.4}
\]

is the original literal hard product wave, then

\[
 \boxed{
 \mathcal A_{L,\sigma}^{\rm st}
 =\mathcal P_{L,\sigma}
  +O_\varepsilon(L^{3/2}X^\varepsilon).}
\tag{1.5}
\]

Moreover, splitting the Möbius divisor at the proposed target scale gives

\[
 \mathcal A_{L,\sigma}^{\rm st}
 =\mathcal A_{<T}+\mathcal A_{\ge T},
\]

where

\[
 \boxed{
 \mathcal A_{<T}=\mathcal P_{L,\sigma}
 +O_\varepsilon(L^{3/2}X^\varepsilon),\qquad
 \mathcal A_{\ge T}\ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{1.6}
\]

Thus a cutoff at \(a\asymp\sqrt L\) removes only a target-safe Möbius
tail and leaves the full hard product wave in the core. It does not
produce a smaller signed owner. This is a mechanism no-go, not a
counterexample to the literal estimate.

**Exact fixed-row correlation connector.** For a fixed \(t<T\), let
\(N_t\) be the length of a consecutive integer interval containing the
exact zero-extended \(s\)-support, put
\(Q_t=\lceil\sqrt{N_t}\rceil\), and define the literal correlation

\[
 \begin{aligned}
 R_{t,\sigma}(q)=\sum_s&\mu^2(s)\mu^2(s+q)
 C_{L,X}^{\sigma}((s+q)t^2)
 \overline{C_{L,X}^{\sigma}(st^2)}\\
 &\times
 e\!\left(\sigma t\sqrt X(\sqrt{s+q}-\sqrt s)\right).
 \end{aligned}
\tag{1.7}
\]

Both coefficient factors are zero outside their exact literal support,
and the sum is over the exact support intersection. The van der Corput
inequality is

\[
 |S_{t,\sigma}|^2
 \le {N_t+Q_t-1\over Q_t}
 \left\{R_{t,\sigma}(0)
 +2\Re\sum_{1\le q<Q_t}
   \left(1-{q\over Q_t}\right)R_{t,\sigma}(q)\right\},
\tag{1.8}
\]

where

\[
 S_{t,\sigma}=\sum_{s>L}\mu^2(s)
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\]

The diagonal satisfies
\(R_{t,\sigma}(0)\ll_\varepsilon N_tX^\varepsilon\). Therefore the
still-unproved literal estimate

\[
 \boxed{
 R_{t,\sigma}(0)+2\Re\sum_{1\le q<Q_t}
 \left(1-{q\over Q_t}\right)R_{t,\sigma}(q)
 \ll_\varepsilon N_tX^\varepsilon}
\tag{1.9}
\]

would imply

\[
 |S_{t,\sigma}|\ll_\varepsilon N_t^{3/4}X^\varepsilon
 \ll_\varepsilon (L^2/t^2)^{3/4}X^\varepsilon.
\tag{1.10}
\]

Summing (1.10) over \(t<T\) would prove the frozen owner. Condition
(1.9) is a sufficient fixed-row theorem, strictly stronger than the
one-absolute-value aggregate, and is not proved here. It is not the old
PSC: it is a quadratic radical-shift correlation with product difference
\(t^2q\), rather than the linear signed difference of two centered
nearest-product divisor fibres. Standard delta/Kloosterman completion
does not bridge this mismatch and, at the scalar level, retains the same
critical missing factor.

## 2. Exact statement and hypotheses

Fix one literal middle or lower residual shell of the unique hard M1
profile, one sign \(\sigma\in\{+1,-1\}\), and real \(X\ge2\). The
coefficient is exactly

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                  r/h\ {\rm odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h),
\tag{2.1}
\]

with zero extension before every regrouping. The literal symbol retains
the dyadic frequency cutoff, \(\Phi(h/(H+1))\),
\(W(\sqrt{4q_Xh/n})\), normalized powers, profiles, floors, stars and half
weights, strict cone edges, the hard sample, both signs, real-\(X\)
crossings and endpoints. Nothing below replaces it by a separable or
arbitrary coefficient.

The accepted product support and divisor bound give constants depending
only on the fixed profile such that

\[
 F_\sigma(r)\ne0\Longrightarrow 0<r\ll L^2,\qquad
 |F_\sigma(r)|\ll_\varepsilon X^\varepsilon.
\tag{2.2}
\]

All estimates below use only (2.2); the exact literal coefficient remains
inside every signed identity. When \(T=1\), (1.1) is empty and the claim is
trivial, so the derivation may assume \(T\ge2\).

For the correlation statement, define

\[
 z_{t,\sigma}(s)=
 \mathbf1_{s>L}\mu^2(s)C_{L,X}^{\sigma}(st^2)
 e(\sigma t\sqrt{Xs})
\tag{2.3}
\]

on all integers, with value zero whenever \(s\le0\) or either literal
support test fails. Choose the smallest consecutive integer interval

\[
 I_t=[A_t,B_t]\cap\mathbb Z
\]

containing the exact geometric support of (2.3), including its literal
open/closed endpoint convention; if it is empty, the row is zero. Put
\(N_t=B_t-A_t+1\). Product support gives

\[
 N_t\ll 1+{L^2\over t^2}\ll {L^2\over t^2}
 \qquad(1\le t<T),
\tag{2.4}
\]

while zero extension retains every hole, floor transition, strict edge,
and real-\(X\) crossing inside that interval. Thus using a consecutive
ambient interval does not complete or alter the coefficient.

## 3. Proof or derivation

### 3.1 Exact small-\(t\) Möbius kernel

Use the finite identity

\[
 \mu^2(s)=\sum_{a^2\mid s}\mu(a).
\]

Writing \(s=a^2b\) in (1.1) gives

\[
 \mathcal A_{L,\sigma}^{\rm st}
 =\sum_{\substack{a,b,t\ge1\\a^2b>L\\t<T}}
 \mu(a)F_\sigma\!\left(b(at)^2\right).
\tag{3.1}
\]

For fixed \(a,t\), set \(u=at\). This is a bijection between positive
\(t\) and positive \(u\) divisible by \(a\), and its two inherited
conditions are exactly

\[
 a^2b>L,\qquad {u\over a}<T.
\tag{3.2}
\]

No weak inequality can replace either one: because \(T\) is an integer,
\(u/a<T\) means the original integer condition \(t\le T-1\), and if \(L\)
is a square then \(t=\sqrt L\) is excluded. Likewise \(a^2b=L\) belongs
to the already-paid low-radical boundary, not (1.1). Equations
(3.1)--(3.2) prove (1.2).

The two lower bounds on the Möbius divisor can also be displayed as

\[
 a>\max\!\left(\sqrt{L/b},\,u/T\right),
\tag{3.3}
\]

subject to \(a\mid u\). On product support \(u\asymp L/\sqrt b\), the
two thresholds are of the same order \(\sqrt{L/b}\). Thus the natural
kernel boundary is \(b\)-dependent; a global cutoff at
\(a\asymp\sqrt L\) is only a coarse tail split.

If \(b>L\) and \(u<T\), both tests in (3.2) hold for every divisor
\(a\mid u\). Möbius orthogonality proves (1.3), including the exact
control

\[
 K_{L,T}(b,1)=\mathbf1_{b>L}.
\tag{3.4}
\]

The \(u=1\) term is the \(a=t=1\) term of the expansion. It contains the
entire product wave before the remaining Möbius terms cancel the
non-squarefree \(b\)'s; it therefore retains more than merely the original
squarefree \(t=1\) face.

### 3.2 Exact self-return and restored powers

Split the right side of (1.2) into the quadrant used in (1.3) and its
disjoint complement. Exactly,

\[
 \begin{aligned}
 \mathcal A_{L,\sigma}^{\rm st}
 ={}&\sum_{b>L}F_\sigma(b)\\
 &+\sum_{\substack{b\le L\\u\ge1}}
 K_{L,T}(b,u)F_\sigma(bu^2)
 +\sum_{\substack{b>L\\u\ge T}}
 K_{L,T}(b,u)F_\sigma(bu^2).
 \end{aligned}
\tag{3.5}
\]

The kernel has the pointwise bound

\[
 |K_{L,T}(b,u)|\le\tau(u).
\tag{3.6}
\]

For \(b\le L\), product support restricts \(u\ll L/\sqrt b\). Hence

\[
 \sum_{b\le L}\#\{u:F_\sigma(bu^2)\ne0\}
 \ll\sum_{b\le L}\left(1+{L\over\sqrt b}\right)
 \ll L^{3/2}.
\tag{3.7}
\]

For \(b>L,\ u\ge T\), product support gives \(b\ll L^2/u^2\), so

\[
 \sum_{u\ge T}\#\{b>L:F_\sigma(bu^2)\ne0\}
 \ll L^2\sum_{u\ge T}u^{-2}
 \ll {L^2\over T}\ll L^{3/2}.
\tag{3.8}
\]

The divisor factors in (3.6) are absorbed into \(X^\varepsilon\). Also

\[
 \sum_{b>L}F_\sigma(b)
 =\mathcal P_{L,\sigma}-\sum_{b\le L}F_\sigma(b),\qquad
 \sum_{b\le L}|F_\sigma(b)|\ll_\varepsilon LX^\varepsilon.
\tag{3.9}
\]

Equations (3.5)--(3.9) prove (1.5). The transformed \(u\ge T\) region is
bounded here exactly once. It is not added to the already accepted
original \(t\ge T\) sector as if the two were independent gains; (1.5) is
an alternative regrouping of the same target-equivalent hard scalar.

### 3.3 Target-scale partial-Möbius truncation

Split (3.1) exactly as

\[
 \begin{aligned}
 \mathcal A_{<T}
 &=\sum_{\substack{1\le a<T\\b\ge1\\1\le t<T\\a^2b>L}}
 \mu(a)F_\sigma(b(at)^2),\\
 \mathcal A_{\ge T}
 &=\sum_{\substack{a\ge T\\b\ge1\\1\le t<T\\a^2b>L}}
 \mu(a)F_\sigma(b(at)^2).
 \end{aligned}
\tag{3.10}
\]

The large-\(a\) part is target-safe without cancellation. Indeed,
\(F_\sigma(b(at)^2)\ne0\) implies
\(b\ll L^2/(a^2t^2)\), and so

\[
 \begin{aligned}
 |\mathcal A_{\ge T}|
 &\ll_\varepsilon X^\varepsilon L^2
 \sum_{a\ge T}a^{-2}\sum_{t\ge1}t^{-2}\\
 &\ll_\varepsilon {L^2\over T}X^\varepsilon
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \end{aligned}
\tag{3.11}
\]

The equality case \(a^2b=L\), possible for example at a square \(L\), was
not inserted; retaining the strict condition in (3.10) only reduces the
upper bound.

After \(u=at\), the small-\(a\) kernel is

\[
 K_{L,T}^{<}(b,u)=
 \sum_{\substack{a\mid u\\a<T\\a^2b>L\\u/a<T}}\mu(a).
\tag{3.12}
\]

For \(b>L,\ u<T\), every divisor \(a\mid u\) already satisfies \(a<T\),
so again

\[
 K_{L,T}^{<}(b,u)=\mathbf1_{u=1}.
\tag{3.13}
\]

Repeating (3.5)--(3.9) with \(K^{<}\) proves the first assertion in
(1.6); (3.11) proves the second. Thus the target-scale truncation does
not leave a genuinely shorter hard core. Any partial-Möbius proposal that
keeps \(a=1\) retains (3.4); discarding \(a=1\) would discard the unproved
full product wave and has no target-safe justification.

### 3.4 Exact fixed-row van der Corput identity

Fix a nonempty row and abbreviate \(z(s)=z_{t,\sigma}(s)\), supported on
\(I_t=[A_t,B_t]\cap\mathbb Z\), with \(N=N_t\). Let
\(1\le Q\le N\), extend \(z\) by zero, and put

\[
 B_m=\sum_{j=0}^{Q-1}z(m+j),\qquad A_t-Q+1\le m\le B_t.
\]

Every \(z(s)\) occurs in exactly \(Q\) of these blocks. There are
\(N+Q-1\) blocks, so Cauchy's inequality gives

\[
 Q^2\left|\sum_s z(s)\right|^2
 \le (N+Q-1)\sum_m|B_m|^2.
\tag{3.14}
\]

Expanding the last square, with no endpoint error because of zero
extension, yields the exact identity

\[
 {1\over Q}\sum_m|B_m|^2
 =R_{t,\sigma}(0)+2\Re\sum_{q=1}^{Q-1}
 \left(1-{q\over Q}\right)R_{t,\sigma}(q),
\tag{3.15}
\]

where

\[
 R_{t,\sigma}(q)=
 \sum_{s=A_t}^{B_t-q}z_{t,\sigma}(s+q)
 \overline{z_{t,\sigma}(s)}.
\tag{3.16}
\]

Substitution of (2.3) into (3.16) is exactly (1.7). In particular, its
support is

\[
 s\in I_t\cap(I_t-q),\qquad s>L,\qquad s+q>L,
\tag{3.17}
\]

together with both literal product-support tests. Every strict cone edge,
floor, star, support crossing, and endpoint is separately retained in the
two factors of \(C\).

Expanding those factors makes the shifted-divisor geometry explicit. If

\[
 h_0n_0=st^2,\qquad h_1n_1=(s+q)t^2,
\]

then each correlation incidence obeys

\[
 h_1n_1-h_0n_0=t^2q,
\tag{3.18}
\]

and carries the literal coefficient

\[
 \mu^2(s)\mu^2(s+q)
 \chi_4(n_1)\chi_4(n_0)
 a_{L,X}^{\mathrm{lit},\sigma}(h_1,n_1)
 \overline{a_{L,X}^{\mathrm{lit},\sigma}(h_0,n_0)}
\tag{3.19}
\]

and the phase in (1.7). Thus it is not a bare shifted-divisor count or a
character-erased Kloosterman sum.

Taking \(Q=Q_t=\lceil\sqrt{N_t}\rceil\) in (3.14)--(3.15) proves (1.8),
and

\[
 {N_t+Q_t-1\over Q_t}\le2\sqrt{N_t}.
\tag{3.20}
\]

The diagonal is

\[
 R_{t,\sigma}(0)=\sum_{s>L}\mu^2(s)
 |C_{L,X}^{\sigma}(st^2)|^2
 \ll_\varepsilon N_tX^\varepsilon.
\tag{3.21}
\]

The brace in (1.8) is nonnegative: by (3.15) it is exactly
\(Q_t^{-1}\sum_m|B_m|^2\). Thus (1.9) is a one-aggregate signed
correlation-energy input; it does not take separate absolute values over
the shifts. Equations (3.20)--(3.21), with an epsilon relabelling, prove
(1.10). Finally,

\[
 \sum_{1\le t<T}N_t^{3/4}
 \ll L^{3/2}\sum_{t\ge1}t^{-3/2}
 \ll L^{3/2},
\tag{3.22}
\]

so triangle in \(t\) supplies the stated conditional connector. It is
precisely this triangle that makes the route stronger than the frozen
one-absolute-value owner.

### 3.5 Power ledger and comparison with the old PSC

The trivial fixed-row capacity is \(N_tX^\varepsilon\), whereas (1.10)
asks for \(N_t^{3/4}X^\varepsilon\). Its scalar saving is

\[
 N_t^{1/4}\asymp L^{1/2}t^{-1/2}.
\tag{3.23}
\]

The trivial bound for the brace in (1.8) is
\(O_\varepsilon(Q_tN_tX^\varepsilon)\). Condition (1.9) therefore asks
for the squared-level saving

\[
 Q_t\asymp\sqrt{N_t}\asymp L/t.
\tag{3.24}
\]

Already at \(t=1\), this is the full missing scalar factor \(L^{1/2}\),
or its square \(L\) in the correlation energy. On the critical hard-top
specialization \(H\asymp X^{1/4}\), \(L\asymp X^{1/6}\), the scalar factor
is \(X^{1/12}\asymp H/L\), the same scalar deficit recorded by the old
PSC and its delta/Kloosterman reformulation.

The interfaces are nevertheless different:

| Seam | Old M9-M1-shifted-divisor-correlation-PSC | Fixed-row condition (1.9) |
|---|---|---|
| Coordinates | Centered offset \(u\), denominator \(d\), and disjoint fibres \(\mathcal F_\pm(u)\) | Squarefree radical \(s\), multiplier \(t\), and radical shift \(q\) |
| Algebraic relation | \(d\mid c-u\) or \(d\mid c+u\), with the fibres compared linearly | \(h_1n_1-h_0n_0=t^2q\), after expanding two product coefficients |
| Coefficient | One linear factor \(\chi_4(d)w_D(d)G_U(u,d)\) | The quadratic literal product (3.19), including both squarefree indicators |
| Phase or kernel | The centered Vaaler kernel on an offset annulus | \(e(\sigma t\sqrt X(\sqrt{s+q}-\sqrt s))\) on the exact support intersection |
| Outer operation | One absolute value after the signed difference of two fibres in one annulus | One nonnegative Fejér block energy for each fixed \(t\), followed by triangle over \(t\) |
| Needed gain | \(H/L\) beyond the trivial linear annular bound at the critical annulus | \(N_t^{1/4}\) on the scalar row, equivalently \(Q_t=N_t^{1/2}\) in the quadratic brace |
| Connector | Half-lattice centering and annular reconstruction would imply the M1 target | (1.8)--(3.22) would imply the stronger fixed-row theorem and then the small-\(t\) owner |
| Status | Open; standard completion retains the deficit | Open; no literal estimate for (1.9) is supplied |

There is no exact map taking the old centered fibre difference to
(3.19): the midpoint of the products in (3.18) moves with \(s,q,t\), and
the old single character and divisor symbol become a quadratic pair of
literal divisor sums. Therefore (1.9) is neither equivalent to PSC nor a
proved consequence of it. It is a distinct, stronger sufficient route to
the current owner.

Conversely, expanding (1.9) exposes a shifted-product equation, so a delta
method would face the same broad obstruction class. The accepted
delta/Kloosterman analysis supplies no theorem for the moving short
numerator together with (3.19), the radical squarefree constraints, the
phase difference, and the one aggregate real part over \(q\). Completing
each \(q\) separately would replace that aggregate by positive errors and
does not earn (3.24). The old \(H/L\) deficit is therefore retained as a
warning, not imported as a proof or as a lower bound for the literal
correlation.

## 4. First doubtful or unproved step

The Möbius statements (1.2), (1.5), and (1.6) have no unproved analytic
step beyond the already accepted support and divisor bounds. Their exact
conclusion is negative: the target-scale truncated core contains
\(K_{L,T}^{<}(b,1)=1\) for every \(b>L\), hence the full hard product wave.
The first false step in a claimed partial-Möbius proof would be to call
that core smaller, or to discard the \(a=1\) term without estimating it.

For the shifted-correlation route, the first unproved step is exactly
(1.9), already for \(t=1\). The generic inequality (1.8), the diagonal
bound (3.21), and the restored powers are rigorous, but support and
pointwise size give only the trivial \(Q_tN_t\) brace. A proof must find
an actual-coefficient relation that saves \(Q_t\) in the single weighted
real shift aggregate while preserving (3.19), every endpoint, and both
signs. Neither the old PSC nor the accepted delta/Kloosterman reduction
provides that relation. An arbitrary phase-adapted coefficient makes
\(z(s)=1\) on a full interval and gives a brace of order \(N_tQ_t\), so no
coefficient-uniform substitute can prove (1.9). This control is not a
literal lower bound.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact_mobius_kernel_both_inequalities | **Pass.** Equations (3.1)--(3.2) retain \(a^2b>L\) and \(u/a<T\) exactly. |
| ceil_sqrt_L_and_strict_t_boundary | **Pass.** \(T=\lceil\sqrt L\rceil\), so \(t=T\) and the equality \(a^2b=L\) are excluded throughout. |
| product_support_and_zero_extension | **Pass.** Every identity is finite after zero extension; support is changed nowhere. |
| partial_truncation_tail_power | **Pass.** Equation (3.11) gives \(L^2/T\ll L^{3/2}\). |
| u_equals_one_original_cone_control | **Pass.** Equations (3.4) and (3.13) retain the full \(a=t=u=1\) product wave in both kernels. |
| complete_mobius_self_return_comparison | **Pass.** Equation (1.5) is the exact small-\(t\) analogue of the earlier complete-Möbius self-return. |
| large_t_sector_once_only | **Pass.** The transformed \(u\ge T\) correction is paid directly once; the accepted original \(t\ge T\) sector is not double counted. |
| fixed_t_van_der_Corput_constants_and_diagonal | **Pass.** Equations (3.14)--(3.21) include \(N_t+Q_t-1\), the Fejér weights, and the exact diagonal. |
| shift_range_and_support_intersection | **Pass.** \(1\le q<Q_t\) and \(s\in I_t\cap(I_t-q)\), with both literal supports zero-extended. |
| literal_correlation_phase_and_coefficient | **Pass.** Equations (1.7), (3.18), and (3.19) retain the exact phase, both characters, both literal symbols, and both squarefree indicators. |
| fixed_t_three_quarter_connector | **Pass conditionally.** (1.9) implies (1.10); (1.9) itself remains unproved. |
| sum_over_t_restored_power | **Pass conditionally.** Equation (3.22) restores \(L^{3/2}\sum t^{-3/2}\). |
| old_PSC_interface_comparison | **Pass.** The line-by-line table shows a different quadratic radical-shift interface and no equivalence. |
| delta_Kloosterman_H_over_L_deficit | **Pass as a barrier audit.** At the critical \(t=1\) scale the same scalar \(H/L\asymp L^{1/2}\) is missing; no old complete-sum theorem supplies the squared correlation gain. |
| correlation_not_owner | **Pass.** The route separates rows and applies triangle in \(t\); it is sufficient and strictly stronger, not the frozen owner. |
| t1_and_endpoint_retention | **Pass.** \(t=1\), both signs, strict edges, floors, stars, crossings, and real-\(X\) endpoints remain in every identity. |
| no_literal_lower_mass_from_adversarial_capacity | **Pass.** The phase-adapted \(z(s)=1\) example falsifies only a coefficient-uniform route. |
| downstream_and_exponent_quarantine | **Pass.** No hard parent, smooth M1 parent, M2 owner, M9, bridge, theorem, or exponent is inferred. |
| no_in_round_pivot | **Pass.** Both mechanisms are assessed only against the frozen small-\(t\) owner. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This report used the assigned brief and exactly the selected packet:

1. protocol.md;
2. state/proof_obligations.yml at the starting hash above, in particular
   M9-M1-hard-top-high-radical-small-t-residual-estimate,
   M9-M1-hard-top-squarefree-radical-sector-reduction,
   M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction,
   M9-M1-top-endpoint-signed-cone, and
   M9-M1-shifted-divisor-correlation-PSC;
3. state/active_campaign.yml;
4. strategy/round183_m1_hard_top_high_radical_small_t_signed_contraction_strategy.md;
5. proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md;
6. rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/candidates/formalized_hard_m1_squarefree_radical_reduction.md;
7. rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_radical_connector_capacity_audit.md;
8. rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/independent_reduction_and_self_return_review.md;
9. rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md;
10. rounds/codex-managed/m9-m1-square-root-product-offdiagonal/synthesis.md;
11. rounds/codex-managed/m9-m1-near-product-delta-salie/synthesis.md;
12. rounds/codex-managed/full-proof-round179-181-strategy-literature-review/synthesis.md.

The direct accepted inputs are the Round-181 exact product/squarefree
reduction, literal support and divisor bounds, and its two target-safe
sectors. No web source, source theorem, numerical evidence, sibling
Round-183 report, or excluded context was used.

## 7. Recommended state effect

**Revise or extend only the existing mechanism obstruction.** The exact
new durable statement is that even with the strict small-\(t\) cutoff, and
even after discarding the absolutely target-safe Möbius tail \(a\ge T\),
the \(a<T\) kernel returns the original literal hard product wave modulo
\(O_\varepsilon(L^{3/2}X^\varepsilon)\). This may be recorded as a
small-\(t\), target-scale refinement of
M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction.

**Retain the owner open.** Condition (1.9) is an exact sufficient
fixed-row correlation interface, but no estimate for it is proved. It
should remain candidate/inconclusive evidence and should not replace the
one-absolute-value owner or become a necessary condition. It neither
proves nor refutes the literal scalar.

No new owner-compatible strict sector of the original sum is obtained:
the safe \(a\ge T\) tail is a signed Möbius-expansion piece, not a disjoint
literal sector. If the other Round-183 reports do not prove a literal
sector, this task supports the terminal label
small_t_signed_mechanism_capacity_or_self_return_no_go. Keep
M9-M1-top-endpoint-signed-cone, the smooth M1 parent, M9-M1, every M2
parent, endpoint uniformity, M9, both bridges, and the Gauss-circle target
unchanged. The internal exponent remains \(1/3\), the accepted external
benchmark remains \(0.3144831759740614\ldots\), and the target remains
\(1/4\).
