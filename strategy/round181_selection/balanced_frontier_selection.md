# Round 181 BAL frontier design selection

- Role: balanced-frontier design audit; no proof attempt
- Authoritative starting graph:
  `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Allocation: 100% analytic, algebraic, and graph review; 0% numerical
- Recommended selection effect: **do not select BAL for Round 181 unless the
  conductor deliberately chooses a high-risk nonlocal-theorem probe**

## 1. Result

The BAL frontier has two independent open scopes:

1. the persistent critical \(j=1\), \(L\asymp K\asymp X^{1/6}\)
   double-far oscillatory remainder; and
2. the remaining-label/quantifier owner, including noncritical persistent
   \(j=1\) scales and the isolated exact-square \(j=2\), \(K/L=16\)
   boundary.

The second is not a substitute for the first and has no single accepted
capacity or common analytic mechanism. The first has an exact literal
formula and a sharp factor-\(L\) deficit, but Round 171 exhausted the current
local commutator, independent-swap, and coefficient-independent Abel
mechanisms. Merely renaming the original remainder as a “correlation
theorem” would violate the Round-181 requirement for a genuinely new
inequality.

The smallest exact BAL statement still outside all accepted no-go scopes is
the following maximal signed two-variable prefix theorem. It is the **best
available BAL reopening gate**, but it is a strict strengthening of the open
remainder and no owner-saving proof mechanism is presently instantiated.
That is a rigorous strategic reason not to select BAL over a frontier that
has a genuinely new concrete transform or arithmetic interface.

## 2. Best exact BAL reopening gate

Fix one persistent critical \(j=1\) literal balanced block \(B\), with
\(L\asymp K\asymp X^{1/6}\), \(R=\sqrt X\), and

\[
 a_B(h,k)=\chi _4(h)
 \eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k),
\]

zero-extended off its exact positive literal support. Write

\[
 h'=h+2s,\qquad k'=k+q,
\]

\[
 \Delta=(h+2s)(k+q)-hk,
 \qquad
 \rho=h(k+q)-(h+2s)k,
\]

and define the complete zero-subtracted atom

\[
 \begin{aligned}
 F_B(h,k,s,q):={}&a_B(h,k)a_B(h+2s,k+q)
 \mathbf 1_{|\Delta|>L}\mathbf 1_{|\rho|>L}\\
 &\times\left[
 e\!\left(R\{\sqrt{hk}-\sqrt{(h+2s)(k+q)}\}\right)-1
 \right].
 \end{aligned}
 \tag{181.B1}
\]

The individual character product is retained: on live support it equals
\(\chi _4(h)\chi _4(h+2s)=(-1)^s\). In (181.B1) it is already contained
in the two factors \(a_B\); it must not be inserted a second time.

Because of zero extension, for arbitrary real cut points \(S,Q\) the
rectangular prefix

\[
 \mathcal P_B(S,Q)
 :=\sum_{s\le S}\sum_{q\le Q}\sum_{h,k}F_B(h,k,s,q)
 \tag{181.B2}
\]

is finite and has no convention-dependent endpoint. The candidate theorem
is

\[
 \boxed{
 \sup_{S,Q\in\mathbb R}|\mathcal P_B(S,Q)|
 \ll_\varepsilon L^3X^\varepsilon .}
 \tag{181.B3}
\]

At terminal cut points, (181.B2) is exactly
\(\mathcal R_B^{\rm osc}\). Thus (181.B3) implies

\[
 |\mathcal R_B^{\rm osc}|\ll_\varepsilon L^3X^\varepsilon,
\]

then the equivalent critical actual energy and fixed-block packet estimate,
after the already proved phase-free and corridor seams. It does **not**
imply the remaining-label owner or full BAL.

The maximal prefixes are not asserted to be necessary. They are proposed
because they are the narrowest explicit nonlocal object that simultaneously
tests all signed \((s,q)\) recombinations and all truncated support/gate
faces before a positive norm. A Round-181 BAL campaign would have to prove
that (181.B3) has a mechanism beyond the terminal instance; if the first
derivation shows it is only a tautological repackaging of the terminal
target, the campaign should close with that no-go rather than continue.

## 3. Dependencies and literal retained fields

### Mathematical dependencies

- `M9-M2-balanced-smooth-literal-atom-dictionary` supplies \(A_B\), exact
  block labels, floors, clipping, stars, support crossings, and zero
  extension.
- `M9-M2-character-factor` supplies the actual \(\chi _4\) normalization.
- `M9-M2-balanced-full-product-double-corridor-reduction` pays the true
  product diagonal and the \(|\Delta|\le L\), \(|\rho|\le L\) corridors.
- `M9-M2-balanced-double-far-phase-free-mode-reduction` pays the complete
  assembled phase-free mode and licenses the zero subtraction in
  (181.B1).

### Binding no-repeat dependencies

- `M9-M2-balanced-divisor-progressive-alias-reduction`;
- `M9-M2-balanced-one-alias-reciprocal-self-return-obstruction`;
- `M9-M2-balanced-alias-character-restoration`;
- `M9-M2-balanced-broad-narrow-gauge-ruling-obstruction`; and
- `M9-M2-balanced-two-defect-commutator-ramp-obstruction`.

The theorem must retain, inside one joint scalar and before any modulus:

- both literal atoms and hence both low-gcd weights;
- both slanted continuum symbols with the exact Vaaler taper;
- \(\chi _4(h)\chi _4(h+2s)=(-1)^s\), including its constancy on a
  fixed-\(s\) fibre;
- both strict far gates, negative and positive shifts, the true axes, and
  every fixed-\(Q\) ruling;
- the real centre \(R=\sqrt X\) and the zero-subtracted square-root phase;
- all floors, stars, clipped profiles, births, deaths, support crossings,
  endpoints, and full zero extension; and
- if the divisor-progressive chart is opened, every \((d,\mu,J)\) lift,
  progression, residue, amplitude, gate, and endpoint. Equal-rational lifts
  have a coherent carrier but distinct literal amplitudes and may not be
  merged.

Only the single outer supremum/absolute value in (181.B3) is allowed.

## 4. Capacity and missing-power ledger

For the critical fixed block:

| object | accepted coefficient-insensitive capacity | required target | deficit |
|---|---:|---:|---:|
| packet scalar | \(L^2X^\varepsilon\) | \(L^{3/2}X^\varepsilon\) | \(L^{1/2}=X^{1/12}\) |
| complete double-far energy | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) | \(L\) |
| terminal instance of (181.B3) | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) | \(L\) |
| axes, width-\(L\) corridors, phase-free mode | \(L^3X^\varepsilon\) | \(L^3X^\varepsilon\) | none |
| surviving endpoint-swap \((++)\) complement | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) | \(L\) |
| one-step faces after the forced coefficient-blind \(q\)-ramp | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) | \(L\) |

Every \(L^4\) entry is an upper/adversarial capacity, not literal lower
mass. For the remaining-label owner there is no one uniform accepted
capacity theorem: the current scalar envelope loses

\[
 \min\!\left(L^{1/2},\frac{R^{1/2}}L\right),
\]

with maximum \(X^{1/12}\) at \(L=X^{1/6}\). The isolated exact-square
\(j=2\) boundary and noncritical \(j=1\) ranges require their own uniform
restoration. Therefore the remaining-label node is a multi-regime owner
completion, not a smaller single Round-181 inequality.

## 5. No-repeat barriers

A BAL round must stop if it reduces to any of the following accepted
barriers.

1. Fixed-\((\Delta,\rho)\) divisor multiplicity: summing the full defect
   range restores \(L^4\).
2. Product-fibre oscillation: the phase is constant on fixed product
   fibres, so determinant separation alone supplies no cancellation.
3. Fixed-\(s\) character cancellation: \((-1)^s\) is constant on that
   fibre.
4. A full-symbol or row Gram followed by positivity: this either erases the
   character or returns to a stronger positive mean square.
5. Short Fejer localization: owner amplification restores the missing
   factor unless almost the full \(L^2\) shift range is retained.
6. Aliaswise triangle, reciprocal spacing alone, a coefficient-blind large
   sieve, or a second one-variable B-process: these have \(L^5/L^4\)
   capacity or exactly self-return.
7. Equal-rational lift cancellation: the character carrier is coherent
   across lifts; only the amplitudes differ.
8. Raw determinant or broad--narrow curvature: the normal geometry is
   gauge-dependent, and strict double-far fixed-\(Q\) rulings survive.
9. The four canonical local multiplier/difference commutators: after
   normalization they are translations; the nonzero affine commutators
   divide back to shift tautologies.
10. Independent endpoint swaps: reality leaves the \((++)\) complement at
    \(L^4\) capacity.
11. Coefficient-independent two-step Abel summation: every \(q\)-primitive
    for constant weight on a length-\(L\) fibre has height at least
    \(L/2\), amplifying target-scale faces to \(L^4\).
12. Any rowwise, shiftwise, rulingwise, aliaswise, divisorwise, or shellwise
    modulus before the complete signed scalar.
13. Any use of the critical child to infer the all-label BAL parent without
    separately proving `M9-M2-balanced-remaining-label-owner-quantifier-completion`.

## 6. Expected mechanism and its current defect

The only graph-unexcluded mechanism is an owner-preserving **signed
two-parameter discrepancy/vector correlation theorem** for (181.B2). It
would have to combine the \(s\)-alternation, both actual gcd weights, the
slanted-symbol variation, and the square-root phase across the complete
\((s,q)\) family before taking a norm. If the divisor-progressive form is
used, it must act on the full lift vector and fixed-\(Q\) families jointly,
not scalarize them and sum nuclear norms.

Such a theorem must visibly fail for:

- arbitrary phase-adapted bounded coefficients;
- the constant-character shadow;
- erased gcd or erased slanted-symbol arrays; and
- a rulingwise positive model.

No accepted kernel or audited source currently supplies this vector
inequality. In particular, “apply a two-dimensional large sieve” is not a
mechanism until the exact literal matrix, its norm, its prefix operator, and
the restored \(L\)-saving are exhibited. This absence is the decisive
selection defect.

## 7. Three orthogonal tasks if BAL is nevertheless selected

### Task A: literal maximal-prefix connector and non-tautology audit

Starting only from the dictionary, corridor theorem, and phase-free theorem,
derive (181.B1)--(181.B3) independently, including the exact finite prefix
domain, axes, negative shifts, zero extension, and endpoint conventions.
Determine whether a two-dimensional Abel/variation connector makes the
maximal theorem structurally stronger in a useful way, or whether every
proposed reduction simply evaluates the terminal prefix. Stop with a
rigorous self-return result if it is tautological.

### Task B: complete actual-symbol vector-correlation attack

Attempt one nonlocal proof before any positive norm. Preserve the primal
\((h,k,s,q)\) scalar or open the full \((h,k,k',d,\mu,J)\) carrier only if
all lifts remain a single vector. The deliverable must be either a proved
prefix bound with a complete \(L^4\to L^3\) ledger, or the first exact seam
where scalarization, fixed-\(Q\) rank, endpoint variation, or lift coherence
restores the missing \(L\).

### Task C: hostile capacity, false-control, and owner-scope review

Independently test fixed-\(s\) character constancy, both axes, fixed-\(Q\)
rulings, the \((++)\) complement, all ramp-weighted faces, phase-adapted and
constant-character arrays, and the exact-square \(j=2\) quarantine. Verify
that any success closes only the persistent-critical child and that no
remaining-label, full-BAL, parent, bridge, or exponent claim follows.

These tasks are mutually separated as connector algebra, proof mechanism,
and hostile falsification. None may pivot to the remaining-label owner or a
different proof frontier inside the round.

## 8. Comparison with the exhausted K17a and K26 automatic routes

| frontier | exact automatic endpoint now known | surviving capacity/deficit | what remains genuinely open | immediate owner scope if proved |
|---|---|---|---|---|
| high-conductor K17a | the centered primitive-conductor sum reconstructs the original orientation block minus the safe low-conductor packet | exact-conductor capacity \(Lq\); one square root still leaves \(L\sqrt q\) | complete literal signed high-conductor orientation defect | only the K17a sufficient residual route after its accepted sectors |
| K26 endpoint | \(\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu\), \(\mathcal D_\nu\ll L\); exact cross-row product collisions are \(O(X^\varepsilon)\) | local \(L^2\) versus \(L\), endpoint \(L^4\) versus \(L^3\) | unequal-product near-cell signed anti-concentration, equivalent to the original local scalar concentration | only K26 and its residual connector |
| critical BAL | diagonal, both width-\(L\) corridors, axes, and the complete phase-free mode are paid; local commutators and independent swaps are self-returns | energy \(L^4\) versus \(L^3\) | a nonlocal complete actual-symbol prefix/vector correlation theorem | only persistent-critical \(j=1\) remainder/energy/fixed-block packet; remaining labels still open |

K17a and K26 should not be revisited through primitive centering or row
Gramization: those transformations now have exact self-return theorems.
BAL is different only in that a two-variable signed prefix object is still
outside the proved no-go classes. That distinction makes BAL logically
reopenable, but not presently selection-ready: there is no concrete
owner-saving vector theorem, and Round 171 has just shown that all local
versions return to capacity.

## 9. Owner and exponent scope

If (181.B3) were proved and all seams reviewed, the lawful immediate effect
would be limited to:

- `M9-M2-balanced-double-far-oscillatory-remainder`;
- the equivalent persistent-critical
  `M9-M2-balanced-double-far-actual-energy`; and
- the corresponding persistent-critical fixed-block packet statement.

It would **not** prove
`M9-M2-balanced-remaining-label-owner-quantifier-completion` or
`M9-M2-smooth-balanced-quarter-packet-estimate`. Even full BAL would still
leave hard TOP and UNBAL before M9--M2; the standard route would also leave
both direct M1 parents and endpoint uniformity, while the alternative route
would leave complete GAR. No local BAL result changes the exponent ledger:

- strongest internally proved exponent: \(1/3\);
- accepted external Li--Yang benchmark:
  \(0.3144831759740614\ldots\);
- target: \(1/4\).

## 10. Recommendation

**Do not choose BAL as the default Round-181 owner.** The critical theorem is
exact and important, but the only fresh formulation presently available is
the stronger maximal-prefix gate (181.B3), and no concrete argument makes
it more accessible than its terminal instance. The remaining-label node is
not one uniform analytic inequality and cannot close BAL while the critical
child remains open.

If the conductor ranks every competing frontier as equally mechanism-poor,
then BAL may be selected explicitly as a high-risk
`signed_two_parameter_prefix_or_self_return_gate`, with Tasks A--C and a
strict stop rule. It must not be presented as continuation of the Round-171
local commutator or as an automatic consequence of character parity,
determinant geometry, Gram positivity, or one-variable summation by parts.

## 11. Exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml` at the starting hash above;
- `state/next_round_plan.yml`;
- `strategy/round178_full_proof_strategy_current_literature_review.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/synthesis.md`;
- `proofs/kernels/m9_m2_balanced_two_defect_commutator_ramp_obstruction.md`;
- `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/synthesis.md`;
- `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`;
- `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reviews/conductor_round170_adjudication.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_residual_k26_near_peak_row_gram_self_return_obstruction.md`.

No web source, external theorem, or computation is used. This report changes
no proof status and starts no analytic proof.
