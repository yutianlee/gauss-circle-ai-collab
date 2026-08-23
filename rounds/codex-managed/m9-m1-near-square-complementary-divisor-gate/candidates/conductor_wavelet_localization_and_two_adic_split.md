# Conductor candidate: wavelet localization and two-adic divisor split

Campaign: `m9-m1-near-square-complementary-divisor-gate`

Status: candidate pending statement-only and hostile review.

Put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,
 \qquad N=\lfloor X\rfloor,
\]

and retain the exact Round-121 notation

\[
 \mathcal B_{\rm flat}^{(N)}(X)=\sum_{k\in\mathbb Z}D_N(k)W(k),
 \qquad W(k)=\widehat J(k)-\widehat J(k+1).
\tag{122.C1}
\]

This candidate proves three strict target-safe deletions and the complete
complementary-divisor identity. It does not estimate the remaining
medium-index, low-two-adic signed functional.

## 1. Uniform difference-wavelet envelope

Since

\[
 W(k)=\int_0^1G_{R,y}(t)e(-kt)\,dt,
 \qquad
 G_{R,y}(t)=J_{R,y}(t)(1-e(-t)),
\tag{122.C2}
\]

the apparent (1/t\) singularity is removable. On its positive arc,

\[
 G_{R,y}(t)=\eta(yt)V_{\rm low}(4R^2t^2)
 {1-e(-t)\over t}.
\tag{122.C3}
\]

The transition of (\eta(yt)) has width (1/y\), while the radial
transition has width (1/R\), and these regions are disjoint for large
(X\). For every fixed integer (M\geq1\), Leibniz and scaling give

\[
 \|G\|_1\ll R^{-1},\qquad
 \|G'\|_1\ll1,
 \qquad \|G^{(M)}\|_1\ll_M y^{M-1}.
\tag{122.C4}
\]

Periodic integration by parts therefore gives

\[
 \boxed{
 |W(k)|\ll_M
 \min\left(R^{-1},{1\over1+|k|},
 {y^{M-1}\over(1+|k|)^M}\right).}
\tag{122.C5}
\]

In particular,

\[
 \sum_k|W(k)|\ll\log(2X),
 \qquad
 \sum_k|kW(k)|\ll y.
\tag{122.C6}
\]

These bounds price, rather than ignore, the one-sided interpolation edge.

## 2. Target-safe far Fourier tail

The exact floor formula has the uniform bound

\[
 |D_N(k)|\leq y,
\tag{122.C7}
\]

because each denominator summand is

\[
 \left\{{N\over d}\right\}
 -\left\{{N+k\over d}\right\}.
\]

Fix (\delta>0\) and put (K_\delta=yX^\delta\). From (122.C5),

\[
 \sum_{|k|>K_\delta}|D_N(k)W(k)|
 \ll_M y^M K_\delta^{1-M}
 \ll X^{1/2-\delta(M-1)}.
\tag{122.C8}
\]

For any desired (A>0\), choosing (M=M(A,\delta)) makes (122.C8)
(O_{A,\delta}(RX^{-A})\). Taking (0<\delta<1/4\) also ensures

\[
 0<N+k<2X\qquad(|k|\leq K_\delta)
\tag{122.C9}
\]

for sufficiently large (X\). Thus the conventions at (m=0\) and
negative (m\) lie in a target-safe tail.

## 3. Target-safe central Fourier window

For (m\ne0\),

\[
 |A_y(m)|\leq\tau(|m|)\ll_\varepsilon |m|^\varepsilon,
 \qquad c_y\ll1.
\tag{122.C10}
\]

The recurrence for (D_N\) consequently gives, throughout
(|k|\leq R\),

\[
 |D_N(k)|\ll_\varepsilon |k|X^\varepsilon.
\tag{122.C11}
\]

Combining (122.C11) with the (R^{-1}) row of (122.C5),

\[
 \boxed{
 \left|\sum_{|k|\leq R}D_N(k)W(k)\right|
 \ll_\varepsilon RX^\varepsilon.}
\tag{122.C12}
\]

This deletes the complete central Fourier-index window by absolute values.

## 4. Target-safe high two-adic strata

Put

