# Round 187 conductor preapplication State Patch check

## Frozen inputs

- Starting proof graph SHA-256: `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`.
- State Patch SHA-256: `bc0e7ed8dc758ebf35c92475d4ef1955457ea8666e70102670ba33daa40549bd`.
- Durable kernel SHA-256: `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2`.
- Intended operation inventory: one create, one update, zero corrected rejected claims, fourteen new rejected-overclaim records, and twenty no-change decisions.

## Independent audits

- `preapply_independent_reverse_audit.md`, SHA-256 `aabf396c15854b44fe8f68f0a8744773e0bd2ad8b3256582a87a32aa2a682a37`: **GREEN**. The official dry validator passed; the isolated application changed exactly the authorized fields; the declared inverse recovered the starting graph byte for byte; frozen-time replay was deterministic; dependencies, evidence paths, IDs, and cycles passed.
- `preapply_scope_path_second_audit.md`, SHA-256 `53ba67c1e8be795c61479d71629568cd73b37cb1097063ee5b790335eb317f27`: **GREEN**. Every evidence and judge path exists; the owner remains open; protected M9/M1/M2, bridge, theorem, and exponent fields remain unchanged; isolated application, reverse, and replay were byte exact.

## Conductor controls

The conductor reran the exact preapplication checks on 2026-08-29:

- State Patch validation: `Patch OK`.
- Active campaign validation: `Campaign OK`.
- Unit tests: six of six passed.
- Python compilation: passed.
- whitespace/diff check: passed, with only repository line-ending conversion notices.

The patch is therefore authorized only for the exact starting graph and patch hashes above, with `round_index=187` and the Round-187 adjudication as judge reference. The permissible mathematical effect is limited to creating the strict high-height inverse-residue conductor reduction and attaching it as inconclusive progress to the still-open hard-M1 small-`t` owner. No complete relation, parent, bridge, theorem, or exponent may change.

