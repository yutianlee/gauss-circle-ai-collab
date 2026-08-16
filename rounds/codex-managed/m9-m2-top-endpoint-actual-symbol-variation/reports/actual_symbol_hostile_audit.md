# Round 77 hostile audit: complete odd-lift actual symbol

## 1. Result

The proposed actual-symbol interface survives the hostile audit, with two
minor statement corrections and no loss of a power of \(G,L,J\), or \(k\).

First, (77.9) is an exact finite Poisson formula only when the sum over
\(\nu\) is interpreted in the standard symmetric (equivalently, a lawful
Cesaro) sense.  After the fixed collars in (77.12) are inserted, the
extended integrand is smooth and compactly supported, and its Poisson
series is absolutely convergent; this convention issue then disappears.
Both half-endpoint samples belong to the removed primal collar.

Second, the constants in (77.16) and (77.18) also depend on the one fixed
cutoff \(\rho\).  With that dependence displayed, one has the stronger
aggregate identity

\[
 \boxed{
 \mathcal O_L=\mathcal O_{L,\mathrm{stat}}^\circ
 +O_{M,\rho,\eta,\Phi,W}\!\left(L^2\log(2X)\right).}
 \tag{A77.1}
\]

The essential point is that every negative Poisson integral whose raw
saddle lies in the affine interval is retained **exactly** inside
\(\mathfrak B^\circ\).  There is consequently no stationary expansion and
no omitted lower stationary correction to sum.  The zero and positive
modes and the negative modes outside the raw saddle interval cost
\(O(\log(2X))\) per ordered pair; there are \(O(L^2)\) pairs.  Modes whose
saddles meet either endpoint are harmless because the fixed collar creates
a derivative gap of size

\[
 \gg {J\over L^2}\ge 1.
\]

The complete centred integral also satisfies, uniformly on every actual
odd lift interval,

\[
 \boxed{
 |\mathfrak B^\circ(g_{\max})|
 +\sum_{g,g+2\in\mathcal G_{a,b}}
 |\mathfrak B^\circ(g+2)-\mathfrak B^\circ(g)|
 \ll_{M,\rho,\eta,\Phi,W}
 {J(\sqrt b-\sqrt a)\sqrt G\over k^{3/2}}.}
 \tag{A77.2}
\]

Thus (77.18) holds without needing its \(X^\varepsilon\) allowance.  The
actual property that makes this true is an exact factorisation after
\(h=ga,s=gb,x=gu\): all two \(W\)-profiles become independent of \(g\),
the dyadic and Vaaler factors vary on the lift scale \(G\asymp g\), and
the centred phase is the exact quadratic

\[
 -J\delta\sqrt u+ku+{X\delta^2\over4k}
 =k\left(\sqrt u-{J\delta\over2k}\right)^2.             \tag{A77.3}
\]

The fixed collar is at least one stationary width wide because
\(k/L\gg J/L^2\ge1\).  This controls the complete and incomplete Fresnel
transitions and their \(g\)-derivatives at the same scale as the interior
Gaussian.  An arbitrary bounded coefficient sequence has none of these
properties and does not satisfy (A77.2).

The exact fourth-power half-integer family passes as a resonance control,
not as a counterexample to the variation theorem: its centred symbol has
the size and variation in (A77.2), while its odd-lift phase is fully
coherent.  Nothing here estimates the resulting resonance union or proves
the energy bound.

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi iz}\), \(J=\sqrt X\),
\(y=\lfloor J\rfloor\), \(q_X=X/y^2\), and let
\(1\le L\le H\le J^{1/2}\).  Use the accepted real top symbol (77.1),
with the usual fixed dyadic seminorms

\[
 \|\eta_L^{(j)}\|_\infty\ll_j L^{-j},
\]

the accepted \(C^1\) endpoint extension of \(\Phi\), and the fixed smooth
profile \(W\).  Only finitely many fixed seminorms of \(W\), \(\eta\), and
\(\rho\) are used.  Let \(M\ge1\) and \(\rho\) be fixed as in (77.12).
All implicit support constants are fixed.

For every ordered odd pair \(h<s\le4h\) in the actual support, define

\[
 C=J(\sqrt s-\sqrt h),\qquad A=\lceil s/4\rceil,
 \qquad B=h,
\]

