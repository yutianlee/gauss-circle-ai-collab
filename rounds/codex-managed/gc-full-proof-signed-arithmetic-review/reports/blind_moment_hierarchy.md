# Round208: statement-only moment hierarchy derivation

## 1. Result: conditional transfer lemma and fixed-order no-go

Campaign: `gc-full-proof-signed-arithmetic-review`. Task: `blind_moment_hierarchy`. Role: statement-only independent derivation. Generated: 2026-09-27. Graph hash: deliberately not inspected under the isolation instruction. Status: candidate evidence only.

Put

\[
s(\alpha)=\min\{\alpha/4,\beta,(1-\alpha)/2\},\qquad M_N=T^{s(\alpha)},\qquad N=T^\alpha.
\]

All displayed power bounds allow an arbitrarily small factor \(T^\varepsilon\), with constants depending on the fixed moment orders. For \(p>q=136/13\) and \(\delta\ge0\), the weak-tail certificate reaches the radius target \(T^{1+\delta+\varepsilon}\) whenever

\[
s(\alpha)\le a_p(\delta),\qquad
\boxed{a_p(\delta)=\min\left\{\frac{1+\delta}{p-2},\frac{\delta}{p-q}\right\}.}
\tag{1}
\]

A complete radius moment of that size implies

\[
\boxed{P(x)\ll_\varepsilon x^{\,1/4+(3+2\delta)/(4(p+1))+\varepsilon}.}
\tag{2}
\]

For a fixed integer \(k\ge1\), \(2k\le p\), the sufficient shell threshold on each untreated block is

\[
\boxed{K_{2k}(N)\ll T^{k+2+\delta+\varepsilon}M_N^{-(p-2k)}.}
\tag{3}
\]

The hypothetical Gaussian bound \(K_{2k}\ll XH^k\), at every fixed order and over all blocks left untreated for that order, would give the full quarter bound. One fixed order does not imply arbitrarily high moments: its interpolation certificate has a loss growing linearly with \(p\) on a fixed interior scale. Neither the actual arithmetic shell estimate nor the full quarter bound is proved here.

## 2. Exact statement and hypotheses

The sole mathematical hypotheses are those in the isolated packet, including

\[
\frac14<\theta<\frac13,\quad \beta=2\theta-\frac12\in(0,1/6),\quad
X=T^2,\quad I=[T/\sqrt2,\sqrt3T],\quad J=[X/2,3X],
\]

the inclusive monotonicity of \(P(x)+\pi x\), its stated initial growth bound, the complete-series representation, the block tail and supremum bounds, and the singleton, tail, and summation assumptions. The pointwise conclusion is first obtained uniformly for real \(x\in[X,2X]\); varying the dyadic scale yields the global conclusion.

Write a bridge block as

\[
H_N(R)=B_N(R)+E_N(R),\qquad B_N(R)=R^{-1/2}Z_N(R^2).
\]

When errors occur, (3) uses their stipulated harmless complete \(p\)-moment at the \(p\)-moment level. A sufficient precise reading is that the complete error of each bridge block has \(\int_I|E_N|^p\ll T^{1+\varepsilon}\), with the stated number of blocks; summing these errors is then harmless. If instead only the signed sum of unrelated block errors is bounded, with no per-block bound, the individual-envelope argument below needs an additional hypothesis. Cancellation of uncontrolled block errors must not silently be treated as a per-block error estimate.

Every proposed bound for \(K_{2k}\) concerns the actual complete \(Z_N\) and the full integral over \(J\), with its actual real moving scale

\[
h(x)=\frac{2\sqrt x}{\sqrt N},\qquad H=\frac{T}{\sqrt N},\qquad
\sqrt2\le\frac{h(x)}H\le2\sqrt3.
\]

The comparison \(h\asymp H\) does not replace the real endpoints occurring in \(Z_N\) by integer endpoints or by a fixed length. Endpoint, singleton, bridge-error, and rapid-tail contributions must all remain covered.

## 3. Proof and derivation

**Complete moments and monotone persistence.** Suppose

\[
\int_I|H_T(R)|^p\,dR\ll T^{1+\delta+\varepsilon}.
\]

The representation and \(\delta\ge0\) give

\[
\int_I|P(R^2)|^p\,dR\ll T^{1+p/2+\delta+\varepsilon},
\qquad
\int_J|P(x)|^p\,dx\ll T^{2+p/2+\delta+\varepsilon}
=X^{1+p/4+\delta/2+\varepsilon}.
\tag{4}
\]

