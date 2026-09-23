# Round 179 final pre-application kernel, scope, and hygiene review

## 1. Result

**Verdict: REPAIR.**

The durable kernel, formalized candidate, conductor reconciliation,
adjudication, controls, synthesis, and State Patch are mathematically and
graph-theoretically consistent.  The `phi(q)` wording repair is present in
the durable kernel.  The primitive projector, `d=1` trace, `q=1` boundary,
centered normalization, self-return, physical powers, literal orientation
map failures, owner scope, and exponent quarantine all pass.

Application is blocked only by evidence-artifact hygiene.  The exact first
issue is
`reports/literal_primitive_conductor_parity_attack.md:196`, where the
display contains `,qquad` instead of `,\qquad`.  The same file repeats that
error at line 213.  Three other cited evidence files contain unmatched
inline-math closing delimiters:

- `reports/hostile_orientation_defect_capacity_audit.md`: lines 81, 214,
  and 369;
- `reports/blind_primitive_kernel_rederivation.md`: lines 234 and 257; and
- `reviews/capacity_owner_and_false_control_review.md`: lines 279 and 326.

Strict UTF-8 decoding passes for every audited artifact, and no C0, DEL,
NUL, tab, or other control byte is present.  Display-math delimiters are
balanced.  The repair is therefore narrow: fix the two missing command
backslashes and the seven unmatched inline closers, then rerun this hygiene
gate.  No mathematical or State Patch change is presently indicated.

The first open mathematical statement remains (179.K19); the REPAIR
verdict concerns file hygiene only.

## 2. Exact statements and state effects reviewed

The durable result uses the accepted literal packet and defines

\[
K_q(b)=\sum_{a\in U(q)}c_q(a)e(ab/q),
\qquad
K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q.
\tag{179.F1}
\]

The reviewed finite identities are

\[
K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
\qquad
K_q(b)+K_q(-b)=\frac{2\mu(q)}q
\quad(b\in U(q)),
\tag{179.F2}
\]

\[
\mathcal C_{u_0,q}
=\frac q{u_0}\sum_bK_q^\circ(b)(B^+_{q,b}-B^-_{q,b})
+\frac{\mu(q)}{u_0}\sum_b(B^+_{q,b}+B^-_{q,b}),
\tag{179.F3}
\]

and, for odd `u_0>1`,

\[
\sum_{q\mid u_0}\frac q{u_0}K_q^\circ(b)=E_{u_0}(b).
\tag{179.F4}
\]

The reviewed high/low conclusion is

\[
\mathcal D^\circ_{>Q_B}
=\mathcal O_{u_0}-\mathcal D^\circ_{\le Q_B},
\qquad
\mathcal C_{>Q_B}=\mathcal O_{u_0}-\mathcal C_{\le Q_B}.
\tag{179.F5}
\]

The exact power ledger is

\[
\#\{z\text{ at fixed }(\kappa,u,u_0)\}\ll u_0L,
\tag{179.F6}
\]

\[
\#\{z\text{ for one ordered pair mod }q\}
\ll \kappa gh^2\asymp Lh/q,
\qquad h=u_0/q,
\tag{179.F7}
\]

\[
\#\{z:\bar v n_0\equiv b\pmod q\}\ll Lu_0/q,
\tag{179.F8}
\]

so the centered exact-conductor positive capacity is

\[
O_\varepsilon(LqX^\varepsilon),
\tag{179.F9}
\]

and one conductor square root leaves

\[
L\sqrt qX^\varepsilon.
\tag{179.F10}
\]

The State Patch is reviewed only for the proposed subordinate
`proved_internal` projector/trace/self-return node, evidence and next-action
updates to the accepted primitive-alias reduction and open hard-TOP owner,
narrow mechanism rejections, and explicit no-change records.  No parent,
bridge, theorem, or exponent promotion is authorized.

## 3. Verification

### 3.1 Projector, `d=1`, `q=1`, and normalization

For `r | q` and `d=q/r`, direct substitution gives

\[
c_q(rk)=r^{-1}c_d(k).
\tag{179.F11}
\]

Möbius inversion of the unit-frequency indicator then gives (179.F2).
For a unit `b`, every divisor `d>1` contributes an odd function under
`b -> -b`; only `d=1` remains in the symmetric part.  Multiplication by
the accepted alias factor `q/u_0` changes `mu(q)/q` to exactly
`mu(q)/u_0` in (179.F3).  No factor `q`, `phi(q)`, `g`, or `h` is missing.

At `q=1`, `K_1(0)=1` and `K_1^circ(0)=0`.  Accordingly (179.F4) is
correctly restricted to `u_0>1`; the `u_0=1` stratum is wholly low
conductor.  For `u_0>1`, the `q=1` centered defect is zero but its symmetric
trace is essential to

\[
\sum_{q\mid u_0}\mu(q)=0.
\tag{179.F12}
\]

Thus the all-conductor centered trace cancels and (179.F5) follows
atomwise from the reduction of the same primitive residue to every
`q | u_0`.  The kernel and every closing artifact correctly call this
self-return, not an estimate or lower mass.

