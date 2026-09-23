# Blind post-unmask Farey-covector post-repair verification

- Campaign: `m9-m1-t1-rho-large-bezout-edge-gate`
- Round: 192
- Role: post-repair verifier preserving the prior blind-review boundary
- Candidate SHA-256:
  `9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5`
- Numerical theorem evidence: none

## 1. Result: PASS

**PASS.** The current candidate implements all five repairs requested in the
blind post-unmask review. No remaining repair was found in the assigned
seams.

In particular:

1. (192.C14) and its coverage paragraph now carry the explicit
   \(T\geq1\) premise, while \(T=0\) continues to give the empty Farey
   projector.
2. (192.C12) is now an exact fixed-packet decomposition, followed separately
   by the inherited linear outer assembly.
3. (192.C38)--(192.C40) now specify the canonical anchor interval, define
   \(\theta_{\omega,c}\), state its two possible carry values, and expose the
   inherited affine parity rule.
4. (192.C37) now assumes a finite or absolutely summable sequence extended
   by zero to every integer height, and the endpoint prose now says the
   translations "need not coincide" rather than claiming universal
   inequality.
5. (192.C41) is now a rigorous, explicitly unsaturated, prime-modulus ambient
   control with a defined central-set size, per-covector capacity, and
   coefficient-class-only scope.

The new endpoint number/divisor translations (192.C40a)--(192.C40b) are
internally consistent with (192.C35), have the correct orientation-swapped
signs, retain the representative-dependent \(d_v\), and do not reintroduce
the rejected transport-invariance claim.

The verdict concerns the repaired formal candidate only. Its inherited
Round-191 endpoint definitions and outer connectors remain full-context
dependencies rather than claims independently reconstructed in this blind
review.

## 2. Exact statement and hypotheses verified

The verification concerns the same exact fixed packet as the prior review,
including the fast predicate and one power-of-two \(J\)-band in (192.C4a),
the rho-large condition \(|\rho|>T\), and the piecewise projector

\[
 P_A(v)=1_{T\geq1}
 1_{\{\exists(c,d)\in\mathcal F_A:
              |c\beta-d\rho|\leq T\}}.
\]

The repaired fixed-level identity is now

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix},
 \qquad
 \mathscr R_{\rm core,fix}=(I-P_A)\mathscr R_{\rm fix}.
\]

The candidate then explicitly applies the inherited linear outer assembly to
obtain the identically typed global decomposition before the single final
real part. This resolves the type ambiguity without changing the union
projector or separately absolutizing orientations.

For \(T\geq1\), the repaired coverage statement is

\[
 \left\lfloor
 \frac{(U-1)/2}{A+1}
 \right\rfloor\leq T
 \quad\Longrightarrow\quad
 \mathscr R_{\rm core,fix}=0.
\]

Its equivalent integral condition
\(U\leq2(A+1)(T+1)-1\) remains correct. The ell-zero identity for
\((c,d)=(|\rho|,|\beta|)\) is algebraically valid in every regime, while
its safe-union coverage consequence occurs only inside this explicitly
\(T\geq1\) paragraph. At \(T=0\), \(P_A=0\), so no ell-zero class is
silently promoted.

## 3. Proof and repair-by-repair derivation

### 3.1 \(T=0\), floors, and ell-zero scope

The candidate now says twice that (192.C14) is a \(T\geq1\) statement,
including the premise inside the boxed formula. Therefore the numerical
floor inequality cannot be used when \(T=0\). Because (192.C9) still sets
\(\mathcal E_A=\varnothing\) in that regime, the exact core remains the
entire inherited rho-large remainder, as required.

For \(T\geq1\), the circular-pigeonhole proof gives

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \leq\left\lfloor\frac{|\rho|}{A+1}\right\rfloor.
\]

A core row has integral minimum at least \(T+1\), so
\(|\rho|\geq(A+1)(T+1)\). The floor and equivalent \(U\)-inequality in
(192.C14) follow exactly. No endpoint or saturation case has changed.

### 3.2 Fixed packet versus outer assembly

