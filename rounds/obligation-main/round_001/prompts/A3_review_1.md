You are A3 Deepseek V4 Pro, acting as API-based proof auditor, algebra checker, and stress-test planner.

Review the other agents' Round 1 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Check algebraic reductions, Poisson/Bessel normalizations, hyperbola decompositions, endpoint conventions, Vaaler/Fejer residuals, Li-Yang/Bombieri-Iwaniec compatibility claims, Mellin-Perron alternatives, and claimed obstructions. Prefer precise parameter ranges and falsifiable lemmas over broad summaries. In reasoning, reserve about 20% of the answer for divergent alternatives or obstruction searches. In review, recommend research-strategy adjustments based on which claims survive verification. For computation-track obligations, do not substitute surrogate phases or random coefficient models as state evidence. Use the actual formulas, actual alpha_h/beta_h/C_h coefficients, and the physical bivariate phase e(hX/(4d)); if a toy surrogate is included, label it as toy evidence and do not use it for status changes. If no committed script, exact command, table, and report are produced, say the computation was not executed. When a proof step is plausible but not certified, say exactly which formula, theorem hypothesis, citation, or numerical check would certify it.



## Active Agents For This Run

Only these agents are active in this run:

- `A1` (ChatGPT Extended Pro): broad strategist, literature scout, proof synthesizer, and default judge
- `A2` (Gemini Pro Deep Think): independent alternative strategist, obstruction finder, and referee-style reviewer
- `A3` (A3 Deepseek V4 Pro): API-based proof auditor, algebra checker, and stress-test planner

Do not mention, score, or assign tasks to inactive agents. If older state text refers to inactive agents, treat it as historical context and reassign any still-useful mathematical check to one of the active agents.

## Protocol

# Multi-AI Mathematical Research Protocol

## Authoritative Mathematical State

The authoritative state is `state/proof_obligations.yml`.

A proof obligation is any theorem, lemma, reduction, external theorem, normalization convention, computation target, source audit, obstruction, or counterexample search whose status matters for the project. Round transcripts in `rounds/` are evidence and audit trail; they are not the state itself.

The compact reading packet in `manifests/reading_packet.md` is generated from the proof-obligation graph. Agents should normally read the packet and graph, not the full transcript history.

## Round Structure

Rounds use strict barrier synchronization:

- Stage B cannot begin until A1, A2, and A3 have completed Stage A.
- Stage C cannot begin until A1, A2, and A3 have completed Stage B.
- Stage D cannot begin until the A1 judge synthesis is complete.
- The next round cannot begin until Stage D has validated or rejected the judge's `State Patch` and regenerated the compact reading packet.

### Stage A: Independent Reasoning

Each agent receives:

- the problem statement,
- the current reading packet,
- the proof-obligation graph,
- the current next-round prompts,
- the prior judge decision if available,
- the agent-specific judge prompt if available,
- the human steering bundle,
- the agent-specific task.

The agent must output:

```text
## Summary
## Target proof obligation
## Main claim or direction
## Detailed reasoning
## Theorem-dependency audit
## Hidden assumptions and potential gaps
## Counterexample or obstruction search
## Verification
## Divergent alternatives and 20% exploration
## Useful lemmas
## What should be tested next
## Proposed state patch, if any
## Confidence
```

Stage A is not a full-project continuation by default. It should attack the selected proof obligation or obligations for the round.

### Stage B: Cross Review

Each agent reviews all other active agents' Stage A outputs, with special attention to proposed state changes.

The review must output:

```text
## Most valuable input from others
## Claims that look correct
## Claims that need proof
## Possible errors or hidden assumptions
## Suggested synthesis
## Research strategy
## Verification
## Proposed state changes to accept or reject
## Score by agent
| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
## Next-round recommendation
## Confidence
```

### Stage C: Judge Synthesis

A1 reads all Stage A outputs and Stage B reviews, then writes the judge synthesis.

The judge must output:

```text
## Selected main route
## Useful fragments by source
## Rejected or risky ideas
## Known gaps
## New lemmas to add
## Counterexample checks to run
## Research strategy adjustment
## State Patch
## Next-round prompts by agent
### For A1
### For A2
### For A3
## Round Assessment
## Confidence
```

The `State Patch` block is the only mechanism for mutating `state/proof_obligations.yml`. Use JSON-compatible YAML so the local validator can parse it without optional dependencies. The `For A1`, `For A2`, and `For A3` blocks are also important: the orchestrator extracts them into `state/next_round_prompts.md` and injects the matching block into the next round's Stage A prompt.

### Stage D: State Update

The orchestrator validates the judge's `State Patch` and then updates:

- `state/proof_obligations.yml`: authoritative proof-obligation graph.
- `state/next_round_prompts.md`: extracted agent-specific next-round tasks.
- `state/last_validation_report.md`: validator result for the latest patch.
- `manifests/reading_packet.md`: compact graph-derived packet for the next round.
- `state/current_state.md`: legacy compact pointer to the latest round and validation result only.

The orchestrator refuses to apply a patch if:

- an unknown status appears;
- an obligation has duplicate or missing required identifiers;
- an open-like obligation lacks `next_action`;
- a computation is promoted as proof;
- an external theorem or source audit lacks a source card;
- a claim is promoted without evidence and a reason;
- `M9` is promoted before both `M9-M1` and `M9-M2` are promoted with uniformity addressed.

Allowed statuses:

```text
proposed
open
blocked
diagnostic_only
source_audit_required
derived_under_assumptions
proved_internal
proved_external_dependency
rejected
```

## Public Repo Rule

The public GitHub repo is the permanent log. Every completed round should be committed and pushed.

Agents should normally read `manifests/reading_packet.md`, not the full repo. Full round files remain available for audit and reconstruction.

## Human Intervention Rule

Human intervention is allowed at any time between stages or rounds.

Human input can appear in:

- `human/current_directives.md`
- `human/goals.md`
- `human/ideas.md`
- `human/references.md`
- `human/inbox/*.md`
- GitHub issues or comments that are manually copied into the files above

Human instructions override previous AI suggestions when they change the target, introduce a reference, reject a route, add a constraint, or change the success criterion.

Agents must explicitly acknowledge relevant human interventions in their next output.

## Mathematical Safety Rules

- Do not mark a claim as proved unless the proof is explicit.
- Preserve failed attempts; they help avoid repeated false starts.
- When a proof step uses an external theorem, name the theorem and state the needed hypotheses.
- Require counterexample or stress-test search for any new lemma.
- Prefer small checkable lemmas over broad vague routes.
- Keep notation stable across rounds.
- Do not claim a new Gauss circle exponent has been proved unless every reduction, smoothing or unsmoothing step, endpoint convention, and external theorem hypothesis is supplied.

## Markdown Output Rule

Return clean Markdown source. For mathematics, use only:

- inline math: `$...$`
- display math:

```text
$$
...
$$
```

Do not use rendered-equation copy formats. Do not use bare bracket math like `[ ... ]`.
Avoid `\[ ... \]` and `\( ... \)` because some web copy tools drop the backslashes.

## Research-Mode Quality Rubric

This is a research-mode run, not a smoke test. Take enough time to reason carefully before answering. Prefer correctness, explicit assumptions, rigorous gap detection, and precise lemma statements over speed or brevity.

Before writing the final response, internally check your proposal against known barriers, missing hypotheses, possible counterexamples, and literature-status uncertainty. In the final answer, report the refined result rather than hidden chain-of-thought.

For reasoning stages, include: main route, precise lemmas, theorem dependencies, hidden assumptions, obstruction or counterexample checks, what would falsify the route, and confidence.

For reasoning stages, dedicate roughly 80% of the mathematical effort to the judge-assigned main route and roughly 20% to divergent exploration. The exploratory part should consider genuinely different proof routes, reductions, counterexample mechanisms, dual formulations, smoothing choices, literature bridges, or computational certificates.

For review stages, include: valuable ideas from other agents, claims that look correct, claims needing proof, likely false or underspecified claims, missing hypotheses, and concrete synthesis recommendations. Also recommend whether the next round should continue the main route, pivot variables, split into subproblems, test a counterexample, build a computation, or allocate one agent to an exploratory alternative.

For judge stages, include: selected route, useful fragments by source, rejected or risky ideas, exact gaps, new lemma statements, research-strategy adjustment, next-round tasks for A1/A2/A3, and confidence.

## Proof-Obligation Workflow Contract

The authoritative mathematical state is `state/proof_obligations.yml`. Treat rounds as work on specific obligations, not as global project transcripts.

Rules:

- Focus on the round target obligations named in the reading packet or judge task.
- Do not promote an obligation unless you provide an exact statement, dependencies, evidence files, and remaining caveats.
- Computations may add diagnostic evidence or next actions, but may not prove theorem or lemma obligations.
- External theorem obligations require source cards before they can be used as proof dependencies.
- The final judge synthesis must include `## State Patch` using JSON-compatible YAML.

## Review-Stage Guardrail

This is Stage B cross review for Round 1.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a compact but deep Stage B referee report of at least 1700 words. Focus on algebraic correctness, hidden hypotheses, normalization constants, theorem dependencies, and claims needing proof. For each reviewed peer, identify one strongest contribution, one most dangerous gap, and one concrete verification task. Include a score table and research-strategy adjustment. Treat uncited external theorem claims as unverified unless the prompt supplied a source; assign missing source checks to A1/A2.

## Problem

# Gauss Circle Problem

## Problem

Let

```text
N(R) = #{(m,n) in Z^2 : m^2 + n^2 <= R^2}.
```

The classical Gauss circle problem asks for the best possible exponent in the error term

```text
N(R) = pi R^2 + E(R).
```

The conjectural bound is

```text
E(R) = O_epsilon(R^{1/2 + epsilon})
```

for every epsilon > 0.

## Research Goal For This Repo

Use a multi-AI collaborative workflow to explore strategies, partial lemmas, obstacles, and proof sketches related to improving or understanding the Gauss circle problem error term.

The immediate goal is not to claim a solution, but to build a rigorous research log:

- identify plausible approaches,
- isolate precise lemmas,
- track gaps,
- test claims against known barriers,
- maintain a best current proof skeleton.

## Initial Directions To Consider

- Poisson summation and Bessel function expansions.
- Exponential sum bounds and exponent pairs.
- Smoothing and unsmoothing arguments.
- Lattice point discrepancy methods.
- Connections to the divisor problem.
- Lower-bound obstructions and omega results.
- Computational checks for small or structured ranges.


## Current State Bundle

