# Round 200 synthesis

Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`.
Date: 2026-09-23. Conductor terminal decision:
`complete_source_interface_with_open_estimate`.

## Strategy implemented

Implemented Campaign A of the requested 23 September strategy review.
The objective was the complete original-t=1 residual, with P1 and P2
recombined before norms. Three independent roles examined the actual
source, the interval/operator lemmas, and coefficient norms and powers.
The round did not prescribe a particular cellular cancellation mechanism.

## Exact source and result

Keep the actual total zero-extended coefficients

\[
 c_N=\sum_{d\mid N,\ d\ {\rm odd}}
 \chi_4(d)\mu^2(N)\rho_N(d)a_{L,X}^{\rm lit,\sigma}(N/d,d),
 \quad z_N=c_N e(\sigma\sqrt{XN}),\quad R=\lceil L\rceil.
\]

The complete even-shift source is

\[
 C_{\rm even}=\sum_{0<r<R,\ 2\mid r}(1-r/R)
 \sum_N z_{N+r}\overline{z_N}.
\]

All endpoint allocations, characters, selectors, orientations, gcd
changes, profiles and endpoint traces remain present. On this common
domain P_cl+P1+P2=1. The coefficient in product coordinates is rank one,
with exact projective norm D=sum|c_N|^2 << L^2 X^epsilon. Thus a large
mixed-coefficient norm is **not** an inherent obstacle in these coordinates.

The independent finite proof confirms that a row-dependent interval mask
costs at most 2(1+ceil(log_2 N)) times an available all-vector bilinear
bound; J intervals cost at most J times that. Arithmetic deletions do
not become interval masks without an additional argument.

## What remains unproved

Define F_R(theta)=R^(-1)|sum_(j=0)^(R-1)e(j theta)|^2. Exactly,

\[
 Q_R:=\int_0^1\frac{F_R(\theta)+F_R(\theta+1/2)}2
 \left|\sum_N c_N e(\sigma\sqrt{XN}+N\theta)\right|^2d\theta
 =D+2\Re C_{\rm even}.
\]

The complete target remains

\[
 \boxed{Q_R\ll_\varepsilon L^2X^\varepsilon.}
\]

The general operator bound supplies only L^3 X^epsilon. The exact
even-Fejer operator norm is R/2 for even R and (R+R^(-1))/2 for odd R;
the displayed square-root phase is a diagonal unitary conjugation and
does not change it. This is an all-vector statement, not a lower bound
or counterexample for the actual arithmetic vector.

The missing factor is L in the complete correlation, or L^(1/2) after
the scalar reconstruction. A proof of the target, together with the
accepted XOR sector, would close original t=1 only.

## Quantified alternative interface

Before XOR removal, the explicit smooth original-leg coefficient admits
the gcd expansion mu^2(md)=mu^2(m)mu^2(d)sum_(g|m,d)mu(g), with norm
O(L log^2(2L)X^epsilon). For the complete literal symbol an additional
interval/BV certificate of cost V_g remains required for every inherited
sharp trace. If B_g is a proved all-vector estimate for
e(sigma g sqrt(Xab)) on a,b comparable to L/g, the sufficient scalar
ledger is

\[
 |T_{\rm full}|\ll X^\varepsilon\sum_{g\ll L,\ g\ {\rm odd}}
 \frac Lg V_g\log(2+L/g)B_g.
\]

Uniform subpower V_g and B_g << (L/g)^(1/2)X^epsilon would reach the
scalar target. Neither is asserted for the complete problem here. This
scalar route does not prove the frozen correlation estimate. No exact
Kloosterman identification or external theorem import has been established.

## Assessment and state

Round 200 delivers a checked complete-source interface and a quantified
location of the missing saving. It proves no new parent estimate,
essential reduction to an already solvable estimate, or improved global
exponent. The elementary tools are archived without graph promotion.

The State Patch is no-change. The authoritative graph and proof draft
remain byte-for-byte unchanged. The internal exponent is still 1/3; the
accepted external benchmark is still 0.3144831759740614...; the 1/4
target remains open. All other original-t sectors, M1/M2 parents and
endpoint requirements remain open or conditional as before.

The next round is pending design from these closed artifacts. Campaign B
requires an exact source-compatible arithmetic kernel and affordable
norms first. Campaign C remains a separate whole-discrepancy route.
Round 202 remains the scheduled broad strategy/literature checkpoint.

Evidence: the three reports, `controls/conductor_complete_source_operator_analysis.md`,
`reviews/independent_operator_review.md`, and
`reviews/conductor_report_reconciliation.md` in this campaign.
