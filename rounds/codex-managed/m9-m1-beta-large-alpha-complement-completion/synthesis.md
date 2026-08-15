# Round 46 synthesis: exact partition closes; quantitative nonsaddle seam remains

Campaign: `m9-m1-beta-large-alpha-complement-completion`  
Round type: beta large-alpha complement completion  
Graph SHA-256 before patch:
`295fbe40d51001a263c0740930b476599f04c35afbc7ca159fb9fa819d204739`

## Conductor decision

Round 46 proves the finite nonnegative positive-line partition but does
not prove the target-sized nonsaddle completion or the full localization
certificate.

The preliminary normalized weights are not geometrically subordinate:
at (t=|\alpha|/\lambda=1), half of their mass lies in the proposed
outer class.  A second finite nonnegative partition
(c_0+c_1+c_\infty=1), with

\[
 \operatorname{supp}c_0\subset[0,3/4],\qquad
 \operatorname{supp}c_1\Subset(2/3,3/2),\qquad
 \operatorname{supp}c_\infty\subset[4/3,\infty),
\]

repairs this exactly.  Multiplying it by the preliminary weights and a
signed-origin partition supported inside the zero set of
(1-\chi_0) gives a smooth finite nonnegative refinement summing
pointwise to (1-\chi_0).  The inner and outer aggregates satisfy

\[
 |\Psi'|\ge\log(4/3),
\]

and all unsafe collars belong to the middle aggregate.

This is not yet a literal match to the accepted Round-41 cells.  The
repaired middle aggregate has value one at (t=1), whereas the frozen
preliminary middle weight has value one half.  Round 41 states a
fixed-ratio saddle/entry/exit theorem but exposes neither the exact cutoff
family nor a cutoff-invariance theorem.  Support compatibility is not an
antecedent identity.

## Corrected nonsaddle target

A nonsaddle cell must be estimated directly on the returned positive-line
radial amplitude.  It is incorrect to multiply it by the Round-41
stationary numerator or to demand the local saddle
(\lambda^{-2}) symbol norm.  After forming the hard-top signed Cauchy
section, one may integrate the (L)-phase by parts on the repaired
supports.  The fixed (\chi_0'\)-collar is compact and must be estimated
directly.  The exact remaining analytic input is a global quantitative
theorem for the complete signed section and smooth shares, including:

- value and one (x)-derivative;
- grouped (L)-variation of (S) and (\alpha S);
- every moving finite-section trace;
- vanishing of the value and (x)-derivative outer boundary terms;
- the actual raw (h,q,D_j,x), radial-BV, floor, star, character, and
  external-factor ledger.

Round 38 proves fixed-(X) tail existence only.  Round 41 is quantitative
only on fixed-ratio saddle/entry/exit cells.  Round 45 proves the particular
compact (\chi_0)-terminal only.  None proves this global nonsaddle
theorem.

## Validation outcome

The clean statement-only report independently constructs the partition and
correctly refutes any amplitude-free inference from the phase identities.
The clean hostile audit corrects the normalization: no saddle numerator or
artificial (\lambda)-gain belongs in the raw nonsaddle ledger, and the
fixed (\chi_0'\)-collar is not itself a power obstruction.  The clean
discovery report proves the same partition and identifies the missing
global outer symbol theorem; its stronger initial fixed-collar no-go is not
accepted.  The first discovery and hostile runs were stopped after
disclosing context contamination and are not evidence.

No numerical experiment or external theorem was used.  The allocation was
100% analytical/algebraic.

## State effect

- Create and promote a scoped exact subordinate positive-line alpha
  partition reduction.
- Retain the positive-line alpha-localization certificate open; revise its
  next action to the global direct nonsaddle signed-section/radial-BV theorem
  and literal Round-41 cutoff coverage.
- Retain the aggregate double-bounded node and complete beta-transition
  assembly open.
- Record that the preliminary normalized outer weight is not nonsaddle,
  support compatibility does not prove a literal Round-41 match, and a
  saddle stationary numerator must not be imported into a nonsaddle cell.
- Keep M9-M1, M9, and the Gauss-circle target open.

Graph SHA-256 after the applied Round-46 patch:
`50afffd106f12da5d4b1d6aba6e15a28782f9c364f8960a084ca611a7a42cf0d`.
