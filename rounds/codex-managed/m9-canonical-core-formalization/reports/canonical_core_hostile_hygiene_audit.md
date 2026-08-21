# Round 92 hostile canonical-core and source-hygiene audit

Campaign: `m9-canonical-core-formalization`  
Task: `canonical_core_hostile_hygiene_audit`  
Role: hostile source and dependency auditor  
Starting graph SHA-256: `1bc91c527bfe3595436497483aeb058d4a3b3e87c073931f8517b53df24fe0e5`  
Status: candidate evidence only; no shared proof state is changed.

## 1. Result

**Revision verdict: the two scalar capacity calculations survive, but the
displayed canonical targets are not yet self-contained or graph-ready.**  The
following parts pass hostile checking.

- In M1, the row, ordered-pair, and four-row gains are respectively
  \(Q^{-5/24}\), \(Q^{-5/12}\), and \(Q^{-5/6}\).  With
  \(\mathsf C_{82}=B^3T^2Q^{-5/12}\) and
  \(\mathsf T_{82}=J^2/T\), the linear gap is
  \(\Gamma_{82}=B^3J^{-11/30}\), while the full-degree Gram gap is
  \(\Gamma_{82}^2\).  At \(B=J^{3/20}\), these are \(J^{1/12}\) and
  \(J^{1/6}\), so the compulsory Toeplitz square root returns to the same
  \(J^{1/12}\) linear deficit.  It gives neither an extra loss nor a gain.
- In M2, a literal residual energy bound of size
  \(L^2X^\varepsilon\), once joined to every earlier energy owner, gives
  \(\mathcal E_L^\top\ll L^2X^\varepsilon\), and the accepted row Cauchy
  inequality then gives
  \(\mathcal T_{\mathrm{end},L}\ll L^{3/2}X^\varepsilon\).  A positive hard
  block has capacity \(L^2\sqrt{\rho}\),
  \(\rho=AJD^3/L^3\), so the required signed saving is exactly
  \(\rho^{-1/2}\).

The hostile audit nevertheless finds four certification blockers.

1. The M1 formula suppresses the class-dependent \((M,K)\) table, the exact
   hard-cell predicate, conjugation closure, and several actual-symbol
   definitions.  It also replaces the exact upper collar
   \(\Delta_b-E_*\), \(E_*=\lfloor J^{3/4}\rfloor\), by
   \(\Delta_b-J^{3/4}\).  The latter contradicts the declared literal-floor
   convention.
2. The M1 owner names do not by themselves prove multiplicity one:
   `O_(83:86)` also names a Round-82 same-residue owner, and
   `E_87` must mean only its \(u\ne0\) incidence after the one global
   \(u=0\) coefficient is removed.  The phrase “sigma not previously owned”
   is not a mathematical predicate.
3. The M2 formula does not specify the dyadic block ranges, the exact
   \(R\)-window partition, the actual \(k\)-weight, the lift set, or the
   global \(2\Re\)/conjugate orientation which turns the complex blocks back
   into the real off-diagonal energy.  Consequently the asserted
   original-to-energy implication is arithmetically correct but not yet an
   exact identity from the displayed definitions.
4. The graph contains a materially overstrong forward edge:
   `M9-M2-top-endpoint-signed-cone` currently implies both
   `M9-endpoint-uniformity` and `M9-M2`, whereas the frozen packet correctly
   says that even the new hard-kernel estimate closes only the displayed top
   M2 cone and leaves other M2 packets and endpoint assembly separate.
   Several `next_action` fields and strategy directives also predate the
   completed Round-91 one-third theorem and R5 reconciliation.

Li--Yang and Xiao were opened in their primary arXiv versions and audited
only as guardrails.  Neither has a hypothesis-preserving substitution into
the M1 Gram operator or M2 density--discrepancy kernel.  Li--Yang's primary
v2 text additionally contains a literal sign inconsistency in one Case-A
threshold, so its existing source card must remain incomplete.  No source is
an imported dependency, no missing signed estimate is proved, and no
M9-M1, M9-M2, endpoint, M9, bridge, or target promotion is licensed.

