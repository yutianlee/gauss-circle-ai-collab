# Hostile audit of the local character-hyperbola discrepancy

## 1. Result: exact Abel seam, unmatched-row obstruction, and source no-go

The corrected affine extension in (65.7a) makes the Abel identity (65.8)
exact, with the displayed sign and index shift.  For integral displacement
\(v\) smaller than the lower supported denominator, period-four pairing
reduces the discrepancy to the *unmatched crossing rows*

\[
 \mathfrak D_X(n_0+v;n_0)
 =\sum_{r\geq0}\Xi\!\left(\frac{4r+1}{\sqrt X}\right)
 \{C_{4r+1}(v)-C_{4r+3}(v)\}
 +O_\Xi(1+vX^{-1/2}),                                      \tag{1.1}
\]

where

\[
 C_j(v)=\mathbf 1_{\{\exists m:\ n_0<jm\leq n_0+v\}}.
\]

Each difference in braces is \(0,1\), or \(-1\).  Thus character
pairing cancels matched rows exactly but supplies no bound for the signed
symmetric difference.  Proving that remaining sum is
\(O(X^{1/4+\varepsilon})\), or proving the weaker wavelet-weighted
version, is precisely the new arithmetic input.  No audited theorem
supplies it at the prescribed center.  In particular, the available
short-divisor results concern the complete divisor function and are
usually averaged over the center; character Voronoi formulas concern
complete convolutions; and Kloosterman-fraction estimates require modular
inverses and coprimality absent here.  This is a scoped source and method
no-go, not a counterexample to LCD.

## 2. Exact statement and hypotheses

Let \(X\geq2\), \(n_0=\lfloor X\rfloor\),
\(N=X^\nu\), \(T=\sqrt{X/N}\), and
\(\Xi\in C_c^\infty((0,1))\).  Put

\[
 A(n)=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X),\qquad
 c_X=\sum_{j\geq1}\frac{\chi_4(j)}j\Xi(j/\sqrt X).
\]

Extend \(A(n)=0\) for \(n\leq0\).  Define \(\mathfrak D(n_0;n_0)=0\)
and, for every \(n\in\mathbb Z\),

\[
 \mathfrak D(n;n_0)-\mathfrak D(n-1;n_0)=A(n)-c_X.          \tag{2.1}
\]

This is the corrected (65.7a); on \(n\leq0\) it is affine and is not the
negative-argument floor formula.  For \(n\geq1\), it agrees with

\[
 \sum_j\chi_4(j)\Xi(j/\sqrt X)
 \left(\left\lfloor\frac nj\right\rfloor-
 \left\lfloor\frac {n_0}j\right\rfloor-
 \frac{n-n_0}{j}\right).                                  \tag{2.2}
\]

If \(W_n=K((n-X)/(2T))\) is the accepted sampled wavelet, then

\[
 \sum_{n\geq1}A(n)W_n
 =\sum_{n\geq1}\mathfrak D(n;n_0)(W_n-W_{n+1})+O_B(X^{-B}). \tag{2.3}
\]

For (1.1), \(v\) is an integer with
\(0<v<a\sqrt X\), where
\(a=\inf\operatorname{supp}\Xi>0\).  A real displacement must first be
replaced by an integral endpoint; its nonintegral part leaves the explicit
linear correction and is not covered by the binary-crossing notation.

At \(\nu=2/5\), \(T=X^{3/10}\).  The unsigned crossing capacity is
\(TX^{o(1)}\), while the requested bound is \(X^{1/4+\varepsilon}\).
The missing factor is

\[
 \frac{T}{X^{1/4}}=X^{1/4-\nu/2}=X^{1/20}=\frac HL
\]

for \(D=\sqrt X\), \(L=\sqrt N\), and \(H=X^{1/4}\).

## 3. Proof and hostile derivation