\[
 \widetilde D_N(k)=D_N(k)+kc_y.
\]

For fixed (X\), exact Fourier convergence gives

\[
 \sum_k kW(k)=\sum_k\widehat J(k)=J(0)=0,
\tag{122.C13}
\]

so replacing (D_N\) by (\widetilde D_N\) changes no full sum. On the
localized window, (\widetilde D_N(k)) is the oriented cumulative sum of
(A_y(N+j)) over the (|k|) intervening integers.

This replacement is also target-safe after truncation. Indeed

\[
 c_y\sum_{|k|\leq K_\delta}kW(k)
 =-c_y\sum_{|k|>K_\delta}kW(k),
\]

and (122.C5) gives

\[
 \sum_{|k|>K_\delta}|kW(k)|
 \ll_M y^{M-1}K_\delta^{2-M}.
\tag{122.C13a}
\]

Choosing (M=M(A,\delta)) makes (122.C13a) (O(RX^{-A})).

Let (A_0=\lceil\log_2R\rceil\), and retain only increments for which
(2^{A_0}\mid N+j\), equivalently (v_2(N+j)\geq A_0\). There are at
most (1+|k|/2^{A_0}) such integers in any oriented interval. Hence the
corresponding cumulative discrepancy (\widetilde D_{\geq A_0}(k))
satisfies

\[
 |\widetilde D_{\geq A_0}(k)|
 \ll_\varepsilon X^\varepsilon
 \left(1+{|k|\over2^{A_0}}\right).
\tag{122.C14}
\]

Equations (122.C6) and (122.C14) give, on the localized window,

\[
 \boxed{
 \left|\sum_{|k|\leq K_\delta}
 \widetilde D_{\geq A_0}(k)W(k)\right|
 \ll_\varepsilon X^\varepsilon
 \left(\log(2X)+{y\over2^{A_0}}\right)
 \ll_\varepsilon RX^\varepsilon.}
\tag{122.C15}
\]

Write the exact cumulative partition

\[
 \widetilde D_N(k)=\widetilde D_{<A_0}(k)
 +\widetilde D_{\geq A_0}(k).
\]

On the overlapping core, no package is counted twice: explicitly,

\[
 \sum_{|k|\leq R}\widetilde D_{<A_0}(k)W(k)
 =\sum_{|k|\leq R}D_N(k)W(k)
 +c_y\sum_{|k|\leq R}kW(k)
 -\sum_{|k|\leq R}\widetilde D_{\geq A_0}(k)W(k).
\tag{122.C15a}
\]

The three terms on the right are target-safe by (122.C12),
\(\sum_{|k|\leq R}|kW(k)|\ll R\), and the absolute majorant used in
(122.C15). Together with the localized centering seam (122.C13a), this
proves that the retained term is exactly the middle-window projection
of \(\widetilde D_{<A_0}\), modulo \(O_\varepsilon(RX^\varepsilon)\).

After combining (122.C8), (122.C12), and (122.C15), the only surviving
Fourier-index package is

\[
 R<|k|\leq yX^\delta,
 \qquad v_2(N+j)<A_0
\tag{122.C16}
\]

inside the cumulative interval. Formula (122.C16) is shorthand for the
exact low-two-adic cumulative projection, not a pointwise condition only
on the terminal index (N+k\).

## 5. Exact complementary-divisor identity

For every positive (m\), write

\[
 m=2^a n,qquad n\ \hbox{odd}.
\]

Only odd divisors contribute, so (A_y(m)=A_y(n)). Put

\[
 a(n)=\sum_{d\mid n}\chi_4(d)={r_2(n)\over4},
 \qquad
 T_z(n)=\sum_{\substack{q\mid n\\q<z}}\chi_4(q).
\tag{122.C17}
\]

Mapping every omitted divisor (d>y\) to (q=n/d<n/y\) and using
(\chi_4(n/q)=\chi_4(n)\chi_4(q)\) gives

\[
 \boxed{
 A_y(2^an)=a(n)-\chi_4(n)T_{n/y}(n).}
\tag{122.C18}
\]

