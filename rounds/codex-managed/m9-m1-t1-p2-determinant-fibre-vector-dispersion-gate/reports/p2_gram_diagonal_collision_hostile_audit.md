# Round 195 hostile \(P_2\) Gram-diagonal and collision audit

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Task: `p2_gram_diagonal_collision_hostile_audit`
- Role: barrier/no-go with strongest repair
- Starting graph SHA-256:
  `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`
- Status: candidate evidence only; no shared-state edit

## 1. Result

**Verdict: REPAIR for a strict sector; scoped NO-GO for the proposed
coefficient-blind closure; the complete \(P_2\) estimate is not proved.**

There is a stronger elementary repair before any \(TT^*\) argument.  Let
\(\kappa_\omega(x)\) be the inward cross gcd in the canonical primitive
chart of the oriented physical atom \(x\), and put

\[
 P_{2,\geq D}(x)=P_2(x)\mathbf 1_{\kappa_\omega(x)\geq D_L},
 \qquad
 P_{2,<D}(x)=P_2(x)\mathbf 1_{1\leq\kappa_\omega(x)<D_L}.
\tag{195.H1}
\]

Then \(P_2=P_{2,\geq D}+P_{2,<D}\) is an exact disjoint physical split and

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\geq D}W)|
 \ll_{B,C_0,\varepsilon}
 Q\mathfrak m\kappa uX^\varepsilon,}
\tag{195.H2}
\]

\[
 \boxed{
 |\mathscr R_{{\rm core},Y,Q}^\sigma(P_{2,\geq D}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.}
\tag{195.H3}
\]

Indeed, lower closeness forces \(g=O(1)\).  In either primitive chart,
for fixed \((\kappa,g,U,v)\) the close variable has \(O(D_L)\) choices,
and the determinant and \(r<R_0\) leave \(O(1)\) choices of the other
variable.  Consequently the complete physical large-\(\kappa\) envelope is

\[
 \sum_{\kappa\geq D_L}
 O\!\left(D_L(1+L/\kappa)^2\right)
 \ll L^2+LD_L\log(2L)\ll L^2.
\tag{195.H4}
\]

Multiplicity one and arbitrary literal deletion make this an absolute
upper bound, not a signed argument.  The through-Round-192 safe estimates
remain valid after this coordinatewise physical deletion; all new mask
jumps remain in the recomputed core.

The exact complement \(P_{2,<D}\) remains open.  Its determinant-fibre
coordinates and dyadic far partition are exact, but they do not by
themselves produce a vector-dispersion estimate.  The first obstruction is
already present at one transported common site: endpoint, phase, carry,
and physical-mask source channels have identical effective phases.  Their
Gram blocks are all-ones blocks, not orthogonal blocks.  Exact
recombination returns the original masked non-Fejer jump.  If one instead
orthogonalizes literal labels, the norm of the final summation functional
restores the same positive support capacity.  Off-diagonal determinant
fibres have spectral aliases and no proved separation for the combined
inverse-residue and square-root phase.

This is a rigorous no-go only for arguments using determinant
multiplicity, phase display, support, and coefficient magnitudes without a
new signed theorem for the actual endpoint vectors.  It is **not** a lower
bound for the literal \(P_{2,<D}\) packet.  Literal coefficients may vanish
or cancel, and no assertion below converts capacity into physical mass.

## 2. Exact statement and hypotheses

### 2.1 Physical source, spectral packet, and exact core

Fix the complete Round-193 physical opposing-incidence source

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\ {\rm odd},\qquad
 0<r<R_0=\lceil L\rceil,\quad 2\mid r,
\]

with \(d,m,d',m'\asymp L\), and impose

