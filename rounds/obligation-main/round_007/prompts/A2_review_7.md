You are Gemini Pro Deep Think, acting as independent alternative strategist, obstruction finder, and referee-style reviewer.

Review the other agents' Round 7 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

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

This is Stage B cross review for Round 7.

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

## Outputs To Review

--- OUTPUT FROM A1 ---
## Summary

Source basis: this is the requested Round 7 Stage A independent reasoning for A1, using `A1_reasoning_7.md` and the included Round 6 state bundle as controlling context.

No proof of `M9`, `M9-M2`, `M9-M1`, or `GC-target` is obtained here. The safe Round 7 conclusion is narrower:

- the Vaaler/H4 source-card content can be written in proof-draft form, but H4 remains `source_audit_required`;
- the $\Phi$ regularity calculation is internally checkable once Vaaler's coefficient formula is accepted, but remains H4-dependent;
- the R5 positive-Fejer product-count proof should remain `derived_under_assumptions` pending H4 source-card validation;
- the local fourth-moment route on coherence windows is not a relaxed averaging route, because the window multiplier has no power-scale decay throughout the full active range;
- the main M9 work should now separate three routes: URES exact-resonance control, graded global near-collision or global-moment control, and sign-preserving reciprocal discrepancy / Poisson endpoint control;
- no state promotion is justified from this reasoning alone.

The main mathematical recommendation is to keep proof-draft maintenance as A1's Round 7 contribution while pushing analytic proof effort toward `M9-M2-unpaired-residual-URES` and sign-preserving endpoint mechanisms. The URES route is the best proof-graph-local route; the sign-preserving endpoint route is the best backup if exact-resonance bookkeeping does not yield pointwise M2.

## Target proof obligation

Primary A1 target obligations from the Round 7 prompt:

- `H4-source-audit`
- `H4-Phi-regularity`
- `R5-Full-reconciliation`
- `M9-M2-beta-algebra`
- `M9-M2-local-fourth-moment-kernel`
- `M9-M2-subcoherence-window-multiplier`
- `M9-M2-LFM-pointwise-equivalence`
- proof-draft maintenance

Related active bottleneck obligations:

- `M9-M2-character-factor`
- `M9-near-collision-taxonomy`
- `M9-M2-unpaired-residual-URES`
- `M9-near-collision-estimate`
- `M9-endpoint-uniformity`
- `M9-M2-reciprocal-SPD-route`
- `M9-M2-sign-preserving-poisson-voronoi-route`

The governing conditional bridge remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is still conditional. `M9` is open.

The active fixed-coefficient M9 target is:

$$
\mathcal M_i(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

for $i=1,2$, uniformly for

$$
X^{1/4}\le D\le X^{1/2}.
$$

This response focuses on $\mathcal M_2$ because the current round targets its character factor, exact/near-collision taxonomy, local fourth-moment obstruction, and diagnostics.

## Main claim or direction

The main A1 claim for Round 7 is:

**Claim A1-R7.1, status `derived_under_assumptions`:** Assuming the H4/Vaaler convention

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

the $\mathcal M_2$ coefficient is

$$
\beta_{h,H}
=
\alpha_{h,H}\left(e(h/4)-e(3h/4)\right)
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)\mathbf 1_{2\nmid h}.
$$

It is real and even. This confirms the M2 single-parity support and the retained $\chi_4$ frequency sign.

**Claim A1-R7.2, status `derived_under_assumptions`:** The R5 residual proof should be written as a pointwise positive-Fejer product-count proof, not as a Fourier-coefficient or RMS argument. The crucial count is

$$
\#\{d\asymp D:\|X/d\|\le \Delta\}
\ll_\epsilon (1+\Delta D)X^\epsilon,
$$

and similarly for shifted legs

$$
\left\|\frac{X/d+\rho}{4}\right\|\le \Delta,
\qquad \rho\in\{1,3\}.
$$

Together with

$$
K_H(t)\ll \min\left(H,\frac{1}{H\|t\|^2}\right)
$$

and $H_D\asymp D X^{-1/4}$, this gives the accepted R5 scale

$$
\frac1H\sum_{d\asymp D}K_H(T_d)
\ll_\epsilon X^{1/4+\epsilon}.
$$

This remains H4-dependent because the residual majorant comes from Vaaler.

**Claim A1-R7.3, status `proved_internal` after accepting the already-created kernel and subcoherence lemmas:** On local coherence windows

$$
\delta=\frac{X^{1/2}}{D},
$$

the fourth-moment phase multiplier gives no power-scale decay throughout the entire active range. Indeed, for

$$
\lambda
=
\frac14
\left(
\frac{h_1}{d_1}
-
\frac{h_2}{d_2}
+
\frac{h_3}{d_3}
-
\frac{h_4}{d_4}
\right),
$$

with $|h_i|\le H_D$ and $d_i\asymp D$,

$$
|\lambda|\ll \frac{H_D}{D}\asymp X^{-1/4},
$$

so

$$
\delta|\lambda|
\ll
\frac{X^{1/2}}{D}X^{-1/4}
=
\frac{X^{1/4}}{D}
\le 1.
$$

Equivalently, in the cleared numerator

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

the local fat band is

$$
|N|\ll \frac{D^4}{\delta}=D^5X^{-1/2}.
$$

The natural maximum scale is

$$
|N|\ll H_DD^3\asymp D^4X^{-1/4},
$$

and since

$$
\frac{D^5X^{-1/2}}{D^4X^{-1/4}}
=
DX^{-1/4}\ge1
$$

for all active $D\ge X^{1/4}$, the local fat band contains the whole natural $N$-range up to constants. Thus coherence-window LFM is pointwise-strength; it is not a softened averaging problem.

The main route should therefore be proof-draft maintenance plus a route split:

1. URES exact-resonance route as the primary local proof-graph route.
2. Graded global near-collision / global moment route as a conditional sub-endpoint route, but only if paired with a pointwise large-value mechanism.
3. Sign-preserving reciprocal discrepancy or Poisson endpoint route as the backup route for actual endpoint M2.

## Detailed reasoning

### 1. H4 source-card normalization

Use the convention

$$
e(t)=e^{2\pi i t}.
$$

Vaaler's source is:

Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bulletin of the American Mathematical Society*, New Series, volume 12, number 2, pages 183--216, April 1985. The local PDF has the title page and printed pagination.

The project source card should record DOI

$$
10.1090/S0273-0979-1985-15349-2.
$$

External metadata search corroborates this DOI in several indices, although the official AMS page was not fetchable in this tool session and one search snippet displayed an inconsistent suffix. The source card should therefore record the project-required DOI but note that the official AMS metadata should be checked directly during repository source-card finalization.

The proof-draft mapping is:

- Vaaler Theorem 6, equation (2.28), supplies

$$
\widehat J(t)
=
\begin{cases}
1, & t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|, & 0<|t|<1,\\
0, & 1\le |t|.
\end{cases}
$$

The same theorem says $\widehat J$ is even, nonnegative, continuously differentiable, and strictly decreasing on $[0,1]$.

- Section 7 equations (7.1)--(7.3) define the periodic trigonometric polynomials $i_N$, $j_N$, and $k_N$, with $k_N$ the periodic Fejer kernel.

- Theorem 18 gives the periodic sawtooth approximation and residual majorant. In project notation the needed statement is

$$
|\psi*j_H(x)-\psi(x)|
\le
(2H+2)^{-1}k_H(x).
$$

The local PDF's rendered page 210 has Theorem 18 and equations (7.13)--(7.17), including equation (7.14), which is exactly the residual inequality in Vaaler's notation.

The project must still separate Vaaler's normalized sawtooth convention from the floor-compatible convention

$$
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12.
$$

At nonintegers there is no ambiguity. At integers, Vaaler's trigonometric polynomial gives zero while the floor-compatible sawtooth gives $-1/2$. The residual bound covers this because $k_H(n)=H+1$, so

$$
(2H+2)^{-1}k_H(n)=\frac12.
$$

This is the correct endpoint conversion. It should be written explicitly before H4 is used in the proof draft.

### 2. $\Phi$ regularity

Assuming Vaaler's Theorem 6 coefficient formula,

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1,
$$

we have the endpoint expansions.

As $u\to0$,

$$
\cot(\pi u)
=
\frac{1}{\pi u}
-
\frac{\pi u}{3}
+
O(u^3),
$$

so

$$
\Phi(u)
=
\pi u(1-u)
\left(
\frac{1}{\pi u}
-
\frac{\pi u}{3}
+
O(u^3)
\right)+u
=
(1-u)+u-\frac{\pi^2}{3}u^2+O(u^3).
$$

Thus

$$
\Phi(0)=1,
\qquad
\Phi'(0)=0.
$$

As $u\to1$, set $v=1-u$. Then

$$
\cot(\pi u)
=
\cot(\pi-\pi v)
=
-\cot(\pi v)
=
-\frac{1}{\pi v}
+
\frac{\pi v}{3}
+
O(v^3).
$$

Therefore

$$
\pi u(1-u)\cot(\pi u)
=
\pi(1-v)v
\left(
-\frac{1}{\pi v}
+
\frac{\pi v}{3}
+
O(v^3)
\right)
=
-(1-v)+O(v^2),
$$

and since $u=1-v$,

$$
\Phi(u)=O(v^2).
$$

Hence

$$
\Phi(1)=0,
\qquad
\Phi'(1)=0.
$$

The formula is smooth on compact subintervals of $(0,1)$ and the endpoint expansions show bounded first derivative on $[0,1]$. Thus

$$
\Phi\in C^1([0,1]),
\qquad
\sup_{0\le u\le1}|\Phi'(u)|<\infty.
$$

This supports coefficient freezing and local-height stability bookkeeping, but it does not validate H4 by itself. Its status should remain `derived_under_assumptions` with blocker `H4-source-audit`.

### 3. M2 beta algebra and parity support

The M2 shifted sawtooth difference produces the factor

$$
C_h=e(h/4)-e(3h/4).
$$

For even $h=2k$,

$$
C_h=e(k/2)-e(3k/2)=(-1)^k-(-1)^{3k}=0.
$$

For odd $h$,

$$
C_h=
\begin{cases}
2i, & h\equiv1\pmod4,\\
-2i, & h\equiv3\pmod4,
\end{cases}
=
2i\chi_4(h).
$$

Thus

$$
C_h=2i\chi_4(h)\mathbf 1_{2\nmid h}.
$$

Using

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

we get

$$
\beta_{h,H}
=
\alpha_{h,H}C_h
=
-\frac{\Phi(|h|/(H+1))}{\pi h}
\chi_4(h)\mathbf 1_{2\nmid h}.
$$

For negative $h$, since $\chi_4(-h)=-\chi_4(h)$, the quotient $\chi_4(h)/h$ is even. Hence

$$
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
$$

Equivalently,

$$
\beta_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{\pi |h|}
\chi_4(|h|)
\mathbf 1_{2\nmid h}.
$$

The official raw two-sided M2 block should therefore be written as

$$
\mathcal M_2(D;X)
=
4
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Because $\beta_h$ is even and real, the complex-weight cosine pairing is

$$
\sum_{1\le |h|\le H}\beta_h
\sum_d w(d)e(hX/(4d))
=
2\sum_{h=1}^H\beta_h
\sum_d w(d)\cos(2\pi hX/(4d)).
$$

This is valid for complex $w(d)$ if the same $w(d)$ is used in the $h$ and $-h$ raw terms.

For real weights, one may also write

$$
\sum_{1\le |h|\le H}\beta_h
\sum_d w(d)e(hX/(4d))
=
2\sum_{h=1}^H\beta_h
\operatorname{Re}
\sum_d w(d)e(hX/(4d)).
$$

For complex weights the $\operatorname{Re}B_h$ shortcut is false in general. A3 should keep this as an explicit regression test.

### 4. R5 positive-Fejer product count

The residual proof must be pointwise in $X$. The correct proof uses the positive Fejer majorant before expanding any Fourier series.

The Fejer bound is

$$
K_H(t)\ll \min\left(H,\frac{1}{H\|t\|^2}\right).
$$

The first-leg counting lemma is:

$$
A(\Delta)
=
\#\{d\asymp D:\|X/d\|\le \Delta\}
\ll_\epsilon
(1+\Delta D)X^\epsilon.
$$

Proof sketch: if $\|X/d\|\le\Delta$, then there is an integer $m$ with

$$
|X/d-m|\le\Delta.
$$

Multiplying by $d\asymp D$ gives

$$
|X-md|\le \Delta D.
$$

Thus the integer $n=md$ lies in an interval of length $O(1+\Delta D)$ around $X$. Each $n$ has at most $\tau(n)\ll_\epsilon X^\epsilon$ factorizations $n=md$ with $d\asymp D$. Hence the count.

The shifted-leg analogue is:

$$
A_\rho(\Delta)
=
\#\left\{d\asymp D:
\left\|
\frac{X/d+\rho}{4}
\right\|\le \Delta
\right\}
\ll_\epsilon
(1+\Delta D)X^\epsilon,
\qquad
\rho\in\{1,3\}.
$$

Indeed, the condition gives an integer $m$ with

$$
\left|
\frac{X/d+\rho}{4}-m
\right|
\le\Delta,
$$

hence

$$
|X-d(4m-\rho)|\le 4\Delta D.
$$

The factor $\ell=4m-\rho$ is positive in the large active range and has fixed congruence class modulo $4$. Again multiplicity is bounded by $\tau(n)$.

Now dyadically decompose by

$$
\|T_d\|\asymp \Delta_j=\frac{2^j}{H}
$$

for $j\ge0$, together with the central region $\|T_d\|\le H^{-1}$. Then

$$
\frac1H\sum_{d\asymp D}K_H(T_d)
\ll
A(H^{-1})
+
\sum_{j\ge0}
\frac{1}{H^2\Delta_j^2}A(\Delta_j).
$$

Using $A(\Delta)\ll_\epsilon(1+\Delta D)X^\epsilon$ gives

$$
\frac1H\sum_{d\asymp D}K_H(T_d)
\ll_\epsilon
\left(1+\frac{D}{H}\right)X^\epsilon
\ll_\epsilon
X^{1/4+\epsilon},
$$

because

$$
H=H_D\asymp DX^{-1/4}.
$$

The same proof applies to shifted legs. This is the proof-draft form of R5-Full. It remains conditional on H4 because H4 supplies the residual majorant.

### 5. Local fourth-moment kernel and whole-range subcoherence

For

$$
S_2(D;t)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(ht/(4d)),
$$

the fourth moment over an interval $I$ of length $\delta$ expands into terms with phase

$$
e\left(t\lambda\right),
$$

where

$$
\lambda=
\frac14
\left(
\frac{h_1}{d_1}
-
\frac{h_2}{d_2}
+
\frac{h_3}{d_3}
-
\frac{h_4}{d_4}
\right).
$$

Let

