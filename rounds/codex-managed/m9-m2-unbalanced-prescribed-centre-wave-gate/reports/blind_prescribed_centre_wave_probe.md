# Round 118 statement-only report: prescribed-centre coherent-wave probe

- Campaign: m9-m2-unbalanced-prescribed-centre-wave-gate
- Task: blind_prescribed_centre_wave_probe
- Role: statement-only blind rederiver
- Graph SHA-256 supplied in the brief: d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb
- Status: candidate evidence only

## 1. Result: coherent-sector no-go and exact remaining survivor

The literal exact centre, a half-integer tie, prime/square/fourth-power centres, an affine same-character tangent run, and the full exactly phase-coherent stationary sector all fail to furnish a countermodel larger than \(X^{1/4+\varepsilon}\). The rigorous conclusion is a scoped no-go.

Put
\[
 R={X\over D},\qquad J={X\over D^2}={K\over L},\qquad
 \mu_L=\mathcal Q_L(0)=\int_0^\infty {q_L(h)\over h}\,dh .
\]

In the flat-smooth range of the blind statement:

- The exact central level, and the two tied nearest levels when \(X\in\mathbb Z+1/2\), have total size \(O_\varepsilon(\mu_LX^\varepsilon)\).
- The literal affine tangent construction
  \[
  d_j=d_0+j,\qquad r_j=4m(d_0-j)+\sigma,\qquad \sigma\in\{1,-1\},
  \]
  has constant character \(\chi_4(r_j)=\sigma\), but among products satisfying
  \(\lvert r_jd_j-X\rvert\ll\Delta\) it supplies only
  \[
  O\!\left(1+\sqrt{\Delta/J}\right)
  =O\!\left(1+\sqrt{D^3/(LX)}\right)\ll X^{1/4}.
  \]
- Poisson summation in the odd \(r\)-variable exposes a stationary product wave with \(M=KL\) pairs, coefficient scale \(\sqrt F/M\), phase \(e(\sqrt{Xk\nu})\), and the actual symbol \(\chi_4(\nu)\) on odd \(\nu\asymp L\). If \(X=bA^2\), with \(b\) squarefree, every exactly phase-one pair satisfies \(k\nu=bw^2\). There are
  \[
  O_\varepsilon(\sqrt M\,X^\varepsilon)
  \]
  such pairs, so even their absolute stationary contribution is
  \[
  O_\varepsilon\!\left({\sqrt F\over M}\sqrt M\,X^\varepsilon\right)
  =O_\varepsilon(\sqrt\Delta\,X^\varepsilon)
  =O_\varepsilon(X^{(\delta-\ell)/2+\varepsilon})
  \ll X^{1/4+\varepsilon}.
  \]
  In the worst square case \(b=1\), the unsigned counting capacity is
  \(O(\sqrt M\log(2L))\), still target-safe. For a fixed scaled smooth weight, the actual \(\chi_4\)-weighted square-sector count is \(O(\sqrt M)\): the character removes that possible logarithm.

These facts rule out the listed coherent countermodels. They do not prove the full estimate. After the exactly coherent sector is removed, the smallest stationary survivor is
\[
 \boxed{
 {\sqrt F\over M}
 \sum_{\substack{n\asymp M\\ \sqrt{Xn}\notin\mathbb Z}}
 b_X(n)e(\sqrt{Xn}),\qquad
 b_X(n)=
 \sum_{\substack{\nu\mid n,\ \nu\ {\rm odd}\\
                   \nu\asymp L,\ n/\nu\asymp K}}
 \chi_4(\nu)A_X(n/\nu,\nu), }
\]
where \(A_X\) is the bounded smooth stationary amplitude. Its absolute capacity is \(\asymp\sqrt F\), not \(\sqrt\Delta\), and no target upper bound or countermodel lower bound for it follows from the permitted statement. Equivalently, on the physical side the unresolved object is the full \(\chi_4(r)\)-weighted discrepancy of all product pairs throughout the \(D/L\)-window, not a selected positive sector. Thus (118.B8) remains open, and no strict subrange for the full wave is proved here.

## 2. Exact statement and hypotheses

Use \(e(z)=e^{2\pi iz}\), all conditions in (118.B1), the scales in (118.B2), and the literal definitions (118.B3)--(118.B5). Write the fixed positive support constants as
\[
 \operatorname{supp}q_L\subset[c_qL,C_qL],\qquad
 W(X/(rD))\ne0\Longrightarrow c_WR\le r\le C_WR.
\]