\[
 P_2=\mathbf1_{|d-gm|\leq D_L}
     \mathbf1_{|d'-gm'|>D_L},
 \qquad g=(d,d'),\qquad D_L=\lceil\sqrt L\rceil
\tag{195.H5}
\]

on each physical atom before anchor Fourier expansion and height
differencing.  The spectral lift gcd is denoted \(\mathfrak m\), never the
physical cofactor \(m\):

\[
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad Q=H_B,
\tag{195.H6}
\]

\[
 T=\min\left\{\frac{U-1}{2},
       \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
 \qquad A=\min\{U-1,\lfloor Q^{C_0}\rfloor\}.
\tag{195.H7}
\]

For a fixed packet \(p=(\kappa,u,\mathfrak m,q,a,J,\sigma)\), write

\[
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q),
 \qquad \epsilon_+=1,\quad\epsilon_-=-1,
\]

and, for any physical mask \(P\),

\[
 W^P_{\omega,v}(h)=K_{\omega,v}(h)G(h)
 \sum_{t\in I_\omega(h)}(-1)^tP(x_{\omega,v,h,t})
 B_{\omega,v}(h,t),
\tag{195.H8}
\]

where \(G(h)=\mathbf1_{(U,h)=1}\), the original carrier and zero
extension are retained, and

\[
 B=F\Lambda\Psi,\qquad
 F(h)=1-\frac{2\kappa gh}{R_0},\qquad
 \Lambda=\lambda_{N+r,\sigma}(d')
          \overline{\lambda_{N,\sigma}(d)}.
\tag{195.H9}
\]

Every selector, endpoint mask, profile, floor, star, half weight, hard
sample, crossing, cell, affine site, conjugation, and square-root phase
remains in (195.H8)--(195.H9).  The exact fixed Abel packet is

\[
 \mathscr J_{\rm fix}(PW)=
 \sum_{\substack{\omega,v\ {\rm literal}\\J\leq j_q(a,v)<2J}}
 \frac1{1-z_{\omega,v}}
 \sum_{h\in\mathbb Z}\Delta^-W^P_{\omega,v}(h)z_{\omega,v}^{\,h}.
\tag{195.H10}
\]

With all inherited support restrictions understood, the Round-192 core is
exactly

\[
 \mathscr R_{{\rm core},{\rm fix}}(PW)
 =(I-P_A)\{\mathscr J_{\rm fix}(PW)
 -\mathscr J_{\rm inv,fix}(PW)
 -\mathscr J_{\rm terminal,fix}(PW)
 -\mathscr J_{\rm Fejer,fix}(PW)\}.
\tag{195.H11}
\]

At \(T=0\), \(P_A=0\) and the whole inherited rho-large remainder is
present.  At \(T\geq1\), every surviving row obeys simultaneously

\[
 |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),
 \qquad |\rho|\geq(A+1)(T+1).
\tag{195.H12}
\]

Both orientations and frequency signs remain in (195.H11), and the exact
outer assembly and its one real part are applied only after the complete
complex sum.

On a transported common site, with previous index \(t+\nu_\omega(h)\)
and \(\chi=(-1)^\nu\), physical masking gives the indispensable identity

\[
 P_hB_h-\chi P_-B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-)B_-^{\rm tr}.
\tag{195.H13}
\]

Thus (195.H11) means \(\mathscr R_{\rm core}(PW)\), not post-expansion
multiplication \(P\mathscr R_{\rm core}(W)\).

### 2.2 Both primitive charts, positive far defects, and multiplicity

In the plus chart put

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,
 \quad h=Sv-Uw>0,
\]

\[
 C_+=\kappa(U-v)-2w,\qquad
 F_+=\kappa(U-v)+2S.
\tag{195.H14}
\]

Then \(gC_+=d-gm\), \(gF_+=d'-gm'\), and

\[
 F_+-C_+=2(S+w),\qquad
 2h=vF_++UC_+-\kappa(U^2-v^2).
\tag{195.H15}
\]

Hence \(P_2\) is exactly \(|gC_+|\leq D_L\), \(gF_+>D_L\).

In the minus chart put

\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,
 \quad h=Uw-vS>0,
\]

\[
 C_-=\kappa(U-v)+2S=\frac{d-gm}{g},\qquad
 F_-=\kappa(v-U)+2w=-\frac{d'-gm'}{g}.
\tag{195.H16}
\]

Now \(C_-+F_-=2(S+w)\), and

\[
 2h=UF_--vC_-+\kappa(U^2-v^2).
\tag{195.H17}
\]

Since the signed upper defect is smaller than the close lower defect,
upper failure forces \(gF_->D_L\).  This sign reversal is essential; a
single unqualified \(\Delta_+\) formula does not cover both orientations.

In either chart, lower closeness and \(d,m\asymp L\) give

\[
 1\leq g\leq d/m+D_L/m=O(1)
\tag{195.H18}
\]

uniformly for every \(L\geq2\).  Define the unique half-open dyadic bin

\[
 E_j=2^jD_L,\qquad E_j<gF_\omega\leq2E_j.
\tag{195.H19}
\]

Here \(j\geq0\), \(E_j\ll L\), and there are \(O(\log(2L))\) bins.