The strict inequality in (T_{n/y}\) is forced by the inclusive hard
cutoff (d\leq y\). It also handles the exact central tie without a half
weight. Formula (122.C18), not the replacement (A_y=a\), is the lawful
full-divisor completion.

For (a=0\), put (z=n/y\). If (z\leq y\), define

\[
 C_-(n)=\sum_{\substack{d\mid n\\z\leq d\leq y}}\chi_4(d),
 \qquad A_y(n)=T_z(n)+C_-(n),
\tag{122.C19}
\]

while if (z>y\), define

\[
 C_+(n)=\sum_{\substack{d\mid n\\y<d<z}}\chi_4(d),
 \qquad T_z(n)=A_y(n)+C_+(n).
\tag{122.C20}
\]

Thus, when (\chi_4(n)=1\),

\[
 2A_y(n)=
 \begin{cases}
 a(n)+C_-(n),&n\leq y^2,\\
 a(n)-C_+(n),&n>y^2,
 \end{cases}
\tag{122.C21}
\]

At the equality case \(n=y^2\), necessarily \(y\) is odd on the
\(a=0\) branch, and the fixed complementary divisor is counted once:

\[
 2A_y(y^2)=a(y^2)+\chi_4(y).
\tag{122.C21a}
\]

where the central band has width

\[
 |n/y-y|={|n-y^2|\over y}\ll1+X^\delta
\tag{122.C22}
\]

on (122.C9). When (\chi_4(n)=-1\), (a(n)=0\) and

\[
 A_y(n)=T_{n/y}(n),
\tag{122.C23}
\]

while the corresponding central character sum in (122.C19) or
(122.C20) is exactly zero. This branch has no scale contraction: its
complementary threshold remains (n/y=y+O(X^\delta)).

For (a\geq1\), (122.C18) is still exact, but its complementary cutoff is

\[
 {n\over y}={N+k\over2^ay}
 \asymp {y\over2^a}
\tag{122.C24}
\]

on the localized window. More precisely, \(N+k<2y^2\) there for all
sufficiently large \(X\), hence \(n=(N+k)/2^a<y^2\) whenever \(a\geq1\).
The lower tail \(T_{n/y}(n)\) is empty when \(n\leq y\); otherwise its
strict threshold lies between \(1\) and \(y\). All two-adic branches,
including the full \(r_2/4\) coefficient and the contracted complement,
remain jointly signed.

### 5.1. The odd positive-character central correction is target-safe

This estimate is made in the localized cumulative form, so no boundary
term is hidden by a truncated Abel summation. For the \(a=0\),
\(\chi_4(n)=1\) branch, define the signed central increment

\[
 \Gamma(n)=
 \begin{cases}
 C_-(n),&n<y^2,\\
 \chi_4(y),&n=y^2,\\
 -C_+(n),&n>y^2,
 \end{cases}
\tag{122.C25}
\]

and set it to zero off that branch. Then (122.C21)--(122.C21a) read

\[
 A_y(n)=\frac12a(n)+\frac12\Gamma(n).
\tag{122.C26}
\]

Every divisor occurring in \(C_-(n)\) or \(C_+(n)\) has its complementary
divisor in the same central interval between \(y\) and \(n/y\). On
\(|j|\leq K_\delta\), with \(n=N+j\), both factors therefore lie within
\(O(1+X^\delta)\) of \(y\). The map from a central divisor occurrence to
its ordered factor pair \((d,n/d)\) is injective. It includes the equality
pair \((y,y)\) exactly once, and therefore gives

\[
 \sum_{|j|\leq K_\delta}|\Gamma(N+j)|
 \ll (1+X^\delta)^2.
\tag{122.C27}
\]

Let \(E(k)\) be the oriented cumulative sum of these increments between
\(N\) and \(N+k\), with the same convention as \(\widetilde D_N(k)\).
Then

\[
 \sup_{|k|\leq K_\delta}|E(k)|
 \leq\sum_{|j|\leq K_\delta}|\Gamma(N+j)|.
\]

Combining this with (122.C6), and choosing \(0<\delta<1/8\), proves

\[
 \sum_{|k|\leq K_\delta}|E(k)W(k)|
 \ll_\delta X^{2\delta}\log(2X)
 =O_\varepsilon(RX^\varepsilon).
\tag{122.C28}
\]

