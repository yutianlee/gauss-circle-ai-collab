# Round216: isolated collective distinct-class rederivation

## 1. Result

Campaign: gc-actual-radical-high-values. Task: isolated_distinct_class_rederivation.
Role: bounded statement-only independent algebraic seam. Generated: 2026-09-28.
Supplied metadata graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
The graph itself was not read.

Under precisely the abstract hypotheses of the new packet, put
\(p_h(R)=\sum_{d>Q}f_d(R)^h\), so \(p_1=Z\). Then

\[
 E_{12}
 =\sum_{\substack{m_1,\ldots,m_{12}\ge0\\
                  \sum_{h=1}^{12}h m_h=12}}
 \frac{12!(-1)^{12-\sum_hm_h}}
      {\prod_{h=1}^{12}h^{m_h}m_h!}
 \prod_{h=1}^{12}p_h^{m_h}.                                      \tag{1}
\]

In particular, the profile \(m_1=12\) is \(Z^{12}\), and every other
profile in (1) retains the collective signed power \(Z^{m_1}\).
With all repeated profiles included, the integrated absolute error obeys

\[
 \boxed{\;
 D(T):=\int_{\mathbb R}w(R/T)|Z(R)^{12}-E_{12}(R)|\,dR
 \ll_\varepsilon
 T^{4/5+\varepsilon}+T^{8\beta-1/5+\varepsilon}.
 \;}                                                            \tag{2}
\]

Since \(1/8<\beta<13/100\), this is

\[
 D(T)\ll_\varepsilon T^{8\beta-1/5+\varepsilon},
 \qquad \frac45<8\beta-\frac15<\frac{21}{25}<\frac{29}{25}.          \tag{3}
\]

Thus (2) is smaller than the target \(T^{29/25}\) by a fixed power for
sufficiently small \(\varepsilon\). There is no new logarithmic factor
from the algebra or passage to infinite sums.

Writing

\[
 I(T)=\int w(R/T)|Z(R)|^{12}\,dR,\qquad
 J(T)=\int w(R/T)E_{12}(R)\,dR,
\]

the exact transfer is

\[
 |I(T)-J(T)|\le D(T),\qquad I(T)\ge0,\qquad J(T)\ge-D(T).             \tag{4}
\]

In particular a one-sided upper bound on the real signed integral \(J\)
is sufficient to upper-bound \(I\), with the error (2). The converse
upper bound on \(I\) gives an absolute bound on \(J\), again with that
error. No pointwise positivity or torus interpretation of \(E_{12}\) is
assumed.

## 2. Exact statement and hypotheses

For each real \(T\ge2\), let \(Q=\lfloor T^{2/5}\rfloor\). The index
family \(\mathcal D\) is any subset of the integers \(d>Q\).
The real functions \(f_d\) satisfy \(|f_d(R)|\le A_d\), where
\(A_d\ge0\) and \(\sum_{d\in\mathcal D}A_d<\infty\) for each fixed
\(T\). The integrals in the packet are understood to be defined; as
usual one may take the functions to be measurable. For every
\(h=2,\ldots,12\) and every \(\eta>0\),

\[
 S_h:=\sum_{d\in\mathcal D}A_d^h
 \ll_\eta Q^{1-3h/4+\eta}.                                        \tag{5}
\]

The weight \(w\) is fixed, nonnegative, smooth, and compactly supported.
The hypotheses supply, for every integer \(0\le r\le10\),

\[
 M_r:=\int_{\mathbb R}w(R/T)|Z(R)|^r\,dR
 \ll_\eta T^\eta\left[T+
                  T^{\max(r-2,0)\beta}\right],                   \tag{6}
\]

where \(1/8<\beta<13/100\) is fixed and \(Z=\sum_{d\in\mathcal D}f_d\).
For \(r=0\), the integrand \(|Z|^0\) is understood to be one, including
where \(Z=0\). This is the zeroth moment, not an indicator.

The ordered distinct-class sum is

\[
 E_{12}(R)=
 \sum_{\substack{(d_1,\ldots,d_{12})\in\mathcal D^{12}\\
                  d_i\ne d_j\ (i\ne j)}}
 \prod_{j=1}^{12}f_{d_j}(R).
                                                                    \tag{7}
\]

All constants may depend on the fixed hypothesis constants, \(\beta\),
and \(w\). The packet does not grant uniformity of those constants as
\(\beta\) approaches either endpoint. No property of the labels beyond
their being distinct indices is used.

## 3. Proof and derivation

### 3.1. Finite identity, with all collective signs retained

