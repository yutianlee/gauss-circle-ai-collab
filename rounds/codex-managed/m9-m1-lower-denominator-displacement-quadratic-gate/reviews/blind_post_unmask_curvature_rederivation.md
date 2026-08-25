## 1. Result and seam verdict

**GREEN.**  The exact curvature collar

\[
 L_h=\left\lfloor\frac{\rho y}{\sqrt h}\right\rfloor,
 \qquad 0<\rho<1,
\]

is target-safe for a fixed \(\rho\), uniformly for every real \(X\ge2\), every \(0\le q\le2y\), both parities of \(y\), and both scalar signs:

\[
 \mathcal C_N^\sigma
 :=\sum_{h\ge1}\frac1h
 \sum_{0\le v\le L_h}
 \chi_4(y-v)V_{\rm low}\!\left(\frac{4R^2h^2}{(y-v)^2}\right)
 e\!\left(\sigma h\frac{q+v^2}{y-v}\right)
 \ll_V R\log(2X),
 \qquad \sigma\in\{\pm1\}.
\tag{R1}
\]

Consequently, if \(\mathcal S_N^\sigma\) is the literal complement \(L_h<v<y\), then

\[
 \mathcal F_N^\sigma=\mathcal C_N^\sigma+\mathcal S_N^\sigma
 =\mathcal S_N^\sigma+O_V(R\log(2X)).
\tag{R2}
\]

This is a strict and owner-complete reduction of the **unsquared scalar support** and makes the scalar targets for \(\mathcal F_N^\sigma\) and \(\mathcal S_N^\sigma\) equivalent after epsilon renaming.

**REVISE.**  In the candidate proof, the parity-interval length should be written \(M_h\le1+L_h/2\), not \(M_h\ll L_h\) without qualification.  The latter fails when a floor gives \(L_h=0\).  The extra \(1\) contributes only a harmless \(\sqrt{h/y}\) term, and bounded \(X\) is separately finite, so this is an archival repair rather than a mathematical gap.

**RED.**  Equation (R2) is not a deletion from the Round-138 square and does not identify \(|\mathcal S_N|^2\) with a subowner of its cross-denominator residual.  Any such reading is impermissible.  The candidate explicitly distinguishes the valid scalar target equivalence from that invalid square-level deletion; that distinction is correct.

## 2. Exact hypotheses, parity lattice, support, and endpoints

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad 0\le q\le2y.
\tag{R3}
\]

The displacement dictionary \(d=y-v\) is a bijection between \(1\le d\le y\) and \(0\le v<y\).  Put \(p_y\in\{0,1\}\) with

\[
 p_y\equiv y-1\pmod2.
\]

Even \(d\) vanish, and all surviving points are uniquely

\[
 v=p_y+2n.
\tag{R4}
\]

Thus \(v\) is even for odd \(y\) and odd for even \(y\).  On this lattice the exact phase for sign \(\sigma\) is

\[
 \Phi_{\sigma,h}(v)
 =\sigma h\left(\frac{N}{y-v}-y-v\right)
 +\frac{y-v-1}{4}.
\tag{R5}
\]

The carrier in (R5) is linear in \(v\), so it affects the first-derivative aliases but not the curvature.  Since \(\chi_4\) and \(V_{\rm low}\) are real, the two scalar signs are conjugate; the direct curvature proof below also treats them symmetrically.

The literal support supplies a fixed \(C_V\) such that any nonzero sample satisfies

\[
 h\le C_V\frac{y-v}{R}\le C_V\frac yR\le C_VR.
\tag{R6}
\]

No lower support inequality is needed.  The only profile input is that its fixed zero extension has bounded supremum and finite one-dimensional variation.  For fixed \(h\),

\[
 t_h(v)=\frac{4R^2h^2}{(y-v)^2}
\]

is monotone on the collar.  Therefore the sampled variation of \(V_{\rm low}(t_h(p_y+2n))\) is at most the fixed total variation of the extended profile.  Profile entry and exit, a possible literal endpoint value, and the artificial endpoint \(L_h\) add only bounded jumps.

