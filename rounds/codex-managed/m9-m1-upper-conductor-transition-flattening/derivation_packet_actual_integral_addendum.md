# Round 81 conductor-authorized exact-integral addendum

This addendum supplies the exact interface omitted from the first blind
packet.  It is extracted from the accepted finite Farey identity and its
fixed-smooth-interior amplitude class.  It does not assert the desired
flattening conclusion.

Fix one endpoint orientation, one nonaxial pair \((\rho,\sigma)\), one
local class \(\kappa\), one numerator \(b\), and one admissible residue
\(c=r\pmod {4b}\).  Put \(\Lambda=J/c\) and

\[
 \phi(z,u,v)=z(uv-1)-\rho u-\kappa\sigma v.
\]

After extracting the exact constant local unit and the already displayed
reciprocal phase, the normalized complete coefficient is

\[
 \mathcal W(c)=
 \Lambda^{1/2}e(-\Lambda\phi_*)\,
 \Lambda\int_{z_-(c)}^{z_+(c)}
 \iint a_c(z,u,v)e(\Lambda\phi(z,u,v))\,du\,dv\,dz.
 \tag{81.A1}
\]

The harmless fixed Gaussian convention may multiply both sides by a unit;
it is absorbed into the limiting coefficient.  The endpoints are exactly
the Farey endpoints in the main packet, with \(R=\lfloor J\rfloor\) in
the neighbor definition.

The actual fixed-interior amplitude has a neighbor-independent smooth
extension \(a_c\).  For a fixed sufficiently large \(M\), after the fixed
partition into neighborhoods of \(z=1\), \(z=-1\), and the central
nonstationary region,

\[
 \max_{|\alpha|\leq M}\sup_{c,z,u,v}
 |\partial_{z,u,v}^{\alpha}a_c(z,u,v)|
 \ll_\varepsilon X^\varepsilon,
 \tag{81.A2}
\]

and the continuous extension in \(c\) satisfies

\[
 \max_{|\alpha|\leq M}
 \int_C^{2C}\sup_{z,u,v}
 |\partial_c\partial_{z,u,v}^{\alpha}a_c(z,u,v)|\,dc
 \ll_\varepsilon X^\varepsilon.
 \tag{81.A3}
\]

Its support in \((u,v)\) is fixed compact, and the stationary support is
bounded away from \(z=0\).  The amplitude contains the dyadic conductor
cutoff, the fixed ratio symbol, and the exact offset alias evaluated before
stationary phase.  The alias costs at most \(T/(cJ)\) per \(z\)-derivative;
at a critical point its \(c\)-dependence is through the smooth normalized
variables \(c/C\), \(Tb/c\), \(c/J\), and fixed stationary ratios.  Floors
and the half-open convention occur only in the exact Farey endpoints;
there is no additional neighbor-dependent floor or star correction inside
\(a_c\).

The local arithmetic unit is constant on the fixed residue progression.
The two nonstationary axes are excluded from (81.A1) and retain their
accepted bound \(O_\varepsilon(X^\varepsilon C^2/J)\).  The central
\(z\)-piece for a nonaxial pair has a phase derivative bounded away from
zero in \(u\) or \(v\) and is arbitrarily small after integration by parts.

The blind gate should now determine directly from (81.A1)--(81.A3), rather
than assume, whether

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),\qquad
 \|V\|_\infty+\operatorname {Var}(V)\ll_\varepsilon X^\varepsilon,
 \quad |E(c)|\ll_\varepsilon X^\varepsilon\Lambda^{-1/2}.
\]

It must use the full integral, including the first omitted stationary
term, and must retain the exact moving endpoint through boundary saddles.
