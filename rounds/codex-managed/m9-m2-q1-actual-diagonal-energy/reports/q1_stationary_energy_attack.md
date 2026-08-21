# Singleton \(q=1\) stationary-energy attack

Campaign: `m9-m2-q1-actual-diagonal-energy`
Round: 103
Task: `q1_stationary_energy_attack`
Role: discovery
Starting graph SHA-256: `902eb43bc0fc72b1c3e080dac5cd89757d17e2eaa1f72d606b89afbecff92935`

## 1. Result

**Complete singleton actual-diagonal lemma.**  On every literal
residual half-open block whose fixed-\(a\) row consists only of \(q=1\),
the complete coefficient satisfies

\[
 \boxed{\qquad
 \mathcal D_1^{\mathrm{act}}
 =\sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.
 \qquad}                                                \tag{103.1}
\]

The proof keeps the full metric member, including its mean, and uses a
complete-Fresnel bounded-variation estimate in the moving reciprocal
variable \(k\).  Fourier expansion of the metric member produces the
*total* reciprocal phase

\[
             \left(\nu-{g\over2}\right){\Lambda_a\over k}.
                                                               \tag{103.2}
\]

Since \(g\) is odd, \(n=|2\nu-g|\geq1\) for every
\(\nu\in\mathbb Z\), including the metric density mode \(\nu=0\).
The centered integral is an actual \(k\)-BV weight, so van der Corput's
second-derivative estimate applies to (103.2) without freezing the
saddle or dropping entry/exit.  It gives

\[
 |F_a(1)|\ll_\varepsilon X^\varepsilon {L^2\over A};            \tag{103.3}
\]

squaring and summing the \(O(A)\) bases proves (103.1).

This is an actual-profile upper bound, not a coefficient-uniform
theorem.  It closes only the singleton input to the fixed-\(a\) Gram.
It does not prove the longer-row Gram, the canonical M2 theorem, any
other M2 packet, \(M9\!-!M2\), \(M9\), endpoint uniformity, or a
Gauss-circle exponent.

## 2. Exact statement and hypotheses

Put \(J=X^{1/2}\), let \(a\asymp A\) be an active odd base, and define

\[
 b=a+2,\qquad
 \delta_a=\sqrt{a+2}-\sqrt a,\qquad
 \Lambda_a={X\delta_a^2\over2},
\]

\[
 I_a=\left({J\delta_a\over2\sqrt a},
            {J\delta_a\over\sqrt{a+2}}\right).        \tag{103.4}
\]

The reciprocal interval is literal and open.  The frozen scales are

\[
 K\asymp {J\over A},\qquad
 G\asymp {L\over A},\qquad
 \rho={AJ\over L^3}>1,
 \qquad L\leq J^{1/2}.                                \tag{103.5}
\]

For one active smooth punctured metric member,

\[
 W_R(t)=\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)e(\nu t),
 \qquad
 0<{c_1\over R}\leq\|t\|\leq {c_2\over R}<\frac12,
 \qquad R\leq N_{a,a+2}\ll G.                       \tag{103.6}
\]

The standard smooth partition gives, for every fixed \(M\),

\[
 |\widehat W_R(\nu)|\ll_M
 {1\over R}\left(1+{|\nu|\over R}\right)^{-M}.      \tag{103.7}
\]

The complete physical and centered integrals are

\[
 \mathfrak C^\circ_{a,a+2,k}(g)
 =g\int_{(a+2)/4}^{a}A^\circ_{ga,g(a+2)}(gu)
 e\!\left(g[ku-J\delta_a\sqrt u]\right)\,du,         \tag{103.8}
\]

\[
 \mathfrak B^\circ_{a,a+2,k}(g)
 =g\int_{(a+2)/4}^{a}A^\circ_{ga,g(a+2)}(gu)
 e\!\left(gk\left(\sqrt u-{J\delta_a\over2k}\right)^2\right)du,
                                                               \tag{103.9}
\]

and the carrier identity is exact:

\[
 \mathfrak C^\circ_{a,a+2,k}(g)
 =e\!\left(-{g\Lambda_a\over2k}\right)
  \mathfrak B^\circ_{a,a+2,k}(g).                  \tag{103.10}
\]

