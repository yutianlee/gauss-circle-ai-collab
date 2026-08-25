# Conductor Round 160 reciprocity seed

This is candidate evidence only.

For ((j,n)=1), choose inverses (\overline j_n\pmod n) and
(\overline n_j\pmod j).  Since

\[
 j\overline j_n+n\overline n_j\equiv1\pmod{jn},
\]

one has

\[
 \frac{\overline j_n}{n}+\frac{\overline n_j}{j}
 \equiv\frac1{jn}\pmod1,
\]

and therefore

\[
 \boxed{
 e(-h\overline j_n/n)=e(h\overline n_j/j-h/(jn)).}
\tag{160.C1}
\]

Substitution into the accepted inverse-selector coefficient gives

\[
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
 e(h\overline n_j/j-h/(jn)).
\tag{160.C2}
\]

The arithmetic inverse is now periodic in (n\pmod j), with
(j\asymp K/g<n\asymp R/g).  The remaining factors are smooth on fixed
dyadic cells, but the support itself moves with (n).  Any decomposition
must therefore price:

- all (n\bmod j) classes and two-adic subclasses;
- the primitive (g=1) contribution;
- every (1\le h<n), not just a short Linnik band;
- the common-test projective and modulus-Sobolev norm;
- every level-(4/8) spectral piece if a trace formula is used; and
- entries, exits, zero extension, and real-centre factors.

If (a=\delta-\ell), the minimum net saving is

\[
 X^{\beta(a)-1/4},\qquad
 \beta(a)=\min(a,(1-a)/2).
\tag{160.C3}
\]

At (a=1/3), this is (X^{1/12}).  Full (h)-summation must be run as a
control: it reconstructs the original reciprocal row exactly.  Thus the
candidate mechanism can succeed only through an interaction of the
centered nonzero-frequency restriction with the shorter (j)-modulus
before a positive norm.  Whether its complete class/projective price saves
or restores (160.C3) is the frozen Round-160 question.
