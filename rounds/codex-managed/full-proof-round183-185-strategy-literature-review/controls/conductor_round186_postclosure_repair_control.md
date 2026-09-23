# Round 186 postclosure lifecycle and source-card repair control

- Campaign: full-proof-round183-185-strategy-literature-review
- Round: 186
- Role: conductor record of two bounded repairs found by the first final
  closure-hygiene review
- Graph SHA-256:
  d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a

## Result

Two exact documentary defects were repaired. Neither repair touches the
proof graph, State Patch, analytic status, dependency, implication, blocker,
owner, bridge, endpoint theorem, global theorem, or exponent.

## Repair 1: round-ledger lifecycle pointer

The top-level round-ledger field incorrectly retained
active_round: 184 even though the ledger's final record closed Round 186
and named Round 187 next. It is now active_round: 187, agreeing with
current_round.md, next_campaign.md, next_round_plan.yml, the final ledger
record, and the rule that Round 187 is pending design and not launched.

- historical ledger SHA-256:
  ed96a9bfac0708625de2dd16d299631c98d2013938f849baab29ba674df2f871
- repaired ledger SHA-256:
  5b9b53c9412f9342c769631f3078e095a17a64394ebccb65ed9da9645087e4a5
- exact reversal: replace the unique top-level active_round value 187 by
  184; this recovers the historical bytes and hash.

## Repair 2: source-card theorem transcription

The Milicevic--Robinson--Shupe source card contained an extraneous comma in
the exponent, p^{,n-(...)}. The primary report, source review, and official
Theorem 1.1 all use the correct formula

\[
 p^{n-(n-\Delta^*(\boldsymbol a)-1)/\lceil k/2\rceil+1}.
\]

The source card now matches them.

- historical source-card SHA-256:
  62697c467b0e3a41bca7849187ff29bb04f234d08f768fd068c27e59775c81b7
- repaired source-card SHA-256:
  6e91d2247fd6c8d3ce8fabce1eaea107ec05527549043e04248a949cb29f3559
- exact reversal: insert one comma immediately after the unique opening
  p^{ in the Theorem-1.1 exponent; this recovers the historical bytes and
  hash recorded by both State Patch audits.

## Scope and required verification

The first final hygiene report remains immutable RED evidence for these two
defects. A fresh independent post-repair verification must check both exact
reversals, current lifecycle consistency, source-theorem consistency,
graph and patch hashes, campaign-plan identity, UTF-8 and TeX hygiene,
tests, and every nonpromotion and exponent quarantine before Round 186 is
finally closed.
