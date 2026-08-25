## 1. Result

**Scoped `level_four_spectral_matrix_no_go`, with a legal odd-character
embedding but no legal joint-matrix estimate.**  Four logically different
claims have to be kept separate.

1. The sibling discovery report proves internally, by a weight-one
   double-coset calculation for the displayed scaling matrices, the exact
   arithmetic identity
   \[
     S^{\chi _4}_{\infty,0}(4N_0,h;2n)
       =\chi _4(n)S(N_0,h;n),\qquad n\ {\rm odd}.             \tag{1.1}
   \]
   Its allowed generalized moduli are exactly \(2n\), and its convention has
   no modulus-dependent root of unity.  This is an internal algebraic result,
   not an application of the source in the next item.
2. Kıral--Young, Theorem 2.7 and (2.20), print the analogous
   \((\infty,0)\) identity only for an **even** character, in a weight-zero
   multiplier system.  Since \(\chi _4(-1)=-1\), that theorem cannot be cited
   for (1.1).  It does not source a weight-one switched-cusp Kuznetsov
   formula or its transform constants.
3. Blomer--Milićević do provide a fully legal odd-character route.
   Their Section 3 sets \(\kappa=1\) for primitive odd \(\chi _1\), and
   (2.3)--(2.5), (4.6), and Theorem 4 encode the \(\chi _4(n)\) modulus sign
   into standard-cusp twisted Kloosterman sums.  For \(q=q_1=4\), the exact
   representation is a level-\(4\) minus level-\(8\) combination, not a
   single pure-level-\(4\) cross-cusp formula.
4. The legal source route stops at the literal coefficient
   \(\widehat\gamma _{g,n}(h)\).  Blomer--Milićević's scalar formula and
   fixed-argument bound require one smooth modulus test; Deshouillers--
   Iwaniec's spectral large sieve requires one common coefficient sequence;
   and the stronger smooth two-variable theorem of Assing--Blomer--Li still
   requires a common sequence times a jointly smooth function with controlled
   derivatives.  The frozen controls supply no representation of the
   inverse-selector matrix satisfying any of those interfaces with an
   owner-saving aggregate norm.  This is an applicability gap, not a proof
   that every smooth extension, low-rank decomposition, or future matrix
   theorem is impossible.

This last item is the first source-hypothesis failure after a source-certified
odd-character embedding.  There is a second independent failure: at modulus
scale \(R/g\), the printed Blomer--Milićević Linnik range covers only
\[
 |h|\ll \frac{X}{D^2g^2}=\frac{K}{Lg^2},
 \qquad
 \frac{\#\{h\text{ in range}\}}{R/g}\ll\frac1{Dg},             \tag{1.2}
\]
The ratio is \(\asymp1/(Dg)\) only in the many-integer range
\(H_{\rm Lin}(g)\gg1\), with the dyadic constants fixed.  Once
\(g\gg\sqrt{K/L}\), with a sufficiently large fixed implied constant, the
range contains no nonzero integer.  Parseval gives no localization of the
matrix in that small slice.

The only currently licensed owner-complete positive closure remains
\[
 R\sqrt\Delta\,X^\varepsilon
   =X^{1-(\delta+\ell)/2+\varepsilon},                          \tag{1.3}
\]
which is worse than the absolute capacity \(\Delta X^\varepsilon\) by an
exponent greater than \(1/4\) at each fixed point of the strict residual
polytope, and is above the quarter target by an exponent greater than
\(3/8\) pointwise.  These strict inequalities do not provide an additional
polytope-uniform margin near the boundary.  Exact summation of the complete
\(h\)-matrix before a positive norm returns the original reciprocal row.
The target-safe \(h=0\) class can nevertheless be removed: the strict
unresolved survivor is the fully gcd-restored centered
\(h\not\equiv0\pmod n\) joint matrix.  This is not a lower bound for the
actual signed scalar and does not rule out a new vector-valued or matrix
Kuznetsov theorem.

## 2. Exact statement and hypotheses

Put
\[
 X=N_0+\xi,\quad N_0=\lfloor X\rfloor,\quad 0\leq\xi<1,
 \qquad
 D=X^\delta,\quad L=X^\ell,\quad R=\frac XD,\quad
 K=\frac{XL}{D^2},\quad \Delta=\frac RK=\frac DL.              \tag{2.1}
\]
The frozen region is
\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,                                      \tag{2.2}
\]
so \(1/4<\delta-\ell<1/2\), \(K<R\), and \(\Delta>1\).  Only the one
flat-smooth strict-UNBAL owner
\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{r\asymp R\\r\ {\rm odd}}}\chi _4(r)
 W\!\left(\frac{X}{rD}\right)
 \sum_{k\asymp K}\frac{q_L(4Xk/r^2)}{k}e(Xk/r)                \tag{2.3}
