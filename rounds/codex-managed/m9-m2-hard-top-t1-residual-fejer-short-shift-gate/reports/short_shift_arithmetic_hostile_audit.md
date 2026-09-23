# Round 165 hostile audit: arithmetic fibres in the residual Fejer shift

## 1. Result

The literal additive opening has an exact, multiplicity-one common-divisor
decomposition, but the two most immediate sources of cancellation disappear
*inside each resulting fibre*.  More precisely, if

\[
 d=gu,\qquad d'=gv,\qquad (u,v)=1,\qquad r=gh,
\tag{165.H1}
\]

then the base row lies in one residue class modulo

\[
 K=guv,
\tag{165.H2}
\]

and may be written

\[
 N_t=A+Kt,\qquad N_t+r=A+r+Kt.
\tag{165.H3}
\]

The character product on the whole fibre is the constant

\[
 \chi _4(d')\chi _4(d)=\chi _4(uv).
\tag{165.H4}
\]

Equivalently, in tangent coordinates (d'=d+a), (m'=m+b), one has

\[
 db+ma+ab=r,
 \qquad a\equiv0\pmod2,
 \qquad \chi _4(d')\chi _4(d)=(-1)^{a/2}.
\tag{165.H5}
\]

Thus a fixed gcd fibre or a fixed tangent-offset fibre contains no long
\(\chi _4\)-sum.  The square-root phase along (165.H3) has

\[
 \phi_{g,h,u,v}''(t)\asymp \frac{Jh}{gL}=:\lambda_{g,h},
 \qquad \lambda_{g,h}\gg1,
\tag{165.H6}
\]

on every fixed smooth physical cell.  A one-dimensional Poisson or
\(B\)-process followed by absolute values of its dual saddles has capacity

\[
 T\sqrt{\lambda_{g,h}}+\lambda_{g,h}^{-1/2}
\tag{165.H7}
\]

for a fibre of length (T\ll g).  Since \(\lambda_{g,h}\gg1\), this is
no better than the trivial (T).  Splitting into parity or squarefree
congruence subprogressions does not improve this positive ledger: a step
\(q\) changes ((T,\lambda)) to ((T/q,q^2\lambda)), leaving

\[
 \frac{T}{q}\sqrt{q^2\lambda}=T\sqrt\lambda.
\tag{165.H8}
\]

This proves the following smallest route-scoped no-go:

\[
 \boxed{\texttt{positive\_gcd\_tangent\_fibre\_no\_go}.}
\tag{165.H9}
\]

Namely, decomposing the literal correlation into individual gcd or tangent
progressions and then taking a positive norm over the progressions, over
their one-dimensional phase duals, over parity classes, or over
squarefree/Mobius openings cannot by itself prove the (L^2X^\varepsilon)
Fejer target.  It destroys the only remaining character and inter-fibre
signs and restores the (L^3X^\varepsilon) correlation capacity.

The no-go is deliberately restricted to those placements.  It does not
exclude a signed sum over the dual frequencies, cancellation between
different ((g,h,u,v)), a joint (r,N) transform, a delta/spectral
formula, or another actual-coefficient theorem.

There is also one surviving actual sector.  If
\(\mathfrak C^{\rm rem}_{\ge G}\) denotes the complete literal divisor
opening restricted only by ((d,d')\ge G), then

\[
 \boxed{
 |\mathfrak C^{\rm rem}_{\ge G}|
 \ll_\varepsilon \frac{L^3}{G}X^\varepsilon
 \qquad(1\le G\ll L).}
\tag{165.H10}
\]

Consequently, for every fixed \(\gamma>0\), the owner-complete sector
((d,d')\ge\gamma L) is target-safe:

\[
 |\mathfrak C^{\rm rem}_{\ge\gamma L}|
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{165.H11}
\]

This sector retains both selector statuses, both parity branches,
squarefreeness, profiles, hard endpoints, zero extension, and the exact
phase.  The complement (g<\gamma L), where the progression length may
be short and the number of fibres large, remains open.

The recommended terminal assessment from this report is
`hard_top_t1_residual_fejer_no_go`, unless a sibling report proves the
missing signed low-gcd aggregate.  This is not a lower bound for the
physical coefficient and not a disproof of the frozen target.

## 2. Exact statement and hypotheses

Retain

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H\le J^{1/2},
\tag{165.H12}
\]

and set (R=\lceil L\rceil).  Every shell, cone, floor, star, profile,
endpoint, point value, parity branch, and zero-extension convention is the
literal one inherited by the accepted residual coefficient.

It is useful to expose one divisor without changing that coefficient.
For an odd divisor (d\mid M_N), define

\[
 \alpha_N(d)=
 \mathbf 1_{N\in\mathcal I_L^{\rm lit}}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}
 \rho_N(d)A_N(d),
\tag{165.H13}
\]

and set it to zero for every other pair ((N,d)).  Here (A_N(d)) is
the complete real literal amplitude and \(\rho_N\) is the accepted
neither/both residual indicator, or (1) on a no-pair row.  Then

\[
 c_N^{\rm rem}=\sum_{d\ {\rm odd}}\chi _4(d)\alpha_N(d).
\tag{165.H14}
\]

The exact correlation is therefore

\[
\begin{aligned}
 \mathfrak C_{R,J,L}^{\rm rem}
 ={}&\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_{\substack{d,m,d',m'\ge1\\d,d'\ {\rm odd}\\d'm'-dm=r}}
 \chi _4(d')\chi _4(d)\,
 \alpha_{d'm'}(d')\alpha_{dm}(d)\\
 &\hspace{42mm}\times
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\end{aligned}
\tag{165.H15}
\]

Every nonzero term in (165.H15) has

\[
 d,d',m,m'\asymp L,
\tag{165.H16}
\]

with constants fixed by the literal shell and near-square cone.  The
amplitudes in one opened term are bounded by (X^\varepsilon) (in fact by
a fixed constant apart from harmless divisor notation).  No absolute
value is part of (165.H15).

For a nonzero term, put (g=(d,d')), (d=gu), and (d'=gv).  Since
(d,d') are odd divisors of supported squarefree rows, (g,u,v) are odd,
((u,v)=1), and the squarefree support further forces the relevant
pairwise coprimalities.  The equation in (165.H15) forces (g\mid r);
write (r=gh).  Choose any integral solution of

\[
 v m'_0-u m_0=h.
\tag{165.H17}
\]

All solutions are then

\[
 m_t=m_0+vt,\qquad m'_t=m'_0+ut,
\tag{165.H18}
\]

and (165.H3) holds with (A=gu m_0) and (K=guv).  Equivalently, the
two congruences

\[
 N\equiv0\pmod{gu},\qquad N\equiv-r\pmod{gv}
\tag{165.H19}
\]

have exactly one solution modulo \({\rm lcm}(gu,gv)=guv\).  This is the
literal multiplicity-one CRT decomposition; choosing another particular
solution merely translates (t).

The parity ledger is also exact.  Since (g,u,v) are odd,

\[
 m'_t-m_t\equiv h\equiv r\pmod2.
\tag{165.H20}
\]

Increasing (t) by one flips both complementary parities.  For even
(h), the fibre alternates between odd/odd and even/even rows; for odd
(h), it alternates between odd/even and even/odd rows.  Passing to one
fixed parity branch replaces (t) by a step-two progression.  It does
not alter (165.H4).

## 3. Proof or derivation

### 3.1 Literal multiplicity, gcd coordinates, and tangent coordinates

Equation (165.H14) opens each supported divisor exactly once.  Multiplying
the two divisor sums and using (N=dm), (N+r=d'm') proves (165.H15)
with multiplicity one.  Taking the gcd of the two odd divisors proves
(d=gu,d'=gv,(u,v)=1), and division by (g) gives (165.H17).  The
standard solution formula for a primitive linear Diophantine equation
proves (165.H18)--(165.H19).

Because (g) is odd,

\[
 \chi _4(d')\chi _4(d)
 =\chi _4(gv)\chi _4(gu)
 =\chi _4(g)^2\chi _4(uv)
 =\chi _4(uv),
\tag{165.H21}
\]

which proves that the character is constant in (t).  This conclusion
survives every parity split.

The tangent form gives a second exact view of the same loss of character.
Put (a=d'-d), (b=m'-m).  Since (d,d') are odd, (a=2k), and direct
expansion gives

\[
 r=db+ma+ab.
\tag{165.H22}
\]

For odd (d), \(\chi _4(d+2k)=(-1)^k\chi _4(d)\), proving (165.H5).
For fixed (a,b,r) with (a\ne0), the remaining variables satisfy

\[
 a m=r-b(d+a),\qquad bd\equiv r\pmod a.
\tag{165.H23}
\]

Writing \(\delta=(a,b)\), solutions exist only if \(\delta\mid r\), and
the admissible (d)'s occupy one residue class modulo \(|a|/\delta\),
before oddness and the literal support are imposed.  Its length is

\[
 O\!\left(1+\frac{L\delta}{|a|}\right).
\tag{165.H24}
\]

The character on that entire progression is the single sign
((-1)^{a/2}).  If (a=0), then (r=db), (d\mid r), (m) is the
free slide, and the character product is (+1).  Thus neither exact
coordinate system contains a hidden long \(\chi _4(d)\)-sum after its
natural fibre labels are fixed.  Alternation in (u,v) or in (a/2)
still exists *between* fibres and is part of the open signed aggregate.

### 3.2 Exact high-common-divisor count

From (165.H16), for fixed (g) every nonempty fibre has

\[
 u,v\asymp\frac Lg,
 \qquad 1\le h<\frac Rg\ll\frac Lg.
\tag{165.H25}
\]

For fixed (g,u,v,h), the allowed interval for (m) has length (O(L))
and successive solutions differ by (v\asymp L/g).  Hence (165.H18)
has (O(g)) possible values of (t).  Dropping coprimality,
squarefreeness, selectors, and every support restriction can only enlarge
the absolute count, so

\[
\begin{aligned}
 |\mathfrak C^{\rm rem}_{\ge G}|
 &\ll_\varepsilon X^\varepsilon
 \sum_{G\le g\ll L}
 \left(\frac Lg\right)^2
 \left(\frac Lg\right)g\\
 &\ll_\varepsilon
 L^3X^\varepsilon\sum_{g\ge G}g^{-2}
 \ll_\varepsilon \frac{L^3}{G}X^\varepsilon.
\end{aligned}
\tag{165.H26}
\]

This proves (165.H10)--(165.H11).  It includes the equal-divisor slide
(d=d'): that case has (u=v=1), (r=gh), character (+1), and lies
in the high-gcd sector whenever it is physically present.  No phase or
character cancellation is needed for the sector theorem.

### 3.3 Phase derivatives, resonant centres, and positive self-return

On one fibre write (x=A+Kt\) and

\[
 \phi(t)=J(\sqrt{x+r}-\sqrt x).
\tag{165.H27}
\]

Direct differentiation gives

\[
 \phi'(t)=
 -\frac{JKr}
 {2\sqrt x\sqrt{x+r}(\sqrt{x+r}+\sqrt x)},
\tag{165.H28}
\]

and

\[
 \phi''(t)=\frac{JK^2}{4}
 \left(x^{-3/2}-(x+r)^{-3/2}\right)>0.
\tag{165.H29}
\]

On a fixed physical cell, (x,x+r\asymp L^2),
(K=guv\asymp L^2/g), and (r=gh).  Therefore

\[
 |\phi'(t)|\asymp\frac{Jh}{L},
 \qquad
 \phi''(t)\asymp\frac{Jh}{gL}=\lambda_{g,h}.
\tag{165.H30}
\]

The third derivative has size \(\asymp Jh/(g^2L)\), so (165.H30) stays
comparable on a cell of (O(g)) consecutive (t)'s.  Since (gh<R\ll L),

\[
 \lambda_{g,h}\gg \frac{Jh^2}{L^2}\gg1;
\tag{165.H31}
\]

the last inequality uses (H\asymp J^{1/2}) and (L\ll H).

There is no uniform distance-to-integer consequence in (165.H30).  For a
fixed admissible lattice point, both \(\phi(t)\) and \(\phi'(t)\) are
nonzero linear functions of the arbitrary real centre (J).  By choosing
arbitrarily large admissible (J), either one can be made integral at that
point.  This is only a one-point resonance control, not simultaneous phase
alignment of a physical family, but it rigorously rejects a uniform first
derivative argument that replaces size by distance to the nearest integer.

For a smooth fibre segment of length (T\ll g), the derivative interval
has length \(\asymp\lambda_{g,h}T\).  A Poisson or (B\)-process therefore
has that many central dual integers, while one stationary coefficient has
scale \(\lambda_{g,h}^{-1/2}\).  Taking absolute values after dualization
restores

\[
 (\lambda_{g,h}T+1)\lambda_{g,h}^{-1/2}
 \asymp T\sqrt{\lambda_{g,h}}
       +\lambda_{g,h}^{-1/2}.
\tag{165.H32}
\]

Because \(\lambda_{g,h}\gg1\), the minimum of (165.H32) and the trivial
bound is just the trivial (T).  This is a positive-ledger statement, not
a lower bound for the signed dual sum.  Keeping cancellation between the
dual integers remains a possible new mechanism.

If a parity, squarefree, coprimality, or Mobius opening places (t) in a
subprogression of step (q), the new phase has second derivative
(q^2\lambda_{g,h}) and length (T/q).  The central positive ledger is
exactly invariant as in (165.H8).  Any gain must therefore come from the
signed recombination of the congruence or Mobius classes, not from their
positive termwise estimates.

### 3.4 Selector, parity, profile, and endpoint effects

Inside a gcd fibre the literal arithmetic weight is

\[
\begin{aligned}
 \mathcal A_{g,h,u,v}(t)={}&
 \alpha_{A+r+Kt}(gv)\alpha_{A+Kt}(gu).
\end{aligned}
\tag{165.H33}
\]

It includes both squarefree indicators and the two row-dependent residual
selectors.  A selected row keeps neither/both incidences; a no-pair row
keeps every incidence.  The selector may change with (t), so ambient
balance within one row does not become a sign-reversing pairing along
(165.H18).  The four-prime unit-profile control remains (-1) for either
selector status and confirms that neither status deletes all high-capacity
rows.  It does not give a literal profile lower bound or an outer-phase
lower bound.

The analytic part of the profile has only (O(1)) smooth cells and hard
entry/exit points on a fixed fibre: (d=gu) and (d'=gv) are fixed, while
the square-root ratio and normalization vary with (N_t).  By contrast,
squarefreeness, coprimality, and the selected-pair rule can punch internal
holes at arithmetic positions.  Treating them as bounded variation is not
licensed.  Conversely, charging one (O(1)) endpoint per fibre has the
same large fibre-count capacity as the original opening.  Zero extension
is already exact in (165.H13) and creates no free endpoint saving.

### 3.5 Restored aggregate power and hostile real arrays

Shiftwise Cauchy, using only the accepted diagonal energy, gives

\[
 \left|\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\right|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{165.H34}
\]

Summing (R\asymp L) shifts restores (L^3X^\varepsilon), one full
factor (L) above the frozen correlation target.  Under the Fejer-to-
scalar connector this is the familiar missing (L^{1/2}): it yields only
the (L^2) scalar scale instead of (L^{3/2}).

This loss is sharp for the coefficient-uniform interface, even for real
bounded arrays supported on squarefree rows.  Let (I) be an interval of
cardinality (M\asymp L^2), let \(\mathscr S\subset I\) contain (Q\asymp M)
squarefree rows, and put \(\theta_N=2\pi J\sqrt N\).  Consider the two real
arrays

\[
 a_N=\mathbf1_{\mathscr S}(N)\cos\theta_N,
 \qquad
 b_N=\mathbf1_{\mathscr S}(N)\sin\theta_N.
\tag{165.H35}
\]

For a window starting at (s), define

\[
 A_s=\sum_{j<R}\mathbf1_{\mathscr S}(s+j),
 \qquad
 U_s=\sum_{j<R}\mathbf1_{\mathscr S}(s+j)e(2J\sqrt{s+j}).
\tag{165.H36}
\]

The two phase-weighted window sums are exactly

\[
 Z_s^{(a)}=\frac{A_s+U_s}{2},
 \qquad
 Z_s^{(b)}=\frac{U_s-A_s}{2i},
\tag{165.H37}
\]

and hence

\[
 |Z_s^{(a)}|^2+|Z_s^{(b)}|^2
 =\frac{A_s^2+|U_s|^2}{2}\ge\frac{A_s^2}{2}.
\tag{165.H38}
\]

Every supported row occurs in exactly (R) full-line windows, so
\(\sum_sA_s=RQ\).  At most (M+R-1) windows meet (I), and Cauchy gives

\[
 \mathfrak E_R(a)+\mathfrak E_R(b)
 \ge\frac{1}{2R}\sum_sA_s^2
 \ge\frac{RQ^2}{2(M+R-1)}\asymp RM.
\tag{165.H39}
\]

At least one real array in (165.H35) has Fejer energy \(\gg RM\asymp L^3\),
while its diagonal energy is (O(M)\).  By the exact Fejer identity, its
one-sided aggregate real correlation is therefore \(\gg L^3\).  The same
argument on the accepted four-prime support of size
(Q\gg L^2/(\log L)^4) gives coefficient-uniform capacity

\[
 \gg \frac{RQ^2}{M}
 \gg \frac{L^3}{(\log L)^8},
\tag{165.H40}
\]

again above (L^2X^\varepsilon) on polynomial blocks for sufficiently
small \(\varepsilon\).  The cosine/sine weights in (165.H35) and (165.H40)
are not the literal residual profile.  These are exact hostile controls
against squarefree-support, row-count, diagonal-energy, or four-prime-
capacity theorems; they are not physical mass.

Finally, scalar target-safety cannot be transferred to Fejer energy.  On
an interval of even length (M\gg R), let (z_N=1) on the first half and
(z_N=-1) on the second.  Then \(\sum_Nz_N=0\), but all windows wholly
inside either half have modulus (R), so

\[
 \frac1R\sum_s\left|\sum_{j<R}z_{s+j}\right|^2
 \ge (M-2R)R\asymp MR.
\tag{165.H41}
\]

Thus the accepted scalar smallness of the XOR sector supplies no energy
connector for subtracting it inside (165.H15).

## 4. First doubtful or unproved step

There is no doubtful step in the multiplicity-one expansion, the gcd/CRT
and tangent parameterizations, the constant-character formulas, the
parity ledger, the derivative calculations, the high-gcd bound
(165.H10), or the hostile array identities (165.H35)--(165.H41).

The first unproved affirmative step is the signed low-gcd aggregate

\[
\boxed{
 \Re\!\sum_{\substack{g<\gamma L\\g\ {\rm odd}}}
 \sum_{1\le h<R/g}\left(1-\frac{gh}{R}\right)
 \sum_{\substack{u,v\ {\rm odd}\\(u,v)=1}}
 \chi _4(uv)
 \sum_t
 \mathcal A_{g,h,u,v}(t)e(\phi_{g,h,u,v}(t))
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{165.H42}
\]

All summands in (165.H42) retain the literal zero-supported weight
(165.H33).  A proof must preserve cancellation between different fibre
labels or between their phase duals.  The especially numerous small-
(g) fibres have only (O(g)) points, so no cancellation can be extracted
solely from their internal (t)-length.  At present there is no exact
sign-reversing map across ((u,v)) or (a/2) that also preserves the two
squarefree rows, both selectors, the parity branches, profiles, endpoints,
and phase.

A joint (r,N) argument remains genuinely open.  The phase as a function
of (r) can have useful curvature in part of the parameter range, but the
coefficient (c_{N+r}^{\rm rem}) is arithmetically discontinuous; no
bounded-variation amplitude theorem applies.  This report therefore does
not rule out a delta method, a signed spectral completion, a two-variable
transform, or a bespoke actual-direction inequality proving (165.H42).

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `actual_residual_coefficient_domain` | **GREEN.** (165.H13)--(165.H15) retain supported squarefree rows, literal residual selectors, profiles, endpoints, and zero extension. |
| `aggregate_one_sided_real_part` | **GREEN quarantine.** The target and (165.H42) keep one outer real part. Absolute values occur only in the explicitly scoped high-gcd theorem and positive-route capacity audit. |
| `additive_product_shift_multiplicity` | **GREEN.** Each opened divisor pair occurs once; (165.H17)--(165.H19) give one CRT class modulo (guv). |
| `gcd_tangent_and_determinant_coordinates` | **GREEN.** Gcd coordinates are (165.H17)--(165.H19); tangent coordinates and their exact congruence are (165.H22)--(165.H24). |
| `chi4_progression_or_pairing` | **GREEN no-go.** The character is constant (chi_4(uv)) on a gcd fibre and ((-1)^{a/2}) on a fixed tangent fibre. No literal cross-fibre pairing is proved. |
| `square_root_phase_resonance` | **GREEN route audit.** Exact derivatives are (165.H28)--(165.H31); point resonances exist for arbitrary-real centres; termwise-positive (B)-process capacity self-returns in (165.H32). Signed dual cancellation stays open. |
| `selected_and_no_pair_rows` | **GREEN scope.** Both are present in (165.H33). Ambient selected-row balance does not pair a fixed (d) across (t); no-pair rows remain whole. |
| `odd_divisor_and_even_complement_branch` | **GREEN.** (d,d') stay odd. Equation (165.H20) shows exactly how odd/odd, even/even, and mixed complementary branches alternate. |
| `hard_profile_endpoint_and_zero_extension` | **GREEN ledger.** Literal zero extension is in (165.H13); fixed-fibre analytic faces are finite, while their global multiplicity and arithmetic internal holes are charged rather than discarded. |
| `phase_aligned_arbitrary_array` | **GREEN falsification.** The real cosine/sine pair (165.H35)--(165.H39) has (L^2) diagonal energy and (L^3) Fejer capacity. It is diagnostic, not physical. |
| `four_prime_unit_profile_capacity` | **GREEN quarantine.** The accepted selector-robust support gives (165.H40) for bounded diagnostic weights. No literal-amplitude or outer-phase lower bound follows. |
| `scalar_vs_energy_connector` | **GREEN falsification.** (165.H41) has zero scalar sum and (MR) sliding energy, so scalar target-safety does not imply energy equivalence. |
| `rank_one_collar_geometry_separation` | **GREEN.** (165.H17)--(165.H19) are additive CRT progressions. They are not the multiplicative dual collar \(|s\ell-XQR|\ll QRJ/L\). Only the positive self-return phenomenon is analogous. |
| `missing_L_half_power` | **GREEN ledger.** Positive shiftwise control is (L^3) at correlation level versus target (L^2); through Fejer/Cauchy this is exactly the scalar loss (L^2) versus (L^{3/2}). |
| `remaining_few_point_and_downstream_scope` | **GREEN quarantine.** No result transfers to other (t)-channels, hard TOP, BAL, UNBAL, either smooth M2 packet, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the quarter theorem, or either exponent. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This report used exactly the task brief and the following authorized
repository artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`, at graph hash
   `141bbc8c998981245e33f18c9c116ef12f309ecfc54898e3a1dbd4569e0f7ba0`;
3. `state/active_campaign.yml`;
4. `strategy/round165_m2_hard_top_t1_residual_fejer_short_shift_strategy.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_short_shift_seed.md`;
7. `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
8. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
9. `proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md`;
10. `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reports/unmatched_transport_capacity_hostile_audit.md`;
11. `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reviews/transport_source_repair_verification.md`;
12. `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reviews/conductor_round164_adjudication.md`; and
13. the generated Round-165 brief for `short_shift_arithmetic_hostile_audit`.

No web source and no computation was used.  The squarefree-row asymptotic
and four-prime capacity invoked in the controls are inherited accepted
inputs from the authorized kernels and reviews, not newly imported source
claims.

## 7. Recommended state effect

**Retain** the exact gcd/CRT and tangent fibre reduction
(165.H17)--(165.H24), the target-safe actual high-common-divisor sector
(165.H10)--(165.H11), and the route-scoped positive fibre/phase no-go
(165.H6)--(165.H9) as candidate Round-165 evidence.

If no sibling report proves (165.H42), close the campaign under
`hard_top_t1_residual_fejer_no_go` and make (165.H42), with one outer real
part and every literal weight retained, the first open actual-direction
theorem.  Park only the following placements: character cancellation
inside a fixed gcd/tangent fibre; termwise-positive one-dimensional
phase dualization; positive parity or Mobius refinement; shiftwise
Cauchy; and scalar-to-energy transfer without a new connector.

**Do not promote** the hostile arrays, raw tuple counts, or four-prime
capacity to physical lower mass.  They do not disprove the literal
residual target.  Do not identify this additive progression obstruction
with the multiplicative rank-one collar.

**No change** to the full residual target, complete (t=1) face, remaining
few-point channels, hard TOP, BAL, UNBAL, either smooth M2 packet,
M9--M2, M9--M1, endpoint uniformity, M9, the conditional bridge, the
quarter theorem, or the internal and external global exponents.
