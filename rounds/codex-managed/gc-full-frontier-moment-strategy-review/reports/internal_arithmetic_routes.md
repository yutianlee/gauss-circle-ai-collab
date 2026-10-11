# Round 205: internal arithmetic routes and a complete modular completion

Campaign: `gc-full-frontier-moment-strategy-review`. Task:
`internal_arithmetic_routes`. Role: source auditor, selected context.
Date: 2026-09-26, Asia/Shanghai. Starting graph:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: 100 percent analytical/source work;
no mathematical numerical experiments. No shared state was edited.

## 1. Result: exact Kloosterman recognition, but no affordable import

There is an elementary, exact modular completion of the **complete
Round-200 original-t=1 residual correlation**, including both P1 and P2,
to ordinary Kloosterman sums. The modulus is an actual divisor
`q=d/g` of the lower physical denominator, with `g=(d,d')`, rather than
an assumed modulus of size `L^2`. It is squarefree on every live term.
The price is a joint two-dimensional Fourier coefficient carrying the
entire original arithmetic, real square-root phase and literal traces.

The automatic complete Fourier/Cauchy price is `L^(7/2) X^epsilon`,
worse than the direct `L^3 X^epsilon` correlation envelope. On the
legal unit-shift, primitive-frequency part, critical-range
Blomer--Pascadi plus a general matrix decomposition costs
`L^(119/32) X^epsilon`. Even granting favorable Pascadi factorizations
everywhere in that part gives `L^(11/3) X^epsilon`. Neither approaches
the target `L^2 X^epsilon`; exceptional contributions remain explicit.
These are upper prices for specified uses of the theorems, **not lower
bounds for the actual sum or for its actual matrix norm**.

Thus this report advances the import audit from an unspecified kernel to
an explicit kernel with an unaffordable certified coefficient ledger.
Summing its Fourier variables exactly returns the physical source.
No M1/M2 parent or exponent closes. The complete whole-discrepancy
high-value target has a smaller, measured remaining gap and broader
proof scope than any currently affordable internal modular import.

## 2. Exact statement, hypotheses, and full frontier

Write `e(u)=exp(2 pi i u)`. All `X>=2` below are real. In the complete
Round-200 source let `L>=2`, `R=ceil L`, `sigma=+1` or `-1`, and keep
the actual total zero-extended coefficient

\[
b(m,d)=\chi_4(d)\mu^2(md)\rho_{md}(d)
 a^{\mathrm{lit},\sigma}_{L,X}(m,d),\qquad
c_N=\sum_{md=N}b(m,d),\quad z_N=c_Ne(\sigma\sqrt{XN}).
\tag{205.I1}
\]

Here `m,d>0`, `d` is odd, `m,d asymp L`, `4m<d<16m`, and
`1<=m<=H=floor(floor(sqrt X)X^(-1/4))`; every failed predicate makes
`b=0`. The allocation-independent selected opposite-character prime
pair gives
`rho_N(d)=1-1_(p_N|d)-1_(q_N|d)+2 1_(p_N q_N|d)`, and `rho=1`
when no pair is selected. Its density is not assumed. On live support
`|b|<<X^epsilon`; all endpoint conventions remain part of `a^lit`.

The source and target are exactly

\[
C_{\rm even}=\sum_{\substack{0<r<R\\2\mid r}}(1-r/R)
\sum_{d'm'-dm=r}b(m',d')\overline{b(m,d)}
 e\!\left(\sigma\sqrt X(\sqrt{d'm'}-\sqrt{dm})\right),
\tag{205.I2}
\]
\[
Q_R=D+2\Re C_{\rm even}\ll_\epsilon L^2X^\epsilon,
\qquad D=\sum_N|c_N|^2\ll_\epsilon L^2X^\epsilon.
\tag{205.I3}
\]

There is one outside real part. Absolute bounds used below are only
stronger sufficient strategies. They are not the requested statement.

The graph's independent direct parents and their exact quantitative
targets are as follows. Literal coefficient and endpoint qualifiers in
this table are part of each target, not optional decorations.

