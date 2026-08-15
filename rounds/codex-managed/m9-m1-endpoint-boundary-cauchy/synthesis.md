# Round 22 synthesis: finite Cauchy collapse exposes the original-sector endpoint prefix

Campaign: `m9-m1-endpoint-boundary-cauchy`  
Round type: endpoint boundary Cauchy reduction  
Graph SHA-256 before patch: `40992c2c6154dc1ced384f8a0ebecc8bbf02e8ec502e94d55d7a6cd617880309`

## Conductor decision

Promote the exact finite \(M=1\) Cauchy reduction, its residue/orientation
ledger, and the target-safe lower radial endpoint. Retain the upper radial
endpoint, the recombined arithmetic residue, and both diagonal transition
traces as open.

All three reports independently obtain the same finite rectangle identity.
The arithmetic attack initially called its absolute upper-endpoint estimate
target-sized. A conductor normalization intervention and three independent
addenda corrected this: the endpoint polynomial is on the normalized GAR
scale, so its elementary \(O(X^{1/8}\log^2 X)\) bound becomes only
\(O(X^{3/8}\log^2 X)\) after the external \(X^{1/4}\) M1 factor is restored.
No numerical experiment or external theorem was used.

## Exact finite Cauchy identity

Let

\[
 z=u+v,\qquad p(v)=\frac34+\frac v2,\qquad
 w_a=1-\frac z2,\qquad
 \delta=w_a-p(v)=\frac14-\frac u2-v,
\]

and, for \(\xi\in\{N_X,1\}\), put

\[
 \epsilon_{N_X}=1,\qquad \epsilon_1=-1,\qquad
 E_{\xi,v}(w)=\epsilon_\xi e(\sqrt{X\xi})
 \frac{\xi^{w-p(v)}}{w-p(v)}.
\]

This is exactly the \(M=1\) endpoint term. Fix the finite Round-19
rectangle. Let \(\mathfrak T_\xi\) be its reflected terminal integral,
\(\mathfrak S_\xi\) the two radial sides with upper left-to-right and lower
right-to-left orientation, \(\mathfrak P_\xi\) the artificial-pole residue
at \(w=p(v)\), \(\mathfrak A_\xi\) the arithmetic-pole residue at
\(w=w_a\), and \(\mathfrak D_{\xi;U,V,S}\) the original right-line
integral. Then

\[
 \boxed{
 \mathfrak T_\xi+\mathfrak S_\xi+\mathfrak P_\xi
 =\mathfrak D_{\xi;U,V,S}-\mathfrak A_{\xi;U,V}.}
 \tag{22.1}
\]

Here

\[
 \mathfrak P_\xi=epsilon_\xi e(\sqrt{X\xi})
 \left\langle F_{u+v}\!\left(\frac34+\frac v2\right)\right\rangle,
\]

and

\[
 \mathfrak A_\xi=epsilon_\xi e(\sqrt{X\xi})
 \left\langle
 \frac{\xi^{1/4-u/2-v}}{1/4-u/2-v}
 L(1-u-v,\chi_4)\right\rangle,
\]

where the brackets retain the exact scale sum, floors, Mellin profiles, and
finite outside segments. The actual Round-21 operator without the reassigned
artificial residue is therefore

\[
 \mathfrak T_\xi+\mathfrak S_\xi
 =\mathfrak D_\xi-\mathfrak A_\xi-\mathfrak P_\xi.
\]

The opposite artificial residue of \(R_1\) cancels \(\mathfrak P_\xi\).
Likewise the unsplit arithmetic ledger recombines exactly as

\[
 \mathfrak R^{\rm ar}[G]-\sum_\xi\mathfrak A_\xi
 =\mathfrak R^{\rm ar}[R_1].
\]

Neither cancellation estimates the remaining operator. If \(\delta=0\),
the arithmetic and artificial poles coincide; one must take their single
double-pole derivative residue rather than add two simple residues.

## Return to original divisor variables

On the right chamber the coefficient is the original \(a_z\), not its
reflection. With \(v=b+i\nu\) and
\(\gamma=c-3/4-b/2\), define the off-centred finite Perron factor