Choose \(0<\rho<1\), with the candidate's \(\rho<1/8\) more than sufficient.  Then \(L_h\le\rho y<y\).  The collar includes every integer \(0\le v\le L_h\); the survivor contains every integer \(L_h<v<y\).  If \(L_h\) has the wrong parity, the last surviving parity point lies below it and is still assigned uniquely.  If no parity point occurs, the row is empty.  The original endpoint \(v=0\), the artificial floor endpoint, the terminal point \(v=y-1\), and all zero-extended samples are therefore assigned exactly once.

## 3. Independent exact-phase curvature proof

Define

\[
 g(v)=\frac{q+v^2}{y-v}=\frac{N}{y-v}-y-v.
\]

Exact differentiation gives

\[
 g'(v)=\frac{N}{(y-v)^2}-1,\qquad
 g''(v)=\frac{2N}{(y-v)^3}.
\tag{R7}
\]

For \(v=p_y+2n\), differentiation with respect to \(n\) gives

\[
 \frac{d^2}{dn^2}\Phi_{\sigma,h}(p_y+2n)
 =\sigma\frac{8hN}{(y-p_y-2n)^3}.
\tag{R8}
\]

On \(0\le v\le L_h\), one has \(y-v\ge(1-\rho)y\).  Since \(y^2\le N\le y^2+2y\),

\[
 8\frac hy
 \le
 \left|\Phi_{\sigma,h}''(n)\right|
 \le
 \frac{8(1+2/y)}{(1-\rho)^3}\frac hy.
\tag{R9}
\]

Thus the parity-lattice second derivative has constant sign, is monotone in magnitude, and is comparable to \(h/y\), uniformly in \(q\), \(p_y\), and \(\sigma\).  By (R6), \(h/y\ll_V1/R\); hence for all sufficiently large \(X\) the second-derivative parameter is at most one.  The remaining bounded \(X\)-range contains only boundedly many active integer samples and is absorbed into the same fixed constant.

Use the elementary estimate

\[
 \sup_{J\subset I}\left|\sum_{n\in J}e(f(n))\right|
 \ll_A M\sqrt\lambda+\lambda^{-1/2}
\tag{R10}
\]

when \(I\) has \(M\) integer points and
\(\lambda\le|f''|\le A\lambda\) with constant sign.  Partial summation preserves (R10) after multiplication by an amplitude whose supremum plus sampled total variation is bounded.  The preceding monotonicity argument verifies that amplitude hypothesis for the literal profile.

Let

\[
 I_h=\{n\ge0:0\le p_y+2n\le L_h\},
 \qquad M_h=|I_h|\le1+\frac{L_h}{2}.
\]

Taking \(\lambda\asymp_\rho h/y\) in (R10) yields the exact row estimate

\[
 \begin{aligned}
 &\left|
 \sum_{n\in I_h}
 V_{\rm low}\!\left(\frac{4R^2h^2}{(y-p_y-2n)^2}\right)
 e\!\left(\Phi_{\sigma,h}(p_y+2n)\right)
 \right| \\
 &\qquad\ll_{\rho,V}
 (1+L_h)\sqrt{\frac hy}+\sqrt{\frac yh}\\
 &\qquad\ll_{\rho,V}
 \sqrt y+\sqrt{\frac yh}+\sqrt{\frac hy}.
 \end{aligned}
\tag{R11}
\]

This proof never separates the prescribed quadratic core from its correction.  It applies curvature directly to the complete reciprocal displacement phase.

By (R6), only \(h\le C_VR\) occur.  Using \(\sqrt y\le R\), (R11) gives

\[
 \begin{aligned}
 |\mathcal C_N^\sigma|
 &\ll_{\rho,V}
 \sqrt y\sum_{h\le C_VR}\frac1h
 +\sqrt y\sum_{h\le C_VR}\frac1{h^{3/2}}
 +\frac1{\sqrt y}\sum_{h\le C_VR}\frac1{\sqrt h}\\
 &\ll_{\rho,V}R\log(2X).
 \end{aligned}
\tag{R12}
\]

This proves (R1) for both signs and all \(q\), with the literal weights rather than a raw tuple count.

## 4. Dyadic height, alias, and endpoint ledger

