## 1. Result

The exact Farey representative at order \(J\), followed by the complete
two-variable residue Poisson formula, has a uniform three-variable
stationary normalization which was not visible in the schematic
Round-70 family.  This statement includes the two offset-Poisson aliases,
the neighbor-dependent sharp Farey interval, all three local parity
classes, and the axial modes.  On a dyadic conductor block
\(c\asymp C\), every nonaxial stationary coefficient has size

\[
 \frac{T}{\sqrt{CJ}}(\rho\sigma)^{-1/4}
\]

up to fixed smooth symbols and \(X^\varepsilon\) divisor losses.  There
are \(O(C)\) moduli, \(O(C/T)\) endpoint numerators, and only a fixed
power-divisor family of stationary \((\rho,\sigma)\).  Consequently

\[
 \mathcal D_C^{\rm stat}
 \ll_\varepsilon
 X^\varepsilon\frac{C^{3/2}}{\sqrt J}.              \tag{71.C1}
\]

The same uniform incomplete-stationary estimate covers saddle
entry/exit, with the actual neighbor-dependent incomplete-Fresnel factor
retained.  Axial and nonstationary cells have no interior critical point;
a summed dual-tail lemma makes them smaller by integration by parts when
\(J/C\) is large.
Hence every fixed-interior conductor block

\[
 T\leq C\leq J^{2/3}                              \tag{71.C2}
\]

is target-safe:

\[
 \mathcal D_C\ll_\varepsilon J^{1/2}X^\varepsilon. \tag{71.C3}
\]

For odd \(c\), reciprocity makes the interior-saddle leading phase
explicit:

\[
 e_{4b}(\rho\sigma\bar c)\,
 e\!\left(
 -\frac{\left(\sqrt{bX}+
          \sqrt{\rho\sigma}/(2\sqrt b)\right)^2}{c}
 \right),                                         \tag{71.C4}
\]

up to the orientation, fixed Gaussian/local units, and the exact
stationary symbol.  At a Farey edge the same phase is multiplied by the
corresponding incomplete-Fresnel transition.  Thus the remaining
upper-conductor range \(J^{2/3}<C\leq J\) is a
linear-plus-inverse reciprocal-square sum, not an inverse-only
Kloosterman fraction.  No target bound for that range is proved here.

## 2. Exact statement and hypotheses

Let \(J=\sqrt X\), \(T=J/Q\), \(Q=X^{1/5}\), and let
\(\Omega(m/J,n/J)\) be one fixed smooth interior one-sided ratio
symbol.  Decompose \(K\) into its two fixed Fourier components so that
\(\widehat K\) is smooth, compactly supported, and separated from zero
on each sign.  The formulas below retain both components; either one
may instead be read separately with the corresponding orientation.

Take the exact Farey partition \(\{I_{a/c}\}\) of order
\(R=\lfloor J\rfloor\), with mediant boundaries.  If
\(\beta=\alpha-a/c\), then

\[
 -\frac1{c(c+c_-)}
 \leq\beta<
 \frac1{c(c+c_+)},
 \qquad c+c_\pm>J,                               \tag{71.C5}
\]

and therefore \(|\beta|\ll(cJ)^{-1}\).

Put \(N=\lfloor X\rfloor\), \(\vartheta=X-N\), and define the exact
periodized offset-Poisson multiplier

\[
 \mathscr G_T(\alpha;\vartheta)
 =\sum_{\ell\in\mathbb Z}
 e\!\left(-\vartheta(\ell+\alpha)\right)
 \widehat K\!\left(T(\ell+\alpha)\right).          \tag{71.C5a}
\]

Then

\[
 K\!\left(\frac{mn-X}{T}\right)
 =T\int_0^1 e\!\left(\alpha(mn-N)\right)
 \mathscr G_T(\alpha;\vartheta)\,d\alpha.          \tag{71.C5b}
\]

Because \(\widehat K\) is compactly supported away from zero, only the
two aliases \(\ell=0,-1\) occur for large \(T\).  They give the positive
and negative endpoint orientations, and (71.C5a)--(71.C5b) retain the
real center exactly before either is unfolded.

For \(L_c=[c,4]\), put

\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =
 \sum_{r\bmod c}\sum_{s\bmod L_c}
 \chi_4(s)e_c(ars+\rho r)e_{L_c}(\sigma s),       \tag{71.C6}
\]

and

