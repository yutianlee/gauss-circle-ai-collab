# Round 165 terminal mathematical review of the parity-gcd-scale kernel

## 1. Result

**Final verdict: GREEN.**  The current repaired kernel is mathematically
sound.  Every boxed statement has the correct status and implication:

- (165.K8), the full-to-even parity connector, is proved for every
  positive integer \(R\), including odd \(R\) and \(R=1\);
- (165.K11), the tangent and character identity, is exact and
  multiplicity one;
- (165.K12), the complete monotone-displacement bound, is genuinely
  \(O(L^2)\) across all short shifts, not per shift;
- (165.K13) is an **open sufficient theorem**, not a proved estimate;
- (165.K17), the actual high character-divisor-gcd sector, is proved with
  the exact \(L^3/G_0\) ledger;
- (165.K17a) is the sharpest displayed **open minimal-scale theorem**;
- (165.K21), including the squarefree even-even parity branch, is exact;
  and
- (165.K26) is a distinct **open maximal-scale sufficient theorem** whose
  implication to the residual scalar is correct.

The three earlier statement defects have been repaired in the current
file: (165.K7a) now excludes the undefined \(\mathcal E_0\) case and
handles \(R=1\) separately; (165.K5) evaluates square roots only on the
positive supported-pair domain; and the status range no longer includes
the open equation (165.K17a) among proved equations.

No open analytic estimate is now stated as proved.  The proved state effect
is a reduction plus two strict target-safe sectors: monotone displacement
and fixed-proportion high character-divisor gcd.  The complete residual
remains open.

## 2. Exact statement and hypotheses

The reviewed coefficient is

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {m odd}}}
   \chi_4(d)\lambda_N(d),
\tag{165.TR1}
\]

where \(\lambda_N(d)\) retains the supported squarefree row, the exact
normalization, selected neither/both or no-pair residual status, the odd
character-bearing divisor, the possibly even complementary factor, every
profile and hard point value, endpoints, and zero extension.  On a nonzero
atom,

\[
 N\asymp L^2,qquad d,m=N/d\asymp L,qquad
 |\lambda_N(d)|\ll1.
\tag{165.TR2}
\]

The uniform atom bound follows from the literal formula: the squarefree
and residual masks are at most one, the outer normalization is \(\asymp1\)
on the shell, and all accepted profile and point values are bounded.

Let \(\mathcal J_L\) be a consecutive interval of cardinality
\(M_L\asymp L^2\) containing the positive literal shell, extend
\(z_N=c_N^{\rm rem}e(J\sqrt N)\) by zero, and set

\[
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{165.TR3}
\]

For every \(R\ge1\), the phase form in the kernel is understood only for
\(N,N+r\) in the positive literal shell.  Zero extension is used in the
window identities without evaluating a square root elsewhere.  At the
minimal scale put \(R_0=\lceil L\rceil\).  At the maximal scale put
\(R=M_L\).

