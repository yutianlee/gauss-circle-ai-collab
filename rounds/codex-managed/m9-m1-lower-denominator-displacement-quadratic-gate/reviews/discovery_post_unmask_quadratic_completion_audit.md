# Round 139 post-unmask review: quadratic-completion and directionality seams

## 1. Result

**Decision: green after one precise normalization correction; no certification
of the curvature-collar claim.**  I did not review or certify conductor
equations (139.C1)--(139.C15).  In particular, every statement below about
(139.C28) is conditional on the independently reviewed validity of
(139.C3).

The audited equations have the following status.

| conductor equations | status | exact disposition |
|---|---|---|
| (139.C16)--(139.C17) | **green** | The decomposition and the $q$-uniform bound on $v\le y/2$ are exact. |
| (139.C18) | **green** | With a fixed sufficiently small constant and literal integer endpoint, the correction has uniformly bounded variation on $v\ll(y^2/h)^{1/3}$; $h\ll\sqrt y$ prices the $q$-term. |
| (139.C19) | **green** | The parity-reduced quadratic polynomial and modulus $2y$ are correct for both parities of $y$. |
| (139.C20)--(139.C21) | **green** | The safe complete-Gauss gcd bound and the weighted divisor ledger are correct, including non-coprime and boundary-frequency cases. |
| (139.C22)--(139.C24) | **green** | The fourth-power $h=1$ construction rigorously gives discrete variation $\gg y$ on a literal profile plateau. |
| (139.C25) | **needs precise correction** | With the natural Fourier convention it needs the constant unit $e(C_h)$, and $w_h,\widehat w_h$ must be defined.  The sign of $k$ changes with Fourier convention.  These repairs do not affect any bound or the obstruction. |
| (139.C27) | **green as the accepted input** | It is the Round-138 scalar-square identity; this review does not re-prove Round 138. |
| (139.C28) | **green conditionally on (139.C3)** | It is a chain of target-scale implications after epsilon renaming, not an identity between the tail square and the Round-138 residual. |

The Salié exclusion is green.  Resolving $\chi_4$ leaves an additive
parity projector and an ordinary quadratic Gauss sum.  The exact correction,
profile, $q$-dependence, and moving denominator stay in the coefficient;
there is no complete unit sum with a variable inverse phase.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,
 \qquad 0\le q\le2y.
\tag{R139.1}
\]

The literal profile is fixed, real, smooth, and zero-extended with its
literal endpoint samples.  Its support gives

\[
 h\ll {y-v\over R}\le {y\over R}\ll\sqrt y.
\tag{R139.2}
\]

Only this inherited implication and fixed one-dimensional profile variation
are used in the completion audit.  Bounded $X$ is absorbed into the
implicit constant.

The exact dictionary is

\[
 d=y-v,\qquad 1\le d\le y
 \quad\Longleftrightarrow\quad 0\le v<y,
\tag{R139.3}
\]

and

\[
 {N\over y-v}=y+v+{q+v^2\over y-v}.
\tag{R139.4}
\]

Even $d$ vanish.  If $p_y\in\{0,1\}$ is defined by
$p_y\equiv y-1\pmod 2$, the surviving points are uniquely
$v=p_y+2n$, and

\[
 \chi_4(y-v)=e\!\left({y-v-1\over4}\right).
\tag{R139.5}
\]

For the positive sign, put

\[
 E_{h,q,y}(v)=h{v(q+v^2)\over y(y-v)},
 \qquad
 C_h={hq\over y}+{hp_y^2\over y}-{p_y\over4}+{y-1\over4}.
\tag{R139.6}
\]

For a literal interval $I_h$ in the allowed parity lattice, define

\[
 w_h(n)=\mathbf 1_{p_y+2n\in I_h}
 V_{\rm low}\!\left({4R^2h^2\over(y-p_y-2n)^2}\right)
 e(E_{h,q,y}(p_y+2n)),
\tag{R139.7}
\]

zero-extended to $\mathbb Z/(2y)\mathbb Z$, and use

\[
 \widehat w_h(k)=\sum_{n\bmod 2y}w_h(n)e(-kn/(2y)).
\tag{R139.8}
\]

