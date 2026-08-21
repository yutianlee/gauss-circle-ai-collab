# Conductor review: Round 94 local cluster kernel

Campaign: `gc-prescribed-point-local-moment-bridge`

Starting graph SHA-256:
`6b7b5b681890edd49b0e0a525fe813044943d4072dd7fc90e27620615d2e93ae`

## Fixed-symbol kernel

Let

\[
 S(t)=\sum_{\lambda\in\Lambda}a_\lambda e(\lambda t)
\]

and let \(I\) have length \(W\) and centre \(c\).  With

\[
 K(u)=\left(\frac{\sin \pi u}{\pi u}\right)^2,
 \qquad \widehat K(\xi)=(1-|\xi|)_+,
\]

the lower bound \(K(u)\ge4/\pi^2\) for \(|u|\le1/2\) gives

\[
 \int_I|S(t)|^2dt
 \le \frac{\pi^2}{4}W
 \sum_{\lambda,\mu}a_\lambda\overline{a_\mu}
 e((\lambda-\mu)c)(1-W|\lambda-\mu|)_+.
 \tag{R94.K1}
\]

For the randomly shifted cells

\[
 C_{\nu,\vartheta}
 =[(\nu+\vartheta)/W,(\nu+1+\vartheta)/W),
\]

two frequencies at distance \(r\) share a cell for exactly
\((1-Wr)_+\) of the shifts.  Therefore, with
\(b_\lambda=a_\lambda e(\lambda c)\),

\[
 \sum_{\lambda,\mu}b_\lambda\overline{b_\mu}
 (1-W|\lambda-\mu|)_+
 =\int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}b_\lambda\right|^2
 d\vartheta.
 \tag{R94.K2}
\]

Equal frequencies are aggregated before (R94.K1), or retained as a
multiset with all cross terms.  No absolute value is inserted inside an
arithmetic cluster.

## Literal M1/M2 frequencies and moving strata

The exact main-block frequency sets are

\[
 \lambda_1=\frac hd,
 \qquad
 \lambda_2=\frac h{4d}.
 \tag{R94.K3}
\]

The earlier common \(h/(4d)\) display was wrong for M1 and is corrected.
Both signs, \(\chi_4\), Vaaler coefficients, profiles, floors, and stars
remain in the aggregated coefficient.

Let the window length satisfy \(W\le Y^{1/2}\).  On a window near \(Y\),

\[
 \sqrt{x+W}-\sqrt x<1,
 \qquad
 D_j|(x+W)^{-1/4}-x^{-1/4}|<1
 \quad(D_j\le Y^{1/2}).
 \tag{R94.K4}
\]

Hence the moving denominator prefix and every dyadic Vaaler height have
only \(O(1)\) changes.  The union over \(O(\log Y)\) scales partitions the
window into \(O(\log Y)\) fixed-symbol strata.  Applying a uniform
fixed-symbol cluster estimate on each stratum loses logarithms only.
Boundary samples have measure zero in the local integral, while their
prescribed-point value retains the original star convention.  The bottom
and R5 stay under their accepted pointwise \(Y^{1/4+\varepsilon}\)
owners.

## Subcoherence and exact surviving range

At the accepted minimax block

\[
 D=Y^{1/2},\qquad L=Y^{1/6},
\]

the M1 band diameter is \(O(Y^{-1/3})\), and the M2 diameter differs only
by the constant factor \(1/4\).  If \(W=Y^\alpha\) with
\(\alpha<1/3\), all frequencies lie in one randomly shifted cell for a
set of shifts of measure \(1-o(1)\).  Consequently (R94.K2) is at least

\[
 (1-o(1))|S(c)|^2.
 \tag{R94.K5}
\]

Thus target-scale local smoothing below \(Y^{1/3}\) is already
pointwise-hard on this block.  At \(\alpha=1/3\) only \(O(1)\) cells
occur.  This obstruction does not extend to
\(1/3<\alpha<1/2\), where the band occupies
\(Y^{\alpha-1/3}\) cells.

## First strict survivor

For any fixed \(1/3<\alpha<1/2\), the smallest useful new estimate is the
literal actual-coefficient cluster bound

\[
 \int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}
 a_\lambda(c)e(\lambda c)\right|^2d\vartheta
 \ll_\varepsilon Y^{1/2+\varepsilon}
 \tag{R94.K6}
\]

uniformly for every fixed M1/M2 stratum, with logarithmic block assembly.
It would imply

\[
 \sup_{|I|=Y^\alpha}\int_I|P(t)|^2dt
 \ll_\varepsilon Y^{\alpha+1/2+\varepsilon}
\]

and hence, by the sharp persistence bridge,

\[
 P(X)\ll_\varepsilon
 X^{1/6+\alpha/3+\varepsilon}<X^{1/3+\varepsilon}.
 \tag{R94.K7}
\]

No accepted theorem proves (R94.K6).  At the actual quarter window
\(\alpha=1/4+o(1)\), (R94.K5) shows that the cluster theorem is not a
simplification of the pointwise minimax core.

## Decision

Promote (R94.K1)--(R94.K5) as an interface and obstruction lemma.  Create
(R94.K6) as the exact open non-subcoherent signed-cluster obligation.
Do not promote a local moment, a new uniform exponent, either canonical
core, endpoint uniformity, M9, or the quarter target.

