# Round227: nonauthor Mellin application review

Campaign: `gc-complete-joint-spectral-remainder`. Role: `independent_mellin_application_review`, NONAUTHOR and NONBLIND after completion of the isolated phase task. Generated: 2026-09-28T07:36:53+08:00. No graph was read or edited. Review target: `controls/conductor_mellin_phase_application.md`, SHA256 **`1A519E5624EF72B28544A9762584F88A26B000377B572B308F7100D7F527CEF4`**.

## 1. Result

**GREEN for the exact control hash above and its explicitly scoped claims.** Equations (1)--(5) have the correct phase derivatives, frequency sign, uniform curvature, interior expansion, actual amplitude substitution, and weighted norm. Equations (6)--(8) correctly compute a stationary point of the leading Stirling phase and correctly expose its failure of uniform applicability in the small-shift gamma transition.

There is one harmless phase convention to make explicit: the literal leading expansion of the gamma quotient has the constant factor \(e^{-i\pi/2}=-i\). The control's displayed phase (6) omits this universal constant, which can be retained in the complex amplitude. It does not change either stationary equation, the reduced oscillatory phase in (7), or the transition scale (8). This convention was communicated to the conductor before freezing this review; it is not an unproved gain or a request for a mathematical repair.

The outcome is not a certification of a full joint stationary-phase asymptotic, contour movement, source coefficient identification, spectral tail bound, all-shift cancellation estimate, or improved wave bound. The reviewed control expressly makes none of those claims.

## 2. Exact hypotheses and review scope

For the elementary phase, retain the control's assumptions \(0<d<3/2\), \(L\geq1\), smooth zero extension, support
\(D_d=(d+1/2,2)\), and uniform fixed-order amplitude derivative bounds. Complex amplitudes are allowed. Lower mass of order \(L^{b+1/2}\) is asserted only after fixing a nonzero amplitude on a fixed interior interval and restricting the frequency ratio to an interval on which its modulus is bounded below. There is no uniform positive lower bound for arbitrary families.

For the actual application, the full packet fixes every real \(cT\leq R\leq CT\), every dyadic \(2\leq N\leq P<2T^{3/2}\), every positive shift \(h<2N\), the real smooth \(g_N\), and \(A_J=(1+N/T)^{-J}\). No sign restriction is imposed on \(\Psi\), and no sharp or arithmetic mask is present.

For (6)--(8), the spectral parameter \(t>0\) is held fixed when differentiating in \(y,\tau\). The calculation is confined to \(\tau>t>0\), with \(\tau-t\) large for a valid separate large-argument gamma expansion. A critical point is relevant only if its resulting \(y\) lies in the actual overlap. The control does not assert that such a point exists for every spectral \(t\), or that the asymptotic owns the transition \(\tau-t=O(1)\).

The gamma quotient is used exactly as recorded and already source-audited in the authorized closed226 report. This is an application and algebra review, not a new independent primary-source audit. The review does not treat the author's own isolated report as independently reviewed evidence.

## 3. Proof and seam verification

### Elementary phase, constants and estimates

Set \(u=\sqrt{1-d/y}\), so \(1/2<u<1\). Since
\[
u'=(1-u^2)/(2uy),\qquad
g_d(y)=\frac1{2\sqrt y\,u(1+u)},
\]
direct differentiation gives
\[
\frac{g_d'}{g_d}
 =-\frac1{2y}-\left(\frac1u+\frac1{1+u}\right)
                  \frac{1-u^2}{2uy}
 =-\frac{1+u-u^2}{2yu^2}.
\]
This is exactly the control's equation (1). The signs are positive for \(g_d\) and negative for \(g_d'\).

The integral identity
\[
f_d(y)=\frac12\int_0^1(y-\theta d)^{-1/2}\,d\theta
\]
also gives
\[
-g_d'(y)=\frac18\int_0^1
 (y+2\theta d)(y-\theta d)^{-5/2}\,d\theta
 \geq\frac1{8y^{3/2}}.
\]
On the whole overlap this proves, for example,
\[
\frac1{4\sqrt2}\leq g_d\leq\frac{\sqrt2}{3},\quad
-g_d'\geq\frac1{16\sqrt2},\quad
-yg_d'\geq\frac1{8\sqrt2}.
\]
Upper bounds and every fixed derivative bound are uniform because \(y\) and \(y-d\) remain in \([1/2,2]\). Thus \(d\downarrow0\) introduces no division loss, despite the unreduced formula for \(f_d\).

