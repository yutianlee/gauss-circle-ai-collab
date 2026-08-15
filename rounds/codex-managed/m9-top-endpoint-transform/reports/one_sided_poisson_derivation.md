# One-sided Poisson derivation for the top block

- Campaign: m9-top-endpoint-transform
- Round: 8 (endpoint_transform_attack)
- Task: one_sided_poisson_derivation
- Role: analytic deriver
- Graph SHA-256: 7b5a7c93190fa88305d91bb1f2e64788921fe2f4cbbd02eddb8e60e654d64d58
- Status: candidate evidence only; no shared state was edited.

## 1. Result and verdict

Put

\[
y=\lfloor\sqrt X\rfloor,\qquad q=\frac{X}{y^2},\qquad
\nu_h=\frac{hX}{4y^2}=\frac{qh}{4},\qquad
A_h=y\nu_h=\frac{hX}{4y}.
\]

For the accepted top profile \(W\), and every positive odd
\(h\leq H_y=\lfloor yX^{-1/4}\rfloor\), the full-endpoint sum

\[
S_h=\sum_{d\leq y}W(d/y)e\!\left(\frac{hX}{4d}\right)
\]

has the uniform one-sided transform

\[
\boxed{
\begin{aligned}
S_h={}&\frac{e(A_h)}{1-e(\nu_h)}\\
&+\frac{e(1/8)(hX)^{1/4}}2
\sum_{m=\lceil h/4\rceil}^{h}
\frac{W\!\left(\sqrt{qh/(4m)}\right)}{m^{3/4}}
e(\sqrt{Xhm})+R_h ,
\end{aligned}}
\tag{1.1}
\]

where

\[
R_h\ll_W\log(2+h)                                    \tag{1.2}
\]

uniformly in the stated range. The first term is the complete upper-endpoint
term at one-term \(B\)-process precision: it includes both the Poisson
midpoint half-weight and the principal-value sum of all modewise endpoint
pieces.

The key arithmetic separation is true:

\[
\boxed{\operatorname{dist}(\nu_h,\mathbb Z)\geq\frac18}.\tag{1.3}
\]

Thus the boundary contributes \(O(\log(2H_y))\) after insertion of the
actual Vaaler coefficients, and all transform errors contribute
\(O_W(\log^2(2H_y))\). Both are \(O_{W,\varepsilon}(X^\varepsilon)\).

Stationary points are not separated from \(u=1\) by a fixed ordinary
\(u\)-distance: the closest distance is \(\asymp1/h\). They are, however,
uniformly noncoalescent on the stationary-phase scale. The endpoint
derivative gap is at least \(y/8\), and the closest stationary point is
\(\gg\sqrt{y/h}\gg y^{1/4}\) stationary widths from \(u=1\).

After the actual \(\chi_4(h)\Phi(h/(H+1))/h\) factor is inserted, (1.1)
reduces a dyadic positive-frequency top block to the exact signed cone

\[
h\asymp L,\qquad h\ {\rm odd},\qquad
\lceil h/4\rceil\leq m\leq h,                        \tag{1.4}
\]

with product phase \(e(\sqrt{Xhm})\), a normalized smooth interior symbol,
and one hard affine lower edge. The successor estimate is

\[
\mathcal T^{\rm end}_L\ll_\varepsilon L^{3/2}X^\varepsilon.\tag{1.5}
\]

This proves the endpoint transform and makes every boundary/error term
target-sized, but it does not prove (1.5). It reduces rather than closes the
full top \(M2\) block. No numerical experiment or external theorem was used.

## 2. Exact hypotheses

Write \(e(t)=e^{2\pi it}\). Assume:

1. \(X\geq1\), \(y=\lfloor\sqrt X\rfloor\), so
   \(y^2\leq X<(y+1)^2\).
2. \(W\in C^\infty(\mathbb R)\) is the accepted Round-7 profile. In
   particular

   \[
   W(u)=0\ (u\leq1/2),\qquad W(1)=1,\qquad
   W(u)=1\ (2/3\leq u\leq1).                         \tag{2.1}
   \]

