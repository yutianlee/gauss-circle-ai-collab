# Blind rederivation: lower-radial phase diagram

## 1. Result

**Exact phase-diagram lemma and residual no-go.**  Put
\[
 a_\nu={1-\nu\over2},\qquad
 b_\nu={552-89\nu\over1816},
 \qquad \nu_0={356\over819}.                              \tag{1}
\]
For a fixed power-scale radial block \(N=X^\nu\),
\(0\le\nu\le1/2\), the stationary relation maps every actual
denominator exponent to
\[
 \ell=\delta+{\nu-1\over2},
 \qquad a_\nu\le\delta\le{1\over2}.                       \tag{2}
\]
The left endpoint has \(L=X^\ell=O(1)\) at exponent resolution and must
be read with its exact support and floors; all strict interior points
have \(L\to\infty\).

The accepted inputs close precisely the following block exponents:
\[
 \begin{aligned}
 \mathcal C_{\rm term}
 &=\{(\nu,\delta):\nu=1/2, 1/4\le\delta\le1/2\},\\
 \mathcal C_{\rm TTY}
 &=\{(\nu,\delta):\nu_0\le\nu\le1/2,
        a_\nu\le\delta\le b_\nu\},\\
 \mathcal C_{V2}&=\{(0,1/2)\}.                            \tag{3}
 \end{aligned}
\]
Round 60 independently covers the same full critical slice \(\nu=1/2\)
for fixed smooth sectors.  The TTY onset is the exact rational point
\[
 (\nu,\delta,\ell)
 =\left({356\over819},{463\over1638},0\right),             \tag{4}
\]
but this is only the onset of **partial scale coverage**, not a closed
radial sector.

For \(0\le\nu\le1/2\), the blockwise uncovered set on the fixed radial
slice is
\[
 \mathcal U_\nu=
 \begin{cases}
 \varnothing,&\nu=0,\\
 [a_\nu,1/2],&0<\nu<356/819,\\
 (a_\nu,1/2],&\nu=356/819,\\
 (b_\nu,1/2],&356/819<\nu<1/2,\\
 \varnothing,&\nu=1/2.
 \end{cases}                                               \tag{5}
\]
At \(\nu=0\) the formal active slice degenerates to the V2 point; at
\(\nu=1/2\) it is the terminal line.  For every
\(0<\nu<1/2\), however, the top denominator block
\[
 (\delta,\ell)=\left({1\over2},{\nu\over2}\right)         \tag{6}
\]
is actual and uncovered.  Consequently the only fully closed fixed-power
radial exponents are \(\nu=0\) and \(\nu=1/2\).  There is no isolated
“first” missing exponent: descending from the critical sector, an
uncovered block occurs for every \(\nu<1/2\), however close to \(1/2\);
ascending from the V2 endpoint, one occurs for every \(\nu>0\).  Thus
the first genuinely uncovered radial band at power resolution is the
entire open band
\[
 \boxed{0<\nu<1/2.}                                       \tag{7}
\]

The exact missing theorem is
\[
 B_1(X^\delta,X^{\delta+(\nu-1)/2};X)
 \ll_\varepsilon X^{1/4+\varepsilon}
 \quad ((\nu,\delta)\in\mathcal U_\nu).                   \tag{8}
\]
Relative to TTY its exponent deficit is
\[
 s_{\rm TTY}(\nu,\delta)
 ={1816\delta+89\nu-552\over2564}>0,                      \tag{9}
\]
while the terminal estimate has deficit
\[
 s_{\rm term}(\nu)={1-2\nu\over4}.                        \tag{10}
\]
The accepted V2 estimate also supplies, away from its closed endpoint,
the deficit
\[
 s_{V2}(\nu,\delta)=
 \min\left\{\delta-{1\over4},{\nu\over4}\right\}.          \tag{11a}
\]
Thus the exact saving required over the best currently accepted bound is
\[
 s_*(\nu,\delta)=\min\{s_{\rm term}(\nu),
                       s_{\rm TTY}(\nu,\delta),
                       s_{V2}(\nu,\delta)\}.               \tag{11b}
\]

## 2. Exact statement and hypotheses

