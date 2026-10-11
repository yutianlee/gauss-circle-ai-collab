# Round 200: independent review of the complete-source operator calculation

## Provenance and isolation status

- Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`.
- Research round: 200.
- Role: independent operator/normalization seam reviewer, **post-isolation**.
- Generated: 2026-09-23.
- Supplied graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`; the graph itself was not read for this review.
- This is a new bounded review after completion of the statement-only assignment. It is distinct from the original blind proof. `reports/blind_interval_operator_rederivation.md` remains frozen and unchanged.
- New context read: `controls/conductor_complete_source_operator_analysis.md`, first as submitted and then after the conductor's endpoint repair. The optional sibling reports were absent when this review started and were not awaited or read.
- Other context retained from the completed blind task: `protocol.md`, `briefs/independent_statement_packet.md`, and `briefs/blind_interval_operator_rederivation.md` in this campaign.
- Method: exact finite algebra and analytical reasoning. No numerical experiment, external source, shared-state edit, or graph promotion.

## 1. Result: green after the recorded endpoint repair

The patched conductor calculation is **GREEN within its stated finite-operator and conditional power-bookkeeping scope**.

- (200.O1), including conjugation and the factor two: green.
- (200.O2), including both parities and `R=1,2`: green.
- Finite-interval lower control: green after replacing `(1-j/M)` by `(1-j/M)_+` and restricting the stated untruncated comparison to `M>=R`.
- Square-root phase as a diagonal unitary conjugation: green.
- (200.O3) as the unproved actual-vector target, equivalent to the desired one-sided real correlation bound given the diagonal estimate: green.
- The factor `L` at the full-correlation/quadratic-form stage and factor `L^(1/2)` after scalar reconstruction: green.

The calculation proves a sharp obstruction to improving this particular full-line or long-interval **all-vector operator bound** using its separable phase. It does not prove a lower bound for the actual arithmetic vector and does not refute the arithmetic target.

The literal coefficient estimate and its Round-184/185 provenance are not independently audited here, since the underlying coefficient definitions were not in the permitted context. The power conclusions are verified conditional on the conductor's stated diagonal and reconstruction inputs.

## 2. Exact statements and hypotheses reviewed

Let `R>=1` be an integer and

\[
k_R(j)=\mathbf1_{2\mid j}(1-|j|/R)_+,
\qquad (K_Rz)_n=\sum_m k_R(n-m)z_m
\]

on `ell^2(Z)`. Initially take `z` finitely supported. Use the inner product conjugate-linear in its first argument, and set

\[
D=\sum_n|z_n|^2,
\qquad C_{\rm even}=\sum_{\substack{0<r<R\\2\mid r}}
(1-r/R)\sum_nz_{n+r}\overline{z_n}.
\]

For the finite-interval control, take any consecutive integer interval `I` of `M>=1` sites and `z=1_I`. The compression is `P_I K_R P_I`, acting on that interval with zero extension.

For the phase calculation, assume `X>=0` and real `sigma`. On the positive-index support set

\[
d_N=e(\sigma\sqrt{XN}),\qquad (D_\sigma c)_N=d_Nc_N,
\]

and extend `d_N` by any unit-modulus values elsewhere, for example one. For nonnegative `X,N`, `sqrt(XN)=sqrt(X)sqrt(N)`.

For the conditional power ledger, write

\[
R=\lceil L\rceil\asymp L,\quad
D\ll_\varepsilon L^2X^\varepsilon,\quad
F=\frac{M+R-1}{R}\ll L,
\]

in the stated large-shell regime. The last input is the scalar reconstruction cost. If `M~L^2` and `R~L`, it follows directly; the source support and exact coefficient hypotheses establishing these inputs are separate application dependencies.

## 3. Independent derivation

### 3.1 (200.O1) and positivity

Expanding the quadratic form gives

\[
\langle z,K_Rz\rangle
=\sum_{n,m}\overline{z_n}\,k_R(n-m)z_m.
\]

