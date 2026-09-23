# Round 197 final-kernel power/operator post-repair verification

- Campaign: m9-m1-t1-p2-four-corner-allocation-commutator-gate
- Role: independent provenance-repair verification
- Starting graph SHA-256:
  b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae
- Repaired durable kernel SHA-256:
  6caf8dc3a027a4548c7059546f117868b45ce51c23f05a5148b78aa995415467
- Numerical theorem evidence: none

## 1. Result

**PASS.**  The prior power/operator/scope PASS remains valid.  A complete
diff of the repaired durable kernel against the final formal candidate
shows only provenance and durable-artifact wording changes:

1. the title and status wrapper identify the file as a proof kernel;
2. the exact final-candidate path and SHA-256 are added;
3. “candidate” is replaced by “kernel” in two scope sentences;
4. claimant and diagnostic paths are expanded to repository-relative
   paths, with all diagnostics explicitly typed diagnostic-only; and
5. the final section heading is changed from proposed state effect to
   dependencies and proof-state boundary.

No mathematical hypothesis, mask, code, coefficient identity, count,
power, selector argument, operator definition, complement, no-go
statement, scope exclusion, dependency theorem, or proposed graph effect
changed.

In particular, the repaired kernel still proves exactly

\[
 |\mathscr R_{\rm core,out}^\sigma(P_{\rm cc}W)|
 +|\mathscr R_{\rm open,out}^\sigma(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\rm sel},\varepsilon}L^2X^\varepsilon
\]

and nothing beyond the common-cell subsector.

## 2. Exact statement and hypotheses

The verified theorem remains the lower-allocation two-cycle on

\[
 P_{\rm cc}
 =P_2\mathbf1_{(m,\beta)=1}
       \mathbf1_{\chi_4(\alpha m)=-1}C_{\rm lit},
\]

with \(C_{\rm lit}\) the arithmetic/live sharp-code equality from
(197.C8a)--(197.C8c).  The physical atom, fixed packet, Farey core,
outer restoration, cap/open partition, physical high source, and safe
projector aggregate remain exactly (197.C9a)--(197.C9k) and
(197.C28a).

The fixed parameters are still \(B>0\), \(K_{\rm sel}>0\), and
\(C_0\ge2\).  The implied constants remain uniform in
\(X,L,\sigma,\kappa,Y,\mathfrak m,q,a,J\) and every orientation,
anchor, Fourier copy, and literal cell.

The accepted logical prerequisites remain the Round-184 coefficient and
selector kernel, Round-185 source/exit kernel, Round-193 physical-mask
kernel, and Round-195 capacity/packet kernel.  The newly expanded report
and control paths are provenance only and are not substituted for those
accepted theorem interfaces.

## 3. Verification

### 3.1 Exact diff classification

The repaired kernel was compared line-by-line with the final candidate
at SHA-256
285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0.
The diff has only five localized provenance hunks:

- line 1: artifact title;
- the header status block: final-candidate path/hash and kernel status;
- Section 6 introduction: “candidate” to “kernel”;
- Section 6 evidence block: fully qualified report/control paths and
  diagnostic-only typing;
- Section 7 heading: durable proof-state wording.

Sections 1--5, including every displayed equation (197.C1)--(197.C37),
are unchanged.  The numbered state-effect list below the renamed Section
7 heading is also unchanged.

### 3.2 Exact \(D_L\) ledger

The raw physical count remains

\[
 \mathcal C_\kappa\ll D_L(1+L/\kappa)^2,
\]

\[
 \sum_{\kappa\ll L}\mathcal C_\kappa
 \ll D_L\{L+L\log(2L)+L^2\}
 \ll D_LL^2X^\varepsilon.
\]

The actual common-cell smooth difference remains
\(O_\varepsilon(D_L/L\,X^\varepsilon)\), giving

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon\ll L^2X^\varepsilon.
\]

The normalized-BV increment multiplicity remains \(O(D_L^2)\), and
the \(O(LX^\varepsilon)\) upper completions give the same
\(D_L^2LX^\varepsilon\) bound.  Since \(D_L^2\le4L\), no positive power
is absorbed into \(X^\varepsilon\).  None of these lines changed.

### 3.3 Selector bounded-shell control

The selector truth table and exact product rule are unchanged.  The
selector commutator can occur only when exactly one selected prime lies
in bounded \(g\).  With

\[
 \delta_{G_0}
 =\min_{\substack{p\le G_0\ {\rm prime}\\q\ne p\ {\rm prime}}}
 |\log(q/p)|>0,
\]

