# Formal candidate: hard-M1 \(t=1\) \(P_2\) cross-gcd cellular-boundary self-return

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Generated: 2026-08-31T10:32:51+08:00
- Role: conductor formalization; candidate evidence only
- Starting graph:
  63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5
- Status: seam repairs applied; pending independent post-repair verification
- Numerical theorem evidence: none

## 1. Result and exact statement

Fix the exact literal squarefree physical source

\[
 N=dm,\qquad N+r=d'm',\qquad 0<r<\lceil L\rceil,\quad 2\mid r,
\]

with \(d,d'\) odd, the total zero-extended endpoint coefficients, and

\[
 W=\chi_4(d')\chi_4(d)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)}.
\tag{199.K1}
\]

Put

\[
 g=(d,d'),\qquad d=g\alpha,\qquad d'=g\beta
\]

and impose before every spectral operation

\[
 P_2=\mathbf1_{|d-gm|\le D_L}
     \mathbf1_{|d'-gm'|>D_L}.
\tag{199.K2}
\]

With \(C_{\mathrm{lit}}\) denoting equality of the complete named sharp
code at the two lower allocations, the exact unresolved masks are

\[
\begin{aligned}
 P_{\partial\mathrm{lit}}
 &=P_2\mathbf1_{(m,\beta)=1}
   \mathbf1_{\chi_4(\alpha m)=-1}(1-C_{\mathrm{lit}}),\\
 P_{s\mathrm f}
 &=P_2\mathbf1_{(m,\beta)=1}
   \mathbf1_{\chi_4(\alpha m)\ne-1},\\
 P_{g\mathrm f}
 &=P_2\mathbf1_{(m,\beta)>1}.
\end{aligned}
\tag{199.K2a}
\]

On the exact open packets

\[
 \kappa<D_L,\qquad
 M:=\min(Y,D_L)>H_B\mathfrak m\kappa,
\tag{199.K3}
\]

the frozen theorem target is

\[
 \left|\mathscr R_{\mathrm{open,out}}^\sigma
 ((P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f})W)\right|
 \ll L^2X^\varepsilon.
\tag{199.K4}
\]

The specified cross-gcd cellular-boundary mechanism does not prove
(199.K4). Its first exact self-return occurs on the mandatory aligned
literal face. A complete \(P_2\)-preserving three-state allocation orbit
has nonzero actual-sign incidence augmentation in the constant-endpoint
control. Completing its endpoint product forces a fourth corner with
recomputed gcd \(gq\), and that corner lies in the unproved
lower-first-failure owner \(P_1\) for all sufficiently large live shells.
Omitting it returns an actual endpoint product with structural coefficient
one. No literal endpoint nonvanishing is asserted.

This is a mechanism-scoped no-go. It is not a lower bound, a nonvanishing
claim, or a disproof of (199.K4) by another method.

## 2. Four cross-gcd factorization

Define

\[
 A=G_{00}=(d,d'),\quad B=G_{10}=(m,d'),\quad
 C=G_{01}=(d,m'),\quad E=G_{11}=(m,m').
\tag{199.K5}
\]

A prime of \((N,N+r)\) occupies exactly one of these four states.
Squarefreeness therefore gives pairwise-coprime factors

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv,
\tag{199.K6}
\]

where all eight displayed factors are pairwise coprime. In particular
\(A=g\), \(B=(m,\beta)\), and

\[
 P_2=
 \mathbf1_{A|Cx-BEu|\le D_L}
 \mathbf1_{A|By-CEv|>D_L}.
\tag{199.K7}
\]

The complete lower, upper, and simultaneous allocation swaps are

\[
\begin{aligned}
 \tau_L(ACx,Eu,Ay,CEv)&=(AEu,Cx,Ay,CEv) &&(B=1),\\
 \tau_U(Ax,BEu,ABy,Ev)&=(Ax,BEu,AEv,By) &&(C=1),\\
 \tau_S(ACx,Bu,ABy,Cv)&=(ABu,Cx,ACv,By) &&(E=1).
\end{aligned}
\tag{199.K8}
\]

Each is an involution on its displayed canonical total zero-extended
allocation domain, preserves \((N,N+r)\), retains recomputed gcd \(A\),
and reverses the appropriate defect in (199.K7). It is a bijection on the
physical live-to-live subdomain only after imposing \(m\) odd for
\(\tau_L\), \(m'\) odd for \(\tau_U\), both odd for \(\tau_S\), and
the transported literal support conditions. Without the displayed
cross-gcd condition its recomputed gcd is \(AB,AC,AE\), respectively.

## 3. The lawful triangle and actual character incidence

Let one odd squarefree block \(q>1\) occupy successively the states
\(B,E,C\). The three vertices are

\[
\begin{aligned}
 V_B&=(Ax,qu,Aqy,v),\\
 V_E&=(Ax,qu,Av,qy),\\
 V_C&=(Aqu,x,Av,qy).
\end{aligned}
\tag{199.K9}
\]

They form the exact cycle

\[
 V_B\xrightarrow{\tau_U}V_E
 \xrightarrow{\tau_L}V_C
 \xrightarrow{\tau_S}V_B.
\tag{199.K10}
\]

All three have recomputed gcd \(A\) and exactly the same \(P_2\) defects

\[
 A|x-qu|\le D_L,\qquad A|qy-v|>D_L.
\tag{199.K11}
\]

This \(q\)-triangle lies in the parity-safe odd-denominator subdomain. The
block \(q\) is odd, while \(m,m'\) have equal parity; if they were both
even, \(E=(m,m')\) would contain \(2\), contradicting
\(E\in\{1,q\}\) at the three vertices. On the transported-support
intersection it is live-to-live; all other literal support changes remain
total-zero-extended.

On the mandatory aligned face impose

\[
 p=-1,\qquad C_{\mathrm{lit}}(V_E)=C_{\mathrm{lit}}(V_C)=0.
\tag{199.K11a}
\]

The two code-mismatched vertices \(V_E,V_C\) then belong to
\(P_{\partial\mathrm{lit}}\), while \(V_B\), with \(B=q>1\), belongs to
\(P_{g\mathrm f}\). If the common-code predicate is instead one, the two
vertices lie in the already proved \(P_{\mathrm{cc}}\) sector and are not
used as the Round-199 aligned obstruction.

Put

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv).
\tag{199.K12}
\]

The actual character quotients on the upper, lower, and simultaneous
edges are \(t,p,tp\). Their product around the cycle is \(1\). Thus the
simultaneous edge has sign \(+1\) when the other two signs are \(-1\).
No formal alternating sign may replace this literal quotient.

Let

\[
\ell_0=\lambda_{N,\sigma}(Ax),\quad
\ell_1=\lambda_{N,\sigma}(Aqu),\quad
u_0=\lambda_{N+r,\sigma}(Aqy),\quad
u_1=\lambda_{N+r,\sigma}(Av).
\tag{199.K13}
\]

After extracting the common scalar and the character at \(V_B\), the
lawful triangle is

\[
 \Sigma_{BEC}
 =u_0\overline{\ell_0}
  +t u_1\overline{\ell_0}
  +tp u_1\overline{\ell_1}.
\tag{199.K14}
\]

For constant endpoint values its twisted augmentation is

\[
 1+t+tp=
 \begin{cases}
 1,&p=-1,\\
 1+2t\in\{-1,3\},&p=+1.
 \end{cases}
\tag{199.K15}
\]

Thus the actual triangle incidence never cancels the joint bad vertices
by itself.

## 4. Forced \(G_{00}\) corner and exact residual

The fourth product corner is uniquely

\[
 V_A=(Aqu,x,Aqy,v),
\tag{199.K16}
\]

with recomputed gcd \(Aq\) and relative character coefficient \(p\).
Direct expansion gives

\[
\begin{aligned}
 \Sigma_{BEC}+p u_0\overline{\ell_1}
 &=(u_0+t u_1)\overline{(\ell_0+p\ell_1)},\\
 \Sigma_{BEC}
 &=(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
   -p u_0\overline{\ell_1}.
\end{aligned}
\tag{199.K17}
\]

On the character-reversing lower edge \(p=-1\), omitting \(V_A\)
therefore returns

\[
 u_0\overline{\ell_1}
\tag{199.K18}
\]

with ordinary coefficient \(+1\). The assertion concerns its structural
coefficient; accidental vanishing of the literal endpoint is neither
excluded nor needed.

At \(V_A\), the lower failure predicate is recomputed with gcd \(Aq\):

\[
 |Aqu-(Aq)x|=Aq|u-x|.
\tag{199.K19}
\]

From (199.K11), \(x=qu+O(D_L/A)\). Since \(q\ge3\) and the live shell
has \(qu\gg L\), (199.K19) exceeds \(D_L\) for every sufficiently large
shell. Hence the unproved lower-first-failure mask

\[
 P_1=\mathbf1_{|d-(d,d')m|>D_L}
\tag{199.K19a}
\]

holds at \(V_A\). No upper-far assertion is made. Bounded shells may be
estimated absolutely but cannot make the asymptotic corner an accepted
error.

Thus a labeled square completion is an allocation bijection but crosses
the \(P_2/P_1\) mask; a same-current-gcd inverse is not the original map.
Deleting the corner violates zero extension, while masking it away
creates the coefficient-one transported-mask commutator (199.K18).

## 5. Aligned sharp face and alternative partial-block failure

On \(p=-1\), the lower ratios at \(V_E,V_C\) satisfy

\[
 \left(\frac{Ax}{qu}-A\right)
 \left(\frac{Aqu}{x}-A\right)
 =-\frac{A^2(x-qu)^2}{qux}.
\tag{199.K20}
\]

Every non-tie close pair therefore crosses the ratio face aligned at
\(A\). When the two complete sharp codes differ, the exact endpoint
difference in (199.K17) contains an ordinary unit jump. It has no
licensed \(D_L/L\) smooth gain, no fictitious \(D_L^2\) collar gain, and
only the inherited \(D_LL^2X^\varepsilon\) positive capacity.

There is a second, earlier failure for a tempting partial-block
completion. For

\[
 v_{01}=(g\kappa a,hb,gc,\kappa he)
\]

moving only \(\kappa\) among \(G_{01},G_{11},G_{10}\) gives masks

\[
\begin{aligned}
 p_{01}&=\mathbf1_{g|\kappa a-hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{11}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{10}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|\kappa c-he|>D_L}.
\end{aligned}
\tag{199.K21}
\]

These are generally different. The partial moves therefore produce the
unpriced commutators

\[
 p_{11}-p_{01},\qquad p_{10}-p_{11},\qquad p_{10}-p_{01}.
\tag{199.K22}
\]

This partial construction is not the lawful whole-allocation triangle of
Section 3 and cannot repair it.

For \(p=+1\), the lower factor in (199.K17) is a sum, not a close
difference. Zero-character configurations lie outside the fully odd
triangle analyzed here and are not used in the no-go. The mandatory
\(p=-1\), code-mismatched aligned face already stops the mechanism.

## 6. Operator, power, and controls

The obstruction is an exact physical identity failure before Fourier,
height, anchor, conductor, Farey, band, packet, or orientation
decomposition. The \(P_2\) and three-piece masks are physical masks and
must be inserted before those operations. The whole allocation cell is
formed before the packet and orientation split. The accepted cap/open
projector is a later linear projector, not an allocation-orbit mask.

Indeed, in the plus chart \(\kappa=C\), while in the minus chart
\(\kappa=B\). On the three vertices,

\[
\begin{array}{c|ccc}
 &V_B&V_E&V_C\\ \hline
 B&q&1&1\\
 C&1&1&q,
\end{array}
\tag{199.K22a}
\]

so the plus inward gcd is \(1,1,q\) and the minus inward gcd is
\(q,1,1\). The triangle is not a fixed-\(\kappa\), fixed-orientation
packet orbit. After the physical identity one must restore both
orientations, both \(T\)-branches, all signs, endpoint translations,
phases, selectors, transported-mask commutators, affine carries,
births/deaths, cells, crossings, Fourier copies, and zero extensions
before the single outer real part. Since the no-go occurs before the
Farey split, it proves no branchwise estimate.

No such restoration turns (199.K18), (199.K19), or (199.K22) into an
already proved owner. The unchanged fixed-packet positive estimate is

\[
 u\{\kappa+M\}X^\varepsilon
\tag{199.K23}
\]

against \(H_B\mathfrak m\kappa uX^\varepsilon\). On (199.K3) the
unremoved ratio is

\[
 \frac{M}{H_B\mathfrak m\kappa}>1.
\tag{199.K24}
\]

At outer scale the aligned unit face retains
\(D_LL^2X^\varepsilon\) capacity against \(L^2X^\varepsilon\).
These are upper capacities only. No positive power is hidden in
\(X^\varepsilon\), and no component modulus is taken.

The calculation rejects the unsigned, character-erased, arbitrary-array,
phase-conjugated, assigned-sign, post-spectral-mask, deleted-corner,
\(\kappa=1\)-rectangle, common-event, fixed-conductor, separate-component,
and capacity-as-lower-mass shadows. No numerical theorem evidence is
used.

## 7. Proof-state recommendation

Record a durable route boundary under
p2_cross_gcd_cellular_boundary_self_return_no_go. Add only
inconclusive evidence to the existing open hard-M1 small-\(t\) owner.
Create no target-safe obligation and promote no \(P_2\) sector.

The exact three-piece theorem (199.K4), complete \(P_2\), \(P_1\), the
rest of original \(t=1\), every original \(t\ge2\) incidence, the
large-\(G\) near-resonant complement, complete hard M1, independent
smooth M1, GAR, every M2 parent, endpoint uniformity, M9, both bridges,
and the quarter theorem remain open or conditional. The internal
exponent \(1/3\), accepted external exponent
\(0.3144831759740614\ldots\), and target \(1/4\) are unchanged.

## 8. Dependencies and exact provenance

The candidate depends on the exact Round-195 open-projector and power
interface, the accepted Round-193 \(P_{\rm cl},P_1,P_2\) partition, the
accepted Round-197 common-cell sector and exact three-piece complement,
and only the following Round-199 artifacts:

1. protocol.md;
2. state/proof_obligations.yml at starting SHA-256
   63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/blind_statement.md;
5. reports/literal_cross_gcd_cellular_boundary_attack.md;
6. reports/aligned_face_twisted_boundary_hostile_audit.md;
7. reports/blind_joint_failure_complex_rederivation.md;
8. controls/conductor_round199_cross_gcd_factorization_analysis.md; and
9. reviews/conductor_round199_report_reconciliation.md.

The report disagreement is resolved explicitly in Section 5: the
whole-allocation triangle preserves \(P_2\), whereas the distinct
partial-block construction produces (199.K22). No web source or numerical
theorem evidence is used. This candidate does not authorize a graph
mutation; acceptance requires the scheduled post-repair reviews and a
mechanically valid State Patch.
