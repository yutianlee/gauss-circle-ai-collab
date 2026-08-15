# Round 72 conductor adjudication

## Decision

Promote a scoped all-class third-derivative lemma and retain the rest of the
upper-conductor problem, the complete fixed-interior wavelet, \(M9\!-\!M1\),
and the exponent open.  The exact order-\(J\) Farey contribution is now
target-safe throughout

\[
 T\leq C\leq J^{32/45}=X^{16/45}.
\]

Round 71 already covered \(T\leq C\leq J^{2/3}\).  The new argument covers
the strict interval

\[
 J^{2/3}<C\leq J^{32/45},
\]

with both endpoint orientations, all three local parity classes, exact Farey
neighbors, incomplete-Fresnel entry and exit, both surviving axes, gcd
restrictions, and the finite dual/error ledger retained.  The remaining
fixed-interior conductor survivor is

\[
 J^{32/45}<C\leq J.
\]

## Accepted row estimate

Let \(Q=J^{2/5}\), \(T=J/Q\), \(b\asymp B=C/T\), and
\(\kappa=c/[c,4]\in\{1/4,1/2,1\}\).  For a compatible nonaxial dual
pair \(k=\rho\sigma\), the exact phase in each local class reduces, after
fixing \(c\bmod 4b\), to

\[
 e\!\left(\pm\frac{A_{\kappa,b}}{c}\right),
 \qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2.
\]

The reduction is exact in the even classes.  Writing
\(bs_0+\rho=tc\), a fixed residue \(c\bmod4b\) fixes \(t\),
\(s_0\bmod4\), and therefore the factors
\(\chi_4(s_0)e_{2b}(\sigma t)\) or
\(\chi_4(s_0)e_b(\sigma t)\).  This is not an inference by changing the
odd-class sign.

For fixed \(b\), a residue progression is split where either Farey-neighbor
numerator changes.  The determinant equations show that there are
\(O(Q/B)\) neighbor-numerator pieces per residue and \(O(B)\) residues,
so there are \(O(Q)\) pieces in the complete row.  Each piece has
\(c\)-length \(O(C^2/J)\), hence at most \(O(C/Q)\) progression samples.
On such a piece the two normalized incomplete-Fresnel arguments vary by

\[
 O\!\left(\frac{B\sqrt{J/C}}{Q}\right)
 =O\!\left(\sqrt{C/J}\right),
\]

and all other accepted normalized stationary factors have bounded
variation.  Thus every piece has sampled sup plus variation
\(O_\varepsilon(X^\varepsilon)\), including saddle entry and exit.

Writing \(c=r+4b\ell\), the remaining phase satisfies

\[
 |f'''(\ell)|
 \asymp \frac{A_{\kappa,b}b^3}{C^4}
 \asymp \frac{J^2}{T^4}=Q^{-1}.
\]

The weighted third-derivative estimate

\[
 \sum_{n\in I}w(n)e(f(n))
 \ll V\{L\lambda^{1/6}+L^{1/2}\lambda^{-1/6}+1\}
\]

follows from one differencing step and the second-derivative estimate.
Summing its linear term by total length and its square-root term by Cauchy
over the \(O(Q)\) pieces gives, uniformly in each local class and
orientation,

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \{CQ^{-1/6}+C^{1/2}Q^{2/3}+Q\}
 \ll_\varepsilon X^\varepsilon CQ^{-1/6}.
\]

Only after this signed row estimate is established is it squared and summed
over \(b\).  Consequently

\[
 \mathcal E_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon
 \frac{C^3}{TQ^{1/3}}.
\]

This is at most \(J^2/T\) exactly when
\(C\leq J^{2/3}Q^{1/9}=J^{32/45}\).  The estimate uses the nonzero third
derivative and therefore includes near-diagonal, exact-square, and
fourth-power resonances without a derivative-gap assumption.

## Axes, tails, and endpoints

The two axes remain separate from the nonaxial row.  The accepted Round-71
nonstationary bound \(\mathcal J_{\rm axis}\ll_A\Lambda^{1-A}\), with
\(A=2\) and \(\Lambda=J/C\), gives

\[
 \mathcal D_C^{\rm axis}
 \ll_\varepsilon X^\varepsilon C^2/J
 \leq J^{19/45}X^\varepsilon.
\]

The same parameter-uniform integration by parts sums the large dual tails
and nonstationary finite cells.  Higher stationary remainders have an
additional \(\Lambda^{-1}\).  Half-open Farey endpoints, singleton pieces,
and incomplete final progressions are included by the \(+1\) term in the
third-derivative estimate.  The finite compatible dual family and two
endpoint aliases cost only \(X^\varepsilon\).

## Evidence reconciliation

The discovery report proves the exact all-class estimate and every power in
the conductor ledger.  The statement-only clean report independently
verified the energy normalization, diagonal, reciprocity, and resonance
controls before seeing the candidate; it correctly identified the actual
symbol seminorm as the missing packet datum.  A separate post-isolation seam
review then derived that seminorm from the exact Farey-neighbor equations and
certified the complete range through \(J^{32/45}\).  The hostile/source audit
independently confirmed the third-derivative powers and the \(O(Q)\) total
piece count.  Promotion therefore rests on an exact proof and an independent
all-class seam review, not on agreement by vote.

The source audit also verifies a useful but nonclosing odd-class route.
Reciprocity and completion identify the generalized level-four cusp pair
\((\infty,1)\), with external phase matched to one Bessel branch.  A full
Kuznetsov closure would require, among additional symbol, Eisenstein, even,
and axial seams, a pointwise short automorphic coefficient estimate of the
conjectural \(X^{1/4+\varepsilon}\) scale.  No audited primary theorem
supplies it.  This route is retained as candidate strategy, not accepted as
an estimate.

The original full-history blind run is exposure-contaminated and is not used
as a promotion gate.  The clean statement-only rederivation and the separate
seam review are the durable independent evidence.

## State recommendation

Create a proved internal lemma for the exact third-derivative subrange.
Update the short-numerator reduction, the low-conductor lemma, the accepted
upper self-return obstruction, and the global angular-radial obligation so
that the next analytic target is only
\(J^{32/45}<C\leq J\).  Record that generic source import and a bare
phase-matched Kuznetsov argument do not close this survivor.

Keep \(M9\!-\!M1\), \(M9\!-\!M2\), \(M9\), and the Gauss-circle target
open.  The improvement is a strict fixed-interior range extension, not a
new global exponent.
