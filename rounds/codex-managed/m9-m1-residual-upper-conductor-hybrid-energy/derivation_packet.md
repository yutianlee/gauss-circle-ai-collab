# Round 73 frozen derivation packet

## 1. Accepted state and scope

Put

\[
 J=X^{1/2},\qquad Q=X^{1/5}=J^{2/5},\qquad
 T=J/Q=J^{3/5}.
\]

Rounds 71 and 72 prove that every exact fixed-smooth-interior order-\(J\)
Farey block with

\[
 T\leq C\leq J^{32/45}=X^{16/45}
\]

is target-safe.  Only

\[
 J^{32/45}<C\leq J                                  \tag{73.1}
\]

is in scope.  Cone edges, other radial sectors, and the global
\(M9\!-\!M1\) theorem are not part of this packet.

## 2. Exact residual rows

Let \(b\asymp B=C/T\), let \(k=\rho\sigma\) run over the fixed compatible
nonaxial dual family, and put

\[
 \kappa=\frac{c}{[c,4]}\in\{1/4,1/2,1\},\qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2.
                                                               \tag{73.2}
\]

For either endpoint orientation and every local parity class, fixing an
admissible residue \(c=r\pmod{4b}\) makes the exact arithmetic local unit
constant.  After also fixing the two Farey-neighbor numerators, the row is
an exact finite sum of cells

\[
 S_{b,k}^{(\kappa)}(C)
 =\sum_{\substack{r\bmod 4b\\r\ \mathrm{admissible}}}
  u_{b,r,k}^{(\kappa)}
  \sum_\nu\sum_{\ell\in I_{b,r,\nu}}
  w_{b,r,\nu,k}^{(\kappa)}(\ell)
  e\!\left(\pm\frac{A_{\kappa,b}}{r+4b\ell}\right).           \tag{73.3}
\]

Here \(|u_{b,r,k}^{(\kappa)}|\leq1\), and it contains the exact inverse
unit or even lift unit.  The cells are half-open and one-count.  The accepted
symbol bounds are

\[
 \|w_{b,r,\nu,k}^{(\kappa)}\|_\infty
 +\operatorname {Var}(w_{b,r,\nu,k}^{(\kappa)})
 \ll_\varepsilon X^\varepsilon,                              \tag{73.4}
\]

\[
 \sum_{r,\nu}|I_{b,r,\nu}|\ll C,qquad
 \#\{(r,\nu)\}\ll_\varepsilon QX^\varepsilon,qquad
 |I_{b,r,\nu}|\ll C/Q.                                      \tag{73.5}
\]

The two axes remain separate nonstationary rows and must be retained.

## 3. Accepted derivative bound and exact deficit

On every cell,

\[
 \left|\frac{d^3}{d\ell^3}
 \frac{A_{\kappa,b}}{r+4b\ell}\right|
 \asymp Q^{-1}.                                               \tag{73.6}
\]

Round 72 therefore proves

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon CQ^{-1/6},\qquad
 \mathcal E_{C,k}^{(\kappa)}
 :=\sum_{b\asymp B}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon\frac{C^3}{TQ^{1/3}}.          \tag{73.7}
\]

The required energy is

\[
 \boxed{\mathcal E_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon\frac{J^2}{T}}.                \tag{73.8}
\]

Thus an argument measured against (73.7) must save the factor

\[
 \Delta_E(C)=\frac{C^3}{J^2Q^{1/3}}>1.                        \tag{73.9}
\]

Alternatively, the sufficient first moment is

\[
 \left|\sum_{b\asymp B}S_{b,k}^{(\kappa)}(C)\right|
 \ll_\varepsilon X^\varepsilon\frac{J\sqrt C}{T}.            \tag{73.10}
\]

The triangle bound after (73.7) misses (73.10) by

\[
 \Delta_1(C)=\frac{C^{3/2}}{JQ^{1/6}}.                        \tag{73.11}
\]

At \(C=J\), \(\Delta_1(J)=J^{13/30}\).  Every claimed gain must be
computed against these exact normalizations.

## 4. Lawful candidate interfaces

A direct proof may combine the third-derivative cancellation inside the
\(\ell\)-cells with genuinely joint cancellation in \(r\) and \(b\).  It
must estimate (73.3) with its actual local unit and transition weights before
taking absolute values in the variables where cancellation is claimed.

For the odd class, exact reciprocity also gives

\[
 e_{4b}(k\bar c)e(-A_{1/4,b}/c)
 =e_c(-k\overline{4b})
  e\!\left(-\frac{bX+J\sqrt k}{c}\right).                     \tag{73.12}
\]

Smooth completion in \(b\pmod c\) produces displacements
\(|h|\ll T\) and the generalized level-four cusp sum

\[
 S_{\infty,1}(N-h,k;2c)
 =S((N-h)\overline4,k;c),                                    \tag{73.13}
\]

while the external phase matches one large-argument Bessel branch.  This is
a lawful non-self-returning reduction only if the actual transition weight,
Bessel transform, Eisenstein spectrum, periodic unit, even classes, and axes
are retained.  A bare appeal to a conjectural \(X^{1/4}\) short Hecke sum is
not a proof.

## 5. Forbidden shortcuts

The following do not close (73.8):

1. repeating \(c\)-Poisson followed by the matching one-variable
   \(B\)-process, which is an exact self-return;
2. multiplying a full-progression estimate by the number of Farey pieces;
3. replacing the actual inverse/even unit by arbitrary coefficients;
4. inferring the even classes or axes from the odd positive branch by a sign
   change;
5. applying a spectral large sieve at interval length \(T\) while ignoring
   that the automorphic index has magnitude \(X\);
6. claiming a global exponent from a fixed-interior conductor estimate.

## 6. Mandatory controls

Every candidate must audit the exact energy or first-moment normalization,
cell ownership, transition variation, diagonal and near diagonal, analytic
rank or degeneracy, inverse local unit, all even classes, both axes, gcds,
perfect squares and fourth powers, finite dual/error sums, source
hypotheses, self-return avoidance, and downstream scope.

## 7. Report contract

Every report must have exactly seven semantic sections: Result; Exact
statement and hypotheses; Proof or derivation; First doubtful or unproved
step; Required control test and outcome; Dependencies and exact
artifacts/sources used; Recommended state effect.  Reports must be valid
UTF-8, contain no forbidden control bytes, and must not edit shared state.
