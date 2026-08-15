# Round 70 conductor adjudication

## Decision

Promote a scoped reduction/no-go and retain the target estimate open.
The signed offset Poisson formula forces the circle variable into
\(\|\alpha\|\asymp T^{-1}\).  At the natural Farey order
\(R=Q=J/T<T\), this lies wholly inside the \(0/1\) cell, so the delta
decomposition is exactly the already known two-dimensional Fourier
self-return.  At conductor order \(J\), nonzero rational cells can occur,
but they have

\[
 T\ll c\ll J,\qquad
 b=\min(a,c-a)\ll c/T,\qquad
 A_c\asymp c/T\leq Q.
\]

At the benchmark \(J=X^{1/2}\), \(T=X^{3/10}\), \(Q=X^{1/5}\), one has
\(A_c<\sqrt c\) throughout.  Thus the actual numerator is incomplete,
and completing it before a Weil or Kuznetsov estimate is non-improving.
No \(J^{1/2}X^\varepsilon\) estimate, full-cone estimate, or exponent
improvement follows.

## Reconciliation of the two delta models

The reports use two exact but differently scaled circle decompositions.
They are compatible.

1. The blind and discovery reports use a finite Farey partition at
   \(R=Q\).  Compact Fourier support of the signed \(s\)-wavelet makes
   every nonzero cell vanish identically.
2. The source audit uses the exact Heath--Brown delta symbol at its
   natural conductor \(J\).  This larger conductor sees nonzero cells,
   but only through endpoint numerators of length \(c/T\).

The first model proves an exact self-return; the second identifies the
first genuinely new arithmetic family.  Neither supplies cancellation.

## Accepted residue algebra

With \(L=[c,4]\),

\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =\sum_{u\bmod c}\sum_{v\bmod L}
 \chi_4(v)e_c(auv+\rho u)e_L(\sigma v).
\]

Summing \(u\) first gives the exhaustive parity table recorded in all
three reports.  For odd \(c\),

\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =2ic\,\chi_4(c\sigma)
 e_c(\lambda_c\rho\sigma\bar a),
 \quad \sigma\ {\rm odd},\qquad
 \lambda_c=(c^2-1)/4,
\]

and it is zero for even \(\sigma\).  The \(c\equiv2\pmod4\) and
\(4\mid c\) cases are fixed-conductor-\(4\) twisted analogues.  A
counterfactual complete numerator gives an ordinary Kloosterman sum for
odd \(c\), not a Salié sum; even \(c\) gives twisted/cusp-to-cusp sums.
The double zero mode vanishes, but the odd-\(c\) \(\rho=0\) and
\(4\mid c\) \(\sigma=0\) axial modes survive with their gcd factors.

The conductor's finite residue computation agrees with the odd-modulus
formula for \(c=3,5,7,9,11\).  It is diagnostic only; the finite
Gauss-sum derivation is the proof.

## First open arithmetic inequality

After retaining the actual delta integral, the smallest new object is a
dyadic family of the form

\[
 \sum_{c\asymp C}
 \sum_{\substack{b\asymp c/T\\(b,c)=1}}
 \alpha_{c,b;\rho,\sigma}
 e_c\!\left(-bN+\lambda_c\rho\sigma\bar b\right),
 \qquad T\leq C\leq J,
\]

with the actual ratio symbol, offset, delta weight, dual aliases, even
modulus variants, axial terms, and gcds retained.  It must save
\(T/J^{1/2}=X^{1/20}\) after the full conductor and dual-frequency
aggregation.  No report proves this estimate or gives an actual-symbol
counterexample.

## Seam and source gates

| Gate | Decision |
|---|---|
| Exact real centre and signed \(s\)-Poisson | green |
| Natural \(R=Q\) Farey collapse | green |
| Conductor-\(J\) modulus and numerator ranges | green |
| Odd/even complete residue table | green |
| Double-zero and axial-mode ledger | green |
| Gcd and conductor-\(4\) factors | green |
| Perfect-square/fourth-power control | green, subtarget |
| Complete Weil estimate on the actual numerator | red as a closure |
| Standard Kuznetsov applicability | red as a closure |
| Joint short-numerator estimate | open |
| \(J^{1/2}\) target and exponent | open |

The source audit checked the exact completeness, modulus, averaging,
gcd, conductor, and coefficient hypotheses in the cited primary
sources.  None matches the short moving numerator family.

## Scope corrections and rejected inferences

The following inferences are rejected:

- a natural delta dissection automatically creates nontrivial moduli;
- the odd-modulus local factor is itself a Salié sum;
- completing the short numerator and applying Weil saves at the
  benchmark;
- standard Kuznetsov directly accepts the moving incomplete numerator;
- \(\chi_4\) kills every zero or axial mode;
- this fixed-interior no-go changes the full Gauss-circle exponent.

The accepted statement is fixed-smooth-interior and coefficient
preserving.  It does not cover cone edges or prove the global angular
radial estimate.

## State recommendation

Create a proved reduction node for the delta/Farey collapse and
short-numerator Kloosterman interface.  Add it as a dependency/evidence
item for the global angular-radial estimate.  Retain the signed
product-wavelet bound, shifted-divisor correlation, \(M9\)-\(M1\),
\(M9\), and the Gauss-circle target open.  A next round may attack the
joint \((c,b)\) large-sieve inequality, but it must not replace the
actual numerator by a complete residue system.