## 2. Exact statement and hypotheses

The smallest statements surviving this audit are conditional implications,
not the missing estimates themselves.

**M1 canonical implication.**  Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 J^{13/18}<C\le J^{3/4},\qquad B=C/T.
\]

Fix one actual Round-81 smooth nonaxial component: one class
\(\kappa\in\{1/4,1/2,1\}\), physical frequency (renamed here
\(k_{\rm phys}\)), stationary sign, alias, and reflected orientation.  The
class table inherited from the accepted Round-83 reduction is

\[
 (g_\kappa,M_\kappa,K_\kappa)=
 \begin{cases}
 (1,4b,k_{\rm phys}),&\kappa=1/4,\\
 (2,2b,2[k_{\rm phys}\bar4]_b),&\kappa=1/2,\\
 (4,b,[k_{\rm phys}\bar4]_b),&\kappa=1,
 \end{cases}
 \qquad b\asymp B,\quad M_\kappa\asymp B.
\]

Set

\[
 D_1=\lfloor J^{87/140}\rfloor,
 \qquad E_*=\lfloor J^{3/4}\rfloor,
\]

and use zero extension outside the actual \(b\)-dependent stationary
support of width \(\Delta_b\).  The deep linear coefficient is

\[
 \mathcal A_{b,d}={1\over M_\kappa^2}\sum_n
 \bigl(S(n+d,K_\kappa;M_\kappa)
       \overline{S(n,K_\kappa;M_\kappa)}-c_{M_\kappa}(d)\bigr)
 I_b(n+d)\overline{I_b(n)}
\]

on the literal interval

\[
 D_1<|d|<\Delta_b-E_*.
\]

Same residue, literal \(d=0\), all smaller nonzero differences, and the
outer collar are separate linear owners.  Nonzero multiples of \(M_\kappa\)
remain.  For a dyadic deep shell of length \(U\), let \(H_{b,U}\) be the
zero-extended shell polynomial with Fourier coefficients
\(\Pi_{b,U}(d)\mathcal A_{b,d}\), and let

\[
 \mathcal E_U=
 \sum_{b\asymp B}\int_{\mathbb T}|D_U(\theta)|^2
 |H_{b,U}(\theta)|^2\,d\theta.
\]

There must be one global owner for
\(U\sum_{b,d}|\mathcal A_{b,d}|^2\), the whole \(u=0\) coefficient.  On
\(u\ne0\), the exact physical edge set must be partitioned, in order, into
the Round-87 same-group incidence, Round-88 coarse shells, Round-88
good-prime fibres, Round-89 certified cell union, and their set-theoretic
complement.  Denote the final complement by
\(\mathcal E_{\rm hard}(U)\).  It must be closed under the reversal which
makes it real and must retain all four factors

\[
 \Omega_{b,d,u}(n,m)=I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m),
\]

all signs, all three class tables, all nonzero modulus multiples, Ramanujan
cross and square terms, the full \(2\)-part, nonunit factors, and every
failed-threshold/aperiodic cell.  Under that exact partition, the open
estimate

\[
 \mathcal E_{\rm hard}(U)
 \ll_\varepsilon X^\varepsilon {U\over B}J^{14/5}
\]

together with the already proved owner bounds and

\[
 \left|\sum_{b\asymp B}H_{b,U}(0)\right|^2
 \ll_\varepsilon X^\varepsilon {B\over U}\mathcal E_U
\]

implies only the Round-82 first-band smooth nonaxial coefficient target
\(J^{7/5}X^\varepsilon\).  It does not cover \(C>J^{3/4}\), axes, raw
transitions, cone edges, other radial sectors, alpha/top interfaces, or
endpoint assembly.

