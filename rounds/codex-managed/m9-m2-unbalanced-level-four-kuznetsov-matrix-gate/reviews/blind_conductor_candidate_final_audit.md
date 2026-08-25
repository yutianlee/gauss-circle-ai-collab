# Blind final audit of the Round 143 conductor candidate

Campaign: m9-m2-unbalanced-level-four-kuznetsov-matrix-gate

Audit verdict: **GREEN**, with one nonmathematical TeX repair required before promotion.

## 1. Result

The candidate is green at the statement-only algebra and logical-strength seams requested here. Its exact character-to-level cancellation, gcd-restored completion, target-safe treatment of \(h=0\), centered \(h\ne0\) survivor, Parseval and Schatten prices, diagonal control, Fourier self-return, coefficient-blind capacity, Linnik-range algebra, and full-polytope comparisons all check.

The logical conclusion is also calibrated correctly. The candidate proves a scoped obstruction from the frozen controls: the audited scalar formulas do not accept the literal joint coefficient matrix with an owner-saving norm, while the automatic coefficient-blind closure is too large. It does **not** prove a lower bound for the signed owner, a rank or nuclear-norm lower bound for the literal matrix, or the impossibility of a future vector-valued trace formula. The one required repair is the missing backslash before qquad in (143.C19); it does not affect any argument.

## 2. Exact statement and hypotheses audited

Assume the candidate's frozen definitions

\[
R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
\Delta=\frac RK=\frac DL,
\]

with

\[
\frac14\le\delta<\frac12,\qquad
0\le\ell<\delta-\frac14,\qquad D=X^\delta,\quad L=X^\ell.
\]

The additional inequality \(178\ell+1638\delta>463\) is not used by the audited local calculations; this is harmless because those calculations hold on the larger displayed range. Retain the literal inverse-selector rows and their three frozen controls

\[
|b_{g,n}(j)|\ll K^{-1}X^\varepsilon,\qquad
\sum_j|b_{g,n}(j)|\ll g^{-1}X^\varepsilon,\qquad
\sum_j|b_{g,n}(j)|^2\ll(gK)^{-1}X^\varepsilon,
\]

where \(gn\asymp R\), \(g,n\) are odd, and \(g\ll K\). With the normalized finite Fourier transform in (143.C11), the exact level-four identity gives (143.C4), with outer factor \(\chi_4(g)\) and no coprimality hypothesis on \((N_0,n)\).

Under only those data, the candidate may promote the following statement: the \(h=0\) term is \(O_\varepsilon(X^\varepsilon)\); the strict survivor is the centered \(h\ne0\) joint matrix; its automatic row, Frobenius, and nuclear controls are (143.C23)--(143.C26); and coefficient-blind use of the complete Kloosterman second moment gives at best

\[
R\sqrt\Delta\,X^\varepsilon
=\frac{X}{\sqrt{DL}}X^\varepsilon.
\]

This statement concerns only the single flat-smooth strict-UNBAL owner named in the candidate. It does not cover endpoints, sharp or clipped pieces, starred pieces, transition pieces, BAL or hard-TOP owners, the full M9-M2 claim, or a global exponent.

## 3. Proof and derivation

**Character and gcd restoration.** The convention-fixed double-coset calculation gives

\[
S^{\chi_4}_{\infty0}(4N_0,h;2n)=\chi_4(n)S(N_0,h;n).
\]

The original gcd stratum carries \(\chi_4(gn)=\chi_4(g)\chi_4(n)\). Since \(\chi_4(n)^2=1\) for odd \(n\), substitution leaves exactly \(\chi_4(g)\) in (143.C4). No step divides by \(N_0\) modulo \(n\), so the identity retains every gcd stratum.

**The zero class.** From the normalization of \(\widehat\gamma\), \(n\asymp R/g\), and the row \(\ell^1\) control,

\[
|\widehat\gamma_{g,n}(0)|
\le \frac1n\sum_j|b_{g,n}(j)|
\ll \frac1R X^\varepsilon.
\]

