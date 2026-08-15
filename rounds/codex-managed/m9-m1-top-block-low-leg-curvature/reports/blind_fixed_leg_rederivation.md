# Blind rederivation: fixed-leg curvature on the top block

## 1. Result

**Fixed-leg margin lemma.** Let \(I_Y\) and the integer \(R\) satisfy the
packet hypotheses

\[
 Y\asymp \sqrt X,\qquad R\asymp \sqrt Y,\qquad
 1\le R\le |I_Y|,
\]

and let \(J\subseteq I_Y\) be any consecutive product interval with
\(|J|\le R\), including an edge interval. Under the stated fixed-dyadic
profile, normalized smoothness, bounded-overlap, Vaaler \(C^1\), and
one-sided hard-top hypotheses, the exact sampled amplitudes have uniform
supremum plus variation. Consequently,

\[
 \left|\sum_{n\in J}^{*}
 A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon
 X^\varepsilon {H+Q\over\sqrt Y}.                            \tag{1}
\]

For each fixed leg \(\ell=h\) or \(\ell=q\), the unweighted phase sum costs
at most

\[
 \sqrt R.
\]

When \(\ell\le\sqrt R\), this follows from the second-derivative estimate
with curvature \(\lambda_\ell\asymp\ell^2/R\); when
\(\ell>\sqrt R\), the complementary product interval has at most
\(R/\ell+O(1)\le\sqrt R+O(1)\) samples and trivial summation gives the same
bound. The crossover is therefore exactly at

\[
 \ell=\sqrt R\asymp Y^{1/4}\asymp X^{1/8}.                   \tag{2}
\]

If \(L=|I_Y|\) and the window star means the exact weights inherited from
the original block rather than new half-weights at artificial window
edges, the moving-window identity has the exact loss

\[
 {L+R-1\over R}.
\]

Thus (1) implies

\[
 S_{Y;H,Q}\ll_\varepsilon X^\varepsilon(H+Q).                \tag{3}
\]

In particular, polylogarithmic \(H+Q\) is target-safe. The remaining
arithmetic object is precisely the balanced core

\[
 h>H,\qquad q>Q,\qquad q\ {\rm odd},\qquad hq\asymp Y.        \tag{4}
\]

This positive low-margin result does not estimate that core or any
downstream shifted correlation.

## 2. Exact statement and hypotheses

For a finite ordered set \(\mathcal T=\{t_1<\cdots<t_s\}\), define the
sampled BV norm

\[
 \|a\|_{\operatorname{SBV}(\mathcal T)}
 =\max_{1\le i\le s}|a(t_i)|
  +\sum_{i=1}^{s-1}|a(t_{i+1})-a(t_i)|.                      \tag{5}
\]

The profile hypotheses in the packet imply, uniformly for every product
window \(J\), the following two estimates:

\[
\begin{aligned}
 &\left\|q\longmapsto\Omega_X^*(hq,h)\right\|_
   {\operatorname{SBV}(\{q:hq\in J,\ q\equiv a\!\!\pmod4\})}
   \ll_\varepsilon X^\varepsilon
   &&(a=1,3),                                                  \tag{6}\\
 &\left\|h\longmapsto\Omega_X^*(hq,h)\right\|_
   {\operatorname{SBV}(\{h:hq\in J\})}
   \ll_\varepsilon X^\varepsilon
   &&(q\ {\rm odd}).                                          \tag{7}
\end{aligned}
\]

The same bounds hold after restricting the \(h\)-set by \(h>H\). That
restriction inserts at most one additional sampled jump. Since \(n\asymp
Y\) on \(I_Y\), multiplication by the exact inherited radial endpoint
weight and by \(n^{-3/4}\) gives

\[
\begin{aligned}
 &\left\|q\longmapsto (hq)^{-3/4}\Omega_X^*(hq,h)\right\|_
   {\operatorname{SBV}}\ll_\varepsilon
   X^\varepsilon Y^{-3/4},                                   \tag{8}\\
 &\left\|h\longmapsto (hq)^{-3/4}\Omega_X^*(hq,h)\right\|_
   {\operatorname{SBV}}\ll_\varepsilon
   X^\varepsilon Y^{-3/4}.                                   \tag{9}
\end{aligned}
\]

All stars in (6)--(9) are the exact stored equality values. No profile star
is replaced by a smoothing convention.

The exponential-sum input used below is the standard finite
second-derivative lemma: if \(F\in C^2\) on a real interval containing
\(L\) consecutive integers and

\[
 \lambda\le |F''(t)|\le C\lambda,
\]

then, uniformly on every integer subinterval,

