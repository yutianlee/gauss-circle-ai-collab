# Round221 review of the endpoint-ceiling chain closure

## 1. Result and final-hash verdict

**GREEN at the revised final control hash**
de4aca2122c9f452e03a3456bfe40b80af4fbe5d9da47b3e04ccf3c747e2ed11.

The finite algebra, effective level, both localization terms, and the comparison with the accepted direct certificate are correct. The conductor incorporated the requested explicit treatment of \(v_{\rm eff}<1\), microscopic localization, and a localization length exceeding the window. No exponent or finite-inequality repair was needed.

The conclusion is narrowly scoped: closing the fixed-vector chain by a same-block scalar ceiling and the same Gram operator norm cannot improve the direct coefficient-uniform certificate. This does not bound the actual measure from below, rule out signed fixed-vector correlations, or improve the full moment.

This is a post-isolation application review. I authored the frozen finite Gram report used as an input, and do not count the present review as an independent review of my own finite proof.

## 2. Exact hypotheses and accepted binding

For the finite calculation, let \(U\) be a \(J\)-by-\(n\) complex matrix, \(b\) a prescribed vector,
\[
 f=Ub,\quad G=UU^*,\quad B=\|b\|_2^2,\quad
 a_k=f^*G^{k-1}f.
 \tag{1}
\]
Take a fixed integer \(k\geq2\), \(B>0\), and a nonempty row set satisfying
\[
 v\leq |f_j|\leq W,\qquad v>0,\qquad \|G\|\leq L.
 \tag{2}
\]
Thus \(W\geq v>0\). Empty high sets, or zero \(B,W,L\) that force them, are treated before division.

The conditional block application uses the exact accepted204 finite mechanism:
\[
 S(R)=\sum_{N<n\leq2N}b_ne(R\sqrt n),\qquad
 B=\sum_n|b_n|^2\leq A N^{-1/2},
 \tag{3}
\]
where \(A\geq1\), \(1\leq N\leq T^{3/2}\), \(T\geq2\), and the radius interval \(I\) has length at most \(C_1T\). Put
\[
 \delta=N^{-1/2},\qquad \kappa=\frac{13}{55},\qquad
 q=2+\frac2\kappa=\frac{136}{13}.
 \tag{4}
\]
The accepted unweighted correlation bound is
\[
 |K_N(u)|\leq A\sqrt N\bigl(|u|^\kappa+|u|^{-1}\bigr),
 \qquad 0<|u|\leq C_1T.
 \tag{5}
\]

The matrix for a selected radius set is the full ambient unweighted matrix \(U_{j,n}=e(R_j\sqrt n)\). Arithmetic masks are encoded by zero coefficients in \(b\), not by replacing the correlation kernel with an unproved masked kernel.

The ceiling \(W\) must bound this same complex block on the relevant radius window, or otherwise genuinely bound every selected row to which the finite calculation is applied. A proved full-wave ceiling is not automatically such a block ceiling.

## 3. Algebra, localization, and complete cost

### Exact effective level

The finite sharp inequality and the stated ceiling closure give
\[
 (Jv^2)^k\leq B^{k-1}a_k
 \leq B^{k-1}JW^2L^{k-1}.
 \tag{6}
\]
The second inequality follows by diagonalizing the positive semidefinite \(G\):
\(f^*G^{k-1}f\leq L^{k-1}\|f\|^2\leq L^{k-1}JW^2\).
It is valid without full rank.

For \(J>0\), divide (6) by \(J\), take its \((k-1)\)-st root, and divide by \(W^{2/(k-1)}\). The result is exactly
\[
 Jv_{\rm eff}^2\leq BL,\qquad
 v_{\rm eff}^2=v^{2k/(k-1)}W^{-2/(k-1)},
 \qquad
 v_{\rm eff}=v(v/W)^{1/(k-1)}.
 \tag{7}
\]
No factor of \(J,B,W\) is lost. Since \(v\leq W\), one has \(0<v_{\rm eff}\leq v\).

### Local Gram row sums, including the full diagonal

