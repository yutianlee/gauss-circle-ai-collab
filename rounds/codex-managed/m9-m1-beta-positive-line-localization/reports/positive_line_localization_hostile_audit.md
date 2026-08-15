## 1. Result

**Partial certification lemma (hostile seam audit).** Assume the exact finite
endpoint-free identity (45.3), the positive-line definitions and selector
decomposition (45.1), (45.6)--(45.11), the already-routed one-count
collision/corner convention. Uniformly for

\[
b=\frac1{\log(2X)},\qquad 0\leq a\leq b,
\]

with \(X\) sufficiently large, recombine-before-localize gives the exact
one-count decomposition

\[
\mathfrak V_{\rm ef}
=\mathfrak T_0+\mathfrak T_\infty
 +\mathfrak P_{\rho,0}+\mathfrak P_{\rho,\infty},
\]

where the subscripts are respectively \(\chi _0(\alpha)\) and
\(1-\chi _0(\alpha)\). The central terminal is exactly the three-selector
functional (45.11), and

\[
\sup_{1\le x\le N_X}
 \bigl(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\bigr)
 \ll \log ^C(2X).
\]

The local oriented residue is

\[
\operatorname {Res}_{s=1/4-v/2}R_{1,v}(1-s)
=+\pi i\sqrt X\,I_1(0)
=e(\sqrt{XN_X})-e(\sqrt X),
\]

so both artificial shares are \(O(\log ^C(2X))\) on the normalized
scale. No tested local seam produced a counterexample. In particular,
there is no missing half-weight, no termwise residue series, no fourth
selector, and no second external \(X^{1/4}\) factor.

The full localization certificate is **not** certified by the permitted
accepted state. Round-45 algebra proves that any finite signed family
satisfying (45.21) on the same positive-line antecedent would equal the
terminal complement. The accepted Round-41 node, however, states a
complete signed saddle/entry/exit package without displaying a finite
partition whose sum is \(1-\chi _0\), and without separately stating
quantitative coverage of all remaining nonsaddle tails. Thus the
large-alpha equality and coverage are a still-open mathematical interface,
not merely a harmless labeling omission.

## 2. Exact statement and hypotheses

The proof uses the following hypotheses. Items 1--5 and the normalization
in item 7 are accepted inputs; item 6 is isolated explicitly as the
additional hypothesis needed for the unresolved full-certificate
implication.

1. At fixed \(U,V,S\), all sixteen product Cauchy--Green cells have one
   common endpoint-free antecedent, all common collisions use their single
   combined coefficient, and

   \[
   \sum_{k=1}^{16}\mathcal C_k[\psi Q_{\rm ef}]
     =R_uR_v[\psi(\beta)Q_{\rm ef}].
   \]

   No limit or physical ownership is assigned to a summand on the left.

2. The alpha split is made only on the returned positive line. If either
   summand is subsequently transferred, the corresponding cutoff
   derivatives must be restored; no such retransfer is used here.

3. The spatial Mellin family is precisely

   \[
   \widehat W_0(u)=u^{-1}+\widehat W_{0,r}(u),
   \qquad \widehat W_j(u)\quad(j\geq1).
   \]

   The first term alone is interpreted by the signed \(a\downarrow0\)
   Plemelj functional. The other two classes use ordinary
   \(\mu\)-integration. Their normalized seminorms, and the seminorms of
   the exact compact gamma quotient, cost at most a power of
   \(b^{-1}=\log(2X)\). The actual height profile has the cubic decay
   (45.2). The physical value \(N_X=\lfloor16\sqrt X\rfloor\) from the
   accepted state makes every logarithmic modulation below
   \(O(\log(2X))\).

4. All original \(h,q,j\) restrictions, equality half-stars, floors,
   \(\chi _4(q)\), and profiles stay attached. They may be discarded only
   after taking absolute values for an upper bound.

5. The artificial residue is kept arithmetically recombined as (45.17).
   The contour chamber satisfies, for sufficiently large \(X\),
   \(a+b<1/2\) and \(a/2+b<1/4\). The latter also keeps the zeta argument
   at the artificial pole uniformly away from \(1\).

6. For the conditional large-alpha implication only, suppose that the
   accepted endpoint-free terminal cells after endpoint, side, arithmetic,
   artificial, axial, collision, connector and corner ownership form a
   finite signed family obeying

   \[
   \sum_\tau\eta_\tau(\alpha)=1-\chi _0(\alpha)
   \]

   on that same direct positive-line integrand, and suppose its quantitative
   theorem covers both signs, entry and exit collars, and every
   nonstationary remainder. These are the exact additional hypotheses
   needed for the full certificate; they are not explicit conclusions of
   the accepted Round-41 node.

