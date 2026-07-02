You are A3 Deepseek V4 Pro, acting as API-based proof auditor, algebra checker, and stress-test planner.

Review the other agents' Round 5 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Check algebraic reductions, Poisson/Bessel normalizations, hyperbola decompositions, endpoint conventions, Vaaler/Fejer residuals, Li-Yang/Bombieri-Iwaniec compatibility claims, Mellin-Perron alternatives, and claimed obstructions. Prefer precise parameter ranges and falsifiable lemmas over broad summaries. In reasoning, reserve about 20% of the answer for divergent alternatives or obstruction searches. In review, recommend research-strategy adjustments based on which claims survive verification. For computation-track obligations, do not substitute surrogate phases or random coefficient models as state evidence. Use the actual formulas, actual alpha_h/beta_h/C_h coefficients, and the physical bivariate phase e(hX/(4d)); if a toy surrogate is included, label it as toy evidence and do not use it for status changes. If no committed script, exact command, table, and report are produced, say the computation was not executed. If you cannot physically write files through the API, output an `## Artifact bundle` with repository-relative file paths, complete script contents, exact commands, expected table schemas, precision/log fields, and a short report template so the local orchestrator or Codex can materialize and run them. When a proof step is plausible but not certified, say exactly which formula, theorem hypothesis, citation, or numerical check would certify it.



## Active Agents For This Run

Only these agents are active in this run:

- `A1` (ChatGPT Extended Pro): broad strategist, literature scout, proof synthesizer, and default judge
- `A2` (Gemini Pro Deep Think): independent alternative strategist, obstruction finder, and referee-style reviewer
- `A3` (A3 Deepseek V4 Pro): API-based proof auditor, algebra checker, and stress-test planner
- `A4` (Claude Max Thinking): independent analytic proof-surgeon for narrow M9 sublemmas

Do not mention, score, or assign tasks to inactive agents. If older state text refers to inactive agents, treat it as historical context and reassign any still-useful mathematical check to one of the active agents.

## Protocol

# Multi-AI Mathematical Research Protocol

## Authoritative Mathematical State

The authoritative state is `state/proof_obligations.yml`.

A proof obligation is any theorem, lemma, reduction, external theorem, normalization convention, computation target, source audit, obstruction, or counterexample search whose status matters for the project. Round transcripts in `rounds/` are evidence and audit trail; they are not the state itself.

The compact reading packet in `manifests/reading_packet.md` is generated from the proof-obligation graph. Agents should normally read the packet and graph, not the full transcript history.

## Round Structure

Rounds use strict barrier synchronization:

- Stage B cannot begin until A1, A2, A3, and A4 have completed Stage A.
- Stage C cannot begin until A1, A2, A3, and A4 have completed Stage B.
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
### For A4
## Round Assessment
## Confidence
```

The `State Patch` block is the only mechanism for mutating `state/proof_obligations.yml`. Use JSON-compatible YAML so the local validator can parse it without optional dependencies. The `For A1`, `For A2`, `For A3`, and `For A4` blocks are also important: the orchestrator extracts them into `state/next_round_prompts.md` and injects the matching block into the next round's Stage A prompt.

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

For judge stages, include: selected route, useful fragments by source, rejected or risky ideas, exact gaps, new lemma statements, research-strategy adjustment, next-round tasks for A1/A2/A3/A4, and confidence.

## Proof-Obligation Workflow Contract

The authoritative mathematical state is `state/proof_obligations.yml`. Treat rounds as work on specific obligations, not as global project transcripts.

Rules:

- Focus on the round target obligations named in the reading packet or judge task.
- Do not promote an obligation unless you provide an exact statement, dependencies, evidence files, and remaining caveats.
- Computations may add diagnostic evidence or next actions, but may not prove theorem or lemma obligations.
- External theorem obligations require source cards before they can be used as proof dependencies.
- The final judge synthesis must include `## State Patch` using JSON-compatible YAML.

## Review-Stage Guardrail

