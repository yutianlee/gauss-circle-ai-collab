# Round 175 post-repair verification: positive capacity and owner scope

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Reviewed artifact: candidates/formalized_whole_chain_scale_telescope_obstruction.md
- Review seam: repaired power, scale normalization, controls, and owner quarantine
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211

## 1. Result

\[
\boxed{\textbf{GREEN}}
\]

The repaired candidate passes the positive-capacity and owner-scope seam.
Equation (175.C8) now has the required interior plus sign; (175.C8a)--(175.C8b)
give the correctly normalized positive Haar/Fejer decrease; and
(175.C16)--(175.C17b) prove that the lower endpoint is target-safe and
that the one-sided whole-chain target is equivalent at target strength to
the still-open literal maximal-energy estimate

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon.
\]

The constants in (175.C18)--(175.C20) are exact. Equation (175.C20a)
cleanly separates the abstract positive-operator control from the physical
dechirped control and from the literal cardinal image. All false controls
remain method-capacity diagnostics only. The candidate expressly leaves
\(Q_M^*\ll L^3X^\varepsilon\), K26, and every downstream owner open.

No remaining mathematical, power-ledger, normalization, control-scope, or
owner-scope defect was found.

## 2. Exact statement and hypotheses

Under the candidate's complete literal coefficient, parity, cardinal,
endpoint, strict-terminal, and zero-extension hypotheses, define

\[
 Q_R^*={1\over2}\sum_{\epsilon=0}^1
 \int_0^1F_R(\theta)|Z_{\epsilon,*}(\theta)|^2\,d\theta.
\]

The verified conclusions are:

1. \(\mathcal N_{R,S}=Q_S^*-Q_R^*\) and
   \(\sum_j\mathcal N_{R_j,R_{j+1}}=Q_M^*-Q_{R_0}^*\);
2. \(Q_R^*\ge0\) and \(Q_R^*\ll_\varepsilon RL^2X^\varepsilon\);
3. \(Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon\);
4. the one-sided chain target is equivalent to
   \(Q_M^*\ll_\varepsilon L^3X^\varepsilon\);
5. coefficient-independent positive closure has \(L^4X^\varepsilon\)
   capacity at \(R=M\); and
6. the exact identities justify only a route-scoped obstruction, with no
   implication to K26 or a larger owner.

## 3. Proof or derivation

### 3.1 Corrected weighted scale Abel identity

The repaired equation is

\[
\sum_{j=0}^{K-1}a_j\mathcal N_{R_j,R_{j+1}}
=a_{K-1}Q_M^*-a_0Q_{R_0}^*
 +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*.
\tag{175.V1}
\]

Indeed, with \(Q_j=Q_{R_j}^*\),

\[
\sum_{j=0}^{K-1}a_j(Q_{j+1}-Q_j)
=a_{K-1}Q_K-a_0Q_0
 +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_j.
\]

For \(a_j\equiv1\), all interior terms vanish exactly. Thus no artificial
scale weight supplies a saving for the unweighted target.

### 3.2 Haar/Fejer normalization

For integer \(R\), the Fejer formula gives

\[
 F_{2R}(\theta)=2F_R(\theta)\cos^2(\pi R\theta).
\]

Therefore

\[
 2F_R-F_{2R}
 =2F_R\sin^2(\pi R\theta)\ge0,
\tag{175.V2}
\]

which proves \(\mathcal H_R^*\ge0\) in (175.C8a). Direct subtraction gives

\[
 Q_{2R}^*=2Q_R^*-\mathcal H_R^*,
\qquad
 {Q_{2R}^*\over2R}
 ={Q_R^*\over R}-{\mathcal H_R^*\over2R}.
\tag{175.V3}
\]

Hence the genuine positive decrease is normalized by \(1/R\). Returning
to the unweighted maximal endpoint multiplies by the top scale \(M\) and
restores \(ML^2\asymp L^4\). The candidate correctly excludes a strict
final link from (175.V3) and uses its exact Fejer difference instead.

### 3.3 Lower endpoint and maximal-energy equivalence

The collective ordinary-zero estimate and Parseval yield

\[
 \sum_{\epsilon=0}^1\|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

Since \(0\le F_{R_0}\le R_0\),

\[
 0\le Q_{R_0}^*
 \le {R_0\over2}\sum_{\epsilon=0}^1
 \|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.V4}
\]

Put \(S_*=Q_M^*-Q_{R_0}^*\). If
\(S_*\ll L^3X^\varepsilon\), then
\(Q_M^*=S_*+Q_{R_0}^*\ll L^3X^\varepsilon\). Conversely, if
\(Q_M^*\ll L^3X^\varepsilon\), positivity gives
\(S_*\le Q_M^*\ll L^3X^\varepsilon\). This verifies (175.C17b) exactly
for the required one-sided upper bound.

The candidate does not claim this maximal estimate is proved. It states
that it is the first open literal theorem.

### 3.4 Exact physical diagnostic constants

With \(L=2n\), \(P=n^2\), \(M=4P=L^2\), and \(z_N=1\) on the \(2P\)
even sites of an \(M\)-site interval,

\[
 D=2P,\qquad A_{2s}=2P-s\quad(1\le s<2P).
\]

Thus

\[
\begin{aligned}
 \mathfrak E_M^{(2)}
 &=2P+2\sum_{s=1}^{2P-1}
 \left(1-{s\over2P}\right)(2P-s)\\
 &=2P+{1\over P}\sum_{t=1}^{2P-1}t^2
 ={8P^2+1\over3},
\end{aligned}
\]

confirming (175.C18). Since \(R_0=2n\) and \(D=2n^2\),

