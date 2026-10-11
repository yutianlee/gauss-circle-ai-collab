# Round223: independent final-hash multiplicative-source review

- Target: reports/multiplicative_wave_sources.md in gc-full-goal-signed-source-review.
- Target SHA256: db7d52b2ebd266a9e92ae347444f6b1c0dbd99258194df07404b39c16b21ed86.
- Role: bounded post-isolation NONBLIND source/application reviewer, 2026-09-28.
- Authorship/history disclosure: this agent authored the current isolated Fourier report and the scoped conductor-control application review, and retains earlier-round history. It did not author the report under review. This review does not independently validate its own earlier reports.
- Allocation: analytical review only; zero experiments. Only the authorized report, two primary texts/status records, two accepted moment kernels and prior scoped review were used.

## 1. Result

**GREEN for the audited source statements, application costs, same-order absorption and signed spectral identity.** No necessary correction to the frozen target was found.

The two source interfaces are accurately transcribed, including both Granville--Lamzouri ranges, its fixed-\(c\) prime-bias consequence and Robles's simultaneous exceptional set. The fixed damping and its restored powers are legal. The report retains the nonlinear phase, mask, exceptional-frequency and prime-main-term problems as unproved.

The sufficient fixed-order family is valid: one-sided control of the complete distinct-class integral at \(T^{5/4+\varepsilon}\), for an unbounded sequence of fixed even orders, pays its own repeated-class terms by same-order absorption. The finite signed spectral identity has the correct normalization and a uniformly negligible tail. Its proposed inequality remains an unproved equivalent representation, not source-provided progress.

## 2. Exact review scope

The report is bound to the hash above. Its moment notation uses the actual accepted normalization

\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 B_T(R)=\sum_n a_n(T)\cos(2\pi R\sqrt n-3\pi/4),
 \tag{1}
\]

with the fixed real even Schwartz \(\Psi\), \(\Psi(0)=1\), and the fixed nonnegative window \(w(R/T)\).

This audit checks the printed statements of the two named source interfaces and the report's applications. It does not re-prove either source paper. Its inherited frontier table is a status inventory, not a new estimate or an independently revalidated graph patch; the report correctly leaves every listed owner open. No unlisted source, sibling report, current graph or strategy file was opened.

The comparison with the earlier conductor-control review is confined to the same fixed-class, damping, mask and transfer-scope issues. That earlier review is not treated as a second independent proof of this agent's Fourier lemma.

## 3. Independent derivations and seam checks

### 3.1 Source statements, ranges and current records

