# Formal candidate: hard-M1 \(t=1\) \(P_2\) absolute-capacity sectors

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Starting graph SHA-256: 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89
- Candidate status: conductor formalization; not accepted before independent seam review and State Patch
- Numerical theorem evidence: none

## 1. Statement

Fix real \(X\ge2\), one nonempty literal middle or lower residual hard-M1
shell \(L\ge2\), a sign \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 R_0=\lceil L\rceil,\qquad D_L=\lceil\sqrt L\rceil.
\tag{195.C1}
\]

Retain the exact accepted Round-192 hard-M1 original-\(t=1\),
\(\rho\)-large core.  Its physical opposing-incidence source has

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\ {\rm odd},\qquad
 0<r<R_0,\quad2\mid r,
\tag{195.C2}
\]

with \(d,m,d',m'\asymp L\).  Every residual selector, squarefree and
allocation-coprimality condition, profile, floor, star, half weight, hard
sample, cell, crossing, endpoint trace, Fejer factor, square-root phase,
orientation, affine site, conjugation, and zero extension remains literal.
Each physical atom has size \(O_\varepsilon(X^\varepsilon)\) after the
accepted divisor ledger.

For the spectral packet use \(\mathfrak m\) for the lift gcd, distinct from
the physical cofactor \(m\):

\[
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad U\mid u.
\tag{195.C3}
\]

The exact Round-192 convention is unchanged: at \(T=0\), the Farey
projector is zero and the whole inherited Round-191 \(\rho\)-large
remainder is present; at \(T\ge1\), every core row retains all simultaneous
strict Farey-covector inequalities and the accepted lower bound on
\(|\rho|\).  Both orientations and frequency signs remain inside one outer
real part.

Put \(g=(d,d')\) and impose, on the physical source before Fourier expansion
or height differencing,

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},
\tag{195.C4}
\]

\[
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}}.
\tag{195.C5}
\]

Here \(\kappa\) is the canonical inward cross gcd in the physical primitive
chart.  Then (195.C5) is an exact disjoint split.  For a fixed packet

\[
 p=(\kappa,u,\mathfrak m,q,a,J,Y,\sigma),
\]

define the small-\(\kappa\) packet sectors

\[
 \mathcal P_{\rm cap}
 =\{p:\kappa<D_L,\ \min(Y,D_L)\le H_B\mathfrak m\kappa\},
\qquad
 \mathcal P_{\rm rem}
 =\{p:\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}.
\tag{195.C5a}
\]

The large-\(\kappa\) sector and the exact packet-level
\(\mathcal P_{\rm cap}\) sector are target-safe:

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D}W)|
 \ll_{B,C_0,\varepsilon}
 H_B\mathfrak m\kappa uX^\varepsilon,}
\tag{195.C6}
\]

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll_{B,C_0,\varepsilon}
 H_B\mathfrak m\kappa uX^\varepsilon
 \qquad(p\in\mathcal P_{\rm cap}).}
\tag{195.C6a}
\]

\[
 \boxed{
 |\mathscr R_{{\rm core},Y,H_B}^\sigma(P_{2,\ge D}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.}
\tag{195.C7}
\]

After the accepted fixed-to-outer ledger, the complete subaggregate of
\(P_2\) packets satisfying either \(\kappa\ge D_L\) or
\(p\in\mathcal P_{\rm cap}\) is also
\(O_{B,C_0,\varepsilon}(L^2X^\varepsilon)\).  Its exact open packet
complement is \(P_{2,<D}\) on \(\mathcal P_{\rm rem}\).

No cancellation, coefficient replacement, extra Farey mask, or separate
orientation norm is used.

## 2. Both primitive charts and multiplicity

In the plus chart,

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad h=Sv-Uw>0,
\tag{195.C8}
\]

and define the close and positive far defects

\[
 \delta_+=\kappa(U-v)-2w,\qquad
 \eta_+=\kappa(U-v)+2S.
\tag{195.C9}
\]

Then

\[
 g\delta_+=d-gm,\quad g\eta_+=d'-gm',\quad
 2h=v\eta_++U\delta_+-\kappa(U^2-v^2).
\tag{195.C10}
\]

In the minus chart,

\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad h=Uw-vS>0,
\tag{195.C11}
\]

and

\[
 \delta_-=\kappa(U-v)+2S,\qquad
 \eta_-=\kappa(v-U)+2w.
\tag{195.C12}
\]

Upper failure forces \(g\eta_->D_L\), and

\[
 g\delta_-=d-gm,\quad -g\eta_-=d'-gm',\quad
 2h=U\eta_--v\delta_-+\kappa(U^2-v^2).
\tag{195.C13}
\]

