# Fixed-scale sampled \(q\)-BV proof

## 1. Result

The proposed lemma is true for the physical symmetric-profile limit.  For
every active scale \(D_j=2^{-j}\lfloor\sqrt X\rfloor\), every
\(1\le h\le H_j=\lfloor D_jX^{-1/4}\rfloor\), and
\(Q=Xh/D_j^2\), the actual sampled \(q\)-weight, including the top jump,
stationary star, product cutoff, and product half-tie, satisfies

\[
 \|a_{j,h}\|_{\ell^\infty}+
 \sum_{q\ge1}|a_{j,h}(q+1)-a_{j,h}(q)|
 \ll_W Q^{-3/4}. \tag{1}
\]

Consequently period-four Abel summation gives
\[
 \sum_q\chi_4(q)a_{j,h}(q)\ll_W Q^{-3/4}. \tag{2}
\]
The complete normalized upper radial endpoint is \(O_W(1)\); restoring
the external \(X^{1/4}\) factor makes it \(O_W(X^{1/4})\), hence
target-sized. This uses \(\chi_4\) essentially and is not an unsigned
bound or GAR.

## 2. Exact statement and hypotheses

Let \(y=\lfloor\sqrt X\rfloor\), \(N=N_X=\lfloor16\sqrt X\rfloor\), and
\(J=\max\{j:D_j\ge X^{1/4}\}\).  Use the accepted profile
\(W\in C_c^\infty([1/2,4/3])\), with \(\operatorname{Var}W\ll_W1\).
Put
\[
 t_q=2\sqrt{Q/q},\qquad
 \kappa_N(hq)=
 \begin{cases}1,&hq<N,\\[1mm]1/2,&hq=N,\\0,&hq>N,\end{cases}
\]
and let
\[
 \kappa_0(t)=
 \begin{cases}0,&t>1,\\1/2,&t=1,\\1,&t<1.\end{cases}
\]
The fixed-scale sequence is
\[
 a_{j,h}(q)=q^{-3/4}W(t_q)\kappa_N(hq)
 \begin{cases}\kappa_0(t_q),&j=0,\\1,&j\ge1.\end{cases} \tag{3}
\]
Smooth support-edge stars have no effect because \(W\) vanishes there.
The factor \(\kappa_0\) is exactly the one-sided top \(d=y\) star, and
\(\kappa_N\) is exactly the radial product star.

## 3. Proof and complete summation

Before multiplying by either cutoff, (3) is supported on
\[
 \frac94Q\le q\le16Q. \tag{4}
\]
Since \(D_j\le y\), one has \(Q\ge h\ge1\).  On (4),
\(\|q^{-3/4}\|_\infty\ll Q^{-3/4}\).  As \(t_q\) is monotone, sampling
cannot increase continuum variation, and the product-variation inequality
gives
\[
 \operatorname{Var}_{q\in\mathbb N}
 \{q^{-3/4}W(t_q)\}
 \le \|q^{-3/4}\|_\infty\operatorname{Var}W
 +\operatorname{Var}_{[9Q/4,16Q]}(q^{-3/4})\|W\|_\infty
 \ll_W Q^{-3/4}. \tag{5}
\]
Both \(\kappa_N(hq)\) and \(\kappa_0(t_q)\) are monotone sequences of
variation \(1\). Their equality values \(1/2\), including a possible
simultaneous tie, add no extra order of magnitude. Applying the same
product inequality proves (1). Thus the hard top discontinuity and the
floor in \(N\) do not spoil sampled BV.

For \(A(r)=\sum_{q\le r}\chi_4(q)\), periodicity gives \(|A(r)|\le1\).
Discrete partial summation therefore yields
\[
 \left|\sum_q\chi_4(q)a_{j,h}(q)\right|
 \le \|a_{j,h}\|_\infty+\operatorname{Var}(a_{j,h}),
\]
which proves (2). Even \(q\)'s require no separate treatment because
\(\chi_4(q)=0\).

After the accepted height and spatial inversions, the normalized endpoint
prefix is exactly
\[
 \begin{aligned}
 \mathfrak U_X
 =e(\sqrt{XN})\sum_{j=0}^{J}\sum_{h=1}^{H_j}
 \Phi\!\left(\frac h{H_j+1}\right)h^{-3/4}
 \sum_{q\ge1}\chi_4(q)a_{j,h}(q). \tag{6}
 \end{aligned}
\]
This retains every floor: no \(H_j\) is replaced by an asymptotic.
Since the fixed Vaaler profile \(\Phi\) is bounded, (2) gives
\[
 \begin{aligned}
 |\mathfrak U_X|
 &\ll X^{-3/4}\sum_{j=0}^{J}D_j^{3/2}
 \sum_{h=1}^{H_j}h^{-3/2}\\
 &\ll X^{-3/4}\sum_{j\ge0}(2^{-j}y)^{3/2}
 \ll1. \tag{7}
 \end{aligned}
\]
The exact lowest active floor may be \(H_J=1\), which is harmless in
(7). The inactive bottom profile was excluded before Fourier expansion
and retains its already accepted physical \(O(X^{1/4})\) cost.

Finally the upper endpoint's contribution to active M1 is
\[
 -\frac4\pi X^{1/4}
 \Re\{e(1/8)\mathfrak U_X\}=O_W(X^{1/4}). \tag{8}
\]
The separate one-sided top cotangent boundary is not part of (6) and is
not double-counted.

## 4. First doubtful or unproved step

No doubtful step remains for the physical symmetric-profile endpoint.
The argument does **not** assert (1) uniformly for a finite top Mellin
truncation: its sine-integral projector is not the one-jump sequence
\(\kappa_0\). The accepted symmetric limit must first produce the exact
starred profile (3). The recombined arithmetic residue and the two
post-functional-equation transition traces remain unestimated.

## 5. Required control test and outcome

Replacing \(\chi_4\) by \(|\chi_4|\) destroys the bounded-partial-sum
step and recovers the Round-22 capacity \(X^{1/8}\) for (6); thus the
proof does not establish the known-false unsigned analogue. At \(t_q=1\)
and \(hq=N\), the two half weights multiply exactly, while their combined
variation remains at most a constant. The top jump, product endpoint,
lowest height \(H_J=1\), and geometric scale sum all pass. No numerical
test was used.

## 6. Dependencies and exact artifacts used

Used only the protocol, proof graph, active campaign, Round-22 synthesis,
the accepted explicit profile construction, the direct-profile kernel
report, and the assigned Round-23 brief. No external theorem or web
source was used.

## 7. Recommended state effect

Promote (1)--(8) and mark the physical upper radial endpoint-prefix
obligation proved at normalized \(O(1)\), with the finite-top-truncation
scope explicitly excluded. This completes the physical endpoint part of
the endpoint boundary operator. Retain the recombined arithmetic residue,
both diagonal transition traces, the post-FE vector estimate, GAR,
M9-M1, M9-M2, M9, and the target as open.
