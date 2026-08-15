## 1. Result

**Exact reduction and capacity no-go lemma.**  The alpha-bounded trace has an exact common-antecedent representation as a radial integral of a connector-completed, masked Mellin convolution of the Abel cosine comb.  No residue is crossed if the \(A\)-line is moved only to a fixed \(\delta\in(1/4,1)\).  On that line the unsigned high series becomes

\[
 C_r(Y)=2\sum_{h\geq 1}r^h\cos(2\pi hY),\qquad 0<r<1,
\]

convolved in the multiplicative variable with the alpha mask, \(L(1-B,\chi _4)\), and the Cauchy factor \(1/\rho\).  At every integer \(Y\),

\[
 C_r(Y)=\frac{2r}{1-r}.
\]

Consequently, neither coefficientwise cancellation nor an absolute estimate of the shifted pieces can be uniform as \(r\uparrow1\).  Radial integration does not repair this coefficient by coefficient: after the convolution variable is denoted by \(t\), the minus phase has an interior stationary point

\[
 \phi^-_{h,t}(x)=\sqrt{Xx}-\frac{hx}{t},\qquad
 x_{h,t}=\frac{Xt^2}{4h^2},\qquad
 \phi^-_{h,t}(x_{h,t})=\frac{Xt}{4h}.
\]

Thus the first unproved assertion is a uniform **connector-completed radial cosine--Cauchy estimate** for the whole signed operator, including its strip connectors and finite outside faces.  Its required height gain is exactly the loss

\[
 U^{-\gamma},\qquad
 \gamma=c'-\frac12-\frac{a+b}{2}>\frac12,
\]

relative to the known absolute capacity \(U^\gamma\).  Its unresolved normalized \(X\)-capacity is \(X^0\) (with \(X^\varepsilon\) allowed), or \(X^{1/4}\) after the single external physical factor.  The packet supplies no theorem implying this coupled estimate.  Hence the target bound is not proved, but the first missing kernel and two exact falsifiers of simpler routes are isolated.

## 2. Exact statement and hypotheses

Put

\[
 \sigma=c'-\frac{a+b}{2}>1,\qquad
 C=C(u,v)=\frac14-\frac u2-v,\qquad
 \tau=\operatorname {Im}(u+v).
\]

For \(A=s-(u+v)/2\), the upward \(s\)-segment becomes

\[
 I_{\sigma,z}^S=
 \{\sigma+i\beta:\ \beta_-\leq\beta\leq\beta_+\},
 \qquad \beta_\pm=\pm S-\frac{\tau}{2},
\]

and \(B=A+z\), so the mask is

\[
 \Theta_\alpha=\Theta(\operatorname {Im}(A+z))
 =\Theta(\beta+\tau).
\]

Assume only that the fixed transition mask is either compactly supported and piecewise \(C^1\), or is the indicator of a bounded interval; all finite contour integrals with the packet's actual profiles are assumed to exist.  Introduce one common Abel parameter \(0<r<1\),

\[
 Z_r(A)=\sum_{h\geq1}r^h h^{-A}=\operatorname {Li}_A(r).
\]

This is a proof regularization, not a new arithmetic term.  At each fixed finite \(U,V,S\), its limit on the original line is the trace in the packet because \(\sigma>1\).

For any fixed \(\delta\in(1/4,1)\), define

\[
 G_r(A;x,z,C)=
 \frac{X_\zeta(A)L(1-A-z,\chi _4)Z_r(A)x^{-A}}{C-A}.
\]

The exact finite alpha kernel is

\[
 \mathcal K_{\sigma,r}^S(x;u,v)
 =\frac1{2\pi i}\int_{I_{\sigma,z}^S}
 \Theta(\operatorname {Im}(A+z))G_r(A;x,z,C)\,dA.
\tag{2.1}
\]

Let \(\mathcal R_z=[\delta,\sigma]\times[\beta_-,\beta_+]\) in the \(A\)-plane.  Then

\[
 \boxed{\mathcal K_{\sigma,r}^S
 =\mathcal K_{\delta,r}^S
  +\mathcal C_{\Theta,r}^S
  +\mathcal E_{s,r}^S,}
\tag{2.2}
\]

