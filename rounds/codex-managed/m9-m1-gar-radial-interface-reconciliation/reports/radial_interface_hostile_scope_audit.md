# Round 120 hostile scope audit: GAR radial interface

## 1. Result

**Corrected terminal-height interface-closure lemma; promote after three
statement repairs.** At graph hash
`daa3c03b4b08ab062fa78724813fd2beff02ad92df8bf25d32407b1ce7f91177`,
the analytic core of (120.C1)--(120.C8) survives hostile review. For one
fixed \(s_0>0\), the terminal-height coefficient
\(\mathcal C_{T,X}^*\) satisfies

\[
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})\ll_{\varepsilon,s_0,W}X^\varepsilon. \tag{120.H1}
\]

It agrees atom by atom with the literal coefficient
\(\mathcal C_X^*\) when \(n/\sqrt X\geq s_0\), and it has no atoms
when \(n/\sqrt X<c_T\) for one fixed \(c_T>0\). Consequently, for a
fixed smooth lower cutoff \(V_{\rm low}\), equal to one on
\([0,s_0]\) and zero on \([2s_0,\infty)\),

\[
 \boxed{\;
 \sum_{n\leq N_X}^{*}(1-V_{\rm low}(n/Y))
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,s_0,W}X^\varepsilon .\;}                 \tag{120.H2}
\]

This is a target-safe theorem for the **whole nonlower radial
complement**. It implies the Round-98 sharp radial/interface estimate
after the already proved fixed compact critical sectors are subtracted.
It closes the interface without identifying a physical collar with an
integration-by-parts prefix, without taking \(C\uparrow16\), and without
invoking an arbitrary finite Mellin height.

Three corrections are mandatory but not fatal:

1. The certified closed profile support is
   \(1/2\leq t\leq3/2\), not \(t\leq C_W<3/2\). Consequently the
   certified lower radial constant is
   \(c_T=\kappa^2/9=s_0/144\).
2. Support of the coefficient does not by itself make
   \(V_{\rm low}\) an admissible compact Mellin cutoff. One must insert
   an auxiliary fixed \(A\in C_c^\infty((c_T/2,C_A))\), with
   \(2s_0<C_A<16\) and \(A=1\) on \([c_T,2s_0]\), and use
   \(A V_{\rm low}\).
3. (120.C8) is not literally the already-critical-deleted Round-98
   interface owner: it also contains those compact critical sectors.
   It is a stronger whole-complement owner. Either use it in a two-piece
   lower/complement assembly or subtract the fixed critical functions
   coefficientwise before naming the old interface node.

The candidate's final owner sentence also needs correction. The physical
Cauchy endpoint and \(R_1\) modules are not “counted through” the hard
B-process errors. They belong to a different transformed routing and are
simply not added to (120.H2). Subject to these repairs, the verdict is
**promote the lemma and the radial-interface node; retain every
downstream analytic status**.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad Y=\sqrt X=R^2,\qquad y=\lfloor Y\rfloor,\qquad
 N_X=\lfloor16Y\rfloor,
\]

\[
 D_j=2^{-j}y,\qquad H_j=\lfloor D_j/R\rfloor,
\]

and retain only active \(j\) with \(H_j\geq1\). Retain the actual smooth
profiles and one-sided hard profile, \(\Phi(h/(H_j+1))\), the spatial
stationary star, the outer product half tie, odd \(q\), and
\(\chi _4(q)\). Thus

\[
 \Omega_X^*(n,h)=
 \sum_j\mathbf 1_{h\leq H_j}\Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
\]

\[
 \mathcal C_X^*(n)=
 \sum_{\substack{hq=n\\q\ {\rm odd}}}\chi _4(q)\Omega_X^*(n,h).
\]

Choose \(0<s_0<8\), put \(\kappa=\sqrt{s_0}/4\), and fix a smooth
\(\vartheta\) with

\[
 \vartheta(u)=0\quad(u\leq\kappa/2),\qquad
 \vartheta(u)=1\quad(u\geq\kappa).
\]

Define

