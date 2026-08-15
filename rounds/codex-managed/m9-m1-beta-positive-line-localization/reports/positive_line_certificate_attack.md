## 1. Result

**Result (proved analytic core; conditional full certificate).** Complete finite product Stokes recombination must precede the \(\alpha\)-split. The resulting central terminal is exactly the three-selector functional (45.11), and

\[
 \sup_{1\le x\le N_X}
 \bigl(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\bigr)
 \ll \log^C(2X).
\]

The oriented artificial residue has sign \(+\pi i\sqrt X I_1(0)\), with the exact evaluation

\[
 \pi i\sqrt X I_1(0)=e(\sqrt{XN_X})-e(\sqrt X),
\]

and both its central and complementary \(\alpha\)-shares are \(O(\log^C(2X))\) on the normalized scale. No transfer connector is created by the positive-line split. Endpoint/arithmetic modules, the artificial residue, axial/corner/collision shares, radial endpoint coefficients, and the external factor are each owned once.

The compact terminal and the complete artificial residue are therefore physically \(O(X^{1/4}\log^C(2X))\). The full certificate is nevertheless **not established from the permitted artifacts**: the accepted Round-41 node estimates signed large-alpha saddle, entry, and exit cells, but the artifacts do not construct an exact finite partition summing to \(1-\chi _0\) on the direct complement or account explicitly for every remaining nonsaddle tail. The complementary terminal, and hence the whole localized positive-line vector, is target-safe only conditional on that missing partition-and-coverage antecedent.

## 2. Exact statement and hypotheses

Let \(X\) be sufficiently large,

\[
 b=\frac1{\log(2X)},\qquad 0\le a\le b,\qquad
 r=\frac54-\frac{a+b}{2},\qquad
 p=\frac54+\frac{a+b}{2},
\]

and assume the strict terminal chamber

\[
 a+b<\frac12,\qquad \frac a2+b<\frac14.
\]

Use the compact beta mask \(\psi\), the central cutoff \(\chi _0\), the active scales \(D_j=2^{-j}\lfloor\sqrt X\rfloor\), \(H_j=\lfloor D_jX^{-1/4}\rfloor\ge1\), the exact floors, equality conventions, stars, character, and normalized profiles of the packet. The actual height transform and its first two derivatives satisfy (45.2), with only polynomial \(b^{-1}\) loss. The compact double-gamma quotient and the required compact derivatives are bounded. In (45.8) I use the corrected phase

\[
 e^{iL\log(D_j/(2q\sqrt{Xx}))-i\beta\log(hqx)}.
\]

At every finite \((U,V,S)\), assume the proved product identity (45.3), the endpoint-free decomposition (45.5), and common one-count collision ownership. For the *conditional* complement conclusion, add the antecedent

\[
 \tag{H_{\rm LA}}
 \sum_\tau\eta_\tau(\alpha)=1-\chi _0(\alpha)
\]

on the same direct positive-line endpoint-free terminal, with a finite one-count family covering both saddle signs, entry/exit collars, and every nonsaddle completion, all with the same profiles and normalization. The derivation packet requests this antecedent, but the accepted Round-41 graph node in the permitted artifacts does not itself establish it.

Then:

1. the finite split after recombination is exact;
2. the central terminal is (45.11) and satisfies (45.12);
3. for \(c\in\{\chi _0,1-\chi _0\}\), the separately owned artificial functional defined by (45.16)--(45.18) satisfies \(|\mathfrak P_\rho[c]|\ll\log^C(2X)\);
4. conditional on \((H_{\rm LA})\), the complementary terminal is exactly \(\sum_\tau\mathfrak T[\psi\eta_\tau Q_{\rm ef}]\);
5. the physical operator \(-4X^{1/4}\Re\{e(1/8)(\cdot)\}/\pi\) is applied once, after normalized assembly.

## 3. Proof or derivation

**Finite recombination and localization.** At fixed finite heights, (45.3) is an equality of linear finite functionals. Therefore

\[
\begin{aligned}
 \sum_{k=1}^{16}\mathcal C_k[\psi Q_{\rm ef}]
 &=R_uR_v[\psi Q_{\rm ef}]\\
 &=R_uR_v[\psi\chi _0(\alpha)Q_{\rm ef}]
   +R_uR_v[\psi(1-\chi _0(\alpha))Q_{\rm ef}].
\end{aligned}
\]