These definitions remove the ambiguity in conductor equation (139.C25).
The negative sign is the conjugate calculation.  Indeed, on odd $d$,
$e((d-1)/4)=e(-(d-1)/4)\in\{\pm1\}$, so no sign or parity owner is lost.

## 3. Proof or derivation

From $y^2\le X<(y+1)^2$, integrality of $N$ gives
$y^2\le N\le y^2+2y$, proving (R139.1).  Equations
(R139.3)--(R139.5) then prove the displacement and character dictionary in
both directions; $v=y$ and $d=0$ never occur.

For the Taylor seam, direct common-denominator algebra gives

\[
 {q+v^2\over y-v}
 ={q\over y}+{v^2\over y}
  +{v(q+v^2)\over y(y-v)}.
\tag{R139.9}
\]

Moreover,

\[
 E'_{h,q,y}(v)
 ={h\{qy+3yv^2-2v^3\}\over y(y-v)^2}\ge0.
\tag{R139.10}
\]

For $0\le v\le y/2$, $q\le2y$ gives

\[
 0\le E_{h,q,y}(v)
 \le {4hv\over y}+{2hv^3\over y^2}.
\tag{R139.11}
\]

Take

\[
 \ell_h=c\min\left\{y,\left({y^2\over h}\right)^{1/3}\right\}
\tag{R139.12}
\]

with fixed sufficiently small $c$.  On the inherited support
$h\ll\sqrt y$,

\[
 {h\ell_h\over y}\ll c\,h^{2/3}y^{-1/3}\ll1,
 \qquad
 {h\ell_h^3\over y^2}\ll c^3.
\tag{R139.13}
\]

Since $E$ is increasing, (R139.13) bounds its complete phase variation.
Together with the two endpoint jumps and the fixed profile variation, this
makes (139.C18) lawful.  At $q=0$,
$E=hv^3/[y(y-v)]$, so the cubic scale in (R139.12) is also the exact
origin-core obstruction scale.

Substituting $v=p_y+2n$ into the nonconstant quadratic core gives

\[
 {hv^2\over y}-{v\over4}
 =\left({hp_y^2\over y}-{p_y\over4}\right)
 +{8hn^2+(8hp_y-y)n\over2y},
\tag{R139.14}
\]

which verifies (139.C19).  Put $M=2y$ and

\[
 G_M(A,B)=\sum_{n\bmod M}e((An^2+Bn)/M).
\tag{R139.15}
\]

Writing $u=n-n'$ after squaring gives

\[
 |G_M(A,B)|^2
 \le M\#\{u\bmod M:M\mid2Au\}
 =M(2A,M).
\tag{R139.16}
\]

For $A=8h$,

\[
 |G_{2y}(8h,B)|
 \le\{2y(16h,2y)\}^{1/2}.
\tag{R139.17}
\]

If $g=(h,y)$, write $h=gh_0$, $y=gy_0$ with
$(h_0,y_0)=1$.  Then

\[
 (16h,2y)=g(16h_0,2y_0)\le16g,
\tag{R139.18}
\]

so (R139.17) is $O(\sqrt{y(h,y)})$, uniformly in both $y$-parities and
all linear coefficients $B$.  In particular, boundary Fourier modes that
revive a complete-sum zero are already included.

The exact corrected form of (139.C25), with the convention (R139.8), is

\[
 \boxed{
 S_h(I_h):=e(C_h)\sum_{n\bmod M}w_h(n)
 e\!\left({8hn^2+(8hp_y-y)n\over M}\right)
 ={e(C_h)\over M}\sum_{k\bmod M}\widehat w_h(k)
 G_M(8h,8hp_y-y+k).}
\tag{R139.19}
\]

If $e(C_h)$ is absorbed into $w_h$, conductor equation (139.C25) is
literally recovered.  With the opposite Fourier convention, $+k$ becomes
$-k$.  This is a normalization correction, not a mathematical failure.

On the Taylor window, cyclic summation by parts gives

\[
 {1\over M}\sum_{k\bmod M}|\widehat w_h(k)|\ll\log(2y),
\tag{R139.20}
\]

