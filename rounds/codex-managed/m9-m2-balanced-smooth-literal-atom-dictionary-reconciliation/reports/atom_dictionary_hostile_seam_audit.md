# Round 113 hostile seam audit: literal balanced smooth atom dictionary

Campaign: `m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation`
Task: `atom_dictionary_hostile_seam_audit`
Role: `seam_reviewer`
Starting graph SHA-256: `9d560539df2db7d69e72dd6e7e6af7247f00237ee795ac13b053b3f34eae8efa`

## 1. Result

**Repair lemma; the candidate is not certifiable verbatim, but its core
algebra survives a smallest explicit repair.** Equations (113.C1)--(113.C15),
the ratio identity (113.C19), the integer gcd telescoping mechanism, and the
quarter-packet sign and factor in (113.C25)--(113.C28) are correct. In
particular:

\[
 B_{2,j,r}=8\operatorname{Re}\mathcal B_{j,r}^{+},\qquad
 \mathcal B_{j,r}^{+}
 =-\frac{e(1/8)}{2\pi}X^{1/4}(LK)^{-3/4}\mathcal T_{j,r}+E_{j,r}
\]

has the correct factor $8$, minus sign, $e(1/8)$, and $1/(2\pi)$, and
the gcd Poisson formula has $1/(2i)$ times the $1/4$-packet minus the
$3/4$-packet.

The first non-certified line is (113.C24): $A_{j,r}$ has only been defined
on positive integers (and $v_r$ was introduced with an integer clipping
indicator), so the assertion that $F_{\sigma,u,v}$ is a *literal* real
$C_c^\infty$ function with uniform seminorms is not yet a typed definition
or a proof. The later one-count claim also uses undefined symbols
$\mathcal T^{\mathrm{low}}$ and the unnamed high-gcd subtotal, and it never writes
the physical correction equation containing high gcd, square, near-square,
and $8\operatorname{Re}E_{j,r}$. Finally, the prose around
(113.C16)--(113.C18) leaves equality/collar ownership optional; optional
ownership is incompatible with an exact one-count dictionary.

These are repairable definition seams, not counterexamples to the displayed
constant algebra. The smallest lawful repair is given below: define one
explicit normalized continuous symbol, freeze the residual-test priority,
define every high/low/correction subtotal, and write the full physical
one-count equation. With those insertions, the finite dictionary is
certified coefficientwise for every sufficiently large real $X$. The
signed packet estimate (113.C29) remains the first analytic gap.

## 2. Exact statement and hypotheses

Let $X\ge X_0$ be real, $R=\sqrt X$, $y=\lfloor R\rfloor\ge1$, and use
exactly the functions $\eta,W$, denominator scales $D_j$, frequency
height $H=\lfloor DX^{-1/4}\rfloor$, and frequency scales $L_r$ from
(113.C1)--(113.C6). Fix one block $B=(X,j,r,+)$ satisfying

\[
 j\ge1,\quad D=D_j\ge X^{1/4},\qquad
 1\le r<J_H,\quad L=2^{-r}H,\qquad
 K=\frac{XL}{D^2},\quad 1\le \frac{K}{L}\le16.                     \tag{2.1}
\]

Thus both denominator and frequency weights are full smooth profiles. The
clipped $r=0$ block and the unit bottom frequency piece are prior-owner
labels, not omitted terms. Freeze the finite preliminary owner priority as
follows: terminal first, then the displayed second-derivative envelope,
then the displayed TTY envelope, assigning equality to the earlier owner;
retain the block only if all three strict inequalities
(113.C16)--(113.C18) hold. This is a conservative exact definition of the
residual set. A different fixed collar is permissible only after replacing
this definition everywhere, not on a block-by-block basis.

For $x,z>0$, define the actual normalized continuous symbol

\[
 a_B(x,z)=W(x)\Phi\!\left(\frac{Lx}{H+1}\right)(xz)^{-3/4}
 W\!\left(\sqrt{\frac{x}{4z}}\right),                              \tag{2.2}
\]

and set it to zero off the positive quadrant. Since $r\ge1$, on the
support of $W(x)$ one has $0<Lx/(H+1)<3/4$; hence (2.2) uses only the
audited smooth interior of $\Phi$. It is a real
$C_c^\infty(\mathbb R^2)$ function and

\[
 A_B(h,k)=a_B(h/L,k/K)                                             \tag{2.3}
\]

