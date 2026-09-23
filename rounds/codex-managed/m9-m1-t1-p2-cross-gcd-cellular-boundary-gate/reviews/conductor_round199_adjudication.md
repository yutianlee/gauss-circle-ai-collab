# Conductor Round-199 adjudication

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Starting graph SHA-256:
  63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5
- Terminal label:
  p2_cross_gcd_cellular_boundary_self_return_no_go
- Numerical theorem evidence: none

## 1. Decision

Round 199 proves no new target-safe sector and does not prove the complete
three-piece \(P_2\) estimate. It rigorously closes the frozen
coefficient-preserving cross-gcd cellular-boundary mechanism at its first
mandatory aligned-face self-return.

On the squarefree physical source, put

\[
 A=(d,d'),\quad B=(m,d'),\quad C=(d,m'),\quad E=(m,m').
\]

Then

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv.
\tag{199.A1}
\]

For a nontrivial odd block \(q>1\), the complete lower, upper and
simultaneous allocation swaps give the exact \(P_2\)-preserving triangle

\[
\begin{aligned}
 V_B&=(Ax,qu,Aqy,v),\\
 V_E&=(Ax,qu,Av,qy),\\
 V_C&=(Aqu,x,Av,qy).
\end{aligned}
\tag{199.A2}
\]

Its actual character incidences are \(1,t,tp\), where

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv).
\tag{199.A3}
\]

The holonomy is \(1\); the simultaneous edge has sign \(+1\) on the
alternating sector.

## 2. Exact self-return

With

\[
\ell_0=\lambda_{N,\sigma}(Ax),\quad
\ell_1=\lambda_{N,\sigma}(Aqu),\quad
u_0=\lambda_{N+r,\sigma}(Aqy),\quad
u_1=\lambda_{N+r,\sigma}(Av),
\]

the lawful triangle contributes

\[
 \Sigma_{BEC}
 =u_0\overline{\ell_0}
  +t u_1\overline{\ell_0}
  +tp u_1\overline{\ell_1}.
\tag{199.A4}
\]

The unique fourth endpoint-product corner is

\[
 V_A=(Aqu,x,Aqy,v),\qquad (Aqu,Aqy)=Aq,
\tag{199.A5}
\]

and the exact product identity is

\[
 \Sigma_{BEC}
 =(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
  -p u_0\overline{\ell_1}.
\tag{199.A6}
\]

On the mandatory aligned face,

\[
 p=-1,\qquad
 C_{\mathrm{lit}}(V_E)=C_{\mathrm{lit}}(V_C)=0.
\]

Thus \(V_E,V_C\in P_{\partial\mathrm{lit}}\) and
\(V_B\in P_{g\mathrm f}\). If \(V_A\) is omitted, (199.A6) leaves
\(u_0\overline{\ell_1}\) with structural coefficient \(+1\). If it is
included, the recomputed gcd is \(Aq\), and

\[
 |d-(d,d')m|_{V_A}=Aq|u-x|>D_L
\]

for every sufficiently large live shell. Under the accepted Round-193
first-failure partition,

\[
 P_1=\mathbf1_{|d-(d,d')m|>D_L},
\]

so \(V_A\) belongs to the unproved \(P_1\) owner. No upper-far assertion
is required or made.

The aligned ratio identity

\[
 \left(\frac{Ax}{qu}-A\right)
 \left(\frac{Aqu}{x}-A\right)
 =-\frac{A^2(x-qu)^2}{qux}
\tag{199.A7}
\]

shows why the literal code mismatch can retain an ordinary unit face for
every non-tie close pair. Its only licensed positive capacity is
\(D_LL^2X^\varepsilon\), not the \(L^2X^\varepsilon\) target.

## 3. Whole swaps versus partial block moves

The exact whole-allocation triangle (199.A2) preserves both \(P_2\)
defects. A different partial transfer of only
\(\kappa=G_{01}>1\), with the residual factors frozen, does not. Its
successive masks are

\[
\begin{aligned}
 p_{01}&=\mathbf1_{g|\kappa a-hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{11}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{10}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|\kappa c-he|>D_L}.
\end{aligned}
\tag{199.A8}
\]

Their differences are unpriced physical-mask commutators. The corrected
statement-only report and the conductor formalization keep this shortcut
separate from the lawful triangle. It supplies an additional no-go
control, not the primary self-return.

## 4. Operator and power disposition

The \(P_2\) and three-piece masks act on the physical source before
spectral operations. The whole allocation cell is formed before the
packet and orientation split. The accepted cap/open projector is later
and linear, not an allocation-orbit mask.

In the plus chart \(\kappa=C\); in the minus chart \(\kappa=B\). Across
\(V_B,V_E,V_C\), the plus inward gcd is \(1,1,q\), while the minus
inward gcd is \(q,1,1\). Hence there is no fixed-\(\kappa\),
one-orientation, or branchwise cancellation. Both orientations, both
\(T\)-branches, every endpoint, phase, selector, mask commutator, carry,
birth/death, cell, crossing, Fourier copy, and zero extension remain
inside the single outer real part.

The fixed-packet positive estimate remains

\[
 u\{\kappa+M\}X^\varepsilon,\qquad M=\min(Y,D_L),
\]

against \(H_B\mathfrak m\kappa uX^\varepsilon\). On the open region the
deficit remains

\[
 \frac{M}{H_B\mathfrak m\kappa}>1.
\tag{199.A9}
\]

All displayed capacities are upper bounds only. No nonemptiness,
nonvanishing, density, mass, or literal lower bound is proved.

## 5. Review disposition

The repaired candidate and durable kernel passed:

1. independent allocation/incidence post-repair verification;
2. independent power/operator/owner/provenance post-repair verification;
3. independent blind post-unmask post-repair verification.

The original REPAIR reviews remain as evidence of the corrected
live-domain, packet-timing, \(P_1\)-definition, provenance, and blind
terminology seams.

The final candidate SHA-256 is

D4F4FEEA48BB27BEFFF9613521B304DE1D319424138FC70E0802B4444F244E6A,

and the durable kernel SHA-256 is

D8BCFAF33B02DB1FD306CEA926EEB57603D1F96C8FA80300B62B2BC8F6A65993.

No result is selected by vote. The chosen no-go is the narrow exact
statement surviving the three derivations, conductor reproduction, and
all post-repair seams.

## 6. Graph and downstream scope

A valid State Patch may add only inconclusive evidence to
M9-M1-hard-top-high-radical-small-t-residual-estimate and record the
mechanism-scoped rejected claims. It creates no obligation, dependency,
blocker, implication, or target-safe sector.

The joint three-piece \(P_2\) theorem, complete \(P_2\), \(P_1\), the
rest of original \(t=1\), every original \(t\ge2\) incidence, the
large-\(G\) near-resonant complement, complete hard M1, independent
smooth M1, GAR, M9-M1, all M2 parents, endpoint uniformity, M9, both
bridges, and the quarter theorem remain open or conditional.

The strongest internally proved exponent remains \(1/3\). The accepted
external benchmark remains
\(0.3144831759740614\ldots\). The target remains \(1/4\). No exponent
improves.

Round 199 closes mathematically under
p2_cross_gcd_cellular_boundary_self_return_no_go, subject to a
mechanically valid State Patch, reverse/replay, and protected-scope audit.

