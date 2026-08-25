# Round 139 discovery report: literal displacement quadratic scalar attack

## 1. Result

**Outcome: `strict_displacement_quadratic_reduction`.**  There is a fixed
\(0<\rho<1/8\), depending at most on the fixed literal profile, for which the
physical top-displacement collar

\[
 L_h=\left\lfloor {\rho y\over \sqrt h}\right\rfloor,
 \qquad 0\le v\le L_h,
\tag{139.1}
\]

is target-safe with the exact phase, exact mod-four carrier, literal profile,
and both signs:

\[
 \mathcal C_N^\pm
 :=\sum_{h\ge1}{1\over h}
 \sum_{0\le v\le L_h}
 \chi _4(y-v)V_{\rm low}\!\left({4R^2h^2\over (y-v)^2}\right)
 e\!\left(\pm h{q+v^2\over y-v}\right),
 \qquad
 |\mathcal C_N^\pm|\ll R\log(2X).
\tag{139.2}
\]

Consequently, with the literal complementary owner

\[
 \mathcal S_N^\pm
 :=\sum_{h\ge1}{1\over h}
 \sum_{L_h<v<y}
 \chi _4(y-v)V_{\rm low}\!\left({4R^2h^2\over (y-v)^2}\right)
 e\!\left(\pm h{q+v^2\over y-v}\right),
\tag{139.3}
\]

one has the exact, owner-complete reduction

\[
 \boxed{\mathcal F_N^\pm=\mathcal S_N^\pm+O(R\log(2X))}.
\tag{139.4}
\]

Thus the \(RX^\varepsilon\) target for \(\mathcal F_N^\pm\) is equivalent,
after the usual epsilon renaming, to that target for \(\mathcal S_N^\pm\).
The survivor is strictly smaller in literal \((h,v)\)-support, but its
absolute capacity is still \(y^{1+o(1)}=R^{2+o(1)}\); the target bound is not
proved.

The proof is genuinely noninvertible on the deleted collar: it applies the
second-derivative inequality to the **complete exact displacement phase**, not
to a principal stationary term and not after taking a modulus of each
stationary tube.  The maximal rowwise collar scale in this ledger is
\(y/\sqrt h\).  Extending a rowwise quadratic/alias modulus to a collar
\(y h^{-\alpha}\) with \(\alpha<1/2\) already costs
\(R h^{1/2-\alpha}\) in one height row; at \(h\asymp R\) this is a power above
\(R\).  Exact finite completion of the Taylor core supplies ordinary
quadratic Gauss sums, not Salié sums, and is an invertible Fourier rewrite
unless new cancellation in the exact Taylor-correction coefficients is
proved.

## 2. Exact statement and hypotheses

Let \(X\ge2\) be real and

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,
 \qquad 0\le q\le2y.
\tag{139.5}
\]

The map \(d\mapsto v=y-d\) is a bijection from \(1\le d\le y\) to
\(0\le v<y\), in both directions.  The inherited literal support says that
there is a fixed \(C_V\) such that a nonzero profile sample forces

\[
 h\le C_V{y-v\over R}\le C_V{y\over R}\ll_V R.
\tag{139.6}
\]

The fixed smooth profile and its zero extension have uniformly bounded
supremum and variation on every monotone sample interval used below.  These
are precisely the inherited profile hypotheses; no new cutoff or extension
is introduced.

For the positive sign,

\[
 {N\over y-v}=y+v+{q+v^2\over y-v}
\tag{139.7}
\]

is exact, and \(h(y+v)\in\mathbb Z\).  If \(y-v\) is even, the term is zero.
If it is odd, then

\[
 \chi _4(y-v)=e\!\left({y-v-1\over4}\right),
 \qquad
 \Psi_{h,q,y}(v)=h{q+v^2\over y-v}+{y-v-1\over4}.
\tag{139.8}
\]

