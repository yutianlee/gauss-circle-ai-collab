## 1. Result

The scalar critical-point calculation is correct for the declared orientation \(c=-n/2\), but it does **not** transform the literal coefficient supplied in the packet. With the Poisson convention \(e(-\ell k)\), \(e(-hu)\), the \(k\)-critical point has negative Hessian and Gaussian factor \(e(-1/8)\); the subsequent \(u\)-critical point has positive Hessian and factor \(e(+1/8)\). The factors cancel. The joint scalar main phase is exactly

\[
-\delta^2,\qquad
\delta=J\sqrt{\frac{dn\ell}{s}}-\frac12\sqrt{\frac{as}{d}},
\qquad s=d-2h>0.
\]

For an interior joint saddle,

\[
\mathcal N_{k,u}
=\left|\det D^2_{(u,k)}P\right|^{-1/2}
=\sqrt{\frac{k_*b_*}{\ell s d}},
\]

where \(P(u,k)=du/2-n\Lambda_{du}/(2k)\). The stationary support is

\[
q_*:=\frac{b_*-a}{2}\in I,\qquad
\frac{n b_*}{4}<\ell<na,\qquad
dJn<s<2dJn\sqrt{\frac a{b_*}},
\]

with \(\ell\in\mathbb Z_{>0}\) and \(s\) positive odd. The last pair of inequalities is equivalent once \(b_*=4d^2Xn\ell/s^2\) is imposed.

The exact capacity consequence is preservation of local \(L^2\) density:

\[
\mathcal N_{k,u}^{\,2}
\left|\det\frac{\partial(\ell,h)}{\partial(k,u)}\right|=1.
\]

On a nondegenerate shell, the dual region has \(\asymp dJD n^2\) cells per \((d,n)\); a scalar coefficient of initial size \(\sqrt{AL/(JD)}\) becomes of size \(\asymp \sqrt{L/J}/(dn)\); and the square-sum capacity remains

\[
\asymp \sqrt{\frac{LD}{d}}.
\]

Thus even square-root cancellation in the scalar dual family merely returns the primal capacity; it does not by itself give \(L^2/A\). The required additional saving relative to that capacity is

\[
\rho_d=\frac{L^2/A}{\sqrt{LD/d}}
=\frac{L^{3/2}\sqrt d}{A\sqrt D}.
\]

The sharp verdict is: promote the scalar saddle algebra and capacity identity only; do not promote a transform of the actual coefficient or the maximal theorem. The packet gives fixed-\(q\) \(k\)-variation only. It gives no mixed or \(q\)-regularity, no lawful extension across floors, stars, collars and owner masks, no control of the centered physical phase on either stationary scale, and no weighted capacity bound for the \((g,\nu)\)-vector.

## 2. Exact statement and hypotheses

Fix \(d\mid a\) with \(\mu(d)\ne0\), so \(d\) is odd, and fix one scalar channel \((g,\nu)\) in the negative orientation. Then \(n=|2\nu-g|\) is positive and odd. Put \(q=du\), \(b=a+2du\), and

\[
P_{d,n}(u,k)=\frac{du}{2}-\frac{n\Lambda_{du}}{2k}.
\]

The critical-point and Hessian identities below are unconditional algebra. Turning them into a two-stage stationary asymptotic for the actual coefficient requires all of the following additional hypotheses.

- The literal discrete coefficient has an exact compactly supported extension in \((u,k)\), or an exact discrete Fourier formulation, for which two Poisson formulas hold with the prescribed half-open conventions.
- The scalar saddle lies away from the \(k\)-endpoints, maximal \(u\)-endpoints, collar boundaries, floor/star jumps, lift boundaries and owner-mask jumps by the relevant stationary widths. Boundary and nonstationary terms must otherwise be retained explicitly.
- If the centered physical integral is put in the amplitude, its full vector representative is symbol-smooth on
  \[
  w_k=\sqrt{\frac{k_*}{2\ell}},\qquad
  w_u=\sqrt{\frac{2b_*}{sd}},
  \]
  with quantitative mixed \((u,k)\)-derivative or variation bounds and summable endpoint traces. If its phase changes by order one on either width, that phase must instead be inserted into \(P_{d,n}\), and the critical equations and support must be recomputed.
