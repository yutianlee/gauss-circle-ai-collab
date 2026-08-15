## 1. Result

The candidate strict-subrange lemma passes the seam review.  With two
terminological clarifications, the all-class conclusion

\[
 J^{2/3}<C\leq J^{32/45}
\]

is unconditional from the accepted Round-71 antecedent and the elementary
third-derivative argument in the discovery report.  The first clarification
is that a “fixed-neighbor piece” fixes the two Farey neighbor numerators
\(a_-,a_+\); the neighbor denominators are then affine functions of \(c\),
not fixed constants.  The second is that the opposite endpoint must be read
through the exact reflected coordinate accepted in Round 71, rather than by
formally changing a sign in the odd positive-orientation formula.

For each fixed \(b\), splitting by \(c\bmod 4b\) and then by the two neighbor
numerators produces \(O(Q)\) pieces in total.  On every such piece the actual
normalized stationary weight has bounded variation \(O_\varepsilon
(X^\varepsilon)\), including incomplete-Fresnel entry and exit, while the
remaining phase in the progression variable has third derivative
\(\asymp Q^{-1}\).  The weighted third-derivative estimate therefore gives

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \left(CQ^{-1/6}+C^{1/2}Q^{2/3}+Q\right)
 \ll_\varepsilon X^\varepsilon C Q^{-1/6}.        \tag{72.S1}
\]

After squaring and summing over \(b\asymp C/T\), this reaches the frozen
energy target precisely for \(C\leq J^{32/45}\).  The exact even local units
are constant on the same progressions, and the accepted nonstationary
integration-by-parts estimate controls both surviving axes and the dual
tails in this range.  No hidden gcd, Farey-endpoint, perfect-power, or
transition loss remains.

## 2. Exact statement and hypotheses

Let

\[
 R=\lfloor J\rfloor,\qquad J=X^{1/2},\qquad
 Q=X^{1/5}=J^{2/5},\qquad T=J/Q=J^{3/5},
\]

and let

\[
 J^{2/3}<C\leq J^{32/45},\qquad
 c\asymp C,\qquad b\asymp B:=C/T.
\]

Use the exact order-\(R\) Farey partition, both offset-Poisson endpoint
orientations, all three local classes, their exact parity and gcd
restrictions, and the complete fixed-smooth-interior stationary symbols
accepted in Round 71.  Fix one compatible nonzero dual pair
\((\rho,\sigma)\), put \(k=\rho\sigma>0\) in its compatible oriented
coordinate, and put

\[
 \kappa=\frac{c}{[c,4]}\in\{1/4,1/2,1\},\qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2.
\]

The accepted compact stationary support makes \(\rho,\sigma,k=O(1)\);
there is no additional size hypothesis on the finite dual family.  For each
nonaxial class and orientation, the claim proved here is (72.S1), uniformly
in \(b\), followed by

\[
 \mathcal E_{C,k}^{(\kappa)}
 :=\sum_{b\asymp B}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon
 \frac{C^3}{TQ^{1/3}}
 \leq \frac{J^2}{T}X^\varepsilon.                 \tag{72.S2}
\]

For the weighted exponential-sum step, the needed symbol assertion is the
following concrete consequence of the accepted “fixed smoothness”:
if \(c=r+4b\ell\) and \(I_i\) is a half-open interval on which both Farey
neighbor numerators are fixed, then the normalized actual weight satisfies

\[
 \|w_i\|_\infty+\operatorname{Var}_{I_i}(w_i)
 \ll_\varepsilon X^\varepsilon.                  \tag{72.S3}
\]

Section 3 verifies (72.S3), including the transition factor, rather than
assuming it for an arbitrary coefficient array.  The axial conclusion is
separate: the odd \(\rho=0\) axis and the \(4\mid c,\sigma=0\) axis retain
their exact Round-71 nonstationary integrals and are target-safe throughout
the displayed range.

## 3. Proof or derivation

Let \(a_-/c_-\) and \(a_+/c_+\) be the Farey neighbors immediately to the
left and right of the reduced fraction \(b/c\).  Their exact determinant
and order conditions are

\[
 bc_--a_-c=1,\qquad a_+c-bc_+=1,\qquad
 R-c<c_\pm\leq R.                                 \tag{72.S4}
\]

Consequently

