# Round 199 discovery report: literal cross-gcd cellular-boundary attack

- Campaign: `m9-m1-t1-p2-cross-gcd-cellular-boundary-gate`
- Task: `literal_cross_gcd_cellular_boundary_attack`
- Role: discovery
- Graph SHA-256: `63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5`
- Status: candidate evidence only; no shared proof-state edit
- Numerical theorem evidence: none

## 1. Result: aligned-face cross-gcd triangle self-return

The specified four-cross-gcd cellular mechanism does **not** prove the
complete Round-199 three-piece theorem.  Its first exact self-return occurs
on the mandatory aligned literal face.

For every squarefree physical allocation, the four cross gcds give an exact
factorization

\[
 d=G_{00}G_{01}x,\qquad m=G_{10}G_{11}u,\qquad
 d'=G_{00}G_{10}y,\qquad m'=G_{01}G_{11}v,
\tag{199.D1}
\]

in which the eight displayed factors are pairwise coprime.  Put
\(g=G_{00}\).  There are exactly three scaled allocation maps based at
this marked \(g\): the lower, upper, and simultaneous swaps.  They are
intrinsic physical involutions with the same recomputed gcd \(g\) only on

\[
 G_{10}=1,\qquad G_{01}=1,\qquad G_{11}=1,
\tag{199.D2}
\]

respectively.  Outside these domains the relevant cross factor is absorbed
into the recomputed \(G_{00}\); the map is not inverted by the physical
map formed with that recomputed gcd.

In the most favourable nontrivial case, one odd squarefree factor
\(\xi>1\) cycles among \(G_{01},G_{11},G_{10}\).  The three lawful
same-\(g\) involutions form a triangle.  The fourth allocation, with
\(\xi\) in \(G_{00}\), is not optional: actual \(\chi _4\)-incidence
gives the exact identity

\[
 \mathcal T_{\triangle}
 =\mathcal T_{\square}
 -\epsilon_\chi\Phi_{r,\sigma}(N)s_U
   \lambda_{N+r,\sigma}(g\xi y)
   \overline{\lambda_{N,\sigma}(g\xi u)}.
\tag{199.D3}
\]

Here \(s_U\in\{\pm1\}\) is the actual upper character quotient and
\(\mathcal T_{\square}\) is the complete four-corner twisted product.
Thus the missing \(G_{00}\) corner returns with ordinary coefficient one.
On a plus-oriented aligned \(P_2\) atom, \(\xi=G_{01}=\kappa\); for all
sufficiently large live shells the missing corner satisfies \(P_1\), not
\(P_2\).  It is therefore not an accepted error owner.  If its literal
coefficient is zero, the corresponding live/dead zero-extension boundary
still remains and cannot be deleted.

Before this attempted triangular completion, the aligned sharp-code
difference itself contains a coefficient-one jump.  The exact ratio
identity places the two lower allocations on opposite sides of the face,
and the jump has only the inherited positive capacity
\(D_LL^2X^\varepsilon\), missing the target by \(D_L\).  Equation
(199.D3) shows that adding the gcd-failure state merely transports that
ordinary face to the missing \(G_{00}\)/\(P_1\) corner; it does not make
it a safe cellular boundary.

The sign-failure edge also has its actual incidence \(+1\), not an
assignable negative orientation.  The changed-gcd lower edge is not a
physical bijection.  Hence, already on this minimal physical orbit, no
coefficient-preserving two-chain built from the four allocation states can
satisfy the proposed identity with every non-target face in an accepted
safe owner,

\[
 \partial_{\chi,\mathrm{lit}}\mathcal C
 =(P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f})W
 +E_{\mathrm{safe}}.
\]

This is a no-go only for the frozen cross-gcd cellular-boundary mechanism.
It is not a lower bound, a nonvanishing assertion, or a disproof of the
Round-199 outer estimate by another method.

## 2. Exact statement and hypotheses

Fix the exact Round-197/Round-198 physical source

\[
 N=dm,\qquad N+r=d'm',\qquad 0<r<R_0,\quad 2\mid r,
\]

and the literal atom

\[
 W=\chi _4(d')\chi _4(d)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(d')
 \overline{\lambda_{N,\sigma}(d)}.
\tag{199.D4}
\]

