# Blind paired-offset identity and capacity audit

- Campaign: `m9-m1-cross-product-offset-pairing`
- Round: `12`
- Task: `blind_offset_pairing_identity`
- Role: statement-only exact deriver
- Isolation: no Round-11 or other Round-12 report was read
- Numerical work: none

## 1. Result

There is an exact pairing on the integer product lattice, but it does not
produce the hoped-for cancellation.  When (2X\in\mathbb Z), products are
paired at genuinely opposite offsets from (X).  When (2X\notin\mathbb Z),
the two offset sets are different translates of the integers; the correct
rank pairing is around the intervening half-integer

\[
c=\lfloor X\rfloor+\frac12.
\]

Moving the phase center from (X) to (c) costs only (O(L)), uniformly
for every active denominator profile, including the hard top profile.  Thus
it is enough to prove the M1 bound on the lattice
\(\frac12\mathbb Z\).

At a lattice center (c\in\frac12\mathbb Z), however, oddness does not make
the two paired product contributions cancel.  The two divisor sets are
disjoint, and the divisibility congruence reverses the kernel sign on the
upper product.  That reversal cancels the minus sign supplied by oddness.
Consequently the two sides **reinforce**:

\[
\begin{aligned}
&\sum_{\tau}
 \left\{
 \sum_{\substack{d\mid c-\tau\\d>2\tau}}
       \chi_4(d)w_D(d)\mathcal V(\tau/d)
 -\sum_{\substack{d\mid c+\tau\\d>2\tau}}
       \chi_4(d)w_D(d)\mathcal V(\tau/d)
 \right\}                                                     \\
&\qquad=
\sum_{\tau}\sum_{d>2\tau}\chi_4(d)w_D(d)
 \bigl({\bf1}_{d\mid c-\tau}+{\bf1}_{d\mid c+\tau}\bigr)
 \mathcal V(c/d)
=\sum_d\chi_4(d)w_D(d)\mathcal V(c/d).
\end{aligned}
\tag{1.1}
\]

Here \(\tau\) runs over positive integers when (c\) is an integer and over
positive half-integers when (c\) is a strict half-integer.  Equality at
(d=2\tau) is immaterial because \(\mathcal V(1/2)=0\).

Therefore naive opposite-offset pairing has no capacity to supply the
missing factor (H/L) in the residual corridor.  The weakest useful
remaining estimate is an outside-absolute shifted-divisor correlation for
the full expression in (1.1), of size (D/H\); by (1.1) this is precisely
the centered M1 block, not a simpler divisor-set stability statement.

## 2. Exact statement and hypotheses

Write (e(z)=e^{2\pi iz}).  Let (1\le L\le H\), let (v_L) be the actual
real dyadic frequency profile, supported on (h\asymp L), and put

\[
u_{L,H}(h)=v_L(h)\frac{\Phi(h/(H+1))}{h},
\qquad
\mathcal V_{L,H}(z)=\frac4\pi\sum_{h>0}u_{L,H}(h)
\sin(2\pi hz).
\tag{2.1}
\]

Only the standard actual-profile properties are used: (O(L)) indices
occur, \(|v_L(h)|\ll1\), and \(|\Phi(h/(H+1))|\ll1\).  Hence

\[
\mathcal V(-z)=-\mathcal V(z),\qquad
\mathcal V(z+1)=\mathcal V(z),\qquad
\mathcal V(0)=\mathcal V(1/2)=0,
\tag{2.2}
\]

and

\[
\|\mathcal V\|_\infty\ll1,
\qquad
\|\mathcal V'\|_\infty
\le 8\sum_{h>0}|v_L(h)\Phi(h/(H+1))|\ll L.
\tag{2.3}
\]

Let (w_D) be any actual active spatial profile.  It is enough here that
\(|w_D|\ll1\), that it is supported on (d\asymp D\), and that

\[
\mathscr H_D:=\sum_{d\ge1}\frac{|\chi_4(d)w_D(d)|}{d}\ll1.
\tag{2.4}
\]

The exact two-sided kernel block is

\[
\mathcal M_{D,L}(X)=
\sum_d\chi_4(d)w_D(d)
\mathcal V_{L,H}\left(\frac{X-n_X(d)}d\right),
\qquad
n_X(d)=d\left\lfloor\frac Xd+\frac12\right\rfloor.
\tag{2.5}
\]

By periodicity this is also

\[
\mathcal M_{D,L}(X)=
\sum_d\chi_4(d)w_D(d)\mathcal V_{L,H}(X/d).
\tag{2.6}
\]

For (c\in\frac12\mathbb Z), define its positive product-offset lattice

