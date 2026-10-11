# Round 225: independent envelope application review

## 1. Result

**Scoped GREEN.** This review binds controls/conductor_complete_envelope_control.md at SHA-256

1f8cd3be4e5aeb9c10e161018e615e59175cd3fedd338501113b8ab1d6e0c593.

The stated Cauchy and exponent-pair costs, conditional weight interface, optimistic scalar comparison, full tail and physical restoration are consistent. The control establishes a limitation of its specified menu of upper estimates. It does not establish an actual lower bound, prove availability of every optimal factor split, or exclude a different signed estimate.

Two scope clarifications are retained below: the inherited \(\beta\) estimate is a complete real-wave fallback, not a bound for each complex block; the general physical conversion includes the smoothing floor. Neither affects the positive exponents compared in the control, and no repair of its operative conclusions is required.

This is nonblind application review of a conductor-authored control. I authored the frozen scalar derivation and earlier isolated finite-convolution report. Those artifacts remain unchanged; their reuse is disclosed and is not independent review of my own claims. The present review checks the application interface and restoration. No current attack/norm report or sibling review was read.

## 2. Exact hypotheses and application boundary

The actual packet fixes
\[
 B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
          \cos(2\pi R\sqrt n-3\pi/4),\qquad R\in[cT,CT],
\]
where \(T\ge2\), \(0<c<C\) are fixed, and \(\Psi\) is the transform of the accepted fixed radial mollifier. In particular it is real, even and Schwartz, with \(|\Psi|\le1\); it is not assumed nonnegative.

For a legal factor block, write \(MK\asymp N\le T^{3/2}\). A sufficient interface for the control's bound is separable arithmetic vectors with
\[
 \|\alpha\|_2^2\ll T^\varepsilon M,\qquad
 \|\beta\|_2^2\ll T^\varepsilon K,
\]
and an inner weight whose paired products after Cauchy have uniformly bounded sup plus total variation, up to a stated \(T^\varepsilon\) charge. Product-cutoff intersections must be proper intervals, or have a separately paid interval/variation decomposition.

Fixed divisor convolutions and logarithmic coefficients can satisfy these size bounds after their multiplicities are included. This observation does not prove that an arbitrary desired regrouping has the required separated coefficients and masks. The control explicitly leaves that verification to an actual application and optimistically grants optimal factor availability only for its scalar comparison.

## 3. Cost, source-interface and restoration checks

### Cauchy and the complete diagonal

