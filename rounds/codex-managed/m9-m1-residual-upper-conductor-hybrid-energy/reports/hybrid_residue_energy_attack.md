## 1. Result

No new nonaxial conductor interval beyond

\[
 C\leq J^{32/45}
\]

is proved. Three sharp conclusions survive the attack.

First, the next one-variable \(A\)-process does not extend the accepted
third-derivative range. On a one-count cell the fourth derivative has size
\(Q^{-5/2}\), and after the \(O(Q)\) exact Farey pieces are summed the row
bound is

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \{C Q^{-5/28}+C^{3/4}Q^{3/7}
              +C^{1/2}Q^{1/2}+Q\}.                         \tag{73.D1}
\]

The first term alone would reach \(C\leq J^{5/7}\), but the second term
would require \(C\leq J^{116/175}<J^{32/45}\). Thus a
fourth-derivative claim that keeps only the first term is false at the
present transition count.

Second, the continuous phase \(A_{\kappa,b}/c\) has a uniformly nonzero
two-dimensional Hessian in the actual \(k=O(1)\) range. This does not by
itself give a lattice saving. A two-dimensional \(B\)-process followed by
absolute values is trivial at \(C\asymp J\) and worse than trivial below
it; it creates a large dual alias family that still needs cancellation.
The exact inverse or even local unit cannot be dropped in order to invoke
continuous curvature.

Third, even granting a lossless transition-compatible odd-class
\(c\)-Poisson formula, phase-matched level-four Kuznetsov, and the
corresponding Voronoi transform, the route preserves the exact
\(X^{1/20}\) deficit. Put

\[
 R=\frac JC=\frac QB,\qquad 1\leq R<J^{13/45}                \tag{73.D2}
\]

in the residual range. The smallest spectral survivor is an
actual-weighted level-four short-coefficient correlation

\[
 \boxed{|\mathfrak H_{R,k}^{\rm act}|
        \ll_\varepsilon X^\varepsilon\sqrt{JR}.}             \tag{73.D3}
\]

It has a coefficient window of length \(T\) about the level-adjusted
\(X\)-centre and spectral range \(t^2\ll R\). A pointwise bound of size
\(J^{1/2+\varepsilon}\) for every transformed short coefficient sum is
sufficient. Even the best-case trivial-length bound \(TX^\varepsilon\)
misses (73.D3) by

\[
 \frac{T}{\sqrt J}=J^{1/10}=X^{1/20},                         \tag{73.D4}
\]

independently of \(C\). The accepted third-derivative estimate becomes

\[
 |\mathfrak H_{R,k}^{\rm act}|
 \ll_\varepsilon X^\varepsilon\frac{J}{R Q^{1/6}},            \tag{73.D5}
\]

which meets (73.D3) only for the already accepted
\(R\geq J^{13/45}\). Taking the better of (73.D4) and (73.D5) therefore
does not close any strict residual subrange.

The energy diagonal is safe for every \(C\leq J\). The accepted
nonstationary axis estimate removes the axes in every fixed
power-separated range \(C\leq J^{1-\delta}\) after sufficiently many
integrations by parts, but the nonaxial correlation (73.D3) remains.

## 2. Exact statement and hypotheses

Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J/Q,\qquad
 B=C/T,\qquad R=J/C=Q/B,
\]

and assume \(J^{32/45}<C\leq J\). Fix one compatible nonaxial
\(k=\rho\sigma=O(1)\), one endpoint orientation, and one local parity
class. The only coefficient arrays under consideration are the actual
one-count arrays in (73.3), with (73.4)--(73.5), the exact inverse or
even lift unit, both Farey-neighbor transitions, and the accepted finite
dual/error ledger.

For the odd class put \(q=4b\) and

\[
 A_b=A_{1/4,b}
 =\left(\sqrt b\,J+\frac{\sqrt k}{2\sqrt b}\right)^2.
\]

The transition-compatible geometric correlation isolated by the formal
stationary transform is

\[
 \mathfrak K_{R,k}^{\rm act}
 :=\sum_{n\asymp Q^2}V(n/Q^2)e(-J\sqrt n)
   \sum_{\substack{q=4b\\b\asymp B}}
   \frac{S(n,k;q)}q
   e\!\left(-\frac{2\sqrt{nk}}q\right)
   \mathcal V_{q,n}^{\rm act},                              \tag{73.D6}
\]

where \(\mathcal V_{q,n}^{\rm act}\) is not an arbitrary bounded array:
it denotes the transform of the actual half-open Farey and
incomplete-Fresnel weight. With a lossless reconstruction of that weight,
the odd first moment has normalization