\[
\Lambda_c^+=\{\tau>0:c-\tau\in\mathbb Z, c+\tau\in\mathbb Z\}.
\tag{2.7}
\]

Thus \(\Lambda_c^+=\mathbb Z_{\ge1}\) for (c\in\mathbb Z), while
\(\Lambda_c^+=\mathbb Z_{\ge0}+1/2\) for
\(c\in\mathbb Z+1/2\).  The two centered divisor sets are

\[
\mathscr D_c^-(\tau)=
\{d\ge1:w_D(d)\ne0, d\mid c-\tau, d>2\tau\},
\tag{2.8}
\]

\[
\mathscr D_c^+(\tau)=
\{d\ge1:w_D(d)\ne0, d\mid c+\tau, d>2\tau\}.
\tag{2.9}
\]

The notation (d\mid c\pm\tau) is legitimate because (c\pm\tau) is an
integer.  The exact centered paired sum is

\[
\mathfrak Q_{D,L}(c)=
\sum_{\tau\in\Lambda_c^+}
\left(
\sum_{d\in\mathscr D_c^-(\tau)}\chi_4(d)w_D(d)\mathcal V(\tau/d)
-\sum_{d\in\mathscr D_c^+(\tau)}\chi_4(d)w_D(d)\mathcal V(\tau/d)
\right).
\tag{2.10}
\]

The exact conclusions are:

1. \(\mathfrak Q_{D,L}(c)=\mathcal M_{D,L}(c)\), with the reinforcing
   identity (1.1).
2. If (X=N+\theta\), (0<\theta<1\), and
   (c=N+1/2\), then, with \(\sigma=\theta-1/2\),

   \[
   \mathcal M_{D,L}(X)=\mathfrak Q_{D,L}(c)+E_{D,L}(X;c),
   \qquad
   |E_{D,L}(X;c)|\ll L|\sigma|\mathscr H_D\ll L.
   \tag{2.11}
   \]

3. If (X\in\frac12\mathbb Z), take (c=X); then \(E=0\).
4. A sufficient residual-corridor estimate is

   \[
   \boxed{
   |\mathfrak Q_{D,L}(c)|
   \ll_\varepsilon \frac D H X^\varepsilon,}
   \tag{SDC}
   \]

   with the absolute value outside the entire \((\tau,d,h)\)-sum.  Since
   (H\asymp DX^{-1/4}\), this is target-sized.  Moreover
   (L\le H\le D/H\) throughout the active range
   (D\le X^{1/2}\), so (2.11) is also target-sized.

Condition (SDC) is the weakest natural paired-offset correlation statement:
it uses the actual character, spatial profile, Vaaler profile, and odd
kernel, and takes no absolute value over a product fiber.  It is equivalent
to bounding the centered M1 block.  An estimate that takes absolute values
separately in \(\tau\), or replaces the character-weighted sums by the
symmetric difference cardinality, is strictly stronger and is not supplied
by the pairing identity.

## 3. Proof and derivation

### 3.1 Nearest-product convention

From the definition of (n_X(d)),

\[
-\frac d2\le X-n_X(d)<\frac d2.
\tag{3.1}
\]

The lower endpoint is included and the upper endpoint is excluded.  Hence,
for a product (n<X) at distance (t=X-n>0\), its divisor condition is

\[
d\mid n,\qquad d>2t,
\tag{3.2}
\]

whereas for (n>X) at distance (t=n-X>0\), it is

\[
d\mid n,\qquad d\ge2t.
\tag{3.3}
\]

At equality (d=2t), the kernel argument is (-1/2\), so (2.2) makes the
contribution zero.  Thus strict (d>2t) may be used on both sides in every
centered formula without changing its value.

### 3.2 Integer center

Let (X=N\in\mathbb Z).  The product (n=N) contributes zero because its
kernel argument is (0\).  The remaining products are (N-t) and (N+t),
(t\in\mathbb Z_{\ge1}\), and (3.2)--(3.3) give

\[
\mathcal M_{D,L}(N)=
\sum_{t\ge1}
\left\{
\sum_{\substack{d\mid N-t\\d>2t}}\chi_4(d)w_D(d)\mathcal V(t/d)
-\sum_{\substack{d\mid N+t\\d>2t}}\chi_4(d)w_D(d)\mathcal V(t/d)
\right\}.
\tag{3.4}
\]

For a lower divisor, (N-t=dm\), and periodicity gives

\[
\mathcal V(t/d)=\mathcal V(N/d-m)=\mathcal V(N/d).
\tag{3.5}
\]

For an upper divisor, (N+t=dm\), and oddness plus periodicity gives

\[
\mathcal V(t/d)=\mathcal V(m-N/d)=-\mathcal V(N/d).
\tag{3.6}
\]

