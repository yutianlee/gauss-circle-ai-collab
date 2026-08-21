# Conductor review: repaired Li--Yang theorem

Campaign: `gc-strict-sub-one-third-cluster-source-fork`

Starting graph SHA-256:
`e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

## Decision

The source report's two substantive supplements have been independently
reproduced. The narrow real-
\(X\), inclusive Gauss-circle theorem is accepted as a repaired external
dependency:

\[
 P(X)\ll_\varepsilon X^{\theta_{\rm LY}+\varepsilon},
 \qquad
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
 \tag{R95.LY1}
\]

The printed general Proposition 3.1 and general Case-B part of Theorem 4.2
are not accepted in their full stated ranges.

## Primary-source boundary

The arXiv record has only v1 and v2, and the author page still calls the
paper a preprint. The source contains four literal defects. The unique
readings needed in the final argument are:

\[
 M<T^{7/16},\qquad H=MT^x,
 \qquad \sqrt{-1-8x}\text{ in (5.27)},
 \tag{R95.LY2}
\]

together with the two-sign, two-range circle identity in Bourgain--Watt
v1 (7.2). The positive \(7/16\) occurs in Li--Yang's own (5.11) and in
Bourgain--Watt v1 (4.3); the negative version is vacuous for large
\(M\ge1\). The other three repairs follow by direct substitution into
the adjacent formulas.

The null/circular labels in Li--Yang Lemma 3.4 are also interchanged in
its prose. The geometry and all later localization equations use the
correct assignment: \(k\) varies in the curved direction with width
\(\eta^{\beta_1}K\), while \(l\) varies in the flat direction with width
\(\eta^{\beta_2}L\).

## Independent small-cap range check

Guth--Maldague Theorem 3 requires

\[
 \beta_1\in[1/2,1],\qquad \beta_2\in[0,1].
\]

Write \(d=\log_\eta(L/K)\) and
\(\beta=2/(q-2)\). Li--Yang's balancing equations give

\[
 \beta_1=\frac{\beta+d}{2},\qquad
 \beta_2=\frac{\beta-d}{2}.
\]

Their printed condition checks \(d\ge1-\beta\), hence
\(\beta_1\ge1/2\), but does not imply \(d\le\beta\). The explicit tuple
\(q=21/5\), \(\eta=10^{-6}\), \(K=10^6\), \(L=1\) satisfies the printed
conditions and has \(\beta_2=-1/22\). Thus the general proposition is
indeed over-stated.

For the final application, \(d\le\beta\) is equivalent to

\[
 \frac HR\ge\left(\frac NH\right)^{(q-4)/4}.
 \tag{R95.LY3}
\]

Put \(H=MT^x\) and use

\[
 N_A=H(M/H)^{41/25}T^{-49/100}
\]

after omitting its favorable logarithmic factor. Then

\[
 \frac HR=T^{51/200+17x/25},\qquad
 \frac NH=T^{-41x/25-49/100}.
\]

The exponent margin is

\[
 D(x)=\frac{51}{200}+\frac{17x}{25}
 -\frac{q_x-4}{4}\left(-\frac{41x}{25}-\frac{49}{100}\right).
\]

With \(s=2/(q_x-2)\), direct simplification gives

\[
 200sD(x)=2s(1-14x)+164x+49.
\]

After moving the negative linear term and squaring with the valid signs,
the desired inequality is exactly

\[
 50(1-14x)(-1-8x)-(192x+47)^2
 =-(8x+3)(3908x+753)\ge0.
 \tag{R95.LY4}
\]

It holds on \([-3/8,-\theta_{\rm LY}]\), with equality only at
\(-3/8\). The actual range has
\(x>2\theta_{\rm LY}-1>-3/8\), hence fixed power slack. Since the left
side of (R95.LY3) grows like \(N^{1/2}\), while its right side grows like
\(N^{(q-4)/4}\) with \(q<4.5\), replacing \(N_A\) by the larger \(N_B\)
makes the inequality easier. Finally, \(\beta_1+\beta_2\le1\) and the
balanced interval-size equation give all remaining plate-range checks.

## Independent Case-B comparison

Direct division of the second branch of \(N_B\) by \(N_A\) gives

\[
 \frac{N_{B,2}}{N_A}
 =M^{9/25}H^{23/75}T^{-53/300}
  (\log T)^{-969/14000}.
\]

Therefore the general implication needs

\[
 H>M^{-27/23}T^{53/92}(\log T)^{2907/12880},
 \tag{R95.LY5}
\]

not merely the printed power inequality. This confirms the second
overstatement. In the final Case-II range,
\(M\ge HT^{\theta_{\rm LY}}\) and
\(H\ge T^{(7\theta_{\rm LY}-2)/2}\), so

\[
 H^{23}M^{27}
 \ge H^{50}T^{27\theta_{\rm LY}}
 \ge T^{202\theta_{\rm LY}-50}
 >T^{53/4}.
 \tag{R95.LY6}
\]

The positive power slack in (R95.LY6) absorbs the logarithm in
(R95.LY5). Division of the first \(N_B\) branch gives exactly the printed
upper inequality
\(H<M^{-9}T^4(\log T)^{171/140}\). Thus \(N_B>N_A\) is valid everywhere
it is actually invoked.

## Endpoint exponent and final implication

The endpoint equality reduces to

\[
 27524\theta^2-13168\theta+1419=0.
\]

Its discriminant is \(10000\cdot1717\); the plus root is the only root
in the stated interval satisfying the unsquared sign condition, and is
exactly (R95.LY1). The optimized exponent function is increasing on the
final \(x\)-interval, so its maximum is the endpoint value.

Bourgain--Watt v1 (7.2)--(7.7) supplies the exact inclusive, real-
\(X\) sawtooth reduction, with the first-spacing norm still symbolic.
The 2023 withdrawal identifies faults in different first-spacing
propositions and says Theorems 1--3 lose status. Those propositions are
not imported here: the restricted Li--Yang/Guth--Maldague argument is the
replacement. The exact Section-7 identity and truncation estimates can be
and were checked independently of the withdrawn theorem statements.

## Scope and state recommendation

Promote only (R95.LY1) and the completed source audit. Keep the internal
project theorem \(P(X)\ll X^{1/3+\varepsilon}\) as the best theorem proved
from the project's M1/M2 architecture; label (R95.LY1) as the stronger
source-audited global theorem. Do not infer the Round-95 cluster estimate,
either canonical core, M9-M1, M9-M2, M9, or the quarter target.

Artifacts used:

- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/li_yang_strict_source_audit.md`;
- `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`;
- the primary Li--Yang, Guth--Maldague, and Bourgain--Watt arXiv records and texts;
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/controls/li_yang_exact_arithmetic_check.txt`.
