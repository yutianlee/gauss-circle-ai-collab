# Round 158 conductor audit: exact strict survivor and boundary weight

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Round: 158
- Role: conductor algebraic control; candidate evidence only
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f

## 1. Result

The full-frequency moving-cell trace has an exact selected-coordinate
description in which the quotient carrying the character is not the
argument sampled by the boundary-frozen profile.  If

\[
 k_\ell=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r_\ell=k_\ell^2-N\ell,
\]

then the positive and negative strict traces select different signed
subsets of the same residual sequence \(r_\ell\).  Their coefficients
sample

\[
 \frac{k_\ell^2-k_\ell+1}{N}
 \quad\hbox{and}\quad
 \frac{k_\ell^2+k_\ell}{N},
\]

respectively, whereas the arithmetic sign is \(\chi _4(\ell)\).
Replacing either boundary argument by \(\ell\) is therefore unlawful
without a separate statement about the inherited half-open
off-congruence extension.

The trace is localized to \(V\asymp K=\sqrt{NM}\), but this gives no
target bound: there its unsigned support may still have order \(M\).
An explicit infinite family below proves that the endpoint
congruences do not exhaust the trace.  It is a strict-survivor control,
not a signed lower bound and not an impossibility theorem for every
possible joint method.

## 2. Exact statement and hypotheses

Let \(J_+=[a_+,b_+]\) and \(J_-=[a_-,b_-]\) be consecutive integer
blocks, with \(J_+\) positive and \(J_-\) negative.  In the
full-frequency trace put

\[
 k=j+1\quad\hbox{on }J_+,\qquad k=-j\quad\hbox{on }J_-.
\]

For every selected term define

\[
 \ell=\frac{k^2-s}{N},\qquad r_\ell=k^2-N\ell=s.
\tag{158.CA1}
\]

The nearest-cell inequalities are

\[
 -k\le r_\ell\le k-1.
\tag{158.CA2}
\]

Assume the inherited profile is supported in a fixed dilation of
\(M\), has zero-extended supremum plus variation
\(O_\varepsilon(M^{-3/4}X^\varepsilon)\), and retains its actual
off-congruence half-open convention.

## 3. Proof or derivation

### 3.1 Exact strict selectors

The positive trace has

\[
 a_+\le j\le b_+-1,\qquad a_+\le s\le j.
\]

Since \(j=k-1\), its endpoint is \(s=k-1\), and its strict part is

\[
 a_++1\le k\le b_+,\qquad
 a_+\le r_\ell\le k-2.
\tag{158.CA3}
\]

Its coefficient is exactly

\[
\begin{aligned}
 F_{k-1}(k)
 &=
 w_U\!\left(\frac{k^2-k+1}{N}\right)
 e\!\left(\sqrt{k^2-k+1}-k\right),
\end{aligned}
\tag{158.CA4}
\]

with every actual support and transition selector retained.

The negative trace has

\[
 a_-+1\le j\le b_-,\qquad j\le s\le b_-.
\]

Since \(j=-k\), its endpoint is \(s=-k\), and its strict part is

\[
 -b_-\le k\le-a_--1,\qquad
 -k+1\le r_\ell\le b_-.
\tag{158.CA5}
\]

Its coefficient is exactly

\[
\begin{aligned}
 F_{-k}(k)
 &=
 w_U\!\left(\frac{k^2+k}{N}\right)
 e\!\left(\sqrt{k^2+k}-k\right).
\end{aligned}
\tag{158.CA6}
\]

Equations (158.CA3) and (158.CA5) delete precisely the two endpoint
faces \(r_\ell=k-1\) and \(r_\ell=-k\).  They do not delete the
interior of the nearest cell.

### 3.2 Quotient and boundary-profile arguments

For a positive strict term,

\[
 \ell-\frac{k^2-k+1}{N}
 =\frac{k-1-r_\ell}{N}\in\left(0,\frac{2k}{N}\right),
\tag{158.CA7}
\]

while for a negative strict term,

\[
 \frac{k^2+k}{N}-\ell
 =\frac{k+r_\ell}{N}\in\left(0,\frac{2k}{N}\right).
\tag{158.CA8}
\]

Thus both boundary arguments lie within one unit of \(\ell\), because
\(2k<N\) in the accepted range, but neither equality is true in the
strict trace.  A choice of left- or right-continuous
piecewise-constant extension can align one side with one adjacent
integer sample; it does not justify replacing both literal
coefficients by one common value.

### 3.3 Top-block localization and its exact limitation

On the support of (158.CA4) or (158.CA6),

\[
 \frac{k^2+O(k)}{N}\asymp M.
\]

Hence \(k\asymp K\).  Since the moving atom also has
\(k\asymp V\), the cell trace vanishes outside the fixed-comparability
top region \(V\asymp K\), with constants inherited from the literal
profile support.

