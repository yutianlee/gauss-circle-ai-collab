## Result

**Recommendation: revise, then promote the repaired reduction.**  The core
finite algebra is correct: the Boolean residual is the exact complement of
the accepted XOR sector; the odd/even terminal-divisor argument is correct
for (N>16); the sign-mass dichotomy is complete; the ordered Abel identity
and the sharp discrete BV dual estimate (164.C14) are valid even when the
total residual sign mass is unequal; the sliding Fejer identity and the
constant in (164.C25) are exact; (R\asymp L) has the claimed power ledger;
and the orientation of the product expansion is exactly
(d'm'-dm=r).

There is, however, one first formal flaw in the conductor candidate.
Equation (164.C17) writes a terminal term (C_ra_r) while leaving the
integration range and the set of included boundary increments unspecified.
If its integral and boundary sum are interpreted over the full
zero-extended line, the terminal term must be omitted; if they are
interpreted only from the first to the last residual divisor, the outgoing
increment at the last divisor must be excluded.  The formula is harmless on
the asymptotic rows because (a_r=0) and the physical support lies strictly
inside the two terminal divisors, but it is not an exact endpoint statement
as presently written.  This must be repaired before promotion.

Three smaller precision repairs are also required.  The minimal-(R) claim
uses (M_L\asymp L^2), whereas (164.C22) states only (M_L\ll L^2); the
one-sided theorem (164.C27) should be written with (leq), or else with an
absolute value if the stronger assertion is intended; and the expanded
tuple sum must either restrict (dm,d'm') to supported squarefree rows or
define the selectors and (\rho_N) off those rows.  These are repairs to an
otherwise correct reduction, not reasons to reject its mathematical core.

## Exact statement and hypotheses

For each supported squarefree row write

\[
 N=2^{\nu_N}M_N,qquad \nu_N\in\{0,1\},\qquad M_N\ \text{odd}.
\]

If no pair is selected, let
(mathscr R_N=\{d:d\mid M_N\}).  If (p_N,q_N) are selected, let

\[
 \rho_N(d)=1-{\bf1}_{p_N\mid d}-{\bf1}_{q_N\mid d}
             +2{\bf1}_{p_N\mid d}{\bf1}_{q_N\mid d},
 \qquad
 \mathscr R_N=\{d\mid M_N:\rho_N(d)=1\}.
\tag{R164.1}
\]

Order the complete residual universe, including zero-amplitude divisors,
as (d_1<\cdots<d_r), and put

\[
 \sigma_i=\chi_4(d_i),\qquad C_0=0,\qquad
 C_j=\sum_{i\leq j}\sigma_i,qquad
 a_i=A_N(d_i),\qquad a_0=a_{r+1}=0.                              \tag{R164.2}
\]

The amplitude is the real literal amplitude with its half-open support,
stars, point values, and zero extension.  For a regulated extension
(a_N(u)=A_N(e^u)), every boundary (\beta) has two formal increments

\[
 \Delta^-_\beta a_N=a_N(\beta)-a_N(\beta^-),\qquad
 \Delta^+_\beta a_N=a_N(\beta^+)-a_N(\beta).                    \tag{R164.3}
\]

The second increment is essential when a literal point value differs from
both one-sided limits.  These split increments are understood as a discrete
regulated path, since an ordinary distributional derivative does not see a
change at a single point followed immediately by its reversal.

For the cross-row reduction, let (c_N^{\rm rem}) be zero outside the
literal shell, let an integer interval of (M_L\asymp L^2) sites contain
that shell, and set

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad R=\lceil L\rceil.            \tag{R164.4}
\]

The accepted profile hypotheses give bounded amplitude, discrete total
variation (V_N\ll1), and smooth logarithmic derivative
(O(1+L/H)\).  The review treats (164.C27) as an explicitly open theorem,
not as an inherited estimate.

## Proof or derivation

