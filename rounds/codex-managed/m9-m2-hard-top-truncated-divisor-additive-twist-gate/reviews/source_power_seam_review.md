# Round 161 post-unmask source/power seam review

## 1. Result: source-legal scoped no-go

**Verdict: GREEN.** The primary sources, coefficient-interface failures,
and restored-power calculation support the narrow
hard_top_radical_frequency_coupling_no_go conclusion. They do not prove
the physical hard-TOP target, a strict polynomial range, a lower bound, or
an impossibility theorem for all literature or all future methods.

The decisive points check independently:

1. Montgomery--Vaughan Theorem 1 acts on one common coefficient vector;
   the literal vectors \(B_D(t)\) vary with \(D\).
2. Bombieri--Iwaniec Lemma 2.4 is genuinely separable: its coefficient is
   \(a(x)b(y)\), and it charges absolute near-collision forms. Under the
   natural singleton specialization \(Y=1\), the \(t=1\) row collision
   form is comparable to the square of the row \(\ell^1\)-norm.
   Independently, the exact one-column evaluation norm is \(R^{1/2}\), so
   no coefficient-uniform common-test argument beats the accepted
   \(L^{2+o(1)}\) capacity there.
3. Robert--Sargos Theorem 2 counts a real four-root inequality, not the
   fixed-centre modulo-one pair collisions required here. Theorem 1 has a
   separated \(a(h,n)b(m)\) coefficient, and the restored bound is
   \[
   J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2}.
   \]
4. Miller Theorem 1.1 requires Fourier coefficients \(a_{q,n}\) of one
   fixed \(GL(3)\) cusp form, with \(q\) fixed. It is not an arbitrary
   additive-twist theorem for the literal \(D\)-dependent truncated
   divisor vectors.

Two harmless source-card clarifications should remain visible. First,
Montgomery--Vaughan Theorem 1 also prints the weighted “Moreover”
conclusion (1.6); the audit invokes only the exact unweighted conclusion
(1.4). Second, Robert--Sargos assume \(X>1\), and with \(N_0=1\) the
sole integer is \(n=2\), so for \(\gamma=1\) the exact phase match is
\(\Xi=JL/2\), not literally \(JL\). The audit writes
\(\Xi\asymp JL\), so its power calculation is unchanged.

## 2. Exact statements and hypotheses

Write

\[
 \mathcal T_L^{\rm ns}
 =\sum_{D>1\ {\rm sf}}\sum_{t\ge1}B_D(t)e(tJ\sqrt D),
 \qquad 1\ll L\ll H\asymp J^{1/2},
\]

with the literal \(B_D(t)\), support, profiles, parity, floors, endpoints,
and zero extension from the assigned artifacts. The review uses only

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),\qquad
 \sum_t|B_D(t)|\ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{161.R1}
\]

### Primary-source table

