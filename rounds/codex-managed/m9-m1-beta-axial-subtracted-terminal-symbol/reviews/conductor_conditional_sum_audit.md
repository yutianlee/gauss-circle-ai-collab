# Conductor audit: conditional leading saddle sum

Campaign: m9-m1-beta-axial-subtracted-terminal-symbol  
Role: exponent and resonance seam  
Allocation: analytical/algebraic only

This review checks only the implication from the proposed cellwise mixed
symbol norm to the leading separated saddle sum. It does not prove that
norm.

Put

\[
 \sigma=\frac54,\qquad \zeta=a+b,\qquad
 r=\sigma-\frac\zeta2,\qquad p=\sigma+\frac\zeta2,
\]

so \(1<r<2\). After the post-endpoint stationary numerator and the
assumed pre-numerator \(\lambda^{-2}\) gain are combined, the retained
coefficient reduces to

\[
 h^{-r}q^{-2}D_j^{2-r}X^{r/2-1/2+b/4}
 x^{-r/2-b/2-5/4}.                                \tag{C39.8}
\]

This matches the earlier Round-28 conductor power ledger. The two radial
phases are

\[
 e^{\,i\pi\sqrt{Xx}(2\mp q/D_j)}.
\]

Since the \(x\)-amplitude and its derivative are integrable on
\([1,N_X]\), one integration by parts after \(y=\sqrt x\) gives

\[
 \min\left(1,\frac1{\sqrt X\,|2\mp q/D_j|}\right). \tag{C39.9}
\]

For the nonresonant plus sign, summation is immediate. Around the possible
minus-sign resonance \(q=2D_j\), write \(q=2D_j+k\). For
\(0<|k|\ll D_j\),

\[
 q^{-2}\min\left(1,\frac{D_j}{\sqrt X\,|k|}\right)
 \ll \frac1{D_j\sqrt X\,|k|}.
\]

Its sum is \(O((D_j\sqrt X)^{-1}\log X)\). The only zero denominator
would require the integer equality \(q=2D_j\). But every \(D_j\) is an
integer, so that \(q\) is even and \(\chi_4(q)=0\); the exact resonant
coefficient vanishes. For the closest nonzero odd \(q\), one has
\(|q-2D_j|\ge1\), and hence its contribution is at most
\[
 \frac1{D_j\sqrt X}\le X^{-3/4}.
\]
The ranges \(q\not\asymp D_j\) contribute \(O(X^{-1/2})\) directly.
Thus

\[
 \sum_q q^{-2}
 \min\left(1,\frac1{\sqrt X\,|2-q/D_j|}\right)
 \ll X^{-1/2}\log(2X).                              \tag{C39.10}
\]

Also \(\sum_hh^{-r}\ll1\). Therefore one scale contributes

\[
 D_j^{2-r}X^{r/2-1+b/4}\log(2X).                   \tag{C39.11}
\]

Because \(2-r>0\) and \(D_j\le\sqrt X\), this is
\(O(X^{b/4}\log X)=O(\log X)\). Summing \(O(\log X)\) actual scales
remains polylogarithmic before the external \(X^{1/4}\) factor.

Verdict: conditional on a correctly normalized cellwise mixed symbol
bound and its entry/exit remainders, the leading \(h,q,x,j\) exponent
ledger is target-safe. Exact resonance creates no obstruction. This
review does not control the complete second translation divided difference,
the regular moving traces, or the smooth non-Plemelj shares, and it does
not promote the beta transition.
