Your architecture is already unusually strong for AI-assisted mathematical research. The best single improvement is **not adding a fourth model** or making prompts longer. It is converting the system from a **round/transcript-centered workflow** into a **claim-centered proof-obligation workflow**.

At present, the repository is the canonical memory, the agents are asymmetric, and the round barriers enforce independent reasoning before cross-review and synthesis. That is sound. The report also correctly identifies the current mathematical state: the project has a conditional bridge

```text
H1-H3 + H4 + R5-Full + M9 => P(X) <<_ε X^(1/4+ε),
```

with `M9` still the real analytic bottleneck, not a solved lemma. 

But the workflow is starting to suffer from **state bloat** and **state ambiguity**. The report says Round 28 prompts are around 1.5 MB and that `current_state.md` and `reading_packet.md` have become near-transcripts rather than compact state. It also notes that `lemma_bank.md` and `gap_register.md` exist but do not yet carry the real active lemma/gap state. 

So the highest-value improvement is:

> **Introduce a formal Proof Obligation Graph, and make every round update that graph rather than merely append prose.**

Everything else — compact reading packets, validator, round manifests, computational harness, source theorem cards — should be subordinated to that one design change.

---

## Evaluation of the current architecture

### 1. The three-agent design is good

The roles are well chosen:

```text
A1 = strategist / synthesis / judge
A2 = conservative referee / obstruction finder
A3 = algebra / normalization / executable-check planner
```

This is better than using three interchangeable models. Mathematical failure usually comes from different directions: false global strategy, hidden analytic gap, normalization error, or invalid algebra. Your three agents attack different failure modes. The report explicitly notes that the roles are intentionally asymmetric and that this gives the workflow “three different failure modes and strengths.” 

I would keep the three-agent structure.

The only modification I would make is this: **A1 should not be both a participant and the final judge without a structured check.** Let A1 write the narrative synthesis, but the repository should accept only a machine-readable state patch that passes validation. In other words, A1 can judge prose, but it should not be allowed to silently mutate the mathematical state.

### 2. The stage barriers are correct

Your Stage A → Stage B → Stage C → Stage D pipeline is well designed:

```text
Stage A: independent reasoning
Stage B: cross-review
Stage C: judge synthesis
Stage D: state update
```

The report says the orchestrator enforces that all Stage A reasoning must finish before reviews, all reviews before synthesis, and synthesis before state update. 

This matters. Without barriers, the first strong-sounding model contaminates the whole round. For a hard open problem, premature convergence is a serious risk.

I would keep the barrier synchronization, but modify the unit of work. Instead of “round 29 discusses the project,” make it:

```text
Round 29 attacks Proof Obligation M9.2.3 only.
```

The barrier should protect independence **on a specific proof obligation**, not on the whole research state.

### 3. The file-based public memory is the right foundation

The repository-as-memory design is correct. Web chats are too fluid, too hard to audit, and too dependent on hidden conversation state. Your report explicitly treats the public repository as authoritative and persistent web conversations only as continuity aids. 

That is the right rule.

However, the repository currently has too much **append-only prose** and too little **queryable mathematical state**. This is the main architectural weakness.

### 4. The current bottleneck is mathematically well isolated

The workflow has done something valuable: it has not falsely claimed a solution. It has reduced the current route to `M9`, the endpoint-strength estimate for fixed-Vaaler-coefficient reciprocal sums, with uniformity over

```text
X^(1/4) <= D <= X^(1/2).
```

The report also notes that the `M2` sum is especially delicate because of the frequency-side character factor

```text
C_h = e(h/4)-e(3h/4).
```



That is a good outcome. Many AI-assisted attempts at hard problems fail by inventing closure. Your system has instead localized the obstruction.

The next architecture should exploit that by forcing every round to ask:

```text
Which specific proof obligation related to M9 changed status?
```

If the answer is “none,” the round did not make mathematical progress.

---

## Main weakness: the workflow is round-centered, not claim-centered

Right now, the natural object of progress is a **round**:

```text
round_027/
round_028/
round_029/
```

But in mathematics, the natural object of progress is a **claim**:

```text
M9
M9-M2-fourth-moment
M9-near-collision-bound
R5-Full
Vaaler-floor-compatibility
Li-Yang-source-hypothesis
```

