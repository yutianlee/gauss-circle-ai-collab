# Round 119 blind statement: direct M1 parent minimax

This statement is self-contained.  Treat the physical owner partition and
all displayed profiles as literal.  Menu optimality is not a lower bound
for an arithmetic sum.

Let \(X\ge2\),

\[
 D=X^\delta,
 \qquad L=X^\ell,
 \qquad
 {1\over4}\le\delta\le{1\over2},
 \qquad
 0\le\ell\le\delta-{1\over4}.
\tag{119.B1}
\]

For a fixed literal M1 block write, suppressing only fixed harmless
constants and the conjugate frequency,

\[
 B_1(D,L;X)=
 \sum_{h\asymp L}{\Phi(h/(H_D+1))\over h}
 \sum_{d\asymp D}\chi _4(d)w_D(d)e(hX/d),
 \qquad H_D\asymp DX^{-1/4}.
\tag{119.B2}
\]

The accepted owner order is:

1. the unexpanded bottom and `R5-Full`;
2. the terminal frequency line \(\ell=\delta-1/4\);
3. the full second-derivative target point \((1/2,0)\); and
4. the TTY wedge \(178\ell+1638\delta\le463\).

The exact residual exponent set is

\[
 \mathcal U_1=
 \left\{(\delta,\ell):
 0\le\ell<\delta-{1\over4},
 \ 178\ell+1638\delta>463\right\}
 \setminus\{(1/2,0)\}.
\tag{119.B3}
\]

Lift (119.B3) to the literal denominator partition.  The unique profile
containing \(d=\lfloor\sqrt X\rfloor\) is the hard profile; every other
profile is smooth.  The direct physical proof has exactly two open
parents:

\[
 \mathrm{HARD}_{M1}:quad
 T_{M1,L}ll_\varepsilon L^{3/2}X^\varepsilon
\tag{119.B4}
\]

on the middle/lower residual shells of the hard profile, after its proved
one-sided transform, and

\[
 \mathrm{SMOOTH}_{M1}:quad
 B_1(D,L;X)ll_\varepsilon X^{1/4+\varepsilon}
\tag{119.B5}
\]

on every smooth literal label in \(\mathcal U_1\).  Both are required for
the standard blockwise assembly.  A global angular-radial theorem is an
alternative whole-route hypothesis, not an already proved owner of either
blockwise parent.

The accepted direct bounds for every literal block are

\[
 B_1(D,L;X)ll_\varepsilon X^\varepsilon(1+D/L)
\tag{119.B6}
\]

and

\[
 B_1(D,L;X)ll_\varepsilon X^\varepsilon
 \left(1+\sqrt{LX/D}+{D^{3/2}\over\sqrt{LX}}\right),
\tag{119.B7}
\]

together with the audited TTY estimate

\[
 B_1(D,L;X)ll_\varepsilon
 X^{[89(1+\ell)+819\delta]/1282+\varepsilon}.
\tag{119.B8}
\]

The hard transform is exact up to target-safe boundary and transform
errors.  On \(h,n\asymp L\), its normalized cone has \(O(L^2)\) absolute
capacity and target \(L^{3/2}\).

The critical physical labels to audit are

\[
 D_0\asymp\sqrt X
 \quad\hbox{(hard)},
 \qquad
 D_1\asymp {\sqrt X\over2}
 \quad\hbox{(first smooth)},
 \qquad
 L\asymp X^{1/6}.
\tag{119.B9}
\]

At exponent scale both have \((\delta,ell)=(1/2,1/6)\).  The terminal,
second-derivative target point, and TTY wedge do not own them.  At this
contact, (119.B6) and the leading term of (119.B7) both have exponent
\(1/3\), while the target has exponent \(1/4\).  The apparent deficit is
\(X^{1/12}=L^{1/2}\).

Required outcome: minimize the exact accepted capacity separately on the
hard and smooth residual parents.  Either prove that an accepted owner or
a literal adjacent-profile identity shrinks a parent, obtain a target-safe
subrange or saving, or certify that the direct menu has asymptotic minimax
\(X^{1/3}\) on each parent and isolate the smallest literal critical
survivor.  Retain floors, stars, both signs, support crossings, hard/smooth
ownership, and real \(X\).  Do not infer a lower bound for the actual sums
from menu optimality, and do not import the frozen canonical Gram without
a block-local inverse.