As \(S(N_0,0;n)=c_n(N_0)\), the Ramanujan bound and the divisor decomposition give

\[
\sum_{n\asymp R/g}(n,N_0)\ll \frac Rg X^\varepsilon.
\]

Thus one \(g\)-stratum costs \(O(g^{-1}X^\varepsilon)\), and the harmonic sum over \(g\ll K\) is absorbed by \(X^\varepsilon\). Removing this term leaves the centered \(h\ne0\) matrix as the correct strict survivor.

**Parseval and Schatten prices.** Normalized finite Parseval is

\[
\sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
=\frac1n\sum_{m\bmod n}|\gamma_{g,n}(m)|^2
\ll \frac{X^\varepsilon}{RK}.
\]

There are \(O(R/g)\) modulus rows at fixed \(g\). Hence

\[
\|A_g\|_{S_2}^2\ll\frac{X^\varepsilon}{gK}.
\]

The zero-padded matrix has rank at most \(O(R/g)\), so Cauchy on singular values gives

\[
\|A_g\|_{S_1}
\le \sqrt{R/g}\,\|A_g\|_{S_2}
\ll \frac{\sqrt\Delta}{g}X^\varepsilon.
\]

Multiplication by \(2n\asymp R/g\) for the conditional cross-cusp \(S/c\) samples, or by \(4n\asymp R/g\) for the legal standard-cusp samples, yields the two bounds in (143.C26), up to fixed constants.

**Diagonal control.** Let \(M\asymp R/g\) and place one entry of size \((RK)^{-1/2}\) in a distinct column of each of \(M\) rows. This abstract diagonal matrix has the same row-Parseval scale and

\[
\|A\|_{S_1}\asymp \frac{M}{\sqrt{RK}}
\asymp \frac{\sqrt\Delta}{g}.
\]

It therefore shows that row Parseval alone cannot improve the uniform nuclear upper price. The candidate correctly refrains from transferring this saturation to the literal inverse-selector matrix.

**Self-return.** Orthogonality in \(h\bmod n\) gives exactly

\[
\sum_h\widehat\gamma_{g,n}(h)S(N_0,h;n)
=\sum_{m\bmod n}^{*}\gamma_{g,n}(m)e(N_0\bar m/n)
=\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n).
\]

Consequently summing the complete \(h\)-family returns the original reciprocal row. Summing only \(h\ne0\) returns that row minus the already safe Ramanujan term, not a new spectral saving.

**Capacity and the polytope.** The exact complete moment

\[
\sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n)
\]

holds without a gcd restriction. Rowwise Cauchy costs \(\sqrt\Delta/g\); summing \(O(R/g)\) rows and then \(g\) costs \(R\sqrt\Delta X^\varepsilon\). If \(a=\delta-\ell\), the accepted envelope exponent is

\[
\beta(a)=\min\left\{a,\frac{1-a}{2}\right\},
\]

because \(\sqrt{KD}\) dominates \(\sqrt{R/L}\) for \(L\ge1\). The capacity exponent \(p=1-(\delta+\ell)/2\) satisfies pointwise

\[
p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,
\qquad
p-\frac{1-a}{2}=\frac12-\ell>\frac14.
\]

Also \(\delta+\ell<3/4\), hence \(p>5/8\). These are strict pointwise comparisons; the candidate does not invent an additional uniform boundary margin.

## 4. First doubtful or unproved step

There is no unproved step in the finite Fourier algebra, the \(h=0\) estimate, the norm ledger, the self-return, or the capacity comparison. The first genuine project gap is exactly where the candidate places it: one must convert the literal centered matrix into an admissible common scalar test or common coefficient sequence with owner-saving projective cost, or prove a vector-valued trace theorem that accepts it directly. Row Parseval, algebraic SVD, and point-mass interpolation do not supply the required modulus Sobolev or Bessel control.