### 3.2 Trace, lift, conductor, and square-root powers

The symmetric trace coefficient has magnitude `|mu(q)|/u_0`; applying it
to the complete `O(u_0L)` atom mass gives `O(|mu(q)|L)` at fixed
`(u_0,q)`.  The exact divisor-label sum is

\[
\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|
=\prod_{p^a\parallel u}(2a+1)
\ll_\varepsilon X^\varepsilon.
\tag{179.F13}
\]

Hence the complete high trace is `O(LX^epsilon)` at fixed supported
`(kappa,u)`.  The internal `d=1` projector term is not the separate
physical `q=1` alias, so no low-conductor term is recounted.

The multiplicities (179.F7)--(179.F8) agree with both accepted predecessor
kernels.  There are `O(gh)` `v`-lifts, `O(h)` `n_0`-lifts, and
`O(kappa)` fibre sites per ordered residue pair; `phi(q)` ordered unit
pairs produce one inverse-product bucket.  The repaired durable wording
now says exactly `phi(q) asymp q` for the prime and prime-square controls.

The pointwise projector bound is

\[
|K_q^\circ(b)|
\le \frac1q\sum_{d\mid q,\ d>1}d|\mu(q/d)|
\ll_\varepsilon q^\varepsilon,
\tag{179.F14}
\]

which combines with (179.F6) to give (179.F9).  For prime `p`,
`K_p^circ=E_p`; for `p^2`,
`K_{p^2}^circ=E_{p^2}-p^{-1}E_p`.  Distributed artificial arrays attain
`asymp Lq` while respecting the unit and per-bucket count shadows.  Every
artifact correctly quarantines them from the actual selector and phase
field.  A single square-root gain restores only (179.F10), not target
scale on power-size conductors.

### 3.3 Literal orientation maps

The fixed-modulus reflection

\[
(s,w)\longmapsto(u-s,v-w)
\tag{179.F15}
\]

maps the unrestricted plus equation `sv-wu=n` to the minus equation
`uw-sv=n`, keeps `u_0,q,b`, and sends fibre index `t` to `-t`.  It is live
only for `1 <= s <= u-1` and `1 <= w <= v-1`, at most one site of a
primitive fibre.  On that overlap it sends the plus endpoint pair
`(x,x+r)` to `(C-x-r,C-x)`, so no phase, selector, squarefree, profile, or
hard-endpoint conjugacy follows.

The endpoint-preserving exchange

\[
(u,v,s,w,+)\longmapsto(v,u,w,s,-)
\tag{179.F16}
\]

preserves the two products but changes the fixed outer row, primitive
modulus, conductor, and bucket.  Its fixed-row case forces `u=v=1` by
coprimality and hence has only low conductor.  It also replaces both
selected divisors by complementary factors: below the upper near-square
window in the odd branch and even in the even branch.  The literal zero
extension kills the exchanged coefficient.  The durable kernel and State
Patch reject only these evident maps; they do not reject every possible
future literal signed theorem.

### 3.4 Candidate, closing artifacts, and State Patch

