# Conductor derivation: exact beta Cauchy decomposition at a moving height face

Campaign: `m9-m1-beta-log-amplitude-two-saddle`  
Role: conductor's actual-kernel algebra  
Allocation: 100% analytical/algebraic; no numerical experiment or external theorem

## 1. Exact two-denominator identity

Use the accepted Round-27 notation

\[
 L=\alpha-\beta,qquad K=-\alpha-\beta,qquad
 A_\alpha=\rho_0-i\alpha,qquad f_b(\nu)=\widehat\phi(b+i\nu).
\]

Then

\[
 \rho_0-i(\nu-K)/2
 =A_\alpha+\frac i2(L-\nu).                           \tag{30.A1}
\]

After taking the physical top limit at fixed finite \(V\), define

\[
 \begin{aligned}
 {\cal C}_V(\alpha,\beta)={}&
 \frac{\pi f_b(L)}{A_\alpha}\mathbf1_{|L|<V}\\
 &-i\operatorname {PV}\!\int_{-V}^{V}
 \frac{f_b(\nu)}{{A_\alpha+i(L-\nu)/2}(L-\nu)}d\nu .
                                                               \tag{30.A2}
 \end{aligned}
\]

Endpoint values use symmetric distributional inversion. The partial
fraction identity

\[
 \frac1{y(A+iy/2)}
 =\frac1A\frac1y-\frac{i}{2A}\frac1{A+iy/2}           \tag{30.A3}
\]

gives the exact decomposition

\[
 \boxed{
 {\cal C}_V(\alpha,\beta)=\frac1{A_\alpha}
 \left\{\pi f_b(L)\mathbf1_{|L|<V}
 -iP_Vf_b(L)-\frac12J_V(\alpha,L)\right\},}          \tag{30.A4}
\]

where

\[
 P_Vf(L)=\operatorname {PV}\!\int_{-V}^{V}
 \frac{f(\nu)}{L-\nu}d\nu,qquad
 J_V(\alpha,L)=\int_{-V}^{V}
 \frac{f_b(\nu)}{A_\alpha+i(L-\nu)/2}d\nu.           \tag{30.A5}
\]

This formula keeps the Plemelj delta and PV signs together. It also shows
why the pointwise edge logarithm is smaller than the bulk at a large
saddle.

## 2. Bulk size near either signed saddle

Assume \(|\beta|\le B_0\), \(|\alpha|\asymp\lambda\gg1\), and the accepted
height estimates

\[
 |f_b^{(k)}(\nu)|\ll_b(1+|\nu|)^{-3-k},qquad k=0,1,2.
                                                               \tag{30.A6}
\]

The full Hilbert transform of \(f_b\) and the nonsingular transform
\(J_V\) have the familiar far-field size \(O_b(\lambda^{-1})\), apart
from the finite endpoint logarithm discussed below. Since
\(|A_\alpha|\asymp\lambda\), the smooth bulk of (30.A4) is

\[
 {\cal C}_{V,\mathrm{bulk}}(\alpha,\beta)=O_b(\lambda^{-2}).
                                                               \tag{30.A7}
\]

This rederives the Round-27 signed-convolution size on both signs of
\(\alpha\). Multiplication by the accepted post-endpoint stationary
numerator \((D_j/q)\lambda\) gives

\[
 \frac{D_j}{q}\lambda\,{\cal C}_{V,\mathrm{bulk}}
 \ll_b\frac{D_j}{q\lambda}
 =\frac{D_j}{q^2\theta_j(x)},
 \qquad \lambda=q\theta_j(x).                       \tag{30.A8}
\]

The estimate is meant in the stationary normalization already fixed in
Round 27; no second Hessian factor is inserted.

## 3. Exact moving-face coefficient

At the upper face \(L=V\), the singular part of the finite Hilbert
transform is

\[
 P_Vf_b(L)=f_b(L)\log|L-V|+\text{a regular finite-part term},  \tag{30.A9}
\]

up to the fixed orientation sign. The lower face is analogous. At a
saddle-face collision, \(L=\pm V\) and
\(|L|\asymp|\alpha|\asymp\lambda\). Hence (30.A6) gives

