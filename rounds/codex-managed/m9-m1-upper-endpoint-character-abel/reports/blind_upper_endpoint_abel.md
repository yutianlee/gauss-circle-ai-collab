# Blind upper-endpoint character Abel derivation

## 1. Result

The physical symmetric-profile upper prefix satisfies
\[
\boxed{\sum_{hq\le N_X}^{*}\chi_4(q)(hq)^{-3/4}
\mathcal H^{\rm prof}_{\infty,X}(h,q)\ll_W1.}
\tag{1}
\]
Thus its physical M1 contribution is \(O_W(X^{1/4})\), hence
target-sized. The proof is elementary period-four Abel summation at each
fixed \((j,h)\). It applies to the completed physical top profile; it does
not prove a uniform statement for an arbitrary finite top Mellin
truncation.

## 2. Exact statement and hypotheses

Let
\[
D_j=2^{-j}\lfloor\sqrt X\rfloor,\qquad
H_j=\lfloor D_jX^{-1/4}\rfloor,\qquad
N=N_X=\lfloor16\sqrt X\rfloor,
\]
over the actual active scales, and put
\[
Q_j(h)=\frac{Xh}{D_j^2},\qquad
t_{j,h}(q)=\frac{2\sqrt{hX/q}}{D_j}
=2\sqrt{\frac{Q_j(h)}q}.
\]
Write \(V_j=W\) for \(j\ge1\) and
\[
V_0(t)=W_+^*(t)=
\begin{cases}W(t),&t<1,\\ \frac12,&t=1,\\0,&t>1.\end{cases}
\]
Here \(W(1)=1\), \(\operatorname {supp}W\subset[1/2,4/3]\).
The product projector is
\[
\kappa_{N,h}(q)=\mathbf1_{hq<N}
+\frac12\mathbf1_{hq=N}.
\tag{2}
\]

## 3. Proof or derivation

Exact height inversion gives
\[
\mathcal H^{\rm prof}_{\infty,X}(h,q)
=\sum_j\phi\!\left(\frac h{H_j+1}\right)V_j(t_{j,h}(q)),
\]
where
\(\phi(h/(H_j+1))=\mathbf1_{h\le H_j}
\Phi(h/(H_j+1))\). Therefore the left side of (1) is exactly
\[
\sum_j\sum_{1\le h\le H_j}
\Phi\!\left(\frac h{H_j+1}\right)h^{-3/4}
\sum_{q\ge1}\chi_4(q)f_{j,h}(q),
\tag{3}
\]
\[
f_{j,h}(q)=q^{-3/4}V_j(t_{j,h}(q))\kappa_{N,h}(q).
\tag{4}
\]
This retains every floor and both independent stars.

For \(j\ge1\), the exact possible \(q\)-support is
\[
\frac94Q_j(h)\le q\le16Q_j(h),\qquad hq\le N.
\tag{5}
\]
The smooth profile vanishes at the two spatial support endpoints. For
\(j=0\), it is
\[
4Q_0(h)\le q\le16Q_0(h),\qquad hq\le N,
\tag{6}
\]
with half weight at \(q=4Q_0(h)\) when that is integral. Equality
\(hq=N\) independently has the product half weight (2). Since
\(D_j\le\sqrt X\), \(Q_j(h)\ge h\ge1\).

Away from the jumps, setting \(t=2\sqrt{Q/q}\) gives
\[
\frac d{dq}\{q^{-3/4}W(t)\}
=q^{-7/4}\left\{-\frac34W(t)-\frac t2W'(t)\right\}.
\tag{7}
\]
On (5)–(6), \(q\asymp Q=Q_j(h)\), so
\[
\sup_q|f_{j,h}(q)|
+\sum_{q\ge1}|f_{j,h}(q+1)-f_{j,h}(q)|
\ll_WQ_j(h)^{-3/4}.
\tag{8}
\]
Indeed the integral of (7) has this size; the top turn-on and product
cutoff add at most one jump each of the same size. Coincident stars only
reduce a boundary value.

For \(A(t)=\sum_{q\le t}\chi_4(q)\), periodicity gives
\(\sup_t|A(t)|\le1\). Discrete Abel summation and (8) yield
\[
\boxed{\sum_q\chi_4(q)f_{j,h}(q)
\ll_WQ_j(h)^{-3/4}.}
\tag{9}
\]
Using boundedness of \(\Phi\),
\[
\begin{aligned}
|(3)|
&\ll_W\sum_j\sum_{h\le H_j}
h^{-3/4}\left(\frac{Xh}{D_j^2}\right)^{-3/4}\\
&=X^{-3/4}\sum_jD_j^{3/2}
\sum_{h\le H_j}h^{-3/2}\\
\ll X^{-3/4}\sum_{j\ge0}
(2^{-j}\lfloor\sqrt X\rfloor)^{3/2}\ll1.
\end{aligned}
\tag{10}
\]
The exact floors merely shorten the convergent \(h\)-sum.

The collapsed upper endpoint also has the unimodular phase
\(e(\sqrt{XN})\). Restoring Round 14's normalization, its physical
contribution is
\[
-\frac4\pi X^{1/4}\operatorname {Re}\!\left\{
e(1/8)e(\sqrt{XN})\,(3)\right\}=O_W(X^{1/4}).
\tag{11}
\]

## 4. First doubtful or unproved step

There is no doubtful step for the accepted physical profile limit.
For finite top height \(U\), the truncated inverse Mellin profile has no
literal compact support (6); a uniform sampled-BV theorem for that
intermediate kernel is not proved here. Thus (1) closes the graph's
physical symmetric-profile-limit prefix, not a stronger arbitrary-\(U\)
claim.

## 5. Required control tests and outcomes

The top equality \(t=1\), the radial equality \(hq=N\), and their possible
coincidence are all included in (4); each half-weight preserves (8).
Replacing \(\chi_4\) by unsigned coefficients destroys (9): a \(q\)-interval
of length \(\asymp Q\) has absolute mass \(\asymp Q^{1/4}\), recovering
the rejected \(N^{1/4}\) capacity. Product truncation can make a support
empty or add one jump, never enlarge its variation order. All controls
pass; no numerics or source import was used.

## 6. Dependencies and exact artifacts used

Only the authorized protocol, graph, active campaign, Round-22 synthesis,
Round-15 explicit profile construction, Round-18 direct-profile
kernel report/synthesis, and the assigned Round-23 brief were read. No
other Round-23 report was read.

## 7. Recommended state effect

Promote (1), the fixed-\((j,h)\) BV estimate (8), character Abel estimate
(9), and physical normalization (11). Mark
M9-M1-upper-radial-endpoint-prefix proved for the physical profile
limit. Retain finite-\(U\) strengthening, the recombined arithmetic
remainder, diagonal transitions, GAR, and M9-M1 as open.
