You are ChatGPT Extended Pro, acting as broad strategist, literature scout, proof synthesizer, and default judge.

We are running a public GitHub based multi-AI mathematics research workflow.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

Follow the protocol and be strict about separating proved claims from conjectural ideas.

## Agent-Specific Instructions

Use ChatGPT Extended Pro. Act as a research strategist and, when judging, as the conservative synthesis writer. For the Gauss circle problem, prioritize exact normalizations, Poisson/Bessel formulas, hyperbola decompositions, Vaaler/Fejer residuals, exponent-pair or Bombieri-Iwaniec hypotheses, smoothing/unsmoothing losses, and literature status. When web search is available, cite exact theorem statements, authors, publication data, and URLs/DOIs/arXiv links. If web search is unavailable, say so and do not invent citations. In reasoning, spend about 80% on the judge-assigned main route and about 20% on serious alternative routes or obstruction searches. Include a dedicated route-proposal section: give at least two serious proof routes, the exact lemma each route would need, why it might work, what obstruction it attacks, and what would falsify it quickly. In review, assess A2 and A3 separately and recommend research-strategy adjustments. As judge, compare route proposals explicitly, select one primary route and one backup route, write concrete next-round prompts for A1, A2, and A3, and split agent scoring into idea quality, state evidence, and calibration.

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
        "M9-M2-N0-diagonal-core-bound"
      ],
      "evidence": {
        "positive": [],
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_002/human/stage-b-review-audit.md"
        ],
        "inconclusive": [
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A2-2.md",
          "rounds/obligation-main/round_002/responses/A2-002.md"
        ]
      },
      "owner": "A2",
      "next_action": "Complete the exact N=0 taxonomy using the corrected numerator N and actual beta_h weights. Resolve or explicitly preserve the unclassified class, prove or downgrade denominator-paired estimates, and formulate near-collision bands using |N| lesssim D^4/X.",
      "last_updated_round": 2,
      "last_updated_at": "2026-06-26T03:16:11"
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
          "rounds/web-research-test/round_028/responses/A3-028.md",
          "rounds/round_001/responses/A3.md",
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/responses/A3-002.md",
          "rounds/obligation-main/round_002/reviews/A1.md"
        ]
      },
      "owner": "A3",
      "next_action": "Produce committed or repository-ready artifacts: computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and computations/m9_regression/report.md. Use the official M1/M2 raw formulas and actual Vaaler coefficients; label all evidence diagnostic_only.",
      "last_updated_round": 2,
      "last_updated_at": "2026-06-26T03:16:11"
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
      "next_action": "Verify the exact H4 coefficient convention from the Vaaler source card and then insert the beta_h algebra into the proof draft.",
      "last_updated_round": 1,
      "last_updated_at": "2026-06-26T01:40:44"
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
          "rounds/obligation-main/round_002/responses/A1-002.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/obligation-main/round_001/judge/judge-001.md",
          "rounds/obligation-main/round_002/responses/A2-002.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use this only as an algebraic expansion. A2 should classify exact and near-collision configurations with actual beta_h weights; do not infer an analytic estimate from the expansion alone.",
      "last_updated_round": 2,
      "last_updated_at": "2026-06-26T03:16:11"
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
        "H4-source-audit"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_002/responses/A2-002.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_002/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_002/judge/judge-002.md"
        ]
      },
      "owner": "A2",
      "next_action": "Prove the bound with actual beta_h weights, bounded dyadic weights, explicit overlap conventions, and the H4 coefficient bound; do not use the incorrect 1/16 constant for the whole union.",
      "last_updated_round": 2,
      "last_updated_at": "2026-06-26T03:16:11"
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
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 2 in run `obligation-main`.

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
  Next action: Complete the exact N=0 taxonomy using the corrected numerator N and actual beta_h weights. Resolve or explicitly preserve the unclassified class, prove or downgrade denominator-paired estimates, and formulate near-collision bands using |N| lesssim D^4/X.
