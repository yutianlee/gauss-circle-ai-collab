# Round 180 row-identity and Fejér-connector seam review

- Campaign: m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate
- Round: 180
- Role: independent seam reviewer
- Starting graph: e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
- Reviewed report: reports/fejer_cell_owner_capacity_audit.md
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

The row identity, circular-cell kernel, incidence and row-diagonal ledger,
one-sided near-cell implication, near/far Fejér powers, collective
ordinary-zero restoration, once-only short correction, exact-product
collision estimate, and K26 connector are all correct. I find no missing
factor \(2\), \(M\), or parity branch and no sign error.

In particular, the hypothesis

\[
 \frac12\sum_{\epsilon=0}^1\mathcal O_{\epsilon,\nu}
 \ll_\varepsilon LX^\varepsilon
 \qquad (|\nu|\le K=\lceil\sqrt L\rceil)
\tag{180.G}
\]

is only a one-sided upper estimate, but that is sufficient: the omitted
row-diagonal term is nonnegative and separately
\(O_\varepsilon(LX^\varepsilon)\). Consequently the full physical energy
in every near cell has the same one-sided upper bound. Summing the Fejér
envelopes gives

\[
 \mathfrak E_M^{(2)}
 =\frac12\sum_{\epsilon=0}^1\int_0^1F_M|Z_\epsilon|^2
 \ll_\varepsilon L^3X^\varepsilon,
\]

and the accepted ordinary-zero and endpoint identities then give
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\) and the one-sided K26 bound.

The report also correctly stops at the coefficient-uniform obstruction.
Its \(L^2\) local and \(L^4\) Fejér capacities are nonliteral diagnostics,
not lower bounds for the residual coefficient, \(Q_M^*\), or K26.

## 2. Exact statement and hypotheses

The verified implication uses the following complete ledger:

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

the exact integer containing cardinality \(cL^2\le M\le CL^2\), and
\(K=\lceil\sqrt L\rceil\). The literal weights are real, zero-extended,
supported on \(d,m\asymp L\), and retain every selector, squarefree,
coprimality, two-adic, profile, floor, star, hard-boundary, transition,
and support-birth/death field. The required accepted energy bounds are

\[
 \Lambda_2:=\sum_{d\ {\rm odd}}\sum_m|\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad n_d\ll L,
 \qquad D_L:=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{R180.1}
\]

The first two estimates have literal incidence provenance. There are
\(O(L^2X^\eta)\) opened incidences because the product interval has
\(M\asymp L^2\) sites and each product has \(X^\eta\)-bounded divisor
multiplicity; the exact weights are \(O(X^\eta)\). For fixed
\(d\asymp L\), the containing product interval permits
\(O(M/d)=O(L)\) cofactors. Epsilon rebudgeting gives the first two bounds
in (R180.1), independently of any cancellation in the recombined \(D_L\).

The report does not display \(D_L\ll L^2X^\varepsilon\) in its Section 2,
but it is an inherited accepted hypothesis stated in the reviewed Round-175
kernel and used transparently at (180.A13), (180.A17), and (180.A19). This
is not a hidden new assertion or a broken implication.

The conclusion is scoped exactly as

\[
 (180.G)\Longrightarrow
 Q_M^*\ll_\varepsilon L^3X^\varepsilon
 \Longrightarrow \mathrm{K26},
\tag{R180.2}
\]

with the second arrow using only the already accepted collective
ordinary-zero and once-only short-correction seams.

## 3. Proof or derivation

### 3.1 Circular cells and the sinc kernel

For \(q=dm-d'm'\in\mathbb Z\), write
\(\theta=(\nu+u)/M\pmod1\), \(-1/2\le u<1/2\). Periodicity gives exactly

\[
 \int_{I_\nu}e(q\theta)\,d\theta
 =\frac{e(\nu q/M)}M\int_{-1/2}^{1/2}e(qu/M)\,du
 =e(\nu q/M)\frac{\sin(\pi q/M)}{\pi q},
\tag{R180.3}
\]

with continuous value \(1/M\) at \(q=0\). Thus wraparound introduces no
extra phase or endpoint term. Since \(2K+1<M\) for large \(L\), the cells
\(I_{-K},\ldots,I_K\) are disjoint and cover

\[
 U_K=[-(K+1/2)/M,(K+1/2)/M)\pmod1.
\]

On the complement, \(M\|\theta\|\ge K+1/2>\sqrt L\). All half-open
endpoint conventions are consistent.

### 3.2 Physical rows, diagonal power, and exact collisions

Expanding the square before any modulus over rows gives

