# Hostile profile, power, and scope review for Round 158

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Review seam: profile and boundary normalization; restored powers;
  scalar target; support localization; quarantine; downstream scope
- Reviewed claimant: reports/sign_adapted_cell_trace_attack.md
- Reviewed conductor candidates: conductor_round158_cell_trace_seed.md
  and conductor_round158_strict_survivor_audit.md
- Status: review evidence only

## 1. Result

**Hostile verdict: GREEN for a narrow promotion, with the original
conductor seed superseded on two calibrations.** The claimant's literal
boundary weights, selected quotient, \(V\asymp K\) localization,
all-\(d\) special-row power ledger, endpoint power, scalar target, and
outer/profile-bulk quarantine agree with the accepted Round 157 kernel.
No downstream transfer is licensed.

The two corrections absent or under-specified in the original conductor
seed are supplied correctly by the claimant and the later conductor
audit:

1. the selected character quotient
   \(\ell=(k^2-s)/N\) is not the profile argument; and
2. the scalar target is \(O_\varepsilon(X^\varepsilon)\), so the
   missing raw estimate is \(M^{3/4}X^\varepsilon\), not necessarily
   square-root size.

The zero and Nyquist Abel pieces and the full-frequency endpoint row
are proved at the stronger \(M^{-1/4}X^\varepsilon\) scale. The strict
selected trace remains open. The discrepancy and exponent-pair
calculations in claimant Section 3.6 are admissible only as diagnostics
for the named placements; they are not a general impossibility theorem
or an imported source theorem.

## 2. Exact statement and hypotheses reviewed

Retain

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 1\ll M\le N^{1/2},\qquad
 M^{3/4}(\log(2X))^A<V\le K.
\tag{R158.H1}
\]

For every odd \(d\mid N\), put
\(c=q/d\), \(H=c/2\), and \(n=H/2=N/d\). The accepted literal
coefficient is

\[
 B_j(x)=
 \mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{R158.H2}
\]

where the actual off-congruence extension, zero extension, component
transitions, half-open choices, and hard endpoints remain fixed. Its
amplitude and zero-extended profile variation are

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{R158.H3}
\]

The reviewed object is only the moving-mask cell trace inside the
paired interior frequencies \(v\ne0,H/2\). The positive right Abel
endpoint, negative left Abel endpoint, two profile-difference
remainders, and external \(B_{1,U}(1)\) factor are separate seams.

The campaign target for this normalized \(D=1\) scalar is

\[
 \mathcal C_{\mathrm{int},U}(V)
 \ll_\varepsilon X^\varepsilon.
\tag{R158.H4}
\]

Any \(M^{-1/4}X^\varepsilon\) statement is stronger than (R158.H4);
it must not be used to redefine the target.

## 3. Hostile derivation and seam audit

### 3.1 Boundary-weight normalization

At the positive moving atom, \(j=k-1\) and \(x=k\). Formula (R158.H2)
therefore gives exactly

\[
 W_+(k)=F_{k-1}(k)=
 w_U\!\left(\frac{k^2-k+1}{N}\right)
 e\!\left(\sqrt{k^2-k+1}-k\right).
\tag{R158.H5}
\]

At the negative moving atom, \(j=-k\) and \(x=k\), hence

\[
 W_-(k)=F_{-k}(k)=
 w_U\!\left(\frac{k^2+k}{N}\right)
 e\!\left(\sqrt{k^2+k}-k\right).
\tag{R158.H6}
\]

These are the claimant's formulas (158.R5) and the conductor audit's
(158.CA4)/(158.CA6). They have the correct phase signs and contain no
missing \(N\), \(q\), \(d\), or Fourier factor. The all-\(d\)
normalization has already disappeared only because complete
half-period inversion returns the physical selector \(G_N\).

For a strict selected term, \(k^2-s=N\ell\). Consequently