where all vertical segments are upward and

\[
 \begin{aligned}
 \mathcal K_{\delta,r}^S
 &=\frac1{2\pi i}\int_{\delta+i\beta_-}^{\delta+i\beta_+}
   \Theta(\operatorname {Im}(A+z))G_r(A)\,dA,\\
 \mathcal E_{s,r}^S
 &=\frac1{2\pi i}\int_\delta^\sigma
 \bigl[\Theta(\beta_++\tau)G_r(\xi+i\beta_+)
       -\Theta(\beta_-+\tau)G_r(\xi+i\beta_-)\bigr]\,d\xi,\\
 \mathcal C_{\Theta,r}^S
 &=\frac1\pi\iint_{\mathcal R_z}
 \partial_{\bar A}\Theta(\operatorname {Im}(A+z))G_r(A)
 \,d(\operatorname {Re}A)\,d(\operatorname {Im}A).
 \end{aligned}
\tag{2.3}
\]

For a sharp mask \({\bf1}_{[\alpha_-,\alpha_+]}\), the last line is interpreted distributionally and is exactly the two oppositely oriented strip edges

\[
 \frac{i}{2\pi}\int_\delta^\sigma
 \left[G_r\bigl(\xi+i(\alpha_--\tau)\bigr)
       -G_r\bigl(\xi+i(\alpha_+-\tau)\bigr)\right]d\xi,
\tag{2.4}
\]

with an edge included only when its height lies in \([\beta_-,\beta_+]\).  Formula (2.2), and not any one of its terms, is the connector-completed kernel.

The missing estimate can now be stated without ambiguity.  Substitute (2.2) into the radial operator in (3.2) below, add every \(u\)- and \(v\)-face produced from that same \(r,U,V,S\) antecedent, take the physical real part before any estimate, then take \(r\uparrow1\) at fixed finite heights and finally a symmetric cofinal exhaustion with \(S>(U+V)/2\).  One needs

\[
 \left|\mathfrak T_{\zeta,\mathrm{cc}}(X)\right|
 \ll_\varepsilon X^\varepsilon
\tag{2.5}
\]

and a uniform Cauchy-tail version of (2.5) that makes the outside-height limit exist.  No claim about a separated line, connector, face, coefficient, or radial saddle is sufficient.

## 3. Proof or derivation

The map \(s\mapsto A=s-z/2\) has Jacobian \(ds=dA\) and preserves upward orientation.  Also

\[
 B=A+z,\qquad
 \rho=\frac14-s-\frac v2
 =\frac14-A-\frac u2-v=C-A,
\]

and hence

\[
 x^{\rho-1/2}=x^{-1/4-u/2-v}x^{-A}.
\]

After inserting the given radial remainder and summing the common Abel-regularized high series, the exact finite trace is

\[
 \begin{aligned}
 \mathfrak T_{\zeta,r}^{U,V,S}
 ={}&-\pi i\sqrt X\sum_j\frac1{(2\pi i)^2}
 \int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}
 \mathcal A_j(u,v)\\
 &\quad\times\int_1^{N_X}
 x^{-1/4-u/2-v}e(\sqrt{Xx})
 \mathcal K_{\sigma,r}^S(x;u,v)\,dx\,dv\,du.
 \end{aligned}
\tag{3.1}
\]

Thus the connector-completed physical expression is

\[
 \boxed{
 -\frac4\pi X^{1/4}\operatorname {Re}\!\left\{
 e(1/8)\,[-\pi i\sqrt X]
 \sum_j\frac1{(2\pi i)^2}\int_u\int_v\mathcal A_j
 \int_1^{N_X}x^{-1/4-u/2-v}e(\sqrt{Xx})
 (\mathcal K_{\delta,r}^S+\mathcal C_{\Theta,r}^S+
 \mathcal E_{s,r}^S)\,dx\,dv\,du
 \right\}.}
\tag{3.2}
\]

