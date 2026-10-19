# Round 231: independent review of complete target-A restoration

- Campaign: `gc-actual-upper-tail-a`; task: `independent_complete_restoration`.
- Role: independent nonauthor reviewer, following the completed and frozen statement-only odd-kernel task.
- Generated: `2026-10-11T15:21:08Z`.
- Supplied graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; graph not inspected in this review.
- Reviewed claimant: `candidates/conductor_tail_restoration.md`, SHA-256 `792af94bcaa73cff66e837f5382eef9baf96d6e51171954f70229dbb168c36d3`.
- Status: conditional restoration passes with the mandatory localized convention repair now verified in the conductor's repair attachment. The target itself remains open.
- Effort: analytical/algebraic, with only a bounded exact-decimal integer-square check; no numerical evidence is used to prove an asymptotic claim.

## 1. Result: pass with one explicit repair

Both target-A tail integrations, the low-amplitude and threshold-boundary payments, the actual-family ceiling inference, the full complementary restoration, and the finite character-pair identities are correct under the supplied reviewed inputs.

**Required repair in claimant section 3A:** replace

\[
 \theta=(1+\beta)/4
\]

by

\[
 \boxed{\theta=\tfrac14+\tfrac12\beta=(1+2\beta)/4.}
\]

The accepted kernel defines \(\beta=2\theta-1/2\). The claimant's displayed expression is therefore incorrect. This correction leaves the tail ledger, the complete moment exponent \(32/25\), the derived pointwise exponent \(207/650\), and the conclusion that this pointwise consequence is weaker than the accepted benchmark unchanged.

The original claimant remains frozen. The subsequently supplied `candidates/conductor_seam_repairs.md` correctly records this repair and governs its use. Its equivalent radical expression `(3292+25sqrt(1717))/13762` is also correct. No arithmetic tail saving or complete new moment bound has been proved by the conditional implication itself.

## 2. Exact statement and hypotheses audited

Use the fixed actual mollifier, real radial Fourier factor \(\Psi\), nonnegative window \(w\), real \(T\ge2\), and unnormalized measure

\[
 d\mu(R)=w(R/T)\,dR,
 \qquad \mu(\mathbb R)\ll T
\]

from `briefs/actual_interface.md`. Set

\[
 \gamma=16/125,
 \quad b=32/25,
 \quad q=136/13,
 \quad \alpha=1/100,
 \quad V_0=T^\gamma,
 \quad \beta=\frac{50\sqrt{1717}-297}{13762}.
\]

The actual radius-independent finite band is

\[
 F(R)=\sum_n[\eta(n/X)-\eta(n/Y)]r_2(n)n^{-3/4}
          \Psi(\sqrt{n/T})\cos(2\pi R\sqrt n-3\pi/4),
\]

with \(X=T^{64/125}\), \(Y=T^{93/125}\). The inherited inputs are:

1. The coefficient-uniform distribution bound
   \(D_F(V)\ll_\zeta T^\zeta(V^{-2}+TV^{-q})\) for \(V\ge1\).
2. The independently proved actual complete ceiling
   \(\|B\|_\infty\ll_\delta T^{\beta+\delta}\).
3. The exact identity \(B=L+F+H\), independently proved ceilings
   \(\|L\|_\infty,\|H\|_\infty\ll_\delta T^{\gamma+\delta}\), and complete complementary moments at \(T^{b+\varepsilon}\). Here \(H\) includes the entire infinite norm tail.
4. If the optional \(F=C+U\) representation is used, the supplied separately paid complete moment of \(U\) is also retained.

The proposed additional hypothesis is either

\[
 D_F(V)\ll_\zeta T^\zeta[T^{-\alpha}V^{-2}+TV^{-q}]
       \quad(V\ge V_0)
 \tag{2.1}
\]

for every \(\zeta>0\), or directly

\[
 12\int_{V_0}^{\infty}V^{11}D_F(V)\,dV
       \ll_\varepsilon T^{b+\varepsilon}.
 \tag{2.2}
\]

The conclusion audited is the conditional complete bound
\(M_{12}(B)\ll_\varepsilon T^{b+\varepsilon}\). Neither hypothesis (2.1) nor (2.2) is asserted as established.

