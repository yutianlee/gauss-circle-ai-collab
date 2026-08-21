## 1. Result

The frozen theorem survives hostile review.  For the literal two-sided
coefficient

\[
 \beta_{h,H}=-{\Phi(|h|/(H+1))\chi _4(|h|)\mathbf 1_{2\nmid h}
 \over \pi |h|}
\]

and any fixed bounded denominator weight on a fixed-ratio shell,

\[
 \int_I|S_{D,H,w}(t)|^2\,dt\ll_{c_0,c_1}(V+D^2)D.                 \tag{1.1}
\]

Exact rational equality must be grouped before spacing is invoked.  After
that grouping, the coefficient mass is \(O(D)\), including all perfect-rational
multiplicities and both signs, and the reduced frequencies are
\(\gg D^{-2}\)-separated.  Montgomery--Vaughan's real-line Hilbert inequality
then gives (1.1) with no logarithm.

For \(I=[Y,2Y]\), \(D\leq Y^{1/2}\), Chebyshev gives the exact consequence

\[
 |\{t:|S_{D,H,w}(t)|>Y^{1/4+\eta}\}|
 \ll D Y^{1/2-2\eta}.                                          \tag{1.2}
\]

The union over dyadic \(D\)'s has measure
\(O(Y^{1-2\eta})\), or \(O_\varepsilon(Y^{1-2\eta+\varepsilon})\)
when the logarithmic loss needed to control the sum of all blocks is also
absorbed.  At \(\eta=0\) and \(D\asymp Y^{1/2}\), this is exactly the trivial
ambient measure \(Y\).  The \(h=1\) full-shell control has grouped
\(\ell^2\)-mass \(\gg D\), and fixed Rademacher denominator signs realize a
second moment \(\gg YD\); hence the diagonal scale and the endpoint failure of
Chebyshev to save measure are genuine.

The moving height alone is not an obstruction: with fixed denominator data,
\(H(t)=\lfloor Dt^{-1/4}\rfloor\) and the literal Vaaler profile still satisfy
\(\int_Y^{2Y}|S(t)|^2dt\ll YD\).  An ordered moving top cutoff, or a uniformly
bounded-variation normalized top profile representable by ordered prefixes,
also transfers with only \(O(\log^2(2D))\), hence no power loss.  The Round-93
packet does not state the literal moving top profile, so this conditional
prefix/BV lemma cannot yet be identified with the actual hard-top block.
For a merely bounded \(t\)-dependent weight the analogue is false by a factor
\(D\).

Thus the frozen global moment should be retained as a new metric lemma, while
every claimed implication to the Round-92 canonical core, pointwise
`M9-M2`, endpoint uniformity, `M9`, or a Gauss-circle exponent is rejected.

## 2. Exact statement and hypotheses

**Frozen theorem.**  Let \(D\geq1\), \(1\leq H\leq D\), let
\(\mathscr D_D\subset[c_0D,c_1D]\cap\mathbb Z_{>0}\), and let
\(|w_D(d)|\leq1\).  The shell constants \(0<c_0<c_1<\infty\) are fixed.
The height, coefficient, set, and weight are independent of \(t\in I\), and
\(I\) is any interval of length \(V\).  With \(e(x)=e^{2\pi ix}\) and the
literal \(\beta_{h,H}\) above, the sum (93.1) satisfies (1.1).  The assertion
also holds trivially for \(H=0\) after declaring the sum empty.  Positivity or
reality of \(w_D\) is not assumed.

**Exceptional-set theorem.**  If \(I=[Y,2Y]\), \(D\leq Y^{1/2}\), and
\(\eta\geq0\), then (1.2) holds.  For a dyadic family
\(\mathcal D\) with \(\sum_{D\in\mathcal D}D\ll Y^{1/2}\),

\[
 \left|\bigcup_{D\in\mathcal D}
 \{t:|S_D(t)|>Y^{1/4+\eta}\}\right|
 \ll Y^{1-2\eta}.                                               \tag{2.1}
\]