The diagonal is `D`. For each positive even `r<R`, the two orientations `m=n+r` and `n=m+r` contribute respectively

\[
(1-r/R)\sum_nz_{n+r}\overline{z_n}
\quad\text{and its complex conjugate}.
\]

Therefore

\[
Q_R(z):=\langle z,K_Rz\rangle=D+2\operatorname{Re}C_{\rm even},
\]

which verifies (200.O1) with the conductor's inner-product convention.

Independently, expansion of the two sliding energies gives

\[
Q_R(z)=\frac12\bigl(E_R(z)+E_R(((-1)^nz_n)_n)\bigr)\ge0.
\tag{R1}
\]

Thus the claimed nonnegativity does not require an unverified arithmetic theorem or any sign condition on `z`.

### 3.2 Exact full-line norm

Let `t=floor((R-1)/2)` and let the kernel's total mass be

\[
\lambda_R=\sum_jk_R(j)
=1+2\sum_{h=1}^t(1-2h/R)
=1+2t-\frac{2t(t+1)}R.
\]

If `R=2h`, then `t=h-1` and this equals `h=R/2`. If `R=2h+1`, then `t=h` and this equals `(R+R^{-1})/2`. For every `z`, the triangle inequality for the finitely many shift operators yields

\[
\|K_Rz\|_2\le\sum_jk_R(j)\|z\|_2=\lambda_R\|z\|_2.
\tag{R2}
\]

The interval test in the next subsection approaches `lambda_R` as `M` tends to infinity with `R` fixed, so the upper bound is sharp. This proves (200.O2) directly, without any issue about whether the constant infinite sequence lies in `ell^2`.

The conductor's Fourier derivation is also correct. The factor `(1+(-1)^j)/2` selecting even shifts gives exactly

\[
\widehat k_R(\theta)=\tfrac12\{F_R(\theta)+F_R(\theta+1/2)\},
\qquad F_R(\theta)=R^{-1}\left|\sum_{a=0}^{R-1}e(a\theta)\right|^2.
\]

The multiplier is nonnegative, and its absolute value is bounded by the sum of its nonnegative Fourier coefficients, `lambda_R`, with equality at zero. The formulas `F_R(0)=R`, `F_R(1/2)=0` for even `R`, and `F_R(1/2)=1/R` for odd `R` agree with the direct calculation.

### 3.3 Finite-interval control and exact truncation loss

For `z=1_I`, there are precisely `(M-|j|)_+` ordered pairs in `I` at displacement `j`. Since `D=M`, the exact Rayleigh quotient for every positive `M,R` is

\[
q_{R,M}:=\frac{\langle1_I,K_R1_I\rangle}{M}
=1+2\sum_{\substack{0<j<R\\2\mid j}}
(1-j/R)(1-j/M)_+.
\tag{R3}
\]

This verifies the repaired formula. For `M>=R`, no positive-part truncation is active on a nonzero summand, and direct summation gives the stronger exact result

\[
q_{R,M}=\lambda_R-\delta_{R,M},\qquad
\delta_{R,M}=
\begin{cases}
(R^2-4)/(6M),&R\text{ even},\\
(R^2-1)/(6M),&R\text{ odd}.
\end{cases}
\tag{R4}
\]

Indeed,

\[
\delta_{R,M}=\frac2M\sum_{h=1}^t2h(1-2h/R)
=\frac{2t(t+1)}M\left(1-\frac{2(2t+1)}{3R}\right),
\]

and substituting `t=h-1` or `t=h` yields (R4). Thus

\[
\lambda_R-\frac{R^2}{6M}
\le\|P_IK_RP_I\|_{2\to2}\le\lambda_R
\qquad(M\ge R).
\tag{R5}
\]

