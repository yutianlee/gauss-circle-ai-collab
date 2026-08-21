# Blind global signed implication

## 1. Result

Put
\[
T=L^2X^\varepsilon,\qquad
S=E_{\mathrm{safe},L},\qquad
O=\sum_{B\in\mathcal B_L}\sum_{\nu\in\mathcal O_B}O_{B,\nu},
\qquad C=C_L^{\mathrm{comp}}=\sum_{B\in\mathcal B_L}Q_B^{\mathrm{comp}}.
\]
The two displayed identities give the exact scalar reduction
\[
E_L=S+2\Re(C-O),
\qquad
\bigl|E_L-2\Re C\bigr|\le (C_s+2C_o)T,
\tag{1}
\]
where \(C_s\) and \(C_o\) are the constants in the safe and omitted-term bounds (they may both be replaced by the displayed constant \(C\)). Consequently, for the usual upper bound on a nonnegative energy, the weakest needed estimate is the one-sided scalar estimate
\[
\Re C_L^{\mathrm{comp}}\le K T.
\tag{2}
\]
It is sufficient and, modulo the already allowed \(O(T)\) terms, necessary. If no nonnegativity is assumed and the intended target is the two-sided assertion \(|E_L|=O(T)\), the exact counterpart is
\[
|\Re C_L^{\mathrm{comp}}|=O(T).
\tag{3}
\]
Neither \(|C_L^{\mathrm{comp}}|\), nor \(\sum_B|Q_B^{\mathrm{comp}}|\), nor any row-energy or full Gram norm is required by (B110.1)--(B110.2).

## 2. Exact statement and hypotheses

Assume only that all displayed index sets are finite, that (B110.1)--(B110.2) hold with the indicated single representative orientation and single outer \(2\Re\), and that the two error constants are uniform in the parameters over which an \(O(T)\) assertion is wanted. Then the following quantitative equivalences hold:

- If \(E_L\le K_E T\), then
  \[
  \Re C\le \left(\frac{K_E+C_s}{2}+C_o\right)T.
  \]
  Conversely, if \(\Re C\le K_C T\), then
  \[
  E_L\le (C_s+2K_C+2C_o)T.
  \]
- If \(|E_L|\le K_E T\), then \(|\Re C|\le (K_E/2+C_s/2+C_o)T\); conversely, \(|\Re C|\le K_C T\) implies \(|E_L|\le(C_s+2K_C+2C_o)T\).
- If \(E_L\ge0\) is part of the meaning of “energy,” its upper target bound also forces \(\Re C\ge-(C_s/2+C_o)T\). Thus \(|\Re C|=O(T)\) follows, but its lower half is supplied for free by positivity and (1), not by a separate completed-sum estimate.

The finite block index can be exchanged or removed algebraically under the following exact conditions. Write, if desired,
\(Q_B^{\mathrm{comp}}=\sum_{\alpha\in I_B}q_{B,\alpha}\). Reordering the sums needs only finiteness. A reindexing through
\(\phi:\bigsqcup_B I_B\to I\) preserves the sum precisely when the merged coefficient is defined by the whole fibre,
\[
\widetilde q_\gamma=
\sum_{(B,\alpha)\in\phi^{-1}(\gamma)}q_{B,\alpha}.
\tag{4}
\]
If the intended merged expression keeps one copy of each underlying term instead, \(\phi\) must be bijective after all prescribed multiplicities and one-count conventions are included. Zero extension is harmless only when the added entries are exactly zero. Block-dependent weights, orientations, truncations, and multiplicities must remain attached to their terms. In particular, merging both conjugate orientations into a sum that still has the outer \(2\Re\) double-counts unless the normalization is changed. The omitted terms may be merged because the packet already supplies the global \(\ell^1\) bound; separate per-block \(O(T)\) bounds would not suffice unless their constants sum to \(O(1)\). No convergence hypothesis is needed here; for infinite replacements, an appropriate absolute-convergence or Fubini/Tonelli hypothesis would be additional.

## 3. Proof, norm separation, and finite countermodels

Summing (B110.2) over \(B\) gives
\(\sum_BQ_B^{\mathrm{res}}=C-O\). Substitution in (B110.1) proves (1), because \(|O|\le\sum_{B,\nu}|O_{B,\nu}|\le C_oT\). Solving (1) for \(\Re C\), or applying it in the other direction, proves every equivalence in Section 2.

The scalar controls form the one-way chain
\[
\Re C\le |\Re C|\le |C|\le\sum_B|Q_B^{\mathrm{comp}}|.
\tag{5}
\]
Thus global modulus and blockwise absolute bounds are sufficient, but are progressively stronger than the required one-sided real-part bound. A bound on every block separately is useful only after its constants are summed; it is not a global target-sized bound merely because each block is target-sized.

Rows are not present in the packet. Under an additional representation
\(C=\sum_{r\in\mathcal R}w_rq_r\), define the row \(\ell^2\) energy
\(R_2=(\sum_r|q_r|^2)^{1/2}\). Then
\[
|C|\le \|w\|_2R_2.
\tag{6}
\]
Accordingly, \(R_2=O(T)\) is a target-sized sufficient condition only with \(\|w\|_2=O(1)\) (or with the correspondingly rescaled target), and it is not necessary because rows may cancel. Likewise, under an additional Gram representation \(C=w^*Gw\),
\[
|C|\le \|G\|_{\mathrm{op}}\|w\|_2^2.
\tag{7}
\]
A full Gram-norm estimate is sufficient only together with normalization of the tested direction, and is not necessary because (1) tests just that direction and only its real part. Even for a positive semidefinite Gram matrix, a large eigenvalue orthogonal to \(w\) is invisible. Combining block Gramians as one full Gramian is exact without new cross terms only for a direct-sum/block-diagonal construction (or when all cross terms are included and justified explicitly).

