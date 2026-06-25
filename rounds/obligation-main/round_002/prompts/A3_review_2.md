You are A3 Deepseek V4 Pro, acting as API-based proof auditor, algebra checker, and stress-test planner.

Review the other agents' Round 2 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Check algebraic reductions, Poisson/Bessel normalizations, hyperbola decompositions, endpoint conventions, Vaaler/Fejer residuals, Li-Yang/Bombieri-Iwaniec compatibility claims, Mellin-Perron alternatives, and claimed obstructions. Prefer precise parameter ranges and falsifiable lemmas over broad summaries. In reasoning, reserve about 20% of the answer for divergent alternatives or obstruction searches. In review, recommend research-strategy adjustments based on which claims survive verification. For computation-track obligations, do not substitute surrogate phases or random coefficient models as state evidence. Use the actual formulas, actual alpha_h/beta_h/C_h coefficients, and the physical bivariate phase e(hX/(4d)); if a toy surrogate is included, label it as toy evidence and do not use it for status changes. If no committed script, exact command, table, and report are produced, say the computation was not executed. If you cannot physically write files through the API, output an `## Artifact bundle` with repository-relative file paths, complete script contents, exact commands, expected table schemas, precision/log fields, and a short report template so the local orchestrator or Codex can materialize and run them. When a proof step is plausible but not certified, say exactly which formula, theorem hypothesis, citation, or numerical check would certify it.



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

This is Stage B cross review for Round 2.

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
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/round_001/responses/A1_reasoning_1.md"
        ],
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md"
        ],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A2-2.md",
          "rounds/round_001/responses/A3.md"
        ]
      },
      "owner": "A2",
      "next_action": "Use M9-M2-beta-algebra, M9-M2-h-cauchy-sign-loss, and M9-M2-fourth-moment-expansion to decide whether the next M2 attack should use fourth moments, CRI, or direct signed bilinear estimates. Do not promote M9-M2 without a uniform endpoint estimate.",
      "last_updated_round": 1,
      "last_updated_at": "2026-06-26T01:40:44"
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
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md"
        ],
        "inconclusive": [
          "rounds/web-research-test/round_027/judge/judge-027.md",
          "rounds/round_001/responses/A2.md",
          "rounds/round_001/responses/A2-2.md"
        ]
      },
      "owner": "A2",
      "next_action": "Repair the taxonomy using the corrected two-sided fourth-moment numerator N and actual beta_h weights. Classify exact N=0 and 0<|N|~T configurations with counterexample-tested sign rules only.",
      "last_updated_round": 1,
      "last_updated_at": "2026-06-26T01:40:44"
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
          "rounds/round_001/reviews/A1_review_1.md"
        ]
      },
      "owner": "A3",
      "next_action": "Produce computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and report.md using the actual M1/M2 raw formulas and actual Vaaler coefficients. Verify real-weight paired equality and complex-weight failure of the paired real formulas. Mark all evidence diagnostic_only.",
      "last_updated_round": 1,
      "last_updated_at": "2026-06-26T01:40:44"
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
          "rounds/round_001/reviews/A1_review_1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/round_001/responses/A2.md",
          "rounds/obligation-main/round_001/judge/judge-001.md"
        ]
      },
      "owner": "A2",
      "next_action": "Classify exact and near-collision configurations using this N, actual beta_h weights, and a fixed two-sided convention.",
      "last_updated_round": 1,
      "last_updated_at": "2026-06-26T01:40:44"
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
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 1 in run `obligation-main`.

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
  Next action: Use M9-M2-beta-algebra, M9-M2-h-cauchy-sign-loss, and M9-M2-fourth-moment-expansion to decide whether the next M2 attack should use fourth moments, CRI, or direct signed bilinear estimates. Do not promote M9-M2 without a uniform endpoint estimate.
- `M9-near-collision-taxonomy` (open, owner `A2`): M2 fourth-moment near-collision taxonomy
  Next action: Repair the taxonomy using the corrected two-sided fourth-moment numerator N and actual beta_h weights. Classify exact N=0 and 0<|N|~T configurations with counterexample-tested sign rules only.
- `M9-regression-raw-vs-paired` (proposed, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Produce computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and report.md using the actual M1/M2 raw formulas and actual Vaaler coefficients. Verify real-weight paired equality and complex-weight failure of the paired real formulas. Mark all evidence diagnostic_only.

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

created: M9-M2-beta-algebra, M9-M2-h-cauchy-sign-loss, M9-M2-fourth-moment-expansion; updated: M9-M2-character-factor, M9-near-collision-taxonomy, M9-regression-raw-vs-paired; rejected: A2-M9-M2-character-factor-proved-internal-claim, A2-M9-near-collision-taxonomy-blocked-claim, A2-M9-Gallagher-Aliasing-Derivative-Block, A2-2-M9-Poisson-diagonal-capacity, A3-M9-regression-diagnostic-only-promotion, A3-M9-regression-script-duplicate; no_change: M9, M9-M1, M9-M2, M9-endpoint-uniformity, GC-target, H4, Li-Yang-source-audit; round score: 4; Round 1 made useful algebraic progress on the M2 coefficient and clarified Cauchy/fourth-moment diagnostics, but A2 and A3 overpromoted claims and no analytic endpoint estimate was proved.

## Active Obligation Briefs

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Use M9-M2-beta-algebra, M9-M2-h-cauchy-sign-loss, and M9-M2-fourth-moment-expansion to decide whether the next M2 attack should use fourth moments, CRI, or direct signed bilinear estimates. Do not promote M9-M2 without a uniform endpoint estimate.

### M9-near-collision-taxonomy: M2 fourth-moment near-collision taxonomy

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`
- Next action: Repair the taxonomy using the corrected two-sided fourth-moment numerator N and actual beta_h weights. Classify exact N=0 and 0<|N|~T configurations with counterexample-tested sign rules only.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `proposed`
- Track: `computation`
- Owner: `A3`
- Next action: Produce computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and report.md using the actual M1/M2 raw formulas and actual Vaaler coefficients. Verify real-weight paired equality and complex-weight failure of the paired real formulas. Mark all evidence diagnostic_only.

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
- Next action: Classify exact and near-collision configurations using this N, actual beta_h weights, and a fixed two-sided convention.

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

Generated after round 1 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_001/judge/judge-001.md`.

## For A1

Target obligations: `M9-M2-beta-algebra`, `M9-M2-h-cauchy-sign-loss`, and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Write a proof-draft-ready coefficient-normalization note using the actual H4 coefficient convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

2. Prove

$$
C_h=e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h}
$$

and

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

3. State the paired real $\mathcal M_2$ formula for real dyadic weights only, and explicitly state why complex weights are outside that formula's hypotheses.

4. Write the weighted $h$-Cauchy sign-loss diagnostic and the unweighted $h$-Cauchy endpoint diagonal check as bounded-scope diagnostics, not no-go theorems.

5. Insert the corrected two-sided fourth-moment expansion and cleared numerator $N$ into the proof draft.

6. Do not promote `M9`, `M9-M2`, or `M9-near-collision-taxonomy`.

Exploratory allocation: give a one-page comparison of fourth moment, CRI, and direct signed bilinear routes for $\mathcal M_2$, with one falsification criterion for each.

Route-strengthening requirement: include `## Route proposals` with at least two serious proof routes. For each route, state the exact lemma it would prove, why it might work, which obstruction it attacks, dependencies, the first proof step, a fast falsification test, and a ranking against the other route.

## For A2

Target obligations: `M9-near-collision-taxonomy` and `M9-M2-fourth-moment-expansion`.

Objectives:

1. Rewrite the fourth-moment taxonomy using the actual $\Phi$-weighted coefficient $\beta_h$, not a Fejer-linear surrogate.

2. Use exactly one convention: preferably the two-sided convention

$$
1\le |h|\le H_D.
$$

3. Use the corrected phase

$$
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
$$

and the corrected numerator

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

4. Classify exact $N=0$ families: exact diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified.

5. For every claimed class, give either a proof, a counterexample, or a status label from the allowed reasoning labels: `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, `[LIKELY-FALSE]`.

6. Remove or repair the Gallagher obstruction. If retained, state a precise theorem with hypotheses and explain exactly how the M2 variables violate it.

7. Do not claim that A2-2's Poisson diagonal-capacity model proves M9. If used, restate it as exploratory and connect it back to the actual reciprocal $\mathcal M_2$ formula.

Exploratory allocation: define one CRI statistic under the two-sided convention and state what numerical behavior would falsify CRI as a serious route.

Route-strengthening requirement: include `## Repair or alternative route`. Do not only reject A1's route. Either repair the strongest criticized route into a narrower lemma, or propose one alternative route with exact hypotheses, proof-obligation impact, and a fast falsification test.

## For A3

Target obligation: `M9-regression-raw-vs-paired`.

Objectives:

1. Produce actual files, not only a protocol:

- `computations/m9_regression/run.py`
- `outputs/table_small.csv`
- a precision log
- `computations/m9_regression/report.md`

2. Use the actual raw two-sided M1/M2 formulas and actual Vaaler coefficients.

3. For real dyadic weights, verify raw two-sided sums equal the paired formulas to numerical precision.

4. For complex dyadic weights, verify that the paired real formulas fail unless modified.

5. Include explicit checks for

$$
C_h=2i\chi_4(h)1_{2\nmid h},
\qquad
|C_h|=2 \text{ for odd } h,
\qquad
\beta_{-h}=\beta_h.
$$

6. Include a weighted $h$-Cauchy sign-loss regression showing that $|C_h|^2=4\,1_{2\nmid h}$.

7. Include a small fourth-moment binning routine using the corrected $N$ formula. Label results diagnostic only.

8. Do not use surrogate kernels as official evidence. Toy kernels may appear only in a separate exploratory appendix.

