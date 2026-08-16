# Round 79 conductor adjudication

Campaign: m9-m2-top-endpoint-generic-reciprocal-resonance  
Round: 79  
Starting graph SHA-256:
5e5c01114e46fcb3079a6e1427f8155421f7ec9a45c9599cbd8aa8c94cf0bac2

## Decision

Promote the exact nonsquare normal form, the metric divisor-strip
incidence theorem, the exact-center closure, and the positively safe
dyadic subregion. Also promote the route obstruction that ordinary
metric resonances occur at density \(1/R\), so a classification of
every resonance as an exceptional algebraic family is false.

The three independent reports and two conductor derivations agree on
the half-angle coordinates, open reciprocal interval, nearest-integer
orientation, divisor-strip count, and complete coefficient ledger.
They also agree that algebraic norm separation is far below the
available metric resolution and that the density saving exactly cancels
the Abel factor.

The nonsquare signed energy, signed top cone, \(M9\!-\!M2\),
\(M9\!-\!M1\), \(M9\), endpoint uniformity, and global exponent remain
open.

## Exact promoted interface

Let \(J=\sqrt X\), \(1\leq L\leq H\leq J^{1/2}\), and let
\(a<b<4a\) be primitive odd coprime integers with \(ab\) nonsquare. Put

\[
 m=\frac{a+b}{2},\qquad q=\frac{b-a}{2},\qquad
 u=\frac{q}{m+\sqrt{m^2-q^2}}
   =\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a}.
\]

Then \((m,q)=1\), \(m,q\) have opposite parity, and

\[
 \frac{(\sqrt b-\sqrt a)^2}{2}=qu,\qquad
 \Lambda=Xqu,\qquad
 \frac{Ju}{1-u}<k<\frac{2Ju}{1+u}.                 \tag{79.A}
\]

On a dyadic block
\(a\asymp A\), \(b-a\asymp D\), \(k\asymp K\),
\(G_{a,b}\asymp G\), let \(P=P(A,D,G)\) be the number of actual
residual rays and \(M_{a,b}(K)\) the literal reciprocal-mode count. For
\(1\leq R\leq N_{a,b}\ll G\),

\[
 \left\|\frac{\Lambda}{k}\right\|\leq\frac cR
 \quad\Longleftrightarrow\quad
 |\Lambda-\ell k|\leq\frac{ck}{R}.                 \tag{79.B}
\]

The divisor-strip theorem is

\[
 \boxed{
 \mathcal I_{\rm ns}(A,D,K,G;R)
 \ll_{\varepsilon,c}X^\varepsilon
 \sum_{(a,b)}
 \min\!\left(M_{a,b}(K),1+\frac KR\right).
 }                                                    \tag{79.C}
\]

Consequently

\[
 \mathcal I_{\rm ns}
 \ll_\varepsilon X^\varepsilon P\left(1+\frac KR\right)
 \ll_\varepsilon X^\varepsilon AD\left(1+\frac KR\right).
                                                               \tag{79.D}
\]

In the actual range,

\[
 K\asymp\frac{JD}{A},\qquad
 R\leq G\asymp\frac LA,\qquad
 \frac KR\gg\frac{JD}{L}\gg J^{1/2},
\]

so (79.D) saves exactly the factor \(R\):

\[
 \mathcal I_{\rm ns}\ll_\varepsilon
 X^\varepsilon\frac{ADK}{R}.                       \tag{79.E}
\]

For a fixed ray, the integer \(p=\ell k\) lies in an interval of
length \(O(K/R)\); each such integer has only \(X^\varepsilon\)
divisor factorizations. Empty and singleton intervals are retained by
the minimum in (79.C).

The complete Round-77 coefficient satisfies

\[
 \mathcal V_{a,b,k}
 \ll_\varepsilon X^\varepsilon
 \frac{J(D/\sqrt A)\sqrt G}{K^{3/2}}
 \asymp_{X^\varepsilon}\frac{A\sqrt G}{\sqrt{JD}}.   \tag{79.F}
\]

Multiplying (79.E) by the Abel weight \(R\mathcal V\), and including
the standalone Abel-\(1\) term, gives

\[
 \boxed{
 \mathcal A_{\rm ns}(A,D,K,G;R)
 \ll_\varepsilon X^\varepsilon
 A\sqrt G\,\sqrt J\,D^{3/2}.
 }                                                    \tag{79.G}
\]