\[
\begin{aligned}
 \ell-\frac{k^2-k+1}{N}
 &=\frac{k-1-s}{N}>0
 &&\text{on the positive strict trace},\\
 \frac{k^2+k}{N}-\ell
 &=\frac{k+s}{N}>0
 &&\text{on the negative strict trace}.
\end{aligned}
\tag{R158.H7}
\]

Thus the claimant correctly refuses to replace either boundary
argument by \(\ell\). A half-open off-congruence convention may identify
one side with an adjacent sample in a particular component, but it
cannot identify both literal weights with one common \(w_U(\ell)\)
without a new lemma.

The original conductor seed (158.C20) is too schematic for promotion
on this seam: its generic indicators do not print (R158.H5)--(R158.H7).
The later conductor audit and claimant repair it exactly.

### 3.2 Localization to the top block

The moving atom has \(k\asymp V\). If either (R158.H5) or (R158.H6) is
nonzero, the inherited fixed-dilate \(M\)-support gives

\[
 \frac{k^2+O(k)}{N}\asymp M.
\tag{R158.H8}
\]

Since \(k\) is large in the frozen range, (R158.H8) is equivalent, up
to the literal support constants, to

\[
 k\asymp\sqrt{NM}=K,\qquad V\asymp K.
\tag{R158.H9}
\]

The claimant's exact support-disjointness test is therefore valid:
blocks whose boundary arguments miss \(\operatorname {supp}(w_U)\)
have zero moving-cell trace. This says nothing about the Abel outer
terms or profile-bulk differences.

Localization is not cancellation. Since \(M\le N^{1/2}\),

\[
 \frac KM=\sqrt{\frac NM}\ge N^{1/4},
\tag{R158.H10}
\]

so on every nonzero trace block \(V\asymp K\gg M\). The corrected
incidence capacity becomes
\[
 L_{\rm str}(V)\ll_\varepsilon
 \min(M,V)X^\varepsilon
 =O_\varepsilon(MX^\varepsilon),
\tag{R158.H11}
\]
not a target bound. The conductor's explicit survivor family is
properly qualified: it proves an admissible strict arithmetic point
can occur in this top region if the inherited component is nonzero at
the displayed off-integer argument; it proves neither actual nonzero
weight nor large signed mass for a fixed component.

### 3.3 Restored powers and target calibration

Write

\[
 a=M^{-3/4}X^\varepsilon.
\tag{R158.H12}
\]

For either removed trace frequency \(v=0\) or \(v=n\), opening the
accepted theta kernel and summing its nonzero additive unit frequencies
over a prefix or suffix gives \(O(c\log(2c))\). Restoring every factor,

\[
\begin{aligned}
 |\mathcal Z_{\rm tr}|+|\mathcal F_{\rm tr}|
 &\ll_\varepsilon
 \frac{aV}{Nq}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}d\,c^{3/2}X^\varepsilon\\
 &=
 O_\varepsilon\!\left(
 a\frac{V}{\sqrt N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}d^{-1/2}
 X^\varepsilon\right)\\
 &\ll_\varepsilon a\sqrt M\,X^\varepsilon
 =M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{R158.H13}
\]

The equality uses \(c=q/d\); no divisor stratum, \(c=4\) case, or
positive power of \(d\) is missing. The claimant's (158.R30) is GREEN.

The full-frequency endpoint row has at most
\(O_\varepsilon(N^\varepsilon)\) entries in each \(V<N\) block, so its
cost is

\[
 O_\varepsilon(aN^\varepsilon)
 =O_\varepsilon(M^{-3/4}X^\varepsilon),
\tag{R158.H14}
\]

again stronger than the scalar target.

For the strict survivor, (R158.H11) gives only

\[
 |\mathcal S_{\rm str}(V)|
 \ll_\varepsilon aM X^\varepsilon
 =M^{1/4}X^\varepsilon.
\tag{R158.H15}
\]

The actual requirement is

\[
 |\mathcal S_{\rm str}(V)|
 \ll_\varepsilon X^\varepsilon,
\quad\text{equivalently raw mass }
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{R158.H16}
\]

