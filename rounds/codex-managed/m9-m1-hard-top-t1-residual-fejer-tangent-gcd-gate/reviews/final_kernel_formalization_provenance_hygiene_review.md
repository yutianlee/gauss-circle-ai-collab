# Round 185 final-kernel formalization, provenance, and hygiene review

## 1. Result

**Verdict: GREEN.**

The durable kernel at SHA-256 `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160` passes the frozen-hash, self-containment, formal-literalness, candidate-provenance, blind-attribution, diagnostic-scope, dependency, downstream-quarantine, and artifact-hygiene gates in the brief. This verdict is limited to the finite reduction and strict bounded-height sector stated in the kernel. It does not certify the open global signed estimate or a downstream exponent.

## 2. Exact statement and hypotheses

Fix the source candidate at SHA-256 `74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65` and the starting graph at SHA-256 `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`. Under the kernel's fixed real \(X\ge2\), hard-M1 shell \(L\ge2\), sign \(\sigma\in\{+1,-1\}\), and fixed \(B>0\), together with the literal Round-184 shell, selector, squarefree, coprimality, endpoint, sign, cone, and profile predicates, the durable statement is:

- the endpoint coefficient \(\lambda_{N,\sigma}(d)\), the residual coefficient \(c_{N,\sigma}^{\rm rem}\), and the full-line sequence \(z_N\) are total by explicit zero extension;
- the even-shift Fejér connector is endpoint-exact;
- the monotone sector together with both opposing orientations having \(h\le H_B=\lfloor(\log(2X))^B\rfloor\) has absolute opened-incidence contribution \(O_{B,\varepsilon}(L^2X^\varepsilon)\), as stated in (K185.7);
- after that sector is removed, (K185.36) is the exact multiplicity-one canonical complement, with both orientations under one outer real part; and
- (K185.37), the uniform dyadic signed estimate for \(Y<h\le2Y\), remains open and is not part of the proved kernel.

The sole terminal label is `strict_hard_m1_t1_residual_tangent_gcd_sector`. The direct accepted dependencies are exactly the five listed in the kernel; the small-\(t\) primitive-ray result is routing context, while the M2 tangent, alias, and conductor material is method control rather than an imported M1 theorem.

## 3. Proof or derivation

1. **Definitions and total domains.** The structural parameters are fixed before the statement is used. The residual mask (K185.1) distinguishes no selected pair from a selected pair and has the required \(1,0,0,1\) truth table. The first branch of (K185.2) is restricted to positive squarefree integer endpoints and legal odd divisors; its otherwise branch is zero. Equation (K185.3) separately covers \(N\le0\). The literal symbol is declared zero off every omitted shell, cone, profile, floor, star, half-weight, hard-sample, crossing, endpoint, sign, squarefree, and coprimality predicate, and \(z_N\) is extended to the full integer line. Thus later divisor openings do not widen the coefficient domain.

2. **Finite connector and tangent variables.** The kernel defines \(H_B\) and \(R_0\) before the opened correlation, introduces \(N,d,m,d',m',r\) in (K185.6), and then introduces \(a,b,\alpha,\beta\) before the tangent identities. The original gcd, inward cross gcd, and joint quotient are introduced in order before \(U,S,h\) and the primitive equations. The local cutoff and tail letters occur only as local count thresholds; the theorem-bearing cutoff is the already defined \(H_B\). The odd/even terminal Fejér coefficients, the Cauchy connector, the two tangent identities, and the monotone/opposing partition agree with the source candidate.

3. **Canonical representatives and positivity.** The outer domain (K185.27) makes \(v\) invertible modulo \(U\). For \(U>1\), (K185.30) gives one least-residue anchor for each orientation. For \(U=1\), the kernel does not invoke an inverse and explicitly sets the plus anchor to \((0,-h)\) and the minus anchor to \((0,h)\); these solve the respective primitive equations. Equation (K185.31) then gives one affine index \(t\) and imposes \(S_{t,\omega}>0\) and \(w_{t,\omega}>0\) before either endpoint or square root in (K185.32)--(K185.35) is evaluated. The plus and minus sectors are disjoint by the signs of \((a,b)\), and each legal physical incidence has one orientation and one canonical index.

4. **Endpoint placement and outer real part.** In (K185.33) the plus upper endpoint is the un-conjugated coefficient and the plus lower endpoint is conjugated; (K185.35) makes the corresponding orientation-dependent placement in the minus sector. Both use the positive square-root difference in its rationalized form and the common even-shift weight. Oddness of \(U\) gives \((-1)^{S_{t,\omega}}=(-1)^{S_{0,\omega}+t}\). Consequently (K185.36) contains exactly one real part outside both orientations, all outer labels, and all row indices, rather than separate real parts whose recombination could lose a sign.

5. **Candidate-to-kernel provenance.** The durable header names the exact conductor-owned source path and source hash. The 39 uniquely tagged kernel relations preserve the candidate's residual mask, total endpoint coefficients, parity connector, tangent and gcd identities, bounded-height count, canonical rows, exact complement, open dyadic relation, capacity obstruction, and exact deletion mechanism. Reordering \(H_B\) and the bounded-sector statement into the opening statement supplies definitions earlier and does not strengthen the result. No blind-only formula is promoted into the kernel.

