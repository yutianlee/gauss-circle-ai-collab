# Round 175 final-kernel mathematical verification

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Round: 175
- Role: independent final-kernel verifier
- Kernel: proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Evidence status: final verification only; no kernel or shared-state mutation

## 1. Result and verdict

\[
\boxed{\mathrm{GREEN}}
\]

The durable kernel is mathematically identical to the repaired candidate
from the first numbered section through the end of the artifact. The only
differences are the title and preamble metadata appropriate to promotion
from candidate evidence to a durable proof kernel.

Every displayed identity, sign, normalization, conditional terminal case,
collective ordinary-zero restoration, K26 seam, lower-endpoint equivalence,
and diagnostic-scope restriction agrees with the repaired candidate, all
three GREEN post-repair verifications, and the Round-175 conductor
adjudication. No remaining mathematical or artifact-hygiene defect was
found.

This GREEN verdict certifies only the route-scoped obstruction. It does not
prove the open maximal estimate, K26, or any downstream theorem.

## 2. Exact copy and metadata audit

Let the mathematical body begin at the literal line

\[
 \text{“## 1. Exact setting”.}
\]

After normalizing line endings to LF, the kernel body and repaired-candidate
body compare equal under ordinal character comparison. Both files already
contain zero CR bytes, so this is also an exact body copy rather than a
line-ending reconciliation. Their common mathematical-body SHA-256 is

\[
 \texttt{6ceb3415c4ebfaed7d0ea61b6a5b2a2120b8efd3aaeb39128abce5376cc9f24b}.
\]

The full-file hashes differ, as expected:

\[
\begin{aligned}
 \text{kernel: }&
 \texttt{cac96682c667a70727f543ec9b7d156845c7c0c2ecc8a71154e0c7b632a31881},\\
 \text{candidate: }&
 \texttt{25ebdc019bcb9ea7af012bb5e2885ea4d9ac7f68bc6a2a2182d3be66bc99e843}.
\end{aligned}
\]

The preamble differences are metadata-only:

1. the title changes from “Candidate: whole-chain Fejer endpoint-collapse
   obstruction” to the durable-kernel title;
2. the role changes from conductor-selected candidate to
   conductor-selected durable proof kernel;
3. the terminal label
   \(\texttt{whole\_chain\_actual\_symbol\_capacity\_or\_self\_return\_no\_go}\)
   is added; and
4. evidence status changes from candidate pending seam review to proved
   internally after independent seam review.

Campaign, round, and starting graph are unchanged. The terminal label and
proved-internal obstruction scope agree exactly with the conductor
adjudication.

## 3. Proof and derivation verification

### 3.1 Literal coefficient and physical transform

Equations (175.C0)--(175.C2b) retain the literal
\(\omega_L\rho_NA_N\) coefficient, selected/no-pair cases, squarefree and
two-adic data, hard profile, point values, support crossings, and full-line
zero extension. The square root is evaluated only on positive live support.

Equation (175.C3) has the exact physical-transform equality

\[
 Z_\epsilon(\theta)
 =\sum_N(-1)^{\epsilon N}z_Ne(N\theta)
 ={i\over2}\sum_{k\ \mathrm{odd}}\chi_4(k)
   \sum_{\ell\in\mathbb Z}U_{k,\ell}^{(\epsilon)}(\theta).
\]

The \(+i/2\) sign is correct because the odd-character comb contributes
\(-2i\), and \((i/2)(-2i)=1\). Since \(d\) is odd,
\((-1)^{\epsilon m}=(-1)^{\epsilon N}\). Both parity branches are
therefore restored exactly.

Writing
\(A_{\epsilon,*}=\sum_{k\ \mathrm{odd}}\chi_4(k)
\sum_{\ell\ne0}U_{k,\ell}^{(\epsilon)}\), one has
\(Z_{\epsilon,*}=(i/2)A_{\epsilon,*}\). Hence

\[
 {1\over2}\sum_\epsilon\int B_{R,S}|Z_{\epsilon,*}|^2
 ={1\over8}\sum_\epsilon\int B_{R,S}|A_{\epsilon,*}|^2
 =\mathcal N_{R,S}.
\]

Thus (175.C6) has the correct \(|i/2|^2=1/4\), parity factor \(1/2\),
total \(1/8\), and one outer real part.

### 3.2 Scale coboundary, Abel sign, Haar normalization, and terminal link

Finite telescoping proves

\[
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 =Q_M^*-Q_{R_0}^*.
\]

The corrected weighted identity (175.C8) has the mandatory sign

\[
 +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*.
\]

At a genuine doubling,
\(2F_R-F_{2R}=2F_R\sin^2(\pi R\theta)\ge0\), so
(175.C8a)--(175.C8b) have the correct sign and \(1/R\) normalization.
The doubling identity is not applied to a non-doubling endpoint.

The terminal conditions are exhaustive and exact:

\[
 R_{K-1}<M<2R_{K-1}
 \quad\text{gives the strict link},\qquad
 M=2R_{K-1}
 \quad\text{gives the final doubling}.
\]

Every chain identity ends at the actual \(R_K=M\), with no rounded scale.

### 3.3 Physical gaps and transformed tuples

Equations (175.C9)--(175.C10) are correctly restricted to integer physical
gaps. Their link coefficients are nonnegative and telescope to
\(f_M-f_{R_0}\). The kernel separately states that a fixed transformed
tuple \((k,k',\ell,\ell')\) receives only the endpoint telescope and is
not a physical-gap diagonal. It neither deletes such a tuple nor assigns
it the physical-gap lower weight.

### 3.4 Collective zero sector and K26 restoration

Equation (175.C11a) restores exactly the sector containing at least one
ordinary zero frequency:

\[
 {1\over2}\sum_\epsilon\int B_{R,S}
 \left(|Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})\right).