The floors, stars, scale set, one-sided top profile, and interior profiles stay inside \(\mathcal A_j\); (3.2) neither smooths nor replaces them.  The displayed \(X^{1/4}\) is the unique external physical factor.

To prove (2.2), apply Cauchy--Pompeiu to
\(\Theta(\operatorname {Im}(A+z))G_r(A)\) on \(\mathcal R_z\).
The counterclockwise boundary consists of the bottom edge from \(\delta\)
to \(\sigma\), the original right edge upward, the top edge from
\(\sigma\) to \(\delta\), and the left edge downward.  Solving the boundary
identity for the right upward edge gives exactly the signs in (2.3).
For a sharp interval,

\[
 \partial_{\bar A}\Theta
 =\frac i2\left[
 \delta_{\operatorname {Im}A=\alpha_--\tau}
 -\delta_{\operatorname {Im}A=\alpha_+-\tau}
 \right],
\]

which gives (2.4).  Thus dropping either strip edge changes the operator.

There are no hidden residues in this displacement.  Indeed,
\(\operatorname {Re}C=1/4-a/2-b<1/4<\delta\), so the artificial pole
\(A=C\) lies to the left.  The arithmetic pole \(A=0\) also lies to the
left.  The point \(A=1\) is not a pole: for \(r<1\), \(Z_r\) is entire and
\(X_\zeta\) vanishes there; at \(r=1\), the full product
\(X_\zeta(A)\zeta(A)=\zeta(1-A)\) is regular at \(A=1\).  The character
\(L\)-function is entire.  Shifting through \(A=0\) would double-count
the already owned arithmetic residue, while shifting through \(A=C\)
would isolate an artificial \(R_1\) residue whose cancellation requires
its common partner.  Neither shift is made here.

On the fundamental line, suppose first that the smooth mask support is
contained in the finite \(A\)-segment.  Set

\[
 m_{z,C,\delta}(A)=
 \Theta(\operatorname {Im}(A+z))
 \frac{L(1-A-z,\chi _4)}{C-A}
\]

and let \(\omega_{z,C,\delta}\) be its inverse Mellin transform on
\(\operatorname {Re}A=\delta\).  Mellin convolution and the stated inverse
Mellin identity give, distributionally and pointwise after convolution
with a permitted smooth profile,

\[
 \begin{aligned}
 \mathcal K_{\delta,r}(x;u,v)
 &=\int_0^\infty
   C_r(x/t)\,\omega_{z,C,\delta}(t)\,\frac{dt}{t},\\
 C_r(Y)
 &=\frac1{2\pi i}\int_{(\delta)}
   X_\zeta(A)Z_r(A)Y^{-A}\,dA
 =2\sum_{h\geq1}r^h\cos(2\pi hY).
 \end{aligned}
\tag{3.3}
\]

The unmasked comb \(C_r\) is not itself the hierarchical alpha share:
the transition mask and all terms in the connector completion (2.2)
remain part of that share.

The Cauchy factor is genuinely one-sided in Mellin space:

\[
 \frac1{C-A}=-\int_1^\infty q^{C-A-1}\,dq
 \qquad(\operatorname {Re}A>\operatorname {Re}C),
\tag{3.4}
\]

so it cannot be discarded as a bounded scalar before the radial and
height limits.  Equations (3.3)--(3.4) are the promised masked
cosine--Cauchy kernel.

The geometric series evaluates the pure comb:

\[
 C_r(Y)=2\operatorname {Re}
 \frac{re^{2\pi iY}}{1-re^{2\pi iY}}.
\tag{3.5}
\]

At every integer \(Y\), (3.5) equals \(2r/(1-r)\).  Therefore a bound
uniform in \(r\) cannot be obtained coefficientwise or in the supremum
norm before the multiplicative convolution and radial integration.  On
the shifted line, the same obstruction appears as the failure of
absolute summation at \(r=1\), since \(\delta<1\).

Finally, insert one cosine from (3.3) into the radial phase.  The plus
phase has no positive stationary point, but the minus phase satisfies

