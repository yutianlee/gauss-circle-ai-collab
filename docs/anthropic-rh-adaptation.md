# Anthropic Zeta Project: What This Repository Adopts

## Correction and scope

Anthropic did not announce a proof of the Riemann Hypothesis. Its August 10, 2026 result improves unconditional proportions of zeta zeros known to lie on the critical line, with related simplicity and distinctness bounds. Anthropic explicitly says the result has no bearing on RH in either direction and that it does not expect the techniques to prove RH.

Primary materials:

- [Anthropic announcement](https://www.anthropic.com/research/riemann-zeta)
- [Full paper](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)
- [Concise proof note](https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf)
- [Research-process appendix](https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf)
- [Annotated transcripts](https://www-cdn.anthropic.com/8a0d1add3c637b858a9a181e98c40e9548c3f44f.pdf)
- [Lean formalization](https://github.com/anthropics/zeta-23-lean)

The local evaluation that motivated this migration is `C:/Users/yutia/Downloads/RH-strategy.md`.

## Verified process lessons

Anthropic reports two Claude Code sessions, roughly 31 million output tokens, about 60 temporary subagents, around 2,400 shell commands, hundreds of Python scripts, thousands of numerical checks, a 54-paper literature search, independent rederivations, human mathematical review, and Lean formalization. Only two subagents are credited with the key ideas; many attempts failed or served validation. This was a coordinator-led, heavy-tailed search, not an agent vote.

The transferable unit is the proof interface:

$$
\text{local structural taxonomy}
+\text{global quantitative data}
+\text{a sharp bridge inequality}.
$$

For the zeta result, those modules were zero-side Hermitian-form structure, prime-side trace moments, and a finite-dimensional rank--trace inequality. For this project, the analogous question is whether M9-M2 admits a sign-sensitive finite operator, quadratic form, energy, or dual transform that connects existing resonance data to a pointwise bound. That is a research hypothesis, not evidence that such an object exists.

## Adopted workflow

- one persistent coordinator with temporary, isolated workers;
- briefs that state the obstruction, allowed inputs, controls, and first doubtful step;
- failures preserved as quantitative barrier results;
- countermodels treated as proof-unit tests;
- review assigned by seam rather than repeated holistic review;
- blind rederivation without claimant files;
- computation used aggressively for falsification but never certification;
- early formalization of stable finite kernels;
- literature and source checking before graph promotion;
- immutable provenance for every claim and review.

## Deliberate safeguards

We do not treat subagent count or agreement as independent validation. Same-model reviews are correlated. The coordinator must read decisive artifacts rather than only summaries. Human review and formalization complement, but do not replace, analytic verification and source checks. The authoritative proof state remains the repository graph, not coordinator memory.
