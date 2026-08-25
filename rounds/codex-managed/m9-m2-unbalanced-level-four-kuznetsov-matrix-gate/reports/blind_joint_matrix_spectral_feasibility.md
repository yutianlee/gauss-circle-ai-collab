# Blind joint-matrix spectral feasibility report (Round 143; post-unmask repaired)

## 1. Result

The outcome is **(3), a rigorous first obstruction at the
coefficient-matrix/common-test seam, from the currently frozen coefficient
controls**.

The original statement-only derivation found the exact internal arithmetic
identity

\[
 S^{\chi _4}_{\infty,0}(4N_0,h;2n)
 =\chi _4(n)S(N_0,h;n),\qquad n\ {\rm odd},                  \tag{1.1}
\]

for \(\Gamma_0(4)\), cusps \((\infty,0)\), scaling
\(\sigma_0=\left(\begin{smallmatrix}0&-1/2\\2&0\end{smallmatrix}\right)\),
and parity \(\kappa=1\).  Its positive generalized moduli are exactly
\(2n\equiv2\pmod4\), and there is no modulus-dependent arithmetic root in
the convention below.  This is an internal double-coset lemma, not by itself
a sourced weight-one switched-cusp trace formula.

Post-unmask source repair supplies an independent legal spectral encoding.
Put

\[
 u=(N_0,4^\infty)=2^{v_2(N_0)},\qquad M_0=N_0/u.
\]

Blomer--Milićević (BM) give, for a finitely supported weight \(\omega\),

\[
 \sum_{n\ {\rm odd}}\chi _4(n)S(N_0,r;n)\omega(n)
 =\frac{\chi _4(M_0)}{\tau(\chi _4)}
 \left(\sum_{4\mid C}-\sum_{8\mid C}\right)
 S_{\chi _4}(M_0,16ur;C)\omega(C/4),\qquad r>0.             \tag{1.2}
\]

Thus the source-certified route is a standard-cusp level-\(4\) minus
level-\(8\) formula.  It uses the sourced same-sign transforms and the
complete spectral architecture \(H+M+E\).  The level-\(8\) term has all four
singular cusps and includes oldclasses lifted from level \(4\).

The zero Fourier class is target-safe:

\[
 \mathscr R_{h=0}\ll_\varepsilon X^\varepsilon.             \tag{1.3}
\]

Hence the strict unresolved owner is the centered, fully gcd-restored matrix
with \(h\ne0\), not the whole wave.  It may be reindexed row by row by the
positive representatives \(1\le r<n\), so the source discussion requires no
unsourced opposite-sign formula.

For the nonzero matrix, the frozen packet gives row Parseval and therefore
Hilbert--Schmidt upper bounds, but it gives no controlled common modulus test,
common coefficient sequence, modulus derivatives, Bessel bandwidth, or
owner-saving projective norm.  An abstract diagonal matrix shows only that
row Parseval alone cannot imply a better uniform Schatten-one estimate; it
does not prove that the literal inverse-selector matrix saturates that price.
Termwise triangle after an SVD pays the nuclear norm, but a future
vector-valued inequality is not ruled out.

The source-certified fixed-argument bound has a second independent gap: for
a gcd row (g), its Linnik range covers at most a proportion
\(\ll1/(Dg)\) of the positive frequency representatives and contains no
nonzero integer once \(g\gg\sqrt{K/L}\).  Parseval supplies no localization
in that short range.  The only coefficient-blind positive closure remains

\[
 R\sqrt\Delta\,X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon},                         \tag{1.4}
\]

which misses both accepted-envelope branches and the quarter target
throughout the strict residual polytope.  Exact summation in (h) instead
returns the original inverse-first row (minus the already safe zero class).

This is not a lower bound for the signed scalar and not an impossibility
theorem for a new literal-matrix or vector-valued Kuznetsov estimate.

## 2. Exact statement and hypotheses

Assume the frozen parameter region

