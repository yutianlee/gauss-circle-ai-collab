# 1. Result

Round229, `gc-full-goal-cuspidal-source-review`, independent nonauthor review of `reports/signed_cm_spectral_sources.md`, 2026-09-29. Reviewer: the fresh NONBLIND complete-frontier source auditor, now explicitly authorized to read this other frozen report. Zero experiments.

**GREEN for the scoped source/no-import evidence and the stated algebraic/test-cost calculations.** No mathematical repair is required. This approves neither the entire cusp estimate nor an exact evaluated CM-to-central-value identity. It does not import a new theorem into the accepted graph.

The final reviewed report SHA256 is `27f67982e63c5ff09fe0e1341ee6b6f1611e4bb64b6f6c5bd86d9dda537c9036`. The initial read bound the pre-repair hash `0d448af1d3e274c2d2914d64cfdc3776015cecb45ad9566984a8bbc014a8fd01`. The conductor identified four bare carriage-return artifacts in formula(4); the author made an authorized formatting-only repair and added provenance. The replacement formula, provenance and final hash were read and checked. No bare carriage returns or other unexpected control characters remain in the final input.

# 2. Exact statement and hypotheses reviewed

The approved conclusion is narrow: AH Lemma2.4 gives a positive upper bound for the actual fixed Heegner-point weight in its stated fixed-level range. It does not provide the evaluated local multiplier needed to transport cancellation in a signed spectral sum. KL Theorem7.14 gives a Fourier-coefficient trace identity under an unramified Hecke-index condition and a Paley--Wiener test condition. It does not itself estimate the complete CM-weighted functional.

The report preserves the frozen actual mollifier, every real radius, dyadic shell, shift, two-adic descendant, both levels, primitive old/new distinctions, exceptional/low modes and spectral/dual/original tails. Its entire cusp target remains
\[
2\Re D\ll_{\epsilon,J}A_J(N)^2N^{3/2}T^\epsilon,
\qquad2\le N\le P<2T^{3/2},\quad R\asymp T.
\]
The entire continuous partner is retained at its reviewed228 size. It is not automatically identified with a differently normalized continuous term obtained after Fourier-coordinate reconstruction.

