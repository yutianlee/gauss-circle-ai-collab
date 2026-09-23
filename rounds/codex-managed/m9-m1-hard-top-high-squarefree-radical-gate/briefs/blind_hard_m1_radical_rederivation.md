# Task Brief: blind_hard_m1_radical_rederivation

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Research round: `181` (`m9_m1_hard_top_high_squarefree_radical_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Generated: `2026-08-27T08:01:37.561951+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete literal high-squarefree-radical part of every residual hard-M1 product cone be bounded by L^(3/2) X^epsilon, closing the hard direct-M1 parent after the low-radical sector is paid, or does the first genuinely new actual-direction contraction self-return or retain L^2 capacity?

## Reference formula and distinctions

|sum_(s>L, mu^2(s)=1) sum_(t>=1) C_(L,X)(s t^2) e(t sqrt(Xs))| <<_epsilon L^(3/2) X^epsilon, where C_(L,X)(r)=sum_(h|r, h asymp L, r/h odd, 4h<r/h<16h) chi_4(r/h) a_(L,X)^lit(h,r/h).

- The exact hard cone is T_L^M1=sum_(h asymp L)sum_(4h<n<16h,n odd)chi_4(n)a_(L,X)^lit(h,n)e(sqrt(Xhn)).
- The symbol retains Phi(h/(H+1)), W(sqrt(4q_X h/n)), normalized powers, the dyadic shell, strict cone edges, floors, stars, both frequency signs, hard sample, real-X support crossings, and zero extensions.
- Write every product uniquely as r=s t^2 with mu^2(s)=1; literal support gives s<<L^2 and t<<L/sqrt(s).
- The proposed low-radical sector s<=L is target-safe by O(1+L/sqrt(s)) square multipliers and divisor-incidence multiplicity.
- High-radical coefficient-insensitive capacity is L^2 X^epsilon against target L^(3/2) X^epsilon, leaving L^(1/2)=X^(1/12) at L asymp X^(1/6).
- The t=1 high-radical face is mandatory; no gain may come only from averaging square multipliers.
- BAL, UNBAL, smooth M1, GAR, M2, assembly, bridges, and exponent claims are forbidden pivots.

## Assigned target

From the isolated finite packet, derive the squarefree split, low-sector incidence bound, high-sector capacity and false controls, and the first structural relation required for the proposed fixed-direction saving.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all prior round artifacts`
- `all sibling reports, reviews, controls, candidates, syntheses, sources, and conductor analysis`

## Required controls

- `exact_product_fibre_identity`
- `unique_squarefree_kernel_decomposition`
- `literal_product_support`
- `low_radical_incidence_bound`
- `high_radical_capacity_ledger`
- `fixed_t_power_summation`
- `perfect_square_centre_control`
- `high_radical_t1_control`
- `complex_dechirped_control`
- `arbitrary_coefficient_control`
- `character_erasure_control`
- `one_site_one_fibre_controls`
- `literal_unknown_quarantine`
- `downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section statement-only report satisfying the repository report contract.
- An independent exact derivation, capacity calculation, false controls, and first missing structural relation.
- Write only the assigned report and make no graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