The candidate, reconciliation, adjudication, controls, and synthesis all
state the same result and closing label
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go`.
The asymmetric split in the discovery report and centered split in the
durable kernel are exactly equivalent.  The blind single-bucket extremizer
is restricted to its statement-only total-mass model; the durable kernel
uses the later-unmasked distributed control.

The canonical state file hashes to
`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`,
exactly matching `state_patch.json`.  The proposed created ID is absent
from the starting graph; both updated IDs and all 18 no-change IDs exist.
All dependencies resolve, the added dependency is acyclic, all 14 reject
IDs are new and unique, and both saved next actions and their restoration
metadata exactly match the starting state.

All 12 distinct evidence paths named by the State Patch exist.  The JSON
parses successfully, and the created statement, next actions, rejections,
no-change records, assessment, and synthesis preserve the exact
mathematical and owner scope.  In particular, the rejection of centering
is explicitly limited to automatic or coefficient-uniform gain and does
not exclude a selector-aware theorem written in centered variables.

### 3.5 Encoding and delimiter audit

Strict UTF-8 decoding succeeds for the durable kernel, candidate, two
predecessor kernels, all reports and reviews, controls, adjudication,
synthesis, and State Patch.  Byte/character scans find no invalid UTF-8,
replacement character, NUL, C0 control, tab, DEL, or other control byte.
Every display delimiter `\[`/`\]` is balanced.

The durable kernel, candidate, reconciliation, adjudication, controls,
synthesis, blind post-unmask review, and literal orientation review have
balanced inline delimiters.  The remaining exact repairs are:

1. `reports/literal_primitive_conductor_parity_attack.md:196` and `:213`:
   replace `,qquad` by `,\qquad`.
2. `reports/hostile_orientation_defect_capacity_audit.md:81`, `:214`, and
   `:369`: replace the respective `(q\mid u_0\)`, `(q\mid u_0\)`, and
   `(u_0\)` fragments by `\(q\mid u_0\)`, `\(q\mid u_0\)`, and
   `\(u_0\)`.
3. `reports/blind_primitive_kernel_rederivation.md:234` and `:257`:
   replace `(q\mid u_0\)` and `(b_0\)` by `\(q\mid u_0\)` and
   `\(b_0\)`.
4. `reviews/capacity_owner_and_false_control_review.md:279` and `:326`:
   replace `(q\mid u_0\)` and `(\ell^1\)` by `\(q\mid u_0\)` and
   `\(\ell^1\)`.

These are presentation-level defects in cited evidence, not changes to
any formula, power, literal claim, or State Patch operation.  Because this
is the final pre-application hygiene gate, they must be repaired before
application.

## 4. Exact first issue and first open mathematical step

The exact first pre-application issue is the missing backslash before
`qquad` at
`reports/literal_primitive_conductor_parity_attack.md:196`.  The State
Patch should not be applied while a cited positive-evidence artifact fails
the required delimiter/TeX hygiene check.

After the listed presentation repairs, no mathematical issue is presently
identified before the explicitly open defect

\[
\left|
\sum_{u_0\mid u}\sum_{q\mid u_0,\ q>Q_B}
\frac q{u_0}\sum_{b\in U(q)}K_q^\circ(b)
(B^+_{q,b}-B^-_{q,b})
\right|
\stackrel{?}{\ll}_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.
\tag{179.F17}
\]

By (179.F5), this is the original unresolved literal orientation block
minus a target-safe low-conductor term.  Neither the exact projector nor
the two failed literal maps prove or disprove it.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| durable `phi(q)` repair | **GREEN.** The proof now says `phi(q) asymp q` specifically for prime and prime-square controls. |
| projector and Fourier sign | **GREEN.** (179.F2) agrees with both independent derivations. |
| `d=1` symmetric term | **GREEN.** It is exactly `mu(q)/q`; after normalization the centered trace is `mu(q)/u_0`. |
| `q=1` and `u_0=1` | **GREEN.** `K_1=1`, `K_1^circ=0`; the high packet is empty at `u_0=1`, while `q=1` remains essential to trace cancellation for `u_0>1`. |
| exact high/low split | **GREEN.** The centered and uncentered identities have no missing divisor or absolute value. |
| trace divisor power | **GREEN.** (179.F13) is a divisor factor and gives the local `L` target up to `X^epsilon`. |
| physical lifts | **GREEN.** `g,h,kappa`, residue-pair, and bucket multiplicities are all restored. |
| defect capacity | **GREEN as capacity only.** It is `LqX^epsilon`, not literal lower mass. |
| one-square-root restoration | **GREEN obstruction.** It leaves `L sqrt(q) X^epsilon`. |
| fixed-modulus reflection | **GREEN obstruction.** It fails complete domain and endpoint/selector preservation. |
| endpoint-preserving exchange | **GREEN obstruction.** It changes the fixed block and is killed by complementary-divisor zero extension. |
| first open defect | **OPEN, correctly quarantined.** (179.F17) remains unproved. |
| State Patch hash and reversibility | **GREEN.** Starting hash, saved next actions, and metadata match exactly. |
| State Patch IDs and paths | **GREEN.** Created/update/no-change/reject IDs are consistent; all current evidence paths exist. |
| downstream owner scope | **GREEN.** Only a subordinate reduction/no-go is created. |
| exponent quarantine | **GREEN.** `1/3`, `0.3144831759740614...`, and `1/4` remain unchanged. |
| UTF-8 and control bytes | **GREEN.** Strict decoding passes and no forbidden control byte occurs. |
| delimiter/TeX hygiene | **REPAIR.** Two missing `\qquad` commands and seven unmatched inline closers remain in cited evidence. |

No numerical or external theorem evidence was used.

## 6. Dependencies and exact artifacts used

This review used the project protocol and authoritative starting state,
the durable kernel and both accepted predecessors, the formalized
candidate, all Round 179 reports and reviews, and the complete closing
packet:

- `AGENTS.md`;
- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/candidates/formalized_primitive_conductor_parity_self_return.md`;
- all three files under that campaign's `reports/` directory;
- all five existing files under that campaign's `reviews/` directory;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/controls/conductor_round179_controls.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reviews/conductor_round179_adjudication.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/synthesis.md`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/state_patch.json`.

No unlisted mathematical source or external theorem was used.  No graph,
state patch, kernel, candidate, report, prior review, control, adjudication,
or synthesis file was edited.

## 7. Recommended state effect

**REPAIR before application.**  Correct only the nine presentation defects
listed in Section 3.5 and rerun the delimiter/UTF-8/control-byte gate.
The mathematical kernel, candidate, controls, adjudication, synthesis, and
State Patch require no current formula, power, dependency, rejection, owner,
or exponent change.

Do not apply `state_patch.json` until the cited evidence files pass the
hygiene gate.  After that repair, the expected verdict is GREEN for the
subordinate primitive-projector/trace/self-return node, while (179.K19),
(177.K34), complete K17a, every parent and bridge, the quarter theorem, and
all exponent owners remain open or unchanged at their inherited status.
This review makes no graph edit.