Only these profile properties are used: \(q_L\ge0\), \(\mu_L\ll X^\varepsilon\) (the normalization implicit in (118.B7)), bounded \(W\), rapid Fourier decay at the displayed scale, and the usual uniform scaled derivative bounds when the stationary normal form is invoked. No lower bound for \(q_L\) or \(W\), and no sign assumption on \(W\), is inserted.

The exact assertions are:

- **Kernel core.**
  \[
  |\mathcal Q_L(y)|\le\mu_L,\qquad
  \mathcal Q_L(-y)=\overline{\mathcal Q_L(y)},\qquad
  |\mathcal Q_L(y)-\mu_L|
  \le 2\pi C_qL\mu_L|y|.
  \]
  Hence \(\Re\mathcal Q_L(y)\ge\mu_L/2\) for
  \(|y|\le(6C_qL)^{-1}\). A sufficiently small fixed product core
  \(|rd-X|\le c\Delta\) therefore has positive real kernel, although its arithmetic multiplier still has both signs.
- **Central and tie levels.** If \(X=N\in\mathbb Z\), the level \(rd=N\) is \(O_\varepsilon(\mu_LX^\varepsilon)\). If \(X=N+1/2\), the union of \(rd=N,N+1\) has the same bound. There is no termwise conjugate pairing at a tie because the divisors of \(N\) and \(N+1\) need not coincide.
- **Affine same-residue run.** If \(d_0,m\) are positive integers, \(\sigma=\pm1\), \(r_0=4md_0+\sigma\), and \(X=r_0d_0\), the family in Section 1 has constant character and at most \(O(1+\sqrt{\Delta/m})\) members in the product window. At the active scales \(m\asymp J\).
- **Stationary coherent class.** On a smooth interior partition, odd-\(r\) Poisson summation gives \(\nu>0\), \(\nu\asymp L\), \(k\asymp K\). Each main term is \(O(\sqrt F/M)\). For integer \(X=bA^2\), \(b\) squarefree, the set on which its phase equals one has \(O_\varepsilon(\sqrt M X^\varepsilon)\) elements.
- **Actual-sign square model.** In the worst case \(X=A^2\), write \(k=au^2,\nu=av^2\), with \(a\) odd squarefree and \(v\) odd. Then \(\chi_4(\nu)=\chi_4(a)\). For every fixed compactly supported \(C^1\) weight \(G\),
  \[
  \sum_{\substack{a\ {\rm odd\ squarefree}\\u,v\ge1}}
  \chi_4(a)G\!\left(u\sqrt{a/K},v\sqrt{a/L}\right)
  =O_G(\sqrt M),
  \]
  whereas deleting or adversarially replacing \(\chi_4(a)\) permits
  \(O_G(\sqrt M\log(2L))\). This is a quantified actual-sign saving only on the exactly square-coherent sector.

Sharp, starred, hard, and arithmetic-owner endpoints are excluded from the stationary assertions.

## 3. Proof or derivation

**Kernel and central controls.** Since \(q_L/h\) is a nonnegative measure,
\[
 |\mathcal Q_L(y)|\le\int {q_L(h)\over h}\,dh=\mu_L.
\]
Reality gives the conjugacy identity, and
\[
 |\mathcal Q_L(y)-\mu_L|
 \le2\pi|y|\int q_L(h)\,dh
 \le2\pi C_qL\mu_L|y|.
\]
The cosine is at least \(1/2\) on the stated core. On the support of \(W\), \(r/X\asymp D^{-1}\), so
\[
 L\left|{r(rd-X)\over4X}\right|\ll {|rd-X|\over\Delta}.
\]
This transfers the kernel core to a fixed physical subwindow. At \(X=N\), the exact products are indexed by divisors of \(N\), giving
\(\mu_L\|W\|_\infty\tau(N)\). Applying the same bound separately to \(N\) and \(N+1\) proves the tie assertion.

**Exact product/reciprocal-row equivalence.** Extend the \(d\)-sum to all integers; the added \(d\le0\) terms are rapidly negligible on the active positive supports. Substitution of (118.B3) and Dirac-comb Poisson summation give
\[
 \begin{aligned}
 \sum_{d\in\mathbb Z}
 \mathcal Q_L\!\left({r(X-rd)\over4X}\right)
 &=\int {q_L(h)\over h}e(hr/4)
       \sum_{d\in\mathbb Z}e\!\left(-{hr^2d\over4X}\right)dh\\
 &={4X\over r^2}\sum_{k\ge1}
   {q_L(4Xk/r^2)\over 4Xk/r^2}
   e\!\left({Xk\over r}\right)\\
 &=\sum_{k\ge1}{q_L(4Xk/r^2)\over k}e(Xk/r).
 \end{aligned}
\]
This proves the stated equivalence and shows why absolute values cannot be moved through this transform.