Here \(dx=2R\,dR\asymp T\,dR\); losing this factor changes the pointwise exponent.

Fix a real \(x_0\in[X,2X]\), and put \(A=|P(x_0)|\). If \(P(x_0)=A>0\), monotonicity gives \(P(y)\ge A/2\) on \([x_0,x_0+A/(2\pi)]\). If \(P(x_0)=-A<0\), it gives \(P(y)\le-A/2\) on \([x_0-A/(2\pi),x_0]\). The initial growth bound, with a sufficiently small fixed epsilon, puts these intervals inside \(J\) for large \(X\). Inclusive counting causes no problem in either inequality. Thus

\[
A^{p+1}\ll_p\int_J|P(y)|^p\,dy,
\]

which proves (2). The small-error exponents in the hypotheses can be chosen sufficiently small to obtain any prescribed epsilon in the conclusion.

**Layer cake and the exact weak-tail threshold.** With an envelope \(M\ge1\), the tail hypothesis gives

\[
\int_I|H_N|^p\ll_p T^\varepsilon
\left(T+\int_1^M v^{p-3}\,dv+T\int_1^M v^{p-q-1}\,dv\right).
\tag{5}
\]

For \(p>q\), this is

\[
\int_I|H_N|^p\ll_p T^\varepsilon
\left(T+M^{p-2}+TM^{p-q}\right).
\tag{6}
\]

Consequently \(M\le T^a\) is sufficient exactly when

\[
(p-2)a\le1+\delta,\qquad (p-q)a\le\delta,
\]

which gives (1). The second branch is the smaller one when
\(\delta\le(p-q)/(q-2)\); the first is the smaller one when the inequality is reversed. Equality is harmless after the epsilon convention.

For completeness, (5) also gives the other fixed orders: for \(0<p\le2\), no power restriction on \(M\) arises; for \(2<p\le q\), the threshold is \(a\le(1+\delta)/(p-2)\). The logarithms at \(p=2,q\) are absorbed by \(T^\varepsilon\). These assertions concern power-sized envelopes, as in the packet.

The adjective “largest” in (1) refers to the universal power threshold certified by these two tail terms. It is sharp as a deduction from just that tail envelope: a peak of height comparable to \(M\) on a set of measure comparable to \(M^{-2}+TM^{-q}\) saturates the two relevant moment powers. For the actual block family, \(s\le\beta\); once the threshold reaches \(\beta\), every block is already covered, so there is no additional finite largest cutoff within that bounded family.

**Safe bands and their complements.** In full form the certified set is

\[
\{\alpha\in[0,1]:\alpha\le4a\}\ \cup\
\{\alpha\in[0,1]:\alpha\ge1-2a\}\ \cup\
\begin{cases}[0,1],&\beta\le a,\\ \varnothing,&\beta>a.\end{cases}
\tag{7}
\]

The first two sets mean \(N\le T^{4a}\) and \(N\ge T^{1-2a}\), intersected with \([1,T]\). Their overlap begins when \(6a\ge1\). At \(a=0\), they contain only the boundary scales \(N=1,T\), if those exact scales occur in the decomposition. They are not positive-width power bands. At larger cutoffs the displayed intersections prevent fictitious bands beyond \([1,T]\).

Because the packet has \(\beta<1/6\), its actual untreated set is simply

\[
\mathcal U_{p,\delta}=
\begin{cases}
(4a,1-2a),&a<\beta,\\
\varnothing,&a\ge\beta.
\end{cases}
\tag{8}
\]

Thus nonempty middle bands are disjoint from the closed certified bands; endpoints belong to the certified part. Equivalently all blocks are certified if

\[
\delta\ge\max\{0,(p-2)\beta-1,(p-q)\beta\}.
\tag{9}
\]

The dyadic rounding of the boundary scales changes constants only. The singleton and the \(N\ge T\) rapid tails have the separate coverage specified by the packet. Summing a fixed moment over the stipulated number of active blocks incurs only logarithms.

**Shell normalization, sufficient arithmetic threshold, and current certificate.** Direct substitution, with no heuristic shell counting, gives

\[
\int_I|B_N(R)|^{2k}\,dR
=\frac12\int_J x^{-(k+1)/2}|Z_N(x)|^{2k}\,dx
\asymp_k T^{-(k+1)}K_{2k}(N).
\tag{10}
\]

For an exact bridge, interpolation with the displayed supremum gives

\[
\int_I|H_N|^p\ll T^\varepsilon M_N^{p-2k}T^{-(k+1)}K_{2k}(N).
\tag{11}
\]

