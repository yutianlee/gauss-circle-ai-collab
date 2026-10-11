# Round 214: independent NONBLIND radius-power seam review

## 1. Result

**GREEN. No mathematical correction required in the reviewed scope.**

- Campaign: `gc-full-goal-radius-source-review`; round: 214.
- Role: independent NONBLIND seam review, following a completed statement-only derivation.
- Generated: 2026-09-27 17:11:16 UTC.
- Reviewed artifact: `rounds/codex-managed/gc-full-goal-radius-source-review/controls/conductor_radius_power_ledger.md`.
- Exact reviewed SHA256: `c4bb7f561e468d271b9487ed10057feb739e8e2c0c52b7dffadfe6ed712bae20`.
- The filesystem SHA256 was checked and matched the assigned immutable review hash.
- Supplied graph metadata: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`; the graph was not opened.

The complete positive certificate, its optimized uniform exponent 1/8, its cap-combined pointwise envelope, the formal sigma condition, and the physical exponent 5/16 are correct consequences of the isolated packet. The ledger correctly limits the obstruction to its explicit certificate and caps. It does not establish or silently extend the hypothetical arithmetic radius estimate.

## 2. Exact statement and hypotheses reviewed

The reviewed claims are the following, under exactly the isolated packet's normalized decomposition, paid radius transfer, hypothetical radius input at the selected lengths, and elementary caps:

\[
 E=\frac N{L^2}+\frac NK+\frac ND+\sqrt{ND},\qquad
 D=\frac{TLK}{N^{3/2}},\qquad 2\le L\le K\le cN.
\]

For D>1 this is an upper certificate for |F|^4 up to arbitrary epsilon losses. For D<=1 the specified method uses the elementary caps. Optimizing the resulting positive expressions gives uniform block power 1/8 and the envelope stated in ledger section 3.C. Replacing only the first arithmetic-input term by sqrt(N)q^{-sigma} gives the target-power condition

\[
 1-\sigma\le b(8-6\sigma),\qquad
 0<b<1/6,\quad 0\le\sigma\le1.
\]

The physical interpretation additionally assumes the reconstruction and complementary-error hypotheses stated in the packet. This review does not certify the arithmetic input, reconstruction from unprovided source artifacts, provenance claims about when the conductor performed a derivation, or the status of other research routes named for context. None of those claims is needed for the algebraic conclusions reviewed here.

## 3. Proof and seam audit

### Shell fractions, tails, and logarithms: ledger section 3.A — GREEN

The paid transfer produces sqrt(Nq)+N/q plus Nq^{-B}, up to the assigned epsilon factors. For H=log(2L), the exact available estimates are

\[
 \sum\delta_q\sqrt q\le\sqrt D,
 \qquad \sum\frac{\delta_q}{q}
 \ll\frac{H(1+\lfloor\log_2D\rfloor)}D,
\]

\[
 \sum\delta_q Nq^{-B}
 \ll\frac{NH}{D}\sum_{j\ge0}2^{j(1-B)}
 \ll_B\frac{NH}D.
\]

These are the ledger's estimates. Its rewriting of the packet's individual fraction bound as min(1,CqH/D) is valid: nonnegativity and sum(delta_q)<=1 give delta_q<=1 separately. The repeated-shift and smooth-model costs N/K+N/D are included. Since L<=cT and D<=c^2 T^{3/2}, all retained logarithms are O_c(1+log T); their products can be absorbed into any prescribed positive epsilon loss. The ledger therefore discards no power-bearing tail or normalization factor.

### Integer target lengths and cap ranges: ledger sections 3.B and 3.D — GREEN

On N>T^{4b}, put x=sqrt(N)T^{-2b}>1. The ledger uses

\[
 L=\max(2,\lceil x\rceil),\qquad
 K=\max(2,\lceil x^2\rceil).
\]

Monotonicity of the ceiling function gives L<=K. The lengths are comparable to x,x^2 even at the lower endpoint, and

\[
 K\le2x^2=2NT^{-4b}\le cN
\]

for sufficiently large T depending only on fixed b,c. Hence D is comparable to T^{1-6b}. Small T can be paid by enlarging constants, because then the full 1<=N<=T interval is bounded. The first cap handles N<=T^{4b}, the second N>=T^{1-2b}. The fixed choice b=1/8 yields exactly the ranges and costs in section 3.B. Equality endpoints need no limiting assumption.

### Free lengths and pointwise envelope: ledger section 3.C — GREEN

The certificate implications

\[
 L\ge\sqrt{N/E},\quad K\ge N/E,
 \quad D\ge T E^{-3/2},\quad E\ge\sqrt{ND}
\]

give E>= (NT)^{2/7}. All directions of inequality are correct.

For fixed S=LK, balancing the diagonal terms at K=L^2 gives their common order N/S^{2/3}; constants from minimizing their sum do not affect any exponent. The radius term is T^{1/2}N^{-1/4}S^{1/2}. Their balance gives S=N^{15/14}T^{-3/7} and E of order (NT)^{2/7}. The remaining cost N/D=N^{5/2}/(TS) becomes N^{10/7}T^{-4/7}, and is no larger than (NT)^{2/7} exactly when N<=T^{3/4}.

The resulting L=N^{5/14}T^{-1/7} and K=N^{5/7}T^{-2/7} satisfy L>=1 and K>=L once N>=T^{2/5}. Applying max(2,ceil(...)) preserves comparability, ordering, and the cN upper limit for large T. Thus the middle envelope is attained throughout its closed power interval, including the constant-length lower endpoint.

The ledger's use of the single lower bound E^{1/4}>=(NT)^{1/14} is sufficient to prove optimality of the entire combined envelope. With N=T^alpha:

- For alpha<=2/5, (alpha+1)/14>=alpha/4, so the first cap cannot be improved by the certificate; the second cap is also no smaller.
- For 2/5<=alpha<=3/4, both cap exponents are at least (alpha+1)/14, and the constructed lengths attain that exponent.
- For alpha>=3/4, (alpha+1)/14>=(1-alpha)/2, so the second cap cannot be improved by the certificate; the first cap is also no smaller.

Pairs with D<=1 add only the caps by hypothesis and therefore do not invalidate these comparisons. The maximum combined power is 1/8 at alpha=3/4.

### Exact-scale scope: ledger sections 2 and 3.C — GREEN

The stated rounded limiting scale can, if desired, be realized exactly by T=m^4,N=m^3 for integers m tending to infinity. Then E>=m^2, the first cap is m^{3/4}, and the second cap is m^{1/2}. This proves a uniform power limitation of the displayed expressions.

It proves no positive lower bound for an actual block sum: the shell data and the arithmetic input are upper bounds. The ledger expressly states this distinction in sections 1, 2, 3.C, 3.D, and 5. It also avoids asserting that every allowed shell family saturates the upper moments. There is no converse inference hidden in the word “optimum.”

### Formal sigma condition and arithmetic scope: ledger sections 3.D and 4 — GREEN

For r=1/2-sigma in [-1/2,1/2], the displayed weighted shell bound is valid. When r>=0, sum(delta_q)<=1 gives D^r, which is no larger than a constant times H D^r because L>=2. When r<0,

\[
 \sum\delta_q q^r
 \ll \frac HD\sum_{2^j\le D}2^{j(1+r)}
 \ll H D^r,
\]

uniformly over the stated r interval because 1+r>=1/2. Thus the negative-power case uses the shell fractions correctly.

At the target lengths, the changed term is sqrt(N)D^{1/2-sigma} and has supremal band power 1-sigma-4b+6b sigma. Comparing with 4b gives exactly the ledger's condition. If the condition fails strictly, choose alpha=1-2b-eta with fixed

\[
 0<\eta<\min(1-6b,\,2[1-\sigma-8b+6b\sigma]).
\]

Then alpha>4b, so both caps have powers strictly above b; the changed certificate term still has power strictly above 4b. This confirms the ledger's necessity statement within its positive certificate, including the role of the complementary caps.

At sigma=0,1/2,1 the thresholds are 1/8,1/10,0. For b tending to zero, the necessary relation is sigma tending to 1; a fixed sigma<1 leaves a positive threshold. The ledger keeps b strictly positive in the length construction and treats sigma=1,b tending to zero only as a formal limit. It does not assume constants uniform in b.

The explicit qualifications in sections 1, 2, 3.B, 3.D, and 4 prevent a silent extension in length or sigma. In particular, the ledger says that an arithmetic result restricted to the original fixed-b range would not justify the b=1/8 optimization. The arithmetic theorem itself remains unproved; the review certifies only the stated conditional algebra.

### Physical normalization: ledger section 3.E — GREEN

The stipulated reconstruction multiplies the block scale by T^{1/2} and logarithmically many blocks. Thus b produces T^{1/2+b+epsilon}=X^{1/4+b/2+epsilon}, with X=T^2 and epsilon relabeled. The b=1/8 certificate gives X^{5/16+epsilon}. It is a conditional milestone and does not close X^{1/4+epsilon}. No quarter-power conclusion is inferred merely from a fixed-b radius estimate.

## 4. First doubtful or unproved step

No doubtful algebraic step was found in the reviewed seams. The first unproved arithmetic step remains the uniform radius input, including its exact admissible range in L,K and, for the formal comparison, its stronger q^{-sigma} factor. The ledger accurately retains that gap.

The specified physical reconstruction is an additional conditional dependency. Since the assignment permits only the packet, the completed isolated report, the protocol, and this ledger, this review does not independently validate reconstruction or contextual research-state assertions from the unprovided historical dependencies. The conditional normalization itself is correct and needs no correction.

## 5. Required controls and outcomes

1. **Hash control — PASS.** SHA256 of the reviewed ledger exactly matches `c4bb7f561e468d271b9487ed10057feb739e8e2c0c52b7dffadfe6ed712bae20`.
2. **Complete shell and localization control — PASS.** The q^{-1} part costs NH log(2D)/D; the fixed-B>1 tail costs O_B(NH/D); logs are bounded by powers of log T.
3. **Length, integer, and cap control — PASS.** Explicit max-and-ceiling pairs satisfy 2<=L<=K<=cN for large T on the stated bands; caps cover the complementary regions and bounded cases.
4. **Free optimization control — PASS.** The balanced lengths attain the middle envelope, and E>=(NT)^{2/7} with both caps proves all three intervals are optimal for these expressions.
5. **Exact obstruction and logical scope control — PASS.** T=m^4,N=m^3 is an exact integer realization. The lower bound is for E, never for actual F.
6. **Sigma and decreasing-power control — PASS.** Shell fractions retain D^{1/2-sigma}; the three special values and an interior-band strict-failure test agree.
7. **Arithmetic scope and physical normalization control — PASS.** Length extensions and stronger input remain explicit hypotheses; T^{1/2} and X=T^2 give 5/16 rather than the quarter target.

No numerical or symbolic-computation experiment was needed. This was an analytical seam review.

## 6. Dependencies and exact artifacts used

- `protocol.md`.
- `rounds/codex-managed/gc-full-goal-radius-source-review/briefs/blind_radius_optimization_statement.md`.
- The completed isolated derivation `rounds/codex-managed/gc-full-goal-radius-source-review/reports/blind_radius_optimization.md`, already available from this reviewer's preceding assigned task and left unchanged.
- The exact pinned ledger `rounds/codex-managed/gc-full-goal-radius-source-review/controls/conductor_radius_power_ledger.md`, SHA256 `c4bb7f561e468d271b9487ed10057feb739e8e2c0c52b7dffadfe6ed712bae20`.

No sibling report, graph, manifest, strategy, historical dependency, next-round artifact, or web source was opened for this review. No claim of independent documentary validation of those unread sources is made. The only newly written file is this review.

## 7. Recommended state effect

**GREEN for the independent final-hash review gate of this conditional power ledger.** Retain the arithmetic radius estimate, stronger frequency input, and full-quarter goal as unproved. The reviewed artifact may be recorded as conditional strategy and certificate-limit evidence, subject to the conductor's remaining validation and state rules.

There are no required corrections to the pinned ledger within this audit. This review does not authorize any unconditional promotion or expansion of arithmetic hypothesis scope. The assigned review stops here and does not open a successor round.
