# M1 terminal arithmetic attack

- Campaign: `m9-m1-frequency-phase-diagram`
- Round: 10
- Task: `m1_terminal_arithmetic_attack`
- Role: analytic mechanism attacker
- Status: candidate evidence only; no shared state was edited

## 1. Result

The terminal M1 frequency block is pointwise target-sized.  The useful
mechanism is to sum the actual Vaaler frequency first and then group spatial
integers by the nearby product integer.  The spatial character is retained,
although the resulting terminal estimate is strong enough to bound its two
additive-quarter components separately.

Let

\[
 \mathcal B_{1,L}(D;X)=
 \sum_h u_{L,H}(h)
 \sum_{d\in\mathcal D_D}
 a_d e(hX/d),
 \qquad a_d=\chi _4(d)w_D(d),
 \tag{1.1}
\]

where \(\mathcal D_D\) is any set of integers in a fixed shell
\([cD,CD]\), possibly truncated by \(d\le y=\lfloor\sqrt X\rfloor\),
\(|w_D(d)|\le C_w\), and

\[
 \|u_{L,H}\|_\infty+
 \sum_h|u_{L,H}(h+1)-u_{L,H}(h)|\ll L^{-1}.
 \tag{1.2}
\]

Then, uniformly for real \(X\ge2\), \(1\le L\le D\le X^{1/2}\),

\[
 \boxed{
 |\mathcal B_{1,L}(D;X)|
 \ll_{\varepsilon,c,C,C_w}X^\varepsilon
 \left(1+\frac DL\right).}
 \tag{1.3}
\]

For the actual positive M1 coefficient,

\[
 -4\alpha_{h,H}=-\frac{2i}{\pi}
 \frac{\Phi(h/(H+1))}{h}\qquad(h>0),
 \tag{1.4}
\]

a fixed dyadic cutoff in \(h\asymp L\), including truncation at \(h=H\),
satisfies (1.2).  Consequently, if

\[
 H=H_D\asymp DX^{-1/4},\qquad L\asymp H_D,
 \tag{1.5}
\]

then the actual positive and negative terminal blocks satisfy

\[
 \boxed{
 \mathcal M_{1,L}(D;X)\ll_\varepsilon X^{1/4+\varepsilon}}
 \tag{1.6}
\]

for every active \(X^{1/4}\le D\le X^{1/2}\), including the hard spatial
endpoint \(D\asymp\sqrt X\).

At the hard endpoint, the accepted one-sided M1 transform then implies the
same target estimate for the **terminal \(h\)-shell** of the actual signed
product-phase cone.  This does not estimate the lower \(h\)-shells of the
full endpoint cone.

## 2. Exact hypotheses and coefficient normalization

For positive frequencies, the audited H4 coefficient is

\[
 \alpha_{h,H}=
 -\frac{\Phi(h/(H+1))}{2\pi i h}
 =\frac{i\Phi(h/(H+1))}{2\pi h}.
 \tag{2.1}
\]

Let \(\eta_L\) be a fixed normalized-BV dyadic cutoff supported on
\([L,2L]\), with its support intersected with \([1,H]\), and put

\[
 u_{L,H}(h)=\eta_L(h)\frac{\Phi(h/(H+1))}{h}.
 \tag{2.2}
\]

The accepted profile \(\Phi\) has uniform bounded variation on \([0,1]\).
Product variation, together with \(h\asymp L\), gives

\[
 \sup_h|u_{L,H}(h)|+
 \sum_h|u_{L,H}(h+1)-u_{L,H}(h)|\ll L^{-1}.
 \tag{2.3}
\]

The last intersection may create one discrete endpoint jump, but its size
is at most \(O(L^{-1})\), so (2.3) remains valid.  Thus the positive M1
terminal block is exactly the fixed factor \(-2i/\pi\) times (1.1).

The lemma is stated for complex bounded \(w_D\).  For the project's real
dyadic profile the negative-frequency block is the conjugate partner of
the positive block.  Without a reality assumption, the same proof is
applied to negative \(h\) separately.

## 3. Proof of the frequency-first divisor lemma

For every real \(\theta\), summation by parts and the geometric-progression
bound give

\[
 \left|\sum_hu_{L,H}(h)e(h\theta)\right|
 \ll \min\left(1,\frac1{L\|\theta\|}\right).
 \tag{3.1}
\]

