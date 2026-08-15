# Conductor adjudication: the terminal norm is hybrid

Campaign: `m9-m1-beta-translation-divided-difference`  
Role: claimant/hostile seam adjudication  
Allocation: analytical/algebraic only

## 1. Exact fixed-height identity

Let

\[
y=L-\nu,\qquad F(L,y)=H(L,L-y).
\]

At fixed physical height \(\nu\),

\[
\partial_LH=F_L+F_y,
\qquad
(\partial_L+\partial_\nu)H(L,L)=F_L(L,0).
\]

Therefore

\[
\boxed{
\mathfrak E_H
=\int_0^1F_{Ly}(L,ty)\,dt
+\int_0^1tF_{yy}(L,ty)\,dt.}                    \tag{40.C5}
\]

The control \(F(L,y)=ay+by^2/2\) gives \(\mathfrak E_H=b/2\), so the
earlier fixed-\(y\) formula with \(-F_y(L,0)/y\) is false for the
declared fixed-\(\nu\) derivative. All three reports agree on (40.C5).

Equation (40.C5) is signed algebra. For the actual separated profile,
the two displayed integrals are individually of order \(\lambda^{-1}\)
on a long translated segment although their recombination can be
\(O_b(\lambda^{-5})\). They may not be estimated term by term.

## 2. Exact Cauchy obstruction and repair

The singular regularizer contains the independent term

\[
K_C(L,\nu)=-\frac{iH_0(L)}{2A(L)D(L,\nu)},
\quad
H_0(L)=H(L,L),
\quad
D=A+\frac i2(L-\nu).
\]

Since \(D=-i\nu/2+O_L(1)\),

\[
K_C(L,\nu)=\frac{H_0(L)}{A(L)\nu}+O_L(\nu^{-2}). \tag{40.C6}
\]

Thus the complete regularizer is not in \(L^1(d\nu)\) whenever
\(H_0(L)\ne0\). This already occurs for the accepted actual separated
kernel \(H(L,\nu)=f_b(\nu)\). It corrects the Round-31 claim of a
pointwise integrable height weight.

For

\[
I_{U,V}(L)=[-V,V]\cap[L-U,L+U]=[p(L),q(L)]
\]

and the continuous logarithm on the left half-plane,

\[
\boxed{
\int_{p(L)}^{q(L)}K_C(L,\nu)\,d\nu
=\frac{H_0(L)}{A(L)}
 \{\Log D(L,q(L))-\Log D(L,p(L))\}.}             \tag{40.C7}
\]

The logarithmic factor has supremum plus variation
\(O(\log(2+\lambda))\) uniformly in the physical cutoffs on a signed
cell. For the actual separated profile,

\[
\left|\frac{f_b(L)}{A(L)}\right|\ll_b\lambda^{-4},
\qquad
\operatorname {Var}_{I_\lambda}\frac{f_b(L)}{A(L)}
\ll_b\lambda^{-4},                               \tag{40.C8}
\]

so (40.C7) has target-safe sup/BV size
\(O_b(\lambda^{-4}\log(2+\lambda))\). It remains target-safe when the
incomplete-Fresnel operator is applied after the signed section is
formed. On symmetric exhaustion, (40.C7) tends to
\(i\pi H_0(L)/A(L)\) with this branch convention.

The explicit face log and (40.C7) must use the same endpoints, branch,
stars, and collision ownership. Pointwise Morse localization before
forming (40.C7) recreates the false absolute tail.

## 3. What is and is not closed

For the separated actual kernel, the remaining off-diagonal term

\[
K_\Delta(L,\nu)
=\frac{f_b(\nu)-f_b(L)}{(L-\nu)D(L,\nu)}
\]

has the required absolute value, fixed-height derivative, and moving
trace bounds by the physical-center/diagonal/radial-ridge partition.
Together with (40.C7), this repairs the separated finite-section BV and
local \(q^{-2}\) conclusion without an integrable majorant for the whole
kernel.

The discovery report proposes the exact singular-cell factorization
\(H^\circ(L,\nu)=G^\circ(L)p_b(\nu)\) and claims the same result for all
off-diagonal, smooth, connector, moving-face, and exact Morse pieces. The
factorization is lawful on a frozen separated singular share. It is not,
as written, an exact all-strata formula: smooth shares contain
\(\widehat W_j(a+i(L-\nu))\), and common artificial ownership, affine
restrictions, and the normalized Morse remainder require their own
one-count formulas. The report's region estimates do not expand those
complete factors or validate every induced trace. The hostile report
independently identifies this seam.

Accordingly, the complete terminal bound is not promoted. The next
kernel is narrower than before: prove a hybrid norm consisting of the
already-controlled signed diagonal section and an absolute, cancellation-
preserving off-diagonal/smooth norm. In the off-diagonal proof, evaluate
the long translation as endpoint divided differences before taking
absolute values.

No numerical experiment or external theorem is used.
