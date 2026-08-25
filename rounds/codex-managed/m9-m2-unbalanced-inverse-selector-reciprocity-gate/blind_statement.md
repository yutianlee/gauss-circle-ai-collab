# Statement-only problem: inverse-selector additive reciprocity

Let (X=N_0+\xi), (N_0=\lfloor X\rfloor), (0\le\xi<1), and set

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 R=X/D,\qquad K=XL/D^2,
\]

where

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,qquad
 178\ell+1638\delta>463.
\tag{160.BL1}
\]

For odd (g,n) with (gn\asymp R), let

\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
\tag{160.BL2}
\]

on a literal compact moving set \(\mathcal J_{g,n}\subset\{j:j\asymp
K/g\}\), extended by zero, with all support entries and exits retained.
For ((j,n)=1), let (\overline j_n) be the inverse of (j\pmod n), and
define

\[
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 b_{g,n}(j)e(-h\overline j_n/n).
\tag{160.BL3}
\]

The scalar to estimate is

\[
 \mathscr R^\circ_{D,L}(X)=
 \sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi_4(g)W\!\left(\frac{X}{gnD}\right)
 \sum_{1\le h<n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n),
\tag{160.BL4}
\]

where, for the fixed level-four convention,

\[
 S^{\chi_4}_{\infty0}(4N_0,h;2n)
 =\chi_4(n)S(N_0,h;n).
\tag{160.BL5}
\]

The desired bound is

\[
 \boxed{\mathscr R^\circ_{D,L}(X)
 \ll_\varepsilon X^{1/4+\varepsilon}.}
\tag{160.BL6}
\]

The zero frequency has already been removed once.  Every (1\le h<n),
both character directions, arbitrary gcd strata, the moving support, the
real-centre factor, profiles, transitions, and endpoints must remain.

Starting only from this statement:

1. prove the exact reciprocity identity
   \[
    e(-h\overline j_n/n)
    =e(h\overline n_j/j-h/(jn))
   \]
   for all coprime (j,n), including even (j);
2. rederive the corresponding exact ((g,n,j,h)) scalar and verify that
   full \(h\)-summation reconstructs the original reciprocal row;
3. test whether the shorter modulus (j\asymp K/g<n\asymp R/g) admits a
   direct signed or low-projective-cost common-test estimate before any
   positive modulus norm;
4. retain the primitive (g=1) stratum and the complete long (h)-range;
5. price every (n\bmod j) class, projective/Sobolev/Bessel norm, level-
   (4/8) term, moving endpoint, and restored (X,D,L,R,K) power; and
6. prove (160.BL6), a strict owner-complete subrange, or the first rigorous
   residue-class, projective, long-frequency, source, or capacity
   obstruction.

For (a=\delta-\ell), a claimed method must save at least

\[
 X^{\min(a,(1-a)/2)-1/4}.
\tag{160.BL7}
\]

Additive reciprocity by itself, a shorter modulus without its class price,
full Fourier inversion, or a positive row norm is not an estimate.
Nothing may be transferred beyond this one flat-smooth owner.