Since \(G\asymp L/A\), positive summation is target-sized whenever

\[
 \boxed{AJD^3\ll L^3.}                               \tag{79.H}
\]

Thus (79.H) is a genuinely closed nonsquare subregion.

## Exact centers and algebraic isolation

Write

\[
 ab=\mathfrak d r^2,\qquad \mathfrak d>1
 \text{ squarefree},\qquad
 \frac{(\sqrt b-\sqrt a)^2}{2}=m-r\sqrt{\mathfrak d}.
\]

If the ratio of two such numerators is rational, comparison in the
quadratic or biquadratic field forces the same primitive ray. Equality
of normalized reciprocal frequencies also forces the same \(k\).
Hence at fixed real \(X\), at most one primitive nonsquare ray is
exactly resonant. Its modes divide one integer \(\Lambda\), and their
complete absolute contribution is

\[
 \boxed{O_\varepsilon(LX^\varepsilon).}              \tag{79.I}
\]

The norm calculation also gives an ultra-fine inverse statement. Two
distinct metric resonances on one block imply

\[
 R\ll A^5D^2K^7,                                     \tag{79.J}
\]

improved to

\[
 R\ll AD^2K^3                                         \tag{79.K}
\]

in one squarefree field. After \(K\asymp JD/A\), these thresholds are
far beyond \(R\leq L/A\). Exact rigidity closes (79.I) but does not
separate ordinary metric windows.

## Metric-density obstruction

On a frozen populated inner cone that stays strictly inside the
reciprocal interval for \(X\in[Y,2Y]\), let \(\mathcal T\) be the
selected nonsquare triples. Elementary periodic averaging gives

\[
 \frac1Y\int_Y^{2Y}
 \#\left\{\tau\in\mathcal T:\|X\omega_\tau\|\leq c/R\right\}\,dX
 =\frac{2c}{R}\#\mathcal T
 +O\!\left(\frac{\#\mathcal T}{BJ_0}\right),
 \qquad J_0=\sqrt Y.                                  \tag{79.L}
\]

Exact equalities form a measure-zero set, so the baseline may be
strictly metric. With \(\asymp B^2\) geometric primitive rays and
\(\asymp J_0\) reciprocal modes per ray, some \(X\) has

\[
 \gg\frac{B^2J_0}{R}                                  \tag{79.M}
\]

geometric incidences. Mapping (79.M) to the literal energy requires a
populated actual subblock with \(N_{a,b}\geq R\); no new lower-support
or coefficient lower-bound theorem is claimed.

Thus the factor-\(R\) incidence saving is sharp at random density. An
inverse theorem can classify only excess above the baseline. The
density itself still needs the actual complex coefficient and outer
signs.

## Hostile controls and first survivor

The near-square family \(b=a+2\), the Pell family
\(a=s^2,\ b=3t^2=a+2\), and perfect-power metric recurrences all pass
as controls. Rational \(X\) has no exact nonsquare resonance, whereas
arbitrary real \(X\) can make any one nonsquare ray exactly resonant.
Algebraic root spacing is too fine at the active resolution, and
reciprocal inversion only enumerates the same fibers \(p=\ell k\).
The audited Robert--Sargos, Montgomery--Vaughan, Bombieri--Pila, and
Bourgain--Demeter theorems do not match the moving normalized frequency
and complete-symbol hypotheses.

After removing exact centers and (79.H), the first unproved object is

\[
 \sum_{\substack{(a,b),k:\ AJD^3\gg L^3\\
                   0<\|\Lambda/k\|\leq c/R}}
 e\!\left(\frac{b-a}{4}
           -\frac{X(\sqrt b-\sqrt a)^2}{4k}\right)
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(2n+1)
 e\!\left(-\frac{n\Lambda}{k}\right).                \tag{79.N}
\]

A future \(TT^*\), primitive-ray large sieve, or signed discrepancy
theorem must control the density and centered discrepancy together.
Another positive incidence count cannot do so.

## Downstream scope

Round 79 closes exact nonsquare centers and the positive region
\(AJD^3\ll L^3\). It does not close the nonsquare signed energy, full
transposed energy, signed top cone, \(M9\!-\!M2\), \(M9\!-\!M1\),
\(M9\), endpoint uniformity, \(R5\)-Full, or the Gauss-circle exponent.
