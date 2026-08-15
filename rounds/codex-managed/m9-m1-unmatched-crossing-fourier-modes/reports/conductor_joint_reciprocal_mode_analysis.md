# Joint reciprocal-mode analysis

## 1. Result

The Vaaler main modes are exact, but generic one-variable exponent-pair
technology does not approach the target. The exact wavelet filter
localizes the surviving modes at (k\asymp Q=J/T=X^{\nu/2}). An exponent
pair ((\kappa,\lambda)) then has capacity

\[
 J^\lambda Q^\kappa
 =X^{(\lambda+\kappa\nu)/2+\varepsilon}.
\]

At \(\nu=2/5\), TTY gives exponent (5163/12820\), while the audited
classical pair ((2/7,4/7)) gives (12/35). Neither closes (1/4).

## 2. Exact statement and hypotheses

For Vaaler height (K\) and (1\leq|k|\leq K),

\[
 \mathcal S_k(v)=\sum_j\chi_4(j)\Xi(j/J)e(kn_0/j)
 \{1-e(kv/j)\}.
\]

The coefficient has size (O(1/|k|)), and

\[
 |\mathcal S_k(v)|\ll X^\varepsilon
 \min(1,|k||v|/J)|k|^\kappa J^\lambda
\tag{2.1}
\]

for any lawfully applicable exponent pair. The fixed (j\bmod4) split
changes only constants.

## 3. Proof or derivation

Subtracting the two Fourier polynomials gives the displayed difference
factor. For low modes it contributes (|k||v|/J); high modes must be
treated as two reciprocal sums. After the exact wavelet difference is
kept signed, Poisson in the displacement variable restricts the
nonzero contribution to (2Tk/j\in\operatorname{supp}g), hence
(k\asymp J/T=Q). The (1/k) coefficients sum over a fixed relative
transition block without an additional power. This yields
(J^\lambda Q^\kappa).

For TTY, ((\kappa,\lambda)=(89/1282,997/1282)), giving
((997/1282+(89/1282)(2/5))/2=5163/12820\). The pair ((2/7,4/7))
gives ((4/7+(2/7)(2/5))/2=12/35\).

## 4. First doubtful or unproved step

The missing input is a joint signed ((j,k)) estimate whose transition
block reaches square-root scale. Pointwise exponent pairs cannot do this.
A Cauchy/large-sieve approach has a diagonal already of final size
(J^{1/2}=X^{1/4}), so every off-diagonal must be controlled with no
power loss.

## 5. Required control test and outcome

- Difference sign and negative modes: pass by conjugacy.
- Low/transition/high modes: pass with transition (Q=J/T).
- TTY normalization: pass with phase parameter (kJ) on length (J).
- Fejer residual: requires (K\geq X^{1/4}) from
  (X^\varepsilon(1+J/K)); it is target-safe but gives no saving.
- Perfect powers: coherent reciprocal modes exist, invalidating generic
  irrationality.
- Bilinear diagonal: exactly target-sized; off-diagonal theorem absent.

## 6. Dependencies and exact artifacts used

This conductor report records the discovery agent's interim result and
reconciles it with the independent hostile/source audit. The agent did
not materialize its assigned report before interruption. Inputs were the
Round-66 packet, Round-65 synthesis, and the audited TTY exponent pair.
No numerics were used.

## 7. Recommended state effect

Promote only the exact Fourier interface, Fejer count, and method-capacity
ledger after adjudication. Retain every signed target and exponent open.
