# Round 119 discovery report: literal M1 parent capacity attack

- Campaign: `m9-m1-direct-parent-minimax-gate`
- Task: `literal_m1_parent_capacity_attack`
- Role: discovery
- Starting graph SHA-256: `c3498daad3bdceb7c69c0e47a616e03ebfa12ccaf42f8df42958aa227f50fd91`
- Status: candidate evidence only; no shared state is changed.

## 1. Result

**Separate-parent direct-menu minimax and adjacent-profile no-go.**  Remove
the bottom, `R5-Full`, terminal, target-sized full-second-derivative, and
TTY owners in the accepted order, and let \(\Lambda_{\rm hard}\) and
\(\Lambda_{\rm sm}\) be the resulting literal hard and smooth M1 label
sets.  For a residual label \(\lambda=(D,L)\), suppressing the common
\(X^\varepsilon\) factor, define the accepted direct capacity

\[
 \mathfrak C(D,L;X)=\min\!\left\{
  1+\frac DL,
  1+\sqrt{\frac{LX}{D}}+\frac{D^{3/2}}{\sqrt{LX}},
  X^{89/1282}L^{89/1282}D^{819/1282}
 \right\}.                                      \tag{1.1}
\]

Then the two physical parents have the same, but logically separate,
exact minimax exponent:

\[
 \boxed{
 \sup_{\lambda\in\Lambda_{\rm hard}}\mathfrak C(\lambda;X)
   \asymp X^{1/3},\qquad
 \sup_{\lambda\in\Lambda_{\rm sm}}\mathfrak C(\lambda;X)
   \asymp X^{1/3}}
                                                        \tag{1.2}
\]

at the level of the accepted numerical capacity functions (fixed profile
constants and the common \(X^\varepsilon\) loss being suppressed).  Thus
neither parent is shrunk below the already accepted one-third menu.

The smallest literal witnesses needed for (1.2) are one interior frequency
shell of the unique hard profile \(D_0=\lfloor\sqrt X\rfloor\), and one
interior frequency shell of the first smooth profile
\(D_1=\lfloor\sqrt X\rfloor/2\), in each case with

\[
 L_j\asymp D_jX^{-1/3}\asymp X^{1/6}.             \tag{1.3}
\]

Both have accepted-menu capacity \(X^{1/3+o(1)}\) against the physical
target \(X^{1/4}\).  On the normalized hard cone this is exactly the
coefficient-blind \(L^2\) capacity against the \(L^{3/2}\) target.  The
missing factor is

\[
 X^{1/12}=L^{1/2+o(1)}.                            \tag{1.4}
\]

No accepted adjacent-profile identity or already-proved blockwise owner
removes either witness.  This is a minimax/no-go theorem for the accepted
upper-bound menu, not a lower bound for either actual signed sum.

## 2. Exact statement and hypotheses

Let \(X\) be sufficiently large and real,

\[
 y=\lfloor\sqrt X\rfloor,\qquad D_j=2^{-j}y,\qquad
 H_j=\lfloor D_jX^{-1/4}\rfloor.
\]

Use the accepted fixed nonnegative telescoping denominator partition, the
exact clipped dyadic frequency partition, both frequency signs, the Vaaler
taper, endpoint stars and half weights, and the real-\(X\) convention.  The
profile \(j=0\) is the unique hard profile containing \(d=y\); every
\(j\geq1\) profile is smooth.  The positive-frequency block is

\[
 B_1(D,L;X)=
 \sum_{h\asymp L}\frac{\Phi(h/(H_D+1))}{h}
 \sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),          \tag{2.1}
\]

with the negative frequency retained by the exact real-even pairing.  Put
\(\delta=\log_XD\), \(\ell=\log_XL\), and \(a=\delta-\ell\).  On

\[
 \Omega=\{1/4\leq\delta\leq1/2,
             0\leq\ell\leq\delta-1/4\},
\]

the residual is the literal lift of

\[
 \mathcal U_1=
 \{(\delta,\ell)\in\Omega:
    \ell<\delta-1/4,\ 178\ell+1638\delta>463\}
 \setminus\{(1/2,0)\}.                            \tag{2.2}
\]

For every such label, (1.1) is the minimum of all accepted direct rows
relevant to the present question.  Its exponent is

\[
 c(\delta,\ell)=\min\left\{
 a,\frac{1-a}{2},
 t(\delta,\ell)
 \right\},\qquad
 t(\delta,\ell)=\frac{89(1+\ell)+819\delta}{1282}. \tag{2.3}
\]

