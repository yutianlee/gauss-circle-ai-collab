## 1. Result

**Post-isolation re-audit, superseding the initial verdict.**  With the
conductor-authorized exact-integral addendum (81.A1)--(81.A3), the complete
transition-flattening lemma (81.12)--(81.14) is proved for every fixed
nonaxial Morse component, all three \(\kappa\)-classes, and both endpoint
orientations.  The complete normalized coefficient has the form

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),\qquad
 \|V\|_\infty+\operatorname{Var}(V)
 \ll_\varepsilon X^\varepsilon,\qquad
 \sup_c|E(c)|
 \ll_\varepsilon X^\varepsilon\Lambda^{-1/2}.
 \tag{R81.1}
\]

The first omitted tangential stationary term and the first
amplitude-variation term in the remaining one-dimensional integral both
obey the required pointwise error.  The exact moving Farey endpoint at
\(z_*=\pm1\) produces a boundary term of size
\(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\), even though its global
variation can have capacity \(\sqrt{J/C}\); it therefore belongs in
\(E\), for which no BV assertion is needed.  The neighbor-independent
principal stationary symbol is \(V\), and (81.A3) gives its global BV
directly across all Farey-neighbor changes.

The countermodel in the initial report is no longer lawful: (81.A1)
states that all neighbor dependence occurs through the exact endpoints,
while (81.A2)--(81.A3) impose a neighbor-independent smooth amplitude
with quantitative seminorms.  An independently alternating
\(\Lambda^{-1/4}\) correction cannot arise under that interface.

The Abel and energy implications (81.17)--(81.20) are correct.  Thus the
proved lemma extends the stated fixed-interior conductor range through
\(C\le J^{13/18}\), without making any claim about cone edges, other
sectors, the full \(M9\!-\!M1\) theorem, or the final Gauss-circle
exponent.

## 2. Exact statement and hypotheses

Fix one endpoint orientation, one retained nonaxial pair
\((\rho,\sigma)\), one class
\(\kappa\in\{1/4,1/2,1\}\), one numerator \(b\), and one admissible
progression \(c=r\pmod{4b}\), with \(c\asymp C\) and
\(\Lambda=J/c\).  Assume exactly (81.A1)--(81.A3): the complete
coefficient is

\[
 \mathcal W(c)=
 \Lambda^{1/2}e(-\Lambda\phi_*)\,
 \Lambda\int_{z_-(c)}^{z_+(c)}
 \iint a_c(z,u,v)e(\Lambda\phi(z,u,v))\,du\,dv\,dz,
 \tag{R81.2}
\]

the amplitude has uniform \(C^M\) seminorms
\(O_\varepsilon(X^\varepsilon)\), its continuous \(c\)-extension has
integrated \(c\)-derivative seminorms
\(O_\varepsilon(X^\varepsilon)\), its \((u,v)\)-support is fixed, and
the stationary support is bounded away from \(z=0\).  The local unit is
constant on the progression, the exact alias is inside \(a_c\), and the
only neighbor-dependent floors or stars are the Farey endpoints.

For one fixed Morse component put

\[
 z_*^2=\kappa\rho\sigma,\qquad
 u_*=\frac{\kappa\sigma}{z_*},\qquad
 v_*=\frac{\rho}{z_*},\qquad
 \epsilon=-\operatorname{sgn}(z_*).
 \tag{R81.3}
\]

Up to the harmless fixed Gaussian and local units allowed in the
addendum, one may take

\[
 V(c)=\frac{a_c(z_*,u_*,v_*)}{\sqrt{2|z_*|}}.
 \tag{R81.4}
\]

The coefficient \(\Gamma_{\epsilon,z_*}\) is the full Gaussian when
\(-1<z_*<1\), the correctly oriented half-Gaussian when \(z_*=\pm1\),
and zero when \(|z_*|>1\).  Formula (R81.1) then holds uniformly over
the fixed finite critical family.  If a row has more than one retained
Morse component, the fixed partition treats them separately; the finite
sum preserves all displayed bounds.

## 3. Proof or derivation

For fixed \(z\ne0\), translate

\[
 p=u-\frac{\kappa\sigma}{z},\qquad
 q=v-\frac{\rho}{z}.
\]

The phase reduces exactly to

\[
 \phi(z,u,v)=\psi(z)+zpq,\qquad
 \psi(z)=-z-\frac{\kappa\rho\sigma}{z}.
 \tag{R81.5}
\]