This is Stage B cross review for Round 5.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a compact but deep Stage B referee report of at least 1700 words. Focus on algebraic correctness, hidden hypotheses, normalization constants, theorem dependencies, and claims needing proof. For each reviewed peer, identify one strongest contribution, one most dangerous gap, and one concrete verification task. Include a score table and research-strategy adjustment. Treat uncited external theorem claims as unverified unless the prompt supplied a source; assign missing source checks to A1/A2/A4.

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
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/obligation-main/round_004/responses/A1-004.md"
        ],
        "negative": [],
        "inconclusive": []
      },
      "owner": "A1",
      "next_action": "Promote only after the Vaaler source card is physically updated and validated; until then use H4-dependent lemmas as derived_under_assumptions.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
        "positive": [
          "rounds/obligation-main/round_004/responses/A1-004.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/obligation-main/round_003/responses/A1-003.md",
          "rounds/obligation-main/round_003/reviews/A3.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ]
      },
      "owner": "A1",
      "next_action": "Commit sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, Fejer normalization, residual constant, and floor-compatible endpoint convention.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
        "H4-source-audit",
        "R5-Full-reconciliation"
      ],
      "evidence": {
        "positive": [
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_003/human/00-strategy-evaluations-judge-merge.md",
          "rounds/obligation-main/round_003/human/strategy-revised4-audit.md"
        ]
      },
      "owner": "A1",
      "next_action": "Use the pointwise product-count proof conditional on H4; do not promote to proved_internal until H4/source-card validation is complete.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
        "M9-near-collision-taxonomy",
        "M9-M2-denominator-paired-weighted-bound",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ]
      },
      "owner": "A2",
      "next_action": "Do not promote from exact-resonance sublemmas. Supply pointwise control, near-collision estimates, and endpoint-uniformity before any status change.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/round_001/responses/A1_reasoning_1.md",
          "rounds/obligation-main/round_002/responses/A1-002.md"
        ],
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md"
        ],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A2-2.md",
          "rounds/round_001/responses/A3.md",
          "rounds/obligation-main/round_002/responses/A2-002.md",
          "rounds/obligation-main/round_002/responses/A3-002.md",
          "rounds/obligation-main/round_002/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use the exact beta_h algebra and the h-Cauchy sign-loss diagnostic to pursue the M2 fourth-moment route first; keep CRI and direct signed bilinear estimates as secondary diagnostics.",
      "last_updated_round": 2,
      "last_updated_at": "2026-06-26T03:16:11"
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
        "M9-near-collision-estimate",
        "M9-M2-N0-diagonal-core-bound",
        "M9-M2-denominator-paired-weighted-bound",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md"
        ],
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_002/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_003/human/stage-a-response-audit.md",
          "rounds/obligation-main/round_003/human/stage-b-review-audit.md"
        ],
        "inconclusive": [
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A2-2.md",
          "rounds/obligation-main/round_002/responses/A2-002.md",
          "rounds/obligation-main/round_003/responses/A2-003.md",
          "rounds/obligation-main/round_003/artifacts/m9_regression/report.md",
          "rounds/obligation-main/round_004/responses/A3-004.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ]
      },
      "owner": "A2",
      "next_action": "Preserve the unclassified exact N=0 class. Next prove or refute mixed/unclassified exact resonances and start denominator-paired near-collision with the normalized L-condition.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
        "inconclusive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ]
      },
      "owner": "A2",
      "next_action": "First attack the denominator-paired near-collision condition 0<|(h_1-h_2)b+(h_3-h_4)a|<<D^2/X, then decide whether absolute or signed estimates are viable.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
      "status": "diagnostic_only",
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
        "positive": [
          "rounds/obligation-main/round_003/artifacts/m9_regression/run.py",
          "rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv",
          "rounds/obligation-main/round_003/artifacts/m9_regression/precision.log",
          "rounds/obligation-main/round_003/artifacts/m9_regression/report.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/web-research-test/round_028/responses/A3-028.md",
          "rounds/round_001/responses/A3.md",
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/responses/A3-002.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_003/responses/A3-003.md",
          "rounds/obligation-main/round_003/human/stage-a-response-audit.md",
          "rounds/obligation-main/round_003/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_004/responses/A3-004.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ]
      },
      "owner": "A3",
      "next_action": "Rerun with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, real paired formula, complex-weight cosine formula, and explicit failure of Re B_h for complex weights. Produce executable artifacts.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
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
    },
    {
      "id": "M9-M2-beta-algebra",
      "type": "normalization",
      "track": "M9_analytic",
      "title": "Exact beta_h coefficient algebra for M2",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming the H4 Vaaler coefficient convention alpha_{h,H}=-Phi(|h|/(H+1))/(2 pi i h), the M2 coefficient beta_{h,H}=alpha_{h,H}(e(h/4)-e(3h/4)) equals -Phi(|h|/(H+1)) chi_4(|h|) 1_{2 not divides h}/(pi |h|). Hence beta_{h,H} is real and even.",
      "dependencies": [
        "H4"
      ],
      "implies": [
        "M9-M2-character-factor"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/round_001/responses/A1_reasoning_1.md",
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_003/responses/A1-003.md",
          "rounds/obligation-main/round_003/reviews/A2.md",
          "rounds/obligation-main/round_003/reviews/A3.md",
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A3.md",
          "rounds/obligation-main/round_001/judge/judge-001.md"
        ]
      },
      "owner": "A1",
      "next_action": "Insert beta_h algebra, raw two-sided formula, real-weight paired formula, and complex-weight cosine pairing into best_proof_draft.md after H4 source-card update.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
    },
    {
      "id": "M9-M2-h-cauchy-sign-loss",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "Weighted h-Cauchy loses the M2 frequency character sign",
      "status": "derived_under_assumptions",
      "statement_tex": "For S_2=sum_h alpha_h C_h B_h, the positive |alpha_h|-weighted h-Cauchy step replaces C_h by |C_h|^2=4 1_{2 not divides h}; therefore the chi_4(h) sign is lost and only odd-frequency support remains. This is a bounded-scope diagnostic for that Cauchy normalization.",
      "dependencies": [
        "M9-M2-beta-algebra"
      ],
      "implies": [
        "M9-M2-character-factor"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/round_001/responses/A1_reasoning_1.md",
          "rounds/round_001/reviews/A1_review_1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A3.md",
          "rounds/obligation-main/round_001/judge/judge-001.md"
        ]
      },
      "owner": "A1",
      "next_action": "Use this only as a diagnostic. A2 should test fourth moments, CRI, or direct signed bilinear estimates rather than treating this as a no-go theorem.",
      "last_updated_round": 1,
      "last_updated_at": "2026-06-26T01:40:44"
    },
    {
      "id": "M9-M2-fourth-moment-expansion",
      "type": "reduction",
      "track": "M9_analytic",
      "title": "Algebraic fourth-moment expansion for M2 with retained character product",
      "status": "derived_under_assumptions",
      "statement_tex": "For S_2(D;X)=sum_{1<=|h|<=H_D} beta_h sum_d w_D(d)e(hX/(4d)), the two-sided fourth moment has phase X/4*(h_1/d_1-h_2/d_2+h_3/d_3-h_4/d_4) and cleared resonance integer N=h_1 d_2 d_3 d_4-h_2 d_1 d_3 d_4+h_3 d_1 d_2 d_4-h_4 d_1 d_2 d_3. The coefficient product retains the fourfold h-character before absolute-value majorization.",
      "dependencies": [
        "M9-M2-beta-algebra"
      ],
      "implies": [
        "M9-near-collision-taxonomy"
      ],
      "blockers": [
        "M9-near-collision-estimate"
      ],
      "evidence": {
        "positive": [
          "rounds/round_001/responses/A1_reasoning_1.md",
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/responses/A1-002.md",
          "rounds/obligation-main/round_003/responses/A1-003.md",
          "rounds/obligation-main/round_003/reviews/A2.md",
          "rounds/obligation-main/round_003/reviews/A3.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/obligation-main/round_001/judge/judge-001.md",
          "rounds/obligation-main/round_002/responses/A2-002.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use the expansion only as algebraic infrastructure for exact N=0 and near-collision estimates; do not infer an analytic bound without weighted mass estimates.",
      "last_updated_round": 3,
      "last_updated_at": "2026-06-29T21:35:33"
    },
    {
      "id": "M9-M2-N0-diagonal-core-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Diagonal-core bound for exact M2 fourth-moment resonances",
      "status": "open",
      "statement_tex": "For the actual beta_h coefficients and bounded dyadic weights, the direct diagonal, pair-swapped, and sign-symmetric exact N=0 families in the M2 fourth moment have total weighted mass O_epsilon(D^2), hence O_epsilon(X) for D <= X^(1/2).",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion",
        "H4"
      ],
      "implies": [
        "M9-near-collision-taxonomy"
      ],
      "blockers": [
        "H4-source-audit",
        "M9-M2-denominator-paired-weighted-bound",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_002/responses/A2-002.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_002/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_002/judge/judge-002.md",
          "rounds/obligation-main/round_003/responses/A1-003.md",
          "rounds/obligation-main/round_003/responses/A2-003.md",
          "rounds/obligation-main/round_003/reviews/A1.md",
          "rounds/obligation-main/round_003/reviews/A3.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ]
      },
      "owner": "A2",
      "next_action": "Record paired-core families as treated under assumptions, but prove or refute mixed and unclassified exact N=0 mass before promoting this obligation.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
    },
    {
      "id": "R5-Full-reconciliation",
      "type": "infrastructure",
      "track": "proof_infrastructure",
      "title": "R5-Full product-count reconciliation audit",
      "status": "derived_under_assumptions",
      "statement_tex": "Reconcile the older H5r/DDP-trap analysis with the later R5-Full product-count proof. The accepted outcome must either write the Fejer residual product-count proof with all edge cases or give a validator-ready downgrade proposal.",
      "dependencies": [
        "R5-Full",
        "H4",
        "H4-source-audit"
      ],
      "implies": [
        "R5-Full",
        "Conditional-bridge"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ],
        "negative": [
          "rounds/obligation-main/round_004/responses/A2-004.md"
        ],
        "inconclusive": [
          "rounds/obligation-main/round_003/human/00-strategy-evaluations-judge-merge.md",
          "rounds/obligation-main/round_003/human/strategy-revised4-audit.md",
          "rounds/obligation-main/round_003/human/strategy-revised-judge-merge.md",
          "rounds/obligation-main/round_003/judge/judge-003.md",
          "rounds/obligation-main/round_004/reviews/A1.md"
        ]
      },
      "owner": "A1",
      "next_action": "Insert A1's positive Fejer product-count proof into best_proof_draft.md; reject the RMS/L2 argument as a pointwise proof; keep H4 dependency visible.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43",
      "reason_for_promotion": "Round 4 supplies a pointwise positive-Fejer product-count proof conditional on H4, with A1 as the main proof source and A4 confirming the norm and dependency."
    },
    {
      "id": "M9-M2-denominator-paired-weighted-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Weighted denominator-paired exact M2 resonance bound",
      "status": "derived_under_assumptions",
      "statement_tex": "For X^(1/4) <= D <= X^(1/2), H_D asymp D X^(-1/4), actual beta_h coefficients, and bounded dyadic weights, the exact N=0 subfamily d_1=d_2=a, d_3=d_4=b, equivalently (h_1-h_2)b+(h_3-h_4)a=0, has total absolute beta-weighted fourth-moment mass <<_epsilon X^(1+epsilon), preferably <<_epsilon D^2 X^epsilon if true.",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion",
        "H4"
      ],
      "implies": [
        "M9-M2-N0-diagonal-core-bound",
        "M9-near-collision-taxonomy"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_003/responses/A2-003.md",
          "rounds/obligation-main/round_003/reviews/A1.md",
          "rounds/obligation-main/round_003/reviews/A2.md",
          "rounds/obligation-main/round_003/reviews/A3.md",
          "rounds/obligation-main/round_003/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_003/judge/judge-003.md"
        ]
      },
      "owner": "A2",
      "next_action": "Treat denominator-paired exact resonance as settled under H4. Use it as a sublemma only; do not infer M9-M2 or full taxonomy.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43",
      "reason_for_promotion": "A1, A2, and A4 independently derive the denominator-paired exact-resonance bound under the H4 beta-coefficient magnitude hypothesis, and A1/A4 reviews agree it is state-promotable only under assumptions."
    },
    {
      "id": "M9-M2-direct-signed-bilinear-lemma",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Direct signed bilinear estimate for M2",
      "status": "proposed",
      "statement_tex": "A direct signed bilinear estimate for S_2(D;X)=sum_{1<=|h|<=H_D} beta_{h,H_D} sum_{d asymp D} w_D(d)e(hX/(4d)) giving S_2(D;X) <<_epsilon X^(1/4+epsilon) uniformly over X^(1/4)<=D<=X^(1/2), without erasing the chi_4 frequency sign by character-blind norms.",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-character-factor",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2"
      ],
      "blockers": [],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_003/responses/A1-003.md",
          "rounds/obligation-main/round_003/responses/A2-003.md",
          "rounds/obligation-main/round_003/reviews/A1.md",
          "rounds/obligation-main/round_003/reviews/A3.md",
          "rounds/obligation-main/round_003/judge/judge-003.md"
        ]
      },
      "owner": "A2",
      "next_action": "Rewrite as a precise theorem with coefficient class, dyadic ranges, exact bilinear or spacing norm, named external theorem if used, and a fast falsification test comparing signed and unsigned statistics.",
      "last_updated_round": 3,
      "last_updated_at": "2026-06-29T21:35:33"
    },
    {
      "id": "M9-M2-harmonic-convolution-LH",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Harmonic convolution bound for reciprocal beta weights",
      "status": "proved_internal",
      "statement_tex": "For H>=1 and integer q, L_H(q)=sum_{1<=|h|<=H, 1<=|h+q|<=H} 1/(|h||h+q|) satisfies L_H(0)<<1 and L_H(q)<<log(2H)/max(1,|q|).",
      "dependencies": [],
      "implies": [
        "M9-M2-denominator-paired-weighted-bound"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/judge/judge-004.md"
        ]
      },
      "owner": "A4",
      "next_action": "Reuse this lemma in paired exact-resonance and denominator-paired near-collision estimates.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
    },
    {
      "id": "M9-M2-paired-core-weighted-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Weighted paired-core exact M2 resonance bound",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming the H4 beta coefficient magnitude |beta_h|<<1_{1<=|h|<=H_D}/|h| and bounded dyadic weights, the pair-equality, denominator-paired, pair-swapped, and semi-diagonal exact N=0 paired families in the M2 fourth moment have total absolute beta-weighted mass <<_epsilon D^2 X^epsilon uniformly for X^(1/4)<=D<=X^(1/2). This does not cover mixed or unclassified exact resonances.",
      "dependencies": [
        "H4",
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion",
        "M9-M2-harmonic-convolution-LH",
        "M9-M2-denominator-paired-weighted-bound"
      ],
      "implies": [
        "M9-M2-N0-diagonal-core-bound",
        "M9-near-collision-taxonomy"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/judge/judge-004.md"
        ]
      },
      "owner": "A2",
      "next_action": "Write the pair-swapped and semi-diagonal proofs in proof-draft-ready form; keep mixed and unclassified exact N=0 classes open.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
    },
    {
      "id": "M9-M2-fourth-moment-average-to-pointwise",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "Average-to-pointwise upgrade for M2 fourth-moment estimates",
      "status": "open",
      "statement_tex": "Any fourth-moment or near-collision estimate for S_2(D;X) used to prove M9-M2 must yield the pointwise bound |S_2(D;X_0)|<<_epsilon X_0^(1/4+epsilon) for each active X_0, not only an average over an X-window. A candidate proof must control local fourth moments plus derivative or unsmoothing losses uniformly over X^(1/4)<=D<=X^(1/2).",
      "dependencies": [
        "M9-M2-fourth-moment-expansion",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2"
      ],
      "blockers": [],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_004/judge/judge-004.md"
        ]
      },
      "owner": "A4",
      "next_action": "Formulate an exact local-sup-from-average inequality for S_2(D;X), including derivative bounds, window length optimization, and endpoint D-uniformity.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
    },
    {
      "id": "M9-fourth-moment-enumeration",
      "type": "computation",
      "track": "computation",
      "title": "Exact and near-collision fourth-moment enumeration for M2",
      "status": "diagnostic_only",
      "statement_tex": "Executable diagnostics should enumerate exact N=0 and near-collision M2 fourth-moment tuples with actual beta_h weights, classified into pair-equality, denominator-paired, pair-swapped, semi-diagonal, mixed, and unclassified bins; output signed and absolute masses normalized by D^2 and X.",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion",
        "M9-regression-raw-vs-paired"
      ],
      "implies": [],
      "blockers": [],
      "accepted_evidence_level": "diagnostic_only",
      "required_output": [
        "script",
        "command",
        "table",
        "precision log",
        "report.md",
        "pass/fail assertions"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/responses/A3-004.md",
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_004/judge/judge-004.md"
        ]
      },
      "owner": "A3",
      "next_action": "Produce a runnable artifact bundle with exact integer arithmetic for N, true Phi coefficients after H4, signed-vs-unsigned comparisons, and unclassified exact N=0 growth tables.",
      "last_updated_round": 4,
      "last_updated_at": "2026-06-30T00:14:43"
    }
  ],
  "rejected_claims": [
    {
      "id": "A2-M9-M2-character-factor-proved-internal-claim",
      "reason": "A2's proposed promotion overstates the coefficient algebra and relies on the false or unproved cross-parity claim 16(-1)^{N/2}.",
      "last_updated_at": "2026-06-26T01:40:44",
      "last_updated_round": 1,
      "evidence": [
        "rounds/obligation-main/round_001/judge/judge-001.md"
      ]
    },
    {
      "id": "A2-M9-near-collision-taxonomy-blocked-claim",
      "reason": "The taxonomy is not complete, and the Gallagher aliasing obstruction is not proved.",
      "last_updated_at": "2026-06-26T01:40:44",
      "last_updated_round": 1,
      "evidence": [
        "rounds/obligation-main/round_001/judge/judge-001.md"
      ]
    },
    {
      "id": "A2-M9-Gallagher-Aliasing-Derivative-Block",
      "reason": "No precise Gallagher lemma, hypotheses, transition inequality, or counterexample construction is supplied.",
      "last_updated_at": "2026-06-26T01:40:44",
      "last_updated_round": 1,
      "evidence": [
        "rounds/obligation-main/round_001/judge/judge-001.md"
      ]
    },
    {
      "id": "A2-2-M9-Poisson-diagonal-capacity",
      "reason": "The Poisson diagonal-capacity computation is an exploratory transformed-model calculation and does not prove M9 or the actual reciprocal M2 estimate.",
      "last_updated_at": "2026-06-26T01:40:44",
      "last_updated_round": 1,
      "evidence": [
        "rounds/obligation-main/round_001/judge/judge-001.md"
      ]
    },
    {
      "id": "A3-M9-regression-diagnostic-only-promotion",
      "reason": "The response supplies a plan and surrogate-kernel script design, not committed executable files or actual M1/M2 raw-vs-paired output.",
      "last_updated_at": "2026-06-26T01:40:44",
      "last_updated_round": 1,
      "evidence": [
        "rounds/obligation-main/round_001/judge/judge-001.md"
      ]
    },
    {
      "id": "A3-M9-regression-script-duplicate",
      "reason": "The existing obligation M9-regression-raw-vs-paired already requires the script, command, table, precision log, and report.",
      "last_updated_at": "2026-06-26T01:40:44",
      "last_updated_round": 1,
      "evidence": [
        "rounds/obligation-main/round_001/judge/judge-001.md"
      ]
    },
    {
      "id": "A2-R2-near-collision-taxonomy-promotion",
      "reason": "Rejected because the proposed taxonomy contains an unclassified class, denominator-paired and semi-diagonal estimates are not proved, and near-collision bands are open.",
      "last_updated_at": "2026-06-26T03:16:11",
      "last_updated_round": 2,
      "evidence": [
        "rounds/obligation-main/round_002/judge/judge-002.md"
      ]
    },
    {
      "id": "A2-R2-denominator-paired-negligibility-proved",
      "reason": "Rejected because the claim is supported only by small numerical examples without a reproducible script or a divisor/gcd proof.",
      "last_updated_at": "2026-06-26T03:16:11",
      "last_updated_round": 2,
      "evidence": [
        "rounds/obligation-main/round_002/judge/judge-002.md"
      ]
    },
    {
      "id": "A2-R2-dual-length-explosion-route-closing",
      "reason": "Rejected as a route-closing theorem. The dual-length calculation is a diagnostic for one Poisson or continuous-relaxation path, not an obstruction to all fourth-moment, CRI, or signed bilinear methods.",
      "last_updated_at": "2026-06-26T03:16:11",
      "last_updated_round": 2,
      "evidence": [
        "rounds/obligation-main/round_002/judge/judge-002.md"
      ]
    },
    {
      "id": "A2-R2-diagonal-core-one-sixteenth-union-constant",
      "reason": "Rejected because A2's own calculation for three positive core families gives a factor 3/16 before overlap bookkeeping, not 1/16 for the whole union. The safe state-level claim is only O(D^2) <= O(X).",
      "last_updated_at": "2026-06-26T03:16:11",
      "last_updated_round": 2,
      "evidence": [
        "rounds/obligation-main/round_002/judge/judge-002.md"
      ]
    },
    {
      "id": "A3-R2-artifact-evidence-without-files",
      "reason": "Rejected because M9-regression-raw-vs-paired requires actual script, command, table, precision log, and report. A prose plan or unexecuted code is not positive evidence.",
      "last_updated_at": "2026-06-26T03:16:11",
      "last_updated_round": 2,
      "evidence": [
        "rounds/obligation-main/round_002/judge/judge-002.md"
      ]
    },
    {
      "id": "A3-R2-official-formula-normalization-unverified",
      "reason": "Rejected as state evidence until the computation uses the official raw M1/M2 formulas and the actual Vaaler coefficient Phi rather than provisional or normalized surrogate formulas.",
      "last_updated_at": "2026-06-26T03:16:11",
      "last_updated_round": 2,
      "evidence": [
        "rounds/obligation-main/round_002/judge/judge-002.md"
      ]
    },
    {
      "id": "A2-R3-total-exact-N0-OD2-proof-promotion",
      "reason": "Rejected because the asserted total additive-energy estimate for exact N=0 resonances is not proved and is challenged by the Stage B reviews.",
      "last_updated_at": "2026-06-29T21:35:33",
      "last_updated_round": 3,
      "evidence": [
        "rounds/obligation-main/round_003/judge/judge-003.md"
      ]
    },
    {
      "id": "A2-R3-near-collision-taxonomy-resolved",
      "reason": "Rejected because the exact N=0 taxonomy is not resolved and Round 3 diagnostics report nonzero unclassified exact N=0 mass.",
      "last_updated_at": "2026-06-29T21:35:33",
      "last_updated_round": 3,
      "evidence": [
        "rounds/obligation-main/round_003/judge/judge-003.md"
      ]
    },
    {
      "id": "A2-R3-denominator-paired-negligibility-proved",
      "reason": "Rejected because the claimed O(D log^4 X) denominator-paired estimate lacks a complete gcd-sum proof with actual beta_h weights and singular cases.",
      "last_updated_at": "2026-06-29T21:35:33",
      "last_updated_round": 3,
      "evidence": [
        "rounds/obligation-main/round_003/judge/judge-003.md"
      ]
    },
    {
      "id": "A2-R3-Gallagher-derivative-route-closing",
      "reason": "Rejected as a route-closing theorem. The derivative-loss calculation is a diagnostic for one continuous relaxation, not a proof that discrete fourth moments or signed bilinear methods fail.",
      "last_updated_at": "2026-06-29T21:35:33",
      "last_updated_round": 3,
      "evidence": [
        "rounds/obligation-main/round_003/judge/judge-003.md"
      ]
    },
    {
      "id": "A2-R3-direct-exponent-pair-M2-proof",
      "reason": "Rejected because the exponent-pair/Poisson sketch lacks exact theorem hypotheses, derivative scales, boundary terms, coefficient treatment, outer h-sum handling, and endpoint uniformity.",
      "last_updated_at": "2026-06-29T21:35:33",
      "last_updated_round": 3,
      "evidence": [
        "rounds/obligation-main/round_003/judge/judge-003.md"
      ]
    },
    {
      "id": "A2-R4-R5-L2-or-RMS-proves-pointwise-R5",
      "reason": "Rejected because R5-Full is a pointwise residual bound in X. An L2 or RMS residual estimate over X does not prove the pointwise product-count statement required by the conditional bridge.",
      "last_updated_at": "2026-06-30T00:14:43",
      "last_updated_round": 4,
      "evidence": [
        "rounds/obligation-main/round_004/judge/judge-004.md"
      ]
    },
    {
      "id": "A2-R4-full-exact-N0-taxonomy-proved",
      "reason": "Rejected because paired families do not exhaust exact N=0 resonances; mixed and unclassified classes remain open.",
      "last_updated_at": "2026-06-30T00:14:43",
      "last_updated_round": 4,
      "evidence": [
        "rounds/obligation-main/round_004/judge/judge-004.md"
      ]
    },
    {
      "id": "A2-R4-M9-M2-N0-diagonal-core-proved",
      "reason": "Rejected because the paired-core estimates are only subfamilies and the unclassified exact N=0 mass has not been bounded.",
      "last_updated_at": "2026-06-30T00:14:43",
      "last_updated_round": 4,
      "evidence": [
        "rounds/obligation-main/round_004/judge/judge-004.md"
      ]
    },
    {
      "id": "A3-R4-unexecuted-artifacts-as-positive-proof-evidence",
      "reason": "Rejected because diagnostic computations require materialized scripts, commands, tables, precision logs, reports, and pass/fail assertions; unexecuted or placeholder code is diagnostic planning only.",
      "last_updated_at": "2026-06-30T00:14:43",
      "last_updated_round": 4,
      "evidence": [
        "rounds/obligation-main/round_004/judge/judge-004.md"
      ]
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 4 in run `obligation-main`.

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
  Next action: Use the exact beta_h algebra and the h-Cauchy sign-loss diagnostic to pursue the M2 fourth-moment route first; keep CRI and direct signed bilinear estimates as secondary diagnostics.
- `M9-near-collision-taxonomy` (open, owner `A2`): M2 fourth-moment near-collision taxonomy
  Next action: Preserve the unclassified exact N=0 class. Next prove or refute mixed/unclassified exact resonances and start denominator-paired near-collision with the normalized L-condition.
- `M9-regression-raw-vs-paired` (diagnostic_only, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Rerun with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, real paired formula, complex-weight cosine formula, and explicit failure of Re B_h for complex weights. Produce executable artifacts.

## Do-Not-Claim Rules

- Do not claim `M9` or the final Gauss circle target.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use Li-Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Agent Assignments

Use `state/next_round_prompts.md` for any judge-assigned A1/A2/A3/A4 tasks.

Default target split:
- `A1`: synthesis, proof-draft maintenance, source-card discipline, and State Patch authoring.
- `A2`: conservative obstruction analysis for the selected M9 obligations.
- `A3`: executable diagnostics or source-card artifacts, not prose-only plans.
- `A4`: independent analytic proof-surgery for narrow sublemmas and route repair.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `sources/vaaler_1985.md`
- `sources/li_yang_2023.md`
- `manifests/reading_packet.md`

## Last State Patch

created: M9-M2-harmonic-convolution-LH, M9-M2-paired-core-weighted-bound, M9-M2-fourth-moment-average-to-pointwise, M9-fourth-moment-enumeration; updated: H4-source-audit, H4, R5-Full-reconciliation, R5-Full, M9-M2-beta-algebra, M9-M2-denominator-paired-weighted-bound, M9-M2-N0-diagonal-core-bound, M9-near-collision-taxonomy, M9-near-collision-estimate, M9-M2, M9-regression-raw-vs-paired; rejected: A2-R4-R5-L2-or-RMS-proves-pointwise-R5, A2-R4-full-exact-N0-taxonomy-proved, A2-R4-M9-M2-N0-diagonal-core-proved, A3-R4-unexecuted-artifacts-as-positive-proof-evidence; no_change: M9, M9-M1, M9-endpoint-uniformity, GC-target, Li-Yang-source-audit, Conditional-bridge; round score: 5; Round 4 proves a narrow but real H4-dependent denominator-paired exact-resonance bound, validates a reusable harmonic-convolution lemma, and largely reconciles R5-Full pointwise under H4. It does not prove M9, resolve unclassified exact N=0 mass, prove near-collision estimates, or bridge average fourth-moment control to pointwise M2.

## Active Obligation Briefs

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Use the exact beta_h algebra and the h-Cauchy sign-loss diagnostic to pursue the M2 fourth-moment route first; keep CRI and direct signed bilinear estimates as secondary diagnostics.

### M9-near-collision-taxonomy: M2 fourth-moment near-collision taxonomy

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`
- Next action: Preserve the unclassified exact N=0 class. Next prove or refute mixed/unclassified exact resonances and start denominator-paired near-collision with the normalized L-condition.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `diagnostic_only`
- Track: `computation`
- Owner: `A3`
- Next action: Rerun with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, real paired formula, complex-weight cosine formula, and explicit failure of Re B_h for complex weights. Produce executable artifacts.

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
- Next action: Promote only after the Vaaler source card is physically updated and validated; until then use H4-dependent lemmas as derived_under_assumptions.

### H4-source-audit: Rendered source audit for Vaaler 1985

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Commit sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, Fejer normalization, residual constant, and floor-compatible endpoint convention.

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
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`
- Next action: Do not promote from exact-resonance sublemmas. Supply pointwise control, near-collision estimates, and endpoint-uniformity before any status change.

### M9-M2-N0-diagonal-core-bound: Diagonal-core bound for exact M2 fourth-moment resonances

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`
- Next action: Record paired-core families as treated under assumptions, but prove or refute mixed and unclassified exact N=0 mass before promoting this obligation.

### M9-M2-direct-signed-bilinear-lemma: Direct signed bilinear estimate for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Rewrite as a precise theorem with coefficient class, dyadic ranges, exact bilinear or spacing norm, named external theorem if used, and a fast falsification test comparing signed and unsigned statistics.

### M9-M2-fourth-moment-average-to-pointwise: Average-to-pointwise upgrade for M2 fourth-moment estimates

- Status: `open`
- Track: `M9_analytic`
- Owner: `A4`
- Next action: Formulate an exact local-sup-from-average inequality for S_2(D;X), including derivative bounds, window length optimization, and endpoint D-uniformity.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Attach explicit D-range hypotheses to every proposed M1 or M2 estimate.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: First attack the denominator-paired near-collision condition 0<|(h_1-h_2)b+(h_3-h_4)a|<<D^2/X, then decide whether absolute or signed estimates are viable.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.

### M9-M2-beta-algebra: Exact beta_h coefficient algebra for M2

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Insert beta_h algebra, raw two-sided formula, real-weight paired formula, and complex-weight cosine pairing into best_proof_draft.md after H4 source-card update.

### M9-M2-denominator-paired-weighted-bound: Weighted denominator-paired exact M2 resonance bound

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`
- Next action: Treat denominator-paired exact resonance as settled under H4. Use it as a sublemma only; do not infer M9-M2 or full taxonomy.

### M9-M2-fourth-moment-expansion: Algebraic fourth-moment expansion for M2 with retained character product

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`
- Next action: Use the expansion only as algebraic infrastructure for exact N=0 and near-collision estimates; do not infer an analytic bound without weighted mass estimates.

### M9-M2-h-cauchy-sign-loss: Weighted h-Cauchy loses the M2 frequency character sign

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Next action: Use this only as a diagnostic. A2 should test fourth moments, CRI, or direct signed bilinear estimates rather than treating this as a no-go theorem.

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Generated after round 4 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_004/judge/judge-004.md`.

## For A1

Target obligations: `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, and proof-draft consolidation.

Objectives:

1. Commit or draft the exact Vaaler source card `sources/vaaler_1985.md`. Include:
   - bibliographic data for Vaaler 1985;
   - local PDF path;
   - Theorem 6, equation (2.28), for $\widehat J(t)$;
   - Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, equations (7.13)--(7.17), especially the residual inequality;
   - coefficient sign
$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h};
$$
   - Fejer normalization $K_H(0)=H+1$;
   - floor-compatible endpoint convention $\psi_F(n)=-1/2$.

2. Insert A1's R5 product-count proof into `best_proof_draft.md`. The proof must use the positive Fejer majorant before Fourier expansion and must prove pointwise bounds for:
$$
T_d=X/d,
\qquad
T_d=(X/d+\rho)/4,\quad \rho\in\{1,3\}.
$$

3. Insert official M9 definitions:
$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_d w_D(d)e(hX/(4d)).
$$

4. Insert raw two-sided, real-weight paired, and complex-weight cosine formulas for $\mathcal M_2$.

5. Formulate the new `M9-M2-fourth-moment-average-to-pointwise` obligation precisely. Include a candidate local inequality, derivative estimate for $S_2(D;X)$, window length variable, and expected loss.

6. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Exploratory allocation:

- Write a short comparison of three routes: absolute exact-resonance taxonomy, average-to-pointwise fourth moment, and direct signed bilinear estimate. State the proof obligation and falsification criterion for each.

## For A2

Target obligations: `M9-M2-paired-core-weighted-bound`, `M9-M2-N0-diagonal-core-bound`, and `M9-near-collision-taxonomy`.

Objectives:

1. Do not re-prove the denominator-paired subcase except as a cited sublemma.

2. Write proof-draft-ready proofs for the pair-swapped and semi-diagonal exact $N=0$ families.

## For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-fourth-moment-enumeration`, `M9-M2-fourth-moment-average-to-pointwise` diagnostics, and signed-vs-unsigned diagnostics.

Objectives:

1. Produce a complete executable artifact bundle. Include:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - precision log;
   - CSV table schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Fix formula and API issues before execution:
   - define $e(t)=\exp(2\pi i t)$ explicitly;
   - use the official M1 phase $e(hX/d)$;
   - use the official M2 phase $e(hX/(4d))$;
   - parse integer parameters exactly for fourth-moment numerator calculations;
   - use high precision near Fejer spikes.

3. Run raw-vs-paired checks:
   - raw two-sided M2;
   - real-weight paired formula;
   - complex-weight cosine formula;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

4. Run exact $N=0$ enumeration with true beta weights:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - semi-diagonal;
   - mixed;
   - unclassified.

Report absolute weighted mass and signed mass normalized by $D^2$ and $X$.

5. Run denominator-paired identity checks using:
$$
a=ga',
\qquad
b=gb',
\qquad
h_1-h_2=ta',
\qquad
h_3-h_4=-tb'.
$$

6. Run near-collision bins:
$$
0<|N|\le C_0D^4/X
$$

at $D=X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

7. Run signed-vs-unsigned tests:
   - true $\beta_h$;
   - unsigned $|\beta_h|$;
   - random signs;
   - adversarial signs.

8. Run average-to-pointwise diagnostics:
   - local sup of $|S_2(D;X)|$ over short $X$ windows;
   - local fourth-moment average;
   - numerical derivative bound;
   - ratio of local sup to average-based upper bound.

All outputs remain `diagnostic_only`.

## For A4

Target obligations: `M9-M2-fourth-moment-average-to-pointwise`, `M9-near-collision-estimate`, and unclassified exact $N=0$ obstruction search.

Objectives:

1. Treat the harmonic-convolution lemma and denominator-paired bound as settled. Do not spend the round re-proving them.

2. Formulate a proof-level average-to-pointwise lemma for $S_2(D;X)$. Start from

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Derive a rigorous candidate inequality relating $|S_2(D;X_0)|^4$ to an average over $X\in I$ plus derivative loss. Track:
   - $|I|$;
   - $\sup_I |S_2|$;
   - $\sup_I |S_2'|$;
   - active range $X^{1/4}\le D\le X^{1/2}$;
   - $H_D\asymp DX^{-1/4}$;
   - whether the resulting bound can reach $X^{1+\epsilon}$ at fourth-moment scale.

3. Attack denominator-paired near-collisions. Use

$$
N=abL,
\qquad
L=(h_1-h_2)b+(h_3-h_4)a,
$$

so

$$
0<|N|\le C_0D^4/X
$$

implies

$$
0<|L|\ll C_0D^2/X.
$$

Since $D^2/X\le1$, determine whether this is just finitely many shifted exact linear equations and prove the corresponding weighted bound if possible.

4. If time remains, begin a structural obstruction search for mixed/unclassified exact $N=0$ solutions. State one exact parameterization attempt or one lower-bound construction.

5. Keep all claims calibrated. Do not claim `M9-M2`, `M9`, or `GC-target`.

Exploratory allocation:

- Propose one sign-preserving spacing or large-sieve theorem that would imply the direct signed bilinear estimate. State its exact variables and falsification test.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 8.0 | 8.5 | Strong H4 formula audit, correct R5 pointwise product-count proof, useful M2 algebra, and good route framing. Slight overpromotion risk if H4/source-card completion is treated as already committed. |
| A2 | 7.5 | 6.5 | 5.5 | Correct denominator-paired proof core and useful paired-family extensions. Calibration is weaker because several `[PROVED]` labels overreach, and the R5 RMS discussion uses the wrong norm for pointwise R5. |
| A3 | 7.0 | 3.0 | 8.0 | Diagnostic design is well targeted and appropriately labeled `diagnostic_only`, but the artifact bundle is not yet executable state-positive evidence. |
| A4 | 8.5 | 8.0 | 9.0 | Best narrow analytic contribution: clean harmonic-convolution proof, correct H4 dependency, sharp scale $T\asymp D^2$, and important identification of the average-to-pointwise gap. |

Overall progress is moderate but real. The proof graph gains one reusable internal lemma and one H4-dependent exact-resonance sublemma. It does not gain an endpoint M2 estimate.

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

For web-agent tests and formal rounds, use the four-agent Gauss workflow:

- A1 = ChatGPT Extended Pro through the web UI.
- A2 = Gemini Pro Deep Think through the web UI.
- A3 = Deepseek V4 Pro through the API.
- A4 = Claude Max Thinking through the web UI.

# Research-mode quality target

Kind: constraint
Timestamp: 2026-05-31T21:35:00

This is no longer a smoke test. Use research mode for the four-agent A1/A2/A3/A4 Gauss run. Take substantially more time to reason before answering. Prefer correctness, explicit hypotheses, gap detection, literature-status caution, and precise lemma formulation over speed or brevity. Do not optimize for short answers.

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

# Round 2 Route-Proposal Strengthening

Kind: workflow directive
Timestamp: 2026-06-26T01:50:00

For the next round and future M9 rounds, strengthen mathematical reasoning and route proposal. The agents should not only audit formulas; they must also propose viable proof routes.

A1 must include a dedicated `## Route proposals` section with at least two serious routes for the active M9 obligation. For each route, A1 must state:

- the exact lemma that would advance the proof graph;
- why the route might plausibly work;
- which existing obstruction it attacks;
- dependencies and theorem hypotheses;
- the first proof step to attempt;
- what would falsify the route quickly.

A2 must still be a conservative referee, but it must not only reject. It must include a `## Repair or alternative route` section. For the best route it criticizes, A2 should either repair it into a narrower lemma or propose one alternative route with exact hypotheses and a falsification test.

A3 should translate the leading route proposals into executable checks where possible, especially formula regression, finite counterexample search, and small exact enumeration. Computation remains diagnostic only.

The judge must compare route proposals explicitly. The judge should select one primary route and one backup route for the next round, and should not reward long critique unless it improves route selection or produces a precise proof obligation.

# Round 2 Score Calibration and Narrow-Evidence Standard

Kind: workflow directive
Timestamp: 2026-06-26T03:05:00

For the current judge synthesis and future M9 rounds, separate idea quality from proof-graph evidence.

The judge and reviewers should not use one vague score to mix creativity, plausible routes, calibration, and state-promotable proof evidence. Keep the existing required `mathematical_progress_score`, but also report:

- `idea_quality_score`: value of proposed routes, formulas, and diagnostics;
- `state_evidence_score`: how much can safely mutate `state/proof_obligations.yml`;
- `calibration_score`: whether the agent used correct statuses, avoided overclaiming, and supplied exact hypotheses.

A2 should improve by proving one narrow lemma per round instead of writing a broad taxonomy essay. If A2 discusses a taxonomy, it must choose one priority subcase, give an exact statement, state dependencies, and mark all other families as open. A2 must label every central claim as exactly one of `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`. `[PROVED]` requires a complete proof with exact hypotheses; numerical examples are never proof.

A3 should improve by producing execution-ready evidence. If the API agent cannot physically write repo files, it must output a concrete artifact bundle: file paths, script contents, exact command lines, expected table schema, precision/log fields, and a short report. The local workflow or Codex can then materialize and run those artifacts. Prose descriptions of tests do not count as evidence.

For Round 2 judging specifically:

- A2 official response has useful route ideas, but its low score is from overpromotion and incomplete proof evidence.
- A3 has useful diagnostic design, but its low score is from missing committed executable artifacts.
- The judge should score A2 and A3 higher on `idea_quality_score` than on `state_evidence_score` if warranted, while keeping mathematical state mutation conservative.

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

No new Gauss circle exponent is proved in this Stage A packet. The conservative route remains

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
\qquad
P(X)=N(\sqrt X)-\pi X,
$$

with `M9` still open. The useful output of this A1 round is proof-draft consolidation, not theorem promotion:

1. a source-card-ready statement of Vaaler's finite periodic sawtooth approximation with the correct coefficient sign, Fejer normalization, and floor-compatible endpoint conversion;
2. a proof-draft-ready R5 product-count proof for the first and shifted Fejer residual legs;
3. frozen official definitions for $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$;
4. raw two-sided, real-paired, and complex-weight cosine formulas for $\mathcal M_2$;
5. a precise `M9-M2-fourth-moment-average-to-pointwise` formulation, including a derivative-loss obstruction showing that the naive local-average route is too weak unless new input is supplied;
6. route proposals ranking the proof-draft/infrastructure route, exact-resonance taxonomy route, average-to-pointwise route, and direct signed bilinear route.

Source anchors: Vaaler's paper is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12(2), 183--216, 1985, with DOI `10.1090/S0273-0979-1985-15349-2`; AMS and Project Euclid metadata agree on the bibliographic data. Li--Yang's comparison paper is Xiaochun Li and Xuerui Yang, "An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem," arXiv:2308.14859v2; its abstract states the Bombieri--Iwaniec/first-spacing/Huxley-second-spacing mechanism, and the paper states $\theta^*=0.314483\ldots$, not the conjectural $\theta=1/4$. The active project state also records that Round 4 did not prove `M9`, `M9-M2`, or `GC-target`, and that the average-to-pointwise gap is now an explicit blocker.

## Target proof obligation

Primary target obligations for this A1 reasoning stage:

- `H4-source-audit`
- `H4`
- `R5-Full-reconciliation`
- `M9-M2-beta-algebra`
- `M9-M2-fourth-moment-average-to-pointwise`
- proof-draft consolidation for `state/best_proof_draft.md`

Secondary analytic context:

- `M9-M2-character-factor`
- `M9-near-collision-taxonomy`
- `M9-near-collision-estimate`
- `M9-endpoint-uniformity`

Do-not-promote list for this response:

- `M9`
- `M9-M1`
- `M9-M2`
- `M9-near-collision-taxonomy`
- `M9-near-collision-estimate`
- `GC-target`

The intended status output is therefore conservative: source-card and proof-draft material can be drafted; H4-dependent lemmas remain `derived_under_assumptions` until the source card is physically committed and validated.

## Main claim or direction

The selected route remains the balanced arithmetic hyperbola/Vaaler framework:

$$
P(X)
=
N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola}
\longrightarrow
\text{floor-compatible sawtooth}
\longrightarrow
\text{finite Vaaler}
\longrightarrow
\text{fixed-coefficient reciprocal main sums}.
$$

The accepted arithmetic identity has the form

$$
P(X)
=
-4\sum_{d\le y}\chi_4(d)\psi_F(X/d)
+
4\sum_{d\le y}
\left[
\psi_F\left(\frac{X/d+1}{4}\right)
-
\psi_F\left(\frac{X/d+3}{4}\right)
\right]
+
O(1),
$$

where

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12.
$$

For active dyadic denominator blocks,

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be removed before Vaaler expansion and bounded directly by $|\psi_F|\le 1/2$, giving an acceptable $O(X^{1/4}\log X)$ contribution.

The frozen main-term target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for all active dyadic $D$. This is exactly `M9`, and it is open.

## Detailed reasoning

### 1. Draft Vaaler source card for `sources/vaaler_1985.md`

Bibliographic data:

- Author: Jeffrey D. Vaaler.
- Title: "Some extremal functions in Fourier analysis."
- Journal: *Bulletin of the American Mathematical Society (New Series)*.
- Volume/issue/pages/year: 12(2), 183--216, 1985.
- DOI: `10.1090/S0273-0979-1985-15349-2`.
- AMS metadata page: `https://www.ams.org/bull/1985-12-02/S0273-0979-1985-15349-2/`.
- Project Euclid page: `https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-12/issue-2/Some-extremal-functions-in-Fourier-analysis/bams/1183552525.full`.
- Local PDF path: `/mnt/data/[Vaaler] Some extremal functions in Fourier analysis_Bull. Amer. Math. Soc..pdf`.

Relevant original source anchors:

- Theorem 6, equation (2.28), printed page 192: Fourier transform of $J$.
- Section 7, equations (7.1)--(7.3), printed page 207: definitions of $i_N,j_N,k_N$.
- Theorem 18, equations (7.13)--(7.17), printed pages 210--211: periodic sawtooth approximation and Fejer residual majorant.
- Vaaler's periodic sawtooth convention is centered at discontinuities:
$$
\psi_C(x)=
\begin{cases}
x-\lfloor x\rfloor-\frac12,&x\notin\mathbb Z,\\
0,&x\in\mathbb Z.
\end{cases}
$$

Theorem 6 gives

$$
\widehat J(t)
=
\begin{cases}
1,&t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|,&0<|t|<1,\\
0,&1\le |t|.
\end{cases}
$$

Define, for $0<u<1$,

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

Then

$$
\Phi(1-u)=1-\Phi(u),
$$

so $\Phi$ is not symmetric around $1/2$ except at $u=1/2$. This asymmetry is harmless for H4 because the coefficient uses $\widehat J(h/(H+1))$, and $\widehat J$ is even as a function of its full Fourier variable.

Section 7 defines the periodic polynomials

$$
i_N(x)=\sum_{m\in\mathbb Z}I_{2N+2}(x+m),
$$

$$
j_N(x)=\sum_{m\in\mathbb Z}J_{N+1}(x+m),
$$

$$
k_N(x)=\sum_{m\in\mathbb Z}K_{N+1}(x+m).
$$

In project notation, set $H=N$ and

$$
K_H(t)=k_N(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2,
$$

where $e(t)=e^{2\pi i t}$. Hence

$$
K_H(0)=H+1.
$$

Theorem 18 gives

$$
\psi_C*j_N(x)
=
\sum_{\substack{1\le |h|\le H}}
-\frac{\widehat J(h/(H+1))}{2\pi i h}e(hx),
$$

and the residual inequality

$$
|\psi_C*j_N(x)-\psi_C(x)|
\le
\frac{1}{2H+2}K_H(x).
$$

Translating to the repository's coefficient convention gives

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
1\le |h|\le H.
$$

For $h>0$,

$$
\alpha_{h,H}
=
\frac{i}{2\pi h}\Phi\left(\frac{h}{H+1}\right),
$$

and therefore

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

This conjugacy relation is important for raw-vs-paired formula checks.

### 2. H4 proof-draft statement with floor-compatible endpoint

Define

$$
V_H(t)=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht).
$$

Vaaler's theorem gives

$$
|\psi_C(t)-V_H(t)|
\le
\frac1{2H+2}K_H(t)
$$

for all real $t$.

The repository uses

$$
\psi_F(t)=t-\lfloor t\rfloor-\frac12
$$

for all real $t$, so

$$
\psi_F(n)=-\frac12
\qquad(n\in\mathbb Z).
$$

At nonintegers, $\psi_F=\psi_C$. At integers, $V_H(n)=0$ because the positive and negative Fourier modes cancel, while

$$
\frac1{2H+2}K_H(n)
=
\frac{H+1}{2H+2}
=
\frac12
=
|\psi_F(n)-V_H(n)|.
$$

Thus the floor-compatible H4 statement is:

**H4-R5A.** For every integer $H\ge1$ and every real $t$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H^F(t)|
\le
\frac1{2H+2}K_H(t).
$$

Status: `source_audit_required` until the source card is physically updated and validated. Mathematically, this is the correct theorem dependency under the rendered source audit.

### 3. R5-Full proof draft: positive Fejer product-count bound

The residual proof must use the positive Fejer majorant before any Fourier expansion. This avoids the older arbitrary-coefficient trap: the residual is controlled by a nonnegative kernel, not by arbitrary complex Fejer coefficients.

Let $D$ be active:

$$
X^{1/4}\le D\le X^{1/2},
$$

and choose

$$
H=H_D\asymp D X^{-1/4}.
$$

Set

$$
\Delta=\frac{D}{H}\asymp X^{1/4}.
$$

The standard Fejer bound is

$$
K_H(t)
\ll
\min\left(H,\frac1{H\|t\|^2}\right),
$$

hence

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

Since the H4 residual has an additional constant comparable to $1/H$, it is enough to prove blockwise estimates of the form

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(T_d)
\ll_\epsilon X^{1/4+\epsilon},
$$

where

$$
T_d=X/d
$$

or

$$
T_d=\frac{X/d+\rho}{4},
\qquad
\rho\in\{1,3\}.
$$

Assume $|w_D(d)|\ll1$ and bounded dyadic overlap.

#### First residual leg

For each $d\asymp D$, choose $m=m(d)$ nearest to $X/d$. Then

$$
\left\|\frac Xd\right\|
\asymp
\frac{|X-md|}{D}
$$

unless the distance is exactly zero, in which case the same majorant below is interpreted by $W_\Delta(0)=1$.

Define

$$
W_\Delta(u)=
\min\left(1,\frac{\Delta^2}{u^2}\right),
\qquad
W_\Delta(0)=1.
$$

Then

$$
\frac1H K_H(X/d)
\ll
W_\Delta(X-md).
$$

Grouping by the integer product

$$
n=md
$$

gives multiplicity at most $\tau(n)$, since each representation $n=md$ determines a divisor $d$. Therefore

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n).
$$

Using the divisor bound

$$
\tau(n)\ll_\epsilon n^\epsilon,
$$

and summing the kernel in unit intervals around the real point $X$,

$$
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)
\ll_\epsilon
X^\epsilon
\left(1+\sum_{1\le |k|\ll X}\min\left(1,\frac{\Delta^2}{k^2}\right)\right)
\ll_\epsilon
X^\epsilon(1+\Delta).
$$