This is only localization.  In the top region the accepted assumptions
\(M\le N^{1/2}\) give \(K\gg M\), so

\[
 \min(M,V)=M.
\]

The unsigned trace capacity is therefore
\(M\cdot M^{-3/4}=M^{1/4}\), whereas genuine square-root cancellation
would give the stronger \(M^{-1/4}\).  The actual scalar target is
\(O_\varepsilon(X^\varepsilon)\), equivalently raw signed mass
\(O_\varepsilon(M^{3/4}X^\varepsilon)\).  Top localization supplies
neither threshold.

### 3.4 Infinite strict-survivor control

Let \(L=2^h\) with \(h\ge3\), and put

\[
\begin{aligned}
 V&=L^2,&
 M=\ell&=L+1,&
 t&=L+4,\\
 k&=(L+1)(L+4),&
 s&=L(L+1),&
 N&=(L+1)(L+4)^2-L.
\end{aligned}
\tag{158.CA9}
\]

Then

\[
 N\ell=k^2-s.
\tag{158.CA10}
\]

Moreover,

\[
 V<s<k-1,\qquad V<k-1\le2V
\tag{158.CA11}
\]

for all sufficiently large \(L\).  Thus \(j=k-1\) and \(s\) lie in
the same positive dyadic block, and \(s<j\) is a strict prefix term.
The cell inequalities hold, so \(k\) is the unique nearest integer to
\(\sqrt{N\ell}\).  Since \(\ell=L+1\equiv1\pmod4\),

\[
 G_N(k^2-s)=\chi _4(\ell)=1.
\tag{158.CA12}
\]

At the same time,

\[
 0<k-1-s=4L+3<N,
\tag{158.CA13}
\]

so \(N\nmid k^2-k+1\): this point is not a root of the positive
endpoint polynomial.  Finally,

\[
 \ell-\frac{k^2-k+1}{N}=\frac{4L+3}{N}\in(0,1),
\tag{158.CA14}
\]

placing the boundary-profile argument in the same fixed-dilate
\(M\asymp L\) region as \(\ell\).  Consequently the strict selector
can be active for an admissible nonzero BV profile although the
endpoint selector is inactive.

### 3.5 What the control does not prove

The character \(\chi _4(\ell)\) has bounded partial sums on consecutive
\(\ell\)-intervals.  The strict conditions (158.CA3) and (158.CA5),
however, cut those intervals by the nearest-square residual
\(r_\ell\).  No bounded number of \(\ell\)-intervals, bounded variation
of that residual mask, or positive/negative coefficient identity has
been proved.  In particular, no argument here gives even the raw
\(M^{3/4}X^\varepsilon\) estimate needed for the scalar target.  The
explicit family proves survival, not large signed mass.

## 4. First doubtful or unproved step

The first unproved estimate is cancellation in

\[
\begin{aligned}
 \sum_{\ell}\chi _4(\ell)\bigl[
 &\mathbf 1_{\mathrm{(158.CA3)}}F_{k_\ell-1}(k_\ell)\\
 &+\mathbf 1_{\mathrm{(158.CA5)}}F_{-k_\ell}(k_\ell)
 \bigr].
\end{aligned}
\tag{158.CA15}
\]

Neither endpoint root counting, top-block localization, ordinary
\(\chi _4\) partial summation, nor equality of the two boundary
profiles proves the required \(O_\varepsilon(X^\varepsilon)\) weighted
bound for (158.CA15).  A square-root raw estimate would be sufficient
but is stronger than required.

## 5. Required control tests and outcomes

- Exact strict positive and negative inequalities: pass in
  (158.CA3) and (158.CA5).
- Character quotient versus profile argument: separated in
  (158.CA4)--(158.CA8).
- Endpoint deletion: only \(r_\ell=k-1\) and \(r_\ell=-k\) are
  removed.
- Infinite strict-survivor family: pass algebraically in
  (158.CA9)--(158.CA14).
- Top localization: pass as support localization; fail as a target
  estimate.
- Positive/negative pairing: no exact coefficient or selector pairing
  proved.
- Target raw \(M^{3/4}\) estimate: open; square-root raw \(M^{1/2}\)
  would be a stronger sufficient input.
- Profile bulk and every downstream owner: unchanged and open.
- Numerical work: none used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- strategy/round158_d1_paired_interior_cell_trace_strategy.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/barrier_packet.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/candidates/conductor_round158_cell_trace_seed.md
- proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md

## 7. Recommended state effect

Do not patch state from this conductor control alone.  Subject to
independent review, retain the exact strict selectors, the distinction
between quotient and boundary-profile arguments, top-block
localization, and the explicit endpoint-route survivor.  Do not promote
a trace target, a paired-matrix target, or a global exponent gain.