The harmless errors need not have the same supremum as \(H_N\). A valid way to retain (11) plus a harmless \(p\)-error is to split into \(|E_N|\ge|H_N|/2\) and its complement. On the first set \(|H_N|^p\le2^p|E_N|^p\); on the second \(|B_N|\ge|H_N|/2\), hence

\[
|H_N|^p\ll_{p,k}M_N^{p-2k}|B_N|^{2k}+|E_N|^p.
\tag{12}
\]

Equations (10)--(12) prove (3), without multiplying a harmless lower-moment error by a possibly large supremum power. In \(X\)-notation the threshold is \(X^{1+k/2+\delta/2+\varepsilon}M_N^{-(p-2k)}\). The root envelope alone gives the more restrictive but sufficient threshold

\[
K_{2k}\ll T^{k+2+\delta+\varepsilon}N^{-(p-2k)/4}.
\tag{13}
\]

The supplied variance bound gives the present unconditional interpolation certificate

\[
\int_I|H_N|^{2k}\ll T^{1+\varepsilon}N^{-1/2}M_N^{2k-2},\qquad
\int_I|H_N|^p\ll T^{1+\varepsilon}N^{-1/2}M_N^{p-2}.
\tag{14}
\]

In particular its sufficient condition for the radius target is

\[
(p-2)s(\alpha)-\alpha/2\le\delta,
\tag{15}
\]

independently of which intermediate \(2k\) is chosen. With an exact bridge the associated current shell certificate is

\[
K_{2k}\ll T^{k+2+\varepsilon}N^{-1/2}M_N^{2k-2}.
\tag{16}
\]

If there is merely a harmless \(2k\)-moment bridge error, what follows for the actual \(K_{2k}\) is instead (16) **plus** \(O(T^{k+2+\varepsilon})\). This additional term cannot be discarded when asserting a saving in \(N\). The direct radius certificate (14) does not have that problem. With \(M_N\le N^{1/4}\), the principal expression in (16) becomes \(T^{k+2+\varepsilon}N^{(k-2)/2}\).

**The dependence on moment order needed for the full target.** Applied along any sequence of available fixed orders, (2) reaches every exponent \(1/4+\eta\) precisely when its positive excess can be made arbitrarily small:

\[
\inf_p\frac{3+2\delta_p}{4(p+1)}=0.
\tag{17}
\]

For \(\delta_p\ge0\), this is equivalent to the existence of \(p_j\to\infty\) with \(\delta_{p_j}/p_j\to0\). It is sufficient to have \(\delta_p=o(p)\) for all sufficiently large available fixed orders, but a subsequence suffices. Constants may depend arbitrarily on a fixed order: choose the order after the desired epsilon, then let \(X\) tend to infinity. No uniform limit in a growing order is assumed.

One fixed order leaves the positive excess \(3/(4(p+1))\), even if \(\delta=0\). A linear loss \(\delta_p\sim cp\), \(c>0\), leaves the excess \(c/2\). These are limitations of this moment-to-pointwise implication; a separately proved stronger pointwise mechanism would require its own argument.

**All Gaussian orders versus one Gaussian order.** Since

\[
XH^k=T^{k+2}N^{-k/2},
\]

the hypothetical bound \(K_{2k}\ll T^\varepsilon XH^k\) implies

\[
\int_I|H_N|^p\ll T^{1+\varepsilon}
\left(1+N^{-k/2}M_N^{p-2k}\right),
\tag{18}
\]

with harmless errors retained as in (12). For \(p=2k\) this is a baseline \(T^{1+\varepsilon}\) moment. A hierarchy for all fixed \(k\), applied to every untreated block for those orders, therefore gives arbitrarily high complete even moments with \(\delta_{2k}=0\). Together with the full complements already identified, (17) proves the quarter bound conditionally on that hierarchy.

For a **single fixed** \(k\) and \(p\ge2k\), its exact sufficient block condition is

\[
\boxed{(p-2k)s(\alpha)-k\alpha/2\le\delta.}
\tag{19}
\]

The set in (19), wherever the Gaussian hypothesis is available, must be joined to (7), the singleton, the tails, and the harmless errors. Any remaining block is an unproved complement. This union formula applies without discarding endpoints or assuming that a hypothesis valid in one middle strip is valid elsewhere.

Even granting a fixed-order Gaussian theorem on **all** \(1\le N\le T\), its largest exponent in (18) is

