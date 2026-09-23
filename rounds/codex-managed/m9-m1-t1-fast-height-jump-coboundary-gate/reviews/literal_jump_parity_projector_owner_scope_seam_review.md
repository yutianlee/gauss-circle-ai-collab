# Round 191 literal-jump, parity-projector, and owner-scope seam review

- Campaign: m9-m1-t1-fast-height-jump-coboundary-gate
- Reviewed candidate:
  candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md
- Review role: independent hostile literal-source, parity-projector, and
  owner-scope seam
- Starting graph SHA-256:
  306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa
- Status: review evidence only; no candidate or shared-state edit

## 1. Result and verdict

**Verdict: REVISE before promotion.** The central strict-sector theorem
is mathematically sound: the signed least inverse cut has the claimed
row count, its $m$ cancels the exact $m^{-1}c_q(a)$ lift before the
outer divisor sum, and the terminal and isolated Fejer components can be
paid as exact linear subpackets. Equations (191.C14)--(191.C20) have the
correct Abel sign and determinant-transport signs. Equation (191.C24)
is an exact algebraic telescoping identity.

The candidate is not yet mechanically promotion-ready for five reasons:

1. The hypotheses used in (191.C27) and (191.C35) are not all displayed
   in the candidate statement. It must state explicitly
   $u,v\asymp L/\kappa$, total literal $v$-interval length $O(u)$, and
   the inherited nonzero-shell connector $L\ll X^{1/4}$.
2. The parity paragraph must display the retained-mode identity

   \[
   (-1)^{\nu_\omega(h)}
   e(\epsilon_\omega k\varrho/U)
   =(-1)^{\nu_\omega(h)}
   e(\epsilon_\omega a\varrho/q),
   \tag{191.R1}
   \]

   and say explicitly that $(-1)^\varrho$ is a full-anchor identity
   only. It is not an identity inside the retained fast projector.
3. The verbal partition preceding (191.C23) needs an exact gated formula,
   and (191.C25) must first expand the two endpoint factors of
   $\Lambda$, including conjugation and orientation-specific divisor
   arguments. As written, the conceptual list is exhaustive, but the
   displayed algebra does not yet mechanically prove that both endpoint
   jump sources occur exactly once.
4. The terminal and Fejer pieces must be defined as exact complete
   complex linear projections over both orientations before either
   modulus or real part. Their positive estimates are lawful only after
   that definition. The full-level and fixed-fibre meanings of
   $\mathscr J^{\rm safe}$ in (191.C9)--(191.C11) must be separated.
5. The bounded-array paragraph incorrectly takes arbitrary jump atoms as
   independent. A jump array must be a zero-extended coboundary. The
   correct control is the exact $L^\infty$ norm on bounded height arrays
   $W$, attained by $W_r(h)=z_r^{-h}$. It is a
   coefficient-uniform mechanism control, not a member of the fixed
   literal endpoint family and not a disproof of (191.C12).

These are exact formal repairs, not a rejection of (191.C8)--(191.C10).
Until they are made and replayed, the candidate should remain pending
review and no graph node should be promoted.

## 2. Exact reviewed statement and required hypotheses

The reviewed local packet fixes

\[
 U=mq\mid u,\quad g=u/U,\quad
 U>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,
\tag{191.R2}
\]

with $\kappa,g,U$ odd, $(u,v)=1$, $(U,h)=1$,
$0<2\kappa gh<R_0$, and the Round-189 fast predicate
$j_q(a,v)>T_Q$. The statement also needs, explicitly,

\[
 u,v\asymp {L\over\kappa},\qquad
 {\rm length}(\mathcal V_{\rm lit})\ll u,\qquad
 L\ll X^{1/4}.
\tag{191.R3}
\]

The first two clauses justify the residue-class multiplicities in
(191.C27); the third justifies absorption of $Q$ and fixed logarithmic
powers in (191.C35). Merely saying “retain the accepted packet” is too
implicit for a durable formal candidate whose proof later invokes these
facts.

For the signed inverse

