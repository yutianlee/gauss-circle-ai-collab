# Round 119 statement-only rederivation: separate hard/smooth M1 parent minimax

## 1. Result: direct-menu minimax obstruction

**Result (no-go for the accepted direct menu).** After the owner order in the
blind statement is applied, the asymptotic minimax exponent of the stated
direct menu is $1/3$ separately on each of the two physical parents.

* On the hard parent, the unique literal profile $D_0(X)$ containing
  $q_X:=\lfloor\sqrt X\rfloor$, together with a literal frequency block
  $L_*(X)\asymp X^{1/6}$, has best stated physical capacity
  $X^{1/3+o(1)}$. The cone sizes $L_*^2$ and target $L_*^{3/2}$ are
  normalized sizes. Multiplication by the physical conversion factor
  $F(L):=X^{1/4}L^{-3/2}$ sends them respectively to
  $F(L_*)L_*^2=X^{1/4}L_*^{1/2}\asymp X^{1/3}$ and
  $F(L_*)L_*^{3/2}=X^{1/4}$.
* On the smooth parent, the first literal profile $D_1(X)$ immediately below
  the hard profile, with $D_1\asymp q_X/2$, and the same $L_*(X)$, has best
  stated capacity $X^{1/3+o(1)}$, whereas its target is $X^{1/4}$.

Thus each parent retains the same exponent deficit $X^{1/12}$; in the hard
normalization this is exactly the missing factor $L_*^{1/2}$. None of the
accepted owners, none of (119.B6)--(119.B8), and no literal adjacent-profile
identity supplied by the statement removes either witness. This is a
minimax statement about the listed **upper-bound capacities**, not an
$\Omega$-bound for either arithmetic sum.

## 2. Exact statement and hypotheses

Assume exactly (119.B1)--(119.B9), including the literal denominator
partition, its endpoint/star convention, both frequency signs, the unique
hard-profile assignment of $q_X=\lfloor\sqrt X\rfloor$, and real $X\ge2$.
Put

\[
 t:=\delta-\ell\in[1/4,1/2],\qquad
 c(\delta,\ell):=\frac{89(1+\ell)+819\delta}{1282}.
\]

For a smooth residual label define the exponent of the accepted direct menu
by

\[
 m_{\rm sm}(\delta,\ell)
 :=\min\left\{t,\frac{1-t}{2},c(\delta,\ell)\right\}.
\tag{R119.1}
\]

For the hard profile, whose scale exponent is

\[
 \delta_0(X):=\frac{\log D_0(X)}{\log X}=\frac12+o(1),
\]

the normalized coefficient-blind cone has size $L^2$, while its normalized
target is $L^{3/2}$. The exact transform converts normalized sizes to
physical $B_1$ sizes by

\[
 F(L):=X^{1/4}L^{-3/2}.
\]

Consequently the physical coefficient-blind cone row is
$F(L)L^2=X^{1/4}L^{1/2}$, of exponent $1/4+\ell/2$. Hence the hard direct
capacity menu, now entirely in physical units, is

\[
 m_{\rm hard}(\delta_0,\ell)
 :=\min\left\{\frac14+\frac{\ell}{2},\delta_0-\ell,
 \frac{1+\ell-\delta_0}{2},c(\delta_0,\ell)\right\}.
\tag{R119.2}
\]

The conclusions are

\[
 \sup_{\substack{\text{smooth literal labels}\\
                         (\delta,\ell)\in\mathcal U_1}}
 m_{\rm sm}(\delta,\ell)=\frac13+o(1),
 \qquad
 \sup_{\substack{\text{hard residual}\\\text{frequency labels}}}
 m_{\rm hard}(\delta_0,\ell)=\frac13+o(1).
\tag{R119.3}
\]

Here $o(1)$ only records fixed literal profile constants, the floor in
$q_X$, and frequency discretization. At continuous exponent scale the two
values are exactly $1/3$. The complete continuous equality locus for the
smooth three-bound menu is

\[
 \ell=\delta-\frac13,\qquad
 \frac{92}{227}\le\delta\le\frac12.
\tag{R119.4}
\]

The two requested top physical witnesses are the hard $D_0$ label and the
first smooth $D_1$ label at the endpoint
$(\delta,\ell)=(1/2,1/6)$.

| Physical parent | Literal residual domain | Accepted capacities compared | Critical literal survivor | Target at survivor | Minimax |
|---|---|---|---|---|---|
| Hard | Middle/lower residual shells of the unique profile containing $q_X$ | physical cone row $F(L)L^2=X^{1/4}L^{1/2}$, (119.B6), full (119.B7), (119.B8) | $D_0\asymp q_X,\ L_*\asymp X^{1/6}$ | $F(L_*)L_*^{3/2}=X^{1/4}$ | $X^{1/3+o(1)}$ |
| Smooth | Every other literal profile whose label lies in $\mathcal U_1$ | (119.B6), full (119.B7), (119.B8) | first smooth $D_1\asymp q_X/2,\ L_*\asymp X^{1/6}$ | $X^{1/4}$ | $X^{1/3+o(1)}$ |

