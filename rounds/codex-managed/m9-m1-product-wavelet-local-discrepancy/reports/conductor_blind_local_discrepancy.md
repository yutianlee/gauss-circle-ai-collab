# Independent local-discrepancy rederivation

## 1. Result

The corrected all-integer Abel reduction is exact. Its weakest sufficient
conclusion is the wavelet-weighted discrepancy bound itself; pointwise LCD
is stronger. Elementary period-four pairing and Fourier expansion do not
prove either estimate.

## 2. Exact statement and hypotheses

Let \(A(n)=A_{X,\Xi}(n)\) for \(n\geq1\) and \(A(n)=0\) for
\(n\leq0\). Let \(\widetilde B(n)=\sum_{m\leq n}A(m)\), so
\(\widetilde B(n)=0\) for \(n\leq0\). With
\(n_0=\lfloor X\rfloor\), define

\[
 \widetilde{\mathfrak D}(n)
 =\widetilde B(n)-B_X(n_0)-c_X(n-n_0).
\]

Then

\[
 \sum_{n\in\mathbb Z}\widetilde{\mathfrak D}(n)(W_n-W_{n+1})
 =\sum_{n\geq1}A(n)W_n.
\tag{2.1}
\]

## 3. Proof or derivation

The difference of \(\widetilde{\mathfrak D}\) is \(A(n)-c_X\).
Absolute convergence permits the index shift, and the sampled zero mode
\(\sum_nW_n=0\) kills the constant \(c_X\), proving (2.1). Restricting
the discrepancy to positive integers without the affine/nonpositive
extension would leave boundary terms.

Period-four Abel summation gives \(c_X\ll_\Xi X^{-1/2}\). For integral
\(v\),

\[
 \mathfrak D_X(n_0+v;n_0)
 =\sum_j\chi_4(j)\Xi(j/\sqrt X)
 \left(\{n_0/j\}-\{(n_0+v)/j\}\right).
\]

For positive \(v\) shorter than every supported \(j\), this is the
oriented crossing indicator minus \(v/j\); negative \(v\) uses reversed
oriented crossings.

## 4. First doubtful or unproved step

The weakest sufficient unproved assertion is

\[
 \left|\sum_n\widetilde{\mathfrak D}(n)(W_n-W_{n+1})\right|
 \ll_\varepsilon X^{1/4+\varepsilon}.
\tag{4.1}
\]

The pointwise LCD estimate on \(|v|\lesssim TX^\eta\), together with
Schwartz tails, implies (4.1) but is not necessary.

## 5. Required control test and outcome

- All-integer extension and Abel sign: pass.
- Period-four main term: pass, \(c_X\ll X^{-1/2}\).
- Positive/negative orientation: pass after treating them separately.
- Character pairing: leaves discontinuous unmatched crossings with
  capacity \(O(T)\).
- Fourier expansion: exact-product resonances and a diagonal/truncation
  remainder remain unless a new joint reciprocal-phase theorem is used.
- Zero moments: insufficient for (4.1).

## 6. Dependencies and exact artifacts used

The independent agent read only the Round-65 packet and its assigned
brief. It supplied this verdict in a final message after failing to
materialize its file; the conductor transcribed it without adding a new
claim. No numerical experiment or external theorem was used.

## 7. Recommended state effect

Promote the corrected Abel identity only. Retain (4.1), LCD, and every
downstream theorem open. This report is an independent statement-only
rederivation for the algebraic seam, but not evidence for the missing
estimate.