\[
 \varrho v-\gamma U=1,\qquad
 -{U-1\over2}\leq\varrho\leq{U-1\over2},
\]

the sector

\[
 0<|\varrho|\leq
 \min\left\{{U-1\over2},
 \left\lfloor{QmU\over Y}\right\rfloor\right\}
\tag{191.R4}
\]

is an exact predicate on literal rows. It may be intersected with the
fast $J$-band before any operation. Its complement is the same fast
packet with the single additional predicate $|\varrho|>T_\varrho$.

The review distinguishes three levels that the repaired candidate must
name separately:

- the fixed $(\kappa,u,m,q,a,J)$ complex packet;
- its exact safe linear subpacket, still summed jointly over both
  orientations and all literal $v,h,t$ labels; and
- the full $\mathscr F_{Y,Q}^{\sigma}$ after restoring
  $m^{-1}c_q(a)$ and every outer label.

At each level the complement must be defined by complex subtraction
before the one final real part. An absolute estimate for an already
defined safe projection is permitted; an inner absolute value in the
remainder is not.

## 3. Proof and line-by-line seam audit

### 3.1 C14--C15: Abel identity

These equations are GREEN. For finite zero-extended $W$,

\[
 \sum_h\{W(h)-W(h-1)\}z^h
 =(1-z)\sum_hW(h)z^h.
\tag{191.R5}
\]

The upper death is included, the denominator is $1-z$, and the sign in
(191.C15) is positive. Since the fast slope is a unit,
$z\neq1$. Abel is an exact re-expression, not a saving.

### 3.2 C16--C20: determinant transport and parity projector

These transport equations are GREEN. From
$\varrho v-\gamma U=1$,

\[
 (S,w)\mapsto(S-\varrho,w-\gamma)
\]

sends $Sv-Uw=h$ to $h-1$, while

\[
 (S,w)\mapsto(S+\varrho,w+\gamma)
\]

sends $Uw-vS=h$ to $h-1$. Thus the uniform form
$(S,w)\mapsto(S-\epsilon_\omega\varrho,
w-\epsilon_\omega\gamma)$ is correct, as are (191.C18)--(191.C20).
The canonical carry $\nu_\omega$ lies in $\{-1,0,1\}$ and the affine
sign ratio is $(-1)^{\nu_\omega(h)}$.

Before Fourier splitting, $U$ odd gives

\[
 (-1)^{S_{0,\omega}(h)+t}=(-1)^{S_\omega(h,t)}.
\]

The old and transported bare site parities differ by
$(-1)^\varrho$ in both orientations. This is exact. It does not survive
mode restriction. For one mode, including the affine reindexing, the
old/new factor is exactly (191.R1), because
$k=ma$, $U=mq$, and $\varrho\equiv\bar v\pmod q$.

The repaired candidate must use the following unambiguous language:

- $(-1)^\varrho$ belongs to the complete original anchor;
- the retained fast summand has (191.R1), which depends on the carry and
  the mode;
- multiplication by the carry sequence mixes Fourier modes, so the fast
  projector does not inherit the full-anchor parity identity; and
- recombining all modes restores the identity but self-returns to the
  pre-Round-187 high-height aggregate.

No appearance of $(-1)^\varrho$ may be used inside (191.C23) or the
fast remainder. The blind statement correctly says the original anchor
has already been replaced by its Fourier phase and is not also present
in $W$.

### 3.3 C21--C23: outer masks and affine births/deaths

The intended partition is correct but needs a displayed gated identity.
Let $K_h,G_h,A_h$ have the meanings of (191.C21), and put a minus
subscript for height $h-1$. The exact disjoint partition is:

\[
\begin{cases}
 K_hG_hA_h-K_-G_-A_-,&K_h\neq K_-,\\[1mm]
 (G_h-G_-)A_h+G_-(A_h-A_-),
   &K_h=K_-=1,\\[1mm]
 0,&K_h=K_-=0.
\end{cases}
\tag{191.R6}
\]