Since $\Delta\asymp X^{1/4}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}.
$$

This is pointwise in $X$.

#### Shifted residual legs

Now take

$$
T_d=\frac{X/d+\rho}{4},
\qquad
\rho\in\{1,3\}.
$$

Near-integrality of $T_d$ is equivalent to

$$
\frac{X/d+\rho}{4}\approx m,
$$

or

$$
X\approx d(4m-\rho).
$$

Let

$$
\ell=4m-\rho.
$$

In the active large-$X$ range, $\ell>0$ except for finitely many small cases absorbed into the implicit constant. The congruence

$$
\ell\equiv-\rho\pmod4
$$

only reduces multiplicity.

As before,

$$
\left\|
\frac{X/d+\rho}{4}
\right\|
\asymp
\frac{|X-d\ell|}{D},
$$

up to harmless constants. Therefore

$$
\frac1H
K_H\left(\frac{X/d+\rho}{4}\right)
\ll
W_\Delta(X-d\ell).
$$

Grouping by

$$
n=d\ell
$$

again gives multiplicity at most $\tau(n)$, with a congruence restriction on $\ell$. Thus

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

This proves both shifted residual legs pointwise.

#### Short blocks and dyadic summation

If $D<X^{1/4}$, no Vaaler expansion is needed. Since

$$
|\psi_F(t)|\le\frac12
$$

for all real $t$ under the floor-compatible convention, a dyadic block contributes $O(D)$, and summing over $D<X^{1/4}$ gives $O(X^{1/4}\log X)$.

For active blocks, the number of dyadic blocks is $O(\log X)$, absorbed into $X^\epsilon$. Therefore R5-Full is proof-draft-ready conditional on H4:

$$
\text{all Fejer residual blocks}
\ll_\epsilon X^{1/4+\epsilon}.
$$

Status: `derived_under_assumptions`, not `proved_internal`, until H4 source-card validation is complete.

### 4. Official M9 definitions

Let $w_D$ be a dyadic weight supported on $d\asymp D$, with bounded overlap across $D$. Use the actual Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

The first fixed-coefficient main sum is

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d\chi_4(d)w_D(d)e(hX/d).
$$

The second fixed-coefficient main sum is

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_d w_D(d)e(hX/(4d)),
$$

where

$$
\beta_{h,H}
=
\alpha_{h,H}C_h,
$$

and

$$
C_h=e(h/4)-e(3h/4).
$$

For odd $h$,

$$
C_h=2i\chi_4(h),
$$

and for even $h$,

$$
C_h=0.
$$

With the H4 coefficient convention,

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Thus $\beta_{h,H}$ is real and even:

$$
\beta_{-h,H}=\beta_{h,H}.
$$

This is the algebraic source of the usable one-sided implementation formulas, but the raw two-sided formula remains canonical.

### 5. Raw two-sided, real-paired, and complex-weight cosine formulas for $\mathcal M_2$

Define

$$
B_h(D;X)=
\sum_d w_D(d)e(hX/(4d)).
$$

The raw two-sided formula is

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}\beta_{h,H_D}B_h(D;X).
$$

Because $\beta_{-h,H_D}=\beta_{h,H_D}$,

$$
\sum_{1\le |h|\le H_D}\beta_hB_h
=
\sum_{1\le h\le H_D}\beta_h
\sum_d w_D(d)
\left(
e(hX/(4d))+e(-hX/(4d))
\right).
$$

Therefore the complex-weight cosine formula is

$$
\mathcal M_2(D;X)
=
8\sum_{1\le h\le H_D}
\beta_{h,H_D}
\sum_d
w_D(d)
\cos\left(\frac{2\pi hX}{4d}\right).
$$

Substituting the explicit $\beta_h$ gives

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\sum_d
w_D(d)
\cos\left(\frac{2\pi hX}{4d}\right).
$$

This identity is valid for complex $w_D$ as an algebraic pairing of the $h$ and $-h$ raw terms. It does not equal a real-part formula when $w_D$ is complex.

If $w_D$ is real-valued, then

$$
\sum_d w_D(d)\cos\left(\frac{2\pi hX}{4d}\right)
=
\operatorname{Re}B_h(D;X),
$$

and the real-weight paired formula becomes

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}B_h(D;X).
$$

Regression warning: for complex weights, replacing the cosine sum by $\operatorname{Re}B_h$ is false in general, because $\operatorname{Re}$ conjugates the coefficient values while the raw $h,-h$ pairing does not.

### 6. Fourth-moment object and the average-to-pointwise obstruction

Use the two-sided normalized object

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Then

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

A sufficient pointwise fourth-moment target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

uniformly for active $D$.

Expanding gives phase

$$
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right),
$$

with cleared numerator

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

Exact resonance is $N=0$. Averaging over an $X$-interval of length $L$ creates a kernel that is large when

$$
\left|
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right|
\lesssim \frac1L,
$$

equivalently

$$
|N|\lesssim \frac{D^4}{L}.
$$

The current proof graph's near-collision threshold

$$
|N|\lesssim D^4/X
$$

corresponds to averaging over an interval of length comparable to $X$. That is not automatically useful for a pointwise value at $X_0$.

The elementary local inequality is as follows.

**Local Lipschitz fourth-moment inequality.** Let $I$ be an interval containing $X_0$, and let

$$
B_I=\sup_{X\in I}|S_2'(D;X)|.
$$

Then

$$
|S_2(D;X_0)|^4
\le
8\frac1{|I|}\int_I |S_2(D;X)|^4\,dX
+
8|I|^4B_I^4.
$$

Proof: for any $X\in I$,

$$
|S_2(D;X_0)|
\le
|S_2(D;X)|+|I|B_I.
$$

Raise to the fourth power and average over $I$.

The derivative is

$$
S_2'(D;X)
=
\frac{2\pi i}{4}
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}
w_D(d)\frac{h}{d}e(hX/(4d)).
$$

Using

$$
|\beta_{h,H_D}|\ll \frac1{|h|},
$$

and $d\asymp D$, the trivial derivative bound is

$$
B_I\ll
\sum_{1\le |h|\le H_D}
\sum_{d\asymp D}
\frac1{|h|}\frac{|h|}{D}
\ll H_D
\asymp D X^{-1/4}.
$$

To make the derivative error satisfy

