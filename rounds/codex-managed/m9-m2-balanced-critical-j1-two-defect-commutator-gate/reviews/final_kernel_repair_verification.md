# Final verification of the Round-171 kernel repairs

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Round: 171
- Role: post-repair independent verifier
- Starting graph SHA-256:
  `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Verdict: **GREEN**

## 1. Result

All requested post-review repairs are present and mathematically sound in
the current conductor kernel and candidate.  The invariant endpoint domain,
ordinary affine singular strip, geometric-versus-arithmetic support split,
exact edge expansion, commutator scope exclusion, and
capacity-versus-lower-bound wording now match the reviewed theorem.  No
further edit is required for these seams.

## 2. Exact repaired statement and hypotheses

The endpoint-swap calculation now uses the positive endpoint rectangle

\[
 I_h^2\times I_k^2,
\]

identified through the multiplicity-one shift chart with

\[
 \{(h,k,p,q):h,h+p\in I_h,\ k,k+q\in I_k\}.
\tag{171.K17a}
\]

The following prose explicitly says that this is the shifted image, not an
independent rectangle in \((h,k,p,q)\).  Both swaps preserve it, every phase
corner is positive, and coefficient zero extension absorbs literal support
failures.

The boundary indicator now uses only the positive geometric/profile support
of \(A_B\).  Both arithmetic low-gcd factors, including their holes and unit
differences, remain in the coefficient \(Y\).  Thus the length-\(L\)
ambient run and \(O(L^3)\) one-coordinate face count no longer rely on a
false interval description of the gcd cutoff.

## 3. Verification of repaired equations and scope

For the ordinary unnormalized operators
\(\mathcal C_s=2yT_s\), \(\mathcal C_q=xT_q\), the displayed identity

\[
 [\mathcal C_s,\mathcal C_q]=2(2y-x)T_sT_q
\]

has the correct sign and factor.  For fixed \(t=2y-x\), three endpoints
determine the fourth up to at most one admissible integer, so
\(|2y-x|\le C\) has absolute mass
\(O_{C,\varepsilon}(L^3X^\varepsilon)\).  Off the singular line, division
returns \(T_sT_q\), and finite reindexing gives exactly

\[
 \sum_{s,q}(-1)^s(T_sT_q-I)F(s,q)
 =-2\sum_{s,q}(-1)^sF(s,q).
\tag{171.K13a}
\]

Thus the ordinary placement is now priced just as the parity-compatible
\(y=x\) placement is priced.

On every oriented edge, the inserted formula

\[
\begin{aligned}
 I_+-I_0={}&(J_+-J_0)H^\Delta_+H^\rho_+\\
 &+J_0(H^\Delta_+-H^\Delta_0)H^\rho_+\\
 &+J_0H^\Delta_0(H^\rho_+-H^\rho_0)
\end{aligned}
\tag{171.K23a}
\]

expands algebraically to
\(J_+H^\Delta_+H^\rho_+-J_0H^\Delta_0H^\rho_0\); its signs and corner
placements are exact.  Together with (171.K23), it exposes precisely the
geometric support face and the two sharp-gate faces, while all gcd
differences remain in \(Y\).

The kernel now expressly limits (171.K11)--(171.K16) to the four displayed
elementary placements and the two displayed ordinary/parity-compatible
commutators.  It excludes the backward and composite Weyl commutators in the
ramp review, as well as coefficient-adapted and nonlocal operators.  The
candidate repeats the same narrow scope, so no universal commutator
classification is implied.

Finally, the kernel and candidate consistently describe \(L^4\) and
\(L^5\) as available coefficient-independent positive or adversarial
capacities, not literal lower bounds.  They also state that aliases and lifts
remain corner-dependent only if the accepted divisor-alias expansion is
opened; they are not presented as pre-existing coordinates of \(a_B^<\).

## 4. First doubtful or unproved step

The first unproved physical statement remains

\[
 |\mathcal R_B^{\rm osc}|\ll_\varepsilon L^3X^\varepsilon.
\]

The repaired text claims only that the currently audited local,
coefficient-independent placements do not prove this estimate.  It leaves
open a signed nonlocal actual-symbol primitive/correlation theorem and makes
no physical lower-bound claim.

## 5. Control outcomes

| repaired seam | outcome |
|---|---|
| invariant endpoint rectangle (171.K17a) | **GREEN.** Exact endpoint domain and invariant shifted image are stated. |
| ordinary \(2y=x\) singular strip | **GREEN.** Fixed-width count and off-strip tautology are both present. |
| geometric/profile support | **GREEN.** Arithmetic gcd holes are excluded from \(J\) and retained in \(Y\). |
| exact edge expansion (171.K23a) | **GREEN.** Three terms telescope to \(I_+-I_0\) with correct signs. |
| undisplayed composite Weyl operators | **GREEN.** Explicitly outside the kernel and durable node. |
| capacity versus lower bound | **GREEN.** Available positive ledgers are not promoted to literal mass. |
| alias/lift wording | **GREEN.** Corner dependence is asserted only after opening the accepted expansion. |
| downstream scope | **GREEN.** No target, parent, bridge, theorem, or exponent change is claimed. |

## 6. Formatting and artifact checks

The current kernel contains 29 distinct equation tags, from (171.K1)
through (171.K26), including the new (171.K13a), (171.K17a), and
(171.K23a).  No tag is duplicated.  Display-math delimiters are balanced;
the `aligned` and `array` environments are balanced; and the repaired
formulas contain no visible formatting corruption.  The candidate's
equation displays are likewise intact and its references to the repaired
kernel are consistent.

This verification used only the current on-disk kernel and candidate, plus
the exact repair requirements from
`reviews/final_commutator_kernel_verification.md`.  No numerical experiment,
computer algebra, source theorem, graph edit, or other artifact mutation was
used.

## 7. Recommended state effect and verdict

The repaired kernel may now support the proposed
`M9-M2-balanced-two-defect-commutator-ramp-obstruction` node as a
`proved_internal`, route-scoped obstruction with no implication edge.  The
critical oscillatory remainder and actual energy remain `open`; the separate
remaining-label owner, full BAL, M9--M2, M9, both bridges, `GC-target`, and
all exponent records remain unchanged.

**Final verdict: GREEN.**