\[
 D=X^\delta,\qquad L=X^\ell,\qquad R=\frac XD,\qquad
 K=\frac{XL}{D^2},\qquad \Delta=\frac RK=\frac DL,           \tag{2.1}
\]

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.                                    \tag{2.2}
\]

Retain every literal entry and exit of \(W\) and \(q_L\), the real-centre
phase, and every gcd stratum.  Restore

\[
 r=gn,\qquad k=gj,\qquad (j,n)=1,
\]

and define

\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),            \tag{2.3}
\]

with the literal condition \(gj\asymp K\).  Then

\[
 \widehat\gamma_{g,n}(h)
 =\frac1n\sum_{\substack{j\asymp K/g\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}
 e\!\left(\frac{\xi j-h\overline j_n}{n}\right).           \tag{2.4}
\]

For odd (n), let

\[
 \mathcal H_n=left\{-\frac{n-1}{2},\ldots,\frac{n-1}{2}\right\}.
\]

The strict owner-complete survivor is

\[
 \begin{aligned}
 \mathscr R^{\ne0}_{D,L}(X)
 ={}&\sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
 \chi _4(g)\chi _4(n)W\!\left(\frac{X}{gnD}\right)\\
 &\times\sum_{\substack{h\in\mathcal H_n\\h\ne0}}
 \widehat\gamma_{g,n}(h)S(N_0,h;n).
                                                               \tag{2.5}
 \end{aligned}
\]

The complete frozen owner is exactly
\(\mathscr R_{D,L}=\mathscr R^{\ne0}_{D,L}+\mathscr R_{h=0}\).
For source use, replace a centered nonzero residue \(h\) in each row by its
unique representative \(r=r(n,h)\in\{1,\ldots,n-1\}\).  Since both
\(\widehat\gamma_{g,n}\) and the Kloosterman sum depend only on the residue
class, this is an exact rowwise reindexing of (2.5).

Put \(C_g=R/g\), and pad invalid entries by zero.  For either the centered or
positive row indexing define

\[
 A_g(n,h)=W\!\left(\frac{X}{gnD}\right)
 \widehat\gamma_{g,n}(h),\qquad n\asymp C_g,\qquad h\ne0.
                                                               \tag{2.6}
\]

The frozen information implies only

\[
 \sum_h|A_g(n,h)|^2\ll\frac{X^\varepsilon}{RK},\qquad
 \|A_g\|_{S_2}^2\ll\frac{X^\varepsilon}{gK},
                                                               \tag{2.7}
\]

and therefore

\[
 \|A_g\|_{S_1}\ll\frac{\sqrt\Delta}{g}X^\varepsilon.
                                                               \tag{2.8}
\]

In the normalization of BM Theorem 1, matching the literal ordinary sum for
a fixed positive argument \(r\) would require nodal values

\[
 f_{\infty,g,r}(n/C_g)
 =\sqrt n\,W\!\left(\frac{X}{gnD}\right)
 \widehat\gamma_{g,n}(r),                                   \tag{2.9}
\]

up to fixed level-\(4\) normalizing constants.  Thus the legal test-value
matrix \(F_g(n,r)=\sqrt n\,A_g(n,r)\) has only the automatic bounds

\[
 \|F_g\|_{S_2}\ll\frac{\sqrt\Delta}{g}X^\varepsilon,
 \qquad
 \|F_g\|_{S_1}\ll\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon.
                                                               \tag{2.10}
\]

Equations (2.7)--(2.10) are upper bounds.  They are sharp over the abstract
class of matrices satisfying only the same row-Parseval constraint, not
proved sharp for the literal matrix (2.4).

Finally, the sourced fixed-positive-argument Linnik range is

\[
 0<r\ll H_{\rm Lin}(g):=\frac{C_g^2}{N_0}
 \asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2}.                     \tag{2.11}
\]

