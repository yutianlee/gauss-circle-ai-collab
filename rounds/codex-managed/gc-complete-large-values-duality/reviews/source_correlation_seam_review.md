# Round 204 source and correlation seam review

Campaign: `gc-complete-large-values-duality`. Task: `source_correlation_seam_review`. Role: independent selected-context seam reviewer. Generated: 2026-09-26T01:17:41Z. Starting graph SHA256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. Analytical/source work only; no mathematical numerical experiments. No sibling review was read.

## 1. Result: GREEN for the assigned seam

**GREEN** for Sections 2--3 of `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, exact reviewed SHA256:

`942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.

The initially assigned version had hash `5f0c1efcdb230b7ba73206dc960a95a58a6fd03166deb8340f00ed46ab532c6e`. The conductor subsequently repaired Section 5 by adding the singleton {1}. I reread the current Sections 2--3 and that repair, and rehashed the file. This verdict attaches to the revised hash; the reviewed source/correlation argument is unchanged.

The exact square-root phase belongs to Bourgain's standard exponent-pair class. The global Theorem 6, the proper-interval provision, the phase/length distinction, the three frequency regimes, and the interpolation to kappa=13/55 are valid. No correction is required within this seam. This is not an independent approval of the separate duality, infinite recombination, smoothing, or moment seams.

## 2. Exact statement and hypotheses

Let T>=2 and 1<=N<=T^(3/2) be real, let C1>0 be fixed, and put e(t)=exp(2 pi i t). For any interval J contained in (N,2N], with arbitrary real endpoints, and every real u with 0<|u|<=C1 T,

\[
 \left|\sum_{n\in J\cap\mathbb Z}e(u\sqrt n)\right|
 \ll_{\epsilon,C_1}T^\epsilon\sqrt N
       (|u|^{13/55}+|u|^{-1}).                         \tag{R1}
\]

Constants are uniform in J, N, u, and T. Fixed enlargement factors in N or the frequency range only alter the implied constant. For J=(N,2N], this is candidate (L4). It is an unweighted estimate. At u=0 the exact value is the number of summands; (R1) is not invoked on the Gram diagonal. Negative u follows by conjugation.

The external input is the already accepted global exponent pair (13/84+eta,55/84+eta), for arbitrarily small fixed eta>0, in its standard monomial derivative class. The auxiliary elementary inputs are the monotone first-derivative estimate and the second-derivative estimate. No Ivić large-values theorem, newer pointwise exponent, or weighted exponent-pair assertion is needed for (R1).

## 3. Proof and primary-source verification

### Precise source locations

