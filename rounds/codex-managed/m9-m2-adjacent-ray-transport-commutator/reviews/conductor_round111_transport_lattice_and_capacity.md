# Conductor review: transport, discrete lattice, and capacity

Campaign: m9-m2-adjacent-ray-transport-commutator

Starting graph SHA-256:
c93f14d6790341b792b54bbaa7ccb96c211741d666729f08addc80fb91d1b759

## Exact continuous transport

Let \(b=a+2q\),

\[
 \delta_q=\sqrt b-\sqrt a,\qquad
 \lambda_q=\left({\delta_q\over\delta_{q+1}}\right)^2.
\]

Writing

\[
 \rho_q={\delta_{q+1}-\delta_q\over\delta_q}
 ={\sqrt b+\sqrt a\over q(\sqrt{b+2}+\sqrt b)}
\]

gives \(\lambda_q=(1+\rho_q)^{-2}\) and
\(1-\lambda_q\asymp q^{-1}\). The map

\[
 T_q(x,k)=(\lambda_qx,k/\lambda_q)
\tag{111.C10}
\]

has determinant one and preserves

\[
 -J\sqrt g\,\delta_{q+1}\sqrt{\lambda_qx}
 =-J\sqrt g\,\delta_q\sqrt x,\quad
 (k/\lambda_q)(\lambda_qx)=kx,\quad
 {\Lambda_{q+1}\over k/\lambda_q}={\Lambda_q\over k}.
\tag{111.C11}
\]

There is no continuous Jacobian or metric gain.

## Exact pulled-back sampler

For a fixed compact cardinal extension \(H\),

\[
 \begin{aligned}
 \sum_nH_q(n)-\sum_nH_{q+1}(n)
 ={}&\sum_n\{H_q(n)-\lambda_qH_{q+1}(\lambda_qn)\}\\
 &+\lambda_q\sum_nH_{q+1}(\lambda_qn)-\sum_nH_{q+1}(n).
 \end{aligned}
\tag{111.C12}
\]

The second line is exactly

\[
 \lambda_q\sum_nH(\lambda_qn)-\sum_nH(n)
 =\sum_r\{\widehat H(r/\lambda_q)-\widehat H(r)\}.
\tag{111.C13}
\]

Equivalently,

\[
 \lambda_q\sum_n\delta_{\lambda_qn}(k)
 =\sum_re(rk/\lambda_q).
\tag{111.C14}
\]

The physical Jacobian is canceled by the changed lattice density. Rounding
the scaled lattice introduces an uncontrolled \(kx\)-phase error.

On a positive interval \(I\) of length \(K\), put

\[
 \mu_I=1_I\sum_n\delta_n,\qquad
 \nu_{I,\lambda}=1_I\lambda\sum_n\delta_{\lambda n}.
\]

If \(\lambda\) is irrational, their supports are disjoint and
\(\|\mu_I-\nu_{I,\lambda}\|_{\mathrm{TV}}=2K+O(1)\). If
\(\lambda=p/r<1\) is reduced, their common support is \(p\mathbb Z\) and

\[
 \|\mu_I-\nu_{I,\lambda}\|_{\mathrm{TV}}
 =2K-{2K\over r}+O(1)\asymp K.
\tag{111.C15}
\]

Thus \(\lambda_q=1+O(D^{-1})\) does not make the atomic commutator
\(O(K/D)\) in a coefficient-blind norm. This is not an actual signed lower
bound.

## Supports and carrier displacement

In a noncollapsed block

\[
 a\asymp b\asymp A,\quad q\asymp D,\quad
 g\asymp {L\over A},\quad k\asymp K\asymp {JD\over A},
\tag{111.C16}
\]

both reciprocal endpoints move by

\[
 \Delta k\asymp {K\over D}\asymp {J\over A}.
\tag{111.C17}
\]

The curvature width is \(K/L\), so one adjacent step crosses \(L/D\)
such widths. In the pullback convention of (111.C12), the neighbor
physical interval is

\[
 \left[{g(b+2)\over4\lambda_q},{ga\over\lambda_q}\right],
\]

and both mismatch widths against \([gb/4,ga]\) are \(\asymp L/D\). The
inverse-map convention in the hostile report is equivalent after scaling
by \(\lambda_q\).

The common-band carrier displacement is

\[
 \Delta\Theta_{q,g}(k)
 ={Xg(\delta_{q+1}^2-\delta_q^2)\over4k}
 \asymp {JL\over A}.
\tag{111.C18}
\]

It is not perturbatively \(O(D^{-1})\), while square, Pell, fourth-power,
or near-centre data can make it integral or nearly integral. Neither
Taylor smallness nor a uniform modular gap follows.

## Capacity ledger

The accepted fixed-\(q\) row scale is \(L^2/A\), with \(O(AD)\)
base/offset pairs. The coefficient-blind common-comb capacity is \(DL^2\).
For the endpoint slabs, the accepted coefficient and count give

\[
 AD\,{J\over A}\,{L\over A}\sqrt{AL\over JD}
 =L^2\sqrt\kappa,\qquad
 \kappa={JD\over AL}\ge D.
\tag{111.C19}
\]

Thus separate endpoint estimation loses at least \(D^{1/2}\). No fixed
positive-power \(D\)-range closes; only the already accepted
prescribed-polylogarithmic range can absorb the deficits.

## Scope and survivor

Jacobian, boundary-only, total-variation, coefficient-blind, and
perturbative transport arguments cannot supply the missing \(D\)-saving.
The result does not refute cancellation of the actual signed coefficient.
The smallest live object is the one-orientation signed common-band
scaled-comb correlation from (111.C13), kept jointly with its one-count
support and arithmetic slabs whenever separation destroys cancellation.

