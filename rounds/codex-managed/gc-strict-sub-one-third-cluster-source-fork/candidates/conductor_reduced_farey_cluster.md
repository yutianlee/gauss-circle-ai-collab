# Conductor candidate: reduced-Farey form of the fixed cluster

Campaign: `gc-strict-sub-one-third-cluster-source-fork`

Starting graph SHA-256:
`e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

This is conductor working evidence, not accepted mathematics until the
Round-95 gates close.

## Literal block and reduction

Fix one denominator shell \(d\asymp D\), one signed height shell
\(|h|\asymp L\), one fixed moving-symbol stratum, and
\(\kappa_1=1\), \(\kappa_2=4\). Write

\[
 S_i(c)=\sum_{h,d}A_i(h,d)e\left(\frac{ch}{\kappa_i d}\right),
 \qquad |A_i(h,d)|\ll L^{-1}.
 \tag{95.C1}
\]

For a reduced signed fraction \(a/b\), \(b>0\), define the exact lift
coefficient

\[
 B_i(a,b)=\sum_{g\ge1}A_i(ga,gb),
 \tag{95.C2}
\]

with every original support, profile, floor, and star retained. Then

\[
 S_i(c)=\sum_{(a,b)=1}B_i(a,b)
 e\left(\frac{ca}{\kappa_i b}\right).
 \tag{95.C3}
\]

For M1, the literal character factor is

\[
 B_1(a,b)=\frac{\chi_4(b)}a
 \sum_g\frac{\chi_4(g)}g U_{1,a,b}(g),
 \tag{95.C4}
\]

up to the fixed H4 constant.  For M2 it is

\[
 B_2(a,b)=\frac{\chi_4(a)}a
 \sum_g\frac{\chi_4(g)}g U_{2,a,b}(g),
 \tag{95.C5}
\]

with the odd supports understood. The \(U_i\) are the literal bounded-BV
height/profile/prefix symbols. Thus the M1 character lives on the
reduced denominator and the M2 character on the reduced numerator; the
common lift character remains inside the \(g\)-sum.

## Exact diagonal

Partial summation on residue classes modulo \(4\) gives, on a dyadic lift
range \(g\asymp D/b\),

\[
 |B_i(a,b)|\ll_\varepsilon
 X^\varepsilon\frac{b}{D|a|}.
 \tag{95.C6}
\]

The same final power follows without exploiting this lift cancellation,
at the cost of logarithms. Since \(|a|\asymp Lb/D\), summation gives

\[
 \sum_{(a,b)=1}|B_i(a,b)|^2
 \ll_\varepsilon X^\varepsilon\frac DL.
 \tag{95.C7}
\]

This is the exact-frequency diagonal after all equal lifts have already
been combined. At \((D,L)=(Y^{1/2},Y^{1/6})\) it is \(Y^{1/3}\), safely
below the Round-95 cluster target \(Y^{1/2+\varepsilon}\).

## Exact off-diagonal kernel

Put

\[
 n=ab'-a'b.
\]

Expanding the accepted triangular form after the lift reduction gives

\[
 \begin{aligned}
 \mathcal C_i(c)
 ={}&\sum_{a,b,a',b'} B_i(a,b)\overline{B_i(a',b')}
 e\left(\frac{cn}{\kappa_i bb'}\right)\\
 &\times
 \left(1-\frac{W|n|}{\kappa_i bb'}\right)_+.
 \end{aligned}
 \tag{95.C8}
\]

The \(n=0\) part is exactly (95.C7). The first strict survivor is

\[
 \boxed{
 \mathcal O_i(c)=
 \sum_{\substack{a,b,a',b'\\ab'-a'b\ne0}}
 B_i(a,b)\overline{B_i(a',b')}
 e\left(\frac{c(ab'-a'b)}{\kappa_i bb'}\right)
 \left(1-\frac{W|ab'-a'b|}{\kappa_i bb'}\right)_+ .}
 \tag{95.C9}
\]

Round 95 closes internally if

\[
 |\mathcal O_i(c)|\ll_\varepsilon Y^{1/2+\varepsilon}
 \tag{95.C10}
\]

uniformly for both literal coefficient systems and all fixed strata.

## Capacity control

Farey density gives \(O(1+D^2/W)\) neighbours per reduced fraction in a
cell.  A coefficient-blind row-degree/Cauchy estimate therefore gives

\[
 \mathcal C_i(c)
 \ll_\varepsilon X^\varepsilon
 \left(1+\frac{D^2}{W}\right)\frac DL.
 \tag{95.C11}
\]

At the minimax point and \(W=Y^{7/16}\), this is

\[
 Y^{43/48+\varepsilon},
 \tag{95.C12}
\]

whereas the target is \(Y^{24/48+\varepsilon}\). The needed signed gain
is therefore exactly \(Y^{-19/48}\). Equivalently, the effective
off-diagonal degree must fall from

\[
 \frac{D^2}{W}=Y^{9/16}
 \quad\hbox{to at most}\quad
 L=Y^{1/6}.
 \tag{95.C13}
\]

The random-cell identity, exact-lift cancellation, or ordinary Farey
spacing alone does not supply this gain.  Any successful proof must act on
the signed phase and the different M1/M2 character placements in
(95.C9).

The accepted Popov local second moment is substantially sharper than
(95.C11):

\[
 Q(Y,W)\ll W\sqrt Y+Y(\log Y)^2.
 \tag{95.C14}
\]

After division by \(W=Y^{7/16}\), this has cluster capacity

\[
 Y^{1/2}+Y^{9/16}(\log Y)^2.
 \tag{95.C15}
\]

Thus the best accepted actual arithmetic ceiling misses (95.C10) by only
\(Y^{1/16}\). It nevertheless returns exactly the exponent \(1/3\)
through the persistence bridge.  Any fixed power saving in the additive
\(Y\)-term would give a strict sub-one-third exponent; the Round-95
internal task is to identify whether the literal kernel (95.C9) permits
such a saving.

## Scope

Equations (95.C2), (95.C8), and the (n=0)/(n\ne0) split are exact.
The BV estimate (95.C6), diagonal ledger, all-stratum assembly, and every
endpoint owner require the independent Round-95 gates.  No internal
strict exponent, canonical core, M9 estimate, or quarter theorem is
claimed here.
