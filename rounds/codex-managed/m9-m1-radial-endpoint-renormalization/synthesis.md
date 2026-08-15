# Round 21 synthesis: radial sides can be renormalized; the boundary operator remains

Campaign: `m9-m1-radial-endpoint-renormalization`  
Round type: endpoint subtraction and residue reconciliation  
Graph SHA-256 before patch: `19f21f378c9f2ca932c25f0de66deba8d37fdc6d5deaeb74185e01dfa3a9b637`

## Conductor decision

Promote the exact finite endpoint-subtraction identity, full endpoint weights,
sign/orientation conventions, artificial-pole ledger, and scoped removal of
the renormalized radial horizontal sides after sufficiently many
subtractions. Retain the explicit endpoint boundary operator and diagonal
transition traces as open.

The blind derivation and independent hostile audit agree that endpoint stars
do not halve integration-by-parts coefficients and that artificial poles of
the split pieces must cancel before residues are counted. The planned signed
boundary attacker did not deliver within the round budget, so no boundary
cancellation or target estimate is promoted.

## Exact endpoint subtraction

Let

\[
 G_v(w)=\int_1^N x^{w-7/4-v/2}e(\sqrt{Xx})\,dx,
 \qquad \rho=w-\frac34-\frac v2,
\]

where (N=N_X). Put (C=\pi i\sqrt X) and

\[
 I_k(\rho)=\int_1^N x^{\rho+k/2-1}e(\sqrt{Xx})\,dx.
\]

The exact recurrence is

\[
 I_k(\rho)=
 \frac{N^{\rho+k/2}e(\sqrt{XN})-e(\sqrt X)}{\rho+k/2}
 -\frac{C}{\rho+k/2}I_{k+1}(\rho).
\]

Therefore, for every (M\ge1),

\[
 \boxed{G_v(w)=E_{M,v}(w)+R_{M,v}(w),}
\]

with

\[
 E_{M,v}(w)=\sum_{k=0}^{M-1}
 \frac{(-C)^k
 \{N^{\rho+k/2}e(\sqrt{XN})-e(\sqrt X)\}}
 {\prod_{r=0}^{k}(\rho+r/2)},
\]

\[
 R_{M,v}(w)=
 \frac{(-C)^M I_M(\rho)}
 {\prod_{r=0}^{M-1}(\rho+r/2)}.
\]

The blind report gives an equivalent expansion obtained by repeatedly
applying (x\,d/dx) to the phase. Both are finite exact identities; the
recurrence above is adopted because it displays every artificial pole and
the half-step denominators directly.

The upper physical endpoint has positive sign and the lower endpoint
negative sign. These coefficients have full weight. The star in the finite
radial cutoff changes symmetric inverse-Mellin values at a boundary, not the
Lebesgue integral defining (G_v), so it does not insert a factor (1/2)
into (E_M).

## Exact finite operator splitting

Insert (G_v(1-s)=E_{M,v}(1-s)+R_{M,v}(1-s)) into the accepted finite vector
identity. Retaining the terminal vertical segment and the original radial
side orientations gives

\[
 \mathfrak I^c
 =\mathfrak R^{\rm ar}[G]
 +\mathfrak T(R_M)+\mathfrak S(R_M)
 +\underbrace{\mathfrak T(E_M)+\mathfrak S(E_M)}
 _{\mathfrak E_M\text{, the endpoint boundary operator}}.
\]

The upper side runs (\lambda+iS\to c+iS), while the lower runs
(c-iS\to\lambda-iS). Equivalently, in common left-to-right orientation,
the side functional is upper minus lower. This reverses the tempting
termwise cancellation; even the (x=1,k=0) control reinforces at a far
right abscissa.

The arithmetic residue remains the unsplit expression

\[
 G_v(1-(u+v)/2)L(1-u-v,\chi_4).
\]

If (E_M) and (R_M) are shifted separately, their artificial poles

\[
 w=\frac34+\frac v2-\frac r2,
 \qquad 0\le r<M,
\]

must have opposite residues and cancel. At the arithmetic pole, the two
pieces must recombine to (G_v(w_0)L). Retaining the unsplit residue and a
split residue would double-count it. The same rule applies to later height,
hard-Perron, and corner residues.

## Renormalized side removal

On (w=\sigma\pm iS), with (S\gg X+U+V), every displayed denominator is
(\asymp S). A further nonstationary integration by parts in (I_M) gives

\[
 R_{M,v}(\sigma\pm iS)=O_{X,N,M,c,c',b}(S^{-M-1}).
\]

Against the accepted worst left-edge degree-two capacity
(O(S^{1-2\lambda})), the renormalized side satisfies, after the outside
Mellin weights,

\[
 \mathfrak S(R_M)
 \ll_{X,M}(\log X)\log(2+U)S^{-M-2\lambda}.
\]

For fixed terminal abscissae choose (M>-2\lambda), then choose a sufficiently
high polynomial (S=S(X,U,V)). This removes the renormalized radial sides.
It does not estimate the explicit boundary operator (mathfrak E_M) or the
two diagonal transition traces.

## Smallest survivor

The remaining boundary problem is now finite and explicit:

1. (mathfrak E_M=\mathfrak T(E_M)+\mathfrak S(E_M)) with full endpoint
   signs and all actual outside profiles;
2. the two diagonal single-transition vector-Hilbert traces;
3. the correctly recombined arithmetic and axial residue ledger.

No endpoint functional cancels automatically with an existing residue, and
no half-weight or upper/lower symmetry supplies a shortcut. The next round
should collapse (mathfrak E_M) by Cauchy algebra—starting with (M=1)—and
decide whether it is target-sized, a known direct boundary term, or a new
signed Dirichlet boundary sum.

## State effect

- promote exact arbitrary-order endpoint subtraction and the artificial-pole
  cancellation rule;
- promote scoped nested removal of only the renormalized radial sides;
- reject half-weighted IBP endpoints, automatic upper/lower cancellation,
  and double-counted split residues;
- retain the explicit endpoint boundary operator, transition traces, GAR,
  M9-M1, M9-M2, M9, and the target as open.

