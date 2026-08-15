# Conductor review: complete diagonal composition

Campaign: `m9-m1-beta-off-diagonal-product-cell`  
Round: 41  
Allocation: 100% analytical/algebraic

## Verdict

The Round-40 signed diagonal lemma extends directly from the separated
profile to the exact Round-41 product cell.  This closes a necessary seam
before composing the off-diagonal estimate into the hybrid terminal bound.

For one singular product cell write

\[
 H(L,\nu)=C(\beta)G(L;\lambda)p(\nu),\qquad
 H(L,L)=C(\beta)G(L;\lambda)p(L).                     \tag{41.C16}
\]

On \(|L+\beta|\asymp\lambda\), the accepted product-symbol estimates give

\[
 |G|\ll P_X,\quad |G'|\ll P_X\lambda^{-1},\quad
 |p(L)|+|p'(L)|\ll P_X\lambda^{-3}.                   \tag{41.C17}
\]

With \(A=-1-b/2-i(L+\beta)\), the exact signed diagonal section is

\[
 C_{U,V}[H](L)=\frac{H(L,L)}{A(L)}
 \{\Log D(L,q_{U,V}(L))-\Log D(L,p_{U,V}(L))\}.       \tag{41.C18}
\]

Its scalar coefficient \(c(L)=H(L,L)/A(L)\) obeys

\[
 \|c\|_\infty\ll P_X\lambda^{-4},\qquad
 \operatorname{Var}_{I_\lambda}c\ll P_X\lambda^{-3}.\tag{41.C19}
\]

The exact affine-endpoint logarithm has uniformly

\[
 \|J_{U,V}\|_\infty+\operatorname{Var}J_{U,V}
 \ll\log(2+\lambda).                                 \tag{41.C20}
\]

Therefore

\[
 \|C_{U,V}[H]\|_\infty+
 \operatorname{Var}C_{U,V}[H]
 \ll P_X\lambda^{-3}\log(2+\lambda)
 \ll_\varepsilon X^\varepsilon\lambda^{-2}.          \tag{41.C21}
\]

The same bound controls the exact normalized Morse remainder after the
signed section is formed, by the incomplete-Fresnel BV inequality.  Upper
moving faces retain positive sign, lower moving faces negative sign, and
the common logarithm branch and collision ownership are unchanged.

Thus the signed diagonal plus the Round-41 off-diagonal/smooth theorem is
the complete corrected hybrid bound for every post-routing large-alpha
cell.  The unintegrated diagonal kernel still has a nonzero \(1/\nu\) tail
and must never be put under an absolute height norm.