\]

This counts \((0,0)\), \((0,*)\), and \((*,0)\) once, after complete
odd-character recombination. Linearity gives the single endpoint
\(\mathcal Z_{R_0,M}\), and (175.C13) has the correct bound

\[
 |\mathcal Z_{R_0,M}|
 \ll (M+R_0)
 \left(D_L^{1/2}{L^2\over J}+{L^4\over J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\]

Equations (175.C13a)--(175.C13b) define the physical correlation
\(A_r\), the exact medium/long scalar \(T_{26}\), and the once-only
\(B_{\mathrm{short}}\). The identity

\[
 {1\over2}
 \left(\mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}\right)
 =T_{26}+B_{\mathrm{short}}
\]

has the correct sign. Here \(T_{26}\) is exactly the left side of
(165.K26). Combining it with the collective zero restoration gives

\[
 \sum_j\mathcal N_{R_j,R_{j+1}}
 =2(T_{26}+B_{\mathrm{short}})-\mathcal Z_{R_0,M},
\]

so (175.C15) has the correct factor \(2\) and minus sign. Both correction
terms are target-safe, and the short correction is paid once.

### 3.5 Lower endpoint and positive-capacity controls

From (175.C16) and \(0\le F_{R_0}\le R_0\),

\[
 0\le Q_{R_0}^*
 \le {R_0\over2}\sum_\epsilon\|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.
\]

Therefore (175.C17b) is a valid equivalence of one-sided upper bounds:
the forward direction adds the target-safe lower endpoint, while the
reverse direction subtracts a nonnegative quantity. The still-open theorem
is precisely

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon.
\]

The physical diagnostic (175.C18)--(175.C20) has the exact values

\[
 \mathfrak E_M^{(2)}={8P^2+1\over3},\qquad
 \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 \ge {L^4\over12}.
\]

The parameter choice \(X=L^8\), \(J=L^4\), \(H=L^2\) is admissible.
The prose correctly says this is a dechirped nonliteral physical
parity-Fejer diagnostic, not a literal \(Q_M^*\) or K26 lower bound.
The abstract control (175.C20a) separately gives
\(Q_{4P}^*-Q_{2P}^*=P^2=MD/8\) and is expressly not required to be a
literal cardinal image.

