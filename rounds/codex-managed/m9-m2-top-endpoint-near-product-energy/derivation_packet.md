# Round 75 derivation packet: character-preserving near-product energy

Campaign: m9-m2-top-endpoint-near-product-energy  
Round: 75  
Starting graph SHA-256:
b5aa6150a62e1ecc21045c21bcb4af9ede4ab164545b43a93756e53fcc402bd2

## 1. Frozen top-cone target

Put

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,
 \qquad H=\lfloor yX^{-1/4}\rfloor,
\]

and, for dyadic \(1\leq L\leq H\),

\[
 a(h,m)=\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right).
 \tag{75.1}
\]

The open estimate is

\[
 \mathcal T_L
 =\sum_{\substack{h\asymp L\\h\ \mathrm{odd}}}
 \chi_4(h)\sum_{m=\lceil h/4\rceil}^{h}
 a(h,m)e(J\sqrt{hm})
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{75.2}
\]

The exact positive physical factor is
\(-2\pi^{-1}e(1/8)X^{1/4}L^{-3/2}\), counted once; the
negative frequency is the conjugate.  Bounded \(L\) and \(L\asymp H\)
are inherited safe.  Round 74 proved only a stronger sufficient
row-correlation reduction.

## 2. Candidate boundary separation

Let \(B=\lceil\sqrt L\rceil\).  The two strips

\[
 0\leq m-\lceil h/4\rceil\leq2B,\qquad
 0\leq h-m\leq2B
 \tag{75.3}
\]

contain \(O(LB)=O(L^{3/2})\) bounded terms and are target-safe
absolutely.  The candidate construction inserts complementary smooth
collars between widths \(B\) and \(2B\), then partitions the remaining
ratio range into \(O(\log L)\) smooth layers \(\tau\).

This step must be validated with the exact ceiling, \(q_X\neq1\), the
flat upper profile, and uniform summed derivative costs.  A collar
defined by additive distance depends on both the radial coordinate and
the angular coordinate; it may not be replaced by a fixed angular
cutoff.

## 3. Candidate quarter-shift normal form

Use

\[
 \chi_4(h)=\frac{e(h/4)-e(-h/4)}{2i}.
 \tag{75.4}
\]

For one smooth layer, two-dimensional Poisson has phase

\[
 J\sqrt{xm}+\frac{\rho x}{4}-ux-lm,\qquad \rho\in\{-1,1\}.
\]

With \(m=xt^2\), its angular phase is

\[
 x\Psi(t),\qquad
 \Psi(t)=Jt+\frac{\rho}{4}-u-lt^2.
\]

The stationary data are

\[
 t_0=\frac{J}{2l},\qquad
 j=4u-\rho,\qquad
 \Psi(t_0)=\frac{X-jl}{4l},\qquad
 W\!\left(\frac{\sqrt{q_X}}{2t_0}\right)=W(l/y).
 \tag{75.5}
\]

Thus \(j\) is odd, \(J<j<2J\), and \(J/2<l<J\), up to the
layer margins.  The angular phase is exactly quadratic,
\(\Psi(t)=\Psi(t_0)-l(t-t_0)^2\), and

\[
 \int_{\mathbb R}e(-xlv^2)\,dv
 =\frac{e(-1/8)}{\sqrt{2xl}}.
 \tag{75.6}
\]

Because \(\rho=-\chi_4(j)\), the quarter-shift coefficient and (75.6)
combine to \(e(1/8)\chi_4(j)\).

The candidate complete interior identity is

\[
 \mathcal T_{L,\mathrm{int}}
 =e(1/8)L^{3/2}X^{-1/4}\mathcal D_L
 +O_A(L^{3/2}X^{-A}),
 \tag{75.7}
\]

where all \(O(\log L)\) layers and actual collar amplitudes are retained.
The exact constant, the error after summing all aliases/layers, and the
absence of an omitted endpoint functional are validation obligations,
not accepted inputs.

## 4. Actual moving wavelet and exact energy interface

For a layer \(\tau\), let

\[
 \mathcal K_{\tau,l}(s)
 =\int_{\mathbb R}\kappa_{\tau,l}(z)e(sz)\,dz
 \tag{75.8}
\]

be the radial Fourier transform obtained after evaluating the complete
two-variable collar/layer symbol at \(t_0=J/(2l)\) and scaling \(x=Lz\).
The dependence on \(l\) is retained.  The candidate dual is

\[
 \mathcal D_L
 =\sum_\tau\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
 \chi_4(j)\sum_{l\asymp J}
 F_{\tau,j}(l),
 \tag{75.9}
\]