\[
 \frac{b(R-c)-1}{c}<a_-\leq\frac{bR-1}{c},
 \qquad a_-c\equiv-1\pmod b,                      \tag{72.S5}
\]

and

\[
 \frac{b(R-c)+1}{c}<a_+\leq\frac{bR+1}{c},
 \qquad a_+c\equiv1\pmod b.                       \tag{72.S6}
\]

Each interval in (72.S5)--(72.S6) has length \(b\), so after fixing
\(c\bmod b\) it contains exactly one member of the required residue class.
As \(c\) moves through a dyadic \(C\)-interval, its endpoints are monotone
and the selected numerator changes in steps of \(b\).  Each of \(a_-\) and
\(a_+\) therefore assumes

\[
 O(1+R/C)=O(J/C)=O(Q/B)
\]

values on a fixed residue progression.  Cutting at the union of their
change points gives \(O(Q/B)\) neighbor-numerator pieces per residue.
There are at most \(4b=O(B)\) residues modulo \(4b\), hence

\[
 P_b\ll B(Q/B)=O(Q)                               \tag{72.S7}
\]

pieces in the entire fixed-\(b\) row.  Smooth support endpoints add only
\(O(B)\), already absorbed in (72.S7).  This proves the asserted piece
count.  Literally fixing the neighbor denominators would be the wrong
partition; (72.S4) instead gives, on a numerator-fixed piece,

\[
 c_-=\frac{a_-c+1}{b},\qquad
 c_+=\frac{a_+c-1}{b}.                            \tag{72.S8}
\]

Because \(C=o(J)\) in the reviewed range,
\(c_\pm\asymp J\) and \(a_\pm\asymp bJ/C\asymp Q\).  The exact inequalities
in (72.S4) show that a numerator-fixed piece has \(c\)-length

\[
 O\!\left(\frac{b^2J}{Q^2}\right)
 =O(Cb/Q)=O(C^2/J),                               \tag{72.S9}
\]

and therefore at most \(O(C/Q)\) points of a \(4b\)-progression.  On it,
the scaled Farey endpoints are

\[
 z_-=-\frac{Jb}{(a_-+b)c+1},\qquad
 z_+= \frac{Jb}{(a_++b)c-1}.                     \tag{72.S10}
\]

They have derivative \(O(C^{-1})\).  With \(\Lambda=J/c\) and fixed
stationary coordinate \(z_*\), the variation of each incomplete-Fresnel
argument \(\sqrt\Lambda(z_\pm-z_*)\) on the piece is

\[
 O\!\left(\frac{b\sqrt\Lambda}{Q}\right)
 =O\!\left(\sqrt{\frac CJ}\right)=O(1).           \tag{72.S11}
\]

The two endpoint derivatives of the incomplete Fresnel integral are
bounded, including at saddle entry or exit.  Every remaining accepted
stationary factor is constant on the residue progression or is a fixed
smooth function of the normalized variables \(c/C\), \(Tb/c\), \(c/J\),
and the fixed stationary ratios.  Its variation on (72.S9) is \(O(1)\).
Thus (72.S11), the accepted uniform parameter-dependent stationary
construction, and partial summation give (72.S3).  A neighbor change merely
ends one half-open piece and starts another; no cross-piece variation is
charged.  This also covers singleton pieces and exact Farey endpoints.

The arithmetic-unit claim is exact.  In the odd class,
\(e_{4b}(k\bar c)\) and every character are constant after fixing
\(c\bmod4b\).  In either even class, choose the Round-71 representative
\(0\leq s_0<c\) and write

\[
 bs_0+\rho=tc.                                    \tag{72.S12}
\]

For fixed \(c\bmod4b\),
\[
 t\equiv\rho\bar c\pmod b.
\]
Since \(\rho=O(1)\) and \(c>|\rho|\), the inequality \(0\leq s_0<c\)
places \(t\) in one fixed complete set of \(b\) consecutive integers:
\(\{1,\ldots,b\}\) when \(\rho>0\), and
\(\{0,\ldots,b-1\}\) when \(\rho<0\).  Hence \(t\) is constant on the
progression.  If \(c\) increases by \(4b\), (72.S12) increases \(s_0\) by
\(4t\), so \(s_0\bmod4\) is also constant.  Therefore

\[
 \chi_4(s_0)e_{2c}(\sigma s_0)
 =\chi_4(s_0)e_{2b}(\sigma t)e(-k/(2bc))
\]

