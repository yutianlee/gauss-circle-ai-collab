# Round208: independent review of the bandlimited peak gate

## 1. Result

**Scoped GREEN for (B1)--(B10), the added old-sixth-to-new-tenth implication, and the printed conditional Gaussian-hierarchy consequences.** The local Fourier reproduction, global off-window estimate, shell normalization and errors, complete pointwise reconstruction, old/new sixth-order comparison, tenth-order intersection bound, and all displayed fractions are correct. No mathematical correction is required.

The selected tenth-order gate is sufficient for the pointwise milestone \(102/325\), and its current certificate has the asserted smaller deficit. This does not prove that gate or its arithmetic saving, does not establish a new pointwise exponent, and does not close the quarter theorem or any independent graph parent. The full hierarchy statement correctly retains extensions of the bridge and complementary estimates as hypotheses.

Campaign: `gc-full-proof-signed-arithmetic-review`. Task: `independent_bandlimited_peak_review`. Date: 2026-09-27. Role: independent post-report line/seam review, explicitly **not blind**. The earlier statement-only report is preserved unchanged. The final candidate SHA-256 is recorded in Section 6.

## 2. Exact statement and hypotheses reviewed

The reviewed candidate is `controls/conductor_bandlimited_strategy.md` in the current campaign. It fixes the actual Round205 mollifier and smooth partition, real \(T\ge2\), \(X=T^2\),

\[
I=[T/\sqrt2,\sqrt3T],\quad J=[X/2,3X],\quad
\beta=2\theta_{LY}-\tfrac12,
\]

and the actual finite frequency blocks supported in \(\{\xi:|\xi|\le2\sqrt N\}\). The moment window contains the pointwise radius interval \([T,\sqrt2T]\) with a margin comparable to \(T\) on both sides.

The exact bridge hypothesis is

\[
H_N(R)=R^{-1/2}Z_N(R^2)+E_N(R),\qquad
|E_N(R)|\ll T^{-1/2+\varepsilon}N^{-1}+O_A(T^{-A}),
\]

where the actual centered shell retains all positive \(m\), its actual fixed filter, and \(h(x)=2\sqrt x/\sqrt N\). This explicit per-block supremum error resolves the error-aggregation ambiguity noted in the separate statement-only report.

For fixed \(k\ge2\) and \(0<b<\min(\beta,1/6)\), the claim is the conditional implication from

\[
K_{2k}(N)\ll T^{k+1+2kb+\varepsilon}N^{-1/2}
\quad\text{for every dyadic }T^{4b}<N<T^{1-2b}
\]

to \(P(x)\ll x^{1/4+b/2+\varepsilon}\), using the printed complements. The concrete choice \(b=83/650\) lies within the reviewed Round206 range. For other choices, any required extension is explicitly hypothetical. All constants may depend on fixed filters, windows, \(b,k\), and epsilon; no moment order growing with \(T\) is asserted.

## 3. Independent proof and line audit

**Fourier reproduction and the off-window contribution, (B2).** Choose a Schwartz \(\eta\) with \(\widehat\eta=1\) on \([-2,2]\). Each block is a finite exponential polynomial, so termwise convolution gives exactly \(H_N=\eta_N*H_N\), with \(\eta_N(u)=\sqrt N\eta(\sqrt N u)\). For \(p=2k\),

\[
\|\eta_N\|_{p'}=N^{(1-1/p')/2}\|\eta\|_{p'}
=N^{1/(2p)}\|\eta\|_{p'}=N^{1/(4k)}\|\eta\|_{p'}.
\]

Hölder on \(I\) gives precisely (B2). For every real \(R_0\in[T,\sqrt2T]\), \(R\notin I\) implies \(|R-R_0|\ge cT\). The global coefficient bound therefore gives

\[
\left|\int_{\mathbb R\setminus I}\eta_N(R_0-R)H_N(R)\,dR\right|
\ll_B N^{1/4+\varepsilon}(T\sqrt N)^{-B}.
\]

Since \(1\le N\le T\), a sufficiently large fixed \(B\) makes this \(O_A(T^{-A})\). The use of a **global** coefficient bound, instead of the local \(T^\beta\) bound outside its licensed interval, is correct. Both real target endpoints retain the same positive margin. No lattice sampling or derivative bound for the discontinuous discrepancy is needed.

**Shell change of variables and explicit errors, (B3)--(B4).** For the main bridge term,

