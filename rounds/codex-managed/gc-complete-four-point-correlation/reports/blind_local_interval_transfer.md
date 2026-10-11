# Round212: statement-only local interval transfer

Campaign: `gc-complete-four-point-correlation`. Task: `blind_local_interval_transfer`. Role: independent statement-only rederiver. Generated: 2026-09-28. Status: conditional analytical report; no arithmetic hypothesis is asserted. Graph hash: withheld from the isolated packet and not inspected. Exact context: `protocol.md` and `rounds/codex-managed/gc-complete-four-point-correlation/briefs/blind_local_interval_statement.md` only.

## 1. Result: conditional transfer and sharp parameter criterion

The proposed transfer is valid if its local hypothesis really holds on every real interval of the stated length. A partition-prefix replacement is also valid, but needs a controlled number of cells, as specified below. For every fixed positive epsilon, with the usual allocation of epsilon between hypotheses and conclusions,

\[
 A_4\ll T^\epsilon\left\{
       NT^{-1+6b}
       +N^{\eta+\nu}T^{(1-6b)(1-\nu)}\right\}.
 \tag{1}
\]

Before absorption into epsilon, the first summand can be multiplied by \((1+\log T)^2\). All shifts, including small shift products and repeated shifts, occur in the exact finite bound (10) below.

The exact criterion for this route to give \(A_4\ll T^{4b+\epsilon}\) throughout the required band is

\[
 \boxed{(10-4\nu+2\eta)b\ge 1+\eta,\qquad
        0<b<\tfrac16.}
 \tag{2}
\]

There is an admissible such \(b\) precisely when \(\nu+\eta<1\). Equality in (2) is allowed. Section 5 gives an abstract nonnegative coefficient model showing that, when (2) fails strictly, the stated local hypotheses alone do not imply the desired bound. That model is not a counterexample about \(r_2\).

For the hypothetical local square-root input \((\nu,\eta)=(1/2,0)\), criterion (2) is \(b\ge1/8\). At \(b=83/650\), the discrepancy term at the upper scale is \(T^{159/325+\epsilon}\), whereas the permitted bound is \(T^{166/325+\epsilon}\). Thus there is a power margin \(7/325\) in that term. Subject also to the two explicitly permitted downstream hypotheses, this certifies

\[
 |F_N|\ll T^{83/650+\epsilon},\qquad
 P(X)\ll X^{102/325+\epsilon}.
 \tag{3}
\]

It does not certify the full-quarter target. Even if the square-root local input and downstream hypotheses were available uniformly as \(b\) varied, its best exponent through this route is \(5/16\), obtained at \(b=1/8\). Across the whole stated family \(0\le\nu\le1,\eta\ge0\), the infimum permitted value of \(b\) is \(1/10\), obtained at \((\nu,\eta)=(0,0)\); thus the family cannot approach \(b=0\) by this transfer.

## 2. Exact statement and hypotheses

Use the packet's definitions without replacing \(L,K\) by nonintegral quantities. Put

\[
 s=N^{1/2}T^{-2b}>1,\quad
 H=L-1,\quad J=K-1,\quad
 q=TN^{-3/2},\quad Q=T^{1-6b},\quad p=1-\nu.
\]

Then \(L=\lceil s\rceil\), \(K=\lceil s^2\rceil\), with the stated maxima by 2 understood. In particular,

\[
 \begin{gathered}
 1\le H\le J,\qquad s\le L\le2s,\qquad
 s^2\le K\le2s^2,\\
 \tfrac{s}{2}\le H<s,\qquad
 \tfrac{s^2}{2}\le J<s^2,\qquad
 \tfrac14\le\frac{HJ}{LK}<1,\\
 qLK\ge Q,\qquad \tfrac14Q\le qHJ<Q.
 \tag{4}
 \end{gathered}
\]

At the closed lower endpoint \(N=T^{4b}\), interpret the strict inequalities for \(H,J,qHJ\) as non-strict: \(L=K=2\), \(H=J=1\), and \(qHJ=Q\). Every estimate below still holds.

For each shift, take its real overlap

\[
 I_{h,k}=[A,B]=[N,4N-h-k].
\]

