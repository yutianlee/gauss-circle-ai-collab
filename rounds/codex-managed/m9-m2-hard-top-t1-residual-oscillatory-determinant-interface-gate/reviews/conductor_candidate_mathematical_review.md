# Mathematical review of the Round 167 conductor candidate

- Candidate: candidates/conductor_round167_determinant_endpoint_polylog_reduction.md
- Role: independent mathematical reviewer
- Scope: determinant/orbit multiplicity, endpoint kernel, Schur capacity, polylogarithmic sector, bare orbit sum, source-interface qualifiers, power ledger, and downstream ownership
- Status: review evidence only; no claimant or shared-state mutation is licensed

## 1. Result

**Verdict: PASS mathematically, with one state-packaging clarification.**

The candidate correctly incorporates the repairs required by the Round-167 seams:

1. the literal incidence-to-matrix map and the free left-orbit opening are multiplicity preserving;
2. the endpoint vector reproduces the double divisor sum exactly and does not duplicate \(c_N^{\rm rem}\);
3. Schur's test gives only the \(L^3X^\varepsilon\) upper capacity;
4. the complete fixed-\(B\) polylogarithmic-shift sector is owner-complete and target-safe with the displayed epsilon relabelling;
5. the bare \(\chi_4\)-orbit coefficient vanishes for every \(k=2^v\), including \(k=1\), while that cancellation is correctly not transferred to a selector-dependent coefficient;
6. the gamma, nonautomorphy, common-\(f\), seminorm, dense-block, source-power, and fixed-shift qualifiers are mathematically scoped correctly; and
7. no residual, parent, bridge, or exponent is overpromoted.

No false or overstated mathematical sentence occurs in Sections 1--5. The first sentence that can be read too broadly is the final recommendation to create “one proved-internal reduction node” containing both the internal reductions and the source-interface no-go. If proof-state nodes are required to have homogeneous provenance, this should be split into an internal reduction node, a finite source-skeleton calculation, and a source-dependent rejected-route record. This is a state-packaging issue, not a defect in equations (167.C1)--(167.C19).

## 2. Exact statement and hypotheses

The candidate fixes

\[
J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
R_0=\lceil L\rceil,\qquad 0<\gamma<1,
\]

and endpoint atoms

\[
u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}),
\tag{2.1}
\]

where \(d,m\asymp L\), \(d\) is odd, \(|\lambda_{dm}(d)|\ll1\), and \(\lambda\) retains every literal selector and endpoint convention.

For \(x=(d,m)\), \(y=(d',m')\), and \(n(x)=dm\), the directed kernel is

