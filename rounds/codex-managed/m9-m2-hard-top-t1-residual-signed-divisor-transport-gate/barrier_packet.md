# Round 164 barrier packet

Campaign: m9-m2-hard-top-t1-residual-signed-divisor-transport-gate

Starting graph:
81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306

## Frozen owner

Let

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
 \sum_{\substack{d\mid N,\ d\ {\rm odd}\\
 \sqrt N\leq d\leq2\sqrt N}}
 \chi_4(d)\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}d}{2\sqrt N}\right),
\]

with every inherited half-open shell, cone, profile, floor, star,
endpoint, parity rule, and zero-extension convention retained.  For each
supported squarefree \(N\), Round 163 canonically selects at most one pair
\(\{p_N,q_N\}\) of distinct odd prime divisors with

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\leq\kappa L^{-1/2},
\]

using \((N,L,\kappa)\) and not a divisor allocation.  The accepted sector
\(\mathcal S_{L,1}^{\rm cp}\) contains exactly the incidences where one
selected prime divides \(d\).  The Round-164 owner is exactly

\[
 \mathcal S_{L,1}^{\rm rem}
 =\mathcal S_{L,1}-\mathcal S_{L,1}^{\rm cp}.
\]

If no pair is selected, all physical incidences remain.  If a pair is
selected, only neither-prime and both-prime incidences remain.  The
accepted sector is subtracted exactly once.

## Required exact identity

For fixed \(N\), order the residual odd divisors
\(d_{N,1}<\cdots<d_{N,r_N}\), use the literal zero-extended amplitude
\(A_N(d)\), and set

\[
 \sigma_{N,i}=\chi_4(d_{N,i}),\qquad
 C_{N,j}=\sum_{i\leq j}\sigma_{N,i}.
\]

The discrete Abel identity

\[
 \sum_{i=1}^{r_N}\sigma_{N,i}A_N(d_{N,i})
 =
 C_{N,r_N}A_N(d_{N,r_N})
 +\sum_{j<r_N}C_{N,j}
 \{A_N(d_{N,j})-A_N(d_{N,j+1})\}
\]

must be derived with the precise divisor universe and endpoint
convention.  Its monotone-transport interpretation is valid only after
unequal sign masses and unmatched atoms are retained.

## Frozen false gains

1. The residual is not the full \(t=1\) scalar and the accepted XOR
   sector may not be subtracted twice.
2. Round 163 proves no selector density, nonemptiness, positive
   proportion, or complement estimate.
3. Existence of local exchange partners does not give a global matching;
   sign-count equality and Hall control remain necessary.
4. A cumulative-discrepancy identity is algebra, not a bound.
5. A per-\(N\) absolute transport functional must include total
   logarithmic displacement, amplitude jumps, and unmatched sign mass.
6. Semiprime or multiprime counts are route-capacity diagnostics until
   literal profiles and the outer oscillatory phase are controlled.
7. The fixed-modulus prime number theorem may support a diagnostic count
   only after an exact source audit; it does not lower-bound the physical
   signed scalar.
8. Taking an absolute value over \(N\) discards \(e(J\sqrt N)\).  If
   within-\(N\) transport is too large, a cross-\(N\) signed theorem is
   mandatory.
9. Exact cross-product phase opposition is not uniform in the arbitrary
   real centre.  Near-product phase cancellation is a separate open
   analytic problem.
10. Ordinary smooth variation does not own cone jumps, support entry or
    exit, floors, stars, or endpoint half-weights; they require explicit
    jump terms.
11. A target residual estimate would still leave the other
    \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels.
12. No residual identity or no-go transfers automatically to hard TOP,
    BAL, UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the
    quarter theorem, or either exponent.

## Required power ledger

- Positive residual capacity may be \(L^{2+o(1)}\).
- The target is \(L^{3/2}X^\varepsilon\).
- Any within-\(N\) positive transport route must save
  \(L^{1/2-o(1)}\) after unmatched mass and all amplitude variation.
- A capacity obstruction is not a physical lower bound.
- If positive transport fails, state the exact cross-\(N\) coefficient
  norm or oscillatory theorem still required.

## Exit rule

Close under exactly one label:

- hard_top_t1_residual_target;
- strict_t1_residual_transport_sector; or
- hard_top_t1_residual_transport_no_go.

Another unquantified sparse sector is not an admissible terminal result.