**Primary verification A.** I independently opened [AH2607.13518v1](https://arxiv.org/html/2607.13518v1), especially Section2.1, Example2.3, Lemma2.4 and its proof. The [current record](https://arxiv.org/abs/2607.13518) gives15 July2026; the HTML body says24 August2026. The report correctly distinguishes these dates. The fixed-level and splitting/ramification hypotheses, probability norm, conductor divisibility and dyadic spectral range match. The displayed lemma is an inequality. The proof retains a local toric product and partial L-values; it bounds those factors rather than evaluating the multiplier. For discriminant minus four, the indicated points and class-number-one specialization are correct.

**Primary verification B.** I independently opened [KL1202.0189v1](https://arxiv.org/html/1202.0189v1), especially equations(3.14)--(3.16), (4.8)--(4.11), Theorem7.14 and its definitions. The [current record](https://arxiv.org/abs/1202.0189) gives1 February2012. The Hecke index must be coprime to the level; positive Fourier indices need not be coprime. The source norm is area norm divided by \(\psi(Q)\). The spectral weight includes two Fourier coefficients and \(1/\cosh(\pi t)\), and the test satisfies \(h(iz)\in PW^{12}\) with evenness. The report correctly retains the diagonal, full continuous term and every Kloosterman modulus. No uniform estimate for a growing test family is supplied by this identity.

# 3. Independent derivation and seam checks

## Positive majorant versus signed substitution

The report's finite control is valid: componentwise comparability of positive weights does not preserve cancellation against signs. In its example, the majorant-weighted sum is zero while the smaller-weighted sum is one half. The correct legal consequence of a positive majorant is an estimate involving the absolute value of the test, not a signed central-value identity. This is a logical counterexample to the proposed inference; it is not a CM counterexample.

Class number one removes the class sum but does not determine a vector-dependent local toric multiplier. The source explicitly leaves such a product in its equality. The report's equation(7) is marked as an unfilled exact interface, so no unknown local factor has been silently set equal to one. Stopping before approximate functional equations is appropriate here: none is claimed to represent the original signed sum.

## Oldspace, primitive conductors and resolvent

The inherited oldspace factor is consistent with the elementary two-dimensional Gram calculation. In area normalization, the conductor-one old basis \(u(z),u(2z)\) at level2 has Gram matrix
\[
G=\begin{pmatrix}3&\sqrt2\lambda_f(2)\\\sqrt2\lambda_f(2)&3\end{pmatrix}.
\]
Both values at \(z_2=(-1+i)/2\) equal \(u(i)\): one uses modular invariance and the other translation invariance. Thus the complete oldspace squared point weight is
\[
|u(i)|^2(1,1)G^{-1}(1,1)^t
=\frac{2|u(i)|^2}{3+\sqrt2\lambda_f(2)}.
\]
This checks the report's primitive recombination against the frozen packet. It does not independently reprove all the inherited spectral identities. Primitive conductor one remains conductor one; the level-two new factor and even/Fricke-plus restrictions remain inherited reviewed premises, correctly preserved.

For the new algebraic identity, write \(l_r=\lambda_f(2^r)\), with \(l_0=1\) and \(l_{r+1}=l_1l_r-l_{r-1}\). Multiplication of the power series gives
\[
\sum_{r\ge0}l_rx^r=(1-l_1x+x^2)^{-1}.
\]
At \(x=-2^{-1/2}\) the denominator is \((3+\sqrt2l_1)/2\), proving the report's equation(1). If the inherited local Satake bound is \(|l_r|\le(r+1)2^{r\vartheta}\), \(\vartheta<1/2\), the discarded tail is bounded by
\[
\sum_{r>B}(r+1)2^{-(1/2-\vartheta)r}
\ll_\vartheta(B+2)2^{-(1/2-\vartheta)B}.
\]
The Hecke multiplication law in equation(9) retains every power-of-two gcd. Achieving a fixed inverse power of T by truncating the resolvent generally introduces polynomial-sized Hecke indices; the report correctly refuses to count them as subpower. The series is an exact representation, not a cancellation estimate.

Probability-to-area conversion divides squared values by \(v_Q\), where \(v_1=\pi/3\), \(v_2=\pi\). KL instead divides area integrals by the index \(\psi(1)=1\), \(\psi(2)=3\). The report does not confuse these quantities. For area-norm-one vectors its division of the complete KL formula by \(\psi(Q)\) is correct.

## Fourier, parity and the original versus extracted test

Pairing positive and negative Fourier modes for an even form gives the report's equation(10), including \(2\sqrt y\), both K-Bessel factors after squaring, and signs \((-1)^a\) at real part minus one half. KL's positive-index identity sums the full parity basis. It cannot be restricted to even forms simply because odd point values vanish: after replacing point values by the positive Fourier half, the odd contributions would no longer vanish automatically. The report correctly requires an explicit parity projection and, at level2, Fricke/old-new reconstruction. The even ramified dual indices must likewise be reduced by the primitive local relation before using an unramified Hecke operator.

A nonzero smooth compact spectral cutoff has no holomorphic extension with the same compact real support. Thus evenizing such a cutoff times a phase does not meet the stated Paley--Wiener premise. This is correctly distinguished from the original transform \(H_h\), whose radial amplitude is compactly supported and smooth before spectral partition.

I checked the report's radial support and derivative ledger directly from \(W_h\), without reading any current radial report. On a nonempty overlap, \(x>N/2\) and \(x+h<2N\), so \(h<3N/2\) and \(x/h>1/3\). With \(\cosh r=1+2x/h\), this yields \(r>\log3\) and \(r\le\log(CN/h)\). Moreover,
\[
\sqrt{x+h}-\sqrt x=\sqrt h\,e^{-r/2}.
\]
On the support, its phase and fixed radial derivatives have scale \(Rh/\sqrt N\), while the differentiated smooth amplitude remains bounded by the stated fixed seminorms times \(A^2\). This avoids any singularity of the radial operator at zero.

Changing variables gives the exact spherical measure \(2\pi\sinh r\,dr\). Applying the radial operator repeatedly, integrating by parts with no boundary terms, and using the elementary spherical estimate in a fixed strip gives the stated sufficient bound
\[
|H_h(t+iv)|\ll_{\sigma,k,J}
A^2(N/h)^{1/2+\sigma}\log(2N/h)
(1+Rh/\sqrt N)^{2k}(1+|t|)^{-2k},\quad |v|\le\sigma.
\]
The bounded real-t region is handled directly, including possible zeros of the spectral eigenvalue; division by that eigenvalue is used only outside a fixed interval. Compact radial support also gives entire exponential type and evenness, so the unpartitioned original test has the required Paley--Wiener route. This does not establish admissibility for its product with the two K-Bessel factors needed by point reconstruction; the report leaves that new moving family unpaid.

For the extracted pure phase \(X_n^{it}\), scaled differentiation and vertical translation give exactly the costs in equation(12). At \(n\asymp K\), \(X_n\asymp T\sqrt N\); outside that range one must retain the exact \(X_n\). These are test seminorms, not a license for integration by parts over discrete spectral parameters and not lower bounds for the full sum.

## Complete restored powers

The inherited positive raw certificate divided by the target is
\[
\frac{A^2T^{3/2}N^{5/4}}{A^2N^{3/2}}=T^{3/2}N^{-1/4};
\]
at \(N=T\) it is \(T^{5/4}\). Dividing the same certificate by the original raw cap gives \(T^{3/2}N^{-3/4}\), at least a constant times \(T^{3/8}\) in the frozen range. The arithmetic cap, after the continuous part is paid, applies only to the complete sum of cusp levels. It leaves a raw ratio \(N^{1/2}\), hence \(T^{1/2}\) at \(N=T\). A relaxed target with factor \(T^{2\gamma}\) requires the stated \(T^{1/2-2\gamma}\) saving there.

Fejer restoration divides the squared shell by \(N^{3/2}\); the mean and diagonal are paid, and the raw cap yields complex amplitude exponent one quarter after all scales and original tails. Its physical exponent is three eighths. The existing complete complex13/56 and complete real beta remain distinct stronger caps. The report correctly compares a sufficient complex improvement with gamma less than beta and preserves the independent moment/other-parent frontiers.

# 4. First doubtful or unproved step

No unproved positive transfer is hidden in the reviewed result. The first missing premise for the CM-central-value route is an evaluated, correctly normalized local weight identity for both primitive conductors and the actual vectors. The separate trace route still lacks complete point/Fourier/parity reconstruction, a lawful moving product test and estimates for the entire resulting geometric and continuous sides.

The reviewed report does not claim to have proved these. Its first unproved complete bound remains its equation(5). The whole signed target cannot be replaced by one level, one band, a positive norm, or a source's continuous term before the exact reconstruction. No mathematical repair was needed to preserve this scope.

# 5. Controls and outcomes

| Seam | Outcome |
|---|---|
| Primary versions and exact hypotheses | GREEN: current exact AH and KL records and statements checked directly. |
| CM majorant versus identity | GREEN: inequality and unevaluated local multiplier correctly distinguished; finite signed control rederived. |
| Area/probability/index conventions | GREEN: the two norm conversions and level-one oldspace factor are consistent. |
| Old/new and two-adic series | GREEN: primitive conductor retained; generating function, absolute convergence, tail and product indices independently checked. |
| KL measure, index, parity and complements | GREEN: no deletion of continuous, diagonal, moduli, parity or oldspace data. |
| Extracted versus original test | GREEN: nonanalytic cutoff rejected; original compact radial test admissible with growing constants; K-Bessel-product test remains unproved. |
| Every restored power and tail | GREEN: ratios, squared-shell factor, complete caps and physical exponents agree. |
| Actual versus certificate | GREEN: no norm deficit or generic counterexample is presented as an actual CM lower bound. |
| Full-goal and fixed-order scope | GREEN: all M1/M2/GAR/endpoints, real-versus-complex distinctions and sufficient unbounded fixed even orders remain open. |
| Freeze integrity | GREEN: final hash verified; repaired roman labels and no bare-CR/unexpected-control characters checked. |

These are source/application and algebraic checks, not numerical experiments. I certify neither paper's full proof, the inherited228 source proof, nor any new asymptotic gain.

# 6. Exact provenance and isolation

Reviewed input: `rounds/codex-managed/gc-full-goal-cuspidal-source-review/reports/signed_cm_spectral_sources.md`, final SHA256 `27f67982e63c5ff09fe0e1341ee6b6f1611e4bb64b6f6c5bd86d9dda537c9036`; superseded formatting-only input `0d448af1d3e274c2d2914d64cfdc3776015cecb45ad9566984a8bbc014a8fd01`. The whole initial report was read; final replacement formula/provenance and final file integrity were checked after the authorized repair.

Inherited permitted context already read before this review: `protocol.md` SHA256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`; authoritative graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; frozen `briefs/complete_cuspidal_interfaces.md` SHA256 `d5a98ff0a5b44063cf9158fd8fcafc24d99ae6ac980bb0711c810bfe015da5c9`; closed228 synthesis SHA256 `f81fd743181cf1aa8381fe3ba932932220008743dab9baf1793733db6df3b721`. Their inherited premises are explicitly distinguished from this report's new source checks.

Primary accesses on29 September2026: the exact AHv1 and KLv1 HTML and current arXiv records linked in Section2. Nearby definitions and normalization equations were checked to audit the two selected statements; no additional estimate was imported.

This is a post-freeze nonauthor review, not a blind rederivation. I did not read any current radial report, conductor scalar control, current strategy/synthesis, or other newly unauthorized artifact. My own earlier frontier report remained untouched. The only new file written is this assigned review. The author/conductor messages concerned the formatting repair and replacement hash, not another current mathematical report. Zero experiments; at least95 percent analytical/algebraic work.

# 7. Recommended state effect and stop

Mark the independent CM-source review **GREEN for scoped no-import/source evidence only**, bound to the final hash above. Retain the exact resolvent and test-cost ledger as reviewed evidence. Do not promote a complete cusp, wave, moment, M1/M2/GAR, endpoint or quarter claim from this review. The graph and accepted exponents remain unchanged.

No further repair is requested. The conductor retains closure and successor authority. Freeze this review at its externally recorded SHA256 and stop.
