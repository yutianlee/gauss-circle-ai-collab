# Round 232: blind integer-center packet band

## 1. Result: proved finite bounds and two distinct no-go controls

Campaign: `gc-upper-tail-separated-products`. Task: `blind_packet_band`. Role: statement-only independent rederiver. Status: candidate evidence, not accepted graph mathematics. Generated: `2026-10-11T23:52:02.9082254Z` (UTC, report preparation). Graph SHA-256 supplied by the brief, not independently read or verified: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

The isolated hypotheses imply the sharp, up to constants depending only on k, bounds

\[
D_E\ll_k A^2Wm,\qquad
H_{L,E}\ll_k A^2Wm\min\{W,1+\lfloor L\rfloor\},\qquad
U_E\ll_k A^2W^2m.
\]

Here D is the exact diagonal, H is the absolute close band, and U is the absolute all-pair sum. These bounds hold on every measurable E, including E chosen from the same functions. Explicit constants and a matching example appear below. All family cross terms can be retained with an explicit ordered double sum; M identical families can require an M-squared cost.

The close-band indicator is not generally positive semidefinite. A signed close-band quadratic form can equal zero while both its complementary form and the full energy are strictly positive. Even the nonnegative diagonal or absolute close band does not linearly control the complementary or full energy with a universal factor: the failure persists for fixed A, W, and m.

There is a necessary qualification to this no-go statement. The envelope itself gives a sharp nonlinear diagonal-to-full bound, proved below, with exponent

\[
\theta=\frac{2k-2}{2k-1}<1.
\]

Thus the correct obstruction is to a cost-free or linear transfer, not to every possible upper bound based on the diagonal and the envelope. No conclusion about any particular arithmetic family or requested arithmetic exponent is drawn.

## 2. Exact statements and hypotheses

Let P be a finite set of distinct integers. Let (Omega, nu) be a finite measure space, x measurable and real valued, W >= 1, A > 0, and k > 2. Suppose the real measurable functions f_p satisfy

\[
|f_p(t)|\le A g_p(t),\qquad
g_p(t)=\left(1+\frac{|x(t)-p|}{W}\right)^{-k}.
\]

Let E be measurable with nu(E)=m, and let L >= 0. All pairs below are ordered, and the close band includes the diagonal. Define

\[
\begin{aligned}
D_E&=\int_E\sum_{p\in P}f_p^2\,d\nu,\\
H_{L,E}&=\int_E\sum_{\substack{p,q\in P\\|p-q|\le L}}|f_pf_q|\,d\nu,\\
U_E&=\int_E\sum_{p,q\in P}|f_pf_q|\,d\nu,\\
B_{L,E}&=\int_E\sum_{\substack{p,q\in P\\|p-q|\le L}}f_pf_q\,d\nu,\\
C_{L,E}&=\int_E\sum_{\substack{p,q\in P\\|p-q|>L}}f_pf_q\,d\nu,\\
F_E&=\int_E\left(\sum_{p\in P}f_p\right)^2\,d\nu.
\end{aligned}
\]

Put r=floor(L), n_L=2r+1, and, for s>1, put

\[
c_s(W)=1+\frac{2W}{s-1}.
\]

The following explicit bounds hold:

\[
\boxed{D_E\le A^2m c_{2k}(W),}
\]

\[
\boxed{H_{L,E}\le \min\{n_LD_E,\ A^2m c_k(W)^2\}
\le A^2m\min\{n_Lc_{2k}(W),\ c_k(W)^2\},}
\]

\[
\boxed{F_E\le U_E\le A^2m c_k(W)^2.}
\]

For 0 <= L < 1, H_{L,E}=B_{L,E}=D_E exactly. For every L,

\[
F_E=B_{L,E}+C_{L,E},\qquad |B_{L,E}|\le H_{L,E},
\]

and therefore

\[
C_{L,E}-H_{L,E}\le F_E\le C_{L,E}+H_{L,E},\qquad
C_{L,E}\ge-H_{L,E}.
\]

In addition, for a constant K_k depending only on k and for m>0,

\[
\boxed{F_E\le U_E\le
K_k A^2W^2m
\left(\frac{D_E}{A^2Wm}\right)^{\theta},
\qquad \theta=\frac{2k-2}{2k-1}.}
\]

When m=0 all quantities vanish. The nonlinear bound can be combined with the preceding all-pair bound by taking their minimum. Since D_E <= H_{L,E}, replacing D_E on its right side by H_{L,E} is also valid, though weaker. These controls are consequences of the upper envelope, not signed cancellation.

For a family variant, let j=1,...,M, with finite integer index sets P_j, amplitudes A_j>0, widths W_j>0, the same exponent k, and envelopes

\[
|f_{j,p}(t)|\le A_j\left(1+\frac{|x_j(t)-p|}{W_j}\right)^{-k}.
\]

