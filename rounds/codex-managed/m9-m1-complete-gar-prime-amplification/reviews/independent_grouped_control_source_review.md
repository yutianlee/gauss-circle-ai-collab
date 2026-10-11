# Round 224: independent grouped-control and source review

## 1. Result

**GREEN in the stated certificate scope; no repair required.** This review binds controls/conductor_grouped_prime_commutator_control.md at SHA-256

34699ab1435e5511d8a586ec1aed17d8a35d2755893231595ab1ccced4c3bb5d.

The lower bound survives aggregation over all divisors and amplifier primes before the coefficient absolute value. Its constants, repeated-prime cases, literal profile geometry and finite cutoff are correct. The asymptotic corollary uses only prime counting in the fixed residue class \(1\bmod4\), with uniformity justified below.

This is a post-report, nonblind review of the conductor's control. I authored the earlier isolated finite-allocation report, which remains unchanged; that authorship is disclosed and is not presented as independent review of my own work. The present control has a different claimant. Retained earlier agent history is also disclosed. No other task report was read.

## 2. Exact statement and hypotheses

Use the actual fixed-centre array
\[
 A_X(h,q)=\sum_j\mathbf1_{h\le H_j}\Phi(h/(H_j+1))
                  [w_j(2Y\sqrt{h/q})]^*,
\quad
 Y=\sqrt X,\ R=X^{1/4},\ y=\lfloor Y\rfloor,
\quad D_j=2^{-j}y,\ H_j=\lfloor D_j/R\rfloor.
\]
The accepted profile facts needed here are nonnegativity, support
\(1/2\le d/D_j\le3/2\), the sole hard top at \(y\), inactive bottom below \(C_bR\), and the active partition sum one on \(C_bR<d<y\). The accepted 121 candidate supplies precisely this support/height/partition geometry. The relevant graph nodes certify the actual partition and the stated GAR coefficient, rather than an unrestricted divisor function.

The taper's accepted formula and endpoint continuation give \(0\le\Phi\le1\) and \(\Phi(0)=1\). For completeness, on \(0<u\le1/2\), \(0\le\pi u\cot(\pi u)\le1\) bounds
\(\Phi(u)=\pi u(1-u)\cot(\pi u)+u\) between zero and one. The identity \(\Phi(1-u)=1-\Phi(u)\) handles the other half. Continuity permits the fixed choice of \(s\) in the control.

Fix \(\delta=1/20\), this \(s>0\), a nonempty finite split-prime set \(\mathcal P\), \(k=|\mathcal P|\), \(P=\max\mathcal P\), and real \(M\ge10\) satisfying
\[
 P(1+\delta)^2M^2\le sY.
\]
The finite conclusion is
\[
 \mathcal C_X(\mathcal P)\ge
 \frac7{40}(1+\delta)^{-3/2}v(M)(v(M)-1)M^{-3/2},
\]
with exactly the control's grouped coefficient modulus and inclusive prime interval. In particular, this need not be positive when \(v(M)\) is zero or one.

## 3. Independent derivation and source audit

### Actual coefficients and the three allocations

For distinct split primes \(a,b\in[M,(1+\delta)M]\), the four divisors of \(ab\) have first coordinates \(1,a,b,ab\). At \(h=a,b\), \(q/h\le1+\delta<4\), so \(d=2Y\sqrt{h/q}>Y\ge y\); the \(h=ab\) allocation is also outside the profile support. Thus
\[
 c_X(ab)=A_X(1,ab)\in[0,1].
\]
All divisors of \(pab\), or of the integer \(ab/p\) when it exists, have character value one. Their coefficients are sums of nonnegative actual allocations.

Set \(m=pab\). The three retained allocations have first coordinates \(1,a,b\), hence are distinct even when \(p=a\) or \(p=b\). They are actual divisors of the same \(m\), not three labels for one divisor. Condition (2) of the control gives \(m\le sY\), and all three satisfy
\[
 d=\frac{2Yh}{\sqrt m}\ge\frac{2R}{\sqrt s}>C_bR.
\]
At the latter two allocations,
\[
 \frac dY\le2\sqrt{\frac{1+\delta}{5}}=\frac{\sqrt{21}}5<\frac{11}{12}.
\]
At \(h=1\), \(p\ge5\) and \(ab\ge100\) give an even smaller upper bound. Therefore, for example \(X\ge256\) suffices for \(d<y\) uniformly: \(Y\ge16\) and \(d<Y-1\le y\). This supplies an absolute hard-top buffer independent of \(p,a,b,M\). The inactive bottom is excluded by the other strict inequality. No hard-top star value is encountered.

