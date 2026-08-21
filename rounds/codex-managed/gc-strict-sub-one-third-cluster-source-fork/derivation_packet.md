# Round 95 derivation packet: fixed non-subcoherent cluster

Campaign: `gc-strict-sub-one-third-cluster-source-fork`

Starting graph SHA-256:
`e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

## Frozen exponent and bridge

Let

\[
 P(t)=N(\sqrt t)-\pi t,
 \qquad W=Y^{7/16}.
\]

The accepted one-sided persistence lemma says that if every relevant
length-\(W\) interval near \(Y\) has square mass at most \(Q(Y,W)\),
then

\[
 |P(X)|\ll Q(Y,W)^{1/3}+\bigl(Q(Y,W)/W\bigr)^{1/2}.
 \tag{95.1}
\]

Therefore the standard local target

\[
 Q(Y,W)\ll_\varepsilon WY^{1/2+\varepsilon}
 =Y^{15/16+\varepsilon}
 \tag{95.2}
\]

would prove

\[
 P(X)\ll_\varepsilon X^{5/16+\varepsilon}.
 \tag{95.3}
\]

This is a strict sub-one-third stepping stone, not the quarter target.

## Accepted triangular cluster reduction

For a fixed exponential polynomial

\[
 S(t)=\sum_{\lambda\in\Lambda}a_\lambda e(\lambda t)
\]

and an interval of length \(W\) centred at \(c\), define

\[
 C_{\nu,\vartheta}
 =[(\nu+\vartheta)/W,(\nu+1+\vartheta)/W).
\]

The accepted sinc-square/random-cell identity is

\[
 \int_I|S(t)|^2dt
 \leq \frac{\pi^2}{4}W\int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}
 a_\lambda e(\lambda c)\right|^2d\vartheta.
 \tag{95.4}
\]

Equal frequencies are aggregated with all cross terms. No arithmetic
absolute value may be inserted inside a cell.

For M1 the literal frequency is

\[
 \lambda_1=\frac hd,
 \tag{95.5}
\]

and for M2 it is

\[
 \lambda_2=\frac h{4d}.
 \tag{95.6}
\]

The coefficient attached to each frequency must retain its literal
Vaaler coefficient, \(\chi_4\) on the correct coordinate, both signs,
profile, floor, hard-top prefix, and star convention. M1 must not be
silently relabelled as M2.

## Moving-symbol reduction

On every window \(W\leq Y^{1/2}\), the moving denominator prefix and
each dyadic Vaaler height have only \(O(1)\) changes. Across all dyadic
scales they form \(O(\log Y)\) fixed-symbol strata. The bottom and R5
terms remain with their accepted pointwise
\(O_\varepsilon(Y^{1/4+\varepsilon})\) owners. Thus it is enough to
prove, uniformly on every literal fixed stratum,

\[
 \mathcal C(c):=
 \int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}
 a_\lambda(c)e(\lambda c)\right|^2d\vartheta
 \ll_\varepsilon Y^{1/2+\varepsilon}.
 \tag{95.7}
\]

Logarithmic scale/stratum assembly is harmless. A proof for arbitrary
bounded coefficients is neither expected nor sufficient: the argument
must use the actual character and phase.

## Geometry and the first averaging range

At the accepted one-third minimax block

\[
 D=Y^{1/2},\qquad L=Y^{1/6},
\]

the frequency-band diameter is \(O(Y^{-1/3})\). At the frozen window it
occupies

\[
 Y^{7/16-1/3}=Y^{5/48}
 \tag{95.8}
\]

random cells. Hence the Round-94 subcoherence obstruction no longer
applies, but the random-cell identity alone supplies no cancellation.

Inside one M1 block the cell condition is

\[
 \left|\frac hd-\frac{h'}{d'}\right|<W^{-1},
 \qquad |hd'-h'd|<\frac{dd'}W,
 \tag{95.9}
\]

and for M2 the right side is multiplied by the harmless factor \(4\).
Every proof must separately audit exact equal reduced fractions, nearby
non-equal fractions, the diagonal, two signs, and cross-block assembly.

## External theorem fork

Li and Yang, arXiv:2308.14859v2, claim the direct pointwise exponent

\[
 \theta_{\rm LY}=0.3144831759741\ldots<\frac13.
 \tag{95.10}
\]

The local source card remains open because Definition 4.1 equation (4.4)
prints \(M<T^{-7/16}\), whereas the later application equation (5.11)
prints \(M<T^{7/16}\). A source promotion requires a clean primary-source
resolution of that discrepancy and an exact audit of every theorem
hypothesis used in the published exponent. Even a certified direct
theorem does not prove (95.7), M9-M1, M9-M2, or the quarter target.

## Required decision

Round 95 has one objective: decide whether a rigorously certified uniform
exponent below one third is now available. The internal route must prove
(95.7), or isolate the first smaller literal signed survivor and quantify
its capacity. The external route must either certify the complete
Li--Yang theorem chain or give the exact first unresolved source seam.
The two routes are independent and may not be blended into a proof.