\[
\int_I|R^{-1/2}Z_N(R^2)|^{2k}\,dR
=\frac12\int_Jx^{-(k+1)/2}|Z_N(x)|^{2k}\,dx
\asymp_k T^{-k-1}K_{2k}(N).
\]

The error's \(2k\)-moment is at most \(T^{1-k+\varepsilon}N^{-2k}+O_A(T^{-A})\). Taking a \(2k\)-th root and multiplying by the reproduction factor gives exactly

\[
T^{-(k+1)/(2k)}N^{1/(4k)}K_{2k}^{1/(2k)}
+T^{(1-k)/(2k)+\varepsilon}N^{-1+1/(4k)}+O_A(T^{-A}).
\]

The second term is harmless for \(k\ge2,N\ge1\). Substitution of (B1) cancels both \(N\) powers and leaves \(T^{b+\varepsilon}\). Conversely, the same bridge and \(x\asymp T^2\) give

\[
K_{2k}\ll T^{k+1}\int_I|H_N|^{2k}\,dR
+T^{2+\varepsilon}N^{-2k}+O_A(T^{-A}).
\]

This verifies the inverse transfer used for (B8). In particular the inverse error for \(k=5\) is far below the stated target, whose radius exponent \(10b-\alpha/2\) ranges from \(294/325\) to \(332/325\) on the closed concrete band. No harmless error is incorrectly magnified by a large supremum.

**Real endpoints and complete reconstruction, (B1).** The low part \(N\le T^{4b}\) is controlled by \(N^{1/4}\), and the high part \(T^{1-2b}\le N\le T\) by \((T/N)^{1/2}\). Their dyadic sums are geometric, bounded by \(T^{b+\varepsilon}\). Both dividing endpoints are assigned to these known bounds. The middle has only \(O(\log T)\) blocks, so its sum costs an epsilon loss.

The cited Round205 decomposition retains the singleton and the entire original tail. More explicitly, between \(T\) and \(T^{3/2}\), the reviewed shell bound sums to \(O(T^\varepsilon)\): the leading \(T^{1/2}N^{-1/2}\) terms form a convergent dyadic sum, and the additive \(T^{-1/2+\varepsilon}\) terms cost only a logarithm. Beyond that cutoff the actual Schwartz coefficient tail is arbitrarily small. Thus the candidate's complete \(N\ge T\) contribution is licensed by the cited bounds, rather than discarded.

The accepted sharp reconstruction gives \(P(R_0^2)\ll T^{1/2+b+\varepsilon}\), including lattice-radius jumps through its stated error. Taking real \(T=\sqrt x\) covers every real \(x\ge4\). The real variable width and all real shell endpoints remain unchanged through the Jacobian. No moment over integer centers or fixed shell lengths is substituted.

**Concrete sixth-order comparison, (B5)--(B6).** With \(b=83/650\),

\[
4+6b=1549/325,\quad 4b=166/325,\quad1-2b=242/325,
\quad\tfrac14+b/2=102/325.
\]

The new open band is strictly contained in \((52/125,99/125)\). Because \(b<\beta<1/6\), both breakpoints satisfy
\(4b<4\beta<1-2\beta<1-2b\), and \(\omega>b\) throughout the new band.

The difference “new allowed sixth exponent minus old allowed sixth exponent” is

\[
6b-29/25-\alpha/2+6\omega.
\]

Its three slopes are \(1,-1/2,-7/2\). Hence it increases to \(4\beta\) and decreases thereafter, so its minimum on the closed band is at an endpoint. Those endpoint values are \(38/325\) and \(0\), respectively. It is strictly positive inside. Thus the new sufficient gate is genuinely weaker wherever required, with its sole equality endpoint already covered separately. It need not imply the old complete twelfth moment, as the candidate explicitly states.

Subtracting the new gate from the retained \(T^5N^{-29/110}\) upper certificate gives

\[
1-6b+(13/55)\alpha.
\]

This is increasing, with endpoint values \(6338/17875\) and \(7326/17875\). Both are positive; the latter is a supremum on the open band. These are gaps between certificates, not lower bounds for the actual moment.

**Both terms in the variance/tail intersection, (B7).** For fixed \(2<p<q\), \(q=136/13\), Chebyshev is valid for all \(V>0\), while the accepted distribution estimate is needed only for \(V\ge1\). Set

\[
V_0=N^{1/(2(q-2))}=N^{13/220}\ge1.
\]

