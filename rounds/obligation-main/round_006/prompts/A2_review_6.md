You are Gemini Pro Deep Think, acting as independent alternative strategist, obstruction finder, and referee-style reviewer.

Review the other agents' Round 6 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Use Gemini Pro Deep Think. Think slowly and answer in a detailed referee style. The A2 standing standard applies to both reasoning and review: long-form, concrete, formula-level, theorem-hypothesis-aware, and calibrated. Be skeptical of any claimed proof of the Gauss circle conjectural exponent unless all smoothing, truncation, endpoint, and theorem-hypothesis details are explicit. Do not invent transformed identities, monotonicity claims, constants, citations, or counterexamples. Derive them in-line, mark them as conjectural, verify them by web/literature search when available, or request a symbolic/numeric check. For the proof-obligation workflow, do not label a new obstruction, taxonomy class, asymptotic estimate, or state promotion as [PROVED] unless the response supplies a complete proof with exact definitions and hypotheses. Default new obstruction mechanisms to [HEURISTIC] or [DERIVED-UNDER-ASSUMPTIONS] until an exact theorem statement or counterexample check is supplied. Use the current graph's two-sided M2 convention, actual beta_h coefficients, and cleared N formula unless you explicitly prove a change of convention. Do not only reject: include a repair or alternative route with exact hypotheses, a narrow lemma, and a falsification test. Avoid overconfident closure language. Before final submission, perform a visible calibration check for unsupported theorem claims, excessive confidence, and missing hypotheses.

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

## Review-Stage Guardrail

This is Stage B cross review for Round 6.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.

## Prompt-Enforced Generation Mode

Low-temperature review mode: behave as a low-variance conservative referee. Optimize for exact formula checking, explicit assumptions, narrow provisional claims, and reproducible verification tasks. Do not optimize for novelty, rhetorical force, broad synthesis, or route advocacy. When multiple phrasings are possible, choose the least conclusive neutral phrasing. Keep creativity low and calibration high. Prefer boring exactness over memorable language. Low-temperature mode controls style only; it does not reduce the need for concrete evidence. If a draft is below the hard minimum, expand with neutral formula-level checks, theorem-hypothesis audits, boundary-case verifications, or explicit falsification tests, not with rhetoric. Score idea quality separately from proof-graph evidence: useful routes may receive credit in prose while state-promotable evidence remains low. Before finalizing, perform a visible approximate word-count self-check. Target 5000-7000 words, with hard minimum 4500 words. If token-family rewriting drops the draft below 4500 words, add neutral mathematical content using additional theorem-hypothesis audit, boundary-case verification, symbolic stress tests, or proof-draft-ready formula audit. Before finalizing, perform a rewrite pass that removes high-certainty, route-closing, finality/permanence, and dramatic wording, then confirm `token-family scan: passed` in the calibration section only if the scan is actually true for the answer body.

## Agent Depth Contract

Standing A2 review standard: write a deep Stage B referee report, not a compact verdict. Target 5000-7000 words; hard minimum 4500 words. If the first draft is shorter, continue expanding before finalizing with concrete mathematics only. Review every other active agent separately and in detail. Include at least 12 top-level `##` sections, a claim ledger with at least 8 reviewed claims, a theorem-dependency audit with at least 6 named dependencies or missing theorem statements, an unsupported-closure/overclaim audit, at least 4 explicit correction or verification items, at least 4 hidden assumptions or failure modes, at least 3 concrete stress tests or numerical/symbolic checks, a required split score table for every other active agent, an explicit `## Confidence` section, and a visible pre-submit calibration check. Split scores into idea quality, state evidence, and calibration; do not collapse useful ideas and proof-graph evidence into one vague rating. For each reviewed agent, identify strongest contribution, exact assumptions, claims that are proved versus derived-under-assumptions versus heuristic, likely false or underspecified statements, missing theorem hypotheses, what would falsify the contribution, and one concrete next verification task. Every major criticism must quote or restate the exact mathematical object being criticized, then give a formula-level reason. Do not reward elegant but uncertified asymptotics, spacing claims, signed-trace claims, Mellin-Perron claims, or Fourier-tail claims unless constants, hypotheses, boundary cases, and error terms are explicit. Use neutral referee language; do not quote, paraphrase, list, or mention prohibited rhetoric examples, even when saying they were avoided. Do not use numeric confidence above 0.89, percentage-allocation rhetoric, totalizing closure claims, dramatic verdict words, finality/permanence language, or lock-in route language. Before finalizing, mechanically replace finality/permanence/lock-in wording with provisional audit wording, then run a hard token-family scan and report only `token-family scan: passed` without listing the scanned roots. End with research-strategy implications and next-round recommendations.

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
          "rounds/obligation-main/round_005/responses/A4-005.md"
        ]
      },
      "owner": "A1",
      "next_action": "Commit sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, and the Phi regularity or Lipschitz fact needed for freezing H_D.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
        "M9-M2-local-fourth-moment-LFM"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_004/responses/A1-004.md",
          "rounds/obligation-main/round_004/responses/A2-004.md",
          "rounds/obligation-main/round_004/responses/A4-004.md",
          "rounds/obligation-main/round_005/responses/A2-005.md",
          "rounds/obligation-main/round_005/responses/A4-005.md"
        ],
        "negative": [
          "rounds/round_001/reviews/A1_review_1.md",
          "rounds/obligation-main/round_002/reviews/A1.md",
          "rounds/obligation-main/round_002/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_003/human/stage-a-response-audit.md",
          "rounds/obligation-main/round_003/human/stage-b-review-audit.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
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
          "rounds/obligation-main/round_005/responses/A3-005.md"
        ]
      },
      "owner": "A2",
      "next_action": "Preserve mixed and unclassified exact N=0 classes. Reconcile semi-diagonal versus fraction-matching terminology, then prove or refute the unpaired exact N=0 mass bound.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_005/reviews/A1.md"
        ]
      },
      "owner": "A2",
      "next_action": "Treat denominator-paired near-collisions as scoped by M9-M2-DP-near-collision-bound after proof-draft verification. Shift the main analytic target to unpaired-denominator near-collisions with exact beta weights.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_005/reviews/A1.md"
        ]
      },
      "owner": "A3",
      "next_action": "Rerun after materialization with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, complex-weight cosine pairing, real-weight Re B_h formula, and explicit failure of Re B_h for complex weights. Archive script, command, table, precision log, and report.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
        "M9-M2-local-fourth-moment-LFM"
      ],
      "evidence": {
        "positive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_004/reviews/A4.md",
          "rounds/obligation-main/round_004/judge/judge-004.md",
          "rounds/obligation-main/round_005/responses/A1-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Use the AP lemma only as an interpolation module. To advance this obligation, prove the everywhere-local fourth-moment estimate on windows delta=X^(1/2)/D, control the fattened band |N|<<D^5 X^(-1/2), handle exceptional windows, and split off the endpoint D=X^(1/2).",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_005/reviews/A1.md"
        ]
      },
      "owner": "A3",
      "next_action": "Materialize and run executable artifacts with exact integer arithmetic for N, official phases, true Phi after H4, raw/cosine/ReB_h formula tests, fraction-matching overlap tests, unpaired exact N=0 tables, local-window diagnostics, and signed-vs-unsigned comparisons.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
        "M9-endpoint-uniformity"
      ],
      "evidence": {
        "positive": [],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/responses/A4-005.md",
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "State and attack a local fourth-moment estimate on every interval of length X^(1/2)/D; include the fattened resonance band, exceptional-window issue, and endpoint D=X^(1/2) subcase.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_005/responses/A4-005.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Write validator-ready dyadic proof with constants, parity support, t=0 and t!=0 cases, and exact dependence on C0; do not use it to promote full near-collision estimates.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_005/responses/A4-005.md"
        ],
        "negative": [],
        "inconclusive": [
          "rounds/obligation-main/round_005/reviews/A1.md",
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "Write the normal form in proof-draft-ready notation and use it to define unpaired exact N=0 families.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
          "rounds/obligation-main/round_005/judge/judge-005.md"
        ]
      },
      "owner": "A4",
      "next_action": "State the exact spacing statistic P(D,H;X), run A3 signed-vs-unsigned and first-spacing diagnostics, and audit Li-Yang only as a source guardrail.",
      "last_updated_round": 5,
      "last_updated_at": "2026-07-02T23:47:54"
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
    }
  ]
}

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 5 in run `obligation-main`.

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
  Next action: Preserve mixed and unclassified exact N=0 classes. Reconcile semi-diagonal versus fraction-matching terminology, then prove or refute the unpaired exact N=0 mass bound.
- `M9-regression-raw-vs-paired` (diagnostic_only, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Rerun after materialization with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, complex-weight cosine pairing, real-weight Re B_h formula, and explicit failure of Re B_h for complex weights. Archive script, command, table, precision log, and report.

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

created: M9-M2-average-to-pointwise-AP-lemma, M9-M2-local-fourth-moment-LFM, M9-M2-DP-near-collision-bound, M9-M2-coprime-rigidity-normal-form, M9-M2-fraction-matching-weighted-bound, M9-M2-reciprocal-SPD-route; updated: M9-M2-fourth-moment-average-to-pointwise, M9-near-collision-estimate, M9-near-collision-taxonomy, M9-M2-paired-core-weighted-bound, M9-M2-N0-diagonal-core-bound, M9-fourth-moment-enumeration, M9-regression-raw-vs-paired, H4-source-audit, M9-M2-direct-signed-bilinear-lemma, M9-M2, M9-endpoint-uniformity; rejected: A2-R5-continuous-L4-rational-orthogonality, A2-R5-semi-diagonal-terminology-promotion, A2-R5-full-exact-N0-taxonomy-promotion, A3-R5-unexecuted-artifact-positive-evidence, A4-R5-AP-implies-M9-M2; no_change: M9, M9-M1, GC-target, Conditional-bridge, R5-Full, H4, Li-Yang-source-audit; round score: 5; Round 5 adds a valid elementary AP interpolation lemma, sharpens the average-to-pointwise obstruction, scopes denominator-paired near-collisions, and isolates fraction-matching as a separate subfamily. It does not prove M9, M9-M2, M9-M1, the full exact N=0 taxonomy, or the final Gauss circle target.

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
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`
- Next action: Preserve mixed and unclassified exact N=0 classes. Reconcile semi-diagonal versus fraction-matching terminology, then prove or refute the unpaired exact N=0 mass bound.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `diagnostic_only`
- Track: `computation`
- Owner: `A3`
- Next action: Rerun after materialization with exact Vaaler Phi, official M1/M2 phases, raw two-sided formula, complex-weight cosine pairing, real-weight Re B_h formula, and explicit failure of Re B_h for complex weights. Archive script, command, table, precision log, and report.

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
- Next action: Commit sources/vaaler_1985.md with bibliographic data, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, and the Phi regularity or Lipschitz fact needed for freezing H_D.

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
- Blockers: `M9-M2-local-fourth-moment-LFM`
- Next action: Use the AP lemma only as an interpolation module. To advance this obligation, prove the everywhere-local fourth-moment estimate on windows delta=X^(1/2)/D, control the fattened band |N|<<D^5 X^(-1/2), handle exceptional windows, and split off the endpoint D=X^(1/2).

### M9-M2-local-fourth-moment-LFM: Everywhere-local fourth-moment estimate for S2 on coherence windows

- Status: `open`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `M9-near-collision-estimate`, `M9-endpoint-uniformity`
- Next action: State and attack a local fourth-moment estimate on every interval of length X^(1/2)/D; include the fattened resonance band, exceptional-window issue, and endpoint D=X^(1/2) subcase.

### M9-M2-reciprocal-SPD-route: Sign-preserving reciprocal discrepancy route for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `H4-source-audit`, `Li-Yang-source-audit`
- Next action: State the exact spacing statistic P(D,H;X), run A3 signed-vs-unsigned and first-spacing diagnostics, and audit Li-Yang only as a source guardrail.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Require each M2 route to isolate the endpoint D=X^(1/2), where the AP/local-average bridge degenerates to pointwise control.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Treat denominator-paired near-collisions as scoped by M9-M2-DP-near-collision-bound after proof-draft verification. Shift the main analytic target to unpaired-denominator near-collisions with exact beta weights.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.

### M9-M2-DP-near-collision-bound: Denominator-paired near-collision scoping bound

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `H4-source-audit`
- Next action: Write validator-ready dyadic proof with constants, parity support, t=0 and t!=0 cases, and exact dependence on C0; do not use it to promote full near-collision estimates.

### M9-M2-beta-algebra: Exact beta_h coefficient algebra for M2

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Insert beta_h algebra, raw two-sided formula, real-weight paired formula, and complex-weight cosine pairing into best_proof_draft.md after H4 source-card update.

--- FILE: state/next_round_prompts.md ---
# Next Round Prompts

Generated after round 5 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_005/judge/judge-005.md`.

## For A1

Target obligations: `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, and proof-draft maintenance.

Objectives:

1. Complete or draft `sources/vaaler_1985.md` physically. Include the earlier required data plus the new Round 5 item: a source-card check for the regularity of

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u
$$

sufficient to justify freezing $H_D$ across windows of length $\delta=X^{1/2}/D$.

2. Insert into `state/best_proof_draft.md`:
   - H1-H3 statement;
   - H4 statement, still source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - official M1/M2 definitions;
   - M2 raw two-sided, complex-weight cosine, and real-weight paired formulas;
   - fourth-moment numerator $N$;
   - AP lemma;
   - local fourth-moment hypothesis `(LFM)`;
   - list of open endpoint and unpaired near-collision blockers.

3. Write a short proof-draft note explaining why AP is not a proof of `M9-M2`: it needs `(LFM)` on every interval of length $\delta=X^{1/2}/D$, the local expansion controls $|N|\ll D^5X^{-1/2}$, and the endpoint $D=X^{1/2}$ degenerates.

4. Reconcile terminology:
   - denominator-pattern semi-diagonal;
   - pair-swapped;
   - fraction-matching/fraction-collision;
   - mixed;
   - unclassified.

5. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Exploratory allocation: compare the absolute unpaired-exact route, the local fourth-moment `(LFM)` route, and the direct signed/SPD route. State for each the exact needed theorem and a one-line falsification test.

## For A2

Target obligations: `M9-near-collision-taxonomy`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-fraction-matching-weighted-bound`, and unpaired exact $N=0$ mass.

Objectives:

1. Do not re-prove denominator-paired exact resonance or pair-swapped exact resonance.

2. Reconcile terminology. If the official semi-diagonal family is

$$
d_1=d_3,\qquad d_2=d_4,\qquad d_2(h_1+h_3)=d_1(h_2+h_4),
$$

then either prove this exact denominator-pattern family or state explicitly that Round 5's fraction-matching proof is a different subfamily.

3. Write one proof-draft-ready lemma for an unpaired exact $N=0$ family. Choose one:
   - an upper bound $\ll D^2X^\epsilon$ for a well-defined unpaired class; or
   - a lower-bound construction showing a larger scale; or
   - a normal-form reduction that leaves a smaller explicit subproblem.

4. Repair or discard the continuous $L^4$ route. If repaired, use an integer frequency based on the cleared numerator $N$ and state the exact kernel. Do not use rational-frequency orthogonality over $[0,1]$.

5. Keep `M9`, `M9-M2`, and `M9-near-collision-taxonomy` open.

Exploratory allocation: propose one sign-preserving analytic inequality that would exploit $\chi_4(h)$ without Cauchy erasing the sign.

## For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-fourth-moment-enumeration`, `M9-M2-local-fourth-moment-LFM`, and signed-vs-unsigned/SPD diagnostics.

Objectives:

1. Materialize and execute the diagnostic bundle. Required outputs:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - `python -m py_compile` result;
   - precision log;
   - CSV schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Use exact integer arithmetic for $N$ and for all exact $N=0$ classification.

3. Implement and separately test:
   - raw two-sided M2;
   - complex-weight cosine pairing;
   - real-weight paired formula;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

4. Replace placeholder $\Phi$ with the audited Vaaler $\Phi$ once H4 is available. Until then, separate classification results from coefficient-magnitude results.

5. Taxonomy tests:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - official denominator-pattern semi-diagonal;
   - fraction-matching/fraction-collision;
   - mixed;
   - unclassified.

6. Test whether A4's fraction-collision family accounts for the previously unclassified exact mass.

7. Local fourth-moment diagnostics:
   - use $\delta=X^{1/2}/D$;
   - sample many windows;
   - report local fourth moment, global fourth moment, exceptional-window concentration, and the ratio to the AP-derived bound;
   - include endpoint $D=X^{1/2}$.

8. Near-collision diagnostics:
   - compare thin band $|N|\ll D^4/X$ and local fat band $|N|\ll D^5X^{-1/2}$;
   - split denominator-paired and unpaired-denominator cases.

9. Signed-vs-unsigned/SPD diagnostics:
   - true $\beta_h$;
   - unsigned $|\beta_h|$;
   - random signs;
   - adversarial signs;
   - reciprocal spacing statistic $P(D,H;X)$ if feasible.

All outputs remain `diagnostic_only`.

## For A4

Target obligations: `M9-M2-DP-near-collision-bound`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-coprime-rigidity-normal-form`, and unpaired near-collision search.

Objectives:

1. Write validator-ready proofs for:
   - DP parity emptiness with exact dyadic constants;
   - thin DP near-collision mass bound;
   - full DP-total mass bound;
   - dependence on H4/beta odd support.

2. Write the coprime-rigidity normal form in a compact lemma format suitable for `state/lemma_bank.md`.

3. Develop the `(LFM)` obstruction:
   - prove exactly how the local window creates the band $|N|\ll D^5X^{-1/2}$;
   - isolate whether an exceptional-window argument can convert a global fourth moment into `(LFM)` outside a small exceptional set;
   - state why the endpoint $D=X^{1/2}$ still requires separate control.

4. Attack one unpaired near-collision or exact-resonance subproblem using the coprime-rigidity normal form. Provide either a proof, a counterexample family, or a sharply reduced equation.

5. Keep the SPD/sign-preserving route exploratory. State the needed first-spacing statistic and the exact falsification test for A3.

Do not claim `M9-M2`, `M9`, or `GC-target`.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.0 | 7.5 | 8.5 | Strong infrastructure consolidation: H4/R5/M2 definitions, formulas, and average-to-pointwise obstruction. No endpoint overclaim. Needs physical source-card/proof-draft commits. |
| A2 | 7.2 | 5.6 | 6.2 | Pair-swapped and fraction-matching material is useful under H4. Calibration weaker because "semi-diagonal" terminology is unsafe and the continuous $L^4$ orthogonality route is false as stated. |
| A3 | 7.6 | 3.8 | 7.2 | Good diagnostic design and correct `diagnostic_only` framing, but no positive state evidence until scripts are materialized and executed; placeholder $\Phi$ must be replaced after H4. |
| A4 | 8.8 | 7.8 | 8.4 | Strongest analytic progress: AP lemma, local-fourth-moment obstruction, DP near-collision scoping, coprime-rigidity, and fraction-collision calibration. Some M2 applications remain H4-dependent and require dyadic proof-draft verification. |

Overall Round 5 assessment: moderate but real proof-graph progress. The main gain is not an M2 estimate; it is a sharper map of what any M2 fourth-moment proof must still supply.

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

According to the uploaded Round 6 prompt and current state bundle, A1's assigned obligations are `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, and proof-draft maintenance; the prompt also explicitly forbids promotion of `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target` in this round. The current reading packet still says the theorem target is conditional only, with no new Gauss circle exponent proved, and identifies `M9` as the active bottleneck.

This Stage A response makes three narrow pieces of proof-graph progress, all short of an endpoint estimate:

1. It drafts the missing `sources/vaaler_1985.md` source-card content, including the extra Round 6 regularity check for
$$
   \Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$
   The calculus check shows that, assuming Vaaler's Theorem 6 formula, $\Phi$ extends to a $C^1$ function on $[0,1]$ with $\Phi(0)=1$, $\Phi(1)=0$, and $\Phi'(0)=\Phi'(1)=0$. This is enough for the source-card item about coefficient regularity. It does not by itself promote `H4`, because the source card still needs to be physically committed and validated.

2. It gives proof-draft-ready text for the finite Vaaler normalization, the R5 positive-Fejer product-count proof, the official $\mathcal M_1/\mathcal M_2$ definitions, the raw/two-sided and paired $\mathcal M_2$ formulas, the fourth-moment numerator $N$, the AP lemma, and the local fourth-moment hypothesis `(LFM)`.

3. It isolates a sharper endpoint obstruction for `(LFM)`: on the coherence window $\delta=X^{1/2}/D$, the local fourth-moment expansion sees the fat band
$$
   |N|\ll D^5X^{-1/2}.
$$
   At the endpoint $D\asymp X^{1/2}$, this threshold is $\asymp X^2$, while every possible cleared numerator satisfies $|N|\ll H_DD^3\asymp X^{7/4}$. Hence the local integral gives essentially no oscillatory discrimination among fourth-moment tuples at the endpoint. This does not disprove `(LFM)`, but it proves that an absolute near-collision counting proof on coherence windows cannot be the whole endpoint argument.

No claim below proves `M9`, `M9-M1`, `M9-M2`, `GC-target`, the full exact $N=0$ taxonomy, or a new Gauss circle exponent.

## Target proof obligation

Primary obligations for this response:

- `H4-source-audit`: rendered source audit for Vaaler 1985.
- `H4`: finite Vaaler approximation with floor-compatible residual.
- `R5-Full-reconciliation`: positive-Fejer product-count proof, still conditional on H4.
- `M9-M2-beta-algebra`: exact $\beta_h$ algebra and paired formulas.
- `M9-M2-fourth-moment-average-to-pointwise`: AP is only an interpolation module.
- `M9-M2-local-fourth-moment-LFM`: formulate and stress-test the everywhere-local fourth moment.
- Proof-draft maintenance: produce text that can be inserted into `sources/vaaler_1985.md` and `state/best_proof_draft.md`.

Secondary obligations touched but not promoted:

- `M9-endpoint-uniformity`.
- `M9-near-collision-estimate`.
- `M9-M2-reciprocal-SPD-route`.
- `Li-Yang-source-audit`.

## Main claim or direction

The correct A1 direction is proof-infrastructure consolidation plus obstruction sharpening, not an endpoint proof.

The main route remains the conditional reduction

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The current state already records this bridge as conditional, with `GC-target` blocked by `M9`. The work below strengthens the bridge documentation and clarifies what a future proof of `M9-M2` would still need.

The most important mathematical conclusion in this response is the following scoped obstruction.

**Endpoint LFM degeneracy claim.** Let

$$
S_2(D;t)
=
\sum_{1\le |h|\le H_D}\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(h t/(4d)),
\qquad
H_D\asymp DX^{-1/4}.
$$

In the local fourth-moment expansion over an interval $I$ of length

$$
\delta=X^{1/2}/D,
$$

the relevant non-oscillatory band is

$$
|N|\ll D^4/\delta=D^5X^{-1/2}.
$$

At $D\asymp X^{1/2}$, this band contains all possible fourth-moment numerators $N$, since

$$
|N|\ll H_DD^3
\asymp
(DX^{-1/4})D^3
=
D^4X^{-1/4}
\asymp
X^{7/4}
\ll X^2
\asymp
D^5X^{-1/2}.
$$

Therefore, at the endpoint, `(LFM)` cannot be proved by a phase-spacing argument that only counts or suppresses large $N$. A separate signed estimate, structural cancellation estimate, or endpoint-specific argument is still necessary.

This is a proof-graph-safe obstruction statement. It does not assert `(LFM)` is false. It asserts that the standard local oscillatory kernel loses all discriminatory power at the top dyadic range.

## Route proposals

### Route 1: H4/R5 proof-draft route

**Rank:** highest proof-infrastructure impact, low direct M9 impact.

**Needed obligation.** Complete `H4-source-audit` and keep `R5-Full` as `derived_under_assumptions` until the source card is physically updated.

**Exact lemma.** Assuming H4, for every active dyadic $D$ with $H=H_D\asymp DX^{-1/4}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

**Dependencies.** Vaaler H4 residual inequality, Fejer kernel normalization, divisor bound $\tau(n)\ll_\epsilon n^\epsilon$, dyadic bounded overlap.

**First proof step.** Apply the positive Fejer residual before Fourier expansion:

$$
|R_H^F(t)|\le \frac{1}{2H+2}K_H(t),
$$

then reduce the residual sum to product counts near $X=md$ and $X=(4m-\rho)d$.

**Likely obstruction.** Endpoint and noninteger $X$ conventions. The product-count proof must count integer $n$ close to real $X$, not only exact divisors of integer $X$.

**Fast falsification test.** Find real $X$, active $D$, and $\rho\in\{0,1,3\}$ for which

$$
\sum_{d\asymp D}K_H\left(\frac{X/d+\rho}{4}\right)
$$

exceeds $HX^{1/4+\epsilon}$ after normalizing by the intended $H$. Existing state treats this as not observed, but a committed diagnostic bundle is still needed.

### Route 2: Local fourth-moment `(LFM)` route

**Rank:** highest analytic relevance to M2, but endpoint obstruction is severe.

**Needed obligation.** Prove `M9-M2-local-fourth-moment-LFM`:

$$
\delta^{-1}\int_I |S_2(D;t)|^4\,dt
\ll_\epsilon X^{1+\epsilon}
$$

for every interval $I$ of length

$$
\delta=X^{1/2}/D
$$

near $X$, uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

**Dependencies.** `M9-M2-fourth-moment-expansion`, AP lemma, endpoint uniformity, actual $\beta_h$ coefficients.

**First proof step.** Expand the local fourth moment. The kernel is

$$
\delta^{-1}\int_I
e\left(\frac{t}{4}
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)\right)\,dt.
$$

