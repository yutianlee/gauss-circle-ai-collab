# Round 139 hostile post-unmask audit: curvature collar and directionality

## 1. Result

**Overall verdict: REVISE mechanically, then GREEN for promotion at the
stated scalar scope.**  The exact curvature collar

\[
 L_h=\left\lfloor\frac{\rho y}{\sqrt h}\right\rfloor,
 \qquad 0<\rho<\frac18,
\tag{1.1}
\]

is target-safe for the complete physical phase, literal profile, both
parities, every \(0\leq q\leq2y\), every real \(X\geq2\), and both scalar
signs:

\[
 |\mathcal C_N^\pm|\ll_{V_{\rm low},\rho}R\log(2X).
\tag{1.2}
\]

Therefore the candidate's strict scalar reduction

\[
 \mathcal F_N^\pm=\mathcal S_N^\pm+O(R\log(2X))
\tag{1.3}
\]

is correct and genuinely noninvertible on the collar.  It uses a
second-derivative estimate for the **complete exact reciprocal phase**;
it neither drops the Taylor correction nor takes moduli over separate
stationary tubes.

The one required repair is confined to the maximal-scale commentary
following (139.C15).  A generalized collar to which the same bounded-ratio
curvature calculation is applied must be written

\[
 L_{\alpha,H}=\rho yH^{-\alpha}
\tag{1.4}
\]

with the same fixed \(\rho<1\), or must explicitly be restricted to
\(d=y-v\asymp y\).  The unqualified formula \(L=yH^{-\alpha}\) reaches
\(v=y\) at \(H=1\), where the condition \(d\asymp y\), and hence the
derivation of (139.C11), fails.  This is a scope repair, not an exponent repair:
with (1.4), the rowwise ledger in (139.C15) is unchanged up to constants,
and \(\alpha=1/2\) remains exactly the last power scale certified at \(R\)
by that ledger.

The new collar strictly supersedes the blind and hostile reports only at
their perturbative seam.  Their Taylor window requires
\(v\ll(y^2/h)^{1/3}\); the exact-curvature collar is polynomially larger.
Their full-completion, coefficient-variation, aliaswise-capacity, Salié,
and Fourier self-return obstructions remain valid.  No full scalar bound
and no square-level deletion from the Round-138 residual is proved.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad 0\leq q\leq2y.
\tag{2.1}
\]

Let \(V_{\rm low}\) be the fixed real smooth lower profile, including its
literal endpoint samples and zero extension.  Its compact upper support
gives a fixed \(C_V\) such that a nonzero term satisfies

\[
 h\leq C_V\frac{y-v}{R}\leq C_V\frac yR\leq C_VR.
\tag{2.2}
\]

For \(\sigma\in\{+1,-1\}\), put

\[
 \mathcal F_N^\sigma
 =\sum_{h\geq1}\frac1h\sum_{0\leq v<y}
 \chi_4(y-v)
 V_{\rm low}\!\left(\frac{4R^2h^2}{(y-v)^2}\right)
 e\!\left(\sigma h\frac{q+v^2}{y-v}\right).
\tag{2.3}
\]

The bijection \(d\leftrightarrow v=y-d\) maps
\(1\leq d\leq y\) exactly to \(0\leq v<y\).  Even \(d=y-v\) vanish.
Set

\[
 p_y\in\{0,1\},\qquad p_y\equiv y-1\pmod2.
\tag{2.4}
\]

Every nonzero point is uniquely \(v=p_y+2n\), and on that lattice

\[
 \chi_4(y-v)=e\!\left(\frac{y-v-1}{4}\right).
\tag{2.5}
\]

Thus the complete physical phase is

\[
 \Psi_{\sigma,h}(v)
 =\sigma h\frac{q+v^2}{y-v}+\frac{y-v-1}{4}.
\tag{2.6}
\]

