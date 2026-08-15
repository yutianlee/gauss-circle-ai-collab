# Lower radial phase diagram attack

- Campaign: m9-m1-lower-radial-phase-diagram
- Round: 61
- Task: lower_radial_phase_diagram_attack
- Role: discovery
- Status: candidate evidence only; no shared state was edited
- Method allocation: entirely analytic; no numerical experiment or new source

## 1. Result

Let

\[
 R=X^{1/4},\qquad N=X^\nu,\qquad D=X^\delta,
\qquad 0\leq\nu\leq\frac12,\quad
\frac14\leq\delta\leq\frac12.
\]

For a fixed smooth block \(n\asymp N\), the exact stationary relation
\[
 n=\frac{4Xh^2}{d^2}
\]
places the frequency at
\[
 L\asymp\frac{D\sqrt N}{2\sqrt X},\qquad
 \boxed{\ell=\delta+\frac{\nu-1}{2}.}
\tag{1.1}
\]
The active spatial scales are exactly, at exponent precision,
\[
 \boxed{\frac{1-\nu}{2}\leq\delta\leq\frac12.}
\tag{1.2}
\]

On this radial slice, the accepted TTY wedge is
\[
 \boxed{1816\delta+89\nu\leq552,}
\tag{1.3}
\]
the terminal line is \(\nu=1/2\), and the V2 target point is
\((\delta,\nu)=(1/2,0)\).  Put
\[
 \delta_0(\nu)=\frac{1-\nu}{2},\qquad
 \delta_T(\nu)=\frac{552-89\nu}{1816}.
\tag{1.4}
\]
Then TTY meets the active slice if and only if
\[
 \nu\geq\nu_*:=\frac{356}{819}.
\tag{1.5}
\]
For \(\nu_*\leq\nu<1/2\), it closes only
\[
 \delta_0(\nu)\leq\delta\leq\delta_T(\nu),
\tag{1.6}
\]
leaving \(\delta_T(\nu)<\delta\leq1/2\).  For
\(0<\nu<\nu_*\), every active scale survives.  Therefore the union of
the accepted direct inputs closes an entire radial sector only at
\[
 \boxed{\nu=0\quad\hbox{and}\quad\nu=\frac12.}
\tag{1.7}
\]
At \(\nu=0\), only the hard top scale occurs and V2 closes it; at
\(\nu=1/2\), Round 60 closes the fixed smooth critical sector.  There is
no positive interval below \(1/2\) that is closed at all spatial scales.
The first uncovered radial band is thus every
\[
 \boxed{0<\nu<\frac12,}
\tag{1.8}
\]
with the completely uncovered subband \(0<\nu<356/819\).

This is an exact phase-diagram theorem and no-go for an all-scale closure
from the accepted menu.  It supplies no new cancellation estimate.

## 2. Exact statement and hypotheses

Fix a real \(V\in C_c^\infty((a,b))\), \(0<a<b<\infty\), and localize
\(n\) by \(V(n/N)\).  Fix one accepted active denominator profile
\(w_j\) at \(d\asymp D_j\), where
\[
 D_j=X^{\delta+o(1)},\qquad
 H_j=\left\lfloor\frac{D_j}{R}\right\rfloor.
\tag{2.1}
\]
At a stationary incidence \(n=hq\), \(q\) positive and odd,
\[
 d_*=2\sqrt{\frac{hX}{q}},
\qquad
 n=\frac{4Xh^2}{d_*^2}.
\tag{2.2}
\]
Since \(n\asymp N\) and \(d_*\asymp D_j\), there are constants depending
only on \(V\) and the fixed profile support such that
\[
 c_V\frac{D_j\sqrt N}{\sqrt X}
 \leq h\leq
 C_V\frac{D_j\sqrt N}{\sqrt X}.
\tag{2.3}
\]
The factor \(1/2\) in the reference scale affects no exponent:
\[
 L=\frac{D_j\sqrt N}{2\sqrt X},\qquad
 \ell=\delta+\frac{\nu-1}{2}.
\tag{2.4}
\]

The accepted Vaaler support is \(1\leq h\leq H_j\).  Its lower inequality
requires \(L\gg1\), hence
\[
 \delta\geq\delta_0(\nu)=\frac{1-\nu}{2}
\tag{2.5}
\]
at exponent level.  The upper inequality \(L\ll H_j\) is
\[
 \frac{L}{H_j}\asymp X^{\nu/2-1/4}\leq1,
\tag{2.6}
\]
equivalent to \(\nu\leq1/2\).  Together with
\(1/4\leq\delta\leq1/2\), (2.5) yields (1.2).

