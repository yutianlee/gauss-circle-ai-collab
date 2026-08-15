## 1. Result

The packet's analytic mechanism is valid as a conditional lemma: recombination followed by the single partition in \(\alpha\) gives one central and one complementary copy; the three central selectors in (45.11) satisfy (45.12); the correctly oriented artificial residue satisfies (45.19); and a finite large-\(\alpha\) partition satisfying (45.21) recombines exactly to the direct complementary terminal.  No algebraic or quantitative obstruction occurs in the compact terminal or in the artificial-residue estimate.

This is not, from the statement-only packet, an unconditional proof of every asserted equality.  The finite-cell operators in (45.3), \(Q_{\rm ef}\), the arithmetic function \(F\) in (45.17), the ownership map in (45.5), and the large-\(\alpha\) theorem (45.22) are not defined or proved in the permitted material.  They can only be frozen hypotheses.  There is also a normalization ambiguity: Section 5 says that (45.22) includes the external factor, while item 5 says that the external operator is applied after the full vector is assembled.  The two statements are compatible only if (45.22) is explicitly typed as a bound for the already externalized image of the normalized complement.  Thus the verdict is **conditional verification, with revision required before unconditional promotion**.

There was no mathematical-isolation breach.

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi i z}\), let \(h,q\) range over positive integers subject to the finite restrictions retained in (45.11), and interpret the singular top share as the boundary value obtained when its positive real regularizer tends to zero.  Assume the following frozen inputs exactly as stated in the packet:

1. the finite linear identity (45.3), the ownership identity (45.5), and the recombined arithmetic identity (45.17);
2. uniform Schwartz seminorms for the normalized spatial profiles, a fixed-power \(b^{-1}\) loss in (45.2), and a uniform compact-set bound for \(\mathcal G\);
3. the finite, signed, one-count partition (45.21), and the large-\(\alpha\) theorem (45.22) for the same direct terminal with all listed metadata unchanged;
4. the usual implicit convention that the active scale indices are nonnegative integers satisfying \(H_j\geq1\).

Then, uniformly for \(1\leq x\leq N_X\),

\[
 |\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|
 \ll b^{-M}\log(2X)\ll\log^C(2X)
\]

for fixed constants \(M,C\).  Both artificial shares satisfy

\[
 |\mathfrak P_\rho[\chi _0]|+|\mathfrak P_\rho[1-\chi _0]|
 \ll b^{-M}\log^C(2X),
\]

and hence (45.19).  Moreover, by linearity and (45.21),

\[
 \sum_\tau \mathfrak T[\psi\eta_\tau Q_{\rm ef}]
 =\mathfrak T[\psi(1-\chi _0)Q_{\rm ef}],
\]

provided both sides are at the same normalization level.  The physical output is consequently to be written in the typed form

\[
 \mathcal E_X(\mathfrak V_{\rm ef}^{\,0}),\qquad
 \mathcal E_X(z)=-\frac{4X^{1/4}}{\pi}\Re\{e(1/8)z\},
\]

with \(\mathcal E_X\) occurring exactly once.  If (45.22) already denotes \(\mathcal E_X\) of the complementary normalized terminal, it must not be placed inside another \(\mathcal E_X\).

## 3. Proof or derivation

**Recombination and one-count localization.**  At finite truncation, (45.3) and linearity give

\[
 \sum_{k=1}^{16}\mathcal C_k[\psi Q_{\rm ef}]
 =R_uR_v[\psi Q_{\rm ef}]
 =R_uR_v[\psi\chi _0(\alpha)Q_{\rm ef}]
  +R_uR_v[\psi(1-\chi _0(\alpha))Q_{\rm ef}].
\]

This uses the identity \(\chi _0+(1-\chi _0)=1\) once and introduces no derivative of either cutoff, because no Stokes transfer is performed after the multiplication.  Localizing any one of the sixteen rows first would not justify discarding the cutoff derivatives produced by a subsequent transfer.  At the artificial pole, \(\alpha=\mu/2\), so the corresponding two artificial multipliers also add to one.  Thus the terminal and artificial partitions are both one-count partitions.