The pure level-four cross-cusp spectral route remains conditional on a convention-matched odd-character weight-one trace formula. The legal Blomer--Milićević route is instead a level-four minus level-eight standard-cusp construction and must retain the level-eight oldclasses and all four singular cusps. Its displayed transforms are used only on the same-sign side. For maximal source-domain clarity, the sentence introducing (143.C20) may state \(h>0\) when that identity is immediately fed into those same-sign transforms; negative centered representatives must be treated by the corresponding sign reduction rather than by an unstated opposite-sign transform. This is a clarification, not a defect in the finite arithmetic identity.

The Linnik algebra is also sound:

\[
H_{\rm Lin}(g)=\frac{X}{D^2g^2}=\frac{K}{Lg^2},
\qquad
\frac{H_{\rm Lin}(g)}{R/g}\asymp\frac1{Dg}.
\]

For \(g\gg\sqrt{K/L}\), with a sufficiently large fixed constant, \(H_{\rm Lin}(g)<1\), so the stated positive-integer range is empty. Parseval gives no localization into the remaining Linnik window.

## 5. Required controls and outcomes

| Seam | Outcome | Audit finding |
|---|---|---|
| Generalized modulus, character, gcd | **PASS** | The modulus is \(2n\), \(n\) odd; the two \(\chi_4(n)\) factors cancel and no \((N_0,n)=1\) condition is inserted. |
| \(h=0\) and survivor | **PASS** | The full zero class is \(O_\varepsilon(X^\varepsilon)\); centered \(h\ne0\) is the owner-complete strict survivor. |
| Parseval and Schatten ledger | **PASS** | (143.C23)--(143.C26) follow with the stated powers of \(R,K,\Delta,g\). |
| Diagonal control | **PASS, scoped** | It proves sharpness of what row Parseval alone can imply, not literal-matrix saturation or a signed lower bound. |
| Fourier self-return | **PASS** | The normalized transform returns the original reciprocal row exactly; deleting \(h=0\) subtracts only the safe term. |
| Complete-moment capacity | **PASS** | Row, modulus, and gcd summations give \(R\sqrt\Delta=X/\sqrt{DL}\), invariant under arbitrary unit row phases. |
| Polytope comparison | **PASS** | Both branch differences are \(>1/4\) pointwise and \(p>5/8\); no chamber is missed. |
| Linnik range | **PASS** | The scale, fraction, and empty-range threshold \(g\gg\sqrt{K/L}\) are algebraically correct. |
| Source and owner scope | **PASS** | Internal level-four arithmetic is separated from the conditional pure-level-four spectrum and the legal level-four/eight source route; the conclusion remains one-owner only. |
| TeX | **REPAIR** | In (143.C19), add the missing backslash before qquad, so the separator is \(\qquad\). |

No numerical control is needed: every requested check is an exact finite identity, norm inequality, or exponent comparison.

## 6. Dependencies and exact artifacts used

This final audit used only:

- protocol.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/blind_statement.md; and
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md.

The calculations above were independently reproduced from those artifacts. No sibling candidate review, proof graph, shared state file, or proposed State Patch was used to decide the verdict. Accordingly this audit certifies the candidate's statement-level algebra and the scope of its conclusions; it does not independently certify the bibliographic contents of the source reports or the current status of graph nodes named by the candidate.

## 7. Recommended state effect

**GREEN.** After the one mechanical \(\qquad\) repair, the candidate is eligible for conductor promotion as a scoped Round 143 obstruction, subject to the already required source and graph validation outside this statement-only audit.

Promote only the exact level-four arithmetic embedding, the target-safe \(h=0\) removal, the centered joint-matrix survivor, the automatic Schatten and complete-moment capacity ledgers, the self-return, the Linnik coverage gap, and the conclusion that the frozen scalar interfaces do not close this owner. Do not promote a literal-matrix lower bound, a universal matrix-decomposition impossibility, a sourced pure-level-four odd trace formula, an opposite-sign transform normalization, a broader owner claim, or any global exponent improvement.