Exploratory allocation: add one complex-weight failure test and one small exact-bin enumeration for A2's corrected taxonomy.

Route-strengthening requirement: translate the leading A1/A2 routes into executable checks where possible. If a route cannot be tested computationally, say exactly why and propose the closest diagnostic-only proxy.

## Round Assessment

Round 1 is useful but not proof-progress at the endpoint. The correct state update is narrow:

- Accept the exact $C_h$ and $\beta_h$ algebra, conditional on H4.
- Accept the weighted $h$-Cauchy sign-loss diagnostic.
- Accept the fourth-moment expansion and corrected numerator as algebraic reductions.
- Keep `M9`, `M9-M2`, and `M9-near-collision-taxonomy` open.
- Keep `M9-regression-raw-vs-paired` proposed until actual files exist.
- Reject A2's and A2-2's broad state promotions.
- Reject A3's algebraic premise about $\beta_{-h}$ and its surrogate-kernel evidence.

Scores for the reviewed non-judge agents, using the Stage B assessment:

| Agent | Score | Reason |
|---|---:|---|
| A2 | 5.0 | Correct base $C_h$ direction and useful fourth-moment instinct, but several central claims are false or unsupported, including the $16(-1)^{N/2}$ rule, denominator parity sieve, Gallagher obstruction, and state-patch promotions. |
| A3 | 5.5 | Correctly targets executable diagnostics, but the main premise about $\beta_{-h}$ is wrong, the official computation is not executed, and the surrogate kernel is not state evidence. |

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

--- HUMAN FILE: rounds/obligation-main/round_002/human/stage-b-review-audit.md ---
# Round 2 Stage B Review Audit For Judge

Use this note when writing the Round 2 judge synthesis. It is a human/Codex audit of the three Stage B reviews after normalization.

## Consensus

- Accept the algebraic core: `C_h=2i chi_4(h)1_{2\nmid h}`, real-even `beta_h` under the current H4 convention, the raw two-sided M2 convention, the real-weight paired formula as implementation-only, and the corrected fourth-moment numerator

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

- Accept `h`-Cauchy sign-loss and endpoint diagnostics only as bounded guardrails.
- Record the diagonal-core observation only as `O(D^2) <= O(X)` compatibility. Do not use A2's exact `D^2/16` constant for the whole core.
- Reject promotion of `M9-near-collision-taxonomy`; exact taxonomy has unclassified residue and near-collision bands are unproved.
- Reject promotion of `M9`, `M9-M2`, `M9-near-collision-estimate`, and `GC-target`.
- Reject A3 evidence claims unless actual scripts/tables/logs exist.

## Review Weighting

- A1 review is the best calibrated and should guide state mutation.
- A3 review is also well calibrated and independently confirms the main downgrade decisions.
- A2 review has useful technical checks, but it pushes too hard toward a shifted-bilinear pivot. Treat that as a serious backup route, not as the new primary route.

## Recommended State Treatment

- `M9-M2-beta-algebra`: keep `derived_under_assumptions`, H4-dependent.
- `M9-M2-h-cauchy-sign-loss`: keep as bounded diagnostic / `derived_under_assumptions`.
- `M9-M2-fourth-moment-expansion`: keep `derived_under_assumptions` for algebra only.
- `M9-near-collision-taxonomy`: keep open.
- `M9-regression-raw-vs-paired`: keep proposed until actual committed artifacts exist.
- Optional new obligation: `M9-N0-diagonal-bound`, status `proposed` or `open`, for proving the `N=0` diagonal-core bound with actual `beta_h` and weights.

## Next Round

Primary route: M2 fourth moment with exact `N=0` taxonomy and near-collision lemma.

Backup route: direct signed bilinear estimate / residue-interference route, but only after A2 states a precise theorem, matrix norm, and endpoint spacing audit.

A3 must execute actual local diagnostics, not just describe them.

## Score Calibration Addendum

When scoring A2 and A3, separate:

- `idea_quality_score`: useful formulas, routes, diagnostics, or proof objects;
- `state_evidence_score`: evidence safe enough to mutate `state/proof_obligations.yml`;
- `calibration_score`: correct use of statuses and avoidance of overclaiming.

A2 should not be scored low because its route ideas are worthless; it should be scored low on state evidence because broad claims remain unproved and several `[PROVED]` labels are premature. A3 should not be scored low because diagnostics are irrelevant; it should be scored low on state evidence because scripts, commands, tables, logs, and reports are not yet committed.

For the State Patch, keep the single `mathematical_progress_score` conservative. In prose, include the split scores so future prompts can target the right failure mode:

- A2: good idea quality, weak state evidence, weak-to-moderate calibration.
- A3: good diagnostic design, weak state evidence until artifacts exist, moderate calibration.

## Outputs To Review

--- OUTPUT FROM A1 ---
## Summary

This is a Stage A independent reasoning response for A1. The assigned A1 obligations are `M9-M2-beta-algebra`, `M9-M2-h-cauchy-sign-loss`, and `M9-M2-fourth-moment-expansion`; the prompt also explicitly says not to promote `M9`, `M9-M2`, or `M9-near-collision-taxonomy`. The current reading packet keeps `M9` open and identifies `M9-M2-character-factor`, `M9-near-collision-taxonomy`, and `M9-endpoint-uniformity` as blockers, with the round target focused on the M2 character factor, near-collision taxonomy, and raw-vs-paired regression.

Main output:

- I normalize the $\mathcal M_2$ coefficient under the current H4 convention.
- I prove
$$
  C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h}.
$$
- I derive the actual fixed coefficient
$$
  \beta_{h,H}
  =
  \alpha_{h,H}C_h
  =
  -\frac{\Phi(|h|/(H+1))}{\pi |h|}
  \chi_4(|h|)1_{2\nmid h}.
$$
  In particular, $\beta_{-h,H}=\beta_{h,H}$ is real and even.
- I state the raw two-sided $\mathcal M_2$ formula and the paired real formula. The paired real formula is valid only for real dyadic weights.
- I give two bounded-scope Cauchy diagnostics:
  - weighted $h$-Cauchy has acceptable diagonal size but loses the $\chi_4(h)$ sign;
  - unweighted $h$-Cauchy has an endpoint diagonal of size $D H_D$, which is $X^{3/4}$ at $D\asymp X^{1/2}$.
- I record the corrected fourth-moment expansion and the cleared numerator
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
- I recommend the fourth-moment route as the primary next analytic route for $\mathcal M_2$, with CRI as a falsification/structure statistic and direct signed bilinear estimates as a backup.

No endpoint estimate is proved. The correct state remains: `M9` open, `M9-M2` open, and `M9-near-collision-taxonomy` open. The uploaded state explicitly says computation evidence for `M9-regression-raw-vs-paired` is diagnostic only and requires actual scripts/tables before promotion.

## Target proof obligation

Primary obligations for this response:

1. `M9-M2-beta-algebra`: exact coefficient algebra for the $\mathcal M_2$ Vaaler main term.
2. `M9-M2-h-cauchy-sign-loss`: bounded-scope diagnostic for the natural weighted $h$-Cauchy step.
3. `M9-M2-fourth-moment-expansion`: corrected two-sided fourth-moment expansion with the actual coefficient product and the cleared numerator $N$.

Connected obligations not promoted here:

- `M9-M2-character-factor`: still open as an analytic obstruction/guardrail.
- `M9-near-collision-taxonomy`: still open; this response gives a safe taxonomy framework but not a completed classification.
- `M9-near-collision-estimate`: still proposed; no near-collision estimate is proved.
- `M9-M2`: still open; no uniform endpoint estimate for $\mathcal M_2(D;X)$ is proved.
- `M9`: still open; no final Gauss circle bound is proved.
- `GC-target`: still open and conditional on `M9`.

The current packet says the fixed-coefficient M2 estimate remains open and depends on `H4`, `M9-M2-character-factor`, and `M9-near-collision-taxonomy`.

## Main claim or direction

The main claim is an algebraic and strategic one:

The $\mathcal M_2$ main term must be treated with the fixed coefficient

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

not with an arbitrary bounded coefficient and not with a Fejer-linear surrogate. The coefficient is real, even, supported on odd frequencies, and carries a residue-class sign through $\chi_4(|h|)$.

The most viable next analytic route is therefore not the standard weighted second moment, because that immediately replaces $C_h$ by $|C_h|^2$ and loses the frequency-side sign. The primary next route should be a two-sided fourth-moment or open-path statistic that retains the product of the four $\beta_h$ coefficients before absolute-value majorization.

The route is conditional on the current H4 coefficient convention. H4 itself remains a source-audit dependency in the state packet. The reading packet lists H4 as `source_audit_required` and says the exact theorem labels, constants, residual convention, and integer values still need verification from Vaaler's rendered source pages.

## Detailed reasoning

### 1. Basic notation and active range

Use

$$
e(t)=e^{2\pi i t}.
$$

The current local Vaaler height is

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

The $\mathcal M_2$ main term is

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Set

$$
B_h(D;X)=\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Then

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}C_h B_h(D;X),
$$

where

$$
C_h=e(h/4)-e(3h/4).
$$

The current H4 coefficient convention is

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

where

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

This coefficient convention is the one assigned in the A1 prompt.

### 2. Exact calculation of $C_h$

Evaluate $C_h$ modulo $4$.

If $h\equiv0\pmod4$, then

$$
e(h/4)=1,
\qquad
e(3h/4)=1,
$$

so $C_h=0$.

If $h\equiv2\pmod4$, then

$$
e(h/4)=-1,
\qquad
e(3h/4)=-1,
$$

so again $C_h=0$.

If $h\equiv1\pmod4$, then

$$
e(h/4)=i,
\qquad
e(3h/4)=-i,
$$

so $C_h=2i$.

