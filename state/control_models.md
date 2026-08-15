# Gauss-Specific Control Models

These controls are proof-unit tests. They can expose a false mechanism; passing them does not certify an asymptotic theorem.

## `raw-vs-weighted`

Compare the weight-blind tuple count with the genuine mass carrying

$$
|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|,
\qquad |\beta_h|\ll |h|^{-1}.
$$

No exponent may be transferred between them without writing the coefficient summation and lift multiplicities explicitly.

## `signed-vs-unsigned`

Run four variants: true $\chi_4(h)$ signs, absolute values, random signs, and adversarial signs of the same magnitude. A signed proof must identify the exact cancellation property that fails in the other three.

## `known-lower-bound-families`

Test every absolute or unsigned near-collision claim against the accepted UNC, TS, and W-1 families. Record parity, dyadic support, coefficient lower envelopes, scale restrictions, and whether the family controls a raw count or a weighted mass.

## `dyadic-endpoints`

Check separately

$$
D=X^{1/4},\qquad D=X^{3/8},\qquad D=X^{1/2}.
$$

An averaging or smoothing argument valid below the endpoint must not silently cross $D=X^{1/2}$.

## `real-vs-complex-pairing`

The raw two-sided M2 formula is authoritative. Compare real dyadic weights, genuinely complex weights, symmetric $h$-weights, and asymmetric $h$-weights. A $\operatorname{Re}B_h$ shortcut requires its exact conjugacy hypotheses.

## `exact-vs-near-resonance`

Keep $N=0$ and $0<|N|$ separate. Test exact Fejer resonances, the smallest nonzero bands, and wider fat bands. Exact-resonance energy does not control near collisions without an explicit theorem.

## `coefficient-adversary`

Replace the fixed Vaaler coefficients by arbitrary coefficients of the same magnitude and by adversarial phases. If an argument survives, it must either prove that stronger statement or identify where the fixed $\Phi$ and $\chi_4$ structure enters.

## `support-and-degeneracy`

Test sharp and smooth dyadic weights, truncation edges, $uv=0$ branches, repeated denominators, and reduced-fraction lift boundaries. State explicitly which cases are excluded and where they are bounded.

## Required reporting

For each control, record the exact input, expected failure or invariant, observed result, and implication for the candidate lemma. “Passed numerics” is never a proof status.