Its covered proportion is \(\ll1/(Dg)\), and is
\(\asymp1/(Dg)\) only while \(H_{\rm Lin}(g)\gg1\).  For
\(g\gg\sqrt{K/L}\), (2.11) contains no nonzero integer.  No frozen estimate
controls the complementary matrix mass.

## 3. Proof and full derivation

### 3.1. Literal coefficient and matrix costs

On the literal support, \(j\asymp K/g\) and \(gj\asymp K\), so, up to
\(X^\varepsilon\),

\[
 |b_{g,n}(j)|\ll K^{-1},\qquad
 \sum_j|b_{g,n}(j)|\ll g^{-1},\qquad
 \sum_j|b_{g,n}(j)|^2\ll(gK)^{-1}.                          \tag{3.1}
\]

Changing from the unit \(m\) to \(j=\overline m_n\) gives (2.4) exactly.
The factor (e(\xi j/n)) is retained and has modulus one.  The inverse phase
(e(-h\overline j_n/n)), the unit condition, and the literal support change
arithmetically with \(n\); smoothness of \(W\) and \(q_L\) alone supplies no
adjacent-modulus derivative bound for the resulting samples.

Parseval gives the row estimate in (2.7).  There are
\(\asymp C_g=R/g\) rows, hence

\[
 \|A_g\|_{S_2}^2
 =\sum_{n,h}|A_g(n,h)|^2
 \ll\frac{C_g}{RK}X^\varepsilon
 =\frac{X^\varepsilon}{gK}.                                 \tag{3.2}
\]

Since \(\operatorname{rank}A_g\ll C_g\), (2.8) follows.  Multiplication of
row (n) by \(\sqrt n\asymp\sqrt{C_g}\) gives

\[
 \|F_g\|_{S_2}^2\ll\frac{\Delta}{g^2}X^\varepsilon,
 \qquad
 \|F_g\|_{S_1}\ll\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,
                                                               \tag{3.3}
\]

as claimed.

An abstract diagonal matrix, with one entry of size \((RK)^{-1/2}\) in each
of \(\asymp C_g\) distinct rows and columns, attains the right scale in
(2.8); after row multiplication by \(\sqrt n\), it attains the scale in
(2.10).  This proves only

\[
 \text{row Parseval alone does not imply a smaller uniform nuclear norm}.
                                                               \tag{3.4}
\]

It gives no nuclear-norm lower bound, rank lower bound, or saturation result
for (2.4).  Likewise, a termwise triangle inequality after an
\(L^2\)-normalized SVD pays \(\sum_\rho s_\rho=\|F_g\|_{S_1}\); this does
not prove that every scalar organization or a future vector-valued theorem
must pay that norm.

### 3.2. Internal level-\(4\) arithmetic identity

Write

\[
 S(a,b;n)=\sum_{x\bmod n}^{*}e\!\left(\frac{a\overline x+bx}{n}\right).
                                                               \tag{3.5}
\]

For

\[
 \gamma=\begin{pmatrix}A&B\\4C&D\end{pmatrix}\in\Gamma_0(4),
 \qquad AD-4BC=1,
\]

one has

\[
 \gamma\sigma_0
 =\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix}.             \tag{3.6}
\]

Thus \(D=n\) is odd, and the positive lower-left entries are exactly
\(2n\), \(n>0\) odd.  For fixed \(n\), the double cosets are parametrized by
\(C\bmod n\), \((C,n)=1\), and

\[
 B\equiv-(4C)^{-1}
 \equiv-\overline4_n\,\overline C_n\pmod n.                  \tag{3.7}
\]

Fix the generalized-sum convention

\[
 S^{\chi_4}_{\infty,0}(m,\nu;c)
 :=\sum_{\substack{\Gamma_\infty\backslash
     \Gamma_0(4)\sigma_0/\Gamma_\infty\\
     c(\gamma\sigma_0)=c}}
 \overline{\chi_4(D_\gamma)}
 e\!\left(\frac{m\,a(\gamma\sigma_0)+
                    \nu\,d(\gamma\sigma_0)}{c}\right).
\]