**The signed top functional.**  Put \(c_b=1+b/2\), \(\alpha=L+\beta\), \(y=\nu-L\).  Then

\[
 A=-c_b-i\alpha,\qquad D=A-iy/2.
\]

For a temporary positive regularizer \(\epsilon\), the top integral underlying (45.9) is

\[
 I_\epsilon=\frac{g}{2\pi}\int_{\mathbb R}
 \frac{p(\nu)}{(\epsilon+i(L-\nu))D(L,\nu)}\,d\nu.
\]

The boundary-value identity

\[
 \lim_{\epsilon\downarrow0}\frac1{\epsilon+i z}
 =\pi\delta_0(z)-i\,\operatorname {pv}\frac1z
\]

has the sign displayed here.  Also

\[
 \operatorname {pv}\int_{\mathbb R}
 \frac{d\nu}{(L-\nu)D(L,\nu)}=\frac{i\pi}{A}.
\]

Indeed,

\[
 -\frac1{y(A-iy/2)}=-\frac1{Ay}-\frac{i}{2A}\frac1{A-iy/2},
 \qquad
 \int_{\mathbb R}\frac{dy}{A-iy/2}=-2\pi.
\]

Subtracting \(p(L)\) in the principal-value integral now yields

\[
 \lim_{\epsilon\downarrow0}I_\epsilon
 =g\frac{p(L)}A-\frac{ig}{2\pi}
 \int_{\mathbb R}\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)}\,d\nu,
\]

which is exactly (45.9), including its full endpoint coefficient rather than a half coefficient.  A smooth spatial share has no boundary value and directly gives (45.10).  Consequently the three, and only three, selectors are the \(j=0\) Plemelj share, the \(j=0\) regular share, and the \(j\geq1\) interior share displayed in (45.11).

**Uniform compact bound.**  The supports of \(\psi(\beta)\) and \(\chi _0(L+\beta)\) put \((L,\beta)\) in a fixed compact set.  Hence \(|A|,|D|\geq c_b>1\), and all nonoscillatory factors in \(g\) are uniformly bounded.  It remains to control the apparent difference quotient in (45.9) uniformly in the real modulation parameter \(\gamma=\gamma_j(x)\).

Write \(\Phi(\nu)=\widehat\phi(b+i\nu)\) and \(p_\gamma(\nu)=e^{i\gamma\nu}\Phi(\nu)\).  Uniformly for compact \(L,\beta\) and every real \(\gamma\),

\[
 \left|\int_{\mathbb R}
 \frac{p_\gamma(\nu)-p_\gamma(L)}{(L-\nu)D(L,\nu)}\,d\nu\right|
 \ll \|\Phi\|_\infty+\|\Phi'\|_{L^\infty(L+[-1,1])}
       +\int_{\mathbb R}(1+|\nu|)^{-2}|\Phi(\nu)|\,d\nu.
\]

To see this, on \(|y|\leq1\) use

\[
 p_\gamma(L+y)-p_\gamma(L)
 =e^{i\gamma(L+y)}(\Phi(L+y)-\Phi(L))
  +e^{i\gamma L}\Phi(L)(e^{i\gamma y}-1).
\]