Writing \(p_y\in\{0,1\}\) for \(p_y\equiv y-1\pmod2\), every surviving
point is uniquely \(v=p_y+2n\).  Thus both parities of \(y\) are retained,
rather than replaced by an all-integer model.  The negative scalar is the
complex conjugate of the positive scalar, since the profile and \(\chi _4\)
are real.

The exact Taylor identity is

\[
 {q+v^2\over y-v}={q\over y}+{v^2\over y}
   +{v(q+v^2)\over y(y-v)},
 \qquad
 \mathcal E_{h,q,y}(v):=h{v(q+v^2)\over y(y-v)}.
\tag{139.9}
\]

Accordingly, the physical quadratic core is

\[
 {hq\over y}+{hv^2\over y}-{v\over4}+{y-1\over4},
\tag{139.10}
\]

and (139.9), with no truncation, is its correction.  Equations
(139.1)--(139.4) assign the hard collar endpoint to \(\mathcal C_N^\pm\), all
remaining points (including the terminal zero-extended range) to
\(\mathcal S_N^\pm\), and leave no boundary owner unassigned.

## 3. Proof or derivation

Put

\[
 g(v)={q+v^2\over y-v}={N\over y-v}-y-v.
\tag{139.11}
\]

This gives the exact derivatives

\[
 g'(v)={N\over(y-v)^2}-1,
 \qquad
 g''(v)={2N\over(y-v)^3}.
\tag{139.12}
\]

On the collar (139.1), \(y-v\ge(1-\rho)y\).  Since
\(y^2\le N\le y^2+2y\), the phase on the actual parity progression satisfies

\[
 {d^2\over dn^2}\Psi_{h,q,y}(p_y+2n)
 ={8hN\over(y-p_y-2n)^3}\asymp_\rho {h\over y},
\tag{139.13}
\]

with constant sign and monotone second derivative, uniformly in
\(0\le q\le2y\) and both parities.  For the negative sign the second
derivative has the opposite sign and the same magnitude.

We use the elementary second-derivative inequality in its precise needed
form: if \(f\in C^2(I)\), \(f''\) has constant sign and
\(\lambda\le |f''|\le A\lambda\) on an integer interval of length \(M\),
with \(0<\lambda\le1\), then

\[
 \sup_{J\subset I}\left|\sum_{n\in J}e(f(n))\right|
 \ll_A M\sqrt\lambda+\lambda^{-1/2}.
\tag{139.14}
\]

This follows by separating the \(O(1+M\lambda)\) integer derivative aliases
and applying the first-derivative bound outside a
\(\lambda^{-1/2}\)-neighbourhood of each alias.  Abel summation gives the
same bound after multiplication by an amplitude whose supremum plus total
variation is \(O(1)\).  Here the amplitude

\[
 V_{\rm low}\!\left({4R^2h^2\over(y-p_y-2n)^2}\right)
\tag{139.15}
\]

has that property: its argument is monotone, remains in a fixed compact
profile range whenever it is nonzero, and the hard collar and literal zero
extensions add only endpoint jumps.  For bounded \(X\), the assertion is
absorbed directly into the implicit constant; otherwise (139.6) makes
\(h/y<1\).

The number of allowed parity points is
\(M_h\leq1+L_h/2\).  Taking \(M=M_h\) and
\(\lambda\asymp h/y\) in (139.14) yields, for each active height,

\[
 \left|\sum_{0\le v\le L_h}\chi _4(y-v)V_{\rm low}(\cdots)
 e\!\left(\pm h{q+v^2\over y-v}\right)\right|
 \ll (1+L_h)\sqrt{h/y}+\sqrt{y/h}
 \ll \sqrt y+\sqrt{y/h}+\sqrt{h/y}
 \ll \sqrt y+\sqrt{y/h}.
\tag{139.16}
\]

Using \(h\ll R\) and \(\sqrt y\asymp R\),

