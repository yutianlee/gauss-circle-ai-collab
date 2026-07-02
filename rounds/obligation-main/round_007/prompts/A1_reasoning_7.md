You are ChatGPT Extended Pro, acting as broad strategist, literature scout, proof synthesizer, and default judge.

We are running a public GitHub based multi-AI mathematics research workflow.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

Follow the protocol and be strict about separating proved claims from conjectural ideas.

## Agent-Specific Instructions

Use ChatGPT Extended Pro. Act as a research strategist and, when judging, as the conservative synthesis writer. For the Gauss circle problem, prioritize exact normalizations, Poisson/Bessel formulas, hyperbola decompositions, Vaaler/Fejer residuals, exponent-pair or Bombieri-Iwaniec hypotheses, smoothing/unsmoothing losses, and literature status. When web search is available, cite exact theorem statements, authors, publication data, and URLs/DOIs/arXiv links. If web search is unavailable, say so and do not invent citations. In reasoning, spend about 80% on the judge-assigned main route and about 20% on serious alternative routes or obstruction searches. Include a dedicated route-proposal section: give at least two serious proof routes, the exact lemma each route would need, why it might work, what obstruction it attacks, and what would falsify it quickly. In review, assess A2, A3, and A4 separately and recommend research-strategy adjustments. As judge, compare route proposals explicitly, select one primary route and one backup route, write concrete next-round prompts for A1, A2, A3, and A4, and split agent scoring into idea quality, state evidence, and calibration.

## Raw Markdown Copy-Response Safety Rule

Your final answer must be one single fenced Markdown code block:

````text
```markdown
## Summary
...
```
````

Do not write anything before or after that outer fence. Inside the fence, write normal Markdown and raw LaTeX source using `$...$` and `$$...$$`.

Do not use additional triple-backtick fences inside your answer. This rule is required because web Copy response can corrupt rendered display math, turning `=` into `====` and minus/fraction bars into long dashed lines.

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

## Reasoning-Stage Guardrail

This is an independent reasoning stage, not a review stage.

Use the previous rounds only as background state and judge instructions. Do not evaluate "other agents' outputs" as your primary task, and do not use review-stage headings such as:

- `Most valuable input from others`
- `Claims that look correct`
- `Claims that need proof`
- `Score by agent`
- `Suggested synthesis`

If your draft begins with a review heading, discard that draft and rewrite it as independent reasoning using the required reasoning schema below. Start from a new mathematical claim, derivation, obstruction check, lemma statement, or concrete test.

Exploration budget: spend about 80% of the answer on the assigned route and about 20% on alternative proof ideas or obstruction searches. The divergent part must be mathematically serious: state why each alternative might work, what exact lemma would be needed, and what quick test could falsify it.



## Agent Depth Contract

