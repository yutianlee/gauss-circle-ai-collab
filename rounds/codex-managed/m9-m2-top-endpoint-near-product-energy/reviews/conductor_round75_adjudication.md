# Round 75 conductor adjudication

Campaign: `m9-m2-top-endpoint-near-product-energy`  
Round: 75  
Starting graph SHA-256: `b5aa6150a62e1ecc21045c21bcb4af9ede4ab164545b43a93756e53fcc402bd2`

## Decision

Reject the frozen leading-wavelet identity (75.7)--(75.10) as an
all-orders formula.  Promote only the exact finite transposed-row energy
reduction.  Retain the energy estimate, the full top cone, (M9!-!M2),
(M9), and the global exponent open.

All three reports independently find the same first correction.  After
(m=xt^2), the quadratic phase is exact but the angular amplitude is not
constant.  If (g_{x,l}) denotes that amplitude and (t_0=J/(2l)), then

\[
 \int g_{x,l}(t)e\!\left(-xl(t-t_0)^2\right)dt
 =\frac{e(-1/8)}{\sqrt{2xl}}
 \left\{g_{x,l}(t_0)+
 \frac{g_{x,l}''(t_0)}{8\pi i,xl}+\cdots\right\}.
\]

The second term is generally nonzero.  On the narrowest
(B=\lceil\sqrt L\rceil) collar it is (O(J^{-1}X^\varepsilon)) on
the normalized-symbol scale.  Thus the leading formula has a target-safe
aggregate error (O(L^{3/2}J^{-1/2}X^\varepsilon)), but not the stated
arbitrary-order error.  An exact Fresnel symbol or a finite all-orders
package is plausible; its complete moving-symbol seminorms were not
independently proved and are not promoted.

## Exact promoted kernel

Let (mathscr H_L) be the actual finite odd (h)-support, let
(a(h,m)) be the exact normalized top-endpoint symbol, and put

\[
 \mathcal T_L=
 \sum_{h\in\mathscr H_L}\chi_4(h)
 \sum_{\lceil h/4\rceil\le m\le h}
 a(h,m)e(J\sqrt{hm}),\qquad J=\sqrt X.
\]

For each integer (m), define

\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a(h,m)e(J\sqrt{hm}).
\]

The ceiling is preserved exactly because
(\lceil h/4\rceil\le m\) is equivalent to (h\le4m).  Hence

\[
 \mathcal T_L=\sum_mR_m,qquad
 |\mathcal T_L|^2\ll L\mathcal E_L^\top,qquad
 \mathcal E_L^\top=\sum_m|R_m|^2.
\]

Writing the second odd index as (h+2r) gives

\[
\begin{aligned}
 \mathcal E_L^\top
 ={}&\sum_h\sum_{\lceil h/4\rceil\le m\le h}|a(h,m)|^2\\
 &+2\Re\sum_{r\ge1}(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a(h,m)\overline{a(h+2r,m)}\\
 &\hspace{27mm}\times
 e\!\left(-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}\right).
\end{aligned}
\]

The sign is exact:

\[
 \chi_4(h)\chi_4(h+2r)=(-1)^r.
\]

The diagonal is (O(L^2)).  Therefore

\[
 \mathcal E_L^\top\ll_\varepsilon L^2X^\varepsilon
\]

is sufficient for
(\mathcal T_L\ll_\varepsilon L^{3/2}X^\varepsilon).  This is a
finite identity plus one Cauchy inequality.  It keeps both affine edges,
the exact (q_X)-profile, and (chi_4); it does not depend on the
rejected moving-wavelet formula.

## Reciprocal-energy adjudication

For a repaired full moving symbol, Poisson in the uncharactered (l)
leg has the exact normalization

\[
 \mathcal D_L=L^{-1}\sum_kS_k,qquad
 S_k=\sum_{\tau,j\ {m odd}}
 \chi_4(j)b_{\tau,j,k}e(-kX/j).
\]

The exact square identity is periodized Parseval, not continuous
Parseval without aliases:

\[
 \sum_k|S_k|^2
 =L^2\sum_{n\in\mathbb Z}
 \int_{\mathbb R}G(\lambda)
 \overline{G(\lambda+n)},d\lambda.
\]

Natural width-(L^{-1}) envelope bounds give the diagonal (LJ), but
do not bound the alternating off-diagonal.  Coefficient (L^2)-mass
alone is insufficient, as the phase-conjugating artificial-array control
shows.

The active Fourier modes are (k=-m<0), (m\asymp L).  The second
high-character B-process has stationary data

\[
 j_*=2\sqrt{mX/r},\qquad m\le r\le4m,qquad
 \phi(j_*)=\sqrt{Xmr},
\]

and Gaussian-character unit (e(-1/8)\chi_4(r)).  At principal-symbol
level,

\[
 S_{-m}^{(0)}
 =e(-1/8)\sqrt{J/L},R_m^{\rm int}.
\]

Thus the proposed reciprocal energy is the adjoint image of the same
transposed-row energy.  Iterating the transform supplies no independent
saving.  The exact full-symbol return is useful as a no-go, but the
frozen leading symbol is not an exact inverse.

## Source and control adjudication

The applicable Kowalski--Robert--Wu bound remains dominated by the
accepted two-shift envelope.  The audited root-spacing, separated-point
large sieve, reciprocal exponential-sum, centre-averaged divisor,
Kloosterman-fraction, and Kuznetsov results do not prove the signed
actual-symbol energy.  No external-dependency promotion or source card
is warranted.

Exact squares, fourth powers, exact products, and the fourth-power
anti-diagonal are all target-safe capacity controls.  They neither
falsify nor prove the signed energy.  No numerical computation was used.

## Downstream scope

The exact open survivor is the alternating even-offset union above.
There is no new polynomial (L)-range.  The full top cone,
(M9!-!M2), (M9!-!M1), (M9), endpoint uniformity, and the
Gauss-circle exponent remain open.

