# Round 132 discovery report: literal ratio-phase hyperbolic map

Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`

Task: `literal_ratio_phase_hyperbolic_map`

Starting graph SHA-256:
`328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`

## 1. Result: exact affine chart, but a source-level no-go

The ratio phase has an **exact**, not merely Morse-theoretic,
hyperbolic-paraboloid chart.  Put

\[
 P_i={cL\over \kappa_iD},\qquad
 U={u\over L},\qquad V={v\over D},\qquad
 \xi=V,\quad \eta=-{U\over V},\quad \zeta=-U.
 \tag{132.1}
\]

Then \(\zeta=\xi\eta\), and

\[
 \Phi_i(u,v)=-{cu\over \kappa_i v}=P_i\eta.
 \tag{132.2}
\]

Equivalently, the ambient linear map

\[
 (u,v,w)\longmapsto
 \left({v\over D},{w\over P_i},-{u\over L}\right)
 \tag{132.3}
\]

sends the graph \(w=-cu/(\kappa_i v)\) exactly to
\(\mathbb H=\{(\xi,\eta,\xi\eta)\}\).  Thus the curvature identity from
Round 131 is genuinely compatible with the Demeter--Wu surface.

The determinant taper selects the anisotropic ratio width

\[
 h_i={\kappa_iD\over WL}=Y^{-5/48+o(1)}.
 \tag{132.4}
\]

After translating an \(h_i\)-cell in \(\eta\) and dilating only the
\(\eta\)-coordinate, the exact source scale is

\[
 \boxed{R=P_i h_i={c\over W}\asymp {D^2\over W}
       =Y^{27/48+o(1)}.}
 \tag{132.5}
\]

At that scale, for two rays \(r=(a,b)\), \(r'=(a',b')\),

\[
 \Delta\xi={b'-b\over D},\qquad
 \Delta\widetilde\eta
 ={\eta'-\eta\over h_i}
 ={W(ab'-a'b)\over \kappa_i bb'}.
 \tag{132.6}
\]

Hence Demeter--Wu transversality is exactly simultaneous denominator
separation \(|b-b'|\asymp D\) and top-size normalized determinant
\(Wn/(\kappa_i bb')\asymp1\).  Same-denominator packets lie on a ruling
and are not transverse.

Nevertheless, the direct use of Demeter--Wu Theorems 1.6 or 1.10 is ruled
out at the frozen interface.  The first invalid inference would be to write
the literal broad coefficient matrix as one product of two independently
owned extension functions.  Its coefficient

\[
 B_i(r,r')=A_i(r)H_{i;r,p}(n)C_{i;r,p}(n)
 \tag{132.7}
\]

is joint in \((r,r')\): the variable primitive lift, Möbius/Stieltjes
profiles, thresholds, taper, stars, cells, signs, aliases, and half-open
owners do not factor.  A finite rank decomposition is tautologically
possible, but the source estimate must then be summed with its projective
tensor/nuclear cost, for which the supplied outer norms give no bound.
Even after granting such a factorization, the source controls a bilinear
\(L^2\) integral, not cancellation at the one prescribed centre.  The
refined incidence factor is maximal at the \(R^{1/2}\)-ball containing that
centre, because every wave packet contributing there meets that ball.

Finally, the nontransverse same-denominator M1/M2 controls remain a complete
narrow term.  One ratio cell has the accepted capacity \(Y^{30/48+o(1)}\),
and the \(Y^{5/48+o(1)}\) cells recover the full
\(Y^{35/48+o(1)}\) upper capacity.  Thus even a perfect broad estimate from
the source would not give a complete exponent below \(27/48\).

The unique terminal label is therefore

\[
 \boxed{\texttt{source_level_no_go}}.
 \tag{132.8}
\]

This is a no-go for deducing the required literal fixed-centre bound from
the two cited source theorems and the presently supplied project data.  It
is not a no-go for a new arithmetic narrow estimate or a new
owner-preserving pointwise decoupling theorem.

## 2. Exact statement and hypotheses

Fix

\[
 W=Y^{7/16},\quad D=Y^{1/2},\quad L=Y^{1/6},\quad c\asymp Y,
 \quad \kappa_1=1,\quad\kappa_2=4,
 \tag{132.9}
\]

and the literal Round-131 top-shell scalar

\[
 \mathfrak O_{i,D}^{+}(c)
 =\sum_{r=(a,b)}^{\rm lit}A_i(r)
   \sum_{n>0}^{\rm lit}\sum_{p\in\Lambda_{i,r}(n)}
   H_{i;r,p}(n)C_{i;r,p}(n)
   e\!\left({cn\over\kappa_i b b'_{r,p}(n)}\right).
 \tag{132.10}
\]

Here \(a'=a+p\), \(n=ab'-a'b\),
\(\#\Lambda_{i,r}(n)=O(1)\), and every physical coefficient and owner in
Round 131 is retained before an absolute value.  The available outer data
are only

\[
 \|A_i\|_{\ell^1}\ll DY^\varepsilon,
 \qquad
 \|A_i\|_{\ell^2}^2\ll {D\over L}Y^\varepsilon.
 \tag{132.11}
\]

No fully reassembled inner \(\ell^2\) norm, low-cost tensor factorization,
or fixed-centre trace estimate is assumed.

The source statements used here were checked in the official v2 source of
Ciprian Demeter and Shukun Wu, *Restriction and decoupling estimates for the
hyperbolic paraboloid in \(\mathbb R^3\)*,
[arXiv:2505.09037v2](https://arxiv.org/abs/2505.09037v2) (Definitions 1.2,
1.3, 1.9 and Theorems 1.6, 1.10; official
[source archive](https://arxiv.org/src/2505.09037v2)).  The source facts used
are exactly these:

1. transverse patches are separated by constants in **both** \(\xi\) and
   \(\eta\);
2. Theorem 1.6 bounds \(\int_{\mathbb R^3}|f_1f_2|^2\) by the product of
   positive cap \(L^4\) square sums for functions Fourier supported in
   \(N_{1/R}(\mathbb H)\), with caps of side \(R^{-1/2}\);
3. Theorem 1.10 has the same integral direction for scale-\(R\) wave
   packets, with the positive incidence factor \((M_1M_2)^{1/2}\); and
4. neither theorem is a fixed-point exponential-sum estimate or an
   arithmetic signed-coefficient theorem.

Items (132.1)--(132.7), the parameter map below, and all capacity conclusions
are project derivations, not statements of the source paper.

## 3. Proof and derivation

### 3.1 Exact cell normalization

Choose a half-open \(\eta\)-cell of length \(h_i\), with base point
\((\xi_0,\eta_0)\), and set

\[
 X=\xi-\xi_0,qquad H={\eta-\eta_0\over h_i},qquad
 Z={\zeta-\eta_0\xi-\xi_0\eta+\xi_0\eta_0\over h_i}.
 \tag{132.12}
\]

Since \(\zeta=\xi\eta\), this is the exact affine identity \(Z=XH\).
Moreover,

\[
 e(\Phi_i(u,v))=e(P_i\eta_0)e(RH).
 \tag{132.13}
\]

The top shell has \(X\)-diameter \(O(1)\), and an ordered pair with taper
support crosses only \(O(1)\) adjacent half-open \(H\)-cells.  Constant
translations and bounded dilations put these patches inside the source's
\([-1,1]^2\) convention without changing a power of \(Y\).

The M1 branches \(e(\pm b'/4)\) add a physical \(X\)-coordinate of size
\(O(D)\).  Expanding the M2 \(\chi_4(a')\) into its two quarter branches
adds a linear functional of \(\zeta=\xi\eta\), whose three coordinates
after (132.12) have size \(O(L)\).  Since
\(D,L<R=Y^{9/16+o(1)}\), all such finite carrier branches still live in an
\(O(R)\) physical ball.  This observation changes no coefficient owner and
supplies no cancellation.

The exact continuous Jacobians are

\[
 d\xi\,d\eta={du\,dv\over DL\xi},
 \qquad
 dX\,dH={du\,dv\over DLh_i\xi}.
 \tag{132.14}
\]

Thus the transformed integer lattice has covolume
\(\asymp(DLh_i)^{-1}=W/(\kappa_iD^2)\asymp R^{-1}\).  There are on average
\(O(1)\) arithmetic atoms per source cap, but this is only an average:
rational strips may cluster.  Replacing the discrete atoms by a Lebesgue
density would require the Jacobian in (132.14); it may not be silently
absorbed into \(A_i\) or \(H_{i;r,p}\).

### 3.2 Coordinate, scale, cap, norm, and owner table

| Project datum | Exact source datum | Size/effect |
|---|---|---|
| \((u,v,w=-cu/(\kappa_i v))\) | \((\xi,\eta,\zeta)=(v/D,w/P_i,-u/L)\) | Exact \(\zeta=\xi\eta\); ambient affine map. |
| Ratio cell | \(H=(\eta-\eta_0)/h_i\) | \(h_i=\kappa_iD/(WL)=Y^{-5/48+o(1)}\). |
| Centre phase | physical point \((0,R,0)\), up to carriers and constants | \(R=P_ih_i=c/W=Y^{27/48+o(1)}\). |
| Taper/determinant | \(H'-H\) | \(H'-H=Wn/(\kappa_i bb')\in(0,1)\). |
| Denominator separation | \(X'-X\) | \((b'-b)/D\). |
| Source cap | \(R^{-1/2}\)-square | side \(Y^{-27/96+o(1)}\). |
| Pullback cap in \(b\) | denominator window | \(\Delta b\ll DR^{-1/2}=Y^{21/96+o(1)}\). |
| Pullback cap in \(a/b\) | ratio window | \(\Delta(a/b)\ll R^{-1/2}/W=Y^{-69/96+o(1)}\). |
| Pullback numerator strip | fixed-\(b\) width | \(D R^{-1/2}/W=Y^{-21/96+o(1)}<1\); nevertheless a cap can contain \(O(DR^{-1/2})\) points along a rational strip. |
| Fourier thickness | \(N_{1/R}(\mathbb H)\) | normal thickness \(R^{-1}=Y^{-27/48+o(1)}\); the arithmetic atoms themselves have zero thickness and need an explicit mollification. |
| Outer coefficients | same discrete weights | \(\ell^1\ll D\), \(\ell^2{}^2\ll D/L\); reindexing gives no extra norm gain. |
| Inner coefficients | joint matrix \(B_i(r,r')\) | no supplied factorization or fully reassembled \(\ell^2\) estimate. |
| M1/M2 carriers | finite physical-coordinate shifts | sizes \(D\) and \(L\), both below \(R\); signs remain literal. |
| Primitive moduli, thresholds, stars, taper, aliases, cells, signs | coefficient/owner data | unchanged and joint; not hypotheses or conclusions of the source theorem. |

The cap count is not uniformly one.  Indeed, the cap conditions imply an
interval of \(O(DR^{-1/2})\) possible denominators and a numerator strip of
width less than one for each denominator.  Hence the unconditional cap
occupancy is only

\[
 \#(\text{lattice points in one cap})
 \ll 1+DR^{-1/2}=Y^{21/96+o(1)},
 \tag{132.15}
\]

and near-rational affine strips can realize polynomial clustering.  The
average-one covolume calculation therefore cannot be used as a pointwise cap
norm.

### 3.3 Legal broad--narrow split

After a fixed constant subdivision of each normalized cell, call a pair
`broad` only when

\[
 {|b-b'|\over D}\asymp1,
 \qquad
 {Wn\over\kappa_i bb'}\asymp1.
 \tag{132.16}
\]

Then every pair of the corresponding small squares is transverse in the
exact sense of Definition 1.2, so the geometry passes.  The complement is
the union of

\[
 \mathcal N_\xi:\ |b-b'|\ll D,
 \qquad
 \mathcal N_\eta:\ Wn/(\kappa_i bb')\ll1.
 \tag{132.17}
\]

The second part can be dyadically zoomed: at determinant height
\(2^{-j}D^2/W\), the same calculation gives source radius
\(R_j=2^{-j}c/W\), down to \(R_j\asymp1\) when \(n\asymp1\).  This is only a
partition, not a saving.  The first part contains the exact ruling
\(b=b'\).  No rescaling makes two points with identical \(\xi\) transverse
in both source coordinates.

In particular, the accepted same-denominator, nonzero-determinant M1 and M2
packets are legal members of \(\mathcal N_\xi\), not exceptional points to
discard.  Their length is \(D/W=Y^{3/48}\), and the quarter/character carrier
may be coherent on one fixed outer ray at the aligned centres recorded in
Round 131.

### 3.4 Coefficient and fixed-centre seams

On a transverse rectangle pair the literal broad part is a bilinear form

\[
 \sum_{r\in\tau_1}\sum_{r'\in\tau_2}
 B_i(r,r')e\big(R(H'-H)+\text{finite carrier}\big).
 \tag{132.18}
\]

Demeter--Wu instead applies to one product \(F_1F_2\), whose coefficient
matrix is a tensor product.  To use it on (132.18), one first needs an exact
owner-preserving decomposition

\[
 B_i|_{\tau_1\times\tau_2}
 =\sum_\nu \alpha_\nu\otimes\overline{\beta_\nu}
 \tag{132.19}
\]

and a bound for the sum of the resulting source norms.  SVD proves existence
of (132.19) but not an affordable norm; applying the theorem termwise and
then taking a triangle charges precisely the missing projective/nuclear
cost.  The two norms in (132.11) concern only \(A_i(r)\), not the joint
matrix (132.7), and do not supply that cost.

Even conditionally on (132.19), define

\[
 \mathcal D_R(F)=
 \left(\sum_{\theta:R^{-1/2}\text{-cap}}\|F_\theta\|_4^2\right)^{1/2}.
 \tag{132.20}
\]

The source theorem and a unit-scale Bernstein trace for the bounded Fourier
support of \(F_1F_2\) give only the project-derived inequality

\[
 |F_1(x_c)F_2(x_c)|
 \ll R^{\varepsilon}\mathcal D_R(F_1)\mathcal D_R(F_2).
 \tag{132.21}
\]

It has no negative power of \(R\).  For the direct cap-scale thickening of
surface atoms, normalized to equal the arithmetic exponential at \(x_c\),
one packet has dual dimensions \(R^{1/2}\times R^{1/2}\times R\) and
\(L^4\)-norm \(\asymp R^{1/2}\).  Consequently the elementary legal
realization gives

\[
 \mathcal D_R(F_\alpha)
 \ll R^{1/2}
 \left(\sum_\theta
       \left(\sum_{r\in\theta}|\alpha_r|\right)^2\right)^{1/2},
 \tag{132.22}
\]

and (132.21) carries the positive factor \(R=Y^{27/48+o(1)}\) before the
unknown cap coefficient functional.  This is a valid localization control,
not an assertion that every possible arithmetic realization must pay exactly
that factor.  It shows that the source theorem itself supplies no fixed-centre
power saving.

For Theorem 1.10, every wave packet that contributes nonnegligibly at
\(x_c\) intersects the \(R^{1/2}\)-ball containing \(x_c\).  Thus the
relevant \(M_j\) is the full local packet incidence, not a small quantity.
No supplied arithmetic incidence estimate lowers it.  The refined theorem
therefore does not repair the trace seam.

Both source inequalities put absolute values around \(F_1F_2\) and use
positive cap or packet norms.  They are valid for phase-adapted coefficients.
Accordingly, they cannot be credited with cancellation from the literal
Vaaler, Möbius, quarter, or \(\chi_4\) signs unless that cancellation is first
proved in (132.19)--(132.22).  A positive square function or Gram operator is
not the scalar (132.10).

### 3.5 Capacity verdict

Let

\[
 C={WL\over D}=Y^{5/48+o(1)},
 \qquad R_0={D\over W}=Y^{3/48}.
 \tag{132.23}
\]

The fixed-outer-ray, fixed-inner-numerator scale is \(K_D/L\).  Hence the
available ledger is

| Stratum/mechanism | Capacity | Verdict |
|---|---:|---|
| One ratio/determinant cell, including an aligned length-\(R_0\) packet | \(D R_0K_D/L=Y^{30/48+o(1)}\) | Narrow control; not a family lower bound, but cannot be discarded. |
| All \(C\) cells with current owners | \(CDR_0K_D/L=DK_D=Y^{35/48+o(1)}\) | Current complete upper capacity. |
| Broad transverse cells | at most the same raw cell ledger | Geometry is source-eligible, but (132.19)--(132.22) supply no signed fixed-centre bound. |
| \(\xi\)-narrow/ruling part | up to \(Y^{35/48+o(1)}\) over the complete cell cover | Contains the accepted M1/M2 same-denominator controls. |
| \(\eta\)-narrow dyadic descendants | radii \(R_j=2^{-j}R\) | Rescaling is exact; without a new coefficient theorem, summing descendants returns the raw owner ledger. |
| Threshold, star, taper-boundary, variable-modulus, sign, and half-open owner pieces | already included in \(Y^{35/48+o(1)}\) | Source smoothing neither deletes nor estimates them. |
| Ideal one term per outer ray | \(DK_D/L=Y^{27/48+o(1)}\) | Exactly the persistence threshold; no strict improvement. |
| Determinant target | \(D=Y^{24/48}\) | Needs a further \(Y^{-3/48}=Y^{-1/16}\) after the ideal per-ray collapse. |

Thus the broad theorem cannot produce a **complete** sub-\(27/48\) result
while the narrow ruling and fixed-centre coefficient seams are left at their
accepted prices.  The conclusion remains true even if the broad contribution
is granted for free.

## 4. First doubtful or unproved step

The first unavailable statement is the following owner-preserving
coefficient bridge:

> For every literal transverse cell pair, decompose the complete physical
> matrix (132.7) as in (132.19), without moving an absolute value through a
> Möbius/Stieltjes sum or changing a threshold/star/owner, and bound the sum
> of the fixed-centre source functionals
> \(\sum_\nu\mathcal D_R(F_{\alpha_\nu})
> \mathcal D_R(F_{\beta_\nu})\) with a strict cross-ray power saving.

Neither (132.11) nor Demeter--Wu Theorem 1.6/1.10 implies this statement.
The source theorem begins only after the two independent functions already
exist; it does not factor a joint arithmetic kernel, estimate its projective
norm, or turn its bilinear integral into signed cancellation at the prescribed
centre.  This is the first exact mismatch, before any exponent can be
credited.

Even if that bridge were postulated for the broad part, a second, separately
necessary hypothesis would be an arithmetic estimate for the ruling/narrow
part (132.17), retaining the aligned M1/M2 controls.  Without it the complete
capacity remains \(35/48\).  These missing statements are project theorems,
not omitted clauses of the Demeter--Wu source.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| `hyperbolic_surface_normalization` | Pass exactly: (132.1)--(132.3) give an ambient affine map to \(\zeta=\xi\eta\). |
| `transversality_in_both_coordinates` | Pass only for (132.16). Separation in determinant/ratio alone is insufficient. |
| `Fourier_support_thickness_and_cap_scale` | Pass as a parameter map: \(R=c/W\), thickness \(R^{-1}\), caps \(R^{-1/2}\); an arithmetic atom still needs explicit mollification. |
| `fixed_centre_scalar_vs_bilinear_L4_integral` | Source-level no-go: (132.21) has only positive source norms, and the elementary atom thickening has the cost (132.22). The refined incidence is maximal at the centre ball. |
| `actual_coefficient_norm_and_absolute_value_direction` | Red: only (132.11) is known; the joint projective norm of (132.7) is missing. Source absolute values cannot be counted as arithmetic sign cancellation. |
| `broad_narrow_ruling_partition` | Pass geometrically via (132.16)--(132.17); no analytic narrow saving follows. |
| `same_denominator_M1_M2_aligned_packets` | Pass as hostile controls: they are \(\xi\)-narrow ruling packets of length \(D/W\), with one-cell capacity \(30/48\). They are not lower bounds for the full scalar. |
| `variable_primitive_moduli_thresholds_and_owners` | Retained in (132.7), (132.10), and the owner table. No common modulus, low-BV envelope, or smoothing deletion is inferred. |
| `capacity_35_27_24_over_48` | Pass: the complete/current, ideal-per-ray, and determinant capacities are respectively \(35/48\), \(27/48\), and \(24/48\); the final gap is \(3/48\) after ideal per-ray collapse. |
| `no_positive_energy_or_global_promotion` | Pass: no positive Gram, arbitrary-coefficient operator norm, global exponent, M9 component, endpoint, bridge, or quarter conclusion is asserted. |

The work was 100% analytical/algebraic.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Only the permitted selected context was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, at the Round-132 starting graph, especially
   the actual determinant-correlation, top-shell bounded-lift,
   post-inner support, outer-energy obstruction, fixed-lift Fourier kernel,
   and residue-interlacing nodes;
3. `state/active_campaign.yml`;
4. `strategy/conductor_0823_full_proof_strategy.md`;
5. the Round-132 `blind_statement.md`;
6. the Round-131 synthesis, conductor adjudication, and
   `literal_induced_residue_weight_derivation.md`;
7. the Round-130 post-inner/outer synthesis; and
8. the official Demeter--Wu arXiv v2 abstract/source linked in Section 2,
   solely for the stated source definitions, theorem directions, Fourier
   support, cap scale, wave-packet incidence, and affine-rescaling facts.

No Round-132 sibling report, secondary source, computation, or unpermitted
historical derivation was used.

## 7. Recommended state effect

**Retain** the exact affine normalization (132.1)--(132.6) and the natural
anisotropic source scale

\[
 R={c\over W}=Y^{9/16+o(1)}
\]

as candidate geometric evidence.  **Retain** the exact broad criterion
(132.16) and classify same-denominator packets as narrow hyperbolic rulings.

Record the scoped terminal result `source_level_no_go`: Demeter--Wu Theorems
1.6 and 1.10, under the currently available literal coefficient data, do not
bound the Round-131 prescribed-centre scalar.  The first missing interface is
the owner-preserving joint-coefficient/fixed-centre bridge in Section 4, and
the complete route additionally needs a separately priced narrow-ruling
arithmetic theorem.

Keep `GC-W7-16-actual-reduced-determinant-correlation` open and the complete
fixed-block bound at \(Y^{35/48+\varepsilon}\).  Make no global exponent,
M9-M1, M9-M2, endpoint, bridge, M9, conditional-bridge, or quarter promotion.
