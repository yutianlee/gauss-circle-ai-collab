# Li--Yang strict primary-source audit

## 1. Result

**Result: the narrow final Gauss-circle theorem is certifiable only with an explicit audit patch; the literal arXiv source is not clean enough to quote without that patch.** More precisely, Li and Yang's Theorem 1.2 can be reconstructed as

\[
 \sum_{m^2+n^2\le X}1-\pi X
 \ll_\varepsilon X^{\theta_{\rm LY}+\varepsilon},
 \qquad
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots ,
 \tag{1.1}
\]

uniformly for real \(X\ge 2\). This is exactly the inclusive discrepancy used in the project. The proof reconstruction requires the corrections and two restricted-range supplements recorded below. It does not certify every intermediate result in the generality in which Li--Yang state it.

The disputed height condition is resolved, not guessed: the intended condition in Case (A) is

\[
 H\ge M^{-9}T^4(\log T)^{171/140}
 \quad\hbox{if }M<T^{7/16}.
 \tag{1.2}
\]

The minus sign in Definition 4.1, (4.4), is a typographical error. Both arXiv versions, their source TeX, and their rendered PDFs retain \(M<T^{-7/16}\), but (i) Li--Yang's own final application (5.11), (ii) every ensuing Case I/Case II implication, and (iii) Bourgain--Watt v1, Theorem 3(A), (4.3), all have and require \(+7/16\). The negative version is also vacuous for the relevant large \(M\ge1\).

Three further literal defects also have unique local repairs:

- (5.18) must read \(H=MT^x\), not \(H=MT^{-x}\), because \(x\in(-3/8,-\theta_{\rm LY}]\) and every substitution from (5.22) onward uses \(H/M=T^x\).
- The two identical sawtooth terms in Li--Yang's printed circle identity cannot be correct. Bourgain--Watt v1 (7.2) gives the exact two-sign, two-range identity used by the argument.
- The isolated \(\sqrt{-1-14x}\) in (5.27) must be \(\sqrt{-1-8x}\), as in (5.25), (5.26), (5.28), and the direct algebra.

There are also two genuine overstatements, rather than mere character slips. First, Proposition 3.1 omits the Guth--Maldague hypothesis \(\beta _2\ge0\). Second, the general Case (B) reduction in Theorem 4.2 omits a logarithmic factor when asserting \(N_B>N_A\). Neither general statement is certified as printed. Both missing checks do hold, with polynomial slack, on the narrower parameter range actually used to prove (1.1); Section 3 gives exact repairs. Thus the recommendation is **revise** the source card and promote only the narrow final theorem after an independent seam review, not promote Proposition 3.1 or Theorem 4.2 in their full printed generality.

If accepted, (1.1) improves the external global pointwise baseline and is strictly below \(1/3\). It does **not** prove Round 95's random-cell cluster estimate (95.7), either canonical M1/M2 core, M9, endpoint uniformity for the cluster route, or the quarter target.

## 2. Exact statement and hypotheses

The source-card-ready citation is:

