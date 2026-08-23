# Round 122 conductor adjudication: localized complement and exact self-return

Campaign: `m9-m1-near-square-complementary-divisor-gate`

Starting graph SHA-256:
`3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

## 1. Decision

Round 122 proves a strict target-scale reduction of the exact Round-121
lower discrepancy, but it does not estimate the remaining signed
functional.  The one-sided difference wavelet has a uniform three-range
Fourier envelope.  This deletes the far Fourier tail, the complete
central index window, all sufficiently high two-adic increments, and the
odd positive-character central divisor correction.  Every deletion costs
at most (O_{\varepsilon,\delta}(RX^\varepsilon)).

The complementary-divisor involution is exact for every two-adic
valuation, residue branch, square fixed point, and hard (d=y) boundary.
It nevertheless supplies no power saving.  On the odd
(3\pmod 4) branch it returns the original truncated coefficient exactly;
on the odd (1\pmod 4) branch it leaves one half of the full
(r_2/4) coefficient; and on unresolved even branches it retains the
full coefficient and its exact complement jointly.  Estimating the full
coefficient at the needed scale would import the circle problem.

Accordingly, promote the exact reduction and the scoped involution
self-return.  Keep `M9-M1-global-lower-radial-signed-estimate` open and
freeze this complementary-divisor route unless a genuinely joint signed
inequality is supplied.

## 2. Uniform wavelet localization

Put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

and retain

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{k\in\mathbb Z}D_N(k)W(k),\qquad
 W(k)=\widehat J(k)-\widehat J(k+1).
\tag{122.J1}
\]

The removable-pole kernel

\[
 G(t)=J(t)(1-e(-t))
 =\eta(yt)V_{\rm low}(4R^2t^2)\frac{1-e(-t)}
\]

satisfies, for every fixed (j\geq1),

\[
 \|G\|_1\ll R^{-1},\qquad
 \|G^{(j)}\|_1\ll_j y^{j-1}.
\tag{122.J2}
\]

Hence, for every fixed (A\geq1),

\[
 |W(k)|\ll_A\frac1{R+|k|}
 \left(1+\frac{|k|}{y}\right)^{-A},
\tag{122.J3}
\]

and in particular

\[
 \sum_k|W(k)|\ll\log(2X),\qquad
 \sum_k|kW(k)|\ll y.
\tag{122.J4}
\]

Since the exact floor remainder gives (|D_N(k)|\leq y), for fixed
(0<\delta<1/8) and (K_\delta=yX^\delta), sufficiently many integrations
by parts give

\[
 \sum_{|k|>K_\delta}|D_N(k)W(k)|
 =O_{A,\delta}(RX^{-A}).
\tag{122.J5}
\]

All (N+k) traversed in the retained oriented intervals are positive.
The divisor bound and the discrepancy recurrence give

\[
 \sum_{|k|\leq R}|D_N(k)W(k)|
 \ll_\varepsilon RX^\varepsilon.
\tag{122.J6}
\]

## 3. High valuations and the centering seam

Let

\[
 c_y=\sum_{d\leq y}\frac{\chi_4(d)}d,qquad
 \widetilde D_N(k)=D_N(k)+kc_y,qquad
 A_0=\lceil\log_2R\rceil.
\]

The full series has

\[
 \sum_k kW(k)=\sum_k\widehat J(k)=J(0)=0.
\tag{122.J7}
\]

After localization its centering leakage is still target-safe because

\[
 \sum_{|k|>K_\delta}|kW(k)|
 \ll_M y^{M-1}K_\delta^{2-M}.
\tag{122.J8}
\]

The high-valuation projection of (\widetilde D_N(k)) is the oriented
cumulative sum of those (A_y(N+j)) with
(v_2(N+j)\geq A_0).  An interval of length (|k|) contains at most
(1+|k|/2^{A_0}) such integers, so

\[
 \sum_{|k|\leq K_\delta}
 \left|\widetilde D_{\geq A_0}(k)W(k)\right|
 \ll_\varepsilon X^\varepsilon
 \left(\log X+\frac{y}{2^{A_0}}\right)
 \ll_\varepsilon RX^\varepsilon.
\tag{122.J9}
\]

The low/high projection and central-(k) deletions overlap.  The exact
identity

\[
 \widetilde D_{<A_0}=D_N+kc_y-\widetilde D_{\geq A_0}
\tag{122.J10}
\]

prices that overlap once; no terminal-index valuation is substituted for
the valuation of every cumulative increment.

## 4. Exact complementary-divisor table

For (m=2^an>0), (n) odd, put

\[
 a(n)=\sum_{d\mid n}\chi_4(d)=\frac{r_2(m)}4,qquad
 T_z(n)=\sum_{\substack{q\mid n\\q<z}}\chi_4(q).
\]

Only odd divisors contribute.  Complementing the omitted divisors by
(d\mapsto n/d=m/(2^ad)), not by (m/d), gives

\[
 \boxed{A_y(2^an)=a(n)-\chi_4(n)T_{n/y}(n).}
\tag{122.J11}
\]

The strict inequality in (T_{n/y}) is forced by the inclusive hard
cutoff (d\leq y).  If (z=n/y\leq y), set

\[
 C_-(n)=\sum_{\substack{d\mid n\\z\leq d\leq y}}\chi_4(d),
\]

and if (z>y), set

\[
 C_+(n)=\sum_{\substack{d\mid n\\y<d<z}}\chi_4(d).
\]

Then for (chi_4(n)=1),

\[
 2A_y(n)=
 \begin{cases}
  a(n)+C_-(n),&n\leq y^2,\\
  a(n)-C_+(n),&n>y^2,
 \end{cases}
\tag{122.J12}
\]

while for (chi_4(n)=-1),

\[
 a(n)=0,\qquad A_y(n)=T_{n/y}(n),
\tag{122.J13}
\]

and the corresponding central character sum is zero.  At (n=y^2),
the odd fixed point contributes once:

\[
 2A_y(y^2)=a(y^2)+\chi_4(y).
\tag{122.J14}
\]

For every (a\geq1) in the localized window, (n<y^2).  Its threshold
is (n/y\asymp y/2^a), and the lower tail is empty when (n\leq y).
Thus the even central band is generally wide and is not covered by the
odd near-square estimate.

## 5. The safe odd central correction and exact survivor

On the odd positive-character branch define

\[
 \Gamma(n)=
 \begin{cases}
 C_-(n),&n<y^2,\\
 \chi_4(y),&n=y^2,\\
 -C_+(n),&n>y^2,
 \end{cases}
\]

and set it to zero off that branch.  Every central divisor occurrence for
(n=N+j), (|j|\leq K_\delta), maps injectively to an ordered factor
pair in a box of side (O(1+X^\delta)) about ((y,y)).  Hence

\[
 \sum_{|j|\leq K_\delta}|\Gamma(N+j)|
 \ll(1+X^\delta)^2.
\tag{122.J15}
\]

If (E(k)=\mathcal I_k\Gamma) is the oriented cumulative correction,
then (122.J4) gives

\[
 \sum_{|k|\leq K_\delta}|E(k)W(k)|
 \ll X^{2\delta}\log X
 \ll_\varepsilon RX^\varepsilon.
\tag{122.J16}
\]

Define the remaining increment by

\[
 \mathscr V_\delta(2^an)=
 \begin{cases}
  \frac12a(n),&a=0,\ \chi_4(n)=1,\\
  T_{n/y}(n),&a=0,\ \chi_4(n)=-1,\\
  a(n)-\chi_4(n)T_{n/y}(n),&1\leq a<A_0,\\
  0,&a\geq A_0.
 \end{cases}
\tag{122.J17}
\]

With (S(k)=\mathcal I_k\mathscr V_\delta), the exact overlap identity is

\[
 S(k)=D_N(k)+kc_y-\widetilde D_{\geq A_0}(k)-\frac12E(k).
\tag{122.J18}
\]

Equations (122.J5)--(122.J10) and (122.J15)--(122.J18) prove

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}W(k)\mathcal I_k\mathscr V_\delta
 +O_{\varepsilon,\delta}(RX^\varepsilon).}
\tag{122.J19}
\]

This is the smallest certified survivor.  It has absolute capacity
(y=R^2).  Equation (122.J13) makes the odd negative-character branch an
exact self-return.  Equations (122.J11)--(122.J12) insert the full circle
coefficient and its complement exactly once; recombining them restores the
original (d\leq y) cone.  No target estimate follows.

## 6. Repairs and report reconciliation

The candidate required seven explicit repairs before promotion:

1. use (\ll), not a literal equality, when replacing powers of
   (y=\lfloor\sqrt X\rfloor) by powers of (X);
2. place complex sums inside a modulus when claiming an upper bound;
3. include the central-window overlap identity for the low/high
   cumulative projections;
4. complement even integers through their odd part (n), and record the
   wide (a\geq1) central band;
5. state the equality (n=y^2), hard (d=y), and square fixed-point
   conventions explicitly;
6. estimate the odd central correction in localized cumulative form,
   rather than inferring a global conclusion from a truncated pre-Abel
   sum; and
7. state the exact piecewise survivor and its additional
   (-E(k)/2) overlap term.

The statement-only report independently proved the uniform envelope and
all boundary identities, and its supersession note verifies the repaired
cumulative argument.  The selected-context discovery report proves both
the (D_NW) localization and an independent (A_y\widehat J)
localization, and exposes the literal full-product self-return.  The
hostile report proves the high-valuation and factor-pair packages and gives
the exact survivor.  Its second-stage audit verifies every repaired line.

This agreement is theorem-by-theorem, not by vote.  No numerical test or
new external source is used.

## 7. Scope and continuation

Promote (122.J2)--(122.J19) as a reduction and scoped obstruction.  Retain
open:

- `M9-M1-global-lower-radial-signed-estimate` and therefore GAR;
- both direct blockwise M1 parents and `M9-M1`;
- hard TOP, balanced, and unbalanced M2 parents and `M9-M2`;
- endpoint uniformity, `M9`, the quarter theorem, and every improved
  exponent.

A lawful continuation on the lower route would require a genuinely joint
signed estimate for (122.J19).  Another complementary inversion,
full-(r_2) completion followed by a circle bound, residuewise or
valuationwise norms, or Fourier/Abel inversion is now an audited return.
Under the August 21 strategy, this failed noninvertible gate parks GAR at
its exact functional and rotates the next core round back to the mandatory
M2 conjunction.