Neither canonical Gram nor a global angular--radial (GAR) statement is an
entry in these menus. Either would require a proved block-local inverse
before it could own one of the two physical parents.

## 3. Proof or derivation

### 3.1 Reduction of the three block bounds

Because $t=\delta-\ell\ge1/4$, (119.B6) has exponent

\[
 a(\delta,\ell)=\delta-\ell=t.
\tag{R119.5}
\]

The two nonconstant exponents in (119.B7) are

\[
 b_1=\frac{1+\ell-\delta}{2}=\frac{1-t}{2},
 \qquad
 b_2=\frac{3\delta-1-\ell}{2}.
\]

Throughout (119.B1),

\[
 b_1-b_2=1-2\delta+\ell\ge0,
\]

and $b_1\ge1/4>0$. Thus neither the constant nor the third term increases
the exponent of the full second-derivative capacity: its exact leading
exponent is

\[
 b(\delta,\ell)=\frac{1-t}{2}.
\tag{R119.6}
\]

This uses the full displayed bound; the third term is not silently deleted.
The TTY exponent is $c(\delta,\ell)$, so (R119.1) follows.

For every $t\in[1/4,1/2]$,

\[
 \min\left\{t,\frac{1-t}{2}\right\}\le\frac13,
\tag{R119.7}
\]

with equality if and only if $t=1/3$. Adding the TTY entry to a minimum can
only decrease it. This proves the universal smooth-menu upper side
$m_{\rm sm}\le1/3$.

On the ridge $t=1/3$,

\[
 c\left(\delta,\delta-\frac13\right)
 =\frac{908\delta+178/3}{1282}.
\]

It is at least $1/3$ exactly when

\[
 2724\delta\ge1104,
 \qquad\text{i.e.}\qquad \delta\ge\frac{92}{227}.
\]

Every such ridge point is strictly below the terminal line, is not
$(1/2,0)$, and satisfies the strict residual TTY inequality. This proves
(R119.4) and the continuous smooth minimax $1/3$.

### 3.2 The two literal top witnesses and owner audit

Let $D_0(X)$ denote the literal scale of the unique profile whose support
contains $q_X=\lfloor\sqrt X\rfloor$, and let $D_1(X)$ be the first lower
adjacent literal profile. By the frozen physical partition,

\[
 D_0\asymp q_X,\qquad D_1\asymp q_X/2.
\]

For real $X\to\infty$, $q_X/\sqrt X=1+O(X^{-1/2})$. Consequently both
profile exponents equal $1/2+O(1/\log X)$; the factor $1/2$ in $D_1$
changes only that $O(1/\log X)$ term. For any literal frequency family
$L_*(X)\asymp X^{1/6}$, its exponent is $1/6+O(1/\log X)$. Hence both
physical labels approach $(1/2,1/6)$, and all strict residual conditions
hold for sufficiently large $X$.

At the limiting label,

\[
 \ell=\frac16<\frac12-\frac14,
 \qquad (\delta,\ell)\ne(1/2,0),
\]

and

\[
 178\ell+1638\delta=\frac{2546}{3}>463.
\tag{R119.8}
\]

Thus the terminal owner, the isolated full-second-derivative target point,
and the TTY wedge do not own either label. The unexpanded bottom and
`R5-Full` have already been removed before $\mathcal U_1$ by the frozen
owner lift; the two witnesses are stipulated middle/lower residual labels.

The capacities at either physical scale are literal up to fixed constants:

\[
 1+\frac{D_j}{L_*}\asymp X^{1/3},
\]

while the two oscillatory terms in (119.B7) have sizes

\[
 \sqrt{\frac{L_*X}{D_j}}\asymp X^{1/3},
 \qquad
 \frac{D_j^{3/2}}{\sqrt{L_*X}}\asymp X^{1/6}.
\tag{R119.9}
\]

The TTY exponent is exactly

\[
 c(1/2,1/6)=\frac{770}{1923}
 =\frac13+\frac{43}{641}>\frac13.
\tag{R119.10}
\]

Therefore the best of (119.B6)--(119.B8) is $X^{1/3+\varepsilon}$ at both
top physical labels. The strict gap in (R119.10) makes this conclusion
stable under their literal $O(1/\log X)$ exponent perturbations.

For the hard parent, the normalized cone capacity $L^2$ and target
$L^{3/2}$ are first multiplied by $F(L)=X^{1/4}L^{-3/2}$. Thus the cone
supplies the physical menu entry
$F(L)L^2=X^{1/4}L^{1/2}$, with exponent $1/4+\ell/2$. At the exact top
exponent $\delta=1/2$,