**M2 canonical implication.**  Let
\(\mathscr H_L\) be the exact half-open odd top-frequency support,
\(1\le L\le X^{1/4}\), and let \(a_{\rm end}(h,m)\) be the literal
normalized Vaaler/profile symbol, including its stars, floors, upper support
edge, and \(m=\lceil h/4\rceil\) lower edge.  Put

\[
 \mathcal T_{\mathrm{end},L}
 =\sum_{h\in\mathscr H_L}\chi_4(h)
   \sum_{\lceil h/4\rceil\le m\le h}
   a_{\rm end}(h,m)e(\sqrt{Xhm}),
\]

\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a_{\rm end}(h,m)e(\sqrt{Xhm}),
 \qquad \mathcal E_L^\top=\sum_m|R_m|^2.
\]

For the positive off-diagonal write uniquely
\(h=ga<s=gb\), where \(a,b,g\) are odd, \((a,b)=1\), and define

\[
 m_0={a+b\over2},\qquad q={b-a\over2},\qquad
 u_{a,b}={q\over m_0+\sqrt{m_0^2-q^2}},
\]

\[
 \Lambda={X(\sqrt b-\sqrt a)^2\over2}=Xqu_{a,b},
 \qquad {Ju_{a,b}\over1-u_{a,b}}<k<
 {2Ju_{a,b}\over1+u_{a,b}}.
\]

On a dyadic block one must state, rather than suppress,

\[
 a\asymp A,\quad b-a\asymp D_{\rm ray},\quad
 k\asymp K_{\rm rec},\quad g\asymp G,\quad
 G\asymp L/A,
\]

the exact residual exclusions, and the fixed thresholds separating

\[
 \rho={AJD_{\rm ray}^3\over L^3}\ll1,
 \qquad \rho\asymp1,
 \qquad \rho\gg1.
\]

The metric windows \(W_R\) must be a declared locally finite partition of
the remaining strict metric set (exact centres excluded), not merely a
family with means \(\mu_R\asymp R^{-1}\).  With the actual reciprocal
weight and lift set explicitly defined, the hard block is the quantity in
(92.34), with the dependence written as
\(\mathfrak C_{a,b,k}^\circ(g)\) and with the global conjugate
orientation/\(2\Re\) convention stated.  The exact energy identity required
for the implication is

\[
 \mathcal E_L^\top
 =\mathcal E_{75,\mathrm{diag}}
  +\mathcal E_{77,\mathrm{endpoint/mode}}
  +\mathcal E_{78,\square}
  +\mathcal E_{79,\mathrm{centre/safe}}
  +2\Re\sum_{A,D_{\rm ray},K_{\rm rec},G,R}
      \mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R},
\]

with each term occurring once.  Under this identity, the open estimate

\[
 \sum_{A,D_{\rm ray},K_{\rm rec},G,R}
 |\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
 \ll_\varepsilon L^2X^\varepsilon
\]

implies the displayed top-cone target and nothing beyond it.  The density
piece \(\mu_R\mathcal K_0\) and all nonzero Fourier modes are components of
the same block and are not separate hypotheses.

## 3. Proof or derivation

**M1 normalization.**  Four normalized rows square the ordered-pair gain:

\[
 (Q^{-5/24})^2=Q^{-5/12},\qquad
 (Q^{-5/12})^2=Q^{-5/6}.
\]

Moreover,

\[
 {\mathsf C_{82}\over\mathsf T_{82}}
 ={B^3T^2Q^{-5/12}\over J^2/T}
 =B^3J^{-11/30}=\Gamma_{82}.
\]

The full-degree four-row capacity and target are

\[
 \mathsf C_{\rm deep}={U\over B}\mathsf C_{82}^2,
 \qquad
 \mathsf T_{\rm deep}={U\over B}\mathsf T_{82}^2,
\]

so their ratio is \(\Gamma_{82}^2=B^6J^{-11/15}\).  A proof at the target
therefore needs the signed factor

\[
 \Gamma_{82}^{-2}=B^{-6}J^{11/15}
\]

