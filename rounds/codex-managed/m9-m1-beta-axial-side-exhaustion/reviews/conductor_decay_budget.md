# Conductor preliminary decay budget for Round 35

Campaign: `m9-m1-beta-axial-side-exhaustion`  
Role: conductor independent analysis  
Allocation: 100% analytical/algebraic

## 1. The useful arbitrary-order input

For

\[
 R_{M,v}(w)=
 \frac{(-C)^M I_M(\rho)}{\prod_{r=0}^{M-1}(\rho+r/2)},
 \qquad
 \rho=w-\frac34-\frac v2,
\]

and \(w=\sigma\pm iS\), \(|\Im v|\le V\), the declared nesting
\(S\ge 4(X+U+V+2)\) gives \(|\rho+r/2|\asymp S\). One additional
nonstationary integration by parts in \(I_M\) yields

\[
 R_{M,v}(\sigma\pm iS)=O_{X,M}(S^{-M-1}).       \tag{35.C1}
\]

The key Round-35 question is not (35.C1), which is already accepted, but
whether every restriction, residue, and mask area in the finite
two-axis transfer costs only a fixed polynomial in \(S,U,V\), uniformly
enough that increasing \(M\) wins.

## 2. Safe derivative heuristic to be proved

At fixed radial side, a \(v\)-derivative is a \(\rho\)-derivative plus
derivatives of the outside Mellin factors. Differentiating the rational
denominators improves the \(S\)-power; differentiating \(I_M\) inserts
\(\log x\), bounded by \(O(\log X)\) on \([1,N_X]\). Hence for each fixed
derivative order \(r\), one expects

\[
 \partial_v^r R_{M,v}(\sigma\pm iS)
 \ll_{X,M,r}(\log X)^rS^{-M-1}.                  \tag{35.C2}
\]

There is no direct \(u\)-dependence in \(R_{M,v}\). The \(u\)-transfer
instead differentiates or restricts the outside \(u\)-profile and the
gamma/Dirichlet factor. Those costs must be read from the complete
integrand rather than charged to \(R_M\).

## 3. Preliminary worst-capacity envelope

The accepted unshifted side proof combines (35.C1) with the degree-two
left-edge capacity \(S^{1-2\lambda}\), giving

\[
 S^{-M-2\lambda}
\tag{35.C3}
\]

up to \(X\)-dependent and outside-profile logarithms. A finite two-axis
transfer adds at most two real area integrations, restrictions to finitely
many faces, and residues of fixed order. If all gamma/residue factors have
a uniform bound

\[
 (1+S+U+V)^K                                      \tag{35.C4}
\]

for one fixed \(K\), then every one of the sixteen strata is bounded by

\[
 C_{X,M}(1+U+V)^K(\log(2+U))^K
 S^{-M-2\lambda+K}.                              \tag{35.C5}
\]

Choosing \(M>K-2\lambda+2\), followed by a sufficiently high polynomial
\(S=(X+U+V+2)^A\), would close the whole side vector. This is a useful
reduction, but (35.C4) must be proved uniformly through axial/artificial
collisions and through all sheared connector faces; it cannot be assumed.

## 4. Likely weakest seam

The mask itself is compactly supported in the bounded transition variable,
so \(\psi'\) and \(\psi''\) should not introduce growing beta volume.
The dangerous terms are instead:

1. axial residues of the degree-two gamma quotient on the radial side;
2. combined residues when an axis meets an artificial \(\rho\)-divisor;
3. horizontal faces of the connector in sheared coordinates;
4. constants hidden in repeated endpoint subtraction as \(M\) is chosen.

Round 35 must show these are fixed-order polynomial costs and give one
uniform exponent \(K\), or isolate the first term for which no such bound
follows. No physical endpoint/arithmetic limit is part of this review.