$$
|I|^4B_I^4\ll X^{1+\epsilon},
$$

one needs

$$
|I|
\ll_\epsilon
\frac{X^{1/4}}{H_D}
\asymp
\frac{X^{1/2}}{D}.
$$

Thus the allowed interval length under the trivial derivative bound is only

$$
|I|\lesssim
\begin{cases}
X^{1/4},&D=X^{1/4},\\
X^{1/8},&D=X^{3/8},\\
1,&D=X^{1/2}.
\end{cases}
$$

But averaging over such a short interval only separates frequencies at the threshold

$$
|N|\lesssim \frac{D^4}{|I|}
\gtrsim
\frac{D^5}{X^{1/2}}.
$$

At the endpoint $D=X^{1/2}$, this is

$$
|N|\lesssim X^2,
$$

which is larger than or comparable to the full natural size of the cleared numerator in the fourth-moment expansion. Therefore the naive derivative-based average-to-pointwise upgrade destroys the global near-collision gain.

This is the main new A1 obstruction for the average route:

- A global $X$-average with threshold $D^4/X$ is too long to unsmooth pointwise by trivial derivative control.
- A short local average compatible with the derivative error has a near-collision band too wide to improve over pointwise expansion.
- Therefore `M9-M2-fourth-moment-average-to-pointwise` cannot be discharged by the elementary Lipschitz inequality plus a global fourth-moment estimate. It needs either a genuinely pointwise fourth-moment method, a much stronger derivative estimate exploiting cancellation, or a smoothing/unsmoothing mechanism tailored to the lattice-counting problem rather than to $S_2$ alone.

### 7. Draft statement for `M9-M2-fourth-moment-average-to-pointwise`

A precise proof obligation should read:

**M9-M2-fourth-moment-average-to-pointwise.** Let

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
H_D\asymp D X^{-1/4}.
$$

For every $X_0$ and every active $D$ with

$$
X_0^{1/4}\le D\le X_0^{1/2},
$$

prove a pointwise implication of the form

$$
|S_2(D;X_0)|^4\ll_\epsilon X_0^{1+\epsilon}
$$

from a local or global fourth-moment estimate, with all losses from localization, differentiation, smoothing, unsmoothing, and endpoint variation controlled uniformly in $D$.

A candidate sufficient inequality is

$$
|S_2(D;X_0)|^4
\le
C\frac1L\int_{X_0-L/2}^{X_0+L/2}|S_2(D;X)|^4\,dX
+
C L^4
\sup_{|X-X_0|\le L/2}|S_2'(D;X)|^4,
$$

but this candidate is not by itself sufficient unless either

$$
\sup_I |S_2'(D;X)|
\ll_\epsilon \frac{X_0^{1/4+\epsilon}}{L}
$$

for a useful long interval $L$, or the local fourth moment can be bounded at the very short lengths

$$
L\lesssim X_0^{1/2}/D.
$$

The current state should treat the above as an open obstruction, not as a solved lemma.

## Theorem-dependency audit

### H1--H3

Status: `proved_internal` in the current state.

Role: supplies the balanced hyperbola and floor-compatible sawtooth reduction.

Risk: low, provided endpoint conventions remain visible whenever H4 is applied.

### H4 / Vaaler finite approximation

Status: `source_audit_required`.

Dependencies:

- Vaaler Theorem 6, equation (2.28), for $\widehat J$.
- Vaaler Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$.
- Vaaler Theorem 18, especially equation (7.14), for the residual inequality.
- Notation conversion from $\psi_C(n)=0$ to $\psi_F(n)=-1/2$.
- Fejer normalization $K_H(0)=H+1$.
- Coefficient sign under $e(t)=e^{2\pi it}$.

Risk: moderate only at source-card transcription level. The formula-level translation is stable.

### R5-Full

Status: `derived_under_assumptions`.

Dependencies:

- H4 residual majorant.
- Positive Fejer kernel bound.
- Divisor bound $\tau(n)\ll_\epsilon n^\epsilon$.
- Bounded-overlap dyadic partition.
- Active height $H_D\asymp D X^{-1/4}$.

Risk: low conditional on H4. The proof uses positivity and divisor counting, not cancellation.

### M9-M2-beta-algebra

Status: `derived_under_assumptions`.

Dependencies:

- H4 coefficient sign and conjugacy.
- Exact factor
$$
C_h=e(h/4)-e(3h/4).
$$

Output:

$$
C_h=2i\chi_4(h)1_{2\nmid h},
$$

and

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Risk: low after H4 is fixed.

### M9-M2-fourth-moment-expansion

Status: `derived_under_assumptions` as algebraic infrastructure.

Dependencies:

- M9-M2-beta-algebra.
- Two-sided $h$ convention.

Risk: low algebraically. It does not prove an analytic bound.

### M9-M2-fourth-moment-average-to-pointwise

Status: `open`.

Dependencies:

- A fourth-moment estimate, exact or local.
- Derivative or unsmoothing control.
- Endpoint uniformity over $D$.

Risk: high. The trivial derivative inequality forces local intervals too short to exploit the global near-collision threshold.

### Li--Yang source audit

Status: `source_audit_required`, comparison only.

Li--Yang's theorem is not imported as an endpoint theorem. Their paper proves a record exponent $\theta^*=0.314483\ldots$, while this project's target in $X$-notation is $\theta=1/4$. At the endpoint $D=X^{1/2}$, the project's Vaaler height is

$$
H_D=X^{1/4},
$$

whereas the Li--Yang final exponent regime corresponds to a smaller height of order

$$
D X^{-\theta^*}=X^{1/2-\theta^*}=X^{0.185516\ldots}.
$$

Therefore black-box Li--Yang technology does not cover endpoint `M9`.

## Hidden assumptions and potential gaps

1. **H4 physical source card is still pending.** The formulas are stable, but the repository should not mark H4 as `proved_external_dependency` until `sources/vaaler_1985.md` is actually populated and validated.

2. **Integer choice of $H_D$.** Near $D=X^{1/4}$, one has $D X^{-1/4}\asymp1$. The proof draft should define
$$
H_D=\max(1,\lfloor cD X^{-1/4}\rfloor)
$$
or use an equivalent integer convention. Any choice must preserve $H_D\asymp D X^{-1/4}$.

3. **Small $X$ and shifted-leg positivity.** In shifted residual legs, $\ell=4m-\rho$ must be positive. For large active $X$ this is automatic after excluding finitely many small cases. The proof draft should state the small-$X$ absorption.

4. **Dyadic weights.** The R5 proof uses $|w_D|$ and bounded overlap. It does not require real weights. Paired formulas for $\mathcal M_2$ do require either complex cosine pairing or real-weight $\operatorname{Re}B_h$ interpretation.

5. **$\Phi$ asymmetry.** It is false that $\Phi(1-u)=\Phi(u)$. Any implementation using symmetry of $\Phi$ across $1/2$ is wrong. The correct identity is $\Phi(1-u)=1-\Phi(u)$.

6. **Average-to-pointwise gap.** This is a genuine analytic obstruction. A global average cannot be converted into a pointwise M9 estimate by the elementary derivative bound without losing the near-collision scale.

7. **Exact-resonance taxonomy remains incomplete.** Denominator-paired and paired-core families are subfamilies. Mixed and unclassified exact $N=0$ configurations remain open.

8. **Near-collision bands remain open.** The condition
$$
0<|N|\lesssim D^4/X
$$
is meaningful for global averages, but the pointwise route may require a different mechanism.

9. **M1 remains analytically untouched in this round.** Even a complete M2 route would not promote `M9` without M1.

## Counterexample or obstruction search

### Obstruction 1: Vaaler endpoint mismatch

At integer $t=n$,

$$
\psi_C(n)=0,
\qquad
\psi_F(n)=-\frac12.
$$

The Vaaler polynomial has $V_H(n)=0$, while

$$
\frac1{2H+2}K_H(0)=\frac12.
$$

This does not falsify H4; it confirms that the Fejer residual is exactly large enough to cover the floor-compatible half-jump.

### Obstruction 2: divisor-rich residual spikes

If $X$ is an integer with many divisors, many $d$ may satisfy $X/d\in\mathbb Z$. Their contribution is bounded by divisor multiplicity:

$$
\#\{d\asymp D:d\mid X\}\le\tau(X)\ll_\epsilon X^\epsilon.
$$

Near-spikes are controlled by the same product-count kernel and contribute $O_\epsilon(X^{1/4+\epsilon})$. Divisor-rich $X$ does not break R5.

### Obstruction 3: shifted Fejer spikes

If

$$
\frac{X/d+\rho}{4}\in\mathbb Z,
$$

then

$$
X=d(4m-\rho).
$$

The number of such representations is bounded by $\tau(X)$ with a congruence restriction on the complementary factor. No new residual obstruction appears.

### Obstruction 4: complex-weight paired formula failure

For complex $w_D$, the identity

$$
\sum_d w_D(d)\cos(2\pi hX/(4d))=\operatorname{Re}B_h(D;X)
$$

is false. Therefore A3 must test:

- raw two-sided formula;
- complex-weight cosine formula;
- deliberate failure of the real-weight $\operatorname{Re}B_h$ shortcut.

### Obstruction 5: average-to-pointwise derivative loss

The derivative bound

$$
|S_2'(D;X)|\ll D X^{-1/4}
$$

forces

$$
|I|\lesssim X^{1/2}/D
$$

if the derivative error is to stay below fourth-moment scale $X^{1+\epsilon}$. This makes the averaging window too short to recover the global near-collision threshold $D^4/X$.

This is a route-level obstruction to any proof that says "we have a fourth-moment average, therefore pointwise follows" without a separate unsmoothing argument.

### Obstruction 6: Li--Yang high-frequency gap

At the endpoint $D=X^{1/2}$, M9 needs $H_D=X^{1/4}$. Li--Yang's final exponent $\theta^*=0.314483\ldots$ corresponds to height $X^{0.185516\ldots}$ in the same endpoint normalization. Thus Li--Yang cannot be imported as a black-box endpoint M9 theorem.

### Obstruction 7: sign erasure by norm extraction

Any proof step that transforms the $\chi_4(h)$ sign into a diagonal unitary and then estimates by an operator norm, Frobenius norm, Schur bound, Gershgorin bound, cyclic trace, or absolute-value majorant is character-blind. Such a step may still produce valid upper bounds, but it should not be described as exploiting the M2 character factor.

## Verification

### H4 checks

The proof draft should verify the following against the rendered PDF:

- printed page 192, Theorem 6, equation (2.28):
$$
\widehat J(t)=\pi t(1-|t|)\cot(\pi t)+|t|,
\qquad 0<|t|<1;
$$

- printed page 207, equations (7.1)--(7.3), definitions of $i_N,j_N,k_N$;

- printed page 210, Theorem 18, especially
$$
|\psi*j_N(x)-\psi(x)|\le(2N+2)^{-1}k_N(x);
$$

- $K_H(0)=H+1$;

- $\alpha_{h,H}=-\Phi(|h|/(H+1))/(2\pi i h)$;

- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$;

- integer jump coverage:
$$
|\psi_F(n)-V_H(n)|=\frac12=\frac1{2H+2}K_H(0).
$$

### R5 checks

The proof draft should explicitly include:

- nearest-integer tie convention;
- exact resonance $W_\Delta(0)=1$;
- first leg $n=md$;
- shifted legs $n=d(4m-\rho)$;
- congruence $\ell\equiv-\rho\pmod4$;
- positivity of $\ell$ for large active $X$;
- small-$X$ absorption;
- dyadic bounded overlap;
- short block removal before Vaaler;
- logarithmic losses absorbed into $X^\epsilon$.

### M9 formula checks

A3 should compare:

$$
\mathcal M_2^{\mathrm{raw}}
=
4\sum_{1\le |h|\le H_D}\beta_h\sum_d w_D(d)e(hX/(4d))
$$

against

$$
\mathcal M_2^{\mathrm{cos}}
=
8\sum_{1\le h\le H_D}\beta_h
\sum_d w_D(d)\cos(2\pi hX/(4d)).
$$

For real $w_D$, also compare against

$$
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}B_h(D;X).
$$

For complex $w_D$, this last formula should fail unless it is replaced by the cosine formula.

## Divergent alternatives and 20% exploration

### Alternative A: exact-resonance taxonomy beyond paired-core

The denominator-paired exact resonance is already treated under H4, and the paired-core families are partially controlled. The next structural problem is mixed/unclassified exact $N=0$ mass.

Needed lemma:

For actual $\beta_h$ coefficients and bounded dyadic weights,

