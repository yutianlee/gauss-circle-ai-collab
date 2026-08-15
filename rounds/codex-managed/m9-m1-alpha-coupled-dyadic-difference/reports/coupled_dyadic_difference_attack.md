# Coupled adjacent-dyadic difference: exact identities and scale-cancellation no-go

- Campaign: `m9-m1-alpha-coupled-dyadic-difference`
- Round: 53 (`alpha_complete_coupled_dyadic_difference`)
- Task: `coupled_dyadic_difference_attack`
- Role: discovery
- Access mode: selected context
- Graph SHA-256: `ffe8d5a79d866395f674ea77294da69c3d8f24ef09072bf36aa7fb3c2287c3a8`
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result: exact coupled-difference lemma and sharp no-go

There are two distinct exact adjacent-scale differences.  On the finite
positive-line antecedent it is

\[
 \Delta_j^{\rm M}(u,v)
 :=\mathcal A_{j+1}(u,v)-\mathcal A_j(u,v),                       \tag{1.1}
\]

and after the licensed physical return it is

\[
 \Delta_j^{\rm ph}(h,q)
 :=\mathscr B_{j+1}(h,q)-\mathscr B_j(h,q).                       \tag{1.2}
\]

Both have exact three-factor/two-factor product-difference formulas on a
common ambient support, given below.  Neither formula is small.  In the
finite formula the height survivor

\[
 (H_{j+1}+1)^v-(H_j+1)^v,
 \qquad H_{j+1}=\lfloor H_j/2\rfloor,                              \tag{1.3}
\]

has full Mellin size.  In the physical formula the scale telescope has a
stronger obstruction: after the common arithmetic factor and phase have
been removed, every scale coefficient is nonnegative.  Hence for every
fixed lattice atom the signed partial sums in the scale label have no
cancellation at all.

More precisely, if

\[
 a_H(h)={\bf1}_{1\le h\le H}\Phi\!\left(\frac h{H+1}\right),
\]

then the exact Abel form of the unstarred active scale sum is

\[
 \sum_{j=0}^{J}w_j(d)a_{H_j}(h)
 =E_0(d)a_{H_0}(h)-E_{J+1}(d)a_{H_J}(h)
  +\sum_{j=1}^{J}E_j(d)
       \{a_{H_j}(h)-a_{H_{j-1}}(h)\}.                             \tag{1.4}
\]

Here (E_0(d)={\bf1}_{d\le y}) and
(E_j(d)=\eta(d/D_j)) for (j\ge1).  Every interior brace in (1.4) is
nonpositive.  Its coefficient mass is exactly

\[
 \sum_h\{a_{H_{j-1}}(h)-a_{H_j}(h)\}
   =\frac{H_{j-1}-H_j}{2}\asymp H_{j-1}.                          \tag{1.5}
\]

Thus (W=\eta-\eta(2\,\cdot)) merely transfers the original positive
scale mass into coherent height differences plus the two boundary terms;
it does not give a signed scale saving.

This failure is sharp at the accepted normalized capacity.  On one
ordinary interior scale there is a star-free plateau family of actual
((h,q)) lattice points whose all-absolute returned mass is

\[
 \gg X^{1/8}.                                                       \tag{1.6}
\]

The accepted upper-capacity ledger is (X^{1/8+o(1)}).  Therefore scale
profile algebra alone cannot supply any positive power saving.  This is
not a signed lower bound for the divisor-grouped/global alpha operator:
cancellation across different ((h,q)), together with the complete alpha
projection and connectors, remains possible and is exactly the missing
theorem.

## 2. Exact statement and hypotheses

Let

\[
 y=\lfloor\sqrt X\rfloor,\quad D_j=2^{-j}y,\quad
 H_j=\lfloor D_jX^{-1/4}\rfloor,
\]

and take the packet's fixed profiles

\[
 \eta(t)=1-s(3(t-1)),\qquad W(t)=\eta(t)-\eta(2t).
\]

The facts used about them are

\[
 0\leq W,\eta\leq1,qquad
 W(t)=1\quad(2/3\leq t\leq1),                                    \tag{2.1}
\]

and the exact active partition, with one top owner and one inactive bottom
owner.  The Vaaler profile is

\[
 \Phi(t)=\pi t(1-t)\cot(\pi t)+t,
\]

with the Round-52 conclusions that (a_H\) is pointwise increasing in
(H) and

\[
 \sum_{h\ge1}a_H(h)=H/2,qquad
 \|a_K-a_H\|_1=|K-H|/2.                                          \tag{2.2}
\]

