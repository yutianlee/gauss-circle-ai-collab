# Polynomial additive twists of the actual norm coefficients: source admission audit

Round231 prelaunch admission evidence; task `quadratic_source_audit`; source auditor, 2026-10-11. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. The active authoritative campaign remains closed Round230. This report is not a State Patch or an accepted new estimate.

## 1. Result

A directly relevant source exists: Proposition A.3 of Matomäki–Shao–Tao–Teräväinen's *Higher uniformity I* supplies a **power saving for the actual difference `r2-r2sharp` against arbitrary fixed-degree polynomial additive phases**, in every sufficiently long short interval. It is neither a multiplicative quadratic-character theorem nor merely a logarithmic estimate. Its approximant is an explicit, signed divisor sum. The source therefore passes the actual-coefficient and moving-polynomial tests.

It does **not** presently pass the complete-bound admission gate. Quadratic patches at `N~T^(2/3)` meet only the excluded length boundary. That particular obstruction disappears for quartic Taylor patches above the affordable norm head `T^(52/125)`. The full signed approximant can also be paid, using monotonicity of the patch cutoffs and the inherited exponent pair; its pointwise exponent is `13/125-13/52500`. The remaining source exponent is only an unspecified positive constant and supplies no certified saving large enough for the complete residual restoration. No better complete moment, pointwise exponent, or final theorem follows.

The almost-all sequel does not repair these gaps by direct application: its very-short-interval polynomial result is stated for `d_k`, has a qualitative error relative to the divisor mean, and retains an exceptional set of interval starts. An `r2` extension and a quantitative payment of all exceptional intervals would be additional work, not source conclusions. This is a bounded negative admission result, not a no-go theorem for polynomial methods.

## 2. Exact hypotheses and source cards

Use `rho,Psi,w,B_T,M_p,beta` exactly as in the assigned complete interface. Thus `R~T`, `a_n=r2(n)n^(-3/4)Psi(sqrt(n/T))`, the accepted moment exponent is `10 beta`, and the preferred complete target is `29/25`. The actual full-wave supremum does not automatically hold for either piece of a new decomposition.

