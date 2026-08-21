# Conductor Round 113 ownership and scope review

## Smooth gcd one-count

For a fixed balanced residual block, put

\[
 G_0=\frac{\sqrt L}{2},\qquad
 S=\max(0,\lceil\log_2G_0\rceil),\qquad G_s=2^{-s}G_0.
\]

For (0\le s<S), set (\psi_s(g)=W(g/G_s)). With

\[
 c_L=\eta(1/G_S),\qquad \psi_{\mathrm{bot}}(g)=c_LW(g),
\]

the positive-integer telescope is exact:

\[
 \sum_{s=0}^{S-1}\psi_s(g)+\psi_{\mathrm{bot}}(g)
 =\eta(g/G_0),
\]

because (G_S\in[1/2,1]) and
(\eta(g/G_S)=c_LW(g)) for every positive integer (g). Hence

\[
 \psi_{\mathrm{hi}}(g)=1-\eta(g/G_0)
\]

is the unique high/crossing owner. Its contribution is
(O(L^{3/2})) in the balanced range (L\le K\le16L).

For a low shell (\sigma), write (h=gu), (k=gv),
((u,v)=1), and define

\[
 F_{B,\sigma,u,v}(t)=\vartheta_\sigma(t)
 A_B(G_\sigma tu,G_\sigma tv).
\tag{113.R4}
\]

The positive-quadrant zero extension makes (113.R4) a literal real
(C_c^\infty) profile. Its support and every derivative seminorm are
uniform in real (X), floors, (B), the gcd shell, and the bottom
coefficient. The ray and Fourier sums are finite or absolutely convergent.

## Quarter packet

Using

\[
 \widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt,
 \qquad
 \chi_4(g)=\frac{e(g/4)-e(3g/4)}{2i},
\]

Poisson gives

\[
 \mathcal T_B^{\mathrm{low}}
 =\frac1{2i}\sum_{\sigma\in\Sigma_L}G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(R),
\tag{113.R5}
\]

where (Q^{\mathrm{full}}) is exactly the (1/4) packet minus the
(3/4) packet and retains (\chi_4(u)). For real profiles,

\[
 Q_{B,\sigma}^{\mathrm{full}}(-R)
 =-\overline{Q_{B,\sigma}^{\mathrm{full}}(R)}.
\tag{113.R6}
\]

The minus sign in (113.R6) cancels the sign from conjugating (1/(2i)),
so the physical frequency recombination is correct.

## Owner corrections and physical equality

High gcd is assigned first. Inside the low part, exact squares precede
nonsquare (R^{-1})-near-squares. Denote their exact signed weighted
subtotals by (\mathcal S_B^{\mathrm{sq}}) and
(\mathcal S_B^{\mathrm{near}}). No arithmetic owner-complement mask is
inserted into the smooth profile (113.R4). Define

\[
 \mathcal T_B^{\mathrm{res}}
 =\frac1{2i}\sum_\sigma G_\sigma Q_{B,\sigma}^{\mathrm{full}}(R)
 -\mathcal S_B^{\mathrm{sq}}-\mathcal S_B^{\mathrm{near}}.
\tag{113.R7}
\]

Then the exact coefficient and physical one-count equations are

\[
 \mathcal T_B
 =\mathcal T_B^{\mathrm{hi}}
  +\mathcal S_B^{\mathrm{sq}}
  +\mathcal S_B^{\mathrm{near}}
  +\mathcal T_B^{\mathrm{res}},
\tag{113.R8}
\]

\[
 B_{2,B}=8\operatorname{Re}\!\left[
 -c_B(\mathcal T_B^{\mathrm{hi}}+\mathcal S_B^{\mathrm{sq}}
 +\mathcal S_B^{\mathrm{near}}+\mathcal T_B^{\mathrm{res}})
 +E_{B,\mathrm{tr}}\right].
\tag{113.R9}
\]

The high, square, near-square, and transform-error tags are target-safe.
After they are subtracted, the literal balanced physical residual is
(8\operatorname{Re}[-c_B\mathcal T_B^{\mathrm{res}}]).

## First analytic gap

The first unproved assertion is now unambiguously

\[
 \boxed{
 \left|\sum_{\sigma\in\Sigma_L}G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
 }
\tag{113.R10}
\]

for each fixed physical residual block (B). The modulus is outside the
complete internal gcd sum. Distinct (D)- or (L)-blocks are not combined.
Shellwise (\ell^1), product-fibre absolute bounds, and arbitrary-weight
Gram inequalities are stronger and are not consequences of the dictionary.

## Capacity and recommendation

The dictionary is capacity-preserving. The existing envelope loses

\[
 \min(L^{1/2},R^{1/2}/L),
\]

with worst deficit (R^{1/6}=X^{1/12}) at (L=X^{1/6}). Round 113
therefore closes the literal-definition and one-count seam only. Promote a
proved dictionary connector, attach it as a dependency of the open balanced
estimate, and leave all three M9-M2 analytic parents and every exponent
claim unchanged.