Allowing separate measurable x_j only makes this variant more general; identical x_j are permitted. Extend missing functions by zero. Write c_j=c_k(W_j), d_j=c_{2k}(W_j), and

\[
\mu_{ij}=\min\{c_i,c_j,\sqrt{d_i d_j}\}.
\]

The absolute cross term between families i,j obeys

\[
\boxed{\int_E\sum_{|p-q|\le L}|f_{i,p}f_{j,q}|\,d\nu
\le m A_iA_j\min\{c_i c_j,n_L\mu_{ij}\}.}
\]

For the exact diagonal cross term its bound is m A_iA_j mu_ij; for all pairs it is m A_iA_j c_i c_j. Consequently all cross terms of the aggregate f_p=sum_j f_{j,p} are retained by summing these bounds over all ordered i,j. In particular,

\[
H^{\rm aggregate}_{L,E}\le
m\sum_{i,j=1}^M A_iA_j\min\{c_i c_j,n_L\mu_{ij}\},
\]

\[
D^{\rm aggregate}_E\le m\sum_{i,j}A_iA_j\mu_{ij},\qquad
U^{\rm aggregate}_E\le m\left(\sum_jA_jc_j\right)^2.
\]

For widths at least one, the pairwise close-band scale is

\[
\ll_k m A_iA_j\min(W_i,W_j)
\min\{\max(W_i,W_j),1+\lfloor L\rfloor\}.
\]

For smaller widths the same statement holds with each W_j replaced, up to constants, by 1+W_j. When there are M=O(J) comparable families with A_j<=A and W_j<=W, the safe uniform cost relative to one family is O(J^2). A linear cost in J requires an additional orthogonality or disjointness input.

## 3. Proof and derivation

First prove the lattice estimate underlying every bound. For s>1, W>0, and y real, layer cake gives

\[
\sum_{p\in\mathbb Z}\left(1+\frac{|y-p|}{W}\right)^{-s}
=\int_0^1\#\left\{p\in\mathbb Z:
|y-p|<W(u^{-1/s}-1)\right\}\,du.
\]

An interval of radius R contains at most 2R+1 integers. Indeed, n integers in an interval have distance at least n-1 between the extreme integers, so n-1<=2R. Thus the last expression is at most

\[
\int_0^1[1+2W(u^{-1/s}-1)]\,du
=1+\frac{2W}{s-1}=c_s(W).
\]

All functions in this calculation are nonnegative, so passage to the sum/integral is legitimate, or can be obtained by monotone limits of finite sums. The estimate is uniform in y. Restricting to any finite P preserves it.

Pointwise in t, this gives sum_p f_p^2 <= A^2 c_{2k}(W), and sum_p |f_p| <= A c_k(W). Integration proves the diagonal and absolute all-pair bounds, since the latter integrand is (sum_p |f_p|)^2. It also proves F_E<=U_E.

For the band, 2|f_pf_q|<=f_p^2+f_q^2, and every integer p has at most n_L integers q with |p-q|<=L. Hence, pointwise,

\[
\sum_{|p-q|\le L}|f_pf_q|
\le\frac12\sum_{|p-q|\le L}(f_p^2+f_q^2)
\le n_L\sum_pf_p^2.
\]

The band is also a subset of all pairs. Taking these two bounds proves the displayed minimum. For W>=1, c_s(W) is bounded above and below by positive constants depending only on s times W. Also n_L is comparable to 1+floor(L). This proves the asserted dependence A^2 m W min(W,1+floor(L)). None of these estimates differentiates or averages over the selection rule for E: they hold before integration.

Here is a matching scale example. Give a singleton Omega measure m, take E=Omega and x=0, set n=floor(W), take P={0,...,n}, and set every f_p=A 2^{-k}. The envelope hypothesis holds because 0<=p/W<=1. Put s=min(floor(L),n). The number of ordered band pairs is

\[
(n+1)(2s+1)-s(s+1)\ge(n+1)(s+1)
\ge W\min\{W,1+\lfloor L\rfloor\}.
\]

The first inequality follows because its difference is s(n-s)>=0. The second follows from n+1>=W and s+1=min(floor(L)+1,n+1). Thus the close-band lower bound matches the upper scale with the factor 2^{-2k}; this same example gives D_E>=2^{-2k}A^2mW and U_E>=2^{-2k}A^2mW^2. The powers of A and m are also exact by amplitude and measure scaling.

For the family estimate, fix an integer offset h and set q=p+h. For normalized envelopes g_{i,p},g_{j,q}, each is at most one, and the lattice estimate yields

\[
\sum_p g_{i,p}g_{j,p+h}\le\min\{c_i,c_j\}.
\]