on positive integers. This is the required continuous extension of
(113.C13), and it fixes the support-crossing convention.

Retain $G_0=\sqrt L/2$, $S=\max(0,\lceil\log_2G_0\rceil)$,
$G_s=2^{-s}G_0$, and $G_S\in[1/2,1]$. Let the low labels be

\[
 \Sigma_B=\{s:0\le s<S\}\cup\{\mathrm{bot}\},
\]

with $(G_\sigma,\vartheta_\sigma)=(G_s,W)$ or
$(G_\sigma,\vartheta_\sigma)=(1,c_LW)$, where $c_L=\eta(1/G_S)$. Define

\[
 F_{B,\sigma,u,v}(t)=
 \vartheta_\sigma(t)
 a_B\!\left(\frac{G_\sigma tu}{L},\frac{G_\sigma tv}{K}\right).    \tag{2.4}
\]

This is the corrected literal version of (113.C24).

For $g=(h,k)$, define coefficientwise

\[
\begin{aligned}
 T_{B,\sigma}
 &=\sum_{h,k\ge1}\chi_4(h)\psi_\sigma(g)A_B(h,k)
 e(R\sqrt{hk}),\\
 T_{B,\mathrm{low}}
 &=\sum_{\sigma\in\Sigma_B}T_{B,\sigma},\\
 T_{B,\mathrm{hi}}
 &=\sum_{h,k\ge1}\chi_4(h)\psi_{\mathrm{hi}}(g)A_B(h,k)
 e(R\sqrt{hk}).                                                    \tag{2.5}
\end{aligned}
\]

Inside $T_{B,\mathrm{low}}$, give priority to the disjoint sets

\[
 hk\in\square,\qquad
 hk\notin\square,\quad
 \operatorname{dist}(\sqrt{hk},\mathbb Z)\le R^{-1},               \tag{2.6}
\]

and denote their exact signed weighted subtotals by $S_B^{\mathrm{sq}}$ and
$S_B^{\mathrm{near}}$. Put

\[
 P_B=\frac{1}{2i}\sum_{\sigma\in\Sigma_B}G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(R),\qquad
 T_B^{\mathrm{res}}=P_B-S_B^{\mathrm{sq}}-S_B^{\mathrm{near}}.     \tag{2.7}
\]

Finally set

\[
 c_B=\frac{e(1/8)}{2\pi}X^{1/4}(LK)^{-3/4},\qquad
 E_B=\mathcal B_B^+ +c_B\mathcal T_B.                              \tag{2.8}
\]

Then $E_B$ is an exact transform-error atom and the accepted stationary
formula gives $|E_B|\ll_W1$. The exact coefficientwise and physical
one-count equations are

\[
\boxed{
 \begin{aligned}
 \mathcal T_B
 &=T_{B,\mathrm{hi}}+S_B^{\mathrm{sq}}+S_B^{\mathrm{near}}
   +T_B^{\mathrm{res}},\\
 B_{2,B}
 &=8\operatorname{Re}\!\left[
 -c_B\left(T_{B,\mathrm{hi}}+S_B^{\mathrm{sq}}+S_B^{\mathrm{near}}
 +T_B^{\mathrm{res}}\right)+E_B\right].
 \end{aligned}}                                                   \tag{2.9}
\]

Thus, after the four prior physical owners are subtracted, the literal
residual is $8\operatorname{Re}[-c_BT_B^{\mathrm{res}}]$. The only open
analytic assertion attached to this dictionary is

\[
 \left|\sum_{\sigma\in\Sigma_B}G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.                            \tag{2.10}
\]

The modulus is per fixed physical $B$; no distinct $j$- or $r$-blocks
are combined.

## 3. Proof or derivation

The denominator telescoping is exact because

\[
 W(d/D_j)=\eta(2^jd/y)-\eta(2^{j+1}d/y),
\]

so the sum through $j=J_y-1$, followed by the bottom remainder, is
$\eta(d/y)=1$ for $1\le d\le y$. For $j\ge1$, the support lies below
$3y/4$, so only $j=0$ meets the hard upper cutoff. The identical
calculation with $H$ proves the clipped frequency partition. If $H=1$,
only the bottom remains. If $H=2$, $J_H=1$: $h=1$ belongs to the
bottom and $h=2$ to the clipped $r=0$ profile because
$W(1/2)=0$, $W(1)=1$, $\eta(1)=1$, and $\eta(2)=0$. Hence neither
case contains a full $r\ge1$ residual block. For every active $D$,

