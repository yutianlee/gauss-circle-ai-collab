# Round205 — independent fixed-p gain frontier

Campaign: `gc-full-frontier-moment-strategy-review`. Task: `blind_gain_frontier`.
Role: independent statement-only analyst. Status: analytical candidate report.
Generated: 2026-09-26 01:39:40 UTC.
Graph hash: deliberately unavailable in the isolated statement packet; no graph was read.
Effort: 100 percent analytical; no experiments, external sources, or sibling artifacts.

## 1. Result

Write

\[
\theta=\frac{3292+25\sqrt{1717}}{13762},\qquad
\beta=2\theta-\frac12,\qquad q=\frac{136}{13},\qquad a=\frac{13}{125}.
\]

For the original hypotheses, the fixed-p radius moment
\(M_p(T)=\int |H_T(R)|^p\,dR\), for every fixed real \(p\ge2\), satisfies

\[
M_p(T)\ll_{p,\varepsilon}T^{E_0(p)+\varepsilon},\qquad
E_0(p)=\max\{1,\beta(p-2)\}.
\]

Its monotonic-persistence pointwise output is

\[
P(x)\ll_{p,\varepsilon}x^{\rho_0(p)+\varepsilon},\qquad
\rho_0(p)=\frac{p/4+(1+E_0(p))/2}{p+1}>\theta.
\]

The infimum over fixed p is exactly \(\theta\). Thus interpolation and iteration using only these original hypotheses cannot improve the supplied exponent. An explicit monotone abstract discrepancy below both realizes peaks of size \(x^\theta\) and saturates the radius-moment exponent \(E_0(p)\).

For the prospective high-level improvement, the exact power envelope obtained by the specified layer-cake integration is

\[
\boxed{E_{\sigma,\tau}(p)=
\max\left\{1+a(p-q)_+,\ \beta(p-2)-\sigma,
\ 1-\tau+\beta(p-q)\right\}.}
\]

All endpoint logarithms and the unsimplified integral expression are retained in Section 3. At \(p=12\),

\[
\boxed{E_{\sigma,\tau}(12)=
\max\left\{\frac{29}{25},\ 10\beta-\sigma,
\ 1+\frac{20}{13}\beta-\tau\right\}.}
\]

Consequently the closed sufficient gain conditions

\[
\boxed{\sigma\ge10\beta-\frac{29}{25},\qquad
\tau\ge\frac{20}{13}\beta-\frac4{25}}
\tag{1}
\]

give \(M_{12}(T)\ll_\varepsilon T^{29/25+\varepsilon}\) and

\[
\boxed{P(x)\ll_\varepsilon x^{102/325+\varepsilon},
\qquad \frac{102}{325}<\theta.}
\]

These conditions are the requirements of this upper-envelope certificate for that moment milestone. They are not necessary facts about the actual arithmetic discrepancy. Moreover, any gains restricted to levels above the fixed cutoff \(T^a\) still admit abstract monotone peaks with discrepancy exponent \(1/4+a/2=151/500>1/4\). This is a genuine logical obstruction to a quarter theorem from the displayed abstract hypotheses alone.

## 2. Exact hypotheses

The only mathematical input is the isolated statement packet. Its windows are interpreted as comparable-radius intervals: the radius variable lies in \([cT,CT]\), with fixed positive constants, and the evaluated points lie in the interior of a comparable enlarged interval on which the same distribution, supremum, and reconstruction bounds are available. Constants may depend on those fixed windows.

This interval/enlargement qualification is essential for an endpoint-uniform persistence argument. A bound on an arbitrary measurable set of measure \(O(T)\), without interval coverage, would not suffice. Likewise, reconstruction on an enlargement alone would not supply a moment bound there. If the packet's word “window” is intended more weakly, the pointwise conclusion below holds only at points whose required one-sided persistence interval is covered by the moment domain.

Assume, for every positive \(\varepsilon\), with corresponding constants,

