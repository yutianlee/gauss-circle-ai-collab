# Proof-Obligation Workflow

This workflow makes mathematical claims, not transcripts, the unit of progress.

## Core Files

- `state/proof_obligations.yml`: authoritative claim graph.
- `manifests/reading_packet.md`: compact generated packet for agents.
- `state/next_round_prompts.md`: extracted judge prompts for A1, A2, and A3.
- `state/last_validation_report.md`: latest patch validation result.
- `sources/*.md`: source cards required before external theorem use.

## Round Flow

1. Select one primary track and at most one secondary track in `state/proof_obligations.yml`.
2. Stage A agents attack the selected target obligations.
3. Stage B agents review proposed graph mutations: creates, updates, rejections, dependencies, blockers, evidence, and no-change claims.
4. Stage C judge writes narrative synthesis plus `## State Patch`.
5. Stage D validates the patch, applies accepted graph changes, extracts next prompts, and regenerates the reading packet.

## Patch Rules

Use JSON-compatible YAML under `## State Patch`. JSON is valid YAML, and this keeps the validator dependency-free when PyYAML is unavailable.

```json
{
  "proof_obligations": {
    "create": [],
    "update": [
      {
        "id": "M9-M2-character-factor",
        "status": "open",
        "evidence_added": {
          "inconclusive": ["rounds/web-research-test/round_029/responses/A2-029.md"]
        },
        "next_action": "State the exact near-collision lemma with C_h retained."
      }
    ],
    "reject": [],
    "no_change": [
      {
        "id": "M9",
        "reason": "No theorem-level proof of both M1 and M2 with endpoint uniformity."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 1,
    "reason": "A blocker was sharpened; no theorem was promoted."
  }
}
```

## Validation Commands

Run the guided workflow with minimal file handling:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId obligation-main -StartRound 1 -Rounds 1
```

The helper automates graph validation, orchestrator reruns, prompt pasting, response saving, Markdown normalization, judge-patch validation, and reading-packet regeneration. You still need to wait for A1/A2 in their web UIs and click Copy response when each answer is done.

Validate the graph:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
```

Validate a judge output before applying it:

```powershell
python -m math_collab.validate_round rounds/web-research-test/round_029/judge/judge-029.md
```

Apply a validated judge patch:

```powershell
python -m math_collab.validate_round rounds/web-research-test/round_029/judge/judge-029.md --apply --round-index 29
```

Normal orchestrator Stage D applies the same validation automatically when `--no-state-update` is not set.

## Safety Rules

- Computation can only add diagnostic evidence.
- External theorem obligations need source cards.
- Open or proposed obligations need owners and concrete next actions.
- `M9` cannot be promoted unless both `M9-M1` and `M9-M2` are promoted and uniformity over active dyadic `D` is explicit.
- A round with no valid graph change may still be useful as evidence, but it should receive a low progress score.