- Every owner mask and complement, finite-lift cutoff, and maximal indicator \(\mathbf1_{du\in I}\) remains inside the actual vector. Replacing one by a smooth symbol requires a uniform maximal reduction and a bound for all jump terms.
- Stationary errors, nonstationary frequencies, boundary saddles, and all outer \((g,\nu,d)\)-sums are summable. In particular, quantitative hypotheses on \(\widehat W_R\), \(\mathcal G_{a,b}\), and their \(q\)-dependence are required; none are in the packet.

Under these added hypotheses, the scalar interior main term has phase \(e(-\delta^2)\), normalization \(\mathcal N_{k,u}\), and no residual Gaussian root of unity. None of those hypotheses follows from

\[
\sup_k|B_{a,q,g}(k)|+\operatorname{Var}_kB_{a,q,g}(k)
\ll_\varepsilon X^\varepsilon\sqrt{\frac{AL}{JD}}.
\]

## 3. Proof or derivation

**Möbius carrier.** Since \(a\), and hence each relevant \(d\mid a\), is odd,

\[
(-1)^q=e(q/2)=e(du/2).
\]

For \(c=-n/2\), the scalar phase before dualization is \(P_{d,n}(u,k)\).

**First stationary transform.** Set \(C=n\Lambda_{du}/2>0\). The \(\ell\)-th Poisson integral has phase

\[
\phi_\ell(k)=-\frac Ck-\ell k.
\]

Its derivative vanishes only for \(\ell>0\), at

\[
k_*^2=\frac C\ell=\frac{n\Lambda_{du}}{2\ell}.
\]

At this point

\[
\phi_\ell(k_*)=-2\sqrt{C\ell}
=-\sqrt{2n\Lambda_{du}\ell}
=-J(\sqrt b-\sqrt a)\sqrt{n\ell},
\]

and

\[
\phi_\ell''(k_*)=-\frac{2\ell}{k_*}<0.
\]

For \(e(x)=e^{2\pi ix}\), an interior smooth saddle contributes

\[
e(-1/8)\,\mathcal N_k,\qquad
\mathcal N_k=\sqrt{\frac{k_*}{2\ell}}
=\frac{(n\Lambda_{du})^{1/4}}{2^{3/4}\ell^{3/4}}.
\]

Writing

\[
k_-=\frac{J(\sqrt b-\sqrt a)}{2\sqrt a},
\qquad
k_+=\frac{J(\sqrt b-\sqrt a)}{\sqrt b},
\]

the strict interior condition \(k_-<k_*<k_+\) is exactly

\[
\frac{nb}{4}<\ell<na.
\tag{3.1}
\]

**Second stationary transform.** After extracting the first scalar phase, the \(h\)-th \(u\)-integral has

\[
\psi_h(u)=\left(\frac d2-h\right)u
-J\sqrt{n\ell}\sqrt{a+2du}+J\sqrt{an\ell}.
\]

Put \(s=d-2h\), which is odd. Then

\[
\psi_h'(u)=\frac s2-\frac{Jd\sqrt{n\ell}}{\sqrt b}.
\]

There is a positive-\(b\) saddle only for \(s>0\), and it satisfies

\[
\sqrt{b_*}=\frac{2Jd\sqrt{n\ell}}s,\qquad
b_*=\frac{4d^2Xn\ell}{s^2},\qquad
u_*=\frac{b_*-a}{2d}.
\]

Moreover,

\[
\psi_h''(u_*)
=\frac{Jd^2\sqrt{n\ell}}{b_*^{3/2}}
=\frac{sd}{2b_*}
=\frac{s^3}{8dXn\ell}>0.
\]

Thus the second Gaussian factor and normalization are

\[
e(+1/8)\,\mathcal N_u,\qquad
\mathcal N_u=\sqrt{\frac{2b_*}{sd}}
=\sqrt{\frac{8dXn\ell}{s^3}}.
\]

The Gaussian factors cancel. Direct substitution gives

\[
\begin{aligned}
\psi_h(u_*)
&=-\frac{dXn\ell}{s}-\frac{as}{4d}+J\sqrt{an\ell}\\
&=-\left(J\sqrt{\frac{dn\ell}{s}}-\frac12\sqrt{\frac{as}{d}}\right)^2.
\end{aligned}
\]

At the saddle,

\[
\delta=\frac12\sqrt{\frac{s}{d}}(\sqrt{b_*}-\sqrt a),
\qquad
\delta^2
=\frac{s}{4d}(\sqrt{b_*}-\sqrt a)^2
=\frac{s q_*^2}{d(\sqrt{b_*}+\sqrt a)^2}.
\tag{3.2}
\]