\[
\sup|H_T|\ll_\varepsilon T^{\beta+\varepsilon},\qquad
D_T(V)=|\{R:|H_T(R)|>V\}|
\ll_\varepsilon T^\varepsilon(V^{-2}+TV^{-q})\quad(V\ge1),
\]

and

\[
P(R^2)=\pi^{-1}\sqrt R\,H_T(R)+O_\varepsilon(T^{1/2+\varepsilon}),
\qquad N(x)=P(x)+\pi x\text{ is nondecreasing}.
\]

For the prospective calculation replace the upper tail on
\(T^a\le V\le T^{\beta+\varepsilon}\) by

\[
D_T(V)\ll_\varepsilon T^\varepsilon
\left(T^{-\sigma}V^{-2}+T^{1-\tau}V^{-q}\right),
\qquad \sigma,\tau\ge0,
\]

retaining the original tail below \(T^a\).

Every moment order p is fixed independently of T. Small epsilon losses can be rescaled depending on p; no bound uniform in arbitrarily large p is assumed. Set \(Y=T^2\).

Useful exact inequalities are

\[
a<\frac{13}{110}<\frac{83}{650}<\beta
<\frac{39}{298}<\frac16,
\qquad \beta(q-2)>1,
\qquad a(q-2)=\frac{22}{25}.
\tag{2}
\]

For example, \(4143/100<\sqrt{1717}<4144/100\), verified by squaring the rational endpoints, proves the needed comparisons with \(\beta=(50\sqrt{1717}-297)/13762\). No numerical experiment is involved.

## 3. Proof or derivation

### 3.1 Original fixed-p moments, including endpoints

For \(1\le U<W\), define

\[
J_s(U,W)=
\begin{cases}
(W^s-U^s)/s,&s\ne0,\\
\log(W/U),&s=0.
\end{cases}
\]

Layer cake and the measure of the radius window give, with a supremum cutoff B,

\[
M_p(T)\ll_p T+
T^\varepsilon p\{J_{p-2}(1,B)+T J_{p-q}(1,B)\}.
\tag{3}
\]

Take \(B\asymp T^{\beta+\delta}\), then choose \(\delta>0\) sufficiently small for the desired final epsilon. For power bookkeeping one can write \(B=T^\beta\); all fixed constants and \(\delta\)-losses are absorbed by the final arbitrary epsilon.

At \(p=2\), the first integral is \(\log B\). At \(p=q\), the second is \(T\log B\). Away from these endpoints their powers are

\[
J_{p-2}(1,B)\ll_p B^{p-2}\quad(p>2),
\]

\[
T J_{p-q}(1,B)\ll_p
\begin{cases}
T,&p<q,\\
T B^{p-q},&p>q.
\end{cases}
\]

Because \(\beta(q-2)>1\), whenever \(p>q\),

\[
\beta(p-2)>1+\beta(p-q).
\]

At \(p=q\), \(T^{\beta(q-2)}\) also dominates \(T\log T\). The \(p=2\) logarithm is dominated by T. Thus (3) gives exactly the stated exponent envelope

\[
E_0(p)=\max\{1,\beta(p-2)\}.
\]

The change of dominant power occurs at
\(p_c=2+1/\beta<q\). There is no new logarithm at \(p=p_c\): this is equality of two already evaluated terms, not an integration endpoint.

### 3.2 Normalization, the Jacobian, and monotonic persistence

Let

\[
Q_p(T)=\int |P(R^2)|^p\,dR,
\qquad S_p(Y)=\int |P(x)|^p\,dx,
\]

over corresponding comparable windows. The reconstruction normalization is \(1/\pi\), and its main term has p-th power \(\pi^{-p}R^{p/2}|H_T|^p\). Consequently

\[
Q_p(T)\ll_{p,\varepsilon}
T^{p/2}\{M_p(T)+T^{1+\varepsilon}\}.
\tag{4}
\]

The exact change of variables is \(x=R^2\), \(dx=2R\,dR\), so

