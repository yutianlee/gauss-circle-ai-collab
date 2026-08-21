# Blind global exponent rederivation (Round 91)

## 1. Result

**Lemma (uniform one-third consequence of the frozen interface).**  The accepted hyperbola--Vaaler reduction, the literal fully weighted M1/M2 direct block menu, and the pointwise Fejer product count imply
\[
  P(X)\ll_\varepsilon X^{1/3+\varepsilon}
\]
for every real \(X\ge 2\).  The proof is pointwise in \(X\), uses neither an \(X\)-average nor M9, and covers every boundary of \(\Omega\).  Thus the sharp verdict on the frozen question is **yes**.  This establishes only the one-third envelope; it does not establish either conjectural quarter-scale hard-core estimate or any exponent below \(1/3\).

## 2. Exact statement and hypotheses

Fix \(\varepsilon>0\) and real \(X\ge2\).  Assume exactly the frozen statements in the derivation packet:

- H1--H3 give the exact floor-compatible reduction, and H4 gives (91.2), including \(\psi_F(n)=-1/2\) and \(K_H(0)/(2H+2)=1/2\).
- Denominators below \(X^{1/4}\) contribute \(O_\varepsilon(X^{1/4+\varepsilon})\).  Active denominator shells satisfy \(X^{1/4}\le D\le X^{1/2}\), use \(H_D\asymp DX^{-1/4}\), and split into \(O(\log X)\) dyadic frequency blocks.
- For every *actual, fully weighted* M1 or M2 block, including its Vaaler coefficient, M1 spatial character, M2 \(\chi_4(h)\) factor and quarter shift, both signs, spatial partition, and hard endpoint profile, the T2S and full second-derivative rows of (91.5) hold uniformly.
- The positive pointwise kernel majorant is (91.7), with the analogous exact product count for both shifted legs, and its far term is \(DH_D^{-2}\asymp X^{1/2}/D\).

Writing \(D=X^\delta\), \(L=X^\ell\), the literal block parameters lie in
\[
 \Omega=\{1/4\le\delta\le1/2,\ 0\le\ell\le\delta-1/4\}.
\]
Fixed comparison constants in \(H_D\asymp DX^{-1/4}\) or at a clipped dyadic endpoint change exponents by \(O(1/\log X)\), hence only by an absolute multiplicative constant; equivalently they are absorbed in the available \(X^\varepsilon\).  No extra normalization factor is to be restored after applying (91.5).

## 3. Proof or derivation

Put \(x=\delta-\ell\).  If \(x\le1/3\), the frequency-first/T2S row gives the fully weighted block bound
\[
  B(D,L)\ll_\eta X^{x+\eta}\le X^{1/3+\eta}.
\]
If \(x\ge1/3\), the two nonconstant exponents in the full second-derivative estimate are
\[
 a={1+\ell-\delta\over2}={1-x\over2}\le {1\over3},
 \qquad
 b={3\delta-1-\ell\over2}={2\delta+x-1\over2}.
\]
Since \(\ell\ge0\) gives \(x\le\delta\), and \(\delta\le1/2\),
\[
 b\le {3\delta-1\over2}\le {1\over4}.
\]
The remaining exponent is \(0\).  Therefore the literal sum of the second-derivative terms is at most
\[
 X^{a+\eta}+X^{b+\eta}+X^\eta\ll X^{1/3+\eta};
\]
replacing this sum by its displayed maximum in (91.5) loses nothing.  At \(x=1/3\) either estimate applies.  The other hard boundaries are also covered: \(\delta=1/4\) and \(\ell=\delta-1/4\) force \(x=1/4\) and use T2S; when \(L=1\), \(x=\delta\), so T2S applies for \(\delta\le1/3\) and the full bound for \(\delta\ge1/3\); at \(D=X^{1/2}\), the second exponent is still at most \(1/4\).  Thus every active literal block is \(O_\eta(X^{1/3+\eta})\), including the hard top profile.

For completeness, the residual reconciliation is pointwise.  In the unshifted leg, if \(m\) is the relevant nearest integer, then
\[
 d(X/d-m)=X-dm,
\]
so the exact product is \(n=dm\).  In a shifted leg \(\rho\in\{1,3\}\),
\[
 4d\left({X/d+\rho\over4}-m\right)=X-d(4m-\rho),
\]
so the exact product is \(n=d(4m-\rho)\).  For fixed \(n\), either representation has at most \(\tau(n)\ll_\eta X^\eta\) admissible choices of \(d\); the congruence restriction in the shifted case can only reduce that count.  Consequently each near part is bounded by
\[
 X^\eta S_\Delta(X),\qquad
 S_\Delta(X)=\sum_{n\asymp X}\min\left(1,{\Delta^2\over|X-n|^2}\right),
 \qquad \Delta=D/H_D\asymp X^{1/4}.
\]
Uniformly for real \(X\), the integers with \(|X-n|\le\Delta\) contribute \(O(\Delta+1)\), while
\[
 \Delta^2\sum_{|X-n|>\Delta}|X-n|^{-2}\ll\Delta.
\]
Thus \(S_\Delta(X)\ll\Delta\ll X^{1/4}\).  If \(X/d\), or a shifted argument, is exactly integral, the corresponding \(n=X\) term is interpreted as \(1\), exactly covering the kernel peak and the floor convention.  Half-open shells and the restriction \(d\le\lfloor\sqrt X\rfloor\) only remove nonnegative terms.  The far part satisfies
\[
 DH_D^{-2}\asymp {X^{1/2}\over D}\le X^{1/4}.
\]
Hence every active-shell Fejer residual is \(O_\eta(X^{1/4+\eta})\), for the unshifted leg and both shifts.