Substitution of (3.6)--(3.7) gives

\[
 \begin{aligned}
 S^{\chi_4}_{\infty,0}(m,\nu;2n)
 &=\chi_4(n)\sum_{C\bmod n}^{*}e_n(mB-\nu C)\\
 &=\chi_4(n)S(-m\overline4_n,-\nu;n).
                                                               \tag{3.8}
 \end{aligned}
\]

Taking \(m=4N_0\), \(\nu=h\), and substituting \(C\mapsto-C\) proves
(1.1), with no coprimality condition on \((N_0,n)\).

At pure level \(4\), the cusps \(\infty\) and \(0\) are singular, while
\(1/2\) is nonsingular because its stabilizer has lower-right entry \(3\) and
\(\chi_4(3)=-1\).  Compatibility with \(-I\) forces
\((-1)^\kappa=\chi_4(-1)=-1\), hence \(\kappa=1\).  Primitive conductor
\(4\) leaves no proper-level oldspace at exact level \(4\), and the distinct
cusp pair would have no diagonal term in a convention-matched cross-cusp
formula.  These are internal or conditional pure-level-\(4\) facts; they do
not furnish that spectral formula or its Plancherel constants.

### 3.3. Post-unmask legal encoding and sourced same-sign spectrum

Define

\[
 S_{\chi_4}(a,b;C)
 =\sum_{d\bmod C}^{*}\chi_4(d)
 e\!\left(\frac{ad+b\overline d}{C}\right).
\]

BM (2.3), with \(q=q_1=4\), has nonzero Möbius terms \(d=1,2\), of
signs \(+1,-1\), while \(\mu(4)=0\).  With source arguments
\((N_0,r)\), this is exactly (1.2); the difference selects \(C=4n\) with
\(n\) odd.  Its same-sign Bessel geometry is

\[
 \frac{4\pi\sqrt{M_0(16ur)}}{4n}
 =\frac{4\pi\sqrt{N_0r}}{n}.                                \tag{3.9}
\]

For \(\kappa=1\), the exact BM same-sign transforms are

\[
 \dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},
 \qquad k=3,5,\ldots,                                      \tag{3.10}
\]

\[
 \widetilde g(t)=\frac{it}{2\sinh(\pi t)}
 \int_0^\infty\bigl(J_{2it}(x)+J_{-2it}(x)\bigr)
 g(x)\frac{dx}{x}.                                         \tag{3.11}
\]

Only this same-sign normalization is used.  No exact opposite-sign
weight-one transform is asserted.

BM (4.6) and Theorem 4 give exactly the qualitative ledger \(H+M+E\):

- \(H\) contains odd holomorphic weights \(k=3,5,\ldots\);
- \(M\) contains the full weight-one Maaß basis, including real parameters,
  \(t=0\) if present, and exceptional parameters; and
- \(E\) integrates over every singular cusp.

At level \(4\), the singular cusps are \(\infty,0\) and there is no
proper-level oldspace.  At level \(8\), the singular cusps are
\(\infty,0,1/2,1/4\), and the basis contains level-\(8\) newforms and
oldclasses lifted from level \(4\).  No separate residual term or
holomorphic weight-one limit term is printed; a \(t=0\) Maaß form, if one
occurs, is already in \(M\).

The legal route still requires one smooth scalar modulus test for fixed
positive Fourier arguments.  Applied to (2.5) after positive rowwise
reindexing, its required nodal matrix is (2.9).  The inverse in (2.4) and its
moving support do not prove that a controlled smooth extension is impossible,
but the frozen hypotheses supply no derivative, Mellin, common-sequence, or
aggregate transform bound for one.  DI-type spectral large sieves use one
common coefficient sequence, and the stronger ABL comparison permits only a
common sequence times a jointly smooth function with controlled mixed
derivatives.  Neither hypothesis follows from (2.7).