- `M9-regression-raw-vs-paired` (proposed, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Produce committed or repository-ready artifacts: computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and computations/m9_regression/report.md. Use the official M1/M2 raw formulas and actual Vaaler coefficients; label all evidence diagnostic_only.

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

created: M9-M2-N0-diagonal-core-bound; updated: M9-M2-character-factor, M9-near-collision-taxonomy, M9-regression-raw-vs-paired, M9-M2-fourth-moment-expansion; rejected: A2-R2-near-collision-taxonomy-promotion, A2-R2-denominator-paired-negligibility-proved, A2-R2-dual-length-explosion-route-closing, A2-R2-diagonal-core-one-sixteenth-union-constant, A3-R2-artifact-evidence-without-files, A3-R2-official-formula-normalization-unverified; no_change: M9, M9-M1, M9-M2, M9-near-collision-estimate, M9-endpoint-uniformity, GC-target, H4, H4-source-audit, Li-Yang-source-audit; round score: 3; Round 2 made useful algebraic and strategic progress on M2 and identified the fourth-moment route as primary, but no endpoint estimate, complete taxonomy, near-collision bound, or executable computation evidence was supplied.

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
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`
- Next action: Complete the exact N=0 taxonomy using the corrected numerator N and actual beta_h weights. Resolve or explicitly preserve the unclassified class, prove or downgrade denominator-paired estimates, and formulate near-collision bands using |N| lesssim D^4/X.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `proposed`
- Track: `computation`
- Owner: `A3`
- Next action: Produce committed or repository-ready artifacts: computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and computations/m9_regression/report.md. Use the official M1/M2 raw formulas and actual Vaaler coefficients; label all evidence diagnostic_only.

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

### M9-M2-N0-diagonal-core-bound: Diagonal-core bound for exact M2 fourth-moment resonances

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`
- Next action: Prove the bound with actual beta_h weights, bounded dyadic weights, explicit overlap conventions, and the H4 coefficient bound; do not use the incorrect 1/16 constant for the whole union.

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

### M9-M2-beta-algebra: Exact beta_h coefficient algebra for M2

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Verify the exact H4 coefficient convention from the Vaaler source card and then insert the beta_h algebra into the proof draft.

### M9-M2-fourth-moment-expansion: Algebraic fourth-moment expansion for M2 with retained character product

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`
- Next action: Use this only as an algebraic expansion. A2 should classify exact and near-collision configurations with actual beta_h weights; do not infer an analytic estimate from the expansion alone.

### M9-M2-h-cauchy-sign-loss: Weighted h-Cauchy loses the M2 frequency character sign

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Next action: Use this only as a diagnostic. A2 should test fourth moments, CRI, or direct signed bilinear estimates rather than treating this as a no-go theorem.

### R5-Full: Fejer residual product-count bound

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Insert the proof with edge cases into the best proof draft after H4 source audit is complete.

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Generated after round 2 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_002/judge/judge-002.md`.

## For A1

Target obligations: `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, `M9-M2-N0-diagonal-core-bound`, and state maintenance.

Objectives:

1. Insert the proof-draft-ready $\mathcal M_2$ coefficient normalization into the proof draft, preserving H4 dependency:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   \beta_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h}.
$$

2. State the raw two-sided formula and the paired real formula, with the real-weight hypothesis explicit.

3. Write the fourth-moment expansion using the exact coefficient product and corrected numerator $N$.

4. Add a small lemma-bank entry for `M9-M2-N0-diagonal-core-bound` as open, not proved. State exactly what A2 must prove.

5. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open.

6. Exploratory allocation: compare fourth moment, CRI, and direct signed bilinear routes in one page, with one falsification criterion for each.

Verification tasks:

- Check H4 source-card dependency before any coefficient bound such as $|\Phi(u)|\le C$ is used.
- Confirm that any paired implementation formula is labelled invalid for complex weights.

## For A2

Target obligations: `M9-near-collision-taxonomy`, `M9-M2-N0-diagonal-core-bound`, and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Use one fixed two-sided convention:
$$
   1\le |h|\le H_D.
$$

2. Use the actual $\beta_h$ coefficients and the corrected numerator
$$
   N=
   h_1d_2d_3d_4
   -
   h_2d_1d_3d_4
   +
   h_3d_1d_2d_4
   -
   h_4d_1d_2d_3.
$$

3. Prove or explicitly mark open the `M9-M2-N0-diagonal-core-bound` lemma. Do not use the incorrect $\frac{1}{16}D^2$ constant for the whole core.

4. Produce a taxonomy table with columns:
   - family name;
   - defining equations;
   - proof that $N=0$;
   - coefficient product;
   - mass bound;
   - status;
   - remaining edge cases.

5. Resolve or preserve as open the unclassified exact $N=0$ residue reported in the small enumeration.

6. Downgrade denominator-paired negligibility unless a proof is supplied.

7. Define near-collision bands using
$$
   |N|\lesssim D^4/X
$$
   and state the first exact theorem needed to bound them.

8. Repair or alternative route: formulate the direct signed bilinear route as a precise lemma with coefficient class, matrix or spacing norm, dependency on a named theorem if any, and a fast falsification test.

Verification tasks:

- Supply either proof or reproducible computation for every numerical claim.
- Label central claims only as `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

## For A3

Target obligation: `M9-regression-raw-vs-paired`.

Objectives:

1. Produce actual repository-ready artifacts, not only a protocol:
   - `computations/m9_regression/run.py`;
   - `outputs/table_small.csv`;
   - `computations/m9_regression/precision.log`;
   - `computations/m9_regression/report.md`.

2. Use the official raw two-sided M1/M2 formulas and actual Vaaler coefficients. If H4 source audit is not final, clearly mark the coefficient as provisional and separate structural tests from quantitative tests.

3. For real dyadic weights, verify raw two-sided sums equal the paired real formulas.

4. For complex weights, verify paired real formulas fail unless modified.

5. Include explicit checks:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   |C_h|^2=4\,1_{2\nmid h},
   \qquad
   \beta_{-h}=\beta_h.
$$

6. Implement small exact fourth-moment binning with the corrected $N$ and actual $\beta_h$ weights. Report exact $N=0$ bins, unclassified bins, and near-collision bands.

7. Compute CRI ratios:
$$
   R_{\rm CRI}
   =
   \frac{|\Sigma_1-\Sigma_3|^2}
   {|\Sigma_1|^2+|\Sigma_3|^2}.
$$

8. Compute one bilinear gradient-spacing diagnostic using
$$
   \nabla f(h,d)=
   \left(
   \frac{X}{4d},
   -\frac{hX}{4d^2}
   \right).
$$

Verification tasks:

- Record command line, Python version, precision settings, table schema, and pass/fail assertions.
- Label all output `diagnostic_only`.
- Do not use surrogate kernels as official evidence; put any toy kernel in a separate exploratory appendix.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.0 | 7.0 | 8.0 | Strong algebraic normalization and conservative state handling. Best basis for the judge synthesis. |
| A2 | 7.5 | 3.0 | 4.5 | Strong route ideas and useful fourth-moment focus, but overpromotes incomplete taxonomy, numerical claims, and unproved denominator-paired estimates. |
| A3 | 6.5 | 2.5 | 6.0 | Good diagnostic design, but evidence is not committed/executed and uses provisional or possibly non-official normalizations. |

Overall, Round 2 is useful but not proof-level endpoint progress. The fourth-moment route is now the primary M2 research direction. The direct signed bilinear route remains the backup. Computation remains diagnostic only until actual files and outputs exist.

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

--- ROUND-LOCAL HUMAN NOTES ---
These files are human steering notes for this round. Treat directional requests as instructions, and treat mathematical assertions as claims to audit unless proof is supplied.

--- HUMAN FILE: rounds/obligation-main/round_003/human/00-strategy-evaluations-judge-merge.md ---
# Human Steering Note: Merged Evaluations Of Strategy Revisions

The files `Evaluation1.md`, `Evaluation2.md`, `Evaluation3.md`, and `Evaluation4.md` are evaluations of the strategy revisions, not new strategy proposals. Use them as meta-review evidence when writing the Round 3 judge synthesis.

## Sources Evaluated

The four evaluation files compare:

- `strategy-revised1.md`: current analytic route, especially signed fourth moments for `M9-M2`;
- `strategy-revised2.md`: broad AI/ML or optimization pivot;
- `strategy-revised4.md`: architecture audit, R5-Full risk check, and possible incremental-exponent retargeting.

## Consensus Across The Four Evaluations

All four evaluations agree on these points:

- `strategy-revised2.md` should not steer the current proof round. It can remain an exploratory backlog, but it lacks theorem-level bridges to `M9` or the final target.
- `strategy-revised1.md` contains the most concrete analytic program: preserve the Vaaler coefficients, retain the `chi_4(h)` sign, and continue the signed fourth-moment / exact-resonance / near-collision attack on `M9-M2`.
- `strategy-revised4.md` is valuable as a proof-hygiene and risk-audit document, especially for R5-Full reconciliation and proof-draft consolidation.
- Computation should remain diagnostic unless converted into a mathematical proof obligation.

## Main Disagreement

The evaluations disagree about how strongly to prioritize `strategy-revised4.md` over `strategy-revised1.md`.

`Evaluation1.md` and `Evaluation4.md` favor `strategy-revised1.md` as the working strategy, with `strategy-revised4.md` as audit/guardrails.

`Evaluation2.md` and `Evaluation3.md` favor `strategy-revised4.md` as the primary governing directive, mainly because it forces an R5-Full audit and supports a verified incremental-exponent milestone.

The deepest technical disagreement is the interpretation of `R5-Full`:

- The skeptical view: R5-Full may hide a Fejer-residual / divisor-problem-strength trap and should be hostile-audited before relying on it.
- The corrective view: later R5-Full product-count arguments may avoid the old trap by using the positive Fejer majorant before Fourier expansion; the proof still needs to be written with edge cases, but it should not be downgraded automatically.

## Judge Instruction

Resolve the disagreement conservatively:

- Do not downgrade `R5-Full` solely because Evaluations 2 and 3 are skeptical.
- Do not treat R5-Full as fully settled solely because Evaluation 4 defends the product-count mechanism.
- Require an explicit R5-Full reconciliation task: compare the older H5r/DDP-trap analysis with the later R5-Full-R18 through R5-Full-R27 product-count entries, then write the accepted proof or downgrade proposal into the proof draft.
- Keep `obligation-main` focused on `M9-M2` unless the project owner explicitly changes the goal to an incremental-exponent track.

## Score Synthesis

The judge should interpret the scores approximately as follows:

| Strategy file | Consensus insight | Consensus feasibility | Judge use |
|---|---:|---:|---|
| `strategy-revised1.md` | High | Moderate as endpoint proof; high as next-step analytic program | Main mathematical workstream |
| `strategy-revised4.md` | High | High as audit workflow; uncertain as route pivot | Guardrails and proof hygiene |
| `strategy-revised2.md` | Mixed/high-level | Low for current proof workflow | Exploratory backlog only |

## Recommended Judge Outcome

The evaluations should push the judge toward this combined stance:

- Primary mathematical route: `strategy-revised1.md`, centered on signed fourth moments for `M9-M2`.
- Mandatory audit overlay: `strategy-revised4.md`, centered on R5-Full reconciliation, proof-draft consolidation, and no-overclaiming.
- Exploratory backlog: `strategy-revised2.md`, with no state-status changes.

## Suggested Next-Round Agent Tasks

A1:

- write the R5-Full product-count proof or reconciliation into `best_proof_draft.md`;
- keep H4, R5-Full, the conditional bridge, and M9 definitions visible;
- state the exact near-collision/additive-energy target.

A2:

- hostile-audit R5-Full against the older H5r/DDP-trap concern;
- prove or refute one narrow exact `N = 0` subfamily for the `M9-M2` fourth moment;
- avoid importing Li--Yang/Bourgain--Watt claims without source-audited hypotheses.

A3:

- run reproducible diagnostics for exact-resonance, unclassified `N = 0`, near-collision, and fixed Fejer residual bins;
- keep all computation labeled `diagnostic_only` unless converted to a proof.

## Bottom Line

The four evaluations are best read as a consensus-plus-disagreement packet: continue the `strategy-revised1.md` analytic program, enforce the `strategy-revised4.md` audit discipline, and set aside `strategy-revised2.md` for this round.

--- HUMAN FILE: rounds/obligation-main/round_003/human/Evaluation1.md ---
# Evaluation1: Strategy Revision Scores

This evaluation scores the three strategy revisions as proof strategies for the endpoint target

```text
P(X) <<_epsilon X^(1/4+epsilon),
```

not merely as brainstorming documents.

| File | Insight score | Feasibility score | Overall rank | Judgment |
|---|---:|---:|---:|---|
| `strategy-revised1.md` | 9.2 / 10 | 6.6 / 10 | 1 | Best current route: aligned with repo state, aimed at the real bottleneck, and actionable. |
| `strategy-revised4.md` | 8.4 / 10 | 5.8 / 10 | 2 | Strong risk audit and state-hygiene note; less concrete as a proof route. |
| `strategy-revised2.md` | 4.5 / 10 | 1.8 / 10 | 3 | Creative but too speculative; lacks theorem-level bridges to the current bottleneck. |

## 1. `strategy-revised1.md`: Best Chance

This is the strongest of the three. It correctly says the balanced hyperbola/Vaaler reduction is mature and that the real problem is the fixed-coefficient `M9` estimate, especially `M9-M2`. It also keeps the conditional bridge

```text
H1-H3 + H4 + R5-Full + M9
  => P(X) <<_epsilon X^(1/4+epsilon)
```

rather than claiming a proof.

Its main insight is to attack `M9-M2` by a signed fourth moment. This is the right instinct because `M9-M2` contains the frequency character

```text
C_h = e(h/4) - e(3h/4) = 2i chi_4(h)
```

on odd `h`, and standard weighted Cauchy in `h` destroys this character by replacing `C_h conjugate(C_h)` with `|C_h|^2`. The proposed fourth-moment expansion keeps the actual coefficients `beta_h = alpha_h C_h` and clears denominators to

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4
  + h3 d1 d2 d4 - h4 d1 d2 d3.
```

That is exactly the object the recent judge packets have been converging toward.

The feasibility score is limited because the hard estimate is still missing. The file is honest about this: the algebraic fourth-moment identity is not an estimate, and exact diagonals, semi-diagonals, denominator-paired cases, truncation edges, and near-collisions still need to be separated and bounded.

Verdict: use this as the primary strategy. Its next task should be narrow: prove one fourth-moment subfamily, then write the first genuine Delta-method or shifted-convolution object for the near-collision band.

## 2. `strategy-revised4.md`: Strong Audit, Weaker Proof Route

This file is a good architecture audit. It correctly reconstructs the route

```text
P(X)
  -> symmetric hyperbola
  -> floor-compatible sawtooth
  -> finite Vaaler
  -> local dyadic chi_4-twisted reciprocal sums.
```

It also correctly states that after H1-H4 the difficulty is concentrated in `M9`, at the endpoint/self-dual scale `D <= X^(1/2)`.

Its best contribution is caution. It flags `R5-Full` as something that must be reconciled with the older Fejer-residual / divisor-problem-trap diagnosis, and it correctly says that the fourth-moment attack on `M9-M2` has a no-slack wall: diagonal terms are already at the conjectural fourth-moment size, so every off-diagonal and near-collision family must be controlled sharply.

It also gives good alternative-route hygiene. Incremental Li--Yang-style reproduction, mean-square/large-values, exact Voronoi--Bessel/Hardy, additive energy of `sqrt(n)`, and omega-side guardrails are all useful to track, but none should replace the active route without a theorem-level bridge.

The reason it ranks below `strategy-revised1.md` is that it is mainly a risk audit, not a proof plan. Its strongest recommendation is to keep `obligation-main` focused on M9-M2 and near-collision estimates, which is correct, but it gives less concrete next-step analytic content than revised1.

Verdict: keep this as the audit checklist. It should govern proof hygiene, state updates, and false-proof detection, while revised1 should drive the next mathematical attack.

## 3. `strategy-revised2.md`: Creative But Least Feasible

This file recommends pivoting from symbolic exponential-sum work toward AI-driven structural exploration: reinforcement learning for discrete `l^2` decoupling partitions, neural optimization of mollifiers/test functions, and symbolic regression for L-function amplifiers.

The ideas are not worthless. Nonstandard smoothing, decoupling partitions, and coefficient search may be useful exploratory tools. But the file does not connect those ideas to the repo's conditional bridge, H4/R5, or fixed-coefficient `M9` bottleneck. The concrete current target is not "find a better generic mollifier" or "search for amplifier coefficients"; it is to prove endpoint estimates for the exact Vaaler main sums with their actual coefficients and character placement.

The main weakness is overclaiming. No theorem-level bridge is supplied from those optimization objects back to

```text
M1(D;X), M2(D;X) <<_epsilon X^(1/4+epsilon).
```

Without such a bridge, this is a research-infrastructure pitch, not a viable proof strategy.

Verdict: archive as divergent ideation. It may inspire side experiments, but it should not steer the main proof effort.

## Final Recommendation

Use:

```text
strategy-revised1.md as the main route,
strategy-revised4.md as the audit / guardrail document,
strategy-revised2.md as speculative background only.
```

For the next round, allocate roughly 70% to the signed fourth-moment / near-collision program from `strategy-revised1.md`, 25% to the R5/M9 proof-audit and state hygiene from `strategy-revised4.md`, and 5% or less to `strategy-revised2.md`-style exploratory AI optimization.

--- HUMAN FILE: rounds/obligation-main/round_003/human/Evaluation2.md ---
# Evaluation2: Referee-Style Ranking Of The Strategy Revisions

This evaluation treats the three strategy revisions as three different philosophies for attacking the Gauss Circle Problem:

1. `strategy-revised1.md`: deepen the current balanced-hyperbola/Vaaler route through signed fourth moments and a Delta-method style near-collision analysis.
2. `strategy-revised2.md`: pivot toward AI/ML structural exploration, including RL decoupling search, neural mollifier optimization, and symbolic-regression amplifiers.
3. `strategy-revised4.md`: perform a pragmatic architecture audit, challenge the R5-Full residual status, and consider a verified incremental-exponent target.

## Evaluation 1: Signed Fourth Moment / Delta-Method Strategy

Core proposal: maintain the reduction to fixed-coefficient reciprocal sums `M1` and `M2`. Attack `M2` by a signed fourth-moment expansion that preserves the `chi_4(h)` character, followed by a Delta-method or shifted-convolution treatment of the near-collision band `|N| <= D^4/X`. A coupled `M1+M2` target is a possible backup.

Insight score: 9 / 10.

This strategy understands the current algebraic state of the repository. It identifies the exact mechanism of failure for standard approaches: the `h`-Cauchy sign loss where `|C_h|^2 = 4 * 1_{2 not divide h}` destroys the character. The coupled `M1+M2` proposal is also mathematically mature, because the two legs originate from a single symmetric hyperbola identity and separate triangle-inequality bounds may discard useful interference.

Feasibility score: 5 / 10.

It is highly feasible for the agents to execute the algebraic expansion and diagnostic decomposition. It is much less clear that this can reach the endpoint. Fourth moments at `D asymp X^(1/2)` naturally produce diagonal mass of size `D^2 asymp X`. To prove the target, near-collision off-diagonal terms must be controlled essentially sharply. This route may produce a rigorous barrier map rather than a proof of the endpoint.

## Evaluation 2: AI/ML Structural Explorer Strategy

Core proposal: pivot away from symbolic algebra toward RL for decoupling partitions, neural optimization of mollifiers, and symbolic regression for L-function amplifiers.

Insight score: 8.5 / 10.

This strategy correctly senses that the current route may suffer from algebraic exhaustion and that modern record exponents use geometric and large-value structure rather than only classical exponent-pair algebra.

Feasibility score: 2 / 10.

For this repository, the proposal is currently not executable as rigorous mathematics. An RL policy or neural mollifier would still need to be converted into a universally quantified theorem with exact hypotheses, symbolic bounds, and an unsmoothing bridge. The current A1/A2/A3 workflow is not set up to turn empirical ML outputs into proof-certified inequalities.

## Evaluation 3: Architecture Audit / Incremental Strategy

Core proposal: acknowledge the ambition gap, consider retargeting to a verified incremental exponent, rigorously audit the R5-Full Fejer residual claim, and organize the near-collision problem as an additive-energy problem.

Insight score: 9.5 / 10.

This is the most mathematically sober assessment in this evaluation. It flags R5-Full as a systemic risk and warns that bounding the Fejer residual at endpoint strength can hide a divisor-problem-strength assumption if the majorant is mishandled.

Feasibility score: 9 / 10.

This path is very executable. The agents can audit R5-Full, translate Li--Yang or Bourgain--Watt style results into the repo's notation, and produce a verified incremental theorem or a rigorous obstruction map.

## Final Synthesis And Ranking

| Rank | Strategy | Insights | Feasibility | Verdict |
|---|---:|---:|---:|---|
| 1 | `strategy-revised4.md` pragmatic audit | 9.5 | 9.0 | Best way to prevent false progress and aim for a verified deliverable. |
| 2 | `strategy-revised1.md` signed fourth moment | 9.0 | 5.0 | Best analytic continuation if the project keeps chasing the endpoint. |
| 3 | `strategy-revised2.md` AI/ML explorer | 8.5 | 2.0 | Conceptually interesting, not currently proof-executable. |

## Recommended Action

Adopt the pragmatic audit as the primary governing directive in the short term. A1 should consider whether the project target should include a verified incremental exponent. A2 should perform a hostile audit of `R5-Full`. The signed fourth-moment expansion from `strategy-revised1.md` should continue as a diagnostic route for the additive energy and exact-resonance structure, not as a presumed route to the endpoint.

--- HUMAN FILE: rounds/obligation-main/round_003/human/Evaluation3.md ---
# Evaluation3: Comparative Assessment Of The Three Strategy Files

This evaluation compares three paradigms for the AI orchestrator:

- `strategy-revised1.md`: deep analytic number theory within the current route.
- `strategy-revised2.md`: machine-learning and AI optimization.
- `strategy-revised4.md`: structural project audit.

Scores are given for insight and feasibility as routes to rigorous, verified mathematical progress.

## 1. `strategy-revised1.md`: Analytic Number Theory Strategy

Summary: this document advocates staying with the repository's current balanced-hyperbola/Vaaler reduction while avoiding standard bounds that destroy the `chi_4(h)` frequency twist. It proposes a signed fourth-moment expansion for `M9-M2` and a possible coupled target for `M1+M2`.

Insight score: 9.5 / 10.

This file shows expert-level understanding of the current exponential-sum problem. It identifies where traditional bounds lose the mod-4 character, formulates the resonance polynomial `N`, and proposes a coupled-leg safety net.

Feasibility score: 7.5 / 10.

The route is actionable for the current AI workflow: expand the fourth moment, isolate `N = 0` cases, and formulate a Delta-symbol or shifted-convolution near-collision problem. The score is capped because bounding the near-collision mass strongly enough for the endpoint remains historically very difficult.

## 2. `strategy-revised2.md`: Continuous AI/ML Pivot

Summary: this document argues for using deep AI architectures: reinforcement learning for geometric `l^2` decoupling, neural networks for mollifier optimization, and symbolic regression for L-function amplifiers.

Insight score: 8.5 / 10.

The file correctly recognizes that modern progress often uses geometric decoupling and optimized analytic structures, not only classical exponent-pair manipulations. The broad generator/verifier idea is worth remembering.

Feasibility score: 3 / 10.

For the current repo, this is not ready. There is a large gap between empirical ML optimization and a rigorous proof. A neural test function or RL-discovered partition would still need exact symbolic derivative bounds, theorem-level hypotheses, and a bridge back to the unsmoothed circle problem or to M9.

## 3. `strategy-revised4.md`: Architecture And Route Audit

Summary: this document audits the project architecture, flags the possible R5-Full inconsistency, warns about the no-slack wall in the fourth-moment diagonal core, and suggests treating a verified incremental exponent as a valid success target.

Insight score: 9.5 / 10.

This file is the orchestrator's safety mechanism. The R5-Full concern is important: if the system previously identified the Fejer residual as a DDP-strength trap and later marked R5-Full as derived, that transition must be checked carefully.

Feasibility score: 9.5 / 10.

This is highly executable. Auditing a specific gap, consolidating lemmas, and accepting an incremental bound as a milestone are exactly the kinds of tasks LLM-based mathematical workflows can do well.

## Final Ranking

| Rank | Strategy | Insights | Feasibility | Overall verdict |
|---|---:|---:|---:|---|
| 1 | `strategy-revised4.md` structural audit | 9.5 | 9.5 | Safest and most necessary structural step. |
| 2 | `strategy-revised1.md` analytic blueprint | 9.5 | 7.5 | Best tactical mathematical playbook. |
| 3 | `strategy-revised2.md` AI/ML pivot | 8.5 | 3.0 | Visionary, but not structurally usable for formal verification now. |

## Recommended Action Plan

1. Halt and audit: immediately audit `R5-Full` to ensure the foundational reduction is not hallucinated or circular. Consider accepting a verified incremental exponent bound as a valid victory condition.
2. Execute the math: after the foundation is verified, point the agents at the signed fourth moment of `M9-M2`. Require them to categorize the `N = 0` resonance families and forbid Cauchy-Schwarz steps that strip the `chi_4` character.
3. Set aside `strategy-revised2.md` for now. Its RL and neural-network suggestions cannot easily be integrated into the discrete proof architecture.

--- HUMAN FILE: rounds/obligation-main/round_003/human/Evaluation4.md ---
# Evaluation4: R5-Full Correction And Final Strategy Ranking

This evaluation compares the three strategy revisions after reading the obligation graph. It also corrects an earlier interpretation of R5-Full.

| File | Insight | Feasibility / usefulness |
|---|---:|---:|
| `strategy-revised1.md` | 9 / 10 | 8 / 10 |
| `strategy-revised4.md` | 7 / 10 | 7 / 10 |
| `strategy-revised2.md` | 4 / 10 | 2.5 / 10 |

## Decisive Differentiator: R5-Full

The most consequential technical question is the status of `R5-Full`, the Fejer-residual bound. `strategy-revised1.md` and `strategy-revised4.md` disagree, and this evaluation concludes that `strategy-revised1.md` is closer to the current state.

`strategy-revised1.md` treats R5-Full as a genuine consolidation: the Vaaler residual is controlled by product counting and divisor multiplicity, with width

```text
Delta = D/H asymp X^(1/4).
```

This removes the earlier overstrong residual targets from the critical path.

`strategy-revised4.md` resurrects the older Round 5 DDP-trap worry and calls R5-Full a likely over-promotion. This evaluation now judges that flagship critique to be too strong.

The concrete reason is order of operations. The residual is bounded pointwise by a nonnegative Fejer kernel:

```text
|R_H(t)| <= K_H(t)/(2H+2).
```

One can bound the residual contribution by summing absolute values:

```text
sum_{d <= D} K_H(X/d),
```

with no cancellation required. This sum is dominated by those `d` for which `X/d` lies within `1/H` of an integer. A divisor-counting argument gives roughly

```text
sum_{|m| <= X^(1/4)} tau(X - m) <= X^(1/4+epsilon),
```

and each near-resonant contribution is at most about `H`, so

```text
sum_d K_H(X/d) <= X^(1/2+epsilon).
```

After division by `2H+2`, this gives the desired

```text
X^(1/4+epsilon)
```

scale. No character cancellation is required.

The earlier DDP-trap analysis expanded the majorant into Fourier modes first and then tried to bound each inner sum by cancellation. That order loses `chi_4` and creates divisor-strength reciprocal sums. R5-Full avoids this by using the positive majorant before expansion.

The remaining valid criticism is proof hygiene: the product-count proof still needs to be written in the proof draft with all edge cases, including exact resonances, shifted products, nearest-integer ties, short blocks, small-X separation, dyadic overlap, and logarithmic losses.

## Why `strategy-revised1.md` Scores Highest

Beyond its R5-Full interpretation, `strategy-revised1.md` is the most engaged and generative note. Its coupled-target proposal,

```text
M1 + M2 << X^(1/4+epsilon),
```

is sharp and non-obvious: the two legs come from the same exact hyperbola identity, so bounding them separately may discard cross-leg cancellation. It also supplies a practical falsification test through signed-vs-unsigned cross-correlation near `D asymp X^(1/2)`.

Its tailored Li--Yang framing is useful: the M9 sums have fixed Vaaler coefficients, so the correct task is not to import Li--Yang as a black box, but to audit the exact theorem and identify which fixed-coefficient endpoint wedge is missing.

Minor caveats: the R5-Full proof is not yet written in the proof draft, and some claimed literature barriers may need source checking.

Verdict: use `strategy-revised1.md` as the working strategy.

## Why `strategy-revised4.md` Is Second

`strategy-revised4.md` reads the architecture accurately: the route, the proved H1-H3/H7/H9 infrastructure, the no-slack wall in the fourth moment, and the empty draft/gap/lemma files. Its alternatives overlap usefully with revised1.

But it is mainly an audit rather than a new proof strategy, and its headline R5-Full concern is probably too pessimistic. The defensible core remains: write and reconcile the product-count proof explicitly. The overstatement is the suggestion that R5-Full is secretly divisor-hard in the same way as the main problem.

Verdict: keep it as the risk-and-hygiene checklist.

## Why `strategy-revised2.md` Scores Lowest

`strategy-revised2.md` does not engage the actual obligation graph closely enough. It critiques a project that is mostly about automated exponent-pair or generic decoupling search, but the current repo is instead focused on exact Vaaler coefficients, fixed reciprocal sums, and proof-obligation hygiene.

Its three proposals have serious weaknesses:

- Decoupling is not simply a partition optimized by RL search; the hard part is proving a sharp inequality.
- Mollifier optimization ignores that Beurling--Selberg/Vaaler objects already have extremal structure, and numerical smooth functions would still require a rigorous unsmoothing bridge.
- The amplifier proposal risks targeting degree-1 Dirichlet L-functions, while the circle problem is tied to degree-2 objects such as `zeta(s)L(s,chi_4)` and their moments.

The general generator/verifier framing is worthwhile, but it does not apply cleanly to the subproblems chosen here.

Verdict: set it aside for this problem.

## Bottom Line

Use `strategy-revised1.md` as the working strategy. It identifies the live M9-M2 bottleneck, gives a plausible signed fourth-moment program, and correctly treats R5-Full as residual infrastructure pending proof-draft insertion.

Keep `strategy-revised4.md` as the risk-and-hygiene checklist: consolidate the empty proof draft, write R5-Full's product-count proof explicitly, and keep false-proof detectors active.

Set `strategy-revised2.md` aside for the current round, while remembering its generator/verifier philosophy for tasks where the hard step is genuinely a search problem.

--- HUMAN FILE: rounds/obligation-main/round_003/human/stage-a-response-audit.md ---
# Human Steering Note: Round 3 Stage A Audit

Use this note for Stage B review and judge synthesis.

Round 3 Stage A responses are archived and polished. A3 API reasoning completed automatically. A3's proposed diagnostic bundle was materialized and executed locally with:

```powershell
python .\computations\m9_regression\run.py
```

Local diagnostic outputs:

- `outputs/table_small.csv`
- `computations/m9_regression/precision.log`
- `computations/m9_regression/report.md`

Round-local archive copy for Stage D auto-publish:

- `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
- `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
- `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
- `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`

Important audit conclusions:

- A1 is calibrated and should be accepted as proof infrastructure under the unresolved H4 source audit.
- A2's total exact `N=0` `O(D^2)` claim is not yet proved. The additive-energy estimate needs a theorem statement or proof.
- A2's proposed promotions for `M9-M2-N0-diagonal-core-bound` and `M9-near-collision-taxonomy` should be rejected unless a reviewer supplies the missing proof.
- A3/Codex diagnostics support raw-vs-paired formula normalization only. They are diagnostic, not theorem evidence.
- The finite diagnostic has nonzero `N0_unclass` mass (`0.0127084`), so do not declare the exact `N=0` taxonomy resolved.
- Keep `M9`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open for now.

--- HUMAN FILE: rounds/obligation-main/round_003/human/stage-b-review-audit.md ---
# Human Steering Note: Round 3 Stage B Review Audit

Use this note when writing the Round 3 judge synthesis.

## Consensus

- Accept A1's M2 algebraic normalization under H4:
  - `C_h = 2i chi_4(h) 1_{2 notmid h}`;
  - real-even `beta_h`;
  - raw two-sided M2 formula;
  - paired formula only under its stated weight hypotheses;
  - corrected fourth-moment numerator `N`.
- Accept A3/Codex artifacts only as `diagnostic_only` evidence:
  - `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`
- Reject A2's Stage A promotions:
  - no `proved_internal` status for `M9-M2-N0-diagonal-core-bound`;
  - no resolved status for `M9-near-collision-taxonomy`;
  - no proved or derived status for the direct exponent-pair/Poisson route.

## Important Caution

A2's Stage B review gives a useful denominator-paired unweighted count stress test:

```text
unweighted denominator-paired count ~ D^4 X^(-3/4) log D,
at D = X^(1/2): ~ X^(5/4) log X.
```

Treat this as a promising stress-test claim, not as final graph evidence unless the judge verifies the counting argument. Its safe conclusion is that trivial unweighted counting is insufficient and the next proof must use actual reciprocal `beta_h` weights, signs, or a weighted energy theorem.

## Recommended State Treatment

- Keep open: `M9`, `M9-M1`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, and `GC-target`.
- Keep source-audit-required: `H4-source-audit`, `Li-Yang-source-audit`.
- `M9-regression-raw-vs-paired`: may become `diagnostic_only`, or remain `proposed` with the Round 3 artifact files attached as positive diagnostic evidence. Do not promote it to theorem evidence.

## Next Round

- A1: H4 source audit and precise near-collision lemma statement.
- A2: one narrow weighted denominator-paired proof, with all gcd cases and reciprocal beta weights.
- A3: post-H4 diagnostic rerun, larger exact `N=0` and near-collision tables, and optional complex-weight generalized cosine regression.

--- HUMAN FILE: rounds/obligation-main/round_003/human/strategy-revised-audit.md ---
# Human Steering Note: Strategy-Revised Audit

Use this note when writing the Round 3 judge synthesis.

## Main Strategy

Use `strategy-revised1.md` as the serious steering note:

- keep the balanced hyperbola/Vaaler/Fejer residual framework;
- treat `M9`, especially `M9-M2`, as the bottleneck;
- preserve the actual Vaaler coefficients and `chi_4(h)` sign;
- continue the signed fourth-moment route for `M2`;
- focus first on exact `N=0` subfamilies, especially denominator-paired and semi-diagonal families;
- keep computation diagnostic only.

## Backup Ideas

Accept only as `proposed` or `open` if the judge wants to track them:

- `M9-coupled`: a backup target for `M1+M2`, not a replacement for separate `M9`.
- Tailored Li--Yang/Bombieri--Iwaniec fixed-coefficient extension after source audit.
- B-process/Hardy-window route with exact dual length and boundary terms.
- Mellin--Perron/L-function route as conditional comparison.

## Exploratory Only

Treat `strategy-revised2.md` as broad exploration, not current proof direction:

- RL/decoupling partition search;
- functional optimization of smoothing weights;
- L-function amplifier coefficient search;
- formal proof tooling ideas.

These need precise theorem statements, ranges, dependencies, executable diagnostics, and an unsmoothing bridge before they can affect the proof graph.

## Do Not Promote

Do not change the status of `M9`, `M9-M1`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `GC-target`, `H4-source-audit`, or `Li-Yang-source-audit` based on these strategy files alone.

## Immediate Next Round Shape

- A1: H4 source audit and exact near-collision lemma statement.
- A2: one narrow weighted denominator-paired or semi-diagonal proof.
- A3: scale diagnostic tables and rerun after H4 replaces the provisional kernel.

--- HUMAN FILE: rounds/obligation-main/round_003/human/strategy-revised-judge-merge.md ---
# Human Steering Note: Merged Strategy-Revised Inputs For Judge

Use this note as the judge-facing merge of:

- `strategy-revised1.md`
- `strategy-revised2.md`
- `strategy-revised4.md`

The raw source files remain included for auditability, but this merge is the priority order for the Round 3 judge synthesis.

## Priority Order

1. `strategy-revised1.md` is the primary mathematical steering note.
2. `strategy-revised4.md` is a risk-audit and route-calibration note.
3. `strategy-revised2.md` is an exploratory architecture backlog, not current proof direction.

## Unified Judge Instruction

Keep `obligation-main` on the current balanced hyperbola / Vaaler / fixed-coefficient reciprocal-sum route. The active mathematical bottleneck remains `M9`, especially `M9-M2`.

The judge should explicitly synthesize the three strategy revisions as follows:

- Adopt the `strategy-revised1.md` near-term plan: preserve the actual Vaaler coefficients, retain the `chi_4(h)` sign, continue the signed fourth-moment route for `M9-M2`, and focus first on exact `N = 0` subfamilies and near-collision estimates.
- Adopt the `strategy-revised4.md` caution: require a reconciliation of old H5r / Fejer-majorant DDP-trap warnings with the later R5-Full product-count proof before changing R5-Full status.
- Downgrade `strategy-revised2.md` to an exploratory backlog: RL/decoupling search, smoothing-weight optimization, formal proof tooling, and amplifier/L-function experiments require exact theorem statements, parameter ranges, executable diagnostics, and an unsmoothing bridge before they can affect the proof graph.

## State-Change Rules

Do not change the status of `GC-target`, `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-estimate`, `M9-near-collision-taxonomy`, `H4`, `H4-source-audit`, `Li-Yang-source-audit`, or `R5-Full` merely because of these strategy notes.

Permissible judge actions:

- Create or emphasize `R5-Full-reconciliation` as `open` or `proposed`.
- Create or emphasize proof-draft consolidation as an infrastructure task.
- Create or emphasize an additive-energy / sqrt-spacing formulation for `M9-M2` near-collisions as `proposed`.
- Keep `M9-coupled` as a backup target only, not a replacement for separate `M9-M1` and `M9-M2`.

Impermissible judge actions:

- Do not downgrade `R5-Full` without checking the later R5-Full-R18 through R5-Full-R27 product-count entries.
- Do not pivot the active `obligation-main` run to an incremental-exponent goal unless the project owner explicitly changes the objective.
- Do not promote Li--Yang, Bourgain--Watt, Voronoi--Bessel, spectral, RL, or formal-methods ideas without a theorem-level bridge to M9 or to the final target.
- Do not treat computation as proof; keep A3 artifacts diagnostic unless a proof obligation is mathematically certified.

## Merged Next-Round Assignments

A1 should consolidate the proof infrastructure:

- write H1-H4, R5-Full, the conditional bridge, M9 definitions, and active blockers into `best_proof_draft.md`;
- finish the H4 source audit and exact residual conventions;
- state the near-collision/additive-energy target precisely enough for A2 and A3 to attack.

A2 should attack the analytic bottleneck:

- give one narrow proof attempt for a weighted exact `N = 0` subfamily, preferably denominator-paired or semi-diagonal;
- independently referee R5-Full against the older H5r/DDP-trap objection;
- state any Li--Yang/Bombieri--Iwaniec dependency with exact hypotheses before using it.

A3 should keep the diagnostics proof-aware:

- run or extend fixed Fejer residual and `M9-M2` fourth-moment diagnostics;
- track exact-resonance, unclassified `N = 0`, and near-collision bins separately;
- report scaling evidence as diagnostic only, with reproducible scripts and tables.

## Bottom Line For Judge

The merged strategy says: stay on the M9-M2 fourth-moment route, add a formal R5-Full reconciliation audit, consolidate the proof draft, and keep broader AI/optimization/spectral ideas as a precise but low-priority backlog.

--- HUMAN FILE: rounds/obligation-main/round_003/human/strategy-revised1.md ---
## Verdict

The **most plausible proof strategy is to keep the repo's balanced hyperbola/Vaaler reduction, but stop treating the reduction itself as the main research problem.** The reduction is now mature. The real proof problem is the fixed-coefficient reciprocal-sum estimate `M9`, especially the second leg (\mathcal M_2).

My recommendation is:

$$
\boxed{
\text{Balanced hyperbola}+\text{Vaaler}+\text{Fejer residual product count}
\quad\Longrightarrow\quad
\text{attack } \mathcal M_2 \text{ by a signed fourth-moment / }\Delta\text{-method route.}
}
$$

More concretely: prove the current bridge

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

then focus nearly all serious analytic work on proving `M9` with the **actual Vaaler coefficients**, not arbitrary bounded coefficients. The repo already states this as the conditional bridge, with `M9` explicitly open.

---

## 1. Evaluation of the current strategy

### What is strong

The current reduction is the right place to stand. It converts

$$
P(X)=N(\sqrt X)-\pi X
$$

into balanced reciprocal sums with denominator length only (D\le X^{1/2}), instead of applying Fourier truncation to the unbalanced (d\le X) identity. The repo's selected route is:

$$
P(X)
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal main sums}.
$$

