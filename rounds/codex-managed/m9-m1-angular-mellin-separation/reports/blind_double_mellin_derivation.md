# Blind double-Mellin derivation of the exact M1 angular symbol

- Campaign: `m9-m1-angular-mellin-separation`
- Round: `15`
- Task: `blind_double_mellin_derivation`
- Role: statement-only exact deriver
- Graph SHA-256 supplied in the brief: `aa33b1c414e135f96f912b34ec17acda79c3cf5cb68a73c4fb706bd393993251`
- Isolation: no other Round-15 report was read.

## 1. Result

The exact active M1 angular coefficient has a double-Mellin separation with
no suppressed floor, parity, product-cutoff, or endpoint factor.  For each
actual scale (D_j=2^{-j}y), (y=\lfloor\sqrt X\rfloor), put

\[
 H_j=\lfloor D_jX^{-1/4}\rfloor,
 \qquad N_X=\lfloor16\sqrt X\rfloor .
\]

If (u) is the spatial Mellin variable and (v) the Vaaler-height Mellin
variable, then grouping by (n=hq) produces exactly the twisted divisor
coefficient

\[
 \tau_{\chi_4,u+v}(n)
 =\sum_{\substack{hq=n\\q\ {\rm odd}}}\chi_4(q)h^{-(u+v)}.
\]

The associated radial sum is

\[
 \mathcal R_X(u,v)
 :=\sum_{n\leq N_X}
 \tau_{\chi_4,u+v}(n)n^{-3/4+u/2}e(\sqrt{Xn}).
\tag{1.1}
\]

All interior (j\geq1) contours are absolutely convergent.  The sole
non-absolutely-convergent contour is the spatial Mellin contour for the
one-sided top profile.  Its transform is an exact Perron kernel (1/u)
plus a rapidly decreasing remainder.  The symmetric contour limit gives
the required endpoint half weight.  Thus the top jump does not alter the
coefficient, but it replaces an ordinary (L^1) contour estimate by one
Perron/Hilbert maximal estimate.  Absolute truncation at height (T)
costs (O(\log(2+T))).  Separately, the already accepted one-sided
stationary transform contributes only (O_W(\log^2(2X))) to the physical
M1 aggregate.

The Dirichlet-series identity is

\[
 \boxed{
 \sum_{n\geq1}\frac{\tau_{\chi_4,z}(n)}{n^s}
 =\zeta(s+z)L(s,\chi_4)}
\tag{1.2}
\]

with absolute convergence precisely in the joint half-plane

\[
 \Re s>1,\qquad \Re(s+z)>1.
\tag{1.3}
\]

This factorization alone gives no saving for (1.1), because (1.1) is a
finite additively oscillatory square-root radial sum rather than its
ordinary Dirichlet series.

## 2. Exact statement and hypotheses

Use the accepted profile (W\in C_c^\infty((0,\infty))), supported in
([1/2,4/3]), with (W(t)=1) for (2/3\leq t\leq1).  Set

\[
 W_j(t)=W(t)\quad(1\leq j\leq J),
 \qquad
 W_+(t)=W(t){\bf1}_{0<t<1},
\tag{2.1}
\]

where Mellin inversion of (W_+) at (t=1) is understood as the average
of its two one-sided limits.  Hence (W_+^*(1)=1/2).  This is exactly the
star in the top term of the accepted coefficient.  At the smooth support
edges of every interior profile the value is zero, so the star is
immaterial there.

For (0<t<1), use the audited Vaaler function

\[
 \Phi(t)=\pi t(1-t)\cot(\pi t)+t,
\]

with (\Phi(0)=1), (\Phi(1)=0), and
(\Phi'(0)=\Phi'(1)=0).  Extend it by

\[
 \phi(t)=
 \begin{cases}
 \Phi(t),&0<t<1,\\
 0,&t\geq1.
 \end{cases}
\tag{2.2}
\]

The value at (t=1) is zero.  For every positive integer (h), this gives
the exact, endpoint-free identity

\[
 {\bf1}_{h\leq H_j}\Phi\!\left(\frac h{H_j+1}\right)
 =\phi\!\left(\frac h{H_j+1}\right).
\tag{2.3}
\]

Indeed (h=H_j+1) has coefficient (\Phi(1)=0), while all larger (h)
lie beyond the support.  Thus the scale is exactly (H_j+1), with
(H_j=\lfloor D_jX^{-1/4}\rfloor); neither (H_j) nor (H_j+1) may be
replaced by an asymptotic surrogate.