**Exact affine coherent-run test.** Put \(r_0=4md_0+\sigma\), \(X=r_0d_0\). Then
\[
 r_jd_j-X=(r_0-4mj)(d_0+j)-r_0d_0
 =\sigma j-4mj^2.
\]
All \(r_j\equiv\sigma\pmod4\), so \(\chi_4(r_j)=\sigma\). For \(|j|\ge1\),
\[
 |\sigma j-4mj^2|\ge(4m-1)j^2.
\]
Thus the product window forces \(|j|\ll1+\sqrt{\Delta/m}\). If \(d_0\asymp D,r_0\asymp R\), then \(m\asymp X/D^2=J\). More precisely,
\[
 \sqrt{\Delta/J}=X^{(3\delta-\ell-1)/2},\qquad
 {\sqrt{\Delta/J}\over X^{1/4}}
 =X^{-\{3(1/2-\delta)+\ell\}/2}<1.
\]
The run is target-safe for either sign. Its unselected complement still has physical absolute capacity \(O_\varepsilon(\Delta X^\varepsilon)\), so the run cannot lower-bound the full wave.

**Odd-character Poisson transform.** For smooth \(f\) supported on positive \(r\), write \(r=2n+1\) and use \(\chi_4(2n+1)=(-1)^n\):
\[
 \sum_{r\ {\rm odd}}\chi_4(r)f(r)
 ={1\over2}\sum_{\nu\in2\mathbb Z+1}
 e(-\nu/4)\int_0^\infty f(r)e(\nu r/4)\,dr.
\]
For reciprocal row \(k\), the phase is
\[
 \Phi_{k,\nu}(r)={Xk\over r}+{\nu r\over4}.
\]
Its positive stationary point and values are
\[
 r_{k,\nu}=2\sqrt{Xk/\nu},\qquad
 {4Xk\over r_{k,\nu}^2}=\nu,\qquad
 \Phi_{k,\nu}(r_{k,\nu})=\sqrt{Xk\nu},\qquad
 \Phi''_{k,\nu}(r_{k,\nu})={\nu\over2r_{k,\nu}}.
\]
Consequently \(q_L\) forces \(\nu\asymp L\), \(W\) forces \(r_{k,\nu}\asymp R\), and \(k\asymp K\). The leading term is
\[
 e(-1/8)\chi_4(\nu)
 {q_L(\nu)\over k}
 W\!\left({\sqrt{X\nu}\over2D\sqrt k}\right)
 \sqrt{{r_{k,\nu}\over2\nu}}\,
 e(\sqrt{Xk\nu}).
\]
Here
\(e(-\nu/4)e(1/8)=e(-1/8)\chi_4(\nu)\) for odd \(\nu\). Thus the actual character survives and is not a completed \(r_2/4\) coefficient. There are \(M=KL\) stationary pairs; each has scale
\[
 {1\over K}\sqrt{R/L}={\sqrt F\over M}.
\]
The full stationary absolute capacity is therefore \(\sqrt F\).

**Exactly coherent arithmetic families.** If \(X=bA^2\), \(b\) squarefree, phase one implies \(k\nu=bw^2\). Since \(k\nu\asymp M\), there are \(O(\sqrt{M/b})\) choices of \(w\), and each product has \(O_\varepsilon(X^\varepsilon)\) divisors. Hence
\[
 \#\{(k,\nu):k\asymp K,\nu\asymp L,\nu\ {\rm odd},k\nu=bw^2\}
 \ll_\varepsilon\sqrt M X^\varepsilon.
\]
This includes divisor-rich \(b\). When \(b=1\), uniqueness of the squarefree kernel gives
\[
 k=au^2,\qquad \nu=av^2,\qquad a\ {\rm odd\ squarefree},\ v\ {\rm odd}.
\]
Since \(K/L=J>1\), summing
\((\sqrt{K/a}+1)(\sqrt{L/a}+1)\) over \(a\ll L\) gives
\(O(\sqrt M\log(2L))\), proving the unsigned bound.

