# 1. Result

**GREEN, with the claimant's stated scope.** This NONAUTHOR, NONBLIND review checks round226 reports/actual_shifted_spectral_sources.md at final SHA256
1bcb14e1899138097a3ab0e273060f2deaa800e3eb732e2924afb2f1f02d25bc.

The source statements, two-adic density, actual Abel costs, spectral normalization, finite Fejer constant and complete conditional implication are consistent. No repair is required. In particular, the overlapping dyadic reconstruction correctly leaves a remainder starting at \(n>N_*\), where \(N_*\) is the largest dyadic integer at most \(T^{3/2}\). Its full residual is paid.

GREEN applies to the source/applicability audit, the failure of the displayed transfer estimates to yield a gain, and the implication from the explicitly UNPROVED complete remainder estimate (24) to quarter. It does not establish (24), a new signed correlation estimate, a lower bound for the actual wave, or any accepted-state improvement.

# 2. Exact statement and hypotheses reviewed

Keep the claimant's actual \(\Psi\), all real \(cT\le R\le CT\), dyadic \(N\ge2\), smooth partition \(w=\phi-\phi(2\cdot)\), zero-extended vector
\[
 a_n=r_2(n)v_N(n)e(R\sqrt n),\qquad F_N=N^{-3/4}\sum_n a_n,
\]
and full positive-shift correlations \(C_{N,h}\). The density is
\[
 \mathfrak c_h=\frac8h\sum_{d\mid h}(-1)^{h+d}d
 =8|2^{\alpha+1}-3|\frac{\sigma_1(h')}{h},
 \quad h=2^\alpha h',\quad h'\ {\rm odd}.
\]
The reviewed proposed bound is one-sided:
\[
 2\Re\sum_{h=1}^{2N-1}\left(1-\frac h{2N}\right)
 \int_0^\infty W_{N,h}(x)\,d(A_h(x)-\mathfrak c_hx)
 \le C_{\epsilon,J}T^\epsilon A_J(N)^2N^{3/2},
 \tag{R1}
\]
uniformly for every dyadic \(2\le N\le T^{3/2}\), all the real radii, and fixed \(J\). It keeps every positive shift, including empty overlaps, the actual complex phase and the complete centered arithmetic remainder.

The source binding is exactly [HKLDW1705.04771v3, Theorem7.1, Theorem3.3 and Lemma3.4](https://arxiv.org/html/1705.04771v3), and [Assing–Humphries2607.13518v1, Theorems1.2–1.3](https://arxiv.org/html/2607.13518v1). These are the two assigned works, not additional theorem searches. The unweighted/Laplace inputs and the claimant's spectral expression are checked against these exact versions. No cusp-coefficient replacement, varying-level theorem, freely bounded test function, or exceptional-spectrum deletion is allowed.

# 3. Independent derivation and application checks

**Primary statement and normalization checks.** HKLDW Theorem7.1 retains \(h^\Theta e^{h/X}X^{1/2+\epsilon}\), with a constant independent of positive integer \(h\), and the weak sharp error with some unspecified positive exponent. Its following stronger prose is not needed and is correctly excluded. Its preliminary remark does not grant a numerical sharp exponent. The density agrees with the claimant's two equivalent formulas. The version record gives v3 on 1 April2020. [Primary statement and record](https://arxiv.org/html/1705.04771v3#S7), [record](https://arxiv.org/abs/1705.04771).

AH Theorem1.2 keeps fixed level and fixed Heegner discriminant in the constant. Theorem1.3 uses the actual sum-of-two-squares function, all positive integer length/shift pairs, and the five printed ranges. Its fixed points at levels one and two have discriminant \(-4\). The final self-reference is recorded as an apparent numbering mistake; it is not used to invent a stronger result. The literal mean-square power is \(N^{4/2}\), with \(1<M^2<N\), in both HTML and PDF text. The v1 record is dated15 July2026. [Primary theorem](https://arxiv.org/html/2607.13518v1#Thmtheorem1.3), [PDF p.4](https://arxiv.org/pdf/2607.13518v1), [record](https://arxiv.org/abs/2607.13518).

I checked the applicable statements and their application, not the complete proofs of the papers and their precursors. No independent precursor theorem is imported.

**Density, phase and endpoints.** The density formula keeps even shifts. For example its two-adic factor is \(1\) at odd \(h\), \(1\) at valuation one, and \(2^{\alpha+1}-3\) at valuation at least two; it is always positive and \(O_\epsilon(h^\epsilon)\) after division by \(h\) and multiplication by \(\sigma_1(h')\). This verifies that parity has not been silently restricted.

On nonempty support, \(x,x+h\asymp N\), and
\[
 \frac{d}{dx}\{R(\sqrt{x+h}-\sqrt x)\}
 =
 -\frac{Rh}{2\sqrt x\sqrt{x+h}(\sqrt x+\sqrt{x+h})}
 \asymp -ThN^{-3/2}.
 \tag{R2}
\]
Its absolute size is monotone. The amplitude has supremum and unscaled total variation \(O_J(A_J(N)^2)\); the phase supplies the additional variation \(Th/\sqrt N\). Thus the claimant's bounds (10), (12) and (15) follow, with exact empty overlaps zero. The Stieltjes identity
\[
 C_{N,h}=\mathfrak c_h\int W_{N,h}
            +\int W_{N,h}\,dE_h
\]
is literal, with no support replacement. Compact smooth overlaps have no boundary term; a separately imposed sharp interval must pay its endpoint terms.

For \(N\le T^{3/2}\), \(T/\sqrt N\ge T^{1/4}\). Consequently the nonstationary density estimate applies even at the smallest positive shift, and its full sum is
\[
 \sum_{h<2N}|M_{N,h}|
 \ll_{\epsilon,J}T^\epsilon A_J(N)^2
             \frac{N^{3/2}}T\log(2N).
 \tag{R3}
\]
This is a bound for an oscillatory integral with the positive density retained, not cancellation asserted merely from centering.

**Sharp-source transfer.** Substituting \(\theta=7/64\) gives
\[
 \frac34+3\theta=\frac{69}{64},
 \qquad \frac{1+4\theta}{8}=\frac{23}{128}.
\]
For all comparable prefix lengths and \(h<2N\), all five branches imply the claimant's safe envelope
\[
 \sup_{x\in[N/2,2N]}|E_h(x)|
 \ll_\epsilon N^\epsilon(N^{2/3}+N^{1/2}h^{23/128}).
 \tag{R4}
\]
The first branch alone is legal only up to a sufficiently small fixed multiple of \(N^{64/69}\). If \(h>x\) on these overlaps then \(h/x\) is bounded; the third branch has the same stated comparable-scale envelope. Any remaining bounded-parameter cases are absorbed in the constant. Flooring a real prefix costs \(O(\mathfrak c_h)\), which is harmless here.

The Abel factor is \(1+Th/\sqrt N\); it cannot be removed using the fixed exponential test. Combining the first term of (R4) with Fejer gives exactly
\[
 \frac{N^{1/2}}H+\frac{N\log(2H)}{TH}
          +N^{1/6}+THN^{-1/3}
 \tag{R5}
\]
up to the common \(T^\epsilon A_J(N)^2\). The extra large-shift terms are
\(H^{23/128}+TN^{-1/2}H^{151/128}\).
At \(N=T^{2/3}\), the last term in (R5) is \(T^{7/9}H\), and the formal balance with the diagonal has \(H=T^{-2/9}<1\). The legal \(H=1\) case is coefficient triangle; capping every correlation does not improve it. This verifies the claimed failure of that displayed upper-bound procedure. It is not a lower bound on any actual correlation.

For the printed mean square, smoothness permits
\[
 \sum_{M<h\le2M}|J_{N,h}|
 \le\int\left(\sum_h|E_h(x)|\right)\sup_h|W'_{N,h}(x)|\,dx.
\]
At each fixed \(x\asymp N\), Cauchy and the literal source power yield
\(\sum_h|E_h(x)|\ll N^\epsilon(NM^{2/3}+M^{5/2})\).
The integral of the derivative envelope contributes
\(A_J(N)^2(1+TM/\sqrt N)\). This reproduces (19). A separate varying hard endpoint is not covered by this calculation, exactly as the claimant cautions.

**Spectral formula and Mellin subtraction.** The source's equation(3.10) has the stated discrete coefficient, gamma quotient and all three continuous cusps. The constant form's Poincare pairing vanishes. Lemma3.4 places the nontrivial discrete poles on or left of \(\Re s=1/2\) at this fixed level four; this does not settle imaginary spectrum at varying levels or remove residual terms under further contour motion.

For \(q_h(y)=W_{N,h}(Ny-h)\), Mellin inversion gives
\[
 \frac1{2\pi i}\int_{(\sigma)}
 N^s\widehat q_h(s)(n+h)^{-s}\,ds=W_{N,h}(n).
\]
The \(n=0\) term is \(r_2(h)W_{N,h}(0)=0\), but its explicit subtraction in (21) is correct. More importantly,
\[
 \frac{h^{1-s}}{s-1}=\int_h^\infty y^{-s}\,dy\quad(\Re s>1);
\]
its Mellin pairing equals \(\int_0^\infty W_{N,h}(x)\,dx\). Thus the entire non-spectral term is precisely the density being subtracted, with no missing shift of the lower limit or factor \(N\).

The support of \(q_h\) stays in a fixed compact positive \(y\)-interval. After \(y=e^u\), its Mellin transform is an ordinary Fourier transform in \(u\), whose \(b\)-th derivative norm is bounded by
\(A_J(N)^2(1+\Lambda_h)^b\).
Weighted Cauchy on \(|\tau|\le1+\Lambda_h\) and \(b>a+1/2\) integrations in the outer dyadic ranges give the claimant's
\((1+\Lambda_h)^{a+1/2}\) bound. No exponential \(\Gamma(s)\) decay is present for this actual test.

Stirling gives the exponential component
\[
 \exp\{-\pi[\max(|\tau|,|t|)-|\tau|]\}.
\]
It has no decay throughout \(|t|\le|\tau|\). Hence the spectral band up to order \(T\sqrt N\), and its fourth-moment growth, cannot be suppressed. The optimistic \(a=0\) absolute transfer at \(N=T^{2/3}\) does indeed reach \(Nh^{\Theta+1/2}\). The claimant correctly labels the preceding spectral bound hypothetical and does not identify CM point values with the theta inner-product vector.

**Exact Fejer constant.** If the zero-extended vector lies on \(L\) consecutive integer sites, write its sum as the average of \(H\) translates. At most \(L+H-1\) translates can be nonzero. Cauchy and expansion give
\[
 H^2\left|\sum_n a_n\right|^2
 \le (L+H-1)\left[
 HD_N+2\Re\sum_{h=1}^{H-1}(H-h)C_{N,h}\right].
 \tag{R6}
\]
This proves (16), including \(H>L\), without altering any correlation. The bracket after division by \(H\) is nonnegative.

For the literal integer support, \(L_N=3N/2-1\). Taking \(H=2N\) in (R6) yields exactly
\[
 \frac{L_N+2N-1}{2N\,N^{3/2}}
\]
after the physical normalization. Since \(D_N\ll A_J(N)^2N^{1+\epsilon}\), inserting (R1) and (R3) proves (25):
\[
 |F_N|^2\ll_{\epsilon,J}T^\epsilon A_J(N)^2
 \left[N^{-1/2}+T^{-1}\log(2N)+1\right].
 \tag{R7}
\]
Only the one-sided upper bound (R1) is used. The centered remainder itself need not be positive.

**Full overlapping reconstruction and quarter.** For every integer \(n\ge2\),
\[
 \sum_{\substack{N=2,4,\ldots\\N\le N_*}}w(n/N)
 =\phi(n/N_*)-\phi(n)=\phi(n/N_*).
\]
At \(n=1\) the sum is zero. Thus the omitted factor is \(1-\phi(n/N_*)\), supported on \(n>N_*\), with a transition between \(N_*\) and \(2N_*\). It is not supported only on \(n>T^{3/2}\). The claimant's final text explicitly makes the correct distinction.

For fixed decay order \(D\) sufficiently large, its complete residual is bounded by
\[
 T^{D/2}N_*^{1/4+\eta-D/2}
 \ll T^{3/8+3\eta/2-D/4},
 \qquad T^{3/2}/2<N_*\le T^{3/2}.
 \tag{R8}
\]
The negative power of \(N_*\) uses its lower comparability bound; the fixed factor \(2^{D/2-1/4-\eta}\) is allowed after choosing fixed \(D\). This prices the whole overlap transition as well as the far tail. The singleton costs \(O(1)\), and all retained blocks number \(O(\log T)\).

Taking square roots in (R7), summing every retained block and rescaling \(\epsilon\) therefore gives the complete complex wave \(O(T^\epsilon)\), conditional on (R1). The exact real rotation is \(e(-3/8)\); indeed
\[
 [\Re(e(-3/8)F)]^2=(|F|^2-\Im(F^2))/2.
\]
Passing through the larger complex norm is explicit. The accepted sharp bridge restores
\(P(R^2)\ll T^{1/2+\epsilon}\), equivalently the physical quarter bound. Nothing in this implication restricts \(R\) to integers or an average set.

# 4. First doubtful or unproved step

No unresolved error was found in the audited source statements, paid transfers or conditional reconstruction. The first unproved mathematical assertion remains claimant(24), written as (R1) here, with its COMPLETE all-shift signed remainder.

The source fourth moment and sharp error theorem do not supply that joint estimate. In particular, no proof is given that the actual spectral coefficients and coupled transforms cancel after the full \(h\)-sum. The finite Fejer implication is not evidence that its premise holds.

The printed source caveats remain fenced off. The review does not amend \(4/2\) to \(4/3\), accept the deleted \(h^\Theta\), claim the numerical weak-sharp exponent, or re-prove the external papers' precursor arguments. There is no actual signed lower bound or all-method obstruction.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact claimant bytes | SHA256 matches the assigned 1bcb14e...d25bc file. |
| Literal printed powers | AH HTML and extracted PDF page4 both retain \(4/2\); self-reference remains expressly qualified. A screenshot request did not return an inspectable image to this reviewer; no visual-check claim is made. |
| Arithmetic and two-adic density | Both formulas agree for every valuation; no odd-shift restriction. |
| Test dependence | Phase variation \(Th/\sqrt N\), all fixed derivative norms, Mellin width and vertical spectral growth are priced. |
| Actual masks and endpoints | Smooth overlap remains literal. Separate hard endpoints require Abel boundary costs; a fixed-prefix mean square is not a maximal theorem. |
| Full Fejer algebra | Exact translate count, diagonal, both conjugate shift orientations, zero and empty shifts, and \(H>L\) case verified. |
| Density and remainder | The positive density is estimated with its actual oscillatory integral; the residual target is one-sided, full and unproved. |
| Dyadic tail | Residual begins at \(N_*\), including the transition below \(T^{3/2}\), and (R8) pays it. |
| Complete restoration | Singleton, logarithmic number of shells, real rotation, every real radius and the sharp physical bridge verified. |
| Stronger complex scope | Complex block control is a declared enlargement; it is not inferred from the inherited real \(\beta\) ceiling. |
| Squarefree deletion | Its quoted cost follows from \(O_\epsilon(\sqrt{NQ}N^\epsilon)\) small-class incidences: normalized correlation \(O(A_J^2Q^{1/2}N^{-1+\epsilon})\), wave-square cost \(Q^{1/2}\). The candidate uses the unmasked complete wave and avoids a false smooth-mask import. |
| Complete frontier | No M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR or endpoint owner is discharged. A future proved whole-wave (R1) would bypass those open routes through the accepted direct bridge. |
| Fixed-order scope | The twelfth milestone is not quarter; the sufficient unbounded sequence uses fixed even orders, with no \(p(T)\) constants. |
| Lower-bound scope | Large upper-certificate prices are never converted into actual correlation or wave lower bounds. |
| Experiments | Zero. All checks are source inspection and analytic/algebraic derivation. |

The inherited accepted204 moment bound and both terms of its high-value distribution remain unchanged. The report's completeness claims concern a proved conditional implication, not an already established source gain.

# 6. Dependencies, exact artifacts and provenance

Reviewer: retained-history agent joint_divisor_kernel, NONAUTHOR of the claimant report. I authored the current theta_wave_full_frontiers report and earlier geometric/norm reports and nonclaimant reviews in rounds218–225. This is a claimant-avoiding application review, not blind or fresh-context certification.

Authorized local dependencies used or retained for this review:

| Artifact | SHA256 |
|---|---|
| Current reports/actual_shifted_spectral_sources.md | 1bcb14e1899138097a3ab0e273060f2deaa800e3eb732e2924afb2f1f02d25bc |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/best_proof_draft.md | 65989358d00f0ecf7c4d385ea58bfad09eaa026af98924266207c5f8af872f00 |
| Current briefs/conductor_complete_spectral_interfaces.md | 8e9cb720ca0495aafc003434877dcd0067779993fc1edd5657b93d35ef9e77e5 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| Closed225 synthesis | c4324e2b8c75b8cb972ccf6a9e4f762ed9d8d648299acf7df77aff2b9b1546c7 |
| Own current theta report, disclosed authorship only | e5e95a4d49ab5220b0533e52a92f6d2fb727d3f4b475ce4813ab3ab698d69c79 |

The primary source dependencies are the exact versioned HTML pages in Section2 and the AH v1 PDF page4 for the printed power. The unversioned records were checked solely for version/status metadata. No additional theorem was audited, no current sibling review/checkpoint/conductor application was read, and no shared file or claimant report was edited. The review used inherited accepted interfaces as accepted context rather than representing them as newly independent proofs.

# 7. Recommended state effect

**Retain** the claimant report as GREEN candidate source/application evidence at the exact final hash above. No repair is requested.

**No change** to accepted exponents, moment bounds, the quarter claim or complete M1/M2/GAR/endpoint owners. Preserve the unproved status of claimant(24). Its proved implication is suitable for conductor strategy consideration only after the prescribed round closure; this review initiates no successor.

The source-audit conclusion is limited and useful: current actual-\(r_2\) spectral statements match the arithmetic coefficients, but their displayed sharp/Laplace estimates do not yet control the complete growing-test joint expression. Stop after this review's final hash.