\[
 |\mathcal C_N^\pm|
 \ll\sum_{h\ll R}{1\over h}
 \left(\sqrt y+\sqrt{y/h}\right)
 \ll R\log(2X),
\tag{139.17}
\]

which proves (139.2)--(139.4).

The complete power ledger is as follows.  Here \(h\asymp H\),
\(d=y-v\asymp D\), and literal support imposes \(H\ll D/R\).

| literal owner | weighted absolute capacity on one dyadic height block | lawful quadratic/curvature ledger |
|---|---:|---:|
| Taylor-perturbative collar \(v\ll \ell_H:=(y^2/H)^{1/3}=R^{4/3}H^{-1/3}\) | \(R^{4/3}H^{-1/3}\) | \(R H^{-1/2}+R^{1/3}H^{1/6}\ll R\) |
| proved collar \(v\le L_H\asymp yH^{-1/2}=R^2H^{-1/2}\) | \(R^2H^{-1/2}\) | \(R+R H^{-1/2}\ll R\) |
| an entire top row of length \(\asymp y\) | \(R^2\) | \(R\sqrt H+R/\sqrt H\), which is \(R^{3/2}\) at \(H=R\) |
| survivor on \(d\asymp D\), \(H\ll D/R\) | \(D\) | no estimate below this capacity is proved |

There are only \(O(\log X)\) height blocks, so the proved-collar line returns
to \(R X^\varepsilon\).  Summing the last line absolutely over \((D,H)\)
returns \(yX^\varepsilon=R^{2+o(1)}\), not the target.

The Taylor correction is not hidden in (139.13).  It is nondecreasing, and
on the smaller collar \(v\le\ell_h\) one has, uniformly in \(q\),

\[
 \mathcal E_{h,q,y}(v)
 \ll {hv\over y}+{hv^3\over y^2}\ll1.
\tag{139.18}
\]

Its total variation there is \(O(1)\), so Abel summation against the pure
quadratic core lawfully gives the first line of the table.  On the larger
proved collar, however, already at \(q=0\) and
\(v\asymp y/\sqrt h\),

\[
 \mathcal E_{h,0,y}(v)\asymp {y\over\sqrt h}.
\tag{139.19}
\]

For example, at fourth-power centres and \(h=1\), the literal profile is on
its near-zero plateau throughout a fixed \(v\le\rho y\) collar, while the
continuous variation of \(e(\mathcal E)\) is \(\asymp y\).  Therefore a
quadratic-core Abel argument has a polynomial, not \(O(1)\), correction
price.  Estimate (139.17) succeeds only because it keeps the exact phase
(139.11).

For completeness, the exact finite quadratic completion also exposes why
the word Salié is unavailable.  Put \(M=4y\),
\(P_y(v)=\mathbf 1_{v\equiv y-1\ (2)}\), and

\[
 K_{h,y}(v)=P_y(v)e\!\left({4hv^2-yv\over4y}\right)
 \quad(v\bmod M).
\tag{139.20}
\]

Its Fourier coefficient is

\[
 \begin{aligned}
 G_{h,y}(m)
 &=\sum_{v\bmod M}K_{h,y}(v)e(mv/M)\\
 &=\frac12G(4h,m-y;4y)
 +\frac{(-1)^{y-1}}2G(4h,m-y+2y;4y),
 \end{aligned}
\tag{139.21}
\]

where \(G(a,b;c)=\sum_{v\bmod c}e((av^2+bv)/c)\) is an ordinary quadratic
Gauss sum.  If \(g=(h,y)\), then \((4h,4y)=4g\); each term in (139.21)
vanishes unless \(4g\) divides its linear coefficient and otherwise obeys

\[
 |G(4h,b;4y)|\le \sqrt{2(4y)(4g)}=4\sqrt{2yg}.
\tag{139.22}
\]

This records every gcd and both parity cases.  The mod-four character has
become an additive parity projector and linear shift; no variable
multiplicative character or inverse phase remains, hence there is no Salié
sum.