\[
 1\le DX^{-1/4}<\infty,\qquad
 \frac{1}{2}DX^{-1/4}\le H\le DX^{-1/4}.                           \tag{3.1}
\]

The clipped $r=0$ profile is terminal and is owned by T2S. The bottom
frequency profile is supported only at $h=1$; in the balanced smooth
case $j\in\{1,2\}$, hence $D\asymp\sqrt X$, and the accepted full
second-derivative envelope is $O(X^{1/4})$. These labels therefore have
target-safe prior owners. If a full block's stationary $k$-support has no
integer, its main sum and every packet atom are zero, while (2.8) assigns
the entire block to the $O(1)$ transform-error owner.

For $h>0$, direct multiplication gives

\[
 \alpha_{h,H}C_h
 =-\frac{\Phi(h/(H+1))}{2\pi ih}\,2i\chi_4(h)
 =-\frac{\Phi(h/(H+1))\chi_4(h)}{\pi h}.                           \tag{3.2}
\]

This coefficient is real and even after the negative frequency is restored.
Consequently the negative-frequency block is the conjugate of the positive
one. The outer physical factor four therefore gives

\[
 4\left(\mathcal B_B^++\overline{\mathcal B_B^+}\right)
 =8\operatorname{Re}\mathcal B_B^+.                               \tag{3.3}
\]

The accepted smooth $d$-Poisson formula has stationary phase
$\sqrt{Xhk}$, stationary unit $e(1/8)$, and amplitude
$(hX)^{1/4}/(2k^{3/4})$. Combining it with (3.2) gives exactly (2.8)--(2.9).
Because $W$ is flat at every support edge, entry or exit of a stationary
point is already represented by the last $W$-factor in (2.2); there is no
hard crossing term. Zero and nonstationary modes, including an empty
stationary range, are in $E_B$, uniformly $O(1)$.

Writing $q=X/y^2$, one has $1\le q<(1+1/y)^2\le4$ and

\[
 \frac{K}{L}=4^jq.                                                  \tag{3.4}
\]

Thus $j=1$ is balanced for every real $X\ge1$, $j=2$ is balanced
only at equality $q=1$, equivalently $X=y^2$, and that equality is
assigned to the balanced side; every $j\ge3$ is unbalanced. The hard
$j=0$ block never enters. Floors therefore create a genuine isolated
$j=2$ label at square $X$, but no overlap or gap.

For the gcd partition, telescoping first gives

\[
 \sum_{s=0}^{S-1}W(g/G_s)=\eta(g/G_0)-\eta(g/G_S).                 \tag{3.5}
\]

Since $G_S\in[1/2,1]$, for a positive integer $g\ge2$ both
$\eta(g/G_S)$ and $W(g)$ vanish, while for $g=1$,
$\eta(1/G_S)=c_L$ and $W(1)=1$. Hence

\[
 \eta(g/G_S)=c_LW(g)\quad(g\in\mathbb N),
\]

and therefore

\[
 \sum_{\sigma\in\Sigma_B}\psi_\sigma(g)=\eta(g/G_0),\qquad
 \psi_{\mathrm{hi}}(g)=1-\eta(g/G_0).                             \tag{3.6}
\]

This proves the claimed bottom integer atom exactly, including $S=0$,
and proves that the high owner vanishes for $g\le\sqrt L/2$. Since
$K/L\le16$, direct counting on $g\gg\sqrt L$ gives

\[
 \sum_{g\gg\sqrt L}
 \left(\frac{L}{g}+1\right)\left(\frac{K}{g}+1\right)
 \ll L^{3/2},                                                       \tag{3.7}
\]

so the high owner is target-safe. The accepted square and near-square
counts give respectively $O_\varepsilon(L^{1+\varepsilon})$ and

\[
 O_\varepsilon\!\left((L^2/R+L)L^\varepsilon\right)
 =O_\varepsilon(L^{1+\varepsilon}),                               \tag{3.8}
\]

because $L\le R^{1/2}$. They remain target-safe after the low smooth
weight is inserted.

On the support of (2.2),

\[
 \frac{1}{2}\le x\le\frac{3}{2},\qquad
 \frac{1}{18}\le z\le\frac{3}{2},\qquad
 0\le \frac{Lx}{H+1}<\frac{3}{4}.                                 \tag{3.9}
\]