\[
\begin{aligned}
T(y,x)={}&
\left(1-\frac{n(y)-n(x)}{R_0}\right)
\mathbf 1_{0<n(y)-n(x)<R_0}
\mathbf 1_{2\mid n(y)-n(x)}\\
&\times
\mathbf 1_{(d'-d)(m'-m)<0}
\mathbf 1_{(d,d')<\gamma L}.
\end{aligned}
\tag{2.2}
\]

The exact open estimate remains

\[
\Re\langle Tu_L,u_L\rangle
\ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{2.3}
\]

The candidate proves only exact reductions, an \(L^3X^\varepsilon\) positive upper bound, a strict small-shift sector, and scoped failures of named black-box placements. It does not claim (2.3).

For the source-power calculation, the hypotheses in (167.C17) are expressly optimistic:

\[
\mathsf A,\mathsf C,\mathsf D\asymp L,\qquad
\mathsf H\asymp L/k,\qquad
|\beta_h|\asymp1\ \text{on }\asymp\mathsf H\text{ indices},\qquad
\mathcal K_+^{1/2}\ll k^{1/2}X^\varepsilon.
\tag{2.4}
\]

The candidate explicitly says literal nonemptiness and density are not asserted. This corrects the earlier unconditional top-block formulation.

## 3. Proof or derivation

### 3.1 Incidence and orbit multiplicity

An ordered divisor incidence at \(N,N+r\) determines

\[
m=N/d,\qquad m'=(N+r)/d',
\]

and hence

\[
A(y,x)=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
\qquad \det A=d'm'-dm=r.
\tag{3.1}
\]

Conversely, the four entries recover \(N=dm\), \(N+r=d'm'\), and the ordered divisors \(d,d'\). There is no transpose, divisor-order, sign, or projective quotient. The map is bijective.

The factorization

\[
r=hk,\qquad k=2^{v_2(r)},\qquad h\ \mathrm{odd}
\]

is unique. For \(\Gamma_2(4,1)\le\mathrm{SL}_2(\mathbb Z)\), left multiplication preserves the determinant. If \(\gamma A=A\), then \(r\ne0\) makes \(A\) invertible over \(\mathbb Q\), so \(\gamma=I\). Thus the action is free, and choosing one representative per orbit introduces no stabilizer multiplicity. The literal subset need not be orbit invariant: the inner restriction to those \(\gamma A_{\mathcal O}\) that are literal still lists every literal matrix exactly once.

### 3.2 Endpoint identity and Schur capacity

The endpoint product is

\[
\begin{aligned}
u_L(y)\overline{u_L(x)}
={}&
\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}\\
&\times
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\end{aligned}
\tag{3.2}
\]

Multiplying by (2.2) adds exactly the Fejer and literal cross-endpoint conditions. Therefore

\[
\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
=\langle Tu_L,u_L\rangle.
\tag{3.3}
\]

Multiple endpoint indices may share the same product, but they are the distinct divisor incidences in the expansion of \(c_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}\). Since \(u_L\) contains individual \(\lambda_N(d)\) atoms rather than the already-summed coefficient \(c_N^{\rm rem}\), no coefficient sum is duplicated.

For fixed \(x\) and \(r\), the product \(n(y)=n(x)+r\) is fixed, and each divisor \(d'\) determines at most one \(m'\). Hence the row degree is at most

\[
\sum_{1\le r<R_0}\tau(n(x)+r)
\ll_\eta LX^\eta.
\]

The reverse argument gives the same column degree. Schur's test yields

\[
\|T\|_{2\to2}\ll_\eta LX^\eta.
\tag{3.4}
\]

Also,

\[
\|u_L\|_2^2
\le\sum_{N\in\mathcal I_L^{\rm lit}}\tau(N)
\ll_\eta L^2X^\eta.
\tag{3.5}
\]

Choosing each auxiliary divisor exponent in terms of the final requested \(\varepsilon\) proves

\[
|\langle Tu_L,u_L\rangle|
\ll_\varepsilon L^3X^\varepsilon.
\tag{3.6}
\]

The candidate correctly labels (3.6) as an upper capacity, not a lower bound.

### 3.3 Fixed-\(B\) polylogarithmic sector

For

\[
R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\},
\]

one modulus outside the complete restricted sector gives

\[
|\mathfrak C^{\rm rem}_{r\le R_{\log}}|
\le
\sum_{\substack{r\le R_{\log}\\2\mid r}}
\sum_N\tau(N)\tau(N+r).
\tag{3.7}
\]

Fix the final \(\varepsilon>0\). Since \(N,N+r\ll X\), the two divisor factors are each

\[
\ll_\varepsilon X^{\varepsilon/4},
\]

while

\[
(\log X)^B\ll_{\varepsilon,B}X^{\varepsilon/2}.
\]

The literal shell has \(O(L^2)\) products, so (3.7) is

\[
\ll_{\varepsilon,B}L^2X^\varepsilon.
\tag{3.8}
\]

The majorization begins only after every literal selector and cross-endpoint restriction is imposed. It is therefore owner-complete. If \(R_0-1\le\lfloor(\log X)^B\rfloor\), it covers every shift; otherwise it gives only an \(X^{o(1)}\)-shift strict sector. The candidate states both cases correctly.

### 3.4 Bare orbit cancellation

For

\[
\Gamma_2(4,1)
=\left\{\begin{pmatrix}p&4q\\s&t\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z)\right\},
\]

left multiplication changes the top row \((a,b)\) to

\[
(pa+4qc,\ pb+4qd_0).
\]

Since \(p\) is odd,

\[
\chi_4(pa+4qc)\chi_4(pb+4qd_0)
=\chi_4(p)^2\chi_4(a)\chi_4(b)
=\chi_4(a)\chi_4(b).
\tag{3.9}
\]

Thus \(\alpha_{\rm bare}\) is left invariant and its induced source character is principal.

The six top-row representatives of
\(\Gamma_2(4,1)\backslash\mathrm{SL}_2(\mathbb Z)\) are

\[
(x,1),\quad x=0,1,2,3,\qquad (1,0),\ (1,2).
\]

Column primitivity gives the Hermite representatives

\[
\sigma_b=\begin{pmatrix}1&b\\0&k\end{pmatrix},
\qquad b\bmod k,\quad (b,k)=1,
\]

with \(b=0\) at \(k=1\). A top row \((x,y)\) becomes

\[
(x,xb+yk).
\]

The candidate's finite sums are correct:

- at \(k=1\), the six contributions sum to \(0\);
- at \(k=2\), the four \((x,1)\) classes total \(-2\), while \((1,0)\) and \((1,2)\) total \(+2\);
- for \(4\mid k\), each odd unit \(b\) contributes \(4\chi_4(b)\), and
  \[
  \sum_{b\in(\mathbb Z/k\mathbb Z)^\times}\chi_4(b)=0.
  \]

Therefore

\[
\sum_{\tau\in\Gamma_2(4,1)\backslash\mathcal M_{2,1,k}}
\alpha_{\rm bare}(\tau)=0
\qquad(k=2^v).
\tag{3.10}
\]

This is exactly the bare coefficient sum. The candidate correctly warns that inserting the residual selector into \(\alpha\) changes the orbit coefficient and requires a new computation.

### 3.5 Gamma, nonautomorphy, common-\(f\), and seminorm qualifiers

The low-gcd witness is correct for \(0<\gamma<1/2\). With

\[
A=\begin{pmatrix}G&3G\\T&3T+2\end{pmatrix},
\qquad
v=\begin{pmatrix}1&4\\0&1\end{pmatrix},
\]

one has \(\det A=2G<L\), while

\[
\gcd(G,3G)=G\ge\gamma L.
\]

The top row of \(vA\) is

\[
(G+4T,\ 3G+12T+8).
\]

Its gcd divides \(8\), and its first entry is odd, so the gcd is \(1\). Hence the globally defined low-gcd multiplier is not left invariant. The candidate properly states that this witness is not asserted to be a literal project incidence and does not rule out a restricted-support extension.

