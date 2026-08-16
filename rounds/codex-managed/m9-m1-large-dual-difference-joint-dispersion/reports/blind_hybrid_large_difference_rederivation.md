## 1. Result

Rigorous interface-level no-go.  For every nontrivial large-difference mask, the exact physical/dual interface is a weighted integral of **continuously twisted** physical rows, whereas the inherited reciprocal estimate controls only the untwisted rows.  The exact zero mean removes only the zero residue-frequency, Parseval merely trades the arithmetic modes for an unresolved stationary ambiguity energy, and \(d\)-differencing meets exact modulus self-return at shifts \(u\equiv0\pmod M\).  Thus the packet does not certify a \(B^{-\delta}\) gain or a new target-safe shell while retaining \(Q^{-5/12}\).  This is a no-go for closing the proposed argument from the accepted interfaces, not a counterexample to cancellation for the actual symbol.

The exact survivor therefore remains

\[
 \mathfrak Y_{>D_0}^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{|d|>D_0}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.
\]

The first new estimate that would change this conclusion is a twisted-row or, equivalently, actual stationary ambiguity estimate that is uniform in the continuous twist and still contains the factor \(Q^{-5/12}\).

## 2. Exact statement and hypotheses

Fix the scales (85.1), any one of the three classes (85.2), either orientation, and the exact smooth-principal symbol in (85.4).  Let \(E\subset\{d:|d|>D_0\}\) be finite (in particular, a positive/negative dyadic shell), let \(q_E=1_E\), and put

\[
 \widehat q_E(\theta)=\sum_{d\in\mathbb Z}q_E(d)e(d\theta),
 \qquad
 V_b(d,h)=\sum_n I_b(n+d)\overline{I_b(n)}e_M(hn).
\]

Then the following two representations are exact:

\[
 \mathfrak Y_E
 ={1\over M^2}\sum_{b\asymp B}\sum_{d\in E}
 \sum_{\substack{h\bmod M\\h\ne0}}
 \mathcal C_{M,K}(d,h)V_b(d,h),                                      \tag{R85.1}
\]

and, with

\[
 F_{b,x}(\theta)={1\over M}\sum_n I_b(n)
 e\!\left(n\left({x\over M}-\theta\right)\right),
 \qquad
 U_b(\theta)=\sum_{x\bmod M}^{*}e_M(Kx^{-1})F_{b,x}(\theta),
\]

\[
 \mathfrak Y_E
 =\sum_{b\asymp B}\int_0^1\widehat q_E(\theta)
 \left(
 |U_b(\theta)|^2-\sum_{x\bmod M}^{*}|F_{b,x}(\theta)|^2
 \right)d\theta .                                                   \tag{R85.2}
\]

At \(\theta=0\), (R85.2) is the normalized coherent nonzero-offset physical-row energy identified in (85.13), up to the harmless fixed class permutation and unit phases.  The hypothesis (85.14) consequently controls these \(\theta=0\) rows.  It supplies no estimate for \(F_{b,x}(\theta)\) when \(\theta\ne0\).

For

\[
 N_M(h)=\#\{y\bmod M:(y(y+h),M)=1\},
\]

the exact arithmetic controls are

\[
 \sum_{a\bmod M}|\mathcal C_{M,K}(a,h)|^2=M N_M(h),                  \tag{R85.3}
\]

\[
 \sum_{a\bmod M}\sum_{h\ne0}|\mathcal C_{M,K}(a,h)|^2
 =M\bigl(\varphi(M)^2-\varphi(M)\bigr),                             \tag{R85.4}
\]

and

\[
 \sum_{a\bmod M}\mathcal C_{M,K}(a+u,h)
 \overline{\mathcal C_{M,K}(a,h)}
 =M e_M(uh)\!\sum_{\substack{y\bmod M\\(y(y+h),M)=1}}e_M(uy).     \tag{R85.5}
\]

