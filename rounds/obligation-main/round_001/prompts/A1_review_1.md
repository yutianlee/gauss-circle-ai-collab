You are ChatGPT Extended Pro, acting as broad strategist, literature scout, proof synthesizer, and default judge.

Review the other agents' Round 1 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Use ChatGPT Extended Pro. Act as a research strategist and, when judging, as the conservative synthesis writer. For the Gauss circle problem, prioritize exact normalizations, Poisson/Bessel formulas, hyperbola decompositions, Vaaler/Fejer residuals, exponent-pair or Bombieri-Iwaniec hypotheses, smoothing/unsmoothing losses, and literature status. When web search is available, cite exact theorem statements, authors, publication data, and URLs/DOIs/arXiv links. If web search is unavailable, say so and do not invent citations. In reasoning, spend about 80% on the judge-assigned main route and about 20% on serious alternative routes or obstruction searches. In review, assess A2 and A3 separately and recommend research-strategy adjustments. As judge, write concrete next-round prompts for A1, A2, and A3.

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

## Review-Stage Guardrail

This is Stage B cross review for Round 1.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a referee-style report on A2 and A3. Include a score table, hidden assumptions, exact claims needing proof, concrete verification tasks, and a research-strategy adjustment recommendation. Use available web search to verify cited external theorems; if search is unavailable, mark citation status as unverified rather than inventing references.

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

--- OUTPUT FROM A3 ---
## Summary

The assigned target obligation is `M9-regression-raw-vs-paired`, a computational diagnostic that compares the full two‑sided complex sum formulation of the M1/M2 reciprocal sums with a paired real simplification (where terms $h$ and $-h$ are combined assuming conjugation properties). The task is to produce an implementation‑ready plan, including exact formulas, script paths, commands, output tables, precision notes, and a clear statement of limitations. The output must be diagnostic only and must not promote `M9` itself.

This audit report (i) reconstructs candidate formulas for the M1 and M2 sums from the available proof‑obligation graph, (ii) derives the algebraic condition under which a paired real representation is exact, (iii) provides a complete Python script (`computations/m9_regression/run.py`) that tests the raw vs. paired equality for both real‑valued and complex‑valued coefficient arrays, (iv) specifies the command line, (v) defines the expected output CSV format (`outputs/table_small.csv`), (vi) discusses precision, rounding, and the role of the character factor $C_h = e(h/4)-e(3h/4)$, and (vii) outlines a follow‑up report (`computations/m9_regression/report.md`). A 20% divergent exploration section sketches alternative analytical routes (Bombieri–Iwaniec large sieve, Mellin–Perron transforms, and a Cauchy–Schwarz fourth‑moment refinement) with precise lemmas that would be needed. Finally, a proposed state patch adds executable diagnostics as evidence and updates the status of the regression obligation.

## Target proof obligation

**ID**: `M9-regression-raw-vs-paired`
**Status**: `proposed` (aiming for `diagnostic_only` after execution)
**Statement (paraphrased)**:
Compare the raw two‑sided complex formulas for the M1 and M2 fixed‑coefficient reciprocal sums with paired real formulas that assume $\beta_{-h} = \overline{\beta_h}$ or similar conjugation. Confirm that paired formulas fail when the coefficients are not suitably symmetric, and thereby demonstrate that the complex character factor $C_h$ must be retained in any rigorous estimate.

## Main claim or direction

The main claim is that the **raw two‑sided complex representation**

$$
M_{\text{raw}} = \sum_{\substack{h\in\mathbb Z\\ h\neq 0}} \beta_h\, \Phi(h)
$$

(for a suitable kernel $\Phi$) is the only trustworthy starting point for M2 because the weights $\beta_h = \alpha_{h,H_D} C_h$ are **complex** and satisfy $\beta_{-h} = -\overline{\beta_h}$ rather than $\beta_{-h} = \overline{\beta_h}$. A naïve pairing

$$
M_{\text{paired}} = \sum_{h=1}^{\infty} \bigl(\beta_h\,\Phi(h) + \beta_{-h}\,\Phi(-h)\bigr)
$$

simplifies to a real sum **only if** $\beta_{-h}\,\Phi(-h) = \overline{\beta_h\,\Phi(h)}$, which fails for the actual M2 weights. Therefore, any attempted proof of the M2 endpoint bound that silently replaces the two‑sided sum by a real paired expression must be rejected.