3. \(h\) is positive and odd, with

   \[
   1\leq h\leq H_y=\lfloor yX^{-1/4}\rfloor.         \tag{2.2}
   \]

For a dyadic block a fixed smooth cutoff \(\eta_L(h)\) may be inserted.
The actual positive Vaaler coefficient is

\[
-\frac1\pi\frac{\chi_4(h)\Phi(h/(H+1))}{h},
\qquad h>0\ {\rm odd},                               \tag{2.3}
\]

with \(0\leq\Phi\leq1\). Negative \(h\) is recovered by conjugation.

## 3. Arithmetic endpoint separation and the exact cone

Let \(\Delta=X-y^2\). Then \(0\leq\Delta<2y+1\), and (2.2) gives

\[
h\leq yX^{-1/4}\leq\sqrt y.                          \tag{3.1}
\]

Because \(h\) is odd,
\(\operatorname{dist}(h/4,\mathbb Z)=1/4\). Moreover

\[
\left|\nu_h-\frac h4\right|
=\frac{h\Delta}{4y^2}
<\frac{\sqrt y(2y+1)}{4y^2}
\leq\frac{3}{4\sqrt y}.                              \tag{3.2}
\]

For \(y\geq36\), (3.2) is at most \(1/8\), proving (1.3), uniformly at
\(h=1\) and \(h\asymp H_y\).

Two further consequences freeze the moving cone. For large \(y\),

\[
0\leq qh-h=\frac{h\Delta}{y^2}<\frac3{\sqrt y}<1.    \tag{3.3}
\]

The positive perturbation in (3.2) also does not reach the next integer.
Thus

\[
\lceil\nu_h\rceil=\lceil h/4\rceil
=\begin{cases}
(h+3)/4,&h\equiv1\pmod4,\\
(h+1)/4,&h\equiv3\pmod4,
\end{cases}                                         \tag{3.4}
\]

and every integer \(m<qh\) has \(m\leq h\). These give the exact lattice
limits in (1.1); in particular the lower edge is independent of \(X\).

## 4. Poisson half-weight and the full endpoint term

Set

\[
F_h(t)=W(t/y)e\!\left(\frac{hX}{4t}\right)
\]

on \(0<t\leq y\), extended by zero near \(0\). Finite Poisson summation on
the integer interval, with symmetric principal-value convergence, gives

\[
\sum_{1\leq d<y}F_h(d)+\frac12F_h(y)
=\operatorname{PV}\sum_{k\in\mathbb Z}
\int_0^yF_h(t)e(-kt)\,dt.                            \tag{4.1}
\]

The project sum gives \(d=y\) full weight. Since \(W(1)=1\),

\[
S_h=\frac12e(A_h)+\operatorname{PV}\sum_{k\in\mathbb Z}I_{h,k},
\quad
I_{h,k}=\int_0^yW(t/y)e\!\left(\frac{hX}{4t}-kt\right)dt.
\tag{4.2}
\]

At \(t=y\), the phase derivative is \(-\nu_h-k\), so the modewise
integration-by-parts endpoint piece is

\[
-\frac{e(A_h)}{2\pi i(\nu_h+k)}.                     \tag{4.3}
\]

Adding the full-sample correction in (4.2) and using
\(\operatorname{PV}\sum_{k\in\mathbb Z}(\nu+k)^{-1}
=\pi\cot(\pi\nu)\) gives

\[
\begin{aligned}
\mathfrak B_h
&=e(A_h)\left\{\frac12-\frac{1}{2\pi i}
\operatorname{PV}\sum_{k\in\mathbb Z}\frac1{\nu_h+k}\right\}\\
&=e(A_h)\left(\frac12+\frac i2\cot(\pi\nu_h)\right)
=\boxed{\frac{e(A_h)}{1-e(\nu_h)}}.                  \tag{4.4}
\end{aligned}
\]

The cotangent identity follows by logarithmically differentiating the
symmetric product for \(\sin(\pi\nu)\). From (1.3),

