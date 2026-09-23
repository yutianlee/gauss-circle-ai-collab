# Hard-M1 \(t=1\), \(P_2\): cross-gcd cellular-boundary self-return

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Generated: 2026-08-31T10:32:51+08:00
- Starting graph SHA-256:
  63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5
- Role: candidate durable kernel
- Status: seam repairs applied; pending post-repair reviews and State Patch
- Numerical theorem evidence: none

## Scope

This candidate kernel formalizes a mechanism-scoped no-go for the
Round-199 coefficient-preserving four-cross-gcd cellular boundary. It
proves no lower bound and no failure of the desired literal estimate by
another method. It is not graph-accepted until the scheduled reviews pass
and a mechanically valid State Patch is applied.

On the squarefree physical source

\[
 N=dm,\qquad N+r=d'm',\qquad
 0<r<\lceil L\rceil,\quad 2\mid r,\quad d,d'\ {\rm odd},
 W=\chi_4(d')\chi_4(d)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)},
\]

with the total zero-extended endpoint coefficients and every literal
support field retained, put \(g=(d,d')\), \(d=g\alpha\),
\(d'=g\beta\), and

\[
 P_2=\mathbf1_{|d-gm|\le D_L}
     \mathbf1_{|d'-gm'|>D_L}.
\]

Define the exact disjoint complement masks

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
\tag{K199.0}
\]

Here \(C_{\mathrm{lit}}\) is equality of the complete named sharp code
at the two lower allocations. The physical masks \(P_2\) and (K199.0)
are inserted before spectral operations. The mechanism is tested after
the later linear cap/open projection on

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa
\]

and has the sole theorem exit

\[
 \left|\mathscr R_{\mathrm{open,out}}^\sigma
 ((P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f})W)\right|
 \ll L^2X^\varepsilon.
\tag{K199.0a}
\]

The cap/open projector is not a physical allocation-orbit mask.

## Cross-gcd factorization and lawful maps

Let

\[
 A=(d,d'),\quad B=(m,d'),\quad C=(d,m'),\quad E=(m,m').
\]

Squarefreeness gives pairwise-coprime factors

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv.
\tag{K199.1}
\]

Thus \(A=g\), \(B=(m,\beta)\), and

\[
 P_2=
 \mathbf1_{A|Cx-BEu|\le D_L}
 \mathbf1_{A|By-CEv|>D_L}.
\tag{K199.2}
\]

The complete lower, upper, and simultaneous allocation swaps preserve
the displayed gcd \(A\) exactly on \(B=1,C=1,E=1\), respectively:

\[
\begin{aligned}
 (ACx,Eu,Ay,CEv)&\leftrightarrow(AEu,Cx,Ay,CEv),\\
 (Ax,BEu,ABy,Ev)&\leftrightarrow(Ax,BEu,AEv,By),\\
 (ACx,Bu,ABy,Cv)&\leftrightarrow(ABu,Cx,ACv,By).
\end{aligned}
\tag{K199.3}
\]

Each is an exact involution on its canonical total zero-extended
allocation domain and reverses the corresponding defect in (K199.2).
It is live-to-live only after the appropriate odd-denominator and
transported-support predicates are imposed.

## The exact \(B\)-\(E\)-\(C\) triangle

For one odd squarefree block \(q>1\), put

\[
\begin{aligned}
 V_B&=(Ax,qu,Aqy,v),\\
 V_E&=(Ax,qu,Av,qy),\\
 V_C&=(Aqu,x,Av,qy).
\end{aligned}
\tag{K199.4}
\]

The three maps in (K199.3) give the cycle

\[
 V_B\to V_E\to V_C\to V_B.
\tag{K199.5}
\]

All three vertices have gcd \(A\) and the same defects

\[
 A|x-qu|\le D_L,\qquad A|qy-v|>D_L.
\tag{K199.6}
\]

