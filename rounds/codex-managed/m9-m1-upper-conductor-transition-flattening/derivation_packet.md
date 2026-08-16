# Round 81 frozen derivation packet

## 1. Accepted state and scope

Put

\[
 J=X^{1/2},\qquad Q=X^{1/5}=J^{2/5},\qquad
 T=J/Q=J^{3/5}.
\]

The accepted fixed-smooth-interior order-\(J\) Farey analysis proves the
target through

\[
 T\leq C\leq J^{32/45}.
\]

This packet concerns only the next conductor range.  Cone edges, other
radial sectors, the full \(M9\!-!M1\) theorem, \(M9\), and the final
Gauss-circle exponent are outside scope.

Let \(b\asymp B=C/T\), let \(k=\rho\sigma\) run over the fixed compatible
nonaxial dual family, and put

\[
 \kappa=\frac{c}{[c,4]}\in\{1/4,1/2,1\},\qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2.
 \tag{81.1}
\]

For either endpoint orientation, fixing an admissible residue
\(c=r\pmod {4b}\) makes the exact odd or even arithmetic unit constant.
The accepted row is

\[
 S_{b,k}^{(\kappa)}(C)
 =\sum_{r\bmod4b}u_{b,r,k}^{(\kappa)}
   \sum_\nu\sum_{\ell\in I_{b,r,\nu}}
   w_{b,r,\nu,k}^{(\kappa)}(\ell)
   e\!\left(\pm\frac{A_{\kappa,b}}{r+4b\ell}\right),
 \tag{81.2}
\]

where the half-open cells are one-count,

\[
 \|w_{b,r,\nu,k}^{(\kappa)}\|_\infty
 +\operatorname {Var}(w_{b,r,\nu,k}^{(\kappa)})
 \ll_\varepsilon X^\varepsilon,
 \tag{81.3}
\]

\[
 \sum_{r,\nu}|I_{b,r,\nu}|\ll C,\qquad
 \#\{(r,\nu)\}\ll_\varepsilon QX^\varepsilon,
 \qquad |I_{b,r,\nu}|\ll C/Q.
 \tag{81.4}
\]

The cellwise third-derivative estimate gives

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon C Q^{-1/6},\qquad
 \sum_{b\asymp B}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon\frac{C^3}{TQ^{1/3}},
 \tag{81.5}
\]

which is target-safe precisely through \(C\leq J^{32/45}\).

## 2. Exact Farey transition geometry

Let \(R=\lfloor J\rfloor\), and let \(a_-/c_-\) and \(a_+/c_+\) be the
Farey neighbors of the reduced fraction \(b/c\) at order \(R\).  Then

\[
 bc_--a_-c=1,\qquad a_+c-bc_+=1,\qquad
 R-c<c_\pm\leq R.
 \tag{81.6}
\]

On a piece where the neighbor numerators are fixed,

\[
 c_-=(a_-c+1)/b,\qquad c_+=(a_+c-1)/b.
 \tag{81.7}
\]

After the exact substitutions

\[
 x=Ju,\quad y=Jv,\quad \tau=\beta J^2,
 \quad \tau=(J/c)z,
\]

the sharp \(z\)-interval is

\[
 z_-(c)=-\frac{J}{c+c_-},\qquad
 z_+(c)= \frac{J}{c+c_+},
 \tag{81.8}
\]

up to the harmless exact replacement of \(J\) by \(R\) in the Farey
endpoints.  The scaled phase is

\[
 \phi(z,u,v)=z(uv-1)-\rho u-\kappa\sigma v.
 \tag{81.9}
\]

Its nonaxial critical point satisfies

\[
 z_*^2=\kappa\rho\sigma=\kappa k.
 \tag{81.10}
\]

The ratio support leaves only a fixed finite family of \((\rho,\sigma)\).
With \(\Lambda=J/c\), a normalized leading transition factor has the
form

\[
 \mathfrak F_\epsilon(Y_-,Y_+),\qquad
 Y_\pm=\sqrt\Lambda\,(z_\pm-z_*),
 \tag{81.11}
\]

where \(\epsilon\in\{+1,-1\}\) is the Morse sign and
\(\mathfrak F_\epsilon\) is the corresponding incomplete Gaussian.  The
complete actual weight also contains the exact smooth ratio symbol,
alias, local unit, stationary Jacobian, floors, orientations, and the
uniform stationary remainder.

On a fixed residue progression there are \(O(J/C)=O(Q/B)\)
neighbor-numerator changes.  A numerator-fixed piece has \(c\)-length
\(O(C^2/J)\), hence \(O(C/Q)\) progression samples.  Cellwise variation
is accepted; global variation across the changes is not.

## 3. Candidate transition-flattening lemma

The round tests the following exact interface.  For every retained
oriented nonaxial row, after a fixed Morse partition independent of the
Farey neighbors, write the complete normalized weight on a residue
progression as

\[
 W_{b,r}(c)=\Gamma_{\epsilon,z_*}\,V_{b,r}(c)+E_{b,r}(c).
 \tag{81.12}
\]