In particular, (R85.5) equals \(M N_M(h)\) whenever \(u\equiv0\pmod M\).  The conclusion uses only the exact packet identities, finite Fourier orthogonality, and the literal normalizations above; it assumes no coefficientwise square-root bound.

## 3. Proof or derivation

Fourier inversion of (85.10)--(85.12) gives

\[
 A_{M,K,d}(n)=\sum_{h\ne0}\mathcal C_{M,K}(d,h)e_M(hn).
\]

Substitution into (85.4), with \(d\) restricted by \(q_E\), proves (R85.1) and keeps the external factor \(M^{-2}\) exactly once.

For (R85.2), write \(m=n+d\) and use

\[
 q_E(m-n)=\int_0^1\widehat q_E(\theta)e(-(m-n)\theta)d\theta.
\]

The Kloosterman part of (85.5), after expanding its two complete sums, becomes \(|U_b(\theta)|^2\).  The Ramanujan identity

\[
 c_M(m-n)=\sum_{x\bmod M}^{*}e_M((m-n)x)
\]

turns the subtracted term into \(\sum_x^*|F_{b,x}(\theta)|^2\).  This proves (R85.2) with the actual \(I_b\), so entry, interior, exit, and all errors present in that exact factor have not been replaced by arbitrary weights.

The obstruction is now algebraic.  Completing all differences makes \(\widehat q\) the point mass at \(\theta=0\), and (R85.2) returns exactly to the physical rows and (85.14).  A finite dyadic or high-pass mask instead has a nonconstant trigonometric kernel spread over the entire circle.  A pointwise bound at \(\theta=0\) cannot bound its integral against the twisted-row quadratic form.  Applying absolute values after postulating a uniform twisted analogue of (85.14) would give only

\[
 B M^2\bigl(TQ^{-5/24}\bigr)^2
 \asymp {C^3\over TQ^{5/12}},                                      \tag{R85.6}
\]

up to the Fourier-kernel norm, namely the already known whole-offset capacity and no \(B\)-gain.  Exploiting the sign of the kernel would require a genuinely new joint correlation estimate.

Equations (R85.3)--(R85.5) follow directly from (85.12).  In (R85.3), summing over \(a\) forces the two variables \(y\) to agree; their inverse phases then cancel.  Summing \(N_M(h)\) over all \(h\) counts all ordered pairs of units, and the omitted \(h=0\) counts \(\varphi(M)\), proving (R85.4).  The same orthogonality with a shift \(u\) proves (R85.5).  For \(p^\nu\Vert M\), the local count is

\[
 N_{p^\nu}(h)=
 \begin{cases}
 p^{\nu-1}(p-1),&p\mid h,\\
 p^{\nu-1}(p-2),&p\nmid h,
 \end{cases}                                                        \tag{R85.7}
\]

and the count for \(M\) is the product of these local counts.  The local Fourier sum on the right of (R85.5) vanishes unless \(p^{\nu-1}\mid u\); when this divisibility holds it can have size \(p^{\nu-1}(p-1)\) or \(O(p^{\nu-1})\), and at \(p^\nu\mid u\) it is exactly the local count.  This simultaneously retains the prime-power bad modes and gives the squarefree comparison (\(\nu=1\)); it supplies no uniform square-root cancellation.

There is a second exact form of the missing analytic input.  Put

\[
 W_{b,r,d}=\sum_{\ell\in\mathbb Z}
 I_b(r+M\ell+d)\overline{I_b(r+M\ell)}.
\]

Then \(V_b(d,h)=\sum_r e_M(hr)W_{b,r,d}\), so Parseval and (R85.4), for a shell of cardinality \(\asymp D\) with \(D>D_0\gg M\), give only

\[
 |\mathfrak Y_{E,b}|
 \ll \sqrt{D/M}
 \left(\sum_{d\in E}\sum_{r\bmod M}|W_{b,r,d}|^2\right)^{1/2}.     \tag{R85.8}
\]