With

$$
Q=d_1d_2d_3d_4\asymp D^4
$$

and

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3,
$$

the integral is bounded by

$$
\min\left(1,\frac{D^4}{\delta |N|}\right)
=
\min\left(1,\frac{D^5X^{-1/2}}{|N|}\right).
$$

**Likely obstruction.** At $D\asymp X^{1/2}$ this kernel is essentially $1$ for all tuples. Absolute near-collision counting cannot yield the desired $X^{1+\epsilon}$ fourth-moment scale.

**Fast falsification test.** A3 should compute endpoint local fourth moments with true $\beta_h$, unsigned $|\beta_h|$, random signs, and adversarial signs. If true signs behave like unsigned/adversarial signs, the LFM route needs a new analytic input rather than more taxonomy.

### Route 3: Direct signed/SPD route

**Rank:** best backup for endpoint M2; currently only proposed.

**Needed theorem.** A sign-preserving reciprocal discrepancy estimate:

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

**Dependencies.** `M9-M2-beta-algebra`, `M9-M2-character-factor`, `M9-endpoint-uniformity`, and a new spacing or discrepancy theorem that does not erase $\chi_4(h)$ through Cauchy, Schur, Frobenius, or operator norm estimates.

**First proof step.** Define a signed spacing statistic. A minimal candidate is

$$
\mathcal P(D,H;X;\eta)
=
\sum_{\substack{d_1,d_2\asymp D\\d_1\ne d_2}}
w_{d_1}\overline{w_{d_2}}
\sum_{\substack{1\le h_1,h_2\le H\\2\nmid h_1h_2}}
\frac{\chi_4(h_1)\chi_4(h_2)}{h_1h_2}
\mathbf 1\left(
\left\|
\frac{h_1X}{4d_1}-\frac{h_2X}{4d_2}
\right\|\le\eta
\right),
$$

or a smoothed variant whose bound implies a large-sieve inequality for the actual $\beta_h$ coefficients.

**Likely obstruction.** Most known norm extractions replace $\chi_4(h)$ by $|\chi_4(h)|$ and leave only odd support. The current state explicitly treats this as a sign-loss diagnostic.

**Fast falsification test.** Compare the actual $\beta_h$ statistic against the same statistic with $|\beta_h|$, random signs, and adversarial signs. If actual signs show no systematic reduction, deprioritize this route.

### Route 4: Unpaired exact-resonance route

**Rank:** necessary taxonomy work, but unlikely alone to prove M2.

**Needed theorem.** Bound exact $N=0$ resonances not covered by pair-equality, denominator-paired, pair-swapped, denominator-pattern semi-diagonal, or fraction-matching:

$$
\sum_{\substack{d_i\asymp D,\,1\le |h_i|\le H_D\\N=0\\\text{unpaired/mixed}}}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\ll_\epsilon D^2X^\epsilon
$$

or construct a counterexample family at larger scale.

**Dependencies.** Coprime-rigidity normal form, actual beta magnitudes, and exact taxonomy definitions.

**First proof step.** Reduce each fraction $h_i/d_i$ to $r_i/s_i$ with $(r_i,s_i)=1$, then classify exact solutions of

$$
\frac{r_1}{s_1}-\frac{r_2}{s_2}+\frac{r_3}{s_3}-\frac{r_4}{s_4}=0.
$$

**Likely obstruction.** Additive energy of rationals in dyadic boxes may have families not visible in denominator-pattern terminology.

**Fast falsification test.** A3 should report whether fraction-matching/fraction-collision accounts for the previously unclassified exact mass. If a residual unclassified mass grows faster than $D^2X^\epsilon$, the absolute exact-resonance route must change.

## Detailed reasoning

### 1. Draft content for `sources/vaaler_1985.md`

Bibliographic data:

- Author: Jeffrey D. Vaaler.
- Title: "Some extremal functions in Fourier analysis."
- Journal: *Bulletin of the American Mathematical Society (New Series)*.
- Volume/issue/pages: 12(2), 183--216.
- Date: April 1985.
- DOI: `10.1090/S0273-0979-1985-15349-2`.

AMS metadata confirms the bibliographic data and DOI. The local rendered PDF also shows the title, author, journal, volume, issue, date, and page range on page 1.

Local file:

- `/mnt/data/[Vaaler] Some extremal functions in Fourier analysis_Bull. Amer. Math. Soc..pdf`

Exact theorem used:

Vaaler defines the entire functions $H,J,K$ in Section 2 and proves Theorem 6. In the project normalization, Theorem 6 supplies the coefficient function through

$$
\widehat J(t)
=
\begin{cases}
1,&t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|,&0<|t|<1,\\
0,&1\le |t|.
\end{cases}
$$

For $0<u<1$, define

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

Vaaler's Section 7 defines periodic trigonometric polynomials $i_N,j_N,k_N$ by equations (7.1)--(7.3). Theorem 18 then gives the periodic sawtooth approximation and residual inequality. The local rendered page snippet identifies the Theorem 18 residual inequality as

$$
|\psi*j_N(x)-\psi(x)|
\le
(2N+2)^{-1}k_N(x).
$$

The source-card status remains `source_audit_required` until the theorem/equation transcription is physically committed.

Project notation translation:

Use the Fourier convention

$$
e(t)=e^{2\pi i t}.
$$

Let Vaaler's centered periodic sawtooth be

$$
\psi_V(x)=
\begin{cases}
x-\lfloor x\rfloor-\frac12,&x\notin\mathbb Z,\\
0,&x\in\mathbb Z.
\end{cases}
$$

The project uses the floor-compatible sawtooth

$$
\psi_F(x)=x-\lfloor x\rfloor-\frac12
$$

with

$$
\psi_F(n)=-\frac12
\qquad(n\in\mathbb Z).
$$

For $H=N$, define

$$
V_H(t)=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

Then the project-form H4 statement should be written as

$$
\psi_F(t)=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)
+
R_H^F(t),
$$

with

$$
|R_H^F(t)|
\le
\frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

At integers $n$, the finite Fourier sum $V_H(n)$ is $0$ by oddness/symmetry of the coefficients, while $\psi_F(n)=-1/2$. The Fejer residual covers the half-jump because

$$
K_H(0)=H+1
$$

and hence

$$
\frac{K_H(0)}{2H+2}=\frac12.
$$

This endpoint convention must be present in the source card before H4 can be used as a validated external theorem.

### 2. Regularity check for $\Phi$

Assume Vaaler's Theorem 6 formula

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u
\qquad(0<u<1).
$$

For $u\in(0,1)$,

$$
\Phi'(u)
=
\pi(1-2u)\cot(\pi u)
-
\pi^2u(1-u)\csc^2(\pi u)
+
1.
$$

Near $u=0$, use

$$
\cot(\pi u)=\frac1{\pi u}-\frac{\pi u}{3}+O(u^3).
$$

Then

$$
\pi u(1-u)\cot(\pi u)
=
(1-u)\left(1-\frac{\pi^2u^2}{3}+O(u^4)\right)
=
1-u-\frac{\pi^2u^2}{3}+O(u^3),
$$

so

$$
\Phi(u)
=
1-\frac{\pi^2u^2}{3}+O(u^3).
$$

Thus

$$
\Phi(0+)=1,
\qquad
\Phi'(0+)=0.
$$

Near $u=1$, put $v=1-u$. Since

$$
\cot(\pi(1-v))=-\cot(\pi v)
=
-\frac1{\pi v}+\frac{\pi v}{3}+O(v^3),
$$

we get

$$
\pi u(1-u)\cot(\pi u)
=
\pi(1-v)v\cot(\pi(1-v))
=
-(1-v)+\frac{\pi^2}{3}(1-v)v^2+O(v^4).
$$

Adding $u=1-v$ gives

$$
\Phi(1-v)
=
\frac{\pi^2}{3}v^2+O(v^3).
$$

Hence

$$
\Phi(1-)=0,
\qquad
\Phi'(1-)=0.
$$

Therefore $\Phi$ extends continuously to $[0,1]$ by

$$
\Phi(0)=1,\qquad \Phi(1)=0,
$$

and $\Phi'$ extends continuously to both endpoints with zero endpoint values. In particular,

$$
\sup_{0\le u\le1}|\Phi'(u)|<\infty,
$$

so $\Phi$ is Lipschitz on $[0,1]$.

This proves the Round 6 regularity item, conditional on the correctness of the Vaaler formula. It is safe to record as a calculus lemma under H4-source assumptions.

### 3. Freezing $H_D$ across local windows

Let $X_0$ be fixed, let

$$
X^{1/4}_0\le D\le X_0^{1/2},
$$

and choose an integer

$$
H=H_D(X_0)\asymp DX_0^{-1/4}.
$$

For a local interval

$$
I=[X_0-c\delta,X_0+c\delta],
\qquad
\delta=X_0^{1/2}/D,
$$

we have, uniformly for $t\in I$,

$$
\frac{|t-X_0|}{X_0}
\ll
\frac{X_0^{1/2}}{DX_0}
=
\frac{1}{DX_0^{1/2}}
\le
X_0^{-3/4}.
$$

Thus

$$
D t^{-1/4}
=
D X_0^{-1/4}
\left(1+O(X_0^{-3/4})\right).
$$

The continuous Vaaler height changes by

$$
O\left(DX_0^{-1/4}X_0^{-3/4}\right)
=
O(DX_0^{-1})
\le
O(X_0^{-1/2}).
$$

In particular, for large $X_0$, the intended local height is stable at the level of dyadic comparability. More importantly, Vaaler's theorem is valid for any fixed integer $H$, so in the local fourth-moment proof one may freeze $H=H_D(X_0)$ throughout $I$ and never differentiate the coefficients in $t$.

The Lipschitz regularity of $\Phi$ is still useful for two bookkeeping tasks:

1. If an auxiliary proof compares coefficients with heights $H_D(t)$ and $H_D(X_0)$, the variation in $u=h/(H+1)$ is bounded by a constant times the variation in $H^{-1}$, and $\Phi$ introduces no endpoint singularity.

2. In computation, replacing a provisional $\Phi$ by the audited $\Phi$ is numerically stable even near $u=0$ and $u=1$ because $\Phi'$ is bounded and in fact vanishes at both endpoints.

The proof draft should emphasize that coefficient freezing is an allowed choice, not a theorem requiring cancellation.

### 4. H1--H3 proof-draft insertion

The accepted H1--H3 statement should be recorded as follows.

Let

$$
P(X)=N(\sqrt X)-\pi X,
\qquad
y=\lfloor X^{1/2}\rfloor,
$$

and

$$
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12.
$$

Then the exact symmetric hyperbola, the periodic $\chi_4$ partial-sum identity, and the balanced sawtooth formula give

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
O(1).
$$

This is the floor-compatible starting point for H4. The endpoint convention $\psi_F(n)=-1/2$ must remain visible whenever Vaaler is applied.

### 5. R5 positive-Fejer product-count proof

After applying H4 with local height

$$
H=H_D\asymp DX^{-1/4},
$$

the residual terms are bounded by positive Fejer sums. It is enough to prove, for active dyadic $D$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}
$$

and

$$
\frac1H\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}
\qquad(\rho=1,3).
$$

Use the pointwise Fejer bound

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac{1}{H^2\|t\|^2}\right).
$$

For the first leg, define

$$
A(\eta)
=
\#\{d\asymp D:\|X/d\|\le \eta\}.
$$

If $\|X/d\|\le\eta$, then for some integer $m\asymp X/D$,

$$
|X/d-m|\le\eta,
$$

so

$$
|X-md|\le \eta D.
$$

Let $n=md$. For real $X$, the number of integers $n$ with $|n-X|\le C\eta D$ is $O(1+\eta D)$. For each such $n$, the number of possible divisors $d$ is at most $\tau(n)$, hence

$$
A(\eta)\ll_\epsilon (1+\eta D)X^\epsilon.
$$

Using dyadic annuli in $\|X/d\|$ with $\eta_j=2^j/H$ gives

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll_\epsilon
\sum_{j\ge0}2^{-2j}A(2^j/H)
\ll_\epsilon
\sum_{j\ge0}2^{-2j}
\left(1+2^jD/H\right)X^\epsilon.
$$

Since

$$
D/H\asymp X^{1/4},
$$

this yields

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted legs, the condition

$$
\left\|\frac{X/d+\rho}{4}\right\|\le\eta
$$

implies that for some integer $m$,

$$
|X/d+\rho-4m|\le 4\eta,
$$

hence

$$
|X-(4m-\rho)d|\le C\eta D.
$$

Let

$$
n=(4m-\rho)d.
$$

Again there are $O(1+\eta D)$ possible integers $n$ in the interval $|n-X|\le C\eta D$, and for each $n$ the number of $d$ is at most $\tau(n)$, with the congruence restriction $n/d\equiv -\rho\pmod 4$ only reducing the count. The same dyadic-annulus argument gives the shifted residual bound.

This proof is pointwise in $X$. It is not an $L^2$ or RMS argument. It remains conditional on H4 until the source card is committed.

### 6. Official M1 and M2 definitions

For active dyadic $D$ and

$$
H_D\asymp DX^{-1/4},
$$

define

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
$$

and

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
C_h=e(h/4)-e(3h/4).
$$

Then

$$
C_h=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

Assuming

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

define

$$
\beta_{h,H}=\alpha_{h,H}C_h.
$$

Then

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

With this notation,

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

The endpoint M9 target is

$$
\mathcal M_i(D;X)\ll_\epsilon X^{1/4+\epsilon}
\qquad(i=1,2)
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

This remains open.

### 7. M2 paired formulas

Let

$$
B_h(D;X)=\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

For the unscaled sum

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}B_h(D;X),
$$

the raw two-sided formula is

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Since $\beta_{-h}=\beta_h$,

$$
S_2(D;X)
=
\sum_{1\le h\le H_D}
\beta_{h,H_D}
\left(B_h(D;X)+B_{-h}(D;X)\right).
$$

For arbitrary complex weights $w_D(d)$,

$$
B_h(D;X)+B_{-h}(D;X)
=
2\sum_{d\asymp D}w_D(d)\cos(2\pi hX/(4d)).
$$

Hence the complex-weight cosine pairing is

$$
S_2(D;X)
=
2\sum_{1\le h\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)\cos(2\pi hX/(4d)).
$$

Multiplying by the outer factor $4$,

$$
\mathcal M_2(D;X)
=
8\sum_{1\le h\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)\cos(2\pi hX/(4d)).
$$

If the weights are real, then $B_{-h}=\overline{B_h}$, so

$$
B_h+B_{-h}=2\operatorname{Re}B_h,
$$

and

$$
\mathcal M_2(D;X)
=
8\sum_{1\le h\le H_D}
\beta_{h,H_D}\operatorname{Re}B_h(D;X).
$$

Substituting $\beta_h$ gives

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

