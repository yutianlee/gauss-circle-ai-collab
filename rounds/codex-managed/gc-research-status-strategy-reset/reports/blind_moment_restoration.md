# Round230 — blind moment restoration

## 1. Result: lemma and scoped no-go result

- Campaign: `gc-research-status-strategy-reset`.
- Round: `230`.
- Generated UTC: 2026-10-11T02:14:13.9805367Z.
- Task and role: `blind_moment_restoration`, statement-only independent rederiver.
- Graph hash supplied by the brief, not independently inspected: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
- Status: candidate evidence only. No graph, proof draft, validation matrix, or synthesis was read or changed.
- Effort: analytical; no numerical experiment or external source was used.

For a nondecreasing counting function with discrepancy `P(x)=N(x)-cx=o(x)`, an absolute moment on an enlarged interval gives the uniform pointwise exponent

\[
\boxed{\sup_{Y\le x\le2Y}|P(x)|\ll_{p,\varepsilon}
Y^{a_p/(p+1)+\varepsilon}.}
\]

With the stated radial restoration formula and an **unnormalized absolute radial moment** of exponent `b_p`, the sharper restoration is

\[
\boxed{\sup_{Y\le x\le2Y}|P(x)|
\ll_{p,\varepsilon}Y^{q_p+\varepsilon},\qquad
q_p=\max\left(\frac14,\frac{p/4+1/2+b_p/2}{p+1}\right).}
\]

The uniform remainder is handled by a height threshold before integrating. This avoids charging its size across the whole interval. For every specified example, `b_p>=1`, so the formula simplifies to

\[
q_p=\frac14+\frac{2b_p+1}{4(p+1)}.
\]

For the specified `theta` and `beta=2theta-1/2`:

1. `b_p=max(1,(p-2)beta)` gives `q_p>theta` at every finite order. Its infimum over unbounded fixed orders is exactly `theta`; it cannot certify a strict improvement through this restoration. An explicit abstract counting-function model below shows that even the complete hypotheses with this moment envelope do not imply the conjectural exponent.
2. `p=12`, `b_12=29/25` gives `q_12=102/325<theta`, a strict conditional improvement, but not the conjectural exponent.
3. An unbounded family of fixed even orders with `b_p<=5/4`, together with the complete uniform restoration hypotheses, implies `P(x)<<_epsilon x^(1/4+epsilon)`. The certificate is `q_p<=1/4+7/[8(p+1)]`. If this bound is available at every even order, the first even order whose displayed certificate improves the specified `theta` is `14`.

None of the unproved moment assertions, considered without its remaining hypotheses, is by itself a proof for the actual circle discrepancy.

## 2. Exact statements and hypotheses

### 2.1 One-sided persistence and the `x`-moment lemma

Let `c>0`, let `N:(0,infinity)->R` be nondecreasing, and set `P(x)=N(x)-cx`. Integer values, continuity, and a convention for the value at a jump are not needed for the lemma. Assume `|P(x)|=o(x)` as `x->infinity`.

For a fixed real `p>=2`, assume, for every `eta>0`,

\[
\int_{Y/2}^{3Y}|P(t)|^p\,dt
\le C_{p,\eta}Y^{a_p+\eta}
\]

for all sufficiently large `Y`, with constants independent of `Y` and the evaluation point. Then the bound in Section 1 holds uniformly for every real `x` in `[Y,2Y]`.

More precisely, for all sufficiently large `Y`, independently of `p`,

\[
|P(x)|^{p+1}\le c(p+1)\int_{Y/2}^{3Y}|P(t)|^p\,dt
\qquad(Y\le x\le2Y).
\]

For a set `S` of available fixed orders, the exact admission criterion supplied by these moment estimates and this lemma is

\[
\inf_{p\in S}\frac{a_p}{p+1}\le\frac14.
\]

In particular, an unbounded sequence with `liminf a_p/(p+1)<=1/4` suffices. The condition `a_p=p/4+o(p)` along such a sequence is a convenient sufficient form. A single sufficiently strong fixed order can also suffice; an unbounded sequence is not intrinsically necessary.

### 2.2 Radial moment normalization and completeness

Put `T=sqrt(Y)` and use a fixed radial window `J_T` containing