\[
 |f_b(L)|\ll_b\lambda^{-3},qquad
 |A_\alpha|^{-1}\ll\lambda^{-1}.                     \tag{30.A10}
\]

Therefore the logarithmic part of the two-denominator convolution is

\[
 {\cal C}_{V,\log}(\alpha,\beta)
 =O_b(\lambda^{-4}\log|L\mp V|).                     \tag{30.A11}
\]

After the Round-27 stationary numerator, its coefficient is

\[
 \frac{D_j}{q}\lambda\,{\cal C}_{V,\log}
 =O_b\!\left(\frac{D_j}{q\lambda^3}
              \log|L\mp V|\right)
 =O_b\!\left(\frac{D_j}{q^4\theta_j(x)^3}
              \log|L\mp V|\right).                 \tag{30.A12}
\]

Thus the explicit face-log coefficient is two powers of \(q\) smaller
than the bulk \(q^{-2}\) term when the face meets a large saddle. A
uniform moving-logarithm Fresnel lemma adds at most
\(\log(2\lambda)\) and changes no algebraic power. This statement concerns
only the explicit diagonal logarithm. The regular finite-part term still
requires a separate normalized BV audit; its derivative may contain
endpoint traces and cannot be declared small from (30.A10) alone.

The same calculation works at the negative saddle. There
\(L\asymp-\lambda\), \(f_b(L)=O_b(\lambda^{-3})\), and
\(|A_\alpha|\asymp\lambda\). No cancellation between saddle signs is
assumed.

## 4. Geometry away from collision

There are three regimes at a saddle \(|\alpha|\asymp\lambda\):

1. If \(V\ge2|L|\), the saddle is well inside the height interval. The
   omitted height tail has polynomial decay and (30.A7) is the full-line
   bulk estimate.
2. If \(V\le|L|/2\), the top pole is separated from the finite interval;
   both denominators are \(\asymp\lambda\), giving (30.A7) directly by
   absolute integration.
3. If \(V\asymp|L|\), only the moving-face regime is new. Equations
   (30.A9)--(30.A12) isolate its entire singular part.

The top-height constraint \(|L-\nu|\le U\) replaces \([-V,V]\) by its
intersection with \([L-U,L+U]\). It introduces additional affine endpoints
at \(L-\nu=\pm U\), but the top denominator is then \(\pm iU\), not zero.
Those faces create steps or ordinary endpoint terms, not a new logarithmic
top-pole collision.

## 5. What remains unproved

The algebra (30.A4) and face coefficient (30.A11) do not by themselves
prove the complete beta estimate. Required seams are:

- uniform BV or Sobolev bounds for the locally regular finite-part term in
  \(P_Vf_b\) and \(J_V\) after every actual scale, radial, beta-mask, and
  \(\rho\)-recombination factor is restored;
- saddle entry/exit and alpha-polytope endpoint terms;
- the \(b\downarrow0\) height residue ledger and polynomial
  \(b^{-1}\) constants;
- uniform \(U,V,S\) tails and finite outside sides;
- the complete \(h,D_j,x,q\) summation with the external \(X^{1/4}\)
  factor.

In particular, differentiating a simplified coefficient must not be used
to bypass derivatives of the complete \(\omega G+(1-\omega)R_1-\omega E_1\)
expression.

## 6. Controls

- **Signed versus unsigned:** (30.A4) requires the signed delta/PV
  combination. Absolute pre-limit integration still diverges.
- **Both saddles:** only absolute magnitudes are used, so no unsupported
  reflection cancellation enters.
- **Endpoint:** the moving-face log is retained explicitly and is not
  called \(C^2\).
- **Normalization:** the bulk gives the accepted \(D_j/(q\lambda)\);
  the log face gives the stronger \(D_j/(q\lambda^3)\).
- **Coefficient adversary:** the face saving uses the actual transform
  decay (30.A6). An arbitrary bounded height coefficient would not have
  the \(\lambda^{-3}\) factor.

## 7. Recommended state effect

After independent validation, promote only the exact partial-fraction
decomposition (30.A4) and the actual-profile saddle-face coefficient
\(O_b(\lambda^{-4}\log)\). Use them to reduce the Round-30 target to the
regular-part scaled-variation and complete-sum problem. Do not promote the
full beta transition or any downstream theorem.
