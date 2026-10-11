# Round223: independent review of the conductor's linear-transfer application

- Role: post-isolation, nonblind application reviewer.
- Prior history: this agent authored the round223 isolated Fourier report and held earlier-round roles. This review does not count as an independent review of that authored report.
- Target: controls/conductor_linear_source_transfer_control.md.
- Exact target SHA256: 44c4ba5ce40402b3c0c88c65d75c41ad14e55cb5e8186ddcf38aab5bf9446288.
- Generated: 2026-09-28. Analytical review only; no experiments, shared-state edits or successor work.

## 1. Result

**GREEN for the control's stated scope.** I find no mathematical correction necessary. The undamped coefficient fails the fixed mean-square class, fixed positive damping repairs that class, and the squarefree cutoff is not multiplicative. The actual smooth family on the selected scale has the uniform bounds needed for its Fourier estimate.

All normalization factors give the displayed lower price

\[
 \mathcal C\gg_\eta
       \frac{R^{1/2}N^{1/2+\eta}}{\log N}.
 \tag{1}
\]

This verdict depends on the control's explicit hypothesis that the selected legal majorant retains a positive \(N/\log N\) floor at every frequency. It is a lower bound on that named absolute upper certificate, not on the actual sum, signed periodization, optimal discrete norm, or every legal source application. The control makes these distinctions correctly.

## 2. Exact reviewed statement and hypotheses

Let \(f=1*\chi_4=r_2/4\), fix \(\eta>0\), and put \(g_\eta(n)=f(n)n^{-\eta}\). The source class has a fixed constant \(A\), normalized multiplicativity, bounded prime values, and a linear second-moment bound for every real \(x\ge1\).

The application uses the fixed actual real even Schwartz function \(\Psi\), with \(\Psi(0)=1\), and a fixed nonzero nonnegative \(\omega\in C_c^\infty((1,2))\). The selected scales are

\[
 R\asymp T,\qquad N\asymp T^{2/3},\qquad T\longrightarrow\infty,
 \tag{2}
\]

with fixed positive comparison constants. Its complex block is

\[
 U(R)=4\sum_{n\ge1}f(n)n^{-3/4}\omega(n/N)
                  \Psi(\sqrt{n/T})e(R\sqrt n).
 \tag{3}
\]

The reviewed certificate assumes a legal nonnegative majorant \(B(\alpha)\ge|S(\alpha)|\) on the whole circle, including any exceptional complement, and additionally

\[
 B(\alpha)\ge c_\eta N/\log N.
 \tag{4}
\]

The constants may depend on the fixed \(\eta,\omega,\Psi\) and scale-comparison constants, but not on \(T,R,N\). No uniformity as \(\eta\to0\) is claimed.

## 3. Independent application checks

### 3.1 Euler factors and the double-pole obstruction

The prime-power values are

\[
 f(2^k)=1,\qquad
 f(p^k)=k+1\ (p\equiv1\pmod4),\qquad
 f(p^k)=\mathbf1_{2\mid k}\ (p\equiv3\pmod4).
 \tag{5}
\]

For \(t=p^{-s}\), the corresponding square-coefficient factors are
\((1-t)^{-1}\), \((1+t)(1-t)^{-3}\), and \((1-t^2)^{-1}\).
Consequently, for real \(s>1\),

\[
 D(s):=\sum_{n\ge1}f(n)^2n^{-s}
 =\frac{\zeta(s)^2L(s,\chi_4)^2}
        {\zeta(2s)(1+2^{-s})}.
 \tag{6}
\]

The product is absolutely convergent there: the local coefficients are \(O((k+1)^2)\), and the nonconstant prime contribution is \(O(p^{-s})\). In particular, the factor at \(2\) in the displayed quotient reduces to \((1-2^{-s})^{-1}\); it has not been lost.

Using \(L(1,\chi_4)=\pi/4\) and \(\zeta(2)=\pi^2/6\),

\[
 D(s)\sim \frac{1}{4(s-1)^2}\qquad(s\downarrow1).
 \tag{7}
\]

If \(\sum_{n\le x}f(n)^2\le A^2x\) for all \(x\ge1\), exact partial summation gives