For fixed \((\kappa,g,U,v,C_+,F_+)\), the plus variables are recovered by

\[
 w=\frac{\kappa(U-v)-C_+}{2},\qquad
 S=\frac{F_+-\kappa(U-v)}{2}.
\tag{195.H20}
\]

For fixed \((\kappa,g,U,v,C_-,F_-)\), the minus variables are recovered by

\[
 S=\frac{C_--\kappa(U-v)}{2},\qquad
 w=\frac{F_-+\kappa(U-v)}{2}.
\tag{195.H21}
\]

Thus the fibre multiplicity is at most one, with the exact parity
conditions \(C_\omega\equiv F_\omega\equiv\kappa(U-v)\pmod2\), positivity,
and all literal predicates merely deleting candidates.  Equivalently,
for fixed \((\kappa,g,U,v,C_\omega,h)\), (195.H15) or (195.H17) determines
at most one \(F_\omega\).

## 3. Proof and hostile derivation

### 3.1 The large-\(\kappa\) repair

For the plus chart, fix \((\kappa,g,U,v)\).  The close inequality in
(195.H14) confines \(w\) to an interval of length \(D_L/g\), hence gives

\[
 \#\{w\}\ll1+D_L/g\ll D_L.
\tag{195.H22}
\]

For each such \(w\), \(0<h<R_0/(2\kappa g)\) and \(h=Sv-Uw\) confine \(S\)
to

\[
 \frac{Uw}{v}<S<\frac{Uw}{v}+\frac{R_0}{2\kappa gv}.
\tag{195.H23}
\]

The literal shell has \(\kappa v\asymp L\), so (195.H23) has \(O(1)\)
integer points.  In the minus chart, close lower defect confines \(S\) to
\(O(D_L)\) choices, and \(h=Uw-vS\), together with
\(\kappa U\asymp L\) after (195.H18), confines \(w\) to an \(O(1)\)
interval.  Each chart is multiplicity one, the charts are disjoint
orientations, and all arithmetic, endpoint, dyadic-height, core, and
literal conditions only delete atoms.

There are \(O(1+L/\kappa)\) choices for each of \(U,v\).  Summing both
orientations and the fixed finite set of \(g\)'s proves

\[
 \#\mathcal I_{P_{2,\geq D}}
 \ll \sum_{\kappa\geq D_L}
 D_L(1+L/\kappa)^2
 \ll L^2+LD_L\log(2L).
\tag{195.H24}
\]

At \(D_L=\lceil\sqrt L\rceil\), the last expression is
\(O(L^2)\).  The pointwise literal endpoint weight is
\(O_\eta(X^\eta)\), so the complete masked physical source is absolutely
target-safe.

There is also a fixed-packet version.  The inherited relation is
\(u=gU\), and the projective band contains \(O(uJ/q)\) literal \(v\)-rows.
The preceding argument gives at most \(O(D_L)\) selected physical atoms
per row over the whole height block.  The original row has at most
\(O(Y\kappa)\) atoms, so the sharp positive envelope is

\[
 M_p(P_2)\ll \frac{uJ}{q}\min\{D_L,Y\kappa\}X^\eta.
\tag{195.H25}
\]

Endpoint-exact Abel inversion removes the apparent (q/J) denominator.
The accepted terminal and Fejer projections cost
\(O(\kappa uX^\eta)\), inverse-small is disjoint from a core row, and
\(I-P_A\) only deletes rows.  Hence

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll \left(\frac{D_LJ}{q}+\kappa\right)uX^\eta.
\tag{195.H26}
\]

When \(\kappa\geq D_L\), (195.H26) is
\(O(\kappa uX^\eta)\), which is stronger than (195.H2).

The physical deletion in (195.H1) preserves every accepted safe proof:
Round 187 uses positive counts and Fourier \(\ell^1\) mass; Round 188 uses
the exact lift and a positive count; Round 189 uses residue sparsity and a
positive count; Round 191 applies exact Abel inversion to the newly masked
zero-extended row and keeps the accepted outer terminal and Fejer bounds;
Round 192 applies one row indicator and positive row counting.  Formula
(195.H13), affine births/deaths, and endpoint zero extensions remain in the
new core.  Thus the safe aggregate is also \(O(L^2X^\varepsilon)\), and
linearity proves (195.H3).

### 3.2 Actual source vectors and the literal phase-collision block