| Source | Exact printed hypotheses and conclusion relevant here | Literal Round-161 match | Seam verdict |
|---|---|---|---|
| H. L. Montgomery and R. C. Vaughan, *The large sieve*, Theorem 1, (1.1), (1.3)--(1.6), [primary PDF](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf) | \(M,N\) are integers with \(N>0\); \(a_n\) are arbitrary complex numbers; \(x_r\) are real and distinct modulo one; \(\delta=\min_{r\ne s}\|x_r-x_s\|\). For \(S(x)=\sum_{M<n\le M+N}a_ne(nx)\), (1.4) is \(\sum_r|S(x_r)|^2\le (N+\delta^{-1})\sum_n|a_n|^2\). The theorem also gives the locally weighted (1.6), using \(\delta_r=\min_{s\ne r}\|x_r-x_s\|\). | Both conclusions still use one common vector \((a_n)\). They do not estimate a row-varying matrix \(B_D(t)\) without decomposition and a positive norm. | **GREEN.** The audit’s \(N+\delta^{-1}\) is the exact printed constant, not \(N-1+\delta^{-1}\). The omitted weighted clause does not alter the interface obstruction. |
| E. Bombieri and H. Iwaniec, *On the order of \(\zeta(1/2+it)\)*, Lemma 2.4, [primary PDF](https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf) | \(\mathcal X,\mathcal Y\subset\mathbb R^K\); arbitrary complex \(a(x),b(y)\); \(X_k,Y_k>0\). The bilinear sum is \(\sum a(x)b(y)e(x\cdot y)\), restricted by \(|x_k|\le X_k,|y_k|\le Y_k\). Its square is at most \((2\pi^2)^K\prod_k(1+X_kY_k)\mathcal B(b;X)\mathcal B(a;Y)\), where the two forms contain absolute products and coordinatewise thresholds \((2X_k)^{-1}\), \((2Y_k)^{-1}\). | The source coefficient is separable. A representation of \(B_D(t)\) must be paid for term by term or through a proved projective/collision norm. | **GREEN.** The separability and absolute-value placement in the audit are exact. |
| O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, Theorem 1, [primary PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf) | \(H,N,M\) are positive integers, \(X>1\); \(|a(h,n)|,|b(m)|\le1\); \(\alpha,\beta,\gamma\) are fixed reals with \(\alpha(\alpha-1)\beta\gamma\ne0\). For the separated coefficient \(a(h,n)b(m)\), (1.3) is \((HNM)^{1+\varepsilon}\{(X/(HNM^2))^{1/4}+(HN)^{-1/4}+M^{-1/2}+X^{-1/2}\}\). | The literal \(W(h/m)\), cone, product shell, parity, floors, and endpoints do not have the required cost-one separation. Even granting it, the restored powers fail below. | **GREEN.** Replace the audit’s harmless endpoint notation \(\Xi\ge1\) by the printed \(\Xi>1\) in an exact source card. |
| Robert--Sargos, Theorem 2, same PDF | Fixed real \(\alpha\ne0,1\), integer \(M\ge2\), and real \(\delta>0\). The number of quadruples \(M<m_i\le2M\) with \(|m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|\le\delta M^\alpha\) is \(\ll_\varepsilon M^{2+\varepsilon}+\delta M^{4+\varepsilon}\), with dependence allowed on fixed parameters. | This is a four-variable Euclidean inequality. It is neither the two-radical circular condition \(\|J(\sqrt D-\sqrt E)\|\le T^{-1}\) nor a coefficient-weighted fixed-centre estimate. | **GREEN.** The audit states the right hypotheses, count, and limitation. |
| Stephen D. Miller, *Cancellation in additively twisted sums on GL(n)*, Theorem 1.1, [primary PDF](https://arxiv.org/pdf/math/0404521) | If \(a_{q,n}\) are Fourier coefficients of a cusp form on \(GL(3,\mathbb Z)\backslash GL(3,\mathbb R)\), then for every \(\varepsilon>0\), \(\sum_{n\le T}a_{q,n}e(n\alpha)=O_\varepsilon(T^{3/4+\varepsilon})\), uniformly in \(\alpha\in\mathbb R\). The implied constant depends on \(q,\varepsilon\), and the cusp form; \(q\) is held fixed. | No artifact identifies \(B_D(t)\), for any \(D\), with the coefficients of one fixed cusp form. Uniformity in \(\alpha\) does not relax the coefficient hypothesis or supply \(D\)-averaging. | **GREEN.** The audit’s coefficient no-match is exact. |

## 3. Proof and independent power derivation

### Montgomery--Vaughan and the exact one-column obstruction

With \(x_D=J\sqrt D\pmod1\), Montgomery--Vaughan controls

\[
 \sum_D\left|\sum_t c_t e(tx_D)\right|^2
\]

for one \(D\)-independent vector \(c\). Neither (1.4), its dual, nor the
weighted (1.6) changes that quantifier. On \(t=1\), over \(R\) rows, the
evaluation map is

\[
 c\longmapsto (c\,e(x_D))_{D=1}^R,
\]

whose norm is exactly \(R^{1/2}\). Its adjoint is the one-row functional
\((a_D)\mapsto\sum_Da_De(x_D)\), also of exact norm \(R^{1/2}\).
For \(R\asymp L^2\), (161.R1) therefore permits only

\[
 R^{1/2}\|B_\bullet(1)\|_2
 \ll L^2\sqrt{\log(2L)},
\tag{161.R2}
\]

leaving the asserted \(L^{1/2-o(1)}\) power unpaid. This is an operator
capacity, not a lower bound for the physical coefficient.

### Bombieri--Iwaniec at \(t=1\)

The audit’s \(\ell^1\) statement is valid with an explicit constant
ledger. Represent every circular frequency by
\(x_D\in[-1/2,1/2)\), take \(K=1\), \(X=1/2\), \(Y=1\), and
\(\mathcal Y=\{1\}\). Then \(\mathcal B(b;X)=|b(1)|^2\), while

\[
 \mathcal B(a;Y)
 =\sum_{|x_D-x_E|\le1/2}|a_Da_E|.
\]

Partition the representative interval into its two half intervals and
write \(A_-,A_+\) for the corresponding \(\ell^1\)-masses. Every pair
in one half is counted, hence

\[
 \frac12\|a\|_1^2
 \le A_-^2+A_+^2
 \le\mathcal B(a;Y)
 \le\|a\|_1^2.
\tag{161.R3}
\]

Thus the natural \(Y=T=1\) collision form is literally comparable to
\(\|a\|_1^2\), despite the Euclidean lift and wrap seam. For a one-column
decomposition \(B=\sum_ra_r\otimes b_r\), (161.R3) and the triangle
inequality give

\[
 \inf\sum_r\mathcal B(a_r;1)^{1/2}|b_r|
 \asymp\|B_\bullet(1)\|_1.
\tag{161.R4}
\]

Equation (161.R4) describes this chosen natural specialization, not a
claim that every optimization of the source parameters has the same
displayed norm. Such optimization still cannot defeat the exact
coefficient-uniform one-column norm above.

### Robert--Sargos restoration

Grant counterfactually a cost-one separation of the literal coefficient.
Put

\[
 H_0=M_0=L,\qquad N_0=1,\qquad
 \alpha=\beta=\frac12,\qquad\gamma=1,\qquad
 \Xi\asymp JL.
\tag{161.R5}
\]

Because \(1<n\le2\) means \(n=2\), the exact choice matching
\(e(J\sqrt{hm})\) is \(\Xi=JL/2\); replacing this by
\(\Xi\asymp JL\) changes no power. Theorem 1 gives

\[
\begin{aligned}
 |S_0|&\ll_\varepsilon L^{2+\varepsilon}
 \left\{
 \left(\frac{JL}{L^3}\right)^{1/4}
 +L^{-1/4}+L^{-1/2}+(JL)^{-1/2}
 \right\}\\
 &\ll_\varepsilon
 J^{1/4}L^{3/2+\varepsilon}
 +L^{7/4+\varepsilon}
 +L^{3/2+\varepsilon}
 +J^{-1/2}L^{3/2+\varepsilon}.
\end{aligned}
\tag{161.R6}
\]

The arithmetic is exact. Since \(L\ll J^{1/2}\),

\[
 \frac{J^{1/4}L^{3/2}}{L^2}
 =\left(\frac{J^{1/2}}L\right)^{1/2},
\tag{161.R7}
\]

so the first source term is never better than the \(L^2\) positive
capacity in the hard-TOP range and is strictly worse away from the
boundary. Taking the better of (161.R6) and triviality therefore leaves
\(L^2\). Also \(J^{1/4}=X^{1/8}\) cannot be absorbed in a statement for
every \(\varepsilon>0\). Theorem 2 does not repair this: its real
four-root count is not the required modulo-one, fixed-\(J\), weighted
pair-collision form.

### Miller coefficient scope

Miller’s theorem is uniform only in the additive centre. Its constant may
depend on fixed \(q\) and the fixed cusp form, and its cancellation comes
with the automorphic coefficient hypothesis. The literal \(B_D(t)\)
changes with \(D\) and with \(X\) through \(H,q_X\), floors, and profiles.
No source-legal substitution \(B_D(t)=a_{q,t}\) is supplied. At \(t=1\)
there is in any case no long additive-twist variable.

## 4. First doubtful or unproved step

The first open physical statement remains

\[
 \boxed{
 \left|\sum_{D\asymp L^2\ {\rm sf}}
 B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{161.R8}
\]

None of the four sources proves (161.R8). The exact one-column and
collision calculations show only that coefficient-uniform common-test
placement plus the accepted energy does not prove it. They do not show
that the literal left side is large. A continuation needs a theorem using
the actual signed close-factor sequence \(B_D(1)\), or a proved literal
collision/projective saving for the full varying matrix.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| MV exact constant and scope | **Pass.** The PDF prints \(N+\delta^{-1}\). The weighted (1.6) was checked and retains the common-vector restriction. |
| BI separability | **Pass.** The source coefficient is exactly \(a(x)b(y)\), with absolute weighted collision forms. |
| BI \(t=1/\ell^1\) claim | **Pass with stated specialization.** Equation (161.R3) proves comparability for \(X=1/2,Y=1\); the independent one-column norm carries the no-go if source parameters are optimized differently. |
| RS Theorem 1 restoration | **Pass.** All four terms and their \(L,J\) powers are in (161.R6); the exact \(n=2\) constant is quarantined. |
| RS Theorem 2 scope | **Pass.** Real four-root counting is not silently converted into fixed-centre circular pair spacing. |
| Miller coefficient hypothesis | **Pass.** Fixed automorphic coefficients and fixed-\(q\) dependence are retained. |
| Missing \(L^{1/2}\) | **Pass as capacity only.** (161.R2) is \(L^{2+o(1)}\) against an \(L^{3/2+o(1)}\) target. |
| Global literature impossibility | **Rejected.** The conclusion is limited to the named primary theorems and the explicit coefficient-uniform/separable interfaces. |
| Physical lower bound | **Rejected.** No nonzero-density, lower-energy, or sign-alignment statement for \(B_D(1)\) follows. |
| Downstream scope | **Pass.** No conclusion transfers beyond the one nonsquare polynomial-intermediate hard-TOP block. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used exactly:

- AGENTS.md;
- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/square_root_spacing_source_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/candidates/conductor_round161_radical_control_and_obstruction.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/controls/conductor_round161_radical_capacity_controls.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/projective_power_scope_review.md;
- the four primary PDFs linked in the source table.

No sibling report, strategy file, barrier packet, synthesis, proof draft, or
other campaign artifact was used.

## 7. Recommended state effect

Promote, subject to conductor graph validation, only the route-scoped
source/common-test obstruction under
hard_top_radical_frequency_coupling_no_go. Retain the exact \(t=1\)
formula, the target-safe long-channel sector, and the one-column power
ledger as supporting evidence.

Keep (161.R8), all remaining few-point channels, the full hard-TOP target,
every downstream M9-M2/M9/bridge obligation, and both global exponents
open. Record explicitly that the audit excludes only the named theorem
interfaces checked through 25 August 2026; it does not exclude a bespoke
coefficient-sensitive theorem, an unexamined source, or a future method.