Equation (192.C12) now uses
\(\mathscr J_{\rm safe,191,fix}\),
\(\mathscr R_{\rm fix}\), and
\(\mathscr R_{\rm core,fix}\) consistently. It no longer adds a fixed
packet to an untyped global aggregate. The next sentence applies the outer
operator only after the fixed identity and explicitly invokes linearity.

This agrees with the exact algebra in (192.C27): selected terminal and
Fejer rows are replaced by the selected complete original packet, while
unselected terminal and Fejer rows remain in the safe aggregate. The core
is the complex complement before the final real part. The repair therefore
preserves the single-outer-operation rule and introduces no overlap.

### 3.3 Canonical anchor, theta values, and affine parity

The candidate now chooses

\[
 S_{0,\omega}(h)\in[0,U),
 \qquad
 S_{0,\omega}(h)\equiv
 \epsilon_\omega\rho h\pmod U
\]

uniquely. This removes the arbitrary height-dependent multiples of \(U\)
identified in the prior review. Since
\(\rho\Delta=c+U\ell\) with \(1\leq c<U\), the repaired definition

\[
 \theta_{\omega,c}(h)=
 \frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
       -\epsilon_\omega c}{U}
\]

gives

\[
 \theta_{+,c}\in\{-1,0\},
 \qquad
 \theta_{-,c}\in\{0,1\}.
\]

Substitution into (192.C38) yields exactly

\[
 N_\omega(h;\Delta)
 =\theta_{\omega,c}(h)-\epsilon_\omega\ell.
\]

The candidate now separately states the inherited affine reindexing rule
\((-1)^{N_\omega}\), so the accumulated factor (192.C40) is no longer
asserted from congruence alone. Its mode part remains
\(e(\epsilon_\omega ac/q)\), as follows from \(U=mq\).

### 3.4 Zero-extended Abel identity and endpoint wording

Equation (192.C37) now quantifies over a finite or absolutely summable
height sequence extended by zero to all \(h\in\mathbb Z\). Reindexing the
second sum by \(h\mapsto h+\Delta\) therefore gives the exact factor
\(1-z^\Delta\), with no omitted endpoint. The nonresonant identity remains
a self-return and supplies no saving; the resonant denominator remains
unavailable.

The prose after (192.C40b) now states that the endpoint translations "need
not coincide." This is precisely the lawful conclusion: equality is not
structurally enforced, but exceptional equality is not excluded.

### 3.5 Endpoint number/divisor translations (192.C40a)--(192.C40b)

Set

\[
 x:=\rho\Delta=c+U\ell,
 \qquad
 y:=\gamma\Delta=d_v+v\ell.
\]

With \(A_0=\kappa gU\) and \(C_v=\kappa v\), the new tables consist
exactly of the four linear translations

\[
 (2A_0y,0),
 \qquad
 (2gC_vx,2gx),
 \qquad
 (-2gC_vx,-2gx),
 \qquad
 (-2A_0y,0).
\]

Thus the plus \(i=0\) row is the negative of the minus \(i=1\) row, and
the plus \(i=1\) row is the negative of the minus \(i=0\) row. The number
and divisor signs are synchronized, the zero divisors remain zero, and all
entries are integral. The \(y\)-translation contains
\(d_v=cn+d\), so it remains representative-dependent exactly as claimed.

These tables are algebraically consistent with the two determinant
translations in (192.C35). Their identification with the inherited ordered
endpoint fields is a full-context connector already declared by the
candidate; nothing in the repaired tables conflicts with the blind
factorization or its method boundary.

### 3.6 Rigorous ambient interpretation of (192.C41)

The repaired control explicitly assumes

\[
 1\leq T<\frac{U-1}{2}
\]

and an ambient prime-modulus universe in which the two inherited fast
predicates leave \(\asymp U\) central residue classes. A fixed covector
meets only \(O_\eta(TX^\eta)\) such classes by the already proved divisor
count. Hence a coefficient-blind cover by \(M\) covectors satisfies

\[
 M\gg_\eta\frac{U}{TX^\eta}.
\]

The unsaturated premise makes the floor term in \(T\) active. Since
\(T\geq1\),

