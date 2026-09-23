# Round 188 blind-report control-character repair

- Campaign: m9-m1-t1-high-h-imprimitive-lift-gcd-gate
- Round: 188
- Scope: two exact TeX/control-byte repairs in one statement-only report
- Mathematical effect: none

## Historical and repaired hashes

Historical report:

- path:
  rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/reports/blind_lift_gcd_rederivation.md
- length: 18,435 bytes
- SHA-256:
  a8de6402d8a57d22a773d9b763e195f3e959a1a50cf084bb7ffab7205460231e
- lone carriage-return bytes: 2

Repaired current report:

- length: 18,437 bytes
- SHA-256:
  a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6
- lone carriage-return bytes: 0
- non-whitespace control bytes: 0

## Exact repair

The historical file contained two U+000D bytes created by interpreting
the intended TeX command prefix backslash-r as a carriage return. The
two byte-local substitutions were:

1. the corrupted phrase
   \(\mathfrak f\ {\rm as\ in}\) at historical byte offset 3,930 was
   restored to the same intended visible TeX phrase by replacing the
   lone U+000D before \(m\) with the two ASCII bytes backslash and \(r\);
2. the corrupted phrase \(v,t\ {\rm live}\) at historical byte offset
   13,214 received the identical repair.

Each substitution replaces one byte by two bytes, so the total length
increases by exactly two. No letter, number, formula, inequality,
hypothesis, conclusion, attribution, or scope statement changes.

## Exact reverse check

Starting from the current bytes, replacing the two repaired literal
substrings only,

- backslash-mathfrak-space-f, backslash-space-open-brace,
  backslash-r-m-space-a-s, and
- v-comma-t, backslash-space-open-brace, backslash-r-m-space-l-i-v-e,

by the corresponding historical U+000D forms gives:

- 18,435 bytes;
- exactly two U+000D bytes; and
- SHA-256
  a8de6402d8a57d22a773d9b763e195f3e959a1a50cf084bb7ffab7205460231e.

Thus the repair reverses byte-exactly to the frozen report reviewed by
the original blind-post-unmask and kernel seams.

## Required provenance update

Artifacts that identify the current blind report by hash must use
a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6.
Reviews frozen before this repair remain valid historical evidence only
after a focused post-repair verification confirms the exact two-site
delta and rechecks the current candidate/kernel hashes.

## Scope

The repair does not change the blind report's result. It still verifies
the lift algebra and exact split, retains logarithmic losses in the
formally independent statement-only packet, and leaves the exact
low-gcd complement open. It provides no theorem evidence beyond the
analytical report and changes no graph, campaign, State Patch, owner,
bridge, theorem, or exponent.