Take Mellin transforms in the convention

\[
 \widehat W(u)=\int_0^\infty W(t)t^{u-1}\,dt,
 \quad
 \widehat W_+(u)=\int_0^1 W(t)t^{u-1}\,dt,
 \quad
 \widehat\phi(v)=\int_0^1\Phi(t)t^{v-1}\,dt.
\tag{2.4}
\]

The first two transforms are entire.  The last is holomorphic for
(\Re v>0).  Fix any (a>0), (b>0).  For (j\geq1), define

\[
 \mathcal I_j(X)
 :=\frac1{(2\pi i)^2}
 \int_{(a)}\!\int_{(b)}
 \widehat W(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u
 (H_j+1)^v\mathcal R_X(u,v)\,dv\,du.
\tag{2.5}
\]

For the top scale (D_0=y), define the symmetric Perron limit

\[
 \mathcal I_0^*(X)
 :=\lim_{T\to\infty}\frac1{(2\pi i)^2}
 \int_{(b)}\int_{a-iT}^{a+iT}
 \widehat W_+(u)\widehat\phi(v)
 \left(\frac{D_0}{2\sqrt X}\right)^u
 (H_0+1)^v\mathcal R_X(u,v)\,du\,dv.
\tag{2.6}
\]

Then the exact angular radial expression in GAR is

\[
 \boxed{
 \sum_{n\leq N_X}\mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 =\mathcal I_0^*(X)+\sum_{j=1}^J\mathcal I_j(X).}
\tag{2.7}
\]

Equivalently, before grouping by (n), the (j)-th term is

\[
 \sum_{\substack{h,q\geq1\\q\ {\rm odd}\\hq\leq N_X}}
 \chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})
 \phi\!\left(\frac h{H_j+1}\right)
 \left[W_j\!\left(\frac{2\sqrt{hX/q}}{D_j}\right)\right]^*,
\tag{2.8}
\]

with (W_0=W_+).  Formula (2.8) displays the odd (q), the product cutoff,
the actual floors, and the endpoint star without abbreviation.

The smallest exact twisted-radial estimate implying GAR is therefore the
single real-part estimate

\[
 \boxed{
 \operatorname {Re}\!\left\{e(1/8)
 \left(\mathcal I_0^*(X)+\sum_{j=1}^J\mathcal I_j(X)\right)\right\}
 \ll_\varepsilon X^\varepsilon.}
\tag{TR-GAR}
\]

By (2.7), (TR-GAR) is equivalent to GAR, not a stronger blockwise claim.
It keeps cancellations between scales and between Mellin modes.

A more modular but stronger sufficient interface is:

1. a uniform (X^\varepsilon) bound for (\mathcal R_X(u,v)) on
   (\Re u=a), (\Re v=b), sufficient for all rapidly decaying interior
   and smooth-top kernels; and
2. an (X^\varepsilon) maximal bound for the one remaining (1/u) Perron
   integral in the top scale.

For scale-neutral bookkeeping one may take
(a=b=1/\log(2X)).  Then all real scale powers in (2.5)--(2.6) are
(O(1)), while the finite number (J+1=O(\log X)) of scales and the
small-(b) Mellin norm contribute only logarithms.

## 3. Proof or derivation

### 3.1 Height Mellin inversion and decay

For (b>0), Mellin inversion applied to (2.2) gives, at every positive
integer (h),

\[
 \phi\!\left(\frac h{H_j+1}\right)
 =\frac1{2\pi i}\int_{(b)}
 \widehat\phi(v)(H_j+1)^vh^{-v}\,dv.
\tag{3.1}
\]

There is no half weight at (h=H_j), because that point lies strictly
inside (0<t<1).  There is also no correction at (h=H_j+1), because
both sides are zero.

