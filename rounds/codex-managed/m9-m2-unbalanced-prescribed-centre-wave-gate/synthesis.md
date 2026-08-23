# Round 118 synthesis: prescribed-centre wave viability gate

Campaign: `m9-m2-unbalanced-prescribed-centre-wave-gate`

Starting graph SHA-256:
`d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb`

Resulting graph SHA-256 after the validated State Patch:
`c3498daad3bdceb7c69c0e47a616e03ebfa12ccaf42f8df42958aa227f50fd91`

## Frozen objective

The round tested the exact flat-smooth unbalanced M2 wave

\[
 \mathscr R_{D,L}(X)=
 \sum_s\sum_{\substack{r\mid s\\r\ {m odd}}}
 \chi _4(r)W\!\left({X\over rD}\right)
 \mathcal Q_L\!\left({r(X-s)\over4X}\right),
\]

equivalently

\[
 \sum_{r\ {m odd}}\chi _4(r)W\!\left({X\over rD}\right)
 \sum_k{q_L(4Xk/r^2)\over k}e(Xk/r),
\]

with \(D=X^\delta\), \(L=X^\ell\),
\(1/4\leq\delta<1/2\),
\(0\leq\ell<\delta-1/4\), and
\(178\ell+1638\delta>463\).  Its absolute product capacity is \(D/L\),
while the required bound is \(X^{1/4+\varepsilon}\).

The permitted outcomes were the target, a target-safe subrange, a
quantified literal saving, a rigorous countermodel, or a scoped no-go with
the smallest signed survivor.

## Certified flat-row envelope

Two independent reports and a hostile seam review prove, for every frozen
flat smooth component,

\[
 \boxed{
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^\varepsilon
 \min\left\{{D\over L},
 \sqrt{XL/D}+\sqrt{X/(LD)}\right\}.}
\tag{118.S1}
\]

The first term follows from Abel summation in \(k\) and a real-centre
integer-product layer cake.  For the second, resolve \(\chi _4\) by its
exact quarter shifts on all integers, or parametrize the odd lattice.  The
fixed-\(k\) phases \(Xk/r\pm r/4\) have second derivative
\(\asymp LD/X\), the literal sampled amplitude has supremum plus variation
\(O(K^{-1})\), and the outer \(O(K)\)-term triangle cancels that factor.

Put \(a=\delta-\ell\).  The exponent in (118.S1) is

\[
 \beta(a)=\min\left(a,{1-a\over2}\right).
\]

It improves absolute capacity exactly when \(a>1/3\), by the power
\(X^{(3a-1)/2}\).  It is never target-safe at a strict residual point,
because \(1/4<a<1/2\) implies \(\beta(a)>1/4\).  This is an exact
fixed-centre realization of the already accepted scalar
second-derivative envelope, not a character-specific gain or a new global
exponent.

## Coherent-run falsification control

Let consecutive \(d\asymp D\) select \(r_d\) in one fixed odd residue
class modulo four and satisfy

\[
 |X-dr_d|\leq cD/L
\]

inside a sufficiently small central kernel lobe.  The discovery report's
fixed-exponent split was repaired to the uniform actual-scale statement

\[
 U\ll
 1+
 \begin{cases}
 (D^3/(XL))^{1/2},&D^3\geq C_0X,\\
 (D^4/(XL))^{1/3},&D^3<C_0X.
 \end{cases}
\tag{118.S2}
\]

The proof uses the gap in \(4\mathbb Z\).  In the first range it forces
\(r_d\) affine and a second divided difference gives the square-root
branch.  In the second it forces \(r_d\) quadratic and a third divided
difference gives the cube-root branch.  The blind report independently
proved the fixed-step affine subcase by exact quadratic product drift.

Both branches are target-safe: the second is
\(O(X^{1/9}L^{-1/3})\), and the first is
\(O(X^{1/4}L^{-1/2})\).  Therefore one consecutive same-character
central-lobe run cannot falsify the target.  Unions of runs, step changes,
noncentral shoulders, the opposite residue class, and the complete signed
complement are not controlled by (118.S2).