Integrating Chebyshev from zero to \(V_0\) is legal because \(p>2\), and gives
\(TN^{-1/2}V_0^{p-2}=TN^{-(q-p)/(2(q-2))}\). If \(W\ge V_0\), integrating the two high-level terms separately gives

\[
\int_{V_0}^W V^{p-3}\,dV\ll_p W^{p-2},\qquad
T\int_{V_0}^W V^{p-q-1}\,dV\ll_p TV_0^{p-q}.
\]

The last expression equals the low contribution in power. If \(W<V_0\), the low integral alone is no larger. This proves (B7), including its second term. There is no artificial \(O(T)\) baseline from \(V<1\), and no extension past \(p=q\) is used.

For \(p=10\), \((q-p)/(2(q-2))=3/110\), so

\[
M_{10}(H_N)\ll T^{1+\varepsilon}N^{-3/110}+T^{8\omega+\varepsilon}.
\]

The shell factor is \(T^6\), which gives the two current \(K_{10}\) terms printed in the candidate. The target has exponent \(6+10b=473/65\). Thus (B8) and both deficits in (B9) follow exactly:

\[
d_A=1-10b+(26/55)\alpha,\qquad
d_B=8\omega-10b+\alpha/2.
\]

**Dominant deficit and exact maximum, (B9)--(B10).** Their difference simplifies to

\[
d_B-d_A=8\omega-1+(3/110)\alpha.
\]

Its three slopes are \(223/110,3/110,-437/110\). Its two possible endpoint minima are respectively \(634/17875\) and \(748/17875\), both positive. This verifies \(d_B>d_A\) on the full closed band. At the lower endpoint, \(d_B=0\) and \(d_A=-634/17875\); at the upper endpoint, \(d_A=1342/17875\) and \(d_B=38/325\).

The slopes of \(d_B\) itself are \(5/2,1/2,-7/2\). Its unique maximum is therefore at \(\alpha=1-2\beta\), with value

\[
7\beta+\tfrac12-10b=7\beta-101/130.
\]

It is positive, since \(\beta>b\) already gives a lower bound \(38/325\). The exact accepted number is

\[
\beta=\frac{50\sqrt{1717}-297}{13762}.
\]

The rational bounds \(207/5<\sqrt{1717}<83/2\), verified by squaring, give \(\beta>b\) and \(\beta<889/6881\). Consequently

\[
7\beta-101/130<114009/894530<13/100.
\]

This proves the claimed strict upper bound without numerical certification. The eighth-order first-term deficit at the upper endpoint is exactly \(4334/17875>24/100\). For completeness, the fourth-order counterpart is \(10318/17875\); the sixth-order supremum is \(7326/17875\). Thus the tenth-order current certificate has the smallest stated worst deficit among the even orders \(4,6,8,10\) available in \(2<p<q\). This comparison does not establish optimality among other estimates or predict the difficulty of proving the arithmetic input.

**Added implication from the old sufficient sixth gate to the new tenth gate.** The old Round206 shell threshold, with the explicit bridge error retained, gives

\[
M_6(H_N)\ll T^{29/25-6\omega+\varepsilon},\qquad
M_{10}(H_N)\le\|H_N\|_\infty^4M_6(H_N)
\ll T^{29/25-2\omega+\varepsilon}.
\]

Relative to the desired radius exponent \(10b-\alpha/2\), the slack is
\(10b-29/25-\alpha/2+2\omega\). It is the constant \(38/325\) on the root branch, has slope \(-1/2\) on the plateau and \(-3/2\) on the high branch, and reaches zero only at \(\alpha=1-2b\). It is therefore nonnegative throughout the needed band. The old full band contains this entire new band; the previously checked inverse bridge converts the resulting radius bound to (B8). Its error terms are negligible at these positive powers. This validates the newly added implication. The candidate also correctly distinguishes it from a supposed logical ordering of the two **new** gates (B5) and (B8): comparing their current deficits alone establishes no such ordering or converse.

**Gaussian hierarchy and full-quarter scope.** Gaussian shell size is \(XH^k=T^{k+2}N^{-k/2}\). Dividing by the (B1) target gives exponent

\[
1-2kb-(k-1)\alpha/2.
\]

For \(k\ge2\) it decreases with \(\alpha\); its supremum on the required open band is \(1-(4k-2)b\). Thus \(b\ge1/(4k-2)\) suffices, including equality with the usual epsilon convention.