\[
 \mathcal I_{\beta,c}(\rho,\sigma)
 =
 \iint_{\mathbb R^2}
 \Omega(x/J,y/J)
 e\!\left(\beta xy-\frac{\rho x}{c}
                   -\frac{\sigma y}{L_c}\right)dx\,dy.           \tag{71.C7}
\]

The exact conductor block is

\[
\begin{aligned}
 \mathcal D_C
 =T\sum_{a/c\in\mathfrak F_J}V_C(c)
 \int_{I_{a/c}-a/c}
 &e\!\left(-N\left(\frac ac+\beta\right)\right)
 \mathscr G_T\!\left(\frac ac+\beta;\vartheta\right)\\
 &\times\frac1{cL_c}
 \sum_{\rho,\sigma}
 \mathfrak C_{c,a}(\rho,\sigma)
 \mathcal I_{\beta,c}(\rho,\sigma)\,d\beta .       \tag{71.C8}
\end{aligned}
\]

Equation (71.C8) is exact and coefficient-preserving.  On the
\(\ell=0\) alias, its first line is
\(e(-X(a/c+\beta))\widehat K(T(a/c+\beta))\); on \(\ell=-1\), the
analogous oriented local coordinate gives the same real center.  The
star/end convention is the inherited Farey half-open convention; a
stationary point at an endpoint receives the corresponding
neighbor-dependent incomplete-Fresnel value, not a new arithmetic
half-weight.

## 3. Proof or derivation

The signed offset Poisson identity localizes
\(\alpha\) to \(\|\alpha\|\asymp T^{-1}\).  On the positive endpoint
write \(a=b\), with

\[
 b\asymp c/T,\qquad (b,c)=1,\qquad T\ll c\leq J.  \tag{71.C9}
\]

The negative endpoint is identical after \(b\mapsto-b\).
Two-dimensional Poisson summation in residue classes gives (71.C8).
For odd \(c\),

\[
 \mathfrak C_{c,b}(\rho,\sigma)
 =
 2ic\,\chi_4(c\sigma)
 e_c(\lambda_c\rho\sigma\bar b),
 \quad \sigma\ \mathrm{odd},\qquad
 \lambda_c=(c^2-1)/4.                            \tag{71.C10}
\]

For the two even classes, put
\(s_0\equiv-\rho\bar b\pmod c\).  Directly summing the remaining
\(L_c/c\) residue classes gives

\[
 \mathfrak C_{c,b}(\rho,\sigma)
 =
 \begin{cases}
  2c\,\chi_4(s_0)e_{2c}(\sigma s_0),
    &c\equiv2\pmod4,\quad \rho,\sigma\ \mathrm{odd},\\
  c\,\chi_4(s_0)e_c(\sigma s_0),
    &4\mid c,\quad \rho\ \mathrm{odd},\\
  0,&\text{otherwise.}
 \end{cases}                                      \tag{71.C10a}
\]

Thus the normalized local prefactor after multiplication by
\((cL_c)^{-1}\) is \(i\chi_4(c\sigma)/(2c)\) in the odd class and
\(1/c\) times the displayed local unit in either even class.  The only
axes are

\[
 \begin{array}{ll}
 c\ \mathrm{odd}:&\rho=0,\quad\sigma\ \mathrm{odd},\\
 4\mid c:&\rho\ \mathrm{odd},\quad\sigma=0.
 \end{array}                                      \tag{71.C10b}
\]

There is no axis for \(c\equiv2\pmod4\), and the double zero vanishes
in all classes.  In particular every nonzero local factor has size
\(O(c)\), but no parity or axial term has been suppressed.

Scale

\[
 x=Ju,\quad y=Jv,\quad \tau=\beta J^2,\quad
 R_\rho=\frac{J\rho}{c},\quad
 S_\sigma=\frac{J\sigma}{L_c}.
\]

The factors \(J^2\) from \(dx\,dy\) and \(J^{-2}\) from \(d\beta\)
cancel.  Including \(e(-X\beta)\), and using \(X=J^2\), the phase is

\[
 \Phi(\tau,u,v)
 =
 \tau(uv-1)-R_\rho u-S_\sigma v.                 \tag{71.C11}
\]

Put \(\Lambda=J/c\) and \(\kappa_c=c/L_c\in\{1/4,1/2,1\}\).  If
\(\tau=\Lambda z\), the exact sharp interval is

\[
 -\frac{J}{c+c_-}\leq z<\frac{J}{c+c_+}.          \tag{71.C11a}
\]

Both endpoints lie in \([-1,-1/2]\cup[1/2,1]\) in absolute value.
The exact scaled phase is