\[
S_p(Y)=2\int R|P(R^2)|^p\,dR
\ll_{p,\varepsilon}T^{p/2+1}
\{M_p(T)+T^{1+\varepsilon}\}.
\tag{5}
\]

Thus if \(E\ge1\) and \(M_p(T)\ll T^{E+\varepsilon}\), then

\[
S_p(Y)\ll_{p,\varepsilon}
T^{p/2+1+E+\varepsilon}
=Y^{p/4+(1+E)/2+\varepsilon}.
\tag{6}
\]

The reconstruction error is included in (4)–(6), rather than silently removed.

For persistence let \(A=|P(x_0)|\). If \(P(x_0)=A>0\), monotonicity gives

\[
P(x_0+h)\ge A-\pi h\ge A/2
\quad\left(0\le h\le\frac{A}{2\pi}\right).
\]

If \(P(x_0)=-A<0\), it gives

\[
P(x_0-h)\le-A+\pi h\le-A/2
\quad\left(0\le h\le\frac{A}{2\pi}\right).
\]

The supplied supremum and reconstruction ensure \(A\ll Y^{\theta+\varepsilon}=o(Y)\), so the appropriate one-sided interval lies in the fixed enlargement for all large Y. Integrating yields

\[
\frac{A^{p+1}}{2^{p+1}\pi}\le S_p(Y).
\tag{7}
\]

Combining (6) and (7) gives

\[
\rho(p;E)=\frac{p/4+(1+E)/2}{p+1}.
\tag{8}
\]

### 3.3 Why the original moments do not bootstrap

For \(p\le p_c\), formula (8) is

\[
\rho_0(p)=\frac14+\frac{3}{4(p+1)}.
\]

For \(p\ge p_c\), it is

\[
\rho_0(p)=\theta+\frac{1-6\beta}{4(p+1)}.
\tag{9}
\]

In fact \(E_0(p)\ge\beta(p-2)\) makes the right side of (9) a lower bound for \(\rho_0(p)\) for every \(p\ge2\). Since \(\beta<1/6\), every finite p returns an exponent strictly worse than \(\theta\). The second formula tends to \(\theta\) as p tends to infinity through fixed orders. Retaining the existing supremum simply keeps \(\theta\).

Interpolation cannot remove this loss. Its available moment exponents are already the maximum of two affine functions of p, and the monotone peak family in Section 5 attains that envelope while having \(x^\theta\) peaks. No inference from these hypotheses can contradict that family.

Likewise, an iteration that retains the better of the old supremum and the new moment-to-pointwise output keeps the old supremum at its first step. Repeating the same operation therefore supplies no new input. Treating p as a T-dependent parameter is not justified by the fixed-p constants, and would not defeat the abstract counterexample in any case.

### 3.4 Prospective envelope with all integration endpoints

Put \(A_0=T^a\) and again use \(B=T^\beta\) for power bookkeeping. The direct unsimplified layer-cake bound is

\[
\begin{aligned}
M_p(T)\ll_p T+pT^\varepsilon\{&J_{p-2}(1,A_0)
+T J_{p-q}(1,A_0)\\
&+T^{-\sigma}J_{p-2}(A_0,B)
+T^{1-\tau}J_{p-q}(A_0,B)\}.
\end{aligned}
\tag{10}
\]

The complete contribution table, up to positive fixed-p constants and the common epsilon loss, is as follows. The baseline T from levels below 1 is additional in every row.

| Moment order | Low \(V^{-2}\) | Low \(TV^{-q}\) | High \(T^{-\sigma}V^{-2}\) | High \(T^{1-\tau}V^{-q}\) |
|---|---|---|---|---|
| \(p=2\) | \(\log T\) | \(T\) | \(T^{-\sigma}\log T\) | \(T^{1-\tau+a(2-q)}\) |
| \(2<p<q\) | \(T^{a(p-2)}\) | \(T\) | \(T^{\beta(p-2)-\sigma}\) | \(T^{1-\tau+a(p-q)}\) |
| \(p=q\) | \(T^{22/25}\) | \(T\log T\) | \(T^{\beta(q-2)-\sigma}\) | \(T^{1-\tau}\log T\) |
| \(p>q\) | \(T^{a(p-2)}\) | \(T^{1+a(p-q)}\) | \(T^{\beta(p-2)-\sigma}\) | \(T^{1-\tau+\beta(p-q)}\) |

