# Level-four embedding of the inverse-first M2 matrix

Campaign: `m9-m2-unbalanced-level-four-kuznetsov-matrix-gate`

Task: `level_four_kloosterman_embedding_attack`

Role: discovery

Starting graph SHA-256: `7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789`

## 1. Result

**`level_four_spectral_matrix_no_go`.**  There is an exact, sign-preserving
fixed-level-four **arithmetic** embedding.  It is the switched cusp pair
\((\infty,0)\) for \(\Gamma_0(4)\), nebentypus \(\chi_4\), and weight
parity \(\kappa=1\).  With the scaling matrices

\[
 \sigma_\infty=I,
 \qquad
 \sigma_0=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\]

the allowed generalized moduli are exactly \(2n\) with \(n\) odd, and

\[
 \boxed{
 S^{\chi_4}_{\infty 0}(4N_0,h;2n)
   =\chi_4(n)S(N_0,h;n).}
 \tag{1.1}
\]

There is no modulus-dependent root of unity in (1.1).  A change of slash,
Fourier-coefficient, or Bessel convention can contribute one global unit,
but not a factor depending on \(n\) or \(h\).  Formula (1.1) is valid for
all integer \(h\), including \(h=0\), and for every gcd
\((N_0,n)\).  Thus the hoped-for character-to-level algebra is real, not
an obstruction.  Formula (1.1) is proved internally by double-coset
algebra; it is not, by itself, a source-certified weight-one
\((\infty,0)\) Kuznetsov formula.  The source-certified odd-character route
used below is the distinct Blomer--Milićević level-\(4\) minus level-\(8\)
standard-cusp encoding (2.7).

After restoring \(r=gn\), \(k=gj\), \((j,n)=1\), the complete flat owner
is exactly

\[
 \mathscr R_{D,L}(X)
 =\sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi_4(g)W\!\left({X\over gnD}\right)
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n).
 \tag{1.2}
\]

The obstruction begins at the next interface.  Kuznetsov has fixed
Fourier indices and one controlled scalar modulus test.  In (1.2), the
second index \(h\) ranges through a complete residue system depending on
the modulus, while

\[
 \widehat\gamma_{g,n}(h)
 ={1\over n}\sum_{\substack{j\asymp K/g\\(j,n)=1}}
 b_{g,n}(j)e(-h\overline j_n/n)                              \tag{1.3}
\]

is a genuinely joint arithmetic matrix in \((n,h)\).  The frozen hypotheses
prove neither a common \(h\)-sequence times a smooth modulus test nor a
simultaneously low-projective-cost, modulus-smooth decomposition of (1.3).
The automatic norms are only

\[
 \sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
 \ll {X^\varepsilon\over RK},
 \qquad
 \sum_{\substack{n\asymp R/g\\h\bmod n}}
 |\widehat\gamma_{g,n}(h)|^2
 \ll {X^\varepsilon\over gK}.                               \tag{1.4}
\]

No Fourier localization in \(h\) follows.  In particular, for fixed
same-sign positive indices at modulus scale \(C=R/g\), the
Blomer--Milićević Linnik range is

\[
 N_0|h|\ll C^2,
 \qquad
 |h|\ll H_{\mathrm{Lin}}(g):={C^2\over N_0}
 \asymp {X\over D^2g^2}={K\over Lg^2}.                       \tag{1.5}
\]

The literal matrix has \(C\) frequencies, and

\[
 {H_{\mathrm{Lin}}(g)\over C}\asymp {1\over Dg}.            \tag{1.6}
\]

For \(g\gg\sqrt{K/L}\), with a sufficiently large fixed implied constant,
not even one nonzero frequency is in that range.  Parseval gives no right
to put the matrix mass in (1.5).  For negative \(h\), (1.5) remains the
corresponding small-Bessel-argument scale, but the cited theorem itself is
same-sign and is not being applied to that range.

If (1.3) is expanded and the complete \(h\)-sum is performed, additive
orthogonality gives the original reciprocal row exactly.  If instead one
uses the only unconditional coefficient-blind closure, the exact complete
Kloosterman second moment gives

\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon R\sqrt\Delta\,X^\varepsilon
 ={X\over\sqrt{DL}}X^\varepsilon.                            \tag{1.7}
\]

This is the already diagnosed rough inverse-first capacity, not a spectral
gain.  It exceeds both branches of the accepted envelope by fixed powers
throughout the full strict residual polytope.  A canonical point-mass
interpolation in the modulus makes a scalar Kuznetsov identity legal but
has spectral/Sobolev width comparable with the number of modulus samples.
No estimate better than the separately available coefficient-blind closure
(1.7) is derived from that interpolation here.  The frozen hypotheses prove
no controlled low-projective-cost separation of the literal matrix; a
better decomposition exploiting its arithmetic structure is not excluded.