\[
[T/\sqrt2,\sqrt3T].
\]

Its endpoints are fixed positive multiples of `T`. The notation `M_p` was undefined in the isolated statement. The conductor subsequently clarified only this notation: it is the unnormalized integral on such a fixed radial window. Accordingly the exact hypothesis used here is

\[
M_p(B_T):=\int_{J_T}|B_T(R)|^p\,dR
\le C_{p,\eta}T^{b_p+\eta}
\quad\text{for every fixed }p\in S\text{ and every }\eta>0.
\]

The restoration hypothesis means, for every `delta>0`,

\[
P(R^2)=\frac{\sqrt R}{\pi}B_T(R)+E_T(R),\qquad
\sup_{R\in J_T}|E_T(R)|\le C_\delta T^{1/2+\delta}.
\]

It must hold for every real `R` in the window. The moment and restoration must concern the same complete `B_T`, the same scale, and all components needed for the actual discrepancy. Bounds for a selected component or signed powers do not imply this hypothesis.

Real-valued `B_T` is sufficient. Complex-valued `B_T` is also permissible with an absolute moment and the displayed modulus-bounded identity; alternatively, a formula with `Re B_T` is sufficient because `|Re B_T|<=|B_T|`. An even algebraic power of a complex quantity is not an absolute moment.

For clarity about normalization, if instead `M_p=T^(-1) integral |B_T|^p dR`, the unnormalized exponent is `b_p+1`, and the restored exponent becomes

\[
\max\left(\frac14,\frac{p/4+1+b_p/2}{p+1}\right)
=\frac14+\max\left(0,\frac{2b_p+3}{4(p+1)}\right).
\]

The numerical exponents asserted in this report use the clarified unnormalized convention only.

## 3. Proof and exact comparisons

### 3.1 One-sided persistence pays both signs and every jump

Fix `x in [Y,2Y]` and write `H=|P(x)|`. If `P(x)=H>0`, monotonicity gives, for `s>=0`,

\[
P(x+s)\ge H-cs.
\]

If `P(x)=-H<0`, monotonicity gives, for `s>=0` with `x-s>0`,

\[
P(x-s)\le-H+cs.
\]

Thus a positive excursion persists to the right and a negative excursion to the left. The argument never assumes persistence on both sides. These inequalities include the prescribed value at a jump and hold regardless of one-sided continuity.

The `o(x)` assumption implies uniformly on `[Y,2Y]` that `H/c<=Y/2` for all sufficiently large `Y`. Hence the relevant interval of length `H/c` lies inside `[Y/2,3Y]`. Integrating the appropriate lower bound for the absolute value gives

\[
\int_{Y/2}^{3Y}|P(t)|^p\,dt
\ge\int_0^{H/c}(H-cs)^p\,ds
=\frac{H^{p+1}}{c(p+1)}.
\]

For `H=0` the conclusion is immediate. Taking the `(p+1)`st root proves the exact inequality and the pointwise exponent. To obtain a final slack `epsilon`, use the moment with `eta=(p+1)epsilon`.

The conclusion is uniform over the full continuum of evaluation points: no discretization or union bound has been used. Taking `Y=x`, or using overlapping dyadic windows, gives the same asymptotic bound for all real `x`.

### 3.2 Fixed-order quantifiers

Let `r_p=a_p/(p+1)`. If `inf_{p in S} r_p<=1/4`, then for a prescribed final `epsilon>0` choose one available order `p=p(epsilon)` with `r_p<1/4+epsilon/2`. Apply its moment bound with `eta=(p+1)epsilon/2`. The resulting bound is `O_epsilon(Y^(1/4+epsilon))`.

The chosen `p` depends on the desired exponent slack, never on `Y`. Its moment constant and its threshold for sufficiently large `Y` may depend on `epsilon`; this is legitimate. No uniformity of moment constants as `p->infinity` is needed. If the infimum of the displayed certificates is strictly greater than `1/4`, those certificates do not supply the target. This last statement is a limitation of the supplied certificates, not a lower bound for a particular arithmetic discrepancy.

### 3.3 Jacobian and uniform remainder

First, the direct global-moment calculation provides a useful normalization check. Since `x=R^2` and `dx=2R dR`,

