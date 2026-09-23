# Round 197 hostile four-corner orbit and power audit

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Task: `four_corner_orbit_power_hostile_audit`
- Role: barrier/no-go with strongest strict repair
- Starting graph SHA-256: `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Status: candidate evidence only; no shared-state edit

## 1. Result

**Verdict: the four gcd identities, commutation, character rectangle, and
mixed coefficient factorization are exact on the stated cross-coprime
domain. They do not act on complete (P_2). A stronger target-safe strict
repair uses only the lower allocation involution, while the first excluded
gcd/sign classes retain the complete unresolved positive-capacity power.**

Write

\[
 d=g\alpha,\qquad d'=g\beta,\qquad (\alpha,\beta)=1,
 \qquad M=m,\quad P=m'.
\tag{197.H1}
\]

At corners (00,10,01,11), the recomputed character-leg gcds are exactly

\[
 \boxed{g_{00}=g,\quad g_{10}=g(M,\beta),\quad
 g_{01}=g(\alpha,P),\quad g_{11}=g(M,P).}
\tag{197.H2}
\]

Consequently the two proposed swaps are commuting involutions with the
same literal (g) precisely on

\[
 (M,\beta)=(\alpha,P)=(M,P)=1.
\tag{197.H3}
\]

There they preserve (N,N+r,r), the Fejer factor, the radical phase,
squarefreeness, allocation coprimality, the two defects and (P_2). The
four character multipliers relative to corner (00) are

\[
 (1,s_0,s_1,s_0s_1),\qquad
 s_0=\chi_4(\alpha M),\quad s_1=\chi_4(\beta P).
\tag{197.H4}
\]

Thus (s_0=s_1=-1) gives ((+,-,-,+)), necessarily (4\mid r), and
the actual zero-extended endpoint product factors exactly as

\[
 \boxed{
 [\lambda_{N+r,\sigma}(g\beta)-\lambda_{N+r,\sigma}(gP)]
 \overline{[\lambda_{N,\sigma}(g\alpha)-\lambda_{N,\sigma}(gM)]}.}
\tag{197.H5}
\]

There is an earlier, less restrictive algebraic repair. Define the
physical lower-swap sector

\[
 \mathcal P_{\rm low}:=
 P_2\mathbf1_{(M,\beta)=1}
 \mathbf1_{\chi_4(\alpha M)=-1}.
\tag{197.H6}
\]

After completing orientation exits by the already safe monotone and
bounded-height source, \(\tau_0\) partitions this sector into two-cycles
and gives

\[
 \boxed{
 F(g\alpha,g\beta)-F(gM,g\beta)
 =\lambda_{N+r,\sigma}(g\beta)
  \overline{\lambda_{N,\sigma}(g\alpha)
             -\lambda_{N,\sigma}(gM)}.}
\tag{197.H7}
\]

Let \(\mathcal P_{\rm low}^{\rm cc}\) be the orbit-invariant submask on
which the two lower allocations lie in one certified literal smooth cell,
all normalized-BV and Boolean lower factors agree, and the residual
selector agrees. The accepted common-cell \(C^1\) estimate gives

\[
 \mathscr H^\sigma(\mathcal P_{\rm low}^{\rm cc}W)
 \ll_\varepsilon D_L^2L X^\varepsilon
 \ll_\varepsilon L^2X^\varepsilon.
\tag{197.H8}
\]

Rerunning the deletion-stable Round-187--Round-192 safe operators on this
physical mask gives the same bound for its exact core contribution. The
four-corner construction is algebraically sound on the frozen rectangular
sector, and the lower two-cycle supplies its common-cell saving with fewer
cross conditions. The whole rectangular sector is **not** proved
target-safe: the assigned artifacts do not certify transversality of every
literal ratio/profile/real-\(X\) face to the narrow line \(d\approx gM\).
Its face complement can retain the raw \(D_LL^2\) capacity.

The repair does **not** close complete (P_2). In the plus primitive chart

\[
 \kappa=(d,P)=(g\alpha,P)=(\alpha,P),
\]

and in the minus chart

\[
 \kappa=(d',M)=(g\beta,M)=(\beta,M),
\]

because physical squarefreeness gives ((g,M)=(g,P)=1). Hence (197.H3)
forces

\[
 \boxed{\kappa=1}
\tag{197.H9}
\]

at every opposing corner. The four-corner orbit cannot touch any exact
open packet with (2\le\kappa<D_L). The lower-only repair still misses
every minus-orientation packet with (kappa>1), as well as its
(s_0\ne-1) complement. On those exact complements the Round-195
capacity ledger remains

\[
 D_L\sum_{2\le\kappa<D_L}(1+L/\kappa)^2
 \quad\text{at the formal capacity scale }D_LL^2,
\tag{197.H10}
\]

or, packetwise, (u\{\kappa+\min(Y,D_L)\}X^\varepsilon) with unresolved
ratio (min(Y,D_L)/(H_B\mathfrak m\kappa)>1) on the exact Round-195 open
region. This is a route-capacity statement only. It supplies no
nonvanishing, density, or literal lower-mass claim.

Accordingly the full route stops at the first recomputed-gcd boundary.
The terminal interpretation is
`p2_four_corner_orbit_boundary_self_return_no_go`, together with the
strict common-cell lower-swap repair (197.H6)--(197.H8), not a complete
P2 or complete rectangular-sector estimate.

## 2. Exact statement and hypotheses

Fix the exact inherited physical source

\[
 N=dM,\qquad N+r=d'P,\qquad d,d'\ \mathrm{odd},\qquad
 0<r<R_0=\lceil L\rceil,\qquad 2\mid r,
\tag{197.H11}
\]

with squarefree endpoint products, allocation coprimality, both opposing
orientations, all residual selectors, profiles, floors, stars, half
weights, hard samples, cells, crossings, endpoint traces, Fejer weight,
radical phase, conjugation and zero extensions exactly as in the accepted
Round-185 source. The endpoint coefficient is the total zero-extended
(lambda_{N,\sigma}(d)) of (K185.2). Put

\[
 g=(d,d'),\qquad d=g\alpha,\qquad d'=g\beta,
 \qquad D=D_L=\lceil\sqrt L\rceil,
\]

and impose before every spectral operation

\[
 P_2=\mathbf1_{|d-gM|\le D}\mathbf1_{|d'-gP|>D}.
\tag{197.H12}
\]

All claims below are outer physical or masked-core claims. No fixed
conductor, one anchor mode, one projective band, one orientation norm, or
post-expansion scalar mask is paired. At (T=0) the complete inherited
rho-large remainder is retained; at (T\ge1) all simultaneous strict
Farey conditions are retained. Both frequency signs and orientations
remain inside the one outer real part.

The strict repair uses three inherited facts present in the permitted
context.

1. On live support, lower closeness and the hard cone give (g=O(1))
   uniformly in (L).
2. On a certified common cell, the actual lower symbol has a uniformly
   normalized \(C^1\) part. Normalized-BV factors, literal ratio/profile
   faces and real-\(X\) support crossings are separate. The assigned
   context supplies no uniform transversality theorem for all such faces
   along \(d\approx gM\).
3. Every accepted Round-187--Round-192 safe proof is stable when rerun on
   a coordinatewise physical deletion. Mask commutators, carries, births,
   deaths and zero extensions remain in the recomputed core.

For the four-corner statement impose (197.H3), and for the exact rectangle
also impose \(s_0=s_1=-1\). For the stronger algebraic two-corner repair
impose (197.H6); for its proved analytic estimate also impose the
orbit-invariant common-cell mask \(\mathcal P_{\rm low}^{\rm cc}\).
These masks are arithmetic/support masks, not assertions that any endpoint
coefficient is nonzero.

## 3. Proof and hostile derivation

### 3.1 All four recomputed gcds and commutation

The four raw allocation tuples are

\[
\begin{array}{c|c}
00&(g\alpha,M,g\beta,P)\\
10&(gM,\alpha,g\beta,P)\\
01&(g\alpha,M,gP,\beta)\\
11&(gM,\alpha,gP,\beta).
\end{array}
\tag{197.H13}
\]

Taking the gcd of the two character legs gives (197.H2) directly. Thus
the three cross conditions in (197.H3) are sufficient and individually
necessary for the same-(g) four-corner action. On that domain

\[
 \tau_0\tau_1(g\alpha,M,g\beta,P)
 =\tau_1\tau_0(g\alpha,M,g\beta,P)
 =(gM,\alpha,gP,\beta),
\]

and both maps square to the identity. The sign conditions exclude fixed
points: if (alpha=M), then (s_0=\chi_4(\alpha^2)=+1), and similarly at
the upper endpoint.

Physical squarefreeness makes (g,\alpha,M) pairwise coprime and
(g,\beta,P) pairwise coprime. Together with (197.H3) and
((\alpha,\beta)=1), all five quantities (g,\alpha,M,\beta,P) are
pairwise coprime. This proves both (197.H9) and the stronger fact that
every opposing corner has inward cross gcd one. Its height is therefore

\[
 h={r\over2g},
\tag{197.H14}
\]

so an opposing four-corner orbit cannot cross a physical dyadic height
boundary. This is the exact seam requested in the brief: the condition
((\alpha,P)=1) is not innocuous in the plus chart; it is precisely
(kappa=1).

For the lower-only action, only

\[
 (gM,g\beta)=g(M,\beta)=g
\]

is needed. At the image the reverse condition is
\((\alpha,\beta)=1\), already true. Hence (197.H6) is invariant under
\(\tau_0\), and \(s_0=-1\) makes every orbit a genuine two-cycle.

### 3.2 (P_2), source, cone and zero-extension truth tables

When the four gcds equal (g), both defects are orbit invariants:

\[
 |g\alpha-gM|=|gM-g\alpha|,\qquad
 |g\beta-gP|=|gP-g\beta|.
\]

Thus the (P_2) truth table is ((1,1,1,1)). If any gcd in (197.H2)
changes, this statement is false with the literal recomputed gcd. Such a
corner is a live allocation elsewhere, not a zero endpoint coefficient,
so replacing it by zero would delete an actual term.

The opposing-source predicate has a different exact table. Put

\[
 O_0=(\beta-\alpha)(P-M),\qquad
 O_1=(\beta-M)(P-\alpha).
\tag{197.H15}
\]

The four orientation products are

\[
 (O_0,O_1,O_1,O_0).
\tag{197.H16}
\]

Therefore opposing-source closure is not automatic. This is not a
full-capacity obstruction: any missing opposing corner is a monotone
corner (the other nonopposing sign patterns are incompatible with
(r>0)), and the complete monotone plus bounded-height source is already
absolutely (O(L^2X^\varepsilon)) by (K185.7). Completing an orbit in the
full even-shift source and subtracting these already safe corners is exact
and costs only the target.

Strict cones, shells, profiles and endpoint support need not have truth
table ((1,1,1,1)), especially at the far upper endpoint. They require no
fictitious support closure. With total zero extension their exact table is
the rectangular product of the two lower values and the two upper values,
so (197.H5) remains an algebraic identity even when an upper corner is
zero. An upper exit costs only the bounded upper factor. A lower exit is
part of the lower difference and is not assigned a pointwise \(C^1\)
bound. Section 3.5 shows that a fixed-coordinate BV collar would be safe,
but that the actual ratio/profile faces have no certified transversality
in the assigned context and can retain full capacity.

The exact Round-195 packet selector is not a literal fixed-mode orbit
predicate. The four-corner cross conditions make physical (kappa=1)
and (h) invariant, but Fourier modulus, anchor, carry and projective-band
labels still cannot be paired modewise. The lower-only repair need not
preserve even (kappa) or a dyadic (h) block. It is therefore formed on
the complete physical source before spectral expansion; orientation and
bounded-height exits are paid by (K185.7), and every accepted safe
operator is then rerun on the physical mask. A fixed-packet pairing would
retain the Round-195/Round-196 mask, anchor, carry and zero-extension
commutators at full available capacity.

### 3.3 Character table and the complete (r\pmod4) split

Because (g) is odd, direct multiplicativity gives (197.H4). In corner
order (00,10,01,11), the complete table is

\[
\begin{array}{c|c|c|c}
s_0&s_1&r\pmod4&\text{relative corner signs}\\ \hline
+1&+1&0&( +,+,+,+)\\
+1&-1&2&( +,+,-,-)\\
-1&+1&2&( +,-,+,-)\\
-1&-1&0&( +,-,-,+).
\end{array}
\tag{197.H17}
\]

The leading (+) on each row is the patch-visible mathematical sign, so
the entries in the first two columns are simply (+1) or (-1). The
congruence follows from

\[
 r=g(\beta P-\alpha M).
\]

Thus (s_0=s_1=-1) implies (4\mid r), but (4\mid r) does not imply
the rectangular sector: (s_0=s_1=+1) also has (r\equiv0\pmod4).
When (r\equiv2\pmod4), exactly one independent swap reverses character.
This is distinct from treating the simultaneous Round-193 swap as a
four-corner rectangle.

If (M,P) are even, then both swapped character legs are even and the
corresponding (chi_4) values are zero. The rectangular and lower-sign
sectors exclude this case automatically. It belongs to the exact open
sign complement and may not be silently discarded.

### 3.4 Actual coefficient factorization and the stronger single-swap repair

Let

\[
 F(x,y)=\lambda_{N+r,\sigma}(y)
        \overline{\lambda_{N,\sigma}(x)}.
\]

Summing one complete rectangular orbit once gives

\[
 F(g\alpha,g\beta)-F(gM,g\beta)
 -F(g\alpha,gP)+F(gM,gP),
\]

which is exactly (197.H5). If instead one sums over every atom rather than
over orbit representatives, the projection carries the harmless factor
(1/4). No multiplicity or positive power is hidden there.

More generally the four-corner character sum is

\[
 [\lambda_{N+r,\sigma}(g\beta)
   +s_1\lambda_{N+r,\sigma}(gP)]
 \overline{[\lambda_{N,\sigma}(g\alpha)
   +s_0\lambda_{N,\sigma}(gM)]}.
\tag{197.H18}
\]

Therefore the close-leg saving needs only \(s_0=-1\), not \(s_1=-1\).
More directly, the lower two-cycle gives (197.H7). This is an exact use
of the actual coefficients, not an arbitrary-array theorem. It
algebraically contains the frozen rectangular sector because it does not
require \((\alpha,P)=(M,P)=1\) or \(s_1=-1\). Analytically, only its
common-cell submask is certified below.

The simultaneous swap alone is different. On (r\equiv2\pmod4) it
produces

\[
 \lambda_1(g\beta)\overline{\lambda_0(g\alpha)}
 -\lambda_1(gP)\overline{\lambda_0(gM)},
\]

whose product-rule expansion contains an uncontrolled far-upper
difference. It does not imply (197.H7) or (197.H5).

### 3.5 Smooth, normalized-BV, selector and literal-face ledger

First count without cancellation. Lower closeness and (g=O(1)) give
(O(LD)) choices for ((\alpha,M)). There are (O(L)) even shifts, and
for fixed (N+r) the upper allocation has at most
(\tau(N+r)\ll_\varepsilon X^\varepsilon) choices. Hence

\[
 \#\mathcal I_{P_2}\ll_\varepsilon DL^2X^\varepsilon.
\tag{197.H19}
\]

On a common literal smooth cell, the accepted normalized (C^1) bound is

\[
 |\lambda_{N,\sigma}(g\alpha)
   -\lambda_{N,\sigma}(gM)|_{\rm sm}
 \ll_\varepsilon {D\over L}X^\varepsilon.
\tag{197.H20}
\]

The upper factor in (197.H5) is (O_\varepsilon(X^\varepsilon)), and in
(197.H7) it is one bounded endpoint value. Thus the common-cell
contribution is

\[
 {D\over L}\cdot DL^2X^\varepsilon
 =D^2LX^\varepsilon\ll L^2X^\varepsilon.
\tag{197.H21}
\]

For a normalized BV factor \(\eta\) in one **fixed absolute coordinate**,
the elementary collar inequality is

\[
 \sum_{|a-b|\le D}|\eta(a)-\eta(b)|
 \le 2D^2\operatorname{Var}(\eta).
\tag{197.H22}
\]

Indeed, expand each difference into its intervening increments; a fixed
increment is crossed by \(O(D^2)\) ordered close pairs. If every actual
lower face were known to have this fixed-coordinate transversality, the
shift and divisor sums would give the desired \(D^2L\) ledger.

That transversality is not certified by the assigned artifacts. A literal
ratio/profile boundary can move with the second lower coordinate and can
be aligned with the whole P2 tube. The exact hostile model is the ratio
boundary \(d/M=g\). At the two lower allocations put

\[
 R_0={g\alpha\over M},\qquad R_1={gM\over\alpha}.
\tag{197.H23}
\]

For every \(\alpha\ne M\),

\[
 (R_0-g)(R_1-g)
 =-{g^2(\alpha-M)^2\over\alpha M}<0.
\tag{197.H23a}
\]

Thus **all** \(O(LD)\) close lower pairs can cross one aligned ratio face,
not merely \(O(D^2)\) pairs. Restoring the shift and divisor sums gives
the raw \(DL^2X^\varepsilon\) capacity. This model does not assert that a
particular literal face equals \(d/M=g\); it proves that a face-by-face
\(D^2\) count requires an exact transversality/separation theorem. The
permitted context neither lists every literal profile/floor/star/crossing
face nor proves uniform separation from every active odd \(g\), including
real-\(X\) support motion. Consequently normalized BV and literal faces
are quarantined to \(\mathcal P_{\rm low}^{\rm cc}\); their complement is
not estimated.

The collar count (193.C31) does not fill this gap. It is proved inside the
double-close geometry, where the second close relation supplies an
additional localization. The one-close \(P_2\) tube has the larger raw
count (197.H19), and no assigned artifact proves the corresponding
transversality after that second close relation is removed.

For the Round-184 residual selector, its exact truth table is

\[
 (\mathbf1_{p\mid d},\mathbf1_{q\mid d})
 =(0,0),(1,0),(0,1),(1,1)
 \quad\longmapsto\quad (1,0,0,1).
\tag{197.H24}
\]

Under the lower allocation swap, a selected prime outside \(g\) changes
membership and a selected prime inside \(g\) does not. Hence the selector
is invariant if both selected primes lie in \(g\) or both lie outside it,
and it flips exactly when one selected prime lies in \(g\). The P2 close
condition gives \(g\le G_0\). The accepted selector chooses its pair with
logarithmic gap \(O(L^{-1/2})\), so a distinct pair with exactly one member
in this fixed finite prime set is absent for all sufficiently large \(L\).
The finitely many remaining shells are paid absolutely. This proves the
selector control without calling it \(C^1\).

Combining the common-cell estimate (197.H21), selector agreement, the
already safe orientation/height exits, and complete zero extension proves
(197.H8) only on \(\mathcal P_{\rm low}^{\rm cc}\). Deletion stability
then gives

\[
 |\mathscr S_{\le192}(\mathcal P_{\rm low}^{\rm cc}W)|
 \ll_\varepsilon L^2X^\varepsilon,
\]

and the exact identity

\[
 \mathscr R_{\rm core}(\mathcal P_{\rm low}^{\rm cc}W)
 =\mathscr H(\mathcal P_{\rm low}^{\rm cc}W)
  -\mathscr S_{\le192}(\mathcal P_{\rm low}^{\rm cc}W)
\]

passes the common-cell strict repair through the literal masked core,
including both \(T\)-branches, all carries and births/deaths, complete anchor
recombination and the one outer real part.

### 3.6 Exact complement and restored powers

The lower repair has the exact first-failure complement

\[
\begin{aligned}
 \mathcal E_{\rm gcd}&=P_2\mathbf1_{(M,\beta)>1},\\
 \mathcal E_{\rm sign}&=P_2\mathbf1_{(M,\beta)=1}
                         \mathbf1_{s_0\ne-1},\\
 \mathcal E_{\rm face}&=\mathcal P_{\rm low}
                         -\mathcal P_{\rm low}^{\rm cc}.
\end{aligned}
\tag{197.H25}
\]

The stricter four-corner complement also includes failure of
\((\alpha,P)=1\), failure of \((M,P)=1\), and \(s_1\ne-1\). The first
two rows of (197.H25) and these extra four-corner failures are arithmetic
or sign complements, not BV collars. The third row is the exact
BV/literal-face complement. By (197.H23a), no assigned artifact gives any
of them a uniform factor \(D/L\).

For (2\le\kappa<D), the exact four-corner conditions already fail by
(197.H9). In the minus chart, even the lower-only gcd condition is
equivalent to (kappa=1). Removing (kappa=1) does not change the power
of the positive Round-195 envelope:

\[
 D\sum_{2\le\kappa<D}(1+L/\kappa)^2
 \ll DL^2+LD\log(2L)+D^2,
\tag{197.H26}
\]

and the formal capacity contribution
\(DL^2\sum_{\kappa\ge2}\kappa^{-2}\) has the same \(DL^2\) scale. At
\(D=\lceil\sqrt L\rceil\), this is the unresolved \(L^{5/2}\) capacity,
and the aligned-face model has that same raw capacity already at fixed
\(\kappa\). The paired common-cell strict sector is

\[
 {D\over L}(DL^2)=D^2L\ll L^2.
\tag{197.H27}
\]

No (D,Y,q,U,\mathfrak m,\kappa), or (L) power is absorbed into
(X^\varepsilon). The physical proof has no (q/J) denominator because
it is made before spectral expansion. The accepted safe-operator and
dyadic/logarithmic sums use only fresh epsilon rebudgeting. Equations
(197.H26)--(197.H27) compare proof capacities; they do not assert that the
literal bad-gcd/sign/face complement is nonempty with positive coefficient
mass, much less that it has a lower bound of this order.

## 4. First doubtful or unproved step

The first false step in a complete-(P_2) four-corner proof is the
unqualified assertion that every recomputed gcd is (g). Equation
(197.H2) is the exact replacement. If, for example,
((\alpha,P)>1), then the (01) corner has gcd
(g(\alpha,P)>g); its literal (P_2) mask is recomputed with that larger
gcd. It is neither the intended corner nor a zero-extension boundary.

After restricting to (197.H3), the first scope obstruction is (197.H9):
the four-corner sector is confined to physical (kappa=1). The exact
open packets with (2\le\kappa<D_L) and
(min(Y,D_L)>H_B\mathfrak m\kappa) are untouched and retain the
Round-195 packet deficit. The lower-only repair removes two unnecessary
cross conditions. Its common-cell pairing and masked-core passage are
valid, but extending its \(D/L\) estimate across all literal faces is
unproved: (197.H23a) falsifies the claimed automatic \(O(D^2)\)
lower-face count when a face is aligned with the P2 tube. Thus its exact
complement (197.H25), including every minus \(\kappa>1\) packet, the
\(s_0\ne-1\) sign class, and the full-capacity face class, remains
unproved.

Thus the first remaining theorem is a jointly signed estimate for
(197.H25) with the actual endpoint coefficients, both orientations and
all literal fields before positive norms. Capacity controls do not
disprove that theorem.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_physical_even_shift_source` | **PASS.** Equations (197.H11)--(197.H12) retain the ordered products, even shift, character, Fejer factor, radical phase, literal fields and zero extensions. |
| `four_corner_recomputed_gcd` | **PASS with exact restriction; FAIL globally.** The four values are (197.H2), not four automatic copies of (g). |
| `cross_coprimality_orbit_closure` | **PASS.** Conditions (197.H3) are exact. They make all five allocation factors pairwise coprime and force (kappa=1). |
| `commuting_independent_allocation_swaps` | **PASS only on (197.H3).** There the maps commute, square to one, and have no fixed point in the rectangular sign sector. |
| `four_corner_character_table` | **PASS.** Equation (197.H17) gives all four sign rows; the frozen rectangle is exactly the last row. |
| `r_mod_four_sign_split` | **PASS.** Both equal-sign rows have (r\equiv0\pmod4); the mixed rows have (r\equiv2\pmod4). Thus (4\mid r) alone does not select the rectangle. |
| `actual_endpoint_mixed_difference` | **PASS.** Equation (197.H5) has the correct upper factor and conjugated lower factor, including zero-extended actual coefficients. |
| `single_swap` | **ALGEBRAIC REPAIR; analytic quarantine.** The lower swap on (197.H6) gives the stronger exact identity (197.H7). Its common-cell submask is target-safe, but its complete literal-face complement is not. |
| `no_simultaneous_swap_substitution` | **PASS.** The simultaneous swap yields a difference of endpoint products with a surviving far-upper product-rule term; it is not the rectangle or lower two-cycle. |
| `lower_close_D_L_over_L_gain` | **PASS for the actual smooth lower symbol.** Equations (197.H19)--(197.H21) give exactly ((D/L)(DL^2)=D^2L\ll L^2). It is not coefficient-uniform. |
| `normalized_BV_and_literal_face_collars` | **PASS only for a certified fixed-coordinate collar; UNPROVED for the complete literal symbol.** Equation (197.H22) is valid, but (197.H23a) shows that an aligned ratio/profile face can be crossed by all O(LD) lower pairs. The assigned context supplies no complete face list or uniform real-X transversality theorem. |
| `residual_selector_truth_table` | **PASS with the exact exceptional row.** The table is (197.H24); a flip occurs exactly when one selected prime lies in bounded (g). The accepted logarithmic-gap property removes it for large (L), and bounded shells are paid absolutely. |
| `opposing_source_and_cone_exits` | **PASS for source exits and upper zero extensions; common-cell only at the lower endpoint.** Source table (197.H16) is not constant, but its missing corners are already safe. Lower cone/profile/support exits belong to E_face unless exact transversality is proved. |
| `complete_four_corner_zero_extension` | **PASS for endpoint support, FAIL as a gcd shortcut.** Zero endpoint values preserve (197.H5). A changed-gcd corner is a different live physical atom and cannot be set to zero. |
| `complete_outer_power_ledger` | **PASS on the common-cell strict repair, FAIL for its complement.** Equations (197.H21) and (197.H27) are target-safe. Equations (197.H23a) and (197.H26) retain the full extra D capacity. |
| `no_arbitrary_coefficient_replacement` | **PASS.** The algebra holds for values, but the (D/L) estimate uses only the actual normalized symbol. Arbitrary close endpoint arrays can have a unit jump. |
| `unsigned_character_erased_phase_conjugated_controls` | **PASS as falsifiers.** Erasing character replaces the close difference by a sum; phase conjugation or adversarial bounded endpoint values can attain positive capacity. None is asserted to be literal. |
| `missing_corner` | **PASS with separation of causes.** Monotone/height exits are already safe and endpoint zeros factor exactly. Changed-gcd corners form the first unresolved arithmetic complement; untransversed lower faces form a second full-capacity complement. |
| `physical_mask_before_spectral_operations` | **PASS.** The repair is made on the complete physical source. No fixed-mode or fixed-conductor pairing is used. |
| `both_T_branches_complete_anchor_one_real_part` | **PASS through masked-core return.** The (T=0) branch, all (T\ge1) conditions, both signs/orientations, full anchor aggregate, carries and births/deaths remain before the final real part. |
| `no_capacity_to_mass_inference` | **PASS.** Equations (197.H10), (197.H26) are capacity ledgers only. No literal nonvanishing or lower mass is claimed. |
| `original_t1_only_downstream_scope` | **PASS.** Even the strict repair concerns only this physical (P_2) part of original (t=1). |
| `exponent_quarantine` | **PASS.** No parent, bridge, theorem or exponent changes. |