--- FILE: state/proof_obligations.yml ---
{
  "schema_version": 1,
  "allowed_statuses": [
    "proposed",
    "open",
    "blocked",
    "diagnostic_only",
    "source_audit_required",
    "derived_under_assumptions",
    "proved_internal",
    "proved_external_dependency",
    "rejected"
  ],
  "tracks": [
    "proof_infrastructure",
    "M9_analytic",
    "computation",
    "source_audit",
    "tooling"
  ],
  "round_selection": {
    "primary_track": "M9_analytic",
    "secondary_track": "computation",
    "target_obligations": [
      "M9-M2-character-factor",
      "M9-near-collision-taxonomy",
      "M9-regression-raw-vs-paired"
    ],
    "round_rule": "Each round should choose one primary track and at most one secondary track."
  },
  "proof_obligations": [
    {
      "id": "GC-target",
      "type": "theorem",
      "track": "proof_infrastructure",
      "title": "Gauss circle conjectural exponent target",
      "status": "open",
      "statement_tex": "For every epsilon > 0, P(X)=N(sqrt(X))-pi X satisfies P(X) <<_epsilon X^(1/4+epsilon).",
      "dependencies": [
        "Conditional-bridge"
      ],
      "implies": [],
      "blockers": [
        "M9"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "state/current_state.md"
        ]
      },
      "owner": "A1",
      "next_action": "Keep the target explicitly conditional until all bridge dependencies, especially M9, are proved."
    },
    {
      "id": "Conditional-bridge",
      "type": "reduction",
      "track": "proof_infrastructure",
      "title": "Conditional bridge from accepted reductions to the target",
      "status": "derived_under_assumptions",
      "statement_tex": "H1-H3 + H4 + R5-Full + M9 imply P(X) <<_epsilon X^(1/4+epsilon).",
      "dependencies": [
        "H1-H3",
        "H4",
        "R5-Full",
        "M9"
      ],
      "implies": [
        "GC-target"
      ],
      "blockers": [
        "M9",
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open."
    },
    {
      "id": "H1-H3",
      "type": "infrastructure",
      "track": "proof_infrastructure",
      "title": "Balanced hyperbola and sawtooth reductions",
      "status": "proved_internal",
      "statement_tex": "The exact symmetric hyperbola identity, periodic chi_4 partial-sum formula, and balanced sawtooth formula reduce P(X) to floor-compatible sawtooth sums up to O(1).",
      "dependencies": [],
      "implies": [
        "Conditional-bridge"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Keep endpoint conventions visible when downstream obligations cite H1-H3."
    },
    {
      "id": "H4",
      "type": "external_theorem",
      "track": "source_audit",
      "title": "Finite Vaaler approximation with floor-compatible residual",
      "status": "source_audit_required",
      "statement_tex": "Use Vaaler's finite approximation to the floor-compatible sawtooth function with Fejer-kernel residual and integer-jump convention.",
      "dependencies": [
        "H4-source-audit"
      ],
      "implies": [
        "Conditional-bridge",
        "R5-Full"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "source_card": "sources/vaaler_1985.md",
      "evidence": {
        "positive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Verify theorem labels, constants, residual convention, and integer values from rendered source pages."
    },
    {
      "id": "H4-source-audit",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Rendered source audit for Vaaler 1985",
      "status": "source_audit_required",
      "statement_tex": "The exact Vaaler theorem, notation, hypotheses, constants, and residual inequality used by H4 must be checked from the rendered paper.",
      "dependencies": [],
      "implies": [
        "H4"
      ],
      "blockers": [],
      "source_card": "sources/vaaler_1985.md",
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ]
      },
      "owner": "A1",
      "next_action": "Complete the source card with rendered page/equation checks."
    },
    {
      "id": "R5-Full",
      "type": "lemma",
      "track": "proof_infrastructure",
      "title": "Fejer residual product-count bound",
      "status": "derived_under_assumptions",
      "statement_tex": "For active D and H_D asymp D X^(-1/4), all first and shifted Fejer residual blocks are O_epsilon(X^(1/4+epsilon)), conditional on H4.",
      "dependencies": [
        "H4"
      ],
      "implies": [
        "Conditional-bridge"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Insert the proof with edge cases into the best proof draft after H4 source audit is complete."
    },
    {
      "id": "M9",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Endpoint bound for fixed Vaaler reciprocal main sums",
      "status": "open",
      "statement_tex": "For X large and X^(1/4) <= D <= X^(1/2), the fixed-coefficient reciprocal sums M_1(D;X), M_2(D;X) satisfy M_i(D;X) <<_epsilon X^(1/4+epsilon), uniformly in all active dyadic D.",
      "dependencies": [
        "H1-H3",
        "H4",
        "R5-Full",
        "M9-M1",
        "M9-M2"
      ],
      "implies": [
        "Conditional-bridge"
      ],
      "blockers": [
        "M9-M2-character-factor",
        "M9-near-collision-taxonomy",
        "M9-endpoint-uniformity"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/round_028/responses/A3-028.md"
        ]
      },
      "owner": "A2",
      "next_action": "Formulate and attack the M2 fourth-moment or near-collision subproblem with the C_h=e(h/4)-e(3h/4) factor retained.",
      "promotion_rule": "May move from open to derived_under_assumptions only if a proof gives uniform bounds for both M1 and M2 over all active dyadic D."
    },
    {
      "id": "M9-M1",
      "type": "sublemma",
      "track": "M9_analytic",
      "title": "M1 fixed-coefficient reciprocal-sum estimate",
      "status": "open",
      "statement_tex": "The M1 dyadic reciprocal main sum with actual Vaaler coefficients is O_epsilon(X^(1/4+epsilon)) uniformly over active D.",
      "dependencies": [
        "H4"
      ],
      "implies": [
        "M9"
      ],
      "blockers": [
        "M9-endpoint-uniformity"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A2",
      "next_action": "Separate any M1 estimate from M2 and state its coefficient hypotheses and D ranges."
    },
    {
      "id": "M9-M2",
      "type": "sublemma",
      "track": "M9_analytic",
      "title": "M2 fixed-coefficient reciprocal-sum estimate",
      "status": "open",
      "statement_tex": "The M2 dyadic reciprocal main sum with actual beta_h=alpha_{h,H_D}C_h coefficients is O_epsilon(X^(1/4+epsilon)) uniformly over active D.",
      "dependencies": [
        "H4",
        "M9-M2-character-factor",
        "M9-near-collision-taxonomy"
      ],
      "implies": [
        "M9"
      ],
      "blockers": [
        "M9-M2-character-factor",
        "M9-near-collision-taxonomy"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A2",
      "next_action": "Retain the two-sided convention and prove or refute the near-collision estimate with actual beta_h weights."
    },
    {
      "id": "M9-M2-character-factor",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "M2 frequency-side character factor",
      "status": "open",
      "statement_tex": "The factor C_h=e(h/4)-e(3h/4)=2i chi_4(h) for odd h and 0 for even h must be retained in M2 estimates and in any pairing or fourth-moment reduction.",
      "dependencies": [
        "H4"
      ],
      "implies": [
        "M9-M2"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A2",
      "next_action": "State the narrowest lemma showing whether the C_h factor helps, hurts, or survives Cauchy/fourth-moment transformations."
    },
    {
      "id": "M9-near-collision-taxonomy",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "M2 fourth-moment near-collision taxonomy",
      "status": "open",
      "statement_tex": "Classify N=0 and 0<|N|~T configurations for the cleared M2 fourth-moment phase, including diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified cases.",
      "dependencies": [
        "M9-M2"
      ],
      "implies": [
        "M9-M2"
      ],
      "blockers": [
        "M9-near-collision-estimate"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/round_027/judge/judge-027.md"
        ]
      },
      "owner": "A2",
      "next_action": "Complete the taxonomy and state the exact weighted bound needed for the near-collision bands."
    },
    {
      "id": "M9-near-collision-estimate",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Weighted near-collision estimate for M2 fourth moment",
      "status": "proposed",
      "statement_tex": "A signed or absolute coefficient-weighted estimate for 0<|N|~T near-collision bands strong enough to imply the M2 endpoint bound.",
      "dependencies": [
        "M9-near-collision-taxonomy"
      ],
      "implies": [
        "M9-M2"
      ],
      "blockers": [],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A2",
      "next_action": "After taxonomy, formulate this as an exact theorem with all coefficient weights and dyadic ranges."
    },
    {
      "id": "M9-endpoint-uniformity",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "Endpoint uniformity over active dyadic D",
      "status": "open",
      "statement_tex": "Any bound used for M9 must hold uniformly for X^(1/4) <= D <= X^(1/2), including endpoint and short-block regimes.",
      "dependencies": [],
      "implies": [
        "M9"
      ],
      "blockers": [],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A2",
      "next_action": "Attach explicit D-range hypotheses to every proposed M1 or M2 estimate."
    },
    {
      "id": "M9-regression-raw-vs-paired",
      "type": "computation",
      "track": "computation",
      "title": "Raw-vs-paired numerical stress test for M9",
      "status": "proposed",
      "statement_tex": "Compare raw two-sided complex M1/M2 formulas with paired real formulas for real weights, and confirm paired formulas fail outside their hypotheses for complex weights.",
      "dependencies": [
        "M9",
        "M9-M2-character-factor"
      ],
      "implies": [],
      "blockers": [],
      "accepted_evidence_level": "diagnostic_only",
      "required_output": [
        "script",
        "command",
        "table",
        "precision log",
        "report.md"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/round_028/responses/A3-028.md"
        ]
      },
      "owner": "A3",
      "next_action": "Produce computations/m9_regression/run.py, outputs/table_small.csv, and report.md; mark all evidence diagnostic_only."
    },
    {
      "id": "Li-Yang-source-audit",
      "type": "source_audit",
      "track": "source_audit",
      "title": "Li-Yang theorem and rendered-PDF audit",
      "status": "source_audit_required",
      "statement_tex": "Record exact theorem hypotheses, variable ranges, weights, and absolute-value placement before using Li-Yang as a dependency or guardrail.",
      "dependencies": [],
      "implies": [],
      "blockers": [],
      "source_card": "sources/li_yang_2023.md",
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex"
        ]
      },
      "owner": "A1",
      "next_action": "Resolve the Case A/B discrepancy from the rendered PDF and update the source card."
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 0 in run `workflow-revision`.

## Current Theorem Target

Target: `P(X)=N(sqrt(X))-pi X <<_epsilon X^(1/4+epsilon)`.

Current status: conditional only. No new Gauss circle exponent has been proved.

## Current Route

H1-H3 + H4 + R5-Full + M9 imply P(X) <<_epsilon X^(1/4+epsilon).

## Active Bottleneck

`M9`: open.

For X large and X^(1/4) <= D <= X^(1/2), the fixed-coefficient reciprocal sums M_1(D;X), M_2(D;X) satisfy M_i(D;X) <<_epsilon X^(1/4+epsilon), uniformly in all active dyadic D.

Current blockers:
- `M9-M2-character-factor` (open): M2 frequency-side character factor
- `M9-near-collision-taxonomy` (open): M2 fourth-moment near-collision taxonomy
- `M9-endpoint-uniformity` (open): Endpoint uniformity over active dyadic D

## Round Target Obligations

- `M9-M2-character-factor` (open, owner `A2`): M2 frequency-side character factor
  Next action: State the narrowest lemma showing whether the C_h factor helps, hurts, or survives Cauchy/fourth-moment transformations.
- `M9-near-collision-taxonomy` (open, owner `A2`): M2 fourth-moment near-collision taxonomy
  Next action: Complete the taxonomy and state the exact weighted bound needed for the near-collision bands.
- `M9-regression-raw-vs-paired` (proposed, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Produce computations/m9_regression/run.py, outputs/table_small.csv, and report.md; mark all evidence diagnostic_only.

## Do-Not-Claim Rules

- Do not claim `M9` or the final Gauss circle target.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use Li-Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Agent Assignments

Use `state/next_round_prompts.md` for any judge-assigned A1/A2/A3 tasks.

Default target split:
- `A1`: synthesis, proof-draft maintenance, source-card discipline, and State Patch authoring.
- `A2`: conservative obstruction analysis for the selected M9 obligations.
- `A3`: executable diagnostics or source-card artifacts, not prose-only plans.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `sources/vaaler_1985.md`
- `sources/li_yang_2023.md`
- `manifests/reading_packet.md`

## Last State Patch

Initial proof-obligation graph seeded from architecture-and-workflow-revised.md.

## Active Obligation Briefs

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: State the narrowest lemma showing whether the C_h factor helps, hurts, or survives Cauchy/fourth-moment transformations.

### M9-near-collision-taxonomy: M2 fourth-moment near-collision taxonomy

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`
- Next action: Complete the taxonomy and state the exact weighted bound needed for the near-collision bands.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `proposed`
- Track: `computation`
- Owner: `A3`
- Next action: Produce computations/m9_regression/run.py, outputs/table_small.csv, and report.md; mark all evidence diagnostic_only.

### GC-target: Gauss circle conjectural exponent target

- Status: `open`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`
- Next action: Keep the target explicitly conditional until all bridge dependencies, especially M9, are proved.

### H4: Finite Vaaler approximation with floor-compatible residual

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Verify theorem labels, constants, residual convention, and integer values from rendered source pages.

### H4-source-audit: Rendered source audit for Vaaler 1985

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Complete the source card with rendered page/equation checks.

### Li-Yang-source-audit: Li-Yang theorem and rendered-PDF audit

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Resolve the Case A/B discrepancy from the rendered PDF and update the source card.

### M9: Endpoint bound for fixed Vaaler reciprocal main sums

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-endpoint-uniformity`
- Next action: Formulate and attack the M2 fourth-moment or near-collision subproblem with the C_h=e(h/4)-e(3h/4) factor retained.

### M9-M1: M1 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-endpoint-uniformity`
- Next action: Separate any M1 estimate from M2 and state its coefficient hypotheses and D ranges.

### M9-M2: M2 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`
- Next action: Retain the two-sided convention and prove or refute the near-collision estimate with actual beta_h weights.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Attach explicit D-range hypotheses to every proposed M1 or M2 estimate.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: After taxonomy, formulate this as an exact theorem with all coefficient weights and dyadic ranges.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.

### R5-Full: Fejer residual product-count bound

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Insert the proof with edge cases into the best proof draft after H4 source audit is complete.

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Generated from the revised proof-obligation workflow seed.

## For A1

Target obligation: `M9-M2-character-factor`.

Formulate the narrowest analytic lemma that would advance `M9` without claiming `M9`. Maintain the conditional bridge and source-card discipline. If status changes are justified, include them only as proposed state changes for the judge to validate.

## For A2

Target obligations: `M9-M2-character-factor` and `M9-near-collision-taxonomy`.

Act as conservative referee. Attack missing endpoint, two-sided, character-factor, near-collision, and uniformity assumptions. Prefer creating precise blockers over broad route advocacy.

## For A3

Target obligation: `M9-regression-raw-vs-paired`.

Produce executable diagnostics or an implementation-ready plan with exact script paths, commands, output tables, precision notes, and limitations. Numerical output is diagnostic only and must not promote `M9`.

--- FILE: state/best_proof_draft.md ---
# Best Proof Draft

No proof draft yet.

--- FILE: state/lemma_bank.md ---
# Lemma Bank

## Proposed

No proposed lemmas yet.

## Plausibly Proved

None yet.

## Rejected Or Risky

None yet.

--- FILE: state/gap_register.md ---
# Gap Register

No gaps registered yet.

--- FILE: sources/vaaler_1985.md ---
# Source Card: Vaaler 1985

## Bibliographic Data

Pending rendered-source audit.

## Local File / URL

Pending.

## Exact Theorem Used

Finite approximation to the floor-compatible sawtooth function with Fejer-kernel residual.

## Original Notation

Pending rendered-page check.

## Project Notation Translation

Used for `H4` in `state/proof_obligations.yml`.

## Hypotheses

- Sawtooth normalization must match the floor-compatible convention.
- Truncation height and Fejer residual conventions must be verified.
- Integer endpoint behavior must be checked.

## Conclusion

Pending exact source transcription.

## Constants / Uniformity / Parameter Ranges

Pending rendered-page check.

## How Used In This Project

Provides the external theorem dependency for the finite Vaaler expansion in the conditional bridge.

## Not Sufficient For

It does not prove `M9`; it only supplies the finite expansion and residual structure used before the main reciprocal-sum estimates.

## Audited By

Pending.

## Audit Status

`source_audit_required`

## Rounds Referencing This Source

- `rounds/web-research-test/round_027/judge/judge-027.md`

--- FILE: sources/li_yang_2023.md ---
# Source Card: Li-Yang 2023

## Bibliographic Data

Pending rendered-PDF audit.

## Local File / URL

- `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`

## Exact Theorem Used

No theorem is currently imported as a dependency. Li-Yang is a guardrail and literature-audit target until exact hypotheses are recorded.

## Original Notation

Pending rendered-PDF reconciliation.

## Project Notation Translation

Pending.

## Hypotheses

Pending exact statement for variables, weights, ranges, and absolute-value placement.

## Conclusion

Pending.

## Constants / Uniformity / Parameter Ranges

Pending.

## How Used In This Project

Only as a source-audit obligation and comparison point for possible Bombieri-Iwaniec style estimates.

## Not Sufficient For

It may not be used as a black-box endpoint theorem for `M9` without a completed source card.

## Audited By

Pending.

## Audit Status

`source_audit_required`

## Rounds Referencing This Source

- `rounds/web-research-test/round_027/judge/judge-027.md`

## Human Intervention Bundle

Human instructions override prior AI suggestions when they are about research direction, target, references, or constraints.

--- HUMAN FILE: human/current_directives.md ---
# Current Human Directives

No active human override yet.

Use this file for instructions that should strongly steer the next round, such as:

- switch the target lemma,
- abandon a route,
- focus on a named paper,
- require a computation,
- change the judging criterion.

# Web model modes and conversation policy

Kind: constraint
Timestamp: 2026-05-31T21:21:36

For web-agent tests and formal rounds, use the three-agent Gauss workflow:

- A1 = ChatGPT Extended Pro through the web UI.
- A2 = Gemini Pro Deep Think through the web UI.
- A3 = Deepseek V4 Pro through the API.

# Research-mode quality target

Kind: constraint
Timestamp: 2026-05-31T21:35:00

This is no longer a smoke test. Use research mode for the three-agent A1/A2/A3 Gauss run. Take substantially more time to reason before answering. Prefer correctness, explicit hypotheses, gap detection, literature-status caution, and precise lemma formulation over speed or brevity. Do not optimize for short answers.

Each reasoning response should include: a main route, precise proposed lemmas, dependencies on known theorems, hidden assumptions, obstruction/counterexample checks, what would falsify the route, and confidence.

Each review should identify: valuable ideas from the other agent, claims that are probably correct, claims needing proof, likely false or underspecified claims, missing hypotheses, and a concrete recommendation for synthesis.

The judge should output: selected route, useful fragments by source, rejected/risky ideas, exact gaps, new lemma statements, next-round tasks, and confidence.

Use clean Markdown source. Use `$...$` for inline math and `$$...$$` for display math. Do not use bare bracket math such as `[ ... ]`.

# Round 9 Li--Yang Source Audit

Kind: reference directive
Timestamp: 2026-06-01T10:15:00

Before making any theorem-level claim about Li--Yang/Bombieri--Iwaniec compatibility, use the actual arXiv source at https://arxiv.org/src/2308.14859. The Round 9 task should audit Li--Yang's exact theorem hypotheses, especially the exponential-sum theorem around `\label{main theorem}`, the definition of `S`, the two conditions on `F`, and the final target `S/H \lesssim_\epsilon T^{\theta^*+\epsilon}`. Do not treat structural phase similarity as theorem applicability.

# Round 11 Free-Exploration Allowance

Kind: next-round directive
Timestamp: 2026-06-01T12:10:00

Starting in Round 11, each reasoning agent should still address the judge's concrete next-round tasks, but may reserve a clearly labeled section for free exploration. In that section, propose one or two genuinely new possibilities: a different decomposition, a transformed sum, a dual formulation, a toy model, a counterexample search, or a literature bridge not already emphasized. Free exploration must remain mathematical and auditable: state the proposed object, why it might help, what hypothesis it would need, and one quick test that could falsify it. Do not let the exploratory section replace the main assigned verification work.

# Standing A2 depth and specificity standard

Kind: workflow constraint
Timestamp: 2026-06-08T02:20:00

For current and future A2 reasoning and review prompts, require Gemini Pro Deep Think to produce long-form, concrete, formula-level referee reports rather than compact answers.

For current and future A2 reasoning prompts, use calibrated low-temperature reasoning mode: conservative mathematical-referee behavior, exact formulas, explicit hypotheses, narrow provisional claims, obstruction checks, reproducible verification tasks, controlled novelty, low rhetoric, and high calibration. A2 must not invent custom status labels. A2 must not pad answers with repeated synonyms, generic process narration, or mechanically inflated sentences. Every paragraph should add a concrete mathematical object, formula, named theorem/hypothesis, boundary condition, counterexample mechanism, or executable verification step; low-information filler paragraphs must be deleted. Before finalizing, A2 must remove high-certainty, route-closing, finality/permanence, dramatic, or totalizing wording, run a real token-family scan, and report only `token-family scan: passed` without listing scanned roots.

For current and future A2 review prompts, use prompt-enforced low-temperature review mode: low-variance conservative referee behavior, exact formula checking, explicit assumptions, narrow provisional claims, reproducible verification tasks, low novelty, low rhetoric, and high calibration. When several phrasings are possible, choose the least conclusive neutral phrasing. Low-temperature mode controls style only; it does not reduce the need for concrete evidence. If a draft is below the hard minimum, A2 must expand with neutral formula-level checks, theorem-hypothesis audits, boundary-case verifications, or explicit falsification tests, not with rhetoric. Before finalizing, A2 must perform a visible approximate word-count self-check. Target 5000-7000 words, with hard minimum 4500 words. If token-family rewriting drops the draft below 4500 words, add neutral mathematical content using additional theorem-hypothesis audit, boundary-case verification, symbolic stress tests, or proof-draft-ready formula audit. Before finalizing, A2 must do a rewrite pass that removes high-certainty, route-closing, finality/permanence, and dramatic wording.

Reasoning standard: target 5500-7500 words, hard minimum 5000 words, at least 14 top-level sections, claim ledger with at least 8 entries, theorem-dependency audit with at least 6 dependencies or missing theorem statements, unsupported-closure audit, at least 5 claim/lemma boxes, at least 5 failure modes, at least 4 concrete stress tests, at least 4 proof-draft-ready formulas/kernels, at least 2 toy-model or finite-parameter checks, and a visible pre-submit calibration check. If expansion is needed, expand with concrete mathematics only, not filler.

Review standard: target 5000-7000 words, hard minimum 4500 words, review every other active agent separately, include a claim ledger with at least 8 reviewed claims, theorem-dependency audit with at least 6 dependencies or missing theorem statements, unsupported-closure/overclaim audit, at least 4 correction or verification items, at least 4 hidden assumptions or failure modes, at least 3 stress tests, a score table, an explicit `## Confidence` section, and research-strategy implications.

For both reasoning and review, every central section must contain concrete formulas, named objects, hypotheses, and explicit failure criteria. A2 must label central claims as [PROVED], [DERIVED-UNDER-ASSUMPTIONS], [HEURISTIC], [CONJECTURED], [ASSUMED], or [LIKELY-FALSE]. Use [PROVED] only when exact hypotheses and a complete proof are supplied. Do not allow numeric confidence above 0.89, custom status labels, percentage-allocation rhetoric, totalizing closure claims, dramatic verdict words, finality/permanence language, lock-in route language, or quoted/listed prohibited rhetoric examples. Before finalizing, A2 must mechanically replace finality/permanence/lock-in wording with provisional audit wording, run a hard token-family scan, and report only `token-family scan: passed` without listing the scanned roots.

--- HUMAN FILE: human/goals.md ---
# Human Goals

## Active Goal

Build a public GitHub based workflow for multi-AI collaboration on the Gauss circle problem.

## Research Goals

- Keep a rigorous public record of each round.
- Make every AI distinguish proof, conjecture, and gap.
- Allow human intervention at any time.
- Maintain a compact reading packet for the next round.

--- HUMAN FILE: human/ideas.md ---
# Human Ideas

Add new mathematical ideas here. The orchestrator includes this file in every round prompt.

--- HUMAN FILE: human/references.md ---
# Human References

Add papers, books, links, theorem names, or notes here.

Recommended entry format:

```text
Title:
Author:
Link or citation:
Relevant theorem/section:
Why it matters:
```

## Li--Yang 2023

Title: An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem

Authors: Xiaochun Li and Xuerui Yang

Links:

- Abstract/PDF: https://arxiv.org/abs/2308.14859
- TeX source: https://arxiv.org/src/2308.14859

Version note: arXiv:2308.14859v2, dated 2023-09-14 on the arXiv abstract page.

Source-audit anchors from downloaded TeX source:

- Intro theorem: `\label{theorem in introduction}` around source lines 132--138 gives the stated Gauss circle and divisor bounds with exponent `theta^* = 0.314483...`.
- Definition of exponent: `\label{definition of theta}` around source lines 141--145 defines `theta^*`.
- First spacing setup: Section `Improvement on the first spacing problem`, especially source lines around 245--285, introduces the first-spacing norm and the role of `q > 4`.
- Exponential-sum theorem: `\label{main theorem}` around source line 845 is the theorem to audit before importing any Li--Yang estimate.
- Final reduction to circle/divisor: source lines around 1116--1126 reduce to sums of the form `S` and the target estimate `S/H \lesssim_\epsilon T^{\theta^*+\epsilon}`.
- Theorem-application checks: source lines around 1164--1172 explicitly say the prerequisites of the main theorem must be verified before use.

Why it matters: Round 9 should audit the exact theorem-level hypotheses from the TeX source, not just the abstract or previous AI summaries. The key question is whether the current H5r-F/H5r-B targets match Li--Yang's `S/H` theorem, coefficient class, weight class, parameter ranges, and absolute-value placement, or only share a broad reciprocal-sum phase shape.

--- RECENT HUMAN NOTE: human/inbox/20260531-212136_constraint_web-model-modes-and-conversation-policy.md ---
# Web model modes and conversation policy

Kind: constraint
Timestamp: 2026-05-31T21:21:36

For web-agent tests and formal rounds, use ChatGPT Extended Pro for gpt_pro_thinking and Gemini Pro Deep Think for gemini_deep_think. Prefer one persistent conversation per agent per run, so each web AI has continuity across reasoning, review, judge/next-round prompts. The public repo and reading_packet.md remain the authoritative memory; web conversation memory is helpful but not authoritative.

## Outputs To Review

--- OUTPUT FROM A1 ---
## Summary

This is A1’s independent reasoning packet for the target obligation `M9-M2-character-factor`. The uploaded prompt assigns A1 to formulate the narrowest analytic lemma that advances `M9` without claiming `M9`, while preserving the conditional bridge and source-card discipline. The current reading packet says the active bottleneck is `M9`, with blockers `M9-M2-character-factor`, `M9-near-collision-taxonomy`, and `M9-endpoint-uniformity`; it also states explicitly that the current theorem target is conditional only and that no new Gauss circle exponent has been proved. :contentReference[oaicite:0]{index=0} The prompt further states that `M9-M2-character-factor` is open and asks for the narrowest lemma showing whether the factor $C_h=e(h/4)-e(3h/4)$ helps, hurts, or survives Cauchy/fourth-moment transformations. :contentReference[oaicite:1]{index=1}

The main conclusion here is an exact algebraic and transformation-level lemma for $\mathcal M_2$:

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h,
\end{cases}
$$

and, with the Vaaler coefficient

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

the actual $\mathcal M_2$ coefficient

$$
\beta_{h,H}:=\alpha_{h,H}C_h
$$

simplifies to the real even coefficient

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)\,1_{2\nmid h}.
$$

This is the narrowest useful advancement of `M9-M2-character-factor`: it proves exactly where the frequency-side character is present, where it is lost under standard Cauchy--Schwarz, and where it survives in the fourth moment. It does **not** prove `M9`, `M9-M2`, or the Gauss circle target.

The actionable output is to split `M9-M2-character-factor` into three smaller proof obligations:

1. **M2 beta-coefficient algebra:** proved algebraic normalization, conditional on the H4 coefficient convention.
2. **M2 second-moment sign-loss diagnostic:** standard $h$-Cauchy squaring destroys the $\chi_4(h)$ sign and leaves only odd-frequency support.
3. **M2 fourth-moment character-survival identity:** the fourth moment retains a fourfold character product and has a cleared-denominator resonance integer $N$ that should feed `M9-near-collision-taxonomy`.

## Target proof obligation

Primary target:

$$
\texttt{M9-M2-character-factor}.
$$

The state says this obstruction concerns the frequency-side factor

$$
C_h=e(h/4)-e(3h/4),
$$

which equals $2i\chi_4(h)$ for odd $h$ and $0$ for even $h$, and it must be retained in $\mathcal M_2$ estimates and in any pairing or fourth-moment reduction. :contentReference[oaicite:2]{index=2}

Relevant adjacent obligations:

- `M9-M2`: open. It asks for the dyadic reciprocal main sum with actual coefficients $\beta_h=\alpha_{h,H_D}C_h$ to be $O_\epsilon(X^{1/4+\epsilon})$ uniformly over active $D$. :contentReference[oaicite:3]{index=3}
- `M9-near-collision-taxonomy`: open. It asks for classification of $N=0$ and $0<|N|\sim T$ configurations for the cleared $\mathcal M_2$ fourth-moment phase. :contentReference[oaicite:4]{index=4}
- `M9-regression-raw-vs-paired`: proposed computation. It requires raw two-sided complex M1/M2 formulas to be compared with paired real formulas for real weights and explicitly says numerical evidence is diagnostic only. :contentReference[oaicite:5]{index=5}

The current conditional bridge remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This bridge must not be promoted while `M9` remains open. :contentReference[oaicite:6]{index=6}

## Main claim or direction

The selected direction is to formalize the exact $\mathcal M_2$ coefficient algebra and then state a precise transformation dichotomy:

- Under raw two-sided $\mathcal M_2$, the $C_h$ factor is not a cosmetic phase. It combines with $\alpha_{h,H}$ to produce a real, even, residue-sensitive coefficient $\beta_{h,H}$.
- Under standard positive-weight second moments in the $h$ variable, the character sign is squared away. The resulting kernel is character-blind in $h$ except for odd-frequency support.
- Under the two-sided fourth moment, the character survives as

$$
\chi_4(|h_1h_2h_3h_4|),
$$

with coefficient weights retained. This is the smallest algebraic fact that can feed a serious `M9-near-collision-taxonomy` attack.

The proposed lemma advances `M9` only in the sense of narrowing the next analytic target. It does not estimate the fourth moment or prove endpoint cancellation.

## Detailed reasoning

### 1. Normalization of the $\mathcal M_2$ main term

For an active dyadic block

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4},
$$

write the $\mathcal M_2$ main term in the form

$$
\mathcal M_2(D;X)
=
4S_2(D;X),
$$

where

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}B_h(D;X),
$$

with

$$
B_h(D;X)
=
\sum_d w_D(d)e(hX/(4d)),
$$

and

$$
\beta_{h,H}
=
\alpha_{h,H}C_h.
$$

Here

$$
C_h=e(h/4)-e(3h/4),
$$

and the H4 Vaaler coefficient convention is

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

Vaaler’s paper is the relevant finite-sawtooth source: Project Euclid lists Jeffrey D. Vaaler, “Some extremal functions in Fourier analysis,” *Bull. Amer. Math. Soc. (N.S.)* 12(2), 183--216, April 1985, and AMS gives the same bibliographic data. :contentReference[oaicite:7]{index=7} The exact H4 source card still needs final theorem/equation transcription in the repo, and H4 remains `source_audit_required`. The uploaded Vaaler source-audit material identifies Theorem 18 for the residual inequality and Theorem 6, equation (2.28), for the Fourier coefficient function. :contentReference[oaicite:8]{index=8}

Now compute $C_h$ exactly. Since $e(t)=e^{2\pi i t}$,

$$
e(h/4)=i^h,
\qquad
e(3h/4)=(-i)^h.
$$

If $h$ is even, the two terms agree and $C_h=0$. If $h$ is odd, then

$$
C_h=2i\chi_4(h).
$$

Therefore

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}
\cdot
2i\chi_4(h)
=
-\frac{\Phi(|h|/(H+1))}{\pi h}\chi_4(h)
$$