Take a \(\delta\)-separated set of high points inside an interval of length at most \(h\). Its Gram entries are
\[
 G_{j,l}=K_N(R_j-R_l).
 \tag{8}
\]
The diagonal is the full number of ambient integer columns, \(O(N)\); it is not an off-diagonal application of (5).

For a fixed row, each off-diagonal distance is at most \(h\), so the positive-power part of (5) contributes at most \(A\sqrt N\,Jh^\kappa\). Ordering the selected points on either side of that row gives
\[
 \sum_{l\ne j}|R_j-R_l|^{-1}
 \leq C\delta^{-1}\log(2+J).
 \tag{9}
\]
The Hermitian row-sum bound therefore yields
\[
 L\leq C N+
 C A\sqrt N\bigl(Jh^\kappa+\delta^{-1}\log(2+J)\bigr)
 \leq
 C A\left[N+\sqrt N\bigl(Jh^\kappa+
                    \delta^{-1}\log(2+J)\bigr)\right].
 \tag{10}
\]
The last step uses \(A\geq1\), precisely as in accepted204. This verifies the conductor's displayed row-sum bound; its extra \(A\) on the diagonal only enlarges it.

Combining (3), (7), and (10), using \(\delta^{-1}=\sqrt N\), gives
\[
 Jv_{\rm eff}^2
 \leq C A^2Jh^\kappa+
 C A^2\sqrt N\log(2+J).
 \tag{11}
\]
The diagonal remains in the second term even for \(J=1\).

### Absorption and the unallocated certificate

Write \(w=v_{\rm eff}>0\), and choose a fixed sufficiently small \(c>0\) so that
\[
 h=c(w^2/A^2)^{1/\kappa}
 \tag{12}
\]
makes the first term of (11) at most \(Jw^2/2\). Always
\(J\leq1+C_1T/\delta\); consequently, after absorption,
\[
 Jw^2\leq C A^2\sqrt N\,\ell_T,
 \qquad \ell_T=\log(2+T\sqrt N).
 \tag{13}
\]

A maximal \(\delta\)-separated subset covers the local high set by radius-\(\delta\) intervals. No persistence estimate for \(S\) is needed. Thus its measure is at most \(2\delta J\), bounded by
\[
 C A^2\ell_T w^{-2}.
 \tag{14}
\]
Partitioning the whole window into at most \(C(1+T/h)\) such pieces gives the exact unallocated cost
\[
 \boxed{
 D_S(v)\leq
 C A^2\ell_T
 \left(w^{-2}+T A^{2/\kappa}w^{-q}\right).
 }
 \tag{15}
\]
The set being covered is \(\{|S|>v\}\), although its local inequality has the weaker effective level \(w\). Applying (7) to each selected set justifies this use.

The full cover count is essential. Its constant term produces \(w^{-2}\); its \(T/h\) term produces \(TA^{2/\kappa}w^{-q}\). Neither can be discarded.

### Small levels and microscopic or oversized localization

The revised control now explicitly covers the following cases.

If \(w<1\), the trivial measure \(D_S(v)\leq|I|=O(T)\) already proves the eventual displayed certificate, because \(Tw^{-q}\geq T\).

If the formal \(h\) in (12) is below \(\delta\), then \(\delta\leq1\). One may again use \(O(T)\), instead of extracting information from a microscopic cover. In fact the unallocated second term, excluding its harmless logarithm, is
\[
 A^2T A^{2/\kappa}w^{-q}
 =T(A^2/w^2)^{1+1/\kappa}
 =T(c/h)^{\kappa+1}
 \geq c^{\kappa+1}T.
 \tag{16}
\]
The constant on the right is positive and fixed. Thus the trivial measure is absorbed by (15) with a fixed enlarged constant. This argument keeps the powers of \(A\) until the small-power allocation; it does not prematurely assert \(Tw^{-q}\geq T\) when \(w\) may exceed one.