For \(v=\log y\), the full phase has second derivative \(-Lyg_d'(y)\), independently of \(\tau\). Its first derivative is \(\tau-Lg_d(y)\). The unique possible stationary point therefore has positive \(\tau\), positive curvature, and ratio
\[
\tau/L\in(g_d(2),g_d(d+1/2)).
\]
The bounded-variation second-derivative estimate gives \(O(L^{-1/2})\) without requiring a support margin. It can also be proved by splitting where the absolute first derivative is at most \(\sqrt L\), whose length is \(O(L^{-1/2})\), and integrating by parts on the two remaining monotone portions.

Choose an enlarged fixed cone, for example
\([L/(8\sqrt2),2\sqrt2 L/3]\). Outside it the first derivative has magnitude comparable to \(L+|\tau|\); all its nonconstant derivatives are \(O_j(L)\). Each integration-by-parts step then gains \((L+|\tau|)^{-1}\), with no boundary term because of zero extension. This verifies both stationary and rapid nonstationary scopes, including \(\tau=0\).

For the alternate Plancherel proof, let \(H(v)=b_d(v)e^{iLF_d(v)}\). Its \(k\)-th derivative has \(L^2\) norm \(O_k(L^k)\). Cauchy on \(|\tau|\leq L\) gives \(O(L^{b+1/2})\). On \(|\tau|\asymp S\geq L\), weighted Cauchy and Plancherel give
\[
O(L^kS^{b+1/2-k}).
\]
For an integer \(k>b+1/2\) these annuli form a convergent geometric sum of order \(L^{b+1/2}\). This independently verifies the stated weight exponent, including nonintegral \(b\geq0\).

At an interior critical point, the original-coordinate curvature is \(-g_d'(y_*)/y_*\), so the coefficient in equation (4) is exactly
\[
a_d(y_*)\sqrt{\frac{2\pi y_*}{L[-g_d'(y_*)]}}.
\]
The positive curvature gives \(+\pi/4\). A quadratic local change of coordinates gives the stated \(O(L^{-3/2})\) remainder uniformly on a fixed interior ratio interval. The rest is nonstationary. The reduced phase satisfies
\(F'(\nu)=\log y_\nu\) and
\(F''(\nu)=1/(y_\nu g_d'(y_\nu))<0\), as printed. Complex amplitudes cause no difficulty: a uniform nonzero modulus makes the leading term dominate the error in absolute value. This proves the matching order only on the control's specified fixed example.

### Actual amplitude and weighted norm

Substitute \(x=Ny-h\), \(d=h/N\), and \(\lambda=2\pi R\sqrt N\). Then the packet's exact test becomes
\[
q_h(y)=g_N(Ny)g_N(Ny-h)
       e^{i\lambda(\sqrt y-\sqrt{y-d})}.
\]
Consequently
\[
\widehat q_h(\sigma+i\tau)=
\int g_N(Ny)g_N(Ny-h)y^{\sigma-1}
 e^{i[(\lambda d)f_d(y)+\tau\log y]}\,dy,
\]
with \(L=\lambda d=2\pi Rh/\sqrt N\). The amplitude is exactly the one in the control. In particular there is no omitted Jacobian in this Mellin transform: it is defined in the scaled \(y\) variable. The factor \(N^s\) belongs to the separate Mellin pairing, not to this amplitude or norm.

For fixed derivative order, differentiating \(g_N(Ny)\) or \(g_N(Ny-h)\) uses a scaled derivative of \(g_N\), bounded by \(O(A_J)\) after the packet's reservation of fixed Schwartz order. Since \(1/2<y<2\), derivatives of \(y^{\sigma-1}\) are bounded for fixed \(\sigma\). The amplitude seminorms are therefore \(O_{J,\sigma}(A_J^2)\), without absolute-valuing or modifying the amplitude itself.

This proves exactly
\[
\int(1+|\tau|)^b|\widehat q_h(\sigma+i\tau)|\,d\tau
 \ll_{b,J,\sigma}A_J^2(1+Rh/\sqrt N)^{b+1/2}.
\]
The harmless \(1+\) also covers bounded phase parameters, either by the same Plancherel proof with \(1+L\), or by bounded-parameter smooth Fourier estimates. For large \(T\), \(h\geq1\) and \(N<2T^{3/2}\) give \(L\gg T^{1/4}\), with constants depending only on the fixed radius window.

If \(h\geq3N/2\), the continuous overlap is empty and \(q_h=0\). If only its integer overlap is empty, there is no such inference: \(q_h\) and its continuous density may remain. The reviewed control makes this distinction correctly. It has no hidden cutoff jumps or discarded signed \(\Psi\) factors.

### Independent derivation of the joint leading-Stirling point

The closed226 equation (20) records
\[
G(s,it)=\frac{\Gamma(s-1/2+it)\Gamma(s-1/2-it)}{\Gamma(s)^2}.
\]
For fixed \(\sigma\), \(s=\sigma+i\tau\), and \(\tau>t>0\) with \(\tau-t\to\infty\), the leading Stirling expression is
\[
G(\sigma+i\tau,it)=
-i\,\frac{(\tau^2-t^2)^{\sigma-1}}{\tau^{2\sigma-1}}
 e^{iQ(\tau,t)}\left(1+O_\sigma((\tau-t)^{-1})\right),
\]
where
\[
Q=(\tau+t)\log(\tau+t)+(\tau-t)\log(\tau-t)-2\tau\log\tau.
\]
Indeed the three linear imaginary-argument terms cancel. The numerator's constant phase is \((\sigma-1)\pi\), the denominator's is \((\sigma-1/2)\pi\), leaving \(-\pi/2\). Their exponential size factors cancel in this region. This accounts explicitly for the universal \(-i\) factor noted in Section 1.

The discrete spectral factor in closed226 is \(N^s h^{1/2-s}\) times constants and coefficients independent of the Mellin integration variable. Its oscillation supplies \(\tau\log(N/h)=-\tau\log d\). Combined with the exact test it gives, up to the universal constant phase,
\[
\Phi(y,\tau;t)=\lambda(\sqrt y-\sqrt{y-d})
          +\tau\log(y/d)+Q(\tau,t),
\]
which is precisely control (6). This verification concerns that gamma quotient; no continuous-spectrum prefactor or spectral coefficient has been declared constant in the full problem.

Differentiation, with \(t\) fixed, gives
\[
\Phi_y=\frac\lambda2\left(y^{-1/2}-(y-d)^{-1/2}\right)+\frac\tau y,
\]
\[
\Phi_\tau=\log\left[\frac yd\left(1-\frac{t^2}{\tau^2}\right)\right].
\]
The second equation implies \(u:=t/\tau=\sqrt{1-d/y}\). The first then becomes
\[
\tau=\frac{\lambda\sqrt y(1-u)}{2u},\qquad
t=\frac{\lambda\sqrt y(1-u)}2
 =\frac\lambda2(\sqrt y-\sqrt{y-d}).
\]
There is at most one interior \(y\) for a fixed \(t\), because the last difference strictly decreases in \(y\). Existence requires that \(t\) lie in its actual overlap image; nothing here asserts existence outside that image.

At this point the first phase term is \(2t\), and the remaining terms simplify exactly to
\[
\tau\{-\log(1-u^2)+(1+u)\log(1+u)+(1-u)\log(1-u)\}
 =t\log\frac{1+u}{1-u}.
\]
Since
\[
\frac{1+u}{1-u}
 =\frac d{(\sqrt y-\sqrt{y-d})^2}
 =\frac{\lambda^2d}{4t^2}
 =\frac{\pi^2R^2h}{t^2},
\]
this proves every constant and sign in control (7).

As an additional algebraic control, the Hessian in \((y,\tau)\) at this point obeys
\[
\Phi_{yy}=\frac{\tau(1+u-u^2)}{2y^2u^2}>0,\quad
\Phi_{y\tau}=\frac1y,\quad
\Phi_{\tau\tau}=\frac{2u^2}{\tau(1-u^2)}>0,
\]
\[
\det\nabla^2_{y,\tau}\Phi=\frac{u}{y^2(1-u^2)}>0.
\]
Thus the interior point is nondegenerate and in fact a local minimum of this real leading phase. The term “saddle” is being used in its generic asymptotic stationary-point sense, not to claim a mixed Hessian signature. This computation does not prove a uniform two-variable asymptotic.

Finally,
\[
1-u=\frac d{y(1+u)},\qquad
\tau=\frac{\lambda d}{2\sqrt y\,u(1+u)}\asymp Rh/\sqrt N,
\]
and therefore the exact saddle expression is
\[
\tau-t=\frac{\lambda d^2}{2y^{3/2}u(1+u)^2}
 =\frac{\pi Rh^2}{N^{3/2}y^{3/2}u(1+u)^2}
 \asymp Rh^2/N^{3/2}.
\]
This proves (8) uniformly as an algebraic comparison on the overlap. Separate Stirling expansions require this last quantity to be large, so they are not a full-range uniform approximation when
\(h\lesssim N^{3/4}R^{-1/2}\). A genuinely asymptotic small relative error requires separation beyond that transition. The control explicitly retains this restriction.

### Signed inversion and the full real/complex bridge

For any allowed amplitude, logarithmic Fourier inversion reads
\[
b_d(v)e^{iLF_d(v)}=\frac1{2\pi}
       \int K_d(L,\tau)e^{-i\tau v}\,d\tau.
\]
Its modulus is \(|b_d(v)|\), even where the absolute frequency mass has order \(L^{1/2}\). The polynomial norm cost is an absolute-transfer upper certificate; it is not a lower bound for a recombined test, for a particular actual test, or for the signed spectral pairing. Similarly the leading interior reduced phase is not a license to replace the exact gamma transition. These separations are maintained in the control.

The packet's sufficient inequality (F) uses one outer real part and every \(h<2N\). With \(L_N=3N/2-1\) and \(H=2N\), the factor \((L_N+H-1)/H\) is bounded. The normalized Fejer square thus contains the diagonal price \(A_J^2N^{-1/2+\eta}\), the density price \(A_J^2T^{-1}N^\eta\log N\), and the hypothetical remainder price \(A_J^2T^\epsilon\). The powers \(N^\eta\) are harmless only after choosing \(\eta\) sufficiently small using \(N<2T^{3/2}\).

If (F) were proved, taking square roots and summing the exact overlapping partition over \(O(\log T)\) blocks, including the singleton and the fixed-Schwartz far tail, would give the stronger complete complex wave \(T^\epsilon\). Its fixed rotated real part is the real wave. The authorized204 kernel's sharp bridge then gives
\(P(R^2)\ll T^{1/2+\epsilon}\), hence the quarter exponent after renaming \(\epsilon\). The inherited real exponent \(\beta\) is never substituted for a complex estimate. The phase control proves none of (F), a new complete exponent, or a new moment estimate; its claim of no complete gain is correct.

## 4. First doubtful or unproved step

There is no unresolved defect in the scope certified GREEN. The omitted universal gamma phase constant is accounted for explicitly above and changes no claim in the reviewed control.

The first invalid extension would be treating (6)--(8) as a uniform asymptotic at \(\tau-t=O(1)\), or inserting the norm from (5) as if it controlled signed spectral cancellation with no loss. The first substantive analytical obligation remains the complete signed all-shift remainder (F), with actual source coefficients, every continuous term, justified contours and all tails. None is discharged here. For this review, the gamma quotient's source provenance remains the expressly authorized closed226 audit rather than a newly checked primary source.

## 5. Required controls and outcomes

1. **Derivative/sign/constants — PASS.** Direct differentiation reproduces control (1); logarithmic curvature is positive uniformly. The original stationary curvature gives the exact \(2\pi\) coefficient and \(+\pi/4\) correction in (4).
2. **Zero amplitude, zero frequency and endpoints — PASS.** Zero amplitudes give zero norms. At \(\tau=0\) the transform is rapidly decreasing. The uniform upper estimate uses curvature, so crossing an endpoint requires no interior expansion. The lower estimate retains a fixed interior nonvanishing interval.
3. **\(d\downarrow0\) and shrinking overlap — PASS.** The integral formula gives the limits \(f_0=1/(2\sqrt y)\), \(g_0=1/(4\sqrt y)\) without a hidden loss. Flat zero extension on an overlap of width \(h_0=3/2-d\) forces each fixed amplitude seminorm to be \(O_M(h_0^M)\) after using higher derivative bounds; no uniform positive lower constant follows.
4. **Actual scale and overlap — PASS.** \(L=2\pi Rh/\sqrt N\), no Mellin Jacobian is missing, and the amplitude seminorms are \(O(A_J^2)\). Empty continuous overlap and empty integer overlap have different consequences, correctly retained. The \(N^s\) pairing factor is outside the transform norm.
5. **Joint critical point and phase — PASS.** Differentiation and substitution prove (7), including \(\pi^2R^2h\). The literal gamma approximation carries a constant \(-i\), harmless to those equations. The Hessian computation supplies an independent nondegeneracy control without claiming a full asymptotic.
6. **Small-shift transition — PASS.** At a formal interior critical point with \(N\asymp T^{3/2}\), \(R\asymp T\), \(h=1\), one has \(\tau\asymp T^{1/4}\) but \(\tau-t\asymp T^{-5/4}\). Thus large Mellin height does not make both numerator gamma arguments large. This is an analytic scale example, not an assertion that a discrete eigenvalue equals that particular critical \(t\). It verifies the reason the control denies a global saddle asymptotic.
7. **Inverse transform and real/complex scope — PASS.** Large absolute transform mass can coexist with bounded or vanishing signed reconstruction. The inherited real \(\beta\) is not promoted to a complex bound, and the complete conditional Fejer bridge includes every shift, diagonal, density, singleton and tail.

No experiments or web research were conducted. All checks are analytical or algebraic; no numerical computation is evidence for the asymptotic statements.

## 6. Dependencies, exact artifacts and provenance

This is a separate, post-isolation NONAUTHOR application review. The reviewer previously authored the frozen isolated phase report and retains that derivation and its original statement packet. It is therefore not history-free and does not claim to be an independent reviewer of its own report. The author of the control is the conductor. No current source-role report, sibling review, graph, campaign manifest, or other mathematical input was read in this assignment.

Authorized input bindings:

| Artifact | SHA256 |
|---|---|
| `protocol.md` | `F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A` |
| `rounds/codex-managed/gc-complete-joint-spectral-remainder/controls/conductor_mellin_phase_application.md` | `1A519E5624EF72B28544A9762584F88A26B000377B572B308F7100D7F527CEF4` |
| `rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/complete_joint_spectral_interface.md` | `ED64B7189D806DAE4DFBF5A2DA598268E09722D9C3812EC0C1376727D8B05D7C` |
| `strategy/round227_complete_joint_spectral_remainder.md` | `C91B9EC5836A4B1C998B18724C951C059241A975F55CAA149BA4449AB0F5E19E` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083C3A124FFB8320F306EB767DE376AE45E2B3B12175FFE9C5B70FEEB5212` |
| `rounds/codex-managed/gc-full-goal-spectral-source-review/reports/actual_shifted_spectral_sources.md` | `1BCB14E1899138097A3AB0E273060F2DEAA800E3EB732E2924AFB2F1F02D25BC` |
| Own frozen `rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/blind_mellin_phase.md` | `31553BBEE7F049E3B2CBEA58F04634854BFE4551AC484FB85D308CBCE07D96E2` |

The original statement packet is retained history through the last listed report, not a newly read application source. The closed226 report is used for its exact gamma quotient and complete transfer/bridge; its other cited files and external links were not opened. An exact-name filename search resolved the authorized strategy and closed226 report paths after two guessed paths did not exist; no additional file contents were accessed. The current control hash was checked before analysis and remains the binding of this review. Only this assigned review file was written.

## 7. Recommended state effect

**Retain, GREEN within scope**, the conductor's frozen phase/application control. Record that the leading gamma phase is understood modulo its explicit universal \(-\pi/2\) constant and that the small-shift transition remains outside a separate-Stirling uniform asymptotic.

**No change** to any accepted theorem, full remainder obligation, pointwise exponent, moment frontier, real/complex benchmark, or authoritative graph. This review certifies a scoped analytical control and the accuracy of its limitations. It does not certify its author's own isolated report as independently reviewed evidence. Freeze this report by its external SHA256 and stop; no successor work is selected.
