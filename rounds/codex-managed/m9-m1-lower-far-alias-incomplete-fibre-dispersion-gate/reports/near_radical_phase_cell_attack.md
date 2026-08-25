# Round 141 discovery report: nearest-square cells and exact divisor pairing

Campaign: `m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate`
Task: `near_radical_phase_cell_attack`
Role: discovery
Graph at assignment: `072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0`

## 1. Result: `incomplete_fibre_dispersion_no_go`

There is an exact nearest-square decomposition, and its genuinely
microscopic near-radical part is target-safe.  It does **not** make the
nonresonant complement target-safe.  The first obstruction is exact and
has two compatible forms.

First, if

\[
 k_m=\left\lfloor \sqrt{Nm}+\frac12\right\rfloor,
 \qquad j_m=k_m^2-Nm,
\tag{141.D1}
\]

then

\[
 e(\sqrt{Nm})
 =e\!\left(-{j_m\over k_m+\sqrt{Nm}}\right).
\tag{141.D2}
\]

On every dyadic block \(M\le m<2M\), the exact-radical terms
\(j_m=0\), together with the nonzero microscopic cells

\[
 0<|j_m|\le \sqrt M,
\tag{141.D3}
\]

have total weighted absolute mass \(O_\varepsilon(X^\varepsilon)\),
summed over all blocks.  Thus the target is equivalent to the same sum
restricted by

\[
 |j_m|>\sqrt M.
\tag{141.D4}
\]

However, the nearest-integer phase cell indexed by \(k\) has physical
\(m\)-length \(2k/N\ll R^{-1}<1\) throughout the support.  Hence every
such cell contains at most one integer \(m\).  There is no intra-cell
sum on which signed cancellation can act, and (141.D4) still has the
full \(R^{1/2+o(1)}\) coefficient-blind capacity of the frozen scalar.

Second, exact divisor pairing does not repair this loss.  Write uniquely

\[
 m=2^\nu n,\qquad n\ \hbox{odd},
\]

and, for \(dr=n\), define

\[
 F_\nu(d,r)
 =\mathbf 1_{\{r\ge r_{2^\nu d}+2\}},
 \qquad
 A_\nu(n)=\sum_{dr=n}\chi_4(r)F_\nu(d,r),
\tag{141.D5}
\]

with \(F_\nu=0\) on an empty or profile-zero row.  All floors are
retained in \(r_{2^\nu d}\).  The two far sectors are exactly disjoint:

\[
 F_\nu(d,r)F_\nu(r,d)=0.
\tag{141.D6}
\]

Put

\[
 B_\nu(n)=
 \sum_{dr=n}\chi_4(r)
 \bigl(1-F_\nu(d,r)-F_\nu(r,d)\bigr),
 \qquad
 \sigma_{\chi_4}(n)=\sum_{r\mid n}\chi_4(r).
\tag{141.D7}
\]

Then the exact fibre identity is

\[
 \boxed{
 \sigma_{\chi_4}(n)
 =(1+\chi_4(n))A_\nu(n)+B_\nu(n).}
\tag{141.D8}
\]

Consequently

\[
 \boxed{
 A_\nu(n)
 ={1\over2}\sigma_{\chi_4}(n)
  -{1\over2}B_\nu(n)
  +\mathbf 1_{\{\chi_4(n)=-1\}}A_\nu(n).}
\tag{141.D9}
\]

For \(\chi_4(n)=-1\), both
\(\sigma_{\chi_4}(n)\) and \(B_\nu(n)\) vanish, so pairing gives the
tautology \(A_\nu(n)=A_\nu(n)\).  For \(\chi_4(n)=1\), it replaces the
far coefficient by half the complete coefficient minus half an exact
neither-far central band.  Since

\[
 \sigma_{\chi_4}(n)={r_2(2^\nu n)\over4},
\tag{141.D10}
\]

this is precisely a full-\(r_2\)/central self-return, while the
negative-character far sector survives untouched.  The complete term,
the raw central band, and the untouched far sector all have
\(R^{1/2+o(1)}\) absolute capacity before the Round-140 outer factor.
Thus (141.D9) is not a strict reduction.

The first unproved estimate is the fixed-centre signed bound for the
exact complement (141.D4), equivalently for one of the three exact
pieces in (141.D9) after their cancellations are retained.  Neither
phase-cell multiplicity nor divisor pairing proves it.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\quad 0\le q\le2y,
\]

