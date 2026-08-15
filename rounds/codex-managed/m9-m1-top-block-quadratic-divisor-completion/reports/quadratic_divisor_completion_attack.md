# Round 59 discovery report: exact quadratic completion and a coefficient self-return

## 1. Result: exact stationary self-return and an equivalent-hard dual strip

For
\[
 g_h(n)=\mathbf 1_{h\mid n}\chi_4(n/h),
\]
finite Fourier inversion modulo \(4h\) gives
\[
\boxed{
 g_h(n)=-{i\over2h}\sum_{a\bmod 4h}\chi_4(a)
 e\left({an\over4h}\right).}
\tag{1.1}
\]
After inserting (1.1), write
\[
 f_{h,a,k}(x)=\sqrt{Xx}+{ax\over4h}-kx,\qquad r=4hk-a.
\]
The positive stationary cone is
\[
 2h\sqrt{X/B}\leq r\leq2h\sqrt{X/A},
\tag{1.2}
\]
and
\[
 x_*={4Xh^2\over r^2},\qquad f(x_*)={Xh\over r},\qquad
 |f''(x_*)|^{-1/2}
 ={4\sqrt2\,X^{1/2}h^{3/2}\over r^{3/2}}.
\tag{1.3}
\]
Since \(f''(x_*)<0\), the Gaussian is \(e(-1/8)\).  Also
\(\chi_4(a)=\chi_4(-r)=-\chi_4(r)\).  The projector, character sign,
and Gaussian therefore combine as
\[
 {-i\over2h}(-\chi_4(r))e(-1/8)
 ={\chi_4(r)\over2h}e(1/8).
\]
Thus the exact smooth-interior stationary contribution is
\[
\boxed{
 P_J^{\rm stat}
 =2\sqrt2\,e(1/8)X^{1/2}
 \sum_{R/4<h\leq R/2}\ \sum_{r\in\mathcal C_h(J)}^{*}
 \chi_4(r)h^{1/2}r^{-3/2}
 \Omega_X^*(n_*(h,r),h)e(Xh/r).}
\tag{1.4}
\]
Here the star gives half a stationary main term when \(x_*=A\) or \(B\);
artificial window endpoints themselves remain full owners.

The decisive identity is
\[
\boxed{2h\sqrt{X/n_*(h,r)}=r.}
\tag{1.5}
\]
Hence the actual angular symbol returns exactly:
\[
\boxed{
 \Omega_X^*(n_*(h,r),h)
 =\sum_j\mathbf 1_{h\leq H_j}
 \Phi\left({h\over H_j+1}\right)[w_j(r)]^*.}
\tag{1.6}
\]
Profiles, height floors, hard top, and angular stars are not smoothed by
the B-process.  On the critical top block \(r\asymp\sqrt X=R^2\), one
has \(H_r\asymp rX^{-1/4}\asymp R\): this is the original
frequency-first terminal M1 architecture in reciprocal coordinates.

For a short physical window \(|J|\leq R\), each cone (1.2) has thickness
\[
 |\mathcal C_h(J)|\ll {h\sqrt X\,|J|\over R^3}+1\ll R,
\tag{1.7}
\]
and generically has size \(\asymp R\) when \(|J|\asymp R\).  Thus the
stationary dual support has \(R^2\) raw capacity, not \(R\).  Since the
stationary coefficient is \(\asymp R^{-1/2}\), a signed raw
\(O_\epsilon(X^\epsilon R)\) theorem is essential; counting gives only
\(O_\epsilon(X^\epsilon R^2)\), losing a full factor \(R\).

It does not prove the complete short-window theorem.  The exact symbol
and artificial hard endpoints are not a smooth compact amplitude with a
known uniform transform error.  More fundamentally, even its stationary
dual strip needs the unproved signed raw \(O(RX^\epsilon)\) estimate.
This is the first rigorous obstruction; endpoints and nonstationary pieces
are an additional transform seam.

