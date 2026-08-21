# Round 92 conductor review: capacities and downstream bridges

## M1

The accepted normalized row, ordered-pair, and four-row gains are

\[
 Q^{-5/24},\qquad Q^{-5/12},\qquad Q^{-5/6}.
\]

Writing

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12},\qquad
 \mathsf T_{82}=J^{7/5},
\]

the exact Gram lift has

\[
 \mathsf C_{\rm Gram}={U\over B}\mathsf C_{82}^2,
 \qquad
 \mathsf T_{\rm Gram}={U\over B}\mathsf T_{82}^2.
\]

At (B=J^{3/20}), the linear capacity gap is (J^{1/12}), while the
Gram gap is its square (J^{1/6}).  The proved finite Toeplitz inequality

\[
 \left|\sum_{b\asymp B}H_{b,U}(0)\right|^2
 \ll_\varepsilon X^\varepsilon{B\over U}\mathcal E_U
\]

square-roots the Gram estimate back to the same linear deficit.  This is an
equal-capacity barrier, not a proof and not a second independent loss.

The canonical open target is

\[
 |\mathcal E_{\rm hard}(U)|
 \ll_\varepsilon X^\varepsilon {U\over B}J^{14/5}.
\]

Even if proved, it closes only the first-band smooth nonaxial principal
packet after the accepted owners.  It does not close (C>J^{3/4}), axes,
raw transitions, cone edges, other radial sectors, alpha/top interfaces, or
target-scale endpoint assembly.

## M2

The exact bridge

\[
 |\mathcal T_{\mathrm{end},L}|^2\ll L\mathcal E_L^\top
\]

shows that (mathcal E_L^\top\ll L^2X^\varepsilon) suffices for the
original endpoint target (L^{3/2}X^\varepsilon).  On a hard primitive-ray
block,

\[
 \rho={AJD_{\rm ray}^3\over L^3}\gg1,
 \qquad
 \mathsf C_{\rm block}=L^2X^\varepsilon\sqrt\rho.
\]

Therefore the exact missing signed gain is (ho^{-1/2}).  The canonical
target is

\[
 \sum_{A,D_{\rm ray},K_{\rm rec},G,R}
 |\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
 \ll_\varepsilon L^2X^\varepsilon,
\]

with the density and discrepancy modes in one coefficient.  Even if proved,
it closes only the residual hard top cone.  Other M2 packets and the
all-denominator endpoint assembly remain separate.

## Outcome

All exponent arithmetic and bridge normalizations pass.  No estimate is
promoted.  The unconditional global exponent remains (1/3), and the
one-quarter target still needs genuinely new signed cancellation.

