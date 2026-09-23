# Round 192 synthesis

## Outcome

Round 192 proves a strict Farey-covector sparse sector inside the exact
Round-191 rho-large hard-M1 \(t=1\) remainder.

For \(v_0=[v]_U\), define

\[
 \rho v_0-\beta U=1,\qquad
 T=\min\!\left\{\frac{U-1}{2},
       \left\lfloor\frac{H_BmU}{Y}\right\rfloor\right\}.
\]

Fix \(C_0\ge2\), set

\[
 A=\min\{U-1,\lfloor H_B^{C_0}\rfloor\},
\qquad
 \ell_{c,d}=c\beta-d\rho,
\]

and range over primitive \(1\le c\le A,\ 0\le d\le c\). For \(T\ge1\),
the union \(|\ell_{c,d}|\le T\) is target-safe; for \(T=0\), the new union
is empty.

The key identity

\[
 \rho(cv_0-dU)=c+U\ell_{c,d}\ne0
\]

gives at most \(2\tau(|c+U\ell|)\) canonical classes per fixed
\((c,d,\ell)\). Literal repetitions, heights, sites, the exact lift, and the
outer divisor ledger then give

\[
 |P_A\mathscr R_{\rm fix}|
 \ll H_Bm\kappa uX^\varepsilon,
\qquad
 |\mathcal O(P_A\mathscr R_{\rm fix})|
 \ll L^2X^\varepsilon.
\]

## Exact core and boundary

The safe union and complement form an exact complex decomposition before
the single final real part. For \(T\ge1\), every remaining core row has

\[
 |c\beta-d\rho|>T
\quad\text{for every allowed }(c,d),
\qquad
 |\rho|\ge(A+1)(T+1).
\]

The core is empty when

\[
 \left\lfloor\frac{(U-1)/2}{A+1}\right\rfloor\le T.
\]

Outside this range, the core estimate is open. Positive control still misses
the target by \(Y/(H_Bm)\). The exact literal phase, carry, and endpoint
translation identities show why static Farey separation, long-step Abel,
positive covering, and bounded-array estimates do not themselves supply
the required cancellation.

## Formalization and controls

The durable kernel is

proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md

at SHA-256

301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325.

It passed independent candidate/power, literal/core/owner, and
formalization/provenance/hygiene review after one local absolute-summability
hypothesis repair. The finite Wolfram checks had zero failures and remain
diagnostic only.

## Proof-state consequence

The State Patch creates one subordinate proved-internal reduction and
updates only the still-open hard-M1 small-\(t\) owner. It does not prove the
complete rho-large core, complete original \(t=1\), any original \(t\ge2\)
range, either M1 parent, any M2 parent, endpoint uniformity, M9, a bridge,
the quarter theorem, or a better exponent.

The internal exponent remains \(1/3\), the accepted external benchmark
remains \(0.3144831759740614\ldots\), and the target remains \(1/4\).

Round 192 closes under exactly
strict_rho_large_farey_covector_sector.

Round 193, if selected after closure, should attack only the actual jointly
signed core correlation under the unequal endpoint translations, masks,
carries, square-root phases, and affine births and deaths. Round 194 remains
the mandatory full-proof strategy and current-primary-literature checkpoint.