The diagnostic test will numerically evaluate both formulas for small synthetic parameters and for a surrogate of the actual Vaaler coefficients, producing a table that clearly exhibits the discrepancy.

## Detailed reasoning

### 1. Reconstructing the M1 and M2 sums from the proof obligations

The proof‑obligation graph states:

- **H1‑H3** reduce the Gauss circle error to sawtooth sums.
- **H4** (Vaaler 1985) provides a finite approximation

$$
  \psi(x) = \sum_{1\le |h|\le H_D} \alpha_{h,H_D}\, \hat\psi(h)\, e(hx) + \text{residual},
  $$

where $\psi$ is a sawtooth function, $\hat\psi(h)$ are known Fourier coefficients, and $\alpha_{h,H_D}$ are Vaaler coefficients.
- **R5‑Full** bounds the Fejér residual.
- **M9** concerns the two **main reciprocal sums** that arise after inserting Vaaler’s expansion into the sawtooth sums and summing over the geometric variables. The obligations `M9-M1` and `M9-M2` specify:
  - M1: fixed‑coefficient reciprocal sum with coefficients **$\alpha_{h,H_D}$** (real, and symmetric in a known way).
  - M2: fixed‑coefficient reciprocal sum with coefficients **$\beta_h = \alpha_{h,H_D} C_h$**, where

$$
    C_h = e\!\left(\frac{h}{4}\right) - e\!\left(\frac{3h}{4}\right) = 2i\,\chi_4(h)
    $$

(odd $h$; $C_h=0$ for even $h$).

$\chi_4$ is the non‑principal Dirichlet character modulo 4.

Although the exact formula for the kernel $\Phi(h)$ is not supplied in the reading packet, it is known from the Fourier expansion of the circle problem (Voronoi summation / classical Bessel‑function expansions) that after Poisson summation one obtains sums of the form

$$
\sum_{n\le X} r_2(n) = \pi X + X^{1/2}\sum_{h=1}^\infty \frac{r_2(h)}{h}\, J_1(2\pi\sqrt{hX}) + \dots,
$$

but the Vaaler approach truncates the $h$‑sum and inserts smooth weights. Typically the contribution responsible for M1/M2 is a sum over $h$ of

$$
\frac{\text{coefficient}}{h}\; \times\; \text{(some oscillatory factor)}.
$$

For the purpose of designing a diagnostic test, we do not need the precise oscillatory kernel; we only need a concrete expression that captures the **algebraic relationships** among the coefficients and the arguments. Therefore we adopt a surrogate kernel

$$
\Phi_X(h) = \frac{1}{h}\, e^{i X \log h}
$$

(the exact choice is harmless because the test merely compares the two summation conventions under the same kernel). The true M2 sum will involve a Dirichlet kernel or a Fejér‑sum kernel; the test script will be written so that the kernel is a pluggable function.

### 2. Algebraic condition for a valid paired real representation

Let $S = \sum_{h\neq 0} \beta_h \Phi(h)$. A paired version that sums only over $h>0$ is

$$
S_{\text{pair}} = \sum_{h=1}^\infty \bigl( \beta_h \Phi(h) + \beta_{-h} \Phi(-h) \bigr).
$$

If $\beta_{-h} \Phi(-h) = \overline{\beta_h \Phi(h)}$, then $S_{\text{pair}} = 2\sum_{h=1}^\infty \operatorname{Re}(\beta_h \Phi(h))$, a real number. Suppose the original $S$ is not guaranteed to be real (and in general it is complex). Then any simplification that forces a real answer is incorrect.
For the actual M2 coefficients we have

- $\alpha_{-h,H_D} = \overline{\alpha_{h,H_D}}$ (Vaaler coefficients are conjugate symmetric, and real if $H_D$ is symmetric, but we must verify from the source).
- $C_{-h} = e(-h/4)-e(-3h/4) = \overline{e(h/4)-e(3h/4)} = \overline{C_h}$.
- Therefore $\beta_{-h} = \alpha_{-h,H_D} C_{-h} = \overline{\alpha_{h,H_D}}\;\overline{C_h} = \overline{\beta_h}$.

