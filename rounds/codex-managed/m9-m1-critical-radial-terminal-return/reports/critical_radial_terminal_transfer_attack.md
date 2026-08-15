# Critical radial terminal transfer attack

- Campaign: m9-m1-critical-radial-terminal-return
- Round: 60
- Task: critical_radial_terminal_transfer_attack
- Role: discovery
- Status: candidate evidence only; no shared state was edited
- Method allocation: entirely analytic; no numerical experiment and no web source

## 1. Result

The fixed-relative-width critical radial sector does return to the already
proved terminal M1 coefficient class.  More precisely, put

\[
 R=X^{1/4},\qquad Y=R^2=\sqrt X,
\]

and let \(V\in C_c^\infty((c,C))\) be fixed and real valued, where
\(0<c<C<16\).  For the exact Round-14 coefficient

\[
 \mathcal C_X^*(n)=
 \sum_{\substack{h\mid n\\q=n/h,\ q\ {\rm odd}}}
 \chi_4(q)\Omega_X^*(n,h),
\]

\[
 \Omega_X^*(n,h)=
 \sum_j{\bf1}_{h\leq H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{\frac Xn}\right)\right]^*,
\]

define

\[
 \mathcal G_V(X)=
 \sum_{n\leq16Y}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn}).
\tag{1.1}
\]

Then

\[
 \boxed{\operatorname {Re}\{e(1/8)\mathcal G_V(X)\}
 \ll_{\varepsilon,V}X^\varepsilon.}
\tag{1.2}
\]

The common antecedent is a radially masked reciprocal M1 aggregate.  It is
Mellin-separable into terminal frequency blocks, so the accepted
frequency-first divisor theorem bounds it in complex modulus by
\(O_{\varepsilon,V}(RX^\varepsilon)\).  The accepted positive-frequency
interior character B-process and positive one-sided hard-top transform,
rerun with the fixed smooth radial multiplier, give the separate complex
identity

\[
 \mathfrak B_V(X):=\sum_j\mathcal B_{j,V}
 =\frac{e(1/8)}{i}R\mathcal G_V(X)+\mathcal E_V^+(X),
\qquad
 |\mathcal E_V^+(X)|\ll_V\log^2(2X).
\tag{1.3}
\]

Consequently this argument actually proves the stronger corollary

\[
 \boxed{|\mathcal G_V(X)|\ll_{\varepsilon,V}X^\varepsilon.}
\tag{1.4}
\]

For real \(V\), pairing the negative frequency gives the frozen GAR
projection in the exact form

\[
 \mathfrak M_V(X)=
 -\frac4\pi R\operatorname {Re}\{e(1/8)\mathcal G_V(X)\}
 +\mathcal E_V(X),
\qquad
\mathcal E_V(X)\ll_V\log^2(2X).
\tag{1.5}
\]

Thus division by \(R\) proves (1.2), while (1.4) is obtained before
negative-frequency pairing.  It is not inferred from the one fixed real
projection: its proof uses the separately accepted positive-frequency
transform and its absolute complex error ledger.

## 2. Exact statement and hypotheses

Let \(D_j=2^{-j}\lfloor\sqrt X\rfloor\) and
\(H_j=\lfloor D_j/R\rfloor\), with the exact accepted active denominator
profiles \(w_j\).  Every active profile has support in a fixed shell

\[
 a_0D_j\leq d\leq b_0D_j
\tag{2.1}
\]

for absolute \(a_0,b_0>0\); exactly one top profile is one-sided at
\(y=\lfloor\sqrt X\rfloor\).  The accepted height ledger gives, whenever
\(H_j\) is not in a bounded exceptional range,

\[
 \frac12\,\frac{D_j}{R}\leq H_j\leq\frac{D_j}{R}.
\tag{2.2}
\]

Choose \(c_V,C_V\) with

\[
 0<c<c_V\leq z\leq C_V<C<16
\tag{2.3}
\]

on the support of \(V\).  If
\(V(4R^2h^2/d^2)w_j(d)\neq0\), then

\[
 h\geq\frac{\sqrt{c_V}}2\frac dR
 \geq\frac{a_0\sqrt{c_V}}2\frac{D_j}{R}
 \gg_V H_j.
\tag{2.4}
\]