All physical profiles are extended by zero to the common ambient lattice

\[
 \mathfrak L_X=\{(h,q):h,q\in\mathbb N, q\ {\rm odd}\}.
\]

The product cutoff/star is then a common multiplier on
(hq\le N_X=16\sqrt X); it is not built separately into the two scale
supports.  Put

\[
 d(h,q)=2\sqrt{Xh/q},\quad
 P_j(h,q)=V_j^*\!\left(\frac{d(h,q)}{D_j}\right),\quad
 F_j(h)=a_{H_j}(h).                                                \tag{2.3}
\]

Thus the packet's bare physical profile is
(\mathscr B_j=P_jF_j).  The notation (F_j) makes explicit the cutoff
which is implicit in the packet's
(\phi(h/(H_j+1))).  Let

\[
 R_X(h,q)=\chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})                        \tag{2.4}
\]

denote the common post-return arithmetic, radial, and phase factor; the
fixed stationary constant, real-part operation, product star, and single
external (X^{1/4}) are retained outside it.

The conclusion concerns only (i) the finite antecedent and (ii) the
already licensed physical return separately.  It assumes no interchange
with an outside-height limit and no deletion of finite alpha connectors.

## 3. Proof and complete owner table

### 3.1 Finite positive-line difference

On one common finite ((u,v))-rectangle write

\[
 C_X(u,v)=\widehat\phi(v)(2\sqrt X)^{-u},\quad
 P_j^{\rm M}(u)=\widehat W_j(u),\quad
 S_j(u)=D_j^u,\quad T_j(v)=(H_j+1)^v.
\]

Extension to this common rectangle before subtraction gives the exact
identity

\[
 \boxed{\Delta_j^{\rm M}
 =C_X\{(P_{j+1}^{\rm M}-P_j^{\rm M})S_{j+1}T_{j+1}
       +P_j^{\rm M}(S_{j+1}-S_j)T_{j+1}
       +P_j^{\rm M}S_j(T_{j+1}-T_j)\}.}                           \tag{3.1}
\]

This ordered product difference owns each change once.  Since

\[
 S_{j+1}-S_j=D_j^u(2^{-u}-1),\qquad
 T_{j+1}-T_j=(\lfloor H_j/2\rfloor+1)^v-(H_j+1)^v,                \tag{3.2}
\]

even two interior scales with the same Mellin shape retain scale-power and
height-power survivors.  If (\rho_H=(\lfloor H/2\rfloor+1)/(H+1)), then

\[
 T_{j+1}-T_j=(H+1)^v(\rho_H^v-1),\qquad \rho_H\longrightarrow1/2. \tag{3.3}
\]

For every fixed (v) with (2^{-v}\ne1), (3.3) has order
((H+1)^{\Re v}); at (v=1) it equals
(-H+\lfloor H/2\rfloor).  Thus the physical unit-height variation cannot
be inserted uniformly on the finite (v)-box.  Possible zeros at isolated
Mellin values do not bound the finite integral.

### 3.2 Physical difference

On the common lattice (\mathfrak L_X), the bare returned difference is

\[
 \boxed{\Delta_j^{\rm ph}
 =(P_{j+1}-P_j)F_{j+1}+P_j(F_{j+1}-F_j).}                          \tag{3.4}
\]

Multiplying (3.4) by the one common product-star multiplier, by (R_X),
and finally by the one external (X^{1/4}) gives the complete physical
difference.  Formula (3.4) includes points that belong to just one of the
two original supports because both profiles were first extended by zero.
No support face is lost.

The full ownership ledger is:

| datum/change | exact owner | location in the formulas | outcome |
|---|---|---|---|
| Mellin shape, including the exceptional top shape | (P_{j+1}^{\rm M}-P_j^{\rm M}) | first term of (3.1) | zero for identical interior shapes; retained at the top |
| dyadic scale power (D^u) | (S_{j+1}-S_j=D_j^u(2^{-u}-1)) | second term of (3.1) | finite Mellin survivor |
| height power ((H+1)^v) | (T_{j+1}-T_j) | third term of (3.1) | full-bulk finite Mellin survivor |
| fixed (\widehat\phi(v)(2\sqrt X)^{-u}) | (C_X) | outside all three terms | common; counted once |
| radial rescaling (d/D_j), denominator profile, and zero extension across its support | (P_{j+1}-P_j) | first term of (3.4) | plus/minus spatial lobes, not cancellation |
| Vaaler retuning and cutoff (h\le H_j) | (F_{j+1}-F_j) | second term of (3.4) | coherent negative height difference |
| equality (h=H_j) | (F_j) with the floor-compatible full endpoint value | (2.3)--(3.4) | no artificial half-star |
| interior profile equality star | (V_j^*-V_j) at that scale only | contained in (P_j) | finite boundary correction, never reassigned to the height cutoff |
| hard top (d=y) and its one-sided/top star | (j=0), hence (P_0^{\rm M}) and (P_0) | top term in (3.1)/(3.4) | retained as a top boundary owner |
| inactive bottom profile | (E_{J+1}) | last term of (1.4) | explicit bottom boundary; its separate target-safe estimate is not a telescope |
| product equality (hq=N_X) | one common product-star multiplier | outside (3.4) | not differenced and not merged with a profile star |
| arithmetic (\chi_4(q)), radial weight ((hq)^{-3/4}), and phase | (R_X(h,q)) | outside (3.4) | independent of (j) for a fixed atom |
| external physical normalization | one (X^{1/4}) | outside the full lattice sum | never placed in an individual owner |
| finite masks, faces, axes, connector strata, and corner | the common finite alpha antecedent | outside (3.1) | no commutation with the physical/outside-height limit is asserted |

This table also explains why a profile star, the Vaaler equality, and the
product star cannot be represented by one generic boundary symbol.

### 3.3 What exact (W)-telescoping actually gives

Define

\[
 E_0(d)={\bf1}_{d\le y},\qquad E_j(d)=\eta(d/D_j)\quad(j\ge1).
\]

The top definition and the support of (\eta) give, for every (d>0),

\[
 w_j(d)=E_j(d)-E_{j+1}(d)\quad(0\le j\le J).                      \tag{3.5}
\]

Summation by parts in (3.5) proves (1.4).  Since (H_j\le H_{j-1}) and
(a_H(h)) is increasing in (H), every interior difference in (1.4) is
nonpositive.  Equation (2.2) proves (1.5).  Equality/profile-star
corrections add separately as

\[
 \sum_{j=0}^{J}\{V_j^*(d/D_j)-w_j(d)\}F_j(h);                    \tag{3.6}
\]

they do not alter the unstarred identity and are each owned at one finite
boundary.

There is an even simpler local witness.  If

\[
 2D_j/3<d<D_j,                                                     \tag{3.7}
\]

then (w_j(d)=1), and nonnegativity plus the exact partition force every
other active scale profile and the bottom profile to vanish.  Hence the
left side of (1.4) is exactly (a_{H_j}(h)).  The telescope has selected
one full height profile, not reduced it.

For a fixed ((h,q)), the factor (R_X(h,q)) is independent of (j),
and all (V_j^*F_j) are nonnegative (stars are equality weights, not sign
changes).  Consequently every scale partial sum satisfies the exact
identity

\[
 \left|R_X(h,q)\sum_{j\le K}V_j^*(d/D_j)F_j(h)\right|
 =|R_X(h,q)|\sum_{j\le K}V_j^*(d/D_j)F_j(h).                      \tag{3.8}
\]

Thus no actual signed partial-sum saving exists in the (j)-variable
alone.  Summing the adjacent differences
(\Delta_j^{\rm ph}) merely gives
(\mathscr B_{K+1}-\mathscr B_0); it is not an identity for
(\sum_j\mathscr B_j).  Formula (1.4), including both boundary terms, is
the lawful identity for that sum.

### 3.4 Sharp star-free capacity witness

Take the ordinary interior scale (j=1), so (D=y/2), and put
(H=\lfloor DX^{-1/4}\rfloor).  For sufficiently large (X), let

\[
 \mathcal R_X=\left\{(h,q):
  \frac H4\le h\le\frac H3, q\ {\rm odd},
  \frac{5Xh}{D^2}\le q\le\frac{8Xh}{D^2}\right\}.               \tag{3.9}
\]

For every point of this set,

\[
 \frac{d(h,q)}D\in[1/\sqrt2,2/\sqrt5]\subset(2/3,1),             \tag{3.10}
\]

so the selected interior profile is exactly one and all other spatial
profiles are zero.  Also

\[
 h/(H+1)\in[1/5,1/3]
\]

for large (H), and hence
(\Phi(h/(H+1))\ge c_\Phi>0).  There are

\[
 \#\mathcal R_X
 \gg\sum_{H/4\le h\le H/3}\frac{Xh}{D^2}
 \gg \frac{XH^2}{D^2}\gg X^{1/2}                                \tag{3.11}
\]

