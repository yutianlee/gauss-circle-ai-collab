# 1. Result and verdict

**Verdict: GREEN.** The durable kernel has SHA-256
`0ea2b3c336795fe5290d0eed836f787a2165ed866ab7ffc9baea81ea144b8723`,
and the formal candidate has SHA-256
`683ad5bd26facb44414e9feeb6f1824c3ccf9c1edcf51269b7b57ad788753808`,
exactly the two frozen hashes assigned for this review.

The complete mathematical body, beginning with `Fix real X>=2` and ending
immediately before `## Evidence and diagnostic`, is byte-identical in the two
files: 9,765 bytes with SHA-256
`6b2bc507a092eacebbcf038fb3fa53970675ed34059053c003957bb9e2baee84`.
It contains all 23 tags (188.K1)--(188.K23), and every tagged display is
individually identical.

Starting from the candidate and applying only four durable editorial changes
reconstructs all 12,279 kernel bytes exactly and reproduces the frozen kernel
hash. Those changes are metadata, the statement heading, one evidence-list
conjunction, and the independent-review evidence block. No hypothesis,
formula, proof step, complement condition, no-go boundary, dependency, or
open relation changed.

# 2. Exact reviewed claim and hypotheses

The kernel and candidate state the same claim under the same hypotheses:

- real `X>=2`, one nonempty literal middle/lower residual hard-M1 shell
  `L>=2`, one sign `sigma`, and fixed `B>0`;
- the hash-bound support consequence `L << X^(1/4)`, with literal zero
  extension outside the inherited hard-top frequency range;
- `R_0=ceil(L)` and `Q=floor((log(2X))^B)`;
- one nonempty integer-height block `Y<h<=2Y`, with `Y>Q`;
- exactly the Round-185 primitive carrier and literal amplitudes and the
  Round-187 high Fourier packet;
- high-mode restrictions `U>4Q`, `q_U(k)>Q`, and `|k|_U>Q`; and
- every selector, arithmetic deletion, profile, floor, star, half-weight,
  hard sample, crossing, endpoint, conjugation, Fejer factor, phase, sign,
  positivity predicate, orientation, and zero extension retained literally.

The proved strict packet is the exact part with `Qm>=Y`, where
`m=(k,U)`. The exact complex complement has

```text
U=mq>4Q,    q>Q,    m|a|_q>Q,    Qm<Y,
```

under the original carrier and one outer real part. The strict packet is
absolutely `O_(B,epsilon)(L^2 X^epsilon)`. The complement has only the
positive `O_epsilon(YL^2 X^epsilon)` estimate, and its one-sided
`O_(B,epsilon)(L^2 X^epsilon)` estimate remains open.

# 3. Derivation and consistency checks

## 3.1 Mechanical comparison

The candidate has 11,388 bytes and 387 lines. The kernel has 12,279 bytes and
405 lines. A line-level comparison has exactly four non-equal hunks:

| candidate location | kernel location | exact classification |
|---:|---:|---|
| line 13 | lines 13--16 | replaces candidate-pending status with the frozen candidate hash and durable-kernel evidence status |
| line 16 | line 19 | changes `## Candidate statement` to `## Accepted statement` |
| line 369 | line 372 | removes `and` before a now-extended evidence list |
| after candidate line 371 | kernel lines 375--389 | inserts the five hash-bound independent review references |

An in-memory construction performed these four replacements on the candidate
text. It produced:

```text
bytes      = 12279
sha256     = 0ea2b3c336795fe5290d0eed836f787a2165ed866ab7ffc9baea81ea144b8723
byte_equal = true
```

Thus the kernel is exactly the candidate plus the declared durable metadata,
heading, and review-evidence edits. There is no unclassified byte drift.

## 3.2 Formulas (188.K1)--(188.K23)

Both files contain exactly one occurrence of each tag from K1 through K23.
Extracting every tagged display from its enclosing display delimiters gives
23 equality checks out of 23. In substance:

- K1--K3 have the same shell support, `R_0,Q`, dyadic block, and high-mode
  hypotheses.
- K4--K6 have the same unique `U=mq`, `k=ma` lift, coefficient
  `c_U(k)=m^(-1)c_q(a)`, inverse phase, and least-distance scaling. Neither
  file assumes `(m,q)=1`.
- K7--K12 have the same `Qm>=Y`/`Qm<Y` complex partition, target-safe strict
  packet, exact complement, positive capacity, and still-open one-sided
  complement.
- K13--K19 have the same coefficient calculation, logarithmic unit mass,
  `O(YL)` dyadic atom count, `Y/m` payment, exact triple-divisor identity,
  and power ledger.
- K20--K23 have the same orientation equations and signs, affine-constant
  lifted phase, repaired `v=1` reciprocal convention, additive reciprocity,
  and primitive near-half mass control.

The equality is literal, not a normalization-by-whitespace comparison.

## 3.3 Proof, multiplicity, complement, and scope

The proof paragraphs are part of the 9,765-byte equal body. Therefore the
kernel preserves exactly:

- the lift bijection even when `m` and `q` share primes;
- the reindexing `(g,U) <-> (u,U)` and ordered factorization
  `u=g m q`, with no lost or duplicated carrier;