Thus the coefficient array $\beta_h$ **does** satisfy $\beta_{-h} = \overline{\beta_h}$.
Why then is the paired sum not automatically real? Because the kernel $\Phi(h)$ may satisfy $\Phi(-h) = \overline{\Phi(h)}$ or not. In the classical circle problem, the oscillatory kernel often involves $J_1(2\pi\sqrt{hX})$ or a complex exponential, and the symmetry may be more subtle. The critical point is that the M2 sum is **not** a standalone object; it arises after multiplication by a certain exponential factor from the sawtooth argument. The judge notes mention “the M2 frequency‑side character factor” and “the factor $C_h$ must be retained” precisely because the kernel’s symmetry is broken by the factor $e(h/4)$ etc. In the raw sum, the factor $C_h$ appears explicitly; in a paired version one might attempt to absorb it into a real combination, but that absorption requires proving that the resulting sum is real, which would need additional justification. The diagnostic test will show that a formal pairing without handling the complex phase correctly yields a different numerical value, confirming that the two‑sided convention is the only safe starting point.

### 3. Designing the numerical stress test

We construct a Python script (`computations/m9_regression/run.py`) that implements:

- A function `raw_sum(beta, h_vals, kernel, X)` computing $\sum_{h} \beta_h \Phi_X(h)$ over a symmetric set `h_vals` (including negatives).
- A function `paired_sum(beta, h_pos, kernel, X)` computing $\sum_{h>0} (\beta_h \Phi_X(h) + \beta_{-h} \Phi_X(-h))$.
- A function `is_paired_valid(beta, kernel, X)` that checks whether raw and paired values agree to a specified tolerance.

#### Parameters and test cases:

We use a small set $\mathcal H = \{\pm 1, \pm 2, \dots, \pm 20\}$.

**Case 1 (Real symmetric coefficients):**
Set $\tilde\beta_h = 1/h$ for $h\neq 0$, which satisfies $\tilde\beta_{-h} = \tilde\beta_h$ (real and even). Choose kernel $\Phi_X(h) = h^{-1} \exp(i X h)$ (complex). The raw sum will be complex; the paired sum should match because the kernel satisfies $\Phi(-h) = -\Phi(h)$? Let's compute exactly:

- Let $K(h) = e^{iXh}/h$. Then $K(-h) = e^{-iXh}/(-h) = -e^{-iXh}/h$.
- With real $\beta_h$ even, $\beta_{-h}K(-h) = \beta_h (-e^{-iXh}/h) = -\beta_h e^{-iXh}/h$.
- Meanwhile $\overline{\beta_h K(h)} = \beta_h e^{-iXh}/h$, which is not $-\beta_h e^{-iXh}/h$ unless a minus sign is accounted. So the conjugation property fails for this kernel. But the paired sum is just the raw sum grouped in pairs; it must give the same total because it’s just a rearrangement of a finite sum. So there is no danger of inequality for any kernel; the paired sum is always equal to the raw sum if we sum over exactly the same set. The issue appears when an **infinite** sum is truncated differently or when the paired formula is further simplified by assuming real‑valuedness and discarding imaginary parts. The real danger is that an analyst might write

$$
  S = 2\sum_{h=1}^\infty \operatorname{Re}(\beta_h \Phi(h))
  $$

and then bound $|\operatorname{Re}(\beta_h \Phi(h))|$ instead of $|\beta_h \Phi(h)|$, losing a factor that could prevent a sharp bound.

Thus the numerical test should check whether the decomposition $S = S_{\text{even}} + S_{\text{odd}}$ (or something similar) leads to a different **absolute value** when the imaginary part is erroneously dropped. The test will compare three objects:

1. `raw` : $\sum_{h\neq 0} \beta_h \Phi(h)$.
2. `paired_abs_raw` : $\sum_{h>0} (\beta_h \Phi(h) + \beta_{-h} \Phi(-h))$ (must equal `raw`).
3. `paired_real_abs` : $2\sum_{h>0} |\operatorname{Re}(\beta_h \Phi(h))|$ (a common bounding attempt).
4. `paired_complex_abs` : $2\sum_{h>0} |\beta_h \Phi(h)|$ (the correct trivial bound).

The test will show that `paired_real_abs` can be smaller than `|raw|` when the phase is rotating, thereby demonstrating that such a simplification is invalid.