Every logarithmic $x,z$ derivative of $a_B$ is consequently bounded by
a constant depending only on its orders and $W,\Phi$. In (2.4), $t$
is confined to $[1/2,3/2]$; wherever the second factor is nonzero,
$G_\sigma u/L$ and $G_\sigma v/K$ are bounded above and below by fixed
constants. The chain rule therefore gives, for every $N$,

\[
 \max_{0\le m\le N}\|F_{B,\sigma,u,v}^{(m)}\|_\infty\le C_N,       \tag{3.10}
\]

uniformly in real $X,D,L,H$, all floors, $\sigma,u,v$, and also for the
bottom because $0\le c_L\le1$. Equivalently, the unscaled gcd profile
$F(g/G_\sigma)$ has $G_\sigma^m\partial_g^m$-seminorm $O_m(1)$.

Finally, on a contributing ray $h=gu,k=gv$, $u$ and $g$ are odd and
$\chi_4(gu)=\chi_4(u)\chi_4(g)$. With

\[
 \chi_4(g)=\frac{e(g/4)-e(3g/4)}{2i}
\]

and the declared Fourier convention, Poisson in $g$ gives exactly

\[
 T_{B,\mathrm{low}}
 =\frac{1}{2i}\sum_{\sigma\in\Sigma_B}G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(R)=P_B.                             \tag{3.11}
\]

The $u,v$ ranges are finite by (3.9), and each $n$-sum is absolutely
convergent by (3.10), so no rearrangement is conditional. Equations
(2.6)--(2.9) now prove the owner one-count identity. For real profiles,
reindexing the two Fourier sums gives

\[
 Q_{B,\sigma}^{\mathrm{full}}(-R)
 =-\overline{Q_{B,\sigma}^{\mathrm{full}}(R)},                     \tag{3.12}
\]

and the extra minus sign is exactly cancelled by conjugating $1/(2i)$.
This is the required frequency-sign conjugacy.

## 4. First doubtful or unproved step

In the uncorrected candidate, the first doubtful step is the sentence after
(113.C24). Integer values of $A_{j,r}$ do not by themselves specify a
continuous extension, and the discrete indicator in $v_r$ cannot simply
be differentiated. Formula (2.2) is the first exact repair: it removes the
inactive clipping indicator, fixes the full slanted extension, and makes all
support crossings and seminorms literal. The extension is independent of
any arithmetic square/near-square mask.

The next bookkeeping repair is (2.5)--(2.9). Without it, the words
"high-gcd term" and "transform error" are not coefficient labels, and
(113.C28) is only the low-shell identity, not a physical one-count equation.
The frozen priority also removes the equality ambiguity in
(113.C16)--(113.C18).