For \(\gamma\ge1/2\), write \(d=gu,d'=gv\). Because \(g\) is odd and \(r\) is even,

\[
\frac rg=vm'-um
\]

is a positive even integer. Thus \(r/g\ge2\) and

\[
g\le r/2<L/2\le\gamma L.
\]

The low-gcd cutoff is indeed identically one in this range. The remaining-selector nonautomorphy is stated only as “no proved law,” not as a universal impossibility.

For the common-\(f\) issue, normalized phases at determinant \(r\) have the form

\[
F_r(x,z)=
e\!\left(J\sqrt r\{\sqrt{xz}-\sqrt{xz-1}\}\right).
\]

For \(r_1\ne r_2\), the quotient \(F_{r_1}/F_{r_2}\) is nonconstant on every common open cell because the bracketed analytic function has nonzero derivative. Hence the natural family is not rank one in determinant and one common analytic test function. The candidate correctly limits this to continuous rank-one nonseparability and leaves discrete interpolation and controlled-rank decompositions open.

The derivative ledger

\[
L|\partial_a\phi_r|+L|\partial_{d_0}\phi_r|
\asymp Jr/L
\]

is correct. Since \(r\ge2\) and \(L\ll J^{1/2}\), a fixed positive uncompensated polynomial loss in

\[
\delta^{-1}\gtrsim1+Jr/L
\]

is not \(X^\varepsilon\)-safe. The words “fixed positive” and “uncompensated” are essential and are present. The candidate does not rule out compensating oscillatory decay.

### 3.6 Conditional source-power ledger

Under (2.4), let \(\mathsf H\asymp L/k\). Then

\[
\|\beta\|_2\asymp\mathsf H^{1/2},
\qquad
\frac{\|\beta\|_1}{\|\beta\|_2}\asymp\mathsf H^{1/2}.
\]

The displayed \(\mathcal R_0\) contribution on a fixed two-adic block has scale

\[
L\cdot\mathsf H^{1/2}\cdot\mathsf H^{1/2}\cdot k^{1/2}
\asymp L^2k^{-1/2}.
\]

Summing over powers of two costs \(O(1)\) at the \(L^2\) scale. Under the same explicitly optimistic hypotheses, the displayed \(\mathcal R_2\) branch has scale

\[
\delta^{-O(1)}L^{2+\theta_4+\varepsilon}k^{-1/2},
\]

and hence sums to the candidate's (167.C18). The candidate explicitly says this is a hypothetical dense-block audit, does not assert literal nonemptiness or density, retains the unspecified seminorm loss, and infers no negative power of \(\mathcal K_+\). These are the required qualifiers.

The distinction between a principal induced character and the finite orbit coefficient is also correct: principality permits a source principal channel, but (3.10) makes the bare finite coefficient vanish. A selector-dependent coefficient must be recomputed.

### 3.7 Downstream scope

The candidate leaves open precisely the non-polylogarithmic shifts, the full K17a inequality, and every downstream owner. It does not move the real part inside the variable-\(r\) sum, claim a fixed-shift theorem, close the residual scalar, close any hard-TOP/BAL/UNBAL or M1 owner, invoke either bridge, or change an exponent. Its terminal no-go is confined to the named 2024, fixed-shift-triangle, and 2025 Part-I black-box placements.

## 4. First doubtful or unproved step

No false or overstated mathematical sentence was found in Sections 1--5.

The first genuine unproved analytic step is exactly (167.C19): obtain the missing factor \(L\) for the literal endpoint vector over the non-polylogarithmic determinant range while preserving one outer real part. The candidate correctly identifies the required selector realization, variable-\(r\) phase treatment, and complete orbit-correlation, principal-component, seminorm, cell, boundary, endpoint, and completion ledger.

The first wording that merits clarification is in Section 6: “create one proved-internal reduction node containing (167.C4)--(167.C9), (167.C14), and the scoped no-go (167.C10).” If provenance is homogeneous at node level, split this into:

1. an internal determinant/endpoint/polylogarithmic reduction node for (167.C4)--(167.C9);
2. a finite source-skeleton orbit lemma for (167.C14), with the exact group and orbit-set definitions as dependencies; and
3. a source-dependent rejected-route record for (167.C10).

If the graph permits one composite node with explicit mixed dependencies, no mathematical repair is needed.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact incidence multiplicity | **GREEN.** Ordered divisor incidences and matrices are bijective |
| Left-orbit multiplicity | **GREEN.** The determinant is nonzero and the left action is free |
| Endpoint quadratic identity | **GREEN.** Every divisor-pair term occurs once; \(c_N\) is not duplicated |
| Schur row/column degree | **GREEN.** Both degrees are \(O_\varepsilon(LX^\varepsilon)\) |
| Schur capacity | **GREEN.** \(L^3X^\varepsilon\) is correctly only an upper capacity |
| Fixed-\(B\) polylog estimate | **GREEN.** The \(\varepsilon/4+\varepsilon/4+\varepsilon/2\) ledger is exact |
| Polylog owner completeness | **GREEN.** All literal conditions precede the majorization |
| Bare orbit cancellation | **GREEN.** The \(k=1\), \(k=2\), and \(4\mid k\) calculations all vanish |
| Gamma qualifier | **GREEN.** The witness is scoped to \(\gamma<1/2\); the cutoff is automatic for \(\gamma\ge1/2\) |
| Nonautomorphy qualifier | **GREEN.** No universal nonautomorphy claim is made |
| Common-\(f\) qualifier | **GREEN.** Only continuous rank-one separation is excluded |
| Seminorm qualifier | **GREEN.** The loss is explicitly fixed, positive, and uncompensated |
| Source-power qualifier | **GREEN.** Dense support is hypothetical; no literal nonemptiness or negative \(\mathcal K_+\) power is inferred |
| Fixed-shift triangle | **GREEN.** It is rejected because it moves absolute values inside the shift aggregation |
| Downstream scope | **GREEN.** K17a, all parents, bridges, and exponents remain open |

No numerical experiment is needed; every check is finite algebra, divisor counting, or power bookkeeping.

## 6. Dependencies and exact artifacts used

The review used:

1. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/candidates/conductor_round167_determinant_endpoint_polylog_reduction.md;
2. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/blind_determinant_interface_rederivation.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/oscillatory_source_power_hostile_audit.md, for the quoted source definitions and \(\mathcal R_2\) formula;
5. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/source_orbit_phase_power_seam_review.md, for the exact group definition and an independent source-formula cross-check.

The calculations in Sections 3.1--3.6 were reproduced in this review. No candidate file, proof graph, synthesis, validation matrix, or shared state was edited.

## 7. Recommended state effect

**PASS the mathematical candidate; no direct graph edit from this review.**

The conductor may retain:

- (167.C4)--(167.C5) as exact multiplicity and endpoint identities;
- (167.C6)--(167.C7) as a positive \(L^3X^\varepsilon\) upper-capacity bound;
- (167.C8)--(167.C9) as the owner-complete fixed-\(B\) polylogarithmic strict sector;
- (167.C14) as the finite bare-orbit cancellation lemma with its selector qualifier;
- (167.C10) as a route-scoped no-go for only the named black-box placements.

Keep K17a, the complete residual scalar, every parent and bridge, and all exponent ledgers unchanged. If the proof graph requires homogeneous provenance, apply the three-way node split described in Section 4; otherwise the candidate needs no mathematical revision.