The exact pre-existing condition \(h\leq H_j\), rather than a new taper,
owns the upper edge.  Consequently there is a fixed
\(\gamma_V>0\) and a fixed-normalized-BV lower cutoff
\(\eta_j(h)\), equal to one for \(\gamma_VH_j\leq h\leq H_j\), such that
inserting \(\eta_j\) changes no summand.  The endpoint jump at \(h=H_j\)
is retained.  Bounded \(H_j\) is treated directly.

Define the exact reciprocal antecedent

\[
 \mathcal B_{j,V}=
 \sum_{1\leq h\leq H_j}\eta_j(h)
 \frac{\Phi(h/(H_j+1))}{h}
 \sum_d\chi_4(d)w_j(d)
 V\!\left(\frac{4Xh^2}{d^2Y}\right)e(hX/d)
\tag{2.5}
\]

and set

\[
 \mathfrak B_V(X)=\sum_j\mathcal B_{j,V}.
\tag{2.6}
\]

The paired Vaaler-normalized aggregate is

\[
 \mathfrak M_V(X)=
 2\operatorname {Re}\left\{
 -\frac{2i}{\pi}\sum_j\mathcal B_{j,V}\right\}.
\tag{2.7}
\]

The theorem uses the following already accepted interfaces:

1. For a bounded spatial coefficient \(a_d\), supported in a fixed shell
   \(d\asymp D\), and a frequency coefficient \(u\) satisfying
   \[
   \|u\|_\infty+\sum_h|\Delta u(h)|\ll L^{-1},
   \]
   the terminal divisor theorem gives
   \[
   \left|\sum_hu(h)\sum_da_de(hX/d)\right|
   \ll_\varepsilon X^\varepsilon(1+D/L).
   \tag{2.8}
   \]
2. The accepted smooth interior M1 character transform has stationary
   denominator \(d_*=2\sqrt{hX/q}\), \(q\) positive and odd, leading
   factor \(e(1/8)(hX)^{1/4}/i\), phase
   \(e(\sqrt{Xhq})\), the accepted stationary stars, and an absolute
   complex remainder bound before frequency-sign pairing.
3. The unique hard top is transformed one-sidedly with the full sample
   \(d=y\), its explicit character-cotangent boundary, the same stationary
   factor, and its proved Vaaler-weighted error ledger.

No assertion is made for a sharp radial window, for \(n=o(Y)\), or for a
cutoff meeting \(n=16Y\).

## 3. Proof or derivation

### 3.1 Exact Mellin separation

Use the convention

\[
 \widehat V(t)=\int_0^\infty V(z)z^{-it}\frac{dz}{z},
 \qquad
 V(z)=\frac1{2\pi}\int_{\mathbb R}\widehat V(t)z^{it}\,dt.
\tag{3.1}
\]

Since \(V\) is smooth and compactly supported in the positive half-line,
\(\widehat V\) is Schwartz and

\[
 \int_{\mathbb R}|\widehat V(t)|(1+|t|)^A\,dt<\infty
\quad(A\geq0).
\tag{3.2}
\]

The radial factor separates exactly as

\[
 V\!\left(\frac{4Xh^2}{d^2Y}\right)
 =\frac1{2\pi}\int_{\mathbb R}\widehat V(t)
 \left(\frac{4X}{Y}\right)^{it}h^{2it}d^{-2it}\,dt.
\tag{3.3}
\]

Thus the \(t\)-mode of (2.5) has frequency and denominator coefficients

\[
 u_{j,t}(h)=
 {\bf1}_{1\leq h\leq H_j}\eta_j(h)
 \frac{\Phi(h/(H_j+1))}{h}h^{2it},
\qquad
 a_{j,t}(d)=\chi_4(d)w_j(d)d^{-2it}.
\tag{3.4}
\]

On the support of \(u_{j,t}\), \(h\asymp_VH_j\).  The variation of the
lower cutoff, the sampled \(\Phi\), and \(h^{-1}\), including the upper
jump at \(H_j\), costs \(O_V(H_j^{-1})\).  Moreover

\[
 |(h+1)^{2it}-h^{2it}|\leq\frac{2|t|}{h}.
\]

It follows that

\[
 \|u_{j,t}\|_\infty+\sum_h|\Delta u_{j,t}(h)|
 \ll_V\frac{1+|t|}{H_j}.
\tag{3.5}
\]

