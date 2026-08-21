# Round 94 derivation packet: prescribed-point local-moment bridge

## Frozen definitions

Let

\[
 P(t)=N(\sqrt t)-\pi t,
 \qquad
 N(\sqrt t)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\le t\},
\]

with the literal inclusive convention at integer jump points.  Round 93
proved

\[
 \int_Y^{2Y}|P(t)|^2\,dt\ll_\varepsilon Y^{3/2+\varepsilon}.
 \tag{94.1}
\]

The accepted uniform fallback is

\[
 P(X)\ll_\varepsilon X^{1/3+\varepsilon}.
 \tag{94.2}
\]

No pointwise quarter theorem or canonical-core estimate is assumed.

## One-sided persistence to audit

If \(M=|P(x)|\), monotonicity of \(N(\sqrt t)\) suggests the exact
one-sided implications

\[
 \begin{aligned}
 P(x)=M>0&\Longrightarrow
 P(x+u)\ge M-\pi u,\\
 P(x)=-M<0&\Longrightarrow
 P(x-u)\le -M+\pi u.
 \end{aligned}
 \tag{94.3}
\]

They must be checked at jumps, dyadic endpoints, and for both signs.  In
particular, when \(M\ge2\pi H\), a favorable adjacent interval of length
\(H\) should satisfy \(|P(t)|\ge M/2\).

## Candidate local bridge

For \(1\le H\le Y^{1/3}\), define the desired local moment property

\[
 \sup_{I\subset[Y/2,3Y],\ |I|=H}
 \int_I|P(t)|^2\,dt
 \ll_\varepsilon H Y^{1/2+\varepsilon}.
 \tag{94.4}
\]

The packet asks for an exact proof of the implication

\[
 (94.4)\Longrightarrow
 |P(x)|\ll H+Y^{1/4+\varepsilon}
 \qquad(Y\le x\le2Y),
 \tag{94.5}
\]

and its additive-error form: if the right side of (94.4) is
\(HY^{1/2+\varepsilon}+E(Y,H)\), determine the resulting pointwise
exponent exactly.  Decide whether unit-window local \(L^2\) is equivalent,
up to constants, to the pointwise problem.

## Discrete sampling deliverable

For every one-separated \(\mathcal X\subset[Y,2Y]\), test whether (94.1)
and (94.3) imply

\[
 \sum_{x\in\mathcal X}|P(x)|^2
 \ll_\varepsilon Y^{3/2+\varepsilon},
 \tag{94.6}
\]

and hence

\[
 \#\{n\in[Y,2Y]\cap\mathbb Z:
 |P(n)|>Y^{1/4+\eta}\}
 \ll_{\varepsilon,\eta}Y^{1-2\eta+\varepsilon}.
 \tag{94.7}
\]

This is an almost-all integer theorem, not a bound at a prescribed integer.

## Exact moving-frequency interface

For every actual M1/M2 denominator block, the active frequency range is

\[
 \left|{h\over4d}\right|\ll Y^{-1/4},
 \qquad |h|\ll D Y^{-1/4},\quad d\asymp D.
 \tag{94.8}
\]

On a window of length \(H=Y^{1/4+\sigma}\), a lawful short-moment
expansion must group rational frequencies into cells of width \(H^{-1}\),
retain exact equal-frequency lifts, \(\chi_4\), both signs, floors, the
moving height, hard top, stars, M1/M2 ownership, and R5.  A schematic
cluster norm is

\[
 H\sum_\nu
 \left|
 \sum_{|h/(4d)-\nu/H|\ll1/H}
 a_{h,d}(x)e\!\left({hx\over4d}\right)
 \right|^2.
 \tag{94.9}
\]

The exact kernel and tails must be derived; (94.9) is not accepted as a
theorem.  At the top \(D\asymp Y^{1/2}\), the frozen separated-frequency
bound is \(\asymp Y^{3/2}\), whereas the desired local scale is
\(HY^{1/2}=Y^{3/4+\sigma}\).  Any claimed bridge must identify the actual
signed cancellation that removes this spacing capacity.

## Forbidden shortcuts and exit rule

- Do not infer a prescribed-point theorem from global Chebyshev.
- Do not replace the actual moving weights by arbitrary bounded weights.
- Do not delete \(\chi_4\), a frequency sign, the hard top, or exact
  rational-frequency multiplicities before the signed estimate.
- Do not assume either Round-92 canonical core.
- A rigorous equivalence/no-go plus the discrete theorem is a successful
  outcome even if (94.4) remains open.