For the actual sign, \(\chi_4(\nu)=\chi_4(a)\). A two-dimensional Euler estimate gives, for each \(a\),
\[
 \sum_{u,v}G\!\left(u\sqrt{a/K},v\sqrt{a/L}\right)
 =c_G{\sqrt M\over a}
 +O_G\!\left(\sqrt{K/a}+\sqrt{L/a}+1\right).
\]
Moreover,
\[
 \sum_{\substack{a\le A\\a\ {\rm odd}}}
 {\mu^2(a)\chi_4(a)\over a}=O(1).
\]
Indeed, \(\mu^2(a)=\sum_{d^2\mid a}\mu(d)\) rewrites this as
\[
 \sum_{\substack{d\le\sqrt A\\d\ {\rm odd}}}{\mu(d)\over d^2}
 \sum_{m\le A/d^2}{\chi_4(m)\over m},
\]
whose inner sums are uniformly bounded and whose outer sum is absolutely convergent. The Euler errors total
\[
 O(\sqrt K\sqrt L+\sqrt L\sqrt L+L)=O(\sqrt M).
\]
This proves the \(O_G(\sqrt M)\) actual-sign bound. Multiplication by \(\sqrt F/M\) gives \(O_G(\sqrt\Delta)\). This controls the entire exactly square-coherent sector, including both signs, but not its nonsquare complement.

**The exact obstruction.** Grouping the remaining stationary terms by \(n=k\nu\) gives the survivor in Section 1. Its trivial absolute bound is \(\sqrt F\), since it retains essentially all \(M\) pairs. A positive square sector of size \(O(\sqrt\Delta X^\varepsilon)\) can be canceled or overwhelmed by that complement. Conversely, adversarial phases of the same magnitudes can align a nonvanishing interior profile box and realize \(\sqrt F\) capacity. Thus neither an actual-sign lower bound nor (118.B8) follows without a new estimate for the full signed survivor.

## 4. First doubtful or unproved step

The first genuinely unproved step is
\[
 {\sqrt F\over M}
 \sum_{\substack{n\asymp M\\ \sqrt{Xn}\notin\mathbb Z}}
 b_X(n)e(\sqrt{Xn})
 \stackrel{?}{\ll}_\varepsilon X^{1/4+\varepsilon},
\]
uniformly throughout (118.B1), or any reverse inequality large enough to refute it. The coefficient \(b_X(n)\) is a truncated, smoothly weighted divisor sum with \(\chi_4\) only on the odd complementary divisor. It cannot be replaced by \(r_2(n)/4\), its absolute value, or a selected sign class. The exact-square calculation controls only \(O(\sqrt M X^\varepsilon)\) of the \(M\) stationary pairs; the signed nonsquare complement remains uncontrolled.

On the physical side this is precisely cancellation in
\[
 \sum_{\substack{r\ {\rm odd},\ d\ge1\\|rd-X|\ll\Delta X^\varepsilon}}
 \chi_4(r)W(X/(rD))
 \mathcal Q_L\!\left({r(X-rd)\over4X}\right),
\]
including every sign and near-centre shell. Positivity of the small kernel core does not control that complement. A secondary audit is needed before using the stationary leading term at a profile endpoint because the blind statement does not spell out the literal scaled derivative constants; the exact physical no-go and exact Poisson identities do not depend on that audit.

## 5. Control tests and outcomes

