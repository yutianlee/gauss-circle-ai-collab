# Final candidate provenance and owner-scope verification

- Round: 193
- Expected candidate SHA-256:
  ac9998ee1ac18a51993a26c2f6f20f9d711fa829f056878fa25e6c5e71e72f30
- Observed candidate SHA-256:
  ac9998ee1ac18a51993a26c2f6f20f9d711fa829f056878fa25e6c5e71e72f30
- Hash check: **PASS**
- Overall verdict: **FAIL**
- Boundary: exact post-repair formalization, syntax/hygiene, dependency
  provenance, owner scope, and lifecycle provenance only.  The incidence
  count is not re-proved here.

## Repairs verified

All previously requested substantive and provenance repairs pass:

1. The Round-192 Fourier lift \(\mathfrak m\) is distinct from physical
   cofactor \(m\); the candidate states the signed inverse, \(T\), fixed
   \(C_0\), \(A\), \(\mathcal F_A\), and the exact \(T=0/T\ge1\) branches.
2. The masked core and safe bounds carry
   \(\ll_{B,C_0,\varepsilon}L^2X^\varepsilon\).
3. The physical mask is imposed before Fourier expansion and differencing;
   the height-mask birth/death term remains explicit.
4. The subsidiary identity defines \(P_{\rm sw}\) and \(\Phi_r\), sums only
   over \(x\in P_{\rm sw}\), and preserves upper-unbarred/lower-conjugated
   endpoint order.
5. The common-cell paragraph separates \(b^{\rm sm}\) from normalized
   dyadic-BV factor \(\eta_L\).
6. The dependency ledger distinguishes the direct Round-192 prerequisite,
   the Round-185 physical interface, reopened connector proofs, and
   inherited/subsidiary provenance.
7. The Round-193 claimant-evidence list now contains only the discovery and
   hostile reports.  The accepted Round-192 kernel is separately and
   correctly typed as parent-kernel provenance.
8. The diagnostic control is named and remains diagnostic-only.  Owner,
   downstream, graph, and exponent quarantine remain correct.
9. Display and inline TeX delimiters are balanced
   (\(40/40\) display and \(89/89\) inline), and all forty equation displays
   have tags.

## Remaining exact hygiene defect

One unescaped command remains in (193.C10).  The source is

\[
 h=Sv-Uw>0,\qquad r=2\kappa gh<R_0,qquad S,w>0.
\]

The second separator is literal text ,qquad, not the TeX command
,\qquad.  Replace (193.C10) by

\[
 h=Sv-Uw>0,\qquad r=2\kappa gh<R_0,\qquad S,w>0.
\]

A full search finds this as the only remaining unescaped qquad or quad.
Because this is the final syntax/hygiene gate, the present hash cannot receive
PASS despite all mathematical typing and provenance repairs being correct.

## Blind lifecycle provenance

The now-existing statement-only blind report lists only protocol.md and
blind_statement.md as consulted artifacts.  It transparently discloses that
its author had pre-Round-193 through-Round-192 proof-status context, while
also stating that no Round-193 claimant, strategy, candidate, review, control,
kernel, graph, or campaign content was received.  Its status is therefore
**qualified blind artifact present**.  Whether that disclosed pre-Round-193
context satisfies the campaign's blind gate remains a conductor lifecycle
decision; this verification records the qualification without adjudicating
the blind mathematics.

## Required action

Repair the single missing backslash in (193.C10), recompute the candidate
SHA-256, and rerun only the literal hash/hygiene check.  No other
formalization, dependency, owner, downstream, or exponent repair is required.