A round is just a communication event. A claim is a mathematical object.

This distinction matters because round-based systems tend to accumulate:

* repeated summaries;
* repeated caveats;
* partially restated lemmas;
* unmerged variants of the same gap;
* buried status changes;
* implicit confidence drift.

Claim-based systems accumulate:

* exact statements;
* dependencies;
* proof status;
* failure modes;
* evidence;
* owners;
* next verification action.

The report already points in this direction by recommending `claims.yml`, `lemmas.yml`, `gaps.yml`, `routes.yml`, `tasks.yml`, and `sources.yml`. 

I would go further: **make these structured ledgers the authority, not a supplement.**

---

# Best improvement: build a Proof Obligation Graph

Implement a central file:

```text
state/proof_obligations.yml
```

This should become the mathematical core of the system.

A proof obligation is any claim whose truth status matters for the project. It can be a theorem, lemma, reduction, source theorem, computation target, counterexample search, or normalization convention.

Use a schema like this.

```yaml
- id: M9
  type: lemma
  title: Endpoint bound for fixed Vaaler reciprocal main sums
  status: open
  statement_tex: |
    For X large and X^{1/4} \le D \le X^{1/2},
    the fixed-coefficient reciprocal sums M_1(D;X), M_2(D;X)
    satisfy
    M_i(D;X) \ll_\epsilon X^{1/4+\epsilon}.
  dependencies:
    - H1
    - H2
    - H3
    - H4
    - R5-Full
  implies:
    - GC-target-conditional
  blockers:
    - M9-M2-character-factor
    - M9-near-collision
    - M9-endpoint-uniformity
  evidence:
    positive: []
    negative: []
    inconclusive:
      - rounds/web-research-test/round_028/responses/A3-028.md
  last_updated_round: 28
  owner: A2
  next_action: >
    Formulate the exact M2 fourth-moment / near-collision subproblem
    with all frequency-side character factors and endpoint conventions.
  promotion_rule: >
    May move from open to derived_under_assumptions only if a proof gives
    uniform bounds over all active dyadic D and handles both M1 and M2.
```

For a source theorem:

```yaml
- id: Vaaler-1985-floor-compatible
  type: external_theorem
  title: Finite Vaaler approximation compatible with sawtooth floor terms
  status: source_audit_required
  source_card: sources/vaaler_1985.md
  used_by:
    - H4
  required_hypotheses:
    - exact sawtooth normalization
    - truncation parameter convention
    - Fejer residual sign and weight convention
  audit_status: pending_rendered_page_check
  next_action: >
    Verify theorem statement, constants, and residual convention directly
    from the source PDF or rendered page.
```

For a computational obligation:

```yaml
- id: M9-regression-raw-vs-paired
  type: computation
  title: Raw-vs-paired numerical stress test for M9
  status: not_started
  target_claim: M9
  required_output:
    - script
    - command
    - table
    - precision log
    - report.md
  accepted_evidence_level: diagnostic_only
  owner: A3
  next_action: >
    Produce one small reproducible table comparing raw and paired sums
    over representative dyadic D blocks.
```

This file should be the object that every agent reads and every judge synthesis updates.

---

## Revised round workflow

Keep your four stages, but change their content.

### Stage A: independent attack on selected proof obligations

Instead of giving every agent the whole project context, assign each agent one or two specific obligations.

Example:

```text
Round 29 target obligations:
- M9-M2-character-factor
- M9-near-collision-taxonomy
- Vaaler-1985-floor-compatible-source-audit
```

A1 prompt:

```text
You are A1. Do not summarize the whole project.

Target obligation:
M9-M2-character-factor

Task:
Give the most plausible analytic route to closing this obligation.
State the exact lemma needed. Do not claim M9.
Return a proposed state patch only if the status should change.
```

A2 prompt:

```text
You are A2. Do not search for a new route.

Target obligation:
M9-M2-character-factor

Task:
Act as hostile referee. Identify why the current formulation is insufficient.
Find missing endpoint, two-sided, character-factor, and uniformity assumptions.
Return blockers as structured proof obligations.
```

A3 prompt:

```text
You are A3.

Target obligation:
M9-regression-raw-vs-paired

Task:
Produce executable diagnostics, not prose-only plans.
Required output:
1. script path;
2. exact command;
3. output table;
4. report.md;
5. limitations.
Numerical output is diagnostic_only and must not promote M9.
```