\]
is in scope.

Restore every gcd stratum by \(r=gn,\ k=gj,\ (j,n)=1\), and define
\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),              \tag{2.4}
\]
with the literal condition \(gj\asymp K\).  On \(\mathbb Z/n\mathbb Z\),
put \(\gamma _{g,n}(m)=b_{g,n}(\bar m)\) when \(m\) is a unit and
\(\bar m\) lies in the literal support, and put it equal to zero otherwise.
Its normalized transform is
\[
 \widehat\gamma _{g,n}(h)=\frac1n\sum_{m\bmod n}
 \gamma _{g,n}(m)e(-hm/n)
 =\frac1n\sum_{\substack{j\asymp K/g\\(j,n)=1}}
 b_{g,n}(j)e(-h\bar j/n).                                     \tag{2.5}
\]
Fourier inversion gives the exact, owner-complete ordinary-Kloosterman form
\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
 \chi _4(g)\chi _4(n)W\!\left(\frac{X}{gnD}\right)
 \sum_{h\bmod n}\widehat\gamma _{g,n}(h)S(N_0,h;n),           \tag{2.6}
\]
equivalently (using the internal identity (1.1)) the same expression with
\(\chi _4(n)S(N_0,h;n)\) replaced by
\(S^{\chi _4}_{\infty,0}(4N_0,h;2n)\).  Define its fully gcd-restored strict
survivor by
\[
 \mathscr R^{\ne0}_{D,L}(X)=
 \sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi _4(g)\chi _4(n)W\!\left(\frac{X}{gnD}\right)
 \sum_{\substack{h\bmod n\\h\not\equiv0\ ({\rm mod}\ n)}}
 \widehat\gamma _{g,n}(h)S(N_0,h;n).                       \tag{2.6a}
\]
The elementary Ramanujan calculation below gives
\(\mathscr R_{D,L}(X)=\mathscr R^{\ne0}_{D,L}(X)
+O_\varepsilon(X^\varepsilon)\).  One may take positive representatives
\(1\le h<n\) in (2.6a) when using the sourced same-sign formula; centered
representatives give the equivalent nonzero residue-class matrix but require
an opposite-sign formula for negative representatives.  Parseval supplies only
\[
 \sum_{h\bmod n}|\widehat\gamma _{g,n}(h)|^2
   \ll \frac{X^\varepsilon}{RK},
 \qquad
 \sum_{\substack{n\asymp R/g\\h\bmod n}}
 |\widehat\gamma _{g,n}(h)|^2
   \ll \frac{X^\varepsilon}{gK}.                              \tag{2.7}
\]
It supplies no \(h\)-localization, modulus derivatives, Mellin variation,
low rank, or projective/Schatten-one bound.