and let \(F(x)=A_{h,s}(x)e(-C\sqrt x)\).  Then

\[
 \sum_{m=A}^{B}F(m)
 ={F(A)+F(B)\over2}
 +\lim_{R\to\infty}\sum_{|\nu|\le R}
   \int_A^B F(x)e(-\nu x)\,dx.                          \tag{A77.4}
\]

If the interval degenerates to one point, the right side is understood in
the evident limiting sense and equals \(F(A)\).  Define

\[
 Q_{h,s}(x)=A_{h,s}(x)
 \rho\!\left({x-s/4\over M}\right)
 \rho\!\left({h-x\over M}\right),                       \tag{A77.5}
\]

extended by zero to the real line.  It is \(C_c^\infty\) in \(x\) for the
fixed profiles used here, so ordinary Poisson applies absolutely.  The
difference between the original lattice sum and the lattice sum with
\(Q_{h,s}\) is supported on

\[
 0\le m-\lceil s/4\rceil\le 2M+1
 \quad\hbox{or}\quad 0\le h-m\le2M+1.                    \tag{A77.6}
\]

For the unique primitive representation

\[
 h=ga,\qquad s=gb,\qquad (a,b)=1,\qquad g,a,b\text{ odd},
\]

put \(\delta=\sqrt b-\sqrt a\), and let

\[
 {J\delta\over2\sqrt a}<k<{J\delta\over\sqrt b}.        \tag{A77.7}
\]

Then (77.13) is the exact negative-mode integral after its stationary
phase \(e(-gX\delta^2/(4k))\) has been removed, and (77.15) is an exact
reindexing of all negative modes satisfying (A77.7).  Uniformly in this
range, (A77.1) and (A77.2) hold.  Equality in either endpoint of (A77.7)
is assigned to the error in (A77.1); the collar makes this assignment
uniform.

The conclusion is about the normalized off-diagonal energy only.  The
physical prefactor from the top-\(M2\) transform is excluded, exactly as in
the packet.

## 3. Proof or derivation

### Endpoint formula and collar ownership

Apply Poisson to \(F(x)\mathbf 1_{[A,B]}(x)\).  At an integer jump, Fourier
inversion returns the average of the two one-sided values.  Hence the
Poisson side equals the starred sum

\[
 {F(A)\over2}+\sum_{A<m<B}F(m)+{F(B)\over2},
\]

which proves (A77.4).  This also shows why both, rather than only one, of
the endpoint samples must be restored.

At every integer where either factor in (A77.5) is not one, (A77.6)
holds.  The actual symbol is uniformly bounded on the affine cone because
\(h,s,m\asymp L\) there and all fixed profiles are bounded.  There are
\(O(L^2)\) ordered pairs and \(O_M(1)\) collar lattice points per pair.
Consequently the two endpoint samples, the whole sharp-ceiling stratum,
the upper stratum, and all incomplete-Fresnel endpoint pieces have total
absolute capacity

\[
 O_{M,\rho,\eta,\Phi,W}(L^2).                             \tag{A77.8}
\]

The cutoff uses the real affine distance \(x-s/4\), not
\(x-\lceil s/4\rceil\).  Thus the retained symbol contains no
\(g\bmod4\) ceiling term.  The discrepancy caused by

\[
 \left\lceil{gb\over4}\right\rceil
 ={gb\over4}+{1\over2}+{\chi_4(gb)\over4}
\]

is wholly inside (A77.8).  Since \(q_X-1\ll J^{-1}\) and
\(s\ll L\le J^{1/2}\), the fixed lower collar is also wider than the
\(q_X-1\) displacement of the profile edge.  No substitution \(q_X=1\)
has been made.

### Exact mode decomposition and aggregate error

Let

\[
 I_\nu(h,s)=\int_{\mathbb R}Q_{h,s}(x)
 e(-C\sqrt x-\nu x)\,dx,
 \qquad D(x)={C\over2\sqrt x}.
\]

The function \(D\) is positive and decreasing.  On the collar-retained
support, \(x\asymp L\), while

\[
 D(x)\asymp {J(s-h)\over L},\qquad
 |D'(x)|\asymp {D(x)\over L}.                             \tag{A77.9}
\]