\[
 F_{\tau,j}(l)
 =W(l/y)\,
 \mathcal K_{\tau,l}\!\left(\frac{L(X-jl)}{4l}\right).
 \tag{75.10}
\]

Rapid radial decay should localize (75.9) to

\[
 |X-jl|\ll_A \frac{JX^\varepsilon}{L}.
 \tag{75.11}
\]

The cone target becomes

\[
 \mathcal D_L\ll_\varepsilon J^{1/2}X^\varepsilon.
 \tag{75.12}
\]

Extend each \(F_{\tau,j}\) smoothly by zero with its exact margins and
define, without approximation,

\[
 \widehat F_{\tau,j}(k)
 =\int_{\mathbb R}F_{\tau,j}(\lambda)e(-k\lambda)\,d\lambda
 =\frac1L b_{\tau,j,k}e(-kX/j).
 \tag{75.13}
\]

Poisson in the uncharactered \(l\)-leg then gives

\[
 \mathcal D_L
 =\frac1L\sum_{k\in\mathbb Z}S_k,\qquad
 S_k=\sum_\tau\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
 \chi_4(j)b_{\tau,j,k}e(-kX/j).
 \tag{75.14}
\]

The required symbol facts are

\[
 b_{\tau,j,k}\ll_A X^\varepsilon(1+|k|/L)^{-A},
 \qquad
 \sum_{\tau,j,k}|b_{\tau,j,k}|^2
 \ll_\varepsilon LJX^\varepsilon.
 \tag{75.15}
\]

They must be proved for the complete moving amplitude, rather than
inferred from a fixed-\(l\) model.  Given (75.15), Cauchy reduces
(75.12) to the diagonal-scale estimate

\[
 \boxed{\ \sum_{|k|\ll LX^\varepsilon}|S_k|^2
 \ll_\varepsilon LJX^\varepsilon.\ }
 \tag{75.16}
\]

The diagonal \(j=j'\) is target-safe by (75.15).  The exact off-diagonal
is the candidate analytic survivor.

## 5. Self-return and capacity controls

The character comb is

\[
 \sum_{j\in\mathbb Z}\chi_4(j)e(-j\xi)
 =\frac1{2i}\left\{
 \sum_n\delta(\xi-n-1/4)
 -\sum_n\delta(\xi-n+1/4)\right\}.
 \tag{75.17}
\]

Fourier inversion in the character-bearing \(j\)-leg should restore the
two short quarter shifts, \(\chi_4(h)\), \(W(l/y)\), and the original top
reciprocal block.  This is a candidate exact self-return; the common
antecedent, signs, density, collar images, and finite errors must be
audited.

The following are controls, not shortcuts:

- exact primal square/fourth-power resonances have
  \(O_\varepsilon(L^{1+\varepsilon})\) capacity;
- exact dual products \(jl=X\) are divisor-bounded;
- for \(X=R^4\), the anti-diagonal \(j=J+s,l=J-s\) has
  \(X-jl=s^2\), so the near-product window contains
  \(O(\sqrt{J/L})\) such points, below \(J^{1/2}\);
- arbitrary bounded \(b_{\tau,j,k}\) can phase-conjugate one \(S_k\),
  so (75.16) must use the actual coupled symbol;
- absolute near-product counting closes only at the inherited terminal
  scale.

## 6. Required controls

Every report must audit:

1. external normalization and conjugate ownership;
2. the exact ceiling and both \(B\)-collars;
3. actual \(q_X\), upper flat edge, and one-count layer partition;
4. quarter-shift sign, odd \(j\), Gaussian constant, and Jacobian;
5. the complete \(l\)-dependent radial symbol;
6. alias/layer error summation and the support (75.11);
7. the exact Poisson definition (75.13);
8. \(k\)-tail decay and the Parseval diagonal (75.15);
9. the signed off-diagonal in (75.16);
10. character-leg self-return with both quarter lattices;
11. perfect powers, exact products, and adversarial coefficients;
12. separation from smooth packets, M1, full M2, M9, and the exponent.

## 7. Promotion and stopping rule

Promote the near-product/energy reduction only if the complete
moving-amplitude identity, constants, collars, (75.15), and self-return
survive a strict statement-only rederivation and an independent hostile
audit.  Promote the cone target only if (75.16), or a weaker
character-preserving outside-Cauchy estimate, is actually proved.

A corrected candidate formula, a smaller actual-symbol off-diagonal, a
strict \(L\)-subrange, or a rigorous self-return/no-go is useful.  Do not
promote M9-M2, M9, or the global exponent from a reduction alone.

