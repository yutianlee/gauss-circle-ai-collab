# Round 165 post-unmask review: variable-scale Fejer bypass

## 1. Result

**Verdict: GREEN as an exact sufficient reduction, with two non-mathematical
clarifications.** The all-\(R\) sliding identity, endpoint count, scale
budget, \(R=M_L\) short-shift payment, epsilon relabelling, and implication
from (165.V1) are correct.

There is no hidden mathematical requirement that
\(R=\lceil L\rceil\). That value is only the least scale at which the
diagonal energy fits the target-square budget. The full-line sliding
identity and endpoint-correct Cauchy inequality hold for every positive
integer \(R\). Taking \(R=M_L\) is valid.

The fact that the literal shell can be a proper, gapped subset of its
containing interval causes no error. The interval supplies an upper bound
of \(M_L+R-1\) on the number of nonzero windows; zeros only improve that
bound. Each supported coefficient is still counted in exactly \(R\)
windows.

Under (165.V1), the short shifts \(1\leq r<\lceil L\rceil\), the diagonal,
and the medium/long aggregate together give
\(\mathfrak E_{M_L}\ll_\eta L^3X^\eta\). Hence

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 \leq {2M_L-1\over M_L}\mathfrak E_{M_L}
 \ll_\eta L^3X^\eta,
\]

which yields
\(|\mathcal S_{L,1}^{\rm rem}|
\ll_\varepsilon L^{3/2}X^\varepsilon\) after taking
\(\eta=2\varepsilon\). Thus (165.V1) truly suffices.

The two requested clarifications are:

1. the number \(M_L+R-1\) is the exact cardinality of the *available
   containing-interval window range*, while the number of actually nonzero
   windows can be smaller when the literal shell is a subset; and
2. the arbitrary-array control is \(\asymp RM_L\) for a filled interval, or
   for a supported set of cardinality \(Q_L\asymp M_L\). For a completely
   unspecified subset the exact lower bound is instead
   \(RQ_L^2/(M_L+R-1)\). This does not affect the bypass proof.

## 2. Exact statement and hypotheses

Let

\[
 \mathcal J_L=\{A_L+1,\ldots,A_L+M_L\},\qquad
 M_L\asymp L^2,
\]

contain the literal support of \(c_N^{\rm rem}\). Extend the coefficient by
zero to all integers and define, without evaluating a square root off the
positive shell,

\[
 z_N=
 \begin{cases}
 c_N^{\rm rem}e(J\sqrt N),&N\text{ in the literal shell},\\
 0,&\text{otherwise}.
 \end{cases}
\]

Assume, for every \(\eta>0\),

\[
 D_L:=\sum_N|z_N|^2=\sum_N|c_N^{\rm rem}|^2
 \ll_\eta L^2X^\eta.                                    \tag{R1}
\]

For every integer \(R\geq1\), put

\[
 Y_s^{(R)}=\sum_{j=0}^{R-1}z_{s+j},\qquad
 \mathfrak E_R={1\over R}\sum_{s\in\mathbb Z}|Y_s^{(R)}|^2.
\]

Then exactly

\[
\begin{aligned}
 \mathfrak E_R
 &=D_L+2\Re\mathfrak C_R,\\
 \mathfrak C_R
 &=\sum_{1\leq r<R}\left(1-\frac rR\right)
   \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
   e\!\left(J(\sqrt{N+r}-\sqrt N)\right),               \tag{R2}\\
 |\mathcal S_{L,1}^{\rm rem}|^2
 &\leq {M_L+R-1\over R}\mathfrak E_R.                   \tag{R3}
\end{aligned}
\]

The exact target-square energy allowance obtained from (R3) is

\[
 \mathfrak E_R
 \ll_\eta {L^3R\over M_L+R-1}X^\eta.                    \tag{R4}
\]

The candidate uses \(M_L+R\) in place of \(M_L+R-1\); that is a slightly
stronger sufficient hypothesis and has the same power. For
\(\lceil L\rceil\leq R\leq M_L\),

\[
 {L^3R\over M_L+R}\asymp LR,                            \tag{R5}
\]

and (R1) fits (R4). No such fit is guaranteed from the accepted diagonal
bound when \(R=o(L)\), because then the diagonal contribution to (R3) has
size \(L^4/R\).

At \(R=M_L\), let \(R_0=\lceil L\rceil\) and write

\[
 \mathfrak C_{M_L}
 =\mathfrak C_{M_L}^{<R_0}+\mathfrak C_{M_L}^{\geq R_0}.
\]

The proposed open theorem is exactly

\[
 \Re\mathfrak C_{M_L}^{\geq R_0}
 \ll_\eta L^3X^\eta.                                    \tag{R6}
\]

Equation (R6) is (165.V1). No absolute value is required around its
medium/long aggregate.

## 3. Proof or derivation

### 3.1 All-\(R\) identity and endpoint count

Expand the full-line square:

\[
 \sum_s|Y_s^{(R)}|^2
 =\sum_{0\leq j,k<R}\sum_s z_{s+j}\overline{z_{s+k}}.
\]

