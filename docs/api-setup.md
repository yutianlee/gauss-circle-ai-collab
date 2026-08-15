# DeepSeek API Setup (Legacy)

> This document describes the retired fixed-agent/API workflow. New research uses Codex-managed subagent campaigns; see `protocol.md` and `docs/proof-obligation-workflow.md`.

This Gauss workflow has one API agent:

- `A3`: Deepseek V4 Pro

The web agents `A1`, `A2`, and `A4` still run manually through ChatGPT, Gemini/AI Studio, and Claude. A2 may also use Google AI Studio Code Execution for small self-contained Python diagnostics, but those outputs are copied manually and must be reproduced locally before they become repository diagnostic evidence.

## Configure Key

Create a local `.env` file from the template:

```powershell
Copy-Item .env.example .env
notepad .env
```

Fill in:

```text
DEEPSEEK_API_KEY=sk-...
```

`.env` is ignored by Git. The orchestrator loads it automatically and does not overwrite already-set environment variables.

You can also set the key only for the current PowerShell session:

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
$env:DEEPSEEK_MODEL="deepseek-v4-pro"
```

## Current API Settings

The active settings live in `config/agents.web-test.json`.

```json
{
  "endpoint": "https://api.deepseek.com/chat/completions",
  "default_model": "deepseek-v4-pro",
  "temperature": 0.1,
  "extra_payload": {
    "thinking": {"type": "enabled"},
    "reasoning_effort": "max",
    "max_tokens": 32768
  }
}
```

## Smoke Test A3

After adding the key:

```powershell
python -m math_collab.api_smoke --config config/agents.web-test.json --agents A3
```

Then generate or advance the mixed run:

```powershell
python -m math_collab.orchestrator --config config/agents.web-test.json --problem problems/gauss_circle.md --run-id gauss-main --start-round 1 --rounds 1 --skip-missing-api
```

What happens:

1. A1/A2/A4 web prompts are written under `rounds/gauss-main/round_001/prompts/`.
2. A3 is called automatically if `DEEPSEEK_API_KEY` is configured.
3. If the key is missing, a pending file is written and the round barrier waits.
4. After saving A1/A2/A4 web responses into `handoff/gauss-main/round_001/responses/`, rerun the same command to advance to reviews.

## A2 Code Execution Diagnostics

When a round assigns Python diagnostics, use A2 in Google AI Studio with Code Execution enabled if available. A2 must include:

- the exact Python code;
- the returned stdout/stderr or table output;
- model/tool settings relevant to execution;
- parameters and dyadic conventions;
- pass/fail criteria;
- limitations and `diagnostic_only` status.

If Code Execution is unavailable or no runtime output is returned, A2 must write `not_executed` and provide only a runnable artifact bundle. Codex or the local workflow should then run the script in this repository and archive the local command/output before the diagnostic is counted as evidence.
