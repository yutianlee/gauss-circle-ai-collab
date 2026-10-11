# Round212 independent actual-sector seam review

## 1. Result and review verdict

**GREEN for the final hash-bound ledger's actual safe-sector bounds, fixed-interior small-phase lower bound R212.1, and conditional local-discrepancy transfer R212.5--R212.7.** The complete actual four-point upper bound remains unproved.

The two Fejer/Cauchy mass inequalities, intervening Jensen step, axis removal, quadrant reindexing, small-phase cosine bound, and treatment of possible sign changes of the real mask all check. The lower bound applies to actual complete correlations with a modulus before the shift average; it is stronger than a lower bound on a positive error certificate. It does not lower-bound the original wave or circle discrepancy.

One precision repair was requested and is present in the final ledger. Its near-edge consequence now excludes only a **uniform fixed power saving below \(T^{4b}\) for the actual small-phase sector over the whole open band**. It neither identifies a smooth-density main term nor infers failure of a moving-edge \(o(T^{4b})\) bound from the stated fixed-interior result.

- Campaign: `gc-complete-four-point-correlation`; round: 212.
- Task: `independent_actual_sector_review`.
- Role: separate same-round **NONBLIND** seam review after completion of the isolated local-transfer task. No new blind credit is claimed.
- Generated: 2026-09-28.
- Graph hash, quoted from the ledger only: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
- Final reviewed ledger SHA-256: **`4f4ea9fb9bde6b0521f504d40e5d1c5574e1389254c96d03ddc713b0f69f8f97`**.
- Effort: entirely analytical; no numerical experiment or new external theorem.

The earlier isolated report remains unchanged. It is not an artifact dependency of this review and is not presented as a blind review of the conductor's ledger.

## 2. Exact hypotheses and review scope

The actual coefficient is \(r_2(n)\), not a centered or artificial replacement. Write

\[
 g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),\qquad
 s_n=r_2(n)g_N(n)e(R\sqrt n),
\]

with the inherited real smooth masks, \(\Psi(0)=1\), a fixed nonzero \(v\) supported in \([1,4]\), and uniform bounds \(g_N^{(j)}\ll_j N^{-j}\). The permitted round211 ledger supplies these smoothness conventions. All sequences are zero extended; \(R\) lies in a fixed compact positive multiple of \(T\), and \(b=83/650\).

Use the exact positive integers

\[
 L=\max(2,\lceil N^{1/2}T^{-2b}\rceil),\qquad
 K=\max(2,\lceil NT^{-4b}\rceil),
\]

and the complete raw four-point correlations

\[
 D_{h,k}=\sum_n r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k)
               W_{h,k}(n)e(\phi_{h,k}(n)),
\]
\[
 A_4=\frac1{LK}\sum_{1\le h<L,\,1\le k<K}|D_{h,k}|,
 \qquad U=N^{3/2}/T,\qquad \Lambda_{h,k}=hk/U.
\]

Define the small-phase sector explicitly by

\[
 A_{4,\mathrm{small}}=
 \frac1{LK}\sum_{\substack{1\le h<L,\,1\le k<K\\hk\le U}}|D_{h,k}|.
\]

The upper sector bounds hold throughout \(T^{4b}<N<T^{1-2b}\), including bounded \(T\) after changing constants. The actual lower statement is only for sufficiently large \(T\) on

\[
 T^{\alpha_0}\le N\le T^{\alpha_1},\qquad
 \tfrac23<\alpha_0\le\alpha_1<1-2b,
 \tag{V1}
\]

with the margins fixed. It asserts, uniformly over that range and the full \(R\)-window,

\[
 A_4\ge A_{4,\mathrm{small}}
       \gg\frac{N^{5/2}}{TLK}\gg NT^{6b-1}.
 \tag{V2}
\]

The smooth means and short-interval discrepancies in the final part of the ledger are separately hypothetical. Their validity for these actual arithmetic coefficients is not supplied by (V2).

## 3. Independent proof and seam checks

### A. Actual upper sectors and exact cutoffs

The inherited divisor envelope and size-one raw mask give \(|D_{h,k}|\ll NT^\epsilon\) uniformly. Since \(K\ge L\), there are exactly \(L-1\) possible repeated-shift pairs. Their averaged contribution is at most

\[
 \frac{L-1}{LK}NT^\epsilon\le\frac NK T^\epsilon
 \le T^{4b+\epsilon}.
\]