This is multiplication on the already returned positive lines, not another contour transfer. Hence there are no \(\chi _0'\) or \(\chi _0''\) connectors. In particular the indispensable \(\psi''/4\) product-area row has already been absorbed into the complete Stokes sum. Linearity gives the same central/complementary split of the separately owned artificial coefficient. Any inherited combined collision coefficient is multiplied by \(\chi _0+(1-\chi _0)=1\), so it is partitioned rather than duplicated.

**Exact three-selector central terminal.** The spatial identity (45.1) has precisely the three physical classes

\[
 j=0\text{ singular }u^{-1},\qquad
 j=0\text{ regular }\widehat W_{0,r},\qquad
 j\ge1\text{ interior }\widehat W_j.
\]

Only the first class is subjected to the signed top limit. To check the normalization in (45.9), put

\[
 A=A(L),\qquad y=L-\nu,\qquad D(L,\nu)=A+\frac{i y}{2}.
\]

The normalized Plemelj formula is

\[
 \frac1{2\pi}\frac1{0^++i\mu}
 =\frac12\delta_0(\mu)-\frac{i}{2\pi}\operatorname{PV}\frac1\mu.
\]

Moreover, since \(\Re A<0\), direct integration on the common continuous branch gives

\[
 \operatorname{PV}\int_{\mathbb R}
 \frac{d\nu}{(L-\nu)D(L,\nu)}
 =\operatorname{PV}\int_{\mathbb R}
 \frac{dy}{y(A+iy/2)}=\frac{i\pi}{A}.
\]

Indeed

\[
 \frac1{y(A+iy/2)}=\frac1{Ay}-\frac{i}{2A}\frac1{A+iy/2},
 \qquad \int_{\mathbb R}\frac{dy}{A+iy/2}=-2\pi.
\]

Thus the delta half and the constant part of the PV integral add to one full diagonal value, leaving

\[
 \frac{gp(L)}A-\frac{ig}{2\pi}
 \int_{\mathbb R}\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)}\,d\nu,
\]

which is exactly \(\mathsf P_j\). The other two selector classes are ordinary \(\mu\)-integrals and give exactly the two \(\mathsf S_j\) terms. The two residual contour measures are \(dL\,d\beta/(2\pi)^2\), so (45.11), including its factor \(-\pi i\), is the central terminal and contains no artificial, axial, connector, or boundary module a second time.

**Compact value and one-\(x\)-derivative bound.** On the support of \(\psi(\beta)\chi _0(L+\beta)\), both \(L\) and \(\beta\) range over fixed compact sets. Also

\[
 |A(L)|\ge1+\frac b2,\qquad
 |D(L,\nu)|^2=\left(1+\frac b2\right)^2+\left(\frac{L+\nu}{2}+\beta\right)^2.
\]

For every active scale,

\[
 |\gamma_j(x)|\ll\log(2X),
\]

uniformly for \(1\le x\le N_X\). Hence (45.2) gives the needed uniform bounds for \(p\) and its first two \(\nu\)-derivatives with a polylogarithmic loss.

For the value of \(\mathsf P_j\), the divided difference is continuous at \(\nu=L\), while for large \(|\nu|\) its integrand is \(O(\langle\nu\rangle^{-2})\): the nondecaying \(-p(L)\) is accompanied by both \(L-\nu\) and \(D(L,\nu)\). Thus \(\mathsf P_j\ll\log^C(2X)\). Every \(\mathsf S_j\) is absolutely bounded by (45.2) and the rapid decay of the relevant spatial profile.

For the derivative, write

\[
 z_\nu=\frac{L+\nu}{2}+\beta,\qquad z_L=L+\beta.
\]

The corrected exact phase gives

\[
 x\partial_x(gp(\nu))=-iz_\nu gp(\nu),\qquad
 x\partial_x(gp(L))=-iz_Lgp(L).
\]

For a smooth selector, \(|z_\nu/D(L,\nu)|\le1\), which directly bounds the differentiated integral. For the hard divided difference one must keep the endpoint cancellation intact:

\[
 x\partial_x\{g(p(\nu)-p(L))\}
 =-ig\{z_\nu p(\nu)-z_Lp(L)\}.
\]

Near \(\nu=L\), the quotient by \(L-\nu\) is the derivative of the smooth function \(z_\nu p(\nu)\); at infinity its numerator is a constant plus \(O(\langle\nu\rangle^{-2})\), while \((L-\nu)D(L,\nu)\asymp\nu^2\). It is therefore absolutely integrable with polylogarithmic norm. This recombined argument is essential: splitting off a separate \(p(L)/D\) term would manufacture two cancelling \(1/\nu\) tails. The diagonal derivative is bounded by \(|z_L/A(L)|\le1\). Consequently every bracketed selector in (45.11), together with its \(x\)-derivative, is \(O(\log^C(2X))\).

For sufficiently large \(X\), \(r,p\ge1+\delta\) for a fixed \(\delta>0\). Dropping only the finite product/equality restrictions for an upper bound gives

\[
 \sum_{h,q}h^{-r}q^{-p}\ll1.
\]

