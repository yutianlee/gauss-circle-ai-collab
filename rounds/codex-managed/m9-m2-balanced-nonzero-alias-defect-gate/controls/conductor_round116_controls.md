# Conductor Round 116 controls

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

## Algebraic reproduction

The conductor independently rederived the literal progression formulas.
For odd (d\mid h',k'), (s=s_d+dt) and
(mu=1/2-m) give (lambda=\mu/d). Direct differentiation gives

\[
 x={Xk'\over\lambda^2},\qquad
 |\phi''(t_*)|\asymp d^2L^2,
\]

so the alias count is (dL^3) and the stationary amplitude is
((dL)^{-1}). Direct substitution reproduces the residue phase and the
exact square completion (116.S5)--(116.S6). Substitution into both
determinants reproduces (116.S7), including their dependence relation.

## Finite-Poisson and error reproduction

The literal accepted (t)-integers form (O(1)) runs for each
((h,k,k',d)). Half-integer enclosure preserves those integers. The
leading nonstationary boundary tails alternate under symmetric dual
summation; the remaining twice-integrated tails are absolutely summable.
The (O(dL)) transition modes per endpoint each cost (O((dL)^{-1})),
and (dL^3) interior stationary remainders of size
(O((dL^3)^{-1})) cost (O(1)). With

\[
 \sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon
\]

and (O(L^3)) outer triples, the aggregate error is
(O_\varepsilon(L^3X^\varepsilon)). No stationary bulk alias is put
inside an absolute sum in this calculation.

## Capacity and involution reproduction

The transformed linear and square masses are

\[
 (dL^3)(dL)^{-1}=L^2,
 \qquad
 (dL^3)(dL)^{-2}=L/d.
\]

For (k'=dv), the reciprocal frequency is (Xd^2/(2\mu)). The product
window at resolution (d/L) has width (d^2L^2); dyadic geometric-sum
charging returns (L^2) per outer row and (L^4) globally at (d=1).

Pigeonholing (N_d=dL^3) frequencies into (Q_d=L/d) resolution cells
reproduces the (d^2L^2) cluster and (d^3L^5) close-pair lower bounds.
Testing the largest short arc gives a coefficient-uniform large-sieve
constant at least (N_d).

Finally, the Legendre transform of

\[
 -{Xd^2v\over2\mu}-{\ell_d\mu\over2}-n\mu
\]

is (-dR\sqrt{v(\ell_d+2n)}). The second Jacobian is reciprocal to the
first, the Fresnel factors cancel, and the half-lattice factor restores
the primal character. This verifies exact two-B-process self-return.

## Row-energy and coefficient controls

For (T_{h,k}=S_B-C_{h,k}), each corridor row has absolute mass
(O_\varepsilon(LX^\varepsilon)). On (L^2) nondegenerate rows,

\[
 \|T\|_2\ge cL|S_B|-O_\varepsilon(L^2X^\varepsilon).
\]

Thus the proposed (L^4) row-energy estimate would force
(|S_B|\ll L), not just the (L^{3/2}) scalar scale. A phase-adapted
bounded coefficient array aligns the replicated Gram, so no
coefficient-uniform version is promoted.

## Source and downstream controls

The B-transform source is used only to check normalization and involution;
the generalized double-large-sieve source is rejected after its separated
phase, factorized coefficient, parameter, and spacing-energy hypotheses
fail to match the literal kernel. No external theorem proves the target.

Only one persistent (j=1) block is used. The exact-square (j=2)
boundary, hard TOP, UNBAL, both M1 parents, endpoint uniformity, M9, and
the pointwise exponent remain untouched. The no-go is for named proof
mechanisms and is not a lower bound for the actual signed sum.

## Hygiene and evidence limits

- all three reports contain exactly the seven required numbered sections;
- all campaign text files are strict UTF-8 with LF line endings, balanced
  display-math delimiters, no bare control characters, and no trailing
  whitespace;
- no numerical experiment was used;
- the algebraic and capacity calculations were independently reproduced;
- the phase-free owner is used exactly once; and
- the validation matrix is green while the actual bulk target is explicitly
  recorded open.

## Validation commands and pre-application outcomes

```text
python -m unittest discover -s tests -p 'test_*.py'
......
Ran 6 tests
OK

python -m math_collab.campaigns validate --manifest state/active_campaign.yml --graph state/proof_obligations.yml
Campaign OK

python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/state_patch.json --round-index 116 --judge-ref rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md
Patch OK
```

```text
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/state_patch.json --apply --round-index 116 --judge-ref rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md
Patch applied: 2 created, 3 updated, 8 rejected; graph validated

python -m math_collab.campaigns validate --manifest state/active_campaign.yml --graph state/proof_obligations.yml
Campaign OK

python -m unittest discover -s tests -p 'test_*.py'
......
Ran 6 tests
OK
```

Resulting graph SHA-256:
`a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`.