Also \(|a_{j,t}(d)|\leq1\).  Scaling (2.8) by \(1+|t|\), using
\(D_j/H_j\ll R\), and then (3.2), gives

\[
 |\mathcal B_{j,V}|
 \ll_{\varepsilon,V}X^\varepsilon
 \left(1+\frac{D_j}{H_j}\right)
 \ll_{\varepsilon,V}RX^\varepsilon.
\tag{3.6}
\]

There are \(O(\log X)\) active scales, so, after relabelling
\(\varepsilon\),

\[
 |\mathfrak B_V(X)|+|\mathfrak M_V(X)|
 \ll_{\varepsilon,V}RX^\varepsilon.
\tag{3.7}
\]

If \(H_j=O_V(1)\), then \(D_j=O_V(R)\); direct summation over the
\(O_V(1)\) frequencies and \(O(D_j)\) denominators gives the same
\(O_V(R)\) bound.  Only \(O_V(1)\) dyadic scales lie in this bounded-height
range.  A scale with \(H_j=0\) is empty, and the accepted inactive bottom
range is not part of (1.1).

### 3.2 Coefficient-preserving localized transform

For fixed \(j,h\), set

\[
 A_{j,h,V}(d)=w_j(d)V(4R^2h^2/d^2).
\tag{3.8}
\]

On its support, the logarithmic derivatives are uniformly controlled:

\[
 D_j^k\frac{d^k}{dd^k}A_{j,h,V}(d)\ll_{k,V}1.
\tag{3.9}
\]

Indeed \(d\asymp D_j\), \(h\asymp_VD_j/R\), and
\((d\,d/dd)^kV(4R^2h^2/d^2)=(-2z\,d/dz)^kV(z)\).  Therefore the accepted
interior character B-process applies with the same stationary points,
stars, phase, and constant.  Its stationary portion is

\[
 \frac{e(1/8)(hX)^{1/4}}{i}
 \sum_{\substack{q\geq1\\q\ {\rm odd}}}^{*}
 \chi_4(q)q^{-3/4}
 \left[w_j\!\left(2\sqrt{\frac{hX}{q}}\right)\right]^*
 V(hq/Y)e(\sqrt{Xhq}).
\tag{3.10}
\]

The equality in the new radial factor is exact, because at
\(d_*=2\sqrt{hX/q}\),

\[
 \frac{4Xh^2}{d_*^2Y}=\frac{hq}{Y}.
\tag{3.11}
\]

Equivalently, mode by mode,

\[
 \left(\frac{4X}{Y}\right)^{it}h^{2it}d_*^{-2it}
 =\left(\frac{hq}{Y}\right)^{it}.
\tag{3.12}
\]

The denominator mode is harmless for the transformation as well:
\[
 D_j^k\frac{d^k}{dd^k}\{w_j(d)d^{-2it}\}
 \ll_k(1+|t|)^k.
\tag{3.13}
\]
Hence a modewise proof has only a fixed polynomial loss in \(t\), which is
integrable by (3.2).  Alternatively, (3.8)--(3.9) apply the transform
directly after Mellin inversion.

Multiplying (3.10) by the exact positive Vaaler factor
\(-2i\Phi(h/(H_j+1))/(\pi h)\) gives

\[
 -\frac2\pi e(1/8)R\,
 \Phi\!\left(\frac h{H_j+1}\right)
 (hq)^{-3/4}\chi_4(q)
 \left[w_j\!\left(2\sqrt{\frac{hX}{q}}\right)\right]^*
 V(hq/Y)e(\sqrt{Xhq}).
\tag{3.14}
\]

Here
\[
 (hX)^{1/4}q^{-3/4}h^{-1}
 =R(hq)^{-3/4},
\tag{3.15}
\]
so the external \(R\) occurs exactly once.

Now put \(n=hq\).  Since
\[
 2\sqrt{\frac{hX}{q}}=2h\sqrt{\frac Xn},
\tag{3.16}
\]
summing \(j,h,q\) in (3.14) reconstructs precisely
\(\mathcal C_X^*(n)\), including \({\bf1}_{h\leq H_j}\), the floor
\(H_j\), the sampled \(\Phi\), the profile seam, and every stationary
equality star.  The accepted profile support and \(h\leq H_j\) imply
\(n\leq16Y\); because \(C_V<16\), the artificial radial cutoff does not
meet that hard outer edge.  The inserted \(\eta_j\) is one on every
nonzero stationary term and therefore disappears without altering the
coefficient.