No numerical or symbolic diagnostic was used.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted context were used:

1. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/briefs/four_corner_orbit_power_hostile_audit.md` —
   `ed9fd0c7aa7ad44af476074977abea376143cdf211f69393a3549a8f7e1f4bb9`.
2. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
3. `state/proof_obligations.yml` —
   `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`.
4. `state/active_campaign.yml` —
   `fa2c0fbf95a18a7c0e4e59afbc2b190e540db5c28301f504ef2147907651ebb9`.
5. `state/failure_ledger.md` —
   `ca3d498597a9a1f316a06a4ea6ef9a50190fa0ad32b439237c9c8631a8b48c38`.
6. `strategy/round197_m1_t1_p2_four_corner_allocation_commutator_strategy.md` —
   `dc2b22ee13bff8b09f3902e0d9717fab4bd8413efda65972e0fff1dfd74f8b15`.
7. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md` —
   `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`.
8. `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md` —
   `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`.
9. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` —
   `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.
10. `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md` —
    `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`.
11. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reports/p2_gram_diagonal_collision_hostile_audit.md` —
    `52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb`.
12. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/literal_gram_nogo_owner_scope_seam_review.md` —
    `5b37315c66bd637c127cc8f3fddbb7f94ed14f9f94955c685f90a5960120c197`.
13. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/conductor_round193_adjudication.md` —
    `dea735b1f41f9305fbc881d61ea0ee616bbe055740a74646d945d3f75888c464`.

No web source, sibling Round-197 report, computation, or unlisted artifact
was used. No graph, proof draft, validation matrix, strategy, candidate,
kernel, synthesis, sibling artifact, or shared state was edited.

## 7. Recommended state effect

**REVISE; no immediate graph mutation from this report alone.**

Retain as candidate evidence only the exact lower-swap algebra (197.H6)--
(197.H7) and its orbit-invariant common-cell sublemma (197.H8). The
algebraic sector contains the frozen rectangle and uses fewer cross
conditions, but the proved common-cell sector need not contain the whole
rectangle. Do not promote a literal BV/face sector until an exact
face-by-face transversality and real-\(X\) uniformity theorem rules out the
aligned-face capacity (197.H23a).

Record the following exact route boundary at the same time:

1. the full four-corner action requires (197.H3) and consequently lives
   only on (kappa=1);
2. changed-gcd corners cannot be supplied by zero extension;
3. the exact gcd/sign/face complement (197.H25), in particular the open
   \(2\le\kappa<D_L\) packets and untransversed lower faces, retains the
   Round-195 unresolved capacity;
4. simultaneous-swap-only, fixed-mode, unsigned, character-erased,
   phase-conjugated, arbitrary-coefficient and separate-orientation
   arguments do not estimate that complement; and
5. none of these capacity statements is literal lower mass.

Do not promote complete (P_2), (P_1), complete original (t=1), any
other original-(t) incidence, the hard small-(t) owner, either M1
parent, GAR, any M2 parent, endpoint uniformity, M9, either bridge, the
quarter theorem, or any exponent.