Consequently the level-four character embedding succeeds, but the frozen
inputs do not supply the common controlled test required by standard
fixed-index Kuznetsov or a standard spectral large sieve.  Summing the
inverse Fourier matrix before a positive norm is an exact self-return; the
available termwise positive modulus closures are coefficient-blind and lose
the cross-modulus character direction.  This is a scoped missing-interface
no-go from the current controls, not a lower bound for the actual
\(\chi_4\)-weighted scalar and not a no-go for a new scalar decomposition or
vector-valued trace formula acting directly on (1.3).  On the internal
pure-level-\(4\) route there is also an earlier source gap: a
convention-matched odd-weight switched-cusp trace formula has not been
established here.  On the source-certified level-\(4/8\) route, the first
project failure is the joint coefficient/common-test seam quantified above.

## 2. Exact statement and hypotheses

Let \(X=N_0+\xi\), where \(N_0=\lfloor X\rfloor\) and
\(0\leq\xi<1\), and put

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 R={X\over D},\qquad K={XL\over D^2},\qquad
 \Delta={R\over K}={D\over L}.                               \tag{2.1}
\]

The frozen region is

\[
 {1\over4}\leq\delta<{1\over2},\qquad
 0\leq\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463,                                     \tag{2.2}
\]

so \(1/4<\delta-\ell<1/2\), \(K<R\), and \(\Delta>1\).
Only one literal flat-smooth strict-UNBAL component is in scope:

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{r\asymp R\\r\ \mathrm{odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\asymp K}{q_L(4Xk/r^2)\over k}e(Xk/r).               \tag{2.3}
\]

All actual smooth cutoffs, their entries and exits, the Vaaler profile,
and any endpoint convention belonging to this frozen owner remain in the
symbols below.  Write \(r=gn\), \(k=gj\), with \((j,n)=1\), and zero
extend the \(j\)-coefficient to \(\mathbb Z/n\mathbb Z\):

\[
 b_{g,n}(j)=
 {q_L(4Xj/(gn^2))\over gj}e(\xi j/n),                         \tag{2.4}
\]

with its literal support \(gj\asymp K\).  Define on residues

\[
 \gamma_{g,n}(m)=
 \begin{cases}
 b_{g,n}(\overline m_n),&(m,n)=1\text{ and }\overline m_n
                         \text{ lies in the literal support},\\
 0,&(m,n)>1,
 \end{cases}
 \qquad
 \widehat\gamma_{g,n}(h)={1\over n}
 \sum_{m\bmod n}\gamma_{g,n}(m)e(-hm/n).                    \tag{2.5}
\]

For the positive/negative spectral split, choose the centered representative

\[
 -\frac{n-1}{2}\le h\le\frac{n-1}{2},                       \tag{2.6}
\]

and zero-pad every row to a common \(|h|\ll R/g\) column set.  Periodicity
of both \(\widehat\gamma_{g,n}(h)\) and (1.1) makes this a convention rather
than a change of the scalar.

For comparison with the source-certified odd-character route, fix one
common arithmetic modulus weight \(\omega\), put

\[
 u=(N_0,4^\infty)=2^{v_2(N_0)},\qquad M_0=N_0/u,
\]

and define the standard-cusp twisted sum

\[
 S_{\chi_4}(a,b;C)
 :=\sum_{d\bmod C}^{*}\chi_4(d)
 e\!\left(\frac{ad+b\overline d}{C}\right).
\]

With
\(\tau(\chi_4)=\sum_{a\bmod4}\chi_4(a)e(a/4)=2i\),
Blomer--Milićević equation (2.3) specializes exactly to

\[
 \begin{aligned}
 &\sum_{\substack{n\ge1\\n\ \mathrm{odd}}}
   \chi_4(n)S(N_0,h;n)\omega(n)\\
 &\quad=\frac{\chi_4(M_0)}{\tau(\chi_4)}
 \left\{
 \sum_{\substack{C\ge1\\4\mid C}}
 S_{\chi_4}(M_0,16uh;C)\omega(C/4)
 -
 \sum_{\substack{C\ge1\\8\mid C}}
 S_{\chi_4}(M_0,16uh;C)\omega(C/4)
 \right\}.                                                   \tag{2.7}
 \end{aligned}
\]

The first and second sums on the right are standard-cusp level-\(4\) and
level-\(8\) families, respectively.  Formula (2.7), including its Gauss
factor, index \(16uh\), and minus sign, is the source-certified
odd-character implementation.  It is distinct from the internal
pure-level-\(4\), switched-cusp arithmetic identity (1.1), although both
encode the same odd-modulus character.

Then the following proposition is proved.