Round 27 records exactly this as the selected route.

The accepted balanced formula is also the correct arithmetic object:

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

with

$$
y=\lfloor X^{1/2}\rfloor,\qquad
\psi_F(t)=t-\lfloor t\rfloor-\frac12.
$$

This is much better than the raw length-(X) sawtooth formula.

The most important improvement in the repo is that the Vaaler residual is no longer treated as an arbitrary hard exponential-sum family. The Fejer residual is controlled by product counting, divisor multiplicity, and a width

$$
\Delta = D/H \asymp X^{1/4}.
$$

Round 27 gives the argument that

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and similarly for the shifted second-leg residuals.

This is a real consolidation: it removes the earlier overstrong `H5r-B` / arbitrary-coefficient residual targets from the critical path.

### What remains weak

The current strategy is still conditional on `M9`. The official open analytic target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2},\qquad
H_D\asymp D X^{-1/4}.
$$

Round 27 states that this is the active bottleneck and that no new Gauss-circle exponent has been proved.

The two fixed-coefficient sums are:

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
C_h
\sum_{d\asymp D}
w_D(d)e(hX/(4d)),
$$

where

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

The second sum is therefore frequency-character twisted. That is the crucial feature to preserve.

The problem is that the obvious analytic tools tend to destroy exactly this character. The repo correctly records that weighted (h)-Cauchy for (\mathcal M_2) replaces (C_h\overline{C_h}) by (|C_h|^2), losing the (\chi_4(h)) sign.