Let \(h\asymp H\), with \(1\le H\ll_VR\).  The \(H\) heights and their weights \(h^{-1}\asymp H^{-1}\) cancel in a dyadic block.  Floors contribute at most one sample per row.  The complete block ledger is

| quantity on \(h\asymp H\) | exact \(R,H\)-power |
|---|---:|
| collar length per row | \(L_H\ll yH^{-1/2}+1\) |
| weighted absolute collar capacity | \(\ll yH^{-1/2}+1=R^2H^{-1/2}+O(1)\) |
| exact-curvature block bound | \(\ll R+RH^{-1/2}+\sqrt{H/y}\) |
| derivative change across the collar | \(\asymp (H/y)L_H\ll\sqrt H\) |
| number of integer aliases | \(O(1+\sqrt H)\) |
| quadratic width of one alias | \(\asymp\sqrt{y/H}=RH^{-1/2}\) |
| full-row exact-curvature cost | \(R\sqrt H+RH^{-1/2}\) |

The alias product \(\sqrt H\cdot RH^{-1/2}=R\) is the first term in the curvature bound; the residual \(RH^{-1/2}\) is the endpoint term.  At \(H=1\), a collar with absolute-capacity upper bound \(O(R^2)\) costs \(O(R)\).  At \(H=R\), a collar with upper bound \(O(R^{3/2})\) again costs \(O(R)\).  Summing the \(O(\log X)\) height blocks gives \(O(R\log(2X))\).

For a hypothetical fixed-top rowwise collar
\(L=\rho yH^{-\alpha}\), so that \(y-v\asymp_\rho y\), the same
exact-phase ledger is, up to a \(\rho\)-dependent constant,

\[
 RH^{1/2-\alpha}+RH^{-1/2}.
\tag{R13}
\]

Thus \(\alpha=1/2\) is the last power scale controlled at \(O(R)\) by independent rowwise curvature.  A full top row at \(H=R\) costs \(R^{3/2}\), reproducing rather than evading the half-integer paired-tube obstruction.

The curvature collar lies wholly at the denominator endpoint \(d\asymp y\asymp X^{1/2}=R^2\), because \(d=y-v\ge(1-\rho)y\).  It does not remove any \(D=X^{1/4}=R\) or \(D=X^{3/8}=R^{3/2}\) owner; those scales remain in \(\mathcal S_N^\sigma\).  At the \(D=X^{1/2}\) endpoint, \(d=y\) belongs to the collar when its parity survives, \(d=y-L_h\) is assigned according to the literal floor and parity, and all smaller denominators belong to the survivor.  No dyadic endpoint is crossed silently.

## 5. Scalar target equivalence, Round-138 seam, and no-go reconciliation

From (R2) and \(\log(2X)\ll_\varepsilon X^\varepsilon\),

\[
 |\mathcal F_N^\sigma|\ll_\varepsilon RX^\varepsilon
 \quad\Longleftrightarrow\quad
 |\mathcal S_N^\sigma|\ll_\varepsilon RX^\varepsilon,
\tag{R14}
\]

after renaming epsilon.  Conditional on the inherited Round-138 identity quoted in the permitted reports,

\[
 |\mathcal F_N|^2=\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon),
\tag{R15}
\]

(R14) also gives a logical target equivalence with
\(|\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon\).

**GREEN:** this chain of target statements is valid.  **RED:** it must not be strengthened to

\[
 |\mathcal S_N|^2=\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).
\]

Indeed,

\[
 |\mathcal F_N|^2
 =|\mathcal S_N|^2
 +2\operatorname{Re}(\mathcal S_N\overline{\mathcal C_N})
 +|\mathcal C_N|^2.
\tag{R16}
\]

The last term is target-safe, but the collar--tail cross term is not controlled without the very tail estimate that remains open.  In reduced variables \(h=ag\), \(d=bg\), the cutoff is

\[
 y-bg\le
 \left\lfloor\frac{\rho y}{\sqrt{ag}}\right\rfloor.
\tag{R17}
\]

It depends on the lift \(g\) and splits the exact reduced lift aggregate.  Therefore the collar is not a separately deletable Round-138 residual owner.  The candidate's explicit refusal to make that deletion is a **GREEN** seam; any graph label should say “scalar-tail reduction,” not “residual sub-square reduction.”