**Source A.** Kaisa Matomäki, Xuancheng Shao, Terence Tao, Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, [arXiv:2204.03754v4](https://arxiv.org/html/2204.03754v4), dated 2024-02-28; initial submission 2022-04-07; Forum of Mathematics, Pi 11 (2023), e29, [DOI](https://doi.org/10.1017/fmp.2023.28). The abstract record describes v4 as including a small Proposition 2.14 proof repair. Audited application: Proposition A.3 together with Theorem 1.1(iii), equation (1.7), and Appendix A.3's approximant. For fixed degree `d` and `epsilon0>0`,

\[
 x^{1/3+\epsilon_0}\le H\le x^{1-\epsilon_0},\qquad
 \sup_{\deg P\le d}\left|\sum_{x<n\le x+H}
 (r_2(n)-r_{2,x}^{\sharp}(n))e(P(n))\right|^*
 \ll_{d,\epsilon_0}H x^{-c_{2,d,1}\epsilon_0},\quad c_{2,d,1}>0. \tag{A}
\]

The star permits every arithmetic-progression subsum, hence prefixes. The circle nilmanifold has fixed complexity; polynomial coefficients are unrestricted. With `z=x^(1/20)`, the approximant is

\[
r_{2,x}^{\sharp}(n)=4\sum_{\substack{z\le m<z^2\\m\mid n}}
\chi_4(m)\frac{\log n-2\log z}{\log z}
+4\sum_{\substack{m<z\\m\mid n}}[\chi_4(m)+\chi_4(n/m)]. \tag{Asharp}
\]

No explicit numerical lower bound for `c_(2,d,1)` is stated. No exceptional set occurs in (A).

**Source B.** Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, [arXiv:2411.05770v2](https://arxiv.org/html/2411.05770v2), dated 2026-01-23; initial submission 2024-11-08. The [current abstract record](https://arxiv.org/abs/2411.05770) identifies v2 as incorporating referee comments. Audited application: Theorem 1.1(v), with a fixed-degree polynomial phase on the circle. For `x in [N,2N]`, `N^epsilon0<=H<=N^(1-epsilon0)`, every fixed `eta,A>0` gives

\[
 \sup_{\deg P\le d}\left|\sum_{x<n\le x+H}
 (d_k(n)-d_k^\sharp(n))e(P(n))\right|^*
 \le\eta H\log^{k-1}N
\]

outside a set of measure `O_(d,epsilon0,eta,A)(N log^(-A)N)`. This states `d_k`, not `r2`. Theorem 1.8 was screened only: it concerns fixed linear phases, not the moving quadratic phases required here; no third application audit was made.

These are two applications within one higher-uniformity source family. No retired Lamzouri, Zhai, Li–Yang, or toric-family audit was repeated. Search coverage is bounded, not exhaustive.

## 3. Derivation and full restoration

### The phase, length, and denominator audit

Choose shell patches and their centers `x_j~N` independently of `R`. Let `P_(j,d,R)` be the degree-`d` Taylor polynomial of `R sqrt(x)` at `x_j`. Its coefficients depend on the real radius, which (A) allows. For `H<=cN`, direct differentiation gives

\[
 \int_{I_j}|(R\sqrt x-P_{j,d,R}(x))'|dx
 \ll T N^{-d-1/2}H^{d+1}.
\]

Thus bounded variation is obtained at

\[
 H_d=c_0 N^{1-1/(2(d+1))}T^{-1/(d+1)}. \tag{3.1}
\]

The exact residual exponential is kept in the amplitude; no Taylor remainder is discarded. The weight and its variation cost
`O_L(N^(-3/4)(1+N/T)^(-L))`. Source (A) bounds prefix sums, so Abel summation applies with this exact amplitude. At a final partial patch, use its progression restriction inside a full source interval; do not demand a new short-interval theorem at the shortened length.

For `N=T^sigma`, (3.1) exceeds `N^(1/3+epsilon0)` with a power margin precisely when

\[
 \sigma>\frac{6}{4d+1-6(d+1)\epsilon_0}. \tag{3.2}
\]

For `d=2`, the limiting threshold is `2/3`. At `N~T^(2/3)`, `H_2~N^(1/3)` misses every fixed positive margin. For `N~T`, `H_2~N^(1/2)` does fit. This is the first failed premise of the direct quadratic application on the complete complement; many atoms per patch do not by themselves meet (A).

There is no required Diophantine denominator in (A): `g(n)=P(n) mod 1` carries arbitrary real polynomial coefficients and the fixed test `e(t)` has fixed Lipschitz norm. Discretizing the coefficients into rational modes would create a separate summation cost; it is unnecessary for this source application and supplies no automatic gain.

### Bounded quartic repair and residual restoration

Take `d=4`, `sigma0=52/125`, and the fixed source margin `epsilon0=1/25`. At the first retained shell,

\[
 \log_N H_4=\frac9{10}-\frac1{5\sigma_0}
 =\frac{109}{260}=\frac13+\frac{67}{780}
 >\frac13+\frac1{25}.
\]

The lower inequality remains valid as `N` increases. Up to `N=T^(3/2)`, the upper exponent is at most `23/30<1-1/25`. Fixed patch-size constants are absorbed by the strict margins for large `T`. Bounded `T` and the finitely many small norms are paid by constants. Consequently Source A really applies on every quartic patch of the retained complement. This repairs the length seam; it proves no cancellation of the main owner.

For each patch use its own base `l_j` in (Asharp), and define exactly

\[
 r_2(n)=r_{2,l_j}^{\sharp}(n)+v_j(n),\quad n\in I_j.
\]

Do not silently substitute a common cutoff into the source theorem. Both coefficient vectors are independent of `R` and satisfy `|r2sharp|+|v_j|<<d(n)` on the ambient shell: the logarithmic ratio in (Asharp) is bounded and every divisor sum is bounded by a fixed multiple of `d(n)`. The total shell has `O(N/H_4)` patches. Set `kappa=c_(2,4,1)/25`; after decreasing it if necessary assume `0<kappa<1/4`. Summing the valid source residual estimates gives

\[
 |V_N(R)|\ll_L (1+N/T)^{-L}N^{1/4-\kappa}. \tag{3.3}
\]

This is a new applicable component estimate, conditional only on the cited external theorem as audited. It is not a complete arithmetic-wave estimate. The constant and `kappa` are fixed, independent of `T,R,N`; no growth of degree or inverse source margin with `T` is used.

Let `V` be the real cosine wave formed from all residual coefficients between `X=T^(52/125)` and `T^(3/2)`, and let `Ssharp` be the corresponding complete real approximant wave with the same patch choices and endpoints. Then the exact decomposition is

\[
 B_T=H_X+V+S^{\sharp}+\mathcal T,
\]

where `H_X` is the actual norm head and `mathcal T` the actual infinite tail. The finite patch choices do not depend on `R`, so the coefficient-uniform Gram/distribution argument in the accepted kernel also applies to `V` and `Ssharp` separately. Summing (3.3) and using Schwartz decay yields

\[
 \sup_R|V(R)|\ll T^{\gamma+\varepsilon},\qquad
 \gamma=1/4-\kappa.
\]

Layer cake therefore supplies

\[
 M_{12}(V)\ll_\varepsilon
 T^{1+\varepsilon}+T^{10\gamma+\varepsilon}
 +T^{1+20\gamma/13+\varepsilon}. \tag{3.4}
\]

This calculation uses a generic coefficient distribution, not the actual full-wave supremum for a new mask. To make (3.4) strictly better than `T^(10 beta)`, the displayed certificate requires

\[
 \kappa>1/4-\beta=0.121033648\ldots . \tag{3.5}
\]

Indeed `10gamma<10beta` is necessary for that certificate, and once `gamma<beta`, its third exponent is smaller too because `beta>13/110`. To reach `29/25` by this certificate, the sharper necessary threshold is

\[
 \gamma\le13/125,\quad\text{equivalently}\quad
 \kappa\ge73/500. \tag{3.6}
\]

The mere existence of an unspecified positive source constant certifies neither (3.5) nor (3.6). This does not assert an upper bound for the best exponent obtainable by reworking the proof. It identifies the quantitative information that the stated theorem lacks for this restoration.

### Payment of the complete approximant by regrouping

The independent `Ssharp` owner contains both divisor ranges and the `chi4(n/m)` term in (Asharp), on every patch. It cannot be deleted by the vanished continuous area transform. It can instead be estimated as follows, using the inherited standard exponent pair `(k,l)=(13/84,55/84)` from the assigned accepted kernel.

For a fixed divisor `m`, the condition `m<l_j^(1/20)` is a suffix of the ordered patches. The condition `l_j^(1/20)<=m<l_j^(1/10)` is one interval of those patches. Their unions of norm intervals therefore each have at most two boundary points. The logarithmic factor is

\[
 b(n)=20\log n/\log l_j-2,\qquad n\in I_j.
\]

Its supremum and total variation across the shell are `O(1)`, even including patch jumps. Indeed `log n` increases, `1/log l_j` decreases, and the product variation is bounded by the supremum of either factor times the variation of the other. Both telescope between comparable shell endpoints. Thus regrouping by `m` incurs no patch-count cost. This also holds after restricting to a partial first or last shell.

Writing `n=mk`, the exponent-pair bound on each full or partial fibre is

\[
 \sum_{k\in J}e(R\sqrt{mk})
 \ll_\eta T^\eta\left(T^{13/84}N^{97/168}m^{-1/2}
 +T^{-1}N^{1/2}m^{-1}\right). \tag{3.7}
\]

For `chi4(k)`, split into the two nonzero residue classes modulo4 and apply the same bound to `k=4u+1` and `k=4u+3`. The normalized phases are fixed translates of the square-root model; their derivatives converge uniformly to that model as the fibre length grows, with no vanishing required derivative. They are in the standard monomial derivative class of the inherited exponent pair. This fixed-shift source seam should be checked alongside the inherited pair at any promotion, rather than treated as an arbitrary weighted exponent-pair theorem. The coefficient weights are handled only afterward by the just-proved variation bound. In this range the phase parameter `R sqrt(N)` exceeds fibre length `N/m`; the reciprocal derivative term in (3.7) is retained even though it is harmless.

Only `m< (2N)^(1/10)` occurs. Summing `m^(-1/2)`, restoring `N^(-3/4)Psi`, and applying partial summation gives

\[
 |S_N^\sharp(R)|\ll_{L,\eta} T^\eta(1+N/T)^{-L}
 \left(T^{13/84}N^{-103/840}+T^{-1}N^{-1/4}\right). \tag{3.8}
\]

The logarithm from the second divisor sum is absorbed into `T^eta`. For the first term the exact exponent calculation is
`55/84-13/168-3/4+1/20=-103/840`. Since this is negative, the complete retained shell sum is bounded by its lower cutoff scale:

\[
 \sup_R|S^\sharp(R)|\ll_\eta
 T^{g_\sharp+\eta},\quad
 g_\sharp=\frac{13}{84}-\frac{103}{840}\frac{52}{125}
 =\frac{13}{125}-\frac{13}{52500}<\frac{13}{125}. \tag{3.9}
\]

The generic coefficient distribution applies to this fixed approximant vector, as explained above. Its twelfth moment is at most
`T^epsilon(T+T^(10gsharp)+T^(1+20gsharp/13))`, hence is paid at `29/25`. Its exact third exponent is `29/25-1/2625`. All source epsilon losses may be chosen smaller than this fixed margin. This is a derivation of a paid approximant component, subject to the recorded inherited exponent-pair seam; it does not make the residual exponent `kappa` larger.

At zero polynomial phase the actual coefficient sum has a main term, whereas (A) only controls its difference from the approximant. Thus this control remains consistent: `Ssharp` has been estimated using the physical oscillation, not discarded as a mean-zero sequence.

The remaining bookkeeping is fully payable: the inherited generic head bound gives

\[
 M_{12}(H_X)\ll T^\varepsilon(T+X^{5/2}+TX^{5/13})
 \ll T^{29/25+\varepsilon}.
\]

The infinite tail `n>T^(3/2)` is `O_K(T^(-K))` uniformly in real `R`, from fixed Schwartz decay and the divisor bound. Its moment is `O(T^(1-12K))`. Shell recombination costs logarithmic factors only, and the finite norm inequality retains every mixed contribution among `H_X,V,Ssharp,mathcal T`. The complete certificate is consequently `max(29/25,10(1/4-kappa),1+(20/13)(1/4-kappa))`, up to epsilon. The source statement does not certify that this is smaller than `10beta`.

### Why the almost-all statement is not a complete repair

Source B's first mismatch is arithmetic: `d2-r2` is not a harmless bounded scalar twist of `d2`, and Source A's explicit extension is not a proof of a corresponding extension of Source B. Even if such an extension were proved, taking an arbitrary fixed `eta>0` does not authorize `eta=N^(-c)` with controlled constants. Thus its very-short-interval qualitative conclusion provides no prescribed power gain after patch summation.

Its exceptional measure concerns the norm-interval start `x`, whereas the desired moment integrates the radius `R`. There is no automatic conversion between these variables. A fixed tiling can intersect exceptional starts; treating them as absent is invalid. Averaging over tiling shifts could be useful only with a new identity and an estimate for all bad-patch coefficient mass. Even optimistically paying a bad portion by `N^(-3/4)N^(1+epsilon)log^(-A)N` produces only a logarithmic saving from a `N^(1/4+epsilon)` envelope, not the power budget (3.5). This is a restoration requirement, not a claim that the actual exceptional contribution attains that size.

## 4. First doubtful or unproved step

For quadratic use of Source A, the first failed hypothesis is the fixed positive length margin at and below `N~T^(2/3)`. Quartic patches repair it within the same complete objective. After that repair and the approximant payment (3.7)--(3.9), the first unproved complete step is a residual bound strong enough for the required restored exponent. An unspecified positive `kappa` does not meet the numerical gate. The approximant derivation also retains the explicit fixed-shift exponent-pair seam for independent review before any promotion.

For Source B, the first failed premise is the coefficient class. Further failures remain even after a hypothetical coefficient extension: qualitative strength, exceptional intervals, and the mismatch between start-variable measure and radius-variable moments. No theorem is rejected as false. No complete polynomial impossibility statement is established.

## 5. Required controls and outcomes

- **Actual coefficient control:** Source A explicitly states the `r2` extension, with `4(1*chi4)` and its signed approximant. Pass. Source B does not state that extension: direct application fails.
- **Polynomial versus character:** The circle nilsequence is an additive polynomial phase; `chi4` appears in the arithmetic coefficients. No multiplicative quadratic twist was substituted. Pass.
- **Quadratic boundary and quartic repair:** Formula (3.2) gives thresholds `2/3` and `6/17` as the margin tends to zero. The affordable cutoff `52/125` lies strictly above `6/17`, and the explicit positive margin was checked algebraically. Pass.
- **Moving coefficients and denominators:** Polynomial coefficients may depend on `R`; fixed test complexity and unrestricted `g` eliminate a denominator cost at this application stage. Patch-dependent arithmetic approximants are regrouped using monotone cutoff masks and bounded variation, so no patch-count factor is lost. Pass, with the fixed-shift exponent-pair seam recorded.
- **Zero phase/main owner:** Source controls a centered coefficient, not `r2` itself. Deleting `Ssharp` is forbidden by the zero-phase check. Pass.
- **Exceptional intervals:** No exceptional set for Source A; Source B's exceptional starts are neither discarded nor reinterpreted as exceptional radii. Pass.
- **Complete restoration:** (3.4)--(3.9), the paid head and approximant, exact partial endpoints, mixed terms, real projection, and infinite tail are explicit. Complete admission fails because a strong enough quantitative residual is not supplied by the stated source.
- **Computation discipline:** No numerical experiment or source-constant extrapolation was used. Rational arithmetic and symbolic derivative calculations are analytical controls. Source retrieval and hashing are provenance operations only.

## 6. Dependencies, exact artifacts, and isolation

Local context used: the assigned brief; `protocol.md`; `state/active_campaign.yml`; the graph nodes `GC-complete-square-root-large-values-moment-bound` and `GC-complete-distinct-radical-twelfth-reduction`; `complete_interface.md`; `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`; and the explicitly assigned earlier `oscillatory_remainder_gate.md`. The first graph-reading command was broader than intended and its output was truncated; the two required nodes were then retrieved selectively. No neighboring claim or sibling report was used. No shared state was edited.

Accepted inputs used mathematically are the coefficient-uniform distribution proof, elementary divisor bound, and paid head/tail restoration in the exact assigned contexts. Accepted216 is used to preserve the distinction between norm and squarefree heads, not to pay a different cutoff. Source A is a newly audited external component, not a promoted graph dependency. Source B supplies no imported estimate for the actual wave.

The conductor independently requested the bounded higher-degree length check and then supplied a proposed Type I exponent calculation with an explicit warning about patch-count loss. This report independently derived the monotone-mask regrouping, variation control, divisor sum, and complete component restoration. No sibling result or proof was supplied. Remote theorem text was read from the explicit arXiv version URLs above, including the actual Appendix A.3 and the sequel's Theorem 1.1; source PDFs were not archived in this write-restricted task. Current version histories were checked on 2026-10-11. Only the assigned report is written. Final file SHA256 is returned separately after freezing it.

For reproducibility, a read-only retrieval hashed the UTF-8 encoding of each HTML response body: Source A `8c27ee8b2827994cf8c5c1cf8d2d2a46690fe61c585ccb78c12baf7d5fb990b6` (3,166,044 bytes); Source B `c32583381357a259fb5aa115887ba3853c4a5ead6ac082ff5f048aca937168c4` (3,465,953 bytes). These are HTML response hashes, not PDF hashes.

Input SHA256 values:

```
protocol.md
f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
state/active_campaign.yml
fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa
state/proof_obligations.yml
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b
strategy/round231_quadratic_signed_admission/briefs/quadratic_source_audit.md
17e73d8aad062f387e86334e95ceed079f5d4c2f0dade19b31fc1e8e28bea68e
strategy/round231_quadratic_signed_admission/briefs/complete_interface.md
abaa43deda1db65351578941aec47e2af0aadfedcf0942b95bfea4c8636de83d
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212
strategy/round231_local_arithmetic_admission/reports/oscillatory_remainder_gate.md
834954f74200d00a508aeb0d360134a444ea1b3b0b2271d4e3b271ecd95febfe
```

## 7. Recommended state effect

**Retain** the actual polynomial-twist component from Source A and the complete approximant-payment candidate as concrete new evidence. **Revise** any blanket claim that short-interval higher uniformity misses the actual `r2` coefficients or supplies only logarithmic cancellation. **Reject** complete admission based only on the audited theorem plus the restored bounds: the statement does not certify the required residual exponent. **No change** to accepted complete moments, pointwise exponents, complete radical target, M1/M2, M9, or the quarter theorem.

The quadratic length failure is a scoped application failure; the quartic check explicitly prevents upgrading it to a polynomial-method no-go. This task stops with this report and proposes no successor round.
