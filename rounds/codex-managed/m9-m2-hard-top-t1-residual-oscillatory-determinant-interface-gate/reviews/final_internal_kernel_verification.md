# Final internal-kernel verification

## 1. Result

**PASS.** The final kernel is homogeneous and internally proved. It contains only:

- the multiplicity-one determinant and free-orbit representation;
- the exact endpoint quadratic-form identity;
- the Schur \(L^3X^\varepsilon\) upper-capacity bound; and
- the owner-complete fixed-\(B\) polylogarithmic-shift estimate.

It contains no source theorem application, source-power claim, bare-orbit source lemma, or source-dependent no-go. It does not promote K17a, the residual scalar, a parent, a bridge, or an exponent.

## 2. Exact statement and hypotheses

The kernel states all hypotheses needed for its formulas:

\[
J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
R_0=\lceil L\rceil,\qquad 0<\gamma<1,
\]

\[
d,m\asymp L,\qquad d\ \mathrm{odd},\qquad
|\lambda_{dm}(d)|\ll1,
\]

with the complete literal selector, endpoint, and zero-extension data retained in \(\lambda\). It defines the endpoint set, product map, directed kernel, operator convention, and fixed-\(B\) cutoff

\[
R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\}.
\]

No missing regularity, automorphy, source-class, or cancellation hypothesis is used.

## 3. Proof or derivation

The incidence map

\[
(N,r,d,d')\longleftrightarrow
\begin{pmatrix}d'&d\\N/d&(N+r)/d'\end{pmatrix}
\]

is bijective and has determinant \(r\). A left action by a subgroup of
\(\mathrm{SL}_2(\mathbb Z)\) preserves determinants; for \(r\ne0\), freeness follows from \(A\) being invertible over \(\mathbb Q\). Thus the orbit statement introduces no stabilizer multiplicity.

The endpoint product

\[
u_L(y)\overline{u_L(x)}
\]

reproduces exactly the two character factors, two literal divisor atoms, and square-root phase. The directed kernel inserts precisely the Fejer, positive even gap, opposing-displacement, and low-gcd restrictions. Hence (167.K6) is exact and does not double-count coefficient sums.

For fixed endpoint and gap, the opposite endpoint has at most one choice per divisor of the forced product. Both Schur degrees are therefore

\[
\ll_\eta LX^\eta.
\]

Together with

\[
\|u_L\|_2^2\ll_\eta L^2X^\eta,
\]

epsilon relabelling gives (167.K9).

For \(r\le R_{\log}\), taking one modulus outside the complete sector gives the divisor-pair count in (167.K16). The two bounds \(X^{\varepsilon/4}\), the logarithmic factor \(X^{\varepsilon/2}\), and \(O(L^2)\) products give exactly \(L^2X^\varepsilon\). All literal restrictions precede the majorization, so the strict sector is owner-complete.

## 4. First doubtful or unproved step

There is no doubtful step inside the stated kernel. The first unproved analytic step is deliberately outside it:

\[
\Re\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},g<\gamma L}
\ll_{\gamma,\varepsilon}L^2X^\varepsilon
\]

for the remaining non-polylogarithmic shifts. The kernel correctly leaves this open.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Incidence multiplicity | **PASS** |
| Free left-orbit multiplicity | **PASS** |
| Endpoint identity and coefficient ownership | **PASS** |
| Schur degree and epsilon relabelling | **PASS** |
| Fixed-\(B\) polylogarithmic estimate | **PASS** |
| Polylogarithmic owner completeness | **PASS** |
| Source-dependent content excluded | **PASS** |
| K17a and downstream scope | **PASS** |

## 6. Dependencies and exact artifacts used

This verification compared:

1. proofs/kernels/m9_m2_hard_top_t1_residual_determinant_endpoint_polylog_shift_reduction.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/candidates/conductor_round167_determinant_endpoint_polylog_reduction.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/conductor_candidate_mathematical_review.md.

No claimant file or shared state was edited.

## 7. Recommended state effect

**Verify as proved-internal reduction evidence.** The kernel may support only its determinant/endpoint identity, Schur upper capacity, and polylogarithmic strict sector. Keep K17a, the complete residual scalar, every downstream parent and bridge, and all exponent ledgers unchanged.