Write a deep long-form reasoning attempt, not a summary. Include precise claim statements, parameter ranges, derivations, gap labels, falsification tests, and a 20% section for divergent alternatives such as a different decomposition, a dual formulation, a sign-preserving spacing statistic, a Mellin-Perron route, a smoothed cutoff route, or a computational certificate. Include `## Route proposals` with at least two serious routes. For each route, state the exact proof obligation or lemma, dependencies, first proof step, likely obstruction, and falsification test. Rank the routes by plausibility and expected proof-graph impact. If web search is available, include a literature-check section with exact theorem statements and sources; if unavailable, state that limitation clearly.

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
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ]
      },
      "owner": "A1",
      "next_action": "Commit sources/vaaler_1985.md with bibliographic data, DOI 10.1090/S0273-0979-1985-15349-2, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, and the M2 single-parity support check.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/responses/A4-006.md"
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
          "rounds/obligation-main/round_006/responses/A3-006.md"
        ]
      },
      "owner": "A2",
      "next_action": "Record fraction-matching versus official semi-diagonal terminology. Treat reduced-paired exact resonances under H4, then attack URES; do not promote full taxonomy until mixed and residual exact N=0 are bounded.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "Recast as a graded global estimate: prove or refute Sigma_abs(0<|N|<=M) <<_epsilon D^2 max(1, M X/D^4) X^epsilon for all relevant M, with signed variants separately marked. Do not infer this from DP or exact N=0 subfamilies.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/reviews/A1.md"
        ]
      },
      "owner": "A3",
      "next_action": "Fix the complex-weight B_{-1} relation before running. Then execute the raw two-sided M2, complex-weight cosine pairing, real-weight Re B_h formula, and deliberate complex-weight Re B_h failure tests with exact Phi or explicitly marked surrogate Phi until H4 validates Phi.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
        "M9-M2-fourth-moment-average-to-pointwise",
        "M9-M2-fraction-matching-weighted-bound",
        "M9-M2-local-fourth-moment-LFM"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md"
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
      "next_action": "Do not promote from paired or fraction-matching subfamilies. Prove or refute mixed and unpaired exact N=0 mass before any status change.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_006/responses/A4-006.md"
        ],
        "inconclusive": [
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_004/judge/judge-004.md",
          "rounds/obligation-main/round_005/responses/A1-005.md",
          "rounds/obligation-main/round_006/responses/A1-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Keep AP as a calculus interpolation module. Re-scope average-to-pointwise around subcoherence: local windows give no power saving, so pursue either global moment plus large-value propagation away from endpoint or direct signed endpoint control.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/responses/A3-006.md"
        ]
      },
      "owner": "A3",
      "next_action": "Before execution fix the d=7 imaginary-part sign, the complex-weight relation B_{-1}=(1+i)conj(Sigma), and the envelope sup_I |S_2'| << H_D. Then materialize and run exact integer diagnostics for DP parity, DP thin mass, URES residual including (6,10,15,5)k, reduced-paired overlap, local-window equivalence, and signed-vs-unsigned beta comparisons. Archive script, command, tables, precision log, report, and assertions.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/reviews/A3.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Transcribe DP-0 through DP-3 into best_proof_draft.md with dyadic constants, C0 dependence, exact H4 parity/magnitude dependencies, and edge cases. Keep H4-source-audit as blocker.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/responses/A4-006.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Attach A4's NF-1 compact statement to the lemma bank and use NF-2 for URES.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/reviews/A1.md"
        ]
      },
      "owner": "A4",
      "next_action": "State the exact sign-preserving spacing theorem required for theta_d=X/(4d), define P(D,H;X), and require A3 to compare true beta signs with unsigned, random, and adversarial signs before further proof investment.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/reviews/A3.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Write NF-2 in lemma-bank notation and use it as the first tool for URES; do not cite randomized checks as proof.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/reviews/A3.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A4",
      "next_action": "Transcribe U-2, SS, anti-paired, and fraction-matching coverage in set-theoretic form; verify overlap bookkeeping before using this lemma in any full taxonomy claim.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
    },
    {
      "id": "M9-M2-unpaired-residual-URES",
      "type": "lemma",
      "track": "M9_analytic",
      "title": "URES residual exact-resonance bound",
      "status": "open",
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
      "blockers": [],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_006/responses/A4-006.md",
          "rounds/obligation-main/round_006/reviews/A1.md",
          "rounds/obligation-main/round_006/reviews/A2.md",
          "rounds/obligation-main/round_006/reviews/A3.md",
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use NF-2 to prove the R(r)^2 bound or produce a lower-bound family exceeding the D^2 X^epsilon budget. A3 should enumerate this residual first.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
          "rounds/obligation-main/round_006/judge/judge-006.md"
        ]
      },
      "owner": "A2",
      "next_action": "State exact stationary phase, boundary terms, k=0 terms, dual m-range m asymp hX/D^2, amplitudes, and the first sign-preserving post-transform estimate; keep as proposed until then.",
      "last_updated_round": 6,
      "last_updated_at": "2026-07-03T01:57:58"
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
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 6 in run `obligation-main`.

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
  Next action: Record fraction-matching versus official semi-diagonal terminology. Treat reduced-paired exact resonances under H4, then attack URES; do not promote full taxonomy until mixed and residual exact N=0 are bounded.