Let a fixed smooth radial multiplier be supported on
\(n\asymp N=X^\nu\), \(0\le\nu\le1/2\).  Let a smooth denominator
profile have \(d\asymp D=X^\delta\),
\(1/4\le\delta\le1/2\), and let
\[
 H_D=\lfloor D/R\rfloor,
 \qquad R=X^{1/4}.
\]
All comparability constants are fixed independently of \(X\).  A block
is called exponent-active if its exact stationary support contains an
integer \(h\) with \(1\le h\le H_D\); at a zero exponent the assertion
means only \(O(1)\) scale and is subject to the exact support constants.

Use only the packet's accepted estimates:
\[
 B_1(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L),           \tag{12}
\]
\[
 B_1(D,L;X)
 \ll_\varepsilon
 X^{[89(1+\ell)+819\delta]/1282+\varepsilon},             \tag{13}
\]
the V2 estimate whose gap from target is (11a), including its closed
endpoint \((\delta,\ell)=(1/2,0)\), and the separate Round-60 closure of
fixed smooth critical sectors.  The physical target for each localized
block is \(R X^\varepsilon=X^{1/4+\varepsilon}\).

At smooth-cutoff level, (12)--(13) must be stable under fixed normalized
amplitudes and the Mellin twists described below, with constants of at
most polynomial growth in the Mellin parameter.  Exact floors, the
one-sided top profile and hard value \(d=\lfloor\sqrt X\rfloor\), and
all prescribed stars remain part of their original blocks.  They may
change constants or bounded-height terms but are not deleted from the
exponent diagram.

Under these hypotheses, (2)--(5) are the exact exponent coverage union.
Full closure at a fixed \(\nu\) means coverage of every nonempty
denominator profile in \([a_\nu,1/2]\), not merely existence of one
closed \(\delta\).

## 3. Proof and derivation

### Stationary map and active support

The stationary equation gives the exact positive root
\[
 h={d\sqrt n\over2\sqrt X}.                                \tag{14}
\]
If \(n\in[\alpha N,\beta N]\) and
\(d\in[\kappa D,KD]\) on fixed smooth supports, then
\[
 \kappa\sqrt\alpha,L\le h\le K\sqrt\beta,L,
 \qquad L={D\sqrt N\over2\sqrt X}.                        \tag{15}
\]
The factor \(1/2\) matters for bounded-height support but not for its
power exponent.  Taking base-\(X\) exponents proves
\[
 \ell=\delta+{\nu-1\over2},
 \qquad \nu=1-2\delta+2\ell.                              \tag{16}
\]

The lower condition \(h\ge1\) gives \(\ell\ge0\), hence
\(\delta\ge a_\nu\).  At equality, (15) has only boundedly many integer
heights and may be empty for particular support constants; if nonempty,
it is a bounded-height endpoint owned by the corresponding accepted
estimate.  For \(\delta>a_\nu\), \(L\to\infty\).

For growing \(H_D\),
\[
 {L\over D/R}={1\over2}X^{(\nu-1/2)/2}.                   \tag{17}
\]
Thus \(L\ll H_D\) for \(\nu<1/2\), and \(L\asymp H_D\) for
\(\nu=1/2\).  Equivalently, the formal upper condition
\(\ell\le\delta-1/4\) is precisely \(\nu\le1/2\), already assumed.
Together with \(\delta\le1/2\), this proves the active interval (2).
When \(\delta=1/4\), \(H_D=O(1)\); (2) then forces
\(\nu=1/2\), so this bounded-height corner belongs to the accepted
critical closure.  A zero floor makes it empty, while a positive bounded
floor is handled directly.  Floors shift no positive power exponent.

### Translation of the three accepted estimates

From the definition of \(L\),
\[
 {D\over L}=2\sqrt{X/N}=2X^{(1-\nu)/2}.                   \tag{18}
\]
Hence (12) reaches \(X^{1/4+\varepsilon}\) exactly when
\((1-\nu)/2\le1/4\).  In the permitted range this means
\(\nu=1/2\), or equivalently
\(\ell=\delta-1/4\).  This proves \(\mathcal C_{\rm term}\).

Substitution of (16) in the TTY target gives
\[
 \begin{aligned}
 178\ell+1638\delta\le463
 &\iff1816\delta+89\nu\le552\\
 &\iff\delta\le b_\nu.                                   \tag{19}
 \end{aligned}
\]
The interval \([a_\nu,b_\nu]\) is nonempty exactly when
\[
 {1-\nu\over2}\le{552-89\nu\over1816}
 \iff \nu\ge{356\over819}.                               \tag{20}
\]
Equality in (20) gives (4).  At the critical endpoint,
\[
 b_{1/2}={1015\over3632},                                  \tag{21}
\]
so TTY covers only the low-\(\delta\) portion there, although the
terminal/Round-60 input closes the entire critical slice.

