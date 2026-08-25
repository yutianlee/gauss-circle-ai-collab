# 1. Result

The terminal hostile review is **GREEN**.  The conductor candidate's estimate
\[
 \mathcal Z_U(V)\ll_{\varepsilon,A}M^{-1/4}X^\varepsilon
\]
is valid for the complete literal zero row and the full range
\(J_A<V\leq K\).  In particular, (156.CT10)--(156.CT11) survive a
component-by-component endpoint audit.  Their correct interpretation is
that every transition belonging to the real profile is charged to the
zero-extended total variation of \(w_U\); one does not charge an unstated
\(O(1)\) number of profile components.  The only additional
\(j\)-dependent hard cutoff is the nearest-integer cell, which has one
cutoff on each signed block.

The induced-character calculation is also exact for arbitrary \(N\),
including even squarefree kernels, repeated prime powers, \(p=2\), and the
conductor-one case.  It selects subsequences \(h\mid j\), but passing to
such a subsequence cannot increase the variation norm.  The final
\(d\)-sum and the exterior normalization give exactly the claimed
\(M^{-1/4}\) saving.  The external \(B_{1,U}(1)\) is correctly absent from
the frozen row; its later reinsertion is harmless because the Round-154
adjudication bounds it by \(X^\varepsilon\).

# 2. Exact statement and hypotheses

The hostile check uses the following data, all stated in the candidate,
barrier packet, or cited Round-154 adjudication.

1. The inherited \(w_U\) is the literal zero-extended **real**
   off-congruence profile and satisfies
   \[
   \|w_U\|_\infty+\operatorname {Var}w_U
   \ll_\varepsilon M^{-3/4}X^\varepsilon.
   \]
   The variation therefore includes transitions between all support
   components and zero, as well as half-open endpoint values.
2. The physical \(x\)-support lies at \(x\asymp K\), has total span
   \(O(K)\), and in Round 154 also satisfies \(2x<N\) for sufficiently
   large \(X\).  Hence it supplies \(O(K)\) physical integers in one
   residue system modulo \(q=4N\), with no wrapping or multiplicity.
3. The exact cell is
   \[
   -x\leq j\leq x-1.
   \]
   For the integer set
   \[
   \mathcal J_V=\{\lfloor V\rfloor+1,\ldots,\lfloor2V\rfloor\},
   \]
   the positive block is \(j=k\), \(k\in\mathcal J_V\), and the negative
   block is \(j=-k\), \(k\in\mathcal J_V\).  This records the strict lower
   boundary and closed upper boundary exactly.
4. For each odd \(d\mid N\), the arithmetic modulus is
   \[
   c=\frac{4N}{d}=4m,\qquad m=\frac Nd,
   \]
   with no assumption that \(m\) is odd or squarefree.
5. The frozen quantity does not contain \(B_{1,U}(1)\).  Round 154 states
   separately that this external factor is
   \(O_\varepsilon(X^\varepsilon)\).

No smoothness beyond bounded variation, no bounded component count, and
no primitive- or odd-modulus shortcut is used in the verdict.

# 3. Proof or derivation

**Literal off-congruence profile and every jump.**  Fix a physical
integer \(x\).  On either signed block the map
\[
 k\longmapsto \frac{x^2-\sigma k}{N},\qquad \sigma\in\{1,-1\},
\]
is monotone.  Therefore the variation of the sampled, zero-extended
profile is bounded by the variation of the full real profile:
\[
 \sum_k\left|
 w_U\!\left(\frac{x^2-\sigma(k+1)}N\right)
 -w_U\!\left(\frac{x^2-\sigma k}N\right)\right|
 \leq \operatorname {Var}w_U.
 \tag{R156.1}
\]
This inequality is valid for any number of support components.  A jump
into or out of a component, a transition value, and a half-open choice
are all individual increments on the left and are already included on
the right.  Consequently the candidate does not need an \(O(1)\)
component-count assertion.

The cell cutoff is equally literal.  On the positive block it becomes
\[
 -x\leq k\leq x-1\quad\Longleftrightarrow\quad k\leq x-1,
\]
whereas on the negative block it becomes
\[
 -x\leq-k\leq x-1\quad\Longleftrightarrow\quad k\leq x.
\]
Thus the asymmetric endpoint is \(k=x-1\) for \(j>0\) and \(k=x\) for
\(j<0\).  Each block has at most one cell jump.  The strict dyadic mask is
external to \(B_j(x)\); its exact endpoints are the endpoints of
\(\mathcal J_V\), and discrete Abel summation charges the terminal weight
through the supremum term.  If one instead extends the block weight by
zero, the two block-boundary jumps cost only two further copies of the
same supremum.