\[
|\mathfrak B_h|\leq\{2\sin(\pi/8)\}^{-1}.            \tag{4.5}
\]

If the midpoint sum were mistakenly identified with the full sum, its
boundary would be only
\(\frac i2e(A_h)\cot(\pi\nu_h)\). The missing
\(\frac12e(A_h)\) is exactly the endpoint-convention error.

## 5. Stationary modes and proof of the transform

For \(k\geq0\), the phase in \(I_{h,k}\) has no critical point. Write
\(k=-m\), \(m\geq1\), for the other sign. Then

\[
\phi_{h,m}(t)=\frac{hX}{4t}+mt
\]

has the unique stationary point

\[
t_{h,m}=\sqrt{\frac{hX}{4m}},\qquad
u_{h,m}=\frac{t_{h,m}}y=\sqrt{\frac{\nu_h}{m}}.      \tag{5.1}
\]

It lies strictly below \(y\) exactly when \(m>\nu_h\). At this point

\[
\phi_{h,m}(t_{h,m})=\sqrt{Xhm},\qquad
\phi''_{h,m}(t_{h,m})
=\frac{2m^{3/2}}{(hX/4)^{1/2}}>0.                   \tag{5.2}
\]

The one-term stationary contribution in the \(e(t)\) normalization is

\[
\frac{e(1/8)(hX)^{1/4}}{2m^{3/4}}
W(u_{h,m})e(\sqrt{Xhm}).                             \tag{5.3}
\]

The support condition \(W(u_{h,m})\neq0\) requires

\[
\nu_h<m<4\nu_h.                                     \tag{5.4}
\]

By (3.3)--(3.4), every nonzero term in (5.4) is included exactly by

\[
\lceil h/4\rceil\leq m\leq h.                       \tag{5.5}
\]

At an equality where \(u=1/2\), the flat factor \(W(1/2)=0\) removes the
term.

Here is a direct uniform error proof. Scale \(t=yu\); the phase becomes
\(y(\nu_h/u-ku)\). Split Poisson modes dyadically by
\(|k+\nu_h|\), and for \(k=-m\), \(m>\nu_h\), split once more around
\(u_{h,m}\). On each nonstationary piece subtract (4.3) and integrate by
parts twice. The first derivative is bounded below by the associated
dyadic \(|k+\nu_h|\), and all reciprocal-phase derivatives are
\(O_j(\nu_h)\) on \(1/2\leq u\leq1\). The resulting mode sums are

\[
\ll_W1+\sum_{1\leq r\leq1+4\nu_h}\frac1r
\ll_W\log(2+\nu_h).                                 \tag{5.6}
\]

On a stationary piece, the Morse coordinate defined by

\[
\phi_{h,m}(t)-\phi_{h,m}(t_{h,m})
=\tfrac12\phi''_{h,m}(t_{h,m})v^2
\]

gives (5.3). One integration by parts in each Gaussian tail gives the same
endpoint term (4.3); the remaining stationary errors, summed over the
\(O(\nu_h)\) possible \(m\), are

\[
\ll_W1+\nu_h/y.                                     \tag{5.7}
\]

The lower support edge is harmless because \(W\) is flat where it leaves
zero. At the upper edge, \(|m-\nu_h|\geq1/8\), so the endpoint tail in the
Morse coordinate never enters a Fresnel transition. Equations
(5.6)--(5.7), \(\nu_h\ll h\), and \(h/y\leq y^{-1/2}\) prove (1.2).
Substitution of (5.3) and (4.4) into (4.2) proves (1.1).

This also treats both Poisson-frequency signs: \(k\geq0\) is
nonstationary, while stationary points occur only for \(k=-m<0\). For
negative original frequency, \(S_{-h}=\overline{S_h}\); the stationary
Poisson sign reverses and every term conjugates.

## 6. Separation from \(u=1\)

Let \(m_h=\lceil\nu_h\rceil=\lceil h/4\rceil\). From (1.3),
\(m_h-\nu_h\geq1/8\), hence