Ordinary Cauchy-Schwarz on this one fixed offset gives the additional bound sqrt(d_i d_j). Thus the offset sum is at most mu_ij. There are n_L permitted offsets, proving n_L mu_ij. Dropping the offset restriction gives c_i c_j. Multiply by A_iA_j and integrate to obtain the family cross bound. The exact diagonal corresponds to h=0. Expanding absolute values by the triangle inequality and summing over all ordered family pairs proves the aggregate statements. These are direct envelope arguments; no positivity of the band matrix is invoked.

For the width scale, c_k(W_j) is comparable to 1+W_j, and mu_ij is comparable to min(1+W_i,1+W_j): both c_i,c_j are at least a fixed positive multiple of the smaller width scale, while sqrt(d_i d_j) is too, and their minimum has the matching upper bound. Taking the minimum with c_i c_j proves the stated expression. With equal W_j=W, mu_ij=c_{2k}(W). If all M families are identical, their sum is exactly M times the single-family function, so every aggregate quadratic expression is M^2 times its counterpart. Hence that factor cannot generally be discarded. Separately, the true full energies do satisfy the elementary bound integral |sum_j S_j|^2 <= M sum_j integral |S_j|^2, where S_j=sum_p f_{j,p}; the right side already costs M^2 when all component energies are equal. The analogous argument cannot be justified by treating the band form as an inner product.

For completeness, prove the nonlinear diagonal control rather than overstate the no-go result. Fix t, put d=sum_p f_p(t)^2, and suppose first 0<d<=A^2W. For any R>=W>=1, the inner region contains at most 2R+1<=3R integers, so

\[
\sum_{|x-p|\le R}|f_p|\le\sqrt{3Rd}.
\]

In the annulus 2^a R<|x-p|<=2^{a+1}R, with a a nonnegative integer, there are at most 2^{a+2}R+1<=5\cdot2^aR integers. The envelope there is at most A W^k(2^aR)^{-k}. Summing the convergent geometric series proves

\[
\sum_{|x-p|>R}|f_p|
\le\frac{5}{1-2^{1-k}}AW^kR^{1-k}.
\]

Choose

\[
R=\left(\frac{A^2W^{2k}}d\right)^{1/(2k-1)}\ge W.
\]

The two terms then have the same scaling. Squaring gives

\[
\left(\sum_p|f_p|\right)^2
\le K_k A^{2/(2k-1)}W^{2k/(2k-1)}d^{\theta}.
\]

For d>A^2W, the earlier all-pair bound proves the same inequality after enlarging K_k, because (d/(A^2W))^theta>1. For d=0 it is immediate. Finally, Holder's inequality on E gives integral_E d^theta <= m^{1-theta} D_E^theta. This is exactly the claimed nonlinear bound for U_E, hence also for F_E.

The exponent theta is optimal for a uniform estimate of this form. Set A=W=m=1, x=0 on a singleton, P={N+1,...,2N}, and every f_p=(1+2N)^{-k}. Write a_N=(1+2N)^{-k}. These functions satisfy the envelope, and

\[
D_E=Na_N^2\asymp_k N^{1-2k},\qquad
F_E=U_E=N^2a_N^2\asymp_k N^{2-2k}=D_E^{\theta}\text{ up to constants}.
\]

Any exponent larger than theta would therefore fail with a constant independent of N. In particular theta cannot be replaced by one even with A, W, and m fixed.

## 4. First doubtful or unproved step

There is no unproved analytic or combinatorial step in the isolated bounds above. The envelopes, integrability, lattice counts, family cross terms, and interpolation are handled explicitly. Constants stated only with the subscript k depend only on the fixed exponent k; no arithmetic input is hidden in them.

The first missing step in any stronger application is an upper bound for the actual complementary signed correlation C_{L,E}, at the application's specified normalization and on its actual selected set E, strong enough that C_{L,E}+H_{L,E} pays the full target. The diagonal or close-band payment alone supplies no such same-scale estimate. It supplies only the separate envelope bound and the weaker nonlinear interpolation proved here.

An additional arithmetic coefficient/phase correlation estimate, or another rigorously justified orthogonality/operator estimate valid for the actual functions on the same E, is needed if those envelope-only bounds do not meet the target. It cannot be replaced by an unproved PSD assertion, by dropping family cross terms, or by assuming E is independent of the packets. This report has not read the actual arithmetic interface and does not assert which additional property that family has or lacks.

## 5. Control tests and outcomes

**Exact non-PSD control: FAIL for universal positivity.** For any L>=1 choose d=floor(L). Then d<=L<2d, and for centers 0,d,2d the band matrix is

\[
M=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}.
\]

