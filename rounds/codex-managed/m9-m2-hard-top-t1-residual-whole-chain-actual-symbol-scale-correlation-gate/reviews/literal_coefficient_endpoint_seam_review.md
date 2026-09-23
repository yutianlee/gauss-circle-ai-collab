# Round 175 literal-coefficient and endpoint seam review

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Round: 175
- Review target: candidates/formalized_whole_chain_scale_telescope_obstruction.md
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211

## 1. Verdict

**Localized revision required; the endpoint-collapse conclusion is sound.**

Equations (175.C5)--(175.C7), (175.C9)--(175.C15), and
(175.C16)--(175.C20) have the correct endpoint algebra, constants, one-sided
orientation, ordinary-zero restoration, once-only short correction, and
\(L^4\)-versus-\(L^3\) capacity ledger. The candidate also correctly limits
the conclusion to a method obstruction: it neither disproves the actual
signed endpoint theorem nor treats the dechirped control as literal physical
mass.

The candidate is not yet self-contained at the requested literal-coefficient
seam. Equations (175.C1)--(175.C4) name the complete coefficient and
transform but do not display the exact \(\omega_L,\rho_N,A_N\) allocation or
the cardinal interpolation defining \(U_{k,\ell}^{(\epsilon)}\).
Equations (175.C21)--(175.C22) give the correct factorization and
selected-pair difference but omit hypotheses needed to verify them
mechanically. There is also a missing plus sign in (175.C8), and the
terminal-link prose should state the strict condition with both
inequalities.

After the repairs in Section 6, the candidate is suitable as the route-scoped
obstruction
whole_chain_actual_symbol_capacity_or_self_return_no_go.

## 2. Audit of (175.C1)--(175.C4)

### (175.C1): coefficient and zero extension

The displayed sum
\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)\lambda_N(d)
\]
is consistent with the accepted coefficient: odd divisors of \(N\) are
exactly divisors of its odd part. The energy bound and outer chirp are also
correct.

Four literal data are missing from the formal statement.

1. Define \(N=2^{\nu_N}M_N\), with \(M_N\) odd. The candidate later uses
   \(M_N\) and \(R_N\) without defining them.
2. Display
   \[
   \omega_L(N)=
   \mathbf1_{N\in\mathcal I_L^{\rm lit}}\mu^2(N)
   \left(\frac{L^2}{N}\right)^{3/4}.
   \]
   Without it, the squarefree projector, shell, and normalization are only
   asserted in prose.
3. Assign to \(A_N(d)\) the exact coprimality mask, complementary two-adic
   profile branch, Vaaler/profile factor, floors, stars, hard support,
   support crossings, endpoints, point values, and divisor-coordinate zero
   extension.
4. Define \(z_N=c_N^{\rm rem}e(J\sqrt N)\) only on positive literal support
   and set \(z_N=0\) everywhere else. This prevents evaluation of a square
   root at a zero-extended or nonpositive site.

The two-adic content is compatible with the accepted kernel but should be
made explicit. On a live squarefree row,
\(\nu_N\in\{0,1\}\). Since \(d\) is odd, \(m=N/d\) has the same parity as
\(N\). Thus the physical even-gap form contains the odd--odd and even--even
branches, has \(4\mid r\) in the latter, and has no mixed branch.

### (175.C2): chain and terminal endpoint

The recursion and minimal terminal index are correct. Replace

> If \(M<2R_{K-1}\), the final link is the actual strict link

by the fully typed condition
\[
 R_{K-1}<M<2R_{K-1}.
\]
If \(M=2R_{K-1}\), the last link is the exact doubling. This is a wording
repair, not an algebraic defect, because minimality already implies
\(R_{K-1}<M\).

The candidate also uses \(F_R\) without defining it. Insert
\[
 F_R(\theta)=\sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta),
 \qquad B_{R,S}=F_S-F_R.
\]

### (175.C3)--(175.C4): transform and literal cells

The constants and ranges are correct: both \(\epsilon\)-branches, \(i/2\),
odd \(k\), the exact ordinary zero/nonzero partition, the squared constant
\(1/8\), and one outer real part are retained.

However, \(U_{k,\ell}^{(\epsilon)}\) is undefined in the candidate.
Consequently (175.C3)--(175.C4) do not themselves certify the retention of
cells, endpoints, point values, support births/deaths, transitions, or zero
extension. Insert the frozen cardinal formulas
\[
\begin{aligned}
 \mathcal W_\epsilon(x,y)
 &=\sum_{\substack{d,m\ge1\\d\ \mathrm{odd}}}
 (-1)^{\epsilon m}\omega_L(dm)\rho_{dm}(d)A_{dm}(d)
 \varphi(x-d)\varphi(y-m),\\
 \mathcal B_{\epsilon,\theta}(x,y)
 &=\mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy),\\
 U_{k,\ell}^{(\epsilon)}(\theta)
 &=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell),
