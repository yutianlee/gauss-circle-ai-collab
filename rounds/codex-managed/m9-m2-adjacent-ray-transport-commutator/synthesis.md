# Round 111 synthesis: adjacent transport has a bulk lattice commutator

Campaign: m9-m2-adjacent-ray-transport-commutator

Starting graph SHA-256:
c93f14d6790341b792b54bbaa7ccb96c211741d666729f08addc80fb91d1b759

Resulting graph SHA-256 after the validated State Patch:
5c49f612b262b1191fe74642ddd8e5d6c70e04b34a59fb1473487d5b5132d747

## 1. Frozen objective

The round tested whether the adjacent primitive-ray parity high-pass,
combined with a phase-preserving dilation, proves the Round-75
off-diagonal, closes a positive-power \(q\)-shell, or exposes an exact
equal-capacity discrete defect.

Three orthogonal reports and two conductor reviews certify the finite
high-pass, one-count partition, sampler normalization, comb calculation,
support widths, carrier displacement, and capacity.

## 2. High-pass and one-count partition

For every finite zero-extended row,

\[
 2\sum_q(-1)^qf(q)
 =\sum_q(-1)^q\{f(q)-f(q+1)\}.
\tag{111.1}
\]

This uses one orientation and one outer \(2\Re\). A finite cutoff retains
\((-1)^{Q+1}f(Q+1)\), so no maximal theorem follows automatically.

A first-failure Boolean identity assigns zero extension, coprimality,
lifts, ceiling, reciprocal support, collars, entry/exit, scales, stars,
terminal, puncture, and metric atoms once. For odd \(a\),

\[
 1_{(a,a+2q)=1}=\sum_{d\mid a}\mu(d)1_{d\mid q},
\]

which preserves parity on odd-divisor progressions but has recurring
interior jumps. These are identities, not estimates.

## 3. Continuous transport

Put

\[
 \delta_q=\sqrt{a+2q}-\sqrt a,\qquad
 \lambda_q=\left({\delta_q\over\delta_{q+1}}\right)^2.
\]

Then \(1-\lambda_q\asymp q^{-1}\), and

\[
 T_q(x,k)=(\lambda_qx,k/\lambda_q)
\tag{111.2}
\]

has determinant one and preserves the radical phase, \(kx\), and
\(\Lambda_q/k\). For a compact cardinal extension \(H\), the exact
sampled comparison contains

\[
 \lambda_q\sum_nH(\lambda_qn)-\sum_nH(n)
 =\sum_r\{\widehat H(r/\lambda_q)-\widehat H(r)\}.
\tag{111.3}
\]

The physical Jacobian is canceled by the density of the scaled comb.

## 4. Bulk discrete obstruction

On a positive interval of length \(K\), the total-variation distance
between \(\sum\delta_n\) and
\(\lambda\sum\delta_{\lambda n}\) is \(2K+O(1)\) for irrational
\(\lambda\), and for reduced \(\lambda=p/r<1\) it is

\[
 2K-{2K\over r}+O(1)\asymp K.
\tag{111.4}
\]

Thus \(\lambda=1+O(D^{-1})\) does not make the atomic sampler
\(O(K/D)\). Rounding instead destroys exact \(kx\)-phase preservation.

The common-band carrier changes by

\[
 {Xg(\delta_{q+1}^2-\delta_q^2)\over4k}
 \asymp {JL\over A},
\tag{111.5}
\]

not by a perturbative \(D^{-1}\). Structured resonances prevent a uniform
modular gap. This is a coefficient-blind route obstruction, not an actual
signed lower bound.

## 5. Supports and capacity

For \(a\asymp A\), \(q\asymp D\), \(g\asymp L/A\), and
\(K\asymp JD/A\), reciprocal endpoints move by \(K/D=J/A\) and the
physical pullback slabs have width \(L/D\). They are not all fixed
Round-77 collars.

The coefficient-blind bulk capacity is \(DL^2\). Absolute endpoint
summation gives

\[
 L^2\sqrt\kappa,\qquad \kappa={JD\over AL}\ge D.
\tag{111.6}
\]

No fixed positive-power shell closes. Only the already accepted
prescribed-polylogarithmic rows absorb these losses.

## 6. Conductor decision

Promote the exact high-pass, one-count partition, determinant-one
transport, scaled-comb normalization, full coefficient-blind comb
capacity, support slabs, ceiling jump, and carrier displacement.

Reject claims of an automatic high-pass saving, a small comb from
\(1-\lambda_q\), a Jacobian gain, a boundary-only defect, fixed-collar
ownership of all slabs, phase-preserving rounding, or a uniform carrier
gap. Also reject the overclaim that comb total variation is an
actual-symbol lower bound.

The live object is the actual signed common-band scaled-comb correlation,
kept jointly with its one-count slabs when separation destroys
cancellation. It retains the original capacity.

## 7. Global status and next interface

No exponent changes. The strongest certified pointwise exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

and the strongest internal uniform exponent remains \(1/3\).

The hard signed cone, fixed-\(a\) Gram, balanced and unbalanced smooth M2
packets, M9-M2, M9-M1, endpoint uniformity, M9, and the quarter target
remain open. Since Round 111 is the speculative core in its three-round
block, the next round should be a deliverable/reconciliation round,
preferably an exact all-packet M9-M2 interface assembly.