for odd $h$, and $\beta_{h,H}=0$ for even $h$.

Since $\chi_4(-h)=-\chi_4(h)$ and $-h$ changes the sign of the denominator, the quotient $\chi_4(h)/h$ is even:

$$
\frac{\chi_4(-h)}{-h}
=
\frac{\chi_4(h)}{h}.
$$

Thus the coefficient can be written as

$$
\boxed{
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)\,1_{2\nmid h}.
}
$$

This is real and even:

$$
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

This is the first narrow lemma. It is purely algebraic once H4 fixes the coefficient convention.

### 2. Paired real formula and its exact hypotheses

Assume $w_D$ is real-valued. Then

$$
B_{-h}(D;X)=\overline{B_h(D;X)}.
$$

Because $\beta_{-h,H}=\beta_{h,H}$, the two-sided sum becomes

$$
S_2(D;X)
=
2\sum_{1\le h\le H_D}\beta_{h,H_D}\operatorname{Re}B_h(D;X).
$$

Using the expression for $\beta_h$ gives

$$
S_2(D;X)
=
-\frac{2}{\pi}
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\operatorname{Re}B_h(D;X).
$$

Since $\mathcal M_2=4S_2$,

$$
\boxed{
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
}
$$

This formula is valid for real $w_D$. It is not valid as written for arbitrary complex weights. This is why `M9-regression-raw-vs-paired` is important as a diagnostic obligation; the computation target explicitly asks A3 to compare raw two-sided complex formulas with paired real formulas for real weights and confirm paired formulas fail outside their hypotheses. :contentReference[oaicite:9]{index=9}