Thus the odd positive-character branch reduces, modulo a target-safe
central cumulative package, to one half of the full \(r_2/4\) coefficient
inside the same one-sided wavelet. No bound for that full coefficient is
asserted. The full pre-Abel identity

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_k\widehat J(k)A_y(N+k)
\]

remains a valid diagnostic for the untruncated series, but is not used to
justify (122.C28).

## 6. Capacity and smallest survivor

| Package | Bound or capacity | Outcome |
|---|---:|---|
| (|k|>yX^\delta) | (O_{A,\delta}(RX^{-A})) | target-safe tail |
| (|k|\leq R) | (O_\varepsilon(RX^\varepsilon)) | target-safe central window |
| cumulative (v_2\geq\lceil\log_2R\rceil) | (O_\varepsilon(RX^\varepsilon)) | target-safe sparse branch |
| odd \(\chi_4(n)=1\) central correction | \(O_\delta(X^{2\delta}\log X)\), \(\delta<1/8\) | target-safe factor band |
| (R<|k|\leq yX^\delta), low (v_2) | no bound below trivial capacity | exact survivor |
| odd (\chi_4(n)=-1) complement | threshold (n/y=y+O(X^\delta)) | no contraction/self-return branch |
| full (r_2/4) component | exact only | cannot use the desired quarter discrepancy |

For an increment \(m=2^an\) in the positive localized window, define

\[
 \mathscr V_\delta(m)=
 \begin{cases}
  \frac12a(n),&a=0,\ \chi_4(n)=1,\\
  T_{n/y}(n),&a=0,\ \chi_4(n)=-1,\\
  a(n)-\chi_4(n)T_{n/y}(n),&1\leq a<A_0,\\
  0,&a\geq A_0.
 \end{cases}
\tag{122.C29}
\]

Let

\[
 \mathcal I_k f=
 \begin{cases}
  \sum_{N<m\leq N+k}f(m),&k>0,\\
  0,&k=0,\\
  -\sum_{N+k<m\leq N}f(m),&k<0.
 \end{cases}
\]

If \(S(k)=\mathcal I_k\mathscr V_\delta\), the exact localized
bookkeeping identity is

\[
 S(k)=D_N(k)+kc_y-\widetilde D_{\geq A_0}(k)-\frac12E(k).
\tag{122.C29a}
\]

In particular, on the already-deleted central window,

\[
 \begin{aligned}
 \sum_{|k|\leq R}S(k)W(k)
 ={}&\sum_{|k|\leq R}D_N(k)W(k)
 +c_y\sum_{|k|\leq R}kW(k)\\
 &-\sum_{|k|\leq R}\widetilde D_{\geq A_0}(k)W(k)
 -\frac12\sum_{|k|\leq R}E(k)W(k).
 \end{aligned}
\tag{122.C29b}
\]

All four terms on the right are target-safe by (122.C12), the central
\(|kW(k)|\) bound, (122.C15), and (122.C28), respectively.

The strict deletions above give the exact target-scale reduction

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}W(k)\mathcal I_k\mathscr V_\delta
 +O_{\varepsilon,\delta}(RX^\varepsilon).}
\tag{122.C30}
\]

Thus the smallest survivor currently justified is (122.C30): the
medium-index, low-two-adic cumulative wavelet with the already-safe odd
positive-character central correction removed. It retains one half of the
full coefficient on that odd branch, the exact self-return on the odd
negative-character branch, and the full-divisor/complement pair together
on every unresolved even branch. This is a scoped no-go for uniform
contraction, not a lower bound for the complete signed survivor.

## 7. Proposed state effect and continuation

If independently verified, promote the uniform wavelet envelope, the
target-safe far, central, and high-two-adic packages, and the exact
complement formula (122.C18)--(122.C24). Retain the complete lower-radial
estimate open.

A valid continuation must estimate the medium-index, low-two-adic signed
functional jointly. In particular it must control the noncontracting odd
(\chi_4(n)=-1\) sector together with the full-divisor and even contracted
pieces. Applying a norm to those branches separately or using a
conjectural short-interval circle estimate is not authorized.