Exact square resonance forces \(b_*=a\), equivalently \(q_*=0\), and is absent from \(q\ge D\ge1\). On scale, (3.2) has size \(\asymp JnD^2/A\).

**Joint support.** The maximal cutoff requires \(q_*\in I\), not merely \(q_*\in[D,2D)\). Substituting \(b_*=4d^2Xn\ell/s^2\) into (3.1) gives

\[
dJn<s<2dJn\sqrt{\frac a{b_*}}.
\tag{3.3}
\]

The interval is nonempty precisely because \(b_*<4a\). This is scalar support only: a generally nonintegral \(q_*\) cannot be inserted into a discrete owner mask.

**Joint normalization and capacity.** Eliminating \(k\) makes \(\psi_h''\) the Schur complement of the \(kk\)-entry of the Hessian of \(P_{d,n}\). Hence

\[
\det D^2P_{d,n}(u_*,k_*)
=\left(-\frac{2\ell}{k_*}\right)\left(\frac{sd}{2b_*}\right)
=-\frac{\ell sd}{k_*b_*},
\]

and

\[
\mathcal N_{k,u}=\mathcal N_k\mathcal N_u
=\sqrt{\frac{k_*b_*}{\ell sd}}
=\left|\det D^2P_{d,n}\right|^{-1/2}.
\tag{3.4}
\]

The dual-frequency map \((u,k)\mapsto(h,\ell)=\nabla P_{d,n}(u,k)\) has this Hessian determinant as its Jacobian. Equation (3.4) proves the local density identity in Section 1 and shows that the scalar transform creates no \(L^2\)-capacity gain.

The exact discrete scalar-channel capacity available from the packet is only

\[
\begin{aligned}
\mathsf C_{d,g,\nu}^2
&:=\sum_{\substack{u:\,D\le du<2D}}
  \sum_{k\in I_{a,du}\cap\mathbb Z}
  \left|\mathbf1_{\rm own}(a,du)B_{a,du,g}(k)\right|^2\\
&\ll_\varepsilon
X^\varepsilon\frac{AL}{JD}
\left(1+\frac Dd\right)
\left(1+\frac{JD}{A}\right).
\tag{3.5}
\end{aligned}
\]

When both lattice lengths are nondegenerate, (3.5) is \(\ll X^\varepsilon LD/d\). On that scale,

\[
\ell\asymp nA,\qquad
s\asymp dJn,\qquad
\mathcal N_{k,u}\asymp\frac1{dn}\sqrt{\frac DA},\qquad
\sqrt{\frac{AL}{JD}}\mathcal N_{k,u}
\asymp\frac1{dn}\sqrt{\frac LJ}.
\]

The joint stationary dual region has \(\asymp dJD n^2\) cells away from degeneracy. Its square-sum is consequently \(\asymp LD/d\), agreeing with (3.5). Counts, absolute mass, and the weighted \((g,\nu)\)-mass are different quantities; the packet supplies no estimate that permits passage between them.

**The first complete actual-vector inequality.** Let \(\omega=(g,\nu)\), put \(n_\omega=|2\nu-g|\), and set entries to zero unless \(g\in\mathcal G_{a,a+2du}\). Define the literal \(d\)-channel, retaining every mask and maximal cutoff, by

\[
\mathcal Q_{a,d}^{I}
=\sum_{\substack{u\in\mathbb Z:\,du\in I}}
 \mathbf1_{\rm own}(a,du)e(du/2)
 \sum_{\omega}\widehat W_R(\nu)
 \sum_{k\in I_{a,du}\cap\mathbb Z}
 B_{a,du,g}(k)e\!\left(-\frac{n_\omega\Lambda_{du}}{2k}\right).
\tag{3.6}
\]

A lawful transform would produce literal vector amplitudes \(\mathfrak A_{a,d,\omega}^{I}(\ell,s)\), not the scalar samples \(\mathcal N_{k,u}B_{a,q_*,g}(k_*)\), and an exact decomposition

\[
\mathcal Q_{a,d}^{I}
=\sum_{\omega}\widehat W_R(\nu)
  \sum_{(\ell,s)\in\mathscr R_{d,n_\omega}(I)}
  \mathfrak A_{a,d,\omega}^{I}(\ell,s)e(-\delta_{d,n_\omega,\ell,s}^2)
  +\mathfrak E_{a,d}^{I},
\tag{3.7}
\]

