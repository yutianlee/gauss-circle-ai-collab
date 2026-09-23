# Round 165 synthesis: parity, gcd sectors, and two exact Fejer frontiers

Round 165 closes under
**`strict_residual_short_shift_sector`**.  The validated State Patch creates
one proved-internal reduction, refines the Round-164 Fejer node, attaches
only inconclusive route evidence to the two open hard-TOP parents, records
twenty-one rejected overclaims, and preserves twenty explicit no-change
decisions.  The resulting graph is
`87d58660e7e11a23eb3d8759917e02376479ba38acaf727b0a2dc15d5920f5e0`.

## What was proved

For the complete actual residual coefficient, put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N)
\]

on its positive literal shell and zero elsewhere.  For every positive
integer window length (R), the exact sliding identity and endpoint-safe
scalar connector are

\[
 \mathfrak E_R=D_L+2\Re\mathfrak C_R,
 \qquad
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le {M_L+R-1\over R}\mathfrak E_R.
\]

Splitting each window by absolute site parity gives the exact energy
inequality

\[
 \boxed{\mathfrak E_R\le2\mathfrak E_R^{(2)}},
\]

where the right side retains exactly the even shifts with their original
Fejer weights.  The odd-(R) formula is endpoint-exact, including weight
(1/R) for the terminal even gap.  Thus no odd-shift estimate is needed.

At the minimal diagonal-safe scale (R_0=\lceil L\rceil), tangent
coordinates

\[
 a=d'-d,\qquad b=m'-m,
 \qquad r=db+am+ab
\]

show that the complete monotone sector (a,b\ge0) has only (O(L^2))
literal atoms over all shifts.  The nonpositive sectors are empty, and
all remaining tuples have (ab<0).

The exact divisor-gcd opening (g=(d,d')) has fixed row character,
row length (O(1+g)), and yields

\[
 \boxed{
 |\mathfrak C_{R_0,g\ge G_0}^{\rm rem}|
 \ll_\varepsilon {L^3\over G_0}X^\varepsilon.}
\]

Hence every fixed-fraction sector (g\ge\gamma L) is target-safe.  This
is owner-complete for opened divisor incidences, not a unique partition of
product rows.  In the dual cofactor-gcd progression, the character equals
(\sigma_0(-1)^{(r\bmod2)k}), so it is frozen on every even-shift row,
including the squarefree even-even branch.

The phase-derivative and resonance ledger is exact.  Large real
derivatives do not give modulo-one separation.  Classical positive
second-derivative placement and smooth row completion followed by absolute
dual modes are adverse in their stated placements only; signed, coupled,
higher-order, joint, or arithmetic transforms remain open.

## Two exact open sufficient theorems

After parity, the monotone count, and the high-gcd count, the sharpest
minimal-scale sufficient theorem is

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,{\rm opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{165.K17a}
\]

This estimate is open.

The length-(L) scale is minimal diagonal-safe but not mandatory.  At
(R=M_L\asymp L^2), fixed-shift Cauchy pays every (r<R_0) inside the
(L^3X^\varepsilon) energy budget.  The residual target would therefore
also follow from the distinct open theorem

\[
 \boxed{
 \Re\sum_{\substack{R_0\le r<M_L\\2\mid r}}
 \left(1-{r\over M_L}\right)
 \sum_N c_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{165.K26}
\]

This estimate is also open.  Its existence means that failure of the
shortest-shift attack does not terminate the Fejer strategy.

## Validation and scope

The tangent/parity, high-gcd, variable-scale, terminal-kernel, repair, and
graph seams are independently green.  The State Patch dry audit confirms
one creation, three updates, twenty-one rejections, twenty no-change
decisions, correct evidence polarity, and an acyclic dependency direction.
Round 165 used only analytical and algebraic reasoning and no numerical or
symbolic experiment.

The complete residual, full (t=1) face, other few-point channels, both
hard-TOP parents, BAL, UNBAL, M9--M2, both M9--M1 parents, endpoint
uniformity, M9, the unconditional bridge, and the quarter theorem remain
open.

There is no global exponent change:

- internally proved: (1/3);
- audited external Li--Yang benchmark:

  \[
  {3292+25\sqrt{1717}\over13762}
  =0.3144831759740614\ldots;
  \]
- target: (1/4).

## Next action

Round 166 performs the scheduled full-proof strategy and current-primary-
literature review.  It must compare (165.K17a), (165.K26), a direct
residual scalar attack, the other M2 parents, the two M1 parents, and the
global bridge before selecting the next frozen inequality.  No open
estimate may be silently promoted during that review.
