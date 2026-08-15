# Ordered resonance-cell cancellation attack

Campaign: `m9-m1-ordered-denominator-resonance-cells`  
Round: 13  
Role: analytic mechanism attacker  
Method allocation: entirely analytical; no numerical experiment and no
external theorem import were used.

## 1. Result

There is a rigorous ordered-denominator decomposition, but its elementary
cell estimates close no point of the residual corridor \(\mathcal U_1\).
The decomposition identifies the exact remaining object.

For one positive frequency shell, put

\[
 S_h(D;X)=\sum_{d\ \mathrm{odd}}\chi _4(d)w_D(d)e(hX/d),
 \qquad R_h=\frac{hX}{D^2}.
\]

The exact two-step increment distinguishes two notions which must not be
confused:

* direct two-term cancellation is strongest when
  \(2hX/(d(d+2))\) is near an **integer**;
* the bad Kusmin--Landau cells, after absorbing \(\chi _4\) into the
  phase, occur when the same number is near a **half-integer**.

Counting the half-integer cells and applying Kusmin--Landau on their
complement gives

\[
 \boxed{
 |S_h(D;X)|\ll_{w,\varepsilon}X^\varepsilon
 \min\!\left(D,\sqrt{D(R_h+1)}\right).}
 \tag{1.1}
\]

Since the actual Vaaler shell has
\(\sum_{h\asymp L}|u_{L,H}(h)|\ll1\), this yields

\[
 \boxed{
 |B_{1,L}(D;X)|\ll_{w,\varepsilon}X^\varepsilon
 \min\!\left(D,\sqrt{LX/D}\right).}
 \tag{1.2}
\]

In exponent coordinates the two alternatives have exponents
\(\delta\) and \((1+\ell-\delta)/2\).  Neither is at most \(1/4\) at
any point of \(\mathcal U_1\).  A first Weyl differencing step gives only
the classical \((1/6,2/3)\) reciprocal-phase exponent and likewise closes
no point of \(\mathcal U_1\).  Termwise pairing and scalar Abel summation
are still weaker.

For the low-curvature cells, Poisson/stationary-phase duality packages the
unresolved cancellation into the exact character cone

\[
 \sum_{h\asymp L}u_{L,H}(h)(hX)^{1/4}
 \sum_{\substack{q\ \mathrm{odd}\\
                  2\sqrt{hX/q}\in\operatorname{supp}w_D}}
 \frac{\chi _4(q)}{q^{3/4}}
 w_D\!\left(2\sqrt{hX/q}\right)e(\sqrt{Xhq}).
 \tag{1.3}
\]

The original character \(\chi _4(d)\) has migrated exactly to
\(\chi _4(q)\).  The phase in (1.3) depends only on the product \(hq\),
and its two-variable Hessian has determinant zero.  Grouping \(n=hq\)
turns (1.3) into one square-root phase weighted by a short, signed divisor
coefficient.  Thus a signed average across resonance cells is not free
two-dimensional curvature; it is an exact dual form of the accepted
cross-product/divisor-correlation problem.

The hard top contributes only a target-sized endpoint term.  At
\(X=y^2,D=y\), the previously successful family \(d=y-s\) lies in the
**nonresonant**, not the bad, half-integer cells: its increment is near the
integer \(2h\).  Its \(O(1)\) character cancellation therefore remains a
valid positive control, but it gives no cancellation among the residual
bad cells.

## 2. Exact statement and hypotheses

Let \(X\ge2\), \(X^{1/4}\le D\le X^{1/2}\),
\(1\le L\le H_D\asymp DX^{-1/4}\), and let \(w_D\) be one of the actual
fixed spatial profiles.  Thus \(w_D\) is supported on a fixed
multiplicative \(D\)-shell, has uniformly bounded discrete variation, and
the top profile is interpreted one-sided at \(d=\lfloor\sqrt X\rfloor\).
Let

\[
 u_{L,H}(h)=\eta(h/L)\frac{\Phi(h/(H+1))}{h},
 \tag{2.1}
\]

where \(\eta\) is the actual fixed shell cutoff.  Only the accepted
consequences