Indeed the companion second-derivative exponent
\((3\delta-1-\ell)/2\) is no larger than
\((1+\ell-\delta)/2=(1-a)/2\) on \(\Omega\), and the exponent-zero
term is smaller still.  The trivial \(D\)-row cannot improve (2.3), since
\(D/L\leq D\).

The complete critical ridge of this capacity function is

\[
 a=\frac13,qquad \delta\geq\frac{92}{227}.        \tag{2.4}
\]

The first condition is the unique contact of the two elementary rows.  On
that line

\[
 t=\frac{178/3+908\delta}{1282},
\]

so \(t\geq1/3\) exactly when \(\delta\geq92/227\).  Formula (2.4)
describes numerical menu contact only; the two physical parent sets remain
separate even where their exponent images coincide.

For the hard transform, let \(q=X/y^2=1+O(X^{-1/2})\) and let
\(\mathcal T_{\mathrm{M1},L}\) have the accepted normalized symbol.  The
proved transform gives, up to target-sized boundary and transform errors,
the scale relation

\[
 B_{1,\mathrm{hard},L}
  =c_\star X^{1/4}L^{-3/2}\mathcal T_{\mathrm{M1},L}
    +O_\varepsilon(X^{1/4+\varepsilon}),          \tag{2.5}
\]

where \(c_\star\neq0\) is the fixed accepted constant.  Consequently the
normalized accepted hard capacity is

\[
 \mathfrak K_{\rm hard}(L;X)=L^{3/2}X^{-1/4}
     \mathfrak C(y,L;X).                           \tag{2.6}
\]

In particular the full second-derivative row in (2.6) is

\[
 L^{3/2}X^{-1/4}\left(
   1+\sqrt{LX/y}+\frac{y^{3/2}}{\sqrt{LX}}
 \right)
 =O\!\left(L^{3/2}X^{-1/4}+q^{1/4}L^2+q^{-3/4}L\right). \tag{2.7}
\]

Thus its leading normalized capacity is genuinely \(L^2\), not
\(L^{3/2}\).

## 3. Proof or derivation

First, on the whole active triangle,

\[
 \min\left(a,\frac{1-a}{2}\right)\leq\frac13,
\]

with equality only at \(a=1/3\).  Adding the TTY row can only decrease
this numerical capacity.  This proves the upper half of both assertions in
(1.2), independently for the two physical parent sets.

For literal witnesses, choose for \(j=0,1\) an actual dyadic frequency
index \(r_j(X)\) whose shell scale satisfies

\[
 D_jX^{-1/3}\leq L_{j,r_j}<2D_jX^{-1/3}.           \tag{3.1}
\]

Such an index exists in the fixed dyadic frequency partition because

\[
 \frac{H_j}{D_jX^{-1/3}}\asymp X^{1/12}\longrightarrow\infty.
\]

Equivalently, \(r_j=(\log_2X)/12+O(1)\).  Moreover
\(L_{j,r_j}\gg X^{1/6}\), while
\(L_{j,r_j}/H_j\asymp X^{-1/12}\).  Hence this is a nonempty interior
shell: it is neither a bounded-frequency clip nor the terminal shell.

For both \(j=0\) and \(j=1\), (3.1) gives

\[
 1+\frac{D_j}{L_{j,r_j}}\asymp X^{1/3},            \tag{3.2}
\]

and

\[
 \sqrt{\frac{L_{j,r_j}X}{D_j}}\asymp X^{1/3},
 \qquad
 \frac{D_j^{3/2}}{\sqrt{L_{j,r_j}X}}\asymp X^{1/6}. \tag{3.3}
\]

Since \(D_0\asymp D_1\asymp X^{1/2}\) and
\(L_{j,r_j}\asymp X^{1/6}\), the exact TTY row costs

\[
 X^{89/1282}L_{j,r_j}^{89/1282}D_j^{819/1282}
   =X^{770/1923+o(1)},                             \tag{3.4}
\]

where

\[
 \frac{770}{1923}-\frac13=\frac{43}{641}>0.       \tag{3.5}
\]

Thus the minimum in (1.1) is \(X^{1/3+o(1)}\) on each witness.  This
proves the lower half of the two *numerical capacity* assertions in (1.2).
It also audits rather than discards TTY: the theorem applies to both
profiles, but its bound is strictly more expensive here.

The labels really lie in the residual.  Their exponents satisfy
\(\delta_j=1/2+O(1/\log X)\),
\(\ell_j=1/6+O(1/\log X)\); hence
\(\ell_j<\delta_j-1/4\) by a limiting gap \(1/12\), and

\[
 178\ell_j+1638\delta_j=\frac{2546}{3}+o(1)>463.   \tag{3.6}
\]