After these repairs, the first genuinely unproved step is exactly (2.10),
equivalently (113.C29). The dictionary proves no cancellation in that
signed internal shell sum. It supplies no theorem for the unsigned packet,
arbitrary coefficients, shellwise $\ell^1$, or cancellation between
different physical blocks.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `denominator_telescoping_and_hard_profile` | **Pass.** The finite telescoping identity is exact; $j=0$ is the unique upper hard profile, $j\ge1$ are full $W$-rescalings, and the inactive bottom is retained separately. |
| `frequency_telescoping_top_bottom_and_clipping` | **Pass.** The top $r=0$ is the unique clipped band, the bottom is retained, and every $r\ge1$ is a full $W$-profile. At $H=2$, $h=1$ and $h=2$ are counted once by bottom and top respectively. |
| `height_floor_and_empty_block` | **Pass after explicit empty-label convention.** Equation (3.1) is uniform. $H=1,2$ produce no full residual block. Empty stationary support means zero main packet and an $O(1)$ error owner. |
| `exact_Phi_and_positive_frequency_constant` | **Pass.** Formula (3.2) gives the exact $-1/\pi$ positive coefficient; stationary phase supplies $e(1/8)/2$, yielding $-e(1/8)/(2\pi)$. |
| `positive_negative_frequency_recombination` | **Pass.** Real-even coefficients give (3.3), hence the physical factor $8$. Packet conjugacy is (3.12), including its compulsory minus sign. |
| `balanced_ratio_boundary_and_real_X` | **Pass.** Equation (3.4) is exact for real $X$; $j=2$ belongs to the balanced side exactly when $X=y^2$. Floors cause a label jump, not a missing term. |
| `stationary_symbol_support_crossings_and_error` | **Pass after (2.2) and (2.8).** The full slanted $W(\sqrt{x/(4z)})$ factor owns smooth entry/exit, while all zero/nonstationary/stationary remainders are in one exact $E_B=O(1)$. |
| `smooth_gcd_one_count_and_boundary_owner` | **Pass.** Equations (3.5)--(3.6) prove that $c_LW(g)$ is exactly the integer bottom remainder. The explicit $\psi_{\mathrm{hi}}$ is the one boundary owner and is target-safe by (3.7). |
| `square_near_square_and_large_gcd_priority` | **Pass only with (2.5)--(2.9).** High gcd is removed first; square and nonsquare-near sets are then disjoint restrictions of the low weighted part. No square or near-square mask enters $F$, and no coefficient is counted twice. |
| `finite_omega_and_no_cross_block_cancellation` | **Pass.** The internal subdivision is the singleton and $\Sigma_B$ is finite. The modulus in (2.10) is taken before the accepted assembly sums distinct $j,r$ blocks. |
| `profile_seminorms_and_uniformity` | **Fail in the uncorrected text; pass after (2.2)--(2.4).** Equations (3.9)--(3.10) give the required scale-normalized seminorms uniformly in real $X$, floors, shell labels, and smooth support crossings. |
| `false_arithmetic_mask_and_unsigned_models` | **Pass as a guardrail.** The actual $\chi_4$, both quarter shifts, their difference, and even products remain. A phase-conjugating or unsigned arbitrary coefficient model can have $\asymp L^2$ mass, so this dictionary licenses no coefficient-uniform $L^{3/2}$ theorem. |
| `capacity_and_downstream_scope` | **Pass.** Canonicalization does not improve the envelope: the deficit remains $\min(L^{1/2},R^{1/2}/L)$, maximally $X^{1/12}$ at $L=X^{1/6}$. Even (2.10) would close only the balanced smooth child; hard and unbalanced owners remain independent and open. |

No numerical experiment or external source import was used.

## 6. Dependencies and exact artifacts used

The complete selected context used was:

- `protocol.md`;
- `state/proof_obligations.yml` (the Round-113 target nodes and their exact dependencies/statuses);
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/briefs/atom_dictionary_hostile_seam_audit.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/candidates/conductor_literal_atom_dictionary.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/hostile_endpoint_scope_review.md`;
- `rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md`;
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/reports/m2_assembly_hostile_hygiene_audit.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reports/balanced_packet_hostile_source_audit.md`.

Within the authoritative graph, the decisive nodes were
`M9-M2-beta-algebra`, `H4-Phi-regularity`,
`M9-M2-character-factor`, `M9-M2-dyadic-weight-nondegeneracy`,
`M9-M2-smooth-dual-three-quarter-equivalence`,
`M9-M2-smooth-small-gcd-quarter-packet`,
`M9-M2-balanced-quarter-packet-normalization-scope`,
`M9-M2-smooth-balanced-quarter-packet-estimate`, and
`M9-M2-physical-one-count-assembly`. No unselected repository file,
sibling Round-113 report, web source, or computation was used.

## 7. Recommended state effect

**Revise, then promote only the connector.** Replace the untyped claim
(113.C24) by (2.2)--(2.4), freeze equality ownership in the residual labels,
and replace the prose one-count assertion by the exact subtotal and physical
equations (2.5)--(2.9). After conductor validation, these repaired formulas
may support a new proved literal-dictionary connector, or may be added as
positive evidence to `M9-M2-balanced-quarter-packet-normalization-scope`.

Retain `M9-M2-smooth-small-gcd-quarter-packet` as the abstract full-small-gcd
reduction, now with this literal coefficientwise instantiation available.
Retain `M9-M2-smooth-balanced-quarter-packet-estimate` as **open**, with
(2.10) as its exact per-block target and with the modulus outside the full
internal gcd sum. Do not replace it by shellwise absolute values, an
unsigned model, or cancellation across physical blocks.

Make no status change to `M9-M2-physical-one-count-assembly`, the hard or
unbalanced smooth children, M9-M2, M9-M1, endpoint uniformity, M9, or the
Gauss-circle exponent. The Round-113 result is a repaired finite dictionary
only; it has no analytic capacity gain.
