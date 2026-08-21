# Conductor review: persistence and discrete sampling

Campaign: `gc-prescribed-point-local-moment-bridge`

Starting graph SHA-256:
`6b7b5b681890edd49b0e0a525fe813044943d4072dd7fc90e27620615d2e93ae`

Status: conductor proof pending independent and hostile gates.

## Exact persistence

For \(u\ge0\), monotonicity of the inclusive counting function gives

\[
 P(x+u)\ge P(x)-\pi u,
 \qquad
 P(x-u)\le P(x)+\pi u.
\]

The first inequality is used when \(P(x)>0\), the second when
\(P(x)<0\).  Thus \(M=|P(x)|\ge2\pi H\) forces
\(|P|\ge M/2\) on one favorable adjacent interval of length \(H\).
Nonnegative jumps only strengthen the selected inequality.

## Exact integer-cell identity

For integer \(n\) and \(n\le t<n+1\), no squared norm crosses an integer,
so

\[
 P(t)=P(n)-\pi(t-n).
\]

Consequently

\[
 \int_n^{n+1}|P(t)|^2\,dt
 =\left(P(n)-{\pi\over2}\right)^2+{\pi^2\over12}.
 \tag{R94.1}
\]

Summing (R94.1) and applying Round 93 on a constant number of comparable
dyadic intervals proves

\[
 \sum_{Y\le n\le2Y}|P(n)|^2
 \ll_\varepsilon Y^{3/2+\varepsilon}.
 \tag{R94.2}
\]

For every fixed \(\eta>0\),

\[
 \#\{n\in[Y,2Y]\cap\mathbb Z:
 |P(n)|>Y^{1/4+\eta}\}
 \ll_{\varepsilon,\eta}Y^{1-2\eta+\varepsilon}.
 \tag{R94.3}
\]

The same bound holds for any one-separated real sample set by orienting
unit persistence intervals; such intervals have absolute bounded overlap.
Moreover, for \(n\le t<n+1\),

\[
 |P(t)|\le |P(n)|+\pi.
 \tag{R94.3a}
\]

Hence the uniform real-variable quarter theorem is equivalent, up to an
absolute additive constant, to the theorem at every integer.  This removes
the jump-convention bridge as a separate difficulty but does not estimate a
prescribed integer.

## Local-to-pointwise bridge

If every length-\(H\) interval near \(Y\) obeys

\[
 \int_I|P(t)|^2dt
 \ll HY^{1/2+\varepsilon}+E(Y,H),
\]

put \(Q=HY^{1/2+\varepsilon}+E(Y,H)\).  Persistence gives the sharp
two-branch inequality

\[
 {|P(x)|^2\over4}\min\!\left(H,{|P(x)|\over2\pi}\right)
 \le Q,
\tag{R94.4}
\]

and therefore

\[
 |P(x)|\ll Q^{1/3}+(Q/H)^{1/2}.
 \tag{R94.5}
\]

For \(H=Y^{\alpha+o(1)}\), \(E=0\), the delivered exponent is
\(\max\{1/6+\alpha/3,1/4\}\).  Thus
\(H=Y^{1/4+\sigma}\) gives \(1/4+\sigma/3\); a fixed longer window needs
the stronger total scale \(Q\ll Y^{3/4+o(1)}\) to reach a strict quarter.

Feeding the accepted uniform fallback into the local integral gives only
\(Q\ll HY^{2/3+\varepsilon}\).  Formula (R94.5) then returns

\[
 \max\!\left\{{2\over9}+{\alpha\over3},{1\over3}\right\}
 ={1\over3}
 \qquad(\alpha\le1/3),
\]

so the current pointwise theorem cannot bootstrap itself through the local
bridge.  A genuine improvement requires lowering the local average
amplitude below \(Y^{1/3}\).

At \(H=1\), (R94.1) shows that uniform local \(L^2\) and pointwise
control are equivalent up to constants.  Therefore the bridge itself is
elementary; the unproved input is a uniform local signed moment.  The
global moment supplies no such uniform localization.

## Scope decision

Equations (R94.2)--(R94.3) are candidates for promotion after both review
gates.  Equations (R94.4)--(R94.5) are bridge/equivalence lemmas.  None estimates a
prescribed exceptional integer, either canonical core, endpoint
uniformity, M9, or the uniform exponent.
