# Postapplication independent reverse/replay audit

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Role: independent postapplication State Patch audit
- Starting graph SHA-256:
  815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89
- Terminal State Patch SHA-256:
  8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e
- Live applied graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2

## 1. Result

**Verdict: PASS.**

The canonical live graph is the exact production application of the
terminal Round-195 patch.  The application metadata recovered from the
live records is:

- round index: \(195\);
- timestamp: \(\texttt{2026-08-30T04:40:21}\); and
- judge reference:
  \(\texttt{rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor\_round195\_adjudication.md}\).

The declared inverse recovers canonical starting bytes at
\(815c15c4\ldots\).  Production replay with those exact metadata reproduces
the live bytes at \(f1f6bd2c\ldots\).  Operation counts and ordered result
IDs are exactly
\[
 (1\ {\rm create},\ 1\ {\rm update},\ 0\ {\rm correct\_rejected},
   23\ {\rm reject},\ 27\ {\rm no\_change}).
\]
No authoritative state was edited by this audit.

## 2. Exact statement and hypotheses

The audit treats the live graph as the alleged application of the exact
terminal patch named above.  Its only created obligation is
\[
 \texttt{M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors},
\]
with status \(\texttt{proved\_internal}\) and dependency
\[
 \texttt{M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector}.
\]
Its only updated pre-existing obligation is the still-open owner
\[
 \texttt{M9-M1-hard-top-high-radical-small-t-residual-estimate}.
\]
The update is limited to one added dependency, 20 inconclusive owner
evidence values, the stated next action, and production last-updated
metadata.  The patch also appends 23 rejected-claim records and declares 27
pre-existing obligations unchanged.

The verification hypotheses are purely mechanical: strict patch JSON,
canonical graph serialization, the repository production parser,
validator, merger, and serializer, and the inverse values explicitly
stored in \(\texttt{reversibility}\).  No mathematical claim is inferred
from a report alone.

## 3. Proof and derivation

### 3.1 Recovering the actual application

The raw live file is byte-identical to the production serialization of its
parsed graph and hashes to
\[
 f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2.
\]
The created node, updated owner, and all 23 appended rejection records carry
the same Round-195 timestamp \(\texttt{2026-08-30T04:40:21}\).  The sole
production-only evidence value on the created node is the conductor
adjudication path quoted in Section 1; every appended rejection record has
exactly that one judge-evidence value.  The judge file exists.

The live created object equals the patch object plus exactly the production
round, timestamp, and judge merge.  The last 23 rejected-claim objects equal
the patch records plus exactly those metadata and the judge evidence, in
patch order.  The entire pre-existing rejected-claim prefix remains deeply
equal.

### 3.2 Exact reversal

In memory I applied the patch's inverse recipe:

1. remove the one created obligation;
2. remove the 23 introduced rejected-claim records;
3. remove the one owner dependency and all 20 owner evidence values added by
   the patch;
4. restore the recorded owner \(\texttt{next\_action}\); and
5. restore owner metadata
   \(\texttt{last\_updated\_round}=194\) and
   \(\texttt{last\_updated\_at=2026-08-30T02:58:26}\).

The resulting production serialization hashes to
\[
 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89,
\]
exactly the patch's declared starting hash.  The recovered graph passes the
production graph validator.

### 3.3 Production replay and mutation scope

I then invoked the production \(\texttt{apply\_state\_patch}\) function on
the recovered graph with round \(195\), recovered timestamp
\(\texttt{2026-08-30T04:40:21}\), and the recovered judge reference.  The
returned operation lists have exact ordered sizes \(1/1/0/23/27\) and exact
ordered IDs.  The replayed canonical bytes are byte-for-byte identical to
the live graph and therefore have the same SHA-256
\(f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2\).

Among all pre-existing obligations, only the declared owner differs between
the recovered starting graph and the live graph.  Its exact changed keys are
\(\texttt{dependencies}\), \(\texttt{evidence}\),
\(\texttt{next\_action}\), \(\texttt{last\_updated\_round}\), and
\(\texttt{last\_updated\_at}\).  Its status remains \(\texttt{open}\).
All 27 no-change obligations are deeply equal.  No statement, owner, type,
track, status, implication, blocker, theorem endpoint, bridge, or exponent
field on any pre-existing obligation changed.