fix \(0<\rho<1/8\), and retain exactly

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor,
 \qquad D_h=y-L_h-1.
\tag{141.D11}
\]

On each nonempty active row, \(r_h\) is the least positive odd integer
at least \(4Nh/D_h^2\).  Empty and profile-zero rows contribute zero.
Let \(C_V\) be fixed so that \(V_{\rm low}(u)=0\) for \(u>C_V\), and
put

\[
 M_*=C_V{N\over R^2}\asymp R^2.
\tag{141.D12}
\]

Use the disjoint dyadic blocks

\[
 \mathcal I_M=[M,2M)\cap[1,M_*],\qquad M=1,2,4,\ldots.
\tag{141.D13}
\]

For \(m\in\mathcal I_M\), define \(k_m,j_m\) by (141.D1), with the
lower nearest-integer boundary included and the upper boundary excluded:

\[
 k_m-\frac12\le\sqrt{Nm}<k_m+\frac12.
\tag{141.D14}
\]

There are in fact no half-integer ties, because
\(\sqrt{Nm}=k+1/2\) would give the impossible identity
\(4Nm=(2k+1)^2\).  Define

\[
 \begin{aligned}
 \mathcal E_0&=\{m:j_m=0\},\\
 \mathcal E_{\rm mic}&=
  \bigcup_M\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\},\\
 \mathcal E_{\rm nr}&=
  \bigcup_M\{m\in\mathcal I_M:|j_m|>\sqrt M\}.
 \end{aligned}
\tag{141.D15}
\]

These sets are disjoint and exhaust the exact support.  With

\[
 w_N(m)=m^{-3/4}V_{\rm low}(R^2m/N)A_\rho(m),
\tag{141.D16}
\]

the proved statement is

\[
 \sum_{m\in\mathcal E_0}|w_N(m)|
 +\sum_{m\in\mathcal E_{\rm mic}}|w_N(m)|
 \ll_{\varepsilon,\rho,V}X^\varepsilon.
\tag{141.D17}
\]

It follows that

\[
 \mathfrak T_N
 =\mathfrak T_N^{\rm nr}+O_\varepsilon(X^\varepsilon),
\qquad
 \mathfrak T_N^{\rm nr}
 =\sum_{m\in\mathcal E_{\rm nr}}w_N(m)e(\sqrt{Nm}).
\tag{141.D18}
\]

The exact target would require

\[
 \boxed{|\mathfrak T_N^{\rm nr}|\ll_\varepsilon X^\varepsilon.}
\tag{141.D19}
\]

No estimate in this report proves (141.D19).  All statements are uniform
on every real-\(X\) interval on which \(N,y\), and the row floors are
constant.  The finitely many bounded values of \(X\) are absorbed in the
implicit constant.

The pairing identity (141.D8) remains true after multiplication by any
function of \(m=2^\nu dr\).  In particular it may be multiplied by the
real-centre profile, the dyadic block indicator, the nonresonant
indicator in (141.D15), the weight \(m^{-3/4}\), and the phase
\(e(\sqrt{Nm})\).  Thus it is an exact identity for
\(\mathfrak T_N^{\rm nr}\), not merely an unweighted fibre observation.

## 3. Proof and derivation

### 3.1 Exact floor mask and mutual exclusivity

For odd \(r\), minimality of the least odd threshold gives the useful
floor-exact equivalence

\[
 r\ge r_h+2
 \quad\Longleftrightarrow\quad
 r-2\ge {4Nh\over D_h^2}
 \quad\Longleftrightarrow\quad
 (r-2)D_h^2\ge4Nh.
\tag{141.D20}
\]

Indeed, \(r-2\) is odd; if it is at least the real threshold, it is at
least the least odd integer \(r_h\), and the converse is immediate.
This retains the equality case and every floor in \(D_h\).

On a nonempty row, \(D_h\le y-1<y\) and \(N\ge y^2\).  Hence

\[
 {4Nh\over D_h^2}>4h.
\tag{141.D21}
\]

Therefore \(F_\nu(d,r)=1\), with \(h=2^\nu d\), implies

\[
 r>4\,2^\nu d.
\tag{141.D22}
\]

The swapped condition would imply
\(d>4\,2^\nu r\), and the two inequalities cannot hold together.
This proves (141.D6) for all \(q\), including \(q=0\) and \(q=2y\),
and also when one swapped row is empty, since its indicator is then
zero.

### 3.2 Exact nearest-square cells are singletons