such odd-(q) points, using
(H\ge\tfrac12DX^{-1/4}).  If (m=hq), then throughout this set

\[
 c\sqrt X\le m\le\frac89\sqrt X<16\sqrt X.                      \tag{3.12}
\]

Thus the product cutoff is strict, the profile lies strictly inside its
plateau, (h<H), and no top, profile, height, or product star occurs.
Taking absolute values in the normalized returned lattice gives

\[
 \sum_{(h,q)\in\mathcal R_X}
 \Phi\!\left(\frac h{H+1}\right)(hq)^{-3/4}
 \gg X^{1/2}X^{-3/8}=X^{1/8}.                                    \tag{3.13}
\]

After the single external normalization this is (X^{3/8}).  The target
therefore requires an (X^{-1/8+o(1)}) gain from cancellation across the
actual arithmetic/phase lattice (or an equivalent aggregate identity),
not from adjacent-scale telescoping.

## 4. First doubtful or unproved step

There is no doubtful step in the two product-difference identities, the
owner ledger, the Abel identity, the sign-coherence statement, or the
capacity construction.  The first unproved step is a signed theorem across
different lattice atoms after the (j)-sum, divisor collisions, the
(\chi_4(q)) factor, the radial phase, the complete finite alpha
projection/connectors, and the prescribed joint outside-height limit have
all been assembled on one antecedent.  Equation (3.13) is deliberately not
a lower bound for that signed aggregate.

In particular, no conclusion here proves that the alpha branch is large;
it proves that scale differencing is incapable of being the missing
source of cancellation.  A new estimate must act in the ((h,q)) or
divisor-grouped variable while retaining the full projected-comb
architecture.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| `common_support` | Pass: both scales are extended by zero before (3.1) and (3.4); one-sided points remain in the differences. |
| `finite_vs_physical` | Pass: (3.1) and (3.4) are stated separately; no termwise outside-height interchange is used. |
| `profile_telescoping` | Pass as an identity, fail as a saving: (1.4) retains coherent height differences and both boundaries. |
| `height_coupling` | Pass: (H_{j+1}=\lfloor H_j/2\rfloor); (1.3), (1.5), and (3.3) quantify the survivor. |
| `top_bottom_ownership` | Pass: the top is in (E_0/P_0), and the bottom is the explicit (-E_{J+1}F_J) boundary. |
| `all_star_ownership` | Pass: profile/top stars are in (3.6), the Vaaler equality is full weight, and the product star is one common multiplier. |
| `signed_partial_sums` | Mechanism falsified: (3.8) gives exact equality with the absolute scale sum at each fixed atom. |
| `boundary_terms` | Pass: neither (E_0F_0) nor (-E_{J+1}F_J) is discarded, and adjacent-difference telescoping is distinguished from the original scale sum. |
| `alpha_capacity_scope` | Pass: (3.13) is a sharp normalized absolute antecedent capacity, not a signed/global lower bound. |
| `downstream_scope` | Pass: no alpha transition, outside-height, GAR, M9-M1, M9, or Gauss-circle conclusion is promoted. |

All work was analytical/algebraic.  No numerical experiment and no
external theorem were used.

## 6. Dependencies and exact artifacts used

Only the selected context in the task brief was used:

- `protocol.md`;
- `state/proof_obligations.yml` (the active alpha, M9-M1, and M9 entries);
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/synthesis.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`;
- `rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/synthesis.md`;
- `rounds/codex-managed/m9-m1-alpha-highpass-log-commutator/synthesis.md`.

No other Round-53 report, proof draft, validation matrix, legacy response,
or outside source was read.

## 7. Recommended state effect

Promote, after independent rederivation and hostile review, the exact
finite product difference (3.1), the physical common-support difference
(3.4), and the boundary-complete Abel identity (1.4).  Record as a proved
scoped no-go that the actual nonnegative scale family has no signed
(j)-partial-sum cancellation, with the sharp star-free normalized
(X^{1/8}) capacity witness (3.9)--(3.13).

Revise the open alpha target so that adjacent-dyadic differencing and
(W)-telescoping are not requested as a stand-alone saving mechanism.  The
next lawful target is a signed cancellation theorem across the complete
post-scale ((h,q)) lattice/divisor fibers on the finite connector-completed
alpha antecedent, followed separately by the joint outside-height Cauchy
limit.  Retain every downstream obligation as open.
