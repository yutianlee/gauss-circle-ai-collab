# Round 214: isolated conditional radius-certificate optimization

## 1. Result: conditional lemma and certificate limitation

- Campaign: `gc-full-goal-radius-source-review`; round: 214.
- Task and role: `blind_radius_optimization`; statement-only independent rederivation.
- Supplied graph hash: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
- Generated: 2026-09-27 17:06:38 UTC (2026-09-28 Asia/Shanghai).
- Context read: only `protocol.md` and `rounds/codex-managed/gc-full-goal-radius-source-review/briefs/blind_radius_optimization_statement.md`.
- Analytical work only; no experiments, web sources, graph inspection, or other reports.

Under the hypothetical radius input in the statement, the complete power-level fourth-power certificate for D>1 is

\[
 |F|^4\ll_\varepsilon T^\varepsilon E_0(L,K),\qquad
 E_0=\frac N{L^2}+\frac NK+\frac ND+\sqrt{ND},\qquad
 D=\frac{TLK}{N^{3/2}}.
\]

Combining all allowed lengths with the two elementary caps gives the uniform conditional bound

\[
 |F|\ll_\varepsilon T^{1/8+\varepsilon}.
\]

Free length optimization does not improve this uniform power. At the exact integer scales T=m^4, N=m^3, every certificate E_0 is at least T^{1/2}; neither cap gives a power below T^{1/8}. This is a lower bound for the displayed certificate, **not** a lower bound for F and not a proof that other uses of the shell data cannot do better.

For the formal replacement sqrt(N) -> sqrt(N)q^{-sigma}, 0<=sigma<=1, the target-power lengths in the packet certify |F|<=T^{b+epsilon}, for fixed 0<b<1/6, precisely at the power level when

\[
 1-\sigma\le b(8-6\sigma),
 \qquad\text{equivalently}\qquad
 b\ge\frac{1-\sigma}{8-6\sigma}.
\]

Thus approaching b=0 requires sigma to approach 1. Nothing here proves the arithmetic input for sigma=0 or for any stronger sigma, or extends its range of admissible lengths.

## 2. Exact statement and hypotheses

Use all definitions, caps, finite-difference inequalities, normalized costs, shell fractions, and paid radius transfer in the isolated statement. In particular, the normalized shell decomposition is used in its averaging sense:

\[
 A_{4,\mathrm{res}}
 \le \sum_j\delta_j\sup_R\operatorname{shellRMS}_j(R).
\]

All non-residual costs, including repeated shifts, hk<=U, and the supplied smooth-model contribution, have already been paid by

\[
 T^\varepsilon\left(\frac NK+\frac ND\right).
\]

The residual indices have q=2^j>=1 and q<=D. No lower bound on any delta_j or any actual shell norm is assumed. Let

\[
 H=\log(2L),\qquad J=1+\lfloor\log_2D\rfloor\quad(D>1).
\]

Constants may depend on the fixed c, a fixed b when target lengths are used, B>1, and epsilon. The input Q_j is assumed only at the lengths actually used in an assertion. In particular:

1. A fixed-length certificate requires the input at that fixed pair (L,K).
2. The optimized bound over lengths is conditional on its availability at the selected optimizing pairs.
3. The target-power comparison only requires it at the rounded target-power pairs.

The statement's elementary caps are used for D<=1 and bounded N. There is no claim that an arithmetic estimate available on some unspecified or narrower length family automatically applies to the pairs selected below.

## 3. Proof and derivation

### Complete shell summation, including the localization remainder

For sigma=0 the paid radius transfer and hypothetical input give

\[
 \sup_R\operatorname{shellRMS}_j
 \ll_\varepsilon
 T^\varepsilon\left(\sqrt{Nq}+\frac Nq+Nq^{-B}\right).
\]

Because q<=D and sum(delta_j)<=1,

\[
 \sum_j\delta_j\sqrt q\le\sqrt D.
\]

The shell-fraction bound gives the other two estimates:

\[
 \sum_j\frac{\delta_j}{q}
 \le\frac{CH}{D}\sum_{j:q\le D}1
 \le\frac{CHJ}{D},
\]