\[
 \sum_h|u_{L,H}(h)|\ll1,
 \qquad
 \|u_{L,H}\|_\infty+\sum_h|\Delta u_{L,H}(h)|\ll L^{-1}
 \tag{2.2}
\]

are used.  Fixed harmless Vaaler constants and the negative-frequency
conjugate are omitted.

### 2.1 Exact two-step identity

For odd \(d\),

\[
 \chi _4(d)=-i e(d/4).
 \tag{2.3}
\]

Put

\[
 g_h(d)=hX/d+d/4,
 \qquad
 \alpha_h(d)=\frac{2hX}{d(d+2)}.
 \tag{2.4}
\]

Then

\[
 \boxed{g_h(d+2)-g_h(d)=\frac12-\alpha_h(d).}
 \tag{2.5}
\]

Equivalently, a disjoint pair of consecutive odd denominators satisfies

\[
 \begin{aligned}
 &\chi _4(d)w_D(d)e(hX/d)
 +\chi _4(d+2)w_D(d+2)e(hX/(d+2))\\
 &\quad=\chi _4(d)e(hX/d)
 \left(w_D(d)-w_D(d+2)e(-\alpha_h(d))\right).
 \end{aligned}
 \tag{2.6}
\]

Thus (2.6) is small for equal weights when \(\alpha_h(d)\) is close to an
integer.  By contrast, the absorbed phase \(e(g_h(d))\) has an increment
close to an integer, and hence loses Kusmin--Landau cancellation, when
\(\alpha_h(d)\) is close to a half-integer.

### 2.2 Exact resonance cells and their cost

For \(0<\eta\le1/8\), define

\[
 \mathcal E_h(\eta)=
 \left\{d\asymp D:d\ \mathrm{odd},
 \operatorname{dist}(\alpha_h(d),\mathbb Z+\tfrac12)<\eta\right\}.
 \tag{2.7}
\]

Uniformly for \(h\asymp L\),

\[
 \boxed{
 \#\mathcal E_h(\eta)
 \ll \min\!\left(D,\eta D+R_h+1\right),
 \qquad R_h=\frac{hX}{D^2}.}
 \tag{2.8}
\]

The complement is a union of \(O(R_h+1)\) intervals on which the exact
increments (2.5) are monotone and remain at distance at least \(\eta\)
from the integers.  Weighted Kusmin--Landau therefore gives

\[
 |S_h(D;X)|
 \ll_w \eta D+R_h+1+\frac{R_h+1}{\eta}.
 \tag{2.9}
\]

If \(R_h\le D\), choose
\(\eta=((R_h+1)/D)^{1/2}\), truncating it at the harmless fixed constant
when necessary.  If \(R_h>D\), use the trivial bound.  Since
\(R_h\gg1\) in the active range, (2.9) proves (1.1).

### 2.3 Exact dual resonance cone

For a smooth interior profile, and for the top profile with its upper
endpoint treated one-sided, the weighted van der Corput transform gives

\[
 \begin{aligned}
 S_h(D;X)
 ={}&-i e(1/8)
 \sum_{\substack{q\ \mathrm{odd}\\
          d_{h,q}=2\sqrt{hX/q}\in\operatorname{supp}w_D}}^{\!*}
 \chi _4(q)(hX)^{1/4}q^{-3/4}\\
 &\hspace{37mm}\times
 w_D(d_{h,q})e(\sqrt{Xhq})+E_h,
 \end{aligned}
 \tag{2.10}
\]

where a star gives the usual half weight to an exact stationary endpoint,
and

\[
 E_h\ll_w \log(2+R_h)+1+\sqrt{\frac{D^3}{hX}}.
 \tag{2.11}
\]

After multiplication by the actual coefficient and summation over
\(h\asymp L\), (2.2) gives

\[
 \sum_h|u_{L,H}(h)E_h|
 \ll_w X^\varepsilon\left(1+\sqrt{\frac{D^3}{LX}}\right)
 \ll X^{1/4+\varepsilon}.
 \tag{2.12}
\]

The last inequality is uniform in the full active region, including
\(D=X^{1/2},L=1\).  Consequently the exact remaining resonance-cell
estimate is

