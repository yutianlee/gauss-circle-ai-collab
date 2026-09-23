# Round 179 final post-repair verification

## 1. Result

**Verdict: GREEN.**

The nine presentation defects isolated by
`final_preapply_kernel_scope_hygiene_review.md` are repaired exactly.  The
complete Round 179 campaign packet and durable kernel pass strict encoding,
control-byte, display/inline delimiter, TeX-command, structured-JSON,
evidence-path, mathematical formula/power/scope, starting-hash, official
State Patch, and repository unit-test gates.

**First issue: NONE.**  No remaining pre-application repair or rejection
issue was found.  The first open mathematical statement remains (179.K19),
equivalently (177.K34) after the safe trace and low-conductor packet are
removed; that inherited open statement is not a hygiene defect.

No patch was applied and no graph, state, kernel, candidate, report, control,
prior review, synthesis, or JSON artifact was edited.

## 2. Exact statement and scope verified

For odd `q` and unit `b`, the durable kernel states and proves

\[
K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
\qquad
K_q(b)+K_q(-b)=\frac{2\mu(q)}q,
\]

with the whole symmetric term supplied by `d=1`.  With

\[
K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q,
\]

the exact block is

\[
\mathcal C_{u_0,q}
=\frac q{u_0}\sum_bK_q^\circ(b)(B^+_{q,b}-B^-_{q,b})
+\frac{\mu(q)}{u_0}\sum_b(B^+_{q,b}+B^-_{q,b}).
\]

For odd `u_0>1`, the all-conductor identity is

\[
\sum_{q\mid u_0}\frac q{u_0}K_q^\circ(b)=E_{u_0}(b).
\]

At `q=1`, `K_1(0)=1` and `K_1^circ(0)=0`; the `u_0=1` stratum has no
high-conductor packet, while the physical `q=1` trace remains essential to
`sum_(q|u_0) mu(q)=0` for `u_0>1`.  Thus the high centered defect and the
uncentered high block self-return exactly to the original literal block minus
their already-safe low-conductor parts.  No estimate or literal lower bound is
silently inferred.

The verified scope is one subordinate primitive-projector/trace/self-return
reduction and mechanism-level no-go.  It does not prove (179.K19), (177.K34),
complete K17a, hard TOP, M9--M2, M9, either bridge, the quarter theorem, or an
exponent improvement.  Internal `1/3`, audited external
`0.3144831759740614...`, and target `1/4` remain quarantined.

## 3. Exact verification

### 3.1 Encoding, controls, delimiters, TeX, and JSON

The audited corpus contains all 20 files presently in the Round 179 campaign
directory plus
`proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`:
21 files, 19 Markdown files, two JSON files, and 194,977 bytes in total.

- Strict UTF-8 decoding passed for all 21 files.  There are zero BOMs, NULs,
  tabs, forbidden C0/DEL bytes, isolated carriage returns, or U+FFFD
  replacement characters.
- After excluding fenced and inline code, the ordered delimiter scan found
  exactly 250 opening and 250 closing display delimiters, and 283 opening and
  283 closing inline delimiters, with zero unmatched, nested, crossed, or
  unclosed delimiter.
- The TeX-command scan found zero bare or malformed `qquad`-family command and
  zero math-brace/environment defect.  In particular, the two former
  `,qquad` strings now read `,\qquad`.
- `plan.json` and `state_patch.json` both parse strictly.  The active campaign
  also passes the repository campaign validator.

The nine exact repair-site checks are GREEN:

1. `reports/literal_primitive_conductor_parity_attack.md:196` and `:213`
   contain `,\qquad`.
2. `reports/hostile_orientation_defect_capacity_audit.md:81`, `:214`, and
   `:369` contain balanced inline math around the formerly unmatched
   `q\mid u_0`, `q\mid u_0`, and `u_0` fragments.
3. `reports/blind_primitive_kernel_rederivation.md:234` and `:257` contain
   balanced inline math around `q\mid u_0` and `b_0`.
4. `reviews/capacity_owner_and_false_control_review.md:279` and `:326`
   contain balanced inline math around `q\mid u_0` and `\ell^1`.

### 3.2 Formula and power ledger

Direct substitution gives `c_q(rk)=r^(-1)c_(q/r)(k)`.  Möbius projection
therefore gives the displayed divisor formula.  For a unit `b`, every `d>1`
term is antisymmetric under `b -> -b`; only `d=1` remains, with exact value
`2mu(q)/q`.  Multiplication by the accepted alias factor `q/u_0` gives the
trace coefficient `mu(q)/u_0`, with no missing `q`, `phi(q)`, `g`, or `h`.

The fixed-stratum atom mass is `O(u_0 L X^epsilon)`, hence the trace is
`O(|mu(q)| L X^epsilon)` at fixed `(u_0,q)`.  The exact divisor count is

\[
\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|
=\prod_{p^a\parallel u}(2a+1)\ll_\varepsilon X^\varepsilon.
\]

