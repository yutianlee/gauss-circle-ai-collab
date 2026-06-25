# Gauss Circle AI Collaboration

This repository is a public-memory workflow for multi-AI research on the Gauss circle problem.
The workflow is claim-centered: `state/proof_obligations.yml` is the authoritative mathematical state, while round transcripts are audit evidence.

It is adapted from the KKT workflow in `yutianlee/kkt-ai-collab`, but this repo uses exactly three agents:

- `A1`: ChatGPT Extended Pro through the web UI.
- `A2`: Gemini Pro Deep Think through the web UI.
- `A3`: Deepseek V4 Pro through the API.

There is no `A4` and no Qwen agent in this Gauss workflow.

## Target

Let

```text
N(R) = #{(m,n) in Z^2 : m^2 + n^2 <= R^2}.
```

The Gauss circle problem asks for the best possible exponent in

```text
N(R) = pi R^2 + E(R).
```

The conjectural bound is

```text
E(R) = O_epsilon(R^{1/2 + epsilon})
```

for every epsilon > 0. The workflow is not allowed to claim a solution without a complete proof; its job is to isolate precise reductions, lemmas, obstructions, citations, and verification tasks.

## Agent Roles

- `A1` is the broad strategist, literature scout, synthesis writer, and default judge. Use ChatGPT Extended Pro or the strongest available long-reasoning mode.
- `A2` is the independent referee and obstacle finder. Use Gemini Pro Deep Think and ask for long, conservative, theorem-hypothesis-aware reports.
- `A3` is the automatic API proof auditor. Use Deepseek V4 Pro with maximum available reasoning effort for algebra checks, exponential-sum normalization audits, obstruction searches, and reproducible verification plans.

A1 and A2 are semi-manual: paste prompts into persistent web conversations and save copied Markdown responses into `handoff/`. A3 is automatic when `DEEPSEEK_API_KEY` is configured.

## Round Protocol

Each round uses these synchronized stages:

1. Stage A: every active agent independently attacks selected proof obligations.
2. Stage B: every active agent reviews proposed state changes, blockers, evidence, and status claims from the other agents.
3. Stage C: A1 writes a judge synthesis, next-round prompts, and a machine-readable `State Patch`.
4. Stage D: the orchestrator validates the `State Patch`, applies accepted changes to `state/proof_obligations.yml`, and regenerates the compact reading packet.

The round barrier is strict: reviews do not start until all three reasoning responses are present; judging does not start until all three reviews are present; state mutation does not happen until the judge synthesis has a valid patch.

## Layout

```text
problems/
  gauss_circle.md
protocol.md
config/
  agents.example.json
  agents.web-test.json
math_collab/
  orchestrator.py
  proof_obligations.py
  validate_state_patch.py
  validate_round.py
  human.py
  normalize_markdown.py
state/
  proof_obligations.yml
  next_round_prompts.md
  last_validation_report.md
  current_state.md
  lemma_bank.md
  gap_register.md
  best_proof_draft.md
sources/
  vaaler_1985.md
  li_yang_2023.md
  huxley_2003.md
  bourgain_watt.md
human/
  current_directives.md
  goals.md
  ideas.md
  references.md
  inbox/
manifests/
  reading_packet.md
rounds/
  <run-id>/
handoff/
  <run-id>/
```

`rounds/` is the public archive. `handoff/` is ignored by Git and is used for temporary web prompts and copied web responses. The reading packet should stay compact because it is generated from the proof-obligation graph rather than from the full transcript history.

## Quick Start

Smoke test the file layout without external API calls:

```powershell
python -m math_collab.orchestrator --config config/agents.example.json --problem problems/gauss_circle.md --rounds 1 --dry-run --run-id smoke --no-state-update
```

Validate the proof-obligation graph:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
```

Configure DeepSeek for the automatic A3 agent:

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
$env:DEEPSEEK_MODEL="deepseek-v4-pro"
```

Or copy `.env.example` to `.env`; the orchestrator loads `.env` automatically.

Generate or advance a mixed manual-web/API research round:

```powershell
python -m math_collab.orchestrator --config config/agents.web-test.json --problem problems/gauss_circle.md --run-id gauss-main --start-round 1 --rounds 1 --skip-missing-api
```

For the most automated routine, use the guided obligation runner. It validates the graph, opens the web agents, pastes prompts, waits while you copy model responses, saves and normalizes them, validates the judge patch, and advances Stage D:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId obligation-main -StartRound 1 -Rounds 1
```

Add `-SubmitPrompts` if you want the helper to press Enter after pasting prompts.

If you prefer to manually open ChatGPT/Gemini, paste prompts, copy responses, save files, and normalize Markdown yourself, use the watcher instead:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\watch_web_research_run.ps1 -RunId obligation-main -StartRound 1 -Rounds 1 -NoNormalize
```

The watcher still automates graph validation, barrier polling, orchestrator reruns, judge-patch validation, Stage D, and reading-packet regeneration.

For A1/A2 web agents, paste prompt files from:

```text
rounds/<run-id>/round_XXX/prompts/
```

Then save copied web responses under:

```text
handoff/<run-id>/round_XXX/responses/
handoff/<run-id>/round_XXX/reviews/
handoff/<run-id>/round_XXX/judge/
```

A3 responses and reviews are written automatically under `rounds/<run-id>/round_XXX/` when the API key is present. If the key is missing, the barrier waits with a pending API marker.

When a judge synthesis is ready, it must include a `## State Patch` section using JSON-compatible YAML. JSON is valid YAML, so this remains dependency-free even when PyYAML is not installed. Stage D validates the patch before mutating `state/proof_obligations.yml`.

For the manual web run procedure and clipboard helpers, see `docs/web-research-run.md`. For DeepSeek API setup, see `docs/api-setup.md`.

## Human Steering

Edit these files before the next stage or round:

- `human/current_directives.md`: active steering instructions for the next round.
- `human/goals.md`: current research and workflow goals.
- `human/ideas.md`: mathematical ideas to try.
- `human/references.md`: papers, links, theorem names, citations, or notes.
- `human/inbox/`: timestamped human notes.

You can also add a note from the command line:

```powershell
python -m math_collab.human --kind idea --title "Try a smoothed cutoff" --text "Ask all agents to compare sharp cutoff vs smooth cutoff before unsmoothing." --activate
```

Human direction is injected into reasoning, review, and judge prompts. Human instructions override prior AI suggestions when they change the target, reject a route, add a reference, or change success criteria.

## Important Practice

Every agent must separate:

- proved statements,
- plausible claims,
- gaps,
- counterexample attempts,
- dependencies,
- confidence.

The public repository is the durable memory; web conversation memory is useful but not authoritative. The proof-obligation graph is the durable mathematical memory; prose rounds explain and audit graph changes.
