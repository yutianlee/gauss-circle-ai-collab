# Round 157 conductor seed: exact centering and target discrepancy

## 1. Result: candidate reduction

The nonzero theta matrix is exactly the original quadratic quotient
selector tested against the spatially centered literal profile. This
turns the first open row into a two-parameter signed root-discrepancy
problem.

## 2. Exact statement and hypotheses

Let

\[
 G_N(t)=\mathbf{1}_{N\mid t}\chi_4(t/N),\qquad q=4N,
\]

\[
 A_j=\widehat B_j(0),\qquad
 B_j^\circ(x)=B_j(x)-\frac{A_j}{q}.
\]

On either frozen signed block,

\[
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod q}
 B_j^\circ(x)G_N(x^2-j).
\tag{157.C1}
\]

All Round-154 through Round-156 profile, phase, cell, transition,
endpoint, sign, and normalization conventions are retained.

## 3. Proof or derivation

The complete \(v\)-sum is the original selector:

\[
 \mathcal T_U(V)=
 \sum_j\sum_{x\bmod q}B_j(x)G_N(x^2-j).
\tag{157.C2}
\]

Round 156 proves the exact zero-row identity

\[
 \mathcal Z_U(V)=\frac1q\sum_j A_j\mathscr S_N(j),
\qquad
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\tag{157.C3}
\]

Subtracting (157.C3) from (157.C2) gives (157.C1), and
\(\sum_xB_j^\circ(x)=0\).

For consecutive \(I\subset\mathbb Z/q\mathbb Z\) and a signed defect
interval \(J\), put

\[
 \mathscr D_N(I,J)=
 \sum_{j\in J}\sum_{x\in I}G_N(x^2-j)
 -\frac{|I|}{q}\sum_{j\in J}\mathscr S_N(j).
\tag{157.C4}
\]

The target discovery question is whether the literal mixed variation of
\(B_j^\circ\) reduces (157.C1) to a family of (157.C4) with total cost
\(M^{-3/4}X^\varepsilon\), and whether those discrepancies are
\(O_\varepsilon(M^{3/4}X^\varepsilon)\).

## 4. First doubtful or unproved step

No accepted result proves the necessary centered discrepancy uniformly
for the moving literal profile. One-dimensional completion has a
square-root-modulus capacity, while fixed-\(v\) interval cancellation
followed by absolute frequency aggregation restores a positive power.
The first task is to determine whether a joint signed placement avoids
both losses.

## 5. Required control test and outcome

Controls to run:

1. independently rederive every constant in (157.C1);
2. compute the exact mixed variation, including the constant tail;
3. open the selector and price the full \(N,M,V,d\) ledger;
4. retain all folds and both reciprocal-arc branches; and
5. compare every proposed gain with complete-resummation self-return,
   fixed-\(v\) \(L^1\), and one-dimensional completion controls.

Current outcome: the centering algebra is derived; the joint discrepancy
estimate is unproved.

## 6. Dependencies and exact artifacts used

- proofs/kernels/m9_m1_d1_theta_zero_row.md
- strategy/round157_d1_nonzero_theta_matrix_strategy.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/conductor_round156_adjudication.md

## 7. Recommended state effect

No graph change. Retain (157.C1) as the conductor seed until it is
independently checked and the first quantitative discrepancy theorem or
obstruction is terminally reviewed.
