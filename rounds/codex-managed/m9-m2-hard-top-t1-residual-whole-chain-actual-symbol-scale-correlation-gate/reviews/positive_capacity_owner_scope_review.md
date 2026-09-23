# Round 175 review: positive-capacity and owner scope

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Reviewed candidate: candidates/formalized_whole_chain_scale_telescope_obstruction.md
- Reviewer role: hostile positive-capacity and owner-scope seam
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

### Verdict: revise two formula seams, then promote only the obstruction

The candidate's central endpoint-collapse result is correct. After complete
signed recombination of all odd character frequencies and all nonzero
ordinary frequencies,

\[
 \mathcal N_{R,S}=Q_S^*-Q_R^*,\qquad
 \sum_{j<K}\mathcal N_{R_j,R_{j+1}}
 =Q_M^*-Q_{R_0}^*.
\tag{175.R1}
\]

The decisive positive-energy seam also passes, but the candidate does not
state its strongest consequence. From (175.C16), Fejer positivity, and
\(R_0=\lceil L\rceil\),

\[
 \boxed{
 0\le Q_{R_0}^*
 \le {R_0\over2}\sum_{\epsilon=0}^1
       \|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{175.R2}
\]

Therefore, for the deliberately one-sided inequality,

\[
 \boxed{
 Q_M^*-Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon
 \quad\Longleftrightarrow\quad
 Q_M^*\ll_\varepsilon L^3X^\varepsilon.}
\tag{175.R3}
\]

The forward implication uses (175.R2); the reverse implication uses
\(Q_{R_0}^*\ge0\). Thus the lower endpoint cannot cancel a maximal
\(L^4\) contribution: the whole-chain target is exactly a literal
factor-\(L\) maximal Fejer-energy theorem at \(R=M\), modulo a
target-safe lower endpoint.

Two repairs are required before the candidate is mechanically durable:

1. Equation (175.C8) is missing a plus sign before its interior sum. As
   printed, it is false or syntactically ambiguous. It must read

   \[
   \sum_{j=0}^{K-1}a_j\mathcal N_{R_j,R_{j+1}}
   =a_{K-1}Q_M^*-a_0Q_{R_0}^*
    +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*.
   \tag{175.R4}
   \]

2. Immediately after (175.C17), insert (175.R2)--(175.R3) and replace the
   suggestion that an unspecified endpoint comparison might save the
   target by the precise statement that the lower endpoint is already
   \(O(L^3X^\varepsilon)\); all missing power is at \(Q_M^*\).

The physical \(L^4\) diagnostic (175.C18)--(175.C20) is algebraically
correct, including its constants. It is only a nonliteral
coefficient-uniform capacity model, not a lower bound for \(Q_M^*\) on the
literal transform or for K26. With that quarantine, a durable
route-scoped obstruction node is justified after the two repairs. It has
no implication edge and changes no target or parent status.

## 2. Exact statement and hypotheses

Retain the candidate's full hypotheses:

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M\asymp L^2,
\]

the literal zero-extended coefficient \(c_N^{\rm rem}\), the energy

\[
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon,
\]

both absolute-parity branches, the exact character factor \(i/2\), all odd
character frequencies, and the exact ordinary split

\[
 Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}.
\]

The complete collective zero-mode estimate is

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta {L^2\over J}X^\eta,
\tag{175.R5}
\]

and Parseval gives \(\|Z_\epsilon\|_2^2=D_L\). Define

\[
 Q_R^*={1\over2}\sum_{\epsilon=0}^1
 \int_0^1F_R(\theta)|Z_{\epsilon,*}(\theta)|^2\,d\theta.
\tag{175.R6}
\]

Since \(0\le F_R(\theta)\le R\), every \(Q_R^*\) is nonnegative. The
stopped chain is the minimal chain

\[
 R_{j+1}=\min(2R_j,M),\qquad R_K=M,
\]

including the actual strict final link when \(M<2R_{K-1}\). The
ordinary-zero-containing sector is restored only after full
odd-character recombination, and the short correction is paid exactly
once.

The review claim is:

> The candidate proves an exact scale-telescope obstruction after the
> repairs (175.R2)--(175.R4). It does not prove the required literal
> maximal energy \(Q_M^*\ll L^3X^\varepsilon\).

## 3. Proof or derivation

### 3.1 Decisive lower-endpoint energy bound

From \(Z_{\epsilon,*}=Z_\epsilon-Z_{\epsilon,0}\),