\[
 (\phi^-_{h,t})'(x)=\frac{\sqrt X}{2\sqrt x}-\frac ht,
 \qquad
 (\phi^-_{h,t})''(x)=-\frac{\sqrt X}{4x^{3/2}}.
\]

Whenever \(1<Xt^2/(4h^2)<N_X\), it has the stationary point and phase
stated in Section 1, with

\[
 (\phi^-_{h,t})''(x_{h,t})=-\frac{2h^3}{Xt^3}.
\tag{3.6}
\]

Hence a uniform radial integration-by-parts argument is false.  A
stationary-phase treatment produces a weighted reciprocal-phase sum
\(\sum_h W(h,t)e(Xt/(4h))\), still integrated against the actual
multiplicative, \(u\)-, \(v\)-, and connector weights.  Proving its
aggregate cancellation is precisely (2.5), not a consequence of the
cosine identity.

No \(u\)- or \(v\)-line was moved in deriving (3.1), so no such residue is
hidden.  If the physical architecture subsequently moves both upward
lines left across zero, the exact sequential residue ledger from the
same regularized integrand is

\[
 I_{a,b}=I_{0,0}+R_{u=0}+R_{v=0}+R_{u=v=0}
          +H_u+H_v+H_{uv},
\tag{3.7}
\]

where every \(H\) denotes its signed finite top-minus-bottom outside
face.  The signs of the three residue terms are positive for leftward
displacement of upward contours; the joint corner occurs once.  Formula
(3.7) must be formed before any face is exhausted or estimated.  The
actual profile residues are not specified in the packet, so (3.7) is an
ownership identity, not an evaluation of them.

## 4. First doubtful or unproved step

The first unproved step is the following uniform assertion:

> After (and only after) adding the fundamental-line term, the smooth
> area connector or both sharp strip edges, every finite \(s\)-outside
> side, and the oriented \(u=0\), \(v=0\), and joint-corner ledger from a
> single \(r,U,V,S\) antecedent, the signed radial operator in (3.2) is
> uniformly \(O_\varepsilon(X^\varepsilon)\), is Cauchy under symmetric
> height exhaustion, and admits the ordered limit \(r\uparrow1\) at each
> finite height.