\end{aligned}
\]
where \(\varphi\in C_c^\infty((-1/2,1/2))\) is real,
\(\varphi(0)=1\), and every forbidden or outside literal incidence has its
exact value zero. Also display the physical equality
\[
 Z_\epsilon(\theta)
 =\sum_N(-1)^{\epsilon N}z_Ne(N\theta),
 \qquad (-1)^{\epsilon N}=(-1)^{\epsilon m},
\]
before the \(i/2\) transform. These additions mechanically connect
(175.C1) to (175.C3) and certify both absolute-parity branches.

No cell or endpoint may be smoothed in this repair. The compact bump
interpolates the exact integer point value, including a hard endpoint or
zero.

## 3. Audit of (175.C21)--(175.C22)

### (175.C21): exact \(\omega\rho A\) allocation

The factorization
\[
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d)
\]
is correct, and all three factors are independent of the stopped-scale
index. For mechanical verification, expand (175.C21) with the exact
\(\omega_L\) above and
\[
 \rho_N(d)=
 \begin{cases}
 1,&\text{if no pair is selected},\\
 1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d},
 &\text{if }p_N,q_N\text{ are selected}.
 \end{cases}
\]
The second case is the Boolean complement of XOR, with values
\(1,0,0,1\); it is not itself a signed weight.

With this repair, the candidate's squarefree conclusion is correctly scoped.
The factor \(\mu^2(N)\) is a nonnegative literal projector. A Möbius opening
gives no automatic gain unless all auxiliary terms remain signed until they
restore either that projector or the literal zero.

### (175.C22): selected and no-pair algebra

The selected-pair identity is correct after adding its hypotheses. For a
live squarefree selected row, write
\[
 M_N=p_Nq_NR_N,\qquad p_N,q_N\nmid R_N,\qquad
 \chi_4(p_Nq_N)=-1.
\]
The selector retains only \(d=a\) and \(d=p_Nq_Na\), \(a\mid R_N\), and
therefore
\[
 c_N^{\rm rem}
 =\omega_L(N)\sum_{a\mid R_N}\chi_4(a)
 \{A_N(a)-A_N(p_Nq_Na)\}.
\]
This proves (175.C22). The accepted \(p_Nq_N\ge15\) support separation says
that the two values in a brace cannot both be nonzero. The exact safe
consequence is
\[
 |A_N(a)-A_N(p_Nq_Na)|
 =|A_N(a)|+|A_N(p_Nq_Na)|.
\]
It shows absence of pointwise cancellation between paired incidences but
gives no lower bound on either profile value.

The phrase

> Unit-profile zero mass becomes an order-one zero-extension boundary
> difference

must be qualified as a statement about the unit-profile diagnostic only.
Replace it by:

> In the unit-profile diagnostic the disjoint pair has a full boundary
> difference. For the actual profile, disjointness prevents pointwise
> cancellation but supplies no lower bound on the surviving value and no
> physical lower mass.

The no-pair branch is correctly scoped. With \(\rho_N\equiv1\),
\[
 \sum_{d\mid M_N}\chi_4(d)
 =\prod_{p\mid M_N}(1+\chi_4(p)),
\]
and if every odd prime factor is \(1\bmod4\), the divisor character is
constantly \(+1\). This refutes universal rowwise character cancellation but
is neither a density statement nor a lower bound for the actual weighted
aggregate.

The profile-BV statement is also correctly method-scoped provided it remains
an upper-capacity statement. The full Abel formula has both outer
zero-extension endpoints. Its \(O(1)\) total variation supplies no automatic
\(O(L^{-1})\) multiplier; it does not assert a lower bound for actual
variation.

## 4. Endpoint, zero-mode, and capacity seam

The following parts pass.

1. Complete expansion of
   \(Q_R^*=\frac12\sum_\epsilon\int F_R|Z_{\epsilon,*}|^2\)
   gives \(\mathcal N_{R,S}=Q_S^*-Q_R^*\) with factor \(1/8\).
2. The unweighted chain telescopes exactly to
   \(Q_M^*-Q_{R_0}^*\). A strict terminal link is included only under the
   condition in Section 2; an exact final doubling remains a doubling.
3. For \(0<R<S\), the physical coefficient
   \(b_{R,S}(r)=f_S(r)-f_R(r)\) is nonnegative and telescopes to (175.C10).
   The zero physical coefficient does not delete a fixed dual diagonal.
