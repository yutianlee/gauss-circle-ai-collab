# Round 180 Fejér-cell owner and capacity audit

- Campaign: m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate
- Round: 180
- Role: hostile barrier/no-go auditor
- Starting graph: e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
- Exit label recommended: row_gram_offdiagonal_capacity_or_self_return_no_go
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

**The reduction is valid, but the proposed local theorem is not proved.**
More precisely, the exact uniform cell estimate (180.G), together with the
literal incidence ledger, implies

\[
 \mathfrak E_M^{(2)}
 :=\frac12\sum_{\epsilon=0}^1
 \int_0^1F_M(\theta)|Z_\epsilon(\theta)|^2\,d\theta
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.A1}
\]

Collective restoration of the ordinary-zero component then gives

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon.
\tag{180.A2}
\]

The exact Round-175 endpoint identity, with the lower endpoint nonnegative,
the ordinary-zero sector restored collectively, and the short correction
paid once, gives the one-sided K26 bound.  No terminal scale is rounded.
Thus (180.G) is a correct sufficient theorem for the literal K26 endpoint.

The first unresolved step is exactly (180.G) for the complete literal
off-row form.  The complete physical product-collision sector
\(dm=d'm'\), including collisions with \(d\ne d'\), is not a failure:
it lies in the off-row form and is absolutely
\(O_\varepsilon(X^\varepsilon)\) per cell.  After it is paid, the
unequal-product off-row form remains open.

At the coefficient-uniform interface, the sharp local scale is
\(L^2X^\varepsilon\), not \(LX^\varepsilon\).  Complex dechirping, a
real cosine-dechirped family, and arbitrary real signs all realize this
local scale on admissible incidence shadows while retaining
\(\Lambda_2\asymp L^2\), \(O(L)\) cofactors per row, exact \(M\asymp
L^2\), and both parity branches.  Weighting the central subcell by
\(F_M\asymp M\) restores \(L^4\) endpoint capacity.  These are
coefficient-uniform capacity controls, not literal lower mass for
\(\lambda_N(d)\), \(Q_M^*\), or K26.  They exclude only an argument
based on energy, row length, realness, parity, \(\chi_4\) modulation,
erasing the selector, or positivity before a new literal-symbol gain.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

and let \(M\) be the exact integer cardinality of the containing interval,
with \(cL^2\le M\le CL^2\).  Put \(K=\lceil\sqrt L\rceil\).
For sufficiently large \(L\), \(2K+1<M\); bounded \(L\) is absorbed in
the implicit constant.  Retain the exact real incidence weight
\(\lambda_{dm}(d)\), including the selected/no-pair field, squarefree and
coprimality projectors, both two-adic branches, profiles, floors, stars,
hard values, endpoints, transitions, support births and deaths, and
full-line zero extension.  On nonzero atoms \(d,m\asymp L\), and

\[
 \Lambda_2=\sum_{\substack{d\ {\rm odd}\\m\ge1}}
 |\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,\qquad
 n_d:=\#\{m:\lambda_{dm}(d)\ne0\}\ll L.
\tag{180.A3}
\]

The provenance of (180.A3) is the literal opened-incidence count
\(O(L^2X^\eta)\), the bound
\(|\lambda_{dm}(d)|\ll X^\eta\), and epsilon rebudgeting.  It is not
deduced from the recombined energy \(D_L\), where cancellation could
occur.

Define \(R_{\epsilon,d}\), \(Z_\epsilon\), \(I_\nu\), and
\(\mathcal O_{\epsilon,\nu}\) exactly as in (180.2)--(180.4).  The audited
implication is

\[
 \left[
 \frac12\sum_{\epsilon=0}^1\mathcal O_{\epsilon,\nu}
 \ll_\varepsilon LX^\varepsilon
 \quad (|\nu|\le K)
 \right]
 \Longrightarrow
 Q_M^*\ll_\varepsilon L^3X^\varepsilon
 \Longrightarrow {\rm K26}.
\tag{180.A4}
\]

This implication uses the exact \(M\), not a dyadic rounding, and uses
both \(\epsilon\)-branches.  It closes only K26 and, after a separate
connector, the displayed residual scalar route.

The accompanying no-go statement is coefficient-uniform.  Under only
\(\#\Omega\ll L^2X^\varepsilon\), (180.A3), product support in an exact
\(M\)-site interval, and the two parity branches, a local positive or
absolute closure has upper capacity \(L^2X^\varepsilon\), and this order
is attained on nonliteral controls.  No literal lower bound is asserted.

## 3. Proof or derivation

### 3.1 Exact cells, wraparound, and sinc kernel

Parameterize the circular half-open cell by

\[
 \theta=\frac{\nu+u}{M}\pmod1,\qquad -\frac12\le u<\frac12.
\]

For the integer product difference \(q=dm-d'm'\), periodicity removes
the wraparound ambiguity and gives

\[
\begin{aligned}
 \int_{I_\nu}e(q\theta)\,d\theta
 &=\frac1M e(\nu q/M)
   \int_{-1/2}^{1/2}e(qu/M)\,du\\
 &=e(\nu q/M)\frac{\sin(\pi q/M)}{\pi q},
\end{aligned}
\tag{180.A5}
\]

with the continuous value \(1/M\) at \(q=0\).  Hence negative cells
crossing \(0\) have exactly the same formula.  The half-open cells
\(I_{-K},\ldots,I_K\) are pairwise disjoint, and their union is

\[
 U_K=\left[-\frac{K+1/2}{M},
            \frac{K+1/2}{M}\right)\pmod1.
\tag{180.A6}
\]

Its complement satisfies
\(M\|\theta\|\ge K+1/2>\sqrt L\).  This is an exact cover; no endpoint
or cell is rounded.

### 3.2 Physical row identity and complete row diagonal

Since \(\chi_4(d)^2=1\) for odd \(d\),

\[
 \int_{I_\nu}|Z_\epsilon|^2
 =\mathcal D_{\epsilon,\nu}+\mathcal O_{\epsilon,\nu},
 \qquad
 \mathcal D_{\epsilon,\nu}
 :=\sum_{d\ {\rm odd}}\int_{I_\nu}|R_{\epsilon,d}|^2\ge0.
\tag{180.A7}
\]

The sinc factor in (180.A5) has modulus at most \(1/M\), including
\(q=0\).  Therefore

\[
\begin{aligned}
 \mathcal D_{\epsilon,\nu}
 &\le\frac1M\sum_d
       \left(\sum_m|\lambda_{dm}(d)|\right)^2\\
 &\le\frac1M\sum_dn_d\sum_m|\lambda_{dm}(d)|^2
 \ll\frac{L}{M}\Lambda_2
 \ll_\varepsilon LX^\varepsilon.
\end{aligned}
\tag{180.A8}
\]

This is the physical row diagonal \(d=d'\).  A physical product diagonal
\(dm=d'm'\) with \(d\ne d'\) remains in
\(\mathcal O_{\epsilon,\nu}\).  Conversely, a fixed diagonal after a
character/ordinary Poisson transform is not a physical diagonal and
cannot be deleted.

The exact cross-row product collisions can, however, be paid without
discarding them.  For fixed \(N\), all odd divisors have the same parity
factor because \(N/d\equiv N\pmod2\).  Hence their total absolute
contribution is at most

\[
 \frac1M\sum_N
 \left(\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 |\lambda_N(d)|\right)^2
 \le \frac{\max_{N\asymp L^2}\tau(N)}{M}\Lambda_2
 \ll_\varepsilon X^\varepsilon.
\tag{180.A9}
\]

Thus exact collisions are an owner-complete target-safe sub-sector, not
the missing \(L\)-saving and not a license to erase a transformed
diagonal.

### 3.3 Both parities, Parseval, and the near/far Fejér ledger

Because \(d\) is odd,
\((-1)^{\epsilon m}=(-1)^{\epsilon N}\) when \(N=dm\).  Regrouping the
physical incidences gives exactly

\[
 Z_\epsilon(\theta)
 =\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
   e(J\sqrt N+N\theta),
 \qquad
 \int_0^1|Z_\epsilon|^2=D_L.
\tag{180.A10}
\]

In particular,
\(\frac12\sum_\epsilon\|Z_\epsilon\|_2^2=D_L\); there is no lost factor
two and neither Fejér peak is omitted.

For \(\theta\in I_\nu\), the standard exact Fejér formula implies

\[
 F_M(\theta)\ll\frac{M}{1+\nu^2}.
\tag{180.A11}
\]

On \(U_K^c\),

\[
 F_M(\theta)\ll
 \frac1{M\|\theta\|^2}\ll\frac ML.
\tag{180.A12}
\]

Thus Parseval gives the far-arc bound

\[
 \frac12\sum_{\epsilon=0}^1
 \int_{U_K^c}F_M|Z_\epsilon|^2
 \ll\frac ML D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.A13}
\]

Assuming (180.G), equations (180.A7)--(180.A8) give, uniformly in
\(|\nu|\le K\),

\[
 \frac12\sum_{\epsilon=0}^1
 \int_{I_\nu}|Z_\epsilon|^2
 \ll_\varepsilon LX^\varepsilon.
\tag{180.A14}
\]

By positivity, (180.A11), and
\(\sum_{\nu\in\mathbb Z}(1+\nu^2)^{-1}<\infty\),

\[
\begin{aligned}
 \frac12\sum_\epsilon\int_{U_K}F_M|Z_\epsilon|^2
 &\le
 \sum_{|\nu|\le K}\frac{CM}{1+\nu^2}
 \left\{\frac12\sum_\epsilon
 \int_{I_\nu}|Z_\epsilon|^2\right\}\\
 &\ll_\varepsilon MLX^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
\tag{180.A15}
\]

Together with (180.A13), this proves (180.A1).

### 3.4 Ordinary-zero restoration, short correction, and exact endpoint

Use the exact cardinal transform
\(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\).  The accepted reverse
character estimate gives

\[
 A_0:=\sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta \frac{L^2}{J}X^\eta.
\tag{180.A16}
\]

Writing

\[
 \mathcal Z_M
 :=\frac12\sum_\epsilon\int_0^1F_M
 \left(|Z_{\epsilon,0}|^2+
 2\Re Z_{\epsilon,0}\overline{Z_{\epsilon,*}}\right),
\]

one has
\(\mathfrak E_M^{(2)}=Q_M^*+\mathcal Z_M\).  Since
\(F_M\le M\),
\(\|Z_{\epsilon,*}\|_2\le D_L^{1/2}+A_0\), and \(L^2\le J\),

\[
\begin{aligned}
 |\mathcal Z_M|
 &\ll M\{A_0D_L^{1/2}+A_0^2\}\\
 &\ll_\varepsilon
 \left(\frac{L^5}{J}+\frac{L^6}{J^2}\right)X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
\tag{180.A17}
\]

This is collective in all odd character frequencies; it licenses no
termwise ordinary-zero estimate.  Equations (180.A1) and (180.A17)
prove (180.A2).

At the exact lower endpoint,
\(Q_{R_0}^*\ge0\) and
\(Q_{R_0}^*\ll R_0L^2X^\varepsilon\ll L^3X^\varepsilon\).
The exact accepted identity is

\[
 Q_M^*-Q_{R_0}^*
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M},
\tag{180.A18}
\]

where

\[
 |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon,\qquad
 |\mathcal Z_{R_0,M}|\ll_\varepsilon L^3X^\varepsilon.
\tag{180.A19}
\]

The correction \(B_{\rm short}\) occurs once.  From
\(-Q_{R_0}^*\le0\), (180.A2), and (180.A18)--(180.A19),
\(T_{26}\ll_\varepsilon L^3X^\varepsilon\).  The exact \(M\) is used
throughout; a strict final stopped-chain link, if present in the historical
telescope, has already telescoped into (180.A18) and is not replaced by a
doubling.

### 3.5 Sharp coefficient-uniform local capacity

Let \(\Omega\) be an incidence rectangle with \(d\asymp L\) odd,
\(m\asymp L\) even, \(\#\Omega=A\asymp L^2\), \(O(L)\) cofactors per
row, and all products in an exact interval of cardinality
\(M\asymp L^2\).  This is an admissible support/energy shadow, not the
literal residual selector.

For every coefficient array on such a shadow,

\[
 \int_{I_\nu}|Z_\epsilon|^2
 \le\frac1M\left(\sum_{\Omega}|\lambda_{dm}(d)|\right)^2
 \le\frac{A}{M}\Lambda_2
 \ll L^2.
\tag{180.A20}
\]

This capacity is sharp.  In the complex dechirped control set

\[
 \lambda_{dm}(d)=\chi_4(d)e(-J\sqrt{dm})
 \quad ((d,m)\in\Omega).
\tag{180.A21}
\]

Because every \(m\) is even, both parity branches coincide and
\(Z_\epsilon(\theta)=\sum_{\Omega}e(dm\theta)\).  On a fixed central
subarc \(|\theta|\le c/M\), after factoring one endpoint frequency, all
product phases lie in a fixed short arc.  Hence

\[
 |Z_\epsilon(\theta)|\gg A,\qquad
 \frac12\sum_\epsilon\int_{I_0}|Z_\epsilon|^2
 \gg \frac{A^2}{M}\asymp L^2.
\tag{180.A22}
\]

The row diagonal is only \(O(L)\), so the off-row form itself has order
\(L^2\).

Realness does not repair this.  Put
\(\phi_{dm}=J\sqrt{dm}\) and, for one global \(\alpha\),

\[
 \lambda_{dm}(d)
 =\chi_4(d)\cos(2\pi(\phi_{dm}+\alpha)).
\tag{180.A23}
\]

At \(\theta=0\), if
\(S=\sum_\Omega e(2\phi_{dm})\), then

\[
 Z_\epsilon(0)
 =\frac12\{e(\alpha)S+e(-\alpha)A\}.
\]

Choose \(\alpha\) so that \(e(2\alpha)S\) is nonnegative real.
Then \(|Z_\epsilon(0)|\ge A/2\).  Shrinking \(c>0\) by an absolute
amount makes the same lower bound stable on \(|\theta|\le c/M\), so
(180.A22) again holds with a different constant.

For an arbitrary-real-sign control, choose a direction \(\alpha\) for
which

\[
 \sum_{\Omega}
 |\cos(2\pi(\phi_{dm}-\alpha))|
 \ge\frac{2}{\pi}A
\]

(such a direction exists by averaging), and choose each sign to make
that projection positive.  This also gives (180.A22).  Restricting to
\(d\equiv1\pmod4\), replacing \(\chi_4\) by a constant, or erasing the
selector changes only fixed densities and leaves the same capacity.

Moreover \(F_M(\theta)\asymp M\) on a sufficiently small fixed central
subarc.  The same controls therefore have physical Fejér capacity

\[
 M\cdot L^2\asymp L^4.
\tag{180.A24}
\]

Equations (180.A22)--(180.A24) are not literal lower bounds.  A one-row
array has \(\mathcal O_{\epsilon,\nu}=0\), and a one-site array has no
off-row pair or nonzero-gap K26 contribution.  These opposite controls
show precisely why “available capacity” cannot be promoted to physical
lower mass.

## 4. First doubtful or unproved step

The first unproved step is the complete literal inequality (180.G), after
the exact product-collision sector (180.A9) if desired.  It requires one
factor \(L\) of signed anti-concentration across distinct divisor rows
inside every near-peak cell, uniformly in \(\nu\), with one outer real
part and before any row, mode, cell, shift, or divisor norm.

No permitted dependency supplies that relation:

1. the selected/no-pair field is Boolean and gives no automatic sign;
2. selected opposite-character divisor supports are disjoint rather than
   pointwise cancelling;
3. allowed all-\(1\bmod4\) no-pair support has constant character;
4. the complete zero-extended profile has variation \(O(1)\), not
   \(O(L^{-1})\);
5. exact collisions are small, but unequal near collisions remain; and
6. reality, parity, incidence energy, chirp geometry, and row length are
   all defeated by the controls in Section 3.5.

The first failure of a coefficient-uniform continuation is therefore the
step

\[
 \text{local capacity }L^2
 \quad\longrightarrow\quad
 \text{literal signed target }L.
\]

A proof must introduce a selector- and endpoint-stable relation absent
from the complex, real-cosine, and arbitrary-sign controls.  The capacity
result does not disprove such a theorem and does not imply literal
\(L^2\) mass.

## 5. Required control test and outcome

| Control | Test and outcome |
|---|---|
| exact half-open cells and wraparound | **PASS.** Equations (180.A5)--(180.A6) give a disjoint circular cover and the exact sinc kernel, including value \(1/M\) at zero difference. |
| exact \(M\asymp L^2\) | **PASS.** No power-of-two or dyadic replacement is used; all cells and endpoint formulas use the containing cardinality \(M\). |
| incidence provenance and row length | **PASS.** (180.A3) comes from the opened-incidence count and bounded weights, not from recombined energy; \(n_d\ll L\). |
| row diagonal and physical/dual distinction | **PASS.** (180.A8) is \(O(LX^\varepsilon)\). Cross-row product collisions remain off-row; a fixed transformed diagonal is not deleted. |
| exact collision | **PASS.** It is retained and bounded by (180.A9), not assumed absent. |
| near/far Fejér partition | **PASS.** Cell weights sum at scale \(M\); the complement has height \(O(M/L)\), yielding (180.A13)--(180.A15). |
| both parities and Parseval | **PASS.** (180.A10) is exact and the parity average has norm \(D_L\). The second Fejér peak is represented by the \(\epsilon=1\) gauge. |
| ordinary zero and short correction | **PASS.** Ordinary-zero terms are restored collectively in (180.A17); (180.A19) pays the short correction once. |
| terminal endpoint | **PASS.** The exact \(M\) endpoint is used; no strict terminal link is rounded to a doubling. |
| complex dechirped | **FAILS any coefficient-uniform \(L\)-contraction.** (180.A21)--(180.A22) attain local \(L^2\) capacity. |
| real cosine dechirped | **FAILS realness-only contraction.** The global phase choice in (180.A23) again attains local \(L^2\). |
| arbitrary real signs | **FAILS sign-uniform contraction.** The projection argument attains local \(L^2\). |
| constant character and erased selector | **FAILS character- or support-only contraction.** The same control survives either change. |
| all-\(1\bmod4\) no-pair | **WARNING PASSED.** Character is constant on this allowed-support shadow. It is not a density theorem or literal lower mass. |
| one row and one site | **PASS.** The off-row form is zero, so capacity is not a universal or literal lower bound; an isolated positive dual term cannot represent the assembled physical form. |
| hard boundary | **PASS for the reduction; FAILS a smooth-shift shortcut.** Zero extension retains births, deaths, point values, and order-one jumps. |
| product-collar no-repeat | **PASS.** Positive simultaneous dualization at either centred peak returns to the rank-one product collar and restores the \(L^4\) endpoint capacity. |
| fixed-shift no-repeat | **PASS.** Fixed-shift Cauchy pays \(D_L\) per shift: the \(O(L)\) short range is target-safe, while the full \(O(M)\) range restores \(L^4\). |
| minimal-scale no-repeat | **PASS.** The \(R_0\) reduction is the distinct open K17a route and is not an estimate for the K26 endpoint; no pivot is made. |
| tangent no-repeat | **PASS.** The target-safe commutator has adjoint remainder equal to the original link minus that commutator, so it self-returns. |
| scale-telescope no-repeat | **PASS.** The whole chain is exactly \(Q_M^*-Q_{R_0}^*\); nonconstant weights change the target and constant weights restore the endpoint. |
| local/endpoint ledger | **PASS.** Diagonal \(L\to L^3\); target \(L\to L^3\); positive capacity \(L^2\to L^4\); far arcs, ordinary zero, and short correction are each \(L^3\). |
| literal and downstream quarantine | **PASS.** No control is called literal mass, and no result is propagated beyond K26 and its separately reviewed residual connector. |

No numerical control was used.

## 6. Dependencies and exact artifacts used

Only the authorized context was used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_tangent_fejer_commutator_self_return_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md; and
- rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/dependency_power_selection_seam_review.md.

The exact cell and capacity derivations are internal.  No external theorem,
web source, numerical experiment, sibling report, blind artifact, or
unpermitted state file was used.  This report edits no proof graph, proof
draft, validation matrix, synthesis, control artifact, or state file.

## 7. Recommended state effect

**Recommend promotion only of the route-scoped local-capacity obstruction,
after the required independent seam and blind reviews.**  Its exact scope
is:

- (180.G) is a verified sufficient theorem for
  \(Q_M^*\ll_\varepsilon L^3X^\varepsilon\) and hence K26;
- the exact cross-row product-collision sector is target-safe;
- coefficient-uniform local positivity, realness, arbitrary signs,
  character modulation, erased selectors, row-length energy, product-collar
  closure, fixed-shift closure, the tangent commutator, and the scale
  telescope cannot supply the missing factor \(L\); and
- the diagnostic \(L^2\) local and \(L^4\) endpoint capacities are not
  literal lower bounds.

Retain K26, the complete residual scalar, the hard-TOP parents, BAL,
UNBAL, M9--M2, both M1 routes, GAR, endpoint uniformity, M9, both bridges,
the quarter theorem, and all exponent owners unchanged.  The first lawful
next analytic object remains the complete literal signed off-row theorem
(180.G), with every selector, collision, endpoint, cell, parity, and
ordinary-frequency seam retained.  This report neither proves nor
disproves that theorem.