The first line is the complete outer-interval birth or death, not merely
$(K_h-K_-)$ times a freely chosen current coefficient. The second line
isolates the coprimality flip and uses $A_h-A_-$ only when both outer
masks persist. This is the precise version needed for the terminal
estimate.

On the last term in (191.R6), the transported common/birth/death formula
(191.C23) is correct. Its common-site sign

\[
 (-1)^t\{B_h(t)-(-1)^{\nu_\omega(h)}
 B_-^{\rm tr}(t+\nu_\omega(h))\}
\]

is the retained-mode affine comparison. It must not be simplified with
the pre-Fourier constant $(-1)^\varrho$.

### 3.4 C24: carry, Fejer, endpoint, and phase telescoping

Equation (191.C24) is algebraically GREEN. Writing
$B_h=F_h\Lambda_h\Psi_h$ and
$B_-^{\rm tr}=F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}$, its right side
sums exactly to $B_h-\chi B_-^{\rm tr}$. The ordering chosen there is
legitimate. The carry term is $(1-\chi)B_-^{\rm tr}$; the Fejer term is
an exact scalar difference; no regularity is inferred for the endpoint
or phase terms.

### 3.5 C25: endpoint factors and literal jump sources

This seam is YELLOW and requires a mechanical repair. The quantity
$\Lambda$ is the product of two orientation-dependent endpoint
coefficients, with one conjugated. Before applying (191.C25), the
candidate must display, in its chosen order,

\[
\begin{aligned}
 \Lambda_h-\Lambda_-^{\rm tr}
 ={}&(\lambda_{{\rm up},h}
       -\lambda_{{\rm up},-}^{\rm tr})
       \overline{\lambda_{{\rm low},h}}\\
 &+\lambda_{{\rm up},-}^{\rm tr}
   \left(\overline{\lambda_{{\rm low},h}}
        -\overline{\lambda_{{\rm low},-}^{\rm tr}}\right),
\end{aligned}
\tag{191.R7}
\]

or the exactly corresponding ordered identity. It must then apply
(191.C25) separately to both endpoint factors, using their actual
orientation-specific divisor arguments. Without (191.R7), the singular
symbol $\lambda$ in (191.C25) does not itself establish exhaustion of
both endpoint jumps.

After this repair, the candidate's first-changed-field construction can
cover every listed source:

- endpoint squarefree and allocation-coprimality masks;
- the residual selected-prime mask and all divisibility predicates;
- shell/cone/profile, floor, star, half-weight, hard-sample, crossing,
  endpoint-trace, and endpoint zero-extension labels;
- both endpoint coefficient values and conjugation;
- the affine positivity births/deaths, carries, Fejer factor, and actual
  square-root phase; and
- the outer dyadic/carrier terminal and $(U,h)=1$ changes from
  (191.R6).

The repaired ordered list must distinguish the outer $K$ terminal zero
from an endpoint coefficient's own zero extension. Otherwise the phrase
“terminal-zero labels” in C25 can appear to count the same outer event a
second time. No additional literal source is conceptually absent, but
the present formulas do not yet prove exact-once coverage.

### 3.6 Signed-inverse count and outer ledger

Equations (191.C26)--(191.C28) are GREEN once (191.R3) is stated. The
inverse map is a unit-class bijection, there are at most
$2T_\varrho$ signed classes, and each occurs $O(u/U)$ times. Hence the
row count is $O(Qmu/Y)$; $Y$ heights and $O(\kappa)$ sites give
$Qm\kappa uX^\eta$. The fast $J$ predicate only deletes rows. Floor-zero
and saturation are both correctly handled.

Equations (191.C33)--(191.C35) are also GREEN once $L\ll X^{1/4}$ and
$u\asymp L/\kappa$ are explicit. The exact $1/m$ removes the projective
$m$ before positivity, $\sum_a|c_q(a)|\ll\log(2q)$, and
$\sum_{mq\mid u}1=\tau_3(u)$. There is no fourth divisor variable and no
positive power of $Y$ is absorbed.

### 3.7 Terminal and Fejer projections under one outer operation