\[
 \sum_{b\asymp B}S_{b,k}^{(1/4)}(C)
 =\frac{C\sqrt T}{J}\,\mathfrak K_{R,k}^{\rm act}
   +\mathcal R_{\rm trans}.                                 \tag{73.D7}
\]

Thus (73.10) requires

\[
 \boxed{|\mathfrak K_{R,k}^{\rm act}|
 \ll_\varepsilon X^\varepsilon Q^{3/2}\sqrt R,}             \tag{73.D8}
\]

with \(\mathcal R_{\rm trans}\) separately target-safe. Formula (73.D8),
rather than a pointwise arbitrary-coefficient Kloosterman bound, is the
exact smaller geometric target.

In the ideal phase-matched spectral normalization, a Kuznetsov transform
of (73.D6) has kernel size \(R^{-1/2}\), spectral support \(t^2\ll R\),
and \(O(RX^\varepsilon)\) discrete plus continuous spectral density. A
Voronoi transform in \(n\) then gives

\[
 \sum_{n\asymp Q^2}\lambda_f(n)V_f(n/Q^2)e(-J\sqrt n)
 =\frac{Q^{3/2}}{\sqrt J}
   \sum_{|m-m_0|\ll T}\lambda_f(m)
   \Omega_f\!\left(\frac{m-m_0}{T}\right)
   +\mathcal R_f,                                           \tag{73.D9}
\]

where \(m_0=X/4\) in the standard \(4\pi\sqrt{mn}\) Bessel
normalization and changes only by the fixed level-four cusp scaling in an
exact cusp normalization. After (73.D9), (73.D8) becomes (73.D3).
The two even classes require their own cusp coefficients and local units;
neither (73.D6) nor (73.D9) is asserted for them by a sign change.

## 3. Proof or derivation

On \(c=r+4b\ell\), differentiation gives, for every fixed \(j\geq1\),

\[
 \left|\frac{d^j}{d\ell^j}\frac{A_{\kappa,b}}{r+4b\ell}\right|
 \asymp \frac{A_{\kappa,b}b^j}{C^{j+1}}.
\]

Since \(A_{\kappa,b}\asymp bJ^2\) and \(b\asymp C/T\), the fourth
derivative is

\[
 \lambda_4\asymp \frac{J^2}{T^5}=Q^{-5/2}.                  \tag{73.D10}
\]

One van der Corput differencing step, followed on each correlation by the
accepted third-derivative estimate, gives the weighted
fourth-derivative bound

\[
 \left|\sum_{\ell\in I}w(\ell)e(f(\ell))\right|
 \ll V\{L\lambda_4^{1/14}
       +L^{3/4}\lambda_4^{-1/14}+L^{1/2}+1\}.                \tag{73.D11}
\]

Indeed, choose the differencing length \(H\asymp\lambda_4^{-1/7}\).
The zero shift gives \(L^2/H\). Summing the two terms of the
third-derivative bound for \(f(x+h)-f(x)\), whose third derivative is
\(h\lambda_4\), gives respectively
\(L^2\lambda_4^{1/6}H^{1/6}\) and
\(L^{3/2}\lambda_4^{-1/6}H^{-1/6}\). Taking square roots gives
(73.D11), and Abel summation supplies \(V\).

For the exact cells, \(\sum_iL_i\ll C\) and their total number is
\(O(QX^\varepsilon)\). Therefore

\[
 \sum_iL_i^{3/4}\leq Q^{1/4}C^{3/4},\qquad
 \sum_iL_i^{1/2}\leq Q^{1/2}C^{1/2},
\]

which proves (73.D1). Squaring its second term and summing over
\(B=C/T\) values of \(b\) would meet \(J^2/T\) only if

\[
 \frac CT C^{3/2}Q^{6/7}\leq\frac{J^2}{T},\qquad
 C\leq J^{4/5}Q^{-12/35}=J^{116/175}.                       \tag{73.D12}
\]

This lies below the old boundary. By contrast, the first term alone
would impose \(C^3Q^{-5/14}\leq J^2\), or \(C\leq J^{5/7}\);
(73.D12) proves why that apparent extension is unavailable. Taking the
minimum of the third- and fourth-derivative estimates cell by cell gives
no improvement near \(C=J^{32/45}\); the fourth-derivative expression
first becomes smaller only near \(C>J^{20/21}\), where it is still far
above the target.

Next consider the continuous two-variable phase

\[
 F(b,c)=\frac{A_{\kappa,b}}c,\qquad
 a=\sqrt{\kappa k},\qquad \eta=\frac{a}{bJ}.
\]

Direct differentiation gives

