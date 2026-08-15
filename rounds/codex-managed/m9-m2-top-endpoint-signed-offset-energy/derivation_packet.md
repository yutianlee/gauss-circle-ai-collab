# Round 76 derivation packet: signed offset energy and gcd lifts

Campaign: m9-m2-top-endpoint-signed-offset-energy  
Round: 76  
Starting graph SHA-256:
baa5fc13ca3682ae561c44cd1b20e94728c117378545f586ff3224c16a8eeb6b

## 1. Accepted finite energy

Put \(J=\sqrt X\), let \(1\leq L\leq H\leq J^{1/2}\), let
\(\mathscr H_L\) be the actual finite odd support, and retain the exact
top-endpoint symbol \(a(h,m)\).  Round 75 proved

\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\leq h\leq4m}}
 \chi_4(h)a(h,m)e(J\sqrt{hm}),
\]

\[
 \mathcal T_L=\sum_mR_m,\qquad
 |\mathcal T_L|^2\ll L\mathcal E_L^\top,\qquad
 \mathcal E_L^\top=\sum_m|R_m|^2.
 \tag{76.1}
\]

The diagonal is \(O(L^2)\).  The exact positive-offset part is

\[
\begin{aligned}
 \mathcal O_L
 ={}&2\Re\sum_{r\geq1}(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a(h,m)\overline{a(h+2r,m)}\\
 &\hspace{24mm}\times
 e\!\left(-\frac{2rJ\sqrt m}
 {\sqrt h+\sqrt{h+2r}}\right).
 \tag{76.2}
\end{aligned}
\]

The sign is exact:

\[
 \chi_4(h)\chi_4(h+2r)=(-1)^r.
 \tag{76.3}
\]

The frozen target is

\[
 \boxed{\ \mathcal O_L\ll_\varepsilon L^2X^\varepsilon.\ }
 \tag{76.4}
\]

This is sufficient for the hard top-\(M2\) cone.  No transform is
needed to define it.

## 2. Exact endpoint and capacity ledger

For \(s=h+2r\), the \(m\)-interval is

\[
 \lceil s/4\rceil\leq m\leq h,\qquad
 h,s\in\mathscr H_L,\qquad s\leq4h.
 \tag{76.5}
\]

The diagonal is target-safe.  The two endpoint samples for every
\((h,r)\), and any fixed-width endpoint collar, have total
\(O(L^2)\) capacity.  A collar of growing width cannot be discarded
absolutely.  Any Poisson argument must therefore retain the complete
sharp-endpoint or incomplete-Fresnel ledger outside fixed width.

Every fixed offset \(r\) has \(O(L^2)\) absolute capacity, but there are
\(O(L)\) offsets.  The target is a signed union estimate, not a
shellwise absolute estimate.

## 3. Candidate Poisson transform in the common variable

Set

\[
 C_{h,r}
 =\frac{2rJ}{\sqrt h+\sqrt{h+2r}}
 =J(\sqrt{h+2r}-\sqrt h)>0.
 \tag{76.6}
\]

The oscillation in (76.2) is \(e(-C_{h,r}\sqrt m)\).  On a smooth
interior \(m\)-cell, Poisson summation has a stationary point only at a
negative Poisson mode.  Write that mode as \(-k\), \(k\geq1\).  The
phase and saddle are

\[
 -C_{h,r}\sqrt x+kx,\qquad
 x_*=\frac{C_{h,r}^2}{4k^2},
 \tag{76.7}
\]

and, with \(e(z)=e^{2\pi iz}\),

\[
 \int A(x)e(-C_{h,r}\sqrt x+kx)\,dx
 =
 \frac{e(1/8)C_{h,r}}{\sqrt2\,k^{3/2}}
 A(x_*)e\!\left(-\frac{C_{h,r}^2}{4k}\right)
 \text{corrections}.
 \tag{76.8}
\]

The saddle belongs to the exact interval only when

\[
 \lceil(h+2r)/4\rceil\leq
 \frac{C_{h,r}^2}{4k^2}\leq h.
 \tag{76.9}
\]

Up to the floor-safe endpoint transition this is

\[
 \frac{C_{h,r}}{2\sqrt h}\leq k
 \leq\frac{C_{h,r}}{\sqrt{h+2r}},
 \qquad k\asymp\frac{Jr}{L}.
 \tag{76.10}
\]

Equations (76.8)--(76.10) are a candidate interface.  The full
one-sided endpoint terms, transition Fresnel functions, stationary
corrections, stars, and summed errors must be proved before promotion.

## 4. Exact gcd-lift phase

Write

\[
 h=ga,\qquad h+2r=gb,\qquad (a,b)=1,\qquad b>a.
 \tag{76.11}
\]

Because both frequencies are odd, \(g,a,b\) are odd and

\[
 r=\frac{g(b-a)}2,\qquad
 (-1)^r=e\!\left(\frac{g(b-a)}4\right).
 \tag{76.12}
\]

At the saddle,

\[
 C_{h,r}=J\sqrt g(\sqrt b-\sqrt a),\qquad
 x_*=
 g\,\frac{X(\sqrt b-\sqrt a)^2}{4k^2}.
 \tag{76.13}
\]

The \(k\)-range is independent of \(g\), apart from the exact ceiling
transition.  Most importantly, the complete stationary phase is linear
in the lift:

\[
 e(g\alpha_{a,b,k}),\qquad
 \alpha_{a,b,k}
 =\frac{b-a}{4}
 -\frac{X(\sqrt b-\sqrt a)^2}{4k}.
 \tag{76.14}
\]

The available lift interval has length

\[
 G_{a,b}\asymp\frac{L}{\max(a,b)}
 \tag{76.15}
\]

when nonempty.  The actual amplitude remains a moving sampled profile in
\(g\); it may not be replaced by arbitrary or constant coefficients.

The same phase in the original variables is

\[
 \Theta_k(h,s)
 =\frac{s-h}{4}
 -\frac{X(\sqrt s-\sqrt h)^2}{4k}.
 \tag{76.16}
\]

It is homogeneous of degree one in \((h,s)\), and its Hessian has
determinant zero.  Treating it as a nondegenerate two-dimensional phase
is forbidden.  The exact linear \(g\)-direction is the lawful
replacement.

## 5. Candidate resonance survivor

Away from

\[
 \|\alpha_{a,b,k}\|\lesssim G_{a,b}^{-1},
 \tag{76.17}
\]

summation in \(g\) should gain by a geometric or sampled-BV estimate.
Near (76.17), the primitive pair, exact \(k\)-range, actual stationary
weight, endpoint transitions, and all gcd multiplicities must remain.

A useful outcome is any one of:

1. a proof of (76.4);
2. a strict polynomial \(L\)-subrange;
3. a complete actual-symbol resonance inequality after the \(g\)-sum;
4. a rigorous self-return or capacity no-go showing that (76.17) is
   equivalent-hard to an accepted open block.

Coefficient-blind phase conjugation, shellwise absolute values, or a
Hessian determinant cannot certify the target.

## 6. Required controls

Every report must audit:

1. exact ceiling, stars, and both \(m\)-endpoints;
2. the diagonal and fixed-offset capacities;
3. the sign \((-1)^r\) before absolute values;
4. Poisson-mode orientation, saddle, Gaussian unit, and Jacobian;
5. full endpoint/Fresnel and stationary-error aggregation;
6. gcd uniqueness, odd parity, and lift multiplicity;
7. the exact \(g\)-linear phase and actual moving amplitude;
8. rank-one Hessian and transform self-return;
9. exact squares, fourth powers, and near-integer resonances;
10. adversarial coefficients versus the actual symbol;
11. applicability of any cited exponent-pair, spacing, or spectral theorem;
12. separation from smooth packets, full \(M2\), \(M9\), and the exponent.

## 7. Promotion and stopping rule

Promote (76.4) only if the complete finite energy, including every
endpoint and actual-symbol contribution, is bounded.  Promote a
Poisson/gcd reduction only after its constants, endpoints, error sum,
and statement-only gate pass.

A precise resonance survivor or no-go is useful progress.  Do not
promote the hard top cone, full \(M2\), \(M9\), or the global exponent
from a formal transform or a partial cell estimate.