The accepted Round-80 owner gate is literal here.  Its
\(\omega_{a,g}(k)\) is only a harmless fixed smooth dyadic \(k\)-cutoff
with bounded sup norm and total variation.  The actual \(\Phi,q_X,W\)
profiles, floors, stars, fixed physical collars, finite odd-lift
support, and all saddle transitions are in \(A^\circ\).  On \(q=1\),
primitivity is automatic, the square and \(\rho\)-safe owners are
ray/block-level, exact centers are killed by \(W_R(0)=0\), and the two
orientations and their signs form a fixed finite ledger.  The full
moving saddle entry and exit remain in (103.9), and no stationary
leading term is substituted.

The only new analytic interface needed below is the following
complete-Fresnel \(k\)-variation statement, applied to the literal
coefficient.  With \(u=y^2\), set

\[
 r_k={J\delta_a\over2k},\qquad \lambda=gk,
 \qquad
 q_{a,g}(y)=2gy\,A^\circ_{ga,g(a+2)}(gy^2).           \tag{103.11}
\]

Then \(q_{a,g}\) is independent of \(k\), and

\[
 \mathfrak B^\circ_{a,a+2,k}(g)
 =\int_{\sqrt{a+2}/2}^{\sqrt a}
 q_{a,g}(y)e\!\left(\lambda(y-r_k)^2\right)dy.       \tag{103.12}
\]

For the exact actual \(k\)-cutoff and zero extension to (103.4), write
\(B_{a,g}(k)\) for (103.12) times every remaining \(k\)-multiplier
other than \(W_R(\Lambda_a/k)\) and the carrier in (103.10).  Then

\[
 \boxed{\quad
 \sup_{k\in I_a}|B_{a,g}(k)|
 +\operatorname {Var}_{k\in I_a\cap\mathbb Z}B_{a,g}(k)
 \ll_\varepsilon X^\varepsilon V,
 \qquad V:=\sqrt{AL\over J}.
 \quad}                                                \tag{103.13}
\]

This statement is for the actual profile only.  In particular, no
arbitrary bounded \(k\)-sequence is inserted.

## 3. Proof or derivation

First verify (103.13) with all moving geometry present.  The exact
Round-77 factorization
\(A_{ga,g(a+2)}(gy^2)=g^{-3}E_{a,a+2}(g)P_{a,a+2}(y^2)\), together
with \(g\asymp G\), makes every actual profile in (103.11) independent
of \(k\).  Its accepted derivative and fixed-collar bounds give a
complete-Fresnel amplitude norm

\[
 Q_g\ll_\varepsilon X^\varepsilon g\sqrt A.          \tag{103.14}
\]

The two fixed physical collars have \(y\)-width
\(w_g\asymp(g\sqrt A)^{-1}\).  Since \(g\asymp G\) and
\(k\asymp K\),

\[
 \lambda w_g^2\asymp {K\over gA}\asymp {J\over AL}\geq1;       \tag{103.15}
\]

the last inequality follows from \(A\leq L\leq J^{1/2}\) whenever
the lift fibre is nonempty.  Also the exact endpoints of (103.4) give

\[
 k={J\delta_a\over2\sqrt a}\Longleftrightarrow r_k=\sqrt a,
 \qquad
 k={J\delta_a\over\sqrt{a+2}}
 \Longleftrightarrow r_k={\sqrt{a+2}\over2}.          \tag{103.16}
\]

Thus the saddle crosses each collared endpoint once and no equality
mode is silently retained.

The complete-Fresnel BV lemma now gives

\[
 \sup_k|B_{a,g}(k)|+\operatorname {Var}_k B_{a,g}(k)
 \ll {Q_g\over\sqrt{gK}}
 \ll_\varepsilon X^\varepsilon
 {g\sqrt A\over\sqrt{gK}}
 \asymp X^\varepsilon\sqrt{AL\over J}.               \tag{103.17}
\]