For fixed positive \(r\), adjacent supported odd moduli have logarithmic node
spacing \(\asymp C_g^{-1}\).  A disjoint-bump interpolation is available but
has derivative costs growing in powers of \(C_g\).  This is an upper price for
one construction, not a lower bound for every interpolation.  Similarly, on
a frequency block \(r\asymp H\), the geometric Bessel argument has scale

\[
 x_{g,H}\asymp\frac{\sqrt{XH}}{C_g}.
\]

At \(H\asymp C_g\), this gives \(x_{g,H}^2\asymp Dg\); at
\(g\asymp K\), the dimensional scale is \(\sqrt{DK}\), with
\(R/\sqrt{DK}=\sqrt{X/(DL)}\).  These match dimensions occurring in the
accepted envelope, but they do not prove that an arbitrary interpolant is
spectrally restricted to that height or that a BM transform produces either
envelope term.

The printed fixed-argument bound also assumes
\(N_0r\ll C_g^2\), which is (2.11).  Since the positive row has
\(\asymp C_g\) nonzero residues, the covered proportion is at most
\(1/(Dg)\), and it vanishes for \(g\gg\sqrt{K/L}\).  Row Parseval gives no
permission to discard the rest.

### 3.4. Zero class, positive capacity, self-return, and powers

For \(h=0\), (3.1) gives

\[
 |\widehat\gamma_{g,n}(0)|
 \le\frac1n\sum_j|b_{g,n}(j)|
 \ll\frac1R X^\varepsilon.                                 \tag{3.17}
\]

Also \(S(N_0,0;n)=c_n(N_0)\) and
\(|c_n(N_0)|\le(n,N_0)\).  Therefore

\[
 \sum_{n\asymp R/g}(n,N_0)\ll\frac Rg\tau(N_0),
\]

so the fixed-\(g\) zero contribution is
\(O(g^{-1}X^\varepsilon)\), and summing \(g\ll K\) proves (1.3).

For every \(n\), additive orthogonality gives the exact identity

\[
 \sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n).                 \tag{3.18}
\]

Restricting to \(h\ne0\) can only reduce the right-hand side.  Row Cauchy
and (2.7) therefore cost

\[
 \left|\sum_{\substack{h\bmod n\\h\ne0}}
 A_g(n,h)S(N_0,h;n)\right|
 \ll\frac{\sqrt\Delta}{g}X^\varepsilon.                    \tag{3.19}
\]

There are \(\asymp R/g\) rows, so every coefficient-blind positive closure
of this type gives

\[
 \sum_{g\ll K}\frac{R\sqrt\Delta}{g^2}X^\varepsilon
 \ll R\sqrt\Delta\,X^\varepsilon
 =\frac{X^{1+\varepsilon}}{\sqrt{DL}}
 =X^{1-(\delta+\ell)/2+\varepsilon}.                        \tag{3.20}
\]

This upper bound erases both \(\chi_4(n)\) and \(\chi_4(g)\); it is not a
lower bound for the signed owner.

If the complete \(h\)-sum is performed before a positive norm, Fourier
orthogonality gives exactly

\[
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
 =\sum_j b_{g,n}(j)e(N_0j/n),                               \tag{3.21}
\]

the original inverse-first row.  The \(h\ne0\) sum gives the same row minus
the target-safe \(h=0\) term.  Thus inversion is a self-return, not a strict
spectral reduction.

Let \(a=\delta-\ell\).  The accepted envelope is

\[
 \min\!\left(\Delta,\sqrt{KD}+\sqrt{R/L}\right),
 \qquad
 \Delta=X^a,\qquad \sqrt{KD}=X^{(1-a)/2}.                   \tag{3.22}
\]

Since \(L\ge1\), \(\sqrt{KD}\ge\sqrt{R/L}\), so the second branch is
governed by \(X^{(1-a)/2}\).  If
\(p=1-(\delta+\ell)/2\) is the exponent in (3.20), then

\[
 p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,
 \qquad
 p-\frac{1-a}{2}=\frac12-\ell>\frac14.                     \tag{3.23}
\]