In particular `||P_I K_R P_I|| >= R/3` whenever `M>=R`, since `lambda_R>=R/2`. For `M~L^2` and `R~L`, the truncation loss is `O(1)` while `lambda_R~L`, giving the conductor's asserted comparable-to-`L` norm. The result concerns interval compression. It does not automatically assert the same lower bound for compression to an arbitrary sparse subset of that interval.

### 3.4 Exact phase conjugation

With `z=D_sigma c`,

\[
Q_R(z)=\langle c,D_\sigma^*K_RD_\sigma c\rangle.
\]

The conjugated matrix has entry

\[
\overline{d_N}\,k_R(N-N')d_{N'}
=k_R(N-N')e\bigl(\sigma\sqrt X(\sqrt{N'}-\sqrt N)\bigr),
\]

exactly as in the conductor calculation. `D_sigma` is unitary because every diagonal entry has modulus one, and its inverse is its adjoint. Thus

\[
\|D_\sigma^*K_RD_\sigma\|=\|K_R\|=\lambda_R.
\tag{R6}
\]

The same statement holds on a fixed support compression because its projection commutes with the diagonal unitary. On an interval, the explicit admissible control vector `c=D_sigma^*1_I` attains the quotient (R3). This is an arbitrary test vector for a universal operator estimate; no assertion is made that it equals the physical residual coefficient vector.

### 3.5 One-sided target and power ledger

From (200.O1),

\[
\operatorname{Re}C_{\rm even}=(Q_R-D)/2.
\tag{R7}
\]

If the diagonal estimate `D<<L^2 X^epsilon` is available, then the desired one-sided upper bound `Re C_even<<L^2 X^epsilon` implies `Q_R<<L^2 X^epsilon`. Conversely the latter implies the former immediately, because `D>=0`. This is the claimed equivalence of (200.O3). Positivity (R1) also gives `Re C_even>=-D/2`; no separate negative-tail estimate is needed.

An absolute upper bound on every shift or every sector is a stronger demand than (200.O3). An absolute bound on the **total real part** would in fact follow once the one-sided target and the diagonal estimate hold; it is not necessary to control the modulus of the complex correlation sum or the absolute values of its separate terms.

The universal estimate is

\[
0\le Q_R\le\lambda_RD.
\]

One can also quantify the conductor's absolute real-correlation bound directly. The off-diagonal kernel `K_R-I` has nonnegative entries and row sum `lambda_R-1`, so the same shift argument as (R2) gives

\[
|\operatorname{Re}C_{\rm even}|
\le\frac{\lambda_R-1}{2}D.
\tag{R8}
\]

For `R~L`, `D<<L^2 X^epsilon`, this is `O(L^3 X^epsilon)`, whereas the target is `O(L^2 X^epsilon)`: one factor of `L` at this stage. At `R=1,2`, `lambda_R=1` and (R8) correctly gives the identically zero off-diagonal correlation.

Finally the already verified connector is

\[
E_R(z)\le2D+4\operatorname{Re}C_{\rm even}=2Q_R,
\qquad |\sum_Nz_N|^2\le F E_R(z).
\]

With `F<<L`, the complete ledger is therefore

| Input for `Q_R` | Bound for `E_R` | Squared absolute scalar sum | Absolute scalar sum |
|---|---|---|---|
| Universal `O(L^3 X^epsilon)` | `O(L^3 X^epsilon)` | `O(L^4 X^epsilon)` | `O(L^2 X^epsilon)` |
| Target (200.O3), `O(L^2 X^epsilon)` | `O(L^2 X^epsilon)` | `O(L^3 X^epsilon)` | `O(L^(3/2) X^epsilon)` |

The exponent on `X` is renamed after taking a square root, as is valid when the input estimates are available for every positive epsilon. The difference is a factor `L^(1/2)` in the scalar bound, exactly as stated. This is a comparison of proved universal capacity with a desired stronger actual-vector estimate, not an inevitable loss for the actual coefficients.

## 4. First doubtful or unproved step