So the current strategy is sound as a **reduction framework**, but not yet a proof strategy unless the next stage is a serious signed estimate for `M9`.

---

## 2. The most plausible proof strategy

### Main proposal: signed fourth moment for (\mathcal M_2), followed by a (\Delta)-method or exact near-collision analysis

Freeze the two-sided convention

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
\beta_h=\alpha_{h,H_D}C_h,
$$

so that

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

Then prove

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}.
$$

This implies

$$
S_2(D;X)\ll_\epsilon X^{1/4+\epsilon},
$$

which is exactly the (\mathcal M_2) part of `M9`.

Round 27 already gives the fourth-moment expansion:

$$
|S_2(D;X)|^4
=
\sum_{\mathbf h,\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
\prod_{j=1}^4w_D(d_j)
e\left(
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
\right).
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

The repo correctly marks this as a proved algebraic identity but not an estimate.

The next proof target should be a theorem of this form:

$$
\sum_{\substack{
h_i\asymp H,\ d_i\asymp D\\
|N|\lesssim D^4/X
}}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
W(\mathbf h,\mathbf d)
\ll_\epsilon X^{1+\epsilon},
$$

with the exact diagonal, pair-swapped, semi-diagonal, denominator-paired, sign-symmetric, truncation-edge, and unclassified (N=0) families separated.

Why this is the best next route:

1. It preserves the (\chi_4(h)) factor rather than killing it by Cauchy.
2. It targets the actual fixed coefficients (\beta_h), not arbitrary bounded coefficients.
3. It works at the exact endpoint (D\asymp X^{1/2}), (H_D\asymp X^{1/4}), where black-box Li--Yang does not apply.
4. It produces a clear falsification mechanism: if the signed near-collision mass behaves like the absolute mass, the route is probably not strong enough.
5. It connects naturally to a (\Delta)-method formulation: detect (N=0) or (|N|\lesssim D^4/X), then test whether the resulting complete sums retain the mod-(4) character from (\beta_h).

The current repo is already pointing in this direction: the reading packet identifies the fourth-moment route as primary for (\mathcal M_2), and keeps direct signed bilinear estimates as backup.

### Immediate proof plan

I would organize the next proof attempt as follows.

First, finish the harmless infrastructure: source-audit Vaaler, insert H4 and R5-Full into the proof draft, and freeze the raw two-sided formula. Vaaler is only an external theorem dependency for the finite approximation and does not prove `M9`; the repo's Vaaler source card correctly says this.

Second, prove the diagonal-core estimate for the fourth moment. The current next-round prompt already asks for this with the actual (\beta_h) coefficients and the corrected numerator (N).

Third, isolate the denominator-paired and semi-diagonal exact (N=0) families. These are the likely danger terms. They should be treated before broad near-collision bands.

Fourth, write a (\Delta)-symbol version of the near-collision problem:

$$
1_{|N|\lesssim D^4/X}
$$

or a smooth substitute, with a modulus range chosen so that the transformed complete sums expose

$$
\chi_4(h_1h_2h_3h_4).
$$

The proof should be rejected if the first transformation turns this into (|C_h|^2) or an unsigned odd-frequency condition.

Fifth, after (\mathcal M_2), return to (\mathcal M_1). The (\mathcal M_1) spatial character (\chi_4(d)) is more fragile under A-process differencing, so I would not spend the next round primarily on it unless the (\mathcal M_2) route collapses.

---

## 3. Main criticism of the current strategy

The current `M9` formulation asks for

$$
\mathcal M_1(D;X)\ll X^{1/4+\epsilon}
\quad\text{and}\quad
\mathcal M_2(D;X)\ll X^{1/4+\epsilon}
$$

separately. This is clean, but it may be stronger than necessary.

The exact formula only requires the combined main term to be small. Therefore, a serious backup route is to replace separate `M9` by a coupled target

$$
\mathcal M_{\mathrm{tot}}(D;X)
=
\mathcal M_1(D;X)+\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

This is weaker than the current target and may preserve cancellation between the two hyperbola legs. The repo should keep separate `M9` as the official clean target for now, but add a backup obligation:

$$
\text{M9-coupled: }
\mathcal M_1(D;X)+\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Why this may work: the two legs are not arbitrary sums. They arise from the same exact hyperbola decomposition. Bounding them separately may discard a structural cancellation that exists only after recombination.

---

## 4. Top alternative strategies

### Alternative 1: coupled two-leg fixed-coefficient estimate

This is my top backup.

Instead of proving

$$
\mathcal M_1,\mathcal M_2\ll X^{1/4+\epsilon}
$$

separately, prove

$$
\mathcal M_1+\mathcal M_2\ll X^{1/4+\epsilon}.
$$

Why it could work: the exact balanced formula is a two-leg identity. The first leg has (\chi_4(d)); the second leg has (\chi_4(h)). A combined quadratic or fourth-moment analysis may retain products such as (\chi_4(d_i)\chi_4(h_j)), while separate Cauchy steps tend to destroy one of the characters.

Main risk: if the two legs are genuinely independent at the endpoint, this only complicates the problem. A quick test is to compute signed and unsigned cross-correlations between the two raw main terms at (D\asymp X^{1/2}).

### Alternative 2: Li--Yang / Bombieri--Iwaniec endpoint extension for fixed coefficients

Li--Yang's work is structurally relevant because it treats reciprocal sums of the type

$$
\sum_{h\sim H}\sum_{m\sim M}e(Th/m),
$$

which is exactly the ambient phase family. Their paper states that they improve the Gauss circle and divisor exponents using the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results. ([arXiv][1])

But the repo is correct not to import Li--Yang as a black box. The source card explicitly says no Li--Yang theorem is currently imported as a dependency and that exact hypotheses, ranges, weights, and absolute-value placement remain unaudited.

Why a tailored extension could work: the current `M9` sums have **fixed Vaaler coefficients**, not arbitrary coefficients. A theorem for these fixed coefficients might be easier than the full Li--Yang framework. The task is not "apply Li--Yang"; it is "audit Li--Yang, identify the endpoint wedge it misses, and prove a fixed-coefficient replacement only for that wedge."

Main risk: Li--Yang themselves note that existing methods appear to face a (5/16) barrier and that new ideas are needed for the conjectural (1/4) exponent. ([arXiv][1])

### Alternative 3: B-process-first / Hardy-window route

Apply Poisson or B-process before differencing. For a reciprocal sum

$$
\sum_{d\asymp D}\chi_4(d)w(d/D)e(hX/d),
$$

stationary phase produces a dual variable roughly

$$
m\asymp \frac{hX}{D^2},
$$

and a square-root phase of the form

$$
e(c\sqrt{Xhm}).
$$

The repo already records that this preserves the character formally, but that the resulting phase has degenerate Hessian.

Why it could work: at the endpoint (D\asymp X^{1/2}), the dual length is (m\asymp h), so the transformed object is short and highly structured. If the local divisor-window coefficients after setting (q=hm) have cancellation, the route may close.

Main risk: the square-root phase is essentially Hardy/Voronoi-like but with nonstandard local divisor-window coefficients. Round 27 correctly says no endpoint estimate follows from this transform alone.

### Alternative 4: Mellin--Perron / (L)-function route

The Dirichlet series for (r_2(n)) is

$$
\sum_{n\ge1}\frac{r_2(n)}{n^s}
=
4\zeta(s)L(s,\chi_4).
$$

A sharp Perron formula plus the functional equation gives a Voronoi/Bessel-type dual expression. Under Lindelof-strength input for (\zeta(s)L(s,\chi_4)), one expects the conjectural exponent.

Why it could work: it is conceptually clean and would identify exactly which moment or subconvexity estimate is needed.

Main risk: unconditionally, this is probably as hard as Lindelof-level control for the divisor problem. The repo should keep this as a conditional comparison route, not a primary proof route.

### Alternative 5: smoothed Poisson--Bessel / radial decoupling

This is useful as calibration but weak as the main route. The repo already says the Poisson--Bessel route should remain for smoothing, unsmoothing, and recovering the classical (R^{2/3}) sanity bound.

Why it could work in a limited sense: it gives the geometric Fourier side and may reveal average cancellation or good smoothed estimates.

Main risk: the radial phase has rank degeneracy, and generic full-rank stationary phase or decoupling does not apply directly. The repo repeatedly flags this correctly.

---

## 5. What I would change in the repo's next research round

I would make the next round narrower and more proof-oriented:

1. **Promote proof infrastructure only after H4 audit.** Vaaler's theorem should be cited exactly, but this is not the mathematical bottleneck.

2. **Add `M9-coupled` as a backup obligation.** Do not abandon separate `M9`, but recognize it may be overstrong.

3. **For (\mathcal M_2), prove one exact fourth-moment sublemma.** Do not write another broad taxonomy. Pick one family: diagonal core, denominator-paired, or semi-diagonal. Prove it or leave it open.

4. **Write the first real (\Delta)-method object.** Specify the modulus range, smooth detector for (N), transformed sums, and where (\chi_4(h)) survives.

5. **Use computation only to falsify.** The repo's reading packet correctly says computation is diagnostic only.  The most useful computations are signed-vs-absolute fourth-moment bins and CRI ratios at endpoint (D\asymp X^{1/2}).

---

## Final ranking

| Rank | Strategy                                                                          | My assessment                                                                                              |
| ---: | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
|    1 | Current balanced hyperbola/Vaaler route + signed fourth moment for (\mathcal M_2) | Best chance. Keeps the successful reduction and attacks the real bottleneck without killing the character. |
|    2 | Coupled (\mathcal M_1+\mathcal M_2) estimate                                      | Very plausible backup; weaker than current separate `M9`.                                                  |
|    3 | Tailored Li--Yang/Bombieri--Iwaniec endpoint extension for fixed coefficients       | Serious but requires theorem-level work beyond black-box Li--Yang.                                          |
|    4 | B-process-first / Hardy-window transform                                          | Useful exploratory route; may expose hidden arithmetic, but degeneracy is severe.                          |
|    5 | Mellin--Perron / (L)-function route                                                | Clean conditional framework, unlikely to be easiest unconditionally.                                       |
|    6 | Poisson--Bessel / radial decoupling                                                | Keep as calibration, not primary.                                                                          |

The repo's current strategy is therefore **correctly chosen but incomplete**. The next likely productive move is not another reduction; it is a hard signed estimate for the fixed-coefficient endpoint sums, with (\mathcal M_2)'s fourth moment as the primary object.

[1]: https://arxiv.org/abs/2308.14859 "An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem"

--- HUMAN FILE: rounds/obligation-main/round_003/human/strategy-revised2.md ---
As a mathematician working at the intersection of analytic number theory and computational mathematics, I have been closely following the integration of multi-agent AI systems into deep mathematical research. The architecture of the **`yutianlee/gauss-circle-ai-collab`** repository is a highly promising structural initiative. Utilizing a multi-agent orchestrator (often combining LLM generators, Python/SageMath computational agents, and Lean 4/Isabelle formal verifiers) to tackle the Gauss Circle Problem represents a necessary shift from human-only intuition to distributed, agent-based mathematical discovery.

Let us define the mathematical stakes: For a circle of radius $\sqrt{x}$, the number of integer lattice points is $N(x) = \pi x + E(x)$. The Hardy-Landau conjecture posits that the error term is bounded by $E(x) = O(x^{1/4+\epsilon})$. For over a century, progress has been agonizingly slow, with the current world record sitting at $E(x) = O(x^{517/1648+\epsilon}) \approx O(x^{0.3137})$ by Bourgain and Watt (2017).

Based on my review of such multi-AI orchestrator setups and the mathematical bottlenecks of this specific problem, here is my professional evaluation of the baseline AI strategy, followed by the top alternative strategies the orchestrator should pivot to in order to achieve a historic breakthrough.

---

### 1. Evaluation of the Current Multi-AI Strategy

A multi-agent AI framework tackling the Gauss Circle Problem naturally defaults to automating the **Method of Exponential Sums**, specifically searching through **Van der Corput Exponent Pairs** or optimizing the discrete Hardy-Littlewood method via the **Bombieri-Iwaniec / Huxley framework**.

* **How the AI executes this:** The orchestrator divides the labor. Generator agents propose new parameter choices, sequence weights, or multi-dimensional Taylor series approximations for the phase function $f(n) = \sqrt{x - n^2}$. Verifier agents rigidly track the massive algebraic expansions to ensure no constants or $\epsilon$-losses are dropped.
* **The AI Advantage:** This strategy is mathematically sound and plays perfectly to AI's strengths. An AI is vastly superior to a human mathematician at navigating the massive combinatorial search trees required to find optimal rational approximations (via Dirichlet's theorem) and managing the algebraic bookkeeping of Weyl differencing.
* **The Critical Flaw (Why it will hit a wall):** While the AI will likely find a highly complex sequence of A and B processes that shaves a microscopic fraction (e.g., $10^{-4}$) off Bourgain's bound, **this strategy will suffer from strictly diminishing returns**. The classical exponential sum frameworks have a mathematically proven "square-root cancellation barrier" introduced by the Cauchy-Schwarz inequality. Expecting an AI orchestrator to break the $1/4$ barrier by merely finding a "better algebraic trick" within the Bombieri-Iwaniec framework is a theoretical dead end.

