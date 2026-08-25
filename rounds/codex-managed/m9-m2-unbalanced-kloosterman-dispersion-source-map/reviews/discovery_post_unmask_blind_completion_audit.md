# Post-unmask audit of the blind completion

Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`

Round: 135

Review role: discovery claimant auditing the statement-only completion after
unmasking

Starting graph SHA-256: `f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`

## 1. Result

**PASS WITH MATERIAL REPAIR.**  The blind report's final
`source_level_no_go`, direct source exponents, exact gcd decomposition, and
owner-complete survivor are correct.  Its completion must, however, be
split into two inequivalent Fourier orders.

1. If the original smooth short \(k\)-weight is Fourier-expanded first,
   its normalized Fourier coefficient has size \(R^{-1}\), bandwidth
   \(\Delta=R/K\), \(L^1\)-mass \(K^{-1}\), and squared \(L^2\)-mass
   \((RK)^{-1}\).  On the coprime part, the complete inverse-only inner sum
   is exactly the Ramanujan sum

   \[
          \mathfrak c_r(N_0+h),\qquad N_0=\lfloor X\rfloor,        \tag{1.1}
   \]

   because inversion permutes the units.  Evaluating (1.1) by
   \(|\mathfrak c_r(n)|\le(r,n)\), then summing the actual modulus family,
   returns

   \[
                  \boxed{\Delta X^\varepsilon}.                  \tag{1.2}
   \]

   The all-residue version gives the same bound by additive orthogonality.
   Thus smooth-weight-first completion is an exact equal-capacity return,
   not a Kloosterman completion.  The blind scalar Bettin--Chandee/Wright
   estimate \(\Delta R^{19/20+\varepsilon}\) is algebraically valid after
   the source-frequency repair below, but is strictly looser than (1.2).

2. If one first reindexes \(k=\overline m\pmod r\) and then Fourier-expands
   the resulting rough inverse-image coefficient as a function of \(m\),
   the complete inner sum is the genuine two-frequency Kloosterman sum

   \[
                     S(N_0,h;r).                                 \tag{1.3}
   \]

   The Fourier coefficients need not have bandwidth \(\Delta\); only
   Parseval gives \(L^1\ll K^{-1/2}\) and
   \(L^2{}^2\ll(RK)^{-1}\).  Weil plus an exact gcd average gives the
   uniform row cost \(\sqrt{R/K}=\sqrt\Delta\), and the row triangle gives
   \(R\sqrt\Delta X^\varepsilon\).  This is worse even than the trivial
   row triangle because \(\Delta>1\), and it is not a Bettin--Chandee or
   Wright coefficient tensor.  The discovery report's description of this
   cost as merely “optimistic under coprimality” can be strengthened to the
   uniform statement just given.

The source's integer-frequency issue is repairable everywhere on the flat
smooth cell.  Write \(X=N_0+\xi\), \(0\le\xi<1\), and absorb
\(e(\xi k/r)\) into the smooth coefficient tensor before any inverse
congruence or completion.  Bettin--Chandee Remark 1 also directly repairs
the degenerate \(m=1\) call.  Consequently:

- the blind use of an untyped real \(\vartheta\) must be replaced by the
  integer \(N_0\) plus this fractional-centre preprocessing;
- direct Wright, smooth-first completion, inverse-selector completion, and
  the \(a=m^2\) connector are source-legal for real \(X\) after the exact
  preprocessing, despite Wright having no printed perturbation remark;
- the discovery report's sentence that the \(a=m^2\) congruence connector
  fails for nonintegral \(X\) must be narrowed.  It fails only if one
  incorrectly leaves \(\xi\) multiplying the congruence lift; absorbing
  \(e(\xi k/r)\) makes the connector exact for every real centre and leaves
  all source exponents unchanged.

The discovery report has the sharp \(a=m^2\) diagonal norm: its projective
cost is \(\asymp1\), an unavoidable factor \(K^{1/2}\) above the direct
\(m=1\) coefficient norm.  The conductor candidate's elementary detector
over all \(a\asymp K^2\) overpays by \(K^{1/2}\).  The discovery
fixed-determinant dictionary and its error
\(X^{3/5}R^{17/20+\varepsilon}\) per nonzero determinant are algebraically
correct; because the source report did not audit Corollary 1, its external
source seam still requires the separately assigned source review before
graph promotion.

No completion or source call produces a strict target-scale remainder.
The smallest owner-complete survivor remains the whole flat-smooth wave,
equivalently its full gcd-completed signed representation.  The quarter
estimate and all downstream claims remain open.

## 2. Exact statement and hypotheses

Let

\[
 R={X\over D}=X^{1-\delta},\qquad
 K={XL\over D^2}=X^{1+\ell-2\delta},\qquad
 \Delta={R\over K}=X^{\delta-\ell},                              \tag{2.1}
\]

with

\[
 {1\over4}\le\delta<{1\over2},\qquad
 0\le\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463.                                        \tag{2.2}
\]

Thus \(1/4<\delta-\ell<1/2\), \(1<K<R\), and the flat packet is

\[
 \mathscr R_{D,L}(X)=
 \sum_{r\ {\rm odd}}\chi_4(r)W\!\left({X\over rD}\right)
 \sum_k b_r(k)e(Xk/r),
 \qquad b_r(k)={q_L(4Xk/r^2)\over k},                            \tag{2.3}
\]

where \(r\asymp R\), \(k\asymp K\), and the scaled profiles have uniform
fixed-order smooth seminorms.

Put

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor\in\mathbb Z_{>0},qquad
 0\le\xi<1,\qquad v_r(k)=b_r(k)e(\xi k/r).                       \tag{2.4}
\]

The factor \(e(\xi k/r)\) is part of a uniformly smooth normalized tensor:
on \(k=Ku,r=Rv\), its frequency is \(\xi K/R=O(\Delta^{-1})\).
Buffered Fourier expansion on the fixed \((u,v)\)-rectangle therefore
separates it together with \(q_L(4Xk/r^2)W(X/(rD))\), with total
projective mass \(O(1)\).  This preprocessing is exact and does not invoke
a source theorem.

The review conclusions are:

> **Completion-order proposition.**  For the flat packet (2.3),
> smooth-weight-first completion has the exact normalization in (3.2)
> below and returns the already known \(\Delta X^\varepsilon\) capacity by
> Ramanujan/additive orthogonality.  Inverse-selector-first completion has
> the exact normalization in (3.11), produces Kloosterman sums, and gives
> at best the stated rowwise positive cost unless a new joint signed theorem
> is supplied.  Neither operation yields a smaller owner-complete survivor.

> **Source-frequency repair.**  In every inverse congruence use the integer
> frequency \(N_0\), retaining \(e(\xi k/r)\) in the exactly separated
> coefficient tensor.  For direct Bettin--Chandee one may equivalently use
> Remark 1 with perturbation \(\xi a/n\).  All previously computed source
> exponents remain unchanged.

The review is confined to the flat smooth principal owner.  It makes no
claim for sharp, clipped, starred, hard, transition, stationary-remainder,
BAL, TOP, complete-UNBAL, M9-M2, M1, endpoint, M9, or global packets.

## 3. Proof or derivation

### 3.1 Integer-frequency repair and the direct exponents

The source audit correctly finds that Bettin--Chandee's proof uses an
integer \(\vartheta\), despite the printed theorem leaving its type
unstated.  In the direct \(m=1,a=k,n=r\) dictionary take
\(\vartheta=N_0\).  Then

\[
 e(Xk/r)=e\!\left(N_0{a\over n}+{\xi a\over n}\right).            \tag{3.1}
\]

Bettin--Chandee Remark 1 applies to \(f_{a,N_0}(m,n)=\xi a/n\): one
derivative is zero, the other is \(O(K/R^2)\), and its perturbation
parameter is \(O(K)\).  The source factor remains
\((1+XK/R)^{1/2}\) up to constants.  Hence the blind direct exponents

\[
 E_{BC,1}={29\over20}+{7\ell\over20}-{13\delta\over10},\qquad
 E_{BC,2}={3\over2}+{\ell\over2}-{3\delta\over2}                 \tag{3.2}
\]

are correct.  The first dominates because
\(E_{BC,1}-E_{BC,2}=(4\delta-3\ell-1)/20>0\), and it is always
\(>4/5\).

For Wright, incorporate \(e(\xi k/r)\) into the tensor (2.4), separate it
before the theorem call, and use integer \(\vartheta=N_0\).  Wright permits
arbitrary independent coefficient sequences, so no printed perturbation
corollary is required after this exact preprocessing.  The blind five
exponents remain correct, with the fifth dominant:

\[
 E_{W,5}={13\over8}+{\ell\over4}-{13\delta\over8}>{13\over16}.    \tag{3.3}
\]

Thus the source audit's phrase “Wright is illegal for nonintegral \(X\)” is
correct only for a bare citation that leaves the fractional phase inside
the exponential.  It is not correct after the conductor's verified flat
tensor separation.

### 3.2 Smooth-weight-first completion: exact Fourier masses

Extend \(v_r(t)\) by zero to a function on \(\mathbb Z/r\mathbb Z\) and
define the normalized Fourier coefficient

\[
 c_r(h)={1\over r}\sum_{t\bmod r}v_r(t)e(-ht/r),qquad
 v_r(t)=\sum_{h\bmod r}c_r(h)e(ht/r).                             \tag{3.4}
\]

The support has length \(K\), \(|v_r(t)|\ll K^{-1}\), and its normalized
finite differences of order \(j\) are \(O(K^{-1-j})\); the fractional
factor in (2.4) has still smaller variation because \(K/R<1\).  Repeated
summation by parts gives, for fixed \(B\),

\[
 |c_r(h)|\ll_B {1\over r}
 \left(1+{\|h-\xi\|_r\over\Delta}\right)^{-B}.                  \tag{3.5}
\]

Consequently

\[
 \sum_{h\bmod r}|c_r(h)|\ll {\Delta\over r}={1\over K},
 \qquad
 \sum_{h\bmod r}|c_r(h)|^2
 ={1\over r}\sum_{t\bmod r}|v_r(t)|^2\ll {1\over rK}.          \tag{3.6}
\]

These are the blind report's intended normalizations.  Its phrase “about
\(\Delta\) modes” refers to (3.5), not to a loss \(\Delta\) in addition to
the coefficient mass.

### 3.3 The complete inner sum is Ramanujan, and returns \(\Delta\)

On the coprime part, put \(t=\overline m\pmod r\).  Equations
(2.4) and (3.4) give exactly

\[
 \begin{aligned}
 S_r^{\times}
 &=\sum_{m\bmod r}^{*}v_r(\overline m)e(N_0\overline m/r)\\
 &=\sum_{h\bmod r}c_r(h)
   \sum_{m\bmod r}^{*}e((N_0+h)\overline m/r)\\
 &=\sum_{h\bmod r}c_r(h)\mathfrak c_r(N_0+h),                   \tag{3.7}
 \end{aligned}
\]

where the last equality follows because \(m\mapsto\overline m\) permutes
the reduced residues.  This is an exact Ramanujan sum, not a two-frequency
Kloosterman sum.

Use \(|\mathfrak c_r(n)|\le(r,n)\), (3.5), and interchange \(h,r\).  For
each integer \(n\asymp X\),

\[
 \begin{aligned}
 \sum_{r\asymp R}{(r,n)\over r}
 &\le \sum_{d\mid n}\varphi(d)
       \sum_{\substack{r\asymp R\\d\mid r}}{1\over r}
 \ll \sum_{d\mid n}{\varphi(d)\over d}
 \ll_\varepsilon X^\varepsilon.                                \tag{3.8}
 \end{aligned}
\]

Since the weighted number of \(h\)'s in (3.5) is \(O(\Delta)\), (3.7)
and (3.8), with \(\chi_4(r)W(X/(rD))\) retained until the final triangle,
give

\[
 \sum_{r\asymp R}\chi_4(r)W\!\left({X\over rD}\right)S_r^{\times}
 \ll_\varepsilon \Delta X^\varepsilon.                          \tag{3.9}
\]

The noncoprime terms need not be discarded.  If (3.4) is applied directly
to the complete original \(k\)-row, then

\[
 \sum_{t\bmod r}e((N_0+h)t/r)=r\,\mathbf1_{r\mid N_0+h}.          \tag{3.10}
\]

The factor \(r\) cancels the \(r^{-1}\) in (3.5); for each effective
\(h\), the number of \(r\asymp R\) dividing \(N_0+h\) is
\(O(X^\varepsilon)\).  This independently proves (3.9) for the full row.
It is precisely the fixed-centre divisor-capacity return.  It gives no
power below \(\Delta\).

If, instead of evaluating (3.7), one partitions \(m\) dyadically and
applies Bettin--Chandee or Wright separately for each fixed \(h\), then
\(\|c_r(h)\|_{\ell^2(r)}\ll R^{-1/2}\) on the effective band and the
source bounds have maximum \(R^{19/20+\varepsilon}\) per \(h\).  Summing
(3.5) by a scalar \(h\)-triangle gives the blind bound

\[
 \Delta R^{19/20+\varepsilon}
 =X^{19/20+\delta/20-\ell+\varepsilon}.                           \tag{3.11}
\]

It is a correct repaired source consequence, but (3.9) is strictly
stronger.  Therefore (3.11) should not be promoted as the completion's
capacity; its value is only to show that scalar use of the named source
theorems adds no saving.

### 3.4 Inverse-selector-first completion: Kloosterman, not Ramanujan

Define on \(\mathbb Z/r\mathbb Z\)

\[
 g_r(m)=
 \begin{cases}
 v_r(\overline m),&(m,r)=1,\\
 0,&(m,r)>1,
 \end{cases}
 \qquad
 \widehat g_r(h)={1\over r}\sum_{m\bmod r}g_r(m)e(-hm/r).        \tag{3.12}
\]

Fourier inversion in the rough variable \(m\) gives

\[
 S_r^{\times}
 =\sum_{h\bmod r}\widehat g_r(h)
   S(N_0,h;r),
 \qquad
 S(a,b;r)=\sum_{m\bmod r}^{*}e((a\overline m+bm)/r).             \tag{3.13}
\]

Here

\[
 \widehat g_r(h)={1\over r}
 \sum_{\substack{k\asymp K\\(k,r)=1}}
 b_r(k)e(\xi k/r)e(-h\overline k/r),                             \tag{3.14}
\]

so the completed coefficient is itself an incomplete inverse-fraction
sum depending jointly on \((r,h)\).  Smoothness of the original interval
does not give Fourier decay in \(h\) after the inversion permutation.
Parseval and Cauchy give only

\[
 \sum_h|\widehat g_r(h)|^2\ll {1\over rK},\qquad
 \sum_h|\widehat g_r(h)|\ll K^{-1/2}.                            \tag{3.15}
\]

The discovery report's normalization (3.15) is correct.  Its gcd
qualification can be removed.  Put \(d=(N_0,r)\).  Weil's bound and
Cauchy--Schwarz yield

\[
 \begin{aligned}
 |S_r^{\times}|
 &\ll r^{1/2+\varepsilon}
       \sum_h|\widehat g_r(h)|(d,h)^{1/2}\\
 &\le r^{1/2+\varepsilon}
       \left(\sum_h|\widehat g_r(h)|^2\right)^{1/2}
       \left(\sum_{h\bmod r}(d,h)\right)^{1/2}.                 \tag{3.16}
 \end{aligned}
\]

Because \(d\mid r\),

\[
 \sum_{h\bmod r}(d,h)
 ={r\over d}\sum_{h\bmod d}(d,h)
 \le r\tau(d).                                                   \tag{3.17}
\]

Combining (3.15)--(3.17) gives the uniform row estimate

\[
             |S_r^{\times}|\ll_\varepsilon
             \sqrt{r/K}\,X^\varepsilon
             \asymp\sqrt\Delta\,X^\varepsilon.                  \tag{3.18}
\]

Thus a rowwise Weil closure costs

\[
 R\sqrt\Delta X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon},
 \qquad
 \left(1-{\delta+\ell\over2}\right)-(\delta-\ell)
 =1-{3\delta\over2}+{\ell\over2}>{1\over4}.                    \tag{3.19}
\]

Since the original row has the trivial bound \(O(1)\), (3.18) is not even
the best rowwise estimate when \(\Delta>1\).  Its importance is diagnostic:
the inverse-selector Fourier transform is rough and positive Weil closure
cannot supply the missing signed modulus cancellation.  The exact joint
matrix (3.13)--(3.14), with all gcd strata restored, is the interface
survivor; neither supplied trilinear theorem accepts its coefficients.

### 3.5 Direct source, gcd, residue, and survivor audit

The blind exact gcd decomposition

\[
 \sum_{d\ {\rm odd}}\chi_4(d)
 \sum_{n\ {\rm odd}}\chi_4(n)W\!\left({X\over dnD}\right)
 \sum_{(j,n)=1}{q_L(4Xj/(dn^2))\over dj}e(Xj/n)                  \tag{3.20}
\]

is correct: it follows from \(r=dn,k=dj,d=(r,k)\), and no stratum is
discarded.  A coprime completion such as (3.7) or (3.13) is not
owner-complete until (3.20) is restored.

The blind and source reports overstate the physical residue obstruction.
With \(s=N_0+t\), where \(t\in\mathbb Z\), one has the exact fixed residue

\[
             r\mid s\quad\Longleftrightarrow\quad
             t\equiv-N_0\pmod r.                                \tag{3.21}
\]

It is not nonintegral and is not intrinsically modulus-dependent.  This
repair does not make Wright's dispersion corollary applicable: the residue
is not uniformly coprime to \(r\), the short variable \(t\) is not an
independent convolution \(mn\), its kernel remains joint in \((r,t)\),
the fixed integer \(|N_0|\asymp X\) violates the relevant residue ranges
if the convolution scale is \(\Delta\), and the source places absolute
values inside the modulus sum after a principal-term subtraction.  The
project instead needs one \(\chi_4(r)\)-signed scalar.

After these repairs, the blind direct exponent and gcd conclusions remain
valid, while its smallest-survivor conclusion should be retained.  Neither
(3.7) nor (3.13) is a strict reduction: both are invertible rewritings of
the coprime portion, and (3.20) restores the rest.  The smallest
owner-complete signed survivor is therefore (2.3), equivalently the full
smooth-completion form (3.10) or the all-gcd version of (3.13).

### 3.6 The \(a=m^2\) diagonal and determinant route

On \((k,r)=1\), introduce a square-supported source variable \(a=p^2\)
and detect \(p=k\) by

\[
 \mathbf1_{p=k}=\int_0^1e(t(p-k))\,dt.                           \tag{3.22}
\]

For each \(t\), choose

\[
 \alpha_k=k^{-1/2}e(-tk),\qquad
 \nu_{p^2}=p^{-1/2}e(tp),\qquad \nu_a=0\quad(a\ne p^2).          \tag{3.23}
\]

Both norms are \(O(1)\).  The diagonal matrix
\(k^{-1}\mathbf1_{p=k}\) has nuclear norm
\(\sum_{k\asymp K}k^{-1}\asymp1\), so this projective cost is sharp.
The conductor candidate's detector over all \(a\asymp K^2\) has norm
product \(K^{1/2}\) and is not sharp.

For real \(X=N_0+\xi\), first retain \(e(\xi k/r)\) in the separated
coefficient tensor.  On the detected diagonal,

\[
 e\!\left(N_0{p^2\overline k\over r}\right)e(\xi k/r)
 =e(Xk/r),                                                        \tag{3.24}
\]

because \(p=k\) and \(k^2\overline k\equiv k\pmod r\).  Thus the
connector is exact for every real \(X\), not only integral \(X\).  At
source lengths \((A,M,N)=(K^2,K,R)\), the sharp Bettin--Chandee terms are

\[
 F^{1/2}K^{21/20}R^{11/10},qquad
 F^{1/2}K^{11/8}R,                                               \tag{3.25}
\]

and Wright's dominant term is \(F^{1/4}KR^{11/8}\).  The discovery
exponent comparisons show that all exceed \(\Delta\) by a fixed power.
The capacity no-go survives the normalization and real-centre repairs.

Finally, put \(\tau=N_0-dr\ne0\).  The discovery determinant dictionary

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 m_1n_2-m_2n_1=-\tau                                            \tag{3.26}
\]

is algebraically exact.  With \((M_1,M_2,N_1,N_2)=(D,1,X,R)\), coefficient
norms \(1,R^{1/2}\), and aspect ratio \(\asymp1\), Bettin--Chandee
Corollary 1 has error

\[
                 X^{3/5+\varepsilon}R^{17/20}.                  \tag{3.27}
\]

Its main term is \(O(X^\varepsilon)\) per \(\tau\), by
\(\sum_{r\asymp R}(N_0,r)/r\ll X^\varepsilon\); summing the
\(O(\Delta X^\varepsilon)\) effective determinants returns \(\Delta\),
while summing (3.27) is much worse.  The zero determinant is one
divisor-bounded product level.  This calculation is internally consistent,
but the original source report explicitly did not audit Corollary 1.  It
should be source-promoted only after the dedicated post-unmask source seam
confirms the exact theorem hypotheses.

## 4. First doubtful or unproved step

After the repairs above, no algebraic or Fourier-normalization doubt remains
in the completion-order proposition.  The first unproved positive step is a
new estimate that keeps \(\chi_4(r)\) before any modulus norm and gains on
one of the equivalent owner-complete forms:

\[
 \mathscr R_{D,L}(X),qquad
 \sum_r\chi_4(r)W_r\sum_h c_r(h)\mathfrak c_r(N_0+h),qquad
 \sum_{d,n,h}\chi_4(d)\chi_4(n)\widehat g_{d,n}(h)S(N_0,h;n).
\tag{4.1}
\]

The first completed form has exact capacity \(\Delta\), and the second has
a rough joint coefficient matrix.  Neither Bettin--Chandee Theorem 1 nor
Wright Theorem 2.1 supplies the cross-modulus signed gain needed to reach
\(X^{1/4+\varepsilon}\).

The determinant import has one remaining review dependency: the source
auditor did not inspect Corollary 1.  Until its hypotheses and main-term
normalization receive that independent source check, (3.26)--(3.27) should
remain candidate evidence rather than an external accepted lemma.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Source integrality | Repaired.  Use \(N_0\in\mathbb Z\), with BC Remark 1 for the direct call or exact absorption of \(e(\xi k/r)\) into the flat tensor. |
| Direct blind exponents | Pass.  (3.2) and (3.3), including their dominance comparisons, are correct and remain non-saving. |
| Smooth-profile separation | Pass on the frozen flat cell.  Buffered Fourier expansion has \(O(1)\) projective mass and may include the fractional-centre factor. |
| Smooth-weight Fourier normalization | Pass.  The normalized coefficient is \(r^{-1}\sum_t\), with size \(R^{-1}\), \(L^1\ll K^{-1}\), and \(L^2{}^2\ll(RK)^{-1}\). |
| Complete inverse-only sum | Repaired.  It is Ramanujan, not Kloosterman.  Exact gcd summation returns \(\Delta X^\varepsilon\), improving the blind loose source bound. |
| Blind scalar completion exponent | Pass but redundant.  \(\Delta R^{19/20}\) and exponent \(19/20+\delta/20-\ell\) are correct after integer-frequency preprocessing. |
| Inverse-selector Fourier normalization | Pass.  The transform has only the Parseval masses (3.15), not smooth bandwidth \(\Delta\). |
| Kloosterman row and outer cost | Repaired and strengthened.  Gcd averaging makes \(\sqrt\Delta\) uniform per row; the positive outer cost is \(R\sqrt\Delta\), though the original row triangle \(R\) is smaller. |
| Gcd strata | Pass.  Formula (3.20) is exact and must accompany every coprime completion. |
| Fixed residue | Repaired.  The exact shifted residue is \(-N_0\), but all convolution, coprimality, coefficient, range, and absolute-value mismatches remain. |
| \(a=m^2\) diagonal | Discovery normalization passes; conductor normalization is nonoptimal by \(K^{1/2}\).  Fractional-centre absorption makes the connector exact for real \(X\). |
| Determinant route | Algebra and capacity pass; external source promotion remains conditional on the independent Corollary 1 source seam. |
| Character placement | Pass.  \(\chi_4\) stays outside each row and before the final modulus triangle; no positive completion is advertised as character cancellation. |
| Smallest survivor | Pass after wording repair.  The whole flat wave, or a fully gcd-restored equivalent completion, remains the smallest owner-complete survivor. |
| Endpoint scope | Pass.  No omitted owner or downstream obligation is changed. |

No numerical experiment was used.  The review was 100% analytical and
source-algebraic.

## 6. Dependencies and exact artifacts used

Read completely for this review:

- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/wright_bc_exact_source_card.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/briefs/discovery_post_unmask_blind_completion_audit.md`.