relative to full Gram capacity; at \(B=J^{3/20}\) this is \(J^{-1/6}\).
The Toeplitz inequality contributes \(B/U\) before the square root, hence

\[
 \left({B\over U}{U\over B}\mathsf T_{82}^2\right)^{1/2}
 =\mathsf T_{82}.
\]

This proves the square-root reconciliation.  It does not estimate
\(\mathcal E_{\rm hard}\), and the \(q=8\) full-degree control forbids
turning local period depth into a power saving.

The exact M1 owner order is

\[
 \begin{array}{c}
 \text{Round 82 same residue}\to
 \text{Round 83 literal }d=0\to
 \text{Rounds 84/86 }0<|d|\le D_1\to
 \text{Round 85 outer collar and aggregate errors}\to
 \text{deep shell},\\[2mm]
 \text{global }u=0\to
 \text{Round 87 same group on }u\ne0\to
 \text{Round 88 coarse}\to
 \text{Round 88 good-prime}\to
 \text{Round 89 safe cells}\to
 \text{hard complement}.
 \end{array}
\]

This diagram also exposes why `O_(83:86)` and “not previously owned” are
insufficient formal definitions.  The accepted support edge is
\(\Delta_b-E_*\), not \(\Delta_b-J^{3/4}\); the floor difference is only
\(O(1)\) analytically, but the campaign requires literal endpoint ownership.

**M2 normalization and character algebra.**  Exact regrouping gives

\[
 \mathcal T_{\mathrm{end},L}=\sum_mR_m,\qquad
 |\mathcal T_{\mathrm{end},L}|^2\ll L\mathcal E_L^\top.
\]

Thus \(\mathcal E_L^\top\ll L^2X^\varepsilon\) implies
\(\mathcal T_{\mathrm{end},L}\ll L^{3/2}X^\varepsilon\), after relabelling
\(\varepsilon\).  On a hard block,

\[
 {L^2\sqrt\rho\over L^2}=\sqrt\rho,
\]

so the exact missing saving is \(\rho^{-1/2}\).  Since \(G\asymp L/A\),
the Round-79 positive capacity
\(A\sqrt G\sqrt J D_{\rm ray}^{3/2}\) is indeed

\[
 A\sqrt{L/A}\sqrt J D_{\rm ray}^{3/2}
 =L^2\sqrt{AJD_{\rm ray}^3/L^3}.
\]

For odd \(a,b,g\),

\[
 \chi_4(ga)\chi_4(gb)=\chi_4(a)\chi_4(b)
 =(-1)^{(b-a)/2},
\]

and

\[
 {X(\sqrt{gb}-\sqrt{ga})^2\over2g}
 ={X(\sqrt b-\sqrt a)^2\over2}=\Lambda.
\]

These two identities pass exactly.  Expanding
\(W_R=\mu_R+\sum_{\nu\ne0}\widehat W_R(\nu)e(\nu\cdot)\) inside the
complete block is also exact, but it leaves
\(\mu_R\mathcal K_0\).  The actual carrier shifts the apparent
half-integral spectrum back to integer frequencies; consequently the mean
and discrepancy must remain coupled.  Here \(\nu\), not \(r\), is used for
the window Fourier mode so it cannot be confused with the Round-75 row
offset \(s=h+2r\).

The lawful M2 owner chain is the Round-75 character-preserving energy
diagonal, the Round-77 full endpoint/collar and Poisson-mode error, the
Round-78 square/common-squarefree family, the Round-79 exact nonsquare
centres and positive-safe blocks, and finally the strict-metric hard
complement.  The Round-74 character-deleting row correlation is an
alternative sufficient route and may not be added as a second owner to this
chain.

## 4. First doubtful or unproved step

The first doubtful steps are documentary identities, before either new
analytic estimate.

For M1, the packet never turns the phrase

\[
 R_*>\rho_*,\qquad \mathfrak a<M^2/\rho_*^2,
 \qquad \sigma\text{ not previously owned}
\]

