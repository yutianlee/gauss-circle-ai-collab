# Round 203: independent review of the radial Poisson calculation

Campaign: `gc-complete-signed-convolution-attack`. Task: `independent_radial_poisson_review`. Role: bounded line/seam reviewer, following completion of the independent divisor discovery report. Generated: 2026-09-23. Starting graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. Candidate review only. Reviewed artifact SHA-256, independently checked: `b58b66f6231c3a3fe01d5f2851a9136f1aaf9c7f0c095b5997a2e57a66a1366a`.

## 1. Result

**PASS for the stated complete radial block identity, errors and no-gain conclusion.** The odd sine kernel, its sign and coefficient are correct. The first Bessel correction and the next remainder have the stated summed cost. Both far-dual regimes, including the zero vector and the infinite high-dual tail, are accounted for. Dyadic reconstruction and the hard cutoff can be made exact with the stated costs. No mathematical repair to (P1) is required.

The displayed complete-tail moment (T^{8/3+\varepsilon}U^{-1/2}) is valid. There is a harmless quantitative refinement: applying the same second-moment argument to each smooth block before recombination gives (T^{7/3+\varepsilon}), as independently obtained in the reviewer's completed divisor report. Either estimate is weaker than the inherited benchmark. This refinement changes no success/failure decision and proves no new exponent.

## 2. Exact reviewed statement and hypotheses

The reviewed file is `rounds/codex-managed/gc-complete-signed-convolution-attack/controls/conductor_radial_poisson_analysis.md`, at the hash above. Its hypotheses are real (T\ge2), (cT\le R\le CT), (1\le N\le T^{1+\alpha}), fixed (0<\alpha<1), fixed smooth (v\) supported in ([1,2]), and the frozen real even Schwartz function (\Psi). Its claim (P1) is

\[
 H_N(R)=\sum_{m\ge1}r_2(m)m^{-1/4}L_{N,T}(R-\sqrt m)
 +O_\varepsilon(T^{-1/2+\varepsilon}N^{-1})+O_K(T^{-K}),
 \tag{R1}
\]

where

\[
 L_{N,T}(z)=\int_0^\infty r^{-1}\Psi(r/\sqrt T)v(r^2/N)
                       \sin(2\pi zr)\,dr.
 \tag{R2}
\]

Uniformity is in real (T,R,N); constants may depend on the fixed window, (\alpha\), test functions, (\varepsilon,K). The full-tail comparison uses the supplied Round-202 (L^2) and benchmark evidence with its original status. This review does not certify a new external moment theorem.

## 3. Independent derivation of the reviewed seams

### Phase and normalization

The radial function is smooth on the plane, compactly supported away from zero, and has value zero at the origin. Thus ordinary two-dimensional Poisson summation is legitimate. Polar integration gives the transform at dual radius (s):

\[
 2\pi\int_0^\infty r^{-1/2}b_{N,T}(r)
 \cos(2\pi Rr-3\pi/4)J_0(2\pi sr)\,dr.
 \tag{R3}
\]

The positive-real fixed-order expansion at (s\asymp T) has leading factor ((\pi\sqrt{sr})^{-1}\cos(2\pi sr-\pi/4)). Consequently the product, including the factor (2\pi) in (R3), is exactly

\[
 s^{-1/2}\int r^{-1}b_{N,T}(r)
 \{\sin(2\pi(R-s)r)-\cos(2\pi(R+s)r)\}\,dr.
 \tag{R4}
\]

Indeed the difference of the two cosine phases is (2\pi(R-s)r-\pi/2), and their sum is (2\pi(R+s)r-\pi). The sine has positive sign. There is no missing (\pi) factor, factor two, or fourth-root weight. Grouping nonzero lattice vectors of squared length (m) gives multiplicity (r_2(m)) and (s^{-1/2}=m^{-1/4}). In particular (L(0)=0); a positive spike at (s=R) would be a different kernel.

### Local correction and remainder

Writing (r=\sqrt N t), all amplitude derivatives are uniformly bounded on a fixed compact annulus. This remains true for (N>T): factors ((\sqrt{N/T})^j\Psi^{(j)}(\sqrt{N/T}t)) are bounded by Schwartz decay.