Here \(\Gamma_{\epsilon,z_*}\) is the neighbor-independent limiting
Gaussian coefficient for the interval \([-1,1]\): full when
\(-1<z_*<1\), the oriented half coefficient when \(z_*=\pm1\), and zero
when \(|z_*|>1\).  The desired bounds are

\[
 \|V_{b,r}\|_\infty+\operatorname {Var}(V_{b,r})
 \ll_\varepsilon X^\varepsilon,
 \tag{81.13}
\]

on the whole half-open progression, without cutting at Farey-neighbor
changes, and

\[
 \sup_c|E_{b,r}(c)|
 \ll_\varepsilon X^\varepsilon\Lambda^{-1/2}
 \asymp X^\varepsilon\sqrt{C/J}.
 \tag{81.14}
\]

No bounded-variation assertion is requested for \(E_{b,r}\).  The proof
must be for the complete actual coefficient.  At the leading-model level
it should follow from the oscillatory tail bound

\[
 \left|\int_Y^\infty e(\epsilon t^2/2)\,dt\right|
 \ll (1+|Y|)^{-1}
 \tag{81.15}
\]

and the finite-set dichotomy \(z_*\in(-1,1)\), \(z_*=\pm1\), or
\(|z_*|>1\).  At an exact boundary, (81.8) gives an adjacent standardized
face of size \(O(\Lambda^{-1/2})\); the opposite face has size
\(\asymp\sqrt\Lambda\) and is controlled by the oscillatory tail in
(81.15).  The candidate must also prove that the
uniform three-variable stationary remainder and every moving-symbol
correction obey (81.14).

## 4. Exact implication if the lemma holds

The already audited full-progression reciprocal exponent-pair estimate is

\[
 \sup_{I\subseteq[1,T]}
 \left|\sum_{\ell\in I}
 e\!\left(\pm\frac{A_{\kappa,b}}{r+4b\ell}\right)\right|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
 \tag{81.16}
\]

Abel summation with (81.13), followed by the \(O(B)\) residue sum, gives

\[
 |S_{b,k}^{(\kappa),\mathrm{main}}(C)|
 \ll_\varepsilon X^\varepsilon C Q^{-5/24}.
 \tag{81.17}
\]

Triangle summation of (81.14) over the \(O(C)\) moduli in a fixed
\(b\)-row gives

\[
 |S_{b,k}^{(\kappa),\mathrm{err}}(C)|
 \ll_\varepsilon X^\varepsilon C\sqrt{C/J}.
 \tag{81.18}
\]

Consequently

\[
 \sum_{b\asymp C/T}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon
 \left\{\frac{C^3}{TQ^{5/12}}+\frac{C^4}{TJ}\right\}.
 \tag{81.19}
\]

The first term is at most \(J^2/T\) for

\[
 C\leq J^{13/18},
 \tag{81.20}
\]

and the second is target-safe for \(C\leq J^{3/4}\).  Thus (81.12)--
(81.14), if proved with all classes and orientations, extend the accepted
fixed-interior range from \(J^{32/45}\) to \(J^{13/18}\).

## 5. Mandatory hostile sawtooth control

A stronger global-BV claim is not assumed.  In the actual class
\(4\mid c\), \(\kappa=1\), \(\rho=\sigma=1\), one has \(z_*=1\).
Along a fixed admissible progression \(c=r\pmod{4b}\), the right-neighbor
numerator changes \(\asymp J/C\) times.  At a change, \(c_+\) can jump by
\(\asymp C\), so

\[
 \Delta\!\left[\sqrt{J/c}\,(z_+(c)-1)\right]
 \asymp\sqrt{C/J}.
 \tag{81.21}
\]

The naive total variation can therefore have capacity
\(\sqrt{J/C}\).  Every proof must either establish the precise version
of this control and use the small pointwise remainder (81.14), or exhibit
an exact cancellation that invalidates it.  Merely summing the cellwise
BV bounds is forbidden.

## 6. Required controls

Every candidate must audit:

1. the exact Farey determinant signs, half-open endpoints, and both aliases;
2. the \(R=\lfloor J\rfloor\) versus \(J\) normalization;
3. all three \(\kappa\)-classes, local units, gcd restrictions, and the two
   separately accepted axes;
4. the finite critical family and the inside/boundary/outside trichotomy;
5. the full stationary remainder, not only the leading incomplete
   Gaussian;
6. the sawtooth control (81.21), singleton pieces, and simultaneous
   neighbor changes;
7. the full-progression source range and proper-subinterval uniformity in
   (81.16);
8. the exact energy arithmetic in (81.19)--(81.20);
9. perfect squares/fourth powers and phase-conjugating coefficients;
10. floors, stars, cone-edge exclusions, and downstream scope.

## 7. Forbidden shortcuts and report contract

Do not multiply (81.16) by the number of Farey pieces.  Do not assert a
global BV bound from cellwise BV.  Do not discard the transition
remainder, axes, even classes, local units, or endpoint orientations.  Do
not infer a global exponent from a fixed-interior conductor extension.

Each report must contain exactly seven semantic sections: Result; Exact
statement and hypotheses; Proof or derivation; First doubtful or unproved
step; Required control test and outcome; Dependencies and exact artifacts
or sources used; Recommended state effect.  Reports are evidence only and
must not edit shared state.