\[
\max_{0\le\alpha\le1}\bigl((p-2k)s(\alpha)-k\alpha/2\bigr)
=\begin{cases}0,&2k\le p\le4k,\\(p-4k)\beta,&p>4k.\end{cases}
\tag{20}
\]

To verify this exactly, split at \(\alpha=4\beta\) and \(\alpha=1-2\beta\). The expression is respectively

\[
\frac{p-4k}{4}\alpha,\qquad
(p-2k)\beta-\frac{k\alpha}{2},\qquad
\frac{p-2k-(p-k)\alpha}{2}.
\]

For \(p>4k\), its maximum is at \(4\beta\). Thus a fixed Gaussian order certifies all orders through \(4k\) at baseline, but its resulting loss for higher orders is \((p-4k)\beta\), whose ratio to \(p\) tends to \(\beta>0\). Combining the weak-tail bounds can improve finite constants in this loss; it does not remove the positive asymptotic slope on a fixed interior scale, as the peak control below confirms.

For an explicit description of the Gaussian safe bands when \(p>4k\): if \(\delta\ge(p-4k)\beta\), all scales are safe. Otherwise the low safe band ends at
\(\alpha_L=4\delta/(p-4k)<4\beta\), and the high safe band starts at

\[
\alpha_G=\begin{cases}
2((p-2k)\beta-\delta)/k,&\delta\ge(p-k)\beta-k/2,\\
(p-2k-2\delta)/(p-k),&\delta<(p-k)\beta-k/2.
\end{cases}
\tag{21}
\]

The first crossing lies on the plateau and the second on the descending high-frequency branch. The bands are closed; the untreated interval is open. For \(2k\le p\le4k\), (19) holds everywhere for every \(\delta\ge0\).

A hierarchy restricted to the single strip chosen for one finite order is insufficient for the all-order conclusion. If \(\delta_p=o(p)\), then (1) has \(a_p\to0\); the untreated middle approaches the whole interior \((0,1)\). Its low and high complements must be re-established for every order, or the hierarchy must cover them too.

## 4. First doubtful or unproved step

The algebraic and measure-theoretic transfers above are proved from the packet. The first missing arithmetic assertion is a uniform estimate for the **actual complete** shell quantity on every remaining block, for example

\[
\int_{X/2}^{3X}|Z_N(x)|^{2k}\,dx
\ll_{p,k,\varepsilon}
T^{k+2+\delta_p+\varepsilon}
\min\{N^{1/4},T^\beta,(T/N)^{1/2}\}^{-(p-2k)},
\]

for some appropriate fixed \(k\le p/2\), at every \(\alpha\in\mathcal U_{p,\delta_p}\) not already covered by (15) or another proved bound. The exact real moving endpoints and the full integral \(J\) are part of this assertion. For the quarter theorem, such input is required along unbounded orders with \(\delta_p/p\to0\), or it must be replaced by a separately proved pointwise mechanism. The stronger all-order Gaussian hierarchy is one sufficient input, not a consequence of its sixth-moment member.

The packet does not define the internal signed arithmetic structure of \(Z_N\). Therefore this report cannot identify or verify a cancellation lemma inside it, cannot assert a character-specific improvement, and cannot certify an unsigned analogue. The per-block interpretation of bridge errors stated in Section 2 is also an explicit seam to confirm if the packet intended a weaker aggregate-error statement.

## 5. Required controls and outcomes

**The required \(p=12,\delta=4/25\) control.** Here

\[
p-q=\frac{20}{13},\qquad
\frac{1+\delta}{p-2}=\frac{29}{250},\qquad
\frac{\delta}{p-q}=\frac{13}{125},\qquad a=\frac{13}{125}.
\]

Thus the low and high safe bands are respectively
\(\alpha\le52/125\) and \(\alpha\ge99/125\). If \(\beta\le13/125\), equivalently \(\theta\le151/500\), they are supplemented by the global beta cap and all blocks are safe. Otherwise the untreated middle is exactly \((52/125,99/125)\).

The complete radius target is \(T^{29/25+\varepsilon}\), the area-variable twelfth moment is \(X^{102/25+\varepsilon}\), and the pointwise consequence is

\[
P(x)\ll x^{102/325+\varepsilon}.
\]

For \(k=3\), the exact sufficient shell condition is

\[
K_6\ll T^{129/25+\varepsilon}M_N^{-6},
\]

and the root-envelope version is \(T^{129/25+\varepsilon}N^{-3/2}\). The Gaussian hypothesis is

\[
K_6\ll XH^3=T^5N^{-3/2},
\]