The first Bessel correction contains an explicit oscillatory sine/cosine factor and has amplitude (O(s^{-3/2}r^{-2})\,dr) in (R3). Rescaling and integration by parts therefore give

\[
 O_A\left(T^{-3/2}N^{-1/2}
           (1+\sqrt N|R-s|)^{-A}\right)
\]

plus an arbitrarily small (R+s) contribution. For (s\asymp T), every interval of radius width (N^{-1/2}) contains (O(1+T/\sqrt N)) possible integer squared lengths. The divisor bound supplies their actual multiplicities. Summing decaying interval weights gives (T^\varepsilon(1+T/\sqrt N)). Since (N\le T^{1+\alpha}=o(T^2)), this is (O_\varepsilon(T^{1+\varepsilon}N^{-1/2})), and the correction sums to (O_\varepsilon(T^{-1/2+\varepsilon}N^{-1})).

After this first correction the Bessel remainder is (O((sr)^{-5/2})). In (R3), its absolute contribution per dual vector is

\[
 O\left(T^{-5/2}\int_{r\asymp\sqrt N}r^{-3}\,dr\right)
 =O(T^{-5/2}N^{-1}).
\]

There are (O(T^2)) vectors in this annulus, so its full cost is (O(T^{-1/2}N^{-1})), as claimed. This step needs no derivative estimate for the Bessel remainder.

### Both far-dual regimes and extension of the main term

For (0\le s<R/2), the angular representation of (J_0) leaves radial phases with derivatives of modulus at least (R/2). Integration by parts (A) times gives (N^{1/4}(T\sqrt N)^{-A}) per vector; summing (O(T^2)) vectors is (O_K(T^{-K})) on increasing (A). This includes the zero vector.

For (s>2R), set (x=\sqrt N y) in the full planar transform. Its two phases are (\sqrt N(\pm R|y|-\xi\cdot y)); their gradients have modulus at least (\sqrt N(s-R)\ge\sqrt N s/2). After factoring out \(\sqrt N s\), all higher derivatives of the normalized phase are bounded, because (R/s<1/2) and the support avoids (y=0). Repeated nonstationary integration gives (N^{1/4}(s\sqrt N)^{-A}). The two-dimensional lattice sum over (s>2R) converges for (A>2), and is arbitrarily small in (T) for larger (A).

The leading shell can also be extended outside the middle annulus. For (s<R/2), the sum of (s^{-1/2}) over nonzero lattice vectors is (O(T^{3/2})), multiplied by arbitrarily rapid decay in (T\sqrt N). For (s>2R), summability follows from (s^{-1/2}(s\sqrt N)^{-A}). Thus extension to every (m\ge1) adds only (O_K(T^{-K})). This verifies the complete (R1), rather than a local formula with an unexamined dual remainder.

### Reconstruction, endpoints and exponent comparison

A smooth dyadic partition may be used with all full blocks above a fixed multiple of (U) and below a fixed multiple of (V=T^{1+\alpha}). The discrepancy from the sharp lower cutoff is supported in (U<n<4U) and has coefficient multipliers uniformly bounded; its supremum is (O_\varepsilon(U^{1/4+\varepsilon})). At the top, stop after full smooth blocks. Their exact remaining multiplier is supported beyond a fixed multiple of (V), so the stated Schwartz (\ell^1) tail bound applies without introducing a nonsmooth terminal block. This supplies an exact implementation of the concise reconstruction in the reviewed file.

The shell absolute bound is (T^{1/2+\varepsilon}N^{-1/2}), and the original sum is (N^{1/4+\varepsilon}). Their intersection is (N=T^{2/3}), size (T^{1/6}). Summing dyadic blocks and the lower collar gives (T^{1/6+\varepsilon}) for the entire tail. With (\int w|H_{T,>U}|^2\ll T^{1+\varepsilon}U^{-1/2}), multiplication by the tenth power of this supremum yields precisely

\[
 T^{8/3+\varepsilon}U^{-1/2},\qquad
 \|K_T*\mu^{*6}\|_2\ll T^{4/3+\varepsilon}U^{-1/4}.
\]