At \(p=2\), the logarithms before suppressing constants are \(\log A_0=a\log T\) and \(\log(B/A_0)=(\beta-a)\log T\). The same logarithms multiply T and \(T^{1-\tau}\), respectively, at \(p=q\).

For \(p\le q\), the low \(V^{-2}\) power is below T since \(a(q-2)=22/25<1\). For \(p>q\), the low second power exceeds the low first power by

\[
1-a(q-2)=\frac3{25}.
\]

For \(p<q\), the high second contribution is also bounded by T, since \(\tau\ge0\). These facts simplify (10) to

\[
M_p(T)\ll_{p,\varepsilon}T^{E_{\sigma,\tau}(p)+\varepsilon},
\]

with the boxed envelope in Section 1. At \(p=q\), a \(T\log T\) contribution remains explicitly in (10), and must not be called O(T) without an epsilon allowance. It is subleading if \(\beta(q-2)-\sigma>1\). At \(p=2\), all logarithms are subleading to T. Equality between two powers of (10) produces no further logarithm.

For every fixed p the resulting pointwise certificate is (8) with \(E=E_{\sigma,\tau}(p)\). This is the exact envelope of the stated integration bound; it does not assert that the true arithmetic moment attains it.

### 3.5 Quantitative strict-improvement frontier

Improvement over the inherited \(\theta\) requires

\[
E_{\sigma,\tau}(p)<\beta(p+1)-\frac12.
\tag{11}
\]

Define the positive numbers

\[
g_2=\frac12-3\beta,\qquad
g_q=\frac32-(q+1)\beta.
\]

The two high-level affine terms in (11) require, independently of p,

\[
\sigma>g_2,\qquad \tau>g_q.
\tag{12}
\]

Since \(\beta<3/[2(q+1)]=39/298\), no \(p\le q\) can satisfy (11), even with both high contributions removed. For \(p>q\), the low-level requirement is exactly

\[
p>p_*:=\frac{3/2-\beta-aq}{\beta-a}
=\frac{103/250-\beta}{\beta-13/125}.
\tag{13}
\]

Here \(q<p_*<12\), the last inequality being equivalent to \(\beta>83/650\). Thus, for this power envelope, a fixed order p gives strict improvement precisely when (12) and (13) hold. Strictness provides room to absorb epsilon losses; equality gives no strict power improvement from this certificate.

At \(p=12\), \(12-q=20/13\), so (10) gives

\[
E_{\sigma,\tau}(12)=
\max\{29/25,10\beta-\sigma,1+(20/13)\beta-\tau\}.
\]

The closed inequalities (1) are exactly what makes every displayed contribution no larger than the target \(T^{29/25+\varepsilon}\). Both right sides in (1) are positive. No endpoint logarithm occurs at \(p=12\).

For this milestone the radius discrepancy moment, the x moment, and the pointwise bound are, respectively,

\[
Q_{12}(T)\ll_\varepsilon T^{179/25+\varepsilon},
\qquad
S_{12}(Y)\ll_\varepsilon T^{204/25+\varepsilon}
=Y^{102/25+\varepsilon},
\]

\[
P(x)\ll_\varepsilon x^{102/325+\varepsilon}.
\]

The strict comparison \(102/325<\theta\) is exactly \(83/650<\beta\). If only strict improvement, rather than this particular moment milestone, is desired at \(p=12\), the weaker open inequalities are

\[
\boxed{\sigma>\frac12-3\beta,\qquad
\tau>\frac32-\frac{149}{13}\beta.}
\tag{14}
\]

The difference between each closed threshold in (1) and its counterpart in (14) equals the same positive quantity \(13\beta-83/50\).

