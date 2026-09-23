# Round 193 hostile core-projection, arithmetic-mask, and power audit

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Task: `core_projection_mask_power_hostile_audit`
- Role: barrier/no-go
- Research round: 193
- Starting graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Status: candidate evidence only; no shared-state edit
- Resource use: entirely analytical/algebraic; no numerical or external-theorem evidence

## 1. Result: the finite involution passes, a sharper determinant count pays the physical sector, and post-Abel masking needs one exact repair

The proposed scaled map is a genuine fixed-point-free, multiplicity-one
involution on the live cofactor-coprime (r\equiv2\pmod4) opened
subsector.  It preserves the two endpoint products, their order, the shift,
the Fejer weight, the square-root phase, the original character-leg gcd,
cofactor gcd one, squarefreeness, allocation coprimality, parity, and the
canonical primitive carrier.  It reverses the product of the two
(\chi _4)-characters before any absolute value.  In the primitive
coordinates of the question it is exactly

\[
 (U,v,S,w,+)\longmapsto(v,U,w,S,-).
\tag{193.H1}
\]

Neither (k=1) nor (r\equiv2\pmod4) is needed for the power theorem.
Let (P_{\rm cl}) be the two-sided close mask on the complete opposing
even-shift source, imposing only

\[
 |d-gm|\le D_L,\qquad |d'-gm'|\le D_L,\qquad g=(d,d').
\tag{193.H1a}
\]

Thus (P_{\rm sw}=P_{\rm cl}\mathbf1_{(m,m')=1}
\mathbf1_{r\equiv2\ (4)}) is only a strict submask on which the
involution and sign are available.  There is a stronger and safer power
repair than the proposed common-cell commutator estimate.  On the
two-sided close active support, the strict hard cone and either close
inequality force (g=O(1)).  The
two close inequalities imply

\[
 S+w\ll D_L/g,
 \qquad |\kappa(v-U)|\ll D_L/g.
\tag{193.H2}
\]

For fixed ((\kappa,g,U,v,w)), the determinant and Fejer-shift bound

\[
 0<h=Sv-Uw<{R_0\over2\kappa g}
\tag{193.H3}
\]

confine (S) to an interval of length
(R_0/(2\kappa gv)=O(1)), because every nonzero original physical atom
has (v\asymp L/\kappa).  Consequently the complete number of physical
close atoms in both orientations is

\[
 \begin{aligned}
 \#\mathcal P_{\rm cl}
 &\ll
 \sum_{\kappa\ll L}\sum_{g=O(1)}
 {L\over\kappa}
 \left(1+{D_L\over\kappa g}\right)
 \left(1+{D_L\over g}\right)\\
 &\ll L D_L\log(2L)+L D_L^2
 \ll L^2\log(2L).
 \end{aligned}
\tag{193.H4}
\]

The dyadic restriction (Y<h\le2Y) only deletes these atoms; (h) is
already determined by ((U,v,S,w)) and is not an additional (Y)-fold
multiplicity.  Since the literal endpoint product is pointwise
(O_\varepsilon(X^\varepsilon)), (193.H4) proves the stronger absolute
physical estimate

\[
 \boxed{
  |\mathscr F_Y^\sigma[P_{\rm cl}]|
  \ll_{B,\varepsilon}L^2X^\varepsilon .}
\tag{193.H5}
\]

Thus no BV, collar, character, or phase cancellation is actually needed
to pay the complete physical close sector.  The proposed common-cell and
collar ledgers also pass independently: the deliberately coarse count in
the strategy, multiplied by the common-cell (D_L/L) difference, is

\[
 O(D_L^3\log(2L)+D_L^4)=O(L^2X^\varepsilon),
\tag{193.H6}
\]

and a fixed crossed normalized-BV increment or literal face has
multiplicity

\[
 \sum_{\kappa\ll L}
 O\!\left(D_L^2\left(1+{D_L\over\kappa}\right)^2\right)
 \ll L D_L^2+D_L^3\log(2L)+D_L^4
 \ll L^2X^\varepsilon.
\tag{193.H7}
\]

The passage through Rounds 187--192 is valid only with one precise
operator convention.  The physical mask must be inserted
coordinatewise in every source amplitude before the complete anchor
Fourier expansion and before height differencing; every accepted safe
projector is then rerun on that masked source.  With this convention all
inherited safe proofs remain absolute after deletion, and linearity gives

\[
 \boxed{
 \mathscr R_{{\rm core},Y,Q}^\sigma[P_{\rm cl}]
 =\mathscr F_Y^\sigma[P_{\rm cl}]
  -\mathscr S_{\le192,Y}^\sigma[P_{\rm cl}],
 \qquad
 |\mathscr R_{{\rm core},Y,Q}^\sigma[P_{\rm cl}]|
 \ll_{B,\varepsilon}L^2X^\varepsilon .}
\tag{193.H8}
\]

This includes the exact (T=0) convention: at (T=0) the Round-192
Farey projection is zero and the core is the whole inherited rho-large
remainder before the new physical restriction.

There is one exact failure if (P_{\rm cl}\mathscr R_{\rm core}) is
instead interpreted as post-Abel termwise multiplication of the already
formed jump packet.  For a physical mask (P_h),

\[
 \Delta^-(P W)(h)
 =P_h\Delta^-W(h)+(P_h-P_{h-1})W(h-1),
\tag{193.H9}
\]

so in general

\[
 {1\over1-z}\sum_hP_h\Delta^-W(h)z^h
 \ne \sum_hP_hW(h)z^h.
\tag{193.H10}
\]

The missing term is the physical-mask birth/death commutator.  It is not
discarded in (193.H8): recomputing (\Delta^-(PW)) puts it in the new
core.  Formula (193.H10) is the first invalid equality in an unqualified
post-expansion reading of the strategy.  It is a literal algebra issue,
not an operator-capacity obstruction.  After the coordinatewise repair,
no mask, Fourier, BV, collar, or power seam blocks the full two-sided
close sector.  The verified (k=1,r\equiv2\pmod4) involution is genuine
algebra but is unused in the stronger estimate.

The strongest supported terminal conclusion is therefore

\[
 \boxed{\texttt{strict\_rho\_large\_gcd\_scaled\_orientation\_sector}.}
\tag{193.H11}
\]

It is not a complete rho-large, complete original-(t=1), parent,
bridge, theorem, or exponent result.

## 2. Exact statement and hypotheses

Fix the exact accepted Round-192 source with real (X\ge2), one
nonempty literal middle or lower residual hard-M1 shell (L\ge2), one
sign (\sigma\in\{+1,-1\}), fixed (B>0),

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,
 \qquad R_0=\lceil L\rceil,
 \qquad D_L=\lceil L^{1/2}\rceil,
\tag{193.H12}
\]

and a nonempty dyadic high-height block (Y<h\le2Y), (Y>Q).  Retain
the exact Round-188--192 predicates

\[
 U=m_0q>4Q,\qquad q>Q,\qquad m_0|a|_q>Q,\qquad Qm_0<Y,
\tag{193.H13}
\]

the fast projective band, the rho-large condition and, for (T\ge1),
all strict Farey-covector inequalities.  Here (m_0) is the Fourier
lift gcd and is not either physical cofactor (m,m').  At (T=0), the
Farey selector is exactly empty and no covector inequality is imposed.
Every orientation, sign, product, phase, Fejer weight, endpoint order,
lower conjugation, selector, cell, floor, star, half weight, hard sample,
crossing, endpoint trace, affine birth/death, and zero extension remains
literal.

Open one opposing physical incidence as

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd},\qquad
 0<r<R_0,\qquad2\mid r.
\tag{193.H14}
\]

Put (g=(d,d')) and (k=(m,m')).  On the subsidiary sector (k=1)
define

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g),
\tag{193.H15}
\]

