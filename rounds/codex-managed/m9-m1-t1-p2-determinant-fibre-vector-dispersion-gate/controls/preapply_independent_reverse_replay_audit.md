# Preapplication independent reverse/replay audit

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Role: independent preapplication State Patch audit
- Starting graph SHA-256:
  815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89
- State Patch SHA-256:
  8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e

## 1. Result

**Verdict: PASS.**

The Round-195 patch is valid against the stated live graph and has exact
operation counts
\[
 (1\ {\rm create},\ 1\ {\rm update},\ 0\ {\rm correct\_rejected},
   \ 23\ {\rm reject},\ 27\ {\rm no\_change}).
\]
All operation IDs are unique and resolve in the correct pre- or
post-application graph.  All 20 unique evidence paths exist.  The one new
dependency is cycle-neutral, all 27 no-change obligations remain deeply
equal, and the production apply/reverse/replay simulation is byte exact.

No state or patch file was mutated.

## 2. Exact patch statement and scope

The patch creates exactly
\[
 \texttt{M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors}
\]
with status \(\texttt{proved\_internal}\) and sole dependency
\[
 \texttt{M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector}.
\]
That dependency exists in the starting graph.  The created ID does not.

It updates exactly
\[
 \texttt{M9-M1-hard-top-high-radical-small-t-residual-estimate}
\]
by:

1. appending the created node to dependencies;
2. appending the 20 Round-195 evidence paths to
   \(\texttt{evidence.inconclusive}\);
3. replacing \(\texttt{next\_action}\); and
4. receiving the production last-updated round and timestamp metadata.

The dependency and all 20 evidence values are absent from the owner before
application, so their inverse removal cannot erase pre-existing data.
The owner already has all three evidence buckets, so production merging
creates no hidden bucket structure.

The 23 reject operations are new rejected-claim records: none is an
existing obligation or an existing rejected-claim ID, every ID is unique,
and every reason is nonempty.  The 27 no-change IDs are distinct existing
obligations and are disjoint from every mutating operation.

The patch is strict JSON with no duplicate keys.  Its top-level and
operation mappings have the production schema, and the created obligation
contains every required field.  The official read-only validator returned
\(\texttt{Patch OK}\).

The terminal notation repair is byte-accounted.  It changes exactly five
JSON string fields, containing eight literal occurrences, from bare
\(\texttt{mfrak}\) to decoded \(\texttt{\\mathfrak m}\).  There is now no
decoded bare \(\texttt{mfrak}\) token.  Replacing only those eight
occurrences in those five fields reconstructs the immediately preceding
patch byte for byte at SHA-256
\(2257205cdedc730a29f84d2f795dd888a1a4443a82c4f5fe8fff543a1f4b3408\).
Thus the repair changes notation only and changes no operation, ID,
dependency, evidence item, status, or disposition.

## 3. Proof and simulation

### 3.1 Hash, references, and evidence

The live graph bytes are already canonical production JSON:
\[
 {\rm SHA256}(\texttt{state/proof\_obligations.yml})
 =815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89.
\]
This equals both the patch's declared starting hash and the SHA-256 of
the production serializer applied to the parsed graph.

After in-memory application, every dependency, implication, and blocker
reference resolves.  The created node depends only on the accepted
Round-193 node; the updated owner depends on the created node.  There is
no path from that prerequisite chain back to either touched node, so the
patch introduces no dependency cycle.

The evidence ledger contains 40 placements but only 20 unique paths:
15 positive and 5 inconclusive entries on the created node, followed by
the same 20 paths as inconclusive evidence on the still-open owner.  All
20 resolve to existing files.  This classification is scope-correct:
the durable kernel and its positive claimant/seam chain support the
subordinate proved node; blind/mechanism/control artifacts remain
inconclusive there; and every Round-195 artifact is only inconclusive
evidence for the unresolved owner.

### 3.2 Production apply and mutation scope

I invoked the repository's production
\(\texttt{apply\_state\_patch}\) function in memory with
\(\texttt{round\_index=195}\) and a fixed diagnostic timestamp.  Its
result lists had exact sizes \(1/1/0/23/27\), in the same order as the
patch.

Among every pre-existing proof obligation, only the declared owner changed.
Its exact changed keys were:

- \(\texttt{dependencies}\);
- \(\texttt{evidence}\);
- \(\texttt{next\_action}\);
- \(\texttt{last\_updated\_round}\); and
- \(\texttt{last\_updated\_at}\).

The created object equals the patch object plus only the production
last-updated metadata.  The existing rejected-claim prefix is deeply equal
and exactly 23 new records are appended.  Every one of the 27 declared
no-change obligations is deeply equal before and after.  Production graph
validation reports no issue after application.

### 3.3 Exact reverse

The declared inverse recipe is complete:

1. remove the one created obligation;
2. remove the 23 rejected-claim records introduced by this patch;
3. remove the one added dependency and all 20 added owner-evidence values;
4. restore the recorded owner \(\texttt{next\_action}\); and
5. restore
   \(\texttt{last\_updated\_round}=194\) and
   \(\texttt{last\_updated\_at=2026-08-30T02:58:26}\).

Applying that recipe to the simulated graph yielded byte-for-byte canonical
starting JSON and starting SHA-256
\[
 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89.
\]

### 3.4 Replay

With diagnostic timestamp
\(\texttt{2026-08-30T12:34:56}\) and no judge reference, the simulated
applied SHA-256 was
\[
 64c8f486874c4532c7179b6ff0b1bb2422512b403f74c9c09fb9f67271373013.
\]
Production replay from the exact reversed graph reproduced those applied
bytes and that hash exactly.

I repeated the simulation with the existing Round-195 conductor
adjudication path as a nonempty judge reference.  The simulated applied
SHA-256 was
\[
 62011ef885a01ddf5a6a8eb98943198d555b6d1e74e002a8f8d0adb9cc0bd619.
\]
The judge evidence was added exactly where production specifies, the same
inverse again recovered the exact starting bytes, and replay again
reproduced the applied bytes exactly.  These two applied hashes are
diagnostic because the eventual production hash depends on its actual
timestamp and judge reference.

## 4. First doubtful step or caveat

There is no patch defect.

The full starting graph contains three inherited two-node dependency
strongly connected components:

1. \(\texttt{M9-M1-lower-far-cone-microscopic-cell-reduction}\) with
   \(\texttt{M9-M1-lower-post-collar-smoothed-far-alias-reduction}\);
2. \(\texttt{M9-M1-lower-height-alias-rank-one-product-fibre-obstruction}\)
   with
   \(\texttt{M9-M1-lower-incomplete-fibre-dispersion-obstruction}\); and
3. \(\texttt{M9-M2-hard-top-product-fibre-mean-obstruction}\) with
   \(\texttt{M9-M2-hard-top-product-fibre-transform-self-return}\).

The identical three components occur before and after simulation.  No new
component appears, and neither the created node nor the updated owner lies
in one.  Thus the Round-195 patch passes the applicable no-new-cycle
control; the inherited components are disclosed rather than attributed to
this patch.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| live graph hash | PASS.  Exact canonical hash \(815c15c4\ldots\). |
| patch hash and JSON structure | PASS.  Exact terminal hash \(8d27e6fc\ldots\), strict JSON, no duplicate keys. |
| notation-only terminal repair | PASS.  Five repaired JSON fields, eight macro occurrences, no bare decoded \(\texttt{mfrak}\), and exact predecessor-hash reconstruction. |
| operation counts | PASS.  \(1/1/0/23/27\). |
| operation IDs | PASS.  Unique, disjoint, and correctly pre/post-resolved. |
| dependency references | PASS.  Created prerequisite and owner addition both resolve. |
| cycle control | PASS with disclosed inherited state.  No new SCC and no touched node enters a cycle. |
| promoted-node evidence | PASS.  New positive evidence exists and all paths resolve. |
| evidence classification | PASS.  \(15/0/5\) on the created node; all 20 are inconclusive on the open owner. |
| evidence preexistence | PASS.  Every owner addition is new, making reversal lossless. |
| reject records | PASS.  Exactly 23 new unique records with reasons. |
| no-change deep equality | PASS.  All 27 objects remain identical. |
| mutation scope | PASS.  Only the declared owner changes among pre-existing obligations. |
| canonical reverse | PASS.  Exact starting bytes and hash recovered. |
| production replay | PASS.  Exact applied bytes reproduced with and without a judge reference. |
| authoritative-state mutation | PASS.  None performed. |

## 6. Exact dependencies and evidence paths

The audit used:

1. \(\texttt{state/proof\_obligations.yml}\) at
   \(815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89\);
2. the Round-195 \(\texttt{state\_patch.json}\) at
   \(8d27e6fc67e44b72e62dcc6d05f0a12e61015aae8190879b4926442ae654d72e\);
3. \(\texttt{math\_collab/proof\_obligations.py}\) at
   \(384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437\);
4. \(\texttt{math\_collab/validate\_state\_patch.py}\) at
   \(cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8\).

The 20 unique evidence files checked were the durable kernel, formal
candidate, two nonblind reports, blind report, launch validation, synthesis,
conductor reconciliation and adjudication, and all eleven named seam,
post-repair, blind, Gram, and final-kernel reviews under the Round-195
campaign.  Every path is a repository-relative existing file; no path is
missing.

## 7. Recommended state effect

Approve this patch for controlled production application at its exact hash,
with Round index 195 and the conductor's declared judge reference.  Record
the resulting timestamp and live graph hash at application time, then run
the independent postapplication protected-scope reverse/replay audit.

This preapplication audit itself changes no graph, patch, proof draft,
campaign state, or exponent.