The endpoint expansions of the explicit cotangent formula show that
(\Phi) has one-sided derivatives of every order at (0) and (1), with
(\Phi(1)=\Phi'(1)=0).  Integrating by parts three times on a fixed line
(\Re v=b>0) gives

\[
 \widehat\phi(v)
 =\frac1{v(v+1)}\int_0^1\Phi''(t)t^{v+1}\,dt
 \ll_b(1+|\Im v|)^{-2},
\tag{3.2}
\]

and one further evaluation of the last integral at (t=1) gives the
sharper bound

\[
 \widehat\phi(b+i\nu)\ll_b(1+|\nu|)^{-3}.
\tag{3.3}
\]

Thus the height contour is absolutely integrable.  Near (v=0),
(\widehat\phi(v)=v^{-1}+O(1)), reflecting (\Phi(0)=1).  This is why a
fixed (b>0), or (b=1/\log(2X)>0), must be retained rather than writing
an unaudited contour through (v=0).

### 3.2 Spatial inversion and all scale powers

For (j\geq1), ordinary Mellin inversion gives

\[
 W\!\left(\frac{2\sqrt{hX/q}}{D_j}\right)
 =\frac1{2\pi i}\int_{(a)}\widehat W(u)
 \left(\frac{D_j}{2\sqrt X}\right)^u
 h^{-u/2}q^{u/2}\,du.
\tag{3.4}
\]

The transform (\widehat W(a+i\mu)) is rapidly decreasing in (mu) on
every fixed vertical line.  For (j=0), the same formula holds with
(\widehat W_+), interpreted as the symmetric limit.  It takes the
correct half value when (2\sqrt{hX/q}=D_0=y).

Multiplying (3.4) by (3.1), then using (n=hq), gives

\[
 h^{-u/2}q^{u/2}h^{-v}
 =n^{u/2}h^{-(u+v)}.
\tag{3.5}
\]

After the pre-existing factor (n^{-3/4}), the radial power is exactly
(n^{-3/4+u/2}), and summing over (h\mid n) gives
(\tau_{\chi_4,u+v}(n)).  This proves every scale power in (2.5)--(2.8).

The cutoff (n\leq16\sqrt X) is also forced before Mellin inversion.  On
the support of any active profile,
(d=2\sqrt{hX/q}\geq D_j/2), while
(h\leq H_j\leq D_jX^{-1/4}).  Therefore

\[
 n=hq=\frac{4h^2X}{d^2}
 \leq\frac{16h^2X}{D_j^2}
 \leq16\sqrt X.
\tag{3.6}
\]

Since (n) is integral, this is exactly (n\leq N_X).

### 3.3 Dirichlet-series factorization

For a general complex (z), define

\[
 \tau_{\chi_4,z}(n)
 =\sum_{\substack{hq=n\\q\ {\rm odd}}}\chi_4(q)h^{-z}.
\]

If (\Re s>1) and (\Re(s+z)>1), Tonelli's theorem applies because

\[
 \sum_{h,q\geq1}|\chi_4(q)|
 h^{-\Re(s+z)}q^{-\Re s}<\infty.
\]

Consequently

\[
 \begin{aligned}
 \sum_{n\geq1}\tau_{\chi_4,z}(n)n^{-s}
 &=\sum_{h,q\geq1}\chi_4(q)h^{-z}(hq)^{-s}\\
 &=\left(\sum_{h\geq1}h^{-(s+z)}\right)
   \left(\sum_{q\geq1}\chi_4(q)q^{-s}\right)\\
 &=\zeta(s+z)L(s,\chi_4).
 \end{aligned}
\tag{3.7}
\]

Writing (\(q\)) as odd is equivalent to summing all (q), because
(\chi_4(q)=0) for even (q).  The two inequalities in (1.3) are the
correct absolute-convergence hypotheses for this Mellin convention.

### 3.4 Interchanges

The original sum (2.8) is finite.  For (j\geq1), on
(\Re u=a>0), (\Re v=b>0),

\[
 |\tau_{\chi_4,u+v}(n)|
 \leq\sum_{h\mid n}h^{-(a+b)}\leq d(n).
\]

The finite radial sum is therefore uniformly bounded in the imaginary
parts by its absolute divisor majorant.  The rapid decay of
(\widehat W), the (O((1+|\nu|)^{-3})) decay of
(\widehat\phi), and the finite (j)-sum justify Fubini and all
interior interchanges absolutely.

For (j=0), first truncate the (u)-contour at height (T).  At finite
(T), every sum and the (v)-integral may be interchanged.  Since the
original ((h,q))-sum is finite, let (T\to\infty) term by term in the
one-dimensional Mellin inversion.  The limit is the profile value away
from (t=1) and the half value at (t=1).  This proves (2.6)--(2.7)
without an unjustified absolute convergence claim.

### 3.5 Exact top-jump separation

Integration by parts uses (W(1)=1), (W=0) near (0), and gives

\[
 \boxed{
 \widehat W_+(u)=\frac1u
 -\frac1u\int_0^1W'(t)t^u\,dt.}
\tag{3.8}
\]

Because (W') is smooth and supported away from both (0) and (1), the
second term is rapidly decreasing on vertical lines.  Hence (1/u) is
the complete non-smooth contribution of the one-sided top.  Its symmetric
inverse is the sharp cone with half weight at its boundary.

On (|\Im u|\leq T), taking absolute values in the (1/u) part costs

\[
 \int_{-T}^T\frac{dt}{|a+it|}
 \ll\log\!\left(2+\frac T a\right).
\tag{3.9}
\]

There is no uniform (T\to\infty) conclusion from a mere pointwise bound
for (\mathcal R_X); the needed statement is a maximal Perron/Hilbert
bound for that single contour.  This is the precise analytic loss caused
by the jump.  It is distinct from the already accepted physical
one-sided-transform error (O_W(\log^2(2X))), which is target-sized after
restoring the (X^{1/4}) prefactor in the M1 aggregate.

## 4. First doubtful or unproved step

No estimate of size (X^\varepsilon) for (\mathcal R_X(u,v)), its
scale-weighted double integral, or the top maximal Perron integral is
proved here.  This is the first genuinely unproved step.  The ordinary
Dirichlet-series factorization (3.7) cannot by itself be inserted into the
finite radial sum (1.1); doing so would require a separately justified
summation formula or functional equation with uniform complex-shift and
truncation control.  It is also not proved here that such a functional
equation avoids returning to the original reciprocal M1 sum.

Thus (TR-GAR) is an exact smaller-coordinate restatement of GAR, not a
proof of GAR or M9-M1.

## 5. Required controls and outcomes

### Scale-power control: pass

Direct substitution (q=n/h) gives
(h^{-u/2}q^{u/2}h^{-v}=n^{u/2}h^{-(u+v)}).  This verifies both the twist
(u+v) and the radial exponent (-3/4+u/2); neither may be replaced by
(v) alone.

### Lowest-height and floor control: pass

When (H_j=1), (2.3) gives the actual (h=1) coefficient
(\Phi(1/2)), the (h=2) coefficient (\Phi(1)=0), and zero thereafter.
Thus the representation remains exact at the lowest active scale and does
not use (H_j\asymp D_jX^{-1/4}) in place of the floor.

### Product, parity, and character control: pass

Equation (2.8) retains (hq\leq N_X), (q) odd, and (\chi_4(q)).  The
Mellin separation does not prove the false unsigned or adversarial
analogue: the only arithmetic cancellation still resides in the signed
coefficient (\tau_{\chi_4,z}).

### Top endpoint control: pass with one declared conditional contour

At (2\sqrt{hX/q}=y), symmetric inversion of (3.8) gives (1/2), exactly
the star.  Away from that equality it gives the full one-sided value.  The
remaining (1/u) contour is deliberately not called absolutely
convergent.

### Angular-asymmetry control: pass

The mode kernel contains the exact factors
((D_j/(2\sqrt X))^u(H_j+1)^v) before the (j)-sum.  Hence Mellin
inversion reconstructs the divisor-angle multiplier rather than the false
(r_2(n)/4) collapse rejected in Round 14.

### Numerical and source controls

No numerical experiment and no web source were used.  The derivation is
algebraic and uses only already accepted internal profile and Vaaler
interfaces.

## 6. Dependencies and exact artifacts used

Only the brief-authorized files were read:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`;
- `rounds/codex-managed/m9-m1-angular-mellin-separation/briefs/blind_double_mellin_derivation.md`.

No other Round-15 report, shared synthesis, validation matrix, proof draft,
or unlisted source was read.  No shared proof state was edited.

## 7. Recommended state effect

1. **Promote after conductor verification:** record the exact
   double-Mellin identity (2.5)--(2.8), the twisted divisor parameter
   (z=u+v), the product cutoff, floor scales, parity, and endpoint star
   as `proved_internal` evidence refining
   `M9-M1-global-angular-recombination`.
2. **Promote the arithmetic identity:** record (3.7) with the joint
   absolute-convergence half-plane (1.3).
3. **Create or retain an open twisted-radial interface:** (TR-GAR) is the
   weakest exact mode-space estimate implying GAR.  A useful decomposed
   version consists of the rapidly weighted interior mode estimate plus
   the single top (1/u) maximal Perron estimate.
4. **Retain all target statuses:** GAR, RCS, blockwise M9-M1, M9, and the
   Gauss target remain open.  The Dirichlet-series product does not license
   a functional-equation estimate without a separate source and
   uniformity audit.
5. **Record the top-jump warning:** a pointwise uniform bound for
   (\mathcal R_X(u,v)) controls the absolutely integrable mode kernels but
   does not, by itself, control the (T\to\infty) (1/u) Perron contour.


