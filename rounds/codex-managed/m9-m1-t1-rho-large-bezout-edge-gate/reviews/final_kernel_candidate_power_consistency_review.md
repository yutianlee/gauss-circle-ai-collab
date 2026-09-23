# Round 192 final-kernel candidate/power consistency review

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Role: independent final-kernel normalization and power audit
- Kernel reviewed:
  proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md
- Kernel SHA-256:
  e02b850f42bc915d696764aa6452800cd41652c3efdb8882c6ff04832fb108fe
- Locked candidate SHA-256:
  9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5

## 1. Verdict

**REPAIR.** The normalization, signed-divisor count, Farey-family cost,
fixed estimate, outer lift, shell ledger, \(T=0\) convention, exact floor
criterion, pigeonhole conclusion, endpoint translations, and proof-state
scope all agree with the locked candidate. There is one local claim-scope
regression in (192.K33).

### First and only defect

Immediately before (192.K33), the kernel says:

> For a finite or summable sequence extended by zero to all integer heights,

whereas the locked candidate (192.C37) says:

> For every finite or absolutely summable height sequence \(W\), extended by
> zero to all \(h\in\mathbb Z\),

The word “summable” is not an exact preservation of the deliberately
repaired “absolutely summable” hypothesis. If it is read as merely
conditionally summable, the bilateral index shift used to derive
(192.K33) is not justified without a specified summation convention and
shift-invariance theorem. This is a claim inflation relative to the locked
candidate, even though “summable” is sometimes informally used to mean
absolutely summable.

### Exact repair

Replace the sentence before (192.K33) by:

> For every finite or absolutely summable height sequence \(W\), extended by
> zero to all \(h\in\mathbb Z\),

No equation, bound, dependency, state scope, or other kernel text needs to
change. Subject to that one-word hypothesis repair, the kernel passes this
audit.

## 2. Exact hypotheses and canonical normalization

The kernel begins by retaining the exact accepted Round-191 hard-M1
\(t=1\) rho-large remainder. Consequently the hypotheses abbreviated in
(192.K1)--(192.K2) inherit, without weakening, the locked candidate’s

\[
 X\ge2,\quad
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\quad
 Y<h\le2Y,
\]

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,\quad
 (a,q)=1,
\]

\[
 U\mid u,\quad g=u/U,\quad
 \kappa,g,U\ {\rm odd},\quad
 (u,v)=(U,h)=1,
\]

the literal carrier inequality, \(u\asymp v\asymp L/\kappa\), total
literal \(v\)-length \(O(u)\), \(L\ll X^{1/4}\), the exact fast predicate,
and one nonempty power-of-two \(J\)-band. The direct Round-191 dependency is
named again in Section 7. The abbreviated display therefore does not enlarge
the parameter range.

The canonical normalization is unchanged:

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2}.
\]

Odd \(U\) gives a unique signed least inverse. The identity implies
\((\rho,\beta)=1\) and \(0\le\beta/\rho\le1\), with the same positive,
negative, and edge cases as the candidate. For a literal representative
\(v=v_0+nU\),

\[
 \gamma=\beta+n\rho,
\]

so the kernel preserves the canonical-\(\beta\)/literal-\(\gamma\)
distinction. For \(1\le c\le A\le U-1\),

\[
 \rho(cv_0-dU)=c+U\ell_{c,d}\ne0,
\]

because the right side is congruent to \(c\not\equiv0\pmod U\). No
normalization or nonvanishing hypothesis is lost.

## 3. Signed-divisor, Farey-family, and fixed-packet ledger

For fixed \((c,d,\ell)\), put \(N=c+U\ell\ne0\). Every row maps injectively,
through its signed least inverse, into a signed divisor \(\rho\mid N\).
Hence (192.K17)

\[
 \#\{v_0\bmod U:\ell_{c,d}(v_0)=\ell\}
 \le2\tau(|c+U\ell|)
\]

has the exact sign factor and no missing \(v_0\), \(\beta\), or factor-pair
multiplicity.

For \(|\ell|\le T\),

\[
 0<|N|<U^2\ll X^{1/2}.
\]

When \(T\ge1\), \(2T+1\le3T\), so one covector contributes
\(O_\eta(TX^\eta)\) canonical classes. The \(\ell=0\) fibre is included
and has \(N=c\ne0\). The family size remains

\[
 |\mathcal F_A|
 =2+\sum_{2\le c\le A}\varphi(c)
 \ll A^2\le Q^{2C_0}.
\]

The union indicator counts an overlapping row once; the factor \(A^2\) is
used only for the upper bound. The inherited fixed finite interval union and
\(U\mid u\) give

\[
 O(u/U+1)=O(u/U)
\]

literal representatives per residue class. Therefore (192.K21) is exactly

\[
 \#\{v\ {\rm literal}:v\in\mathcal E_A\}
 \ll_\eta A^2\frac{uT}{U}X^\eta
 \ll_\eta A^2\frac{Qmu}{Y}X^\eta.
\]