First take a finite index family. Let \(\Pi_{12}\) denote the set of
partitions of the twelve labeled positions. For \(\pi\in\Pi_{12}\), put

\[
 \mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!.
\]

For a tuple \(\boldsymbol d=(d_1,\ldots,d_{12})\), let \(\tau\) be its
partition into equal-label positions. Then

\[
 {\bf1}_{\{d_1,\ldots,d_{12}\ {\rm pairwise\ distinct}\}}
 =\sum_{\pi:\,\pi\ {\rm refines}\ \tau}\mu(\pi).                    \tag{8}
\]

To prove (8), the sum on the right factors over the blocks of \(\tau\).
On a block with \(k\) positions the factor is

\[
 \sum_{\rho\in\Pi_k}
       \prod_{B\in\rho}(-1)^{|B|-1}(|B|-1)!
 =\sum_{\sigma\in\mathfrak S_k}(-1)^{k-c(\sigma)},                  \tag{9}
\]

where \(c(\sigma)\) is the number of cycles. This equality follows
because a set of \(b\) labeled elements has \((b-1)!\) cyclic orderings.
The sign on the right is the sign of the permutation. It sums to zero
for \(k\ge2\), by the sign-reversing bijection that composes with a fixed
transposition, and is one for \(k=1\). Therefore the product is one
exactly when all blocks of \(\tau\) are singletons, proving (8).

Multiply (8) by \(\prod_j f_{d_j}\) and sum all ordered tuples.
For each \(\pi\), labels are forced equal within each block but are
unrestricted between blocks, giving the finite polynomial identity

\[
 E_{12}=\sum_{\pi\in\Pi_{12}}\mu(\pi)\prod_{B\in\pi}p_{|B|}.         \tag{10}
\]

For a profile \(\boldsymbol m=(m_1,\ldots,m_{12})\), there are

\[
 \frac{12!}{\prod_{h=1}^{12}(h!)^{m_h}m_h!}
\]

partitions with \(m_h\) blocks of size \(h\). Multiplying by the cycle
factors in \(\mu\) reduces this coefficient to the one in (1).
Consequently the exact difference is

\[
 Z^{12}-E_{12}
 =-\!\!\sum_{\substack{m_1,\ldots,m_{12}\ge0\\
                      \sum_hh m_h=12\\m_1\ne12}}
 \frac{12!(-1)^{12-\sum_hm_h}}
      {\prod_{h=1}^{12}h^{m_h}m_h!}\,
 Z^{m_1}\prod_{h=2}^{12}p_h^{m_h}.                                \tag{11}
\]

For example the first profiles give
\(66p_2Z^{10}-440p_3Z^9-1485p_2^2Z^8+2970p_4Z^8\) in the difference.
Formula (11), rather than this illustrative initial list, specifies
every term including all higher multiplicities.

### 3.2. Infinite sums and integration

Fix \(T\), put \(S_1=\sum_d A_d<\infty\), and exhaust \(\mathcal D\)
by finite subsets \(\mathcal D_N\). Then \(Z_N\to Z\) uniformly in \(R\).
For \(h\ge2\), \(\sum_dA_d^h<\infty\), either by (5) or by
\(\sum_d A_d^h\le S_1^h\), so \(p_{h,N}\to p_h\) uniformly as well.
The ordered sum in (7) converges absolutely and uniformly, since

\[
 \sum_{\substack{d_1,\ldots,d_{12}\\{\rm distinct}}}
       \prod_j|f_{d_j}(R)|\le S_1^{12}.
\]

More explicitly, the sum of the absolute values of all terms using at
least one label outside \(\mathcal D_N\) is at most

\[
 12S_1^{11}\sum_{d\notin\mathcal D_N}A_d\longrightarrow0.            \tag{12}
\]

This upper bound follows by a union bound over the twelve positions,
and remains valid after restricting to distinct tuples. When \(S_1=0\)
all functions vanish and convergence is immediate.

Thus (10)--(11) pass to the limit uniformly for this fixed \(T\).
Each side and each of their finitely many polynomial terms are bounded
by a fixed numerical constant times \(S_1^{12}\). Since
\(\int w(R/T)\,dR=T\int w<\infty\), the identities also pass through
the integral, as does the integral of their absolute difference.
No uniform-in-\(T\) rate of convergence is needed here.

Importantly, (6) is used only for the full \(Z\) after taking this
limit. The hypotheses do not grant (6) for truncated sums \(Z_N\), and
no such assertion is made.

### 3.3. The bound for every profile

For a non-discrete profile in (11), define