\[
 \det \nabla^2F
 =\frac{J^4}{c^4}(3\eta-1)(1+\eta)^3.                       \tag{73.D13}
\]

Here \(b\gg J^{1/9}\) in the residual range and \(k=O(1)\), so
\(\eta=o(1)\); the formal degeneracy \(\eta=1/3\) is outside the
domain. Nevertheless a two-dimensional Poisson transform does not save
by curvature alone. The gradient image of a \(B\)-by-\(C\) box has area

\[
 |\det\nabla^2F|BC\asymp\frac{J^4}{TC^2},
\]

while one stationary integral has size
\(|\det\nabla^2F|^{-1/2}\asymp C^2/J^2\). Absolute summation of the
dual aliases is therefore \(J^2/T=JQ\), equal to the original point
count \(BC\) when \(C=J\) and worse by \((J/C)^2\) below it. Cancellation
among the dual aliases, with the inverse/even unit retained, is a new
problem rather than a consequence of (73.D13).

The homogeneous near-rays do not supply a counterexample, but show why
Hessian rank is not a proof. In the perfect-power control
\(J=L^5,\ Q=L^2,\ T=L^3\), the exact ray \(c=Tb\) has
\((b,c)=b\) and is inadmissible for \(b>1\). If \(T\equiv0\pmod4\),
the nearest odd rays \(c=Tb+s,\ s=\pm1\), are admissible and have
\(\bar c\equiv s\pmod{4b}\). After the integral main phase is removed,
their combined odd local phase has leading reciprocal term

\[
 e\!\left(
   \frac{s\,(Q-s\sqrt{k}/2)^2}{b+s/T}\right).                \tag{73.D14}
\]

This identity is exact after discarding the integer \(JQ=TQ^2\). It is
not constant along the ray. When the numerator is integral, exact aliases
force \(Tb+s\) to divide one fixed integer and hence have only
\(X^\varepsilon\) capacity; a square or fourth-power choice of \(X\)
therefore does not force a target-sized coherent family. Estimating the
remaining reciprocal ray is nonetheless another oscillatory sum, not a
free consequence of nonzero Hessian.

For the odd residue unit, Poisson summation modulo \(q=4b\) gives
formally

\[
 S_{b,k}^{(1/4)}(C)
 =\frac1q\sum_n S(n,k;q)I_{b,n}+\mathcal R_b,\qquad
 I_{b,n}=\int W_b(x)e\!\left(-\frac{A_b}{x}-\frac{nx}{q}\right)dx.
                                                               \tag{73.D15}
\]

The stationary point is \(x_0=(A_bq/n)^{1/2}\). Since \(x_0\asymp C\),
the stationary family is \(n\asymp A_bq/C^2\asymp Q^2\). Stationary
phase gives, up to a fixed Gaussian unit and a normalized actual weight,

\[
 \frac{I_{b,n}}q
 =\left(\frac{A_b}{q}\right)^{1/4}n^{-3/4}
   e\!\left(-2\sqrt{\frac{A_bn}{q}}\right)V_{b,n}
 =J^{1/2}n^{-3/4}
   e\!\left(-J\sqrt n-\frac{\sqrt{kn}}{2b}\right)V_{b,n}.
                                                               \tag{73.D16}
\]

The last phase identity is exact because
\(\sqrt{A_b/q}=J/2+\sqrt k/(4b)\). Equivalently, rewriting the
\(q\)-sum with \(S(n,k;q)/q\) extracts the prefactor
\(C\sqrt T/J\) and gives (73.D6)--(73.D7).

In the phase-matched Kuznetsov model the Bessel argument is

\[
 x=4\pi\sqrt{nk}/q\asymp Q/B=R.
\]

The factor \(e(-2\sqrt{nk}/q)=e^{-ix}\) cancels one large-argument
Bessel branch. That branch has transform size \(R^{-1/2}\); its residual
phase is of size \(t^2/R\), hence \(t^2\ll R\). Weyl density gives
\(O(RX^\varepsilon)\) spectral data. Thus a uniform spectral \(n\)-sum
of size \(Q^{3/2}X^\varepsilon\) is exactly sufficient for (73.D8),
independently of \(C\).

The \(n\)-sum has one stationary Voronoi branch. Combining
\(e(-J\sqrt n)\) with the standard Hankel phase \(e(2\sqrt{mn})\)
shows that it is stationary at \(2\sqrt m=J\). Since \(n\asymp Q^2\),
integration by parts restricts

\[
 |2\sqrt m-J|\ll Q^{-1},\qquad |m-X/4|\ll J/Q=T.
\]