The value at \(\|\theta\|=0\) is interpreted as the first alternative.
Apply (3.1) with \(\theta=X/d\).  Choose an integer \(m_d\) nearest to
\(X/d\), and set

\[
 n_d=d m_d.
 \tag{3.2}
\]

Then

\[
 |X-n_d|=d\|X/d\|\le d/2\ll D.
 \tag{3.3}
\]

Moreover, for a fixed integer \(n\), each participating \(d\) is a divisor
of \(n\).  Since \(d\le X^{1/2}\) and \(|X-n|\ll D\), one has \(n\asymp X\)
for large \(X\); the finitely many small cases are absorbed in the implied
constant.  Hence the multiplicity of (3.2) is at most

\[
 \tau(n)\ll_\varepsilon X^\varepsilon.
 \tag{3.4}
\]

Taking absolute values only after the frequency sum, (3.1)--(3.4) yield

\[
\begin{aligned}
 |\mathcal B_{1,L}(D;X)|
 &\ll \sum_{d\in\mathcal D_D}
 \min\left(1,\frac1{L\|X/d\|}\right)\\
 &\ll_\varepsilon X^\varepsilon
 \sum_{\substack{n\in\mathbb Z\\|n-X|\ll D}}
 \min\left(1,\frac{CD}{L|X-n|}\right).
 \tag{3.5}
\end{aligned}
\]

If \(X\) is an integer, its zero denominator contributes one term in the
last sum.  For all other terms, split at \(|X-n|\le D/L\) and then into
unit-distance bins.  This gives

\[
 \sum_{|n-X|\ll D}
 \min\left(1,\frac{CD}{L|X-n|}\right)
 \ll \left(1+\frac DL\right)\log(2D).
 \tag{3.6}
\]

Absorbing the logarithm into \(X^\varepsilon\) proves (1.3).  Under (1.5),

\[
 \frac DL\asymp X^{1/4},
\]

which proves (1.6).  No stationary-phase or unsmoothing error occurs in
this direct argument.

## 4. Additive-quarter form and why it is not the source of the saving

The spatial character identity is exact:

\[
 \chi_4(d)=\frac{e(d/4)-e(3d/4)}{2i}.
 \tag{4.1}
\]

Thus (1.1) is the difference of the two quantities

\[
 \mathcal B_{1,L}^{(\rho)}=
 \sum_{d\in\mathcal D_D}w_D(d)e(\rho d/4)
 \sum_hu_{L,H}(h)e(hX/d),
 \qquad \rho\in\{1,3\}.
 \tag{4.2}
\]

The proof of Section 3 applies to each \(\rho\) separately because
\(|e(\rho d/4)|=1\).  In contrast with M2, these quarter shifts lie on the
spatial variable, not on \(h\); they do not alter the geometric frequency
denominator \(\|X/d\|\).  Therefore (1.6) is not a cancellation between
the residues \(1\) and \(3\pmod4\).  The character is exact in the formula,
but the terminal estimate does not need to spend its sign.

## 5. Consequence for the terminal shell of the accepted endpoint cone

Assume the hard endpoint notation of Round 9:

\[
 y=\lfloor\sqrt X\rfloor,\qquad q=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]

and the real top profile \(W(d/y){\bf1}_{d\le y}\).  Insert an additional
fixed-BV cutoff \(h\asymp L\asymp H\) into the accepted transform.  Its
positive stationary part is

\[
 -\frac{2e(1/8)}{\pi}X^{1/4}\mathcal K_L(X;q),
 \tag{5.1}
\]

where

\[
 \mathcal K_L(X;q)=
 \sum_{h\asymp L}
 \frac{\eta_L(h)\Phi(h/(H+1))}{h^{3/4}}
 \sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
 \frac{\chi_4(n)W(\sqrt{4qh/n})}{n^{3/4}}
 e(\sqrt{Xhn}).
 \tag{5.2}
\]

On one terminal \(h\)-shell, the exact character-boundary contribution is
\(O(1)\), because each \(E_h^\chi(X)\ll1\) and the coefficient mass is
\(\sum_{h\asymp L}h^{-1}=O(1)\).  The accepted per-frequency transform
remainder \(O_W(\log(2+h))\), after multiplication by \(h^{-1}\) and
summation over this shell, is \(O_W(\log(2L))\).  These are both
target-sized.  Combining (1.6) with the exact transform identity gives

\[
 \boxed{|\mathcal K_L(X;q)|\ll_{\varepsilon,W}X^\varepsilon.}
 \tag{5.3}
\]