\[
 \boxed{
 \begin{aligned}
 \mathfrak R_{D,L}(X):={}&
 \sum_{h\asymp L}u_{L,H}(h)(hX)^{1/4}
 \sum_{\substack{q\ \mathrm{odd}\\d_{h,q}\in\operatorname{supp}w_D}}^{\!*}
 \chi _4(q)q^{-3/4}w_D(d_{h,q})e(\sqrt{Xhq})\\
 &\ll_\varepsilon X^{1/4+\varepsilon}.
 \end{aligned}}
 \tag{RCS}
\]

RCS is sufficient and, up to the target-sized error (2.12), equivalent to
the M1 shell.  It is a strict analytic localization only when further
cancellation is proved; by itself it is an exact re-expression.

Grouping \(n=hq\), set

\[
 \begin{aligned}
 A^*_{D,L}(n;X)=
 \sum_{\substack{hq=n,\ h\asymp L,\ q\ \mathrm{odd}\\
                  2\sqrt{hX/q}\in\operatorname{supp}w_D}}
 &u_{L,H}(h)(hX)^{1/4}q^{-3/4}\chi _4(q)\\
 &\times w_D\!\left(2\sqrt{hX/q}\right).
 \end{aligned}
 \tag{2.13}
\]

Then RCS is exactly

\[
 \sum_{n\asymp N}A^*_{D,L}(n;X)e(\sqrt{Xn})
 \ll_\varepsilon X^{1/4+\varepsilon},
 \qquad N=\frac{L^2X}{D^2}.
 \tag{2.14}
\]

This is the smallest explicit residual statement produced by the ordered
cell method: it retains the actual Vaaler coefficient, actual spatial
profile, character, endpoint, and cross-cell phase.

## 3. Proof and capacity derivation

### 3.1 Proof of the cell count and nonresonant bound

On a fixed \(D\)-shell, \(\alpha_h(d)\asymp R_h\), and direct
differentiation gives

\[
 |\alpha_h'(d)|\asymp\frac{hX}{D^3}=\frac{R_h}{D}.
 \tag{3.1}
\]

The image of the shell meets \(O(R_h+1)\) half-integers.  The inverse
image of the \(\eta\)-neighborhood of each such half-integer has length
\(O(\eta D/R_h)\).  Counting odd integers adds at most one per component,
so summing over all components gives

\[
 \#\mathcal E_h(\eta)
 \ll (R_h+1)\left(1+\frac{\eta D}{R_h}\right)
 \ll R_h+1+\eta D,
\]

and the trivial \(D\)-cap proves (2.8).

On each complementary component, (2.5) is monotone and its distance from
the integers is at least \(\eta\).  Kusmin--Landau bounds the unweighted
partial sums by \(O(\eta^{-1})\).  Partial summation against the uniformly
bounded discrete variation of \(w_D\) preserves this order.  There are
\(O(R_h+1)\) components.  Taking absolute values only on the exceptional
set proves (2.9), and optimizing proves (1.1).  Finally (2.2) and
\(h\asymp L\) prove (1.2).  No averaging hypothesis on \(X\) is used.

The natural half-width of one low-curvature resonance cell is

\[
 \rho_h=\left(\frac{D^3}{hX}\right)^{1/2}
 =\sqrt{\frac{D}{R_h}}.
 \tag{3.2}
\]

There are \(\asymp R_h\) possible cells, and an individual quadratic
stationary cell can have size \(\asymp\rho_h\): on a sufficiently small
fixed multiple of \(\rho_h\), its quadratic phase varies by only a fixed
small constant.  Therefore summing uniform local cell bounds in absolute
value necessarily costs

\[
 R_h\rho_h=\sqrt{DR_h}.
 \tag{3.3}
\]

This proves a sharp capacity obstruction for any argument which uses only
cell count, local curvature, and absolute summation.  When \(R_h>D\), the
cells are sublattice-scale and the original trivial cost \(D\) is better;
there is then no localization gain at all.

### 3.2 Derivation of the dual character cone

Write \(d=2m+1\) and

\[
 F_h(m)=\frac{hX}{2m+1}+\frac{2m+1}{4}.
\]

