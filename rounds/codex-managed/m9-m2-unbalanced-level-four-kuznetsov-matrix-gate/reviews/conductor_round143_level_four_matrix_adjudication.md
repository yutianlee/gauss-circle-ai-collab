# Round 143 conductor adjudication: the character embeds, but the literal matrix is outside the audited scalar interfaces

Campaign: m9-m2-unbalanced-level-four-kuznetsov-matrix-gate

Starting graph SHA-256:
7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789

## 1. Result and decision

Close Round 143 under
\(\mathsf{level\_four\_spectral\_matrix\_no\_go}\).
The round proves the exact internal fixed-modulus identity

\[
\boxed{
S^{\chi_4}_{\infty0}(4N_0,h;2n)
=\chi_4(n)S(N_0,h;n),\qquad n\ \operatorname{odd}.}
\tag{143.J1}
\]

It holds for all \(h\in\mathbb Z\) and all \((N_0,n)\), under the
displayed weight-one scaling convention, with no modulus-dependent root of
unity.  After every gcd stratum is restored, the complete inverse-first
owner is

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{g,n\ \operatorname{odd}\\gn\asymp R}}
\chi_4(g)W\!\left(\frac{X}{gnD}\right)
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)
S^{\chi_4}_{\infty0}(4N_0,h;2n).
\tag{143.J2}
\]

The \(h=0\) complement is
\(O_\varepsilon(X^\varepsilon)\).  The strict unresolved survivor is
therefore the centered, fully gcd-restored \(h\ne0\) joint matrix.

The exact arithmetic embedding does not close the analytic estimate.
The source-certified odd-character implementation is the
Blomer--Milićević standard-cusp level-\(4\) minus level-\(8\) identity,
whose scalar trace formula requires fixed arguments and one common smooth
test.  The literal coefficient is a joint arithmetic function of modulus
and Kloosterman argument, and the frozen data prove no admissible
owner-saving common-test, common-sequence, or vector-valued norm.  The
automatic coefficient-blind closure is

\[
R\sqrt\Delta\,X^\varepsilon
=\frac{X}{\sqrt{DL}}X^\varepsilon,
\tag{143.J3}
\]

strictly worse than the accepted envelope at every point of the frozen
polytope.  Complete \(h\)-summation returns the original reciprocal row.
Thus the round proves a scoped interface obstruction, not the quarter
bound, a signed lower bound, or a universal impossibility theorem.

## 2. Exact arithmetic kernel

Use

\[
S(a,b;n)=\sum_{x\bmod n}^{*}
e\!\left(\frac{a\bar x+bx}{n}\right),
\qquad
\sigma_\infty=I,\quad
\sigma_0=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix}.
\tag{143.J4}
\]

For
\(\gamma_0=\left(\begin{smallmatrix}A&B\\4C&D\end{smallmatrix}\right)\)
in \(\Gamma_0(4)\),

\[
\gamma_0\sigma_0=
\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix}.
\tag{143.J5}
\]

The positive lower-left entries are exactly \(2n\), \(n\) odd.  Translation
stabilizers reduce \(B\) modulo \(n\), and

\[
4BC\equiv-1\pmod n,\qquad
-C\equiv\bar4\,\bar B\pmod n.
\tag{143.J6}
\]

In the fixed translation double quotient,

\[
S^{\chi_4}_{\infty0}(M,H;2n)
=\chi_4(n)S(\bar4M,H;n),
\tag{143.J7}
\]

which proves (143.J1).  The cusps \(\infty,0\) are singular, \(1/2\) is
nonsingular, and \(-I\) forces weight parity \(\kappa=1\).

Put \(X=N_0+\xi\), \(r=gn\), \(k=gj\), \((j,n)=1\), and

\[
b_{g,n}(j)=
\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n).
\tag{143.J8}
\]

The normalized inverse-residue Fourier transform gives

\[
\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
=\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n),
\tag{143.J9}
\]

and \(\chi_4(gn)=\chi_4(g)\chi_4(n)\) proves (143.J2).  Every real-centre
factor, profile, unit condition, support boundary, and odd gcd stratum
remains literal.

## 3. Source boundary and complete spectral ledger

Kıral--Young equation (2.20) has the same arithmetic shape as (143.J1),
but their Theorem 2.7 assumes an even character in a weight-zero setting.
It cannot certify \(\chi_4\), a weight-one switched-cusp trace formula, or
its transform constants.  Equation (143.J1) is therefore promoted only as
an internal arithmetic lemma.