At the boundary \(\delta=\delta_0(\nu)\), \(L\asymp1\), so an ordinary
dyadic exponent block must be replaced by a bounded set of exact
frequencies.  When simultaneously \(\nu=1/2,\delta=1/4\),
\(H_j=O(1)\) as well.  These are floor layers, not open exponent regions.
They inherit the accepted direct small-height treatment.  For
\(\delta>\delta_0(\nu)\), both \(L\) and \(H_j\) tend to infinity and the
exponent diagram is literal.

The physical target for the radially localized reciprocal antecedent is
\[
 \boxed{B_{D,N,V}(X)\ll_{\varepsilon,V}R X^\varepsilon
 =X^{1/4+\varepsilon}.}
\tag{2.7}
\]
After the accepted positive-frequency transform, the common external
factor is exactly \(R\); consequently (2.7) is equivalent to an
\(O(X^\varepsilon)\) normalized radial GAR contribution.  No additional
power of \(N\) may be inserted into the target.

## 3. Proof or derivation

### 3.1 Translation of the accepted regions

Substituting (2.4) into the formal M1 triangle gives
\[
 0\leq\ell
 \Longleftrightarrow
 \delta\geq\frac{1-\nu}{2},
\qquad
 \ell\leq\delta-\frac14
 \Longleftrightarrow
 \nu\leq\frac12.
\tag{3.1}
\]
This proves (1.2).

The terminal condition is
\[
 \ell=\delta-\frac14.
\]
Using (2.4), this is
\[
 \delta+\frac{\nu-1}{2}=\delta-\frac14
 \Longleftrightarrow
 \boxed{\nu=\frac12.}
\tag{3.2}
\]
Thus the terminal theorem closes no fixed lower exponent
\(\nu<1/2\); Round 60 owns the critical endpoint in its stronger smooth
all-scale form.

The TTY target
\[
 178\ell+1638\delta\leq463
\]
becomes
\[
 178\left(\delta+\frac{\nu-1}{2}\right)+1638\delta
 \leq463,
\]
or
\[
 \boxed{1816\delta+89\nu\leq552.}
\tag{3.3}
\]
Thus TTY closes \(\delta\leq\delta_T(\nu)\).  It meets the active interval
exactly when
\[
 \delta_0(\nu)\leq\delta_T(\nu)
 \Longleftrightarrow
 908(1-\nu)\leq552-89\nu
 \Longleftrightarrow
 819\nu\geq356.
\tag{3.4}
\]
Equality gives the exact rational threshold \(356/819\).

The V2 target point
\[
 (\delta,\ell)=\left(\frac12,0\right)
\]
maps through (2.4) to
\[
 \boxed{(\delta,\nu)=\left(\frac12,0\right).}
\tag{3.5}
\]
It closes the degenerate radial endpoint \(\nu=0\) because (1.2) then
contains only \(\delta=1/2\).

Finally, the exact residual corridor becomes
\[
 \boxed{
 \mathcal U_{\rm rad}=
 \left\{(\delta,\nu):
 0\leq\nu<\frac12,\quad
 \frac{1-\nu}{2}\leq\delta\leq\frac12,\quad
 1816\delta+89\nu>552
 \right\}
 \setminus\left\{\left(\frac12,0\right)\right\}.}
\tag{3.6}
\]
For \(0<\nu<356/819\), (3.4) fails, so the whole active interval lies in
\(\mathcal U_{\rm rad}\).  At \(\nu=356/819\), TTY closes only the
bounded-frequency boundary point \(\delta=\delta_0=\delta_T\).
Above it, TTY closes the prefix (1.6), while the top interval survives.
In particular, at \(\delta=1/2\),
\[
 1816\delta+89\nu=908+89\nu>552,
\tag{3.7}
\]
so no lower radial slice \(0<\nu<1/2\) is fully covered.

### 3.2 Exact deficit of the accepted menu

The terminal frequency-first estimate is
\[
 B_{D,N,V}\ll X^\varepsilon(1+D/L).
\]
Since
\[
 \frac DL\asymp X^{(1-\nu)/2},
\]
its exponent exceeds \(1/4\) by
\[
 \boxed{\sigma_{\rm term}(\nu)=\frac{1-2\nu}{4}.}
\tag{3.8}
\]

The TTY exponent after substitution is
\[
 \frac{89(1+\ell)+819\delta}{1282}
 =\frac{89(1+\nu)}{2564}
  +\frac{908\delta}{1282}.
\]
Its excess over \(1/4\) is
\[
 \boxed{\sigma_{\rm TTY}(\delta,\nu)
 =\frac{1816\delta+89\nu-552}{2564}.}
\tag{3.9}
\]