\[
 \Omega_{T,X}^*(n,h)=
 \sum_j\mathbf 1_{h\leq H_j}\vartheta(h/H_j)
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
\]

\[
 \mathcal C_{T,X}^*(n)=
 \sum_{\substack{hq=n\\q\ {\rm odd}}}\chi _4(q)
 \Omega_{T,X}^*(n,h).                                      \tag{120.H3}
\]

The internal analytic input is the accepted terminal divisor theorem

\[
 B_1(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L)
\]

for a frequency coefficient of sampled BV norm \(O(L^{-1})\), including
the one-sided hard denominator profile. The exact positive-frequency
smooth and hard transforms, with their constants, stars, hard sample,
cotangent boundary, and aggregate errors, are also retained.

The certified closed support interval for every nonzero stationary
profile atom is \(1/2\leq t\leq3/2\). Then

\[
 \mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)
 \quad(n/Y\geq s_0),                                       \tag{120.H4}
\]

\[
 \mathcal C_{T,X}^*(n)=0
 \quad(n/Y<c_T),\qquad
 c_T={\kappa^2\over9}={s_0\over144}.                       \tag{120.H5}
\]

For the exact Round-98 partition, write on \([0,16]\)

\[
 1=V_{\rm low}+\sum_{r=1}^mV_r+V_{\rm int},                \tag{120.H6}
\]

where every \(V_r\in C_c^\infty((c_r,C_r))\) has
\(0<c_r<C_r<16\). Besides (120.H2), the exact interface conclusion is

\[
 \sum_{n\leq N_X}^{*}V_{\rm int}(n/Y)\mathcal C_X^*(n)
 n^{-3/4}e(\sqrt{Xn})\ll_\varepsilon X^\varepsilon.         \tag{120.H7}
\]

All assertions are physical-profile statements for real \(X\). None is
a uniform theorem at arbitrary finite Perron or Mellin top height.

## 3. Proof or derivation

For an active \(j\), set \(H=H_j\) and

\[
 u_j(h)=\mathbf 1_{h\leq H}\vartheta(h/H)
 {\Phi(h/(H+1))\over h}.
\]

Its support lies in \((\kappa H/2,H]\). On this fixed-ratio interval,
\(h^{-1}\ll_{s_0}H^{-1}\). The accepted variation of \(\Phi\), the
fixed variation of \(\vartheta\), product variation, and the jump from
\(h=H\) to \(H+1\) give

\[
 \|u_j\|_\infty+\sum_h|u_j(h+1)-u_j(h)|
 \ll_{s_0}H^{-1}.                                         \tag{120.H8}
\]

Equivalently, the support splits into \(O_{s_0}(1)\) fixed-BV shells
\(L\asymp H\). For every active height,

\[
 H=\lfloor D_j/R\rfloor\geq {D_j\over2R},\qquad
 {D_j\over H}\leq2R.                                      \tag{120.H9}
\]

The terminal theorem therefore gives

\[
 \mathcal B_{T,j}^+\ll_{\varepsilon,s_0}RX^\varepsilon,
 \qquad
 \mathcal B_T^+\ll_{\varepsilon,s_0}RX^\varepsilon,         \tag{120.H10}
\]

after absorbing the logarithmic number of active \(j\)'s. Bounded heights
\(H=1,2\) satisfy the same estimate directly.

The positive stationary transform is termwise in \(h\), so multiplication
by \(\vartheta(h/H_j)\) changes neither its stationary constant nor its
support convention. The accepted constant calculation gives

\[
 \mathcal B_T^+
 ={e(1/8)\over i}R
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})+\mathcal E_T.                                \tag{120.H11}
\]

On the hard profile, the cotangent boundary is

\[
 \ll\sum_{\kappa H_0/2<h\leq H_0}{1\over h}\ll_{s_0}1,
\]