For completeness, this lemma is a statement about the whole integral,
not stationary asymptotics.  In the exact Morse coordinate
\(z=\sqrt{gk}(y-r_k)\), an interior piece is a Fresnel convolution at
scale \((gk)^{-1/2}\).  Its supremum and total variation as the monotone
center \(r_k\) moves across the amplitude are bounded by
\(Q_g/\sqrt{gK}\).  On a collar, rescaling by \(y-y_e=w_gs\) leaves
the single parameter \(gkw_g^2\geq1\); the complete incomplete-Fresnel
function and its first parameter derivative are uniformly bounded.
Each collar is crossed once, so it has the same total-variation bound.
The nonstationary complements follow by one integration by parts, and
the sharp open-interval zero extension adds only the two endpoint
suprema.  Smooth dyadic \(k\)-profiles have bounded variation and
preserve the estimate.  This proves (103.13) uniformly through saddle
entry and exit, with no stationary remainder.

Now insert (103.10) and the absolutely convergent Fourier series
(103.6) into the literal finite \(g,k\)-sum.  For one orientation,

\[
 F_{a,R}(1)
 =\mathbf 1_{\mathrm{residual}}
 \sum_{\substack{g\ \mathrm{odd}\\g\in\mathcal G_{a,a+2}}}
 \sum_{\nu\in\mathbb Z}\widehat W_R(\nu)
 \sum_{k\in I_a\cap\mathbb Z}
 B_{a,g}(k)
 e\!\left(\left(\nu-{g\over2}\right){\Lambda_a\over k}\right).
                                                               \tag{103.18}
\]

The accepted sign and orientation are already in \(B_{a,g}\); the
conjugate orientation replaces \(\nu-g/2\) by \(\nu+g/2\) and is
identical after absolute values.  Formula (103.18) is also the carrier
audit: the metric mean \(\nu=0\) is present, but its complete phase is
\(-g\Lambda_a/(2k)\).  No quotient sign or deleted zero mode is being
claimed.

Put \(n=|2\nu-g|\).  Oddness of \(g\) gives \(n\geq1\).  On the exact
moving interval, \(k\asymp K\), \(\Lambda_a\asymp J^2/A\), and

\[
 \left|{d^2\over dk^2}
 \left(\nu-{g\over2}\right){\Lambda_a\over k}\right|
 ={n\Lambda_a\over k^3}\asymp {nA^2\over J}.         \tag{103.19}
\]

The second-derivative estimate, uniformly on every partial
subinterval needed for Abel summation, is

