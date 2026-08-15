# Round 67 conductor adjudication

## Decision

Promote the exact reciprocal-energy and B-process reduction, but retain
the signed reciprocal large sieve (RSLS) open. The three reports agree on
the normalization, diagonal, Poisson sign, character sign, and the first
unproved off-diagonal estimate. None proves a power saving or produces a
counterexample to RSLS.

## Accepted kernel

Let \(J=X^{1/2}\), \(Q=J/T\),
\(a_j=\chi _4(j)\Xi(j/J)\), and let \(w\geq 0\) be smooth and bounded
below on the support of the coefficients \(b_k\). Then

\[
 \mathcal E=
 \sum_k w(k/Q)\left|\sum_j a_j e(kX/j)\right|^2
\]

satisfies

\[
 |\mathcal B|^2\ll Q^{-1}\mathcal E.
\]

Poisson summation gives the exact energy identity

\[
 \mathcal E=Q\sum_{j_1,j_2}a_{j_1}\overline{a_{j_2}}
 \sum_{m\in\mathbb Z}\widehat w
 \!\left(Q\left[m-X(1/j_1-1/j_2)\right]\right),
\]

whose diagonal is \(\asymp QJ\). For odd \(j_1,j_2\),

\[
 \chi _4(j_1)\chi _4(j_2)=(-1)^{(j_2-j_1)/2}.
\]

Under the accepted smooth fixed-interior B-process interface,

\[
 S_k=(J/k)^{1/2}
 \sum_{\rho\in\{1,3\}}\epsilon_\rho
 \sum_{r\asymp k}c_\rho(k,r)
 e\!\left(2\sqrt{kX(r-\rho/4)}\right)+O_A(X^{-A}).
\]

Consequently RSLS is equivalent, up to controlled errors, to the
target-diagonal second moment

\[
 \sum_{k\asymp Q}|P_k|^2\ll Q^2X^\varepsilon.
\]

## Why the estimate is not promoted

The diagonal of the last moment is already \(\asymp Q^2\); the missing
claim is lossless cancellation of its complete signed off-diagonal.
Unsigned reciprocal spacing is too large. Pairing the character sign in
the half-difference is invalid because one step moves the Poisson alias
on unit scale, whereas the kernel has width \(Q^{-1}\). Visible
square/fourth-power fibers are only diagonal-sized, so they do not
disprove the conjectured energy bound.

The source audit found no theorem with the required fixed-center,
moving-symbol, residue-restricted hypotheses. The B-process instead
returns to the same subcritical one-sided square-root-product kernel.

## Scope

This round proves a reduction, not RSLS. It changes no radial interval,
M9-M1 status, M9 status, or Gauss-circle exponent.

