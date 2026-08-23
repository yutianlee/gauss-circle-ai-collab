# 1. Result: one-sided reduction and a sharp Fejer-sector no-go

**Lemma (exact signed reduction and coefficient-blind sector obstruction).**  For the literal array (125.B1), with zero extension made before every shift,

\[
 \mathcal S_{\rm off}=\widetilde{\mathcal F}_{M,H}-\mathcal D_0,
 \qquad \widetilde{\mathcal F}_{M,H}\geq 0,
 \qquad \mathcal D_0\geq 0.
\tag{1.1}
\]

Consequently

\[
 \mathcal S_{\rm off}\geq-\mathcal D_0,
 \qquad
 |\mathcal S_{\rm off}|
 \leq \max\{\widetilde{\mathcal F}_{M,H},\mathcal D_0\},
\tag{1.2}
\]

and, because \(\mathcal D_0\ll X^{1/2}\), (125.B10) is equivalent to the single upper estimate

\[
 \widetilde{\mathcal F}_{M,H}\ll_\varepsilon X^{1/2+\varepsilon}.
\tag{1.3}
\]

Thus the negative side of the complete signed survivor is already target-safe.  The positive side is the only unresolved side.

There is also a rigorous fixed-power no-go for coefficient-blind sectorization.  With the exact Fejer weights, exact zero extension, and the actual placement of two opposite \(\chi _4\)-signs, one can have

\[
 |\mathcal S_{\rm eq}^{\ne0}|\gg H\mathcal D_0,
 \qquad |\mathcal S_{\rm neq}|\gg H\mathcal D_0,
 \qquad \mathcal S_{\rm off}=-\mathcal D_0.
\tag{1.4}
\]

Since \(H\asymp X^{1/2-\delta}\to\infty\), separate target estimates for the two sectors are strictly stronger, by a fixed power, than the required estimate.  This is a no-go only for arguments using block positivity, coefficient sizes, zero extension, and character magnitudes without the literal phase/profile interaction.  It is not a counterexample to (125.B10) for (125.B1).

# 2. Exact statement and hypotheses

Assume all hypotheses in the blind statement: \(M\asymp X\),

\[
 D=X^\delta,\quad L=X^\ell,\quad K=XL/D^2,\quad
 H=\lceil X^{1/2}/D\rceil,
\]

with

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,
\]

and \(Q=D^2/(L\sqrt X)\to\infty\).  The profiles are the literal smooth, compact fixed-interior profiles, and \(b_{p,k}\) is exactly (125.B1) for positive odd \(p\), extended by zero outside its literal support before a shift.  The character is the real primitive character \(\chi _4(p)\in\{1,-1\}\) on odd \(p\), and \(C_H=(J+H-1)/H^2\), \(J\asymp K\).

For the structural no-go only, let \(H\geq 8\), choose two odd modes \(r\equiv1\pmod4\) and \(s\equiv3\pmod4\), and let \(c=(c_k)\) be any finite, zero-extended sequence.  Put

\[
 b_{r,k}=b_{s,k}=c_k,
 \qquad b_{p,k}=0\quad(p\notin\{r,s\}).
\tag{2.1}
\]

One may take a smooth-after-scaling adversary

\[
 c_k=\alpha\psi(k/N),
\tag{2.2}
\]

where \(0\leq\psi\leq1\), \(\psi\in C_c^\infty((0,1))\), \(\psi=1\) on \([1/3,2/3]\), and \(N\geq48H\).  This auxiliary table is used only for the mandated coefficient-adversary control; it is never substituted for the physical formula (125.B1).

# 3. Proof and derivation

## 3.1. Scale normalization

The inequalities \(0\leq\ell<\delta-1/4\) force \(\delta>1/4\).  If \(H_0=X^{1/2}/D\), then

\[
 H=H_0+O(1)\asymp X^{1/2-\delta}\longrightarrow\infty,
 \qquad K=L H_0^2,
 \qquad Q=\frac{\sqrt X}{K}.
\tag{3.1}
\]

Also \(K/H\asymp LH\to\infty\).  Since \(J\asymp K\),

\[
 C_H=\frac{J+H-1}{H^2}\asymp\frac K{H^2}\asymp L.
\tag{3.2}
\]

The two stated post-transform capacities normalize exactly as