The numerical bounds (191.C30) and (191.C32) are sound:

- $K$ is the intersection of two integer intervals, so its complete
  boundary contribution has at most two heights and costs
  $O(\kappa)$ per row;
- on a nonempty live block,
  $2\kappa gY/R_0<1$; therefore the isolated Fejer difference over
  $O(Y)$ heights and $O(\kappa)$ sites costs $O(\kappa)$ per row; and
- $(q/J)(uJ/q)$ restores $O(\kappa uX^\eta)$.

The one-outer-operation rule requires a definition repair, not a new
estimate. Define $\mathscr J_{\rm terminal}$ as the sum of the first
line of (191.R6) over all rho-large rows and both orientations, and
define $\mathscr J_{\rm Fejer}$ as the C24 Fejer term only on
$K_h=K_-=G_h=G_-=1$ and transported common sites. Complete each complex
sum before taking its modulus. Then

\[
 \mathscr J^{\rm safe}
 =\mathscr J_{\rm inv}
  +\mathscr J_{\rm terminal}
  +\mathscr J_{\rm Fejer}
\tag{191.R8}
\]

is an exact linear subpacket and triangle inequality among these three
already target-safe projections is lawful. The remainder is defined by
complex subtraction. This does not put an absolute value inside the
remaining signed packet and does not separately norm the two
orientations.

### 3.8 Bounded-array scope

The last paragraph of Section 7 needs replacement. Arbitrary jump atoms
are not independent because $\Delta^-W$ is a zero-extended coboundary.
For oriented rows $r$ with $n_r$ heights, the correct statement is

\[
 \left\|
 \sum_r{1\over1-z_r}\sum_h\Delta^-W_r(h)z_r^h
 \right\|_{\prod_r\ell^\infty\to\mathbb C}
 =\sum_r n_r.
\tag{191.R9}
\]

The upper bound follows from Abel and triangle inequality; equality is
attained by the legitimate zero-extended arrays
$W_r(h)=z_r^{-h}$ on their row intervals. Both orientations can be
chosen to contribute positive real values under one outer operation.
This proves insufficiency of arguments using only support and
pointwise bounds. It does not prove that such arrays arise from the
literal pair of endpoint coefficients, and it does not lower-bound or
disprove (191.C12). Atomwise dephasing of the square-root phase may be
mentioned only as a broader coefficient-uniform control with the same
quarantine.

## 4. First doubtful or unproved step

For the strict signed-inverse sector there is no doubtful mathematical
step after adding (191.R3). The first formal defect is the absent
two-endpoint identity (191.R7), because C25 presently does not
mechanically establish exact-once coverage of both endpoint factors.

For the open analytic remainder, the first genuinely unproved estimate
is unchanged:

\[
 \left|\sum_{\substack{\omega,v\ {\rm fast}\\
 |\varrho_U(v)|>T_\varrho}}
 {1\over1-z_{\omega,v}}
 \sum_h\Delta^-W_{\omega,v}(h)z_{\omega,v}^h\right|
 \ll Qm\kappa uX^\varepsilon
\tag{191.R10}
\]