\[
 \phi_{\rho,\sigma}(z,u,v)
 =z(uv-1)-\rho u-\kappa_c\sigma v,
 \qquad \Phi=\Lambda\phi_{\rho,\sigma}.          \tag{71.C11b}
\]

The amplitude retains \(V_C(c)\), the appropriate alias of
\(\mathscr G_T\), the ratio symbol, and the half-open endpoints in
(71.C11a).  Its smooth derivatives away from the sharp \(z\)-faces are
uniform: differentiating the alias in \(z\) costs at most
\(T/(cJ)\ll J^{-1}\).

The factors \(R_\rho,S_\sigma\) are \(\Lambda\) times fixed integer
ratios.
An interior critical point exists only for compatible nonzero
\(\rho,\sigma\), and then

\[
 uv=1,\qquad \tau v=R_\rho,\qquad \tau u=S_\sigma.               \tag{71.C12}
\]

For odd \(c\), this gives

\[
 u_*=\frac12\sqrt{\frac{\sigma}{\rho}},\quad
 v_*=2\sqrt{\frac{\rho}{\sigma}},\quad
 \tau_*=\frac{J}{2c}\sqrt{\rho\sigma},\quad
 \Phi_*=-\frac{J}{c}\sqrt{\rho\sigma}.            \tag{71.C13}
\]

The ratio support and (71.C5) restrict \((\rho,\sigma)\) to a fixed
finite set.  Indeed, on the compact \((z,u,v)\)-box the two equations
\(zv=\rho\), \(zu=\kappa_c\sigma\) force
\(|\rho|+|\sigma|\ll1\).  The
Hessian in \((\tau,u,v)\) is

\[
 \begin{pmatrix}
 0&v&u\\
 v&0&\tau\\
 u&\tau&0
 \end{pmatrix},
 \qquad
 \det=2\tau uv\asymp
 \frac{J}{c}\sqrt{\rho\sigma}.                    \tag{71.C14}
\]

Uniform three-variable stationary phase, including an incomplete
interval in \(\tau\), therefore gives

\[
 \int\!\!\iint e(\Phi)\,A\,du\,dv\,d\tau
 \ll_A
 \left(\frac cJ\right)^{1/2}
 (\rho\sigma)^{-1/4},                             \tag{71.C15}
\]

with the same bound at entry and exit.  In local Morse coordinates the
leading symbol contains the bounded incomplete-Gaussian factor

\[
 \mathfrak F\!\left(
   \sqrt\Lambda\,(z_+-z_*),
   \sqrt\Lambda\,(z_*-z_-)
 \right),                                        \tag{71.C15c}
\]

where \(z_\pm=\pm J/(c+c_\pm)\) with the signs in (71.C11a).
Formula (71.C15c), rather than a universal half-weight, is retained in
the upper-conductor stationary symbol; its uniform boundedness is all
that is used in the low-conductor estimate.  If a critical point is absent,
the fixed compact support gives the same bound, and usually arbitrary
powers of \(c/J\), by integration by parts in \(u\) or \(v\).  This is
uniform at the sharp \(z\)-faces because no integration by parts in
\(z\) is needed.  More explicitly, once
\(|\rho|+|\sigma|>M_0\), compactness gives

\[
 \max\{|\partial_u\phi|,|\partial_v\phi|\}
 \gg 1+|\rho|+|\sigma|,
\]

and \(A\) integrations by parts yield, after the outer
\(d\tau=\Lambda\,dz\) measure,

\[
 \mathcal J_{\rho,\sigma}
 \ll_A
 \Lambda^{1-A}(1+|\rho|+|\sigma|)^{-A}.           \tag{71.C15a}
\]

This is summable for fixed large \(A\).  The remaining finite family is
covered by ordinary or incomplete stationary phase.  The axes in
(71.C10b) cannot satisfy all three stationary equations.  For example,
on the odd axis \(\rho=0\), either
\(|z|\leq\kappa_c|\sigma|/(2u_1)\), when
\(|\partial_v\phi|\geq\kappa_c|\sigma|/2\), or the complementary
region has \(|\partial_u\phi|=|zv|\gg|\sigma|\); the
\(4\mid c\), \(\sigma=0\) axis is symmetric.  A two-piece smooth
partition therefore gives (71.C15a) for both axes.  Hence the complete
dual sum, including both axes and every transition face, is

\[
 \sum_{\rho,\sigma}|\mathcal J_{\rho,\sigma}|
 \ll \Lambda^{-1/2},                              \tag{71.C15b}
\]