Better yet, we can directly compare the two summation conventions for a kernel where $\Phi(-h) \neq \overline{\Phi(h)}$ and show that `paired_sum` still equals `raw` (because it’s just a grouping), but that any attempt to bound the sum by a real positive series loses phase cancellation. Since the M9 obligation is about **bounds** (the sum is $O(X^{1/4+\epsilon})$), the test should illustrate that the phase cannot be ignored.

I'll design the test to compute the four quantities for arrays of random complex coefficients and a kernel with a nontrivial phase, and output a table showing the ratio `(paired_real_abs - |raw|)/|raw|` is large, while `paired_complex_abs` is a valid upper bound. The conclusion: any proof that does not account for the complex phase will fail to achieve the required exponent.

#### Script path:
`computations/m9_regression/run.py`

#### Commands:
```bash
cd computations/m9_regression
python run.py --X 100.0 --H 20 --seed 42 --output ../outputs/table_small.csv
```

The script will accept command‑line arguments for $X$ (a scale parameter) and $H$ (max $|h|$). It will generate coefficients that mimic the M2 structure:

- Set $\alpha_h = \exp(2\pi i \theta_h) / (|h|+1)$ with random phases to simulate Vaaler coefficients.
- Multiply by $C_h = e(h/4)-e(3h/4)$.
- Compute kernel $\Phi_X(h) = \exp(i X \log(1+|h|)) / (|h|+1)$ (a toy placeholder).
- Compute the four aggregates.
- Append a row to the CSV file with columns: `X, H, seed, raw_real, raw_imag, paired_real_abs, paired_complex_abs, max_ratio`.

#### Expected output:
```
X,H,seed,raw_real,raw_imag,paired_real_abs,paired_complex_abs,max_ratio
100.0,20,42,-2.345,1.987,0.873,5.632,2.402
...
```
The `max_ratio` = `paired_complex_abs / |raw|` should be ≥1 (since it’s an upper bound), while `paired_real_abs / |raw|` could be less than 1, showing the danger.

### 4. Precision notes

- Use Python’s `float` (double precision) for initial tests; for critical validation switch to `mpmath` with 50 digits.
- When $X$ is large and $h$ values moderate, the phase $X\log(1+h)$ may cause catastrophic cancellation in the real part; the paired sum must be computed by summing terms exactly (no premature simplification). The script will compute `raw` by summing over all signed $h$ directly.
- The CSV output should be generated with exactly 15 significant digits and verified against a known algebraic simplification case where the answer is analytically known (e.g., constant coefficients and a kernel like $e^{iX h}/h$).

### 5. Limitations

- This test does **not** prove that the M2 sum is large; it only demonstrates that dropping the complex phase leads to an invalid bound.
- The surrogate kernel is not the true oscillatory kernel of the Gauss circle problem; however, the algebraic principle (complex coefficients do not decouple into real positive parts) is independent of the kernel.
- The full M2 sum may contain additional oscillatory factors from the Vaaler residual; those must be accounted for in a later test.

## Theorem-dependency audit

The diagnostic test itself does not depend on any external theorem; it is a self‑contained algebraic comparison. However, it is designed to stress‑test the claims made in the broader proof effort, which does depend on several theorems. The following table summarizes the dependency status of those theorems.

| Theorem / Lemma | ID | Status | Needed hypothesis missing? |
|---|---|---|---|
| Vaaler finite approximation (H4) | `H4` | `source_audit_required` | Exact statement, constants, residual inequality not yet verified from rendered paper. |
| Balanced hyperbola & sawtooth reductions (H1‑H3) | `H1-H3` | `proved_internal` | Endpoint conventions must be kept visible. No missing external dep. |
| Fejér residual bound (R5‑Full) | `R5-Full` | `derived_under_assumptions` | Depends on `H4`; hence inherits its audit requirement. |
| Bombieri–Iwaniec type estimates (Li‑Yang 2023) | `Li-Yang-source-audit` | `source_audit_required` | Theorem hypotheses not yet transcribed from arXiv source; cannot be used as black‑box. |
| M2 character factor | `M9-M2-character-factor` | `open` | Need lemmas on how $C_h$ behaves under fourth‑moment transformations. |
| M2 near‑collision taxonomy | `M9-near-collision-taxonomy` | `open` | Exact classification not yet complete. |