Finally,
\[
 (\delta,\ell)=(1/2,0)
 \overset{(16)}{\Longleftrightarrow}\nu=0.                \tag{22}
\]
At \(\nu=0\), (2) itself degenerates to \(\delta=1/2\), so the V2
endpoint closes the entire bounded radial slice.  For any \(\nu>0\),
the top point is instead (6), and V2 does not apply.

### Union, residual corridor, and required saving

For \(\nu<1/2\), the strict inequality
\(\ell<\delta-1/4\) in the packet's residual corridor holds
automatically.  Its TTY-failure condition is, by (19),
\(\delta>b_\nu\).  Removing the sole V2 point and treating the critical
line separately yields exactly (5).

The TTY exponent after substitution is
\[
 \theta_{\rm TTY}(\nu,\delta)
 ={1816\delta+89(1+\nu)\over2564}.                         \tag{23}
\]
Subtracting \(1/4=641/2564\) gives (9).  Equation (18) gives the
terminal exponent \((1-\nu)/2\), hence (10).  The accepted V2 exponent
ledger gives (11a).  All three deficits are positive on
\(\mathcal U_\nu\), so (11b) is the exact improvement over the best
currently accepted estimate.  The V2 gap vanishes at the sole point
\((\nu,\delta)=(0,1/2)\), in agreement with (22), and hence changes no
coverage set.

For a single improvement uniform in \(\delta\) on a fixed residual
slice, the largest required deficit still occurs at the hard top
\(\delta=1/2\), since each nonconstant entry of (11b) is nondecreasing
in \(\delta\).  There
\[
 s_{V2}(\nu,1/2)={\nu\over4},
 \qquad
 \max_{\delta\in\mathcal U_\nu}s_*(\nu,\delta)
 =\min\left\{{\nu\over4},{1-2\nu\over4}\right\}.          \tag{24a}
\]
The TTY deficit at the top is never smaller than this minimum.  The two
displayed alternatives cross at \(\nu=1/3\): V2 is the best top-block
baseline for \(0<\nu\le1/3\), and the terminal estimate is best for
\(1/3\le\nu<1/2\).  Near the critical endpoint the remaining top block
needs only \((1-2\nu)/4=(1/2-\nu)/2\) over (12), but it is still a
genuine positive saving for every fixed \(\nu<1/2\).

### Smooth multiplier, scale sum, and endpoints

For a smooth radial multiplier \(V(n/N)\), stationary substitution is
handled exactly by
\[
 V\!\left({4Xh^2\over d^2N}\right)
 ={1\over2\pi}\int_{\mathbb R}\widehat V(t)
 \left({4X\over N}\right)^{it}h^{2it}d^{-2it}\,dt.       \tag{26}
\]
Here \(\widehat V\) is Schwartz.  Every fixed derivative of
\(d^{-2it}\), and every sampled variation of \(h^{2it}\) on
\(h\asymp L\), costs only a polynomial in \(1+|t|\), which is integrable
against \(\widehat V\).  Therefore an accepted weighted form of
(12)--(13) loses no power of \(X\).  Formula (26) is exact: the smooth
radial cutoff creates no sharp radial endpoints and no approximation
error by itself.  Any B-process remainder must nevertheless be uniform
with these polynomial Mellin losses.

There are \(O(\log X)\) denominator profiles; this is absorbed once into
\(X^\varepsilon\).  The one-sided top profile and the hard integer
\(d=\lfloor\sqrt X\rfloor\) remain at \(\delta=1/2\), which is why (6)
cannot be discarded as an endpoint of measure zero.  Profile stars,
stationary half-weights, height floors, and any independent radial star
retain their separate ownership.  They affect bounded endpoint terms,
not inequalities (16), (19), or the power deficits (9)--(11).

## 4. First doubtful or unproved step

The stationary exponent map, active interval, three coverage sets,
boundary rationals, residual slices, and required-saving formulas follow
algebraically from the packet and have no remaining doubtful step.

