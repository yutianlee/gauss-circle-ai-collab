# Gauss Circle Proof Research

This repository is a claim-centered research workspace for the Gauss circle problem. `state/proof_obligations.yml` is the authoritative mathematical state; campaign reports, computations, and historical rounds are auditable evidence.

The active workflow uses one persistent Codex conductor and temporary, context-isolated subagents chosen for a specific mathematical interface. The conductor designs strategy, distributes objectives, monitors execution, closes each reasoning round, and defines the next one. The former A1/A2/A3/A4 web/API panel is retired. Its rounds and evidence paths are preserved as historical provenance.

## Target and current status

Let

```text
N(R) = #{(m,n) in Z^2 : m^2 + n^2 <= R^2}.
```

The conjectural error estimate is

```text
N(R) - pi R^2 = O_epsilon(R^(1/2+epsilon)).
```

Equivalently, in the repository's $X=R^2$ normalization,

```text
P(X) = N(sqrt(X)) - pi X <<_epsilon X^(1/4+epsilon).
```

The repository does not contain an unconditional proof of this target. The accepted reduction is conditional, and `M9`, especially its `M9-M2` pointwise bridge, remains the main bottleneck. See `state/best_proof_draft.md` for the proof assembled from accepted obligations and its explicit gaps.

## Active architecture

```text
Human objective
  -> Codex conductor
      -> frozen obligation and barrier packet
      -> temporary discovery / no-go / control workers
      -> smallest candidate proof kernel
      -> seam-specific reviewers and blind rederivation
      -> local computational falsification and source checks
  -> conductor round-closing synthesis
  -> validated State Patch
  -> proof graph and proof draft
```

Subagents are selected by function, not permanent identity. Reasoning proceeds in numbered rounds, with one campaign manifest per round. A round may use discovery, hostile obstruction, countermodel, source-audit, numerical-falsification, seam-review, blind-rederivation, or formalization tasks. There is no vote and no fixed response barrier. At most three subagents run concurrently, and they stop at the round interface chosen by the conductor.

The full rules are in `protocol.md` and `AGENTS.md`.

## Core files

```text
AGENTS.md                         conductor and subagent rules
protocol.md                       mathematical campaign protocol
problems/gauss_circle.md          problem statement
state/proof_obligations.yml       authoritative claim graph
state/project_summary.md          project, route, strategy, and progress summary
state/active_campaign.yml         current frozen campaign and briefs
state/current_round.md            generated active-round summary
state/round_ledger.yml            numbered round status and decisions
state/next_campaign.md            generated campaign summary
state/failure_ledger.md            generated rejected-claim memory
state/control_models.md            Gauss-specific proof-unit tests
state/validation_matrix.yml        claim-by-seam acceptance gates
state/best_proof_draft.md          proof assembled from accepted graph
manifests/reading_packet.md        compact generated project state
math_collab/campaigns.py           campaign validator and brief generator
math_collab/proof_obligations.py   graph validation and packet generation
proofs/kernels/                    isolated candidate proof kernels
rounds/codex-managed/              active campaign artifacts
rounds/obligation-main/            immutable legacy evidence
rounds/web-research-test/          immutable legacy evidence
```

## First campaign

The pilot campaign adjudicates the Round 9 count-versus-weighted-mass disagreement. It keeps separate:

1. the raw, weight-blind near-collision tuple count;
2. the Vaaler-$\beta$-weighted absolute mass;
3. the true signed mass carrying $\chi_4$;
4. the unsigned comparison quantity.

Its three orthogonal tasks are a statement-only upper-bound rederivation, a hostile lower-bound/missing-factor audit, and an exact finite diagnostic. Normalization, counting, coefficient summation, and endpoint uniformity are separate review seams. The campaign must not promote `M9`.

## Quick start

The bundled Codex Python runtime can be located through the desktop workspace dependencies. If `python` is already on `PATH`, run:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
python -m math_collab.campaigns validate
python -m math_collab.campaigns prepare
```

`prepare` creates the campaign directory, immutable plan snapshot, and minimal subagent briefs. It does not launch subagents and does not mutate the proof graph.

After work is complete:

```powershell
python -m unittest discover -s tests -v
python -m compileall -q math_collab tests
git diff --check
```

## Evidence and promotion discipline

- A report must give an exact lemma or no-go result, proof, first doubtful step, control test, dependencies, and recommended state effect.
- Computation is diagnostic and must be locally reproducible.
- External results require source cards and exact theorem-hypothesis checks.
- Review is by failure seam; at least one important claim receives a statement-only independent derivation.
- Only the conductor writes round synthesis, State Patches, or changes the accepted proof draft.
- Historical A1--A4 owner labels and artifact names remain provenance, not active assignments.

## Legacy workflow

`math_collab/orchestrator.py`, `config/agents*.json`, the manual web/clipboard scripts, `docs/api-setup.md`, `docs/web-research-run.md`, and `state/next_round_prompts.md` document the retired four-agent system. They are retained so old evidence remains interpretable; do not use them for new research campaigns.

## Human steering

Edit `human/current_directives.md`, `human/goals.md`, `human/ideas.md`, and `human/references.md`. Human instructions may change the target, completion rule, allowed sources, or controls. The conductor must record any such change in the active round before delegating work.
