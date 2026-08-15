# Round 55 discovery report: low angular legs are target-safe

## 1. Result: an actual-profile margin theorem

Let \(I_Y\subset[cY,CY]\cap\mathbb Z\) be a consecutive top radial
block, where the fixed constants \(c,C>0\) are independent of \(X\), and

\[
 Y\asymp\sqrt X,\qquad R\asymp\sqrt Y,\qquad |I_Y|\asymp Y.
\]

For every consecutive product window \(J\subseteq I_Y\) of length at most
\(R\), including every edge window, the exact union-of-margins coefficient
in the Round-55 packet satisfies

\[
 \boxed{\left|
 \sum_{n\in J}^{*} A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})
 \right|
 \ll \frac{H+Q}{\sqrt Y}.}                                  \tag{1.1}
\]

The implied constant depends only on the fixed block constants and accepted
profiles.  No \(X^\varepsilon\) is needed in (1.1).  The exact finite
Fejer identity consequently gives

\[
 \boxed{|S_{Y;H,Q}|\ll H+Q.}                                \tag{1.2}
\]

Thus every margin with
\[
 H+Q\leq(\log(2X))^B
\]
is \(O_{\varepsilon,B}(X^\varepsilon)\), hence target-safe in the
normalized physical radial sum.

There is also an asymmetric strengthening forced by the actual angular
support.  If an active summand with \(n=hq\) is nonzero, then

\[
 q\geq 4h,\qquad q\geq2\sqrt n,\qquad h\leq\frac12\sqrt n.  \tag{1.3}
\]

Consequently the entire \(q\)-low margin is identically zero whenever
\[
 Q<2\sqrt{cY}.                                               \tag{1.4}
\]
In particular it is empty for every polylogarithmic \(Q\), once \(X\) is
large.  The substantive positive theorem is therefore the low-\(h\)
curvature estimate.

After taking \(H=Q=(\log(2X))^B\), the exact survivor is

\[
 \boxed{
 A^{\mathrm{core}}_{X;H,Q}(n)=
 \sum_{\substack{hq=n,\ q\ {\rm odd}\\h>H,\ q>Q}}
 \chi_4(q)\Omega_X^*(n,h),}                                 \tag{1.5}
\]

with the additional actual cone \(q\geq2\sqrt n\) and
\(h\leq\sqrt n/2\).  Estimate (1.2) does not control this balanced
product core.

## 2. Exact statement and hypotheses

Write \(\tau_X(n)\) for the prescribed radial endpoint weight: it is one
away from the global radial endpoint and one half at an included starred
endpoint.  For a fixed \(h\), define

\[
\begin{split}
 T_h(J)
 ={}&\sum_{\substack{q\ {\rm odd}\\hq\in J}}
 \tau_X(hq)\chi_4(q)\Omega_X^*(hq,h)(hq)^{-3/4}
 e(\sqrt{Xhq}),                                             \tag{2.1}\\
 a_h(q)
 ={}&\tau_X(hq)\Omega_X^*(hq,h)(hq)^{-3/4}.
\end{split}
\]

For a fixed odd \(q\), with the overlap assigned to the \(h\)-low family,
define

\[
\begin{split}
 U_q(J;H)
 ={}&\chi_4(q)\sum_{\substack{h>H\\hq\in J}}
 \tau_X(hq)\Omega_X^*(hq,h)(hq)^{-3/4}
 e(\sqrt{Xhq}),                                             \tag{2.2}\\
 b_q(h)
 ={}&\mathbf1_{h>H}\tau_X(hq)\Omega_X^*(hq,h)(hq)^{-3/4}.
\end{split}
\]

This is a disjoint owner rule:

\[
 \sum_{n\in J}^{*}A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})
 =\sum_{h\leq H}T_h(J)
  +\sum_{\substack{q\leq Q\\q\ {\rm odd}}}U_q(J;H).          \tag{2.3}
\]

No incidence in the overlap \(h\leq H,q\leq Q\) is counted twice.

The exact sampled-amplitude theorem is

\[
 \boxed{
 \|a_h\|_{\mathrm{BV}(J,h)}
 +\|b_q\|_{\mathrm{BV}(J,q)}
 \ll Y^{-3/4},}                                             \tag{2.4}
\]