\[
 \int_{I_\nu}|Z_\epsilon|^2
 =\sum_d\int_{I_\nu}|R_{\epsilon,d}|^2
 +2\Re\sum_{d<d'}\chi_4(d)\chi_4(d')
 \int_{I_\nu}R_{\epsilon,d}\overline{R_{\epsilon,d'}},
\tag{R180.4}
\]

because \(|\chi_4(d)|^2=1\) for odd \(d\). This is exactly
\(\mathcal D_{\epsilon,\nu}+\mathcal O_{\epsilon,\nu}\), with one outer
real part.

The kernel in (R180.3) has modulus at most \(1/M\), including \(q=0\).
Hence

\[
 \mathcal D_{\epsilon,\nu}
 \le \frac1M\sum_d\Bigl(\sum_m|\lambda_{dm}(d)|\Bigr)^2
 \le \frac1M\sum_dn_d\sum_m|\lambda_{dm}(d)|^2
 \ll_\varepsilon \frac{L}{M}\Lambda_2
 \ll_\varepsilon LX^\varepsilon.
\tag{R180.5}
\]

This is the complete physical row diagonal \(d=d'\). It does not remove
cross-row collisions \(dm=d'm'\), and it makes no assertion about a fixed
diagonal in transformed variables.

For the complete exact-product sector, fixing \(N\) fixes the parity of
\(m=N/d\) for every odd \(d\mid N\). Its absolute contribution in one cell
is bounded by

\[
 \frac1M\sum_N\Bigl(\sum_{d\mid N,\ d\ {\rm odd}}
 |\lambda_N(d)|\Bigr)^2
 \le \frac{\max_{N\asymp L^2}\tau(N)}M\Lambda_2
 \ll_\varepsilon X^\varepsilon.
\tag{R180.6}
\]

This upper bound includes the same-row pieces, so it certainly bounds the
cross-row collision sub-sector. The possible factor \(2\) from \(d<d'\)
is already dominated by the full square. Thus the collision claim is
owner-complete and target-safe.

### 3.3 One-sided near cells and far arcs

Since \(d\) is odd, \((-1)^{\epsilon m}=(-1)^{\epsilon N}\) for
\(N=dm\). Therefore

\[
 Z_\epsilon(\theta)=\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
 e(J\sqrt N+N\theta),\qquad
 \|Z_\epsilon\|_2^2=D_L.
\tag{R180.7}
\]

Thus \(\frac12\sum_\epsilon\|Z_\epsilon\|_2^2=D_L\); neither parity
gauge nor the corresponding centred Fejér peak is lost.

The exact formula

\[
 F_M(\theta)=\frac1M
 \left(\frac{\sin(\pi M\theta)}{\sin(\pi\theta)}\right)^2
\]

gives, with absolute constants,

\[
 \sup_{\theta\in I_\nu}F_M(\theta)
 \ll\frac{M}{1+\nu^2},\qquad
 \sup_{\theta\in U_K^c}F_M(\theta)
 \ll\frac{M}{L}.
\tag{R180.8}
\]

The far part is therefore at most

\[
 \frac ML\cdot\frac12\sum_\epsilon\|Z_\epsilon\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.
\tag{R180.9}
\]

On a near cell, (180.G) and (R180.5) give

\[
 \frac12\sum_\epsilon\int_{I_\nu}|Z_\epsilon|^2
 =\frac12\sum_\epsilon
 (\mathcal D_{\epsilon,\nu}+\mathcal O_{\epsilon,\nu})
 \ll_\varepsilon LX^\varepsilon.
\tag{R180.10}
\]

No lower bound for the signed off-row form is needed. Positivity of the
left side licenses multiplication by the cell supremum in (R180.8), and

\[
 \sum_{|\nu|\le K}\frac{M}{1+\nu^2}
 \ll M.
\]

Hence the near contribution is \(O_\varepsilon(MLX^\varepsilon)\), which
is \(O_\varepsilon(L^3X^\varepsilon)\). This verifies the full
near/far power ledger \(L\mapsto ML\asymp L^3\).

### 3.4 Ordinary zero, endpoint identity, and K26

With the exact cardinal decomposition
\(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\), put

\[
 A_0=\sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta L^2J^{-1}X^\eta.
\]

Since \(F_M\le M\) and
\(\|Z_{\epsilon,*}\|_2\le D_L^{1/2}+A_0\), the complete zero-containing
sector satisfies

\[
 |\mathcal Z_M|
 \ll M(A_0D_L^{1/2}+A_0^2)
 \ll_\varepsilon
 \left(\frac{L^5}{J}+\frac{L^6}{J^2}\right)X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon,
\tag{R180.11}
\]

using \(M\asymp L^2\) and \(L^2\le J\). This is collective in all odd
character frequencies. Since
\(\mathfrak E_M^{(2)}=Q_M^*+\mathcal Z_M\), the physical bound implies the
claimed upper bound for \(Q_M^*\).

Finally the accepted exact endpoint identity is

\[
 Q_M^*-Q_{R_0}^*
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M}.
\tag{R180.12}
\]

Here \(Q_{R_0}^*\ge0\),
\(|B_{\rm short}|\le R_0D_L\ll_\varepsilon L^3X^\varepsilon\), and
\(|\mathcal Z_{R_0,M}|\ll_\varepsilon L^3X^\varepsilon\). Solving
(R180.12) gives

\[
 T_{26}
 \le \frac12Q_M^*+\frac12|\mathcal Z_{R_0,M}|+|B_{\rm short}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{R180.13}
\]

The sign is correct because the discarded term is
\(-Q_{R_0}^*/2\le0\). The factor \(2\) in (R180.12) is therefore handled
correctly. \(B_{\rm short}\) occurs once, and the identity already ends at
the exact \(M\), so no strict terminal link is replaced by a doubling.

### 3.5 Capacity and false controls

For an \(A\asymp L^2\) incidence shadow in an exact
\(M\asymp L^2\)-site product interval,

\[
 \int_{I_\nu}|Z_\epsilon|^2
 \le \frac1M\Bigl(\sum_\Omega|\lambda|\Bigr)^2
 \le \frac{A}{M}\Lambda_2\ll L^2.
\tag{R180.14}
\]

This bound is attained in order by complex dechirping, by the report's
real cosine construction after a single global phase choice, and by the
real-sign projection construction. On a central subarc of length
\(\asymp M^{-1}\), these controls have \(|Z_\epsilon|\gg A\), so the local
energy is \(\gg A^2/M\asymp L^2\). The row diagonal is only \(O(L)\), hence
the off-row form has order \(L^2\). Because \(F_M\asymp M\) on a smaller
central subarc, the restored physical Fejér capacity is \(L^4\).

The controls are expressly nonliteral. Restriction to one parity/two-adic
branch, constant character, or an erased selector therefore rules out only
coefficient-uniform arguments using those features alone. It supplies no
literal residual lower mass.

## 4. First doubtful or unproved step

There is no erroneous step in the reviewed reduction. The first unproved
affirmative step is exactly the complete literal one-sided off-row estimate
(180.G), or its unequal-product complement after (R180.6) is paid.

The report correctly identifies the missing gain:

\[
 \text{coefficient-uniform local capacity }L^2
 \quad\longrightarrow\quad
 \text{literal signed target }L.
\]

None of the reviewed hypotheses supplies that factor \(L\). The capacity
controls disprove only coefficient-uniform closure by positivity,
realness, parity, character constancy, row length, or erased selectors;
they do not disprove a selector- and endpoint-sensitive literal theorem.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| circular half-open cells and wraparound | **PASS.** Exact disjoint cover and sinc kernel, with \(1/M\) at zero difference. |
| incidence provenance and row length | **PASS.** Opened incidence counting, not recombined energy, gives \(\Lambda_2\ll L^2X^\varepsilon\) and \(n_d\ll L\). |
| row diagonal | **PASS.** Complete \(d=d'\) contribution is \(O_\varepsilon(LX^\varepsilon)\) in every cell. |
| one-sided use of (180.G) | **PASS.** Adding the nonnegative row diagonal gives the required full-cell upper bound. |
| physical versus transformed diagonal | **PASS.** Cross-row product collisions remain in the physical off-row form; no fixed transformed diagonal is deleted. |
| exact-product collision | **PASS.** The complete sector is \(O_\varepsilon(X^\varepsilon)\) per cell by divisor multiplicity and incidence energy. |
| both parity branches and Parseval | **PASS.** The average is exactly \(D_L\), with no extra factor \(2\). |
| near/far Fejér powers | **PASS.** Near \(ML=L^3\); far \((M/L)D_L=L^3\). |
| ordinary-zero restoration | **PASS.** Restored collectively at \(O_\varepsilon(L^3X^\varepsilon)\). |
| once-only short correction | **PASS.** \(B_{\rm short}\) is paid exactly once. |
| exact terminal endpoint | **PASS.** All formulas use the actual cardinality \(M\). |
| complex, cosine, and real-sign controls | **PASS.** Each attains local \(L^2\) coefficient-uniform capacity without asserting literal lower mass. |
| local-to-endpoint restoration | **PASS.** Multiplication by the central Fejér height \(M\asymp L^2\) restores \(L^4\). |
| owner and exponent quarantine | **PASS.** No conclusion beyond K26 and its separately required residual connector is claimed. |

No numerical control was used.

## 6. Dependencies and exact artifacts used

This review used only:

1. protocol.md;
2. state/proof_obligations.yml;
3. state/active_campaign.yml;
4. strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md;
5. proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md; and
6. rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/fejer_cell_owner_capacity_audit.md.

No web source, external theorem, numerical experiment, sibling report,
blind artifact, proof draft, validation matrix, synthesis, or State Patch
was used or modified.

## 7. Recommended state effect

Accept this seam as independent GREEN evidence that (180.G) is an exact
sufficient local theorem for \(Q_M^*\ll_\varepsilon L^3X^\varepsilon\)
and hence for the one-sided K26 endpoint after the already accepted paid
seams. Accept also the exact-product collision sector as target-safe and
the \(L^2\) local/\(L^4\) endpoint calculation only as a route-scoped
coefficient-uniform capacity obstruction.

Do not promote (180.G), \(Q_M^*\), K26, the complete residual scalar, full
\(t=1\), another hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, either M1
route, GAR, endpoint uniformity, M9, a bridge, the quarter theorem, or any
exponent. Those owners remain unchanged unless the complete literal
off-row theorem and the separately required connector reviews are proved.

GREEN