The finite operator identities, repaired interval control, phase conjugation, and conditional exponent ledger contain no remaining doubtful step.

The first unproved analytic input remains (200.O3) for the **actual** residual coefficient vector. Norm invariance under the displayed phase does not exclude a bound exploiting arithmetic properties of that vector or a different exact transform. This review also does not independently prove the supplied `D<<L^2 X^epsilon` estimate or verify the exact original-source decomposition and coefficient multiplicities; the cited durable kernels defining those were not read in this bounded assignment.

No comparison with a high-`h` block loss or a P2 packet loss can be deduced from the full-line operator calculation alone. The conductor correctly treats those as different interfaces rather than substituting their parameters into this ledger.

## 5. Control tests, repair history, and outcomes

1. **Endpoint repair found and applied.** The initial finite-interval display omitted the positive part. At `R=5`, `M=1`, that initial expression equals `-7/5`, whereas the actual quotient for a one-site vector is one. The reviewer reported this issue. The conductor replaced it by `(1-j/M)_+`, added `M>=R` for the untruncated comparison, and recorded the endpoint control. The reviewer re-read the patched artifact and verified all three changes. The current expression gives one for every one-site vector. Status: green.
2. **Even/odd operator norm.** Direct row-sum summation gives exactly the stated two cases. Long finite intervals approach that row sum. Status: green.
3. **Small `R`.** For `R=1,2`, the kernel is precisely the identity; all even off-diagonal shifts are absent. The norm is one, the correlation is zero, and (R4) has zero loss. Status: green.
4. **Positivity and one real part.** Equation (R1) proves nonnegativity; the two orientations contribute one complex number and its conjugate. No termwise positivity of the arithmetic correlations is assumed. Status: green.
5. **Finite versus infinite vectors.** The constant sequence on all of `Z` is not used as an `ell^2` vector. The proof uses finite intervals and then a limit of quotients. Status: green.
6. **Phased adversarial control.** `D_sigma^*1_I` witnesses the same norm scale for the conjugated operator, but is explicitly not identified with the physical coefficient sequence. Status: green.
7. **Support restriction.** The lower bound is certified for consecutive intervals, not arbitrary sparse support sets. The conductor's current finite-interval statement has this scope. Status: green.
8. **Power and capacity.** The table above preserves both the `O(L)` scalar prefactor and the square root. No lower bound for the actual source is inferred from the all-vector norm. Status: green.
9. **Protected claims.** The reviewed artifact leaves (200.O3), all unsupported arithmetic estimates, and protected parent/exponent claims open. Its assertions about historical sector closure are not independently audited here; they are not used in this finite review. Status: no new promotion.

## 6. Dependencies and exact artifacts used

- Principal reviewed artifact, both original and repaired versions: `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/controls/conductor_complete_source_operator_analysis.md`.
- Retained finite-statement context: `protocol.md` and the same campaign's `briefs/independent_statement_packet.md` and `briefs/blind_interval_operator_rederivation.md`.
- Earlier frozen output whose independent status is preserved: the same campaign's `reports/blind_interval_operator_rederivation.md`. It was not edited in this follow-up.
- Optional sibling reports were not used. No graph, historical coefficient file, strategy review, external theorem source, or numerical computation was consulted.

Only `reviews/independent_operator_review.md` is written by this post-isolation task. The conductor, not this reviewer, made the repair to the principal artifact.

## 7. Recommended state effect

**Final review status: GREEN after repair, with the arithmetic target still OPEN.**

Archive the corrected conductor calculation and this seam review as candidate analytical evidence. As instructed for this analysis round, do not promote these elementary lemmas to the claim graph. No shared-state edit, proof-draft update, or parent/exponent change is recommended.

The useful certified conclusion is precise: the square-root phase does not improve the universal operator norm in the complete `(N,N')` coordinates, while the actual-vector estimate (200.O3) is exactly the additional cancellation needed at this interface. The review task is complete.