The accepted V2/B-process estimate is
\[
 B_{D,N,V}\ll_\varepsilon
 X^\varepsilon\min\left(D,\sqrt{\frac{LX}{D}}\right).
\tag{3.10}
\]
Its two exponents are
\[
 \delta,\qquad
 \frac{1+\ell-\delta}{2}=\frac{1+\nu}{4}.
\]
Therefore its excess over \(1/4\) is
\[
 \boxed{\sigma_{\rm V2}(\delta,\nu)
 =\min\left(\delta-\frac14,\frac{\nu}{4}\right).}
\tag{3.11}
\]
It reaches the target only on the active endpoints \(\nu=0\) or
\(\delta=1/4\); the latter occurs only at \(\nu=1/2\).

On a survivor \((\delta,\nu)\in\mathcal U_{\rm rad}\), all three deficits
are positive.  The exact saving required over the best accepted direct
menu is
\[
 \boxed{
 \sigma_*(\delta,\nu)=
 \min\left\{
 \frac{1-2\nu}{4},\
 \frac{1816\delta+89\nu-552}{2564},\
 \delta-\frac14,\
 \frac{\nu}{4}
 \right\}.}
\tag{3.12}
\]
Equivalently, it suffices to improve whichever accepted estimate realizes
the minimum by \(X^{\sigma_*(\delta,\nu)}\), up to \(X^\varepsilon\), to
reach (2.7).

At the hard top \(\delta=1/2\), TTY is never competitive with the two
elementary deficits.  Indeed its numerator is \(356+89\nu\), whereas
\[
 \frac{\sigma_{\rm TTY}(1/2,\nu)}{1}
 >\min\left(\frac{\nu}{4},\frac{1-2\nu}{4}\right)
\quad(0<\nu<1/2).
\]
Thus the exact top survivor requires
\[
 \boxed{
 \sigma_{\rm top}(\nu)=
 \min\left\{\frac{\nu}{4},\frac{1-2\nu}{4}\right\}.}
\tag{3.13}
\]
The two bounds cross at \(\nu=1/3\).  Hence V2 is best for
\(0<\nu\leq1/3\), while the terminal estimate is best for
\(1/3\leq\nu<1/2\).

### 3.3 Scale sum, floors, and transform ledger

For a fixed \(V(n/N)\), (2.3) gives one constant-relative-width frequency
block per spatial scale.  Mellin separation writes
\[
 V\!\left(\frac{4Xh^2}{d^2N}\right)
 =\frac1{2\pi}\int_{\mathbb R}\widehat V(t)
 \left(\frac{4X}{N}\right)^{it}h^{2it}d^{-2it}\,dt.
\tag{3.14}
\]
The frequency BV norm acquires only \(1+|t|\), the denominator mode is
bounded, and its transform derivatives have fixed polynomial
\(|t|\)-loss.  Schwartz decay of \(\widehat V\) absorbs all such losses.
Thus the terminal, TTY, and V2 bounds transfer to the radial block without
changing any exponent.

There are \(O(\log X)\) active \(D_j\)-scales, absorbed by
\(X^\varepsilon\).  This summation proves a radial sector only if every
contributing scale is target-sized; existence of the TTY prefix alone is
not enough.  The exact floors \(H_j=\lfloor D_j/R\rfloor\), the
one-sided top, the full hard sample, profile overlaps, and stationary
stars remain inside the accepted transforms.  Smooth localization changes
the remainder constants only by seminorms of \(V\); the accepted
Vaaler-weighted transform errors remain polylogarithmic and hence
target-safe.  The bounded-\(L\) boundary is handled by finitely many exact
frequencies, and the bounded-\(H_j\) corner by direct summation.

## 4. First doubtful or unproved step

There is no unproved algebraic step in (1.1)--(3.13), conditional on the
accepted terminal, TTY, V2, and transform interfaces.  The first unproved
step is an actual cancellation theorem on \(\mathcal U_{\rm rad}\).

A sharp sufficient blockwise statement is: for every fixed smooth radial
profile \(V\), every
\[
 (\delta,\nu)\in\mathcal U_{\rm rad},
\qquad
 D=X^\delta,\quad
 L\asymp D\sqrt{N/X},
\]
prove
\[
 \boxed{B_{D,N,V}(X)\ll_{\varepsilon,V}X^{1/4+\varepsilon}.}
\tag{4.1}
\]
Relative to the currently best accepted direct estimate, this requires
the exact power \(X^{\sigma_*(\delta,\nu)}\) from (3.12).

