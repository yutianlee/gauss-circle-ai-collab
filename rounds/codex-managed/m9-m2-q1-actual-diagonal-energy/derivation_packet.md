# Round 103 derivation packet

## 1. Accepted input and exact target

Round 102 proves that the residual half-open \(q=1\) block has no
nonzero shifted correlation. Its complete actual diagonal is therefore
the first disjoint input required by the fixed-\(a\) Gram:

\[
 \mathcal D_1^{\rm act}
 =\sum_{a\asymp A}|F_a(1)|^2
 \stackrel{?}{\ll_\varepsilon}
 X^\varepsilon {L^4\over A}.
\]

Here

\[
 K\asymp {J\over A},\qquad
 G\asymp {L\over A},\qquad
 \rho={AJ\over L^3}>1.
\]

The statement is sufficient for this singleton subrange only. It is not
known to be true.

## 2. Literal coefficient

Put \(b=a+2\),

\[
 \delta_a=\sqrt{a+2}-\sqrt a,\qquad
 \Lambda_a={X\delta_a^2\over2},
\]

and

\[
 I_a=\left({J\delta_a\over2\sqrt a},
           {J\delta_a\over\sqrt{a+2}}\right).
\]

The complete row is typed as

\[
 F_a(1)
 =\mathbf1_{\rm residual}
 \sum_{\substack{g\ {\rm odd}\\g\in\mathcal G_{a,a+2}}}
 \sum_{k\in I_a\cap\mathbb Z}
 \omega_{a,g,k}
 W_R\left({\Lambda_a\over k}\right)
 \mathfrak C^\circ_{a,a+2,k}(g).
\]

The multiplier \(\omega\) includes every accepted primitive and owner
mask, actual profile, floor, star, sign, orientation, collar convention,
and zero extension. The complete physical integral is

\[
 \mathfrak C^\circ_{a,a+2,k}(g)
 =g\int_{(a+2)/4}^{a}A^\circ_{ga,g(a+2)}(gu)
 e\left(g[ku-J\delta_a\sqrt u]\right)\,du.
\]

No sign, positivity, or separability not displayed here may be assumed.

## 3. Exact carrier and accepted lift variation

Completing the square gives

\[
 ku-J\delta_a\sqrt u
 =k\left(\sqrt u-{J\delta_a\over2k}\right)^2
 -{\Lambda_a\over2k}.
\]

Thus

\[
 \mathfrak C^\circ(g)
 =e\left(-{g\Lambda_a\over2k}\right)
 \mathfrak B^\circ(g),
\]

where the centred complete integral retains all saddle entry and exit.
Round 77 proves

\[
 |\mathfrak B^\circ(g)|
 +g|\partial_g\mathfrak B^\circ(g)|
 \ll {J\delta_a\sqrt G\over k^{3/2}}
 \asymp \sqrt{AL\over J}.
\]

This is structured step-two lift variation. It is not cancellation by
itself.

## 4. Metric carrier guardrail

If \(\theta=\Lambda_a/k=\ell+\eta\), the complete carrier cancels the
apparent quotient sign and restores the integer metric zero mode. The
actual density and every discrepancy mode remain one coefficient.
Consequently a proof may not:

- delete the density term;
- infer lift cancellation only from quotient parity;
- estimate the metric discrepancy without the mean;
- repeat adjoint reciprocal Poisson as a new gain.

The strict metric partition is supported where

\[
 0<c_1/R\le\|\Lambda_a/k\|\le c_2/R<1/2
\]

for its literal active \(R\)-range.

## 5. Competing mechanisms

Test both directions before taking absolute values across the internal
sums.

1. Direct upper bound: seek a lift-\(k\) energy, large-sieve, or
   \(a\)-averaged estimate which uses the complete actual coefficient
   and gains \(\rho^{-1}\) at energy level.
2. Literal obstruction: on a strict interior stationary plateau, test
   whether the Gaussian unit, carrier cancellation, metric annulus, and
   actual profiles leave a coherent nonzero contribution large enough
   to falsify the sufficient diagonal lemma.

A lower obstruction requires an actual lower bound after every owner,
profile, star, collar, and competing mode is included. A leading
stationary term or a positive-capacity count alone is insufficient.

## 6. Mandatory controls and scope

- exact singleton normalization and target;
- literal \(k\)-interval and finite odd \(g\)-support;
- complete metric density and discrepancy;
- quotient-carrier cancellation;
- exact centred integral and saddle entry/exit;
- all profiles, floors, stars, orientations, and prior owners;
- empty and singleton \(k\)-fibres;
- Pell \((25,27)\) and general near-square \(q=1\) rays;
- fourth-power and strict-metric recurrence;
- Gaussian phase and any actual amplitude sign;
- arbitrary-coefficient and unsigned false shadows;
- upper versus lower proof requirements;
- route counterexample versus canonical M2 theorem;
- primary-source literal hypothesis map;
- downstream and exponent scope.

Do not infer the longer-row Gram, canonical density-discrepancy energy,
other M2 packets, M9-M2, M9-M1, M9, endpoint uniformity, or an exponent
without the exact implication.
