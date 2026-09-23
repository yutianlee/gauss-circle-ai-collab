# Round 173 final durable-kernel mathematical review

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Kernel: proofs/kernels/m9_m2_hard_top_t1_residual_tangent_fejer_commutator_self_return_obstruction.md
- Starting graph: 70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f
- Scope: equations (173.K1)--(173.K19), constants, domains, power ledger, stopped-chain sign, and obstruction boundary
- Verdict: **REPAIR**

## 1. Result

The durable kernel is mathematically sound except for one local
self-containment issue and two associated domain qualifiers:

1. \(N_s'\), used in (173.K19), is never defined in the kernel.
2. The comparison \(m'\asymp L\) in (173.K7) is true only on a nonzero
   literal summand \(G_{d,m,v}(s)\ne0\), not for every formal
   \(v\in2\mathbb Z\).
3. The abbreviated sums in (173.K9), (173.K13), and (173.K14) should be
   declared to use the exact domain of (173.K6).

These are local exact-statement repairs. After defining
\(N_s'=(d+2s)(m+v)\), conditioning the scale comparison on
\(G_{d,m,v}(s)\ne0\), and declaring the inherited sum domain, all equations,
constants, endpoint statements, incidence powers, epsilon choices,
stopped-chain signs, and scope restrictions are GREEN. No mathematical
conclusion or power changes.

## 2. Equation-by-equation audit

| Equation | Ruling | Audit |
|---|---|---|
| (173.K1) | **GREEN** | The complete literal residual opening and energy \(D_L\ll_\varepsilon L^2X^\varepsilon\) match the accepted residual setting. |
| (173.K2) | **GREEN** | The one-sided Fejer difference is exact for every \(R<T\le2R\), including the strict final link. |
| (173.K3) | **GREEN with local addition** | The tangent expansion \(r_s=dv+2s(m+v)\) is exact and the inverse is multiplicity one. Add \(N_s':=(d+2s)(m+v)\) here for (173.K19). |
| (173.K4) | **GREEN** | \(r_s\equiv v\pmod2\) and \(\chi_4(d+2s)\chi_4(d)=(-1)^s\) are exact, including negative \(s\). |
| (173.K5) | **GREEN** | \(G\) is character-free and is evaluated only on positive literal incidences, with zero extension otherwise. |
| (173.K6) | **GREEN** | The domain \(d>0\) odd, \(m\ge1\), \(v\in2\mathbb Z\), \(s\in\mathbb Z\), factor \(2\), and one outer real part are correct. |
| (173.K7) | **REPAIR qualifier** | The equality \(r_{s+1}-r_s=2m'\) is global, but \(m'\asymp L\) holds only when \(G_{d,m,v}(s)\ne0\). |
| (173.K8) | **GREEN conditionally** | On a nonzero literal summand, global Lipschitz continuity and (173.K7) give \(O(L/R)\). |
| (173.K9) | **GREEN after domain declaration** | The commutator formula is exact when the sum uses the domain of (173.K6) and \(G=G_{d,m,v}\). |
| (173.K10) | **GREEN** | The per-link and complete-chain commutator bounds have the correct \(L^3X^\varepsilon\) power. |
| (173.K11) | **GREEN** | The finite alternating identity has factor \(2\), the correct shift sign, and no boundary term under full-line zero extension. |
| (173.K12) | **GREEN** | The split \(\Delta=\mathcal C+\mathcal R\) follows exactly from (173.K11). |
| (173.K13) | **GREEN after domain declaration** | The remainder has the correct shifted beta and forward difference. |
| (173.K14) | **GREEN after domain declaration** | Reindexing produces the adjacent sum with a plus sign and no factor \(1/2\). |
| (173.K15) | **GREEN** | \(\mathcal R=\Delta-\mathcal C\) is exact. |
| (173.K16) | **GREEN** | The accepted stopped-chain identity has the correct factor \(1/2\) and sign \(-B_{\rm short}\). |
| (173.K17) | **GREEN** | Solving (173.K16) and (173.K15) gives \(2(T_{26}+B_{\rm short})-\sum_j\mathcal C_j\), with the short correction paid once. |
| (173.K18) | **GREEN in stated scope** | \(RL^2X^\varepsilon\) is the available coefficient-uniform positive/absolute scale and becomes \(L^4X^\varepsilon\) at \(R\asymp L^2\); it is not asserted as literal lower mass. |
| (173.K19) | **REPAIR notation only** | The phase increment is correct once \(N_s'=(d+2s)(m+v)\) is defined. Its large real size gives no modulo-one separation. |

## 3. Chart, parity, and domain verification

For a positive opened pair \(N=dm\), \(N'=d'm'\) with \(d,d'\) odd,

\[
 s=\frac{d'-d}{2},\qquad v=m'-m
\]

is the unique inverse of (173.K3). Negative \(s,v\) are lawful whenever
\(d+2s>0\), \(m+v>0\), and both atoms remain literal. Modulo two,

\[
 d'm'-dm\equiv m'-m=v\pmod2,
\]

so the even link is exactly \(v\in2\mathbb Z\). The odd--odd branch has
even \(v\). In the squarefree even--even branch,
\(m=2u,m'=2u'\) with \(u,u'\) odd, hence \(4\mid v\) and
\(4\mid r_s\). Mixed product parity gives an odd gap and is absent.

The character calculation is

\[
 \chi_4(d+2s)=(-1)^s\chi_4(d),
\]

so its product with \(\chi_4(d)\) is exactly \((-1)^s\). Thus the
character-free \(G\), the domain, factor \(2\), and one outer real part in
(173.K6) all pass.

The later shorthand is unambiguous mathematically but should be made
formally explicit in a durable kernel. A single sentence before (173.K9)
is enough:

> All sums in (173.K9)--(173.K14) use the domain in (173.K6), and
> \(G(s)\) abbreviates \(G_{d,m,v}(s)\).

## 4. Continuity, incidence, and epsilon audit

At the three bandpass gates,

\[
 \beta(0)=0,\qquad
 \beta(R^-)=\frac{T-R}{T}=1-\frac RT=\beta(R^+),\qquad
 \beta(T)=0.
\]

The nonzero slopes are

\[
 \frac{T-R}{RT}\quad\text{and}\quad-\frac1T.
\]

Because \(T\le2R\), the first magnitude is at most \(1/T\). Therefore
\(\beta\) is globally \(1/T\)-Lipschitz, hence \(1/R\)-Lipschitz. No
doubling identity is used, so the same conclusion holds for
\(R<T<2R\).

On a term with \(G_{d,m,v}(s)\ne0\), both target factors are literal and
\(m'=m+v\asymp L\). If the adjacent beta difference is nonzero, at least
one of \(r_s,r_{s+1}\) belongs to \((0,T)\), and
\[
 r_{s+1}-r_s=2m'=O(L)
\]
forces
\[
 -O(L)<r_s<T.
\]
Since \(R\ge R_0\asymp L\), this is an \(O(R)\)-length signed-gap
interval. There are \(O(L^2)\) base product sites and
\(X^{O(\eta)}\) weighted double-opening cost, so the total relevant mass is
\(O(RL^2X^{C_0\eta})\). Multiplication by \(L/R\) gives
\(L^3X^{C_0\eta}\).

The stopped chain has \(O(\log L)\) links. With
\(L\le H\le X^{1/4}\), choose \(\eta\) sufficiently small relative to
the requested \(\varepsilon\) and reserve a further small \(X\)-power for
\(\log L\). This proves (173.K10) with the displayed epsilon. The strict
terminal link is included.

## 5. Split, constants, and stopped-chain sign

For finite zero-extended \(H\),
\[
 \sum_s(-1)^sH(s+1)=-\sum_s(-1)^sH(s),
\]
which proves (173.K11). Expanding
\[
 \beta_sG_s-\beta_{s+1}G_{s+1}
 =(\beta_s-\beta_{s+1})G_s
  +\beta_{s+1}(G_s-G_{s+1})
\]
gives (173.K12)--(173.K13). Reindexing only the second \(G_{s+1}\)
term gives
\[
 -\sum_s(-1)^s\beta_{s+1}G_{s+1}
 =+\sum_s(-1)^s\beta_sG_s,
\]
so (173.K14) has the required adjacent **sum**. Consequently
\(\mathcal C+\mathcal R=\Delta\) and (173.K15) is exact.

From
\[
 T_{26}=\frac12\sum_j\Delta_j-B_{\rm short}
\]
one gets
\[
 \sum_j\Delta_j=2(T_{26}+B_{\rm short}),
\]
and hence (173.K17). Both implications between the one-sided remainder
bound and the one-sided K26 bound use only absolute target bounds for
\(\sum_j\mathcal C_j\) and \(B_{\rm short}\). Cross-link cancellation and
one outer real part are preserved.

## 6. Power and exact-scope audit

The adjacent-sum carrier in (173.K14) has no \(L/R\) factor. Its positive
or absolute coefficient-uniform ledger is therefore
\(RL^2X^\varepsilon\), reaching \(L^4X^\varepsilon\) on a maximal
link. The kernel correctly labels the phase-adapted example nonliteral and
the all-\(1\bmod4\) no-pair family an allowed-support warning rather than a
density theorem, physical lower bound, or owner-complete sector.

The phase increment in (173.K19) is exactly the target-product change
\(N_s'\mapsto N_s'+2m'\). No modulo-one lower bound follows from its real
size, and moving the difference back to the weight is the already-proved
adjoint tautology.

The obstruction boundary is correctly narrow. It does not prove or
disprove K26 and does not close the residual scalar, another hard-TOP
channel, hard TOP, BAL, UNBAL, M9--M2, either M1 route, endpoint assembly,
M9, a bridge, the quarter theorem, or an exponent improvement. The
target-safe commutator has no target-safe complement and is not promoted as
a standalone owner.

## 7. Proposed repair and disposition

Make only these edits:

1. In (173.K3), define
   \[
   N_s':=(d+2s)(m+v)=d'm'.
   \]
2. Replace the prose before (173.K7) by:
   “For every \(s\), \(r_{s+1}-r_s=2m'\); on a summand with
   \(G_{d,m,v}(s)\ne0\), \(m'\asymp L\).”
3. Before (173.K9), declare that all sums through (173.K14) use the exact
   domain of (173.K6), with \(G(s)=G_{d,m,v}(s)\).
4. In the incidence paragraph, explicitly retain the qualifier
   \(G_{d,m,v}(s)\ne0\).

After these local repairs, the durable kernel is GREEN. No equation,
constant, power, stopped-chain sign, or scope conclusion otherwise needs
revision.