There is also no conflict with the primary perturbative-completion no-go.  The prescribed-centre decomposition writes

\[
 \Phi_{\sigma,h}(v)
 =\text{quadratic core}
 +\sigma E_{h,q,y}(v),
 \qquad
 E_{h,q,y}(v)=h\frac{v(q+v^2)}{y(y-v)}.
\]

At \(q=0\) and \(v\asymp y/\sqrt h\),

\[
 E_{h,0,y}(v)\asymp\frac y{\sqrt h},
\tag{R18}
\]

so the correction has polynomial, not bounded, variation on the curvature collar.  A quadratic-core Abel or fixed-modulus completion is therefore still forbidden there.  Estimate (R12) succeeds for a different reason: it leaves \(E\) inside the exact phase and uses the exact curvature (R8).  It estimates only the collar.  Extending the same rowwise estimate to a full \(h\asymp R\) row gives \(R^{3/2}\), exactly the capacity in the original no-go.  Hence the strict exact-phase collar reduction and the perturbative prescribed-core obstruction are complementary statements, not contradictory ones.

## 6. First doubtful step and control verdicts

The first doubtful line **inside the written candidate proof** is only the floor shorthand \(M_h\ll L_h\).  **REVISE** it to \(M_h\le1+L_h/2\), as in Section 3.  After that repair, no gap remains in the curvature-collar estimate.

The first genuinely unproved analytic step is

\[
 \boxed{|\mathcal S_N^\sigma|\ll_\varepsilon RX^\varepsilon.}
\tag{R19}
\]

Equivalently, a continuation would need joint signed cancellation across heights and exact half-integer aliases on \(v>L_h\), or a direct estimate of the full Round-138 cross-denominator residual.  Independent rowwise moduli have exhausted the \(R\) budget at the boundary (R13).

| seam | verdict | reason |
|---|---|---|
| exact \(q\)-range and two-way displacement | **GREEN** | only \(y^2\le N\le y^2+2y\) and the exact bijection are used |
| both parity lattices and both scalar signs | **GREEN** | (R4), (R5), and (R8) retain the carrier and sign |
| profile variation and zero extension | **GREEN** | monotone composition has fixed sampled variation; all entry, exit, and hard-cut jumps are bounded |
| floors and empty short rows | **REVISE** | replace \(M\ll L_h\) by \(M\le1+L_h/2\); the claim is unchanged |
| weighted dyadic height ledger | **GREEN** | the actual \(h^{-1}\) mass yields (R12), not a raw-count transfer |
| exact versus near aliases | **GREEN** | the second-derivative lemma sums all aliases collectively; no principal-only stationary formula is substituted |
| prescribed-core completion on this larger collar | **RED** | (R18) violates bounded correction variation |
| scalar target equivalence | **GREEN** | follows from the target-safe additive collar |
| deletion from the Round-138 square | **RED** | the cross term (R16) and lift split (R17) remain uncontrolled |
| downstream theorem or exponent | **RED** | the survivor retains \(R^{2+o(1)}\) absolute capacity |

The argument is analytic and requires no centre average, numerical experiment, arbitrary-coefficient theorem, positive energy replacement, Salié completion, or desired Gauss-circle bound.

## 7. Dependencies and recommended state effect

This independent review used exactly:

- problems/gauss_circle.md;
- state/control_models.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/literal_displacement_quadratic_scalar_attack.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reports/displacement_completion_hostile_audit.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md.

**Recommended state effect: GREEN with one wording repair.**  Promote the exact scalar collar estimate (R1)--(R2) and the scalar-tail target equivalence (R14) under the scoped outcome \(\mathsf{strict\_displacement\_quadratic\_reduction}\).  Record the floor correction \(M_h\le1+L_h/2\).  Retain the perturbative prescribed-core completion and full-row alias mechanisms as obstructed.

Do not promote a Round-138 residual deletion, a full scalar bound, lower GAR, a blockwise M1 parent, M9-M1, any M2 parent, endpoint uniformity, M9, the quarter theorem, or an exponent.  No shared state is edited.