The source-frequency conclusions use the primary-source audit of
Bettin--Chandee arXiv:1502.00769v1, Theorem 1 and Remark 1, and Wright
arXiv:2604.25177v2, Theorem 2.1.  The determinant statement is retained
conditionally because the source report did not audit Bettin--Chandee
Corollary 1.  The withdrawn arXiv:2601.00292 was not used.

## 7. Recommended state effect

**Revise.**  Retain the Round-135 terminal label `source_level_no_go`, but
make the following repairs before promotion:

1. promote smooth-weight-first completion only as the exact Ramanujan or
   additive-orthogonality self-return (3.7)--(3.10), with capacity
   \(\Delta X^\varepsilon\);
2. retain \(\Delta R^{19/20}\) only as a redundant scalar-source diagnostic,
   not as the completion's best bound;
3. identify inverse-selector-first completion separately as the
   Kloosterman matrix (3.13)--(3.14), with exact Parseval masses and uniform
   positive row cost (3.18)--(3.19);
4. replace every real-\(\vartheta\) use by integer \(N_0\) plus Remark 1 or
   exact fractional-centre tensor absorption;
5. promote the sharp square-supported \(a=m^2\) diagonal normalization,
   not the conductor's crude all-\(a\) detector, and state that it works for
   all real \(X\) after preprocessing;
6. state the exact shifted residue \(-N_0\), while retaining the remaining
   Wright-dispersion mismatches; and
7. retain the determinant calculation as candidate evidence until its
   separate source seam is green.

Keep the flat-wave quarter estimate, complete UNBAL, BAL, TOP, M9-M2,
M9-M1, endpoint uniformity, M9, the internal global exponent, and the
Gauss-circle target unchanged.