\[
 \left|\sum e(F(m))\right|
 \ll_C L\lambda^{1/2}+\lambda^{-1/2}.                         \tag{10}
\]

Only the regime \(\lambda\ll1\), up to harmless fixed rescaling constants,
is used. Amplitudes satisfying (5) are inserted by Abel summation, which
multiplies the uniform unweighted bound by their sampled BV norm.

To count the union \(h\le H\) or \(q\le Q\) once, use the disjoint owner
rule

\[
 \mathcal M_H=\{h\le H,\ q\ {\rm odd}\},\qquad
 \mathcal M_Q=\{q\le Q,\ q\ {\rm odd},\ h>H\}.                \tag{11}
\]

Thus every overlap term \(h\le H,\ q\le Q\) belongs only to
\(\mathcal M_H\).

## 3. Proof and exponent ledger

### Sampled profile variation

Write the angular coordinate as

\[
 u(n,h)=2h\sqrt{X/n}.
\]

For fixed \(h\), with \(n=hq\), this is
\[
 u=2\sqrt{Xh/q},
\]
and is strictly decreasing in \(q\). For fixed \(q\), with \(h=n/q\), it
is
\[
 u={2\sqrt{Xn}\over q},
\]
and is strictly increasing in \(h\). In either case, as \(n\) crosses a
window of length at most \(R\) inside \(n\asymp Y\),

\[
 {|\Delta u|\over u}\ll {R\over Y}\asymp {1\over R}.         \tag{12}
\]

Fixed dyadic support and bounded overlap therefore restrict the union of
active profile indices \(j\) on one product window to \(O(1)\) indices
(or, under a merely logarithmic global profile count, to
\(O(\log(2X))\), which is absorbed by \(X^\varepsilon\)).

For fixed \(h\), the factors

\[
 \mathbf1_{h\le H_j}\Phi\!\left({h\over H_j+1}\right)
\]

are constant in \(q\). The monotone coordinate crosses each smooth profile
with total variation bounded by its normalized first seminorm. It crosses
each profile equality location at most once. Changing that one sampled
value according to the equality star contributes at most two
supremum-sized variation increments. The one-sided hard-top profile
contributes its full jump once; that full jump is not converted into an
equality half-weight. This proves (6).

For fixed \(q\), the coordinate remains monotone, but \(h\) and the height
cutoff move. For each active \(j\),

\[
 \mathbf1_{h\le H_j}
\]

drops exactly once, across the sampled edge from \(h=H_j\) to
\(h=H_j+1\), where

\[
 H_j=\lfloor D_jX^{-1/4}\rfloor.
\]

