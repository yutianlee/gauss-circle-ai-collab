# Round 168 conductor adjudication

## 1. Result and terminal decision

Round 168 closes under

\[
 \boxed{\texttt{strict\_t1\_mellin\_euler\_sector}.}
\]

The complete polynomial-range \(t=1\) estimate is not proved.  The round
does prove one homogeneous internal reduction and one complete strict
sector.  The intact arithmetic family factors as

\[
 D(s_1,s_2)=L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2),
\tag{168.A1}
\]

with \(G\) holomorphic for \(\Re s_1,\Re s_2>1/2\).  An exact cardinal
Mellin interpolation gives

\[
 \mathcal S_{L,1}=R_\zeta+\mathcal I_\eta,
 \qquad R_\zeta\ll_\varepsilon L^2J^{-1}X^\varepsilon,
\tag{168.A2}
\]

so the first open theorem is the signed two-height estimate

\[
 \mathcal I_\eta\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{168.A3}
\]

For every fixed \(B>0\), the complete full scalar is target-safe when
\(L\le(\log X)^B\).  For every fixed \(B,\kappa>0\), the residual in the
accepted canonical \(\kappa\)-dependent close-prime decomposition is
target-safe on the same sector.

Inside this accepted strict-sector result, the interface no-go is narrow.
It rejects only the two named absolute placements on the favorable
recombined smooth/BV control, the inspected source placements, and a bare
functional-equation analogy.  It is not a physical lower bound and not a
no-go for a new signed weighted hybrid theorem.

## 2. Accepted internal kernel

For odd primes, the local state space is exactly
\(1+\chi_4(p)p^{-s_1}+p^{-s_2}\); at \(2\), oddness of the first leg gives
\(1+2^{-s_2}\).  Removing the local factors of
\(L(s_1,\chi_4)\zeta(s_2)\) gives

\[
 G_2=1-2^{-2s_2},\qquad
 G_p=(1+x_p+y_p)(1-x_p)(1-y_p),
\tag{168.A4}
\]

and the quadratic start of \(G_p-1\) proves absolute local-uniform
convergence in the required half-plane.

Choose a smooth bump supported in \((-1/3,1/3)\) and place one disjoint
cell at every literal lattice sample.  This encodes all hard values,
floors, stars, half-open faces, endpoints, and zero values exactly.  Move
the \(s_2\)-contour first while \(\Re s_1>1\).  The sole pole is
\(s_2=1\), whose coefficient series is

\[
 L(s,\chi_4)G(s,1)
 =\frac1{\zeta(2)}
 \sum_{\substack{n\ge1\\n\ {\rm odd,\ squarefree}}}
 \frac{\chi_4(n)}{n^s}
 \prod_{p\mid n}(1+p^{-1})^{-1}.
\tag{168.A5}
\]

On each cardinal cell, the remaining phase derivative is \(\asymp J\).
One integration by parts gives \(J^{-1}\), and \(O(L^2)\) cells give the
safe residue in (168.A2).  This reduction is exact, but the cardinal
interpolation is an identity device with \(O(L^2)\) cell complexity, not
an analytic smoothing theorem.

On a favorable recombined smooth/BV control, radial stationarity has
length \(T\asymp JL\) and pointwise transform scale
\(L^{2\eta}\sqrt{L/J}\).  Before epsilon absorption, pointwise triangle
and fixed-angular mean-square Cauchy each give

\[
 L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
\tag{168.A6}
\]

For a requested final epsilon, choose \(\eta\) after epsilon and then
choose \(\delta\) smaller.  This absorbs \(L^{2\eta}X^\delta\), but the
structural \(\sqrt J\) remains.

Finally, the literal support has \(O(L^2)\) bounded terms.  The extra
\(L^{1/2}\) over the target is absorbed into \(X^\varepsilon\) whenever
\(L\le(\log X)^B\).  Exact subtraction of the accepted fixed-\(\kappa\)
XOR sector transfers this strict result to its residual complement.

## 3. Source and interface adjudication

The dated source audit checks exact hypotheses and power placement for
Topacogullari's common-height pointwise, absolute moment, positive second
moment, and approximate-functional-equation results; Bourgain's
pointwise zeta bound; Ramana--Ramare's exact Perron formula with its local
boundary correction; and Durkan--Karak--Mahatab's conditional positive
shifted moments.  None estimates the independent-height signed nonlinear
weight in (168.A3), and none is used to prove the internal kernel.

No exact coefficient bridge from factorwise functional equations or
approximate functional equations to the Round-162 collar has been
proved.  The only lawful comparison is inherited: deliberately reopen the
original squarefree/coprime projector and then apply the accepted positive
physical Poisson calculation.  Its capacity is \(\sqrt{JL}\), with ratio

\[
 \frac{\sqrt{JL}}{L^{3/2}}
 =\frac{\sqrt J}{L}
 =\frac HL+O(L^{-1}).
\tag{168.A7}
\]

The exact cardinal residue and the blind exact Stieltjes residue belong to
different interpolations.  The former is target-safe by continuous
nonstationary integration; the latter is a discrete oscillatory sum and
does not inherit that saving.  No residue comparison across the two
models is promoted.

## 4. First doubtful or unproved step

After removing the target-safe pole, the first open statement is exactly
(168.A3) for a chosen endpoint-lawful transform, or an equivalent physical
estimate.  A successful proof must retain cancellation between the radial
stationary phase and the two arithmetic factors before absolute values,
while paying the actual angular behavior and interpolation complexity.

Round 168 supplies no such signed theorem.  It also supplies no natural
continuous-plus-atoms decomposition, no factorwise-FE/AFE self-return, and
no polynomial-\(L\) residual estimate.

## 5. Required controls and outcomes

Every required control is recorded in
`controls/conductor_round168_controls.md`.  Euler algebra, literal cardinal
inversion, the pole coefficient, residue bound, floor normalization,
statement-only independence, source hypotheses, epsilon ordering,
fixed-\(B\) full/residual sectors, and downstream scope are green.  The
signed two-height target, polynomial range, functional-equation bridge,
and target-safe global transform control remain open.  No numerical
experiment was used.

## 6. Dependencies and exact artifacts used

The accepted internal reduction is formalized in
`proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md`.
It uses the accepted Round-162 literal scalar/collar statement and the
Round-163 fixed-\(\kappa\) XOR connector.  Its new Euler, cardinal,
residue, capacity, and polylogarithmic arguments are internal.

The adjudication uses all three Round-168 reports, the repaired claimant
review, the repaired conductor candidate, both final candidate reviews,
the final kernel verification, the graph-scope review, and the conductor
control ledger.  Source-facing conclusions remain route-audit evidence
rather than proof of the internal node or any parent.

## 7. Recommended state effect

Create one `proved_internal` reduction node containing only the exact
Euler factorization, cardinal Mellin identity, target-safe zeta residue,
signed two-height reduction, the two named absolute-capacity ledgers, and
the fixed-\(B\) full/residual sectors.  Attach it only as inconclusive
evidence to the open hard-TOP owners.  Record the scoped false
implications and source-route failures as rejected claims.

Keep the general full \(t=1\) scalar, general residual, K17a, K26, every
other few-point channel, hard TOP, BAL, UNBAL, M9--M2, both direct M1
parents, GAR, endpoint uniformity, M9, both bridges, the quarter theorem,
and both exponent ledgers unchanged.