\[
 \mathcal P_{S,\nu}^{\gamma}(y)=\frac1{2\pi i}
 \int_{\gamma-i(S+\nu/2)}^{\gamma+i(S-\nu/2)}\frac{y^r}{r}\,dr.
\]

Then \(\mathfrak D_{\xi;U,V,S}\) is exactly

\[
 \begin{aligned}
 \epsilon_\xi e(\sqrt{X\xi})
 \sum_{j,h,q}\frac{\chi_4(q)}{(hq)^{3/4}}
 \frac1{(2\pi i)^2}\iint &\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\sqrt{\frac qh}\right)^u\\
 &\times\left(\frac{H_j+1}{h}\right)^v
 \mathcal P_{S,\nu}^{\gamma}\!\left(\frac\xi{hq}\right)
 \,dv\,du .
 \end{aligned}
 \tag{22.2}
\]

This is the accepted finite-height form. At finite \(S\) the Perron factor
has no sharp support and no endpoint half weight. Only after a separately
justified symmetric Perron limit does (22.2) become

\[
 \boxed{
 \mathfrak D_{\xi;U}=epsilon_\xi e(\sqrt{X\xi})
 \sum_{hq\le\xi}^{*}\frac{\chi_4(q)}{(hq)^{3/4}}
 \mathcal H^{\rm prof}_{U,X}(h,q),}
 \tag{22.3}
\]

with every actual scale, height floor, Vaaler factor, and top star retained.

## Endpoint estimates and normalization

The accepted direct-profile bound
\(\sup_{U,h,q}|\mathcal H^{\rm prof}_{U,X}(h,q)|\ll\log(2X)\)
gives

\[
 \mathfrak D_{1;U}=O(\log X).
\]

After restoring the exact physical factor
\(-4X^{1/4}\operatorname{Re}\{e(1/8)\,\cdot\}/\pi\), this endpoint is
\(O(X^{1/4}\log X)\), hence target-safe.

For the upper endpoint, absolute summation gives only

\[
 |\mathfrak D_{N_X;U}|
 \ll N_X^{1/4}\log N_X\log(2X)
 \asymp X^{1/8}\log^2X.
\]

This is the full triangle-inequality capacity, not a saving. In physical
M1 normalization it is

\[
 O(X^{3/8}\log^2X),
\]

so it is not target-sized. The required new estimate is the signed
normalized endpoint-prefix bound

\[
 \boxed{
 \sum_{hq\le N_X}^{*}\chi_4(q)(hq)^{-3/4}
 \mathcal H^{\rm prof}_{U,X}(h,q)
 \ll_\varepsilon X^\varepsilon,}
 \tag{22.4}
\]

uniformly in the symmetric top truncation. This is an exact original-sector
return map; neither the arithmetic residue nor the already controlled
one-sided spatial cotangent boundary cancels it.

After the profile limit, its grouped coefficient is exactly
\(\mathcal C_X^*(n)\) from Round 14, but its internal radial phase has been
removed:

\[
 \mathfrak D_{N_X;\infty}
 =e(\sqrt{XN_X})
 \sum_{n\le N_X}^{*}\mathcal C_X^*(n)n^{-3/4}.
\]

GAR instead contains
\(\sum_{n\le N_X}\mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})\).
Thus the endpoint is neither a thin subtotal nor GAR up to a constant: it
is the same full angular coefficient with the useful \(n\)-dependent radial
oscillation replaced by a constant phase, apart from the single Perron half
tie. A standalone proof of (22.4) would therefore be a genuinely new
unoscillated character-prefix theorem. The more plausible next move is to
recombine it with the \(R_1\) arithmetic/transition package and test whether
the missing radial phase is restored, producing a precise return to GAR.

## State effect

- promote (22.1)--(22.3), the artificial/arithmetic residue recombination,
  the off-centred finite Perron convention, and the double-pole collision
  exception;
- promote the target-safe \(\xi=1\) endpoint bound;
- create (22.4) as the open upper radial endpoint-prefix obligation;
- reject finite-height half weights, sharp finite-Perron support, dual-series
  expansion at \(\Re s\simeq1/4\), and the claim that the unsigned
  \(X^{1/8}\) inner bound is target-sized;
- retain the recombined arithmetic residue, transition traces, GAR, M9-M1,
  M9-M2, M9, and the Gauss-circle target as open.