The first quotient is bounded by \(\Phi'\).  For the second, expand \(D^{-1}=A^{-1}+yR(y)\).  Its constant part is bounded uniformly because

\[
 \int_{-1}^{1}\frac{e^{i\gamma y}-1}{y}\,dy
 =2i\int_0^1\frac{\sin(\gamma y)}y\,dy=2i\operatorname {Si}(\gamma),
\]

and the sine integral is uniformly bounded; the remainder is absolutely bounded.  On \(|y|>1\), the original kernel is integrable because \(|yD|^{-1}\ll (1+y^2)^{-1}\) outside a fixed compact interval.  Estimate (45.2) therefore makes every \(\mathsf P_j\) and \(\mathsf S_j\) \(O(b^{-M})\), uniformly in \(x\); no bound on \(|\gamma_j(x)|\) is needed.

For the corrected phase in (45.8), direct differentiation gives

\[
 x\partial_x\{g(L,\beta)p_\gamma(\nu)\}
 =-i\xi_\nu g(L,\beta)p_\gamma(\nu),
 \qquad \xi_\nu=\frac{L+\nu}{2}+\beta.
\]

Thus (45.13) follows immediately from \(D=-c_b-i\xi_\nu\):

\[
 |\xi_\nu/D|\leq1.
\]

This proves the differentiated smooth-share bound by absolute integration.  For the Plemelj difference term, note that \(\xi_L=\alpha\) and

\[
 \xi_\nu p_\gamma(\nu)-\alpha p_\gamma(L)
 =\alpha\{p_\gamma(\nu)-p_\gamma(L)\}
   +\frac{\nu-L}{2}p_\gamma(\nu).
\]

The first term is controlled by the preceding modulation lemma and the second cancels the factor \(L-\nu\) and is absolutely integrable against \(D^{-1}\).  The first term \(gp(L)/A\) differentiates with multiplier \(-i\alpha\), which is bounded on the central support.  Hence both terms in (45.12) are \(O(b^{-M})\) before coefficient and scale summation.

The active-scale condition gives

\[
 2^{-j}\lfloor\sqrt X\rfloor\geq X^{1/4},
 \qquad 0\leq j\leq \tfrac14\log_2X+O(1).
\]

Moreover

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a\leq1,
 \qquad (H_j+1)^b\leq (2X^{1/4})^{1/\log(2X)}\ll1.
\]

For sufficiently large \(X\), \(r\geq9/8\) and \(p\geq5/4\).  Dropping only the finite equality/product restrictions therefore gives the legitimate majorant

\[
 \sum_{h,q\geq1}h^{-r}q^{-p}\leq\zeta(9/8)\zeta(5/4),
\]

while the \(j\)-sum costs only \(O(\log(2X))\).  This proves (45.12).

**Artificial pole and its orientation.**  If \(s_0=1/4-v/2\), then \(\rho=-(s-s_0)\).  Therefore

\[
 -\frac{\pi i\sqrt X}{\rho}I_1(\rho)
 =\frac{\pi i\sqrt X I_1(0)}{s-s_0}+O(1),
\]

which proves the positive sign in (45.16).  Since \(t=-\nu/2\) at \(s=s_0\), the coordinate calculation gives

\[
 \alpha_\rho=\mu/2,\qquad \beta_\rho=-\mu/2-\nu,
\]

as in (45.14).  The radial coefficient is not merely bounded but is an exact endpoint difference:

\[
 I_1(0)=2\int_1^{\sqrt{N_X}}e(\sqrt X y)\,dy
 =\frac{e(\sqrt{XN_X})-e(\sqrt X)}{\pi i\sqrt X},
\]

so

\[
 \pi i\sqrt X I_1(0)=e(\sqrt{XN_X})-e(\sqrt X),\qquad
 |\pi i\sqrt X I_1(0)|\leq2.
\]

This also verifies that no spurious \(X^{1/2}\) loss is present.

**Artificial arithmetic chamber and integrability.**  On the support of \(\psi(\beta_\rho)\),

\[
 \Im\!\left(\frac34+\frac u2+v\right)=\frac\mu2+\nu=-\beta_\rho
\]

is confined to a fixed compact interval.  Its real part \(3/4+a/2+b\) is, for large \(X\), in a compact interval strictly below \(1\).  Hence the zeta factor in (45.17) is uniformly bounded and is never sampled near its pole.  For the other factor, if \(A(t)=\sum_{n\leq t}\chi _4(n)\), then \(A(t)\) is bounded and Abel summation gives, for \(\sigma>0\),