7. The external real-linear operator is typed separately as

   \[
   \mathcal E_X Z=-\frac4\pi X^{1/4}
      \Re\{e(1/8)Z\}.
   \]

   All estimates called “normalized” are estimates before
   \(\mathcal E_X\). The accepted Round-41 physical estimate applies to its
   named package. It becomes \(\mathcal E_X(\mathfrak T_\infty)\), rather
   than a new normalized summand, only after item 6 is proved.

## 3. Proof or derivation

**Operator order and one count.** Finite linearity gives, only after the
complete Stokes sum has returned to the original positive lines,

\[
R_uR_v[\psi Q_{\rm ef}]
=R_uR_v[\psi\chi _0 Q_{\rm ef}]
 +R_uR_v[\psi(1-\chi _0)Q_{\rm ef}].
\]

This is multiplication on the positive-line representative, so no
\(\chi _0'\) or \(\chi _0''\) term is generated. The mixed
\(\frac14A_uA_v[\psi''Q_{\rm ef}]\) has already done its finite Stokes job
inside the sum in (45.3); it is neither deleted nor copied into either
positive-line share. Conversely, inserting \(\chi _0\) in each transferred
row would differentiate it and would be a different operator. Thus the
order in the packet is the only one among these two procedures that gives
the displayed connector-free split.

The three selectors in (45.11) are disjoint and exhaustive: \(j=0\),
singular \(u^{-1}\); \(j=0\), regular \(\widehat W_{0,r}\); and \(j\geq1\),
interior \(\widehat W_j\). The first is \(\mathsf P_j\), and the latter two
are the two occurrences of \(\mathsf S_j\). Thus no Plemelj regularizer is
applied to a smooth profile, and no \(j=0\) regular profile is silently
identified with a \(j\geq1\) profile. Leaving the actual finite restrictions
inside the \(j,h,q\) sum preserves every floor, star, equality convention
and character exactly; replacing the restricted sum by unrestricted
positive \(h,q\) sums occurs only in the majorant below.

**Signed hard top.** For fixed compact \(L,\beta\), write

\[
A=-1-\frac b2-i(L+\beta),\qquad
D(L,\nu)=A+\frac i2(L-\nu).
\]

The normalized distribution is

\[
\frac1{2\pi}\frac1{0^++i(L-\nu)}
=\frac12\delta_L(\nu)-\frac i{2\pi}
 \operatorname {PV}\frac1{L-\nu}.
\]

Moreover, on the full line,

\[
\operatorname {PV}\int_{\mathbb R}
 \frac{d\nu}{(L-\nu)D(L,\nu)}
=\frac{i\pi}{A}.
\]

Indeed, with \(y=L-\nu\),

\[
\frac1{y(A+iy/2)}
=\frac1{Ay}-\frac{i}{2A(A+iy/2)},
\qquad
\int_{\mathbb R}\frac{dy}{A+iy/2}=-2\pi,
\]

because \(\Re A<0\). The delta contributes \(p(L)/(2A)\), and the
constant part of the PV integral contributes the other \(p(L)/(2A)\).
The remainder is exactly the divided difference in (45.9), including its
minus sign and factor \(1/(2\pi)\). This proves the displayed
\(\mathsf P_j\) formula before any absolute value is taken.

**Compact value and physical-height derivative.** On
\(\operatorname {supp}\psi(\beta)\operatorname {supp}\chi _0(L+\beta)\),
both \(L\) and \(\beta\) range over a fixed compact set, while

\[
|A|\geq1+b/2,\qquad |D(L,\nu)|\geq1+b/2.
\]

The corrected phase (45.8), together with (45.7), gives exactly

\[
x\partial_x\{g(L,\beta)p(\nu)\}
=-i\theta_\nu g(L,\beta)p(\nu),
\qquad
\theta_\nu=\frac{L+\nu}{2}+\beta,
\]

and

\[
\left|\frac{\theta_\nu}{D(L,\nu)}\right|\leq1.
\]

In particular, the \(L\)-phase contributes \(-L/2\), the beta phase
contributes \(-\beta\), and the exact height modulation contributes
\(-\nu/2\); omitting any one makes (45.13) false.

Let \(P_X\ll\log^C(2X)\) absorb the allowed profile and compact gamma
seminorms. Since

\[
\gamma_j(x)=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}
=O(\log(2X)),
\]

