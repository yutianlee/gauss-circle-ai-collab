# Conductor source and seam audit

Campaign: `m9-endpoint-fixed-profile-attack`  
Round: 6  
Role: conductor review  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

## Result

The three discovery reports are mutually consistent after scope correction.
They do not prove the balanced endpoint. They isolate two candidates for
independent validation:

1. an explicit exact dyadic partition with uniform discrete BV, sampled
   \(\ell^1\) mass, and a single hard endpoint jump;
2. a signed small-gcd quarter-resonance packet that is exactly equivalent to
   the remaining smooth balanced dual sum after the large-gcd sector is
   removed.

The fixed-profile annulus result is only a no-go for classwise or absolute
estimation. Its large subtotal is not a lower bound for the full signed sum.

## Primary-source check

Proposition 5 of E. Kowalski, O. Robert, and J. Wu,
[*Small gaps in coefficients of L-functions and B-free numbers in small
intervals*](https://arxiv.org/abs/math/0507001), states for
\(\alpha,\beta\notin\{0,1\}\), \(\mathsf X>0\), \(M,N\ge1\), and separated
coefficients of modulus at most one that

\[
S(M,N)\ll_\varepsilon
\bigl((\mathsf X M^6N^6)^{1/8}+M^{1/2}N+MN^{3/4}
+\mathsf X^{-1/2}MN\bigr)(MN)^\varepsilon.
\]

The hypotheses and all four terms were checked directly in the primary PDF.
With \(\alpha=\beta=1/2\), \(M\asymp N\asymp L\), and
\(\mathsf X\asymp RL\), it gives

\[
R^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+R^{-1/2}L^{3/2},
\]

up to \(X^\varepsilon\). It therefore does not prove the
\(L^{3/2}\) target. A fixed smooth two-variable symbol may be separated by
an absolutely summable Fourier expansion; this preserves \(\chi_4(h)\) in
one separated coefficient but does not improve the theorem.

The Robert--Sargos spacing theorem is used only as an unsigned explanation of
the large-sieve input, not as a character-sensitive endpoint theorem. No
external theorem is proposed for graph promotion in this round.

## Algebraic seam checks

- The telescoping profile identity is correct on every integer
  \(1\le d\le\lfloor\sqrt X\rfloor\). Interior blocks are full smooth
  rescalings; the top block has one genuine jump at the finite endpoint.
- The inactive denominator range is \(O(X^{1/4})\) by termwise boundedness;
  this transfer must remain explicit in any later assembly.
- The exact product-energy count \(\sum_m r_L(m)^2\ll L^2\log L\), the
  square and near-square counts, and the large-gcd absolute bound have the
  correct scales.
- In the gcd factorization \(h=ga,k=gb\), the identity
  \(\chi_4(h)=\chi_4(g)\chi_4(a)\) holds on the surviving odd \(h\)-support.
  Poisson summation in \(g\) produces the stated difference of the
  \(1/4\)- and \(3/4\)-packets.
- The proposed packet estimate remains unproved. Voronoi returns a first
  product annulus whose trivial estimate is the already known
  \(R^{1/2}L^{1/2}\) envelope, so it supplies no hidden gain.

## First doubtful steps

The discovery reports have not received the protocol-required routed
validation. In particular:

- the profile construction needs an independent statement-only
  rederivation before it can alter the graph;
- the exact packet reduction and its signs need a second independent
  derivation;
- the fixed-profile annulus and local square-transition lemmas need a hostile
  line audit, especially their endpoint scope and the distinction between a
  subtotal and the full signed sum.

## State recommendation

Close Round 6 with no graph mutation. Retain the profile certificate and
packet reduction as candidates, retain the classwise annulus lemma as a
scoped obstruction, and begin a separate seam-validation round. Do not
promote `M9-M2`, endpoint uniformity, or the Gauss-circle target.
