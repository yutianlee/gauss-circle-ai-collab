# Round 45 synthesis: compact beta core closes; complement coverage remains

Campaign: `m9-m1-beta-positive-line-localization`  
Round type: beta positive-line localization  
Graph SHA-256 before patch:
`45b0c54cad320dc5a08b1129f5a7b4776f6b9e321b3c1c7c9fa738bcb85c5196`

## Conductor decision

Round 45 proves the local analytic core but does not promote the full
positive-line localization certificate.

After all sixteen finite product Cauchy--Green cells are recombined, the
central multiplier \(\psi(\beta)\chi _0(\alpha)\) produces exactly three
terminal selectors: the \(j=0\) singular top under signed Plemelj, the
\(j=0\) regular top, and the \(j\ge1\) interior profiles under ordinary
integration. The exact compact amplitude satisfies

\[
 \sup_{1\le x\le N_X}
 \left(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\right)
 \ll\log^C(2X).
\]

The crucial derivative identity retains the complete x-phase:

\[
 x\partial_x\{g(L,\beta)p(\nu)\}
 =-i\left(\frac{L+\nu}{2}+\beta\right)g(L,\beta)p(\nu),
\]

whose multiplier is bounded after division by the radial denominator.
The Plemelj remainder is differentiated as one divided difference before
absolute values. Absolute \(h,q\) convergence and the dyadic scale sum
cost only a polylogarithm. Composed with the accepted radial-BV reduction,
the central terminal is physically \(O(X^{1/4}\log^C X)\).

The separately owned artificial residue is also target-safe. Its local
orientation and exact radial coefficient are

\[
 \operatorname {Res}_sR_{1,v}(1-s)=+\pi i\sqrt X I_1(0),
 \qquad
 \pi i\sqrt X I_1(0)=e(\sqrt{XN_X})-e(\sqrt X).
\]

The arithmetic factor stays recombined as \(\zeta L(\chi _4)\). Compact
beta height bounds the zeta factor, period-four Abel summation gives at
most linear character-height growth, and cubic height decay makes the
complementary artificial tail integrable. Both alpha shares are therefore
\(O(\log^C X)\) before the external factor.

## Validation outcome

The discovery proof, clean mathematical statement-only rederivation, and
hostile audit agree on the compact Plemelj normalization, x derivative,
selectors, scale sums, artificial residue orientation, exact endpoint
coefficient, arithmetic chamber, and one-count external normalization.
No numerical experiment or external theorem was used.

The same three reports also expose a genuine coverage gap in the frozen
large-alpha interface. The accepted Round-41 node proves the signed
large-alpha saddle, entry, and exit package, but it does not exhibit a
finite same-antecedent family \(\eta_\tau\) satisfying

\[
 \sum_\tau\eta_\tau=1-\chi _0
\]

or quantitatively bound every nonsaddle remainder in that complement.
The equality with the positive-line complement is immediate if that
antecedent is supplied, but it cannot be promoted from the packet alone.

## State effect

- Create and promote a scoped lemma for the exact compact terminal and
  both artificial-residue alpha shares.
- Retain `M9-M1-beta-positive-line-alpha-localization-certificate` open,
  narrowing it to the identical-antecedent partition and nonsaddle
  coverage seam.
- Retain the aggregate `M9-M1-beta-double-bounded-cell-bound` open because
  its current statement requires that full certificate; record that its
  analytic compact component is now closed.
- Retain complete beta-transition assembly, the alpha-bounded branch,
  M9-M1, M9, and the Gauss-circle target open.

Round 46 should construct and audit the exact positive-line
\(1-\chi _0\) partition and prove the residual nonsaddle completion.

Graph SHA-256 after the applied Round-45 patch:
`295fbe40d51001a263c0740930b476599f04c35afbc7ca159fb9fa819d204739`.