because $\lVert w_h\rVert_\infty+\operatorname{Var}(w_h)\ll1$.  Equations
(R139.17)--(R139.20) and the literal weight give

\[
 \sum_{h\ll\sqrt y}{(h,y)^{1/2}\over h}
 \le \log(2y)\sum_{g\mid y}g^{-1/2}
 \ll_\varepsilon X^\varepsilon.
\tag{R139.21}
\]

This independently verifies (139.C20)--(139.C21) and the target-safe
Taylor window, without using the larger curvature collar.

For the fourth-power control, take $X=N=M_0^4$, so $R=M_0$,
$y=M_0^2$, $q=0$, and $h=1$.  Writing $v=ty$,

\[
 E(v)=yF(t),\qquad F(t)={t^3\over1-t},\qquad
 F'(t)={t^2(3-2t)\over(1-t)^2}.
\tag{R139.22}
\]

By continuity there is a fixed compact $I\subset(0,1)$ with
$1/20\le F'(t)\le1/12$.  For every allowed parity step inside a slightly
smaller copy of $I$, the mean-value theorem gives

\[
 {1\over10}\le E(v+2)-E(v)\le {1\over6}.
\tag{R139.23}
\]

There are $\asymp y$ such steps.  Their chord lengths
$2|\sin(\pi(E(v+2)-E(v)))|$ are bounded below, hence

\[
 \operatorname{Var}_{v\equiv p_y(2)}e(E(v))\gg y.
\tag{R139.24}
\]

On this fixed $t$-interval the $h=1$ profile argument is
$4/[M_0^2(1-t)^2]$, so the literal profile is on its near-zero plateau for
large $M_0$.  Thus (139.C22)--(139.C24) are green and do not rely on an
artificial nonzero coefficient.

Equation (R139.19) is an ordinary additive quadratic Gauss correlation.
Evaluating $G_M$ may introduce the usual quadratic unit, but there is no
sum over units carrying a multiplicative character and an inverse phase.
The reciprocal denominator and all $q$-dependence remain in $w_h$.
Therefore the Salié exclusion is exact.

For directionality, the accepted input is

\[
 |\mathcal F_N|^2=\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).
\tag{R139.25}
\]

If the independently claimed scalar split
$\mathcal F_N=\mathcal C_N+\mathcal S_N$,
$|\mathcal C_N|\ll R\log X$, is valid, the triangle inequality gives

\[
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon.
\tag{R139.26}
\]

Equation (R139.25), in both directions and after epsilon renaming, gives
the second equivalence in (139.C28).  But with $h=ag$, $d=bg$, the collar
condition is $y-bg\le L_{ag}$, which depends on the lift $g$ and splits
the exact $L_\chi(y/b)$ coefficient.  Also

\[
 |\mathcal F_N|^2=|\mathcal C_N|^2+|\mathcal S_N|^2
 +2\Re(\mathcal C_N\overline{\mathcal S_N}),
\tag{R139.27}
\]

and the cross term is not target-square bounded without the open tail
estimate.  Thus (139.C27)--(139.C28) are directionally correct, while a
tail-square identity or a deletion from $\mathcal R_{y^{-2}}$ would fail.

One wording correction accompanies (139.C25): coefficient-blind $L^2$
on a full active interval gives $O(y)$.  The BV/Fourier-$\ell^1$ estimate
with (R139.24) can be worse (for $h=1$, $O(Ry\log y)$) before taking the
minimum with the trivial $O(y)$ bound.  It is accurate to say that these
methods give **no improvement over** the $y^{1+o(1)}$ capacity, not that
each raw inequality equals $y^{1+o(1)}$.

## 4. First doubtful or unproved step

As written, the first doubtful seam is the undefined normalization in
(139.C25): without a definition of $w_h,\widehat w_h$, its missing constant
unit and Fourier sign cannot be checked.  Equation (R139.19) repairs it.

After that repair, the first genuinely unproved analytic step is a signed
estimate for the full-support correlation in (R139.19), jointly in $h$ and
the Fourier/alias index.  Parseval gives only full scalar capacity, while
Fourier inversion reconstructs the reciprocal scalar.  Neither Gauss
evaluation nor the fourth-power BV obstruction supplies the missing signed
cancellation.