In either chart, lower closeness and the shell bounds give \(g=O(1)\).
For fixed \((\kappa,g,U,v,\delta_\omega,\eta_\omega)\), the formulas above
recover \(S,w\) uniquely, subject only to parity and positivity; every
literal predicate deletes candidates.

## 3. Absolute large-\(\kappa\) count

Fix \((\kappa,g,U,v)\).  In the plus chart, lower closeness confines \(w\)
to \(O(D_L)\) integers.  For each \(w\),

\[
 0<Sv-Uw<R_0/(2\kappa g)
\tag{195.C14}
\]

confines \(S\) to an interval of length
\(R_0/(2\kappa gv)=O(1)\), since \(\kappa v\asymp L\).  In the minus chart,
lower closeness gives \(O(D_L)\) choices of \(S\), and \(h=Uw-vS\) confines
\(w\) to an interval of length \(R_0/(2\kappa gU)=O(1)\).

For fixed \(\kappa\), each of \(U,v\) has \(O(1+L/\kappa)\) possibilities.
Therefore

\[
 \begin{aligned}
 \#\mathcal I_{P_{2,\ge D}}
 &\ll\sum_{D_L\le\kappa\ll L}
 D_L(1+L/\kappa)^2\\
 &\ll D_LL+LD_L\log(2L)
      +D_LL^2\sum_{\kappa\ge D_L}\kappa^{-2}\\
 &\ll L^2+LD_L\log(2L)\ll L^2.
 \end{aligned}
\tag{195.C15}
\]

The bound covers both orientations and the whole Fejer range.  The
physical source is counted before Fourier or Abel expansion, so no
\(q/J\) denominator occurs here.  Literal endpoint weights cost only the
accepted \(X^\varepsilon\) allowance.  Thus the complete physically masked
source is \(O(L^2X^\varepsilon)\).

At a fixed spectral packet and one literal projective row, the same
argument gives \(O(D_L)\) physical atoms over the whole height block.
There are \(O(uJ/q)\) rows, and the complete anchor/Abel return costs at
most the accepted factor \(q/J\).  Hence the new physical contribution is

\[
 O(D_LuX^\varepsilon).
\tag{195.C16}
\]

The accepted terminal and Fejer projections cost
\(O(\kappa uX^\varepsilon)\); the inverse-small sector is disjoint from a
core row and the Farey projector only deletes rows.  Since
\(\kappa\ge D_L\), (195.C16) gives

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D}W)|
 \ll\kappa uX^\varepsilon
 \le H_B\mathfrak m\kappa uX^\varepsilon,
\tag{195.C17}
\]

which proves (195.C6).

## 4. Exact masked-operator passage

The notation in (195.C6)--(195.C7) means evaluation of the accepted linear
operator on \(P_{2,\ge D}W\), not multiplication of an already expanded
operator by a scalar mask.  At a transported common affine site the exact
identity is, with \(P_-^{\rm tr}\) denoting the previous mask evaluated at
the transported site,

\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{195.C18}
\]

The second term is the physical-mask commutator.  Affine births, deaths,
endpoint zero extensions, unequal endpoint translations, carries, phase
changes, cells, and crossings remain in the newly recomputed core.

Every accepted Round-187--192 safe proof is stable under this
coordinatewise physical deletion: it uses exact linear return followed by
positive row/atom counts, Fourier \(\ell^1\) mass, residue sparsity, or a
row indicator.  Reapplying those projectors gives a safe aggregate
\(O(L^2X^\varepsilon)\).  Subtracting it from the masked source bound after
(195.C15) proves (195.C7), including the \(T=0\) branch, all simultaneous
\(T\ge1\) inequalities, and the one outer real part.

## 5. Exact complement and mechanism boundary

The exact remaining mask is \(P_{2,<D}\).  At fixed height, primitivity
makes the plus close variable one residue class modulo \(v\), and the minus
close variable one residue class modulo \(U\).  Since
\(U,v\asymp L/\kappa\), the close window contains

\[
 O(1+\kappa D_L/L)=O(1)\qquad(\kappa<D_L)
\tag{195.C19}
\]

sites.  This fixed-height argument gives \(YuX^\varepsilon\).  Independently,
the all-height determinant count gives \(D_LuX^\varepsilon\).  Combining
the two bounds with the accepted terminal/Fejer cost gives the complete
positive estimate

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.}
\tag{195.C20}
\]

The \(\kappa u\) term is automatically target-safe.  Equation (195.C20)
proves (195.C6a), and the accepted lift, anchor, band, divisor, and shell
ledger then gives the asserted outer \(L^2X^\varepsilon\) bound for the
safe packet union.  Explicitly,

\[
 H_BX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon,
\tag{195.C20b}
\]