at fixed outer labels and band, or an exactly ledger-equivalent
one-sided theorem after full recombination. Positive variation gives
only $Y\kappa uX^\varepsilon$, with deficit $Y/(Qm)$. The safe terminal
and Fejer projections do not reduce this deficit in the remaining carry,
birth/death, endpoint-mask, common-cell, and square-root-phase packet.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| C14 backward Abel sign | GREEN: (191.R5) is exact and endpoint-free under zero extension. |
| C15 denominator | GREEN: $1-z$, not $1-z^{-1}$; $z\neq1$ on the fast unit band. |
| C16--C20 transport signs | GREEN: plus subtracts $(\varrho,\gamma)$ and minus adds it. |
| Full parity versus retained mode | REPAIR: add (191.R1) and prohibit use of $(-1)^\varrho$ inside the fast projector. |
| Exact fast and signed-inverse complement | GREEN locally; REPAIR notation so fixed-fibre and full-complex levels are not conflated. |
| Small signed-inverse class count | GREEN after explicitly adding (191.R3). |
| Floor-zero and saturation | GREEN: the sector is respectively empty or contains every unit inverse class. |
| C21 outer masks | REPAIR: replace the verbal split by the gated identity (191.R6). |
| C23 affine common/birth/death | GREEN once invoked only on the persistent-mask branch of (191.R6). |
| C24 carry/Fejer/endpoint/phase | GREEN: algebraically exact. |
| C25 literal endpoint exhaustion | REPAIR: add the two-factor/conjugation identity (191.R7) and apply C25 to both endpoints. |
| Missing or duplicate jump source | No conceptual omission found; REPAIR the distinction between outer $K$ terminal zero and endpoint zero-extension labels. |
| Terminal isolation | GREEN estimate; REPAIR its exact complex projection definition as in (191.R8). |
| Fejer isolation | GREEN estimate; REPAIR its persistent-mask/common-site projection definition as in (191.R8). |
| One outer real part and both orientations | GREEN only after the safe projections are defined jointly before modulus; no separate orientation norm is licensed. |
| Lift/coefficient/divisor ledger | GREEN after stating $u\asymp L/\kappa$ and $L\ll X^{1/4}$. |
| Arbitrary bounded jump atoms | REJECT as stated; replace with the bounded-$W$ coboundary norm (191.R9). |
| Literal lower mass | GREEN quarantine after the bounded-array repair: none is asserted. |
| Complete fast packet | OPEN: (191.C12)/(191.R10) remains the first analytic obstruction. |
| Downstream owner scope | REPAIR to list every remaining owner explicitly, not “a bridge” or “an M1 parent” generically. |
| Exponent scope | REPAIR to state that $1/3$, $0.3144831759740614\ldots$, and $1/4$ are unchanged. |
| Numerical evidence | GREEN: none is used. |

## 6. Dependencies and exact artifacts used

Only the four assigned artifacts were used:

1. protocol.md —
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
2. candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md —
   21b5c881a37a3dd6eb719928931fc92d45d2ab1c3636f7bed24e997c31a763cb.
3. blind_statement.md —
   3334c6dd1610e6f4398f4424775a7b0ccc435ba7aa456be8eb430f88a0f13781.
4. reports/joint_hv_phase_jump_hostile_audit.md —
   902ea86fd79cef97ab2a4e3ad0f92457b49d13c97212a03be70078ada656b22e.

No state file, sibling report, external source, web result, or numerical
computation was used.

## 7. Recommended state effect

**Revise; do not promote the candidate in its current form.**

Require all of the following before a post-repair replay:

1. Add the explicit support connectors (191.R3).
2. Add the retained-mode parity equation (191.R1) and the exact
   full-projector/self-return caveat.
3. Add the gated outer-mask identity (191.R6), the two-endpoint
   telescoping identity (191.R7), and a disjoint ordered field list that
   distinguishes outer terminal zero from endpoint zero extensions.
4. Define the signed-inverse, terminal, and Fejer safe terms as exact
   complex projections at fixed-fibre and full-aggregate levels, then
   define the complement by complex subtraction as in (191.R8).
5. Replace arbitrary independent jump-atom capacity by the legitimate
   bounded-height coboundary statement (191.R9).
6. Replace the downstream shorthand by the complete quarantine:
   every original $t\geq2$ small-$G$ incidence, the large-$G$
   near-resonant complement, the rest of the small-$t$ owner, the hard
   and smooth M1 parents, GAR, every M2 parent, endpoint uniformity, M9,
   both bridges, and the Gauss-circle quarter target all remain open or
   conditional at their existing scopes. The internal exponent $1/3$,
   accepted external benchmark $0.3144831759740614\ldots$, and target
   $1/4$ remain unchanged.

After these repairs, the strict signed-inverse plus terminal/Fejer
reduction is suitable for a fresh independent replay. The fast
rho-large signed remainder and every downstream owner must remain open.