Write transported previous quantities with a minus subscript.  Expanding
(195.H13) with the exact Round-191 product rule gives, at every common
site,

\[
\begin{aligned}
 P_hB_h-\chi P_-B_-={}&
 P_h(1-\chi)F_-\Lambda_-\Psi_-\\
 &+P_h(F_h-F_-)\Lambda_h\Psi_h\\
 &+P_hF_-(\Lambda_h-\Lambda_-)\Psi_h\\
 &+P_hF_-\Lambda_-(\Psi_h-\Psi_-)\\
 &+\chi(P_h-P_-)F_-\Lambda_-\Psi_-.
\end{aligned}
\tag{195.H27}
\]

The second line is the accepted Fejer projection.  In the core, the two
remaining current-phase channels have the identical effective phase
\(z_{\omega,v}^{h}\Psi_h\) and recombine as

\[
 P_hF_-(\Lambda_h-\Lambda_-)+P_hF_-\Lambda_-
 =P_hF_-\Lambda_h.
\tag{195.H28}
\]

The three previous-phase channels have the identical effective phase
\(z_{\omega,v}^{h}\Psi_-\) and recombine as

\[
 P_h(1-\chi)F_-\Lambda_- -P_hF_-\Lambda_-
 +\chi(P_h-P_-)F_-\Lambda_-
 =-\chi P_-F_-\Lambda_-.
\tag{195.H29}
\]

Thus their phase Gram blocks are respectively all-ones \(2\times2\) and
\(3\times3\) blocks (after zero channels are removed), and the exact
recombined core common-site term is

\[
 P_hF_-\Lambda_h\Psi_h-\chi P_-F_-\Lambda_-\Psi_-.
\tag{195.H30}
\]

Restoring the Fejer line changes \(F_-\) to \(F_h\) on the current atom
and returns the full masked jump.  Opening
\(\Lambda=\lambda_1\overline{\lambda_0}\), then opening endpoint masks and
the ordered first-changed field list, only enlarges the exact
current-phase all-ones block.  The upper and conjugated lower endpoint
differences are not orthogonal vectors.

The inherited height transport also moves the two endpoints unequally.
With \(A_0=\kappa gU\), \(C_v=\kappa v\), and the Round-192 covector
notation, the plus shifts are

\[
 (\Delta N_0,\Delta d_0)=(2A_0(d_v+v\ell),0),\qquad
 (\Delta N_1,\Delta d_1)=(2gC_v(c+U\ell),2g(c+U\ell)),
\tag{195.H31}
\]

and the minus shifts are the corresponding negative swapped pair.  Carries
are \(\nu\in\{-1,0,1\}\), so \(\chi=(-1)^\nu\) is not a constant signed
discrepancy.  Affine births, deaths, endpoint zero extensions, and
\(P_h-P_-\) terms can be unpaired.  Their positive number is bounded by
the same \(O(D_L)\) per-row envelope, but no accepted relation makes their
actual coefficient vectors cancel.

### 3.3 Exact Gram, diagonal, aliases, and off-diagonal fibres

After the mandatory within-site recombination, enumerate all remaining
literal core occurrences by \(x\), retaining orientation, frequency sign,
endpoint order, source type, zero extension, and far bin.  Write their
actual coefficients as \(b_x\) and their combined phase as

\[
 \Theta_x=
 \frac{\epsilon_{\omega_x}a\bar v_{x,q}h_x}{q}
 +\sigma\sqrt X\bigl(\sqrt{N_x+r_x}-\sqrt{N_x}\bigr).
\tag{195.H32}
\]

Before any positive norm, the exact scalar Gram identity is

\[
 \left|\sum_x b_xe(\Theta_x)\right|^2
 =\sum_{x,y}b_x\overline{b_y}
   e(\Theta_x-\Theta_y).
\tag{195.H33}
\]

Its diagonal is exactly \(\sum_x|b_x|^2\).  This is not known to be
comparable below to the support size; it may be zero.  Using only
\(|b_x|\ll X^\eta\), however, Cauchy--Schwarz combines the diagonal with
the norm of the final summation functional and gives precisely the
positive capacity \(M_p(P_2)X^\eta\), not a contraction.

If instead one keeps endpoint/carry/mask sources as orthogonal Hilbert
coordinates, (195.H33) is no longer the scalar square until one applies
the all-ones summation functional; its norm restores the discarded support
factor.  If equal physical coordinates are identified, (195.H28)--(195.H29)
restore the collision cross terms and return (195.H30).  These are the two
exact vectorizations; neither creates a free saving.

