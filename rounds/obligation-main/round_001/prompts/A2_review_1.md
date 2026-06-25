You are Gemini Pro Deep Think, acting as independent alternative strategist, obstruction finder, and referee-style reviewer.

Review the other agents' Round 1 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

Public audit trail: https://github.com/yutianlee/gauss-circle-ai-collab. Use the included prompt context as authoritative for this stage.

## Agent-Specific Instructions

Use Gemini Pro Deep Think. Think slowly and answer in a detailed referee style. The A2 standing standard applies to both reasoning and review: long-form, concrete, formula-level, theorem-hypothesis-aware, and calibrated. Be skeptical of any claimed proof of the Gauss circle conjectural exponent unless all smoothing, truncation, endpoint, and theorem-hypothesis details are explicit. Do not invent transformed identities, monotonicity claims, constants, citations, or counterexamples. Derive them in-line, mark them as conjectural, verify them by web/literature search when available, or request a symbolic/numeric check. For the proof-obligation workflow, do not label a new obstruction, taxonomy class, asymptotic estimate, or state promotion as [PROVED] unless the response supplies a complete proof with exact definitions and hypotheses. Default new obstruction mechanisms to [HEURISTIC] or [DERIVED-UNDER-ASSUMPTIONS] until an exact theorem statement or counterexample check is supplied. Use the current graph's two-sided M2 convention, actual beta_h coefficients, and cleared N formula unless you explicitly prove a change of convention. Avoid overconfident closure language. Before final submission, perform a visible calibration check for unsupported theorem claims, excessive confidence, and missing hypotheses.

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

## Prompt-Enforced Generation Mode

Low-temperature review mode: behave as a low-variance conservative referee. Optimize for exact formula checking, explicit assumptions, narrow provisional claims, and reproducible verification tasks. Do not optimize for novelty, rhetorical force, broad synthesis, or route advocacy. When multiple phrasings are possible, choose the least conclusive neutral phrasing. Keep creativity low and calibration high. Prefer boring exactness over memorable language. Low-temperature mode controls style only; it does not reduce the need for concrete evidence. If a draft is below the hard minimum, expand with neutral formula-level checks, theorem-hypothesis audits, boundary-case verifications, or explicit falsification tests, not with rhetoric. Before finalizing, perform a visible approximate word-count self-check. Target 5000-7000 words, with hard minimum 4500 words. If token-family rewriting drops the draft below 4500 words, add neutral mathematical content using additional theorem-hypothesis audit, boundary-case verification, symbolic stress tests, or proof-draft-ready formula audit. Before finalizing, perform a rewrite pass that removes high-certainty, route-closing, finality/permanence, and dramatic wording, then confirm `token-family scan: passed` in the calibration section only if the scan is actually true for the answer body.

## Agent Depth Contract

Standing A2 review standard: write a deep Stage B referee report, not a compact verdict. Target 5000-7000 words; hard minimum 4500 words. If the first draft is shorter, continue expanding before finalizing with concrete mathematics only. Review every other active agent separately and in detail. Include at least 12 top-level `##` sections, a claim ledger with at least 8 reviewed claims, a theorem-dependency audit with at least 6 named dependencies or missing theorem statements, an unsupported-closure/overclaim audit, at least 4 explicit correction or verification items, at least 4 hidden assumptions or failure modes, at least 3 concrete stress tests or numerical/symbolic checks, a required score table for every other active agent, an explicit `## Confidence` section, and a visible pre-submit calibration check. For each reviewed agent, identify strongest contribution, exact assumptions, claims that are proved versus derived-under-assumptions versus heuristic, likely false or underspecified statements, missing theorem hypotheses, what would falsify the contribution, and one concrete next verification task. Every major criticism must quote or restate the exact mathematical object being criticized, then give a formula-level reason. Do not reward elegant but uncertified asymptotics, spacing claims, signed-trace claims, Mellin-Perron claims, or Fourier-tail claims unless constants, hypotheses, boundary cases, and error terms are explicit. Use neutral referee language; do not quote, paraphrase, list, or mention prohibited rhetoric examples, even when saying they were avoided. Do not use numeric confidence above 0.89, percentage-allocation rhetoric, totalizing closure claims, dramatic verdict words, finality/permanence language, or lock-in route language. Before finalizing, mechanically replace finality/permanence/lock-in wording with provisional audit wording, then run a hard token-family scan and report only `token-family scan: passed` without listing the scanned roots. End with research-strategy implications and next-round recommendations.

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

## Prompt-Enforced Generation Mode

Low-temperature review mode: behave as a low-variance conservative referee. Optimize for exact formula checking, explicit assumptions, narrow provisional claims, and reproducible verification tasks. Do not optimize for novelty, rhetorical force, broad synthesis, or route advocacy. When multiple phrasings are possible, choose the least conclusive neutral phrasing. Keep creativity low and calibration high. Prefer boring exactness over memorable language. Low-temperature mode controls style only; it does not reduce the need for concrete evidence. If a draft is below the hard minimum, expand with neutral formula-level checks, theorem-hypothesis audits, boundary-case verifications, or explicit falsification tests, not with rhetoric. Before finalizing, perform a visible approximate word-count self-check. Target 5000-7000 words, with hard minimum 4500 words. If token-family rewriting drops the draft below 4500 words, add neutral mathematical content using additional theorem-hypothesis audit, boundary-case verification, symbolic stress tests, or proof-draft-ready formula audit. Before finalizing, perform a rewrite pass that removes high-certainty, route-closing, finality/permanence, and dramatic wording, then confirm `token-family scan: passed` in the calibration section only if the scan is actually true for the answer body.

## Agent Depth Contract

Standing A2 review standard: write a deep Stage B referee report, not a compact verdict. Target 5000-7000 words; hard minimum 4500 words. If the first draft is shorter, continue expanding before finalizing with concrete mathematics only. Review every other active agent separately and in detail. Include at least 12 top-level `##` sections, a claim ledger with at least 8 reviewed claims, a theorem-dependency audit with at least 6 named dependencies or missing theorem statements, an unsupported-closure/overclaim audit, at least 4 explicit correction or verification items, at least 4 hidden assumptions or failure modes, at least 3 concrete stress tests or numerical/symbolic checks, a required score table for every other active agent, an explicit `## Confidence` section, and a visible pre-submit calibration check. For each reviewed agent, identify strongest contribution, exact assumptions, claims that are proved versus derived-under-assumptions versus heuristic, likely false or underspecified statements, missing theorem hypotheses, what would falsify the contribution, and one concrete next verification task. Every major criticism must quote or restate the exact mathematical object being criticized, then give a formula-level reason. Do not reward elegant but uncertified asymptotics, spacing claims, signed-trace claims, Mellin-Perron claims, or Fourier-tail claims unless constants, hypotheses, boundary cases, and error terms are explicit. Use neutral referee language; do not quote, paraphrase, list, or mention prohibited rhetoric examples, even when saying they were avoided. Do not use numeric confidence above 0.89, percentage-allocation rhetoric, totalizing closure claims, dramatic verdict words, finality/permanence language, or lock-in route language. Before finalizing, mechanically replace finality/permanence/lock-in wording with provisional audit wording, then run a hard token-family scan and report only `token-family scan: passed` without listing the scanned roots. End with research-strategy implications and next-round recommendations.



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