For the high-gcd statement, \(g=(d,d')\) always denotes the gcd of the two
odd character-bearing divisors, and \(G_0\) is its threshold.  The fixed
fraction consequence uses \(g\ge\gamma L\), with \(\gamma>0\) fixed.  If
the threshold is beyond the possible range \(g<R_0\), the sector is empty;
otherwise (165.K17) applies directly.

The proved/open ledger is therefore:

\[
\begin{array}{c|c}
\text{proved internally}&
 (165.K4)\text{--}(165.K12),\ (165.K14)\text{--}(165.K17),\
 (165.K18)\text{--}(165.K25)\\
\hline
\text{open estimates}&(165.K13),\ (165.K17a),\ (165.K26).
\end{array}
\tag{165.TR4}
\]

Only the logical implications from the three open estimates are proved.

## 3. Proof and line-by-line seam verification

### 3.1 All-scale Fejer identity and odd-
\(R\) endpoints

For

\[
 Y_s^{(R)}=\sum_{j=0}^{R-1}z_{s+j},
\]

expansion of the full-line square counts a pair at positive gap \(r<R\)
in exactly \(R-r\) windows.  This proves (165.K4)--(165.K5) for every
integer \(R\ge1\).  Each supported coefficient occurs in exactly \(R\)
windows, and the range of starts whose window can meet \(\mathcal J_L\)
has exactly \(M_L+R-1\) sites.  Cauchy on that containing start range
proves

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le {M_L+R-1\over R}\mathfrak E_R.
\tag{165.TR5}
\]

If the literal shell has gaps, some of those windows are zero; this can
only improve the bound.

Split a window into its absolute even and odd sites.  Pointwise,

\[
 |Y_s^{(0)}+Y_s^{(1)}|^2
 \le2(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2),
\]

which proves the boxed (165.K8).  On the right a pair survives exactly
when its gap is even, still with multiplicity \(R-r\).  Hence (165.K9)
is exactly

\[
 \Re\mathfrak C_R
 \le {D_L\over2}+2\Re\mathfrak C_R^{(2)}.
\tag{165.TR6}
\]

For odd \(R=2S+1\ge3\), reindexing even- and odd-start windows gives the
printed convex combination (165.K7a).  A subsequence gap \(q<S\) has
coefficient

\[
 {S+1-q\over2S+1}+{S-q\over2S+1}
 =1-{2q\over2S+1},
\]

and the terminal gap \(q=S\) occurs only in the length-\(S+1\) energy,
with coefficient \(1/(2S+1)\).  At \(R=1\), the separate formula
\(\mathfrak E_1=\mathfrak E_1^{(2)}=D_L\) is exact.  Thus there is no odd-
\(R\) floor, ceiling, or terminal-weight error.

### 3.2 Tangent identity and the complete monotone count

Every divisor tuple determines uniquely

\[
 a=d'-d,qquad b=m'-m,
\]

and the inverse is \((d',m')=(d+a,m+b)\).  Since \(d,d'\) are odd,
\(a\) is even, and

\[
 d'm'-dm=db+am+ab=db+a m'.
\tag{165.TR7}
\]

Also

\[
 \chi_4(d')\chi_4(d)=(-1)^{a/2},
\tag{165.TR8}
\]

because \(\chi_4(d+2q)=(-1)^q\chi_4(d)\).  This verifies the boxed
(165.K11), including negative even \(a\).

On literal support all four factors exceed \(\kappa L\) for a fixed
\(\kappa>0\).  In the monotone sector \(a,b\ge0\),

\[
 r=db+a m'\ge\kappa L(a+b).
\tag{165.TR9}
\]

Because \(r<R_0\asymp L\), only \(O(1)\) displacement pairs occur.  For
each pair there are \(O(L^2)\) choices of \((d,m)\); then \(d',m'\) and
\(r\) are determined.  There is no further \(R_0\)-factor.  With
(165.TR2) and Fejer weight at most one, this proves the boxed

\[
 |\mathfrak C_{R_0,\rm mon}^{\rm rem}|\ll L^2.
\tag{165.TR10}
\]

If \(a,b\le0\), or one displacement is zero and the other negative,
(165.TR7) is nonpositive and is strictly negative unless \(a=b=0\); the
latter gives \(r=0\).  Thus every remaining nonempty tuple has \(ab<0\).

Combining (165.TR6), (165.TR10), the diagonal bound, and the accepted
Fejer-to-scalar inequality proves the *implication* from (165.K13).  It
does not prove the estimate printed in (165.K13), which the kernel labels
open.

### 3.3 Character-divisor gcd, the high-gcd count, and (165.K17a)

Put

\[
 g=(d,d'),\qquad d=gu,qquad d'=gv,qquad (u,v)=1.
\]

The divisors are odd, so \(g,u,v\) are odd.  Dividing
\(d'm'-dm=r\) gives

\[
 g(vm'-um)=r,qquad r=gh.
\tag{165.TR11}
\]

After one base solution is fixed, all solutions are
\(m=m_0+vt\), \(m'=m'_0+ut\).  This is a bijection, not merely a count.
The product step is

\[
 K_d=guv={dd'\over g}\asymp {L^2\over g},
\]

so the geometric row has \(O(1+g)\) points.  The character is the fixed
row sign \(\chi_4(uv)\).

For fixed \(g\), there are \(O(L/g)\) possibilities for each of
\(u,v,h\), and \(O(g)\) row points.  Consequently the absolute literal
atom count at that gcd is

\[
 O\!\left((L/g)^3g\right)=O(L^3/g^2).
\]

Summing \(g\ge G_0\), and using the bounded atom weights, gives

\[
 |\mathfrak C_{R_0,g\ge G_0}^{\rm rem}|
 \ll_\varepsilon L^3X^\varepsilon
       \sum_{g\ge G_0}g^{-2}
 \ll_\varepsilon {L^3\over G_0}X^\varepsilon.
\tag{165.TR12}
\]

This proves the boxed (165.K17).  Equal divisors \(d=d'\), both selector
statuses, even complementary factors, hard values, and shell endpoints
are included; their restrictions only delete atoms.  The ownership is the
opened divisor-incidence sector, not a unique gcd attached to an entire
product row.

At \(G_0=\gamma L\), (165.TR12) is target-sized.  Split the even opposing
aggregate into \(g<\gamma L\) and \(g\ge\gamma L\), use (165.K12) for
the monotone part, and apply (165.K8).  This proves that the boxed
(165.K17a), if established, implies the residual scalar target.  The
low-gcd estimate itself remains open.

### 3.4 Cofactor gcd and squarefree even-even parity

Put \(s=(m,m')\), \(m=su\), \(m'=sv\), \((u,v)=1\).  Then

\[
 s\mid r,qquad r=sh,qquad vd'-ud=h.
\]

All solutions have step \((v,u)\).  Simultaneous oddness of \(d,d'\)
selects one parameter parity, giving

\[
 d=D_0+2vk,qquad d'=D'_0+2uk,qquad
 K_s=2suv={2mm'\over s}.
\tag{165.TR13}
\]

The row has \(O(1+s)\) points.  Increasing \(k\) changes the two
characters by the product factor \((-1)^{u+v}\).  If \(r\) is odd, the
products and therefore \(m,m'\) have opposite parity; \(s\) is odd and
\(u,v\) have opposite parity, so the sign flips.  If \(r\) is even and
both products are odd, \(u,v\) are both odd, so the product sign is fixed.

If both products are even and squarefree, then \(m,m'\) each contain
exactly one factor two.  Hence

\[
 \nu_2(s)=1,qquad u,v\text{ odd},qquad 4\mid r,qquad h=r/s\text{ even}.
\tag{165.TR14}
\]

The character is again fixed.  Thus the boxed (165.K21) is exact in every
parity branch.

### 3.5 Phase-step convention and route scope

Let \(K\) be the actual increment of the product under one increment of
the printed integer row parameter.  For
\(x(t)=x_0+Kt\), differentiation gives exactly

\[
\begin{aligned}
 \Psi'(t)&={JK\over2}\{(x+r)^{-1/2}-x^{-1/2}\},\\
 \Psi''(t)&={JK^2\over4}\{x^{-3/2}-(x+r)^{-3/2}\},\\
 \Psi'''(t)&={3JK^3\over8}\{(x+r)^{-5/2}-x^{-5/2}\}.
\end{aligned}
\tag{165.TR15}
\]

There is no factor-two mismatch: in the cofactor form the parameter is
\(k\) and its actual step is \(K_s=2suv\).  With \(r=sh\), the printed
scales (165.K23) follow.

After absorbing (165.K21), the effective phase is
\(\Psi(k)+(r\bmod2)k/2\), and its exact discrete increment is the quantity
in (165.K24).  Large real derivatives give no uniform integer or
half-integer separation.  Moreover
\(\Psi''\asymp Jh/(sL)\) is bounded below at the inherited power scale, so
the usual positive second-derivative expression supplies no power saving
over the trivial row estimate.  On a smooth full divisor-gcd row, taking
absolute values of all stationary dual modes is likewise adverse.

The kernel states these conclusions with the correct scope.  They do not
exclude signed cancellation between dual modes, higher derivatives, joint
\((r,N)\) transforms, spectral identities, or actual arithmetic.  No open
phase theorem is smuggled into the proved ledger.

### 3.6 Maximal-scale even-long alternative (165.K26)

Let

\[
 A_r=\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\]

For every fixed \(r\), zero extension and Cauchy give \(|A_r|\le D_L\).
Therefore, at \(R=M_L\),

\[
 \sum_{1\le r<R_0}\left(1-{r\over M_L}\right)|A_r|
 \le(R_0-1)D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{165.TR16}
\]

Now decompose the even-gap correlation in
\(\mathfrak E_{M_L}^{(2)}\) into \(r<R_0\) and \(r\ge R_0\).  The first
part is bounded above by (165.TR16).  Assuming the boxed one-sided
medium/long estimate (165.K26), the second part is
\(O(L^3X^\varepsilon)\).  Together with the diagonal,

\[
 \mathfrak E_{M_L}^{(2)}\ll_\varepsilon L^3X^\varepsilon.
\tag{165.TR17}
\]

The parity connector then gives
\(\mathfrak E_{M_L}\le2\mathfrak E_{M_L}^{(2)}\), and (165.K6) has

\[
 {M_L+M_L-1\over M_L}<2.
\]

Hence the residual scalar square is
\(O(L^3X^\varepsilon)\).  Applying the energy hypotheses with
\(2\varepsilon\) before taking the square root gives

\[
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{165.TR18}
\]

This verifies every weight, the odd-\(M_L\) endpoint through (165.K7a),
the one-sided direction, and the epsilon relabelling in the implication
from (165.K26).  It does not prove (165.K26).

### 3.7 Proof-status wording

The current status paragraph correctly lists

\[
 (165.K4)\text{--}(165.K12),\quad
 (165.K14)\text{--}(165.K17),\quad
 (165.K18)\text{--}(165.K25)
\]

as proved.  It separately calls (165.K17a) and (165.K26) open and
(165.K13) a broader sufficient statement.  The former accidental inclusion
of (165.K17a) in a proved equation range is no longer present.

## 4. First doubtful or unproved step

There is no doubtful step in the exact identities, sector counts, parity
classification, derivative ledger, or logical implications reviewed
above.

The first open minimal-scale estimate is exactly (165.K17a): the complete
even-shift, opposing-displacement, low-character-divisor-gcd aggregate.
It must save the remaining factor \(L\) while retaining the squarefree
masks, both residual selectors, parity branches, hard profiles, endpoints,
and aggregate real part.  The broader sufficient estimate (165.K13) is
also open.

Independently, (165.K26) is the open maximal-scale alternative.  It asks
for a target-sized one-sided aggregate over the even medium/long shifts.
The fixed-shift Cauchy payment proves only the short part (165.K25); it
does not estimate this long aggregate.

The route-scoped derivative and positive-dual observations do not close
either frontier and are not universal no-go theorems.

## 5. Control tests and outcomes

| Terminal control | Outcome |
|---|---|
| Positive phase domain | **GREEN.** (165.K5) now restricts to positive supported pairs; zero extension is used only in the window identity. |
| All-\(R\) Fejer identity | **GREEN.** Pair multiplicity is exactly \(R-r\), and the containing start range has \(M_L+R-1\) sites. |
| Odd-\(R\) endpoint | **GREEN.** (165.K7a) is exact for \(R\ge3\); \(R=1\) is handled separately.  The terminal even gap has weight \(1/R\). |
| Boxed parity connector (165.K8) | **GREEN, proved.** It follows pointwise before summing and uses no shiftwise modulus. |
| Boxed tangent identity (165.K11) | **GREEN, proved.** The map and inverse are unique and the character is \((-1)^{a/2}\). |
| Boxed monotone sector (165.K12) | **GREEN, proved.** \(a+b=O(1)\); \(O(L^2)\) counts the complete union over shifts. |
| Boxed opposing theorem (165.K13) | **GREEN implication, OPEN estimate.** It is never listed as proved. |
| Divisor-gcd row and support | **GREEN.** Product step is \(L^2/g\), row length is \(O(1+g)\), and the character is fixed. |
| Boxed high-gcd sector (165.K17) | **GREEN, proved.** Per-gcd capacity is \(L^3/g^2\), summing to \(L^3/G_0\). |
| Boxed low-gcd frontier (165.K17a) | **GREEN implication, OPEN estimate.** The status paragraph explicitly excludes it from proved equations. |
| Boxed cofactor parity (165.K21) | **GREEN, proved.** The even-even branch has \(\nu_2(s)=1\), \(u,v\) odd, \(4\mid r\), and \(h\) even. |
| Phase-step convention | **GREEN.** \(K\) is the actual row step; the cofactor step includes its factor two. |
| First/second derivative scope | **GREEN.** The statements establish only failure of the printed positive placements, not a universal phase no-go. |
| Absolute dual modes | **GREEN scope.** Adversity is asserted only for a smooth full row after the modes are made positive. |
| Short payment (165.K25) | **GREEN, proved.** It costs at most \((R_0-1)D_L\ll L^3X^\varepsilon\). |
| Boxed maximal alternative (165.K26) | **GREEN implication, OPEN estimate.** Parity, diagonal, endpoint, and epsilon powers all close conditionally. |
| Open/proved status | **GREEN.** No open estimate is stated as proved in the repaired kernel. |
| Downstream scope | **GREEN.** No complete residual, parent, M9 component, bridge, quarter theorem, or exponent is promoted. |
| Numerical experimentation | **NOT USED.** The review is entirely algebraic and analytic. |

## 6. Dependencies and exact artifacts used

The terminal review used the current kernel and every completed Round-165
report and review:

- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/actual_residual_short_shift_attack.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/blind_fejer_short_shift_rederivation.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/short_shift_arithmetic_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/tangent_gcd_parity_seam_review.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/parity_connector_high_gcd_review.md`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/variable_scale_fejer_bypass_review.md`.

No external source, sibling unfinished artifact, numerical experiment, or
computation was used.

## 7. Recommended state effect

**Promote the current kernel as a proved-internal reduction.**  The all-
scale Fejer identity, exact parity connector, tangent decomposition, dual
gcd normal forms, parity ledger, phase-step formulas, and logical
minimal-/maximal-scale implications have passed terminal mathematical
review.

**Promote the two strict owner-complete sectors:**

1. the complete monotone-displacement sector (165.K12); and
2. for every fixed \(\gamma>0\), the opened divisor-incidence sector
   \(g=(d,d')\ge\gamma L\) from (165.K17).

These justify the terminal label `strict_residual_short_shift_sector`.

**Retain as open** the sharp minimal-scale theorem (165.K17a), the broader
minimal-scale theorem (165.K13), and the distinct maximal-scale theorem
(165.K26).  Record only route-scoped obstructions for shiftwise modulus,
large real derivatives without modulo-one separation, the classical
positive second-derivative placement, and absolute stationary dual modes.

**Make no downstream promotion.**  The complete residual, full \(t=1\)
face, other few-point channels, hard TOP, BAL, UNBAL, both smooth M2
packets, M9--M2, M9--M1, endpoint uniformity, M9, the conditional bridge,
the quarter theorem, and both global exponents remain open or unchanged.