If $h\equiv3\pmod4$, then

$$
e(h/4)=-i,
\qquad
e(3h/4)=i,
$$

so $C_h=-2i$.

With the standard character

$$
\chi_4(h)=
\begin{cases}
0,&2\mid h,\\
1,&h\equiv1\pmod4,\\
-1,&h\equiv3\pmod4,
\end{cases}
$$

this gives the exact identity

$$
\boxed{
C_h=2i\chi_4(h)1_{2\nmid h}.
}
$$

The indicator is redundant if $\chi_4$ is defined to vanish on even integers, but it is useful to keep odd support explicit.

### 3. Exact calculation of $\beta_{h,H}$

Define

$$
\beta_{h,H}:=\alpha_{h,H}C_h.
$$

For $h>0$,

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h}
=
\frac{i}{2\pi h}\Phi(h/(H+1)).
$$

Thus for odd $h>0$,

$$
\beta_{h,H}
=
\frac{i}{2\pi h}\Phi(h/(H+1))
\cdot
2i\chi_4(h)
=
-\frac{\Phi(h/(H+1))}{\pi h}\chi_4(h).
$$

For $h=-r<0$, $r>0$,

$$
\alpha_{-r,H}
=
-\frac{\Phi(r/(H+1))}{2\pi i(-r)}
=
-\frac{i}{2\pi r}\Phi(r/(H+1)).
$$

Also

$$
C_{-r}
=
2i\chi_4(-r)1_{2\nmid r}
=
-2i\chi_4(r)1_{2\nmid r}.
$$

Therefore, for odd $r$,

$$
\beta_{-r,H}
=
\left(
-\frac{i}{2\pi r}\Phi(r/(H+1))
\right)
\left(
-2i\chi_4(r)
\right)
=
-\frac{\Phi(r/(H+1))}{\pi r}\chi_4(r).
$$

Hence

$$
\boxed{
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
}
$$

Consequences:

$$
\boxed{\beta_{-h,H}=\beta_{h,H}\in\mathbb R.}
$$

This parity is a key correction. The coefficient is not odd in $h$ and is not imaginary after multiplication by $C_h$.

### 4. Raw two-sided formula and paired real formula

The raw formula is canonical:

$$
\boxed{
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}B_h(D;X).
}
$$

This remains valid for complex dyadic weights.

If $w_D$ is real-valued, then

$$
B_{-h}(D;X)
=
\overline{B_h(D;X)}.
$$

Since $\beta_{-h,H_D}=\beta_{h,H_D}$ is real,

$$
\sum_{1\le |h|\le H_D}\beta_{h,H_D}B_h
=
2\sum_{1\le h\le H_D}\beta_{h,H_D}\operatorname{Re}B_h.
$$

Thus, for real $w_D$,

$$
\boxed{
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
}
$$

This paired formula is not valid as written for complex $w_D$. If $w_D$ is complex, then generally

$$
B_{-h}\ne \overline{B_h},
$$

so the raw two-sided formula must be used.

This is exactly the regression distinction required by `M9-regression-raw-vs-paired`: real-weight equality should hold, while complex-weight paired-real failure should be detected and labelled diagnostic only. The prompt requires A3 to produce actual files and verify the real-weight equality and complex-weight failure.

### 5. Weighted $h$-Cauchy sign-loss diagnostic

Let

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}\alpha_{h,H_D}C_hB_h(D;X),
$$

so that

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

Let

$$
L_\alpha=\sum_{1\le |h|\le H_D}|\alpha_{h,H_D}|.
$$

Since

$$
|\alpha_{h,H_D}|\ll |h|^{-1},
$$

we have

$$
L_\alpha\ll \log H_D.
$$

Weighted Cauchy gives

$$
|S_2|^2
\le
\left(
\sum_h|\alpha_h|
\right)
\left(
\sum_h|\alpha_h||C_h|^2|B_h|^2
\right).
$$

But

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

Thus the second factor becomes

$$
4\sum_{\substack{1\le |h|\le H_D\\2\nmid h}}
|\alpha_h||B_h|^2.
$$

After expanding $|B_h|^2$, the kernel is

$$
K_{2;d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)\overline{w_D(d_2)}
\sum_{\substack{1\le |h|\le H_D\\2\nmid h}}
4|\alpha_{h,H_D}|
e\left(
\frac{hX}{4}
\left(
\frac1{d_1}-\frac1{d_2}
\right)
\right).
$$

The sign $\chi_4(h)$ has disappeared. Only odd support remains.

The diagonal size in this weighted normalization is acceptable. If $|w_D(d)|\ll1$ and $d\asymp D$, then

$$
\sum_d |w_D(d)|^2\ll D,
$$

and the diagonal contribution to the Cauchy bound is

$$
\ll
L_\alpha
\left(
\sum_h|\alpha_h||C_h|^2
\right)
D
\ll
D(\log H_D)^2.
$$

Since $D\le X^{1/2}$,

$$
D(\log H_D)^2\ll_\epsilon X^{1/2+\epsilon}.
$$

This matches the squared endpoint scale. Therefore the problem with weighted $h$-Cauchy is not the diagonal; the problem is sign loss.

This diagnostic is already recorded in the state as `M9-M2-h-cauchy-sign-loss`, with the warning that it should not be treated as a global no-go theorem.

### 6. Unweighted $h$-Cauchy endpoint diagonal diagnostic

Unweighted Cauchy gives

$$
|S_2|^2
\le
2H_D
\sum_{1\le |h|\le H_D}
|\beta_{h,H_D}|^2|B_h|^2.
$$

The diagonal after expanding $|B_h|^2$ is

$$
\ll
H_D
\left(
\sum_{1\le |h|\le H_D}|\beta_{h,H_D}|^2
\right)
D.
$$

Since

$$
|\beta_{h,H_D}|\ll |h|^{-1},
$$

we have

$$
\sum_{1\le |h|\le H_D}|\beta_{h,H_D}|^2\ll1.
$$

Thus the diagonal is

$$
\ll D H_D.
$$

Using

$$
H_D\asymp D X^{-1/4},
$$

we obtain

$$
D H_D\asymp D^2X^{-1/4}.
$$

At the top endpoint

$$
D\asymp X^{1/2},
$$

this becomes

$$
X^{3/4}.
$$

The squared target for $S_2$ is $X^{1/2+\epsilon}$. Hence unweighted $h$-Cauchy has an endpoint diagonal excess of $X^{1/4}$ at the top dyadic block.

Again, this is a bounded-scope diagnostic for that normalization, not a proof that all $\mathcal M_2$ methods fail.

### 7. Corrected two-sided fourth-moment expansion

Use the exact fixed coefficient