$$
Q=d_1d_2d_3d_4
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
h_4d_1d_2d_3.
$$

Then

$$
\lambda=\frac{N}{4Q}.
$$

The local kernel bound is

$$
\left|
\frac1{|I|}
\int_I e(tN/(4Q))\,dt
\right|
\ll
\min\left(1,\frac{Q}{\delta |N|}\right)
\asymp
\min\left(1,\frac{D^4}{\delta |N|}\right).
$$

For the coherence window

$$
\delta=\frac{X^{1/2}}{D},
$$

the fat band is

$$
|N|\ll D^5X^{-1/2}.
$$

But the whole natural range satisfies

$$
|N|
\ll
H_DD^3
\asymp
D^4X^{-1/4}.
$$

Since

$$
D^4X^{-1/4}\le D^5X^{-1/2}
$$

is equivalent to

$$
D\ge X^{1/4},
$$

the local fat band contains the entire phase range in every active dyadic block. Therefore the local fourth-moment kernel supplies no power saving.

This proves the conceptual point needed for the proof draft:

`M9-M2-local-fourth-moment-LFM` is not a relaxed average route. A proof of LFM on these windows must supply essentially the same $h,d$ cancellation as pointwise control. It should be treated as an equivalent-strength formulation, not as a softened path around endpoint uniformity.

### 6. URES exact-resonance route analysis

The exact resonance equation is

$$
\frac{h_1}{d_1}
-
\frac{h_2}{d_2}
+
\frac{h_3}{d_3}
-
\frac{h_4}{d_4}
=
0.
$$

Equivalently,

$$
x_1+x_3=x_2+x_4,
\qquad
x_i=\frac{h_i}{d_i}.
$$

Reduce each fraction:

$$
x_i=\frac{p_i}{q_i},
\qquad
(p_i,q_i)=1,
\qquad
q_i\le D.
$$

The dyadic lift is

$$
h_i=g_ip_i,
\qquad
d_i=g_iq_i,
\qquad
g_iq_i\asymp D,
\qquad
|g_ip_i|\le H_D.
$$

For fixed reduced $p/q$, the dyadic lift has $g\asymp D/q$, so the beta weight is approximately

$$
|\beta_{gp,H_D}|
\ll
\frac{1}{g|p|}
\asymp
\frac{q}{D|p|}.
$$

This motivates defining a reduced-fraction weight

$$
A(p/q)
=
\sum_{\substack{gq\asymp D\\1\le |gp|\le H_D}}
|\beta_{gp,H_D}|\,|w_D(gq)|.
$$

At proof-draft level one expects

$$
A(p/q)
\ll
\frac{q}{D|p|}X^\epsilon
$$

with support

$$
1\le |p|\ll qX^{-1/4}.
$$

For a reduced value $r=\mu/Q$, define a pair representation function

$$
R(r)
=
\sum_{\substack{x_1+x_3=r\\x_i=p_i/q_i\\q_i\le D}}
A(x_1)A(x_3),
$$

with paired/reduced-paired/fraction-matching classes removed according to the current taxonomy. The URES target is

$$
\sum_{r\ne0}R_{\mathrm{res}}(r)^2
\ll_\epsilon
D^2X^\epsilon.
$$

The NF-2 participation-rigidity lemma says: if $r=\mu/Q$ is reduced, $x_1=p_1/q_1$ is reduced, $x_3=r-x_1$ is nonzero with reduced denominator $q_3$, and

$$
g=\gcd(Q,q_1),
\qquad
\widehat Q=Q/g,
\qquad
\widehat q_1=q_1/g,
\qquad
M=\mu\widehat q_1-p_1\widehat Q,
$$

then

$$
\gcd(\widehat Q\widehat q_1,M)=1
$$

and

$$
q_3=
\frac{g\widehat Q\widehat q_1}{\gcd(g,M)}
\ge
\frac{Qq_1}{g^2}.
$$

Thus if $q_3\le 2D$, then

$$
g=\gcd(Q,q_1)
\ge
\sqrt{\frac{Qq_1}{2D}}.
$$

This is a genuine rigidity constraint: denominators participating in residual representations of $r$ must have large common factors with $Q$.

A first proof attempt should bound the participation weight for fixed $r=\mu/Q$:

$$
P(r)
=
\sum_{\substack{x=p/q\\r-x=p'/q'\\q,q'\le D}}
A(x)A(r-x).
$$

Using NF-2, split by $g=\gcd(Q,q)$ and write $Q=gb$, $q=ga$. The condition

$$
g\ge \sqrt{\frac{Qq}{2D}}
$$

becomes

$$
ab\le 2D.
$$

This transforms the problem into a divisor-weighted sum over large common divisors $g\mid Q$ and reduced numerator congruences

$$
M=\mu a-pb.
$$

The hoped-for bound is not pointwise $P(r)\ll1$; the target is the second moment

$$
\sum_r P_{\mathrm{res}}(r)^2\ll D^2X^\epsilon.
$$

A likely obstacle is that Egyptian-fraction identities, such as

$$
\frac1{6k}+\frac1{10k}
=
\frac1{15k}+\frac1{5k},
$$

give real residual exact resonances outside reduced-paired classes. However this family has only one scaling parameter $k$ and is not by itself above the $D^2X^\epsilon$ budget. A3 should search for multi-parameter families.

The URES route is not a proof of M2 by itself. It can at most clear the exact $N=0$ part of the fourth-moment taxonomy. Near-collisions and pointwise upgrade remain separate.

## Theorem-dependency audit

### H1--H3

Status: `proved_internal`.

These supply the balanced hyperbola and floor-compatible sawtooth reductions. They may be cited in the conditional bridge.

### H4 / Vaaler finite approximation

Status: `source_audit_required`.

The local PDF supports the required Vaaler theorem mapping, especially Theorem 6 and Theorem 18. The source card still must physically record bibliographic data, DOI, local PDF path, exact equations, notation translation, Fejer normalization, coefficient sign, residual constant, endpoint convention, $\Phi$ regularity, and M2 parity support.

No H4-dependent statement should be promoted beyond `derived_under_assumptions` until this is complete.

### R5-Full

Status: `derived_under_assumptions`.

The proof-draft route is pointwise product counting with positive Fejer majorants. It depends on H4 for the residual inequality.

### H4-Phi-regularity

Status: `derived_under_assumptions`.

The calculus proof is internal once the coefficient formula is accepted. It does not validate H4.

### M9-M2-beta-algebra

Status: `derived_under_assumptions`.

The algebra is direct under H4. It should be inserted into the proof draft but not treated as an independent external theorem.

### M9-M2-local-fourth-moment-kernel

Status: `proved_internal`.

The kernel calculation follows from elementary integration of exponentials after the fourth-moment expansion. It is algebraic infrastructure, not an estimate for M2.

### M9-M2-subcoherence-window-multiplier

Status: `proved_internal`.

The bound

$$
\delta|\lambda|
\ll
X^{1/4}/D
\le1
$$

is uniform over the active range. This re-scopes local fourth moments.

### M9-M2-LFM-pointwise-equivalence

Status: `derived_under_assumptions`.

This depends on the H4 beta magnitude and frozen coefficient bookkeeping. Its conceptual conclusion is sound: LFM is target-strength, not relaxed.

### M9-M2-NF-participation-rigidity

Status: `proved_internal`.

This is a rational normal-form lemma. It is the first serious tool for URES.

### M9-M2-unpaired-reduced-paired-bound

Status: `derived_under_assumptions`.

Useful for excluding reduced-denominator multiset $\{q,q,q',q'\}$ classes, but H4 remains a blocker.

### Li--Yang 2023

Status: `source_audit_required`; guardrail only.

Li and Yang's arXiv paper states an improvement for the Gauss circle and divisor problems with exponent $\theta^*=0.3144831759741\cdots$, using Bombieri--Iwaniec, a new first-spacing estimate, and Huxley second-spacing input. The arXiv page states the title, authors, and abstract, and the rendered source describes Theorem 1.2 and the $5/16$ barrier discussion. The uploaded local PDF confirms the same theorem statement and setup.

Li--Yang is not a black-box dependency for M9. Its theorem ranges, weights, and absolute-value placement remain unaudited for the exact fixed-Vaaler endpoint problem.

## Hidden assumptions and potential gaps

1. **H4 source-card is still not committed.** The proof-draft can contain the Vaaler mapping, but the graph status must remain `source_audit_required`.

2. **The DOI should be cross-checked from official AMS metadata.** The project state gives DOI `10.1090/S0273-0979-1985-15349-2`, and external indices corroborate it; however, an AMS search snippet showed an inconsistent suffix while the official page was not fetchable. The final source card should verify the official DOI directly.

3. **Vaaler's sawtooth convention must be translated explicitly.** At integers, $\psi_V(n)=0$ versus $\psi_F(n)=-1/2$ is harmless only because the Fejer residual gives exactly $1/2$ at integer points.

4. **R5 is pointwise, not averaged.** Any proof using $L^2_X$, RMS, or cancellation after Fourier expansion does not prove R5-Full.

5. **The beta sign is lost under common norms.** The $h$-Cauchy step replaces $C_h$ by $|C_h|^2=4\mathbf 1_{2\nmid h}$ and erases $\chi_4(h)$. Any route relying on character-blind Hilbert-Schmidt, Frobenius, Schur, trace, or operator-norm bounds should be marked diagnostic unless it preserves the sign elsewhere.

6. **Exact resonances do not prove M2.** Even complete exact $N=0$ taxonomy would leave near-collision bands and pointwise upgrade.

7. **Local LFM does not relax the problem.** On coherence windows, all fourth-moment tuples are phase-coherent at power scale.

8. **Global moments need a large-value mechanism.** A global fourth moment over $X\le t\le2X$ cannot by itself imply pointwise $|S_2|\ll X^{1/4+\epsilon}$ using only the crude derivative bound $|S_2'|\ll H_D$.

9. **URES lift multiplicities are delicate.** Reduced-fraction bounds must account for all lifts $h=gp,d=gq$, actual beta weights, dyadic truncation, parity, and overlap with already-treated classes.

10. **Endpoint $D\asymp X^{1/2}$ is structurally different.** At the top block $H_D\asymp X^{1/4}$ and the local window has length $\asymp1$. Average-to-pointwise and local smoothing devices degenerate there.

11. **M1 remains open.** Even a future proof of M2 would not prove M9 unless M1 is also uniformly bounded.

## Counterexample or obstruction search

### Obstruction 1: local fourth moment is pointwise-strength

The subcoherence calculation is already a structural obstruction to local-window smoothing. It does not rule out M2; it rules out the claim that LFM is easier merely because it is an average.

Fast falsification test for any LFM proof: identify the first step that produces decay from

$$
\frac1{\delta}\int_I e(tN/(4Q))\,dt.
$$

If the proof uses only $N$-spacing on $\delta=X^{1/2}/D$, it cannot produce power savings in the active range because the entire natural $N$-range lies in the fat band.

### Obstruction 2: exact URES families exist

The identity

$$
\frac1{6k}+\frac1{10k}
=
\frac1{15k}+\frac1{5k}
$$

shows that the residual class is nonempty. It is not enough to classify exact resonances by denominator pairing.

A3 should search for two- or three-parameter families of the same type. A lower-bound family with beta-weighted mass $\gg D^{2+c}$ for some $c>0$ would refute the URES absolute route.

### Obstruction 3: global moment plus derivative is too weak

Suppose one could prove the global fourth moment

$$
\int_X^{2X}|S_2(D;t)|^4\,dt
\ll_\epsilon X^{2+\epsilon}.
$$

Using only

$$
|S_2'(D;t)|\ll H_D\le X^{1/4},
$$

a large-value propagation argument gives, if $|S_2(D;t_0)|=V$, an interval of length $\gg V/H_D$ on which $|S_2|\gg V$. Hence

$$
X^{2+\epsilon}
\gg
\frac{V}{H_D}V^4
=
\frac{V^5}{H_D},
$$

so

$$
V\ll (H_DX^{2+\epsilon})^{1/5}
\le X^{9/20+\epsilon}.
$$

This is much weaker than $X^{1/4+\epsilon}$. Therefore a global fourth-moment route requires either a much stronger moment, a higher-moment large-value theorem, additional oscillation control, or a direct pointwise mechanism.

### Obstruction 4: sign-preserving routes can collapse under Cauchy

For any proposed SPD or Poisson route, the first serious norm estimate must be audited. If the route transforms the signed object into

$$
v^*U^*KUv
$$

and then bounds it by $\|K\|_{\mathrm{op}}\|v\|_2^2$ or by an absolute trace bound, then the $\chi_4$ structure is usually hidden in a diagonal unitary and has been erased.

A3's true beta / unsigned / random / adversarial comparison is a necessary falsification test.

### Obstruction 5: endpoint Poisson boundary terms

For the $d$-sum phase

$$
f(d)=\frac{hX}{4d},
$$

stationary phase after Poisson in $d$ has stationary relation

$$
m\asymp \frac{hX}{D^2}.
$$

At $D\asymp X^{1/2}$ and $h\asymp H_D\asymp X^{1/4}$, this gives

$$
m\asymp h.
$$

The dual is not length $1$; it is comparable to the $h$-range. Boundary terms, $m=0$, sign of $m$, and support-edge stationary points must all be included before this can become a theorem.

## Verification

A1 proof-draft verification checklist for this round:

1. **Vaaler source card.** Record title, author, journal, volume, issue, pages, date, DOI, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)--(7.3), Theorem 18 equations (7.13)--(7.17), coefficient sign, residual constant, Fejer normalization, endpoint convention.

2. **Phi regularity.** Insert the endpoint expansions showing $\Phi(0)=1$, $\Phi(1)=0$, $\Phi'(0)=\Phi'(1)=0$, and $\|\Phi'\|_\infty<\infty$.

3. **M2 parity support.** Verify $C_h=0$ for even $h$ and $C_h=2i\chi_4(h)$ for odd $h$.

4. **M2 pairings.** Insert raw two-sided, complex-weight cosine, and real-weight $\operatorname{Re}B_h$ formulas with hypotheses.

5. **R5 proof.** Insert the product-count proof in the order: positive residual majorant, Fejer pointwise bound, product count, dyadic shell sum.

6. **Local kernel.** Insert

$$
\frac1{|I|}\left|\int_I e(tN/(4Q))\,dt\right|
\ll
\min\left(1,\frac{D^4}{|I||N|}\right).
$$

7. **Subcoherence note.** Insert the calculation

$$
\delta|\lambda|\ll X^{1/4}/D\le1.
$$

8. **URES target.** Insert the representation target

$$
\sum_{r\ne0}R_{\mathrm{res}}(r)^2\ll_\epsilon D^2X^\epsilon
$$

with all dependencies and the known example $(6,10,15,5)k$.

9. **No promotions.** Do not update `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `GC-target`, or `H4` to a stronger status.

## Divergent alternatives and 20% exploration

### Alternative A: graded global near-collision estimate plus large-value theorem

The state currently proposes a graded near-collision estimate of the form

$$
\Sigma_{\mathrm{abs}}(M)
\ll_\epsilon
D^2
\max\left(1,\frac{MX}{D^4}\right)X^\epsilon.
$$

This is natural because $M\sim D^4/X$ is the global $X$-scale near-collision threshold, while larger $M$ should pay linearly in the band thickness.

However, this estimate alone is not enough for pointwise M2 unless paired with a pointwise extraction theorem. The local coherence obstruction shows that local windows do not produce power decay. Therefore this route should be stated as:

**Proposed theorem GNC-LV.** For some $p>4$ and active $D$, prove a global moment or large-value estimate strong enough that

$$
\#\{t\in[X,2X]: |S_2(D;t)|\ge V\}
$$

has a saving beyond derivative propagation, uniformly up to the endpoint. The theorem must imply

$$
|S_2(D;X_0)|\ll_\epsilon X_0^{1/4+\epsilon}
$$

for every $X_0$.

Fast falsification: show that the strongest available global moment plus $|S_2'|\ll H_D$ still gives only $X^{9/20+o(1)}$ or similar. Then this route needs a higher-order large-value theorem, not merely a fourth-moment count.

### Alternative B: endpoint sign-preserving reciprocal discrepancy

Define the endpoint discrepancy object

$$
P(D,H;X)
=
\sum_{\substack{1\le h\le H\\2\nmid h}}
\frac{\Phi(h/(H+1))}{h}\chi_4(h)
\sum_{d\asymp D}w(d)e(hX/(4d)).
$$

At $D\asymp X^{1/2}$ and $H\asymp X^{1/4}$, this is the hardest pointwise block. The proposed theorem would be:

**Proposed theorem SPD.** For $D\asymp X^{1/2}$, $H\asymp X^{1/4}$, and smooth dyadic $w$, the signed truncated sawtooth discrepancy at reciprocal points satisfies

$$
P(D,H;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is tautologically at target scale, so the value is in specifying a proof mechanism: either a sign-preserving spacing theorem for

$$
\theta_d=\frac{X}{4d}
$$

with Fourier-side coefficient $\chi_4(h)\Phi(h/(H+1))/h$, or a Poisson/B-process transformation retaining a nontrivial character in the dual variable.

Fast falsification: compare true beta signs against unsigned, random signs, and adversarial signs. If true beta signs do not improve the statistic, the route is low priority.

### Alternative C: Poisson/B-process first in the $d$ variable

For fixed $h$, apply Poisson to

$$
\sum_{d\asymp D}w(d)e(hX/(4d)).
$$

The stationary equation is roughly

$$
m=\frac{hX}{4d^2},
$$

so the dual range is

$$
m\asymp \frac{hX}{D^2}.
$$

At the endpoint $D\asymp X^{1/2}$ this gives $m\asymp h$, suggesting possible interaction between $h$ modulo $4$ and the dual variable $m$. At lower $D$, the dual length is larger.

The exact theorem required is:

**Proposed theorem SP-Poisson.** After Poisson in $d$, the transformed double sum over $(h,m)$ retains enough of the $\chi_4(h)$ structure to give

$$
\sum_h \beta_h \sum_m A(h,m;X,D)e(\Phi_{h,m}(X,D))
\ll_\epsilon X^{1/4+\epsilon},
$$

with all boundary, $m=0$, nonstationary, and support-edge terms bounded uniformly.

Fast falsification: if the first Cauchy step in $(h,m)$ erases $\chi_4(h)$ or if boundary terms alone reach $X^{1/4+c}$, this route fails in its current form.

## Route proposals

### Route 1: URES exact-resonance route

**Target lemma.**

Let $R_{\mathrm{res}}(r)$ be the residual pair-representation function after removing fraction-matching, denominator-paired, pair-swapped, semi-diagonal, reduced-paired, and sign-symmetric classes. Prove

$$
\sum_{r\ne0}R_{\mathrm{res}}(r)^2
\ll_\epsilon
D^2X^\epsilon.
$$

**Why it might work.**

NF-2 participation rigidity forces large common factors between $Q$ and any denominator $q$ participating in $r-x$ with denominator $\le D$:

$$
\gcd(Q,q)\ge \sqrt{Qq/(2D)}.
$$

This is a strong arithmetic restriction and may reduce URES to divisor sums over $Q$.

**Obstruction attacked.**

This directly attacks the remaining exact $N=0$ residual class blocking `M9-near-collision-taxonomy`.

**Dependencies.**

- `M9-M2-beta-algebra`, H4-dependent.
- `M9-M2-coprime-rigidity-normal-form`, proved internal.
- `M9-M2-NF-participation-rigidity`, proved internal.
- `M9-M2-unpaired-reduced-paired-bound`, H4-dependent.
- dyadic lift bookkeeping for beta weights.

**First proof step.**

For fixed reduced $r=\mu/Q$, prove a participation bound

$$
R_{\mathrm{res}}(r)
\ll_\epsilon
X^\epsilon
\sum_{\substack{g\mid Q\\\text{large}}}
\mathcal W(Q,g,D),
$$

where large means $g^2\gg Qq/D$, then square and sum over $r$.

**Fast falsification.**

A3 enumerates residual classes, including the $(6,10,15,5)k$ family, and detects

$$
\sum_rR_{\mathrm{res}}(r)^2\gg D^{2+c}
$$

for some stable $c>0$.

**Plausibility rank.**

Highest proof-graph locality, medium endpoint relevance. It can clear taxonomy but cannot prove M2 alone.

### Route 2: graded near-collision / global moment route

**Target lemma.**

For all relevant $M$,

$$
\Sigma_{\mathrm{abs}}(M)
=
\sum_{0<|N|\le M}
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|
\prod_j |w_D(d_j)|
\ll_\epsilon
D^2\max\left(1,\frac{MX}{D^4}\right)X^\epsilon.
$$

A signed variant may be separately proposed but must not be conflated with the absolute version.

**Why it might work.**

The exact $N=0$ paired classes already have $D^2X^\epsilon$ scale under H4. A linear band-thickness loss is the natural analogue for near-collisions.

**Obstruction attacked.**

It attacks `M9-near-collision-estimate`.

**Dependencies.**

- exact fourth-moment expansion;
- beta algebra;
- exact taxonomy;
- arithmetic spacing of rational sums;
- a pointwise upgrade or large-value theorem, not currently available.

**First proof step.**

Prove the bound for denominator-paired and reduced-paired near-collision classes with explicit $M$ dependence, then test residual classes.

**Fast falsification.**

At $D=X^{1/2}$, A3 finds absolute near-collision mass above the predicted linear-band scale, or the only available global moment plus derivative yields a pointwise exponent far larger than $1/4$.

**Plausibility rank.**

Medium as a counting program, low as a complete endpoint proof without a new large-value mechanism.

### Route 3: sign-preserving reciprocal discrepancy / Poisson endpoint route

**Target lemma.**

Prove directly that

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for active $D$, preserving the $\chi_4$ sign through the first nontrivial analytic estimate.

**Why it might work.**

The exact coefficient sign is the main information lost by absolute fourth moments. Endpoint blocks may have a dual structure after Poisson where $m\asymp hX/D^2$ and at $D\asymp X^{1/2}$ one has $m\asymp h$.

**Obstruction attacked.**

It attacks `M9-M2-character-factor` and `M9-endpoint-uniformity`.

**Dependencies.**

- beta algebra and parity support;
- exact stationary phase or reciprocal spacing theorem;
- boundary and $m=0$ estimates;
- no character-erasing Cauchy step.

**First proof step.**

Write the Poisson-transformed fixed-$h$ $d$-sum with exact amplitude and stationary point:

$$
m=\frac{hX}{4d^2}.
$$

Classify the dual range and boundary terms for $D=X^{1/4},X^{3/8},X^{1/2}$.

**Fast falsification.**

The first Cauchy/operator-norm step makes the result identical for true $\beta_h$, $|\beta_h|$, and random signs; or boundary terms alone exceed target scale.

**Plausibility rank.**

Best backup for endpoint pointwise M2, but currently `proposed`.

## Useful lemmas

### Lemma R7-L1: floor-compatible Vaaler endpoint conversion

Assuming Vaaler's residual inequality

$$
|\psi_V*j_H(x)-\psi_V(x)|\le (2H+2)^{-1}k_H(x),
$$

the same residual majorant controls the project convention $\psi_F(n)=-1/2$ at integer points because

$$
k_H(n)=H+1
$$

and therefore

$$
(2H+2)^{-1}k_H(n)=1/2.
$$

Status: `derived_under_assumptions`, dependency `H4-source-audit`.

### Lemma R7-L2: $\Phi$ endpoint regularity

Assuming

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

then $\Phi$ extends to $C^1([0,1])$ with

$$
\Phi(0)=1,\quad \Phi(1)=0,\quad \Phi'(0)=\Phi'(1)=0.
$$

Status: `derived_under_assumptions`.

### Lemma R7-L3: shifted R5 product count

For $\rho\in\{1,3\}$,

$$
\#\left\{d\asymp D:
\left\|
\frac{X/d+\rho}{4}
\right\|
\le \Delta
\right\}
\ll_\epsilon
(1+\Delta D)X^\epsilon.
$$

Status: `derived_under_assumptions` as part of R5 because the residual source is H4-dependent; the product count itself is elementary.

### Lemma R7-L4: whole-range subcoherence

For every active $D$ and every fourth-moment tuple,

$$
\delta|\lambda|\ll1,
\qquad
\delta=X^{1/2}/D.
$$

Equivalently, the local fat band contains the full natural $N$ range. Status: `proved_internal`.

### Lemma R7-L5: URES weighted representation target

With reduced-fraction weights $A(p/q)$ induced by beta-weighted dyadic lifts, the URES exact-resonance target is

$$
\sum_{r\ne0}R_{\mathrm{res}}(r)^2\ll_\epsilon D^2X^\epsilon.
$$

Status: `open`.

## What should be tested next

1. **H4 source-card physical update.** A1 or the orchestrator should commit `sources/vaaler_1985.md` with exact page/equation anchors.

2. **Beta parity regression.** A3 should check $C_h=0$ for even $h$ and $C_h=2i\chi_4(h)$ for odd $h$ in the raw code.

3. **Complex-weight pairing.** A3 should verify raw two-sided M2 equals complex cosine pairing and deliberately fails the real-weight $\operatorname{Re}B_h$ shortcut when weights are complex.

4. **R5 product-count stress.** Test first and shifted legs for square, near-square, nonsquare, and divisor-rich $X$.

5. **Subcoherence numerical confirmation.** For $D=X^{1/4},X^{3/8},X^{1/2}$, compute

$$
\max_{\text{tuples}}\delta|\lambda|
$$

and confirm no power decay.

6. **URES enumeration first.** A3 should prioritize residual exact $N=0$ enumeration, including the $(6,10,15,5)k$ family and $R(r)^2$ concentration.

7. **NF-2 divisor-sum attempt.** A2/A4 should try to turn

$$
\gcd(Q,q)\ge\sqrt{Qq/(2D)}
$$

into a second-moment divisor bound.

8. **Global moment large-value obstruction.** Quantify what global fourth, sixth, or eighth moment strength would be needed to recover pointwise $X^{1/4+\epsilon}$ using derivative propagation.

9. **Poisson endpoint exact transform.** Derive the stationary-phase formula for the $d$-sum with all boundary terms and dual range

$$
m\asymp hX/D^2.
$$

10. **Signed-vs-unsigned SPD diagnostic.** Compare true beta signs, unsigned coefficients, random signs, and adversarial signs in the endpoint block.

## Proposed state patch, if any

No promotion should be made from this Stage A reasoning alone.

Suggested non-promotional update for the judge to consider, only if a new route-tracking obligation is desired:

proof_obligations:
  create:
    - id: M9-M2-global-moment-large-value-route
      type: lemma
      track: M9_analytic
      title: Global moment plus large-value propagation route for M2
      status: proposed
      statement_tex: "A proposed route in which graded global near-collision estimates for the M2 fourth moment are combined with a large-value propagation theorem strong enough to imply pointwise bounds |S_2(D;X_0)| <<_epsilon X_0^(1/4+epsilon) uniformly over X^(1/4)<=D<=X^(1/2). The known derivative bound alone is insufficient."
      dependencies:
        - M9-M2-fourth-moment-expansion
        - M9-near-collision-estimate
        - M9-M2-fourth-moment-average-to-pointwise
        - M9-endpoint-uniformity
      implies:
        - M9-M2
      blockers:
        - M9-M2-LFM-pointwise-equivalence
      evidence:
        positive: []
        negative: []
        inconclusive:
          - rounds/obligation-main/round_007/responses/A1-007.md
      owner: A1
      next_action: "Determine the exact global moment or large-value theorem needed; test whether fourth, sixth, or eighth moments plus derivative propagation can ever reach the endpoint."

All current theorem-level obligations remain unchanged:

- `M9`: open.
- `M9-M1`: open.
- `M9-M2`: open.
- `M9-near-collision-taxonomy`: open.
- `M9-near-collision-estimate`: proposed.
- `GC-target`: open.
- `H4`: source_audit_required.

## Confidence

Confidence in the source-audit mapping for Vaaler's Theorem 6 and Theorem 18: high, pending physical source-card completion.

Confidence in the $\Phi$ endpoint regularity calculation: high, conditional on the coefficient formula.

Confidence in the M2 beta algebra and parity support: high, conditional on H4 coefficient sign.

Confidence in the R5 positive-Fejer product-count proof strategy: high, conditional on H4 residual majorant.

Confidence in the subcoherence-window obstruction: high.

Confidence that URES is the right next exact-resonance target: moderate to high.

Confidence that URES alone can prove M2: low.

Confidence that a graded near-collision global moment route can reach pointwise endpoint without a new large-value theorem: low.

Confidence that a sign-preserving endpoint route is worth keeping as backup: moderate.

No new Gauss circle exponent is proved in this reasoning round.

--- OUTPUT FROM A3 ---
## Summary

We present a rigorous algebra audit and an executable diagnostic bundle for the M9 analytic track, targeting the computation obligations `M9-fourth-moment-enumeration`, `M9-regression-raw-vs-paired`, `M9-M2-local-fourth-moment-LFM` diagnostics, and `M9-M2-reciprocal-SPD-route`. All formulas are checked for sign consistency, the derivative envelope is derived, and the complex-weight regression is corrected. Since the API cannot materialize files, a complete artifact bundle with repository-relative paths, full Python scripts, exact commands, expected schemas, and a report template is supplied for local execution by the orchestrator or Codex.

## Target proof obligation

Obligations assigned to A3 in Round 7 (all `diagnostic_only`):

- `M9-regression-raw-vs-paired` -- Raw-vs-paired numerical stress test for M9
- `M9-fourth-moment-enumeration` -- Exact and near-collision fourth-moment enumeration for M2
- `M9-M2-local-fourth-moment-LFM` diagnostics -- Everywhere-local fourth-moment estimate for S2 on coherence windows
- `M9-M2-reciprocal-SPD-route` -- Sign-preserving reciprocal discrepancy route for M2

## Main claim or direction

The diagnostic bundle will:

1. Confirm the algebraic correctness of the M2 formulas (raw two-sided, cosine pairing, real-weight pairing) and verify the failure mode when complex weights break the conjugate symmetry.
2. Provide a numerical verification of the derivative envelope `sup|S2'| << H_D`.
3. Test the subcoherence multiplier bound `delta|lambda| <= O(1)` and the local fourth-moment averaging for representative parameters.
4. Enumerate exact `N=0` resonances for a small dyadic block, classify them into denominator-paired, fraction-matching, semi-diagonal, and residual (URES) families, and tabulate absolute beta-weighted masses.
5. Compare the true signed M2 sum with variants where the harmonic-sign pattern is replaced by absolute values or random signs.

All outputs remain `diagnostic_only`. No theorem obligation is promoted.

## Detailed reasoning

### 1. Algebraic normalization and corrected formulas

#### 1.1 Vaaler coefficient and M2 weight

From H4 (source card pending) the finite Vaaler approximation uses coefficients

$$
\alpha_h = -\frac{\Phi(|h|/(H+1))}{2\pi i h}, \qquad h \neq 0,
$$

with \(\alpha_{-h} = \overline{\alpha_h}\) and \(\Phi\) the Vaaler \(\Phi\) function (assumed \(C^1\), \(\Phi(0)=1\), \(\Phi(1)=0\)).
The frequency-side character factor is

$$
C_h = e(h/4) - e(3h/4), \qquad e(x)=e^{2\pi i x}.
$$

For odd \(h\),

$$
C_h = 2i\,\chi_4(h), \qquad \chi_4(h)=
\begin{cases}
+1 & h\equiv 1 \pmod 4,\\
-1 & h\equiv 3 \pmod 4,\\
0 & h\text{ even}.
\end{cases}
$$

Thus the M2 coefficient becomes

$$
\beta_h = \alpha_h C_h = -\frac{\Phi\,\chi_4(h)}{\pi h}.
$$

Because \(\chi_4(-h)=-\chi_4(h)\), the ratio \(\chi_4(h)/h\) is **even**, so \(\beta_{-h} = \beta_h\). Moreover \(\alpha_h\) and \(C_h\) are both purely imaginary, hence \(\beta_h\) is **real**. Consequently the M2 sum

$$
S_2(D;X) = \sum_{1\le |h| \le H_D} \beta_h \sum_{d \sim D} w_D(d)\, e\!\Bigl(\frac{hX}{4d}\Bigr)
$$

is real and can be expressed by the **cosine-pairing** formula

$$
S_2(D;X) = 2\sum_{\substack{h=1\\ h\text{ odd}}}^{H_D} \beta_h \sum_d w_D(d)\,
\cos\!\Bigl(\frac{\pi h X}{2d}\Bigr). \tag{1}
$$

#### 1.2 Correction of the `B_{-1}` relation

In previous scripts an incorrect complex-weight relation `B_{-1} = (1+i)\overline{\Sigma}` appeared.
The correct identity for the true symmetric weights is

$$
B_{-h} = \overline{B_h}, \qquad B_h = \sum_d w_D(d)\,e(hX/(4d)).
$$

This follows from \(e(-hX/(4d)) = \overline{e(hX/(4d))}\) and real \(w_D\). The relation (1) relies on \(\beta_{-h}=\beta_h\) and the conjugate-symmetry of \(B_h\).
For generic complex coefficients that break the symmetry, (1) fails; the bundle implements a deliberate failure test to illustrate this.

#### 1.3 Derivative envelope

Differentiating termwise (justified for smooth \(w_D\); indicator weights give the same order but require boundary care) yields

$$
S_2'(X) = \sum_{h\neq0} \beta_h \sum_d w_D(d)\, \frac{2\pi i h}{4d}\, e(hX/(4d)).
$$

Using \(|\beta_h| \le \Phi(|h|/(H+1))/(\pi|h|) \ll 1/|h|\) and \(|h|/d \le H_D/(D/2)\),

$$
|S_2'(X)| \ll \frac{1}{D} \sum_{h=1}^{H_D} \frac{\Phi(h/(H+1))}{\pi h}\, \pi h \sum_d w_D(d) \ll H_D.
$$

A refined constant is computable but the order \(O(H_D)\) is sufficient; it matches the judge's instruction `sup_I |S_2'| << H_D`.

### 2. Regression test specifications

The bundle computes four variants of the M2 sum:

- **`raw_two_sided`** -- direct double sum over all \(h\neq0\) and all \(d\sim D\).
- **`cosine_pairing`** -- uses (1) with \(\cos\).
- **`real_weight_ReB`** -- \(2\operatorname{Re}\sum_{h>0}\beta_h B_h\); equivalent to `cosine_pairing`.
- **`fake_complex`** -- artificial weight \(\alpha_h=1\) (real), for which \(S_{\text{fake}}\) is not real and the naive real-part formula \(2\operatorname{Re}\sum_{h>0} B_h\) differs from the raw sum.

Assertions (run-time checks) confirm:

1. `abs(S2_raw.imag) < 1e-12` (true weights give real output).
2. `abs(S2_raw.real - S2_cosine) < 1e-10`.
3. For the fake weights, `abs(S2_fake_raw.real - 2*Re(...)) > 0.01` (failure demonstration).

These tests detect any sign error in the phase \(e(hX/(4d))\) (the "\(d=7\) imaginary-part sign" bug) and verify the corrected conjugate-pairing.

### 3. Local fourth-moment diagnostics

Let \(\delta = X^{1/2}/D\). For a tuple \((h_i,d_i)\) the local multiplier is

$$
\lambda = \frac14\Bigl(\frac{h_1}{d_1} - \frac{h_2}{d_2} + \frac{h_3}{d_3} - \frac{h_4}{d_4}\Bigr).
$$

The subcoherence lemma (`M9-M2-subcoherence-window-multiplier`) gives \(|\lambda| \ll H_D/D \asymp X^{-1/4}\), whence

$$
\delta|\lambda| \ll \frac{X^{1/4}}{D} \le 1 \quad (\text{for } D \ge X^{1/4}).
$$

The script:

- Samples thousands of random tuples, computes \(\delta|\lambda|\) exactly using Python's `Fraction`, and reports the maximum.
- Evaluates \(S_2\) on a fine grid over an interval \(I\) of length \(\delta\), computes \(\delta^{-1}\int_I |S_2|^4\) by averaging, and compares with \(\sup_I |S_2|^4\). At the endpoint \(D \asymp X^{1/2}\) the average-to-max ratio should be close to 1, reflecting the LFM obstruction.

### 4. Exact fourth-moment enumeration

#### 4.1 Algorithm

For small parameters (e.g. \(D \le 30\), \(H \le 15\)) the script exhausts all quadruples

$$
d_i \in (D/2, D], \qquad h_i \in [-H,H]\setminus\{0\},\; h_i\text{ odd},
$$

filtering those with

$$
N = h_1 d_2 d_3 d_4 - h_2 d_1 d_3 d_4 + h_3 d_1 d_2 d_4 - h_4 d_1 d_2 d_3 = 0.
$$

For each zero tuple it records:

- the multiset of original \(d_i\);
- the reduced fraction \(h_i/d_i\);
- the signed and absolute weight product \(\prod \beta_{h_i} w_D(d_i)\);
- a classification tag:
  - **FM** -- fraction-matching,
  - **DP** -- original denominators paired,
  - **SD** -- semi-diagonal placeholder,
  - **URES** -- unpaired residual.

#### 4.2 Residual example

The identity

$$
\frac{1}{6k} + \frac{1}{10k} = \frac{1}{15k} + \frac{1}{5k}
$$

gives an exact resonance that is **not** denominator-paired when the four denominators are distinct (e.g. \(k=2\) yields 12,20,30,10). The script will classify such a tuple as URES and measure its contribution to the total exact-\(N=0\) mass.

### 5. SPD sign diagnostics

The SPD (sign-preserving discrepancy) route hypothesises that the true signs \(\chi_4(h)\) provide essential cancellation. The script computes \(S_2\) for four sign patterns:

- **true** -- the actual \(\beta_h\).
- **unsigned** -- \(\beta_h\) replaced by \(|\beta_h|\).
- **random** -- \(|\beta_h|\) with independent \(\pm1\) signs.
- **adversarial** -- all signs identical (e.g. \(+\!|\beta_h|\)).

Comparing \(|S_2^{\text{true}}|\) with the other variants on a few sample points \(X\) measures the importance of the character sign; a large ratio would support the SPD route.

## Theorem-dependency audit

All diagnostics depend on the **assumed** Vaaler coefficient formula from H4, which is still `source_audit_required`. Dependencies:

- `H4` (Vaaler approximation) -- not validated; used via surrogate \(\Phi\).
- `M9-M2-beta-algebra` -- derived under H4; provides \(\beta_h\).
- `M9-M2-fourth-moment-expansion` -- gives the algebraic structure for the fourth moment and the integer \(N\).
- `M9-M2-subcoherence-window-multiplier` -- tested numerically.
- `M9-M2-average-to-pointwise-AP-lemma` -- elementary calculus; the derivative bound in Section 1.3 is proved without H4 beyond the magnitude of \(\beta_h\).

**Missing theorem statement** (needed for full certification): exact continuity, differentiability, and Fejer-residual inequality for Vaaler's \(\Phi\) (Theorem 18 of Vaaler 1985). Until the source card is completed, the script uses a **surrogate** \(\Phi(u)=1-u\); results dependent on the true \(\Phi\) must be re-checked after audit.

## Hidden assumptions and potential gaps

- **Floating-point precision**: For large \(X\) (beyond \(10^{12}\)) the double-precision phases may accumulate errors; a `mpmath` high-precision fallback is not provided.
- **Weight smoothness**: The derivative bound uses term-wise differentiation; the script's default indicator weight violates smoothness at the boundary. For a strict check a smooth compactly supported weight should be used, but the order estimate remains valid.
- **Enumeration scope**: The exhaustive search is only feasible for tiny \(D,H\); larger ranges require a collision-based method. The small-scale results cannot prove global URES bounds but can reveal unexpected large mass.
- **Local-window integration**: The average of \(|S_2|^4\) is approximated by a finite sum; if \(S_2\) oscillates faster than the grid, the integral may be inaccurate. A convergence test (increasing grid size) is included in the script comments.

## Counterexample or obstruction search

The script actively searches for:

- **Large URES mass**: If the absolute URES weight for the tested block exceeds, say, \(D^{2+\epsilon}\), it would indicate a serious potential obstruction.
- **Violation of the subcoherence multiplier bound**: if \(\delta|\lambda| > 10\) for any sampled tuple, the lemma is numerically falsified (or the derivation has a mistake).
- **Near-collision bands**: by listing tuples with small non-zero \(|N|\), one can see the size of the bands that must be controlled in any global moment estimate.

## Verification

The bundle can be verified locally by:

1. **Compilation**: `python -m py_compile run.py` must succeed.
2. **Determinism**: the script uses a fixed random seed; running with the same arguments must produce identical tables.
3. **Pass/fail assertions**: the three regression assertions are embedded; exit code 0 only if all pass.
4. **Precision log**: Python version, command line, timestamps are recorded in `results/precision.log`.

If any assertion fails, the algebraic normalisation is **incorrect** and must be fixed in the state.

## Divergent alternatives and 20% exploration

Beyond the judge's assigned tasks, we briefly explore a **Mellin--Perron alternative**.

Define

$$
D(s)=\sum_d w_D(d)\, d^{-s},\qquad
F(s)=\sum_h \beta_h\, h^{-s}.
$$

Then formally

$$
S_2(D;X) = \frac{1}{2\pi i} \int_{c-i\infty}^{c+i\infty} D(s)\, F(-s)\, (X/4)^s\, \frac{ds}{s},
$$

provided the integral converges absolutely on some vertical line.
The critical step is to control \(F(s)\), which is essentially a linear combination of Dirichlet \(L\)-functions twisted by \(\chi_4\) and the \(\Phi\) factor. A quick falsification test: compute \(F(s)\) for real \(s\) in a small interval and check whether it has a pole that prevents closing the contour. This route is not developed further but could be assigned to A4 or A1 in a later round.

## Useful lemmas

**Lemma DC (Derivative control).** Under the active range and assuming \(|\beta_h| \le C/|h|\),

$$
\sup_{X \in [X_0, X_0+\delta]} |S_2'(X)| \le C' H_D,
$$

with \(C'\) depending only on the weight \(w_D\). The proof follows by absolute values and the trivial estimate \(|e(hX/(4d))|=1\).

**Lemma CS (Conjugate-symmetry pairing).** For real \(\beta_h\) with \(\beta_{-h}=\beta_h\) and any sequence \(B_h\) satisfying \(B_{-h}=\overline{B_h}\),

$$
\sum_{h\neq0} \beta_h B_h = 2\operatorname{Re}\!\Bigl(\sum_{h>0} \beta_h B_h\Bigr).
$$

If the symmetry is violated, the equality fails; the script provides a numerical demonstration.

## What should be tested next

1. Materialise the bundle and execute the commands on a Python >= 3.9 environment.
2. Examine the regression output: all three assertions must pass.
3. Check the subcoherence `max delta|lambda|` and the local-average ratio; record them for the proof draft.
4. Run the small-block enumeration (e.g. `--D 20 --H 5`) and inspect the URES mass relative to \(D^2\).
5. Compare the SPD sign ratios; if the true sum is significantly smaller than the unsigned or adversarial variants, it supports the sign-preserving approach.
6. After H4 source-card validation, re-run with the exact \(\Phi\) and replace the surrogate.

## Proposed state patch, if any

Because no computation has been executed yet, **no positive evidence is added**. Once the bundle is executed and the results are committed to the repo, the judge may apply:

- Update `M9-regression-raw-vs-paired` next_action to "Regression bundle materialised; verify pass/fail status."
- Add a new obligation `M9-M2-regression-verified` (status `diagnostic_only`) recording the outcome.
- Add **`M9-M2-derivative-envelope`** (status `derived_under_assumptions`, depends on H4) with the bound `sup|S2'| << H_D`.
- If enumeration reveals a significant URES mass, add an obstruction note to `M9-M2-unpaired-residual-URES`.

No theorem obligation is promoted.

## Confidence

- Algebraic derivations: 0.95
- Script syntactic correctness: 0.90
- Numerical accuracy for moderate \(X\): 0.85
- Completeness of artifact bundle: 0.92
- Utility for future proof graph decisions: moderate (diagnostic only).

## Artifact bundle

All paths are relative to the repository root.

### 1. Script path

```
rounds/obligation-main/round_007/artifacts/m9_diagnostics/run.py
```

### 2. Complete script contents

```python
#!/usr/bin/env python3
"""
M9 diagnostics bundle for Round 7.
Performs formula regression, local fourth-moment checks, exact N=0 enumeration,
and SPD sign comparison.
"""
import math, cmath, fractions, itertools, random, csv, os, argparse, sys, time
from collections import defaultdict

# ---------- Vaaler surrogate ----------
def Vaaler_Phi(u):
    """Surrogate Phi(u) = 1-u for testing; replace with exact after H4 audit."""
    if u <= 0.0: return 1.0
    if u >= 1.0: return 0.0
    # Exact formula would be pi*u*(1-u)/tan(pi*u)+u; using 1-u for simplicity
    # To switch to exact, uncomment next line:
    # return math.pi * u * (1-u) / math.tan(math.pi * u) + u
    return 1.0 - u

def chi4(n):
    n = n % 4
    if n == 0: return 0
    if n == 1: return 1
    return -1

def beta_h_mag(h, H):
    """Real beta coefficient for h odd; zero for even."""
    if h % 2 == 0:
        return 0.0
    phi = Vaaler_Phi(abs(h) / (H + 1))
    return -phi * chi4(abs(h)) / (math.pi * abs(h))

# ---------- M2 sums ----------
def e(x):
    return cmath.exp(2j * math.pi * x)

def weight_d(d, D):
    """Simple indicator weight."""
    if D/2 < d <= D:
        return 1.0
    return 0.0

def S2_raw(X, D, H):
    total = 0j
    for d in range(D//2 + 1, D + 1):
        w = weight_d(d, D)
        if w == 0: continue
        for h in range(-H, H+1):
            if h == 0: continue
            beta = beta_h_mag(h, H)
            if beta == 0: continue
            total += beta * w * e(h * X / (4 * d))
    return total

def S2_cosine(X, D, H):
    total = 0.0
    for d in range(D//2 + 1, D + 1):
        w = weight_d(d, D)
        if w == 0: continue
        for h in range(1, H+1, 2):
            beta = beta_h_mag(h, H)
            if beta == 0: continue
            total += 2 * beta * w * math.cos(math.pi * h * X / (2 * d))
    return total

def S2_fake_raw(X, D, H):
    total = 0j
    for d in range(D//2 + 1, D + 1):
        w = weight_d(d, D)
        if w == 0: continue
        for h in range(-H, H+1):
            if h == 0: continue
            total += 1.0 * w * e(h * X / (4 * d))
    return total

def S2_fake_cosine(X, D, H):
    total = 0j
    for d in range(D//2 + 1, D + 1):
        w = weight_d(d, D)
        if w == 0: continue
        for h in range(1, H+1):
            total += 1.0 * w * e(h * X / (4 * d))
    return 2 * total.real

# ---------- Derivative bound ----------
def S2_prime_bound(H, D, X0, delta, npoints=100):
    max_val = 0.0
    step = delta / npoints
    for i in range(npoints):
        X1 = X0 + i * step
        X2 = X1 + step
        val = abs(S2_raw(X2, D, H) - S2_raw(X1, D, H)) / step
        if val > max_val:
            max_val = val
    return max_val

# ---------- LFM diagnostics ----------
def sample_tuple(D, H):
    hs = [random.choice([h for h in range(-H, H+1) if h%2==1 and h!=0]) for _ in range(4)]
    ds = [random.randint(D//2+1, D) for _ in range(4)]
    return hs + ds

def compute_lambda(h1,d1,h2,d2,h3,d3,h4,d4):
    return 0.25 * (h1/d1 - h2/d2 + h3/d3 - h4/d4)

def check_subcoherence(D, H, X, num_samples=1000):
    delta = math.sqrt(X) / D
    max_val = 0.0
    for _ in range(num_samples):
        tup = sample_tuple(D, H)
        lam = compute_lambda(*tup)
        val = delta * abs(lam)
        if val > max_val:
            max_val = val
    return max_val, delta

# ---------- Exact enumeration ----------
def reduced_fraction(h, d):
    g = math.gcd(abs(h), d)
    return fractions.Fraction(h//g, d//g)

def classify_tuple(hs, ds):
    d1,d2,d3,d4 = ds
    # fraction-matching
    if ((hs[0]*d2 == hs[1]*d1 and hs[2]*d4 == hs[3]*d3) or
        (hs[0]*d4 == hs[3]*d1 and hs[1]*d3 == hs[2]*d2)):
        return 'FM'
    # denominator-paired (original d)
    if (d1 == d2 and d3 == d4) or (d1 == d3 and d2 == d4) or (d1 == d4 and d2 == d3):
        return 'DP'
    red_den = [reduced_fraction(hs[i], ds[i]).denominator for i in range(4)]
    den_set = sorted(red_den)
    if len(set(den_set)) == 2 and den_set[0]==den_set[1] and den_set[2]==den_set[3]:
        return 'SD'
    return 'URES'

def enumerate_N0(D, H, X_placeholder=1e6):
    d_range = list(range(D//2+1, D+1))
    h_vals = [h for h in range(-H, H+1) if h%2==1 and h!=0]
    total_mass = defaultdict(float)
    count = defaultdict(int)
    for d1,d2,d3,d4 in itertools.product(d_range, repeat=4):
        w = weight_d(d1,D)*weight_d(d2,D)*weight_d(d3,D)*weight_d(d4,D)
        if w == 0: continue
        for h1,h2,h3,h4 in itertools.product(h_vals, repeat=4):
            N_val = (h1 * d2 * d3 * d4 - h2 * d1 * d3 * d4 +
                     h3 * d1 * d2 * d4 - h4 * d1 * d2 * d3)
            if N_val != 0:
                continue
            beta = beta_h_mag(h1,H) * beta_h_mag(h2,H) * beta_h_mag(h3,H) * beta_h_mag(h4,H)
            mass_abs = abs(beta) * w
            cat = classify_tuple([h1,h2,h3,h4], [d1,d2,d3,d4])
            total_mass[cat] += mass_abs
            count[cat] += 1
    return total_mass, count

# ---------- SPD sign comparison ----------
def S2_signed(X, D, H, sign_pattern):
    total = 0j
    for d in range(D//2+1, D+1):
        w = weight_d(d, D)
        if w == 0: continue
        for h in range(-H, H+1):
            if h == 0: continue
            base_mag = abs(beta_h_mag(h, H))
            if sign_pattern == 'true':
                val = beta_h_mag(h, H)
            elif sign_pattern == 'unsigned':
                val = base_mag
            elif sign_pattern == 'random':
                val = base_mag * random.choice([1, -1])
            else:  # adversarial
                val = base_mag
            total += val * w * e(h * X / (4 * d))
    return abs(total)

# ---------- Main ----------
def main():
    parser = argparse.ArgumentParser(description='M9 diagnostics')
    parser.add_argument('--X', type=float, default=1e6, help='central X value')
    parser.add_argument('--D', type=int, default=100, help='dyadic parameter')
    parser.add_argument('--H', type=int, default=10, help='truncation height H')
    parser.add_argument('--outdir', type=str, default='results')
    args = parser.parse_args()
    X = args.X
    D = args.D
    H = args.H
    os.makedirs(args.outdir, exist_ok=True)
    precision_log = os.path.join(args.outdir, 'precision.log')
    with open(precision_log, 'w') as log:
        log.write(f"Python version: {sys.version}\n")
        log.write(f"Arguments: X={X}, D={D}, H={H}\n")
        log.write(f"Start time: {time.ctime()}\n")

print("=== Formula regression ===")
    s_raw = S2_raw(X, D, H)
    s_cos = S2_cosine(X, D, H)
    print(f"Raw two-sided: {s_raw.real:.6e} + {s_raw.imag:.6e}i")
    print(f"Cosine pairing: {s_cos:.6e}")
    passed_real = abs(s_raw.imag) < 1e-12
    print(f"Imaginary < 1e-12Section  {passed_real}")
    passed_equal = abs(s_raw.real - s_cos) < 1e-10
    print(f"Real matches cosineSection  {passed_equal}")

s_fake_raw = S2_fake_raw(X, D, H)
    s_fake_cos = S2_fake_cosine(X, D, H)
    diff_fake = abs(s_fake_raw.real - s_fake_cos)
    passed_fake = diff_fake > 0.01
    print(f"Fake weight test: diff={diff_fake:.4e}, failsSection  {passed_fake}")

print("\n=== Derivative envelope ===")
    delta = math.sqrt(X) / D
    sup_deriv = S2_prime_bound(H, D, X, delta)
    print(f"Estimated sup|S2'| = {sup_deriv:.4e}, expected O(H)={H}")

print("\n=== Subcoherence multiplier ===")
    random.seed(42)
    max_dlam, delta_val = check_subcoherence(D, H, X, num_samples=5000)
    print(f"delta = {delta_val:.4f}, max delta*|lambda| = {max_dlam:.4f} (target <= 1)")

print("\n=== Local fourth-moment average ===")
    n_grid = 200
    grid_x = [X + j*delta/(n_grid-1) for j in range(n_grid)]
    vals = [abs(S2_raw(x, D, H)) for x in grid_x]
    avg4 = sum(v**4 for v in vals) / len(vals)
    max4 = max(v**4 for v in vals)
    print(f"Average |S2|^4 = {avg4:.6e}, max = {max4:.6e}, ratio = {max4/avg4:.4f}")

print("\n=== SPD sign comparison ===")
    random.seed(42)
    for pat in ['true', 'unsigned', 'random', 'adversarial']:
        val = S2_signed(X, D, H, pat)
        print(f"|S2| ({pat:12s}): {val:.6e}")

if D <= 30 and H <= 15:
        print("\n=== Exact N=0 enumeration ===")
        t0 = time.time()
        mass_abs, cnt = enumerate_N0(D, H, X)
        dt = time.time() - t0
        print(f"Enumeration time: {dt:.1f} s")
        table_path = os.path.join(args.outdir, 'enum_table.csv')
        with open(table_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Count', 'AbsMass'])
            for cat in sorted(mass_abs.keys()):
                writer.writerow([cat, cnt[cat], mass_abs[cat]])
                print(f"{cat:5s}: count={cnt[cat]:6d}, abs_mass={mass_abs[cat]:.6e}")
        print(f"Table written to {table_path}")
    else:
        print("\nEnumeration skipped (D > 30 or H > 15).")

with open(precision_log, 'a') as log:
        log.write(f"End time: {time.ctime()}\n")
    print(f"\nLog written to {precision_log}")

if __name__ == '__main__':
    main()
```

### 3. Exact commands

```bash
cd /path/to/repo
python -m py_compile rounds/obligation-main/round_007/artifacts/m9_diagnostics/run.py
python rounds/obligation-main/round_007/artifacts/m9_diagnostics/run.py \
  --X 1000000 --D 100 --H 10 \
  --outdir rounds/obligation-main/round_007/artifacts/m9_diagnostics/results

# Small-block enumeration
python rounds/obligation-main/round_007/artifacts/m9_diagnostics/run.py \
  --X 1000000 --D 20 --H 5 \
  --outdir rounds/obligation-main/round_007/artifacts/m9_diagnostics/results_smallD
```

### 4. Expected table schemas

**Regression console output** -- six pass/fail assertions, derivative estimate, subcoherence maximum, local-average ratio, SPD values.

**`results/enum_table.csv`**

| Category | Count | AbsMass |
|---|---:|---:|
| DP | ... | ... |
| FM | ... | ... |
| SD | ... | ... |
| URES | ... | ... |

**`results/precision.log`** -- Python version, command line arguments, start and end timestamps.

### 5. Report template

After execution, the orchestrator should produce a `report.md` containing:

- Summary of regression pass/fail.
- Observed `max delta|lambda|`.
- Ratio of average to max `|S_2|^4`.
- SPD comparison table.
- For enumeration run, a table of masses with commentary on URES magnitude relative to `D^2`.
- Any anomalies or unexpected failures.

All outputs remain `diagnostic_only`.

--- OUTPUT FROM A4 ---
## Summary

This Stage A response executes the five judge-assigned objectives for A4 in Round 7. (1) It writes validator-ready statements and proofs of the denominator-paired suite DP-0 (parity), DP-1 (thin-band emptiness), DP-2 (thin DP mass), DP-3 (full DP mass), organized as unconditional class-level lemmas plus one application corollary carrying the entire H4 dependency; DP-2 is sharpened to $\ll C_0 D\log^2(2H_D)$, matching the diagnostic threshold assigned to A3. (2) It transcribes NF-1 and NF-2 into lemma-bank form with complete proofs, all definitions, degenerate-case checks, and a verified worked example, and adds a small participation-window lemma NF-0 ($q_i \ge D/H_D$, $|p_i|\le 2H_D q_i/D$, and odd $p_i$, odd $t_i$ under the H4 parity support). (3) It gives a complete coverage-and-overlap lemma OB-1 for exact $N=0$ tuples with reduced-denominator multiset $\{q,q,q',q'\}$: the FM, AP (sign-symmetric), U-2 (cross-unpaired), and SS (same-side-unpaired) classes cover this set with covering multiplicity at most 3, so absolute-mass union bounds are safe; it also records that multiplicity pattern $(3,1)$ multisets fall in URES and exhibits a concrete such resonance. (4) On URES it proves an exact energy-transfer identity, reduces the full target $\sum_{r\ne0}R(r)^2 \ll_\epsilon D^2X^\epsilon$ to a pointwise representation bound URES-P ($R(r)\ll_\epsilon X^\epsilon$ for all $r \ne 0$), proves URES-P for the subfamily of representations with $q_1 \mid Q$ or $q_3 \mid Q$ via NF-2 and a per-cell weighted bound, and isolates the exact remaining obligation as a primitive-point count for congruence lattices in the participation triangle. (5) It states the exact SPD theorem SPD-1 at reciprocal points $\theta_d = X/(4d)$ as a smoothed square-wave cancellation statement, identifies its jump set with divisor conditions $X \equiv \pm d \pmod{4d}$, and supplies A3 a numeric falsification threshold. The exploratory allocation formulates a global-moment/large-value propagation ladder: a square-root-strength $2k$-th moment bound would yield the M2 target for $D \le X^{1/2 - 1/(k+1)}$, quantifying precisely why the endpoint is a sup-norm problem. No promotion of `M9`, `M9-M2`, or `GC-target` is proposed.

## Target proof obligation

Primary: `M9-M2-DP-near-collision-bound`, `M9-M2-coprime-rigidity-normal-form`, `M9-M2-NF-participation-rigidity`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-unpaired-residual-URES`. Backup: `M9-M2-reciprocal-SPD-route`. Exploratory: a proposed map feeding `M9-M2-fourth-moment-average-to-pointwise` and `M9-near-collision-estimate` for sub-endpoint ranges.

## Main claim or direction

Main claims of this round, with statuses: the DP suite DP-0 through DP-3 is proved at class level (proved_internal) with a single H4-carrying application corollary (derived_under_assumptions); NF-1, NF-2, NF-0, and the overlap-coverage lemma OB-1 are proved_internal; the URES target is rigorously reduced, via a proved energy identity and Cauchy--Schwarz, to the pointwise bound URES-P, which is proved for the divisor-compatible subfamily and remains open in general, with the residual difficulty identified exactly. Direction: URES-P is the single sharpest open sublemma on the exact-resonance side; SPD-1 is the stated backup with a falsification test.

## Detailed reasoning

Conventions. Throughout, $X$ is large, $X^{1/4}\le D\le X^{1/2}$, $H=H_D\asymp DX^{-1/4}$, and $d$ ranges over one dyadic block $[D,2D)$ with bounded weights $|w_D(d)|\le W$. The two-sided M2 object is $S_2(D;t)=\sum_{1\le|h|\le H}\beta_h\sum_{d\in[D,2D)}w_D(d)\,e(ht/(4d))$. The coefficient class is: (K-mag) $|\beta_h|\le K/|h|$; (K-par) $\beta_h=0$ for even $h$. Under H4 (`M9-M2-beta-algebra`) the actual coefficients $\beta_h=-\Phi(|h|/(H+1))\chi_4(|h|)\mathbf 1_{2\nmid h}/(\pi|h|)$ satisfy both with $K$ absolute, but (K-mag) needs $\sup|\Phi|\ll1$ (H4-Phi-regularity, source-audit-dependent), while (K-par) needs only the elementary identity $C_h=e(h/4)-e(3h/4)=2i\chi_4(h)\mathbf 1_{2\nmid h}$, which is internal once the M2 object is written in H4 form. The fourth-moment tuple has cleared numerator $N=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3$ and $Q_\times=d_1d_2d_3d_4$. Absolute mass of a tuple family means the sum of $|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|$ times $|w|^4\le W^4$ over the family.

Part I. The DP suite. The DP class is $d_1=d_2=a$, $d_3=d_4=b$, $a,b\in[D,2D)$. Direct computation gives $N=ab\,L$ with $L=(h_1-h_2)b+(h_3-h_4)a$.

DP-0 (parity; class-level, proved_internal). Assume (K-par). Then all $h_i$ are odd, so $u:=h_1-h_2$ and $v:=h_3-h_4$ are even, hence $L=ub+va$ is even; in particular $L\ne0$ implies $|L|\ge2$. Proof: immediate. No magnitude hypothesis is used.

DP-1 (thin-band emptiness; class-level, proved_internal). Assume (K-par). Fix $C_0>0$. If $C_0D^2<2X$, then no DP tuple satisfies $0<|N|\le C_0D^4/X$. Proof: $0<|N|=ab|L|$ forces $L\ne0$, so $|N|\ge2ab\ge2D^2$ by DP-0 and $a,b\ge D$; but $C_0D^4/X\le C_0D^2\cdot D^2/X<2D^2$ under the stated inequality. Equivalently, the thin DP band is empty unless $D\ge\sqrt{2X/C_0}$; since $D\le X^{1/2}$, this can occur only for $C_0\ge2$ and only in the top dyadic blocks. Endpoint check: at $D=X^{1/2}$ and $C_0>2$ the band can be nonempty, which is exactly the regime DP-2 addresses. Dyadic-convention sensitivity: with the block $(D/2,2D]$ instead of $[D,2D)$, constants shift by factors of 4; the statement should carry the block convention explicitly.

DP-2 (thin DP mass; class-level, proved_internal). Assume (K-par) and (K-mag). Then for every $C_0>0$,
$$
\Sigma_{DP}\big(0<|N|\le C_0D^4/X\big)\ \le\ C\,W^4K^4\,C_0\,D\,\log^2(2H),
$$
with $C$ absolute. Proof. Write the mass as a sum over $u,v$ even and $a,b$: the $h$-sums at fixed $(u,v)$ are bounded by $L_H(u)L_H(v)$, where $L_H$ is the harmonic-convolution function; by `M9-M2-harmonic-convolution-LH` (proved_internal), $L_H(u)\ll\log(2H)/\max(1,|u|)$. If $u=0$, $v\ne0$ (or symmetrically), then $|L|=|v|a\ge2D>C_0\ge L^*(a,b):=C_0D^4/(Xab)$ for large $X$, so such tuples are outside the thin band; likewise $u=v=0$ gives $N=0$. So both $u,v$ are nonzero and even, $2\le|u|,|v|\le2H$. Fix such $(u,v)$ and set $w=\gcd(u,v)$, which is even. Any attained $L=ub+va$ is a multiple of $w$; the number of nonzero multiples of $w$ with $|L|\le L^*\le C_0$ is at most $2C_0/w$ (zero if $w>C_0$). For each such $L$, the solutions of $ub+va=L$ form the line $(a,b)=(a_0+t\,u/w,\;b_0-t\,v/w)$, and the box constraint $a,b\in[D,2D)$ allows at most $1+Dw/\max(|u|,|v|)$ integers $t$. Hence the pair count for fixed $(u,v)$ is at most $\frac{2C_0}{w}\big(1+\frac{Dw}{\max(|u|,|v|)}\big)\le\frac{2C_0}{w}+\frac{2C_0D}{\max(|u|,|v|)}$.
Summing over $(u,v)$: split the count as $P(u,v)\le \frac{2C_0}{w}+\frac{2C_0D}{\max(|u|,|v|)}$, valid when $w=\gcd(u,v)\le C_0$, while $P(u,v)=0$ when $w>C_0$ because no nonzero multiple of $w$ lies in $[-C_0,C_0]$. Using $L_H(u)\ll \log(2H)/|u|$ from `M9-M2-harmonic-convolution-LH` and $w\ge2$ (both $u,v$ even):

Term A:
$$
\sum_{\substack{u,v\ne0\ \mathrm{even}\\ |u|,|v|\le 2H}}\frac{\log^2(2H)}{|u||v|}\cdot\frac{2C_0}{w}
\ \le\ C_0\log^2(2H)\Big(\sum_{2\le|u|\le2H}\frac{1}{|u|}\Big)^{2}\ \ll\ C_0\log^4(2H).
$$

Term B: by the $u\leftrightarrow v$ symmetry assume $|u|=\max(|u|,|v|)$; then
$$
\sum_{u,v}\frac{\log^2(2H)}{|u||v|}\cdot\frac{2C_0D}{\max(|u|,|v|)}
\ \ll\ C_0D\log^2(2H)\sum_{u\ne0}\frac{1}{u^2}\sum_{1\le|v|\le|u|}\frac{1}{|v|}
\ \ll\ C_0D\log^2(2H)\sum_{u\ne0}\frac{\log(2|u|)}{u^2}\ \ll\ C_0D\log^2(2H).
$$

Since $D\ge X^{1/4}$ and $H\le 2X^{1/4}$ give $\log^2(2H)\le D$ for $X\ge X_0$ absolute, Term A is absorbed into the Term B scale, and

$$
\Sigma_{DP}\big(0<|N|\le C_0D^4/X\big)\ \le\ C\,W^4K^4\,C_0\,D\,\log^2(2H),
$$

which is the DP-2 statement. Edge cases: (i) if $C_0<2$ the band is empty by DP-0/DP-1 and the bound is vacuous-true; (ii) tuples with $u=0$ or $v=0$ were shown to lie outside the thin band for $X\ge X_0$, and $u=v=0$ gives $N=0$, excluded; (iii) two-sided $h$-ranges are built into $L_H$; (iv) the constant $C$ depends on the dyadic block convention $[D,2D)$ and must be re-derived if the block convention changes. This matches the diagnostic threshold $C_0D\log^2(2H)$ assigned to A3. Status: proved_internal at class level under (K-par), (K-mag).

**DP-3 (full DP total mass; class-level, proved_internal).** Assume (K-mag). The full DP class (no band restriction, all four $h_i$ free, $d_1=d_2=a$, $d_3=d_4=b$) has absolute mass
$$
\Sigma_{DP}^{\mathrm{all}}\ \le\ W^4\,\#\{a\}\,\#\{b\}\,\Big(\sum_{1\le|h|\le H}\frac{K}{|h|}\Big)^{4}\ \le\ C\,W^4K^4\,D^2\log^4(2H)\ \ll_\epsilon\ D^2X^{\epsilon}\ \le\ X^{1+\epsilon},
$$
by pure factorization, since $\#\{a\in[D,2D)\cap\mathbb Z\}=D$. So the entire DP class is harmless at the $D^2X^\epsilon$ scale, hence at the $X^{1+\epsilon}$ scale, uniformly for $X^{1/4}\le D\le X^{1/2}$.

**DP-A (application corollary; the entire H4 dependency; derived_under_assumptions, blocked by `H4-source-audit`).** Under the H4 coefficient convention of `M9-M2-beta-algebra` and the regularity bound $\sup_{[0,1]}|\Phi|\le\Phi_0<\infty$ of `H4-Phi-regularity`, the actual M2 coefficients $\beta_h=-\Phi(|h|/(H+1))\chi_4(|h|)\mathbf 1_{2\nmid h}/(\pi|h|)$ satisfy (K-par) exactly and (K-mag) with $K=\Phi_0/\pi$. Hence DP-0 through DP-3 hold verbatim for the actual M2 fourth moment. This is the exact dependency split requested: DP-0/DP-1/DP-2/DP-3 are proved_internal statements about any coefficient class satisfying (K-par)/(K-mag); DP-A alone carries H4, and it is blocked by `H4-source-audit`. Note (K-par) for the actual coefficients uses only the internal identity $C_h=e(h/4)-e(3h/4)=2i\chi_4(h)\mathbf 1_{2\nmid h}$ once M2 is written in its project-defined H4 form; (K-mag) genuinely needs the unaudited $\Phi$ bound.

Part II. NF lemmas in lemma-bank form.

**NF-0 (participation window; proved_internal).** Let $(h,d)$ satisfy $1\le|h|\le H$, $d\in[D,2D)$, and write $h/d=p/q$ in lowest terms with lift $g=\gcd(h,d)\ge1$, so $h=gp$, $d=gq$. Then
$$
\frac{D}{H}\ \le\ q\ \le\ d\ <\ 2D,\qquad 1\le|p|\ \le\ \frac{H}{D}\,q\ \le\ H,\qquad g\in\Big[\frac{D}{q},\frac{2D}{q}\Big).
$$
Under (K-par), $h$ is odd, hence $g$ and $p$ are odd and $v_2(q)=v_2(d)$. Proof: $q=d/g\ge d/|h|\ge D/H$; $|p|/q=|h|/d\le H/D$; $p\mid h$ gives $|p|\le H$; parity is immediate from $g\mid h$. Moreover the lift-weight sum obeys, for any coefficients with (K-mag),
$$
\sum_{g\in[D/q,\,2D/q)}|\beta_{gp}|\ \le\ \frac{K}{|p|}\sum_{g\in[D/q,\,2D/q)}\frac1g\ \le\ \frac{cK}{|p|},
$$
with $c$ absolute, since a dyadic block of integers $[m,2m)$ contributes $\sum_{g=m}^{2m-1}1/g\le1$.

**NF-1 (two-fraction denominator rigidity; proved_internal).** Let $x_1=p_1/q_1$ and $x_3=p_3/q_3$ be reduced and nonzero with $x_1+x_3\ne0$. Put $e=\gcd(q_1,q_3)$,
$s_1=q_1/e$, $s_3=q_3/e$, so $\gcd(s_1,s_3)=1$, and set $T=p_1s_3+p_3s_1$, so that $x_1+x_3=T/(es_1s_3)$ with $T\ne0$. Then $\gcd(T,s_1s_3)=1$, the reduced denominator $q$ of $x_1+x_3$ is
$$
q\;=\;\frac{e\,s_1s_3}{\gcd(T,e)}\;=\;\frac{\mathrm{lcm}(q_1,q_3)}{\gcd(T,e)},
$$
and consequently
$$
s_1s_3\ \Big|\ q,\qquad q\ \Big|\ \mathrm{lcm}(q_1,q_3),\qquad q\ \ge\ \frac{q_1q_3}{e^2},
$$
with equality $q=q_1q_3/e^2$ if and only if $e\mid T$. Proof: reducing $T$ modulo $s_1$ gives $T\equiv p_1s_3$, and $\gcd(p_1,s_1)\mid\gcd(p_1,q_1)=1$, $\gcd(s_3,s_1)=1$, so $\gcd(T,s_1)=1$; symmetrically $\gcd(T,s_3)=1$; hence $\gcd(T,s_1s_3)=1$ and the only cancellation available in $T/(es_1s_3)$ is by $\gcd(T,e)$, which divides $e$. Degenerate case: if $x_1+x_3=0$ then $T=0$ and NF-1 is vacated; NF-1 is stated only for nonzero sums (the zero-sum configuration is exactly the anti-paired class AP below). Status: proved_internal, no coefficient hypotheses.

**NF-2 (participation rigidity; lemma-bank transcription of `M9-M2-NF-participation-rigidity`; proved_internal).** Let $r=\mu/Q$ be reduced with $\mu\ne0$, $Q\ge1$, and let $x_1=p_1/q_1$ be reduced with $x_3:=r-x_1\ne0$ of reduced form $p_3/q_3$. Define
$$
g=\gcd(Q,q_1),\qquad \widehat Q=Q/g,\qquad \widehat q_1=q_1/g,\qquad M=\mu\widehat q_1-p_1\widehat Q.
$$
Then: (a) $\gcd(\widehat Q,\widehat q_1)=1$; (b) $M\ne0$ and $\gcd(\widehat Q\widehat q_1,\,M)=1$; (c)
$$
x_3=\frac{M}{g\,\widehat Q\,\widehat q_1},\qquad
p_3=\frac{M}{\gcd(g,M)},\qquad
q_3=\frac{g\,\widehat Q\,\widehat q_1}{\gcd(g,M)}\ \ge\ \widehat Q\,\widehat q_1=\frac{Qq_1}{g^2},
$$
with equality in the last inequality if and only if $g\mid M$; (d) consequently, if $q_3\le 2D$ then
$$
\gcd(Q,q_1)\ \ge\ \sqrt{\frac{Qq_1}{2D}},\qquad
\gcd(g,M)\ \ge\ \frac{Qq_1}{2Dg}.
$$
Proof. (a) If a prime $\ell$ divided both $\widehat Q$ and $\widehat q_1$, then $\ell g$ would divide both $Q$ and $q_1$, contradicting $g=\gcd(Q,q_1)$. (b) $x_3=\mu/Q-p_1/q_1=(\mu q_1-p_1Q)/(Qq_1)=gM/(g^2\widehat Q\widehat q_1)=M/(g\widehat Q\widehat q_1)$; $x_3\ne0$ gives $M\ne0$. Modulo $\widehat Q$: $M\equiv\mu\widehat q_1$, and $\gcd(\mu,\widehat Q)\mid\gcd(\mu,Q)=1$, $\gcd(\widehat q_1,\widehat Q)=1$ by (a), so $\gcd(M,\widehat Q)=1$. Modulo $\widehat q_1$: $M\equiv-p_1\widehat Q$, and $\gcd(p_1,\widehat q_1)\mid\gcd(p_1,q_1)=1$, $\gcd(\widehat Q,\widehat q_1)=1$, so $\gcd(M,\widehat q_1)=1$. By (a) these combine to $\gcd(M,\widehat Q\widehat q_1)=1$. (c) By (b), the only cancellation in $M/(g\widehat Q\widehat q_1)$ is by $\gcd(M,g\widehat Q\widehat q_1)=\gcd(M,g)$, giving the displayed reduced forms; the inequality follows from $\gcd(g,M)\le g$, with equality iff $\gcd(g,M)=g$, i.e. $g\mid M$. (d) $q_3\le2D$ and $q_3\ge Qq_1/g^2$ give $g\ge\sqrt{Qq_1/(2D)}$; and $\gcd(g,M)=g\widehat Q\widehat q_1/q_3\ge g\cdot(Qq_1/g^2)/(2D)=Qq_1/(2Dg)$. This matches the state statement of `M9-M2-NF-participation-rigidity` exactly, with the equality case added. Status: proved_internal, no coefficient hypotheses; H4 enters only when NF-2 is combined with the lift-weight bound of NF-0.

**Worked verification of NF-2 (equality case).** Take $r=4/15$ ($\mu=4$, $Q=15$), $x_1=1/6$ ($p_1=1$, $q_1=6$). Then $g=\gcd(15,6)=3$, $\widehat Q=5$, $\widehat q_1=2$, $M=4\cdot2-1\cdot5=3$. Check (b): $\gcd(\widehat Q\widehat q_1,M)=\gcd(10,3)=1$. Check (c): $\gcd(g,M)=3$, $q_3=3\cdot5\cdot2/3=10$, and directly $x_3=4/15-1/6=3/30=1/10$, reduced denominator $10$; the lower bound $Qq_1/g^2=90/9=10$ is attained, consistent with $g\mid M$ ($3\mid3$). All clauses verified.

Part III. Overlap bookkeeping OB-1 for the reduced-paired stratum.

Let $\mathcal E$ denote the set of participating exact-resonance quadruples $((h_i,d_i))_{i=1}^4$ with $N=0$; since $Q_\times=d_1d_2d_3d_4\ne0$, $N=0$ is equivalent to the rational equation $x_1-x_2+x_3-x_4=0$, i.e. $x_1+x_3=x_2+x_4$, where $x_i=h_i/d_i$ has reduced form $p_i/q_i$. Let $\mathcal Q\subset\mathcal E$ be the subset whose reduced-denominator multiset $\{q_1,q_2,q_3,q_4\}$ has shape $\{q,q,q',q'\}$ (patterns $(4)$ and $(2,2)$; the complement of $\mathcal Q$ in $\mathcal E$, patterns $(3,1)$, $(2,1,1)$, $(1,1,1,1)$, is by definition the URES stratum). Define, set-theoretically:

- FM $:=\{x\in\mathcal E:\{x_1,x_3\}=\{x_2,x_4\}$ as multisets of values$\}$; explicitly $(x_1=x_2\wedge x_3=x_4)\vee(x_1=x_4\wedge x_3=x_2)$. The first branch is exactly the family of `M9-M2-fraction-matching-weighted-bound`; the second follows from it by the index relabeling $2\leftrightarrow4$, which is a symmetry of the absolute mass.
- AP (anti-paired / sign-symmetric) $:=\{x\in\mathcal E:x_1+x_3=0\}$, equivalently $x_2+x_4=0$ given the resonance.
- Denominator patterns: CROSS $:\iff(q_1=q_2\wedge q_3=q_4)\vee(q_1=q_4\wedge q_2=q_3)$; SAME $:\iff q_1=q_3\wedge q_2=q_4$.
- U-2 $:=(\mathcal Q\setminus(\mathrm{FM}\cup\mathrm{AP}))\cap\mathrm{CROSS}$; SS $:=(\mathcal Q\setminus(\mathrm{FM}\cup\mathrm{AP}))\cap\mathrm{SAME}$.

**OB-1 (coverage and overlap; proved_internal).** (i) FM $\subset\mathcal Q$ and AP $\subset\mathcal Q\cap\mathrm{SAME}$. (ii) Coverage: $\mathcal Q=\mathrm{FM}\cup\mathrm{AP}\cup\text{U-2}\cup\mathrm{SS}$. (iii) Overlaps: $\mathrm{FM}\cap\text{U-2}=\mathrm{FM}\cap\mathrm{SS}=\mathrm{AP}\cap\text{U-2}=\mathrm{AP}\cap\mathrm{SS}=\emptyset$ by construction; $\mathrm{FM}\cap\mathrm{AP}\ne\emptyset$ (example $(a,a,-a,-a)$, which satisfies $a-a+(-a)-(-a)=0$, $x_1=x_2$, $x_3=x_4$, $x_1+x_3=0$); $\text{U-2}\cap\mathrm{SS}$ is contained in the all-equal stratum $q=q'$ and is nonempty there (example below). Hence the covering multiplicity of the four classes is at most $2$, a fortiori at most $3$ as recorded in the Summary; if instead U-2 and SS are taken in their natural forms without excluding $\mathrm{FM}\cup\mathrm{AP}$, the multiplicity is at most $4$ (attained only on the all-equal stratum). For absolute-mass upper bounds any finite covering multiplicity is harmless; for any future signed identity the exact partition $\mathrm{FM}\succ\mathrm{AP}\succ\text{U-2}\succ\mathrm{SS}$ (assign each tuple to the first class containing it) must be used. (iv) If $q\ne q'$, each tuple in $\mathcal Q$ satisfies exactly one of CROSS, SAME; moreover $\mathrm{SAME}\cap\mathrm{FM}=\emptyset$ when $q\ne q'$ (FM forces $q_1=q_2$ or $q_1=q_4$, both of which force $q=q'$ under SAME).

Proof. (i) Matching values have equal reduced denominators, so FM tuples realize CROSS with the split $\{1,2\}\,|\,\{3,4\}$ or $\{1,4\}\,|\,\{2,3\}$; AP forces $q_1=q_3$ and $q_2=q_4$. (ii) The two denominator-pairs of a $\{q,q,q',q'\}$ multiset occupy one of the three unordered splits of positions: $\{1,2\}\,|\,\{3,4\}$, $\{1,4\}\,|\,\{2,3\}$ (CROSS), or $\{1,3\}\,|\,\{2,4\}$ (SAME); at least one holds (all three hold when $q=q'$), so every element of $\mathcal Q\setminus(\mathrm{FM}\cup\mathrm{AP})$ lands in U-2 or SS. (iii) and (iv) are direct case checks as indicated. Nonemptiness of SS on the all-equal stratum: with a common denominator $q$ in the participation window, take numerators $(p_1,p_2,p_3,p_4)=(1,3,7,5)$: $1+7=3+5$, $\{1,7\}\ne\{3,5\}$, $1+7\ne0$; realizable once $(H/D)q\ge7$, e.g. $q\asymp D$ and $X$ large; this tuple lies in both natural patterns, confirming the all-equal double count. Status: proved_internal.

**OB-2 (gcd rigidity mechanism; proved_internal, uses only the participation window $|x_i|\le H/D$).** Let $x\in\mathcal Q\setminus(\mathrm{FM}\cup\mathrm{AP})$ with denominator values $q,q'$. In the CROSS case with split $\{1,2\}\,|\,\{3,4\}$, put $y=x_1-x_2=x_4-x_3$; in the split $\{1,4\}\,|\,\{2,3\}$, put $y=x_1-x_4=x_2-x_3$; in the SAME case put $y=x_1+x_3=x_2+x_4$. In all cases $y\ne0$ (vanishing would place the tuple in FM, respectively AP), and the reduced denominator $f$ of $y$ divides both $q$ and $q'$, hence $f\mid\gcd(q,q')$; since $0<|y|\le2H/D$ we get $f\ge D/(2H)$ and therefore
$$
\gcd(q,q')\ \ge\ \frac{D}{2H}\ \asymp\ X^{1/4}.
$$
On the all-equal stratum the same argument gives a divisor $f\mid q$ with $f\ge D/(2H)$. This is the congruence rigidity that powers the mass bound of `M9-M2-unpaired-reduced-paired-bound`; that bound itself remains at its current status (derived_under_assumptions, H4-blocked) and is not re-proved here. Note that OB-2 is superseded in strength, for absolute mass purposes, by the URES energy bound of Part IV, which controls all exact resonances at once.

Finally, the residual is genuinely nonempty even under the H4 parity support: besides the known pattern-$(1,1,1,1)$ family $1/(6k)-1/(15k)+1/(10k)-1/(5k)=0$, the pattern-$(3,1)$ tuple
$$
\frac{1}{15}-\frac{7}{15}+\frac{1}{15}-\Big(-\frac{1}{3}\Big)=-\frac{5}{15}+\frac{5}{15}=0
$$
has all numerators odd (so it survives (K-par)), reduced-denominator multiset $\{15,15,15,3\}$, and scales to the participation window by $x_i\mapsto x_i/m$ with $m$ odd, $7\nmid m$, $m\asymp D/15$. So parity alone cannot empty URES, and both URES shapes $(3,1)$ and $(1,1,1,1)$ must be covered by any residual bound. A3 should add this $(3,1)$ family to the enumeration list alongside $(6,10,15,5)k$.

Part IV. URES: definitions, exact reductions, and a complete class-level proof.

**Definitions.** A pair $(h,d)$ participates if $1\le|h|\le H$, $d\in[D,2D)$. For $r\in\mathbb Q$ define the representation-weighted pair-sum
$$
R(r)\;:=\;\sum_{\substack{(h,d),(h',d')\ \mathrm{participating}\\ h/d+h'/d'=r}}\big|\beta_h\,\beta_{h'}\,w_D(d)\,w_D(d')\big|,
$$
an ordered-pair sum. Two remarks fix the bookkeeping that caused the Round 6 rejection of the earlier unpaired-mass claim: (lifts) grouping each $(h,d)$ by its reduced fraction $p/q$ and lift $g=d/q$, NF-0 gives $\sum_{g\in[D/q,2D/q)}|\beta_{gp}w_D(gq)|\le cKW/|p|$ under (K-mag), with $c$ absolute, so all dyadic lifts are absorbed with explicit multiplicity; (overlaps) all bounds below are for absolute mass, so covering multiplicities from Part III never enter.

**URES-E (energy identity; proved_internal).** Grouping exact-resonance quadruples by the common value $r=x_1+x_3=x_2+x_4$, the weights factorize over the two pairs, and
$$
\Sigma^{\mathrm{abs}}_{N=0}\;=\;\sum_{r\in\mathbb Q}R(r)^2\;=\;R(0)^2+\sum_{r\ne0}R(r)^2 .
$$
The $r=0$ term is exactly the AP class. The identity is exact; no hypotheses.

**URES-M1 (first moment; proved_internal under (K-mag)).** Since every ordered pair has a unique $r$,
$$
\sum_{r}R(r)\;=\;\Big(\sum_{(h,d)}|\beta_h w_D(d)|\Big)^2\;\le\;\big(cKWD\log(2H)\big)^2\;\ll\;K^2W^2D^2\log^2(2H).
$$

**URES-R (reduction to a pointwise representation bound; proved_internal).** By the trivial inequality $\sum_{r\ne0}R(r)^2\le\big(\sup_{r\ne0}R(r)\big)\sum_{r\ne0}R(r)$ and URES-M1, the target of `M9-M2-unpaired-residual-URES` follows from
$$
\textbf{(URES-P)}\qquad \sup_{r\ne0}R(r)\ \ll_\epsilon\ X^{\epsilon}.
$$
This converts a second-moment problem into a pointwise divisor-type count: how much weighted mass can concentrate on a single nonzero value.

**URES-P, divisor-compatible subfamily (proved_internal under (K-mag)).** Fix reduced $r=\mu/Q\ne0$. Restrict to representations with $q_1\mid Q$ (so $g=q_1$, $\widehat q_1=1$ in NF-2). Then $q_1$ ranges over divisors of $Q$ in the window, at most $d(Q)$ values; for each, NF-0 bounds the two lift sums by $cKW/|p_1|$ and $cKW/|p_3|\le cKW$, and $\sum_{0<|p_1|\le2H}1/|p_1|\ll\log(2H)$, giving mass $\ll K^2W^2\,d(Q)\log(2H)\ll_\epsilon X^\epsilon$ since $Q\le\mathrm{lcm}(q_1,q_3)\le4D^2\le4X$. The symmetric family $q_3\mid Q$ is identical. This was the subcase announced in the Summary.

**URES-D (representation-count divisor bound; proved_internal; supersedes the announced congruence-lattice residual).** Pushing the NF-2 congruence analysis to its endpoint yields a complete multiplicity bound, which corrects the Summary: no residual congruence-lattice obligation remains. Claim: for fixed reduced $r=\mu/Q\ne0$ and fixed nonzero integers $p_1,p_3$, the number of pairs $(q_1,q_3)$ of positive integers with $p_1/q_1+p_3/q_3=\mu/Q$ (reducedness and windows only thin the set) is at most $2\,d\big(Q^2|p_1p_3|\big)$. Proof. Clearing denominators, $\mu q_1q_3=Q(p_1q_3+p_3q_1)$; multiplying by $\mu$ and completing the product gives the exact factorization identity
$$
(\mu q_1-Qp_1)(\mu q_3-Qp_3)\;=\;Q^2p_1p_3 .
$$
Neither factor vanishes: $\mu q_1=Qp_1$ with $\gcd(\mu,Q)=1$ and $\gcd(p_1,q_1)=1$ forces $x_1=r$, hence $x_3=0$, excluded since $|h'|\ge1$. The map from solutions to ordered factorizations $A\cdot B=Q^2p_1p_3$, $A=\mu q_1-Qp_1$, $B=\mu q_3-Qp_3$, is injective, because $q_1=(A+Qp_1)/\mu$ and $q_3=(B+Qp_3)/\mu$ recover the solution; the number of ordered factorizations of the nonzero integer $Q^2p_1p_3$ (sign of $A$ free, $B$ determined) is at most $2\,d(Q^2|p_1p_3|)$. Numeric verification at $r=4/15$: $(x_1,x_3)=(1/6,1/10)$ gives $A=9$, $B=25$, $AB=225=Q^2p_1p_3$; $(1/15,1/5)$ gives $(45)(5)=225$; the mixed-sign pair $(7/15,-1/5)$ gives $(-45)(35)=-1575=225\cdot7\cdot(-1)$. All match, and $q_1=(A+Qp_1)/\mu$ recovers $6,15,15$ respectively.

**URES-P in full (proved_internal under (K-mag); actual $\beta_h$: derived_under_assumptions, blocked by `H4-source-audit`).** For any reduced $r\ne0$,
$$
R(r)\ \le\ c^2K^2W^2\sum_{\substack{0<|p_1|\le2H\\ 0<|p_3|\le2H}}\frac{2\,d(Q^2|p_1p_3|)}{|p_1||p_3|}\ \le\ c'K^2W^2\Big(\max_{|p_i|\le2H}d(Q^2|p_1p_3|)\Big)\log^2(2H)\ \ll_\epsilon\ X^{\epsilon},
$$
using NF-0 for the two lift sums, URES-D for the multiplicity per numerator pair, $|p_i|\le(H/D)q_i\le2H$ from NF-0, and the divisor bound $d(n)\ll_\epsilon n^\epsilon$ with $n=Q^2|p_1p_3|\le(4D^2)^2(2H)^2\le64X^{5/2}$. The bound is uniform in $r$ and in $D\in[X^{1/4},X^{1/2}]$ including the endpoint, since no step used the size of $D$ beyond window truncation.

**URES-F (the state target; same status as URES-P).** Combining URES-R with URES-P:
$$
\sum_{r\ne0}R(r)^2\ \ll_\epsilon\ D^2X^{\epsilon}.
$$
This is precisely the displayed inequality of `M9-M2-unpaired-residual-URES`, and it a fortiori bounds the URES residual class, since residual mass is a sub-sum of $\sum_{r\ne0}R(r)^2$.

**EXN0-T (total exact-resonance mass; same status).** The $r=0$ term satisfies $R(0)\le(cKW)^2\sum_{q\le2D}\sum_{p\ne0}p^{-2}\ll K^2W^2D$, so by URES-E
$$
\Sigma^{\mathrm{abs}}_{N=0}\ \ll_\epsilon\ D^2X^{\epsilon}\qquad\text{uniformly for }X^{1/4}\le D\le X^{1/2}.
$$
Scope discipline: this settles only the exact $N=0$ arm at absolute-mass level under the coefficient class; it does not touch near-collisions $0<|N|\le M$ (`M9-near-collision-estimate` stays open), does not give average-to-pointwise or endpoint sup-norm control, and does not move `M9-M2` or `M9`. Because this is a single-agent, single-round proof, I recommend promotion only after A2 verifies the factorization identity, the injectivity step, and the NF-0 lift bookkeeping in Stage B; the exposed failure surface is small (three displayed identities and two harmonic sums), which is why the claim is checkable.

Part V. SPD backup.

**SPD-1 (exact required theorem; proposed).** Under H4 the M2 kernel is the smoothed odd-harmonic square wave $V_H(\theta)=\sum_{1\le|h|\le H}\beta_he(h\theta)=-\frac{2}{\pi}\sum_{0\le m,\ 2m+1\le H}\frac{(-1)^m\Phi\big(\frac{2m+1}{H+1}\big)}{2m+1}\cos(2\pi(2m+1)\theta)$, whose sharp limit is $-\frac12\,\mathrm{sgn}\cos(2\pi\theta)$ with jumps at $\theta\equiv\pm\frac14\ (\mathrm{mod}\ 1)$. The exact theorem the SPD route requires is: uniformly for $X^{1/4}\le D\le X^{1/2}$,
$$
\Big|\sum_{d\in[D,2D)}w_D(d)\,V_{H_D}\Big(\frac{X}{4d}\Big)\Big|\ \ll_\epsilon\ X^{1/4+\epsilon},
$$
whose unsmoothed core is signed equidistribution of the parity sequence $\varepsilon_d=(-1)^{\lfloor X/(2d)+1/2\rfloor}$: $\sum_{d\asymp D}w_D(d)\varepsilon_d\ll_\epsilon X^{1/4+\epsilon}$. This is a reformulation of `M9-M2` with explicit sign structure, not an a priori easier statement; its value is diagnosability. **SPD-J (jump-set divisor lemma; proved_internal):** the exact jump condition $X/(4d)\equiv\pm1/4\ (\mathrm{mod}\ 1)$ means $X\equiv\pm d\ (\mathrm{mod}\ 4d)$, i.e. $X=d(4k\pm1)$, so $d\mid X$ with cofactor $\equiv\pm1\ (\mathrm{mod}\ 4)$; hence at most $d(X)\ll_\epsilon X^\epsilon$ values of $d\in[D,2D)$ sit on a jump, so the sharp/smoothed discrepancy at exact jumps is divisor-bounded; the near-jump band $\|X/(4d)\mp1/4\|\le\delta_0$ remains a near-divisor count and is logged as obligation SPD-2 (open). **Falsification threshold for A3:** define $P(D,H;X)=|S_2^{\mathrm{sq}}(D;X)|/X^{1/4}$ with the sharp square-wave weights; over a grid of $X$ spanning three decades at $D=X^{1/2}$, fit $\log P$ against $\log X$; a stable fitted exponent $\ge0.02$ falsifies SPD-1 as stated (reject the route); a bounded or logarithmic $P$ keeps it proposed. Compare true $\beta$ signs against unsigned, random, and adversarial signs per the standing task in `M9-M2-reciprocal-SPD-route`.

**Claim ledger.** DP-0/DP-1/DP-2/DP-3: proved_internal at class level under (K-par)/(K-mag); DP-A: derived_under_assumptions (H4). NF-0/NF-1/NF-2, OB-1, OB-2, URES-E, URES-M1, URES-R, URES-D, SPD-J: proved_internal. URES-P, URES-F, EXN0-T: proved_internal at class level, derived_under_assumptions for actual $\beta_h$ (blocked by `H4-source-audit`), promotion recommended only after Stage B verification. SPD-1, SPD-2, GM ladder (below): proposed. DP-1 sharpness construction ($b=a+1$, $u=-v=2$): diagnostic remark showing the DP-1 threshold is order-sharp.

## Theorem-dependency audit

1. H4 / `M9-M2-beta-algebra` (source_audit_required): supplies (K-par) exactly and (K-mag) with $K=\Phi_0/\pi$; needed only by DP-A and by the actual-$\beta$ readings of URES-P/URES-F/EXN0-T. All class-level lemmas are H4-free.
2. `H4-Phi-regularity` (derived_under_assumptions): source of $\sup|\Phi|=\Phi_0<\infty$ inside (K-mag).
3. `M9-M2-harmonic-convolution-LH` (proved_internal): used in DP-2 only.
4. `M9-M2-fourth-moment-expansion` (derived_under_assumptions): supplies the identification $N=0\iff x_1-x_2+x_3-x_4=0$ via $Q_\times\ne0$; the identification step itself is internal algebra.
5. `M9-M2-coprime-rigidity-normal-form` (proved_internal): formalized here as NF-1/NF-2.
6. Elementary divisor bound $d(n)\ll_\epsilon n^\epsilon$: classical and provable in a few lines from multiplicativity; I treat it as internal-grade elementary number theory and flag to the judge that no source card should be required; if the judge disagrees, URES-P inherits a source-audit blocker.
7. No Li--Yang, Huxley, Bourgain--Watt, or Vaaler-beyond-H4 dependencies appear anywhere in Parts I--V.

## Hidden assumptions and potential gaps

The definition of $R(r)$ is fixed here as the weighted ordered-pair sum; if Round 6 intended an unweighted or unordered normalization, URES-R survives but URES-P must be restated (an unweighted variant is genuinely larger by lift factors $\asymp D/q$), so A1 should reconcile the definition against the Round 6 text before patching. The dyadic block convention $[D,2D)$ and $|w_D|\le W$ are assumed throughout; constants shift under other conventions. (K-mag)'s constant is H4-audit-dependent. URES-F/EXN0-T are single-agent unreviewed proofs this round; the protocol's promotion discipline applies. All bounds are absolute-mass; signed refinements are untouched. Windows and coprimality were used only to thin counts, so nothing here yields lower bounds or asymptotics. Near-collision bands, average-to-pointwise, and endpoint sup-norm control are explicitly outside the scope of every claim above.

## Counterexample or obstruction search

Searched for URES-P violations: high-multiplicity values $r=\mu/Q$ with smooth $Q$ (Egyptian-fraction type, $d(Q^2)$ representations with $p_i=\pm1$) meet the divisor bound exactly and stay within $X^\epsilon$; the factorization identity caps multiplicity structurally, so no violating family exists for the weighted $R$. The odd-parity $(3,1)$ family above shows parity cannot empty URES. The DP-1 sharpness construction shows the thin-band threshold cannot be improved beyond constants. For the exploratory ladder, the $k=1$ obstruction $D\le X^{1/3}$ (from off-diagonal mass $D^4$ versus $XD$) is recorded as the first hard wall of the global-moment route.

## Verification

Numeric checks performed inline: three factorization-identity instances at $r=4/15$ including a mixed-sign pair; the NF-2 equality case; the odd-parity $(3,1)$ resonance; the SS all-equal example $(1,3,7,5)$; DP-1 sharpness. Requested A3 verifications (all diagnostic_only): exact-arithmetic evaluation of $\sum_{r\ne0}R(r)^2/D^2$ and $\sup_{r\ne0}R(r)$ at $D=X^{1/4},X^{3/8},X^{1/2}$; brute-force confirmation of OB-1 exhaustiveness and multiplicities on small windows; symbolic spot-checks of $(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3$ on random tuples; DP-2 mass against $C_0D\log^2(2H)$; the SPD threshold protocol.

## Divergent alternatives and 20% exploration

Global-moment/large-value propagation map for $D\le X^{1/2-\eta}$ (all items proposed or diagnostic). Define $G_{2k}(D)=\int_X^{2X}|S_2(D;t)|^{2k}dt$. The Lipschitz envelope $\sup|S_2'|\ll KWH$ (internal, one line) gives the propagation principle: $|S_2(t_0)|\ge2V$ forces $|S_2|>V$ on a set of measure $\ge V/(cKWH)$, hence $\sup_{[X,2X]}|S_2|\ll(G_{2k}H)^{1/(2k+1)}$. Benchmark Gaussian-strength moments $G_{2k}\ll_\epsilon X^{1+\epsilon}D^k$ (proposed) then yield the M2 target exactly for $D\le X^{1/2-1/(k+1)}$: $k=2$ covers $D\le X^{1/6}$, $k=3$ covers $X^{1/4}$, $k=5$ covers $X^{1/3}$, and the endpoint requires $k=\infty$, which quantifies and sharpens the Round 6 subcoherence obstruction: no fixed-order Gaussian-strength global moment plus Lipschitz propagation reaches $D=X^{1/2}$. New reduction worth logging: URES-F (proved here) supplies the resonant diagonal of $G_4$ at Gaussian strength $X^{1+\epsilon}D^2$, and the graded near-collision target of `M9-near-collision-estimate`, $\Sigma_{\mathrm{abs}}(0<|N|\le M)\ll_\epsilon D^2\max(1,MX/D^4)X^\epsilon$, supplies the off-resonant part via the kernel $\min(X,Q_\times/|N|)$ summed over dyadic $M\le HD^3$; together they give $G_4\ll_\epsilon X^{1+\epsilon}D^2$, hence the pointwise M2 bound for $D\le X^{1/6}$. So after this round the graded near-collision estimate is the single analytic bottleneck of the entire global-moment route, and the endpoint remains a sign-cancellation problem (SPD-1 or the A2 Poisson route). Falsification test: A3 estimates $G_4(D)/(XD^2)$ numerically; growth like a positive power of $X$ at $D=X^{1/3}$ would refute the Gaussian benchmark before proof effort is spent.

## Useful lemmas

NF-0, NF-1, NF-2, OB-1, OB-2, DP-0 through DP-3, URES-E, URES-M1, URES-R, URES-D, URES-P, URES-F, EXN0-T, SPD-J, plus the propagation principle, all stated above with proofs or exact status; NF-2 and URES-D are the reusable cores (URES-D is a general two-fraction multiplicity bound applicable to any future stratum, including near-collision variants with $r$ replaced by a short interval of values).

## What should be tested next

A2: referee URES-D injectivity, the NF-0 lift bookkeeping, and the $R(r)$ definition reconciliation; then attempt the graded near-collision estimate using URES-D's interval variant. A3: the five diagnostic bundles in Verification, with the $(3,1)$ family added to the URES enumeration. A1: reconcile $R(r)$ with the Round 6 text, decide the divisor-bound sourcing question, and fold DP-0..DP-3/NF/OB/URES statements into `state/best_proof_draft.md` and the lemma bank.

## Proposed state patch, if any

For the judge's decision, using existing ids plus proposed new ones: update `M9-M2-unpaired-residual-URES` from open to derived_under_assumptions (blockers: `H4-source-audit`), conditional on A2 Stage B verification, else keep open with positive evidence rounds/obligation-main/round_007/responses/A4-007.md. Create `M9-M2-URES-energy-reduction` (lemma, proved_internal: URES-E, URES-M1, URES-R), `M9-M2-URES-representation-divisor-bound` (lemma, proved_internal: URES-D), and `M9-M2-exact-N0-total-mass` (lemma, derived_under_assumptions, blockers `H4-source-audit`: EXN0-T; implies the exact side of `M9-M2-N0-diagonal-core-bound` and the exact arm of `M9-near-collision-taxonomy`). Update `M9-M2-DP-near-collision-bound` (DP-0..DP-3 class-level transcription with DP-A carrying H4), `M9-M2-coprime-rigidity-normal-form` and `M9-M2-NF-participation-rigidity` (lemma-bank transcription complete), `M9-M2-unpaired-reduced-paired-bound` (OB-1 bookkeeping supplied), `M9-M2-reciprocal-SPD-route` (SPD-1 statement, SPD-J, falsification threshold; keep proposed). Optionally create `M9-M2-GM4-from-exact-plus-graded` (reduction, proposed). No change to `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `GC-target`, `H4`.

## Confidence

High (0.88) on DP-0..DP-3, NF-0/1/2, OB-1/OB-2, URES-E/M1/R, URES-D, SPD-J, each verified against numeric instances. Moderately high (0.82) that URES-P/URES-F/EXN0-T are fully correct as stated, pending independent Stage B review of the three identities and two harmonic sums that carry the proof. Low (0.2) that SPD-1 is materially easier than `M9-M2` itself. The exploratory ladder is heuristic except for the stated internal envelope; its moment benchmarks are unproved. Nothing in this round moves `M9`, `M9-M2`, or the Gauss circle target.

## State-Change Review Task

Review proposed new obligations, status changes, dependency changes, evidence files, and no-change claims. Prefer accepting, revising, or rejecting state mutations over giving a broad prose critique.

## Review-Stage Guardrail

This is Stage B cross review for Round 7.

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
