# Conductor preliminary review: metric-resolved square owner

Campaign: m9-m2-blockwise-owner-completion

Starting graph SHA-256:
f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d

This is a conductor calculation to be adjudicated against the three
independent Round-109 reports.

## 1. Why the square owner is the critical refinement

The Round-77 error is estimated absolutely per ordered pair and hence
survives every dyadic refinement with only logarithmic cost.  The
Round-79 \(\rho\leq1\) owner is also a positive-capacity estimate.
Exact nonsquare centres vanish in the complete punctured multiplier.
The singleton and prescribed polylogarithmic rows are already proved
for each metric member.

The Round-78 square theorem is signed in \(k\), so it does not formally
give an outside-absolute estimate after the metric partition.  It is
therefore the first owner requiring a new check.

## 2. Metric-resolved square phase

Write

\[
 a=s^2,\qquad b=t^2,\qquad t=s+2u,\qquad g\ {\rm odd}.
\]

Then

\[
 \Lambda={X(\sqrt b-\sqrt a)^2\over2}=2Xu^2,
\]

and the centered Round-78 carrier is

\[
 e(-gXu^2/k)=e(-g\Lambda/(2k)).
\]

For one smooth punctured metric member,

\[
 W_R(\Lambda/k)=\sum_{\nu\in\mathbb Z}
 \widehat W_R(\nu)e(\nu\Lambda/k).
\]

The complete phase is therefore

\[
 e\!\left(-{(g-2\nu)Xu^2\over k}\right).
\tag{109.R1}
\]

Because \(g\) is odd,

\[
 n=|g-2\nu|\geq1
\tag{109.R2}
\]

for every metric mode, including \(\nu=0\).

## 3. Sampled variation and reciprocal curvature

The accepted Round-78 complete-Fresnel estimate is

\[
 V_{s,u,g}:=
 \sup_k|\mathfrak B_g(k)|
 +\operatorname {Var}_k\mathfrak B_g(k)
 \ll_\varepsilon X^\varepsilon
 \sqrt{gt^2/K},
\tag{109.R3}
\]

where \(K=Ju/s\).  For the phase in (109.R1),

\[
 |f_{\nu,g}''(k)|
 \asymp {nXu^2\over K^3}.
\tag{109.R4}
\]

Weighted van der Corput gives

\[
\begin{aligned}
 \left|\sum_k\mathfrak B_g(k)e(f_{\nu,g}(k))\right|
 &\ll_\varepsilon X^\varepsilon V_{s,u,g}
 \left(K\sqrt{nXu^2/K^3}
 +(nXu^2/K^3)^{-1/2}\right)\\
 &\ll_\varepsilon X^\varepsilon
 \left(\sqrt{gn}\,ts+\sqrt{g/n}\,{t\over s}\right).
\end{aligned}
\tag{109.R5}
\]

The accepted complete Fourier moments, valid uniformly for
\(1\leq R\leq G\) and \(g\asymp G\), are

\[
 \sum_\nu|\widehat W_R(\nu)|\,|g-2\nu|^{1/2}
 \ll\sqrt G,
\qquad
 \sum_\nu|\widehat W_R(\nu)|\,|g-2\nu|^{-1/2}
 \ll G^{-1/2}.
\tag{109.R6}
\]

Since \(gt^2\asymp L\) and \(s\asymp t\), (109.R5)--(109.R6)
give

\[
 \sum_\nu|\widehat W_R(\nu)|
 \left|\sum_k\mathfrak B_g(k)e(f_{\nu,g}(k))\right|
 \ll_\varepsilon X^\varepsilon(L+1)
\tag{109.R7}
\]

for every actual lifted square triple.

## 4. Blockwise owner norm

The exact lift count is

\[
 \sum_{s,u}N_{s^2,t^2}\ll L\log(2L).
\tag{109.R8}
\]

Taking absolute values after the coupled \(k,\nu\)-sum and then summing
the lifted triples yields, for each metric member and every additional
dyadic subblock,

\[
 |\mathcal S_{L,R,B}^{\square}(X)|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.R9}
\]

There are only logarithmically many metric members and scale blocks.
Thus

\[
 \sum_{R,B}|\mathcal S_{L,R,B}^{\square}(X)|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.R10}
\]

This is stronger than the Round-78 aggregate theorem in exactly the
direction required by the Round-109 blockwise owner gate.  It uses the
actual complete-Fresnel variation and odd lift parity; the false
absolute Abel majorant remains false.

## 5. Remaining seams

Before promotion the reviews must verify:

1. that the canonical metric member is exactly the \(W_R\) used in
   (109.R6);
2. that all orientations have \(n=|g\mp2\nu|\geq1\);
3. that the dyadic block cutoffs have bounded sampled variation and do
   not split a collar transition with a power loss;
4. that the square owner is inserted before, or disjointly within, the
   \(\rho\)-safe and short-row owners;
5. that the global diagonal stays separate and is not reinserted as an
   oriented pair.

If these pass, the strongest remaining owner issue should be an exact
one-count dictionary rather than an analytic square-owner norm.