These are positive repeated shifts, not the zero axes used later in the mass argument; no claim that their phase vanishes is needed.

If \(U<1\), the small-phase set is empty. Otherwise its cardinality is bounded by
\(\sum_{h\le U}\lfloor U/h\rfloor\ll U\log(2U)\), with no fixed-shift or nondegeneracy restriction. The exact cutoff comparison
\(LK\asymp N^{3/2}T^{-6b}\) then gives

\[
 A_{4,\mathrm{small}}
 \ll T^\epsilon\frac{NU}{LK}
 \ll T^\epsilon NT^{6b-1}\le T^{4b+\epsilon}.
 \tag{V3}
\]

The harmonic logarithm is absorbed into the arbitrarily small epsilon loss. Summing the two sector upper bounds can double count their intersection but remains a valid upper bound. The unpaid complement is exactly \(h\ne k\), \(\Lambda>1\).

### B. Actual nonnegative mass and the two finite smoothing steps

Set \(a_n=r_2(n)|g_N(n)|\). Because \(v\) is nonzero and continuous, some closed interval \([u_1,u_2]\subset(1,4)\) has \(|v|\ge c>0\). On the full band, \(N/T\le T^{-2b}\), so \(\Psi(\sqrt{t/T})\to1\) uniformly on the mask support. Thus \(|g_N|\gg1\) on this interval for all sufficiently large \(T\).

The elementary disk-area estimate suffices for the required first moment. Unit squares based at the integer lattice points compare the union with disks whose radii differ from \(\sqrt x\) by a fixed constant; their areas differ by \(O(\sqrt x+1)\). Consequently
\(\sum_{n\le x}r_2(n)=\pi x+O(\sqrt x+1)\), with the origin convention changing only a constant. Subtracting at \(u_1N,u_2N\) yields

\[
 \sum_n a_n\gg N,
 \qquad\sum_n a_n^4\ll N^{1+\epsilon}.
 \tag{V4}
\]

The second estimate follows from the divisor envelope after allocating its epsilon sufficiently small. No conjectural circle-error estimate is used.

Take an ambient integer interval of length \(M\le3N+2\) supporting \(a\). For a nonnegative sequence \(z\) supported in such an interval and integer \(Q\ge2\), exact expansion gives

\[
 \frac1Q\sum_{|h|<Q}w_Q(h)\sum_nz_nz_{n+h}
 =\frac1{Q^2}\sum_x\left(\sum_{j=0}^{Q-1}z_{x+j}\right)^2,
 \quad w_Q(h)=1-|h|/Q.
 \tag{V5}
\]

Every \(z_n\) occurs in exactly \(Q\) moving sums; at most \(M+Q-1\) starting indices contribute. Cauchy therefore lower-bounds the right side by \((\sum z_n)^2/(M+Q)\). These facts hold on the integers with zero extension; there is no periodic completion.

For fixed \(k\), use \(z_n=a_na_{n+k}\), whose support remains within the original ambient interval. Define \(C_{h,k}\) and \(B_Q\) as in the ledger. Since
\(Q^{-1}\sum_{|k|<Q}w_Q(k)=1\), averaging (V5) in \(k\) and applying Jensen gives

\[
 B_Q\ge\frac1{M+Q}
 \left[\frac1Q\sum_{|k|<Q}w_Q(k)\sum_na_na_{n+k}\right]^2.
\]

Apply (V5) again, this time to \(a_n\), to conclude

\[
 B_Q\ge\frac{(\sum_na_n)^4}{(M+Q)^3}\gg N
 \qquad (Q\le N).
 \tag{V6}
\]

The denominator power three and normalization \(Q^{-2}\) are correct. This does not assume an individual four-point asymptotic or independence of shifted coefficients.

### C. Axes and positive quadrants

For every integer \(k\), Cauchy gives

\[
 C_{0,k}=\sum_na_n^2a_{n+k}^2\le\sum_na_n^4\ll N^{1+\epsilon}.
\]

The two weighted axes in \(B_Q\) therefore contribute at most
\(2N^{1+\epsilon}/Q\), since each one-dimensional weight sum is \(Q\). Their intersection can be counted twice in this upper bound without harm.

The identities \(C_{-h,k}=C_{h,k}\) and \(C_{h,-k}=C_{h,k}\) follow by changing the summation variable. The weights are even, so the four strict quadrants have equal mass. If \(N^\epsilon/Q=o(1)\), subtracting the axes from (V6) yields