The Bessel amplitude \((mn)^{-1/4}\) and an \(n\)-interval of length
\(Q^2\) give transform size

\[
 Q^2(JQ)^{-1/2}=Q^{3/2}J^{-1/2},
\]

which proves the scaling (73.D9). Hence (73.D8) is equivalent, in this
lossless model, to (73.D3). Triangle summation of \(O(R)\) spectral data,
each with transform \(R^{-1/2}\), and the best-case short-sum bound \(T\)
gives

\[
 |\mathfrak H_{R,k}^{\rm act}|\ll X^\varepsilon\sqrt R\,T,
\]

whose ratio to (73.D3) is exactly (73.D4).

Finally, the accepted third-derivative first-moment bound is

\[
 \sum_{b\asymp B}|S_{b,k}^{(\kappa)}(C)|
 \ll X^\varepsilon\frac{C^2}{TQ^{1/6}}.
\]

Using the prefactors in (73.D7) and (73.D9) converts this to (73.D5).
Its ratio to (73.D3) is

\[
 \frac{J^{13/30}}{R^{3/2}},                                  \tag{73.D17}
\]

which is at least one precisely in the residual range. The derivative
and spectral-trivial bounds cross at \(R=J^{2/9}\), equivalently
\(C=J^{7/9}\), but their minimum remains above the target on both sides.
There is no lawful operation that multiplies these two gains: the
third-derivative proof takes absolute values over the cells before residue
cancellation, whereas Kuznetsov must recombine those cells before absolute
values. Applying Kuznetsov again to bound the transformed short spectral
correlation returns moduli \(c\asymp J/R=C\), and applying Voronoi twice
is involutive. This is a deficit-preserving terminal transfer, not a new
saving.

The exact energy diagonal is

\[
 \mathcal E_{\rm diag}\ll X^\varepsilon BC
 =X^\varepsilon C^2/T\leq X^\varepsilon J^2/T
\]

for every \(C\leq J\). All nonzero near-diagonal terms remain inside
(73.D6) or (73.D3). For either surviving axis, the accepted \(A\)-fold
nonstationary estimate gives

\[
 \mathcal D_C^{\rm axis}
 \ll_{A,\varepsilon}X^\varepsilon
 C\left(\frac JC\right)^{1-A}
 =X^\varepsilon\frac{C^A}{J^{A-1}}.                          \tag{73.D18}
\]

Thus the axes are safe for \(C\leq J^{1-1/(2A)}\); for example \(A=3\)
removes them through \(C\leq J^{5/6}\). This does not settle the
nonaxial energy, and no axis claim is made for the top \(C\asymp J\)
band.

## 4. First doubtful or unproved step

The first unproved step is earlier than Kuznetsov. The packet supplies a
bounded-variation weight separately on each half-open residue/Farey cell,
but it does not supply a cross-residue smooth extension whose Poisson
transform can be recombined into the complete \(S(n,k;4b)\) in (73.D15)
with only \(X^\varepsilon\) total transition loss. Applying Poisson to
the \(O(Q)\) cells separately and multiplying by their number is forbidden
and is too large. Consequently \(\mathcal R_{\rm trans}\) in (73.D7)
has not been proved target-safe from (73.4)--(73.5) alone.

