# Round 164 synthesis: residual transport no-go and exact Fejer frontier

Round 164 closes under
**hard_top_t1_residual_transport_no_go**.  The validated State Patch
creates one proved-internal reduction, updates only the two open hard-TOP
parents with dependency and inconclusive evidence, records twenty-three
rejected overclaims, and preserves twenty explicit no-change decisions.
The resulting graph is
141bbc8c998981245e33f18c9c116ef12f309ecfc54898e3a1dbd4569e0f7ba0.

## What was proved

The exact residual after the accepted Round-163 XOR sector has indicator

\[
 \rho_N(d)
 =1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d}
\]

when a pair is selected, and \(\rho_N(d)=1\) otherwise.  Thus the
selected residual contains exactly the \(00\) and \(11\) incidences and
the XOR sector is subtracted once.

Its ambient character mass is zero in the selected branch.  In the
no-pair branch it is

\[
 \prod_{r\mid M_N}(1+\chi_4(r)),
\]

which vanishes if a \(3\pmod4\) prime occurs and equals
\(2^{\omega(M_N)}\) if all odd primes are \(1\pmod4\).  Ambient balance
therefore is neither universal nor a physical-window balance theorem.

For ordered residual divisors, exact Abel summation and zero extension give

\[
 b_N^{\rm rem}
 =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j)
\]

and the sharp unequal-mass BV bound

\[
 \boxed{
 |b_N^{\rm rem}|
 \leq\frac12\operatorname{osc}(C_N)
       \sum_{j=0}^{r}|a_{j+1}-a_j|.}
\]

The literal sampled profile has total variation \(V_N\ll1\), including
every hard face and point value.  The actual BV/triangle target is the
weighted sum \(\sum_N\operatorname{osc}(C_N)V_N\).  The unweighted sum
is only a coefficient-uniform envelope.

Four-prime odd and even controls have geometric physical signs
\(\{+,-,-\}\) and unit-profile residual \(-1\) for every selector status.
The audited fixed-modulus prime theorem supplies
\(\gg L^2/(\log L)^4\) such diagnostic products.  Hence no theorem
uniform over bounded-variation coefficients can close by positive
within-product transport alone.  This is not a lower bound for the actual
\(\eta_L\Phi W\) profile and not an oscillatory lower bound.

## Exact affirmative frontier

Let \(c_N^{\rm rem}\) be the actual residual coefficient, zero-extended on
an interval of \(M_L\asymp L^2\) integer sites, and take
\(R=\lceil L\rceil\).  The exact sliding energy is

\[
\begin{aligned}
 \mathfrak E_R^{\rm rem}
 &:={1\over R}\sum_s
 \left|\sum_{j=0}^{R-1}c_{s+j}^{\rm rem}e(J\sqrt{s+j})\right|^2\\
 &=\sum_N|c_N^{\rm rem}|^2
 +2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right).
\end{aligned}
\]

Every coefficient occurs in \(R\) windows and at most \(M_L+R-1\)
windows meet the support.  Therefore

\[
 \boxed{
 |\mathcal S_{L,1}^{\rm rem}|^2
 \leq\frac{M_L+R-1}{R}\mathfrak E_R^{\rm rem}.}
\]

Since \(\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon\),
the residual target follows from the single one-sided actual-direction
bound

\[
 \boxed{
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right)
 \leq C_\varepsilon L^2X^\varepsilon.}
\]

This theorem is open.  Opening both supported squarefree coefficients gives
the exact arithmetic interface

\[
 \boxed{d'm'-dm=r,\qquad1\leq r<R\asymp L,}
\]

with both selectors, parity branches, profiles, and phases retained.  The
aggregate real part is essential.  Shiftwise absolute values leave a
positive additive-shift form.  The accepted multiplicative rank-one collar
is a separate adverse positive route, not the same geometry.

## Review and source status

The statement-only derivation independently reproduced the Boolean,
sign-mass, Abel, BV, Fejer, endpoint, power, and additive-shift algebra.
Its formal endpoint and domain objections were repaired and reverified.
The independent capacity/profile/power/source review verified the
four-prime constructions, \(V_N\ll1\), fixed-modulus source hypotheses,
and all powers; its weighted-envelope, geometry, shell-length, and
literature wording objections were repaired and reverified.  The
downstream graph review certified one acyclic child, two inconclusive
parent attachments, and no downstream mutation.

The dated journal/arXiv scan found no listed later theorem improving the
classical pointwise exponent or accepting the literal short-shift
interface.  The project continues to use Li--Yang only through the accepted
five-repair narrow source audit.  This is a scoped search conclusion, not a
claim that no unindexed result exists.

Round 164 used 100% analytical/algebraic work and no numerical or symbolic
experiment.

## Full proof status

The complete residual, full \(t=1\) face, other few-point channels, and
both hard-TOP parents remain open.  The balanced and unbalanced smooth M2
packets also remain open, so M9--M2 is open.  Both direct M9--M1 parents
remain open.  Endpoint uniformity, M9, the unconditional bridge, and the
quarter theorem therefore remain open.

There is no global exponent change:

- internally proved: \(1/3\);
- externally audited Li--Yang benchmark:
  \[
  \frac{3292+25\sqrt{1717}}{13762}
  =0.3144831759740614\ldots;
  \]
- target: \(1/4\).

## Next action

Attack the exact aggregate short-shift theorem above before any
shiftwise modulus, positive Möbius opening, or divisor-pair triangle
inequality.  Any successful theorem must exploit the literal residual
arithmetic and fail on phase-aligned arbitrary coefficient arrays.  Even
after this face closes, the remaining few-point channels and near collars
must be treated separately.

