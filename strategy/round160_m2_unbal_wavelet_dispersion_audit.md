# Round 160 M2 UNBAL wavelet--dispersion audit

Date: 2026-08-25

Role: alternative-surface strategy audit; no proof-state authority

Graph read for this audit: `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

## 1. Result

The physical prescribed-centre wave is already reduced to the correct
noninvertible arithmetic interface.  For one frozen flat-smooth strict
UNBAL owner, the smallest unresolved scalar is the centered nonzero-frequency
level-four Kloosterman coefficient matrix in (160.WD10) below.  Its target is
exactly \(X^{1/4+\varepsilon}\), equivalently the original
\(M^{3/4}X^\varepsilon\) product-phase target.

The current accepted dependencies do not prove that target on any open
strict-UNBAL chamber.  They also do not prove a signed lower bound or a
universal impossibility theorem.  What they do prove is a complete scoped
method no-go for the currently available routes:

- product regrouping and functional equations return the same width
  \(\Delta=D/L\);
- the sign-preserving \(h\)-process followed by \(k\)-Poisson returns the
  prescribed-centre wave exactly;
- smooth-weight-first completion returns the absolute
  \(\Delta X^\varepsilon\) capacity;
- inverse-selector-first completion gives the joint Kloosterman matrix, and
  coefficient-blind completion costs \(R\sqrt\Delta X^\varepsilon\);
- the audited Bettin--Chandee, Wright, scalar Kuznetsov, Linnik-range,
  Gram, and second-stationary interfaces are either quantitatively worse or
  invert back to the original row.

Consequently a Round-160 campaign called merely "wavelet dispersion" or
"Kloosterman completion" would repeat Rounds 107, 118, 123--125, 135, and
143.  It cannot have a new theorem or strict range as a credible exit gate
without a new joint-matrix hypothesis.  It could only reproduce an already
accepted scoped no-go.  This surface should remain parked unless the round is
preloaded with a precise new theorem for (160.WD10), or with a genuinely new
literal-matrix obstruction stronger than the abstract row-Parseval control.

## 2. Exact statement and hypotheses

Let

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor,\qquad 0\leq\xi<1,
 \tag{160.WD1}
\]

and, for one frozen flat-smooth strict-UNBAL component, put

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 R={X\over D},\qquad K={XL\over D^2},\qquad
 \Delta={R\over K}={D\over L},
 \tag{160.WD2}
\]

\[
 {1\over4}\leq\delta<{1\over2},\qquad
 0\leq\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463.
 \tag{160.WD3}
\]

Write \(a=\delta-\ell\).  Then

\[
 {1\over4}<a<{1\over2},\qquad
 M=LK={XL^2\over D^2}=X^{1-2a},\qquad
 F=\sqrt{XM}={XL\over D}=X^{1-a}.
 \tag{160.WD4}
\]

With the literal smooth profiles \(W,q_L\), the physical row is

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{r\asymp R\\r\ \operatorname{odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\asymp K}{q_L(4Xk/r^2)\over k}e(Xk/r).
 \tag{160.WD5}
\]

It is also the prescribed-centre truncated-divisor wave

\[
 \mathscr R_{D,L}(X)=
 \sum_s\sum_{\substack{r\mid s\\r\ \operatorname{odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \mathcal Q_L\!\left({r(X-s)\over4X}\right),
 \quad
 \mathcal Q_L(y)=\int_0^\infty {q_L(h)\over h}e(hy)\,dh,
 \tag{160.WD6}
\]

rapidly supported on \(|s-X|\ll\Delta X^\varepsilon\).  Its exact target is

\[
 \boxed{\mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}.}
 \tag{160.WD7}
\]

For the inverse-first arithmetic form, write \(r=gn\), \(k=gj\),
\((j,n)=1\), and define

\[
 b_{g,n}(j)=
 {q_L(4Xj/(gn^2))\over gj}e(\xi j/n),
 \tag{160.WD8}
\]

\[
 \gamma_{g,n}(m)=
 \begin{cases}
 b_{g,n}(\overline m_n),& (m,n)=1\text{ and the inverse lies in the
 literal support},\\
 0,&(m,n)>1,
 \end{cases}
 \quad
 \widehat\gamma_{g,n}(h)={1\over n}
 \sum_{m\bmod n}\gamma_{g,n}(m)e(-hm/n).
 \tag{160.WD9}
\]

For \(\Gamma_0(4)\), primitive \(\chi_4\), weight parity one, cusps
\((\infty,0)\), and the accepted scaling convention,

\[
 S^{\chi_4}_{\infty0}(4N_0,h;2n)
 =\chi_4(n)S(N_0,h;n),\qquad n\ \operatorname{odd}.
\]

Thus (160.WD5) is exactly

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{g,n\ \operatorname{odd}\\gn\asymp R}}
 \chi_4(g)W\!\left({X\over gnD}\right)
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n).
 \tag{160.WD10}
\]

Use centered representatives
\(-(n-1)/2\leq h\leq(n-1)/2\).  The \(h=0\) class is
\(O_\varepsilon(X^\varepsilon)\).  Therefore the exact prospective new
theorem is (160.WD7) with the \(h=0\) term deleted from (160.WD10), one
outer absolute value only, and all \(g,n,h\), gcd strata, real-centre
factors, profiles, entries, and exits retained.

## 3. Proof and derivation of the audit conclusion

The accepted stationary normalization gives

\[
 \mathcal T_{L,K}^{\mathrm{stat}}
 =i e(-1/8)X^{-1/4}M^{3/4}\mathscr R_{D,L}(X),
 \tag{160.WD11}
\]

while the inherited physical prefactor is
\(-e(1/8)X^{1/4}M^{-3/4}/(2\pi)\).  Hence the physical block is
exactly \(-i\mathscr R_{D,L}(X)/(2\pi)\), up to the already controlled
flat-smooth stationary remainder.  This verifies that (160.WD7) is neither
stronger nor weaker than the original three-quarter target.

The absolute product bound and the accepted curvature envelope are

\[
 |\mathscr R_{D,L}(X)|\ll_\varepsilon X^\varepsilon
 \min\left\{\Delta,
 \sqrt{XL/D}+\sqrt{X/(LD)}\right\}.
 \tag{160.WD12}
\]

Since \(L\geq1\), the first square-root term dominates the second for
exponent bookkeeping.  Thus the envelope exponent is

\[
 \beta(a)=\min\left\{a,{1-a\over2}\right\}>{1\over4}
 \quad\left({1\over4}<a<{1\over2}\right).
 \tag{160.WD13}
\]

It saves a power over \(\Delta\) only for \(a>1/3\), and even there its
remaining excess over the target is

\[
 X^{(1-a)/2-1/4}=X^{(1-2a)/4}=M^{1/4}.
 \tag{160.WD14}
\]

Therefore (160.WD12) supplies no open strict-UNBAL target range.  It is
target-sized only on the terminal boundary, or in a collar thin enough to
be absorbed into \(X^\varepsilon\).

The inverse-first coefficient bounds are

\[
 \sum_j|b_{g,n}(j)|^2\ll_\varepsilon(gK)^{-1}X^\varepsilon,
 \qquad
 \sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
 \ll_\varepsilon(RK)^{-1}X^\varepsilon.
 \tag{160.WD15}
\]

At \(h=0\), \(|\widehat\gamma_{g,n}(0)|\ll R^{-1}X^\varepsilon\),
\(S(N_0,0;n)=c_n(N_0)\), and
\(\sum_{n\asymp R/g}(n,N_0)\ll(R/g)X^\varepsilon\).  The fixed-\(g\)
cost is \(O_\varepsilon(g^{-1}X^\varepsilon)\), proving the claimed safe
zero class after the harmonic \(g\)-sum.

For the complete positive closure,

\[
 \sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n).
 \tag{160.WD16}
\]

Cauchy on a row costs \(\sqrt\Delta/g\); there are \(O(R/g)\) rows at
fixed \(g\).  Summation gives

\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon R\sqrt\Delta X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon}.
 \tag{160.WD17}
\]

If \(p=1-(\delta+\ell)/2\), then throughout (160.WD3)

\[
 p-a=1-{3\delta\over2}+{\ell\over2}>{1\over4},
 \qquad
 p-{1-a\over2}={1\over2}-\ell>{1\over4}.
 \tag{160.WD18}
\]

Thus positive Kloosterman completion is uniformly worse than both branches
of (160.WD12).  This remains true for arbitrary unit row phases, so it does
not use the required cross-modulus character cancellation.

The remaining method ledger is exact:

| Route | Exact output | Capacity or obstruction |
|---|---|---|
| Product regrouping and two degree-one functional equations | Dual lengths \(X/D\) and \(D\), resonant width \(\Delta\) | Absolute dual summation returns \(\Delta X^\varepsilon\) |
| \(h\)-process then \(k\)-Poisson | (160.WD6) with physical constant \(-i/(2\pi)\) | Invertible self-return |
| Smooth-weight-first finite completion | Ramanujan/additive sums | Exactly \(\Delta X^\varepsilon\) |
| Inverse-selector-first completion | The matrix (160.WD10) | Positive closure is (160.WD17) |
| Direct Bettin--Chandee | \(F^{1/2}(R^{11/10}K^{-3/20}+R)\) | The two exponent margins over \(\Delta\) exceed \(3/10\) and \(1/4\) |
| Direct Wright | \(R^{11/8}F^{1/4}\) | Its exponent margin over \(\Delta\) exceeds \(5/16\) |
| Fixed-determinant dispersion | Main terms total \(\Delta X^\varepsilon\); error \(X^{3/5}R^{17/20}\) per nonzero determinant | No saving after the determinant sum |
| Scalar level-\(4/8\) Kuznetsov or Linnik | Requires fixed Fourier arguments and a common smooth modulus test | The literal \((n,h)\)-matrix has neither accepted common data nor complementary long-\(h\) coverage |
| Sum all \(h\) by Fourier inversion | The original reciprocal row | Exact self-return |
| Shifted Gram and second stationary transforms | Safe zero alias/diagonal, then the original reciprocal principal phase | No contraction of the full actual-character aggregate |

The Round-95 cluster theorem has different scales and a different reduced
determinant scalar.  Its coefficient-blind capacity warning applies, but
its \(Y^{1/8}\), \(Y^{1/6}\), and \(Y^{1/2}\) powers do not transfer to
(160.WD7).  Likewise the Round-64/65 M1 product-wavelet moment and Abel
identities show why wavelet cancellation alone is illusory; they provide no
M2 estimate.  These are hostile controls, not hidden dependencies.

The table exhausts the existing accepted mechanisms for this surface.
Every route either returns (160.WD5)/(160.WD6), yields an upper bound no
better than (160.WD12), or requires the new theorem stated next.  That is
the claimed scoped method no-go.

## 4. First doubtful or unproved step

The first unproved step is the literal centered joint-matrix estimate

\[
 \boxed{
 \left|
 \sum_{\substack{g,n\ \operatorname{odd}\\gn\asymp R}}
 \chi_4(g)W\!\left({X\over gnD}\right)
 \sum_{\substack{-(n-1)/2\leq h\leq(n-1)/2\\h\ne0}}
 \widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n)
 \right|
 \ll_\varepsilon X^{1/4+\varepsilon}.}
 \tag{160.WD19}
\]

A power-saving version

\[
 \text{left side of (160.WD19)}
 \ll X^{\beta(a)-\eta+\varepsilon}
 \tag{160.WD20}
\]

would give a strict target range only where

\[
 \eta\geq
 \begin{cases}
 a-1/4,&1/4<a\leq1/3,\\
 (1-2a)/4,&1/3\leq a<1/2.
 \end{cases}
 \tag{160.WD21}
\]

This makes any proposed "some cancellation" exit gate too vague: the
gain must be priced against (160.WD21).

A proof of (160.WD19) must cross all of the following seams at once:

1. preserve \(\chi_4(g)\chi_4(n)\) before every positive modulus norm;
2. retain every gcd stratum and allow arbitrary \((N_0,n)\);
3. control the moving inverse support and the joint coefficient
   \(\widehat\gamma_{g,n}(h)\) with genuine modulus Sobolev/Bessel data,
   rather than algebraic SVD alone;
4. cover the long centered \(h\)-range omitted by the available Linnik
   range \(h\ll K/(Lg^2)\);
5. include weight-one odd-character level-\(4/8\) holomorphic, Maaß,
   exceptional, Eisenstein, cusp, and oldclass terms with correct signs and
   transforms;
6. retain the real-centre factor, both frequency signs, profiles, entries,
   exits, and all transform remainders;
7. after the flat owner, supply separate sharp, starred, clipped,
   transition, and arithmetic-owner endpoint kernels before claiming
   complete UNBAL.

No accepted lemma or audited source supplies this joint theorem.  A new
vector-valued trace formula or a new low-projective-cost decomposition is
not a routine application of the existing scalar formulas; proving it would
be the main analytic theorem of the campaign.

## 5. Required control test and outcome

The mandatory control is to expand any proposed matrix theorem back through
(160.WD9) before taking absolute values.

First, finite Fourier orthogonality gives exactly

\[
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
 =\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n).
 \tag{160.WD22}
\]

Thus a proof whose only gain appears after summing all \(h\), applying row
Parseval, interpolating point masses, or using an unrestricted scalar trace
formula has merely inverted back to the original reciprocal row.  It fails
the control.

Second, replace \(\chi_4(g)\) by arbitrary unit phases while keeping the
same row norms.  Bounds (160.WD12) and (160.WD17) are unchanged.  Therefore
any proposed contraction derived only from support, curvature, Parseval,
or complete Kloosterman energy is coefficient-blind and cannot be credited
as the required character saving.  It also fails the control.

Third, test the two strict endpoints of (160.WD13).  For every fixed
\(1/4<a<1/2\), \(\beta(a)>1/4\); hence the current envelope gives no open
strict range.  The coherent-run and integer phase-one square-sector
controls from Round 118 are individually target-safe, but they do not bound
their disconnected signed complement and therefore do not falsify or prove
(160.WD19).

Outcome: all three controls pass as obstructions.  They validate the scoped
no-go for the existing mechanisms, but they provide neither an actual
counterexample nor the missing signed upper bound.

## 6. Dependencies and exact artifacts used

Accepted graph dependencies used directly:

- `M9-M2-smooth-dual-three-quarter-equivalence`;
- `M9-M2-character-factor`;
- `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`;
- `M9-M2-unbalanced-flat-wave-curvature-envelope`;
- `M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction`;
- `M9-M2-unbalanced-level-four-spectral-matrix-obstruction`;
- `Bettin-Chandee-Wright-Kloosterman-source-audit`.

The open target is
`M9-M2-smooth-unbalanced-three-quarter-estimate`; it remains a dependency
of `M9-M2-physical-one-count-assembly` and a blocker of `M9-M2`.

Exact local artifacts read:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`;
- the syntheses of the Round-123, Round-124, and Round-125 UNBAL
  Gram/stationary/off-product campaigns;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md` and
  `candidates/conductor_degenerate_source_capacity.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/synthesis.md` and
  `candidates/conductor_round143_level_four_matrix_obstruction.md`;
- the Round-95 cluster synthesis and the Round-64/65 product-wavelet
  syntheses, used only as hostile transfer controls.

No new external theorem, numerical experiment, average over \(X\), or
coefficient model is used.  The audit is entirely analytical and
algebraic.

## 7. Recommended state effect

Recommend `no change`.  This strategy audit proves no new graph claim; its
scoped no-go is already represented by the Round-135 and Round-143
obstruction nodes.  Keep the flat-smooth target, every remaining UNBAL
owner, BAL, hard TOP, `M9-M2`, endpoint uniformity, `M9`, the bridge, and
the quarter target unchanged.  No exponent changes.

Do not select this as Round 160 under a generic transform, completion,
dispersion, scalar Kuznetsov, or fixed-index large-sieve objective.  Reopen
the surface only if the frozen objective is (160.WD19) or (160.WD20) with
the exact threshold (160.WD21), and the initial packet already contains one
of the following genuinely new inputs:

- a source-audited vector-valued odd-character trace theorem accepting the
  literal \((n,h)\)-matrix with a quantified owner-saving norm; or
- a proved low-projective-cost decomposition of the literal matrix with
  uniform modulus smoothness and long-frequency coverage; or
- a literal arithmetic counterexample or literal nuclear/Sobolev lower
  bound that strengthens the existing abstract row-Parseval obstruction.

Absent such an input, a bounded campaign cannot credibly exit with a new
theorem, strict range, or new exact no-go.  It should rotate to a distinct
unresolved owner rather than repeat an invertible transform.
