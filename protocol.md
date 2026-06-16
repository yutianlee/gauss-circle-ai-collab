# Multi-AI Mathematical Research Protocol

## Agents

The default Gauss circle panel has exactly three active agents:

1. `A1`: ChatGPT Extended Pro through the web UI. Broad strategist, literature scout, synthesis writer, and default judge.
2. `A2`: Gemini Pro Deep Think through the web UI. Independent alternative strategist, obstruction finder, and conservative referee.
3. `A3`: Deepseek V4 Pro through the API. Automatic proof auditor, algebra checker, exponential-sum normalization checker, and stress-test planner.

Do not mention, score, or assign tasks to `A4`, Qwen, or any inactive KKT agent. Older state text may contain historical agent IDs such as `gpt_pro_thinking`, `gemini_deep_think`, or `deepseek_api`; treat them as aliases for A1, A2, and A3 only when reconstructing prior contributions.

## Round Structure

Rounds use strict barrier synchronization:

- Stage B cannot begin until A1, A2, and A3 have completed Stage A.
- Stage C cannot begin until A1, A2, and A3 have completed Stage B.
- Stage D cannot begin until the A1 judge synthesis is complete.
- The next round cannot begin until Stage D has updated the compact repo state.

### Stage A: Independent Reasoning

Each agent receives:

- the problem statement,
- the current reading packet,
- the current lemma bank,
- the current gap register,
- the prior judge decision if available,
- the agent-specific judge prompt if available,
- the human steering bundle,
- the agent-specific task.

The agent must output:

```text
## Summary
## Main claim or direction
## Detailed reasoning
## Theorem-dependency audit
## Hidden assumptions and potential gaps
## Counterexample or obstruction search
## Verification
## Divergent alternatives and 20% exploration
## Useful lemmas
## What should be tested next
## Confidence
```

### Stage B: Cross Review

Each agent reviews all other active agents' Stage A outputs.

The review must output:

```text
## Most valuable input from others
## Claims that look correct
## Claims that need proof
## Possible errors or hidden assumptions
## Suggested synthesis
## Research strategy
## Verification
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
## Next-round prompts by agent
### For A1
### For A2
### For A3
## Confidence
```

The `For A1`, `For A2`, and `For A3` blocks are important: the orchestrator extracts them and injects the matching block into the next round's Stage A prompt.

### Stage D: State Update

The orchestrator updates:

- `state/current_state.md`: compact current research state.
- `state/lemma_bank.md`: proposed, proved, and rejected lemmas.
- `state/gap_register.md`: known gaps and possible failure points.
- `state/best_proof_draft.md`: best current proof skeleton.
- `manifests/reading_packet.md`: compact packet for the next round.

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