where the displayed order is lower character divisor, lower
complementary factor, upper character divisor, upper complementary
factor.  The primary physical mask is

\[
 P_{\rm cl}(d,m,d',m')=
 \mathbf1_{|d-gm|\le D_L}
 \mathbf1_{|d'-gm'|\le D_L}.
\tag{193.H16}
\]

It is imposed on every opposing atom of the inherited even-shift
source, with no restriction on (k) or on (r\bmod4).  The narrower
involution mask is

\[
 P_{\rm sw}=P_{\rm cl}\mathbf1_{k=1}
             \mathbf1_{r\equiv2\ (4)}.
\tag{193.H16a}
\]

For any physical source amplitude (B_x), where (x) includes its
orientation, height, affine site, both ordered endpoints, and every
literal field, write

\[
 B_x[P_{\rm cl}]=P_{\rm cl}(x)B_x.
\tag{193.H17}
\]

All Fourier expansions, lift partitions, projective cuts, height
differences, terminal/Fejer decompositions, and the Round-192 Farey
projection in (193.H8) are evaluated on (193.H17).  Geometric carrier
intervals and canonical anchors remain the original ones; an interior
zero created by (P_{\rm cl}) is a zero-extended coefficient, not a
license to replace the carrier by a new convex hull.  This makes every
operator linear and gives the exact additivity

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 +\mathscr R_{\rm core}[1-P_{\rm cl}]
 =\mathscr R_{\rm core}[1].