the cubic profile bound gives, with one \(\nu\)-derivative,

\[
|p(\nu)|\ll P_X(1+|\nu|)^{-3},
\qquad |p'(\nu)|\ll P_X(1+|\nu|)^{-3}.
\]

For \(|\nu-L|\leq1\), the divided difference in (45.9) is bounded by
\(\sup|p'|\). For \(|\nu-L|>1\), its denominator has size
\(\gg(1+|\nu|)^2\), while \(p(\nu)-p(L)\) is bounded. Hence its absolute
integral is \(O(P_X)\). The ordinary smooth integrals are easier because
\(p\in L^1\) and each normalized spatial profile is rapidly decreasing.

For the \(x\)-derivative of the divided difference, set
\(q(\nu)=\theta_\nu p(\nu)\). Exact differentiation, rather than
termwise loss of the diagonal cancellation, gives

\[
x\partial_x\{g[p(\nu)-p(L)]\}
=-ig[q(\nu)-q(L)].
\]

Now \(q(\nu)\ll P_X(1+|\nu|)^{-2}\), with the corresponding local
Lipschitz bound, so the same near/far division is integrable. The smooth
shares are controlled directly by \(|\theta_\nu/D|\leq1\). Integration in
the compact \(L,\beta\) set therefore costs only \(P_X\).

Finally,

\[
r-1=\frac14-\frac{a+b}{2}\geq\frac14-b>0,
\qquad p-1=\frac14+\frac{a+b}{2}>0,
\]

uniformly for large \(X\). Thus the unrestricted absolute \(h\)- and
\(q\)-sums are \(O(1)\). Also

\[
\left(\frac{D_j}{2\sqrt X}\right)^a\leq1,
\qquad (H_j+1)^b=O(1),
\]

and \(H_j\geq1\) leaves \(O(\log(2X))\) dyadic scales. Stars and equality
weights have modulus at most one. This proves (45.12), uniformly as
\(a\downarrow0\). It implies the radial-BV hypothesis because

\[
\int_1^{N_X}|\mathcal A'_{\rm db}(x)|\,dx
\leq \log N_X\sup_x x|\mathcal A'_{\rm db}(x)|.
\]

Radial integration by parts differentiates \(e(\sqrt{Xx})\) continuously
and therefore has full endpoint coefficients; it creates no new star or
half-weight.

**Artificial residue.** Put \(s_0=1/4-v/2\). Since
\(\rho=1/4-s-v/2=-(s-s_0)\),

\[
R_{1,v}(1-s)
=-\frac{\pi i\sqrt X}{\rho}I_1(\rho)
=\frac{\pi i\sqrt X I_1(0)}{s-s_0}+O(1).
\]

The local \(s\)-residue is therefore positive, as asserted in (45.16).
Furthermore,

\[
\frac d{dx}e(\sqrt{Xx})
=\pi i\sqrt X\,x^{-1/2}e(\sqrt{Xx}),
\]

which proves the exact radial coefficient

\[
\pi i\sqrt X I_1(0)=e(\sqrt{XN_X})-e(\sqrt X)
\]

and its uniform \(O(1)\) bound. There is no endpoint factor \(1/2\).

On this residue,

\[
\alpha_\rho=\mu/2,\qquad \beta_\rho=-\mu/2-\nu.
\]

The zeta argument in (45.17) is

\[
\frac34+\frac a2+b-i\beta_\rho.
\]

Compact beta support and \(a/2+b<1/4\) put it in a fixed compact set away
from the pole at \(1\). The other factor is

\[
L\!\left(\frac34-\frac a2-\frac{i\mu}{2},\chi _4\right).
\]

If \(A_4(y)=\sum_{n\leq y}\chi _4(n)\), then \(|A_4(y)|\leq1\), and Abel
summation for \(\sigma>0\) gives

\[
L(\sigma+i\tau,\chi _4)
=(\sigma+i\tau)\int_1^\infty
 A_4(y)y^{-\sigma-i\tau-1}\,dy,
\qquad
|L(\sigma+i\tau,\chi _4)|\ll1+|\tau|.
\]

The beta mask forces \(\nu=-\mu/2+O(1)\), so (45.2) contributes
\(P_X(1+|\mu|)^{-3}\). In the singular top share the remaining factors
have the absolute tail

\[
(1+|\mu|)^{-1}\,(1+|\mu|)\,(1+|\mu|)^{-3}
\ll(1+|\mu|)^{-3}.
\]

For \(c=\chi _0(\mu/2)\), both remaining heights are compact and the top
is evaluated by Plemelj. For \(c=1-\chi _0(\mu/2)\), the cutoff vanishes
near the top pole and the displayed tail is absolutely integrable.
Regular-top and \(j\geq1\) profiles are no worse. The scale factors have
unit-modulus imaginary powers, bounded real powers, and only
\(O(\log X)\) active \(j\)'s. This proves (45.19) without expanding the
residue into an \(h,q\) series.

**Large alpha and conditional final assembly.** If the cells act on the
same already-routed positive-line terminal and really satisfy (45.21),
finite linearity gives the exact identity

\[
\sum_\tau\mathfrak T[\psi\eta_\tau Q_{\rm ef}]
=\mathfrak T[\psi(1-\chi _0)Q_{\rm ef}]
=\mathfrak T_\infty.
\]

No alpha connector, axis or artificial residue appears here: those would
belong to a new contour transfer, while the artificial coefficient is the
separate \(\mathfrak P_{\rho,\infty}\). Under the further hypothesis that
the Round-41 estimate covers this entire sum, Round 41 supplies the
physical bound for \(\mathcal E_X(\mathfrak T_\infty)\). Independently of
that hypothesis, the normalized local bounds proved above give

\[
\mathcal E_X(\mathfrak T_0+
 \mathfrak P_{\rho,0}+\mathfrak P_{\rho,\infty})
\ll X^{1/4}\log^C(2X)
\ll_\varepsilon X^{1/4+\varepsilon}.
\]

Thus the compact central and both artificial shares are target-safe with
\(\mathcal E_X\) applied once. If the missing coverage interface is later
closed, the same typed assembly applies \(\mathcal E_X\) once to the full
normalized vector. The fact that the named Round-41 package already has a
physical bound is not permission to apply \(\mathcal E_X\) to it a second
time.

## 4. First doubtful or unproved step

The first unproved step is the assertion in Section 5 that the previously
accepted Round-41 cells are the same direct positive-line functional
\(\mathfrak T[\psi\eta_\tau Q_{\rm ef}]\) with
\(\sum_\tau\eta_\tau=1-\chi _0\). Once those two facts are supplied,
equality with the complement is forced by linearity. But neither the
accepted node nor the permitted Round-41 synthesis prints the finite list
of \(\eta_\tau\), its cell domains and signs, or the pointwise partition
identity. More importantly, the accepted node names the complete
saddle/entry/exit package but does not explicitly state that every
nonsaddle part of \(\psi(1-\chi _0)Q_{\rm ef}\) belongs to that package or
has its own quantitative bound.

**Scope addendum.** Round-45 analysis proves all of the following without
the missing interface: the lawful aggregate-before-localize order; the
exact direct split into a central terminal and its abstract complement;
the exact three-selector central formula; its value and one-\(x\)-derivative
bound; the oriented artificial coefficient; and bounds for both its
central and complementary alpha shares. It also proves the conditional
identity

\[
\left(\sum_\tau\eta_\tau=1-\chi _0
\ \hbox{on the identical antecedent}\right)
\Longrightarrow
\sum_\tau\mathfrak T[\psi\eta_\tau Q_{\rm ef}]
=\mathfrak T[\psi(1-\chi _0)Q_{\rm ef}].
\]

What remains is both documentary and mathematical coverage: exhibit the
finite partition and antecedent map, then show that the Round-41 bounds
cover its nonsaddle completion as well as the named saddle, entry and exit
pieces. “Complete package” cannot substitute for those two exact
statements in an operator-equality certificate.

The same limited issue occurs in (45.18), which says “the accepted residue
sign” instead of displaying the global contour insertion sign. This audit
proves the intrinsic local \(s\)-residue has the plus sign in (45.16); a
global sign multiplying it is inherited from the already accepted contour
orientation. This omission does not affect the absolute estimate, but an
exact formal certificate should type that inherited interface by its
accepted obligation ID. No earlier doubtful step was found in the compact
estimate, arithmetic chamber, or radial coefficient.

## 5. Control tests and outcomes

| Control | Outcome | Hostile check |
|---|---|---|
| aggregate_stokes_before_localization | PASS | The sixteen cells are summed at finite height before the alpha multiplier or any limit. The positive mixed \(\psi''/4\) cell is absorbed only by the whole sum. |
| alpha_partition_one_count | PASS | On the returned positive line, \(\chi _0+(1-\chi _0)=1\) exactly. No cutoff derivative arises without a new transfer. |
| three_terminal_selectors | PASS | The indicators in (45.11) give exactly \(j=0\) singular, \(j=0\) regular, and \(j\geq1\) interior shares; only the first is Plemelj. |
| signed_plemelj_before_absolute_values | PASS | Delta plus PV gives \(p(L)/A\) and the signed divided difference with the exact \(-i/(2\pi)\) coefficient. Absolute value is taken only afterward. |
| artificial_radial_residue | PASS | Since \(d\rho/ds=-1\), the two minus signs give \(+\pi i\sqrt X I_1(0)\); direct differentiation gives the endpoint difference and no half-weight. |
| artificial_arithmetic_chamber | PASS | The product stays \(\zeta L\); beta compactness bounds zeta, Abel gives \(L\ll1+|\mu|\), and cubic height decay makes the complementary singular tail \(O(|\mu|^{-3})\). |
| large_alpha_positive_line_match | OPEN | Linearity proves the match conditionally, but the accepted Round-41 node does not exhibit \(\sum_\tau\eta_\tau=1-\chi _0\) on the identical antecedent or explicit quantitative coverage of every nonsaddle tail. |
| compact_x_derivative | PASS | The corrected \(L\)-phase, beta phase, and height modulation sum to \(-\theta_\nu\); differentiation preserves the diagonal divided difference. |
| coefficient_and_scale_sums | PASS | \(r,p>1\) uniformly, real scale powers are bounded, there are \(O(\log X)\) active scales, and allowed profile losses are polylogarithmic. |
| collision_corner_and_external_once | PASS locally; full assembly conditional | Routed axes/corners/collisions are not reinserted; the current chamber avoids a new arithmetic/artificial collision; the certified central/artificial vector is sent through \(\mathcal E_X\) once. Full assembly awaits the large-alpha coverage seam. |

Adversarial alternatives fail for explicit reasons: localizing each Stokes
row generates missing alpha connectors; taking absolute values before
Plemelj produces the hard-top divergence; expanding (45.17) termwise
leaves its absolute Dirichlet chamber; dropping the height modulation
breaks (45.13); and multiplying the already physical large-alpha bound by
\(X^{1/4}\) again double normalizes the result. No numerical or
external-source test was used.

## 6. Dependencies and exact artifacts used

This report used only the following permitted mathematical artifacts:

- rounds/codex-managed/m9-m1-beta-positive-line-localization/briefs/positive_line_localization_hostile_audit.md;
- protocol.md;
- state/proof_obligations.yml, at graph hash 45b0c54cad320dc5a08b1129f5a7b4776f6b9e321b3c1c7c9fa738bcb85c5196;
- state/active_campaign.yml, Round 45;
- rounds/codex-managed/m9-m1-beta-positive-line-localization/derivation_packet.md, with the coordinator-supplied correction of (45.8) to \(e^{iL\log(D_j/(2q\sqrt{Xx}))-i\beta\log(hqx)}\);
- rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md;
- rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md;
- rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md;
- rounds/codex-managed/m9-m1-beta-double-bounded-cell/synthesis.md;
- rounds/codex-managed/m9-m1-beta-compact-selector-ownership/synthesis.md.

The principal accepted dependencies used by name are the finite two-axis
product Cauchy--Green identity, finite endpoint-free Plemelj vector,
endpoint-free axial remainder limit, mask--endpoint--axial compatibility,
hierarchical radial split identity, large-alpha transition package bound,
and conditional compact radial-BV reduction. I did not read either other
Round-45 report, any Round-45 candidate proof, or any nonpermitted prior
report. The allocation was 100% analytical/algebraic and 0% numerical.

## 7. Recommended state effect

**Promote only the local analytic conclusions**, subject to the campaign's
separate clean statement-only gate: the exact compact three-selector
functional and its value/one-\(x\)-derivative bound, and the oriented
artificial-residue radial/arithmetic estimate for both alpha shares. The
lawful aggregate-before-localize algebra is also verified.

**Retain the full positive-line alpha-localization certificate open.**
Before promotion it needs an exact finite Round-41 interface recording

\[
\sum_\tau\eta_\tau=1-\chi _0
\]

on the identical direct endpoint-free antecedent, plus a quantitative
statement covering every nonsaddle tail in that complement. This is not
resolved merely by adding a citation or renaming the accepted
saddle/entry/exit package. The State Patch should also type the accepted
global contour sign multiplying (45.16).

Consequently retain the complete double-bounded-cell promotion and the
complete beta transition open until that interface and the separate clean
rederivation gates close. Do not promote the alpha-bounded branch, M9-M1,
M9, or the Gauss-circle target from this report.