\[
\int_{Y/2}^{3Y}|P(x)|^p\,dx
\ll_p T^{1+p/2}M_p(B_T)+T^{2+p/2+p\delta}.
\]

The two powers of `T` in the second term are the Jacobian factor and the radial interval length. Using a sufficiently small moment slack and remainder slack therefore permits

\[
a_p=\frac p4+\frac12+\frac{\max(b_p,1)}2.
\]

This is valid, but unnecessarily weak when `b_p<1`. To obtain the sharper result, let `E_* = C_delta T^(1/2+delta)`. If `H=|P(x)|<=4E_*`, the error term itself controls the point. Otherwise use the one-sided interval of length `H/(2c)`, on which `|P(t)|>=H/2`. There,

\[
\left|\frac{\sqrt R}{\pi}B_T(R)\right|
\ge |P(R^2)|-|E_T(R)|\ge H/4.
\]

Throughout this interval `R` is comparable to `T`, so `|B_T(R)|>>H/T^(1/2)`. Moreover,

\[
dR=\frac{dt}{2\sqrt t}\asymp\frac{dt}{T}.
\]

The radial length is consequently bounded below by a fixed positive constant times `H/T`, and

\[
M_p(B_T)\gg_p\frac{H^{p+1}}{T^{1+p/2}}.
\]

The high-excursion case gives

\[
H\ll_{p,\eta}T^{(1+p/2+b_p+\eta)/(p+1)}.
\]

Combining both cases,

\[
H\ll_{p,\delta,\eta}
T^{1/2+\delta}
+T^{(1+p/2+b_p+\eta)/(p+1)}.
\]

Since `Y=T^2`, choose `delta<=2epsilon` and `eta<=2(p+1)epsilon` to obtain exactly `q_p+epsilon`. This proves the sharper formula. Any smoothing or truncation procedure behind the supplied formula is used only through its explicitly uniform error bound. An averaged error or an error excluding exceptional radii would not suffice for this proof.

### 3.4 General admission gate for improving `theta`

Let `1/4<theta<1/3` and `beta=2theta-1/2`, so `0<beta<1/6`. Because the error exponent `1/4` is already smaller than `theta`, a fixed-order certificate strictly improves `theta` precisely when

\[
\frac{p/4+1/2+b_p/2}{p+1}<\theta,
\quad\text{equivalently}\quad
\boxed{b_p<(p+1)\beta-\frac12.}
\]

Strictness matters: equality supplies `theta+epsilon`, not a smaller exponent. More quantitatively, to certify `theta-kappa` with `theta-kappa>1/4`, it suffices that

\[
b_p\le(p+1)\beta-\frac12-2(p+1)\kappa.
\]

For an unbounded fixed-order family, the exact criterion furnished by the sharper radial certificates is that their infimum be `1/4`. In particular `liminf b_p/p<=0`, and especially `b_p=o(p)`, is sufficient. A fixed order with `b_p<=-1/2` is another sufficient possibility. The latter observations describe the formal interface; no such moment estimate is asserted here for the actual arithmetic object.

### 3.5 Exact bounds on the specified algebraic constants

Set `s=sqrt(1717)`. Then

\[
41<s<42,\qquad s>207/5,
\]

because `41^2<1717<42^2` and `207^2=42849<42925=25*1717`. Also

\[
\beta=\frac{50s-297}{13762}.
\]

These rational comparisons imply

\[
\boxed{\frac18<\beta<\frac2{15}<\frac16.}
\]

Indeed the lower comparison follows from `8*1753=14024>13762`; the upper comparison follows from `15*1803=27045<27524=2*13762`. They also verify `1/4<theta<1/3` without decimal approximation.

### 3.6 Envelope `b_p=max(1,(p-2)beta)`

Here

\[
q_p-\theta
=\frac{2\max(1,(p-2)\beta)+1-2\beta(p+1)}{4(p+1)}
\ge\frac{1-6\beta}{4(p+1)}>0.
\]

Thus no finite available order meets the strict admission gate. For `p>=2+1/beta`, the exact identity is

\[
q_p=\theta+\frac{1-6\beta}{4(p+1)}.
\]

