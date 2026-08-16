# Round 77 conductor adjudication

Campaign: `m9-m2-top-endpoint-actual-symbol-variation`  
Round: 77  
Starting graph SHA-256:
`e14373a05ee7d55258b53f07e18afa33682806add90bee49789208f464e46166`

## Decision

Promote the complete collar-extracted actual-symbol normal form and its
step-two variation as one scoped internal lemma.  The promotion uses the
standard fixed smooth dyadic cutoff and top profile, the accepted
bounded \(C^1\) Vaaler coefficient profile, one fixed smooth collar, and
symmetric finite Poisson summation before the collar is inserted.

The three reports agree on the exact factorisation, the treatment of all
Poisson modes, the moving-collar estimate, and the variation scale.  The
statement-only report identifies the hypotheses and summation convention
that were implicit in the packet.  The hostile report independently
finds no missing power or transition-count factor.  The discovery report
supplies the complete mode sum and centred-Fresnel derivative proof.

The weighted reciprocal resonance union, the transposed energy, the top
cone, \(M9\!-\!M2\), \(M9\), endpoint uniformity, and the global exponent
remain open.

## Exact promoted interface

Let \(J=\sqrt X\), \(1\leq L\leq H\leq J^{1/2}\), and let \(a_L(h,m)\)
be the accepted exact normalized top symbol with its finite odd support,
floors, stars, and fixed profiles.  For odd \(h<s<4h\), remove fixed
physical collars at \(m=\lceil s/4\rceil\) and \(m=h\).  Write uniquely

\[
 h=ga,\qquad s=gb,\qquad (a,b)=1,
 \qquad a,b,g\ \mathrm{odd},
\]

and set

\[
 \delta=\sqrt b-\sqrt a,\qquad
 \Lambda={X\delta^2\over2},\qquad
 \alpha={b-a\over4}-{X\delta^2\over4k}.
\]

For

\[
 {J\delta\over2\sqrt a}<k<{J\delta\over\sqrt b},
\]

retain the complete centred integral

\[
 \mathfrak B_{a,b,k}^{\circ}(g)
 =g\int_{b/4}^{a}A_{ga,gb}^{\circ}(gu)
 e\!\left(g\left[-J\delta\sqrt u+ku
              +{X\delta^2\over4k}\right]\right)du.
\]

If \(g=2n+1\) and \(\mathcal G_{a,b}\) is the actual odd lift interval,
then

\[
\begin{aligned}
 \mathcal O_L={}&2\Re
 \sum_{\substack{a<b<4a\\a,b\ \mathrm{odd}\\(a,b)=1}}
 \sum_k e(\alpha)
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B_{a,b,k}^{\circ}(2n+1)e(-n\Lambda/k)\\
 &\quad+O_{M,\eta,\Phi,W}\!\left(L^2\log(2+L)\right).
\end{aligned}                                           \tag{77.A}
\]

The error includes both full lattice endpoint samples, every removed
collar sample, the zero and positive Poisson modes, and every negative
nonstationary or equality mode.  There is no stationary-expansion
error: all stationary and transition modes remain inside the complete
integral.

Uniformly through either saddle transition,

\[
 |\mathfrak B^{\circ}(g)|
 +g|\partial_g\mathfrak B^{\circ}(g)|
 \ll_{M,\eta,\Phi,W}
 {J\delta\sqrt G\over k^{3/2}},
 \qquad G\asymp {L\over b},                           \tag{77.B}
\]

and hence

\[
 |\mathfrak B^{\circ}(g_{\max})|
 +\sum_{g,g+2\in\mathcal G_{a,b}}
 |\mathfrak B^{\circ}(g+2)-\mathfrak B^{\circ}(g)|
 \ll {J\delta\sqrt G\over k^{3/2}}.                \tag{77.C}
\]

The logarithm in (77.A) is absorbed by \(X^\varepsilon\).

## Proof adjudication

The finite Poisson formula with nonzero endpoints is interpreted as a
symmetric limit.  Once the fixed collars are inserted, the amplitude is
smoothly compactly supported and the transformed series is absolutely
convergent.  The two original endpoint samples and all removed collar
samples have \(O(1)\) capacity per ordered pair, hence \(O(L^2)\) in the
block.

For one collared ordered pair, write

\[
 p(x)={J(\sqrt s-\sqrt h)\over2\sqrt x}.
\]

The curvature scale on the cone is

\[
 -p'(x)\asymp {J(s-h)\over L^2}\geq1.
\]

The fixed collars separate every nonstationary and equality mode from
zero derivative by at least a constant number of curvature units.  A
first-derivative bound for nearby modes and two integrations by parts
for the tails give \(O(\log(2+L))\) per ordered pair.  Negative modes
whose saddle lies in the raw interval are retained exactly, including
saddles inside either collar.

The decisive actual-symbol identity is

\[
 A_{ga,gb}(gu)=g^{-3}E_{a,b}(g)P_{a,b}(u),            \tag{77.D}
\]

where \(P_{a,b}\) contains both exact \(W\)-arguments and \(q_X\) but is
independent of \(g\), while

\[
 |E(g)|\ll1,\qquad |E'(g)|\ll G^{-1}.                \tag{77.E}
\]

The collars depend on \(g\) only through

\[
 \rho\!\left({g(u-b/4)\over M}\right)
 \rho\!\left({g(a-u)\over M}\right).
\]

Finally,

\[
 -J\delta\sqrt u+ku+{X\delta^2\over4k}
 =k\left(\sqrt u-{J\delta\over2k}\right)^2.         \tag{77.F}
\]

In the exact centred coordinate the phase is \(gv^2\), and

\[
 g\partial_g e(gv^2)={v\over2}\partial_v e(gv^2).
\]

Integration by parts transfers the phase derivative to the complete
symbol without a power loss.  The primitive gap \(b-a\geq2\) and
\(L^2\leq J\) make each fixed physical collar at least one stationary
width in the centred coordinate, so the same estimate holds at saddle
entry and exit.  This proves (77.B)--(77.C).

## Hostile and false-analogue controls

For \(X=T^4\), odd \(13\mid T\), \((a,b)=(81,121)\), and
\(k=2T^2/13\), the saddle is \(u_0=169/4\), both actual profile
arguments are \(9/13\) and \(11/13\), and \(\Lambda/k\in\mathbb Z\).
Thus every odd lift is coherent.  The promoted lemma correctly supplies
variation control but no fictitious cancellation.

The analogous theorem for arbitrary bounded lift coefficients is false:
alternating or phase-conjugating coefficients can make step-two
variation comparable to the sum of pointwise masses.  The proof depends
essentially on (77.D)--(77.F).  A sharp uncollared ceiling also remains a
separate step-four object; its parity is not silently folded into the
step-two theorem.

## Downstream scope

Discrete Abel now gives the lawful pointwise ray bound

\[
 \left|\sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^{\circ}(2n+1)e(-n\Lambda/k)\right|
 \ll {J\delta\sqrt G\over k^{3/2}}
 \min\!\left(N_{a,b},{1\over2\|\Lambda/k\|}\right).
\]

Summing this coefficient-weighted quantity over primitive pairs and
reciprocal modes is the next obligation.  The present round does not
authorize absolute summation over that union and does not change the
global exponent.