\[
\begin{aligned}
 \sum_{\epsilon=0}^1\|Z_{\epsilon,*}\|_2^2
 &\le
 2\sum_{\epsilon=0}^1\|Z_\epsilon\|_2^2
 +2\sum_{\epsilon=0}^1\|Z_{\epsilon,0}\|_2^2\\
 &\le 4D_L+
 O\left({L^4\over J^2}X^{2\eta}\right)
 \ll_\varepsilon L^2X^\varepsilon,
\end{aligned}
\tag{175.R7}
\]

because \(J\ge L^2\), with \(\eta\) rebudgeted into \(\varepsilon\).
Applying \(F_{R_0}\le R_0\) to (175.R6) proves (175.R2).

Let

\[
 S_*:=\sum_{j<K}\mathcal N_{R_j,R_{j+1}}
 =Q_M^*-Q_{R_0}^*.
\]

If \(S_*\ll L^3X^\varepsilon\), then

\[
 Q_M^*=S_*+Q_{R_0}^*\ll L^3X^\varepsilon.
\]

Conversely, if \(Q_M^*\ll L^3X^\varepsilon\), then

\[
 S_*=Q_M^*-Q_{R_0}^*\le Q_M^*
 \ll L^3X^\varepsilon.
\]

This proves (175.R3). It is essential that the target is one-sided and
that \(Q_{R_0}^*\ge0\). No absolute bound for \(S_*\) is being inserted.

### 3.2 Ordinary-zero restoration and K26 equivalence

The sector containing at least one ordinary zero frequency is, exactly,

\[
 \mathcal Z_{R_0,M}
 ={1\over2}\sum_{\epsilon=0}^1\int_0^1
 (F_M-F_{R_0})
 \left(2\Re(Z_\epsilon\overline{Z_{\epsilon,0}})
       -|Z_{\epsilon,0}|^2\right)\,d\theta.
\tag{175.R8}
\]

This is the same as
\(|Z_{\epsilon,0}|^2+
2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})\), so the sector is counted
once. Using
\(|F_M-F_{R_0}|\le M+R_0\), (175.R5), and Parseval,

\[
\begin{aligned}
 |\mathcal Z_{R_0,M}|
 &\ll M\left(
 D_L^{1/2}{L^2\over J}
 +{L^4\over J^2}\right)X^{O(\eta)}\\
 &\ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
\tag{175.R9}
\]

Thus (175.C13) is valid at the single endpoint, with no termwise-\(k\)
claim. Together with the once-only short correction,

\[
 S_*=2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M}.
\tag{175.R10}
\]

Hence the one-sided chain target, the one-sided K26 target, and
\(Q_M^*\ll L^3X^\varepsilon\) are equivalent at target strength. None is
proved.

### 3.3 Weighted scale Abel identity

Put \(Q_j=Q_{R_j}^*\). Finite reindexing gives

\[
\begin{aligned}
 \sum_{j=0}^{K-1}a_j(Q_{j+1}-Q_j)
 &=\sum_{j=1}^{K}a_{j-1}Q_j
   -\sum_{j=0}^{K-1}a_jQ_j\\
 &=a_{K-1}Q_K-a_0Q_0
   +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_j.
\end{aligned}
\tag{175.R11}
\]

This proves the corrected (175.R4). For \(a_j\equiv1\), every interior
coefficient is exactly zero. A nonconstant weight changes the target.
Closing (175.R4) by \(Q_R^*\ll RL^2X^\varepsilon\) gives

\[
 \left|\sum_ja_j\mathcal N_j\right|
 \ll_\varepsilon L^2X^\varepsilon
 \left(
 |a_{K-1}|M+|a_0|R_0+
 \sum_{j=1}^{K-1}|a_{j-1}-a_j|R_j\right).
\tag{175.R12}
\]

The constant target weights retain the top term \(ML^2\asymp L^4\).
Therefore weighted scale Abel creates no factor-\(L\) resource.

### 3.4 Exact physical \(L^4\) diagnostic

The constants in (175.C18)--(175.C19) are correct. Let \(L=2n\),
\(P=n^2\), \(M=4P=L^2\), and support \(z_N=1\) on the \(2P\) even sites
of an \(M\)-site interval. Then

\[
 D=2P,\qquad A_{2s}=2P-s\quad(1\le s<2P).
\]

At \(R=M=4P\),

\[
\begin{aligned}
 \mathfrak E_M^{(2)}
 &=2P+2\sum_{s=1}^{2P-1}
 \left(1-{s\over2P}\right)(2P-s)\\
 &=2P+{1\over P}\sum_{t=1}^{2P-1}t^2
 ={8P^2+1\over3}.
\end{aligned}
\tag{175.R13}
\]