\[
 \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 \ge {8n^4+1\over3}-4n^3
 \ge {4n^4\over3}={L^4\over12}
\]

for \(n\ge3\). The difference between the middle and final lower bounds is
\((4n^3(n-3)+1)/3\ge0\). With \(X=L^8\), \(J=L^4\), and
\(H=L^2=J^{1/2}\),

\[
 {\mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
  \over L^3X^{\varepsilon_0}}
 \ge {1\over12}L^{1-8\varepsilon_0}\to\infty
\]

for \(0<\varepsilon_0<1/8\). Equations (175.C18)--(175.C20), including
the constant \(1/12\), are correct.

### 3.5 Abstract control separation

For

\[
 Z_{0,*}=Z_{1,*}=\sum_{u=0}^{2P-1}e(2u\theta),
\]

the same exact tent calculation gives

\[
 Q_{4P}^*-Q_{2P}^*=P^2={MD\over8}.
\]

This verifies (175.C20a) as an abstract sharpness control for the positive
operator. The candidate explicitly says that this \(Z_*\) need not be a
literal cardinal image. Separately, the physical even-site array is
explicitly phase-dechirped and nonliteral. Neither diagnostic is presented
as literal lower mass.

## 4. First doubtful or unproved step

The first unproved affirmative statement remains

\[
 \boxed{Q_M^*\ll_\varepsilon L^3X^\varepsilon}
\]

for the complete literal residual transform. The repaired candidate
correctly identifies it as open and equivalent, through target-safe seams,
to the one-sided whole-chain/K26 endpoint estimate.

No doubtful step remains in the endpoint telescope, corrected weighted
Abel identity, normalized Haar identity, lower-endpoint estimate,
ordinary-zero restoration, short correction, or diagnostic arithmetic.

## 5. Control tests and outcomes

| Seam or control | Outcome |
|---|---|
| Corrected (175.C8) | **GREEN.** The missing plus sign is restored and the indices are exact. |
| (175.C8a)--(175.C8b) | **GREEN.** Equation (175.V2) proves positivity; normalization by \(1/R\) is exact. |
| Strict terminal link | **GREEN.** It is excluded from the doubling identity and retained through the literal Fejer difference. |
| (175.C16)--(175.C17a) | **GREEN.** The \(L^2\) norm bound gives \(Q_{R_0}^*\ll L^3X^\varepsilon\). |
| (175.C17b) | **GREEN.** Both directions of the one-sided equivalence are valid. |
| (175.C18)--(175.C20) | **GREEN.** The formulas \((8P^2+1)/3\), \(L^4/12\), and the ratio with \(1/12\) are exact. |
| Abstract (175.C20a) | **GREEN.** It attains \(P^2=MD/8\) and is explicitly quarantined from the literal cardinal image. |
| Dechirped and arbitrary-coefficient controls | **GREEN.** They falsify symbol-blind methods only and are not physical lower bounds. |
| Constant-character and erased-selector shadows | **GREEN.** They show the scale algebra is coefficient-independent; they do not disprove the literal target. |
| Selected/no-pair and Möbius controls | **GREEN.** Their scope is local algebraic obstruction only; joint literal correlation remains unexcluded. |
| One-site/fixed-dual-diagonal control | **GREEN.** The candidate does not identify a transformed diagonal with the zero physical diagonal. |
| Rank-one centred peak | **GREEN.** The abstract control is tied to both peaks and labelled nonliteral. |
| Round-173 scope | **GREEN.** The parked tangent first-difference route is not reused or broadened. |
| Claim that \(Q_M^*\) is proved | **GREEN: absent.** The candidate calls it the first open theorem. |
| Literal lower-mass claim from diagnostics | **GREEN: absent.** Both physical and abstract controls are expressly diagnostic. |
| Owner quarantine | **GREEN.** No implication edge or downstream status change is claimed. |

## 6. Dependencies and artifact audit

This verification used only the repaired candidate and the prior
positive-capacity review for the same seam. No shared state, synthesis,
sibling report, source, or computation was used.

The candidate file audit is:

| Audit | Result |
|---|---:|
| Bytes | 15,769 |
| CR bytes | 0 |
| TAB bytes | 0 |
| NUL bytes | 0 |
| Unicode replacement characters | 0 |
| Numbered sections | 7 |
| Display delimiters | \(36\) opening / \(36\) closing |
| Inline delimiters | \(77\) opening / \(77\) closing |
| aligned environments | \(4\) opening / \(4\) closing |
| cases environments | \(2\) opening / \(2\) closing |
| Equation tags | 36, all unique |

The repaired candidate is mechanically clean under the requested
byte/tag/display audit.

## 7. Recommended state effect

**GREEN for promotion of exactly one route-scoped obstruction node after
the conductor's normal graph validation.**

The node may record:

1. exact collapse of the whole stopped chain to
   \(Q_M^*-Q_{R_0}^*\);
2. target safety of \(Q_{R_0}^*\) and equivalence of the one-sided target
   to the open literal maximal-energy estimate;
3. restored \(L^4X^\varepsilon\) capacity for coefficient-independent
   Abel, Haar, martingale, and positive-operator closure; and
4. sharp nonliteral physical and abstract controls, with no physical
   lower-mass interpretation.

The node has no implication edge. Do not promote
\(Q_M^*\ll L^3X^\varepsilon\), the Round-175 target, K26, the complete
residual scalar, full \(t=1\), another hard-TOP channel, hard TOP, BAL,
UNBAL, M9--M2, either M1 route, endpoint uniformity, M9, either bridge,
the quarter theorem, or either exponent.