6. **Blind normalization and computation attribution.** The normalized blind report remains bound to post-normalization SHA-256 `0c2e9937ae3b1c31a31fc77d8fdf9c389f3a7869fabded3271d20e11a2ff93c2` and records pre-normalization SHA-256 `a51982e042e34cf36c5310f1f22c376edcbdd7db1b5ad02745ea673cd545547a` with typographic-only edit scope. The reconciliation assigns the canonical-domain correction to the conductor candidate. The durable kernel likewise identifies the conductor candidate as its exact source and describes the stronger tuple as a conductor-reproduced exact-integer control. It explicitly denies profile nonvanishing, lower mass, asymptotic evidence, or a disproof of (K185.37).

7. **Dependencies and quarantine.** The five direct dependencies reproduce the candidate's classification. The small-\(t\) primitive ray remains routing-only; M2 material remains method-only; no external theorem is claimed. The final scope paragraph keeps the complete \(t=1\) residual, all \(t\ge2\) and near-resonant complements, the small-\(t\) owner, both M1 parents, GAR, all M2 parents, endpoint uniformity, M9, both bridges, the Gauss-circle target, and every exponent claim open. The exact terminal-label token occurs once in the durable kernel.

## 4. First doubtful or unproved step

There is no failing formalization or provenance seam in the frozen durable kernel. The first unproved mathematical step is (K185.37): a uniform signed estimate over every dyadic block \(Y<h\le2Y\), with both orientations and every arithmetic endpoint condition still coupled. The kernel correctly records positive capacity \(O(YL^2X^\varepsilon)\), so the missing factor \(Y\) must come from a genuinely global signed theorem. The bounded exact-integer control and bare alternating law do not provide it.

## 5. Required control tests and outcomes

- **Frozen hashes:** the starting graph, source candidate, and durable kernel reproduce respectively `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`, `74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65`, and `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`. Outcome: pass.

- **Exact mechanism control:** the hash-bound control at \((\kappa,u,v,s,w)=(103,7,1,99,14)\) reproduces the live squarefree/coprime site, the adjacent lower-endpoint deletion by \(7^2\), the preserved shift and ratios, the character flip, and canonical indices \(14,15\). Both control and kernel limit this to a deletion mechanism diagnostic. Outcome: pass.

- **Encoding and bytes:** the durable kernel decodes under strict UTF-8, has no BOM, forbidden control byte, replacement character, zero-width character, isolated carriage return, or mixed line ending. It uses LF throughout, has no trailing whitespace, and ends with exactly a newline. Outcome: pass.

- **TeX and references:** there are 81 balanced inline delimiter pairs, 42 balanced display delimiter pairs, and five correctly ordered begin/end environment pairs. All 39 equation tags are unique. Every explicit K185 cross-reference resolves to an existing tag; no duplicate tag or unresolved reference was found. Outcome: pass.

- **Multiplicity and presentation:** the \(U=1\) branch avoids an inverse, positivity precedes square roots, canonical anchors distinguish the two orientations, the complement has one outer real part, and the terminal-label token occurs exactly once. Outcome: pass.

- **Provenance and scope:** source and normalization hashes agree with the reconciliation and post-repair verification; the conductor repairs are not attributed to the blind claimant; the computation remains diagnostic; dependency roles and all downstream open claims remain quarantined. Outcome: pass.

## 6. Dependencies and exact artifacts used

Only the context authorized by the brief was used:

- `protocol.md`, SHA-256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
- `state/active_campaign.yml`, SHA-256 `d67f738e38fcd5288773d12b8b0dc6dd22440f9ebe98bbc0d020cd7b11c82ab6`;
- `state/proof_obligations.yml`, hash-checked only at the frozen starting SHA-256 `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md`, SHA-256 `74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65`;
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`, SHA-256 `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/conductor_round185_report_reconciliation.md`, SHA-256 `8b6bd63dea841c1d11d3c29daa68e8a97aed688b9c473d278958675ef809e198`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/controls/conductor_round185_exact_fibre_deletion_control.md`, SHA-256 `2531efad2e40c77b61985e0e694c11a9683088abc9d82a0a287a676772606999`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reports/blind_residual_fejer_tangent_rederivation.md`, SHA-256 `0c2e9937ae3b1c31a31fc77d8fdf9c389f3a7869fabded3271d20e11a2ff93c2`, recording pre-normalization SHA-256 `a51982e042e34cf36c5310f1f22c376edcbdd7db1b5ad02745ea673cd545547a`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/blind_post_unmask_literal_owner_scope_post_repair_verification.md`, SHA-256 `45d6090fd63925165b4fb917d36a7e8548fd6dba2e0e1fd158786e36bbc598d4`.

The controlling task brief was `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/final_kernel_formalization_provenance_hygiene_review.md`. No source candidate, durable kernel, report, control, graph, proof draft, validation matrix, synthesis, campaign file, or other shared-state artifact was edited.

## 7. Recommended state effect

Promote this review as a passing independent formalization, provenance, and artifact-hygiene gate for the hash-bound durable kernel. The conductor may use that kernel in a mechanically validated State Patch for only its finite reduction, strict bounded-height sector, and exact canonical complement under the sole label `strict_hard_m1_t1_residual_tangent_gcd_sector`. Retain (K185.37) and every quarantined owner, parent, endpoint-uniformity, bridge, terminal, target, and exponent claim in its current open or assumption-qualified state.
