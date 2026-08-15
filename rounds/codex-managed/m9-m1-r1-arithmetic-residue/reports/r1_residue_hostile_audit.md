## 1. Result

The proposed physical-return route survives, but only after the symmetric Mellin limits have produced the actual profiles. On that scope,
\[
 \mathfrak R^{\rm ar}[R_1]=O(1)
\]
in the normalized transform, uniformly in \(X\). Restoring the external M1 factor \(-(4/\pi)X^{1/4}\) gives \(O(X^{1/4})\). The saving is genuinely arithmetic: fixed-\(y\) Abel summation against \(\chi _4(q)\) gives one inverse support-length. It is unavailable for the unsigned replacement. No claim at arbitrary finite top Mellin height follows.

## 2. Exact statement and hypotheses

Let \(N=N_X=\lfloor16\sqrt X\rfloor\), \(u=a+i\mu\), and \(v=b+i\nu\), where
\[
 a>0,\qquad b>0,\qquad a/2+b<1/4.
\]
Then \(\Re\delta>0\) for \(\delta=1/4-u/2-v\), and \(a+b<1\), so the Dirichlet series for \(L(1-u-v,\chi _4)\) converges conditionally, locally uniformly on finite-height rectangles. Assume the accepted dyadic spatial profiles, the exact height profile \(\phi(t)=\Phi(t){\bf1}_{0<t<1}\), the top hard cutoff with symmetric half-star, and the exact integer \(H_j+1\).

The assertion is for the iterated physical profile limit: first truncate the \(q\)-series and both contours, perform finite operations, then take the symmetric profile limits, and only afterward remove the \(q\)-truncation. It is not an identity for a fixed finite top height.

## 3. Proof or derivation

Since \(\Re\delta>0\), insert
\[
 \delta^{-1}=\int_0^1 r^{\delta-1}\,dr.
\]
With \(y=xr\), \(dr=dy/x\), the domain becomes \(0<y<N\) and \(\max(1,y)\le x\le N\), while
\[
 x^{\delta-1/2}r^{\delta-1}dr=x^{-1/2}y^{\delta-1}dy.
\]
There is no orientation reversal. With \(e(t)=e^{2\pi it}\),
\[
 {d\over dx}e(\sqrt{Xx})=\pi i\sqrt X\,x^{-1/2}e(\sqrt{Xx}).
\]
Thus the prefactor \(-\pi i\sqrt X\) cancels exactly and leaves the lower-minus-upper phase
\[
 B_X(y)=e(\sqrt{X\max(1,y)})-e(\sqrt{XN}).
\]

Expanding \(L(1-u-v,\chi _4)\) first at finite \(q\)-length and then applying Mellin inversion gives
\[
 \mathfrak R^{\rm ar}[R_1]
 =\int_0^N y^{-3/4}B_X(y)\,\mathcal K_X(y)\,dy,
\]
\[
 \mathcal K_X(y)=\sum_j\sum_{q\ge1}{\chi _4(q)\over q}
 \phi\!\left({y\over q(H_j+1)}\right)
 \left[w_j\!\left({2\sqrt{Xy}\over q}\right)\right]^* .
\]
In particular, the character remains on \(q\), the coefficient is exactly \(1/q\), and no factor of \(\pi\), \(i\), or \(\sqrt X\) remains.

Put \(Q_j(y)=\sqrt{Xy}/D_j\). The smooth spatial support confines an interior-scale \(q\) to
\[
 3Q_j/2\le q\le4Q_j,
\]
and the hard top cutoff changes the lower endpoint to \(2Q_0\). On writing \(q=Q_j s\), the unsigned amplitude is
\[
 Q_j^{-1}s^{-1}W(2/s)\,
 \phi\!\left({D_j\sqrt y\over\sqrt X(H_j+1)s}\right),
\]
times at most one hard-cutoff half-star. The two fixed profiles are BV and \(s\) lies in a fixed compact interval; monotone composition preserves variation. Hence
\[
 \|a_{j,y}\|_\infty+\sum_q|a_{j,y}(q+1)-a_{j,y}(q)|\ll Q_j(y)^{-1}.
\]
Since partial sums of \(\chi _4\) have absolute value at most one, Abel summation yields
\[
 \sum_q\chi _4(q)a_{j,y}(q)\ll {D_j\over\sqrt{Xy}}.
\]
If \(Q_j<1/4\), the support contains no positive integer. Geometric summation over the remaining dyadic \(D_j\), first using \(D_j\le4\sqrt{Xy}\) and then \(\sum_jD_j\ll\sqrt X\), gives
\[
 |\mathcal K_X(y)|\ll\min(1,y^{-1/2}).
\]
As \(|B_X|\le2\),
\[
 |\mathfrak R^{\rm ar}[R_1]|
 \ll\int_0^1y^{-3/4}dy+\int_1^Ny^{-5/4}dy\ll1.
\]

The legal limiting order is essential. At finite \(q,U,V\), Fubini is finite. On compact \(y\)-subintervals, BV Mellin inversion in logarithmic coordinates gives the physical profiles and endpoint averages; then the displayed physical bound controls \(y\downarrow0\). Finally the uniform Abel majorant permits removal of the \(q\)-truncation.

## 4. First doubtful or unproved step

There is no unresolved step in the scoped physical-limit estimate. The first invalid step in either stronger version is asserting compact \(q\asymp Q_j(y)\) support before taking the top Mellin limit. A finite symmetric Perron truncation has noncompact logarithmic tails; even at its jump it equals \(\pi^{-1}\arctan(U/a)\), not \(1/2\). Therefore the BV support estimate above cannot be used uniformly at arbitrary finite \(U\).

## 5. Required control test and outcome

All endpoint controls pass. As \(y\downarrow0\), \(y^{-3/4}\) is integrable and sufficiently small \(y\) activates no scale. At \(y=1\), \(B_X\) is continuous, although its derivative changes. At \(y=N\), \(B_X(N)=0\). The hard top contributes exactly one jump of size \(O(Q^{-1})\), with the accepted half-star. Smooth support endpoints contribute no mass. At \(y=q(H_j+1)\), \(\Phi(1)=0\), so no height half-star occurs; retaining \(H_j+1\) also covers the smallest height \(H_j=1\). Coincident hard-top, height, or radial boundaries introduce no extra term: the height edge is zero and the radial top is killed by \(B_X(N)\).

For the unsigned replacement, a \(q\asymp Q\) block has \(Q\) terms of size \(Q^{-1}\), hence only \(O(1)\), not \(O(Q^{-1})\), per active scale. The absolute fixed-\(y\) argument then has no \(y^{-1/2}\) tail and allows normalized size \(N^{1/4}\), with a possible scale logarithm. Thus this mechanism does not prove the unsigned analogue; oscillation of \(B_X\) would require a different argument.

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, the Round-21, Round-22, and Round-23 syntheses, and rounds/codex-managed/m9-m1-r1-arithmetic-residue/briefs/r1_residue_hostile_audit.md. No claimant Round-24 report, numerical experiment, or external theorem was used.

## 7. Recommended state effect

**Promote**, with the explicit qualifier “after the physical profile limits,” the normalized \(O(1)\) R1 arithmetic-residue lemma. Reject any arbitrary-finite-height or unsigned extension. This closes only the R1 residue ledger item. It does not prove GAR, whose full radial sum remains; it does not estimate either diagonal transition trace; and therefore it does not prove M9-M1, M9, or the target.
