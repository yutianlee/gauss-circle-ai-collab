# Round 62 hostile/source audit: subcritical small-angle collapse

## 1. Result

The small-angle collapse is valid, with a stronger exact conclusion for
the limiting arithmetic coefficient.  Fix \(0<\nu<1/2\), put
\(N=X^\nu\), and restrict \(n\) to a fixed smooth block
\(n\asymp N\).  Uniformly for every factorization \(n=hq\) with \(q\)
positive and odd,
\[
 \Omega_X^*(n,h)
 =\mathbf1_{d_{n,h}\le y}^{*}
 +O\!\left({n\over Y}\right),
 \qquad
 d_{n,h}=2h\sqrt{X/n}.
 \tag{62.H1}
\]
The star on the right means weight \(1/2\) at \(d_{n,h}=y\), weight
\(1\) below, and weight \(0\) above.

Moreover, throughout a fixed subcritical block and for all sufficiently
large \(X\), the floor-perturbed starred coefficient in the packet is
exactly the \(X\)-independent one-sided divisor coefficient
\[
 \boxed{
 \mathcal D(n)=
 \sum_{\substack{hq=n\\q\ {\rm odd}\\q>4h}}\chi_4(q)
 =
 \sum_{\substack{q\mid n,\ q\ {\rm odd}\\q>2\sqrt n}}\chi_4(q).}
 \tag{62.H2}
\]
No equality star survives in (62.H2), because \(q=4h\) is even.

The coefficient replacement error in one radial block is
\[
 \ll_V {N^{5/4}\log(2N)\over Y},
 \tag{62.H3}
\]
so it is power-safe for every fixed \(\nu<2/5\), logarithmically
target-safe at \(\nu=2/5\), and not target-safe by this absolute ledger
for \(\nu>2/5\).  Thus the exact threshold in the usual
\(X^\varepsilon\) convention is \(\nu\le2/5\), not strictly
\(\nu<2/5\).

The reduction does not estimate the signed radial sum with coefficient
\(\mathcal D(n)\).  Popov's truncated Voronoi theorem applies to the
complete coefficient \(r_2(n)=4\sum_{q\mid n}\chi_4(q)\), not the
nonmultiplicative one-sided truncation (62.H2), and supplies no bound for
it.  Hence no downstream exponent changes.

## 2. Exact statement and hypotheses

Let
\[
 R=X^{1/4},\qquad Y=\sqrt X,\qquad y=\lfloor\sqrt X\rfloor,
\]
and use the accepted partition
\[
 \mathbf1_{1\le d\le y}
 =w_0(d)+\sum_{j=1}^{J}w_j(d)+w_{\rm bot}(d).
\tag{62.H4}
\]
Here \(D_j=2^{-j}y\), \(H_j=\lfloor D_j/R\rfloor\),
\(\operatorname {supp}w_j\subset[D_j/2,4D_j/3]\) for interior
scales, the top is \(w_0(d)=\mathbf1_{d\le y}W(d/y)\), and
\(w_{\rm bot}\) is supported on \(d<4R/3\).

Let \(V\) be fixed and supported in \([a,b]\subset(0,\infty)\).
The conclusions below are uniform for
\[
 aN\le n\le bN,\qquad N=X^\nu,\qquad 0<\nu<1/2.
\tag{62.H5}
\]
For a profile containing \(d=d_{n,h}\), put
\[
 u_j={h\over H_j+1}.
\]
Since \(\lfloor z\rfloor+1>z\),
\[
 u_j
 <{hR\over D_j}
 ={d\over2D_j}\sqrt{n\over Y}
 \le {2\over3}\sqrt{n\over Y}.
\tag{62.H6}
\]
For the top profile the last constant improves to \(1/2\).
Conversely, on a nonzero profile and in (62.H5),
\(D_j/R\to\infty\), so \(H_j+1\le2D_j/R\) eventually and
\[
 u_j\asymp_V\sqrt{n/Y}.
\tag{62.H7}
\]
The upper bound (62.H6), not the comparability, is what is needed for
the uniform error.

The exact finite-\(X\) cone coefficient is
\[
 \mathcal D_X^*(n)
 =
 \sum_{\substack{hq=n,\ q\ {\rm odd}\\q\ge4\vartheta_Xh}}^{*}
 \chi_4(q),
 \qquad
 \vartheta_X={X\over y^2}.
\tag{62.H8}
\]
The star is half weight at equality.  Formula (62.H2) is the exact
subcritical simplification of (62.H8), not merely its pointwise limit
for fixed \(n\).

## 3. Proof and seam derivation