Both products are squarefree on nonzero support, \(d,d'\) are odd, and
every shell, endpoint, profile, selector, phase, carry, star, half-weight,
cell, crossing, arithmetic, orientation, conjugation, and zero-extension
field in the accepted coefficients remains literal.  Put

\[
 g=(d,d'),\qquad d=g\alpha,\qquad d'=g\beta,
\]

and impose on the physical source, before any spectral operation,

\[
 P_2=\mathbf1_{|d-gm|\le D_L}
     \mathbf1_{|d'-gm'|>D_L}.
\tag{199.D5}
\]

The exact unresolved mask is

\[
 P_{\partial\mathrm{lit}}\ \dot\cup\ P_{s\mathrm f}\ \dot\cup\ P_{g\mathrm f},
\tag{199.D6}
\]

where

\[
\begin{aligned}
P_{\partial\mathrm{lit}}
 &=P_2\mathbf1_{(m,\beta)=1}
   \mathbf1_{\chi _4(\alpha m)=-1}(1-C_{\mathrm{lit}}),\\
P_{s\mathrm f}
 &=P_2\mathbf1_{(m,\beta)=1}
   \mathbf1_{\chi _4(\alpha m)\ne-1},\\
P_{g\mathrm f}
 &=P_2\mathbf1_{(m,\beta)>1}.
\end{aligned}
\tag{199.D7}
\]

The open packet condition is retained exactly as

\[
 \kappa<D_L,\qquad M:=\min(Y,D_L)>H_B\mathfrak m\kappa.
\tag{199.D8}
\]

It is applied only after the physical allocation algebra.  The theorem
target is the one outer estimate

\[
 \left|\mathscr R_{\mathrm{open,out}}^\sigma
 ((P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f})W)\right|
 \ll L^2X^\varepsilon.
\tag{199.D9}
\]

The no-go statement proved here is the following.

> **Cross-gcd cellular self-return.**  On the squarefree physical source,
> the only lower, upper, and simultaneous scaled allocation maps which
> preserve the actual recomputed gcd \(G_{00}=g\) are the involutions on
> the three domains in (199.D2).  On an aligned character-reversing lower
> edge, every attempted same-\(g\) two-cell is either absent, restricted to
> the already known \(\kappa=1\) rectangle, or belongs to the three-state
> orbit (199.D20) below.  The actual character incidence on that orbit
> forces the coefficient-one fourth corner (199.D3).  This corner has
> recomputed gcd \(g\xi\) and lies in the unproved \(P_1\) owner for all
> sufficiently large aligned shells.  Therefore it cannot be included in
> \(E_{\mathrm{safe}}\), and the proposed complete cellular identity fails.

No assertion that the surviving endpoint product is numerically nonzero is
made or needed for this mechanism statement.

## 3. Proof and derivation

### 3.1 Four-cross-gcd factorization

Define

\[
 G_{00}=(d,d'),\quad G_{10}=(m,d'),\quad
 G_{01}=(d,m'),\quad G_{11}=(m,m').
\tag{199.D10}
\]

A prime common to two different \(G_{ij}\)'s would divide both \(d\) and
\(m\), or both \(d'\) and \(m'\), contrary to the squarefreeness of
\(N\) or \(N+r\).  Hence the four factors are pairwise coprime.  Every
prime of \((N,N+r)\) occurs in exactly one of them according to whether it
is allocated to \(d\) or \(m\), and to \(d'\) or \(m'\).  Thus

\[
 (N,N+r)=G_{00}G_{10}G_{01}G_{11}.
\]

Dividing the four physical factors by the indicated cross gcds gives
(199.D1), with \(x,u,y,v\) pairwise coprime and coprime to every
\(G_{ij}\).  In particular \(G_{00}=g\) and
\(G_{10}=(m,\beta)\), exactly as required by the three-piece filtration.

### 3.2 The three scaled maps, recomputed gcds, and inverse cells

On the ambient zero-extended allocation space define

\[
\begin{aligned}
 \mathcal L_g(d,m,d',m')&=(gm,d/g,d',m'),\\
 \mathcal U_g(d,m,d',m')&=(d,m,gm',d'/g),\\
 \mathcal S_g(d,m,d',m')&=(gm,d/g,gm',d'/g).
\end{aligned}
\tag{199.D11}
\]

They preserve \(N,N+r,r\), and the common scalar
\(\Phi_{r,\sigma}(N)\).  Direct use of (199.D1) gives the complete
recomputed cross-gcd table

\[
\begin{array}{c|cccc}
 &G_{00}^{\rm new}&G_{10}^{\rm new}&G_{01}^{\rm new}&G_{11}^{\rm new}\\ \hline
 \mathcal L_g&gG_{10}&1&G_{11}&G_{01}\\
 \mathcal U_g&gG_{01}&G_{11}&1&G_{10}\\
 \mathcal S_g&gG_{11}&G_{01}&G_{10}&1.
\end{array}
\tag{199.D12}
\]

Consequently:

* \(\mathcal L_g\) is a same-\(g\) involution precisely on
  \(G_{10}=1\); its inverse is \(\mathcal L_g\), and it swaps
  \(G_{01}\) with \(G_{11}\).
* \(\mathcal U_g\) is a same-\(g\) involution precisely on
  \(G_{01}=1\); its inverse is \(\mathcal U_g\), and it swaps
  \(G_{10}\) with \(G_{11}\).
* \(\mathcal S_g\) is a same-\(g\) involution precisely on
  \(G_{11}=1\); its inverse is \(\mathcal S_g\), and it swaps
  \(G_{10}\) with \(G_{01}\).

Thus, on their respective live same-\(g\) domains (with literal zero
extension at the boundary), the inverse cells are explicitly

\[
 \mathcal L_g^{-1}=\mathcal L_g,\qquad
 \mathcal U_g^{-1}=\mathcal U_g,\qquad
 \mathcal S_g^{-1}=\mathcal S_g.
\tag{199.D12a}
\]

On these domains the \(P_2\) defects are respectively changed by

\[
 (\Delta_0,\Delta_1)\mapsto(-\Delta_0,\Delta_1),\quad
 (\Delta_0,-\Delta_1),\quad(-\Delta_0,-\Delta_1),
\tag{199.D13}
\]

so the physical \(P_2\) mask is preserved exactly.

If, for example, \(G_{10}>1\), the image under \(\mathcal L_g\) has
physical gcd \(g_L=gG_{10}\).  Forming the inverse from the physical image
with this recomputed gcd gives

\[
 \mathcal L_{g_L}\mathcal L_g(d,m,d',m')
 =(gG_{10}G_{01}x,\,G_{11}u,\,d',\,m'),
\tag{199.D14}
\]

not the original allocation.  The analogous failure holds for
\(\mathcal U_g\) when \(G_{01}>1\) and for \(\mathcal S_g\) when
\(G_{11}>1\); explicitly, with \(g_U=gG_{01}\) and
\(g_S=gG_{11}\),

\[
\begin{aligned}
 \mathcal U_{g_U}\mathcal U_g(d,m,d',m')
  &=(d,m,gG_{01}G_{10}y,G_{11}v),\\
 \mathcal S_{g_S}\mathcal S_g(d,m,d',m')
  &=(gG_{11}G_{01}x,G_{10}u,
     gG_{11}G_{10}y,G_{01}v),
\end{aligned}
\tag{199.D14a}
\]

which are again not the source allocations.  Remembering the old \(g\)
would manufacture a marked
inverse, but the mark is not physical: at a changed-gcd image every
suitable divisor of the new \(G_{00}\) is a possible former \(g\).
Thus forgetting the mark is many-to-one.  This is the exact
changed-gcd bijection failure.

All live/dead endpoint changes in (199.D11) are interpreted through the
accepted total zero extension.  A dead image is a boundary term, not a
deleted corner.

### 3.3 Actual \(\chi _4\)-twisted incidence

On an odd live four-corner allocation put

\[
 s_L=\chi _4(\alpha m),\qquad
 s_U=\chi _4(\beta m').
\tag{199.D15}
\]

These are not chosen cellular orientations.  They are the literal
quotients

\[
 \frac{\chi _4(gm)\chi _4(g\beta)}
      {\chi _4(g\alpha)\chi _4(g\beta)}=s_L,
 \qquad
 \frac{\chi _4(g\alpha)\chi _4(gm')}
      {\chi _4(g\alpha)\chi _4(g\beta)}=s_U.
\tag{199.D16}
\]

The simultaneous quotient is \(s_Ls_U\).  Hence the actual corner table
is

\[
 (1,s_L,s_U,s_Ls_U).
\tag{199.D17}
\]

Its holonomy is \(+1\).  On \(s_L=s_U=-1\), the complete four-corner
combination is the familiar \((+,-,-,+)\) mixed difference; the diagonal
simultaneous swap itself still has sign \(+1\).  If \(s_L=+1\), the lower
edge is a sum.  If the swapped divisor is even, the quotient is zero and
the original endpoint is an unpaired zero-extension boundary.  In the
aligned sector \(s_L=-1\), all factors of \(N\), and hence of \(N+r\),
are odd, so \(s_U\in\{\pm1\}\).

### 3.4 Mandatory aligned literal-face test

On \(P_{\partial\mathrm{lit}}\), \(G_{10}=1\), \(s_L=-1\), and the
lower allocations are

\[
 (m,g\alpha),\qquad(\alpha,gm).
\]

For \(\alpha\ne m\),

\[
 \left(\frac{g\alpha}{m}-g\right)
 \left(\frac{gm}{\alpha}-g\right)
 =-\frac{g^2(\alpha-m)^2}{\alpha m}<0.
\tag{199.D18}
\]

Restrict to the required aligned-face stratum of a named sharp-code
coordinate whose face is at this ratio.
If its multiplier is \(K\) and the remaining literal endpoint value on
the two branches is \(F\), then the exact lower difference contains

\[
 K_0F_0-K_1F_1
 =K_0(F_0-F_1)+(K_0-K_1)F_1.
\tag{199.D19}
\]

Equation (199.D18) gives \(K_0-K_1=\pm1\) on every close pair in this
aligned-face stratum.
The second term of (199.D19) is therefore an ordinary face with coefficient
one.  It has no \(D_L/L\) smooth gain and no fictitious
\(D_L^2\)-collar gain.  The inherited physical count prices it only by
\(D_LL^2X^\varepsilon\).

If neither transverse same-\(g\) map is live, this is already an exposed
face and the mechanism stops.  The strongest possible repair occurs when
one odd squarefree cross factor \(\xi>1\) cycles through the other three
cross states.  In the plus primitive chart,
\(\kappa=(d,m')=G_{01}\); in the minus chart,
\(\kappa=(d',m)=G_{10}\).  Hence an aligned lower edge
\(G_{10}=1\) with \(2\le\kappa<D_L\) is necessarily plus-oriented,
whereas the minus aligned edge is confined to \(\kappa=1\).  Take that
plus-oriented aligned state and write the complete
orbit as

\[
\begin{array}{c|c|c}
\text{cross state}&(d,m,d',m')&\text{lawful edges}\\ \hline
V_{01}&(g\xi u,x,gv,\xi y)&\mathcal L_g,\mathcal S_g\\
V_{11}&(gx,\xi u,gv,\xi y)&\mathcal L_g,\mathcal U_g\\
V_{10}&(gx,\xi u,g\xi y,v)&\mathcal U_g,\mathcal S_g\\
V_{00}&(g\xi u,x,g\xi y,v)&\text{changed-gcd only}.
\end{array}
\tag{199.D20}
\]

Thus \(V_{01},V_{11},V_{10}\) form the exact three-state orbit, while

\[
 \mathcal U_gV_{01}=\mathcal S_gV_{11}=\mathcal L_gV_{10}=V_{00}
\tag{199.D21}
\]

uses precisely the forbidden changed-gcd version of each map.  The actual
gcd at \(V_{00}\) is \(g\xi\).

Let

\[
\begin{aligned}
 L_0&=\lambda_{N,\sigma}(g\xi u),&
 L_1&=\lambda_{N,\sigma}(gx),\\
 U_0&=\lambda_{N+r,\sigma}(gv),&
 U_1&=\lambda_{N+r,\sigma}(g\xi y),
\end{aligned}
\]

and let \(\epsilon_\chi=\chi _4(g\xi u)\chi _4(gv)\).  Relative to
\(V_{01}\), the actual character incidences at
\((V_{01},V_{11},V_{00},V_{10})\) are

\[
 (1,s_L,s_U,s_Ls_U),\qquad
 s_L=\chi _4(\xi ux),\quad s_U=\chi _4(\xi yv).
\tag{199.D22}
\]

On the aligned face, \(s_L=-1\).  The complete four-corner cell is

\[
 \mathcal T_{\square}
 =\epsilon_\chi\Phi_{r,\sigma}(N)
 (U_0+s_UU_1)\overline{(L_0-L_1)}.
\tag{199.D23}
\]

The three lawful vertices consist of two
\(P_{\partial\mathrm{lit}}\) vertices and the \(P_{g\mathrm f}\)
vertex \(V_{10}\).  Their exact sum is

\[
\begin{aligned}
 \mathcal T_{\triangle}
 =\epsilon_\chi\Phi_{r,\sigma}(N)
 \{U_0\overline{L_0}-U_0\overline{L_1}
      -s_UU_1\overline{L_1}\}.
\end{aligned}
\tag{199.D24}
\]

Subtracting (199.D23) gives (199.D3).  In particular, even when
\(s_U=-1\) makes the formal square a product of two differences, the
lawful triangle leaves \(V_{00}\) with coefficient one.  When
\(s_U=+1\), the transverse factor is a sum and the same missing corner
remains.  There is no character case in which the lawful three-state
orbit is a complete two-cell.

Finally, \(V_{01}\in P_2\) gives

\[
 |g\xi u-gx|\le D_L.
\tag{199.D25}
\]

Write \(x=\xi u+e\), \(|e|\le D_L/g\).  At \(V_{00}\), whose physical
gcd is \(g\xi\), the first defect is

\[
\begin{aligned}
 |g\xi u-g\xi x|
 &=g\xi|u-x|\\
 &\ge \xi\{(1-1/\xi)g\xi u-D_L\}.
\end{aligned}
\tag{199.D26}
\]

The literal shell gives \(g\xi u\ge cL\) for a fixed \(c>0\), while
\(\xi\ge3\) and \(D_L\le2\sqrt L\).  Hence (199.D26) is greater than
\(D_L\) for every sufficiently large shell.  Thus \(V_{00}\in P_1\).
The finitely many remaining shells are absolutely bounded, but that does
not turn the large-shell \(P_1\) corner into a licensed safe owner.

This proves the aligned-face self-return.

### 3.5 Sign failure and changed-gcd failure

On the odd part of \(P_{s\mathrm f}\), the actual lower quotient is
\(s_L=+1\).  A lower orbit contributes

\[
 \epsilon_\chi\Phi_{r,\sigma}(N)U_0
 \overline{(L_0+L_1)},
\tag{199.D27}
\]

not a difference.  Assigning a negative cellular sign would replace the
literal coefficient.  On the even part, the swapped odd-divisor endpoint
is zero and the source is an ordinary live/dead boundary.  Therefore the
sign-failure piece supplies no lower close-leg gain.

On \(P_{g\mathrm f}\), \(G_{10}>1\).  Equation (199.D12) shows that the
lower scaled map changes \(g\) to \(gG_{10}\), while (199.D14) proves
that the physical inverse formed with the new gcd does not return.  The
one-cross-factor orbit (199.D20) is the least complicated possible repair,
and (199.D3) shows its exact return to \(P_1\).  On strata with more
nontrivial cross factors, the same-g domain tests in (199.D2) remove still
more of these three maps; in particular they cannot repair the already
closed minimal orbit.  Thus neither failure channel completes this aligned
cell.

### 3.6 Operator and power consequences

The obstruction is an identity failure at the physical source, before
Fourier, height, anchor, Farey, or packet operations.  Applying the exact
masked operator afterward must still retain both orientations, both
\(T\)-branches, all endpoint translations, commutators, phases, carries,
births/deaths, selectors, Fourier copies, and zero extensions before the
one outer real part.  None of these operations converts the unproved
\(P_1\) term in (199.D3) into an accepted error by a cellular identity.

The unchanged fixed-packet positive estimate is

\[
 u\{\kappa+M\}X^\varepsilon,
\]

against the sufficient target \(H_B\mathfrak m\kappa uX^\varepsilon\).
On (199.D8), the unresolved ratio is

\[
 \frac{M}{H_B\mathfrak m\kappa}>1.
\tag{199.D28}
\]

At outer physical scale the coefficient-one aligned face retains
\(D_LL^2X^\varepsilon\) capacity against \(L^2X^\varepsilon\).  No
positive power of \(D_L,M,Y,\kappa,L\), or a conductor has been hidden in
\(X^\varepsilon\).  These are upper capacities only.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in the mechanism no-go: the
factorization, recomputed-gcd table, inverse tests, character quotients,
three-state orbit, endpoint identity, and \(P_1\) placement are exact.

The first unproved step of any positive continuation would be a genuinely
new coefficient-sensitive estimate which either prices the literal
coefficient-one \(V_{00}\) term in the unproved \(P_1\) owner or cancels
the complete three-piece operator by a mechanism not based on the scaled
cross-gcd allocation complex.  No permitted dependency supplies such an
estimate.  In particular, neither the numerical nonvanishing of the
surviving coefficient nor a lower mass is proved here.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_physical_even_shift_source` | **Pass.** Equations (199.D4)--(199.D5) retain the exact squarefree even-shift atom and physical mask. |
| `exact_round198_three_piece_complement` | **Pass.** The disjoint complement is exactly (199.D6)--(199.D7); no strict piece is treated as the theorem exit. |
| `exact_open_packet_condition` | **Pass.** Condition (199.D8) is retained after, not inside, the physical orbit. |
| `cross_gcd_four_state_factorization` | **Pass.** Equation (199.D1) and its prime-by-prime proof expose all four pairwise-coprime cross states. |
| `physical_allocation_bijection_and_inverse_cells` | **Mechanism fail, exactly located.** The three same-\(g\) inverse domains are (199.D2); (199.D14) proves failure outside them. |
| `actual_twisted_character_incidence` | **Pass.** The literal quotient table is (199.D15)--(199.D17), with no assigned alternating sign. |
| `aligned_literal_face_first_stress` | **Mechanism fail.** Equations (199.D18)--(199.D19) leave an ordinary coefficient-one jump; the attempted triangle returns (199.D3). |
| `sign_failure_plus_edge` | **Mechanism fail.** Equation (199.D27) is a sum when \(s_L=+1\); an even swapped divisor is an unpaired zero boundary. |
| `changed_gcd_failure_allocation` | **Mechanism fail.** \(G_{10}>1\) changes the recomputed gcd, destroys the physical inverse, and in the minimal cycle forces \(V_{00}\). |
| `safe_boundary_owner_verification` | **Fail for the proposed chain.** Equation (199.D26) places \(V_{00}\) in unproved \(P_1\) for all large shells. |
| `actual_endpoint_cell_difference` | **Pass.** Equations (199.D23)--(199.D24) use the actual four endpoint products and yield the literal residual (199.D3). |
| `packet_and_outer_power_ledger` | **Fail for the theorem, pass as audit.** The exact deficits are (199.D28) and the outer factor \(D_L\). |
| `one_outer_real_part` | **Pass.** No orientation, branch, height, anchor, conductor, frequency, or component modulus is taken; the no-go precedes these operations. |
| `no_kappa1_rectangle_substitution` | **Pass.** The cross-coprime square remains restricted to physical \(\kappa=1\); the \(\xi>1\) orbit requires the missing changed-gcd corner. |
| `no_in_round_owner_pivot` | **Pass.** No alternative analytic owner is proposed. |
| `downstream_scope` | **Pass.** No claim is made for \(P_1\), the rest of original \(t=1\), any other \(t\), either M1 parent, GAR, M2, endpoint uniformity, M9, a bridge, or the circle target. |
| `exponent_quarantine` | **Pass.** The internal \(1/3\), accepted external \(0.3144831759740614\ldots\), and target \(1/4\) records are unchanged. |

The unsigned, character-erased, arbitrary-array, post-Fourier-mask,
deleted-corner, formal-wrap, common-\(\Delta_2\), component-norm, and
capacity-as-mass shadows are all rejected by the exact calculations above.
No computation was used.

## 6. Dependencies and exact artifacts used

This report used exactly the permitted context:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `state/failure_ledger.md`;
5. `strategy/round199_m1_t1_p2_cross_gcd_cellular_boundary_strategy.md`;
6. `proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md`;
7. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`;
8. `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`;
9. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_adjudication.md`;
10. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/synthesis.md`;
11. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`.

The Round-195 kernel supplies the physical source, \(P_2\), packet split,
positive capacities, masked-operator order, and outer ledger.  The
Round-197 kernel and adjudication supply the literal lower edge, sharp code,
actual coefficient product, and the \(\kappa=1\) rectangle boundary.  The
Round-196 kernel quarantines the parity-restored carrier shadow.  The
Round-198 synthesis and seam review fix the complete three-piece theorem
boundary and no-pivot rule.  No sibling Round-199 report, web source,
computation, validation file, proof draft, candidate, or shared synthesis
was used.

## 7. Recommended state effect

**Recommend: retain the graph and record
`p2_cross_gcd_cellular_boundary_self_return_no_go` as mechanism-scoped
candidate evidence.**

Do not promote (199.D9), any strict failure sector, complete \(P_2\), an
owner, a parent, an endpoint theorem, a bridge, the Gauss-circle target, or
an exponent.  If the conductor accepts the no-go after the scheduled
independent reviews, it may record only the following obstruction: the
same-\(G_{00}\) cross-gcd allocation triangle has actual incidence
(199.D22), and its cellular completion necessarily returns the
coefficient-one \(G_{00}\) corner (199.D3), which lies in unproved
\(P_1\) on large aligned shells.  No in-round analytic pivot is licensed.