where \(\mathfrak A^I\) still contains the centered physical variable, collars, floors, stars, finite lifts, owner masks and complements, and \(\mathfrak E^I\) contains every boundary and nonstationary mode. The logically weakest complete missing inequality is (3.7) together with

\[
\sup_{I\subset[D,2D)}
\left|\sum_{d\mid a}\mu(d)
\left\{
\sum_{\omega}\widehat W_R(\nu)
\sum_{(\ell,s)\in\mathscr R_{d,n_\omega}(I)}
\mathfrak A_{a,d,\omega}^{I}(\ell,s)e(-\delta^2)
+\mathfrak E_{a,d}^{I}
\right\}\right|
\ll_\varepsilon X^\varepsilon\frac{L^2}{A}.
\tag{AV}
\]

This is smaller than the original task only because the scalar carrier, support and Gaussian constants have been settled; all actual-vector content remains in \(\mathfrak A^I\). Define the literal weighted direct-sum capacity by

\[
\bigl(\mathsf C_{a,d}^{\rm act}\bigr)^2
:=\sum_{\omega=(g,\nu)}
\sum_{\substack{u:\,D\le du<2D\\
                 k\in I_{a,du}\cap\mathbb Z}}
\left|
\widehat W_R(\nu)\,
\mathbf1_{g\in\mathcal G_{a,a+2du}}\,
\mathbf1_{\rm own}(a,du)\,
B_{a,du,g}(k)
\right|^2.
\tag{3.8}
\]

A capacity-normalized sufficient version is

\[
\sup_I|\mathcal Q_{a,d}^{I}|
\ll_\varepsilon X^\varepsilon
\frac{L^{3/2}\sqrt d}{A\sqrt D}\,
\mathsf C_{a,d}^{\rm act},
\qquad
\mathsf C_{a,d}^{\rm act}
\ll_\varepsilon X^\varepsilon\sqrt{\frac{LD}{d}}.
\tag{AV-cap}
\]

Summing (AV-cap) over \(d\mid a\) implies the target after absorbing the divisor count into \(X^\varepsilon\). Neither inequality in (AV-cap) follows from the packet: (3.5) is only per scalar channel, while the first demands cancellation specific to the literal physical vector and fixed signs.

## 4. First doubtful or unproved step

The first unproved actual step is replacing the literal \(k\)-sum by

\[
e(-1/8)\mathcal N_k B_{a,du,g}(k_*)
e\!\left(-J(\sqrt b-\sqrt a)\sqrt{n\ell}\right)
\]

with summable uniform error. The fixed-\(q\) bound on \(\sup|B|+\operatorname{Var}_kB\) can support some one-dimensional oscillatory upper bounds, but it does not supply a coherent leading sample, a uniform Gaussian constant across jumps, or an exact extension preserving floors, stars, collars and finite lifts. An order-one phase change of the centered physical integral across \(w_k\) can shift the critical point and Gaussian phase while remaining compatible with an \(O(1)\), rather than \(o(1)\), variation allowance.

Even if the first replacement is granted, the second transform is unsupported more decisively: no \(u\)-variation, mixed variation or Fourier-bandwidth bound is stated for the first transformed physical vector. The centered physical oscillation may translate the \(h\)-support; owner masks may jump at every permitted \(u\); and the sharp maximal cutoff creates \(I\)-dependent endpoint terms. Therefore the scalar conditions \(s>0\), \(b_*=4d^2Xn\ell/s^2\), and phase \(-\delta^2\) cannot be asserted for the actual transformed coefficient without (3.7). Evaluating an owner mask at the generally nonintegral \(q_*\) would be a category error.

## 5. Required control test and outcome

