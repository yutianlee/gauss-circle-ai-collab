# Conductor Round-199 report reconciliation

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Starting graph SHA-256:
  63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5
- Status: reconciled for formalization and independent seam review
- Numerical theorem evidence: none

## 1. Frozen objective and report receipts

Round 199 asks whether the complete open-packet complement

\[
 P_{\partial\mathrm{lit}}\dot\cup P_{s\mathrm f}\dot\cup P_{g\mathrm f}
\]

admits the specified coefficient-preserving twisted cellular boundary, or
whether that mechanism has a first exact self-return. The three reports
are:

1. reports/literal_cross_gcd_cellular_boundary_attack.md,
   SHA-256
   FD20236FF18F06A5E226BC86B4D1567BF4DFBB52A64CE825F1599A215F83CB04;
2. reports/aligned_face_twisted_boundary_hostile_audit.md,
   SHA-256
   06F35DA18E28429889E6348A0018646C26DDA263F441BFD3154FD5B26C354885;
3. reports/blind_joint_failure_complex_rederivation.md,
   SHA-256
   C62156FFB0AE3611A482055DBB1EA651E1FE02B532DAE2BBC8F234282C71F378.

No conclusion is selected by vote. The discovery and hostile reports
derive the same complete-allocation triangle and missing-corner identity.
The statement-only report independently finds the aligned unit jump and,
after self-audit, proves that a different tempting partial-block
completion creates literal \(P_2\)-mask commutators.

## 2. Exact common factorization

Put

\[
 A=G_{00},\qquad B=G_{10},\qquad C=G_{01},\qquad E=G_{11}.
\]

Squarefreeness gives the unique pairwise-coprime factorization

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv.
\tag{199.R1}
\]

Here \(A=(d,d')=g\) and \(B=(m,\beta)\). The two \(P_2\) defects are

\[
 A|Cx-BEu|\le D_L,\qquad A|By-CEv|>D_L.
\tag{199.R2}
\]

The complete lower, upper and simultaneous allocation swaps preserve the
displayed gcd \(A\) exactly on \(B=1,C=1,E=1\), respectively. On those
canonical total zero-extended domains they are exact involutions and
reverse the lower defect, the upper defect, or both, so they preserve
\(P_2\). A physical live-to-live claim additionally retains the
odd-denominator and transported-support predicates.

## 3. Reconciliation of whole swaps and partial block moves

The reports analyze two distinct constructions, and they must not be
conflated.

For one nontrivial odd squarefree block \(q>1\), the complete
whole-allocation swaps give

\[
\begin{aligned}
 V_B&=(Ax,qu,Aqy,v),\\
 V_E&=(Ax,qu,Av,qy),\\
 V_C&=(Aqu,x,Av,qy).
\end{aligned}
\tag{199.R3}
\]

They form the exact cycle

\[
 V_B\xrightarrow{\tau_U}V_E
 \xrightarrow{\tau_L}V_C
 \xrightarrow{\tau_S}V_B
\tag{199.R4}
\]

and all three have recomputed gcd \(A\) and the same literal defects

\[
 A|x-qu|\le D_L,\qquad A|qy-v|>D_L.
\tag{199.R5}
\]

Thus this triangle is genuinely a \(P_2\)-preserving physical orbit.

By contrast, the statement-only report projects a block
\(\kappa=G_{01}>1\) while leaving the remaining allocation factors fixed.
For

\[
 v_{01}=(g\kappa a,hb,gc,\kappa he)
\]

the resulting partial vertices have masks

\[
\begin{aligned}
 p(v_{01})&=
 \mathbf1_{g|\kappa a-hb|\le D_L}
 \mathbf1_{g|c-\kappa he|>D_L},\\
 p(v_{11})&=
 \mathbf1_{g|a-\kappa hb|\le D_L}
 \mathbf1_{g|c-\kappa he|>D_L},\\
 p(v_{10})&=
 \mathbf1_{g|a-\kappa hb|\le D_L}
 \mathbf1_{g|\kappa c-he|>D_L}.
\end{aligned}
\tag{199.R6}
\]

These are not identical. Consequently the partial moves generate the
exact transported-mask commutators

\[
 p(v_{11})-p(v_{01}),\qquad
 p(v_{10})-p(v_{11}),\qquad
 p(v_{10})-p(v_{01}).
\tag{199.R7}
\]

The partial construction is therefore not the physical triangle
(199.R3). Its failure is retained as an additional control, but the
formal candidate rests on the stronger \(P_2\)-preserving
whole-allocation triangle.

## 4. Actual incidence and the missing corner

Put

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv).
\tag{199.R8}
\]