Whenever \(w_j(d)\ne0\),
\[
 \frac{hR}{D_j}\le\frac{3hR}{2d}
 =\frac{3\sqrt m}{4R}\le\frac34\sqrt s<\frac12.
\]
Consequently \(D_j/R>2h\), so the literal integer height includes \(h\), and
\[
 \frac{h}{H_j+1}<\frac{hR}{D_j}\le\frac34\sqrt s.
\]
The floor is used exactly, including when \(D_j/R\) is an integer. Every contributing taper is at least \(9/10\). Nonnegative partition weights sum to one, giving \(A_X(h,q)\ge9/10\) at each retained allocation. All other allocations and the backward coefficient are nonnegative, including when \(p=a\) or \(p=b\). Hence
\[
 c_X(pab)+c_X(ab/p)-2c_X(ab)\ge3\cdot\frac9{10}-2=\frac7{10}.
\]
The proof keeps \(A_X\) fixed throughout.

### Both aggregations and normalization

The same semiprime set works simultaneously for every \(p\in\mathcal P\). Thus at each such \(n=ab\), the already divisor-summed, prime-summed defect is at least \(7k/10\). Unique factorization gives exactly \(v(M)(v(M)-1)/2\) distinct products of unordered distinct pairs. Repeated-prime amplifier incidences do not change this count.

Each product satisfies \(ab\le sY/P<16Y\), and, being integral, lies in the literal cutoff \(ab\le\lfloor16Y\rfloor\). Here the prescribed bound \((3/4)\sqrt s<1/2\) already implies \(s<4/9\), and \(P\ge5\). Also
\[
 (ab)^{-3/4}\ge(1+\delta)^{-3/2}M^{-3/2}.
\]
The remaining factors are
\[
 \frac1{2k}\cdot\frac{7k}{10}\cdot\frac{v(M)(v(M)-1)}2
 =\frac7{40}v(M)(v(M)-1).
\]
Dropping other \(n\)'s from the nonnegative absolute certificate is legitimate. This step takes no absolute value inside either aggregation.

### The one external statement and uniformity

