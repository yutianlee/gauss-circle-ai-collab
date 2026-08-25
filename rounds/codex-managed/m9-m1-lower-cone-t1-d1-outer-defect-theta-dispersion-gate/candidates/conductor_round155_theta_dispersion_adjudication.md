# Round 155 conductor candidate: exact theta inversion and the remaining signed seam

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate`
- Round: 155
- Role: conductor-selected proof kernel pending terminal source and hostile review
- Starting graph SHA-256: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`
- Proposed terminal label: `outer_defect_theta_dispersion_no_go`
- Allocation used: 100% analytic, algebraic, and primary-source work; 0% numerical

## 1. Result and exact scope

Fix an arbitrary constant $A>0$ and put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM}.
\tag{155.CA1}
$$

For a dyadic block $J_A<V\le K$, the accepted selected linearization is

$$
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac j{2k}\right),
\tag{155.CA2}
$$

with the literal profile, support, endpoints, and both signs. Round 155
does not estimate this block. It proves a new exact route obstruction and
localizes the first remaining signed theorem.

Let $q=4N$, let $d\mid N$ be odd, and put

$$
 c=\frac qd,\qquad H=\frac c2.
\tag{155.CA3}
$$

With the exact pre-linearization coefficient $B_j$ and

$$
 \widehat B_j(2dv)=\sum_{x\bmod q}B_j(x)e_c(-2vx),
\tag{155.CA4}
$$

the accepted theta sum is

$$
 K(-v^2,-j;c)=
 \sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)
 e_c(-\bar a v^2-aj).
\tag{155.CA5}
$$

The complete half-period resummation is the exact identity

$$
 \boxed{
 \begin{aligned}
 &\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &\quad=\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
 \end{aligned}}
\tag{155.CA6}
$$

After the factor
$-i(1+i)\chi_4(d)d\sqrt c/(2Nq)$ is restored, $dc=q$ and
$(1+i)(1-i)=2$ return precisely

$$
 -\frac{i}{2N}\chi_4(d)
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
\tag{155.CA7}
$$

Summing $d$ partitions every odd $h\bmod4N$ by $(h,N)=d$ and returns the
literal quotient selector. Complete $v$-resummation is therefore exactly
the inverse of the Round-154 Gauss completion, even with the strict outer
mask and endpoints retained. It supplies no residual square-root gain.

No full target, strict positive-power defect owner, $M$-range, downstream
theorem, or exponent is proved.

## 2. Exact inversion and norm controls

For a unit $a\bmod c$, define

$$
 I_c(a,x)=\sum_{v\bmod H}e_c(-\bar a v^2-2xv).
\tag{155.CA8}
$$

The summand has exact period $H$: shifting by $c/2$ changes the exponent
by the integer $-\bar a v-\bar a c/4-x$. Completing the square and using
the all-parity even Gauss formula give

$$
 I_c(a,x)=
 \frac{1-i}{2}\epsilon_a\left(\frac ca\right)
 \sqrt c\,e_c(ax^2).
\tag{155.CA9}
$$

The multiplier identity follows from
$\bar a\equiv a\pmod4$ and quadratic-character inversion. Squaring the
theta multiplier gives $\chi_4(a)$, which proves (155.CA6). An independent
mathematical review verifies the half-period, sign, multiplier, $dc=q$,
all-parity, and mask seams.

For later Cauchy placements, fold the literal coefficient modulo $H$:

$$
 C_{j,d}(r)=
 \sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x).
\tag{155.CA10}
$$

Sampled Parseval is exactly

$$
 \boxed{
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}|C_{j,d}(r)|^2.}
\tag{155.CA11}
$$

The collisions are $x-y\equiv0\pmod{2N/d}$. On an $O(K)$ physical
span their multiplicity is $O(1+dK/N)$, so

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 \ll_\varepsilon
 \left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\tag{155.CA12}
$$

This is an upper norm capacity, not orthogonality between defects and not
a signed lower bound.

## 3. Zero mode, partial transforms, and restored powers

The $v=0$ row is mandatory. DFI Lemma 6.1, the actual
$|\widehat B_j(0)|\ll KM^{-3/4}X^\varepsilon$, and the summed gcd bound
give

$$
 |\mathcal T_{0,U}(V)|
 \ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{155.CA13}
$$

At $V=K$ this is $M^{1/4}+M^{-1/4}$. The nonzero termwise DFI/BV ledger
remains

$$
 |\mathcal T_{\ne0,U}(V)|
 \ll_\varepsilon M^{-3/4}VX^\varepsilon.
\tag{155.CA14}
$$

Both are upper bounds. They do not show the signed terms are large.

For a proper dual cutoff $\eta$, square completion gives

$$
 \sum_{v\bmod H}\eta(v)e_c(-\bar a v^2-2xv)
 =e_c(ax^2)
 \sum_{u\bmod H}\eta(u-ax)e_c(-\bar a u^2).
\tag{155.CA15}
$$

Thus every nonconstant cutoff remains coupled in $a$ and $x$. The only
translation-invariant cutoff is the complete family, and that is the
self-return (155.CA6). A future partial-frequency theorem must control
the translated chirp, its complementary modes, $v=0$, and the literal
$j$-dependent coefficient.

Square-root cancellation among the $O(VX^\varepsilon)$ restored defect
incidences would have capacity

$$
 M^{-3/4}V^{1/2}X^\varepsilon,
\tag{155.CA16}
$$