where each norm is supremum plus discrete variation on its own sampled
integer or odd-integer interval.  Empty intervals contribute zero.
Equation (2.4) includes the height floors, the moving height cutoffs in the
fixed-\(q\) sum, every angular equality star, the one-sided hard-top jump,
the radial endpoint star, and the artificial edge of \(h>H\).

For \(t\geq1\), put

\[
 \mathcal B_R(t)=
 \min\left\{
 \frac Rt+1,\
 \sqrt R+\frac{\sqrt R}{t}+\frac{t}{\sqrt R}
 \right\}.                                                  \tag{2.5}
\]

The strongest uniform fixed-leg bounds obtained here are

\[
 \boxed{
 |T_h(J)|\ll Y^{-3/4}\mathcal B_R(h),\qquad
 |U_q(J;H)|\ll Y^{-3/4}\mathcal B_R(q).}                    \tag{2.6}
\]

Thus \(\mathcal B_R(t)\ll\sqrt R+1\) uniformly.  More precisely,
curvature gives \(O(\sqrt R)\) for \(t\leq\sqrt R\), while trivial
summation gives \(O(R/t+1)\) for \(t>\sqrt R\).  On the actual support of
\(U_q\), (1.3) gives \(q\gg R\), and hence the sharper estimate

\[
 \boxed{|U_q(J;H)|\ll Y^{-3/4}.}                            \tag{2.7}
\]

For later exponent bookkeeping, (2.6) also gives

\[
 \sum_{h\leq H}\mathcal B_R(h)
 \ll
 \begin{cases}
 H\sqrt R,&H\leq\sqrt R,\\
 R\left(1+\log(2H/\sqrt R)\right),&
       \sqrt R<H\ll R.
 \end{cases}                                                \tag{2.8}
\]

The harmless \(O(R)\) term arising from the \(+1\)'s has been absorbed in
the second line.

## 3. Proof and derivation

### 3.1 An internal second-derivative lemma

We use the following elementary finite lemma.  If \(F\in C^2(\mathcal I)\),
\(F''\) has one sign, and

\[
 \lambda\leq |F''(x)|\leq A\lambda
\]

on an interval containing \(M\) consecutive integers, with
\(0<\lambda\leq1\), then

\[
 \left|\sum_{m\in\mathcal I\cap\mathbb Z}e(F(m))\right|
 \ll_A M\sqrt\lambda+\lambda^{-1/2}.                        \tag{3.1}
\]