for \(c\equiv2\pmod4\), and

\[
 \chi_4(s_0)e_c(\sigma s_0)
 =\chi_4(s_0)e_b(\sigma t)e(-k/(bc))
\]

for \(4\mid c\), with the displayed local units constant on the progression.
Combining these reciprocal terms with the exact stationary critical values
\(-2(J/c)\sqrt{\kappa k}\) gives \(e(-A_{\kappa,b}/c)\) in both even
classes.  This derives the even phases from their exact local formulas; it
does not infer them by altering the odd phase.  The reflected endpoint
coordinate accepted in Round 71 gives the corresponding oriented sign and
the same derivative magnitude.

Write \(c=r+4b\ell\).  After the constant unit has been removed, the phase is

\[
 f(\ell)=\pm\frac{A_{\kappa,b}}{r+4b\ell},
\]

and hence

\[
 |f'''(\ell)|
 =\frac{6(4b)^3A_{\kappa,b}}{c^4}
 \asymp\frac{b^4J^2}{C^4}
 \asymp\frac{J^2}{T^4}=Q^{-1}.                   \tag{72.S13}
\]

It has one sign on each piece.  The weighted third-derivative lemma used in
the discovery report is correctly normalized:

\[
 \left|\sum_{n\in I}w(n)e(f(n))\right|
 \ll V\left(L\lambda^{1/6}
       +L^{1/2}\lambda^{-1/6}+1\right),           \tag{72.S14}
\]

when \(|f'''|\asymp\lambda\) has one sign and
\(V=\|w\|_\infty+\operatorname{Var}(w)\).  Indeed, for
\(L^{-3}\leq\lambda\leq1\), differencing with
\(H\asymp\lambda^{-1/3}\) changes the phase to one with second derivative
\(\asymp h\lambda\).  The second-derivative estimate and the differencing
inequality give

\[
 |S|^2\ll L^2\lambda^{1/3}+L\lambda^{-1/3},
\]

which is (72.S14); outside that range its right side dominates the trivial
bound.  Abel summation supplies \(V\).  Thus exact integral first- or
second-derivative resonances, including square and fourth-power centers, do
not invalidate the estimate.

On one residue progression, let the neighbor-piece lengths be \(L_i\).
Then

\[
 \sum_iL_i\ll T,\qquad \#\{i\}\ll Q/B.
\]

Using (72.S3), (72.S13), (72.S14), and Cauchy on
\(\sum_iL_i^{1/2}\) gives

\[
 X^\varepsilon\left(
 TQ^{-1/6}+Q^{1/6}\sqrt{TQ/B}+Q/B\right).
\]

Multiplication by \(O(B)\) residue progressions proves the first inequality
in (72.S1).  Since \(C\geq J^{2/3}=Q^{5/3}\), its second and third terms are
bounded by \(CQ^{-1/6}\), proving the second inequality.

Only now is the row squared.  Since \(B=C/T\),

\[
 \mathcal E_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon B C^2Q^{-1/3}
 =X^\varepsilon\frac{C^3}{TQ^{1/3}}.
\]

This is at most \(J^2/T\) exactly when

\[
 C^3\leq J^2Q^{1/3},
\qquad
 C\leq J^{2/3}Q^{1/9}=J^{32/45}.
\]

The zero differencing shift is the energy diagonal; all nonzero shifts are
handled inside (72.S14), so no near-diagonal is discarded.

Finally, the two axes do not use the nonaxial row.  Round 71 gives
\(\mathcal J_{\rm axis}\ll_A\Lambda^{1-A}\).  Taking \(A=2\), multiplying by
the exact per-incidence prefactor \(T/C\), and counting \(O(CB)\) incidences
gives

\[
 \mathcal D_C^{\rm axis}
 \ll_\varepsilon X^\varepsilon
 CB\frac TC\Lambda^{-1}
 =X^\varepsilon\frac{C^2}{J}
 \leq J^{19/45}X^\varepsilon.                    \tag{72.S15}
\]

This is below \(J^{1/2}X^\varepsilon\).  Taking more integrations by parts
also sums the large dual tails and nonstationary finite cells.  The finite
compatible dual family and the two orientations cost only
\(X^\varepsilon\).  Since \(B\geq J^{1/15}\), no \(b=O(1)\) stationary row
occurs.