- the affine `O(1+kappa)` terminal-site allowance and both orientations;
- the split of the complex aggregate before triangle inequality or real part;
- the factor `Y` removed only through `1/m<=Q/Y` in the strict packet;
- the primitive and moderately imprimitive complement;
- the fact that determinant, completion, reciprocity, and positive-energy
  manipulations are controls rather than the missing signed estimate; and
- the bounded-array countermodel as a coefficient-uniform mechanism control,
  not literal lower mass or failure of the open relation.

The no-go and downstream boundary is also identical. Even a proof of
(188.K12) would close only the exact original-`t=1` residual through the
accepted connectors; all original `t>=2` small-G incidence, the large-G
near-resonant complement, M1 and M2 parents, endpoint uniformity, M9, both
bridges, the quarter target, and exponent claims remain open.

## 3.4 Dependencies

The dependency paragraph is byte-identical. Both artifacts name exactly the
direct accepted dependencies

- `M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`; and
- `Divisor-bound-elementary`.

Both state that the K1 support is transitive through the accepted Round-185/
187 chain, made explicit by the support connector, with authoritative source
node `M9-M1-top-endpoint-transform`. Both state that no external theorem is
used.

# 4. First doubtful step

**None in kernel-candidate consistency.** The earlier K1 support-provenance
and K22 modulus-one repairs appear identically in both artifacts. The first
open mathematical step remains exactly (188.K12): obtain a jointly signed
actual-coefficient estimate for the exact complement, gaining the full
factor `Y` before positive recombination.

# 5. Controls

| control | outcome |
|---|---|
| frozen kernel hash | PASS: `0ea2b3c3...8723` |
| frozen candidate hash | PASS: `683ad5bd...3808` |
| candidate-to-kernel four-edit reconstruction | PASS: byte-identical |
| statement/proof/scope body | PASS: 9,765 identical bytes |
| tags K1--K23 | PASS: 23/23 present once in each file |
| tagged display equality | PASS: 23/23 |
| hypotheses and literal carrier | PASS: identical |
| complement and one-real-part placement | PASS: identical |
| proof and multiplicity ledger | PASS: identical |
| no-go and downstream scope | PASS: identical |
| dependency paragraph | PASS: identical |
| hash-bound referenced artifacts | PASS: all exist and match |
| unhashed evidence paths checked | PASS: both exist |

This was a textual and analytical review. No numerical computation was used
as theorem evidence, and no candidate, kernel, state, graph, synthesis, plan,
or validation file was edited.

# 6. Dependencies, evidence, and hashes

Every hash stated in the kernel resolves to the expected existing artifact:

| artifact | SHA-256 |
|---|---|
| starting `state/proof_obligations.yml` | `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff` |
| discovery report | `c77fe83e1c04042c221a1132121c50d8e745aaaca274d1284ec385e0bd3b8ca7` |
| hostile report | `1f27281d91fd7290f548e3c1dfa696f2a6a9b82e184f8bc878747a29f1a3dce1` |
| blind report | `a8de6402d8a57d22a773d9b763e195f3e959a1a50cf084bb7ffab7205460231e` |
| formal candidate | `683ad5bd26facb44414e9feeb6f1824c3ccf9c1edcf51269b7b57ad788753808` |
| normalization/multiplicity seam review | `6c29cf14987029a3279c595ca38f051a29d5f7efbfb63ebe89e8b2e7ac56b899` |
| normalization/multiplicity post-repair verification | `097226ab0d8acf98f65502b3163f1d5c5a384289725aa06379d5e6a27be0401e` |
| power/literal-scope/completion seam review | `2ec3c9c0d96303400348fd3b2682e72dac4eeb955b0e558ab2f4dbad91548a01` |
| blind post-unmask seam review | `80c4359a5f5d1a37fa2de60262de25325cfa9f3e4b45c01ff1489eda0fadd2a1` |
| blind post-unmask post-repair verification | `79e0be1854c9e61f643081a42e300a766f1829826ecf97ac6ac7dd313e051c26` |
| exact-check Wolfram script | `7bad1b482654e69325feaf844d359d1643a3245c8e990742ecfc83141e995b99` |
| Wolfram diagnostic report | `4d6173c31bfe63e158f5d07d90488808e65d6b81a58d5e428ed1e01ae69bcb42` |

The two evidence paths stated without hashes also exist:

| artifact | observed SHA-256 |
|---|---|
| support connector | `9791a4224dff4f2067e331060b39d0c742ee4c20785a9350d81bd7382d18b9ac` |
| conductor report reconciliation | `d67f5a7a43a735dd8ae7c3534c5e4998c988253cc1d4f68c765f7ff4096e20b8` |

# 7. Recommended state effect

**Accept the final kernel-candidate consistency seam as GREEN.** The kernel
may be used as the durable form of the already GREEN candidate because its
entire mathematical statement, proof, complement, dependencies, and scope are
unchanged. The kernel's additional material is exclusively durable metadata,
the accepted-statement heading, and hash-bound review evidence.

This recommendation promotes no claim beyond the strict imprimitive-lift
packet and exact reduction already stated. Keep (188.K12), the complete
high-height relation, the original-`t=1` residual, every `t>=2` incidence,
parent, bridge, theorem, and exponent open.
