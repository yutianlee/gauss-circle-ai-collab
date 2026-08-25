# Conductor exact hyperbolic normalization

Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`

Starting graph SHA-256:
`328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`.

This is an independent conductor derivation. It establishes the exact
surface coordinates but makes no decoupling-applicability claim.

## 1. Exact affine chart

For a top-shell ray \(r=(a,b)\), define

\[
 \xi_r=\frac bD,
 \qquad
 \eta_r=-\frac{Da}{Lb},
 \qquad
 \zeta_r=-\frac aL.                                      \tag{132.C1}
\]

Then

\[
 \zeta_r=\xi_r\eta_r,                                    \tag{132.C2}
\]

so \(\omega_r=(\xi_r,\eta_r,\zeta_r)\) lies exactly on

\[
 \mathbb H=\{(\xi,\eta,\xi\eta)\}.
\]

This is not merely a Hessian or quadratic approximation. It is the affine
coordinate permutation of the dimensionless ratio graph
\(z=-x/y\), whose equation is \(x+yz=0\).

Put

\[
 t_i=\frac{cL}{\kappa_iD},
 \qquad \kappa_1=1,\quad\kappa_2=4.                       \tag{132.C3}
\]

For an inner ray \(r'=(a',b')\),

\[
 \frac{ca}{\kappa_i b}-\frac{ca'}{\kappa_i b'}
 =t_i(\eta_{r'}-\eta_r).                                  \tag{132.C4}
\]

Thus the outer factor is an extension wave on \(\mathbb H\) evaluated in
the \(\eta\)-dual direction and the inner factor is its oppositely oriented
wave. Since \(c\asymp Y\),

\[
 t_i\asymp \frac{YL}{D}=Y^{2/3}=Y^{32/48}.                 \tag{132.C5}
\]

The natural unrescaled physical radius is therefore at least \(t_i\), not
an unspecified unit scale.

## 2. Determinant support is near one ruling direction

If \(n=ab'-a'b>0\), then

\[
 \eta_{r'}-\eta_r
 =\frac{Dn}{Lbb'}.                                         \tag{132.C6}
\]

On \(b,b'\asymp D\) and
\(n\ll D^2/W\), this gives

\[
 0<\eta_{r'}-\eta_r\ll
 \delta_*:=\frac{D}{LW}=Y^{-5/48}.                         \tag{132.C7}
\]

Lines \(\eta=\text{constant}\) are one ruling family of \(\mathbb H\).
Consequently the complete determinant-supported bilinear relation lies in a
\(\delta_*\)-neighborhood of that ruling family. In the original source
coordinates it never satisfies the unit transversality condition
\(|\eta_{r'}-\eta_r|\asymp1\).

This observation does not by itself forbid parabolic rescaling. On a
dyadic band

\[
 h<\eta_{r'}-\eta_r\le2h,
 \qquad (LD)^{-1}\lesssim h\lesssim\delta_*,               \tag{132.C8}
\]

the exact hyperbolic symmetry

\[
 (\xi,\eta,\xi\eta)
 =(\widetilde\xi,h\widetilde\eta,
   h\widetilde\xi\widetilde\eta)                          \tag{132.C9}
\]

turns an \(h\)-separation in \(\eta\) into unit separation, but changes
the physical evaluation scale to

\[
 R_h\asymp t_i h.                                         \tag{132.C10}
\]

At the widest determinant band,

\[
 R_{\delta_*}\asymp
 \frac{YL}{D}\frac{D}{LW}=\frac YW=Y^{27/48}.             \tag{132.C11}
\]

Any use of the source after (132.C9) must still verify its Fourier
thickness, square-cap rather than anisotropic-rectangle hypotheses, spatial
ball, Jacobian, and coefficient normalization. These do not follow from
(132.C9) alone.

## 3. First structural seams

The exact chart exposes three independent seams.

1. Demeter--Wu transversality also requires separation in \(\xi\). The
   same-denominator packets have \(b'=b\), hence \(\xi_{r'}=\xi_r\), and
   remain narrow after every \(\eta\)-rescaling.
2. The target is a signed scalar at the one prescribed point
   \((0,\pm t_i,0)\). The source statements bound bilinear spatial
   integrals. A pointwise localization inequality and all normalization
   costs must be supplied separately.
3. The determinant relation couples the two frequency sets. A source
   inequality for two independent extension functions can be invoked only
   after an exact decomposition of this incidence kernel, with the literal
   variable primitive moduli, thresholds, and owners retained.

The exact surface identification is therefore real progress, but it is not
yet a source import or an exponent gain.