## 4. First doubtful or unproved step

There is no remaining unproved seam inside
\(J^{2/3}<C\leq J^{32/45}\).  In particular, (72.S3) is not a new
arbitrary-weight hypothesis: the accepted Round-71 fixed smoothness handles
the ordinary factors, while (72.S8)--(72.S11) supply the previously missing
quantitative variation calculation for the exact neighbor and
incomplete-Fresnel factors.

The first unproved step is extension past the endpoint:

\[
 J^{32/45}<C\leq J.
\]

The verified third-derivative row bound then yields energy larger than
\(J^2/T\); a further joint saving is needed.  Repeating the forbidden
one-variable Poisson/B-process loop does not provide it.  No spectral
interface for the remaining range has been verified in the assigned
antecedents.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Farey piece count | Pass, with precise wording: fix \(a_-,a_+\), not \(c_-,c_+\).  Equations (72.S5)--(72.S9) give \(O(Q/B)\) pieces per residue and \(O(Q)\) per fixed-\(b\) row. |
| Piece length | Pass: a neighbor-numerator piece has \(c\)-length \(O(Cb/Q)=O(C^2/J)\) and at most \(O(C/Q)\) progression terms. |
| Actual-symbol BV | Pass: (72.S11) bounds the full change of each incomplete-Fresnel argument, and accepted normalized smoothness handles every remaining factor, proving (72.S3). |
| Third-derivative normalization | Pass: in the progression variable, \(f'''=6(4b)^3A_{\kappa,b}/c^4\asymp Q^{-1}\); (72.S14) has the correct exponents and endpoint regimes. |
| Odd arithmetic unit | Pass: it is constant on admissible residues modulo \(4b\). |
| Even arithmetic units | Pass: (72.S12) puts \(t\) in a fixed complete residue set, and \(c\mapsto c+4b\) changes \(s_0\) by \(4t\).  Thus \(t\), \(s_0\bmod4\), and both exact units are constant. |
| Opposite orientation | Pass through the exact Round-71 reflected coordinate; no bare sign substitution in (72.2) is used. |
| Gcd and parity | Pass: each residue progression is either admissible throughout or omitted throughout.  No completion or Möbius inversion introduces a gcd loss. |
| Farey and dyadic endpoints | Pass: half-open, singleton, and incomplete progressions are covered by the \(+1\) in (72.S14) and by the \(O(Q)\) piece count. |
| Diagonal and near-diagonal | Pass: differencing retains the zero shift and controls every nonzero shift before the row is squared. |
| Perfect powers and derivative resonances | Pass: only the nonvanishing third derivative is used; no Diophantine exclusion is imposed. |
| Axes | Pass: the exact Round-71 nonstationary bound gives (72.S15) for both surviving axes. |
| Dual tails and stationary errors | Pass: accepted parameter-uniform integration by parts handles nonstationary tails; the complete stationary terms are in the BV symbols, and higher remainders have extra \(\Lambda^{-1}\). |
| Finite dual family | Pass: Round 71 makes the compatible family fixed, with local restrictions applied before summation. |
| Scope | Pass: only the fixed-smooth-interior Farey contribution is extended.  No cone-edge, full \(M9\!-\!M1\), \(M9\), or Gauss-circle claim follows. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts/sources used

This review used exactly:

1. rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/conductor_farey_stationary_low_conductor.md;
2. rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/derivation_packet.md;
3. rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_reciprocal_energy_attack.md; and
4. the candidate strict-subrange claim supplied directly in the task.

No state file, proof graph, sibling review, source card, web page, or external
literature was read.  The clean blind report was neither read nor edited
during this seam review.  The only edited file is this report.

## 7. Recommended state effect

Promote the scoped internal lemma (72.S1)--(72.S2) and extend the accepted
exact fixed-smooth-interior Farey range to

\[
 T\leq C\leq J^{32/45}=X^{16/45}.
\]

The promoted statement should retain both endpoint orientations, all three
local parity classes, both surviving axes, exact gcd restrictions,
neighbor-dependent incomplete-Fresnel transitions, and the finite
dual/error sums.  Revise the open upper-conductor survivor to
\(J^{32/45}<C\leq J\).  Do not promote the complete fixed-interior wavelet,
the cone edges, \(M9\!-\!M1\), \(M9\), or any Gauss-circle exponent.