To genuinely push toward the $1/4$ conjecture, the AI orchestrator must pivot from being a *symbolic algebraic assistant* to a *structural explorer*.

---

### 2. Top Alternative Proof Strategies (And Why They Will Work)

To make mathematical history, the orchestrator's prompts and objective functions should be redirected toward the following three alternative strategies, which leverage areas where AI possesses a native computational advantage over humans: high-dimensional spatial geometry, functional optimization, and spectral pattern recognition.

#### Alternative Strategy A: Reinforcement Learning for Discrete $\ell^2$-Decoupling

* **The Concept:** Bourgain and Watt broke the decades-old $131/416$ barrier by stepping outside classical exponent pairs and applying **continuous $\ell^2$-decoupling** and incidence geometry. The efficiency of their bound depends entirely on how cleverly one partitions the frequency space (short arcs of the circle) into overlapping rectangular regions.
* **Why this works for AI:** Finding the optimal multilinear partition of geometric arcs is fundamentally a combinatorial geometry game. DeepMind's *AlphaTensor* and *AlphaGeometry* proved that Reinforcement Learning (RL) agents are superhuman at discovering non-intuitive, highly efficient structural decompositions that humans miss. By framing the "decoupling polynomial partition" as a discrete game within your orchestrator, an RL agent can search millions of irregular spatial partition schemes. If it discovers a multi-scale induction path that bounds the overlaps more efficiently than Bourgain's uniform caps, the exponent will immediately drop.

