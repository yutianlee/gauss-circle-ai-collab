# Hostile audit: capacity of the M1 near-product character fiber

Campaign: `m9-m1-near-product-character-kernel`  
Round: 11  
Role: hostile capacity reviewer  
Method allocation: entirely analytical; no numerical experiment and no
external theorem import were used.

## 1. Result

There is a rigorous route obstruction, but not an obstruction to the actual
M1 estimate.

1. The frequency-first M1 block has an exact nearest-product regrouping in
   which the character occurs in a **short truncated divisor fiber**, but the
   actual Fourier kernel still depends on the individual divisor through
   \((X-n)/d\).  Replacing that kernel by the bare coefficient
   \(A_D(n)=\sum_{d\mid n}\chi _4(d)w_D(d)\) on the whole coherent window is
   not exact.
2. Pointwise cancellation on one divisor fiber is not a uniform mechanism.
   Exact prime-power, semiprime, and square controls give singleton active
   fibers, while a many-divisor family gives sign-locked fibers of size
   \(\gg\log X\) for nonnegative actual dyadic profiles.  Thus there is no
   identity forcing a power saving on every fiber.
3. The trivial near-window scale is
   \(D/L=X^{\delta-\ell}\).  The target needs the power saving
   \[
   X^{\gamma},\qquad \gamma=\delta-\ell-\frac14>0
   \]
   everywhere in the residual corridor.  Since one fiber has at most
   \(\tau(n)=X^{o(1)}\) entries, divisor-fiber compression followed by a
   triangle inequality over \(n\) has only subpower capacity.  It cannot
   supply \(X^\gamma\) on any fixed subregion \(\gamma\ge\eta>0\).
4. This limitation is sharp for arbitrary bounded spatial weights.  For
   every compact interior point of the residual corridor there are real
   \(X\) and bounded, nonsmooth, \(X\)-dependent dyadic weights for which the
   positive-frequency block has size \(\gg D/L\).  Hence an
   arbitrary-bounded-weight strengthening of the desired M1 bound is false
   by the exact factor \(X^\gamma\).
5. Actual fixed profiles are different.  At an exact-square endpoint an
   explicit family of \(\asymp(D/L)^{1/2}\) nearby products cancels to
   \(O(1)\) under \(\chi _4\), whereas its character-erased analogue has that
   full size.  This cancellation occurs **across different products**,
   not inside one divisor fiber.  It shows where an actual proof may still
   live: a cross-product oscillation estimate retaining the ordered
   \(d\)-variable, rather than separate absolute estimates for the fibers.

Recommended conclusion: reject a single-fiber-cancellation-plus-triangle
strategy and reject arbitrary bounded weights; retain the actual M1 kernel
as open and revise the next lemma to a signed cross-\(n\) (or equivalent
two-variable) estimate.

## 2. Exact statements and hypotheses

### 2.1 Exact nearest-product regrouping

Let \(\eta\ge0\) be a fixed smooth frequency cutoff supported in a compact
subinterval of \((0,\infty)\), let \(1\le L\le H\), and put
\[
 u_{L,H}(h)=\eta(h/L)\frac{\Phi(h/(H+1))}{h},
 \qquad
 K_{L,H}(z)=\sum_{h\ge1}u_{L,H}(h)e(hz).
\]
The harmless fixed constant and rotation coming from the positive Vaaler
coefficient are suppressed.  For a spatial block \(d\asymp D\), define
\[
 B_1^+(D,L;X)=
 \sum_{d\asymp D}\chi _4(d)w_D(d)K_{L,H}(X/d).
\]
For each \(d\), choose a nearest integer
\(m_d\) to \(X/d\), with any fixed convention at a half-integer, and set
\(n_d=dm_d\).  Periodicity gives the exact identity
\[
 \boxed{
 B_1^+(D,L;X)=
 \sum_{|n-X|\ll D}
 \sum_{\substack{d\mid n,\ d\asymp D\\
                 |X-n|\le d/2\\ n/d=m_d}}
 \chi _4(d)w_D(d)
 K_{L,H}\!\left(\frac{X-n}{d}\right).}
 \tag{2.1}
\]
The convention condition in (2.1) is redundant away from half-integers but
is displayed to keep the regrouping literally exact.

