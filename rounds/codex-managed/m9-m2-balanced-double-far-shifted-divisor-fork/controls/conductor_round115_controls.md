# Conductor Round 115 controls

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

## Algebraic reproduction

The divisor, increment, parity, radial-angular, and Hessian identities were
rederived independently by the conductor. In particular,

\[
 \det\nabla^2
 \left(\sqrt{(x+p)(y+q)}-\sqrt{xy}\right)
 =
 -{(qx-py)^2\over
 16\{xy(x+p)(y+q)\}^{3/2}}.
\]

This follows from the difference of the rank-one Hessians and needs no
numerical evidence.

## Phase-free reproduction

Two independent proofs were checked:

1. divisor expansion of the second low-gcd mask followed by Abel summation
   in \(h'\), giving \(O(X^\varepsilon)\) per outer
   \((h,k,k')\);
2. exact-gcd coordinates followed by Möbius inversion and Abel summation,
   giving \(\sum a_B^{<}\ll L\log^2L\), then restoring the two target-safe
   corridors.

Both prove

\[
 |M_B^{(0)}|\ll_\varepsilon L^3X^\varepsilon.
\]

No absolute value over an internal signed family is hidden in either proof.

## Fejer reproduction

Expansion of the sliding-window square verifies

\[
 \mathfrak D_H
 ={1\over H}\sum_m\left|\sum_{j=1}^Hb_{m+j}\right|^2
 =\Gamma(0)+2\Re\sum_{1\le r<H}(1-r/H)\Gamma(r).
\]

The outer Cauchy factor is \((N_B+H-1)/H\). Substituting the accepted
Round-114 corridor allowances gives

\[
 O_\varepsilon\!\left((L^5/H+L^3)X^\varepsilon\right)
\]

for \(H\ge L\), and \(O_\varepsilon(L^4X^\varepsilon)\) for
\(2\le H\le L\). This certifies no fixed-power shortening. It does not
certify a lower bound for the signed Fejer form.

## Source reproduction

The source-hypothesis comparison was checked against:

- Alex Cowan, A twisted additive divisor problem,
  https://arxiv.org/abs/2304.12572;
- Fernando Chamizo, The Additive Problem for the Number of Representations
  as a Sum of Two Squares,
  https://doi.org/10.1007/s00009-021-01959-3.

No external theorem was used to prove an internal estimate.

## Hygiene and evidence limits

- all three reports contain the required seven top-level contract sections;
- all campaign text files are UTF-8 with LF line endings and no bare
  carriage returns;
- no numerical experiment was used;
- the one symbolic Hessian check was reproduced by the displayed
  rank-one derivation and is not treated as computational certification;
- the critical scale is always \(R\asymp L^3\), \(N_B\asymp L^2\);
- no result is passed to hard TOP, unbalanced M2, M9-M1, endpoint
  uniformity, M9, or the global exponent.

## Validation commands and outcomes

```text
python -m unittest discover -s tests -p 'test_*.py'
......
Ran 6 tests
OK

python -m math_collab.campaigns validate --manifest state/active_campaign.yml --graph state/proof_obligations.yml
Campaign OK

python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/state_patch.json --round-index 115 --judge-ref rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md
Patch OK

python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/state_patch.json --apply --round-index 115 --judge-ref rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md
Patch applied: 3 created, 3 updated, 8 rejected; graph validated

git diff --check
exit 0; line-ending conversion warnings only
```