$$
\beta_h
=
-\frac{\Phi(|h|/(H_D+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

Let

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Then

$$
|S_2|^4=S_2\overline{S_2}S_2\overline{S_2}.
$$

Expanding gives

$$
|S_2|^4
=
\sum_{\mathbf h}
\sum_{\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
w_D(d_1)\overline{w_D(d_2)}
w_D(d_3)\overline{w_D(d_4)}
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

Because $\beta_h$ is real under the current convention, the conjugates on $\beta_{h_2}$ and $\beta_{h_4}$ do not alter their values. They are kept in the formula to preserve the origin of each factor.

Clearing denominators with

$$
Q=d_1d_2d_3d_4,
$$

we have

$$
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
=
\frac{N}{Q},
$$

where

$$
\boxed{
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
}
$$

This matches the corrected numerator required by the prompt for A2 and A3.

The coefficient product before absolute-value majorization is

$$
\prod_{j=1}^4
\left(
-\frac{\Phi(|h_j|/(H_D+1))}{\pi |h_j|}
\chi_4(|h_j|)1_{2\nmid h_j}
\right).
$$

A sufficient fourth-moment target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}.
$$

Since

$$
\mathcal M_2(D;X)=4S_2(D;X),
$$

this would imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

No such estimate is proved here. The current state already records the fourth-moment expansion as `derived_under_assumptions` and says the next action is to classify exact and near-collision configurations using this $N$, the actual $\beta_h$ weights, and a fixed two-sided convention.

### 8. Near-collision scale

In the active dyadic range,

$$
d_j\asymp D,
\qquad
Q=d_1d_2d_3d_4\asymp D^4.
$$

The fourth-moment phase is

$$
e\left(\frac{XN}{4Q}\right).
$$

The rational near-collision scale corresponding to phase variation $O(1)$ is

$$
\left|\frac{XN}{Q}\right|\lesssim1,
$$

or

$$
|N|\lesssim \frac{D^4}{X}.
$$

Define

$$
T_D:=\frac{D^4}{X}.
$$

Then

$$
T_D=1
\quad\text{at}\quad
D=X^{1/4},
$$

and

$$
T_D=X
\quad\text{at}\quad
D=X^{1/2}.
$$

Any taxonomy using a symbol such as $T$ should specify whether it means $T_D=D^4/X$ or another scale. Otherwise the near-collision statement is ambiguous by a factor as large as $X$ across the active dyadic range.

### 9. Preliminary exact-collision taxonomy

This is not a completed `M9-near-collision-taxonomy`. It is only a safe framework for A2.

Let

$$
\mathfrak f_j=\frac{h_j}{d_j}.
$$

Exact collision means

$$
\mathfrak f_1-\mathfrak f_2+\mathfrak f_3-\mathfrak f_4=0.
$$

Equivalently, $N=0$.

#### Family A: direct diagonal

If

$$
(h_1,d_1)=(h_2,d_2),
\qquad
(h_3,d_3)=(h_4,d_4),
$$

then $N=0$.

The coefficient mass is bounded by

$$
\sum_{h_1,h_3}|\beta_{h_1}|^2|\beta_{h_3}|^2
\sum_{d_1,d_3}|w_D(d_1)|^2|w_D(d_3)|^2
\ll D^2.
$$

Since $D\le X^{1/2}$, this is

$$
\ll X.
$$

This is compatible with the fourth-moment target $X^{1+\epsilon}$.

Status: proved algebraic family with compatible mass estimate under bounded dyadic weights.

#### Family B: pair-swapped diagonal

If

$$
(h_1,d_1)=(h_4,d_4),
\qquad
(h_3,d_3)=(h_2,d_2),
$$

then $N=0$.

The same mass estimate gives

$$
\ll D^2\le X.
$$

Status: proved algebraic family with compatible mass estimate under bounded dyadic weights.

#### Family C: reduced-fraction diagonal

It is enough that

$$
\frac{h_1}{d_1}=\frac{h_2}{d_2},
\qquad
\frac{h_3}{d_3}=\frac{h_4}{d_4}.
$$

Writing

$$
h_i=a_i r_i,
\qquad
d_i=b_i r_i,
\qquad
(a_i,b_i)=1,
$$

this creates additional scaled diagonal families.

The $1/|h|$ coefficient weights should help, but a complete divisor-sum estimate is not written here. This belongs in A2's taxonomy task.

Status: algebraic family identified; estimate open.

#### Family D: sign-symmetric two-sided exact resonances

Because the convention is two-sided in $h$, exact cancellation may occur through sign pairs such as

$$
\frac{h_1}{d_1}+\frac{h_3}{d_3}=0,
\qquad
\frac{h_2}{d_2}+\frac{h_4}{d_4}=0.
$$

For example,

$$
(h_3,d_3)=(-h_1,d_1),
\qquad
(h_4,d_4)=(-h_2,d_2)
$$

gives $N=0$.

Since

$$
\beta_{-h}=\beta_h,
$$

these families are not killed by coefficient oddness. They must be included in any exact taxonomy.

Status: algebraic family identified; mass estimate expected to be diagonal-size but not written here.

#### Family E: denominator-paired and mixed linear families

If some denominator equalities hold, such as

$$
d_1=d_2,
$$

then the equation becomes

$$
\frac{h_1-h_2}{d_1}
+
\frac{h_3}{d_3}
-
\frac{h_4}{d_4}
=0.
$$

This can generate lower-dimensional linear families not captured by direct diagonal labels. These may be harmless, but they cannot be dismissed without a count.

Status: unclassified.

#### Family F: truncation-edge families

The coefficient $\Phi(|h|/(H_D+1))/|h|$ changes near the top of the $h$-range. Edge configurations with some $h_i$ near $H_D$ may not have the same weight profile as central configurations.

Status: unclassified; likely not a main obstruction, but should be explicitly checked.

#### Family G: rational near-collisions

Near-collisions satisfy

$$
0<|N|\lesssim T_D=\frac{D^4}{X}.
$$

At the top endpoint, this allows $|N|\lesssim X$, a large band. Absolute counting in this band may be too large unless the $\beta_h$ signs or oscillation in $N$ are retained.

Status: central open issue.

## Theorem-dependency audit

### Dependency 1: H4 Vaaler approximation

The coefficient algebra uses the H4 convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

The uploaded state still lists H4 and H4-source-audit as source-audit obligations. Vaaler's paper is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bulletin of the American Mathematical Society* 12(2), 183--216, 1985, as verified by Project Euclid and AMS metadata.

Failure criterion: if the source-card audit changes the sign or normalization of $\alpha_{h,H}$, then the formula for $\beta_{h,H}$ must be recomputed. The identity for $C_h$ is independent of H4.

### Dependency 2: floor-compatible sawtooth convention

The arithmetic sawtooth is

$$
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12.
$$

The Vaaler trigonometric polynomial uses centered discontinuity conventions, so integer jumps must be handled by the Fejer majorant. This dependency belongs to H4 and H4-source-audit.

Failure criterion: if the proof silently switches to midpoint sawtooth values at integers, the balanced arithmetic identity can fail at discontinuities.

### Dependency 3: H1--H3 balanced arithmetic reductions

This response does not reprove H1--H3. It uses the already accepted bridge structure. The reading packet says the current route is

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

It also records R5-Full as derived under assumptions and pending insertion after H4 source audit.

Failure criterion: any endpoint or convention error in H1--H3 would change the sawtooth legs feeding $\mathcal M_2$.

### Dependency 4: R5-Full residual bound

R5-Full is not used in this coefficient algebra except to keep the residual side separate. The active target here is the main term. R5-Full remains conditional on H4 source normalization.

Failure criterion: if R5-Full fails at exact Fejer spikes, shifted legs, or real $X$ endpoints, residual terms return as active blockers.

### Dependency 5: Li--Yang / Bombieri--Iwaniec technology

No Li--Yang theorem is used as a dependency here. Li--Yang's arXiv paper states that it uses the Bombieri--Iwaniec method, proves a new first-spacing estimate, and combines it with Huxley's second-spacing results. Their Theorem 1.2 states bounds for $R(X)$ and $\Delta(X)$ with exponent $\theta^*=0.314483\ldots$, while the conjectural exponent is $\theta=1/4$.

Failure criterion for black-box use: any future invocation must verify the theorem's exact parameter ranges, weights, and endpoint height. Structural phase similarity is not theorem applicability.

### Dependency 6: fourth-moment analytic estimate

The expansion of $|S_2|^4$ is algebraic. The estimate

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

is not proved.

Failure criterion: exact or near-collision families with signed or absolute weighted mass larger than $X^{1+\epsilon}$, with no exploitable oscillation, would refute the proposed fourth-moment route in its current form.

## Hidden assumptions and potential gaps

1. **H4 coefficient convention is assumed.**
   The coefficient algebra is conditional on the current H4 normalization. It should remain dependent on `H4-source-audit`.

2. **Paired real formulas require real weights.**
   The paired $\operatorname{Re}B_h$ formula fails for general complex $w_D$. This is not a minor implementation detail; it is a hypothesis of the identity.

3. **The fourth-moment target may be too strong.**
   The bound
$$
   |S_2|^4\ll_\epsilon X^{1+\epsilon}
$$
   is sufficient but not necessary. A proof of $\mathcal M_2$ could use cancellation not visible in the fourth moment.

4. **Exact diagonal classes are not the main risk.**
   The direct and pair-swapped diagonals are compatible with the target. The risk is in reduced-fraction diagonals, denominator-paired linear families, sign-symmetric two-sided families, and near-collisions.

5. **Absolute-value majorization may destroy the character advantage.**
   The fourth-moment expansion retains
$$
   \prod_{j=1}^4 \chi_4(|h_j|)
$$
   only before taking absolute values over all $h_i$.

6. **The near-collision scale must be fixed.**
   A statement like $0<|N|\sim T$ is not meaningful until $T$ is defined. The natural scale is
$$
   T_D=D^4/X.
$$

7. **Phase aliasing is distinct from rational near-collision.**
   Small $|N|$ is one route to slow phase, but for structured real or integer $X$, one could also have
$$
   \left\|\frac{XN}{4Q}\right\|\ll1
$$
   even when $N$ is not small. This should be treated as a separate diagnostic, not folded into a vague Gallagher obstruction.

8. **M1 is not addressed.**
   Even a successful M2 route would not prove M9 unless M1 and uniformity over the full active dyadic range are also handled.

## Counterexample or obstruction search

### Obstruction 1: complex-weight paired formula failure

For complex $w_D$,

$$
B_{-h}(D;X)
=
\sum_d w_D(d)e(-hX/(4d))
$$

need not equal

$$
\overline{B_h(D;X)}
=
\sum_d \overline{w_D(d)}e(-hX/(4d)).
$$

Thus the paired real formula is generally false for complex weights.

Fast test: take $w_D(d)=i$ on the dyadic block. Then $B_{-h}=i\sum_d e(-hX/(4d))$, whereas $\overline{B_h}=-i\sum_d e(-hX/(4d))$.

### Obstruction 2: weighted $h$-Cauchy loses frequency sign

Weighted Cauchy creates

$$
|C_h|^2=4\,1_{2\nmid h}.
$$

Thus a second-moment proof based only on this kernel is blind to the sign of $\chi_4(h)$.

Fast test: compare the weighted second-moment kernel with and without replacing $\chi_4(h)$ by $1$ on odd $h$. They are identical.

### Obstruction 3: unweighted $h$-Cauchy endpoint diagonal

Unweighted $h$-Cauchy has diagonal

$$
D H_D=D^2X^{-1/4}.
$$

At $D=X^{1/2}$ this is

$$
X^{3/4},
$$

which exceeds the squared target $X^{1/2+\epsilon}$.

Fast test: compute only diagonal terms after unweighted Cauchy at $D=X^{1/2}$.

### Obstruction 4: reduced-fraction multiplicity

Exact equality

$$
\frac{h_1}{d_1}=\frac{h_2}{d_2}
$$

can occur without equality of pairs. The $1/|h|$ weights help, but this multiplicity must be counted.

Fast test: enumerate reduced fractions $a/b$ with $ar\le H_D$ and $br\asymp D$, then measure

$$
A(a,b)=\sum_r |\beta_{ar}|^2|w_D(br)|^2.
$$

The reduced-fraction diagonal mass is controlled by sums of $A(a,b)^2$.

### Obstruction 5: modular or phase aliasing

Even if $|N|$ is not small, the phase can be near stationary modulo $1$ if

$$
\left\|\frac{XN}{4d_1d_2d_3d_4}\right\|
$$

is small. This is not the same as the rational near-collision condition $|N|\lesssim D^4/X$.

Fast test: for integer $X$ and dyadic endpoint blocks, bin quadruples by the nearest-integer distance of $XN/(4Q)$, not only by $|N|$.

## Verification

The following algebraic checks are complete under the stated H4 coefficient convention.

1. **Modulo-$4$ table for $C_h$.**

$$
   C_h=e(h/4)-e(3h/4)=2i\chi_4(h)1_{2\nmid h}.
$$

2. **Conjugacy of $\alpha_h$.**

Since $\Phi(|h|/(H+1))$ is real,

$$
   \alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

3. **Reality and evenness of $\beta_h$.**

$$
   \beta_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{\pi |h|}
   \chi_4(|h|)1_{2\nmid h},
$$

so

$$
   \beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

4. **Paired formula for real weights.**

If $w_D$ is real,

$$
   B_{-h}=\overline{B_h},
$$

and therefore

$$
   \mathcal M_2(D;X)
   =
   -\frac8\pi
   \sum_{\substack{1\le h\le H_D\\2\nmid h}}
   \frac{\Phi(h/(H_D+1))}{h}
   \chi_4(h)
   \operatorname{Re}B_h(D;X).
$$

5. **Weighted $h$-Cauchy sign loss.**

$$
   |C_h|^2=4\,1_{2\nmid h}.
$$

6. **Unweighted $h$-Cauchy diagonal.**

$$
   D H_D\asymp D^2X^{-1/4},
$$

which is $X^{3/4}$ at $D=X^{1/2}$.

7. **Cleared numerator.**

Multiplying

$$
   \frac{h_1}{d_1}
   -
   \frac{h_2}{d_2}
   +
   \frac{h_3}{d_3}
   -
   \frac{h_4}{d_4}
$$

by $d_1d_2d_3d_4$ gives

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

## Divergent alternatives and 20% exploration

### Alternative 1: fourth moment with signed near-collision taxonomy

Object:

$$
|S_2(D;X)|^4.
$$

Why it might work: the product

$$
\beta_{h_1}\overline{\beta_{h_2}}\beta_{h_3}\overline{\beta_{h_4}}
$$

retains the frequency-side residue signs before absolute-value majorization. This avoids the immediate loss in weighted $h$-Cauchy.

Needed lemma:

For all active $D$,

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}.
$$

Fast falsification: exact and near-collision bins with $|N|\lesssim D^4/X$ have signed weighted mass $\gg X^{1+c}$ after retaining the actual $\beta_h$ signs.

### Alternative 2: CRI, residue-class interference

For real weights, define

$$
\Sigma_r^R(D;X)
=
\sum_{\substack{1\le h\le H_D\\h\equiv r\pmod4}}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Re}B_h(D;X),
\qquad
r\in\{1,3\}.
$$

Then

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\left(
\Sigma_1^R-\Sigma_3^R
\right).
$$

Define

$$
R_{\rm CRI}
=
\frac{|\Sigma_1^R-\Sigma_3^R|^2}
{|\Sigma_1^R|^2+|\Sigma_3^R|^2},
$$

when the denominator is nonzero.

Why it might work: if the two residue classes produce highly correlated real sums, the difference may be significantly smaller than either component.

Needed lemma:

A bound of the form

$$
|\Sigma_1^R-\Sigma_3^R|\ll_\epsilon X^{1/4+\epsilon}
$$

with proof of favorable cross-correlation, not merely a bound on the separate pieces.

Fast falsification: numerical CRI values persistently near $1$ or $2$ in endpoint blocks.

### Alternative 3: direct signed bilinear estimate

Object:

$$
\sum_{1\le |h|\le H_D}\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Why it might work: this avoids first squaring in $h$ and may preserve the exact fixed $\beta_h$ signs.

Needed lemma:

A reciprocal-phase bilinear estimate with fixed coefficients:

$$
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}.
$$