For `2<=p<=2+1/beta`, it is `q_p=1/4+3/[4(p+1)]`. Both branches decrease with `p`, agree at the junction, and the second tends to `theta` from above. Therefore the infimum over an unbounded family is `theta`. Choosing a large fixed order for each final slack recovers `theta+epsilon`, but does not improve the exponent.

There is also an abstract countermodel to inferring the conjecture from this entire envelope, even with an exact complete restoration formula. Take `c=1`, `x_k=100^k`, and `h_k=floor(x_k^theta)`. Define the integer-valued nondecreasing function

\[
N(x)=
\begin{cases}
x_k+h_k,&x_k\le x\le x_k+h_k\text{ for some }k,\\
\lfloor x\rfloor,&\text{otherwise}.
\end{cases}
\]

The intervals are disjoint. On them `P(x)=h_k-(x-x_k)`, while elsewhere `-1<P(x)<=0`; consequently `P=o(x)` and `P(x_k)=h_k`. Define `B_T(R)=pi P(R^2)/sqrt(R)` on each fixed radial window, with zero remainder. A window with endpoints fixed multiples of `T` meets at most a fixed number of the geometrically separated spike intervals. The baseline contributes `O_p(T^(1-p/2))`; a spike contributes

\[
O_p\left(T^{-1-p/2}h_k^{p+1}\right)
=O_p\left(T^{\beta(p+1)-1/2}\right).
\]

Since

\[
\beta(p+1)-\frac12<(p-2)\beta\le b_p
\]

by `3beta<1/2`, and `1-p/2<=0<b_p`, all the prescribed radial moments hold for every fixed `p>=2`. Nevertheless the conjectural bound fails for any final slack less than `theta-1/4`. This is a countermodel in the stated class of counting functions, not a lower-bound result about the lattice-point counting function.

### 3.7 Order twelve with `b_12=29/25`

The restored certificate is exactly

\[
q_{12}=\frac14+\frac{2(29/25)+1}{52}
=\frac14+\frac{83}{1300}=\boxed{\frac{102}{325}}.
\]

For a rational proof of strict improvement,

\[
\theta>\frac{3292+25(207/5)}{13762}
=\frac{4327}{13762}>\frac{102}{325},
\]

where the final cross-product difference is

\[
4327\cdot325-102\cdot13762=2551>0.
\]

This exponent is strictly greater than `1/4`; hence it does not reach the conjecture. The preceding integer counting-function construction with spike exponent `q=102/325` makes its order-twelve radial spike exponent exactly `29/25`. It therefore also proves the insufficiency of this single moment, even with exact restoration, to imply the conjectural exponent in the abstract class.

### 3.8 Unbounded even orders with `b_p<=5/4`

For every available even order,

\[
q_p\le\frac14+\frac7{8(p+1)}.
\]

The displayed certificate improves the specified `theta` whenever

\[
p+1>\frac7{4\beta}.
\]

At `p=12`, the certificate is `33/104`, and it exceeds `theta` because `beta<2/15<7/52`. At `p=14`, the certificate is `37/120`, and it is below `theta` because `beta>1/8>7/60`. The certificate decreases with `p`; hence order fourteen is the first improving even order when the family is available at every even order. If only an unbounded subset of even orders is assumed, an available sufficiently large member works; availability at order fourteen is not inferred.

For any prescribed `epsilon>0`, choose a single available even `p` with `p+1>=7/(4epsilon)`. This places the displayed gain above `1/4` at most `epsilon/2`. Use the restoration with final slack `epsilon/2`. Its moment and remainder slack choices are fixed after `p` is fixed. The conclusion is

\[
P(x)\ll_\varepsilon x^{1/4+\varepsilon}
\]

for all real sufficiently large `x`. This is a complete conditional implication under Section 2, not a proof that the requisite moments hold.

## 4. First doubtful or unproved step

There is no unproved analytic step in the persistence or restoration implication under the explicit hypotheses of Section 2. The initial notation gap in `M_p` was resolved by the conductor's normalization-only clarification and remains explicitly recorded.

The first unproved step in applying the result to the actual circle problem is obtaining the asserted **complete** absolute moments for the actual restored quantity, with the required uniform expansion on the enlarged real window. This report has neither read nor proved those arithmetic inputs. In particular, it does not establish `b_12=29/25`, the unbounded family `b_p<=5/4`, or the applicability of any external theorem.