The $\operatorname{Re}B_h$ shortcut is valid only under real weights. For complex weights the correct paired formula is the cosine formula above.

### 8. Fourth-moment numerator and local expansion

For

$$
S_2(D;t)
=
\sum_{1\le |h|\le H_D}\beta_h
\sum_{d\asymp D}w_d e(ht/(4d)),
$$

the fourth moment expands with phase

$$
\frac{t}{4}
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right).
$$

Let

$$
Q=d_1d_2d_3d_4.
$$

The cleared numerator is

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

Thus the phase is

$$
e\left(\frac{tN}{4Q}\right).
$$

On an interval $I$ of length $\delta$,

$$
\left|
\delta^{-1}\int_I e\left(\frac{tN}{4Q}\right)\,dt
\right|
\ll
\min\left(1,\frac{Q}{\delta |N|}\right)
\ll
\min\left(1,\frac{D^4}{\delta |N|}\right).
$$

For the coherence window

$$
\delta=X^{1/2}/D,
$$

this becomes

$$
\min\left(1,\frac{D^5X^{-1/2}}{|N|}\right).
$$

Therefore `(LFM)` is not just an exact $N=0$ problem. It requires control of the fat band

$$
|N|\ll D^5X^{-1/2}
$$

and weighted tails beyond that band.

### 9. AP lemma and why it is not a proof of M2

The current state records the AP lemma as an internal calculus lemma:

For $F\in C^1(I)$, $|I|=\delta$, and $X_0\in I$,

$$
|F(X_0)|^4
\le
\delta^{-1}\int_I |F|^4
+
4\sup_I|F'|\delta^{1/4}
\left(\int_I |F|^4\right)^{3/4}.
$$

The state also records that AP must be kept separate from any $S_2$ application.

Apply this with $F(t)=S_2(D;t)$ and

$$
\delta=X^{1/2}/D.
$$

A trivial derivative estimate gives

$$
S_2'(D;t)
=
\frac{2\pi i}{4}
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_d\frac{h}{d}e(ht/(4d)).
$$

Using

$$
|\beta_h|\ll 1/|h|,
$$

bounded $w_d$, and $d\asymp D$, we get

$$
\sup_I |S_2'(D;t)|
\ll
\sum_{1\le |h|\le H_D}\sum_{d\asymp D}\frac{|h\beta_h|}{D}
\ll
H_D.
$$

If `(LFM)` were known:

$$
\delta^{-1}\int_I |S_2(D;t)|^4\,dt
\ll_\epsilon X^{1+\epsilon},
$$

then

$$
\int_I |S_2(D;t)|^4\,dt
\ll_\epsilon \delta X^{1+\epsilon}.
$$

The AP lemma would yield

$$
|S_2(D;X_0)|^4
\ll_\epsilon
X^{1+\epsilon}
+
H_D\delta^{1/4}(\delta X^{1+\epsilon})^{3/4}.
$$

Since

$$
H_D\delta
=
(DX^{-1/4})(X^{1/2}/D)
=
X^{1/4},
$$

the second term is also

$$
\ll_\epsilon X^{1+\epsilon}.
$$

Thus AP + `(LFM)` would prove the desired fourth-moment pointwise bound

$$
|S_2(D;X_0)|^4\ll_\epsilon X^{1+\epsilon}.
$$

But AP does not prove `(LFM)`. It only transfers `(LFM)` into pointwise control. At the endpoint $D=X^{1/2}$, `(LFM)` itself is essentially as hard as direct pointwise control because the local interval has length $\delta=1$ and the phase changes by too little to create orthogonality.

### 10. Endpoint degeneracy of the local fourth moment

The state already instructs that endpoint $D=X^{1/2}$ must be split off in any M2 route. Here is the explicit calculation.

For any fourth-moment tuple,

$$
|N|
\le
|h_1|d_2d_3d_4
+
|h_2|d_1d_3d_4
+
|h_3|d_1d_2d_4
+
|h_4|d_1d_2d_3.
$$

Since $|h_i|\le H_D$ and $d_i\asymp D$,

$$
|N|\ll H_DD^3.
$$

With

$$
H_D\asymp DX^{-1/4},
$$

this is

$$
|N|\ll D^4X^{-1/4}.
$$

The local fat-band threshold is

$$
T_{\mathrm{LFM}}=D^5X^{-1/2}.
$$

The ratio is

$$
\frac{T_{\mathrm{LFM}}}{H_DD^3}
\asymp
\frac{D^5X^{-1/2}}{D^4X^{-1/4}}
=
DX^{-1/4}.
$$

At $D=X^{1/2}$,

$$
DX^{-1/4}=X^{1/4},
$$

so

$$
T_{\mathrm{LFM}}\gg H_DD^3.
$$

Therefore all fourth-moment tuples lie in the non-oscillatory local band. The normalized local integral kernel is essentially bounded below by a positive constant for all tuples, not only for exact or near resonances.

Consequences:

1. Exact $N=0$ taxonomy is insufficient for endpoint `(LFM)`.
2. Thin near-collision taxonomy with threshold $D^4/X$ is much too small for local AP.
3. The endpoint cannot be handled by absolute local spacing alone.
4. A pointwise signed estimate, a different local window mechanism, or a different endpoint decomposition is needed.

This is a safe new obstruction to add to the proof graph.

### 11. Terminology reconciliation

Use the following terminology in the proof draft.

**Pair-equality.** Exact fraction equality in conjugate positions, such as

$$
\frac{h_1}{d_1}=\frac{h_2}{d_2},
\qquad
\frac{h_3}{d_3}=\frac{h_4}{d_4}.
$$

This is a fraction-level condition, not necessarily a denominator-pattern condition.

**Denominator-paired.** The denominator pattern

$$
d_1=d_2=a,
\qquad
d_3=d_4=b.
$$

The exact resonance equation is

$$
(h_1-h_2)b+(h_3-h_4)a=0.
$$

**Pair-swapped.** The denominator pattern

$$
d_1=d_4=a,
\qquad
d_2=d_3=b.
$$

The exact resonance equation is

$$
(h_1-h_4)b+(h_3-h_2)a=0.
$$

**Denominator-pattern semi-diagonal.** Reserve "semi-diagonal" for

$$
d_1=d_3=a,
\qquad
d_2=d_4=b.
$$

Then exact resonance is

$$
\frac{h_1+h_3}{a}
=
\frac{h_2+h_4}{b},
$$

or equivalently

$$
b(h_1+h_3)=a(h_2+h_4).
$$

This is the official denominator-pattern semi-diagonal family in the Round 6 prompt.

**Fraction-matching / fraction-collision.** Use this term for

$$
\frac{h_1}{d_1}=\frac{h_2}{d_2},
\qquad
\frac{h_3}{d_3}=\frac{h_4}{d_4},
$$

or analogous exact rational-pair collisions, without asserting any denominator pattern.

**Mixed.** Use this as a temporary bin for exact resonances satisfying one named relation plus another nonmatching relation, or overlaps among denominator and fraction patterns not yet assigned.

**Unclassified.** Exact $N=0$ tuples not covered by the named bins after applying the current classification rules.

The state should not identify fraction-matching with denominator-pattern semi-diagonal. The Round 5 patch already records that this terminology is unsafe.

## Theorem-dependency audit

### Vaaler

Vaaler's article metadata is verified by AMS: Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12 (1985), 183--216, DOI `10.1090/S0273-0979-1985-15349-2`.

The local rendered PDF supplies the mathematical source for Theorem 6 and Theorem 18. The H4 source card still must transcribe the exact theorem/equation statements and notation translation before `H4` can move beyond `source_audit_required`. The state already records this requirement, including Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, and $\Phi$ regularity.

Status: `source_audit_required`.

### H4-to-beta algebra

The beta algebra depends on the H4 coefficient convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
$$

Once this convention is fixed, the computation of

$$
\beta_{h,H}=\alpha_{h,H}(e(h/4)-e(3h/4))
$$

is internal algebra. Until H4 is validated, this remains `derived_under_assumptions`.

### R5-Full

R5 uses H4 plus elementary product counting. It does not require Li--Yang, Huxley, Bombieri--Iwaniec, or exponent-pair technology.

Status: `derived_under_assumptions`, blocked by `H4-source-audit`.

### AP lemma

The AP lemma is a pure calculus statement. It is already recorded as `proved_internal` in the state. Its use in `M9-M2` is conditional on `(LFM)`, which remains open.

### LFM

The current state defines `M9-M2-local-fourth-moment-LFM` as open and requires proof on every interval of length $\delta=X^{1/2}/D$, with the fattened band $|N|\ll D^5X^{-1/2}$ and endpoint handling. This response sharpens the endpoint obstruction for that obligation.

### Li--Yang

Li--Yang's arXiv page identifies the paper as arXiv:2308.14859v2, last revised 14 September 2023, by Xiaochun Li and Xuerui Yang; the abstract says it uses the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results. The local PDF states Theorem 1.2 with

$$
R(X)=O_\epsilon(X^{\theta^*+\epsilon}),
\qquad
\Delta(X)=O_\epsilon(X^{\theta^*+\epsilon}),
\qquad
\theta^*=0.314483\cdots.
$$

This is useful literature calibration only. It is not imported as a black-box dependency for `M9`, and the current state keeps `Li-Yang-source-audit` as `source_audit_required`.

### GitHub/source freshness caveat

The pasted state bundle is treated as authoritative for this Stage A run. I did not use the public GitHub repo to override the pasted state. Web search verified bibliographic metadata, not the latest repository files.

## Hidden assumptions and potential gaps

1. **Physical source-card gap.** The source-card draft above is not a committed file. `H4` should remain `source_audit_required`.

2. **Vaaler convention gap.** The project must explicitly distinguish $\psi_V(n)=0$ from $\psi_F(n)=-1/2$. Omitting this convention risks a half-jump sign error at integer arguments.

3. **Coefficient sign gap.** The sign in

$$
   \alpha_{h,H}
   =
   -\frac{\Phi(|h|/(H+1))}{2\pi i h}
$$

must be checked against Theorem 18's coefficient formula. A sign flip would change $\beta_h$ and the paired formula.

4. **Integer height gap.** The proof draft should say that $H_D$ is a fixed integer chosen per dyadic block and base point $X_0$. Differentiating $H_D(t)$ is not part of the analytic setup.

5. **AP misuse gap.** AP converts `(LFM)` into pointwise control. It does not prove `(LFM)`. Treating AP as proof of M2 is exactly the error rejected in Round 5.

6. **Endpoint LFM gap.** At $D=X^{1/2}$, local averaging over $\delta=1$ gives essentially no oscillatory cancellation. A separate endpoint argument is mandatory.

7. **Absolute fourth-moment gap.** Even away from the endpoint, an absolute weighted count with kernel

$$
   \min\left(1,\frac{D^5X^{-1/2}}{|N|}\right)
$$

may be too large. Signed coefficient structure may be necessary.

8. **Unpaired exact resonance gap.** Paired/fraction-matching families do not exhaust exact $N=0$.

9. **Complex weights gap.** The $\operatorname{Re}B_h$ formula is invalid for complex weights. Diagnostics must include the raw two-sided formula and the complex-weight cosine formula.

10. **Li--Yang theorem-application gap.** Li--Yang's $S/H$ theorem and Case A/B hypotheses must be audited before any theorem import. Broad phase similarity is not enough.

## Counterexample or obstruction search

### Obstruction 1: endpoint local fourth moment has no spacing gain

At $D=X^{1/2}$,

$$
H_D=X^{1/4},
\qquad
\delta=1.
$$

For all fourth-moment tuples,

$$
|N|\ll H_DD^3=X^{1/4}X^{3/2}=X^{7/4}.
$$

The local fat-band threshold is

$$
D^5X^{-1/2}=X^{5/2}X^{-1/2}=X^2.
$$

Thus every tuple is in the local non-oscillatory band. This is a decisive obstruction to any endpoint proof based only on excluding large $N$.

### Obstruction 2: absolute local fourth moment is too large at endpoint

At $D=X^{1/2}$ and $H=X^{1/4}$, the absolute coefficient mass of $S_2$ is roughly

$$
\sum_{1\le |h|\le H}|\beta_h|\sum_{d\asymp D}1
\asymp
D\log H.
$$

The absolute fourth-power scale is then roughly

$$
D^4(\log H)^4
\asymp
X^2(\log X)^4,
$$

well above the desired fourth-moment scale $X^{1+\epsilon}$. This does not show the true signed fourth moment is large, but it shows absolute estimates cannot close the endpoint.

### Obstruction 3: thin DP near-collision does not address LFM fat band

The denominator-paired near-collision state uses a thin band of the type

$$
0<|N|\le C_0D^4/X.
$$

For LFM, the relevant band is

$$
0<|N|\ll D^5X^{-1/2}.
$$

The ratio is

$$
\frac{D^5X^{-1/2}}{D^4/X}
=
DX^{1/2}.
$$

In the active range this is at least $X^{3/4}$ and can be $X$. Thus thin near-collision scoping is not enough for AP/LFM.

### Obstruction 4: Cauchy sign erasure remains

Any route beginning with

$$
|S_2|^2
\le
\left(\sum_h |\beta_h|\right)
\left(\sum_h |\beta_h||B_h|^2\right)
$$

replaces the $\chi_4(h)$ sign by $|\chi_4(h)|$, leaving only odd support. This is a diagnostic, not a universal impossibility theorem, but it blocks character-blind routes.

### Obstruction 5: continuous rational-frequency orthogonality remains false

Do not revive the rejected continuous $L^4$ route where

$$
\int_0^1 e(\alpha \theta)\,d\alpha
$$

is treated as zero for arbitrary nonzero rational $\theta$. It is not. Exact resonance requires an integer-frequency kernel built from the cleared numerator $N$, not arbitrary rational phase orthogonality.

## Verification

### Verification of $\Phi$ endpoint values

From the expansions above:

$$
\Phi(u)=1-\frac{\pi^2u^2}{3}+O(u^3)
\qquad(u\to0+),
$$

so

$$
\Phi(0)=1,\qquad \Phi'(0)=0.
$$

Also

$$
\Phi(1-v)=\frac{\pi^2v^2}{3}+O(v^3)
\qquad(v\to0+),
$$

so

$$
\Phi(1)=0,\qquad \Phi'(1)=0.
$$

Thus $\Phi$ has no endpoint singularity relevant to coefficient freezing.

### Verification of R5 count

For the first leg, the count

$$
\#\{d\asymp D:\|X/d\|\le \eta\}
\ll_\epsilon (1+\eta D)X^\epsilon
$$

follows by mapping to integer products $n=md$ with $|n-X|\ll\eta D$ and applying $\tau(n)\ll_\epsilon n^\epsilon$.

For the shifted leg, the same proof uses

$$
n=(4m-\rho)d.
$$

The congruence condition only reduces divisor multiplicity.

### Verification of M2 beta parity

For odd $h$,

$$
e(h/4)-e(3h/4)=2i\chi_4(h).
$$

For even $h$, both exponentials are equal, so the difference is zero. Multiplication by

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}
$$

gives

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)1_{2\nmid h},
$$

which is real and even.

### Verification of AP scaling

Assume `(LFM)`:

$$
\delta^{-1}\int_I |S_2|^4\ll_\epsilon X^{1+\epsilon}.
$$

Then the AP derivative term is

$$
\ll
H_D\delta^{1/4}(\delta X^{1+\epsilon})^{3/4}
=
H_D\delta X^{3/4+\epsilon}
=
X^{1+\epsilon}.
$$

So AP has the correct formal scale. The gap is entirely in proving `(LFM)` uniformly.

### Verification of endpoint degeneracy

The local kernel discriminates by $|N|$ only when

$$
|N|\gg D^5X^{-1/2}.
$$

At the endpoint, all tuples satisfy

$$
|N|\ll X^{7/4}\ll X^2=D^5X^{-1/2}.
$$

Thus no tuple is in the oscillatory regime. This is a direct scale calculation.

## Divergent alternatives and 20% exploration

### Alternative A: use a longer local window at the endpoint

One might try to take $\delta>X^{1/2}/D$ at $D=X^{1/2}$ to force oscillation. The maximum frequency in the endpoint block is

$$
\left|\frac{N}{D^4}\right|
\ll
\frac{X^{7/4}}{X^2}
=
X^{-1/4}.
$$

To see oscillation, one needs

$$
\delta\gg X^{1/4}.
$$

But the AP derivative term scales like

$$
H_D\delta X^{3/4}
=
X^{1/4}\delta X^{3/4}
=
\delta X.
$$

For $\delta\gg1$, this already exceeds the target $X^{1+\epsilon}$ unless a stronger derivative or local regularity estimate replaces the trivial derivative bound. Thus longer windows do not solve the endpoint with the present AP lemma.

Needed lemma:

$$
|S_2(D;X_0)|^4
\ll
\delta^{-1}\int_I |S_2|^4
+
\text{smaller derivative loss}
$$

with derivative loss $o(\delta X)$ at $D=X^{1/2}$. I do not see such a lemma from elementary calculus alone.

Fast falsification: numerically compare local sup and local average over endpoint windows of length $1$, $X^{1/8}$, and $X^{1/4}$. If local sup persists and derivative variation dominates, discard longer-window AP.

### Alternative B: endpoint B-process or stationary transform

At $D=X^{1/2}$, the phase for fixed $h$ is

$$
f(d)=\frac{hX}{4d}.
$$

The first derivative scale is

$$
|f'(d)|\asymp \frac{hX}{D^2}.
$$

At $D=X^{1/2}$ and $h\le H_D=X^{1/4}$,

$$
|f'(d)|\asymp h.
$$

A B-process in $d$ has dual length approximately $hX/D^2\asymp h$, hence up to $X^{1/4}$ at the top $h$. This is not a one-term dual sum. Any claim of endpoint collapse to length $1$ is wrong under this normalization.

Needed lemma: a B-process formula for

$$
\sum_{d\asymp D}w(d)e(hX/(4d))
$$

uniformly in $1\le h\le H_D$, including boundary stationary points and amplitudes, followed by a signed sum over $h$ preserving $\chi_4(h)$.

Fast falsification: if the transformed $h$-sum becomes sign-blind after the first Cauchy or large-sieve step, this route does not address the M2 character obstruction.

### Alternative C: integer-frequency kernel for exact rational resonance

The rejected continuous rational orthogonality can be repaired only by using the cleared numerator $N$. For example, use a Fejer kernel in an auxiliary variable $\alpha$:

$$
\mathcal K_L(N)
=
\sum_{|r|\le L}
\left(1-\frac{|r|}{L+1}\right)e(r\alpha N),
$$

integrated over $\alpha\in[0,1]$, so that integer orthogonality detects $N=0$.

Needed lemma: choose $L$ and weights so that the resulting integer-frequency exact detector or near-detector controls the actual fourth moment without introducing a loss worse than $X^{1+\epsilon}$.

Likely obstruction: detecting $N=0$ exactly does not control endpoint local fourth moments because the endpoint local band contains all $N$, not only $0$.

Fast falsification: apply the integer detector to endpoint blocks. If exact $N=0$ is small but the local fourth moment remains large, exact orthogonality is not the right local tool.

### Alternative D: smoothed radial cutoff before hyperbola

A smoothed circle cutoff could reduce pointwise endpoint sensitivity by moving from sharp $P(X)$ to a smoothed discrepancy. This would naturally yield averaged exponential sums. However, unsmoothing back to the sharp circle error at exponent $1/4+\epsilon$ is itself a hard endpoint problem.

Needed lemma: a smoothing/unsmoothing theorem with smoothing radius small enough to preserve $X^{1/4+\epsilon}$ and error terms controlled uniformly.

Likely obstruction: the boundary layer of a circle of radius $\sqrt X$ has area roughly proportional to smoothing width times $\sqrt X$, which quickly exceeds $X^{1/4}$ unless the smoothing is extremely fine.

Fast falsification: compute the unsmoothing loss for a window of size $\Delta X$ in the $X$ variable. If the geometric boundary-layer error is $\gg X^{1/4}$, this route cannot be the main proof.

## Useful lemmas

### Lemma A: $\Phi$ regularity under H4

Assume

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u
\qquad(0<u<1).
$$

Then $\Phi$ extends to $C^1([0,1])$ with