> **Proposition (exact level-four embedding and standard spectral-matrix
> obstruction).**  On \(\Gamma_0(4)\) with primitive odd character
> \(\chi_4\), weight parity \(\kappa=1\), cusps \((\infty,0)\), and the
> scaling matrices displayed in Section 1, (1.1) and (1.2) hold exactly.
> This is an internal arithmetic statement, not a promoted pure-level-\(4\)
> trace formula.  The source-certified same-sign spectral comparison uses
> the level-\(4/8\) standard-cusp identity (2.7).
> Every gcd stratum, \(e(\xi j/n)\), literal profile, and support face is
> retained.  The \(h=0\) term is \(O_\varepsilon(X^\varepsilon)\).
> For fixed positive \(h\), the same-sign fixed-argument Linnik range is
> (1.5), while the full coefficient has only (1.4).  For negative \(h\),
> (1.5) is only a small-Bessel scale in this report, not an application of
> that theorem.  No common spectral coefficient sequence with a controlled
> scalar modulus test is proved.  Exact
> expansion of the joint coefficient followed by \(h\)-orthogonality
> returns the original row.  The automatic positive \(L^2\) closure is
> (1.7), which is strictly worse than the accepted envelope on (2.2).
> Hence the clean level-four identity alone gives neither a quarter bound
> nor a further strict spectral reduction of the centered \(h\ne0\)
> survivor.

The external-source status is kept precise.  Kıral--Young (arXiv:
1710.00914), equation (2.20), prints the same switched-cusp formula, but
their Theorem 2.7 assumes that the character is even and therefore is not,
by itself, a legal black-box citation for \(\chi_4\).  The double-coset
calculation in Section 3 proves the needed algebra without that hypothesis.
Blomer--Milićević (arXiv:1410.4538), Sections 3--4 and Theorem 4,
explicitly use \(\kappa=1\) for primitive odd characters and include
holomorphic, Maaß, and Eisenstein spectra.  It validates the odd-parity
same-sign spectral architecture, but its fixed-argument theorem still
requires fixed positive indices, one controlled scalar modulus test, and a
common archimedean test.  Its exact arithmetic implementation here is
(2.7), not the pure-level-\(4\) switched-cusp identity.  It is not an
opposite-sign or joint-matrix theorem.

No sharp, clipped, starred, transition, hard-TOP, BAL, other UNBAL owner,
complete M9-M2, endpoint, M9, or global theorem is asserted.

## 3. Proof or derivation

### 3.1 The switched-cusp double coset

Take

\[
 \gamma_0=\begin{pmatrix}A&B\\4C&D\end{pmatrix}
 \in\Gamma_0(4),\qquad AD-4BC=1.
\]

Then

\[
 \gamma_0\sigma_0=
 \begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix}.                \tag{3.1}
\]

If its positive lower-left entry is \(c=2D\), then \(D=n>0\)
is odd.  Conversely every positive odd \(n\) occurs, so the allowed
modulus set is exactly

\[
 \mathcal C_{\infty0}=\{2n:n\geq1,\ n\text{ odd}\}.          \tag{3.2}
\]

The left and right cusp stabilizers reduce \(B\) modulo \(n\).
The determinant congruence says

\[
 4BC\equiv-1\pmod n,
 \qquad -C\equiv\overline4\,\overline B\pmod n,              \tag{3.3}
\]

so \(B\) ranges through the units.  Put
\(\Gamma_\infty^+=\langle T\rangle\), and for fixed \(c>0\) define

\[
 \mathcal D_{\infty0}(c):=
 \left\{[\rho]\in
 \Gamma_\infty^+\backslash
 \sigma_\infty^{-1}\Gamma_0(4)\sigma_0/\Gamma_\infty^+:
 \rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}\right\}.
\]

The fixed-modulus generalized Kloosterman convention used here is

\[
 S^{\chi_4}_{\infty0}(M,H;c)=
 \sum_{[\rho]\in\mathcal D_{\infty0}(c)}
 \overline{\chi_4}\!\left(D(\rho)\right)
 e\!\left({Ma+Hd\over c}\right),                             \tag{3.4}
\]

where \(D(\rho)\) is the lower-right entry of an underlying
\(\gamma_0\in\Gamma_0(4)\) with
\(\rho=\sigma_\infty^{-1}\gamma_0\sigma_0\).  Its
\(\chi_4\)-value is invariant under the translation stabilizers.  If one
instead quotients by \(\{\pm T^j\}\), the weight-one multiplier and the
global cusp-\(0\) Fourier phase must be fixed simultaneously; this can
change one global unit but not an \(n\)- or \(h\)-dependent factor.

(3.1)--(3.3) give

\[
 \begin{aligned}
 S^{\chi_4}_{\infty0}(M,H;2n)
 &=\chi_4(n)\sum_{B\bmod n}^{*}
 e\!\left({MB-HC\over n}\right)\\
 &=\chi_4(n)S(M,H\overline4;n)
  =\chi_4(n)S(\overline4M,H;n).                               \tag{3.5}
 \end{aligned}
\]