Thus a factor \(M^{1/4}\) saving over absolute mass is required.
Square-root raw mass \(M^{1/2}\) would give the stronger
\(M^{-1/4}\) weighted bound, but is not necessary. The claimant and
later conductor audit are calibrated correctly; the original seed
must not be read as making square-root cancellation the minimal target.

### 3.4 Diagnostic methods

The claimant's Erdős--Turán, second-derivative, classical exponent-pair,
and centered-completion ledgers restore the right formal powers. In
particular, the named standard placements become scalar-target sized
only at \(M\ge N^{2/3}\), outside (R158.H1).

This conclusion is route-scoped. The claimant explicitly freezes
slowly varying mask boundaries and grants normalized BV before applying
those estimates. Therefore these calculations may be retained as
diagnostic capacities for those placements, but not promoted as a
theorem that every discrepancy, exponent-pair, incomplete-quadratic,
or joint mask-preserving method must fail.

### 3.5 Quarantine and downstream scope

The complete Abel identities contain

\[
 A_{b_+}(v)P^+_{d,v}(b_+),\qquad
 A_{a_-}(v)P^-_{d,v}(a_-),
\tag{R158.H17}
\]

and the two profile-difference remainders. The claimant prints all four
objects and then sums only the moving-atom lines into
\(\mathcal C_{\mathrm{int},U}(V)\). This is the correct quarantine.
Neither the stronger special-row errors nor a future strict-trace
theorem would estimate (R158.H17) or the profile bulk.

The external \(B_{1,U}(1)\) factor remains a separate
\(O_\varepsilon(X^\varepsilon)\) assembly seam. No result here
transfers to the full paired matrix, \(D>1\), \(L>1\), generic
\(t=1\), \(t\ge2\), cross, another M1 owner, M2, endpoint uniformity,
M9, the bridge, the quarter target, or a global exponent. The claimant
and both conductor candidates respect this downstream quarantine after
the seed is read together with the later audit.

## 4. First doubtful or unproved step

There is no remaining profile-normalization, support-localization,
special-row power, endpoint-power, scalar-target, or quarantine defect
in the claimant's final formulas.

The first unproved mathematical step is the literal signed estimate

\[
 \left|\sum_{\ell}\chi _4(\ell)
 \left[
 \mathbf1_{\rm pos}W_+(k_\ell)
 +\mathbf1_{\rm neg}W_-(k_\ell)
 \right]\right|
 \ll_\varepsilon X^\varepsilon,
\tag{R158.H18}
\]

with the exact strict selectors, boundary arguments (R158.H5)--(R158.H7),
residual phases, component transitions, half-open conventions, and hard
endpoints. In raw normalization this is the \(M^{3/4}\) bound
(R158.H16). Cardinality, endpoint roots, localization, ordinary
\(\chi _4\) partial summation, and the diagnostic placements in
claimant Section 3.6 do not prove it.

The first artifact-level caveat is narrower: the original conductor
seed should not be promoted alone because its selected coefficient is
schematic and its discussion can be misread as requiring square-root
rather than raw \(M^{3/4}\). The later conductor audit and claimant
fully repair those seams.

## 5. Required control tests and outcomes

The hostile controls give the following ledger.

1. **Literal profile test: GREEN.** Substitution into (R158.H2) gives
   \(W_+(k)\) at \((k^2-k+1)/N\) and \(W_-(k)\) at
   \((k^2+k)/N\), with the phases printed in (R158.H5)--(R158.H6).
   Neither is silently evaluated at the selector quotient
   \(\ell=(k^2-s)/N\).
2. **Half-open and component test: GREEN with an inherited-data
   caveat.** The formulas preserve rather than smooth across
   off-congruence values, component transitions, and hard endpoints.
   No equality of adjacent profile samples is asserted without an
   inherited interpolation lemma.