They are not bottom labels, `R5-Full` owns only the Fejer residual, they are
not terminal, and they are not the isolated full-second-derivative target
cell \((1/2,0)\).  Thus neither witness is reassigned by owner priority.

Floors and physical support do not destroy the witnesses.  The accepted
profile certificate gives \(H_j\asymp D_jX^{-1/4}\), positive profile
mass \(\gg D_j\), and exactly one hard jump.  Since \(L_j\to\infty\) and
\(L_j/H_j\to0\), the frequency taper has a genuine interior shell.  For
the hard transform, \(q=1+O(X^{-1/2})\), and the fixed interval
\(4h<n<16h\) contains \(\asymp h\) odd integers for every
\(h\asymp L_j\); endpoint stars and real-\(X\) support crossings affect
only their prescribed boundary weights.  The first smooth profile is a
full smooth rescaling and does not acquire the hard sample \(d=y\).

At the hard witness, (2.6)--(2.7), (3.2), and (3.4) give

\[
 \mathfrak K_{\rm hard}(L_0;X)\asymp L_0^2
       \asymp X^{1/3},                             \tag{3.7}
\]

whereas the cone target is \(L_0^{3/2}\asymp X^{1/4}\).  This is exactly
the same \(L_0^{1/2}=X^{1/12+o(1)}\) deficit as the smooth physical
comparison, with no identification of the two sums.

Finally, adjacent profiles do not telescope at the block level.  For two
adjacent scales the coefficient of a fixed \((h,d)\) is