For a positive difference \(r=j-k\), there are exactly \(R-r\) choices
of \((j,k)\), and after writing \(N=s+k\) the summand is
\(z_{N+r}\overline{z_N}\). The negative difference gives its conjugate.
Dividing by \(R\) proves (R2) for every positive integer \(R\). No step
uses \(R=\lceil L\rceil\), \(R\asymp L\), or \(R\leq M_L\).

If a length-\(R\) window meets the containing interval
\(\mathcal J_L\), then its start lies in

\[
 A_L-R+2\leq s\leq A_L+M_L.
\]

This interval contains exactly \(M_L+R-1\) integers. A literal supported
site \(N\in\mathcal J_L\) occurs in the \(R\) distinct windows
\(s=N-j\), \(0\leq j<R\), all of whose starts lie in this range. Therefore

\[
 \sum_sY_s^{(R)}=R\sum_Nz_N
 =R\mathcal S_{L,1}^{\rm rem}.                           \tag{R7}
\]

Cauchy on the displayed start interval gives

\[
 R^2|\mathcal S_{L,1}^{\rm rem}|^2
 \leq(M_L+R-1)\sum_s|Y_s^{(R)}|^2
 =(M_L+R-1)R\mathfrak E_R,
\]

which is (R3). If the literal shell has gaps or is a proper subset of
\(\mathcal J_L\), some \(Y_s^{(R)}\) vanish; retaining them as zero terms is
valid and can only make Cauchy's cardinality bound less sharp, never false.

### 3.2 General sufficient scale

The desired scalar square is \(O_\eta(L^3X^\eta)\). Combining this with
(R3) gives the exact allowance (R4). Suppose
\(\lceil L\rceil\leq R\leq M_L\). Since \(M_L\asymp L^2\),

\[
 {L^3R\over M_L+R}\asymp LR\geq cL^2.
\]

Thus (R1) is within this budget. A one-sided bound

\[
 \Re\mathfrak C_R
 \ll_\eta {L^3R\over M_L+R}X^\eta
\]

then gives the same bound for
\(\mathfrak E_R=D_L+2\Re\mathfrak C_R\), with constants absorbing the
diagonal and the factor \(2\). Positivity of \(\mathfrak E_R\) creates no
additional requirement when the correlation is negative.

This verifies the candidate's scale \(L^3R/(M_L+R)\). The role of
\(R_0=\lceil L\rceil\) is only to mark the diagonal-safe threshold; it is
not an identity constraint.

### 3.3 The \(R=M_L\) short-shift payment

For every fixed \(r\), zero extension and Cauchy give

\[
\begin{aligned}
 \left|\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\right|
 &\leq
 \left(\sum_N|c_{N+r}^{\rm rem}|^2\right)^{1/2}
 \left(\sum_N|c_N^{\rm rem}|^2\right)^{1/2}\\
 &\leq D_L.                                             \tag{R8}
\end{aligned}
\]

The first norm can be smaller at a literal endpoint, but is never larger
than \(D_L\). Since \(0<1-r/M_L\leq1\),

\[
 |\mathfrak C_{M_L}^{<R_0}|
 \leq(R_0-1)D_L
 \ll_\eta L^3X^\eta.                                    \tag{R9}
\]

Assuming (R6), equations (R1), (R2), and (R9) yield

\[
\begin{aligned}
 \mathfrak E_{M_L}
 &=D_L+
 2\Re\mathfrak C_{M_L}^{<R_0}
 +2\Re\mathfrak C_{M_L}^{\geq R_0}\\
 &\ll_\eta L^3X^\eta.                                   \tag{R10}
\end{aligned}
\]

Now \((2M_L-1)/M_L<2\), so (R3) and (R10) prove the target square.
For a requested final exponent \(X^\varepsilon\) on the unsquared scalar,
apply (R1) and (R6) with \(\eta=2\varepsilon\). Then taking the square root
of (R10) gives exactly

\[
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.                  \tag{R11}
\]

This confirms that (165.V1) is sufficient, including the factor \(2\), all
Fejer weights, and the endpoint terms.

### 3.4 Arbitrary-array control

For a filled interval diagnostic with
\(z_N=1\) on all \(M_L\) sites and \(R\leq M_L\), the window occupancies
are

\[
 1,2,\ldots,R-1,
 \underbrace{R,\ldots,R}_{M_L-R+1\ {\rm times}},
 R-1,\ldots,2,1.
\]

Consequently,

\[
 \mathfrak E_R
 ={(M_L-R+1)R^2+2\sum_{k=1}^{R-1}k^2\over R}
 \asymp RM_L.                                           \tag{R12}
\]

The allowed energy in (R5) is \(\asymp LR\), so this diagnostic fails by
\(M_L/L\asymp L\).

More generally, if the diagnostic is supported on a subset of
\(\mathcal J_L\) of cardinality \(Q_L\), and \(q_s\) is its window
occupancy, then

\[
 \sum_sq_s=RQ_L,\qquad
 \mathfrak E_R={1\over R}\sum_sq_s^2
 \geq {RQ_L^2\over M_L+R-1}.                            \tag{R13}
\]