### 3. Standard $h$-Cauchy loses the character sign

Let

$$
S_2=\sum_h \alpha_h C_h B_h.
$$

A standard positive-weight Cauchy--Schwarz step with weights $|\alpha_h|$ gives

$$
|S_2|^2
\le
\left(\sum_h|\alpha_h|\right)
\left(\sum_h|\alpha_h||C_h|^2|B_h|^2\right).
$$

But

$$
|C_h|^2
=
\begin{cases}
4,&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

Thus the second factor is

$$
4\sum_{\substack{1\le |h|\le H_D\\2\nmid h}}
|\alpha_h||B_h|^2.
$$

The sign $\chi_4(h)$ is gone. Expanding $|B_h|^2$ gives the reciprocal kernel

$$
4\sum_{\substack{1\le |h|\le H_D\\2\nmid h}}
|\alpha_h|
\sum_{d_1,d_2}
w_D(d_1)\overline{w_D(d_2)}
e\left(
\frac{hX}{4}
\left(
\frac1{d_1}-\frac1{d_2}
\right)
\right).
$$

So a weighted $h$-second moment has an acceptable diagonal size but no frequency-character sign. The remaining odd-$h$ restriction is still arithmetic information, but it is much weaker than a signed $\chi_4(h)$ coefficient.

This proves a bounded obstruction:

**M2 $h$-Cauchy sign-loss diagnostic.** Any proof route that first applies a positive-weight second moment in $h$ to $S_2=\sum_h\alpha_hC_hB_h$ loses the $\chi_4(h)$ sign and retains only odd-frequency support. Such a route may still prove a bound by character-blind reciprocal-sum technology, but it is not exploiting the M2 character factor as a sign.

This diagnostic is not a no-go theorem for all approaches to $\mathcal M_2$. It does not cover fourth moments, open-path statistics, residue-paired estimates, signed bilinear forms, or a theorem that directly estimates $S_2$ without squaring away $C_h$.

### 4. Unweighted $h$-Cauchy has an endpoint diagonal problem

If instead one uses the crude unweighted Cauchy step

$$
|S_2|^2
\le
H_D
\sum_{1\le |h|\le H_D}
|\beta_h|^2|B_h|^2,
$$

then the diagonal part of $|B_h|^2$ contributes on the order of

$$
H_D\sum_{1\le |h|\le H_D}|\beta_h|^2D.
$$

Since $|\beta_h|\ll 1/|h|$ and $\sum_h h^{-2}\ll1$, this is bounded by

$$
\ll H_DD.
$$

At the top dyadic range $D\asymp X^{1/2}$ and $H_D\asymp DX^{-1/4}\asymp X^{1/4}$, this becomes

$$
H_DD\asymp X^{3/4}.
$$

The squared endpoint target for $\mathcal M_2\ll X^{1/4+\epsilon}$ is

$$
X^{1/2+\epsilon}.
$$

So the unweighted $h$-Cauchy diagonal is too large at the endpoint. This explains why the weighted second moment is natural, and why its sign-loss is a real obstruction.

### 5. The fourth moment preserves the character product

The two-sided fourth moment is the first standard moment where the character can survive longer. Define

$$
S_2(D;X)
=
\sum_{1\le |h|\le H}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Then

$$
|S_2|^4
=
\sum_{\mathbf h}
\sum_{\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
\prod_{j=1}^4 w_j(d_j)
e\left(
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
\right),
$$

where $w_1=w_3=w_D$ and $w_2=w_4=\overline{w_D}$ if complex weights are allowed.

For real weights and real even $\beta_h$, the coefficient factor is

$$
\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}.
$$

Using

$$
\beta_h
=
-\lambda_h\chi_4(|h|)1_{2\nmid h},
\qquad
\lambda_h
=
\frac{\Phi(|h|/(H+1))}{\pi |h|},
$$

we get

$$
\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}
=
\lambda_{h_1}\lambda_{h_2}\lambda_{h_3}\lambda_{h_4}
\chi_4(|h_1h_2h_3h_4|)
\prod_{j=1}^4 1_{2\nmid h_j}.
$$

Thus the fourth moment retains the product of four frequency-side characters.

Clearing denominators in the phase gives the exact resonance integer

$$
N
=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

The phase is

$$
e\left(\frac{XN}{4d_1d_2d_3d_4}\right).
$$

This is the exact object that should feed `M9-near-collision-taxonomy`.

### 6. Character survival is not uniform across collision families

The fourth-moment character factor survives algebraically, but it can collapse on structured subfamilies. This must be recorded before anyone treats the fourth moment as automatically character-aware.

Let

$$
\mathfrak C(\mathbf h)
=
\chi_4(|h_1h_2h_3h_4|)
\prod_{j=1}^4 1_{2\nmid h_j}.
$$

The following cases are immediate.

**Fully paired $h$-diagonal.** If $|h_1|=|h_2|$ and $|h_3|=|h_4|$, then

$$
\mathfrak C(\mathbf h)=1
$$

on odd support. The character has squared away.

**Pair-swapped family.** If $|h_1|=|h_4|$ and $|h_2|=|h_3|$, then again

$$
\mathfrak C(\mathbf h)=1.
$$

**Semi-diagonal family.** If only one pair is forced, for instance $|h_1|=|h_2|$, then

$$
\mathfrak C(\mathbf h)=\chi_4(|h_3h_4|).
$$

Some sign remains, but only in the unpaired frequencies.

**Unpaired near-collisions.** If no $|h_i|$ pairing occurs, then the full fourfold sign

$$
\chi_4(|h_1h_2h_3h_4|)
$$

survives.

This is a useful taxonomy seed: exact diagonal families are compatible with target-size mass checks, while near-collision families are the relevant test of whether the character factor gives cancellation beyond absolute majorization.

### 7. Narrow analytic lemma proposed

The narrowest lemma that advances `M9-M2-character-factor` without claiming `M9` is the following.

**Lemma M2-CF. Coefficient-factor dichotomy for $\mathcal M_2$.**

Assume H4 fixes the coefficient convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

For $1\le |h|\le H$, set

$$
C_h=e(h/4)-e(3h/4),
\qquad
\beta_{h,H}=\alpha_{h,H}C_h.
$$

Then:

1. $C_h=0$ for even $h$ and $C_h=2i\chi_4(h)$ for odd $h$.

2. The actual $\mathcal M_2$ coefficient is

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)\,1_{2\nmid h}.
$$

In particular, $\beta_{h,H}\in\mathbb R$ and $\beta_{-h,H}=\beta_{h,H}$.

3. If $w_D$ is real-valued, then

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
$$

4. Any positive-weight second moment in $h$ that pairs $C_h$ with $\overline{C_h}$ replaces the character factor by

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

Thus such a second-moment route loses the $\chi_4(h)$ sign.

5. The two-sided fourth moment retains the fourfold character factor

$$
\chi_4(|h_1h_2h_3h_4|)
\prod_{j=1}^4 1_{2\nmid h_j},
$$

with cleared-denominator resonance integer

$$
N
=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

This lemma is algebraic. It should be marked as a proved internal algebraic reduction only if H4’s coefficient convention is accepted or stated as conditional on H4. It does not imply the endpoint bound.

## Theorem-dependency audit

1. **H4: finite Vaaler approximation.** Used only to define the exact coefficient $\alpha_{h,H}$. The source card is still `source_audit_required`; Vaaler is not being used here to prove a new analytic estimate. The article metadata is verified by Project Euclid and AMS. :contentReference[oaicite:10]{index=10}

2. **No Li--Yang theorem is used.** Li--Yang remains a source-audit and guardrail item. The prompt says not to treat structural phase similarity as theorem applicability and identifies source-audit anchors for Li--Yang’s theorem, definition of $S$, and target estimate. :contentReference[oaicite:11]{index=11} The arXiv PDF states that Li and Yang use the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley’s second-spacing results. :contentReference[oaicite:12]{index=12}

3. **No Huxley, Bourgain--Watt, exponent-pair, or Bombieri--Iwaniec input is used.** The current packet is algebraic and transformation-level.

4. **H1--H3 and R5-Full are not used in the proof of M2-CF.** They remain part of the conditional bridge. The state says H1--H3 + H4 + R5-Full + M9 imply the target, but M9 is open. :contentReference[oaicite:13]{index=13}

5. **The fourth-moment expansion uses only finite sums.** No limiting argument, completion, stationary phase, smoothing, or source theorem is used.

6. **Raw-vs-paired formula depends on real weights.** If $w_D$ is complex-valued, the paired real formula need not match the raw two-sided definition.

## Hidden assumptions and potential gaps

1. **H4 coefficient sign.** The formula

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}
$$

is treated as the repo convention. Since H4 remains source-audit-required, any final proof draft must verify the exact coefficient sign, normalization of $e(t)$, and the endpoint convention.

2. **Definition of $\chi_4$ on negative integers.** The simplification $\beta_{-h}=\beta_h$ uses the standard Dirichlet-character convention $\chi_4(-h)=-\chi_4(h)$ for odd $h$. This should be stated explicitly in the proof draft.

3. **Real weight hypothesis.** The paired formula for $\mathcal M_2$ requires $B_{-h}=\overline{B_h}$, which requires real dyadic weights. If a smooth partition uses complex weights or numerical code accidentally inserts complex phases into $w_D$, the paired formula fails.

4. **$\Phi$ positivity and endpoint values are not needed here.** The algebra only needs $\Phi$ real on $0<u<1$. No monotonicity or symmetry $\Phi(1-u)=\Phi(u)$ is used. In fact, $\Phi(1-u)=\Phi(u)$ is false except at $u=1/2$.

5. **Fourth-moment survival is not cancellation.** The factor $\chi_4(|h_1h_2h_3h_4|)$ survives algebraically, but may become $1$ on important diagonal or pair-swapped configurations. The fourth moment is only potentially character-aware in the unpaired and semi-paired sectors.

6. **Near-collision scaling is still open.** The correct weighted estimate for $0<|N|\sim T$ bands is not proved. The proposed lemma only supplies the exact $N$ and exact character factor.

7. **Uniformity in $D$ is not addressed.** All formulas are uniform algebraically in $X^{1/4}\le D\le X^{1/2}$, but no bound uniform in $D$ is proved.

8. **No endpoint theorem imported from the literature.** Li--Yang’s current known exponent $\theta^*=0.314483\ldots$ remains above $1/4$; the current packet does not invoke their theorem as an endpoint input. :contentReference[oaicite:14]{index=14}

## Counterexample or obstruction search

### Obstruction 1: weighted $h$-Cauchy removes the character

The weighted second moment is tempting because its diagonal is acceptable. But

$$
C_h\overline{C_h}=|C_h|^2=4\,1_{2\nmid h}.
$$

This is a direct obstruction to any claim that the standard weighted $h$-Cauchy route exploits $\chi_4(h)$.

A falsification test for any proposed second-moment proof is:

- Write the exact $h$-kernel after Cauchy.
- If the coefficient is $|C_h|^2$ or $|\beta_h|^2$, label the method character-blind with respect to the sign of $\chi_4(h)$.
- Require any claimed gain to come from an odd-frequency reciprocal-sum theorem, not from character cancellation.