\[
 \sum_j\delta_jq^{-B}
 \le\frac{CH}{D}\sum_{j\ge0}2^{j(1-B)}
 =\frac{CH}{D(1-2^{1-B})}.
\]

Thus a certificate retaining the logarithmic costs explicitly is

\[
 |F|^4\ll_\varepsilon T^\varepsilon
 \left[
 \frac N{L^2}+\frac NK+\frac ND
 +\sqrt{ND}+\frac{NHJ}{D}+C_B\frac{NH}{D}
 \right].                                      \tag{1}
\]

Here the N/K cost in A4 has been combined with the already displayed N/K term. Since L,K<=cN and N<=T,

\[
 D\le c^2T N^{1/2}\le c^2T^{3/2},\qquad
 H,J\ll_c1+\log T.
\]

For every eta>0, (1+log T)^2<=C_eta T^eta. Allocate the input and transfer epsilon losses smaller than the final requested loss; then (1) gives E_0 exactly at power level. The arbitrary fixed B>1 is sufficient: its localization tail is absorbed by N/D with one logarithm. It leaves no extra power of N or T.

### A direct target-power choice

Fix 0<b<1/6. The first cap handles N<=T^{4b}, and the second handles N>=T^{1-2b}. In the intervening band put

\[
 x=\sqrt N\,T^{-2b}>1,\qquad
 L=\lceil2x\rceil,\quad K=\lceil4x^2\rceil.
\]

Then 2<=L<=K, L is comparable with x, K with x^2, and

\[
 K\le5NT^{-4b}\le cN
\]

for all sufficiently large T depending on b,c. The finitely bounded remaining T range can be absorbed into the implicit constant. Consequently

\[
 D\asymp T^{1-6b}>1,\qquad
 \frac N{L^2}+\frac NK+\frac ND\ll T^{4b}.
\]

For sigma=0, the remaining term satisfies

\[
 \sqrt{ND}\ll
 T^{(1-2b)/2+(1-6b)/2}=T^{1-4b}.
\]

It is at most T^{4b} precisely when b>=1/8. Choosing b=1/8 proves the uniform conditional bound, with all length and rounding requirements satisfied.

### Free length optimization and the exact certificate obstruction

Write E=E_0(L,K)>0. Independently of the allowed-length restrictions,

\[
 \frac N{L^2}\le E,\quad\frac NK\le E
 \quad\Longrightarrow\quad
 LK\ge\frac{N^{3/2}}{E^{3/2}},\quad D\ge\frac T{E^{3/2}}.
\]

Combining this with sqrt(ND)<=E gives

\[
 E\ge(NT)^{2/7}.                               \tag{2}
\]

Also, N/D<=E and sqrt(ND)<=E imply

\[
 \frac NE\le D\le\frac{E^2}N,
 \qquad E\ge N^{2/3}.                          \tag{3}
\]

For T^{2/5}<=N<=T^{3/4}, let

\[
 Y=(NT)^{2/7},\quad \ell=\sqrt{N/Y}\ge1,
 \quad L=\lceil2\ell\rceil,\quad K=\lceil4\ell^2\rceil.
\]

These pairs are allowed for large T, because K<=5N/Y<=cN. They yield

\[
 D\asymp\frac T{Y^{3/2}},\quad
 \frac N{L^2}+\frac NK\ll Y,\quad
 \sqrt{ND}\asymp Y,\quad
 \frac ND\asymp\frac{NY^{3/2}}T\le Y.
\]

The last inequality is exactly N<=T^{3/4}. This achieves (2) at power level on the entire interval where it improves both elementary caps. For N<=T^{2/5}, the first cap is already no larger than the fourth root of the lower bound (2). For N>=T^{3/4}, the second cap is no larger than the fourth root of the lower bound (3).

For completeness, the formal optimum E of order N^{2/3} above T^{3/4} is also attainable: take lengths comparable to

\[
 L=N^{1/6},\qquad K=N^{5/3}/T.
\]

