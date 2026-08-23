# Conductor review: curvature envelope, coherent runs, and scope

Campaign: `m9-m2-unbalanced-prescribed-centre-wave-gate`

Starting graph SHA-256:
`d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb`

## Flat-row estimate

The product-window and reciprocal-curvature estimates pass on each frozen
flat smooth component.  With

\[
 R=X/D,\qquad K=XL/D^2,
\]

Abel summation in \(k\), followed by the real-centre product layer cake,
gives

\[
 \mathscr R_{D,L}(X)\ll_\varepsilon (D/L)X^\varepsilon.
\]

For fixed \(k\), use the identity

\[
 \chi _4(r)={e(r/4)-e(-r/4)\over2i}
\]

on every integer, including its zero value on even integers.  This avoids
zero-extending the smooth amplitude across the odd lattice.  Equivalently,
one may set \(r=2n+1\).  The two phases have

\[
 f_{k,\pm}''(r)\asymp LD/X,
\]

and the literal sampled amplitude, including \(k^{-1}\), has supremum plus
variation \(O(K^{-1})\).  Weighted second-derivative summation and the
\(O(K)\)-term outer triangle therefore prove

\[
 \boxed{
 \mathscr R_{D,L}(X)
 \ll_\varepsilon X^\varepsilon
 \min\left\{{D\over L},
 \sqrt{XL/D}+\sqrt{X/(LD)}\right\}.}
\tag{118.R1}
\]

Let \(a=\delta-\ell\).  The exponent in (118.R1) is

\[
 \beta(a)=\min\left(a,{1-a\over2}\right).
\]

It is strictly below the divisor capacity precisely for \(a>1/3\), with
saving exponent \((3a-1)/2\).  It remains strictly above \(1/4\) at every
strict point \(1/4<a<1/2\).  This is the fixed-centre orientation of the
already accepted scalar second-derivative menu.  It is a useful exact
capacity certificate, but neither a new global exponent nor a
character-specific cancellation theorem.

## Uniform consecutive-run repair

The discovery report's split at the sign of \(\delta-1/3\) is not uniform
when a dyadic scale approaches \(X^{1/3}\).  The safe version uses the
actual scale.

Suppose consecutive \(d\asymp D\) select \(r_d\) in one fixed odd residue
class modulo four and

\[
 |X-dr_d|\le cD/L
\]

for a sufficiently small fixed central-lobe constant \(c\).  There is a
profile-dependent \(C_0\) such that

\[
 U\ll
 1+
 \begin{cases}
 (D^3/(XL))^{1/2},&D^3\ge C_0X,\\
 (D^4/(XL))^{1/3},&D^3<C_0X.
 \end{cases}
\tag{118.R2}
\]

Indeed, \(r_d-X/d=O(c/L)\), while every finite difference of \(r_d\) is
in \(4\mathbb Z\).  In the first scale range the lattice gap forces
\(\Delta^2r_d=0\); three separated points and the second divided
difference of \(X/d\) give the square-root branch.  In the second range it
forces \(\Delta^3r_d=0\); four separated points give the cube-root branch.
Shrinking \(c\) below half the same-residue lattice gap also makes the
selected value unique and handles ties.

Both branches are uniformly target-safe.  The second is
\(O(X^{1/9}L^{-1/3})\), and the first is
\(O(X^{1/4}L^{-1/2})\).  The blind report independently proves the affine
fixed-step subcase by exact quadratic drift.  Thus a single consecutive
central-lobe same-character run cannot falsify the quarter target.

This is not a bound for a union of runs.  Step-change packets, disconnected
hits, noncentral shoulders, the opposite residue class, and the full signed
complement survive.  A positive core is not a lower bound for the complete
wave.

## Scope decision

Promote (118.R1) only for the accepted flat smooth owner.  Promote
(118.R2) only as a scoped countermodel obstruction.  Sharp, starred,
clipped, hard, arithmetic-owner, and profile-crossing kernels are not
errors and are not covered.

The full target remains

\[
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}.
\]

After (118.R1), the live excess in the saving region is
\(X^{(1-2a)/4}\).  Removing it requires a genuinely joint estimate before
the \(k\)-triangle, or an inverse theorem controlling every coherent
selector component and its complement.  A second coefficient-preserving
transform, clean \(r_2/4\) completion, or transfer of the Round-117
exponents remains inadmissible.