[Robles v1](https://arxiv.org/html/2609.11070v1) matches the report's normalized class, reduced-rational hypotheses, Theorem 1.1 majorant and Corollary 1.1 approximation range. Corollary 7.2 has the simultaneous exceptional-set bound

\[
 |\mathcal E_A(N,\lambda)|\le K_A/(N\lambda^4),
 \quad c_A/\log N\le\lambda\le1,
 \tag{2}
\]

with \(c_A=\max(6,2C(A))\) and \(K_A=2C_\varphi(2C(A))^4\), taking an admissible \(C(A)\ge1\). These are effective class-dependent constants, not numerical values or uniform constants for growing \(A\). The source explicitly keeps exceptional real characters within its scope. The report does not omit them.

[Granville--Lamzouri v1, Theorem 1.1 and Corollary 1.1](https://arxiv.org/html/2604.02306v1) require multiplicative \(|f|\le1\), fixed \(0<\delta<1/10\), the report's denominator interval and approximation error \(1/(qx)\). Writing \(\mathcal L=\exp\sqrt{\log x\log\log x}\), the two checked upper ranges for integer \(M\ge2\) are

\[
 M\ll\min\left\{
 \frac{q^{1-\delta/4}}{(\log x)^2},\mathcal L^{1/2-\delta}
 \right\}\quad(q\le x^{1-\delta}),
 \tag{3}
\]

\[
 M\ll\min\left\{
 \frac{\sqrt{x/q}}{\log x},
 \frac{x}{q\log(2x/q)(\log x)^3},
 \mathcal L^{1-\delta}
 \right\}\quad(q\ge x^{1-\delta}).
 \tag{4}
\]

Their remainders are respectively \(x/(\sqrt M\log x)\) and \(x\sqrt{\log M}/(\sqrt M\log x)\). The report's retained prime main term, fixed-\(c\) threshold, \(h\), \(z\), and bias-size formulas match the corollary. Its absolute-value interpretation of the complex prime bias is appropriate. The introductory conjectures are not imported.

The live records show only v1, dated [10 September 2026 for Robles](https://arxiv.org/abs/2609.11070) and [2 April 2026 for Granville--Lamzouri](https://arxiv.org/abs/2604.02306), with no withdrawal notice on either record at this review. A clean status record is not a verification of a theorem's proof.

### 3.2 Coefficient premise, upper norms and fixed damping

For \(g=1*\chi_4\), the three prime-power types in the report give

\[
 \sum_n g(n)^2n^{-s}
   =\frac{\zeta(s)^2L(s,\chi_4)^2}
           {\zeta(2s)(1+2^{-s})},
 \qquad
 \lim_{s\downarrow1}(s-1)^2\sum_n g(n)^2n^{-s}=\frac14.
 \tag{5}
\]

The factor at \(2\) is \((1-2^{-s})^{-1}\), as required. A fixed bound
\(\sum_{n\le x}g(n)^2\le A^2x\) would instead give at most \(A^2s/(s-1)\) by partial summation. The fixed-class rejection is rigorous and does not need a Tauberian theorem.

The report's complementary upper bound is also justified. If
\[
 H(s)=[\zeta(2s)(1+2^{-s})]^{-1}=\sum_d h(d)d^{-s},
 \tag{6}
\]
then
\[
 \sum_d|h(d)|/d
 \le\left(\sum_{m\ge1}|\mu(m)|/m^2\right)
       \left(\sum_{j\ge0}2^{-j}\right)<\infty.
 \tag{7}
\]
The disk count gives \(\sum_{n\le x}g(n)\ll x\), and hence
\[
 \sum_{n\le x}(g*g)(n)
 \ll x\sum_{m\le x}\frac{g(m)}m
 \ll x\log(2x).
 \tag{8}
\]
Convolving with \(|h|\) proves \(\sum_{n\le x}g(n)^2\ll x\log(2x)\). It follows that the two dyadic coefficient norms in the report have exactly the displayed \(N^{1/4}\) and \(N^{-1/2}\log(2N)\) powers, with arbitrary Schwartz decay after changing the fixed decay order. Masking cannot increase these absolute norms.

For fixed \(0<\eta<1/2\), partial summation of this upper bound gives
\(\sum_{n\le x}g(n)^2n^{-2\eta}\ll_\eta x^{1-2\eta}\log(2x)\ll_\eta x\).
Larger fixed \(\eta\) follows by domination by any smaller positive damping. Prime values are bounded by \(2\), and the value at \(1\) remains \(1\). Thus \(g(n)n^{-\eta}\) belongs to a fixed admissible class.

At \(\eta=3/4\), \(k+1\le2^k\le p^{3k/4}\) for split primes \(p\ge5\), while the other prime-power numerators are at most \(1\). The pointwise bound is therefore \(1\), including \(n=1\). Conversely, \(g(5)5^{-\eta}>1\) if \(\eta<\log2/\log5\), so small damping is not automatically permitted by GL. The report claims a sufficient damping, not an optimal threshold. The warning against multiplying the whole function by a length-dependent constant is valid: normalized multiplicativity is then lost.

### 3.3 Linear restoration, nonlinear transfer and omitted regions

In the favorable linear block of the report, \(q\le N/H\) implies \(q\le u/H\) for every \(u\in[N,2N]\), while the rational error bound \(q^{-2}\) does not depend on \(u\). Therefore the Robles corollary really does apply to the prefixes needed for Abel summation. The multiplier's supremum plus variation is

\[
 O_{\eta,J}\!\left(
 N^{-3/4+\eta}(1+N/T)^{-J}\right).
 \tag{9}
\]

Multiplication by the length-\(N\) prefix majorant produces exactly the report's \(N^{1/4+\eta}\) power and both logarithmic/rational-approximation terms. Real endpoints and a partial last block are handled by the same prefix formula; bounded lengths use the triangle bound. A fixed logarithmic improvement is not a fixed power saving.

The mask counterexample with \(2,p\) is valid for \(Q\ge2\):
\(\operatorname{sf}(2)=2\le Q\), whereas
\(\operatorname{sf}(p)=p>Q\) and \(\operatorname{sf}(2p)=2p>Q\).
The masked values at \(p\) and \(2p\) are nonzero, while the value at \(2\) is zero. No multiplicative or bounded-variation mask transfer follows.

The nonlinear tangent residual has scale \(TM^2N^{-3/2}\), giving the stated permissible interval length \(N^{3/4}T^{-1/2}\) and, when that length is at least one, the piece count \(T^{1/2}N^{1/4}\). Translating the index does not preserve multiplicativity or change a source prefix's length to that short length. This is correctly labelled a transfer diagnostic.

In both GL ranges, \(M\le\mathcal L^{O(1)}=x^{o(1)}\). Thus \(p>x/M>\sqrt x\) for large \(x\), giving the unique large-prime factor and its coprime complementary factor. Nevertheless the main term still requires an estimate. The largest permitted \(M\) cannot turn either generic remainder into \(O(x^{1-\sigma})\) for fixed positive \(\sigma\). None of this estimates the square-root phase.

For the Robles exceptional set, \(|S_f|\le AN\) follows from the class second moment and Cauchy. Hence
\[
 \int_{\mathcal E_A}|S_f|^p
 \le A^pK_A N^{p-1}\lambda^{-4}.
 \tag{10}
\]
At \(\lambda=c_A/\log N\), the displayed good- and bad-set prices follow whenever that threshold lies in the permitted range; bounded remaining lengths are harmless. This is an \(\alpha\)-measure statement. A weighted signed-kernel integral cannot discard its exceptional part.

The small-modulus check is exact:
\(\chi_4(n)e(n/4)=i\) for odd \(n\) and \(0\) for even \(n\).
Its sum is \(ix/2+O(1)\). The report uses it only to block deletion of a legitimate linear factor's modulus-\(4\) region, not to lower-bound the complete radial wave. GL's fixed-\(c\) corollary is not used at a shrinking physical level.

### 3.4 Same-order absorption for each fixed even order

This is the main extension beyond the twelfth-order statement in accepted216. It can be derived without intermediate-order moment inputs.

For the same actual \(Q\), write
\[
 Z=\sum_{d>Q}f_d,\qquad
 p_j(R)=\sum_{d>Q}f_d(R)^j,\qquad
 A_d=\sup_R|f_d(R)|
 \tag{11}
\]
with \(A_d\) bounded by the accepted coefficient mass. The ordered distinct-class polynomial \(E_p\) is the partition-lattice inclusion-exclusion polynomial. Its all-singleton term is \(Z^p\). Every other monomial has the form
\[
 Z^{p-r}\prod_{j\ge2}p_j^{m_j},
 \quad r=\sum_{j\ge2}jm_j\ge2,\quad
 b=\sum_{j\ge2}m_j\le r/2.
 \tag{12}
\]
There are finitely many such monomials for fixed \(p\). The accepted class-mass estimate implies, with arbitrarily small fixed losses,
\[
 \left|\prod_{j\ge2}p_j^{m_j}\right|
 \ll_{p,\varepsilon}Q^{b-3r/4+\varepsilon}
 \le Q^{-r/4+\varepsilon}.
 \tag{13}
\]

Weighted Young's inequality, including the case \(r=p\), gives for any fixed small \(\delta_0>0\)
\[
 Q^{-r/4+\varepsilon}|Z|^{p-r}
 \le \delta_0|Z|^p+
       C_{p,\varepsilon,\delta_0}
          Q^{-p/4+p\varepsilon/r}.
 \tag{14}
\]
Choose the input losses small enough for this finite collection of terms. Since \(Q\ge1\), the residual factor is bounded. After integration against \(w(R/T)\) and summing the finite monomials,
\[
 \left|M_p(Z)-I_p(T,Q)\right|
 \le \tfrac12 M_p(Z)+O_{p,\varepsilon}(T^{1+\varepsilon}).
 \tag{15}
\]
The fixed \(p\) is even, so \(Z^p=|Z|^p\). Absolute convergence of the class sums passes the finite identity to the full series.

A one-sided upper bound for \(I_p\) therefore suffices. For
\(Q=\lfloor T^{1/p}\rfloor\), the head satisfies
\[
 M_p(L_Q)\ll_p TQ^{p/4}\le T^{5/4}.
 \tag{16}
\]
The inequality \(|Z+L_Q|^p\le2^{p-1}(|Z|^p+|L_Q|^p)\) pays every mixed term. Thus the report's sufficient fixed-order family is correct. All constants may depend on the fixed order; the derivation supplies no bound for \(p=p(T)\).

### 3.5 Complete physical powers

Layer-cake integration of accepted204 at \(p>136/13\) gives
\[
 M_p(B_T)\ll T^\varepsilon
 \left(T+W^{p-2}+TW^{p-136/13}\right).
 \tag{17}
\]
The low region \(|B_T|\le1\) contributes \(O(T)\), the equality case in the second exponent gives a logarithm, and smaller fixed \(p\) gives a bounded lower-end integral. At \(p=12\), the two ceiling terms are indeed \(W^{10}\) and \(TW^{20/13}\). The low cutoff \(V_0=T^{13/125}\) produces powers \(26/25\) and \(29/25\), respectively. Neither high term is paid by the source audit.

Accepted216 supplies the actual head cost \(15/13\) and repeated-class error \(8\beta-1/5\) at \(Q=\lfloor T^{2/5}\rfloor\), with its one-sided interpretation. The report retains these costs rather than replacing them by an unsigned distinct-tuple grant.

For the sufficient family \(M_p(B_T)\ll T^{5/4+\varepsilon}\), the accepted amplitude \(\sqrt R\) and Jacobian \(dx=2R\,dR\) give
\[
 \int_{Y/2}^{3Y}|P(x)|^p\,dx
 \ll T^{1+p/2}M_p(B_T)+T^{2+p/2+\varepsilon},
 \quad Y=T^2.
 \tag{18}
\]
The persistence argument then yields
\[
 \frac{p/2+9/4}{2(p+1)}
   =\frac14+\frac7{8(p+1)}.
 \tag{19}
\]
An unbounded sequence of fixed even orders suffices for quarter with arbitrary epsilon. At the twelfth milestone \(29/25\), the corresponding calculation gives \(102/325\), not quarter.

### 3.6 Exact signed spectral identity and all tails

Let \(H_T=\lfloor T^{3/2}\rfloor\). Opening the two finite polynomials in the report and integrating over \([0,1]\) enforces equality of their indices:
\[
 \begin{split}
 4\int_0^1F_{\eta,H_T}(\alpha)K_{T,R,Q}(\alpha)\,d\alpha
 =4\sum_{n\le H_T}
 &g(n)n^{-\eta}m_Q(n)n^{-3/4+\eta}
       \Psi(\sqrt{n/T})\\
 &\times\cos(2\pi R\sqrt n-3\pi/4).
 \end{split}
 \tag{20}
\]
The factors \(e(n\alpha)\) and \(e(-n\alpha)\) have opposite signs. The two powers of \(n^\eta\) cancel, and \(4g=r_2\). The integral is already real; taking its real part is harmless and keeps the exact real pairing visible.

Since the mask is bounded by one and the cosine by one, the absolute omitted tail is uniformly
\[
 \sum_{n>H_T}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
       =O_A(T^{-A})
 \tag{21}
\]
for every fixed \(A\), uniformly in real \(R\) and every \(Q\). The floor in \(H_T\), a partial final dyadic block and any empty support do not change this estimate. Also the whole absolute coefficient mass is \(O_\varepsilon(T^{1/4+\varepsilon})\), uniformly after masking.

If the truncated real expression is \(Z_Q+E\), then
\[
 \int w(R/T)\left|(Z_Q+E)^p-Z_Q^p\right|\,dR
 \ll_{p,\varepsilon}
 T^{1-A+(p-1)/4+\varepsilon}+T^{1-pA}.
 \tag{22}
\]
The report's choice \(A>(p-1)/4+2\), followed by a sufficiently small input epsilon, makes this harmless. The choice is fixed after \(p\) is fixed. The small-class estimate (16) then completes the stated implication from its proposed spectral inequality to the full moment family.

All exceptional, major-arc and minor-arc pieces remain inside the same real \(p\)-th power. No estimate for a separate kernel norm is smuggled into (20). The identity is exact up to the paid tail; its desired inequality is still unproved. It neither grants an optimal discrete norm nor transfers an absolute Fourier-mass lower bound to an actual signed sum.

## 4. First doubtful or unproved step

No necessary repair was identified within the assigned seams. The first unproved analytic step is exactly the proposed complete signed spectral inequality: neither source bounds its actual masked, nonlinear kernel interaction, its exceptional-frequency contribution or all its mixed products at the required moment power.

The source formulas alone do not imply that inequality. The report states this explicitly. Its recommendation is a conditional complete objective, not a newly established mechanism or estimate. The earlier absolute-transfer certificate remains only a scoped comparison and is not used as a universal signed obstruction here.

## 5. Controls and outcome

| Control | Outcome |
|---|---|
| Versioned source formulas | GREEN: Robles theorem/corollary/exceptional constants and both GL ranges agree with the exact v1 texts. |
| Prime-bias consequence | GREEN under its fixed-\(c\), one-bounded and rational-approximation hypotheses; no shrinking-threshold import. |
| Source status | Both current histories show only v1 and no withdrawal notice; this is a record check, not proof validation. |
| Coefficient and damping | GREEN: double-pole failure, logarithmic mean-square upper bound, fixed damping and the \(3/4\) bound are correct. |
| Restored linear weights | GREEN: prefix ranges, multiplier variation, real endpoints and the \(N^{1/4+\eta}\) factor are paid. |
| Mask/nonlinear/exceptional complements | GREEN as limitations: none is removed or declared source-controlled. |
| Same-order absorption | GREEN by (12)--(16), with one-sided \(I_p\), fixed even order and all repeated partitions. |
| Physical powers | GREEN: both ceiling terms, the two twelfth-order lower-cutoff powers, amplitude/Jacobian and final exponent are retained. |
| Signed spectral identity and tails | GREEN: factor \(4\), opposite Fourier signs, exact real pairing, all cutoffs and the fixed-\(p\) tail error checked. |
| Scope | No actual signed lower bound, complete frontier improvement or graph promotion follows. |

No mathematical experiment or third source survey was used.

## 6. Dependencies and provenance

| Exact local artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| Current223 reports/multiplicative_wave_sources.md | db7d52b2ebd266a9e92ae347444f6b1c0dbd99258194df07404b39c16b21ed86 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| Current223 reviews/independent_linear_transfer_review.md, authored by this reviewer | 0b371eeb6bc28535346e4d2375d29c749140a2a0b0d74aea661487891dbd5e42 |

External reads were restricted to [Robles2609.11070v1](https://arxiv.org/html/2609.11070v1), [Granville--Lamzouri2604.02306v1](https://arxiv.org/html/2604.02306v1), and their versioned/current arXiv status records. Their statement and application seams were checked; their complete proofs were not re-audited. The inherited graph/strategy artifacts named inside the target report were not independently opened under this task.

The same-order partition argument and finite spectral/tail calculations above were rederived for this review. Prior authorship and post-isolation status are disclosed rather than presented as fresh history-free independence.

## 7. Recommended state effect

Retain the frozen report as **GREEN source/application evidence with no complete analytic gain**. No same-round correction is required by this review. The source premises, costs and proposed full-family implication are valid within their stated ranges.

Do not promote the proposed spectral inequality, a moment improvement, a pointwise exponent or any M1/M2/GAR owner. No shared state or successor artifact was edited. This bounded review stops with its final hash.
