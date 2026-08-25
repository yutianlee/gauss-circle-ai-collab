# Round 162 source and downstream graph-scope review

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Review: `source_and_downstream_graph_scope_review`
- Verdict: **GREEN**
- Scope: primary-source parameter/power seam and accepted-graph scope only
- Status: review evidence; no state mutation

## 1. Result

**GREEN.**  The selected candidate is source-calibrated and graph-safe in
its stated route scope.  Its terminal conclusion is only that exact
character Poisson, exact Möbius opening closed by termwise positive dual
control, a second bare character transform, standard positive differencing,
and the specifically audited named-source interfaces do not prove

\[
 |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon
\tag{162.SG1}
\]

uniformly for

\[
 J=\sqrt X,\qquad H=J^{1/2}+O(1),\qquad 1\ll L\ll H.
\tag{162.SG2}
\]

The conclusion is not a physical lower bound, a literature impossibility
theorem, or a completed hard-TOP estimate.

One new node,

`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`,

is nonduplicate.  Round 137 already owns the unprojected product-fibre
reciprocal self-return, and Round 161 already owns the coarse common-test
and named-source obstruction.  The new content is the exact mod-four
character transform, its odd dual character, the literal
\(Q=[a^2,c],R=[b^2,c]\) opening, the scaled saddle and collar

\[
 e(XQd_2/s),\qquad s\asymp JQ,qquad
 |s\ell-XQR|\ll QRJ/L,
\tag{162.SG3}
\]

the cancellation of the \(QR\)-powers in the positive collar ledger, the
bare-transform involution, and the even-shift differencing obstruction.

The new node may be added only as a dependency and as inconclusive evidence
to the two open hard-TOP parents

1. `M9-M2-top-endpoint-signed-cone`;
2. `M9-M2-top-endpoint-density-discrepancy-energy`.

No reverse dependency into an accepted node and no status promotion of an
open parent is licensed.

## 2. Exact statement and hypotheses

### 2.1 Literal source maps

For a fixed exact opening

\[
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\quad d_2=Rn,
\tag{162.SG4}
\]

the nonempty physical block has \(m\asymp L/Q\), \(n\asymp L/R\), while

\[
 J\sqrt{QRmn}
 =F\frac{m^{1/2}n^{1/2}}{M^{1/2}N^{1/2}},qquad
 M=L/Q,\quad N=L/R,\quad F=JL.
\tag{162.SG5}
\]

Thus the monomial frequency \(F=JL\) is invariant under the opening.
Here and below a source length is chosen as a positive dyadic/integer
envelope comparable to \(L/Q\) or \(L/R\) when the quotient itself is not
an integer.  This is covered by the explicitly granted cost-one subdivision
and changes no displayed power; it is not a claim that the rough physical
coefficient has become source-legal.
The named cards and literal substitutions are as follows.

| Source | Printed hypotheses relevant here | Literal map and restored result |
|---|---|---|
| Bombieri--Iwaniec, Lemma 2.4 | A separated coefficient \(a(x)b(\eta)\); the right side charges absolute near-collision forms | \(K=1,F=JL,u(m)=\sqrt{m/M},v(n)=\sqrt{n/N}\).  The phase maps, but the shell, cone, ratio profile, Möbius projector, and boundary coefficient are joint.  No cost-controlled separated representation is supplied. |
| Kowalski--Robert--Wu, Proposition 5 | \(F>0\), \(M,N\ge1\), \(|\varphi_m|,|\psi_n|\le1\), and \(\alpha,\beta\notin\{0,1\}\) | With \(\alpha=\beta=1/2\) and (162.SG5), the bound is (162.SG6) below. |
| Robert--Sargos, Theorem 1 | \(H_0,N_0,M_0\) positive integers, \(\Xi>1\), separated \(a(h,n)b(m)\), and \(\alpha(\alpha-1)\beta\gamma\ne0\) | \(H_0=L/Q,M_0=L/R,N_0=1,\alpha=\beta=1/2,\gamma=1,\Xi=JL/2\), with the sole source value \(n=2\).  The restored bound is (162.SG7). |
| Duke--Friedlander--Iwaniec, Theorems 1--2 | A fixed integral modular numerator and separated coefficient vectors in \(e(a\overline m/n)\) | The moving ordinary reciprocal \(e(XQd_2/s)\) has no uniform literal substitution for arbitrary real \(X\); taking a one-point inverse variable formally still leaves a moving numerator and no target-strength bound. |
| Duke--Friedlander--Iwaniec, Lemma 8 | One fixed modulus \(c\), an interval/progression variable \(x\), \((c,k)=1\), and integers \(a,b\) in \(e((a\bar x+bx)/c)\) | Here \(s\) is the varying denominator, not a residue variable modulo one fixed \(c\).  There is no literal substitution. |
| Bettin--Chandee, Theorems 1--2 | Separated \(\nu_a\alpha_m\beta_n\), coprimality, and the source arithmetic multiplier in \(e(\vartheta a\bar m/n)\) | On the admissible integral subcase there is a formal degenerate placement \(M=1,N\asymp JQ,A\asymp L,\vartheta=XQ\).  It is not a target-strength match: \((1+|\vartheta|A/(MN))^{1/2}\asymp(JL)^{1/2}\), independently of \(Q,R\), before the remaining positive powers and physical stationary normalization. |
| Dong--Robles--Zeindler, Theorem 1.6 | Positive integral \(a,b\), separated coefficients, coprime dyadic variables, and modular phase \(e(a\bar m/(bn))\) | A formal one-point inverse placement requires the moving value \(a=XQd_2\), which is not a fixed positive integer uniformly for arbitrary real \(X\).  The theorem has no literal uniform target-strength placement. |