For the subtraction seam, evaluating (R164.1) on selected-prime bit
patterns (00,10,01,11) gives (1,0,0,1).  The Round-163 kernel retains
exactly (10,01), so the two indicators sum to one at every incidence.
When there is no selected pair, the XOR sector is empty and the residual is
the entire odd divisor cube.  This verifies one-time subtraction without a
double loss at (11).

The largest odd divisor is (M_N).  It is residual in the no-pair branch
and contains both selected primes in the selected branch.  If (N) is odd,
(M_N=N>2\sqrt N) for (N>4).  If (N) is even,
(M_N=N/2>2\sqrt N) exactly when (N>16).  Thus the conductor's uniform
(N>16) cutoff is correct and (a_r=0) there.  The factor (2) remains in
the complementary factor (N/d); it is never inserted into the odd divisor
universe.

For sign mass, a selected pair gives

\[
 \mathscr R_N=\{a:a\mid M_N/(p_Nq_N)\}
 \ \dot\cup\
 \{p_Nq_Na:a\mid M_N/(p_Nq_N)\},                                \tag{R164.5}
\]

and the two terms have opposite character because
(chi_4(p_Nq_N)=-1).  Hence the positive and negative ambient masses are
equal.  With no pair,

\[
 \sum_{d\mid M_N}\chi_4(d)
 =\prod_{\ell\mid M_N}(1+\chi_4(\ell)).                          \tag{R164.6}
\]

This is zero, and therefore gives equal sign counts, if any odd prime
(ell\equiv3\pmod4) occurs.  If every odd prime factor is
(1\pmod4), every divisor has positive sign.  These are all cases, so the
claimed unequal-mass branch is exact.

Direct telescoping in (R164.2) gives

\[
 b_N^{\rm rem}
 =C_ra_r+\sum_{j<r}C_j(a_j-a_{j+1})
 =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j).                               \tag{R164.7}
\]

Let (Delta_j=a_{j+1}-a_j).  Since
(sum_{j=0}^{r}\Delta_j=a_{r+1}-a_0=0), for every real (lambda),

\[
 b_N^{\rm rem}=-\sum_{j=0}^{r}(C_j-\lambda)\Delta_j.             \tag{R164.8}
\]

Taking
(lambda=(\max_jC_j+\min_jC_j)/2) proves

\[
 \boxed{|b_N^{\rm rem}|
 \leq \frac12(\max_jC_j-\min_jC_j)
       \sum_{j=0}^{r}|a_{j+1}-a_j|.}                             \tag{R164.9}
\]

This proof never assumes (C_r=0), so it fully covers unequal total sign
mass.  It is sharp as a coefficient-uniform inequality: under the
constraint (sum\Delta_j=0), put variation (1/2) with opposite signs at
indices where (C_j) reaches its maximum and minimum.  In the all-positive
test with (a_i\equiv1), one has
(operatorname{osc}C_N=r), (V_N=2), and equality
(|b_N^{\rm rem}|=r).  Thus (164.C14) correctly absorbs unmatched mass
without a cemetery convention.

The exact Stieltjes repair is as follows.  If the compact zero extension is
traversed on the whole real line, then

\[
 \boxed{
 b_N^{\rm rem}
 =-\int_{\mathbb R}F_N(u)a'_{N,\rm sm}(u)\,du
 -\sum_{\beta}
 \bigl(F_N(\beta^-)\Delta^-_\beta a_N
       +F_N(\beta)\Delta^+_\beta a_N\bigr),}                    \tag{R164.10}
\]

where (F_N(u)=\sum_{\log d_i\leq u}\sigma_i), and there is **no**
additional (C_ra_r).  If one instead stops at (u_r=\log d_r), the
correct formula has (C_ra_r), includes the incoming increment at (u_r)
with (F_N(u_r^-)), and excludes the outgoing increment at (u_r).  At an
interior divisor boundary (\beta=\log d_k), the incoming increment is
weighted by (C_{k-1}=F_N(\beta^-)) and the outgoing increment by
(C_k=F_N(\beta)), exactly as asserted in the reports.  Thus the two-sided
point convention is correct, but (164.C17) must say which of the two global
conventions it uses.