The minus sign in (3.4) and the minus sign in (3.6) cancel.  This proves
the reinforcing form of (1.1) for integer centers.

### 3.3 Half-integer center

Let (X=c=N+1/2\).  The exact offset lattice is
\(\tau=k+1/2\), (k\ge0\), and the products are

\[
c-\tau=N-k,\qquad c+\tau=N+1+k.
\tag{3.7}
\]

There is no central integer product.  Equations (3.2)--(3.3) yield (2.10).
The same congruence calculation gives

\[
d\mid c-\tau\Longrightarrow
\mathcal V(\tau/d)=\mathcal V(c/d),
\tag{3.8}
\]

\[
d\mid c+\tau\Longrightarrow
\mathcal V(\tau/d)=-\mathcal V(c/d).
\tag{3.9}
\]

Again the upper minus sign is canceled, proving (1.1).  Notice also that

\[
\mathscr D_c^-(\tau)\cap\mathscr D_c^+(\tau)=\varnothing:
\tag{3.10}
\]

membership in the intersection would imply (d\mid2\tau), which is
impossible when (d>2\tau>0\).  Thus there is not even a same-denominator
matching on which oddness could act.

For fixed (d), the nearest multiple of (d) to (c) supplies exactly
one incidence in the plus expression in (1.1), except for an exact product
or a half-way tie.  Exact products give \(\mathcal V(0)=0\), and ties give
\(\mathcal V(1/2)=0\).  This proves the final equality in (1.1).

### 3.4 Generic real center and the two unequal offset sets

Let (X=N+\theta\), where (0<\theta<1\) and \(\theta\ne1/2\).  The actual
positive distances from (X) to integer products are

\[
\mathcal T_-(X)=\{k+\theta:k\ge0\},\qquad
\mathcal T_+(X)=\{k+1-\theta:k\ge0\}.
\tag{3.11}
\]

They are unequal; writing a common real offset (t) on both sides would be
incorrect.  Put

\[
c=N+\frac12,\qquad \sigma=\theta-\frac12,
\qquad \tau=k+\frac12.
\tag{3.12}
\]

Then the lower and upper distances are respectively \(\tau+\sigma\) and
\(\tau-\sigma\), and the exact product pairing is

\[
\begin{aligned}
\mathcal M_{D,L}(X)=\sum_{k\ge0}\bigg\{&
\sum_{\substack{d\mid N-k\\d>2(\tau+\sigma)}}
 \chi_4(d)w_D(d)\mathcal V((\tau+\sigma)/d)\\
&-\sum_{\substack{d\mid N+1+k\\d\ge2(\tau-\sigma)}}
 \chi_4(d)w_D(d)\mathcal V((\tau-\sigma)/d)
\bigg\}.
\end{aligned}
\tag{3.13}
\]

This is the requested real-center lattice convention.  The products in a
pair are separated by (2\tau=2k+1\), but their distances from the real
center differ by (2\sigma=2\theta-1\).

Relative to the centered cutoff (d>2\tau\), integrality shows that the
only possible cutoff discrepancy is (d=2\tau\).  The centered kernel is
zero there.  Its shifted value is bounded by (2.3) by

\[
\left|\mathcal V\left(\frac{\tau\pm\sigma}{2\tau}\right)
-\mathcal V(1/2)\right|
\ll \frac{L|\sigma|}{2\tau}.
\tag{3.14}
\]

More efficiently, (2.6) and the mean-value theorem include both the
argument and cutoff seams at once:

\[
\begin{aligned}
|\mathcal M_{D,L}(X)-\mathfrak Q_{D,L}(c)|
&=\left|\sum_d\chi_4(d)w_D(d)
 \{\mathcal V(X/d)-\mathcal V(c/d)\}\right|\\
&\le \|\mathcal V'\|_\infty |X-c|
 \sum_d\frac{|\chi_4(d)w_D(d)|}{d}\\
&\ll L|\sigma|\mathscr H_D.
\end{aligned}
\tag{3.15}
\]

This proves (2.11).  No spatial-profile or Vaaler-profile mismatch occurs:
the same (w_D\), (H\), \(v_L\), and \(\Phi\) from the original (X)-block
are retained when only the phase center is moved.

### 3.5 Hard top profile

For the actual hard top band,

\[
w_0(d)={\bf1}_{d\le y}W(d/y),\qquad y=\lfloor\sqrt X\rfloor,
\tag{3.16}
\]

and its support lies in \([y/2,y]\).  Therefore

\[
\mathscr H_y\ll\sum_{y/2\le d\le y}\frac1d\ll1.
\tag{3.17}
\]