The same \(R\)-thick raw dual geometry returns coefficient-for-coefficient
to the existing
terminal M1 kernel.  The conductor's proposed frequency-first bound
\(O(1+D/L)=O(R)\) may close a terminal sector, but the authorized context
does not identify the entire high-\(h\) dual image with that theorem,
including its \(D,L\) ownership and boundary terms.  No aggregate GAR
closure is licensed here.

## 2. Exact statement and hypotheses

Let \(Y=R^2\asymp\sqrt X\), let
\(J=[A,B]\cap\mathbb Z\subset[cY,CY]\) have
\(\ell=B-A+1\leq R\), and restrict \(R/4<h\leq R/2\).  The exact sum is
\[
 P_J=\sum_{n\in J}^{*}e(\sqrt{Xn})
 \sum_{\substack{h\mid n\\R/4<h\leq R/2}}
 \chi_4(n/h)\Omega_X^*(n,h).
\tag{2.1}
\]
Because \(\chi_4\) vanishes on evens, the odd-quotient condition is
implicit.  The radial star is inherited; membership in \([A,B]\) is a
full artificial cutoff.

Equation (1.1) gives the exact completed primal identity
\[
\boxed{
 P_J=-{i\over2}\sum_{R/4<h\leq R/2}{1\over h}
 \sum_{a\bmod4h}\chi_4(a)
 \sum_{n\in J}^{*}\Omega_X^*(n,h)
 e\left(\sqrt{Xn}+{an\over4h}\right).}
\tag{2.2}
\]
For \(V_h\in C_c^\infty((A,B))\), define
\[
 S_h(V_h)
 =-{i\over2h}\sum_{a\bmod4h}\chi_4(a)
 \sum_{n\in\mathbb Z}V_h(n)
 e\left(\sqrt{Xn}+{an\over4h}\right).
\tag{2.3}
\]
Poisson summation is exact:
\[
 S_h(V_h)
 =-{i\over2h}\sum_{a\bmod4h}\chi_4(a)
 \sum_{k\in\mathbb Z}
 \int_{\mathbb R}V_h(x)e(f_{h,a,k}(x))\,dx.
\tag{2.4}
\]
Put
\[
 \mathcal C_h(J)
 =\{r\in\mathbb Z:
 2h\sqrt{X/B}\leq r\leq2h\sqrt{X/A}\}.
\tag{2.5}
\]
Every integer \(r\) has the unique representation
\[
 a\equiv-r\pmod{4h},\quad 0\leq a<4h,\qquad
 k={r+a\over4h}\in\mathbb Z.
\tag{2.6}
\]
Thus the stationary map preserves multiplicity.  If \(x_*\) stays in
the smooth interior and \(V_h\) has uniform normalized derivative bounds,
then
\[
\begin{split}
 S_h(V_h)^{\rm stat}
 ={}&2\sqrt2\,e(1/8)X^{1/2}
 \sum_{r\in\mathcal C_h(J)}
 \chi_4(r)h^{1/2}r^{-3/2}\\
 &\times V_h(4Xh^2/r^2)e(Xh/r)
 +\mathcal E_h(V_h).
\tag{2.7}
\end{split}
\]
At \(x_*=A\) or \(B\), the stationary main has half weight.  Formula
(2.7) is asserted only with the displayed smooth-interior hypotheses;
applying it to the hard actual symbol needs a one-sided or BV transform.

Choose an integer \(K\) and shear
\[
 r=4Kh+s,\qquad \Phi_K(h,s)={Xh\over4Kh+s}.
\tag{2.8}
\]
On character support,
\[
 \chi_4(r)=\chi_4(s).
\tag{2.9}
\]
Direct differentiation gives
\[
 \boxed{\det\nabla^2\Phi_K(h,s)
 =-{X^2\over(4Kh+s)^4}.}
\tag{2.10}
\]
For a length-\(R\) window the lawful support is a sheared strip with
\(h\)-length \(\asymp R\), transverse thickness \(O(R)\), generically
\(\asymp R\) when the window length is \(\asymp R\), and total raw
lattice capacity \(O(R^2)\).

## 3. Proof and derivation