into an exhaustive indicator identity.  It must state the Round-87
\(u\ne0\) restriction, the Round-88 coarse and good-prime predicates, the
Round-89 condition involving \(\mathfrak b_\sigma\) and the summable union,
the failed-threshold complement, and the reversal/conjugation action.  Until
then, the displayed sum need not be manifestly real and multiplicity-one;
for a complex quantity, the bare notation
\(\mathcal E_{\rm hard}\ll\cdots\) is not even typed.  After that identity
is supplied, the first mathematical unknown is exactly the signed estimate
at scale \((U/B)J^{14/5}\).

For M2, the first missing line is the exact equality from the Round-75 real
off-diagonal energy to the sum of the collared hard blocks.  A valid line
must include \(2\Re\) or a declared pair of conjugate orientations, an exact
partition of every strict metric point by the \(R\)-windows, empty and
singleton reciprocal intervals, the actual \(k\)-weight, the lift endpoints,
and the safe/hard boundary owner.  The current facts
\(\mu_R\asymp R^{-1}\) and “residual” do not prove this equality.  Once it is
written, the first analytic unknown is the joint bound for the complete
density--discrepancy blocks; no bound for the mean term alone is available.

These documentary defects do not refute either desired inequality.  They do
prevent certification of the present formulas as standalone graph nodes.

## 5. Required controls and outcomes

Here “pass” means that the hostile control was executed; it never means that
one of the open signed estimates was proved.

| Campaign control | Outcome |
|---|---|
| `variable_dictionary` | **Revision required.** Namespace M1 \(b,M,K,A,B_2,V,U,u,H\) against M2 \(a,b,A,K,R,u\) and source parameters. Define \(\Delta_b,\Pi_{b,U},P,x,y,R_*,\mathfrak a,\mathfrak b_\sigma,\mathfrak T_M,\omega,\mathcal G_{a,b},A^\circ\). Rename the M2 ray gap \(D_{\rm ray}\), reciprocal scale \(K_{\rm rec}\), and window Fourier mode \(\nu\). |
| `M1_linear_and_Gram_normalization` | **Pass.** The \(Q\)-powers, \(M^{-2}\) pair normalization, \(M^{-5}\mathfrak T_M=M^{-4}\tau_M\) convention, Toeplitz factor, and square-root gap are mutually consistent. No duplicate \(M^{-2}\) or \(Q^{-5/12}\) is available. |
| `M1_one_count_owner_map` | **Revision required.** Replace `O_(83:86)` and “not previously owned” by the two-level owner diagram in Section 3. Make `E_87` explicitly \(u\ne0\) after the one global diagonal and state the Round-89 cell/union complement. |
| `M1_full_degree_capacity` | **Pass as a capacity barrier only.** Full directed degree gives Gram gap \(\Gamma_{82}^2\), top value \(J^{1/6}\), and required gain \(J^{-1/6}\).  The \(q=8\) fibre is not an aggregate lower bound. |
| `M1_outside_core_scope` | **Pass.** Upper conductors, axes, raw transitions, cone edges, other radial sectors, alpha/top interfaces, and endpoint uniformity remain outside. |
| `M2_original_to_energy_implication` | **Arithmetic passes; exact reassembly requires revision.** Cauchy gives \(L^{3/2}\) from \(L^2\), but the displayed packet lacks the exact residual-energy equality, \(2\Re\)/orientation convention, and window partition. |
| `M2_density_discrepancy_joint_kernel` | **Pass as the required form.** The zero mode survives; discrepancy alone, quotient parity, and the half-frequency argument fail.  The target must be imposed on the unseparated complete block. |
| `M2_one_count_owner_map` | **Revision required.** Name the Round-75 diagonal, Round-77 endpoint/mode error, Round-78 square family, Round-79 exact-centre and safe blocks, bounded boundary, and strict-metric complement.  Do not combine the alternative Round-74 characterless route with this energy ledger. |
| `M2_hard_ratio_capacity` | **Pass.** Positive capacity is \(L^2\sqrt\rho\), safe blocks have \(\rho\ll1\), and the hard side requires \(\rho^{-1/2}\).  Exact constants for the \(\rho\asymp1\) owner still need to be stated. |
| `M2_outside_core_scope` | **Pass.** The hard top cone is only one M2 packet; smooth interior packets, other target-scale endpoint owners, pointwise upgrade, and all-\(D_{\rm den}\) assembly remain separate. |
| `actual_coefficients_characters_endpoints` | **Revision required.** Restore the M1 class table, the exact collar floor \(E_*\), both sign conventions, and actual hard-cell indicator.  Restore the M2 actual \(k\)-weight/lift set, half-open supports, \(2\Re\) convention, and exact endpoint/collar owner.  The identity \((-1)^{(b-a)/2}=\chi_4(ga)\chi_4(gb)\) passes. |
| `false_shadow_table` | **Pass as rejections.** The detailed outcomes are listed immediately below; none is a theorem about the actual signed operators. |
| `source_hypothesis_map` | **Pass as a mismatch map, not applicability.** Both primary papers were opened; neither maps to either canonical core.  Li--Yang's literal threshold inconsistency keeps its source audit open. |
| `graph_forward_pointer_hygiene` | **Fail; patch required.** The overstrong `implies` edge and stale actions/directives are listed below. |
| `downstream_scope` | **Pass.** Formalization licenses no analytic or downstream promotion. |

