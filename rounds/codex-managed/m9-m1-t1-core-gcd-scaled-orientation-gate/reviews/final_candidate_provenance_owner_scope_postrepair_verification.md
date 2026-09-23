# Final candidate provenance and owner-scope post-repair verification

- Round: 193
- Candidate SHA-256:
  756d22a53be2df0f105a8d7a91fe6d4b074a7df2f99b15ab9f259ab1f5911a05
- Verdict: **FAIL**
- Review boundary: repaired formalization regions only; no re-proof or
  self-review of the incidence count.

## Repaired regions that pass

The substantive repairs requested in the provenance review are present:

1. The Round-192 Fourier lift is now \(\mathfrak m\), distinct from the
   physical endpoint cofactor \(m\).  The candidate gives the exact signed
   inverse, \(T\), fixed \(C_0\), \(A\), and the primitive Farey family with
   noncolliding coordinate \(d_0\).
2. The \(T=0\) branch states \(P_A=0\) and retains the whole inherited
   Round-191 rho-large remainder before the Round-193 split.  The
   \(T\ge1\) branch states both
   \[
   |c\beta-d_0\rho|>T
   \quad((c,d_0)\in\mathcal F_A),\qquad
   |\rho|\ge(A+1)(T+1).
   \]
3. The core and masked-safe bounds now carry
   \(\ll_{B,C_0,\varepsilon}L^2X^\varepsilon\).
4. The subsidiary paired identity now defines
   \(P_{\rm sw}=P_{\rm cl}\mathbf1_{(m,m')=1}
   \mathbf1_{r\equiv2\pmod4}\), defines \(\Phi_r(N)\), and restricts the
   sum to \(x\in P_{\rm sw}\).  The ordered coefficient remains upper
   unbarred and lower conjugated on both legs.
5. The common-cell paragraph now assigns \(O(D_L/L)\) only to the uniformly
   \(C^1\) factor \(b^{\rm sm}\) and charges the normalized dyadic-BV factor
   \(\eta_L\) separately.
6. The dependency ledger now distinguishes the direct Round-192 graph
   prerequisite, the Round-185 physical interface, connector proofs reopened
   for deletion stability, and inherited/subsidiary provenance.  The finite
   control and output are named and typed diagnostic-only.
7. The literal physical owner, masked-core operator typing, downstream
   quarantine, and exponent quarantine remain unchanged and correct.

## Remaining exact issues

Two literal provenance/hygiene defects remain.

1. In (193.C3), the source still reads
   \[
   d,m,d',m'\asymp L,qquad |W_x|\ll_\eta X^\eta.
   \]
   Replace the literal text ,qquad by ,\qquad.
2. The heading at line 528 says “The exact claimant evidence paths are” but
   its third bullet is the accepted Round-192 kernel, not claimant evidence.
   Retype this exactly as two ledgers:
   - “The exact Round-193 claimant-evidence paths are:” followed only by the
     discovery and hostile report paths; and
   - “The accepted parent-kernel provenance is:” followed by
     proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md.

The first is a TeX defect; the second is a dependency-type defect.  Neither
changes the mathematical sector, but both must be corrected before this
formal post-repair check can pass.

## Blind lifecycle provenance

The statement-only artifact
rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reports/blind_scaled_orientation_involution_rederivation.md
now exists.  Its dependency section lists only protocol.md and
blind_statement.md.  It also transparently records that the run was not
pristine fresh context because its author had completed a through-Round-192
proof-status audit before Round 193, while affirming that no Round-193
claimant, strategy, candidate, review, control, kernel, graph, or campaign
content was received.  Accordingly, the lifecycle status is **qualified
blind artifact present**; the conductor must decide whether that disclosed
pre-Round-193 context meets the campaign's blind gate.  This post-repair
review records that provenance only and does not adjudicate the blind
report's mathematics.

## Recommended action

Apply the two exact textual corrections above, recompute the candidate hash,
and rerun this narrow post-repair verification.  No owner, downstream, graph,
or exponent change is warranted.
