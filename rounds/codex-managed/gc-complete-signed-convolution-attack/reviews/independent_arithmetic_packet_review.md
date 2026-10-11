# Round 203: independent arithmetic packet seam review

Campaign: `gc-complete-signed-convolution-attack`. Reviewer task: `actual_density_remainder_attack`, bounded follow-up seam review. Date: 2026-09-23. Reviewed artifact: `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/arithmetic_signed_tail_attack.md`. Exact reviewed SHA-256, verified before reading: `c8780626545887e255ffbb77815bf6fad1f7f743846c0485e35f34924b5739b8`. Starting graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`.

## 1. Result: scoped GREEN

**GREEN for the complete arithmetic transformation and its stated no-gain conclusion.** The reviewed report has the correct stationary phase, amplitude and cosine sign. The stationary remainder is uniform when its critical point crosses a smooth support boundary, and its complete sum has the stated size. The actual character expansion, geometric bound, real-centered product count, degenerate dyadic endpoints, infinite tails, lower collar and moment recombination all pass this review.

The direct established estimates are the box bound
\[
 |H_{D,M}(R)|\ll_\varepsilon T^\varepsilon
 \min\{N^{1/4},T^{1/2}N^{-1/2}\},\qquad N=DM,
 \tag{R1}
\]
and the complete bounds
\[
 \int w(R/T)|H_{T,>U}(R)|^{12}dR\ll_\varepsilon T^{7/3+\varepsilon},
 \qquad \|K_T*\mu_{T,>U}^{*6}\|_2\ll_\varepsilon T^{7/6+\varepsilon}.
 \tag{R2}
\]
These are weaker than the requested estimate. The comparison using \(q_0=262/27\) remains conditional on its inherited source and smoothing interface. This GREEN does not certify that inherited premise, prove the target packet moment, or promote any parent obligation.

## 2. Exact reviewed statement and hypotheses

The review covers equations (2), (8)-(29), and the equivalence claim surrounding (31) of the hashed report. It checks the comparison arithmetic in (30), while retaining that comparison's explicit evidentiary condition.

Use real \(T\ge2\), \(R\asymp T>0\), \(U=\lfloor T^{1/2047}\rfloor\), \(V=T^{3/2}\), and the fixed prescribed real Schwartz function \(\Psi\). The smooth dyadic partition functions have fixed support ratios bounded away from zero, derivative bounds \(O_j(D^{-j})\), and include lower-end functions containing the positive integer 1. The cutoffs \(\eta,\zeta\) have exactly the plateaus and smooth zero extensions specified in the report. All constants can depend on these fixed functions and on \(\varepsilon\).

For a nonzero box \(N=DM\ll V\), define
\[
 F=R\sqrt N,\qquad K=RD/\sqrt N=F/M.
 \tag{R3}
\]
Since \(D,M\ge1\), these obey \(F\gg T\), \(K\gg T^{1/4}\), and \(K\ll T^{7/4}=o(R^2)\), up to fixed support constants for sufficiently large \(T\). Bounded \(T\) is handled by uniform enlargement of constants. No integer condition on \(R^2\) is assumed.

## 3. Independent derivation of the reviewed seams

### Stationary amplitude and phase

For fixed \(d\asymp D\), the Poisson integral in \(m\) has phase \(f(m)=R\sqrt{dm}-km\). Direct differentiation gives
\[
 m_0=\frac{R^2d}{4k^2},\quad f(m_0)=\frac{R^2d}{4k},\quad
 f''(m_0)=-\frac{2k^3}{R^2d},\qquad k>0.
 \tag{R4}
\]
Therefore
\[
 (dm_0)^{-3/4}|f''(m_0)|^{-1/2}
 =\left(\frac{R^2d^2}{4k^2}\right)^{-3/4}
   \frac{R\sqrt d}{\sqrt2 k^{3/2}}
 =\frac2{\sqrt R\,d}.
 \tag{R5}
\]
The Gaussian phase is \(e(-1/8)\). Multiplication by the original divisor factor 4 gives \(8R^{-1/2}e(-1/8)\); multiplication by the original cosine phase \(e(-3/8)\) gives \(-8R^{-1/2}\) before taking the real part. Thus the report's signed main packet and its weights at \(m_0\) have the correct constant, sign and arguments.

### A uniform proof at every stationary-support endpoint

The support-boundary issue can be checked without a moving-endpoint stationary phase rule. Put \(m=Mv^2\), so the smooth amplitude, including its Jacobian, has the form \(MN^{-3/4}A_d(v)\), with \(A_d\) supported in a fixed compact subinterval of \((0,\infty)\). All fixed derivative norms of \(A_d\) are uniformly bounded: powers of the normalized arguments times derivatives of \(\Psi\) are bounded by its Schwartz seminorms, while differentiated lower and upper cutoffs are supported where their normalized arguments are bounded.

The phase is now exactly quadratic:
\[
 R\sqrt{dM}\,v-kMv^2
 =\frac{R^2d}{4k}-\lambda(v-v_0)^2,
 \quad \lambda=kM,\quad v_0=\frac{R\sqrt d}{2k\sqrt M}.
 \tag{R6}
\]
For the enlarged positive range \(k\asymp K\), \(\lambda\asymp F\). The Fourier-Gaussian identity, with the report's Fourier convention, is
\[
 \int A(v)e(-\lambda(v-v_0)^2)dv
 =\frac{e(-1/8)}{\sqrt{2\lambda}}
   \int\widehat A(\xi)e(v_0\xi)e(\xi^2/(4\lambda))d\xi.
 \tag{R7}
\]
Subtracting the same expression with the last exponential replaced by 1, and using \(|e(t)-1|\le C|t|\), bounds the error by
\[
 C\lambda^{-3/2}\int |\widehat A(\xi)|\xi^2d\xi
 \ll \lambda^{-3/2}.
\]
The last integral is uniformly bounded by compact support and four bounded derivatives. Crucially, this proof is uniform in \(v_0\); if the saddle is outside the amplitude support its leading value is zero, and the same remainder bound holds. Flat smooth zero extension at the supports produces no boundary term.

After restoring \(MN^{-3/4}\), the first remainder for each integral is exactly
\[
 O(MN^{-3/4}F^{-3/2}).
\]
There are \(O(D)\) allowed integers \(d\) and \(O(K)\) dual indices in this range. Their complete absolute error is
\[
 O(DKMN^{-3/4}F^{-3/2})
 =O(R^{-1/2}D/N)=O(R^{-1/2}/M)\ll T^{-1/2}.
 \tag{R8}
\]
This confirms the report's total, including \(M=1\). It does not require a large number of original \(m\)-integers in a box.

### Every nonstationary dual index

Outside a fixed enlarged positive interval \(k\asymp K\), the derivative of the normalized phase is bounded below by a constant times \(F+|k|M\). Repeated integration by parts in the smooth compact amplitude gives
\[
 |I_{d,k}|\ll_A MN^{-3/4}(F+|k|M)^{-A}.
\]
Summing the nonstationary \(k\)'s and the \(d\)'s yields
\[
 O_A\{N^{1/4}(1+K)F^{-A}\}.
 \tag{R9}
\]
For example, at \(A=2\), the terms with and without \(K\) are bounded by \(R^{-1}DN^{-5/4}\) and \(R^{-2}N^{-3/4}\), respectively. Since \(D\le N\), this is already \(O(T^{-1})\), stronger than the required \(O(T^{-1/2})\). Thus \(k=0\), every negative \(k\), and the unbounded positive dual tail are priced. Summing over the \(O((\log T)^2)\) boxes incurs only \(T^\varepsilon\).

### Actual character, geometric sums and product counting

The identity
\[
 \chi_4(d)=\frac{e(d/4)-e(-d/4)}{2i}
\]
is exact, including even \(d\). At fixed \(R,k\), the report's weight \(d^{-1}W_{D,M}\) has size and total variation \(O(D^{-1})\). All its arguments change on scale \(D\); smooth cutoff derivatives and Schwartz derivatives preserve this bound. Partial summation therefore gives precisely the two geometric factors
\[
 D^{-1}\min\left(D,\left\|R^2/(4k)\pm1/4\right\|^{-1}\right).
 \tag{R10}
\]
This is valid also at \(D=1\), where the geometric sum contains only a bounded number of integers and its minimum is bounded by 1 up to the fixed support constants. The report explicitly locates the loss of cancellation between different \(k\)'s and between the two character branches at this modulus step.

If one distance is at most \(\delta\le1/2\), then some integer \(\ell\) satisfies
\[
 |R^2-k(4\ell\mp1)|\le C K\delta.
 \tag{R11}
\]
Because \(K=o(R^2)\), the integer product is positive and comparable to \(T^2\). The real-centered interval in (R11) contains \(O(K\delta+1)\) integers. Each has at most its divisor count \(O_\varepsilon(T^\varepsilon)\) possible \(k\)'s. Restricting the other factor modulo 4 only decreases the count. The resulting bound includes integer centers, exact products and either endpoint of the interval; the possible multiplicity at distance \(1/2\) is bounded.

The range of distances below \(1/D\) costs at most \(T^\varepsilon(K+D)\); the successive dyadic distance ranges cost in total \(T^\varepsilon(K\log(2D)+D)\). Exact zero distances have cost \(D\). For the bounded small values \(D=1,2\), the same formula follows directly from the trivial count, without requiring a nonempty list of dyadic distance ranges.

Multiplication by \(R^{-1/2}D^{-1}\), followed by (R8)-(R9), gives
\[
 |H_{D,M}|\ll_\varepsilon T^\varepsilon
 (R^{1/2}N^{-1/2}+R^{-1/2}).
\]
Since \(N\ll T^{3/2}\ll R^2\), the second term is dominated by the first. The original box has the independent trivial bound \(O(N^{1/4})\), proving (R1).

### The direct twelfth-moment power

Regrouping the original box by \(n=dm\) gives real coefficients on \(n\asymp N\), bounded by \(4d(n)n^{-3/4}\). Hence their squared sum is \(O_\varepsilon(N^{-1/2+\varepsilon})\). Since the product cutoff forces \(n\ll V\), distinct radicals satisfy
\[
 T|\sqrt n-\sqrt m|\gg T^{1/4}|n-m|.
\]
Fourier decay of the fixed smooth \(w\), the inequality \(2|a_na_m|\le|a_n|^2+|a_m|^2\), and summation of the resulting row bounds prove
\[
 \int w|H_{D,M}|^2\ll_\varepsilon T^{1+\varepsilon}N^{-1/2}.
\]
The sum-frequency terms are also rapidly small; they have no zero frequency. Multiplying by the tenth power of (R1) gives
\[
 \int w|H_{D,M}|^{12}
 \ll_\varepsilon T^\varepsilon\min(TN^2,T^6N^{-11/2}).
 \tag{R12}
\]
The first envelope increases with \(N\), the second decreases, and equality occurs at \(N=T^{2/3}\), with value \(T^{7/3}\). Weighted \(L^{12}\) triangle inequalities over the boxes cost only powers of \(\log T\). Thus the direct powers \(7/3\) and \(7/6\) are correct. The norm gap to \(29/50\) is \(44/75\).

### Collar, upper tails and cross terms

The cutoff identity (8) in the report is exact at every positive integer, in particular at \(n=U\) and \(n=2U\). Its collar is supported on \(U<n<2U\), has supremum \(O(U^{1/4+\varepsilon})\), and twelfth moment \(O(T^{1+3/2047+\varepsilon})\). This is strictly below the target exponent \(29/25\).

For \(V=T^{3/2}\), the absolute upper tail is bounded by
\[
 T^{L/2}V^{1/4+\varepsilon-L/2}
 =T^{3/8+(3/2)\varepsilon-L/4},
\]
so it is arbitrarily small after a fixed choice of a sufficiently large Schwartz seminorm. The report's estimate for every twelfth product with an upper-tail factor follows from its complete coefficient \(\ell^1\) norm. No cutoff at \(n=T\) is substituted for this argument.

The complete stationary error has supremum \(O(T^{-1/2+\varepsilon})\), hence twelfth moment \(O(T^{-5+\varepsilon})\). Combining the original two cosine signs by the real part is exact, while weighted Minkowski controls all box, collar, stationary-error and upper-tail cross terms. It never asserts that cross inner products vanish. Both directions of this same triangle inequality prove the stated equivalence between the target tail moment and the report's complete packet moment (31).

## 4. First doubtful or unproved step

There is no unproved seam identified in the reviewed elementary transformation and direct bound. The first outstanding estimate remains the complete signed packet moment (31) in the claimant report. Taking separate absolute values over the dual packets leads to (R12), which is quantitatively too weak.

The inherited \(q_0\) comparison is algebraically correct if its explicit premises hold:
\[
 \int w|B|^{q_0}\ll T^{1+\varepsilon},\qquad
 \|B\|_\infty\ll T^{\beta+\varepsilon}
 \Longrightarrow
 \|K_T*\mu^{*6}\|_2\ll
 T^{1/2+(12-q_0)\beta/2+\varepsilon}.
\]
Its printed value and its gap to \(29/50\) agree with the frozen strategy. This review does not re-audit the external \(q_0\) source or turn the inherited smoothing premise into an accepted theorem. The countermodel saturating the two abstract box norms is correctly labeled a norm-information control, not an actual arithmetic example or a refutation of the target.

## 5. Controls and outcomes

| Reviewed seam | Outcome |
|---|---|
| Actual stationary phase, factor and sign | GREEN: (R4)-(R5) and the Gaussian phase reproduce the report's \(-8R^{-1/2}\operatorname{Re}\) main term. |
| Stationary-support endpoints | GREEN: the exact quadratic proof (R6)-(R7) gives a uniform remainder with no moving-boundary loss. |
| Full stationary and dual remainder | GREEN: (R8)-(R9) include every \(d\), all near-stationary \(k\), nonpositive \(k\), and the infinite dual tail. |
| Actual \(\chi_4\), geometric sums and product count | GREEN: no surrogate coefficients; both character branches are present before the explicitly identified loss. |
| \(D=1\), \(M=1\) and real centers | GREEN: lower partition functions are smooth away from zero; all stated bounds remain valid without a long original interval, and exact product distances have finite cost. |
| Infinite arithmetic tails, lower collar and cross terms | GREEN: exact cutoff identity and weighted triangle inequalities cover every factor. |
| Direct moment and norm powers | GREEN: \(7/3\) and \(7/6\), with gap \(44/75\) to the norm target. |
| Inherited \(q_0\) comparison | CONDITIONAL, exactly as in the claimant: algebra checked, source and smoothing premises not certified here. |
| Scope and parent claims | GREEN: the target and parent obligations stay open; no universal arithmetic no-go is claimed. |

This is a derivation-aware independent seam review, not the campaign's statement-only task. No numerical experiment was performed, and no other sibling report was read.

## 6. Dependencies and exact artifacts used

The newly reviewed artifact is the hashed arithmetic report identified above. The review used only that report and the context already permitted for this reviewer:

- `protocol.md`.
- `state/proof_obligations.yml`, in its previously read relevant accepted/open scopes.
- `state/active_campaign.yml` and `strategy/round203_complete_signed_convolution_attack.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/candidates/conductor_signed_convolution_interface.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`.
- This reviewer's existing density task brief and analytical context.

The independent quadratic calculation above uses elementary smooth Poisson summation, the Fourier transform of a Gaussian, integration by parts, the elementary divisor bound and weighted norm inequalities. No new external result or source audit is imported. No sibling filter report, shared synthesis or successor plan was consulted.

## 7. Recommended state effect

Record **scoped GREEN** for the arithmetic packet interface, full remainders and direct no-improvement exponent accounting at the exact reviewed SHA. No correction is requested.

Keep the accepted graph, proof draft, target exponent and inherited \(q_0\) evidentiary status unchanged. The complete packet target remains unproved. Only this assigned review file was written; this bounded review stops here.