| Graph owner | Exact target and independent scope |
|---|---|
| `M9` | Fixed-coefficient `M_i(D;X)<<X^(1/4+epsilon)` for both `i=1,2`, uniformly over `X^(1/4)<=D<=X^(1/2)`. |
| `M9-M1` | The actual Vaaler M1 dyadic reciprocal main sum at the quarter scale. Its sole assembly dependency is `M9-M1-physical-one-count-assembly`; its two open blockers are the following HARD and SMOOTH parents. |
| `M9-M1-top-endpoint-signed-cone` (HARD) | Every middle/lower residual shell of the unique hard profile containing `d=floor(sqrt X)` requires `T_(M1,L)=sum_(h asymp L)sum_(4h<n<16h,n odd) chi_4(n)a_(M1)(h,n)e(sqrt(Xhn))<<L^(3/2)X^epsilon`, with actual Phi, W, floors, stars, signs and real-X crossings; already owned terminal and full-second-derivative points are excluded once. |
| `M9-M1-direct-smooth-residual-blockwise-estimate` (SMOOTH) | Every literal smooth physical `(D,L)` label in `U_1` requires `B_1(D,L;X)<<X^(1/4+epsilon)`, with exact Vaaler taper, both frequency signs, denominator profile, height floor, stars/half weights, crossings and real-X boundary convention. The hard profile is excluded. |
| `M9-M2` | Actual `beta_h=alpha_(h,H_D) C_h` M2 dyadic reciprocal sums at the quarter scale; its assembly has three independent open parents TOP, BAL and UNBAL. |
| `M9-M2-top-endpoint-density-discrepancy-energy` (TOP) | With exact row energy `E_L^top=sum_m|R_m|^2`, the complete one-count identity is `E_L^top=E_tilde_owned,L+2Re C_(L,tag)^comp`, `|E_tilde_owned,L|<<L^2X^epsilon`. Require `Re C_(L,tag)^comp<<L^2X^epsilon`. Keep one primitive orientation `h<s`, one outer `2Re`, all complete collared coefficients, density/discrepancy modes, terminal member, exact centres, floors, stars and entry/exit data. This yields only the hard top cone through `|T_end,L|^2<<L E_L^top`. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` (BAL) | On every smooth residual `1<=K/L<=16`, after the fixed smooth gcd decomposition and owned exact/near-square and large-gcd pieces, require `|sum_G G P_G|<<L^(3/2)X^epsilon`, with the modulus outside the G sum and both quarter shifts, character, taper and all literal endpoints retained. |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` (UNBAL) | On every smooth residual `K=XL/D^2`, `M=LK`, `K/L>16`, require `sum_(h asymp L,k asymp K) chi_4(h)a_(L,K)(h,k)e(sqrt(Xhk))<<M^(3/4)X^epsilon`, with slanted actual symbol, both quarter shifts/signs, profiles, floors, stars, entry/exit and transform boundary terms. |
| `M9-endpoint-uniformity` | Every estimate used for M9 must hold throughout `X^(1/4)<=D<=X^(1/2)`, including endpoints and short blocks; its blockers are exactly these five direct analytic parents. |

For M1 the exact residual exponent set is
`U_1={(delta,ell) in Omega: ell<delta-1/4,
178ell+1638delta>463} minus {(1/2,0)}`. The one-count M1 assembly
uses priority R5, terminal divisor theorem, full second derivative,
then TTY. M2 uses R5, terminal T2S, full second derivative, then TTY,
and splits its residual physically into TOP/BAL/UNBAL. These assembly
lemmas are proved conditional implications, not proofs of their parents.

The GAR alternative has a different quantifier. The exact open
`M9-M1-global-angular-radial-estimate` is

\[
\Re\left\{e(1/8)\sum_{n\le16\sqrt X}
C_X^*(n)n^{-3/4}e(\sqrt{Xn})\right\}\ll_\epsilon X^\epsilon.
\tag{205.I4}
\]

`M9-M1-GAR-total-active-equivalence` states
`M_(1,active)^stat=-(4/pi)X^(1/4)G_X+O(log^2 X)`, with inactive
bottom/transform errors separately target-sized. GAR therefore supplies
total active M1 but no individual `B_1(D,L;X)`, blockwise M1 or M9.
Its alternative global bridge still requires complete M2.

