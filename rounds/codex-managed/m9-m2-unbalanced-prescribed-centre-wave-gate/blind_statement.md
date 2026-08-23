# Round 118 blind statement: prescribed-centre truncated divisor wave

This statement is self-contained. Treat every displayed profile as fixed
literal data; do not replace it by a complete divisor coefficient.

Let \(X\ge2\) be real, let

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 H_D\asymp DX^{-1/4},
\]

with

\[
 {1\over4}\le\delta<{1\over2},\qquad
 0\le\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463.
\tag{118.B1}
\]

Put

\[
 K={XL\over D^2},\qquad M=LK,qquad
 F={XL\over D},\qquad \Delta={D\over L}.
\tag{118.B2}
\]

Let \(q_L\) be the literal nonnegative smooth Vaaler/frequency profile,
supported on \(h\asymp L\), with the inherited height taper. Let \(W\)
be the fixed smooth spatial profile. Define

\[
 \mathcal Q_L(y)=\int_0^\infty {q_L(h)\over h}e(hy)\,dh
\tag{118.B3}
\]

and the prescribed-centre wave

\[
 \boxed{
 \mathscr R_{D,L}(X)=
 \sum_{s\ge1}\sum_{\substack{r\mid s\\r\ {\rm odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \mathcal Q_L\!\left({r(X-s)\over4X}\right).}
\tag{118.B4}
\]

Equivalently, after writing \(s=rd\),

\[
 \mathscr R_{D,L}(X)=
 \sum_{r\ {\rm odd}}\chi_4(r)W\!\left({X\over rD}\right)
 \sum_{d\ge1}
 \mathcal Q_L\!\left({r(X-rd)\over4X}\right).
\tag{118.B5}
\]

The active scales are \(r\asymp X/D\), \(d\asymp D\). Rapid decay of
\(\mathcal Q_L\) restricts the product to

\[
 |rd-X|\ll_A \Delta X^\varepsilon.
\tag{118.B6}
\]

The raw number of active product pairs is
\(O_\varepsilon(\Delta X^\varepsilon)\), and divisor bounds give only

\[
 \mathscr R_{D,L}(X)\ll_\varepsilon {D\over L}X^\varepsilon.
\tag{118.B7}

\]

The required estimate is

\[
 \boxed{
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}.}
\tag{118.B8}
\]

Thus the missing factor is

\[
 {D\over LX^{1/4}}={H_D\over L}>1.
\tag{118.B9}
\]

For an integer centre \(X\), the exact central product contributes only

\[
 \mathcal Q_L(0)
 \sum_{\substack{r\mid X\\r\ {\rm odd}}}
 \chi_4(r)W\!\left({X\over rD}\right),
\tag{118.B10}
\]

which is divisor-bounded. A proposed countermodel must therefore control
nearby products and every competing sign; one positive subset is not a
lower bound for the full outside-absolute wave.

The same object has the exact reciprocal row form

\[
 \sum_{r\ {\rm odd}}\chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\ge1}{q_L(4Xk/r^2)\over k}e(Xk/r),
\tag{118.B11}
\]

up to the already certified flat-smooth normalization and target-safe
stationary remainder. Applying the inverse transform to (118.B11) returns
(118.B4); this identity is not an estimate.

Required outcome: prove (118.B8), a nonempty target-safe strict subrange,
a quantified actual-sign saving, a rigorous coherent countermodel to the
uniform pointwise strategy, or a scoped no-go whose smallest signed
survivor is explicit. Test exact centre, near centre, primes in both odd
classes, squares, fourth powers, divisor-rich products, short coherent
runs, profile edges, and both signs. Do not infer a lower bound from an
uncontrolled positive sector, and do not complete (118.B4) to
\(r_2/4\).