In particular, \(\texttt{M9-M1}\), \(\texttt{M9-M2}\), endpoint
uniformity, \(\texttt{M9}\), and \(\texttt{GC-target}\) remain open; both
bridge records remain \(\texttt{derived\_under\_assumptions}\).  The
internal exponent remains \(1/3\), the external benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).

### 3.4 Dependency, cycle, and evidence integrity

Every live dependency, implication, and blocker reference resolves.  The
new node depends on the accepted Round-193 node, and the open owner depends
on the new node.  Neither touched node lies in a dependency cycle.  The
starting and live dependency graphs have exactly the same three inherited
two-node strongly connected components, so application introduced no cycle.

The patch has 40 evidence placements over 20 unique repository-relative
paths; all 20 files exist.  The live created-node bucket counts are
\(15/0/6\) positive/negative/inconclusive: the sixth inconclusive value is
the production judge receipt.  All 20 patch values appear on the open owner
as inconclusive evidence, and neither touched node has a duplicate within
an evidence bucket.  The judge path also appears as positive claimant-chain
evidence on the created node, so its additional inconclusive occurrence is
the deterministic production receipt rather than a missing or replay-drifted
classification.

## 4. First doubtful step or caveat

There is no application defect.

The full graph retains three pre-existing two-node dependency components:

1. \(\texttt{M9-M1-lower-far-cone-microscopic-cell-reduction}\) with
   \(\texttt{M9-M1-lower-post-collar-smoothed-far-alias-reduction}\);
2. \(\texttt{M9-M1-lower-height-alias-rank-one-product-fibre-obstruction}\)
   with \(\texttt{M9-M1-lower-incomplete-fibre-dispersion-obstruction}\);
   and
3. \(\texttt{M9-M2-hard-top-product-fibre-mean-obstruction}\) with
   \(\texttt{M9-M2-hard-top-product-fibre-transform-self-return}\).

They are identical before and after Round 195 and are unrelated to the
touched nodes.  The only evidence-bookkeeping nuance is the cross-bucket
judge receipt described in Section 3.4; production replay reproduces it
exactly.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| terminal patch hash | PASS. \(8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e\). |
| live graph hash/canonical bytes | PASS. \(f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2\). |
| application metadata | PASS. Round 195, timestamp \(2026\text{-}08\text{-}30T04{:}40{:}21\), exact existing adjudication judge reference. |
| operation counts and order | PASS. Exact \(1/1/0/23/27\) and exact ordered IDs. |
| canonical inverse | PASS. Exact starting bytes/hash \(815c15c4\ldots\). |
| production replay | PASS. Byte-identical live graph/hash \(f1f6bd2c\ldots\). |
| created record | PASS. Patch content plus only production metadata/judge merge. |
| owner mutation scope | PASS. Only five declared operational/metadata keys changed; status remains open. |
| rejection disposition | PASS. Exact 23-object tail; prior prefix deeply equal. |
| no-change objects | PASS. All 27 deeply equal. |
| dependency/reference integrity | PASS. All references resolve. |
| cycle control | PASS with inherited-state disclosure. No new component. |
| evidence paths and buckets | PASS. All 20 unique paths exist; no within-bucket duplicate. |
| theorem/exponent quarantine | PASS. No parent, bridge, endpoint, target, or exponent field changed. |
| authoritative-state mutation by audit | PASS. None. |

## 6. Exact dependencies and artifacts used

This audit used only:

1. \(\texttt{state/proof\_obligations.yml}\) at live SHA-256
   \(f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2\);
2. the Round-195 \(\texttt{state\_patch.json}\) at SHA-256
   \(8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e\);
3. \(\texttt{math\_collab/proof\_obligations.py}\) at SHA-256
   \(384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437\);
4. the patch-named 20 unique Round-195 evidence files, including the durable
   kernel, candidate, reports, reviews, launch control, synthesis, and
   conductor adjudication.

The reconstructed starting graph was held only in memory.  Its exact
canonical hash is the declared
\(815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89\).

## 7. Recommended state effect

Retain the applied Round-195 graph unchanged and record this audit as
postapplication PASS evidence.  The subordinate P2 absolute-capacity node
is lawfully \(\texttt{proved\_internal}\), while its hard-M1 owner remains
open with the exact strict packet complement.  No parent, bridge, endpoint,
target theorem, or exponent is promoted by this audit.