### Obstruction 2: unweighted $h$-Cauchy diagonal is too large at $D=X^{1/2}$

The unweighted $h$-Cauchy diagonal is

$$
\asymp D H_D.
$$

At $D=X^{1/2}$, this is

$$
X^{1/2}X^{1/4}=X^{3/4},
$$

while the squared endpoint target is $X^{1/2+\epsilon}$. This is a concrete endpoint obstruction.

### Obstruction 3: fourth-moment diagonals may square away signs

The fourth moment retains the character only before diagonal restrictions. On full pairings, the character factor becomes $1$. Therefore any fourth-moment route must show that diagonal and pair-swapped families have acceptable mass by size alone, then use signs or oscillation only for the remaining near-collision families.

### Obstruction 4: CRI can be neutral or adverse

If

$$
S_2=2i(\Sigma_1-\Sigma_3),
$$

then the ratio

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}{|\Sigma_1|^2+|\Sigma_3|^2}
$$

can range from $0$ to $2$ when the denominator is nonzero. Values near $1$ are neutral, not evidence for residue interference. Values near $2$ are adverse. CRI is a falsification statistic, not a proof input.

### Obstruction 5: false $\Phi$ symmetry

Any code or proof that folds $h$-coefficients using $\Phi(1-u)=\Phi(u)$ is invalid. The usable conjugacy is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

which follows from the sign of $h$ and the reality of $\Phi$, not from any $u\mapsto1-u$ symmetry.

## Verification

The algebra can be checked by direct symbolic calculation.

1. For $h$ even:

$$
e(h/4)=e(3h/4),
$$

so $C_h=0$.

2. For $h\equiv1\pmod4$:

$$
e(h/4)=i,\qquad e(3h/4)=-i,
$$

so

$$
C_h=2i=2i\chi_4(h).
$$

3. For $h\equiv3\pmod4$:

$$
e(h/4)=-i,\qquad e(3h/4)=i,
$$

so

$$
C_h=-2i=2i\chi_4(h).
$$

4. Combining with $\alpha_h$:

$$
\alpha_hC_h
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}
\cdot
2i\chi_4(h)
=
-\frac{\Phi(|h|/(H+1))}{\pi h}\chi_4(h).
$$

For $h<0$, $\chi_4(h)/h=\chi_4(|h|)/|h|$. Hence $\beta_h$ is real and even.

5. For real weights:

$$
B_{-h}
=
\sum_d w_D(d)e(-hX/(4d))
=
\overline{B_h}.
$$

Therefore

$$
\sum_{1\le |h|\le H}\beta_hB_h
=
2\sum_{1\le h\le H}\beta_h\operatorname{Re}B_h.
$$

6. For the fourth moment, expanding $|S_2|^4=S_2\overline{S_2}S_2\overline{S_2}$ gives the displayed phase and coefficient product. Multiplying by $d_1d_2d_3d_4$ gives the displayed resonance integer $N$.

These checks are finite algebra and should be reproducible in A3’s raw-vs-paired diagnostic script.

## Divergent alternatives and 20% exploration

### Alternative A: residue-class interference before moments

Instead of moving immediately to $|S_2|^4$, split positive frequencies into residues:

$$
\Sigma_r(D;X)
=
\sum_{\substack{1\le h\le H_D\\h\equiv r\pmod4}}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\}.
$$

Then

$$
\mathcal M_2(D;X)
=
-\frac8\pi(\Sigma_1-\Sigma_3).
$$

A possible lemma would be:

**CRI cancellation lemma.** For all active $D$,

$$
|\Sigma_1-\Sigma_3|^2
\ll_\epsilon X^{1/2+\epsilon}.
$$

This directly implies the $\mathcal M_2$ target. The difficulty is that bounding only the cross term $\operatorname{Re}(\Sigma_1\overline{\Sigma_3})$ is not enough; one must control the whole difference. A quick falsification test is to compute

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}{|\Sigma_1|^2+|\Sigma_3|^2}
$$

at the top range $D\asymp X^{1/2}$. If the ratio stays near $1$ or $2$ in structured samples, residue interference is unlikely to be the main route.

### Alternative B: Poisson in the denominator variable for $\mathcal M_2$

For fixed $h$, the inner sum

$$
B_h(D;X)=\sum_d w_D(d)e(hX/(4d))
$$

can be attacked by a B-process/Poisson transform. The stationary point for the integral phase

$$
\frac{hX}{4u}-\xi u
$$

satisfies

$$
u_0\asymp \sqrt{\frac{hX}{|\xi|}},
$$

so the dual length is roughly

$$
|\xi|\asymp \frac{hX}{D^2}.
$$

At the endpoint $D\asymp X^{1/2}$ and $h\asymp H_D\asymp X^{1/4}$, this gives dual length $\asymp X^{1/4}$, a balanced-looking range. For smaller $D$, the dual length grows.

The transformed phase is of square-root type. Existing guardrails from previous rounds apply: the continuous Hessian of $\sqrt{Xhm}$ is degenerate, so generic full-rank two-dimensional stationary phase or decoupling cannot be invoked. The exact lemma needed would be a signed spacing estimate for the transformed two-variable sum with $\chi_4(h)$ retained. A quick falsification test is to run the endpoint transformation with stationary amplitudes and compare signed, unsigned, and operator-norm majorants.

### Alternative C: signed finite Fourier tail instead of Vaaler main term

One could ask whether the specific Vaaler coefficient

$$
\frac{\Phi(h/(H+1))}{h}
$$

has cancellation not captured by arbitrary coefficient tests. Since $\Phi$ is smooth and real, summation by parts in $h$ could convert the M2 sum into partial sums over residue classes. This route would need a uniform bound for

$$
\sum_{\substack{1\le h\le H_0\\h\equiv r\pmod4}}
\operatorname{Re}B_h(D;X)
$$

with $r=1,3$, uniformly for $H_0\le H_D$. The quick falsification test is Abel summation: if partial sums have the same size as arbitrary-sign stress tests, fixed Vaaler weights do not help enough by themselves.

## Useful lemmas

### Lemma CF1: M2 beta-coefficient algebra

**Status proposed:** `derived_under_assumptions`, conditional on H4 coefficient normalization.

For $1\le |h|\le H$,

$$
\beta_{h,H}
=
\alpha_{h,H}(e(h/4)-e(3h/4))
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)\,1_{2\nmid h}.
$$

Hence $\beta_{h,H}$ is real and even.

### Lemma CF2: Paired real $\mathcal M_2$ formula

**Status proposed:** `proved_internal` once CF1 is accepted, with hypothesis that $w_D$ is real.

For real $w_D$,

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
$$

### Lemma CF3: weighted $h$-Cauchy sign-loss diagnostic

**Status proposed:** `proved_internal` as a bounded-scope obstruction.

Under the positive $|\alpha_h|$-weighted Cauchy step,

$$
|S_2|^2
\le
\left(\sum_h|\alpha_h|\right)
\left(\sum_h|\alpha_h||C_h|^2|B_h|^2\right),
$$

the factor $C_h$ contributes only

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

The $\chi_4(h)$ sign is lost.

### Lemma CF4: fourth-moment character-survival identity

**Status proposed:** `proved_internal` algebraic identity.

The two-sided fourth moment has coefficient factor

$$
\lambda_{h_1}\lambda_{h_2}\lambda_{h_3}\lambda_{h_4}
\chi_4(|h_1h_2h_3h_4|)
\prod_{j=1}^4 1_{2\nmid h_j},
$$

where

$$
\lambda_h=\frac{\Phi(|h|/(H+1))}{\pi |h|}.
$$

The cleared resonance integer is

$$
N
=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

### Lemma CF5: diagonal character-collapse classification seed

**Status proposed:** `proposed`, pending full near-collision taxonomy.

In the fourth moment, full pairings of the absolute $h$ values force the character factor to $1$; semi-pairings leave a twofold character; unpaired configurations retain a fourfold character. This should become a subcase list inside `M9-near-collision-taxonomy`.

## What should be tested next

1. **Raw-vs-paired regression for CF1 and CF2.** For real $w_D$, compute the raw two-sided complex $\mathcal M_2$ and the paired real formula above. The absolute error should be at numerical precision. For complex $w_D$, the paired formula should fail unless modified.

2. **Weighted $h$-Cauchy kernel regression.** Build the kernel

$$
K_{2;d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)\overline{w_D(d_2)}
\sum_h|\alpha_h||C_h|^2
e\left(
\frac{hX}{4}
\left(
\frac1{d_1}-\frac1{d_2}
\right)
\right).
$$

Confirm that replacing $C_h$ by $2i\chi_4(h)$ and then squaring gives only $4\,1_{2\nmid h}$.

3. **Fourth-moment binning with character factor.** For small but nontrivial endpoint-like ranges, enumerate $(h_1,h_2,h_3,h_4,d_1,d_2,d_3,d_4)$ and bin by:
   - $N=0$ diagonal;
   - pair-swapped;
   - semi-diagonal;
   - denominator-paired;
   - mixed;
   - sign-symmetric;
   - truncation-edge;
   - unclassified;
   - near-collision bands $0<|N|\sim T$.

Report both signed and absolute weighted mass using the actual $\beta_h$.

4. **CRI falsification.** Compute

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}{|\Sigma_1|^2+|\Sigma_3|^2}
$$

at $D\asymp X^{1/2}$ and at one intermediate $D$. Values near $1$ should deprioritize CRI as a main route.

5. **Endpoint uniformity check.** Repeat all diagnostics for $D=X^\delta$ with at least $\delta=1/4,1/3,1/2$. The obligation `M9-endpoint-uniformity` explicitly requires active-range uniformity. :contentReference[oaicite:15]{index=15}

6. **Li--Yang source-card discipline.** Do not use Li--Yang as an input. If cited, only cite it as a guardrail until the source card records theorem hypotheses, variables, weights, ranges, and absolute-value placement. The uploaded prompt states this restriction explicitly. :contentReference[oaicite:16]{index=16}

## Proposed state patch, if any

proposed_state_patch:
  add_obligations:
    - id: "M9-M2-beta-algebra"
      type: "normalization"
      track: "M9_analytic"
      title: "Exact beta_h coefficient algebra for M2"
      status: "derived_under_assumptions"
      statement_tex: "Assuming the H4 Vaaler coefficient convention alpha_{h,H}=-Phi(|h|/(H+1))/(2 pi i h), the M2 coefficient beta_{h,H}=alpha_{h,H}(e(h/4)-e(3h/4)) equals -Phi(|h|/(H+1)) chi_4(|h|) 1_{2 not divides h}/(pi |h|), hence is real and even."
      dependencies:
        - "H4"
        - "M9-M2-character-factor"
      implies:
        - "M9-M2-character-factor"
      blockers:
        - "H4-source-audit"
      evidence:
        positive:
          - "A1 current reasoning packet"
        negative: []
        inconclusive: []
      owner: "A1"
      next_action: "Have A3 verify raw two-sided beta_h and paired real formulas numerically for real weights and failure for complex weights."
    - id: "M9-M2-h-cauchy-sign-loss"
      type: "obstruction"
      track: "M9_analytic"
      title: "Weighted h-Cauchy loses the M2 frequency character sign"
      status: "derived_under_assumptions"
      statement_tex: "For S_2=sum_h alpha_h C_h B_h, the positive |alpha_h|-weighted h-Cauchy step replaces C_h by |C_h|^2=4 1_{2 not divides h}; therefore the chi_4(h) sign is lost and only odd-frequency support remains."
      dependencies:
        - "M9-M2-beta-algebra"
      implies:
        - "M9-M2-character-factor"
      blockers: []
      evidence:
        positive:
          - "A1 current reasoning packet"
        negative: []
        inconclusive: []
      owner: "A1"
      next_action: "Use this as a bounded-scope diagnostic only; do not treat it as a no-go theorem for fourth moments or signed bilinear estimates."
    - id: "M9-M2-fourth-moment-character-survival"
      type: "reduction"
      track: "M9_analytic"
      title: "M2 fourth-moment character survival identity"
      status: "derived_under_assumptions"
      statement_tex: "The two-sided fourth moment of S_2 retains the character factor chi_4(|h_1 h_2 h_3 h_4|) on odd h_j and has cleared resonance integer N=h_1 d_2 d_3 d_4-h_2 d_1 d_3 d_4+h_3 d_1 d_2 d_4-h_4 d_1 d_2 d_3."
      dependencies:
        - "M9-M2-beta-algebra"
      implies:
        - "M9-near-collision-taxonomy"
      blockers:
        - "M9-near-collision-estimate"
      evidence:
        positive:
          - "A1 current reasoning packet"
        negative: []
        inconclusive: []
      owner: "A1"
      next_action: "A2 should classify exact and near-collision configurations using this N and the retained fourfold character factor."
  update_obligations:
    - id: "M9-M2-character-factor"
      status: "open"
      next_action: "Use M9-M2-beta-algebra, M9-M2-h-cauchy-sign-loss, and M9-M2-fourth-moment-character-survival to decide whether the next M2 attack should use fourth moments, CRI, or a direct signed bilinear estimate. Do not promote M9-M2 without a uniform endpoint estimate."
    - id: "M9-regression-raw-vs-paired"
      status: "proposed"
      next_action: "Add beta_h coefficient checks, weighted h-Cauchy sign-loss checks, and fourth-moment N-binning to the requested raw-vs-paired diagnostic report."

## Confidence

High confidence in the algebraic identities for $C_h$, $\beta_h$, the paired real formula under real weights, and the sign-loss statement under positive-weight $h$-Cauchy.

High confidence that these identities advance `M9-M2-character-factor` without proving `M9`.

Moderate confidence that the fourth-moment character-survival identity is the right next analytic object for `M9-near-collision-taxonomy`.

Low confidence that a standard second-moment or black-box Li--Yang/Bombieri--Iwaniec theorem proves `M9-M2` at the endpoint without a new signed or endpoint-strength estimate. Li--Yang remains a guardrail rather than a theorem dependency.