The narrow all-scale obstruction already lives at the hard top: for every
\(0<\nu<1/2\), it is enough, and necessary for a proof that estimates
scales separately, to establish the one-sided top instance of (4.1), with
the saving (3.13).  A global radial proof could instead cancel different
\(D_j\)-profiles, but then it must retain the exact Round-14 scale sum; a
single closed scale cannot certify the radial sector.

## 5. Required control tests and outcomes

1. **stationary_exponent_map — pass.**  Equations (2.2)--(2.4) retain the
   factor \(2\); it disappears only after taking \(\log_X\).
2. **active_support — pass.**  Equation (3.1) gives
   \((1-\nu)/2\leq\delta\leq1/2\), with no reversal of inequalities.
3. **floor_small_height — pass.**  The line
   \(\delta=\delta_0(\nu)\) is explicitly a bounded-frequency layer;
   \(H_j=O(1)\) occurs only at the lower active denominator corner.
4. **terminal_translation — pass.**  The terminal line maps exactly to
   \(\nu=1/2\), not to an interval below it.  Its failed-bound deficit is
   (3.8).
5. **TTY_translation — pass.**  The exact inequality is
   \(1816\delta+89\nu\leq552\); the first contact rational is
   \(356/819\).
6. **V2_translation — pass.**  Target equality at
   \((1/2,0)\) maps to \(\nu=0\), while the global failed-bound deficit
   \(\min(\delta-1/4,\nu/4)\) is retained in (3.11)--(3.12).
7. **union_over_delta — pass.**  Closure requires all of (1.2).
   Equations (3.6)--(3.7) show that every \(0<\nu<1/2\) has a survivor,
   even when a low-\(D\) TTY prefix exists.
8. **scale_sum — pass.**  The \(O(\log X)\) scale count is
   \(X^\varepsilon\), but absolute scale summation cannot erase an
   uncontrolled block.
9. **transform_errors — pass.**  The smooth radial multiplier has
   uniform rescaled derivatives; Mellin losses are polynomial and
   integrable.  Hard top, floors, profiles, stars, and polylogarithmic
   errors retain their accepted owners.
10. **first_uncovered_band — pass.**  The first nontrivial survivor is
    immediately above \(\nu=0\); the full open lower range is
    \(0<\nu<1/2\), and \(0<\nu<356/819\) is completely uncovered.
11. **required_saving — pass.**  The exact best-menu deficit is (3.12),
    including V2.  At the unavoidable top scale it reduces to (3.13).
12. **downstream_scope — pass.**  The diagram proves no estimate on
    \(\mathcal U_{\rm rad}\), no full GAR or M9-M1, no M9, and no
    Gauss-circle exponent.

## 6. Dependencies and exact artifacts used

Only the Round-61 authorized context was used:

- protocol.md
- state/proof_obligations.yml, specifically the accepted M1 terminal,
  TTY, V2/resonance-cell, phase-diagram, global-recombination, and
  critical-radial nodes
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-lower-radial-phase-diagram/derivation_packet.md
- rounds/codex-managed/m9-m1-critical-radial-terminal-return/synthesis.md
- rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md
- rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md

Round 60 supplies the separately proved \(\nu=1/2\) smooth-sector
theorem and the radial Mellin/error ledger.  Round 10 supplies the
terminal line, TTY wedge, and exact residual corridor.  Round 14 supplies
the all-scale angular coefficient, external \(R\), floors, profiles,
hard-top ownership, and stars.  The accepted graph supplies the global
V2 bound (3.10).  No web source was reopened because no theorem beyond
the already audited TTY node was proposed.

## 7. Recommended state effect

Promote, after the required independent validation, a scoped
M9-M1-lower-radial-phase-diagram lemma consisting of:

1. the exact stationary map (1.1), active interval (1.2), TTY boundary
   (1.3), and residual set (3.6);
2. the exact contact exponent \(\nu_*=356/819\);
3. the all-scale conclusion that only \(\nu=0\) and \(\nu=1/2\) are
   closed by the accepted direct menu;
4. the best-current saving ledger (3.12), including terminal, TTY, and
   V2, and its top specialization (3.13).

Record \(0<\nu<1/2\) as the first uncovered lower-radial band, with
\(0<\nu<356/819\) wholly uncovered and
\(356/819\leq\nu<1/2\) only partially TTY-covered.  The next narrow target
should be the exact one-sided hard-top smooth radial block, requiring
\(X^{\min(\nu,1-2\nu)/4}\) saving over the best accepted bound.

Retain lower-radial GAR, full GAR, blockwise M9-M1, M9, and the final
exponent as open.  Do not interpret the existence of one closed
denominator scale, or the \(O(\log X)\) scale count, as all-scale radial
closure.