There are \(O(\log X)\) active scales, and

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a\le1,
 \qquad (H_j+1)^b\ll1.
\]

Thus the coefficient and scale sums cost only a further polylogarithm, proving (45.12).

For completeness, the normalized radial functional is handled locally, without invoking the unmasked endpoint module:

\[
 \sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})\mathcal A_{\rm db}(x)\,dx.
\]

Since \(d e(\sqrt{Xx})=\pi i\sqrt Xx^{-1/2}e(\sqrt{Xx})\,dx\), one integration by parts gives full continuous boundary coefficients and an integral bounded by

\[
 \int_1^{N_X}\left(x^{-2-b/2}|\mathcal A_{\rm db}(x)|
 +x^{-1-b/2}|\mathcal A'_{\rm db}(x)|\right)dx
 \ll\log^C(2X).
\]

No new half weight is created.

**Oriented artificial residue and exact radial evaluation.** Since

\[
 \rho=\frac14-s-\frac v2=-(s-s_0),
\]

the factor \(-\pi i\sqrt X I_1(\rho)/\rho\) has oriented \(s\)-residue

\[
 +\pi i\sqrt X I_1(0).
\]

With \(y=\sqrt{Xx}\),

\[
 I_1(0)=\int_1^{N_X}x^{-1/2}e(\sqrt{Xx})\,dx
 =\frac{e(\sqrt{XN_X})-e(\sqrt X)}{\pi i\sqrt X},
\]

so the exact radial residue coefficient is

\[
 e(\sqrt{XN_X})-e(\sqrt X),
\]

of modulus at most \(2\).

The arithmetic factor must remain

\[
 Z(\mu,\nu)=
 \zeta\!\left(\frac34+\frac a2+b+i\left(\frac\mu2+\nu\right)\right)
 L\!\left(\frac34-\frac a2-\frac{i\mu}{2},\chi _4\right).
\]

On the support of \(\psi(-\mu/2-\nu)\), the zeta height \(\mu/2+\nu=-\beta_\rho\) is compact; its real part stays in a compact subset of \((0,1)\) away from the pole by \(a/2+b<1/4\). Hence the zeta factor is uniformly bounded. If \(A(t)=\sum_{n\le t}\chi _4(n)\), then \(|A(t)|\le1\), and Abel summation gives, uniformly for \(\sigma\) in the required compact interval,

\[
 L(\sigma+i\tau,\chi _4)
 = (\sigma+i\tau)\int_1^\infty A(t)t^{-\sigma-i\tau-1}\,dt
 \ll 1+|\tau|.
\]

Thus \(|Z(\mu,\nu)|\ll1+|\mu|\).

For the central share \(c=\chi _0\), \(\mu\) is compact and the beta mask then makes \(\nu\) compact. The singular top is exactly its signed Plemelj distribution acting on a compact smooth test function; all test seminorms, including scale phases, are polylogarithmic. The regular top and interior selectors are ordinary compact integrals.

For \(c=1-\chi _0\), the cutoff vanishes on a fixed neighborhood of \(\mu=0\), so the singular top may be bounded ordinarily by \(|\mu|^{-1}\). The beta mask forces \(\nu=-\mu/2+O(1)\). Using (45.2), the singular-share tail is

\[
 |\mu|^{-1}(1+|\mu|)(1+|\nu|)^{-3}\ll(1+|\mu|)^{-3},
\]

and is integrable. Every regular spatial share has additional rapid \(\mu\)-decay. Finally,

\[
 \sum_j\left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \ll\log(2X).
\]

This proves (45.19) without a termwise \(h,q\) expansion on the residue line. The strict arithmetic chamber also excludes an arithmetic-pole collision there.

**Conditional large-alpha match.** If \((H_{\rm LA})\) holds on the already returned positive line, finite linearity gives the exact pre-normalization identity

\[
 \mathfrak T[\psi(1-\chi _0)Q_{\rm ef}]
 =\sum_\tau\mathfrak T[\psi\eta_\tau Q_{\rm ef}].
\]

Under that antecedent, both sides contain the same three selectors, beta mask, floors, stars, character, contour constants, radial integration, and finite equality conventions. The artificial residue is absent from both sides because it was split and estimated as \(\mathfrak P_\rho\); the endpoint/arithmetic and axial/corner/collision modules were routed before this terminal identity. Thus \((H_{\rm LA})\), together with estimates for every one of its cells, would make the accepted large-alpha estimate apply literally and would complete the proof after the external physical operator is applied once.

The permitted artifacts do not prove \((H_{\rm LA})\). They certify the signed saddle/entry/exit package, but not an explicit finite identity covering all of \(1-\chi _0\) and its remaining nonsaddle tails. Hence the displayed equality is a conditional seam calculation, not a certification of the full complement.

## 4. First doubtful or unproved step

**Scope addendum.** The first unproved step is \((H_{\rm LA})\): one must construct the exact finite one-count partition of the direct terminal complement, prove that it sums to \(1-\chi _0\) with no transferred connector or duplicated module, and show that the accepted large-alpha estimates cover every resulting cell, including the nonsaddle tails. The packet states this as the desired interface; it is not, by itself, accepted evidence. The Round-41 graph node proves the signed saddle/entry/exit estimates but does not supply the missing partition-and-coverage theorem. Therefore the large-alpha complement control remains conditional.

The compact terminal estimate, its \(x\)-derivative, and both artificial-residue shares do not use this missing antecedent and remain proved. Beyond this seam, the alpha-bounded zeta-high branch and final complete transition assembly remain open; nothing here proves M9-M1, M9, or the Gauss-circle target.

## 5. Control tests and outcomes

| Control | Outcome | Reason |
|---|---|---|
| `aggregate_stokes_before_localization` | PASS | All sixteen finite cells, including \(\psi''/4\), are first returned to \(R_uR_v[\psi Q_{\rm ef}]\). |
| `alpha_partition_one_count` | PASS | \(\chi _0+(1-\chi _0)=1\) is inserted only on the returned positive lines; no cutoff derivative is generated. |
| `three_terminal_selectors` | PASS | The exact classes are singular \(j=0\), regular \(j=0\), and ordinary \(j\ge1\); only the first uses Plemelj. |
| `signed_plemelj_before_absolute_values` | PASS | The diagonal half plus the PV constant equals the full \(gp(L)/A\); the remaining divided difference is absolutely integrable. |
| `artificial_radial_residue` | PASS | Orientation gives \(+\pi i\sqrt XI_1(0)\), exactly \(e(\sqrt{XN_X})-e(\sqrt X)\). |
| `artificial_arithmetic_chamber` | PASS | The zeta factor has compact height away from its pole; the character \(L\)-factor is bounded by period-four Abel summation; no residue-line Dirichlet expansion is used. |
| `large_alpha_positive_line_match` | OPEN / CONDITIONAL | The equality follows from \((H_{\rm LA})\), but the permitted accepted artifacts do not construct the partition or cover all nonsaddle tails. |
| `compact_x_derivative` | PASS | The exact phase gives \(z_\nu\); the hard derivative is kept as the recombined divided difference, avoiding false separate \(1/\nu\) tails. |
| `coefficient_and_scale_sums` | PASS | \(r,p>1\) uniformly, the \(h,q\) sums are bounded, each scale weight is \(O(1)\), and there are \(O(\log X)\) scales. |
| `collision_corner_and_external_once` | PASS | Combined collision coefficients are partitioned, not copied; routed axes/corners/modules are not reinserted; radial endpoints have full coefficients; the external \(X^{1/4}\) operator is applied once. |

No numerical experiment and no external theorem were used.

## 6. Dependencies and exact artifacts used

The proof uses only the task brief and the permitted context:

- `protocol.md`;
- `state/proof_obligations.yml` at graph hash `45b0c54cad320dc5a08b1129f5a7b4776f6b9e321b3c1c7c9fa738bcb85c5196`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-beta-positive-line-localization/derivation_packet.md`, with the communicated correction to (45.8);
- `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md`;
- `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`;
- `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md`;
- `rounds/codex-managed/m9-m1-beta-double-bounded-cell/synthesis.md`;
- `rounds/codex-managed/m9-m1-beta-compact-selector-ownership/synthesis.md`.

The exact accepted dependencies used for the proved core are the finite product Cauchy--Green identity, the fixed endpoint-free Plemelj vector and its positive-line limit, aggregate-before-localization ownership, and the conditional compact radial-BV reduction. The Round-41 large-alpha package is used only for its graph-certified saddle/entry/exit scope; the stronger partition-and-nonsaddle coverage antecedent is explicitly not treated as accepted. Neither other Round-45 report was read.

## 7. Recommended state effect

**Promote only the scoped compact/artificial analytic lemma**: after aggregate-before-localization, (45.11) is the exact lawful central functional, (45.12) is proved, the local radial-BV reduction makes it target-safe, and both oriented artificial shares satisfy (45.19) with the exact radial coefficient.

Retain `M9-M1-beta-positive-line-alpha-localization-certificate` open at the large-alpha partition-and-nonsaddle-coverage interface. Because the current `M9-M1-beta-double-bounded-cell-bound` node explicitly depends on that complete certificate, retain that full node open as well unless the conductor splits off the proved compact analytic sublemma. Retain the complete beta-transition assembly, the alpha-bounded zeta-high branch, M9-M1, M9, and the Gauss-circle target open. Do not revive the rejected rowwise sixteen-stratum selector table.