Even if that seam is granted, the first genuinely new analytic estimate is
(73.D3), or equivalently the geometric correlation (73.D8), with the
actual moving transition transform. It requires the exact level-four cusp
normalization, the continuous spectrum, both even cusp pairs, local gcd
data, and the two axes. The stationary calculations above show that a
lossless Kuznetsov--Voronoi transfer cannot replace this estimate by a
known trivial bound: it retains the \(X^{1/20}\) deficit.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Inherited row normalization | Pass. Equations (73.D15)--(73.D16) reproduce \(n\asymp Q^2\), \(I/q\asymp J^{1/2}n^{-3/4}\asymp T^{3/2}/J\), and the first-moment prefactor \(C\sqrt T/J\). Equations (73.D5), (73.D8), and (73.D17) use the exact target. |
| Residue progression and one-count ownership | Pass algebraically, unproved analytically. Half-open cells can be recombined without duplicating an integer \(c\), but their actual weights have not been shown to admit the single transition-compatible smooth extension required by (73.D15). |
| Transition bounded variation | Fail as a closure seam. Per-cell variation proves (73.D1), but does not license a complete Kloosterman sum or low-rank spectral weight across all \(O(Q)\) cells. No factor equal to the number of Farey pieces was suppressed. |
| Energy deficit | Pass. The fourth-derivative secondary term gives (73.D12). The hybrid target is (73.D3); the derivative loss is \(J^{13/30}R^{-3/2}\), the spectral-trivial loss is \(J^{1/10}\), and neither is \(<1\) in the residual range. |
| Diagonal and near diagonal | Pass for the diagonal: \(BC\leq J^2/T\) for all \(C\leq J\). The Kuznetsov diagonal \(n=k\) is absent for large \(X\), since \(n\asymp Q^2\) and \(k=O(1)\). Nonzero near diagonals are retained in (73.D3), not deleted. |
| Analytic rank and aliases | Pass. The exact determinant is (73.D13), with the \(\eta=1/3\) locus outside the domain. Absolute summation of the two-dimensional Poisson aliases gives \(JQ\), so nondegeneracy alone is non-saving. The Bessel match restricts \(t^2\ll R\), and the Voronoi match creates the genuine length-\(T\) alias at \(m_0\asymp X\). |
| Inverse local unit | Pass in the odd formal reduction. The factor \(e_{4b}(k\bar c)\) is what produces \(S(n,k;4b)\); it is never replaced by arbitrary coefficients. The near-ray test also retains it. |
| Even local classes | Retained and open. Their lift units are constant only after fixing \(c\bmod4b\), and their spectral transforms require separate cusp data. No even estimate is inferred from the odd branch by a sign change. |
| Axes and gcds | Pass as a scoped audit. Equation (73.D18) removes axes only in power-separated subranges and leaves \(C\asymp J\) open. The exact ray \(c=Tb\) is rejected by \((b,c)=1\); \(S(n,k;q)\) retains all remaining gcd factors, with no Weil bound or Moebius loss used. |
| Perfect squares and fourth powers | Pass as a falsification control. The perfect-power model leading to (73.D14) has only divisor-capacity exact aliases. In (73.D9), a square or fourth-power value at the level-adjusted centre is included in the short \(m\)-window and receives no assumed cancellation. |
| Finite dual family and errors | Retained but not certified above the old boundary. The fixed \(k=O(1)\), two endpoint orientations, stationary \(n\)-family, nonstationary \(n\)-tails, singleton cells, and stationary remainders are explicit. Target-safe summation of the new transition and spectral errors is part of the first unproved seam. |
| Source hypotheses | No external result is imported as proved. Kuznetsov and Voronoi are used only as a best-case normalization/no-go calculation; exact source applicability is not asserted. |
| Self-return avoidance | Pass. The positive calculations do not repeat \(c\)-Poisson followed by its matching one-variable \(B\)-process. The report identifies that inverse Kuznetsov or a second Voronoi returns the same conductor/short-sum problem, so their gains cannot be multiplied by (73.7). |
| Downstream scope | Pass. The result concerns only the fixed-smooth-interior residual rows. It proves neither the residual nonaxial energy, cone edges, the complete wavelet, \(M9\!-\!M1\), \(M9\), nor a circle exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts/sources used

Only the assigned artifacts were used:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/briefs/hybrid_residue_energy_attack.md`;
* `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/derivation_packet.md`;
* `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/synthesis.md`;
* `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reviews/conductor_round72_adjudication.md`; and
* `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_reciprocal_energy_attack.md`.

The fourth-derivative estimate, Hessian calculation, stationary
normalization, conductor ledger, and perfect-power control are derived in
this report. No web source or unassigned artifact was consulted.

## 7. Recommended state effect

Retain (73.8) open and promote no new nonaxial conductor range. Record two
scoped no-go statements: the fourth-derivative \(A\)-process is blocked by
the \(C^{3/4}Q^{3/7}\) transition term, and a black-box combination of the
accepted third-derivative estimate with phase-matched Kuznetsov--Voronoi
preserves an \(X^{1/20}\) deficit and cannot multiply the two savings.

Revise the residual nonaxial target to the smaller actual-symbol
correlation (73.D8), or, after an exact level-four transition and cusp
seam, to (73.D3). A sufficient but stronger pointwise target is

\[
 \sum_{|m-m_0|\ll T}\lambda_f(m)\Omega_f(m)
 \ll_\varepsilon J^{1/2}X^\varepsilon
 \qquad(t_f^2\ll R),
\]

while the weakest target is the full signed spectral aggregate (73.D3),
including the continuous spectrum and actual transition weight. Record
separately that the energy diagonal is safe for all \(C\leq J\) and that
the axes are safe in fixed power-separated subranges by (73.D18); neither
fact closes the nonaxial survivor or the top axial band.

Do not promote the residual energy, the even spectral transforms, the
complete fixed-interior wavelet, \(M9\!-\!M1\), \(M9\), or any global
exponent.
