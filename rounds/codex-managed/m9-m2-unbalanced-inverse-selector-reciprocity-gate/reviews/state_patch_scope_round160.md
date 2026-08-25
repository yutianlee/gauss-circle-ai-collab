# Round 160 terminal State Patch scope review

- Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`
- Round: 160
- Task: `round160_state_patch_scope_review`
- Role: terminal independent State Patch, dependency, evidence, and scope reviewer
- Access mode: post-unmask full patch review
- Claimant/reviewer status: independent reviewer; review evidence only; no shared-state edit
- Generated at: 2026-08-25T19:22:00+08:00
- Starting graph SHA-256:
  `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`
- Patch reviewed:
  `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/state_patch.json`
- Allocation: 100% analytical, algebraic, source-scope, and graph review;
  0% numerical experimentation

## 1. Result

**Terminal verdict: GREEN. No State Patch repair is required before
application.**

The patch is a faithful and deliberately narrow encoding of the accepted
Round-160 kernel. It creates one `proved_internal` route-scoped
obstruction, updates four directly affected interfaces, records fifteen
false inferences, and explicitly leaves eleven owner, downstream, and
exponent records unchanged. It changes no existing status, blocker,
positive owner estimate, strict range, endpoint theorem, bridge, target,
or exponent.

The current proof-graph hash equals the campaign's frozen starting hash.
Every created dependency exists. The sole new dependency insertion, from
`M9-M2-smooth-unbalanced-three-quarter-estimate` to the new obstruction,
introduces no cycle: none of the new obstruction's eight accepted
dependencies reaches that open target. The three remaining updates add
only evidence and next-action text. Every evidence path exists, including
this review after its creation. The independent dry validator returns
`Patch OK`, and the unmodified graph validator exits successfully.

The patch promotes only exact reciprocity, exact finite inverse-residue
matrix algebra, exact long-frequency compression, pointwise strict-region
power comparisons, and failure of the explicitly audited scalar routes.
It does not promote a lower bound for the signed owner or literal weighted
matrix and does not obstruct a theorem acting on the coupled weighted
matrix before positive norms.

## 2. Exact statement and hypotheses reviewed

The created record is
`M9-M2-unbalanced-inverse-selector-reciprocity-projective-obstruction`.
It retains

\[
 X=N_0+\xi,\qquad D=X^\delta,\qquad L=X^\ell,\qquad
 R=X/D,\qquad K=XL/D^2,\qquad \Delta=D/L,
\]

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 a=\delta-\ell,
\]

together with the frozen strict-polytope inequality, odd (g,n), arbitrary
parity of (j), ((j,n)=1), arbitrary ((N_0,n)), the literal moving
support and zero extension, both character directions, all profiles and
endpoints, and the complete centered range (1\le h<n).

For arbitrary inverse representatives the exact identity is

\[
 e(-h\overline j_n/n)
 =e(h\overline n_j/j-h/(jn)).
\tag{160.SP1}
\]

The literal centered summand retains the factor (1/(gnj)),
\(\chi_4(g)\chi_4(n)\), the real-centre and correction phases, the moving
profile, and (S(N_0,h;n)). Complete (h\bmod n) summation reconstructs
the original reciprocal row exactly; the accepted (h=0\pmod n)
Ramanujan row is removed once, while positive (h=mj<n) remain.

For (A\subseteq(\mathbb Z/j\mathbb Z)^\times), (M=|A|), and

\[
 F_{j,A}(u,h)=e(h\overline u_j/j),
 \qquad u\in A,\quad 1\le h\le j-1,
\]

the promoted finite identity is

\[
 F_{j,A}F_{j,A}^*=jI_M-\mathbf1\mathbf1^*.
\tag{160.SP2}
\]

Thus the singular values are (sqrt j) with multiplicity (M-1) and
(sqrt{j-M}) once. Exact Hilbert rank-one scalarization followed
termwise by triangle pays at least the nuclear norm. For all unit classes,
the resulting nuclear-to-Hilbert--Schmidt inflation is
(j^{1/2-o(1)}). The normalized full positive residue block has
orthonormal rows.

The complete physical range also has

\[
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}
 \asymp\sqrt\Delta.
\tag{160.SP3}
\]

At (g=1), (j\asymp K), the two capacities
(K^{1/2-o(1)}) and (X^{a/2}) exceed the missing factor at every fixed
strict exponent pair. The statement correctly disclaims a margin uniform
up to (delta=1/2).

## 3. Proof, dependency, and State Patch derivation

If (u=\overline j_n) and (v=\overline n_j), then
(ju+nv-1) is divisible by both coprime integers (j,n), hence by
(jn). This proves (160.SP1), is independent of the representatives,
and uses no parity restriction. Additive orthogonality in a complete
(h\bmod n) system gives the exact self-return and isolates only the
single (h=0\pmod n) row.

For (u,v\in A), summation over (1\le h\le j-1) gives (j-1) on
the diagonal and (-1) off the diagonal, proving (160.SP2). Its
eigenvalues are (j) on the orthogonal complement of the all-ones vector
and (j-M>0) on that vector. The nuclear norm is the projective infimum
for exact Hilbert rank-one decompositions, so the patch's lower price is
exactly scoped to scalarization plus termwise triangle. The accepted
divisor bound implies

\[
 j/\varphi(j)\le2^{\omega(j)}\le d(j)\ll_\varepsilon j^\varepsilon,
\]

which supplies the stated (j^{1/2-o(1)}) inflation without a hidden
totient input. Disjoint supports of the residue-compression rows prove
(160.SP3), including sharpness.

The new node depends only on eight existing accepted records: the exact
fixed-centre return, flat-wave envelope, Round-135 dispersion obstruction,
Round-143 level-four matrix obstruction, character factor, elementary
divisor bound, and the two relevant source audits. Redundancy between the
dispersion and level-four dependencies is harmless. Adding the new node as
a dependency of the open strict-UNBAL target cannot create a return path,
and the patch correctly avoids adding the reverse dependency to the
Round-135 or Round-143 obstruction nodes.

The source-specific sentence is supported by a distinct primary-source
report and independent source/level review. It is explicitly confined to
the named scalar interfaces and their printed hypotheses. The patch does
not turn finite high additive bandwidth into an automatic automorphic
Sobolev loss and does not turn source no-match into a universal vector
impossibility theorem.

## 4. First doubtful or unproved step

The first unproved transfer is from the exact unweighted kernel to the
literal weighted owner. The frozen hypotheses supply support, upper size,
regularity, and zero extension, but no complete unit-class interval on
which the joint profile is quantitatively bounded away from zero. Even a
future lower-buffer lemma would not imply that entrywise interaction with
(S(N_0,h;n)) preserves the unweighted nuclear lower bound.

The first open positive step is therefore a signed vector-valued estimate
for the complete literal ((g,n,j,h)) matrix before every positive norm,
covering all (1\le h<n), moving boundaries, gcd and two-adic strata,
characters, induced levels, and spectral pieces, with the required
(X^{\mu(a)}) saving. Round 160 neither proves nor rules out such a
theorem. This open step is stated in the kernel, adjudication, controls,
synthesis, created node, update text, and rejected-inference ledger, so it
is not a defect in the patch.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Starting graph hash | **PASS.** It equals the frozen Round-160 hash. |
| JSON and patch schema | **PASS.** The file parses, and the dry validator returns `Patch OK`. |
| Created dependency existence | **PASS.** All eight dependencies exist with accepted statuses. |
| New-cycle check | **PASS.** No new dependency path returns to the open strict-UNBAL target. |
| Evidence paths | **PASS.** All referenced artifacts exist once this review is written. |
| Reciprocity, representatives, and parity | **PASS.** Exact and parity-free. |
| Literal scalar and complete reconstruction | **PASS.** Both characters, normalization, support, endpoints, arbitrary gcd strata, and single zero-row deletion are retained. |
| Unweighted matrix spectrum and projective price | **PASS WITH SCOPE.** Exact Hilbert scalarization plus triangle only. |
| Long-(h) complement | **PASS WITH SCOPE.** Sharp operator capacity, not a signed lower bound. |
| Boundary power | **PASS POINTWISE.** No open-face-uniform margin is claimed. |
| Source seam | **PASS WITH NAMED-ROUTE SCOPE.** Growing levels, long-row coverage, character encoding, and theorem hypotheses remain charged. |
| Weighted matrix and bespoke vector theorem | **QUARANTINED/OPEN.** No lower bound or impossibility is promoted. |
| M9--M1 and other M9--M2 owners | **NO CHANGE.** The patch transfers no result outside this flat strict-UNBAL surface. |
| Endpoint, M9, bridge, target, and exponents | **NO CHANGE.** The internal exponent remains (1/3); the separately audited external exponent also remains unchanged. |

No numerical experiment was used as evidence.

## 6. Dependencies and exact artifacts used

This review read and used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/state_patch.json`;
- `proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/controls/conductor_round160_controls.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/conductor_round160_adjudication.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/post_blind_reciprocity_projective_seam.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/exact_kernel_power_review.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/source_level_seam_review.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/scope_hygiene_review.md`.