If \(A_h(v)\) is the exact profile, hard collar, zero extension, and
\(e(\mathcal E_{h,q,y}(v))\), extended by zero to \(\mathbb Z/M\mathbb Z\),
then completion is the exact identity

\[
 \sum_{v\bmod M}A_h(v)K_{h,y}(v)
 ={1\over M}\sum_{m\bmod M}\widehat A_h(m)G_{h,y}(m).
\tag{139.23}
\]

It is invertible Fourier completion.  Parseval gives

\[
 \sum_m|\widehat A_h(m)|^2=M\sum_v|A_h(v)|^2\ll ML_h,
 \qquad
 \sum_m|G_{h,y}(m)|^2=M\sum_v|K_{h,y}(v)|^2={M^2\over2}.
\tag{139.24}
\]

Thus coefficient-blind Cauchy in (139.23) gives only
\(O(\sqrt{yL_h})=O(yh^{-1/4})\), no gain even over the trivial collar bound
when \(h>1\).  Using the pointwise Gauss bound instead requires control of
the Fourier \(\ell^1\)-mass of the exact correction; (139.19) is the first
BV obstruction.  Any improvement there would be a new signed estimate for
the correction coefficients, not a free Gauss factor.

Finally, on the parity progression the derivative in (139.13) changes by
\(\asymp\sqrt h\) across the proved collar.  Hence there are
\(O(1+\sqrt h)\) integer Poisson aliases, equivalently half-integer aliases
in the physical \(v\)-derivative.  Each has quadratic width
\(\asymp\sqrt{y/h}\), and their complete rowwise capacity is

\[
 \sqrt h\sqrt{y/h}=\sqrt y\asymp R.
\tag{139.25}
\]

For a longer fixed-top collar \(L=\rho yh^{-\alpha}\), with the same
\(0<\rho<1/8\) so that \(y-v\asymp_\rho y\), the same lawful rowwise
alias ledger is \(R h^{1/2-\alpha}+R h^{-1/2}\), up to a
\(\rho\)-dependent constant.  Therefore \(\alpha=1/2\) is the last
power scale that returns to \(R\) under a rowwise modulus.  At full top-row
length and \(h\asymp R\), (139.25) becomes \(R^{3/2}\), agreeing with the
known half-integer-tube capacity rather than contradicting it.

Round 138 gives

\[
 |\mathcal F_N|^2=\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).
\tag{139.26}
\]

Together, (139.4) and (139.26) imply the exact chain of target-scale
equivalences

\[
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.
\tag{139.27}
\]

This is a logical map to the accepted residual, not a false claim that the
square-level near/far cross terms may be deleted separately.

## 4. First doubtful or unproved step

The first unproved step is

\[
 \boxed{|\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon.}
\tag{139.28}
\]

On \(v>L_h\), a rowwise second-derivative or stationary-alias modulus has
already exhausted the \(R\) budget.  Covering a full \(d\asymp y\) row at
\(h\asymp R\) costs \(R^{3/2}\).  Completing only the rational quadratic
core is not a repair: the exact correction has polynomial variation, its
Fourier coefficients remain the complete unresolved data, and the exact
Gauss transform (139.23) is invertible.  The terminal ranges \(v\to y\)
also have rapidly varying curvature and moving literal support; they are
retained untouched in (139.3).

A continuation would have to prove joint signed cancellation across
physical half-integer aliases and heights, or directly estimate the exact
Round-138 cross-denominator residual.  No such inequality is derived here.
The calculation is therefore not a universal impossibility theorem for all
displacement methods; it is a rigorous capacity and self-return obstruction
to extending the present rowwise quadratic/Gauss mechanism.

## 5. Required controls and outcomes