If \(h\) exceeds the length of the full radius window, use that window as one interval. Its actual distances are still at most \(C_1T\), the range of (5), and at most the formal \(h\), so (11)--(14) remain valid. This gives the first term in (15). There is never a fractional number \(T/h<1\) of intervals.

At the boundaries \(h=\delta\) or \(h=|I|\), either adjacent argument applies with fixed constants. A zero-length window or an empty high set has zero measure. No step substitutes a fractional positive count for an integer \(J\).

### Small-power allocation and comparison with the direct bound

In the accepted application \(A\) is bounded by a fixed constant times an arbitrarily small chosen power of \(T\). Since \(N\leq T^{3/2}\), \(\ell_T\ll\log(2+T)\). The largest power of \(A\) in (15) is
\[
 2+2/\kappa=q=136/13.
 \tag{17}
\]
Choosing the input power sufficiently small relative to a requested output \(\epsilon\), and then absorbing the logarithm, proves
\[
 D_S(v)\ll_\epsilon T^\epsilon
        \left(v_{\rm eff}^{-2}+T v_{\rm eff}^{-q}\right).
 \tag{18}
\]
This is the conductor's claimed certificate.

Accepted204 applies directly to the same vector, without the chain ceiling, and supplies
\[
 D_S(v)\ll_\epsilon T^\epsilon(v^{-2}+Tv^{-q}).
 \tag{19}
\]
At the level of the displayed functional costs, the ratios of the two terms in (18) to those in (19) are exactly
\[
 (W/v)^{2/(k-1)},\qquad (W/v)^{q/(k-1)}.
 \tag{20}
\]
Both are at least one. For \(k=2\), (18) is
\[
 T^\epsilon\bigl(W^2v^{-4}+TW^qv^{-2q}\bigr),
 \tag{21}
\]
with the ratios \((W/v)^2\) and \((W/v)^q\), as printed in the control.

The same conclusion survives capping either certificate by the trivial \(O(T)\) measure. Increasing a fixed \(k\) reduces this loss toward the direct level; it creates no improvement over that level. No uniform assertion for an order growing with \(T\) is required.

### Legal block ceilings and actual masks