Expanding \(\cot z=z^{-1}-z/3-z^3/45+O(z^5)\) gives
\[
\begin{aligned}
 \Phi(u)
 &=\pi u(1-u)\cot(\pi u)+u\\
 &=1-{\pi^2\over3}u^2+{\pi^2\over3}u^3+O(u^4).
\end{aligned}
\tag{62.H9}
\]
Thus \((\Phi(u)-1)/u^2\) extends continuously to \(u=0\).  In
particular,
\[
 |\Phi(u)-1|\le C u^2
\tag{62.H10}
\]
uniformly on a fixed neighborhood of zero.  By (62.H6), every actual
supported \(u_j\) lies in that neighborhood for sufficiently large
\(X\), and
\[
 |\Phi(u_j)-1|\ll {n\over Y}.
\tag{62.H11}
\]

The active-height indicator causes no loss.  Indeed (62.H6) is less
than \(1\) for large \(X\).  If \(h\ge H_j+1\), then
\(h/(H_j+1)\ge1\), a contradiction.  Hence every profile that can
contain \(d_{n,h}\) automatically has \(h\le H_j\).

The bottom owner is also absent from the actual stationary sample:
\[
 {d_{n,h}\over R}
 ={2hR\over\sqrt n}
 \ge {2R\over\sqrt{bN}}\longrightarrow\infty.
\tag{62.H12}
\]
Thus \(w_{\rm bot}(d_{n,h})=0\).  With all active indicators now equal
to one, the exact telescope (62.H4) gives
\[
 \sum_j[w_j(d_{n,h})]^*
 =\mathbf1_{d_{n,h}\le y}^{*}.
\tag{62.H13}
\]
At a smooth profile support endpoint the profile value is zero, so a
stationary half-weight changes nothing.  The only nonzero hard endpoint
is \(d=y\), where \(w_0(y)=1\) and the stationary main term has weight
\(1/2\).  For \(d>y\), the top is truncated and every interior active
profile is supported below \(2y/3\), so both sides of (62.H13) vanish.

Since all profiles are nonnegative and their starred mass is at most
one, inserting \(\Phi=1+O(n/Y)\) into (62.1) and using (62.H13)
proves (62.H1) without an \(O(\log X)\) scale loss.  Notice that the
inactive bottom contribution remains separately owned before Fourier
expansion; it is not inserted into either side of (62.H1).

For the exact arithmetic cone,
\[
 d_{n,h}\le y
 \quad\Longleftrightarrow\quad
 q\ge4\vartheta_Xh.
\tag{62.H14}
\]
Also
\[
 0\le\vartheta_X-1
 ={X-y^2\over y^2}\ll X^{-1/2}.
\]
On a term near this boundary, \(h\le\sqrt n/2\), so uniformly in
(62.H5),
\[
 4h(\vartheta_X-1)
 \ll {\sqrt n\over\sqrt X}=o(1).
\tag{62.H15}
\]
For large \(X\), the threshold \(4\vartheta_Xh\) lies in
\([4h,4h+1)\).  Because \(q\) is an odd integer and \(4h\) is even,
(62.H14) is then exactly \(q>4h\); equality is impossible.  This proves
(62.H2) and removes both the floor perturbation and the star uniformly
on the whole subcritical block.

Finally,
\[
 |\mathcal C_X^*(n)-\mathcal D(n)|
 \ll\tau(n){n\over Y}.
\tag{62.H16}
\]
Therefore
\[
\begin{aligned}
 \sum_n|V(n/N)|n^{-3/4}
 |\mathcal C_X^*(n)-\mathcal D(n)|
 &\ll_V {1\over Y}\sum_{n\asymp N}\tau(n)n^{1/4}\\
 &\ll_V {N^{5/4}\log(2N)\over Y},
\end{aligned}
\]
which is (62.H3).  For \(N=X^\nu\), its power is
\[
 X^{5\nu/4-1/2}\log X.
\tag{62.H17}
\]
This tends to zero by a power for \(\nu<2/5\), is \(O(\log X)\) at
\(\nu=2/5\), and grows by a power for \(\nu>2/5\).

## 4. First doubtful or unproved step