| required control | outcome |
|---|---|
| `exact_N_y2_q_and_displacement_bijection` | Pass: (139.5), (139.7), and the bijection \(d\leftrightarrow v\) are exact in both directions. |
| `literal_profile_support_zero_extension_and_both_signs` | Pass: (139.6) is the literal support; (139.2)--(139.3) partition every sample and endpoint, and the negative sign is conjugate. |
| `physical_mod_four_carrier_and_y_parity` | Pass: (139.8) and \(v=p_y+2n\) retain the carrier for both parities; even denominators remain zero. |
| `exact_quadratic_core_and_Taylor_correction` | Pass: (139.9)--(139.10), the legal subcollar (139.18), and the nonperturbative size (139.19) price the correction without dropping it. |
| `small_v_and_terminal_v_boundaries` | Pass: the small/top collar is proved target-safe; the hard boundary belongs to it, and every terminal point belongs literally to the survivor, including profile-zero samples. |
| `dyadic_h_v_capacity_ledger` | Pass: the four-line table gives absolute capacity, returned \(R\)-power, the \(R^{3/2}\) overrun, and the survivor's \(R^2\) capacity. |
| `quadratic_Gauss_Salie_completion_cost` | Pass: (139.20)--(139.24) give modulus \(4y\), gcd \(4(h,y)\), support conditions, Gauss size, completion and Parseval costs.  The complete sums are Gauss, not Salié. |
| `stationary_alias_and_half_integer_tubes` | Pass: (139.25) counts all physical half-integer aliases.  No aliaswise modulus is taken beyond its target-safe collar, and the known \(R^{3/2}\) capacity is reproduced at full length. |
| `q_zero_q_max_and_real_centre_uniformity` | Pass: (139.13) uses only \(y^2\le N\le y^2+2y\), hence is uniform for \(q=0\), \(q=2y\), and every real \(X\).  Fourth powers also furnish the literal correction-BV control. |
| `map_back_to_round138_exact_residual` | Pass: (139.27) maps the survivor to the exact accepted residual by target equivalence, without deleting square-level cross terms. |
| `noninvertibility_directionality_and_self_return` | Pass: (139.17) is a noninvertible estimate for the literal collar only.  Equation (139.23) identifies exact completion as an invertible self-return; no block modulus, arbitrary array, or centre average replaces the scalar. |
| `lower_GAR_and_downstream_scope` | Pass: only the scalar support is reduced.  The survivor, lower signed estimate, lower GAR, both direct M1 parents, M9-M1, all M2 parents, endpoint uniformity, M9, the quarter bridge, and the exponent remain open. |

No numerical, symbolic, or probabilistic experiment was used.

## 6. Dependencies and exact artifacts used

The derivation used only the assigned brief and its permitted context:

- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/briefs/literal_displacement_quadratic_scalar_attack.md`;
- `protocol.md`;
- `state/proof_obligations.yml`, specifically the active lower-radial owner, the Round-121 flat/displacement and half-integer obstructions, and the two accepted Round-138 Farey nodes;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/conductor_round138_signed_farey_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md`.

The only general analytic input is the explicitly stated elementary
second-derivative inequality (139.14), with its parameter range and alias
proof indicated.  The Gauss facts in (139.21)--(139.22) follow directly by
the parity projector, gcd reduction, and squaring the reduced quadratic
sum.  No external source or unlisted round artifact is used.  The work was
100% analytic.

## 7. Recommended state effect

**Promote only the scoped reduction after independent seam review:** record
(139.2)--(139.4) as a target-safe deletion of the exact physical collar
\(v\le\rho y/\sqrt h\), and record (139.18)--(139.25) as its exact Taylor,
Gauss-completion, half-integer-alias, and maximal rowwise-capacity ledger.
Attach it to the open lower signed scalar and to the accepted Round-138
residual through (139.27).

Retain (139.28) as open.  Make no promotion of the complete lower-radial
signed estimate, lower GAR, either direct blockwise M1 owner, M9-M1, any M2
owner, endpoint uniformity, M9, the conditional quarter theorem, or the
global exponent.  No shared proof state is edited by this report.