### 3.6 Why this is not a quarter proof

Even the hypothetical fixed-p radius bound \(M_p(T)\ll T^{1+\varepsilon}\) gives only
\(\rho=1/4+3/[4(p+1)]\). A finite fixed-p milestone therefore retains a positive persistence loss.

In this particular prospective scheme, merely allowing arbitrary fixed p is also insufficient. The retained low-level envelope is
\(1+a(p-q)\) for \(p>q\), and its pointwise output is

\[
\frac14+\frac a2+
\frac{3/4-a(q+1)/2}{p+1}
=\frac{151}{500}+\frac{77}{500(p+1)}.
\tag{15}
\]

Thus that low-level certificate alone has a limiting exponent \(151/500\), even if both high-level terms could be deleted. For fixed finite \(\sigma,\tau\), the supplied high-level exponent still has slope \(\beta p\) at large p. No unrestricted high-moment claim with sublinear growth in p has been proved here. More decisively, the fixed-cutoff abstract peak control below shows why a quarter theorem needs additional information below the cutoff, a cutoff tending to exponent zero, or an arithmetic mechanism beyond the displayed hypotheses.

## 4. First doubtful or unproved step

There is no unproved analytical step in the conditional layer-cake, Jacobian, or monotonic-persistence derivations above, subject to the interval/enlargement qualification in Section 2.

The first unproved step toward an arithmetic improvement is to establish the prospective high-level distribution estimate with actual gains satisfying (1), or at least (12), for the actual square-root series on the required enlarged windows. The original distribution and supremum do not establish those gains. Their availability has been assumed only to calculate a frontier.

The exact arithmetic identity, coefficients, sign structure, and endpoint-uniform provenance of the packet's original estimates were not supplied to this isolated task and were not audited. No claim about a Vaaler coefficient, a \(\chi_4\) cancellation, M9, or the true circle discrepancy follows from the abstract peak constructions.

## 5. Required controls and outcome

### 5.1 Abstract monotone peaks saturate the original moment envelope

Choose a sufficiently lacunary sequence \(T_j\to\infty\), so any fixed comparable-radius window meets at most a bounded number of its clusters. Put

\[
A_j=T_j^{1/2+\beta},\qquad
n_j=\lfloor T_j^{1/2-3\beta}\rfloor,
\qquad P_0(x)=\frac{x^{1/4}}{4\pi}.
\]

Near \(x=T_j^2\), choose \(n_j\) disjoint intervals, each of length \(A_j/\pi\), separated by gaps of that length. If an interval starts at s, add the positive wedge

\[
W_s(x)=
\begin{cases}
A_j-\pi(x-s),&s\le x\le s+A_j/\pi,\\
0,&\text{otherwise}.
\end{cases}
\]

The total length of a cluster is
\(O(n_jA_j)=O(T_j^{1-2\beta})=o(T_j^2)\), so the clusters can be separated. Define

\[
P(x)=P_0(x)+\sum_s W_s(x),\qquad
H(R)=\frac{\pi P(R^2)}{\sqrt R}.
\]

This is an exact reconstruction with zero error. At a wedge's left endpoint, \(N(x)=\pi x+P(x)\) jumps upward. Inside a wedge, \(N'(x)=P_0'(x)>0\). Outside wedges, \(N'(x)=\pi+P_0'(x)>0\). At a right endpoint it is continuous. Hence N is nondecreasing globally.

On a window with \(T\asymp T_j\), the background H is exactly \(1/4\), the peak height is \(\asymp T^\beta\), each wedge occupies radius length \(\asymp T^{\beta-1/2}\), and the total wedge radius measure is

\[
\asymp n_jT^{\beta-1/2}\asymp T^{-2\beta}.
\]

For \(V\ge1\), only wedges contribute. Since \(V\ll T^\beta\) whenever the tail is nonempty,

\[
D_T(V)\ll T^{-2\beta}\ll V^{-2}.
\]