\[
 \sum_{1\le h<Q,\,1\le k<Q}w_Q(h)w_Q(k)C_{h,k}
 \gg NQ^2.
 \tag{V7}
\]

This includes \(h=k>0\). Residue obstructions that force particular correlations to vanish are compatible with the averaged inequality.

### D. Uniform choice of the small box, rounding, and cosine

Choose the fixed small constant in the ledger as \(\eta_0\), to distinguish it from the discrepancy exponent later, and put
\(Q=\lfloor\eta_0\sqrt U\rfloor\). Under (V1),

\[
 Q\asymp\sqrt U,\qquad
 Q\gg T^{\kappa},\quad\kappa=(3\alpha_0-2)/4>0,
\]
\[
 \frac{\sqrt U}{L}\ll N^{1/4}T^{2b-1/2}
 \le T^{(6b-1)/4}=o(1),\qquad
 \frac QN\ll N^{-1/4}T^{-1/2}
 \le T^{-1/2-\alpha_0/4}.
 \tag{V8}
\]

For sufficiently large \(T\), these imply \(Q\ge2\), \(Q\le L\le K\), \(Q\le N\), and \(Q^2\asymp U\), with uniform constants. Taking the divisor epsilon less than \(\kappa/(2\alpha_1)\), for example, makes the axis error \(o(N)\) uniformly.

The exact phase identity is

\[
 \phi_{h,k}(n)=-\frac R4\int_0^h\int_0^k
                      (n+u+v)^{-3/2}\,dv\,du.
 \tag{V9}
\]

For a nonzero summand \(n\ge N\), and for \(h,k<Q\), its absolute value is at most \(C TQ^2/N^{3/2}\le C\eta_0^2\). Choosing \(\eta_0\) once using the upper bound for \(R/T\) ensures \(\cos(2\pi\phi)\ge3/4\) throughout the complete support and the full \(R\)-window. Taking \(\eta_0<1\) also ensures every pair in the box belongs to \(hk\le U\).

### E. Signed-mask crossings and the actual complete correlations

When the four real mask values have nonnegative product, their contribution to \(\Re D_{h,k}\) is at least \(3/4\) of the corresponding summand of \(C_{h,k}\), because all four arithmetic coefficients are nonnegative.