\[
1-u_{h,m_h}
=\frac{m_h-\nu_h}
{\sqrt{m_h}(\sqrt{m_h}+\sqrt{\nu_h})}
\gg\frac1h.                                         \tag{6.1}
\]

For \(h\equiv3\pmod4\), \(X=y^2\), and \(h\to\infty\), this is
\(\asymp1/h\); a fixed positive \(u\)-separation is therefore false.

The stationary width in \(u\) is
\(\sigma_{h,m}\asymp(yh)^{-1/2}\). Consequently

\[
\frac{1-u_{h,m_h}}{\sigma_{h,m_h}}
\gg\sqrt{\frac yh}\geq y^{1/4}.                     \tag{6.2}
\]

Thus ordinary separation tends to zero, but stationary-scale separation
tends to infinity uniformly. There is no endpoint stationary transition.

## 7. Actual Vaaler insertion and the exact signed cone

Define the positive-frequency top contribution

\[
\mathcal M^+_{\rm end}(H)
=-\frac1\pi\sum_{\substack{1\leq h\leq H\\h\ {\rm odd}}}
\frac{\chi_4(h)\Phi(h/(H+1))}{h}S_h,\qquad H\leq H_y.
\tag{7.1}
\]

Its boundary is exactly

\[
\mathcal E^+_{\rm bdry}
=-\frac1\pi\sum_{\substack{1\leq h\leq H\\h\ {\rm odd}}}
\frac{\chi_4(h)\Phi(h/(H+1))}{h}
\frac{e(hX/(4y))}{1-e(hX/(4y^2))},                  \tag{7.2}
\]

and

\[
\mathcal E^+_{\rm bdry}\ll\log(2H).                 \tag{7.3}
\]

All remainders sum to

\[
\sum_{h\leq H}\frac{\Phi(h/(H+1))}{h}|R_h|
\ll_W\sum_{h\leq H}\frac{\log(2+h)}h
\ll_W\log^2(2H).                                    \tag{7.4}
\]

The stationary part is

\[
\begin{aligned}
\mathcal M^+_{\rm stat}
={}&-\frac{e(1/8)}{2\pi}X^{1/4}
\sum_{\substack{h\leq H\\h\ {\rm odd}}}
\chi_4(h)\Phi(h/(H+1))h^{-3/4}\\
&\quad\times\sum_{m=\lceil h/4\rceil}^{h}
m^{-3/4}W\!\left(\sqrt{qh/(4m)}\right)e(\sqrt{Xhm}).
\end{aligned}                                       \tag{7.5}
\]

The full two-sided real top block is
\(2\operatorname{Re}\mathcal M^+_{\rm end}\), since beta is real-even and
\(S_{-h}=\overline{S_h}\).

For a smooth dyadic cutoff \(\eta_L\), put

\[
\begin{aligned}
a^{\rm end}_{L,H,q}(h,m)
={}&\eta_L(h)\Phi(h/(H+1))
\left(\frac{L^2}{hm}\right)^{3/4}
W\!\left(\sqrt{qh/(4m)}\right),\\
\mathcal T^{\rm end}_L
={}&\sum_{\substack{h\asymp L\\h\ {\rm odd}}}
\sum_{\lceil h/4\rceil\leq m\leq h}
\chi_4(h)a^{\rm end}_{L,H,q}(h,m)e(\sqrt{Xhm}).
\end{aligned}                                       \tag{7.6}
\]

Then

\[
\boxed{
\mathcal M^+_{{\rm end},L}
=-\frac{e(1/8)}{2\pi}X^{1/4}L^{-3/2}
\mathcal T^{\rm end}_L
+\mathcal E^+_{{\rm bdry},L}+O_W(\log(2L)).}         \tag{7.7}
\]

On the cone interior, \(h\asymp m\asymp L\), and

\[
(h\partial_h)^i(m\partial_m)^j
a^{\rm end}_{L,H,q}(h,m)\ll_{i,j,W}1                \tag{7.8}
\]

to every fixed order supplied by the dyadic cutoff and the elementary
smooth extension of \(\Phi\). The upper support transition is smooth and
flat because \(W\) is flat at \(1/2\). The lower edge is hard because
\(W(1)=1\); after splitting \(h\equiv1,3\pmod4\), it is the affine lattice
boundary \(m=(h+3)/4\) or \(m=(h+1)/4\).

