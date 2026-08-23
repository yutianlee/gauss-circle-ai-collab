# Statement-only packet: near-square complementary-divisor gate

Let (X\ge2) be real,

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,
 \qquad N=\lfloor X\rfloor.
\]

Fix a real smooth function (V_{\rm low}) equal to one near zero and
supported sufficiently close to zero. Choose a fixed smooth
(\eta) with (\eta(u)=0) for (u\leq1/2) and
(\eta(u)=1) for (u\geq1). On a small positive arc define

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t},
\]

extended smoothly by zero and periodically, and put

\[
 W_{R,y}(k)=\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1).
\]

For every (m,k\in\mathbb Z), with every positive (d) understood to
divide zero, define

\[
 A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d),
 \qquad c_y=\sum_{d\leq y}{\chi_4(d)\over d},
\]

and

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left(\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right).
\]

The accepted exact identity is

\[
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}D_N(k)W_{R,y}(k),
\tag{122.B1}
\]

and the target is

\[
 \mathcal B_{\rm flat}^{(N)}(X)
 \ll_\varepsilon RX^\varepsilon.
\tag{122.B2}
\]

Independently determine whether the complementary-divisor involution
(d\leftrightarrow m/d) for (m=N+k\) produces a noninvertible gain in
(122.B1). Required work:

1. Prove a quantitative localization or weighted envelope for
   (W_{R,y}(k)), including the one-sided cutoff at scale (1/y), and
   make every discarded (k)-tail target-safe using only stated bounds.
2. On the remaining near-square window, derive the exact divisor
   complement separately for every (2)-adic valuation and odd residue
   class of (m\), with square/central-divisor ties explicit.
3. Keep the signed (k)-sum intact until an actual inequality is proved.
   A full divisor identity, a Fourier inversion, or a restatement of
   (122.B1) is not a saving.
4. Produce one of: the complete target (122.B2), a strict target-safe
   subpackage, a signed power saving, an inverse theorem, or a rigorous
   self-return/no-go with the smallest survivor.

Do not assume the conjectural quarter Gauss-circle estimate or any short-
interval consequence of it. Computation may falsify a claim but cannot
certify the asymptotic theorem.
