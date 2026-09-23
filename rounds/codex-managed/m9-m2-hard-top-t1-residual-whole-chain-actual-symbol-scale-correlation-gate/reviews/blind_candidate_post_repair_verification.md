# Round 175 blind candidate post-repair verification

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Round: 175
- Role: blind post-repair verifier
- Candidate: formalized_whole_chain_scale_telescope_obstruction.md
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Evidence status: verification only; no candidate or shared-state edit

## 1. Verdict

\[
\boxed{\mathrm{GREEN}}
\]

Every mathematical repair requested in
blind_post_unmask_endpoint_telescope_review.md is present and correct. No
remaining coefficient, normalization, scale-Abel, endpoint, terminal-link,
ordinary-zero, K26, diagnostic-scope, tag, display, or byte-level defect was
found.

The candidate remains an obstruction only. GREEN does not prove K26,
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\), or the residual target.

## 2. Repair-by-repair verification

| Repair seam | Status | Verification |
|---|---|---|
| Physical transform (175.C3) | GREEN | The physical polynomial \(\sum_N(-1)^{\epsilon N}z_Ne(N\theta)\), the \(+i/2\) character transform, and the decomposition \(Z_{\epsilon,0}+Z_{\epsilon,*}\) now appear in one exact display. |
| Constants in (175.C6) | GREEN | The text now states \(|i/2|^2=1/4\), parity average \(1/2\), total \(1/8\), with one outer real part. |
| Weighted Abel identity (175.C8) | GREEN | The previously missing \(+\) precedes \(\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*\). |
| Collective zero sector (175.C11a)--(175.C13) | GREEN | The \((0,0)\), \((0,*)\), and \((*,0)\) pieces are exactly \(|Z_{\epsilon,0}|^2+2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})\), counted once after odd-character recombination. The whole chain telescopes to the single endpoint \(\mathcal Z_{R_0,M}\), and its displayed bound has target size. |
| Physical \(A_r,T_{26},B_{\mathrm{short}}\) | GREEN | (175.C13a)--(175.C13b) define all three explicitly. \(T_{26}\) is exactly the left side of (165.K26), and (175.C14) pays \(B_{\mathrm{short}}\) once. |
| K26 identity (175.C15) | GREEN | The sign and factor are correct: \(\sum_j\mathcal N_j=2(T_{26}+B_{\mathrm{short}})-\mathcal Z_{R_0,M}\). |
| Terminal cases | GREEN | (175.C2) distinguishes an exact final doubling from the possible strict link \(R_{K-1}<M<2R_{K-1}\); (175.C8b) is used only at doublings. |
| Lower endpoint and maximal equivalence | GREEN | (175.C17a) proves \(Q_{R_0}^*\ll L^3X^\varepsilon\); positivity then makes (175.C17b) a valid equivalence of one-sided upper bounds. |
| Physical versus transformed diagonals | GREEN | (175.C9)--(175.C10) are explicitly limited to physical integer gaps. A fixed transformed tuple receives only the endpoint telescope and is not deleted. |
| Diagnostic scope | GREEN | (175.C18)--(175.C20) are explicitly a complete physical parity-Fejer diagnostic, not a literal \(Q_M^*\) or K26 lower bound. The separate abstract \(Z_*\) control (175.C20a) is also labeled nonliteral. |

## 3. Independent equation checks

Let

\[
 A_{\epsilon,*}
 =\sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}
 U_{k,\ell}^{(\epsilon)}.
\]

From (175.C4),
\(Z_{\epsilon,*}=(i/2)A_{\epsilon,*}\). Therefore

\[
 {1\over2}\sum_\epsilon\int B_{R,S}|Z_{\epsilon,*}|^2
 ={1\over8}\sum_\epsilon\int B_{R,S}|A_{\epsilon,*}|^2
 =\mathcal N_{R,S},
\]

which rechecks (175.C6). Finite telescoping proves (175.C7), while
collecting each interior \(Q_{R_j}^*\) gives

\[
 \sum_ja_j(Q_{j+1}-Q_j)
 =a_{K-1}Q_K-a_0Q_0
 +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_j,
\]

