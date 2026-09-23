# Blind post-unmask cross-gcd post-repair verification

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Role: independent blind post-unmask post-repair verifier
- Numerical theorem evidence: none

## 1. Result

The repaired candidate and reconciliation pass the requested
post-repair audit.  The earlier adverse owner finding resulted from
treating the blind packet's phrase “two-far mask \(P_1\)” as a
definition.  The authoritative accepted Round-193 partition instead
defines

\[
 P_1=\mathbf1_{|d-(d,d')m|>D_L},
\]

with no upper-far predicate.  Under that definition the forced fourth
corner is exactly in \(P_1\) for every sufficiently large live shell.
The repaired candidate and reconciliation now state this definition
explicitly and make no upper-far claim.

The whole-allocation triangle remains exactly \(P_2\)-preserving; the
distinct partial-block construction still has unequal transported masks;
the actual character and endpoint residual remains exact; and the final
conclusion remains restricted to the frozen cellular-boundary mechanism.

## 2. Authoritative partition check

The accepted Round-193 kernel defines

\[
 P_{\rm cl}
 =\mathbf1_{|d-gm|\le D_L}
  \mathbf1_{|d'-gm'|\le D_L},
\]

and then the disjoint first-failure masks

\[
\begin{aligned}
 P_1&=\mathbf1_{|d-gm|>D_L},\\
 P_2&=\mathbf1_{|d-gm|\le D_L}
       \mathbf1_{|d'-gm'|>D_L}.
\end{aligned}
\]

Consequently

\[
 1=P_{\rm cl}+P_1+P_2
\]

on the opposing physical source.  The second defect is intentionally
irrelevant after the lower defect has failed.  Thus “lower-far and
upper-close” is a \(P_1\) atom, not an omitted fourth class.

The same kernel records the live-shell fact \(m\ge cL\) and
\(D_L\le2\sqrt L\).  At the aligned \(V_E\) vertex of the repaired
triangle, \(m=qu\), so the candidate's notation \(qu\gg L\) is licensed
by the accepted shell support.

## 3. Re-audit of the repaired four-state obstruction

Write the squarefree cross-gcd factorization as

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv.
\]

For one odd squarefree block \(q>1\), the whole-allocation vertices

\[
\begin{aligned}
 V_B&=(Ax,qu,Aqy,v),\\
 V_E&=(Ax,qu,Av,qy),\\
 V_C&=(Aqu,x,Av,qy)
\end{aligned}
\]

have recomputed gcd \(A\) and the identical defects

\[
 A|x-qu|\le D_L,\qquad A|qy-v|>D_L.
\]

The upper, lower, and simultaneous maps are the complete allocation
involutions on \(C=1,B=1,E=1\), respectively.  Their parity and
transported-support qualifications are now stated in the candidate.
Thus the triangle is genuinely \(P_2\)-preserving on its live
intersection and total-zero-extended elsewhere.

The separate partial-block construction beginning at

\[
 (g\kappa a,hb,gc,\kappa he)
\]

instead changes its lower and upper defect expressions.  Its three masks
are those in (199.K21)/(199.R6), and their differences are the literal
commutators in (199.K22)/(199.R7).  The repaired candidate does not use
this partial construction to justify the whole triangle.

On the aligned face,

\[
 p=\chi_4(qxu)=-1,
\]

and the two lower-swapped vertices have the code-mismatch predicate
required for \(P_{\partial\mathrm{lit}}\); the \(B=q\) vertex lies in
\(P_{g\mathrm f}\).  The actual character quotients around the whole
triangle are \(t,p,tp\), with product \(1\).  Hence no artificial
negative sign is assigned to the simultaneous edge.

With the repaired candidate's endpoint notation, the physical triangle
after extraction of its common character and phase is

\[
 \Sigma_{BEC}
 =u_0\overline{\ell_0}
  +t u_1\overline{\ell_0}
  +tp u_1\overline{\ell_1}.
\]

The unique fourth product corner is

\[
 V_A=(Aqu,x,Aqy,v),\qquad (Aqu,Aqy)=Aq,
\]

with relative character \(p\), and

\[
 \Sigma_{BEC}
 =(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
  -p u_0\overline{\ell_1}.
\]

Therefore \(p=-1\) leaves
\(u_0\overline{\ell_1}\) with relative coefficient \(+1\) when
\(V_A\) is omitted.  The full residual also retains the extracted common
character and \(\Phi_{r,\sigma}(N)\).  The endpoint, character,
orientation, and conjugation bookkeeping is exact.

## 4. Exact \(P_1\) owner proof

At \(V_A\), the recomputed gcd is \(Aq\), so its lower first-failure
quantity is

\[
 \Delta_L(V_A)=Aq|u-x|.
\]

Put \(e=x-qu\).  The common \(P_2\) condition gives
\(|e|\le D_L/A\).  Since \(q\) is odd and \(q>1\), \(q\ge3\), while live
support at \(V_E\) gives \(qu\ge cL\).  Hence

\[
\begin{aligned}
 |u-x|
 &=|(q-1)u+e|\\
 &\ge (q-1)u-|e|\\
 &\ge \frac23\,qu-\frac{D_L}{A}\\
 &\ge \frac{2c}{3}L-2\sqrt L.
\end{aligned}
\]

For all sufficiently large \(L\), this is \(\gg L\); multiplying by
\(Aq\ge3\) proves

\[
 \Delta_L(V_A)>D_L.
\]

Thus \(P_1(V_A)=1\) under the exact Round-193 definition.  No assertion
about

\[
 Aq|y-v|
\]

is needed or made.  The finite control in the earlier review had
\(\Delta_L(V_A)>D_L\) and an upper-close value.  It therefore confirms,
rather than refutes, this lower-first-failure classification.

Bounded shells remain an absolute finite exception exactly as stated in
the candidate; they do not turn the asymptotic fourth corner into a
target-safe boundary.

## 5. Controls and outcomes

1. **Authoritative owner definition:** pass.  Candidate (199.K19a) and
   reconciliation (199.R14a) match the accepted Round-193 partition.
2. **Fourth-corner gcd and lower defect:** pass.  They are \(Aq\) and
   \(Aq|u-x|\), and the accepted shell lower bound proves lower failure
   for sufficiently large live shells.
3. **Upper-status control:** pass.  The repaired artifacts explicitly
   deny an upper-far assertion; upper-close and upper-far corners are both
   contained in \(P_1\).
4. **Whole-allocation \(P_2\) control:** pass.  All three lawful vertices
   have identical two-defect values and recomputed gcd \(A\).
5. **Partial-block distinction:** pass.  Its unequal masks are retained
   only as a separate commutator control.
6. **Actual incidence and endpoint control:** pass.  Quotients
   \(t,p,tp\), holonomy \(1\), the positive simultaneous sign on the
   alternating sector, and the coefficient-one missing atom are exact.
7. **Operator and scope control:** pass.  The obstruction is physical
   before the packet/orientation split, no premature modulus is taken,
   capacities are not lower bounds, and no theorem outside the specified
   mechanism is claimed.

## 6. First doubtful step and state effect

There is no remaining doubtful step in the finite allocation,
character, endpoint, or first-failure-owner kernel of the
mechanism-scoped no-go.  Literal nonemptiness, endpoint nonvanishing, and
the desired three-piece estimate by another coefficient-sensitive
method remain deliberately unproved and are not consequences of this
candidate.

The earlier REPAIR verdict based solely on a supposed upper-far
requirement is withdrawn.  Recommended state effect: accept the repaired
candidate as a durable route boundary for the frozen cross-gcd
cellular-boundary mechanism, subject to the other scheduled seam reviews;
promote no \(P_2\), \(P_1\), parent, endpoint, bridge, global, or exponent
claim.

## 7. Dependencies

This post-repair audit used the relevant partition and shell-bound lines
of
proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md,
the repaired formal candidate, the repaired conductor reconciliation,
and the prior statement-only derivation.  No sibling Round-199 report or
proof-state graph was read.

PASS