### 3.1 Exact projector and character sign

If \(h\nmid n\), orthogonality modulo \(h\) makes the right side of
(1.1) zero: writing \(a=b+4t\), the \(t\)-sum is
\(\sum_{t\bmod h}e(tn/h)\).  If \(n=hm\), then
\[
\sum_{a\bmod4h}\chi_4(a)e(am/4)
=h\sum_{b\bmod4}\chi_4(b)e(bm/4),
\]
and
\[
\sum_{b\bmod4}\chi_4(b)e(bm/4)
=
\begin{cases}
2i,&m\equiv1\pmod4,\\
-2i,&m\equiv3\pmod4,\\
0,&m\equiv0,2\pmod4.
\end{cases}
\tag{3.1}
\]
Multiplication by \(-i/(2h)\) gives \(1,-1,0,0\), proving (1.1).
The congruence \(a\equiv-r\pmod{4h}\) also proves
\[
 \chi_4(a)=\chi_4(-r)=-\chi_4(r).
\tag{3.2}
\]

### 3.2 Radial B-process normalization

The derivatives are
\[
 f'(x)={\sqrt X\over2\sqrt x}-{r\over4h},\qquad
 f''(x)=-{\sqrt X\over4x^{3/2}}<0.
\tag{3.3}
\]
At the saddle,
\[
 |f''(x_*)|={r^3\over32Xh^3},\qquad
 |f''(x_*)|^{-1/2}
 ={4\sqrt2\,X^{1/2}h^{3/2}\over r^{3/2}}.
\tag{3.4}
\]
In the convention \(e(t)=e^{2\pi it}\), stationary phase contributes
\(e(f(x_*))e(-1/8)|f''(x_*)|^{-1/2}\).  Since
\[
 i\,e(-1/8)=e(1/8),
\]
the projector and character sign give the coefficient in (1.4).
For \(h\asymp R\), \(r\asymp R^2\), and \(X\asymp R^4\),
\[
 2\sqrt2\,X^{1/2}h^{1/2}r^{-3/2}\asymp R^{-1/2}.
\tag{3.5}
\]
Therefore a raw \(O_\epsilon(X^\epsilon R)\) bound is exactly the
unweighted \(O_\epsilon(X^\epsilon\sqrt R)\) target.

### 3.3 Exact dual strip and anisotropic Hessian

The cone width is
\[
\begin{split}
 |\mathcal C_h(J)|
 &\leq2h\sqrt X\left({1\over\sqrt A}-{1\over\sqrt B}\right)+1\\
 &={2h\sqrt X(B-A)\over
 \sqrt A\sqrt B(\sqrt A+\sqrt B)}+1
 \ll {h\sqrt X\,\ell\over R^3}+1
 \asymp {h\ell\over R}+1.
\tag{3.6}
\end{split}
\]
For \(h\asymp R\) and \(\ell\asymp R\), this is \(\asymp R\), and
there are \(\asymp R\) admissible \(h\)'s.  Thus the general capacity is
\[
 \#\{(h,r):h\in\mathcal I_R,\ r\in\mathcal C_h(J)\}
 \ll R\ell+R\ll R^2.
\tag{3.7}
\]
For a uniformly bounded transformed interior symbol, absolute values give
\[
 \sum_h\sum_{r\in\mathcal C_h(J)}
 |\chi_4(r)W_X(h,r)|\ll R^2,
\tag{3.8}
\]
which is a factor \(R\) above the required raw bound.

Writing \(d=4Kh+s\), one has
\[
 \Phi_{hh}=-{8KXs\over d^3},\qquad
 \Phi_{hs}={X(4Kh-s)\over d^3},\qquad
 \Phi_{ss}={2Xh\over d^3},
\]
which proves (2.10).  On \(h,s,K\asymp R\), \(d\asymp R^2\),
the Hessian entries have scales at most \(1,1,R^{-1}\), while the mixed entry
is \(\asymp1\) and the determinant is \(\asymp-1\), its two eigenvalues
are both \(\asymp1\) in magnitude with opposite signs.  This full real
rank is still not a modulo-one lattice theorem.