The floor changes only the integer location of this full cutoff jump; it
does not create a fractional family of jumps. On the retained side,
\(\Phi(h/(H_j+1))\) has variation bounded by
\(\|\Phi'\|_\infty\) times the change of its argument, and its supremum is
bounded by \(\|\Phi\|_\infty\). The smooth profile variation, equality-star
correction, and hard-top jump are as above. Since only boundedly many
dyadic profiles are active on the window, summing these contributions
proves (7). Restricting to \(h>H\) adds only the owner-boundary jump.

Finally, \(n^{-3/4}\) is monotone on a product window, has supremum
\(\asymp Y^{-3/4}\), and total sampled variation
\(O(Y^{-3/4}R/Y)\). An inherited radial equality star changes at most one
sample and contributes \(O(Y^{-3/4})\). The product variation inequality
then proves (8)--(9). Artificial moving-window endpoints introduce no new
stars.

### Fixed-\(h\) phase

For fixed \(h\), the relevant \(q\)-interval has length

\[
 L_h\le {R\over h}+O(1),
\]

and

\[
 f_h(q)=\sqrt{Xhq},\qquad
 |f_h''(q)|\asymp {h^2\over R}
\quad(q\asymp Y/h).                                          \tag{13}
\]

The odd character may be retained exactly either by the two residue
classes modulo \(4\), or by

\[
 \chi_4(q)={e(q/4)-e(-q/4)\over 2i}.                          \tag{14}
\]

In (14) the two phases are \(f_h(q)\pm q/4\), whose second derivatives are
still \(f_h''(q)\). The two resulting bounds are combined by the triangle
inequality; no cancellation is claimed merely from the character
representation.

If \(h\le\sqrt R\), apply (10) with
\(\lambda_h\asymp h^2/R\). Uniformly on all partial subintervals,

\[
\begin{aligned}
 L_h\lambda_h^{1/2}+\lambda_h^{-1/2}
 &\ll
 \left({R\over h}+1\right){h\over\sqrt R}
 +{\sqrt R\over h} \\
 &\ll \sqrt R.                                                \tag{15}
\end{aligned}
\]

If \(h>\sqrt R\), then \(L_h\le\sqrt R+O(1)\), so trivial summation gives
the same bound. Abel summation with (8) yields, for every fixed \(h\),

\[
 \left|\sum_{\substack{q:\ hq\in J\\q\ {\rm odd}}}^{*}
 \chi_4(q)\Omega_X^*(hq,h)(hq)^{-3/4}e(f_h(q))\right|
 \ll_\varepsilon
 X^\varepsilon Y^{-3/4}\sqrt R
 \asymp {X^\varepsilon\over\sqrt Y}.                         \tag{16}
\]

### Fixed-\(q\) phase

For fixed odd \(q\), the \(h\)-interval has length

\[
 L_q\le {R\over q}+O(1),
\]

and

\[
 g_q(h)=\sqrt{Xqh},\qquad
 |g_q''(h)|\asymp {q^2\over R}
\quad(h\asymp Y/q).                                          \tag{17}
\]

For \(q\le\sqrt R\), (10) gives

\[
 L_q(q/\sqrt R)+\sqrt R/q\ll\sqrt R.
\]

For \(q>\sqrt R\), trivial summation uses
\(L_q\le\sqrt R+O(1)\). With (9), the restriction \(h>H\), and the constant
factor \(\chi_4(q)\), this gives

\[
 \left|\sum_{\substack{h:\ hq\in J\\h>H}}^{*}
 \Omega_X^*(hq,h)(hq)^{-3/4}e(g_q(h))\right|
 \ll_\varepsilon {X^\varepsilon\over\sqrt Y}.                \tag{18}
\]

### Perfect-fourth-power resonance

Let \(X=K^4\), so the central top scale is \(Y\asymp K^2\) and
\(R\asymp K\). At the exact point \(q_0=K^2/h\), when integral,

\[
 f_h'(q_0)={Kh\over2},\qquad
 f_h''(q_0)=-{h^2\over4K}.                                   \tag{19}
\]

On a residue class \(q=4m+a\), the linear derivative is
\(4f_h'(q_0)=2Kh\in\mathbb Z\). Thus a first-derivative distance from the
integer lattice can vanish exactly. Likewise, at
\(h_0=K^2/q\),

\[
 g_q'(h_0)={Kq\over2},\qquad
 g_q''(h_0)=-{q^2\over4K}.                                   \tag{20}
\]

For even \(K\), \(g_q'(h_0)\) is integral for every odd \(q\); for odd
\(K\), it is half-integral. Hence no uniform first-derivative gap is
available. The proof uses only the nonzero curvatures in (19)--(20), and
when they exceed the small-curvature range it uses the trivial crossover.
Integer or half-integer linear resonance therefore does not invalidate
(15)--(18).

### \(H,Q\) and moving-window ledger

Apply (16) to each integer \(h\le H\) in \(\mathcal M_H\), and (18) to each
odd \(q\le Q\) in \(\mathcal M_Q\). The owner rule (11) gives

\[
 \left|\sum_{n\in J}^{*}
 A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon
 X^\varepsilon{H+Q\over\sqrt Y},
\]

which is (1).

For the exact moving-window count, write
\(I_Y=[a,b]\cap\mathbb Z\), \(L=b-a+1\), and let \(z_n\) denote the exact
star-weighted summand, extended by zero. For
\(\ell=a-R,\ldots,b-1\), define

\[
 W_\ell=\sum_{k=1}^{R}z_{\ell+k}
 =\sum_{n\in I_Y\cap[\ell+1,\ell+R]}z_n.
\]

Every \(z_n\) occurs exactly \(R\) times, including a starred hard endpoint,
so

\[
 R S_{Y;H,Q}=\sum_{\ell=a-R}^{b-1}W_\ell.                    \tag{21}
\]

There are exactly \(L+R-1\) windows. The first and last windows have one
sample, and all rising and falling edge windows have length \(<R\); these
are covered by the uniform form of (1). Therefore

\[
\begin{aligned}
 |S_{Y;H,Q}|
 &\le {L+R-1\over R}
 X^\varepsilon{H+Q\over\sqrt Y} \\
 &\ll_\varepsilon X^\varepsilon(H+Q),                        \tag{22}
\end{aligned}
\]

because \(L\ll Y\) and \(R\asymp\sqrt Y\).

At the level of powers, a single fixed leg contributes

\[
 Y^{-3/4}\sqrt R=Y^{-1/2}=X^{-1/4},
\]

and the moving-window factor contributes
\[
 {L+R-1\over R}\asymp {Y\over R}\asymp\sqrt Y=X^{1/4}.
\]

Thus \(H=Y^\alpha\), \(Q=Y^\beta\) give a window bound
\[
 X^\varepsilon\bigl(Y^{\alpha-1/2}+Y^{\beta-1/2}\bigr)
\]
and a block bound
\[
 X^\varepsilon(Y^\alpha+Y^\beta).                            \tag{23}
\]

Target safety therefore requires \(\alpha=\beta=0\) at the level of powers;
polylogarithmic \(H,Q\) are allowed.

## 4. First doubtful or unproved step

Within the frozen low-margin problem, the only quantitative interpretation
needed is that “fixed dyadic support and bounded smooth seminorms” means
uniform support-scale \(C^1\) control, so that a monotone traversal of one
profile has \(O(1)\) total variation, and that bounded overlap applies to
the union of active indices over the relative \(O(1/R)\) window in (12).
This is the standard content of the packet's accepted profile hypotheses.
If those words provide only pointwise derivative bounds with no
support-scale normalization, then (6)--(7) are the first unproved step and
the packet is insufficient to certify (1).

Under the stated normalized interpretation, the low-margin proof is
complete. The first remaining analytic problem is the balanced bilinear
core (4). Neither one-dimensional fixed-leg summation nor the estimates
above control it when both cutoffs are only polylogarithmic.

The exact numeric convention for an equality star is also not restated in
the packet. The argument needs only that the tagged equality value is
uniformly bounded and occurs at one sample; the report preserves that value
rather than asserting a new half-weight rule.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| fixed_leg_phase | **Pass.** Equations (13) and (17) use the exact phases \(\sqrt{Xhq}\) with curvatures \(h^2/R\) and \(q^2/R\). The period-four character is retained by (14) without claiming free cancellation. |
| curvature_trivial_crossover | **Pass.** Second derivative for \(\ell\le\sqrt R\) and trivial length for \(\ell>\sqrt R\) both give \(O(\sqrt R)\); the junction is \(X^{1/8}\). |
| sampled_profile_BV | **Pass under the packet's normalized profile meaning.** Monotone angular motion, dyadic locality, bounded overlap, Vaaler \(C^1\), equality corrections, and the hard jump give (6)--(9). |
| height_floor_and_stars | **Pass.** A fixed-\(h\) cutoff is constant; a fixed-\(q\) cutoff drops once after \(h=H_j\). Floors locate that full jump. Equality-star values and the hard-top full jump remain distinct. |
| moving_window_edges | **Pass.** Identity (21) has exactly \(L+R-1\) inherited-weight windows, and all short edge windows are included. No artificial endpoint star is introduced. |
| perfect_fourth_power | **Pass.** Equations (19)--(20) exhibit exact integer or half-integer derivative resonance. The proof relies on curvature, not a false derivative gap. |
| H_Q_ledger | **Pass.** Per leg is \(X^\varepsilon/\sqrt Y\), per window is \(X^\varepsilon(H+Q)/\sqrt Y\), and the exact moving-window loss yields \(X^\varepsilon(H+Q)\). |
| double_counting | **Pass.** The disjoint owner rule (11) counts the overlap exactly once. |
| balanced_core_scope | **Pass.** The remainder is exactly \(h>H,\ q>Q,\ hq\asymp Y\); no estimate for it is claimed. |
| downstream_scope | **Pass.** No full shifted-correlation, GAR, alpha-transfer, M9-M1, M9, or final-target conclusion is inferred. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The Round-55 packet's definitions of \(I_Y,R,A_X,\Omega_X^*\),
   \(A_{X;H,Q}\), and \(S_{Y;H,Q}\).
2. The packet's fixed-dyadic support, bounded normalized smoothness,
   bounded-overlap, one-sided hard-top, and Vaaler \(C^1\) hypotheses.
3. The finite second-derivative estimate (10), Abel summation, and the
   elementary moving-window identity (21).

Isolation ledger:

- Read
  rounds/codex-managed/m9-m1-top-block-low-leg-curvature/briefs/blind_fixed_leg_rederivation.md.
- Read
  rounds/codex-managed/m9-m1-top-block-low-leg-curvature/derivation_packet.md.
- Opened no proof graph, proof draft, prior synthesis, validation matrix, or
  other Round-55 report.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Promote the low-margin lemma after a seam review of the profile
normalization and inherited-star convention; retain the balanced core as
open.** The fixed-leg curvature/trivial crossover is target-sized for every
individual low leg, and the exact \(H,Q\) ledger permits polylogarithmic
margins. Do not promote any claim that this controls the balanced bilinear
core or a downstream theorem.