The introduction of [Tao's 24 September 2009 exposition](https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/) states the prime number theorem for fixed coprime \(a,q\), with error tending to zero as the counting parameter grows and allowed dependence on \(q\). Specializing to \(a=1,q=4\) gives the control's \(t/(2\log t)\) asymptotic. This review uses that stated known theorem, not the later heuristic discussion.

Inclusive endpoints satisfy exactly
\[
 v(M)=\pi((1+\delta)M;4,1)-\pi(M;4,1)
             +\mathbf1_{\{M\text{ is a split prime}\}}.
\]
For fixed \(\delta>0\), subtraction therefore gives
\[
 v(M)=\frac{\delta M}{2\log M}+o(M/\log M).
\]
The extra endpoint term is at most one. Hence for all sufficiently large \(M\), \(v(M)\ge c_\delta M/\log M\) and \(v(M)\ge2\); inserting this in the finite bound proves (10). No density claim is made for each finite \(M\).

For fixed \(0<\eta<1/2\), the control's choice
\[
 M=\frac{\sqrt s}{1+\delta}X^{1/4}P^{-1/2}
\]
has \(M\ge c_sX^{\eta/2}\) whenever \(P\le X^{1/2-\eta}\). Thus \(M\to\infty\) uniformly over all admissible sets and maxima, after an \(X\)-threshold depending on the fixed \(\eta,s,\delta\). In particular \(M\ge10\) and the preceding prime-count threshold hold uniformly. Also \(P\ge5\) gives \(M\le c_sX^{1/4}\), so \(\log M\le\log X\) for large \(X\). Therefore
\[
 \frac{M^{1/2}}{(\log M)^2}
 \gg_{s,\delta}\frac{X^{1/8}P^{-1/4}}{(\log X)^2}.
\]
This verifies (11). The statement for fixed \(\eta\ge1/2\) is eventually vacuous, since a nonempty split-prime set has \(P\ge5\). No uniformity as \(\eta\downarrow0\) is claimed. The arithmetic modulus stays four and the relative interval length stays \(\delta\); \(P\) is neither of these. No count of amplifier primes is used.

## 4. First doubtful or unproved step

No gap remains in the finite grouped-coefficient bound or its stated asymptotic consequence. Constants involving the fixed accepted profiles and the chosen fixed \(s\) are harmless; the asymptotic threshold may depend on \(\eta\).

The missing application step is still a bound on the complete signed main-minus-correction expression, with the radial phases and the prescribed real part retained. A lower bound for this coefficient absolute certificate is not a lower bound for that expression, for \(G_X\), or for physical M1. The physical normalization contributes \((4/\pi)X^{1/4}\) to a corresponding sufficient certificate, with the inherited reconstruction errors retained; it does not reverse the triangle inequality.

No conclusion is supplied outside the stated prime range, nor against another norm or a coefficient-sensitive joint estimate. Prime \(2\) is absent from the witness and amplifier, while its original character-zero convention remains part of the complete target.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Accepted actual profile and taper | GREEN; fixed nonnegative profile, exact partition and taper range retained. |
| Literal \(D_0=y,D_1=y/2\), heights and stars | GREEN; strict interior inequalities precede use of floors and partition. |
| \(p=a\), \(p=b\), repeated powers | GREEN; three distinct first coordinates; backward coefficient retained. |
| Divisor aggregation | GREEN; all relevant character values equal one. |
| Prime aggregation | GREEN; common witness products have the same positive sign for every prime. |
| \(7/10\) and \(7/40\) constants | GREEN by the displayed arithmetic and unordered-pair count. |
| Finite \(v(M)\), empty witness, cutoff | GREEN; no positive claim for \(v(M)<2\), inclusive integer cutoff preserved. |
| Fixed-modulus source premise | GREEN for \(a=1,q=4\), with fixed \(\delta\). |
| Uniform asymptotic corollary | GREEN for each fixed \(\eta>0\), interpreted asymptotically as above. |
| Signed/physical scope | GREEN; no actual wave lower bound or complete owner closure inferred. |

Zero experiments. The only web access was the assigned Tao source; no linked source or source proof was audited.

## 6. Dependencies and exact artifacts used

Campaign: m9-m1-complete-gar-prime-amplification. Round: 224. Role: independent_grouped_control_source_review. Date: 28 September 2026, Asia/Shanghai. Claimant: conductor; reviewer: reused temporary agent after completing its isolated report.

| Artifact | SHA-256 |
|---|---|
| controls/conductor_grouped_prime_commutator_control.md | 34699ab1435e5511d8a586ec1aed17d8a35d2755893231595ab1ccced4c3bb5d |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| briefs/conductor_actual_gar_interface.md | f5ea5afa70e8315179d56d066303bb17b1280b4fabd2bbfb5867aece531bd803 |
| strategy/round224_complete_gar_split_prime_amplification.md | c1f2364a958d484f523745bc06711aaebaf049c1c989f73639c55a48590da9a5 |
| rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md | 6a60d62ff42c5b764a79e4303eb50b8a780572ef4ac6e635ff9406e9192d095d |
| state/proof_obligations.yml, restricted profile/interface lookups | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |

The relevant graph checks were the actual dyadic-weight certificate, Phi regularity and GAR coefficient/reconstruction interfaces. The accepted 121 argument was used for its support and floor geometry, not to substitute a flattened coefficient for \(A_X\). The exact Tao source and audited premise are identified in Section 3. No other task reports, shared-state edits or successor work were used.

## 7. Recommended state effect

Retain the control as **scoped GREEN actual-coefficient evidence** after this mathematical and source review. It tests the grouped absolute-coefficient procedure in the printed range. It proves no complete signed estimate, graph promotion or exponent gain. No shared state is changed. Stop after freezing this review.