If the desired conclusion is instead
\(\sum_D|S_D(t)|\leq Y^{1/4+\eta}\), one lowers the individual threshold by
\(O(\log Y)\); the resulting \(O(\log^2Y)\) measure factor is
\(Y^\varepsilon\)-harmless but must not be silently omitted.

**Moving-height lemma.**  Keep \(\mathscr D_D,w_D\) fixed on \([Y,2Y]\),
assume \(D\leq Y^{1/2}\), put
\(H(t)=\lfloor Dt^{-1/4}\rfloor\), and use the exact
\(\beta_{h,H(t)}\), extended by zero for \(|h|>H(t)\).  Then

\[
 \int_Y^{2Y}\left|\sum_{h\ne0}\beta_{h,H(t)}
       \sum_{d\in\mathscr D_D}w_D(d)e(ht/(4d))\right|^2dt
 \ll YD.                                                        \tag{2.2}
\]

**Conditional moving-top lemma.**  Suppose, in addition, that the moving
denominator multiplier is a fixed bounded multiplier times either an ordered
prefix \(1_{d\leq m(t)}\), or a Stieltjes superposition of such prefixes with
uniform total variation \(O(1)\).  This includes a profile of the form
\(W(d/\sqrt t)\) when \(W\) has fixed compact support and bounded variation,
as well as a starred boundary point.  Then the left side of (2.2) is

\[
 \ll YD\log^2(2D).                                               \tag{2.3}
\]

No assertion about the actual moving hard-top profile is made until its
literal formula is checked against this hypothesis.  The condition
\(|w_D(d,t)|\leq1\) alone is explicitly insufficient.

## 3. Proof or derivation

Write every nonzero rational \(h/d\) uniquely as \(a/b\), where \(b>0\),
\((|a|,b)=1\), and \(h=ka,d=kb\) with \(k\geq1\).  Exact equality gives

\[
 A_{a,b}=\sum_{\substack{k:\,kb\in\mathscr D_D\\|ka|\leq H}}
           \beta_{ka,H}w_D(kb),
 \qquad
 S(t)=\sum_{a,b}A_{a,b}e(at/(4b)).                               \tag{3.1}
\]

Since \(kb\in[c_0D,c_1D]\), the admissible \(k\)'s lie in a fixed-ratio
interval.  If its lower endpoint is below (1), then \(b>c_0D\) and the
upper endpoint is \(<c_1/c_0\).  Therefore in both cases

\[
 |A_{a,b}|\leq{1\over\pi|a|}\sum_k k^{-1}\ll_{c_0,c_1}|a|^{-1}.
\]

Here \(|a|\leq H\) and \(b\leq c_1D\), so, without needing coprimality,

\[
 \sum_{a,b}|A_{a,b}|^2
 \ll D\sum_{1\leq |a|\leq H}a^{-2}\ll D.                       \tag{3.2}
\]

Distinct reduced signed fractions satisfy