\[
 L(\sigma+i\tau,\chi _4)
 = (\sigma+i\tau)\int_1^\infty A(t)t^{-\sigma-i\tau-1}\,dt,
\]

up to the harmless initial endpoint convention.  Consequently

\[
 |L(\sigma+i\tau,\chi _4)|\ll_\sigma1+|\tau|,
\]

which proves (45.20) on the stated compact \(\sigma\)-interval.

Now \(\psi(-\mu/2-\nu)\neq0\) implies \(\nu=-\mu/2+O(1)\).  Away from a fixed neighborhood of \(\mu=0\), the singular top share is therefore bounded, apart from a power of \(b^{-1}\), by

\[
 \frac1{|\mu|}(1+|\mu|)(1+|\nu|)^{-3}
 \ll (1+|\mu|)^{-3}.
\]

This is integrable.  The regular shares are even smaller because their spatial profiles are Schwartz.  The scale factors have bounded modulus and their sum costs \(O(\log(2X))\), exactly as above.  No \(h,q\) expansion is made on this residue.

For the central singular artificial share, collect every factor other than \((a+i\mu)^{-1}\) into \(F_a(\mu)\).  Its support in \(\mu\) is compact, and its \(C^1\) norm is at most a fixed power of \(\log(2X)\); this follows from the stated smoothness, the compact zeta chamber, Abel summation locally for \(L\), and the scale-phase bounds.  The signed boundary value is

\[
 \lim_{a\downarrow0}\int_{\mathbb R}\frac{F_a(\mu)}{a+i\mu}\frac{d\mu}{2\pi}
 =\frac12F_0(0)-\frac{i}{2\pi}\operatorname {pv}
   \int_{\mathbb R}\frac{F_0(\mu)}\mu\,d\mu.
\]

Subtracting \(F_0(0)\) against a fixed even cutoff proves a \(C^1\)-norm bound for the principal value.  For \(1-\chi _0(\mu/2)\), the multiplier vanishes on a fixed neighborhood of zero, so the preceding absolute tail estimate applies and no principal value is needed.  Together with the bounded radial endpoint coefficient, this proves (45.19).

**Large-\(\alpha\) seam.**  Because the accepted partition is finite and the direct terminal is linear in its cutoff,

\[
 \sum_\tau\mathfrak T[\psi\eta_\tau Q_{\rm ef}]
 =\mathfrak T\!\left[\psi\left(\sum_\tau\eta_\tau\right)Q_{\rm ef}\right]
 =\mathfrak T[\psi(1-\chi _0)Q_{\rm ef}].
\]

This is exactly the complement produced after (45.3), not a new transfer.  Hence there is no cutoff connector.  The equality also preserves the three selectors, floors, stars, character, and residue ownership if, as the frozen interface states, those objects are identical cell by cell.  Equation (45.22) then supplies the analytic estimate; it is not reproved by the packet.

Finally, define the normalized assembled vector before physical scaling and apply \(\mathcal E_X\) to that vector once.  Linearity over real sums permits estimating its central, complementary, and artificial pieces separately, but it does not permit nesting a second copy of \(\mathcal E_X\).  Axial, corner, and collision terms can occur only in their declared owner and are absent from the three terminal selectors and the artificial coefficient above.

## 4. First doubtful or unproved step

The first unproved assertion is (45.3) itself.  The permitted packet names \(\mathcal C_k\), \(R_uR_v\), and \(Q_{\rm ef}\), but gives none of their definitions, boundaries, orientations, or connector terms.  Thus a statement-only reader cannot independently establish the sixteen-cell Stokes identity; one can only prove that, **if** it holds, recombine-before-localize is the lawful order.