- `M9-regression-raw-vs-paired` (diagnostic_only, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Fix the complex-weight B_{-1} relation before running. Then execute the raw two-sided M2, complex-weight cosine pairing, real-weight Re B_h formula, and deliberate complex-weight Re B_h failure tests with exact Phi or explicitly marked surrogate Phi until H4 validates Phi.

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

created: H4-Phi-regularity, M9-M2-local-fourth-moment-kernel, M9-M2-LFM-endpoint-degeneracy, M9-M2-subcoherence-window-multiplier, M9-M2-LFM-pointwise-equivalence, M9-M2-NF-participation-rigidity, M9-M2-unpaired-reduced-paired-bound, M9-M2-unpaired-residual-URES, M9-M2-sign-preserving-poisson-voronoi-route; updated: H4-source-audit, M9-M2-DP-near-collision-bound, M9-M2-coprime-rigidity-normal-form, M9-M2-local-fourth-moment-LFM, M9-M2-fourth-moment-average-to-pointwise, M9-near-collision-taxonomy, M9-near-collision-estimate, M9-fourth-moment-enumeration, M9-regression-raw-vs-paired, M9-M2-reciprocal-SPD-route, M9-M2-beta-algebra; rejected: A2-R6-unpaired-exact-N0-mass-bound-derived, A2-R6-cleared-phase-non-separability-route-closing, A2-R6-poisson-voronoi-as-proof-evidence, A3-R6-unexecuted-artifact-positive-evidence, A3-R6-unclassified-mass-pass-fail; no_change: M9, M9-M1, M9-M2, GC-target, Conditional-bridge, H4, R5-Full, Li-Yang-source-audit, M9-M2-character-factor; round score: 4; Round 6 makes modest proof-graph-safe progress by adding the local kernel, the whole-range subcoherence obstruction with endpoint degeneration as a corollary, a validator-ready DP update, NF-2 rigidity, reduced-paired exact-resonance control under H4, and a precise URES residual target. It does not prove M9, M9-M2, M9-M1, the full taxonomy, near-collision estimates, or the final target.

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
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-unpaired-residual-URES`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-NF-participation-rigidity`
- Next action: Record fraction-matching versus official semi-diagonal terminology. Treat reduced-paired exact resonances under H4, then attack URES; do not promote full taxonomy until mixed and residual exact N=0 are bounded.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `diagnostic_only`
- Track: `computation`
- Owner: `A3`
- Next action: Fix the complex-weight B_{-1} relation before running. Then execute the raw two-sided M2, complex-weight cosine pairing, real-weight Re B_h formula, and deliberate complex-weight Re B_h failure tests with exact Phi or explicitly marked surrogate Phi until H4 validates Phi.

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
- Next action: Commit sources/vaaler_1985.md with bibliographic data, DOI 10.1090/S0273-0979-1985-15349-2, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, and the M2 single-parity support check.

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

### M9-M2-N0-diagonal-core-bound: Diagonal-core bound for exact M2 fourth-moment resonances

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-fraction-matching-weighted-bound`, `M9-M2-local-fourth-moment-LFM`
- Next action: Do not promote from paired or fraction-matching subfamilies. Prove or refute mixed and unpaired exact N=0 mass before any status change.

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
- Next action: Keep AP as a calculus interpolation module. Re-scope average-to-pointwise around subcoherence: local windows give no power saving, so pursue either global moment plus large-value propagation away from endpoint or direct signed endpoint control.

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
- Next action: State the exact sign-preserving spacing theorem required for theta_d=X/(4d), define P(D,H;X), and require A3 to compare true beta signs with unsigned, random, and adversarial signs before further proof investment.

### M9-M2-sign-preserving-poisson-voronoi-route: Sign-preserving Poisson or B-process route for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `Li-Yang-source-audit`
- Next action: State exact stationary phase, boundary terms, k=0 terms, dual m-range m asymp hX/D^2, amplitudes, and the first sign-preserving post-transform estimate; keep as proposed until then.

### M9-M2-unpaired-residual-URES: URES residual exact-resonance bound

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Use NF-2 to prove the R(r)^2 bound or produce a lower-bound family exceeding the D^2 X^epsilon budget. A3 should enumerate this residual first.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Require each M2 route to isolate the endpoint D=X^(1/2), where the AP/local-average bridge degenerates to pointwise control.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Recast as a graded global estimate: prove or refute Sigma_abs(0<|N|<=M) <<_epsilon D^2 max(1, M X/D^4) X^epsilon for all relevant M, with signed variants separately marked. Do not infer this from DP or exact N=0 subfamilies.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Generated after round 6 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_006/judge/judge-006.md`.

## For A1

Target obligations: `H4-source-audit`, `H4-Phi-regularity`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-local-fourth-moment-kernel`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`, proof-draft maintenance.

Objectives:

1. Physically draft or commit `sources/vaaler_1985.md`. Include:
   - bibliographic data and DOI;
   - local PDF path;
   - Theorem 6 equation (2.28);
   - Section 7 equations (7.1)--(7.3);
   - Theorem 18 equations (7.13)--(7.17);
   - coefficient sign;
   - Fejer normalization;
   - residual constant;
   - floor-compatible endpoint convention;
   - $\Phi$ regularity;
   - the M2 single-parity support check from the $\rho=1,3$ difference.

2. Insert into `state/best_proof_draft.md`:
   - H1--H3;
   - H4 as source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - M1/M2 definitions;
   - beta algebra;
   - raw two-sided, complex-weight cosine, and real-weight paired M2 formulas;
   - fourth-moment numerator $N$;
   - local kernel;
   - endpoint degeneracy;
   - subcoherence-window multiplier and LFM-pointwise equivalence;
   - DP-0 through DP-3;
   - NF-1/NF-2;
   - reduced-paired bound;
   - URES residual target.

3. Write a proof-draft note explaining that `(LFM)` is no longer the primary relaxed route: coherence windows provide no power-saving multiplier, and endpoint control must come from signed pointwise or global-moment/large-value propagation.

4. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `GC-target`, and `H4` unpromoted.

Exploratory allocation: compare three route maps in one page:
- URES exact-resonance route;
- graded global near-collision/moment route;
- SPD or sign-preserving Poisson endpoint route.

For each, state the exact theorem needed and one falsification test.

## For A2

Target obligations: `M9-M2-unpaired-residual-URES`, `M9-near-collision-taxonomy`, `M9-M2-sign-preserving-poisson-voronoi-route`.

Objectives:

1. Attack URES only. Do not re-prove denominator-paired, pair-swapped, or fraction-matching subfamilies.

2. Use NF-2 explicitly. For each reduced value $r=\mu/Q$, bound the possible reduced fractions $x_1=p_1/q_1$ with $x_3=r-x_1$ and $q_3\le2D$ using

$$
q_3\ge \frac{Qq_1}{\gcd(Q,q_1)^2}.
$$

3. Produce one of:
   - a proof of $\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon$;
   - a lower-bound family exceeding the budget;
   - a rigorous reduction to a smaller divisor-sum problem with all lifts and beta weights stated.

4. If using the Poisson/B-process route, supply the exact transformed object:
   - sign of the dual variable;
   - stationary point;
   - amplitude;
   - boundary terms;
   - $k=0$ terms;
   - dual range $m\asymp hX/D^2$;
   - the first signed theorem that would imply `M9-M2`.

5. Do not label any unpaired mass bound `derived_under_assumptions` unless all lifts, signs, reduced denominators, overlaps, and dyadic endpoints are handled.

Exploratory allocation: write one sign-preserving endpoint lemma for the top block $D\asymp X^{1/2}$ using the expansion $d=\lfloor X^{1/2}\rfloor+m$, but keep it `proposed` unless fully proved.

## For A3

Target obligations: `M9-fourth-moment-enumeration`, `M9-regression-raw-vs-paired`, `M9-M2-local-fourth-moment-LFM` diagnostics, `M9-M2-reciprocal-SPD-route`.

Objectives:

1. Execute, not plan. Required deliverables:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - `python -m py_compile` result;
   - precision log;
   - CSV schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Use exact integer arithmetic for $N$ and exact rational reduction for $h_i/d_i=p_i/q_i$.

3. First required tables:
   - DP parity/no-small-nonzero-$N$ check;
   - DP thin mass compared to $C_0D\log^2(2H)$;
   - URES residual enumeration including $(6,10,15,5)k$;
   - $R(r)^2$ concentration;
   - reduced-paired versus residual exact mass.

4. Formula regression:
   - raw two-sided M2;
   - complex-weight cosine pairing;
   - real-weight $\operatorname{Re}B_h$ pairing;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

5. Local-window diagnostics:
   - compute $\max \delta|\lambda|$;
   - compare $\delta^{-1}\int_I |S_2|^4$ to local sup;
   - include $D=X^{1/4},X^{3/8},X^{1/2}$.

6. Before running any diagnostic, fix the $d=7$ imaginary-part sign, the complex-weight relation $B_{-1}=(1+i)\overline{\Sigma}$, and the envelope $\sup_I |S_2'|\ll H_D$.

7. SPD diagnostics:
   - compute $P(D,H;X)$;
   - compare true beta signs, unsigned signs, random signs, and adversarial signs.

All outputs remain `diagnostic_only`.

## For A4

Target obligations: `M9-M2-DP-near-collision-bound`, `M9-M2-coprime-rigidity-normal-form`, `M9-M2-NF-participation-rigidity`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-unpaired-residual-URES`, `M9-M2-reciprocal-SPD-route`.

Objectives:

1. Write validator-ready statements and proofs for:
   - DP-0 parity;
   - DP-1 thin-band emptiness;
   - DP-2 thin DP mass;
   - DP-3 full DP total mass;
   - exact H4 dependency split.

2. Insert NF-1 and NF-2 in lemma-bank form. NF-2 must include all definitions:

$$
g=\gcd(Q,q_1),\quad
\widehat Q=Q/g,\quad
\widehat q_1=q_1/g,\quad
M=\mu\widehat q_1-p_1\widehat Q.
$$

3. Verify overlap bookkeeping for U-2, SS, anti-paired, and fraction-matching coverage of all exact $N=0$ tuples with reduced-denominator multiset $\{q,q,q',q'\}$.

4. Attack URES jointly with A2:
   - attempt a proof of $\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon$;
   - or produce a counterexample/lower-bound family;
   - or reduce it to a named divisor-sum inequality.

5. Develop SPD only as backup. State the exact theorem required for reciprocal points $\theta_d=X/(4d)$ and give A3 a falsification threshold.

Exploratory allocation: formulate a global-moment/large-value propagation map for sub-endpoint ranges $D\le X^{1/2-\eta}$, with all assumptions marked as proposed or diagnostic unless proved.

## Round Assessment

Round 6 produced real proof-graph progress, but not endpoint proof.

Agent scores:

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 7.0 | 9.0 | Strong source-card draft, $\Phi$ regularity, M2 formulas, local kernel, and endpoint degeneracy. Correctly avoided endpoint overclaim. A4's subcoherence result supersedes the endpoint-only framing. |
| A2 | 7.2 | 3.8 | 5.8 | Good terminology separation and useful exploratory Poisson/B-process idea. The unpaired mass bound is not proved, and the nonseparability obstruction is over-scoped if treated as route-closing. |
| A3 | 7.0 | 2.5 | 7.5 | Useful diagnostic architecture and correct diagnostic-only attitude, but no executed artifact. Formula and classifier issues must be fixed before evidence is positive. |
| A4 | 9.0 | 8.0 | 8.5 | Strongest analytic contribution: DP suite, NF-2, subcoherence-window equivalence, reduced-paired exact-resonance bounds, and URES residual definition. Some overlap bookkeeping still needs proof-draft verification. |

Split round scores:

- idea quality: 8/10;
- state evidence: 6/10;
- calibration: 8/10;
- mathematical progress: 5/10.

The proof graph gains narrower lemmas and a better obstruction map. It does not gain `M9-M2`, `M9`, or the final theorem.

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

## Judge-Assigned Reasoning Prompt For This Agent

Target obligations: `H4-source-audit`, `H4-Phi-regularity`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-local-fourth-moment-kernel`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`, proof-draft maintenance.

Objectives:

1. Physically draft or commit `sources/vaaler_1985.md`. Include:
   - bibliographic data and DOI;
   - local PDF path;
   - Theorem 6 equation (2.28);
   - Section 7 equations (7.1)--(7.3);
   - Theorem 18 equations (7.13)--(7.17);
   - coefficient sign;
   - Fejer normalization;
   - residual constant;
   - floor-compatible endpoint convention;
   - $\Phi$ regularity;
   - the M2 single-parity support check from the $\rho=1,3$ difference.

2. Insert into `state/best_proof_draft.md`:
   - H1--H3;
   - H4 as source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - M1/M2 definitions;
   - beta algebra;
   - raw two-sided, complex-weight cosine, and real-weight paired M2 formulas;
   - fourth-moment numerator $N$;
   - local kernel;
   - endpoint degeneracy;
   - subcoherence-window multiplier and LFM-pointwise equivalence;
   - DP-0 through DP-3;
   - NF-1/NF-2;
   - reduced-paired bound;
   - URES residual target.

3. Write a proof-draft note explaining that `(LFM)` is no longer the primary relaxed route: coherence windows provide no power-saving multiplier, and endpoint control must come from signed pointwise or global-moment/large-value propagation.

4. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `GC-target`, and `H4` unpromoted.

Exploratory allocation: compare three route maps in one page:
- URES exact-resonance route;
- graded global near-collision/moment route;
- SPD or sign-preserving Poisson endpoint route.

For each, state the exact theorem needed and one falsification test.

## Your Task For Round 7

Continue the research from the current state. Make concrete progress on the judge's next-round instructions, and be explicit about proof gaps.

Work against the proof-obligation graph. If you propose a mathematical state change, describe it under `## Proposed state patch, if any` using ids from `state/proof_obligations.yml`; the judge will decide whether to include it in the formal State Patch.



## Required Output Schema

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