Separately, (139.C28) depends on (139.C3).  This review deliberately does
not certify the curvature-collar proof of (139.C3); it certifies only that,
**if (139.C3) is valid**, the scalar and Round-138 directionality asserted in
(139.C27)--(139.C28) is correct.

## 5. Required controls and outcomes

| campaign control | outcome in this scoped seam |
|---|---|
| `exact_N_y2_q_and_displacement_bijection` | **green** by (R139.1)--(R139.4), including both endpoints and both directions. |
| `literal_profile_support_zero_extension_and_both_signs` | **green for the Taylor/completion audit**: (R139.2), (R139.7), and cyclic zero extension retain both hard jumps; the negative sign is conjugate.  The larger curvature collar is not reviewed. |
| `physical_mod_four_carrier_and_y_parity` | **green** by (R139.5) and (R139.14); $y$ odd gives even $v$, $y$ even gives odd $v$. |
| `exact_quadratic_core_and_Taylor_correction` | **green** by (R139.9)--(R139.13), uniformly for $q=0$ and $q=2y$. |
| `small_v_and_terminal_v_boundaries` | **green for the literal Taylor endpoint and zero extension; not certified globally**.  No terminal point is deleted by this audit. |
| `dyadic_h_v_capacity_ledger` | **not reviewed for (139.C1)--(139.C15)**.  The narrower height/gcd ledger (R139.21) is green; no full-survivor capacity claim is promoted here. |
| `quadratic_Gauss_Salie_completion_cost` | **green after correction of (139.C25)**: modulus $2y$, gcd $(16h,2y)$, all Fourier boundary modes, and the exact unit are displayed in (R139.17)--(R139.20).  Salié structure is absent. |
| `stationary_alias_and_half_integer_tubes` | **not re-certified in this seam**.  Only the statement that aliaswise modulus is not supplied by (R139.19) is used. |
| `q_zero_q_max_and_real_centre_uniformity` | **green for the audited formulas**: (R139.11)--(R139.13) cover $q=2y$, and (R139.22)--(R139.24) cover $q=0$ fourth powers.  Floors enter only through exact $y,N,q$. |
| `map_back_to_round138_exact_residual` | **green only as conditional scalar target equivalence; red as an owner deletion** by (R139.25)--(R139.27). |
| `noninvertibility_directionality_and_self_return` | **green for the completion seam**: (R139.19) is invertible Fourier completion.  No claim about noninvertibility of the unreviewed curvature collar is made. |
| `lower_GAR_and_downstream_scope` | **green**: none of the audited algebra closes the full scalar, lower GAR, a direct M1 parent, M9-M1, any M2 parent, endpoint uniformity, M9, the quarter bridge, or an exponent. |

No numerical experiment, external theorem, centre average, arbitrary
coefficient replacement, or positive residual sub-square was used.

## 6. Dependencies and exact artifacts used

This post-unmask review used exactly:

- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/blind_displacement_scalar_feasibility.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/displacement_completion_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md`.

All displayed formulas were recomputed rather than accepted from either
report.  No numerical or symbolic computation, web source, additional round
artifact, candidate edit, or shared-state edit was used.

## 7. Recommended state effect

Accept conductor equations (139.C16)--(139.C24) as green.  Replace or
explicitly define (139.C25) by (R139.19), including the constant unit and
Fourier convention, and revise its capacity prose to “no improvement over
the trivial $y^{1+o(1)}$ capacity.”  Accept the Salié exclusion.

Accept (139.C27)--(139.C28) only as the stated scalar-level target
equivalence, conditional on a separate independent certification of
(139.C3).  Explicitly reject any inference that the displacement split
deletes a sub-square of $\mathcal R_{y^{-2}}$ or that its lift-dependent
cutoff preserves the complete Round-138 reduced coefficient.

This review makes no finding on (139.C1)--(139.C15), does not certify the
curvature collar, and licenses no full scalar, lower-GAR, M9-M1, M9,
quarter-scale, or exponent promotion.
