# Conductor audit of the support-separated cell complex

Campaign: `m9-m1-beta-axial-side-exhaustion`  
Role: conductor seam validation  
Allocation: 100% analytical/algebraic

The actual fixed mask is even, smooth, equals one on \([-B_0,B_0]\),
and is supported on \([-2B_0,2B_0]\). Put \(B=2B_0\).

On the original radial sides \(w=\sigma\pm iS\), reflection gives
\(s=1-w\), so \(t=\Im s=\mp S\). Every point in the closed outside
product satisfies

\[
 |\beta|=\left|t-\frac{\mu+\nu}{2}\right|
 \ge S-\frac{U+V}{2}.
\tag{35.CA1}
\]

Therefore \(S>(U+V)/2+B\) gives an open neighborhood on which
\(\psi(\beta)=\psi'(\beta)=\psi''(\beta)=0\). The complete Round-34
cell complex has only these three mask coefficients:

| cell class | coefficient |
|---|---|
| pure faces, pure axes, corner | \(\psi(\beta)\) restricted to the cell |
| connector faces and connector axes | \(\psi'(\beta)/2\) restricted to the cell |
| mixed product area | \(\psi''(\beta)/4\) |

Restrictions to \(u=0\) or \(v=0\) replace one height by zero and hence
cannot violate (35.CA1). Outside horizontal faces keep
\(|\mu|\le U,|\nu|\le V\). The two-axis displacement changes real
abscissae and finite outside boundaries but not the fixed radial height
\(t=\mp S\). Thus every cell vanishes pointwise.

There is no hidden collision distribution supported inside the zero-mask
neighborhood. An artificial radial pole requires
\(-t-\nu/2=0\), hence \(|\nu|=2S>V\); the moving arithmetic divisor
requires \(|\mu+\nu|=2S>U+V\). Neither meets the product. Coordinate-axis
residues remain multiplied by the identically zero restricted mask.

This verifies the hostile report's stronger mechanism: the beta-masked
radial-side transfer is eventually exactly zero, for any \(M\ge1\).
The accepted unmasked radial-side deletion is still needed for the global
boundary-first package, but localization of its already-separated beta
side creates no commutator. This result neither touches nor implies the
endpoint/arithmetic physical-module commutator.