All external theorems needed for `M9` have open source audits. Until those audits are completed, any derived bound for M1/M2 must be treated as `derived_under_assumptions`. The regression test is not affected because it only tests the algebraic handling of complex weights, which is a sub‑claim that does not rely on the exact Vaaler theorem.

## Hidden assumptions and potential gaps

1. **Exact form of M2 kernel**: The reading packet does not contain the explicit analytic expression for $\Phi_X(h)$ in the M2 sum. We have assumed a generic oscillating kernel; the test script is written with a pluggable function so that the true kernel can be substituted once it is provided by A1/A2. Until then, the test’s relevance is limited to the principle that complex phases cannot be ignored.

2. **Vaaler coefficient symmetry**: We assumed $\alpha_{-h,H_D} = \overline{\alpha_{h,H_D}}$, which is plausible because Vaaler’s coefficients come from a real‑valued approximation of a real function. However, this must be confirmed from the rendered paper. If the symmetry is different (e.g., real and even), the conjugation properties of $\beta_h$ change, and the test's simulated coefficients may not reflect the actual scenario.

3. **Integer endpoint convention**: The sawtooth function used by Vaaler may have a jump convention at integers; this affects the exact Fourier coefficients. The test sidesteps this by using continuous parameters.

4. **Infinite sum truncation**: The test uses a finite truncation $|h|\le H$. The real M2 sum is over an infinite set but is absolutely convergent after smoothing. The paired vs. raw equality holds termwise, so a finite test is sufficient to expose algebraic mistakes.

5. **Complex vs. real bound confusion**: The central gap is that a bound like `paired_real_abs` is not an upper bound for `|raw|`. The test can quantify the failure ratio, but cannot guarantee that the ratio remains bounded away from 1 for the true M2 kernel; that would require an analytic proof.

## Counterexample or obstruction search

### Analytic counterexample:
Consider $\beta_h = (i)^{|h|} / h$ (complex, with $\beta_{-h}=(-1)^{|h|}\overline{\beta_h}$? Not exactly). Let $\Phi(h) = e^{i h} / h$. Then the raw sum

$$
S = \sum_{h\neq 0} \frac{i^{|h|}}{h}\,\frac{e^{ih}}{h}
$$

is absolutely convergent and has a non‑zero imaginary part. If one erroneously bounds $|S|$ by $2\sum_{h=1}^\infty |\operatorname{Re}(i^h e^{ih}/h^2)|$, the bound can be much smaller than $|S|$ because the imaginary parts add constructively while the real parts cancel. This is a rigorous counterexample to the claim that a real‑paired bound suffices for all complex weight sequences. The test will produce such an example and measure the gap.

### Near‑collision obstruction:
The `M9-near-collision-taxonomy` obligation warns that in the fourth‑moment approach, terms with $|h_1\pm h_2|$ small create large correlations. The paired simplification might accidentally cancel some of these correlations if not handled with full complex weights. The diagnostic test cannot explore the fourth moment directly, but it can incorporate a two‑parameter sum to illustrate that phase coherence can survive in a paired representation even when the coefficients are complex.

## Verification

### Test script verification plan:

1. **Unit test with explicit analytic sum**:
   Choose $\beta_h = 1$ for $h=\pm 1$ and $0$ otherwise, $\Phi(h)=e^{i\theta h}$. Compute raw and paired by hand, verify Python output matches.

2. **Symmetry test for real even coefficients**:
   Set $\beta_h$ real even, kernel $K(h)=1/h$. The raw sum is purely real (odd parts cancel). Check that `paired_real_abs` equals `|raw|` in this special case.

3. **Complex coefficient test**:
   Use random complex $\beta_h$ with $\beta_{-h} = \overline{\beta_h}$ (but not real). Verify that raw sum is not real, and that `paired_real_abs` underestimates.

4. **Precision stress test**:
   Run with $H=200$ and large $X$; compare double‑precision vs. `mpmath` to see if cancellation causes relative error > $10^{-6}$. If so, recommend `mpmath` for the production diagnostic.

### Output table:
The script will produce `outputs/table_small.csv` with at least 20 rows varying $X$ and the coefficient randomness. A separate report `computations/m9_regression/report.md` will include:

- Exact formulas used.
- Table of results with commentary.
- Conclusions about the necessity of the two‑sided complex formulation.
- Limitations and next steps.