\[
 D(s)=s\int_1^\infty
          \left(\sum_{n\le x}f(n)^2\right)x^{-s-1}\,dx
       \le A^2\frac{s}{s-1},
 \tag{8}
\]

contradicting (7). This argument needs no Tauberian theorem or asymptotic formula for the partial sums. It proves precisely the fixed-class failure asserted by the conductor.

### 3.2 Fixed damping and the \(3/4\) check

For each fixed \(\eta>0\), the elementary divisor estimate
\(\tau(n)\le C_\eta n^{\eta/2}\) implies

\[
 0\le g_\eta(n)\le C_\eta n^{-\eta/2}\le C_\eta.
 \tag{9}
\]

To verify the constant, for sufficiently large primes \(p\), \(p^{\eta/2}\ge2\) and \(k+1\le2^k\le p^{\eta k/2}\). For each of the finitely many remaining primes, \(\sup_{k\ge0}(k+1)p^{-\eta k/2}\) is finite. Multiplying these finitely many constants proves the estimate.

Thus \(g_\eta(1)=1\), multiplicativity is preserved, its prime values are bounded, and
\(\sum_{n\le x}|g_\eta(n)|^2\le C_\eta^2x\).
Taking \(A_\eta\ge\max(1,C_\eta)\) satisfies both source-class conditions.

At \(\eta=3/4\), a split prime has \(p\ge5\), so
\(k+1\le2^k\le p^{3k/4}\). At \(2\) and the inert primes the numerator is at most one. Therefore \(0\le g_{3/4}(n)\le1\) for every \(n\), including \(n=1\). Its class constant can be \(A=1\).

The source allows functions to vary with parameters while remaining in a fixed class; that does not make a growing class constant legal. Multiplying \(g_\eta\) by \(N^\eta\) is not a free repair of the extracted prefactor: in general it already changes the value at \(1\) from \(1\) to \(N^\eta\). The control correctly keeps \(\eta\) fixed.

### 3.3 Narrow primary-source premise

