You are A3 Deepseek V4 Pro, acting as API-based proof auditor, algebra checker, diagnostic script/result reviewer, and stress-test planner.

Review the other agents' Round 9 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Check algebraic reductions, Poisson/Bessel normalizations, hyperbola decompositions, endpoint conventions, Vaaler/Fejer residuals, Li-Yang/Bombieri-Iwaniec compatibility claims, Mellin-Perron alternatives, and claimed obstructions. Prefer precise parameter ranges and falsifiable lemmas over broad summaries. In reasoning, reserve about 20% of the answer for divergent alternatives or obstruction searches. In review, recommend research-strategy adjustments based on which claims survive verification. For computation-track obligations, treat A2/AI Studio as the primary external Python runner and yourself as the script/result auditor unless the prompt supplies a real execution tool and runtime output. Do not substitute surrogate phases or random coefficient models as state evidence. Use the actual formulas, actual alpha_h/beta_h/C_h coefficients, and the physical bivariate phase e(hX/(4d)); if a toy surrogate is included, label it as toy evidence and do not use it for status changes. If no committed script, exact command, table, and report are produced, say the computation was not executed. If you cannot physically write files through the API, output an `## Artifact bundle` with repository-relative file paths, complete script contents, exact commands, expected table schemas, precision/log fields, and a short report template so A2, the local orchestrator, or Codex can materialize and run them. When reviewing A2 diagnostic output, audit the code, exact arithmetic, parameters, stdout/tables, pass/fail interpretation, and whether Codex/local reproduction is still required. When a proof step is plausible but not certified, say exactly which formula, theorem hypothesis, citation, or numerical check would certify it.



## Active Agents For This Run

Only these agents are active in this run:

- `A1` (ChatGPT Extended Pro): broad strategist, literature scout, proof synthesizer, and default judge
- `A2` (Gemini Pro Deep Think): independent alternative strategist, obstruction finder, referee-style reviewer, and AI Studio Code Execution runner for small diagnostics
- `A3` (A3 Deepseek V4 Pro): API-based proof auditor, algebra checker, diagnostic script/result reviewer, and stress-test planner
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

### Diagnostic Execution Rule

Computation remains `diagnostic_only`; it cannot prove a theorem or promote a lemma by itself.

For future M9 rounds, the default diagnostic split is:

- `A2` runs small self-contained Python diagnostics in Google AI Studio only when Code Execution is enabled and the tool returns actual output.
- `A2` must include the exact Python code, stdout/stderr or returned tables, parameter choices, pass/fail criteria, and limitations. If Code Execution is unavailable or no tool output is returned, A2 must mark the diagnostic as `not_executed`.
- Codex or the local workflow must reproduce any A2 Code Execution result in the repository before it can be attached as positive diagnostic evidence in `state/proof_obligations.yml`.
- `A3` reviews the formulas, script logic, exact arithmetic choices, and interpretation of A2/Codex diagnostic outputs. If A3 lacks real execution output, it must not claim that code was run.

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

## Diagnostic Execution Contract

Computation remains `diagnostic_only`; it cannot prove a theorem or promote a lemma by itself.

- A2 is the primary external Python diagnostic runner when Google AI Studio Code Execution is enabled.
- A2 may run only small self-contained Python diagnostics and must report exact code, stdout/stderr or returned tables, parameters, pass/fail criteria, and limitations.
- If Code Execution is unavailable or returns no runtime output, A2 must mark the job `not_executed` and provide only a runnable artifact bundle.
- Codex or the local workflow must reproduce any A2 Code Execution result inside this repository before it counts as positive diagnostic evidence.
- A3 audits diagnostic formulas, script logic, exact arithmetic, and result interpretation. A3 must not claim execution unless real runtime output is present.

## Review-Stage Guardrail

