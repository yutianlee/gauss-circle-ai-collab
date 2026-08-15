# Gauss Circle Research Protocol

## 1. Authority and scope

`state/proof_obligations.yml` is the authoritative mathematical state. Reports, computations, and historical rounds are evidence for graph decisions; none of them becomes accepted mathematics merely by being written.

The active execution model is a persistent Codex conductor with temporary, context-isolated subagents. The former fixed A1/A2/A3/A4 panel and its all-agent round barriers are retired and retained only for provenance. Reasoning proceeds round by round; one campaign manifest defines one numbered reasoning round.

The target remains conditional until every dependency is closed:

$$
P(X)=N(\sqrt X)-\pi X\ll_\varepsilon X^{1/4+\varepsilon}.
$$

## 2. Mathematical interfaces

Research is divided at proof interfaces, not by permanent personalities:

1. exact H1--H4 reduction and coefficient conventions;
2. Fejer residual and R5;
3. the M9-M1 kernel;
4. the M9-M2 configuration side;
5. the M9-M2 global estimate;
6. the pointwise bridge and endpoint uniformity;
7. final conditional assembly.

A campaign freezes one exact interface, statement, and completion rule. Subagents receive only the files needed for that interface.

## 3. Campaign stages

### Conductor and round boundaries

The conductor owns strategy, task decomposition, monitoring, interventions, synthesis, and proof-state decisions. Subagents solve bounded objectives; they do not choose the program's next objective or advance themselves to a new round.

Every reasoning round records:

- round index and type;
- one frozen mathematical objective;
- inherited accepted state and barriers;
- analytical/numerical resource allocation;
- one to three orthogonal subagent tasks;
- required artifacts and exit gates;
- live status and conductor interventions;
- closing assessment and proposed next round.

The conductor closes a round only after its required reports exist or a task is explicitly terminated. A new round is then designed from the closed artifacts. Discovery, hostile review, seam review, blind rederivation, formalization, and synthesis may therefore occupy different rounds; there is no automatic all-purpose round template.

### A. Design and freeze the round

Record the obligation IDs, exact quantities and normalizations, allowed dependencies, forbidden shortcuts, endpoint range, and promotion criteria in `state/active_campaign.yml`.

### B. Build the barrier packet

Extract relevant rejected claims and known obstructions into `state/failure_ledger.md`. A new mechanism must state exactly which earlier obstruction it bypasses.

### C. Launch orthogonal work

The coordinator may run up to three concurrent subagents. Typical functions are discovery, hostile obstruction search, countermodel construction, source audit, numerical falsification, seam review, blind rederivation, and formalization. The mix is selected per obligation; there is no fixed roster.

Every brief requires:

$$
\boxed{\text{lemma or no-go result}+\text{proof}+\text{first doubtful step}+\text{control test}.}
$$

A subagent may refute the proposed route. A precise no-go theorem is a successful result.

### D. Select the smallest proof kernel

The coordinator selects the narrowest candidate that could change the graph. Do not synthesize a full proof from mutually incompatible candidates or from a majority vote.

### E. Validate by seam

Reviews are routed around the claimant and assigned to distinct seams, such as:

- definitions and normalization;
- coefficient or character algebra;
- counting and multiplicity;
- summation and exponent bookkeeping;
- endpoint uniformity;
- source hypotheses;
- implication into downstream obligations.

At least one important lemma must receive a statement-only independent rederivation. A reviewer does not inherit the claimant's derivation unless the task explicitly requires a line audit.

### F. Falsify computationally

Run exact, extremal, degenerate, random-sign, and adversarial controls where useful. Archive code, command, parameters, output, precision notes, pass/fail rule, and limitations. Computation is always `diagnostic_only`; it can reject a claim but cannot prove an asymptotic theorem.

Apply an 80/20 allocation across each campaign: at least 80% of effort is analytical or algebraic reasoning, and at most 20% is numerical experimentation. Numerical examples may expose a pattern and motivate a conjecture or lemma, or produce a counterexample that falsifies one. Python and Mathematica are available on Windows for bounded symbolic and diagnostic work.

Web literature searches are permitted and expected when they can sharpen strategy or method selection. Cite the exact source, distinguish a structural analogy from theorem applicability, and audit every imported theorem's hypotheses before graph promotion.

### G. Formalize the finite kernel early

Once a finite algebraic or combinatorial kernel is stable, isolate it under `proofs/kernels/` and consider formalization before investing in the analytic shell. Formalization complements source and analytic review; it does not replace them.

### H. Close the round, synthesize, and patch state

Only the conductor writes the round-closing synthesis and a State Patch. Apply it only after graph validation and after all required entries in `state/validation_matrix.yml` are green. Update `state/best_proof_draft.md` only from the accepted graph. Record the closing decision in the round ledger before opening the next round.

## 4. Artifact layout

Active campaign artifacts live under:

```text
rounds/codex-managed/<campaign-id>/
  plan.json
  briefs/
  reports/
  candidates/
  reviews/
  controls/
  synthesis.md
  state_patch.json
```

Each artifact records the campaign and task ID, graph hash, generated time, exact context files, role, dependencies, and claimant/reviewer/blind status. Historical A1--A4 names inside old paths remain valid provenance but are not current assignments.

## 5. Promotion rules

- Do not promote a claim without an exact statement, proof, dependencies, evidence, and remaining caveats.
- External theorems require completed source cards and exact hypothesis matching.
- `M9` remains open unless M9-M1 and M9-M2, including endpoint uniformity, are proved.
- Signed and unsigned quantities, exact and near resonances, and raw counts and coefficient-weighted masses are separate objects until an explicit lemma connects them.
- Known false controls must be addressed. For M9 work, explain which property of the Vaaler coefficients or $\chi_4$ prevents the argument from proving the false unsigned or adversarial analogue.
- A failed campaign may add an obstruction or rejected claim without promoting the target.

## 6. State ownership

Subagents do not edit the proof graph, proof draft, validation matrix, or shared synthesis. The coordinator owns those files and validates every mutation. Temporary task IDs belong in campaign artifacts, not in durable obligation ownership fields.

## 7. Legacy policy

The following remain readable but are not active workflow instructions: the old web/API orchestrator, manual clipboard scripts, model configuration files, `state/next_round_prompts.md`, and historical rounds. Do not complete the unfinished Round 9 four-agent barrier. Import any useful candidate into a new Codex-managed campaign and validate it under this protocol.