> Xiaochun Li and Xuerui Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, arXiv:2308.14859v2 [math.NT], revised 14 September 2023, 32 pp., [arXiv record](https://arxiv.org/abs/2308.14859), [arXiv-issued DOI](https://doi.org/10.48550/arXiv.2308.14859).

The arXiv record has only v1 (28 August 2023) and v2 (14 September 2023). As of 17 August 2026, the current author publication page still labels the work a **preprint**; the primary channels searched disclosed no journal version, erratum, later arXiv version, or public author clarification. This is a statement about the searched public primary record, not a claim that private correspondence cannot exist.

Li--Yang define

\[
 R(X)=\sum_{m^2+n^2\le X}1-\pi X,
 \qquad
 \Delta(X)=\sum_{n\le X}d(n)-X\log X-(2\gamma-1)X,
 \tag{2.1}
\]

and Theorem 1.2 claims \(R(X),\Delta(X)=O_\varepsilon(X^{\theta_{\rm LY}+\varepsilon})\) as \(X\to\infty\). There is no integer restriction on \(X\). With the project's \(P(X)=N(\sqrt X)-\pi X\), the first quantity in (2.1) is literally \(P(X)\), including points on \(m^2+n^2=X\).

The analytic input concerns

\[
 S=\sum_{H\le h\le2H}g(h/H)
      \sum_{M\le m\le2M}G(m/M)
 e\!\left(\frac{hT}{M}F(m/M)\right),
 \tag{2.2}
\]

where \(T,M\) are large, \(H\ge1\), \(F\in C^3[1,2]\), \(g,G\) have bounded variation, and fixed constants \(C_1,\ldots,C_5\ge2\) satisfy

\[
 C_r^{-1}\le |F^{(r)}(z)|\le C_r\quad(r=1,2,3),
 \qquad
 |F'(z)F'''(z)-3F''(z)^2|\ge C_4^{-1}.
 \tag{2.3}
\]

The corrected Case (A) hypotheses are (1.2),

\[
 H\ge M^{11}T^{-6}(\log T)^{171/140}\quad\hbox{if }M>T^{9/16},
 \qquad H\le MT^{-49/164}.
 \tag{2.4}
\]

Case (B) requires

\[
 M\le C_5T^{1/2},
 \qquad
 H\le \min\{M^{35/69}T^{-2/23},\ B_0M^{3/2}T^{-1/2}\}.
 \tag{2.5}
\]

The short length used in the Bombieri--Iwaniec decomposition is

\[
 N_A\asymp H(M/H)^{41/25}T^{-49/100}(\log T)^{969/14000}
 \tag{2.6}
\]

in Case (A), and

\[
 N_B\asymp \min\left\{
 M^{7/8}T^{-3/20}H^{-29/40}(\log T)^{969/5600},
 M^2H^{-1/3}T^{-2/3}\right\}
 \tag{2.7}
\]

in Case (B). Lemma 4.1 additionally assumes

\[
 N^{6-q}\gg H^{2q-6}(M^3/T)^{4-q}.
 \tag{2.8}
\]

Theorem 4.2 uses \(4\le q\le4.5\); in Case (B) it also prints

\[
 M^{-27/23}T^{53/92}<H<M^{-9}T^4(\log T)^{171/140}.
 \tag{2.9}
\]

For the final circle/divisor application, the actual ranges are narrower:

\[
 M\le T^{1/2},\qquad
 \max\{T^{(7\theta_{\rm LY}-2)/2},MT^{2\theta_{\rm LY}-1}\}
 <H\le MT^{-\theta_{\rm LY}}.
 \tag{2.10}
\]

With the corrected definition \(H=MT^x\),

\[
 2\theta_{\rm LY}-1<x\le-\theta_{\rm LY},
 \qquad -3/8<x\le-\theta_{\rm LY},
 \tag{2.11}
\]

and Li--Yang choose

\[
 q=q_x=2+\frac{2}{5\sqrt{\frac{-1-8x}{2(1-14x)}}-1},
 \qquad 4<q_x\le4.291635244\ldots<4.5.
 \tag{2.12}
\]

The first-spacing estimate concerns arbitrary \(|a_{k\ell}|\le1\), \(1\le L<K\le1/\eta\le KL\), and \(q\ge4\). Its use of Guth--Maldague requires plates of dimensions \(\eta^{\beta _2}\times\eta^{\beta _1}\times\eta\) with

\[
 \beta _1\in[1/2,1],\qquad \beta _2\in[0,1].
 \tag{2.13}
\]

Li--Yang set

\[
 \beta=\beta _1+\beta _2=\frac2{q-2},
 \qquad
 \eta^{\beta _1}K=\eta^{\beta _2}L=(\eta^\beta KL)^{1/2}.
 \tag{2.14}
\]

Their printed condition

\[
 (L/K)^{(q-2)/(q-4)}\le\eta
 \tag{2.15}
\]

is exactly the check \(\beta _1\ge1/2\); it is not, by itself, the missing lower bound \(\beta _2\ge0\).

## 3. Proof or derivation

The exact theorem map is

\[
\begin{aligned}
&\text{Guth--Maldague Thm. 3}
 +\text{ Li--Yang Lemmas 3.5--3.7 and the }E_4\text{ count}
 \longrightarrow \text{restricted Prop. 3.1},\\
&\text{restricted Prop. 3.1}
 +\text{Bourgain--Watt v1 (5.22)/Huxley second spacing}
 \longrightarrow \text{Li--Yang Lemma 4.1},\\
&\text{Lemma 4.1}+N_A/N_B\text{ monotonicity}
 \longrightarrow \text{restricted Theorem 4.2},\\
&\text{Case I/II verification}+q_x+(2.8)
 \longrightarrow S/H\ll T^{\theta_{\rm LY}+\varepsilon},\\
&\text{Bourgain--Watt v1 (7.1)--(7.7), with the new }S/H\text{ bound}
 \longrightarrow (1.1).
\end{aligned}
\tag{3.1}
\]

**The \(7/16\) seam.** The source TeX for (4.4) literally contains `M<T^{-\frac{7}{16}}`, and the rendered v2 PDF reproduces it on viewer page 17/32. The same source later contains `M<T^{\frac{7}{16}}` in (5.11), rendered on viewer page 26/32. V1 has the same contradiction. Bourgain--Watt v1, Theorem 3(A), (4.3), supplies the upstream condition with the positive exponent. The rest of Li--Yang's proof first uses \(M\le T^{1/2}<T^{9/16}\), then splits according to the positive-threshold condition and proves Case (A) or Case (B). Thus (1.2) is the uniquely consistent reading and is proved in the same source's final application; the negative exponent is not an alternative theorem.

**Repair of the missing small-cap range.** Put

\[
 d=\log_\eta(L/K).
\]

Solving (2.14) gives \(\beta _1=(\beta+d)/2\), \(\beta _2=(\beta-d)/2\). Condition (2.15) gives \(d\ge1-\beta\), hence \(\beta _1\ge1/2\). Guth--Maldague additionally needs

\[
 d\le\beta
 \quad\Longleftrightarrow\quad
 \frac{L}{K}\ge\eta^{2/(q-2)}.
 \tag{3.2}
\]

In the Bombieri--Iwaniec parameters

\[
 R\asymp(M^3/(NT))^{1/2},\quad
 L\asymp HQ/R^2,\quad K\asymp NQ/R^2,\quad
 \eta\asymp R^2/(NH),
 \tag{3.3}
\]

(3.2) is

\[
 \frac HR\ge (N/H)^{(q-4)/4}.
 \tag{3.4}
\]

For \(N=N_A\), discard the favorable logarithmic power and use \(H=MT^x\). The exponent margin in (3.4) is

\[
 D(x)=\frac{51}{200}+\frac{17x}{25}
 -\frac{q_x-4}{4}\left(-\frac{41x}{25}-\frac{49}{100}\right).
 \tag{3.5}
\]

Let \(s=2/(q_x-2)=5\sqrt{(-1-8x)/(2(1-14x))}-1\). Then

\[
 200sD(x)=2s(1-14x)+164x+49.
 \tag{3.6}
\]

The right side is nonnegative on \([-3/8,-\theta_{\rm LY}]\). Indeed, after moving the negative linear term and squaring (both sides have the required signs there), the claim is equivalent to

\[
 50(1-14x)(-1-8x)-(192x+47)^2
 =-(8x+3)(3908x+753)\ge0.
 \tag{3.7}
\]

Here \(8x+3\ge0\) and \(3908x+753<0\). Equality occurs only at \(x=-3/8\), while the actual range starts at \(x>2\theta_{\rm LY}-1=-0.371033648\ldots>-3/8\), so there is fixed positive power slack; the logarithm in (2.6) is favorable because the left-to-right ratio in (3.4) grows as \(N^{1/2-(q-4)/4}\). In Case (B), \(N_B>N_A\) on the final range and the same monotonicity makes (3.4) still easier. Thus the final application has \(\beta _2\ge0\); together with \(\beta _1\ge1/2\), \(\beta_1+\beta_2\le1\), and (2.14), all of (2.13) and the interval-size conditions hold.

**Repair of the Case (B) logarithm.** Direct division shows that the second branch in (2.7) exceeds (2.6) only when

\[
 H>M^{-27/23}T^{53/92}(\log T)^{2907/12880},
 \tag{3.8}
\]

not merely under the lower inequality in (2.9). The final Case II argument supplies much more:

\[
 H^{23}M^{27}\ge T^{202\theta_{\rm LY}-50}>T^{53/4},
 \tag{3.9}
\]

with a positive power margin, so (3.8) follows for large \(T\). The first branch condition is exactly the printed upper bound in (2.9), including \((\log T)^{171/140}\). Therefore \(N_B>N_A\) is valid where Theorem 4.2 is actually invoked, although its general printed implication is too broad.

**Remaining Case A/B and auxiliary checks.** From (2.10), \(M<T^{9/16}\) and \(H<MT^{-49/164}\), so the second and third Case (A) clauses are harmless. If the first clause (1.2) holds, Case (A) applies. If it fails, interpolation between \(H\le MT^{-\theta_{\rm LY}}\) and that failure gives

\[
 H\ll M^{35/69}T^{(68-328\theta_{\rm LY})/345}
 (\log T)^{969/16100}
 \le M^{35/69}T^{-2/23},
\]

and (2.10) gives \(H\le B_0M^{3/2}T^{-1/2}\) for large \(T\). This is Case (B). Equation (3.9) and the negation of Case I give the two sides of the corrected reduction range. The choice (2.12) lies in \((4,4.292]\); Li--Yang's (5.23) proves (2.8), and (5.24) removes the parenthetical term in (4.10). The latter reduces exactly to

\[
 (8x+3)(4888x+683)\le0,
\]

on the stated interval. The former has a margin of about \(3.662\) at its worst endpoint \(x=-\theta_{\rm LY}\), and its two sides are monotone in opposite directions as Li--Yang state.

**Exact optimization.** If \(x=-\theta\), the defining equality for the endpoint exponent is equivalent, with the positive-sign condition, to

\[
 364\theta-74=10\sqrt{2(1+14\theta)(8\theta-1)}.
\]

Squaring gives

\[
 27524\theta^2-13168\theta+1419=0.
 \tag{3.10}
\]

Only the plus root lies in \([0.3,0.35]\) and satisfies the unsquared sign condition, yielding (1.1). The exponent after inserting \(q_x\) is

\[
 \Phi(x)=-\frac{8x}{25}
 -\frac1{200}\left(\sqrt{2(1-14x)}-5\sqrt{-1-8x}\right)^2
 +\frac{51}{200}.
 \tag{3.11}
\]

Writing \(r=\sqrt{2(1-14x)/(-1-8x)}\), one has

\[
 \Phi'(x)=\frac{41}{50}-\frac{7}{10r}-\frac r5>0
\]

on \([-3/8,-\theta_{\rm LY}]\); equivalently \(10r^2-41r+35<0\), and here \(5/2\le r<2.73<(41+\sqrt{281})/20\). Hence \(\Phi(x)\le\Phi(-\theta_{\rm LY})=\theta_{\rm LY}\).

**Removal, real scope, and endpoints.** Li--Yang's own displayed circle identity and phase list are malformed, but their cited Bourgain--Watt v1 Section 7 supplies the exact identities for real \(X\), the sawtooth truncation and divisor-count control of its error, the dyadic reduction, and the correct phase

\[
 F(z)=(z+a/(4M))^{-1}+bM/(4T),\qquad |a|+|b|\le1,
\]

with \(g(z)=z^{-1}\), \(G=1\). These weights have bounded variation and the reciprocal phase satisfies (2.3) uniformly for \(3\le M\le\sqrt T\). Small \(M\), small \(H\), and the range \(H/M\le T^{2\theta-1}\) are handled respectively by the trivial estimate, the \((2/7,4/7)\) exponent-pair estimate, and the stated one-dimensional derivative estimate. The Fourier truncation error is uniform even when its argument is an integer; the exact sawtooth convention and the \(O(1)\) terms retain the inclusive lattice boundary. Dyadic logarithms are absorbed in \(X^\varepsilon\). Thus the asymptotic for real \(X\) extends to all real \(X\ge2\) by enlarging the constant on a compact interval.

Finally, Bourgain--Watt arXiv:1709.04340 was withdrawn in v2. The withdrawal notice identifies faults in its Propositions 2, 3, and \(1'\), namely its first-spacing estimates, and says its Theorems 1--3 lose theorem status. Li--Yang do not import those estimates: Bourgain--Watt v1 (5.22) leaves the first-spacing norm \(A_q^{1/q}\) symbolic, and Li--Yang replace its estimate by their restricted Proposition 3.1. The exact Section 7 reduction is also independent of the faulty first-spacing proposition. The withdrawal is therefore a mandatory source warning but not, by itself, a logical break in the repaired chain (3.1).

## 4. First doubtful or unproved step

The first substantive unproved step in the literal source is the application of Guth--Maldague inside Proposition 3.1 without verifying \(\beta _2\ge0\). This is not implied by Li--Yang's printed hypotheses. For example, take

\[
 q=21/5,\qquad \eta=10^{-6},\qquad K=10^6,\qquad L=1.
\]

Then \(1\le L<K\le1/\eta\le KL\) and

\[
 (L/K)^{(q-2)/(q-4)}=10^{-66}\le10^{-6}=\eta,
\]

but \(\beta=10/11\), \(d=1\), and

\[
 \beta _2=(\beta-d)/2=-1/22<0.
\]

Thus the cited Guth--Maldague theorem is outside its range, and Proposition 3.1 is not proved in its full stated generality. Equations (3.2)--(3.7) repair only the final Li--Yang application.

The next general overstatement is the implication \((2.9)\Rightarrow N_B>N_A\), which misses the logarithm in (3.8). Again, (3.9) repairs the final application but not every tuple allowed by the printed Theorem 4.2.

The remaining visible defects are typographical or expository rather than surviving theorem-specific gaps: the \(7/16\) sign, the sign in \(H=MT^x\), the \(-1-8x\) radicand, the circle identity, the first factor in (5.15), a \(\sqrt L/\sqrt K\) normalization typo, and swapped \(\beta_1,\beta_2\) labels in Lemma 3.4. In each case the adjacent equations or the explicitly cited primary formula determine and prove the needed reading. The passage from a box-localized discrete cone sum to the global Guth--Maldague inequality is also sketched too tersely (the stated bump has Fourier tails); the standard band-limited cutoff/finite-overlap replacement supplies the claimed \(\eta^{-\varepsilon}\) loss and does not alter the exponent. It should be written out in any clean version.

Accordingly, there is no surviving algebraic or endpoint gap in the **narrow final theorem after the two supplements above**, but there is no public corrected Li--Yang artifact containing those supplements. A policy that permits only the literal external source, and not this audited repair, must retain the theorem as uncertified.

## 5. Required control test and outcome

| Control | Exact test | Outcome |
|---|---|---|
| Discrepancy and scope | Compare (2.1) with \(P(X)=N(\sqrt X)-\pi X\); inspect the sawtooth identities at jump points and the quantifier on \(X\). | Pass: identical inclusive discrepancy, real \(X\), with endpoint-uniform \(O(1)\) terms. |
| Rendered height seam | Compare v1/v2 TeX, v2 PDF page 17, v2 (5.11)/PDF page 26, and Bourgain--Watt v1 (4.3). | Pass only after explicit correction: (4.4) has a rendered minus typo; \(+7/16\) is uniquely intended. |
| Other literal seams | Substitute the printed \(H=MT^{-x}\); compare the two circle terms; recompute (5.27). | All three printed forms fail internally. The unique repairs are \(H=MT^x\), Bourgain--Watt (7.2), and \(\sqrt{-1-8x}\). |
| Version/publication search | Check the arXiv version history, current author publication page, source TeX, PDFs, and public primary correction channels. | V1 and v2 only; both preserve the defects. No public journal version, erratum, or author clarification found; author page says “Preprint.” |
| Exact exponent | Derive (3.10), retain the unsquared sign, and evaluate the valid root. | Pass: \(\theta=(3292+25\sqrt{1717})/13762=0.3144831759740614\ldots\). The other quadratic root is extraneous. |
| \(q\) and final inequalities | Evaluate (2.12), (5.23), (5.24), and \(\Phi'\). | Pass: \(q(-\theta)=4.2916352435\ldots\); endpoint margins for (5.23) and (5.24) are approximately \(3.662\) and \(0.2536\); exact factorization proves (5.24), and \(\Phi'>0\). |
| Guth--Maldague range | Test the printed proposition with the explicit countertuple above; then test (3.4) on the final \(x\)-range. | General proposition fails its proof-range check. Final application passes by exact factorization (3.7), with \(D(2\theta-1)=0.0022761\ldots>0\). |
| Case (B) comparison | Divide each branch of \(N_B\) by \(N_A\), retaining logarithms. | General (2.9) is too weak by \((\log T)^{2907/12880}\); final application passes by the positive power margin (3.9). |
| Withdrawn dependency | Locate the precise Bourgain--Watt withdrawal fault and the exact formulas imported by Li--Yang. | Conditional pass: the withdrawn first-spacing propositions are not imported; symbolic (5.22) and the elementary Section 7 reduction are the components used. |
| Scope effect | Compare (1.1) with the Round-95 obligations. | Improves only the external global pointwise baseline; no implication to (95.7), M1/M2, M9, or \(1/4\). |

The decimal evaluations in this table were diagnostic checks. The certification rests on the exact equations and factorizations (3.7), (3.10), and the exact factorization for (5.24), not on floating-point output.

## 6. Dependencies and exact artifacts used

Project artifacts, and no sibling Round-95 report, were used:

- `protocol.md`;
- `state/active_campaign.yml`;
- the relevant `Li-Yang-source-audit` and downstream-scope entries in `state/proof_obligations.yml`;
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/derivation_packet.md`;
- `sources/li_yang_2023.md`;
- `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`;
- the two exact prior conductor context files named by the active campaign.

Primary external artifacts:

- Li--Yang [arXiv record and version history](https://arxiv.org/abs/2308.14859), [v2 HTML](https://arxiv.org/html/2308.14859v2), [v1 HTML](https://arxiv.org/html/2308.14859v1), [rendered PDF](https://arxiv.org/pdf/2308.14859), and source TeX linked from the arXiv record;
- Xuerui Yang's current [publication/preprint page](https://sites.google.com/view/xuerui-yang), which labels this item a preprint;
- Guth and Maldague, *Amplitude dependent wave envelope estimates for the cone in \(\mathbb R^3\)*, [arXiv:2206.01093v2](https://arxiv.org/abs/2206.01093), especially [Theorem 3](https://arxiv.org/html/2206.01093v2);
- Bourgain and Watt, *Mean square of zeta function, circle problem and divisor problem revisited*, [withdrawal record](https://arxiv.org/abs/1709.04340) and [v1 full text](https://arxiv.org/html/1709.04340v1), especially (4.3), (5.12), (5.22), and (7.1)--(7.7).

The exact imported-source boundary is important. Guth--Maldague provides only the small-cap inequality under (2.13). Bourgain--Watt v1 provides the double-large-sieve/second-spacing inequality with \(A_q\) left symbolic and the exact circle/divisor reduction. Li--Yang's local \(E_4\) count and interpolation provide the replacement first-spacing bound, subject to the repaired \(\beta_2\) check. No theorem was imported from a secondary summary.

## 7. Recommended state effect

**Recommended state effect: revise.** Complete the Li--Yang source card with the exact citation, real/inclusive convention, corrected formula ledger, the Guth--Maldague restricted-range supplement (3.2)--(3.7), the Case (B) logarithmic supplement (3.8)--(3.9), and the Bourgain--Watt withdrawal boundary. After an independent seam reviewer reproduces those two supplements and graph validation succeeds, the conductor may promote the narrow statement (1.1) as a repaired external theorem.

Do not promote Li--Yang Proposition 3.1 for all printed \((L,K,\eta,q)\), and do not promote Theorem 4.2 for every tuple satisfying its printed Case (B) lower bound. Do not describe arXiv v2 as a corrected or published version. Leave every Round-95 cluster, canonical-core, M9, and quarter-target node unchanged.
