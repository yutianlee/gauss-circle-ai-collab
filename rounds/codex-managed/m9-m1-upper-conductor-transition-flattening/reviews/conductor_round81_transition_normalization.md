# Round 81 transition-normalization review

Campaign: `m9-m1-upper-conductor-transition-flattening`
Starting graph SHA-256:
`f69da71546e5a6fd1d48c7fa561e17b62ce6669fb4a29c497f74f748e7379635`

## Decision

The exact-integral normalization, the complete first stationary
corrections, and the Farey-boundary scaling pass.  The complete fixed-
interior coefficient admits

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),\qquad
 \|V\|_\infty+\operatorname {Var}V\ll_\varepsilon X^\varepsilon,
 \qquad
 |E(c)|\ll_\varepsilon X^\varepsilon\sqrt{C/J}.
 \tag{81.N1}
\]

The raw incomplete-Gaussian transition does **not** have bounded total
variation: its possible variation is \(\asymp\sqrt{J/C}\).  The proof is
valid because this transition is kept in the pointwise-small remainder
\(E\), while only the neighbor-independent critical coefficient \(V\) is
used as an Abel weight.

## Exact finite antecedent

Round 71 equation (71.C8), followed by

\[
 x=Ju,\qquad y=Jv,\qquad \tau=\beta J^2,
 \qquad \tau=(J/c)z,
\]

gives, after extracting the constant local unit and the reciprocal phase,

\[
 \mathcal W(c)=\Lambda^{1/2}e(-\Lambda\phi_*)
 \Lambda\int_{z_-(c)}^{z_+(c)}\iint
 a_c(z,u,v)e(\Lambda\phi(z,u,v))\,du\,dv\,dz,
 \quad \Lambda=J/c.                              \tag{81.N2}
\]

Here

\[
 \phi=z(uv-1)-\rho u-\kappa\sigma v,
 \qquad
 z_-=-{J\over c+c_-},\quad z_+={J\over c+c_+}.
\]

The factors \(J^2\) from \(dx\,dy\), \(J^{-2}\) from \(d\beta\), and
\(d\tau=\Lambda dz\) give exactly the normalization in (81.N2).  Both
offset aliases are already present in the exact Round 71 antecedent.

On a fixed progression \(c=r\pmod {4b}\), the parity class, gcd
restriction, and local unit are constant.  The remaining amplitude depends
on \(c\) only through smooth normalized variables.  In particular the
alias has arguments of the form

\[
 {Tb\over c}+O\!\left({Tz\over cJ}\right),
\]

the conductor cutoff depends on \(c/C\), and the ratio symbol is fixed.
Each \(c\)-derivative therefore costs \(O(C^{-1})\), or less, on a dyadic
\(c\)-block.  The exact finite identity consequently gives

\[
 \max_{|\alpha|\le M}\int_C^{2C}
 \sup_{z,u,v}|\partial_c\partial_{z,u,v}^{\alpha}a_c|\,dc
 \ll_\varepsilon X^\varepsilon.                 \tag{81.N3}
\]

Farey neighbors occur only in the sharp endpoints.  Thus the addendum
(81.A1)--(81.A3) is a typed extraction of the accepted finite identity,
not an assumption of the desired flattening.

## Stationary normalization

At fixed \(z\ne0\), put

\[
 p=u-{\kappa\sigma\over z},\qquad
 q=v-{\rho\over z}.
\]

Then exactly

\[
 \phi(z,u,v)=\psi(z)+zpq,qquad
 \psi(z)=-z-{\kappa\rho\sigma\over z}.          \tag{81.N4}
\]

The tangential Hessian has determinant \(-z^2\), so two-dimensional
stationary phase is uniform on the fixed support away from \(z=0\).  Its
first correction is \(\Lambda^{-1}A_{1,c}(z)\); after the outer
normalization its absolute contribution is already
\(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\).

If \(z_*^2=\kappa\rho\sigma\), then

\[
 \psi(z)-\psi(z_*)=-{(z-z_*)^2\over z}.
\]

On the fixed sign chart the exact Morse variable

\[
 t={\sqrt2\,(z-z_*)\over\sqrt{|z|}}
\]

reduces the remaining phase to \(\epsilon t^2/2\).  Writing the reduced
amplitude as \(g_c(t)=g_c(0)+t h_c(t)\), integration by parts evaluates the
linear term with its exact moving endpoint and bounds it by
\(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\).  Higher tangential and
Morse corrections are smaller.  Equation (81.N3) gives

\[
 \|g_c(0)\|_\infty+\operatorname {Var}_c g_c(0)
 \ll_\varepsilon X^\varepsilon,                 \tag{81.N5}
\]

which is the asserted bound for \(V\).

## Farey boundary and hostile sawtooth

Let \(R=\lfloor J\rfloor\), \(\delta=J-R\), and
\(q_\pm=c+c_\pm-R\).  The determinant inequalities give

\[
 1\le q_\pm\le c,
\]

and, at the boundary saddle \(z_*=1\),

\[
 \sqrt\Lambda\,(z_+-1)
 =\sqrt{J/c}\,{\delta-q_+\over R+q_+}
 =O(\Lambda^{-1/2}).                             \tag{81.N6}
\]

The opposite face is **not** small: its standardized Morse distance is
\(\asymp\sqrt\Lambda\).  Its oscillatory tail is nevertheless
\(O(\Lambda^{-1/2})\).  This correction is present consistently in the
discovery, blind, and hostile reports.

The exact numerator reset changes the adjacent standardized face by
\(\asymp\sqrt{C/J}\), and there are \(\asymp J/C\) resets.  Hence the
raw transition variation can be \(\asymp\sqrt{J/C}\).  Left and right
resets are not simultaneous in the active range.  This falsifies a raw-BV
shortcut but does not affect (81.N1), because each reset remains inside
the pointwise remainder.

## Exponent and source check

For \(c=r+4b\ell\), the reciprocal phase is

\[
 e\!\left(\pm{K_{\kappa,b}\over\ell+\alpha}\right),
 \qquad \ell+\alpha\asymp T.
\]

Bourgain's audited exponent pair
\((13/84+\varepsilon,55/84+\varepsilon)\), with
\(M=T\), \(\mathcal T\asymp JQ\), and
\(\log M/\log\mathcal T=3/7\), gives uniformly on proper subintervals

\[
 \sup_I\left|\sum_{\ell\in I}
 e\!\left(\pm{K_{\kappa,b}\over\ell+\alpha}\right)\right|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.      \tag{81.N7}
\]

Abel summation is applied once to the globally BV main, not once per
Farey cell.  The pointwise error is triangle-summed.  Therefore

\[
 \sum_{b\asymp C/T}|S_b|^2
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{C^4\over TJ}\right). \tag{81.N8}
\]

The first term is target-safe precisely for \(C\le J^{13/18}\); the
second is target-safe for \(C\le J^{3/4}\).  Thus \(13/18\) is the
binding exponent.  The separately owned axes are safe on this interval.

## Scope

This review certifies only the fixed-smooth-interior Farey block.  It does
not estimate \(J^{13/18}<C\le J\), cone edges, other radial sectors,
full \(M9\!-\!M1\), \(M9\!-\!M2\), \(M9\), endpoint uniformity, or the
global Gauss-circle exponent.