The exact mathematical dependencies are those listed in the created graph
record. The source statements enter only through the two accepted source
audit nodes, the Round-160 primary-source report, and the independent
source/level seam. No computation, proof draft, validation matrix, or
post-patch state was used as mathematical evidence. No shared graph,
kernel, patch, synthesis, control, or proof-draft file was edited.

## 7. Recommended state effect

**Apply the State Patch unchanged.** Create the one narrow obstruction,
add it only to the open strict-UNBAL target, update the three inherited
interfaces by evidence and next-action text, record the fifteen rejected
overclaims, and preserve every explicit no-change decision.

Close Round 160 under
`inverse_selector_projective_capacity_no_go`, defined only as failure of
low-cost exact unweighted Hilbert common-test scalarization plus termwise
triangle together with the named audited scalar realizations. Park this
scalar surface. Reopen it only for a genuinely new signed complete-matrix
vector theorem; otherwise rotate to a different mandatory M9--M2 owner.

Do not promote `M9-M2-smooth-unbalanced-three-quarter-estimate`, any strict
M9--M2 range, `M9-M2`, `M9-M1`, endpoint uniformity, `M9`, the conditional
bridge, `GC-target`, or either global exponent. The patch already enforces
all of these quarantines.

## Addendum: 2026-08-25 scope-narrowing precision repair

After this review, the created node's hypothesis line was repaired to state
explicitly the frozen inequality

\[
 178\ell+1638\delta>463.
\]

This is the same hypothesis retained in Section 2 above. It narrows no
accepted conclusion and introduces no dependency, evidence, status, range,
or downstream change. The independent dry validator was rerun against the
unchanged starting graph and again returned `Patch OK`; the graph hash still
equals `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`.
The terminal verdict remains **GREEN: apply the State Patch unchanged from
its repaired form**.