The false-shadow outcomes are:

| Shadow | Hostile outcome |
|---|---|
| Replace the M1 symbol by arbitrary bounded four-row coefficients | Rejected. Phase-conjugating coefficients and the retained full-degree fibre remove any coefficient-uniform signed gain. |
| Take M1 absolute values, identify the linear row with its Gram lift, or count sparse periods as a saving | Rejected. Full degree returns to \(\Gamma_{82}^2\), and Toeplitz square-roots it back to \(\Gamma_{82}\). |
| Drop nonzero modulus multiples, Ramanujan terms, nonunit/bad-prime cells, or the full \(2\)-part | Rejected as a different operator and a one-count failure. |
| Replace the M2 symbol by arbitrary coefficients or discard \(\chi_4(h)\chi_4(s)\) | Rejected. It proves a stronger unsigned/adversarial analogue for which the required cancellation mechanism is absent. |
| Use quotient parity, a half-integral spectral gap, discrepancy alone, or another reciprocal Poisson step | Rejected by the exact carrier identity: the zero mode and original two-character row return. |
| Call the ordinary \(1/R\) density exceptional | Rejected by the accepted Round-79 density control.  Only excess over ordinary density can be exceptional. |
| Infer the pointwise hard endpoint from a global moment | Rejected. A quantitative pointwise or large-value bridge is a distinct obligation. |

**Current-primary-source map.**