The trivial ambiguity energy in (R85.8) cancels the apparent Parseval saving exactly.  Neither (85.9) nor the untwisted row estimate (85.14) bounds this \((d,r)\)-energy with the required \(Q^{-5/12}B^{-2\delta}\).

For comparison, even if one additionally grants the shifted-product bounded-variation and large-\(d\) error audit not supplied by the packet, the second-derivative test on \(D<|d|\le2D=o(Q^2)\) yields only the pointwise-dual diagnostic

\[
 \mathfrak Y_E
 \ll_\varepsilon X^\varepsilon
 \left(B^3J^{1/10}D^{3/2}+B^2J^{3/10}D^{1/2}\right).                \tag{R85.9}
\]

The first term reaches the target only for

\[
 D\le J^{13/15}B^{-2}=J^{31/15}C^{-2};                              \tag{R85.10}
\]

at \(C=J^{3/4}\), (R85.10) is exactly \(D_0=J^{17/30}\).  For smaller \(C\) it has slack, but (R85.9) is precisely a fixed-\(d\) estimate summed after discarding \(Q^{-5/24}\); under the round's stated rule it is not a retained physical/dual gain and is not promoted here.

Finally, apply \(d\)-differencing to \(z_d=\sum_{h\ne0}\mathcal C(d,h)V_b(d,h)\), extended by zero outside an interval of length \(N\asymp D\).  For \(1\le U\le N\), the exact van der Corput inequality has prefactor

\[
 {N+U-1\over U}
\left(
 \sum_d|z_d|^2+2\sum_{1\le u<U}(1-u/U)
 \Re\sum_d z_{d+u}\overline{z_d}
\right).                                                           \tag{R85.11}
\]

Thus the diagonal is not removable.  Hypothetically negligible off-diagonals give at most \(U^{-1/2}\).  Taking \(U\le M\asymp B\) gives at most \(B^{-1/2}\), only the \(C\le J^{56/75}\) capacity.  The \(B^{-5/9}\) needed at \(C=J^{3/4}\) would require \(U\asymp B^{10/9}>M\), where (R85.5) necessarily includes the exact self-return shift \(u=M\).  The actual \(V_b\)-correlation could still cancel it, but no such estimate is in the packet.  Differencing an unlocalized range of length \(Q^2\), or covering it by \(D\)-blocks, also retains the corresponding \(Q^2/D\) block/prefactor cost.

## 4. First doubtful or unproved step

The first unavailable step is an estimate for the twisted quadratic form in (R85.2), or equivalently for the actual ambiguity energy/correlations in (R85.8) and (R85.11), that simultaneously

\[
 \text{(i) saves }B^{-\delta},\qquad
 \text{(ii) retains }Q^{-5/12},\qquad
 \text{(iii) is uniform in }\theta,d,b,r,
\]

and includes entry/exit pieces, wrong-sign tails, aggregate stationary errors, modulus-multiple shifts, and integer-derivative resonances.  Estimate (85.14) is only the \(\theta=0\), completely transformed endpoint of this family; (85.9) is only a bounded-variation control and does not supply its \(L^2\) dispersion.  No interpolation between these two facts is justified.  In particular, an arbitrary-weight large sieve, a coefficientwise bound for \(\mathcal C\), or reuse of the Round-84 error statement beyond \(D_0\) would be the first invalid step.

## 5. Required control test and outcome

- **Normalization and target ledger:** The factor \(M^{-2}\) appears in (R85.1) and is absorbed exactly by the two \(M^{-1}\) row normalizations in (R85.2).  The physical capacity is (R85.6).  Relative to \(J^2/T\), its excess is \(C^3/J^{13/6}\).  A genuine \(B^{-\delta}\) would give the endpoint \(C\le J^{(13/6-3\delta/5)/(3-\delta)}\); no such factor was obtained.