The KRW substitution is exactly

\[
\begin{aligned}
 &J^{1/8}L^{13/8}(QR)^{-3/4}
 +L^{3/2}Q^{-1/2}R^{-1}\
 &\qquad+L^{7/4}Q^{-1}R^{-3/4}
 +J^{-1/2}L^{3/2}(QR)^{-1}.
\end{aligned}
\tag{162.SG6}
\]

At \(Q=R=1\), this is

\[
 J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}
 +J^{-1/2}L^{3/2},
\]

which is the candidate's (162.CA28).

The Robert--Sargos substitution is exactly

\[
\begin{aligned}
 &J^{1/4}L^{3/2}Q^{-3/4}R^{-1/2}
 +L^{7/4}Q^{-3/4}R^{-1}\
 &\qquad+L^{3/2}Q^{-1}R^{-1/2}
 +J^{-1/2}L^{3/2}(QR)^{-1}.
\end{aligned}
\tag{162.SG7}
\]

At \(Q=R=1\), this is the candidate's (162.CA29).  Since
\(J\asymp H^2\) and \(L\ll H\), the displayed direct source bounds do not
reach (162.SG1), even after the counterfactual grant of cost-one coefficient
separation.

The Kloosterman conclusion must be read with the calibration in the table:
DFI Lemma 8, DFI's fixed-numerator bilinear form, and DRZ have no uniform
literal map; Bettin--Chandee has a formal degenerate arithmetic-subcase map,
but its printed parameter factor and separated coefficient are adverse.
In particular the formal integral placement uses \(XQ\in\mathbb Z\); if a
version of the theorem is read with a more permissive real multiplier, the
same calculation (162.SG8), rather than integrality, still blocks this
direct target-strength use.
The candidate says only that none gives a **literal target-strength**
substitution, which is correct.  It does not say that ordinary reciprocals
can never be embedded degenerately into a modular-inverse form.

### 2.2 Graph hypotheses

The current graph contains, with `proved_internal` status:

- `M9-M2-hard-top-product-fibre-transform-self-return` (Round 137);
- `M9-M2-hard-top-radical-long-channel-exact-collision-control`
  (Round 161);
- `M9-M2-hard-top-radical-frequency-common-test-source-obstruction`
  (Round 161).

It contains, with `open` status:

- `M9-M2-top-endpoint-signed-cone`;
- `M9-M2-top-endpoint-density-discrepancy-energy`.

The Round-161 patch already places both radical nodes as dependencies and
inconclusive evidence on those two open parents.  The selected Round-162
node continues that direction; it does not modify an accepted statement.

## 3. Proof and derivation

### 3.1 Power restoration

Substituting \(M=L/Q,N=L/R,F=JL\) into KRW Proposition 5 gives

\[
 (FM^6N^6)^{1/8}=J^{1/8}L^{13/8}(QR)^{-3/4},
\]

\[
 M^{1/2}N=L^{3/2}Q^{-1/2}R^{-1},\qquad
 MN^{3/4}=L^{7/4}Q^{-1}R^{-3/4},
\]

and

\[
 F^{-1/2}MN=J^{-1/2}L^{3/2}(QR)^{-1}.
\]

This proves (162.SG6).  No \(Q,R\)-factor or stationary normalization is
missing.

For Robert--Sargos, \(H_0N_0M_0=L^2/(QR)\), and the four bracket terms in
Theorem 1 give, after multiplying by that prefactor,

\[
 J^{1/4}L^{3/2}Q^{-3/4}R^{-1/2},quad
 L^{7/4}Q^{-3/4}R^{-1},quad
 L^{3/2}Q^{-1}R^{-1/2},quad
 J^{-1/2}L^{3/2}(QR)^{-1}.
\]