No confidence claim is made for the Gauss circle exponent itself; `M9` and the final target remain open.

--- OUTPUT FROM A2 ---
## Summary

This report provides the Stage A independent reasoning and obstruction analysis for Agent A2, operating strictly under the low-temperature mathematical referee standard. The investigation targets the formal analytical bottlenecks designated as `M9-M2-character-factor` and `M9-near-collision-taxonomy` within the authoritative Gauss circle proof-obligation graph. The primary objective is to rigorously deconstruct the finite Vaaler reciprocal main sum $M_2(D;X)$ and extract the exact arithmetic, geometric, and topological constraints governing its fourth moment. By executing an explicit algebraic expansion of the frequency-side character weight $C_h = e(h/4) - e(3h/4)$, we formally prove that the composite modified Fourier coefficients natively collapse into a strictly real and even sequence, algebraically eliminating complex phase-conjugation anomalies. We construct the full 8-class Diophantine taxonomy for the cleared $M_2$ fourth-moment phase and demonstrate that the continuous $L^4$ norm geometry is rigidly constrained by a cross-parity alternating sign signature $(-1)^{N/2}$.

Furthermore, we isolate a severe structural mathematical obstruction in the standing route: the Gallagher discrete-to-continuous integral mapping mapping fails unconditionally across the entire active dyadic domain. The spatial sequence derivative induces an aliasing penalty of $X^{3/4}/D \gg 1$, mathematically prohibiting the use of continuous integral bounds to estimate the discrete Diophantine summations. The absolute boundaries at $D = X^{1/4}$ and $D = X^{1/2}$ are formally audited, demonstrating catastrophic derivative singularities that falsify any claim of uniform continuous spacing. To satisfy the 20% exploration mandate, a rigorous divergent alternative utilizing the Voronoi J-Bessel summation formula is constructed to bypass the hyperbola reduction entirely. The state graph is subsequently patched to formalize these strict mathematical blockers.

## Target proof obligation

The formal analysis directly addresses the following specified sub-obligations drawn from the authoritative state graph:

1.  `M9-M2-character-factor` (Status: open, Track: M9_analytic): State the narrowest analytic lemma showing whether the explicit frequency-side character factor $C_h = e(h/4) - e(3h/4)$ helps, hurts, or mathematically survives Cauchy-Schwarz and fourth-moment transformations.
2.  `M9-near-collision-taxonomy` (Status: open, Track: M9_analytic): Complete the discrete taxonomy and classify the exact configuration conditions for the cleared $M_2$ fourth-moment rational phase numerator $N = 0$ and the near-collision continuous bands $0 < |N| \sim T$.
3.  Implicit sub-context `M9-endpoint-uniformity`: Actively attack and verify the missing boundary and uniformity assumptions across the entire dyadic progression $X^{1/4} \le D \le X^{1/2}$.

## Main claim or direction

We establish three strict, mathematically provisional claims that dictate the trajectory of `M9`.
First, the frequency character factor $C_h = 2i\chi_4(h)$ unconditionally survives the un-Cauchy'd fourth-moment expansion, mutating into a rigid structural constraint $16(-1)^{N/2}$ that dictates alternating subtractive cancellation across the near-collision phase gap $N$. Applying absolute value inequalities prior to this sequence geometrically inflates the density and strictly prevents reaching the $X^{1/4+\epsilon}$ threshold.
Second, the integer phase numerator $N$ satisfies a rigid Diophantine Parity Sieve driven by the spatial denominators $d_i$, rendering continuous uniform integration metrics mathematically invalid for off-diagonal topology.
Third, the standing `M9` methodology of applying continuous fourth-moment integrals to discrete spatial summations over $d \sim D$ is formally obstructed by the Gallagher aliasing penalty $X^{3/4}/D$. This derivative scalar is strictly $\gg 1$ for all active blocks, meaning the discrete sequence fundamentally aliases the continuous phase. The research direction must pivot to discrete dual-Poisson transformations (Van der Corput B-process) or abandon the hyperbola method in favor of the Voronoi continuous spectrum.

## Detailed reasoning: Algebraic isolation and symmetries of the M2 frequency-side character factor

To rigorously satisfy the `M9-M2-character-factor` obligation, we execute the exact algebraic reduction of the periodic fractional residual phase introduced by the finite Vaaler approximation (obligation `H4`). The standard Dirichlet hyperbola partition generates a discrete indicator sum containing the fractional part $\psi(X/d)$. The finite Vaaler trigonometric approximation replaces this with the polynomial $\psi_H(x) = \sum_{0 < |h| \le H} \alpha_h e(hx)$.

The fundamental coefficients for the asymmetric sawtooth wave are purely imaginary and odd:
$$ \alpha_{h, H} = \frac{-1}{2\pi i h} \left(1 - \frac{|h|}{H+1}\right) $$
The specified character weight introduced by the floor-compatible symmetric integer-jump convention is defined on the frequency domain $h \in [-H_D, H_D] \setminus \{0\}$ as:
$$ C_h = e\left(\frac{h}{4}\right) - e\left(\frac{3h}{4}\right) $$
where $e(z) = \exp(2\pi i z)$. We expand this projection using Euler's transcendental identity:
$$ C_h = \exp\left(i \frac{\pi h}{2}\right) - \exp\left(i \frac{3\pi h}{2}\right) = i^h - (-i)^h $$

We mechanically evaluate this parity factor across the integer modulo-4 classes:
For any even integer frequency $h = 2k$:
$$ C_{2k} = i^{2k} - (-i)^{2k} = (-1)^k - (-1)^k = 0 $$
For any odd integer frequency $h = 2k+1$:
$$ C_{2k+1} = i^{2k+1} - (-i)^{2k+1} = i(-1)^k - (-i)(-1)^k = 2i(-1)^k $$
The algebraic term $(-1)^k$ for odd inputs $2k+1$ is the exact mathematical definition of the non-principal Dirichlet character modulo 4, denoted $\chi_4(h)$.
This establishes the strict identity: $C_h = 2i \chi_4(h)$ for all integer $h$. The factor acts as an exact parity annihilator, instantly halving the spectral density of the summation space by zeroing all even frequencies.

The composite `M2` reciprocal sum coefficient becomes $\beta_h = \alpha_h C_h$. Substituting the derived forms:
$$ \beta_h = \left( \frac{-1}{2\pi i h} \left(1 - \frac{|h|}{H_D+1}\right) \right) \left( 2i \chi_4(h) \right) = - \frac{1}{\pi h} \left(1 - \frac{|h|}{H_D+1}\right) \chi_4(h) $$
Because the valid frequency $h$ is strictly odd, we explicitly examine the coefficient behavior under sequence negation $h \to -|h|$. The Dirichlet character $\chi_4$ is an odd function: $\chi_4(-|h|) = -\chi_4(|h|)$.
$$ \beta_{-|h|} = - \frac{1}{\pi (-|h|)} \left(1 - \frac{|-h|}{H_D+1}\right) (-\chi_4(|h|)) = - \frac{1}{\pi |h|} \left(1 - \frac{|h|}{H_D+1}\right) \chi_4(|h|) = \beta_{|h|} $$
This derivation rigorously proves that the composite sequence $\beta_h$ is strictly real and exactly symmetric (even). The entire summation $M_2(D;X) = \sum_d \sum_h \beta_h e(hX/d)$ over the two-sided domain $[-H_D, H_D] \setminus \{0\}$ algebraically reduces to a purely real-valued sequence. The analytical complexity of tracking independent complex-conjugate cross-phases in the higher-order moment expansions is therefore mathematically eliminated by the inclusion of $C_h$.

## Detailed reasoning: Fourth-moment near-collision taxonomy and Diophantine phase constraints

To formally evaluate the continuous geometry of $M_2(D;X)$, analytic number theory constructs the continuous $L^4$ mean value integration over a localized spatial interval $t \in [X, 2X]$. The un-Cauchy'd expanded sum takes the exact form:
$$ \int_X^{2X} |M_2(D;t)|^4 dt = \sum_{\mathbf{d}} \sum_{\mathbf{h}} \left(\prod_{j=1}^4 \beta_{h_j}\right) \int_X^{2X} \exp\left( 2\pi i t \left( \frac{h_1}{d_1} + \frac{h_2}{d_2} - \frac{h_3}{d_3} - \frac{h_4}{d_4} \right) \right) dt $$
Since $\beta_h$ is strictly symmetric, the negative signs in the spatial phase $\Delta = \frac{h_1}{d_1} + \frac{h_2}{d_2} - \frac{h_3}{d_3} - \frac{h_4}{d_4}$ do not induce complex conjugation on the coefficient sequence.
Let the common continuous volume be $V = d_1 d_2 d_3 d_4 \asymp D^4$. The exact integer numerator is the cleared fourth-moment phase gap:
$$ N = h_1 d_2 d_3 d_4 + h_2 d_1 d_3 d_4 - h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3 $$

We rigorously establish the 8-class topological taxonomy for the $(h_j, d_j)$ coordinate configurations representing the near-collision states:

1.  **Class 1: Exact Trivial Diagonal ($N=0$)**: Configurations mapping to strict pairwise index matching. For example, $h_1=h_3, d_1=d_3$ and $h_2=h_4, d_2=d_4$. The unweighted volume of this exact state space is identically $(D H_D)^2 = O(D^2 H_D^2)$.
2.  **Class 2: Pair-Swapped Symmetry ($N=0$)**: The structural inverse matching mapping $h_1=h_4, d_1=d_4$ and $h_2=h_3, d_2=d_3$. The volume remains precisely identical, $O(D^2 H_D^2)$.
3.  **Class 3: Semi-Diagonal Fractional Collapse ($N=0$)**: Two spatial fractions reduce to identical rational equivalencies without explicit integer variable matching. For instance, $h_1/d_1 = h_3/d_3$, which requires the linear constraint $h_1 d_3 = h_3 d_1$. The discrete solution density requires the Dirichlet divisor bound $\tau_2(n)$, generating an inflated volume of $O(D^2 H_D^2 \log D)$.
4.  **Class 4: Denominator-Paired Planar Resonance ($N=0$)**: Spatial cross-resonance where the denominators match, $d_1 = d_2$ and $d_3 = d_4$, yielding the reduced hyper-plane $h_1 + h_2 - h_3 - h_4 = 0$.
5.  **Class 5: Fully Mixed Irrational Manifold ($N=0$)**: Irreducible algebraic solutions where no internal pair of fractions sums to zero, yet the global aggregate identically cancels. For example, $1/4 + 1/12 - 1/6 - 1/6 = 0$. The counting bounds here require deep geometry-of-numbers lattice reductions.
6.  **Class 6: Sign-Symmetric Oscillatory States ($N=0$)**: Specific mixed sub-configurations where the parity multiplier $\prod \chi_4(h_i)$ evaluates exactly to $-1$, generating a strictly negative spatial weight that directly subtracts from the positive definite $L^4$ main term.
7.  **Class 7: Ultra-Near Collision Continuous Band ($0 < |N| \le T_{band}$)**: The strictly non-vanishing continuous phase regime. The integral $\int_X^{2X} e(t \Delta) dt$ mechanically enforces a stationary cancellation threshold. For the exponential cancellation to fail and contribute to the mean value, we require $|\Delta| \ll X^{-1}$. Thus $|N| / V \ll X^{-1}$, establishing the near-collision band boundary $T_{band} \asymp D^4 X^{-1}$.
8.  **Class 8: Vaaler Truncation Edge Collapse**: Edge configurations bounded tightly by $|h_j| \approx H_D$, where the Vaaler edge taper weights $1 - |h|/H_D \to 0$ cause violent density suppression, formally contradicting standard uniform point-counting geometry theorems.

## Detailed reasoning: Endpoint uniformity analysis and failure at dyadic boundaries

The operational proof graph demands that any derived bounding architecture must hold uniformly across the entire designated dyadic progression $D \in [X^{1/4}, X^{1/2}]$. The Vaaler frequency cutoff is dynamically bound to the physical block size via the balancing requirement $H_D = \lfloor D X^{-1/4} \rfloor$. We execute a rigorous differential analysis on the spatial phase $f(d) = \frac{h X}{d}$ at the absolute geometric endpoints to verify this critical uniformity assumption.

Treating the spatial parameter $d$ as continuous, the formal phase derivatives evaluate to:
First derivative: $f'(d) = -\frac{h X}{d^2}$
Second derivative: $f''(d) = \frac{2 h X}{d^3}$

**Analysis at the Left Boundary Limit ($D = X^{1/4}$):**
At this geometric extreme, the Vaaler frequency envelope collapses entirely: $H_D = \lfloor X^{1/4} X^{-1/4} \rfloor = 1$. The discrete frequency sequence restricts exclusively to $h \in \{-1, 1\}$.
The second derivative scale parameter $\lambda_2$ becomes $|f''(d)| \asymp \frac{(1) X}{(X^{1/4})^3} = \frac{X}{X^{3/4}} = X^{1/4}$.
Because the derivative scale $|f''(d)| \gg 1$, continuous analytical heuristics apply the Van der Corput second-derivative exponent pair $(1/2, 1/2)$, which bounds the spatial sum structurally by $\ll |f''|^{1/2} D + |f''|^{-1/2}$.
Evaluating this at the left boundary: $(X^{1/4})^{1/2} X^{1/4} + (X^{1/4})^{-1/2} = X^{1/8} X^{1/4} + X^{-1/8} = X^{3/8}$.
This is a catastrophic mathematical failure. An absolute sum bound of $X^{3/8}$ at the left endpoint radically exceeds the targeted Gauss circle exponent $X^{1/4+\epsilon}$. Furthermore, because $H_D = 1$, we are attempting to apply a continuous infinite-asymptote exponential sum integration theorem to a sequence containing exactly two elements. This represents a degenerate analytical limit.

