# Research Round 1 Closing Synthesis

## Outcome

Round 1 closes with no proof-graph mutation. It produced a stronger candidate obstruction that must be independently validated in Round 2.

## Evidence comparison

### Blind upper-bound derivation

The statement-only worker proved a valid definition-level estimate

$$
\mathcal M_{\rm abs}(D,H;K)
\ll D^3(\log(1+H))^3(1+K/D^2),
$$

up to explicit coefficient and dyadic-weight factors. It correctly accounts for reduced fractions, lifts, harmonic weights, and Farey packing. At $K=D^4/X$ it is too weak for the desired $D^2X^\epsilon$ budget. It does not support A4-009's proposed $D+D^4/X$ bound.

### Hostile audit and conductor derivation

Two independent derivations restrict to $h_1=h_2=h_3=h_4=1$, partition the pair sums $1/d_1+1/d_3$ into windows of width $M/(16D^4)$, and apply Cauchy--Schwarz. Conditional on $|\beta_{1,H}|\gg1$ and the accepted exact-$N=0$ closure, they obtain

$$
\Sigma_{\rm abs}(0<|N|\le M)
\ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon.
$$

At $M=D^4/X$, this is $cD^5/X-C_\epsilon D^2X^\epsilon$ and yields a power obstruction for $D\ge X^{1/3+\delta}$. The older $X^{3/8}$ scale is the $h\asymp H_D$ bulk-frequency specialization, not the strongest weighted obstruction.

The same audit identifies a direct error in A4-009: its equal-denominator additive family has $N=0$ exactly and therefore gives no nonzero-band count.

### Bounded finite diagnostic

The diagnostic exactly separates raw count, reciprocal mass, true signed beta mass, and unsigned beta mass. The conductor reproduced the run locally with all controls passing. It is retained as `diagnostic_only`; it neither proves nor refutes the asymptotic lower bound.

## Round decision

- Reject A4-009's weighted upper bound and equal-denominator nonzero-count argument as candidates.
- Retain the unit-frequency W-1 lower bound as a high-value conditional candidate.
- Do not patch `state/proof_obligations.yml` in Round 1.
- Do not infer anything about the full true signed mass, M9-M2, M9, or the Gauss-circle target.
- Send the candidate to a statement-only rederivation, H4/weight normalization audit, and adversarial endpoint review in Round 2.

## Resource accounting

The round was dominated by analytical and algebraic work. One bounded finite diagnostic was used for normalization and falsification controls and did not drive the theorem-level conclusion, satisfying the 80/20 policy.
