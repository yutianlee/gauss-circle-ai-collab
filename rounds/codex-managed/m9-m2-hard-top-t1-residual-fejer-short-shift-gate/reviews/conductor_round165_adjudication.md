# Round 165 conductor adjudication

## 1. Result and terminal decision

Round 165 closes under

\[
 \boxed{\texttt{strict\_residual\_short\_shift\_sector}.}
\]

The complete residual Fejer estimate is not proved.  The round proves two
owner-complete target-safe sectors and a sharper exact sufficient
interface:

1. the complete tangent sector with
   \(d'-d\ge0\) and \(m'-m\ge0\) has
   \(O(L^2)\) literal correlation mass over all short shifts; and
2. after the exact divisor opening, the sector
   \((d,d')\ge\gamma L\) has
   \(O_{\gamma,\varepsilon}(L^2X^\varepsilon)\) mass for every fixed
   \(\gamma>0\).

The endpoint-exact parity connector

\[
 \mathfrak E_R\le2\mathfrak E_R^{(2)}
\]

shows that odd shifts need not be estimated.  At the minimal scale
\(R_0=\lceil L\rceil\), the sharpest currently exposed sufficient theorem
is the one-sided even-shift, opposing-displacement, low-character-divisor-
gcd aggregate

\[
 \Re\mathfrak C_{R_0,2,\mathrm{opp},\,g<\gamma L}^{\mathrm{rem}}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{165.A1}
\]

Equation (165.A1) remains open.  A second exact route uses the full-shell
window \(R=M_L\asymp L^2\): all shifts below \(R_0\) may then be paid by
Cauchy, and it is enough to prove an \(O(L^3X^\varepsilon)\) one-sided
aggregate over the even medium/long shifts.  This alternative is also
open, but it proves that the length-\(L\) short-shift theorem is sufficient
rather than mandatory.

No parent theorem or exponent changes.

## 2. Exact accepted statements and hypotheses

All statements retain the Round-164 residual coefficient, its squarefree
support, neither/both selector or no-pair value, both parity branches,
normalization, profiles, floors, stars, hard values, endpoints, and zero
extension.  The accepted coefficient energy is

\[
 D_L=\sum_N|c_N^{\mathrm{rem}}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{165.A2}
\]

For every positive integer \(R\), the full-line sliding identity and
Cauchy connector are

\[
\begin{aligned}
 \mathfrak E_R
 &=D_L+2\Re\mathfrak C_R,\\
 |\mathcal S_{L,1}^{\mathrm{rem}}|^2
 &\le {M_L+R-1\over R}\mathfrak E_R.
\end{aligned}
\tag{165.A3}
\]

Splitting each window by absolute parity gives

\[
 \mathfrak E_R^{(2)}
 =D_L+2\Re\mathfrak C_R^{(2)},\qquad
 \mathfrak E_R\le2\mathfrak E_R^{(2)}.
\tag{165.A4}
\]

For odd \(R=2S+1\ge3\), the same-parity energy is the exact positive
mixture of the length-\(S\) and length-\(S+1\) Fejer energies of the even
and odd subsequences; the terminal even gap has weight \(1/R\).  At
\(R=1\), both energies equal \(D_L\).

In tangent coordinates

\[
 a=d'-d,\qquad b=m'-m,
\]

one has, with multiplicity one,

\[
 r=db+am+ab=db+a m',\qquad
 \chi_4(d')\chi_4(d)=(-1)^{a/2}.
\tag{165.A5}
\]

The monotone sector \(a,b\ge0\) has \(O(L^2)\) atoms across the complete
short-shift aggregate.  The nonpositive and one-zero negative sectors are
empty; every remaining tuple has \(ab<0\).

With \(g=(d,d')\), \(d=gu\), \(d'=gv\), and \(r=gh\), the exact divisor-
gcd row is

\[
 vm'-um=h,\qquad m=m_0+vt,\qquad m'=m'_0+ut,
\tag{165.A6}
\]

and

\[
 N(t)=A+guv\,t,\qquad
 \chi_4(d')\chi_4(d)=\chi_4(uv).
\tag{165.A7}
\]

It has \(O(1+g)\) geometric points.  Summing the literal atoms with
\(g\ge G_0\) gives

\[
 |\mathfrak C_{R_0,g\ge G_0}^{\mathrm{rem}}|
 \ll_\varepsilon {L^3\over G_0}X^\varepsilon.
\tag{165.A8}
\]

The cofactor-gcd form has \(s=(m,m')\), \(m=su\), \(m'=sv\),
\(r=sh\), and, after enforcing odd divisors,

\[
 d=D_0+2vk,\qquad d'=D'_0+2uk.
\tag{165.A9}
\]

The character product equals

\[
 \sigma_0(-1)^{(r\bmod2)k}.
\tag{165.A10}
\]

Thus it is frozen on every even-shift row, including the squarefree
even-even branch.

Finally, for a row with actual product step \(K\), the phase derivatives
are exactly those in (165.K22).  On a cofactor row they have sizes

\[
 |\Psi'|\asymp {Jh\over L},\qquad
 \Psi''\asymp {Jh\over sL},\qquad
 |\Psi'''|\asymp {Jh\over s^2L}.
\tag{165.A11}
\]

The required discrete resonance is modulo integers for even shifts and
half-integers for odd shifts before the character is absorbed.

## 3. Proof reconciliation and power ledger

The parity inequality is pointwise in each full-line window and therefore
introduces no shiftwise modulus.  Expanding its right side retains a pair
exactly when the gap is even, with its original multiplicity \(R-r\).
This proves (165.A4) and the exact odd-window endpoint formula.

For the monotone tangent sector, literal support supplies a fixed
\(\kappa>0\) with all four factors at least \(\kappa L\).  Equation
(165.A5) gives

\[
 r=db+a m'\ge\kappa L(a+b),
\]

so only \(O(1)\) nonnegative displacement pairs occur.  Each permits
\(O(L^2)\) choices of \((d,m)\), and \(r\) is then determined.  The
uniformly bounded atom weight proves the target-safe total estimate with
no extra shift factor.

For the high divisor-gcd sector, fixed \(g\) permits
\(O(L/g)\) choices for each of \(u,v,h\) and \(O(g)\) points on each
row.  Hence

\[
 \sum_{g\ge G_0}O((L/g)^3g)\ll {L^3\over G_0}.
\]

Squarefreeness, selectors, parity, and profiles only delete opened atoms.
Equal divisors and the squarefree even-even branch are contained in this
count.  It is owner-complete for opened divisor incidences, not a claim
that a product row has a unique gcd.

The positive global ledger remains

\[
 \sum_{1\le r<R_0}\sum_N
 |c_{N+r}^{\mathrm{rem}}c_N^{\mathrm{rem}}|
 \ll_\varepsilon L^3X^\varepsilon,
\tag{165.A12}
\]

one factor \(L\) above the correlation target.  A fixed natural gcd or
tangent fibre has constant character.  The classical real second-
derivative estimate is vacuous in the inherited range, and completion of
a smooth full row followed by absolute values of its stationary dual
modes is worse than the trivial row bound.  These are placement-specific
no-go results, not an impossibility theorem for a signed aggregate method.

At the maximal scale \(R=M_L\), the allowed energy is
\(O(L^3X^\varepsilon)\).  Fixed-shift Cauchy pays the first
\(R_0-1\) shifts at that exact scale.  Applying the parity connector then
leaves only the open even medium/long aggregate.  No density input or
short-shift theorem is used in that alternative.

## 4. First doubtful or unproved step

The first unproved minimal-scale statement is (165.A1).  Its character is
constant along every cofactor-gcd progression.  A proof must preserve
cancellation across primitive slopes, opposing tangent displacements,
shifts, or phase dual modes while retaining both squarefree masks, the two
row-dependent selectors, parity branches, profiles, and hard endpoints.

No bounded two-step variation in the tangent displacement, no uniform
modulo-one resonance estimate, and no applicable complete signed shifted-
divisor or spectral theorem is proved in Round 165.

The maximal-scale alternative is also open:

\[
 \Re\sum_{\substack{R_0\le r<M_L\\2\mid r}}
 \left(1-{r\over M_L}\right)
 \sum_Nc_{N+r}^{\mathrm{rem}}\overline{c_N^{\mathrm{rem}}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon.
\tag{165.A13}
\]

Round 166 must compare these two exact frontiers, the direct scalar route,
and the rest of the proof graph during the scheduled full-strategy and
current-literature review.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal residual coefficient | **GREEN.** Every selector, parity, profile, endpoint, and squarefree convention remains in the zero-supported atom. |
| one-sided aggregate real part | **GREEN reduction, OPEN theorem.** No modulus is placed around (165.A1) or (165.A13). |
| sliding endpoints | **GREEN.** The available start interval has exactly \(M_L+R-1\) sites; gaps only create zero windows. |
| parity connector | **GREEN.** Exact for all \(R\), with the odd-\(R\) terminal weight printed. |
| tangent multiplicity and character | **GREEN.** Equation (165.A5) is bijective and the sign is \((-1)^{a/2}\). |
| monotone displacement sector | **GREEN, promotable.** \(O(L^2)\) counts the union over all short shifts. |
| dual gcd normal forms | **GREEN.** Both maps are bijective after a base solution and parity class are fixed. |
| high divisor-gcd sector | **GREEN, promotable.** Equation (165.A8) is owner-complete for opened incidences. |
| even-even squarefree branch | **GREEN.** \(\nu_2(s)=1\), reduced \(u,v\) are odd, \(4\mid r\), and \(h\) is even. |
| phase resonance | **GREEN ledger, OPEN estimate.** Large real derivatives are not confused with modulo-one separation. |
| positive fibre/B-process route | **GREEN scoped no-go.** Only positive stationary-mode placement on smooth full rows is parked. |
| phase-aligned arrays | **GREEN diagnostic.** They retain \(L^3\) Fejer capacity at \(L^2\) diagonal energy but are not physical coefficients. |
| scalar versus energy | **GREEN distinction.** The parity connector is an energy inequality; no XOR scalar estimate is promoted to energy. |
| variable Fejer scale | **GREEN reduction.** \(R_0\) is minimal diagonal-safe, not mandatory; (165.A13) is a distinct open route. |
| additive versus multiplicative geometry | **GREEN.** \(d'm'-dm=r\) is not the character-Poisson product collar. |
| downstream and exponent scope | **GREEN.** Every parent and both exponents remain open or unchanged. |
| numerical experimentation | **NOT USED.** Round 165 is entirely algebraic and analytic. |

## 6. Dependencies and exact artifacts used

- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- both Round-165 conductor candidates;
- all three primary Round-165 reports;
- the variable-scale, tangent/gcd/parity, parity/high-gcd, terminal-kernel,
  kernel-repair, and downstream graph-scope reviews; and
- the Round-165 barrier packet and active campaign.

No external source and no computation is used.

## 7. Recommended state effect

Create one proved-internal reduction node for the terminal kernel.  Update
the accepted Round-164 residual Fejer node to record that \(R_0\) is the
minimal, not unique, Fejer continuation and to point to (165.A1) and
(165.A13).  Add the new reduction only as an inconclusive dependency and
evidence item on the two open hard-TOP parents.

Promote the monotone-displacement and fixed-proportion high-divisor-gcd
sectors only inside the new reduction.  Retain the complete residual, full
\(t=1\) face, every other few-point channel, hard TOP, BAL, UNBAL, both
smooth M2 packets, M9--M2, M9--M1, endpoint uniformity, M9, bridge,
quarter theorem, internal exponent \(1/3\), and audited external exponent
unchanged.