which is sufficient, including at the band endpoints. Its normalized sixth moment is \(TN^{-3/2}\), and interpolation gives the twelfth-moment bound \(TN^{-3/2}M_N^6\le T\). This certifies the middle even more strongly than the requested target; the complete conclusion still uses the separately retained complements at their stated target.

In contrast, the principal variance-based current certificate is
\(K_6\ll T^{5+\varepsilon}N^{-1/2}M_N^4\), or \(T^{5+\varepsilon}N^{1/2}\) with the root envelope. Relative to the root-envelope target its gap is \(N^2/T^{4/25}\). Directly, (14) gives \(\int|H_N|^{12}\ll TN^2\), sufficient only when \(\alpha\le2/25\) if that root envelope alone is used. Outcome: all powers and Jacobians agree; the current variance certificate does not supply the claimed Gaussian gain. Any bridge-error addition to the shell certificate remains as stated after (16).

**Constant normalization control.** Take \(Z_N(x)=H^{1/2}\) on \(J\). Then
\(K_{2k}=|J|H^k\asymp XH^k\), while
\(B_N(R)=H^{1/2}R^{-1/2}\asymp N^{-1/4}\), so
\(\int_I|B_N|^{2k}\asymp TN^{-k/2}\). Outcome: (10) and the Gaussian normalization pass. No additional factor of \(N\), \(T\), or shell length is available from normalization.

**Single narrow peak control against fixed-order extrapolation.** Fix \(k\), set \(C=\max\{4k,q\}\), and choose a fixed

\[
0<s<\min\left\{\beta,\frac16,\frac{3}{2(C+1)}\right\}.
\]

Use the scale \(N=T^{4s}\), envelope \(M=T^s\), and a peak with a positive plateau of height comparable to \(M\), supported on an interior radius interval of length comparable to
\(L=T^{1-Cs}\). Smooth cutoffs, or a trapezoidal peak, preserve every following power. Put \(Z_N(R^2)=R^{1/2}H_N(R)\). Then

\[
\int|H_N|^r\asymp LM^r=T^{1+(r-C)s}.
\]

The envelope is allowed since \(s<\beta,1/6\). For \(1\le V\le M\), the level-set measure is at most a constant times \(L\le TM^{-q}\le TV^{-q}\), so the stipulated tail bound holds. The variance holds because
\(LM^2\le T^{1-2s}=TN^{-1/2}\), using \(C\ge4\). The fixed Gaussian order holds because
\(LM^{2k}\le T^{1-2ks}=TN^{-k/2}\), using \(C\ge4k\). Nevertheless the \(p\)-moment has loss \((p-C)s\) for every \(p>C\). Its loss divided by \(p\) tends to \(s>0\).

For \(k=3\), \(C=12\), so this model has a Gaussian sixth moment and a baseline twelfth moment but higher moments \(T^{1+(p-12)s}\). This directly rejects the proposed deduction of all high moments from Gaussian \(K_6\).

Even the elementary persistence constraint need not repair this extrapolation: a nonnegative trapezoidal peak with \(P(R^2)=R^{1/2}H_N(R)/\pi\) has a descending derivative in the \(x\)-variable of size at most a constant times \(T^{-3/2+(C+1)s}=o(1)\). After a fixed amplitude scaling, \(P(x)+\pi x\) is monotone; the initial \(x^\theta\) bound also holds since \(s<\beta\). This is a functional control model, not an assertion that an arithmetic circle discrepancy or the actual arithmetic \(Z_N\) realizes the peak. Outcome: fixed-order-to-all-order extrapolation is invalid on the supplied size and moment information. No numerical experiment or theorem certification was used.

## 6. Dependencies and exact artifacts used

Only the following files were read:

1. `protocol.md`.
2. `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/briefs/blind_moment_hierarchy_statement.md`.

No graph, active campaign, generated general brief, strategy, predecessor report, sibling report, web page, or external theorem was consulted. The derivation uses layer cake, the change of variables \(x=R^2\), elementary interpolation with an explicit error split, and monotonicity. All controls are analytic. The only file written is this task-specific report.

## 7. Recommended state effect

Retain this report as independent evidence for the conditional transfer formulas, complete shell normalization, exact safe-band bookkeeping, and the fixed-order extrapolation obstruction. Any promotion must be decided by the conductor after its required seam reviews and graph validation. In particular, do not promote the missing arithmetic shell hierarchy, arbitrarily high moments, or the quarter theorem from this report. Confirm the complete bridge-error hypothesis before accepting the per-block version of (3). No shared-state edit, successor round, or further task is initiated here.
