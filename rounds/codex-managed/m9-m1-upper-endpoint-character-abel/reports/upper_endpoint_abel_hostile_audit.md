# Hostile audit of the upper-endpoint \(q\)-Abel mechanism

## 1. Result

**PROMOTE, but only for the physical profile limit.** The proposed
fixed-\((j,h)\) estimate is correct:
\[
\sum_{q\ge1}\chi _4(q)q^{-3/4}
[w_j(2\sqrt{Xh/q})]^*\,\kappa_N(hq)
\ll_W Q_j(h)^{-3/4},\qquad
Q_j(h)=\frac{Xh}{D_j^2}, \tag{1}
\]
where \(\kappa_N(n)=1,\frac12,0\) according as \(n<N,n=N,n>N\).
Consequently the normalized physical upper endpoint is \(O_W(1)\), and
the external \(-(4/\pi)X^{1/4}\) factor makes it
\(O_W(X^{1/4})\), hence target-safe. This closes neither finite top
truncations nor the recombined arithmetic and transition operators.

## 2. Exact statement and hypotheses

Let \(y=\lfloor\sqrt X\rfloor\), \(D_j=2^{-j}y\),
\(H_j=\lfloor D_jX^{-1/4}\rfloor\), and
\(N=\lfloor16\sqrt X\rfloor\). In the accepted physical profile,
\[
\mathcal U_X=
\sum_{j=0}^{J}\sum_{h=1}^{H_j}
h^{-3/4}\Phi\!\left(\frac h{H_j+1}\right)
\sum_{q\ge1}\chi_4(q)q^{-3/4}
[w_j(d_{h,q})]^*\kappa_N(hq), \tag{2}
\]
\[
d_{h,q}=2\sqrt{Xh/q},\qquad
w_0(d)=W(d/y)\mathbf1_{d\le y},\quad
w_j(d)=W(d/D_j)\ (j\ge1).
\]
The upper boundary itself is \(e(\sqrt{XN})\mathcal U_X\); this phase has
modulus one.

## 3. Proof or derivation

The character is on \(q\), exactly as forced by the odd-lattice
stationary phase. Extending the sum from odd \(q\) to all positive
integers is harmless because \(\chi_4(q)=0\) for even \(q\), and
\[
\sup_T\left|\sum_{q\le T}\chi_4(q)\right|\le1. \tag{3}
\]

Fix \(j,h\), set \(Q=Xh/D_j^2\), and write \(r=q/Q\). For \(j\ge1\),
\[
q^{-3/4}w_j(d_{h,q})
=Q^{-3/4}\psi(r),\qquad
\psi(r)=r^{-3/4}W(2r^{-1/2}), \tag{4}
\]
where \(\psi\) is a fixed smooth BV function supported in
\([9/4,16]\). For \(j=0\), the fixed rescaled function is
\[
\psi_0(r)=r^{-3/4}W(2r^{-1/2})\mathbf1_{r\ge4}, \tag{5}
\]
supported in \([4,16]\), with one bounded jump at \(r=4\).
Neither proof assumes that \(W\) is monotone. Sampling an increasing
sequence cannot increase continuum total variation, so
\[
\sup_q|f_{j,h}(q)|+
\sum_q|f_{j,h}(q+1)-f_{j,h}(q)|
\ll_W Q^{-3/4}. \tag{6}
\]
Stationary stars at smooth support edges are zero because \(W\) vanishes
there. A top hard-edge half value or the single prefix half tie changes
(6) by at most \(O(Q^{-3/4})\). Discrete Abel summation using (3) proves
(1).

The product cutoff introduces no new moving edge. On profile support,
\[
q\le16Q,\qquad h\le H_j\le D_jX^{-1/4},
\]
hence
\[
hq\le\frac{16Xh^2}{D_j^2}\le16\sqrt X.
\]
Since \(hq\) is integral, \(hq\le N\); only equality can invoke
\(\kappa_N=\frac12\).

The Vaaler factor is uniformly bounded because \(\Phi\) extends
continuously to \([0,1]\). Applying (1) to (2) gives
\[
\begin{aligned}
|\mathcal U_X|
&\ll_W X^{-3/4}\sum_{j=0}^{J}D_j^{3/2}
\sum_{h\le H_j}h^{-3/2}\\
&\ll_W X^{-3/4}y^{3/2}
\sum_{j\ge0}2^{-3j/2}\ll_W1. \tag{7}
\end{aligned}
\]
There is no scale-count logarithm: the \(D_j^{3/2}\) weights form a
geometric series. The lowest active height \(H_j=1\) is harmless:
\(\Phi(1/2)=1/2\), \(Q\ge1\), and the \(h^{-3/2}\) sum remains bounded.

## 4. First doubtful or unproved step

The proof begins only after the accepted physical symmetric Perron/profile
limit. At finite top height \(U\), the truncated inverse
\[
\frac1{2\pi i}\int_{a-iU}^{a+iU}\widehat W_+(u)A^u\,du
\]
is not the compactly supported \(w_0\); it has Perron tails and no
established uniform sampled-\(q\) BV bound. Thus (7) cannot be promoted
uniformly in finite \(U\). For each fixed \(X\), however, the physical
sum is finite, so the already licensed termwise profile limit yields
(2). The recombined \(R_1\) arithmetic residue and both diagonal
transition traces remain wholly unestimated.

## 5. Required controls and outcomes

- **Character placement:** for \(X=y^2\), \(h=2,q=9\) is active in the
  top plateau for large \(y\). Its sign is \(\chi_4(9)=1\), whereas
  \(\chi_4(h)=0\); moving the character to \(h\) fails exactly.
- **Unsigned falsifier:** on the top plateau \(4Q\le q\le9Q\),
  replacing \(\chi_4\) by \(1\) gives size \(\asymp Q^{1/4}\), not
  \(Q^{-3/4}\). The saving uses period-four cancellation essentially.
- **Top seam:** with \(h\le H_0\), the hard equality is
  \(q=4hX/y^2\). For large \(y\) it lies between the even integer \(4h\)
  and \(4h+1\) (or equals \(4h\)); hence no odd \(q\) hits it. The BV
  proof would still tolerate a half sample.
- **Finite-limit control:** the truncated Perron value at \(A=1\) is
  \(\pi^{-1}\arctan(U/a)\ne1/2\) for finite \(U\). Physical stars must
  not be inserted earlier.
- **Normalization:** (7) becomes \(O(X^{1/4})\), not \(O(1)\), after
  restoring the M1 prefactor. This is target-safe but not a bound for
  GAR or the remaining vector operator.

## 6. Dependencies and exact artifacts used

Used protocol.md, the proof graph and active campaign, Round-22
synthesis, the exact Round-14 profile/coefficient construction, and the
Round-18 direct-profile pointwise report named by the brief. No other
Round-23 report, external source, or numerical experiment was used.

## 7. Recommended state effect

Promote (1)--(7) as a physical-limit \(q\)-Abel lemma and promote the
upper radial endpoint prefix as target-safe. Record explicitly that the
lemma depends on \(\chi_4(q)\), automatic product support, full actual
floors and stars, and geometric scale summation. Reject its extension to
finite \(U\) without a new sampled-BV theorem. Retain the endpoint
boundary operator, recombined arithmetic residue, transition traces,
GAR, M9-M1, and all downstream targets as open.