| Primary source opened | Literal theorem/hypotheses checked | Map to the canonical cores and verdict |
|---|---|---|
| X. Li and X. Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, arXiv:2308.14859v2 ([primary HTML](https://arxiv.org/html/2308.14859v2), [primary PDF](https://arxiv.org/pdf/2308.14859v2)) | Proposition 3.1 concerns an averaged \(L^q\) norm of \(\sum_{k\sim K}\sum_{l\sim L}a_{kl}e(lx_1+klx_2+l\sqrt{k}x_3)\), with \(|a_{kl}|\le1\), \(4\le q\le4.5\), \(1\le L<K\le\eta^{-1}\le KL\), and \((L/K)^{(q-2)/(q-4)}\le\eta\).  Their Section-4 sum is the separated BV-weighted form \(\sum_{h\sim H}g(h/H)\sum_{m\sim M}G(m/M)e((hT/M)F(m/M))\), with \(F\in C^3[1,2]\), all first three derivatives bounded above and away from zero, \( |F'F'''-3(F'')^2|\gg1\), and the Case-A/B plus \(N,q\) inequalities of Theorem 4.2. | M1 is a centered four-Kloosterman, varying-composite-modulus Gram operator with a joint four-factor moving symbol; M2 is a two-character triangular cross-row integral with a moving reciprocal selector. Neither has the separated two-variable phase/weights or the stated cone-norm geometry. No substitution for all variables, weights, moduli, norms, and endpoints exists.  Moreover Definition 4.1 equation (4.4) literally prints \(M<T^{-7/16}\), while the application equation (5.11) prints \(M<T^{7/16}\); until resolved from an erratum or author clarification, the card cannot certify the literal theorem range. Guardrail only. |
| Y. Xiao, *Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*, arXiv:2606.28986v1 ([primary HTML](https://arxiv.org/html/2606.28986v1), [primary PDF](https://arxiv.org/pdf/2606.28986v1)) | With the unweighted \(S(h,n)=\sum_{n/2\le a\le n}e(h\sqrt a)\), Theorem 1.1 gives \(\sum_{h\sim H}|S(h,n)|^2\ll_{\varepsilon,\delta}Hn^{1+\varepsilon}\) for fixed \(\delta>0\) and \(H\ge n^{1/2+\delta}\).  Theorem 1.2 gives the fourth moment \(\ll Hn^{2+\varepsilon}\) only for fixed \(0<\delta<1/6\) and \(n^{1/2+\delta}\le H\le n^{2/3}\).  Theorem 1.3 combines the second moment with separate pointwise exponential-sum estimates and Erdős--Turán. | Neither core is an unweighted one-dimensional square-root sum averaged over an independent integer frequency.  In M2 the support \(m\in[\lceil h/4\rceil,h]\), the coefficient, and the character move with the row, while \(e(\sqrt{Xhm})\) does not give Xiao's independent integer-frequency model under either row ordering.  M1 has Kloosterman products and varying moduli.  The moment conclusions are averaged, not the required fixed-\(X\) endpoint estimate; Xiao's own discrepancy proof needs a separate pointwise input. Guardrail only. |

The precise stale or overstrong directives are:

| Artifact/pointer | Defect after Round 91 | Required repair |
|---|---|---|
| Graph `M9.next_action` | Still asks to formulate an M2 fourth-moment/near-collision subproblem. | Point to separate exact M1 and M2 canonical signed cores, their outside packets, endpoint assembly, and the pointwise bridge. |
| Graph `M9-M1.next_action` | Begins “First extract the strongest unconditional exponent,” completed in Round 91. | Delete that sentence; retain the hard Gram attack plus separate upper-conductor/axis/cone/endpoint owners. |
| Graph `M9-M1-global-angular-radial-estimate.next_action` | Calls \(J^{32/45}<C\le J\) the current fixed-interior residual, ignoring the accepted Round-81 extension through \(J^{13/18}\). | Start the first smooth nonaxial residual at \(J^{13/18}\), preserve the \(J^{3/4}\) split, and list the upper main/transition/axis package separately. |
| Graph `M9-M2-top-endpoint-signed-cone.implies` | Directly points to `M9-endpoint-uniformity` and `M9-M2`, contrary to the node statement and frozen packet's outside-core warning. | Remove those direct edges or route them through explicit top-cone and full-M2 assembly nodes. |
| Graph `M9-M2.blockers` | Retains older fourth-moment/conditional blockers but does not name the canonical hard density--discrepancy estimate or the remaining packet assembly as immediate blockers. | Reconcile blockers with dependencies and the new exact canonical node; do not silently delete historical open alternatives. |
| Graph `M9-endpoint-uniformity.next_action` | Describes only the M2 AP/local-average degeneration although the obligation is uniform M1 and M2 target-scale control. | State all-\(D_{\rm den}\) M1/M2 endpoint and short-block assembly; a top-M2 cone theorem alone is insufficient. |
| Strategy Section 3 | Still lists closing `R5-Full-reconciliation` on the unresolved critical path. | Mark R5 and its reconciliation closed in Round 91. |
| Strategy Round-94 and priority-4 directives | Still schedule conditional R5 closure and “R5 and endpoint reconciliation.” | Remove the R5 work item and retain endpoint/bridge reconciliation only. |
| Strategy evaluation of active source hygiene | Still groups R5-Full reconciliation with Li--Yang and Xiao. | Keep Li--Yang/Xiao as guardrails; record R5 as closed. |

No numerical experiment was used.  All capacity checks were exact exponent
arithmetic, and all source checks were literal theorem-hypothesis checks.

## 6. Dependencies and exact artifacts used

The SHA-256 of `state/proof_obligations.yml` was independently recomputed and
matched the frozen value
`1bc91c527bfe3595436497483aeb058d4a3b3e87c073931f8517b53df24fe0e5`.
The repository artifacts used were exactly the permitted context:

- `protocol.md`;
- `state/proof_obligations.yml`, restricted to the target, source-audit,
  Round-75--91, and forward-pointer interfaces relevant to this task;
- `state/best_proof_draft.md`, especially the accepted Round-74--91
  normalizations and owner statements;
- `state/project_summary.md`, especially the current Round-90--91 summary;
- `state/gap_register.md`;
- `state/active_campaign.yml`;
- `strategy/conductor_0817_full_proof_strategy.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/m1_self_return_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/strict_metric_energy_hostile_source_audit.md`;
- `sources/li_yang_2023.md`;
- `sources/xiao_2026.md`;
- `sources/method_strategy_review_2026-08-11.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/briefs/canonical_core_hostile_hygiene_audit.md`.

For the required current source check, only the primary Li--Yang arXiv v2
HTML/PDF and the primary Xiao arXiv v1 HTML/PDF linked in Section 5 were
opened.  No secondary literature was used.  The primary PDFs were opened as
well as the HTML renderings; the Li--Yang threshold discrepancy occurs in the
PDF itself, not merely in experimental HTML.  No theorem from either paper is
used positively.

No sibling Round-92 report was read.  No source card, graph, proof draft,
validation matrix, strategy file, project summary, gap register, or synthesis
was edited.

## 7. Recommended state effect

**Retain every analytic target open; promote nothing; revise the two
formalized statements and repair graph hygiene before certification.**

For M1, preserve
`M9-M1-square-root-capacity-self-return-barrier` as proved and create, or
reuse only if its statement is replaced exactly, a distinct open node for the
hard first-band actual-symbol Gram estimate.  That node must contain the
class table, exact \(D_1\) and \(E_*\) floors, a set-theoretic one-count
indicator, global \(u=0\) convention, conjugation closure, and the complete
actual symbol.  Its downstream effect is only first-band smooth-nonaxial
closure after the accepted owners; it must not imply `M9-M1` or a global
exponent by itself.

For M2, create a distinct open density--discrepancy block-estimate node only
after recording the exact residual-energy identity and block/window
partition.  Its success may imply the residual top energy and then
`M9-M2-top-endpoint-signed-cone`, but the latter must no longer point directly
to full endpoint uniformity or `M9-M2`; explicit outside-packet and endpoint
assembly nodes must intervene.

Apply the forward-pointer repairs in Section 5.  Update the Xiao card with
Theorems 1.1--1.3 and the exact mismatch while retaining it as a nondependency.
Keep `Li-Yang-source-audit` at `source_audit_required` until the literal
\(T^{-7/16}\) versus \(T^{7/16}\) discrepancy and all Case-A/B auxiliary
conditions are resolved; even a corrected card remains a guardrail because
the operator hypotheses fail.

Retain `M9-M1`, `M9-M1-global-angular-radial-estimate`, `M9-M2`,
`M9-M2-top-endpoint-signed-cone`, `M9-endpoint-uniformity`, `M9`, and
`GC-target` open.  Retain the Round-91 one-third theorem and R5 closure
unchanged.  There is no new endpoint range, bridge, one-quarter estimate, or
Gauss-circle exponent.