For the centered defect,
`|K_q^circ(b)| <<_epsilon q^epsilon`, so coefficient-uniform positive
capacity is `O_epsilon(LqX^epsilon)`.  Restoring the physical lifts gives
`O(kappa g h^2)=O(Lh/q)` atoms per ordered residue pair and
`O(Lu_0/q)` per inverse-product bucket.  The durable wording correctly uses
`phi(q) asymp q` only for the prime and prime-square controls.  One conductor
square-root leaves `L sqrt(q) X^epsilon`, not the local `L` target.

The prime formulas `K_p^circ=E_p` and
`K_(p^2)^circ=E_(p^2)-p^(-1)E_p` correctly retain artificial `Lq` capacity.
Every artifact keeps those arrays diagnostic and does not promote them to
literal lower mass.

### 3.3 Literal orientation and owner scope

The fixed-modulus reflection maps the unrestricted plus lattice to the minus
lattice but is live only for `1<=s<=u-1` and `1<=w<=v-1`, at most one site of
a primitive fibre.  It does not preserve the endpoint pair or the complete
selector, phase, squarefree, profile, and hard-value fields.  The
product-preserving exchange changes the fixed outer row, primitive modulus,
conductor, and bucket, and sends selected divisors to zero-extended
complements.  The packet rejects only these audited maps, not every possible
future selector-aware signed theorem.

### 3.4 State Patch, hash, and evidence paths

The raw SHA-256 of `state/proof_obligations.yml` is

`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`,

exactly matching `starting_graph_sha256` in `state_patch.json`.  The official
read-only validator returned `Patch OK`; official in-memory application at
round 179 and post-application graph validation returned zero issues.

The exact operation ledger is `1 create / 2 update / 0 correct_rejected /
14 reject / 18 no_change`, changing the simulated counts from 380 to 381
obligations and 1,472 to 1,486 rejected claims.  Created and rejected IDs are
collision-free.  There is zero pre-existing status or statement drift, zero
no-change-record drift, and zero drift in the three exponent owners.

The patch contains 24 evidence-path insertions drawn from 12 distinct,
existing, normalized regular files: 12 positive paths on the created node and
six inconclusive paths on each updated node.  No path has parent traversal,
backslash separators, control characters, or surrounding whitespace.  The
saved next actions and metadata match the starting graph and support exact
reversal.  The new dependency direction is subordinate and introduces no new
cycle or parent promotion.

### 3.5 Six repository tests

All six tests passed:

1. `test_concurrency_is_bounded`;
2. `test_prepare_writes_minimal_brief_and_provenance`;
3. `test_statement_only_context_leak_is_rejected`;
4. `test_valid_statement_only_campaign`;
5. `test_correct_rejected_requires_existing_claim`; and
6. `test_correct_rejected_updates_existing_claim`.

## 4. First doubtful or unproved step

There is no doubtful step in the repaired presentation, finite projector,
trace, self-return, power ledger, patch mechanics, or declared scope.  The
first unproved mathematical estimate is exactly (179.K19), the complete
literal centered high-conductor defect.  It remains explicitly open and
quarantined.

## 5. Required controls and outcomes

| Gate | Outcome |
|---|---|
| UTF-8 and forbidden bytes | **GREEN:** 21/21 files; zero issue. |
| Display/inline delimiters | **GREEN:** 250/250 and 283/283; zero order issue. |
| TeX commands and nine repairs | **GREEN:** all nine exact sites pass. |
| JSON and campaign structure | **GREEN:** both JSON files parse; campaign validates. |
| Projector, `d=1`, `q=1`, centering | **GREEN:** exact formulas and boundary. |
| Formula, lift, divisor, and capacity powers | **GREEN:** no missing factor. |
| Literal orientation-map scope | **GREEN:** both failures are narrowly stated. |
| Evidence paths | **GREEN:** 24 insertions, 12 distinct existing files. |
| Starting hash | **GREEN:** exact declared hash match. |
| Official State Patch validation | **GREEN:** `Patch OK`; zero post-graph issue. |
| Owner and exponent quarantine | **GREEN:** zero status, statement, or exponent drift. |
| Repository unit tests | **GREEN:** 6/6. |

No numerical or external-theorem evidence was used.

## 6. Dependencies and exact artifacts used

This verification used `AGENTS.md`, `protocol.md`, the authoritative starting
graph and active campaign, every file in the complete Round 179 campaign
directory, the durable primitive-conductor parity/self-return kernel, and the
repository campaign, graph, State Patch, and unit-test machinery.  The
mechanical corpus was the 20 campaign files existing before this report plus
the durable kernel.  No unlisted mathematical source was used.

## 7. Recommended state effect

**GREEN for conductor-controlled application of the reviewed State Patch.**
Authorize only its declared subordinate create/update/rejection/no-change
ledger.  Preserve (179.K19), (177.K34), complete K17a, every parent and
bridge, the quarter theorem, and all exponent owners at their inherited
status.  This verification itself makes no graph change.