$$
\Phi(0)=1,\quad \Phi(1)=0,\quad \Phi'(0)=\Phi'(1)=0.
$$

In particular $\Phi$ is Lipschitz on $[0,1]$.

Status recommendation: `derived_under_assumptions`, depending on `H4-source-audit`.

### Lemma B: fixed-height freezing on local windows

Let

$$
H=H_D(X_0)\asymp DX_0^{-1/4}
$$

and

$$
I=[X_0-O(X_0^{1/2}/D),X_0+O(X_0^{1/2}/D)].
$$

Then for $t\in I$,

$$
D t^{-1/4}\asymp D X_0^{-1/4},
$$

and the continuous height changes by $O(DX_0^{-1})\le O(X_0^{-1/2})$. Thus one may use the same integer Vaaler height $H$ throughout the local AP/LFM argument.

Status recommendation: `proved_internal` as bookkeeping, or include inside `H4-Phi-regularity`.

### Lemma C: R5 pointwise product-count lemma

For $H\asymp DX^{-1/4}$,

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}
$$

and

$$
\frac1H\sum_{d\asymp D}K_H((X/d+\rho)/4)
\ll_\epsilon X^{1/4+\epsilon},
\qquad \rho\in\{1,3\}.
$$

Status: already `derived_under_assumptions` through `R5-Full`, pending H4.

### Lemma D: local fourth-moment kernel

For $I$ of length $\delta$,

$$
\left|
\delta^{-1}\int_I e\left(\frac{tN}{4d_1d_2d_3d_4}\right)\,dt
\right|
\ll
\min\left(1,\frac{D^4}{\delta |N|}\right).
$$

With $\delta=X^{1/2}/D$, the fat band is

$$
|N|\ll D^5X^{-1/2}.
$$

Status recommendation: `proved_internal`.

### Lemma E: endpoint LFM degeneracy

At $D\asymp X^{1/2}$, every fourth-moment tuple lies inside the local fat band:

$$
|N|\ll H_DD^3\asymp X^{7/4}
\ll X^2\asymp D^5X^{-1/2}.
$$

Therefore the local fourth-moment kernel gives no $N$-spacing gain at the endpoint.

Status recommendation: create as `M9-M2-LFM-endpoint-degeneracy`, `proved_internal`, scoped as an obstruction to absolute local-spacing proofs.

## What should be tested next

1. **Rendered H4 transcription.** Confirm line-by-line from the rendered Vaaler PDF:
   - Theorem 6, equation (2.28), for $\widehat J$;
   - Section 7, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, equations (7.13)--(7.17), especially (7.14);
   - coefficient sign;
   - residual constant;
   - Fejer normalization;
   - integer convention.

2. **Source-card materialization.** Commit `sources/vaaler_1985.md` with the draft content above and mark any unresolved transcription uncertainty.

3. **Proof-draft insertion.** Insert H1--H3, H4, R5, M1/M2 definitions, paired formulas, $N$, AP, `(LFM)`, and the endpoint-degeneracy note into `state/best_proof_draft.md`.

4. **Endpoint LFM diagnostics.** At $D=X^{1/2}$, compute local fourth moments on intervals of lengths $1$, $X^{1/8}$, and $X^{1/4}$ for true $\beta$, $|\beta|$, random signs, and adversarial signs.

5. **Unpaired exact $N=0$ enumeration.** Test whether fraction-matching/fraction-collision accounts for previously unclassified exact mass.

6. **Complex-weight regression.** Verify:
   - raw two-sided M2 equals complex-weight cosine pairing;
   - real-weight paired formula agrees for real weights;
   - $\operatorname{Re}B_h$ fails for deliberately complex weights.

7. **R5 stress tests.** Run product-count residual diagnostics for:
   - first leg;
   - shifted $\rho=1,3$ legs;
   - integer and noninteger $X$;
   - square, near-square, nonsquare, and divisor-rich $X$;
   - $D=X^{1/4}$, $X^{3/8}$, $X^{1/2}$.

8. **Signed/SPD statistic.** Define and compute a first reciprocal-spacing statistic that preserves $\chi_4(h)$. Compare true signs to unsigned/adversarial signs.

## Proposed state patch, if any

proof_obligations:
  create:
    - id: "H4-Phi-regularity"
      type: "lemma"
      track: "source_audit"
      title: "Regularity of Vaaler's Phi coefficient function"
      status: "derived_under_assumptions"
      statement_tex: "Assuming Vaaler's Theorem 6 formula Phi(u)=pi u(1-u)cot(pi u)+u for 0<u<1, Phi extends to a C^1 function on [0,1] with Phi(0)=1, Phi(1)=0, Phi'(0)=Phi'(1)=0, and sup_[0,1] |Phi'(u)|<infty. Hence Phi is Lipschitz on [0,1], sufficient for coefficient-stability bookkeeping when H_D is frozen or compared across local windows of length delta=X^(1/2)/D."
      dependencies:
        - "H4-source-audit"
      implies:
        - "H4"
        - "M9-M2-local-fourth-moment-LFM"
      blockers:
        - "H4-source-audit"
      evidence:
        positive: []
        negative: []
        inconclusive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
      owner: "A1"
      next_action: "After H4 source-card validation, move the calculus part into the lemma bank and cite it in the proof-draft discussion of freezing H_D on local windows."

- id: "M9-M2-local-fourth-moment-kernel"
      type: "lemma"
      track: "M9_analytic"
      title: "Local fourth-moment kernel and fattened N-band"
      status: "proved_internal"
      statement_tex: "For S_2(D;t) expanded to fourth moment over an interval I of length delta, the normalized local integral of a tuple with cleared numerator N and denominator product Q=d_1d_2d_3d_4 satisfies |I|^(-1)|int_I e(tN/(4Q))dt| << min(1,D^4/(delta |N|)). For delta=X^(1/2)/D this gives the fat band |N| << D^5 X^(-1/2)."
      dependencies:
        - "M9-M2-fourth-moment-expansion"
      implies:
        - "M9-M2-local-fourth-moment-LFM"
        - "M9-M2-fourth-moment-average-to-pointwise"
      blockers: []
      evidence:
        positive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
        negative: []
        inconclusive: []
      owner: "A1"
      next_action: "Use this kernel in any LFM proof attempt; distinguish it from the thinner global near-collision band D^4/X."

- id: "M9-M2-LFM-endpoint-degeneracy"
      type: "obstruction"
      track: "M9_analytic"
      title: "Endpoint degeneration of local fourth-moment spacing"
      status: "proved_internal"
      statement_tex: "At D asymp X^(1/2), H_D asymp X^(1/4), and delta=X^(1/2)/D asymp 1, every fourth-moment tuple has |N| << H_D D^3 asymp X^(7/4), while the LFM fat-band threshold is D^5 X^(-1/2) asymp X^2. Thus the local fourth-moment kernel gives no N-spacing discrimination at the endpoint. This is a scoped obstruction to proving LFM by absolute local N-spacing alone, not a disproof of LFM."
      dependencies:
        - "M9-M2-local-fourth-moment-kernel"
        - "M9-endpoint-uniformity"
      implies:
        - "M9-M2-local-fourth-moment-LFM"
        - "M9-M2-fourth-moment-average-to-pointwise"
        - "M9-endpoint-uniformity"
      blockers: []
      evidence:
        positive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
        negative: []
        inconclusive: []
      owner: "A1"
      next_action: "Require any LFM route to split off D asymp X^(1/2) or supply a signed endpoint estimate not based solely on absolute N-spacing."

update:
    - id: "H4-source-audit"
      status: "source_audit_required"
      evidence_added:
        inconclusive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
      next_action: "Commit sources/vaaler_1985.md with bibliographic data, DOI 10.1090/S0273-0979-1985-15349-2, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, and the Phi regularity calculation."

- id: "M9-M2-local-fourth-moment-LFM"
      status: "open"
      blockers_added:
        - "M9-M2-LFM-endpoint-degeneracy"
      evidence_added:
        inconclusive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
      next_action: "Prove the local fourth-moment estimate with the kernel min(1,D^5 X^(-1/2)/|N|), but split off D asymp X^(1/2) since the endpoint local window gives no N-spacing gain."

- id: "M9-M2-fourth-moment-average-to-pointwise"
      status: "open"
      blockers_added:
        - "M9-M2-local-fourth-moment-kernel"
        - "M9-M2-LFM-endpoint-degeneracy"
      evidence_added:
        inconclusive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
      next_action: "Keep AP as a calculus interpolation module. Any application to S2 must prove LFM on every coherence window and supply a separate endpoint mechanism."

- id: "M9-M2-beta-algebra"
      status: "derived_under_assumptions"
      evidence_added:
        inconclusive:
          - "rounds/obligation-main/round_006/responses/A1-006.md"
      next_action: "After H4 source-card validation, insert the beta_h formula, raw two-sided M2 formula, complex-weight cosine pairing, and real-weight Re B_h formula into best_proof_draft.md."

no_change:
    - id: "M9"
      reason: "No uniform endpoint estimate for both M1 and M2 is proved."
    - id: "M9-M1"
      reason: "This response does not estimate M1."
    - id: "M9-M2"
      reason: "AP plus LFM would imply pointwise M2, but LFM remains open and endpoint-degenerate for spacing-only proofs."
    - id: "M9-near-collision-taxonomy"
      reason: "Terminology is clarified, but mixed and unclassified exact N=0 remain open."
    - id: "M9-near-collision-estimate"
      reason: "No full weighted near-collision estimate is proved."
    - id: "GC-target"
      reason: "The final target remains conditional on M9."
    - id: "H4"
      reason: "H4 remains source_audit_required until the Vaaler source card is physically updated and validated."

## Confidence

High confidence in the $\Phi$ endpoint expansions and Lipschitz conclusion, conditional on the Vaaler formula.

High confidence in the R5 positive-Fejer product-count proof structure, conditional on H4.

High confidence in the raw/two-sided and paired $\mathcal M_2$ algebra, conditional on the H4 coefficient convention.

High confidence in the local fourth-moment kernel calculation and the endpoint-degeneracy scale calculation.

Moderate confidence that `M9-M2-LFM-endpoint-degeneracy` should be added as a new proved internal obstruction. The statement must remain scoped: it blocks absolute local $N$-spacing as a complete endpoint proof, not all possible LFM proofs.

Moderate confidence that the direct signed/SPD route is the right backup after the endpoint LFM obstruction, but there is no theorem-level signed spacing estimate yet.

Low confidence that current absolute fourth-moment taxonomy alone can prove `M9-M2`.

No new Gauss circle exponent is proved.

--- OUTPUT FROM A3 ---
## Summary

This report performs a rigorous algebra audit for the M2 reciprocal sum, its paired formulations, the fourth-moment taxonomy, and the local fourth-moment obstruction targeted in Round 6. It produces a detailed diagnostic-bundle plan (scripts, commands, expected outputs) that the local orchestrator can materialize and execute. The audit confirms the beta-coefficient identity, catches a subtle sign in the real-weight pairing, isolates the exact N-macro and its computing requirements, and supplies a small reproducible numeric check. All proposed computations remain `diagnostic_only`.

## Target proof obligation

We target three obligations from `state/proof_obligations.yml`:

- **M9-regression-raw-vs-paired** -- Validate raw two-sided M2, complex-weight cosine pairing, real-weight paired formula, and verify that `Re B_h` fails for complex weights.
- **M9-fourth-moment-enumeration** -- Enumerate exact N=0 and near-collision M2 fourth-moment tuples, classify them, and output signed/absolute masses.
- **M9-M2-local-fourth-moment-LFM** -- Compute local fourth-moment averages on windows of length $\delta=X^{1/2}/D$, compare with global averages, and probe the fattened resonance band $|N|\ll D^5 X^{-1/2}$.

The auxiliary signed-vs-unsigned/SPD diagnostics are also covered.

## Main claim or direction

The main technical claim is that **the M2 sum's real-weight pairing and the fourth-moment integer-numerator machinery are algebraically sound, but the transition from global fourth-moment heuristics to a pointwise $O_\epsilon(X^{1/4+\epsilon})$ bound via local-fourth-moment averages is far from automatic**; computational stress tests must reveal whether the local-fourth-moment estimate fails catastrophically in certain windows, especially near the endpoint $D=X^{1/2}$.

We will therefore:

1. Audit the exact beta-coefficient algebra and the paired formulas.
2. Design a comprehensive executable bundle that enumerates exact N=0 and near-collision tuples, classifies them into the accepted taxonomy, and measures signed and unsigned fourth-moment masses.
3. Build a local-fourth-moment diagnostic that sweeps many windows and flags exceptional windows.
4. Provide a small manual numeric check to verify the basic formulas.
5. Frame the output as a diagnostic report that the judge and other agents can use to guide proof strategy.

## Detailed reasoning

### 1. Beta-coefficient audit

From the obligation `M9-M2-beta-algebra` (status `derived_under_assumptions`) we have

$$
\alpha_{h,H} = -\frac{\Phi(|h|/(H+1))}{2\pi i h},\qquad
\beta_{h,H} = \alpha_{h,H}\bigl(e(h/4)-e(3h/4)\bigr),
$$

where $\Phi(u)$ is the Vaaler kernel.

Compute the character factor:

$$
e(h/4)-e(3h/4)=e^{-i\pi h/2}\bigl(e^{i\pi h/2}-e^{i3\pi h/2}\bigr) = 2i\,e^{-i\pi h/2}\sin(\pi h/2).
$$

When $h$ is even, $\sin(\pi h/2)=0$. For odd $h$, $\sin(\pi h/2)=(-1)^{(h-1)/2}$. Thus

$$
e(h/4)-e(3h/4) = 2i\,(-1)^{(h-1)/2} e^{-i\pi h/2},\qquad (h\text{ odd}).
$$

Multiplying by $\alpha_h$ gives

$$
\beta_{h,H} = -\frac{\Phi(|h|/(H+1))}{2\pi i h}\cdot 2i\,(-1)^{(h-1)/2} e^{-i\pi h/2} = -\frac{\Phi(|h|/(H+1))}{\pi h}\,(-1)^{(h-1)/2} e^{-i\pi h/2}.
$$

Using $e^{-i\pi h/2}=(-i)^{h}$? Better: note that $\chi_4(h)=(1/h)\bigl(e(h/4)-e(3h/4)\bigr)/(2i)$? Actually the standard non-trivial Dirichlet character mod 4 is

$$
\chi_4(n)=\begin{cases}
0 & n\text{ even},\\
1 & n\equiv 1\pmod 4,\\
-1 & n\equiv 3\pmod 4.
\end{cases}
$$

One can check

$$
e(n/4)-e(3n/4)=2i\,\chi_4(n)\cdot(-1)^{(n-1)/2}?
$$

Let's verify numerically: for $n=1$, $e(1/4)-e(3/4)=e^{i\pi/2}-e^{3i\pi/2}=i-(-i)=2i$. $\chi_4(1)=1$. So RHS $2i\cdot1=2i$. OK. For $n=3$: $e(3/4)-e(9/4)=e^{3i\pi/2}-e^{i\pi/2}=-i-i=-2i$. $\chi_4(3)=-1$, RHS $2i\cdot(-1)=-2i$. So indeed

$$
e(n/4)-e(3n/4)=2i\,\chi_4(n),\qquad (n\text{ odd}).
$$

No extra $(-1)^{(n-1)/2}$ factor. My earlier sine expansion overlooked that the sign of $\sin(\pi n/2)$ for odd $n$ is exactly $\chi_4(n)$ times $(-1)^{(n-1)/2}$? Let's recompute: $\sin(\pi n/2)$ for $n=1$ is $\sin(\pi/2)=1$, for $n=3$ is $\sin(3\pi/2)=-1$, for $n=5$ is $\sin(5\pi/2)=1$, etc. So $\sin(\pi n/2) = (-1)^{(n-1)/2}$ for odd $n$? For $n=1$, $(1-1)/2=0$, $(-1)^0=1$. For $n=3$, $(3-1)/2=1$, $(-1)^1=-1$. So $\sin(\pi n/2) = (-1)^{(n-1)/2}$. Then $e^{i\pi n/2}=i^n$. The difference $e^{i\pi n/2}-e^{3i\pi n/2}=e^{i\pi n/2}(1-e^{i\pi n}) = e^{i\pi n/2}(1-(-1)^n)$. For odd $n$, this is $2 e^{i\pi n/2}$. Then $e^{i\pi n/2}=i^n$. For $n=1$, $i$; for $n=3$, $i^3=-i$. So $2i$ and $-2i$ respectively, which matches $2i\chi_4(n)$. So indeed $2i\chi_4(n)$. Thus the beta-coefficient identity simplifies to

$$
\beta_{h,H} = -\frac{\Phi(|h|/(H+1))}{2\pi i h}\cdot 2i\,\chi_4(h) = -\frac{\Phi(|h|/(H+1))}{\pi h}\,\chi_4(h),\qquad h\text{ odd}.
$$

For $h$ even, $\beta_{h,H}=0$. Since $\chi_4(h)$ is real and $\Phi$ is real, $\beta_{h,H}$ is **real**. Moreover $\beta_{-h,H}=\beta_{h,H}$ because $\chi_4(-h)=\chi_4(h)$ and $|{-h}|=|h|$. This matches the statement in `M9-M2-beta-algebra` (except that the statement says $\beta_{h,H} = -\Phi(|h|/(H+1)) \chi_4(|h|) 1_{2\not\mid h}/(\pi |h|)$, which is identical after noting $\chi_4(|h|)=\chi_4(h)$ for $h>0$). So the algebra is **correct**.

**Crucial consequence:** $\beta_{h,H}$ is real and even. Therefore for a complex inner sum $B_h = \sum_{d} w_D(d) e(hX/(4d))$, we have

$$
S_2 = \sum_{1\le |h|\le H} \beta_h B_h
      = \sum_{h=1}^H \beta_h (B_h + B_{-h}).
$$

If the weight $w_D$ is real, $B_{-h} = \overline{B_h}$. Hence $S_2 = \sum_{h=1}^H 2\beta_h \operatorname{Re}(B_h)$. This is the **real-weight paired formula**. It fails when $w_D$ is complex because then $B_{-h}$ is not the conjugate of $B_h$. The diagnostics must confirm this failure.

### 2. M2 raw two-sided formula

The raw two-sided formula is simply

$$
S_2^{\text{raw}}(D;X) = \sum_{h=-H}^{-1} \beta_h B_h + \sum_{h=1}^{H} \beta_h B_h.
$$

Given that $\beta_{-h}=\beta_h$, this is identical to the paired form when $B_{-h}=\overline{B_h}$. In code we implement both and cross-check.

### 3. Fourth-moment expansion

For the two-sided sum, the fourth power expands to

$$
|S_2|^4 = \sum_{h_1,\dots,h_4} \beta_{h_1}\beta_{h_2}\overline{\beta_{h_3}}\overline{\beta_{h_4}} \;
          \sum_{d_1,\dots,d_4} w_D(d_1)w_D(d_2)\overline{w_D(d_3)}\overline{w_D(d_4)} \;
          e\!\left(\frac{X}{4}\Bigl(\frac{h_1}{d_1}+\frac{h_2}{d_2}-\frac{h_3}{d_3}-\frac{h_4}{d_4}\Bigr)\right).
$$

The exponent's argument simplifies to $\frac{X}{4}\frac{N}{\Delta}$ where $\Delta = d_1d_2d_3d_4$ and

$$
N = h_1 d_2 d_3 d_4 - h_2 d_1 d_3 d_4 + h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3.
$$

This is the integer numerator from `M9-M2-fourth-moment-expansion`. Note the signs: first and third terms positive, second and fourth negative. This matches the alternating sum $h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4$ after clearing denominators. **We must verify that the sign pattern in the expansion matches the actual complex conjugate placement.** In $|S_2|^2 = S_2 \overline{S_2}$, we get a double sum with terms $e(\frac{X}{4}(h_1/d_1 - h_2/d_2))$. Squaring again yields $e(\frac{X}{4}(h_1/d_1 - h_2/d_2 + h_3/d_3 - h_4/d_4))$. So the sign pattern is correct. The coefficient product is $\beta_{h_1}\beta_{h_2}\overline{\beta_{h_3}}\overline{\beta_{h_4}}$. Since $\beta_h$ is real, this equals $\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}$. **Hence the fourth-moment coefficient is purely a product of real numbers; there is no residual phase.** This is an important simplification: the exact N=0 mass depends only on $\beta_h$ magnitude, not on sign cancellations from complex coefficients. However, the sign of $\beta_h$ still matters when we later combine with the near-collision phases; for exact N=0, the exponential factor is $1$, so only the product of $\beta$'s matters (and the sign can cause cancellations between different tuples, but the taxonomy usually bounds absolute value). The diagnostic will compute both signed and unsigned masses.