\[
 m_{\rm hard}(1/2,\ell)=
 \min\left\{\frac14+\frac{\ell}{2},\frac12-\ell,
 \frac14+\frac{\ell}{2},\frac{997+178\ell}{2564}\right\}.
\tag{R119.11}
\]

Already

\[
 \min\left\{\frac14+\frac{\ell}{2},\frac12-\ell\right\}\le\frac13,
\]

with equality only at $\ell=1/6$. At that point the other two entries are
$1/3$ and $770/1923>1/3$. Hence the hard minimax is also exactly $1/3$ at
exponent scale. If the literal hard scale is written as
$\delta_0=1/2+o(1)$, maximizing
$\min\{1/4+\ell/2,\delta_0-\ell\}$ gives
$1/6+\delta_0/3=1/3+o(1)$, and the literal witness gives the matching menu
value $1/3+o(1)$. The remaining two rows can only lower this maximum, and
at $(\delta,\ell)=(1/2,1/6)$ they equal $1/3$ and
$770/1923>1/3$, so they do not lower the contact.

Finally,

\[
 \frac{L_*^2}{L_*^{3/2}}
 =\frac{F(L_*)L_*^2}{F(L_*)L_*^{3/2}}
 =L_*^{1/2}\asymp X^{1/12},
 \qquad
 \frac{X^{1/3}}{X^{1/4}}=X^{1/12}.
\tag{R119.12}
\]

This is the exact separate hard/smooth deficit.

### 3.3 Why adjacent profiles do not telescope

For fixed $h$, adjoining the two literal denominator profiles gives only

\[
 \sum_d\chi_4(d)\bigl(w_{D_0}(d)+w_{D_1}(d)\bigr)e(hX/d).
\tag{R119.13}
\]

This is an aggregation identity, not a telescoping identity. A cancellation
would require a stated pointwise difference relation between the two
cutoffs (including their support-crossing and starred boundary terms), or a
proved inverse which recovers each physical block from a controlled
aggregate. Neither is among the hypotheses. The blind statement supplies no
definition from which an additional star-boundary cancellation could be
derived, so the literal convention is retained without inventing one.
Moreover, the hard and smooth profiles have different physical owners, so
an aggregate estimate would not by itself bound either component. Thus no
lawful adjacent-profile shrink is available from the accepted statement.

The two frequency signs are retained separately in this reasoning. No
$\operatorname{Re}B_h$ identification or cancellation between signs is
used; applying each capacity to each sign changes only a harmless fixed
factor.

## 4. First doubtful or unproved step

The first unproved step in every attempted closure visible from the blind
statement is a block-local cancellation statement at the literal critical
survivor. On the hard cone one would need, in normalized units,

\[
 T_{M1,L_*}\ll L_*^{3/2}X^\varepsilon
 \quad\text{instead of the coefficient-blind }L_*^2
\]

Equivalently, in physical units, this is

\[
 F(L_*)T_{M1,L_*}\ll X^{1/4+\varepsilon}
 \quad\text{instead of}\quad
 F(L_*)L_*^2=X^{1/4}L_*^{1/2}
\]

On the first smooth profile one would instead need

\[
 B_1(D_1,L_*;X)\ll X^{1/4+\varepsilon}
 \quad\text{instead of the direct-menu }X^{1/3+\varepsilon}
\]
Claiming that the adjacent profiles provide
this saving would first require an exact cutoff identity through the
support crossing and star convention; none is supplied. Claiming that
canonical Gram or GAR provides it would first require a block-local inverse
preserving the hard/smooth owner split; none is supplied. The missing amount
is $L_*^{1/2}=X^{1/12}$, not an endpoint constant.

## 5. Control tests and outcomes

These are algebraic controls; no numerical experiment was used.