Here K>=N^{1/3}>=L, K/N<=T^{-1/3}, and the rounded lengths are allowed for large T. They give D comparable to N^{1/3}; all four terms are O(N^{2/3}). This optimization is unnecessary for the final bound because the second cap is stronger there.

In terms of N=T^n, the optimized combined certificate has the power envelope

\[
 g(n)=
 \begin{cases}
 n/4,&0\le n\le2/5,\\
 (n+1)/14,&2/5\le n\le3/4,\\
 (1-n)/2,&3/4\le n\le1.
 \end{cases}                                  \tag{4}
\]

Equivalently its displayed magnitudes, up to epsilon loss, are N^{1/4}, (NT)^{1/14}, and (T/N)^{1/2} on the respective intervals. This describes optimization of these available certificates, not the size of the actual sums. The maximum of g is 1/8 at n=3/4.

In particular, take integers m tending to infinity and set T=m^4, N=m^3. For every pair with D>1, (2) gives E>=m^2=T^{1/2}; the logarithm-retaining certificate (1) cannot improve its power. The elementary caps have magnitudes m^{3/4} and m^{1/2}. For D<=1 the stipulated fallback consists of those caps and likewise supplies no smaller power. Hence no selection of the allowed lengths followed by these certificates supplies a uniform power below T^{1/8}. This is an exact-scale certificate limitation.

### Formal frequency-decay comparison

Set a=1/2-sigma, so -1/2<=a<=1/2. The changed paid contribution is

\[
 T^\varepsilon\sqrt N\sum_j\delta_jq^a.
\]

If a>=0, the sum is at most D^a. If a<0, using only sum(delta_j)<=1 would lose the essential frequency decay. Instead use the full fractions:

\[
 \sum_j\delta_jq^a
 \le\frac{CH}{D}\sum_{2^j\le D}2^{j(1+a)}
 \le\frac{CH}{1-2^{-(1+a)}}D^a
 \ll H D^a.                                   \tag{5}
\]

The constant is bounded throughout the stated sigma interval because 1+a>=1/2. There is also the trivial upper bound 1 when a<0; (5) is the useful estimate when D is a growing power. After absorbing logarithms the changed certificate is

\[
 E_\sigma=
 \frac N{L^2}+\frac NK+\frac ND
 +\sqrt N D^{1/2-\sigma}.                      \tag{6}
\]

For the rounded target-power lengths, D is comparable to T^{1-6b}. The last term is increasing with N and has supremal band exponent

\[
 r(b,\sigma)
 =\frac{1-2b}{2}+(1/2-\sigma)(1-6b)
 =1-\sigma-4b+6b\sigma.
\]

Thus (6), with the caps outside the band, gives the target precisely when

\[
 r(b,\sigma)\le4b
 \iff 1-\sigma\le b(8-6\sigma)
 \iff \sigma\ge\frac{1-8b}{1-6b}.             \tag{7}
\]

Here “precisely” refers to the power comparison in (6). To check necessity within that comparison despite the cap at the upper endpoint, suppose r>4b. Choose a fixed positive eta smaller than both 1-6b and 2(r-4b), and put N=T^{1-2b-eta}. Then N lies strictly inside the band, both cap powers are strictly greater than b, and the radius-term exponent remains r-eta/2>4b. Hence the displayed certificates fail to supply the claimed uniform target. This argument does not refute a bound for the actual F.

For b<1/8, condition (7) can also be written

\[
 1-\sigma\le\frac{2b}{1-6b}.
\]

Therefore sigma must tend to 1 as b tends to zero; for fixed sigma<1 there remains the positive threshold (1-sigma)/(8-6sigma). At sigma=1 every fixed positive b<1/6 passes this formal comparison. This limiting statement does not permit setting b=0 in the rounded-length proof or assume constants uniform as b tends to zero.

### Consequences for the physical discrepancy

Under the additional assembly stipulated in the packet, a physical discrepancy is bounded by T^{1/2} times logarithmically many such blocks, plus target-safe complementary errors. A uniform block power b then gives

