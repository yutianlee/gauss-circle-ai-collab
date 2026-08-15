# Round 71 derivation packet

## Frozen benchmark

\[
 J=X^{1/2},\qquad Q=X^{1/5},\qquad
 T=J/Q=X^{3/10}.
\]

The fixed-interior product wavelet has absolute capacity
\(TX^\varepsilon\); the target is \(J^{1/2}X^\varepsilon\).  The exact
required saving is

\[
 T/J^{1/2}=X^{1/20}.
\]

No cone-edge, full \(M9\)-\(M1\), or final-exponent inference is allowed.

## Accepted Round 70 reduction

Exact Poisson summation in the offset gives

\[
 \sum_s K\!\left(\frac{s-\vartheta}{T}\right)e(-\alpha s)
 =
 T\sum_{\ell\in\mathbb Z}
 e(-\vartheta(\ell+\alpha))
 \widehat K(T(\ell+\alpha)),
\]

so \(\|\alpha\|\asymp T^{-1}\).  Farey order \(R=Q<T\) therefore
contains only the \(0/1\) cell and is the known Fourier self-return.

At conductor order \(J\), every nonzero rational cell has

\[
 T\ll c\ll J,\qquad
 b=\min(a,c-a)\ll c/T,\qquad
 A_c\asymp c/T<\sqrt c.
\]

The last inequality follows from \(c\leq J<T^2\), not from
\(Q<\sqrt c\).

For odd \(c\), the exact two-variable residue is

\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =
 2ic\,\chi_4(c\sigma)
 e_c(\lambda_c\rho\sigma\bar a),
 \qquad
 \sigma\ {\rm odd},\qquad
 \lambda_c=(c^2-1)/4,
\]

and it vanishes for even \(\sigma\).  The classes
\(c\equiv2\pmod4\) and \(4\mid c\) give the accepted
conductor-\(4\) twisted analogues.  The double zero vanishes; odd-\(c\)
\(\rho=0\) and \(4\mid c\) \(\sigma=0\) axial modes survive.

The counterfactual complete odd-modulus numerator is an ordinary
Kloosterman sum.  The actual numerator is incomplete, so termwise
completion plus Weil and standard complete-sum Kuznetsov are
non-improving.

## Exact family to normalize

For each dyadic \(T\leq C\leq J\), derive from the fixed
Heath--Brown/Farey representative the complete weighted contribution

\[
 \mathscr S_C
 =
 \sum_{c\asymp C}
 \sum_{\substack{b\ll c/T\\(b,c)=1}}
 \sum_{\rho,\sigma}
 \alpha_{c,b}(\rho,\sigma;X)
 e_c\!\left(\mp bN+\lambda_c\rho\sigma\bar b\right),
 \tag{71.1}
\]

plus the two even-modulus versions and all axial terms.  The weight
\(\alpha\) must retain:

- the real offset \(\vartheta=X-\lfloor X\rfloor\);
- the exact delta/Farey integral and orientation;
- the one-sided ratio symbol and all smooth cutoffs;
- Poisson normalization and the local factor \(c\);
- the natural \((\rho,\sigma)\) ranges and stationary/nonstationary
  pieces;
- gcd factors, parity, and the conductor-\(4\) local data.

The first mandatory output is an exact normalization of (71.1) and a
dyadic inequality which is demonstrably sufficient, after summing
\(C,\rho,\sigma\), for the \(J^{1/2}X^\varepsilon\) wavelet target.
An arbitrary-coefficient large sieve is not assumed: the weights are the
actual delta-transform weights.

## Candidate mechanisms

The round may test:

1. dispersion in the short numerator before completion;
2. reciprocity followed by a large sieve in \(c\) and one dual index;
3. completion only after averaging, with the completion frequency kept;
4. a Kuznetsov/Deshouillers--Iwaniec or bilinear-Kloosterman-fraction
   theorem after exact hypothesis matching;
5. separate exact treatment of axial/Ramanujan modes;
6. a rigorous resonance or diagonal obstruction.

It may not replace the incomplete numerator by a complete residue
system, drop the actual weight, or count the natural zero-cell return as
new cancellation.

## Barrier ledger

- Natural delta order \(Q\): exact zero-cell self-return.
- Termwise completion plus Weil: non-improving because \(c/T<\sqrt c\).
- Standard Kuznetsov: wrong completeness and moving-argument interface.
- Odd modulus: ordinary Kloosterman, not Salié.
- Double zero: vanishes, but axial modes survive with gcd factors.
- Perfect squares/fourth powers: subtarget and not a counterexample.
- Required gain after full aggregation: exactly \(X^{1/20}\).

## Promotion rule

Promote only if the exact dyadic normalization and every summation power
close, or if a rigorous narrower reduction/no-go is independently
validated.  Candidate calculations and source analogies are not
accepted mathematics by themselves.