Taking \(M=4N_0\) proves (1.1).  This calculation also proves that
there is no omitted root-of-unity factor.  The oddness of \(\chi_4\)
requires weight parity \(\kappa=1\), since \(\chi_4(-1)=-1\); a
weight-zero \(\chi_4\) space would be killed by \(-I\).  The cusps
\(\infty\) and \(0\) are singular.  The third cusp \(1/2\) is
nonsingular for this character (its width-normalized generator has
lower-right entry \(3\bmod4\)).  Thus the singular-cusp set at pure level
four is exactly \(\{\infty,0\}\).  If a convention-matched pure-level-\(4\)
switched-cusp trace formula is supplied, its continuous spectrum would use
those two inducing cusps.  This is a conditional pure-level-\(4\) ledger,
not the full source-certified level-\(4/8\) ledger of (2.7).

### 3.2 Full gcd restoration and the inverse-first identity

Since \(\chi_4(gn)=\chi_4(g)\chi_4(n)\), (2.3) becomes

\[
 \sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi_4(g)\chi_4(n)W\!\left({X\over gnD}\right)
 \sum_{\substack{j\\(j,n)=1}}b_{g,n}(j)e(N_0j/n).            \tag{3.6}
\]

Fourier inversion in (2.5), followed by \(m=\overline j_n\), gives

\[
 \sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
 =\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n).          \tag{3.7}
\]

Substitution of (1.1) in (3.6)--(3.7) proves (1.2).  Notice that
\((N_0,n)>1\) was never excluded.  The real-centre factor
\(e(\xi j/n)\), the moving \(q_L\)-profile, and every support face remain
inside \(b_{g,n}\).

The same calculation in the reverse order proves the exact self-return:

\[
 \begin{aligned}
 &\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)\\
 &\quad={1\over n}\sum_m\gamma_{g,n}(m)
 \sum_{x\bmod n}^{*}e(N_0\overline x/n)
 \sum_{h\bmod n}e(h(x-m)/n)\\
 &\quad=\sum_{m\bmod n}^{*}\gamma_{g,n}(m)e(N_0\overline m/n)
 =\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n).                         \tag{3.8}
 \end{aligned}
\]

Thus full \(h\)-summation is not a new completion gain.  It is exactly
the original row.

### 3.3 Joint coefficient geometry

Put \(J=K/g\) and \(C=R/g\).  On the literal support,
\(J/C=K/R=\Delta^{-1}\), and the profile bounds give

\[
 |b_{g,n}(j)|\ll X^\varepsilon K^{-1},\qquad
 \sum_j|b_{g,n}(j)|^2\ll {X^\varepsilon\over gK}.             \tag{3.9}
\]

Parseval for the normalized transform (2.5) yields

\[
 \sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
 ={1\over n}\sum_m|\gamma_{g,n}(m)|^2
 \ll {X^\varepsilon\over ngK}
 \asymp {X^\varepsilon\over RK}.                             \tag{3.10}
\]

Also

\[
 |\widehat\gamma_{g,n}(h)|\ll {X^\varepsilon\over R},
 \qquad
 \sum_h|\widehat\gamma_{g,n}(h)|
 \ll {X^\varepsilon\over\sqrt{gK}}.                          \tag{3.11}
\]

Summing (3.10) over \(n\asymp C\) gives the second relation in (1.4).
For the unnormalized \(C\)-by-\(C\) coefficient matrix, the Hilbert--
Schmidt norm is \(\ll(gK)^{-1/2}X^\varepsilon\).  Its automatic
\(\ell^2\)-projective (nuclear) bound is only

\[
 \|\widehat\gamma_g\|_*
 \leq\sqrt C\,\|\widehat\gamma_g\|_{HS}
 \ll {\sqrt\Delta\over g}X^\varepsilon.                      \tag{3.12}
\]

This algebraic singular-value decomposition by itself supplies no modulus
smoothness.  Formula (1.3) displays the unresolved arithmetic dependence:
\(\overline j_n\) and \(1_{(j,n)=1}\) change with \(n\).  The smoothness of
(2.4) before inversion does not by itself prove a controlled separation
after inversion.

For a fixed nonzero \(h\), the proposed pure-level-\(4\) switched-cusp
Kuznetsov normalization would require a scalar test \(\Phi_{g,h}\)
satisfying, at

\[
 x_n={4\pi\sqrt{(4N_0)|h|}\over2n}
     ={4\pi\sqrt{N_0|h|}\over n},
\]

the samples

\[
 \Phi_{g,h}(x_n)=2nW\!\left({X\over gnD}\right)
                  \widehat\gamma_{g,n}(h).                   \tag{3.13}
\]

On the source-certified standard-cusp route (2.7), the corresponding
modulus is \(C=4n\), and

\[
 \frac{4\pi\sqrt{M_0(16u|h|)}}{C}
 =\frac{4\pi\sqrt{N_0|h|}}{n}.
\]

Thus the common standard-cusp test \(G_{g,h}\) would instead need the exact
samples