Equation (7.7) shows that the remaining target is (1.5), the balanced
\(M^{3/4}\) target with \(M\asymp L^2\). The transform does not estimate it.

## 8. Required controls

### \(X=y^2\): pass

Here \(q=1\), \(\nu_h=h/4\), and the distance is exactly \(1/4\). The cone
is unchanged. The \(m=h\) symbol is \(W(1/2)=0\). For \(h=1\), the only
nominal stationary term is \(m=1\), and it vanishes; the endpoint and
\(O(1)\) remainder remain.

### \(X=(y+1)^2-1=y^2+2y\): pass

Here \(q=1+2/y\). For \(h\leq H_y\leq\sqrt y\),

\[
0<\nu_h-h/4=h/(2y)\leq1/(2\sqrt y),\qquad
0<qh-h=2h/y<1.
\]

Neither the lower ceiling nor upper integer limit changes.

### \(h=1\): pass

One has \(\nu_1=1/4+O(1/y)\), so the boundary denominator is uniformly
nonzero. The sole cone frequency is \(m=1\), with stationary point
\(u=\sqrt q/2=1/2+O(1/y)\), where the flat lower edge of \(W\) suppresses
the stationary term. No large-\(h\) assumption entered the error proof.

### \(h\asymp H_y\): pass

Here \(h\ll\sqrt y\). The closest stationary point has ordinary distance
\(\asymp1/h\), but is \(\gg y^{1/4}\) stationary widths away. The endpoint
derivative gap remains at least \(y/8\), and (7.3)--(7.4) still apply.

### Both signs: pass

For \(h>0\), only negative Poisson frequencies are stationary; for \(h<0\),
only positive ones are. The formulas are conjugate. The cone retains
\(\chi_4(h)\).

### Full endpoint versus midpoint: pass

The midpoint formula weighs \(d=y\) by \(1/2\), while the project sum gives
weight \(1\). Adding the missing half changes
\(\frac i2e(A_h)\cot(\pi\nu_h)\) into
\(e(A_h)/(1-e(\nu_h))\). This nonzero \(O(1)\) term cannot be removed by a
convention change.

## 9. First doubtful or unproved step

There is no unproved endpoint-separation, half-weight, lattice-cone,
stationary-amplitude, boundary-size, or Vaaler-error summation step in
(1.1)--(7.7). The first unproved analytic step is the signed cone estimate
(1.5), equivalently the \(M^{3/4}\) product-phase bound for (7.6). Taking
absolute values, applying Cauchy in \(h\), or treating the product-grouped
coefficient as smooth would erase the retained structure and is not
justified.

Consequently this report does not prove the full top \(M2\) block and does
not prove M9-endpoint-uniformity.

## 10. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- rounds/codex-managed/m9-top-endpoint-transform/briefs/one_sided_poisson_derivation.md
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md
- rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md

No proof draft, validation matrix, legacy response, web source, or
computational artifact was used.

## 11. Recommended state effect

1. **Promote a scoped internal endpoint-transform lemma:** (1.1), including
   the half-weight, explicit boundary (4.4), exact cone (5.5), stationary
   constant, and summed error (7.4).
2. **Record odd-frequency endpoint separation as proved:** (1.3), with the
   qualification that ordinary \(u\)-distance is only \(\asymp1/h\), while
   stationary-scale separation is uniform and growing.
3. **Revise M9-M2-top-endpoint-transform:** the hard denominator endpoint is
   reduced to the exact signed cone (7.6), with boundary and transform
   errors target-sized. The remaining candidate is (1.5).
4. **Retain M9-M2 and M9-endpoint-uniformity as open:** the cone estimate is
   not proved, so the full top block is not closed.
5. **Do not transfer the smooth interior packet theorem automatically:** the
   cone has a hard lower edge where \(W(1)=1\); a successor must retain that
   edge and \(\chi_4(h)\).