The kernel satisfies
\[
 |K_{L,H}(z)|\ll
 \min\left(1,\frac1{L\|z\|}\right),
 \qquad
 \|K'_{L,H}\|_\infty\ll L,
 \tag{2.2}
\]
for the fixed-BV frequency profile used in the project.  Hence the coherent
window is
\[
 |n-X|\lesssim \Delta,\qquad \Delta=\frac DL.
 \tag{2.3}
\]
For \(|n-X|\le cD/L\), Taylor's formula only gives
\[
 K_{L,H}\!\left(\frac{X-n}{d}\right)
 =K_{L,H}(0)+O\!\left(\frac{L|X-n|}{D}\right).
 \tag{2.4}
\]
The error in (2.4) is order one at the outer edge of (2.3).  Therefore the
bare character-divisor coefficient
\[
 A_D(n)=\sum_{\substack{d\mid n\\d\asymp D}}
 \chi _4(d)w_D(d)
 \tag{2.5}
\]
is an exact leading model only in a narrower window, not an exact
replacement throughout (2.3).

### 2.2 Single-fiber capacity obstruction

For \(n\asymp X\), the active fiber has cardinality
\[
 r_D(n)=\#\{d\mid n:d\asymp D\}\le\tau(n)\ll_\varepsilon X^\varepsilon.
 \tag{2.6}
\]
Taking absolute values in (2.1), using (2.2), and summing proximity shells
recovers the accepted scale
\[
 |B_1^+(D,L;X)|\ll_\varepsilon X^\varepsilon
 \left(1+\frac DL\right).
 \tag{2.7}
\]
Any regrouping gain that uses only (2.6), or a square-root improvement in
the number of divisors within each fixed \(n\), is absorbed by
\(X^\varepsilon\).  After a triangle inequality over the
\(\asymp D/L\) possible near products it retains exponent
\(\delta-\ell\), whereas M1 requires exponent \(1/4\).  Thus its exact
power deficit is
\[
 \boxed{\gamma=\delta-\ell-\frac14.}
 \tag{2.8}
\]
On every compact subset \(\gamma\ge\eta>0\) of \(\mathcal U_1\), a
power-saving assertion about almost all fibers, or cancellation between
different \(n\), is logically necessary.  Pointwise multiplicity alone has
no such capacity.

The next controls show that the stronger possible escape, a uniform exact
or power-saving identity for each \(A_D(n)\), is false.

### 2.3 Arbitrary bounded-weight no-go

Assume \(L/H\to0\), as happens at every fixed interior exponent
\(\ell<\delta-1/4\), and use a nonnegative nonzero dyadic frequency cutoff.
Then there is an absolute \(c_0>0\) such that
\[
 \operatorname{Re}K_{L,H}(z)\gg1
 \quad\text{when}\quad \|z\|\le c_0/L.
 \tag{2.9}
\]
For \(D=X^{\delta+o(1)}\), \(L=X^{\ell+o(1)}\) with
\(\ell<\delta-1/4\), there are arbitrarily large real \(X\) and bounded real
weights supported on \(d\asymp D\) for which
\[
 \boxed{|B_1^+(D,L;X)|\gg D/L.}
 \tag{2.10}
\]
Indeed the weights may be chosen as
\[
 w_X(d)=\chi _4(d)
 \mathbf1_{\{d\asymp D,\ d\ {\rm odd},\
                   \|X/d\|\le c_0/L\}}.
 \tag{2.11}
\]
These weights are deliberately not the actual fixed smooth partition.
Consequently (2.10) is a no-go only for arbitrary bounded weights, not for
M1 itself.  In exponent coordinates, (2.10) exceeds the desired scale by
exactly
\[
 \frac{D/L}{X^{1/4}}=X^{\gamma+o(1)}.
 \tag{2.12}
\]

### 2.4 Exact-square endpoint cross-product control

