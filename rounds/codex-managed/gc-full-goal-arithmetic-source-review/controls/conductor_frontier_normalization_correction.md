# Round220 forward correction of a strategy-table transcription

## 1. Result

Checkpoint217 contains two transcription errors in its M2 UNBAL row.
The graph and accepted proof draft already contain the correct formulas.
Correct forward in checkpoint220; preserve the closed217 archive.
No mathematical state change or exponent improvement is involved.

## 2. Exact authoritative statement

Node M9-M2-smooth-unbalanced-three-quarter-estimate states

    K=XL/D^2, M=LK, K/L>16,
    T_(L,K)=sum_(h~L,k~K) chi4(h) a_(L,K)(h,k) e(sqrt(X h k)),
    T_(L,K) <<_epsilon (LK)^(3/4) X^epsilon.

It remains open. The actual symbol includes every quarter shift/sign,
Vaaler taper, support entry/exit, floor, star and transform boundary term.
The required complete estimate cannot be replaced by a subrange.

## 3. Derivation and reconciliation

I read the named node directly from state/proof_obligations.yml and
checked the corresponding accepted draft's Round160 normalization,
where K=XL/D^2. The round220 full-frontier role independently flagged
the discrepancy while comparing its exact context. The archived217
checkpoint instead printed K=XL^2/D^2 and e(sqrt(X)hk). Both differ
from the authoritative statement, the latter moving hk outside the
square root. These were errors in a summary table, not amendments to
the accepted graph. All220 and later summaries must use section2.

## 4. First doubtful or unproved step

The complete M2 UNBAL estimate in section2 is still unproved. This
transcription correction supplies none of its missing cancellation.

## 5. Controls and outcomes

Graph hash and draft bytes remain pinned. Checkpoint217 and its archive
hash remain unchanged. The active220 frozen objective concerns all live
frontiers and does not introduce an alternative UNBAL normalization;
its task context names the authoritative graph. Zero experiments.

## 6. Dependencies and provenance

Conductor, round220. Graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b;
draft SHA256
65989358d00f0ecf7c4d385ea58bfad09eaa026af98924266207c5f8af872f00;
strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md,
SHA25639054e4123c11b85e55d9146794cfdd7453915ebefd8a1286763e08b4ecabcd2;
named node and accepted draft Round160. Primary source theorem content
is not used in this correction.

## 7. Recommended state effect

No graph patch beyond identity. Record this forward correction explicitly
in checkpoint220, synthesis and the next task's context. Keep both the
unproved estimate and all closed evidence intact.