This proves (162.SG7).  The candidate quotes only the unsieved
\(Q=R=1\) instances, so its displayed powers are exact.

For Bettin--Chandee's formal one-point inverse placement,

\[
 \frac{|\vartheta|A}{MN}
 \asymp\frac{XQ\,L}{JQ}=JL.
\tag{162.SG8}
\]

Thus scaling by \(Q,R\) does not repair the printed adverse factor.  For
the other Kloosterman cards, the fixed integral modular data and separated
coefficient hypotheses fail before a physical power comparison is
available.  These facts justify a named-interface no-go, not a universal
source no-go.

### 3.2 Nonduplication

The Round-137 node proves a coefficient-free/product-fibre derivative
capacity and the reciprocal principal self-return after resolving the
divisor fibre.  It explicitly leaves endpoints and the actual rough
coefficient open.  It does not contain the exact character Poisson formula,
the odd-dual \(\chi_4(s)\), the lcm opening, the scaled \(Q,R\) collar, or
the even-shift differencing identity.

The Round-161 common-test node records the literal \(t=1\) coefficient,
the \(L^{2+o(1)}\) positive capacity, a phase-aligned diagnostic, and the
no-match of four earlier source interfaces.  It does not identify the
character saddle, prove the product collar
\(|s\ell-XQR|\ll QRJ/L\), show cancellation of its \(QR\)-powers, or park
the second character transform and standard differencing.  It also does
not contain the KRW, DFI, Bettin--Chandee, or DRZ source audit now recorded.

The Round-162 node therefore adds a distinct exact transform-and-collar
obstruction.  It depends forward on the older nodes and neither supersedes
nor weakens them.

### 3.3 Downstream direction

The new obstruction is relevant to the exact \(t=1\),
\(D\asymp L^2\) close-factor subproblem named by both open hard-TOP parents.
Adding it to each parent's `dependencies` and `evidence.inconclusive` is
therefore directionally valid.  It proves no estimate needed by either
parent, so it cannot enter `evidence.positive`, change either status, or
create an `implies` edge.  An accepted dependency must not be made to
depend backward on this later obstruction.

## 4. First doubtful or unproved step

The first affirmative step still missing is a target-strength signed bound
for the complete aggregate represented at smooth principal level by