Let \(X=y^2\) with \(y\) odd, \(D=y\), let the top spatial profile
\(W(d/y)\) be \(C^1\) with \(W(1)>0\), and retain a positive-frequency
kernel as above with \(L/H\to0\), the strict residual-corridor regime at
\(\delta=1/2\).  For a sufficiently small fixed \(c>0\), set
\[
 S=\left\lfloor c\sqrt{\frac yL}\right\rfloor .
\]
On the subfamily \(d=y-s\), \(0\le s\le S\), \(s\) even, one has
\[
 \frac{X}{d}=y+s+\frac{s^2}{y-s},
 \qquad n=d(y+s)=y^2-s^2,
 \tag{2.13}
\]
and \(y+s\) is the nearest integer.  The actual signed subtotal obeys
\[
 \boxed{
 \sum_{\substack{0\le s\le S\\s\ {\rm even}}}
 \chi _4(y-s)W(1-s/y)
 K_{L,H}\!\left(\frac{s^2}{y-s}\right)=O_W(1).}
 \tag{2.14}
\]
After erasing \(\chi _4\), the real part of the same subtotal is
\[
 \gg S\asymp (D/L)^{1/2}.
 \tag{2.15}
\]
Thus actual character cancellation can be substantial, but (2.13) shows
that it runs across the distinct products \(y^2-s^2\).  It is invisible to
a strategy that estimates every \(n\)-fiber separately and then takes
absolute values.

## 3. Proofs and derivations

### 3.1 Regrouping and kernel bounds

For the chosen nearest integer, write
\(X/d=m_d+(X-n_d)/d\).  Since \(h m_d\) is integral,
\(e(hX/d)=e(h(X-n_d)/d)\).  Grouping equal values of \(n_d\) proves
(2.1).  Abel summation in \(h\) gives the first inequality in (2.2), while
direct differentiation and
\(u_{L,H}(h)\ll L^{-1}\) on \(h\asymp L\) give
\[
 \sum_h h|u_{L,H}(h)|\ll L,
\]
which proves the derivative estimate and (2.4).

### 3.2 Proof of the bounded-weight obstruction

Let \(T\) be a large reference scale and hold \(D=T^{\delta+o(1)}\),
\(L=T^{\ell+o(1)}\) fixed while \(x\) varies in \([T,2T]\).  For each odd
\(d\asymp D\), periodicity modulo \(d\) gives
\[
 \operatorname{meas}\{x\in[T,2T]:\|x/d\|\le c_0/L\}
 =\frac{2c_0T}{L}+O(d).
 \]
Summing over the \(\asymp D\) odd integers in the spatial shell and dividing
by \(T\) yields
\[
 \frac1T\int_T^{2T}
 \#\{d\asymp D:d\ {\rm odd},\ \|x/d\|\le c_0/L\}\,dx
 \gg \frac DL-O\!\left(\frac{D^2}{T}\right).
 \tag{3.1}
\]
Here \(D^2/T\ll1\), while \(D/L\ge T^{1/4+o(1)}\).  Some
\(X\in[T,2T]\) therefore has \(\gg D/L\) selected denominators.  For the
weight (2.11), \(\chi _4(d)w_X(d)=1\) on this set, it is zero elsewhere,
and (2.9) proves (2.10).

To verify (2.9), note that in the interior corridor
\(h/(H+1)=o(1)\), so \(\Phi(h/(H+1))\) is uniformly positive on the fixed
frequency shell and \(K_{L,H}(0)\asymp1\).  If
\(|z|\le c_0/L\), choosing \(c_0\) small makes every \(e(hz)\) lie in a
fixed right half-plane.  Hence the real part remains bounded below.

### 3.3 Exact fiber controls

The following are algebraic controls; none is asserted to lower-bound the
whole signed M1 block.

* **Prime.**  If \(n=P\) is prime and
  \(P^{1/4}\ll D\ll P^{1/2}\), then the active fiber is empty, since the
  only divisors are \(1,P\).  Hence \(A_D(P)=0\).  Fiber occupancy is not
  uniform.