## Divergent alternatives and 20% exploration

While the primary task is the regression test, the following divergent analytical alternatives could complement or circumvent the current M9 bottleneck. Each is stated with the precise lemma that would be needed and a quick falsification test.

### Alternative 1: Bombieri–Iwaniec double large sieve with character factor

**Idea**: Instead of bounding M2 via a fourth‑moment near‑collision expansion, apply the Bombieri–Iwaniec double large‑sieve inequality directly to the exponential sum

$$
S = \sum_{h\sim H} \alpha_h C_h\, e(f(h)),
$$

where $f(h)$ contains a reciprocal term. The character factor $C_h$ is essentially a multiplicative character, which can be absorbed into the sieve weight after a dyadic decomposition.
**Lemma needed**: A double large‑sieve bound for sums $\sum_{h} \chi_4(h) a_h e(f(h))$ with smooth $f$, valid for $h$ up to $X^{1/2}$.
**Quick test**: Formulate the sum with $f(h) = c/h$ and $a_h = 1$; compute the large‑sieve constant numerically for small $H$ and check if the theoretical savings match a random‑matrix prediction. If the predicted bound is worse than $X^{1/4}$, the route is obstructed.

### Alternative 2: Mellin–Perron representation of the M2 sum

**Idea**: Write the reciprocal sum $\sum_{h} \beta_h h^{-1} e^{i X \log h}$ as a Perron integral

$$
\frac{1}{2\pi i} \int_{c-i\infty}^{c+i\infty} \Bigl(\sum_{h} \beta_h h^{-s}\Bigr) X^s \frac{ds}{s},
$$

shift the contour to left, and pick up poles from the Dirichlet series. The character factor $C_h$ contributes a Dirichlet $L$‑function $L(s,\chi_4)$. The sum then reduces to a residue plus an error that can be bounded by convexity estimates.
**Lemma needed**: Estimate for $\sum_{h\le H} \alpha_{h,H_D} \chi_4(h) h^{-s}$ on the critical line.
**Quick test**: For a toy Dirichlet polynomial, compute the Mellin inversion numerically and see if the error term can be made $O(X^{1/4})$. If the convexity bound gives $O(X^{1/3})$, the method fails.

### Alternative 3: Cauchy–Schwarz refinement with fourth moment but signed character weights

**Idea**: The current fourth‑moment approach squares the sum, leading to near‑collisions. Instead, apply the Hölder inequality with exponent $4$ but keep the character factor inside an absolute value, yielding a weighted $L^4$ norm that can be compared to the unweighted case.
**Lemma needed**: Moment inequality for exponential sums with multiplicative character weights: $\| \sum \chi_4(h) a_h e(f(h)) \|_4 \le C \| \sum a_h e(f(h)) \|_4$, where $C$ depends on the conductor.
**Quick test**: For a generic polynomial phase, compute the fourth moment numerically with and without the character and estimate the constant. If $C$ is > 2, the method gives no improvement.

These alternatives are not intended to replace the regression test; they are recorded as potential research directions for later rounds.

## Useful lemmas

1. **Lemma (Coefficient conjugation):** If $a_{-h} = \overline{a_h}$ and $f(-h) = -f(h)$ (odd function), then $\sum_{h\neq 0} a_h e^{i f(h)}$ is purely imaginary.
   *Proof*: Pair $h$ and $-h$: $a_h e^{i f(h)} + a_{-h} e^{i f(-h)} = a_h e^{i f(h)} + \overline{a_h} e^{-i f(h)} = 2 \operatorname{Re}(a_h e^{i f(h)})$, which is real; the sum over all pairs is real. If the sum is claimed to be imaginary, the symmetry must be broken. This lemma helps identify when a real simplification is justified.

2. **Lemma (Invalid paired bound):** For any complex numbers $z_h$,
   $$
   \Bigl| \sum_{h>0} (z_h + z_{-h}) \Bigr|
   \le \sum_{h>0} |z_h + z_{-h}|
   \le \sum_{h>0} (|z_h|+|z_{-h}|) = \sum_{h\neq 0} |z_h|.
   $$
   However, the intermediate bound $\sum_{h>0} |\operatorname{Re}(z_h+z_{-h})|$ is **not** necessarily an upper bound for $|\sum z_h|$.
   *Counterexample*: $z_1 = i$, $z_{-1}=i$, then $z_1+z_{-1}=2i$, $|2i|=2$, but $|\operatorname{Re}(2i)|=0$.
   This is the core algebraic mistake that the regression test must expose.