The phase identity is exact:
\[
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x.
\]
On every continuous piece,
\[
 \frac{\partial}{\partial j}\bigl(\sqrt{x^2-j}-x\bigr)
 =-\frac1{2\sqrt{x^2-j}}.
 \tag{R156.2}
\]
The cell gives \(j\leq x-1\), while \(x\asymp K\) and \(K\to\infty\);
hence
\[
 x^2-j\geq x^2-x+1\asymp K^2.
\]
For negative \(j\) the radicand is still larger.  Thus the exponential
phase has variation
\[
 O\!\left(\frac VK\right)=O(1)
\]
on either block, since \(V\leq K\).  Multiplication by the profile and
the literal cell indicator now yields
\[
 \sup_k|B_{\sigma k}(x)|
 +\sum_k|B_{\sigma(k+1)}(x)-B_{\sigma k}(x)|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
 \tag{R156.3}
\]

The Round-154 support statement puts every physical \(x\) in an interval
of \(O(K)\) integer length (indeed with \(2x<N<q\)).  Summing (R156.3)
over those \(x\), without multiplying by the number of profile
components, gives
\[
 \mathcal A\ll_\varepsilon
 K M^{-3/4}X^\varepsilon.
 \tag{R156.4}
\]
This proves the content of (156.CT10)--(156.CT11), including positive and
negative cell endpoints, strict block endpoints, and zero-extension
jumps.

**Subsequence variation under \(h\mid j\).**  The exact induced-modulus
formula restricts a term to \(j=hn\).  For consecutive admissible \(n\),
the triangle inequality gives
\[
 |A_{h(n+1)}-A_{hn}|
 \leq\sum_{r=hn}^{h(n+1)-1}|A_{r+1}-A_r|.
\]
These intervening intervals are disjoint as \(n\) varies.  Hence
\[
 \sup_n|A_{hn}|+\operatorname {Var}_n(A_{hn})
 \leq \sup_j|A_j|+\operatorname {Var}_j(A_j)
 \leq\mathcal A.
 \tag{R156.5}
\]
The same argument applies after reversing the negative block.  The first
and last multiples of \(h\) are handled by the supremum in (R156.5).
There is no factor \(h\), no component-count factor, and no endpoint loss.
This validates the precise BV input in (156.CT19).

**Hostile check of the character formula.**  Write \(m=u^2s_0\), where
\(s_0\) is squarefree and may be even.  For every unit \(a\bmod4m\),
\[
 \epsilon_a=\frac{1+i}{2}+\frac{1-i}{2}\chi_4(a),
 \qquad
 \left(\frac{4m}{a}\right)=\left(\frac{s_0}{a}\right).
\]
The candidate's discriminants are the fundamental discriminants attached
to \(s_0\) and \(-s_0\):
\[
\begin{array}{c|c|c}
s_0\bmod4&\Delta_+&\Delta_-\\ \hline
1&s_0&-4s_0\\
3&4s_0&-s_0\\
2&4s_0&-4s_0.
\end{array}
\]
They divide \(4m\), including the \(s_0\equiv2\pmod4\) case, where their
two-adic conductor is \(8\).  The only conductor-one constituent is
\(s_0=1\), equivalently \(m\) is a square (and then \(c=4m\) is a square).

For a primitive constituent of conductor \(f\mid c\), put \(L=c/f\).
Inclusion-exclusion over the extra primes gives exactly
\[
 G_{c,\chi}(n)=\tau(\chi)
 \sum_{\substack{r\mid R_f\\L/r\mid n}}
 \mu(r)\chi(r)\frac Lr\,
 \overline\chi\!\left(\frac{n}{L/r}\right),
 \qquad
 R_f=\prod_{\substack{p\mid c\\p\nmid f}}p.
 \tag{R156.6}
\]
At \(p\mid f\), the divisibility in (R156.6), followed by the zero of the
primitive character on nonunits, forces
\[
 v_p(n)=v_p(c)-v_p(f).
\]
At \(p\nmid f\), the two Ramanujan alternatives force
\[
 v_p(n)\geq v_p(c)-1.
\]
These statements include \(p=2\) and all repeated prime powers.  For
\(f=1\), (R156.6) is the exact Ramanujan sum.  Thus the character formula
does not shift either signed \(j\)-endpoint; it merely chooses the exact
subsequence already covered by (R156.5).

For \(f>1\), the character is primitive and nonprincipal, so
Pólya--Vinogradov applies on each resulting consecutive \(n\)-interval.
Together with (R156.5), it proves (156.CT19)--(156.CT20).  Independently,
the blind derivation gives the elementary check
\[
 \sup_{I\subset\mathbb Z\ {\rm consecutive}}
 \left|\sum_{j\in I}K(0,-j;c)\right|
 \ll c\log(2c),
 \tag{R156.7}
\]
directly by opening the complete additive transform and bounding its
geometric sums.  Abel summation with (R156.4) therefore proves
(156.CT22) even without importing Pólya--Vinogradov.  The principal
partial-sum bound (156.CT21) is also exact, because the linear term in
\(\sum_{j\leq Y}c_c(j)\) cancels for \(c>1\).