For distinct physical atoms, an exact combined phase collision is

\[
 \frac{a}{q}
 (\epsilon_\omega\bar v_qh-
  \epsilon_{\omega'}\bar v'_qh')
 +\sigma\sqrt X\{\sqrt{N+r}-\sqrt N
                 -\sqrt{N'+r'}+\sqrt{N'}\}\in\mathbb Z.
\tag{195.H34}
\]

The determinant relation supplies no lower bound for the distance in
(195.H34).  It even has exact spectral aliases.  In the plus chart, at
fixed \((\kappa,g,U,v,C_+)\), the legal algebraic step

\[
 F_+\mapsto F_++2q\ell,\quad S\mapsto S+q\ell,
 \quad h\mapsto h+qv\ell
\tag{195.H35}
\]

leaves \(z_{+,v}^{h}\) unchanged.  In the minus chart,

\[
 F_-\mapsto F_-+2q\ell,\quad w\mapsto w+q\ell,
 \quad h\mapsto h+qU\ell
\tag{195.H36}
\]

also leaves the spectral factor unchanged.  Shells and literal masks may
delete either member, and the radical phases need not agree, so
(195.H35)--(195.H36) are not literal lower mass.  They do prove that the
determinant identity alone gives no spectral phase separation.  The
guaranteed repeated **combined** phases are the within-site channel blocks
(195.H28)--(195.H29), whenever those actual channels are nonzero.

For off-diagonal plus fibres with the same close coordinate, the exact
difference law is

\[
 2(h-h')=vF-v'F'+C(U-U')
 -\kappa\{U^2-v^2-(U'^2-v'^2)\},
\tag{195.H37}
\]

with the orientation-appropriate analogue from (195.H17).  It controls
integer multiplicity, not the radical part of (195.H34), endpoint-vector
inner products, or their signs.  No accepted large-sieve spacing,
determinant transposition, or two-orientation commutator estimate bounds
the off-diagonal quadratic form at the required scale.

### 3.4 Restored powers and the small-\(\kappa\) boundary

The original whole-packet positive bound
\(Y\kappa uX^\varepsilon\) and its deficit
\(Y/(Q\mathfrak m)\) remain valid coarse controls.  The physical \(P_2\)
count sharpens this to (195.H25), so the exact worst-band deficit after
using the one-close geometry is

\[
 \boxed{
 \mathfrak D_{P_2}(p)
 \ll
 \min\left\{
 \frac{Y}{Q\mathfrak m},
 \frac{D_L}{Q\mathfrak m\kappa}
 \right\}.}
\tag{195.H38}
\]

This is a capacity ratio, not a lower bound.  It is at most one on the
proved sector \(\kappa\geq D_L\).  On \(1\leq\kappa<D_L\), the complete
physical positive envelope is

\[
 \sum_{\kappa<D_L}D_L(1+L/\kappa)^2
 \ll D_LL^2,
\tag{195.H39}
\]

which is \(O(L^{5/2})\) at \(D_L=\lceil\sqrt L\rceil\), one \(D_L\)-factor
above the \(L^2\) target.  A positive sum over the disjoint far bins costs
at most \(O(\log(2L))\), absorbable into a fresh \(X^\varepsilon\), but no
power.

For the proved fixed-packet bound (195.H2), the accepted outer ledger is
unchanged:

\[
 c_{\mathfrak m q}(\mathfrak ma)=\mathfrak m^{-1}c_q(a),
 \qquad \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),
 \qquad \sum_{\mathfrak m q\mid u}1\leq\tau_3(u).
\tag{195.H40}
\]

The \(\mathfrak m^{-1}\) cancels the \(\mathfrak m\) in (195.H2), dyadic
bands and divisor logs are polylogarithmic, and

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{195.H41}
\]

There is no hidden \(Y\), \(q\), \(U\), Fourier-lift, or far-bin power in
(195.H41).  Formula (195.H39), not epsilon absorption, is the unresolved
small-\(\kappa\) power.

## 4. First doubtful or unproved step

The first algebraically false step in a source-separated Gram proof is

\[
 \left\|V_{\rm endpoint}+V_{\rm phase}+V_{\rm carry}
             +V_{\rm mask}\right\|_2^2
 \stackrel{\rm false}{=}
 \sum_s\|V_s\|_2^2.
\tag{195.H42}
\]

Equations (195.H28)--(195.H29) give nonzero cross terms of exactly the
same phase whenever the corresponding channels survive.  Replacing
(195.H42) by the correct Gram recombines those channels to (195.H30), an
exact self-return.

After that repair, the first genuinely unproved inequality is the direct
small-\(\kappa\) packet estimate

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \stackrel{?}{\ll}_{B,C_0,\varepsilon}
 Q\mathfrak m\kappa uX^\varepsilon.}
\tag{195.H43}
\]