\[
 \chi_4(d)e(hX/d)
 \{u_{j,r}(h)w_j(d)+u_{j+1,r'}(h)w_{j+1}(d)\}.     \tag{3.8}
\]

Although the spatial weights participate in a partition of unity,
\(u_{j,r}\) and \(u_{j+1,r'}\) have different height floors, Vaaler
tapers, clipped frequency supports, and endpoint conventions.  Hence
(3.8) does not factor through a common frequency coefficient.  The
accepted adjacent-height calculation has order-one \(1/h\)-weighted
capacity under a dyadic height change, and the exact scale-difference
identity retains both a profile difference and a height-symbol difference.
The original scale terms have no built-in opposite profile sign; the hard
sample is additionally unmatched.  Even a lawful merge into one
fixed-ratio BV profile would change \(D\) only by a constant and would
leave (3.2)--(3.4) unchanged.  Thus no coefficientwise adjacent identity
with a power gain is present, and a bound for an adjacent aggregate would
not by itself imply either coordinatewise parent.

The other accepted statements do not shrink the witnesses.  The ordered
resonance estimate is bounded by \(\min(D,\sqrt{LX/D})\) and returns the
same \(X^{1/3}\) cost here.  The hard transform is an equivalence with
target-sized errors, not an estimate.  The canonical Gram is both open and
post-global: it has no inverse localization to \((D,L)\).  GAR is an
alternative total-active-M1 statement; even if proved, the summation map
from physical blocks to the total has a nontrivial kernel and supplies no
individual block bound.  Therefore no accepted owner or route identity
strictly shrinks either direct parent.

## 4. First doubtful or unproved step

The first unproved analytic step is an actual-symbol estimate that saves
\(X^{1/12}\) on either literal critical family: equivalently
\(\mathcal T_{\mathrm{M1},L_0}\ll L_0^{3/2}X^\varepsilon\) on the hard
shell, or \(B_1(D_1,L_1;X)\ll X^{1/4+\varepsilon}\) on the first smooth
shell.  No such estimate is proved here.  Likewise, no coefficientwise
adjacent-profile connector with a block-local inverse is known.

The assertion \(\mathfrak C\asymp X^{1/3}\) is only a lower bound for the
minimum of the *listed upper-bound capacities*.  It gives no arithmetic
lower bound for \(|B_1|\) or \(|\mathcal T_{\mathrm{M1},L}|\), and
therefore does not rule out a genuinely new sign-sensitive inequality.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_m1_block_and_profiles` | **Pass.** Equation (2.1) retains the actual Vaaler taper, physical profile, both signs, and literal frequency shell. |
| `owner_priority_and_U1` | **Pass.** Bottom, Fejer residual, terminal, full-second-derivative target cell, and TTY wedge are removed in the accepted order; (3.6) leaves both witnesses in \(\mathcal U_1\). |
| `hard_smooth_physical_split` | **Pass.** \(j=0\) is hard because it alone contains \(y\); \(j=1\) is smooth despite both having exponent \(1/2+o(1)\). |
| `frequency_first_capacity` | **Pass.** It is \(1+D/L\asymp X^{1/3}\) on both critical labels. |
| `full_second_derivative_capacity` | **Pass.** Its two nonconstant terms are respectively \(X^{1/3+o(1)}\) and \(X^{1/6+o(1)}\); the bound is their sum, so its capacity is \(X^{1/3+o(1)}\). |
| `TTY_exponent_and_hypotheses` | **Pass.** Both accepted BV profiles, including the one-jump hard profile, satisfy the theorem's fixed-profile hypotheses.  Its exact cost is \(X^{770/1923+o(1)}\), worse than one third at the witnesses. |
| `critical_hard_label` | **Pass.** The \(j=0\), \(r_0=(\log_2X)/12+O(1)\) interior shell exists, is residual, and has physical capacity \(X^{1/3}\). |
| `critical_first_smooth_label` | **Pass.** The \(j=1\), \(r_1=(\log_2X)/12+O(1)\) full-smooth interior shell exists, is residual, and has physical capacity \(X^{1/3}\). |
| `floor_star_support_and_real_X` | **Pass.** \(H_j\asymp D_jX^{-1/4}\), \(L_j\gg1\), \(L_j/H_j\to0\), \(q=1+O(X^{-1/2})\), and the strict hard-cone support contains many interior odd integers; floors and stars retain, rather than delete, the labels. |
| `hard_cone_physical_normalization` | **Pass.** Multiplication by \(L^{3/2}X^{-1/4}\) gives (2.7); at contact the capacity is \(L^2\), target \(L^{3/2}\), deficit \(L^{1/2}\). |
| `adjacent_profile_telescope` | **No-go/pass.** Spatial telescoping does not telescope the scale-dependent frequency coefficients.  The exact difference retains full-capacity height/profile terms, and the hard sample is unmatched. |
| `menu_optimality_vs_lower_bound` | **Pass.** (1.2) is explicitly a menu-capacity minimax.  No lower bound for an actual signed sum is asserted. |
| `canonical_Gram_and_GAR_nonimplication` | **Pass.** Neither route has a block-local inverse; canonical is a partial post-global packet and GAR controls only the total active aggregate. |
| `downstream_scope` | **Pass.** Neither parent, M9-M1, M9, endpoint uniformity, nor the quarter theorem is proved; the existing one-third theorem is unchanged. |

No numerical experiment or web/source import was used.  The work was
entirely algebraic and capacity-theoretic.

## 6. Dependencies and exact artifacts used

Mathematical dependencies used are the accepted H4 coefficient and
\(\Phi\)-regularity convention; the fixed dyadic denominator/frequency
profile certificate; `R5-Full`; the frequency-first divisor bound; the
full second-derivative block bound; the audited M1 TTY theorem; the exact
\(\mathcal U_1\) phase diagram; the hard-top transform; the physical
one-count assembly; the adjacent-height/scale capacity obstruction; and
the canonical/GAR route-scope obstruction.  No result from an unproved
canonical Gram hypothesis was used as an estimate.

Exact artifacts read and used:

- `protocol.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/briefs/literal_m1_parent_capacity_attack.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`
- `rounds/codex-managed/gc-unconditional-exponent-extraction/reviews/conductor_round91_block_optimization.md`
- `rounds/codex-managed/m9-m1-route-interface-assembly/synthesis.md`
- `rounds/codex-managed/m9-m1-route-interface-assembly/reports/m1_route_assembly_attack.md`
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/derivation_packet.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/candidates/conductor_m1_parent_capacity_chart.md`

## 7. Recommended state effect

**Promote** a normalization/obstruction statement recording (1.1)--(1.4):
the accepted direct menu has separate hard-parent and smooth-parent minimax
capacity \(X^{1/3+o(1)}\), witnessed respectively by the literal hard and
first-smooth \(L\asymp X^{1/6}\) labels.  Record the complete menu critical
ridge (2.4) and the exact TTY cost \(770/1923\) at the two named witnesses.

**Retain open without shrink**
`M9-M1-top-endpoint-signed-cone` and
`M9-M1-direct-smooth-residual-blockwise-estimate`.  Record that raw
adjacent-profile telescoping, a fixed-ratio BV merge, the ordered-resonance
bound, the canonical Gram without a block-local inverse, and GAR as a
total estimate do not reduce either direct parent.

Do not change `M9-M1`, `M9`, `M9-M2`, endpoint uniformity, the internal
one-third exponent, or the quarter target.  A direct continuation needs a
new sign-sensitive \(X^{1/12}\) gain on each critical parent (or a proved
coefficientwise connector replacing both).  The lawful global backup
instead requires both open parents
`M9-M1-global-lower-radial-signed-estimate` and
`M9-M1-global-radial-interface-estimate`, which would imply GAR through
the accepted global radial one-count assembly but still would not prove
the blockwise M9-M1 node.
