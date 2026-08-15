# Conductor independent analysis: weighted W-1 transfer

## Verdict in advance of external reviews

The unit-frequency window argument transfers to the actual absolute block under a strictly weaker hypothesis than a pointwise plateau for the dyadic weight.  It is enough that the block has uniformly positive discrete \(\ell^1\)-mass.  This yields the candidate lower bound, conditional on the accepted exact-resonance closure and the H4 coefficient formula.  It gives no lower bound for the true signed fourth moment.

## Weighted window lemma

Let \(I_D\subset [D,2D)\cap\mathbb Z\), put \(a_d=|w_D(d)|\ge 0\), and suppose

\[
 A_D:=\sum_{d\in I_D}a_d\ge \kappa D
\]

for a constant \(\kappa>0\) independent of the active block.  Assume also that the frequency cutoff contains \(h=1\).  For \(M\ge 1\), define

\[
 \eta=\frac{M}{16D^4},\qquad
 r(d,e)=\frac1d+\frac1e.
\]

All \(r(d,e)\) lie in an interval of length at most \(D^{-1}\).  Partition this interval into half-open cells of length at most \(\eta\), and let

\[
 P_j=\sum_{r(d,e)\text{ in cell }j}a_da_e.
\]

The number of cells is

\[
 K\le 2+\frac{16D^3}{M}.
\]

If \((d_1,d_3)\) and \((d_2,d_4)\) lie in the same cell, then

\[
 \left|\frac1{d_1}-\frac1{d_2}+\frac1{d_3}-\frac1{d_4}\right|
 \le \eta.
\]

Since \(d_1d_2d_3d_4<(2D)^4=16D^4\), the cleared integer

\[
 N=d_2d_3d_4-d_1d_3d_4+d_1d_2d_4-d_1d_2d_3
\]

satisfies \(|N|\le M\).  Cauchy--Schwarz now gives the weighted same-cell mass

\[
 \sum_jP_j^2\ge \frac{(\sum_jP_j)^2}{K}
 =\frac{A_D^4}{K}
 \gg_\kappa \frac{D^4}{1+D^3/M}
 \gg_\kappa \min(D^4,MD).
\]

Thus, if \(|\beta_{1,H_D}|\ge b_0>0\), restriction to \(h_1=h_2=h_3=h_4=1\) gives

\[
 \Sigma_{\rm abs}(|N|\le M)
 \ge c(\kappa,b_0)\min(D^4,MD).
\]

After subtracting the entire exact-resonance mass, the conditional closure

\[
 \Sigma_{\rm abs}(N=0)\le C_\epsilon D^2X^\epsilon
\]

implies

\[
 \boxed{\Sigma_{\rm abs}(0<|N|\le M)
 \ge c(\kappa,b_0)\min(D^4,MD)-C_\epsilon D^2X^\epsilon.}
\]

The proof does not require a pointwise lower bound for \(|w_D|\).  The weakest convenient block normalization is \(\sum_{d\asymp D}|w_D(d)|\gg D\).  A fixed, nonzero smooth profile \(w_D(d)=w(d/D)\) has this property, but the draft's phrase "bounded smooth dyadic partition" does not by itself record it and should be strengthened before this result is consolidated.

## H4 coefficient consequence

Under the coefficient algebra currently recorded in the proof graph,

\[
 |\beta_{1,H}|=\frac{\Phi(1/(H+1))}{\pi},
 \qquad
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u.
\]

For \(H\ge1\), \(0<u\le1/2\).  The explicit formula extends continuously to \(u=0\) with value \(1\), and it is positive on \((0,1/2]\); compactness therefore gives a uniform positive lower envelope.  In fact \(\Phi(u)\ge1/2\) on this interval: for \(x\in[0,\pi/2]\), concavity of \(x\cot x\) gives

\[
 x\cot x\ge1-\frac{2x}{\pi},
\]

and hence

\[
 \Phi(u)\ge u+(1-u)(1-2u)
 =1-2u+2u^2\ge\frac12.
\]

Consequently \(b_0=1/(2\pi)\) is available if and only if the primary-source audit confirms the project's formula and normalization.  This paragraph is an internal algebra check, not a substitute for H4 source validation.

## Fat band and endpoint audit

In the active range \(X^{1/4}\le D\le X^{1/2}\), put \(M=D^4/X\).  Then \(M\ge1\) and \(M/D^3=D/X\le X^{-1/2}\), so the linear branch applies:

\[
 \Sigma_{\rm abs}(0<|N|\le D^4/X)
 \ge cD^5/X-C_\epsilon D^2X^\epsilon.
\]

For every fixed \(\delta>0\), if \(D\ge X^{1/3+\delta}\), choose a fixed \(\epsilon<3\delta\).  Since

\[
 \frac{D^5/X}{D^2X^\epsilon}=\frac{D^3}{X^{1+\epsilon}}
 \ge X^{3\delta-\epsilon},
\]

the main lower bound eventually dominates both the exact-resonance subtraction and any proposed \(O_\epsilon(D^2X^\epsilon)\) upper bound.  At the exact crossover \(D=X^{1/3}\), the lower bound is only of order \(D^2\), so there is no power contradiction.  At \(D=X^{3/8}\) and \(D=X^{1/2}\), the excess powers over \(D^2\) are respectively \(X^{1/8}\) and \(X^{1/2}\).

## Scope and remaining seams

The argument applies to:

- the unweighted raw tuple count (take \(a_d=1\));
- the absolute \(\beta\)-weighted mass when the block has \(\ell^1\)-mass \(\gg D\);
- the corresponding \(\chi_4\)-removed unsigned mass.

It does not apply to the true signed mass, because a positive restricted subtotal need not survive cancellation from the other frequencies or from signed dyadic factors.  Round 2 must still validate the primary Vaaler normalization, the exact convention for \(N\), the availability of \(h=1\) at the lower endpoint, and the actual dyadic block's uniform \(\ell^1\)-normalization.