\[
 G_{g,h}(x_n)=4nW\!\left({X\over gnD}\right)
                 \widehat\gamma_{g,n}(h),                   \tag{3.13a}
\]

with the global factor \(\chi_4(M_0)/\tau(\chi_4)\) and the level-\(4\)
minus level-\(8\) sign left outside.  The factor \(2\) between (3.13) and
(3.13a) does not affect any power estimate, but it records that the two
trace-formula architectures are not the same.

Adjacent \(\log x_n\)'s are separated by \(\asymp C^{-1}\).
An exact disjoint-bump interpolation therefore has order-\(r\) logarithmic
Sobolev cost \(C^{r-1}\sum_n|2n\widehat\gamma_{g,n}(h)|\).
Across the full \((n,h)\)-matrix, Cauchy and (1.4) give for this canonical
exact interpolation

\[
 \sum_{n,h}|2n\widehat\gamma_{g,n}(h)|
 \ll {C^2\over\sqrt{gK}}X^\varepsilon.                       \tag{3.14}
\]

Thus the canonical exact interpolation is controlled only by the large
upper price (3.14); the frozen hypotheses give no bounded projective mass
or uniform Bessel-transform decay for it.  Equation (3.12) is cheaper
algebraically, but its modulus singular vectors have no proved Sobolev
control.  A simultaneously low-projective-cost, modulus-smooth
decomposition of the literal matrix is precisely the missing lemma; this
report neither supplies nor rules out such a decomposition.

### 3.4 Source-certified level-\(4/8\) route, Linnik range, and conditional pure-level-\(4\) inventory

Formula (2.7) is the source-certified arithmetic entry to the weight-one
standard-cusp trace formulas, and it requires the same modulus test
\(\omega\) in its level-\(4\) and level-\(8\) terms.  At fixed \(g\), put
\(C=R/g\) for the original odd-modulus scale.  In (2.7), the selected
standard modulus is \(C_{\mathrm{std}}=4n\asymp4C\), while the product of
the two fixed indices is
\(M_0(16u|h|)=16N_0|h|\).  Hence the fixed-factor Linnik inequality
\(16N_0|h|\ll(4C)^2\) is exactly the following scale:

\[
 N_0|h|\ll C^2,
\]

which gives (1.5)--(1.6).  In particular, for
\(g\gg\sqrt{K/L}\), with a sufficiently large fixed constant, the range
contains no nonzero integer \(h\).  Such supported strata exist because
\(K/\sqrt{K/L}=\sqrt{KL}=X^{(1-2(\delta-\ell))/2}\to\infty\).
For either sign, the natural Bessel argument on a dyadic
\(|h|\asymp H\) block is

\[
 Z(g,H)\asymp{\sqrt{XH}\over C};                              \tag{3.15}
\]

outside the small-argument range this is greater than one, reaching
\(Z^2\asymp Dg\) at \(H\asymp C\).  The cited same-sign theorem's transform
estimate cannot be extended to that range or to negative \(h\) by notation.

For each standard-cusp term in (2.7), one legal common smooth test, and
\(h>0\), the weight-one same-sign transform has, in the
Blomer--Milićević convention,

\[
 \dot\Phi(k)=i^k\int_0^\infty J_{k-1}(x)\Phi(x){dx\over x},
 \quad k\geq3\text{ odd},                                    \tag{3.16}
\]

and

\[
 \widetilde\Phi(t)={it\over2\sinh(\pi t)}
 \int_0^\infty\{J_{2it}(x)+J_{-2it}(x)\}\Phi(x){dx\over x}. \tag{3.17}
\]

The source-certified spectral ledger for (2.7) is the difference of two
\(H+M+E\) ledgers.  At level \(4\), the singular cusps are
\(\infty,0\), and primitive conductor four leaves no proper-level oldspace.
At level \(8\), all four cusps

\[
 \infty,\qquad 0,\qquad \frac12,\qquad \frac14 .
\]

are singular.  Its discrete basis contains level-\(8\) newforms and
oldclasses lifted from level \(4\), and its continuous term must include
all four inducing cusps.  Thus the two-cusp/empty-oldspace ledger describes
only pure level \(4\), not the complete source-certified implementation.

For a convention-matched pure-level-\(4\), switched-cusp formula, the
following is only a **conditional structural inventory**:

1. all holomorphic forms of odd weights \(k\geq3\), with
   \(\rho_{f,\infty}(4N_0)\overline{\rho_{f,0}(h)}\dot\Phi(k)\);
2. all weight-one Maaß forms, including every exceptional
   \(t_f\in i(0,1/2)\), with the corresponding product of Fourier
   coefficients and (3.17);
3. the continuous Eisenstein integrals attached to the singular cusps
   \(\infty\) and \(0\), with the two-cusp Fourier-coefficient products;
4. no cross-cusp diagonal term, since the two cusps are distinct.