because the accepted \(E_h^\chi(X)\) is \(O(1)\). Its weighted transform
errors cost at most
\(\sum h^{-1}\log(2+h)\ll(\log(2X))^2\). The accepted smooth-profile
errors remain polylogarithmic after the bounded height multiplier is
inserted. Hence
\(\mathcal E_T=O_{s_0,W}((\log(2X))^C)=O_\varepsilon(X^\varepsilon)\)
for fixed \(C\). Combining (120.H10)--(120.H11) and dividing by the
single factor \(R\) proves (120.H1). Pairing negative frequency is needed
only for the original real M1 projection; the positive identity already
proves the displayed complex modulus.

For the exact geometry, put \(s=n/Y\) and

\[
 t={2h\sqrt{X/n}\over D_j}.
\]

Every nonzero atom satisfies

\[
 {hR\over D_j}={t\sqrt s\over2}.                           \tag{120.H12}
\]

If \(s\geq s_0\), then \(t\geq1/2\) and
\(H_j\leq D_j/R\) give

\[
 {h\over H_j}\geq {hR\over D_j}
 ={t\sqrt s\over2}\geq{\sqrt{s_0}\over4}=\kappa.
\]

Thus \(\vartheta=1\) on every contributing \((j,h,q)\) incidence,
proving (120.H4) coefficientwise, including the hard incidence and every
star. Conversely, a nonzero terminal atom has
\(h/H_j>\kappa/2\). Equations (120.H9) and (120.H12) yield

\[
 {hR\over D_j}>{\kappa\over4},\qquad
 s={4(hR/D_j)^2\over t^2}>
 {\kappa^2\over9}={s_0\over144}=c_T.
\]

The inequalities \(h\leq H_j\leq D_j/R\) and \(t\geq1/2\) also give
\(s\leq16\). This proves (120.H5) without replacing any floor.

Choose a fixed

\[
 A\in C_c^\infty((c_T/2,C_A)),\qquad
 2s_0<C_A<16,\qquad A=1\ \hbox{on }[c_T,2s_0].             \tag{120.H13}
\]