| Required control | Exact input and expected invariant/failure | Outcome | Implication |
|---|---|---|---|
| literal_wave_and_physical_normalization | Use (118.B3)--(118.B5), retaining \(\mu_L,W(X/(rD)),\chi_4(r)\); expect no complete-divisor replacement. | Passed analytically; all literal factors remain. | Conclusions concern only the prescribed-centre truncated wave. |
| product_and_reciprocal_row_equivalence | Poisson-sum \(d\) with \(h>0\); expect \(h=4Xk/r^2\), \(1/k\), and \(e(Xk/r)\). | Passed by the displayed Dirac-comb calculation. | The forms are equivalent, but the identity gives no estimate. |
| exact_centre_and_tie | Test \(X=N\) and \(X=N+1/2\); expect divisor bounds and no automatic tie conjugacy. | Both give \(O_\varepsilon(\mu_LX^\varepsilon)\). | Neither falsifies the target. |
| near_centre_kernel_sign | Use \(q_L\ge0\) and \(|rd-X|\le c\Delta\); expect positive real kernel only on a small core. | \(\Re\mathcal Q_L\ge\mu_L/2\) there; the kernel is not globally nonnegative. | Kernel positivity neither removes \(\chi_4\) nor controls outer shells. |
| prime_square_fourth_power_divisor_rich | Test prime \(X,p^2,p^4\), divisor-rich squarefree part \(b\), and prime/square/fourth-power \(\nu\). | Exact centres are bounded by \(\tau(X)\). If \(X=bA^2\), phase-one pairs are \(O_\varepsilon(\sqrt{M/b}X^\varepsilon)\). For \(X=A^2\), prime \(\nu=p\) forces \(k=pu^2\) and has either sign according to \(p\bmod4\); square/fourth-power \(\nu\) is positive but remains in the \(O(\sqrt M X^\varepsilon)\) class. | Prime powers and divisor richness create no power-sized countermodel; both prime signs occur. |
| coherent_run_selector_and_complement | Use \(r_j=4m(d_0-j)+\sigma,d_j=d_0+j\); expect constant character and quadratic drift, while retaining unselected pairs. | The run has \(O(1+\sqrt{\Delta/J})\) terms; its complement has capacity \(O_\varepsilon(\Delta X^\varepsilon)\). | The run is target-safe and is not a lower bound. |
| character_residue_and_both_signs | Test \(\sigma=\pm1\), primes \(1,3\bmod4\), and odd-\(r\) Poisson. | Both tangent signs occur; Poisson transfers the exact symbol to \(\chi_4(\nu)\). | No sign may be dropped and no \(r_2/4\) completion is valid. |
| profile_support_and_endpoint_kernels | Retain the taper, smooth \(q_L,W\), \(L=1\), and profile edges; expect only smooth interior stationary phase. | Interior passes; \(L=1\) leaves \(O(1)\) stationary odd indices. Sharp/starred/hard and arithmetic-owner endpoints are not claimed. | The no-go does not cross excluded endpoints. |
| capacity_before_after_each_norm | Compare physical, reciprocal-row, stationary, and coherent capacities. | Physical: \(\Delta\). Reciprocal raw \(\ell^1\): \(RK/K=R\). Stationary raw \(\ell^1\): \(M(\sqrt F/M)=\sqrt F\). Exactly coherent: \(\sqrt M(\sqrt F/M)=\sqrt\Delta\), up to \(X^\varepsilon\). | Absolute values do not commute with the transforms; only the coherent class is automatically target-safe. |
| actual_symbol_vs_unsigned_adversary | Compare actual \(\chi_4\), absolute values, random signs, and adversarial phases. | On the square sector actual sign gives \(O(\sqrt M)\), unsigned/adversarial counting permits \(O(\sqrt M\log L)\). On the full box adversarial phases can align \(\sqrt F\); random signs prove nothing. | Actual arithmetic is essential on the unresolved complement. |
| strict_residual_exponent_region | Use all of (118.B1), including \(178\ell+1638\delta>463\). | Unsigned physical capacity is super-target since \(\delta-\ell>1/4\); coherent capacity is target-safe since \((\delta-\ell)/2<1/4\). The linear inequality is not needed for this no-go. | The no-go holds throughout the strict residual region, but no full-wave subrange follows. |
| downstream_scope | Test whether the work proves (118.B8), transfers an earlier exponent, covers endpoints, or closes M9-M2. | It does none; it only falsifies the listed coherent mechanisms and isolates a survivor. | Keep the downstream obligation open. |

No numerical or web control was used; all outcomes are algebraic or analytic.

## 6. Dependencies and exact artifacts used

Only these artifacts were read or used:

- protocol.md
- problems/gauss_circle.md
- state/control_models.md
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/blind_statement.md
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/briefs/blind_prescribed_centre_wave_probe.md

No proof-state file, strategy file, Round-107 or Round-117 report/review, Round-118 derivation packet, conductor candidate, sibling report, computation, or external source was used. The product/row identity depends only on the accepted positive-support extension in the blind packet. The stationary main-term description additionally uses ordinary scaled smoothness of the flat profiles; endpoint promotion would require the omitted derivative/kernel audit.

## 7. Recommended state effect

**Revise; no graph promotion.** Reject any proposed countermodel whose lower bound comes only from the exact centre, a half-integer tie, a selected positive near-centre sector, an affine same-residue tangent run, primes/squares/fourth powers, divisor richness, or the phase-one stationary square class. Each is divisor-bounded, \(O(\sqrt\Delta X^\varepsilon)\), or lacks control of a complement with much larger capacity.

Retain (118.B8) as open. The useful obstruction is the precise requirement to control the full off-square actual-sign survivor \(b_X(n)e(\sqrt{Xn})\), with smooth truncated divisor coefficient \(b_X\), rather than any positive coherent subset. The \(O(\sqrt M)\) versus \(O(\sqrt M\log L)\) calculation may be retained as an actual-sign saving confined to the exact-square coherent sector.