Since \(h,n\asymp L\), (5.3) is equivalently the normalized signed-cone
bound \(T_L\ll L^{3/2}X^\varepsilon\) for this terminal shell, with the
actual \(\Phi\), \(W\), parity, and \(\chi_4(n)\) retained.  It is not the
whole-height cone bound: summing (1.3) over lower dyadic \(L\) loses
\(D/L\), and the smallest shells are not controlled at the target scale by
this lemma.

## 6. Required controls

1. **Hard endpoint and endpoint jump: pass.**  The direct proof sums the
   included integer \(d=y\) with full weight and never replaces the
   one-sided sum by a full-line Poisson formula.  In the cone transfer, the
   accepted explicit boundary is retained and is \(O(1)\) on the terminal
   shell; it is not silently deleted.

2. **Shifted residues \(1,3\pmod4\): pass separately.**  Equation (4.2)
   shows that each additive-quarter component satisfies (1.3).  No false
   cross-residue cancellation is claimed.

3. **Both frequency signs: pass.**  Negative frequencies obey the same
   BV-geometric estimate after replacing \(\theta\) by \(-\theta\).  For
   real \(w_D\), they are the exact conjugate partner required by H3/H4.

4. **Exact-square resonances: pass.**  If \(X=y^2\), every divisor
   \(d\mid y^2\) makes \(X/d\) integral and the frequency sum can be
   coherent.  Their number in the shell is at most
   \(\tau(y^2)\ll_\varepsilon X^\varepsilon\), exactly the zero-distance
   term already allowed in (3.5).  Thus exact resonance costs no power.
   Product-phase resonances after the endpoint transform are controlled
   only in aggregate through the exact identity, not termwise.

5. **Arbitrary-weight proves-too-much test: scoped pass.**  The proof does
   establish (1.3) for arbitrary bounded spatial coefficients \(a_d\), not
   merely for \(\chi_4(d)w_D(d)\).  This is harmless because (1.3) closes
   only \(L\asymp H_D\); for lower blocks it deteriorates by
   \(H_D/L\).  It proves neither an arbitrary-frequency-coefficient
   theorem nor an unsigned fourth-moment/near-collision estimate.  An
   adversarial frequency sequence destroys (1.2) and the geometric bound.

6. **Boundary and errors: pass.**  There are no transform errors in the
   direct proof.  When translating to (5.2), the accepted one-sided
   boundary is \(O(1)\) and the accepted transform remainder is
   \(O_W(\log L)\) on one dyadic shell.

7. **Target comparison: pass.**  At \(L\asymp H_D\), the exact loss is
   \(D/L\asymp X^{1/4}\).  There is no additional endpoint power at
   \(D\asymp X^{1/4},X^{1/3},X^{3/8}\), or \(X^{1/2}\).

8. **Numerical use: none.**

## 7. First doubtful or unproved step

The direct lemma (1.3) has no unproved analytic step beyond the elementary
divisor bound and the accepted BV regularity of the Vaaler profile.  The
endpoint-cone corollary additionally relies on the already accepted Round-9
one-sided transform and its remainder.

The first genuinely unproved continuation is the lower/intermediate M1
frequency range \(L=o(H_D)\).  Estimate (1.3) becomes

\[
 X^{1/4+\varepsilon}\frac{H_D}{L},
\]

so it cannot be extrapolated to those blocks.  Likewise, (5.3) proves only
the terminal shell of the endpoint cone, not `M9-M1-top-endpoint-signed-cone`
as a whole unless that obligation is explicitly decomposed by frequency.

## 8. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/briefs/m1_terminal_arithmetic_attack.md`
- `rounds/codex-managed/m9-generic-band-signed-correlation/reports/top_block_two_shift_attack.md`
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`
- `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_hostile_audit.md`

No external theorem or numerical artifact was used.

## 9. Recommended state effect

1. **Promote**, after the required independent validation, a scoped
   `M9-M1-terminal-frequency-divisor-bound` with status `proved_internal`:
   (1.3) and its terminal consequence (1.6).
2. Record as a corollary that the hard-endpoint transformed M1 cone satisfies
   its normalized signed estimate on the terminal \(h\)-shell only.
3. Keep `M9-M1-top-endpoint-signed-cone`, `M9-M1`, `M9-endpoint-uniformity`,
   `M9`, and the Gauss-circle target open.  Their lower/intermediate
   frequency blocks are not settled by this report.