## 4. First doubtful or unproved step

There is no doubtful step inside the durable obstruction. The first
unproved affirmative statement is

\[
 \boxed{Q_M^*\ll_\varepsilon L^3X^\varepsilon,}
\]

equivalently the one-sided K26 estimate after the collective zero-containing
sector and once-only short correction are restored. The kernel labels this
statement open and derives no implication from it.

No coefficient-insensitive scale, Haar, martingale, physical diagnostic,
or abstract positive-operator control proves this literal maximal estimate.

## 5. Controls and artifact hygiene

### Mathematical controls

1. Arbitrary coefficients, phase dechirping, constant character, and
   erased selector leave the scale telescope intact; the kernel therefore
   does not misidentify the telescope as literal-symbol cancellation.
2. A one-site physical array has zero complete Fejer endpoint difference;
   an isolated transformed contribution must retain its compensating dual,
   cell, and boundary assembly.
3. Physical zero gaps remain distinct from fixed transformed diagonals.
4. Both centred rank-one peaks are only positive-capacity controls and
   yield no literal lower mass.
5. The selected-pair disjoint-support identity supplies no pointwise
   \(L^{-1}\), while no-pair all-\(1\bmod4\) rows are only an
   allowed-support warning.
6. The Round-173 tangent first-difference family is not reused.
7. The kernel expressly leaves direct literal endpoint, joint-transform,
   coefficient-sensitive positive, and fully signed nonlocal routes open.

These outcomes agree with all three post-repair verifications and the
conductor adjudication.

### Artifact audit

- Kernel bytes: 15,874.
- Full-file SHA-256:
  \(\texttt{cac96682c667a70727f543ec9b7d156845c7c0c2ecc8a71154e0c7b632a31881}\).
- Numbered sections: 7.
- Equation tags: 36; unique tags: 36; duplicates: 0.
- Display delimiters: 36 opening and 36 closing.
- Inline delimiters: 77 opening and 77 closing.
- Aligned environments: 4 opening and 4 closing.
- Cases environments: 2 opening and 2 closing.
- CR bytes: 0.
- TAB bytes: 0.
- NUL bytes: 0.
- Other forbidden C0 control bytes: 0.
- UTF-8 BOM: absent.
- Unicode replacement characters: 0.
- Accidental patch-prefix lines: 0.
- Trailing LF: present.

Literal uses of the ASCII TeX command \(\backslash\mathrm{rm}\) remain
ordinary backslash characters; the byte audit confirms that none is an
embedded carriage return.

## 6. Dependencies and exact artifacts used

The verification compared:

1. proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/candidates/formalized_whole_chain_scale_telescope_obstruction.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/reviews/blind_candidate_post_repair_verification.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/reviews/literal_candidate_post_repair_verification.md;
5. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/reviews/positive_capacity_post_repair_verification.md;
6. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/reviews/conductor_round175_adjudication.md;
7. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md; and
8. proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md.

No state file, State Patch, synthesis, proof draft, source card, web source,
or numerical experiment was used or modified in this verification.

## 7. Recommended state effect

Accept the durable kernel as GREEN proved-internal evidence for exactly one
route-scoped obstruction node:

\[
 \texttt{M9\text{-}M2\text{-}hard\text{-}top\text{-}t1\text{-}residual
 \text{-}whole\text{-}chain\text{-}scale\text{-}coboundary
 \text{-}positive\text{-}capacity\text{-}obstruction}.
\]

The node should carry terminal label

\[
 \texttt{whole\_chain\_actual\_symbol\_capacity\_or\_self\_return\_no\_go}
\]

and no implication edge. It may be attached only as route evidence to the
open residual Fejer reduction and the open hard-TOP endpoint owners, exactly
as directed by the conductor adjudication.

Do not promote the maximal estimate, the Round-175 target, K26, the
complete residual scalar, full \(t=1\), another hard-TOP channel, hard TOP,
BAL, UNBAL, M9--M2, either M1 route, endpoint uniformity, M9, a bridge, the
quarter theorem, or an exponent.