#### Alternative Strategy B: AI-Driven Functional Optimization of Mollifiers (Test Functions)

* **The Concept:** To analyze the Gauss Circle Problem, we use the Poisson/Voronoi Summation Formula, which converts the problem into an infinite sum of highly oscillatory Bessel functions. Because the circle has a "hard" geometric boundary, this sum decays poorly. The standard analytic trick is to multiply the indicator function by a smoothed "test function" (a mollifier) to control the Fourier transform.
* **Why this works for AI:** Human mathematicians almost always choose standard, symmetric test functions (like Gaussian bumps or Beurling-Selberg polynomials) simply because we must compute their Fourier transforms manually. For an AI, finding the absolute best smoothing function $\psi(x)$ that minimizes the Bessel tail in the dual space is an infinite-dimensional variational calculus problem.
* **Execution:** The orchestrator can assign a Neural Network to parameterize highly non-standard, asymmetric, or irregular test functions (akin to Maryna Viazovska's "magic functions" for sphere packing). Gradient descent can optimize the shape of the mollifier to strictly minimize the residual error bounds, shifting the burden from discrete sum bounding to continuous functional optimization.

#### Alternative Strategy C: Automated Proof Synthesis for L-Function Amplifiers

* **The Concept:** The Gauss circle problem is deeply tied to the subconvexity of the Dedekind zeta function of the Gaussian integers, specifically the Dirichlet $L$-function $L(s, \chi_4)$ on the critical line. Bounds here are traditionally achieved using the "Amplification Method" (Iwaniec and Friedlander).
* **Why this works for AI:** To use the amplification method, one must design an "amplifier"--a Dirichlet polynomial $A(s) = \sum a_l l^{-s}$ that artificially boosts the signal at a specific point on the critical line. Humans usually guess the coefficients $a_l$ using heuristic arithmetic functions. AI excels at high-dimensional coefficient tuning.
* **Execution:** You can deploy a Symbolic Regression Agent to dynamically search for non-intuitive coefficients that yield tighter subconvexity bounds. The AI might discover a highly irregular amplifier sequence that paves a direct analytic path to lower the exponent of $E(x)$, completely side-stepping the messy geometric bounds of traditional methods.

### Summary Recommendation for the Orchestrator

The `yutianlee/gauss-circle-ai-collab` repository represents a brilliant architectural choice because human mathematicians currently suffer from "algebraic exhaustion" on this problem.

To maximize the project's impact, update the system prompts to **stop treating the problem as a discrete exponential sum puzzle**. Reconfigure the orchestrator into a Hybrid Neural-Symbolic loop: use Neural Networks to propose continuous smoothing weights (Strategy B) or RL agents to propose novel decoupling partitions (Strategy A), and only then use the symbolic agents (Python/Lean 4) to verify the bounds. Allowing the AI to optimize the underlying mathematical *structures* rather than just the equations is the most mathematically viable path to cracking the $1/4$ barrier.

--- HUMAN FILE: rounds/obligation-main/round_003/human/strategy-revised4-audit.md ---
# Human Steering Note: Strategy-Revised4 Audit

Use `strategy-revised4.md` as a risk audit, not as a direct state patch.

## Main Use

- Keep the active route focused on `M9`, especially `M9-M2`.
- Continue the signed fourth-moment / exact-resonance / near-collision program.
- Require a reconciliation of older H5r/DDP-trap warnings with the later R5-Full product-count proof.
- Move accepted proof infrastructure out of transcripts and into `best_proof_draft.md`, `gap_register.md`, and `lemma_bank.md`.

## Do Not Promote

- Do not downgrade `R5-Full` without checking later Round 18-27 R5-Full entries.
- Do not pivot `obligation-main` to an incremental-exponent target unless explicitly requested.
- Do not promote Li--Yang, Bourgain--Watt, Voronoi--Bessel, spectral, or additive-energy routes without precise theorem statements and a bridge to M9 or the final target.

## Next Round Shape

- A1: proof-draft consolidation for H1-H4, R5-Full, the conditional bridge, M9 definitions, and blockers.
- A2: R5-Full referee report against H5r/DDP-trap objections.
- A3: diagnostics for Fejer residuals and M9-M2 fourth-moment near-collision scaling.

## Verdict

The note is useful because it identifies a load-bearing consistency check: whether R5-Full is truly residual infrastructure or still hides a DDP-strength endpoint. Treat that as an audit obligation while preserving the current M9-M2 workstream.

--- HUMAN FILE: rounds/obligation-main/round_003/human/strategy-revised4.md ---
# Strategy-Revised4: Architecture And Route Audit

This note reassesses the current proof architecture after reading the obligation graph, proof draft, gap register, lemma bank, current state, and the active round materials. The reconstruction in the earlier answer was directionally right about the framework, but wrong about the ambition: this project is not merely chasing an incremental exponent. It is attempting the full conjectural target, namely theta = 1/4 in the X = R^2 variable, equivalently E(R) = O(R^(1/2+epsilon)), through a specific arithmetic route.

## 1. What The Strategy Is, And Where It Stands

The route is internally visible across the state:

```text
P(X) = N(sqrt(X)) - pi X
  -> symmetric Dirichlet hyperbola identity
  -> floor-compatible sawtooth formula
  -> finite Vaaler approximation of psi
  -> local dyadic chi_4-twisted reciprocal exponential sums.
```

The genuinely proved infrastructure deserves credit. H1 gives the symmetric hyperbola identity, H2 gives the exact partial-sum formula for chi_4, and H3 gives the balanced sawtooth formula with an exact O(1) residual. The structural obstructions H7 and H9 are also valuable: direct Weyl differencing destroys the chi_4 character, and the B-process dual phase has a Hessian degeneracy that blocks off-the-shelf two-dimensional stationary phase or decoupling.

The reduction itself is classical and moves the problem rather than solving it. After H1-H4, the difficulty is concentrated in M9: the fixed-coefficient reciprocal main sums M1 and M2 must be O_epsilon(X^(1/4+epsilon)) uniformly up to D = X^(1/2). That is the endpoint/self-dual scale. The current known-technology gap remains the right warning: the sums sit in the Li--Yang / Bombieri--Iwaniec reciprocal-sum world, but known record-scale technology does not reach theta = 1/4.

The strongest criticism in this note is about R5-Full. The conditional bridge uses H1-H3 + H4 + R5-Full + M9 => target, and `proof_obligations.yml` currently marks R5-Full as `derived_under_assumptions`. Earlier state text, however, identified the Fejer residual as a character-blind or parity-supported DDP-strength obstruction. If that older diagnosis is still correct, R5-Full is over-promoted. If the later product-count proof really resolves the fixed Fejer residual conditional on H4, then the state needs a clearer reconciliation explaining why this does not secretly solve a divisor-problem-strength endpoint. This is the highest-priority audit point.

The newer fourth-moment attack on M9-M2 is directionally right. Opening |S2|^4, clearing denominators to the resonance integer

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4 + h3 d1 d2 d4 - h4 d1 d2 d3
```

and separating exact N = 0 structure from near-collisions is the correct Bombieri--Iwaniec/Bourgain--Watt style instinct. It also reveals the no-slack wall: the diagonal core is already at the conjectural fourth-moment size, so every off-diagonal or near-collision family must be controlled essentially sharply. That is why `M9-near-collision-estimate` remains the active bottleneck.

The process hygiene gap is real. `best_proof_draft.md`, `gap_register.md`, and `lemma_bank.md` are still sparse compared with the state and transcript history. The durable artifact should not be only the judge transcript. The proof draft needs the bridge, H4, R5-Full, M9 definitions, and the current gap list in one place.

## 2. Alternative Strategies Worth Tracking

**A. Retarget to a verified incremental exponent.** Keep the H1-H4 scaffold, reproduce the Li--Yang-style exponent within the repo's notation, and then test whether the second-spacing/additive-energy side can be sharpened. This is the highest-confidence way to produce a checkable mathematical deliverable, but it changes the project goal from the conjectural endpoint to an incremental record-style target.

**B. Mean-square and large-value leverage.** The fourth-moment work is already a small version of the mean-square/large-values philosophy behind modern record exponents. This route should be made theorem-level before it affects state: exact hypotheses, variable conventions, weights, loss factors, and the bridge to M9 are required.

**C. Exact Voronoi--Bessel / Hardy route.** The Vaaler residual difficulty suggests keeping an exact signed transform route alive. A Hardy--Voronoi/Bessel formulation avoids the positive Fejer majorant, but it must include amplitudes, boundary terms, dyadic truncation, character survival, and unsmoothing before it can replace the current route.

**D. Additive energy of sqrt(n).** The near-collision problem should be named directly as an additive-energy or spacing problem for square roots. This is a clean way to organize the M9-M2 fourth-moment taxonomy, even if known bounds are likely still too weak for theta = 1/4.

**E. Omega-side refutation rails.** Hardy--Landau, Heath-Brown distribution results, and Cramer mean-square information should be encoded as guardrails against any spurious sub-1/4 or endpoint-breaking claim. They do not prove the upper bound, but they are useful false-proof detectors.

## Recommendation

Use this note as a risk audit, not as an automatic route pivot.

Immediate state hygiene:

- A1 should consolidate H1-H4, R5-Full, the conditional bridge, M9 definitions, and current blockers into `best_proof_draft.md`.
- A2 should independently referee R5-Full against the older H5r/DDP-trap diagnosis and either confirm the later product-count proof or propose a validator-ready downgrade.
- A3 should keep diagnostics focused on fixed Fejer residuals, M9-M2 fourth moments, exact N = 0 families, and near-collision scaling.

Strategic posture:

- Keep the current `obligation-main` track focused on M9-M2 and exact-resonance/near-collision estimates.
- Do not replace the active route with Li--Yang, Voronoi--Bessel, or spectral machinery until a precise theorem-level bridge is written.
- Consider opening a separate incremental-exponent track only if the project owner explicitly wants a more attainable milestone than the conjectural theta = 1/4 endpoint.

## Judge-Assigned Reasoning Prompt For This Agent

Target obligations: `M9-M2-beta-algebra`, `M9-M2-fourth-moment-expansion`, `M9-M2-N0-diagonal-core-bound`, and state maintenance.

Objectives:

1. Insert the proof-draft-ready $\mathcal M_2$ coefficient normalization into the proof draft, preserving H4 dependency:
$$
   C_h=2i\chi_4(h)1_{2\nmid h},
   \qquad
   \beta_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h}.
$$

2. State the raw two-sided formula and the paired real formula, with the real-weight hypothesis explicit.

3. Write the fourth-moment expansion using the exact coefficient product and corrected numerator $N$.

4. Add a small lemma-bank entry for `M9-M2-N0-diagonal-core-bound` as open, not proved. State exactly what A2 must prove.

5. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open.

6. Exploratory allocation: compare fourth moment, CRI, and direct signed bilinear routes in one page, with one falsification criterion for each.

Verification tasks:

- Check H4 source-card dependency before any coefficient bound such as $|\Phi(u)|\le C$ is used.
- Confirm that any paired implementation formula is labelled invalid for complex weights.

## Your Task For Round 3

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