which is target-sized only for $V\le M^{3/2}$. No report proves this
cancellation, so (155.CA16) is not a strict-range theorem. At
$V=K$, it is $N^{1/4}M^{-1/2}$ and needs a second mechanism unless
$M\asymp N^{1/2}$.

## 4. Flat defect phase and exact selected seam

For fixed $k\asymp K$, the selected phase has

$$
 \frac{\partial}{\partial j}\left(-\frac j{2k}\right)=-\frac1{2k},
 \qquad \operatorname {osc}_{|j|\asymp V}\frac j{2k}
 \ll\frac VK\le1.
\tag{155.CA17}
$$

Bare archimedean $j$-integration cannot supply square-root cancellation.
After expanding the theta sum, the exact phase localizes on the circular
arc

$$
 \left\|\frac ac+\frac1{2\sqrt{x^2-j}}\right\|_{\mathbb R/\mathbb Z}
 \ll\frac1V.
\tag{155.CA18}
$$

Its total capacity is $O(1+c/V)$. Because the radius $c/V$ can exceed the
centre offset $c/(2x)$, the arc crosses zero: in positive representatives
it has both a near-zero piece and a piece near $c-c/(2x)$. Neither may be
dropped. This is reciprocal-arc localization, not a gain.

The statement-only report independently proves the exact cell reindexing,
the selected-only linearization error, the all-parity incidence bound, and
the literal bounded-variation reduction. Its ordinary-K half-period
calculation is only a blind surrogate/invertibility control and is not used
as the project's theta normalization. The exact selected theorem still
needed is

$$
 \sup_{I\subset\{n\asymp M\}}
 \left|
 \sum_{\substack{n\in I,\ n\ \mathrm{odd}\\V<|j_n|\le2V}}
 \chi_4(n)e(\sqrt{Nn})
 \right|
 \ll_\varepsilon X^\varepsilon M^{3/4},
\tag{155.CA19}
$$

with both signs and all literal endpoints. Bounded variation converts
(155.CA19) into the weighted block target, but does not prove it.

## 5. First doubtful or unproved step

The first source-unproved term in a nonzero-frequency spectral route is
the fixed-modulus zero row

$$
 \sum_{V<|j|\le2V}\widehat B_j(0)K(0,-j;4N/d),
\tag{155.CA20}
$$

uniformly in every odd $d\mid N$, both signs, the actual profile, and the
endpoints. If that row is resolved, the next missing input is a signed
estimate for the nonzero coupled matrix with
$\widehat B_j(2dv)$, or equivalently (155.CA19). It must beat
$M^{-3/4}V$, provide a second gain above $V=M^{3/2}$ when
$M<N^{1/2}$, and retain the translated cutoff, large-$d$ folds,
principal or exceptional terms, complementary frequencies, both signs,
all endpoints, and the external $B_{1,U}(1)$ seam.

Complete $v$-resummation cannot be that step because it is (155.CA6).
Bare Poisson only gives (155.CA18). Sampled Parseval preserves
(155.CA11). Current source theorems match DFI termwise only; their joint
fixed-modulus, multiplier, coefficient, zero-mode, averaging, or endpoint
hypotheses do not match the literal family. The source conclusion is a
direct no-match, not a literature-impossibility theorem.

## 6. Required controls and source scope

The candidate retains:

1. the literal selected and ambient blocks, actual profile, strict mask,
   endpoints, both signs, selected-only linearization, and external
   coefficient seam;
2. the exact $q$, $c$, $H$, Fourier, selector, $d\sqrt c$, half-Gauss,
   theta multiplier, and all gcd/two-adic normalizations;
3. complete versus truncated dual transforms and the mandatory zero mode;
4. sampled Parseval with every $2N/d$ fold and no false defect
   orthogonality;
5. the full $N$--$M$--$V$--$d$ power ledger and the hypothetical-only
   threshold $V\le M^{3/2}$;
6. the circular flat-$j$ arc, including its wrapped near-zero branch;
7. DFI as an individual Kloosterman match only, with every joint source
   analogy audited against fixed modulus, multiplier, coefficient,
   zero/exceptional terms, masks, and endpoints; and
8. complete downstream separation from $D>1$, $L>1$, generic $t=1$,
   original $t\ge2$, the Round-138 cross owner, other M1 owners, M2,
   endpoint assembly, M9, the bridge, the quarter target, and both global
   exponents.

The current source search is cutoff-checked through 25 August 2026. The
absence of a direct theorem match is method evidence only.

## 7. Recommended state effect

Subject to independent GREEN source and hostile terminal reviews:

- promote (155.CA6)--(155.CA7) as an exact inverse-Gauss self-return for
  complete half-period resummation;
- record (155.CA11)--(155.CA15) and the circular reciprocal-arc
  localization as route-scoped norm, zero-mode, partial-transform, and
  flat-phase obstructions;
- retain the full signed outer-defect target and every positive-power
  subrange as open, with (155.CA20) and then (155.CA19) as the first
  missing inputs;
- reject deletion of $v=0$, complete-$v$ square-root gain, bare
  $j$-Poisson gain, physical-diagonal-only Parseval, separated surrogate
  coefficients, fixed-modulus use of a modulus-average theorem, omission
  of principal/exceptional spectral pieces, and any claim that
  (155.CA16) is a proved range; and
- make no scale-boundary, downstream theorem, endpoint, target, or global
  exponent change.
