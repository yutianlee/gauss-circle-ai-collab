# Round 122 synthesis: sharp localization, strict deletions, and complement self-return

Campaign: `m9-m1-near-square-complementary-divisor-gate`

Starting graph SHA-256:
`3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

Resulting graph SHA-256:
`d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`

## 1. Conductor decision

Round 122 proves a uniform localization and four target-safe packages for
the exact Round-121 lower discrepancy.  It also proves every branch of the
near-square complementary-divisor identity.  The involution does not
produce a signed power saving: one odd residue branch is an exact
self-return, while the other leaves a full circle coefficient.  The lower
radial estimate and every downstream target remain open.

The promoted content is therefore a reduction and a scoped no-go, not the
claimed quarter-scale inequality.

## 2. Uniform one-sided wavelet

Let

\[
 R=X^{1/4},\quad y=\lfloor\sqrt X\rfloor,\quad N=\lfloor X\rfloor,
\quad
 \mathcal B_{\rm flat}^{(N)}=\sum_kD_N(k)W(k).
\]

Writing (W=\widehat G), where

\[
 G(t)=\eta(yt)V_{\rm low}(4R^2t^2)\frac{1-e(-t)}t,
\]

removes the formal pole but retains both physical transition scales.  For
every fixed (A\geq1),

\[
 |W(k)|\ll_A\frac1{R+|k|}
 \left(1+\frac{|k|}{y}\right)^{-A},
\qquad
 \sum_k|W(k)|\ll\log X,
\qquad
 \sum_k|kW(k)|\ll y.
\tag{122.S1}
\]

For fixed (0<\delta<1/8), set (K_\delta=yX^\delta).  The exact
fractional-part formula gives (|D_N(k)|\leq y), and sufficiently many
integrations by parts give

\[
 \sum_{|k|>K_\delta}|D_N(k)W(k)|
 =O_{A,\delta}(RX^{-A}).
\tag{122.S2}
\]

Every retained oriented interval is positive.  The central window is
target-safe:

\[
 \sum_{|k|\leq R}|D_N(k)W(k)|
 \ll_\varepsilon RX^\varepsilon.
\tag{122.S3}
\]

These bounds explicitly price the growing (1/y)-cutoff seminorms; they
do not use fixed-(X) Schwartz decay as a uniform estimate.

## 3. Two further strict target-safe packages

Put

\[
 \widetilde D_N(k)=D_N(k)+kc_y,
 \qquad A_0=\lceil\log_2R\rceil.
\]

The full identity (sum_k kW(k)=J(0)=0), together with the high-order
tail in (122.S1), makes the localized centering seam target-safe.  The
oriented cumulative projection onto increments divisible by (2^{A_0})
satisfies

\[
 \sum_{|k|\leq K_\delta}
 |\widetilde D_{\geq A_0}(k)W(k)|
 \ll_\varepsilon X^\varepsilon
 \left(\log X+\frac y{2^{A_0}}\right)
 \ll_\varepsilon RX^\varepsilon.
\tag{122.S4}
\]

On the odd positive-character branch, every central divisor occurrence
for (N+j), (|j|\leq K_\delta), is an ordered factor pair in a box of
side (O(1+X^\delta)) around ((y,y)).  The map from an occurrence to its
ordered pair is injective, including the square tie once.  Thus the total
central increment mass is (O((1+X^\delta)^2)), and its cumulative
wavelet cost is

\[
 O_\delta(X^{2\delta}\log X)
 =O_\varepsilon(RX^\varepsilon).
\tag{122.S5}
\]

## 4. Complete complementary-divisor identity

For every positive (m=2^an), (n) odd, define

\[
 a(n)=\sum_{d\mid n}\chi_4(d)=\frac{r_2(m)}4,
 \qquad
 T_z(n)=\sum_{\substack{q\mid n\\q<z}}\chi_4(q).
\]

The character-preserving complement is (d\leftrightarrow n/d), not
(d\leftrightarrow m/d) when (a\geq1).  Exact completion gives

\[
 \boxed{A_y(2^an)=a(n)-\chi_4(n)T_{n/y}(n).}
\tag{122.S6}
\]

The strict threshold (q<n/y) is forced by the inclusive (d\leq y)
cutoff.  It handles the hard sample and square fixed points without a half
weight.  At (n=y^2), on the odd branch,

\[
 2A_y(y^2)=a(y^2)+\chi_4(y).
\tag{122.S7}
\]

If (chi_4(n)=-1), then (a(n)=0) and

\[
 A_y(n)=T_{n/y}(n),
\tag{122.S8}
\]

so the complement returns the coefficient exactly.  If
(chi_4(n)=1), then (A_y) is one half of (a(n)) plus an exact central
band.  For (a=0) that band is covered by (122.S5); for (a\geq1) its
threshold is (y/2^a+O(X^\delta/2^a)), and the band is generally wide.

## 5. Exact smallest survivor

For a localized increment (m=2^an), define

\[
 \mathscr V_\delta(m)=
 \begin{cases}
  \frac12a(n),&a=0,\ \chi_4(n)=1,\\
  T_{n/y}(n),&a=0,\ \chi_4(n)=-1,\\
  a(n)-\chi_4(n)T_{n/y}(n),&1\leq a<A_0,\\
  0,&a\geq A_0.
 \end{cases}
\tag{122.S9}
\]

Let (mathcal I_k) be the exact oriented interval from (N) to (N+k).
The low/high, centering, central-(k), and odd-central overlap identities
then give

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}
 W(k)\mathcal I_k\mathscr V_\delta
 +O_{\varepsilon,\delta}(RX^\varepsilon).}
\tag{122.S10}
\]

The displayed survivor retains capacity (y=R^2).  Its odd
negative-character part is the self-return (122.S8); its odd
positive-character part is half of the full (r_2/4) wave; and every low
even branch retains the exact full-minus-complement coefficient.  Applying
the desired quarter-scale circle estimate to the full coefficient would be
circular.  Expanding the full coefficient and subtracting its complement
reconstructs the original (d\leq y) product cone exactly.

## 6. Review outcome and proof-state effect

The three independent reports and their second-stage audits verify the
uniform constants, exact tail exponents, positive window, cumulative
projection, localized centering, all two-adic and residue branches,
strict/weak boundaries, square ties, ordered-pair count, and exact
survivor.  The conductor repairs make every overlap explicit.  No report
proves a target estimate for (122.S10).

Promote the wavelet localization and survivor reduction, and promote the
complementary-divisor self-return as an obstruction to this mechanism.
Reject any claim that a factor (1/2), a contracted even threshold, a
full-(r_2) insertion, or a second complement is a power saving.

`M9-M1-global-lower-radial-signed-estimate`, GAR, both direct blockwise M1
parents, all three M2 parents, endpoint uniformity, `M9`, and both
Gauss-circle bridges remain open.

## 7. Strategy after Round 122

The lower GAR route is now parked at the exact functional (122.S10).  It
may be reopened only by a new joint signed inequality across Fourier
indices, low two-adic valuations, residue classes, and the full/complement
labels.  Complementary inversion, residuewise or valuationwise norms,
full-circle completion, and Abel/Fourier reconstruction are exhausted.

Under the August 21 strategy, the next core campaign rotates to the
mandatory M2 conjunction and must name a noninvertible actual-symbol
mechanism before reopening TOP, BAL, or UNBAL.  No pointwise exponent
changes: the internal theorem remains (1/3), and the separately audited
external benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]