\[
 \frac{D^2}{L}=Q\sqrt X,
 \qquad D^2=LQ\sqrt X.
\tag{3.3}
\]

Thus the capacities \(D^2/L\) and \(D^2\), if all that remains after an unsigned estimate, exceed the square target by the factors \(Q\) and \(LQ\), respectively.

On the declared fixed-interior packet support, \(p\asymp L\), \(k\asymp K\), and \(|h|<H=o(K)\).  The literal amplitude has size

\[
 |b_{p,k}|\ll X^{1/4}K^{-3/4}L^{-3/4}.
\tag{3.4}
\]

There are \(O(LK)\) supported pairs, so

\[
 \sum_{p,k}|b_{p,k}|^2\ll
 X^{1/2}K^{-1/2}L^{-1/2}=\frac DL,
 \qquad
 C_HH\sum_{p,k}|b_{p,k}|^2\ll X^{1/2},
\tag{3.5}
\]

consistent with the accepted diagonal estimate.

## 3.2. Exact Fejer expansion and the two sectors

Write \(A(k)=\widetilde A(k)=\sum_p\chi _4(p)b_{p,k}\).  All sums are finite after zero extension.  Expanding the block square and putting \(h=a-c\), \(k=n+c\), gives

\[
\begin{aligned}
 \sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
 &=\sum_n\sum_{a,c=0}^{H-1}A(n+a)\overline{A(n+c)}\\
 &=\sum_{|h|<H}(H-|h|)\sum_k A(k+h)\overline{A(k)}.
\end{aligned}
\tag{3.6}
\]

For every \(h\), the multiplicity \(H-|h|\) is the exact number of ordered pairs \((a,c)\in[0,H-1]^2\) with \(a-c=h\).  Expanding the two mode sums yields

\[
 \widetilde{\mathcal F}_{M,H}
 =C_H\sum_{p,q}\chi _4(p)\chi _4(q)
 \sum_{|h|<H}(H-|h|)\sum_k
 b_{p,k+h}\overline{b_{q,k}}.
\tag{3.7}
\]

The subcase \(p=q,h=0\) is exactly \(\mathcal D_0\), because \(\chi _4(p)^2=1\).  The subcase \(p=q,h\ne0\) is exactly \(\mathcal S_{\rm eq}^{\ne0}\).  The ordered subcase \(p\ne q\), including \(h=0\), is exactly \(\mathcal S_{\rm neq}\).  Therefore

\[
 \widetilde{\mathcal F}_{M,H}
 =\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
  +\mathcal S_{\rm neq},
 \qquad
 \mathcal S_{\rm off}
 =\widetilde{\mathcal F}_{M,H}-\mathcal D_0.
\tag{3.8}
\]

Keeping only \(p=q\) before summing the modes gives the distinct positive energy

\[
 \mathcal P_{\rm eq}:=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
 =C_H\sum_p\sum_n\left|\sum_{a=0}^{H-1}b_{p,n+a}\right|^2\geq0.
\tag{3.9}
\]

It is \(\widetilde{\mathcal F}_{M,H}\), not \(\mathcal P_{\rm eq}\), that is equivalent to the target after the diagonal is known.

For

\[
 T_{p,q}(h)=\sum_k b_{p,k+h}\overline{b_{q,k}},
\]

zero extension and reindexing give

\[
 T_{q,p}(-h)=\overline{T_{p,q}(h)}.
\tag{3.10}
\]

Hence the negative shift is the conjugate only after the ordered modes are swapped (with no swap needed when \(p=q\)).  The symmetric Fejer weight makes both full sectors real.  This proves reality, not cancellation or smallness.

## 3.3. Literal correlation phase and character placement

On the common positive support, the constant phases \(e(-1/8)\) cancel and

\[
\begin{aligned}
 b_{p,k+h}\overline{b_{q,k}}
 &=M^{1/2}(k+h)^{-3/4}k^{-3/4}p^{-3/4}q^{-3/4}\\
 &\quad\times \mathcal A_{p,k+h}\overline{\mathcal A_{q,k}}
 e\!\left(\Theta_{p,q,h}(k)\right),
\end{aligned}
\tag{3.11}
\]

where

\[
 \Theta_{p,q,h}(k)=\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\}.
\]