Thus the entire original distribution bound holds, even without its \(TV^{-q}\) term. The supremum holds as well. Taking fixed positive fractions of the wedges shows, on windows containing a cluster,

\[
M_p(T)\asymp_p T+T^{\beta(p-2)}
\quad\text{for every fixed }p\ge2.
\]

At wedge starts, \(P(x)\asymp T^{1/2+\beta}\asymp x^\theta\). This simultaneously checks normalization, moment-envelope sharpness, persistence direction, and the absence of a self-bootstrap. The positive exponent \(1/2-3\beta\) in the number of wedges is exactly why this construction is possible. Outcome: the abstract control passes; any purported improvement using only the original abstract assumptions would fail it.

### 5.2 A fixed positive cutoff admits peaks for every high-level gain

Repeat the construction with one wedge per cluster and amplitude
\(A_j=cT_j^{1/2+a}\), with c sufficiently small relative to the fixed window-comparability constants. Then throughout every comparable window the corresponding H peak lies strictly below \(T^a\), so

\[
D_T(V)=0\qquad(V\ge T^a).
\]

The strengthened high-level bound holds for every \(\sigma,\tau\ge0\). Below the cutoff, the wedge radius length is \(O(T^{a-1/2})\), and

\[
T^{a-1/2}\ll T^{-2a}\ll V^{-2}
\quad(1\le V\ll T^a),
\]

because \(3a<1/2\). The same original low-level bound and monotonicity hold. Yet these peaks have

\[
P(x)\asymp x^{1/4+a/2}=x^{151/500}.
\]

Outcome: high-range gains alone at the stipulated fixed cutoff cannot logically imply a quarter bound for arbitrary discrepancies satisfying these hypotheses. This is not a counterexample to the arithmetic Gauss-circle conjecture.

### 5.3 Endpoint, seam, and interpretation controls

- At \(p=2\) and \(p=q\), equation (10) and the table retain every logarithm. No logarithm is introduced at equality of gain thresholds.
- The baseline radius measure T is retained, and the reconstruction error contributes at that same baseline scale after normalization.
- The exact Jacobian is \(dx=2R\,dR\), adding a factor T between radius and x moments. Omitting it would incorrectly improve the pointwise exponent.
- Positive peaks persist to the right and negative peaks to the left. Using the opposite direction would not follow from monotonicity.
- The p=12 moment milestone gives \(T^{29/25}\), then \(Y^{102/25}\) for the x moment, then \(x^{102/325}\) pointwise. These are distinct normalizations.
- Conditions (1) are necessary for this displayed upper bound to certify its chosen moment exponent; they need not be necessary for the actual moment, whose tail may be much smaller.
- No numerical control was run or needed; all controls are exact analytical constructions or algebraic checks.

## 6. Dependencies and exact artifacts used

Read in full, and only these files:

1. `protocol.md`.
2. `rounds/codex-managed/gc-full-frontier-moment-strategy-review/briefs/blind_gain_frontier_statement.md`.

No graph, campaign manifest, generated general brief, strategy file, prior report, source card, sibling artifact, or external literature was consulted. No theorem beyond the elementary layer-cake identity, change of variables, and the stated monotonicity was imported. The clock was read only to timestamp this report.

The exact report path is
`rounds/codex-managed/gc-full-frontier-moment-strategy-review/reports/blind_gain_frontier.md`.

## 7. Recommended state effect

Promote, only after the conductor's independent seam checks, the abstract fixed-p gain-envelope calculation and the original-input no-self-bootstrap obstruction. Retain the actual arithmetic target and every unsupplied distribution-gain obligation as unresolved.

Treat (1) as a sufficient quantitative milestone specification, and treat (12)–(13) as the strict-improvement frontier for this upper-envelope route. Reject any inference that a fixed p=12 milestone, or arbitrary gains only above the unchanged positive cutoff exponent a, constitutes a quarter proof.

No state files, proof draft, validation matrix, shared synthesis, or other task artifact were edited. This task stops with this report and does not design or start another round.