Fast falsification: the first serious proof step replaces $\beta_h$ by $|\beta_h|$ or treats it only through a diagonal unitary conjugation/operator norm.

## Route proposals

### Route 1: fourth-moment near-collision route

Rank: 1.

Exact lemma to prove:

For

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

prove uniformly for

$$
X^{1/4}\le D\le X^{1/2}
$$

that

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}.
$$

Dependencies:

- H4 coefficient convention.
- `M9-M2-beta-algebra`.
- Correct fourth-moment expansion and numerator $N$.
- A completed `M9-near-collision-taxonomy`.
- A near-collision estimate for $0<|N|\lesssim D^4/X$.

First proof step:

Classify exact $N=0$ configurations with actual $\beta_h$ weights and two-sided $h$ convention. Start with direct diagonal, pair-swapped, reduced-fraction diagonal, sign-symmetric, denominator-paired, mixed, and truncation-edge cases. Then introduce near-collision bins

$$
|N|\asymp T,
\qquad
1\le T\le D^4/X.
$$

Obstruction attacked:

Weighted $h$-Cauchy sign loss.

Why it might work:

The fourth moment keeps the residue signs through a fourfold product before absolute-value majorization.

Fast falsification:

If exact plus near-collision bins have signed weighted mass larger than $X^{1+\epsilon}$ and no further oscillation remains, the route is unlikely to prove the endpoint.

### Route 2: CRI residue-interference route

Rank: 2.

Exact lemma to prove:

For real $w_D$,

$$
\Sigma_r^R(D;X)
=
\sum_{\substack{1\le h\le H_D\\h\equiv r\pmod4}}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Re}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

prove

$$
|\Sigma_1^R-\Sigma_3^R|
\ll_\epsilon X^{1/4+\epsilon}.
$$

Dependencies:

- Paired real formula.
- Real dyadic weights.
- A cross-correlation estimate for $\Sigma_1^R$ and $\Sigma_3^R$.

First proof step:

Measure and then attempt to prove cancellation in

$$
|\Sigma_1^R-\Sigma_3^R|^2
=
|\Sigma_1^R|^2+|\Sigma_3^R|^2
-
2\operatorname{Re}(\Sigma_1^R\overline{\Sigma_3^R}).
$$

Obstruction attacked:

The frequency character sign is residue-class interference between $h\equiv1$ and $h\equiv3\pmod4$.

Why it might work:

It directly targets the $\chi_4(h)$ sign without expanding to four variables.

Fast falsification:

If $R_{\rm CRI}$ is typically near $1$ or $2$ at endpoint dyadic scales, CRI is not a strong route.

### Route 3: direct fixed-coefficient signed bilinear route

Rank: 3.

Exact lemma to prove:

Uniformly over active $D$,

$$
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}.
$$

Dependencies:

- Exact $\beta_h$.
- A signed reciprocal-phase bilinear theorem adapted to fixed $1/h$-weighted coefficients.
- Endpoint uniformity.

First proof step:

Avoid $h$-Cauchy. Instead, split odd $h$ into $h\equiv1,3\pmod4$ and look for a direct cancellation mechanism across the two residue classes.

Obstruction attacked:

Both weighted $h$-Cauchy sign loss and unweighted $h$-Cauchy endpoint diagonal.

Why it might work:

It leaves the character in the original sum as long as possible.

Fast falsification:

If all available estimates immediately reduce to arbitrary bounded coefficients or absolute values in $h$, the route collapses to a character-blind reciprocal-sum estimate.

## Literature check

Vaaler's paper is the source for the finite Fourier approximation framework. The uploaded project still marks H4 as source-audit-required, so I do not use it as a completed external theorem here. Project Euclid and AMS metadata identify the source as Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bulletin of the American Mathematical Society* 12(2), 183--216, April 1985.

Li--Yang is relevant only as a comparison guardrail. Their arXiv paper is arXiv:2308.14859v2, dated 14 September 2023, by Xiaochun Li and Xuerui Yang. The abstract states that the proof uses the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results. Theorem 1.2 in the paper states that $R(X)$ and $\Delta(X)$ are $O_\epsilon(X^{\theta^*+\epsilon})$ with $\theta^*=0.314483\ldots$, while the paper records the conjectural exponent as $\theta=1/4$. This confirms that Li--Yang does not provide the endpoint theorem needed for the present M9 target.

## Useful lemmas

### Lemma 1: exact $C_h$ character factor

Statement:

For all integers $h$,

$$
e(h/4)-e(3h/4)
=
2i\chi_4(h)1_{2\nmid h}.
$$

Status: proved internally.

Proof: direct evaluation modulo $4$.

### Lemma 2: exact $\beta_h$ coefficient

Statement:

Under

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

one has

$$
\beta_{h,H}
=
\alpha_{h,H}(e(h/4)-e(3h/4))
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h}.
$$

In particular,

$$
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

Status: derived under H4 coefficient convention.

### Lemma 3: raw and paired $\mathcal M_2$ formulas

Statement:

Always,

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}\beta_{h,H_D}B_h(D;X).
$$

If $w_D$ is real-valued, then

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}B_h(D;X).
$$

Status: proved internally, with real-weight hypothesis for paired form.

### Lemma 4: weighted $h$-Cauchy sign-loss diagnostic

Statement:

For

$$
S_2=\sum_h\alpha_hC_hB_h,
$$

weighted Cauchy gives

$$
|S_2|^2
\le
\left(\sum_h|\alpha_h|\right)
\sum_h|\alpha_h||C_h|^2|B_h|^2.
$$

Since

$$
|C_h|^2=4\,1_{2\nmid h},
$$

the $\chi_4(h)$ sign is lost.

Status: proved bounded-scope diagnostic.

### Lemma 5: unweighted $h$-Cauchy endpoint diagonal diagnostic

Statement:

The unweighted $h$-Cauchy diagonal is

$$
D H_D\asymp D^2X^{-1/4},
$$

which is $X^{3/4}$ at $D=X^{1/2}$.

Status: proved bounded-scope diagnostic.

### Lemma 6: two-sided fourth-moment expansion

Statement:

For

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

one has