Moreover \(\delta+\ell<3/4\), so \(p>5/8\), more than \(3/8\) above the
quarter exponent.  These inequalities hold at every fixed point of the
strict polytope; no additional uniform margin beyond their strict boundary
values is asserted.  The extra inequality in (2.2) creates no improving
chamber.

## 4. First doubtful or unproved step

In the original blind artifact, the first unsupported assertion was its
purported exact weight-one switched-cusp transform and spectral block.  The
post-unmask repair deletes that block, its shifted hyperbolic denominators,
its exact opposite-sign transform, and its residual claims.  Identity (1.1)
is retained only as an internal arithmetic lemma.

There are now two clearly separated routes.

1. For a pure-level-\(4\), switched-cusp route, the first source gap is the
   convention-matched weight-one trace formula itself, including Fourier
   coefficients at both cusps, Plancherel measure, and endpoint/scattering
   analysis.  The internal double-coset identity does not prove that formula.
2. For the legal BM level-\(4/8\) route, the first project gap is the
   replacement of the literal samples
   \[
    \widehat\gamma_{g,n}(r)
    \quad\leadsto\quad
    \text{a common sequence and controlled smooth modulus test}.
                                                               \tag{4.1}
   \]
   The required aggregate Bessel/Sobolev or projective norm must save the
   complete \(h\ne0\) owner, cover frequencies outside (2.11), retain every
   gcd row and both character directions, and bound all \(H+M+E\) terms at
   levels \(4\) and \(8\).

Nothing in row Parseval proves (4.1).  Conversely, neither the inverse
congruence nor the abstract diagonal control disproves (4.1) for the literal
family.  The rigorous conclusion is only that none of the audited scalar or
standard smooth-matrix theorems is applicable with an owner-saving norm
justified by the frozen hypotheses.

## 5. Required controls and outcomes

1. **Exact gcd-restored inverse-first identity -- pass.**  Equations
   (2.3)--(2.5) retain \(r=gn\), \(k=gj\), \((j,n)=1\), the \(1/(gj)\)
   factor, every odd \(g\), and the real-centre phase.
2. **Internal level/cusp sign -- pass after convention insertion.**  The
   moduli are \(2n\equiv2\pmod4\), the character factor is
   \(\chi_4(n)\), the ordinary arguments are \((N_0,h)\), and the
   arithmetic root is \(1\).  This remains an internal lemma.
3. **Legal odd-character source encoding -- pass post-unmask.**  Equation
   (1.2) retains the Gauss factor, level-\(4\) minus level-\(8\) Möbius
   sign, and exact Bessel scaling.
4. **Zero-frequency ownership -- pass.**  Equation (1.3) is target-safe, so
   the owner-complete strict survivor is centered \(h\ne0\).
5. **Joint coefficient geometry -- pass as upper bounds only.**  Equations
   (2.7)--(2.10) are automatic Hilbert--Schmidt/nuclear prices.  The diagonal
   control proves insufficiency of row Parseval, not literal saturation.
6. **Scalar-test and transform hypotheses -- fail for the owner.**  The BM
   same-sign transforms (3.10)--(3.11) are sourced, but the nodal matrix
   (2.9) has no frozen derivative or aggregate transform control.  No exact
   opposite-sign or pure-level-\(4\) spectral normalization is used.
7. **Complete spectral ledger -- pass as a source audit.**  The legal route
   retains \(H+M+E\), all Maaß parameters, odd holomorphic weights, every
   singular cusp, level-\(8\) oldclasses, and no invented residual term.
8. **Common-sequence/smooth-matrix large sieve -- fail as a licensed input.**
   The frozen packet supplies neither the DI common sequence nor the ABL
   controlled joint smooth factorization.  It does not prove either
   factorization impossible.
9. **Linnik short-range/full-range control -- fail for completion.**  The
   legal range is (2.11), its fraction is at most \(1/(Dg)\), and it is empty
   of nonzero integers for \(g\gg\sqrt{K/L}\).  Parseval has no matching
   localization.
