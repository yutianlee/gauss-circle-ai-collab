# Round 42 synthesis: compact-cell candidate and validation gap

Campaign: m9-m1-beta-double-bounded-cell

Graph SHA-256 before patch:
774b64709170bd09a99200f7f1f5cdf237fa6c712820394f309c6b7e58e177f8

## Conductor decision

Do not promote the complete double-bounded beta cell in this round.

The discovery proof and hostile audit independently obtain the same
target-sized estimate. They agree on the exact gamma unit phase, signed
Plemelj diagonal, one \(x\)-derivative, absolute \(h,q\) sums, dyadic
scale ledger, full radial endpoint coefficients, and a direct local
masked-endpoint estimate. Conductor calculations verify those local
formulas and find no exponent or sign defect.

The assigned statement-only task did not materialize. A replacement
statement-only audit correctly rejected citing the unmasked global
endpoint theorem for a beta-masked trace, but its frozen packet did not
contain the explicit post-routing amplitude needed to test the direct
local estimate. A second fast isolated audit proved the conditional
radial lemma and accepted the local compact endpoint majorant, but likewise
could not certify the finite connector/module and \(j\)-scale assembly
from the packet alone.

The protocol requires an important lemma to pass isolated rederivation.
Therefore the full compact cell remains open. Round 42 promotes only the
exact conditional radial-BV reduction and records the explicit cell as
the next open obligation.

## Accepted conditional kernel

If the exact post-routing compact amplitude satisfies

\[
\sup_{1\le x\le N_X}|\mathcal A(x)|
+\int_1^{N_X}|\mathcal A'(x)|\,dx
\ll_\varepsilon X^\varepsilon,
\]

then

\[
\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
\mathcal A(x)\,dx\ll_\varepsilon X^\varepsilon.
\]

The exact integration-by-parts identity has full radial endpoint
coefficients. Existing stars remain inside the endpoint values; no new
half-weight is created.

## Candidate compact estimate

For the explicit functional in
proofs/kernels/m9_m1_beta_double_bounded_cell_candidate.md, discovery and
hostile review prove

\[
\sup_x\{|\mathcal A(x)|+x|\mathcal A'(x)|\}
\ll\log^C(2X).
\]

The mechanism is:

1. compact \(\beta\) and \(\alpha=L+\beta\) make \(L\) compact;
2. the exact gamma quotient, including
   \(e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}\), is bounded without
   Stirling;
3. the hard top is evaluated as a signed diagonal plus an absolutely
   integrable divided difference;
4. the exact \(x\)-derivative preserves the diagonal cancellation;
5. \(r,p>1\), with \(r-1>b/2\), so \(h,q\) and fixed logarithmic
   connector weights cost only polylogarithms;
6. the actual dyadic scale mass is polylogarithmic.

The direct endpoint bound does not identify the beta-masked endpoint with
the global endpoint module. Equivalently, on the fixed terminal line use
\(R_1=G-E_1\) and bound both masked terms without another contour shift or
residue extraction.

## Failure ledger

Reject:

- absolute values before signed top recombination;
- omission of the gamma unit phase;
- omission of \(L,\beta\) phase derivatives;
- half weight at a continuous radial IBP endpoint;
- use of the unmasked endpoint theorem for one beta-masked trace;
- inference of the finite connector/module assembly from an undefined
  post-routing amplitude.

No numerical experiment or external theorem was used. The allocation was
100% analytical/algebraic.

## State effect

- Promote the conditional radial-BV reduction.
- Create the explicit double-bounded cell bound as an open obligation.
- Keep the complete physical-height beta symbol, regular finite part,
  logarithmic beta kernel, and beta-transition assembly open.
- Run a narrow explicit-amplitude validation round before returning to
  the alpha-bounded zeta-high branch.
- Keep M9-M1, M9-M2, M9, and the Gauss-circle target open.

