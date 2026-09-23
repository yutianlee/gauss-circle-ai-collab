# Conductor Round-195 preapply validation

- Starting graph SHA-256: 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89
- Terminal State Patch SHA-256: 8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e
- Intended scope: 1 create / 1 update / 0 corrected rejection / 23 reject / 27 no change

## Result

PASS.  The official graph validator reports the starting graph valid and
the terminal State Patch valid.  The six repository unit controls pass.
The unavailable optional pytest runner was not used; the same six tests
were executed through the standard-library unittest runner.

The conductor checked that every one of the 20 evidence paths exists, the
new dependency endpoint exists, the created ID and 23 rejected IDs are
fresh, and the one updated owner is currently open.  The new node depends
only on the accepted Round-193 sector, and the owner depends on the new
node, with no return path and no cycle.

Three independent preapply audits pass:

1. controls/preapply_independent_reverse_replay_audit.md verifies exact
   production simulation, reversal, replay, operation counts, paths, and
   cycles;
2. controls/preapply_hostile_scope_protected_state_audit.md verifies owner,
   downstream, protected-node, rejection, and exponent quarantine;
3. controls/preapply_evidence_provenance_hygiene_audit.md verifies evidence
   classification, claimant receipts, packet notation, and strict
   UTF-8/LF hygiene.

The only preapply repair replaced bare plaintext spectral-gcd placeholders
in five JSON fields, eight token occurrences in total, by the exact
JSON-escaped \(\mathfrak m\) notation.  No operation, dependency, status,
evidence path, scope decision, or mathematical claim changed.

The patch is approved for mechanical application at Round 195 with the
conductor adjudication as judge reference.