The end-to-end implication ledger is:

| Input | Operation | Output and unique owner |
|---|---|---|
| H1--H3 | Exact hyperbola/sawtooth identity | Floors, equality stars, signs, and the top cutoff remain exact; H1--H3 own the identity. |
| \(d<X^{1/4}\) | Elementary pre-Vaaler estimate | \(O_\eta(X^{1/4+\eta})\); the small-denominator owner. |
| Active shells plus H4 | Vaaler decomposition | Main frequency blocks plus positive Fejer residual; H4 owns the floor-compatible endpoint. |
| (91.7) and the exact products above | Pointwise product count | \(O_\eta(X^{1/4+\eta})\) per shell; R5 owns the residual, including kernel peaks and shifted legs. |
| (91.5) on literal blocks | The region split above | \(O_\eta(X^{1/3+\eta})\) per M1/M2 block; the direct block menu owns all actual coefficients and hard endpoint BV. |
| Dyadic assembly | Sum \(O(\log X)\) denominator shells and \(O(\log X)\) frequency blocks per shell | \(O_\varepsilon(X^{1/3+\varepsilon})\), after taking \(\eta<\varepsilon\) and absorbing \(O(\log^2X)\). |
| Exact H1--H3 identity | Recombine the uniquely owned pieces | \(P(X)\ll_\varepsilon X^{1/3+\varepsilon}\), uniformly for real \(X\). |

## 4. First doubtful or unproved step

There is no missing implication seam under the frozen hypotheses.  The first primitive fact not re-proved from lower-level formulas in the permitted packet is the assertion that (91.5) is uniform for each fully weighted literal M1/M2 block, including the sampled hard endpoint profile.  That assertion is explicitly an accepted input here, so it is a dependency rather than an unproved step in this statement-only derivation.  If (contrary to the packet) (91.5) bounded only an inner unweighted sum, or omitted the hard endpoint BV term, this would be the first missing seam; the frozen wording expressly rules out both readings.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_block_normalization` | **Pass.**  The menu quantifies over the actual fully weighted block; no factor \(D\), \(L\), or Vaaler coefficient is reinserted.  Fixed dyadic comparison constants are harmless. |
| `one_third_region_optimization` | **Pass.**  T2S covers \(x\le1/3\); the full bound covers \(x\ge1/3\), with exponents at most \(1/3,1/4,0\). |
| `second_derivative_small_curvature` | **Pass at the frozen statement interface.**  The accepted full bound is uniform on every actual block and includes the \(0\) term; \(L=1\), \(x=1/3\), and \(D=X^{1/2}\) were checked explicitly. |
| `actual_M1_M2_coefficients` | **Pass.**  M1's spatial character, M2's \(\chi_4(h)\), both signs, quarter shifts, partitions, and actual Vaaler weights remain inside the stated block estimate. |
| `R5_pointwise_product_count` | **Pass.**  The positive divisor-product argument gives \(S_\Delta(X)\ll\Delta\) for each real \(X\); no mean square is used. |
| `exact_product_and_floor_endpoint` | **Pass.**  The products are exactly \(dm\) and \(d(4m-\rho)\); exact integrality is the \(n=X\) peak, consistent with \(\psi_F(n)=-1/2\) and \(K_H(0)/(2H+2)=1/2\). |
| `hard_top_BV` | **Pass at the frozen statement interface.**  The direct menu includes the sampled hard endpoint profile, while truncation only decreases the positive residual majorant. |
| `small_denominator_owner` | **Pass.**  The elementary pre-Vaaler estimate uniquely owns \(D<X^{1/4}\). |
| `dyadic_frequency_and_denominator_assembly` | **Pass.**  At most \(O(\log^2X)\) block occurrences are absorbed by an epsilon split; the residual has only the denominator logarithm. |
| `real_X_uniformity` | **Pass.**  The lattice-tail estimate is translation-uniform, floors are retained, and all arguments are pointwise for real \(X\ge2\). |
| `downstream_scope` | **Pass.**  The conclusion is restricted to the R5 reconciliation, the uniform one-third envelope, and the one-third theorem. |

No numerical experiment was needed; every control is algebraic or pointwise.

## 6. Dependencies and exact artifacts used

The only artifacts used were:

- `rounds/codex-managed/gc-unconditional-exponent-extraction/briefs/blind_global_exponent_rederivation.md`;
- `rounds/codex-managed/gc-unconditional-exponent-extraction/derivation_packet.md`.

The derivation uses the packet at starting graph SHA-256 `b3a0a086608be2df3b56c6c9f996206796998b3afdf750b6162d760c614a811b`.  No proof-state file, strategy file, prior or sibling report, source card, web source, or computation was inspected.  The result depends on H1--H4, the elementary small-denominator estimate, the literal direct block menu (91.5), and the stated positive Fejer interface (91.7), and it does not depend on M9.

## 7. Recommended state effect

**Promote**, after the conductor's ordinary graph validation, the pointwise Fejer reconciliation, a uniform one-third M9 envelope, and the theorem \(P(X)\ll_\varepsilon X^{1/3+\varepsilon}\).  **Do not promote** `M9-M1`, `M9-M2`, `M9`, the endpoint exponent \(1/4\), `GC-target`, or any exponent below \(1/3\).  The proposed mechanism survives all required hostile controls; there is no first missing seam within the frozen statement interface.