### 3.4 Exact actual-symbol self-return

The accepted symbol is
\[
 \Omega_X^*(n,h)=\sum_j\mathbf1_{h\leq H_j}
 \Phi\left({h\over H_j+1}\right)
 \left[w_j\left(2h\sqrt{X/n}\right)\right]^*.
\tag{3.9}
\]
Substituting \(n_*=4Xh^2/r^2\) proves (1.5)--(1.6).  Hence:

1. the transform does not create a generic smooth \(W_X(h,r)\);
2. angular equalities become integer \(r\)-profile equalities with their
   original stars;
3. \(H_j=\lfloor D_jX^{-1/4}\rfloor\) remains unchanged, and on
   \(D_j\asymp r\asymp R^2\) it is \(\asymp R\).

Already for a physical window of length \(\asymp R\), (3.6) gives
\(|\mathcal C_h|\asymp R\), hence \(R^2\) raw capacity.  The required
raw \(O(RX^\epsilon)\) estimate needs the original
frequency-first character/divisor cancellation.  The transform has
returned to that terminal architecture rather than created a new
two-dimensional estimate.

The possible shortcut \(O(1+D/L)=O(R)\) cannot be promoted from the
authorized context.  Round 14 records the global recombination and Hardy
return, but not a common-antecedent theorem identifying the entire
high-\(h\) image of (1.4) with one accepted terminal-frequency sector.
That audit must retain the exact \(D,L\) partition and all boundary terms.

### 3.5 Endpoint and nonstationary obstruction