It has length between \(N\) and \(3N\): indeed \(h+k<\sqrt N+N<2N\). The weight vanishes smoothly at both endpoints and outside this overlap. The enlarged region in the hypothesis must contain these overlaps and every interval used below. Coefficients are interpreted with the stated zero extension. An atom at \(A\) has zero weight.

The density and local discrepancy assumptions are exactly the hypothetical ones in the packet, with constants uniform in shifts, real interval endpoints, and \(R\) in its fixed compact range of positive multiples of \(T\). In particular, the discrepancy scale uses \(T\), independently of \(R\).

Here is a sufficient precise weaker partition hypothesis. For each \((h,k)\), have a partition

\[
 A=x_0<x_1<\cdots<x_M=B,
 \qquad x_j-x_{j-1}\le\ell_{h,k},\qquad
 M\le C(1+\Lambda_{h,k}),
 \tag{5}
\]

with a fixed uniform constant \(C\). Require, for every cell and every real \(x\in[x_{j-1},x_j]\), including its right endpoint,

\[
 \left|\sum_{x_{j-1}<n\le x}a_{h,k}(n)
      -\int_{x_{j-1}}^x\mu_{h,k}(t)\,dt\right|
 \ll T^\epsilon N^\eta\ell_{h,k}^\nu.
 \tag{6}
\]

The cells are half-open on the left for their atomic sums, so every relevant atom is counted once. The partition can be fixed from \(T,N,h,k\), independently of \(R\), for example by consecutive cells of length \(\ell\) and one terminal shorter cell. If a different partition is supplied, its prefix bounds and cell count must still be uniform in the allowed parameters. Merely bounding full-cell totals, or allowing an uncontrolled number of tiny cells, is insufficient for this proof. A lower length bound comparable to \(\ell\) on all but a bounded number of cells is one alternative way to ensure the cell-count condition.

No global unweighted discrepancy hypothesis is substituted for (6). The permitted finite physical bridge and reconstruction are used only for the conditional consequence (3).

## 3. Proof and derivation

### Phase and weight estimates

The exact mixed-difference identity is

\[
 \phi(t)=-\frac R4\int_0^h\int_0^k(t+u+v)^{-3/2}\,dv\,du.
\]

Throughout the overlap, \(N\le t+u+v\le4N\). Differentiation gives precisely the derivatives used here:

\[
 \begin{aligned}
 \phi'(t)&=\frac{3R}{8}\int_0^h\int_0^k(t+u+v)^{-5/2}\,dv\,du,
 \\
 \phi''(t)&=-\frac{15R}{16}\int_0^h\int_0^k(t+u+v)^{-7/2}\,dv\,du.
 \end{aligned}
\]

Consequently, uniformly in the full range,

\[
 |\phi(t)|\asymp\Lambda,\qquad
 \phi'(t)\asymp\Lambda/N>0,\qquad
 |\phi''(t)|\ll\Lambda/N^2.
 \tag{7}
\]