For \(k=3\), \(b=1/10\) requires the whole band \((2/5,4/5)\) and yields exponent \(3/10\). A theorem only on the old band \((52/125,99/125)\) requires \(4b\ge52/125\) and \(1-2b\le99/125\). Both say \(b\ge13/125\), giving exponent \(151/500\). The two missing outer pieces cannot be added without further estimates.

As fixed \(k\) tends through arbitrarily large values, \(1/(4k-2)\to0\). If the bridge, Gaussian estimate, and every complement are proved on each resulting required band, the quarter bound follows by choosing a fixed \(k\) after the desired epsilon. The candidate correctly makes these extensions explicit and does not require constants uniform for \(k\) growing with \(T\). One fixed \(k\) leaves a positive gap in this certificate; a different argument using more arithmetic information is not ruled out.

## 4. First doubtful or unproved step

No doubtful mathematical step remains in the reviewed conditional derivation. The first unproved arithmetic input is the complete actual tenth-order estimate

\[
K_{10}(N)\ll_\varepsilon T^{473/65+\varepsilon}N^{-1/2}
\quad\text{for every dyadic }T^{166/325}<N<T^{242/325},
\]

uniformly in real \(T\), with the actual signed coefficients, all positive indices, actual varying widths, masks, and errors. Equivalently one may prove its correctly normalized full radius moment gate. The existing upper bound retains the obstructing \(T^{8\omega}\) contribution; variance and the accepted tail estimate alone do not remove it.

An exact fifth convolution identity, an unsigned replacement, or success on a proper sub-band would not establish this input. Even a proof of this concrete gate gives only the stated milestone, not the quarter theorem. General-band bridge extensions and an unbounded-order program remain separate hypotheses.

## 5. Controls and outcomes

1. **Local reproduction scale — GREEN.** The required factor is \(N^{1/(4k)}\); a generic bandlimited peak of width \(N^{-1/2}\) shows why a factor-free local moment-to-supremum assertion would be false. This control concerns generic Fourier functions, not the actual arithmetic weights.
2. **Global off-window tail — GREEN.** Positive window margin, the global coefficient norm, and an arbitrarily decaying Schwartz kernel are all present. A local supremum alone would not justify this step.
3. **Jacobian and bridge error — GREEN.** The shell factor is exactly \(T^{-k-1}\); explicit errors are negligible in both directions of the concrete tenth-order transfer.
4. **Complete endpoints and complements — GREEN.** Real centers and target endpoints, dyadic dividing endpoints, singleton, high blocks, infinite tail, and sharp reconstruction error are all retained.
5. **Sixth-order comparison — GREEN.** New/old gate difference is strictly positive on the required open band; its equality endpoint is already safe.
6. **Tenth-order two-term control — GREEN.** The \(W^8\) term is not dominated by the first term here. Its deficit is the larger one everywhere and has the stated exact interior maximum.
7. **Full-quarter limitation — GREEN.** All-order conditional scope is explicit. Neither fixed sixth nor fixed tenth order is promoted into arbitrarily high moments or a full proof.

All controls are analytic or exact algebra. File hashing is provenance verification, not a numerical mathematical experiment.

## 6. Exact artifacts and final candidate hash

The following context was used for this post-report review:

- `protocol.md` (read for the original assignment and retained).
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/reviews/independent_middle_band_review.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, especially its block-tail, infinite-tail, and sharp-reconstruction statements.
- `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`, for the exact accepted \(\theta\) and inherited scope.

No new external theorem was imported, and no web search was used. The existing graph's acceptance status is inherited from the assignment and cited reviewed dependencies; this task does not modify or independently revalidate the graph.

Final reviewed candidate SHA-256:

`6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552`

This is the version containing the full (B7)--(B10) tenth-order comparison, the added old-sixth-to-new-tenth implication, the qualification that the two new gates are not logically ordered merely by their current deficits, and the corrected final reference to (B8). The complete comparison and added paragraph were independently checked before binding this review to that final hash.

## 7. Recommended state effect

**GREEN as conditional strategy evidence; no mathematical state change.** The conductor may adopt the complete (B8) gate as the next arithmetic objective after closing the current round. Preserve the full-quarter program, all inherited qualifications, and all independently open graph parents.

Only this assigned review was written. The earlier isolated report, candidate, graph, proof draft, validation matrix, shared synthesis, and other artifacts were not edited. No successor round or further task is initiated here.