\[
 \sup_{I'\subseteq I_a}
 \left|\sum_{k\in I'\cap\mathbb Z}
 e\!\left(\left(\nu-{g\over2}\right){\Lambda_a\over k}\right)
 \right|
 \ll K\sqrt{nA^2/J}+\sqrt{J/(nA^2)}.                 \tag{103.20}
\]

Partial summation with (103.13) therefore bounds the inner \(k\)-sum
in (103.18) by

\[
 X^\varepsilon\left(\sqrt{ALn}
                 +\sqrt{L/A}\,n^{-1/2}\right).       \tag{103.21}
\]

It remains to audit the entire Fourier series, including tails and the
near-half-integer indices.  From (103.7), \(R\leq G\), and
\(g\asymp G\), splitting at \(|\nu|\leq g/4\) and then at
\(|2\nu-g|\leq g\) gives

\[
 \sum_{\nu\in\mathbb Z}|\widehat W_R(\nu)|
 |2\nu-g|^{1/2}\ll\sqrt G,
 \qquad
 \sum_{\nu\in\mathbb Z}|\widehat W_R(\nu)|
 |2\nu-g|^{-1/2}\ll G^{-1/2}.                       \tag{103.22}
\]

There is no singular term because \(|2\nu-g|\) is an odd positive
integer.  In the possible near-resonant region \(\nu\approx g/2\),
the factor \(R^{-1}(1+G/R)^{-M}\) from (103.7) makes both sums in
(103.22) uniform; the remote tails converge for \(M>3\).

Summing (103.21) with (103.22) gives, for each literal odd lift,

\[
 \sum_\nu|\widehat W_R(\nu)|
 \left|\sum_k B_{a,g}(k)
 e\!\left(\left(\nu-{g\over2}\right){\Lambda_a\over k}\right)
 \right|
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{AL}\sqrt G+\sqrt{L/A}\,G^{-1/2}\right)
 \ll_\varepsilon X^\varepsilon(L+1).                \tag{103.23}
\]

Finally, the finite odd support has \(O(G)\) lifts.  Empty and singleton
fibres are included, and for a nonempty block \(L\geq A\geq1\).  Thus

\[
 |F_{a,R}(1)|\ll_\varepsilon X^\varepsilon G(L+1)
 \ll_\varepsilon X^\varepsilon {L^2\over A}.        \tag{103.24}
\]

The logarithmically many metric members, profiles, and dyadic blocks,
and the finite orientation ledger are absorbed into \(X^\varepsilon\).
There are \(O(A)\) bases, so

\[
 \sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon
 A\left({L^2\over A}\right)^2
 =X^\varepsilon{L^4\over A},                         \tag{103.25}
\]

which proves (103.1).

## 4. First doubtful or unproved step

No mathematical step in the singleton estimate remains unproved after
the complete-Fresnel \(k\)-BV interface (103.13) is checked against the
literal Round-77 symbol.  The first seam requiring independent review is
precisely that interface: every residual \(k\)-dependent multiplier
outside the centered phase must be part of the smooth bounded-BV cutoff
in \(B_{a,g}(k)\), independent of \(k\), or zero on the punctured metric
support.  An unrecorded arbitrary or rapidly varying \(k\)-mask would
invalidate partial summation.  The accepted Round-80 owner gate rules
this out unconditionally: \(\omega(k)\) is explicitly only the fixed
dyadic cutoff; the actual physical profiles, floors, stars, and collars
are in \(q_{a,g}\); the reciprocal-interval extension has exactly two
jumps; the square and safe owners are ray/block-level; and an exact
center is annihilated by \(W_R(0)=0\).

The next genuinely open mathematical step is therefore outside the
singleton: the longer-row complete mode-resolved fixed-\(a\) Gram.  This
proof uses the absence of a half-integral zero frequency only after
freezing \(q=1\) and summing in its reciprocal variable.  It supplies no
nonzero-shift determinant estimate and no implication to the canonical
M2 theorem without the remaining longer-row input.

## 5. Required control tests and outcomes

1. **Literal coefficient and singleton Gram normalization -- passed.**
   The proof estimates \(\sum_a|F_a(1)|^2\) directly, with no Fejer
   shift, determinant, or artificial coefficient.
2. **Exact moving \(k\)-interval -- passed.**  Equations
   (103.4) and (103.16) retain both open endpoints.  Zero extension adds
   only the two endpoint jumps already charged in (103.13).  Empty and
   singleton \(k\)-fibres obey (103.20)--(103.24) trivially.
3. **Finite odd \(g\)-support -- passed.**  No infinite lift sum is
   introduced.  Oddness is used exactly once to prove
   \(|2\nu-g|\geq1\); empty and singleton lift fibres remain literal.
4. **Complete metric density and discrepancy -- passed.**  The exact
   smooth \(W_R\) is Fourier-expanded, and every \(\nu\), including the
   density coefficient \(\widehat W_R(0)\), is bounded by the same
   complete-phase argument.  Neither the mean nor a Fourier tail is
   deleted, and no adjoint reciprocal Poisson step is repeated.
5. **Carrier convention and quotient cancellation -- passed.**
   Equation (103.10) is the exact centered carrier.  The phase in
   (103.18) is \((\nu-g/2)\Lambda_a/k\), not \(\nu\Lambda_a/k\) and not
   an independent quotient-parity sign.  The density mode remains, but
   it has \(n=g\) and is estimated rather than declared absent.
6. **Centered Gaussian, entry/exit, and collars -- passed.**
   Equations (103.11)--(103.17) use the complete Fresnel integral.
   The condition \(gKw_g^2\asymp J/(AL)\geq1\) is exact on every
   nonempty active block, so both saddle entries, exits, and incomplete
   Fresnel transitions satisfy the same BV estimate.  There is no
   stationary-expansion error.
7. **Profiles, floors, stars, signs, orientations, and prior owners --
   passed.**  They remain in \(q_{a,g}\) and \(B_{a,g}\).  For odd
   \(a\), \((a,a+2)=1\).  Also \(a(a+2)\) cannot be a square:
   coprimality would force two positive odd squares differing by two.
   The exact-center puncture and the prior safe/residual half-open
   convention are unchanged.  The conjugate orientation has
   \(|2\nu+g|\geq1\) and the same proof.
8. **Fourier tails -- passed.**  Equation (103.22) treats both
   \(\nu\approx g/2\) and remote \(|\nu|\), using the literal scale
   \(R\leq G\).  No finite Fourier truncation or uncharged tail is used.
9. **Pell \((25,27)\), general near-square, and fourth-power strict
   recurrence -- passed.**  The ray \((25,27)=(5^2,3\cdot3^2)\)
   solves \(s^2-3t^2=-2\), is primitive, and is not a square ray.  For
   \(X=T^4\), \(T=8n\), the integer \(k=T^2/32\) lies strictly in
   (103.4) and
   \[
    {\Lambda_{25}\over k}=2048n^2(26-15\sqrt3).
   \]
   Weyl equidistribution puts infinitely many such values in every
   nonempty fixed strict metric subannulus; with \(L\asymp T^{1/2}\),
   \(\rho\to\infty\).  The estimates (103.13), (103.19), and
   (103.22) are nevertheless uniform in this family and in general
   odd near-square \((a,a+2)\) rays.  Thus recurrence does not obstruct
   the upper bound.  No leading stationary term is used to claim a
   lower bound.
10. **Actual lower-bound gate -- passed by irrelevance.**  A lower
    obstruction is unnecessary because the complete upper bound is
    proved.  No positive-capacity or leading-Gaussian lower claim is
    recorded.
11. **Arbitrary-coefficient and unsigned false shadows -- rejected.**
    The proof requires the actual complete-Fresnel BV estimate
    (103.13).  Multiplying the \(k\)-row by arbitrary phases can destroy
    that variation and conjugate (103.2).  Replacing (103.18) by an
    unsigned \(k\)-sum likewise loses (103.20).  Hence no adversarial or
    unsigned analogue follows.
12. **Energy, \(\rho\), route, and downstream scope -- passed.**
    Equation (103.25) gives the requested \(L^4/A\) for all hard
    \(\rho>1\), not merely bounded \(\rho\).  It closes only the
    singleton sufficient lemma.  The canonical density-discrepancy
    energy, longer-row Gram, other M2 packets, \(M9\!-!M2\),
    \(M9\!-!M1\), \(M9\), endpoint uniformity, and every exponent
    remain outside its implication.

No numerical experiment and no external source were used.

## 6. Dependencies and exact artifacts used

1. `protocol.md`
2. `state/proof_obligations.yml`
3. `state/active_campaign.yml`
4. `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/derivation_packet.md`
5. `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/synthesis.md`
6. `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/reviews/conductor_round102_adjudication.md`
7. `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/centered_integral_variation_attack.md`
8. `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md`
9. `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/primitive_ray_parity_energy_attack.md`
10. `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`
11. `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/synthesis.md`
12. `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`
13. `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/briefs/q1_stationary_energy_attack.md`
14. Live Round-103 conductor seam specifying the complete-Fresnel
    \(k\)-BV interface and requesting its literal carrier, collar,
    Fourier-tail, and endpoint audit.

No sibling Round-103 report, shared synthesis, proof draft, validation
artifact, source card, web result, or computational artifact was used.

## 7. Recommended state effect

**Promote after independent seam review.**  Promote (103.1) as the
complete actual-symbol energy theorem on the residual singleton
\(q=1\) block and close
`M9-M2-primitive-ray-q1-actual-diagonal-energy`.  Record the exact
complete-phase mechanism (103.18): Fourier expansion retains the metric
density, odd lifts prevent a half-integral zero frequency, and the
complete-Fresnel \(k\)-BV theorem licenses second-derivative cancellation
uniformly through both physical collars.

Retain `M9-M2-primitive-ray-fixed-a-actual-Gram` and
`M9-M2-top-endpoint-density-discrepancy-energy` as open, with the
singleton removed as a proved disjoint input.  Do not infer a longer-row
estimate, a canonical M2 theorem, any downstream M9 statement, endpoint
uniformity, or an exponent from this result.
