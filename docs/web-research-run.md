# Web Research Run Procedure

Use this procedure when ChatGPT or Gemini web automation is unreliable, or when the goal is maximum-quality reasoning with long model thinking time.

## Required Web Modes

- ChatGPT: `Extended Pro`
- Gemini: `Pro Deep Think`

Use one persistent conversation per AI for the whole run.

## Research-Mode Rule

This is not a smoke test. Let each model think as long as it needs. Prefer correctness, explicit hypotheses, gap detection, and precise lemma statements over short answers.

All copied responses should be Markdown source. Use each web UI's own **Copy response** button.

## Round Barrier

Do not start the next stage until every file required by the current stage has a real response.

For the two-web-agent test:

1. Stage A requires:
   - `handoff/<run-id>/round_XXX/responses/gpt_pro_thinking.md`
   - `handoff/<run-id>/round_XXX/responses/gemini_deep_think.md`
2. Stage B requires:
   - `handoff/<run-id>/round_XXX/reviews/gpt_pro_thinking.md`
   - `handoff/<run-id>/round_XXX/reviews/gemini_deep_think.md`
3. Stage C requires:
   - `handoff/<run-id>/round_XXX/judge/judge.md`

After each stage is filled, rerun the orchestrator command for that same round. It will advance only when the barrier is satisfied.

## Commands

Generate or advance a research-mode round:

```powershell
python -m math_collab.orchestrator --config config/agents.web-test.json --problem problems/gauss_circle.md --run-id web-research-test --start-round 1 --rounds 1
```

If `python` is not on PATH in Codex Desktop, use the bundled Python:

```powershell
& 'C:\Users\yutia\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m math_collab.orchestrator --config config/agents.web-test.json --problem problems/gauss_circle.md --run-id web-research-test --start-round 1 --rounds 1
```

Or leave the watcher running while the web models think:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\watch_web_research_run.ps1 -RunId web-research-test -StartRound 1 -Rounds 3 -PollSeconds 30
```

The watcher will:

- print the prompt files to paste,
- wait until the required Copy-response Markdown files are saved,
- normalize copied Markdown,
- advance the orchestrator through reasoning, review, judge, and the next round.

Normalize copied Markdown after saving GPT responses:

```powershell
python -m math_collab.normalize_markdown handoff/web-research-test/round_001/responses/gpt_pro_thinking.md
```

## Prompt Files

For each stage, paste the corresponding prompt file into the correct web conversation.

Reasoning:

```text
rounds/<run-id>/round_XXX/prompts/gpt_pro_thinking_reasoning.md
rounds/<run-id>/round_XXX/prompts/gemini_deep_think_reasoning.md
```

Review:

```text
rounds/<run-id>/round_XXX/prompts/gpt_pro_thinking_review.md
rounds/<run-id>/round_XXX/prompts/gemini_deep_think_review.md
```

Judge:

```text
rounds/<run-id>/round_XXX/prompts/judge.md
```

The default judge for `config/agents.web-test.json` is ChatGPT.
