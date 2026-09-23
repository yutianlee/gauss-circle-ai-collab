# Round 167 statement-only determinant-interface rederivation

- Campaign: m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate
- Task: blind_determinant_interface_rederivation
- Role: statement-only blind rederiver
- Status: candidate evidence only; no proof-state mutation is licensed

## 1. Result

### 1.1 Exact dictionary lemma

The literal opened incidence family in (167.B1) has a multiplicity-one variable-determinant parameterization. Put

\[
k=2^{\nu_2(r)},\qquad r=kh,\qquad h\ \mathrm{odd},
\]

and, for every opened tuple, put

\[
g=(d,d'),\qquad d=gu,\qquad d'=gv,\qquad (u,v)=1.
\]

Because \(d,d'\) are odd, \(g,u,v\) are odd. Since \(g\mid r\), necessarily \(g\mid h\); writing \(h=g\ell\) gives

\[
vm'-um=k\ell.
\tag{167.R1}
\]

Choose the canonical solution \(m_0\in\{0,\ldots,v-1\}\) of

\[
um_0\equiv-k\ell\pmod v,
\]

and put \(m'_0=(k\ell+um_0)/v\). Then every solution of (167.R1), and no other one, is

\[
m=m_0+vt,\qquad m'=m'_0+ut,
\qquad t\in\mathbb Z.
\tag{167.R2}
\]

The literal support, squarefree conditions, selector, profiles, hard values, endpoints, zero extension, and opposing-displacement inequality merely select the allowed set of \(t\)'s; they do not change multiplicity. In these variables

\[
N(t)=A+Kt,\qquad N(t)+r=A+r+Kt,
\]

where

\[
A=gu m_0,\qquad K=guv={dd'\over g},
\tag{167.R3}
\]

and

\[
\chi_4(d')\chi_4(d)=\chi_4(uv).
\tag{167.R4}
\]

Thus the two-adic split, divisor-gcd split, determinant equation, and fixed row character are exactly compatible and cost no multiplicity.

### 1.2 Scoped interface and power no-go

The packet does **not** license a variable-determinant transform proving (167.B1). The first exact failure is the absence of a representation and norm bound for the literal joint selector multiplier after the multiplicity-one opening. Boundedness of that multiplier does not place it in any stated transform class, and no modulus, orbit/correlation norm, main term, error, cell count, boundary term, or completion loss is given. Consequently there is no theorem-shaped inequality to apply or restore to the \(L^2X^\varepsilon\) scale.

There is a second, quantitative no-go for a common attempted interface. If the square-root phase is absorbed into a smooth amplitude and the transform loses an uncompensated fixed positive power \(\delta^{-A}\), \(A>0\), then the packet's necessary scale

\[
\delta^{-1}\gtrsim 1+{Jr\over L}
\tag{167.R5}
\]

produces a fixed positive power of \(X\), not an \(X^\varepsilon\) loss. Such an amplitude-smoothing implementation cannot prove (167.B1). A viable theorem would have to treat the square-root factor as genuine oscillation, preserve the selector and the single outer real part across variable \(r\), and produce enough compensating decay to pay every restored term. No such estimate is contained in the statement packet.

This is a scoped no-go, not a no-go for every possible determinant or spectral method. It leaves open a bespoke selector-aware, native-oscillatory variable-determinant theorem.

## 2. Exact statement and hypotheses

Assume exactly the statement packet:

\[
J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},
\qquad R_0=\lceil L\rceil,\qquad 0<\gamma<1,
\]

and

\[
c_N^{\rm rem}
=\sum_{\substack{d\mid N\\2\nmid d}}
\chi_4(d)\lambda_N^{\rm rem}(d),
\qquad
\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon.
\]

The support is a fixed-relative squarefree shell \(N\asymp L^2\), with \(d,m=N/d\asymp L\). The multiplier \(\lambda_N^{\rm rem}(d)\) is bounded and normalized but retains the literal joint selector, squarefree row, both parity branches, profiles, hard point values, endpoints, and zero extension.

After opening both endpoint divisor sums, define the literal incidence weight

\[
\begin{aligned}
W(d,m;d',m')={}&
\mathbf{1}_{\rm lit}\,
\mathbf{1}_{(d'-d)(m'-m)<0}\,
\mathbf{1}_{(d,d')<\gamma L}\,
\lambda_{d'm'}^{\rm rem}(d')
\overline{\lambda_{dm}^{\rm rem}(d)},
\end{aligned}
\tag{167.R6}
\]

where \(\mathbf{1}_{\rm lit}\) retains every literal shell, squarefree, parity, profile, hard-point, endpoint, and zero-extension convention. The conjugation is retained even though the final \(c_N^{\rm rem}\) is real.

The exact target is

\[
\boxed{
\Re\sum_{\substack{1\le r<R_0\\2\mid r}}
\left(1-{r\over R_0}\right)
\sum_{\substack{d,m,d',m'>0\\d'm'-dm=r}}
\chi_4(d')\chi_4(d)
W(d,m;d',m')
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right)
\ll_{\gamma,\varepsilon}L^2X^\varepsilon .}
\tag{167.R7}
\]

Every incidence is ordered: \((d,m)\) is the \(N\) endpoint and \((d',m')\) is the \(N+r\) endpoint. No quotient by matrix symmetry is permitted. The determinant dictionary is therefore

\[
\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
\qquad
\det\begin{pmatrix}d'&d\\m&m'\end{pmatrix}
=d'm'-dm=r,
\tag{167.R8}
\]

with multiplicity exactly one.

The positive opened-incidence capacity \(L^3X^\varepsilon\) and the target \(L^2X^\varepsilon\) are assumed exactly as stated. Hence a proof must gain a complete factor \(L\) through signed cancellation; parity, gcd bookkeeping, and reparameterization alone are not a gain.

## 3. Proof or derivation

### 3.1 Multiplicity-one determinant opening

An original summand is specified by \(r,N,d,d'\), with \(d\mid N\), \(d'\mid N+r\), and all literal conditions. Set \(m=N/d\) and \(m'=(N+r)/d'\). This produces one ordered positive matrix (167.R8). Conversely, any ordered positive matrix satisfying the literal conditions gives the unique data

\[
N=dm,\qquad r=d'm'-dm,\qquad d\mid N,\qquad d'\mid N+r.
\]

These maps are inverse. Thus opening both divisor sums and replacing incidences by determinant matrices is a bijection; there is no divisor, orbit, transpose, sign, or projective multiplicity to discard.

There is also a multiplicity-one displacement description. Put

\[
a=d'-d,\qquad b=m'-m.
\]

Then

\[
r=db+am+ab=db+am',
\tag{167.R9}
\]

and the opposing sector is exactly \(ab<0\). Since \(d,d'\) are odd, \(a\) is even. Since \(r\) is even, (167.R9) modulo \(2\) gives \(b\equiv r\equiv0\pmod2\). Thus both tangent displacements are even, but this parity fact provides only a structural restriction, not a power saving.

### 3.2 Gcd, two-adic, character, and row dictionary

The divisor gcd \(g=(d,d')\) is odd and unique. Writing \(d=gu,d'=gv\) gives \((u,v)=1\) and

\[
r=g(vm'-um).
\]

Hence \(g\mid r\). The factorization

\[
r=kh,\qquad k=2^{\nu_2(r)},\qquad h\ \mathrm{odd}
\]

is unique. Because \(g\) is odd, \(g\mid h\), and \(h=g\ell\) with \(\ell\) odd is also unique. This proves (167.R1).

As \((u,v)=1\), the congruence \(um_0\equiv-k\ell\pmod v\) has one solution modulo \(v\). The selected representative and (167.R2) give all integer solutions. From an opened tuple, \(t=(m-m_0)/v\) is unique; conversely, every integer \(t\) gives a determinant-\(r\) solution. Literal support and positivity delete values of \(t\) without duplicating the others. This proves the claimed row multiplicity.

Since \(g,u,v\) are odd and \(\chi_4(g)^2=1\),

\[
\chi_4(d')\chi_4(d)
=\chi_4(gv)\chi_4(gu)
=\chi_4(uv),
\]

which is fixed along the \(t\)-row. In particular, the even-determinant condition does not create character alternation along that row.

With \(x_t=A+Kt\), formulas (167.R3) give \(N=x_t\) and \(N+r=x_t+r\). The opposing condition becomes

\[
g(v-u)\{m'_0-m_0+(u-v)t\}<0.
\tag{167.R10}
\]

Thus it cuts the literal \(t\)-range but does not alter the determinant identity or multiplicity.

Substitution into (167.R7) yields the exact variable-determinant row form

\[
\begin{aligned}
\Re\sum_{\substack{k=2^\nu,\ \nu\ge1}}
\sum_{\substack{h\ \mathrm{odd}\\kh<R_0}}
\left(1-{kh\over R_0}\right)
\sum_{\substack{g\mid h\\g<\gamma L}}
\sum_{\substack{u,v\ \mathrm{odd}\\ (u,v)=1}}
\sum_{t\in\mathcal T(k,h,g,u,v)}
&\chi_4(uv)\,
W_{k,h,g,u,v}(t)\\
&\times e\!\left(J(\sqrt{x_t+kh}-\sqrt{x_t})\right),
\end{aligned}
\tag{167.R11}
\]

where \(\mathcal T\) and \(W_{k,h,g,u,v}\) retain all literal restrictions and endpoint weights from (167.R6), and \(x_t=A+Kt\). The outer real part remains outside every sum. The factorization \(r=kh\), the divisor \(g\mid h\), and the canonical row solution are all unique, so (167.R11) has multiplicity one.

On literal support \(gu,gv,m,m'\asymp L\), hence

\[
K=guv={dd'\over g}\asymp {L^2\over g}.
\tag{167.R12}
\]

The interval \(m\asymp L\) and step \(v\asymp L/g\) give \(O(1+g)\) possible row parameters \(t\). This is only a size ledger; taking absolute values over the rows would return to a positive estimate and is not a proof of (167.B1).

### 3.3 Phase scale and restored-power obstruction

For fixed \(r,A,K\), let

\[
\Phi(t)=J(\sqrt{x_t+r}-\sqrt{x_t}),
\qquad x_t=A+Kt.
\]

Rationalizing gives

\[
\Phi(t)={Jr\over\sqrt{x_t+r}+\sqrt{x_t}},
\tag{167.R13}
\]

and differentiation gives

\[
\Phi'(t)
={JK\over2}\{(x_t+r)^{-1/2}-x_t^{-1/2}\}
=-{JKr\over
2\sqrt{x_t}\sqrt{x_t+r}(\sqrt{x_t}+\sqrt{x_t+r})}.
\tag{167.R14}
\]

Since \(x_t,x_t+r\asymp L^2\) and \(K\asymp L^2/g\),

\[
|\Phi'(t)|\asymp {Jr\over gL}.
\tag{167.R15}
\]

A row has \(t\)-length \(O(g)\), so in a normalized row variable its phase-variation scale is

\[
1+{Jr\over L}.
\tag{167.R16}
\]

This independently recovers the necessary smoothing condition (167.R5). It also shows why the phase cannot be declared a harmless smooth multiplier.

Suppose an attempted determinant theorem accepts the phase only after absorbing \(e(\Phi)\) into a smooth amplitude and its restored estimate contains an uncompensated factor \(\delta^{-A}\) for some fixed \(A>0\). For every nonempty shift stratum,

\[
\delta^{-A}\gtrsim (1+Jr/L)^A.
\]

Already \(r\ge2\) and \(L\ll H\le J^{1/2}\) imply

\[
{Jr\over L}\gg {J\over L}\gg J^{1/2},
\]

so

\[
\delta^{-A}\gg J^{A/2}=X^{A/4}.
\tag{167.R17}
\]

A fixed factor \(X^{A/4}\) is not absorbable in \(X^\varepsilon\) for arbitrary \(\varepsilon>0\). Therefore an \(L^2X^\varepsilon\) base estimate with this uncompensated smoothing loss is not target-safe. If a method claims compensating oscillatory decay, that decay, together with every main term and error, must be stated and proved before (167.R17) can be regarded as paid. This proves the scoped smooth-amplitude no-go.

### 3.4 Why the factor \(L\) is still missing

The exact positive capacity is \(L^3X^\varepsilon\). The changes of variables above are bijections, so they cannot alter that capacity. The target is \(L^2X^\varepsilon\); hence the row form (167.R11) still needs an \(L\)-fold signed gain.

A fixed-\(r\) estimate followed by triangle inequality cannot create this gain: it places a modulus inside the complete \(r\)-aggregate and returns the stated \(L^3X^\varepsilon\) positive ledger unless the fixed-\(r\) theorem itself supplies a total factor \(L\) after summation. No such uniform fixed-\(r\) estimate is in the packet. The unique two-adic split has only logarithmically many possible values, but bookkeeping over those strata is not cancellation over the \(\asymp L\) determinants.

The literal multiplier in (167.R11) depends jointly on both products and both chosen divisors:

\[
W_{k,h,g,u,v}(t)
=\mathbf{1}_{\rm lit,opp,low\text{-}g}\,
\lambda_{x_t+kh}^{\rm rem}(gv)
\overline{\lambda_{x_t}^{\rm rem}(gu)}.
\tag{167.R18}
\]

The packet provides boundedness but no separability, periodicity, transform formula, smoothness norm, correlation norm, or finite exact decomposition for (167.R18). A variable-determinant transform cannot discard this multiplier, replace it by its modulus, or smooth it without pricing the resulting cells and boundaries. Thus the first exact transform interface is missing before any main term or error can be evaluated.

## 4. First doubtful or unproved step

The first unproved step is an exact selector-interface lemma:

> Represent the literal multiplier (167.R18), with every hard value, endpoint, squarefree condition, parity branch, and zero extension, in the coefficient/test class of one variable-determinant oscillatory transform; prove exact multiplicity, preserve the single outer real part, and bound the sum of all representation norms, moduli, cells, and boundary terms by \(X^\varepsilon\).

No such class, representation, or norm estimate is present in the statement packet. Therefore the transform cannot yet be applied. This precedes the analytic question of whether its main term and error save \(L\).

If the selector-interface lemma were supplied, the next doubtful step would be native treatment of the phase. Absorbing it into a smooth amplitude with any uncompensated fixed polynomial seminorm loss fails by (167.R17). The transform would need to exploit that oscillation while retaining variable \(r\) and then prove that its principal term, correlation norms, errors, endpoints, and completion together are \(O(L^2X^\varepsilon)\).

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| literal_residual_selector_and_multiplicity | **PARTIAL/GATE OPEN.** The determinant and row maps are exact bijections, and (167.R18) retains the selector. No admissible representation or norm bound for that selector is supplied. |
| determinant_two_adic_gcd_character_dictionary | **PASS.** Equations (167.R1)--(167.R4) and (167.R11) give unique \(k,h,g,u,v,t\), with \(g\mid h\), and character \(\chi_4(uv)\) fixed along each row. |
| one_outer_real_part_and_variable_r_aggregate | **PASS algebraically / OPEN analytically.** Formula (167.R11) preserves the real part outside all determinants. No target-scale transform estimate is proved. |
| phase_aligned_filter_erased_control | **PASS as a rejection control only.** An arbitrary phase-aligned product-site array has no canonical \(d,d',m,m'\), selector, opposing-sector, or low-gcd labels and may also violate the stipulated reality of \(c_N^{\rm rem}\). It neither proves nor refutes (167.B1). Any argument that remains valid only after erasing those literal filters is rejected. No lifted literal-incidence adversary is claimed here. |
| fixed_shift_triangle_no_go | **PASS.** A modulus before the \(r\)-sum restores the stated \(L^3X^\varepsilon\) positive capacity and loses the required factor \(L\). |
| minimal_scale_power_ledger | **PASS.** Positive capacity \(L^3X^\varepsilon\), target \(L^2X^\varepsilon\), missing gain \(L\); all exact reparameterizations have multiplicity one and give no gain. |
| endpoint_and_real_centre | **OPEN.** Endpoints, hard values, and zero extension remain literally inside (167.R18), but no smoothing-cell or boundary ledger is supplied. No real-centre uniformity may be inferred. |
| statement_only_independence | **PASS.** Only the permitted packet and task brief were used; no source theorem or nonblind artifact was consulted. |
| downstream_scope_and_no_exponent_promotion | **PASS.** Even a proof of (167.B1) would close only the complete residual scalar after its accepted connectors; it would not close a parent or change either exponent ledger. |
| no_in_round_pivot | **PASS.** The result is a scoped interface/power no-go for the frozen determinant route; no alternative frontier is proposed. |

The remaining accounting is exact in the following sense:

- **multiplicity:** one for the matrix map, the two-adic split, the gcd split, and the canonical row parameter;
- **modulus:** none is introduced by the exact dictionary; any transform modulus is undefined and therefore unpriced;
- **main term and errors:** no transform theorem is present, so none is available to bound;
- **boundaries and cells:** retained literally in (167.R18), but any smoothing decomposition and its total cost are unproved;
- **power:** an uncompensated \(\delta^{-A}\) smooth-amplitude loss is forbidden by (167.R17), and fixed-shift triangle inequality is forbidden by the \(L^3/L^2\) ledger.

No numerical or symbolic experiment was performed. The report is entirely algebraic.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

1. protocol.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/briefs/blind_determinant_interface_rederivation.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/blind_statement.md.

No proof graph, active campaign, strategy, Round-166 artifact or source audit, barrier packet, sibling report, conductor artifact, source theorem statement, web result, or shared synthesis was inspected.

## 7. Recommended state effect

**RETAIN (167.B1) as open; record the scoped selector-interface and smooth-amplitude no-go; make no proof-state change.**

The exact determinant, two-adic, gcd, character, and row dictionaries are algebraically compatible and multiplicity preserving, but they do not yield cancellation. Stop this round at the absent selector representation. Do not apply a transform, smooth the phase, take fixed-shift moduli, pivot to another frontier, promote the residual scalar or any parent, or change an exponent. A future attempt is viable only if it supplies a selector-aware native-oscillatory variable-determinant theorem and restores every norm, modulus, main term, error, cell, endpoint, and completion cost to \(O_{\gamma,\varepsilon}(L^2X^\varepsilon)\).