The amplitude in (A77.5) has uniformly bounded \(L^1\) first and second
derivative norms.  Its interior derivatives cost powers of \(L^{-1}\);
the only \(O(1)\)-scale derivatives occur on two fixed-width collars, so
their \(L^1\) costs are still \(O_M(1)\).

For \(\nu\ge0\), the derivative of the phase is \(-D(x)-\nu\) and never
vanishes.  For \(\nu=-k<0\), it is \(k-D(x)\).  A saddle lies in the raw
affine interval precisely when

\[
 D(h)<k<D(s/4),                                           \tag{A77.10}
\]

which is exactly (A77.7).  If \(k\le D(h)\) or \(k\ge D(s/4)\), the
distance from \(k\) to the derivative range on the retained support is,
for the nearest possible alias, at least

\[
 \min\{D(h-M)-D(h),\ D(s/4)-D(s/4+M)\}
 \gg_M {J(s-h)\over L^2}\gg_M1.                         \tag{A77.11}
\]

Here \(s-h\ge2\) and \(L^2\le J\).  The monotone first-derivative bound,
summed by distance from the two endpoints of the interval (A77.10), gives
a harmonic \(O(\log(2X))\) loss.  Two integrations by parts give an
absolutely summable tail once the alias distance exceeds the derivative
range.  Therefore, uniformly for one ordered pair,

\[
 \sum_{\nu\ge0}|I_\nu(h,s)|
 +\sum_{\substack{k\ge1\\k\notin(D(h),D(s/4))}}
 |I_{-k}(h,s)|
 \ll_{M,\rho,\eta,\Phi,W}\log(2X).                       \tag{A77.12}
\]

This estimate includes zero modes, positive modes, negative
nonstationary modes, the two equality cases in (A77.10), and saddle
entry/exit modes removed by the fixed collars.

For a mode in (A77.10), substitute \(h=ga,s=gb,x=gu\).  Its integral is

\[
 I_{-k}(ga,gb)
 =e\!\left(-{gX\delta^2\over4k}\right)
 \mathfrak B_{a,b,k}^\circ(g).                            \tag{A77.13}
\]

Also

\[
 (-1)^r=e\!\left({g(b-a)\over4}\right).
\]

With \(g=2n+1\), multiplication of (A77.13) by this character factor gives

\[
 e(g\alpha)\mathfrak B^\circ(g)
 =e(\alpha)\mathfrak B^\circ(2n+1)
   e(-n\Lambda/k),                                       \tag{A77.14}
\]

because \(e(2\alpha)=e(-\Lambda/k)\).  The primitive representation is
unique, so summing (A77.14) gives exactly (77.15), with no gcd
multiplicity or transition-count factor.  Summing (A77.12) over
\(O(L^2)\) pairs and adding (A77.8) proves (A77.1).  In particular, all
stationary corrections are already present in the exact integral
\(\mathfrak B^\circ\); none is estimated term by term.

### Exact actual-symbol factorisation

For \(x=gu\), direct substitution into (77.1) gives

\[
 A_{ga,gb}(gu)=L^3g^{-3}P_{a,b}(g)Q_{a,b}(u),             \tag{A77.15}
\]

where

\[
\begin{aligned}
 P_{a,b}(g)={}&
 \eta_L(ga)\eta_L(gb)
 \Phi\!\left({ga\over H+1}\right)
 \Phi\!\left({gb\over H+1}\right),\\
 Q_{a,b}(u)={}&(ab)^{-3/4}u^{-3/2}
 W\!\left(\sqrt{{q_Xa\over4u}}\right)
 W\!\left(\sqrt{{q_Xb\over4u}}\right).
\end{aligned}                                             \tag{A77.16}
\]

Complex conjugates may be retained in (A77.16) with no change to the
estimates.  The actual fixed profiles are real.  This identity is the
decisive protection against the arbitrary-coefficient analogue: both
\(W\)-arguments and \(q_X\) are exactly independent of \(g\).

On an active lift interval,

\[
 a\asymp b,\qquad g\asymp G\asymp {L\over b},\qquad
 |P(g)|\ll1,\qquad |P'(g)|\ll G^{-1}.                     \tag{A77.17}
\]