For the exact block (3), the coefficient \(\ell^1\) bound always gives a legal ceiling:
\[
 \sup_R|S(R)|\leq\sum_{N<n\leq2N}|b_n|
 \leq \sqrt{\#\{N<n\leq2N\}}\;B^{1/2}
 \ll A^{1/2}N^{1/4}.
 \tag{22}
\]
A smaller independently proved ceiling for this same block can replace it, but cannot make \(v_{\rm eff}>v\) on a nonempty high set.

Accepted216 verifies the masked-vector binding explicitly. The large-squarefree-class mask is independent of \(R\). Zeroing inactive coefficients preserves the coefficient energy bound and leaves the ambient unweighted Gram kernel unchanged. No smoothness of this arithmetic mask is assumed. A cosine block's high set is contained in the high set of its associated complex wave, with its fixed phase retained.

The full-wave Li--Yang ceiling in accepted204 is obtained after complete reconstruction. The accepted216 ceiling for the complete large-class wave uses the identity \(Z_Q=B_T-L_Q\). Neither statement alone is a ceiling for an arbitrary individual complex dyadic block. The conductor's warning on this point is correct.

For the complete problem, the singleton, all dyadic blocks through \(T^{3/2}\), and the uniform Schwartz tail are already accounted for by accepted204/216. Since the new closure does not improve any block's direct certificate, combining with the better accepted estimate leaves the existing full-wave bound available. It creates no new complete distribution or moment exponent. The proved full-wave ceiling may still be used at the final moment step, exactly in its accepted scope.

## 4. First unproved step and clarification status

The first missing input for a gain is an estimate of \(f^*G^{k-1}f\) using the prescribed coefficient endpoints and their correlation with the interior Gram chain, before replacing it by \(JW^2L^{k-1}\).

The initial reviewed control hash was
91fddafacef8a8cc0eddec063a49a649347d47caaa60ca7c73cc7860cfb33ead.
I requested explicit endpoint wording rather than treating terse localization as automatically sufficient. The conductor added the paragraph covering \(v_{\rm eff}<1\), \(h<\delta\) with unallocated \(A\)-powers, and \(h\) exceeding the window. I read that added paragraph and verified the new final hash stated in section 1.

That clarification resolves the endpoint presentation. No algebraic or exponent repair remains at the final hash. This is not a claim that the finite closure is the only possible way to estimate anchored chains.

## 5. Exact controls and outcomes

- **Finite equality:** for \(L,W>0\), take \(U=\sqrt L\,I_J\) and \(b=(W/\sqrt L)\mathbf1\). Then \(G=LI_J\), \(f=W\mathbf1\), \(B=JW^2/L\), and \(a_k=JW^2L^{k-1}\). At \(v=W\), both inequalities in (6) are equalities for every fixed \(k\). This is an enlarged finite algebra control, not an arithmetic block.
- **Empty and zero cases:** \(J=0\) is immediate. If \(B=0\), \(W=0\), or \(L=0\), no nonempty positive high set is possible under the respective hypotheses. If \(v>W\), the high set is empty.
- **Singular matrices:** the closure uses nonnegative powers of a PSD matrix only; it never requires an inverse.
- **Full diagonal and \(J=1\):** the \(N\) term in (10) remains. It is responsible for a valid local bound even with a single selected point.
- **Levels below one:** handled by the trivial measure before any localization assertion.
- **Microscopic \(h\):** the exact \(A\)-dependent second term dominates a fixed multiple of \(T\), as in (16).
- **Oversized \(h\):** one whole-window interval is used and the first distribution term remains.
- **Arithmetic masks:** implemented in the fixed vector by zeros, with the accepted coefficient-energy and tail bounds. No weighted correlation theorem is imported.
- **Ceiling scope:** the block \(\ell^1\) norm is legal; a complete-wave ceiling is not silently assigned to a block.
- **Both-term comparison:** (20) verifies loss, or equality when \(W=v\), separately in each term. It is a comparison of upper certificates, not a lower bound on actual level sets.

All checks were analytical. No experiment or numerical evaluation was performed. Authorship of the frozen finite input is disclosed and is not presented as an independent validation of that input.

## 6. Exact files, hashes, and provenance

Only the following authorized files were read:

1. protocol.md — SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
2. rounds/codex-managed/gc-actual-vector-gram-correlations/reports/blind_anchored_gram.md — SHA256 c79eb543c4dd1229e8e6b9c6550f9b6df0fb10bed0ed76f386bf08c79d7d2ebd.
3. rounds/codex-managed/gc-actual-vector-gram-correlations/controls/conductor_chain_ceiling_cost.md — final SHA256 de4aca2122c9f452e03a3456bfe40b80af4fbe5d9da47b3e04ccf3c747e2ed11; the superseded initial hash is recorded in section 4.
4. proofs/kernels/gc_complete_square_root_large_values_moment_bound.md — SHA256 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212.
5. proofs/kernels/gc_complete_distinct_radical_moment_reduction.md — SHA256 d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee.

All listed file hashes were independently obtained from the files; the revised final control hash was independently obtained after reading its added paragraph. The finite report is my own frozen statement-only derivation. This audit is a separate NONBLIND application review of the conductor's closure, not a fresh statement-only task and not an independent review of my own report.

Retained round217--220 and current round221 history is disclosed. No other current attack report, graph, manifest, source, strategy, or artifact merely cited by these files was opened. In particular, the cited closed209 barrier was not read or needed for this proof. No original report, control, shared state, or successor artifact was edited; only this assigned review was written.

## 7. Recommended state effect

**Close the final-hash application seam GREEN and retain the control as a scoped quantitative limitation of the stated endpoint-ceiling closure.**

The complete accepted bounds remain available and unchanged. No full-target, moment, pointwise-exponent, or complete distinct-integral improvement follows. The control does not reject genuine signed fixed-vector chain estimates.

No graph mutation, synthesis, successor design, or additional work is undertaken. This review ends here.