The first genuinely unproved mathematical step is (8) on the residual
corridor.  It is already exposed at the hard top (6) for every
\(0<\nu<1/2\).  Neither choosing a lower denominator scale that TTY
does close nor summing only the closed scales proves a radial-sector
estimate, because the one-sided top profile is an actual separately
owned contribution.

There is also an interface seam if one seeks a complete transformed
theorem rather than only the phase diagram: the packet does not state
termwise smooth-Mellin uniformity or a quantitative total for all
B-process, hard-top, floor, and star remainders.  Equation (26) shows
that the multiplier itself costs only integrable polynomial
\(t\)-weights, but an accepted transform must supply corresponding
uniform remainder bounds of total size \(O(RX^\varepsilon)\).  This
does not change the uncovered set; it limits what can be promoted beyond
the blockwise diagram.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| stationary_exponent_map | **Pass.** Equations (14)--(16) give \(\ell=\delta+(\nu-1)/2\) and its inverse exactly. |
| active_support | **Pass.** For fixed \(\nu\), the exponent-active scales are \(a_\nu\le\delta\le1/2\); (17) verifies the upper-height condition. |
| floor_small_height | **Pass with endpoint qualification.** \(\ell=0\) and \(\delta=1/4\) are bounded-scale statements, so exact constants decide emptiness; nonempty bounded terms remain owned by TTY, V2, or the critical input as specified. |
| terminal_translation | **Pass.** Equation (18) reaches the \(R\)-target only at \(\nu=1/2\). |
| TTY_translation | **Pass.** It becomes \(1816\delta+89\nu\le552\), with onset \((356/819,463/1638)\). |
| V2_translation | **Pass.** The endpoint maps only to \((\nu,\delta)=(0,1/2)\). |
| union_over_delta | **Pass.** Equations (3) and (5) distinguish partial block coverage from full radial-slice closure. |
| scale_sum | **Pass.** The \(O(\log X)\) denominator scales cost one \(X^\varepsilon\), not an additional power. |
| transform_errors | **Multiplier pass; transform-total seam.** Mellin separation (26) is exact and all fixed-order twist losses are integrable.  A global transformed claim still needs the accepted remainders, hard top, floors, and stars to total \(O(RX^\varepsilon)\). |
| first_uncovered_band | **Pass/no-go.** Every \(0<\nu<1/2\) has the uncovered actual top block (6); \(356/819\) is only the onset of partial TTY coverage. |
| required_saving | **Pass after V2 correction.** Equations (9)--(11b) give the exact best-menu blockwise deficit.  At the hard top it is \(\min\{\nu/4,(1-2\nu)/4\}\), with crossover \(\nu=1/3\), as in (24a). |
| downstream_scope | **Pass.** No full GAR, M9-M1, M9, or Gauss-circle exponent is inferred. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The stationary relation, exponent ranges, terminal estimate, TTY
   estimate, V2 endpoint, residual corridor, external normalization, and
   critical-sector statement contained in the authorized Round-61
   packet.
2. Elementary algebra, floor inequalities, dyadic scale counting, and
   Mellin inversion for a fixed compactly supported smooth multiplier.

Isolation ledger:

- Read only
  `rounds/codex-managed/m9-m1-lower-radial-phase-diagram/briefs/blind_lower_radial_rederivation.md`
  and
  `rounds/codex-managed/m9-m1-lower-radial-phase-diagram/derivation_packet.md`.
- Incorporated the conductor-authorized correction that the accepted V2
  failed bound has gap
  \(\min\{\delta-1/4,\nu/4\}\); no additional artifact was opened.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  other Round-61 reports, validation matrices, or shared proof state.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared-state edit.

## 7. Recommended state effect

**Promote the exact phase diagram; retain the open-band obstruction.**
Promote (2)--(5), including the TTY onset
\((356/819,463/1638,0)\), and record that only the endpoint slices
\(\nu=0\) and \(\nu=1/2\) are fully closed by the listed inputs.  Do not
describe the TTY radial projection \([356/819,1/2]\) as full radial
coverage: for every subcritical exponent its high-\(\delta\) scales,
including the hard top, remain.

Retain (8) on \(\mathcal U_\nu\) as the next blockwise obligation, with
the exact best-menu savings (9)--(11b) and hard-top maximum (24a).
Before promoting a transformed radial theorem, separately certify the
smooth-Mellin uniformity and total hard-top/floor/star/error ledger.
Make no downstream state change toward full GAR, M9-M1, M9, or the final
Gauss-circle exponent.