This conditional pure-level-\(4\) inventory is consistent with its two
singular cusps and empty proper-level oldspace, but neither Kıral--Young nor
Blomer--Milićević states the convention-matched odd-character
\((\infty,0)\) trace formula needed to certify it.  For \(h<0\), a
pure-level-\(4\) counterpart would conditionally be expected to use an
opposite-sign \(K\)-Bessel transform and no holomorphic tower.  Its exact
transform normalization and complete spectral ledger are not supplied by
the cited same-sign theorem and are not promoted here.  For \(h=0\), the
nonzero-index Kuznetsov formula is inapplicable and the term must be
handled as a degenerate Ramanujan term.

The problem occurs before these transforms can be used owner-completely:
the frozen hypotheses do not identify (3.13) with one controlled
\(C_c^\infty\) test, nor do they control (3.13a) or provide the one common
\(\omega\) required
simultaneously by both standard-cusp terms of (2.7).  The canonical
disjoint-bump interpolation has reciprocal-grid spectral width, and no
target-saving large-sieve estimate is derived from it here.  Dropping its
transform tails would be an uncontrolled endpoint error.  A different
arithmetic decomposition of the literal matrix is not excluded.

### 3.5 Degenerate frequency and positive capacity

At \(h=0\),

\[
 S(N_0,0;n)=\mathfrak c_n(N_0),\qquad
 |\widehat\gamma_{g,n}(0)|\ll R^{-1}X^\varepsilon.
\]

Since

\[
 \sum_{n\asymp C}(n,N_0)\ll C X^\varepsilon,
\]

the \(h=0\) contribution at fixed \(g\) is
\(O_\varepsilon(g^{-1}X^\varepsilon)\), and summing \(g\) is
\(O_\varepsilon(X^\varepsilon)\).  It is target-safe.

For the remaining frequencies, the complete-frequency identity

\[
 \sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n)                  \tag{3.18}
\]

holds for every \((N_0,n)\).  Combining (3.10) and (3.18) gives one row

\[
 \left|\sum_h\widehat\gamma_{g,n}(h)S(N_0,h;n)\right|
 \ll {\sqrt\Delta\over g}X^\varepsilon.                      \tag{3.19}
\]

There are \(O(R/g)\) moduli at fixed \(g\).  Hence

\[
 \sum_g {R\sqrt\Delta\over g^2}X^\varepsilon
 \ll R\sqrt\Delta X^\varepsilon,                            \tag{3.20}
\]

which is (1.7).  This closure counts all gcd strata and all signs, but it
also proves the same statement for arbitrary unit phases in place of
\(\chi_4(n)\).  It therefore cannot be the desired signed gain.

### 3.6 Full-polytope power comparison and self-return

Write \(a=\delta-\ell\).  The accepted flat envelope has exponent

\[
 \beta(a)=\min\{a,(1-a)/2\},
 \qquad {1\over4}<a<{1\over2}.                               \tag{3.21}
\]

The positive inverse-first exponent is

\[
 p=1-{\delta+\ell\over2}.                                    \tag{3.22}
\]

It exceeds both branches, not merely their minimum:

\[
 p-a=1-{3\delta\over2}+{\ell\over2}>{1\over4},
 \qquad
 p-{1-a\over2}={1\over2}-\ell>{1\over4}.                    \tag{3.23}
\]

Also \(\delta+\ell<3/4\), so \(p>5/8\), far above the quarter
target.  These inequalities hold on all of (2.2); the extra residual-
polytope inequality creates no improving chamber.

There are two exact returns.  Smooth-weight-first completion gives the
already accepted Ramanujan/additive capacity \(\Delta X^\varepsilon\).
Inverse-selector-first completion gives (1.2), but complete \(h\)-
orthogonality is exactly (3.8).  A trace formula is therefore only a
change of representation until a new estimate for the literal joint
spectral matrix is supplied.  The strict reduction proved here is removal
of the target-safe \(h=0\) complement; the unresolved survivor is the
centered nonzero-frequency matrix.  No further strict survivor follows
from the representation alone.

## 4. First doubtful or unproved step

There is no doubtful step in the double-coset identity, gcd restoration,
real-centre placement, Parseval ledger, \(h=0\) estimate, orthogonality
self-return, or positive capacity comparison.

The two spectral routes have different first gaps.  For the internal
pure-level-\(4\) route, the first source gap is already the
convention-matched odd-character switched-cusp trace formula: its Fourier
normalizations, same- and opposite-sign transforms, Plancherel measure,
continuous terms, and any scattering contribution have not been derived
here.  Identity (1.1) alone does not supply that formula.

For the source-certified level-\(4/8\) standard-cusp route (2.7), the first
project gap is the following joint theorem.  For each \(g\), it would have
to estimate the unresolved internal representation

\[
 \sum_{n\asymp R/g}
 \sum_{\substack{h\bmod n\\h\ne0}}
 W_{g,n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n)                             \tag{4.1}
\]