They are parity-safe: \(q\) is odd, \(m,m'\) have equal parity, and
\((m,m')\in\{1,q\}\), so both cofactors are odd. They are live-to-live
on the transported-support intersection; other literal support changes
remain represented by total zero extension.

Put

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv).
\tag{K199.7}
\]

The actual character quotients are \(t,p,tp\), so the holonomy is \(1\).
On the mandatory aligned face,

\[
 p=-1,\qquad C_{\mathrm{lit}}(V_E)=C_{\mathrm{lit}}(V_C)=0.
\tag{K199.7a}
\]

Then \(V_E,V_C\in P_{\partial\mathrm{lit}}\), while \(V_B\), with
\(B=q>1\), lies in \(P_{g\mathrm f}\). The common-code case instead
belongs to the already proved \(P_{\mathrm{cc}}\) sector and is not used
for this aligned no-go.

For

\[
\ell_0=\lambda_{N,\sigma}(Ax),\quad
\ell_1=\lambda_{N,\sigma}(Aqu),\quad
u_0=\lambda_{N+r,\sigma}(Aqy),\quad
u_1=\lambda_{N+r,\sigma}(Av),
\]

the three vertices contribute, after one common scalar is removed,

\[
 \Sigma_{BEC}
 =u_0\overline{\ell_0}
  +t u_1\overline{\ell_0}
  +tp u_1\overline{\ell_1}.
\tag{K199.8}
\]

Its constant-endpoint augmentation is \(1\) when \(p=-1\), and
\(1+2t\in\{-1,3\}\) when \(p=1\). It never vanishes by incidence alone.

## Missing corner and lower-far return

The fourth product corner is

\[
 V_A=(Aqu,x,Aqy,v),
\tag{K199.9}
\]

with gcd \(Aq\) and relative character coefficient \(p\). Exactly,

\[
 \Sigma_{BEC}
 =(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
  -p u_0\overline{\ell_1}.
\tag{K199.10}
\]

On the aligned character-reversing face \(p=-1\), omission of \(V_A\)
therefore leaves \(u_0\overline{\ell_1}\) with structural coefficient
\(+1\). At \(V_A\), the recomputed lower defect is

\[
 Aq|u-x|.
\tag{K199.11}
\]

Since (K199.6) gives \(x=qu+O(D_L/A)\), while \(q\ge3\) and
\(qu\gg L\) on the live shell, (K199.11) is \(>D_L\) for all
sufficiently large shells. Hence \(V_A\) is in the unproved
lower-first-failure mask

\[
 P_1=\mathbf1_{|d-(d,d')m|>D_L}.
\tag{K199.11a}
\]

No upper-far assertion is made. Adding \(V_A\) crosses the \(P_2/P_1\)
mask; deleting it leaves the coefficient-one term in (K199.10).

The aligned ratios obey

\[
 \left(\frac{Ax}{qu}-A\right)
 \left(\frac{Aqu}{x}-A\right)
 =-\frac{A^2(x-qu)^2}{qux}.
\tag{K199.12}
\]

Thus a literal face aligned at \(A\) can be crossed by every non-tie
close pair. On a code mismatch, the lower difference in (K199.10)
retains an ordinary unit jump and only the inherited
\(D_LL^2X^\varepsilon\) positive capacity.

## Partial-block mask commutator

A partial transfer of a block \(\kappa=G_{01}>1\) is not the lawful
whole-allocation triangle. Starting from

\[
 v_{01}=(g\kappa a,hb,gc,\kappa he),
\]

its three would-be masks are

\[
\begin{aligned}
 p_{01}&=\mathbf1_{g|\kappa a-hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{11}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{10}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|\kappa c-he|>D_L}.
\end{aligned}
\tag{K199.13}
\]

They are generally unequal. Masking the unmasked block complex therefore
produces the unpriced commutators

\[
 p_{11}-p_{01},\qquad p_{10}-p_{11},\qquad p_{10}-p_{01}.
\tag{K199.14}
\]

The simultaneous block move has actual quotient \(+1\), and the fourth
block state has gcd \(g\kappa\). Consequently this shortcut supplies no
safe completion.

## Operator and power boundary

The obstruction is physical and occurs before Fourier, height, conductor,
anchor, Farey, packet, or orientation operations. The whole allocation
cell is formed before the packet and orientation split; the accepted
cap/open projector is applied later and linearly.

In the plus chart \(\kappa=C\), while in the minus chart \(\kappa=B\).
Along the triangle,

\[
\begin{array}{c|ccc}
 &V_B&V_E&V_C\\ \hline
 B&q&1&1\\
 C&1&1&q.
\end{array}
\tag{K199.15}
\]

Thus the plus inward gcd is \(1,1,q\), the minus inward gcd is
\(q,1,1\), and the triangle is not a fixed-\(\kappa\) or
fixed-orientation packet orbit. Every transported mask, endpoint, phase,
selector, carry, birth/death, cell, crossing, Fourier copy, zero
extension, both physical orientations, and both \(T\)-branches must remain
inside the one outer real part. Since the no-go is pre-Farey, it proves no
branchwise estimate.

The inherited fixed-packet positive estimate remains

\[
 u\{\kappa+\min(Y,D_L)\}X^\varepsilon
\]

against \(H_B\mathfrak m\kappa uX^\varepsilon\). On the open region the
deficit

\[
 \frac{\min(Y,D_L)}{H_B\mathfrak m\kappa}>1
\]

is unchanged. The outer aligned-face capacity remains
\(D_LL^2X^\varepsilon\), not \(L^2X^\varepsilon\). Neither capacity is a
lower bound.

The calculation rejects the unsigned, character-erased, arbitrary-array,
phase-conjugated, assigned-sign, post-spectral-mask, deleted-corner,
\(\kappa=1\)-rectangle, fixed-conductor, common-event,
separate-orientation, branchwise, component-norm, and
capacity-as-lower-mass shadows. No numerical theorem evidence is used.

Subject to the remaining post-repair reviews and a mechanically valid
State Patch, the recommended terminal label is
p2_cross_gcd_cellular_boundary_self_return_no_go. The only admissible
graph effect is inconclusive no-go evidence on the existing open hard-M1
small-\(t\) owner plus mechanism-scoped rejected claims. Add no proved
obligation, dependency, blocker, target-safe sector, parent implication,
theorem, or exponent.

The literal three-piece \(P_2\) estimate remains open to a different
coefficient-sensitive method. Complete \(P_2\), \(P_1\), the rest of
original \(t=1\), every original \(t\ge2\) incidence, the large-\(G\)
near-resonant complement, complete hard M1, independent smooth M1, GAR,
every M2 parent, endpoint uniformity, M9, both bridges, and the quarter
theorem remain open or conditional. The internal exponent \(1/3\), the
accepted external exponent \(0.3144831759740614\ldots\), and target
\(1/4\) are unchanged.

## Provenance

This kernel was formalized from Round 199. Its immediate source is the
repaired formal candidate
rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/candidates/formalized_hard_m1_t1_p2_cross_gcd_cellular_boundary_self_return.md
at SHA-256
D4F4FEEA48BB27BEFFF9613521B304DE1D319424138FC70E0802B4444F244E6A.
Earlier lineage is:

- rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/reports/literal_cross_gcd_cellular_boundary_attack.md;
- rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/reports/aligned_face_twisted_boundary_hostile_audit.md;
- rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/reports/blind_joint_failure_complex_rederivation.md;
- rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/controls/conductor_round199_cross_gcd_factorization_analysis.md;
- rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/reviews/conductor_round199_report_reconciliation.md.

Exact inherited dependencies are the Round-193 lower-first-failure
partition, the Round-195 open-projector and packet-power interface, and
the Round-197 common-cell sector with its three-piece complement. The
starting graph is the hash in the header. This kernel is candidate
evidence only until State Patch validation and application.