**External factor and complete power normalization.**  The external
\(B_{1,U}(1)\) is not a function of \(j\) and is not part of the frozen
quantity (156.CT2).  Round 154 records
\[
 B_{1,U}(1)\ll_\varepsilon X^\varepsilon.
\]
When the scalar is reassembled, multiplying the present estimate by this
factor only changes \(X^\varepsilon\) to \(X^{2\varepsilon}\), which is
absorbed by relabelling epsilon.  It creates no \(N\), \(M\), \(V\), or
\(d\) power.

Finally, with \(q=4N\), \(c=q/d\), and (156.CT22),
\[
\begin{aligned}
 |\mathcal Z_U(V)|
 &\ll_\varepsilon
 \frac{\mathcal A}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\sqrt c\,c\,X^\varepsilon\\
 &=\frac{\mathcal A}{N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}\sqrt c\,X^\varepsilon\\
 &=\frac{2\mathcal A}{\sqrt N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}d^{-1/2}X^\varepsilon\\
 &\ll_\varepsilon
 \frac{\mathcal A}{\sqrt N}X^\varepsilon
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{R156.8}
\]
Both signs have already been included in the bound defining
\(\mathcal A\), \(|\chi_4(d)|=1\), and the omitted numerical constant
\(|-i(1+i)/2|\) is absolute.  Equation (R156.8) confirms every exterior
factor and the final \(N\)--\(M\)--\(V\)--\(d\) ledger.

# 4. First doubtful or unproved step

No defect remains in the zero-mode candidate.  The most audit-sensitive
wording is the sentence before (156.CT10) saying that “cell and support
indicators” create \(O(1)\) jumps.  It is valid only with the division
made explicit above: the hard cell contributes \(O(1)\) jumps, fixed
\(x\)-support contributes none as \(j\) varies, and every profile-component
or zero-extension jump is charged to \(\operatorname {Var}w_U\).  This is
exactly what (156.CT5), the Round-154 zero-extended real profile, and the
first sentence of Section 3.1 provide, so the wording is not a mathematical
gap.

After promotion of the zero row, the first genuinely unproved object is
still the nonzero-\(v\) matrix (156.CT24).  Nothing in the BV argument
controls its coupled coefficient \(\widehat B_j(2dv)\).

# 5. Required control test and outcome

| Control | Hostile outcome |
|---|---|
| literal off-congruence profile | PASS. Round 154 supplies the real zero-extended BV profile used in (R156.1). |
| component count | PASS. No bounded number of components is needed; total profile variation and total \(x\)-span suffice. |
| physical \(x\)-support | PASS. The inherited \(O(K)\) span and \(2x<N<q\) give \(O(K)\) physical representatives with no wrap. |
| exact phase derivative | PASS. The derivative is \(-1/(2\sqrt{x^2-j})\), and the literal cell makes it \(O(K^{-1})\). |
| cell, transition, half-open, and zero-extension jumps | PASS. Profile jumps are in \(\operatorname {Var}w_U\); the cell has the two asymmetric signed cutoffs stated above. |
| positive and negative strict endpoints | PASS. Both are parametrized by the same exact integer set \(\mathcal J_V\); Abel's endpoint term is controlled by the supremum. |
| BV after \(h\mid j\) | PASS. Equation (R156.5) proves contraction of variation under ordered subsequences. |
| external \(B_{1,U}(1)\) | PASS. It remains outside the frozen row and costs only \(X^\varepsilon\) on later reinsertion. |
| character conductors and \(p=2\) | PASS. The even squarefree-kernel row has conductor \(8\), and (R156.6) retains every local valuation. |
| conductor-one/square case | PASS. It is the exact Ramanujan branch, not a primitive square-root estimate. |
| final \(d\)-sum and normalization | PASS. Equation (R156.8) uses \(dc=q\) and yields exactly \(M^{-1/4}\). |
| signed versus unsigned control | PASS. The proof uses signed character/additive partial sums and does not promote the unsigned capacity. |

No numerical experiment or numerical certification was used.

# 6. Dependencies and exact artifacts used

This terminal review read and used exactly:

- protocol.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_target.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/blind_zero_mode_character_rederivation.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/barrier_packet.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md.

The frozen normalized row was taken from the barrier packet.  No graph,
proof draft, synthesis, validation matrix, campaign state, sibling report,
or web source was read or changed.

# 7. Recommended state effect

Promote (156.CT3), the literal profile variation
(156.CT10)--(156.CT11), the exact character and induced-modulus identities,
and the weighted transform bound through (156.CT23) for the frozen zero
row.  Retain (156.CT24) and all downstream owners as open.  When the
larger scalar is reassembled, restore the external \(B_{1,U}(1)\) once,
using its accepted \(X^\varepsilon\) bound.

**Verdict: GREEN.  First defect: none.**