where the spectral \(\mathfrak m^{-1}\) lift weight cancels the
\(\mathfrak m\) in the fixed target.  Restricting this positive ledger to
the safe packets only deletes terms.  On the exact remaining region
\(\mathcal P_{\rm rem}\), the unresolved positive-capacity multiplier is

\[
 \frac{\min(Y,D_L)}{H_B\mathfrak m\kappa}.
\tag{195.C20a}
\]

Writing \(\eta\) for the positive far defect, the height equations are

\[
 2h=v\eta+U\delta-\kappa(U^2-v^2)\quad(+),\qquad
 2h=U\eta-v\delta+\kappa(U^2-v^2)\quad(-).
\tag{195.C21}
\]

The parity step \(\eta\mapsto\eta+2\) changes \(h\) by \(v\) or \(U\).
Because the live height block has length \(Y\ll L/\kappa\) and
\(U,v\asymp L/\kappa\), a fixed primitive row has only \(O(1)\) far
samples.  At a fixed retained plus mode the exact character-anchor ratio is

\[
 (-1)^{c_+(h;v)}e(a/q),\qquad c_+(h;v)\in\{0,1\},
\tag{195.C21a}
\]

where \(c_+\) is the canonical-anchor wrap.  The pre-Fourier physical
parity flip is \(-1\), but is recovered only after all anchor modes
recombine.  In the minus chart the retained-mode ratio is exactly one
because \(U=\mathfrak m q\).  Neither identity provides a long within-row
averaging variable.

On nonzero literal support, the fixed divisor \(\kappa gU\) is squarefree;
hence \(U\) is squarefree and \((\kappa,U)=1\).  For fixed
\((\kappa,U,h,\delta)\), the minus congruence

\[
 \kappa v^2+\delta v+2h\equiv0\pmod U
\tag{195.C22}
\]

has at most \(2^{\omega(U)}\ll_\varepsilon U^\varepsilon\) roots modulo
\(U\), and the plus fibre has the analogous divisor-bound multiplicity.
This removes a squareful algebraic false shadow, but it does not control
the \(q/J\) anchor denominator or actual cross-row coefficient
correlations and therefore supplies no missing power by itself.

At each common site, exact event recombination is mandatory.  Current
phase channels form an all-ones \(2\times2\) Gram block and previous phase
channels an all-ones \(3\times3\) block; recombination returns the original
masked non-Fejer jump.  Orthogonalizing literal source labels instead makes
the final summation functional restore the same capacity.  The full
cross-row Gram has \(++,+-,-+,--\) blocks and must retain the actual endpoint
products, square-root phases, Fejer factors, residual masks, carries,
births/deaths, mask commutator, and cross-event interference.  With the
available interfaces only the Cauchy positive-capacity bound is proved.

This is a no-go for coefficient-blind or within-row determinant/anchor
dispersion, not a lower bound for the literal operator.  The first open
step is a coefficient-sensitive joint cross-row four-block Gram estimate
on \(P_{2,<D}\cap\mathcal P_{\rm rem}\) recovering (195.C20a).

## 6. Scope and dependencies

This candidate proves only the strict sector \(P_{2,\ge D_L}\), the
absolute-capacity packet sector \(\mathcal P_{\rm cap}\), their exact open
packet complement, and the stated method boundary.  It does not prove complete
\(P_2\), \(P_1\), complete original \(t=1\), any original \(t\ge2\) range,
the remaining hard-M1 owner, either M1 parent, GAR, any M2 parent, endpoint
uniformity, M9, either final bridge, or the Gauss-circle target.  The
internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) exponent records are
unchanged.

The direct graph prerequisite is
M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector, which supplies the
exact physical \(P_{\rm cl},P_1,P_2\) partition and accepted core operator.
Its dependency M9-M1-hard-top-t1-rho-large-farey-covector-reduction
supplies the exact Farey-core convention.  The physical primitive chart is
inherited from
M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction.

The claimant evidence is exactly the three frozen Round-195 reports and
the conductor reconciliation.  The blind report supports only the fibre
algebra and method boundary after the post-unmask repairs in the
reconciliation; it is not evidence for the positive estimate or literal
lower mass.

## 7. Proposed state effect

After independent count/power/operator, literal Gram/no-go, blind
post-unmask, candidate-kernel consistency, provenance/scope, and graph
replay reviews:

1. create one subordinate proved_internal node for (195.C4)--(195.C22),
   including (195.C6a) and the exact \(\mathcal P_{\rm rem}\) complement;
2. add it only as strict-sector evidence to the already-open hard-M1
   small-\(t\) residual owner;
3. record \(P_{2,<D_L}\cap\mathcal P_{\rm rem}\), (195.C20a), and the
   within-row self-return as the exact remaining seam; and
4. leave every parent, bridge, theorem, and exponent unchanged.

The proposed terminal label is strict_p2_absolute_capacity_sectors.
