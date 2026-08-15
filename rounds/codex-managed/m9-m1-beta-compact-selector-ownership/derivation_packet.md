# Round 44 frozen derivation packet

This packet contains accepted inputs but no proposed ownership answer. A
statement-only task may use only this file and its task brief.

## 1. Contour and physical families

Fix

\[
b=\frac1{\log(2X)},\qquad
r=\frac54-\frac{a+b}{2},\qquad
p=\frac54+\frac{a+b}{2},
\]

on

\[
0\le a<a_0,qquad a+b<\frac12,qquad \frac a2+b<\frac14.
\]

Let

\[
D_j=2^{-j}\lfloor\sqrt X\rfloor,qquad
H_j=\lfloor D_jX^{-1/4}\rfloor,qquad H_j\ge1.
\]

There are exactly three spatial-profile selector classes:

\[
\begin{array}{c|c|c}
\text{class}&\text{selector}&\text{profile}\ \\ \hline
\text{hard singular top}&\mathbf1_{j=0}&u^{-1}\text{ top share}\ \\
\text{regular top}&\mathbf1_{j=0}&W_{0,r}\ \\
\text{interior}&\mathbf1_{j\ge1}&W_j.
\end{array}
\]

The singular class is evaluated by the signed Plemelj functional; the
other two retain ordinary \(\mu\)-integration. Every row keeps its actual
\(D_j,H_j+1\), floor, star, \(\chi_4(q)\), and physical profile.

## 2. Terminal density and masks

At finite height the terminal density is

\[
\begin{aligned}
Q_T={}&\mathbf1_{hq=m}\chi_4(q)\sum_j
\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
\left(\frac hq\right)^{(u+v)/2}\\
&\qquad\times G_v(1-s)K_{u+v}(1-s)m^{-s}.
\end{aligned}
\]

Use

\[
\beta=t-\frac{\mu+\nu}{2},\qquad
\alpha=\mu+\nu+\beta,
\]

the compact beta mask \(\psi(\beta)\), and a central cutoff
\(\chi_0(\alpha)\). Put

\[
c_{\rm db}=\psi(\beta)\chi_0(\alpha).
\]

Then

\[
\partial_\mu\partial_\nu c_{\rm db}
=\frac14\{\psi''\chi_0-2\psi'\chi_0'+\psi\chi_0''\}.
\]

When the central and large-alpha shares are recombined before the compact
family is frozen, all \(\chi_0'\) and \(\chi_0''\) terms cancel. The pure
beta first and mixed connectors need not cancel; in particular

\[
\frac14A_uA_v[\psi''(\beta)Q_T]
\]

must either be a named terminal type or be assigned to an already proved
module with an exact identity.

## 3. Accepted finite product identity

Let \(L_j\) be the final left vertical, let
\(B_j=H_{j,+}-H_{j,-}\) be the oriented horizontal difference, put
\(F_j=L_j+B_j\), let \(P_j\) be the coordinate-axis residue, and let
\(A_j\) be positive area integration. The exact finite identity is

\[
\begin{aligned}
R_uR_v[\psi Q]={}&F_uF_v[\psi Q]
+F_uP_v[\psi Q]+P_uF_v[\psi Q]+P_uP_v[\psi Q]\\
&+\frac12F_uA_v[\psi'Q]+\frac12P_uA_v[\psi'Q]\\
&+\frac12A_uF_v[\psi'Q]+\frac12A_uP_v[\psi'Q]\\
&+\frac14A_uA_v[\psi''Q].
\end{aligned}
\]

Expanding both \(F\)'s gives these sixteen rows:

1. \(L_uL_v[\psi Q]\);
2. \(L_uB_v[\psi Q]\);
3. \(B_uL_v[\psi Q]\);
4. \(B_uB_v[\psi Q]\);
5. \(L_uP_v[\psi Q]\);
6. \(B_uP_v[\psi Q]\);
7. \(P_uL_v[\psi Q]\);
8. \(P_uB_v[\psi Q]\);
9. \(P_uP_v[\psi Q]\), once;
10. \(\frac12L_uA_v[\psi'Q]\);
11. \(\frac12B_uA_v[\psi'Q]\);
12. \(\frac12P_uA_v[\psi'Q]\);
13. \(\frac12A_uL_v[\psi'Q]\);
14. \(\frac12A_uB_v[\psi'Q]\);
15. \(\frac12A_uP_v[\psi'Q]\);
16. \(\frac14A_uA_v[\psi''Q]\).

Both orders of transfer agree. Coordinate-axis collisions with an
artificial or arithmetic pole use one combined Laurent/derivative
coefficient. The corner occurs once. Identical transfer of
\(G=E_1+R_1\) preserves the artificial-pole cancellation on every row.

## 4. Accepted routing scope

The following statements may be used, only in their stated scopes.

1. **Radial sides.** Compact beta support annihilates every transferred
   renormalized radial \(w\)-side after the prescribed finite support
   separation. This does not say that the \(u,v\) horizontal rows
   \(B_u,B_v\) vanish.
2. **Physical endpoint/arithmetic module.** Only the aggregate sum over
   the three hierarchical masks returns the finite endpoint plus
   recombined \(R_1\)-arithmetic module to its accepted positive-line
   physical limit. Individual beta-masked faces, axes, connectors, and
   corner have no separate physical-module theorem.
3. **Endpoint-free limit.** After aggregate module subtraction, the full
   finite endpoint-free vector, with all retained rows and combined
   collisions, has a unique joint height/profile limit on the positive
   \(b\)-line.
4. **Large alpha.** The complete beta-owned large-alpha saddle, entry,
   and exit package is target-sized. This theorem applies only after the
   actual row ownership and profile selectors are retained; it does not
   delete beta connectors from the central share by assertion.
5. **Local compact estimate.** Any actual compact terminal row that has a
   fixed compact multiplier, the correct singular/smooth profile, and the
   stated selectors belongs analytically to the corrected finite-family
   class. This is a conditional class estimate, not an ownership identity.

## 5. Required certificate

Construct or refute a table in which every row above records:

- exact operator and orientation;
- coefficient and remaining contour measure;
- central/large-alpha recombination effect;
- terminal survivor or exact accepted routed module;
- named singular, regular-top, or interior type and j-selector;
- physical profile, floors, stars, and collision convention;
- whether it reaches the corrected compact amplitude;
- unique external normalization owner.

If the accepted inputs do not determine one of these columns, isolate the
first exact underdetermined row. Do not fill a gap by saying only that the
family is finite or target-safe.

The external physical factor is

\[
-\frac4\pi X^{1/4}\Re\{e(1/8)(\cdot)\}
\]

and is restored exactly once after the complete vector identity.