\[
 r=m_1,\qquad S=\sum_{h=2}^{12}h m_h=12-r,\qquad
 m=\sum_{h=2}^{12}m_h.
\]

The exact feasible range is

\[
 0\le r\le10,\qquad
 1\le m\le\left\lfloor\frac{12-r}{2}\right\rfloor,\qquad
 m_h\ge0,\quad\sum_{h=2}^{12}h m_h=12-r.                           \tag{13}
\]

There can be no \(r=11\), because a non-singleton part has size at
least two. For each fixed \(r\), every value of \(m\) in (13) is
realizable: use \(m-1\) parts of size two and one part of size
\(S-2(m-1)\), which lies between two and twelve. All profiles with
given \(r,m\) have the same exponent in the ensuing bound.

Since the functions are real, \(|p_h|\le S_h\) also for odd \(h\).
Equations (5)--(6) imply

\[
 \begin{aligned}
 \int w(R/T)|Z|^r\prod_{h=2}^{12}|p_h|^{m_h}\,dR
 &\ll_\eta
 Q^{\,m-3(12-r)/4+m\eta}\,
 T^\eta\left[T+T^{\max(r-2,0)\beta}\right].
 \end{aligned}                                                    \tag{14}
\]

For \(T\ge2\), integer rounding gives
\[
 \tfrac12T^{2/5}\le Q\le T^{2/5}.
\]
Thus, after allocating the arbitrarily small losses, the complete
two-term exponent for this profile is

\[
 \boxed{\quad
 T^{\,1+2m/5-3(12-r)/10+\varepsilon}
 +T^{\,2m/5-3(12-r)/10+\max(r-2,0)\beta+\varepsilon}.
 \quad}                                                         \tag{15}
\]

To verify the allocation explicitly, for a requested \(\varepsilon>0\)
choose the same
\(\eta=\min\{1/4,5\varepsilon/17\}\) in all finitely many hypotheses.
Then the power of \(Q\) in (14) is negative, and the rounding factor
is bounded by a numerical constant for each profile. The total
\(T\)-loss is
\[
 \left(1+\frac{2m}{5}\right)\eta
 \le\frac{17}{5}\eta\le\varepsilon,
\]
because \(m\le6\). There are finitely many profiles, so their
coefficients and hypothesis constants can all be absorbed after
this common choice. In particular, no uncontrolled multiple use of
an \(\varepsilon\)-loss occurs.

### 3.4. Exhaustive profile comparison

For fixed \(r\), both exponents in (15) increase with \(m\).
It suffices to use \(m_{\max}=\lfloor(12-r)/2\rfloor\), retaining the
fact that all smaller \(m\)'s have already been covered by (15).
The following table covers every possible \(r\) and hence every
feasible profile:

| \(r\) | Feasible \(m\) | \(\delta_r=2m_{\max}/5-3(12-r)/10\) | Exponent from \(T\) | Exponent from the second moment term |
|---:|:---|---:|---:|:---|
| 0 | \(1,\ldots,6\) | \(-6/5\) | \(-1/5\) | \(-6/5\) |
| 1 | \(1,\ldots,5\) | \(-13/10\) | \(-3/10\) | \(-13/10\) |
| 2 | \(1,\ldots,5\) | \(-1\) | \(0\) | \(-1\) |
| 3 | \(1,\ldots,4\) | \(-11/10\) | \(-1/10\) | \(\beta-11/10\) |
| 4 | \(1,\ldots,4\) | \(-4/5\) | \(1/5\) | \(2\beta-4/5\) |
| 5 | \(1,\ldots,3\) | \(-9/10\) | \(1/10\) | \(3\beta-9/10\) |
| 6 | \(1,\ldots,3\) | \(-3/5\) | \(2/5\) | \(4\beta-3/5\) |
| 7 | \(1,2\) | \(-7/10\) | \(3/10\) | \(5\beta-7/10\) |
| 8 | \(1,2\) | \(-2/5\) | \(3/5\) | \(6\beta-2/5\) |
| 9 | \(1\) | \(-1/2\) | \(1/2\) | \(7\beta-1/2\) |
| 10 | \(1\) | \(-1/5\) | \(4/5\) | \(8\beta-1/5\) |

The largest first exponent is \(4/5\), and the largest second exponent
is \(8\beta-1/5\), both arising at \(r=10,m=1\), the single-pair
profile. For example, subtracting any other second exponent from
\(8\beta-1/5\) gives a strictly positive quantity for the supplied
range of \(\beta\), as is also immediate from the table.
Summing (14) in (11), taking the absolute value of each already
collected polynomial term, proves (2).