### 4. Taxonomy of exact N=0 configurations

We adopt the categories listed in the obligations, with precise definitions:

- **Pair-equality (PE)**: $h_1=h_3$, $d_1=d_3$, $h_2=h_4$, $d_2=d_4$.
- **Denominator-paired (DP)**: $d_1=d_2=a$, $d_3=d_4=b$; then $N=ab[(h_1-h_2)b+(h_3-h_4)a]$. N=0 reduces to a linear equation in $h$'s.
- **Pair-swapped (PS)**: $h_1=h_4$, $d_1=d_4$, $h_2=h_3$, $d_2=d_3$.
- **Official denominator-pattern semi-diagonal (SD-official)**: $d_1=d_3$, $d_2=d_4$, together with the equation $d_2(h_1+h_3)=d_1(h_2+h_4)$ (from the N=0 condition after simplification? Need to derive.)
- **Fraction-matching (FM)**: $h_1/d_1 = h_2/d_2$ and $h_3/d_3 = h_4/d_4$.
- **Mixed**: tuples that satisfy N=0 but belong to none of the above "simple" families.
- **Unclassified**: any remaining N=0 tuple not caught by the implemented classifiers (should be empty if taxonomy is exhaustive over the enumerated set).

We must implement classifiers that assign each $(h_1,\dots,d_4)$ to a unique category (or first-match priority). The taxonomy in `M9-near-collision-taxonomy` is still open, so our classification will serve as diagnostic data.

### 5. Local fourth-moment (LFM) diagnostics

The AP lemma (from `M9-M2-average-to-pointwise-AP-lemma`) states that for $F\in C^1$ on an interval $I$ of length $\delta$,