with the local parity restrictions imposed before summation.

Combining the exact outer local factors from (71.C10)--(71.C10a) with
(71.C15b) gives \(T/\sqrt{cJ}\) per admissible incidence, up to the
fixed factor \(1/2\) in the odd class.  Counting
\(c\asymp C\), \(b\asymp C/T\), and the divisor-bounded dual family
proves (71.C1).  The inequality

\[
 C^{3/2}/\sqrt J\leq\sqrt J
\]

is equivalent to \(C\leq J^{2/3}\), proving (71.C2)--(71.C3).

Finally, for odd \(c\),

\[
 e_c(\lambda_c\rho\sigma\bar b)
 =
 e_{4b}(\rho\sigma\bar c)
 e\!\left(-\frac{\rho\sigma}{4bc}\right).         \tag{71.C16}
\]

The real-centre factor, the stationary phase in (71.C13), and the last
factor in (71.C16) combine exactly as

\[
 -\frac{bX}{c}
 -\frac{\sqrt{X\rho\sigma}}{c}
 -\frac{\rho\sigma}{4bc}
 =
 -\frac{\left(\sqrt{bX}+
        \sqrt{\rho\sigma}/(2\sqrt b)\right)^2}{c},
\]

which proves (71.C4).

## 4. First doubtful or unproved step

The first unproved estimate is the upper-conductor sum
\(J^{2/3}<C\leq J\) with the complete leading symbol and phase
(71.C4), together with both even-modulus analogues.  Its raw stationary
capacity is \(C^{3/2}/\sqrt J\), so it needs the gain
\(C^{3/2}/J\) to reach \(J^{1/2}\).  At \(C=J\) this is a square-root
gain in the conductor family.

An inverse-only incomplete Kloosterman theorem does not automatically
apply: (71.C4) contains the high-conductor reciprocal-square factor,
its coefficient couples \(b,c,\rho,\sigma\), and the even classes live
at level \(4\).  A second B-process in \(c\) is also not declared a
saving; its stationary map must be checked for a return to the original
near-product wavelet.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Exact common antecedent | Pass: (71.C8) is the finite Farey identity before estimates. |
| Natural/conductor cutoff | Pass: order \(Q\) is the zero-cell return; order \(J\) gives (71.C5). |
| Real centre | Pass: \(N+\vartheta=X\) is kept in (71.C8) and (71.C4). |
| Character and local factors | Pass for the absolute low-\(C\) bound; odd phase is explicit and even classes retain level \(4\). |
| Dual lengths | Pass: the Farey width and stationary equations force a fixed divisor-bounded \((\rho,\sigma)\) family. |
| Axial modes | Pass in the fixed interior: no axial triple critical point; nonstationary integration is retained. |
| Stationary entry/exit | Pass: incomplete three-variable stationary phase has the same \(\Lambda^{-1/2}\) bound. |
| Low-conductor power | Pass: \(C^{3/2}/\sqrt J\leq\sqrt J\) exactly for \(C\leq J^{2/3}\). |
| Perfect powers | No special estimate is used; exact products remain divisor-bounded. |
| Upper conductor | Open: (71.C4) requires new signed cancellation. |
| Downstream scope | Pass: no cone-edge, GAR, \(M9\)-\(M1\), \(M9\), or final exponent is claimed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The derivation uses:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- the Round-71 derivation packet;
- the accepted Round-70 exact Farey partition, residue formulas, and
  real-centre convention.

The calculation was first obtained without a sibling Round-71 report.
The final exact-seam revision was then checked against the completed
post-isolation addendum in
`reports/blind_short_numerator_large_sieve.md` and the independent
source/hostile audit in
`reports/short_numerator_source_hostile_audit.md`; both certify the
stationary factor and identify the alias, Farey-edge, tail, axial, and
even-class details now written explicitly above.  No external theorem is
imported into the low-conductor estimate.
The stationary estimate is the standard compact-support
nondegenerate stationary-phase lemma applied after the explicit scaling
in (71.C11)--(71.C15).

## 7. Recommended state effect

Promote the exact Farey
stationary normalization and the target-safe low-conductor range
\(T\leq C\leq J^{2/3}\).  Revise the open short-numerator target to the
upper conductors \(J^{2/3}<C\leq J\), with phase (71.C4), both
even-modulus analogues, and the exact stationary symbol retained.

Do not promote the full fixed-interior wavelet, global angular-radial
estimate, \(M9\)-\(M1\), \(M9\), or the Gauss-circle exponent.