For v=(1,-2,1), Mv=(-1,0,-1) and v^T Mv=-2. This is an exact integer calculation, not a numerical eigenvalue test. On a singleton of measure m, set x=d and c=(A/2)(1+d/W)^{-k}; taking f=c v respects the envelope, including the central value 2c<=A. Therefore B_{L,E}=-2mc^2 is an admissible negative band value. For 0<=L<1 the band is the identity and is PSD; if all pairs in a particular P lie in the band it is the all-ones matrix and is PSD. These special cases do not rescue universal positivity when L>=1.

**Zero signed band with positive full/complementary energy: FAIL for control by signed B.** With the same three centers, x, and c, take v=(1,-1,2). It still satisfies the envelope. Here Mv=(0,2,1), so v^T Mv=0, while (sum v)^2=4. The only omitted ordered pairs are (0,2d) and (2d,0), and their sum is 4. Thus B_{L,E}=0 and C_{L,E}=F_E=4mc^2>0. Signed close-band size alone cannot be treated as a positive energy.

**Fixed-width diagonal/absolute-band linear transfer: FAIL.** Use the remote block in Section 3 with fixed A=W=m=1. For any fixed r=floor(L) and N>r,

\[
H_{L,E}=[N(2r+1)-r(r+1)]a_N^2,
\]

\[
F_E=N^2a_N^2,\qquad C_{L,E}=F_E-H_{L,E}.
\]

Consequently F_E/D_E=N and F_E/H_{L,E} grows like N/(2r+1), while C_{L,E}/H_{L,E} also tends to infinity. No constant depending only on k, A, W, m, and a fixed L can give a linear upper bound of these types. All quantities tend to zero, consistent with the valid nonlinear estimate; this control does not claim a violation of that estimate.

**Small close band with nonvanishing full energy when the width grows: FAIL for unnormalized vanishing transfer.** On a singleton with m=A=1, let W=N, x=0, P={1,...,N}, and f_p=1/N. For N>=2^k the envelope holds since its minimum on P is at least 2^{-k}. For fixed L, D_E=1/N and H_{L,E}<=(2r+1)/N tend to zero, whereas F_E=1 and C_{L,E}=1-H_{L,E} tend to one. This keeps every stated hypothesis and exposes the indispensable width cost.

**Sharp size and family controls: PASS.** The block {0,...,floor(W)} in Section 3 gives matching diagonal, band, and all-pair orders. Identical aligned families give exact M^2 growth. Thus no universal improvement of those powers is available from the stated upper envelopes alone.

**Selected-set control: PASS.** Every positive bound is proved pointwise and then integrated. No independence or regularity of E is used. All countercontrols take E=Omega, an allowed measurable selection, and can be realized on an atom of any prescribed finite measure.

**Blind isolation: PASS.** Only the three authorized files listed in Section 6 were read. The graph, active manifest, actual interface, historical files, sibling reports, and external sources were not opened. The brief's broad reference to an arithmetic target was not used as an additional hypothesis. No numerical experiment was run; the finite matrix controls and counting formulas were checked algebraically. Analytical/algebraic allocation was 100%; computational experimentation was 0%.

## 6. Dependencies and exact artifacts used

The only mathematical hypotheses used are those in the isolated packet statement. The proofs use elementary integer spacing, nonnegative layer cake, Cauchy-Schwarz, Holder's inequality, and a geometric series, all with their applications derived above. No external theorem, citation, arithmetic hypothesis, or previous-round lemma is imported.

Authorized files read and their SHA-256 values:

- `protocol.md`: `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `rounds/codex-managed/gc-upper-tail-separated-products/briefs/blind_packet_band.md`: `2e460d93278ba95e2e9a9b1b07903e3e4ec6a4ad72fdf7b860733e615c9ee0c7`.
- `rounds/codex-managed/gc-upper-tail-separated-products/briefs/isolated_packet_band.md`: `6c1d32bb503d2136c059c4a52dcb6bc60da5b536016cb6b0a75b716b440f3456`.

The only output written is `rounds/codex-managed/gc-upper-tail-separated-products/reports/blind_packet_band.md`. Its SHA-256 is computed after this final write and returned to the conductor; it is not embedded recursively in the file. No shared-state file is edited. No separate computation artifact is needed because the exact controls and their derivations are fully reproduced in this report.

## 7. Recommended state effect

**Retain as independently derived candidate evidence** the explicit diagonal, absolute close-band, all-pair, and unequal-width cross-family lemmas, together with the sharp nonlinear diagonal interpolation. They may support narrow promotion only after the conductor completes the required seam reviews and graph validation.

**Reject** universal PSD of the nontrivial band mask, control of full energy by the signed band alone, a universal linear transfer from diagonal/absolute close-band mass to the complementary or full energy, and omission of inter-family cross terms without an extra proved hypothesis.

**No change** to any arithmetic target or completion claim follows from this isolated report. Determining whether the bounds meet an application's exponents and estimating its actual complementary signed sum remain outside this blind assignment. The report is frozen after hashing; no successor round is proposed or started.