Then

\[
 F_h'(m)=\frac12-\frac{2hX}{d^2},
 \qquad
 F_h''(m)=\frac{8hX}{d^3}>0.
 \tag{3.4}
\]

A Poisson mode \(\nu=-k\) has a stationary point precisely when

\[
 \frac{2hX}{d^2}=k+\frac12.
\]

Putting \(q=2k+1\), this point is

\[
 d=d_{h,q}=2\sqrt{hX/q},
 \tag{3.5}
\]

and its stationary amplitude is exactly

\[
 (F_h''(m))^{-1/2}
 =\frac{d^{3/2}}{\sqrt{8hX}}
 =(hX)^{1/4}q^{-3/4}.
 \tag{3.6}
\]

At the stationary point,

\[
 F_h(m)+km=\sqrt{Xhq}-\frac{k}{2},
 \qquad e(-k/2)=(-1)^k=\chi _4(q).
 \tag{3.7}
\]

The positive second derivative supplies \(e(1/8)\), while (2.3) supplies
the factor \(-i\).  Equations (3.5)--(3.7) give the main term in (2.10).

For completeness, the error in (2.11) follows by applying Poisson
summation on the fixed support interval, integrating nonstationary modes
by parts, and using one-dimensional stationary phase on the modes in the
range of \(F_h'\).  The ratios

\[
 \frac{|F_h'''|D}{F_h''}\asymp1,
 \qquad \frac{|F_h^{(4)}|D^2}{F_h''}\asymp1
\]

are uniform.  The nonstationary modes form a reciprocal-distance sum and
cost \(O(\log(2+R_h))\).  The two derivative endpoints cost at most
\(O(1+(F_h'')^{-1/2})=O(1+\rho_h)\); an exact endpoint stationary mode is
included with half weight.  The fixed profile derivatives contribute only
fixed constants.  The hard top is a summation endpoint, not an interior
profile jump in this calculation, so the same one-sided estimate applies.
This proves (2.10)--(2.12).

### 3.3 Product degeneracy and the exact missing saving

On the support of (1.3),

\[
 q\asymp Q:=\frac{LX}{D^2},
 \qquad h\asymp L,
 \qquad n=hq\asymp N:=LQ=\frac{L^2X}{D^2}.
 \tag{3.8}
\]

One dual term, including \(u_{L,H}(h)\), has size

\[
 A_0:=\frac{D^{3/2}}{\sqrt X\,L^{3/2}}.
 \tag{3.9}
\]

Consequently divisor multiplicity alone gives

\[
 |A^*_{D,L}(n;X)|\ll_\varepsilon A_0X^\varepsilon,
 \tag{3.10}
\]

and a triangle inequality in (2.14) gives

\[
 A_0N X^\varepsilon
 =X^\varepsilon\sqrt{LX/D},
 \tag{3.11}
\]

exactly the low-curvature cell cost.  Since each fixed product fiber has
at most \(\tau(n)=X^{o(1)}\) entries, pointwise compression of the fiber
cannot produce a power saving.

Moreover

\[
 \phi(h,q)=\sqrt{Xhq}
\]

has

\[
 \phi_{hh}=-\frac{\phi}{4h^2},\qquad
 \phi_{qq}=-\frac{\phi}{4q^2},\qquad
 \phi_{hq}=\frac{\phi}{4hq},\qquad
 \det D^2\phi=0.
 \tag{3.12}
\]

Thus a two-dimensional curvature estimate requiring a nonsingular Hessian
is inapplicable.  All pairs with the same product \(hq=n\) have exactly the
same oscillatory phase.  Any improvement over (3.11) must use cancellation
in the signed divisor coefficient (2.13), or cancellation across different
products \(n\); it cannot come from generic two-variable phase spacing.

The exact power missing from the absolute cell method is

\[
 \kappa_{\rm cell}(\delta,\ell)=
 \begin{cases}
 \delta-\tfrac14,
   &1+\ell>3\delta \quad(R>D),\\[2mm]
 \dfrac{1+2\ell-2\delta}{4},
   &1+\ell\le3\delta \quad(R\le D).
 \end{cases}
 \tag{3.13}
\]

Both quantities are strictly positive on \(\mathcal U_1\).  In the second
line, equality can occur in the active region only at
\((\delta,\ell)=(1/2,0)\), which is already excluded from
\(\mathcal U_1\).  Hence (1.2) closes no new point.

### 3.4 Capacity of pairing, Abel, and one further differencing step

Equation (2.6) and bounded variation give, after taking absolute values,
at best \(O_w(D)\), because
\(|1-e(-\alpha_h(d))|\) is uniformly allowed to be of order one.  The
same obstruction appears if one first sums in \(h\): the actual kernel
values at \(X/d\) and \(X/(d+2)\) are separated by
\(2X/(d(d+2))\), and in the active range
\(LX/D^2\ge1\); the Lipschitz estimate therefore saturates at its trivial
constant bound on generic pairs.  Termwise pairing has no target capacity
for \(\delta>1/4\).

If van der Corput differencing is applied to \(S_h\), then for an odd-step
shift \(2r\),

\[
 \chi _4(d+2r)\overline{\chi _4(d)}=(-1)^r,
 \tag{3.14}
\]

which is constant in \(d\).  The differenced phase is

\[
 hX\left(\frac1{d+2r}-\frac1d\right).
 \tag{3.15}
\]

Thus the first differencing step removes, rather than amplifies, the
character structure.  The resulting standard \(A\)-process estimate is
the classical exponent-pair bound

\[
 |S_h|\ll_\varepsilon
 (hX/D)^{1/6}D^{1/2+\varepsilon},
 \tag{3.16}
\]

equivalently exponent

\[
 \frac{1+\ell}{6}+\frac{\delta}{3}.
\]

It reaches the target only if

\[
 2\ell+4\delta\le1,
\]

which in \(\Omega\) is only the left corner
\((\delta,\ell)=(1/4,0)\).  More elaborate untwisted exponent-pair
iteration is already represented by the stronger accepted TTY wedge; a
single extra differencing step adds no part of \(\mathcal U_1\).

## 4. First doubtful or unproved step

The first unproved step is RCS, equivalently (2.14).  No estimate in this
report saves a power in the signed coefficient \(A^*_{D,L}(n;X)\), and no
spacing theorem is available from the phase alone because of the rank-one
degeneracy (3.12).

In particular, it would be invalid to apply a one-dimensional exponent-sum
estimate to \(\sum_nA^*(n)e(\sqrt{Xn})\) while retaining only the pointwise
bound (3.10): \(A^*(n)\) is not a fixed smooth weight and may carry the
opposite phase.  It would also be invalid to estimate the separate
\(h\)- or \(q\)-fibers and infer cross-product cancellation.  The missing
lemma must exploit the actual restricted convolution in (2.13), including
\(\chi _4(q)\), rather than divisor multiplicity or generic curvature.

In the high-curvature subregion \(R>D\), even the localization is not a
strict reduction: the cells are shorter than the odd-denominator lattice
spacing and the trivial \(D\)-term estimate is better than their summed
stationary costs.  There the ordered-cell proposal has no demonstrated
capacity beyond a reparametrization of the original sum.

## 5. Required controls and outcomes

### Exact increment control: pass

Equations (2.3)--(2.6) are exact.  They also catch the essential sign
distinction: integer \(\alpha_h(d)\) is favorable for a two-term pair,
whereas half-integer \(\alpha_h(d)\) is a bad absorbed-phase resonance.
Treating both as the same notion would reverse the control.

### Cell-count and total-cost control: pass, with no target region

The monotonicity calculation gives the complete cost
\(\eta D+R+(R+1)/\eta\), including the number of cell boundaries.  Its
optimized value is (1.1), and the exponent audit (3.13) shows that it is
strictly above \(X^{1/4}\) throughout \(\mathcal U_1\).

### Frequency-boundary control: pass

The actual coefficient is retained in (1.3).  Its \(\ell^1\) norm is
bounded, so summing the fixed-\(h\) errors creates no factor \(L\).  The
frequency-shell endpoints are included in (2.2), and the logarithmic loss
is absorbed by \(X^\varepsilon\).

### Hard-top control: pass

The one-sided denominator endpoint contributes at most

\[
 1+\sqrt{D^3/(LX)}\le 1+X^{1/4}.
\]

At \(D=X^{1/2}\) this is \(1+X^{1/4}L^{-1/2}\).  Thus the top boundary is
target-sized even for \(L=1\); it is not the obstruction in RCS.

### Exact-square cancellation family: pass, but it is nonresonant

Let \(X=y^2\), \(D=y\), \(y\) odd, and
\(d=y-s\) with even \(0\le s\le S=c\sqrt{y/L}\).  Then

\[
 \frac{X}{y-s}=y+s+\frac{s^2}{y-s},
 \qquad
 \chi _4(y-(s+2))=-\chi _4(y-s).
 \tag{5.1}
\]

For the actual frequency-summed kernel \(K_{L,H}\),
\(\|K'_{L,H}\|_\infty\ll L\), and

\[
 L\,\operatorname{Var}_{0\le s\le S}
 \left(\frac{s^2}{y-s}\right)
 \ll \frac{LS^2}{y}\ll1.
\]

Discrete Abel summation therefore gives the accepted \(O_w(1)\) signed
subtotal.  At the same time, uniformly for \(h\asymp L\),

\[
 \frac{2hy^2}{(y-s)(y-s+2)}=2h+O(hs/y),
 \tag{5.2}
\]

and \(hs/y\ll\sqrt{L/y}=o(1)\) in the active top range.  Hence this family
stays a fixed distance from the half-integer bad cells.  It is a genuine
positive control for ordered character cancellation, but it does not
validate cancellation between the RCS stationary cells.

### Character-erased/adversarial control: pass

Erasing \(\chi _4\) destroys (5.1)'s alternating subtotal.  Conversely,
after one Weyl differencing step the character product is the constant
\((-1)^r\), as in (3.14), so any claimed additional saving from character
oscillation at that stage would also prove an untwisted statement.  The
report makes no such claim.

### Product-fiber control: red/open exactly at RCS

The phase is constant on every product fiber \(hq=n\), and the Hessian is
singular.  The divisor bound gives only (3.10)--(3.11), missing the positive
power (3.13).  No numerical example is used to disguise this open step.

## 6. Dependencies and exact artifacts used

Only the brief-authorized files were read:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`;
* `rounds/codex-managed/m9-m1-near-product-character-kernel/reports/near_product_hostile_audit.md`;
* `rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md`;
* `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
* `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/briefs/ordered_cell_cancellation_attack.md`.

No other Round-13 report was read.  The only background tools used are the
elementary period-four character identity, partial summation,
Kusmin--Landau, Poisson summation with one-dimensional stationary phase,
and the divisor bound \(\tau(n)\ll_\varepsilon n^\varepsilon\).  No web
source, external result specialized to this problem, Python, or Mathematica
was used.

## 7. Recommended state effect

1. **Promote as a scoped no-go/capacity lemma:** exact two-step
   resonance counting plus separate absolute cell bounds yields only
   \(B_{1,L}\ll X^\varepsilon\min(D,\sqrt{LX/D})\), which closes no point
   of \(\mathcal U_1\).  Termwise pairing, scalar Abel, and one ordinary
   differencing step have no greater target capacity.
2. **Retain M9-M1 and PSC as open.**  Do not infer a target estimate from
   the resonance decomposition.
3. **Record RCS as the exact surviving ordered-cell interface:** after a
   target-sized endpoint/error term, it is equivalent to M1 and groups as
   the signed short-divisor coefficient (2.13) against
   \(e(\sqrt{Xn})\).
4. **Retain the exact-square family as a positive control only:** it is a
   favorable nonresonant family and does not test cancellation among the
   bad half-integer cells.
5. **Reject nondegenerate two-variable-curvature shortcuts:** the dual
   phase \(\sqrt{Xhq}\) has rank-one Hessian and is constant on product
   fibers.  A future lemma must exploit the actual \(\chi _4(q)\)-weighted
   restricted convolution, or introduce information across distinct
   products that is absent from cell counting.