After accepting (45.3) as frozen input, the first material ambiguity is normalization at the large-\(\alpha\) seam.  The phrase in Section 5 that (45.22) has the external factor and the instruction in item 5 to apply that factor after full assembly must be typed as described in Sections 1--2 above.  Otherwise the claim that the left side of (45.22) is “exactly” the unexternalized terminal complement is false by a factor and a real-part operation.  Also, the packet does not state the radial kernel for the compact terminal or a growth bound for \(N_X\), so its sentence asserting a complete radial integration-by-parts estimate cannot be reconstructed from (45.12) alone.  None of these omissions refutes the compact or artificial estimates proved above, but they prevent an unconditional exactness certification.

## 5. Control tests and outcomes

1. `aggregate_stokes_before_localization`: **pass conditional on (45.3)**.  Linearity gives exactly two aggregate shares; no rowwise physical limit was used.
2. `alpha_partition_one_count`: **pass**.  The two cutoffs add to one both on the direct line and at \(\alpha_\rho=\mu/2\).
3. `three_terminal_selectors`: **pass**.  The Plemelj top, \(j=0\) regular, and \(j\geq1\) smooth terms are the only shares in (45.11).
4. `signed_plemelj_before_absolute_values`: **pass**.  The distribution sign and the principal-value constant give the full coefficient \(gp(L)/A\).  Taking absolute values before this calculation would lose the cancellation.
5. `artificial_radial_residue`: **pass**.  Since \(d\rho/ds=-1\), the residue is \(+\pi i\sqrt X I_1(0)\), and that coefficient is the bounded endpoint difference displayed above.
6. `artificial_arithmetic_chamber`: **pass conditional on (45.17)**.  The beta mask makes the zeta height compact, while Abel summation and height-transform decay make the \(L\)-factor tail integrable.  No termwise \(h,q\) replacement was used.
7. `large_alpha_positive_line_match`: **pass as a frozen seam, with a normalization qualification**.  Equation (45.21) gives exact recombination by linearity; (45.22) itself is an assumed analytic theorem.
8. `compact_x_derivative`: **pass**.  The corrected combined phase gives exactly \(-\xi_\nu\), \(|\xi_\nu/D|\leq1\), and the differentiated Plemelj numerator retains the necessary cancellation.
9. `coefficient_and_scale_sums`: **pass under the packet's implicit positive-integer index convention**.  The \(h,q\) sums are uniformly convergent and there are \(O(\log X)\) active scales with bounded weights.
10. `collision_corner_and_external_once`: **qualified pass**.  No duplicate collision/axis coefficient appears in the displayed terminal or artificial formulas.  The external operator is one-count under the typed normalization in Section 2; the packet's wording should be revised to make that typing explicit.

No numerical or experimental control was used.

## 6. Dependencies and exact artifacts used

The only mathematical artifacts read were:

- `rounds/codex-managed/m9-m1-beta-positive-line-localization/briefs/isolated_positive_line_rederivation.md`;
- `rounds/codex-managed/m9-m1-beta-positive-line-localization/derivation_packet.md`.

I also used the coordinator's formatting-only correction that (45.8) has phase
\(e^{iL\log(D_j/(2q\sqrt{Xx}))-i\beta\log(hqx)}\).  No proof graph, proof draft, prior report, synthesis, other Round-45 report, web source, or numerical computation was read or used.  System-supplied operating instructions were treated only as operating instructions and not as mathematical evidence.

## 7. Recommended state effect

**Revise.**  Retain the compact-terminal estimate, the oriented artificial-residue estimate, and the one-count seam derivation as valid conditional evidence.  Before promotion, add or cite the exact definitions that certify (45.3), (45.5), and (45.17); mark (45.22) explicitly as a frozen imported theorem; state the compact radial kernel and the needed size condition on \(N_X\); and type (45.22) unambiguously as either normalized or already acted on by \(\mathcal E_X\).  Once those seams are supplied, this rederivation finds no remaining analytic obstruction.
