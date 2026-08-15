## 1. Result

There is a scoped algebraic promotion but no transition estimate. Undoing the bounded-height factor is an exact pointwise meromorphic substitution on each finite terminal segment; by itself it moves no contour and crosses no pole. It also leaves exactly the nonintegrable one-large-gamma capacity already present in Round 20. Every shift to a useful arithmetic chamber creates an unclosed seam: the beta-bounded trace crosses the moving zeta pole already represented in the accepted arithmetic-residue ledger, while the alpha-bounded trace has no chamber in which both ordinary Dirichlet series converge. A compact transition cutoff additionally prevents a side-free Cauchy shift. Thus the proposed one-factor strategy does not presently reduce either trace to a target-sized operator.

## 2. Exact statement and hypotheses

Put
\[
 A=s-z/2,\qquad B=s+z/2,\qquad z=u+v.
\]
Then \(\Im A=\beta\) and \(\Im B=\alpha\). Define
\[
 X_\zeta(A)=\pi^{1/2-A}{\Gamma(A/2)\over\Gamma((1-A)/2)},\qquad
 X_4(B)=\left({4\over\pi}\right)^{B-1/2}
 {\Gamma((B+1)/2)\over\Gamma((2-B)/2)}.
\]
With the accepted root numbers,
\[
 K_z(1-s)=X_\zeta(A)X_4(B),\quad
 X_\zeta(A)\zeta(A)=\zeta(1-A),\quad
 X_4(B)L(B,\chi _4)=L(1-B,\chi _4).
\]
Hence beta bounded means low-height zeta and high-height \(\chi _4\); alpha bounded means low-height \(\chi _4\) and high-height zeta. The statement below assumes finite \(u,v,s\) boxes, all actual profiles and floors, and a specified bounded transition cutoff.

## 3. Proof or derivation

On the beta trace, the exact partial substitution is
\[
 K_z(1-s)F_{-z}(s)
 =\zeta(1-A)\,X_4(B)L(B,\chi _4).
\]
On the alpha trace it is
\[
 K_z(1-s)F_{-z}(s)
 =X_\zeta(A)\zeta(A)\,L(1-B,\chi _4).
\]
These identities retain the cancellations between gamma poles and trivial zeros. Multiplying either by a finite trace cutoff and the existing radial/profile factors is legal and creates no residue.

This does not improve the terminal-line estimate. On \(\Re s=c'>1+\Re z/2\), beta bounded gives
\[
 |X_4(B)|\asymp (1+|\alpha|)^{c'+\Re z/2-1/2},
\]
and alpha bounded gives
\[
 |X_\zeta(A)|\asymp (1+|\beta|)^{c'-\Re z/2-1/2}.
\]
Along a swept trace the hard top transform supplies only one inverse high-height factor. The resulting powers are respectively
\[
 |\alpha|^{c'+\Re z/2-3/2},\qquad
 |\beta|^{c'-\Re z/2-3/2},
\]
both nonintegrable under the required condition on \(c'\). The bounded factor and fixed-height portions of \(\widehat\phi\) cannot repair this control.

To make the beta formula arithmetic on both factors, one needs
\[
 \Re A<0\quad\hbox{and}\quad \Re B>0,
\]
using the ordinary zeta series and Dirichlet convergence for the nonprincipal character. Such a line exists, but moving there crosses \(A=0\), where
\[
 \zeta(1-A)=-A^{-1}+O(1).
\]
This is the same moving arithmetic pole \(s=z/2\) already isolated before the terminal vector kernel. It must be subtracted with the transition-cutoff value and reconciled with the accepted \(R_1\) residue; adding it anew double-counts the ledger.

For the alpha formula, ordinary expansions would require
\[
 \Re A>1,\qquad \Re(1-B)>0,
\]
equivalently \(\Re s>1+\Re z/2\) and \(\Re s<1-\Re z/2\), an empty chamber. Replacing zeta by
\[
 \zeta(A)={\eta(A)\over1-2^{1-A}}
\]
does not create a free Abel gain: on shifting across \(\Re A=1\), the zeros and pole in numerator, denominator, and \(X_\zeta\) must remain recombined. Expanding the reciprocal on a left line restores the full dyadic \(2\)-adic tower and hence the unsigned zeta coefficients. Dropping that reconstruction is exactly an illicit unsigned/adversarial shortcut.

## 4. First doubtful or unproved step

The first invalid step is calling a transition-restricted contour shift an ordinary Cauchy shift. If \(\psi(\beta)\) is a smooth compact cutoff, then it is not holomorphic in \(s\). Cauchy--Pompeiu adds an area term proportional to
\[
 \iint \psi'(\Im(s-z/2))\,f(s,z)\,d(\Re s)\,d(\Im s).
\]
For a hard cutoff this becomes the two internal connector integrals at the strip edges. Those terms lie at the same swept heights and have no accepted saving. An analytic cutoff cannot also have compact transition support. Thus a finite mixed-line formula is exact only after these cutoff seams, the original horizontal sides, and crossed residues are displayed.

## 5. Required control test and outcome

The factor-assignment control passes: character coefficients occur on the high \(q\)-series only in the beta branch,
\[
 L(B,\chi _4)=\sum_q\chi _4(q)q^{-B}.
\]
The alpha branch has the unsigned high series \(\zeta(A)=\sum_hh^{-A}\); its low \(L(1-B,\chi _4)\) is a scalar until one performs the incompatible shift. Consequently a character-Abel estimate for both traces either omits the alpha branch or reconstructs the previous coupled GAR/RCS arithmetic.

All seams remain material. In diagonal coordinates
\[
 u=a+i(\alpha-\beta-\nu),
\]
so the top \(1/u\) is coupled to the trace cutoff and cannot be separated before the symmetric physical limit. Shifting \(u\) or \(v\) crosses the top, height, and corner residues and creates outside sides. A sharp strip has a non-\(L^1\) Fourier tail; a smooth strip has controlled Fourier variation but the nonzero Cauchy--Pompeiu seam above. The constraints \(|\nu|\le V\), \(|\alpha-\beta-\nu|\le U\), and \(|\alpha+\beta|\le2S\) create finite corners. Exact \(H_j+1\), \(H_j=1\), the top star, and the dyadic scale count are untouched by the partial equation and supply no cancellation.

Finally, the normalized transition operator must be \(O(X^\varepsilon)\) to become \(O(X^{1/4+\varepsilon})\) after the external M1 factor. The raw height capacities above do not even have a finite physical limit; no normalization gain has been proved.

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, the Round-19, Round-20, Round-21, and Round-24 syntheses, and rounds/codex-managed/m9-m1-partial-functional-equation-transitions/briefs/partial_FE_hostile_audit.md. No claimant Round-25 report, numerical experiment, or external theorem was used.

## 7. Recommended state effect

Promote only the exact \(A/B\) assignment and the two finite pointwise one-factor identities. Retain the transition-reduction obligation as open and reject any side-free mixed-chamber or two-trace character-Abel claim. The beta shift returns the already counted arithmetic residue; the alpha branch either remains unsigned or returns, after exact reconstruction, to GAR/RCS. Both diagonal traces, their cutoff/outside-height seams, M9-M1, M9, and the target remain open.