If the mask product is negative, at least two of the four values have opposite signs. Continuity provides a zero between the smallest and largest arguments. Those arguments are all within distance \(h+k<2Q\) of one another. The derivative bound \(\|g_N'\|_\infty\ll N^{-1}\) therefore implies that each of the four values has modulus \(O(Q/N)\). Thus the total absolute contribution of all such crossing terms, for a fixed pair, is

\[
 \ll N^{1+\epsilon}(Q/N)^4.
\]

The constant in this estimate can absorb the difference between a negative real contribution and \(3/4\) of its positive absolute amplitude. This proves exactly

\[
 \Re D_{h,k}\ge\tfrac34 C_{h,k}
           -O\bigl(N^{1+\epsilon}(Q/N)^4\bigr).
 \tag{V10}
\]

There is no assumption about the number of zeros or sign changes of the fixed mask. The derivative bound controls every crossing term at once, including zeros or crossings close to an exterior support boundary.

Summing the error in (V10) with the nonnegative Fejer weights costs at most
\(O(N^{1+\epsilon}Q^2(Q/N)^4)\). Relative to (V7), this is \(O(N^\epsilon(Q/N)^4)=o(1)\), uniformly by (V8) after a sufficiently small epsilon allocation. Since \(|D|\ge\Re D\) and the weights are at most one,

\[
 \sum_{h<Q,k<Q}|D_{h,k}|
 \ge\sum_{h<Q,k<Q}w_Q(h)w_Q(k)\Re D_{h,k}
 \gg NQ^2\gg NU.
 \tag{V11}
\]

These are complete \(n\)-correlations, not sums truncated to a favorable interior subinterval. Dividing by \(LK\), using \(LK\le4N^{3/2}T^{-6b}\), and noting that all other terms of \(A_4\) are nonnegative prove (V2).

This step specifically uses \(r_2(n)\ge0\). It is not a lower bound for the centered coefficient alternative, where arithmetic sign changes would require a different argument.

### F. Exact lower-bound scope after the repair

At any fixed \(N=T^\alpha\) with \(2/3<\alpha<1-2b\), (V2) has power \(\alpha+6b-1\). Its gap to \(4b\) is \(1-2b-\alpha>0\). Thus the lower bound is compatible with the target upper bound, and even with a power saving at any one fixed interior scale.

If instead a fixed \(\delta>0\) were a uniform power saving for the entire open band, choose one fixed admissible \(\alpha\) with \(1-2b-\alpha<\delta/2\). The lower bound would exceed \(T^{4b-\delta}\) by a positive power; the same argument applies to \(T^{4b-\delta+\epsilon}\) after taking \(\epsilon<\delta/4\). This proves the repaired uniform-power statement.

Constants in the given theorem may depend on the fixed interior margins. Its formulation therefore does not by itself address a moving \(\alpha(T)\) tending to the edge or rule out a little-oh bound there. It also says nothing about a separately chosen smooth-density main term. The final ledger now makes both restrictions explicit. Because \(A_4\) takes moduli before the shift average, no signed-wave or circle-discrepancy lower bound follows.

### G. Separate check of the conditional local transfer

For the hypothetical local input, write \(f=We(\phi)\), \(\ell=N/(1+\Lambda)\), and let \((x_{j-1},x_j]\) be the controlled partition cells. Put

\[
 E_j(x)=\sum_{x_{j-1}<n\le x}a_{h,k}(n)
                -\int_{x_{j-1}}^x\mu_{h,k}(t)\,dt.
\]

The exact cell error is

\[
 f(x_j)E_j(x_j)-\int_{x_{j-1}}^{x_j}E_j(t)f'(t)\,dt.
 \tag{V12}
\]

In particular, resetting the primitive does not cancel its internal right-boundary terms. The half-open convention counts every integer atom once and is valid for real endpoints.

From (V9),

\[
 \phi'(t)=\frac{3R}{8}\int_0^h\int_0^k(t+u+v)^{-5/2}\,dv\,du
              \asymp\Lambda/N,
\]

and \(\phi''\ll\Lambda/N^2\); both bounds hold across the complete overlap, including \(h=k\). Consequently \(|f'|\ll(1+\Lambda)/N=\ell^{-1}\). Each cell has bounded variation cost, and the number of cells is \(O(1+\Lambda)\). Thus (V12) and the stated prefix bound give

\[
 |D-\int\mu We(\phi)|
 \ll T^\epsilon N^\eta\ell^\nu(1+\Lambda)
 =T^\epsilon N^{\eta+\nu}(1+\Lambda)^{1-\nu}.
 \tag{V13}
\]

This proves R212.5 with all boundaries retained. The input must hold at every real prefix inside each cell, and a supplied partition must satisfy the controlled cell count. Full-cell totals or arbitrarily many tiny cells do not justify this estimate.

The smooth density can be incorporated in the amplitude in round211's continuous integration by parts because all its scaled derivatives are bounded by \(T^\epsilon\). Its full shift average, including small products and repeated shifts, is

\[
 \frac1{LK}\sum_{h,k}|\int\mu We(\phi)|
 \ll T^\epsilon\frac{N^{5/2}}{TLK}
 \ll T^\epsilon NT^{6b-1}\le T^{4b+\epsilon}.
 \tag{V14}
\]

For \(0\le\nu\le1\), the complete average of (V13) is bounded using
\(\Lambda_{h,k}\le TLK/N^{3/2}\asymp T^{1-6b}\). This is R212.6. Since \(\eta+\nu\ge0\), its largest exponent across the band is

\[
 (1-2b)(\eta+\nu)+(1-6b)(1-\nu)
 =1-6b+4b\nu+(1-2b)\eta.
\]

Requiring that exponent to be at most \(4b\) gives exactly R212.7,
\(b\ge(1+\eta)/(10-4\nu+2\eta)\). For \((\nu,\eta)=(1/2,0)\), this becomes \(b\ge1/8\); at \(83/650\), \(1-4b=159/325\) and \(4b=166/325\), leaving the stated margin \(7/325\).

The calculation does not establish this local arithmetic hypothesis, recover it from a global prefix bound, or upgrade any fixed-shift source. It is a conditional transfer, checked here nonblind and separately from the actual small-phase lower bound.

## 4. First doubtful or unproved step

No remaining defect was found in the final ledger's actual sector estimates or its scoped lower theorem. The first missing arithmetic statement remains the complete upper estimate on the oscillatory nonrepeated complement. For the local route, the uniform genuine smooth density and every-cell prefix discrepancy are unproved inputs.

The only requested repair concerned the consequence attributed to the lower bound. It is now correctly a uniform fixed-power limitation on the actual small-phase sector, not a statement about an identified density main term, moving-edge little-oh, or the original signed wave. No lower bound on a mere certificate was substituted for the actual lower bound in (V11).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Actual coefficient first moment | GREEN: a nonzero interior mask interval and elementary disk cover prove positive mass; no sharp circle estimate is used. |
| First Fejer/Cauchy normalization | GREEN: exact moving-sum expansion yields \(Q^{-1}\) weighted correlation and \(Q^{-2}\) square-sum normalization. |
| Jensen and second smoothing step | GREEN: \(w_Q/Q\) has total mass one, and the two Cauchy factors yield \((M+Q)^{-3}\). |
| Axis removal | GREEN: axes cost \(O(N^{1+\epsilon}/Q)\), and fixed \(\alpha_0>2/3\) supplies the required uniform power growth of \(Q\). |
| Positive quadrants | GREEN: sign reversals of either shift are exact reindexings; repeated positive shifts remain included. |
| Integer rounding and shift-box containment | GREEN: for sufficiently large \(T\), \(Q\ge2\), \(Q^2\asymp U\), and \(Q\le L\le K\), uniformly on the stated fixed-interior range. |
| Actual small phase | GREEN: the exact second derivative of \(\sqrt t\) supplies a uniformly small phase on the complete support and full \(R\)-window. |
| Signed-mask crossings | GREEN: continuity plus the scaled first derivative makes all four factors \(O(Q/N)\), regardless of the number of mask zeros. |
| Complete-correlation lower bound | GREEN: phase restoration is performed on the whole \(n\)-sum; averaging moduli preserves the lower mass. |
| Near-edge scope | GREEN after repair: only a uniform fixed power saving over the entire open band is excluded. |
| Actual upper sectors | GREEN: every repeated shift and small product is paid with exact integer cutoffs; overlap double counting is harmless for an upper bound. |
| Conditional local boundary terms | GREEN: real prefixes, one-time atom assignment, all reset boundaries, and controlled cell count are present. |
| Conditional density and powers | GREEN: smooth density is paid separately; \(159/325\), \(166/325\), and \(7/325\) check. |
| Arithmetic and full-target promotion | GREEN in scope: no complete \(A_4\) estimate, new unconditional exponent, original moment, M1/M2 parent, or full-quarter theorem is established. |

These controls are analytical identities and inequalities. No computation is used to certify an asymptotic assertion.

## 6. Dependencies, hashes, and provenance

Only these allowed files were opened for this separate review:

1. `protocol.md` — SHA-256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `rounds/codex-managed/gc-complete-four-point-correlation/controls/conductor_actual_sector_ledger.md` — final SHA-256 `4f4ea9fb9bde6b0521f504d40e5d1c5574e1389254c96d03ddc713b0f69f8f97`.
3. `rounds/codex-managed/gc-full-source-method-review/controls/conductor_two_stage_strategy.md` — SHA-256 `9bf8f30d240304f88c46a5a93c7d93586b3ade1c674d5a5fdbc61a251fcd176f`.
4. `rounds/codex-managed/gc-full-source-method-review/reviews/independent_two_stage_review.md` — SHA-256 `052c3362897ae5185eee0a7afed6242164b3fa0ae6c89edcef90466c5d2adca5`.

The closed211 material supplies the precise coefficient, mask, support, phase, and normalization conventions and the already reviewed full smooth-main calculation. Files cited inside these allowed documents were not opened. The current graph, manifest, strategy, sources, sibling reports, original isolated report, and successor files were not accessed for this review.

The conductor received the scope repair request promptly. After repair, the entire final ledger was reread and its SHA-256 was independently checked. Only this assigned review file was written; the earlier isolated report and all authoritative state were left unchanged.

## 7. Recommended state effect and final ledger binding

**Retain the ledger as independently checked actual-sector control, actual fixed-interior lower-bound evidence, and a conditional local-discrepancy transfer.** Do not promote the complete four-point target, the hypothetical local arithmetic input, a pointwise exponent, the original moment, an M1/M2 parent, or the quarter theorem.

This GREEN verdict binds exclusively to:

`rounds/codex-managed/gc-complete-four-point-correlation/controls/conductor_actual_sector_ledger.md`

**SHA-256: `4f4ea9fb9bde6b0521f504d40e5d1c5574e1389254c96d03ddc713b0f69f8f97`.**

The lower-bound scope repair is present at that hash. A material later change requires a new review binding. This separate NONBLIND task is complete and stops here.