| Required control | Exact input / expected invariant | Outcome | Implication |
|---|---|---|---|
| `literal_m1_block_and_profiles` | Use (119.B2) with its literal $h$- and $d$-blocks; suppress no scale-dependent factor. | **Pass.** All three bounds were compared on that same block. | The $1/3$ contact is not caused by changing the block definition. |
| `owner_priority_and_U1` | Remove bottom/`R5-Full`, terminal, $(1/2,0)$, then TTY wedge, in that order. | **Pass.** (R119.8) and $\ell=1/6<1/4$ put both witnesses in the strict residual set. | No accepted owner captures either critical label. |
| `hard_smooth_physical_split` | Keep the unique $q_X$-containing profile separate from every other profile. | **Pass.** $D_0$ is hard and the adjacent $D_1$ is smooth even though both have limiting exponent $\delta=1/2$. | Exponent labels alone cannot merge the two parents. |
| `frequency_first_capacity` | Evaluate $1+D/L$ without discarding $D/L$. | **Pass.** It is $\asymp X^{1/3}$ for both $D_0$ and $D_1$. | (119.B6) misses the target by $X^{1/12}$. |
| `full_second_derivative_capacity` | Retain both oscillatory terms in (119.B7). | **Pass.** They are $X^{1/3}$ and $X^{1/6}$; globally $b_1-b_2=1-2\delta+\ell\ge0$. | The full bound, not a truncated surrogate, has leading exponent $1/3$. |
| `TTY_exponent_and_hypotheses` | Apply only the audited (119.B8) under (119.B1)--(119.B2). | **Pass relative to the frozen statement.** Its critical exponent is $770/1923>1/3$, and its owner inequality fails as in (R119.8). No unlisted endpoint extension is used. | TTY neither owns nor shrinks the witnesses. |
| `critical_hard_label` | $D_0\asymp\lfloor\sqrt X\rfloor,\ L_*\asymp X^{1/6}$. | **Pass.** The physical cone row $X^{1/4}L_*^{1/2}$, (119.B6), and leading (119.B7) all contact at $X^{1/3+o(1)}$. | The hard menu has a literal asymptotic witness. |
| `critical_first_smooth_label` | $D_1\asymp\lfloor\sqrt X\rfloor/2,\ L_*\asymp X^{1/6}$. | **Pass.** Its direct menu is $X^{1/3+o(1)}$. | The first smooth profile is already a smooth-parent witness. |
| `floor_star_support_and_real_X` | Keep $q_X=\lfloor\sqrt X\rfloor$ for arbitrary real $X$, with the stipulated unique-profile and star/support convention. | **Pass at the stated exponent interface.** The floor gives a relative $1+O(X^{-1/2})$ change, and the literal convention leaves exactly one hard profile. No undefined star identity is used. | Floors and crossings do not supply an exponent saving or blur ownership; a stronger boundary claim would need its missing definition. |
| `hard_cone_physical_normalization` | Convert the normalized capacity $L^2$ and target $L^{3/2}$ by the common factor $F(L)=X^{1/4}L^{-3/2}$, without reusing the visible $1/h$ a second time. | **Pass.** The physical rows are $X^{1/4}L^{1/2}$ and $X^{1/4}$; their ratio remains $L^{1/2}=X^{1/12}$ at $L_*$. | The hard menu is compared in physical $B_1$ units and the normalization is consistent. |
| `adjacent_profile_telescope` | Add the two literal $d$-profiles and inspect support-crossing/star terms. | **Fails as a shrink mechanism.** Only (R119.13) follows; no difference identity or block-local inverse is given. | Adjacent aggregation cannot close either parent. |
| `menu_optimality_vs_lower_bound` | Distinguish the minimum exponent among listed bounds from the size of the actual signed sum. | **Pass.** The proof asserts only that no listed menu entry beats $1/3$ at the witnesses. | No arithmetic $\Omega(X^{1/3})$ claim is made. |
| `canonical_Gram_and_GAR_nonimplication` | Treat canonical Gram and GAR as alternative whole routes unless a block-local inverse is proved. | **Pass.** No such inverse is a hypothesis. | Neither alternative is promoted to a hard or smooth blockwise owner. |
| `downstream_scope` | Ask what the minimax calculation alone establishes. | **Pass.** It establishes a direct-menu obstruction for the two M9-M1 parents only. | It does not prove either parent, M9, or the Gauss-circle target. |

The signed coefficient structure is never used to claim cancellation here.
Accordingly, the calculation intentionally survives absolute-value,
random-sign, and adversarial-coefficient controls: it is a capacity/no-go
calculation, not a proposed signed proof.

## 6. Dependencies and exact artifacts used

Mathematical inputs were restricted to:

1. `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/blind_statement.md`;
2. `problems/gauss_circle.md`;
3. `state/control_models.md`.

Workflow and output constraints came from `protocol.md` and
`rounds/codex-managed/m9-m1-direct-parent-minimax-gate/briefs/blind_m1_parent_minimax_rederivation.md`.
No proof-state file, strategy file, historical Round-91/Round-98 artifact,
Round-119 nonblind artifact, derivation packet, conductor candidate, sibling
report, web source, or computation was read or used.

## 7. Recommended state effect

**Retain.** Retain both hard and smooth M9-M1 physical parents as open and
record the quantitative no-go: the accepted direct menu has separate
asymptotic minimax $X^{1/3}$ at the literal families $(D_0,L_*)$ and
$(D_1,L_*)$, against target $X^{1/4}$, with a missing
$X^{1/12}=L_*^{1/2}$ saving. Do not promote an adjacent-profile telescope,
canonical Gram, or GAR owner without the exact block-local identity/inverse
identified in Section 4. This report is candidate evidence only and does
not authorize a shared-state change.