\tag{193.H18}
\]

The first-failure ordered complement of (193.H16), inside the exact
even-shift Round-192 source, is

\[
 \begin{array}{ll}
 \mathcal C_1:&|d-gm|>D_L,\\
 \mathcal C_2:&|d-gm|\le D_L,\quad |d'-gm'|>D_L.
 \end{array}
\tag{193.H19}
\]

These two sets are disjoint in the displayed first-failure order.  No
density, nonemptiness, or coefficient lower mass is asserted for either.

## 3. Proof and hostile derivation

### 3.1 Parity, integrality, gcds, involution, and character reversal

Because (d,d') are odd and (r=d'm'-dm) is even, (m,m') have the
same parity.  On (k=(m,m')=1) they cannot both be even, so both are
odd.  Since (g\mid d,d'), (193.H15) is integral and all four image
entries are odd.

The products and shift are unchanged:

\[
 (gm)(d/g)=dm=N,qquad
 (gm')(d'/g)=d'm'=N+r.
\tag{193.H20}
\]

Moreover

\[
 (gm,gm')=g(m,m')=g,qquad
 (d/g,d'/g)=1.
\tag{193.H21}
\]

Thus the image has the same character-leg gcd and cofactor gcd one.
Using that same canonical gcd on the image, a second application gives

\[
 \tau_g^2(d,m,d',m')=(d,m,d',m').
\tag{193.H22}
\]

The signs of (d'-d) and (m'-m) are interchanged in the image, so the
two opposing orientations are bijected.  A fixed point would require
(d=gm) and (d'=gm').  Since (m,m') are odd, then
(r=g(m'^2-m^2)\equiv0\pmod8), contrary to (r\equiv2\pmod4).
Hence every orbit in (193.H16) has size two.

For odd numbers, complete multiplicativity of (\chi _4), (193.H20),
and (N+r\equiv N+2\pmod4) give

\[
 \begin{aligned}
 &\{\chi_4(d')\chi_4(d)\}
   \{\chi_4(gm')\chi_4(gm)\}\\
 &\qquad=\chi_4(d'm')\chi_4(dm)
 =\chi_4(N+r)\chi_4(N)=-1.
 \end{aligned}
\tag{193.H23}
\]

Therefore

\[
 \boxed{\chi_4(d')\chi_4(d)
 =-\chi_4(gm')\chi_4(gm).}
\tag{193.H24}
\]

No absolute value has been used in this derivation.

If the two products are squarefree, every factorization in (193.H20) is
allocation-coprime and squarefree.  Indeed (g\mid d) and
((d,m)=1) give ((g,m)=1), so (gm\mid N), and similarly at the
upper endpoint.  Thus squarefreeness, divisor status, allocation
coprimality, and oddness survive on both orbit legs.

### 3.2 Canonical primitive coordinates

Take the plus representative

\[
 d=\kappa gU,\qquad d'=g(\kappa U+2S),\qquad
 m'=\kappa v,\qquad m=\kappa v+2w,\qquad
 Sv-Uw=h>0.
\tag{193.H25}
\]

Its image is

\[
 \begin{array}{ll}
 d_{\rm new}'=\kappa gv,&
 d_{\rm new}=\kappa gv+2gw,\\
 m_{\rm new}=\kappa U,&
 m_{\rm new}'=\kappa U+2S.
 \end{array}
\tag{193.H26}
\]

This is the canonical minus parametrization with

\[
 (U',v',S',w')=(v,U,w,S),qquad
 U'w'-v'S'=vS-Uw=h.
\tag{193.H27}
\]

The only potentially hidden seam is preservation of the inward cross
gcd (\kappa).  On a live squarefree product,
(d=\kappa gU) is squarefree, hence (\kappa,g,U) are pairwise
coprime.  The inherited primitive domain gives ((gU,v)=1).  Therefore

\[
 (d_{\rm new}',m_{\rm new})
 =(\kappa gv,\kappa U)=\kappa.
\tag{193.H28}
\]

Also (k=1) and oddness give

\[
 1=(\kappa v+2w,\kappa v)=(w,\kappa v),
\tag{193.H29}
\]

so ((v,w)=1).  Hence

\[
 (gv,U)=1,qquad (v,h)=(v,Uw)=1,
\tag{193.H30}
\]

which are exactly the new primitive-domain and ((U',h)=1)
conditions.  Finally ((gv,gw)=g), so the primitive gcd label is
canonical after the swap.  This proves (193.H1) with no remembered-label
convention.

Equations (193.H20) and (193.H27) show that (r=2\kappa gh), the
dyadic height, the Fejer factor (1-r/R_0), and the square-root product
phase are identical.  The lower product remains lower and the upper
product remains upper, so the transformed term is

\[
 \lambda_{N+r,\sigma}(gm')
 \overline{\lambda_{N,\sigma}(gm)},
\tag{193.H31}
\]

with the lower endpoint still conjugated.

### 3.3 Close mask, active (g), and the complete atom count

Return now to the complete opposing even-shift source and drop both
(k=1) and (r\equiv2\pmod4).  The canonical plus/minus tangent
coordinates (193.H25) and the determinant identity remain valid there;
only the involution-specific conclusions (193.H27)--(193.H30) used the
narrower hypotheses.

From (193.H25), the two close conditions are

\[
 |\kappa(v-U)+2w|\le D_L/g,qquad
 |-\kappa(v-U)+2S|\le D_L/g.
\tag{193.H32}
\]

Adding the expressions inside the absolute values gives (2(S+w)),
so

\[
 S+w\le D_L/g,qquad
 |\kappa(v-U)|\le3D_L/g.
\tag{193.H33}
\]

Under (193.H27), both close differences merely change sign.  Hence the
subsidiary mask (P_{\rm sw}) is exactly orbit-invariant.  No invariance
claim is made for the wider (P_{\rm cl}) when (k>1), and none is needed.

Consider a nonzero original physical atom in (P_{\rm cl}).  Its lower
strict hard ratio satisfies (4<d/m<16), and

\[
 \left|g-{d\over m}\right|\le {D_L\over m}.
\tag{193.H34}
\]

Since every live lower cofactor satisfies (m\asymp L), there is an
absolute (G_0) and an (L_0) such that (g\le G_0) for (L\ge L_0).
The finitely many smaller shells are absorbed in the same final bound.
This proves the required active-support (g=O(1)), not merely
(g\le D_L).

For fixed ((\kappa,g)), the active box gives (O(L/\kappa)) choices
of (U).  Equation (193.H33) gives
(O(1+D_L/(\kappa g))) choices of (v) and
(O(1+D_L/g)) choices of (w).  For fixed (U,v,w), (193.H3) puts
(S) in

\[
 {Uw\over v}<S<{Uw\over v}+{R_0\over2\kappa gv}.
\tag{193.H35}
\]

On the original live active box (v\asymp L/\kappa), so this interval
contains (O(1)) integers.  Summing yields (193.H4).  This proof counts
each opened incidence once because the plus/minus parametrizations are
canonical and only the plus representative of each two-point orbit is
used.  Restoring both orientations changes only an absolute constant.

The capacity ledger is therefore

| item | bound before (X^\varepsilon) | outcome at (D_L=\lceil\sqrt L\rceil) |
|---|---:|---:|
| complete close physical atoms | (LD_L\log(2L)+LD_L^2) | (O(L^2\log(2L))) |
| pointwise endpoint product | (O(X^\eta)) | absorbed with fresh (\eta<\varepsilon) |
| dyadic (Y) | no multiplicity | already fixed by (h=Sv-Uw) |
| (Q,m_0,q,J) | no physical multiplicity | absent before Fourier splitting |
| full physical close block | (O(L^2\log(2L)X^\eta)) | (O(L^2X^\varepsilon)) |

This is capacity used as an upper bound on the explicitly selected
sector.  It is not a lower bound for the literal packet or its
complement.

### 3.4 Residual selector, literal fields, BV, collars, and zero extension

For one squarefree endpoint write (d=gd_0).  Under (193.H15), every
prime in (g) remains on the character leg and every prime outside
(g) is complemented.  The Round-184 residual truth table is the
equality indicator on the two selected-prime bits:

\[
 (00,10,01,11)\longmapsto(1,0,0,1).
\tag{193.H36}
\]

Complementing both selected bits preserves (193.H36); retaining both
selected bits in (g) also preserves it.  If exactly one selected prime
lies in (g), (193.H36) is complemented and the residual mask changes.
This is the exact and only selected-pair mismatch.

It causes no power loss here.  First, (g\le G_0) on active support.
If a selected prime (p\mid g), then (p\le G_0), while the other
selected prime is distinct and must obey the fixed Round-184 separation

\[
 |\log(q/p)|\ll L^{-1/2}.
\tag{193.H37}
\]

For all sufficiently large (L), (193.H37) is smaller than the minimum
positive logarithmic separation between a prime (p\le G_0) and a
distinct integer, so the exactly-one-in-(g) case is absent.  On the
remaining bounded shells it is paid by the absolute count (193.H4).
The argument is applied independently at (N) and (N+r).  No density
of selected pairs is used.

Even without this absence statement, orbit reindexing and zero extension
give the exact physical identity

\[
 \begin{aligned}
 \mathscr F_Y^\sigma[P_{\rm sw}]
 ={1\over2}\sum_{x\in P_{\rm sw}}
 &\chi_4(d')\chi_4(d)\Phi_r(N)\\
 &\times\left\{
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)}
 -\lambda_{N+r,\sigma}(gm')\overline{\lambda_{N,\sigma}(gm)}
 \right\}.
 \end{aligned}
\tag{193.H38}
\]

Here (\Phi_r(N)) contains the unchanged Fejer and square-root phase
factors.  A selector mismatch changes the bracket; it does not invalidate
the identity.

For completeness, the originally proposed coefficient-difference ledger
also closes.  Each endpoint allocation moves by (O(D_L)) in the
character coordinate and (O(D_L/g)) in the complementary coordinate.
On a common literal smooth cell, the accepted normalized hard symbol has
difference (O(D_L/L)X^\eta).  Multiplying the strategy's coarse
incidence envelope

\[
 O(LD_L^2\log(2L)+LD_L^3)
\tag{193.H39}
\]

by (D_L/L) gives (193.H6).

For the normalized dyadic-BV field, telescope over crossed unit
increments.  A fixed increment confines the corresponding
(\kappa U) or (\kappa v) coordinate to an (O(D_L)) collar.
At fixed (\kappa), the two close coordinates and the two opposing
displacements give at most

\[
 O\!\left(D_L^2(1+D_L/\kappa)^2\right)
\tag{193.H40}
\]

occurrences of that increment.  Summing (\kappa\ll L) and using the
scale-normalized total variation proves (193.H7).  The same count applies
to each fixed vertical, horizontal, or ratio face.  The inherited hard
symbol has only a fixed finite family of shell/profile faces, strict-cone
faces, floor/star/tie/half-weight sites, hard samples, real-(X)
crossings, and endpoint traces.  Thus every different-cell, boundary,
and endpoint-zero term is (O(L^2X^\varepsilon)).  The two-term product
rule handles the ordered upper coefficient and conjugated lower
coefficient without exchanging them.

This BV/collar proof is an independent audit of the proposed pairing;
(193.H5) is stronger and already pays every such event.  In particular,
an allocation that is live on only one orbit leg is a birth or death
through the original zero extension and is counted in (193.H4), never
silently deleted.

### 3.5 Complete Fourier recombination and deletion stability of every inherited safe source

Let (x) be a physical affine atom and let (b_x) be its canonical
anchor residue.  Since (P_{\rm cl}(x)) is independent of the Fourier
mode,

\[
 P_{\rm cl}(x)E_U(b_x)B_x
 =P_{\rm cl}(x)
  \sum_{k\bmod U}c_U(k)e(kb_x/U)B_x.
\tag{193.H41}
\]

Thus the complete mode sum may be recombined exactly before (193.H24)
or (193.H38) is used.  Using character reversal on a retained mode alone
would be invalid; the accepted carry-dependent mode factor does not equal
the full physical character.

Coordinatewise replacement (B_x\mapsto P_{\rm cl}(x)B_x) preserves
every accepted safe estimate through Round 192:

1. The bounded-height physical sector is an absolute opened-incidence
   count.
2. The (U=1), low-exact-conductor, and ordinary-edge packets use
   positive atom counts and Fourier (\ell^1) mass.
3. The imprimitive (Qm_0\ge Y) packet uses the positive atom count and
   the exact (m_0^{-1}) lift weight.
4. The projectively slow packet uses residue-class sparsity, heights,
   sites, coefficient mass, and the (m_0^{-1}) cancellation, all after
   a modulus.
5. The signed-inverse-small packet is a row-cardinality estimate.  The
   outer carrier terminal has at most two live-side heights, and the
   isolated Fejer difference uses the scalar step
   (2\kappa g/R_0).  Deleting physical sites can only reduce each of
   these positive bounds.
6. The Round-192 Farey union is a row selector followed by divisor
   multiplicity and positive row counting.  It commutes with the physical
   deletion because it depends only on the canonical row (v\bmod U).

The Round-184 XOR exchange sector is not one of these source terms: the
Round-185--192 carrier is already its exact residual complement.

At the Round-191 height-difference interface, the deletion must be made
before differencing.  In transported site notation the exact new common
term is

\[
 P_h(t)B_h(t)
 -\chi P_{h-1}(t+\nu)B_{h-1}(t+\nu).
\tag{193.H42}
\]

The difference of the two (P)'s is a new literal-field jump and stays
in the remainder.  The terminal and isolated Fejer projections are
defined from (193.H42) with the original carrier geometry and retain
their old positive bounds.  This proves deletion stability without the
false commutation in (193.H10).

Writing the accepted safe operators as (\Pi_j), define

\[
 \mathscr S_{\le192}[P]=\sum_j\Pi_j(PB),qquad
 \mathscr R_{\rm core}[P]=\mathscr F(PB)-\sum_j\Pi_j(PB).
\tag{193.H43}
\]

Every estimate above gives

\[
 |\mathscr S_{\le192}[P_{\rm cl}]|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{193.H44}
\]

Equations (193.H5), (193.H43), and (193.H44) prove (193.H8).  No safe
term is lost or counted twice, and no Fourier/core projector is treated
as a physical incidence predicate.

### 3.6 Method boundary and exact remaining scope

The proof of (193.H8) is a sparse-sector upper bound.  It says nothing
about the two complementary sets (193.H19).  In particular it does not
turn the (YL^2X^\varepsilon) positive capacity of the full high-height
source, or the fixed-packet (Y/(Qm_0)) deficit, into literal lower mass.
Arbitrary bounded coefficient arrays remain only operator-class
controls on the complement.  No coefficient-uniform far-sector theorem,
separate-orientation norm, positive Fourier completion, or unscaled
complementary-factor exchange follows.

The exact subsidiary pairing (193.H38) is useful evidence that the
character symmetry is real, but it is unused in the stronger theorem.
The target proof does not extrapolate the two-sided close count to any
atom failing (193.H16).

## 4. First doubtful or unproved step

There is no doubtful step in the parity deduction, integrality,
preservation of (g) and cofactor gcd one, fixed-point freedom,
orientation bijection, primitive-coordinate image, character reversal,
product/shift/Fejer/phase preservation, active (g)-bound, determinant
count, residual truth table, common-cell estimate, BV/collar ledger,
complete Fourier recombination, or coordinatewise deletion stability.

The first invalid equality in the uncorrected mechanism is precisely

\[
 P\Delta^-W\stackrel{\rm false}=\Delta^-(PW),
\tag{193.H45}
\]

or its transported version obtained by omitting

\[
 \chi\{P_h(t)-P_{h-1}(t+\nu)\}
 B_{h-1}(t+\nu).
\tag{193.H46}
\]

This is a literal algebraic failure if the mask is imposed after the
Round-191 coboundary has been formed.  The repair is exact: impose the
mask on the physical source, form (\Delta^-(PW)), and retain (193.H46)
in the new core.  With that convention the safe projections remain
absolute and (193.H8) follows.

After (193.H8), the first open relation is not another seam inside the
close sector.  It is the estimate for

\[
 \mathscr R_{\rm core}[1-P_{\rm cl}],
\tag{193.H47}
\]

with the ordered complement (193.H19), the complete Round-192 (T=0)
or strict-covector scope, both orientations, and every literal field.
Its available positive or arbitrary-bounded-array control still has the
inherited (Y/(Qm_0)) deficit.  That is operator-class insufficiency,
not a demonstrated literal failure and not physical lower mass.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| `exact_round192_core_and_T_zero_scope` | **PASS.** The masked source is fed through the exact core operator.  At (T=0), the Farey projection is zero and the whole inherited rho-large remainder is retained before masking. |
| `opened_endpoint_tuple_order` | **PASS.** (193.H15) and (193.H31) keep character divisor then cofactor at each ordered endpoint. |
| `cofactor_gcd_one_forces_odd_cofactors` | **PASS.** Even (r) makes (m,m') equi-parity; gcd one forces both odd. |
| `scaled_map_integrality_and_involution` | **PASS.** (193.H20)--(193.H22); (r\equiv2\pmod4) excludes fixed points. |
| `g_and_cofactor_gcd_preservation` | **PASS.** Exact identities are (193.H21). |
| `opposing_orientation_bijection_and_multiplicity` | **PASS.** Signs are interchanged and each orbit has exactly two atoms; plus representatives give multiplicity one. |
| `primitive_coordinate_image_and_coprimality` | **PASS.** (193.H25)--(193.H30) prove the canonical image, inward (\kappa), new primitive gcd, and ((U',h)=1). |
| `product_shift_phase_and_Fejer_preservation` | **PASS.** Products, (r=2\kappa gh), (h), Fejer weight, and square-root phase are unchanged. |
| `r_two_mod_four_character_reversal` | **PASS.** Derived before a modulus in (193.H23)--(193.H24). |
| `endpoint_order_and_lower_conjugation` | **PASS.** The transformed ordered product is (193.H31). |
| `tau_invariant_close_mask` | **PASS.** The two close differences change sign under (193.H27). |
| `active_support_bounds_g` | **PASS.** The original nonzero lower allocation has (4<d/m<16) and (m\asymp L); its lower close inequality gives (g\le G_0), uniformly after bounded-shell absorption. |
| `residual_selector_truth_table_under_g_complement` | **PASS with exact exception.** Complementing both outside-(g) selected bits preserves (1,0,0,1); exactly one selected prime in (g) flips it. |
| `selected_pair_intersects_g_exception` | **PASS.** It is absent for large (L) by fixed-(g) logarithmic separation and paid absolutely by (193.H4) on bounded shells. |
| `squarefree_divisor_coprimality_and_parity` | **PASS.** Product invariance and squarefreeness make every image allocation a legal odd coprime divisor allocation. |
| `literal_common_cell_difference` | **PASS.** The optional paired proof costs (193.H6); the stronger absolute count (193.H5) bypasses it. |
| `dyadic_BV_lift_multiplicity` | **PASS.** Fixed-increment multiplicity and its full sum are (193.H40) and (193.H7). |
| `all_boundary_collar_floor_star_endpoint_fields` | **PASS.** Every finite literal face/trace has the same (193.H7) bound; endpoint order is preserved and product rule is applied only afterward. |
| `zero_extension_births_and_deaths` | **PASS.** The primary proof counts every nonzero physical close atom directly.  On the subsidiary involution sector missing orbit legs are zeros in (193.H38); source-mask jumps are the explicit commutator (193.H46), retained in the core. |
| `complete_close_sector_power_no_hidden_Y` | **PASS.** (193.H4) uses the determinant to make (S) (O(1)); (Y) is a deletion, not a multiplier. |
| `complete_anchor_Fourier_recombination_before_pairing` | **PASS.** (193.H41) recombines all modes because the physical mask is mode-independent.  Pairing is used only on subsidiary (P_{\rm sw}); the wider theorem is absolute. |
| `inherited_safe_projection_deletion_stability` | **PASS under the coordinatewise convention.** Every safe proof is positive/absolute after (B\mapsto PB); post-Abel termwise masking is rejected by (193.H45). |
| `exact_masked_core_identity_no_double_count` | **PASS after notation repair.** The exact identity is the operatorial (193.H43), not post-Abel multiplication; linear additivity is (193.H18). |
| `exact_first_failure_complement` | **PASS.** The disjoint ordered complement is (193.H19). |
| `no_arbitrary_bounded_coefficient_closure` | **PASS.** Bounded coefficients are used only with the sparse count (193.H4), never to estimate (193.H47). |
| `diagnostic_only_computation` | **PASS.** No computation was used. |
| `original_t1_only_downstream_scope` | **PASS.** Even the strict result concerns only a sector of the exact original-(t=1) residual. |
| `exponent_quarantine` | **PASS.** No parent, endpoint, bridge, theorem, internal, external, or target exponent changes. |

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted context were used:

1. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/briefs/core_projection_mask_power_hostile_audit.md`;
2. `protocol.md`;
3. `state/proof_obligations.yml`;
4. `state/active_campaign.yml`;
5. `state/failure_ledger.md`;
6. `strategy/round193_m1_t1_core_gcd_scaled_orientation_involution_strategy.md`;
7. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`;
8. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`;
9. `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md`;
10. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`;
11. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`;
12. `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reports/tangent_gcd_transfer_capacity_audit.md`;
13. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reports/joint_hv_phase_jump_hostile_audit.md`; and
14. `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reports/central_core_phase_hostile_audit.md`.

No sibling Round-193 report, unlisted theorem, web source, or numerical
diagnostic was read or used.

## 7. Recommended state effect

**Promote only after the mandatory independent seams a subordinate strict
sector, with the operator notation repaired; retain every parent and
exponent status.**

Concretely:

1. Promote the two-sided close mask (P_{\rm cl}) of (193.H16) on all
   opposing even-shift atoms, with neither (k=1) nor
   (r\equiv2\pmod4).  Retain the exact finite involution, character
   reversal, canonical primitive map, residual-mask exception analysis,
   and physical pairing (193.H38) only as subsidiary algebra on
   (P_{\rm sw}).
2. Prefer the determinant-count proof (193.H3)--(193.H5) as the primary
   power argument.  It pays the whole two-sided physical close sector
   absolutely
   and removes any dependence on a delicate common-cell or collar saving.
3. Retain (193.H6)--(193.H7) as independent seam evidence that the
   proposed common-cell/BV/collar route also has the correct (L)-power.
4. Define the masked core only coordinatewise as in (193.H17) and
   (193.H43).  Reject the post-Abel shorthand (P\Delta W=\Delta(PW))
   and keep every mask birth/death commutator in the remainder.
5. Add only the strict sector (193.H8) under the terminal label
   `strict_rho_large_gcd_scaled_orientation_sector`.  Leave the ordered
   complement (193.H19)/(193.H47) open.
6. Make no claim about original (t\ge2), the near-resonant complement,
   the complete small-(t) owner, hard or smooth M1, GAR, any M2 parent,
   endpoint uniformity, M9, either bridge, the Gauss-circle target, or any
   exponent.
