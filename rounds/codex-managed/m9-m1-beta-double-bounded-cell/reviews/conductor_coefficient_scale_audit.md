# Conductor review: coefficient, scale, and normalization ledger

Campaign: m9-m1-beta-double-bounded-cell

At

\[
r=\frac54-\frac{a+b}{2},\qquad
p=\frac54+\frac{a+b}{2},
\]

the accepted contour inequality gives

\[
r-1=\frac14-\frac{a+b}{2}>\frac b2.
\]

Therefore, for every fixed \(k\),

\[
\sum_{h\ge1}h^{-r}\log^k(2h)\ll_k b^{-k-1},\qquad
\sum_{q\ge1}q^{-p}\log^k(2q)\ll_k1.
\]

The compact cell needs no character cancellation; \(|\chi_4(q)|\le1\)
suffices. This does not imply an unsigned large-height estimate.

On every active scale,

\[
\left(\frac{D_j}{2\sqrt X}\right)^a\le1,\qquad
(H_j+1)^b\ll1,
\]

and there are \(O(\log X)\) active blocks. Thus the \(h,q,j\) mass is
polylogarithmic once the finite post-routing family is fixed.

The raw coefficient contains \(-\pi i\sqrt X\); the radial integration
by parts cancels this internal factor. Restoring

\[
-\frac4\pi X^{1/4}\Re\{e(1/8)\,\cdot\,\}
\]

then gives the candidate \(O_\varepsilon(X^{1/4+\varepsilon})\) scale.
Residual contour measures remain exact constants.

The missing validation is not an exponent gap. It is the one-count
assembly: the isolated packet did not list every connector/profile
derivative and excluded boundary module. A follow-up round must freeze
that list and validate it independently.