Two subordinate quantifier gaps matter. Complete original t=1 leaves
`1<=t<ceil(sqrt L)`, `s>L`, squarefree s in
`M9-M1-hard-top-high-radical-small-t-residual-estimate`, in particular
all remaining t>=2 and their incidences. BAL's critical persistent
`j=1`, `L asymp X^(1/6)` double-far target is
`|E_(B,df)|<<L^3X^epsilon`, with both product and cross-product
differences larger than L. It does not own
`M9-M2-balanced-remaining-label-owner-quantifier-completion`, including
noncritical scales and the exact-square j=2 boundary at K/L=16.

## 3. Derivation and current primary-source audit

### 3.1 Exact modular completion of the full original-t=1 source

Fix a lower denominator d, a divisor `g|d`, and `r=gk` with
`0<gk<R`, k even. Set

\[
q=d/g,\qquad a=d'/g,\qquad (a,q)=1.
\]

The physical determinant equation is exactly

\[
a m'-q m=k,
\qquad m'\equiv k\bar a\pmod q.
\tag{205.I5}
\]

This holds without `(k,q)=1`. The chart is bijective: `(d,g,k,a,m')`
recovers `(d,d',r,m,m')` uniquely. Every live d is odd and squarefree
by `mu^2(md)`, hence so is q. No modulus has been invented.

Here is an explicit bounded extension that avoids assuming a formula
for unspecified sharp traces. Take finite containing integer intervals
`I_a` and `I_m'` for all physical `a=d'/g` and upper m'. Their lengths
are `O(q)` and `O(gq)`, respectively. For residues `x,y mod q`, define