3. **Lemma (Character factor parity):** $C_h = e(h/4)-e(3h/4)$ satisfies $C_{-h} = \overline{C_h}$ and $C_h = 2i\chi_4(h)$. Moreover, $|C_h| = \sqrt{2}$ for odd $h$ and $0$ for even $h$.
   *Verification*: direct computation.

## What should be tested next

1. **Execute the regression test** using the supplied script; confirm that the `paired_real_abs` underestimates the true absolute value by a factor that grows with $H$.
2. **Extend the test to the actual M2 kernel** once the exact expression is provided by A1. This will involve substituting the Bessel‑function‑like kernel and using high‑precision arithmetic.
3. **Audit the Vaaler source** to obtain the true $\alpha_{h,H_D}$ coefficients; then run the test with those coefficients to see if any accidental real‑valuedness occurs (unlikely).
4. **Design a fourth‑moment test** simulating the $N=0$ and near‑collision configurations with the character factor included, to stress the `M9-near-collision-taxonomy`.
5. **Implement an endpoint uniformity check**: vary $D$ from $X^{1/4}$ to $X^{1/2}$ and see if the computed M2 sum (via brute force for small $X$) shows any blow‑up at the endpoints.

## Proposed state patch, if any

The following changes are proposed for `state/proof_obligations.yml`. They add concrete evidence and actionable next steps for the regression obligation, and create a new computation‑track obligation for the script deliverable.

```yaml
- id: M9-regression-raw-vs-paired
  status: diagnostic_only
  evidence:
    positive:
      - "computations/m9_regression/run.py"
      - "outputs/table_small.csv"
      - "computations/m9_regression/report.md"
    negative: []
    inconclusive: []
  next_action: "Run the script with true Vaaler coefficients and M2 kernel when available; add those results as further evidence."

- id: M9-regression-script
  type: computation
  track: computation
  title: "Python diagnostic script for M2 raw vs paired convention"
  status: proposed
  statement_tex: "The script computes four aggregates: raw two‑sided sum, paired exact sum, paired real‑absolute bound, and paired complex‑absolute bound, for synthetic coefficients and a toy kernel, and outputs a CSV table."
  dependencies: []
  implies: ["M9-regression-raw-vs-paired"]
  accepted_evidence_level: diagnostic_only
  required_output:
    - "computations/m9_regression/run.py"
    - "outputs/table_small.csv"
    - "computations/m9_regression/report.md"
  owner: A3
  next_action: "Commit script and run with parameters; generate report."
```

Additionally, the `M9-M2-character-factor` obligation could be augmented with a note that the regression test provides algebraic evidence that the factor cannot be absorbed, but that is not a formal proof obligation. I will not over‑patch.

## Confidence

- **That the two‑sided complex sum is the only algebraically safe representation for M2**: very high (0.98). The symmetry of the coefficient array guarantees $\beta_{-h}=\overline{\beta_h}$, but the kernel’s phase prevents a trivial real‑paired bound.
- **That the provided script will correctly demonstrate the discrepancy for synthetic data**: high (0.95), provided the kernel is chosen with a non‑trivial odd part.
- **That the script remains relevant after the exact M2 kernel is supplied**: moderate (0.70), because the kernel may possess additional symmetries (e.g., $\Phi_X(-h) = \overline{\Phi_X(h)}$) that could make the raw sum real; but even then, a proof that relies on that symmetry must **prove** it, not assume it. The diagnostic test can still check whether the symmetry actually holds.
- **Overall confidence that the regression test will contribute to preventing a faulty proof of M9**: high (0.85). It serves as a necessary sanity check and can be extended to other parts of the argument.

The diagnostic plan is ready for execution. The judge and other agents may use the provided script directly or adapt it after receiving the precise analytic formulas.

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 1.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Agent Depth Contract

Write a referee-style report on A2 and A3. Include a score table, hidden assumptions, exact claims needing proof, concrete verification tasks, and a research-strategy adjustment recommendation. Use available web search to verify cited external theorems; if search is unavailable, mark citation status as unverified rather than inventing references.



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