### 3.5. Endpoint, logarithmic, and target bookkeeping

The algebraic bound before using the strict lower endpoint is
\[
 D(T)\ll_\varepsilon
 T^{\,\max\{4/5,\,8\beta-1/5\}+\varepsilon}.                        \tag{16}
\]
At the formal value \(\beta=1/8\), the two exponents merely coincide:
the finite sum produces no logarithm. At the formal value
\(\beta=13/100\), the second exponent is \(21/25\). These statements
about the algebra do not assert the hypotheses at either endpoint.
For the granted strict range, the target gap is

\[
 \frac{29}{25}-\left(8\beta-\frac15\right)
 =\frac{34}{25}-8\beta>\frac8{25}.                                \tag{17}
\]

For instance, fixing any \(0<\varepsilon<8/25\) in (3) yields
\(D(T)=o(T^{29/25})\). More precisely one may use any
\(\varepsilon<34/25-8\beta\) for the fixed supplied \(\beta\).
Every pre-existing loss in (5)--(6) has been accounted for in (15).
There is no limiting integral at a critical exponent here and no
new logarithmic loss. The integer cutoff and \(T=2\) endpoint are
covered directly by the floor comparison, so no large-\(T\)-only
replacement of \(Q\) is made.

### 3.6. Exact direction of signed-integral transfer

All integrands defining \(I,J\) are real and integrable, by Section 3.2.
Since \(Z\) is real, \(Z^{12}=|Z|^{12}\); nonnegativity of \(w\) gives
\(I\ge0\). Integrating the exact difference proves (4).

For any specified nonnegative function \(M(T)\):

* If \(J(T)\le M(T)\), then \(I(T)\le M(T)+D(T)\).
* If \(|J(T)|\le M(T)\), the same upper bound on \(I\) follows.
* If \(I(T)\le M(T)\), then
  \(-D(T)\le J(T)\le M(T)+D(T)\), and consequently
  \(|J(T)|\le M(T)+D(T)\).

These are the precise one-sided and absolute implications. More
generally a lower bound on \(J\) transfers to \(I\) after subtracting
\(D\), and a lower bound on \(I\) transfers to \(J\) in the same way.
For a positive target scale \(F(T)\) with \(D(T)\ll F(T)\), the three
claims \(I(T)\ll F(T)\), \(J(T)\le C F(T)\), and
\(|J(T)|\ll F(T)\) are equivalent up to constants. If \(F\) is smaller
than the known error, the error cannot be removed by this identity.
In particular the equivalence applies at the requested exponent
\(29/25\), or at \(29/25+\varepsilon\), by (17).

## 4. First doubtful or unproved step

There is no unproved algebraic, summability, partition, or exponent step
in (1)--(17), conditional on the packet's granted hypotheses (5)--(6).
The resulting comparison is a conditional reduction, not a proof of a
bound for \(J(T)\). Any attempted proof of the target twelfth moment
through this identity first needs an independent upper bound on the
real signed integral \(J(T)\) at the desired scale. Conversely, an
independently proved twelfth-moment upper bound would bound \(|J(T)|\)
by Section 3.6.

No upper bound on \(J(T)\) at exponent \(29/25\) follows merely from the
identity or the displayed error estimate. No attempt to supply such
an extra bound, or to infer an arithmetic origin for \(f_d\), is part
of this report.

## 5. Required controls and outcomes

### 5.1. Fewer than twelve labels

For a finite family of size \(N<12\), the defining sum (7) is empty,
so \(E_{12}=0\). Identity (8) proves that (1) then vanishes identically,
with all cancellations among its power-sum terms retained. Therefore
(11) equals \(Z^{12}\), exactly as required. The identity does not
mistakenly discard the remaining twelfth power.
For \(N=0\), every \(p_h\) and \(Z\) is zero and the identity is zero
on both sides. Each monomial has positive total degree twelve, so
the conventional value of a zeroth power introduces no nonzero term.
Outcome: passes.

### 5.2. All functions coincide, or vanish

For a finite family of size \(N\) with \(f_d(R)=x(R)\), one has
\[
 p_h=Nx^h,\quad Z=Nx,\quad
 E_{12}=N(N-1)\cdots(N-11)x^{12}.
\]
Substitution into (1), or the indicator proof itself, gives the
polynomial identity
\[
 \sum_{\pi\in\Pi_{12}}\mu(\pi)N^{|\pi|}
       =N(N-1)\cdots(N-11).
\]
Thus the difference is
\[
 \bigl[N^{12}-N(N-1)\cdots(N-11)\bigr]x^{12},
\]
including \(N<12\) and \(x=0\). No requirement of distinct function
values is hidden in the use of distinct labels.
If infinitely many indexed functions all coincide, the summable
envelope forces their common value to be zero for every \(R\):
a nonzero common value at any point would imply
\(\sum_dA_d=\infty\). The infinite coincident case therefore also
passes, as the zero case.