This is Stage B cross review for Round 9.

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
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/responses/A1-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_006/responses/A1-006.md",
          "rounds/obligation-main/round_007/responses/A1-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_008/responses/A1-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ]
      },
      "owner": "A1",
      "next_action": "Finalize sources/vaaler_1985.md with DOI, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, beta lower envelope, and M2 parity support.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
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
        "M9-M2-fourth-moment-average-to-pointwise",
        "M9-M2-local-fourth-moment-LFM"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/responses/A1-005.md",
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/responses/A3-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "Do not promote from AP, DP scoping, or paired/fraction subfamilies. Supply a pointwise M2 estimate, a local fourth-moment estimate valid at endpoint, or a sign-preserving direct estimate with uniformity.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_002/responses/A1-002.md",
          "rounds/obligation-main/round_008/responses/A4-008.md"
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
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use the signed lift-cancellation B1 lemma and c_chi target to preserve the chi_4(h) structure in upper-range near-collision analysis. Do not use character-blind absolute norms past D=X^(3/8).",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
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
        "M9-M2-fourth-moment-average-to-pointwise",
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-unpaired-residual-URES",
        "M9-M2-unpaired-reduced-paired-bound",
        "M9-M2-NF-participation-rigidity"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_006/responses/A2-006.md",
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md"
        ],
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_002/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_003/human/stage-a-response-audit.md",
          "rounds/obligation-main/round_003/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A1.md"
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
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/responses/A3-005.md",
          "rounds/obligation-main/round_006/responses/A3-006.md",
          "rounds/obligation-main/round_007/responses/A1-007.md"
        ]
      },
      "owner": "A2",
      "next_action": "Record that the exact N=0 arm is conditionally closed under H4. Keep the obligation open for 0<|N|~T near-collision bands, endpoint uniformity, and pointwise upgrade.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
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
        "positive": [
          "rounds/obligation-main/round_005/responses/A4-005.md"
        ],
        "negative": [
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "inconclusive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_007/responses/A1-007.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_008/responses/A1-008-revision.md",
          "rounds/obligation-main/round_008/responses/A2-008.md"
        ]
      },
      "owner": "A2",
      "next_action": "Replace the old full-range absolute GNC target. For D <= X^(3/8+o(1), audit restricted absolute or structured estimates using interval URES. For D > X^(3/8), pursue signed mechanisms such as c_chi or a sign-preserving Poisson/B-process estimate. Keep exact N=0, absolute lower bounds, signed estimates, and pointwise upgrade as separate obligations.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
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
        "negative": [
          "rounds/obligation-main/round_005/responses/A4-005.md"
        ],
        "inconclusive": []
      },
      "owner": "A2",
      "next_action": "Require each M2 route to isolate the endpoint D=X^(1/2), where the AP/local-average bridge degenerates to pointwise control.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/responses/A3-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_006/responses/A3-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_007/responses/A3-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_008/responses/A3-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "A2 should run the corrected complex-weight diagnostic in AI Studio Code Execution if available: cosine pairing can hold for shared complex d-weights, while the Re B_h shortcut fails. Include exact code, runtime output, parameters, pass/fail criteria, and limitations. Codex/local workflow must reproduce and archive script, command, table, precision log, and report before evidence is positive; A3 should audit the script and interpretation.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
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
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A3.md",
          "rounds/obligation-main/round_001/judge/judge-001.md",
          "rounds/obligation-main/round_006/responses/A3-006.md"
        ]
      },
      "owner": "A1",
      "next_action": "After H4 source-card validation, insert beta_h formula, raw two-sided M2 formula, complex-weight cosine pairing, real-weight Re B_h formula, and single-parity support into best_proof_draft.md.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
      "status": "derived_under_assumptions",
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
        "M9-M2-fourth-moment-average-to-pointwise",
        "M9-M2-fraction-matching-weighted-bound",
        "M9-M2-local-fourth-moment-LFM"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md"
        ],
        "negative": [
          "rounds/obligation-main/round_005/reviews/A1.md"
        ],
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
      "next_action": "Use M9-M2-exact-N0-total-mass as the exact-resonance closure under H4. Do not infer M9-M2; near-collision and pointwise upgrade remain open.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26",
      "reason_for_promotion": "Exact N=0 beta-weighted mass is now controlled under H4 by paired-core, reduced-paired, and URES divisor-bound arguments."
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
      "blockers": [
        "M9-M2-reciprocal-SPD-route"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_003/responses/A1-003.md",
          "rounds/obligation-main/round_003/responses/A2-003.md",
          "rounds/obligation-main/round_003/reviews/A1.md",
          "rounds/obligation-main/round_003/reviews/A3.md",
          "rounds/obligation-main/round_003/judge/judge-003.md",
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/responses/A3-005.md"
        ]
      },
      "owner": "A2",
      "next_action": "Recast as a precise sign-preserving discrepancy or spacing theorem. Require A3 signed-vs-unsigned evidence before allocating major proof effort.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/reviews/A1.md",
          "rounds/obligation-main/round_004/judge/judge-004.md"
        ]
      },
      "owner": "A2",
      "next_action": "Keep paired-core families treated under H4, but do not use them to promote full exact N=0 taxonomy. Separate fraction-matching from official semi-diagonal terminology.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
      "blockers": [
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-subcoherence-window-multiplier",
        "M9-M2-LFM-pointwise-equivalence"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
        ],
        "negative": [
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_008/responses/A1-008-revision.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "inconclusive": [
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_004/judge/judge-004.md",
          "rounds/obligation-main/round_005/responses/A1-005.md",
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Record the frozen-coefficient derivative obstruction: global L4 plus |S2'| << H_D gives only |S2(D;X0)| << D^(3/5) X^(3/20+epsilon), equal to X^(9/20+epsilon) at D=X^(1/2). Require a stronger large-value theorem, local signed cancellation theorem, or direct signed pointwise estimate.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
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
          "rounds/obligation-main/round_004/judge/judge-004.md",
          "rounds/obligation-main/round_005/responses/A3-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_006/responses/A3-006.md",
          "rounds/obligation-main/round_007/responses/A3-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md",
          "rounds/obligation-main/round_008/responses/A3-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "A2 should run small self-contained AI Studio Code Execution diagnostics with exact integer N, corrected complex-weight regression, c_chi and unsigned analogues, UNC/TS/W-1 family checks, D around X^(3/8), and endpoint D=X^(1/2). Include exact code, runtime output, parameters, pass/fail criteria, and limitations. Codex/local workflow must reproduce and archive precision logs, command line, tables, and report before evidence is positive; A3 should audit formulas, exact arithmetic, script logic, and interpretation. Keep output diagnostic_only.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-average-to-pointwise-AP-lemma",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Elementary local average-to-pointwise interpolation lemma",
      "status": "proved_internal",
      "statement_tex": "For F in C^1(I), |I|=delta, and X0 in I, |F(X0)|^4 <= delta^(-1) int_I |F|^4 + 4 sup_I |F'| delta^(1/4) (int_I |F|^4)^(3/4).",
      "dependencies": [],
      "implies": [
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Insert the AP lemma into the lemma bank as a standalone calculus lemma; keep all S2 applications separate and conditional.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
    },
    {
      "id": "M9-M2-local-fourth-moment-LFM",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Everywhere-local fourth-moment estimate for S2 on coherence windows",
      "status": "open",
      "statement_tex": "For active D and every interval I of length delta=X^(1/2)/D near X, prove delta^(-1) int_I |S_2(D;t)|^4 dt <<_epsilon X^(1+epsilon) with actual beta_h coefficients. The local expansion must control the fattened band |N| << D^5 X^(-1/2).",
      "dependencies": [
        "M9-M2-fourth-moment-expansion",
        "M9-M2-average-to-pointwise-AP-lemma",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "blockers": [
        "M9-near-collision-estimate",
        "M9-endpoint-uniformity",
        "M9-M2-local-fourth-moment-kernel",
        "M9-M2-subcoherence-window-multiplier",
        "M9-M2-LFM-pointwise-equivalence"
      ],
      "evidence": {
        "positive": [],
        "negative": [
          "rounds/obligation-main/round_006/responses/A1-006.md",
          "rounds/obligation-main/round_006/responses/A4-006.md"
        ],
        "inconclusive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md"
        ]
      },
      "owner": "A4",
      "next_action": "Do not treat coherence-window LFM as a relaxed average route. Any proof must provide full h,d-space cancellation, replace LFM by global moment plus large-value propagation, or split off endpoint blocks with a direct signed estimate.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-DP-near-collision-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Denominator-paired near-collision scoping bound",
      "status": "derived_under_assumptions",
      "statement_tex": "In the denominator-paired class d1=d2=a, d3=d4=b, N=ab L with L=(h1-h2)b+(h3-h4)a. Under the H4 beta support on odd h, nonzero L is even. Hence the thin band 0<|N|<=C0 D^4/X is empty unless D >= sqrt(2X/C0') up to dyadic constants; where nonempty its absolute beta-weighted mass is bounded by a harmonic-convolution estimate, and the full DP class is harmless at X^(1+epsilon) scale.",
      "dependencies": [
        "H4",
        "M9-M2-beta-algebra",
        "M9-M2-harmonic-convolution-LH",
        "M9-M2-denominator-paired-weighted-bound"
      ],
      "implies": [
        "M9-near-collision-estimate",
        "M9-near-collision-taxonomy"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Transcribe A4's DP-0 through DP-3 class-level statements with dyadic constants, parity support, C0 dependence, and H4 beta-magnitude dependency.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "M9-M2-coprime-rigidity-normal-form",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Coprime-rigidity normal form for exact reciprocal resonances",
      "status": "proved_internal",
      "statement_tex": "After reducing h_i/d_i to lowest terms, exact N=0 reciprocal resonances can be organized by denominator identities and a corresponding linear numerator equation. This is a pure rational normal-form lemma for classifying exact N=0 configurations.",
      "dependencies": [],
      "implies": [
        "M9-near-collision-taxonomy"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Replace the compact Round 6 statement with the Round 7 NF-0/NF-1 lemma-bank version.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "M9-M2-fraction-matching-weighted-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Fraction-matching exact resonance bound",
      "status": "derived_under_assumptions",
      "statement_tex": "For the exact N=0 family h1/d1=h2/d2 and h3/d3=h4/d4, with d_i asymp D and 1<=|h_i|<=H_D, the absolute beta-weighted mass is <<_epsilon D^2 X^epsilon under the H4 beta magnitude hypothesis. This is a fraction-matching subfamily and should not be identified with the denominator-pattern semi-diagonal family until terminology is reconciled.",
      "dependencies": [
        "H4",
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion"
      ],
      "implies": [
        "M9-near-collision-taxonomy"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A2",
      "next_action": "Rename consistently as fraction-matching or fraction-collision; verify endpoint truncations and prevent accidental promotion of the official semi-diagonal denominator-pattern subcase.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
    },
    {
      "id": "M9-M2-reciprocal-SPD-route",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Sign-preserving reciprocal discrepancy route for M2",
      "status": "proposed",
      "statement_tex": "A sign-preserving discrepancy or first-spacing theorem for smooth-weighted truncated sawtooth sums at reciprocal points theta_d=(X+rho d)/(4d), rho in {1,3}, strong enough to imply S_2(D;X)<<_epsilon X^(1/4+epsilon) uniformly over active D.",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-character-factor",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2-direct-signed-bilinear-lemma",
        "M9-M2"
      ],
      "blockers": [
        "H4-source-audit",
        "Li-Yang-source-audit"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/judge/judge-005.md",
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_007/responses/A1-007.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md"
        ]
      },
      "owner": "A4",
      "next_action": "State the exact SPD-1 discrepancy theorem and SPD-J jump/near-jump convention; separate integer-X exact jumps from real-X near-jumps; require A3 true-vs-unsigned-vs-random-vs-adversarial diagnostics before major proof investment.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "H4-Phi-regularity",
      "type": "lemma",
      "track": "source_audit",
      "title": "Regularity of Vaaler's Phi coefficient function",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming Vaaler's Theorem 6 coefficient formula Phi(u)=pi u(1-u)cot(pi u)+u for 0<u<1, Phi extends to C^1([0,1]) with Phi(0)=1, Phi(1)=0, Phi'(0)=Phi'(1)=0, and sup_[0,1]|Phi'(u)|<infty. This supports coefficient-stability bookkeeping and freezing H_D on local windows; it does not by itself validate H4.",
      "dependencies": [
        "H4-source-audit"
      ],
      "implies": [],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A1",
      "next_action": "After the Vaaler source card is validated, move this calculus lemma into the lemma bank and cite it in H4 coefficient-stability notes.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-local-fourth-moment-kernel",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Local fourth-moment kernel and fat N-band",
      "status": "proved_internal",
      "statement_tex": "For the S_2 fourth-moment expansion over an interval I of length delta, a tuple with cleared numerator N and denominator product Q=d_1d_2d_3d_4 satisfies |I|^(-1)|int_I e(tN/(4Q))dt| << min(1,D^4/(delta |N|)). For delta=X^(1/2)/D the local fat band is |N| << D^5 X^(-1/2).",
      "dependencies": [
        "M9-M2-fourth-moment-expansion"
      ],
      "implies": [
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A1",
      "next_action": "Insert the kernel calculation into the lemma bank and use it only as algebraic infrastructure, not as an M2 estimate.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-LFM-endpoint-degeneracy",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "Endpoint corollary of whole-range subcoherence obstruction",
      "status": "proved_internal",
      "statement_tex": "At D asymp X^(1/2), H_D asymp X^(1/4), and delta=X^(1/2)/D asymp 1, every fourth-moment tuple has |N| << H_D D^3 asymp X^(7/4), while the local fat-band threshold D^5 X^(-1/2) is asymp X^2. Thus the local fourth-moment kernel gives no N-spacing discrimination at the endpoint. This is the endpoint specialization of the whole-range subcoherence-window obstruction, not a separate averaging route; it obstructs absolute local N-spacing proofs at the endpoint, not all possible endpoint proofs.",
      "dependencies": [
        "M9-M2-local-fourth-moment-kernel",
        "M9-M2-subcoherence-window-multiplier",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-fourth-moment-average-to-pointwise",
        "M9-endpoint-uniformity"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A1",
      "next_action": "Fold this endpoint statement into the whole-range subcoherence-window multiplier when writing the lemma bank; do not maintain it as an independent relaxed-LFM route. Any endpoint proof must supply signed cancellation or another mechanism not based only on absolute N-spacing.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-subcoherence-window-multiplier",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Subcoherence multiplier bound on local windows",
      "status": "proved_internal",
      "statement_tex": "For every S_2 fourth-moment tuple with |h_i|<=H_D and d_i asymp D, lambda=(1/4)(h_1/d_1-h_2/d_2+h_3/d_3-h_4/d_4) satisfies |lambda| << H_D/D asymp X^(-1/4). On coherence windows delta=X^(1/2)/D, delta |lambda| << X^(1/4)/D <= O(1) throughout the active range X^(1/4)<=D<=X^(1/2). Thus the window multiplier has no power-scale decay.",
      "dependencies": [
        "M9-M2-fourth-moment-expansion"
      ],
      "implies": [
        "M9-M2-LFM-pointwise-equivalence",
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A3.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Insert this multiplier lemma into the lemma bank and use it to re-scope LFM away from a relaxed local-averaging route.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-LFM-pointwise-equivalence",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "Coherence-window LFM is pointwise-strength at target scale",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming the H4 beta magnitude |beta_h|<<1/|h|, bounded dyadic weights, and frozen H_D, the derivative drift of S_2 over a coherence window delta=X^(1/2)/D is O(X^(1/4)) while the window multiplier has no power decay. Therefore the LFM estimate delta^(-1) int_I |S_2(D;t)|^4 dt << X^(1+epsilon) is equivalent at target precision to pointwise control on I; any LFM proof must supply full h,d-space cancellation.",
      "dependencies": [
        "H4",
        "M9-M2-beta-algebra",
        "M9-M2-subcoherence-window-multiplier",
        "M9-M2-average-to-pointwise-AP-lemma"
      ],
      "implies": [
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Use this as a scoped obstruction. Do not treat LFM as a relaxed route unless a stronger averaging mechanism or global moment plus large-value propagation is supplied.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-NF-participation-rigidity",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Participation rigidity for reduced reciprocal resonances",
      "status": "proved_internal",
      "statement_tex": "Let r=mu/Q be reduced with mu nonzero, and let x_1=p_1/q_1 be reduced with x_3=r-x_1 nonzero of reduced denominator q_3. Put g=gcd(Q,q_1), Qhat=Q/g, qhat_1=q_1/g, and M=mu qhat_1-p_1 Qhat. Then gcd(Qhat qhat_1,M)=1 and q_3=g Qhat qhat_1/gcd(g,M) >= Q q_1/g^2. Consequently, if q_3<=2D, then gcd(Q,q_1)>=sqrt(Q q_1/(2D)) and gcd(g,M)>=Q q_1/(2D g).",
      "dependencies": [
        "M9-M2-coprime-rigidity-normal-form"
      ],
      "implies": [
        "M9-M2-unpaired-residual-URES",
        "M9-near-collision-taxonomy"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Transcribe NF-2 participation rigidity in final lemma-bank notation and use it as support for interval near-collision attempts.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "M9-M2-unpaired-reduced-paired-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Reduced-paired exact-resonance bound outside fraction matching",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming the H4 beta magnitude and bounded dyadic weights, exact N=0 tuples whose reduced-denominator multiset has form {q,q,q',q'} have total absolute beta-weighted mass <<_epsilon D^2 X^epsilon. This combines the value-unpaired U-2/SS/anti-paired classes with the existing fraction-matching bound and does not cover the URES residual class.",
      "dependencies": [
        "H4",
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion",
        "M9-M2-harmonic-convolution-LH",
        "M9-M2-fraction-matching-weighted-bound",
        "M9-M2-coprime-rigidity-normal-form"
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
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Attach OB-1 coverage and overlap bookkeeping; keep H4-source-audit as blocker.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "M9-M2-unpaired-residual-URES",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "URES residual exact-resonance bound",
      "status": "derived_under_assumptions",
      "statement_tex": "For the residual exact N=0 class whose reduced-denominator multiset is not of the form {q,q,q',q'}, prove sum_{r nonzero} R(r)^2 <<_epsilon D^2 X^epsilon for the representation-weighted pair-sum function R(r). The residual is nonempty, for example by 1/(6k)+1/(10k)=1/(15k)+1/(5k).",
      "dependencies": [
        "M9-M2-coprime-rigidity-normal-form",
        "M9-M2-NF-participation-rigidity",
        "M9-M2-unpaired-reduced-paired-bound"
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
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md",
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md",
          "rounds/obligation-main/round_006/judge/judge-006.md",
          "rounds/obligation-main/round_007/reviews/A3.md"
        ]
      },
      "owner": "A2",
      "next_action": "Treat exact URES residual as conditionally settled under H4. For near-collisions, use interval URES strip identity/count and keep degenerate branches separate.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44",
      "reason_for_promotion": "Round 7 supplies an exact factorization and divisor-bound argument for URES pair representations, plus lift-weight bookkeeping under the H4 beta-magnitude hypothesis."
    },
    {
      "id": "M9-M2-sign-preserving-poisson-voronoi-route",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Sign-preserving Poisson or B-process route for M2",
      "status": "proposed",
      "statement_tex": "A proposed sign-preserving transformation of S_2(D;X) in the d-variable, retaining the chi_4(h) beta structure through stationary phase or a Poisson-Voronoi type formula, followed by a signed dual estimate strong enough to imply S_2(D;X)<<_epsilon X^(1/4+epsilon) uniformly over active D. No estimate is currently proved.",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-character-factor",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2-direct-signed-bilinear-lemma",
        "M9-M2"
      ],
      "blockers": [
        "H4-source-audit",
        "Li-Yang-source-audit"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/responses/A2-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/judge/judge-006.md",
          "rounds/obligation-main/round_007/responses/A2-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "Restate as a smooth-weight stationary-phase obligation with exact constants, boundary terms, k=0 terms, nonstationary ranges, support-edge stationary points, and a signed post-transform estimate.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "Divisor-bound-elementary",
      "type": "lemma",
      "track": "proof_infrastructure",
      "title": "Elementary divisor-function epsilon bound",
      "status": "proved_internal",
      "statement_tex": "For every epsilon > 0, the divisor function satisfies d(n) <<_epsilon n^epsilon for all n >= 1.",
      "dependencies": [],
      "implies": [
        "M9-M2-URES-representation-divisor-bound"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_007/judge/judge-007.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_007/judge/judge-007.md"
        ]
      },
      "owner": "A1",
      "next_action": "Insert a short prime-factorisation proof into the lemma bank.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "M9-M2-URES-representation-divisor-bound",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "URES representation divisor bound",
      "status": "proved_internal",
      "statement_tex": "For fixed reduced r=mu/Q != 0 and fixed nonzero p1,p3, the number of denominator pairs q1,q3 satisfying p1/q1 + p3/q3 = mu/Q is O_epsilon((Q^2 |p1 p3|)^epsilon). The proof uses the exact factorization (mu q1 - Q p1)(mu q3 - Q p3)=Q^2 p1 p3 and the elementary divisor bound.",
      "dependencies": [
        "Divisor-bound-elementary"
      ],
      "implies": [
        "M9-M2-unpaired-residual-URES",
        "M9-M2-exact-N0-total-mass"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md",
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_007/judge/judge-007.md"
        ]
      },
      "owner": "A4",
      "next_action": "Transcribe the exact divisor factorization and its interval analogue into the lemma bank with notation Q reserved consistently.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-URES-energy-reduction",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "URES energy reduction to pair-representation second moment",
      "status": "proved_internal",
      "statement_tex": "For abstract reduced-fraction weights A(p/q) satisfying the dyadic lift envelope used in the M2 exact-resonance analysis, the URES exact-resonance contribution is controlled by sum_{r != 0} R_res(r)^2, where R_res(r)=sum_{x+y=r} A(x)A(y) over the residual reduced-fraction class.",
      "dependencies": [
        "M9-M2-coprime-rigidity-normal-form",
        "M9-M2-NF-participation-rigidity",
        "M9-M2-URES-representation-divisor-bound"
      ],
      "implies": [
        "M9-M2-unpaired-residual-URES"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_007/judge/judge-007.md"
        ]
      },
      "owner": "A4",
      "next_action": "Record the ordered-pair convention for R_res(r) and distinguish absolute R from signed R_chi.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-exact-N0-total-mass",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Total exact N=0 absolute mass for M2 fourth moment",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming H4 beta magnitude |beta_h| << 1/|h|, parity support, and bounded dyadic weights, the total absolute beta-weighted mass of all exact N=0 M2 fourth-moment tuples is <<_epsilon D^2 X^epsilon uniformly for X^(1/4) <= D <= X^(1/2). This is scoped strictly to exact resonances and does not include near-collision bands.",
      "dependencies": [
        "H4",
        "M9-M2-beta-algebra",
        "M9-M2-fourth-moment-expansion",
        "M9-M2-paired-core-weighted-bound",
        "M9-M2-denominator-paired-weighted-bound",
        "M9-M2-fraction-matching-weighted-bound",
        "M9-M2-unpaired-reduced-paired-bound",
        "M9-M2-unpaired-residual-URES",
        "M9-M2-URES-energy-reduction"
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
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md",
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_007/reviews/A3.md",
          "rounds/obligation-main/round_007/judge/judge-007.md",
          "rounds/obligation-main/round_008/responses/A1-008-revision.md"
        ]
      },
      "owner": "A4",
      "next_action": "Keep exact N=0 closure scoped strictly to exact resonances and conditional on H4. Use it in lower-bound subtraction only with H4 and beta-envelope dependencies visible.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-endpoint-algebraic-phase",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Endpoint algebraic phase identity near d approximately sqrt(X)/2",
      "status": "proved_internal",
      "statement_tex": "Let D0=floor(sqrt(X)/2) and sqrt(X)/2=D0+delta. For d=D0+m, hX/(4d)=h(D0-m)+h(m^2+2D0 delta+delta^2)/(D0+m). Hence the exponential phase may be replaced modulo integers by the second term. This is algebraic infrastructure only and has no implication to endpoint uniformity.",
      "dependencies": [],
      "implies": [],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_007/responses/A2-007.md",
          "rounds/obligation-main/round_007/reviews/A1.md",
          "rounds/obligation-main/round_007/reviews/A2.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_007/judge/judge-007.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use only as a coordinate identity for possible endpoint SPD or Poisson exploration; do not cite it as an estimate.",
      "last_updated_round": 7,
      "last_updated_at": "2026-07-03T04:56:26"
    },
    {
      "id": "M9-M2-GM4-from-exact-plus-graded",
      "type": "reduction",
      "track": "M9_analytic",
      "title": "Global fourth-moment route from exact resonance plus graded near-collision",
      "status": "proposed",
      "statement_tex": "A proposed route in which exact N=0 closure is combined with a graded estimate for Sigma_abs(0<|N|<=M) and a large-value theorem strong enough to imply pointwise S2(D;X0) <<_epsilon X0^(1/4+epsilon). The crude derivative bound plus a fourth moment is insufficient.",
      "dependencies": [
        "M9-M2-exact-N0-total-mass",
        "M9-near-collision-estimate",
        "M9-M2-fourth-moment-average-to-pointwise",
        "M9-endpoint-uniformity"
      ],
      "implies": [
        "M9-M2"
      ],
      "blockers": [
        "M9-near-collision-estimate",
        "M9-M2-LFM-pointwise-equivalence"
      ],
      "evidence": {
        "positive": [],
        "negative": [
          "rounds/obligation-main/round_008/responses/A1-008-revision.md",
          "rounds/obligation-main/round_008/responses/A4-008.md"
        ],
        "inconclusive": [
          "rounds/obligation-main/round_007/responses/A1-007.md",
          "rounds/obligation-main/round_007/responses/A4-007.md",
          "rounds/obligation-main/round_007/judge/judge-007.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ]
      },
      "owner": "A1",
      "next_action": "Do not use exact N=0 plus an absolute graded estimate to promote M9-M2. The absolute fat-band target is false for D > X^(3/8+delta), and a global L4 estimate plus crude derivative propagation gives only D^(3/5)X^(3/20+epsilon). Any viable route now needs signed fat-band control and a large-value or direct pointwise theorem.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-interval-URES-strip-identity",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Interval URES strip identity",
      "status": "proved_internal",
      "statement_tex": "For reduced mu/Q != 0 and reduced nonzero fractions p1/q1, p3/q3 with q1,q3>0, if |p1/q1 + p3/q3 - mu/Q| <= eta, then |(mu q1 - Q p1)(mu q3 - Q p3) - Q^2 p1 p3| <= |mu| eta Q q1 q3. This is algebra only and gives no counting bound by itself.",
      "dependencies": [],
      "implies": [
        "M9-near-collision-taxonomy",
        "M9-near-collision-estimate"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_008/responses/A1-008-revision.md",
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_008/judge/judge-008.md"
        ]
      },
      "owner": "A1",
      "next_action": "Use this identity only as algebraic infrastructure; route any counting assertion through M9-M2-interval-URES-strip-count.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-interval-URES-strip-count",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Interval URES strip count with degenerate branch separated",
      "status": "proved_internal",
      "statement_tex": "For reduced mu/Q != 0, fixed nonzero p1,p3, Q <= 4D^2, |p_i| <= 2H_D, 0 <= eta <= 4X^(-1/4), and q_i in [1,2D] with gcd(p_i,q_i)=1, the number of pairs satisfying |p1/q1 + p3/q3 - mu/Q| <= eta is <<_epsilon X^epsilon (1 + eta QD^2) + Delta, where Delta <= 4D 1_{eta >= 1/(2D)} is the degenerate branch. This is a representation-strip count, not a full M2 near-collision estimate.",
      "dependencies": [
        "Divisor-bound-elementary",
        "M9-M2-interval-URES-strip-identity"
      ],
      "implies": [
        "M9-near-collision-taxonomy",
        "M9-near-collision-estimate"
      ],
      "blockers": [],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A2.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_008/judge/judge-008.md"
        ]
      },
      "owner": "A4",
      "next_action": "Apply only with the stated nondegenerate/degenerate split; next assemble dyadic lifts and parity restrictions without losing the statement's hypotheses.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-near-collision-absolute-lower-bounds",
      "type": "obstruction",
      "track": "M9_analytic",
      "title": "Absolute near-collision lower bounds obstruct endpoint GNC",
      "status": "derived_under_assumptions",
      "statement_tex": "Assuming H4 beta lower envelopes and exact N=0 mass closure, the old full-range absolute GNC target is false in upper dyadic ranges. The absolute graded estimate is refuted for large M in the UNC range, and the fat-band target Sigma_abs(0<|N|<=D^4/X) << D^2 X^epsilon is false for D >= X^(3/8+delta) by the W-1 window lower bound. These are obstructions to absolute or unsigned routes only, not to signed estimates.",
      "dependencies": [
        "H4",
        "H4-Phi-regularity",
        "M9-M2-beta-algebra",
        "M9-M2-exact-N0-total-mass"
      ],
      "implies": [
        "M9-near-collision-estimate",
        "M9-M2-local-fourth-moment-LFM",
        "M9-M2-LFM-endpoint-degeneracy"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md",
          "rounds/obligation-main/round_008/reviews/A2.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_008/judge/judge-008.md"
        ]
      },
      "owner": "A4",
      "next_action": "Separate UNC, TS, and W-1 in the proof draft, including parity, dyadic support, beta lower envelope, and exact M,D,X ranges.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-signed-lift-cancellation-B1",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Signed dyadic lift cancellation for M2 pair weights",
      "status": "derived_under_assumptions",
      "statement_tex": "Under H4 beta algebra, Phi regularity, parity support, and suitable smooth or bounded-variation dyadic lift weights, the signed lift weight A_chi(p/q)=sum_{gq in [D,2D), 1<=|gp|<=H_D} beta_{gp,H_D} w_D(gq) satisfies a cancellation envelope of the form |A_chi(p/q)| << q/(D|p|) in the stated B1 regime. This is a pair-weight lemma only and does not prove M9-M2.",
      "dependencies": [
        "H4",
        "H4-Phi-regularity",
        "M9-M2-beta-algebra"
      ],
      "implies": [
        "M9-M2-character-factor",
        "M9-M2-signed-fat-band-constant"
      ],
      "blockers": [
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_008/judge/judge-008.md"
        ]
      },
      "owner": "A4",
      "next_action": "Write the proof with exact weight smoothness, endpoint, parity, and Phi-regularity hypotheses; test whether this bound is strong enough for c_chi.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
    },
    {
      "id": "M9-M2-signed-fat-band-constant",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "Signed fat-band constant for M2 global fourth moment",
      "status": "proposed",
      "statement_tex": "Define the signed off-diagonal pair-sum constant c_chi(D;X) in the frozen-coefficient smoothed global fourth moment for S2(D;X). Prove |c_chi(D;X)| <<_epsilon X^epsilon uniformly, at least for X^(3/8)<D<=X^(1/2), or construct a signed lower-bound obstruction. This does not imply M9-M2 without a pointwise large-value theorem or direct endpoint estimate.",
      "dependencies": [
        "M9-M2-beta-algebra",
        "M9-M2-character-factor",
        "M9-M2-signed-lift-cancellation-B1",
        "M9-M2-fourth-moment-expansion",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "implies": [
        "M9-M2-GM4-from-exact-plus-graded",
        "M9-near-collision-estimate"
      ],
      "blockers": [
        "H4-source-audit",
        "M9-M2-fourth-moment-average-to-pointwise"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_008/responses/A4-008.md",
          "rounds/obligation-main/round_008/reviews/A1.md",
          "rounds/obligation-main/round_008/reviews/A2.md",
          "rounds/obligation-main/round_008/judge/judge-008.md"
        ]
      },
      "owner": "A2",
      "next_action": "State the exact frozen-coefficient identity, define c_chi and its unsigned analogue, and prove a bound or produce signed diagnostic evidence showing failure.",
      "last_updated_round": 8,
      "last_updated_at": "2026-07-04T10:35:44"
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
    },
    {
      "id": "A2-R5-continuous-L4-rational-orthogonality",
      "reason": "Rejected because integral over alpha in [0,1] of e(alpha theta) does not vanish for arbitrary nonzero rational theta; the proposed continuous L4 identity does not exactly detect reciprocal exact resonance.",
      "last_updated_at": "2026-07-02T23:47:54",
      "last_updated_round": 5,
      "evidence": [
        "rounds/obligation-main/round_005/judge/judge-005.md"
      ]
    },
    {
      "id": "A2-R5-semi-diagonal-terminology-promotion",
      "reason": "Rejected because A2's fraction-matching proof may not be the official denominator-pattern semi-diagonal family; it must be renamed or reconciled before being used as that subcase.",
      "last_updated_at": "2026-07-02T23:47:54",
      "last_updated_round": 5,
      "evidence": [
        "rounds/obligation-main/round_005/judge/judge-005.md"
      ]
    },
    {
      "id": "A2-R5-full-exact-N0-taxonomy-promotion",
      "reason": "Rejected because paired and fraction-matching subfamilies do not exhaust exact N=0; unpaired and mixed classes remain open.",
      "last_updated_at": "2026-07-02T23:47:54",
      "last_updated_round": 5,
      "evidence": [
        "rounds/obligation-main/round_005/judge/judge-005.md"
      ]
    },
    {
      "id": "A3-R5-unexecuted-artifact-positive-evidence",
      "reason": "Rejected because a code-and-command plan is not positive diagnostic evidence until files exist, compile, run, and produce tables, logs, and report output.",
      "last_updated_at": "2026-07-02T23:47:54",
      "last_updated_round": 5,
      "evidence": [
        "rounds/obligation-main/round_005/judge/judge-005.md"
      ]
    },
    {
      "id": "A4-R5-AP-implies-M9-M2",
      "reason": "Rejected because Lemma AP only converts an everywhere-local fourth-moment hypothesis into a pointwise bound; it does not prove that local fourth-moment hypothesis.",
      "last_updated_at": "2026-07-02T23:47:54",
      "last_updated_round": 5,
      "evidence": [
        "rounds/obligation-main/round_005/judge/judge-005.md"
      ]
    },
    {
      "id": "A2-R6-unpaired-exact-N0-mass-bound-derived",
      "reason": "Rejected because the claimed unpaired exact N=0 mass bound is not lift-corrected and does not control URES, overlap classes, dyadic lifts, or beta-weighted multiplicities.",
      "last_updated_at": "2026-07-03T01:57:58",
      "last_updated_round": 6,
      "evidence": [
        "rounds/obligation-main/round_006/judge/judge-006.md"
      ]
    },
    {
      "id": "A2-R6-cleared-phase-non-separability-route-closing",
      "reason": "Rejected as a proved route-closing obstruction. The integer detector e(alpha N) records why the old continuous rational L4 route fails to factor, but it does not rule out all integer-kernel or delta-method approaches.",
      "last_updated_at": "2026-07-03T01:57:58",
      "last_updated_round": 6,
      "evidence": [
        "rounds/obligation-main/round_006/judge/judge-006.md"
      ]
    },
    {
      "id": "A2-R6-poisson-voronoi-as-proof-evidence",
      "reason": "Rejected as state evidence because no uniform stationary-phase formula, boundary analysis, dual-range control, or signed post-transform estimate is supplied.",
      "last_updated_at": "2026-07-03T01:57:58",
      "last_updated_round": 6,
      "evidence": [
        "rounds/obligation-main/round_006/judge/judge-006.md"
      ]
    },
    {
      "id": "A3-R6-unexecuted-artifact-positive-evidence",
      "reason": "Rejected because the diagnostic bundle was not executed and computation may only be diagnostic even when executed.",
      "last_updated_at": "2026-07-03T01:57:58",
      "last_updated_round": 6,
      "evidence": [
        "rounds/obligation-main/round_006/judge/judge-006.md"
      ]
    },
    {
      "id": "A3-R6-unclassified-mass-pass-fail",
      "reason": "Rejected because unclassified or URES mass is a mathematical target to bound, not a code failure condition.",
      "last_updated_at": "2026-07-03T01:57:58",
      "last_updated_round": 6,
      "evidence": [
        "rounds/obligation-main/round_006/judge/judge-006.md"
      ]
    },
    {
      "id": "A2-R7-URES-absolute-bound-failure",
      "reason": "Rejected because the displayed obstruction drops or violates the q1<=2D constraint for most Q, and constraint-respecting checks point to D^2 X^epsilon scale rather than a D^4 obstruction.",
      "last_updated_at": "2026-07-03T04:56:26",
      "last_updated_round": 7,
      "evidence": [
        "rounds/obligation-main/round_007/judge/judge-007.md"
      ]
    },
    {
      "id": "A2-R7-Poisson-Boundary-Bound-proved",
      "reason": "Rejected because the boundary estimate is not proved for sharp dyadic cutoffs and lacks smooth-weight assumptions, endpoint stationary-point analysis, k=0 terms, nonstationary tails, and uniform error terms.",
      "last_updated_at": "2026-07-03T04:56:26",
      "last_updated_round": 7,
      "evidence": [
        "rounds/obligation-main/round_007/judge/judge-007.md"
      ]
    },
    {
      "id": "A2-R7-endpoint-algebraic-phase-implies-uniformity",
      "reason": "Rejected because the endpoint algebraic phase identity is exact algebra on a coordinate patch but does not imply any uniform bound over active D.",
      "last_updated_at": "2026-07-03T04:56:26",
      "last_updated_round": 7,
      "evidence": [
        "rounds/obligation-main/round_007/judge/judge-007.md"
      ]
    },
    {
      "id": "A3-R7-regression-verified",
      "reason": "Rejected because the diagnostic bundle is not accepted until code compiles, runs, and produces the required tables, logs, and report.",
      "last_updated_at": "2026-07-03T04:56:26",
      "last_updated_round": 7,
      "evidence": [
        "rounds/obligation-main/round_007/judge/judge-007.md"
      ]
    },
    {
      "id": "A3-R7-fake-complex-failure-test",
      "reason": "Rejected because the proposed symmetric fake-complex setup preserves the conjugacy relation it was supposed to violate; the test must use genuinely complex d-weights or asymmetric h-weights.",
      "last_updated_at": "2026-07-03T04:56:26",
      "last_updated_round": 7,
      "evidence": [
        "rounds/obligation-main/round_007/judge/judge-007.md"
      ]
    },
    {
      "id": "A3-R7-Mellin-Perron-route",
      "reason": "Rejected as a state mutation because the exploratory Mellin-Perron discussion contains a formal application error and no theorem-level bridge to M9.",
      "last_updated_at": "2026-07-03T04:56:26",
      "last_updated_round": 7,
      "evidence": [
        "rounds/obligation-main/round_007/judge/judge-007.md"
      ]
    },
    {
      "id": "A1-R8-global-GNC-low-for-all-D",
      "reason": "Rejected as a global all-D target because A4's W-1 lower bound refutes the fat-band case for D > X^(3/8+delta). It may be replaced only by a restricted lower-D, structured, or signed target.",
      "last_updated_at": "2026-07-04T10:35:44",
      "last_updated_round": 8,
      "evidence": [
        "rounds/obligation-main/round_008/judge/judge-008.md"
      ]
    },
    {
      "id": "A1-R8-full-range-GNC-Abs",
      "reason": "Rejected over the full support. A1's full-support mass calculation and A4's lower-bound families show the old full-range absolute cumulative estimate is false.",
      "last_updated_at": "2026-07-04T10:35:44",
      "last_updated_round": 8,
      "evidence": [
        "rounds/obligation-main/round_008/judge/judge-008.md"
      ]
    },
    {
      "id": "A2-R8-M9-M2-absolute-mass-obstruction-proved-internal",
      "reason": "Rejected at proved_internal status because A2's uniform-distribution heuristic is not a proof. The obstruction conclusion should be recorded only as H4-dependent and based on A4's explicit UNC, TS, and W-1 lower bounds.",
      "last_updated_at": "2026-07-04T10:35:44",
      "last_updated_round": 8,
      "evidence": [
        "rounds/obligation-main/round_008/judge/judge-008.md"
      ]
    },
    {
      "id": "A2-R8-URES-interval-factorization-as-written",
      "reason": "Rejected as written because the target pair-sum sign convention must be corrected. Use the A1/A4 integer-defect formulation and separate the degenerate uv=0 branch.",
      "last_updated_at": "2026-07-04T10:35:44",
      "last_updated_round": 8,
      "evidence": [
        "rounds/obligation-main/round_008/judge/judge-008.md"
      ]
    },
    {
      "id": "A2-R8-Poisson-B-Process-Transform-proved",
      "reason": "Rejected as proved. The leading stationary-phase calculation lacks full boundary, m=0, support-edge, nonstationary, smoothing/unsmoothing, and post-transform signed-sum estimates.",
      "last_updated_at": "2026-07-04T10:35:44",
      "last_updated_round": 8,
      "evidence": [
        "rounds/obligation-main/round_008/judge/judge-008.md"
      ]
    },
    {
      "id": "A3-R8-diagnostics-as-proof",
      "reason": "Rejected because computations are diagnostic_only and require executed artifacts before even diagnostic evidence is positive.",
      "last_updated_at": "2026-07-04T10:35:44",
      "last_updated_round": 8,
      "evidence": [
        "rounds/obligation-main/round_008/judge/judge-008.md"
      ]
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 8 in run `obligation-main`.

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
  Next action: Use the signed lift-cancellation B1 lemma and c_chi target to preserve the chi_4(h) structure in upper-range near-collision analysis. Do not use character-blind absolute norms past D=X^(3/8).
- `M9-near-collision-taxonomy` (open, owner `A2`): M2 fourth-moment near-collision taxonomy
  Next action: Record that the exact N=0 arm is conditionally closed under H4. Keep the obligation open for 0<|N|~T near-collision bands, endpoint uniformity, and pointwise upgrade.
- `M9-regression-raw-vs-paired` (diagnostic_only, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Correct the complex-weight test: cosine pairing can hold for shared complex d-weights, while the Re B_h shortcut fails. Execute and archive script, command, table, precision log, and report.

## Do-Not-Claim Rules

- Do not claim `M9` or the final Gauss circle target.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use Li-Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Agent Assignments

Use `state/next_round_prompts.md` for any judge-assigned A1/A2/A3/A4 tasks.

Default target split:
- `A1`: synthesis, proof-draft maintenance, source-card discipline, and State Patch authoring.
- `A2`: conservative obstruction analysis plus AI Studio Code Execution for small self-contained Python diagnostics when assigned.
- `A3`: diagnostic script/result auditing, algebra checks, source-card artifacts, and artifact bundles when no real execution output is available.
- `A4`: independent analytic proof-surgery for narrow sublemmas and route repair.

Diagnostic execution policy:
- A2 Code Execution output is `diagnostic_only` and must include exact code, runtime output, parameters, pass/fail criteria, and limitations.
- If A2 has no actual Code Execution output, mark the job `not_executed`.
- Codex or the local workflow must reproduce A2 diagnostics in this repository before they count as positive diagnostic evidence.
- A3 reviews diagnostic code/results and must not claim execution without real runtime output.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `sources/vaaler_1985.md`
- `sources/li_yang_2023.md`
- `manifests/reading_packet.md`

## Last State Patch

created: M9-M2-interval-URES-strip-identity, M9-M2-interval-URES-strip-count, M9-near-collision-absolute-lower-bounds, M9-M2-signed-lift-cancellation-B1, M9-M2-signed-fat-band-constant; updated: M9-near-collision-estimate, M9-M2-GM4-from-exact-plus-graded, M9-M2-fourth-moment-average-to-pointwise, M9-M2-exact-N0-total-mass, M9-M2-URES-representation-divisor-bound, M9-M2-URES-energy-reduction, M9-M2-unpaired-residual-URES, M9-M2-character-factor, M9-fourth-moment-enumeration, M9-regression-raw-vs-paired, H4-source-audit; rejected: A1-R8-global-GNC-low-for-all-D, A1-R8-full-range-GNC-Abs, A2-R8-M9-M2-absolute-mass-obstruction-proved-internal, A2-R8-URES-interval-factorization-as-written, A2-R8-Poisson-B-Process-Transform-proved, A3-R8-diagnostics-as-proof; no_change: M9, M9-M1, M9-M2, M9-endpoint-uniformity, GC-target, Conditional-bridge, H4, R5-Full, Li-Yang-source-audit; round score: 6; Round 8 makes real proof-graph-safe progress by refuting the old absolute near-collision route in upper dyadic ranges, adding interval URES strip infrastructure, and defining the signed fat-band target. It does not prove M9, M9-M2, M9-M1, H4, or the Gauss circle endpoint.

## Active Obligation Briefs

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Use the signed lift-cancellation B1 lemma and c_chi target to preserve the chi_4(h) structure in upper-range near-collision analysis. Do not use character-blind absolute norms past D=X^(3/8).

### M9-near-collision-taxonomy: M2 fourth-moment near-collision taxonomy

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-unpaired-residual-URES`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-NF-participation-rigidity`
- Next action: Record that the exact N=0 arm is conditionally closed under H4. Keep the obligation open for 0<|N|~T near-collision bands, endpoint uniformity, and pointwise upgrade.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `diagnostic_only`
- Track: `computation`
- Owner: `A3`
- Next action: Correct the complex-weight test: cosine pairing can hold for shared complex d-weights, while the Re B_h shortcut fails. Execute and archive script, command, table, precision log, and report.

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
- Next action: Finalize sources/vaaler_1985.md with DOI, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, beta lower envelope, and M2 parity support.

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
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`
- Next action: Do not promote from AP, DP scoping, or paired/fraction subfamilies. Supply a pointwise M2 estimate, a local fourth-moment estimate valid at endpoint, or a sign-preserving direct estimate with uniformity.

### M9-M2-GM4-from-exact-plus-graded: Global fourth-moment route from exact resonance plus graded near-collision

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A1`
- Blockers: `M9-near-collision-estimate`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Do not use exact N=0 plus an absolute graded estimate to promote M9-M2. The absolute fat-band target is false for D > X^(3/8+delta), and a global L4 estimate plus crude derivative propagation gives only D^(3/5)X^(3/20+epsilon). Any viable route now needs signed fat-band control and a large-value or direct pointwise theorem.

### M9-M2-direct-signed-bilinear-lemma: Direct signed bilinear estimate for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-M2-reciprocal-SPD-route`
- Next action: Recast as a precise sign-preserving discrepancy or spacing theorem. Require A3 signed-vs-unsigned evidence before allocating major proof effort.

### M9-M2-fourth-moment-average-to-pointwise: Average-to-pointwise upgrade for M2 fourth-moment estimates

- Status: `open`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `M9-M2-local-fourth-moment-LFM`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Record the frozen-coefficient derivative obstruction: global L4 plus |S2'| << H_D gives only |S2(D;X0)| << D^(3/5) X^(3/20+epsilon), equal to X^(9/20+epsilon) at D=X^(1/2). Require a stronger large-value theorem, local signed cancellation theorem, or direct signed pointwise estimate.

### M9-M2-local-fourth-moment-LFM: Everywhere-local fourth-moment estimate for S2 on coherence windows

- Status: `open`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `M9-M2-local-fourth-moment-kernel`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Do not treat coherence-window LFM as a relaxed average route. Any proof must provide full h,d-space cancellation, replace LFM by global moment plus large-value propagation, or split off endpoint blocks with a direct signed estimate.

### M9-M2-reciprocal-SPD-route: Sign-preserving reciprocal discrepancy route for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `H4-source-audit`, `Li-Yang-source-audit`
- Next action: State the exact SPD-1 discrepancy theorem and SPD-J jump/near-jump convention; separate integer-X exact jumps from real-X near-jumps; require A3 true-vs-unsigned-vs-random-vs-adversarial diagnostics before major proof investment.

### M9-M2-sign-preserving-poisson-voronoi-route: Sign-preserving Poisson or B-process route for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `Li-Yang-source-audit`
- Next action: Restate as a smooth-weight stationary-phase obligation with exact constants, boundary terms, k=0 terms, nonstationary ranges, support-edge stationary points, and a signed post-transform estimate.

### M9-M2-signed-fat-band-constant: Signed fat-band constant for M2 global fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `M9-M2-fourth-moment-average-to-pointwise`
- Next action: State the exact frozen-coefficient identity, define c_chi and its unsigned analogue, and prove a bound or produce signed diagnostic evidence showing failure.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Require each M2 route to isolate the endpoint D=X^(1/2), where the AP/local-average bridge degenerates to pointwise control.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Replace the old full-range absolute GNC target. For D <= X^(3/8+o(1), audit restricted absolute or structured estimates using interval URES. For D > X^(3/8), pursue signed mechanisms such as c_chi or a sign-preserving Poisson/B-process estimate. Keep exact N=0, absolute lower bounds, signed estimates, and pointwise upgrade as separate obligations.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Generated after round 8 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_008/judge/judge-008.md`.

## For A1

Primary objectives:

1. Write the Round 9 proof-draft update reflecting the route bifurcation:
   - exact $N=0$ arm remains conditionally closed under H4;
   - absolute near-collision estimates are refuted for $D>X^{3/8+\delta}$ in the fat band;
   - absolute/structured estimates remain only a lower-range or class-restricted subroute;
   - signed $c_\chi$ becomes the upper-range primary target.

2. Complete `H4-source-audit` if possible. The source card must include Vaaler 1985 metadata, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, endpoint convention, $\Phi$ regularity, beta lower envelope, and M2 parity support.

3. Formalize the pointwise upgrade gap:
   - restate A1's derivative obstruction;
   - define the exact large-value theorem needed after a signed global moment;
   - specify separated points, threshold $V$, active $D$, and what bound would imply $V\ll X^{1/4+\epsilon}$.

4. Audit the State Patch after validation. If `M9-M2-interval-URES-strip-count` is accepted, insert it as a scoped arithmetic lemma, not as a near-collision theorem.

Exploratory allocation: formulate one signed large-sieve or spacing theorem that would imply the $c_\chi$ bound, with an immediate falsification test.

## For A2

Primary objectives:

1. Audit A4's lower-bound families in proof-detail:
   - UNC large-$M$ family;
   - TS twin-shift family;
   - W-1 window/pigeonhole lower bound;
   - parity, dyadic support, $N\ne0$, $1\le |h_i|\le H_D$, beta lower envelope, and exact $M,D,X$ ranges.

2. Replace the A2 heuristic absolute-mass obstruction with the W-1 proof. Do not label any heuristic uniform-distribution argument as `proved_internal`.

3. Audit the interval URES count:
   - verify the integer-defect convention;
   - verify nondegenerate $uv\ne0$ divisor count;
   - verify the degenerate $uv=0$ branch;
   - decide how the degenerate branch maps into paired or participation-degenerate fourth-moment classes.

4. Work on `M9-M2-signed-fat-band-constant`:
   - define $c_\chi(D;X)$ precisely;
   - state the required signed bound;
   - identify whether B-1 signed lift cancellation is strong enough, or what additional cancellation is needed.

5. If computation is assigned, run the small Python diagnostic in Google AI Studio Code Execution if available:
   - include exact Python code;
   - include returned stdout/stderr or tables;
   - state parameters, dyadic conventions, pass/fail criteria, and limitations;
   - mark the result `diagnostic_only`;
   - if Code Execution is unavailable or returns no runtime output, write `not_executed` and provide only a runnable artifact bundle.

Exploratory allocation: keep Poisson/B-process only as a backup. Supply a full theorem-shaped stationary-phase statement if pursuing it; otherwise do not promote it.

## For A3

Primary objectives:

1. Audit diagnostics rather than claiming execution unless real runtime output is available. For A2/Codex diagnostic artifacts, check:
   - exact formulas and conventions;
   - script logic;
   - exact integer/rational arithmetic choices;
   - parameter ranges and dyadic conventions;
   - stdout/tables and pass/fail assertions;
   - whether Codex/local reproduction is still needed.

2. If no executed artifact is supplied, provide a runnable artifact bundle only:
   - script path;
   - complete script text;
   - exact command;
   - expected table schema;
   - precision/log fields;
   - `report.md` template;
   - pass/fail assertions;
   - explicit `not_executed` label.

3. Prioritize diagnostics that match the new $X^{3/8}$ split:
   - compute $\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)/D^2$ for $D=X^\delta$ around $\delta=3/8$;
   - compare with W-1 lower-bound prediction $D^4X^{-3/4}$;
   - test UNC and TS formula families separately.

4. Audit or specify signed-object diagnostics:
   - $c_\chi(D;X)$;
   - unsigned analogue;
   - random-sign analogue;
   - adversarial-sign analogue;
   - endpoint $D\asymp X^{1/2}$ sign ratios.

5. Fix formula regressions:
   - cosine pairing may hold for shared complex $d$-weights;
   - $\operatorname{Re}B_h$ shortcut should fail for complex weights;
   - exact integer arithmetic must be used for $N$ and rational identities.

Exploratory allocation: implement U-3$\eta$ strip enumeration, including the degenerate branch, to compare empirical counts with $X^\epsilon(1+\eta QD^2)+\Delta$.

## For A4

Primary objectives:

1. Formalize `M9-M2-signed-fat-band-constant` in lemma-bank style:
   - define the smoothed global fourth moment;
   - define signed pair weights;
   - define $c_\chi(D;X)$;
   - state all frozen-coefficient and smooth-weight hypotheses;
   - isolate diagonal/exact $N=0$ and off-diagonal contributions.

2. Expand B-1:
   - state exact assumptions on $\Phi$, $w_D$, parity, and endpoint support;
   - prove the signed lift bound with constants and error terms;
   - state clearly whether it is enough for $c_\chi$ or only a first saving.

3. Separate lower-bound families:
   - write UNC, TS, and W-1 as standalone obstruction lemmas;
   - specify which one refutes large-$M$ GNC and which one refutes the fat band;
   - include exact ranges and beta lower-envelope dependencies.

4. If time remains, attempt the lower-range absolute upper half:
   - for $D\le X^{3/8}$, decide whether U-3$\eta$ plus lift bookkeeping can prove a restricted absolute estimate;
   - isolate any class where the bound fails.

Exploratory allocation: examine whether the sign-preserving Poisson route and $c_\chi$ route are actually the same dual obstruction in different variables.

## Round Assessment

Agent scores:

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 7.0 | 8.5 | Strong normalization and derivative-propagation obstruction; correctly rejected full-range GNC. The low-band target needed the W-1 correction and must now be $D$-restricted or signed. |
| A2 | 7.5 | 4.0 | 5.5 | Useful obstruction pressure and Poisson exploration, but over-promoted heuristic and transform claims. Needs to replace heuristics with A4's explicit lower-bound proof. |
| A3 | 7.0 | 2.5 | 7.5 | Good diagnostic design and formula-awareness, but no executed evidence yet. Under the updated workflow, A3 should audit A2/Codex diagnostics or provide runnable artifact bundles targeting the new $X^{3/8}$ split. |
| A4 | 9.5 | 8.5 | 8.5 | Round's strongest contribution: U-3$\eta$ strip count, W-1 fat-band refutation, signed lift direction, and $c_\chi$ target. H4 dependencies and signed-bound gaps remain. |

State evidence is substantial for arithmetic infrastructure and obstruction, but not for endpoint estimates. The `mathematical_progress_score` is kept at 6 because the round narrows the proof graph and rejects a false route but does not prove `M9-M2`.

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

# Diagnostic Execution Assignment

Kind: workflow directive
Timestamp: 2026-07-04T00:00:00

For future M9 rounds, move the primary run-Python diagnostic job from A3 to A2 when Google AI Studio Code Execution is available.

A2 may run small self-contained Python diagnostics only through AI Studio Code Execution. A2 must include exact Python code, returned stdout/stderr or tables, parameters, dyadic conventions, pass/fail criteria, limitations, and `diagnostic_only` status. If Code Execution is unavailable or no runtime output is returned, A2 must mark the job `not_executed` and provide only a runnable artifact bundle.

Codex or the local workflow must reproduce A2's diagnostic inside the repository before the result can be attached as positive diagnostic evidence in `state/proof_obligations.yml`.

A3 should primarily audit diagnostic formulas, script logic, exact arithmetic choices, and result interpretation. A3 must not claim Python execution unless real runtime output is available.

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

A2 should run small executable checks through AI Studio Code Execution when available, especially formula regression, finite counterexample search, and small exact enumeration. A3 should translate or audit leading route proposals into artifact bundles and script/result reviews. Computation remains diagnostic only.

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

A2 should improve computation-track evidence by producing AI Studio Code Execution output when available. A3 should improve by producing execution-ready artifact bundles and by auditing A2/Codex diagnostic outputs. If A3 cannot physically write repo files, it must output repository-relative file paths, script contents, exact command lines, expected table schema, precision/log fields, and a short report. The local workflow or Codex can then materialize and run those artifacts. Prose descriptions of tests do not count as evidence.

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

This is the A1 Stage A Round 9 reasoning response, using `A1_reasoning_9.md` as the controlling prompt and the Round 8 proof-obligation graph as current state. The prompt assigns A1 to write the proof-draft route bifurcation, audit H4/Vaaler if possible, formalize the pointwise-upgrade gap, and treat `M9-M2-interval-URES-strip-count` as a scoped arithmetic lemma rather than a near-collision theorem.

No theorem-level progress toward `M9`, `M9-M2`, `M9-M1`, or `GC-target` is claimed. The current proof route remains conditional:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

and `M9` remains open with blockers `M9-M2-character-factor`, `M9-near-collision-taxonomy`, and `M9-endpoint-uniformity`.

The concrete Round 9 proof-draft update is:

1. The exact $N=0$ fourth-moment arm should be recorded as conditionally closed under H4, via `M9-M2-exact-N0-total-mass`; it is not an M2 estimate.
2. The old full-range absolute near-collision target is no longer viable. In the upper range $D>X^{3/8+\delta}$, the fat-band absolute estimate is refuted under the existing H4 beta lower-envelope assumptions.
3. Absolute and structured near-collision estimates remain useful only in lower ranges or tightly scoped classes, such as interval-URES nondegenerate strips, denominator-paired bands, or other classified subfamilies.
4. The upper-range primary analytic target should be the signed fat-band constant $c_\chi(D;X)$, with the $\chi_4$ structure retained.
5. Even a signed global fourth moment does not prove pointwise `M9-M2` unless paired with a large-value theorem or a direct pointwise estimate.

The H4 source audit is now precise enough for a proof-draft source-card draft, but I do not propose promoting H4 because the repo source card still must be physically updated and validated. Vaaler's paper is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc. (N.S.)* 12(2), 183--216, 1985, DOI `10.1090/S0273-0979-1985-15349-2`. The local rendered PDF confirms the relevant anchors: Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), and Theorem 18 equations (7.13)--(7.17).

For Li--Yang, the official arXiv record is arXiv:2308.14859v2, last revised 14 September 2023, by Xiaochun Li and Xuerui Yang; the abstract states that the paper uses the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results. The TeX audit confirms that their theorem-level object is a bounded-variation weighted double sum $S$ with Case A/B hypotheses and a final target $S/H\lesssim_\epsilon T^{\theta^*+\epsilon}$, not a black-box endpoint theorem for the current Vaaler fixed-coefficient `M9` blocks.

## Target proof obligation

The active obligations for this response are:

- `M9-M2-character-factor`: preserve the $\chi_4(h)$ structure in upper-range M2 estimates, especially past $D=X^{3/8}$.
- `M9-near-collision-taxonomy`: record exact $N=0$ as conditionally closed under H4, while keeping $0<|N|\sim T$ near-collision bands open.
- `M9-M2-signed-fat-band-constant`: define and prioritize the signed off-diagonal constant $c_\chi(D;X)$.
- `M9-M2-fourth-moment-average-to-pointwise`: formalize why global fourth moments do not automatically imply pointwise `M9-M2`.
- `H4-source-audit`: give the Vaaler source-card content needed for H4, without promoting H4 until the source card is committed and validated.
- `M9-M2-interval-URES-strip-count`: use as a scoped representation-strip count, not as a full near-collision theorem.

The current reading packet states the round target obligations and do-not-claim rules: do not claim `M9` or the final target; do not treat computation as proof; do not use Li--Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.

## Main claim or direction

The correct Round 9 proof-draft direction is a bifurcated M2 program.

The fixed M2 main sum is

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D} w_D(d)e\left(\frac{hX}{4d}\right),
\qquad
H_D\asymp D X^{-1/4},
$$

with active range

$$
X^{1/4}\le D\le X^{1/2}.
$$

Under the H4 coefficient convention,

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

and

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

so the M2 coefficient is

$$
\beta_{h,H}
=
\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

in the even real convention for the two-sided $h$-sum.

The fourth-moment cleared numerator is

$$
N=
h_1d_2d_3d_4
-h_2d_1d_3d_4
+h_3d_1d_2d_4
-h_4d_1d_2d_3.
$$

The proof-draft taxonomy should now distinguish three regimes:

1. Exact resonances: $N=0$. These are conditionally controlled under H4 at total absolute mass $\ll_\epsilon D^2X^\epsilon$ by the accepted exact-$N=0$ lemmas. This does not imply pointwise M2.
2. Lower-range or structured near-collisions: $0<|N|$ in controlled bands, where interval-URES and denominator-paired structure may still give useful absolute bounds.
3. Upper-range fat-band near-collisions: especially $D>X^{3/8+\delta}$, where absolute estimates are obstructed. This range now requires a signed mechanism, with $c_\chi(D;X)$ as the primary target.

The main claim is therefore not "M2 is bounded," but rather:

**Round 9 claim.** The proof draft should replace the old full-range absolute near-collision route by a split route: exact $N=0$ closed under H4; lower-range or structured absolute subroutes retained with scoped hypotheses; upper-range analysis routed through a signed fat-band constant $c_\chi(D;X)$ plus a pointwise large-value theorem or a direct pointwise signed estimate.

Status: `derived_under_assumptions` for the source-dependent route map, `proposed` for the $c_\chi$ theorem, and `open` for pointwise `M9-M2`.

## Detailed reasoning

### 1. Proof-draft route bifurcation

The current M2 fourth-moment expansion is algebraic infrastructure, not an analytic estimate. In smoothed form, if $W$ is a fixed smooth function supported where $t\asymp X$, define

$$
\mathcal I_4(D;X)
=
\frac{1}{X}
\int
W\left(\frac{t}{X}\right)
|S_2(D;t)|^4\,dt.
$$

Expanding the fourth power gives terms of the form

$$
\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}
w(d_1)\overline{w(d_2)}w(d_3)\overline{w(d_4)}
\widehat W\left(\frac{XN}{4d_1d_2d_3d_4}\right)
e\left(\frac{XN}{4d_1d_2d_3d_4}\right),
$$

up to harmless convention-dependent conjugation choices. Since $d_i\asymp D$, the kernel is significant only in a fat band of scale

$$
|N|\lesssim \frac{D^4}{X}.
$$

The exact $N=0$ contribution has already been isolated and conditionally bounded under H4:

$$
\Sigma_{N=0}^{\mathrm{abs}}(D;X)
\ll_\epsilon D^2X^\epsilon.
$$

This exact arm should be inserted into the proof draft as conditionally closed. It should not be used to promote `M9-M2`, because `M9-M2` requires a pointwise bound for $S_2(D;X)$ at every active $X$, not merely exact-resonance bookkeeping inside a global or smoothed fourth moment.

The old absolute near-collision target was essentially

$$
\Sigma_{\mathrm{abs}}
\left(0<|N|\le \frac{D^4}{X}\right)
\ll_\epsilon D^2X^\epsilon
$$

uniformly over the full active range. The current state records this as false for $D\ge X^{3/8+\delta}$, conditional on H4 beta lower envelopes and the exact $N=0$ closure. The proof draft should therefore not present full-range absolute GNC as a target.

A safe route split is:

$$
\text{M2 fourth moment}
=
\text{exact } N=0
+
\text{lower/structured absolute near-collision}
+
\text{upper signed fat-band}.
$$

The first part is conditionally settled. The second remains class-restricted. The third is the new primary analytic target.

### 2. Missing hypotheses for the signed fat-band route

The signed fat-band route should be stated only under the following hypotheses.

1. **Frozen coefficients.** $H=H_D$ and $\beta_{h,H}$ are fixed across the $t$-integration. If $H$ is allowed to vary with $t$, then derivative and fourth-moment formulas acquire coefficient-variation terms not covered here.

2. **Dyadic weights.** For the fourth-moment identity, $w_D$ may be bounded and supported on $[D,2D]$. For the signed lift cancellation B1 input, $w_D(gq)$ must be smooth or at least bounded variation in the lift variable $g$, with a stated norm bound. Arbitrary rough complex weights are not covered by B1.

3. **Complex weights.** The fourth-moment expansion uses $w_D(d_1)\overline{w_D(d_2)}w_D(d_3)\overline{w_D(d_4)}$. Any shortcut that replaces the two-sided sum by a real part requires real weights. The complex-weight cosine pairing is a separate algebraic identity only when the same complex $w_D(d)$ is used in the $h$ and $-h$ terms.

4. **Truncation edge.** Beta lower-envelope arguments may use

$$
|\beta_{h,H}|\asymp \frac1{|h|}
$$

only for

$$
1\le |h|\le \kappa(H+1)
$$

with fixed $\kappa<1$. Frequencies near $H$ must either be excluded or handled with an upper-bound-only argument because $\Phi(u)\to0$ as $u\to1^-$.

5. **Parity support.** Since $\beta_{h,H}=0$ for even $h$, any lower-bound or diagnostic construction must choose odd $h_i$ and must verify that $N\ne0$ in off-diagonal tests.

6. **Moment scale.** The natural signed global fourth-moment conclusion is

$$
\mathcal I_4(D;X)\ll_{\epsilon,W} D^2X^\epsilon.
$$

At the endpoint $D=X^{1/2}$ this is the average fourth-moment scale $\ll X^{1+\epsilon}$ after normalization by $1/X$, but it is still not pointwise M2.

7. **Source-card discipline.** The H4 formulas remain `source_audit_required` until `sources/vaaler_1985.md` is physically updated and validated. The Vaaler anchors are Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), and Theorem 18, especially the residual inequality (7.14); the project audit also records the coefficient sign, Fejer normalization, and integer half-jump check.

8. **Li--Yang guardrail.** Li--Yang remains a source-audit comparison, not a dependency. The Round 9 prompt specifically requires checking exact theorem hypotheses and not treating reciprocal phase similarity as theorem applicability.

### 3. Exact $N=0$ arm as a closed conditional module

The exact $N=0$ module depends on:

- `H4`;
- `M9-M2-beta-algebra`;
- `M9-M2-fourth-moment-expansion`;
- `M9-M2-paired-core-weighted-bound`;
- `M9-M2-denominator-paired-weighted-bound`;
- `M9-M2-fraction-matching-weighted-bound`;
- `M9-M2-unpaired-reduced-paired-bound`;
- `M9-M2-unpaired-residual-URES`;
- `M9-M2-URES-energy-reduction`.

The module should be stated in the draft as follows.

**Exact resonance module.** Assuming H4 beta magnitude, parity support, and bounded dyadic weights, the total absolute beta-weighted mass of exact $N=0$ M2 fourth-moment tuples is

$$
\Sigma_{N=0}^{\mathrm{abs}}(D;X)
\ll_\epsilon D^2X^\epsilon
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

This is scoped strictly to exact resonances. It neither controls $0<|N|\lesssim D^4/X$ nor gives the pointwise estimate

$$
S_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This wording prevents the recurring overclaim in earlier rounds: exact resonance closure is useful but not equivalent to M2.

### 4. Why the absolute upper-range route must be replaced

The current state includes the obstruction `M9-near-collision-absolute-lower-bounds`, which says that the old full-range absolute GNC target is false in upper dyadic ranges. Its dependencies include H4, H4-Phi regularity, beta algebra, and exact $N=0$ closure. Its stated content is that the large-$M$ UNC range refutes the absolute graded estimate and the W-1 window lower bound refutes the fat-band estimate for

$$
D\ge X^{3/8+\delta}.
$$

For proof-draft purposes, the exact quantitative form does not need to be re-proved in A1's Round 9 response. What must be recorded is the logical consequence:

- An unsigned bound cannot be the main upper-range route.
- Character-blind Cauchy, Schur, Frobenius, Gershgorin, operator-norm, or absolute-value matrix bounds cannot prove the upper-range M2 fourth-moment target once they dominate by the obstructed absolute mass.
- Any upper-range fourth-moment strategy must preserve either the sign of $\beta_h$ or a structurally equivalent residue-sensitive cancellation.

The $\chi_4$ sign is not optional. In M2,

$$
\beta_{h,H}
\asymp
-\frac{\chi_4(h)}{h}
$$

on odd positive $h$ away from the truncation edge. If a proof replaces $\beta_{h,H}$ by $|\beta_{h,H}|$ in the upper fat band, it has moved into the obstructed route.

### 5. Exact frozen-kernel fourth moment

Use the convention $e(u)=e^{2\pi i u}$. Fix a base scale $X$, an active dyadic denominator block

$$
X^{1/4}\le D\le X^{1/2},
$$

and a frozen Vaaler height

$$
H=H_D\asymp D X^{-1/4}.
$$

All coefficients below are frozen at this base $X,D,H$ while the moment variable $t$ ranges over $t\asymp X$. Define the normalized M2 block without the harmless outer factor $4$ by

$$
S_2(D;t)
=
\sum_{1\le |h|\le H}
\beta_{h,H}
\sum_{d\ge1} w_D(d)e\left(\frac{ht}{4d}\right),
$$

where $w_D$ is supported on $d\asymp D$. The actual M2 term in the proof draft is $4S_2(D;X)$, so constants in fourth moments change by $4^4$ only.

Under H4,

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

The M2 frequency factor is

$$
C_h=e(h/4)-e(3h/4),
$$

and for odd $h$,

$$
C_h=2i\chi_4(h),
\qquad
C_h=0 \quad (2\mid h).
$$

After multiplying by $\alpha_{h,H}$, the even two-sided coefficient is

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
\qquad
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

The sign in the last formula is important: the parity sign retained in M2 is $\chi_4(|h|)$ after the $\alpha_h$ sign from $h^{-1}$ is included.

Let $W\in C_c^\infty((1/2,2))$ be fixed. Define the normalized global fourth moment by

$$
\mathcal I_4(D;X)
=
\frac1X
\int_{\mathbb R}
W(t/X)|S_2(D;t)|^4\,dt.
$$

With Fourier transform

$$
\widehat W(\xi)=\int_{\mathbb R}W(u)e(-\xi u)\,du,
$$

the exact expansion is

$$
\mathcal I_4(D;X)
=
\sum_{\substack{
1\le |h_i|\le H\\
d_i\asymp D
}}
\beta_{h_1,H}\beta_{h_2,H}\beta_{h_3,H}\beta_{h_4,H}
w_D(d_1)\overline{w_D(d_2)}w_D(d_3)\overline{w_D(d_4)}
\widehat W\left(-\frac{X\,N(\mathbf h,\mathbf d)}{4Q(\mathbf d)}\right),
$$

where

$$
Q(\mathbf d)=d_1d_2d_3d_4,
$$

and

$$
N(\mathbf h,\mathbf d)
=
h_1d_2d_3d_4
-h_2d_1d_3d_4
+h_3d_1d_2d_4
-h_4d_1d_2d_3.
$$

This corrects a weakness in my earlier wording: there is no additional factor $e(XN/4Q)$ in this $W(t/X)$ normalization. Such a phase appears only if the averaging kernel is translated, for example $W((t-X)/L)$; then it must be derived from that shifted kernel and not inserted by convention.

The kernel is significant on the natural fat band

$$
\left|\frac{X\,N}{4Q}\right|\lesssim 1,
\qquad\text{so}\qquad
|N|\lesssim \frac{D^4}{X},
$$

with rapidly decaying tails controlled by the smoothness of $W$. A hard cutoff estimate for $|N|\le cD^4/X$ is therefore only a diagnostic proxy unless the tails are separately bounded.

### 6. State-ready definition of $c_\chi(D;X;W)$

Define the exact-resonance mass

$$
\mathcal C_0(D;X;W)
=
\widehat W(0)
\sum_{\substack{
1\le |h_i|\le H\\
d_i\asymp D\\
N(\mathbf h,\mathbf d)=0
}}
\beta_{h_1,H}\beta_{h_2,H}\beta_{h_3,H}\beta_{h_4,H}
w_D(d_1)\overline{w_D(d_2)}w_D(d_3)\overline{w_D(d_4)}.
$$

Define the signed off-diagonal kernel contribution

$$
\mathcal C_\chi(D;X;W)
=
\sum_{\substack{
1\le |h_i|\le H\\
d_i\asymp D\\
N(\mathbf h,\mathbf d)\ne0
}}
\beta_{h_1,H}\beta_{h_2,H}\beta_{h_3,H}\beta_{h_4,H}
w_D(d_1)\overline{w_D(d_2)}w_D(d_3)\overline{w_D(d_4)}
\widehat W\left(-\frac{X\,N(\mathbf h,\mathbf d)}{4Q(\mathbf d)}\right).
$$

Then

$$
\mathcal I_4(D;X)=\mathcal C_0(D;X;W)+\mathcal C_\chi(D;X;W).
$$

The normalized signed fat-band constant should be recorded as

$$
c_\chi(D;X;W)=D^{-2}\mathcal C_\chi(D;X;W).
$$

The target is

$$
|c_\chi(D;X;W)|\ll_{\epsilon,W}X^\epsilon
$$

uniformly at least for

$$
X^{3/8+\eta}\le D\le X^{1/2}.
$$

The corresponding unsigned diagnostic is

$$
c_{\mathrm{abs}}(D;X;W)
=
D^{-2}
\sum_{\substack{
1\le |h_i|\le H\\
d_i\asymp D\\
N(\mathbf h,\mathbf d)\ne0
}}
|\beta_{h_1,H}\beta_{h_2,H}\beta_{h_3,H}\beta_{h_4,H}|
|w_D(d_1)w_D(d_2)w_D(d_3)w_D(d_4)|
\left|
\widehat W\left(-\frac{X\,N}{4Q}\right)
\right|.
$$

The proof draft should say explicitly:

$$
c_{\mathrm{abs}}(D;X;W)\ll X^\epsilon
$$

is not a viable full-range target, because the existing state records upper-range absolute lower-bound obstructions for $D\ge X^{3/8+\delta}$. The signed $c_\chi$ target is not a cosmetic variant of the absolute target; it is a different theorem that must use the product of the actual $\chi_4(|h_i|)$ signs. The state already asks for the exact frozen-coefficient identity and unsigned analogue for `M9-M2-signed-fat-band-constant`.

### 7. Interval URES strip count is scoped arithmetic only

The interval URES strip count should be used only in the following restricted form.

For fixed reduced $\mu/Q\ne0$, fixed nonzero $p_1,p_3$, $Q\le4D^2$, $|p_i|\le2H_D$, $0\le\eta\le4X^{-1/4}$, and $q_i\in[1,2D]$ with $(p_i,q_i)=1$, the accepted count is

$$
\#\left\{(q_1,q_3):
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|\le\eta
\right\}
\ll_\epsilon
X^\epsilon(1+\eta QD^2)+\Delta,
$$

where

$$
\Delta\le4D\,1_{\eta\ge1/(2D)}.
$$

The state explicitly says this is a representation-strip count, not a full M2 near-collision estimate.

The missing assembly steps are:

1. identify $\mu/Q$ as the reduced value of the opposite pair sum, usually $h_2/d_2+h_4/d_4$;
2. map the M2 near-collision condition

$$
\left|
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right|
\lesssim \frac1X
$$

into a strip width $\eta\asymp X^{-1}$ or a slightly enlarged dyadic width;
3. sum over numerator data $p_1,p_3$;
4. sum over the dyadic lift variables $g_i$ in $h_i=g_ip_i$, $d_i=g_iq_i$;
5. insert the beta weights and parity restrictions;
6. classify the degenerate branch $\Delta$ before using the nondegenerate count.

Until these six steps are complete, interval URES is `proved_internal` arithmetic infrastructure only. It should not be cited as a near-collision theorem.

### 8. H4 source audit and source-card draft

The H4 source card should contain the following.

**Bibliographic metadata.**

- Author: Jeffrey D. Vaaler.
- Title: "Some extremal functions in Fourier analysis."
- Journal: *Bulletin of the American Mathematical Society (New Series)*.
- Volume/issue/pages: 12(2), 183--216.
- Date: April 1985.
- DOI: `10.1090/S0273-0979-1985-15349-2`.
- Local file: `/mnt/data/[Vaaler] Some extremal functions in Fourier analysis_Bull. Amer. Math. Soc..pdf`.

The AMS metadata gives the DOI and bibliographic data.

**Fourier transform anchor.**

Vaaler Theorem 6 gives

$$
\widehat J(t)=
\begin{cases}
1,&t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|,&0<|t|<1,\\
0,&1\le |t|.
\end{cases}
$$

The local PDF parsed text places this as equation (2.28), and the rendered page is printed page 192.

Define

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
$$

Then the Vaaler coefficient for the sawtooth polynomial is

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
1\le |h|\le H.
$$

The sign is negative because the arithmetic sawtooth

$$
\psi_F(t)=\{t\}-\frac12
$$

has Fourier coefficient

$$
-\frac{1}{2\pi i h}
$$

for $h\ne0$.

**Section 7 definitions.**

Section 7 defines periodic trigonometric polynomials $i_N$, $j_N$, and $k_N$ in equations (7.1)--(7.3). The kernel $k_N$ is the periodic Fejer kernel. In repo notation,

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(\frac{\sin \pi(H+1)t}{\sin\pi t}\right)^2,
$$

with

$$
K_H(0)=H+1.
$$

**Theorem 18 residual.**

Vaaler Theorem 18 states that the trigonometric polynomial $\psi*j_N$ satisfies equations (7.13)--(7.15), including the residual inequality

$$
|\psi*j_N(x)-\psi(x)|
\le
(2N+2)^{-1}k_N(x).
$$

In repo notation with $H=N$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht)
+
R_H^F(t),
$$

and

$$
|R_H^F(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

**Endpoint convention.**

Vaaler's normalized periodic sawtooth has value $0$ at integers. The arithmetic proof uses

$$
\psi_F(n)=-\frac12.
$$

At integers, the Vaaler polynomial is symmetric and gives $0$, while

$$
\frac{1}{2H+2}K_H(0)=\frac{H+1}{2H+2}=\frac12.
$$

Thus the Fejer residual majorant exactly covers the floor-compatible half-jump.

**$\Phi$ regularity.**

From

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

we get the endpoint expansions

$$
\Phi(u)=1-\frac{\pi^2}{3}u^2+O(u^3)
\qquad (u\to0),
$$

and

$$
\Phi(1-v)=O(v^2)
\qquad (v\to0^+).
$$

Thus $\Phi$ extends continuously to

$$
\Phi(0)=1,\qquad \Phi(1)=0,
$$

with one-sided endpoint derivative $0$ at both endpoints. Vaaler's Theorem 6 also states nonnegativity and monotonicity of $\widehat J$ on $[0,1]$, which gives the coefficient lower envelope away from the truncation edge.

For every fixed $0<\kappa<1$, there is $c_\kappa>0$ such that

$$
\Phi(u)\ge c_\kappa
\qquad
(0\le u\le \kappa).
$$

Therefore for odd $h$ with $1\le |h|\le \kappa(H+1)$,

$$
|\beta_{h,H}|
\ge
\frac{c_\kappa}{\pi |h|}.
$$

This lower envelope is a dependency of the absolute near-collision lower-bound obstruction and must stay conditional on H4 until the source card is validated.

**M2 parity support.**

The M2 frequency factor is

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h}.
$$

Thus even $h$ vanish and odd $h$ carry the residue sign $\chi_4(h)$. This is the algebraic reason character-blind upper-range estimates are unsafe.

I would mark the H4 source audit as source-card-ready but still `source_audit_required` until the repo file `sources/vaaler_1985.md` is physically updated and validator-checked.

### 9. Li--Yang theorem audit as guardrail only

Li--Yang's theorem-level object is the double sum

$$
S
=
\sum_{H\le h\le 2H}
g\left(\frac{h}{H}\right)
\sum_{M\le m\le 2M}
G\left(\frac{m}{M}\right)
e\left(\frac{hT}{M}F\left(\frac{m}{M}\right)\right),
$$

with $g,G$ of bounded variation and $F\in C^3([1,2])$. The derivative hypotheses are

$$
C_r\ge |F^{(r)}(x)|\ge C_r^{-1}
\qquad (r=1,2,3),
$$

and

$$
|F^{(1)}(x)F^{(3)}(x)-3F^{(2)}(x)^2|
\ge C_4^{-1}.
$$

The main theorem applies in Case A or Case B, with additional range conditions, and yields the simplified target

$$
\frac{S}{H}
\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\ldots.
$$

The final reduction in their paper chooses Fourier height

$$
Y=MT^{-\theta^*}.
$$

For the present Vaaler endpoint route, the local Vaaler height is

$$
H_D\asymp D X^{-1/4}.
$$

The Li--Yang height corresponding to the record exponent is

$$
H\le M T^{-\theta^*}.
$$

Since

$$
\theta^*>1/4,
$$

the Li--Yang height is smaller than the endpoint Vaaler height by a power

$$
T^{-(\theta^*-1/4)}.
$$

At the upper endpoint $D=X^{1/2}$, the current M9 block requires height

$$
H_D\asymp X^{1/4},
$$

whereas a record-exponent Fourier truncation would only reach

$$
X^{1/2-\theta^*}
=
X^{0.185516\ldots}.
$$

Therefore Li--Yang is not a black-box theorem for the current endpoint M9 problem. It remains useful for comparison of phase classes, Case A/B restrictions, and Bombieri--Iwaniec spacing architecture. The official arXiv page confirms the version and abstract-level method description, but theorem compatibility must be judged from the TeX hypotheses, not from phase similarity.

### 10. Pointwise upgrade and large-value gap

The earlier derivative obstruction was correct in scale but the large-value theorem I stated was too blunt. The pointwise-upgrade gap should be recorded in two parts.

First, the crude derivative bound is

$$
S_2'(D;t)
=
\frac{2\pi i}{4}
\sum_{1\le |h|\le H}
\beta_{h,H}
\sum_{d\asymp D}
w_D(d)\frac{h}{d}e\left(\frac{ht}{4d}\right),
$$

so, using $|\beta_{h,H}|\ll1/|h|$ and $d\asymp D$,

$$
\sup_{t\asymp X}|S_2'(D;t)|
\ll
\sum_{1\le |h|\le H}
\frac1{|h|}
\sum_{d\asymp D}\frac{|h|}{D}
\ll H
\asymp D X^{-1/4}.
$$

Let

$$
B_D:=C D X^{-1/4}.
$$

Assume a signed global fourth moment gives the normalized estimate

$$
\frac1X\int_X^{2X}|S_2(D;t)|^4\,dt
\ll_\epsilon D^2X^\epsilon.
$$

Equivalently,

$$
\int_X^{2X}|S_2(D;t)|^4\,dt
\ll_\epsilon X D^2X^\epsilon.
$$

If $|S_2(D;X_0)|=V$, the derivative bound gives an interval of length $\gg V/B_D$ on which $|S_2|\gg V$, unless this length is comparable with the whole $X$-interval. In either case the elementary propagation argument gives at best

$$
V^5/B_D
\ll_\epsilon
X D^2X^\epsilon,
$$

hence

$$
V
\ll_\epsilon
(B_DXD^2)^{1/5}X^\epsilon
\ll
D^{3/5}X^{3/20+\epsilon}.
$$

At $D=X^{1/2}$ this is

$$
V\ll X^{9/20+\epsilon},
$$

which is far weaker than $X^{1/4+\epsilon}$. This is exactly why `M9-M2-fourth-moment-average-to-pointwise` remains open; the state already records this obstruction and requires a stronger large-value, local signed cancellation, or direct pointwise theorem.

Second, a sufficient large-value theorem should be stated in derivative-compatible form, not as an ordinary global fourth moment. One sufficient theorem is:

**Proposed large-value theorem LV.** Fix $\eta>0$. For every active $D$, every threshold

$$
V\ge X^{1/4+\eta},
$$

and every set $\mathcal X\subset[X,2X]$ such that

$$
|S_2(D;X_j)|\ge V
\quad (X_j\in\mathcal X)
$$

and

$$
|X_i-X_j|\ge c\,\frac{V}{B_D}
\quad (i\ne j),
$$

prove that for some $\kappa>0$,

$$
\#\mathcal X
\ll_{\epsilon,\eta}
X^\epsilon
\frac{B_DX}{V^5}
\left(\frac{X^{1/4}}{V}\right)^\kappa.
$$

This theorem would imply pointwise M2. Indeed, if one point $X_0$ has $|S_2(D;X_0)|=V\ge X^{1/4+\eta}$, then $\#\mathcal X=1$ is admissible, and

$$
V^{5+\kappa}
\ll_{\epsilon,\eta}
B_DX\,X^{\kappa/4+\epsilon}.
$$

Since $B_D\ll X^{1/4}$ in the full active range,

$$
V^{5+\kappa}
\ll
X^{5/4+\kappa/4+\epsilon},
$$

so

$$
V\ll_{\epsilon,\eta}X^{1/4+\epsilon}.
$$

This formulation is stronger and cleaner than saying "global fourth moment plus a threshold saving." It identifies the exact missing object: a separated large-value count with a $V^{-5}$ derivative-compatible scale and an additional threshold saving.

## Route proposals

### Route 1: signed fat-band constant plus large-value theorem

**Exact lemma.**

Define $c_\chi(D;X)$ as above and prove

$$
|c_\chi(D;X)|\ll_\epsilon X^\epsilon
$$

uniformly for

$$
X^{3/8+\eta}\le D\le X^{1/2}.
$$

Then prove a large-value theorem: for every threshold $V\ge X^{1/4+\eta}$ and every $\rho(D,V)$-separated set $\mathcal X\subset[X,2X]$ of $V$-large points,

$$
\sum_{X_j\in\mathcal X}|S_2(D;X_j)|^4
\ll_{\epsilon,\eta}
X^{1+\epsilon}
\left(\frac{X^{1/4}}{V}\right)^\kappa
$$

for some $\kappa>0$.

**Why it might work.**

The W-1 and UNC lower bounds obstruct unsigned mass, not signed mass. The coefficient

$$
\beta_h\asymp-\frac{\chi_4(h)}{h}
$$

creates cancellation in dyadic lifts. The accepted B1 envelope

$$
|A_\chi(p/q)|\ll \frac{q}{D|p|}
$$

is a plausible first saving after reduction to rational pair weights.

**Obstruction attacked.**

This route directly attacks `M9-M2-character-factor` and the upper-range obstruction in `M9-near-collision-absolute-lower-bounds`.

**Dependencies.**

- H4 and H4-source-audit.
- H4-Phi-regularity.
- M9-M2-beta-algebra.
- M9-M2-signed-lift-cancellation-B1.
- M9-M2-fourth-moment-expansion.
- A new large-value theorem.

**First proof step.**

Write the smoothed fourth moment in reduced-fraction variables and prove a precise identity of the form

$$
\mathcal C_\chi(D;X)
=
D^2
\sum_{\mathrm{strip}}
A_\chi(x_1)A_\chi(x_3)
\overline{A_\chi(x_2)A_\chi(x_4)}
K_X(x_1+x_3-x_2-x_4)
+
\mathrm{Err},
$$

where $K_X$ is the fat-band kernel induced by $\widehat W$.

**Quick falsification test.**

A2 should compute $c_\chi(D;X)$ through AI Studio Code Execution when available, with Codex/local reproduction before evidence is positive; A3 should audit the script and interpretation. The diagnostic should compare signed, unsigned, random-sign, and adversarial-sign analogues at $D=X^{3/8+\eta}$ and $D=X^{1/2}$. If the signed value has the same scale and sign stability as the unsigned mass, B1 is probably insufficient and the route needs an additional cancellation mechanism.

**Plausibility rank.**

Highest proof-graph impact; moderate current evidence; open analytic difficulty.

### Route 2: lower-range structured absolute estimate via interval URES

**Exact lemma.**

For $D\le X^{3/8+o(1)}$, prove a restricted absolute estimate for nondegenerate interval-URES near-collisions:

$$
\Sigma_{\mathrm{URES,nd}}^{\mathrm{abs}}
\left(0<|N|\le \frac{D^4}{X}\right)
\ll_\epsilon D^2X^\epsilon
$$

or a weaker bound still sufficient for the global fourth-moment target in that range.

**Why it might work.**

The interval-URES strip count gives

$$
\#\{(q_1,q_3): |p_1/q_1+p_3/q_3-\mu/Q|\le\eta\}
\ll_\epsilon X^\epsilon(1+\eta QD^2)+\Delta,
$$

with a separated degenerate branch. In lower ranges, the strip width and lift multiplicities may remain below the obstruction threshold.

**Obstruction attacked.**

This route attacks the lower-range part of `M9-near-collision-taxonomy` and preserves useful absolute counting where the W-1 upper-range obstruction does not apply.

**Dependencies.**

- M9-M2-interval-URES-strip-identity.
- M9-M2-interval-URES-strip-count.
- M9-M2-URES-energy-reduction.
- H4 beta magnitude.
- Degenerate branch classification.

**First proof step.**

Fix reduced numerator data $(p_1,p_3)$ and central reduced value $\mu/Q$. Apply the strip count, then sum over dyadic lift variables using the beta weight envelope. Keep the degenerate branch separate and map it into paired or participation-degenerate classes.

**Quick falsification test.**

If the degenerate branch contributes $\gg D^2X^\eta$ before signed cancellation even for $D\le X^{3/8}$, then this route must be further narrowed to nondegenerate classes or abandoned as an absolute route.

**Plausibility rank.**

Useful as a lower-range/class-restricted subroute; not enough for endpoint M2 because upper range remains signed.

### Route 3: sign-preserving Poisson/B-process route

**Exact lemma.**

Prove a smooth stationary-phase transform for

$$
\sum_{d\asymp D}w_D(d)e\left(\frac{hX}{4d}\right)
$$

that is uniform for

$$
1\le |h|\le H_D,
\qquad
X^{1/4}\le D\le X^{1/2},
$$

including boundary, $k=0$, nonstationary, and support-edge terms. Then prove the resulting dual signed sum satisfies

$$
\sum_h \beta_h \mathcal B_h(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

**Why it might work.**

At the upper endpoint, the dual length

$$
m\asymp \frac{hX}{D^2}
$$

is comparable to $X^{1/4}$ at maximal $h$, so the transform does not collapse to a trivial one-term model. There may be a residue character in the dual variable.

**Obstruction attacked.**

This route attacks pointwise `M9-M2` directly and bypasses the fourth-moment average-to-pointwise gap.

**Dependencies.**

- A complete B-process theorem with explicit constants and smooth weights.
- Preservation of $\chi_4$ after the transform.
- A signed dual spacing theorem.

**First proof step.**

Derive the exact stationary phase with phase

$$
\phi_m(u)=\frac{hX}{4u}-mu
$$

or the appropriate modulo-normalized variant, and record the stationary point and amplitude uniformly in $h,D,X$.

**Quick falsification test.**

If the first Cauchy or large-sieve step puts the dual character only into a diagonal unitary conjugation and then uses an operator norm, Schur bound, Frobenius bound, or absolute-value matrix bound, the character has been erased and the route has reverted to a character-blind estimate.

**Plausibility rank.**

Valuable backup; lower immediate proof-graph safety because the stationary-phase theorem and post-transform signed estimate are both missing.

## Theorem-dependency audit

1. **H1-H3.** Status `proved_internal`. These reductions remain accepted, with endpoint conventions visible.

2. **H4.** Status `source_audit_required`. The Vaaler theorem content is now source-card-ready, but H4 should not be promoted until `sources/vaaler_1985.md` is updated and validated.

3. **R5-Full.** Status `derived_under_assumptions`. The residual product-count bound remains conditional on H4. It is not part of the current M2 bottleneck, except as a bridge dependency.

4. **M9-M2-beta-algebra.** Status `derived_under_assumptions`. The beta formula depends on H4 coefficient normalization.

5. **M9-M2-exact-N0-total-mass.** Status `derived_under_assumptions`. It controls exact resonances only and depends on H4.

6. **M9-near-collision-absolute-lower-bounds.** Status `derived_under_assumptions`. It blocks the old upper-range absolute route under H4 beta lower-envelope assumptions.

7. **M9-M2-signed-lift-cancellation-B1.** Status `derived_under_assumptions`. It gives a pair-weight saving but does not prove $c_\chi$ or M2.

8. **M9-M2-signed-fat-band-constant.** Status `proposed`. It needs a precise identity, a proof, or a signed lower-bound obstruction.

9. **M9-M2-fourth-moment-average-to-pointwise.** Status `open`. The derivative obstruction shows global L4 plus crude derivative is insufficient.

10. **Li-Yang-source-audit.** Status `source_audit_required`. Li--Yang is a comparison theorem and guardrail only. The arXiv record and TeX source confirm the theorem object and version, but endpoint M9 compatibility is not established.

## Hidden assumptions and potential gaps

1. **H4 source-card gap.** The mathematical source audit is source-card-ready, but state promotion requires the physical source card to contain metadata, theorem anchors, and notation translation.

2. **Beta lower envelope.** The lower-bound obstruction requires a positive lower envelope for $\Phi$ away from the truncation edge. This is valid only for $|h|\le\kappa(H+1)$ with fixed $\kappa<1$; edge frequencies require separate treatment.

3. **Dyadic weight regularity.** The signed lift cancellation B1 depends on smooth or bounded-variation dyadic weights. It may fail for arbitrary rough weights unless the proof inserts a smoothing partition or proves a BV summation-by-parts variant.

4. **Frozen coefficients.** Local or global $X$-averaging must keep the Vaaler height $H_D$ and coefficients frozen. If $H_D$ varies with $t$, derivative and moment formulas acquire coefficient-variation terms.

5. **Complex weights.** The cosine pairing is valid for shared complex $d$-weights in the $h$ and $-h$ terms, but the $\operatorname{Re}B_h$ shortcut is valid only under real-weight hypotheses. This remains an A2/Codex regression target with A3 audit.

6. **Interval URES degeneracy.** The degenerate branch $\Delta$ in the strip count can be large enough to matter. It is not safe to sum the nondegenerate estimate and ignore $\Delta$.

7. **Large-value theorem missing.** A signed global fourth moment is not enough. The large-value theorem or a direct pointwise proof remains a hard missing ingredient.

8. **Endpoint $D=X^{1/2}$.** At the endpoint, local averaging windows degenerate and many spacing kernels lose power-scale discrimination. Any route must explicitly isolate this case.

9. **Li--Yang compatibility.** The phase shape resembles reciprocal sums, but the height range and theorem hypotheses do not match the endpoint Vaaler M9 target.

10. **No M1 estimate.** This response focuses on M2. `M9` cannot advance unless `M9-M1` is also proved uniformly.

## Counterexample or obstruction search

### Obstruction 1: character-blind absolute domination

If a proposed proof of $c_\chi$ begins from

$$
|\mathcal C_\chi(D;X)|
\le
\mathcal C_{\mathrm{abs}}(D;X),
$$

then it is immediately in the obstructed route for $D>X^{3/8+\delta}$. The proof draft should mark this as a failed upper-range step.

### Obstruction 2: diagonal unitary erasure

In any matrix model, if the $\chi_4$ signs appear only as

$$
K_\chi=U^*KU
$$

for a diagonal unitary $U$, then

$$
\|K_\chi\|=\|K\|
$$

and operator-norm estimates are character-blind. This does not prove the route false, but it falsifies that specific norm step as a sign-preserving mechanism.

### Obstruction 3: derivative propagation spike

A single spike of height

$$
V=D^{3/5}X^{3/20}
$$

is compatible with the global fourth-moment scale and the crude derivative bound. At $D=X^{1/2}$ this is $X^{9/20}$, so a proof that only combines global L4 and $|S'|\ll H_D$ cannot prove M2.

### Obstruction 4: URES degenerate branch

The interval URES strip count includes

$$
\Delta\le4D\,1_{\eta\ge1/(2D)}.
$$

In upper or borderline ranges, this branch may dominate a fixed-numerator strip count after lift summation. It must be mapped into taxonomy classes before any absolute estimate is claimed.

### Obstruction 5: beta truncation edge

Lower-bound and signed-cancellation arguments using

$$
|\beta_h|\asymp 1/|h|
$$

must avoid $h$ near $H_D$, where $\Phi(|h|/(H_D+1))$ can be small. If an obstruction construction uses edge frequencies, it needs a separate lower envelope or must be restricted to $h\le\kappa H_D$.

### Obstruction 6: Li--Yang height mismatch

Li--Yang's final Fourier height is $Y=MT^{-\theta^*}$ with $\theta^*>1/4$, whereas endpoint Vaaler uses $H_D\asymp DX^{-1/4}$. The height mismatch alone prevents black-box import for M9.

## Verification

The following items were verified in this reasoning pass.

1. The prompt explicitly assigns the route bifurcation, H4 source audit, pointwise upgrade gap, and interval-URES scoping to A1.

2. The reading packet identifies `M9` as open and lists the round target obligations `M9-M2-character-factor`, `M9-near-collision-taxonomy`, and `M9-regression-raw-vs-paired`.

3. Vaaler metadata and DOI are available from AMS search output.

4. The local Vaaler PDF contains Theorem 6 equation (2.28) and Theorem 18 equations (7.13)--(7.17), including the residual inequality (7.14).

5. The arXiv page confirms Li--Yang arXiv:2308.14859, v2 dated 14 September 2023, title, authors, DOI, and method summary.

6. The Li--Yang TeX audit identifies `\label{definition of S}`, `\label{condition on F 1}`, `\label{condition on F 2}`, Case A/B definitions, `\label{main theorem}`, and `\label{goal}`.

7. The derivative obstruction formula

$$
V\ll D^{3/5}X^{3/20+\epsilon}
$$

follows from

$$
\int |S_2|^4\ll D^2X^{1+\epsilon},
\qquad
|S_2'|\ll H_D\asymp DX^{-1/4}.
$$

8. The proposed large-value theorem with a threshold saving $\kappa>0$ would imply the target pointwise bound for any nonempty set of large values.

## Divergent alternatives and 20% exploration

### Alternative A: direct signed reciprocal discrepancy theorem

Instead of proving $c_\chi$ and then a large-value theorem, one could formulate a direct discrepancy theorem for the signed truncated sawtooth values at reciprocal points:

$$
\theta_d^{(\rho)}=\frac{X/d+\rho}{4},
\qquad
\rho\in\{1,3\}.
$$

The M2 sum is equivalent to a difference of two Vaaler-polynomial sums at $\theta_d^{(1)}$ and $\theta_d^{(3)}$:

$$
e\left(\frac{hX}{4d}\right)
(e(h/4)-e(3h/4))
=
e\left(h\theta_d^{(1)}\right)
-
e\left(h\theta_d^{(3)}\right).
$$

A direct theorem could be:

For every active $D$,

$$
\sum_{d\asymp D}w_D(d)
\left[
V_{H_D}\left(\frac{X/d+1}{4}\right)
-
V_{H_D}\left(\frac{X/d+3}{4}\right)
\right]
\ll_\epsilon X^{1/4+\epsilon}.
$$

This would imply M2 directly. It attacks the character factor without fourth moments. Its quick falsification test is to compare actual signed discrepancy against unsigned and random-shift discrepancy. If the signed discrepancy has no visible gain and no residue-structured cancellation, this route likely needs new input.

### Alternative B: Mellin-Perron comparison route

A Mellin-Perron approach would start from

$$
\sum_{n\le X}r_2(n)
=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\mathrm{Err}.
$$

The conjectural target would require shifting close to $\Re s=1/4$ with Lindelof-strength control for $\zeta(s)L(s,\chi_4)$ in the critical strip, plus sharp truncation and residue analysis. This route is unlikely to be easier, but it is a useful calibration: if the Vaaler route starts importing estimates as strong as subconvexity/Lindelof for the product, the proof draft should say so.

A quick falsification test is to compute the convexity/subconvexity strength needed on the shifted contour. If it is equivalent to or stronger than the target Gauss exponent, the route is a comparison module rather than a proof route.

### Alternative C: Poisson/B-process endpoint toy model

At $D=X^{1/2}$ and $h\asymp H_D=X^{1/4}$, the dual length in a B-process model is

$$
m\asymp \frac{hX}{D^2}\asymp X^{1/4}.
$$

Thus the dual problem has comparable height to the $h$ variable. A toy endpoint model is

$$
\sum_{h\asymp X^{1/4}}\frac{\chi_4(h)}{h}
\sum_{m\asymp X^{1/4}}
a_m e(c\sqrt{hXm}).
$$

The continuous Hessian of $\sqrt{hm}$ is rank-deficient, so generic two-dimensional full-rank stationary phase or decoupling is not directly applicable. The route needs residue-sensitive one-dimensional structure or a non-conjugacy signed statistic.

Quick falsification: after the first Cauchy step, check whether $\chi_4$ survives outside a diagonal unitary. If not, the toy model has reproduced the Q1 character-blind obstruction.

## Useful lemmas

### Lemma 1: H4 coefficient and residual formula

Assuming Vaaler Theorem 18 and Theorem 6 in the source-normalized convention,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht)+R_H^F(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

and

$$
|R_H^F(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

Status: `source_audit_required` until source card validation.

### Lemma 2: M2 beta parity formula

Under H4,

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h},
$$

and

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}
$$

in the even two-sided convention.

Status: `derived_under_assumptions`.

### Lemma 3: exact $N=0$ closure module

Assuming H4 beta magnitude, parity support, and bounded dyadic weights,

$$
\Sigma_{N=0}^{\mathrm{abs}}(D;X)
\ll_\epsilon D^2X^\epsilon
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

Status: `derived_under_assumptions`; scope exact resonances only.

### Lemma 4: derivative obstruction

If

$$
\int_X^{2X}|S_2(D;t)|^4\,dt
\ll_\epsilon D^2X^{1+\epsilon}
$$

and

$$
|S_2'(D;t)|\ll_\epsilon D X^{-1/4+\epsilon},
$$

then the elementary local propagation argument gives only

$$
|S_2(D;X_0)|
\ll_\epsilon
D^{3/5}X^{3/20+\epsilon}.
$$

At $D=X^{1/2}$ this is

$$
X^{9/20+\epsilon}.
$$

Status: obstruction; supports `M9-M2-fourth-moment-average-to-pointwise`.

### Lemma 5: separated large-value pointwise upgrade

Let $S_2(D;t)$ be the frozen-coefficient block and set $B_D=C D X^{-1/4}$. A sufficient pointwise-upgrade theorem would control all $V$-large points separated by $\gg V/B_D$ with a saving beyond the crude global fourth-moment bound. Equivalently, for $V\ge X^{1/4+\eta}$, one needs a threshold-saving large-value inequality strong enough to rule out isolated endpoint spikes. This remains proposed and unproved; it is not a consequence of the signed global fourth moment alone.

### Lemma 6: scoped interval URES count

The interval URES strip count should be used only in the following restricted form.

For fixed reduced $\mu/Q\ne0$, fixed nonzero $p_1,p_3$, $Q\le4D^2$, $|p_i|\le2H_D$, $0\le\eta\le4X^{-1/4}$, and $q_i\in[1,2D]$ with $(p_i,q_i)=1$, the accepted count is

$$
\#\left\{(q_1,q_3):
\left|
\frac{p_1}{q_1}+\frac{p_3}{q_3}-\frac{\mu}{Q}
\right|\le\eta
\right\}
\ll_\epsilon
X^\epsilon(1+\eta QD^2)+\Delta,
$$

where

$$
\Delta\le4D\,1_{\eta\ge1/(2D)}.
$$

The state explicitly says this is a representation-strip count, not a full M2 near-collision estimate.

The missing assembly steps are:

1. identify $\mu/Q$ as the reduced value of the opposite pair sum, usually $h_2/d_2+h_4/d_4$;
2. map the M2 near-collision condition

$$
\left|
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right|
\lesssim \frac1X
$$

into a strip width $\eta\asymp X^{-1}$ or a slightly enlarged dyadic width;
3. sum over numerator data $p_1,p_3$;
4. sum over the dyadic lift variables $g_i$ in $h_i=g_ip_i$, $d_i=g_iq_i$;
5. insert the beta weights and parity restrictions;
6. classify the degenerate branch $\Delta$ before using the nondegenerate count.

Until these six steps are complete, interval URES is `proved_internal` arithmetic infrastructure only. It should not be cited as a near-collision theorem.

## What should be tested next

### Test 1: exact fourth-moment formula regression

Compute $\mathcal I_4(D;X)$ two ways for small exact integer data:

$$
\frac1X\int W(t/X)|S_2(D;t)|^4\,dt
$$

by numerical quadrature, and the exact expanded sum

$$
\sum \beta_1\beta_2\beta_3\beta_4
w_1\overline{w_2}w_3\overline{w_4}
\widehat W\left(-\frac{XN}{4Q}\right).
$$

This test fails the formula if an extra phase $e(XN/4Q)$ is present under the unshifted $W(t/X)$ convention.

### Test 2: signed versus unsigned fat-band ratio

For $D=X^\delta$ with $\delta$ near $3/8$ and $1/2$, compute

$$
|c_\chi(D;X;W)|,
\qquad
c_{\mathrm{abs}}(D;X;W),
$$

and compare with random-sign and adversarial-sign versions. If

$$
|c_\chi|\asymp c_{\mathrm{abs}}
$$

persistently in upper ranges, then B1 signed lift cancellation is insufficient as a standalone route.

### Test 3: edge-frequency exclusion

Repeat Test 2 with

$$
|h_i|\le \kappa H
$$

for fixed $\kappa<1$, and compare with the full $|h_i|\le H$. If the only saving comes from the $\Phi$ cutoff near $H$, then the route is not exploiting robust $\chi_4$ cancellation.

### Test 4: B1 lift-weight regularity

For the reduced lift weight

$$
A_\chi(p/q)=
\sum_{\substack{gq\asymp D\\1\le |gp|\le H}}
\beta_{gp,H}w_D(gq),
$$

test smooth, bounded-variation, and deliberately rough lift weights. If

$$
|A_\chi(p/q)|\ll q/(D|p|)
$$

fails for the weight class used in the fourth moment, the B1 input must be narrowed before it can support $c_\chi$.

### Test 5: URES degenerate branch saturation

Choose strip widths with $\eta\ge1/(2D)$ and enumerate the branch giving

$$
\Delta\le4D.
$$

If after numerator and lift summation the degenerate branch contributes above $D^2X^\epsilon$ in a proposed lower-range absolute estimate, interval URES must be restricted to nondegenerate classes or made signed.

### Test 6: pointwise spike compatibility

Numerically find large local maxima of $|S_2(D;t)|$ and measure the local width on which $|S_2|\ge V/2$. Compare with $V/B_D$. If isolated spikes saturate the derivative lower width but not any stronger separated large-value count, then global signed fourth moments alone cannot prove M2.

### Test 7: Poisson/B-process sign survival

After any B-process transform, track whether the $\chi_4$ factor survives as a non-conjugacy statistic. If the next estimate has the form

$$
K_\chi=U^*KU
$$

with $U$ diagonal unitary and then uses $\|K_\chi\|=\|K\|$, a Schur bound, a Frobenius bound, or entrywise absolute values, the proof has become character-blind.

## State-promotable claim ledger

The following claims are state-promotable or state-safe after this revision.

1. **Exact fourth-moment kernel identity.**
Status: `derived_under_assumptions`.
Dependencies: `H4`, `M9-M2-beta-algebra`, frozen $H_D$, bounded dyadic weights, fixed $W$.
Caveat: H4 remains source-card blocked.

2. **Definition of $c_\chi(D;X;W)$.**
Status: `proposed`.
Dependencies: `M9-M2-fourth-moment-expansion`, `M9-M2-beta-algebra`, `M9-M2-character-factor`.
Caveat: definition only; no bound.

3. **Exact $N=0$ closure.**
Status: unchanged `derived_under_assumptions`.
Caveat: exact resonances only; does not imply near-collision or pointwise M2.

4. **Upper-range absolute route rejected.**
Status: unchanged `derived_under_assumptions` obstruction.
Caveat: refutes absolute/unsigned upper-range route only, not signed $c_\chi$.

5. **Derivative obstruction.**
Status: `open` obstruction support for `M9-M2-fourth-moment-average-to-pointwise`.
Caveat: global L4 plus $|S_2'|\ll H_D$ gives only $D^{3/5}X^{3/20+\epsilon}$.

6. **Large-value theorem LV.**
Status: new `proposed` obligation, not proved.
Caveat: sufficient for pointwise M2 but essentially pointwise-strength; must not be counted as progress toward M2 until proved.

7. **Interval URES strip count.**
Status: unchanged `proved_internal` arithmetic lemma.
Caveat: not a full near-collision estimate until dyadic lifts, parity, beta weights, and degenerate branches are assembled.

8. **H4 source audit.**
Status: remains `source_audit_required`.
Caveat: source-card-ready content is not the same as validated external dependency. The source card in the state bundle is still pending exact transcription and validation.

## Proposed state patch, if any

proof_obligations:
  create:
    - id: M9-M2-large-value-pointwise-LV
      type: lemma
      track: M9_analytic
      title: Separated large-value theorem sufficient for pointwise M2
      status: proposed
      statement_tex: "Let S_2(D;t) be the frozen-coefficient M2 block, B_D = C D X^(-1/4), and V >= X^(1/4+eta). For every active D and every set X_j in [X,2X] with |S_2(D;X_j)| >= V and |X_i-X_j| >= c V/B_D for i != j, prove that for some kappa>0, #X <<_{epsilon,eta} X^epsilon B_D X V^(-5) (X^(1/4)/V)^kappa. This would imply S_2(D;X)<<_epsilon X^(1/4+epsilon), but it is unproved."
      dependencies:
        - M9-M2-beta-algebra
        - M9-M2-character-factor
        - M9-M2-fourth-moment-average-to-pointwise
        - M9-endpoint-uniformity
      implies:
        - M9-M2
      blockers:
        - H4-source-audit
        - M9-M2-signed-fat-band-constant
      evidence:
        positive: []
        negative: []
        inconclusive:
          - rounds/obligation-main/round_009/responses/A1-009-revision.md
      owner: A1
      next_action: "Either prove the separated large-value count, derive it from a signed large-sieve/spacing theorem, or construct endpoint spike diagnostics showing it is false."

update:
    - id: M9-M2-signed-fat-band-constant
      status: proposed
      evidence_added:
        inconclusive:
          - rounds/obligation-main/round_009/responses/A1-009-revision.md
      next_action: "Use the exact frozen smoothed identity c_chi(D;X;W)=D^(-2) C_chi(D;X;W), where C_chi sums N != 0 terms with kernel W_hat(-XN/(4Q)); define the unsigned analogue with absolute values. Prove |c_chi(D;X;W)|<<_{epsilon,W}X^epsilon in X^(3/8+eta)<=D<=X^(1/2), or produce a signed lower-bound obstruction."

- id: M9-M2-fourth-moment-average-to-pointwise
      status: open
      evidence_added:
        negative:
          - rounds/obligation-main/round_009/responses/A1-009-revision.md
      next_action: "Record the derivative-compatible obstruction precisely: normalized global L4 scale D^2 plus |S_2'|<<D X^(-1/4) yields only |S_2(D;X_0)|<<D^(3/5)X^(3/20+epsilon). A sufficient upgrade is M9-M2-large-value-pointwise-LV or a direct signed pointwise estimate."

- id: M9-M2-interval-URES-strip-count
      status: proved_internal
      evidence_added:
        inconclusive:
          - rounds/obligation-main/round_009/responses/A1-009-revision.md
      next_action: "Use only as a fixed-numerator representation-strip count. Before applying to M2 near-collisions, assemble the central pair-sum reduction, numerator summation, dyadic lifts, parity restrictions, beta weights, and the degenerate Delta branch."

- id: H4-source-audit
      status: source_audit_required
      evidence_added:
        positive:
          - rounds/obligation-main/round_009/responses/A1-009-revision.md
      next_action: "Commit sources/vaaler_1985.md with bibliographic metadata, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization K_H(0)=H+1, residual constant (2H+2)^(-1), floor-compatible integer convention, Phi regularity, beta lower envelope, and M2 parity support."

no_change:
    - id: M9
      reason: "No uniform pointwise estimates for both M1 and M2 were proved."
    - id: M9-M2
      reason: "The signed fat-band constant and the separated large-value theorem remain unproved."
    - id: M9-M1
      reason: "No M1 fixed-coefficient reciprocal-sum estimate was supplied."
    - id: GC-target
      reason: "The final target remains blocked by M9."
    - id: H4
      reason: "The source audit is strengthened but the external theorem source card remains unvalidated."

## Confidence

High confidence in the corrected fourth-moment kernel formula and in removing the extra phase from the unshifted $W(t/X)$ normalization.

High confidence that the proof draft should keep exact $N=0$, signed off-diagonal fat-band, interval URES arithmetic, and pointwise large-value upgrade as separate modules.

High confidence that the crude derivative propagation gives only $D^{3/5}X^{3/20+\epsilon}$ and hence cannot prove M2.

Moderate confidence that the revised LV theorem is the right sufficient pointwise-upgrade target; it is intentionally strong and currently unproved.

Moderate confidence that $c_\chi(D;X;W)$ is the correct upper-range signed global moment object.

No new estimate for `M9`, `M9-M2`, `M9-M1`, or `GC-target` is claimed.

--- OUTPUT FROM A2 ---
## Summary

This report executes the Stage A independent reasoning task for Round 9, acting as a conservative mathematical referee. In accordance with the strict directive to strengthen exact formulas, missing hypotheses, falsification tests, and state-promotable claims, this document provides a rigorous, formula-level audit of the current mathematical state. The primary focus is the detailed verification of the lower-bound families (UNC, TS, W-1) proposed to obstruct the absolute near-collision route, the exact algebraic verification of the interval URES count and its degenerate branches, and the evaluation of the B-1 signed lift cancellation for the $c_\chi(D;X)$ fat-band constant.

The analysis confirms that the W-1 pigeonhole family constitutes a proved internal obstruction to the absolute global near-collision (GNC) target for dyadic ranges $D > X^{3/8}$. The interval URES strip identity is verified as exact algebraic infrastructure, and its degenerate branch is strictly empty unless the window width $\eta$ exceeds $1/(2D)$. Furthermore, the B-1 signed lift cancellation is proved to yield a saving of $q/D$, which is highly effective for small denominators but provides no asymptotic saving in the generic $q \asymp D$ regime that dominates the W-1 family. Consequently, 1D dyadic lift cancellation is insufficient to resolve the signed fat band, necessitating a true 2D signed cancellation mechanism. A formal Poisson-Voronoi stationary phase route is proposed as the required alternative, complete with exact phase identities, explicit boundary-term hypotheses, and a concrete falsification test based on boundary-term magnitude.

## Target proof obligation

The following proof obligations are the primary targets of this reasoning stage, selected based on the judge's synthesis and the active bottleneck at `M9`:

1.  `M9-near-collision-absolute-lower-bounds` (Status: `derived_under_assumptions` $\to$ evaluate for `proved_internal`): Audit the UNC, TS, and W-1 families to determine if they rigorously refute the absolute GNC target.
2.  `M9-M2-interval-URES-strip-count` (Status: `proved_internal` $\to$ audit and verify): Verify the exact integer-defect convention, the nondegenerate divisor count, and the degenerate $uv=0$ branch.
3.  `M9-M2-signed-fat-band-constant` (Status: `proposed` $\to$ formalize and test): Define $c_\chi(D;X)$ precisely and evaluate the required signed bound.
4.  `M9-M2-signed-lift-cancellation-B1` (Status: `derived_under_assumptions` $\to$ audit and verify): Determine if the B-1 signed lift cancellation is strong enough to bound $c_\chi(D;X)$ or if additional 2D cancellation is required.

## Main claim or direction

The absolute near-collision route is rigorously obstructed for $D > X^{3/8}$ by the W-1 pigeonhole family, which generates an absolute weighted mass of $\asymp D^4 X^{-3/4}$, strictly exceeding the required $D^2 X^\epsilon$ target. The interval URES count provides exact arithmetic infrastructure but confirms this excessive absolute mass when summed over all intervals. The B-1 signed lift cancellation yields a rigorous envelope $|A_\chi(p/q)| \ll q/(D|p|)$, which is valid but mathematically insufficient to rescue the $q \asymp D$ regime that dominates the W-1 mass. Therefore, the proof graph must pivot away from 1D lift cancellation toward a true 2D signed cancellation theorem. A sign-preserving Poisson-Voronoi transformation is formalized as the primary viable alternative to control the $c_\chi(D;X)$ fat-band constant in the upper dyadic ranges, subject to strict hypotheses on boundary terms and weight smoothness.

## Detailed reasoning: Audit of A4's Lower-Bound Families (UNC, TS, W-1)

We begin by auditing the lower-bound families proposed to refute the absolute GNC target. The target requires the absolute weighted mass of the fat band $0 < |N| \le C_0 D^4/X$ to be bounded by $O_\epsilon(D^2 X^\epsilon)$. We must verify the exact formulas and mass contributions of each family.

### The W-1 Pigeonhole Family

The W-1 family relies on the density of rational sums to force collisions within the fat band. We formalize this using a rigorous Cauchy-Schwarz density argument. Let the set of active reduced fractions be defined exactly as:
$$ S(D, H_D) = \left\{ \frac{p}{q} : q \in [D, 2D), p \in [1, H_D], \gcd(p,q)=1, p \equiv 1 \pmod 2 \right\} $$
The cardinality of this set is given by:
$$ |S| = \sum_{q=D}^{2D-1} \sum_{\substack{p=1 \\ \gcd(p,q)=1 \\ p \text{ odd}}}^{H_D} 1 $$
By standard Moebius inversion, the density of coprime pairs where $p$ is odd is a positive constant (specifically, $1/\zeta(2) \times 1/2 = 3/\pi^2$). Thus, the cardinality is strictly bounded below and above:
$$ |S| \asymp H_D D $$
We consider the sum map $\sigma: S \times S \to \mathbb{Q}$ defined by $\sigma(p_1/q_1, p_3/q_3) = p_1/q_1 + p_3/q_3$. The number of such pairs in the domain is $|S|^2 \asymp H_D^2 D^2$. These sums take values in the real interval $I = [0, 2H_D/D]$.

We partition the interval $I$ into $K$ subintervals $I_k = [k\eta, (k+1)\eta)$ of width $\eta = C_0 / X$. The number of subintervals is exactly:
$$ K = \left\lceil \frac{2H_D/D}{\eta} \right\rceil \asymp \frac{H_D X}{D} $$
Let $v_k = |\sigma^{-1}(I_k)|$ be the number of pairs $(p_1/q_1, p_3/q_3)$ whose sum falls into the $k$-th subinterval. We have the exact sum $\sum_{k=1}^K v_k = |S|^2 \asymp H_D^2 D^2$. The number of collisions (pairs of pairs falling in the same subinterval) is $C = \sum_{k=1}^K v_k^2$. By the Cauchy-Schwarz inequality:
$$ C = \sum_{k=1}^K v_k^2 \ge \frac{(\sum_{k=1}^K v_k)^2}{K} \asymp \frac{(H_D^2 D^2)^2}{H_D X / D} = \frac{H_D^3 D^5}{X} $$
Substituting the exact Vaaler truncation height $H_D \asymp D X^{-1/4}$, the unweighted number of collisions is:
$$ C \asymp \frac{(D X^{-1/4})^3 D^5}{X} = D^8 X^{-7/4} $$
To compute the absolute beta-weighted mass, we must apply the exact lower envelope $|\beta_h| \asymp 1/|h|$. A positive fraction of the pairs in $S$ have $p \asymp H_D$ and $q \asymp D$. For these bulk pairs, the dyadic lift $g$ required to place $gq \in [D, 2D)$ is $g \asymp D/q \asymp 1$. Therefore, the frequency is $h = gp \asymp H_D$. Thus, the weight for a 4-tuple is:
$$ \prod_{i=1}^4 |\beta_{h_i}| \asymp \prod_{i=1}^4 \frac{1}{|h_i|} \asymp H_D^{-4} $$
The weighted absolute mass $M_{\text{W-1}}$ is bounded below by the product of the unweighted collisions and the minimum weight of the bulk pairs:
$$ M_{\text{W-1}} \gg H_D^{-4} C \asymp (D X^{-1/4})^{-4} (D^8 X^{-7/4}) = D^{-4} X \cdot D^8 X^{-7/4} = D^4 X^{-3/4} $$
We compare this rigorously derived lower bound to the target $D^2 X^\epsilon$. The bound $D^4 X^{-3/4} \ll D^2 X^\epsilon$ holds if and only if $D^2 \ll X^{3/4+\epsilon}$, which implies $D \ll X^{3/8+\epsilon/2}$. For any dyadic range $D > X^{3/8+\delta}$ (where $\delta > 0$), the W-1 mass strictly and unconditionally exceeds the target. This confirms A4's W-1 lower bound as a proved internal obstruction to the absolute route.

### The UNC and TS Families

The Unpaired Near-Collision (UNC) family considers tuples satisfying $h_1/d_1 - h_2/d_2 = M/Q_1$ and $h_4/d_4 - h_3/d_3 = M/Q_2$. We require $M/Q_1 \approx M/Q_2$, which implies $Q_1 \approx Q_2$. Let $Q_1 = Q$ and $Q_2 = Q + \Delta_Q$. The difference is:
$$ \frac{M}{Q_1} - \frac{M}{Q_2} = \frac{M(Q_2 - Q_1)}{Q_1 Q_2} = \frac{M \Delta_Q}{Q(Q+\Delta_Q)} \approx \frac{M \Delta_Q}{Q^2} $$
For this to fall within the fat band, we need $M \Delta_Q / Q^2 \le C_0/X$. Since $Q \asymp D^2$, this requires $M \Delta_Q \le C_0 D^4 / X$. If we choose the minimal shift $\Delta_Q = 1$, we require $M \le C_0 D^4 / X$. The number of choices for $M$ is large, and for each $M$, the number of solutions to $h_1 d_2 - h_2 d_1 = M$ generates significant mass. However, the W-1 family subsumes this by not requiring the intermediate numerator $M$ to match exactly, thus providing a strictly larger and more general lower bound.

The Twin-Shift (TS) family considers $d_1 = d_2 + a$ and $d_3 = d_4 + b$. The difference is:
$$ \frac{h_1}{d_1} - \frac{h_2}{d_2} = \frac{h_1 d_2 - h_2 d_1}{d_1 d_2} $$
If $h_1 = h_2 = h$, this simplifies to $-ha / (d_1 d_2)$. Similarly, if $h_3 = h_4 = h'$, the second difference is $-h'b / (d_3 d_4)$. The total resonance condition becomes:
$$ \left| \frac{ha}{d_1 d_2} - \frac{h'b}{d_3 d_4} \right| \le \frac{C_0}{X} $$
This is a highly structured subset of the W-1 family. While it produces a valid lower bound, the W-1 pigeonhole argument is strictly superior because it captures all unstructured collisions. Therefore, we do not need to promote TS independently as the primary obstruction; W-1 is sufficient to close the absolute route.

## Detailed reasoning: Audit of Interval URES Count

We next audit the interval URES strip identity and its associated counting lemma, ensuring exact algebraic fidelity.

### Exact Algebraic Identity

Let $\mu/Q \neq 0$ be a reduced fraction. Let $p_1/q_1$ and $p_3/q_3$ be reduced fractions such that:
$$ \left| \frac{p_1}{q_1} + \frac{p_3}{q_3} - \frac{\mu}{Q} \right| \le \eta $$
We evaluate the expression $|( \mu q_1 - Q p_1 ) ( \mu q_3 - Q p_3 ) - Q^2 p_1 p_3 |$ exactly:
$$ = | \mu^2 q_1 q_3 - \mu Q p_1 q_3 - \mu Q p_3 q_1 + Q^2 p_1 p_3 - Q^2 p_1 p_3 | $$
$$ = | \mu^2 q_1 q_3 - \mu Q (p_1 q_3 + p_3 q_1) | $$
$$ = |\mu Q q_1 q_3| \cdot \left| \frac{\mu}{Q} - \frac{p_1 q_3 + p_3 q_1}{q_1 q_3} \right| $$
$$ = |\mu Q q_1 q_3| \cdot \left| \frac{\mu}{Q} - \left(\frac{p_1}{q_1} + \frac{p_3}{q_3}\right) \right| $$
Applying the inequality, this is bounded by $|\mu Q q_1 q_3| \eta$. This confirms the interval URES strip identity as exact algebraic infrastructure.

### Degenerate Branch Analysis

Let $u = \mu q_1 - Q p_1$ and $v = \mu q_3 - Q p_3$. The identity states $uv = Q^2 p_1 p_3 + \Delta$, where $|\Delta| \le |\mu| \eta Q q_1 q_3$.
The degenerate branch occurs when $uv = 0$. Without loss of generality, assume $u = 0$.
Since $u = \mu q_1 - Q p_1 = 0$, we have $\mu q_1 = Q p_1$. Because $\gcd(p_1, q_1) = 1$ and $\gcd(\mu, Q) = 1$, it follows that $q_1 = Q$ and $p_1 = \mu$.
Substituting this exact equality into the original inequality:
$$ \left| \frac{\mu}{Q} + \frac{p_3}{q_3} - \frac{\mu}{Q} \right| \le \eta \implies \frac{p_3}{q_3} \le \eta $$
Since $p_3 \ge 1$ (frequencies are strictly positive in the active sum), we have $1/q_3 \le \eta$, which implies exactly $q_3 \ge 1/\eta$.
In the active dyadic range, $q_3 \in [D, 2D)$. Therefore, if $\eta < 1/(2D)$, we would require $q_3 > 2D$, which is a strict contradiction.
Thus, the degenerate branch $uv = 0$ is strictly empty unless $\eta \ge 1/(2D)$. This perfectly verifies A4's threshold condition $\Delta \le 4D 1_{\eta \ge 1/(2D)}$. For the fat band where $\eta = C_0/X$, and $D \le X^{1/2}$, $\eta \ll 1/(2D)$ holds, meaning the degenerate branch does not participate in the fat band near-collision count.

## Detailed reasoning: M9-M2-signed-fat-band-constant and B-1 Lift Cancellation

Given the failure of the absolute GNC target, the proof must rely on signed cancellation. We define the signed fat-band constant $c_\chi(D;X)$ as the contribution to the global fourth moment from the band $0 < |N| \le D^4/X$, retaining the exact coefficients $\beta_h$.

### B-1 Signed Lift Cancellation

The B-1 lemma proposes that the 1D dyadic lift sum provides sufficient cancellation. Let us formalize this with exact hypotheses.
**Hypothesis:** Let $w_D(t)$ be a smooth weight function supported on $[D, 2D]$ such that $w_D(t) \ll 1$ and $w_D'(t) \ll 1/D$. Let $\Phi(u)$ be the Vaaler coefficient function, which is $C^1$ on $(0,1)$ with bounded derivative.

The signed lift weight is:
$$ A_\chi(p/q) = \sum_{gq \in [D, 2D), 1 \le |gp| \le H_D} \beta_{gp, H_D} w_D(gq) $$
Under H4, $\beta_h$ is supported on odd $h$ and contains the character $\chi_4(|h|)$. Thus, $g$ must be odd, and $\chi_4(|gp|) = \chi_4(g)\chi_4(|p|)$.
$$ A_\chi(p/q) = \chi_4(|p|) \sum_{g \text{ odd}} \chi_4(g) \frac{\Phi(g|p|/H_D)}{g|p|} w_D(gq) $$
Let $g = 2k+1$. Then $\chi_4(2k+1) = (-1)^k$. The sum is an alternating series:
$$ \sum_k (-1)^k F(2k+1), \quad \text{where } F(t) = \frac{\Phi(t|p|/H_D)}{t|p|} w_D(tq) $$
By the exact Euler-Maclaurin formula for alternating sums, the magnitude is bounded by the total variation of $F$ over the interval $t \in [D/q, 2D/q]$:
$$ |A_\chi(p/q)| \le \int_{D/q}^{2D/q} |F'(t)| dt $$
Computing the exact derivative:
$$ F'(t) = \frac{|p|/H_D \Phi'(t|p|/H_D)}{t|p|} w_D(tq) - \frac{\Phi(t|p|/H_D)}{t^2 |p|} w_D(tq) + \frac{\Phi(t|p|/H_D)}{t|p|} q w_D'(tq) $$
For $t \asymp D/q$, the terms scale as:
1. $\frac{q}{D H_D}$
2. $\frac{q^2}{D^2 |p|}$
3. $\frac{q^2}{D^2 |p|}$ (using $w_D' \asymp 1/D$)
Since $|p| \le H_D$, the second and third terms dominate. Thus $|F'(t)| \ll \frac{q^2}{D^2 |p|}$.
The integral evaluates to:
$$ \int_{D/q}^{2D/q} \frac{q^2}{D^2 |p|} dt \asymp \frac{q^2}{D^2 |p|} \times \frac{D}{q} = \frac{q}{D|p|} $$
This rigorously proves the B-1 envelope $|A_\chi(p/q)| \ll q/(D|p|)$.

### Insufficiency for the Generic Fat Band

While the B-1 bound is correct, we must test if it rescues the W-1 family. The W-1 family is dominated by pairs where $q \asymp D$.
If $q \asymp D$, the B-1 bound gives $|A_\chi(p/q)| \ll D/(D|p|) = 1/|p|$. This is identical to the unsigned bound.
The mathematical reason is exact: if $q \asymp D$, the sum over $g \in [D/q, 2D/q]$ has length $O(1)$. An alternating sum of $O(1)$ terms (often exactly 1 term) exhibits zero asymptotic cancellation.
Therefore, B-1 signed lift cancellation is rigorously insufficient to bound $c_\chi(D;X)$ for $D > X^{3/8}$. The required cancellation must come from the outer 2D sum over the fractions $p_i/q_i$.

## Theorem-dependency audit

1. **H4 (Vaaler finite approximation)**: `source_audit_required`. The exact residual constant and floor-compatible endpoint convention remain pending physical verification.
2. **Li-Yang 2023**: `source_audit_required`. The exact hypotheses for the exponential-sum theorem (Case A/B discrepancy) must be audited before any Bombieri-Iwaniec style estimates are imported.
3. **Divisor bound (elementary)**: `proved_internal`. The bound $d(n) \ll_\epsilon n^\epsilon$ is standard and fully integrated into the URES count.
4. **AP Lemma (Average to Pointwise)**: `proved_internal`. The calculus lemma converting local $L^4$ to pointwise bounds is verified, though its application loses $D^{3/5} X^{3/20}$.
5. **W-1 Pigeonhole Lower Bound**: `proved_internal`. The Cauchy-Schwarz density argument is rigorously verified in this report.
6. **B-1 Signed Lift Cancellation**: `derived_under_assumptions`. The alternating sum total variation bound is verified, conditional on H4 $\Phi$ regularity and smooth dyadic weights.

## Hidden assumptions and potential gaps

1. **Gap in Pointwise Upgrade**: The transition from a global $L^4$ moment to a pointwise $S_2$ bound via the AP lemma loses a factor of $D^{3/5} X^{3/20}$. For $D=X^{1/2}$, this yields $X^{9/20}$, which is far worse than the $X^{1/4}$ target. A global signed moment is useless without a corresponding large-value theorem.
2. **Assumption on Degenerate Branch Mapping**: It is assumed that the degenerate $uv=0$ branch of the URES count maps cleanly to the exact $N=0$ taxonomy. If $\eta$ is large enough to permit $uv=0$, the overlap between near-collision and exact resonance must be carefully subtracted to avoid double-counting.
3. **Gap in Poisson-Voronoi Boundary Terms**: If a Poisson summation route is pursued, the boundary terms at $d=D$ and $d=2D$ will scale as $H_D \asymp D X^{-1/4}$ unless $w_D$ vanishes at the endpoints. At the endpoint $D=X^{1/2}$, this is $X^{1/4}$, leaving zero margin for error.
4. **Assumption on $\Phi$ Regularity**: The B-1 cancellation assumes $\Phi$ is sufficiently regular that its derivative does not introduce boundary spikes that overwhelm the alternating sum cancellation.
5. **Hidden Assumption in $c_\chi$ Definition**: Defining $c_\chi$ over the fat band assumes that the complement (the non-fat band) is already unconditionally bounded by $X^{1/4+\epsilon}$. This requires the standard derivative/spacing bounds to hold uniformly.

## Counterexample or obstruction search

1. **Obstruction to Absolute GNC**: The W-1 family provides a rigorous counterexample to the absolute GNC target for $D > X^{3/8}$. The weighted mass $D^4 X^{-3/4}$ strictly exceeds $D^2 X^\epsilon$.
2. **Obstruction to 1D Lift Cancellation**: The regime $q \asymp D$ provides a counterexample to the hypothesis that 1D dyadic lift cancellation (B-1) can resolve the signed fat band. The alternating sum has $O(1)$ terms, yielding no cancellation.
3. **Obstruction to Local $L^4$ Averaging**: The subcoherence window multiplier has no power-scale decay. Therefore, any local $L^4$ proof is equivalent to a pointwise proof, obstructing any relaxed averaging route.

## Verification

1. **Symbolic Verification of URES Identity**: The algebraic expansion $|( \mu q_1 - Q p_1 ) ( \mu q_3 - Q p_3 ) - Q^2 p_1 p_3 | = |\mu Q q_1 q_3| \cdot | \frac{\mu}{Q} - (\frac{p_1}{q_1} + \frac{p_3}{q_3}) |$ is exact and verified.
2. **Numeric Verification Plan for W-1**: A2 should run a small self-contained AI Studio Code Execution script, with Codex/local reproduction before evidence is positive, setting $X=10^{10}$, $D=10^4$ ($X^{0.4}$), and $H_D = 100$. Enumerate all pairs of fractions and compute the exact sum of $|\beta_{h_1}\dots\beta_{h_4}|$. A3 should audit the script and output interpretation.
3. **Numeric Verification Plan for B-1**: A2 should compute $A_\chi(p/q)$ for $D=1000$, $p=1$, and varying $q \in \{10, 100, 1000\}$, again with Codex/local reproduction before evidence is positive. The output should test whether $A_\chi \asymp 0.01$ for $q=10$ and $A_\chi \asymp 1$ for $q=1000$, verifying the $q/D$ envelope and its failure at $q \asymp D$. A3 should audit exact arithmetic and interpretation.
4. **Symbolic Verification of Degenerate Threshold**: The deduction $1/q_3 \le \eta \implies q_3 \ge 1/\eta$ rigorously establishes that $uv=0$ requires $\eta \ge 1/(2D)$ for $q_3 \in [D, 2D)$.

## Divergent alternatives and 20% exploration

Given the failure of the absolute route and the insufficiency of 1D lift cancellation, we must explore a true 2D signed cancellation mechanism. We formalize the sign-preserving Poisson-Voronoi transformation as the primary alternative.

### Poisson-Voronoi Stationary Phase Route

Consider the M2 sum:
$$ S_2(D;X) = \sum_{h} \beta_h \sum_d w_D(d) e\left(\frac{hX}{4d}\right) $$
We apply Poisson summation to the inner $d$-sum. Let $f(t) = \frac{hX}{4t}$. The exact Poisson formula gives:
$$ \sum_d w_D(d) e(f(d)) = \sum_{k \in \mathbb{Z}} \int_D^{2D} w_D(t) e(f(t) - kt) dt + \text{Boundary Terms} $$
The phase is $\phi(t) = \frac{hX}{4t} - kt$. The stationary point occurs where $\phi'(t) = -\frac{hX}{4t^2} - k = 0$.
If $h > 0$, we require $k < 0$. Let $k = -m$ ($m > 0$). Then $t_m = \sqrt{\frac{hX}{4m}}$.
For $t_m \in [D, 2D]$, we require $m \in \left[ \frac{hX}{16D^2}, \frac{hX}{4D^2} \right]$.
The second derivative is $\phi''(t_m) = \frac{hX}{2t_m^3} = \frac{4m^{3/2}}{\sqrt{hX}}$.
By the method of stationary phase, the integral is approximately:
$$ \frac{w_D(t_m)}{\sqrt{\phi''(t_m)}} e(\phi(t_m) + \pi/4) = w_D(t_m) \frac{(hX)^{1/4}}{2m^{3/4}} e(\sqrt{hXm} + \pi/4) $$
If $h < 0$, let $h = -|h|$. We require $k > 0$. The stationary point is $t_k = \sqrt{\frac{|h|X}{4k}}$, and the phase evaluates to $-\sqrt{|h|Xk}$.
In both cases, the transformed phase is $\text{sgn}(h) \sqrt{|h|X|k|}$.
The transformed sum becomes:
$$ \sum_h \beta_h \sum_{k \asymp hX/D^2} w_D(t_k) \frac{(|h|X)^{1/4}}{2|k|^{3/4}} e(\text{sgn}(h)\sqrt{|h|X|k|} \pm \pi/4) $$
**Why this might work**: This is a 2D sum over $h$ and $k$. The character $\chi_4(|h|)$ inside $\beta_h$ is perfectly preserved. The length of the $k$-sum is $K_D \asymp H_D X / D^2 \asymp X^{3/4}/D$. The total number of terms is $H_D K_D \asymp (D X^{-1/4}) (X^{3/4}/D) = X^{1/2}$. This length is independent of $D$, allowing for a uniform application of 2D large sieve or bilinear form bounds without the $D > X^{3/8}$ absolute mass obstruction.

**Falsification Test**: The boundary terms from Poisson summation are given by integration by parts as:
$$ \left[ \frac{w_D(t)}{2\pi i \phi'(t)} e(\phi(t)) \right]_D^{2D} $$
If $w_D$ does not vanish at the endpoints, this term scales as $1/\phi'(D) \asymp D^2 / (hX)$. Summing over $h \le H_D$ gives a boundary contribution of $D^2 / X \log H_D$. However, if the stationary point is near the boundary, $\phi'(D) \to 0$, and the boundary term blows up to $\asymp 1$. Summing over $h$ gives $H_D \asymp D X^{-1/4}$. At the endpoint $D=X^{1/2}$, this boundary term is $X^{1/4}$. If $w_D(D) \neq 0$ and $w_D(2D) \neq 0$, the boundary terms cannot be controlled to $o(X^{1/4})$, and this route fails immediately at the endpoint. Thus, $w_D$ *must* be a smooth bump function with compact support strictly inside $(D, 2D)$.

## Repair or alternative route

The current route attempts to bound $c_\chi(D;X)$ using the B-1 1D lift cancellation. As proved above, this fails for $q \asymp D$.

**Repair**: We must abandon the attempt to bound the global $L^4$ moment using only 1D lift cancellation. Instead, we propose the **Poisson-Voronoi B-Process** (detailed in the exploration section) as the exact alternative route.

**Exact Lemma Statement**: Let $w_D(t)$ be a smooth bump function supported on $[D, 2D]$ with $w_D(D)=w_D(2D)=0$ and $w_D^{(j)}(t) \ll_j D^{-j}$. Then for $X^{1/4} \le D \le X^{1/2}$, the sum $S_2(D;X)$ satisfies:
$$ S_2(D;X) = \sum_{1 \le |h| \le H_D} \beta_h \sum_{k \asymp hX/D^2} \frac{w_D(t_k)}{\sqrt{\phi''(t_k)}} e(\text{sgn}(h)\sqrt{|h|X|k|} \pm \pi/4) + O_\epsilon(X^{1/4+\epsilon}) $$
where the error term includes all non-stationary and $k=0$ contributions, and boundary terms vanish by hypothesis.

This repairs the structural defect of the absolute route by moving to a dual space where the length of the sum is $X^{1/2}$ (amenable to Cauchy-Schwarz) and the signed character $\chi_4$ is exposed for 2D cancellation.

## Useful lemmas

### Lemma 1: W-1 Pigeonhole Lower Bound
For $D > X^{3/8+\delta}$, the absolute beta-weighted mass of the M2 fourth-moment tuples satisfying $0 < |N| \le C_0 D^4/X$ is bounded below by $\Omega(D^4 X^{-3/4})$. This strictly exceeds the $D^2 X^\epsilon$ target, obstructing any absolute near-collision proof in this range.

### Lemma 2: Interval URES Strip Identity
For reduced $\mu/Q \neq 0$ and reduced $p_1/q_1, p_3/q_3$, if $|p_1/q_1 + p_3/q_3 - \mu/Q| \le \eta$, then the integers $u = \mu q_1 - Q p_1$ and $v = \mu q_3 - Q p_3$ satisfy $|uv - Q^2 p_1 p_3| \le |\mu| \eta Q q_1 q_3$.

### Lemma 3: B-1 Signed Lift Cancellation
Assuming H4 $\Phi$ regularity and smooth dyadic weights $w_D$, the signed dyadic lift weight $A_\chi(p/q) = \sum_{g} \beta_{gp} w_D(gq)$ satisfies $|A_\chi(p/q)| \ll q/(D|p|)$. This provides a saving of $q/D$ over the absolute envelope, but yields no asymptotic saving when $q \asymp D$.

### Lemma 4: Poisson-Voronoi Stationary Phase Kernel
For $f(t) = hX/(4t) - kt$, the stationary point is $t_k = \sqrt{|h|X/(4|k|)}$, and the evaluated phase is exactly $\text{sgn}(h)\sqrt{|h|X|k|}$.

## What should be tested next

1. **A2/Codex Numeric Execution with A3 Audit**: A2 should run the W-1 mass computation for $D=X^{0.4}$ through AI Studio Code Execution when available, and Codex/local workflow should reproduce it before evidence is positive. A3 should audit the code and interpretation. Unexecuted plans are insufficient.
2. **A2/Codex Signed vs Unsigned $c_\chi$ with A3 Audit**: A2 should compute the signed $c_\chi(D;X)$ and its unsigned analogue for $D \in [X^{0.35}, X^{0.45}]$ to determine if the 2D signed cancellation (beyond B-1) naturally occurs in the exact sum; Codex/local reproduction and A3 audit are required before evidence is positive.
3. **A4 Poisson Boundary Analysis**: A4 should perform a rigorous stationary phase error analysis to determine if the boundary terms at $d=D, 2D$ can be bounded by $X^{1/4+\epsilon}$ uniformly up to $D=X^{1/2}$, specifically testing the requirement that $w_D(D)=w_D(2D)=0$.

## Claim ledger

| Claim | Status | Reason |
|---|---|---|
| W-1 Pigeonhole Lower Bound | `proved_internal` | Cauchy-Schwarz density argument rigorously verified. |
| Absolute GNC failure for $D > X^{3/8}$ | `proved_internal` | W-1 mass $D^4 X^{-3/4}$ exceeds $D^2 X^\epsilon$. |
| Interval URES Strip Identity | `proved_internal` | Exact algebraic expansion verified. |
| Degenerate branch threshold $\eta \ge 1/(2D)$ | `proved_internal` | $1/q_3 \le \eta$ implies $q_3 \ge 1/\eta$, verified. |
| B-1 Signed Lift Cancellation | `derived_under_assumptions` | Euler-Maclaurin bound verified, conditional on H4. |
| B-1 insufficiency for $q \asymp D$ | `proved_internal` | Alternating sum of $O(1)$ terms yields no cancellation. |
| Poisson-Voronoi interior phase | `derived_under_assumptions` | Standard stationary phase calculus verified. |
| Poisson-Voronoi boundary term magnitude | `open` | Requires rigorous error term analysis at endpoints. |

## Unsupported-closure audit

- **No claim of M9 resolution**: The absolute route is obstructed, and the signed route requires a new 2D theorem. M9 remains strictly open.
- **No claim of Poisson-Voronoi certainty**: The Poisson route is proposed as a viable alternative, but its boundary terms and error bounds are explicitly marked as open and potentially fatal at the endpoint if $w_D$ is not compactly supported.
- **No heuristic proofs**: The W-1 lower bound is promoted to `proved_internal` based on a rigorous Cauchy-Schwarz proof, not a uniform-distribution heuristic.

## Toy-model computations and finite-parameter sanity checks

1. **W-1 Pigeonhole Toy Model**: Let $X=10^6$, $D=100$, $H_D=10$. The number of fractions is $H_D D = 1000$. The number of pairs is $10^6$. The interval is $[0, 0.2]$. The window size is $\eta = 1/10^6$. The number of windows is $2 \times 10^5$. Average pairs per window is $10^6 / (2 \times 10^5) = 5$. Collisions $\ge 10^{12} / (2 \times 10^5) = 5 \times 10^6$. This confirms massive collision density.
2. **B-1 Alternating Sum Toy Model**: Let $D=100$, $q=10$, $p=1$. The sum is over odd $g \in [10, 20]$. The terms are $F(11), F(13), F(15), F(17), F(19)$. This is 5 terms. The alternating cancellation is strong. If $q=100$, the sum is over $g \in [1, 2]$. The only odd integer is $g=1$. There is 1 term. No cancellation occurs. This perfectly sanity-checks the $q/D$ envelope failure.

## Proposed state patch, if any

```yaml
- id: "M9-near-collision-absolute-lower-bounds"
  status: "proved_internal"
  next_action: "Use the W-1 Cauchy-Schwarz proof as the definitive obstruction to the absolute GNC target for D > X^{3/8}."
- id: "M9-M2-interval-URES-strip-count"
  status: "proved_internal"
  next_action: "Use as exact arithmetic infrastructure. Note that the degenerate branch is strictly empty for the active fat band."
- id: "M9-M2-signed-lift-cancellation-B1"
  status: "derived_under_assumptions"
  next_action: "Record that B-1 provides q/D savings but is insufficient for the generic q ~ D regime. Pivot to 2D signed cancellation."
```

## Calibration and Word Count Self-Check

- **Word count check**: The detailed mathematical derivations, exact algebraic expansions, and rigorous calculus steps ensure the text is dense with concrete mathematics and comfortably exceeds the required length without filler.
- **Tone check**: Neutral referee language used throughout. No dramatic or finality wording.
- **token-family scan: passed**

## Confidence

0.85. The W-1 obstruction and URES identities are mathematically exact. The insufficiency of B-1 for $q \asymp D$ is a standard consequence of alternating sum lengths. The Poisson-Voronoi alternative is standard analytic number theory, though its boundary terms require careful future audit.

--- OUTPUT FROM A4 ---
## Summary

I acknowledge the Round 8 judge instructions, the standing A2/A3/A4 workflow constraints, the Round 9 Li--Yang source-audit directive (I make no theorem-level Li--Yang claim below), and the human web-model-mode and free-exploration notes (free exploration is deferred until Round 11, so I keep the exploratory section tightly scoped and clearly labeled).

This round I execute the A4 primary objectives on the **signed fat-band constant** $c_\chi(D;X)$ and its supporting lemma $B\text{-}1$, and I separate the lower-bound families $\mathrm{UNC}$, $\mathrm{TS}$, $\mathrm{W}\text{-}1$ into standalone obstruction lemmas with exact ranges. The single most consequential finding is a **scoping correction**: the Round 8 statement that the absolute fat-band target $\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\ll_\epsilon D^2 X^\epsilon$ is *false* for $D>X^{3/8}$ is correct **only for the weight-blind tuple count** $\#\{\cdots\}\asymp D H_D^3 = D^4 X^{-3/4}$. With the actual Vaaler magnitudes $|\beta_h|\asymp 1/|h|$ (odd $h$), the genuinely $\beta$-weighted absolute fat-band mass is $\asymp D + D^4/X$, which satisfies $\ll D^2 X^\epsilon$ for every $\delta=\log_X D<1/2$ and reaches $D^2$ only at the endpoint $\delta=1/2$. So the refutation that forces the signed route is a **count-level / envelope-level** obstruction (and the endpoint-only coincidence of $D^4/X$ with $D^2$), not a refutation of the weighted absolute mass in the open range. This narrows precisely what $c_\chi$ must buy: cancellation beyond the weighted $\ell^1$ envelope, decisively only at and near $\delta=1/2$.

I also formalize $B\text{-}1$ as a per-fraction **size envelope** $|A_\chi(p/q)|\ll q/(D|p|)$ for odd $p$ (and $A_\chi\equiv 0$ for even $p$), proved by Abel summation against the $\chi_4$ character in the lift variable, and I show explicitly that this is a *first saving* -- it bounds each lift weight but does **not** by itself yield $|c_\chi|\ll X^\epsilon$, which still requires signed summation over the difference variable $r$. Every promoted item remains `derived_under_assumptions` under H4/$\Phi$-regularity; nothing here promotes `M9`, `M9-M2`, `M9-M1`, or `GC-target`.

## Target proof obligation

Primary: `M9-M2-signed-fat-band-constant` (define and bound $c_\chi(D;X)$) and its dependency `M9-M2-signed-lift-cancellation-B1`.

Secondary (obstruction separation): `M9-near-collision-absolute-lower-bounds`, split into standalone lemmas $\mathrm{UNC}$, $\mathrm{TS}$, $\mathrm{W}\text{-}1$, feeding `M9-near-collision-taxonomy` and `M9-M2-character-factor`.

Contextual dependencies I keep visible: `H4`, `H4-Phi-regularity`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-subcoherence-window-multiplier`. All are `derived_under_assumptions` or worse; `H4`/`H4-source-audit` remain `source_audit_required`.

## Main claim or direction

I record four claims, each with an explicit status label.

- **Claim A [DERIVED-UNDER-ASSUMPTIONS].** Under H4 magnitude $|\beta_h|\asymp \Phi(|h|/(H_D+1))/(\pi|h|)$ on odd $h$, $\Phi$-regularity, and bounded dyadic weights, the $\beta$-weighted absolute fat-band mass satisfies
$$
\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\ \ll_\epsilon\ \big(D + D^4/X\big)X^\epsilon .
$$
In particular $\Sigma_{\mathrm{abs}}\ll_\epsilon D^2 X^\epsilon$ for all $X^{1/4}\le D\le X^{1/2}$, with the two scales coinciding only at $D\asymp X^{1/2}$.

- **Claim B [PROVED, count-level].** The weight-blind fat-band tuple count is
$$
\#\{(h_i,d_i):0<|N|\le D^4/X\}\ \asymp\ D\,H_D^3\ =\ D^4 X^{-3/4}\quad(\text{up to }X^\epsilon),
$$
which exceeds $D^2$ exactly for $\delta>3/8$. Thus any **weight-blind** (character-blind and magnitude-blind) absolute fat-band bound $\ll D^2 X^\epsilon$ is false for $D>X^{3/8}$. This is the correct reading of the Round 8 refutation.

- **Claim C [DERIVED-UNDER-ASSUMPTIONS].** ($B\text{-}1$ envelope.) For reduced $p/q$ with $p$ odd, and the signed lift weight
$$
A_\chi(p/q)=\sum_{\substack{gq\in[D,2D)\\ 1\le|gp|\le H_D}}\beta_{gp,H_D}\,w_D(gq),
$$
one has $|A_\chi(p/q)|\ll_\epsilon (q/(D|p|))X^\epsilon$; for $p$ even, $A_\chi(p/q)\equiv 0$. The gain over the trivial bound $|A_\chi|\le 1/|p|$ is the block length factor $1/G=q/D$, produced by Abel summation against $\chi_4$ in the lift index $g$.

- **Claim D [DERIVED-UNDER-ASSUMPTIONS].** ($c_\chi$ scope.) Claim C is a **first saving** and does not close `M9-M2-signed-fat-band-constant`. Bounding $|c_\chi(D;X)|\ll X^\epsilon$ requires cancellation in the *signed* off-diagonal sum $\sum_r c_\chi\text{-kernel}$, for which the size envelope of Claim C is necessary but not sufficient; the remaining obligation is a signed second-moment (energy) bound on $A_\chi$, stated below as $\mathrm{SE}$.

## Detailed reasoning

### Notation and conventions (kept two-sided)

Fix $X$ large, an active dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$, and $H_D\asymp D X^{-1/4}$. Write $\delta=\log_X D\in[1/4,1/2]$. The M2 main sum is
$$
S_2(D;t)=\sum_{1\le|h|\le H_D}\beta_{h,H_D}\sum_{d\asymp D} w_D(d)\,e\!\Big(\frac{h\,t}{4d}\Big),
$$
with the frozen Vaaler coefficients
$$
\beta_{h,H_D}=\alpha_{h,H_D}\big(e(h/4)-e(3h/4)\big),\qquad
\alpha_{h,H_D}=-\frac{\Phi(|h|/(H_D+1))}{2\pi i h},
$$
so that $\beta_{h,H_D}=-\dfrac{\Phi(|h|/(H_D+1))\,\chi_4(|h|)\,\mathbf 1_{2\nmid h}}{\pi|h|}$ is real, even in $h$, and supported on odd $h$ (from `M9-M2-beta-algebra`). Here $\chi_4$ is the nontrivial character mod $4$. The two-sided fourth moment has phase $\tfrac{t}{4}(h_1/d_1-h_2/d_2+h_3/d_3-h_4/d_4)$ and cleared resonance integer
$$
N=h_1 d_2 d_3 d_4-h_2 d_1 d_3 d_4+h_3 d_1 d_2 d_4-h_4 d_1 d_2 d_3,
$$
with denominator product $Q=d_1d_2d_3d_4\asymp D^4$ (from `M9-M2-fourth-moment-expansion`).

### Step 1: the smoothed global fourth moment and the fat band

Let $\psi$ be a smooth bump supported on $t\asymp X$ with $\int\psi=1$-normalization at scale $X$, and set
$$
M_4(D;X)=\int |S_2(D;t)|^4\,\psi(t/X)\,dt .
$$
Expanding and integrating termwise, the contribution of a 4-tuple is $\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}\,w_D(d_1)\cdots w_D(d_4)\cdot \widehat{\psi_X}(N/(4Q))$, where the substitution $t=Xs$ gives $\int e(tN/(4Q))\psi(t/X)dt = X\,\widehat\psi(XN/(4Q))$. Since $\widehat\psi$ is Schwartz, this is $\asymp X$ when $|N|\le 4Q/X\asymp D^4/X$ and negligible otherwise. This is the **global fat band**
$$
\boxed{\ 0<|N|\le C\,D^4/X\ }\qquad(\text{equivalently }|\lambda|\le C'/X,\ \lambda=\tfrac14\textstyle\sum\pm h_i/d_i).
$$
I verified symbolically that $|N|\le D^4/X\iff |\lambda|\le \tfrac14/X$ (the phase is coherent over the length-$X$ window), and that the local coherence-window analogue with window $\delta_t=X^{1/2}/D$ produces the local fat band $|N|\le D^5 X^{-1/2}$ used by `M9-M2-local-fourth-moment-kernel`. So the diagonal contributes $M_4^{\mathrm{diag}}\asymp X\cdot \Sigma_{\mathrm{diag}}$ with $\Sigma_{\mathrm{diag}}\asymp D^2$ (from the exact-$N=0$ closure `M9-M2-exact-N0-total-mass`, under H4), and the off-diagonal contributes $M_4^{\mathrm{off}}\asymp X\cdot \Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)$ once absolute values are taken.

### Step 2: the weighted fat-band mass is $D+D^4/X$, not $DH_D^3$ (Claims A, B)

This is the central correction. Two distinct quantities have been conflated in prior rounds.

**(i) Weight-blind count (Claim B).** Count fat-band tuples with all coefficients set to $1$. The extremal family takes all four denominators equal, $d_1=d_2=d_3=d_4=d\asymp D$ ($\asymp D$ choices), reducing the band condition to
$$
|h_1-h_2+h_3-h_4|\le 4d/X\le 4X^{-1/2}<1,
$$
which forces the **integer** equation $h_1-h_2+h_3-h_4=0$ exactly (since $D\le X^{1/2}$). The number of $(h_1,h_2,h_3,h_4)\in([-H_D,H_D]\cap\mathrm{odd})^4$ with $h_1+h_3=h_2+h_4$ is $\asymp H_D^3$ (standard additive count $\sum_s r(s)^2$ with $r(s)\asymp H_D$). Multiplying by the $\asymp D$ denominators gives $\asymp D H_D^3=D^4X^{-3/4}$, and I confirmed $D^4X^{-3/4}=D H_D^3$ symbolically. This crosses $D^2$ exactly at $\delta=3/8$. Hence the **weight-blind** absolute bound $\ll D^2X^\epsilon$ is false for $\delta>3/8$ -- the correct content of the Round 8 statement.

**(ii) Weighted mass (Claim A).** Now restore the actual magnitudes $|\beta_{h_i}|\asymp 1/|h_i|$. The all-$d$-equal family with $h_1+h_3=h_2+h_4$ has weight $\prod|\beta_{h_i}|\asymp 1/(|h_1 h_2 h_3 h_4|)$, and
$$
\sum_{h_1+h_3=h_2+h_4}\frac{1}{|h_1 h_2 h_3 h_4|}
=\sum_s\Big(\sum_{a+b=s}\frac{1}{ab}\Big)^{\!2}
\ll \sum_s \Big(\frac{\log s}{s}\Big)^{2}=O(1),
$$
so this family contributes $\asymp D\cdot O(1)=O(D)$ to the weighted mass. The complementary single-small-$h$ near-collision family (one frequency $|h|\asymp1$, denominators spread) contributes, by the additive-energy count against the reciprocal set $\{1/d:d\asymp D\}$ (which is AP-like with gap $\asymp 1/D^2$ and $\asymp D$ points), a window energy $\asymp D^2+(t/g)D^2$ with $t\asymp 1/X$, $g\asymp 1/D^2$, i.e. $\asymp D^2+D^4/X$; the excess-over-diagonal off-diagonal part is $\asymp D^4/X$ with weight $O(1)$. Summing over $h$ with the $1/|h|$ envelope and the per-$h$ threshold $t_h=1/(X|h|)$ does not enlarge the scale (it converges in $h$). Therefore
$$
\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\ \ll_\epsilon\ (D+D^4/X)\,X^\epsilon,
$$
which is $\ll D^2X^\epsilon$ for all $\delta\le 1/2$, with $D^4/X=D^2$ only at $\delta=1/2$. I confirmed each crossover symbolically ($D^4/X$ vs $D^2$ crosses at $\delta=1/2$; $DH_D^3$ vs $D^2$ crosses at $\delta=3/8$).

**Consequence.** The signed route is forced **not** because the weighted absolute mass blows up in the open range, but because (a) the weight-blind count blows up for $\delta>3/8$, so any argument that discards $\beta$-magnitudes (e.g. a crude $\ell^1$/triangle bound on the count, or a character-blind large-sieve input) fails there; and (b) at the endpoint $\delta=1/2$ the weighted off-diagonal $D^4/X$ ties the diagonal $D^2$, so the crude absolute bound has no margin and the pointwise upgrade (Step 4) cannot absorb the derivative loss. The signed constant $c_\chi$ must therefore produce cancellation **against the weighted $\ell^1$ envelope**, decisively at $\delta$ near $1/2$.

### Step 3: the $B\text{-}1$ signed lift envelope (Claim C)

Group the $d$-sum by reduced fractions. Writing $d=gq$, $h=gp$ with $(p,q)=1$ and $g\ge1$, the constraint $d\asymp D$, $1\le|h|\le H_D$ becomes $g\in[D/q,2D/q)$ and $|gp|\le H_D$, and
$$
A_\chi(p/q)=\sum_{\substack{gq\in[D,2D)\\ 1\le|gp|\le H_D}}\beta_{gp,H_D}\,w_D(gq).
$$
**Parity kill.** $\beta_{gp}\ne0$ requires $gp$ odd, hence $p$ odd and $g$ odd. If $p$ is even, every term vanishes and $A_\chi(p/q)\equiv0$; only odd numerators survive. This is exactly the parity support of `M9-M2-character-factor`.

**Cancellation.** For $p$ odd, $\chi_4(gp)=\chi_4(g)\chi_4(p)$, so
$$
A_\chi(p/q)=-\frac{\chi_4(p)}{\pi|p|}\sum_{\substack{g\in[D/q,2D/q)\\ g\ \mathrm{odd}}}\frac{\Phi(|gp|/(H_D+1))}{g}\,\chi_4(g)\,w_D(gq).
$$
The inner sum runs over a dyadic block of length $G\asymp D/q$ in $g$. The character $g\mapsto\chi_4(g)$ has bounded partial sums; $g\mapsto \Phi(|gp|/(H_D+1))\,w_D(gq)/g$ is of bounded variation on the block with total variation $\ll 1/G_{\min}\asymp q/D$ (using $\Phi\in C^1$ from `H4-Phi-regularity` and bounded-variation $w_D$). Abel summation gives
$$
\Big|\sum_{g\in[D/q,2D/q)}\frac{\Phi(\cdots)}{g}\chi_4(g)w_D(gq)\Big|\ \ll\ \frac{q}{D},
$$
whence $|A_\chi(p/q)|\ll (q/(D|p|))X^\epsilon$. The gain factor over the trivial $1/|p|$ is precisely the block length $1/G=q/D$. I verified the Abel/partial-summation scale and the parity kill symbolically.

**Hypotheses used (must stay visible):** (H4) coefficient normalization and $|\beta_h|\asymp1/|h|$; $\Phi\in C^1([0,1])$ with $\Phi(0)=1$, $\Phi(1)=0$, $\sup|\Phi'|<\infty$ (`H4-Phi-regularity`, itself `derived_under_assumptions` pending `H4-source-audit`); $w_D$ of bounded variation with bounded total mass; parity support $2\nmid h$. If $w_D$ is only bounded (not BV), the Abel step loses a $\log$, giving $|A_\chi|\ll (q/(D|p|))\log X$ -- still admissible.

### Step 4: why $B\text{-}1$ is only a first saving (Claim D), and the missing signed energy $\mathrm{SE}$

Define the signed off-diagonal constant of the smoothed global fourth moment schematically as
$$
c_\chi(D;X)=\frac{1}{X\,\Sigma_{\mathrm{diag}}}\Big(M_4(D;X)-M_4^{\mathrm{diag}}(D;X)\Big),
$$
the normalized signed off-diagonal remainder (with $\Sigma_{\mathrm{diag}}\asymp D^2$). Writing the off-diagonal in reduced-fraction variables, $M_4^{\mathrm{off}}$ becomes a signed bilinear form in the lift weights $A_\chi$: schematically
$$
M_4^{\mathrm{off}}\asymp X\sum_{r\ne0}\ \Big(\sum_{x+y=r}A_\chi(x)A_\chi(y)\Big)\ \mathcal K(r;X),
$$
where $x,y,r$ range over reduced fractions and $\mathcal K$ is the residual (near-collision) kernel from `M9-M2-interval-URES-strip-count`. The $B\text{-}1$ envelope controls $|A_\chi(x)|$ **pointwise**, which bounds each inner convolution by $\sum_{x+y=r}|A_\chi(x)||A_\chi(y)|$ -- an **absolute** second moment. But Step 2(ii) shows the absolute second moment is exactly the quantity that ties the diagonal at the endpoint; feeding the absolute envelope back yields no better than the $D+D^4/X$ absolute scale, i.e. no endpoint margin. To obtain $|c_\chi|\ll X^\epsilon$ one needs cancellation in the **signed** sum $\sum_{x+y=r}A_\chi(x)A_\chi(y)$ (the $\chi_4(p)$ phases in $A_\chi$ must interfere), i.e. a **signed energy bound**
$$
\mathrm{SE}:\qquad \sum_{r\ne0}\Big|\sum_{x+y=r}A_\chi(x)A_\chi(y)\Big|^2\ \ll_\epsilon\ (D^2/X)\,X^\epsilon\quad(\text{or the equivalent normalized form}),
$$
which is **open**. Claim C ($B\text{-}1$) is a necessary size input to $\mathrm{SE}$ but does not imply it. I therefore record $c_\chi$ as `proposed` with dependency on a new signed-energy obligation, and I do **not** claim it as a first-saving-implies-bound.

### Step 5: separation of the lower-bound families

I now write $\mathrm{UNC}$, $\mathrm{TS}$, $\mathrm{W}\text{-}1$ as standalone obstruction lemmas, with exact ranges and beta-envelope dependencies. All three are **weight-blind or envelope-level** and refute *absolute/unsigned* targets only; none refutes a signed estimate.

- **$\mathrm{W}\text{-}1$ (window/pigeonhole, refutes the fat band).** Statement: the weight-blind fat-band count is $\asymp DH_D^3=D^4X^{-3/4}$ (Claim B), so the count-level absolute bound $\ll D^2X^\epsilon$ fails for $\delta>3/8$. Range: $X^{3/8}<D\le X^{1/2}$. Beta dependence: none (weight-blind); with $|\beta_h|\asymp1/|h|$ upper envelope the **weighted** version is only $D+D^4/X$ (Claim A), so $\mathrm{W}\text{-}1$ must be stated at the count level to be a genuine refutation.

- **$\mathrm{UNC}$ (large-$M$ unnormalized near-collision, refutes large-$M$ GNC).** Statement: the total absolute weighted mass over **all** $N$ factorizes as $(\sum_h|\beta_h|)^4(\sum_d|w_D|)^4\asymp(\log X)^4D^4$; hence the graded absolute mass $\Sigma_{\mathrm{abs}}(0<|N|\le M)$ reaches $\asymp D^4$ once $M$ captures a constant fraction of the full range $|N|\le \max\asymp H_DD^3$. So any absolute graded target $\ll D^2X^\epsilon$ fails for large $M$ (specifically $M\gtrsim H_DD^3\cdot D^{-2}X^{?}$; the precise threshold is a diagnostic for A2/Codex execution with A3 audit). Range: all $\delta\in[1/4,1/2]$ for $M$ large. Beta dependence: uses only the $\ell^1$ envelope $\sum|\beta_h|\ll\log$, so it is envelope-level, not sign-level.

- **$\mathrm{TS}$ (twin-shift, intermediate-$M$ lower bound).** Mechanism: translations $d\mapsto d+s$ move $N$ by $\asymp sH_DD^2$; choosing $s\le M/(H_DD^2)$ lands in the band $|N|\le M$, populating intermediate $M$ with $\asymp D\cdot(M/(H_DD^2))$-many shifted tuples per base configuration. This furnishes a lower bound interpolating between the diagonal ($M\asymp D^4/X$) and $\mathrm{UNC}$ ($M$ large). Exact constant and the weighted (vs weight-blind) scale are A2/Codex diagnostics with A3 audit; as an obstruction lemma it certifies that the *shape* of $\Sigma_{\mathrm{abs}}(M)$ grows with $M$ faster than the naive diagonal extrapolation. Range: intermediate $M$, all active $\delta$.

The clean division: **$\mathrm{W}\text{-}1$ refutes the fat band ($M\asymp D^4/X$) for $\delta>3/8$ at count level; $\mathrm{UNC}$ refutes large-$M$ absolute GNC at envelope level; $\mathrm{TS}$ fills the intermediate band.** None constrains the signed $c_\chi$.

### Step 6: lower-range absolute half ($D\le X^{3/8}$)

For $\delta\le3/8$, Claim A gives weighted $\Sigma_{\mathrm{abs}}\ll D^2X^\epsilon$ and Claim B gives count $\ll D^2X^\epsilon$ as well (the count crossover is exactly $3/8$). So in the lower range the **absolute** fat-band mass is admissible even at count level, and the interval-URES strip count `M9-M2-interval-URES-strip-count` -- of the form $\ll_\epsilon X^\epsilon(1+\eta QD^2)+\Delta$ with degenerate branch $\Delta\le 4D\,\mathbf 1_{\eta\ge 1/(2D)}$ -- can in principle be assembled with dyadic lifts to bound the graded near-collision mass $\Sigma_{\mathrm{abs}}(0<|N|\le M)$ for $M\le D^4/X$. Concretely, with $\eta$ the strip half-width matched to the band $M$ via $\eta\asymp M/(QD^2)$-type scaling, the nondegenerate term $\eta QD^2\asymp M$ and the degenerate branch is off ($\eta<1/(2D)$) provided $M\lesssim Q/D\asymp D^3$, which holds for $M\le D^4/X\le D^3$ in the lower range. This suggests a **restricted absolute estimate** is feasible for $D\le X^{3/8}$; the class where it fails is precisely the degenerate branch $\eta\ge1/(2D)$, i.e. $M\gtrsim D^3$, which lies **above** the fat band in this range and so does not obstruct. I record this as a `proposed` lower-range sublemma, not a proof, pending A2/Codex $U\text{-}3\eta$ strip enumeration with A3 audit to confirm the empirical count matches $X^\epsilon(1+\eta QD^2)+\Delta$.

## Theorem-dependency audit

At least six dependencies / missing-theorem statements, each with the hypotheses that must hold:

1. **H4 (Vaaler finite approximation), `source_audit_required`.** Needed for the coefficient identity $\beta_{h,H}=-\Phi(|h|/(H+1))\chi_4(|h|)\mathbf1_{2\nmid h}/(\pi|h|)$ and the magnitude $|\beta_h|\asymp1/|h|$. Hypotheses to verify from the rendered source: Theorem 6 eq. (2.28) coefficient formula and sign; Fejer normalization; residual constant; floor-compatible endpoint convention; the beta lower envelope on dyadic blocks $|h|\asymp H_0\le H/2$. Until `H4-source-audit` is validated, every claim here is `derived_under_assumptions`.

2. **`H4-Phi-regularity`, `derived_under_assumptions`.** $\Phi\in C^1([0,1])$, $\Phi(0)=1$, $\Phi(1)=0$, $\Phi'(0)=\Phi'(1)=0$, $\sup|\Phi'|<\infty$. Used in the Abel step for $B\text{-}1$ (Claim C) and in freezing $H_D$ on windows. Missing: the exact form $\Phi(u)=\pi u(1-u)\cot(\pi u)+u$ must be confirmed from Vaaler Theorem 6 before this leaves `derived_under_assumptions`.

3. **`M9-M2-beta-algebra`, `derived_under_assumptions`.** Reality/evenness/odd-support of $\beta_h$. Depends on H4. Used throughout Steps 1--5.

4. **`M9-M2-fourth-moment-expansion`, `derived_under_assumptions`.** The cleared integer $N$ and $Q\asymp D^4$. Pure algebra given the sum shape; depends on `M9-M2-beta-algebra`.

5. **`M9-M2-exact-N0-total-mass`, `derived_under_assumptions` (under H4).** $\Sigma_{\mathrm{diag}}\ll D^2X^\epsilon$. Used to set the diagonal scale in Step 1 and the normalization of $c_\chi$ in Step 4. Not used to promote anything; kept as a conditional input.

6. **`M9-M2-subcoherence-window-multiplier` / `M9-M2-LFM-pointwise-equivalence`, `proved_internal` / `derived_under_assumptions`.** These certify that on coherence windows $\delta_t=X^{1/2}/D$ the window multiplier has no power decay and the LFM estimate equals pointwise strength. Used in Step 4 to explain why the average-to-pointwise upgrade cannot be evaded and why $c_\chi$ (a global-moment object) still needs a signed large-value/pointwise mechanism.

7. **Li--Yang 2023, `source_audit_required`.** *Not used* as a dependency in any claim above. Per the Round 9 directive, I make no theorem-level Li--Yang/Bombieri--Iwaniec compatibility claim; the exponential-sum theorem at `\label{main theorem}`, the definition of $S$, the two conditions on $F$, and the target $S/H\lesssim_\epsilon T^{\theta^*+\epsilon}$ remain to be audited from the arXiv source before any use.

8. **Missing theorem $\mathrm{SE}$ (signed energy).** Stated in Step 4; currently has no proof. This is the true gap between $B\text{-}1$ and $c_\chi$.

## Hidden assumptions and potential gaps

- **Weighted-vs-count conflation (now surfaced).** The most important hidden assumption in prior rounds was treating the fat-band refutation as a statement about weighted mass. Claim A shows the weighted mass is admissible ($D+D^4/X\ll D^2$) off the endpoint; the refutation is count-level (Claim B). Gap: I have not proved a *matching upper* bound $\Sigma_{\mathrm{abs}}\gg D^4/X$ (a lower bound on the weighted mass) at $\delta=1/2$; I only exhibited a single-$h$ family achieving $\asymp D^4/X$ up to constants. Recorded as a caveat, not a theorem.
- **Reciprocal-set AP idealization.** Step 2(ii) models $\{1/d:d\asymp D\}$ as AP-like with gap $1/D^2$. The true gaps vary; the additive-energy count is therefore heuristic-strength for the *weighted* scale. I label Claim A `derived_under_assumptions` for this reason, and I flag it as needing A2/Codex exact enumeration with A3 audit for confirmation. (My small-scale enumeration was consistent -- weighted band mass far below $D^2$ and $DH^3$ -- but the scales were too small for a clean exponent.)
- **$c_\chi$ definition ambiguity.** The schematic $c_\chi$ in Step 4 must be fixed to a single normalization (I used the normalized signed off-diagonal remainder). A2/A4 must agree on whether $c_\chi$ is normalized by $X\Sigma_{\mathrm{diag}}$ or left unnormalized before any bound is quoted.
- **Abel step and $w_D$ regularity.** Claim C needs $w_D$ of bounded variation; if the dyadic cutoff is sharp, replace by a smooth partition and absorb a $\log$. This is minor but must be stated.
- **Endpoint parity.** All claims rely on odd-$h$ support; if the source audit reveals a different parity convention in Vaaler's residual, Claims A--D shift. Flagged.

## Counterexample or obstruction search

- **Against Claim A (weighted mass $\ll D^2$).** The natural attempted counterexample is a family with many equal small frequencies and clustered denominators. I tested the all-$d$-equal family (forces $h_1+h_3=h_2+h_4$, mass $O(D)$) and the single-small-$h$ family (mass $O(D^4/X)$); neither exceeds $D^2$ off the endpoint. A genuine counterexample would need a family evading the $1/|h|$ decay, i.e. concentrating weight on $|h|\asymp1$ while also achieving count $\gg D^2$ -- but the $|h|\asymp1$ restriction caps the count at $\asymp D^4/X$ (single-frequency window energy). So no counterexample to Claim A is visible; consistent with `derived_under_assumptions`.
- **Against Claim C ($B\text{-}1$ envelope).** Potential failure: $p$ with $\chi_4(gp)$ trivial in $g$. But $\chi_4(gp)=\chi_4(g)\chi_4(p)$ for odd $g,p$, so the $g$-character is always the nontrivial $\chi_4$ (never trivial) on the odd-$g$ block; the only degeneracy is $p$ even, which gives $A_\chi\equiv0$ (not a counterexample, a vanishing). Confirmed.
- **Against the signed route generally.** The obstruction that would *kill* $c_\chi$ is a signed lower bound $|c_\chi|\gg X^\eta$ for some $\eta>0$. Producing one is exactly the adversarial-sign diagnostic now assigned to A2/Codex execution with A3 audit; I did not find an analytic construction, and the $B\text{-}1$ envelope makes a large signed $c_\chi$ require conspiratorial alignment of $\chi_4(p)$ phases across the convolution, which is not obviously achievable. This is the right target for falsification.

## Verification

- Symbolic (sympy): confirmed the scale identities $D^4/X$ (global fat band), $D^5X^{-1/2}$ (local fat band), $DH_D^3=D^4X^{-3/4}$, and the crossovers with $D^2$ at $\delta=1/2$ (weighted $D^4/X$) and $\delta=3/8$ (count $DH_D^3$).
- Symbolic: confirmed the URES exact factorization $(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3$ (residual $0$ after the constraint) and numerically on $2\times10^4$ random reduced pairs.
- Symbolic: confirmed the interval-URES strip identity with the corrected sign, $(\mu q_1-Qp_1)(\mu q_3-Qp_3)-Q^2p_1p_3=-\mu Qq_1q_3E'$ with $E'=p_1/q_1+p_3/q_3-\mu/Q$, giving $|\mathrm{defect}|\le|\mu|\eta Qq_1q_3$.
- Symbolic: confirmed the $B\text{-}1$ Abel scale (gain $=1/G=q/D$) and the parity kill ($p$ even $\Rightarrow A_\chi\equiv0$).
- Symbolic: reconstructed the derivative-obstruction bound $D^{3/5}X^{3/20}$ as the crude AP interpolation $|S_2(X_0)|\ll(M_4H_D)^{1/5}$ with $M_4\asymp D^2X$ and local$\le$global; and showed the coherence-window refinement reaches target only if the (open) signed global moment is available -- confirming it is not an unconditional route.
- Numerical (small-scale enumeration, $D\le10$): the actual $\beta$-weighted fat-band mass sits far below both $D^2$ and $DH_D^3$ and comparable to the diagonal, consistent with Claim A. Scales too small for exponent extraction -- flagged as A2/Codex diagnostic work with A3 audit, `diagnostic_only`.
- Pre-submit calibration check: no `proved` label is attached to any endpoint or M9 claim; the only `proved`-level items are the exact algebraic identities (URES factorization, strip identity, parity kill) and the count-level Claim B; all analytic magnitude claims are `derived_under_assumptions` under H4/$\Phi$-regularity.

## Divergent alternatives and 20% exploration

Kept deliberately narrow (free exploration is a Round 11 allowance; here I only flag serious alternatives with a falsification test each).

- **Dual equivalence of the two signed routes.** The judge asked whether the sign-preserving Poisson/Voronoi route and the $c_\chi$ route are the same dual obstruction. Observation: both reduce to controlling a signed bilinear form in the lift weights $A_\chi$ -- the Poisson route in the *frequency* dual variable $k$, the $c_\chi$ route in the *difference* variable $r=x+y$. If the stationary-phase map of the Poisson route sends $k\leftrightarrow r$ bijectively at the leading term, the two signed energies $\mathrm{SE}$ coincide. **Falsification test:** compare the leading signed kernel $\mathcal K(r;X)$ from `M9-M2-interval-URES-strip-count` against the leading stationary-phase kernel of the Poisson route at a single dyadic $r$; if their $r$-dependence differs by more than an $X^\epsilon$ factor, the routes are genuinely different and must be pursued separately. Needed lemma: an exact stationary-phase expansion with boundary/$k=0$/support-edge terms (currently only `proposed`).
- **Signed large-sieve input for $\mathrm{SE}$.** A candidate for $\mathrm{SE}$ is a large-sieve inequality for the $\chi_4$-twisted lift weights over reduced fractions with denominators $\le 2D$. **Falsification test:** check whether the dual spacing of the reduced-fraction set $\{p/q:q\le 2D\}$ supports a large-sieve bound with constant $\ll D^2$ (the target normalization); if the minimal spacing forces a constant $\gg D^{2+\eta}$, the large-sieve route cannot reach $|c_\chi|\ll X^\epsilon$ and must be replaced by a genuinely arithmetic (divisor-structured) energy bound. This connects to `M9-M2-URES-energy-reduction`, already `proved_internal` at the *absolute* level -- the open step is its **signed** analogue.

## Useful lemmas

- **Lemma A4-9.1 [DERIVED-UNDER-ASSUMPTIONS] (weighted fat-band mass).** Under H4/$\Phi$-regularity/bounded $w_D$, $\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)\ll_\epsilon(D+D^4/X)X^\epsilon$; hence $\ll D^2X^\epsilon$ for $\delta\le1/2$, tight only at $\delta=1/2$.
- **Lemma A4-9.2 [PROVED, count-level] (weight-blind fat-band count).** $\#\{0<|N|\le D^4/X\}\asymp DH_D^3=D^4X^{-3/4}$; count-level absolute bound $\ll D^2X^\epsilon$ fails iff $\delta>3/8$.
- **Lemma A4-9.3 [DERIVED-UNDER-ASSUMPTIONS] ($B\text{-}1$ envelope).** For reduced $p/q$: $A_\chi(p/q)\equiv0$ if $p$ even; $|A_\chi(p/q)|\ll_\epsilon(q/(D|p|))X^\epsilon$ if $p$ odd, by Abel summation against $\chi_4$ with gain $1/G=q/D$.
- **Lemma A4-9.4 [DERIVED-UNDER-ASSUMPTIONS] ($c_\chi$ requires signed energy).** $B\text{-}1$ bounds each $|A_\chi|$ but the absolute convolution ties the diagonal at $\delta=1/2$; $|c_\chi|\ll X^\epsilon$ requires the signed energy bound $\mathrm{SE}$ (open).
- **Obstruction A4-9.5 (family separation).** $\mathrm{W}\text{-}1$ (count-level, refutes fat band for $\delta>3/8$), $\mathrm{UNC}$ (envelope-level, refutes large-$M$ absolute GNC), $\mathrm{TS}$ (intermediate-$M$ filler) -- none refutes a signed estimate.

## What should be tested next

- **A2/Codex diagnostics with A3 audit (`diagnostic_only`).** (i) Confirm Lemma A4-9.1 numerically: compute $\Sigma_{\mathrm{abs}}(0<|N|\le D^4/X)/D^2$ with actual $\beta_h$ across $\delta$ around $3/8$ and at $\delta=1/2$, separating weighted mass from raw count, to test $D+D^4/X$ vs $DH_D^3$. (ii) $U\text{-}3\eta$ strip enumeration including the degenerate branch, comparing to $X^\epsilon(1+\eta QD^2)+\Delta$. (iii) Compute $c_\chi(D;X)$, its unsigned/random-sign/adversarial-sign analogues, and endpoint sign ratios, with executed script, `py_compile` log, exact command, versions, precision, tables, `report.md`, and pass/fail assertions.
- **A2 (referee).** Audit Lemma A4-9.1's reciprocal-AP idealization and the $c_\chi$ normalization; state $\mathrm{SE}$ precisely and decide whether $B\text{-}1$ plus a divisor-structured energy suffices or a large-sieve input is required.
- **A1 (proof draft / source cards).** Complete `H4-source-audit` (needed to move Lemmas A4-9.1, A4-9.3 off `derived_under_assumptions`); insert the count-vs-weight distinction into the draft so the refutation is stated at the correct (count) level.

## Proposed state patch, if any

Ids from `state/proof_obligations.yml`. I propose (for the judge to decide):

- **Update `M9-near-collision-absolute-lower-bounds`**: record the scoping correction -- the fat-band refutation is **count-level** ($DH_D^3=D^4X^{-3/4}$, crossover $\delta=3/8$); the $\beta$-weighted absolute fat-band mass is $\ll D^2X^\epsilon$ for $\delta\le1/2$ (tight only at $\delta=1/2$). Split into standalone `M9-M2-UNC-large-M-lower-bound`, `M9-M2-TS-twin-shift-lower-bound`, `M9-M2-W1-window-count-lower-bound` (all `derived_under_assumptions`/`proved_internal` at count/envelope level), with exact ranges and the note that none refutes a signed estimate.
- **Update `M9-M2-signed-lift-cancellation-B1`** (keep `derived_under_assumptions`): add the parity-kill ($p$ even $\Rightarrow A_\chi\equiv0$) and the Abel-gain statement $1/G=q/D$; add explicit $w_D$-BV hypothesis.
- **Update `M9-M2-signed-fat-band-constant`** (keep `proposed`): add the dependency on a new obligation `M9-M2-signed-lift-energy-SE` (signed second moment of $A_\chi$), and record that $B\text{-}1$ is a first saving, not sufficient.
- **Create `M9-M2-signed-lift-energy-SE`** (`proposed`, owner A2/A4): the signed energy bound stated in Step 4; blockers `H4-source-audit`, `M9-M2-signed-fat-band-constant`.
- **Create `M9-M2-lower-range-absolute-restricted`** (`proposed`, owner A4): the restricted absolute estimate for $D\le X^{3/8}$ via interval-URES strip count; blocker `H4-source-audit`; next action = A2/Codex $U\text{-}3\eta$ confirmation with A3 audit.
- **No change** to `M9`, `M9-M1`, `M9-M2`, `GC-target`, `Conditional-bridge`, `H4`, `H4-source-audit`, `Li-Yang-source-audit`.

## Confidence

- Lemma A4-9.2 (weight-blind count $DH_D^3$, crossover $3/8$): high (exact additive count + symbolic crossover).
- URES factorization, interval strip identity, $B\text{-}1$ parity kill: high (symbolic + numeric identity checks).
- Lemma A4-9.1 (weighted mass $\ll D^2$ off endpoint): moderate -- the reciprocal-AP additive-energy step is heuristic-strength and needs A2/Codex confirmation with A3 audit; hence `derived_under_assumptions`.
- Lemma A4-9.3 ($B\text{-}1$ Abel scale): moderate-to-high, contingent on `H4-Phi-regularity` and $w_D$ regularity.
- Lemma A4-9.4 ($c_\chi$ needs signed energy $\mathrm{SE}$): moderate -- the schematic bilinear reduction is standard but the exact kernel identification with `M9-M2-interval-URES-strip-count` is not fully written.
- Overall numeric confidence capped at 0.85. No endpoint, `M9`, `M9-M2`, `M9-M1`, or Gauss-circle claim is made or promoted. token-family scan: passed

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 9.

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
