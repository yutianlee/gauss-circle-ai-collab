# Multi-AI Math Research Orchestrator

This repo is designed to use a public GitHub repository as the shared memory for a multi-AI mathematics research workflow.

The intended setup is:

- **GPT Pro Thinking** and **Gemini Deep Think** through their web interfaces.
- **Qwen** and **DeepSeek** through OpenAI-compatible APIs.
- **GitHub** as the permanent, public research log: every round is committed and pushed.

The first target problem in this repo is the Gauss circle problem.

## Core Idea

Each round follows a fixed protocol:

1. Every AI produces an independent strategy or reasoning attempt.
2. Every AI reviews the other agents' outputs.
3. A judge agent summarizes the useful parts, gaps, and next direction.
4. The repo state is updated:
   - `state/current_state.md`
   - `state/lemma_bank.md`
   - `state/gap_register.md`
   - `state/best_proof_draft.md`
   - `manifests/reading_packet.md`
5. The round is committed and pushed to GitHub.
6. The next round gives each AI only the compact reading packet plus selected prior outputs, not the whole repo.

This keeps the public repo complete while keeping each AI's working context small.

Rounds are synchronized by default. The orchestrator will not start reviews until all four reasoning responses are present, will not start judging until all four reviews are present, and will not update state until judge synthesis is complete.

## Repo Layout

```text
problems/
  gauss_circle.md
protocol.md
config/
  agents.example.json
math_collab/
  orchestrator.py
state/
  current_state.md
  lemma_bank.md
  gap_register.md
  best_proof_draft.md
human/
  current_directives.md
  goals.md
  ideas.md
  references.md
  inbox/
manifests/
  reading_packet.md
rounds/
  round_001/
    prompts/
    responses/
    reviews/
    judge/
handoff/
  ...
```

`rounds/` is the public archive. `handoff/` is ignored because it contains temporary web prompts and local copy-paste files.

## Human Intervention

Human intervention is first-class. Edit these files any time before starting the next round:

- `human/current_directives.md`: active steering instructions for the next round.
- `human/goals.md`: current research and workflow goals.
- `human/ideas.md`: new mathematical ideas to try.
- `human/references.md`: papers, links, theorem names, citations, or notes.
- `human/inbox/`: timestamped human notes.

You can also add a note from the command line:

```powershell
python -m math_collab.human --kind idea --title "Try a smoothed cutoff" --text "Ask all agents to compare sharp cutoff vs smooth cutoff before unsmoothing." --activate
```

The orchestrator injects these human files into every reasoning, review, and judge prompt. Human direction is treated as stronger than prior AI suggestions.

## Quick Start

Run a smoke test without calling any external API:

```powershell
python -m math_collab.orchestrator --config config/agents.example.json --problem problems/gauss_circle.md --rounds 1 --dry-run --run-id smoke
```

Run a real round, generating prompts for web agents and calling API agents when keys are present:

```powershell
$env:QWEN_API_KEY="..."
$env:DEEPSEEK_API_KEY="..."
python -m math_collab.orchestrator --config config/agents.example.json --problem problems/gauss_circle.md --rounds 1 --run-id gauss-001
```

For GPT/Gemini web agents, the orchestrator writes prompt files under:

```text
handoff/<run-id>/round_001/
```

Paste those prompts into the web UI, then save the responses back to the response files named by the script. The next version can add Playwright automation on top of the same handoff interface.

If you want to test only prompt generation before setting API keys:

```powershell
python -m math_collab.orchestrator --config config/agents.example.json --problem problems/gauss_circle.md --run-id handoff-test --rounds 1 --skip-missing-api --no-state-update
```

In normal research mode, rerun the same command after adding web responses. The round advances only when every agent has completed the current stage.

For browser smoke tests, use compact prompts so the web UI does not choke on large prior-round context:

```powershell
python -m math_collab.orchestrator --config config/agents.web-test.json --problem problems/gauss_circle.md --run-id web-smoke --rounds 1 --compact-prompts
```

When copying responses from web UIs, prefer the page's own **Copy response** button. The prompts require Markdown math as `$...$` and `$$...$$`, because some web copy paths turn `\[...\]` into bare `[ ... ]`. If a copied ChatGPT response still contains bare display math, normalize it before committing:

```powershell
python -m math_collab.normalize_markdown rounds/web-smoke/round_001/responses/gpt_pro_thinking.md
```

For the long-thinking web research workflow, see `docs/web-research-run.md`.

To keep a three-round web research run moving while ChatGPT/Gemini think, use:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\watch_web_research_run.ps1 -RunId web-research-test -StartRound 1 -Rounds 3
```

## Publishing as a Public GitHub Repo

This directory is currently safe to turn into its own repo:

```powershell
git init -b main
git add .
git commit -m "Initialize multi-AI math research workflow"
```

Then create a public GitHub repo in the browser and connect it:

```powershell
git remote add origin https://github.com/<your-user>/<repo-name>.git
git push -u origin main
```

After that, each research round can be committed and pushed:

```powershell
git add protocol.md problems state manifests human rounds config math_collab .github README.md .gitignore
git commit -m "Add research round 001"
git push
```

## API Configuration

Copy `config/agents.example.json` to `config/agents.local.json` and edit model names or endpoints if needed.

API keys are read from environment variables only:

- `QWEN_API_KEY`
- `DEEPSEEK_API_KEY`

Do not commit secrets.

## Important Practice

The workflow should force every AI to separate:

- proven statements,
- plausible claims,
- gaps,
- counterexample attempts,
- dependencies,
- confidence.

This is more important than simply making the agents write long answers.