| Control | Exact input and expected invariant/failure | Observed analytic outcome | Implication |
|---|---|---|---|
| raw-vs-weighted | Compare the \(\asymp dJD n^2\) scalar dual-cell count with coefficients carrying \(\widehat W_R(\nu)\), \(B_{a,q,g}\), lift multiplicities and masks. | The raw count gives absolute mass \(\asymp Dn\sqrt{JL}\) per scalar channel at the displayed scale, while its square-sum is only \(\asymp\sqrt{LD/d}\). No bounds on the outer weights or multiplicities are supplied. | No raw-count exponent or capacity statement transfers to \(F_a\). |
| signed-vs-unsigned | Compare literal signs, absolute values, random signs and adversarial phases of the same magnitude. A valid saving must name the literal cancellation. | Absolute values give the raw mass above; random square-root cancellation gives only \(\sqrt{LD/d}\); adversarial phases can remove the carrier oscillation completely. The packet identifies no cancellation of the actual centered vector. | The scalar square is not a signed proof. |
| known-lower-bound-families | Test an unsigned near-collision assertion against UNC, TS and W-1, including parity, support and coefficient lower envelopes. | Those families are named but not defined in an authorized artifact, so this control cannot be executed under statement-only isolation. | No unsigned or near-collision lemma is eligible for promotion here. |
| dyadic-endpoints | Insert \(D=X^{1/4}=J^{1/2}\), \(D=X^{3/8}=J^{3/4}\), and \(D=X^{1/2}=J\) into the capacity. | Capacities are respectively \(L^{1/2}J^{1/4}/\sqrt d\), \(L^{1/2}J^{3/8}/\sqrt d\), and \(L^{1/2}J^{1/2}/\sqrt d\). Required gain factors are \(L^{3/2}\sqrt d/(AJ^{1/4})\), \(L^{3/2}\sqrt d/(AJ^{3/8})\), and \(L^{3/2}\sqrt d/(AJ^{1/2})\). | The transform has no hidden endpoint gain, and nothing permits crossing \(D=J\). |
| real-vs-complex-pairing | Compare this negative orientation with the positive orientation without assuming conjugacy. | Only \(c=-n/2\) was transformed. \(B\) may be genuinely complex and the \(g\)- and \(h\)-weights asymmetric; no conjugacy hypothesis is given. | No \(\operatorname{Re}\)-pairing or doubling shortcut is valid. |
| exact-vs-near-resonance | Separate \(\delta=0\) from \(0<|\delta|\). | By (3.2), \(\delta=0\) forces \(q_*=0\), outside the shell. The smallest nonzero and wider square bands receive no estimate from the algebra. | Absence of an interior exact resonance does not prove near-resonant cancellation. |
| coefficient-adversary | Permit arbitrary same-size coefficients satisfying the stated fixed-\(q\) variation bound. | Whenever the \(k\)-interval contains an integer \(k_q\), take one channel and a coefficient supported at \(k_q\) with phase \((-1)^q e(n\Lambda_q/(2k_q))\), removing the phase of \(\widehat W_R\) as well. Its \(k\)-variation is \(O(\sup|B|)\), but every term of \(\sum_q(-1)^qF_a(q)\) has the same phase. Scaling an unconstrained \(\widehat W_R\) is an even simpler failure. | The maximal theorem is false for the coefficient class described only by the displayed size/variation hypothesis; literal physical structure is indispensable. |
| support-and-degeneracy | Check sharp/smooth boundaries, \(uv=0\), repeated lifts, and collapse at \(b=4a\). | Here \(u,k>0\) at an interior saddle, but as \(b\uparrow4a\), both the \(k\)-interval and \((nb/4,na)\) collapse. Saddles at a \(k\)- or maximal-\(u\) endpoint have one-sided/transition Fresnel factors, not two full Gaussian constants. Repeated-denominator and lift-boundary information remains hidden inside \(B\). | The count \(\asymp dJDn^2\) is only nondegenerate-interior shorthand; all boundary and mask terms must remain in \(\mathfrak E^I\). |

These are analytic controls, not numerical certification. The decisive failure is the coefficient adversary, which shows that the supplied scalar norm is insufficient even before one asks for asymptotics.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read or used:

- problems/gauss_circle.md (background statement only);
- state/control_models.md (the required controls);
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/blind_statement.md (all mathematical data);
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/briefs/blind_dual_square_rederivation.md (scope and output contract only).

No proof graph, proof draft, protocol, strategy file, derivation packet, candidate, claimant report, earlier derivation, sibling report, web source, or external computation was read or used. The statement-only hygiene requirement was satisfied.

## 7. Recommended state effect

**Promote only** the algebraic scalar lemma consisting of the critical points, Hessian signs, Gaussian cancellation, exact support (3.1)--(3.3), square identity (3.2), joint normalization (3.4), and local \(L^2\)-capacity preservation.

**Retain/revise** any proposed actual-symbol transfer until a literal vector construction proves (3.7), including maximal-cutoff endpoint terms and every owner mask, and until an actual weighted capacity estimate plus the saving in (AV-cap) are proved.

**Reject** any inference of the target maximal theorem from the stated bound on \(\sup_k|B|+\operatorname{Var}_kB\) alone. The first unproved step is already the coherent stationary replacement of the actual \(k\)-coefficient, and the missing \(u\)-regularity makes the second transform strictly less justified.