### 5.3. \(E_{12}\) need not be nonnegative

With exactly twelve labels, take eleven functions equal to \(x(R)\)
and the remaining one equal to \(-x(R)\). Then
\[
 E_{12}(R)=-12!\,x(R)^{12},
\]
which is negative wherever \(x\ne0\). This control can respect the
granted bounds: for each \(T\), choose twelve admissible labels and
take \(x=Q^{-3/4}\) constant in \(R\). Then
\(\sum A_d^h=12Q^{-3h/4}\) satisfies (5), and
\(|Z|=10Q^{-3/4}\) gives (6) with fixed constants.
Hence positivity cannot be added even under the quantitative packet
hypotheses. This calculation is algebraic, not a numerical experiment.
Outcome: a positivity interpretation is rejected.

### 5.4. Collective identity versus absolute repeated-tuple expansion

The original repeated-label part is
\[
 \sum_{\substack{d_1,\ldots,d_{12}\\\text{not pairwise distinct}}}
       \prod_j f_{d_j}.
\]
Taking absolute values before collection instead bounds it by
\[
 \sum_{\substack{d_1,\ldots,d_{12}\\\text{not pairwise distinct}}}
       \prod_j |f_{d_j}|.
\]
For instance, a bound for tuples with one chosen equal pair already
involves \(S_2 S_1^{10}\), where \(S_1=\sum A_d\). The hypotheses give
only fixed-\(T\) finiteness for \(S_1\), not the signed moments (6)
for a function represented by \(S_1\).

In contrast, (11) first performs the complete signed collection,
producing \(66p_2Z^{10}\) and its overlap-correction terms. Taking
absolute values afterward leaves the full signed \(Z\) inside
\(|Z|^r\), to which (6) actually applies. The algebraic corrections
handle all repeated-label intersections; no absolute repeated-tuple
bound has been equated to (2). Outcome: the distinction is essential
and retained.

### 5.5. Infinite limits and exhaustive partitions

The finite identity is proved before any integration. Uniform
absolute convergence in (12) justifies all infinite-sum passages.
Only after that passage are the supplied moments for the full \(Z\)
used. Profiles with \(r=0,1,\ldots,10\), including all odd block sizes
and all multiplicities, are exhausted by (13) and the table.
The forbidden \(r=11\) does not introduce an ungranted eleventh
moment. The only \(r=12\) profile is exactly the leading \(Z^{12}\)
term removed in (11). Outcome: passes.

All controls in this section are exact analytical or algebraic
controls. No numerical experiment, external source, source expansion,
or successor task was undertaken.

## 6. Dependencies and exact artifacts used

The new mathematical input is solely:

rounds/codex-managed/gc-actual-radical-high-values/briefs/isolated_distinct_class_statement.md

The protocol and permitted prior isolated context already available
to this agent were:

1. protocol.md.
2. rounds/codex-managed/gc-actual-radical-high-values/briefs/blind_radical_cutoff_statement.md.
3. rounds/codex-managed/gc-actual-radical-high-values/reports/blind_radical_cutoff.md,
   frozen at SHA256
   e0accd624e0d9f1b95644c3456ed6302f9ac145aa6d4356aba4fb6cf82c7595e.

No result from the prior cutoff report is needed to prove the present
abstract identity or estimate; hypotheses (5)--(6) are granted here
independently. No claimant, ledger, graph, manifest, strategy, current
sibling, or outside source was read. The supplied graph hash remains
unverified metadata. Only this assigned review file was written during
this seam; the original report remains frozen.

## 7. Recommended state effect

Retain the exact collective identity (1), its infinite-sum justification,
the complete error bound (2), and the signed-integral transfer (4) as
an independent conditional seam verification. The strongest resulting
error exponent from these hypotheses is
\(8\beta-1/5+\varepsilon<21/25+\varepsilon\), not merely the requested
comparison exponent \(29/25\).

No arithmetic theorem, distinct-class integral bound, or new graph
claim is promoted by this report. Any graph effect remains the
conductor's responsibility after the required validation. No state
file or original report was edited, and no next-round work was begun.