For the Fejer seam, put
(Y_s=\sum_{j=0}^{R-1}z_{s+j}).  Expanding and counting the
(R-r) windows containing an ordered pair at positive gap (r) gives

\[
 \frac1R\sum_s|Y_s|^2
 =\sum_N|c_N^{\rm rem}|^2
 +2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).                          \tag{R164.11}
\]

Every (z_N) occurs in exactly (R) sliding windows, including at the two
zero-extended ends, so

\[
 \sum_sY_s=R\sum_Nz_N.                                          \tag{R164.12}
\]

Exactly (M_L+R-1) window starts can meet an interval of (M_L) integer
sites.  Cauchy's inequality therefore gives the claimed constant

\[
 \boxed{
 \left|\sum_Nz_N\right|^2
 \leq\frac{M_L+R-1}{R}
       \left(\frac1R\sum_s|Y_s|^2\right).}                       \tag{R164.13}
\]

There is no lost factor of (R).  Since
(M_L\asymp L^2), (R\asymp L), and
(sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon), a
one-sided upper bound

\[
 \Re\mathfrak C_{R,J,L}^{\rm rem}
 \leq C_\varepsilon L^2X^\varepsilon                            \tag{R164.14}
\]

makes the Fejer energy (O(L^2X^\varepsilon)), hence gives
(|\mathcal S_{L,1}^{\rm rem}|^2\ll L^3X^\varepsilon) and, after
renaming (\varepsilon), the target.  At the accepted diagonal scale, a
hypothetical (R=o(L)) leaves
(L^4/R\) in (R164.13), which exceeds (L^3).  This verifies the
(R\asymp L) ledger once (M_L\asymp L^2) is stated.