\[
 T\leq\frac{QmU}{Y}<T+1\leq2T,
\]

and therefore

\[
 \frac{U}{TX^\eta}
 \asymp\frac{Y}{Qm}X^{-\eta}.
\]

This proves the displayed scale in (192.C41). The candidate now labels the
argument a residue-universe mechanism control, not a masked-literal-core
lower bound. It therefore neither divides by zero nor overclaims literal
mass.

## 4. First doubtful or unproved step

After the repairs, the first unproved mathematical step is again exactly
the declared core estimate

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon,
\]

or its assembled version (192.C15). Neither (192.C41) nor the endpoint
tables claim to prove it.

The provenance of the accepted endpoint definitions, affine sign rule,
terminal/Fejer positivity, and outer ledger remains assigned to their
full-context seams. This is not a remaining defect in the five repaired
formal statements; it is the same explicit dependency boundary recorded in
the prior blind review.

## 5. Control tests and outcomes

1. `T_zero_and_C14_scope` — **PASS.** The boxed coverage statement now
   includes \(T\geq1\); \(P_A=0\) remains exact at \(T=0\).
2. `ell_zero_scope` — **PASS.** The algebraic ell-zero fact is retained, and
   its coverage use is confined to the \(T\geq1\) paragraph.
3. `fixed_vs_outer_C12` — **PASS.** Fixed and global aggregates are now
   separately and consistently typed.
4. `one_outer_operation` — **PASS.** The outer assembly is applied linearly
   only after the complex fixed-packet decomposition.
5. `canonical_anchor_interval` — **PASS.** The unique representative is in
   \([0,U)\).
6. `theta_signs` — **PASS.** The repaired definition gives exactly
   \(\{-1,0\}\) for plus and \(\{0,1\}\) for minus.
7. `affine_parity_connector` — **PASS as an exposed inherited connector.**
   The parity rule is now stated separately from the congruence argument.
8. `zero_extended_long_Abel` — **PASS.** Finiteness/absolute summability,
   all integer heights, and zero extension are explicit.
9. `endpoint_wording` — **PASS.** "Need not coincide" makes no universal
   inequality claim.
10. `endpoint_translation_C40a` — **PASS algebraically.** Its two rows are
    the positive \(y\)- and \(x\)-translations dictated by (192.C35).
11. `endpoint_translation_C40b` — **PASS algebraically.** It is the exact
    orientation-swapped negative table.
12. `representative_dependence` — **PASS.** The \(d_v\) term is explicit.
13. `C41_unsaturated_scope` — **PASS.** It excludes \(T=0\) and saturation.
14. `C41_cover_lower_bound` — **PASS.** Both ambient-set size and
    per-covector capacity are stated, giving the displayed lower bound.
15. `C41_literal_quarantine` — **PASS.** The result is diagnostic only and
    is not used as literal lower mass or a disproof of the open core.
16. `downstream_scope` — **PASS.** The complete rho-large packet and all
    downstream owners and exponents remain unchanged.

No computation or external source was used.

## 6. Dependencies and exact artifacts used

This verification used only:

- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/candidates/formalized_hard_m1_t1_rho_large_farey_covector_reduction.md`,
  SHA-256
  `9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5`;
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/blind_post_unmask_farey_covector_verification.md`,
  SHA-256
  `428f35a30ca5277297f921edae7ca4bd7d6f0a8069504e36e393d482d1c42794`.

No new context, sibling report, graph, strategy artifact, control, state file,
kernel, reconciliation, or synthesis was inspected.

## 7. Recommended state effect

**The blind post-unmask seam now passes.** Retain the repaired candidate as
positive evidence for the narrow Farey safe-union reduction and its exact
core/method boundary. Route the explicitly inherited endpoint and outer
connectors through their designated full-context verification before any
graph promotion.

Keep (192.C15)/(192.C42), the complete rho-large remainder, complete
original \(t=1\), every \(t\geq2\) range, all M1 and M2 parents, endpoint
uniformity, M9, both bridges, the quarter target, and every exponent open,
conditional, or unchanged.