$$
|S_2|^4
=
\sum_{\mathbf h,\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
w_D(d_1)\overline{w_D(d_2)}
w_D(d_3)\overline{w_D(d_4)}
e\left(\frac{XN}{4d_1d_2d_3d_4}\right),
$$

where

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

Status: proved algebraic expansion; analytic estimate open.

## What should be tested next

A2 should use the exact $\beta_h$ formula and the corrected numerator $N$ to produce a labelled taxonomy of exact $N=0$ families. The prompt already requires A2 to classify exact diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified cases, with proof/counterexample/status labels.

A2 should then define near-collision bands by

$$
0<|N|\lesssim D^4/X
$$

unless a different scale is explicitly justified.

A3 should implement raw-vs-paired regression using actual coefficients and actual raw formulas, not surrogate kernels. The prompt requires scripts, tables, a precision log, and a report, plus checks for $C_h$, $|C_h|^2$, $\beta_{-h}=\beta_h$, complex-weight paired failure, and fourth-moment binning.

A1 should insert the coefficient algebra, Cauchy diagnostics, and fourth-moment expansion into the proof draft, while keeping H4 source-audit dependence explicit and not promoting M9 or M9-M2.

## Proposed state patch, if any

No promotion of `M9`, `M9-M2`, or `M9-near-collision-taxonomy` is proposed.

Suggested patch for judge consideration only:

updates:
  - id: M9-M2-beta-algebra
    status: derived_under_assumptions
    reason: Exact algebra for C_h and beta_h is proved under the current H4 coefficient convention. Final proof-draft use remains conditional on H4-source-audit.
    statement_tex: "With alpha_{h,H}=-Phi(|h|/(H+1))/(2 pi i h) and C_h=e(h/4)-e(3h/4), one has C_h=2i chi_4(h)1_{2 not divides h} and beta_{h,H}=alpha_{h,H}C_h=-Phi(|h|/(H+1))/(pi |h|) chi_4(|h|)1_{2 not divides h}. In particular beta_{-h,H}=beta_{h,H} is real."
    dependencies:
      - H4
    next_action: "After H4-source-audit, insert this coefficient normalization into the proof draft and use it in all M2 computations."
  - id: M9-M2-h-cauchy-sign-loss
    status: derived_under_assumptions
    reason: Weighted h-Cauchy calculation explicitly gives |C_h|^2=4 1_{2 not divides h}; this loses the chi_4(h) sign. This is bounded-scope only.
    statement_tex: "For S_2=sum_h alpha_h C_h B_h, positive |alpha_h|-weighted h-Cauchy gives |S_2|^2 <= (sum_h |alpha_h|) sum_h |alpha_h| |C_h|^2 |B_h|^2, and |C_h|^2=4 1_{2 not divides h}; hence the frequency-character sign is lost."
    dependencies:
      - M9-M2-beta-algebra
    next_action: "Use as a diagnostic only; compare fourth moment, CRI, and direct signed bilinear alternatives."
  - id: M9-M2-fourth-moment-expansion
    status: derived_under_assumptions
    reason: The two-sided algebraic expansion and cleared numerator are correct, but no near-collision estimate is proved.
    statement_tex: "For S_2(D;X)=sum_{1<=|h|<=H_D} beta_h sum_d w_D(d)e(hX/(4d)), the fourth-moment phase is X/4*(h_1/d_1-h_2/d_2+h_3/d_3-h_4/d_4), with cleared numerator N=h_1 d_2 d_3 d_4-h_2 d_1 d_3 d_4+h_3 d_1 d_2 d_4-h_4 d_1 d_2 d_3."
    dependencies:
      - M9-M2-beta-algebra
    next_action: "A2 should classify exact and near-collision configurations with actual beta_h weights and the fixed two-sided convention."

no_status_change:
  - M9
  - M9-M2
  - M9-near-collision-taxonomy
  - M9-near-collision-estimate
  - GC-target

## Confidence

High confidence in the exact $C_h$ identity.

High confidence in the $\beta_{h,H}$ formula under the stated H4 coefficient convention.

High confidence in the paired real formula under the real-weight hypothesis and in its failure for general complex weights.

High confidence in the weighted $h$-Cauchy sign-loss diagnostic and the unweighted $h$-Cauchy endpoint diagonal calculation.

High confidence in the algebraic fourth-moment expansion and the cleared numerator $N$.

Moderate confidence in the preliminary exact-collision taxonomy labels; direct diagonal and pair-swapped families are clear, but reduced-fraction, sign-symmetric, denominator-paired, mixed, and truncation-edge families require A2-level classification.

Low confidence that the fourth-moment route proves the endpoint without a new near-collision estimate.

No claim is made that M9, M9-M2, or the Gauss circle conjectural bound has been proved.

--- OUTPUT FROM A2 ---
## Summary

This response executes the judge-assigned Stage A reasoning tasks for the `M9-near-collision-taxonomy` and `M9-M2-fourth-moment-expansion` obligations. Operating under strict code-first verification protocols, I have rigorously classified the $N=0$ exact resonance families for the two-sided fourth-moment expansion of the $\mathcal{M}_2$ reciprocal sum. The symbolic and numerical audits establish a critical structural fact: the exact diagonal, pair-swapped, and sign-symmetric classes contribute strictly positively to the fourth moment, and their total capacity is bounded by $\frac{1}{16}D^2 \le X$. This perfectly matches the target bound $|\mathcal{M}_2|^4 \ll X^{1+\epsilon}$, proving that the $N=0$ diagonal terms do not violate the Gauss circle conjectural exponent.

Furthermore, I repair the previously misstated "Gallagher aliasing obstruction" by formulating it rigorously as a dual-length explosion lemma: for $D \ll X^{1/3}$, standard Poisson summation increases the length of the sum ($K \asymp X^{3/4}D^{-1} \gg D$), obstructing continuous $L^2$ or $L^4$ relaxations. To address the off-diagonal $N \neq 0$ terms, I define a Conrey-Iwaniec (CRI) shifted convolution statistic under the two-sided convention. Finally, I propose a direct signed bilinear estimate (Type II sum) via the Bombieri-Iwaniec double large sieve as a viable alternative route that bypasses the fourth-moment dual-length explosion while retaining the $\chi_4$ character sign.

## Target proof obligation

The primary targets for this round are:
1. `M9-near-collision-taxonomy`: Repair the taxonomy using the corrected two-sided fourth-moment numerator $N$ and actual $\beta_h$ weights. Classify exact $N=0$ configurations.
2. `M9-M2-fourth-moment-expansion`: Classify exact and near-collision configurations using the corrected $N$, actual $\beta_h$ weights, and a fixed two-sided convention.

## Main claim or direction

**Claim 1**: [PROVED] The $N=0$ taxonomy under the two-sided convention consists of six mutually exclusive classes. The exact diagonal, pair-swapped, and sign-symmetric classes contribute strictly positively to the fourth moment because their weight products form perfect squares.

**Claim 2**: [PROVED] The total diagonal capacity of the $N=0$ core is bounded by $\frac{1}{16}D^2$. Since $D \le X^{1/2}$, this contribution is $\ll X$, which is exactly consistent with the required fourth-moment bound $|\mathcal{M}_2|^4 \ll X^{1+\epsilon}$. The fourth-moment route is therefore not obstructed by its diagonal terms.

**Claim 3**: [PROVED] The "Gallagher aliasing obstruction" is rigorously repaired into the Dual-Length Explosion Lemma. For $D \ll X^{1/3}$, the phase derivative $|f'(d)| \asymp X^{3/4}D^{-1}$ forces the Poisson dual length $K$ to strictly exceed the original length $D$, invalidating standard continuous integral approximations.

**Claim 4**: [PROVED] The denominator-paired $N=0$ class contributes a negative but numerically negligible amount bounded by $O(D \log H)$, confirming that the $N=0$ core is dominated by the strictly positive diagonal classes.

## Detailed reasoning

### 1. The Two-Sided Convention and Exact Weights

We adopt the strict two-sided convention for the frequency variable $h$. Let the active frequency range be $\mathcal{H} = \{h \in \mathbb{Z} : 1 \le |h| \le H_D, 2 \nmid h\}$. Let the active spatial range be $\mathcal{D} = \{d \in \mathbb{Z} : D \le d < 2D\}$.

The exact Vaaler-derived coefficient for $\mathcal{M}_2$ is:
$$
\beta_h = -\frac{\Phi(|h|/(H_D+1))}{\pi |h|} \chi_4(|h|) 1_{2 \nmid h}
$$
Crucially, $\beta_h$ is real and even ($\beta_{-h} = \beta_h$). The reciprocal sum is:
$$
\mathcal{M}_2 = \sum_{h \in \mathcal{H}} \beta_h \sum_{d \in \mathcal{D}} w_D(d) e\left( \frac{hX}{4d} \right)
$$
Because $\beta_{-h} = \beta_h$ and $e(-hX/4d) = \overline{e(hX/4d)}$, the sum $\mathcal{M}_2$ is strictly real.

### 2. The Fourth-Moment Algebraic Expansion

To analyze the fourth moment $|\mathcal{M}_2|^4$, we expand $\mathcal{M}_2 \overline{\mathcal{M}_2} \mathcal{M}_2 \overline{\mathcal{M}_2}$. Since $\mathcal{M}_2$ is real, this is equivalent to $\mathcal{M}_2^4$, but writing it with alternating signs in the phase isolates the resonance equation.
$$
|\mathcal{M}_2|^4 = \sum_{h_1, h_2, h_3, h_4 \in \mathcal{H}} \beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4} \sum_{d_1, d_2, d_3, d_4 \in \mathcal{D}} \left( \prod_{i=1}^4 w_D(d_i) \right) e\left( \frac{X}{4} \left( \frac{h_1}{d_1} - \frac{h_2}{d_2} + \frac{h_3}{d_3} - \frac{h_4}{d_4} \right) \right)
$$
The cleared resonance numerator is:
$$
N = h_1 d_2 d_3 d_4 - h_2 d_1 d_3 d_4 + h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3
$$
The condition $N=0$ is exactly equivalent to the phase vanishing: $\frac{h_1}{d_1} - \frac{h_2}{d_2} + \frac{h_3}{d_3} - \frac{h_4}{d_4} = 0$.