The first unproved step is the signed estimate
\[
 \sum_nV(n/N)\mathcal D(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{62.H18}
\]
Neither the Taylor expansion nor denominator telescoping supplies
cancellation between distinct products \(n=hq\).  The limiting
coefficient is not \(r_2(n)/4\): it keeps only the cone \(q>4h\).
Its complement \(q<4h\) carries the rest of the classical divisor sum,
and exchanging \(h\) and \(q\) does not preserve either the factor \(4\)
or the placement of \(\chi_4\).

There is a strict absolute-capacity obstruction to finishing by triangle
inequality.  For every odd prime \(p>4\),
\[
 \mathcal D(p)=\chi_4(p),
\]
because only \((h,q)=(1,p)\) lies in \(q>4h\).  Hence, for a
nonnegative radial cutoff bounded below on a fixed subinterval,
\[
 \sum_{p\asymp N}p^{-3/4}|\mathcal D(p)|
 \gg {N^{1/4}\over\log N}.
\tag{62.H19}
\]
Thus the actual one-sided coefficient has polynomial absolute mass and
(62.H18) requires genuine phase/character cancellation.  This does not
constitute a lower bound for the signed sum and does not rule out a new
arithmetic theorem.

For \(2/5<\nu<1/2\), there is an earlier limitation: even the absolute
replacement error (62.H17) exceeds the normalized target.  A signed
treatment of the \(\Phi-1\) correction, a higher-order retained
coefficient, or a different mechanism would be required before the
one-sided model alone could replace the actual symbol.

## 5. Control tests and outcomes

| Control | Hostile test | Outcome |
|---|---|---|
| \(\Phi\) quadratic expansion | Recompute through the cubic term and check uniformity. | Pass: (62.H9) has cubic coefficient \(+\pi^2/3\), and (62.H10) is uniform on the actual shrinking range. |
| Height-floor ratio | Use \(H_j+1\), not \(D_j/R\), in the inequality. | Pass: \(\lfloor z\rfloor+1>z\) gives the floor-safe upper bound (62.H6); no \(1/H_j\) error appears. |
| Active cutoff | Test whether a supported profile can have \(h>H_j\). | Pass for fixed \(\nu<1/2\): (62.H6) is \(<1\), forcing \(h\le H_j\) integrally. |
| Partition telescope | Sum actual nonnegative profiles rather than their supports. | Pass: (62.H13) is exact, and the error is weighted by total mass at most one, not by the number of scales. |
| Bottom support | Compare the smallest possible stationary denominator with \(R\). | Pass: (62.H12) tends to infinity, so the separately owned bottom never occurs in the subcritical stationary coefficient. |
| Hard top and stars | Check \(d=y\), smooth support endpoints, and \(d>y\). | Pass: only \(d=y\) has a nonzero half-weight; smooth endpoint values vanish and the hard cotangent boundary remains separate. |
| Divisor-error sum | Include divisor multiplicity and the \(n^{-3/4}\) weight. | Pass: the exact absolute ledger is \(N^{5/4}\log(2N)/Y\). |
| Two-fifths threshold | Test strict, equality, and supercritical sides. | Pass with correction: \(\nu<2/5\) gives power decay, \(\nu=2/5\) gives a logarithm absorbed by \(X^\varepsilon\), and \(\nu>2/5\) fails absolutely. |
| One-sided divisor identity | Remove the \(y/\sqrt X\) perturbation without ignoring integrality. | Pass: (62.H15) and odd \(q\) give the exact floor-free cone \(q>4h\) uniformly. |
| Signed radial capacity | Test an actual coefficient family. | No-go for absolute methods: primes give (62.H19); no signed estimate follows. |
| Downstream scope | Test implications for full GAR, M9-M1, M9, or the exponent. | Fail: a target-safe coefficient replacement is not a bound for (62.H18). |

The external factor \(R=X^{1/4}\) in the accepted M1 recombination is
unchanged.  Thus a normalized \(O(X^\varepsilon)\) error corresponds
exactly to a physical \(O(RX^\varepsilon)\) error; no extra \(N\)-power
is hidden in the normalization.

## 6. Dependencies and primary-source applicability

This audit used only the selected artifacts:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/derivation_packet.md;
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md;
- rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md; and
- sources/popov_2024_voronoi_gauss.md.

Popov's Theorem 5 gives a truncated Voronoi formula with coefficient
\(r_2(n)=4\sum_{q\mid n}\chi_4(q)\) and a full radial cosine sum.  The
coefficient (62.H2) retains only factorizations \(q>4h\); the cutoff
depends jointly on complementary divisors and destroys the complete
Dirichlet convolution to which Popov's formula applies.  Adding the
omitted cone recovers the classical coefficient, but Popov bounds
neither cone separately, and its complete radial sum at the relevant
cutoff is itself Gauss-equivalent at target scale.  Therefore this
primary theorem is non-importable for (62.H18).

No other primary theorem in the permitted context has the required
one-sided character-divisor coefficient.  Since no genuinely matching
candidate theorem was identified, no additional literature search was
performed.  No numerical experiment was used.

## 7. Recommended state effect

Promote, after independent validation, the scoped collapse (62.H1), the
exact floor-free coefficient (62.H2), and the replacement error
(62.H3).  State the threshold as follows: power-safe for fixed
\(\nu<2/5\), \(X^\varepsilon\)-safe with an endpoint logarithm at
\(\nu=2/5\), and not absolutely safe above \(2/5\).

Retain the one-sided signed radial estimate (62.H18), the range
\(2/5<\nu<1/2\), full GAR, M9-M1, M9, and the Gauss-circle exponent as
open.  Reject any claim that the active telescope produces
\(r_2(n)/4\), that the bottom owner must be inserted into
\(\mathcal D\), that the hard star can be discarded before the
integrality argument, or that Popov's full-coefficient theorem estimates
the one-sided cone.
