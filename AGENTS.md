# Codex Research Protocol

This repository uses one persistent Codex conductor and temporary, task-specific subagents. The old A1/A2/A3/A4 panel is retired; its files remain historical evidence only. Reasoning proceeds in explicitly numbered rounds.

Before research work, read `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, and the exact context files named by the active task.

## Coordinator rules

- Act as the conductor: design the round strategy, select one objective, distribute bounded tasks, monitor subagents, intervene when scope or evidence drifts, and decide when the round closes.
- Own the authoritative graph, round plan, synthesis, and State Patch.
- Do not let subagents start the next round. Close and assess the current round before designing its successor.
- Decompose by mathematical interface before delegating. Use at most three concurrent subagents.
- Use descriptive task names and functional roles; do not recreate permanent agent identities.
- Give each subagent the minimum context listed in its brief. Preserve statement-only isolation where specified.
- Do not decide claims by vote. Promote only after the required proof, seam reviews, controls, source checks, and graph validation exist.
- Treat a rigorous no-go result as useful progress.
- Reproduce important computations locally. Computation can falsify or diagnose, but cannot certify an asymptotic theorem.
- Enforce an 80/20 effort allocation: at least 80% analytical/algebraic reasoning and at most 20% numerical experimentation. Use Python or Mathematica only for bounded symbolic, pattern-finding, or falsification work.
- Use web literature for strategy and method review when relevant. Preserve exact citations and audit theorem hypotheses before relying on a source.
- Keep `rounds/obligation-main/` and `rounds/web-research-test/` immutable as legacy evidence.

## Round discipline

Each round has one index, one frozen objective, a resource budget, one to three orthogonal tasks, explicit exit gates, and a conductor decision. A subagent stops after its assigned report. The conductor monitors live progress and may narrow, redirect, or terminate a task. The next round is designed only from the closed round's artifacts and graph state; no result is silently carried forward.

## Subagent output contract

Every research report must contain:

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect: promote, retain, revise, reject, or no change.

Subagents must not edit `state/proof_obligations.yml`, `state/best_proof_draft.md`, validation matrices, or synthesis files. Write only to the task-specific paths assigned by the coordinator.

## Proof-state rule

The claim graph is authoritative. Candidate reports and computations are evidence, not accepted mathematics. The proof draft is updated only after a mechanically valid State Patch changes the accepted graph.