**Source card KY (generalized cusps).**  In
[Kıral--Young, arXiv:1710.00914](https://arxiv.org/html/1710.00914),
Definition 2.2 and (2.3) define generalized-cusp sums for singular cusps in
the weight-zero, even-character setting.  A scaling change contributes only
the modulus-independent factor \(e(-\alpha m+\beta n)\), by (2.7).
Proposition 2.6, (2.13)--(2.14), gives
\[
 \mathcal C_{\infty,1/r}
 =\{c\sqrt s:c\equiv0\pmod r,(c,s)=1\},\qquad
 S_{\infty,1/r}(m,n;c\sqrt s)=S(\bar s m,n;c).                 \tag{2.8}
\]
Theorem 2.7, (2.15)--(2.17), explicitly assumes that \(\chi\) is even.
Its example (2.20), at cusps \((\infty,0)\), is
\[
 S_{\infty,0}(m,n;c\sqrt N;\chi)
   =\bar\chi(c)S(\bar N m,n;c),\qquad(c,N)=1.                 \tag{2.9}
\]
For \(N=4,\ m=4N_0\), this has geometric modulus \(2c\), ordinary
Kloosterman arguments \(N_0,h\), and no further root factor.  But its even
hypothesis excludes \(\chi_4\).  Equations (3.2)--(3.4) also show that a
cross-cusp trace formula must use Fourier coefficients and Eisenstein data
computed with the same scaling matrices.

**Source card BM (legal odd character).**  In
[Blomer--Milićević, JEMS 17 (2015), 51--69](https://ems.press/content/serial-article-files/32008?nt=1),
write
\[
 S_{\chi _1}(a,b;C)=\sum_{d\bmod C}^{*}\chi _1(d)
 e\!\left(\frac{ad+b\bar d}{C}\right),\qquad q_1\mid C.      \tag{2.10}
\]
Their (2.3), p.55, holds for an arbitrary character \(\chi\pmod q\)
induced by primitive \(\chi _1\pmod{q_1}\).  With
\(m_0=m/(m,q^\infty)\), \(n_0=n(m,q^\infty)\), it states
\[
 \sum_{(c,q)=1}\chi(c)S(m,n;c)\omega(c)
 =\frac{\chi(m_0)}{\tau(\chi _1)}
   \sum_{d\mid q}\mu(d)\sum_{dq_1\mid C}
   S_{\chi _1}(m_0,n_0q_1^2;C)\omega(C/q_1).                 \tag{2.11}
\]
This identity is valid for a finitely supported \(\omega\), and more
generally under the decay assumed in the source; the literal dyadic weight
used below is finitely supported.
For \(q=q_1=4,\ \chi=\chi _4\), let
\(u=(N_0,4^\infty)=2^{v_2(N_0)}\) and \(M_0=N_0/u\).  Then (2.11)
specializes exactly to
\[
 \sum_{n\ {\rm odd}}\chi _4(n)S(N_0,h;n)\omega(n)
 =\frac{\chi _4(M_0)}{\tau(\chi _4)}
 \left(\sum_{4\mid C}-\sum_{8\mid C}\right)
 S_{\chi _4}(M_0,16uh;C)\omega(C/4).                         \tag{2.12}
\]
Thus the standard-cusp levels are \(4\) and \(8\), and the difference
selects \(C=4n\) with \(n\) odd.  Section 3, p.57, sets \(\kappa=1\) for
odd \(\chi _1\).  In (4.1)--(4.6), pp.61--62, the common scalar test has
Bessel transforms
\[
 \dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},
 \quad
 \widetilde g(t)=\frac{i\,t^\kappa}{2\sinh(\pi t)}
 \int_0^\infty\{J_{2it}(x)-(-1)^\kappa J_{-2it}(x)\}
 g(x)\frac{dx}{x}.                                           \tag{2.13}
\]
The exact spectral ledger (4.6) and Theorem 4, pp.67--68, is
holomorphic \(H\), Maaß \(M\), and continuous Eisenstein \(E\), at every
level \(dq_1\), with the fixed Fourier arguments \(m_0,n_0q_1^2\).  The
test is smooth and compactly supported; it is common to the modulus sum.

Theorem 1, pp.52--53, assumes positive fixed Fourier arguments, a fixed
arithmetic weight \(f:(\mathbb Z/q\mathbb Z)^*\to\mathbb C\), and a fixed
smooth compactly supported \(f_\infty\).  It states uniformly in
\(mn\leq C_0^2\)
\[
 \sum_{(c,q)=1}\frac{S(m,n;c)}{\sqrt c}f(c)f_\infty(c/C_0)
 \ll_{f_\infty,\varepsilon}
 C_0^{1/2+2\theta}\|\widehat f\|_1(mnq)^\varepsilon.          \tag{2.14}
\]
Here \(\|\widehat f\|_1\) is the normalized \(q\)-Mellin norm defined in
their (1.2).  The theorem permits the fixed arithmetic weight \(\chi _4\);
it does not include an additional arbitrary modulus-frequency matrix at no
cost.
Equation (2.5) has the corresponding fixed-character factor
\(q_1^{1/2}\); it is harmless at \(q_1=4\).  The source calls
\(mn\leq C_0^2\) the Linnik range and says only that the complementary
range would require a different transform analysis; no complementary
uniform theorem is printed.

**Source card DI (trace formula and spectral large sieve).**  In
[Deshouillers--Iwaniec, Invent. Math. 70 (1982), 219--288](https://gdz.sub.uni-goettingen.de/id/PPN356556735_0070?tify=%7B%22view%22%3A%22info%22%2C%22pages%22%3A%5B243%5D%7D),
Theorem 1, p.228, has one \(C_c^3(0,\infty)\) test
\(\varphi(4\pi\sqrt{mn}/\gamma)\) for fixed \(m,n\) and a fixed cusp
pair.  Its displayed same-sign side contains holomorphic, Maaß, and
continuous Eisenstein pieces, with the \(J\)-Bessel transforms (1.21)--
(1.22); (1.23) is the weight-zero opposite-sign \(K\)-transform.  This
source is not itself an odd-nebentypus, weight-one theorem.

Theorem 2, p.230, fixes a cusp \(\mathfrak a\) of \(\Gamma_0(q)\), assumes
\(T\geq1\), \(N\geq1/2\), and \(\varepsilon>0\), and uses one sequence
\((a_n)_{N<n\leq2N}\).  It is the relevant interface audit: each of its
holomorphic, Maaß, and Eisenstein quadratic forms contains that **same one
sequence**, and each is bounded by
\[
 \bigl(T^2+\mu(\mathfrak a)N^{1+\varepsilon}\bigr)
 \|a_N\|_2^2.                                                  \tag{2.15}
\]
Theorem 5, p.232, additionally assumes \(Y\geq1\) and treats exceptional
parameters but still with that same sequence:
\[
 \sum_{\lambda_j\ {\rm exceptional}}Y^{2i\kappa_j}
 \left|\sum_{N<n\leq2N}a_n\rho_{j\mathfrak a}(n)\right|^2
 \ll
 (1+\sqrt{\mu(\mathfrak a)NY})
 (1+\sqrt{\mu(\mathfrak a)N^{1+\varepsilon}})\|a_N\|_2^2.    \tag{2.16}
\]
These are accurate common-sequence interface checks.  Their printed form is
not itself the odd-nebentypus, weight-one, level-\(4/8\) large sieve required
here.

**Source card ABL (strongest near-matrix comparison).**  Assing--Blomer--
Li, [*Uniform Titchmarsh divisor problems*, Theorem 2.4, p.5](https://arxiv.org/pdf/2005.13915),
allows
\[
 \sum_{(c,r)=1}\frac1c\sum_m\alpha_mF(m,c)
 S(m\bar r,\pm n;sc),                                        \tag{2.17}
\]
where \(n,r,s\) are positive integers with \((r,s)=1\), \(M,C,Z\geq1\),
\(\alpha_m\) is one arbitrary sequence, and \(F\) is supported on
\([M,2M]\times[C,2C]), and
\(F^{(\nu_1,\nu_2)}\ll Z^{\nu_1+\nu_2}M^{-\nu_1}C^{-\nu_2}\).
The mixed-derivative inequality is required for every displayed derivative
order in the theorem.  It assumes \((Mn/(s^2rC^2))^{1/2}\ll Z\) and bounds
(2.17) by
\[
 \|\alpha\|_2 Z\left(
 Z(sM)^{1/2}+Z^2s\sqrt r+
 \frac{(M(n,rs))^{1/4}(ZsC)^{1/2}}{r^{1/4}}+
 \frac{Z^{3/2}(n,rs)^{1/4}C^{1/2}r^{1/4}s}{M^{1/4}}
 \right)(CMZnrs)^\varepsilon.                                \tag{2.18}
\]
It permits controlled smooth joint \(m,c\)-dependence.  The frozen statement
does not supply a representation of the literal matrix as
\(\alpha_mF(m,c)\) with derivative and aggregate norms small enough to save
the owner.  The theorem also does not itself contain the \(\chi _4(c)\)
modulus twist or the level-\(4/8\) twisted sums of (2.12).

## 3. Proof or derivation

**The character and cusp seam.**  For the internal weight-one scaling
\(\sigma_\infty=I\),
\(\sigma_0=\left(\begin{smallmatrix}0&-1/2\\2&0\end{smallmatrix}\right)\),
the double coset has lower-left entry \(2n\) exactly when \(n\) is odd;
the sibling calculation gives (1.1).  It is legitimate to use this as an
internal arithmetic lemma.  It is not legitimate to call it Kıral--Young
(2.20): their Definition 2.2 uses an even character as a weight-zero
multiplier and their Theorem 2.7 repeats that hypothesis.  Changing scaling
matrices cannot repair parity, since (2.7) changes the sum only by a single
factor independent of the modulus.

Blomer--Milićević repairs the source problem independently.  Apply (2.11)
with source arguments \(m=N_0,n=h\), then use
\(m_0=M_0\), \(n_0=uh\), and \(\mu(4)=0\).  This gives (2.12).  The
twisted Bessel geometry for the positive-index same-sign formula is exact:
\[
 \frac{4\pi\sqrt{M_0(16uh)}}{4n}
   =\frac{4\pi\sqrt{N_0h}}{n}
   =\frac{4\pi\sqrt{(4N_0)h}}{2n}.                            \tag{3.1}
\]
Thus no power of \(2\), cusp width, or Bessel root has been lost.  The
fixed arithmetic constants \(\chi_4(M_0)/\tau(\chi_4)\) and the Möbius
sign between levels \(4\) and \(8\) must remain.

Equation (2.11) is algebraic and can be applied for each fixed \(g,h\) with
\(\omega(n)=W(X/(gnD))\widehat\gamma_{g,n}(h)\).  The next, spectral
step is not licensed by the frozen controls.  In Blomer--Milićević's
normalization it would require a family of scalar tests satisfying, on
\(n\asymp R/g\),
\[
 f_{\infty,g,h}(n/(R/g))
   =\sqrt n\,W\!\left(\frac{X}{gnD}\right)
     \widehat\gamma_{g,n}(h),                                 \tag{3.2}
\]
up to fixed normalizing constants.  In cross-cusp normalization the same
requirement is
\[
 \Phi_{g,h}\!\left(\frac{4\pi\sqrt{N_0h}}n\right)
   =2nW\!\left(\frac{X}{gnD}\right)
     \widehat\gamma_{g,n}(h).                                 \tag{3.3}
\]
The inverse \(\bar j\pmod n\), the unit indicator, and the literal entry
and exit in (2.5) change arithmetically with \(n\).  Hence (3.2) is not a
single test supplied by the source theorem, and the frozen data do not
provide a common Bessel test with controlled norm for (3.3).  Pointwise
interpolation makes an identity possible, but the available estimates give
no owner-saving Sobolev or spectral-bandwidth bound for such an interpolant.
Likewise, a generic finite SVD combined only with (2.7) supplies the
Hilbert--Schmidt norm, while summing positive scalar estimates over its
rank-one pieces introduces a trace/projective price for which the frozen
data give no saving bound.  Thus the common-sequence hypotheses in
(2.15)--(2.16) have not been verified.  This does not exclude a better
controlled representation exploiting additional arithmetic structure.

Assing--Blomer--Li (2.17) is a hostile check against the claim that no
theorem permits any joint dependence.  It does permit a smooth
\(F(h,n)\), after Kloosterman symmetry, but the frozen controls provide
neither the required derivative bounds nor a factorization of the literal
\(\widehat\gamma_{g,n}(h)\) as a common \(\alpha_h\) times such an \(F\)
with owner-saving aggregate norms.  Moreover, at
\(M\asymp C\asymp R/g\), fixed source argument \(N_0\asymp X\) forces
its smoothness parameter to satisfy \(Z\gg\sqrt{Dg}\), even before pricing
the unproved controlled factorization and the \(\chi_4\) twist.  Thus
(2.17) supplies no owner-saving capacity for (2.6) from the frozen data.

**The Linnik seam.**  For fixed \(g\), put \(C_g=R/g\).  Theorem 1 applies
only when
\[
 N_0h\leq C_g^2,\qquad
 0<h\ll H_{\rm Lin}(g):=\frac{C_g^2}{N_0}
 \asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2}.                       \tag{3.4}
\]
But (2.6) contains a complete residue system \(0\leq h<n\asymp C_g\),
so the covered fraction is \(\ll1/(Dg)\), and is
\(\asymp1/(Dg)\) only when \(H_{\rm Lin}(g)\gg1\), with the dyadic
constants fixed.  For \(g\gg\sqrt{K/L}\), with a sufficiently large fixed
implied constant, (3.4) contains no nonzero integer.  Equation (2.7) gives
no license to discard or dominate the complementary frequencies.
The \(h=0\) class is outside the positive-index theorem and is treated
elementarily through \(S(N_0,0;n)=\mathfrak c_n(N_0)\); its complete
owner contribution is \(O(X^\varepsilon)\).  One may use representatives
\(1\leq h<n\) for the strict survivor (2.6a), so no opposite-sign theorem
is required.  If centered signed
representatives are chosen instead, Blomer--Milićević only remarks that
an opposite-sign formula is possible; Theorem 4 does not print the
weight-one \(K\)-transform or its cross-cusp constants.

**The complete spectrum seam.**  For the legal (2.12) route, no spectral
piece may be omitted.

- At both levels \(4\) and \(8\), \(\kappa=1\).  The Maaß basis includes
  real \(t\), \(t=0\) if present, and exceptional \(t\in i(0,1/2)\).
- The holomorphic tower has \(k\equiv1\pmod2\) and \(k>1\), hence
  \(k=3,5,\ldots\).
- The Eisenstein term integrates over every singular cusp.  The criterion
  (5.1), p.64, is \(4\mid[w,Q/w]\).  It gives the two cusps
  \(\infty,0\) at \(Q=4\), and all four cusps
  \(\infty,0,1/2,1/4\) at \(Q=8\).
- Section 3's bases explicitly contain newforms and oldclass shifts.  At
  level \(4\), primitive conductor \(4\) leaves no proper-divisor
  oldspace.  At level \(8\), the basis contains both level-\(8\) newforms
  and oldforms lifted from level \(4\).
- The exact printed formula is \(H+M+E\).  It displays no separate
  residual term; a Maaß form with \(t=0\) is already in \(M\).  Conversely,
  a custom weight-one cross-cusp formula cannot be assigned an extra
  residual or limit-of-discrete-series term, or declared free of one,
  without a separate primary-source/scattering calculation.

**Capacity and self-return.**  Parseval plus the gcd-sensitive Weil/complete
Kloosterman second-moment closure gives, uniformly through every \(g\)-row,
\[
 |\mathscr R_{D,L}(X)|
 \ll R\sqrt{R/K}\,X^\varepsilon
 =R\sqrt\Delta\,X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon}.                          \tag{3.5}
\]
Since the accepted envelope is at most \(\Delta X^\varepsilon\), the
excess exponent is
\[
 \left(1-\frac{\delta+\ell}{2}\right)-(\delta-\ell)
 =1-\frac{3\delta}{2}+\frac\ell2>\frac14.                    \tag{3.6}
\]
Also \(\delta+\ell<3/4\) on (2.2), so the exponent in (3.5) is
greater than \(5/8\), more than \(3/8\) above the quarter target, at every
fixed point of the strict region.  These are pointwise strict inequalities;
no additional fixed margin is uniform as a boundary is approached.  The
extra residual-polytope inequality creates no improving chamber.

If (2.5) is inserted in (2.6) and the complete \(h\)-sum is performed
before taking a positive norm, additive orthogonality returns the original
reciprocal row exactly.  Smooth-weight-first completion instead yields the
Ramanujan/additive expression of absolute capacity
\(\Delta X^\varepsilon\).  Kuznetsov inversion without a new matrix
estimate is therefore a self-return on the complete \(h\)-sum.  Removing
the target-safe \(h=0\) complement leaves the strict survivor (2.6a), but
does not by itself estimate that survivor.

## 4. First doubtful or unproved step

For the pure-level-\(4\), switched-cusp route, the first source error would
be to cite Kıral--Young (2.20) for \(\chi_4\), or to transplant their
weight-zero transform normalization to weight one.  Their theorem assumes
an even character.  The internal double-coset identity (1.1) may be used as
an internal lemma, but it does not by itself prove a weight-one
Bruggeman--Kuznetsov formula, its Fourier normalizations, or its complete
spectral ledger.

The Blomer--Milićević level-\(4/8\) route removes that source error.  On
this legal route, the first unproved step is the replacement
\[
 \widehat\gamma_{g,n}(h)
 \quad\rightsquigarrow\quad
 a_g(h)V_{g,h}(n/(R/g))                                      \tag{4.1}
\]
with a common \(h\)-sequence and a family of smooth modulus tests whose
Bessel/Sobolev norms have an owner-saving aggregate bound.  Nothing in
(2.7) proves (4.1); the moving inverse map and support explain why no such
control follows from the available Parseval statement, but they do not prove
that every controlled interpolation or arithmetic decomposition is
impossible.  Treating \(\widehat\gamma_{g,n}(h)\) as independent of \(n\),
or applying a spectral large sieve rowwise and then summing positive norms
without first proving the required aggregate control, is the first
unsupported coefficient step.  It occurs before any Maaß, holomorphic,
exceptional, or Eisenstein estimate can be used.

Two spectral-ledger shortcuts are likewise unsupported.  First, the legal
Blomer--Milićević implementation includes the level-\(8\) oldclasses from
level \(4\); the statement "the oldspace is empty" is true only for the
pure level-\(4\), primitive-character space, not for the complete source
embedding (2.12).  Second, Blomer--Milićević Theorem 4 prints exactly
\(H+M+E\) and no ad hoc \(\mathcal R^\pm\); a separate residual or
weight-one limit term in a custom switched-cusp formula is neither proved
present nor proved absent by the audited sources.  In particular, a
\(t=0\) Maaß cusp form, if present, already belongs to \(M\).

The missing result would have to be a vector-valued fixed-level trace
formula or matrix large sieve controlling the literal family (2.5), with
its common Bessel transforms, long frequencies outside (3.4), every gcd
stratum, and all the spectrum in Section 3, by a bound strictly below the
accepted envelope.  No audited theorem states such a result.

The rigorous source verdict is therefore only that none of the audited
theorems applies to the literal strict survivor (2.6a) with an owner-saving
norm justified by the frozen hypotheses.  It is not a categorical
nonfactorization or impossibility theorem.

## 5. Required control test and outcome

1. **`exact_gcd_restored_inverse_first_identity` -- pass.**  Equations
   (2.4)--(2.6) retain \(r=gn,\ k=gj,\ (j,n)=1\), the \(1/(gj)\) factor,
   and every \(g\)-stratum.  No coprime-only row is promoted as the owner.
2. **`chi4_modulus_sign_and_level_four_embedding` -- pass internally;
   source-qualified.**  The internal double-coset identity is (1.1).
   Kıral--Young cannot certify it for odd \(\chi_4\); Blomer--Milićević
   certifies the odd sign by the level-\(4/8\) identity (2.12).
3. **`cusp_modulus_progression_and_root_of_unity` -- pass.**  The internal
   cross-cusp moduli are \(2n\), \(n\) odd, with geometric root \(1\) in
   the stated convention.  The source-certified standard-cusp moduli are
   \(4\mid C\) minus \(8\mid C\), selecting \(C=4n\); the fixed Gauss and
   Möbius factors are displayed in (2.12).  Equation (3.1) checks the
   complete Bessel root normalization for the positive-index same-sign
   formula.
4. **`joint_gammahat_n_h_coefficient_geometry` -- fail as a source input.**
   The frozen data supply neither a common-sequence representation nor a
   controlled smooth modulus extension of the literal matrix (2.5) with an
   owner-saving norm.  Only the Hilbert norms (2.7) are available; no
   categorical nonfactorization is claimed.
5. **`real_centre_profile_and_endpoint_ownership` -- pass.**  The integer
   \(N_0\) is the Kloosterman argument; \(e(\xi j/n)\), \(q_L\), \(W\),
   the unit condition, and all literal support entries and exits stay in
   (2.4)--(2.6).  No endpoint or real-centre term is deleted.
6. **`Kuznetsov_test_Bessel_transform_hypotheses` -- fail for the owner.**
   The legal source kernels are (2.13), but the required samples are
   (3.2)--(3.3).  The frozen statement gives no modulus-derivative or
   transformed-family bound for those samples.  Point interpolation alone
   does not provide an owner-saving uniform source norm.  The Linnik range
   covers at most the slice (3.4), subject to the discrete qualifications
   following that equation.
7. **`holomorphic_Maass_Eisenstein_exceptional_ledger` -- pass as an
   audit, not as an estimate.**  The level-\(4/8\) Maaß, exceptional,
   odd-weight holomorphic, all-singular-cusp continuous, newform, and
   oldform terms are recorded above.  No unsourced residual term is added
   and no printed spectral term is discarded.
8. **`spectral_large_sieve_common_sequence_and_norms` -- fail.**
   Deshouillers--Iwaniec Theorems 2 and 5 require one sequence in all
   spectral forms, with the fixed-cusp, \(T,N,Y\) hypotheses recorded in
   Section 2, and are not themselves an odd-nebentypus level-\(4/8\) large
   sieve.  Assing--Blomer--Li assumes positive coprime level parameters, a
   single sequence, and all stated smooth derivative bounds.  No
   owner-saving representation satisfying either interface follows from
   (2.7).
9. **`full_polytope_D_L_R_K_Delta_capacity` -- fail.**  The legal positive
   closure (3.5) exceeds \(\Delta\) by the exponent (3.6) and exceeds the
   quarter target by an exponent greater than \(3/8\) pointwise on the
   strict region.  No additional fixed margin is uniform near its boundary.
10. **`Ramanujan_original_wave_and_spectral_self_return` -- pass, with a
    strict survivor.**  The \(h=0\) Ramanujan term is target-safe; hence
    (2.6a), not the whole wave, is the smallest unresolved object isolated
    here.  Summing the complete \(h\)-matrix before a positive norm returns
    the original row, while smooth-first returns \(\Delta X^\varepsilon\).
11. **`actual_character_vs_unsigned_adversary` -- fail after positive
    separation.**  Identity (2.12) genuinely preserves \(\chi_4\), but
    rowwise Cauchy, Schatten, or spectral large-sieve norms are invariant
    under arbitrary unit row signs.  They erase the only cross-modulus
    direction and give (3.5), so they do not distinguish the actual
    character from an unsigned/adversarial matrix.
12. **`downstream_owner_and_exponent_scope` -- pass.**  This audit concerns
    only the one flat-smooth strict-UNBAL owner.  It proves no claim about
    clipped, starred, transition, hard-TOP, BAL, other UNBAL, complete
    M9-M2, endpoint, M9, or the global circle exponent.

## 6. Dependencies and exact artifacts used

The project dependencies, read for this audit, are:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`, task `kuznetsov_source_hypothesis_audit`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`, especially (3.28)--(3.36);
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/bettin_chandee_wright_kloosterman.md`;
- `rounds/codex-managed/m9-m1-near-product-delta-salie/reports/delta_kuznetsov_source_hostile_audit.md`;
- the sibling `level_four_kloosterman_embedding_attack.md`, used only for
  its internal double-coset identity and for the requested source seam; and
- the sibling `blind_joint_matrix_spectral_feasibility.md`, inspected only
  to identify transform/residual/oldspace assertions needing primary-source
  qualification, not as a source of external facts; and
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_post_unmask_source_hypothesis_audit.md`, used for the present
  source-hypothesis, discreteness, survivor, and scope repairs.

The primary sources and exact locations are:

1. E. M. Kıral and M. P. Young,
   [*Kloosterman sums and Fourier coefficients of Eisenstein series*, arXiv:1710.00914](https://arxiv.org/html/1710.00914):
   Definition 2.2 and (2.3), printed p.2; scaling rule (2.7), p.3;
   Proposition 2.6 and (2.13)--(2.14), p.5; Theorem 2.7 and
   (2.15)--(2.17), pp.5--6; example (2.20) and remark (2.24), p.7;
   Eisenstein Fourier expansions (3.2)--(3.4), p.8.
2. V. Blomer and D. Milićević,
   [*Kloosterman sums in residue classes*, JEMS 17 (2015), 51--69,
   DOI 10.4171/JEMS/498](https://ems.press/content/serial-article-files/32008?nt=1):
   Theorem 1 and Linnik range (1.3), pp.52--53; character encoding
   (2.3), p.55, and arbitrary-weight identity (2.4), fixed-character
   bound (2.5), p.56; parity and oldclass bases, Section 3, pp.57--60;
   Bessel tests and (H+M+E), (4.1)--(4.11), pp.61--63; singular-cusp
   criterion (5.1), p.64; generalized Kuznetsov Theorem 4, pp.67--68.
3. J.-M. Deshouillers and H. Iwaniec,
   [*Kloosterman Sums and Fourier Coefficients of Cusp Forms*, Invent.
   Math. 70 (1982), 219--288, DOI 10.1007/BF01390728](https://doi.org/10.1007/BF01390728):
   Kuznetsov Theorem 1 and transforms (1.19)--(1.23), p.228; spectral
   large-sieve Theorem 2, p.230; weighted exceptional Theorem 5, p.232.
   The linked [official GDZ scan](https://gdz.sub.uni-goettingen.de/id/PPN356556735_0070?tify=%7B%22view%22%3A%22info%22%2C%22pages%22%3A%5B243%5D%7D)
   was used to verify the printed pages.
4. E. Assing, V. Blomer, and J. Li,
   [*Uniform Titchmarsh divisor problems*, arXiv:2005.13915](https://arxiv.org/pdf/2005.13915):
   Theorem 2.4, printed p.5, and the common-sequence spectral quantities
   (3.2), printed p.7.

All work was analytical and source-comparative.  No numerical experiment
or heuristic sampling was used.

## 7. Recommended state effect

**Retain** `M9-M2-smooth-unbalanced-three-quarter-estimate` as open and
record only the scoped label `level_four_spectral_matrix_no_go`.

The promotable source-audit content is:

- the internal pure-level-\(4\) switched-cusp arithmetic identity is
  distinct from Kıral--Young's even-character theorem and cannot inherit
  weight-one spectral constants from it;
- Blomer--Milićević supplies a legal odd-character, weight-one
  architecture via an exact level-\(4/8\) standard-cusp combination, with
  every Maaß, exceptional, holomorphic, Eisenstein, newspace, and oldspace
  term retained;
- the first source-certified failure is the literal joint
  \((n,h)\)-coefficient/common-test seam (4.1): the frozen data supply no
  controlled representation with an owner-saving norm.  This is followed
  independently by the discretely qualified Linnik-range gap (3.4);
- no separate residual term or custom weight-one switched-cusp transform
  normalization is source-certified by the audited papers; and
- the only unconditional owner-complete positive capacity remains
  \(R\sqrt\Delta X^\varepsilon\), while the exact alternatives are the
  original-wave self-return or the equal-capacity Ramanujan return.

The smallest unresolved object isolated here is the fully gcd-restored
nonzero-frequency matrix (2.6a), equivalently the centered
\(h\not\equiv0\pmod n\) matrix; its \(h=0\) complement is
\(O_\varepsilon(X^\varepsilon)\) and target-safe.  A future repair must
prove a genuinely vector-valued Bessel/Sobolev or spectral-large-sieve
estimate for this literal family, preserve \(\chi_4(n)\) until the final
scalar absolute value, cover the complement of (3.4), and include all
level-\(4/8\) spectral terms.  Nothing here excludes a new controlled
factorization or matrix theorem beyond the frozen source interfaces.
No complete-UNBAL, BAL, TOP, M9-M2, M9-M1, endpoint, M9, internal
global-exponent, or Gauss-circle claim changes.