- **Classes and orientations:** The derivation uses only \(gM=4b\), \(M\asymp B\), and the exact finite transforms, so it applies to all three classes.  For orientation \(\eta\), replace \(n\) by \(m=\eta n>0\) and \(d\) by \(\eta d\); conjugation/reflection leaves every norm and orthogonality identity unchanged.

- **Small-difference ownership:** Every mask used above is supported on \(|d|>D_0\).  The literal \(d=0\) and \(0<|d|\le D_0\) are neither restored nor subtracted a second time.  Completing \(d\bmod M\) in (R85.3)--(R85.5) is only an arithmetic identity, not permission to replace an actual large \(d\) by its residue.

- **Large, negative, edge, and wraparound differences:** (R85.1)--(R85.2) are exact for both signs and for differences comparable with \(Q^2\), including moving or empty support overlaps.  Since \(I_b(n+d)\) is not periodic in \(d\), arithmetic wraparound \(d\mapsto d+M\) is forbidden.  Formula (R85.9) was explicitly kept diagnostic and restricted to \(D=o(Q^2)\).

- **Ramanujan and modulus-multiple terms:** The Ramanujan subtraction is the full diagonal-row term in (R85.2), not a discarded error.  It removes \(h=0\), not nonzero \(d\equiv0\pmod M\).  Such \(d\), and the shifts \(u\equiv0\pmod M\), remain and give exact self-return in (R85.5).

- **Prime powers and gcd modes:** (R85.7) and the local Fourier condition \(p^{\nu-1}\mid u\) retain every high-gcd prime-power mode.  For squarefree moduli the same formula specializes with \(\nu=1\); this comparison does not license a coefficientwise square-root estimate.

- **Actual symbol, entries/exits, and errors:** The main identities never replace \(I_b\) by a model sequence and hence include the actual stationary symbol and all support edges.  No large-\(d\) stationary error or wrong-sign tail estimate is asserted.  The tempting estimate (R85.9) is labelled conditional precisely because those aggregate controls and the physical saving are absent.

- **Differencing and diagonals:** The full prefactor and diagonal are displayed in (R85.11).  The \(u=M\) correlation is retained, and a full-range localization must also pay its \(Q^2/D\) cost.

- **Perfect-power and integer-derivative resonances:** No Diophantine separation from integral first derivatives is assumed.  Such resonances may concentrate \(W_{b,r,d}\), and fourth-power/perfect-square specializations remain inside (R85.8).  They cannot be deleted by a generic second-derivative or large-sieve slogan.

- **Complete-transform self-return:** Replacing \(q_E\) by the complete difference range concentrates (R85.2) at \(\theta=0\) and returns exactly to (85.13); it yields (85.15), not a new estimate.

- **Downstream scope:** The conclusion concerns only the frozen transition-flattened nonaxial smooth-principal component, fixed \(k\), fixed local class, and its conjugate orientation in (85.1).  It says nothing about raw transition or axis terms, cone edges, other radial sectors, endpoint uniformity beyond the packet, full M9-M1 or M9, or the Gauss-circle exponent.

## 6. Dependencies and exact artifacts used

Only `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/derivation_packet.md` and the task brief `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/briefs/blind_hybrid_large_difference_rederivation.md` were used.  No sibling report, prior-round report, strategy file, proof-state file, source card, web source, or computation was read or used.  All new formulas are elementary consequences of the packet's finite Fourier identities.

## 7. Recommended state effect

**Revise.**  Do not promote a bound and do not change the survivor.  Record the exact obstruction as a new mechanism-level obligation: prove a continuously twisted reciprocal-row/actual ambiguity estimate strong enough to retain \(Q^{-5/12}\) and save \(B^{-\delta}\), with the \(u=M\) self-return, high-gcd prime-power modes, support edges, and resonant phases included.  Absent that estimate, reject dyadic completion, zero-mean Parseval, and \(d\)-differencing as standalone closures of Round 85.