For the legal source route, let

\[
u=2^{v_2(N_0)},\qquad M_0=N_0/u,\qquad
\tau(\chi_4)=2i.
\]

Blomer--Milićević give exactly

\[
\begin{aligned}
&\sum_{\substack{n\ge1\\n\ \operatorname{odd}}}
\chi_4(n)S(N_0,h;n)\omega(n)\\
&\quad=\frac{\chi_4(M_0)}{\tau(\chi_4)}
\left\{
\sum_{4\mid C}S_{\chi_4}(M_0,16uh;C)\omega(C/4)
-
\sum_{8\mid C}S_{\chi_4}(M_0,16uh;C)\omega(C/4)
\right\}.
\end{aligned}
\tag{143.J10}
\]

The same \(\omega\) occurs in both sums.  The source-certified spectral
ledger is \(H+M+E\): odd holomorphic weights \(k\ge3\), the full
weight-one Maaß spectrum including exceptional parameters and \(t=0\) if
present, and Eisenstein integrals over every singular cusp.  Level \(4\)
has the two singular cusps \(\infty,0\) and no proper-level oldspace for
primitive conductor four.  Level \(8\) has
\(\infty,0,1/2,1/4\) and includes level-\(4\) oldclasses.  The printed
same-sign transforms are

\[
\dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},
\tag{143.J11}
\]

\[
\widetilde g(t)=\frac{it}{2\sinh(\pi t)}
\int_0^\infty\{J_{2it}(x)+J_{-2it}(x)\}g(x)\frac{dx}{x}.
\tag{143.J12}
\]

No exact odd-weight opposite-sign transform, ad hoc residual term, or
holomorphic weight-one limit is promoted.

The conditional cross-cusp \(S/c\) samples are \(2nA_g(n,h)\).  The
source-certified standard-cusp \(S/C\) samples are \(4nA_g(n,h)\), with
the fixed Gauss factor and level sign in (143.J10).  Their Bessel arguments
agree exactly, but neither representation removes the joint coefficient.

## 4. Matrix, range, capacity, and self-return

Centered zero padding and Parseval give

\[
\sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
\ll_\varepsilon\frac{X^\varepsilon}{RK},\qquad
\|A_g\|_{S_2}^2\ll_\varepsilon
\frac{X^\varepsilon}{gK},
\tag{143.J13}
\]

\[
\|A_g\|_{S_1}\ll_\varepsilon
\frac{\sqrt\Delta}{g}X^\varepsilon.
\tag{143.J14}
\]

For either fixed-multiple geometric normalization,

\[
\|B_g\|_{S_2}\ll_\varepsilon
\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,\qquad
\|B_g\|_{S_1}\ll_\varepsilon
\frac{R\sqrt\Delta}{g^2}X^\varepsilon.
\tag{143.J15}
\]

These are upper bounds.  An abstract diagonal control proves only that row
Parseval permits saturation of the nuclear upper price; it gives no lower
bound or rank statement for the literal family.

Blomer--Milićević fix positive arguments, one arithmetic weight, one
compact smooth test, and the Linnik range.  Deshouillers--Iwaniec fix a
cusp and one common sequence across the spectral quadratic forms.
Assing--Blomer--Li permit one sequence times a controlled jointly smooth
two-variable test under their support, derivative, coprimality, and scale
hypotheses.  None of the frozen coefficient controls proves an
owner-saving representation satisfying those hypotheses.

At modulus scale \(C_g=R/g\), the same-sign Linnik comparison scale is

\[
H_{\rm Lin}(g)\asymp
\frac{C_g^2}{N_0}
\asymp\frac{X}{D^2g^2}
=\frac{K}{Lg^2}.
\tag{143.J16}
\]

The continuous ratio is \(1/(Dg)\); the discrete frequency coverage is at
most a constant times that ratio and is asymptotic to it only when
\(H_{\rm Lin}(g)\gg1\).  For
\(g\gg\sqrt{K/L}\), no nonzero integer is covered.  Parseval supplies no
localization, and the source prints no complementary-range uniform
theorem.

The zero class is target-safe because

\[
|\widehat\gamma_{g,n}(0)|\ll_\varepsilon R^{-1}X^\varepsilon,
\qquad S(N_0,0;n)=c_n(N_0).
\tag{143.J17}
\]

For nonzero frequencies,

\[
\sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n)
\tag{143.J18}
\]

gives (143.J3).  With \(a=\delta-\ell\) and
\(p=1-(\delta+\ell)/2\),