Define \(\mathcal C_N^\sigma\) by restricting (2.3) to
\(0\leq v\leq L_h\), including the literal integer endpoint, and define
\(\mathcal S_N^\sigma\) by \(L_h<v<y\).  These two owners are disjoint and
exhaust every literal sample, including even zero terms and profile-zero
samples.  Since the character and profile are real,
\(\mathcal F_N^-=\overline{\mathcal F_N^+}\), and similarly for the two
pieces.

The exact statement certified below is (1.2)--(1.3).  It is a scalar
support reduction.  It does not state that a filtered part of the
Round-138 square residual is small.

## 3. Proof or derivation

Put

\[
 g(v)=\frac{q+v^2}{y-v}=\frac{N}{y-v}-y-v.
\tag{3.1}
\]

The identity is exact, and

\[
 g'(v)=\frac{N}{(y-v)^2}-1,\qquad
 g''(v)=\frac{2N}{(y-v)^3}.
\tag{3.2}
\]

For \(v=p_y+2n\), let \(d_n=y-p_y-2n\) and
\(F_{\sigma,h}(n)=\Psi_{\sigma,h}(p_y+2n)\).  The carrier in (2.6) is
linear in \(n\), so it contributes zero second derivative.  The chain
rule gives the exact parity-lattice formula

\[
 F_{\sigma,h}''(n)
 =4\sigma h\,g''(p_y+2n)
 =\sigma\frac{8hN}{d_n^3}.
\tag{3.3}
\]

On the collar, \(L_h\leq\rho y\), hence

\[
 (1-\rho)y\leq d_n\leq y.
\tag{3.4}
\]

For \(y\geq2\),
\(y^2\leq N\leq y^2+2y\leq2y^2\), so

\[
 8\frac hy
 \leq |F_{\sigma,h}''(n)|
 \leq \frac{16}{(1-\rho)^3}\frac hy.
\tag{3.5}
\]

Thus the second derivative has constant sign, a ratio depending only on
\(\rho\), and scale \(\lambda\asymp_\rho h/y\), uniformly in \(q\), \(p_y\),
and \(\sigma\).  By (2.2), \(\lambda\leq1\) once \(y\) exceeds a fixed
profile-dependent constant.  The remaining bounded range of real \(X\)
contains only \(O_{V_{\rm low}}(1)\) literal samples and is absorbed in
the implicit constant.

The elementary second-derivative estimate in the needed form is

\[
 \sup_{J\subset I}\left|\sum_{n\in J}e(f(n))\right|
 \ll_A M\sqrt\lambda+\lambda^{-1/2},
\tag{3.6}
\]