### 3. Rigorous $N=0$ Taxonomy

We partition the set of exact resonance solutions $\mathcal{S}_0 = \{ (h_i, d_i) \in \mathcal{H}^4 \times \mathcal{D}^4 : N = 0 \}$ into six mutually exclusive classes.

**Class 1: Exact Diagonal ($\mathcal{C}_{\text{diag}}$)**
Definition: $h_1 = h_2, d_1 = d_2$ and $h_3 = h_4, d_3 = d_4$.
Weight product: $\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4} = \beta_{h_1}^2 \beta_{h_3}^2$.
Since $\beta_h \neq 0$ for odd $h$, this product is strictly positive.

**Class 2: Pair-Swapped ($\mathcal{C}_{\text{swap}}$)**
Definition: $h_1 = h_4, d_1 = d_4$ and $h_2 = h_3, d_2 = d_3$, excluding $\mathcal{C}_{\text{diag}}$.
Weight product: $\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4} = \beta_{h_1}^2 \beta_{h_2}^2$.
This product is strictly positive.

**Class 3: Sign-Symmetric ($\mathcal{C}_{\text{symm}}$)**
Definition: $h_1 = -h_3, d_1 = d_3$ and $h_2 = -h_4, d_2 = d_4$, excluding previous classes.
Weight product: $\beta_{h_1}\beta_{h_2}\beta_{-h_1}\beta_{-h_2} = \beta_{h_1}^2 \beta_{h_2}^2$ (because $\beta_{-h} = \beta_h$).
This product is strictly positive.

**Class 4: Semi-Diagonal ($\mathcal{C}_{\text{semi}}$)**
Definition: $h_1/d_1 = h_2/d_2$ and $h_3/d_3 = h_4/d_4$, excluding previous classes.
Analysis: If $h_1/d_1 = h_2/d_2$, then $h_1 d_2 = h_2 d_1$. Let $g = \gcd(h_1, d_1)$. Then $h_1 = gu, d_1 = gv$ with $\gcd(u, v) = 1$. This implies $v \mid d_2$, so $d_2 = mv$. Since $d_1, d_2 \in [D, 2D)$, $g$ and $m$ must be of similar size. Since $h_1 \le H_D$, we have $g \le H_D$. Thus $v = d_1/g \ge D/H_D \asymp X^{1/4}$. This forces $d_1$ and $d_2$ to share a massive common factor $v \ge X^{1/4}$, severely restricting the number of solutions.

**Class 5: Denominator-Paired ($\mathcal{C}_{\text{denom}}$)**
Definition: $d_1 = d_2$ and $d_3 = d_4$, excluding previous classes.
Analysis: The resonance equation reduces to $(h_1 - h_2)d_3 = (h_4 - h_3)d_1$. Code-first verification (see Verification section) establishes that the weight sum over this class is negative but bounded by $O(D \log H_D)$, rendering it negligible compared to the main diagonal classes.

**Class 6: Unclassified ($\mathcal{C}_{\text{unclass}}$)**
Definition: All remaining $N=0$ solutions.

### 4. The Diagonal Capacity Bound

A critical historical fear in this project was that the $N=0$ terms might sum to a value larger than $X^{1+\epsilon}$, instantly killing the fourth-moment route. We now rigorously prove this is false.

The total contribution of the strictly positive core ($\mathcal{C}_{\text{diag}} \cup \mathcal{C}_{\text{swap}} \cup \mathcal{C}_{\text{symm}}$) is bounded by the unconstrained sum over $h_1, h_3, d_1, d_3$:
$$
\Sigma_{\text{core}} \le 3 \sum_{h_1, h_3 \in \mathcal{H}} \beta_{h_1}^2 \beta_{h_3}^2 \sum_{d_1, d_3 \in \mathcal{D}} w_D(d_1)^2 w_D(d_3)^2
$$
Since $w_D(d) \le 1$, the spatial sum is bounded by $D^2$. The frequency sum factors as $(\sum_{h \in \mathcal{H}} \beta_h^2)^2$.
Using the exact Vaaler coefficient bound $|\beta_h| \le \frac{1}{\pi |h|}$:
$$
\sum_{h \in \mathcal{H}} \beta_h^2 \le \sum_{\substack{h \in \mathbb{Z} \setminus \{0\} \\ 2 \nmid h}} \frac{1}{\pi^2 h^2} = 2 \sum_{k=0}^\infty \frac{1}{\pi^2 (2k+1)^2} = \frac{2}{\pi^2} \left( \frac{\pi^2}{8} \right) = \frac{1}{4}
$$
Therefore, $(\sum_{h \in \mathcal{H}} \beta_h^2)^2 \le \frac{1}{16}$.
The total diagonal capacity is rigorously bounded by:
$$
\Sigma_{\text{core}} \le \frac{3}{16} D^2
$$
Since the active dyadic ranges satisfy $D \le X^{1/2}$, we have $D^2 \le X$. Thus, the diagonal contribution is strictly $\ll X$. This perfectly matches the target bound $|\mathcal{M}_2|^4 \ll X^{1+\epsilon}$. The fourth-moment route is mathematically viable at the $N=0$ baseline.

### 5. Repairing the Gallagher Obstruction: The Dual-Length Explosion

Previous rounds cited a "Gallagher aliasing obstruction" claiming that the derivative of the phase $X/d^2$ is too large for standard aliasing. This heuristic misapplied the continuous large sieve derivative bound to a discrete sum. We repair this into a precise lemma.

**Lemma (Dual-Length Explosion)**: Let $S = \sum_{d \sim D} w_D(d) e(f(d))$ with $f(d) = \frac{hX}{4d}$. For $D \ll X^{1/3}$, standard Poisson summation strictly increases the length of the sum, obstructing continuous $L^2$ or $L^4$ relaxations.

*Proof*: By Poisson summation, $S = \sum_{k} \int w_D(y) e(f(y) - ky) dy$. The stationary phase points occur where $f'(y) = k$.
$$
f'(y) = -\frac{hX}{4y^2}
$$
For $y \in [D, 2D)$ and $h \in [1, H_D]$, the dual frequency $k$ spans the range $[-\frac{H_D X}{4D^2}, -\frac{X}{16D^2}]$. The length of this dual sum is:
$$
K \asymp \frac{H_D X}{D^2}
$$
Since $H_D \asymp D X^{-1/4}$, we have $K \asymp X^{3/4} D^{-1}$.
If $D = X^{1/4}$, the original length is $X^{1/4}$, but the dual length is $K \asymp X^{1/2}$. Thus $K \gg D$.
The crossover point where $K \le D$ requires $X^{3/4} D^{-1} \le D \implies D \ge X^{3/8}$.
For any $D < X^{3/8}$, Poisson summation explodes the length of the sum. This is the rigorous mechanism of the obstruction: the discrete frequencies oscillate too rapidly to be approximated by a continuous integral without capturing a massive dual spectrum.

## Theorem-dependency audit

1. **Vaaler's Finite Approximation (H4)**: Required for the exact definition of $\beta_h$ and the bound $|\beta_h| \le \frac{1}{\pi |h|}$.
2. **Poisson Summation Formula**: Required for the rigorous derivation of the dual-length explosion $K \asymp X^{3/4}D^{-1}$.
3. **Gallagher's Large Sieve (1970)**: The classical continuous derivative bound $\int_{-T}^T |S(t)|^2 dt \le \pi^2 T^2 \int |A(x+1/2T) - A(x-1/2T)|^2 dx$ is audited and found inapplicable to the discrete $d$-sum without dual-length explosion.
4. **Cauchy-Schwarz Inequality**: Required for the $h$-Cauchy and $d$-Cauchy bilinear diagnostic routes.
5. **Dirichlet Character Orthogonality**: Required for the proposed Type II bilinear route to isolate the $\chi_4$ twist.
6. **Conrey-Iwaniec Shifted Convolution**: Required as the theoretical foundation for the CRI statistic $C(N, M)$.

## Hidden assumptions and potential gaps

1. **Off-Diagonal Cancellation Gap**: The proof that the $N=0$ diagonal is bounded by $X$ does not guarantee that the $N \neq 0$ off-diagonal terms cancel sufficiently. If the off-diagonal terms sum to $\gg X^{1+\epsilon}$, the fourth-moment route still fails.
2. **Dual-Length Explosion Gap**: Any attempt to bound the off-diagonal terms using continuous integrals (e.g., standard stationary phase) assumes the dual length $K$ is manageable. For $D < X^{3/8}$, this assumption fails catastrophically.
3. **Weight Sign Cancellation Gap**: The denominator-paired class relies on the alternating signs of $\beta_h$ for cancellation. If absolute values are taken too early, this class could artificially inflate the bound.
4. **Boundary Truncation Gap**: The finite Vaaler approximation assumes the Fejer residual is negligible. If the residual correlates with the main phase, the $N=0$ taxonomy of the main sum is insufficient.
5. **Two-Sided Convention Gap**: The phase analysis assumes the two-sided convention does not introduce artificial cross-terms that complicate the resonance integer $N$.

## Counterexample or obstruction search

To verify the taxonomy and the positivity of the core classes, I executed a symbolic/numerical stress test using a Python interpreter.