Suppressing a legal bounded-variation weight temporarily, let
\[
 S=\sum_{m\asymp M}\alpha_m
       \sum_{n\asymp K}\beta_n e(R\sqrt{mn}).
\]
Cauchy in \(m\) gives the outer factor \(\|\alpha\|_2^2\). The diagonal \(n=n'\) contributes
\[
 \|\alpha\|_2^2\sum_n|\beta_n|^2
          \#\{m\text{ in the applicable interval}\}
 \ll T^\varepsilon M^2K.
\]
This is the retained diagonal upper price, not a uniform lower bound for the actual vectors or sum.

For \(r=|n-n'|\ge1\),
\[
 |u|=R|\sqrt n-\sqrt{n'}|
     =\frac{Rr}{\sqrt n+\sqrt{n'}}
     \asymp\frac{Tr}{\sqrt K}.
\]
For every \(r\), Cauchy also gives
\(\sum_n|\beta_n\beta_{n+r}|\le\|\beta\|_2^2\).
Thus no extra uncounted pair multiplicity is available.

### The accepted exponent-pair interface

Set \(\kappa=13/84\) and \(\lambda=55/84\). For the unweighted phase \(u\sqrt m\), the source parameter is
\(\mathcal T=|u|\sqrt M\), and the fixed normalized phase is \(\pm\sqrt t\). Its monomial derivative class is the one checked in the accepted 204 kernel. Moreover
\[
 \frac{|u|}{\sqrt M}\gg\frac{T}{\sqrt N}\gg T^{1/4},
\]
so \(M\le\mathcal T\) is satisfied for sufficiently large \(T\). Negative \(u\) is handled by conjugation. Bounded \(T\) can be included by enlarging constants.

The accepted global Theorem-6 source interface, including proper subintervals, gives the power
\[
 |u|^\kappa M^{\lambda-\kappa/2}
 =|u|^\kappa M^{1/2+\kappa/2}.
\]
Adding the nonnegative standard term \(\sqrt M/|u|\) is harmless. This application uses the global source interface, not the narrower direct Theorem-4 window. Nor does it invoke kernel 204's displayed \(L4\) outside its stated \(|u|\ll T\) range: here \(|u|\) can be as large as \(O(T\sqrt K)\). The source remains legal, and
\[
 |u|\ll T^{7/4},\quad M\ll T^{3/2},\quad
 \mathcal T\ll T\sqrt N\ll T^{7/4}.
\]
Hence every fixed source epsilon and proper-interval logarithm is absorbed in \(T^\varepsilon\) after choosing the input epsilon sufficiently small.

Summing the first off-diagonal term over \(1\le r\ll K\) gives
\[
 T^\varepsilon M K
 \sum_{r\ll K}
 (Tr/\sqrt K)^\kappa M^{1/2+\kappa/2}
 \ll T^{\kappa+\varepsilon}
       M^{3/2+\kappa/2}K^{2+\kappa/2}.
\]
The inverse-\(u\) contribution is at most
\[
 T^{-1+\varepsilon}M^{3/2}K^{3/2}\log(2K).
\]
Its ratio to \(M^2K\), apart from epsilon losses, is
\[
 T^{-1}\sqrt{K/M}\log(2K)
 \le T^{-1}\sqrt N\log(2K)
 \ll T^{-1/4}\log(2T),
\]
so it is absorbed by the diagonal. When \(K\) is a singleton there is no off-diagonal contribution at all; retaining the displayed upper expression still gives a valid ceiling.

Taking square roots and dividing by \(N^{3/4}\) yields exactly
\[
 N^{-3/4}|S|
 \ll T^\varepsilon
 \left(N^{1/4}K^{-1/2}
       +T^{13/168}N^{13/336}K^{1/4}\right).
\]

### Weights and masks

Partial summation is applied only after the unweighted proper-interval estimate. For the radial factors, on a dyadic product interval the normalized powers, \(1/\log n\) for \(n\ge2\), and a fixed smooth dyadic cutoff have bounded scaled variation. Schwartz regularity supplies uniform bounds for \(\Psi(z)\) and \(z\Psi'(z)\), including the transition and large \(z\). Products of two such weights after Cauchy retain the required variation bound.

For two product conditions on \(mn\) and \(mn'\), the allowed \(m\)'s are their interval intersection, with exact integer endpoints. A finite endpoint convention can be retained directly. Arbitrary arithmetic or mixed masks do not automatically have this form; their decomposition and variation costs remain prerequisites. Neither the source card nor this review grants exponent-pair cancellation through arbitrary bounded weights.

### Scalar use and the complete real fallback

The closed 203 synthesis records the precise classical envelope
\(T^\varepsilon\min(N^{1/4},T^{1/2}N^{-1/2})\) used as the control's additional optimistic grant. No arbitrary weighted-factor extension of that envelope is asserted here.

My disclosed frozen scalar derivation gives
\[
 \max_\nu H(\nu)=81/614,\quad \nu_{\max}=226/307,
\]
and, for the accepted \(1/8<\beta<27/208\),
\[
 H(\nu)>\beta
 \iff
 \frac{504\beta-26}{55}<\nu<1-2\beta.
\]
The local value \(47/378\) at \(\nu=2/3\) therefore does not improve the complete optimized envelope. The numerical relation
\(\sup_\nu\min(\beta,H(\nu))=\beta\) may be read as
\[
 \min\{\beta,\sup_\nu H(\nu)\}=\beta.
\]
This compares the whole-real-wave inherited bound with the hypothetical complete bound obtained from the optimistic block menu. It does not assign the inherited \(\beta\) bound to individual blocks or to the complex wave.

### Singleton, tail and sharp reconstruction

The omitted original singleton has size at most \(r_2(1)=4\), because \(|\Psi|\le1\). Division by \(\log n\) is restricted to \(n\ge2\). Before finite convolution, truncate at \(Z=T^{3/2}\), retaining \(2\le n\le\lfloor Z\rfloor\); the last partial block and every transformed product cutoff remain exact.

For a fixed divisor exponent \(\eta>0\) and fixed Schwartz order \(J\),
\[
 \begin{aligned}
 \sum_{n>Z}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 &\ll_{\eta,J}T^{J/2}
       \sum_{n>Z}n^{-3/4+\eta-J/2}\\
 &\ll_{\eta,J}T^{J/2}Z^{1/4+\eta-J/2}\\
 &=O_{\eta,J}(T^{3/8+3\eta/2-J/4}),
 \end{aligned}
\]
provided \(J/2>1/4+\eta\). Choosing the fixed \(J\) sufficiently large pays any prescribed \(T^{-A}\). Renaming the small divisor exponent gives the control's displayed epsilon. This bound is uniform in real \(R\), uses no positivity of \(\Psi\), and requires no radius average.

The accepted bridge is
\[
 P(R^2)=\frac{\sqrt R}{\pi}B_T(R)
                   +O_\varepsilon(T^{1/2+\varepsilon}).
\]
Thus a complete bound \(B_T(R)\ll T^{\gamma+\varepsilon}\) with \(\gamma\ge0\) yields squared-radius exponent \(1/4+\gamma/2\). For a general real \(\gamma\), the exact implication is instead
\[
 1/4+\max(\gamma,0)/2,
\]
because the already paid smoothing error remains. Both exponents compared by the control are positive. Its conversion
\[
 \frac14+\frac12\frac{81}{614}=\frac{97}{307}
\]
is correct and exceeds the accepted \(\theta_{\rm LY}\). The factor \(4\) from \(r_2=4f\), the single real projection and phase \(e(-3/8)\) are fixed constants/conventions in the original packet, not discarded phases or an inherited complex bound.

## 4. First doubtful or unproved step

The first missing positive application step is a fully restored estimate for the actual finite decomposition that is stronger than this coefficient-uniform closure on every relevant scale. The control neither proves arbitrary optimal factor availability nor supplies a new bound for signed Möbius/character correlations.

Its optimistic grant is explicitly favorable. Even under that grant, the calculated menu supplies no complete improvement over \(\beta\). This is a comparison of sufficient upper prices; using it as an actual circle-wave lower bound would reverse the inequality.

No unproved step remains in the stated conditional cost calculation, tail or restoration. The two scope clarifications in Sections 1 and 3 preserve the claimed comparison without changing the frozen control.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Cauchy norms, diagonal and pair multiplicity | GREEN; actual norms retained before divisor-size upper bounds. |
| Large phase parameter and source range | GREEN; global source interface, monomial derivatives and proper intervals used. |
| Restricted \(L4\) versus global source | GREEN; no misuse of the \(|u|\ll T\) restriction. |
| Inverse-\(u\) term | GREEN; full harmonic sum absorbed by the diagonal. |
| Smooth variation and product masks | GREEN conditionally on the stated legal interface; arbitrary mixed masks remain unlicensed. |
| Optimal factor availability | Explicit optimistic grant, not an actual decomposition theorem. |
| Scalar worst scale and critical-scale contrast | Consistent with the disclosed frozen scalar calculation. |
| Complete real \(\beta\) fallback | GREEN; no per-block or complex-wave transfer inferred. |
| Full Schwartz tail, singleton and final cutoff | GREEN with fixed seminorms and literal integer endpoints. |
| Physical normalization | GREEN for the compared positive exponents; general smoothing floor made explicit. |
| Actual lower bound or universal no-go | Neither asserted. |

Zero experiments and no new primary-source audit were performed.

## 6. Dependencies and provenance

Campaign: gc-complete-logarithmic-convolution. Round: 225. Role: independent_envelope_application_review. Claimant: conductor. Reviewer: reused temporary agent, with prior authorship disclosed in Section 1.

| Artifact | SHA-256 |
|---|---|
| controls/conductor_complete_envelope_control.md | 1f8cd3be4e5aeb9c10e161018e615e59175cd3fedd338501113b8ab1d6e0c593 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| briefs/conductor_complete_circle_wave.md | 6adcf15bf5850f080aefd63c00d83d3482f6c244f5244c340b4206c47c46e0ef |
| strategy/round225_complete_circle_logarithmic_convolution.md | 64be6a3fb32b2f33deea69cef87b846ec06732e002ffd2f5156f21f7ea8c878b |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| sources/bourgain_2017_exponent_pair.md | a2b13364b738457889546d0a52c027358d7eb450bebd4272a612d70f5e917361 |
| rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md | 6ea983ef7066a7dc1a7833bbf4a99889e79c75eef9c42190421a4248c104aa5a |
| state/proof_obligations.yml, relevant source/interface lookups | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| Own frozen independent_envelope_rederivation.md, disclosed prior work | 6798954c20b615d7c53fd4478d2c05128364ab79f0ecec2fcf523e8e8aadd63c |

The closed 203 synthesis is used for the classical block envelope only; its historical moment comparison is not substituted for later accepted bounds. The source card and accepted 204 kernel supply the already audited theorem interface; no new source theorem or primary-source search was needed. The conductor supplied the exact 203 path and confirmed the two scope clarifications. No current attack/norm report or sibling review was consulted, and no frozen earlier artifact or shared state was edited.

## 7. Recommended state effect

Retain the control as **scoped GREEN complete-envelope evidence**. No analytic parent, source scope or pointwise exponent is promoted. The actual complete target still needs a stronger estimate with all decomposition and reconstruction costs paid. Stop after freezing this review; no successor is proposed or begun.