\[
p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,\qquad
p-\frac{1-a}{2}=\frac12-\ell>\frac14,
\tag{143.J19}
\]

while \(p>5/8\).  Thus the positive closure is worse than both branches
of the accepted envelope
\(\min(\Delta,\sqrt{KD}+\sqrt{R/L})X^\varepsilon\).

Finally,

\[
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
=\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
\tag{143.J20}
\]

is exact self-return.  Smooth-first completion returns the accepted
\(\Delta X^\varepsilon\) capacity.  Neither is a new signed estimate.

## 5. Review decision and rejected claims

The decision is based on proof seams, not a vote.  The discovery and blind
lanes independently reproduced the double-coset identity, zero class,
matrix powers, Linnik scale, second moment, capacity, and self-return.  The
source lane separated the internal pure-level-\(4\) arithmetic identity
from the legal level-\(4/8\) spectral route.  Cross-reviews removed the
blind lane's unsupported transform constants, shifted denominators,
opposite-sign formula, residual terms, and weight-one limit term.  They
also narrowed the diagonal and interpolation controls to their exact
logical strength.

Post-candidate audits repaired the fixed double quotient, full polytope,
profile and padding ledger, exact Gauss factor, \(2n/4n\) samples,
discrete Linnik count, complete DI/ABL hypotheses, dependency paths, and
TeX hygiene.  The final discovery, blind, and source confirmations are
green before state mutation.

Reject the following route claims:

1. Kıral--Young's even theorem directly certifies odd \(\chi_4\).
2. Weight zero is legal for \(\chi_4\).
3. The internal arithmetic identity is already a sourced pure-level-\(4\)
   weight-one trace formula.
4. The Blomer--Milićević implementation is pure level four.
5. Level-\(8\) oldclasses or any singular-cusp continuous term may be
   omitted.
6. An unsupported opposite-sign transform, residual term, or separate
   holomorphic weight-one limit may be inserted.
7. The audited scalar formulas accept the literal joint matrix at no
   separation or smoothness cost.
8. Row Parseval localizes mass to the Linnik range.
9. The sharp empty-range threshold is \(g>\sqrt{K/L}\) without support
   constants.
10. The abstract diagonal is the literal matrix or proves a literal lower
    bound.
11. Exact point interpolation has free Bessel bandwidth.
12. The \(h=0\) class is an obstruction or the whole completed wave is the
    smallest survivor.
13. Complete \(h\)-summation is a gain rather than self-return.
14. The positive closure exploits \(\chi_4\) or lower-bounds the signed
    scalar.
15. Round 143 proves M9-M2, the target, or a global exponent.

## 6. Controls, dependencies, and scope

All twelve frozen controls pass with the outcomes recorded in
controls/conductor_round143_controls.md.  The exact accepted dependencies
are:

- M9-M2-unbalanced-truncated-divisor-fixed-centre-return;
- M9-M2-unbalanced-flat-wave-curvature-envelope;
- M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction; and
- M9-M2-character-factor.

The evidence consists of the three Round-143 reports, all post-unmask
cross-reviews, the conductor candidate, the three final seam families, and
the conductor controls.  Exact artifact paths are listed in the candidate
and controls.  The source locations and hypotheses are recorded in
reports/kuznetsov_source_hypothesis_audit.md and the two source-oriented
candidate audits.

The allocation was 100 percent analytical, algebraic, and source
verification.  No numerical experiment, averaging in \(X\), arbitrary
array substitution, erased gcd stratum, or unsigned-to-signed inference
was used.

Only the mechanism ledger for one flat-smooth strict-UNBAL owner changes.
Sharp, clipped, starred, transition, hard-TOP, BAL, all other UNBAL owners,
M9-M2, endpoint uniformity, M9, the conditional bridge, and the target
remain open.  No global exponent changes.

## 7. State effect

Create one external source-audit node for the exact Kıral--Young parity
boundary, Blomer--Milićević level-\(4/8\) identity and spectrum, and the
DI/ABL common-sequence and smooth-test hypotheses.

Create one proved scoped obstruction for (143.J1)--(143.J3), the
target-safe zero class, automatic matrix norms, missing common-test
interface, Linnik complement, exact self-return, and full-polytope
capacity.

Update the strict-UNBAL target and the accepted fixed-centre return,
curvature envelope, and Kloosterman-interface obstruction with this
evidence.  Keep all target and downstream statuses unchanged.  The State
Patch is authorized only after its graph validation passes.