so the repaired sign in (175.C8) is correct.

Expanding
\(|Z_{\epsilon,0}+Z_{\epsilon,*}|^2\) proves (175.C12). The bound in
(175.C13) follows from

\[
 \|F_M-F_{R_0}\|_\infty\le M+R_0,\qquad
 \|Z_\epsilon\|_2=D_L^{1/2},\qquad
 \|Z_{\epsilon,0}\|_2\ll_\eta L^2J^{-1}X^\eta,
\]

together with \(M\asymp L^2\) and \(L^2\le J\).

The physical parity identity (175.C13aa) yields

\[
 {1\over2}
 \left(\mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}\right)
 =B_{\mathrm{short}}+T_{26}.
\]

Combining this with (175.C12)--(175.C13) proves (175.C15). Thus the
Round-175 target and K26 are equivalent one-sided upper bounds at target
strength.

Finally, (175.C16) and \(F_{R_0}\le R_0\) give

\[
 Q_{R_0}^*
 \le {R_0\over2}\sum_\epsilon\|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.
\]

Hence the forward direction of (175.C17b) adds a target-safe lower
endpoint, while the reverse direction subtracts the nonnegative
\(Q_{R_0}^*\). Both directions are valid.

For the physical diagnostic, direct summation gives

\[
 \mathfrak E_M^{(2)}
 =2P+P^{-1}\sum_{t=1}^{2P-1}t^2
 ={8P^2+1\over3},
\]

and the lower bound (175.C19) follows for \(n\ge3\). With \(X=L^8\),
\(J=L^4\) and \(H=L^2\), so (175.C20) is admissible. Its revised prose
correctly quarantines this calculation from the literal \(Q^*\) sector.

## 4. First doubtful or unproved step

No doubtful step remains in the repaired endpoint telescope, normalization,
ordinary-zero restoration, once-only short correction, K26 equivalence, or
diagnostic scope. The first unproved mathematical statement is still the
complete literal coefficient-sensitive endpoint estimate

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon,
\]

equivalently K26 after the target-safe collective seams. This verification
does not prove that estimate or any downstream owner.

## 5. Structural and file-integrity controls

- All 36 equation tags are unique:
  (175.C0), (175.C0a), (175.C1), (175.C2), (175.C2a),
  (175.C2b), (175.C3)--(175.C8), (175.C8a)--(175.C8b),
  (175.C9)--(175.C11), (175.C11a), (175.C12)--(175.C13),
  (175.C13a), (175.C13aa), (175.C13b), (175.C14)--(175.C20),
  (175.C20a), (175.C21), (175.C22), and (175.C22a).
- Display delimiters balance: 36 openings and 36 closings.
- Aligned environments balance: four beginnings and four endings.
- Embedded carriage returns: 0.
- Tab bytes: 0.
- NUL bytes: 0.
- Unicode theta substitutions: 0.
- No accidental patch-prefix line remains.

## 6. Dependencies

The verification used:

1. the revised candidate
   rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/candidates/formalized_whole_chain_scale_telescope_obstruction.md;
2. the prior seam requirements in
   rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/reviews/blind_post_unmask_endpoint_telescope_review.md;
3. the accepted Round-165 kernel
   proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md; and
4. the accepted Round-172 kernel
   proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md.

No sibling review, synthesis, candidate edit, shared-state edit, web source,
or numerical experiment was used.

## 7. State-scope recommendation

The revised candidate passes this seam and may be retained under the
route-scoped label

\[
 \texttt{whole\_chain\_actual\_symbol\_capacity\_or\_self\_return\_no\_go}.
\]

Its durable conclusion is only that the unweighted stopped chain is one
endpoint difference, the lower endpoint is target-safe, and
coefficient-independent scale manipulations do not provide the missing
factor \(L\). The open theorem is still
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\), equivalently K26 modulo the
collective target-safe seams.

No implication edge is licensed. The candidate proves neither K26 nor the
complete residual scalar, full \(t=1\), another hard-TOP channel, hard TOP,
BAL, UNBAL, M9--M2, either M1 route, endpoint uniformity, M9, a bridge, the
quarter theorem, or an exponent.