Since \(B(y)=\sum_{n\leq y}A(n)\), one has
\(B(n)-B(n-1)=A(n)\) for positive integral \(n\), proving (2.1)--(2.2).
Period-four Abel pairing applied to
\(f(t)=\Xi(t/\sqrt X)/t\) gives

\[
 |c_X|\leq \sum_{r\geq0}|f(4r+1)-f(4r+3)|
 \ll_\Xi X^{-1/2}.                                         \tag{3.1}
\]

Summing \(A(n)=\mathfrak D(n)-\mathfrak D(n-1)+c_X\) over
\(\mathbb Z\), shifting the second sum, and using the exact sampled zero
mode \(\sum_nW_n=0\), gives

\[
 \sum_nA(n)W_n=\sum_n\mathfrak D(n)(W_n-W_{n+1}).
\]

On \(n\leq0\), \(\mathfrak D\) grows only affinely while \(W_n\) is a
Schwartz tail a distance \(\asymp X/T\) from its center.  Removing that
tail gives (2.3).  The sign is therefore \(W_n-W_{n+1}\), not its
negative.

For the thin-hyperbola formula, the condition \(v<a\sqrt X\leq j\) means
that \((n_0,n_0+v]\) contains at most one multiple of each supported
\(j\).  Hence the floor increment is \(C_j(v)\in\{0,1\}\).  Pair
\(j=4r+1\) with \(j+2=4r+3\).  Writing \(\Xi_j=\Xi(j/\sqrt X)\),

\[
 \Xi_jC_j-\Xi_{j+2}C_{j+2}
 =\Xi_j(C_j-C_{j+2})+(\Xi_j-\Xi_{j+2})C_{j+2}.
\]

The second term sums to \(O_\Xi(1)\), because
\(\sum_r|\Xi_{4r+1}-\Xi_{4r+3}|\ll_\Xi1\); zero extension of \(\Xi\)
owns both support edges.  The subtracted linear terms total
\(-vc_X=O_\Xi(vX^{-1/2})\) by (3.1).  This proves (1.1), including all
cutoff rows.  It also proves that \(C_j-C_{j+2}\in\{-1,0,1\}\): it is
the signed indicator of the symmetric difference of the two crossing
events.

Fourier or Vaaler expansion of the fractional parts does not close this
gap.  It produces jointly summed phases \(e(kn_0/j)\), while its positive
Fejer residual is itself a near-rational crossing count.  Taking that
residual absolutely can retain the full \(T X^{o(1)}\) capacity.  Thus a
truncation parameter alone cannot manufacture the required \(H/L\) gain.

## 4. First doubtful or unproved step

The first unproved step is a uniform estimate for the unmatched-row sum
in (1.1), or directly for its convolution against
\(W_n-W_{n+1}\), of size \(O(X^{1/4+\varepsilon})\) for
\(|v|\lesssim TX^\eta\).  Periodicity controls the smooth main term and
matched pairs, but it gives no deterministic bound for how often exactly
one of \(j,j+2\) crosses the moving hyperbola.

This is not presently a known short-divisor theorem.  It has the same
\(H/L\) deficit as PSC and is a separable fixed-interior test case, but it
is not equivalent to PSC: PSC retains two offset fibers and the full
actual divisor-dependent symbol.  Conversely, LCD controls neither the
sharp \(j=\sqrt X\) half-saddle nor the other cone modules.

## 5. Required controls and outcomes

- **Abel normalization: pass after correction.**  The affine extension
  (2.1) is essential.  Substituting negative integers in (2.2) would not
  justify (2.3).
- **Integral endpoint: pass with scope.**  Equations (1.1) and the binary
  crossing interpretation require integral \(v\).  Real endpoints retain
  an explicit fractional linear term.
- **Period-four pairing: pass/no-go.**  Matched crossings cancel; every
  unmatched pair contributes exactly \(0\) or \(\pm1\), up to the bounded
  smooth-cutoff commutator.