These formulas remain valid when \(h=k\); no difference of shifts appears in a denominator. Products and differentiation of the four smooth masks give \(\|W\|_\infty\ll1\), \(\|W'\|_\infty\ll N^{-1}\). For \(f(t)=W(t)e(\phi(t))\),

\[
 \|f'\|_\infty\ll(1+\Lambda)/N=\ell^{-1},\qquad
 \int_A^B|f'(t)|\,dt\ll1+\Lambda.
\]

### Local summation by parts, including its boundary terms

Write

\[
 E_j(x)=\sum_{x_{j-1}<n\le x}a(n)
               -\int_{x_{j-1}}^x\mu(t)\,dt.
\]

Stieltjes integration by parts on a cell gives the exact identity

\[
 \sum_{x_{j-1}<n\le x_j}a(n)f(n)
   -\int_{x_{j-1}}^{x_j}\mu(t)f(t)\,dt
 = f(x_j)E_j(x_j)-\int_{x_{j-1}}^{x_j}E_j(t)f'(t)\,dt.
\]

There is no left boundary contribution because \(E_j(x_{j-1})=0\). This formula is valid for integer and noninteger real endpoints, including an atom at the right endpoint. Summing cells yields

\[
 D=\int_A^B\mu(t)W(t)e(\phi(t))\,dt
       +\sum_{j=1}^M f(x_j)E_j(x_j)
       -\sum_{j=1}^M\int_{x_{j-1}}^{x_j}E_j(t)f'(t)\,dt.
 \tag{8}
\]

The terminal boundary term is zero because \(f(B)=0\). The internal terms have all been retained; they cannot be canceled merely because the underlying intervals abut, since \(E_j\) resets at each cell. From (5)--(6), their combined contribution and the integral errors are at most

\[
 \begin{aligned}
 C T^\epsilon N^\eta\ell^\nu
       \left\{\sum_j|f(x_j)|+\int_A^B|f'(t)|\,dt\right\}
 &\ll T^\epsilon N^\eta\ell^\nu(1+\Lambda)\\
 &=T^\epsilon N^{\eta+\nu}(1+\Lambda)^{1-\nu}.
 \tag{9}
 \end{aligned}
\]

The every-interval input implies (6) on the equal-length partition just described, whose number of cells is at most \(3(1+\Lambda)+1\). This also explains why a global discrepancy estimate cannot silently replace the local input: no such replacement was used or proved.

### The smooth main density integral

Put \(B_0=\mu W\). Its zeroth and first derivatives are bounded by \(T^\epsilon\) and \(T^\epsilon/N\), respectively, and it vanishes at the overlap endpoints. The trivial integral bound is \(O(T^\epsilon N)\). A single ordinary integration by parts, using (7), gives

\[
 \int_A^B B_0e(\phi)
 =-\frac1{2\pi i}\int_A^B
       \left(\frac{B_0'}{\phi'}-
                    \frac{B_0\phi''}{(\phi')^2}\right)e(\phi),
\]

with no endpoint contribution. Thus the integral is also \(O(T^\epsilon N/\Lambda)\). Combining these two bounds,

\[
 \left|\int_A^B\mu W e(\phi)\right|
       \ll T^\epsilon\frac{N}{1+\Lambda}.
\]

This integral has not been discarded or identified with a discrepancy error.

### Exact finite average and its simplification

Equations (8)--(9) first give the complete finite bound

\[
 \boxed{
 A_4\ll\frac{T^\epsilon}{LK}
    \sum_{h=1}^{H}\sum_{k=1}^{J}
       \left\{\frac{N}{1+qhk}
                +N^{\eta+\nu}(1+qhk)^p\right\}.}
 \tag{10}
\]

For additional precision one may replace the first summand in (10) by the actual absolute density integral divided by \(T^\epsilon\); equation (8) is the underlying identity.

The small-product set \(qhk\le1\) has the exact cardinality

\[
 C_0(q;H,J)=\sum_{h=1}^H
            \min\!\left(J,\left\lfloor\frac1{qh}\right\rfloor\right).
 \tag{11}
\]

Its terms in (10) are retained and bounded by
\(\ll T^\epsilon(N+N^{\eta+\nu})C_0/(LK)\). In particular,
\(C_0\le q^{-1}\sum_{h\le H}h^{-1}\), so its density contribution is at most \(T^\epsilon NQ^{-1}\sum_{h\le H}h^{-1}\). No nonstationary decay larger than the trivial bound was assumed at small product.

The repeated shifts form the subset \(h=k\), \(1\le h\le H\), and their full contribution is bounded by

\[
 \frac{T^\epsilon}{LK}\sum_{h=1}^H
      \left\{\frac{N}{1+qh^2}
            +N^{\eta+\nu}(1+qh^2)^p\right\}.
 \tag{12}
\]

This is already part of (10), not an additional term. The local density hypothesis must hold for these repeated configurations as well. At the lower closed endpoint the only pair is \((1,1)\), demonstrating why they cannot be dropped as an exceptional empty or negligible set.

Writing \(\mathcal H_m=\sum_{r=1}^m r^{-1}\), the density part of (10) satisfies

\[
 \frac{N}{LK}\sum_{h,k}\frac1{1+qhk}
 \le\frac{N}{qLK}\mathcal H_H\mathcal H_J
 \le NQ^{-1}\mathcal H_H\mathcal H_J
 \ll NT^{-1+6b}(1+\log T)^2.
 \tag{13}
\]

For the discrepancy part, since \(0\le p\le1\) and \(qHJ\le Q\),

\[
 \frac1{LK}\sum_{h,k}(1+qhk)^p\le(1+Q)^p\ll Q^p.
 \tag{14}
\]

This average really has that order of magnitude: at least \(HJ/4\) pairs have \(h\ge H/2,k\ge J/2\), their products satisfy \(qhk\ge Q/16\), and \(HJ/(LK)\ge1/4\). Hence its lower bound is
\(\frac1{16}(1+Q/16)^p\). Thus the replacement by \(Q^p\) is not a loss of a missing saving from shift averaging. Equations (13)--(14) prove (1).

### Exponents, downstream consequence, and endpoints

For all \(N\le T^{1-2b}\), the density term in (1) is at most \(T^{4b}\). Since \(\eta+\nu\ge0\), the largest discrepancy exponent is attained at the upper end of the band:

\[
 E=(1-2b)(\eta+\nu)+(1-6b)(1-\nu)
   =1-6b+4b\nu+(1-2b)\eta.
\]

The inequality \(E\le4b\) is exactly (2). When \(\eta+\nu=0\) all scales have the same discrepancy exponent; there is no need for a strict monotonicity assertion. The criterion is feasible below \(1/6\) exactly when \(\eta+\nu<1\), because its threshold is
\((1+\eta)/(10-4\nu+2\eta)\).

The original strict scale endpoints cause no limiting issue. The estimates hold on their closed enlargement, with the explicit lower-end ceiling convention in (4). At the lower endpoint the discrepancy exponent is
\(4b(\eta+\nu)+(1-6b)(1-\nu)\), no larger than its upper-end value. Real endpoints were handled in (8). If \(\ell<1\), the proof still holds: empty cells cause no difficulty, the given discrepancy control applies to their prefixes, and the stated bound remains an upper bound. For bounded \(T\), all the scale and shift ranges are bounded; the estimates above use \(1+\Lambda\), exact ceilings, and harmonic numbers with positive integer indices and do not invoke a large-parameter approximation. Their constants stay uniform.

Under criterion (2), the exact ceiling inequalities also give

\[
 N/L^2\le T^{4b},\qquad N/K\le T^{4b}.
\]

Only now, assuming the supplied finite physical bridge and reconstruction, one obtains \(|F_N|\ll T^{b+\epsilon}\) and \(P(X)\ll X^{1/4+b/2+\epsilon}\). For \(\nu=1/2,\eta=0\), the error exponent is \(1-4b\); at \(83/650\) the arithmetic in section 1 follows exactly. Its limiting permissible \(b=1/8\) yields \(5/16\). No inference to \(b=0\) or the full-quarter conjecture is justified.

## 4. First doubtful or unproved step

There is no remaining unproved step in the conditional analytic transfer just derived. The first substantive unproved input in an application is the existence of genuine smooth densities for the actual arithmetic coefficients with the uniform local discrepancy bound (including every repeated shift and every real moving interval). This report neither assumes that input has been established elsewhere nor derives it from unweighted global discrepancy.

The finite physical bridge and complete reconstruction are additional hypotheses supplied solely for the requested consequence. Their validity is not reviewed or promoted here. The report's sharpness construction concerns the general hypotheses, not the arithmetic family.

## 5. Required control tests and outcomes

All controls here are analytical; no numerical experiment was used.

**Cell-boundary and partition control — pass.** Identity (8) preserves every internal reset boundary term. With only an arbitrary fine partition, the demonstrated bound would be \(T^\epsilon N^\eta\ell^\nu[M+1+\Lambda]\), so the controlled cell count is a genuine requirement of the stated weaker replacement. Full-cell totals alone do not furnish the prefix estimate used under the integral.

**Small-product, repeated-shift, and endpoint control — pass.** The exact count (11), repeated subset (12), lower endpoint \(L=K=2\), positive phase derivative (7), and half-open endpoint convention all enter the proof explicitly. There is no division by \(h-k\), no omission of small products, and no unproved sum-to-integral replacement in the transfer.

**Sharpness under the abstract assumptions — pass, with explicit scope.** Fix \(b\in(0,1/6)\), set \(N=c_NT^{1-2b}\) with a fixed \(0<c_N<1\), and let \(T\) grow. This lies strictly inside the required band for all sufficiently large \(T\). Choose one permissible nonnegative smooth mask \(g_N(t)=g(t/N)\), where \(g\) is supported in \([1,4]\) and equals 1 on \([2,3]\). Fix a single \(R_0=c_RT\) in the allowed compact range before defining any coefficient. Below \(\phi_0\) means the phase at this fixed \(R_0\).

For the positive proportion of shifts with \(h\ge H/2,k\ge J/2\), set

\[
 A_{h,k}=N^\eta\ell_{h,k}^{\nu-1},\qquad
 a_{h,k}(n)=A_{h,k}[1+\cos(2\pi\phi_{0,h,k}(n))]
\]

on the real overlap's integer points, and zero outside it. On all other shift pairs set \(a=0\). Take \(\mu_{h,k}=0\) everywhere. These are real nonnegative coefficients and genuine smooth zero densities. They are fixed independently of the subsequently varying test \(R\).

For these large shifts,

\[
 \Lambda\asymp Q=T^{1-6b}\longrightarrow\infty,
 \quad \ell\asymp N/Q\asymp T^{4b}\longrightarrow\infty,
 \quad \Lambda/N\asymp T^{-4b}\longrightarrow0.
\]

Every real interval of length at most \(\ell\) contains at most \(\ell+1\) integers. Hence, including intervals crossing the zero-extension boundary,

\[
 \left|\sum_{u<n\le v}a(n)\right|
 \le 2A_{h,k}(\ell+1)
 \le4N^\eta\ell^\nu
\]

for large enough \(T\). The local input therefore holds with no epsilon loss, on every permitted interval, and uniformly for every test \(R\) because its scale uses \(T\) and the coefficients were already fixed.

At \(R=R_0\), define \(S_m=\sum_nW(n)e(m\phi_0(n))\) for \(m=0,1,2\). Since \(h+k=o(N)\), the common plateau of the four masks has length comparable to \(N\), so \(S_0\asymp N\). For \(m=1,2\), the same integration by parts as above gives
\(\int W(t)e(m\phi_0(t))\,dt=O(N/\Lambda)\).
Elementary quadrature on unit intervals gives

\[
 \left|\sum_n f(n)-\int f(t)\,dt\right|
 \le\int|f'(t)|\,dt\ll1+\Lambda
\]

for these compactly supported smooth functions. This inequality follows directly by comparing \(f(n)\) with \(f(t)\) on each \([n,n+1]\) and integrating \(|f'|\); it is not an imported asymptotic theorem. Therefore

\[
 S_m=O(N/\Lambda+1+\Lambda)=o(N),\qquad m=1,2,
\]

uniformly on the selected shifts. Expanding the cosine exactly,

\[
 D_{h,k}(R_0)=A_{h,k}\left(S_1+\tfrac12S_0+\tfrac12S_2\right),
\]

so \(|D_{h,k}(R_0)|\gg A_{h,k}N\). Averaging over that positive proportion yields

\[
 A_4(R_0)\gg N^{\eta+\nu}Q^{1-\nu}
             \asymp T^E.
\]

If \(E>4b\), this contradicts \(A_4\ll T^{4b+\epsilon}\) for sufficiently small fixed positive epsilon. Thus (2) is sharp for the stated general class of inputs and admissible masks. The construction deliberately uses shift-dependent artificial coefficients; it is never an actual \(r_2\) counterexample and does not show failure of any conjectured arithmetic local estimate. It identifies precisely what the abstract input alone can certify.

## 6. Dependencies and exact artifacts used

Read context consists only of:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-four-point-correlation/briefs/blind_local_interval_statement.md`.

No graph, campaign state, general brief, strategy file, previous report, sibling report, web page, or numerical computation was consulted. The proof uses the packet's smooth-mask hypotheses, genuine-density bounds, hypothetical local discrepancy bound (or the precisely specified partition-prefix substitute), and elementary integration by parts and finite summation. The finite physical bridge and complete reconstruction are conditional dependencies only of the stated consequence for \(F_N\) and \(P(X)\).

## 7. Recommended state effect

**Promote only the conditional analytical transfer, if it passes the conductor's remaining required reviews and graph validation.** Its statement must include the local arithmetic hypothesis as unresolved, the controlled-cell version of any partition substitute, the exact criterion (2), and complete inclusion of repeated shifts and moving real endpoints.

**No change** to actual arithmetic local-discrepancy obligations or unconditional Gauss-circle claims. Retain the abstract sharpness model as a limitation on what this input can imply. No authoritative state, validation matrix, proof draft, synthesis, or successor-round plan was edited or proposed by this task.
