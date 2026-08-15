# Task Brief: log_kernel_hostile_audit

- Campaign: `m9-m1-beta-log-amplitude-two-saddle`
- Research round: `30` (`beta_log_amplitude_two_saddle`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `23a3c1929047ab40a0a67d07a4de96a7943ce3b83a8beec35ff433d933038be2`
- Generated: `2026-08-12T23:21:02.811021+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact distribution-first beta kernel with its delta-plus-finite-section-PV logarithmic amplitude be estimated uniformly through both signed saddles, moving height faces, and saddle-face coalescence with only polylogarithmic loss, while retaining the accepted local q^(-2) power?

## Reference formula and distinctions

After the physical top limit in mu=L-nu, the exact section is pi*1_(|L|<V)H(L,L)-i PV int_([-V,V] intersect [L-U,L+U]) H(L,nu)/(L-nu)dnu. The phase has saddles alpha=plus or minus lambda, lambda=pi q sqrt(Xx)/D_j. Ordinary pointwise C2 fails at L=plus or minus V; a candidate moving-logarithm Fresnel estimate should lose at most log(2+lambda).

- abstract moving-logarithm oscillatory integral
- exact Morse coordinate and both Hessian signs
- delta trace and finite-section PV term
- saddle-face and saddle-endpoint coalescence
- polytope faces |nu|=V and |L-nu|=U
- scale-normalized variation of the complete recombined numerator
- local q^(-2) normalization
- height-tail and finite-side remainder

## Assigned target

Hostilely test the moving-logarithm Fresnel bound, delta/PV recombination, both saddle signs, coalescing saddle and polytope faces, derivative and variation hypotheses, q^(-2) normalization, and height exhaustion. Construct a sharp counterexample or certify the narrowest uniform lemma.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/reports/outside_v_hostile_audit.md`
- `rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/synthesis.md`

## Required controls

- `signed-vs-unsigned`
- `support-and-degeneracy`
- `residue-and-normalization`
- `endpoint-uniformity`
- `order-of-limits`
- `coefficient-adversary`

## Required deliverables

- Independent singular stationary and normalization audit
- Counterexample or scoped certification
- Seven-section report at the assigned path

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
