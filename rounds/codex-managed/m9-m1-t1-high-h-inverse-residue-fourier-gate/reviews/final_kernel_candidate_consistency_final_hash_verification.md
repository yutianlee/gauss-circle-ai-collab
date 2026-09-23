# Verdict

**GREEN.**  The sole delta from the previously verified kernel is correction
of the two diagnostic-evidence SHA-256 strings.  Every formula
(K187.1)--(K187.27), every carrier and multiplicity statement, every power
ledger, and every proved/open boundary is byte-for-byte unchanged.

# Hash replay

| Artifact | SHA-256 |
|---|---|
| Previous verified kernel | `026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24` |
| Current kernel | `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2` |
| `controls/conductor_round187_wolfram_inverse_residue_check.md` | `032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113` |
| `controls/inverse_residue_exact_check.wls` | `e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd` |

The two control hashes printed by the current kernel agree exactly with the
independently recomputed hashes of those files.

# Exact delta classification

The two previous evidence strings were

- `032d8039636b0e4e2040caed7c0d2ade570761812aed85711930ba37300b176a`;
- `e818367a710c4051f9259966133ca48b9496dfc3d5b8b18d559072cfac4a7d83`.

Replacing the two corrected strings in the current kernel by precisely these
two former strings reproduces SHA-256
`026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24`
exactly, with identical file length.  This mechanically proves that no other
byte changed.  The delta is provenance-only and has no mathematical effect;
the controls remain explicitly diagnostic rather than theorem evidence.

# State recommendation

Retain every prior **GREEN** normalization, carrier, multiplicity, power, and
kernel/candidate-consistency verdict.  Accept the current kernel hash only for
the strict inverse-residue conductor reduction.  Keep (K187.11), the complete
high-height target, all residual parents, bridges, theorems, and exponent
claims open exactly as before.  No repeat mathematical review or state-scope
change is required.