\[
A_{d,g,k}(x,y)=\sum_{\substack{a\in I_a, a\equiv x\ (q)\\
m'\in I_{m'}, m'\equiv y\ (q)}}
b(m',ga)\overline{b(m_0,d)}
e\!\left(\sigma\sqrt X(\sqrt{gam'}-\sqrt{dm_0})\right),
\quad m_0=\left\lfloor\frac{am'-k}{q}\right\rfloor.
\tag{205.I6}
\]

A summand is zero unless both b coefficients are live; positivity is
checked before taking square roots. The arbitrary floor extension is
used only off the modular hyperbola. On `xy=k mod q` its quotient is
already integral, so it agrees exactly with the physical coefficient.
It does not replace any actual endpoint by a rounded endpoint on the
source. There are `O(1)` a lifts and `O(g)` m' lifts, so

\[
|A_{d,g,k}(x,y)|\ll_\epsilon gX^\epsilon.
\tag{205.I7}
\]

The complete `(d,g,k)` contribution is

\[
T_{d,g,k}=\sum_{x\bmod q}^{*}A_{d,g,k}(x,k\bar x).
\tag{205.I8}
\]

For q>1 put

\[
\widehat A(s,t)=q^{-2}\sum_{x,y\bmod q}
A(x,y)e(-(sx+ty)/q),\qquad
S(u,v;q)=\sum_{x\bmod q}^{*}e((ux+v\bar x)/q).
\]

Finite Fourier inversion gives an actual identified arithmetic kernel:

\[
\boxed{T_{d,g,k}=\sum_{s,t\bmod q}\widehat A_{d,g,k}(s,t)S(s,kt;q).}
\tag{205.I9}
\]

The full source is `sum_d sum_(g|d) sum_(k even,0<gk<R)
(1-gk/R)T_(d,g,k)`. Thus every shift, gcd, both orientations, selector,
character and real-X endpoint survives. The q=1 chart is evaluated by
(I8) as its direct finite one-residue sum, with `O(gX^epsilon)` cost;
its entire contribution is `O(L^2X^epsilon)` even without using tighter
support exclusions.

All Fourier factors are priced by Parseval:

\[
\sum_{s,t}|\widehat A(s,t)|^2
=q^{-2}\sum_{x,y}|A(x,y)|^2\ll g^2X^\epsilon.
\tag{205.I10}
\]

Opening S and summing first over s proves, for every integer k,

\[
\sum_{s,t\bmod q}|S(s,kt;q)|^2=q^2\varphi(q).
\tag{205.I11}
\]

Indeed s-orthogonality forces equal unit variables; t then contributes
q regardless of `(k,q)`. Hence positive Fourier/Cauchy closure gives
`|T_(d,g,k)|<<g q^(3/2)X^epsilon`. Summing d, all divisors g, and
`O(L/g)` k values gives

\[
|C_{\rm even}|\ll L^{7/2}X^\epsilon.
\tag{205.I12}
\]

By comparison, (I8) immediately gives `|T|<<gqX^epsilon<<LX^epsilon`
and the direct complete `L^3X^epsilon`. Expanding S in (I9) and
performing Fourier inversion returns (I8) exactly. Recognition is not
cancellation. In particular the original rank-one norm D has not
magically remained rank one in `(s,t)`.

### 3.2 Two current theorem interfaces and their actual costs

Only the following two substantive primary theorem statements were
re-audited, on 2026-09-26. Neither paper is withdrawn at its checked
current record.

**A. Blomer--Pascadi, Theorem 1.1 (1.3), current v1,
27 July 2026.** For integer c, interval lengths at most `N<=c`,
arbitrary product vectors, unit a, and `(m,n,c)=1`, the unnormalized
Kloosterman operator bound is

\[
\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(N^{1/8}c^{-3/32}+N^{5/16}c^{-3/16}
+N^{2/3}c^{-7/18}\right).
\tag{205.I13}
\]

At `N asymp sqrt c` it is `c^(31/32+o(1))` times the product norm.
The gcd restriction can be removed for initial intervals `[1,N]`,
not arbitrary translated intervals. Theorem 5.5 provides different
unequal-length prices; this audit makes no uniform critical-range
claim for those. [Primary theorem](https://arxiv.org/html/2607.24311v1),
[current record](https://arxiv.org/abs/2607.24311).

**B. Pascadi, Theorem 1.2 and Example 1.3, current v2,
21 June 2026.** For `c=dd'e`, `d'|d`, `(d,e)=1`, largest f with
`f^2|cd`, interval lengths `<<c^(1/2+o(1))`, arbitrary product
vectors, unit a and `(m,n,c)=1`, the bound is

\[
\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(f/\min(c,d^2)\right)^{1/6}.
\tag{205.I14}
\]

If `d|c` and `c/d` is squarefree the saving is
`min(d,c/d)^(-1/6)`. Comparable two-prime products and prime squares
give `c^(-1/12)`. Our physical q is squarefree, so only compatible
squarefree factorizations can use this favorable example; prime
squares are excluded by the actual source, despite being valid for
the theorem. [Primary theorem](https://arxiv.org/html/2511.08445v2),
[current record](https://arxiv.org/abs/2511.08445).

Apply these only when `(k,q)=1`, since then
`S(s,kt;q)=S(ks,t;q)`. Retain only the primitive frequency part
`(s,t,q)=1` for this call. Let B denote the matrix
`widehat A(s,t)1_((s,t,q)=1)`. Partition each full residue interval
into consecutive intervals of length at most `ceil(sqrt q)`; there
are `O(q)` rectangular pairs. No physical mask is removed: it remains
in B. For each rectangle J, finite singular-value decomposition gives

\[
\|B_J\|_\pi\le q^{1/4+o(1)}\|B_J\|_{\rm HS},\qquad
\sum_J\|B_J\|_\pi\ll gq^{3/4+o(1)}X^\epsilon.
\tag{205.I15}
\]

The second estimate uses disjoint rectangles and Cauchy over their
`O(q)` Hilbert norms. It is an upper certificate, not a claim of
sharpness for the physical B. The theorem's primitive kernel can be
applied to each product decomposition even if individual products
are not themselves primitive-supported: multiplying the reconstructed
B by the same primitive kernel restores exactly the intended sum.

Consequently A costs `gq^(55/32+o(1))` per `(d,g,k)`, and B costs
`gq^(5/3+o(1))` in its favorable case. The outer d and k sums restore
the following complete ledger.

| Stage/method | Certified upper price, up to epsilon | Required |
|---|---:|---:|
| Original endpoint coefficient norm squared | `L^2` | `L^2` |
| Direct full correlation via physical hyperbola | `L^3` | `L^2` |
| Full Fourier/Cauchy completion, including all k and modes | `L^(7/2)` | `L^2` |
| A on its legal part, after (I15) and positive outer sums | `L^(119/32)` | `L^2` |
| B on a favorable legal part, after (I15) and positive outer sums | `L^(11/3)` | `L^2` |
| Physical nonunit-k complement, estimated directly | at most `L^3` | no target-safe estimate supplied |
| Zero Fourier mode alone, using `S(0,0;q)=phi(q)` | at most `L^3` | no target-safe estimate supplied |
| General nonprimitive Fourier complement by (I10)--(I11) | at most `L^(7/2)` | no target-safe estimate supplied |
| q=1 direct chart | at most `L^2` | sufficient |

The exponents for A/B describe their legal contributions, not bounds
for the complete source with exceptions silently suppressed. Even an
unproved improvement of (I15) to `O(gX^epsilon)` would give about
`L^(3-delta)` under a critical `q^(-delta)` saving, still above L^2.
For the dominant `g=1`, `q asymp L` labels, a rowwise application
would need the averaged rectangle projective mass as small as
`L^(-1+delta+epsilon)`, or a separate compensating signed outer gain.
Neither follows from Parseval. No theorem is imported into the graph.

Reconstruction is also not free. The Round-200 exact window connector
has `|sum_N z_N|^2<<L Q_R`; the stationary M1 multiplier is
`-(2e(1/8)/pi)X^(1/4)L^(-3/2)`. Thus the direct correlation L^3 gives
scalar L^2 and physical `X^(1/4)L^(1/2)`. The target correlation L^2
would give scalar `L^(3/2)` and physical `X^(1/4)`. A saving in a
correlation exponent is halved at the scalar stage, as is the deficit.

### 3.3 Why switching complete parents does not remove the same costs

The graph and one exact direct-parent artifact show independent hard
and first-smooth M1 witnesses near `(delta,ell)=(1/2,1/6)`. Their
accepted direct menu has exponent

\[
\min\left\{a,(1-a)/2,
[89(1+\ell)+819\delta]/1282\right\},\qquad a=\delta-\ell,
\]

which reaches 1/3 separately on each physical parent. Thus each retains
an `X^(1/12)` physical deficit. Finishing the original t=1 correlation
addresses neither the full hard parent nor the independent smooth
parent. GAR recombination avoids blockwise quantifiers but keeps the
full radial signed difficulty and all M2 obligations.

M2 TOP's latest reviewed row split is `E_nu=D_nu+G_nu`, with
`D_nu<<LX^epsilon`; exact physical product collisions are safe.
The remaining unequal-product local form still carries all chirps,
sinc factors, characters and endpoints. Its one-sided off-row target
is equivalent in strength to the original complete local concentration
problem, not supplied by the row diagonal. This does not close full TOP.
BAL likewise retains actual critical double-far energy and separate
remaining-label quantifiers. An arbitrary-coefficient L^4 shadow does
not refute its actual L^3 target.

UNBAL already has a genuine modular/spectral dictionary on a **flat
smooth owner**, not the full parent. With `R_0=X/D`, `K=XL/D^2`,
`Delta=D/L`, and `X=N_0+xi`, its inverse-first completion is

\[
\sum_{g,n\ {m odd},,gn\asymp R_0}\chi_4(g)
 W(X/(gnD))\sum_{h\bmod n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n),
\]

where exactly `S^(chi4)_(infinity,0)(4N_0,h;2n)=chi_4(n)S(N_0,h;n)`
in the fixed weight-one convention. Its h=0 term is target-safe;
the centered joint coefficient remains. Automatic spectral/completion
closure costs `R_0 sqrt(Delta)=X/sqrt(DL)`, whereas the accepted flat
owner envelope is
`min(Delta,sqrt(XL/D)+sqrt(X/(LD)))X^epsilon`.
Complete h summation returns the original reciprocal row. The common
test/common sequence required by scalar spectral tools is unproved
for this joint matrix. The graph's inverse-selector scalarization
obstruction prices a further `K^(1/2-o(1))` nuclear inflation and a
`sqrt(Delta)` residue-compression norm in its exact stated scope.
New all-moduli fixed-c bilinear bounds do not remove that modulus/argument
coupling or control sharp, clipped, starred and transition owners.

### 3.4 Comparison with the complete whole-discrepancy target

For the actual mollified series, retain every coefficient and the
infinite Schwartz tail:

\[
H_T(u)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi u\sqrt n-3\pi/4).
\]

On the fixed displaced radius window, the accepted Round-204 bound is
`D(V)<<T^epsilon(V^(-2)+T V^(-136/13))`. Put
`theta=(3292+25sqrt(1717))/13762`, `beta=2theta-1/2`.
It yields complete twelfth moment `T^(10beta+epsilon)` and sixth-power
norm `T^(5beta+epsilon)`, versus targets `T^(29/25+epsilon)` and
`T^(29/50+epsilon)`. The norm deficit is
`5beta-29/50=0.0648317597...`; it is a deficit in a proved upper bound,
not actual lower mass.

A concrete complete remaining objective is

\[
\int_{\{|H_T(u)|>T^{13/125}\}}w(u/T)|H_T(u)|^{12}\,du
\ll_\epsilon T^{29/25+\epsilon},
\tag{205.I16}
\]

for the same fixed smooth nonnegative displaced window w. The omitted
low-value part is already target-safe: integration of the distribution
bound to `V_0=T^(13/125)` gives
`V_0^10+T V_0^(20/13)=T^(26/25)+T^(29/25)` up to epsilon.
This is an exact complete high-value objective, not a claim that a new
method proves it. A sufficient dyadic tail estimate is
`D(V)<<T^(29/25+epsilon)V^(-12)` in the remaining high-value range;
an integrated estimate can be weaker and is preferable if available.

Unlike original t=1 success, (I16) plus accepted reconstruction would
give a complete sharp twelfth-moment milestone. The Jacobian and
amplitude restore a factor T^7, while the full reconstruction error
is `O(T^(8+epsilon))`. Therefore the sharp moment becomes
`Y^(102/25+epsilon)` and persistence gives `102/325`, a strict
improvement on theta but still not one quarter. Arbitrarily high fixed
target-order moments, with complete arithmetic control, remain the
full-proof route through persistence.

The costed method recommendation is therefore to seek an actual-r2
signed correlation/high-value estimate at (I16), preserving the
oscillatory filter and all tails, rather than launch either completed
Kloosterman scalar import above. Its first unproved estimate is (I16)
itself or a coefficient-sensitive Gram bound implying it. The already
proved physical positive twelve-root majorant obstruction and the
generic aligned-coefficient control must both survive. No claim of
independence, generic diagonal deletion, or positive replacement of
the signed displaced Fourier kernel is licensed.

### 3.5 Versions, withdrawals and a fresh conditional lead

The current records still mark
[Bourgain--Watt 1709.04340v2](https://arxiv.org/abs/1709.04340)
withdrawn (16 July 2023), and
[Dong--Robles--Zeindler 2601.00292v2](https://arxiv.org/abs/2601.00292)
withdrawn (5 January 2026). The latter record identifies an omitted L^2
factor that removes the claimed improvement. Neither is an input here.

The conductor supplied a fresh lead,
[Baier 2609.21195v1](https://arxiv.org/abs/2609.21195), submitted
18 September 2026. Its abstract states a square-moduli large-sieve
improvement at `N=Q^3` conditional on Hooley's hypothesis R*, obtained
through modular square roots and Salié completion. This was only a
dated abstract/version screen, not a third theorem audit. Its
conditionality is already disqualifying for an unconditional import
without proving R*. Moreover (I9) has actual squarefree q and complete
ordinary Kloosterman sums with a joint weight; the source's modular
square root is not the real square-root phase in (I2). No saving is
credited. This is a bounded corpus audit, not an exhaustive literature
claim.

## 4. First doubtful or unproved step

The modular kernel itself is now explicit in (I9). The first failed
positive transfer is an affordable theorem-compatible norm for the
**actual** completed matrix, together with target-safe treatment of
nonunit k and nonprimitive/zero frequencies, or a theorem acting on
the signed d,k aggregate without positive scalarization. The source
theorems are legal on their specified parts; their certified prices
are insufficient. The rough floor extension in (I6) is an explicit
bounded construction, not a claimed optimal extension. A better
extension or weighted matrix theorem is not ruled out.

For the complete whole-discrepancy alternative the first unproved
analytic statement is (I16), at a net twelfth-moment saving of
`10beta-29/25` from the current complete bound. Neither exact
resonance removal nor the accepted supremum supplies this saving.
No source or finite algebra above proves it.

## 5. Controls and outcomes

| Required control | Outcome |
|---|---|
| `complete_source_scope` | Pass: (I5)--(I9) are a bijective decomposition of all of (I2); no P1/P2, orientation, gcd or shift is lost. (I16) uses the full H_T. |
| `actual_arithmetic_coefficients` | Pass: b includes chi4, squarefreeness, selector, literal symbol and every trace. Off-hyperbola floor extension agrees exactly on the physical source. |
| `current_primary_hypotheses` | Pass as audit: two theorem texts checked, integer moduli/units/lengths/product norms/gcd restrictions priced. No complete project import. |
| `withdrawals_and_versions` | Pass for the named records; Baier is conditional metadata only. |
| `all_costs_restored` | Pass: lifts g, normalized DFT q^-2, HS/projective mass, all rectangles, d/k outer sums, exceptions, scalar reconstruction and M1 factor are displayed. |
| `signed_absolute_distinction` | Pass: Q_R requires one real part; all positive prices are sufficient-method envelopes. No upper price is asserted to be an actual lower bound. |
| `independent_gain_frontier` | Report supplies direct algebraic checks; independent statement-only frontier remains the conductor's separate gate. No sibling derivation read. |
| `real_endpoint_uniformity` | Pass for exact identities: X remains real in b and phase; no frozen endpoint or smooth surrogate is substituted. All parents still require endpoint-uniform estimates. |
| `full_proof_scope` | Pass: original t=1 is narrower than full HARD; SMOOTH independent; TOP/BAL/UNBAL and BAL quantifier complement separate; GAR total only; one p=12 gain is not quarter. |
| `no_unproved_import` | Pass: no imported theorem or new graph claim. Completion is candidate finite algebra, and any promotion would need independent seam review. |

Further exact controls: q=1 is separately direct; k need not be a unit
in (I9)--(I11); Fourier zero modes are retained; q cannot be a
nontrivial prime square; inverse Fourier reconstruction gives exact
self-return. These are analytic algebra, not numerical experiments.

## 6. Exact dependencies and artifacts used

The assigned brief and all permitted context were read, with named
graph records extracted rather than treating a truncated full-file
display as the proof state:

1. `protocol.md`.
2. `state/proof_obligations.yml`: all IDs explicitly named in Section 2,
   the accepted full moment node, and the UNBAL curvature, Kloosterman,
   level-four matrix and inverse-selector obstruction nodes used above.
3. `state/active_campaign.yml`.
4. `strategy/round205_full_frontier_strategy_review.md`.
5. `rounds/codex-managed/gc-complete-large-values-duality/synthesis.md`.
6. `strategy/gauss_circle_strategy_checkpoint_round202_2026-09-23.md`.
7. `strategy/gauss_circle_strategy_review_2026-09-23.md`.
8. `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/synthesis.md`.
9. `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/reports/complete_source_analytic_derivation.md`, complete report, especially (200.A1)--(200.A8), (200.A10)--(200.A11), (200.A21)--(200.A26).
10. `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/current_primary_methods_audit.md`, including exact H_T/weight definitions and prior source qualification.
11. `rounds/codex-managed/gc-full-frontier-moment-strategy-review/briefs/internal_arithmetic_routes.md`.

Additional exact evidence artifacts, within the at-most-two-per-parent
allowance:

- M1 direct parents: `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md` (one artifact shared by HARD/SMOOTH).
- M2 TOP: `rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/synthesis.md` (one).
- M2 UNBAL: `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`, source statements, real-centre/completion, scope and control sections; and `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/conductor_round143_level_four_matrix_adjudication.md` (two).
- BAL and GAR: graph statements and already assigned context only;
  no extra artifact was opened.

External primary theorem texts and current records are linked in 3.2.
Withdrawal and Baier records are linked in 3.5. No source card was
modified. No blind packet or sibling report was read. The conductor's
Baier message provided only a lead and its stated conditionality.

## 7. Recommended state effect

**No change** to accepted mathematics, exponents, source cards or
parent statuses. Retain (I9)--(I15) as a bounded, auditable failed
completion/import attempt, with exact coefficient costs. Do not
promote a universal impossibility claim or a lower bound from it.

Prefer the complete arithmetic high-value objective (I16) over an
immediate application of the two scalar Kloosterman theorems. Preserve
every internal route and its endpoint owner. The conductor selects
and freezes the next objective only after this round closes. This task
stops with this report and initiates no successor.
