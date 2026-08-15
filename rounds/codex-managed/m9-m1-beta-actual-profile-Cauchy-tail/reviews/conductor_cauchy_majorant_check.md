# Conductor verification: the (c'=5/4) Cauchy majorant

Campaign: `m9-m1-beta-actual-profile-cauchy-tail`  
Role: conductor independent seam verification  
Allocation: 100% analytical/algebraic

Choose

\[
c'=\frac54,\qquad b=\frac1{\log(2X)},\qquad
0\le a<a_0,qquad a+b<\frac12,qquad \frac a2+b<\frac14.
\tag{38.C10}
\]

These inequalities are compatible for all sufficiently large (X), and
(c'>1+(a+b)/2) remains in the absolute dual-series chamber.  Put

\[
\delta=a+b,qquad
\kappa=c'+\delta/2-1/2=\frac34+\frac\delta2<1.
\tag{38.C11}
\]

On the beta slab,

\[
A=s-(u+v)/2=\left(\frac54-\frac\delta2\right)+i\beta,
\]

is confined to a compact vertical strip, while

\[
B=s+(u+v)/2=\left(\frac54+\frac\delta2\right)+i\alpha.
\]

The gamma quotient therefore has magnitude

\[
|K_{u+v}(1-s)|\ll(1+|\alpha|)^\kappa.
\tag{38.C12}
\]

The real coefficient powers are exactly

\[
h^{-5/4+\delta/2}q^{-5/4-\delta/2};
\tag{38.C13}
\]

both exponents are greater than one under (38.C10), including one logarithm
from a tangent derivative.  Thus the terminal coefficient series may be
summed absolutely.

The radial coordinate is

\[
\rho=-1-b/2-i(\mu/2+\nu+\beta).
\tag{38.C14}
\]

Since the (I_1) integrand has absolute weight
(x^{-3/2-b/2}), both (I_1) and its first tangent derivative are bounded,
and

\[
|R_1|+|\partial_\mu R_1|\ll_X
\{1+|\mu/2+\nu|\}^{-1}
\tag{38.C15}
\]

up to bounded beta shifts.

After the signed top split, the complete terminal numerator (H) obeys

\[
|H(\mu,\nu)|\ll_X|f_b(\nu)|
\frac{(1+|\mu+\nu|)^\kappa}
     {1+|\mu/2+\nu|},
\tag{38.C16}
\]

and its local (mu)-difference quotient costs at most one logarithm.  The
key elementary convolution is

\[
\int_{|\mu|>1}
\frac{(1+|\mu+\nu|)^\kappa}
{|\mu|\{1+|\mu/2+\nu|\}}\,d\mu
\ll(1+|\nu|)^{\kappa-1}\log(2+|\nu|).
\tag{38.C17}
\]

Splitting at scales (1,|\nu|/4,4|\nu|), and neighborhoods of
(-\nu,-2\nu) verifies (38.C17); the far integral is
(\int r^{\kappa-2}dr), convergent precisely because (kappa<1).
The symmetric PV subtracts (H(0,\nu)) near zero.  Since

\[
|f_b(\nu)|\ll_b(1+|\nu|)^{-3},
\]

the final majorant is

\[
|\mathcal F_T(\nu)|\ll_{X,b}
(1+|\nu|)^{\kappa-4}\log(2+|\nu|),
\tag{38.C18}
\]

which is integrable and uniform in the symmetric (mu)-cutoff.

At the artificial residue, (38.C13) must not be used: that cell lies
outside the absolute coefficient chamber.  Recombine the completed factor
as (zeta(1-A)L(1-B,\chi_4)).  Compact beta support forces
(mu=-2\nu+O(1)); the top factor gives (O(|\nu|^{-1})), the height
profile gives (O_b(|\nu|^{-3})), and elementary Dirichlet summation gives
(L(1-B,\chi_4)=O(1+|\nu|)).  The residue tail is therefore
(O_{X,b}(|\nu|^{-3})).

These two integrable majorants prove the (U,V) Cauchy property.  Compact
beta support makes the (S)-stage eventually constant and deletes the
radial sides.  This verifies existence only: the constants have not been
controlled by (X^\varepsilon), and no local (q^{-2}) or terminal-symbol
estimate follows.

No numerical experiment or external theorem was used.
