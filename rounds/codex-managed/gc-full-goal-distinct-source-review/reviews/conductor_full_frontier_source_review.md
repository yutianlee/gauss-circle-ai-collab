# Round217 conductor review of the complete-frontier source report

## 1. Result

GREEN for the bounded source applications and their stated limitations.
Claimant:reports/full_frontier_sources.md, SHA256
3fcd969a5fb4b53edb6cbbd337b19ae18c363fb44bc1cdc0042a80f05c1fd338.
Conductor NONBLIND review, 2026-09-28; campaign
gc-full-goal-distinct-source-review; starting graph
f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7.
Neither of the two audited theorems supplies the complete signed target.
No source theorem is newly imported into the accepted graph.

## 2. Exact statements and hypotheses

Kim--Ko, arXiv:2511.04503v2, Theorem1.1, is a weighted square-function
estimate for Fourier support in an S^-1 neighborhood of the truncated
parabola, with 2<=p<=4 and 0<=H<=1. Its factor is S^epsilon times
max_U kappa_p,H(U)+S^-100, where
kappa=max_(V subset U)(H(V)/|V|)^(1/4)(H(U)/|U|)^(1/p-1/4).
The V and U dimensions and the full range of scales are essential.

Granville--Lamzouri, arXiv:2604.02306v1, Theorem1.1 first range,
requires a multiplicative f with |f|<=1, reduced a/q,
|alpha-a/q|<=1/(qx), (log x)^(2+eta)<=q<=x/(log x)^(3+eta),
q<=x^(1-eta), and 2<=M<<min(q^(1-eta/4)/log^2 x,
exp((1/2-eta)sqrt(log x loglog x))). It expresses the original
linear-phase sum as a specified large-prime sum plus
O(x/(sqrt(M)log x)); it does not estimate that prime sum by zero.
The report explicitly confines its application to this first range.

## 3. Proof and independent cost verification

The parabola lift xi_n=sqrt(n/(4N)), x=2sqrt(N)R has spatial windows
of length N in x and sqrt(N) in R. At S comparable to N, a coarse
S^-1/2 cap can contain O(sqrt(N)) integers n. With actual normalized
coefficients its triangle bound is N^(-1/4+epsilon) A_N, and there
are O(sqrt(N)) caps. The fourth power of their square function thus
costs A_N^4 N^epsilon over area O(N^2), giving N^(2+epsilon) A_N^4.
The band-limited trace uses a bounded nonnegative integrable transverse
weight; the smallest V has unit size, so max kappa_4 is only O(1),
with no power saving. Dividing dx by sqrt(N) yields the local cost
N^(3/2+epsilon) A_N^4. Covering the radius window costs T/sqrt(N),
giving T N^(1+epsilon) A_N^4 per block. Schwartz decay sums this
to T^(2+epsilon) for the complete series. Raising by the inherited
physical ceiling gives T^(2+(p-4)beta+epsilon), worse than the accepted
moment certificate. This is a failure of this explicit coarse-cap
application; no impossibility claim about all uses of the theorem follows.
Theorem1.1 does not itself cover p=12.

For the multiplicative theorem, r2(n)/4 is not 1-bounded. Opening its
actual divisor formula exposes chi4(d), which does meet that hypothesis,
but the phase is R sqrt(kd). At d comparable to D, kd comparable to N,
and R comparable to T, linearization on length ell has error
O(T sqrt(N) ell^2/D^2), requiring ell<=C D/(T sqrt(N))^(1/2).
The number of pieces is at least of order (T sqrt(N))^(1/2).
Translation to a short interval loses multiplicativity; subtraction
of prefixes keeps the ambient error. Even a hypothetical direct short
interval version with the displayed M range gives only x^(1-o(1))
error, not a fixed power saving, and its large-prime term remains.
The exact major-arc control chi4(d)e(d/4)=i for odd d, zero otherwise,
shows why the missing small-denominator contribution cannot be dropped.
It is a coefficient control, not a lower bound on an actual large value.

The full frontier and anchored-energy costs agree with the closed216
packet. The fixed rho<=208/2625 anchored hypothesis is unproved and
only a fixed-order milestone. Its fixed distribution tail cannot by
itself yield E(p)=1+o(p). A fixed twelfth target likewise cannot.

## 4. First doubtful or unproved step

The first gaps are the required signed distinct-class estimate or the
complete anchored off-diagonal energy, not a source citation. Neither
the weighted trace calculation nor the multiplicative decomposition
closes these gaps. The report's conditional family is sufficient under
its explicit all-orders premises, but no such premise is established.
The independent moment-family review supplies a stronger absorption
argument: it can remove the need for intermediate orders, without
proving any new signed-integral premise. This refines the strategy;
it does not falsify the report's deliberately inductive proof.

## 5. Controls and outcomes

GREEN: exact versions and theorem ranges; actual r2 versus bounded
multiplicative coefficients; cap occupancy and radius Jacobian; covering
and tails; real endpoints and prefixes; q=4 character control; fixed-order
versus full-quarter scope. All calculations are analytical, with no
numerical experiment. Source inspection checks statements and application
hypotheses, not a new proof of the source theorems themselves.

## 6. Dependencies and exact sources

The claimant, its allowed context, protocol, graph, frozen217 strategy,
closed216 synthesis and accepted204/216 kernels were read. The primary
theorem statements were checked directly on 2026-09-28:
- https://arxiv.org/html/2511.04503v2, Theorem1.1 and its weight definitions.
- https://arxiv.org/html/2604.02306v1, Theorem1.1, formula(1.12),
  preceding definition of L(x), and introductory multiplicativity convention.

No withdrawn claim or conjectural high moment was imported. This is a
conductor line/source review, not statement-only independent rederivation.

## 7. Recommended state effect

Retain the report as a qualified source and strategy no-go. Keep every
complete M1/M2/GAR parent, signed moment target and quarter theorem open.
Use the complete actual I12 target as the next analytic objective, while
tracking an explicitly sufficient unbounded-fixed-order family. No graph
promotion follows from either source resemblance or conditional family.