Here are exact finite countermodels. Set \(T=1\), take \(S=O=0\), and always define \(E_L=2\Re C\); hence both displayed identities hold.

- One-sided real part does not imply a two-sided real-part bound for a merely real, not assumed nonnegative, \(E_L\): one block with \(Q=-M\) has \(E_L=-2M\le1\) but \(|\Re C|=M\). This countermodel is excluded if \(E_L\ge0\) is a hypothesis, exactly as Section 2 records.
- Real-part control does not imply modulus control: one block with \(Q=iM\) has \(E_L=0\) and \(|C|=M\).
- Global modulus does not imply blockwise absolute control: two blocks with \(Q_1=M\), \(Q_2=-M\) have \(C=E_L=0\) but \(\sum_B|Q_B|=2M\). The same example shows that no bound on an individual block follows from the global scalar bound.
- A target bound for each block does not imply a target bound after merging: with \(N\) blocks and \(Q_B=1\), every \(|Q_B|\le1\), while \(C=N\) and \(E_L=2N\).
- Blockwise scalar control does not imply internal row energy: in one block let \(q_1=M,q_2=-M\), with \(Q=q_1+q_2=0\). Then \(E_L=0\) but \(R_2=\sqrt2M\). Conversely, row energy at unit scale does not control an unnormalised row sum: for an integer \(M\), take \(M^2\) rows with \(q_r=1/M\) and \(w_r=1\). Then \(R_2=1\), but \(C=M\) and \(E_L=2M\).
- A directional scalar bound does not imply a full Gram bound: take \(G=\operatorname{diag}(1,M)\), \(w=(1,0)^t\). Then \(G\) is a Gram matrix, \(C=w^*Gw=1\), and \(E_L=2\), while \(\|G\|_{\mathrm{op}}=M\). Conversely, a Gram-norm bound without direction normalization is insufficient: \(G=[1]\), \(w=[\sqrt M]\) gives \(\|G\|_{\mathrm{op}}=1\) but \(C=M\).

All parameters \(M,N\) are finite but arbitrarily large, so these are finite logical countermodels rather than convergence examples.

## 4. First doubtful or unproved step

There is no unproved step in the scalar reduction (1): it is finite algebra plus the stated triangle inequality. The first unsupported step in any stronger conclusion would be introducing “rows” or a “Gram matrix” and assuming that its norm is controlled, or that its tested vector has bounded norm. Neither such representation nor normalization occurs in the statement-only packet. The other possible ambiguity is semantic: “real energy” may or may not explicitly assert \(E_L\ge0\), and \(E_L\ll T\) may be read as an upper energy estimate or as \(|E_L|=O(T)\). Sections 1--2 give the exact conclusion in each reading, so no positivity assumption is silently used.

## 5. Required control tests and outcomes

- **Real-vs-complex-pairing.** Input: the singleton model \(Q=iM\), with real safe and final energy zero. Expected invariant: the displayed outer \(2\Re\) annihilates the imaginary direction. Observed result: \(E_L=0\) while \(|C|=M\). Implication: replacing real-part control by complex modulus is invalid without an extra theorem.
- **Signed-vs-unsigned and coefficient-adversary.** Input: two labelled blocks \(M,-M\). Expected failure: taking absolute values destroys inter-block cancellation. Observed result: the signed merged scalar is zero, whereas its blockwise absolute mass is \(2M\); adversarial equal phases would instead give scalar \(2M\). Implication: the algebra requires the actual complex coefficients and signs and does not justify an unsigned upgrade.
- **Support-and-degeneracy / one-count merging.** Input: two labelled occurrences of the value \(1\) mapped to one unlabelled index. Expected invariant: a multiplicity-preserving fibre sum remains \(2\); an illicit set-union deduplication becomes \(1\). Observed result: formula (4) preserves \(2\), while deleting the duplicate changes the exact identity. Implication: a block index may be hidden only after its multiplicities, zero extensions, and representative orientation are preserved.
- **Dimension normalization.** Input: the \(M^2\)-row and one-dimensional Gram models in Section 3. Expected failure: a bare row or operator norm omits the norm of the contraction vector. Observed result: the proposed norm stays \(1\) while the scalar is \(M\). Implication: any row-energy or Gram route must state the cardinality/weight normalization that makes (6) or (7) target-sized.

These controls are exact symbolic finite tests; no numerical experiment is being used as proof.

## 6. Dependencies and exact artifacts used

The derivation uses only `problems/gauss_circle.md`, `state/control_models.md`, and `rounds/codex-managed/m9-m2-global-signed-completed-directional/blind_statement.md`, as required by the blind brief. The proof itself depends only on (B110.1), (B110.2), finiteness, the two stated target-sized error bounds, and (for the optional energy reading) an explicitly added hypothesis \(E_L\ge0\). No graph, strategy, candidate formula, earlier round, or sibling report was consulted.

## 7. Recommended state effect

**Promote** the finite scalar interface
\[
E_L=2\Re C_L^{\mathrm{comp}}+O(L^2X^\varepsilon)
\]
together with its one-sided/two-sided distinction and the multiplicity-preserving merge hypotheses. **Reject** as logically necessary any upgrade to global modulus, blockwise absolute mass, row energy, or full Gram norm. A later application may retain any of those stronger estimates as a chosen sufficient method, but only with its missing normalization and reindexing hypotheses stated explicitly. This report recommends no direct shared-state edit.