Since \(R_0=L=2n\) and \(D=2n^2\),

\[
 \mathfrak E_{R_0}^{(2)}\le R_0D=4n^3.
\]

For \(n\ge3\),

\[
\begin{aligned}
 \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 &\ge {8n^4+1\over3}-4n^3\\
 &\ge {4n^4\over3}={L^4\over12}.
\end{aligned}
\tag{175.R14}
\]

The last inequality differs from equality by
\((4n^3(n-3)+1)/3\ge0\). Taking \(X=L^8\) and, explicitly,
\(H=L^2\), the parameter range is admissible. For
\(0<\varepsilon_0<1/8\),

\[
 {\mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
  \over L^3X^{\varepsilon_0}}
 \ge {1\over12}L^{1-8\varepsilon_0}\longrightarrow\infty.
\tag{175.R15}
\]

This validates the exact \(L^4\) physical capacity, including the constant
\(1/12\). It is a phase-dechirped, nonliteral diagnostic. It does not show
that the literal \(Q_M^*\), the literal physical endpoint, or K26 has
large mass.

If the candidate wants to call the bound in (175.C17) sharp specifically
as an abstract positive-operator inequality for \(Q_R^*\), it should add
the separate control

\[
 Z_{0,*}(\theta)=Z_{1,*}(\theta)
 =\sum_{u=0}^{2P-1}e(2u\theta),
\tag{175.R16}
\]

for which the calculation above is exactly
\(Q_{4P}^*-Q_{2P}^*=P^2=MD/8\). This abstract \(Z_*\) need not be a
literal cardinal image and must be labelled accordingly. Alternatively,
the candidate should retain its current, narrower wording
“coefficient-insensitive physical scale is sharp.”

### 3.5 Literal and owner boundary

The telescope and weighted Abel identity are coefficient-independent.
They survive dechirping, arbitrary coefficient phases, constant
character, and erased selector. That is evidence that the scale algebra
has not used the literal symbol, not evidence against the literal target.

The selected-pair identity, squarefree/coprimality projectors, and
no-pair positive-character rows justify only the stated local algebraic
no-go. They do not exclude a joint product/gap/character/phase theorem.
Likewise, the one-site control shows that a fixed positive dual diagonal
is not the physical zero diagonal. It supplies no lower mass.

Accordingly the durable statement must stop at the scale-telescope and
coefficient-uniform positive-capacity obstruction. The first open
coefficient-sensitive theorem is \(Q_M^*\ll L^3X^\varepsilon\), or its
exact physical/dual equivalent.

## 4. First doubtful or unproved step

After the repairs, there is no doubtful algebraic step in (175.C5)--(175.C7),
(175.C9)--(175.C17), or the physical diagnostic. The printed (175.C8) is
the sole false displayed formula and must be repaired by adding the plus
sign in (175.R4).

The first genuinely unproved mathematical step is

\[
 \boxed{Q_M^*\ll_\varepsilon L^3X^\varepsilon}
\]

for the complete literal residual transform. Neither the endpoint
telescope, the \(L^2\) energy, Fejer positivity, the physical diagnostic,
the selector identity, nor profile variation proves this. Any affirmative
continuation must exploit a literal property absent from dechirped,
arbitrary-phase, constant-character, and erased-selector controls before
using positivity.

The candidate's sentence after (175.C7) should not leave “endpoint energy
comparison” as though \(Q_{R_0}^*\) could cancel an \(L^4\) maximal
endpoint. Equation (175.R2) proves that it cannot: the entire missing
factor belongs to \(Q_M^*\).

## 5. Control tests and outcomes