On the support of \(\mathcal C_{T,X}^*\), multiplication by
\(V_{\rm low}\) is identical to multiplication by the admissible compact
cutoff \(A V_{\rm low}\). In Mellin mode \(t'\), the terminal-height
fixed-cutoff argument has frequency BV norm

\[
 \ll_{s_0}{1+|t'|\over H_j},
\]

the denominator mode has modulus one, and
\(\int|\widehat{A V_{\rm low}}(t')|(1+|t'|)\,dt'<\infty\).
All cutoff seminorms are fixed. Hence

\[
 \sum_{n\leq N_X}^{*}V_{\rm low}(n/Y)
 \mathcal C_{T,X}^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_\varepsilon X^\varepsilon.                            \tag{120.H14}
\]

Where \(1-V_{\rm low}\neq0\), (120.H4) gives the exact identity

\[
 (1-V_{\rm low})\mathcal C_X^*
 =(1-V_{\rm low})\mathcal C_{T,X}^*.
\]

Subtracting (120.H14) from (120.H1) proves (120.H2). Equation (120.H6)
then gives

\[
 G_{V_{\rm int}}=G_{1-V_{\rm low}}-\sum_{r=1}^mG_{V_r}.
\]

Every \(G_{V_r}\) is an accepted fixed compact critical transfer, proving
(120.H7).

For comparison, the accepted upper integration-by-parts prefix is

\[
 e(\sqrt{XN_X})
 \sum_{n\leq N_X}^{*}\mathcal C_X^*(n)n^{-3/4},             \tag{120.H15}
\]

whereas a physical collar has multiplier
\(V(n/Y)e(\sqrt{Xn})\). Even with a common coefficient and star, these
are not equal: their difference contains the genuine phase/cutoff
commutator

\[
 \sum_{n\leq N_X}^{*}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 \{e(\sqrt{Xn})-e(\sqrt{XN_X})\}.                           \tag{120.H16}
\]

The terminal-height proof bounds the collar directly and never identifies
(120.H16) with an endpoint boundary term.

## 4. First doubtful or unproved step

The first false seam in the printed candidate is its strict support
constant \(C_W<3/2\). The certified profile support reaches the closed
edge \(t=3/2\). Replacing it by \(1/2\leq t\leq3/2\) gives exactly
\(c_T=\kappa^2/9=s_0/144\); no stronger uniform lower support has been
proved.

The first incomplete analytic step then occurs after (120.C7). The
sentence “by (120.C6), that weighted part is supported compactly” is not
by itself enough to invoke the accepted Mellin transfer:
\(V_{\rm low}\) equals one at zero and is not in
\(C_c^\infty((c,C))\). Formula (120.H13) is the required repair. It is
legal because the corrected support supplies fixed \(c_T>0\), and it
introduces only fixed seminorms.

The next overstatement is that (120.C8) is “exactly” the Round-98
interface owner. It is the larger nonlower complement. Equation (120.H6)
and subtraction of the accepted compact sectors give the exact old owner;
alternatively the graph may record a new two-piece lower/complement route.
A flat assembly containing (120.C8), the critical pieces, and the
interface as independent summands would double-own those sectors.

Finally, the claim that the Cauchy endpoint and \(R_1\) modules are counted
through transform errors is false as an identification. The hard cotangent
boundary in (120.H11), the finite Cauchy endpoint prefix, and the physical
\(R_1\) arithmetic return are different formulas. The corrected proof
bypasses the latter route; it neither adds nor re-estimates it.

After these corrections, no analytic step in (120.H1)--(120.H7) remains
unproved from the permitted accepted interfaces. In particular,
\(\vartheta(h/H_j)\) has the exact BV norm required by the terminal
theorem. The absolute-error proof in (120.J11)--(120.J12) is valid:
on one terminal scale its cost is
\[
 \sum_{\kappa H_j/2<h\leq H_j}{\log(2+h)\over h}
 \ll_{s_0}\log(2+H_j),
\]
and the geometric height sequence gives
\(\sum_j\log(2+H_j)\ll\log^2(2X)\). The hard cotangent term is
\(O_{s_0}(1)\). Thus neither the outer \(\vartheta\) nor deletion of the
lower heights hides cancellation or an extra factor of \(R\).

## 5. Control tests and outcomes

| Seam / required control | Outcome | Hostile check |
|---|---|---|
| Coefficient: `literal_global_radial_coefficient` | **Pass** | (120.H11) inserts \(\vartheta(h/H_j)\) only in the literal \(j,h\) incidence of \(\Omega_X^*\). Odd \(q\) retains \(\chi _4(q)\); no character is moved to \(h\). |
| Coefficient: terminal-theorem applicability | **Pass** | (120.H8) gives the required \(O(H_j^{-1})\) BV norm, including the lower transition, \(H_j+1\), and upper jump. Only \(O_{s_0}(1)\) shells \(L\asymp H_j\) occur. |
| Normalization: `external_X_one_quarter_normalization` | **Pass** | The transform contributes exactly one \(R=X^{1/4}\) in (120.H11); it is divided out in (120.H1) and restored once as \(-4R/\pi\) in physical M1. |
| Owner: `fixed_radial_partition_one_count` | **Pass after correction** | (120.C8) owns the whole nonlower complement, not the already-critical-deleted interface. Use the two-piece route or (120.H6); do not add (120.C8), critical sectors, and interface as flat owners. |
| Critical scope: `compact_critical_transfer_scope` | **Pass after correction** | The weighted transfer uses \(A V_{\rm low}\in C_c^\infty((c_T/2,C_A))\), \(C_A<16\). No endpoint extension of the old fixed-\(V\) theorem is assumed. |
| Endpoint: `upper_endpoint_prefix_coefficient` | **Pass as a nonidentification** | The prefix has the same physical coefficient and stars but the frozen phase (120.H15), not the radial multiplier. Equality with the collar fails by (120.H16); the proof does not use it. |
| Endpoint: `endpoint_boundary_and_R1_routing` | **Pass after wording correction** | Lower prefix, upper prefix, and recombined \(R_1\) remain one accepted physical Cauchy package. None is a B-process error or another summand in (120.H2). |
| Collar: `radial_collar_vs_boundary_prefix` | **Pass** | The collar through \(N_X\) is bounded from the terminal-height antecedent. No integration-by-parts prefix is substituted for it. |
| Collar/seminorm: `flat_support_edge_and_cutoff_seminorms` | **Pass** | The proof uses the accepted whole-profile transform with a fixed height cutoff. Its only radial cutoff is fixed below \(16\). There is no \(C\uparrow16\), shrinking collar, or unsummed seminorm growth. |
| Hard transform/error ledger | **Pass** | The hard cotangent term is \(O_{s_0}(1)\), weighted errors are polylogarithmic, and the \(h\)-only cutoff commutes with the one-sided spatial endpoint. |
| Profile support constant | **Pass after repair** | The closed certified range is \(1/2\leq t\leq3/2\). It gives \(c_T=\kappa^2/9=s_0/144\); the candidate's \(C_W<3/2\) claim is rejected. |
| Geometry: `floor_star_product_tie_hard_sample` | **Pass** | (120.H12) uses \(H_j=\lfloor D_j/R\rfloor\) exactly. Hard \(j=0\), spatial stars, support crossings, and the outer half tie are multiplied identically in (120.H4). |
| Limit: `physical_limit_vs_finite_height` | **Pass** | (120.H1)--(120.H7) concern physical finite sums. The ordinary Mellin integral of fixed \(A V_{\rm low}\) is not an arbitrary Perron top-height estimate. |
| Owner: `alpha_route_nonduplication` | **Pass** | No connector-completed alpha term is added. It remains an alternative transformed architecture. |
| Owner: `lower_parent_disjointness` | **Pass** | The lower owner is \(V_{\rm low}\mathcal C_X^*\); (120.H2) has the exact complementary multiplier. The lower-radial signed aggregate remains open. |
| Source seam | **Pass** | No external theorem is used. The accepted internal terminal theorem's one-sided hard hypothesis is matched literally. |
| Implication: `downstream_scope` | **Pass** | Only the interface parent closes. GAR still needs the lower parent; blockwise M9-M1, M9-M2, endpoint uniformity, M9, and the quarter theorem do not follow. |

The conductor's repaired seams (120.J5)--(120.J25) were also checked
line by line:

| Review lines | Verdict | Independent hostile check |
|---|---|---|
| (120.J5)--(120.J6) | **Pass** | Zero extension creates two jumps of size \(O(H_j^{-1})\); sampled variation of \(\vartheta\Phi/h\) is \(O_{s_0}(H_j^{-1})\). |
| (120.J7)--(120.J8) | **Pass** | For \(x_j=D_j/R\geq1\), \(\lfloor x_j\rfloor\geq x_j/2\). Thus \(D_j/H_j\leq2R\), including \(H_j=1\); \(H_j=0\) is empty. |
| (120.J9)--(120.J10) | **Pass** | \((hX)^{1/4}q^{-3/4}h^{-1}=R(hq)^{-3/4}\) is exact. The outer \(\vartheta\) is constant in \(d\), so the accepted positive character transform reconstructs \(\mathcal C_{T,X}^*\) with all stars and factor \(e(1/8)R/i\). |
| (120.J11)--(120.J12) | **Pass; absolute-error proof confirmed** | The accepted remainder is absolute per \(h\). Terminal support changes \(\sum_{h\leq H}\log(2+h)/h\) to \(O_{s_0}(\log(2+H))\); summing geometric \(H_j\)'s is \(O(\log^2X)\). The hard cotangent mass is \(O_{s_0}(1)\). No deleted-height cancellation is used. |
| (120.J13)--(120.J18) | **Pass after constant repair** | The identity \(hR/D_j=t\sqrt s/2\) is exact. The closed upper support \(t\leq3/2\), not a strict smaller constant, yields \(n/Y>s_0/144\); \(t\geq1/2\) yields \(n/Y\leq16\). |
| (120.J19)--(120.J20) | **Pass** | Since \(0<s_0/144<2s_0<16\), a fixed \(\psi\in C_c^\infty((0,16))\) equal to one on \([s_0/144,2s_0]\) exists. On reciprocal support, \(d\leq3D_j/2\) and \(\vartheta\neq0\) give \(4R^2h^2/d^2>s_0/144\), so inserting \(\psi\) changes no term. |
| (120.J21)--(120.J22) | **Pass** | Mellin separation gives \(h^{2it}\) and \(d^{-2it}\); the former costs \(O((1+|t|)/H_j)\), the latter is bounded, and the fixed compact transform is Schwartz. |
| (120.J23)--(120.J24) | **Pass** | On terminal support \(h\asymp_{s_0}D_j/R\), every normalized \(d\)-derivative of \(w_j(d)W_0(4R^2h^2/d^2)\) is uniformly bounded. At \(d_*=2\sqrt{hX/q}\), its argument is exactly \(hq/Y\). The same absolute error proof applies, including the one-sided hard sample. |
| (120.J25) | **Pass as an implication, not a definition** | Coefficient equality holds wherever \(1-V_{\rm low}\neq0\), so full terminal minus localized terminal proves the whole complement. It implies the old Round-98 interface after compact sectors are subtracted, or supports a two-piece route; it is not definitionally the old already-deleted owner. |

The finite-height falsifier remains operative outside this proof: at a
Perron jump the finite symmetric value is
\(\pi^{-1}\arctan(U/a)\neq1/2\). Thus (120.H2) supplies no uniform
finite-\(U\) extension of the endpoint modules.

## 6. Dependencies and exact artifacts used

The mathematical dependencies are
`M9-M1-terminal-frequency-divisor-bound`,
`M9-M1-global-angular-recombination`, the accepted positive smooth and
one-sided hard transforms in `M9-M1-top-endpoint-transform`, the exact
Vaaler/profile normalization and \(\Phi\)-BV input, and
`M9-M1-smooth-critical-radial-terminal-transfer` only for converting the
stronger whole-complement theorem to the old three-piece Round-98 owner.
Endpoint-prefix, boundary, and \(R_1\) nodes are used only to audit
nonduplication and scope, not to prove (120.H2).

Exact artifacts read and used were:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-route-interface-assembly/reports/m1_route_graph_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-route-interface-assembly/reviews/conductor_round98_graph_and_cycle_audit.md`;
- `rounds/codex-managed/m9-m1-critical-radial-terminal-return/reports/critical_terminal_transfer_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-upper-endpoint-character-abel/reports/upper_endpoint_abel_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/reports/boundary_cauchy_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/reports/r1_residue_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/briefs/radial_interface_hostile_scope_audit.md`;
- `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md`;
- and `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/reviews/conductor_round120_terminal_height_adjudication.md`.

No web source, external theorem, numerical experiment, sibling Round-120
report, or legacy artifact was used.

## 7. Recommended state effect

**Promote after revision.** Promote the corrected terminal-height theorem
(120.H1)--(120.H5), the auxiliary-cutoff subtraction
(120.H13)--(120.H14), and the whole-nonlower estimate (120.H2). Then
promote `M9-M1-global-radial-interface-estimate`, either by the exact
subtraction (120.H6)--(120.H7) or by recording a cleaner alternative
two-piece lower/complement assembly. Record that (120.C8) is stronger
than, but not definitionally equal to, the old interface child.

Revise the candidate's owner wording so that the finite Cauchy endpoint,
\(R_1\), diagonal transitions, and hard B-process errors are not identified
with one another. Retain the accepted endpoint and \(R_1\) results only in
their physical-limit scope; reject any arbitrary-finite-height implication.
Retain alpha as an alternative route and not an additional summand.

After this promotion the GAR route still has exactly one open analytic
parent, `M9-M1-global-lower-radial-signed-estimate`. Therefore
`M9-M1-global-angular-radial-estimate` and the GAR-to-total-active-M1
step remain unusable until that lower parent closes. Nothing here proves
or shrinks either direct blockwise M9-M1 parent, any of the three M9-M2
parents, `M9-endpoint-uniformity`, `M9`, or the quarter theorem. Even
a later complete GAR would enter only `GC-global-M1-alternative-bridge`
together with complete blockwise M9-M2; it would not prove blockwise
`M9-M1`. The accepted internal \(1/3\) exponent and the separately
audited external benchmark are unchanged.