The actual character quotients along (199.R4) are \(t,p,tp\); their
holonomy is \(1\). In particular, on the alternating sector the
simultaneous edge has actual sign \(+1\), not an assignable negative sign.

Let

\[
\begin{aligned}
 \ell_0&=\lambda_{N,\sigma}(Ax),&
 \ell_1&=\lambda_{N,\sigma}(Aqu),\\
 u_0&=\lambda_{N+r,\sigma}(Aqy),&
 u_1&=\lambda_{N+r,\sigma}(Av).
\end{aligned}
\tag{199.R9}
\]

After extracting the common phase and the character at \(V_B\), the
three lawful vertices contribute

\[
 \Sigma_{BEC}
 =u_0\overline{\ell_0}
  +t u_1\overline{\ell_0}
  +tp u_1\overline{\ell_1}.
\tag{199.R10}
\]

The only fourth product corner is

\[
 V_A=(Aqu,x,Aqy,v),\qquad (Aqu,Aqy)=Aq,
\tag{199.R11}
\]

with relative character coefficient \(p\). Direct expansion gives

\[
\begin{aligned}
 \Sigma_{BEC}+p u_0\overline{\ell_1}
 &=(u_0+t u_1)\overline{(\ell_0+p\ell_1)},\\
 \Sigma_{BEC}
 &=(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
   -p u_0\overline{\ell_1}.
\end{aligned}
\tag{199.R12}
\]

Hence on the aligned lower character-reversing face \(p=-1\), omitting
\(V_A\) returns \(u_0\overline{\ell_1}\) with ordinary coefficient one.
This is an exact endpoint identity before any positive norm.

The constant-endpoint augmentation of the triangle is

\[
 1+t+tp=
 \begin{cases}
 1,&p=-1,\\
 1+2t\in\{-1,3\},&p=+1,
 \end{cases}
\tag{199.R13}
\]

so character incidence alone never annihilates the joint bad triangle.

## 5. Unsafe owner and aligned-face return

At \(V_A\), the recomputed lower defect is

\[
 |Aqu-(Aq)x|=Aq|u-x|.
\tag{199.R14}
\]

From \(A|x-qu|\le D_L\), \(q\ge3\), and the live shell lower bound
\(qu\gg L\), (199.R14) exceeds \(D_L\) for every sufficiently large
live shell. Thus \(V_A\) belongs to the unproved lower-first-failure mask

\[
 P_1=\mathbf1_{|d-(d,d')m|>D_L}.
\tag{199.R14a}
\]

No upper-far assertion is made. Bounded shells are absolutely harmless,
but do not make the asymptotic \(P_1\) boundary target-safe.

This authoritative Round-193 definition corrects the blind packet's
informal phrase “two-far mask \(P_1\)”; that phrase is not imported into
the candidate or kernel.

The two alternatives are therefore exact:

1. omit \(V_A\), and the coefficient-one term in (199.R12) remains;
2. include \(V_A\), and the cell crosses the \(P_2/P_1\) mask with a
   changed gcd \(Aq\).

Moreover, even the complete rectangle on \(p=-1\) contains the full
literal lower difference \(\ell_0-\ell_1\). When the two sharp codes
differ, the aligned identity

\[
 \left(\frac{Ax}{qu}-A\right)
 \left(\frac{Aqu}{x}-A\right)
 =-\frac{A^2(x-qu)^2}{qux}
\tag{199.R15}
\]

shows that every non-tie close pair can cross the face aligned at \(A\).
The ordinary jump still has only
\(D_LL^2X^\varepsilon\) positive capacity.

The \(p=+1\) class gives a lower sum rather than a close difference, and
the zero-character class gives a live/dead zero-extension boundary. These
facts are secondary because the mandatory aligned stress already stops
the mechanism.

## 6. Conductor decision

The formalized result is a mechanism-scoped no-go:

> The allowed complete-allocation \(B\)-\(E\)-\(C\) triangle is an exact
> \(P_2\)-preserving orbit, but its actual coefficient expansion is not a
> complete product cell. Its unique fourth product corner has recomputed
> gcd \(Aq\) and lies in the unproved \(P_1\) owner for large shells.
> Omitting it returns a literal coefficient-one endpoint atom; including
> it returns the physical-mask commutator. Partial prime-block
> completions fail even earlier because they do not preserve \(P_2\).

This proves neither nonemptiness nor nonvanishing of the aligned literal
sector and supplies no lower bound. It does not disprove the desired
three-piece estimate by another coefficient-sensitive method.

No strict sector, parent, endpoint theorem, bridge, global theorem, or
exponent is promoted. The candidate proceeds to independent
allocation/incidence, operator/power/owner, and blind post-unmask review.