$$
|F(X_0)|^4 \le \frac{1}{\delta}\int_I |F|^4 \;+\; 4\bigl(\sup_I |F'|\bigr) \delta^{1/4} \Bigl(\int_I |F|^4\Bigr)^{3/4}.
$$

To use it for $S_2(D;\cdot)$, we need a bound for $\sup|F'|$ and an estimate of the local $L^4$ average. The local-fourth-moment hypothesis `(LFM)` asserts

$$
\frac{1}{\delta}\int_I |S_2(D;t)|^4 dt \ll_\epsilon X^{1+\epsilon}
$$

for every interval $I$ of length $\delta = X^{1/2}/D$ near $X$. Our diagnostic will compute this local average by sampling many $X$ points in $I$ and using Riemann sums. Because $S_2$ is a smooth function (assuming smooth $w_D$), the integral can be approximated well.

Key challenge: the derivative $F'(X)$ involves terms $\frac{h}{4d} e(\dots)$ times coefficients, and can be as large as $H/D \approx (D X^{-1/4})/D = X^{-1/4}$, but multiplied by the sum length gives something like $H \cdot D \cdot X^{-1/4} = D^2 X^{-1/2} \le X^{1/2} X^{-1/2} = 1$, so derivative might be $O(1)$ or larger? Actually $S_2$ is a sum of $\approx H\times(\text{support of w})$ terms, each of size $\approx 1/h \cdot 1$. With derivative, each term gets factor $h/d \approx H/D = X^{-1/4}$, so $F'$ could be as large as $H\cdot D \cdot (H/D) = H^2 \approx D^2 X^{-1/2}$. For $D=X^{1/2}$, $H^2 \approx X^{1/2} X^{-1/2} = 1$; for $D=X^{1/4}$, $H^2 \approx X^{1/2} X^{-1/2} = X^0$ times something? Actually $H \approx D X^{-1/4}$, so $H^2 \approx D^2 X^{-1/2}$. At $D=X^{1/4}$, $D^2 X^{-1/2} = X^{1/2} X^{-1/2} = 1$. So derivative may be $O(1)$. But we need the supremum; it could be larger due to cancellation? We'll compute it numerically.

The diagnostic will compute local averages and compare them to the global fourth moment average. We will also flag windows where the local average exceeds a threshold, indicating exceptional windows.

### 6. Near-collision diagnostics

We define two resonance bands:

- **Thin band**: $0 < |N| \le C_{\text{thin}} \cdot D^4 / X$.
- **Fat band** (local): $0 < |N| \le C_{\text{fat}} \cdot D^5 X^{-1/2}$.

Constants $C_{\text{thin}}, C_{\text{fat}}$ will be set to small integers (e.g., 10). The fat band is the one required for the LFM local expansion (since the phase variation over $\delta$ is $\approx \delta \cdot (h/d^2) \cdot h$? Actually the derivative of the phase is $\frac{h}{4d}$, and over a window $\delta$, the phase change is $\frac{h}{4d} \delta$. The fourth moment integration picks up a Dirichlet kernel-like factor from the integration over $X$ in the local window. The cutoff on $N$ emerges from the condition $|N \cdot \delta / (4 \Delta)| \ll 1$ for constructive interference. Indeed the local average involves $\frac{1}{\delta}\int_I e(\frac{X}{4}\frac{N}{\Delta}) dX$, which is a sinc function of $\frac{\delta N}{4\Delta}$. It is significant only when $|N| \lesssim 4\Delta/\delta$. Since $\Delta \approx D^4$, and $\delta = X^{1/2}/D$, this gives $|N| \lesssim 4 D^4 / (X^{1/2}/D) = 4 D^5 / X^{1/2}$. So the fat band is $|N| \ll D^5 X^{-1/2}$. We will verify this heuristic by explicitly computing the local average for a sample window and plotting the contribution vs $N$.

### 7. Signed-vs-unsigned / SPD diagnostics

We will compute the true $S_2$ with actual $\beta_h$, and compare with versions where we replace $\beta_h$ by $|\beta_h|$, random signs, or adversarial signs (e.g., all signs chosen to avoid cancellation). This probes whether the sign pattern $\chi_4$ is crucial for cancellation.

The "reciprocal spacing statistic" $P(D,H;X)$ is not precisely defined; we define it as the minimum distance between distinct fractional parts $\{h X/(4d) \mod 1\}$ for $h\in[1,H]$, $d\in[D,2D]$. This statistic could indicate if the phases are well-separated (helpful for exponent pairs) or clumped. We will implement it subject to computational cost.

## Theorem-dependency audit

| Obligation / Lemma | Used in diagnostic | Status | Hypothesis check |
|---|---|---|---|
| H4 (Vaaler approx.) | Supplies $\Phi$ and $\alpha_h,\beta_h$ conventions | source_audit_required | We use a placeholder $\Phi(u)=1$ or the cubic B-spline until H4 audited; then update. |
| M9-M2-beta-algebra | Exact $\beta_h$ formula | derived_under_assumptions | Verified algebraically above; depends on H4 for $\Phi$. |
| M9-M2-fourth-moment-expansion | Cleared numerator $N$ | derived_under_assumptions | Correctly derived from the phases; used as-is. |
| M9-M2-character-factor | Odd-only support | open | Strongly supported by beta algebra, but must be retained in all estimates. |
| M9-M2-average-to-pointwise-AP-lemma | LFM diagnostic | proved_internal | Valid calculus lemma; used only as interpolation formula, not as proof. |
| M9-M2-local-fourth-moment-LFM | Target of diagnostics | open | We test the hypothesis, not prove it. |
| M9-n-collision-taxonomy | Classification categories | open | We implement the taxonomy as currently documented; any gaps will appear in "unclassified" bin. |
| H1-H3 | Underlying sawtooth reduction | proved_internal | Not directly needed for the diagnostic; we assume the sums $M_i$ as defined. |
| Vaaler source card | Exact $\Phi$ and residual | source_audit_required | Placeholder used; after audit we replace. |

**Missing theorems for literature search (to be assigned to A1/A2/A4):**

- An explicit statement of the Vaaler theorem with the exact $\Phi$ function (cubic B-spline?) and the precise constant in the Fejer kernel residual, to be inserted into `sources/vaaler_1985.md`.
- A precise theorem from the Li--Yang paper that could be applied to $M_1$ or $M_2$, with exact hypotheses about the coefficient class, weight smoothness, and allowed ranges.

## Hidden assumptions and potential gaps

1. **Smoothness of $w_D(d)$.** The sawtooth/Fejer reduction assumes a smooth dyadic weight. The choice of weight affects the derivative bound and the cancellation in inner sums. The diagnostic must use a smooth bump function; rectangular weights will create discontinuities and spurious large high-frequency terms.
2. **Truncation of $h$ sum to $H_D$.** The Vaaler approximation uses $|h|\le H$, where $H$ is a parameter that must scale as $H \approx D X^{-1/4}$ for the residual to be controlled. The diagnostic will use that scaling, but the exact constant must be chosen so that the residual $R_5$ is $O_\epsilon(X^{1/4+\epsilon})$. Since $H_4$ is not audited, we use a plausible scaling.
3. **Endpoint $D=X^{1/2}$.** At this endpoint, the local window length $\delta = X^{1/2}/D = 1$, so the local average degenerates to a single point. The AP lemma still holds, but the derivative term then involves $\sup|F'|$ with no averaging, making the bound potentially weaker. The diagnostic will check this regime separately.
4. **Fattened band $|N| \ll D^5 X^{-1/2}$.** This bound was derived heuristically; we must confirm that the local integration indeed restricts to this band after considering the exact oscillatory integral. The diagnostic will compute the exact local average (via Riemann sum) and compare with the sum over the fat band to see if contributions outside are negligible.
5. **Complex weight failure:** The paired formula relies on $B_{-h}=\overline{B_h}$, which holds if $w_D(d)$ is real. The diagnostic will confirm that when we deliberately use complex weights, the raw two-sided formula still gives the correct sum, but the paired formula fails.
6. **Classification completeness:** The taxonomy of exact N=0 tuples may be incomplete. The diagnostic will list any tuple that satisfies N=0 but is not matched by any of the implemented classifiers; these will be recorded as "unclassified". Their total mass will indicate how much of the exact N=0 set is unexplained.
7. **Integer arithmetic overflow:** The numerator $N$ can be as large as $4 H D^3 \approx D^4 X^{-1/4}$, which for $D\approx X^{1/2}$ is $X^{7/4}$. For $X=10^6$, this is $10^{10.5}$, which fits in Python's arbitrary-precision integers, but performance will degrade. We will use Python's `int` and possibly limit $X$ to $10^4$--$10^5$ for full enumeration; for larger $X$, we may use sampling.
8. **Derivative bound for AP lemma:** The term $\sup|F'|$ must be bounded analytically; our diagnostic can compute it numerically for the windows tested, but cannot provide a uniform proof. It may reveal windows where $|F'|$ is large, which would weaken the AP bound.
9. **Local-average computation cost:** Computing the exact fourth-moment for many windows is expensive. We will use Monte Carlo or coarse Riemann sums for the integral. We must report the sampling error.

## Counterexample or obstruction search

Potential obstructions that the computation could uncover:

- **Massive unclassified exact N=0 family:** If the "unclassified" bin contains a significant fraction of the total exact-N=0 mass, then the current taxonomy is insufficient and a new algebraic structure must be identified.
- **Local-fourth-moment spikes:** If for some windows the local $L^4$ average exceeds $C X^{1+\epsilon}$ with $C$ growing, the `(LFM)` hypothesis fails, and the AP-based route to pointwise bound collapses.
- **Endpoint $D=X^{1/2}$ failure:** Even if the local fourth moment is well-behaved for smaller $D$, the endpoint may exhibit a pointwise $|S_2|$ larger than $X^{1/4+\epsilon}$, violating the required uniformity.
- **Near-collision fat band not dominant:** The diagnostic will check whether the total fourth moment (global) is well approximated by the sum over the fat band. If the fat-band bound is too small, the LFM error may be large.
- **Signed-vs-unsigned cancellation:** If replacing $\beta_h$ by $|\beta_h|$ leads to a significantly larger $S_2$, then sign cancellation is active and must be preserved by any proof strategy. If the random-sign version often gives similar magnitude, then the specific $\chi_4$ pattern is not special, which would make the sign-preserving route less promising.
- **Spacing statistic suggests huge clumps:** If the minimal spacing is very small, then the phases are almost resonant, potentially causing constructive interference that amplifies the sum beyond expected bounds.

We will also deliberately construct a potential counterexample configuration: e.g., choose all $d$ equal (so denominator-paired case) and $h$ choices that satisfy N=0 with large weights; compute the resulting $S_2$ to see if it exceeds the target bound for that $X,D$.

## Verification

### Manual symbolic numeric check

Take $X=100$, $D=5$ (so $d \in \{5,6,7,8\}$ as a small dyadic range), $H=2$, and use placeholder $\Phi(u)=1$ (so $\beta_1 = -1/(\pi\cdot1) \cdot \chi_4(1) = -1/\pi$, $\beta_{-1}$ same; $\beta_2=0$). Choose weight $w_D(d)=1$ for simplicity (not smooth, but okay for a quick algebraic check). Then

$$
B_1 = \sum_{d=5}^{8} e(100/(4d)) = e(5) + e(25/6) + e(25/7) + e(25/8)?
$$

Careful: $100/(4d) = 25/d$. So $e(25/d)$. For $d=5$, $e(5) = 1$. For $d=6$, $e(25/6)=e^{2\pi i \cdot 25/6} = e^{2\pi i \cdot (4 + 1/6)} = e^{i\pi/3}=0.5 + 0.866i$. For $d=7$, $e(25/7)=e^{2\pi i \cdot 25/7} = e^{2\pi i \cdot (3 + 4/7)} = e^{8\pi i/7} \approx \cos(205.714^\circ) + i\sin(...) \approx -0.901 + 0.433i$. For $d=8$, $e(25/8)=e^{2\pi i \cdot 25/8} = e^{2\pi i \cdot (3 + 1/8)} = e^{i\pi/4} \approx 0.707+0.707i$.

Sum $B_1 \approx 1 + (0.5+0.866i) + (-0.901+0.433i) + (0.707+0.707i) = 1.306 + 2.006i$. $B_{-1}$ is the complex conjugate (since weight is real): $1.306 - 2.006i$.

Then $S_2 = \beta_1 (B_1 + B_{-1}) \approx (-0.3183) \cdot (2.612) \approx -0.831$.

Raw two-sided formula: $S_2 = \beta_{-1}B_{-1} + \beta_1 B_1 = \beta_1 (B_{-1}+B_1)$ because $\beta_{-1}=\beta_1$, same result.

Now paired formula: $S_2 = 2\beta_1 \operatorname{Re}(B_1) = 2(-0.3183)\cdot 1.306 \approx -0.831$. Matches.

If we replace $w_D$ by a complex weight, e.g., $w_D(d)=1+i$, then $B_1 = (1+i)\sum_d e(25/d)$, and $B_{-1} = (1-i)\sum_d e(-25/d) = (1-i)\overline{\sum_d e(25/d)}$, which is not the conjugate of $B_1$. Hence $\operatorname{Re}(B_1)$ pairing fails. This simple test confirms the formulas.

### Diagnostic bundle plan (to be materialized)

I will output an `## Artifact bundle` section with:

- Repository-relative file paths: `state/artifacts/round_006/m9_diagnostics.py`, `state/artifacts/round_006/run.sh`, `state/artifacts/round_006/expected_schema.md`, `state/artifacts/round_006/report_template.md`.
- Complete Python script contents (approx. 600 lines) implementing all required computations.
- Exact command lines and Python version requirements (Python 3.10+, numpy, scipy, sympy optional).
- Expected table schemas (CSV columns) for each diagnostic output.
- Precision log requirements (recording input parameters, timing, memory, numerical error estimates).
- Pass/fail assertions (e.g., raw-two-sided should match paired within machine epsilon for real weights; paired must diverge for complex weights; unclassified exact N=0 mass should be zero or negligible if taxonomy complete; local fourth moment should not exceed threshold in most windows).
- Report template that the executed script will fill.

Once the orchestrator materializes these files and runs them, the outputs become diagnostic evidence under `M9-regression-raw-vs-paired` and `M9-fourth-moment-enumeration`. Until then, they are plans only.

I will note that the computation was **not executed** at the time of writing, as per the protocol.

## Divergent alternatives and 20% exploration

**Alternative route 1: Sign-preserving discrepancy (SPD)**

Instead of fourth-moment averaging, one could try to bound $S_2$ directly using the fact that the points $\theta_{h,d} = \{h X/(4d)\}$ are well-spaced in $\mathbb{R}/\mathbb{Z}$. If a spacing theorem showed that the minimum gap is $\gtrsim 1/(H D)$, then standard large-sieve or Halasz-Montgomery type bounds could give $|S_2| \ll H^{1/2} D^{1/2} \log X$ which is $\approx D X^{-1/8} \cdot D^{1/2} = D^{3/2} X^{-1/8}$, too large. But if the spacing is $1/(\text{lcm})$ something, it might be better. This route would require proving a spacing theorem for reciprocal points, which connects to the divisor problem and Vinogradov's method. The first-spacing statistic $P(D,H;X)$ we compute is a diagnostic for this. If the minimal spacing is much larger than $1/(H D)$ on average, then a direct exponential-sum bound might succeed. The exact theorem needed: a bound for exponential sums with rational frequencies with denominator separation, perhaps from the Bombieri--Iwaniec method. The Li--Yang paper may be relevant; we need the source audit.

**Alternative route 2: Mellin-Perron and double-integral transform**

Transform $S_2(D;X)$ as a double integral over $s$ using Mellin inversion of the weight and the exponential, leading to an integral of $L$-functions. This is classical for the Gauss circle problem but requires careful contour shifting. It might bypass the fourth-moment hurdles but would need estimates on the growth of the resulting Dirichlet series $\sum_{d} w_D(d) d^{-s}$ near $\Re(s)=1$.

**Exploratory diagnostic:** We could modify the script to compute the Mellin transform numerically and compare with the direct sum to gauge cancellation.

**What would falsify each alternative quickly:** For SPD, if the minimal spacing is exponentially small in $X$, the direct exponential-sum bound fails. For Mellin, if the Dirichlet series has a pole with large residue, the contour integral yields a large contribution.

## Useful lemmas

**Lemma A (Real-weight pairing):** If $\beta_h$ is real and even, and $w_D(d)$ is real, then

$$
S_2 = \sum_{h=1}^H 2\beta_h \operatorname{Re}\!\biggl( \sum_{d} w_D(d) e\!\bigl(hX/(4d)\bigr)\biggr).
$$

**Lemma B (Fourth-moment numerator):** For $S_2$ defined with two-sided $h$, the $L^4$-norm squared integrand (with respect to $X$) has phase factor $e(N X/(4\Delta))$ where $N$ is given above.

**Lemma C (Local average band):** For a window of length $\delta$, the contribution of a tuple with numerator $N$ to $\frac{1}{\delta}\int_I e(N t/(4\Delta)) dt$ is bounded by $\min(1, \frac{4\Delta}{\delta |N|})$, so only $|N| \ll \Delta/\delta = D^5 X^{-1/2}$ contributes significantly.

These lemmas are already present in the proof obligations or can be trivially derived.

## What should be tested next

After the diagnostic bundle is executed:

1. **Check the unclassified exact N=0 mass.** If nonzero, isolate examples and see if they fall into a new algebraic family. Provide the examples to A2/A4 for analysis.
2. **Analyze local fourth-moment histograms.** Identify windows where the local average exceeds the global average by more than a factor, and examine the tuples involved. Determine if they cluster around certain $d$ patterns.
3. **Validate the fat-band approximation.** Compare the full local $L^4$ average with the average obtained by restricting the inner sum to $|N|\le C D^5 X^{-1/2}$; if the discrepancy is large, the LFM heuristics need revision.
4. **Endpoint $D=X^{1/2}$ stress test.** Run at a few $X$ values with $D=X^{1/2}$ and measure $|S_2|$ directly; compare with $X^{1/4+\epsilon}$.
5. **Signed-vs-unsigned plots.** If the true $S_2$ is often smaller than the unsigned version by a significant factor, then sign preservation is essential, supporting the SPD route. If not, the fourth-moment route may be robust to sign changes.
6. **Refine the $\Phi$ placeholder** after H4 source card is audited. Rerun with the actual Vaaler $\Phi$ to see if the magnitude of $\beta_h$ changes the scales.

The results should be fed into the proof graph as `diagnostic_only` evidence under the obligations `M9-fourth-moment-enumeration` and `M9-regression-raw-vs-paired`.

## Proposed state patch, if any

I propose to **add a new computation obligation** `M9-lfm-window-diagnostics` (diagnostic_only) to track the local fourth-moment windows and exceptional windows. Its required outputs: CSV of window summary, exceptional window list, histogram plot.

Also update `M9-fourth-moment-enumeration` next_action to reflect the executed bundle and to request analysis of unclassified tuples.

But these are only proposals; the judge will decide.

For now, no safe mutation of `state/proof_obligations.yml` can be done without actual execution output. So I will not include a formal state patch, but I will note the desired updates in the report for the judge.

## Artifact bundle

**Important note:** The computation was **not executed** at the time of writing. The following bundle provides everything needed for the local orchestrator to materialize and run the diagnostics. Once executed, the artifacts become positive evidence.

### Repository paths

```
state/artifacts/round_006/m9_diagnostics.py
state/artifacts/round_006/run.sh
state/artifacts/round_006/schema.md
state/artifacts/round_006/report_template.md
state/artifacts/round_006/precision.log   (to be generated)
state/artifacts/round_006/table_raw_vs_paired.csv
state/artifacts/round_006/table_n0_taxonomy.csv
state/artifacts/round_006/table_lfm_windows.csv
state/artifacts/round_006/table_near_collision.csv
state/artifacts/round_006/table_signed_unsigned.csv
state/artifacts/round_006/table_spacing.csv (optional)
```

### Python script (summarized content; full script in the actual artifact)

The script `m9_diagnostics.py` will be structured as follows:

```python
#!/usr/bin/env python3
"""
M9 diagnostics for Gauss circle problem.
Computes raw-vs-paired M2, fourth-moment exact N=0 taxonomy,
local fourth-moment averages, near-collision bands, signed-vs-unsigned,
and optional spacing statistic.
"""
import argparse, json, csv, time, math, sys
from typing import List, Tuple, Dict
import numpy as np
from scipy.integrate import trapezoid  # if needed

# -------------------------- Configuration --------------------------
# Placeholder Vaaler Phi: use flat 1.0 for testing; replace after H4.
def Phi(u: float) -> float:
    """Vaaler kernel placeholder. To be replaced by actual cubic B-spline."""
    return 1.0 if 0 <= u <= 1 else 0.0

def beta_h(h: int, H: int) -> float:
    """Real beta coefficient; zero for even h."""
    if h % 2 == 0:
        return 0.0
    # chi_4(h): 1 for h%4==1, -1 for h%4==3
    chi = 1 if h % 4 == 1 else -1
    u = abs(h) / (H + 1)
    val = Phi(u)
    return -val * chi / (math.pi * abs(h))

def weight_d(d: int, D: float, smooth: bool = True) -> float:
    """Smooth bump supported on approximately [D, 2D)."""
    x = d / D
    if x < 0.9 or x > 2.1:
        return 0.0
    if not smooth:
        return 1.0 if 1 <= x < 2 else 0.0
    # Example smooth bump: compact support and C^2
    t = (x - 1.0) / 0.5  # map [1,2] to [0,2]; extend slightly
    # bump: exp(-1/(t*(2-t))) for 0<t<2 else 0
    if t <= 0 or t >= 2:
        return 0.0
    return math.exp(-1.0 / (t * (2 - t)))

def B_h(h: int, D: float, X: float, d_start: int, d_end: int, smooth: bool = True, complex_weight: bool = False) -> complex:
    """Inner sum: sum_d w(d) e(hX/(4d))."""
    s = 0+0j
    for d in range(d_start, d_end):
        w = weight_d(d, D, smooth)
        if w == 0:
            continue
        phase = 2 * math.pi * (h * X) / (4 * d)
        if complex_weight:
            # example complex weight: multiply by (1 + 0.5j)
            s += w * (1 + 0.5j) * cmath.exp(1j * phase)
        else:
            s += w * cmath.exp(1j * phase)
    return s

def S2_raw(D: float, X: float, H: int, d_start: int, d_end: int, smooth: bool, complex_weight: bool) -> complex:
    """Raw two-sided M2."""
    s = 0+0j
    for h in range(-H, H+1):
        if h == 0:
            continue
        b = beta_h(h, H)
        s += b * B_h(h, D, X, d_start, d_end, smooth, complex_weight)
    return s

def S2_paired(D: float, X: float, H: int, d_start: int, d_end: int, smooth: bool, complex_weight: bool) -> float:
    """Real-weight paired formula (only valid if weight is real)."""
    if complex_weight:
        raise ValueError("Paired formula requires real weights.")
    s = 0.0
    for h in range(1, H+1):
        b = beta_h(h, H)
        if b == 0:
            continue
        s += 2 * b * (B_h(h, D, X, d_start, d_end, smooth, complex_weight=False).real)
    return s

# ... further functions for fourth moment, classification, LFM windows, etc.
```

The script will include:

- Argument parser: `--X`, `--D`, `--H` (or auto-scale), `--d-start`, `--d-end` (default based on D), `--smooth/--rect`, `--complex-weight`, `--output-dir`.
- Functions for `S2_raw`, `S2_paired`, and tests that they match within tolerance for real weights and diverge for complex.
- Fourth-moment enumeration: for small ranges (exhaustive), iterate over $h_1,h_2,h_3,h_4\in[-H,H]\setminus\{0\}$ and $d_1,\dots,d_4$ in the dyadic range, compute $N$, record tuple if $N=0$ (exact) or within band. For each exact N=0 tuple, classify into categories.
- Compute the signed fourth-moment mass: sum of product of $\beta$ and weights for each N=0 tuple.
- Compute absolute mass: sum of absolute values.
- LFM windows: sample many $X_0$ values in $[X_{\min}, X_{\max}]$, and for each compute $|S_2|^4$ and also local average over a window of length $\delta = X^{1/2}/D$ by averaging over a few nearby points. Report statistics.
- Near-collision: for a given $X$, enumerate tuples with $0<|N|\le C_{\text{fat}}$, compute contribution to fourth power, compare with full sum.
- Signed-vs-unsigned: compute $S_2$ with true $\beta$, with $|\beta|$, with random signs, with adversarial signs (all same sign, or alternating pattern).
- Spacing: collect fractional parts $\{hX/(4d)\}$ for all pairs, compute minimum distance, histogram.

The script will output CSV tables with the schemas described below.

### Exact commands

```bash
# Setup
python -m venv env
source env/bin/activate
pip install numpy scipy sympy  # sympy for exact rational if needed

# Compile check
python -m py_compile state/artifacts/round_006/m9_diagnostics.py

# Run diagnostics with small sample
python state/artifacts/round_006/m9_diagnostics.py \
  --X 1000 --D 10 --H 4 --d-start 10 --d-end 20 \
  --smooth --output-dir state/artifacts/round_006/ \
  --run-tests

# Full run for larger X
python state/artifacts/round_006/m9_diagnostics.py \
  --X 100000 --D 100 --H 0 --d-start 100 --d-end 200 \
  --auto-H --smooth --output-dir state/artifacts/round_006/ \
  --run-all
```

The `--auto-H` flag will set $H = \max(1, \lfloor D X^{-1/4} \rfloor)$.

### Expected table schemas

1. **table_raw_vs_paired.csv**

Columns: `X, D, H, S2_raw_real, S2_raw_imag, S2_paired (real only for real weights), diff_real, diff_imag, weight_type` (real/complex). One row per test case.

2. **table_n0_taxonomy.csv**

Columns: `tuple_id, h1, h2, h3, h4, d1, d2, d3, d4, N, category, signed_mass, abs_mass`. For each N=0 tuple, classification category string. The `signed_mass` is $\beta_{h1}\beta_{h2}\beta_{h3}\beta_{h4} w(d1)w(d2)w(d3)w(d4)$, `abs_mass` same with absolute values.

After enumeration, summary rows: `category, total_signed, total_abs, count`.

3. **table_lfm_windows.csv**

Columns: `window_id, X_center, delta, local_L4_avg, global_L4_avg, sup_deriv (if computed), AP_rhs_bound, ratio_local_global, is_exceptional`. `is_exceptional` true if local > 2*global or exceeds threshold.

4. **table_near_collision.csv**

Columns: `X, D, band_type (thin/fat), C, total_fourth_moment_contribution, total_fourth_moment_full, ratio`. For each band we sum |tuple contribution| and compare to full fourth moment.

5. **table_signed_unsigned.csv**

Columns: `X, D, H, beta_type (true, abs, random_seed, adversarial_pattern), S2_real, S2_imag, |S2|, comment`.

6. **table_spacing.csv** (optional if feasible)

Columns: `X, D, H, min_spacing, avg_spacing, median_spacing, count_pairs`.

### Precision log (precision.log)

The script will write to `precision.log` the exact input parameters, Python version, package versions, timings, number of tuples enumerated, any warnings about overflow or memory, and the machine epsilon for float comparisons.

### Report template (report_template.md)

The script will generate `report.md` with sections:

- Summary of raw-vs-paired test (pass/fail).
- Taxonomy completeness metric (unclassified mass, if any).
- LFM window analysis: number of windows, exceptional windows, worst-case ratio.
- Near-collision band efficiency.
- Signed-vs-unsigned comparison.
- Recommendations for proof strategy.

The template will contain placeholders that the script fills.

### Pass/fail assertions

The script will include assertions:

- For real weights: `abs(S2_raw - S2_paired) < 1e-12 * (abs(S2_raw)+1)`.
- For complex weights: `S2_paired` raises or gives a different result (not used), but raw formula still consistent.
- Unclassified exact N=0 mass should be less than $10^{-6}$ of total absolute mass, else flag.
- Local L4 average in at least 95% of windows should be bounded by $K X^{1+\epsilon}$ with a chosen $K$; otherwise, the LFM hypothesis is challenged.

If any assertion fails, the script exits with a non-zero code and logs the failure.

## Confidence

**Algebra audit:** High confidence (95%) that the beta-coefficient algebra and the paired-formula relationships are correct, assuming the stated H4 conventions.

**Diagnostic design:** Moderate confidence (80%) that the proposed computational bundle will correctly implement the required tests. The main risks are performance for large $X$ and possible mis-specification of the smooth weight normalization. The bundle includes conservative defaults and can be adjusted.

**Proof-graph advancement:** Low confidence (30%) that these diagnostics alone will reveal a direct path to proving $M9$. They are designed to identify algebraic gaps (unclassified N=0 families) and to stress-test the local fourth-moment hypothesis. The actual proof will require analytic bounds that the diagnostics can only suggest, not prove.

**Overall research:** The project remains at an early stage. The current conditional bridge is plausible but heavily dependent on $M9$, which is still open. The computational evidence, when materialized, will either reinforce the chosen route or force a strategic pivot. We recommend that the judge allocate further rounds to either (a) proving the LFM hypothesis using the enumeration data, or (b) developing the sign-preserving discrepancy route if the signed-unsigned diagnostics show strong cancellation.

---

--- OUTPUT FROM A4 ---
## Summary

This is A4 Stage A reasoning for Round 6 (run `obligation-main`), executing the judge-assigned tasks on `M9-M2-DP-near-collision-bound`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-coprime-rigidity-normal-form`, and the unpaired near-collision/exact-resonance search. I acknowledge the standing human directives (research mode, four-agent configuration, 80/20 allocation, calibrated status labels) and the Round 5 judge instructions; no new human override appeared this round.

Deliverables:

1. A validator-ready DP suite: exact parity emptiness with dyadic constants (Lemmas DP-0, DP-1), the thin DP near-collision mass bound in the only nonempty regime (Lemma DP-2), the full DP-total mass bound (Lemma DP-3), and a precise statement of exactly which part of H4 each lemma consumes.
2. A compact lemma-bank form of the coprime-rigidity normal form (NF-1) plus a new, unconditionally proved participation-rigidity lemma (NF-2) that constrains which reduced fractions can participate in a resonance with a given target value $\mu/Q$.
3. A sharpened analysis of `(LFM)`: the exact window-multiplier computation producing the band, a proof that on coherence windows $\delta = X^{1/2}/D$ the per-tuple frequency satisfies $\delta|\lambda| \ll X^{1/4}/D \le O(1)$ for every active $D$, hence the `(LFM)` statement is equivalent at target precision to the pointwise bound on the window (not only at the endpoint); a quantified answer to the exceptional-window question via a large-value propagation lemma; and a conditional moment-hierarchy range map showing which $D$-ranges a $2k$-th moment plus slow variation could reach and why the endpoint block $D \asymp X^{1/2}$ is outside the reach of every fixed moment order under a diagonal-floor hypothesis.
4. Two new proved unpaired exact-resonance bounds (Lemmas U-2 and SS, plus the anti-paired class), which together with fraction-matching cover all exact $N=0$ tuples whose reduced-denominator multiset has the form $\{q,q,q',q'\}$; a sharply reduced residual problem (URES) with a concrete nonempty witness family and a heuristic size prediction.
5. The SPD route kept exploratory: exact spacing statistic $P(D,H;X)$ and a falsification test specification for A3.

No promotion of `M9-M2`, `M9`, or `GC-target` is proposed.

## Target proof obligation

Primary: `M9-M2-DP-near-collision-bound`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-coprime-rigidity-normal-form`, and the unpaired exact-resonance component of `M9-near-collision-taxonomy` / `M9-near-collision-estimate`. Secondary (affected): `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-reciprocal-SPD-route`.

## Main claim or direction

Conventions used throughout (project two-sided conventions): active dyadic block $D$ with $X^{1/4} \le D \le X^{1/2}$; $d \in \mathcal D := [D,2D) \cap \mathbb Z$; truncation $1 \le H = H_D \le c_H D X^{-1/4}$ with $H \ge 1$; weights $|w_D(d)| \le 1$; coefficients $\beta_h = \alpha_{h,H} C_h$ with $C_h = e(h/4) - e(3h/4) = 2i\chi_4(h)\mathbf 1_{2\nmid h}$, so that under the H4 model (id `M9-M2-beta-algebra`) $\beta_h$ is real, even, supported on odd $h$, with $|\beta_h| \le K/|h|$. The fourth-moment tuple is $(\mathbf h, \mathbf d) = (h_1,\dots,h_4; d_1,\dots,d_4)$, phase frequency
$$
\lambda = \frac{h_1}{4d_1} - \frac{h_2}{4d_2} + \frac{h_3}{4d_3} - \frac{h_4}{4d_4} = \frac{N}{4\Pi},\qquad \Pi = d_1d_2d_3d_4,
$$
with $N$ the cleared integer of `M9-M2-fourth-moment-expansion`.

Claim ledger (statuses recommended, per-claim):

| # | Claim | Status recommendation |
|---|---|---|
| C1 | DP-0: single-parity $\beta$-support forces $N \in \{0\} \cup \{|N| \ge 2ab\}$ on the DP class | proved given the support structure; overall `derived_under_assumptions` (structure pending H4 audit) |
| C2 | DP-1: thin band $0<|N|\le C_0D^4/X$ meets DP only if $D \ge (2X/C_0)^{1/2}$; empty for all active $D$ when $C_0 < 2$ | same as C1 |
| C3 | DP-2: thin DP mass $\le C\,C_0K^4 D\log^2(2H)$ where nonempty | `derived_under_assumptions` (uses $|\beta_h|\le K/|h|$) |
| C4 | DP-3: full DP-total mass $\le 4K_1^4 D^2$, $K_1 = 2K(1+\log H)$ | `derived_under_assumptions` |
| C5 | NF-1 normal form (compact lemma-bank statement) | already `proved_internal`; text supplied |
| C6 | NF-2 participation rigidity: $q_3 \ge Qq_1/\gcd(Q,q_1)^2$ and the divisor condition | `proved_internal` candidate (pure integer lemma) |
| C7 | W (window multiplier) and B (bandwidth): $\delta|\lambda| \le c_H X^{1/4}/D$ for all tuples, all active $D$ | multiplier identity unconditional; bandwidth uses only $H \le c_H DX^{-1/4}$: `proved_internal` candidate |
| C8 | EQ: `(LFM)` on $\delta = X^{1/2}/D$ windows is equivalent at target precision to the pointwise bound on the window | `derived_under_assumptions` ($|\beta_h| \le K/|h|$ for the drift) |
| C9 | LV: large-value propagation, $V^{2k+1} \le 2^{2k+1}\pi K H\, G_{2k}$ | `derived_under_assumptions` |
| C10 | Moment-hierarchy range map: $2k$-th moment + LV reaches only $D \le X^{(k-1)/(2(k+1))}$ under the stated moment sizes; endpoint outside every fixed $k$ under a diagonal-floor hypothesis | `diagnostic_only` route map (moment bounds unproven) |
| C11 | U-2 / SS / anti-paired: unpaired exact $N=0$ mass on all $\{q,q,q',q'\}$ reduced-denominator patterns is $\ll D\log^4 X + D^2$ | `derived_under_assumptions` |
| C12 | URES residual is nonempty (explicit family) and heuristically of size $\asymp DH\,\mathrm{polylog} = D^2X^{-1/4+o(1)}$ | witness proved; size prediction `diagnostic_only` |

## Detailed reasoning

### A. DP suite (objective 1)

DP class: $d_1 = d_2 = a$, $d_3 = d_4 = b$, $a,b \in \mathcal D$. Substituting into $N$ gives the exact factorization
$$
N = ab\,L, \qquad L = (h_1 - h_2)\,b + (h_3 - h_4)\,a .
$$

Lemma DP-0 (parity). Assume $\operatorname{supp}\beta$ lies in a single residue class mod $2$ (the H4 model gives the odd class via $C_h$). Then for every DP tuple with all $\beta_{h_i} \ne 0$, both $h_1 - h_2$ and $h_3 - h_4$ are even, hence $L \in 2\mathbb Z$. Consequently either $L = 0$ (exact resonance, scoped by `M9-M2-denominator-paired-weighted-bound`) or $|L| \ge 2$ and
$$
|N| = ab\,|L| \ge 2ab \ge 2D^2 .
$$
The degenerate case $a = b$ only strengthens this: $N = a^3(h_1-h_2+h_3-h_4)$ with an even bracket, so $|N| \ge 2a^3 \ge 2D^3$. Proof is complete as stated; the only input is single-parity support, which is robust under either pure-odd or pure-even support but would fail for mixed-parity support (see hidden assumptions).

Lemma DP-1 (thin-band emptiness with exact constants). Fix $C_0 > 0$ and the thin band $0 < |N| \le C_0 D^4/X$. By DP-0, a DP tuple in the band requires $2D^2 \le C_0D^4/X$, i.e.
$$
D \ \ge\ \left(\frac{2X}{C_0}\right)^{1/2}.
$$
Hence: for $C_0 < 2$ the band is empty on the DP class for every active $D \le X^{1/2}$; for $C_0 \ge 2$ it can be nonempty only on the top blocks with $D \ge (2/C_0)^{1/2}X^{1/2}$, a bounded number of dyadic blocks depending only on $C_0$. Note the local fat threshold $D^5X^{-1/2}$ behaves differently: $2D^2 \le C_1D^5X^{-1/2}$ holds as soon as $D \ge (2/C_1)^{1/3}X^{1/6}$, i.e. throughout the active range; parity emptiness protects only the thin band.

Lemma DP-2 (thin DP mass where nonempty). Assume additionally $|\beta_h| \le K/|h|$. Write $h_1-h_2 = 2u$, $h_3-h_4 = 2v$, $L = 2\ell'$, $\ell' = ub+va$. In the band, $ab \ge D^2$ and $D \le X^{1/2}$ give $1 \le |\ell'| \le C_0D^2/(2X) \le C_0/2$. If $u = 0$ then $|v|a = |\ell'| \le C_0/2 < D \le a$ forces $v = 0$ and $\ell' = 0$, excluded; so $u,v \ne 0$, and from $|ub+va| \le C_0/2$ with $a,b \in [D,2D)$ one gets, for $D > C_0$, the two-sided comparability $|u| \le 2|v|$ and $|v| \le 2|u|$. Group by $(u,v,\ell')$. For fixed $(u,v,\ell')$ the count of $(a,b) \in \mathcal D^2$ with $ub+va = \ell'$ is at most $1 + D\gcd(u,v)/\max(|u|,|v|)$ (the congruence $va \equiv \ell' \pmod{|u|}$ pins $a$ to one class mod $|u|/\gcd(u,v)$, and $b$ is then determined; symmetrize in $u,v$). The $h$-pair sums are controlled by `M9-M2-harmonic-convolution-LH`: $\sum_{h_1}|\beta_{h_1}\beta_{h_1-2u}| \le K^2L_H(2u) \le CK^2\log(2H)/|u|$. Therefore
$$
\Sigma^{\mathrm{thin}}_{DP} \ \le\ C K^4 C_0 \log^2(2H) \sum_{\substack{u,v\ne 0,\ |u|\le H \\ |u|\asymp|v|}} \frac{1}{|u||v|}\left(1 + \frac{D\gcd(u,v)}{\max(|u|,|v|)}\right).
$$
The first part is $\ll \log(2H)$. For the second, $\sum_{|v|\le 2|u|}\gcd(u,v) \le \sum_{g\mid u}(4|u|+g) \le 5|u|\,d(u)$, so the inner sum over $v$ is $\ll d(u)$ and the total is $\ll D\sum_u d(u)/u^2 \ll D$. Conclusion:
$$
\Sigma^{\mathrm{thin}}_{DP} \ \le\ C'\,C_0\,K^4\, D\,\log^2(2H) \qquad (\text{nonempty only when } D \ge (2X/C_0)^{1/2}),
$$
so at most $\ll X^{1/2+\epsilon}$, far inside both the $X^{1+\epsilon}$ and $D^2X^\epsilon$ budgets. The case split requested by the judge is: $L = 0$ (exact, external to this lemma), $L \ne 0$ with the unique-solution regime (the line $ub+va = \ell'$ meets $|u| \le H$ in $\le 1 + C_0H/D \to 1$ points for each $(a,b,\ell')$ since $\gcd(a,b) \mid \ell'$ forces $\gcd(a,b) \le C_0/2$).

Lemma DP-3 (full DP-total). With no band restriction, $\Sigma^{\mathrm{full}}_{DP} = \big(\#\mathcal D\big)^2\big(\sum_{h}|\beta_h|\big)^4 \le D^2\,K_1^4$ with $K_1 = 2K(1+\log H)$, hence $\ll D^2\log^4(2H) \le X\log^4 X$. The DP constraint itself removes two denominator degrees of freedom; the class is harmless at the $X^{1+\epsilon}$ scale regardless of oscillation.

H4 dependence split (objective 1d): DP-0/DP-1 use only single-parity support of $\beta$, i.e. the presence of the $C_h$ factor from the $\rho \in \{1,3\}$ difference; they do not use the size or sign of $\alpha_{h,H}$. DP-2/DP-3 additionally use $|\beta_h| \le K/|h|$. The specific audit item that could break DP-0 is the sign structure of the $\rho$-combination: a sum instead of a difference gives $e(h/4)+e(3h/4) = 2(-1)^{h/2}\mathbf 1_{2\mid h}$, which is even-supported -- DP-0 survives (differences of evens are even) -- while a mixed-parity support would break it. So the audit checklist item is: confirm that the two reciprocal blocks enter with a relative structure producing single-parity $h$-support.

### B. Coprime-rigidity normal form (objective 2)

Lemma NF-1 (compact lemma-bank form). Let $h_i \ne 0$, $d_i \ge 1$, and write $h_i/d_i = p_i/q_i$ in lowest terms, $q_i \ge 1$. Set $g_{13} = \gcd(q_1,q_3)$, $q_1 = g_{13}s_1$, $q_3 = g_{13}s_3$, $m_{13} = p_1s_3 + p_3s_1$, $e_{13} = \gcd(g_{13}, m_{13})$, and define $g_{24}, s_2, s_4, m_{24}, e_{24}$ analogously. Then $\gcd(m_{13}, s_1s_3) = 1$, the reduced form of $p_1/q_1 + p_3/q_3$ is $\dfrac{m_{13}/e_{13}}{(g_{13}/e_{13})\,s_1s_3}$, and $N = 0$ holds if and only if
$$
\frac{g_{13}}{e_{13}}\,s_1s_3 = \frac{g_{24}}{e_{24}}\,s_2s_4 \quad\text{and}\quad \frac{m_{13}}{e_{13}} = \frac{m_{24}}{e_{24}},
$$
with the convention that the value $0$ has reduced form $0/1$ (the case $m_{13} = m_{24} = 0$ is the anti-paired class $p_3/q_3 = -p_1/q_1$, $p_4/q_4 = -p_2/q_2$). Equivalently: there exist $Q \ge 1$, $\mu$ with $\gcd(\mu,Q) = 1$, and $e_{13} \mid \gcd(q_1,q_3)$, $e_{24} \mid \gcd(q_2,q_4)$ such that $\operatorname{lcm}(q_1,q_3) = e_{13}Q$, $\operatorname{lcm}(q_2,q_4) = e_{24}Q$, $m_{13} = e_{13}\mu$, $m_{24} = e_{24}\mu$. In the project ranges, $D/H \le c\,q_i \le 2D$ and $|p_i| \le q_iH/D$.

Lemma NF-2 (participation rigidity; new, unconditional). Let $r = \mu/Q$ be reduced, $\mu \ne 0$, and let $x_1 = p_1/q_1$ be reduced with $x_3 := r - x_1 \ne 0$ of reduced denominator $q_3$. Put $g = \gcd(Q,q_1)$, $\hat Q = Q/g$, $\hat q_1 = q_1/g$, $M = \mu\hat q_1 - p_1\hat Q$. Then $\gcd(\hat Q\hat q_1, M) = 1$ and
$$
q_3 = \frac{g\,\hat Q\,\hat q_1}{\gcd(g, M)} \ \ge\ \hat Q\hat q_1 = \frac{Qq_1}{g^2}.
$$
Consequently, if $q_3 \le 2D$ is required (as in our tuple space), then
$$
\gcd(Q, q_1)\ \ge\ \left(\frac{Qq_1}{2D}\right)^{1/2} \quad\text{and}\quad \gcd(g, M)\ \ge\ \frac{Qq_1}{2Dg}.
$$
Proof: mod $\hat q_1$ the integer $M$ is $\equiv -p_1\hat Q$, coprime to $\hat q_1$; mod $\hat Q$ it is $\equiv \mu\hat q_1$, coprime to $\hat Q$; a prime dividing $\gcd(g\hat Q\hat q_1, M)$ cannot divide $\hat Q\hat q_1$, so the gcd equals $\gcd(g,M)$ prime by prime; then $q_3 = Qq_1/\gcd(Qq_1, \mu q_1 - p_1Q) = g^2\hat Q\hat q_1/(g\gcd(g,M))$. This lemma converts the residual unpaired problem into a divisor-constrained lattice count: only $q_1$ sharing a large divisor with $Q$ can participate, and within those only $p_1$ in prescribed residue classes mod $\gcd(g,M)$-forcing sets.

### C. The `(LFM)` obstruction (objective 3)

(3a) Exact band mechanism. For an interval $I$ of length $\delta$ centered at $X_0$,
$$
\frac{1}{\delta}\int_I |S_2(D;t)|^4\,dt \;=\; \sum_{\mathbf h,\mathbf d} B(\mathbf h)W(\mathbf d)\, e(X_0\lambda)\,\frac{\sin(\pi\lambda\delta)}{\pi\lambda\delta},
$$
with $B, W$ the coefficient and weight products. The multiplier is $1$ at $\lambda = 0$ and bounded by $\min(1, (\pi\delta|\lambda|)^{-1})$; the sufficient no-decay region expressed in $N$ via $\Pi \ge D^4$ is $|N| \le 4\Pi/\delta$, whose worst case at $\delta = X^{1/2}/D$ is the stated fat band $|N| \ll D^5X^{-1/2}$. This derivation is complete and validator-ready.

(3a') Sharpening -- the band is not the right object. The sharp condition is on $\lambda$, and directly from the fraction form,
$$
|\lambda| \le 4\cdot\frac{H}{4D} = \frac{H}{D} \le c_H X^{-1/4} \quad\text{uniformly over active } D,
$$
because $H_D/D \asymp X^{-1/4}$ by the project normalization. Hence on coherence windows $\delta = X^{1/2}/D$:
$$
\delta\,|\lambda| \ \le\ c_H\,\frac{X^{1/4}}{D} \ \le\ c_H \qquad\text{for every tuple and every active } D.
$$
So the window multiplier admits no power-in-$X$ decay on any tuple anywhere in the active range; at $D \ge C_2X^{1/4}$ it is uniformly $\ge c > 0$, and at the bottom block $D \asymp X^{1/4}$ it can vanish only on a top-frequency constant fraction. The fat band $|N| \ll D^5X^{-1/2}$ is technically correct but exceeds the maximal $|N| \asymp HD^3 = c_H D^4X^{-1/4}$ by the factor $\asymp H_D$ for $D \gg X^{1/4}$: it contains the whole tuple space. Numerical spot checks (Verification) confirm both the $N$-ratio and the $\delta\lambda$ values.

(3a'') Consequence -- equivalence lemma EQ. Since $\sup_t|S_2'(t)| \le \sum_h |\beta_h|\sum_{d\in\mathcal D}\frac{2\pi|h|}{4d} \le \pi K H$, the drift over a coherence window is $\le \pi K H\delta/2 \le (\pi K c_H/2)\,X^{1/4}$: exactly target order. Therefore, elementarily,
$$
|S_2(X_0)| \ \le\ \Big(\tfrac1\delta\int_I|S_2|^4\Big)^{1/4} + \pi K c_H X^{1/4}, \qquad \tfrac1\delta\int_I|S_2|^4 \ \le\ \Big(\sup_I |S_2|\Big)^4,
$$
so `(LFM)` at threshold $X^{1+\epsilon}$ on a window is equivalent, at target precision, to the pointwise bound $\ll X^{1/4+\epsilon}$ on that window; quantified over all windows, `(LFM)` and pointwise `M9-M2` are the same statement up to constants. This supersedes and strengthens my Round 5 framing (and is consistent with the judge's rejection `A4-R5-AP-implies-M9-M2`): `(LFM)` is not an intermediate weaker target; its proof must contain the full $h,d$-space cancellation. The AP lemma remains true but redundant for this purpose. Also note the absolute-mass route to `(LFM)` is not available: the full absolute tuple mass is $\asymp D^4\log^4(2H)$, exceeding $X^{1+\epsilon}$ once $D \ge X^{1/4+\eta}$.

(3b) Exceptional windows and the global moment. Over a global window $\Delta \asymp X$ the multiplier does decay: the surviving region is genuinely the thin band $|N| \ll D^4/X$ (where DP-1 applies), so global fourth-moment estimates have real oscillatory content; by Chebyshev, a global bound $\int_X^{2X}|S_2|^4 \le G_4$ makes all but a measure-$\eta X$ set of coherence windows satisfy the local average bound at level $G_4/(\eta X)$. What can be recovered pointwise from this is quantified by:

Lemma LV (large-value propagation). If $|S_2(t_0)| = V$ then $|S_2| \ge V/2$ on an interval of length $V/(2\pi K H)$ around $t_0$, hence for any $k \ge 1$,
$$
V^{2k+1} \ \le\ 2^{2k+1}\,\pi K H\;\int_{X}^{2X}|S_2|^{2k}\,dt \qquad (t_0 \in [X,2X]).
$$
With the (unproven) expected sizes $G_{2k} := \int_X^{2X}|S_2|^{2k} \ll X^{1+\epsilon}D^k$ (diagonal-dominated), LV yields $V \ll (D^{k+1}X^{3/4+\epsilon})^{1/(2k+1)}$, which meets the target $X^{1/4+\epsilon}$ exactly when
$$
D \ \le\ X^{\frac{k-1}{2(k+1)}}.
$$
Range map: $k=3$ reaches $D \le X^{1/4}$ (trivial blocks anyway), $k=5$ reaches $X^{1/3}$, $k=10$ reaches $X^{0.409}$, and $D = X^{1/2-\eta}$ needs $k \ge (1-\eta)/\eta$. So an exceptional-window/global-moment strategy can in principle cover every fixed range $D \le X^{1/2-\eta}$ conditionally on the corresponding $G_{2k}$ bounds -- but not the endpoint: at $D \asymp X^{1/2}$ the requirement $D^{k+1} \le X^{(k-1)/2}$ fails for every finite $k$. Under the diagonal-floor hypothesis $\frac1X\int|S_2|^2 \gg D$ (diagonal $\asymp D$; the off-diagonal control needed to also confirm the matching upper bound is standard-looking but not yet a state lemma), Jensen gives $G_{2k} \gg XD^k$, and then the LV mechanism at the endpoint stalls at $V \ll X^{1/4}\cdot X^{1/(2(2k+1))}\cdot$ powers strictly above target for all $k$. This is a scoped statement about this mechanism, not about other routes.

(3c) Endpoint. At $D \asymp X^{1/2}$: $\delta = X^{1/2}/D \asymp 1$; every phase $ht/(4d)$ has frequency $\le c_HX^{-1/4}$, so every admissible window (any $t$-average whose recovery cost, via derivative drift or via monotonicity of $N(R)$ at the level of $P$, stays $\le X^{1/4}$) is sub-coherence; no $t$-average can help, and the trivial bound $|S_2| \le 2KD(1+\log H) \asymp X^{1/2}\log X$ must be improved to $X^{1/4+\epsilon}$ purely by $h,d$-space cancellation. Two remarks sharpen the picture at the range ends: (i) bottom blocks are trivial -- for $D \le X^{1/4}/(2K(1+\log H))$ the absolute-value bound already gives $|S_2| \le X^{1/4}$, so the effective range is $X^{1/4-o(1)} \lesssim D \le X^{1/2}$; (ii) I checked whether the classical monotonicity averaging of $P(X)$ itself (window $U \le X^{1/4}$, cost $\pi U$) bypasses the average-to-pointwise obstruction: it does convert pointwise $P$ into a windowed $L^1$ target, but since the uniform bandwidth is $c_HX^{-1/4}$, every admissible window is again sub-coherence for every active $D$, so no oscillatory gain is created there either. The obstruction is structural: admissible window length ($\le X^{1/4}$, target-forced) equals the uniform coherence length ($\asymp X^{1/4}$, forced by $H_D \asymp DX^{-1/4}$).

### D. Unpaired exact-resonance lemmas (objective 4)

Parametrize $(h,d) \leftrightarrow (p,q,t)$, $h = pt$, $d = qt$, $\gcd(p,q)=1$, $t \ge 1$; each value's representation weight satisfies $\sum_{t:\,qt\in\mathcal D}\frac{1}{|p|t} \le \frac{C}{|p|}$, and $|p| \le qH/D$, $q \ge D/H$ for nonemptiness.

Lemma U-2 (reduced-denominator cross-paired, value-unpaired). Consider exact $N = 0$ tuples with $q_1 = q_2 = Q_a$, $q_3 = q_4 = Q_b$ (pattern $(12)(34)$; pattern $(14)(23)$ is identical after relabeling). The resonance is $(p_1-p_2)/Q_a = (p_4-p_3)/Q_b$; with $g = \gcd(Q_a,Q_b)$, $Q_a = g\sigma_1$, $Q_b = g\sigma_3$, coprimality forces $p_1 - p_2 = \sigma_1\kappa$, $p_4 - p_3 = \sigma_3\kappa$ for a single $\kappa \in \mathbb Z$. The case $\kappa = 0$ is exactly fraction-matching (`M9-M2-fraction-matching-weighted-bound`, cited not re-proved). For $\kappa \ne 0$: nonemptiness of the $p$-ranges forces $|\kappa| \le 2gH/D$, hence $g \ge D/(2H)$; the shifted harmonic sums give $\sum_{p_1}\frac{1}{|p_1||p_1-\sigma_1\kappa|} \ll \log(4H)/(\sigma_1|\kappa|)$ and similarly in $(p_3,p_4)$, so
$$
\Sigma_{U2} \ \ll\ \log^2(4H)\sum_{g \le 2D}\ \sum_{\sigma_1,\sigma_3 \le 2D/g}\frac{1}{\sigma_1\sigma_3}\sum_{\kappa\ne0}\frac{1}{\kappa^2} \ \ll\ D\,\log^4 X .
$$

Lemma SS (same-side reduced pairing). For $q_1 = q_3 = Q_a$, $q_2 = q_4 = Q_b$ the resonance is $(p_1+p_3)/Q_a = (p_2+p_4)/Q_b$, forcing $p_1+p_3 = \tau_a\nu$, $p_2+p_4 = \tau_b\nu$ with $Q_a = g\tau_a$, $Q_b = g\tau_b$. The case $\nu = 0$ is contained in the anti-paired class below; for $\nu \ne 0$ the identical computation gives $\Sigma_{SS} \ll D\log^4X$.

Anti-paired class ($\mu = 0$ in NF-1): $x_3 = -x_1$, $x_4 = -x_2$, free $x_1, x_2$; its total mass is $\big(\sum_{q\le 2D}\sum_{1\le|p|\le qH/D}\frac{C^2}{p^2}\big)^2 \ll D^2$, within the $D^2X^\epsilon$ budget (and always inside the SS pattern, since $x_3 = -x_1$ forces $q_3 = q_1$).

Coverage statement. The three perfect matchings of four indices are $(12)(34)$, $(14)(23)$, $(13)(24)$; a tuple whose reduced-denominator multiset has the form $\{q,q,q',q'\}$ admits at least one equal-$q$ matching and is therefore covered by fraction-matching or pair-swap (value-paired, cited from state), U-2 (cross patterns, $\kappa\ne0$), SS ($\nu\ne0$), or anti-paired -- total $\ll D^2X^\epsilon$ under H4-magnitude. Residual class (URES): exact $N=0$ tuples whose $q$-multiset is not of the form $\{q,q,q',q'\}$ (all distinct, or exactly one repeated value). By NF-1 these carry the lcm/numerator coincidence structure; by NF-2 each participating $q_1$ must satisfy $\gcd(q_1,Q)^2 \ge Qq_1/(2D)$ for the common value $\mu/Q$. The residual is nonempty: $\frac{1}{6k}+\frac{1}{10k} = \frac{1}{15k}+\frac{1}{5k}$ for every $k \ge 1$ (verified, including its normal-form data $Q = 15k$-scaled, $\mu = 4$, $e_{13} = 2$, $e_{24} = 1$ at $k=1$), giving residual mass $\ge cD$ in suitable blocks; so the residual must be bounded, not emptied. Exact reformulation: with $R(r) := \sum_{x_1+x_3 = r} \tilde w(x_1)\tilde w(x_3)$ over representation-weighted values, the full exact mass is $\sum_r R(r)^2$; the target is $\sum_{r} R(r)^2 \ll D^2X^\epsilon$, with $R(0) \ll D$ proved (anti-paired) and the danger concentrated, via NF-2, at values $r = \mu/Q$ with small $Q$; the smallest available $Q \asymp D/H$ gives $R \lesssim H$, and a window-count heuristic predicts $\sum_{r\ne0}R(r)^2 \asymp DH\,\mathrm{polylog} = D^2X^{-1/4+o(1)}$, comfortably inside budget. This heuristic is not a proof; it defines the A3 diagnostic below.

### E. SPD route (objective 5, kept exploratory)

Swapping sums, $S_2(D;X) = \sum_{d\in\mathcal D} w_D(d)\,G_H(X/(4d))$ with $G_H(\theta) = -\frac2\pi\sum_{h\ge1\ \mathrm{odd}}\frac{\Phi(h/(H+1))\chi_4(h)}{h}\cos(2\pi h\theta)$, a smoothed square wave (the unsmoothed series equals $-\frac12\operatorname{sq}(\theta)$ with $\operatorname{sq} = +1$ on $(-\frac14,\frac14)$ mod 1). So `M9-M2` is a signed discrepancy statement for the points $\theta_d = X/(4d)$ against the interval $(-\frac14,\frac14)$ at resolution $1/H$, with target square-root cancellation $\sqrt D$ at the endpoint. Needed first-spacing statistic:
$$
P(D,H;X) := \#\{(d_1,d_2)\in\mathcal D^2:\ d_1\ne d_2,\ \|X/(4d_1)-X/(4d_2)\| \le 1/H\},
$$
Poisson prediction $\asymp D^2/H + D$. Falsification test for A3: on a grid $X \in \{10^{10},10^{12}\}$, $D \in \{X^{0.3}, X^{0.4}, X^{0.5}\}$, $H = \lceil DX^{-1/4}\rceil$, compute $P(D,H;X)$; if at any grid point $P > 100\,\log^3X\,(D^2/H + D)$, record the SPD $L^2$ mechanism as failing at that scale (diagnostic only). Companion: $|S_2^{\mathrm{true}}|$ versus the median of 50 random-sign surrogates; a persistent power-size gap in either direction is the second falsifier/indicator.

## Theorem-dependency audit

1. `M9-M2-beta-algebra` (`derived_under_assumptions`): supplies $\beta$ support parity (DP-0/1) and magnitude $|\beta_h|\le K/|h|$ (DP-2/3, U-2, SS, anti-paired, EQ, LV). Every lemma consuming it inherits `derived_under_assumptions`; the H4 source audit remains the blocker.
2. `M9-M2-fourth-moment-expansion` (`derived_under_assumptions`): supplies the $N$, $\lambda$, $\Pi$ formulas used everywhere.
3. `M9-M2-harmonic-convolution-LH` (`proved_internal`): used quantitatively in DP-2, U-2, SS; hypotheses (range $H$, shift $\ne 0$) verified at each use, including the range-$2H$ variant.
4. `M9-M2-average-to-pointwise-AP-lemma` (`proved_internal`): referenced; shown redundant for EQ (a direct inf-plus-drift argument suffices).
5. `M9-M2-denominator-paired-weighted-bound` and `M9-M2-fraction-matching-weighted-bound` (`derived_under_assumptions`): cited as the $L=0$ and $\kappa=0$ cases; not re-proved.
6. NF-1/NF-2, Lemma W/B: pure integer/normalization statements; NF-2 and W/B use no external theorem and no H4 magnitude (W/B uses only the convention $H \le c_HDX^{-1/4}$).
7. No Vaaler, Li--Yang, Huxley, or Bourgain--Watt theorem is imported; Li--Yang remains a source-audit guardrail only (relevant to the endpoint exploration note).
8. Missing theorem statements deliberately not assumed: the diagonal-dominance of $\frac1X\int|S_2|^2$ (needed only for the negative direction of the moment-hierarchy map; flagged as hypothesis), and all $G_{2k}$ upper bounds (route map is conditional).

## Hidden assumptions and potential gaps

1. Coefficient freezing: all lemmas are for fixed $(H_D, \beta)$ per block, matching M9's fixed-coefficient phrasing; global-moment statements over $[X,2X]$ assume the frozen model, and unfreezing needs the $\Phi$-regularity item already on the H4 audit list.
2. Single-parity support: DP-0/1 fail under mixed-parity $\beta$-support; the audit must confirm the $\rho\in\{1,3\}$ combination yields pure-odd (or at least single-parity) support.
3. Dyadic conventions: constants in DP-1's threshold $(2X/C_0)^{1/2}$ assume $d\in[D,2D)$ and $D \le X^{1/2}$; a different top-block convention shifts the constant, not the structure.
4. Overlap bookkeeping: U-2/SS/anti-paired are value-level classes; integer-level families (DP, pair-swapped) overlap them. Union upper bounds are safe; any exact taxonomy accounting by A1 must avoid double-counting and must not treat my coverage statement as exhausting exact $N=0$ (the residual URES is open and nonempty).
5. The bandwidth conclusion (Lemma B and EQ) depends on $H_D \le c_HDX^{-1/4}$; if a future variant enlarges $H_D$, windows regain oscillation and the analysis must be redone.
6. In DP-2, the comparability $|u|\asymp|v|$ needs $D > C_0$; harmless since $D \ge X^{1/4}$, but the constant appears in the lemma statement.
7. The heuristic $\sum_{r\ne0}R(r)^2 \asymp DH$ ignores $e$-factor multiplicities in NF-1; treat strictly as a prediction to test.
8. LV's negative endpoint statement is conditional on the diagonal floor; I did not prove the off-diagonal control for the second moment, so the impossibility claim is scoped and hypothesis-labeled.

## Counterexample or obstruction search

1. DP parity: exhaustive search at $D=8$, $H=5$, all-odd $h_i$, over all $(a,b,h_1,\dots,h_4)$ found no tuple with $0<|N|<2ab$ -- consistent with DP-0.
2. $|u|\asymp|v|$ forcing: 20{,}000 random trials found no violation of $|u|\le2|v|$, $|v|\le2|u|$ under $|ub+va|\le3$.
3. NF-2 formula: 50{,}000 random reduced pairs confirmed $q_3 = g\hat Q\hat q_1/\gcd(g,M)$ and the lower bound $q_3 \ge Qq_1/g^2$ with zero violations; 50{,}000 trials confirmed the U-2 divisibility structure ($\sigma_1\mid p_1-p_2$ with a common $\kappa$).
4. Residual nonemptiness: the family $\frac{1}{6k}+\frac{1}{10k} = \frac{1}{15k}+\frac{1}{5k}$ is verified exactly for sample $k$, with the predicted normal-form data; this refutes any hope that the residual class is empty and calibrates its mass at $\ge cD$.
5. Obstruction identified this round: the sub-coherence window equivalence (C7/C8). It limits the scope of all $t$-averaging components in the fourth-moment route; it does not close the fourth-moment program (global moments, moment hierarchy, and mass bookkeeping retain content) and says nothing against direct signed/SPD or transform-based routes.

## Verification

Finite diagnostics executed this session (diagnostic only, not state evidence): (i) $C_h = i^h - (-i)^h$ identity, even-$h$ vanishing, evenness of $\chi_4(h)/h$ -- all pass; (ii) the DP exhaustive check above; (iii) the NF-2 and U-2 randomized structural checks above; (iv) bandwidth table: at $X = 10^8$, $\delta\lambda_{\max} = 1.00, 0.32, 0.10, 0.025, 0.01$ for $D = X^{0.25}, X^{0.3}, X^{0.375}, X^{0.45}, X^{0.5}$, and the $N$-threshold to $N_{\max}$ ratio crosses $1$ near $D \approx X^{0.42}$, confirming that the sharp statement lives in $\lambda$, not $N$; (v) moment-hierarchy thresholds $\frac{k-1}{2(k+1)} = 0.167, 0.25, 0.333, 0.409, 0.48$ for $k = 2,3,5,10,50$; (vi) trivial-block check: $2K(1+\log H)D/X^{1/4} \approx 2$ at $D = X^{1/4}$, growing at $X^{0.26}$ -- the trivial range ends just above the bottom block, as claimed. All proofs above were additionally checked by hand at the equality/singular cases: $a=b$, $u$ or $v$ zero, $\ell'=0$, $\kappa=0$, $\nu=0$, $\mu=0$, and the endpoint $D = X^{1/2}$.

## Divergent alternatives and 20% exploration

1. Endpoint focal structure. At $D \asymp X^{1/2}$, write $d = \lfloor X^{1/2}\rfloor + m$: the phase $X/(4d)$ expands with a linear term $-m/4$ (a period-4 character in $m$, meshing with $\chi_4$) plus a quadratic term $m^2/(4X^{1/2})$ and non-negligible higher terms. The endpoint block is thus a genuinely polynomial-phase (Bombieri--Iwaniec/exponent-pair) regime rather than an elementary one; the exact first lemma to attempt is a bound for $\sum_{m\asymp M} e(-hm/4 + h m^2/(4X^{1/2}) + O(hm^3/X))$ with the cubic kept, for individual odd $h \le X^{1/4}$. This reinforces the priority of the Li--Yang source audit as a guardrail before any import; falsification test: if a single-$h$ vdC/Gauss-sum treatment cannot beat $D^{1/2+1/6}$ per $h$ in a toy computation, the elementary version of this idea fails.
2. Range-split strategy. Given the moment-hierarchy map, propose splitting `M9-M2` into `M9-M2-subendpoint` ($X^{1/4} \le D \le X^{1/2-\eta}$: target the conditional $G_{2k}$ program with $k \asymp 1/\eta$, all bounds still to be proved) and `M9-M2-endpoint-block` ($D \asymp X^{1/2}$: $h,d$-cancellation only). Quick falsifier for the sub-endpoint program: A3 computes empirical $G_6/X$ at $D = X^{0.35}$ and compares with $D^3$; a persistent excess by a power indicates the diagonal-dominance assumption fails already at $k=3$.
3. Square-wave/divisor bridge. Since $G_H$ is a smoothed square wave, $S_2$ is a signed count of $d\in\mathcal D$ with $\{X/(4d)\}\in(\pm\frac14)$; this connects to counting divisor-like points in intervals and suggests comparing against known discrepancy results for $\{N/d\}$ sequences; needed lemma: an $H$-resolution discrepancy bound for $\{X/(4d)\}_{d\asymp D}$ of size $D^{1/2}X^\epsilon$; quick test: A3 empirically measures this discrepancy at the endpoint scale.

## Useful lemmas

For `state/lemma_bank.md` (proposed entries, statements as in Detailed reasoning): DP-0 (parity dichotomy), DP-1 (thin-band emptiness threshold $(2X/C_0)^{1/2}$), DP-2 (thin DP mass $\le C C_0K^4D\log^2 2H$), DP-3 (full DP mass $\le 4K_1^4D^2$), NF-1 (normal form, compact form above), NF-2 (participation rigidity, unconditional), W/B (window multiplier and uniform sub-coherence bandwidth $\delta|\lambda| \le c_HX^{1/4}/D$), EQ (`(LFM)`--pointwise equivalence at target precision), LV (large-value propagation $V^{2k+1} \le 2^{2k+1}\pi KH\,G_{2k}$), U-2 and SS (unpaired $\{q,q,q',q'\}$-pattern masses $\ll D\log^4X$), anti-paired bound ($\ll D^2$), trivial-block bound ($|S_2| \le 2K(1+\log H)D$), and the graded global formulation: the global fourth moment at level $D^2X^\epsilon$ follows from $\Sigma_{\mathrm{abs}}(0<|N|\le M) \ll X^\epsilon D^2\max(1, MX/D^4)$ for all $M$, with the tail part trivially satisfied for $D \le X^{3/8}$.

## What should be tested next

For A3 (all `diagnostic_only`, with scripts, commands, tables, precision logs, reports, pass/fail assertions): (t1) residual-mass enumeration -- exact $N=0$ tuples with $q$-multiset not of form $\{q,q,q',q'\}$, absolute $\beta$-weighted mass versus $D^2$ and versus the $DH$ prediction, including detection of the $(5,6,10,15)k$ family; (t2) $\max_{r\ne0}R(r)$ and $\sum_{r\ne0}R(r)^2$ against $DH\,\mathrm{polylog}$; (t3) window-equivalence check -- sample $\frac1\delta\int_I|S_2|^4$ versus $|S_2(X_0)|^4$ on coherence windows across $D$ (predicted ratio $1+O(X^{-1/4}\text{-scale drift})$); (t4) the SPD statistic $P(D,H;X)$ and signed/unsigned/random-sign comparison with the stated falsification thresholds; (t5) assertion tests for DP-1 (no DP tuple with $0<|N|<2D^2$ in any enumeration) and for the DP-2 unique-solution count. For A1: fold the DP suite, NF-1/NF-2, W/B/EQ, and U-2/SS into `best_proof_draft.md` and `lemma_bank.md`; record the parity-structure item on the H4 audit checklist. For A2: attack (URES) using NF-2's divisor constraint, or produce a lower-bound family exceeding $D^2X^{-1/4}$.

## Proposed state patch, if any

Proposed for judge consideration (ids from `state/proof_obligations.yml`; JSON-compatible YAML fragments, judge to finalize):

- id: M9-M2-DP-near-collision-bound
  status: derived_under_assumptions
  change: keep status; add this response as positive evidence (validator-ready dyadic proof with constants, parity cases, C0 dependence); next_action: A1 to transcribe DP-0..DP-3 into best_proof_draft.md; add H4 parity-structure check to the audit list.
- id: M9-M2-coprime-rigidity-normal-form
  status: proved_internal
  change: no status change; attach the compact NF-1 lemma-bank text from this response.
- id: M9-M2-NF-participation-rigidity
  type: lemma
  status: proved_internal
  statement_tex: For reduced r=mu/Q (mu nonzero) and reduced x1=p1/q1 with x3=r-x1 nonzero, q3 = g*Qhat*q1hat/gcd(g,M) with g=gcd(Q,q1), M=mu*q1hat-p1*Qhat; hence q3 >= Q*q1/g^2, and q3<=2D forces gcd(Q,q1)>=sqrt(Q*q1/(2D)) and gcd(g,M)>=Q*q1/(2D g).
  dependencies: [M9-M2-coprime-rigidity-normal-form]
  evidence: this response plus 50000-case randomized check (diagnostic).
- id: M9-M2-unpaired-reduced-paired-bound
  type: lemma
  status: derived_under_assumptions
  statement_tex: Under the H4 beta magnitude, exact N=0 tuples whose reduced-denominator multiset is {q,q,q',q'} have absolute beta-weighted mass << D log^4 X (value-unpaired part) plus D^2 (anti-paired) plus the fraction-matching bound; combined << D^2 X^eps.
  dependencies: [H4, M9-M2-beta-algebra, M9-M2-fourth-moment-expansion, M9-M2-harmonic-convolution-LH, M9-M2-fraction-matching-weighted-bound]
  blockers: [H4-source-audit]
- id: M9-M2-subcoherence-window-equivalence
  type: obstruction
  status: derived_under_assumptions
  statement_tex: On windows delta=X^(1/2)/D, every fourth-moment tuple satisfies delta*|lambda| <= c_H X^(1/4)/D <= c_H for all active D, so the window multiplier admits no power decay; combined with drift <= (pi K c_H/2) X^(1/4), the (LFM) statement at threshold X^(1+eps) is equivalent at target precision to the pointwise bound on the window. Any (LFM) proof must supply the full h,d-space cancellation.
  dependencies: [M9-M2-fourth-moment-expansion, M9-M2-beta-algebra]
- id: M9-M2-unpaired-residual-URES
  type: lemma
  status: open
  statement_tex: For the representation-weighted R(r), prove sum over r nonzero of R(r)^2 << D^2 X^eps restricted to reduced-denominator multisets not of the form {q,q,q',q'}; the class is nonempty (mass >= cD via the (5,6,10,15)k family).
  next_action: attack via NF-2 divisor rigidity; A3 tests t1-t2.
- id: M9-M2-local-fourth-moment-LFM
  status: open
  change: keep open; revise next_action: the fat-band phrasing in N is lossy (band contains all tuples for D >> X^(1/4)); route content must come from graded mass bounds over the full |N| range plus signed cancellation, or from the global-moment/moment-hierarchy program for D <= X^(1/2-eta).
- id: M9-M2-fourth-moment-average-to-pointwise
  status: open
  change: keep open; add subcoherence-equivalence evidence; note the moment-hierarchy range map (k >= (1-eta)/eta for D = X^(1/2-eta)) as a conditional strategy, endpoint excluded under the diagonal-floor hypothesis.
- id: M9-near-collision-estimate
  status: proposed
  change: recast statement as the graded global form: Sigma_abs(0<|N|<=M) << X^eps D^2 max(1, M X/D^4) for all M, sufficient for the global fourth moment at D^2 X^eps; note trivial tails for D <= X^(3/8).

No change proposed to `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy` statuses, `GC-target`, or `Conditional-bridge`.

## Confidence

DP suite proofs (C1--C4): 0.87 conditional on the stated H4 support/magnitude hypotheses; the algebra is short and machine-spot-checked. NF-1 compact form and NF-2 (C5--C6): 0.88; NF-2 is elementary and randomized-verified. Bandwidth/equivalence findings (C7--C8): 0.85 for the mathematics; 0.75 that the framing will be accepted as the right re-scoping of `(LFM)` (it corrects my own Round 5 emphasis). LV and the range map (C9--C10): 0.8 for the inequalities as stated; the negative endpoint conclusion is explicitly conditional on the diagonal floor, confidence 0.6 that the hypothesis holds as expected. Unpaired lemmas U-2/SS/anti-paired (C11): 0.82; the main risk is bookkeeping of overlaps and the exact class definitions, which I have tried to state set-theoretically. URES prediction (C12): heuristic only, 0.5. Overall round contribution: narrows the exact $N=0$ taxonomy to a well-defined residual with a rigidity handle, completes the assigned DP write-ups, and replaces a partially illusory $t$-averaging target with a precise statement of where the remaining difficulty lives; no endpoint or `M9-M2` progress is claimed.

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 6.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet or continuing your own proof attempt.

You should, however, give research-strategy adjustment recommendations based on the other agents' responses and your confidence in them. Recommend whether the next round should continue the main route, pivot to a different coordinate or theorem, allocate an agent to counterexample search, deepen a numeric certificate, or reserve exploratory effort for an alternative proof path.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.

## Prompt-Enforced Generation Mode

Low-temperature review mode: behave as a low-variance conservative referee. Optimize for exact formula checking, explicit assumptions, narrow provisional claims, and reproducible verification tasks. Do not optimize for novelty, rhetorical force, broad synthesis, or route advocacy. When multiple phrasings are possible, choose the least conclusive neutral phrasing. Keep creativity low and calibration high. Prefer boring exactness over memorable language. Low-temperature mode controls style only; it does not reduce the need for concrete evidence. If a draft is below the hard minimum, expand with neutral formula-level checks, theorem-hypothesis audits, boundary-case verifications, or explicit falsification tests, not with rhetoric. Score idea quality separately from proof-graph evidence: useful routes may receive credit in prose while state-promotable evidence remains low. Before finalizing, perform a visible approximate word-count self-check. Target 5000-7000 words, with hard minimum 4500 words. If token-family rewriting drops the draft below 4500 words, add neutral mathematical content using additional theorem-hypothesis audit, boundary-case verification, symbolic stress tests, or proof-draft-ready formula audit. Before finalizing, perform a rewrite pass that removes high-certainty, route-closing, finality/permanence, and dramatic wording, then confirm `token-family scan: passed` in the calibration section only if the scan is actually true for the answer body.

## Agent Depth Contract

Standing A2 review standard: write a deep Stage B referee report, not a compact verdict. Target 5000-7000 words; hard minimum 4500 words. If the first draft is shorter, continue expanding before finalizing with concrete mathematics only. Review every other active agent separately and in detail. Include at least 12 top-level `##` sections, a claim ledger with at least 8 reviewed claims, a theorem-dependency audit with at least 6 named dependencies or missing theorem statements, an unsupported-closure/overclaim audit, at least 4 explicit correction or verification items, at least 4 hidden assumptions or failure modes, at least 3 concrete stress tests or numerical/symbolic checks, a required split score table for every other active agent, an explicit `## Confidence` section, and a visible pre-submit calibration check. Split scores into idea quality, state evidence, and calibration; do not collapse useful ideas and proof-graph evidence into one vague rating. For each reviewed agent, identify strongest contribution, exact assumptions, claims that are proved versus derived-under-assumptions versus heuristic, likely false or underspecified statements, missing theorem hypotheses, what would falsify the contribution, and one concrete next verification task. Every major criticism must quote or restate the exact mathematical object being criticized, then give a formula-level reason. Do not reward elegant but uncertified asymptotics, spacing claims, signed-trace claims, Mellin-Perron claims, or Fourier-tail claims unless constants, hypotheses, boundary cases, and error terms are explicit. Use neutral referee language; do not quote, paraphrase, list, or mention prohibited rhetoric examples, even when saying they were avoided. Do not use numeric confidence above 0.89, percentage-allocation rhetoric, totalizing closure claims, dramatic verdict words, finality/permanence language, or lock-in route language. Before finalizing, mechanically replace finality/permanence/lock-in wording with provisional audit wording, then run a hard token-family scan and report only `token-family scan: passed` without listing the scanned roots. End with research-strategy implications and next-round recommendations.



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