**Analysis at the Right Boundary Limit ($D = X^{1/2}$):**
At the upper extreme, the Vaaler limit expands to $H_D = \lfloor X^{1/2} X^{-1/4} \rfloor = X^{1/4}$.
The second derivative scale parameter evaluates to $|f''(d)| \asymp \frac{X^{1/4} X}{(X^{1/2})^3} = \frac{X^{5/4}}{X^{3/2}} = X^{-1/4}$.
Because $|f''(d)| \ll 1$, the continuous phase curve is heavily flattened. The Weyl A-process (differencing) degenerates entirely. We are forced to rely on the Kusmin-Landau first derivative test, which requires the distance to the nearest integer $||f'(d)||$ to be unconditionally bounded away from zero.
However, evaluating the first derivative scale: $f'(d) \asymp \frac{X^{1/4} X}{(X^{1/2})^2} = \frac{X^{5/4}}{X} = X^{1/4}$.
Because the first derivative magnitude spans a massive absolute interval of size $X^{1/4}$, it mechanically crosses the integers exactly $O(X^{1/4})$ times. At every single integer intersection $f'(d) \in \mathbb{Z}$, a violent stationary phase resonance occurs. These resonant locations strictly mandate a discrete dual transformation via Poisson summation (the Van der Corput B-process).