- **Exact products and fourth powers: target-safe but hostile.**  At
  \(v=0\), \(\mathfrak D=0\).  For a positive interval, a divisor
  \(j\mid n_0\) does not cross again until displacement \(j>T X^\eta\)
  in the packet's range.  For negative displacement, exact products may
  occur at the endpoint, but their total is divisor-bounded
  \(X^{o(1)}\).  If \(X\) is a fourth power, reciprocal Fourier phases
  can nevertheless be rationally coherent, so a generic irrationality or
  derivative-gap argument is invalid.  No coherent unmatched mass above
  the target is proved; hence this is not a counterexample to LCD.
- **Target power: pass.**  At \(\nu=2/5\), the needed gain is exactly
  \(X^{1/20}=H/L\), not merely a logarithm.
- **Full-cone scope: fail for promotion.**  Even LCD would leave the sharp
  saddle, lower \(j\)-scales, stationary entry/exit, negative frequencies,
  and subtraction/boundary recombination.

## 6. Dependencies, sources, and hypothesis matching

Repository dependencies read were `protocol.md`,
`state/proof_obligations.yml`, `state/active_campaign.yml`, the Round-65
derivation packet and assigned brief, and
`rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`.
The graph hash in the campaign plan is
`3a797e6c20eadee4a0030d9d405b62661cc96e256ace7b99b840b25b2423ee80`.
No other Round-65 report was read.

Primary-source audit:

1. A. Ivic and W. Zhai, *On the Dirichlet divisor problem in short
   intervals*, [arXiv:1209.0872](https://arxiv.org/abs/1209.0872), treats
   differences of the classical complete error \(\Delta(x+U)-\Delta(x)\)
   and important mean-square/maximal averages.  It does not retain the
   moving truncated divisor leg \(\Xi(j/\sqrt X)\chi_4(j)\) at one
   prescribed center.
2. D. Banerjee and K. Khurana, *Character analogues of Cohen type
   identities and related Voronoi summation formulas*,
   [arXiv:2306.12399](https://arxiv.org/abs/2306.12399), transforms
   complete twisted divisor convolutions such as
   \(\sum_{d\mid n}\chi(d)\).  The \(X\)-dependent truncation of one
   divisor leg destroys that coefficient class, and the source supplies a
   transformation rather than LCD.
3. S. Bettin and V. Chandee, *Trilinear forms with Kloosterman
   fractions*, [arXiv:1502.00769](https://arxiv.org/abs/1502.00769),
   estimates separable forms containing
   \(e(a\overline m/n)\) under coprimality.  The phase arising here is
   \(e(kn_0/j)\), with a moving crossing selector and no modular inverse;
   its Theorems 1--2 therefore do not apply.
4. K. Matomaki, M. Radziwill, X. Shao, T. Tao, and J. Teravainen,
   *Higher uniformity of arithmetic functions in short intervals II.
   Almost all intervals*, Invent. Math. 244 (2026),
   [article](https://doi.org/10.1007/s00222-026-01408-6), gives strong
   results for \(d_k-d_k^\sharp\) outside an exceptional set of centers.
   LCD is required at the prescribed center \(n_0=\lfloor X\rfloor\), for
   an \(X\)-dependent truncated convolution rather than \(d_k\); the
   exceptional-center and coefficient hypotheses both fail to match.

No external theorem is imported as a proof step.

## 7. Recommended state effect

**Promote only a scoped internal reduction/no-go:** the corrected affine
Abel identity and the exact period-four unmatched-row formula (1.1) are
valid.  Record that elementary period-four pairing, Vaaler expansion, and
the audited short-divisor/Voronoi/Kloosterman theorems do not supply the
\(H/L\) gain.

**Retain open** LCD, its weaker wavelet-weighted form, PSC, GAR, M9-M1,
M9, and the Gauss-circle target.  No radial interval and no exponent
improvement are proved.