\[
 \left|{a\over4b}-{a'\over4b'}\right|
 ={ |ab'-a'b|\over4bb'}\geq {1\over4c_1^2D^2}.                 \tag{3.3}
\]

This is false before equality grouping: repeated representations have zero
spacing.

For completeness, let \(\lambda_r\) be the distinct frequencies in (3.1),
\(\delta=\min_{r\ne s}|\lambda_r-\lambda_s|\), and \(z_r(u)=A_re(\lambda_ru)\).
Montgomery--Vaughan Theorem 2, equation (1.6), states for distinct real
\(\lambda_r\)

\[
 \left|\sum_{r\ne s}{z_r\overline{z_s}\over\lambda_r-\lambda_s}\right|
 \leq \pi\delta^{-1}\sum_r|z_r|^2.                             \tag{3.4}
\]

Expanding the integral over \([u,u+V]\), its off-diagonal part is

\[
 {1\over2\pi i}\left(
 \sum_{r\ne s}{z_r(u+V)\overline{z_s(u+V)}\over\lambda_r-\lambda_s}
 -\sum_{r\ne s}{z_r(u)\overline{z_s(u)}\over\lambda_r-\lambda_s}
 \right).
\]

Thus

\[
 \int_u^{u+V}\left|\sum_rA_re(\lambda_rt)\right|^2dt
 \leq(V+\delta^{-1})\sum_r|A_r|^2,                              \tag{3.5}
\]

and (3.2)--(3.3) prove (1.1).  Notice that the \(2\pi\) in the project's
\(e(x)\) is exactly accounted for in the factor \(1/(2\pi i)\); importing an
\(e^{i\lambda t}\) formula without this conversion risks a spurious \(2\pi\).
Chebyshev applied to (3.5) gives (1.2), and summing \(D\) gives (2.1).

For sharpness, take the half-open full shell
\(\mathscr D_D=[D,2D)\cap\mathbb Z\).  For every such \(d\), the reduced
groups \((a,b)=(1,d)\) and \((-1,d)\) contain only \(k=1\).  Hence

\[
 \sum_{a,b}|A_{a,b}|^2
 \geq2|\beta_{1,H}|^2\sum_{D\leq d<2D}|w_D(d)|^2\gg D           \tag{3.6}
\]

whenever the displayed denominator mass is \(\gg D\), since
\(|\beta_{1,H}|\geq1/(2\pi)\).  More strongly, put \(H=1\) and choose fixed
Rademacher signs \(w_D(d)\).  Averaging over the signs kills distinct-\(d\)
cross terms and gives

\[
 \mathbb E_w\int_Y^{2Y}|S(t)|^2dt
 =|\beta_{1,1}|^2\sum_{D\leq d<2D}
 \int_Y^{2Y}|e(t/(4d))+e(-t/(4d))|^2dt
 =2|\beta_{1,1}|^2YD+O(D^2).
\]

For \(Y\geq D^2\) some fixed choice of signs therefore has moment
\(\gg YD\).  Also, on an interval of length \(\asymp D\) about zero, \(w=1\)
makes the \(h=\pm1\) terms coherent and gives moment \(\gg D^3\), showing
that the \(D^2D\) term in (1.1) is also of the right uniform order.

It remains to justify the moving statements.  Define
\(\beta_{h,0}=0\) and
\(\Delta_K(h)=\beta_{h,K}-\beta_{h,K-1}\).  Vaaler's \(\Phi\) is \(C^1\)
on \([0,1]\) and \(\Phi(1)=0\), so for every \(|h|\leq K\), including the new
edge \(|h|=K\),

\[
 |\Delta_K(h)|\ll K^{-2}.                                      \tag{3.7}
\]

After rational grouping let \(m_{a,b}\) be the number of terms in a
\(\Delta_K\) group.  Then

\[
 \sum_{a,b}|\Delta A_{K;a,b}|^2
 \ll K^{-4}\sum_{a,b}m_{a,b}^2
 \leq K^{-4}(\max m_{a,b})\sum_{a,b}m_{a,b}
 \ll {D\over K^2},                                             \tag{3.8}
\]

because \(\max m_{a,b}\leq K\) and there are \(O(KD)\) underlying
\((h,d)\)'s.  The set \({t:H(t)\geq K}\) is an interval, so (3.5) applies
to each increment on its own interval.  On \([Y,2Y]\), the nonconstant
\(K\)'s occupy a fixed-ratio range (or an \(O(1)\) range near \(K=1\)); hence

\[
 \sum_K\left(Y{D\over K^2}\right)^{1/2}\ll\sqrt{YD}.
\]

Minkowski, together with the fixed minimum-height piece, proves (2.2).
This also shows that partitioning into all height-floor intervals is an
avoidable loss, not a genuine obstruction.

For (2.3), order the \(O(D)\) denominators and use a binary interval tree.
Every prefix is a disjoint union of \(O(\log(2D))\) tree blocks.  At each
tree level the blocks partition the shell, and for the base coefficient

\[
 \sum_{B}\sum_{a,b}|A_{B;a,b}|^2
 \leq\sum_{a,b}\left(\sum_k|\beta_{ka,H}|\right)^2\ll D.        \tag{3.9}
\]

For \(\Delta_K\), the same argument as (3.8), now summed over the blocks of
one level, gives \(O(D/K^2)\).  Cauchy over the \(O(\log D)\) blocks in a
prefix and (3.5) over the \(O(\log D)\) tree levels prove the maximal bounds
\(YD\log^2(2D)\) and \(YD\log^2(2D)/K^2\), respectively.  Minkowski in \(K\)
then proves (2.3).  A bounded-variation profile is a Stieltjes integral of
prefix indicators, so its total variation only changes the constant.

Finally, bounded moving weights without ordered structure are impossible.
For \(H=1\), \(Y=D^2\), set

\[
 g_d(t)=e(t/(4d))+e(-t/(4d)),\qquad
 w_d(t)=\overline{g_d(t)}/|g_d(t)|
\]

away from its zeros, and put \(w_d(t)=0\) at a zero.  Then
\(S(t)=\beta_{1,1}\sum_d|g_d(t)|\).  Since each \(|g_d|\) has mean bounded
below on an interval of length \(Y\gg d\), Cauchy gives

\[
 \int_Y^{2Y}|S(t)|^2dt\gg YD^2,
\]

which is a factor \(D\) larger than \(YD\).  A literal structural hypothesis
on the moving top profile is therefore indispensable.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the frozen proof once Theorem 2 of
Montgomery--Vaughan is mapped with the project's \(2\pi\)-normalization.
The first unproved transfer step is documentary and mathematical: the packet
does not state \(w_D(d;t)\) for the actual hard-top block, so one cannot check
whether it is an ordered prefix/Stieltjes-BV profile covered by (2.3).  The
words “support or profile may move” are not a hypothesis.

If one ignores the increment argument and applies (1.1) independently on all
height-floor intervals, their number is

\[
 M_H\asymp DY^{-1/4},
\]

and one obtains only

\[
 \int_Y^{2Y}|S(t)|^2dt
 \ll YD+M_HD^3=YD+D^4Y^{-1/4}.                                  \tag{4.1}
\]

At \(D=Y^{1/2}\), (4.1) is \(Y^{7/4}\), a factor \(Y^{1/4}\) above the
target.  Its Chebyshev bound is
\(Y^{5/4-2\eta}\), hence gives density saving only for \(\eta>1/8\).
Freezing anew at each of \(O(D)\) moving top-denominator crossings can lose a
factor \(D=Y^{1/2}\) if one repeatedly pays the full \(D^2D\) term.  These are
the first exact losses of the naive freezing method; (2.2)--(2.3) show how
ordered variation avoids them, but only after the actual profile is matched.

The second forbidden step is average-to-pointwise.  At the top endpoint the
threshold \(Y^{1/4}\) equals the diagonal root-mean-square scale
\(D^{1/2}\).  Equation (1.2) has no saving there, and even for \(\eta>0\) it
allows every preassigned point to lie in the exceptional set.  No local
fourth moment, large-value propagation theorem, or fixed-\(X\) estimate is
contained in (1.1).

## 5. Required control test and outcome

| Hostile seam | Test | Outcome |
|---|---|---|
| Reduced-frequency equality | Compare \((h,d)=(ka,kb)\) before spacing. | **Pass only after grouping.** Ungrouped spacing is zero; reduced signed fractions have spacing at least \((4c_1^2D^2)^{-1}\). |
| Perfect-rational multiplicity | Let every admissible multiple \(k\) occur. | **Pass.** The \(k\)'s remain in a fixed-ratio interval, so their \(1/k\) mass is \(O(1)\); no hidden \(\log D\) occurs. |
| Coefficient \(\ell^2\) mass | Sum the grouped bound over all \(a,b\), including support edges. | **Pass:** \(\sum|A_{a,b}|^2\ll D\). The hypotheses \(h\ne0\), \(H\leq D\), and fixed-ratio denominator shell are essential. |
| \(\chi_4\) and two signs | Expand negative and positive \(h\) as distinct signed reduced numerators. | **Pass algebraically.** The proof then uses only \(|\beta_h|\leq(\pi|h|)^{-1}\); it also proves unsigned/adversarial frozen analogues and therefore supplies no signed canonical-core gain. |
| Continuous large sieve | Track \(e(x)=e^{2\pi ix}\) through Montgomery--Vaughan (1.6). | **Pass:** (3.5) is \(V+\delta^{-1}\), not \(V+2\pi\delta^{-1}\) or a modulo-one separation statement. |
| \(h=1\), actual shell | Use \([D,2D)\), where the groups \((\pm1,d)\) have only \(k=1\). | **Pass/sharp:** coefficient energy is \(\gg D\) for nondegenerate denominator \(\ell^2\)-mass; Rademacher fixed weights give moment \(\gg YD\). No lower moment is asserted for every deterministic actual profile. |
| Short-interval sharpness | Take \(H=1,w=1,V\asymp D\) near a coherent point. | **Pass/sharp:** moment \(\gg D^3\), matching the \(D^2D\) term. |
| Chebyshev endpoint | Put \(D=Y^{1/2}\) in (1.2). | **Pass with no saving:** \(Y^{1-2\eta}\); at \(\eta=0\) this is \(Y\). |
| All dyadic blocks | Sum \(D\), not merely the number of blocks. | **Pass:** \(\sum_D D\ll Y^{1/2}\) gives (2.1); controlling the total sum costs only logarithms. |
| Moving height floor | Difference consecutive exact Vaaler profiles and retain equality groups. | **Pass:** (3.7)--(3.8) give the no-power-loss height transfer (2.2). Naive separate freezing loses \(Y^{1/4}\) at the top. |
| Moving hard top | Test ordered prefix/BV representation and also arbitrary bounded motion. | **Conditional pass / general fail:** prefix/BV motion costs \(\log^2D\); arbitrary bounded \(w(d,t)\) violates the target by factor \(D\). Literal actual-profile matching is missing. |
| Local fourth moment | Compare the \(L^2_t\) theorem with `M9-M2-local-fourth-moment-LFM`. | **No implication.** Neither a fourth moment nor coherence-window control is proved. |
| Canonical density--discrepancy core | Look for the fixed-\(X\) blocks \(\mathfrak Q\), the density zero mode, and the \(\rho^{-1/2}\) gain. | **Absent.** Rational large-sieve spacing is coefficient-blind and does not estimate the Round-92 transformed energy. |
| Pointwise and exponent scope | Evaluate \(\eta=0\) and inspect exceptional points. | **Reject all forward claims:** no pointwise `M9-M2`, endpoint uniformity, `M9`, one-quarter theorem, or new unconditional exponent follows. |

## 6. Dependencies and exact artifacts used

The exact permitted project artifacts used were:

- `protocol.md`;
- `state/proof_obligations.yml` at starting graph SHA-256
  `db11a048eaafe05832a8fe5d2a62af297967c2ca5c6721630256acb063fb7c47`;
- `state/best_proof_draft.md`;
- `state/gap_register.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/derivation_packet.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/synthesis.md`;
- `sources/xiao_2026.md`;
- `sources/vaaler_1985.md`.

No sibling Round-93 report was read.

| Primary source | Literal hypotheses/results checked | Applicability decision |
|---|---|---|
| H. L. Montgomery and R. C. Vaughan, [*Hilbert's Inequality*, Theorem 2 (1.6), JLMS (1974), 73--82](https://doi.org/10.1112/jlms/s2-8.1.73); [author-hosted scan](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf) | A finite family of **distinct real** \(\lambda_r\), real-line spacing \(\delta=\min_{r\ne s}|\lambda_r-\lambda_s|>0\), and arbitrary complex coefficients.  Theorem 2 is not the modulo-one Theorem 1. | **Applies literally** after reduced equality grouping.  Equation (3.5) is derived from (1.6), so no further large-sieve theorem is imported. |
| Jeffrey D. Vaaler, [*Some extremal functions in Fourier analysis* (1985)](https://doi.org/10.1090/S0273-0979-1985-15349-2), Theorem 6 and Theorem 18 | Integer \(H\geq0\), \(e(u)=e^{2\pi iu}\), midpoint sawtooth, \(\Phi=\widehat J\) with \(0\leq\Phi\leq1\), \(C^1\) support on \([0,1]\), and the argument \(h/(H+1)\).  The project endpoint conversion is separately recorded in `sources/vaaler_1985.md`. | **Applies only to the exact beta algebra and (3.7).** It supplies neither a reciprocal large sieve, a moving top profile, nor a pointwise M2 estimate. |
| Yixiu Xiao, [*Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*, arXiv:2606.28986v1](https://arxiv.org/html/2606.28986v1), Theorems 1.1--1.3 | \(S(h,n)=\sum_{n/2\leq a\leq n}e(h\sqrt a)\) is unweighted; the averaged variable is positive integer \(h\sim H\).  Theorem 1.1 assumes fixed \(\delta>0\) and \(H\geq n^{1/2+\delta}\).  Theorem 1.2 assumes fixed \(0<\delta<1/6\) and \(n^{1/2+\delta}\leq H\leq n^{2/3}\).  Theorem 1.3 combines the second moment with Erdős--Turán and separate pointwise exponential-sum bounds (Lemmas 2.3--2.5). | **Guardrail only.** There is no map of variable, phase, coefficient, support, norm, moving endpoint, or fixed-\(X\) conclusion to (93.1) or the Round-92 canonical core.  Xiao does not provide an average-to-pointwise principle here. |

## 7. Recommended state effect

**Promote, narrowly:** create or retain a lemma such as
`M9-M2-frozen-global-second-moment` with (1.1), exact reduced grouping,
two-sided \(\chi_4\) coefficient, (1.2)--(2.1), and the explicit statement that
it is a global metric result.  The \(h=1\) coefficient-mass and Rademacher
sharpness controls should be part of that lemma's evidence.

**Promote conditionally or revise:** the moving-height statement (2.2) is
proved internally.  A moving-top statement may be promoted with the
\(O(\log^2D)\) loss only after the conductor writes the literal actual
\(w_D(d;t)\) and verifies its ordered prefix/Stieltjes-BV representation,
including floors, the top star, and every profile reset.  Until then, record
the arbitrary-moving-weight counterexample and the naive losses (4.1), and
do not call the frozen theorem an “actual moving block” theorem.

**Source effect:** the Xiao v1 hypotheses and discrepancy proof have now been
checked from the primary text.  `Xiao-2026-source-audit` may be marked as a
completed guardrail audit with no implication edge and no proof dependency.
Montgomery--Vaughan Theorem 2 should receive a source card if (1.1) is added
to the graph.

**Retain open / reject forward edges:** leave
`M9-M2-top-endpoint-density-discrepancy-energy`,
`M9-M2-local-fourth-moment-LFM`,
`M9-M2-fourth-moment-average-to-pointwise`, `M9-M2`,
`M9-endpoint-uniformity`, `M9`, `Conditional-bridge`, and `GC-target`
unchanged.  Reject any claim that (1.1) supplies the canonical
\(\rho^{-1/2}\) gain, a pointwise endpoint estimate, closure of other M2
packets, closure of M1, or an improved Gauss-circle exponent.

### Authorized addendum: fixed-in-\(Y\) moving partition and almost-all assembly

This addendum is conductor-authorized and supersedes only the earlier
documentary reservation about the unspecified actual moving top.  It uses the
additional candidate
rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/candidates/conductor_moving_moment_extension.md,
the blind profile construction in
rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md,
and the accepted literal statement of the \(R5\)-Full node.

**Exact fixed-in-\(Y\) partition: pass.**  Fix \(Y\geq2\), put
\(D_0=\sqrt Y\), \(D_j=2^{-j}\sqrt Y\), and let \(J\) be maximal with
\(D_J\geq(2Y)^{1/4}\).  The accepted functions satisfy
\(W(u)=\eta(u)-\eta(2u)\), \(\eta(u)=1\) for \(u\leq1\), and
\(\eta(u)=0\) for \(u\geq4/3\).  For every integer \(d\geq1\) and every
\(t\in[Y,2Y]\),

\[
\begin{aligned}
&\mathbf 1_{d\leq\lfloor\sqrt t\rfloor}
 \left\{\sum_{j=0}^{J}W\!\left(\frac d{2D_j}\right)
 +\eta\!\left(\frac d{2D_{J+1}}\right)\right\}\\
&\qquad=
 \mathbf 1_{d\leq\lfloor\sqrt t\rfloor}
 \eta\!\left(\frac d{2D_0}\right)
 =
 \mathbf 1_{d\leq\lfloor\sqrt t\rfloor}.                        \tag{7.A.1}
\end{aligned}
\]

The first equality is finite telescoping.  The second uses
\(d/(2D_0)\leq\sqrt{2Y}/(2\sqrt Y)=1/\sqrt2<1\).
Thus (7.A.1) is exact with the floor:
for integral \(d\), \(d\leq\sqrt t\) is equivalent to
\(d\leq\lfloor\sqrt t\rfloor\).  Every active denominator multiplier is
exactly a fixed \(W(d/(2D_j))\) times the one moving ordered prefix.  Its
untruncated support is
\[
 D_j\leq d\leq\frac83D_j.                                      \tag{7.A.1a}
\]
Moreover \(D_j\leq D_0=\sqrt Y\leq\sqrt t\), so the literal active-scale
condition \(D_j\leq\sqrt t\) is automatic, including the moving top.  No
moving smooth symbol or profile reset remains.

**Bottom owner: pass.**  Since
\(D_{J+1}<(2Y)^{1/4}\), the last term in (7.A.1) is supported on

\[
 d<\frac83D_{J+1}\ll Y^{1/4}.                                  \tag{7.A.2}
\]

It is removed before Fourier expansion.  The sawtooth terms in both balanced
legs, including the two-shift difference, are uniformly bounded, so their
complete bottom contribution is \(O(Y^{1/4})\).  This assignment is exact
and neither duplicates nor omits an active Fourier block.

**Height and maximal-prefix proof: pass.**  For each active \(D=D_j\), set

\[
 H_D(t)=\lfloor Dt^{-1/4}\rfloor.
\]

Because \((2Y)^{1/4}\leq D\leq\sqrt Y\), one has \(H_D(t)\geq1\)
throughout the window and \(H_D(t)\asymp Dt^{-1/4}\).  With
\(\gamma_{h,r}=\beta_{h,r}-\beta_{h,r-1}\), extended from
\(\beta_{h,0}=0\),

\[
 |\gamma_{h,r}|\ll r^{-2}\mathbf 1_{0<|h|\leq r},\qquad
 \beta_{h,H_D(t)}
 =\sum_{r\geq1}\gamma_{h,r}\mathbf 1_{t\leq(D/r)^4}.             \tag{7.A.3}
\]

For a denominator interval containing \(N\) integers, exact reduced-fraction
grouping and Cauchy within each equality class give grouped energy
\(O(N/r^2)\).  At a fixed binary-tree level the intervals partition the
shell, so their energies sum to \(O(D/r^2)\).  A prefix uses at most one
tree interval per level.  Pointwise Cauchy, the frozen continuous
large-sieve estimate, and summation over levels therefore cost only
\(O(\log^2(2D))\), not the number of possible prefixes.  Applying this on
\([Y,2Y]\cap(-\infty,(D/r)^4]\) and using Minkowski in \(r\) proves, for
both original main blocks,

\[
 \int_Y^{2Y}|S_{i,D}^{\mathrm{mov}}(t)|^2\,dt
 \ll_\varepsilon
 Y^\varepsilon(Y+D^2)D,\qquad i\in\{1,2\}.                     \tag{7.A.4}
\]

For \(i=2\), both frequency signs and the literal \(\chi_4(h)\) remain in
the equality classes.  For \(i=1\), the same increment bound holds for the
Vaaler coefficient and multiplication by the spatial \(\chi_4(d)\) does
not alter the energy.  The prefix is exactly
\(d\leq\lfloor\sqrt t\rfloor\), so (7.A.4) certifies the actual moving M1
and M2 blocks, not merely a BV majorant.

**Applicability of \(R5\)-Full: pass.**  The accepted node is pointwise for
every real parameter, every active \(D\) with
\(H_D\asymp Dt^{-1/4}\), and every actual active denominator profile,
explicitly including the hard top, exact products, both shifts, height
floors, and dyadic assembly.  The blind profile report proves for this same
fixed \(W\) the required nonnegativity, \(0\leq W\leq1\), fixed-shell
support, and bounded discrete variation; (7.A.1)--(7.A.2) prove the exact
partition and bottom owner in the present normalization.  Moreover, the
literal active range satisfies
\[
 t^{1/4}\leq(2Y)^{1/4}\leq D\leq\sqrt Y\leq\sqrt t.
\]
Equation (7.A.1) identifies the literal active profile as
\[
 W\!\left(\frac d{2D}\right)
 \mathbf 1_{d\leq\lfloor\sqrt t\rfloor},
\]
supported on \([D,8D/3]\), with \(D\leq\sqrt t\).  Its only moving datum is
the hard prefix already included in the accepted node.  Therefore
\(R5\)-Full applies without an unsmoothing or continuum-smoothness
hypothesis and gives the complete residual contribution

\[
 O_\varepsilon(Y^{1/4+\varepsilon})                            \tag{7.A.5}
\]

pointwise after dyadic assembly.  This use is distinct from smooth Poisson:
the latter still cannot treat a discontinuous top profile, but no smooth
Poisson theorem is used in the moment or almost-all argument.

**H1--H4 almost-all assembly: pass.**  Identity (7.A.1) is inserted into
the already accepted exact balanced sawtooth formula before H4.  Vaaler's
finite identity is pointwise and permits the integer order \(H_D(t)\) on
each fixed block.  The bottom is owned by (7.A.2), the main polynomials by
(7.A.4), the Fejer residuals by (7.A.5), and the \(O(1)\) term remains
unchanged.  Chebyshev applied to (7.A.4), with each block threshold lowered
by the number of geometric scales, followed by the union over both main
sums and \(\sum_D D\ll\sqrt Y\), yields after absorbing the resulting
logarithms and renaming \(\varepsilon\)

\[
 \left|\left\{t\in[Y,2Y]:
 |P(t)|>Y^{1/4+\eta+\varepsilon}\right\}\right|
 \ll_{\eta,\varepsilon}Y^{1-2\eta+\varepsilon}.                \tag{7.A.6}
\]

For every fixed \(\eta>0\), choosing \(0<\varepsilon<2\eta\) makes
(7.A.6) a density-one theorem for real \(t\).

**Certification decision.**  The moving actual-block theorem (7.A.4)
**certifies**, for both M1 and M2.  The almost-all \(P(t)\) theorem (7.A.6)
also **certifies** under the already accepted H1--H4 and \(R5\)-Full nodes.
This is an almost-everywhere real-variable theorem only.  It gives no bound
at every real \(t\), at every integer, or at circle-problem jump points;
does not estimate either Round-92 canonical core; and does not promote
M9-M1, M9-M2, M9-endpoint-uniformity, M9, Conditional-bridge, or GC-target.
The accepted uniform \(1/3\) exponent is unchanged.