* **Semiprime.**  Let \(n=pq\), where \(p<q\) are odd primes,
  \(p\asymp D\), and \(q\) lies outside the dyadic \(D\)-shell.  If the
  profile is nonzero at \(p\), then the active fiber is the singleton
  \(d=p\), so
  \[
  A_D(n)=\chi _4(p)w_D(p)\ne0.
  \tag{3.2}
  \]
  By choosing \(q=p^{(1-\delta)/\delta+o(1)}\), this occurs at every
  prescribed limiting \(1/4\le\delta<1/2\).
* **Prime power.**  Let \(n=p^k\), with the odd prime \(p\) larger than
  the fixed multiplicative width of the dyadic shell, and take
  \(D\asymp p^j\).  Exactly one power \(p^j\) is active, and
  \[
  A_D(p^k)=\chi _4(p)^j w_D(p^j).
  \tag{3.3}
  \]
  Ratios \(j/k\) are dense in the active \(\delta\)-range.  Setting
  \(k=2j\) gives the exact-square endpoint \(n=X=p^{2j}\),
  \(D=\sqrt X=p^j\), including the hard endpoint divisor.
* **Many divisors, sign locked.**  Put \(n=65^K=5^K13^K\).  Every
  divisor has \(\chi _4(d)=1\).  The divisors
  \(5^a13^b\) with \(K/4\le a,b\le K/2\) number \(\gg K^2\) and lie
  between \(n^{1/4}\) and \(n^{1/2}\).  There are only \(O(K)\) dyadic
  blocks in that range, so one block contains \(\gg K\) of them.  For a
  nonnegative finite-overlap partition with \(\sum_Dw_D(d)=1\), summing
  over blocks and pigeonholing gives an actual block satisfying
  \[
  A_D(n)=\sum_{d\mid n}\!w_D(d)\gg K\asymp\log n.
  \tag{3.4}
  \]
  This is only logarithmic and is absorbed by \(X^\varepsilon\), but it
  disproves automatic cancellation even on a highly composite active
  fiber.

At exact resonance \(n=X\), the kernel in (2.1) is the common value
\(K_{L,H}(0)\asymp1\), so (3.2)--(3.4) are genuine controls for the actual
near-product coefficient, not artifacts of replacing its divisor-dependent
kernel.

### 3.4 Proof of the exact-square cancellation control

For \(s\le S\), (2.13) is exact and
\(s^2/(y-s)<1/2\), so the stated nearest integer is valid.  Since \(y\) is
odd and \(s\) is even,
\[
 \chi _4(y-(s+2))=-\chi _4(y-s).
 \tag{3.5}
\]
The partial sums of this sign sequence are bounded.  Set
\[
 F(s)=W(1-s/y)K_{L,H}(s^2/(y-s)).
\]
The \(C^1\) spatial profile contributes total variation \(O(S/y)\).  Also
\[
 \left(\frac{s^2}{y-s}\right)'
 =\frac{2sy-s^2}{(y-s)^2},
\]
and therefore, by (2.2),
\[
 \operatorname{Var}_{[0,S]}K_{L,H}(s^2/(y-s))
 \ll L\frac{S^2}{y-S}\ll1.
\]
Discrete Abel summation using (3.5) proves (2.14).  If \(c\) is sufficiently
small, then \(s^2/(y-s)\le c^2/L\), so all frequency phases remain in a
fixed right half-plane.  Since \(W(1)>0\), shrinking the endpoint interval
if necessary gives (2.15).

### 3.5 Fixed-profile versus divisor-restricted cancellation

For a fixed \(C^1\) profile, bounded partial sums of \(\chi _4\) give the
ordinary consecutive-integer estimate
\[
 \sum_d\chi _4(d)W(d/D)=O_W(1).
 \tag{3.6}
\]
There is no transfer of (3.6) to \(d\mid n\): the divisor restriction can
select a singleton as in (3.2)--(3.3), or only residue class \(1\pmod4\) as
in (3.4).  Conversely, (2.14) proves that keeping the order of nearby
denominators can expose cancellation across different values of \(n\).
This is the exact distinction the next argument must preserve.

## 4. First doubtful or unproved step