Thus there is no cubic or higher tangential phase error.  Uniform
two-dimensional stationary phase, using (81.A2) and the fixed compact
support, gives

\[
 \Lambda\iint a_c(z,u,v)e(\Lambda\phi(z,u,v))\,du\,dv
 =
 e(\Lambda\psi(z))
 \left(A_{0,c}(z)+\Lambda^{-1}A_{1,c}(z)
 +O_\varepsilon(X^\varepsilon\Lambda^{-2})\right),
 \tag{R81.6}
\]

on the stationary support, with nonstationary pieces arbitrarily smaller
after integration by parts.  For the convention
\(e(x)=\exp(2\pi i x)\),

\[
 A_{0,c}(z)=
 \frac{a_c\!\left(z,\kappa\sigma/z,\rho/z\right)}{|z|},
 \qquad
 A_{1,c}(z)=
 \frac{i}{2\pi z|z|}
 \,\partial_u\partial_v
 a_c\!\left(z,\kappa\sigma/z,\rho/z\right).
 \tag{R81.7}
\]

A different fixed Gaussian convention only multiplies these expressions
by fixed units.  Equation (R81.7) explicitly identifies the first
omitted tangential stationary term.  Its contribution to (R81.2) is,
without using any outer cancellation,

\[
 \Lambda^{1/2}
 \left|\int_{z_-}^{z_+}
 \Lambda^{-1}A_{1,c}(z)
 e\!\left(\Lambda(\psi(z)-\phi_*)\right)\,dz\right|
 \ll_\varepsilon X^\varepsilon\Lambda^{-1/2},
 \tag{R81.8}
\]

because the \(z\)-interval has bounded length.  The remainder in
(R81.6) contributes
\(O_\varepsilon(X^\varepsilon\Lambda^{-3/2})\).

At a reduced critical point, \(\psi(z_*)=\phi_*\), and

\[
 \psi(z)-\psi(z_*)
 =-\frac{(z-z_*)^2}{z}.
 \tag{R81.9}
\]

On the fixed sign-neighborhood of \(z_*\), introduce the exact,
neighbor-independent Morse coordinate

\[
 t=t(z)=\frac{\sqrt2\,(z-z_*)}{\sqrt{|z|}}.
 \tag{R81.10}
\]

Then

\[
 \psi(z)-\psi(z_*)=\epsilon t^2/2,\qquad
 \left.\frac{dz}{dt}\right|_{t=0}
 =\sqrt{\frac{|z_*|}{2}}.
 \tag{R81.11}
\]

The principal part of (R81.2) is therefore, on that Morse component,

\[
 \sqrt\Lambda\int_{\alpha(c)}^{\beta(c)}
 g_c(t)e(\epsilon\Lambda t^2/2)\,dt,\qquad
 g_c(t)=A_{0,c}(z(t))\frac{dz}{dt}.
 \tag{R81.12}
\]

Here the endpoint lying near a boundary saddle is retained exactly as
\(\alpha(c)\) or \(\beta(c)\); a remote fixed partition endpoint may be
replaced by the corresponding infinite Gaussian tail at a cost
\(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\).
Since

\[
 g_c(t)=g_c(0)+t h_c(t),\qquad
 g_c(0)=\frac{a_c(z_*,u_*,v_*)}{\sqrt{2|z_*|}}=V(c),
 \tag{R81.13}
\]

the constant term is \(V(c)\) times the exact incomplete Gaussian.
The first omitted outer amplitude term has the exact integration-by-parts
identity

\[
\begin{aligned}
 \sqrt\Lambda\int_{\alpha(c)}^{\beta(c)}
 t h_c(t)e(\epsilon\Lambda t^2/2)\,dt
 =\frac{1}{2\pi i\epsilon\sqrt\Lambda}
 \Bigg(
 &\left[h_c(t)e(\epsilon\Lambda t^2/2)\right]_{\alpha(c)}^{\beta(c)}
 \\
 &-\int_{\alpha(c)}^{\beta(c)}
 h_c'(t)e(\epsilon\Lambda t^2/2)\,dt
 \Bigg).
 \tag{R81.14}
\end{aligned}
\]

