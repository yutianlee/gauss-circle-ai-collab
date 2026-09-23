# Round 171 State Patch application audit

- Starting graph SHA-256:
  `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Resulting graph SHA-256:
  `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`
- Patch dry validation: PASS
- Independent scope review: GREEN
- Independent downstream graph/cycle review: GREEN
- Application: PASS
- Patched graph validation: PASS
- Exact reverse audit: PASS

The applied mutation created one obligation, updated two obligations,
appended eighteen rejected claims, and changed no other obligation record.
The patched graph contains 375 obligations and 1,371 rejected claims.

For the reverse audit, the created node and eighteen appended rejection
records were removed in memory; the two added dependency/evidence sets were
removed; and the two pre-patch next-action and update metadata records were
restored. The resulting canonical graph serialization has SHA-256

`4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`,

exactly the certified starting hash. The authoritative on-disk graph remains
the applied, validated result at `c98f95b...b54853`.

No dependency-only or combined semantic cycle was added. The three
pre-existing dependency cycles and four pre-existing combined components
are unchanged. Both critical physical nodes remain open, and no parent,
bridge, theorem, or exponent status changed.