Without the restoration identity, take `B_T=0`: all its moments vanish while `P` can still be the nonconjectural spike model. Without a complete moment bound, an omitted component can carry that entire discrepancy. Thus these are substantive hypotheses, not bookkeeping conditions.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `graph_vs_evidence` | PASS within assigned scope. No graph was read or changed; all conclusions are candidate implications or abstract countermodels. The supplied graph hash is provenance only. |
| `complete_bound_vs_component` | PASS. Section 2 requires the same complete restored quantity. No component estimate was substituted for its absolute moment. |
| `current_primary_versions` | NOT EVALUATED by design. Statement-only isolation forbids literature access; no current-literature claim is made. |
| `exact_source_hypotheses` | NOT APPLICABLE to an imported theorem: none was used. All locally used hypotheses and normalization conventions are explicit. |
| `full_restoration` | PASS as a conditional lemma. Both signs, jumps, the enlarged interval, every real evaluation point, `dx=2R dR`, radial support width, and the uniform remainder are paid explicitly. |
| `fixed_order_quantifiers` | PASS. Each selected `p` depends only on the requested final exponent slack. No order depends on `Y` or `T`; no uniform-in-order moment constant is assumed. |
| `real_complex_scope` | PASS. Absolute moments suffice for real or complex quantities. Complex algebraic even moments are not substituted for modulus moments. A real-part restoration is covered explicitly. |
| `all_owners_preserved` | PASS as an interface safeguard. Every component must already be included in the complete `B_T` or in the uniformly bounded error. Arithmetic ownership assignments were not accessible and are not certified here. |
| `certificate_not_lower_bound` | PASS. Failure of an exponent certificate is not called a lower bound for the actual circle discrepancy. The two no-go examples are explicitly abstract integer counting-function countermodels. |
| `blind_independence` | PASS. Only the three permitted files were read. The incoming conductor clarification supplied only the normalization of `M_p`; no derivation, historical result, source, sibling report, or root control was accessed. |

Additional analytical controls: a positive spike persists to the right; a negative spike persists to the left; an arbitrary upward jump satisfies the same inequalities; the spike countermodels saturate the `p+1` height/width relationship. All constant and exponent comparisons were exact rational algebra. No computational result is being used to certify an asymptotic theorem.

## 6. Dependencies and exact artifacts used

Files read, and only these files:

1. `protocol.md`.
2. `rounds/codex-managed/gc-research-status-strategy-reset/briefs/blind_moment_restoration.md`.
3. `rounds/codex-managed/gc-research-status-strategy-reset/briefs/blind_moment_statement.md`.

Additional permitted communication: the conductor's normalization-only clarification that `M_p` is an unnormalized radial integral over a fixed window covering `[sqrt(Y/2),sqrt(3Y)]`.

Mathematical dependencies are only monotonicity, `P=o(x)`, elementary integration, the explicitly assumed complete moments and restoration identity, and exact rational comparisons with `sqrt(1717)`. No external theorem or source is relied on. No state file, research-history file, sibling artifact, or root control was opened.

Sole written artifact: this report. Its final SHA-256 is delivered separately after writing, to avoid a self-referential embedded hash. The tool-call record supplies the generation time; the brief's context timestamp is `2026-10-11T02:09:43.812207+00:00`.

## 7. Recommended state effect

**Retain** the complete moment-restoration lemma and the exact fixed-order admission gate as candidate evidence for conductor review. They are independently derived and establish a usable conditional interface.

**Reject** any inference that the envelope `max(1,(p-2)beta)` strictly improves the specified `theta` through these certificates, or that the order-twelve estimate alone proves the conjecture. The abstract countermodels establish the latter insufficiencies even when restoration is exact.

**Retain conditionally** the implications `b_12<=29/25 => 102/325+epsilon` and an unbounded fixed-even-order family `b_p<=5/4 => 1/4+epsilon`, with all of Section 2 attached. Do not promote either arithmetic moment hypothesis, the actual circle conjecture, or a literature-status claim on this report's authority.

No authoritative state change is made or requested automatically. The conductor owns the seam assessment and any mechanically valid State Patch. This task ends after the report hash; no successor round is designed.