The \(C^M\) bounds in (81.A2) make (R81.14)
\(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\), uniformly even when an
endpoint moves through a boundary saddle.  This is the full first
omitted stationary contribution, including its moving-boundary value;
no endpoint BV is used.

It remains to compare the exact incomplete Gaussian with its limiting
coefficient.  Write \(R=\lfloor J\rfloor\),
\(\theta=J-R\in[0,1)\), and
\(\delta_\pm=c+c_\pm-R\).  The Farey inequalities give
\(1\le\delta_\pm\le c\), and the \(J\)-normalized endpoints satisfy

\[
 z_+-1=-\frac{\delta_+-\theta}{R+\delta_+},\qquad
 z_-+1=\frac{\delta_--\theta}{R+\delta_-}.
 \tag{R81.15}
\]

Hence each endpoint differs from its limiting value \(\pm1\) by
\(O(c/J)=O(\Lambda^{-1})\).  At \(z_*=1\),

\[
 \sqrt\Lambda\,|t(z_+)|
 \ll \sqrt\Lambda\,|z_+-1|
 \ll\Lambda^{-1/2},
 \tag{R81.16}
\]

while the other endpoint or fixed partition boundary is at standardized
distance \(\gg\sqrt\Lambda\).  The integral between
\(\sqrt\Lambda\,t(z_+)\) and \(0\) is
\(O(\Lambda^{-1/2})\), and (81.15) bounds the remote tail by the same
quantity.  Thus the exact integral differs from the oriented
half-Gaussian by \(O(\Lambda^{-1/2})\).  The case \(z_*=-1\) is the
endpoint-reversed conjugate argument.

For \(-1<z_*<1\), finiteness of the critical family gives fixed
separation from both limiting endpoints, so both Gaussian tails are
\(O(\Lambda^{-1/2})\) and the limit is the full coefficient.  For
\(|z_*|>1\), the reduced derivative

\[
 \psi'(z)=-1+\frac{\kappa\rho\sigma}{z^2}
 \tag{R81.17}
\]

is bounded away from zero throughout the Farey interval, after the fixed
partition.  One integration by parts in \(z\) makes the normalized
coefficient \(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\), so
\(\Gamma=0\).  This proves the full inside/boundary/outside trichotomy.

Replacing \(R\) by \(J\) in an endpoint changes it by \(O(J^{-1})\);
after Morse scaling the change is

\[
 O\!\left(\sqrt{J/c}\,J^{-1}\right)
 =O((Jc)^{-1/2})
 \le O(\Lambda^{-1/2}),
 \tag{R81.18}
\]

so the normalization choice is harmless at the required scale.

The hostile sawtooth is also exact but pointwise small.  In the class
\(4\mid c\), \(\kappa=1\), \(\rho=\sigma=1\), one has \(z_*=1\).
A jump \(\Delta c_+\asymp C\) changes the standardized boundary by
\(\asymp\sqrt{C/J}=\Lambda^{-1/2}\).  Across
\(\asymp J/C\) changes its possible total variation is
\(\asymp\sqrt{J/C}\).  Equations (R81.14) and (R81.16) place every such
neighbor-dependent term in \(E\) pointwise.  In contrast, (81.A1) says
that \(a_c\), and hence \(V(c)\), is neighbor-independent.  From
(81.A2)--(81.A3),

\[
 \|V\|_\infty\ll_\varepsilon X^\varepsilon,\qquad
 \operatorname{Var}_{c=r\;(\mathrm{mod}\;4b)}V
 \le
 \int_C^{2C}|V'(c)|\,dc
 \ll_\varepsilon X^\varepsilon.
 \tag{R81.19}
\]

Restriction to admissible samples, singleton pieces, or simultaneous
neighbor changes cannot increase the variation of this continuous
principal symbol.  Combining (R81.8), (R81.14), the endpoint tails, and
the nonstationary remainders proves (R81.1).

For completeness, Abel summation now applies (81.16) once to the whole
half-open progression, using its proper-subinterval supremum.  There are
\(O(B)\) residue progressions, and \(BT\asymp C\), so

\[
 |S_b^{\mathrm{main}}|
 \ll_\varepsilon X^\varepsilon C Q^{-5/24}.
 \tag{R81.20}
\]

Triangle summation of \(E(c)\) over \(O(C)\) moduli gives

\[
 |S_b^{\mathrm{err}}|
 \ll_\varepsilon X^\varepsilon C\sqrt{C/J}.
 \tag{R81.21}
\]