[Robles, arXiv:2609.11070v1, Theorem 1.1](https://arxiv.org/html/2609.11070v1) uses normalized multiplicative \(f\) with
\(|f(p)|\le A\) and \(\sum_{n\le x}|f(n)|^2\le A^2x\).
At length \(M\ge3\), put \(Q_0=M/(\log M)^3\). For a reduced approximant \(\alpha=a/r+\beta\), \(r\le Q_0\), \(|\beta|\le(rQ_0)^{-1}\), it states

\[
 |S_f(M,\alpha)|\ll_A
       \frac{M}{\log M}
       +\frac{M}{\sqrt{\varphi(r)\max(1,M|\beta|)}}.
 \tag{10}
\]

Its constant is uniform under those hypotheses. The paper's real upper limits mean their floors. These are linear-phase hypotheses; (10) supplies neither an unconditional \(M/\log M\) bound at every frequency nor a square-root-phase bound. This is the only source premise audited here, not a re-audit of the paper's proof or further theorems.

### 3.4 Actual profile uniformity and exact rescaling

Set \(q=N/T\), \(\lambda=R\sqrt N\), and

\[
 W_{T,N}(x)=x^{\eta-3/4}\omega(x)\Psi(\sqrt{qx}),
 \qquad F(x)=W_{T,N}(x)e(\lambda\sqrt x).
 \tag{11}
\]

The two accepted kernels cited by the control give the same \(\Psi(\sqrt{n/T})\), the identity \(r_2=4(1*\chi_4)\), and the real-even Schwartz normalization \(\Psi(0)=1\). On (2), \(q\to0\). Since \(x\) stays in a fixed compact subset of \((1,2)\), differentiating \(\Psi(\sqrt{qx})\) any fixed number of times gives uniform bounds. Indeed evenness and smoothness imply convergence to \(1\) in each fixed \(C^j\) norm on this interval. Thus

\[
 W_{T,N}\longrightarrow x^{\eta-3/4}\omega(x)
       \quad\text{in each fixed }C^j\text{ norm}.
 \tag{12}
\]

The limiting function is nonzero. Therefore the \(L^2\) norms are uniformly bounded below for sufficiently large \(T\), all needed derivative bounds are uniform, and the common compact support has a fixed gap from both endpoints. The curvature of \(\sqrt x\) has a fixed nonzero lower bound there.

These verified family bounds justify the control's uniform Fourier estimate directly: the monotone-curvature integral bound gives
\(\|\widehat F\|_\infty\ll\lambda^{-1/2}\), while Parseval gives \(\|\widehat F\|_2^2\gg1\). Hence \(\|\widehat F\|_1\gg\sqrt\lambda\).
Cauchy--Schwarz on a band of length \(O(\lambda)\), and repeated integration by parts with derivative bounded away from zero outside an enlarged band, give the reverse bound. In the tail, \(\lambda/|u|\) is bounded, so the derivative constants in \(O_j(|u|^{-j})\) are uniform in this family. Therefore

\[
 \|\widehat F\|_1\asymp\sqrt\lambda
       =R^{1/2}N^{1/4}.
 \tag{13}
\]

This checks the conductor's family extension; it is not an independent review of my earlier authored fixed-profile lemma.

For each positive integer \(n\),

\[
 N^{\eta-3/4}g_\eta(n)F(n/N)
 =f(n)n^{-3/4}\omega(n/N)
          \Psi(\sqrt{n/T})e(R\sqrt n).
 \tag{14}
\]

Thus the factor \(4N^{\eta-3/4}\) is exact. Let \(M=\lfloor2N\rfloor\) and \(S(\alpha)=\sum_{1\le n\le M}g_\eta(n)e(n\alpha)\). Compact support of \(\omega\) makes every omitted term vanish. Fourier inversion and periodization give

\[
 U=4N^{\eta-3/4}\int_0^1G(\alpha)S(\alpha)\,d\alpha,
 \quad
 G(\alpha)=\sum_nF(n/N)e(-n\alpha),
 \quad
 \int_0^1A=\|\widehat F\|_1.
 \tag{15}
\]

The signs, the single factor \(N\) in the defining periodization, and the external factor \(4\) are consistent.

### 3.5 Prefactors, endpoint floors, exceptions and the certificate floor

At large \(N\), \(M=\lfloor2N\rfloor\asymp N\) and
\(M/\log M\asymp N/\log N\). The source hypotheses must be tested at this actual length, or at the equivalent real upper limit \(2N\); the floor does not alter any power or logarithmic scale. The smooth compact support introduces no sampled boundary correction. Finitely many small scales can be absorbed in constants; the selected asymptotic family has \(M\ge3\).

Under the explicit global floor (4),

\[
 \begin{split}
 \mathcal C
 &=4N^{\eta-3/4}\int_0^1A(\alpha)B(\alpha)\,d\alpha\\
 &\gg_\eta N^{\eta-3/4}\frac{N}{\log N}
                 R^{1/2}N^{1/4}
 =\frac{R^{1/2}N^{1/2+\eta}}{\log N}.
 \end{split}
 \tag{16}
\]

At (2), this is \(T^{5/6+2\eta/3}/\log T\). The coefficient triangle is at most \(N^{1/4+\varepsilon}\), since \(r_2(n)\ll_\varepsilon n^\varepsilon\), the support contains \(O(N)\) terms, and all displayed smooth factors are uniformly bounded. The accepted bound \(\sum_{n\le x}r_2(n)\ll x\) even removes the epsilon on this fixed block, but that strengthening is unnecessary.

If the source estimate is used only on \(E\subset[0,1]\), the complement \(\int_{E^c}A|S|\) must be paid. The control explicitly requires legal fallbacks and the floor (4) everywhere. Such a construction is possible with a sufficiently large class-dependent triangle majorant on the complement; it is not forced for every other construction. In particular, a sharper coefficient-specific cap may fall below \(N/\log N\), in which case (4) no longer describes that certificate. The control expressly leaves that possibility open.

Since the coefficients of \(U\) are real, the corresponding selected cosine block is \(\Re(e(-3/8)U)\), or equivalently the correctly paired half-sum of the positive and negative frequencies. An upper bound for \(U\) therefore suffices; no lower bound for that real part follows. No additional physical bridge prefactor is asserted by the control's bound for \(U\).

### 3.6 Mask and signed/discrete scope

For \(Q\ge1\), choose an odd prime \(p\equiv1\pmod4\), \(p>Q\). Then

\[
 \operatorname{sf}(4)=1,\quad
 \operatorname{sf}(p)=\operatorname{sf}(4p)=p,
 \quad (4,p)=1,
 \tag{17}
\]

\[
 f_Q(4)=0,\qquad f_Q(p)=2,\qquad f_Q(4p)=2.
 \tag{18}
\]

The multiplicativity equation fails. Damping changes the last nonzero value to \(2(4p)^{-\eta}\), so it does not repair the failure. Also \(f_Q(1)=0\) violates the normalized source definition. This refutes direct substitution, not every expansion or separate estimate for the mask.

The alias control is correctly stated: at \(N=1\) with only sample \(1\),
\(G(\alpha)=W(1)e(\lambda)e(-\alpha)\), so
\(\|G\|_1=|W(1)|\) although \(\int A\asymp\sqrt\lambda\).
It is a general analytic scope control, not an assertion about this arithmetic coefficient block. It prevents interpreting (16) as a signed-kernel or optimal discrete lower bound. The favorable unmasked block does not by itself prove a lower certificate for every possible masked construction.

## 4. First doubtful or unproved step

No unsupported step remains in the narrow conductor claims as written. The first unavailable extension would be to remove the explicit hypothesis (4), discard an exceptional complement, let \(\eta\) or the class constant vary without control, substitute \(f_Q\) directly into the multiplicative theorem, or turn the absolute certificate floor into a lower bound for a signed sum.

The conductor states none of these extensions. It supplies no new complete nonlinear, masked, wave or moment estimate. The narrow source inspection above is not an independent verification of the source theorem's proof.

## 5. Controls and verdicts

| Seam | Verdict |
|---|---|
| Euler factors, including the prime \(2\) | GREEN; (6) and leading double-pole coefficient \(1/4\). |
| Fixed-class contradiction | GREEN; exact partial summation yields only a simple-pole upper bound. |
| Damping and normalization | GREEN for fixed \(\eta>0\); both class conditions verified. |
| Pointwise \(g_{3/4}\le1\) | GREEN, including all prime-power types and \(n=1\). |
| Masked multiplicativity | GREEN; the coprime \(4,p\) counterexample remains after damping. |
| Actual moving smooth family | GREEN on \(N\asymp T^{2/3}\), by uniform smooth convergence and a positive \(L^2\) buffer. |
| All prefactors | GREEN; \(4N^{\eta-3/4}\), \(N/\log N\), and \(R^{1/2}N^{1/4}\) give (16). |
| Floors and exceptional frequencies | GREEN within the explicitly required legal global majorant; no complement deleted. |
| Signed/absolute and discrete distinction | GREEN; only the named certificate has the proved floor. |
| Authorship and isolation | Disclosed. This is a post-isolation review of the conductor's application, not self-validation of the authored blind report. |

No requested correction to the frozen control is necessary.

## 6. Dependencies and exact artifacts used

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| Current223 controls/conductor_linear_source_transfer_control.md | 44c4ba5ce40402b3c0c88c65d75c41ad14e55cb5e8186ddcf38aab5bf9446288 |
| Current223 briefs/blind_oscillatory_transfer_statement.md | 8f22f707e3ee85bb8438e11eff55613cba31a227a7b5a3b113bf35b12a087ea5 |
| Current223 reports/blind_oscillatory_transfer.md, authored by this reviewer | 2d630317cdf25d30fbec3705941ee6aa4fe664b457cc6acfdea9992913595f0e |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |

The sole external source read was [Robles2609.11070v1](https://arxiv.org/html/2609.11070v1), for the fixed-class definition, Theorem 1.1's displayed majorant and endpoint convention. No further source, sibling or application file was read. The two accepted kernels were consulted only for their stated \(r_2\), mollifier and wave conventions. The graph was not opened for this review.

## 7. Recommended state effect

Retain the frozen conductor control as **GREEN scoped application evidence**. No mathematical state promotion follows from it: the fixed damping is a valid coefficient repair, while the displayed source transfer is too expensive only in the precisely named absolute certificate.

Keep the signed, coefficient-specific and differently transferred possibilities open. This review changes neither the frozen objective nor any accepted moment or pointwise exponent. The assigned review ends with this file and its final hash.