For the optional refinement noted in Section 1, the same frequency separation proves (\int w|H_N|^2\ll T^{1+\varepsilon}N^{-1/2}) for each smooth block. Hence its twelfth moment is bounded by

\[
 T^\varepsilon\min(TN^2,T^6N^{-11/2})\le T^{7/3+\varepsilon}.
\]

Physical (L^{12}) Minkowski recombination and the collar contribution (TU^{3+\varepsilon}) preserve that bound. This agrees with the completed independent divisor calculation. The resulting norm (T^{7/6+\varepsilon}), and the reviewed coarser norm, both remain weaker than (T^{0.648072478\ldots+\varepsilon}). The target remains (T^{29/50+\varepsilon}).

## 4. First doubtful or unproved step

No unproved step was found in the block identity or the claimed complete error bounds. The first missing mathematical input is exactly the signed shell moment estimate identified by the conductor. The oddness of (L) does not pair the actual lattice radii or their multiplicities around a general real (R). Absolute shell counting discards the cancellation needed for that estimate.

The phrase “at best” is justified only for the stated absolute-shell/minimum-envelope calculation. It is not a lower bound for the actual signed shell sum and must not be read as excluding stronger arithmetic treatment. The reviewed final scope paragraph correctly imposes this limitation.

## 5. Required control outcomes

| Control | Outcome |
|---|---|
| Actual coefficients and phases | PASS: (r_2(m)), (m^{-1/4}), positive odd sine and negative high-frequency cosine are exact. |
| Full far-dual remainder | PASS: low, zero and arbitrarily high dual vectors are bounded by separate summable nonstationary estimates. |
| Bessel source hypotheses | PASS: order zero, positive real argument, fixed order and retained first correction satisfy the inspected formulas and real-remainder conditions. |
| Endpoints and real uniformity | PASS: interval counts retain (+1) until (N=o(T^2)) is used; exact and near-integer (R^2) are included. |
| Dyadic and infinite reconstruction | PASS with the explicit smooth-block implementation above; lower collar and upper Schwartz tail are fully priced. |
| Cross terms and signed filter | PASS: complete physical (L^{12}) inequalities cover all cross terms; no positive shell estimate is called a signed moment lower bound. |
| Net exponent | PASS: classical normalized supremum (1/6); stated coarse moment powers correct; optional blockwise refinement still supplies no gain. |
| Independent statement-only control | This is a line review after unmasking, not the campaign's blind task. The divisor discovery report was saved before this artifact was read. |
| No parent overclaim | PASS: no quarter result, internal parent closure, target refutation or improved exponent is asserted. |

No numerical experiment was performed.

## 6. Dependencies and exact artifacts

- Reviewed conductor artifact at the SHA-256 recorded above.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/arithmetic_signed_tail_attack.md`, completed before review; used only for the explicit comparison and optional sharpening, not as evidence for the Bessel calculation.
- The protocol, graph, Round-203 manifest, frozen strategy, exact convolution interface and Round-202 tail audit already listed in the discovery report. No sibling report was read.
- Primary formula check, independently opened on 2026-09-23: [DLMF 10.17.3](https://dlmf.nist.gov/10.17.E3) and [10.17(iii)](https://dlmf.nist.gov/10.17.iii), for the fixed-order expansion and real-remainder hypotheses; [DLMF 10.9.1](https://dlmf.nist.gov/10.9.E1), for the angular integral representation.

No additional number-theoretic theorem is imported. The source check concerns only the Bessel formulas, not the inherited moment benchmark.

## 7. Recommended state effect

**Retain** the radial calculation as reviewed candidate evidence for a complete unsuccessful analytic attempt. **No graph or exponent change.** The block identity and its complete remainder pass this seam review; the frozen signed target remains open. The conductor may use the optional (T^{7/3+\varepsilon}) moment refinement when reporting the strongest bound supplied by these elementary block estimates, while retaining the stronger inherited benchmark as the actual comparison.

Only this assigned review was written during the review task. No shared mathematical state, conductor artifact or successor plan was changed. The review task stops here.