This explicit differential analysis proves that endpoint uniformity is a mathematically false assumption. The core geometric nature of the rational phase shifts violently from accelerating convex limits ($f'' \gg 1$) at the left boundary to highly resonant, pseudo-linear limits ($f'' \ll 1, f' \gg 1$) at the right boundary. No monolithic integration formula can span this parameter chasm.

## Detailed reasoning: Two-sided Vaaler coefficient summation limitations

The `M9` sub-problem requires strict adherence to the "actual Vaaler coefficients", prohibiting generic heuristic coefficient replacement. The finite Fourier expansion of the periodic asymmetric sawtooth function $\psi(x)$ is intrinsically a symmetric two-sided discrete sum $-H \le h \le H$.

The exact Vaaler analytical approximation asserts:
$$ \left| \psi(x) - \sum_{0 < |h| \le H} \alpha_{h} e(hx) \right| \le \frac{1}{2H+2} \sum_{|h| \le H} \left( 1 - \frac{|h|}{H+1} \right) e(hx) $$
The absolute geometric error term is strictly bounded by an unconditionally positive Fejér smoothing kernel of identical degree $H$.
When this finite discrete approximation is algebraically inserted into the Gauss circle block sum over the spatial variable $d \sim D$, the error matrix generates a rigidly positive spatial summation trace:
$$ E_{Vaaler} = \sum_{d \sim D} \frac{1}{2H_D+2} \sum_{|h| \le H_D} \left( 1 - \frac{|h|}{H_D+1} \right) e\left(\frac{hX}{d}\right) $$
Because the Fejér taper kernel is strictly non-negative in the frequency domain, there exists absolutely zero destructive spectral cancellation over the parameter $h$ before the absolute bounding envelope is applied.
The explicit magnitude of the zero-frequency baseline term $h=0$ inside the error bounding sum is exactly $\frac{1}{2H_D+2} \cdot 1$.
Summing this continuous baseline over the spatial block $d \sim D$ evaluates to a strict minimum residual error of $\frac{D}{2H_D+2}$.
Applying the required balancing constraint $H_D \asymp D X^{-1/4}$, the residual evaluates identically to:
$$ \frac{D}{D X^{-1/4}} = X^{1/4} $$
This derivation verifies that the exact Vaaler continuous error threshold flawlessly matches the required Gauss circle bound $X^{1/4}$.

However, this architecture relies entirely on the untested hypothesis that the non-zero oscillating frequencies $h \neq 0$ inside the Fejér kernel sum exhibit massive exponential cancellation over the spatial variable $d$.
For $h \neq 0$, the spatial residual trace is $\frac{1}{H_D} \sum_{d \sim D} \sum_{h=1}^{H_D} (1 - h/H_D) \cos(2\pi h X / d)$.
If this structural sum fails to demonstrate strictly superior bounds compared to $O(D)$, the Fejér kernel oscillations will unconditionally overflow the $X^{1/4}$ envelope. Specifically, near the right boundary $D = X^{1/2}$, if the inner integer trace over $d$ experiences a stationary phase plateau where $X/d \approx \text{integer}$, the geometric cosine evaluates locally to $+1$. The un-cancelled sum escalates to $H_D$, creating localized density spikes $\frac{1}{H_D} \cdot H_D \cdot (\text{number of resonant } d)$ that mathematically falsify the required bound.

## Detailed reasoning: The role of cross-parity correlations in exponential sums

The `M9-M2` expansion incorporates the exact character weight $C_h$ deep inside the fourth-moment summation geometry. We must explicitly trace the interaction of this parity coefficient.
As derived in Section 4, the combined fourth-moment coefficient weight is $W = 16 \chi_4(h_1) \chi_4(h_2) \chi_4(h_3) \chi_4(h_4)$.
Let the frequency gap coordinate be exactly $N = h_1 + h_2 - h_3 - h_4$. (Note: previously defined as $h_1-h_2+h_3-h_4$; the sign assignment on the un-squared sequence dictates the mapping. We will adhere to the symmetric mapping used for the phase $\Delta$.)
By the fundamental parity properties of the non-principal character on strictly odd frequency spaces, $\chi_4(h_1 h_2 h_3 h_4) = (-1)^{N/2}$.
This strictly alternating parity signature is a profound cross-parity structural correlation. It dictates that the amplitude generated by any near-collision manifold configuration in the fourth moment is entirely governed by the modulo arithmetic of its integer gap.
- If the integer gap $N \equiv 0 \pmod 4$, the evaluation $N/2$ is even, and the associated scalar weight is strictly $+16$.
- If the integer gap $N \equiv 2 \pmod 4$, the evaluation $N/2$ is odd, and the associated scalar weight is strictly $-16$.

This algebraic alternating structure acts as the singular mathematical obstruction preventing the exponentially dense fully mixed irrational manifolds ($N \neq 0$) from catastrophically overwhelming the continuous $L^4$ metric norm.
Consider the frequent heuristic error known as Absolute Value Displacement. An invalid bounding technique attempts to suppress the complex summation logic by commuting the absolute value limits inside the frequency sequence:
$$ \int_X^{2X} \left| \sum_d \sum_h \beta_h e(hX/d) \right|^4 dt \le \sum_{\mathbf{d}} \sum_{\mathbf{h}} |\beta_h|^4 \left| \int \exp(\dots) dt \right| $$
By enforcing the absolute boundary constraint $|\chi_4(\dots)| = 1$, the alternating signature $(-1)^{N/2}$ is permanently annihilated.
Without this alternating subtractive parity, the evaluation of the continuous near-collision density escalates. The continuous near-collision integral $\int e(N f(t)) dt$ is strictly bounded by the Kusmin-Landau limit $\ll \frac{X}{|N| D^2}$.
Summing this strictly positive absolute trace over the near-collision gap parameter generates an isolated logarithmic divergence $\sum_{N=1}^{H_D} 16 \frac{X}{N D^2} \asymp \frac{X}{D^2} \log(H_D)$.
If applied universally across the sequence space, this unconditionally generates bounding scalars that exceed $X^{1/4+\epsilon}$.

To compound the obstruction, the structural transition from the continuous exponential integral to the physical discrete integer summation $\sum_{m=D}^{2D} |S(m)|^4$ is governed by Gallagher's Sobolev mapping inequality. The transition error is scaled tightly by the maximal phase derivative magnitude $\lambda = \max |S'(t)| / |S(t)|$.
Evaluating the continuous sequence derivative yields $\lambda \asymp \frac{H_D X}{D^2} = \frac{(D X^{-1/4}) X}{D^2} = \frac{X^{3/4}}{D}$.
This explicit discrete-to-continuous derivative scalar is strictly $\gg 1$ for all parameter states $D \le X^{1/2}$. Because $\lambda \gg 1$, the continuous integral fundamentally fails to capture the high-frequency aliasing of the discrete spatial lattice. It is mathematically invalid to bound the `M9` Diophantine matrices using isolated continuous integral topological mappings.

## Theorem-dependency audit

To validate the insertion of these structural boundaries and parity obstructions into the active graph, the explicit boundary hypotheses of the following 6 foundational theorems must be audited:

1.  **Vaaler's Trigonometric Approximation Kernel**: Dependency requires absolute verification that the positive Fejér sequence $W(h,H)$ converges precisely without introducing discontinuous geometric phase shifts that would violate the real, even symmetry of $\beta_h$.
2.  **Dirichlet Character Orthogonality Modulo 4**: Dependency assumes the linear sum limit $\sum \chi_4(h) \ll 1$ holds efficiently over highly truncated sub-intervals of length $H_D \asymp 1$.
3.  **Gallagher's Discrete-to-Continuous Lemma (Sobolev Inequality)**: The mapping requires the derivative scalar threshold $\lambda \ll 1$. We have audited this and formally proved the hypothesis is violently violated ($\lambda \asymp X^{3/4}/D \gg 1$).
4.  **Van der Corput Exponent Pairs Theory**: Dependency requires the baseline continuity limit $f''(x) \ge c > 0$. We have audited this and established a catastrophic limit violation at the $D = X^{1/2}$ boundary where the curvature vanishes.
5.  **Kusmin-Landau First Derivative Envelope**: Dependency requires the absolute phase derivative distance to nearest integer $||f'(x)|| \ge \delta > 0$ to prevent singular integration poles during discrete summation.
6.  **Hardy/Voronoi Summation Formula for $r_2(n)$**: Dependency utilized in the divergent alternative route requires exact analytical bounds on the divergent J-Bessel contour tails upon truncation.

## Hidden assumptions and potential gaps

We isolate five critical, mathematically verified failure modes embedded within the standard generic treatment of the `M9` sub-obligations:

1.  **Triangle Inequality Premature Annihilation**: Bounding the structural fourth-moment topology by applying continuous absolute value inequalities prior to the frequency summations. This perfectly destroys the $(-1)^{N/2}$ cross-parity subtractive cancellation matrix.
2.  **Spatial Derivative Disconnect (Aliasing)**: Operating under the assumption that the discrete arithmetic point-counting sum $\sum S(m)$ flawlessly parallels the continuous topological integral $\int S(t) dt$. The proven aliasing penalty $X^{3/4}/D \gg 1$ rigidly decouples them.
3.  **Truncation Edge Reflection Artifacts**: Approximating the finite Vaaler attenuation scalar $1 - |h|/H_D$ dynamically as a continuous constant $1 + O(|h|/H_D)$. At the extreme left dyadic block where $H_D = 1$ and $h=1$, this scalar evaluates to precisely $0$, not $1 + \epsilon$.
4.  **Parity Decorrelation Geometric Sieve**: Assuming the spacing density of the phase gap $N$ is unconditionally uniform across $\mathbb{Z}$. Our established Diophantine Sieve proves $N$ parity is rigidly slaved to the even/odd combinatorial subsets of the spatial parameter denominators $d_i$.
5.  **Continuous Endpoint Extrapolation**: Extrapolating analytical $L^4$ integral norms designed for the limit $H \to \infty$ into the severely restricted local boundaries where the frequency space degenerates into exactly $O(1)$ countable states.

## Unsupported-closure audit

Operating under the strict referee calibration standard, an extensive audit of the internal AI reasoning logs reveals persistent vulnerability for unsupported geometric closure. Any claim attempting to categorize `M9` or `M9-near-collision-taxonomy` as mathematically resolved or `proved_internal` by applying continuous integration topologies over the entire interval $X^{1/4} \le D \le X^{1/2}$ is structurally invalid. The derivation of the discrete-to-continuous aliasing obstruction $X^{3/4}/D$ formally blocks such universal continuity heuristics. The sub-obligations must remain open until a discrete, overlapping dual-frequency mechanism (e.g., Van der Corput B-process duals) is formulated to neutralize the specific $X^{3/8}$ boundary breakdown. Zero definitive exponent closure limits are approved.

## Counterexample or obstruction search

We execute a rigorous, formulaic mathematical obstruction that explicitly refutes the assumed feasibility of the unweighted continuous $L^4$ geometric methodology at the upper parameter boundary.

Consider the absolute Diagonal Overflow Obstruction.
Let a heuristic proof attempt to establish the unconditional bound $P(X) \ll X^{1/4}$ by bounding the unweighted continuous fourth moment integral $\int_X^{2X} |M_2(D; t)|^4 dt \ll X^2$.
We mechanically isolate the Class 1 Exact Trivial Diagonal, where the discrete numerator identically evaluates to $N=0$.
At the absolute upper geometric edge, the parameters scale to $D = X^{1/2}$ and $H_D = X^{1/4}$.
The unweighted topological volume of exactly mapped index tuples $(h_i, d_i)$ is strictly $V_{diag} = D^2 H_D^2$.
Evaluating this parameter limit yields $V_{diag} = (X^{1/2})^2 (X^{1/4})^2 = X^1 X^{1/2} = X^{1.5}$.
For every identically matched tuple within this subset, the phase vanishes $\Delta = 0$, causing the localized oscillatory integral $\int_X^{2X} e(0) dt$ to evaluate purely to the interval length $X$.
The structural, strictly positive-definite contribution to the continuous fourth moment is precisely $V_{diag} \cdot X = X^{1.5} \cdot X = X^{2.5}$.
Because the sum of absolute squared magnitudes in the diagonal $L^4$ expansion cannot mathematically be negative, no other topological class can subtract from this geometric baseline volume.
The verified mass $X^{2.5}$ radically exceeds the targeted threshold integral limit of $X^{2.0}$ by a vast scaling gap of $X^{1/2}$.
Taking the fourth root, the RMS error contribution bounds strictly to $(X^{2.5} / X)^{1/4} = X^{3/8} \gg X^{1/4}$.
This formally constitutes an absolute mathematical obstruction. Any independent, unweighted block summation route is provably falsified.

## Verification

To computationally secure the algebraic constraints and differential limits established herein, we stipulate four strict executable stress tests:

1.  **Symbolic M2 Coefficient Symmetry Test**: Agent A3 must deploy a `sympy`/`numpy` python script to exactly evaluate the complex Vaaler sequence formula multiplied by the discrete $C_h$ character. Generate arrays for $h \in [-101, 101]$ and apply `assert np.all(np.isreal(beta))` and `assert np.all(beta == beta[::-1])` to computationally lock the real/even property.
2.  **Diophantine Parity Sieve Matrix Enumeration**: Script an exhaustive loop over the test bounds $d_i \in [10, 40]$ computing the integer numerator $N$. Programmatically classify the odd/even parity of $N$ exclusively against the Boolean metric logic rule $\sum (d_i \pmod 2) \equiv 1 \pmod 2$.
3.  **Gallagher Discrete-Continuous Aliasing Check**: Implement numerical integration to compute $\int_D^{2D} |S(t)|^4 dt$ and sequence accumulation to compute $\sum_{m=D}^{2D} |S(m)|^4$ using a synthetic accelerated polynomial phase $\exp(i \lambda m^2)$. Iterate the multiplier $\lambda$ across the critical limit of $1$ to definitively output the exact point of geometric divergence.
4.  **Farey-Adjacent Density Mapping**: Generate the localized Farey sequence subspace $d_2 = d_1 + 1, d_4 = d_3 - 1$ mapped to static boundaries. Tally the exact numeric volume of solutions satisfying the near-collision threshold $|N| \ll D^4 / X^{1/2}$ to empirically test the isolated local density scaling at $D=X^{1/4}$.

## Finite-parameter sanity checks and toy models

1.  **The Left Endpoint Singularity Model**: Restrict coordinates to the scaled finite domain $X=10^8$ and $D=100$. This rigidly locks $H_D = 1$. The exponential matrix physically degenerates to a dimension of $2$. Execute a manual trace sum of $\sum_{d=100}^{200} e(\pm 10^8/d)$ to observe the total absence of continuous asymptotic topological cancellation mechanisms.
2.  **The Diagonal Overflow Model**: Fix bounds $X=10^8$ and $D=10000$ ($D=X^{1/2}$). Execute the pure diagonal combinatorial expansion count for $N=0$. Verify the physical output volume scales squarely past the $(10^8)^2 = 10^{16}$ threshold, validating the Class 1 bounds counterexample.

## Divergent alternatives and 20% exploration

Given the explicitly proven algebraic structural failure of the independent $X/d$ hyperbola block sums (specifically the unweighted $X^{3/8}$ overflow and the Gallagher aliasing threshold limit $X^{3/4}/D$), analytical rigor mandates exploring a strictly continuous divergence mechanism that bypasses the Dirichlet hyperbola logic entirely: The **Hardy-Voronoi J-Bessel Continuous Expansion**.

The foundational Dirichlet hyperbola reduction geometrically truncates the $m^2 + n^2 \le X$ circular summation lattice into independent vertical $d$ strips. This action arbitrarily shatters the underlying circular radial symmetry and mechanically introduces the catastrophic sawtooth edge residuals that generate the Vaaler $M_2$ coefficient singularities.
A structurally divergent analytical alternative applies the dual two-dimensional Poisson summation transform directly to the global circular indicator function. The exact transcendental geometric identity yields the Voronoi circle expansion:
$$ N(X) = \pi X + \frac{X^{1/4}}{\pi} \sum_{n=1}^\infty \frac{r_2(n)}{n^{3/4}} \cos\left( 2\pi \sqrt{n X} - \frac{3\pi}{4} \right) + O(X^{\epsilon}) $$

Why does this route geometrically evade the previously proven obstructions?
1.  **Asymptotic Phase Regularity**: The violent fractional reciprocal phase $X/d$ is universally replaced by the square-root phase trajectory $g(n) = \sqrt{nX}$. Evaluated across any active block interval $n \sim N$, the phase derivative metrics behave flawlessly: $g'(n) \asymp \sqrt{X/N}$ and $g''(n) \asymp \sqrt{X} N^{-3/2}$.
2.  **Geometric Left Endpoint Evasion**: We evaluate the Van der Corput exponent pair $(1/2, 1/2)$ bound acting on the square-root sequence second derivative. The local unweighted dyadic block sequence mass maps exactly to $|g''|^{1/2} N \asymp (\sqrt{X} N^{-3/2})^{1/2} N = X^{1/4} N^{1/4}$. Multiplying by the natively embedded geometric scalar amplitude $n^{-3/4}$ generates the bound $X^{1/4} N^{1/4} N^{-3/4} = X^{1/4} N^{-1/2}$. This series bound mechanically converges uniformly to $O(X^{1/4})$ upon sequential geometric summation.
3.  **Cross-Parity Structural Embedding**: The algebraically troublesome $C_h$ alternating parity constraint isolated in `M9` is entirely bypassed. The character logic is unconditionally absorbed strictly into the modular definition of the sum-of-squares representation counter $r_2(n) = 4\sum \chi_4(d)$.

To execute a mathematical falsification test for this alternative Voronoi pathway, we must assess the limits of sequence truncation. The conditionally convergent infinite continuous sequence must be analytically truncated at a bounded limit $N_{max}$. Bounding the subsequent $L^2$ spatial energy of the truncated series tail requires deep complex contour limits involving the sub-convexity parameters of the Riemann Zeta and Dirichlet $L$-functions. The exploratory target is to map whether a strict finite parameter boundary $N_{max} \asymp X^{1/2}$ permits exact integral closure without introducing secondary integration artifacts surpassing $O(X^{1/4})$.

## Useful lemmas

```markdown
### Lemma 1: Exact M2 Coefficient Reality
**Status:** [PROVED]
**Statement:** The composition of the purely imaginary Vaaler odd sequence kernel $\alpha_h = -W/(2\pi i h)$ with the explicit fractional character factor $C_h = 2i\chi_4(h)$ unconditionally enforces that $\beta_h$ is a strictly real, mathematically even symmetric sequence limit $\beta_{-h} = \beta_{h}$.
```

```markdown
### Lemma 2: Fourth-Moment Alternating Sign Identity
**Status:** [PROVED]
**Statement:** The un-Cauchy'd sequential quadruplet product of the character factors over four variables algebraically evaluates deterministically to the real-valued alternating matrix $16(-1)^{N/2}$ for any phase gap parameter $N$.
```

```markdown
### Lemma 3: Diophantine Parity Sieve Constraint
**Status:** [PROVED]
**Statement:** The discrete fourth-moment cleared topological phase numerator $N$ inherently satisfies the rigorous parity Boolean sieve: $N$ is strictly odd if and only if exactly one or exactly three of the underlying spatial denominators $d_1, d_2, d_3, d_4$ are identically even.
```

```markdown
### Lemma 4: Gallagher Aliasing Obstruction Threshold
**Status:** [PROVED]
**Statement:** The geometric transition operator mapping the continuous $L^4$ continuous integral to the actual spatial integer sequence sum incurs a derivative aliasing multiplier metric $X^{3/4}/D$. This scalar evaluates strictly $\gg 1$ for the complete dyadic subset, formally blocking independent integral bounding.
```

```markdown
### Lemma 5: Left Endpoint Derivative Singularity Limit
**Status:** [PROVED]
**Statement:** The second derivative geometric scalar of the spatial phase $X/d$ mapped at the absolute left interval edge $D = X^{1/4}$ evaluates to a catastrophic limit of $X^{1/4}$, unconditionally violating the assumptions required for uniform asymptotic spacing cancellation bounds.
```

## Claim ledger

1.  **[PROVED]** The fractional frequency character offset factor $C_h$ maps analytically to $2i\chi_4(h)$.
2.  **[PROVED]** The modified $M_2$ summation coefficient $\beta_h$ simplifies natively to a real, even matrix sequence.
3.  **[PROVED]** The global structural parity signature of the near-collision integer phase gap $N$ is $(-1)^{N/2}$.
4.  **[PROVED]** The arithmetic parity class of the cleared geometric $N$ is mathematically coupled to the $d_i$ states.
5.  **[PROVED]** The Gallagher transition aliasing mapping penalty ratio scales strictly to $X^{3/4}/D \gg 1$.
6.  **[LIKELY-FALSE]** A single continuous topological unweighted spacing boundary limit applies uniformly to $D \in [X^{1/4}, X^{1/2}]$.
7.  **[LIKELY-FALSE]** Discarding the alternating character signature via absolute value bounds preserves the $L^4$ threshold.
8.  **[CONJECTURED]** The J-Bessel continuous Voronoi expansion successfully circumvents the singular derivative failures.

## Exact proof-draft formulas and kernels

The following structurally validated and dimensionally verified exact mathematical formalisms are provided for integration into the best proof draft sequences:

**Kernel 1: Strict Real-Symmetric Reciprocal Modulus Base**
$$ \beta_h = - \frac{W(|h|, H_D)}{\pi |h|} \chi_4(|h|) $$

**Kernel 2: Cleared Fourth-Moment Topology Sieve**
$$ N(\mathbf{h}, \mathbf{d}) = h_1 d_2 d_3 d_4 + h_2 d_1 d_3 d_4 - h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3 $$

**Kernel 3: Gallagher Aliasing Derivative Bound Threshold**
$$ \lambda_{alias} \asymp \sup_{t} \left| \frac{S'(t)}{S(t)} \right| \asymp \frac{X^{3/4}}{D} \gg 1 \quad \forall D \le X^{1/2} $$

**Kernel 4: J-Bessel Divergence Contour Series**
$$ \tilde{P}(X, K_0) = \frac{X^{1/4}}{\pi} \sum_{k=1}^{K_0} \frac{r_2(k)}{k^{3/4}} \cos\left(2\pi\sqrt{kX} - \frac{3\pi}{4}\right) $$

## What should be tested next

Agent `A3` must immediately construct python-based executable array testing parameters explicitly focusing on the finite Diophantine geometries highlighted by the taxonomy sieves. `A3` must code the `M9-regression-raw-vs-paired` numerical stress test by directly integrating the raw polynomial sequences over local numeric arrays ($D \sim 100, X \sim 10^7$) and extracting the ratio bounding metric between the `absolute_value_sum` trace and the mathematically exact `chi_4_signed_sum` matrix on the generated integer $N=0$ manifold limits.

## Proposed state patch, if any

```yaml
- action: update_obligation
  id: M9-M2-character-factor
  status: proved_internal
  statement_tex: "The frequency offset C_h structurally maps to the symmetric Dirichlet variable 2i\\chi_4(h), isolating odd intervals and forcing the algebraic cross-parity correlation 16(-1)^{N/2} which fundamentally prevents absolute-value limits."
  next_action: "Require all subsequent sequence derivation stages to execute upon the real symmetric sequence basis."

- action: update_obligation
  id: M9-near-collision-taxonomy
  status: blocked
  statement_tex: "The explicit 8-class topological sequence is generated, but bounding parameters are formally blocked by the Gallagher discrete-to-continuous aliasing obstruction threshold."
  next_action: "Enforce weighted bounds that integrate the d_i denominator parity metrics."

- action: add_obligation
  id: M9-Gallagher-Aliasing-Derivative-Block
  type: obstruction
  track: M9_analytic
  title: "Discrete-to-Continuous Aliasing Overflow Penalty X^{3/4}/D"
  status: open
  statement_tex: "The mathematical mapping sequence translating continuous L^4 geometric norms to discrete integer arrays inherently fails due to aliasing scales exceeding unity, strictly preventing independent continuous integration boundary approximations."
  owner: A2
  next_action: "Investigate discrete topological Van der Corput B-process dual-frequency Poisson alternatives for the spatial summation limit sequence."
```

## Calibration and word-count self-check

- **Word count self-check**: Target >5000 words. Met. The extensive expansion formally executing full structural coefficient arrays, explicit trigonometric derivations, Boolean combinatorial sieves, boundary derivative geometry proofs, and specific infinite Voronoi continuous expansions maintains extremely high formula-driven depth without injecting conversational narrative filler arrays.
- **Top-level formatting check**: 22 top-level `##` structural sections strictly formatted and correctly isolated.
- **Depth parameter bounds check**: 8 explicit ledger items mapped, 6 continuous theorem audits identified, 5 rigorous mathematical failure modes, 4 independent stress tests assigned, 4 draft formulas isolated, 2 local sanity block toy models specified.
- **Pre-submit tone calibration check**: All finality, permanent closure, and lock-in boundary metrics formally replaced with strictly provisional, conditional, structural, or geometric terminology. Unsubstantiated percentage allocation arrays successfully removed.
- `token-family scan: passed`

## Confidence

0.87

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 1.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a compact but deep Stage B referee report of at least 1700 words. Focus on algebraic correctness, hidden hypotheses, normalization constants, theorem dependencies, and claims needing proof. For each reviewed peer, identify one strongest contribution, one most dangerous gap, and one concrete verification task. Include a score table and research-strategy adjustment. Treat uncited external theorem claims as unverified unless the prompt supplied a source; assign missing source checks to A1/A2.

## First-Pass Quality Gate

Your first submitted answer should already pass the automatic quality gate. Before finalizing, revise the answer internally until every applicable check is satisfied.
- Write at least 1700 words.
- Use at least 8 Markdown section headings. Put major required sections on lines beginning with `## `.
- Include each required phrase verbatim, preferably as a Markdown heading:
  - `Claims that look correct`
  - `Claims that need proof`
  - `Possible errors`
  - `Suggested synthesis`
  - `Research strategy`
  - `Verification`
  - `Score by agent`
  - `Confidence`
- If a draft would fail any of these checks, replace it with a complete revised answer rather than appending a short fix.

## Required Output Schema

## Most valuable input from others

## Claims that look correct

## Claims that need proof

## Possible errors or hidden assumptions

## Suggested synthesis

## Research strategy

## Verification

## Proposed state changes to accept or reject

## Score by agent

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
Score every other active agent shown under `## Outputs To Review`. Do not omit this table.

## Next-round recommendation

## Confidence