The derivative bound follows from \(a/L,b/L\asymp G^{-1}\) for the
dyadic factors and from
\(a/(H+1),b/(H+1)\ll G^{-1}\), since \(L\le H\), for the two \(\Phi\)
factors.  It remains valid at the \(\Phi\)-edge because the accepted
extension is \(C^1\), with \(\Phi(1)=\Phi'(1)=0\).

Writing

\[
 R_g(u)=\rho\!\left({g(u-b/4)\over M}\right)
         \rho\!\left({g(a-u)\over M}\right),
\]

one obtains the exact form

\[
 \mathfrak B^\circ(g)
 =L^3g^{-2}P(g)
  \int_{b/4}^{a}Q(u)R_g(u)e(g\psi_k(u))\,du,              \tag{A77.18}
\]

where (A77.3) holds.  No leading stationary value has replaced the
integral.

### Uniform complete-Fresnel variation

Put \(t=\sqrt u\), \(t_0=J\delta/(2k)\), and

\[
 \widetilde Q(t)=2tQ(t^2).
\]

On the active interval \(t\asymp\sqrt b\), fixed profile seminorms give

\[
 |\partial_t^j\widetilde Q(t)|\ll_j b^{-(5+j)/2}.          \tag{A77.19}
\]

The phase is \(gk(t-t_0)^2\).  Its stationary width in \(t\) is

\[
 w=(gk)^{-1/2}.                                           \tag{A77.20}
\]

The collar transition has \(t\)-width

\[
 w_c\asymp_M {1\over g\sqrt b},
 \qquad {w_c\over w}\asymp_M\sqrt{{k\over gb}}.          \tag{A77.21}
\]

The saddle condition and \(b-a\ge2\) imply

\[
 k\gg {J\over b},\qquad {k\over gb}\asymp {k\over L}
 \gg {J\over L^2}\ge1.                                  \tag{A77.22}
\]

Thus every continuous collar transition is at least one stationary width
wide.  Moreover \(g\partial_gR_g\) has the same fixed symbol bounds as
\(R_g\), since on a transition
\(g(u-b/4)\asymp_M1\) or \(g(a-u)\asymp_M1\).

For completeness, split the exact quadratic integral into
\(|t-t_0|\le2w\) and dyadic annuli outside it.  The central interval costs
\(O(b^{-5/2}w)\).  On each outer annulus integrate with

\[
 {1\over4\pi i gk(t-t_0)}{d\over dt}e(gk(t-t_0)^2).
\]

Two integrations sum the annuli.  If a saddle crosses a collar, (A77.21)
keeps the differentiated collar symbol at this same scale; if the other
collar is far from the saddle, repeated integration gives an additional
power of \(k^{-1}\).  Differentiating in \(g\) is also harmless: the phase
term can be integrated by the exact identity

\[
 \partial_g e(gkz^2)
 ={1\over2g}\left({d\over dz}\{z e(gkz^2)\}-e(gkz^2)\right),             \tag{A77.23}
\]

and the boundary term is zero because of the flat collars.  The same
annular argument treats a collar far from \(z=0\).  Consequently

\[
 \left|\int \widetilde Q(t)R_g(t^2)e(gk(t-t_0)^2)dt\right|
 +g\left|{d\over dg}\int
   \widetilde Q(t)R_g(t^2)e(gk(t-t_0)^2)dt\right|
 \ll b^{-5/2}(gk)^{-1/2}.                                \tag{A77.24}
\]

This is a complete-Fresnel estimate, uniform when the saddle is inside a
collar, entering it, leaving it, or in the flat interior.

Combining (A77.17), (A77.18), and (A77.24) yields

\[
 |\mathfrak B^\circ(g)|+g|\partial_g\mathfrak B^\circ(g)|
 \ll L^3g^{-5/2}b^{-5/2}k^{-1/2}
 \asymp \sqrt{{gb\over k}}.                              \tag{A77.25}
\]

By (A77.7),

\[
 \sqrt b<{J\delta\over k}<2\sqrt a\asymp\sqrt b,
\]

so the last member of (A77.25) is equivalent, up to fixed cone constants,
to

\[
 {J\delta\sqrt g\over k^{3/2}}.                          \tag{A77.26}
\]

The actual lift interval has length \(O(G)\) and \(g\asymp G\).  Applying
the fundamental theorem of calculus on each step \(g\to g+2\), and using
the endpoint term at \(g_{\max}\), proves (A77.2).  There is no lost
factor \(N_{a,b}\), no \(O(\log L)\) transition count, and no extra power
of \(G\).

### Hostile actual-profile families

For \(X=T^4\), odd \(13\mid T\), \((a,b)=(81,121)\), and
\(k=2T^2/13\), one has

\[
 t_0={13\over2},\qquad u_*=t_0^2={169\over4},\qquad
 {b\over4}<u_*<a.
\]

At the saddle the two \(W\)-arguments are exactly \(9/13\) and \(11/13\),
and

\[
 {\Lambda\over k}=13T^2\in\mathbb Z.
\]

The lift phase is therefore coherent.  Equations (A77.24)--(A77.26)
still give the claimed variation; Abel correctly returns its full
\(N_{a,b}\) factor through (77.19).  This control confirms that (A77.2)
does not smuggle in character cancellation.

There is an equally explicit nonresonant actual-profile perturbation.
Keep the same \(T,a,b,k\), but take

\[
 X=T^4+{k\over8}=T^4+{T^2\over52}.                        \tag{A77.27}
\]

Then \(y=T^2\) for large \(T\), the saddle remains strictly interior, and

\[
 {\Lambda\over k}=13T^2+{1\over4}.                       \tag{A77.28}
\]

Because \(q_X=X/T^4\) and \(u_*=X/k^2\), the two actual profile arguments
remain **exactly** \(9/13\) and \(11/13\).  This tests a genuinely
nonresonant family without freezing \(q_X\) or altering \(W\).  At the
\(\Phi\)-edge, take the terminal lifts of the same primitive ray with
\(gb\) approaching \(H\).  The \(b/(H+1)\ll G^{-1}\) derivative in
(A77.17), together with \(\Phi(1)=\Phi'(1)=0\), gives the same variation
bound and no terminal loss.

## 4. First doubtful or unproved step

The first literal gap in the packet is (77.9): an unqualified
\(\sum_{\nu\in\mathbb Z}\) is not an unordered absolutely convergent
series when the endpoint values are nonzero.  Formula (A77.4) supplies
the required symmetric summation convention.  This is not a false sign
or endpoint coefficient.

After that convention is fixed, the first genuinely unproved step in the
packet is the aggregate assertion (77.16).  A pointwise leading
stationary formula would not prove it.  The repair above does not use such
a formula: it first removes the full primal collar, applies ordinary
Poisson to the resulting compact smooth amplitude, retains every
raw-stationary negative mode as the exact centred integral, and proves
the summed nonstationary estimate (A77.12).  This closes the gap with the
stronger error (A77.1).

The next missing derivation was the variation theorem.  Equations
(A77.15)--(A77.26) close it.  The key step that would fail for a different
symbol is (A77.15): without exact \(g\)-independence of the two rescaled
\(W\)-profiles and the scale-\(G\) derivative bound for \(P(g)\), an
arbitrary multiplier could make the variation \(N_{a,b}\) times larger.

No doubtful power-saving step remains inside the frozen actual-symbol
interface.  The first open step after it is the coefficient-weighted sum
over the reciprocal resonance union; that step is expressly outside this
round.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| External normalization | **Pass.**  The audit starts with the normalized \(a_L\) and \(\mathcal O_L\).  No physical factor from the top transform is inserted.  The Gaussian \(e(1/8)\) is internal to the exact integral, not a second external factor. |
| Full endpoint samples | **Pass with convention correction.**  Equation (A77.4) contains both half-endpoint samples.  They and all endpoint Fresnel pieces lie in the grouped collar (A77.8). |
| Fixed collar capacity | **Pass.**  Width \(2M+O(1)\) at two endpoints over \(O(L^2)\) pairs costs \(O_M(L^2)\).  No growing stationary-width collar is used. |
| Actual symbol and support | **Pass.**  Equation (A77.15) retains \(\eta_L,\Phi,W,q_X\) exactly.  The finite odd support is retained through \(\mathcal G_{a,b}\).  The primitive representation is unique. |
| All Poisson modes | **Pass.**  Raw-stationary negative modes give (77.15) exactly.  Zero, positive, negative nonstationary, and equality modes satisfy (A77.12). |
| Stationary error sum | **Pass by exact retention.**  There is no truncated stationary expansion.  Every Gaussian correction and incomplete-Fresnel term of a retained mode is inside \(\mathfrak B^\circ\). |
| \(g\)-derivative and variation | **Pass.**  Equations (A77.15)--(A77.26) prove the step-two variation at the proposed scale, with no extra \(G,L,J,k\), or transition-count factor. |
| Saddle entry and exit | **Pass.**  The exact quadratic lemma (A77.24) is uniform through both collars.  The inequality \(k/L\gg J/L^2\ge1\) makes each collar at least one stationary width wide. |
| Sharp ceiling modulo four | **Pass after primal extraction.**  The real-affine cutoff puts the complete \(\lceil gb/4\rceil-gb/4\) discrepancy in (A77.8).  The bulk symbol is genuinely step two; no step-four channel remains in it. |
| Half-integer actual profile | **Pass as a resonance obstruction.**  The \((81,121)\) fourth-power family has \(W(9/13)W(11/13)=1\), coherent phase, and the variation (A77.2).  It receives no false nonresonant saving. |
| Nonresonant and \(\Phi\)-edge families | **Pass.**  The perturbation (A77.27) has exact phase distance \(1/4\) and unchanged plateau arguments.  At the terminal \(\Phi\)-edge, (A77.17) and \(\Phi(1)=\Phi'(1)=0\) prevent an \(H/L\) or endpoint loss. |
| Rank-one self-return | **Pass as a stopping control.**  No second Poisson transform is counted as a gain.  The lift phase remains linear after centering, so exact resonances remain for the later union estimate. |
| Coefficient adversary | **Pass / false analogue rejected.**  Multiplying the lift symbol by arbitrary signs can make its step-two variation \(N_{a,b}\) times the right side of (A77.2).  The proof uses the actual factorisation (A77.15), scale-\(G\) derivative (A77.17), and centred quadratic (A77.3), none of which arbitrary coefficients possess. |
| Downstream scope | **Pass.**  The result proves only the collar-extracted identity and actual-symbol variation.  It does not estimate the resonant primitive-pair/\(k\) union, the off-diagonal energy, the top cone, \(M9\!-\!M2\), \(M9\), or the Gauss-circle exponent. |

No numerical computation or external theorem was used.  The audit was
entirely algebraic and analytic.

## 6. Dependencies and exact artifacts used

Campaign: m9-m2-top-endpoint-actual-symbol-variation.  Task:
actual_symbol_hostile_audit.  Role: hostile seam reviewer.  Starting graph
SHA-256: e14373a05ee7d55258b53f07e18afa33682806add90bee49789208f464e46166.
Generated: 2026-08-16T12:14:46+08:00.

The exact repository artifacts used were:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/derivation_packet.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/briefs/actual_symbol_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reviews/conductor_round76_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/signed_offset_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/blind_near_product_energy_rederivation.md;
- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md.

No Round-76 discovery report, sibling Round-77 report, proof draft,
validation matrix, source card, web source, or legacy response was read.
The accepted mathematical dependencies are the exact transposed energy,
the Round-76 odd-lift parity correction, the fixed primal-collar capacity,
the accepted \(C^1\) regularity of \(\Phi\), and the fixed smooth profile
seminorms stated above.

## 7. Recommended state effect

**Revise the wording, then promote the actual-symbol identity and
variation interface.**

Record (77.9) with symmetric Fourier summation, include \(\rho\) among the
fixed implied-constant dependencies, and replace the unproved error
ledger by the stronger bound (A77.1).  Promote (77.15)--(77.18) as the
complete collar-extracted actual-symbol theorem under the explicit fixed
profile seminorm hypotheses in Section 2.  The exact properties carrying
the theorem are (A77.15), (A77.17), and the centred quadratic identity
(A77.3).

Retain the fourth-power family as a permanent hostile control: it shows
that the promoted variation theorem gives coefficient control but no
cancellation on resonance.  Retain the arbitrary-coefficient analogue as
rejected.  Do not promote the resonance-union estimate, the off-diagonal
energy, M9-M2-top-endpoint-signed-cone, M9-M2, M9, endpoint uniformity, or
the global exponent.  The next lawful obligation is still the
coefficient-weighted primitive-pair/reciprocal-mode union with the
step-two distance \(\|X(\sqrt b-\sqrt a)^2/(2k)\|\).