Multiplication by \(O(Y)\) heights, \(O(\kappa)\) sites, and the second
fresh \(O_\eta(X^\eta)\) literal weight gives

\[
 |P_A\mathscr J_{\rm fix}|
 \ll_\eta A^2Qm\kappa uX^{2\eta}.
\]

The terminal and Fejer restrictions are row deletions from accepted positive
bounds. Equation (192.K24) exactly replaces those two projections on
Farey-selected rows by the complete selected original packet; it does not
double them. Thus (192.K8) has the same fixed-packet content as the locked
candidate.

## 4. Fixed-to-outer power bookkeeping

The kernel retains all three exact outer inputs:

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{mq\mid u}1\le\tau_3(u).
\]

The \(m^{-1}\) cancels the \(m\) in the fixed estimate before positive
outer summation. The Farey family contributes \(Q^{2C_0}\), while the
fixed estimate contributes the single \(Q\), so the exact outer prefactor
is

\[
 Q^{2C_0+1}X^{2\eta}.
\]

Coefficient mass and the number of power-of-two bands are logarithmic, and
the remaining ledger is precisely

\[
 Q^{2C_0+1}X^{2\eta}
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u).
\]

Before subpolynomial factors,

\[
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}\kappa u
 \ll L^2\log(2L).
\]

Choosing the local \(\eta\) with \(2\eta<\varepsilon\) leaves a positive
fresh budget for the fixed power of \(Q\), \(\tau_3\), and every coefficient,
band, and shell logarithm. With \(u\ll L\ll X^{1/4}\), (192.K26) follows:

\[
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\]

No positive power of \(Y\), \(U\), or \(L\) is absorbed. There is no missing
\(Q\), \(m\), \(L\), \(Y\), \(U\), or \(X\) factor and no fixed/global type
conflation.

## 5. \(T=0\), floors, pigeonhole coverage, and claim boundary

The kernel defines \(\mathcal E_A=\varnothing\) when \(T=0\), does not use
the \(O(TX^\eta)\) density bound there, and explicitly states in Section 6
that the core is then the entire inherited rho-large remainder. The boxed
empty-core condition (192.K12) includes \(T\ge1\), so no zero-covector class
is charged to a sub-one-class budget.

For \(T\ge1\), the circular-gap proof gives exactly

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \le\left\lfloor\frac{|\rho|}{A+1}\right\rfloor.
\]

Gcd reduction preserves \(1\le c\le A\) and \(0\le d\le c\), and only
decreases the determinant. A core row therefore satisfies

\[
 |\rho|\ge(A+1)(T+1).
\]

Writing \(M=(U-1)/2\) and \(D=A+1\),

\[
 \left\lfloor\frac MD\right\rfloor\le T
 \iff M<D(T+1)
 \iff U\le2D(T+1)-1.
\]

Thus the floor and strict endpoint in (192.K12) are exact. The
\((|\rho|,|\beta|)\) zero covector is recorded only as a coverage fact and
does not override the \(T=0\) convention.

The ambient full-cover control (192.K40) retains all candidate qualifiers:
prime modulus, unsaturated \(1\le T<(U-1)/2\), an
\(\asymp U\)-class central residue universe, and the divisor slack
\(X^{-\eta}\). It is not used as literal lower mass. The kernel also leaves
(192.K13), the complete rho-large remainder, all downstream owners, and
every exponent open or unchanged. Apart from the “summable” regression
identified in Section 1, no claim inflation was found.

## 6. Dependencies and exact artifacts

This audit used:

- proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md,
  SHA-256
  e02b850f42bc915d696764aa6452800cd41652c3efdb8882c6ff04832fb108fe;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/candidates/formalized_hard_m1_t1_rho_large_farey_covector_reduction.md,
  SHA-256
  9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reports/farey_covector_sparse_sector_attack.md,
  SHA-256
  c853502a8ae8721b17c3c862a4d9b8865a80e7b2697e15950cd748b05227e2a8;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/canonical_covector_divisor_power_seam_review.md,
  SHA-256
  8090cc7205ad3f5417c428354106216072171e2e2706e30a830ccdc6b40983d0;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/blind_post_unmask_farey_covector_postrepair_verification.md,
  SHA-256
  3b61fa78517748d1c8da2625c12f667934260aa819150d293b8262f63ad2e752.

The graph dependencies remain:

- M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction;
- Divisor-bound-elementary.

The lift, projective-band, terminal, Fejer, shell, literal-support, and
endpoint connectors continue through the accepted Round-191 dependency
chain.

## 7. Hygiene and recommended effect

The reviewed kernel bytes are strict UTF-8, contain zero forbidden C0/DEL
characters, and use LF-only line endings:

- byte count: 11,036;
- CR count: 0;
- LF count: 469;
- forbidden control count: 0.

Recommended effect: apply only the exact “absolutely summable” wording repair
in Section 1, then rerun a byte-specific post-repair consistency and hygiene
check. Do not promote or alter any mathematical owner, state, exponent, or
dependency on the basis of this review alone.
