# Final kernel blind and scope consistency review

## Verdict: PASS

The durable Round-193 kernel is an exact mathematical copy of the final
formal candidate.  No new estimate, hypothesis, implication, or scope
claim was introduced during formalization.

- Kernel:
  `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`
- Kernel SHA-256:
  `4f053d1e0396876877efb1c9631e010f4f17fdd11fba478ca8b5ec95ba5ff5f8`
- Final candidate SHA-256:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Candidate-declared and kernel-declared starting graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`

The kernel hash was independently recomputed and matches the hash supplied
for review.  The formal-candidate hash recorded in the kernel metadata also
matches the current candidate byte for byte.

## Exact copy consistency

Sections 1 through 6 of the kernel and final candidate are byte-identical.
Their common sections-1--6 SHA-256 is

`920e4ccf8fe8a91d2666a613df6b8e3f8b1ca96d6d773ddafb1d01b26ec4d005`.

The complete line diff contains only the declared formalization changes:

1. the title drops “Formal candidate”;
2. candidate-status metadata is replaced by durable-kernel metadata and
   the exact final candidate hash;
3. Section 7 is renamed from “Proposed state effect” to “Dependencies and
   proof-state boundary”;
4. Section 7 changes proposal wording to durable support wording and
   “proposed terminal label” to “Round-193 terminal label.”

The four numbered state effects and the terminal-label value are otherwise
identical.  The final candidate's C10 TeX repair is present in the kernel:

\[
 h=Sv-Uw>0,\qquad r=2\kappa gh<R_0,\qquad S,w>0.
\]

The post-unmask mathematical verdict therefore transfers unchanged; the
intervening candidate repair was typographical and introduced no
mathematical content.

## Blind finite-seam agreement

The durable kernel retains every finite identity independently obtained in
the blind derivation:

- the physical tuple order \((d,m,d',m')\);
- product and phase preservation under
  \(\tau_g(d,m,d',m')=(gm,d/g,gm',d'/g)\);
- gcd preservation, parity, involutivity, and fixed-point exclusion on
  \(k=1\);
- character reversal only on \(r\equiv2\pmod4\);
- the plus-to-minus primitive assignment
  \(U'=v,\ v'=U,\ S'=w,\ w'=S\);
- exact preservation of the positive determinant \(h\);
- floor-safe close counting, including \(F_g=0,1\), \(U=1\), small \(U\),
  and \(D_L\ge U\);
- the determinant range \(r=2\kappa gh<R_0\), which for integral \(r\)
  is consistent with the blind bound \(0<r<L\); and
- the fact that \(k=1\) and \(r\equiv2\pmod4\) are needed for the
  involution/sign seam but not for the stronger absolute double-close
  count.

The kernel's main estimate still uses the unmasked live facts
\(d,m,d',m'\asymp L\), multiplicity-one physical coordinates, and the
accepted linear core interface.  It absolutely counts the full
double-close sector and does not convert the subsidiary involution into a
false cancellation theorem for arbitrary bounded arrays.  Its optional
common-cell/BV discussion remains a separate seam control.

## Operator, complement, and scope

The physical-mask bracket retains the verified convention

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 =\mathscr R_{\rm core}(P_{\rm cl}W),
\]

not multiplication of a completed Abel jump by a post-expansion scalar
mask.  The exact mask commutator, births, deaths, transported sites, and
zero extension remain present.

The complement remains the disjoint first-failure partition

\[
 1=P_{\rm cl}
 +\mathbf1_{|d-gm|>D_L}
 +\mathbf1_{|d-gm|\le D_L}\mathbf1_{|d'-gm'|>D_L}.
\]

Only the \(P_{\rm cl}\) term is proved target-safe.  The kernel expressly
leaves both complements, the complete rho-large core, complete \(t=1\),
all \(t\ge2\) ranges, the large-\(G\) near-resonant complement, every M1
and M2 parent, GAR, endpoint uniformity, M9, both bridges, and the
Gauss-circle target open or unchanged.

The exponent quarantine is exact: internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) are all unchanged.
Section 7 permits only one subordinate strict-sector node, evidence on the
already-open owner, the stated square-root-width method boundary, and
subsidiary algebraic controls.  This is not a new mathematical claim.

The provenance typing is also preserved: the two Round-193 reports are
claimant evidence; the accepted Round-192 parent kernel is prerequisite
provenance rather than claimant evidence; finite computation remains
diagnostic only.

## Qualified blind provenance disclosure

This review does not characterize the blind run as pristine.  The blind
reviewer had previously performed a high-level proof-status audit through
Round 192 before Round 193 launched.  No Round-193 claimant strategy,
report, candidate, control, sibling conclusion, or kernel was seen before
the statement-only blind report was completed.  The candidate was first
seen at the expressly post-unmask stage, and this durable kernel review is
necessarily fully unmasked.

Accordingly the evidence is a disclosed, qualified claimant-blind
finite-seam rederivation with prior Round-192 context, followed by
post-unmask candidate and kernel consistency checks.  It must not be
described as a pristine fresh-context blind run.

## State recommendation

**PASS** the final-kernel blind/scope consistency seam at exact kernel
SHA-256
`4f053d1e0396876877efb1c9631e010f4f17fdd11fba478ca8b5ec95ba5ff5f8`.
Any State Patch must retain the kernel's subordinate strict-sector scope
and leave all parents, bridges, theorem nodes, and exponent records
unchanged.