before a modulus triangle, using either a vector-valued generalized-cusp
Kuznetsov formula or a spectral large sieve which accepts a genuinely
joint \((n,h)\) coefficient.  It must prove all of the following rather
than assume them:

\[
 \text{controlled projective mass}
 +\text{controlled modulus Sobolev norm}
 +\text{controlled Bessel transforms}
 +\text{common spectral coefficient interface},              \tag{4.2}
\]

uniformly through every entry, exit, gcd stratum, and real centre.  It
must also control the long-frequency range
\(|h|>X/(D^2g^2)\), every exceptional form, the two level-\(4\)
Eisenstein cusp families, all four level-\(8\) Eisenstein cusp families,
and the level-\(4\) oldclasses inside level \(8\).  No theorem in the
audited packet has this input type.

The first false shortcut would be to replace
\(\widehat\gamma_{g,n}(h)\) by an independent \(h\)-coefficient or by a
smooth function of \(n\).  Equation (1.3) shows that this deletes the
inverse selector.  The second false shortcut would be to sum \(h\) first
and advertise the result as a spectral gain; (3.8) shows that this is the
original reciprocal row.  The third would be to apply the fixed-argument
Linnik theorem to all \(h\); (1.5)--(1.6) show the exact range failure.

This gap does not prove that (4.1) is large.  An actual-family theorem
could exploit precisely the \(\chi_4\) direction which all positive
closures above erase.

## 5. Required control test and outcome

1. **`exact_gcd_restored_inverse_first_identity` -- pass.**  Equations
   (2.4)--(2.5), (3.6)--(3.8) retain every \(g\), every unit row, and the
   exact normalized Fourier transform.
2. **`chi4_modulus_sign_and_level_four_embedding` -- pass.**  Equation
   (1.1) places \(\chi_4(n)\) inside the switched-cusp generalized
   Kloosterman sum at level four and weight parity one as an internal
   arithmetic identity.  It is not promoted as a sourced switched-cusp
   trace formula; (2.7) is the distinct source-certified encoding.
3. **`cusp_modulus_progression_and_root_of_unity` -- pass.**  The cusps
   are \((\infty,0)\), the allowed generalized moduli are exactly
   \(2n\equiv2\pmod4\), and the direct double-coset calculation produces
   no modulus-dependent root.  The ordinary arguments are exactly
   \((N_0,h)\).
4. **`joint_gammahat_n_h_coefficient_geometry` -- obstruction located.**
   Parseval, Hilbert--Schmidt, nuclear, and interpolation costs are
   (1.4), (3.12), and (3.14).  No smooth/common-sequence separation is
   proved from the frozen inputs; expanding the joint coefficient and
   summing \(h\) returns the original row.  A better decomposition of the
   literal matrix is not excluded.
5. **`real_centre_profile_and_endpoint_ownership` -- pass.**
   \(e(\xi j/n)\), \(q_L\), \(W\), the \(1/(gj)\) weight, zero-extension,
   entries, and exits remain literal.  Setting \(\xi=0\) is never used.
6. **`Kuznetsov_test_Bessel_transform_hypotheses` -- fail for the full
   matrix.**  The required samples (3.13)--(3.13a) are not one controlled
   smooth test under the frozen hypotheses.  The canonical disjoint-bump
   interpolation has grid-scale Sobolev and spectral width.  The cited
   same-sign theorem covers only positive fixed \(h\) in (1.5), a fraction
   (1.6) of the complete frequency range, and its level-\(4/8\) terms
   require one common \(\omega\); it is not applied to negative \(h\).
7. **`holomorphic_Maass_Eisenstein_exceptional_ledger` -- pass as a
   two-route scope audit.**  The source-certified same-sign route is the
   level-\(4\) minus level-\(8\) \(H+M+E\) combination (2.7).  Level \(4\)
   has singular cusps \(\infty,0\) and no proper-level oldspace; level \(8\)
   has singular cusps \(\infty,0,1/2,1/4\) and includes level-\(4\)
   oldclasses.  The two-cusp pure-level-\(4\) switched-cusp inventory and
   every negative-\(h\) opposite-sign ledger remain conditional and
   unpromoted.  The degenerate \(h=0\) term is separately target-safe.
8. **`spectral_large_sieve_common_sequence_and_norms` -- fail at the
   common-sequence seam.**  Algebraic SVD supplies (3.12), but no Sobolev
   control for its modulus vectors or one common level-\(4/8\) test.
   Modulus point masses are legal, but no estimate better than the
   separately available coefficient-blind closure (3.20) is derived from
   them here.
9. **`full_polytope_D_L_R_K_Delta_capacity` -- pass as a no-go.**  The
   owner-complete positive capacity is \(R\sqrt\Delta=X/\sqrt{DL}\).
   Equations (3.21)--(3.23) show it exceeds both accepted-envelope
   branches by fixed powers everywhere in the strict region.