Thus the same \(RM_L\) scale follows whenever \(Q_L\asymp M_L\), including
the ambient-squarefree diagnostic cited in the Round-164 report. If no
lower bound on the cardinality of a proper literal subset is assumed,
(R13), rather than \(\asymp RM_L\), is the universally correct statement.
This is only a diagnostic-scope clarification: neither (R2), (R3), (R9),
nor the sufficiency of (R6) uses a support-density lower bound.

For a real diagnostic, the cosine/sine pair from the Round-164 report
retains at least a fixed fraction of (R13), so the coefficient-sensitive
warning is not an artefact of allowing complex coefficients.

### 3.5 Downstream scope

Equation (R6) is still open. If proved, it combines with the accepted
coefficient energy and the all-\(R\) identity to prove only the displayed
residual scalar (R11) within this candidate. Any subsequent assembly with
the accepted XOR sector, the other few-point channels, or a hard-TOP parent
requires its own graph seam and is not supplied by the variable-scale
argument. Therefore the candidate's refusal to promote hard TOP, M9--M2,
M9, the pointwise bridge, the quarter theorem, or a global exponent is
correct and conservatively scoped.

## 4. First doubtful or unproved step

The first unproved estimate remains exactly (165.V1), equivalently (R6):

\[
 \Re\sum_{R_0\leq r<M_L}\left(1-\frac r{M_L}\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\eta L^3X^\eta.
\]

Nothing in the candidate estimates this medium/long aggregate. The
variable-scale observation relocates the required cancellation away from
the first \(O(L)\) shifts; it does not reduce the full problem to a positive
or coefficient-uniform statement. Its literal divisor opening still
retains squarefreeness, both selectors and parity branches, hard profiles,
zero-extended endpoints, and \(d'm'-dm=r\).

The only review caveat is presentational: the claimed
\(\asymp RM_L\) arbitrary-array control should explicitly identify either
the filled containing interval or a permitted support set with
\(Q_L\asymp M_L\). Without that cardinality input, (R13) is the exact
control. This caveat does not touch (165.V1)'s sufficiency.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| All-\(R\) sliding identity | **GREEN.** Pair multiplicity is exactly \(R-r\) for every integer \(R\geq1\). |
| Hidden \(R=\lceil L\rceil\) dependence | **GREEN.** None. That scale is only the minimal diagonal-safe choice. |
| Endpoint count | **GREEN with wording clarification.** The containing start interval has exactly \(M_L+R-1\) sites; actual nonzero windows are at most this many. |
| Literal shell is a subset | **GREEN.** Zero windows remain in the Cauchy sum and can only improve the bound. |
| General sufficient scale | **GREEN.** The exact denominator is \(M_L+R-1\); using \(M_L+R\) is slightly stronger and valid. |
| Diagonal at \(R\geq\lceil L\rceil\) | **GREEN.** \(D_L\ll L^2X^\eta\) fits \(L^3R/(M_L+R)\asymp LR\). |
| \(R=M_L\) short-shift Cauchy payment | **GREEN.** It costs at most \((R_0-1)D_L\ll L^3X^\eta\). |
| (165.V1) implication | **GREEN.** Diagonal plus short part plus its one-sided long bound give \(\mathfrak E_{M_L}\ll L^3X^\eta\). |
| Epsilon bookkeeping | **GREEN.** Use the energy hypotheses with \(\eta=2\varepsilon\) before square root. |
| Arbitrary-array control | **GREEN after support cardinality is stated.** Exact general form is (R13); it is \(\asymp RM_L\) for \(Q_L\asymp M_L\). |
| Actual-direction scope | **GREEN.** The diagnostic still fails by a factor \(\asymp L\); (165.V1) is not coefficient-uniform. |
| Downstream scope | **GREEN.** No parent or exponent promotion is justified by this open alternative frontier. |
| Numerical experimentation | **NOT USED.** Review is entirely algebraic and analytic. |

## 6. Dependencies and exact artifacts used

The post-unmask review used:

1. proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reports/complete_residual_transport_attack.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_variable_scale_fejer_bypass.md.

The previously supplied isolation baseline consisted only of protocol.md
and the Round-165 blind statement. No proof graph, active campaign,
strategy, sibling report, external source, or numerical computation was
read for this review.

## 7. Recommended state effect

**Promote the variable-scale statement only as a proved reduction.** Record
that the Fejer identity and endpoint inequality hold for every integer
\(R\geq1\), that \(R\asymp L\) is minimal rather than mandatory, and that
(165.V1) is a distinct sufficient theorem at \(R=M_L\).

**Retain (165.V1) as open.** It proves no estimate until its one-sided
medium/long actual-coefficient aggregate is established. Keep the original
short-shift frontier open as another sufficient route rather than rejecting
it.

Before durable promotion, repair only the arbitrary-array wording as in
(R13) and the typographical unmatched parenthesis in
\(\mathfrak C_{M_L}\). Make no change to the residual target, complete
\(t=1\) face, hard TOP, M9--M2, M9--M1, endpoint uniformity, M9, bridge,
quarter target, or either global exponent.