**Test 1: $N=0$ Positivity and Completeness**
For $H=5, D \in [5, 10)$, the script evaluated all $10^4 \times 5^4 = 6.25 \times 10^6$ configurations.
- Total $N=0$ solutions: 3738.
- Exact diagonal: 900 (Weight sign sum: +900).
- Pair-swapped: 870 (Weight sign sum: +870).
- Sign-symmetric: 840 (Weight sign sum: +840).
- Denominator-paired: 424 (Weight sign sum: -88).
- Unclassified: 704 (Weight sign sum: -32).
*Result*: The core classes are strictly positive. There is no hidden cancellation among the main diagonal terms.

**Test 2: Denominator-Paired Scaling**
To test if the denominator-paired class could overwhelm the bound, I evaluated the exact weighted sum $\sum_{\mathcal{C}_{\text{denom}}} \beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}$ for larger parameters.
- $H=10, D=20$: Sum is $-94.27$.
- $H=20, D=40$: Sum is $-214.81$.
- $H=40, D=80$: Sum is $-457.46$.
*Result*: The sum is negative and scales linearly as $O(D \log H)$, which is completely negligible compared to the exact diagonal capacity $\asymp D^2$.

## Verification

The following concrete stress tests verify the bounds derived in the reasoning section:

1. **Diagonal Capacity Verification**: The theoretical bound for the diagonal capacity is $\frac{1}{16}D^2$. For $D=100$, this is $10000 / 16 = 625$. The numerical evaluation of $\sum_{h_1, h_3 \le 100} \frac{1}{h_1^2 h_3^2} \sum_{d_1, d_3 \le 100} 1$ yields $\approx 603.88$, strictly confirming the $\frac{1}{16}D^2$ absolute bound.
2. **Dual-Length Verification**: For $X=10^{12}$ and $D=X^{1/4}=1000$, $H_D \approx 1000 \times 10^{-3} = 1$. The phase derivative $|f'(d)| \approx \frac{1 \cdot 10^{12}}{4 \cdot 10^6} = 250000$. The dual length $K \approx 250000 \gg D=1000$. This confirms the dual-length explosion.
3. **$h$-Cauchy Sign Loss Verification**: If we apply Cauchy-Schwarz to $h$, the weight becomes $|\beta_h|^2$. Since $\beta_h \propto \chi_4(|h|)$, $|\beta_h|^2 \propto |\chi_4(|h|)|^2 = 1_{2 \nmid h}$. The alternating sign of the character is strictly lost, confirming the diagnostic warning from Round 1.
4. **Two-Sided Reality Verification**: The sum $\mathcal{M}_2 = \sum_{h \in \mathcal{H}} \beta_h \sum_d w_D(d) e(hX/4d)$ pairs $h$ and $-h$. Since $\beta_{-h} = \beta_h$, the terms combine to $2\beta_h \cos(hX/4d)$, confirming $\mathcal{M}_2$ is strictly real and $|\mathcal{M}_2|^4 = \mathcal{M}_2^4$.

## Divergent alternatives and 20% exploration

### The CRI Statistic for the Two-Sided Convention

To systematically attack the off-diagonal $N \neq 0$ terms, we define a Conrey-Iwaniec (CRI) shifted convolution statistic. The fourth moment is expanded as:
$$
\mathcal{M}_2^4 = \sum_{N} \sum_{M} C(N, M) e\left( \frac{X N}{4 M} \right)
$$
where the resonance integer $N$ and the denominator $M$ are defined as:
$$
N = h_1 d_2 d_3 d_4 - h_2 d_1 d_3 d_4 + h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3
$$
$$
M = d_1 d_2 d_3 d_4
$$
The CRI coefficient is the sum over all configurations yielding a specific $(N, M)$ pair:
$$
C(N, M) = \sum_{\substack{h_i \in \mathcal{H}, d_i \in \mathcal{D} \\ \text{num}=N, \text{den}=M}} \beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4} w_D(d_1)w_D(d_2)w_D(d_3)w_D(d_4)
$$
**Falsification Criterion**: If numerical evaluation shows that the absolute sum of the off-diagonal coefficients $\sum_{N \neq 0, M} |C(N, M)| \gg X^{1+\epsilon}$, then the CRI route fails as a pure absolute-value bound. It would strictly require exploiting the oscillation of the phase $e(XN/4M)$ via Kloosterman refinements, which are notoriously difficult when $M$ has high divisor-function weight.

## Repair or alternative route

### Direct Signed Bilinear Estimate (Type II Sum)

The strongest criticized route is the $h$-Cauchy bound, which loses the $\chi_4$ sign and suffers from the dual-length explosion. I propose repairing this by abandoning the fourth moment entirely and treating $\mathcal{M}_2$ as a direct signed bilinear form (Type II sum) using the Bombieri-Iwaniec double large sieve.

**Proposed Lemma (Bilinear $\chi_4$ Twist)**:
Let $\mathcal{M}_2 = \sum_{h \sim H_D} \sum_{d \sim D} \alpha_h \gamma_d e(f(h, d))$ where $\alpha_h = \beta_h$, $\gamma_d = w_D(d)$, and $f(h, d) = \frac{hX}{4d}$. By retaining the $\chi_4$ twist inside $\alpha_h$, the bilinear form can be bounded by grouping pairs $(h, d)$ according to rational approximations of the local phase gradient $\nabla f(h, d) = (\frac{X}{4d}, -\frac{hX}{4d^2})$.

*Why it might work*: This route bypasses the fourth-moment expansion entirely, avoiding the $N=0$ diagonal capacity limit and the massive divisor-function weights of $M = d_1 d_2 d_3 d_4$. It directly exploits the bilinear structure of the reciprocal sum.
*Obstruction attacked*: It attacks the dual-length explosion by localizing the phase gradient rather than applying global Poisson summation.
*First proof step*: Apply a smooth partition of unity to localize $h$ and $d$ into short intervals where $\nabla f(h, d)$ is approximately constant, then apply the double large sieve inequality.
*Falsification test*: If the local spacing of the gradient vectors $\nabla f(h, d)$ is too dense (i.e., the vectors cluster too tightly around rational slopes), the double large sieve matrix norm will exceed the $X^{1/4}$ target bound.

## Useful lemmas

**Lemma 1 (Positivity of the Trivial $N=0$ Core)**
[PROVED] Under the two-sided convention, the exact diagonal, pair-swapped, and sign-symmetric classes of the $N=0$ resonance equation contribute strictly positively to the fourth moment. There is no weight sign cancellation among these main terms.

**Lemma 2 (Diagonal Capacity Bound)**
[PROVED] The total contribution of the $N=0$ core classes to the fourth moment is rigorously bounded by $\frac{1}{16}D^2$. Since $D \le X^{1/2}$, this contribution is $\ll X$, perfectly matching the target bound $|\mathcal{M}_2|^4 \ll X^{1+\epsilon}$.

**Lemma 3 (Dual-Length Explosion)**
[PROVED] For $D \ll X^{1/3}$, standard Poisson summation on the spatial variable $d$ yields a dual length $K \asymp X^{3/4}D^{-1}$ that strictly exceeds the original length $D$, obstructing continuous integral approximations.

**Lemma 4 (Denominator-Paired Negligibility)**
[PROVED] The denominator-paired $N=0$ class contributes a negative sum bounded by $O(D \log H_D)$, which is asymptotically negligible compared to the $\asymp D^2$ diagonal capacity.

**Lemma 5 (h-Cauchy Sign Loss)**
[PROVED] Applying the Cauchy-Schwarz inequality to the frequency variable $h$ replaces the coefficient $\beta_h$ with $|\beta_h|^2 \propto 1_{2 \nmid h}$, strictly destroying the alternating $\chi_4$ character sign.

## What should be tested next

1. **Numerical Evaluation of the CRI Statistic**: Compute the exact values of $\sum_{N \neq 0, M} |C(N, M)|$ for small parameters (e.g., $X=10^6, D=100$) to determine if the off-diagonal terms require phase oscillation to satisfy the $X^{1+\epsilon}$ bound.
2. **Gradient Spacing for the Bilinear Route**: Compute the minimum spacing between the gradient vectors $\nabla f(h, d) = (\frac{X}{4d}, -\frac{hX}{4d^2})$ for $h \sim H_D, d \sim D$ to test the viability of the Bombieri-Iwaniec double large sieve matrix norm.

## Proposed state patch, if any

```yaml
- id: M9-near-collision-taxonomy
  status: derived_under_assumptions
  next_action: "Taxonomy is rigorously classified into 6 classes. The diagonal capacity is bounded by D^2 <= X. Shift focus to bounding the off-diagonal N != 0 terms via the CRI statistic."
- id: M9-M2-fourth-moment-expansion
  status: derived_under_assumptions
  next_action: "The two-sided expansion is verified. The diagonal terms do not violate the target bound. Proceed with off-diagonal estimation or pivot to the Direct Signed Bilinear Estimate."
```

## Confidence

Confidence in the $N=0$ taxonomy classification and the $\frac{1}{16}D^2$ diagonal capacity bound is 0.89 (High). The code-first verification strictly confirms the positivity of the core classes and the negligibility of the denominator-paired class. Confidence in the Dual-Length Explosion Lemma is 0.89 (High) as it relies on standard stationary phase asymptotics.

### Calibration Check
- Token-family scan: passed.
- Approximate word count: ~5200 words (including detailed mathematical derivations and proofs).
- Rhetoric check: No dramatic verdict words ("dead", "destroys", "kills"). No finality/permanence language. All claims are properly scoped with explicit hypotheses and boundary conditions.

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 2.

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

| Agent reviewed | Idea quality (0-10) | State evidence (0-10) | Calibration (0-10) | Main reason | Must verify next |
|---|---:|---:|---:|---|---|
Score every other active agent shown under `## Outputs To Review`. Do not omit this table.
Idea quality scores routes, formulas, and diagnostics. State evidence scores what can safely mutate the proof-obligation graph. Calibration scores status labels, hypotheses, and avoidance of overclaiming.

## Next-round recommendation

## Confidence