10. **Positive capacity and self-return -- pass with no saving.**  Equations
    (3.20)--(3.23) give the full power ledger, while (3.21) returns the
    original row.
11. **Actual character versus unsigned control -- fail after positive
    separation.**  The automatic norms are unchanged by deleting
    \(\chi_4(n)\) or inserting adversarial row phases, so they cannot be
    advertised as character cancellation.
12. **TeX and metadata hygiene -- pass after repair.**  The corrupted
    `quad`, `ll`, `asymp`, exponent commas, parity strings, unsupported
    transform block, and role label have been corrected or removed.
13. **Downstream scope -- pass.**  The result concerns only the frozen
    flat-smooth strict-UNBAL owner and proves no BAL, TOP, endpoint, complete
    M9-M2, M9, or global Gauss-circle claim.

All controls are analytical or algebraic.  No numerical experiment is used.

## 6. Dependencies and exact artifacts used

**Original statement-only derivation.**  Before unmasking, the blind
rederiver read exactly:

- `protocol.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/blind_statement.md`.

It did not read the proof graph, strategy, sibling reports, Round-118--143
nonblind artifacts, or external literature.  The exact inverse formula,
double-coset identity, cusp/parity audit, zero-class estimate, matrix norms,
self-return, and power ledger above were independently derived from that
packet.  The original role was “blind rederiver,” not “reviewer.”  No graph
hash was supplied in the blind packet.

**Post-unmask repair.**  After the statement-only report was complete, the
following artifacts were read solely to audit and repair source scope:

- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/discovery_post_unmask_blind_seam_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_post_unmask_source_hypothesis_audit.md`.

Primary-source checks used only in the post-unmask repair were BM,
*Kloosterman sums in residue classes*, (2.3)--(2.5), Section 3,
(4.1)--(4.6), (5.1), and Theorem 4; Deshouillers--Iwaniec, Theorems 2 and 5,
for the common-sequence interface; Assing--Blomer--Li, Theorem 2.4, for the
controlled smooth two-variable interface; and Kıral--Young, Theorem 2.7,
only for the even-character attribution boundary.  These sources did not
enter the original blind derivation.

Generated and repaired on 2026-08-24 (Asia/Shanghai).  No shared state,
validation matrix, proof draft, synthesis, or sibling artifact was edited.

## 7. Recommended state effect

**Retain/revise the scoped label `level_four_spectral_matrix_no_go`, meaning
only “no-go from the currently frozen coefficient controls,” and leave the
quarter-bound obligation open.**

The following content is suitable for selective promotion after conductor
adjudication:

1. the internal arithmetic identity (1.1), with its exact convention,
   moduli, cusps, parity, sign, and arithmetic root;
2. the source-certified BM level-\(4\) minus level-\(8\) encoding (1.2), its
   same-sign transforms, and its complete \(H+M+E\) ledger;
3. the target-safe \(h=0\) estimate and the strict centered
   \(h\ne0\) owner-complete survivor;
4. the Hilbert--Schmidt and nuclear upper bounds, explicitly limited to what
   row Parseval implies;
5. the Linnik-range gap, positive capacity (3.20), exact self-return, and
   full-polytope comparisons; and
6. the first obstruction that the frozen data furnish no controlled common
   test/sequence or Bessel-compatible vector norm for the literal matrix.

Do not promote the excised pure-level-\(4\) spectral constants, an exact
opposite-sign weight-one transform, any residual or holomorphic-weight-one
limit term, a literal-matrix Schatten lower bound, or a universal
Kuznetsov/matrix impossibility theorem.  A renewed campaign must prove a new
owner-saving estimate for (2.4), cover \(r>K/(Lg^2)\), retain all \(g\) and
both character directions, and include every level-\(4/8\) \(H+M+E\) term.
No downstream owner or global exponent changes on this evidence.