it vanishes once
\(K_{\rm sel}L^{-1/2}<\delta_{G_0}\).  On the remaining bounded shells,
\(D_L=O_{K_{\rm sel},G_0}(1)\), so the raw count is already
\(O_{K_{\rm sel},\varepsilon}(L^2X^\varepsilon)\).  The repaired
provenance block neither changes this threshold nor adds a hidden
constant.

### 3.4 Masked outer passage

The repaired kernel still applies the mask to the physical parent before
Fourier, height, Farey, or packet operations.  It retains:

- the full \(T=0\) branch and all simultaneous strict \(T\ge1\)
  conditions;
- the \(\mathfrak m^{-1}\) lift, anchor, band, divisor, shell, dyadic,
  orientation, and zero-extension weights;
- the exact transported mask commutator, births, deaths, carries,
  unequal translations, phases, cells, and crossings;
- the identity

\[
 \mathscr R_{\rm core,out}^\sigma(MW)
 =\mathscr H_{\rm out}^\sigma(MW)
  -\mathscr S_{\le192,\rm out}^\sigma(MW);
\]

- and the exact cap/open partition of that same recomputed masked core.

The Round-195 safe packet union is still subtracted only after the
complete physical pairing and masked-core passage.  No fixed-component
modulus is introduced, and the single real part remains outside the
complete complex outer assembly.

### 3.5 Complement, no-go, and scope

The exact partition remains

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\rm lit}
       \ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}.
\]

Only \(P_{\rm cc}\) is proved target-safe.  The aligned-face identity

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}<0
\]

still quarantines the sharp-face complement at full
\(D_LL^2X^\varepsilon\) capacity.  The kernel still infers no
nonemptiness, nonvanishing, density, or lower mass.

The scope exclusions and all exponent records are identical to the
previously reviewed kernel.  The new proof-state heading is more
accurate and does not promote a parent or create a reverse dependency.

## 4. First doubtful or unproved step

There is no doubtful step caused by the provenance repair.  The first
unproved mathematical step remains a target bound for

\[
 P_{\partial\rm lit}\ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}
\]

inside the Round-195 open packet region.  The current common-cell
mechanism cannot cross an aligned sharp face with a \(D_L/L\) gain.
Any extension requires a new literal transversality/continuity theorem
or a different signed mechanism.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current kernel hash | **PASS.** It is exactly 6caf8dc3a027a4548c7059546f117868b45ce51c23f05a5148b78aa995415467. |
| Full diff against final candidate | **PASS.** Only five provenance/status hunks occur. |
| Equations (197.C1)--(197.C37) | **PASS.** All are unchanged. |
| Raw and saved \(D_L\) powers | **PASS.** \(D_LL^2\) raw and \(D_L^2L\ll L^2\) after smooth/BV control. |
| Selector threshold | **PASS.** Same large-shell vanishing and \(K_{\rm sel}\)-bounded-shell payment. |
| Physical-mask timing | **PASS.** Mask remains on the parent atom before every spectral operation. |
| Source/safe/core identity | **PASS.** Exact outer subtraction is unchanged. |
| Cap/open packet subtraction | **PASS.** Same linear operator and one final real part. |
| Complement and aligned-face quarantine | **PASS.** Exact partition and no mass inference unchanged. |
| Dependency provenance | **PASS.** Accepted kernels remain logical prerequisites; report/control paths are evidence only. |
| Scope and state boundary | **PASS.** Only the subordinate common-cell node is supported. |

## 6. Dependencies and exact artifacts used

The repaired durable kernel was inspected and diffed in full:

- proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md,
  SHA-256
  6caf8dc3a027a4548c7059546f117868b45ce51c23f05a5148b78aa995415467.

It was compared against the final candidate:

- rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md,
  SHA-256
  285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0.

The prior durable-kernel power review was:

- rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/final_kernel_power_operator_scope_review.md,
  SHA-256
  b87d83dee94335430b9660cce6e54c014ae348909d0e19aa7f4bdf5f7bb47755.

The previously reviewed kernel hash was
d3d6ac897e8a193be83820136eab28d0b55eaff030351d060e72b4524d413cc9.
The current diff against the unchanged final candidate isolates every
change made after that review.

No web source, numerical computation, shared state, or sibling artifact
was used as theorem evidence.

## 7. Recommended state effect

**PASS: retain the prior narrow kernel recommendation unchanged.**
Subject to the remaining final reviews and a mechanically valid State
Patch, the repaired kernel may serve as durable proof evidence for one
subordinate proved_internal \(P_{\rm cc}\) node.

Leave the accepted Round-184, Round-185, Round-193, and Round-195 nodes
unchanged.  Do not change any parent, bridge, theorem, endpoint-uniformity
claim, or exponent.  Record the exact complement only in the new node
and the open owner's next action.

The route-wide terminal label remains
p2_four_corner_orbit_boundary_self_return_no_go.
