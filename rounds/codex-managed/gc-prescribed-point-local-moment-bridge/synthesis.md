# Round 94 synthesis: prescribed points and local clusters

## Frozen objective

Determine exactly what the Round-93 global mean square says at prescribed
points and reduce any stronger pointwise conclusion to the weakest honest
short-window actual-coefficient estimate.

## Exact new consequences

Monotonicity of the inclusive lattice count gives one-sided persistence:
positive values persist to the right and negative values to the left.  If
\(M=|P(x)|\) and \(Q(Y,W)\) bounds every relevant length-\(W\) local
square integral, then

\[
 \frac{M^2}{4}\min\left(W,\frac{M}{2\pi}\right)\le Q(Y,W),
 \qquad
 M\ll Q^{1/3}+(Q/W)^{1/2}.
\]

For integer \(n\), the exact unit-cell identity is

\[
 \int_n^{n+1}P(t)^2dt
 =\left(P(n)-\frac\pi2\right)^2+\frac{\pi^2}{12}.
\]

Consequently

\[
 \sum_{n\asymp Y}|P(n)|^2\ll_\varepsilon Y^{3/2+\varepsilon},
\]

and the number of integers with
\(|P(n)|>Y^{1/4+\eta}\) is
\(O(Y^{1-2\eta+\varepsilon})\).  The same square-sampling estimate holds
for any one-separated real set.  These are discrete density-one theorems,
not prescribed-integer bounds.

## Exact cluster reduction

For a fixed exponential polynomial on a window of length \(W\), the
sinc-square majorant and randomly shifted cells give the exact positive
triangular form

\[
 \int_I|S(t)|^2dt
 \le \frac{\pi^2}{4}W\int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}
 a_\lambda e(\lambda c)\right|^2d\vartheta.
\]

The literal frequencies are \(h/d\) for M1 and \(h/(4d)\) for M2.
For \(W\le Y^{1/2}\), all moving floors, heights, and the hard prefix
partition the window into only \(O(\log Y)\) fixed-symbol strata; stars,
both signs, and \(\chi_4\) are retained.

At the accepted worst block \((D,L)=(Y^{1/2},Y^{1/6})\), the band diameter
is \(Y^{-1/3}\).  Windows \(W=Y^\alpha\), \(\alpha<1/3\), are
subcoherent, so the cluster form contains the pointwise square with
\(1-o(1)\) weight.  The first genuinely averaging range is therefore

\[
 \boxed{1/3<\alpha<1/2.}
\]

In that range, a uniform actual signed cluster energy
\(\ll Y^{1/2+\varepsilon}\) would imply

\[
 P(X)\ll_\varepsilon X^{1/6+\alpha/3+\varepsilon}<X^{1/3+\varepsilon}.
\]

No such estimate is currently proved.

## Source ceiling

Popov's published theorem gives

\[
 \int_{T-H}^{T+H}P(t)^2dt
 \ll H\sqrt T+T(\log T)^2.
\]

The additive \(T\)-term returns exactly the exponent \(1/3\) through the
sharp bridge.  Existing fourth/sixth local moments start at
\(H\ge T^{1/2}\).  No audited source reaches the required cluster bound.

## State decision

Promote the persistence/local bridge, exact integer-cell sampling theorem,
fixed triangular cluster kernel, moving-stratum reduction, and scoped
subcoherence obstruction.  Create the non-subcoherent actual-cluster
estimate as an open obligation.  Do not promote a new uniform exponent,
either canonical core, endpoint uniformity, M9-M1, M9-M2, M9, or the
quarter target.

## Exponent status

The internally certified uniform exponent remains

\[
 \boxed{P(X)\ll_\varepsilon X^{1/3+\varepsilon}.}
\]

Round 94 improves the density-one theorem at integer samples and identifies
the exact local mechanism needed for any further uniform gain, but it does
not itself improve the exponent.