No step above proves a lower bound for the complete actual M1 block, and no
such lower bound is claimed.  The singleton and many-divisor examples are
controls for individual fibers; contributions from other products may
cancel them.  The arbitrary-weight lower bound uses an \(X\)-dependent,
nonsmooth adversarial weight and therefore cannot be transferred to the
actual partition.

The first genuinely open step is a cross-product estimate for the fixed
profile version of (2.1), strong enough to save
\(X^{\gamma}\) while retaining the variation of
\(K((X-n)/d)\).  The exact-square calculation proves such cancellation only
on one special endpoint subfamily of length \((D/L)^{1/2}\); it neither
covers the remaining denominators nor any general interior point of
\(\mathcal U_1\).

## 5. Required controls and outcomes

| Control | Exact input | Outcome | Implication |
|---|---|---|---|
| Exact square | \(X=p^{2j}\), \(D=p^j\), and separately \(d=y-s\) at \(X=y^2\) | Exact fiber is a nonzero singleton; the nearby endpoint family cancels from \((D/L)^{1/2}\) to \(O(1)\) | A single term cannot lower-bound the block; actual cancellation is cross-product |
| Prime | \(n=P\) prime, active \(D\) | Empty fiber | Do not assume uniform occupancy of nearby products |
| Semiprime | \(n=pq\), only \(p\asymp D\) | Nonzero singleton fiber | No uniform per-fiber character saving |
| Prime power | \(n=p^k\), \(D\asymp p^j\) | One active divisor for a narrow dyadic shell | Singleton obstruction occurs at dense limiting \(\delta=j/k\) |
| Many divisors | \(n=65^K\), nonnegative actual partition | Some active block has \(A_D(n)\gg\log n\), all signs positive | Smoothness does not survive divisor restriction as character cancellation |
| Endpoint | \(X=y^2,D=y,d=y-s\) | Alternating \(\chi _4(y-s)\) gives exact \(O(1)\) subtotal | Cross-\(n\) cancellation is real but special |
| Fixed profile | \(W(d/D)\) versus \(W(d/D)\mathbf1_{d\mid n}\) | Consecutive sum is \(O_W(1)\); restricted sum may be singleton or sign locked | The divisor selector is the first seam requiring a new lemma |
| Arbitrary bounded weights | Weight (2.11) selected by near resonance | Block size \(\gg D/L=X^{\delta-\ell}\) | The arbitrary-weight target fails by \(X^\gamma\) throughout compact subsets of \(\mathcal U_1\) |
| Actual versus adversarial | Fixed nonnegative partition versus (2.11) | The full lower bound is proved only for the adversary | No obstruction to actual M1 has been proved |

All controls are exact and analytical.  No computation was used.

## 6. Dependencies and exact artifacts used

Only the context authorized by the brief was used:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `state/best_proof_draft.md`;
* `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`;
* `state/control_models.md`;
* `rounds/codex-managed/m9-m1-near-product-character-kernel/briefs/near_product_hostile_audit.md`.

No Round-11 claimant report was read.  The divisor bound
\(\tau(n)\ll_\varepsilon n^\varepsilon\), bounded partial sums of the
elementary period-four character, Abel summation, and elementary measure
averaging are the only background inputs.  No primary literature was
needed.

## 7. Recommended state effect

**Retain M9-M1 and the Round-11 kernel estimate as open.**

Promote, if the conductor's independent derivation and seam review agree,
the following scoped no-go statement:

> In every compact subregion of \(\mathcal U_1\), the missing power is
> \(X^{\delta-\ell-1/4}\).  It cannot be supplied by divisor multiplicity
> compression followed by a triangle inequality over products; no uniform
> pointwise character-cancellation identity exists on the active divisor
> fibers, and the corresponding arbitrary-bounded-weight M1 assertion is
> false at scale \(D/L\).

Revise the research target to an actual-profile cross-product estimate for
(2.1), or an equivalent estimate in the ordered \((d,m)\) variables.  The
new lemma must identify cancellation between different nearby products and
must fail on the adversarial weight (2.11).  Do not promote any total-block
lower bound or any no-go against the actual Vaaler M1 sum.