With \(B\asymp C/T\), squaring and using
\((x+y)^2\le2x^2+2y^2\) gives

\[
 \sum_{b\asymp C/T}|S_b|^2
 \ll_\varepsilon X^\varepsilon
 \left(\frac{C^3}{TQ^{5/12}}+\frac{C^4}{TJ}\right).
 \tag{R81.22}
\]

Since \(Q=J^{2/5}\), the first term is at most \(J^2/T\) exactly for
\(C^3\le J^{13/6}\), or \(C\le J^{13/18}\); the second is target-safe
for \(C\le J^{3/4}\).  Thus the claimed range \(C\le J^{13/18}\) is
correct.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the transition-flattening lemma
under (81.A1)--(81.A3).  The earliest non-derived ingredient in the
downstream implication is the full-progression reciprocal exponent-pair
estimate (81.16): the original packet declares its source range and
proper-subinterval uniformity already audited, but the permitted
artifacts do not contain that source proof.  The Abel and energy
deductions from (81.16) are verified above.

Likewise, (81.A1) is a conductor-authorized exact identity rather than
something rederived in this blind report.  The proof here audits all
stationary and moving-boundary consequences of that identity and the
seminorm hypotheses, but does not independently reconstruct the finite
Farey identity from excluded source material.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| Farey determinant signs, half-open endpoints, and both aliases | Passed.  The determinant inequalities give (R81.15).  Both endpoint orientations use the same proof with signs reversed.  The exact aliases lie inside the neighbor-independent amplitude and obey (81.A2)--(81.A3). |
| \(R=\lfloor J\rfloor\) versus \(J\) | Passed by (R81.18). |
| Three \(\kappa\)-classes, units, gcd restrictions, and axes | Passed for every fixed nonaxial class because the finite stationary support is away from \(z=0\).  The local unit is constant on each admissible progression, and restriction to gcd-admissible samples cannot increase principal-symbol variation.  The two axes are excluded from (81.A1) and retain the separately accepted \(O_\varepsilon(X^\varepsilon C^2/J)\) bound. |
| Finite critical family and endpoint trichotomy | Passed using (R81.15)--(R81.17) and the finite-set separation. |
| Full stationary remainder and moving symbols | Passed.  The first tangential correction is (R81.7)--(R81.8); the first outer correction, with the exact moving endpoint, is (R81.14).  Higher terms are smaller by (81.A2). |
| Hostile sawtooth, singleton pieces, and simultaneous changes | Passed.  Its possible BV is \(\sqrt{J/C}\), but every neighbor-dependent contribution is pointwise \(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\) and is assigned to \(E\); \(V\) is globally BV by (R81.19). |
| Full-progression range and proper-subinterval uniformity in (81.16) | The packet supplies this as an audited input.  Proper-subinterval uniformity is used exactly once in Abel summation, with no multiplication by the number of Farey pieces. |
| Energy arithmetic | Passed in (R81.20)--(R81.22), including the square cross term and both threshold exponents. |
| Perfect squares, fourth powers, and phase-conjugating coefficients | Passed at this interface.  They only select members or conjugates of the fixed finite critical family.  The determinant in (R81.7) is nonzero for every retained nonaxial saddle; conjugation preserves all size and BV estimates, and a vanishing coefficient only removes a row. |
| Floors, stars, cone-edge exclusions, and downstream scope | Passed.  Floors and half-open stars occur only in the exact endpoints and are covered pointwise by \(E\).  Cone edges and all global downstream claims remain excluded. |

## 6. Dependencies and exact artifacts or sources used

Only the following three artifacts were used:

1. rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet.md
2. rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/briefs/blind_transition_flattening_rederivation.md
3. rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet_actual_integral_addendum.md

No proof graph, strategy file, prior-round report, sibling report, source
card, web source, or external computation was read or used.

## 7. Recommended state effect

**Promote.**  Promote the complete transition-flattening lemma
(81.12)--(81.14), with (81.A1)--(81.A3) recorded as its exact hypotheses,
and promote the conditional conductor extension through
\(C\le J^{13/18}\).  Preserve the separation between the global-BV
principal symbol \(V\) and the pointwise-only endpoint/stationary error
\(E\); no global BV assertion for the transition error is justified or
needed.  Do not infer any theorem beyond the conductor range and
downstream scope stated in the packet.