10. **`Ramanujan_original_wave_and_spectral_self_return` -- pass.**
    Smooth-first is the known Ramanujan return; inverse-first followed by
    full \(h\)-orthogonality is exactly (3.8), the original reciprocal
    row.
11. **`actual_character_vs_unsigned_adversary` -- pass.**  The exact cusp
    identity is genuinely \(\chi_4\)-specific.  The estimate (3.20) is
    coefficient-blind and also holds for arbitrary phases, so it is not
    misreported as actual-character cancellation.
12. **`downstream_owner_and_exponent_scope` -- pass.**  Only one
    flat-smooth strict-UNBAL owner was analyzed.  No omitted UNBAL owner,
    BAL, TOP, complete M9-M2, endpoint, M9, bridge, or exponent is changed.

The work was 100% analytical, algebraic, and primary-source hypothesis
checking, with 0% numerical experimentation.

## 6. Dependencies and exact artifacts used

The report used, without altering shared state:

- `protocol.md`;
- `state/proof_obligations.yml`, especially
  `M9-M2-smooth-unbalanced-three-quarter-estimate`,
  `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`,
  `M9-M2-unbalanced-flat-wave-curvature-envelope`,
  `M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction`, and
  `M9-M2-character-factor`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/conductor_round135_kloosterman_dispersion_adjudication.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md`.

Post-unmask revision instructions were applied from
rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_post_unmask_discovery_seam_audit.md.
The mandatory source-seam repairs were applied from
rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md.

Primary sources checked for normalization and hypothesis scope:

- E. M. Kıral and M. P. Young, *Kloosterman sums and Fourier
  coefficients of Eisenstein series*, arXiv:1710.00914, especially
  Proposition 2.6, Theorem 2.7, and equation (2.20).  Equation (2.20)
  matches (3.5); the even-character hypothesis of Theorem 2.7 is recorded
  and not silently applied to \(\chi_4\).
- V. Blomer and D. Milićević, *Kloosterman sums in residue classes*,
  arXiv:1410.4538, equations (2.1)--(2.5), the odd-character choice
  \(\kappa=1\) in Section 3, the full \(H+M+E\) Kuznetsov formula
  (4.6), the singular-cusp criterion (5.1), and Theorem 4.  Equation (2.3)
  is specialized in (2.7), including the level-\(4/8\) difference, Gauss
  factor, and shifted index.  Its coefficient and Linnik-range hypotheses
  are used only in the directions stated above.

The exact switched-cusp identity is proved internally in Section 3.1, so
it does not depend on extending Kıral--Young's even-character theorem by
assertion.

## 7. Recommended state effect

**Retain the exact embedding, but classify the attempted route as
`level_four_spectral_matrix_no_go`.**  The recommended promotable scoped
content is:

1. the exact internal arithmetic level-four identity (1.1), with cusps,
   modulus progression, character, arguments, gcd scope, and arithmetic
   root fixed, but not a pure-level-\(4\) trace formula;
2. the owner-complete formula (1.2) and the exact coefficient norms
   (1.4);
3. the target-safe \(h=0\) bound and centered \(h\ne0\) survivor;
4. the same-sign fixed-argument range obstruction (1.5)--(1.6);
5. the exact inverse-Fourier self-return (3.8); and
6. the positive capacity obstruction (1.7), with the full-polytope
   comparisons (3.23).

Record the exact source-certified level-\(4\) minus level-\(8\)
standard-cusp encoding (2.7) as source-routing data, with its Gauss factor,
minus sign, index \(16uh\), four level-\(8\) singular cusps, and
level-\(4\) oldclasses retained.  It is not a new target estimate or a
promotion of the conditional pure-level-\(4\) spectral formula.

Do not promote a source-level switched-cusp Kuznetsov theorem for odd
character solely from Kıral--Young, whose printed theorem assumes an even
character.  Blomer--Milićević supplies the legal \(\kappa=1\) same-sign
spectral architecture only through the level-\(4/8\) standard-cusp route,
but not an opposite-sign normalization or the missing joint matrix theorem.
The pure-level-\(4\) two-cusp/empty-oldspace spectral inventory is
conditional and unpromoted; it must not be substituted for the complete
level-\(4/8\) ledger.

Keep `M9-M2-smooth-unbalanced-three-quarter-estimate` open.  The smallest
unresolved survivor proved here is the centered nonzero-frequency quantity
(4.1); its \(h=0\) complement is \(O_\varepsilon(X^\varepsilon)\).  A future
reopening must supply a genuinely vector-valued or otherwise
arithmetic-structure-sensitive, actual-\(\chi_4\), modulus-and-frequency
joint estimate before positive modulus norms.  The matrix no-go asserted
here is only a no-go from the currently frozen coefficient controls.  No
sharp, clipped, starred, hard, transition, BAL, TOP, complete M9-M2, M9,
endpoint, bridge, or Gauss-circle status should change from this report.