### Stage B: cross-review only the proposed state changes

Currently, agents review each other’s full responses. That is expensive and noisy.

Instead, require each agent to review:

```text
1. proposed new obligations;
2. proposed status changes;
3. proposed dependency changes;
4. proposed rejection/promotions;
5. claimed evidence files.
```

This shifts review from prose criticism to mathematical state integrity.

### Stage C: judge synthesis produces a state patch

A1 may still write a narrative synthesis, but the important output should be:

````markdown
## State Patch

```yaml
proof_obligations:
  update:
    - id: M9-M2-character-factor
      status: open
      blockers_added:
        - M9-M2-two-sided-frequency-convention
        - M9-M2-near-collision-offdiagonal
      evidence_added:
        inconclusive:
          - rounds/web-research-test/round_029/responses/A2-029.md
      next_action: >
        Prove or refute the near-collision offdiagonal estimate with the
        C_h=e(h/4)-e(3h/4) weight retained.

  create:
    - id: M9-M2-two-sided-frequency-convention
      type: normalization
      status: open
      statement_tex: |
        Specify the two-sided frequency convention for M_2 and show that
        the C_h-weighted expression is invariant under the pairing used
        in the proposed fourth-moment reduction.
      owner: A3

  no_change:
    - id: M9
      reason: >
        No theorem-level proof or reduction closed the endpoint-strength
        fixed-coefficient estimate.
```
````

### Stage D: orchestrator validates and applies the patch

The orchestrator should refuse to update state if:

* an unknown status appears;
* a claim is promoted without evidence;
* a lemma has no exact statement;
* `M9` is promoted without both `M1` and `M2`;
* a source theorem is used without a source card;
* a computation is treated as proof;
* an obligation has no owner or next action.

This is the single most important reliability improvement.

---

## Proposed status system

Use a small controlled vocabulary.

```yaml
allowed_statuses:
  - proposed
  - open
  - blocked
  - diagnostic_only
  - source_audit_required
  - derived_under_assumptions
  - proved_internal
  - proved_external_dependency
  - rejected
```

For a hard problem, I would make promotion deliberately difficult:

```text
proposed → open
    allowed if exact statement exists.

open → derived_under_assumptions
    allowed only if dependencies are explicit.

derived_under_assumptions → proved_internal
    allowed only if proof file exists and no fatal gaps remain.

proved_external_dependency → usable
    allowed only if source theorem card records hypotheses and exact theorem statement.

diagnostic_only → open
    forbidden automatically.
```

In particular:

```text
numerical evidence may support next_action,
but may not promote theorem status.
```

That rule should be enforced by script, not merely by prompt.

---

## Reading packet redesign

The report correctly says the reading packet should become compact and layered rather than carrying full history. 

I would generate `manifests/reading_packet.md` automatically from the proof-obligation graph.

Target structure:

```markdown
# Reading Packet: Round 29

## 1. Current theorem target

P(X) = N(sqrt(X)) - pi X <<_epsilon X^(1/4+epsilon)

Current route:
H1-H3 + H4 + R5-Full + M9 => target.

Status:
Conditional only. No new Gauss circle exponent proved.

## 2. Active bottleneck

M9: open.

Exact statement:
[...]

Current blockers:
- M9-M2-character-factor
- M9-near-collision
- M9-endpoint-uniformity

## 3. Round 29 target obligations

- M9-M2-character-factor
- M9-regression-raw-vs-paired
- Vaaler-1985-floor-compatible-source-audit

## 4. Do-not-claim rules

- Do not claim M9.
- Do not treat computation as proof.
- Do not use Li-Yang or Vaaler without source-card hypotheses.

## 5. Agent assignments

A1:
[...]

A2:
[...]

A3:
[...]

## 6. Relevant files

- state/proof_obligations.yml
- state/best_proof_draft.md
- sources/vaaler_1985.md
- computations/m9_regression/report.md
```

This is much more useful to a model than a 1.5 MB history dump.

---

## Add a progress metric

You need a way to decide whether a round was useful.

I would add:

```text
Round score = number of valid state changes, weighted by importance.
```

For example:

```yaml
progress_score:
  +5: proof obligation proved_internal
  +4: fatal gap discovered in previously plausible route
  +3: exact bottleneck lemma formulated
  +3: source theorem audited and usable/rejected
  +2: reproducible computation added
  +2: conjecture sharpened by counterexample or edge case
  +1: useful diagnostic evidence added
   0: no state change
  -2: state bloat without new obligations
  -5: invalid promotion of open claim
```

Then each judge synthesis should end with:

```yaml
round_assessment:
  mathematical_progress_score: 3
  reason: >
    No proof of M9, but the M2 character-factor obstruction was split
    into two precise proof obligations and one executable diagnostic.
```

This prevents the system from rewarding long discussions.

---

## Improve the judge role

A1 as judge is acceptable, but I would add a **non-agent validator** after A1.

The judge’s role:

```text
interpret, synthesize, assign next tasks
```

The validator’s role:

```text
accept or reject the state mutation
```

The validator should be script-based where possible.

Example checks:

```python
def validate_state_patch(patch):
    assert all_statuses_allowed(patch)
    assert no_claim_promoted_without_evidence(patch)
    assert computations_not_used_as_proofs(patch)
    assert source_dependencies_have_cards(patch)
    assert each_open_obligation_has_next_action(patch)
    assert M9_not_promoted_without_M1_M2_uniformity(patch)
```

This removes the weakest part of multi-agent collaboration: models deciding that other models have proved something.

---

## A3 should become an execution agent, not a report agent

The report notes that A3 still needs to produce committed tables or scripts rather than protocol-level plans, and recommends a computation package with experiments such as R5 residual tables, raw-vs-paired M9 regression, complex-weight failure tests, fixed-coefficient stress comparison, M2 Cauchy kernel diagnostics, and CRI endpoint ratios. 

I would make this stricter:

```text
A3 output is invalid unless it contains at least one of:
1. a committed script;
2. an exact command that ran;
3. a table;
4. a source theorem card;
5. a failed test with reproducible parameters.
```

A3 can still write audit prose, but it should be secondary.

For example, A3’s next prompt should be:

```text
You are A3.

Target:
M9-regression-raw-vs-paired.

Deliverable:
Create computations/m9_regression/.

Required files:
- computations/m9_regression/run.py
- computations/m9_regression/report.md
- computations/m9_regression/outputs/table_small.csv

Rules:
- Use exact integer arithmetic where feasible.
- Use high precision near Fejer resonances.
- Log all parameters.
- Mark the result diagnostic_only.
- Do not claim evidence proves M9.

Done only when:
- python computations/m9_regression/run.py runs from repo root;
- the CSV table is generated;
- report.md explains what was tested and what was not tested.
```

This converts A3 from “third opinion” into a mathematical laboratory.

---

## Add source theorem cards before further analytic synthesis

The report says source audits for Li-Yang and Vaaler are still partly manual and warns that theorem labels/equations may be mis-copied or hypotheses applied outside their range. 

For a problem at this level, source-card discipline is essential.

Create:

```text
sources/vaaler_1985.md
sources/li_yang_2023.md
sources/huxley_2003.md
sources/bourgain_watt.md
```

Each card should have this exact structure:

```markdown
# Source Card: Vaaler 1985

## Bibliographic data

## Local file / URL

## Exact theorem used

## Original notation

## Project notation translation

## Hypotheses

## Conclusion

## Constants / uniformity / parameter ranges

## How used in this project

## Not sufficient for

## Audited by

## Audit status

## Rounds referencing this source
```

Then enforce:

```text
No external theorem may appear in proof_obligations.yml
unless it has a source card.
```

This will reduce citation drift and prevent agents from treating remembered theorem statements as facts.

---

## Track separation

The report recommends splitting the single loop into tracks:

```text
Track A: proof infrastructure
Track B: M9 analytic attack
Track C: computation and falsification
Track D: source/literature audit
Track E: workflow/tooling maintenance
```



I agree, but I would implement tracks inside the proof-obligation graph rather than as separate workflows.

Add:

```yaml
track:
  - proof_infrastructure
  - M9_analytic
  - computation
  - source_audit
  - tooling
```

Then each round can choose one primary track and at most one secondary track.

Rule:

```text
A round should not mix more than two tracks.
```

Otherwise every round becomes overloaded: proof draft maintenance, theorem hunting, computation planning, source audit, and workflow repair all compete for attention.

