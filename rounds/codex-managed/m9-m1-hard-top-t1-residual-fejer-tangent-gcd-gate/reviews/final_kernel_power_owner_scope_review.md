# Round 185 final-kernel power and owner-scope review

## 1. Result / verdict

**Verdict: GREEN.**

The frozen source candidate and durable kernel hashes match the review
brief exactly.  Independent recomputation confirms the diagonal and
support scales, every incidence and row count, both gcd tails, the joint
gcd identity, the bounded-height double harmonic sum, logarithmic
rebudgeting, the explicit \(\gamma^{-1}\) and \(\delta^{-1}\) costs,
the \(L^3\) row capacity, and the missing dyadic-\(h\) factor.

The kernel proves only the strict opened-incidence sector (K185.7) and
its exact complement (K185.36).  Its direct dependencies are accepted
in the starting graph, its uses of the small-\(t\) ray and M2 material
are correctly classified, and it makes no unauthorized owner or
exponent inference.  Only the strict subordinate \(t=1\) residual
sector is eligible for promotion.

## 2. Exact statement and hypotheses

Fix real \(X\geq2\), one nonempty literal middle or lower hard-M1
residual shell \(L\geq2\), \(\sigma\in\{\pm1\}\), and fixed
\(B>0\).  Put

\[
 R_0=\lceil L\rceil,
 \qquad H_B=\lfloor(\log(2X))^B\rfloor.
\]

The zero-extended residual coefficient is supported on products
\(N=dm\asymp L^2\), with \(d,m\asymp L\), \(d\) odd,
\((d,m)=1\), and
\(|\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon\).  It retains
the allocation-independent Round-184 selector, squarefreeness,
coprimality, hard cone, every literal profile and endpoint field, and
both signs.

At positive even shifts \(0<r<R_0\), open

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd},
\]

and put \(a=d'-d\), \(b=m'-m\).  The proved sector is the complete
monotone set \(a,b\geq0\), together with both opposing orientations
\(ab<0\) for which

\[
 r=2\kappa gh,\qquad h\leq H_B.
\]

Its absolute contribution is
\(O_{B,\varepsilon}(L^2X^\varepsilon)\).  The exact complement is the
canonical, orientation-restricted, one-outer-real-part aggregate
(K185.36) with \(h>H_B\).  The complete residual would require the
still-open dyadic estimate (K185.37).

The only eligible campaign result is therefore the terminal label
strict_hard_m1_t1_residual_tangent_gcd_sector.  It is a subordinate
physical incidence theorem, not the complete \(t=1\) residual or any
owner theorem.

## 3. Proof or exponent-ledger audit

### Diagonal, containing interval, and Fejer scale

For each supported \(N\), the divisor bound gives

\[
 |c_{N,\sigma}^{\rm rem}|
 \leq\sum_{d\mid N}|\lambda_{N,\sigma}(d)|
 \ll_\varepsilon X^\varepsilon
\]

after epsilon rebudgeting.  Since \(d,m\asymp L\), every supported
product lies in one positive interval of \(O(L^2)\) integer sites.
There are therefore \(O(L^2)\) possible \(N\)'s and