\[
 \frac{L^{3/2}}{\sqrt J}
 \sum_{a,b,c}\frac{\mu(a)\mu(b)\mu(c)\chi_4(Q)}{QR}
 \sum_{N\approx XQR}
 \sum_{\substack{s\mid N, s\ {
m odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s),
\tag{162.SG9}
\]

with \(Q=[a^2,c]\), \(R=[b^2,c]\), arbitrary-real centre, exact physical
profiles, the even-\(d_2\) branch, collar tails, hard boundaries, stars,
floors, and endpoint transitions retained before every positive norm.

Equation (162.SG9) is only the principal interface.  No complete physical
Poisson formula for every hard piece, and no signed estimate for their
aggregate, is proved.  This is why the two parent updates are inconclusive
only.  For direct monomial sources, the earlier unproved seam is a
cost-controlled separation of the actual joint coefficient.  For the
Kloosterman route, either the source arithmetic hypotheses do not match or,
in the Bettin--Chandee degenerate subcase, the restored source bound remains
too large.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_L_J_H_X_map` | **Pass.** \(J=\sqrt X\), \(H=J^{1/2}+O(1)\), and \(1\ll L\ll H\) are used consistently. |
| `scaled_Q_R_opening` | **Pass.** \(Q=[a^2,c]\), \(R=[b^2,c]\), \(s\asymp JQ\), \(\ell\asymp JR\), and \(|s\ell-XQR|\ll QRJ/L\) are literal. |
| `KRW_Proposition_5_parameters_and_powers` | **Pass.** Equations (162.SG5)--(162.SG6) reproduce all four printed terms. |
| `Robert_Sargos_Theorem_1_parameters_and_powers` | **Pass.** The sole \(n=2\) choice, \(\Xi=JL/2\), and all four restored terms in (162.SG7) are correct. |
| `Bombieri_Iwaniec_coefficient_hypothesis` | **Pass.** The candidate uses the lemma only as a separated-coefficient interface and does not declare the physical coefficient separated for free. |
| `Kloosterman_no_match_calibration` | **Pass.** Fixed-modulus/fixed-integral data failures are distinguished from Bettin--Chandee's formal degenerate arithmetic-subcase placement; the conclusion is only no target-strength match. |
| `source_no_go_not_literature_no_go` | **Pass.** Future, unexamined, or bespoke coefficient-sensitive theorems remain open. |
| `new_node_nonduplicate` | **Pass.** The exact character, opening, scaled collar, involution, and differencing package is absent from the Round-137 and Round-161 nodes. |
| `dependency_direction` | **Pass.** New node depends on the three accepted predecessors; only the two open parents may receive it. |
| `parent_status_and_evidence_scope` | **Pass.** Both parents remain open and receive only inconclusive evidence. |
| `physical_lower_bound_control` | **Pass.** \(\sqrt{JL}\) is a positive route capacity, not physical mass or a lower bound. |
| `remaining_channels_and_downstream_scope` | **Pass.** No remaining few-point channel, full hard TOP, smooth M2 packet, M9--M2, M9, bridge, target, or exponent is changed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The review used exactly these internal artifacts:

1. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reports/t1_bilinear_source_hostile_audit.md`;
3. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/state_patch.json`;
4. `state/proof_obligations.yml` at its current Round-161-applied state.

The theorem statements and maps were checked against the primary links
already carried by the source report:

1. Bombieri--Iwaniec, Lemma 2.4:
   <https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf>;
2. Kowalski--Robert--Wu, Proposition 5:
   <https://ems.press/content/serial-article-files/38194?nt=1>;
3. Robert--Sargos, Theorem 1:
   <https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf>;
4. Duke--Friedlander--Iwaniec, Theorems 1--2 and Lemma 8:
   <https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf>;
5. Bettin--Chandee, Theorems 1--2:
   <https://arxiv.org/html/1502.00769v1>;
6. Dong--Robles--Zeindler, Theorem 1.6:
   <https://arxiv.org/abs/2601.00292>.

No state, source card, candidate, sibling report, synthesis, strategy,
validation, or graph file was edited.

## 7. Recommended state effect

### 7.1 Create exactly one node

Create

```text
id: M9-M2-hard-top-t1-character-poisson-product-collar-obstruction
type: obstruction
track: M9_analytic
status: proved_internal
dependencies:
  - M9-M2-hard-top-product-fibre-transform-self-return
  - M9-M2-hard-top-radical-long-channel-exact-collision-control
  - M9-M2-hard-top-radical-frequency-common-test-source-obstruction
implies: []
blockers: []
terminal_label: hard_top_t1_close_factor_bilinear_no_go
```

Its statement must retain all candidate qualifications: exact
character-preserving Poisson, the \(Q,R\)-scaled positive collar capacity,
bare-transform involution, standard-differencing sign loss, and only the
audited named-source interfaces are parked.  The target, physical mass, and
all boundary owners remain open.

The minimum direct evidence is the selected candidate, the source report,
and this review.  Other independently validated Round-162 reports may be
added by the conductor, but are not inferred here.

### 7.2 Update exactly two open parents

For each of

- `M9-M2-top-endpoint-signed-cone`;
- `M9-M2-top-endpoint-density-discrepancy-energy`,

add the new node to `dependencies` and add the Round-162 candidate, source
report, and this review only as `evidence.inconclusive`.  Preserve status,
statement, `implies`, blockers, and all existing evidence.

### 7.3 No change

Make no statement, status, implication, blocker, or reverse-dependency
change to:

- the three accepted dependency nodes named in Section 7.1;
- `M9-M2-hard-top-truncated-divisor-energy-and-radical-control`;
- `M9-M2-character-factor`;
- `M9-M2-hard-top-square-product-entry-sector`;
- either open hard-TOP parent's status or claimed estimate;
- `M9-M2-physical-one-count-assembly`;
- `M9-M2-smooth-balanced-quarter-packet-estimate`;
- `M9-M2-smooth-unbalanced-three-quarter-estimate`;
- `M9-M2`, `M9-M1`, `M9-endpoint-uniformity`, or `M9`;
- `Conditional-bridge`, `GC-partial-one-third`,
  `GC-external-Li-Yang-theta-star`, or `GC-target`.

### 7.4 Reject only the following readings

Reject:

1. the \(t=1\) target is proved;
2. the collar capacity is physical mass or a lower bound;
3. Möbius opening, tensor separation, or divisor completion is free;
4. a second character transform or standard positive differencing supplies
   a contraction;
5. every hard endpoint or transformed boundary family is target-safe;
6. every Kloosterman source has no formal degenerate embedding--the correct
   conclusion is that none of the audited cards gives a uniform literal
   **target-strength** estimate;
7. the named-source audit excludes another or future coefficient-sensitive
   theorem;
8. the new node supersedes or reverses the Round-137 or Round-161 nodes;
9. the \(t=1\) route no-go closes the remaining few-point channels, full
   hard TOP, either smooth M2 packet, M9--M2, M9, a bridge, or any global
   exponent.

Accordingly, the exact graph recommendation is: **create one nonduplicate
obstruction node, attach it inconclusively to exactly two open hard-TOP
parents, and make no other graph change.**