---

# Concrete implementation plan

## Step 1: Add the proof-obligation graph

Create:

```text
state/proof_obligations.yml
```

Seed it with the currently active objects:

```yaml
- id: GC-target
  type: theorem
  status: open

- id: Conditional-bridge
  type: reduction
  status: derived_under_assumptions
  dependencies: [H1, H2, H3, H4, R5-Full, M9]
  implies: [GC-target]

- id: H1-H3
  type: infrastructure
  status: derived_under_assumptions

- id: H4
  type: external_or_internal_reduction
  status: source_audit_required

- id: R5-Full
  type: lemma
  status: conditional

- id: M9
  type: lemma
  status: open

- id: M9-M1
  type: sublemma
  status: open

- id: M9-M2
  type: sublemma
  status: open

- id: M9-M2-character-factor
  type: obstruction
  status: open

- id: M9-near-collision
  type: obstruction
  status: open

- id: Vaaler-source-card
  type: source_audit
  status: source_audit_required

- id: Li-Yang-source-card
  type: source_audit
  status: source_audit_required
```

## Step 2: Require state patches from every judge synthesis

Modify the judge prompt:

````text
Your synthesis is not complete unless it contains:

## State Patch
```yaml
...
````

Allowed operations:

* create
* update
* reject
* no_change

No theorem or lemma may be promoted without:

1. exact statement;
2. dependencies;
3. evidence file;
4. reason for promotion;
5. remaining caveats.

````

## Step 3: Add a validator

Create:

```text
math_collab/validate_state_patch.py
math_collab/validate_round.py
````

Minimum checks:

```text
- valid YAML
- allowed statuses only
- every obligation has id/type/status/title
- no duplicate IDs
- no computation promoted to proof
- every external dependency has source card
- every open item has next_action
- every promoted item has evidence
- M9 cannot be promoted unless M1 and M2 are both handled uniformly
```

## Step 4: Generate the reading packet from state

Stop appending judge prose into the active context. Keep full prose in `rounds/`, but generate `reading_packet.md` from:

```text
state/proof_obligations.yml
state/best_proof_draft.md
sources/*.md
human/current_directives.md
```

The packet should be compact enough that each agent sees the current problem sharply.

## Step 5: Make A3 executable

Change A3’s contract:

```text
A3 must produce executable artifacts whenever assigned a computation/source-audit task.
Prose-only A3 outputs are acceptable only for pure algebra audits.
```

This directly addresses the report’s concern that computational verification is still partly aspirational. 

---

## The revised architecture

Your current architecture is approximately:

```text
round archive → judge synthesis → append to current_state.md → next prompt
```

The improved architecture should be:

```text
proof obligations → compact packet → agent work
        ↓              ↑
state patch ← judge synthesis
        ↓
validator
        ↓
updated proof graph
```

More explicitly:

```text
state/proof_obligations.yml
state/source_cards/*.md
state/best_proof_draft.md
human/current_directives.md
        ↓
packet generator
        ↓
A1 / A2 / A3 prompts
        ↓
responses + reviews
        ↓
A1 narrative synthesis
        ↓
machine-readable State Patch
        ↓
validator
        ↓
updated proof obligation graph
        ↓
next round
```

This makes the mathematical claim graph, not the transcript, the central object.

---

# Final recommendation

Keep the three-agent collaboration and stage barriers. They are good.

Do **not** primarily improve the system by adding more agents, longer prompts, or more discussion rounds.

The best improvement is:

> **Make `state/proof_obligations.yml` the authoritative mathematical memory, require every judge synthesis to produce a validated YAML state patch, and generate compact reading packets from that structured state.**

This single change will reduce prompt bloat, prevent informal claim promotion, make gaps queryable, make progress measurable, and force every round to update the actual proof state rather than merely generate more mathematical prose.

For the Gauss circle project specifically, the immediate next round should not ask the agents to “continue the project.” It should ask:

```text
Target obligation: M9-M2-character-factor / near-collision taxonomy.

A1: formulate the narrowest analytic lemma that would advance M9.
A2: attack the formulation and identify missing endpoint/uniformity assumptions.
A3: produce one executable diagnostic table or source-card audit.

Judge: update proof_obligations.yml only if a precise obligation changes status.
```

That is the highest-leverage architectural change.