when \(I\) has \(M\) integer points,
\(\lambda\leq|f''|\leq A\lambda\), and \(f''\) has constant sign.  This is
the usual derivative-alias proof: \(f'\) is monotone, the neighborhoods
where \(f'\) approaches an integer have total cost
\(O(M\sqrt\lambda+\lambda^{-1/2})\), and the first-derivative estimate
controls their complement.  Abel summation multiplies the right side by
\(\|a\|_\infty+\sum|\Delta a|\).

For the literal amplitude, set

\[
 z_h(n)=\frac{4R^2h^2}{d_n^2},\qquad
 a_h(n)=V_{\rm low}(z_h(n)).
\tag{3.7}
\]

The sequence \(z_h(n)\) is monotone.  Consequently

\[
 \sum_n|a_h(n+1)-a_h(n)|
 \leq \operatorname{Var}_{[0,\infty)}(V_{\rm low})+O(\|V_{\rm low}\|_\infty)
 \ll_{V_{\rm low}}1.
\tag{3.8}
\]

The \(O(1)\) term safely owns the hard start, the artificial collar end,
and any literal zero-extension jump.  No smooth replacement of either
endpoint is made.

The number \(M_h\) of allowed parity points in the collar satisfies

\[
 M_h\leq\frac{L_h}{2}+1\ll 1+\frac{y}{\sqrt h}.
\tag{3.9}
\]

Applying (3.6)--(3.8) with \(\lambda\asymp h/y\) gives

\[
 \begin{aligned}
 \left|\sum_{\substack{0\leq v\leq L_h\\y-v\ {\rm odd}}}
 V_{\rm low}\!\left(\frac{4R^2h^2}{(y-v)^2}\right)
 e(\Psi_{\sigma,h}(v))\right|
 &\ll
 M_h\sqrt{\frac hy}+\sqrt{\frac yh} \\
 &\ll \sqrt y+\sqrt{\frac yh}.
 \end{aligned}
\tag{3.10}
\]

The \(+1\) in (3.9) is absorbed by the second term because active
\(h\ll\sqrt y\) outside the already absorbed finite range.  Equation
(3.10) is uniform in the physical carrier, both signs, and all \(q\).

Restoring the exact \(h^{-1}\) coefficient and using (2.2),

\[
 \begin{aligned}
 |\mathcal C_N^\sigma|
 &\ll
 \sum_{h\ll R}\frac1h
 \left(\sqrt y+\sqrt{\frac yh}\right)\\
 &\ll
 \sqrt y\log(2R)+\sqrt y\sum_{h\geq1}h^{-3/2}\\
 &\ll R\log(2X).
 \end{aligned}
\tag{3.11}
\]

This proves (1.2).  The literal partition then proves (1.3), and the
target for \(\mathcal F_N^\sigma\) is equivalent, after renaming
\(\varepsilon\), to the target for \(\mathcal S_N^\sigma\).

For the capacity ledger, fix \(h\asymp H\).  There are \(O(H)\) heights,
each has coefficient \(O(H^{-1})\), and the collar length is
\(O(yH^{-1/2})\).  Its dyadic weighted absolute capacity is therefore

\[
 yH^{-1/2}.
\tag{3.12}
\]

The signed curvature estimate on the same block is

\[
 R+RH^{-1/2}.
\tag{3.13}
\]

There are only \(O(\log X)\) dyadic height blocks, so (3.13) returns to
\(RX^\varepsilon\).

For the corrected generalized top collar
\(L_{\alpha,H}=\rho yH^{-\alpha}\), the same calculation gives

\[
 R H^{1/2-\alpha}+R H^{-1/2}.
\tag{3.14}
\]

At \(\alpha=1/2\), this is \(O(R)\) for every \(H\geq1\).  If
\(\alpha<1/2\), an active block \(H\asymp R\) makes the first term
\(R^{3/2-\alpha}\), a fixed power above \(R\).  Hence
\(\alpha=1/2\) is the maximal **certified power scale for this rowwise
second-derivative-plus-height-modulus ledger**.  It is not a lower bound
for the physical sum and does not exclude a new cross-height theorem.
At \(\alpha=0\), \(H\asymp R\), the ledger is \(R^{3/2}\), exactly the
accepted full-row half-integer-alias capacity.

## 4. First doubtful or unproved step

The first open estimate is still

\[
 |\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon.
\tag{4.1}
\]

The survivor has \(v>L_h\), retains every terminal profile crossing and
stationary alias, and has \(y^{1+o(1)}\) absolute scalar capacity.  On a
longer top collar the rowwise expression (3.14) exceeds \(R\); that means
the current method no longer certifies the target, not that the actual
signed sum is large.  A continuation needs cancellation across heights
and physical aliases, or a direct estimate of the exact Round-138
cross-denominator residual.

The first doubtful sentence in the candidate is only the literal
antecedent of (139.C15): \(L=yH^{-\alpha}\) must be replaced by (1.4), or
the discussion must be explicitly confined to \(d\asymp y\).  Without
that repair, \(H=1,\alpha=0\) reaches \(d=0\), outside both the scalar and
the bounded-curvature-ratio proof.  No displayed exponent or promoted
collar estimate changes after the repair.

There is no square-level consequence beyond logical target equivalence.
Writing \(\mathcal F_N=\mathcal C_N+\mathcal S_N\) gives

\[
 |\mathcal F_N|^2
 =|\mathcal S_N|^2+|\mathcal C_N|^2
  +2\Re(\mathcal C_N\overline{\mathcal S_N}).
\tag{4.2}
\]

The cross term is not \(O(yX^\varepsilon)\) before (4.1) is known.  In
reduced coordinates \(h=ag,d=bg\), the condition
\(y-bg\leq L_{ag}\) depends on the lift \(g\), so it splits the accepted
\(L_\chi(y/b)\) coefficient.  Thus no collar-filtered part of
\(\mathcal R_{y^{-2}}\) is deleted.

## 5. Required controls and post-unmask seam verdicts

| seam | verdict | hostile outcome |
|---|---|---|
| Exact \(N=y^2+q\), displacement bijection, and support | **GREEN** | Equations (2.1)--(2.3) retain \(0\leq q\leq2y\), \(d\leftrightarrow v\), floors, and the literal bound \(h\ll R\). |
| Parity-lattice derivatives | **GREEN** | The factor \(4\) from \(v=p_y+2n\) is present, giving exactly \(8\sigma hN/d^3\).  The mod-four carrier is linear and contributes no curvature. |
| Second-derivative lemma and parameter range | **GREEN** | On \(v\leq\rho y/\sqrt h\), \(d\asymp_\rho y\), \(\lambda\asymp h/y\), the curvature has fixed sign and bounded ratio.  Bounded \(X\) is absorbed separately. |
| Literal profile BV | **GREEN** | The profile argument is monotone; sampled variation is bounded by the fixed profile variation.  Hard, artificial, support-entry, and zero-extension jumps cost \(O(1)\). |
| Weighted \(h\)-sum and dyadic capacity | **GREEN** | The \(h^{-1}\) weight is retained.  Equations (3.11)--(3.13) give \(R\log X\), not a raw-count transfer. |
| Small and terminal endpoints | **GREEN** | The collar includes its floor endpoint; parity-inadmissible terms remain literal zeros.  Every \(L_h<v<y\) point, including profile-zero terminal samples, belongs to the survivor. |
| Both signs and both \(y\)-parities | **GREEN** | The curvature changes sign with \(\sigma\) but not magnitude.  The negative scalar is the conjugate; \(p_y=0,1\) covers both parities without averaging. |
| \(q=0\), \(q=2y\), fourth powers, and real-centre uniformity | **GREEN** | Only \(y^2\leq N\leq y^2+2y\) enters (3.5).  The proof is uniform over every floor interval; fourth powers are included. |
| Asserted maximal rowwise power scale | **REVISE** | Insert the fixed \(\rho\) in \(L_{\alpha,H}\), or state \(d\asymp y\).  After this scope repair, (139.C15) and the threshold \(\alpha=1/2\) are GREEN.  The threshold is method-specific, not an optimality theorem. |
| Noninvertibility of the promoted collar estimate | **GREEN** | The second-derivative inequality genuinely bounds the exact unsquared collar.  It is not Fourier inversion, a principal-only replacement, or an aliaswise modulus on the tail. |
| Logical map to the Round-138 residual | **GREEN** | From (1.3) and the accepted Round-138 identity, the three target bounds are equivalent after epsilon renaming.  Equation (4.2) correctly forbids a square-level deletion. |
| Supersession of the blind/hostile perturbative restriction | **GREEN, SCOPED** | The exact-phase collar is larger than the bounded-correction Taylor window and therefore supplies the strict scalar reduction those reports did not find.  It does not refute their statements about Taylor-core BV completion. |
| Full Gauss/Salié/Poisson completion obstruction | **GREEN** | The exact correction still has \(\gg y\) discrete variation on the fourth-power control interval; complete Gauss correlation is invertible, there is no Salié unit sum, and full aliaswise capacity remains \(R^{3/2}\). |
| Downstream scope | **GREEN** | The tail estimate, lower signed estimate, lower GAR, both direct M1 parents, M9-M1, all M2 parents, endpoint uniformity, M9, the quarter theorem, and the exponent remain open. |

To make the supersession quantitative, let

\[
 \ell_h\asymp\left(\frac{y^2}{h}\right)^{1/3}
\tag{5.1}
\]

be the legal Taylor-correction window.  Since \(h\ll\sqrt y\),

\[
 \frac{L_h}{\ell_h}
 \asymp \rho\,y^{1/3}h^{-1/6}
 \gg_\rho y^{1/4}\asymp R^{1/2}.
\tag{5.2}
\]

Thus the new collar is genuinely larger.  On it the correction is not
perturbative: at \(q=0\), \(v\asymp y/\sqrt h\),

\[
 E_{h,0,y}(v)
 =\frac{hv^3}{y(y-v)}
 \asymp \frac{y}{\sqrt h}.
\tag{5.3}
\]

The success of (1.2) therefore comes from retaining the complete exact
phase in (3.3), not from silently extending the Taylor-core argument.

Conversely, the full-completion obstruction survives.  At
\(X=N=M^4\), \(h=1\), write \(v=ty\).  On a fixed interval
\(I\Subset(0,1)\), the profile is on its near-zero plateau and

\[
 E_{1,0,y}(v)=y\frac{t^3}{1-t}.
\tag{5.4}
\]

Choosing \(I\) with
\(1/20\leq (t^3/(1-t))'\leq1/12\) makes each allowed parity increment
\(E(v+2)-E(v)\) lie between \(1/10\) and \(1/6\).  There are
\(\asymp y\) such samples, so

\[
 \operatorname{Var}_{v\equiv p_y\ (2)} e(E_{1,0,y}(v))\gg y.
\tag{5.5}
\]

Hence the exact correction is still not a bounded-variation coefficient
on the full range.  Retaining all Fourier modes gives an invertible
completion; taking coefficient-blind or aliaswise moduli gives \(y\) or
\(R^{3/2}\), not \(R\).  This conclusion is analytic and does not rely on
agreement among reports.

Finally, the logical residual map is exactly

\[
 \begin{aligned}
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 &\Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon\\
 &\Longleftrightarrow
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon,
 \end{aligned}
\tag{5.6}
\]

using (1.3) and the accepted Round-138 relation.  It is not the false
identity
\(|\mathcal S_N|^2=\mathcal R_{y^{-2}}+O(yX^\varepsilon)\).

## 6. Dependencies and exact artifacts used

The post-unmask audit used:

- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/literal_displacement_quadratic_scalar_attack.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/blind_displacement_scalar_feasibility.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/displacement_completion_hostile_audit.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/hostile_post_unmask_owner_and_capacity_audit.md;
- state/active_campaign.yml and the relevant accepted nodes of state/proof_obligations.yml;
- protocol.md and strategy/conductor_0823_full_proof_strategy.md.

No numerical or symbolic experiment, web theorem, centre average,
arbitrary coefficient estimate, or vote was used.  Every calculation in
Sections 2--5 was recomputed from the displayed scalar and the elementary
second-derivative lemma.

## 7. Recommended state effect

After repairing the antecedent of (139.C15) as in (1.4), promote the exact
scalar collar reduction (139.C1)--(139.C14):

\[
 \mathcal F_N^\pm=\mathcal S_N^\pm+O(R\log(2X)).
\]

Record the \(\alpha=1/2\) statement only as the maximal power scale
certified by the fixed-\(\rho\), rowwise second-derivative ledger.  Promote
no claim that it is an arithmetic lower bound or the limit of every
possible signed displacement method.

Retain the Taylor window, the full correction-variation example, the
ordinary-Gauss-not-Salié classification, exact Fourier self-return, and
the \(R^{3/2}\) full-alias capacity as compatible obstruction controls.
The curvature collar supersedes only the earlier conclusion that no
strict scalar contraction had been obtained; it leaves their
full-completion no-go intact.

Attach the survivor to the accepted Round-138 residual only through the
logical equivalence (5.6).  Do not delete a residual sub-square or a
collar--tail cross term.  Retain (4.1), the full lower signed estimate,
lower GAR, both direct M1 parents, M9-M1, every M2 parent, endpoint
uniformity, M9, the conditional quarter theorem, and the target as open.