Finally, expand the two coefficients in a positive-shift correlation.
For each residual divisor (d\mid N), set (m=N/d); for each residual
divisor (d'\mid N+r), set (m'=(N+r)/d').  Then, with no approximation,

\[
 d'm'-dm=(N+r)-N=r.                                              \tag{R164.15}
\]

Conversely a tuple with (d'm'-dm=r), (d,d') odd,
(dm,d'm') in the literal shell, both products squarefree, and both
literal residual/support conditions determines exactly one term.  The
factor (2), if present, remains in (m) or (m').  Thus (164.C28) has
the correct sign, orientation, and multiplicity.  The displayed expanded
sum should include those squarefree/support restrictions explicitly (or
define all selectors to be zero off their domain), so that expressions
such as (\rho_{dm}(d)) are never evaluated where they are undefined.

The fixed-box prime input used for the raw capacity claim is also scoped
correctly.  Bennett--Martin--O'Bryant--Rechnitzer, Theorem 1.2, gives the
stated (q=4) theta estimate with (c_\theta(q)\leq1/840) for
(3\leq q\leq10^4) and the stated threshold bound.  Subtracting it at
fixed relative endpoints yields (gg P/\log P) primes per box and hence
(gg L^2/(\log L)^4) four-prime products.  This certifies only the
coefficient-uniform/raw transport capacity, exactly as quarantined in the
candidate; it is not a lower bound for the literal profiled, phased scalar.

## First doubtful or unproved step

The first flaw in the written candidate is the endpoint ambiguity in
(164.C17), not a failure of the underlying Abel algebra.  Repair it by
using the full-line formula (R164.10), or by specifying a finite path and
excluding its outgoing terminal increment.  The first genuinely unproved
analytic step after that repair remains (164.C27), equivalently the
one-sided actual-coefficient correlation bound (R164.14).  Neither the BV
duality, raw capacity controls, nor the diagonal energy estimate proves it.

The sentence preceding (164.C19) should also be narrowed.  Equation
(164.C19) is the new estimate needed by a coefficient-uniform use of
(164.C14); it is not logically necessary for every possible positive
within-product proof that might exploit the exact locations or values of
the literal amplitude.  The candidate's overall no-go is already
route-scoped, so this wording repair restores consistency without changing
the conclusion.

## Required control test and outcome

| Seam/control | Outcome |
|---|---|
| Boolean values (00,10,01,11) | **GREEN:** residual values are (1,0,0,1), complementary to Round-163 XOR. |
| Odd/even terminal divisor | **GREEN:** (M_N) is residual; (M_N>2\sqrt N) for both branches once (N>16). |
| Sign-mass dichotomy | **GREEN:** selected rows balance; no-pair rows balance iff some odd prime is (3\pmod4), otherwise all signs are positive. |
| Discrete Abel identity | **GREEN:** coefficient-by-coefficient telescoping proves (164.C11). |
| Sharp BV duality, unequal mass | **GREEN:** (R164.8)--(R164.9) prove the factor (1/2); the all-positive test attains equality. |
| Regulated Stieltjes endpoints | **REVISE:** incoming/outgoing cumulative values are right, but (164.C17) must choose full-line/no-terminal or finite-range/terminal conventions explicitly. |
| Sliding Fejer identity | **GREEN:** pair counting gives exactly (1-r/R) and the factor (2\Re). |
| van der Corput constant | **GREEN:** exactly (M_L+R-1) possible windows give ((M_L+R-1)/R). |
| (R\asymp L) ledger | **GREEN after notation repair:** use (M_L\asymp L^2); the square bound is (L^3X^\varepsilon). |
| One-sided off-diagonal statement | **REVISE notation:** write (Re\mathfrak C\leq C_\varepsilon L^2X^\varepsilon), or state an absolute-value bound if that stronger theorem is intended. |
| Product-shift expansion | **GREEN algebra, REVISE domain:** (d'm'-dm=r) and multiplicity one are exact; make squarefree/support restrictions or off-domain extensions explicit. |
| Raw four-prime capacity | **GREEN and quarantined:** the fixed-modulus source supports fixed boxes only; no literal profile or oscillatory lower bound follows. |
| First open theorem | **OPEN by design:** (164.C27) is neither proved nor smuggled into the reduction. |

No numerical or symbolic experiment was used.

## Dependencies and exact artifacts used

This post-unmask review used:

* `protocol.md`;
* the three Round-164 primary reports
  `blind_residual_transport_rederivation.md`,
  `complete_residual_transport_attack.md`, and
  `unmatched_transport_capacity_hostile_audit.md`;
* `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/candidates/conductor_round164_residual_transport_fejer_reduction.md`;
* the accepted kernel
  `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`;
* the earlier candidate
  `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md`, read only while resolving the accepted-kernel path; and
* the primary source [Bennett--Martin--O'Bryant--Rechnitzer, *Explicit bounds for primes in arithmetic progressions*, Theorem 1.2](https://arxiv.org/html/1802.00085v3#S1.Thmtheorem2).

No sibling review, synthesis, proof graph, or state file was used.  No
computation was performed.

## Recommended state effect

**Revise.**  Do not promote the conductor candidate verbatim.  First:

1. replace (164.C17) by the full-line formula (R164.10), or state the
   finite-range endpoint exclusions exactly;
2. state (M_L\asymp L^2) where the minimal-(R) claim is used;
3. write (164.C27) as the intended one-sided inequality;
4. restrict the expansion behind (164.C28) to supported squarefree rows,
   or define (\rho_N) and every literal coefficient off-domain; and
5. scope the necessity claim around (164.C19) to coefficient-uniform BV
   duality.

After these repairs, promote the exact Boolean partition, sign-mass
dichotomy, Abel identity, sharp BV bound (including unequal mass), raw
capacity no-go with its physical quarantine, and Fejer reduction through
(164.C28) as a proved-internal, route-scoped obstruction/reduction node.
Keep (164.C27), the complete residual target, every other few-point
channel, both hard-TOP parents, and all downstream obligations open.