\[
 D_{L,\sigma}=\sum_N|c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

A containing interval may be taken with \(M_L\asymp L^2\).  At
\(R_0=\lceil L\rceil\),

\[
 \frac{M_L+R_0-1}{R_0}=O(L).
\]

Thus a diagonal-plus-correlation energy of
\(O(L^2X^\varepsilon)\) yields the scalar square
\(O(L^3X^\varepsilon)\), exactly the \(L^{3/2}\) scalar target.  No
factor of \(R_0\), endpoint window, or support site is missing.

### Monotone, original-gcd, and cross-gcd counts

For \(a,b\geq0\),

\[
 r=db+am+ab\gg L(a+b).
\]

Since the integer \(r<R_0\) satisfies \(r<L\), only \(O(1)\)
displacement pairs occur.  The \((d,m)\)-box has \(O(L^2)\) sites, so
the complete monotone count is \(O(L^2)\).

For \(g=(d,d')\), write \(d=gu\), \(d'=gv\).  At fixed \(g\), the
choices of \((u,v)\), \(r/g\), and the solution position in

\[
 vm'-um=r/g
\]

are respectively

\[
 O((L/g)^2),\qquad O(L/g),\qquad O(g).
\]

Their product is \(O(L^3/g^2)\), and summing \(g^{-2}\) gives

\[
 \#\{g\geq G\}\ll L^3/G.
\]

In the plus orientation, \(\kappa=(d,m')\) gives

\[
 r=2\kappa(sv-wu),
\]

while in the minus orientation, \(\kappa=(d',m)\) gives

\[
 r=2\kappa(uw-sv).
\]

At fixed \(\kappa\), there are \(O((L/\kappa)^2)\) choices of
\((u,v)\), \(O(L/\kappa)\) choices of
\(n=r/(2\kappa)\), and \(O(\kappa)\) sites on the affine solution
line.  Hence the count is \(O(L^3/\kappa^2)\), per orientation up to a
constant, and

\[
 \#\{\kappa\geq K\}\ll L^3/K.
\]

### Joint gcd, primitive multiplicity, and bounded height

At a live plus endpoint, squarefreeness of
\((\kappa u+2s)\kappa v\) forces \((\kappa,s)=1\); the corresponding
lower endpoint does so in the minus orientation.  With \((u,v)=1\),
this gives

\[
 g=(d,d')=(u,s)=(u,n).
\]

Writing \(u=gU\), \(s=gS\), \(n=gh\) yields

\[
 r=2\kappa gh,
\]

with primitive equations

\[
 Sv-wU=h,\qquad Uw-vS=h.
\]

The domain \((gU,v)=1\), \((U,h)=1\), together with the canonical
least-residue anchors and the positive index sets, gives one and only
one label and one integer \(t\) for every physical opposing incidence.
Zero extension handles all remaining literal deletions and creates no
extra multiplicity.

For fixed \((\kappa,g,h)\), the numbers of \(U\), \(v\), and physical
\(t\)-sites are

\[
 O\!\left(\frac{L}{\kappa g}\right),\qquad
 O\!\left(\frac{L}{\kappa}\right),\qquad
 O(\kappa).
\]

Thus the fixed-triple count is

\[
 O\!\left(\frac{L^2}{\kappa g}\right).
\]

The shift condition gives \(\kappa g<L/(2h)\), and

\[
 \sum_{\kappa g<T}\frac1{\kappa g}
 \ll\log^2(2T).
\]

Consequently

\[
 \#\{ab<0:h\leq H\}
 \ll HL^2\log^2(2L).
\]

For \(H=H_B\), the fixed powers of \(\log(2X)\) and
\(\log(2L)\), and the two endpoint coefficient bounds, are absorbed
into \(X^\varepsilon\) in the inherited nonempty literal-shell range.
This gives exactly the claimed \(L^2X^\varepsilon\) contribution.

### Restored tail powers, row capacity, and the missing factor

Putting \(G=\gamma L\) and \(K=\delta L\) in the two verified tails
gives

\[
 O_\varepsilon(\gamma^{-1}L^2X^\varepsilon),
 \qquad
 O_\varepsilon(\delta^{-1}L^2X^\varepsilon).
\]

Moreover, \(2\kappa gh<L\) puts the first fixed-proportion tail inside
\(h<(2\gamma)^{-1}\) and the second inside
\(h<(2\delta)^{-1}\), exactly as stated in (K185.29).

At fixed \((\kappa,g)\), the choices of \(U,v,h\) give at most

\[
 O\!\left(\frac{L}{\kappa g}\right)
 O\!\left(\frac{L}{\kappa}\right)
 O\!\left(\frac{L}{\kappa g}\right)
 =O\!\left(\frac{L^3}{\kappa^3g^2}\right)
\]

canonical primitive rows.  Even an unproved \(O(1)\) estimate for each
row therefore positively recombines only to

\[
 O\!\left(L^3\sum_{\kappa,g\geq1}
 \frac1{\kappa^3g^2}\right)=O(L^3).
\]

For \(Y<h\leq2Y\), positive counting instead has
\(O(YL^2X^\varepsilon)\) capacity after logarithmic rebudgeting.  The
desired \(O(L^2X^\varepsilon)\) estimate thus needs a genuine global
factor \(Y\); bare alternation or positive row recombination does not
supply it.  Finally,

\[
 \sup_{|B(t)|\leq1}\left|\sum_{t\in I}(-1)^tB(t)\right|=|I|
\]

is exact by taking \(B(t)=(-1)^t\).

## 4. First doubtful or unproved step

No doubtful step remains in the kernel's proved counting, power, or
owner-scope claims.  The first unproved relation is precisely
(K185.37), the global signed estimate on every dyadic block
\(Y<h\leq2Y\), with both orientations and all literal endpoint fields
still coupled under one real part.  The kernel labels this relation
open and derives no owner conclusion from it.

## 5. Controls, dependencies, and owner outcomes

The source candidate hash is
74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65,
and the durable kernel hash is
4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.
Both equal the frozen values.  The starting graph hash is
f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0.

The exact arithmetic control also reproduces.  The canonical plus
anchor for \((\kappa,g,h,U,v)=(103,1,1,7,1)\) is \((S_0,w_0)=(1,0)\),
so its two sites have canonical indices \(t=14,15\).  Exact arithmetic
gives

\[
\begin{array}{c|c|c|c}
t&(d,d',m',m)&(N,N')&r\\ \hline
14&(721,919,103,131)&(94451,94657)&206\\
15&(721,933,103,133)&(95893,96099)&206.
\end{array}
\]

At \(t=14\), both products are squarefree and allocation-coprime, both
ratios lie strictly in \((4,16)\), and all prime factors
\(7,103,131,919\) are \(3\bmod4\); both residual masks are therefore
one.  At \(t=15\), the ratios and shift persist, but
\((721,133)=7\), so the lower product contains \(7^2\), while the upper
product remains squarefree and coprime.  The character product flips
from \(-1\) to \(+1\).  This licenses only failure of automatic
no-pair arithmetic-support invariance.  It proves no opaque-profile
nonvanishing, density, lower mass, asymptotic obstruction, or failure of
(K185.37).

All five direct kernel dependencies are graph-valid and
proved internally:

- M9-M1-hard-top-t1-comparable-factor-exchange-sector;
- M9-M1-top-endpoint-transform;
- M9-M1-frequency-phase-diagram-R10;
- M9-M2-dyadic-weight-nondegeneracy; and
- Divisor-bound-elementary.

The small-\(t\) primitive-ray theorem is accepted routing context and
also lies in the ancestry of the comparable-factor theorem, but the new
bounded-\(h\) count invokes no separate estimate from it.  The
M9-M2-dyadic-weight-nondegeneracy node is profile infrastructure, not a
proof of the M2 parent.  The M2 tangent, alias, and conductor kernels are
method controls only and are absent from the direct dependency list.

The graph permits only a new strict subordinate sector.  In particular:

- M9-M1-hard-top-high-radical-small-t-residual-estimate,
  M9-M1-top-endpoint-signed-cone, and the independent smooth residual
  parent remain open;
- M9-M1-physical-one-count-assembly remains an accepted conditional
  reduction with its blockers unchanged, while M9-M1 remains open;
- M9-M2, M9-endpoint-uniformity, and M9 remain open;
- Conditional-bridge and GC-global-M1-alternative-bridge remain derived
  only under assumptions, and GC-target remains open; and
- the proved internal exponent \(1/3\), the external
  \(0.3144831759740614\ldots\) benchmark, and the unproved target
  \(1/4\) are unchanged.

The capacity mechanism is subordinate evidence, not a second terminal
label.

## 6. Exact artifacts used

- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/final_kernel_power_owner_scope_review.md;
- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md;
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/controls/conductor_round185_exact_fibre_deletion_control.md;
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/conductor_round185_report_reconciliation.md;
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/residual_fejer_parity_tangent_multiplicity_post_repair_verification.md;
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/joint_h_count_power_and_deletion_post_repair_verification.md; and
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/blind_post_unmask_literal_owner_scope_post_repair_verification.md.

The full graph parsed as 387 uniquely identified obligations with no
missing dependency references.  No other repository artifact, web
source, external theorem, or floating-point calculation was used.

## 7. Recommended state effect

Promote only the strict subordinate physical sector (K185.7), together
with its exact complement (K185.36), under the sole terminal label
strict_hard_m1_t1_residual_tangent_gcd_sector.  Any mutation remains the
conductor's responsibility through a mechanically valid State Patch.
Do not change the status of the complete residual, any hard or smooth
owner, M9-M1, M9-M2, endpoint uniformity, M9, either bridge, either
proved benchmark, the quarter target, or any exponent record.