I inspected the [Bourgain v2 primary text](https://arxiv.org/html/1408.5794v2). The relevant locations are Section 3, (3.1)--(3.2) and Theorem 4, (3.19); Section 4, the warning after (4.2); and [Section 5](https://arxiv.org/html/1408.5794v2#S6), (5.1), Theorem 6, items (a)--(b), and its final four paragraphs. Theorem 4 has the direct window 17/42<=log(M)/log(A)<=1/2. Theorem 6 supplies the global pair with M<=A. Its discussion treats longer lengths by rescaling and the B-process, and proper intervals by phase extension and the Sargos device with a logarithmic cost. The paragraph beginning with the model y x^(-s), s>0, identifies the requisite derivative class. Nonvanishing derivatives in (3.1) alone are insufficient.

These locations support the candidate's distinction between the two theorems. The primary paper's letter T denotes phase size; below it is renamed A to distinguish it from the campaign window T.

### Exact derivative class and normalization

Assume u>0. Set

\[
 M=2N,\qquad A=u\sqrt M,\qquad F(t)=\sqrt t,
 \qquad f(x)=A F(x/M)=u\sqrt x.
\]

The ambient source interval [M/2,M] is exactly [N,2N]. For every integer j>=1,

\[
 f^{(j)}(x)=u\prod_{h=0}^{j-1}(1/2-h)x^{1/2-j}.
\]

In particular f'(x)=(u/2)x^(-1/2): the monomial model is exact with s=1/2 and y=u/2. Every finite-order approximation error required by the standard class is zero. All normalized higher derivatives are bounded on [1/2,1]; moreover

\[
 |F''|\ge1/4,\quad |F'''|\ge3/8,\quad |F''''|\ge15/16.
\]

Thus one may choose, for example, a fixed lower derivative constant c=1/8. This stronger exact model verifies the global class, independently of merely checking (3.1). If the source's required finite differentiation order depends on eta, the same exact formula covers that order.

The source condition M<=A holds as soon as u>=sqrt(2N). Taking the candidate's unspecified fixed large constant to be C0=4 safely meets this and also makes y M^(-1/2)>1. The candidate's phase parameter u sqrt(N) differs from A by the fixed factor sqrt(2); it is not being identified with the length of a proper interval. The ambient length remains comparable to N regardless of J. The function u sqrt(x) itself supplies a global ambient extension, so no endpoint-dependent derivative constants arise. Half-open endpoint conventions change a source sum by at most two terms, harmless in (R1).

The global source gives, permitting an explicit logarithmic interval loss,

\[
 |S_J(u)|\ll_\eta \log(2M)\,(A/M)^{13/84+\eta}
                 M^{55/84+\eta}
 \ll_\eta\log(2M)A^\eta u^{13/84}N^{97/168}.       \tag{R2}
\]

Here 55/84-13/168=97/168. Using only Theorem 4 instead would require, up to fixed factors, M^(3/2)<=u<=M^(67/34), and would leave substantial frequency ranges untreated. No such restriction is inherited in (R2).

### Frequency regimes and integer derivatives

For definiteness choose c0=1/2 and C0=4; both are absolute constants.

If 0<u<=c0 sqrt(N), then f' is positive and decreasing, and

\[
 u/(2\sqrt{2N})\le f'(x)\le1/4.
\]

Its distance from every integer is at least u/(2 sqrt(2N)). The monotone first-derivative estimate yields

\[
 |S_J(u)|\ll\min(N,\sqrt N/u).                      \tag{R3}
\]

One can see the hypothesis directly from the successive phase increments: they are monotone and remain in [u/(2 sqrt(2N)),1/4]. Telescoping with the multiplier (1-e(f(n+1)-f(n)))^(-1) has total variation O(sqrt(N)/u). The final endpoint costs O(1), already included. As u tends to zero the trivial member of (R3) applies. A derivative merely being nonzero would not suffice; its separation from all integers is what is used here.

For every u>0, the exact second derivative obeys |f''(x)| asymp u N^(-3/2), with absolute comparison constants and constant sign. The ordinary second-derivative bound, on any interval of length at most N, is therefore

\[
 |S_J(u)|\ll u^{1/2}N^{1/4}+u^{-1/2}N^{3/4}.       \tag{R4}
\]

On c0 sqrt(N)<=u<=C0 sqrt(N), both terms are O(sqrt(N)). This is bounded by (R1), because u^(13/55)+u^(-1)>=1 for every positive u. At u>=C0 sqrt(N), the ratio of the second term to the first is sqrt(N)/u<=1/4, so the first term alone suffices. There is no condition on the distance of f' from integers in (R4). Thus every crossing of an integer derivative is allowed in the middle and high regimes.

### Interpolation and epsilon accounting

In the high regime (R2) and the reduced (R4) bound the same sum. If X and Y are these two bounds, min(X,Y)<=X^(42/55)Y^(13/55). Consequently the exponents of u and N are respectively

\[
 (42/55)(13/84)+(13/55)(1/2)=13/55,
\]
\[
 (42/55)(97/168)+(13/55)(1/4)=1/2.
\]

This is simply a geometric mean of valid nonnegative upper bounds. It assumes no interpolation theorem for weighted sums, and it does not replace an arithmetic coefficient vector by arbitrary weights inside (R2).

For completeness, the source loss is uniform in the campaign variables: A<=C sqrt(2) T^(7/4) and M<=2T^(3/2). Given the desired output epsilon, take source eta=epsilon/4 and use log(2M)<<_epsilon T^(epsilon/4). Then log(2M)A^eta<<_epsilon T^(11 epsilon/16), and raising that factor to 42/55 leaves a power strictly below T^epsilon. Fixed multiplicative constants are absorbed into the epsilon-dependent constant. Source thresholds for sufficiently large A and bounded N are covered by the trivial bound, since sqrt(N)(u^(13/55)+u^(-1))>=sqrt(N). This proves (R1) uniformly without an extra range assumption.

## 4. First doubtful or unproved step

**None within the assigned source/correlation seam.** In particular there is no missing interval between the first-derivative range and the legal global exponent-pair range. The global source is not inferred solely from Theorem 4 or from condition (3.1).

The next logically distinct interface is the candidate's finite-vector large-values argument and its complete reconstruction. Those arguments require their own reviews. This review does not infer them merely from (R1).

The original Ivić proof remains unavailable/unaudited as recorded in the permitted primary-source audit. That does **not** invalidate an independently derived distribution and moment bound whose complete proof uses (R1), the finite Gram argument, the actual coefficient norm, complete covering and tails, the accepted pointwise input, and a verified smoothing interface. Ivić is then not a dependency. Its unavailability does prevent representing an enlarged endpoint as a direct substitution into an audited original Ivić theorem. The candidate expressly claims an independent argument, so there is no source-provenance obstruction from Ivić within this seam.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact monomial class | PASS: s=1/2, y=u/2; all derivative approximation errors vanish. |
| Global versus local theorem | PASS: Theorem 6 is used; the direct Theorem-4 u-window is not imposed globally. |
| Phase versus interval length | PASS: M=2N, A=u sqrt(M); proper J keeps ambient M. |
| Proper intervals and real endpoints | PASS: the same exact extension works; logarithmic and O(1) endpoint costs are absorbed. |
| Tiny nonzero u | PASS: min(N,sqrt(N)/u), without falsely claiming cancellation at u=0. |
| Integer derivative crossing | PASS: f'=1 can occur when u is between 2 sqrt(N) and 2 sqrt(2N), inside the second-derivative regime; higher crossings use (R4)/(R2), never (R3). |
| Matching thresholds | PASS: c0=1/2, C0=4 produce complete overlapping coverage. |
| Large frequency | PASS: no extra upper bound beyond the stated polynomial range is needed; beyond u=N^(55/26), the target expression already dominates N. |
| Interpolation | PASS: weights sum to one and give u^(13/55)N^(1/2) exactly. |
| Epsilon and constants | PASS: A=O(T^(7/4)); fixed source constants, interval logarithm, and interpolation losses are paid explicitly. |
| Negative u and exact diagonal | PASS: conjugation for u<0; K_N(0)=#((N,2N] intersect Z) remains separate. |
| Arithmetic weights | PASS as scope: no weighted source theorem is asserted. |
| Singleton repair | Compatible with this seam: |e(u)|=1<=u^(13/55)+u^(-1), so it requires no new source theorem. |
| No parent overclaim | PASS: this review certifies only the source/correlation interface, not the frozen stronger distribution, pointwise improvement, M1/M2, or the quarter target. |

These are exact symbolic/analytical controls. No numerical experiment was run.

## 6. Dependencies and exact artifacts used

The only local reads were the assigned candidate, the two assigned source artifacts, and required protocol/state context:

- `protocol.md`, SHA256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `state/proof_obligations.yml`, SHA256 `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`; relevant nodes include the accepted Bourgain source interface, accepted repaired Li--Yang exponent, open GC target, and physical absolute-majorant obstruction.
- `state/active_campaign.yml`, SHA256 `16d73bb9523c77fd58f1aaffdef50ba0435509cdd00ab0546cbc7cca2c7502c2`, Round 204.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, final reviewed SHA256 `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
- `sources/bourgain_2017_exponent_pair.md`, SHA256 `a2b13364b738457889546d0a52c027358d7eb450bebd4272a612d70f5e917361`.
- `rounds/codex-managed/gc-complete-large-values-duality/reports/large_values_primary_source_audit.md`, SHA256 `15685e292a53f27caf543b6276628964699b751fde66bee9d917b7dfcc275e86`.

The primary web text was Bourgain arXiv:1408.5794v2, with exact locations given in Section 3. No broad literature review, additional Ivić access attempt, sibling review, or successor-round work was undertaken. Only this assigned review file was written.

## 7. Recommended state effect

**Retain** the accepted global Bourgain dependency. **Promote the source/correlation seam to GREEN** for candidate SHA256 `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`, subject to the conductor's graph and State Patch process. No source-seam correction is required.

Full-kernel acceptance must still depend on the other assigned reviews and the mechanically valid State Patch. This bounded review supplies no independent promotion of the frozen distribution target, a new pointwise exponent, M1/M2/M9, or the quarter theorem. It does not update authoritative state or open a new round.