For the finite arithmetic identities, \(h,h'>0\), \(g=\gcd(h,h')\), \(h=ga\), \(h'=gb\), \((a,b)=1\), and \(q_1,q_2\) are odd integers. In this review the subscripts distinguish these odd labels from the tail exponent \(q=136/13\). Let \(r=aq_1-bq_2\).

## 3. Independent derivation and seam audit

### Low amplitudes and the threshold boundary: pass

The exact layer-cake identity is

\[
 M_{12}(F)=12\int_0^\infty V^{11}D_F(V)\,dV.
\]

Below \(1\), the contribution is at most \(O(T)\). Between \(1\) and \(V_0\), the inherited generic bound gives

\[
 \begin{aligned}
 12\int_1^{V_0}V^{11}D_F(V)\,dV
 &\ll T^\zeta\left[
   \frac65(V_0^{10}-1)
    +\frac{39}{5}T(V_0^{20/13}-1)\right].
 \end{aligned}
 \tag{3.1}
\]

Indeed \(11-q=7/13\), so its integral has exponent \(20/13\), not \(7/13\). The three resulting exponents are

\[
 1,\qquad 10\gamma=32/25,\qquad
 1+20\gamma/13=389/325<416/325=32/25.
 \tag{3.2}
\]

If one uses a truncated event moment instead of the layer-cake upper integral, the exact identity is

\[
 \int |F|^{12}\mathbf1_{|F|>V_0}\,d\mu
 =V_0^{12}D_F(V_0)
    +12\int_{V_0}^\infty V^{11}D_F(V)\,dV.
 \tag{3.3}
\]

The generic bound pays its boundary term by
\(T^\zeta[V_0^{10}+TV_0^{20/13}]\), hence the same budget. The claimant correctly does not discard it. The strict inequality in the definition of \(D_F\) causes no issue in either identity.

### Actual ceiling provenance: pass at the supplied inherited scope

The complete actual \(B\) ceiling comes from the accepted kernel's section 6: sharp discrepancy, its exact smoothing reconstruction, and the convention \(\beta=2\theta-1/2\). The low and high complementary ceilings have independent provenance in `conductor_combined_owner.md`. Since \(\gamma<\beta\), their exact physical-space identity yields

\[
 \|F\|_\infty\le\|B\|_\infty+\|L\|_\infty+\|H\|_\infty
 \le C_\delta T^{\beta+\delta}=:W.
 \tag{3.4}
\]

This is a valid ceiling for this \(F\). It does not assert that the complete \(B\) ceiling survives arbitrary masking. The finite coefficient-uniform distribution applies independently because these coefficients are fixed as \(R\) varies and are divisor bounded. Infinite complementary vectors are treated by the accepted Schwartz-tail truncation and full recombination argument.

The inherited smooth high-norm estimate is used here as the explicitly supplied reviewed input. This bounded review does not reopen its historical proof or certify unseen source reports.

### Both upper tails and epsilon margins: pass

When \(W\le V_0\), the upper integral is zero. Otherwise target A gives the exact upper-integral bound

\[
 \begin{aligned}
 12\int_{V_0}^W V^{11}D_F(V)\,dV
 \ll T^\zeta\bigg[&\frac65T^{-\alpha}(W^{10}-V_0^{10})\\
                  &+\frac{39}{5}T(W^{20/13}-V_0^{20/13})\bigg].
 \end{aligned}
 \tag{3.5}
\]

Thus the two exponents before internal losses are

\[
 e_1=10\beta-1/100=1.279663519481228\ldots,
 \qquad
 e_2=1+20\beta/13=1.198409772227881\ldots.
 \tag{3.6}
\]

Both are below \(b=1.28\). This can be certified without trusting the printed decimals. Squaring positive quantities in the exact expression for \(\beta\) verifies

\[
 \frac{128966}{10^6}<\beta<\frac{128967}{10^6}.
\]

Consequently

\[
 b-e_1>\frac{33}{100000}=0.00033,
 \qquad
 b-e_2>0.08158.
 \tag{3.7}
\]

For example, given the requested output \(\varepsilon>0\), take
\(\delta=\varepsilon/40\) in (3.4) and
\(\zeta=\varepsilon/4\) in the distribution estimates. The first tail gains at most
\(10\delta+\zeta=\varepsilon/2\); the second gains at most
\((20/13)\delta+\zeta<\varepsilon/2\). The low contribution gains only \(\zeta\). The constants \(C_\delta^{10}\), \(C_\delta^{20/13}\), and distribution constants are allowed to depend on \(\varepsilon\). This explicitly validates the epsilon renaming. Smaller fixed internal losses can also be chosen if the exponents are to remain strictly below \(b\) before the final epsilon is added.

The minimum first-tail saving is exactly \(10\beta-b\), and the proposed \(1/100\) exceeds it by
\(1.29-10\beta=0.000336480518771\ldots>0\). Thus the small first-tail margin is real, though it is not an estimate for the actual tail. Hypothesis (2.1) implies (2.2); hypothesis (2.2) alone also suffices after (3.1).

### Complete complements and sharp reconstruction: pass with the theta repair

The cutoff algebra is exact:

\[
 (1-\eta(n/X))+[\eta(n/X)-\eta(n/Y)]+\eta(n/Y)=1.
\]

It owns both smooth transitions and every norm. In particular \(H\) is not truncated at its first dyadic block or at a finite upper scale. For large \(T\), the transition ranges separate; bounded \(T\) is absorbed into constants. The inherited ledger pays the complete \(L^{12}\) norms of \(L,H\), and, when used, \(U\). The finite norm inequality or
\(|x_1+\cdots+x_k|^{12}\le k^{11}\sum|x_i|^{12}\)
therefore restores the full moment without discarding mixed terms.

The claimant correctly distinguishes this moment restoration from literal transfer of the tail estimate at \(V_0\). A remainder of size \(T^{\gamma+\delta}\) need not be at most \(V_0/2\), so such distribution transfer would require a separate threshold argument.

For clarity, the accepted reconstruction gives, with \(Y=T^2\),

\[
 \int_{Y/2}^{3Y}|P(x)|^{12}\,dx
 \ll T^7M_{12}(B)+T^{8+\varepsilon}.
 \tag{3.8}
\]

Here \(T^6\) comes from the twelfth power of \(\sqrt R\), \(T\) from the Jacobian, and the second term retains the smoothing error. Thus a complete exponent \(b\) gives sharp moment exponent
\(\max(4,(7+b)/2)\). At \(b=32/25\), this is \(207/50\); the accepted persistence/pointwise bridge gives \(207/650\).

The correct accepted benchmark is

\[
 \theta=\frac14+\frac\beta2=0.314483175974\ldots.
 \tag{3.9}
\]

The inherited bound \(\theta<131/416\) alone proves
\(\theta<207/650\), since \(207\cdot416-131\cdot650=962>0\). Therefore the pointwise conclusion remains weaker than the accepted benchmark. The formula \((1+\beta)/4\) in the claimant must nevertheless be repaired; it mixes the beta convention and cannot remain part of a reviewed statement.

### Character-pair and real-phase algebra: pass

If \(a,b\) are both odd, then \(r\) is even. Multiplying
\(aq_1-bq_2=r\) by \(aq_1\) modulo four gives

\[
 1-abq_1q_2\equiv r aq_1\equiv r\pmod4.
\]

For odd integers the character takes values \(\pm1\), so

\[
 \chi_4(q_1)\chi_4(q_2)=\chi_4(ab)(-1)^{r/2}.
 \tag{3.10}
\]

At \(r=0\), coprimality gives \(q_1=bk,q_2=ak\), and their oddness gives odd \(k\). The pair sign is \(\chi_4(ab)\), including negative odd labels if allowed. This is a character identity, not a sign determination of the weighted covariance or of a high moment.

If \(a,b\) have different parity, \(r\) is odd. All integer solutions form
\((q_1,q_2)=(q_{1,0}+bs,q_{2,0}+as)\); preserving oddness of both entries forces \(s\) even. On the resulting progression with \(s=2j\),

\[
 \chi_4(q_{1,0}+2bj)\chi_4(q_{2,0}+2aj)
 =\chi_4(q_{1,0})\chi_4(q_{2,0})(-1)^{(a+b)j}.
\]

Since \(a+b\) is odd, this alternates. For a finitely supported sequence \(c_j\), summation by parts gives the stated bound by an endpoint supremum plus discrete total variation. It does not bound that variation for an actual restricted progression, and says nothing comparable for the same-two-adic sector.

The complete-product identity is exactly
\(\sum_{hq=p,\ q\text{ odd}}\chi_4(q)=\sum_{q\mid p}\chi_4(q)=r_2(p)/4\)
for positive \(p\), with positive factorizations. It requires all factor pairs and unit weights. It cannot erase the actual cutoff and smooth-amplitude weights.

Finally, for odd \(q_1\),
\(\chi_4(d)e(q_1d/4)=i\chi_4(q_1)\mathbf1_{d\text{ odd}}\).
The stationary factor \(e(-1/8)\) combined with the original \(e(-3/8)\) equals \(-1\). Writing \(R^2=hq_1+\Delta\), the real leading term is therefore

\[
 -\Re\left[i\chi_4(q_1)\sum_{d\text{ odd}}b_h(d)
                  e(\Delta d/(4h))\right]
 =\chi_4(q_1)\sum_{d\text{ odd}}b_h(d)
                  \sin(\pi\Delta d/(2h)).
 \tag{3.11}
\]

This confirms the sign, the exact-resonance zero, and the need to retain physical detuning. The corrected single-fibre example is only a single-fibre control. The negative cosine branch is conjugate; repeated \(q_1\) descriptions require unique ownership or an explicit partition. The claimant preserves these scopes.

## 4. First doubtful or unproved step

The first genuinely unproved analytic premise is the actual-family upper-tail estimate (2.1), or the integrated substitute (2.2). None of the audited character formulas, exact-resonance cancellations, or the previously isolated odd-kernel signed-mean identities supplies it.

The only definite error found in the restoration claimant is its displayed conversion between \(\theta\) and \(\beta\). It is repaired by (3.9), with no other exponent changed. The subsequently read conductor repair attachment records exactly this correction against the frozen claimant, so this repair condition is satisfied.

The historical high-norm and optional factor-owner estimates were audited as supplied reviewed dependencies, not reconstructed from their unprovided source reports. The claimant's counts of computational controls were not independently rerun in this task; the algebra and exponent implications were independently proved above.

## 5. Controls and outcomes

| Seam | Outcome | Evidence and scope |
|---|---|---|
| Both tail integrations | PASS | Exact antiderivatives in (3.1), (3.5); both powers retained. |
| Threshold boundary | PASS | Exact event identity (3.3), paid by the generic tail. |
| Actual ceiling | PASS | Exact \(B-L-H\) inference using independent complementary ceilings; no arbitrary-mask ceiling. |
| Epsilon margins | PASS | Explicit input losses and positive rational margins in (3.7). |
| Infinite complements and transitions | PASS | Cutoff identity and full norm inequality; infinite \(H\) retained. |
| Pointwise consequence | PASS AFTER REPAIR | Conductor attachment replaces \(\theta=(1+\beta)/4\) by \((1+2\beta)/4\); weaker-pointwise conclusion unchanged. |
| Same and mixed two-adic sectors | PASS | Independent modular proof and complete odd-solution progression. |
| Real phase and ownership | PASS | Equation (3.11), exact-resonance zero, detuning and conjugacy correctly scoped. |
| Arithmetic target/no-go scope | PASS | No implication from generic countercontrols to actual arithmetic lower bounds. |
| Prior blind isolation | PASS | Initial report rehashed unchanged before this authorized context expansion. |

The sole bounded arithmetic check evaluated, with exact decimal-integer arithmetic,

\[
 (13762\cdot128966+297\cdot10^6)^2
 <2500\cdot1717\cdot10^{12}
 <(13762\cdot128967+297\cdot10^6)^2.
\]

Both inequalities returned true. This certifies only the stated rational enclosure and is diagnostic support for the algebra, not evidence for the open tail hypothesis.

## 6. Dependencies, reviewed hashes, and isolation provenance

The new review role was explicitly assigned only after the isolated report had been written and frozen. The following newly authorized files were read and hashed:

1. `rounds/codex-managed/gc-actual-upper-tail-a/candidates/conductor_tail_restoration.md`: `792af94bcaa73cff66e837f5382eef9baf96d6e51171954f70229dbb168c36d3`.
2. `rounds/codex-managed/gc-actual-upper-tail-a/briefs/actual_interface.md`: `8eaa7c1e67f5b1c5f6e1340abc5861756e3bfea54c9e1f1d0c96d1fbb90e23d7`.
3. `strategy/round231_balanced_cancellation/conductor_combined_owner.md`: `9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b`.
4. `strategy/round231_balanced_cancellation/conductor_seam_repairs.md`: `e4dc22c726eb241e24a4e7c485202ea6b6b567ecc4e16a3708d435ddc82eab14`.
5. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`: `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
6. `rounds/codex-managed/gc-actual-upper-tail-a/candidates/conductor_seam_repairs.md`, explicitly authorized in a closing follow-up: `c3877cea77e37a11b2919a35a0f692230432a19f912c09737f543600bdc863cd`. Its theta correction and unchanged consequences were verified; its additional detuning-control run counts were not independently rerun and are not used as proof here.

The previously isolated report
`rounds/codex-managed/gc-actual-upper-tail-a/reports/blind_odd_kernel_covariance.md`
was checked by hash only and remains
`b4333428aee065f580ee3adae0a4b6a6ef952c9be115eb8638fa926f130de810`.
Its original three-file context restriction and freeze preceded all expanded-context reading. The present review does not retroactively describe itself as statement-only.

Earlier context comprised `protocol.md`, the isolated statement and the original task brief, as already documented in that frozen report. No graph, synthesis, additional sibling report, external source, or control-code file was read for this review. Only this assigned review path was written. The claimant and initial blind report were not edited.

## 7. Recommended state effect

**Retain** the frozen claimant under the now-verified explicit theta/beta convention repair attachment. **Retain** the corrected conditional complete-restoration implication and the finite arithmetic identities as reviewed round evidence.

**No promotion** of target A, its integrated alternative, complete moment \(32/25\), or any new pointwise estimate follows. The actual signed high-tail premise remains open. No graph, proof-draft, or shared-state mutation is recommended on this bounded review alone. The assigned review ends here; no successor round is initiated.
