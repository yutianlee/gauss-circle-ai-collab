# Round 143 synthesis: exact odd-character embedding, no owner-saving joint-matrix trace estimate

Campaign: m9-m2-unbalanced-level-four-kuznetsov-matrix-gate

Starting graph SHA-256:
7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789

## Decision

Close under
\(\mathsf{level\_four\_spectral\_matrix\_no\_go}\).
Round 143 proves an exact character-to-level arithmetic identity and
eliminates the degenerate transformed frequency, but it does not prove the
flat strict-UNBAL target or a smaller owner-complete signed spectral
survivor.

## Positive progress

For \(\Gamma_0(4)\), primitive \(\chi_4\), weight parity \(\kappa=1\),
cusps \((\infty,0)\), and

\[
\sigma_\infty=I,\qquad
\sigma_0=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\]

the generalized moduli are exactly \(2n\), \(n\) odd, and

\[
\boxed{
S^{\chi_4}_{\infty0}(4N_0,h;2n)
=\chi_4(n)S(N_0,h;n).}
\tag{143.S1}
\]

This internally proved fixed-modulus identity holds for every \(h\) and
every \((N_0,n)\), with no modulus-dependent root in the chosen convention.
After \(r=gn\), \(k=gj\), and \((j,n)=1\), it gives the complete owner

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{g,n\ \operatorname{odd}\\gn\asymp R}}
\chi_4(g)W\!\left(\frac{X}{gnD}\right)
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)
S^{\chi_4}_{\infty0}(4N_0,h;2n).
\tag{143.S2}
\]

Every gcd stratum, profile, support boundary, and real-centre factor remains
literal.  The degenerate class satisfies

\[
\mathscr R_{h=0}\ll_\varepsilon X^\varepsilon.
\tag{143.S3}
\]

Hence the strict unresolved object is the centered \(h\ne0\) joint matrix,
not the whole completed wave.

## Source-safe spectral architecture

Kıral--Young's matching switched-cusp formula lies under an even-character,
weight-zero hypothesis and cannot certify \(\chi_4\).  Equation (143.S1)
is promoted only as an internal arithmetic lemma.

Blomer--Milićević supply a legal odd-character implementation:

\[
\sum_{n\ \operatorname{odd}}\chi_4(n)S(N_0,h;n)\omega(n)
=\frac{\chi_4(M_0)}{\tau(\chi_4)}
\left(\sum_{4\mid C}-\sum_{8\mid C}\right)
S_{\chi_4}(M_0,16uh;C)\omega(C/4),
\tag{143.S4}
\]

where \(u=2^{v_2(N_0)}\), \(M_0=N_0/u\), and
\(\tau(\chi_4)=2i\).  The same weight occurs at both levels.  The
source-certified ledger is weight-one \(H+M+E\): odd holomorphic weights
\(k\ge3\), all Maaß parameters including exceptional and \(t=0\) if
present, and all singular-cusp Eisenstein integrals.  Level \(8\) includes
four singular cusps and level-\(4\) oldclasses.  No unsupported
opposite-sign transform or residual term is used.

## Exact obstruction

Centered zero padding and Parseval give

\[
\|A_g\|_{S_2}^2\ll_\varepsilon(gK)^{-1}X^\varepsilon,\qquad
\|A_g\|_{S_1}\ll_\varepsilon
\frac{\sqrt\Delta}{g}X^\varepsilon.
\tag{143.S5}
\]

The conditional cross-cusp geometric samples are \(2nA_g(n,h)\); the
source-certified standard-cusp samples are \(4nA_g(n,h)\).  Their automatic
norms are, up to fixed factors,

\[
\|B_g\|_{S_2}\ll_\varepsilon
\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,\qquad
\|B_g\|_{S_1}\ll_\varepsilon
\frac{R\sqrt\Delta}{g^2}X^\varepsilon.
\tag{143.S6}
\]

These are upper prices, not literal lower bounds.  Row Parseval proves no
common smooth modulus test, no common spectral coefficient sequence, and no
owner-saving projective--Sobolev or vector-valued norm for the literal
matrix.  The audited Blomer--Milićević, Deshouillers--Iwaniec, and
Assing--Blomer--Li interfaces all require such controlled common data.

At modulus scale \(R/g\), the printed same-sign Linnik comparison range is

\[
H_{\rm Lin}(g)\asymp\frac{X}{D^2g^2}
=\frac{K}{Lg^2}.
\tag{143.S7}
\]

The continuous ratio is \(1/(Dg)\); the discrete coverage is at most that
order and is asymptotic to it only in the many-integer range.  For
\(g\gg\sqrt{K/L}\), no nonzero frequency is covered.  Parseval gives no
localization, and no audited complementary-range uniform theorem applies.

The exact complete Kloosterman second moment yields only

\[
|\mathscr R_{D,L}(X)|
\ll_\varepsilon R\sqrt\Delta\,X^\varepsilon
=X^{1-(\delta+\ell)/2+\varepsilon}.
\tag{143.S8}
\]

For \(a=\delta-\ell\), the accepted envelope exponent is
\(\min(a,(1-a)/2)\), while the exponent \(p\) in (143.S8) satisfies

\[
p-a>\frac14,\qquad p-\frac{1-a}{2}>\frac14,\qquad p>\frac58.
\tag{143.S9}
\]

Thus the positive closure is worse than both accepted branches throughout
the strict polytope.  It remains true for arbitrary row phases and is not
character cancellation.

Finally,

\[
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
=\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
\tag{143.S10}
\]

is the original reciprocal row exactly.  Smooth-first completion returns
the accepted \(\Delta X^\varepsilon\) Ramanujan/additive capacity.
Neither operation is a gain.

## Remaining gap and full-proof status

A pure-level-\(4\) route would first need a convention-matched
odd-character weight-one switched-cusp trace formula.  The legal
level-\(4/8\) route instead first needs a genuinely new theorem for the
literal centered \(h\ne0\) coefficient matrix, including a controlled
common test or vector norm, long frequencies, all spectral pieces,
profiles, and endpoints.  No current lemma or audited source supplies it.

This is a scoped method obstruction, not a lower bound or proof that such a
future theorem is impossible.  The flat strict-UNBAL estimate remains open.
Hard TOP, BAL, the other UNBAL owners, M9-M2, both remaining M9-M1 parents,
endpoint uniformity, M9, and the unconditional quarter theorem all remain
open.

The strongest internally proved global exponent remains \(1/3\).  The
separately audited external Li--Yang exponent remains

\[
\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots.
\]

Round 143 proves no exponent improvement.

Resulting graph SHA-256:
179e40fb38e6a5e26623c2584d469b1c4c8d5ae444a70d791298852f2d511204
