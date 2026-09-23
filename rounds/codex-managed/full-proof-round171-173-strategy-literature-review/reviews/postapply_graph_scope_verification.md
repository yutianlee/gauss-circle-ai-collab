# Round 174 post-application graph scope verification

- Campaign: `full-proof-round171-173-strategy-literature-review`
- Round: 174
- Role: independent post-application exact-delta and scope auditor
- Expected authoritative SHA-256: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
- Observed authoritative SHA-256: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
- Audit date: 2026-08-27, Asia/Shanghai
- Verdict: **GREEN**

## 1. Result

**GREEN.**  The authoritative graph is exactly the intended post-Round-174
graph.  Its observed SHA-256 equals the required hash, its bytes are the
repository's canonical serialization, and graph validation returns zero
issues.

Relative to the certified Round-174 starting graph, the applied delta is
exactly:

1. one changed existing obligation,
   `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`;
2. eight inconclusive-evidence additions, the exact patch `next_action`,
   `last_updated_round: 174`, and application timestamp on that obligation;
3. exactly twenty-two fresh rejected records appended in patch order; and
4. no created or removed obligation and no other mutation.

The post-application graph contains 377 obligations and 1,411 rejected
claims.  All statuses, statements, dependencies, blockers, implications, and
certified exponents remain unchanged.

## 2. Exact applied statement and hypotheses

The sole updated record remains a `proved_internal` reduction.  Its current
`next_action` is byte-for-byte equal to the patch text selecting the exact
one-sided whole-stopped-chain nonzero ordinary-frequency K26 bound

\[
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon.
\]

The action retains the literal coefficient, both parity branches, constants
\(i/2\) and \(1/8\), collective ordinary-zero bookkeeping, strict terminal
link, once-only short correction, cells, endpoints, transitions, and zero
extension; it stops on the named capacity or self-return failures and forbids
an in-round pivot.  It limits any eventual implication to K26 and the
complete residual scalar, not full \(t=1\), hard TOP, M9-M2, a bridge, or an
exponent.

The target's application metadata is exactly
`last_updated_round: 174` and `last_updated_at: 2026-08-27T00:52:12`.
Each of the eight patch evidence paths occurs exactly once in
`evidence.inconclusive`, occurs in the declared order, is normalized and
repository-relative, and resolves to an existing file.

The final twenty-two rejected records have exactly the patch IDs and reasons,
all have round 174 and timestamp `2026-08-27T00:52:12`, and none collides with
an earlier rejected ID or any obligation ID.  All 1,411 rejected IDs are
unique.

## 3. Exact reverse derivation and cycle audit

I reconstructed the starting graph entirely in memory by reversing only the
declared patch effects:

1. remove the final twenty-two rejected records after verifying their IDs,
   reasons, order, round, and timestamp;
2. remove exactly the eight newly appended inconclusive paths from the sole
   updated reduction;
3. restore that reduction's exact accepted Round-167 `next_action`;
4. restore `last_updated_round: 167` and
   `last_updated_at: 2026-08-26T15:28:52`; and
5. change nothing else.

Canonical serialization of this inverse has SHA-256

`04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`,

exactly the certified Round-174 starting hash.  The inverse also validates
with zero issues.  Structured comparison shows that the selected reduction
is the only changed obligation and that its changed keys are exactly
`evidence`, `next_action`, `last_updated_round`, and `last_updated_at`.
Every other obligation and every pre-existing rejected record is data-
identical to its preimage.

The before/after hashes of every status, statement, dependency, blocker, and
implication ledger are identical.  Hence the three pre-existing dependency
strongly connected components and the four pre-existing combined proof-flow
components have identical membership before and after; no new dependency or
semantic cycle was introduced, and the updated reduction belongs to none of
them.

## 4. First doubtful or unproved step

There is no unresolved application, evidence-path, status, statement, edge,
exponent, uniqueness, or cycle seam.

The first mathematical gap remains the selected K26 inequality itself.  No
accepted theorem supplies the missing factor-\(L\) saving on the complete
literal one-sided whole-chain signed nonzero-frequency aggregate.  Its
placement in `next_action` and the use of `inconclusive` evidence do not
promote it.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| authoritative graph hash | **GREEN:** exact `e40c2143...bbf211` |
| canonical bytes | **GREEN** |
| graph validation | **GREEN:** zero issues |
| exact inverse hash | **GREEN:** exact `04090ef6...0d962a` |
| inverse validation | **GREEN:** zero issues |
| obligation delta | **GREEN:** one changed, zero created/removed |
| target changed keys | **GREEN:** evidence/action/round/timestamp only |
| evidence resolution | **GREEN:** 8/8 present, normalized, unique |
| rejected delta | **GREEN:** exactly 22 appended |
| rejected-ID uniqueness | **GREEN:** 1,411/1,411 unique |
| status and statement drift | **NONE** |
| dependency/blocker/implies drift | **NONE** |
| theorem and exponent drift | **NONE** |
| new dependency or semantic cycle | **NONE** |
| UTF-8/control-byte hygiene | **GREEN:** zero bare CR and forbidden C0 bytes |

The exponent sentinels `GC-partial-one-third`,
`GC-external-Li-Yang-theta-star`, and `GC-target` are complete structured
matches to their pre-application records.  Thus the internal \(1/3\), repaired
external \(0.3144831759740614\ldots\), and target \(1/4\) ledgers are
unchanged.

## 6. Dependencies and exact artifacts used

This verification used the authoritative `state/proof_obligations.yml`, the
applied Round-174 `state_patch.json`, the accepted Round-167 State Patch for
the exact prior action, the Round-174 pre-apply scope and reverse audits, the
eight applied evidence artifacts, and the repository graph loader, validator,
and canonical serializer.  All comparisons and the inverse existed only in
memory.  No state file was edited or applied.

## 7. Recommended state effect

Retain the authoritative graph without repair.  The selected reduction
properly receives only inconclusive strategy/source evidence and an exact
next action; it remains `proved_internal` only for its already accepted
reduction statement.  The twenty-two appended records correctly quarantine
Round-174 overclaims.

K26, the complete residual scalar, full \(t=1\), hard TOP, BAL, UNBAL,
M9-M2, both M1 routes, endpoint uniformity, M9, both bridges, the internal
one-third result, the external Li--Yang benchmark, and the quarter target all
remain at their pre-Round-174 states.

**Final verdict: GREEN.**