\[
 P(T^2)\ll_\varepsilon T^{1/2+b+\varepsilon},
 \qquad P(X)\ll_\varepsilon X^{1/4+b/2+\varepsilon}.
\]

The original hypothetical input therefore gives the conditional milestone X^{5/16+epsilon}, not the full X^{1/4+epsilon} target. To reach the full quarter through this formal comparison, one would need the stronger arithmetic input at the required lengths with (7) available for arbitrarily small fixed b (for example sigma=1), as well as the stipulated assembly and error controls. The algebra does not establish those arithmetic or assembly hypotheses.

## 4. First doubtful or unproved step

The first unproved mathematical input is the stated uniform arithmetic radius estimate Q_j. It was assumed, not derived. The stronger frequency-decay version is a further hypothetical estimate whose feasibility is not established here. Applicability at the selected optimizing or target-power lengths is a separate hypothesis and cannot be inferred from the algebra.

No doubtful algebraic step remains within the supplied normalized shell interface. The exact-scale lower bound concerns E_0 only. For example, the supplied upper constraints allow all residual fractions to vanish; they cannot furnish a positive actual lower bound on F. Extra knowledge of actual fractions, cancellation, or a stronger estimate could improve the certificate and is outside this limitation.

## 5. Required control tests and outcomes

All controls were analytic; no numerical experiment was used.

1. **Complete-cost control — pass.** Repeated shifts and hk<=U supply N/K+N/D; the q^{-1} term contributes NHJ/D; the paid q^{-B} remainder contributes O_B(NH/D). No leftover localization power was discarded.
2. **Length and endpoint control — pass.** Explicit ceilings give 2<=L<=K<=cN on every selected growing-T band; the constants may depend on fixed b,c. Bounded T and bounded N are absorbed by the caps. The cases D<=1 use only their specified fallback.
3. **Exact obstruction control — pass.** At T=m^4,N=m^3 the positive-term inequalities force E_0>=m^2, while the better cap is m^{1/2}. This independently matches the b=1/8 construction.
4. **Decreasing-weight control — pass.** Equation (5) uses the actual shell-fraction bound for sigma>1/2. Replacing it by a mere sum(delta_j)<=1 would incorrectly erase D^{1/2-sigma}.
5. **Special-sigma control — pass.** Sigma=0 gives b>=1/8; sigma=1/2 gives b>=1/10; sigma=1 gives no positive algebraic lower threshold on b. All agree with direct substitution into (6).
6. **Logical lower-bound control — pass.** The obstruction is stated for the optimized upper certificate; no lower bound or impossibility theorem about actual arithmetic F is inferred.
7. **Physical normalization control — pass.** T^{1/2+b} at X=T^2 is X^{1/4+b/2}; b=1/8 is exactly 5/16, not 1/4.

## 6. Dependencies and exact artifacts used

1. `protocol.md`: round discipline, state ownership, analytical controls, and distinction between candidate evidence and accepted mathematics.
2. `rounds/codex-managed/gc-full-goal-radius-source-review/briefs/blind_radius_optimization_statement.md`: every mathematical hypothesis, the allowed length range, shell normalization and radius-transfer interface, the hypothetical input, caps, and physical normalization.

The graph hash above is metadata supplied by the isolated packet; the graph was not opened or independently hashed. No graph, manifest, strategy, general generated brief, prior report, sibling report, conductor artifact, or web source was read. The sole written artifact is this report.

## 7. Recommended state effect

**Retain** the arithmetic radius inputs as hypothetical and unproved. Subject to the conductor's required independent seam checks and graph validation, **promote only the conditional certificate algebra and its exact-scale optimization limitation** as mathematical consequences of the explicitly stated interface.

Do not promote an unconditional block estimate, a radius arithmetic theorem, a full-quarter discrepancy bound, or a claim that actual F must attain the certificate's lower-bound scale. Free lengths improve some individual block certificates but leave the uniform original-input exponent at 1/8. The formal sigma comparison records the strength of input this route would require; it is not evidence that such input is feasible.

This assigned task stops with this report and selects no successor round.