The phase cell with nearest integer \(k\) is

\[
 \mathcal C_k=
 \left[{(k-1/2)^2\over N},{(k+1/2)^2\over N}\right)\cap\mathbb N.
\tag{141.D23}
\]

Its underlying real interval has length

\[
 { (k+1/2)^2-(k-1/2)^2\over N}={2k\over N}.
\tag{141.D24}
\]

On the support (141.D12),

\[
 k\le\sqrt{NM_*}+\frac12
 \le \sqrt{C_V}{N\over R}+\frac12,
\]

so \(2k/N\ll_V R^{-1}<1\) once \(X\) is large.  Hence

\[
 \boxed{\#\mathcal C_k\le1.}
\tag{141.D25}
\]

The occupied \(k\)-cells on \(m\asymp M\) lie in an interval of length
\(\asymp\sqrt N\sqrt M\), but only \(O(M)\) of them are occupied.  The
relabeling is highly sparse and supplies no multiplicity cancellation.
Also, (141.D2) follows exactly from

\[
 k_m-\sqrt{Nm}={j_m\over k_m+\sqrt{Nm}}.
\]

The microscopic threshold in (141.D3) corresponds to a genuine phase
width

\[
 |\sqrt{Nm}-k_m|le {\sqrt M\over k_m+\sqrt{Nm}}ll N^{-1/2},
\tag{141.D26}
\]

whereas (141.D4) implies the reverse lower bound
\(\gg N^{-1/2}\), up to fixed dyadic constants.  Thus the endpoints and
width are explicit.

### 3.3 Quadratic-congruence multiplicity

For nonzero \(j\), let

\[
 \rho_N(j)=\#\{k\pmod N:k^2\equiv j\pmod N\}.
\]

For every \(\varepsilon>0\),

\[
 \rho_N(j)ll_\varepsilon
 N^\varepsilon\sqrt{(N,j)}
 \le N^\varepsilon |j|^{1/2}.
\tag{141.D27}
\]

Here is a proof.  For \(p^a\Vert N\), if
\(v_p(j)=2s<a\), every solution has \(v_p(k)=s\); after division by
\(p^{2s}\), there are at most two unit roots for odd \(p\), at most
four for \(p=2\), and \(p^s\) lifts.  If \(v_p(j)\ge a\), the number of
solutions of \(k^2\equiv0\pmod{p^a}\) is
\(p^{\lfloor a/2\rfloor}\le p^{a/2}\).  An odd valuation below \(a\)
gives no roots.  The Chinese remainder theorem now gives

\[
 \rho_N(j)\le4^{\omega(N)+1}\sqrt{(N,j)},
\]

and \(4^{\omega(N)}\ll_\varepsilon N^\varepsilon\).

Throughout the effective range, \(k_m<N\) for all sufficiently large
\(X\).  For fixed \(j\), the map
\(m\mapsto k_m\) injects into the roots counted in (141.D27), since
\(m=(k_m^2-j)/N\).  Consequently

\[
 \#\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\}
 \ll_\varepsilon
 N^\varepsilon\sum_{1\le j\le\sqrt M}j^{1/2}
 \ll_\varepsilon N^\varepsilon M^{3/4}.
\tag{141.D28}
\]

This is the exact phase-cell multiplicity saving.  It reaches precisely
the \(M^{3/4}\) count needed against the weight \(M^{-3/4}\), but only
inside the width (141.D26).

### 3.4 Weighted near-radical bound and all dyadic scales

The divisor bound gives

\[
 |A_\rho(m)|\le\tau(m)\ll_\varepsilon X^\varepsilon.
\tag{141.D29}
\]

Combining (141.D28) and (141.D29), block by block,

\[
 \sum_{\substack{m\in\mathcal I_M\\0<|j_m|\le\sqrt M}}
 m^{-3/4}|V_{\rm low}(R^2m/N)A_\rho(m)|
 \ll_\varepsilon X^\varepsilon
 M^{-3/4}M^{3/4}
 \ll_\varepsilon X^\varepsilon.
\tag{141.D30}
\]

There are \(O(\log X)\) blocks, including \(M=1\); epsilon renaming
absorbs the logarithm.  Thus no small-\(m\) block has been omitted.

For \(j_m=0\), write \(N=Du^2\) with \(D\) squarefree.  Then
\(Nm\) is a square exactly when \(m=Dt^2\), and

\[
 \sum_{j_m=0}m^{-3/4}|V_{\rm low}A_\rho(m)|
 \ll_\varepsilon
 D^{-3/4}X^\varepsilon\sum_{t\ge1}t^{-3/2}
 \ll_\varepsilon D^{-3/4}X^\varepsilon.
\tag{141.D31}
\]

Equations (141.D30)--(141.D31) prove (141.D17) and the exact reduction
(141.D18).

### 3.5 Exact divisor-pairing identity

Because of (141.D6), every ordered factorization \(dr=n\) lies in
exactly one of the first far sector, the swapped far sector, or the
neither-far central sector.  The swapped far coefficient is

\[
 \begin{aligned}
 S_\nu(n)
 &=\sum_{dr=n}\chi_4(r)F_\nu(r,d)\\
 &=\sum_{dr=n}\chi_4(d)F_\nu(d,r)\\
 &=\chi_4(n)\sum_{dr=n}\chi_4(r)F_\nu(d,r)
 =\chi_4(n)A_\nu(n),
 \end{aligned}
\tag{141.D32}
\]

since \(d,r\) are odd and
\(\chi_4(d)=\chi_4(n)\chi_4(r)\).  Adding the three sectors gives
(141.D8).

If \(\chi_4(n)=-1\), the central set is stable under \(d\leftrightarrow
r\), and paired terms have weights
\(\chi_4(r)+\chi_4(d)=0\).  There is no fixed point because such an
\(n\) is not a square.  Therefore

\[
 B_\nu(n)=0\qquad(\chi_4(n)=-1),
\tag{141.D33}
\]

and the complete divisor sum also vanishes.  This proves (141.D9).
Finally, the classical divisor identity

\[
 r_2(m)=4\sum_{a\mid m}\chi_4(a)
\]

contains only odd \(a\), and hence gives (141.D10) for every \(\nu\).

As exact controls, for a supported large prime
\(p\equiv3\pmod4\) with \(F_0(1,p)=1\), one has

\[
 A_0(p)=-1,\qquad \sigma_{\chi_4}(p)=B_0(p)=0.
\tag{141.D34}
\]

Thus the negative-character survivor is genuinely nonzero.  On the
Round-140 prime-square control, \(p\equiv1\pmod4\) and
\(A_0(p^{2a})=a\); then

\[
 \sigma_{\chi_4}(p^{2a})=2a+1,
 \qquad B_0(p^{2a})=1,
\tag{141.D35}
\]

so the sole central diagonal term is exactly the correction required
by (141.D8).  Pairing creates no hidden character cancellation.

### 3.6 Complete weighted \(R\)-power ledger

On \(m\asymp M\), the coefficient-blind mass is

\[
 M\cdot M^{-3/4}X^\varepsilon
 =M^{1/4}X^\varepsilon.
\tag{141.D36}
\]

Since \(M\le M_*\asymp R^2\), the top block has size
\(R^{1/2}X^\varepsilon\).  The ledger for the frozen scalar and for the
Round-140 scalar \(\mathcal P=e(-1/8)N^{1/4}\mathfrak T_N\) is

\[
\begin{array}{c|c|c}
\text{family}&\mathfrak T_N&\mathcal P\\ \hline
\text{target}&R^0X^\varepsilon&R^1X^\varepsilon\\
\text{all terms by modulus}&R^{1/2}X^\varepsilon&R^{3/2}X^\varepsilon\\
\text{exact radicals}&R^0X^\varepsilon&R^1X^\varepsilon\\
\text{nonzero microscopic cells}&R^0X^\varepsilon&R^1X^\varepsilon\\
\text{nonresonant complement by modulus}&R^{1/2}X^\varepsilon&R^{3/2}X^\varepsilon.
\end{array}
\tag{141.D37}
\]

The pieces in (141.D9) are not capacity-smaller.  For the complete
coefficient, the elementary lattice estimate

\[
 \sum_{m\le U}r_2(m)=\pi U+O(\sqrt U)
\tag{141.D38}
\]

shows on any fixed plateau interval \(m\asymp M_*\) that

\[
 \sum m^{-3/4}\sigma_{\chi_4}(n)\asymp M_*^{1/4}\asymp R^{1/2}.
\tag{141.D39}
\]

The exact and microscopic cells remove only \(O_\varepsilon(X^\varepsilon)\)
from this nonnegative mass, by the same proof as (141.D30)--(141.D31).

The raw central band also has matching capacity.  Take \(\nu=0\) and
odd \(d,r\) in a fixed rectangle \(aR\le d,r\le bR\), chosen inside a
plateau of \(V_{\rm low}\) and with \(b/a<4\).  There are
\(\asymp R^2\) ordered pairs; (141.D22) makes both far indicators zero,
and every weight is \(\asymp R^{-3/2}\).  Hence the raw central
incidence mass is \(\asymp R^{1/2}\).  Grouping it into \(B_\nu(n)\)
requires actual signed cancellation; geometry alone does not reduce it.

Likewise, in the untouched \(\chi_4(n)=-1\) sector, the \(\nu=0,d=1\)
row with top-plateau \(r\equiv3\pmod4\) has
\(F_0(1,r)=1\) and raw mass

\[
 \sum_{r\asymp R^2\atop r\equiv3(4)}r^{-3/4}asymp R^{1/2}.
\tag{141.D40}
\]

Removing (141.D3) and exact radicals costs only target size.  Equations
(141.D39)--(141.D40) are modulus capacities, not signed lower bounds.
They prove only that the exact pairing has not produced a target-safe
piece.

### 3.7 Coefficient hypothesis and canonical self-return

The nonresonance condition (141.D4) controls
\(\|\sqrt{Nm}\|\), not the distance of the derivative
\(\sqrt N/(2\sqrt m)\) from an integer.  Since the cells (141.D23) are
singletons, no first-derivative cancellation occurs within a cell.

Moreover, \(A_\rho(m)\) is a discontinuous divisor-incidence sequence.
The only immediate variation estimate on a block is

\[
 \operatorname {Var}_{[M,2M]}A_\rho
 \le2\sum_{M\le m<2M}|A_\rho(m)|
 \ll_\varepsilon MX^\varepsilon,
\tag{141.D41}
\]

which is quantitatively useless for transferring a smooth-coefficient
derivative estimate.  A sufficient blockwise additive-twist input would
have to prove, with the actual mask,

\[
 \sup_{M\le U\le2M}\left|
 \sum_{\substack{M\le m<U\\|j_m|>\sqrt M}}
 A_\rho(m)e(\sqrt{Nm})
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{141.D42}
\]

uniformly with the smooth profile and endpoints.  After multiplication
by \(M^{-3/4}\), (141.D42) is exactly the missing target-scale block
bound, not a consequence of (141.D29) or (141.D41).

Finally, a second stationary transform is invertible here.  For dual
frequency \(z/4\),

\[
 \Psi(m)=\sqrt{Nm}-{mz\over4},\qquad
 m_*={4N\over z^2},\qquad
 \Psi(m_*)={N\over z}.
\tag{141.D43}
\]

Resolving the divisor incidence to make this transform legal returns the
Round-140 reciprocal family.  Completing the divisor fibre instead gives
(141.D10) and the uncontrolled \(B_\nu\) and negative-character pieces
in (141.D9).  Thus neither transform nor pairing supplies a noninvertible
gain.

## 4. First doubtful or unproved step

All algebraic and counting statements through (141.D43) are proved
above.  The first unproved step is exactly (141.D19), or dyadically
(141.D42): signed fixed-centre cancellation for the actual incomplete
coefficient on

\[
 |k_m^2-Nm|>\sqrt M.
\]

The nearest-square relabeling cannot prove it because every \(k\)-cell
has multiplicity at most one.  The exact divisor involution cannot prove
it because:

1. on \(\chi_4(n)=-1\) fibres it is identically blind;
2. on \(\chi_4(n)=1\) fibres it introduces the complete
   \(r_2/4\) square-root twist and an owner-sized central band; and
3. all three resulting raw families retain the \(R^{1/2}\) excess.

Any continuation therefore needs a new fixed-centre additive-twist
theorem for the discontinuous incomplete coefficient, or a genuinely
noninvertible arithmetic mechanism controlling the central and
negative-character survivors.  Invoking the desired radial circle bound
for the complete term would be circular.

## 5. Control tests and outcomes

- `exact_incomplete_fibre_mask_floors_profiles_and_real_centre` — **pass**.
  Equation (141.D20) is equivalent to the least-odd threshold, retains
  equality and all floors, and the argument is uniform in real \(X\),
  \(q=0\), and \(q=2y\).  Empty/profile-zero rows are zero.

- `dyadic_m_range_weight_and_small_m_owner` — **pass**.  The disjoint
  blocks (141.D13) include \(M=1\) and stop only at the literal support.
  Equations (141.D30), (141.D36), and (141.D37) give every weight and
  \(R\)-power.  Small nonresonant blocks remain explicitly in
  \(\mathfrak T_N^{\rm nr}\).

- `chi4_parity_divisor_pairing_and_complete_fibre_comparison` — **pass,
  with no-go outcome**.  The unique decomposition \(m=2^\nu n\), the
  exact disjointness (141.D6), identity (141.D8), negative-character
  blindness, and \(r_2/4\) comparison are proved without replacing the
  mask.

- `phase_cell_definition_width_multiplicity_and_endpoints` — **pass**.
  Equations (141.D14), (141.D23)--(141.D28) give endpoint conventions,
  width \(O(N^{-1/2})\), singleton \(k\)-multiplicity, and congruence
  multiplicity.

- `exact_radical_versus_near_radical_separation` — **pass**.  Exact
  radicals are \(m=Dt^2\); nonzero cells satisfying (141.D3) are
  separately bounded.  Nothing is inferred for the wider complement.

- `nonresonant_complement_target_return` — **fail/open at the first exact
  seam**.  The complement is (141.D18)--(141.D19); modulus gives
  \(R^{1/2}X^\varepsilon\), not the target.

- `fourth_power_rays_and_prime_square_fibres` — **pass as hostile
  controls**.  The character-correct exact-radical fourth-power ray lies
  in (141.D31) and is target-scale, not a lower bound.  Equations
  (141.D34)--(141.D35) show that negative prime fibres and positive
  prime-square fibres survive the pairing exactly.

- `coefficient_variation_or_additive_partial_sum_hypothesis` — **fail/open**.
  Only (141.D41) is available; the needed actual-direction statement is
  (141.D42).  A smooth-amplitude theorem has not been applied to the
  discontinuous coefficient.

- `canonical_transform_self_return_and_circularity` — **pass as no-go**.
  Equation (141.D43) self-returns to the reciprocal phase; completion
  gives (141.D9)--(141.D10), not a saving.  No desired circle estimate is
  used.

- `fixed_centre_signed_directionality` — **pass**.  The only modulus
  arguments are for target-safe discarded sets and capacity controls.
  No capacity statement is called a signed scalar lower bound, and no
  centre average is taken.

- `lower_GAR_and_downstream_scope` — **pass**.  The result concerns only
  the Round-140 grouped far scalar.  It proves no square identity,
  residual deletion, lower GAR, direct blockwise M1 parent, M9-M1, M2
  parent, endpoint theorem, M9, quarter theorem, or exponent change.

## 6. Dependencies and exact artifacts used

The derivation is 100 percent analytical.  It used no numerical or
symbolic experiment, no web theorem, no centre average, and no sibling
Round-141 report.  The exact permitted artifacts used were:

1. `protocol.md`;
2. `state/proof_obligations.yml`, specifically the current entries
   `M9-M1-global-lower-radial-signed-estimate`,
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`, and
   `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction`;
3. `state/active_campaign.yml`;
4. `strategy/conductor_0823_full_proof_strategy.md`;
5. `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/conductor_round140_height_alias_adjudication.md`;
6. `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/synthesis.md`;
7. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/synthesis.md`;
8. `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/blind_statement.md`.

The accepted Round-140 facts used as dependencies are the exact grouped
coefficient, its support and weight, the prime-square and fourth-power
controls, the exact-radical characterization, and canonical self-return.
The new ingredients proved here are the scale-sharp congruence count
(141.D27)--(141.D30) and the floor-exact divisor-pairing identity
(141.D20), (141.D6), and (141.D8)--(141.D9).

## 7. Recommended state effect

Recommend **promote after seam review** only the following narrow facts:

1. the microscopic nearest-square lemma (141.D17)--(141.D18), which
   removes exact radicals and all nonzero cells
   \(|k_m^2-Nm|\le\sqrt M\) at target cost; and
2. the exact pairing obstruction (141.D8)--(141.D10), which proves that
   divisor swapping is blind on \(\chi_4(n)=-1\) and otherwise returns a
   complete \(r_2/4\) term plus an owner-sized central correction.

Retain `M9-M1-global-lower-radial-signed-estimate` as open.  Record the
first surviving owner as (141.D19)/(141.D42), with full
\(R^{1/2+o(1)}\) excess.  Reject any claimed strict reduction obtained by
discarding the central band, the negative-character sector, the wider
near-radical cells, or by treating singleton phase cells as cancellation.
Make no downstream or exponent promotion.