### 3.3 Hard top and the total error

At the unique top profile, the preceding transform is performed
one-sidedly.  Let \(y=\lfloor\sqrt X\rfloor\) and \(q_0=X/y^2\).  The
accepted full-endpoint character boundary is

\[
 E_h^\chi(X)=\frac1{2i}\left\{
 \frac{e(hX/y+y/4)}{1-e(hq_0-1/4)}
 -\frac{e(hX/y+3y/4)}{1-e(hq_0-3/4)}
 \right\}.
\tag{3.17}
\]

For the radial amplitude it becomes exactly

\[
 V(4R^2h^2/y^2)E_h^\chi(X).
\tag{3.18}
\]

The denominators in (3.17) retain their accepted uniform separation.
Since radial support forces \(h\asymp_VH_{\rm top}\), the outer
\(h^{-1}\)-mass is \(O_V(1)\); hence (3.18) contributes \(O_V(1)\).
The included integer \(d=y\) has full weight.  It is not replaced by a
Poisson midpoint, and its missing half is not discarded.

For both an interior scale and the top scale, (3.9) leaves the accepted
one-term transform remainder \(O_V(\log(2+h))\) per frequency.  Therefore

\[
 \sum_{\gamma_VH_j\leq h\leq H_j}
 \frac{\log(2+h)}h\ll_V\log(2+H_j).
\tag{3.19}
\]

Summing the \(O(\log X)\) scales yields, before pairing,
\[
 |\mathcal E_V^+(X)|\ll_V\log^2(2X).
\tag{3.20}
\]
Equations (3.10)--(3.20) first give the complex positive-frequency
identity (1.3).  Combining (1.3), (3.7), and (3.20), and dividing by
\(R\), proves (1.4).

Only then are the positive and negative original frequencies paired,
after all constants and endpoint terms have been retained.  Because
\(V\) and the accepted profiles are real, the negative transform is the
complex conjugate.  This gives (1.5), with
\(-4/\pi\), \(R\), and \(\operatorname {Re}\{e(1/8)\cdot\}\) each
appearing once, and
\[
 \mathcal E_V(X)=
 2\operatorname {Re}\{-2i\mathcal E_V^+(X)/\pi\}
 \ll_V\log^2(2X).
\]
The frozen conclusion (1.2) follows either from (1.4) or directly from
(1.5).

## 4. First doubtful or unproved step

There is no unproved step inside the fixed smooth sector (1.2), or in the
stronger positive-frequency corollary (1.4), conditional
only on the already accepted terminal divisor theorem and accepted
interior/top M1 transforms stated in Section 2.  The new operation is
stable under those interfaces because the direct radial amplitude has the
uniform derivative bounds (3.9), while its Mellin modes have (3.13) and
Schwartz-integrable losses.

The first unproved continuation is radial: as the lower edge of the radial
window approaches \(0\), (2.4) no longer forces \(h\gg H_j\), so the
terminal divisor estimate deteriorates to \(1+D_j/L\) on lower
frequency shells.  A sharp window would additionally introduce radial
endpoints and is outside this theorem.

## 5. Required control tests and outcomes

1. **Mellin_normalization — pass.**  Equations (3.1)--(3.3) use
   \(z^{-it}\) in the forward transform and \(z^{it}\) in inversion.
   The factor is exactly \((4X/Y)^{it}h^{2it}d^{-2it}\).
2. **terminal_support — pass.**  The positive lower radial support gives
   (2.4).  The exact factor \({\bf1}_{h\leq H_j}\) owns the upper edge;
   no condition \(C<9/4\), no strict upper taper, and no removal of
   \(h=H_j\) is used.
3. **frequency_BV — pass.**  Equation (3.5) includes the oscillatory
   \(h^{2it}\) cost and the \(O(H_j^{-1})\) upper endpoint jump.
4. **denominator_mode — pass.**  The coefficient \(d^{-2it}\) has modulus
   one for the terminal theorem, and (3.13) gives only polynomial
   \(t\)-loss in the B-process.  Equation (3.2) absorbs it.