For completeness, take \(\delta=\sqrt\lambda\).  Since \(F'\) is
monotone, the portions on which its distance from an integer is less than
\(\delta\) have total integer length
\[
 O_A\big((M\lambda+1)\delta/\lambda\big)
 =O_A(M\sqrt\lambda+\lambda^{-1/2}).
\]
The complementary pieces number \(O_A(M\lambda+1)\).  On each one, the
elementary monotone first-derivative summation estimate is
\(O(\delta^{-1})\).  Their combined contribution has the same bound.
This proves (3.1).  When \(\lambda>1\), we use the trivial bound \(M\).
Abel summation shows that a sampled amplitude of sup-plus-variation \(V\)
multiplies the right side by \(O(V)\).

### 3.2 Exact fixed-leg phases and crossover

For fixed \(h\), write \(q=2m+1\).  Since

\[
 \chi_4(2m+1)=(-1)^m=e(m/2),
\]

the complete phase, including the character, is

\[
 F_h(m)=\sqrt{Xh(2m+1)}+\frac m2.                            \tag{3.2}
\]

The linear character phase does not change curvature, and

\[
 |F_h''(m)|
 =\sqrt{Xh}\,(2m+1)^{-3/2}
 \asymp\frac{\sqrt X\,h^2}{Y^{3/2}}
 \asymp\frac{h^2}{R}.                                      \tag{3.3}
\]

The \(m\)-interval has \(M_h\ll R/h+1\) samples.  When
\(h\ll\sqrt R\), (3.1) gives

\[
\begin{split}
 M_h\left(\frac{h^2}{R}\right)^{1/2}
 +\left(\frac{h^2}{R}\right)^{-1/2}
 &\ll
 \sqrt R+\frac{h}{\sqrt R}+\frac{\sqrt R}{h}.               \tag{3.4}
\end{split}
\]

For \(h\gg\sqrt R\), trivial summation gives \(R/h+1\).
The bounded transition \(h\asymp\sqrt R\) is covered by either estimate.
Combining (3.4), trivial summation, (2.4), and Abel summation proves the
first half of (2.6).

For fixed odd \(q\), the character is one constant unit scalar and

\[
 G_q(h)=\sqrt{Xqh},\qquad
 |G_q''(h)|
 =\frac14\sqrt{Xq}\,h^{-3/2}
 \asymp\frac{\sqrt X\,q^2}{Y^{3/2}}
 \asymp\frac{q^2}{R}.                                      \tag{3.5}
\]

There are \(M_q\ll R/q+1\) sampled \(h\)'s.  The same argument proves the
second half of (2.6).  On actual support \(q\gg R\), so \(M_q=O(1)\);
this proves (2.7) without any curvature assertion.

This establishes the intended curvature/trivial crossover at
\(t\asymp\sqrt R\).  No first-derivative gap, modular nonresonance, or
unproved character cancellation is used.

### 3.3 Sampled BV of the complete actual amplitude

For \(n=hq\), write the angular coordinate as

\[
 d(h,q)=2h\sqrt{X/n}=2\sqrt{Xh/q}.                           \tag{3.6}
\]

As \(n\) moves through a product window of length at most \(R\) inside
\([cY,CY]\), the ratio of its largest and smallest values is
\(1+O(R/Y)=1+O(Y^{-1/2})\).  Hence the range of \(d\) has ratio
\(1+O(Y^{-1/2})\).  Since the scales \(D_j\) are dyadic and every
\(w_j\) has fixed annular support, only \(O(1)\) scale profiles can meet
this range.

For fixed \(h\), the quantities

\[
 \mathbf1_{h\leq H_j}\Phi\left(\frac h{H_j+1}\right)
\]

are constants.  The coordinate \(d(h,q)\) is monotone in \(q\), so
composition with it cannot increase the fixed total variation of any
interior profile.  The top profile contributes its one full hard jump when
\(d\) crosses \(y\).  A prescribed equality star changes only the endpoint
sample at its monotone crossing and adds \(O(1)\) variation.  There are
only \(O(1)\) relevant scales.  Therefore

\[
 \sup_q|\Omega_X^*(hq,h)|
 +\sum_q|\Omega_X^*(h(q+2),h)-\Omega_X^*(hq,h)|
 \ll1,                                                       \tag{3.7}
\]

where the sum is on the relevant odd \(q\)-interval.

For fixed \(q\), the coordinate \(d(h,q)\) is monotone in \(h\).  For each
of the same \(O(1)\) relevant scales,

\[
 h\longmapsto
 \mathbf1_{h\leq H_j}\Phi\left(\frac h{H_j+1}\right)          \tag{3.8}
\]

has uniformly bounded sampled variation: \(\Phi\in C^1[0,1]\), and the
floor \(H_j\) is a fixed integer, so the cutoff has at most one full jump.
This explicitly counts the moving height seam.  The product inequality

\[
 \operatorname {Var}(uv)
 \leq\|u\|_\infty\operatorname {Var}(v)
    +\|v\|_\infty\operatorname {Var}(u)                      \tag{3.9}
\]

then gives the fixed-\(q\) analogue of (3.7).  The disjoint owner
\(\mathbf1_{h>H}\) adds one more full variation jump.

Finally, \(n^{-3/4}\asymp Y^{-3/4}\), and its supremum plus variation on a
monotone product window is \(O(Y^{-3/4})\).  The radial endpoint star
changes at most one sample and contributes another
\(O(Y^{-3/4})\).  Equations (3.7)--(3.9) prove (2.4).  Notice that a star
changes a point value, whereas the top cutoff and a height cutoff are
counted as full jumps; neither is silently smoothed.

### 3.4 Actual angular support and the empty low-\(q\) margin

The accepted top profile is zero for \(d>y=\lfloor\sqrt X\rfloor\), and
every interior active profile is already zero below that hard ceiling.
Thus \(\Omega_X^*(hq,h)\ne0\) implies

\[
 2\sqrt{\frac{Xh}{q}}\leq y.
\]

Consequently

\[
 q\geq\frac{4X}{y^2}h\geq4h.                                \tag{3.10}
\]

Since \(n=hq\), (3.10) gives \(q^2\geq4n\) and
\(h^2\leq n/4\), proving (1.3).  If \(n\geq cY\), then
\(q\geq2\sqrt{cY}\), proving (1.4).  Equality \(d=y\), including its
prescribed half weight, still satisfies the non-strict inequalities and
does not alter the conclusion.

### 3.5 Margin and \(H,Q\) ledgers

Summing (2.6) under the disjoint decomposition (2.3) gives the strongest
direct window ledger

\[
\begin{split}
 \left|\sum_{n\in J}^{*}A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll Y^{-3/4}\left\{
 \sum_{h\leq H}\mathcal B_R(h)
 +\sum_{\substack{q\leq Q,\ q\ {\rm odd}\\q\geq2\sqrt{cY}}}
 \left(\frac Rq+1\right)\right\}.                            \tag{3.11}
\end{split}
\]

The second sum is empty below the threshold (1.4).  The uniform bound
\(\mathcal B_R(t)\ll\sqrt R+1\), together with
\(\sqrt R\asymp Y^{1/4}\), proves (1.1).  Formula (2.8) gives the sharper
low-\(h\) ledger

\[
 B_H(J)\ll
 \begin{cases}
 H\,Y^{-1/2},&H\leq Y^{1/4},\\
 Y^{-1/4}\big(1+\log(2H/Y^{1/4})\big),&
       Y^{1/4}<H\ll Y^{1/2}.
 \end{cases}                                                \tag{3.12}
\]

If \(H=Y^\alpha\), the eventual full-block loss derived from (3.12) is
\(Y^\alpha\) for \(0\leq\alpha\leq1/4\), and at most
\(Y^{1/4}\log Y\) thereafter.  A \(q\)-margin with
\(Q=Y^\beta\), \(\beta<1/2\), is empty; once \(Q\) crosses the actual
\(\sqrt Y\) cone it is no longer a target-sized low margin by this method.

### 3.6 Exact Fejer propagation and edge windows

Extend the margin sequence by zero outside \(I_Y=[a,b]\), put
\[
 W_k=\sum_{s=0}^{R-1}c_{k+s},
\]
and let \(B=(H+Q)/\sqrt Y\) denote the right side of (1.1).
Every \(W_k\) is exactly a product-window sum on
\(I_Y\cap[k,k+R-1]\), including the two shortened edge windows and any
radial star.  Hence \(|W_k|\ll B\).  The exact Fejer energy is

\[
 \mathfrak F_{Y,R}^{H,Q}
 =\frac1R\sum_{k=a-R+1}^{b}|W_k|^2
 \ll\frac{|I_Y|+R-1}{R}\frac{(H+Q)^2}{Y}
 \ll\frac{(H+Q)^2}{\sqrt Y}.                                \tag{3.13}
\]

This is \(O_{\varepsilon,B}(X^\varepsilon R/Y)\), the Round-54 target
energy, when \(H+Q\) is polylogarithmic.  The exact finite Fejer inequality
then yields

\[
 |S_{Y;H,Q}|^2
 \leq\frac{|I_Y|+R-1}{R}\mathfrak F_{Y,R}^{H,Q}
 \ll(H+Q)^2,                                                 \tag{3.14}
\]

proving (1.2).  Equivalently, the identity
\(R S_{Y;H,Q}=\sum_{k=a-R+1}^{b}W_k\) gives the same constant ledger
directly.  No complete-window assumption is made at either edge.

## 4. First doubtful or unproved step

There is no unproved step in the low-margin theorem (1.1)--(1.4).  The
first remaining step is the same balanced signed product correlation, but
with all low angular legs removed:

\[
 \sum_{n\in I_Y}^{*}n^{-3/4}e(\sqrt{Xn})
 \sum_{\substack{hq=n,\ q\ {\rm odd}\\
                  h>(\log(2X))^B,\ q>(\log(2X))^B}}
 \chi_4(q)\Omega_X^*(n,h).                                  \tag{4.1}
\]

On actual support, \(q\geq2\sqrt n\asymp\sqrt Y\), so the \(q\)-lower
cutoff in (4.1) is redundant.  The unresolved range can be written more
sharply as

\[
 (\log(2X))^B<h\ll\sqrt Y,\qquad
 q=\frac nh\geq2\sqrt n\asymp\sqrt Y.                       \tag{4.2}
\]

Summing the lawful one-dimensional estimates through the whole range
\(h\ll\sqrt Y\) gives only the \(Y^{1/4}\)-scale absolute loss in
(3.12).  Thus curvature removes every polylogarithmic margin but does not
produce cancellation between the remaining distinct \(h\)-legs or product
fibers.  That interaction is the first survivor.

The result is a physical radial theorem only.  It does not transfer the
balanced estimate, or even the low-margin estimate, through the finite
connector-completed alpha operator without a separate common-antecedent
Plemelj and outside-height transfer.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| fixed_leg_phase | Pass.  The odd-\(q\) character is the exact linear shift \(m/2\) in (3.2); fixed \(q\) retains its constant \(\chi_4(q)\). |
| curvature_trivial_crossover | Pass.  Equations (3.3)--(3.5) use curvature for \(t\lesssim\sqrt R\) and the exact interval length \(R/t+O(1)\) above it. |
| sampled_profile_BV | Pass.  Only \(O(1)\) dyadic scales meet one moving window; monotone composition, (3.8), and (3.9) prove the complete sampled BV bound (2.4). |
| height_floor_and_stars | Pass.  \(H_j\) is fixed in \(X,j\); its fixed-\(q\) cutoff contributes one full sampled jump.  Equality stars alter endpoint samples and are counted separately from hard jumps. |
| moving_window_edges | Pass.  Every shortened edge interval is one of the windows controlled in (1.1), and (3.13) keeps all \(L+R-1\) window starts. |
| perfect_fourth_power | Pass.  If \(X=K^4\), then \(Y\asymp K^2\), \(R\asymp K\), and the small-leg curvature is \(t^2/K\).  Even when a first derivative plus the character shift is an integer or half-integer, (3.1) gives \(O(\sqrt K)\); for \(t>\sqrt K\) the proof is trivial.  No derivative-gap claim is used. |
| H_Q_ledger | Pass.  Equations (3.11)--(3.14) give the exact moving-window and Fejer losses; polylogarithmic margins are target-safe. |
| double_counting | Pass.  Formula (2.3) assigns the overlap to \(h\leq H\) and imposes \(h>H\) in every fixed-\(q\) term. |
| balanced_core_scope | Pass.  The surviving coefficient is exactly (1.5), sharpened by (4.2); no estimate for it is asserted. |
| downstream_scope | Pass.  GAR, the alpha transition, M9-M1, M9, and the Gauss-circle target remain open. |

The perfect-fourth-power check also explains why the character cannot be
used through an unverified first-derivative gap.  At resonant centers that
gap may vanish; curvature still gives precisely the square-root window
bound used above.

## 6. Dependencies and exact artifacts used

Only the task-authorized artifacts were used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-top-block-low-leg-curvature/derivation_packet.md;
- rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md;
- rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/synthesis.md;
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md.

The second-derivative estimate was proved internally in Section 3.1.  No
external theorem, web source, or numerical experiment was used.  The round
allocation for this report is 100% analytical/algebraic.

## 7. Recommended state effect

Promote, after independent seam validation, a scoped
top-block-low-angular-leg node consisting of:

1. the complete actual-profile sampled BV theorem (2.4);
2. the fixed-leg crossover theorem (2.6), with the stronger active
   fixed-\(q\) bound (2.7);
3. the angular-cone support law (1.3);
4. the moving-window and Fejer margin estimates (1.1)--(1.2).

Record explicitly that the polylogarithmic \(q\)-margin is empty, rather
than attributing its control to character cancellation.  Revise the next
action for the open top-block problem to the core (4.1)--(4.2), where
distinct surviving \(h\)-legs must interact before absolute values.

Do not promote the full shifted-correlation theorem, GAR, the alpha
transition, M9-M1, M9, or the final Gauss-circle theorem.