This is not an ordinary dominated-convergence problem.  Absolute height
control leaves \(U^\gamma\), with
\(\gamma=c'-1/2-(a+b)/2>1/2\).  The assertion must therefore provide a
full \(U^{-\gamma}\) gain (up to logarithms).  It must also control the
interior stationary family (3.6) at normalized \(X^0\) scale.  The exact
integer value (3.5) rules out a uniform coefficientwise majorant, and
the stationary point rules out uniform radial nonstationarity.  Neither
the mask nor the Cauchy factor has a stated mean-zero or orthogonality
condition that would make these obstructions cancel automatically.

There is also a finite-geometric condition that must not be hidden: if
the support of \(\Theta\) is contained in \([-M,M]\), then the \(s\)-outside
sides vanish identically only once

\[
 S>\frac{U+V}{2}+M.
\]

The weaker displayed inequality \(S>(U+V)/2\) does not by itself remove
them.  Without this stronger choice they remain as \(\mathcal E_{s,r}^S\)
and must be covered by the same uniform estimate.  Likewise, the packet
does not provide profile estimates that would independently exhaust the
\(u\)- and \(v\)-faces.  These are subsidiary parts of the same missing
outside-height theorem, not permissions to delete the faces.

## 5. Control tests and outcomes

- **branch_orientation — pass.**  Only \(X_\zeta(A)\zeta(A)\) is kept in
  its high expansion; the bounded character factor is
  \(L(1-B,\chi _4)=L(1-A-z,\chi _4)\).  The map \(ds=dA\) preserves the
  upward orientation, and the physical factor remains
  \(-4\pi^{-1}X^{1/4}\operatorname {Re}\{e(1/8)\cdot\}\).

- **common_antecedent_and_mask_connectors — pass.**  A single Abel
  parameter and one finite \(U,V,S\) antecedent produce all terms in
  (2.2).  A smooth mask yields the area term in (2.3); a sharp mask yields
  both oppositely oriented edges in (2.4).  No connector is estimated or
  limited separately.

- **pole_and_residue_ledger — pass at the stated displacement.**  Taking
  \(\delta>1/4\) crosses neither \(A=0\) nor \(A=C\); \(A=1\) is removable.
  The \(A=0\) arithmetic residue and the artificial \(\rho=0\) residue are
  not reinserted.  Formula (3.7) records the \(u=0\), \(v=0\), and unique
  joint corner if those contours are moved.

- **signed_height_order — pass as a definition, open as an estimate.**
  At fixed finite heights, first sum the complete signed physical
  expression and take \(r\uparrow1\); only then take a symmetric cofinal
  height limit.  No interchange of this order is established.

- **integer_cosine_resonance — falsifies the naive route.**  Equation
  (3.5) gives \(C_r(n)=2r/(1-r)\) for every integer \(n\).  Thus the
  unsigned tower has no uniform coefficientwise or supremum bound.

- **unsigned_coefficient_control — pass only on the original line.**
  The series is absolutely controlled for \(\operatorname {Re}A=\sigma>1\).
  It is not absolutely controlled on \(\operatorname {Re}A=\delta<1\) as
  \(r\uparrow1\); the shifted equality is valid only for the common
  regularization and subsequent signed aggregate.

- **radial_and_external_normalization — pass.**  Equation (3.1) retains
  the exact radial \(R_1\) factor, actual profiles, floors, stars, and
  scales.  Equation (3.2) applies exactly one external \(X^{1/4}\).
  Radial endpoint terms are not regenerated by an integration by parts;
  if stationary phase is later used, its boundary terms remain owned by
  the already separated endpoint module.

- **outside_height_limit — open.**  The known absolute capacity grows as
  \(U^\gamma\).  Neither the required signed Cauchy-tail estimate nor
  independent bounds for all finite outside faces occur in the packet.

- **downstream_scope — pass.**  The derivation concerns only the
  alpha-bounded terminal.  It gives no implication for a completed swept
  operator, a post-functional-equation kernel, or any final circle
  estimate.

## 6. Dependencies and exact artifacts used

The only mathematical artifact used was
`rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/derivation_packet.md`.
The task instructions were taken from
`rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/briefs/blind_alpha_kernel_rederivation.md`.
No proof graph, proof draft, earlier report or synthesis, other Round-49
work, web source, numerical experiment, Python computation, or
Mathematica computation was inspected or used.

Isolation ledger:

| Item | Treatment in this report |
|---|---|
| beta-bounded branch | excluded; never used to infer an alpha bound |
| radial endpoints and radial sides | referenced as separately owned; not regenerated |
| recombined \(R_1\) arithmetic residue at \(A=0\) | excluded; the contour stays to its right |
| artificial \(\rho=0\) residue | excluded; the contour stays to its right |
| alpha fundamental line | retained in \(\mathcal K_{\delta,r}^S\) |
| smooth/sharp mask connectors | retained in \(\mathcal C_{\Theta,r}^S\) |
| finite \(s\)-outside sides | retained in \(\mathcal E_{s,r}^S\) unless the support is enclosed |
| \(u=0\), \(v=0\), joint corner and outside faces | recorded once by (3.7) if those shifts are made |
| high \(h\)-tower | retained through one common Abel parameter; never made absolute on the shifted line |
| physical normalization | retained with one external \(X^{1/4}\) |

## 7. Recommended state effect

**Retain/revise; do not promote the target estimate.**  Retain (2.1)--(3.4)
as an exact definition and connector-completed reduction of the
alpha-bounded operator, and retain (3.5)--(3.6) as rigorous no-go tests
for coefficientwise cosine cancellation and radial nonstationarity.
Revise the next obligation to the single uniform estimate stated in
Section 4, with the explicit support/finite-side alternative and the
required \(U^{-\gamma}\) gain.  Reject any proposal that drops an area or
strip-edge connector, takes the high series absolutely on
\(\operatorname {Re}A<1\), uses radial integration by parts uniformly, or
deduces this alpha estimate from a completed beta branch.