$$
\sum_{\substack{
d_i\asymp D,\ 1\le |h_i|\le H_D\\
N=0\\
\text{mixed or unclassified}
}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\ll_\epsilon X^{1+\epsilon},
$$

preferably $\ll_\epsilon D^2X^\epsilon$ if true.

Why it might work: the reciprocal weights $|\beta_h|\ll1/|h|$ sharply reduce frequency-difference multiplicities, as in the denominator-paired harmonic-convolution proof.

Likely obstruction: exact rational identities may create families not parameterized by one linear difference equation. If they have two free denominator variables and too many frequency choices, the absolute weighted mass may exceed $D^2X^\epsilon$.

Fast falsification test: A3 should enumerate unclassified exact $N=0$ mass with actual $\beta_h$ weights and fit against $D^2$, $D^2\log^A D$, $D^{5/2}$, and $D^3$.

### Alternative B: direct signed bilinear estimate

The theorem-shaped target is:

$$
\left|
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\right|
\ll_\epsilon X^{1/4+\epsilon}.
$$

This route tries to preserve $\chi_4(h)$ rather than bounding by $|\beta_h|$.

A possible sign-preserving large-sieve formulation is:

For phases

$$
\lambda_{h,d}=\frac{h}{4d},
$$

and coefficients

$$
a_h=
-\frac{\Phi(|h|/(H_D+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

prove a bound for

$$
\sum_d w_D(d)\sum_h a_h e(X\lambda_{h,d})
$$

that is stronger than the same estimate with $|a_h|$ or adversarial signs.

Why it might work: the $\chi_4(h)$ sign is in the Fourier variable, not the denominator variable, and may survive a carefully designed signed spacing statistic.

Likely obstruction: standard Cauchy or large-sieve proofs replace $a_h\overline{a_{h'}}$ by absolute values or unitary conjugations, erasing $\chi_4$.

Fast falsification test: compare actual $\beta_h$, $|\beta_h|$, random signs, and adversarial signs for endpoint blocks $D=X^{1/2}$ and intermediate blocks $D=X^{3/8}$. If the actual signs track unsigned/adversarial behavior, deprioritize this route.

### Alternative C: Li--Yang/Bombieri--Iwaniec extension

A theorem-extension route would map the M9 sums to Li--Yang-type double sums

$$
\sum_{h\sim H}\sum_{m\sim M}e(-hT/m),
$$

or to the smooth phase version

$$
\sum_{h\sim H}g(h/H)\sum_{m\sim M}G(m/M)e\left(\frac{hT}{M}F(m/M)\right).
$$

Needed new theorem: a Bombieri--Iwaniec first/second-spacing estimate reaching the height

$$
H\le M T^{-1/4}
$$

rather than the Li--Yang height corresponding to $\theta^*=0.314483\ldots$.

Why it might work: M9 has the same reciprocal phase geometry as the circle/divisor double sums.

Likely obstruction: the existing Li--Yang theorem is designed to improve the known exponent to $\theta^*$, not to reach $\theta=1/4$. The endpoint M9 height is outside the black-box range.

Fast falsification test: finish the Li--Yang source card and write the exact $(H,M,T)$ inequalities for $M=D$, $T=X$ or $X/4$, and $H=DX^{-1/4}$. If any required Case A/B hypothesis fails at $D=X^{1/2}$, black-box import is rejected.

### Alternative D: smoothed Poisson--Bessel calibration

This is not a primary M9 route, but it is a useful sanity module. Prove the classical smoothed Poisson--Bessel formula and recover the $R^{2/3}$-type bound by standard smoothing/unsmoothing.

Needed lemma: a clean radial smoothing sandwich with Bessel asymptotics, showing exactly where the classical exponent arises and why it does not imply the conjectural endpoint.

Why it might work as a diagnostic: it provides a separate normalization check for $P(X)$ and endpoint conventions.

Likely obstruction: this route does not directly exploit the finite Vaaler reciprocal sums and is not currently connected to `M9`.

Fast falsification test: if the smoothing/unsmoothing loss already exceeds $X^{1/4}$ under trivial Bessel-sum bounds, keep it as calibration only.

## Route proposals

### Route 1: proof-draft consolidation and H4/R5 closure

Rank: 1 for proof-graph hygiene, not for solving M9.

Exact obligation:

- Complete `sources/vaaler_1985.md`.
- Insert H4, R5-Full, M9 definitions, and Bridge into `best_proof_draft.md`.
- Keep H4 as `source_audit_required` until validated.
- Keep R5-Full as `derived_under_assumptions`.

Dependencies:

- Vaaler Theorem 6 and Theorem 18.
- Divisor bound $\tau(n)\ll_\epsilon n^\epsilon$.
- Bounded dyadic partition.

First proof step:

Write the source card and proof draft in the notation of this response.

Likely obstruction:

Only transcription and convention errors; no serious analytic obstruction remains for R5.

Falsification test:

Find any mismatch in the rendered Vaaler residual constant, coefficient sign, or Fejer normalization. If found, update constants and rerun A3 raw-vs-paired tests.

Expected proof-graph impact:

High. It removes ambiguity from H4/R5 and sharpens the remaining bottleneck to M9.

### Route 2: exact-resonance taxonomy and near-collision control

Rank: 2 for M2 progress.

Exact obligation:

Prove mixed/unclassified exact $N=0$ weighted mass bounds and then a near-collision estimate for

$$
0<|N|\lesssim D^4/X
$$

with actual $\beta_h$ weights.

Dependencies:

- M9-M2-beta-algebra.
- M9-M2-fourth-moment-expansion.
- Harmonic-convolution lemma.
- Denominator-paired bound under H4.

First proof step:

Classify mixed exact $N=0$ denominator patterns, not just paired-core patterns. Identify whether every unclassified solution admits a parameterization with a divisor or harmonic-convolution saving.

Likely obstruction:

The exact variety $N=0$ may contain higher-dimensional rational families not controlled by pairwise denominator coincidences.

Falsification test:

A3 enumeration shows unclassified absolute weighted mass growing faster than $X^{1+o(1)}$ or faster than $D^2X^{o(1)}$ in the expected paired-core normalization.

Expected proof-graph impact:

Moderate to high if successful. It would advance `M9-near-collision-taxonomy`, but it still would not prove `M9-M2` without pointwise or near-collision control.

### Route 3: average-to-pointwise fourth moment

Rank: 3 because it exposes a gap, but the naive version is currently weak.

Exact obligation:

Prove a local fourth-moment-to-pointwise implication for $S_2(D;X)$ that reaches

$$
|S_2(D;X_0)|^4\ll_\epsilon X_0^{1+\epsilon}
$$

uniformly in active $D$.

Dependencies:

- A fourth-moment estimate over an interval $I$.
- Derivative or unsmoothing control.
- Endpoint uniformity.

First proof step:

Attempt the local Lipschitz inequality and quantify the window length. This response already shows the trivial derivative bound forces

$$
|I|\lesssim X^{1/2}/D.
$$

Likely obstruction:

At such short lengths, the average does not impose the desired near-collision threshold $D^4/X$.

Falsification test:

Show that any available fourth-moment estimate only holds on intervals $L\gg X^\eta X^{1/2}/D$ or on global intervals $L\asymp X$, with no stronger derivative control. Then this route cannot close M2.

Expected proof-graph impact:

High if repaired by a new smoothing argument; otherwise mostly diagnostic.

### Route 4: direct signed bilinear estimate

Rank: 4 as backup, but potentially the only route that can exploit $\chi_4(h)$ signs.

Exact obligation:

Prove

$$
S_2(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

directly, preserving the $\chi_4(h)$ sign beyond the first norm extraction.

Dependencies:

- M9-M2-beta-algebra.
- A new sign-preserving spacing or large-sieve theorem.
- Endpoint uniformity.

First proof step:

Write one finite signed statistic whose smallness implies M9-M2 and verify it is not invariant under diagonal-unitary sign erasure.

Likely obstruction:

Cauchy, large-sieve, and operator-norm arguments tend to replace the sign by $|\beta_h|$.

Falsification test:

A3 signed-vs-unsigned comparison. If true $\beta_h$ behaves like unsigned/adversarial signs, the route is unlikely to succeed without a new idea.

Expected proof-graph impact:

Potentially high, but evidence currently weak.

## Useful lemmas

### Lemma H4-R5A: finite Vaaler approximation with floor-compatible residual

For every integer $H\ge1$ and real $t$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)
+
R_H^F(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H^F(t)|
\le
\frac1{2H+2}K_H(t).
$$

Status: source-audit-required external theorem dependency.

### Lemma R5-Full-R5A: pointwise Fejer residual product-count bound

For active $D$ and $H_D\asymp DX^{-1/4}$,

$$
\frac1{H_D}\sum_{d\asymp D}|w_D(d)|K_{H_D}(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1{H_D}
\sum_{d\asymp D}|w_D(d)|
K_{H_D}\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Status: derived under H4.

### Lemma M2-beta-R5A: exact $\beta_h$ algebra

Assuming H4 coefficient convention,

$$
\beta_{h,H}=\alpha_{h,H}(e(h/4)-e(3h/4))
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Thus $\beta_h$ is real and even.

Status: derived under H4.

### Lemma M2-pairing-R5A: raw and paired M2 formulas

Raw two-sided:

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}\beta_h\sum_d w_D(d)e(hX/(4d)).
$$

Complex-weight cosine pairing:

$$
\mathcal M_2(D;X)
=
8\sum_{1\le h\le H_D}\beta_h
\sum_d w_D(d)
\cos\left(\frac{2\pi hX}{4d}\right).
$$

Real-weight paired formula:

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\operatorname{Re}B_h(D;X).
$$

Status: algebraic implementation lemma under H4; real-paired version requires real $w_D$.

### Lemma Local-Avg-Pointwise-R5A

For any $C^1$ function $S$ on an interval $I$ containing $X_0$,

$$
|S(X_0)|^4
\le
8\frac1{|I|}\int_I |S(X)|^4\,dX
+
8|I|^4\sup_I |S'(X)|^4.
$$

Applied to $S=S_2(D;\cdot)$, the trivial derivative bound is

$$
\sup_I|S_2'(D;X)|\ll D X^{-1/4}.
$$

Status: proved elementary inequality; diagnostic only. It currently reveals a gap rather than closing it.

## What should be tested next

1. Render-check Vaaler Theorem 6, Section 7, and Theorem 18 directly from the PDF images. Record exact page/equation labels in `sources/vaaler_1985.md`.

2. Implement H4 integer-jump tests:
$$
V_H(n)=0,\qquad
\psi_F(n)=-1/2,\qquad
K_H(0)/(2H+2)=1/2.
$$

3. Implement R5 first-leg and shifted-leg tables for:
   - square $X$;
   - near-square $X$;
   - nonsquare $X$;
   - divisor-rich $X$;
   - $D=X^{1/4},X^{3/8},X^{1/2}$.

4. Run raw-vs-paired M2 regression:
   - raw two-sided;
   - complex-weight cosine;
   - real-weight $\operatorname{Re}B_h$;
   - deliberate complex-weight failure of $\operatorname{Re}B_h$.

5. Enumerate exact $N=0$ fourth-moment bins:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - semi-diagonal;
   - mixed;
   - unclassified.

6. For unclassified exact $N=0$, report absolute and signed weighted mass normalized by $D^2$ and by $X$.

7. For near-collision bands, distinguish global-average threshold
$$
|N|\le C_0D^4/X
$$
from local-window threshold
$$
|N|\le C_0D^4/L.
$$

8. Test average-to-pointwise numerically:
   - local sup of $|S_2|$;
   - local fourth-moment average;
   - derivative bound;
   - ratio in the inequality
$$
|S_2(X_0)|^4/
\left(
L^{-1}\int_I|S_2|^4+L^4\sup_I|S_2'|^4
\right).
$$

9. Run signed-vs-unsigned M2 tests:
   - true $\beta_h$;
   - $|\beta_h|$;
   - random signs;
   - adversarial signs.

10. Complete the Li--Yang source-card audit for:
   - definition of $S$;
   - Case A;
   - Case B;
   - allowed $F,g,G$ hypotheses;
   - absolute-value placement;
   - final $S/H$ target.

## Proposed state patch, if any

No proof-obligation status should be promoted from this Stage A packet alone.

Recommended Stage A patch proposal for the later judge to consider:

schema_version: 1
proposed_updates:
  - id: H4-source-audit
    status: source_audit_required
    proposed_next_action: "Populate sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, Fejer normalization K_H(0)=H+1, residual constant (2H+2)^(-1), and floor-compatible endpoint conversion."
    reason: "This packet drafts the source-card content but does not physically update the repository file."
  - id: H4
    status: source_audit_required
    proposed_next_action: "Keep H4 as source_audit_required until the source card is committed and validated; use H4-dependent lemmas only as derived_under_assumptions."
    reason: "The formula-level translation is stable, but the workflow requires a completed source card."
  - id: R5-Full-reconciliation
    status: derived_under_assumptions
    proposed_next_action: "Insert the positive Fejer product-count proof into best_proof_draft.md with first leg, shifted legs, exact resonances, short blocks, dyadic overlap, and divisor-count details."
    reason: "The proof is pointwise and avoids the old arbitrary-coefficient trap, but it depends on H4."
  - id: M9-M2-beta-algebra
    status: derived_under_assumptions
    proposed_next_action: "Insert beta_h algebra and M2 raw/cosine/real-paired formulas into best_proof_draft.md after H4 source-card update."
    reason: "The algebra depends on the H4 coefficient convention."
  - id: M9-M2-fourth-moment-average-to-pointwise
    status: open
    proposed_next_action: "Record the local Lipschitz inequality and derivative-loss obstruction; require any fourth-moment route to specify the averaging length and unsmoothing mechanism."
    reason: "The naive derivative upgrade only permits windows L <= X^(1/2)/D, too short to exploit the global near-collision threshold D^4/X."
no_change:
  - id: M9
    reason: "No uniform endpoint estimate for M1 and M2 is proved."
  - id: M9-M1
    reason: "No M1 estimate is supplied."
  - id: M9-M2
    reason: "M2 exact-resonance and pointwise control remain incomplete."
  - id: M9-near-collision-taxonomy
    reason: "Mixed and unclassified exact N=0 classes remain open."
  - id: M9-near-collision-estimate
    reason: "No near-collision estimate with actual beta weights is proved."
  - id: GC-target
    reason: "The final target remains conditional on M9."

## Confidence

High confidence:

- The Vaaler coefficient sign and Fejer normalization in this packet are internally consistent.
- The floor-compatible endpoint conversion is correct.
- The R5 product-count proof is pointwise and conditional only on H4.
- The raw two-sided and cosine-paired $\mathcal M_2$ formulas are algebraically correct under the stated conventions.
- The real-weight $\operatorname{Re}B_h$ formula must not be used for complex weights.
- `M9`, `M9-M2`, and `GC-target` must remain open.

Moderate confidence:

- The source-card draft contains all required Vaaler data, pending direct rendered-page validation.
- The local average-to-pointwise obstruction is a serious blocker for any averaged fourth-moment route.
- The paired-core exact-resonance route remains useful but probably insufficient alone.
- The direct signed bilinear route is the right backup, though no theorem-level estimate is currently available.

Low confidence:

- Existing Li--Yang/Bombieri--Iwaniec technology reaches the endpoint M9 height.
- A global fourth-moment average can be converted to pointwise M2 by elementary derivative control.
- Absolute near-collision estimates alone will prove the endpoint without a sign-preserving mechanism.

Overall confidence: 0.82 for proof-infrastructure and normalization claims; 0.35 for any route currently implying `M9-M2`; 0 for any claim of a completed Gauss circle endpoint proof.

--- OUTPUT FROM A2 ---
## Summary

This response executes the Stage A independent reasoning task for Round 5, acting as the conservative mathematical referee (A2). The primary objective is to advance the exact $N=0$ taxonomy for the $\mathcal{M}_2$ fourth moment by providing proof-draft-ready derivations for the pair-swapped and semi-diagonal exact resonance families, while strictly avoiding the re-proof of the denominator-paired subcase.

The analysis confirms that under the $H_4$ coefficient magnitude hypothesis $|\beta_h| \ll 1/|h|$, both the pair-swapped and semi-diagonal families yield a total absolute weighted mass bounded by $O_\epsilon(D^2 X^\epsilon)$. The pair-swapped bound follows by direct algebraic symmetry from the denominator-paired case, while the semi-diagonal bound is established via a lowest-terms parameterization and dyadic block summation. However, this response explicitly isolates the "mixed" (unclassified) exact resonance class as a remaining obstruction, demonstrating via a parameterized Egyptian-fraction toy model that strictly mixed solutions exist and carry non-trivial mass. Consequently, the full exact $N=0$ taxonomy cannot be claimed as resolved.

In addition to the core proofs, this document provides a comprehensive theorem-dependency audit, a ledger of provisional claims, explicit failure modes, and a 700+ word divergent exploration of a Diophantine geometric approach to the resonance hyperboloid. The proposed state patch updates the taxonomy obligations to reflect the completed paired-core proofs while keeping the mixed class strictly open.

## Target proof obligation

This reasoning stage targets the following proof obligations from `state/proof_obligations.yml`:

1.  **`M9-M2-paired-core-weighted-bound`**: Weighted paired-core exact M2 resonance bound. (Status: `derived_under_assumptions`). The task is to write proof-draft-ready proofs for the pair-swapped and semi-diagonal exact $N=0$ families.
2.  **`M9-M2-N0-diagonal-core-bound`**: Diagonal-core bound for exact M2 fourth-moment resonances. (Status: `open`).
3.  **`M9-near-collision-taxonomy`**: M2 fourth-moment near-collision taxonomy. (Status: `open`).

## Main claim or direction

**Claim 1 (Pair-Swapped Exact Resonance Bound):** Under the $H_4$ assumption that $|\beta_h| \ll 1/|h|$ for $1 \le |h| \le H_D$, the pair-swapped exact $N=0$ family (defined by $d_1=d_4$ and $d_2=d_3$) contributes a total absolute weighted mass of $O_\epsilon(D^2 X^\epsilon)$ to the $\mathcal{M}_2$ fourth moment, uniformly for $X^{1/4} \le D \le X^{1/2}$.

**Claim 2 (Semi-Diagonal Exact Resonance Bound):** Under the same $H_4$ assumption, the semi-diagonal exact $N=0$ family (defined by $h_1/d_1 = h_2/d_2$ and $h_3/d_3 = h_4/d_4$, or permutations thereof) contributes a total absolute weighted mass of $O(D^2)$ to the $\mathcal{M}_2$ fourth moment.

**Claim 3 (Mixed Class Obstruction):** The paired and semi-diagonal families do not exhaust the exact $N=0$ solutions. Strictly mixed solutions (e.g., generated by rational relations like $1/2 - 1/3 + 1/6 - 1/3 = 0$) exist within the active dyadic ranges and form parameterized families that prevent the immediate closure of the `M9-near-collision-taxonomy` obligation.

## Detailed reasoning: Setup and Notation

We analyze the fourth moment of the reciprocal sum $\mathcal{M}_2(D;X)$. The localized sum is given by:

$$
S_2(D;X) = \sum_{1 \le |h| \le H_D} \beta_{h,H_D} \sum_{d \asymp D} w_D(d) e\left(\frac{hX}{4d}\right)
$$

where $H_D \asymp D X^{-1/4}$, $X^{1/4} \le D \le X^{1/2}$, and $w_D(d)$ is a bounded dyadic weight supported on $D \le d < 2D$. The coefficients $\beta_{h,H_D}$ are real, even, and satisfy the $H_4$-dependent bound $|\beta_{h,H_D}| \ll 1/|h|$.

Expanding $|S_2(D;X)|^4$ yields a sum over 8 variables $(h_1, d_1, h_2, d_2, h_3, d_3, h_4, d_4)$ with the phase:

$$
\frac{X}{4} \left( \frac{h_1}{d_1} - \frac{h_2}{d_2} + \frac{h_3}{d_3} - \frac{h_4}{d_4} \right) = \frac{X}{4 d_1 d_2 d_3 d_4} N
$$

where the cleared resonance integer is:

$$
N = h_1 d_2 d_3 d_4 - h_2 d_1 d_3 d_4 + h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3
$$

The exact resonance condition is $N=0$, which is algebraically equivalent to the phase vanishing identically:

$$
\frac{h_1}{d_1} - \frac{h_2}{d_2} + \frac{h_3}{d_3} - \frac{h_4}{d_4} = 0
$$

We seek to bound the absolute weighted mass of specific subfamilies of the $N=0$ solution set. The mass is defined as:

$$
\mathcal{E}_{\text{family}} = \sum_{(h_i, d_i) \in \text{family}} |\beta_{h_1} \beta_{h_2} \beta_{h_3} \beta_{h_4}| |w_D(d_1) w_D(d_2) w_D(d_3) w_D(d_4)|
$$

Since $w_D(d) \ll 1$, we majorize this by:

$$
\mathcal{E}_{\text{family}} \ll \sum_{(h_i, d_i) \in \text{family}} \frac{1}{|h_1 h_2 h_3 h_4|}
$$

## Detailed reasoning: Pair-Swapped Exact Resonance Bound

The pair-swapped family is defined by the index permutation $d_1 = d_4$ and $d_2 = d_3$. Let $d_1 = d_4 = a$ and $d_2 = d_3 = b$, where $a, b \asymp D$.

Substituting these into the exact resonance condition yields:

$$
\frac{h_1}{a} - \frac{h_2}{b} + \frac{h_3}{b} - \frac{h_4}{a} = 0 \implies \frac{h_1 - h_4}{a} + \frac{h_3 - h_2}{b} = 0
$$

Clearing denominators, we obtain the linear Diophantine constraint:

$$
(h_1 - h_4)b + (h_3 - h_2)a = 0
$$

This equation is structurally identical to the denominator-paired condition $(h_1 - h_2)b + (h_3 - h_4)a = 0$, under the involution $(h_2 \leftrightarrow h_4)$. Because the summation ranges $1 \le |h_i| \le H_D$ are symmetric and identical for all four frequency variables, and the absolute weight function $\prod |h_i|^{-1}$ is invariant under any permutation of the indices, the sum over the pair-swapped family is exactly equal to the sum over the denominator-paired family.

To make the proof draft self-contained without re-deriving the harmonic convolution, we formalize the symmetry argument:

1.  Let $\Omega_{\text{DP}}$ be the set of tuples $(h_1, h_2, h_3, h_4, a, b)$ satisfying $1 \le |h_i| \le H_D$, $a, b \asymp D$, and $(h_1 - h_2)b + (h_3 - h_4)a = 0$.
2.  Let $\Omega_{\text{PS}}$ be the set of tuples $(h_1, h_2, h_3, h_4, a, b)$ satisfying $1 \le |h_i| \le H_D$, $a, b \asymp D$, and $(h_1 - h_4)b + (h_3 - h_2)a = 0$.
3.  Define the bijection $\phi: \Omega_{\text{DP}} \to \Omega_{\text{PS}}$ by $\phi(h_1, h_2, h_3, h_4, a, b) = (h_1, h_4, h_3, h_2, a, b)$.
4.  The absolute weight $W(h_1, h_2, h_3, h_4) = |h_1 h_2 h_3 h_4|^{-1}$ satisfies $W(\phi(h)) = W(h)$.
5.  Therefore, $\sum_{\Omega_{\text{PS}}} W(h) = \sum_{\Omega_{\text{DP}}} W(h)$.

By the established `M9-M2-denominator-paired-weighted-bound` (which relies on `M9-M2-harmonic-convolution-LH`), the sum over $\Omega_{\text{DP}}$ is bounded by $O_\epsilon(D^2 X^\epsilon)$. Consequently, the pair-swapped mass is rigorously bounded by $O_\epsilon(D^2 X^\epsilon)$.

## Detailed reasoning: Semi-Diagonal Exact Resonance Bound

The semi-diagonal family is defined by the condition that the phase vanishes due to two independent internal cancellations. Up to permutation, the primary semi-diagonal configuration is:

$$
\frac{h_1}{d_1} = \frac{h_2}{d_2} \quad \text{and} \quad \frac{h_3}{d_3} = \frac{h_4}{d_4}
$$

Because the variables $(h_1, d_1, h_2, d_2)$ are completely decoupled from $(h_3, d_3, h_4, d_4)$ in this configuration, the total mass factors into the square of a bilinear mass:

$$
\mathcal{E}_{\text{semi}} \ll \left( \sum_{\frac{h_1}{d_1} = \frac{h_2}{d_2}} \frac{1}{|h_1 h_2|} \right)^2 = W^2
$$

We now rigorously bound the bilinear mass $W$. The condition $h_1/d_1 = h_2/d_2$ implies that the two fractions reduce to the same rational number in lowest terms. Let this reduced fraction be $u/v$, where $u \in \mathbb{Z} \setminus \{0\}$, $v \in \mathbb{N}$, and $\gcd(|u|, v) = 1$.

This parameterization forces:
$$
h_1 = k_1 u, \quad d_1 = k_1 v
$$
$$
h_2 = k_2 u, \quad d_2 = k_2 v
$$
for some integers $k_1, k_2 \ge 1$.

We must enforce the summation constraints:
1.  $d_1, d_2 \asymp D \implies k_1 v \asymp D$ and $k_2 v \asymp D$. This restricts $k_1, k_2 \in [D/v, 2D/v)$.
2.  $1 \le |h_1|, |h_2| \le H_D \implies 1 \le |k_1 u|, |k_2 u| \le H_D$.

Substituting this parameterization into $W$:

$$
W = \sum_{v \le 2D} \sum_{u \neq 0} \sum_{k_1 \asymp D/v} \sum_{k_2 \asymp D/v} \frac{1}{|k_1 u| |k_2 u|}
$$

We can separate the sums over $k_1$ and $k_2$:

$$
W = \sum_{v \le 2D} \sum_{u \neq 0} \frac{1}{u^2} \left( \sum_{k \asymp D/v} \frac{1}{k} \right)^2
$$

Crucially, the sum over $k$ is restricted to a dyadic block $[D/v, 2D/v)$. The harmonic sum over a dyadic interval is bounded by a constant, independent of the endpoints:

$$
\sum_{k = \lceil D/v \rceil}^{\lfloor 2D/v \rfloor} \frac{1}{k} \ll \log\left(\frac{2D/v}{D/v}\right) = \log 2 \ll 1
$$

Therefore, the squared inner sum is $O(1)$. The sum over $u$ converges absolutely:

$$
\sum_{u \neq 0} \frac{1}{u^2} = 2 \zeta(2) = \frac{\pi^2}{3} \ll 1
$$

This leaves only the outer sum over the reduced denominator $v$:

$$
W \ll \sum_{v \le 2D} 1 \cdot 1 \ll D
$$

Squaring this bilinear mass yields the total semi-diagonal mass:

$$
\mathcal{E}_{\text{semi}} \ll W^2 \ll D^2
$$

This bound is extremely sharp--it does not even incur a logarithmic penalty. The proof is complete and ready for integration into the proof draft.

## Detailed reasoning: The Mixed Exact Resonance Obstruction

While the paired and semi-diagonal families are now rigorously bounded by $O(D^2 X^\epsilon)$, the `M9-near-collision-taxonomy` obligation requires classifying *all* exact $N=0$ solutions. We must address the "mixed" or unclassified class, where $N=0$ but no two fractions $h_i/d_i$ are equal, nor do they form symmetric pairs.

Consider the rational relation:
$$
\frac{1}{2} - \frac{1}{3} + \frac{1}{6} - \frac{1}{3} = 0
$$
We can embed this relation into the $\mathcal{M}_2$ summation variables by scaling. Let $u \in \mathbb{Z} \setminus \{0\}$ and $v \in \mathbb{N}$. Set:
$$
\frac{h_1}{d_1} = \frac{u}{2v}, \quad \frac{h_2}{d_2} = \frac{u}{3v}, \quad \frac{h_3}{d_3} = \frac{u}{6v}, \quad \frac{h_4}{d_4} = \frac{u}{3v}
$$
To satisfy $d_i \asymp D$, we introduce multipliers $k_i$:
$$
h_1 = k_1 u, \quad d_1 = k_1 (2v) \implies k_1 \asymp \frac{D}{2v}
$$
$$
h_2 = k_2 u, \quad d_2 = k_2 (3v) \implies k_2 \asymp \frac{D}{3v}
$$
$$
h_3 = k_3 u, \quad d_3 = k_3 (6v) \implies k_3 \asymp \frac{D}{6v}
$$
$$
h_4 = k_4 u, \quad d_4 = k_4 (3v) \implies k_4 \asymp \frac{D}{3v}
$$
For this specific family, the mass contribution is:
$$
\mathcal{E}_{\text{mixed\_toy}} = \sum_{v \le D/6} \sum_{u \neq 0} \frac{1}{u^4} \left( \sum_{k_1 \asymp D/(2v)} \frac{1}{k_1} \right) \left( \sum_{k_2 \asymp D/(3v)} \frac{1}{k_2} \right) \left( \sum_{k_3 \asymp D/(6v)} \frac{1}{k_3} \right) \left( \sum_{k_4 \asymp D/(3v)} \frac{1}{k_4} \right)
$$
As shown in the semi-diagonal proof, each dyadic sum over $k_i$ is $O(1)$. The sum over $u$ is $O(1)$. The sum over $v$ yields:
$$
\mathcal{E}_{\text{mixed\_toy}} \ll \sum_{v \le D/6} 1 \ll D
$$
This proves that a *single* rational relation generates a mixed family with mass $\asymp D$. The true obstruction lies in the multiplicity of such base rational relations. The equation $1/A - 1/B + 1/C - 1/E = 0$ has many solutions. If the number of such base relations bounded by $V$ grows like $V \log^c V$, integrating this over all possible scales $v$ could theoretically push the total mixed mass to $D^2$ or slightly higher.

Therefore, the mixed class is non-empty, carries macroscopic mass, and cannot be dismissed by taxonomy definitions. It must be bounded explicitly using additive energy or large sieve techniques before `M9-near-collision-taxonomy` can be closed.

## Claim Ledger

| ID | Claim | Status | Justification |
| :--- | :--- | :--- | :--- |
| CL-01 | Pair-swapped exact $N=0$ mass is $O_\epsilon(D^2 X^\epsilon)$. | `derived_under_assumptions` | Proved via exact algebraic bijection to the denominator-paired family, inheriting its harmonic convolution bound under $H_4$. |
| CL-02 | Semi-diagonal exact $N=0$ mass is $O(D^2)$. | `derived_under_assumptions` | Proved via lowest-terms parameterization $u/v$ and dyadic block summation, yielding a sharp bound without log penalties under $H_4$. |
| CL-03 | Mixed exact $N=0$ class is non-empty. | `proved_internal` | Demonstrated via the explicit parameterized family based on $1/2 - 1/3 + 1/6 - 1/3 = 0$. |
| CL-04 | A single mixed rational relation generates mass $\asymp D$. | `proved_internal` | Derived via dyadic summation over the scaling multipliers $k_i$. |
| CL-05 | Full exact $N=0$ taxonomy is resolved. | `rejected` | The mixed class remains unquantified over all possible base rational relations. |
| CL-06 | Dyadic harmonic sum $\sum_{k \asymp K} 1/k \ll 1$. | `proved_internal` | Standard calculus bound for $\log(2K) - \log(K) = \log 2$. |
| CL-07 | Pair-swapped phase involution preserves absolute weights. | `proved_internal` | The weight $\prod \|h_i\|^{-1}$ is invariant under the permutation $(h_2 \leftrightarrow h_4)$. |
| CL-08 | Semi-diagonal condition decouples into independent bilinear sums. | `proved_internal` | The condition $h_1/d_1 = h_2/d_2$ shares no variables with $h_3/d_3 = h_4/d_4$. |

## Theorem-dependency audit

1.  **`H4` (Vaaler approximation)**: The proofs for pair-swapped and semi-diagonal bounds strictly require the coefficient magnitude bound $|\beta_h| \ll 1/|h|$. If the true Vaaler coefficients exhibit constructive interference that violates this pointwise bound, the harmonic sums diverge. Status: `source_audit_required`.
2.  **`M9-M2-harmonic-convolution-LH`**: The pair-swapped proof relies entirely on this lemma to bound the shifted divisor sums. Status: `proved_internal` (from Round 4).
3.  **`M9-M2-denominator-paired-weighted-bound`**: Used as a black-box symmetry target for the pair-swapped proof. Status: `derived_under_assumptions`.
4.  **Dyadic Harmonic Summation**: The semi-diagonal proof relies on $\sum_{k \asymp K} 1/k \ll 1$. This is a standard elementary result, but its application requires strict adherence to the dyadic support of $w_D(d)$.
5.  **Absolute Convergence of $\zeta(2)$**: Used to bound the numerator sum $\sum u^{-2}$ in the semi-diagonal proof. Standard analytic number theory fact.
6.  **Missing Theorem (Mixed Class Additive Energy)**: To bound the full mixed class, we lack a theorem controlling the number of solutions to $h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4 = 0$ weighted by $(h_1 h_2 h_3 h_4)^{-1}$. A continuous large sieve or Gallagher-type lemma is required here.

## Unsupported-closure audit

In previous rounds, claims were made that the "full exact N=0 taxonomy is proved" and that the "diagonal core is bounded." These claims were correctly rejected by the judge because they ignored the mixed class. This response explicitly repairs that overreach by:
1.  Restricting the $O(D^2)$ claims strictly to the *paired* and *semi-diagonal* subfamilies.
2.  Providing a concrete, parameterized counterexample (the $1/2 - 1/3 + 1/6 - 1/3$ family) that proves the mixed class exists and carries mass.
3.  Refusing to promote `M9-near-collision-taxonomy` to proved, keeping it `open` until the mixed class is globally bounded.

## Hidden assumptions and potential gaps

1.  **Failure Mode 1: Boundary Effects in Dyadic Sums.** The semi-diagonal proof assumes $k_1$ ranges exactly over a dyadic block $D/v \le k_1 < 2D/v$. If the weight $w_D(d)$ is not a sharp cutoff but a smooth bump function, the sum $\sum w_D(k_1 v) / k_1$ is still $O(1)$, but the exact constants depend on the derivative of $w_D$. This is safe but must be tracked.
2.  **Failure Mode 2: Mixed Class Explosion.** If the number of base rational relations $1/A - 1/B + 1/C - 1/E = 0$ grows too fast with respect to the denominators, the sum over all such families could exceed $D^2 X^\epsilon$. This is the primary remaining threat to the exact $N=0$ bound.
3.  **Failure Mode 3: Sign Cancellation Reliance.** The current proofs use the absolute weight $|\beta_h|$. If the mixed class absolute mass exceeds $D^2 X^\epsilon$, we will be forced to use the signed weights $\beta_h$. However, the exact $N=0$ condition does not easily preserve the $\chi_4(h)$ character signs, potentially leading to a dead end if absolute bounds fail.
4.  **Failure Mode 4: $H_D$ Truncation Asymmetry.** The parameterization $h_1 = k_1 u$ requires $1 \le |k_1 u| \le H_D$. The proof majorizes this by extending the sum over $u$ to infinity. This is an upper bound, so it is safe, but it might lose a small factor of sharpness near the truncation edge.
5.  **Failure Mode 5: Coprimality in Mixed Class.** The toy model for the mixed class assumed $u$ and $v$ were independent. In reality, the exact Diophantine equation $h_1 d_2 d_3 d_4 - \dots = 0$ imposes complex coprimality conditions that might suppress the number of solutions, meaning the $O(D)$ mass per family is an overestimate.

## Counterexample or obstruction search

The primary obstruction is the **Mixed Exact Resonance Class**.

To search for a counterexample where the mixed class mass exceeds $D^2$, we must analyze the density of solutions to the Egyptian fraction equation:
$$
\frac{x_1}{y_1} + \frac{x_3}{y_3} = \frac{x_2}{y_2} + \frac{x_4}{y_4}
$$
subject to $y_i \asymp D$ and $x_i \le H_D$.

Let $S(V)$ be the number of solutions to $1/A + 1/C = 1/B + 1/E$ with $A, B, C, E \le V$ and $\gcd(A,B,C,E)=1$. It is known from the circle method that $S(V) \asymp V^2 \log^3 V$.
For each such base relation, we can scale it by $u/v$ as in the toy model. The number of valid scalings $v$ is roughly $D/V$.
The mass contribution per base relation is $\asymp D/V$.
Integrating this over all base relations up to scale $V \asymp D$:
$$
\text{Total Mixed Mass} \approx \sum_{V \le D} S(V) \cdot \frac{D}{V} \cdot (\text{weight factor})
$$
The weight factor depends on the numerators $u$, which introduces a $1/u^4$ decay. If the base relations require large numerators to satisfy the $H_D$ bounds, the mass is heavily suppressed. A rigorous upper bound requires applying a fourth-moment divisor bound to the equation $n_1 + n_3 = n_2 + n_4$ where $n_i = h_i / d_i$. This remains an open analytic task.

## Verification

**Stress Test 1: Pair-Swapped Symmetry Check.**
Symbolically verify that the substitution $d_1 \leftrightarrow d_4$ maps the denominator-paired phase exactly to the pair-swapped phase, and that the integration measure $\prod dh_i/h_i$ is invariant. (Passed analytically in Section 2).

**Stress Test 2: Semi-Diagonal Dyadic Sum.**
Numerically evaluate $f(D, v) = \sum_{k=\lceil D/v \rceil}^{\lfloor 2D/v \rfloor} 1/k$ for $D=10^6$ and various $v \in [1, D]$. Confirm that $f(D, v)$ is strictly bounded by $\log 2 + O(v/D)$, verifying the $O(1)$ claim.

**Stress Test 3: Mixed Class Enumeration.**
Write a Python script using `itertools` to enumerate all exact $N=0$ solutions for $D=50, H_D=10$. Filter out pair-equality, denominator-paired, pair-swapped, and semi-diagonal solutions. Sum the absolute weights $(h_1 h_2 h_3 h_4)^{-1}$ of the remaining mixed solutions. Compare this sum to $D^2$.

**Stress Test 4: Toy Model Mass Verification.**
For the specific family $1/2 - 1/3 + 1/6 - 1/3 = 0$, numerically sum the weights for $D=1000, H_D=100$ and confirm the mass scales linearly with $D$, not $D^2$ or $\log D$.

## Divergent alternatives and 20% exploration

To break the deadlock on the mixed exact resonance class and the impending near-collision bands, we should explore a genuinely different mathematical formulation: **Lattice Point Counting on the Resonance Hyperboloid via the Circle Method**.

Currently, the taxonomy approach attempts to manually classify solutions to the Diophantine equation:
$$
h_1 d_2 d_3 d_4 - h_2 d_1 d_3 d_4 + h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3 = N
$$
This is a polynomial equation of degree 4 in 8 variables. For $N=0$, it defines a projective variety $\mathcal{V}$ in $\mathbb{P}^7$. Instead of decomposing $\mathcal{V}$ into linear subspaces (the paired and semi-diagonal families) and struggling with the residual points (the mixed class), we can treat $\mathcal{V}$ as a single geometric object.

**The Geometric Variety Formulation:**
We wish to estimate the sum:
$$
\mathcal{I}(N) = \sum_{\mathbf{x} \in \mathcal{V}_N \cap \mathcal{B}} W(\mathbf{x})
$$
where $\mathbf{x} = (h_1, h_2, h_3, h_4, d_1, d_2, d_3, d_4)$, $\mathcal{B}$ is the bounding box $[1, H_D]^4 \times [D, 2D]^4$, and $W(\mathbf{x}) = (h_1 h_2 h_3 h_4)^{-1}$.

**The Hardy-Littlewood Circle Method Application:**
We can detect the condition $N=0$ using continuous orthogonality:
$$
\mathcal{I}(0) = \int_0^1 \left| \sum_{h \le H_D} \sum_{d \asymp D} \frac{\beta_h}{h} e(\alpha h / d) \right|^4 d\alpha
$$
Wait, the phase in the integral would be $\alpha (h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4)$. This is exactly the fourth moment of the exponential sum $T(\alpha) = \sum_{h, d} \frac{\beta_h}{h} e(\alpha h / d)$.
By Parseval's theorem, the exact $N=0$ mass is exactly $\int_0^1 |T(\alpha)|^4 d\alpha$.

This continuous relaxation is incredibly powerful. Instead of counting Diophantine solutions, we bound the $L^4$ norm of the trigonometric polynomial $T(\alpha)$.
We can apply standard major arc and minor arc decompositions to $T(\alpha)$.
- **Major Arcs:** $\alpha$ is near a rational $a/q$ with small $q$. Here, the sum $T(\alpha)$ exhibits constructive interference. The major arc contribution corresponds exactly to the highly structured paired and semi-diagonal families.
- **Minor Arcs:** $\alpha$ is far from rationals with small denominators. Here, $T(\alpha)$ experiences square-root cancellation. The minor arc integral bounds the chaotic "mixed" class automatically!

**Falsification Test and Computational Verification:**
To test if this Circle Method route is viable, we must check if the $L^2$ norm of $T(\alpha)$ is small enough to allow an $L^\infty$ bound on the minor arcs to yield the required $L^4$ bound.
Compute $\int_0^1 |T(\alpha)|^2 d\alpha$. This is the number of solutions to $h_1/d_1 = h_2/d_2$, which we already proved in the semi-diagonal section is bounded by $O(D)$.
If $\sup_{\alpha \in \mathfrak{m}} |T(\alpha)| \ll D^{1/2}$, then the minor arc contribution to the fourth moment is bounded by $\sup |T|^2 \int |T|^2 \ll D \cdot D = D^2$.
This would completely solve the mixed class obstruction in one stroke. The next exploratory step should be to formulate a precise Weyl bound for $T(\alpha)$ on the minor arcs.

## Repair or alternative route

**Criticized Route:** The claim that the "full exact N=0 taxonomy is proved" or that the "diagonal core is bounded" (implying closure of the exact resonance problem).

**Repair:** We repair this by strictly narrowing the claim to the `M9-M2-paired-core-weighted-bound`. The taxonomy is explicitly bifurcated into the "Paired/Semi-Diagonal Core" (which is now rigorously bounded by $O(D^2)$ under $H_4$) and the "Mixed Class" (which remains open).

**Alternative Route for the Mixed Class:** Instead of attempting to parameterize all Egyptian fraction solutions, we propose the $L^4$ norm continuous relaxation (detailed in the Divergent section).
*Exact Lemma Proposal:* Let $T(\alpha) = \sum_{1 \le |h| \le H_D} \frac{1}{|h|} \sum_{d \asymp D} e(\alpha h / d)$. Prove that $\int_0^1 |T(\alpha)|^4 d\alpha \ll_\epsilon D^2 X^\epsilon$.
*Falsification Test:* Numerically integrate $\int_0^1 |T(\alpha)|^4 d\alpha$ for $D=100, H_D=10$ and check if the growth rate exceeds $D^2$.

## Useful lemmas

```markdown
**Lemma (Pair-Swapped Exact Resonance Bound)**
Let $\Omega_{\text{PS}}$ be the set of indices satisfying $1 \le |h_i| \le H_D$, $d_1=d_4=a \asymp D$, $d_2=d_3=b \asymp D$, and $(h_1-h_4)b + (h_3-h_2)a = 0$. Assuming $|\beta_h| \ll 1/|h|$, the absolute weighted mass $\sum_{\Omega_{\text{PS}}} |h_1 h_2 h_3 h_4|^{-1}$ is bounded by $O_\epsilon(D^2 X^\epsilon)$.
*Proof:* Follows by the index involution $(h_2 \leftrightarrow h_4)$ mapping $\Omega_{\text{PS}}$ bijectively to the denominator-paired set $\Omega_{\text{DP}}$, preserving the absolute weight measure.
```

```markdown
**Lemma (Semi-Diagonal Exact Resonance Bound)**
Let $\Omega_{\text{SD}}$ be the set of indices satisfying $1 \le |h_i| \le H_D$, $d_i \asymp D$, $h_1/d_1 = h_2/d_2$, and $h_3/d_3 = h_4/d_4$. Assuming $|\beta_h| \ll 1/|h|$, the absolute weighted mass $\sum_{\Omega_{\text{SD}}} |h_1 h_2 h_3 h_4|^{-1}$ is bounded by $O(D^2)$.
*Proof:* The condition decouples into the square of a bilinear sum $W$. Parameterizing $h_1/d_1 = u/v$ in lowest terms forces $h_1 = k_1 u, d_1 = k_1 v$. The dyadic constraint $d_1 \asymp D$ restricts $k_1$ to a dyadic block, yielding $\sum 1/k_1 \ll 1$. Summing over $u \neq 0$ gives $\zeta(2)$, leaving $W \ll \sum_{v \le 2D} 1 \ll D$. Thus $W^2 \ll D^2$.
```

```markdown
**Lemma (Mixed Class Existence)**
The paired and semi-diagonal families do not exhaust the exact $N=0$ solutions for the phase $h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4 = 0$.
*Proof:* The parameterized family $h_1/d_1 = u/(2v), h_2/d_2 = u/(3v), h_3/d_3 = u/(6v), h_4/d_4 = u/(3v)$ provides strictly mixed solutions within the active dyadic ranges, contributing a mass of at least $\Omega(D)$.
```

```markdown
**Lemma (Dyadic Harmonic Block Bound)**
For any $v \ge 1$ and $D \ge v$, the harmonic sum over the dyadic block $k \in [D/v, 2D/v)$ satisfies $\sum_{k=\lceil D/v \rceil}^{\lfloor 2D/v \rfloor} \frac{1}{k} \le \log 2 + \frac{v}{D} \ll 1$.
*Proof:* Standard integral comparison test for the decreasing function $1/x$.
```

```markdown
**Lemma (Continuous $L^4$ Relaxation)**
The total absolute weighted mass of all exact $N=0$ resonances (including paired, semi-diagonal, and mixed) is exactly equal to the integral $\int_0^1 |T(\alpha)|^4 d\alpha$, where $T(\alpha) = \sum_{1 \le |h| \le H_D} |\beta_h| \sum_{d \asymp D} e(\alpha h / d)$.
*Proof:* Expanding the $L^4$ norm and integrating term-by-term isolates exactly the terms where the phase $h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4$ vanishes.
```

## What should be tested next

**For A3 (Executable Diagnostics):**
1.  **Mixed Class Enumeration Script:** Write a Python script that iterates over all $1 \le h_i \le H_D$ and $D \le d_i < 2D$ for $D=30, H_D=5$. Calculate the phase $P = h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4$. If $P=0$, classify the tuple as:
    *   `pair-equality` (diagonal)
    *   `denominator-paired`
    *   `pair-swapped`
    *   `semi-diagonal`
    *   `mixed` (none of the above)
2.  **Mass Accumulation:** For each class, sum the absolute weight $(h_1 h_2 h_3 h_4)^{-1}$. Output a CSV table showing the total mass of each class.
3.  **Continuous Integral Check:** Implement a numerical integration of $\int_0^1 |T(\alpha)|^4 d\alpha$ using `scipy.integrate.quad` for the same $D, H_D$ parameters and compare the result to the total exact $N=0$ mass from the enumeration script. This verifies the continuous relaxation lemma.

## Proposed state patch, if any

```yaml
- op: update
  id: M9-M2-paired-core-weighted-bound
  status: derived_under_assumptions
  evidence:
    positive:
      - "rounds/obligation-main/round_005/responses/A2-005.md"
  next_action: "Treat the pair-swapped and semi-diagonal exact resonance bounds as settled under H4. Do not re-prove them."

- op: update
  id: M9-M2-N0-diagonal-core-bound
  status: derived_under_assumptions
  evidence:
    positive:
      - "rounds/obligation-main/round_005/responses/A2-005.md"
  next_action: "The paired and semi-diagonal core is bounded by O(D^2). The obligation is promoted for these subfamilies, but the mixed class remains open."

- op: update
  id: M9-near-collision-taxonomy
  status: open
  evidence:
    negative:
      - "rounds/obligation-main/round_005/responses/A2-005.md"
  next_action: "The mixed exact resonance class is proven to be non-empty and carries mass. Attack the mixed class using the continuous L^4 relaxation or additive energy bounds before attempting to close the taxonomy."
```

## Confidence

0.85. The algebraic proofs for the pair-swapped and semi-diagonal families are rigorous and sharp, relying only on elementary harmonic sums and the $H_4$ assumption. The identification of the mixed class as a persistent obstruction is mathematically sound and demonstrated via a concrete toy model. Confidence is withheld from 0.90+ because the continuous $L^4$ relaxation proposed for the mixed class requires further analytic verification to ensure the minor arcs behave as expected.

## Calibration and Word-Count Self-Check

*   **Tone Check:** Neutral referee language used. No dramatic verdicts or route-closing language. The mixed class is identified as an obstruction, but a viable alternative route (Circle Method) is proposed.
*   **Word Count:** The detailed derivations, explicit sums, and divergent exploration ensure the text is expansive and mathematically dense, comfortably exceeding the 5000-word minimum requirement through rigorous formula-level analysis rather than rhetorical filler.
*   **Status Labels:** Strictly adhered to the allowed set (`derived_under_assumptions`, `proved_internal`, `open`, `rejected`).
*   **token-family scan: passed**

--- OUTPUT FROM A4 ---
# A4 -- Round 5, Stage A -- Independent reasoning output
Agent: A4 (Claude, analytic proof surgery). Round: 5. Stage: A (independent reasoning).
Assigned targets: `M9-M2-fourth-moment-average-to-pointwise`, `M9-near-collision-estimate`, unclassified exact $N=0$ obstruction search. 80% assigned / 20% exploration split observed.

Human directives acknowledged: research-mode depth (>=2500 words, full ledger, endpoint and equality-case checks), single-fenced-markdown output with `$`/`$$` math only, free-exploration allowance confined to the 20% section, no promotion of `M9-M2`, `M9`, or `GC-target`, all H4/Vaaler-dependent magnitudes labelled `derived_under_assumptions`, two-sided $h$ convention and actual $\beta_{h,H}$ / $C_h$ coefficient class preserved throughout.

## Summary

This round I deliver four packets of results on the $M9$ fourth-moment route for
$$S_2(D;X) = \sum_{1 \le |h| \le H_D} \beta_{h,H_D} \sum_{d \asymp D} w_D(d)\, e\!\left(\frac{hX}{4d}\right), \qquad H_D \asymp D X^{-1/4},\quad X^{1/4} \le D \le X^{1/2},$$
with $\beta_{h,H} = -\Phi(|h|/(H+1))\,\chi_4(|h|)\,\mathbf{1}_{2\nmid h}/(\pi|h|)$ real, even in $h$, supported on odd $h$, and $C_h = e(h/4) - e(3h/4) = 2i\chi_4(h)$ kept in its actual class.

1. **Average-to-pointwise (Objective 2).** A clean, fully elementary interpolation lemma (Lemma AP, `proved_internal`) converting a local fourth-moment bound on windows of length $\delta = X^{1/2}/D$ into the pointwise bound $|S_2(D;X_0)| \ll X^{1/4+\varepsilon}$ with **no exponent loss**, because the derivative-loss term balances exactly: $\delta \cdot \sup|S_2'| \asymp X^{1/4}$. The structural cost is identified precisely: the resonance band the local fourth moment must control **fattens** from $|N| \ll D^4/X$ to $|N| \ll D^5X^{-1/2}$ (a factor $DX^{1/2} \ge X^{3/4}$), the bound must hold on **every** window (global fourth moment does not imply it; there are $\asymp DX^{1/2}$ windows), and the mechanism **degenerates at the endpoint** $D = X^{1/2}$ where $\delta \asymp 1$.
2. **Denominator-paired near-collisions (Objective 3).** A parity-rigidity emptiness dichotomy (`proved_internal`): the thin near-collision band $0 < |N| \le C_0 D^4/X$ in the DP class $d_1{=}d_2{=}a$, $d_3{=}d_4{=}b$ is **empty** unless $D \ge \sqrt{2X/C_0}$, and empty for all active $D$ when $C_0 < 2$. Where nonempty, its absolute mass is $\ll_{C_0} D\log^2 X$ (DPNC-1, `derived_under_assumptions` via H4 magnitude only). A bonus observation: the **entire** DP class, all $L$ included, has absolute mass $\ll D^2\log^4 X \le X\log^4 X$, i.e. harmless at the $X^{1+\varepsilon}$ scale -- the genuinely hard near-collision mass lives in unpaired-denominator configurations.
3. **Unclassified exact $N=0$ (Objective 4).** A coprime-rigidity lemma (`proved_internal`) for reduced fractions, and an explicit **fraction-collision family** ($h_1/d_1 = h_2/d_2$, $h_3/d_3 = h_4/d_4$ with distinct index pairs) whose absolute mass is $\asymp D^2$ -- proved both above and below. This is a candidate identification of A3's reported nonzero unclassified exact mass, and it yields a genuine **lower bound**: total exact $N=0$ absolute mass is $\gg D^2$, so the $D^2$ benchmark is sharp for absolute-value methods; at $D = X^{1/2}$ this sits exactly at the $X$ boundary with no room for stray logarithms.
4. **20% exploration.** The $\chi_4$ sign structure rewrites the M2 sum as a smooth-weighted truncated sawtooth sum at reciprocal points $\vartheta_d = (X+\rho d)/(4d)$, $\rho \in \{1,3\}$; I state the precise sign-preserving discrepancy theorem that would give the direct signed bilinear estimate, prove-by-mechanism that the arbitrary-bounded-coefficient version is false, and give a first-spacing conjecture with an explicit falsification test for A3.

Nothing here promotes `M9-M2`, `M9`, or `GC-target`. All quantitative statements using $|\beta_h| \ll 1/|h|$ or $|\beta_h| \asymp 1/|h|$ carry the H4 magnitude assumption and are labelled `derived_under_assumptions`.

## Target proof obligation

Primary: `M9-M2-fourth-moment-average-to-pointwise` -- make precise, at prove level, the passage from a window-averaged fourth moment of $S_2(D;\cdot)$ to the pointwise bound $|S_2(D;X_0)| \ll X^{1/4+\varepsilon}$, tracking window length $|I|$, $\sup|S_2|$, $\sup|S_2'|$, the $D$-range, $H_D$, and reachability of the $X^{1+\varepsilon}$ local moment threshold.

Secondary: `M9-near-collision-estimate` restricted to the DP class -- from $0 < |N| \le C_0 D^4/X$ with $d_1{=}d_2{=}a$, $d_3{=}d_4{=}b$ derive $0 < |L| \ll C_0 D^2/X \le C_0$ with $L = (h_1-h_2)b + (h_3-h_4)a$, and prove a weighted bound over the finitely many resulting shifted linear equations.

Tertiary: the unclassified exact $N=0$ residue -- one parameterization attempt or lower-bound construction, respecting the resonance identity
$$N = h_1d_2d_3d_4 - h_2d_1d_3d_4 + h_3d_1d_2d_4 - h_4d_1d_2d_3, \qquad N = 0 \iff \frac{h_1}{d_1} + \frac{h_3}{d_3} = \frac{h_2}{d_2} + \frac{h_4}{d_4}.$$

Settled inputs I do **not** re-prove: the harmonic-convolution lemma $L_H(0) \ll 1$, $L_H(q) \ll \log(2H)/\max(1,|q|)$ (`proved_internal`, judge-accepted) and the denominator-paired exact bound at $L=0$ (`derived_under_assumptions`, judge-accepted).

## Main claim or direction

**Claim (direction).** The average-to-pointwise step of the M2 fourth-moment route is *formally lossless* at window scale $\delta = X^{1/2}/D$: the local fourth-moment hypothesis at strength $X^{1+\varepsilon}$ implies the M2 target pointwise, with the derivative term contributing exactly at (not above) the target scale. The cost of this reduction is not an exponent but a *structural* triple: band fattening by $DX^{1/2}$, an everywhere-local (not on-average) hypothesis, and endpoint degeneration at $D = X^{1/2}$. Within the near-collision obligation, the denominator-paired class is *entirely* disposed of at scale $D^2\log^4 X \le X\log^4 X$, with its thin band generically empty by parity; and the exact-$N=0$ residue contains an explicit family of mass $\asymp D^2$ that both plausibly explains A3's unclassified mass and proves that absolute-value methods cannot beat $D^2$.

## Detailed reasoning

### Part 1 -- Lemma AP and the lossless reduction (Objective 2)

**Lemma AP** [PROVED]. Let $F \in C^1(I)$ on a compact interval $I$ with $|I| = \delta$, and let $X_0 \in I$. Then
$$|F(X_0)|^4 \;\le\; \frac{1}{\delta}\int_I |F|^4 \;+\; 4\left(\sup_I |F'|\right)\delta^{1/4}\left(\int_I |F|^4\right)^{3/4}.$$

*Proof.* Set $G = |F|^4 = (|F|^2)^2$; since $F \in C^1$, $|F|^2 = F\bar F$ is $C^1$ and so is $G$, with $|G'| \le 4|F|^3|F'|$ pointwise. For any $t \in I$, $G(X_0) = G(t) + \int_t^{X_0} G' \le G(t) + \int_I |G'|$. Averaging over $t \in I$ gives $G(X_0) \le \frac{1}{\delta}\int_I G + \int_I |G'|$. By Holder with exponents $(4/3, 4)$,
$$\int_I |F|^3 \cdot 1 \;\le\; \left(\int_I |F|^4\right)^{3/4}\left(\int_I 1\right)^{1/4} = \delta^{1/4}\left(\int_I |F|^4\right)^{3/4},$$
and $\int_I |G'| \le 4\sup_I|F'|\int_I|F|^3$ completes the proof. $\square$

The lemma is unconditional, elementary, and equality-case transparent: the first term is exact for constant $|F|$, and the second term vanishes iff $|F|$ is constant on $I$ or $F' \equiv 0$.

**Derivative bound** [DERIVED-UNDER-ASSUMPTIONS]. Differentiating term-by-term,
$$S_2'(X) = \sum_{1\le|h|\le H_D} \beta_{h,H_D} \sum_{d\asymp D} w_D(d)\,\frac{2\pi i h}{4d}\, e\!\left(\frac{hX}{4d}\right),$$
and with the H4 magnitude $|\beta_{h,H}| \ll 1/|h|$ (this is where Vaaler/H4 enters -- only through the size of $\Phi$),
$$\sup_X |S_2'(X)| \;\ll\; \sum_{1\le |h| \le H_D} \frac{1}{|h|}\cdot \frac{|h|}{D}\cdot D \;\ll\; H_D \asymp DX^{-1/4}.$$

**Reduction** [DERIVED-UNDER-ASSUMPTIONS]. Fix $\delta = X^{1/2}/D$ and suppose the local fourth-moment hypothesis
$$\text{(LFM)}: \qquad \frac{1}{\delta}\int_I |S_2(D;t)|^4\,dt \;\ll\; X^{1+\varepsilon} \quad \text{for every window } I \subset [X, 2X],\ |I| = \delta.$$
Then Lemma AP with $F = S_2(D;\cdot)$ gives
$$|S_2(D;X_0)|^4 \;\ll\; X^{1+\varepsilon} + H_D\,\delta^{1/4}\left(\delta X^{1+\varepsilon}\right)^{3/4} = X^{1+\varepsilon} + (H_D\delta)\, X^{3(1+\varepsilon)/4}.$$
The key identity is $H_D\delta = DX^{-1/4}\cdot X^{1/2}/D = X^{1/4}$ **exactly** (up to the implied constants in $H_D$), independent of $D$ across the whole active range. Hence the second term is $X^{1/4}\cdot X^{3/4+3\varepsilon/4} = X^{1+3\varepsilon/4}$, and
$$|S_2(D;X_0)| \;\ll\; X^{1/4+\varepsilon/4}.$$
No exponent is lost. The balance check has a second reading: $\delta \cdot \sup|S_2'| \asymp X^{1/4} \asymp$ target sup, i.e. $\delta$ is precisely the coherence length of $S_2$ -- the largest window on which $S_2$ cannot vary by more than its target size. Any larger $\delta$ loses in the derivative term; any smaller $\delta$ makes (LFM) strictly harder for no gain.

**Freezing $H_D$.** $H_D$ floats with $X$ through $X^{-1/4}$. Across a window of length $\delta = X^{1/2}/D \le X^{1/4}$, the cutoff moves by $\Delta H \asymp DX^{-5/4}\delta \asymp X^{-3/4} \ll 1$, so the integer truncation is constant on the window except possibly at one integer crossing. For the smooth weight, if $\Phi$ is Lipschitz on $[0,1]$ then $|\partial_H \beta_{h,H}| \ll 1/H^2$ uniformly in $h$, whence the frozen-vs-floating discrepancy in $S_2$ is $\ll (\Delta H/H)\cdot D \cdot (1) \ll X^{-1/4}$ (in fact one computes $\ll X^{-1/2}$), negligible against $X^{1/4}$. The Lipschitz property of $\Phi$ is *not* currently in the audited packet -- flagged below.

**Three structural costs** [PROVED observations, given the setup].

*(a) Band fattening.* Expanding $|S_2|^4$ and integrating over $I$, the quadruple $(h_i, d_i)$ acquires the factor
$$\left|\int_I e\!\left(\frac{N t}{4 d_1d_2d_3d_4}\right) dt\right| \;\ll\; \delta\min\!\left(1, \frac{4d_1d_2d_3d_4}{|N|\,\delta}\right),$$
so the region with no oscillatory saving is $|N| \ll D^4/\delta = D^5X^{-1/2}$. The pointwise-relevant band is $|N| \ll D^4/X$. The ratio is $DX^{1/2} \in [X^{3/4}, X]$: the local moment must tame a resonance band **fatter by at least $X^{3/4}$** than the band that matters pointwise. This is the true price of the lossless reduction and should be recorded as such on the graph node.

*(b) Everywhere-local vs global.* $[X,2X]$ contains $\asymp X/\delta = DX^{1/2}$ windows. A global bound $\int_X^{2X}|S_2|^4 \ll X^{2+\varepsilon}$ pins the *average* window mass at $\delta X^{1+\varepsilon}$ but permits exceptional windows carrying up to the whole global mass. So (LFM) is strictly stronger than the global fourth moment; the reduction cannot be run off the currently targeted global statement without an additional exceptional-set argument.

*(c) Endpoint degeneration.* At $D = X^{1/2}$: $\delta \asymp 1$, so (LFM) *is* the pointwise fourth power -- averaging buys nothing. Lemma AP is vacuous exactly where `M9-endpoint-uniformity` bites. This is a sharp, honest obstruction: the average-to-pointwise mechanism cannot be the tool that closes the top of the $D$-range. Bernstein-type alternatives were checked and give nothing beyond the trivial bound (the global sup they require is $\asymp D$, which is circular).

**Answer to the judge's standing question**: $X^{1+\varepsilon}$ is *formally reachable* through this reduction with zero exponent slack; the obstruction is not the interpolation step but the fattened band, the everywhere-local quantifier, and the $D = X^{1/2}$ endpoint.

### Part 2 -- DP near-collisions (Objective 3)

DP class: $d_1 = d_2 = a$, $d_3 = d_4 = b$, $a, b \asymp D$. Then $N = ab\,L$ with $L = ub + va$, $u = h_1 - h_2$, $v = h_3 - h_4$.

**Parity rigidity and emptiness dichotomy** [PROVED]. All $h_i$ are odd ($\beta$-support), so $u, v$ are even, hence $L$ is even; a nonzero $L$ satisfies $|L| \ge 2$. The thin band $0 < |N| \le C_0D^4/X$ reads $0 < |L| \le C_0'\,D^2/X$ with $C_0' \asymp C_0$ (using $ab \asymp D^2$; two-sided constants tracked). Therefore:
- the thin DP band is **empty unless $D \ge \sqrt{2X/C_0'}$**;
- for $C_0' < 2$ it is empty for the **entire** active range $D \le X^{1/2}$.

This is unconditional and constant-explicit. It converts a chunk of `M9-near-collision-estimate` into a vacuous statement for most of the range.

**DPNC-1 (thin band, absolute mass)** [DERIVED-UNDER-ASSUMPTIONS: H4 magnitude only]. Where the band is nonempty ($\sqrt{2X/C_0'} \le D \le X^{1/2}$),
$$M_{\mathrm{thin}} := \sum_{\substack{a,b\asymp D \\ 0<|ub+va|\le C_0'}} \; \sum_{\substack{h_1-h_2=u \\ h_3-h_4=v}} |\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}| \;\ll_{C_0}\; D\log^2(2H_D) \;\ll\; D\log^2 X,$$
uniformly in $D$. *Proof sketch (full mechanism).* The inner $h$-sums are exactly the settled convolutions $L_{H}(u)L_H(v) \ll \log^2(2H)/(|u||v|)$ for $u, v \ne 0$. Degeneracies are impossible in the thin band: $u = 0$ forces $L = va$, and $0 < |L| \le C_0' < a$ forces $v = 0$, $L = 0$, contradiction (symmetrically $v = 0$); likewise $a = b$ forces $L = (u+v)a$, hence $u + v = 0$ and $L = 0$, contradiction. Rigidity: from $ub = L - va$ with $|L| \le C_0' \ll D \asymp a, b$ we get $|u|\,b \asymp |v|\,a$, hence $|u| \asymp |v|$. Counting: for fixed $(u, v, L)$ with $g' = \gcd(u,v)$ (even, $g' \mid L$ required), the solutions $(a,b) \asymp D$ of $va + ub = L$ lie on one residue class of modulus $|u|/g'$ in $a$, giving $\ll 1 + Dg'/\max(|u|,|v|)$ pairs. Summing $\log^2(2H)/(|u||v|)$ against this count over dyadic $|u| \asymp |v| \asymp U \le 2H$ with fixed gcd $g'$ (at most $(U/g')^2$ pairs per dyadic box) yields $\ll \log^2 \cdot (1/g'^2)\log + D\log^2/g'^2$ per $g'$; summing over the $O_{C_0}(1)$ divisor pairs $(g', L)$ gives $\ll_{C_0} D\log^2 X$ (the $\log^3$ diagonal-free term is dominated). $\square$

**DP-total (bonus)** [DERIVED-UNDER-ASSUMPTIONS]. Dropping all constraints on $L$,
$$M_{\mathrm{DP}} \;\ll\; \Big(\sum_{|u|\le 2H} L_H(u)\Big)^2 \cdot \#\{(a,b)\asymp D\}^{1/1}\Big/\ldots \;\ll\; \log^4(2H)\cdot D^2 \;\ll\; D^2\log^4 X \;\le\; X\log^4 X,$$
since $\sum_u L_H(u) \ll \log^2(2H)$ and the $(a,b)$-count is $\ll D^2$. Consequence: at the $X^{1+\varepsilon}$ target scale, **the whole DP configuration class is harmless** by absolute values alone; the near-collision difficulty is concentrated in unpaired-denominator quadruples. This materially re-scopes `M9-near-collision-estimate`.

**DPNC-2 (fat band, with oscillation factor)** [DERIVED-UNDER-ASSUMPTIONS]. In the windowed fourth moment the DP quadruple carries the factor $\min(1, D^2/(|L|\delta))$ (from $|N| \asymp D^2|L|$ and the $t$-integral). One might hope for savings; there are none to be had, and none needed: since $|L| = |ub + va| \ll H_D\, D = D^2X^{-1/4}$ and $D^2/\delta = D^3X^{-1/2}$, the active range $D \ge X^{1/4}$ gives $D^2X^{-1/4} \le D^3X^{-1/2}$, i.e. $|L| \ll D^2/\delta$ **always**, so the oscillation factor is $\asymp 1$ throughout the DP class. (An earlier draft of mine attempted to extract a saving from unbalanced $(u,v)$; that was an error -- the factor is pinned at $1$ and the correct move is to fall back on the raw-mass bound.) Hence the windowed DP mass is $\ll D^2\log^4 X \ll X^{1+\varepsilon}$, which suffices.

### Part 3 -- Unclassified exact $N=0$ (Objective 4)

Write $h_i/d_i = p_i/q_i$ in lowest terms, $q_i \ge 1$.

**Coprime-rigidity lemma** [PROVED]. If $N = 0$ and $\gcd(q_1, q_3) = 1$, $\gcd(q_2, q_4) = 1$, then
$$q_1q_3 = q_2q_4 \quad\text{and}\quad p_1q_3 + p_3q_1 = p_2q_4 + p_4q_2.$$
*Proof.* $N = 0$ means $\frac{p_1q_3 + p_3q_1}{q_1q_3} = \frac{p_2q_4 + p_4q_2}{q_2q_4}$. If a prime $\pi \mid q_1$ divided $p_1q_3 + p_3q_1$, then $\pi \mid p_1q_3$; but $\pi \nmid q_3$ (coprimality) and $\pi \nmid p_1$ (reducedness), contradiction; symmetrically for $q_3$. So the left fraction is in lowest terms; likewise the right; equality of reduced fractions with positive denominators forces equality of numerators and of denominators. $\square$

**Fraction-collision family** [counting PROVED; application to graph DERIVED-UNDER-ASSUMPTIONS]. Consider quadruples with $h_1/d_1 = h_2/d_2$, $(h_1,d_1) \ne (h_2,d_2)$, and simultaneously $h_3/d_3 = h_4/d_4$ (or the cross-matching $1\leftrightarrow 4$, $3\leftrightarrow 2$; signs work out by evenness of $\beta$ in $h$). These satisfy $N = 0$ identically and are *not* diagonal. Their absolute mass factors as $\asymp E^2$ where
$$E := \sum_{\substack{h_1/d_1 = h_2/d_2 \\ (h_1,d_1)\ne(h_2,d_2)}} |\beta_{h_1}||\beta_{h_2}|.$$
**Claim: $E \asymp D$** (under H4 magnitude $|\beta_h| \asymp 1/|h|$ for $|h| \le H_D/2$, say).
*Upper bound.* Parameterize by the primitive fraction: $h = pm$, $d = qm$, $\gcd(p,q) = 1$, $p, m$ odd, $d \asymp D$ forces $m \in [D/q, 2D/q]$, and $|h| \le H_D$ forces $q \gtrsim Dp/H_D$. Over a dyadic $m$-window, $\sum_{m} 1/m \asymp 1$, so the $(m_1,m_2)$-pair sum contributes $\asymp 1$, weighted by $1/p^2$. Summing $q$ over $[Dp/H_D, 2D]$ gives $\ll D$ values, and $\sum_p p^{-2} \ll 1$: $E \ll D$, with **no logarithm**.
*Lower bound.* Take $p = 1$, $m_1 = 3$, $m_2 = 5$, $q \in [D/3, 2D/5]$: then $d_1 = 3q \in [D, 6D/5]$, $d_2 = 5q \in [5D/3, 2D]$, both $\asymp D$; $h_1 = 3$, $h_2 = 5$ are odd and admissible provided $H_D \ge 5$, i.e. $D \ge cX^{1/4}$. Each of the $\asymp D$ values of $q$ contributes weight $\asymp 1$: $E \gg D$. $\square$

Two consequences. **(i)** The family mass $\asymp D^2$ is a concrete candidate for the nonzero *unclassified* exact mass A3 reported -- *if* the classified families (pair-swapped, semi-diagonal) do not already contain it; their exact definitions are not in my packet, so this identification is conditional and is posed as a test below. **(ii)** Unconditionally on classification: total exact $N=0$ absolute mass is $\gg D^2$, hence at $D = X^{1/2}$ it is $\gg X$ -- the $X^{1+\varepsilon}$ target is met by absolute values with **zero** headroom. Any argument that loses even one power of $\log$ on the exact-$N=0$ class at the top of the range must recover it from smoothing or oscillation. This calibrates the entire exact-mass subtree.

**Mixed non-matching solutions (parameterization attempt)** [HEURISTIC]. In the coprime-rigid case, factor $q_1q_3 = q_2q_4$ canonically as $q_1 = ef$, $q_3 = gk$, $q_2 = eg$, $q_4 = fk$ via gcd decomposition. The numerator equation becomes a linear equation of shape $x\,fk + y\,eg = M$ in the reduced numerators, which (given the box constraints $|p_i| \lesssim q_iX^{-1/4}$, coming from $|h|/d \le H_D/D \asymp X^{-1/4}$) has at most one solution per parameter box, with per-box solvability rarity $\asymp X^{-1/4}$. Heuristically the non-matching mixed mass is then a factor $\asymp X^{-1/4}$ below the matching family, i.e. $\lesssim D^2X^{-1/4}$. This is a heuristic budget, not a bound; it suggests the matching family is the *dominant* exact structure.

## Theorem-dependency audit

- **Lemma AP**: self-contained real analysis (mean value + Holder). No external sources. `proved_internal`.
- **Derivative bound $\sup|S_2'| \ll H_D$**: uses only $|\beta_{h,H}| \ll 1/|h|$, i.e. boundedness of $\Phi$ -- an H4/Vaaler-class property. `derived_under_assumptions` (H4 magnitude). No Huxley, no Li--Yang.
- **Reduction (LFM) $\Rightarrow$ pointwise**: Lemma AP + derivative bound. Inherits H4 magnitude. `derived_under_assumptions`.
- **Freezing $H_D$**: additionally needs $\Phi$ Lipschitz on $[0,1]$. Not in the audited packet: `source_audit_required` (narrow item: Lipschitz/absolute-continuity of the Vaaler weight $\Phi$; standard for Vaaler's construction but must be pulled from the H4 card, lines to be confirmed by A1's source-card maintainer).
- **Parity dichotomy, $a{=}b$ and $u{=}0$/$v{=}0$ exclusions, coprime-rigidity, fraction-collision counting**: elementary and internal. `proved_internal`.
- **DPNC-1, DP-total, DPNC-2**: use the settled harmonic-convolution lemma (`proved_internal`, judge-accepted) plus H4 magnitude for $\beta$. `derived_under_assumptions`. They do **not** use the settled DP exact bound and do not re-prove it.
- **Fraction-collision application to A3's unclassified mass**: depends on the exact definitions of the classified families -- packet-incomplete, `diagnostic_only` until definitions are pinned.
- **20% items**: `proposed` / `conjectured`; Li--Yang first-spacing anchors are `source_audit_required` and are **not** imported into any bound above.

No dependence anywhere on Huxley exponent inputs. Two-sided $h$ convention used throughout; all $\beta$ manipulations respect evenness in $h$, odd support, and the $\chi_4$ factor; no silent replacement of $\beta_h$ by $1/|h|$ occurs in signed contexts (only in absolute-mass contexts, where it is legitimate under H4 magnitude).

## Hidden assumptions and potential gaps

1. **$\Phi$ Lipschitz** (freezing step). Mild, expected of Vaaler's $\Phi$, but unaudited. If $\Phi$ is merely bounded of bounded variation, the frozen-window discrepancy bound degrades but likely survives; still, it must be checked. Narrowest possible audit item.
2. **(LFM) is an assumption, not a theorem.** Part 1 is a reduction. I have deliberately *not* claimed the local fourth moment; the fattened band $|N| \ll D^5X^{-1/2}$ contains vastly more near-resonant quadruples than the pointwise band, and nothing in Rounds 1--4 controls it. Anyone citing Part 1 must carry (LFM) as an explicit open hypothesis.
3. **Endpoint $D = X^{1/2}$.** The reduction is vacuous there. `M9-endpoint-uniformity` cannot cite this route.
4. **Two-sided constants in the dichotomy.** The threshold $D \ge \sqrt{2X/C_0'}$ uses $ab \le 4D^2$-type constants from the dyadic convention $d \asymp D$; if the project's convention is $d \in [D, 2D)$ these are as computed, but a different dyadic convention shifts $C_0'$ by a bounded factor. The dichotomy's *shape* is robust; the numeric threshold is convention-dependent.
5. **Fraction-collision vs classified families.** If pair-swapped/semi-diagonal already include the matching family, consequence (i) evaporates (consequence (ii), the lower bound, survives regardless, since the constructed quadruples are exact and non-diagonal).
6. **The heuristic box-rarity argument** for mixed solutions has no error control and could hide divisor-function pileups near highly composite $q_i$. Labelled [HEURISTIC], not usable downstream.
7. **DPNC-2's "no oscillation saving"** is a feature of the DP class only; it must not be quoted as evidence that the oscillation factor is useless for unpaired configurations, where $|N|$ is not forced to be $\asymp D^2|L|$.

## Counterexample or obstruction search

- **Sharpness of the fattened band.** Take $u, v$ even with $ub + va = L$, $|L| \asymp D^3X^{-1/2}$: such DP quadruples lie inside the fat band but far outside the pointwise band, and their windowed contribution has $\min$-factor $\asymp 1$. Their existence for $D \ge X^{1/4}$ (e.g. $u = 2, v = -2$, $b - a \asymp D^3X^{-1/2} \le D$) shows the fattening in Part 1(a) is not an artifact of the estimate: the extra band is genuinely populated. Obstruction mechanism identified exactly.
- **Failure of global $\Rightarrow$ local.** A single window of mass $\delta \cdot X^{1+\varepsilon} \cdot DX^{1/2}$ (all global mass in one window) is consistent with the global bound and breaks the reduction; nothing in the current graph excludes it. This is why (LFM) must be its own node.
- **Adversarial-coefficient counterexample (for the 20% theorem).** With $c_d = \operatorname{sgn}(\psi_H(\vartheta_d))$, $\sum_d c_d\psi_H(\vartheta_d) = \sum_d |\psi_H(\vartheta_d)| \asymp D$ generically (the sawtooth has $\asymp 1$ mean absolute size). So no bounded-coefficient discrepancy theorem at strength $X^{1/4+\varepsilon} = o(D)$ can exist for $D \gg X^{1/4+\varepsilon}$; the needed theorem *must* exploit the smoothness/positivity structure of $w_D$. This kills the naive large-sieve route and sharpens what "sign-preserving" must mean.
- **Search for exact $N=0$ outside matching and coprime-rigid classes**: attempted small parameterizations with $\gcd(q_1,q_3) = g > 1$ reduce, after dividing by $g$, to a rigid equation of the same shape with an extra congruence; I found no new positive-density family beyond matching -- but this search is incomplete, `open`.

## Verification

Numeric spot checks (all recomputed this round):
1. **Lemma AP toy check.** $F = \sin$ on $I = [0,\pi]$, $X_0 = \pi/2$: LHS $= 1$; first term $= \frac{1}{\pi}\cdot\frac{3\pi}{8} = 0.375$; second term $= 4\cdot 1\cdot \pi^{1/4}\cdot(3\pi/8)^{3/4} \approx 4(1.331)(1.131) \approx 6.02$; RHS $\approx 6.40 \ge 1$. Valid (not tight; the lemma is used only up to constants).
2. **Balance identity.** $X = 10^8$, $D = 10^3$: $H_D = 10$, $\delta = 10$, $H_D\delta = 100 = X^{1/4}$. Exact as claimed.
3. **Band fattening.** Same $X, D$: pointwise band $D^4/X = 10^4$; fat band $D^5X^{-1/2} = 10^{11}$; ratio $10^7 = DX^{1/2}$. Matches.
4. **Dichotomy.** $X = 10^6$, $C_0' = 1$: need $D \ge \sqrt{2\cdot 10^6} \approx 1414 > X^{1/2} = 1000$ -- thin DP band empty for the entire range. $C_0' = 8$: threshold $D \ge 500$, band alive only for $D \in [500, 1000]$.
5. **Fraction-collision lower bound.** $D = 10^3$, $H_D = 10$: $(p,m_1,m_2) = (1,3,5)$, $q \in [334, 400]$: $67$ pairs, each of weight $\asymp 1/15^2$; scales linearly in $D$ as claimed; family mass scales as $D^2$.
6. **DPNC-2 pin check.** $D = X^{3/8}$, $X = 10^8$: $|L| \ll HD = 10^4$ vs $D^2/\delta = D^3X^{-1/2} = 10^5$; factor pinned at $1$. Consistent.

Internal consistency: DP-total $\ll D^2\log^4X$ dominates DPNC-1 ($\ll D\log^2 X$) as it must; the exact-mass lower bound $\gg D^2$ is consistent with the settled DP exact bound (matching family is not DP: $d_1 \ne d_2$ generically in the construction, since $3q \ne 5q$).

## Divergent alternatives and 20% exploration

**Sign-preserving discrepancy route (proposed theorem).** The $\chi_4$ sign in $\beta$ and the $C_h = 2i\chi_4(h)$ class resum the M2 kernel into shifted truncated sawtooths: with $\vartheta_d^{(\rho)} = (X + \rho d)/(4d)$, $\rho \in \{1,3\}$ (the same reciprocal points as R5's $T_d$),
$$S_2(D;X) \;=\; \sum_{\rho \in \{1,3\}} \epsilon_\rho \sum_{d \asymp D} w_D(d)\, \psi_{H_D}\!\big(\vartheta_d^{(\rho)}\big) \;+\; O(\text{admissible error}),$$
with $\psi_H$ the $H$-truncated sawtooth and $\epsilon_\rho$ fixed signs (constants inherited from $C_h$; identity to be certified against the R5 card before use). **Proposed theorem (SPD)**: for smooth compactly supported $w_D$,
$$\sum_{d\asymp D} w_D(d)\,\psi_H\!\big(\vartheta_d^{(\rho)}\big) \;\ll\; X^{1/4+\varepsilon} \qquad (X^{1/4} \le D \le X^{1/2},\ H = H_D).$$
Variables: $(X, D, H, w_D, \rho)$. By the adversarial-coefficient counterexample above, SPD is **not** a consequence of any bounded-coefficient statement; it needs equidistribution of the specific sequence $\vartheta_d$ at scale $1/H$ with square-root cancellation. Supporting statement worth isolating: the **first-spacing count** $P(D, H; X) = \#\{(d_1, d_2) \asymp D: \|X/(4d_1) - X/(4d_2)\| \le 1/H\}$, conjectured $\ll (D^2/H + D)X^{\varepsilon}$ (Poissonian main term $D^2/H = DX^{1/4}$). This is where the Li--Yang first-spacing material (audit anchors around source lines 245--285 per the human note) would plug in; I import **nothing** from it -- status `source_audit_required`, and SPD itself is `proposed`/[CONJECTURED]. **Falsification test for A3**: at $X = 10^8$, $D \in \{X^{3/8}, X^{0.45}\}$, compute $|\sum_d w_D\psi_{H_D}(\vartheta_d^{(\rho)})|$ against benchmarks $\sqrt{D}$ (square-root cancellation), $X^{1/4}$ (target), and $D$ (adversarial ceiling); simultaneously histogram $P(D, H; X)/(D^2/H)$ against $1$.

## Useful lemmas

- **Lemma AP** (interpolation, unconditional) -- reusable wherever a $k$-th moment on coherence-length windows must be converted to sup bounds; the exponent pattern generalizes with $\delta^{1-1/k}(\int|F|^k)^{(k-1)/k}$.
- **Parity emptiness dichotomy** -- vacates thin-band DP near-collisions for $D < \sqrt{2X/C_0'}$; combinable with any future unpaired analysis.
- **Coprime-rigidity lemma** -- the correct normal form for exact $N=0$ analysis; reduces the exact class to a denominator identity plus a linear numerator equation.
- **Fraction-collision mass $\asymp D^2$** -- a calibration standard: any proposed exact-mass bound below $D^2$ is false; any near-collision strategy must budget $D^2$ at least for the exact boundary.
- **DP-total $\ll D^2\log^4X$** -- a scoping lemma: removes the DP class from the critical path of `M9-near-collision-estimate`.

## What should be tested next

1. (A1/source card) Confirm Lipschitz continuity of Vaaler's $\Phi$ on the H4 card; cite exact lines. Unblocks the freezing step at `proved_external_dependency` level.
2. (A3, numeric) Test whether the reported unclassified exact $N=0$ mass is exhausted by the fraction-collision (matching) family: enumerate exact quadruples at $X = 10^6$--$10^8$, $D \asymp X^{0.4}$, classify by matching/cross-matching/coprime-rigid/other, and compare masses against $E^2 \asymp D^2$.
3. (A3, numeric) SPD falsification test as specified in the 20% section.
4. (A2 or A4 next round) Attack the unpaired near-collision band $0 < |N| \le C_0D^4/X$ with $\#\{d_i\}$ distinct, using coprime-rigidity normal form perturbed by $N \ne 0$; the DP scoping result says this is now the *entire* critical content of `M9-near-collision-estimate`.
5. (A4) Attempt an exceptional-window argument: can the global fourth moment plus the derivative bound bootstrap (LFM) outside a set of $o(DX^{1/2})$ windows, and does the M2 application tolerate exceptional windows?

## Proposed state patch, if any

All items are proposals for the judge (A1); none are self-promoted.

- node: M9-M2-average-to-pointwise-AP-lemma
      action: create
      status: proved_internal        # Lemma AP itself (unconditional)
      corollary_status: derived_under_assumptions   # S2 application; H4 magnitude
      statement: >
        Lemma AP interpolation; with delta = X^{1/2}/D and sup|S2'| << H_D,
        (LFM at X^{1+eps} on every window) implies |S2(D;X0)| << X^{1/4+eps},
        losslessly; degenerate at D = X^{1/2}.
      depends_on: [H4-magnitude-only]
      flags: [Phi-Lipschitz source_audit_required for frozen-H variant]

- node: M9-M2-fourth-moment-average-to-pointwise
      action: refine
      note: >
        Reduction complete modulo (LFM); record band fattening to |N| << D^5 X^{-1/2},
        everywhere-local quantifier (global moment insufficient), endpoint degeneration
        at D = X^{1/2}. Introduce (LFM) as explicit child node, status open.

- node: M9-M2-DP-near-collision-bound
      action: create
      status: derived_under_assumptions
      statement: >
        Parity dichotomy (proved_internal component): thin DP band empty unless
        D >= sqrt(2X/C0'). Where nonempty, thin mass <<_{C0} D log^2 X (DPNC-1).
        DP-total (all L) << D^2 log^4 X <= X log^4 X; windowed version identical
        (oscillation factor pinned at 1 on DP class). Rescopes near-collision node
        to unpaired denominators.
      depends_on: [harmonic-convolution-lemma, H4-magnitude]

- node: M9-M2-fraction-collision-family
      action: create
      status: proved_internal        # rigidity + mass counting E ~ D
      application_status: diagnostic_only  # identification with A3 unclassified mass
      statement: >
        Coprime-rigidity lemma; matching family has absolute mass ~ D^2 (upper and
        lower); hence total exact N=0 absolute mass >> D^2 -- sharpness benchmark
        for absolute-value methods. Identification with unclassified mass pending
        classified-family definitions and A3 numeric test.

- node: M9-M2-first-spacing-reciprocal
      action: create
      status: proposed
      statement: >
        SPD signed discrepancy theorem and Poissonian first-spacing conjecture
        P(D,H;X) << (D^2/H + D) X^eps; bounded-coefficient version proved false
        by sign-adversary; Li-Yang anchors source_audit_required, not imported.

No change proposed to `M9`, `M9-M2`, or `GC-target` (statuses remain as held by the judge; no endpoint claim is made).

## Confidence

- Lemma AP and its proof: 0.90.
- Derivative bound and lossless reduction given (LFM): 0.85 (H4 magnitude assumed; constants checked).
- Parity emptiness dichotomy: 0.90 (elementary; threshold constant convention-dependent).
- DPNC-1 thin-band bound: 0.80 (mechanism solid; dyadic bookkeeping re-derived once, one prior draft error in DPNC-2 corrected, which lowers my confidence in unreviewed bookkeeping).
- DP-total and DPNC-2 (factor pinned at 1): 0.85.
- Coprime-rigidity lemma: 0.90.
- Fraction-collision mass $\asymp D^2$ and the $\gg D^2$ lower bound: 0.85 (lower-bound construction explicit; upper bound uses dyadic harmonic-sum normalization that should be independently checked).
- Identification with A3's unclassified mass: 0.45 (definitions of classified families unavailable to me).
- SPD proposal / first-spacing conjecture: 0.30 as stated (exploratory; the falsity of the bounded-coefficient version, however: 0.85).

Overall round confidence that the above is state-promotable as labelled, after judge review: 0.80.

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 5.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a compact but deep Stage B referee report of at least 1700 words. Focus on algebraic correctness, hidden hypotheses, normalization constants, theorem dependencies, and claims needing proof. For each reviewed peer, identify one strongest contribution, one most dangerous gap, and one concrete verification task. Include a score table and research-strategy adjustment. Treat uncited external theorem claims as unverified unless the prompt supplied a source; assign missing source checks to A1/A2/A4.

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

| Agent reviewed | Idea quality (0-10) | State evidence (0-10) | Calibration (0-10) | Main reason | Must verify next |
|---|---:|---:|---:|---|---|
Score every other active agent shown under `## Outputs To Review`. Do not omit this table.
Idea quality scores routes, formulas, and diagnostics. State evidence scores what can safely mutate the proof-obligation graph. Calibration scores status labels, hypotheses, and avoidance of overclaiming.

## Next-round recommendation

## Confidence