The proof never differentiates (w_0\), so the jump at (d=y\) causes no
extra term.  Since (L\le H_y\le yX^{-1/4}\le X^{1/4}\), the generic-center
error is (O(X^{1/4})\).  If (X=y^2\), then (X\) is an integer center and
the error is zero; the endpoint denominator (d=y\) is an exact product and
its kernel value is zero.  If (X\) is not a square, (d=y\) is simply
assigned to its unique lower or upper product pair, with no endpoint
correction.

### 3.6 Capacity of the pairing

The accepted frequency-first size before the residual improvement is
essentially (D/L\), whereas the target scale is

\[
\frac D H\asymp X^{1/4}.
\tag{3.18}
\]

For (L<H\), the missing saving is the factor

\[
\frac{D/L}{D/H}=\frac HL.
\tag{3.19}
\]

Equations (3.5)--(3.10) show that the pairing supplies none of it: the two
divisor sets are disjoint and both sides enter with the same reciprocal
phase sign.  Any proof of (SDC) must therefore obtain cancellation among
different denominators or different offsets using the actual
\(\chi_4(d)\), profile, and oscillatory kernel.  Oddness plus rank pairing
alone is algebraically neutralized by divisibility.

## 4. First doubtful or unproved step

All lattice, endpoint, tie, stability, and reinforcement identities above
are exact.  The first unproved step is (SDC).  No estimate in the authorized
packet bounds its centered character-weighted plus-incidence sum by
\(D/H\) throughout the residual corridor.  In particular, (1.1) shows that
calling the two sides a ``divisor-set discrepancy'' does not itself provide
cancellation: after the congruence is used, the apparent difference is a
sum.  A new cross-denominator correlation theorem is still required.

## 5. Required controls and outcomes

### Integer control: pass

The offset lattice is \(\mathbb Z_{\ge1}\); the central product is killed by
\(\mathcal V(0)=0\).  Lower cutoffs are strict and upper cutoffs are weak,
but the equality term is killed by \(\mathcal V(1/2)=0\).  Formula (3.4) is
exact.

### Half-integer control: pass

The offset lattice is \(\mathbb Z_{\ge0}+1/2\), not the integers.  There is
no central product.  The same tie convention and zero at (1/2\) give the
strict common cutoff, and (3.8)--(3.9) prove reinforcement.

### Generic-real control: pass

The two actual offset sets are (3.11), so exact reflection about (X\) is
impossible.  Rank pairing about (c=N+1/2\) gives (3.13), and the entire
lattice/argument mismatch is (O(L|\theta-1/2|)\) by (3.15).  No false
assumption that (2X\) is integral is used.

### Divisor-overlap control: fails in the direction needed for cancellation

The paired centered divisor sets have empty intersection by (3.10).  Even
formally identical kernel arguments do not pair the same denominator.
After imposing divisibility, both sides have the same sign as in (1.1).
This is a rigorous no-go result for termwise opposite-offset cancellation.

### Profile and character control: pass

Every identity retains \(\chi_4(d)w_D(d)\) exactly.  No character is made
absolute inside the target correlation, and neither the spatial profile nor
the Vaaler profile is frozen or shifted.

### Hard-top control: pass

The only analytic input is the harmonic mass (3.17), so the hard jump at
(d=y\) is harmless.  Exact squares, nonsquares, the endpoint denominator,
and the maximal height (H_y\asymp X^{1/4}\) are all covered.

### Numerical-control accounting

No numerical experiment was used.  The conclusions are algebraic and
analytic identities, not finite-data evidence.

## 6. Dependencies and exact artifacts used

Only the files authorized by the task brief were read:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-m1-cross-product-offset-pairing/briefs/blind_offset_pairing_identity.md`.

No Round-11 report, other Round-12 report, web source, or numerical artifact
was used.

## 7. Recommended state effect

1. **Promote the half-lattice stability reduction:** arbitrary real (X)
   differs from the correctly centered integer/half-integer M1 block by
   (O(L)\), uniformly for all active profiles and the hard top band.
2. **Promote the offset-pairing no-go:** the opposite-side divisor sets are
   disjoint, and oddness plus the divisibility congruence makes their
   contributions reinforce.  Naive rank pairing cannot provide the missing
   (H/L) saving.
3. **Retain `M9-M1-cross-product-odd-kernel-discrepancy` as open, but revise
   its next action:** the precise remaining sufficient estimate is (SDC),
   equivalently the centered character-weighted plus-incidence correlation
   (1.1).  It must use cancellation across distinct denominators or offsets,
   not same-denominator set stability.
4. **Do not promote `M9-M1`, `M9-M1-top-endpoint-signed-cone`, `M9`, or the
   final target.**  This report proves an exact reduction and a route
   obstruction, not the required correlation estimate.
