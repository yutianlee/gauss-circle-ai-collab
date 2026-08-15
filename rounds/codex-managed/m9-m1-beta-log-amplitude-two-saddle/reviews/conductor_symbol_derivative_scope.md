# Conductor review: why the regular finite-part symbol is the exact survivor

Campaign: `m9-m1-beta-log-amplitude-two-saddle`  
Role: conductor scope and derivative audit

## 1. Fixed-profile model

For the isolated two-denominator height model, let

\[
 A=\rho_0-i\alpha,qquad L=\alpha-\beta,qquad
 f(\nu)=\widehat\phi(b+i\nu),
\]

and retain a finite section \([\ell(L),r(L)]\). The exact post-top kernel is

\[
 {\cal C}(\alpha,L)=\frac1A
 \left\{\pi f(L)\mathbf1_{\ell<0<r}
 -iP_{\ell,r}f(L)-\frac12J_{\ell,r}(A,L)\right\},    \tag{30.S1}
\]

where

\[
 P_{\ell,r}f(L)=\operatorname {PV}\int_{\ell}^{r}
 \frac{f(L-y)}y\,dy,qquad
 J_{\ell,r}(A,L)=\int_{\ell}^{r}
 \frac{f(L-y)}{A+iy/2}\,dy.                          \tag{30.S2}
\]

On a cell where \(\ell,r\) are affine, subtracting \(f(L)\) from the PV
term isolates the explicit face logs. The remaining quotient

\[
 Q(L,y)=\frac{f(L-y)-f(L)}y                         \tag{30.S3}
\]

extends continuously to \(-f'(L)\). Its first \(L\)-derivative is

\[
 \partial_LQ(L,y)=\frac{f'(L-y)-f'(L)}y,             \tag{30.S4}
\]

bounded by \(\|f''\|_\infty\). Thus for the fixed height profile alone,
the regular PV remainder has a piecewise BV norm bounded by weighted
\(W^{2,1}\) norms of \(f\), plus affine endpoint traces. The accepted
\((1+|\nu|)^{-3-k}\) decay makes these bounds uniform in the height cutoff
up to the declared polynomial \(b^{-1}\) loss.

Similarly, away from the artificial pole \(|A+iy/2|\ge c(|A|+|y|)\),
differentiating \(J\) costs at most one extra such denominator and a
derivative of \(f\). Its fixed-profile regular part therefore has the
required piecewise BV control. At saddle-face collision, the explicit log
coefficient is the already certified \(O_b(\lambda^{-4})\).

## 2. Why this is not yet the project symbol lemma

The actual numerator is not just \(f_b(\nu)\). Before stationary reduction
it includes:

- the exact bounded beta gamma factor;
- the large-alpha gamma quotient and its Stirling remainder;
- scale and height powers with \(H_j+1\) floors;
- radial \(x\)-integration and phase;
- the beta connector and finite alpha endpoints;
- the artificial-pole-safe sum
  \(\omega G+(1-\omega)R_1-\omega E_1\);
- top and interior spatial profiles, endpoint stars, and outside pieces.

An \(L\)-derivative at fixed beta changes alpha, hence can hit every
alpha-dependent factor. In the normalized saddle variable
\(y=\alpha/\lambda\), the correct norm is scaled: one derivative in \(y\)
equals \(\lambda\partial_\alpha\). A pointwise value
\(D_j/(q\lambda)\) does not imply that its scaled derivative has the same
size. The phase-cancelling amplitude adversary in the hostile report shows
this logical gap is sharp.

At \(\rho=0\), termwise differentiation of \(R_1\) or \(E_1\) is invalid.
The \(\omega'\) terms cancel only when all three summands use identical
domains, masks, and endpoints. The correct symbol lemma must therefore be
stated for the complete recombined expression rather than proved for the
fixed-profile model and extended by assertion.

## 3. Smallest next statement

For each signed saddle component, after exact Morse scaling, define
\({\cal B}_{j,h,q,x}^{\pm}(y;U,V,S,b)\) to be the full recombined regular
finite-part amplitude after removing the explicit face logarithms and
delta jumps. The precise missing estimate is

\[
 \|{\cal B}\|_{L^\infty_y}
 +\|\partial_y{\cal B}\|_{L^1_y}
 \ll_{b,W,\phi} X^\varepsilon\frac{D_j}{q\lambda}
 \times\{\text{the already recorded }h,D_j,x\text{ monomial}\}. \tag{30.S5}
\]

It must be uniform in saddle entry/exit, all affine polytope cells, and the
\(\rho\)-patch, and its finite-height tail must be summable. If (30.S5)
holds, the blind/hostile logarithmic Fresnel theorem immediately changes
the right side only by \(\log(2+\lambda)\), preserving absolute q
summability. If it fails, the first offending differentiated factor is the
next exact obstruction.

## 4. State recommendation

Promote no actual-profile symbol estimate from this review. Record the
fixed-height-profile regular quotient as benign, and freeze (30.S5) as the
next smallest project-specific obligation after Round 30 closes. The full
beta transition and theorem remain open.