For a hard endpoint, integration by parts produces the boundary trace
\[
 \left.
 {V_h(x)e(f_{h,a,k}(x))\over2\pi i f'_{h,a,k}(x)}
 \right|_{A}^{B}
\tag{3.10}
\]
when no saddle meets the endpoint.  If a saddle coalesces with it, a
uniform Fresnel transition replaces (3.10); an interior half-saddle alone
is not a uniform error theorem.  The exact object additionally contains
the hard top, angular stars after \(d=r\), the independent radial star,
and height-floor/profile seams.

There are \(O(R)\) original \(h\)-rows, and the inherited fourth-power
family has \(\gg R\) strict full-amplitude rows.  Therefore separate
absolute treatment of primal boundary and nonstationary pieces has the
ledger
\[
 O_\epsilon(X^\epsilon R),
\tag{3.11}
\]
which misses the unweighted short-window target by \(\sqrt R\); it does
not receive the stationary \(R^{-1/2}\) prefactor.  No theorem for the
complete moving traces occurs in the authorized context.  This seam is
additional to the already open signed stationary-strip estimate.

### 3.6 Character and fourth-power resonance controls

With \(r=4Kh+s\),
\[
 {Xh\over4Kh+s}
 ={X\over4K}-{Xs\over16K^2h}
 +{Xs^2\over64K^3h^2}
 +O\left({X|s|^3\over K^4h^3}\right).
\tag{3.12}
\]
At \(X=L^4\), near \(n=L^2+t\),
\[
 \sqrt{Xn}
 =L^3+{L\over2}t-{t^2\over8L}
 +O\left({|t|^3\over L^3}\right).
\tag{3.13}
\]
The linear term can be integral or half-integral.  Further,
\[
 \chi_4(s)={e(s/4)-e(3s/4)\over2i}
\tag{3.14}
\]
only shifts an \(s\)-frequency by \(\pm1/4\); it does not exclude
integer or quarter-integral resonance.  A bilinear phase \(e(ms)\) is
fully coherent on the integer lattice despite nonzero mixed derivative.

The exponent ledger is:

| owner or method | raw size | after stationary normalization |
|---|---:|---:|
| short-window stationary-strip capacity | \(R^2 X^\epsilon\) | \(R^{3/2} X^\epsilon\), loses \(R\) |
| short-window hard edge/nonstationary ledger | \(R X^\epsilon\) | no stationary prefactor |
| required signed stationary raw bound | \(R X^\epsilon\) | \(\sqrt R X^\epsilon\), target |
| exact transformed symbol | original terminal M1 architecture | no new saving |

## 4. First doubtful or unproved step

For a short window, the first unproved step is the signed raw stationary
strip theorem
\[
 \left|\sum_{h\asymp R}\sum_{r\in\mathcal C_h(J)}^{*}
 \chi_4(r)W_X(h,r)e(Xh/r)\right|
 \ll_\epsilon X^\epsilon R,
\tag{4.1}
\]
with the exact returned symbol and its floors, hard top, and stars.
Counting gives only \(O(X^\epsilon R^2)\).  A second unproved seam is a
uniform exact-symbol B-process bounding the edge and nonstationary pieces
by \(O_\epsilon(X^\epsilon\sqrt R)\).

For the full block, the alternative first unproved step is
\[
 \text{full high-\(h\) image of (1.4)}
 =\text{accepted terminal-frequency M1 sector}
 +O_\epsilon(X^\epsilon R)
\tag{4.2}
\]
at raw scale.  Identity (1.6) proves the coefficient match but not the
\(D,L\) ownership or endpoint ledger.  Completing instead to the full
\(r_2\) radial sum invokes the Hardy return and is equivalent-hard.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| projector constant | Pass. The four residues in (3.1) give \(1,-1,0,0\) after multiplication by \(-i/(2h)\). |
| B-process normalization | Pass for smooth interior saddles. Equations (3.3)--(3.5) give \(e(-1/8)\) before character recombination and the final \(2\sqrt2\,e(1/8)X^{1/2}h^{1/2}r^{-3/2}\). |
| dual strip geometry | Corrected. For \(|J|\asymp R\), \(|dr/dn|\asymp1\), so the transverse thickness is \(\asymp R\) and raw capacity is \(\asymp R^2\). |
| Hessian and rank | Pass as geometry only. Its eigenvalues are both \(\asymp1\) in magnitude with opposite signs; determinant \(\asymp-1\) is not a lattice theorem. |
| character resonance | Pass. The signs, shear \(\chi_4(r)=\chi_4(s)\), and quarter modes (3.14) are retained. |
| actual amplitude | Pass with exact self-return: (1.5)--(1.6) restore \(w_j(r)\), floors, hard top, and Vaaler factors. |
| endpoints and stars | Open transform seam. Artificial edges are full; transform equalities, angular stars, and the radial star are distinct. |
| perfect fourth power | Pass. Equation (3.13) retains the integral/half-integral linear and critical quadratic terms. |
| target ledger | Pass. The stationary strip has raw \(R^2\) capacity and needs a signed raw \(R\) theorem. |
| source applicability | No external theorem imported. A generic Hessian theorem does not by itself control the modulo-one resonances or discontinuous actual symbol. |
| downstream scope | Pass. No lower-shell, alpha, GAR, M9-M1, M9, or exponent closure is asserted. |

## 6. Dependencies and exact artifacts used

Only the task-authorized artifacts were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/synthesis.md`;
- `rounds/codex-managed/m9-m1-top-block-low-leg-curvature/synthesis.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`.

No external theorem, web source, unlisted artifact, or numerical
experiment was used.  The work is 100% analytical/algebraic.

## 7. Recommended state effect

Promote after independent validation the projector (1.1), stationary map
and normalization (1.2)--(1.4), corrected strip capacity (3.6)--(3.8),
and coefficient self-return (1.5)--(1.6).  The self-return is the central
structural result: completion restores the original integer angular
profile and height architecture exactly.

Do not promote a stationary square-root bound: even a length-\(R\)
window gives \(R^2\) raw stationary capacity, and (4.1) is open.  The
hard edge, nonstationary, and exact-symbol transform error are separate
open seams.

Retain the possible full-block terminal-frequency shortcut as an audit
target, not a theorem.  It requires (4.2) with exact \(D,L\) sectors and
boundary owners.  Retain the high shell, lower shell, alpha transfer,
GAR, M9-M1, M9, and the Gauss-circle exponent open.