4. The ordinary-zero-containing sector is restored after the full signed
   odd-character recombination, and the short correction appears exactly
   once. Thus (175.C15) is the correct target-strength equivalence to K26.
5. Positivity gives only
   \(Q_M^*\ll MD_L\ll L^4X^\varepsilon\), against the
   \(L^3X^\varepsilon\) target. This restores exactly one factor \(L\).
6. The dechirped even-site family is expressly nonliteral and proves only
   coefficient-uniform method capacity.

Three localized repairs remain.

First, (175.C8) is missing a plus sign. The exact formula is
\[
\boxed{
\sum_{j=0}^{K-1}a_j\mathcal N_{R_j,R_{j+1}}
=a_{K-1}Q_M^*-a_0Q_{R_0}^*
+\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*.}
\]

Second, make the nonadjacent endpoint use in (175.C13) explicit:
\[
 |\mathcal Z_{R_0,M}|
 \ll (M+R_0)\left(
 D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\]
This shows that the ordinary-zero sector is paid once at the whole endpoint
and does not assume \(M\le2R_0\).

Third, after (175.C20), specify \(H=L^2=J^{1/2}\) when \(X=L^8\), and
place the \(M\)-site control interval at positive integers. The capacity
calculation itself is correct.

## 5. No-go scope and lower-mass audit

The no-go boundary passes after the C22 wording repair.

- The candidate states that (175.C15) proves no estimate.
- It leaves a direct signed endpoint theorem, a selector-stable joint
  transform, a coefficient-sensitive positive theorem, and the fully
  recombined product/gap/cell/frequency theorem open.
- It states that K26 remains open.
- It quarantines (175.C18)--(175.C20) as a dechirped nonliteral array and
  disclaims physical lower mass.
- The all-\(1\bmod4\) no-pair row is only an allowed-support warning.
- The one-site test is used only to require complete dual and boundary
  recombination.
- No fixed dual diagonal is identified with the zero physical diagonal.
- Neither rank-one centred stationary phase nor the Round-173 tangent first
  difference, adjoint, or second-Abel return is used.
- The telescope survives arbitrary-sign, dechirped, constant-character, and
  erased-selector controls. It is therefore correctly recognized as
  coefficient-independent, not as the missing actual-symbol gain.

There is no overclaim that the actual signed endpoint theorem fails. The
only lower-bound ambiguity is the phrase “order-one zero-extension boundary
difference” in the C22 discussion; the replacement in Section 3 removes it.

Owner scope also passes. The candidate cannot promote K26, the residual
scalar, another \(t=1\) channel, hard TOP, BAL, UNBAL, M9--M2, M1/GAR,
endpoint assembly, M9, a bridge, the quarter theorem, or an exponent.

## 6. Exact required repairs

1. Expand (175.C1)/(175.C21): define \(N=2^{\nu_N}M_N\), the exact
   \(\omega_L(N)\), both cases of \(\rho_N(d)\), and the allocation of all
   literal masks, two-adic profiles, hard values, and zero extension to
   \(A_N(d)\).
2. Type zero extension before the square root.
3. Define \(F_R\) and \(B_{R,S}\).
4. Insert the physical \(Z_\epsilon\), disjoint cardinal
   \(\mathcal W_\epsilon\), \(\mathcal B_{\epsilon,\theta}\), and
   \(U_{k,\ell}^{(\epsilon)}\) definitions.
5. State the odd--odd/even--even two-adic ledger and \(4\mid r\) in the
   even--even branch.
6. State “strict if \(R_{K-1}<M<2R_{K-1}\), exact doubling if
   \(M=2R_{K-1}\)” everywhere.
7. Insert the missing plus sign in (175.C8).
8. Add the squarefree selected-pair hypotheses to (175.C22).
9. Replace the C22 “order-one” phrase by the exact disjoint-support equality
   and expressly disclaim an actual-profile lower bound.
10. Display the endpoint ordinary-zero bound with its \(M+R_0\) factor.
11. Complete the diagnostic line with \(H=L^2\) and a positive interval.

No change to the endpoint-collapse conclusion, capacity conclusion, terminal
label, or owner boundary is required.

## 7. Recommended state effect

Recommended effect: **revise the candidate, then retain it as a route-scoped
obstruction; make no proof-state promotion from this review alone.**

After the eleven localized repairs, the candidate exactly supports the
conclusion that the unweighted whole stopped chain is one endpoint difference
and that coefficient-independent scale algebra or positivity does not save
the missing factor \(L\). The complete literal signed endpoint estimate
remains open, and no literal lower bound has been proved.