5. **Bprocess_constant — pass, first complex then paired.**  The positive saddle factor is
   \(e(1/8)(hX)^{1/4}/i\).  With the positive Vaaler factor it becomes
   \(-2e(1/8)R/\pi\); pairing signs gives the external
   \(-4R/\pi\) in (1.5).  Without the Vaaler factor or pairing it gives
   the complex coefficient \(e(1/8)R/i\) in (1.3).
6. **hard_top_boundary — pass.**  Equations (3.17)--(3.18) retain the
   character-cotangent term and the full hard sample.  Its terminal
   weighted mass is \(O_V(1)\).
7. **floors_profiles_stars — pass.**  No replacement of
   \(H_j=\lfloor D_j/R\rfloor\) is made in a coefficient.  Equations
   (3.11), (3.16), and the starred transform preserve the actual profile
   arguments and equality half-weights.  The smooth \(V\) creates no
   independent radial star.
8. **small_height — pass.**  Bounded \(H_j\) contributes \(O_V(R)\)
   directly, \(H_j=0\) is empty, and only \(O_V(1)\) scales require this
   treatment.
9. **scale_one_count — pass.**  The sum over \(j\) is the exact accepted
   profile sum defining \(\Omega_X^*\).  The lower cutoff is identically
   one on every surviving incidence.  There is one hard top and no
   duplicated radial partition.
10. **error_sum — pass.**  Boundary and transform remainders total
    \(O_V(\log^2(2X))\), hence are \(O_{\varepsilon,V}(RX^\varepsilon)\)
    on the physical scale.
11. **GAR_implication_scope — pass, with a stronger audited corollary.**
    Equation (1.5) proves exactly the frozen
    \(\operatorname {Re}\{e(1/8)\mathcal G_V\}\ll X^\varepsilon\).
    The modulus conclusion (1.4) is licensed separately by the
    positive-frequency identity (1.3) and the complex terminal bound; it
    is not deduced from the real projection.
12. **downstream_scope — pass.**  The result removes fixed smooth
    \(n\asymp Y\) sectors from the GAR problem.  It proves nothing for
    \(n=o(Y)\), the alpha transition, full GAR, blockwise M9-M1, M9, or
    the final Gauss-circle exponent.

## 6. Dependencies and exact artifacts used

The derivation used only the context authorized by the Round-60 brief:

- protocol.md
- state/proof_obligations.yml, specifically the accepted dyadic-profile,
  terminal-frequency, hard-top M1-transform, global-recombination, and
  elementary-divisor nodes
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-critical-radial-terminal-return/derivation_packet.md
- rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/synthesis.md
- rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md
- rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md
- rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md

The Round-59 synthesis supplied the exact terminal-symbol return to be
tested.  The Round-14 synthesis supplied the authoritative coefficient,
stars, floors, and \(-4R/\pi\) paired normalization.  The Round-10 report
supplied (2.8), including arbitrary bounded complex spatial coefficients
and the hard \(h=H_j\) jump.  The accepted graph supplied the M1-specific
one-sided character boundary; the endpoint report supplied the underlying
full-versus-midpoint and error discipline.  No legacy response, proof
draft, unlisted report, external source, or computation was used.

## 7. Recommended state effect

Promote, after the normal independent seam validation, a scoped
M9-M1-smooth-critical-radial-terminal-transfer lemma consisting of
(1.2)--(1.5) for every fixed real
\(V\in C_c^\infty((c,C))\), \(0<c<C<16\).  Record as proved components:

1. exact Mellin separation and the \((1+|t|)/H_j\) terminal BV ledger;
2. the all-scale reciprocal antecedent bound
   \(\sum_j\mathcal B_{j,V}\ll_{\varepsilon,V}RX^\varepsilon\);
3. the coefficient-preserving saddle identity
   \((4X/Y)^{it}h^{2it}d_*^{-2it}=(hq/Y)^{it}\);
4. the complex positive-frequency identity (1.3), its modulus corollary
   (1.4), and the paired identity (1.5), including the hard top, floors,
   profiles, stars, one-count, and \(O_V(\log^2X)\) errors.

Revise the global-angular-radial obligation by marking every fixed smooth
critical sector \(n\asymp\sqrt X\) as closed, even in complex modulus for
the positive-frequency sum.  Retain the lower radial range, sharp radial
cutoffs, full GAR, blockwise M9-M1, M9, and the final exponent as open.
Do not transfer this
result to the Round-59 short moving strip: that selector is not a fixed
relative-width radial multiplier and is not separable before completion.