## Exact phase-one square sector

The statement-only report also exposed the odd-\(r\) Poisson stationary
orientation.  On a smooth interior cell it has phase

\[
 e(\sqrt{Xk\nu}),\qquad k\asymp K,\quad \nu\asymp L,quad
 \nu\ {m odd},
\]

literal character \(\chi _4(\nu)\), and coefficient scale

\[
 {1\over K}\sqrt{R/L}={\sqrt F\over M}.
\]

For integer \(X=bA^2\), with \(b\) squarefree, the complete interior
leading phase-one sector satisfies \(k\nu=bw^2\), hence has
\(O_\varepsilon(\sqrt M X^\varepsilon)\) modes and absolute contribution

\[
 O_\varepsilon(\sqrt{D/L}\,X^\varepsilon),
\]

which is target-safe.  In the square case \(b=1\), the parametrization
\(k=au^2\), \(\nu=av^2\) gives
\(\chi _4(\nu)=\chi _4(a)\).  Uniform two-dimensional Euler summation on
the interior literal profile gives a signed \(O(\sqrt M)\) count; deleting
the character gives the upper bound \(O(\sqrt M\log(2L))\).

The seam review restricted this result sharply.  It controls the interior
leading phase-one sector for integer \(X\), not every coherent root-of-unity
sector for arbitrary real \(X\), and not any endpoint, transition, or
stationary-remainder package.  It is another coherent-countermodel no-go,
not a proof of the full wave.

## Arithmetic and source controls

The exact centre, when present, is divisor-bounded.  A half-integer tie is
the union of two separately divisor-bounded product levels and has no
automatic conjugate pairing.  Prime, square, fourth-power, and
divisor-rich centres create no target-sized exact-centre obstruction.
The small near-centre kernel has a common real direction, but its
\(\chi _4\) multiplier has both signs and its complement is uncontrolled.

The hostile source audit found no applicable imported theorem.  Complete
\(r_2\) Voronoi formulae, complete short-interval divisor results, general
Voronoi identities, and the audited one-dimensional exponent-pair theorem
all fail at least one of the literal truncated coefficient, moving profile,
fixed real centre, pointwise norm, power saving, or endpoint hypotheses.

## Smallest survivor and decision

After the certified one-dimensional envelope and coherent controls, the
smallest flat-smooth survivor remains the complete joint sum

\[
 \sum_{k\asymp K}{1\over k}
 \sum_{r\asymp X/D}\chi _4(r)
 W\!\left({X\over rD}\right)
 q_L\!\left({4Xk\over r^2}\right)e(Xk/r),
\tag{118.S3}
\]

with all disconnected selector packets, both character classes,
noncentral shoulders, and the signed complement retained before the
\(k\)-triangle.  In the saving region, the remaining excess over the
target is \(X^{(1-2a)/4}\).  Equivalently, after odd-\(r\) Poisson, the
survivor is the full off-coherent truncated-divisor product-phase sum, not
its square sector.

Round 118 therefore promotes only (118.S1), the actual-scale coherent-run
obstruction (118.S2), and the scoped integer-centre phase-one control.  It
rejects the proposed single-run countermodel, exact-centre or positive-core
lower bounds, clean \(r_2/4\) completion, another coefficient-preserving
transform followed by a norm, and automatic transfer of Round-117
exponents.

The full \(X^{1/4+\varepsilon}\) wave estimate remains open.  Sharp,
starred, clipped, hard, arithmetic-owner, and profile-transition kernels
remain separate.  Consequently hard TOP, BAL, complete UNBAL, M9-M2,
M9-M1, endpoint uniformity, M9, and the Gauss-circle quarter target all
remain open.

The internal uniform exponent remains \(1/3\), and the audited external
benchmark remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]

Because the probe found no viable noninvertible pointwise mechanism for
the complete wave, the next core campaign is the strategy-mandated direct
minimization of the two M9-M1 physical parents.  It must identify the exact
residual parent capacities under all already proved owners before any new
transform or Gram proposal is entertained.