| Control or seam | Outcome |
|---|---|
| Exact \(i/2\), \(1/8\), both parity branches, one outer real part | **PASS.** The recognition of the complete double sum as \(|Z_{\epsilon,*}|^2\) is exact and occurs only after full frequency recombination. |
| Positivity of \(Q_R^*\) | **PASS.** \(F_R\ge0\); no claim is made that a link difference is positive. |
| Lower endpoint \(Q_{R_0}^*\) | **PASS after explicit repair.** Equation (175.R2) gives \(O(L^3X^\varepsilon)\). |
| One-sided equivalence to \(Q_M^*\) | **PASS after explicit repair.** Equation (175.R3) uses both \(Q_{R_0}^*\ge0\) and its target-safe upper bound. |
| Weighted scale Abel | **FAIL as printed; PASS after repair.** Add the missing plus sign before the interior sum in (175.C8). |
| Strict final link | **PASS.** The telescope is finite and uses the exact value \(R_K=M\); no doubling identity is applied to the final strict link. |
| Ordinary-zero collective restoration | **PASS.** Equations (175.R8)--(175.R9) retain all odd \(k\)-modes before the bound. |
| Once-only short correction | **PASS.** It occurs once in (175.C14)--(175.C15). |
| Physical gap signs | **PASS.** \(f_S(r)-f_R(r)\ge0\) for every fixed nonzero physical gap; there is no alternating scale sign. |
| Exact \(L^4\) physical diagnostic | **PASS.** Equations (175.R13)--(175.R15) verify \((8P^2+1)/3\) and the lower constant \(1/12\). |
| Dechirped control | **PASS as method falsification only.** It is nonliteral and proves no lower bound for K26 or the literal \(Q_M^*\). |
| Arbitrary-sign/phase control | **PASS in scope.** The telescope is coefficient-blind; a coefficient-uniform proof would also cover phase-adapted arrays. |
| Constant-character and erased-selector shadows | **PASS in scope.** They show that scale algebra alone uses neither character nor selector; they are not literal counterexamples. |
| Selected/no-pair and Möbius identities | **PASS as local no-go only.** They do not rule out a nonlocal literal correlation theorem. |
| One-site and fixed dual diagonal | **PASS.** Every physical endpoint difference vanishes on one site, so a surviving fixed dual diagonal lacks compensating modes. |
| Rank-one peak | **REPAIR NEEDED FOR COMPLETENESS.** “Not used” is too terse. Either add the abstract control (175.R16), or state explicitly that rank-one/centred-peak positivity is inherited from Round 172 and is not a literal lower bound. |
| Round-173 tangent self-return | **PASS in scope.** The candidate does not reuse the parked first-difference route; it must not claim to exclude other nonlocal signed mechanisms. |
| Downstream owner scope | **PASS.** The candidate assigns no implication edge and leaves K26, residual completion, every larger M2/M1 owner, endpoint assembly, M9, bridges, theorem, and exponents open. |

No numerical experiment or external source was used.

## 6. Dependencies and exact artifacts used

This review used:

1. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/candidates/formalized_whole_chain_scale_telescope_obstruction.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/reports/actual_symbol_capacity_hostile_audit.md;
3. the Round-175 strategy, active campaign, and exact kernels already
   incorporated by those two artifacts; and
4. no sibling Round-175 report, shared state mutation, synthesis, web
   source, or computation.

The review reproduced the decisive norm estimate, endpoint zero-sector
bound, weighted Abel identity, and diagnostic constants directly.

## 7. Recommended state effect

**Recommended effect: revise the candidate, then promote one
route-scoped obstruction node with no implication edge and no status
change for any target owner.**

Promotion is justified after:

1. correcting (175.C8) to (175.R4);
2. inserting the explicit lower-endpoint estimate (175.R2) and one-sided
   equivalence (175.R3);
3. sharpening (175.C20) to the directly relevant diagnostic ratio
   \((1/12)L^{1-8\varepsilon_0}\) and specifying \(H=L^2\); and
4. either adding the abstract rank-one positive-operator control
   (175.R16) or limiting the sharpness claim strictly to the physical
   coefficient-uniform interface.

The durable obstruction may assert only:

- the unweighted whole chain is the endpoint coboundary
  \(Q_M^*-Q_{R_0}^*\);
- \(Q_{R_0}^*\) is target-safe, so the one-sided target is equivalent to
  the still-open literal maximal energy \(Q_M^*\ll L^3X^\varepsilon\);
- weighted scale Abel, Haar/martingale normalization, and
  coefficient-independent positivity restore \(L^4X^\varepsilon\); and
- nonliteral controls make this method capacity sharp but give no physical
  lower mass.

Do not promote the desired \(Q_M^*\ll L^3X^\varepsilon\) statement
(175.H5), (175.5), K26, the complete residual scalar, full \(t=1\), hard
TOP, BAL, UNBAL, M9--M2, either M1 route, endpoint uniformity, M9, either
bridge, the quarter theorem, or either exponent. Equation (175.C17) is
only the proved \(L^4X^\varepsilon\) capacity bound. The appropriate
terminal classification remains

\[
 \boxed{\texttt{whole\_chain\_actual\_symbol\_capacity\_or\_self\_return\_no\_go}.}
\]