3. **Top-block localization test: GREEN as a zero statement only.** A
   nonzero moving atom forces \(V\asymp K\). On that range
   \(\min(M,V)=M\), so localization supplies no target-sized estimate.
4. **All-divisor special-row test: GREEN.** Restoring \(1/(Nq)\),
   \(d\sqrt c\), the interval bound \(c\log c\), \(c=q/d\), the
   \(O(V)\) atom count, and the odd-divisor sum gives (R158.H13).
   The \(c=4\) interior set is empty and creates no exceptional term.
5. **Endpoint test: GREEN.** The local root table gives only
   \(O_\varepsilon(N^\varepsilon)\) classes in a block of length
   \(<N\), hence (R158.H14). This estimate does not leak into the
   strict prefix or suffix.
6. **Target test: GREEN.** The required weighted strict estimate is
   \(O_\varepsilon(X^\varepsilon)\), equivalently raw
   \(O_\varepsilon(M^{3/4}X^\varepsilon)\). A raw square-root estimate
   is sufficient but unnecessarily strong.
7. **Strict-survivor test: GREEN for arithmetic survival only.** The
   dyadic family in the conductor audit produces a positive strict
   selected point with nonresonant endpoint polynomial. Actual nonzero
   profile value and a lower bound for the signed sum remain
   conditional and are not claimed.
8. **Outer/profile-bulk quarantine test: GREEN.** Both Abel outer
   terms in (R158.H17) and both profile-difference remainders stay
   outside the cell trace. They are not labelled target-safe.
9. **Method-scope test: GREEN after restriction.** The threshold
   \(M\ge N^{2/3}\) is a capacity calculation for the explicitly named
   discrepancy, exponent-pair, and completion placements only. It is
   not a general no-go theorem.
10. **Downstream test: GREEN.** The external scalar seam and every
    broader \(D,L,t\), matrix, M1/M2, M9, bridge, quarter-target, and
    global-exponent claim remain unpromoted.

No numerical experiment or web source is needed for these algebraic
and power-counting controls.

## 6. Dependencies and exact artifacts used

This review used the following exact artifacts:

1. `protocol.md` for the report contract and proof-state discipline;
2. `proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md` for the
   accepted Round 157 literal coefficient, inversion normalization,
   special-frequency conventions, and external-seam scope;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reports/sign_adapted_cell_trace_attack.md`
   as the reviewed claimant;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/candidates/conductor_round158_cell_trace_seed.md`
   as the original schematic conductor candidate;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/candidates/conductor_round158_strict_survivor_audit.md`
   as the calibration and survivor control; and
6. `proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md`
   as a line-by-line consistency check of the current exact reduction,
   not as an independent premise replacing the Round 157 kernel.

No shared state, candidate, report, proof kernel, synthesis, control,
or State Patch was edited. This review writes only the assigned review
artifact.

## 7. Recommended state effect

Promote narrowly the literal boundary normalization
(R158.H5)--(R158.H7), the exact \(V\asymp K\) zero range with no
on-support saving, the all-divisor special-row and endpoint powers,
the scalar-target calibration (R158.H16), and the explicit quarantine
and downstream scope. Retain the survivor family only as evidence that
strict arithmetic points exist, conditional on the literal component
weight being nonzero. Retain Section 3.6 only as a route-specific
capacity audit.

Do not promote the original conductor seed by itself: revise its use
so that its schematic selected coefficient is always replaced by the
literal two-profile formula and its square-root discussion is read as
sufficient rather than necessary. Do not promote a strict-trace
theorem, an actual nonzero-weight lower bound, a universal method
no-go, any Abel outer/profile-bulk bound, or any downstream transfer.

**Decision: PROMOTE the narrow profile/power/quarantine package; REVISE
the original conductor seed before citation.**

**First unproved step: prove the literal strict signed selected sum is
\(O_\varepsilon(X^\varepsilon)\), equivalently that its raw
character-mask mass is
\(O_\varepsilon(M^{3/4}X^\varepsilon)\).**