No character occurs in (3.11).  It remains outside as the exact factor \(\chi _4(p)\chi _4(q)\) in the ordered unequal-mode sum.  In the equal-mode sum it becomes \(\chi _4(p)^2=1\).

For \(p=q\) and \(h\ne0\), direct differentiation gives

\[
 \Theta'_{p,p,h}(k)
 =\frac{\sqrt{Mp}}2\{(k+h)^{-1/2}-k^{-1/2}\}
 =-\frac{\sqrt{Mp}\,h}
 {2\sqrt k\sqrt{k+h}(\sqrt k+\sqrt{k+h})},
\tag{3.12}
\]

and

\[
 \Theta''_{p,p,h}(k)
 =\frac{\sqrt{Mp}}4\{k^{-3/2}-(k+h)^{-3/2}\}.
\tag{3.13}
\]

On a fixed-interior support piece,

\[
 |\Theta'_{p,p,h}(k)|\asymp \frac{Q|h|}{H},
 \qquad
 |\Theta''_{p,p,h}(k)|\asymp\frac{Q|h|}{HK}.
\tag{3.14}
\]

Thus \(\Theta'\) is monotone on such a piece, but its range can meet
\(O(1+Q|h|/H)\) integers.  Nonvanishing of the real derivative is not a first-derivative estimate for an integer sum: neighborhoods where \(\Theta'\) meets an integer are discrete stationary returns, and curvature (3.13) must be paid for.

For unequal modes, rationalization gives two genuinely different defects:

\[
 \Theta_{p,q,h}(k)
 =\frac{\sqrt M\,[p(k+h)-qk]}
 {\sqrt{p(k+h)}+\sqrt{qk}}
 =\frac{\sqrt M\,\mathcal N}
 {\sqrt{p(k+h)}+\sqrt{qk}},
\tag{3.15}
\]

whereas

\[
 \Theta'_{p,q,h}(k)
 =\frac{\sqrt M\,[pk-q(k+h)]}
 {2\sqrt{k(k+h)}\,[\sqrt{pk}+\sqrt{q(k+h)}]}
 =\frac{\sqrt M\,\mathcal G}
 {2\sqrt{k(k+h)}\,[\sqrt{pk}+\sqrt{q(k+h)}]}.
\tag{3.16}
\]

Their difference is \(\mathcal N-\mathcal G=(p+q)h\).  If both defects vanish, positivity of \(p,q,k\) forces \(h=0\), then \(p=q\).  Hence there is no joint exact zero inside the unequal sector.  This does not exclude near zeros or integer stationary returns, and it supplies no saving by itself.

## 3.4. Positivity, target equivalence, and the no-go example

Equation (3.8), together with the square in (125.B3), proves (1.1).  For nonnegative real numbers \(u,v\), \(|u-v|\leq\max(u,v)\); this proves (1.2).  If (125.B10) holds, then

\[
 \widetilde{\mathcal F}_{M,H}
 =\mathcal S_{\rm off}+\mathcal D_0
 \ll_\varepsilon X^{1/2+\varepsilon}.
\]

Conversely, (1.3) and \(\mathcal D_0\ll X^{1/2}\) imply (125.B10).  This proves the equivalence without confusing the full block energy with the equal-mode energy (3.9).

Now use the auxiliary table (2.1).  Since \(\chi _4(r)=1\) and \(\chi _4(s)=-1\),

\[
 \widetilde A(k)=c_k-c_k=0,
 \qquad \widetilde{\mathcal F}_{M,H}=0.
\tag{3.17}
\]

Put

\[
 E_0=\sum_k|c_k|^2,
 \qquad E_H=\sum_n\left|\sum_{a=0}^{H-1}c_{n+a}\right|^2,
 \qquad R=\frac{E_H}{HE_0}.
\tag{3.18}
\]

For (2.2), at least \(N/4\) block origins have all \(H\) entries in the plateau \(\psi=1\), once \(N\geq48H\).  Hence

\[
 E_H\geq\frac N4H^2|\alpha|^2,
 \qquad E_0\leq N|\alpha|^2,
 \qquad R\geq\frac H4.
\tag{3.19}
\]

The exact sector identities are

\[
 \mathcal D_0=2C_HHE_0,
 \quad \mathcal P_{\rm eq}=2C_HE_H=R\mathcal D_0,
\tag{3.20}
\]

\[
 \mathcal S_{\rm eq}^{\ne0}=(R-1)\mathcal D_0,
 \quad \mathcal S_{\rm neq}=-R\mathcal D_0,
 \quad \mathcal S_{\rm off}=-\mathcal D_0.
\tag{3.21}
\]

This proves (1.4).  Scaling \(\alpha\) so that \(\mathcal D_0\asymp X^{1/2}\) makes each separate sector as large as \(X^{1-\delta}\), while their complete signed sum remains target-sized.

For completeness, retaining only the mode \(r\) in the same auxiliary table gives

\[
 \mathcal S_{\rm neq}=0,
 \qquad \mathcal S_{\rm off}=\mathcal S_{\rm eq}^{\ne0}
 =(R-1)\mathcal D_0\gg H\mathcal D_0.
\tag{3.22}
\]

Therefore positivity and the diagonal estimate alone do not provide the missing upper bound either.  The two examples together isolate the exact logical boundary: neither a separate-sector target bound nor a full upper bound follows from the Fejer algebra; any such proof must use additional literal signed oscillation in (3.11).

# 4. First doubtful or unproved step

The first unproved step is precisely

\[
 C_H\sum_n\left|
 \sum_{\substack{p>0\\p\text{ odd}}}\chi _4(p)
 \sum_{a=0}^{H-1}b_{p,n+a}
 \right|^2
 \ll_\varepsilon X^{1/2+\varepsilon}.
\tag{4.1}
\]

Neither the nonzero derivative (3.12), the distinction \(\mathcal N\ne\mathcal G\), conjugate pairing, nor a stationary inversion proves (4.1).  Absolute sectorization can be stronger than the target by \(H=X^{1/2-\delta+o(1)}\), and the quoted unsigned return capacities still require gains \(Q\) or \(LQ\).  I have not proved that the literal phases and profiles supply any of these gains.  Accordingly this report does not prove (125.B10), a target-safe complete equal sector, or a target-safe complete unequal sector.

# 5. Control tests and outcomes

| Control | Exact input | Expected invariant or failure | Observed outcome | Implication |
|---|---|---|---|---|
| `literal_Round124_dual_offproduct_survivor` | (125.B1)--(125.B9), unchanged | The complete survivor must remain the literal scalar, modulo only the accepted diagonal identity | (3.7)--(3.8) give exactly \(\mathcal S_{\rm off}=\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}=\widetilde{\mathcal F}_{M,H}-\mathcal D_0\) | No sub-sector or rectangular proxy replaces the physical survivor |
| `H_K_Q_normalization` | Exact definitions of \(D,L,K,H,Q,C_H\) | Ceilings and relative sizes must not change a power | (3.1)--(3.3): \(H\asymp X^{1/2-\delta}\), \(K\asymp LH^2=\sqrt X/Q\), \(K/H\to\infty\), \(C_H\asymp L\) | All later factors \(H,Q,LQ\) are on the declared scale |
| `bpk_profile_and_character_placement` | Literal (125.B1), (125.B2) | Profile, phase, and character must not be flattened or relocated | (3.11) keeps both moving profiles; \(\chi _4(p)\chi _4(q)\) remains outside the correlation and becomes 1 only for \(p=q\) | Any future signed gain must act with this exact placement |
| `Fejer_block_square_identity` | All \(a,c\in\{0,\ldots,H-1\}\), all integer block origins, zero extension | Exact triangular multiplicity | (3.6) gives \(H-|h|\) with no boundary remainder | Passed as an algebraic identity |
| `equal_mode_offzero_vs_positive_energy` | \(p=q\), split \(h=0\) from \(0<|h|<H\) | Positivity belongs to \(\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}\), not to the offzero term | (3.9) is positive, but (3.21) makes it \(\gg H\mathcal D_0\) while the target survivor is safe | Treating (3.9) as target-equivalent fails |
| `equal_mode_integer_crossings_and_curvature` | (3.12) on \(p\asymp L,k\asymp K,0<|h|<H\) | A nonzero real derivative must still be checked modulo integers | (3.13)--(3.14) show curvature and up to \(O(1+Q|h|/H)\) possible integer crossings | A first-derivative slogan gives no certified saving |
| `unequal_mode_product_gradient_defects` | \(p\ne q\), exact \(\Theta\) and \(\Theta'\) | Product and stationary defects must remain distinct | (3.15)--(3.16) give \(\mathcal N-\mathcal G=(p+q)h\); joint exact zero forces the excluded \(p=q,h=0\) | Near-product counting cannot be silently used as gradient control |
| `unequal_mode_character_persistence` | Ordered \(p\ne q\) sector including \(h=0\) | No outside modulus may erase \(\chi _4(p)\chi _4(q)\) | The character remains in (3.7), and the adversary (3.17) changes completely when it is removed | An unsigned unequal estimate is only sufficient and may lose the decisive cancellation |
| `sector_intercancellation` | Opposite-character smooth adversary (2.1)--(2.2) | Test whether the two sectors can each be large while their sum is small | Exact equations (3.20)--(3.21) give cancellation to \(-\mathcal D_0\) | Separate target bounds are overstrong by \(\gg H\) at the algebraic level |
| `negative_shift_conjugacy` | Ordered triple \((p,q,h)\) and its partner \((q,p,-h)\) | Pairing should certify reality only | (3.10) is exact; the weights agree | No magnitude saving is inferred from conjugacy |
| `mode_shift_multiplicity` | Ordered block positions \((a,c)\) | Include both signs and exact entries/exits | Multiplicity is \(H-|h|\), and \(\sum_{|h|<H}(H-|h|)=H^2\) | No factor \(H\) is discarded |
| `moving_profile_and_zero_extension` | Literal \(\mathcal A_{p,k+h}\overline{\mathcal A_{q,k}}\) | No common rectangular support and no periodic wraparound | (3.11) retains both moving profiles; zero extension justifies (3.6) and (3.10) exactly | Endpoint terms are present through the shifted profiles, not omitted |
| `stationary_endpoint_and_error_scope` | Only the common positive interior for derivative formulas; zero elsewhere | A transform must account for endpoints and errors before claiming a gain | No second transform is used here; (3.12)--(3.16) are exact local identities and no endpoint/error estimate is asserted | The nominal stationary return is retained only as a barrier |
| `signed_vs_unsigned_and_adversarial_coefficients` | In (2.1), test true \(\chi _4\), \(|\chi _4|\), random signs, and adversarial relative phases | A signed mechanism must distinguish the four | True signs give \(\widetilde A=0\); absolute signs give \(\widetilde A=2c\) and energy \(4C_HE_H\); two random signs give either case, while an adversarial phase can force cancellation or reinforcement | Fejer positivity and coefficient magnitudes do not constitute a signed proof; the auxiliary test is not a claim about (125.B1) |
| `capacity_before_and_claimed_gain` | Nominal ledgers \(D^2/L\), \(D^2\), target \(\sqrt X\) | Inversion alone must not be counted as saving | (3.3) leaves excess factors \(Q\) and \(LQ\); no gain is claimed in this report | A future proof must exhibit at least the relevant signed factor explicitly |
| `owner_and_downstream_scope` | Flat-smooth strict-UNBAL owner only | No transfer to hard, sharp, clipped, starred, arithmetic, nonflat, or transition owners | Every statement above is restricted to the blind packet, and the adversary is only a structural control | No downstream theorem or other owner is certified |

# 6. Dependencies and exact artifacts used

Only the following permitted artifacts were used:

1. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/briefs/blind_dual_offproduct_sector_rederivation.md` for the frozen task, scope, and required controls.
2. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/blind_statement.md` for (125.B1)--(125.B13) and the packet hypotheses.
3. `state/control_models.md` for the proof-unit-test semantics, especially signed-versus-unsigned, coefficient adversary, exact-versus-near resonance, and support/degeneracy separation.
4. `problems/gauss_circle.md` for the ambient square-error goal.

No strategy file, proof graph, prior nonblind round artifact, sibling report, web source, or numerical experiment was consulted.

# 7. Recommended state effect

**Retain.**  Retain (1.1)--(1.3) as the exact one-sided reduction and retain (1.4), proved by (3.17)--(3.21), as a sharp fixed-power barrier to coefficient-blind separate-sector estimates.  Do not promote (125.B10): the full signed upper bound (4.1) remains unproved.  If this UNBAL lane is continued, it should continue only with a mechanism that uses the literal \(\chi _4\)-weighted moving-profile phase before taking an outside modulus; otherwise the smallest rigorous conclusion is the no-go above.