Neither multiplicity one, (195.H15)/(195.H17), the far partition, nor the
displayed phases controls the actual quadratic form in (195.H33) by the
square of (195.H43).  The off-diagonal endpoint-vector inner products and
the radical part of (195.H34) remain unproved.  An unsigned or adversarial
bounded coefficient may take \(b_x=e(-\Theta_x)\) after exact source
recombination and attain the positive support capacity.  That falsifies a
coefficient-uniform theorem but is not asserted to be the literal endpoint
coefficient and does not disprove (195.H43).

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_round193_P2_physical_mask` | **PASS.** Equation (195.H5) is the complete lower-close/upper-far mask. |
| `mask_before_Fourier_and_height_difference` | **PASS.** Equations (195.H8), (195.H10), and (195.H13) impose and difference the physical mask first. |
| `exact_round192_core_and_T_zero_scope` | **PASS.** Equation (195.H11) retains the exact subtraction; at \(T=0\), \(P_A=0\). |
| `strict_T_positive_Farey_covectors` | **PASS.** Every simultaneous inequality and the \(|\rho|\) lower bound are retained in (195.H12). |
| `spectral_lift_gcd_vs_physical_cofactor_notation` | **PASS.** \(\mathfrak m\) is spectral; \(m,m'\) are physical cofactors. |
| `both_orientation_primitive_charts` | **PASS.** Equations (195.H14)--(195.H17) audit both charts without a false symmetric sign. |
| `Delta_minus_Delta_plus_identity` | **PASS with orientation repair.** (195.H15) is the plus identity; (195.H17) is the exact minus identity. |
| `lower_close_uniform_g_bound` | **PASS.** Equation (195.H18) is uniform for all \(L\ge2\). |
| `upper_failure_positive_far_defect` | **PASS.** \(F_+>0\); in the minus chart the positive far defect is the negative of the signed upper defect. |
| `dyadic_far_defect_partition` | **PASS.** Equation (195.H19) is unique, half-open, exhaustive, and has \(E\ll L\). |
| `determinant_fibre_multiplicity` | **PASS.** Equations (195.H20)--(195.H21), parity, and positivity give multiplicity at most one. |
| `actual_endpoint_coefficient_vectors` | **PASS as retained data; no estimate.** Ordered products, conjugation, literal masks, numerical profiles, and zero extensions remain in \(b_x\). |
| `unequal_endpoint_translations_and_carries` | **PASS as a barrier.** Equation (195.H31) and \(\nu\in\{-1,0,1\}\) reject a common translation or constant carry sign. |
| `birth_death_zero_extension_vectors` | **PASS for exact coverage.** Affine and mask births/deaths and both outer and endpoint zero extensions remain; only the accepted outer terminal is already safe. |
| `physical_mask_commutator` | **PASS.** The last term of (195.H27) is indispensable and can have the unresolved \(O(D_L)\)-per-row capacity. |
| `one_outer_real_part` | **PASS.** No orientation or frequency-sign modulus is inserted; the large-\(\kappa\) proof is an absolute strict-sector estimate. |
| `TTstar_Gram_before_positive_norms` | **PASS as an exact audit.** Equations (195.H27)--(195.H33) form the literal Gram first. They do not prove (195.H43). |
| `Gram_diagonal_and_phase_collisions` | **NO-GO for the proposed automatic closure.** The diagonal has no literal lower comparison, while (195.H28)--(195.H29) are exact all-ones collision blocks. |
| `off_diagonal_determinant_fibres` | **UNPROVED.** Equations (195.H34)--(195.H37) expose aliases and the missing radical/endpoint-vector estimate. |
| `Y_over_HBmfrak_deficit` | **PASS with sharp \(P_2\) repair.** The coarse ratio is \(Y/(Q\mathfrak m)\); the exact one-close ratio is (195.H38). Neither is lower mass. |
| `fixed_packet_to_outer_power_ledger` | **PASS on \(P_{2,\ge D}\), FAIL to close \(P_{2,<D}\).** Equations (195.H40)--(195.H41) restore every factor; (195.H39) is the remaining \(D_L\) loss. |
| `unsigned_character_erased_adversarial_controls` | **PASS as falsifiers.** Phase conjugation attains support capacity, so none of these shadows can certify the literal theorem. |
| `no_arbitrary_bounded_coefficient_closure` | **PASS.** The no-go is explicitly theorem-class only; arbitrary arrays are never substituted for the claimant coefficients. |
| `no_separate_orientation_norm` | **PASS.** The small-\(\kappa\) theorem remains a joint complex sum. |
| `no_width_Farey_or_proper_submask_escape` | **PASS.** \(D=D_L\); no new Farey cover is used. The strict repair is accompanied by the exact complement \(P_{2,<D}\) and is not called complete \(P_2\). |
| `diagnostic_only_computation` | **PASS.** No numerical or symbolic computation was used. |
| `original_t1_only_downstream_scope` | **PASS.** Even full \(P_2\) would close only this one Round-193 complement. |
| `exponent_quarantine` | **PASS.** Internal \(1/3\), external \(0.3144831759740614\ldots\), and target \(1/4\) remain unchanged. |

The unsigned, character-erased, phase-conjugating, arbitrary bounded-array,
and separately normed-orientation controls all fail at the capacity level.
No conclusion about literal lower mass is drawn from any of them.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted selected context were used:

1. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/briefs/p2_gram_diagonal_collision_hostile_audit.md` —
   `3736b9afa53bfb44dbcf6a5757b32417d8519168357110683b352ca07187b166`.
2. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
3. `state/proof_obligations.yml` —
   `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.
4. `state/active_campaign.yml` —
   `7a6762a4030410bce88305638367821bc9280dc2f88f1b201e3403594e41e00d`.
5. `state/failure_ledger.md` —
   `281738ecf07a4909551fe5270017bfb25ef041a8731e123dc21cdfd738b9583c`.
6. `strategy/round195_m1_t1_p2_determinant_fibre_vector_dispersion_strategy.md` —
   repaired byte-clean SHA-256
   `4c98defd23667f724ddc00856d7add96fe58748890a82b905ecb2fbf3b180740`.
7. `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md` —
   `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`.
8. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md` —
   `301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325`.
9. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md` —
   `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`.
10. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md` —
    `31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58`.
11. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md` —
    `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`.
12. `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/blind_post_unmask_frontier_selection_review.md` —
    `065641931a9899855a2d7b4e6b09c191396b87fd760738e9de52b65e23ae5ede`.
13. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reports/core_projection_mask_power_hostile_audit.md` —
    `9e344e35f0c8a8ca9acce9416cf0b4f0c4d8ce7f3cfbbd4de95f854fdf7b81fb`.
14. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reports/joint_hv_phase_jump_hostile_audit.md` —
    `902ea86fd79cef97ab2a4e3ad0f92457b49d13c97212a03be70078ada656b22e`.

No web source and no computation were used.  No graph, proof draft,
strategy, synthesis, validation matrix, sibling artifact, or shared state
was edited.

## 7. Recommended state effect

**Revise.**  Subject to the ordinary independent seam and power reviews,
promote only the strict subordinate lemma (195.H1)--(195.H3) for the exact
large-inward-cross-gcd sector \(P_{2,\ge D}\).  Record
\(P_{2,<D}\) as its exact complement and retain it open.

Reject as closures of that complement:

1. source-type orthogonalization, by the exact collision blocks
   (195.H28)--(195.H29);
2. exact recombination or determinant completion, because it self-returns
   to (195.H30) and the positive capacity (195.H25);
3. multiplicity-only, phase-only, unsigned, character-erased,
   adversarial-array, separately normed-orientation, positive large-sieve,
   or coefficient-blind \(TT^*\) estimates; and
4. any inference that (195.H38) or (195.H39) is literal lower mass.

The first remaining theorem is exactly (195.H43): a jointly signed
small-\(\kappa\) estimate for the actual endpoint/carry/birth-death/mask
vectors and both orientations before positive norms.  No parent, complete
original \(t=1\) owner, original \(t\ge2\) range, large-\(G\) complement,
M1 parent, GAR owner, M2 parent, endpoint theorem, M9 node, bridge,
Gauss-circle target, or exponent should change on this report.
