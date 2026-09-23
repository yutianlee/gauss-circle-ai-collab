# Literal \(P_2\) determinant-fibre attack

## 1. Result

The complete \(P_2\) target is not proved.  There is, however, a
target-safe exact sector and a first rigorous obstruction for its complement.

Let
\[
 D:=D_L=\lceil\sqrt L\rceil,\qquad
 P_2=\mathbf 1_{\{|d-gm|\le D\}}
     \mathbf 1_{\{|d'-gm'|>D\}},
\]
and retain the physical primitive parameter \(\kappa\).  Then the exact
partition
\[
 P_2=P_{2,\ge D}+P_{2,<D},\qquad
 P_{2,\ge D}:=P_2\mathbf 1_{\{\kappa\ge D\}},\qquad
 P_{2,<D}:=P_2\mathbf 1_{\{\kappa<D\}},
\tag{1.1}
\]
has the following properties.

**Large-\(\kappa\) sector theorem.**  For both orientations, both frequency
signs, the \(T=0\) full inherited branch and the \(T\ge1\) strict
Farey-covector branch, and the literal Round-192 core operator,
\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D}W)\right|
 \ll_{B,C_0,\varepsilon}
 H_B\mathfrak m\kappa uX^\varepsilon,
\tag{1.2}
\]
and
\[
 \left|\mathscr R_{{\rm core},Y,H_B}^\sigma(P_{2,\ge D}W)\right|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{1.3}
\]
Here \(\mathfrak m\) is the spectral lift gcd and \(m\) remains the physical
cofactor.  No endpoint coefficient is replaced, no orientation is separately
normed, and no additional Farey or geometric mask is inserted.

The proof of (1.2) is stronger than required.  At the physical row-counting
level the surviving mass is
\[
 \ll Yu\,{J\over q}\left(1+{\kappa D\over L}\right)X^\varepsilon.
\tag{1.4a}
\]
After the complete anchor/Abel \(\ell^1\) factor \(q/J\) is restored, this
is
\[
 \ll Yu\left(1+{\kappa D\over L}\right)X^\varepsilon
 \ll \kappa uX^\varepsilon
 \qquad(\kappa\ge D).
\tag{1.4}
\]
The direct outer count is
\[
 \#P_{2,\ge D}
 \ll
 \sum_{D\le\kappa\ll L}
 D\left(1+{L\over\kappa}\right)^2
 \ll L^2+LD\log(2L)
 \ll L^2.
\tag{1.5}
\]

**Small-\(\kappa\) determinant-fibre obstruction.**  On the exact complement
\(P_{2,<D}\), lower closeness improves the fixed positive capacity only from
\(Y\kappa uX^\varepsilon\) to
\[
 YuX^\varepsilon.
\tag{1.6}
\]
Thus the remaining ratio to (1.2) is
\[
 {Y\over H_B\mathfrak m\kappa}.
\tag{1.7}
\]
The exact determinant relation does not itself recover this ratio.  In one
fixed primitive row the far-defect parameter has only \(O(1)\) surviving
samples in a height block, while in the minus orientation the complete
anchor-character factor is exactly constant along that row.  Consequently a
proof using only determinant-fibre multiplicity, support size, the anchor
Fourier phase, coefficient moduli, or separate orientation norms also proves
one of the required false shadows and cannot establish (1.2).  A completion
of \(P_{2,<D}\) needs a new cross-row correlation estimate for the actual
moving endpoint coefficients and square-root phases, with every core event
component and the cross-orientation Gram blocks present.  This is a scoped
no-go for the proposed within-row determinant-fibre dispersion mechanism,
not a lower bound for the literal operator and not a disproof of the full
\(P_2\) estimate.

## 2. Exact statement and hypotheses

All hypotheses and support restrictions are those of the selected Round-195
packet and the five accepted kernels.  In particular,
\[
 Q:=H_B,\qquad U=\mathfrak m q,\qquad
 Q\mathfrak m<Y,\qquad Y<h\le2Y,\qquad
 0<2\kappa gh<R_0,\qquad R_0\asymp L,
\tag{2.1}
\]
and every physical endpoint \(d,m,d',m'\) lies in its inherited \(L\)-shell.
The projective band contains
\[
 \#\{v\}\ll {uJ\over q}\le u.
\tag{2.2}
\]
The \(T=0\) projector is empty and leaves the complete inherited
\(\rho\)-large branch.  When \(T\ge1\), the simultaneous inequalities
\[
 |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1)
\tag{2.3}
\]
remain imposed.  These restrictions are never deleted in the argument.

Write
\[
 \delta:={d-gm\over g}.
\tag{2.4}
\]
The physical lower-close condition is \(|g\delta|\le D\).  Its accepted
consequence is the uniform bound \(g=O(1)\).

In the plus chart,
\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad h=Sv-Uw>0.
\tag{2.5}
\]
Put
\[
 \alpha=\kappa(U-v),\qquad
 \eta={d'-gm'\over g}.
\tag{2.6}
\]
Then
\[
 \delta=\alpha-2w,\qquad \eta=\alpha+2S,
\qquad
 w={\alpha-\delta\over2},\quad
 S={\eta-\alpha\over2},
\tag{2.7}
\]
\[
 2h=v\eta+U\delta-\kappa(U^2-v^2).
\tag{2.8}
\]
The tuple and endpoint data are
\[
 (d,m,d',m')
  =(\kappa gU,\ \kappa U-\delta,\
       g(\kappa v+\eta),\ \kappa v),
\tag{2.9}
\]
\[
 N_0^+=\kappa gU(\kappa U-\delta),\quad d_0^+=\kappa gU,
\qquad
 N_1^+=\kappa gv(\kappa v+\eta),\quad
 d_1^+=g(\kappa v+\eta).
\tag{2.10}
\]
Integrality and chart positivity require
\[
 \delta\equiv\eta\equiv\alpha\pmod2,\qquad
 \delta<\alpha<\eta.
\tag{2.11}
\]
Since \(\eta>\delta\), the upper failure is precisely \(g\eta>D\).

In the minus chart,
\[
 d=g(\kappa U+2S),\quad d'=\kappa gU,\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad h=Uw-vS>0.
\tag{2.12}
\]
Use the positive far magnitude
\[
 \eta:=-{d'-gm'\over g}.
\tag{2.13}
\]
Then
\[
 \delta=\alpha+2S,\qquad \eta=2w-\alpha,
\qquad
 S={\delta-\alpha\over2},\quad
 w={\eta+\alpha\over2},
\tag{2.14}
\]
\[
 2h=U\eta-v\delta+\kappa(U^2-v^2),
\tag{2.15}
\]
\[
 (d,m,d',m')
  =(g(\kappa v+\delta),\ \kappa v,\
       \kappa gU,\ \kappa U+\eta),
\tag{2.16}
\]
\[
 N_0^-=\kappa gv(\kappa v+\delta),\quad
 d_0^-=g(\kappa v+\delta),
\qquad
 N_1^-=\kappa gU(\kappa U+\eta),\quad d_1^-=\kappa gU.
\tag{2.17}
\]
Here
\[
 \delta\equiv\eta\equiv\alpha\pmod2,\qquad
 \delta>\alpha,\qquad \eta>-\alpha,
\tag{2.18}
\]
and the upper failure is again exactly \(g\eta>D\).

For either orientation the positive far defect is partitioned, without
overlap or omission, into dyadic intervals
\[
 E<g\eta\le2E,\qquad E\ge D,\qquad E\ll L,
\tag{2.19}
\]
with the final interval truncated at the physical endpoint bound.  There are
\(O(\log(2L))\) such scales.

The operator in (1.2) is the literal one.  It keeps both orientations
jointly, both frequency signs, the complete anchor Fourier sum, actual
Vaaler/profile endpoint products, the residual selector, squarefree and
coprimality masks, unequal endpoint translations and carries, Fejer weights,
square-root phases, cells, crossings, births, deaths, the physical-mask
commutator, conjugations, and zero extensions under one complex aggregate.
Only after that aggregate is formed is the single outer real part taken.

## 3. Proof and derivation

### 3.1. Primitive multiplicity and shell bounds

Equations (2.7) and (2.14) show that
\[
 (\kappa,g,U,v,\delta,\eta,\omega)
 \longmapsto (S,w,h;d,m,d',m')
\tag{3.1}
\]
has multiplicity one for each orientation \(\omega\in\{+,-\}\), provided the
displayed parity, positivity, and inherited endpoint conditions hold.  There
is no additional \(h\), \(S\), or \(w\) multiplicity hidden in the
determinant fibre.

At fixed height, (2.8) and (2.15) give respectively
\[
 \eta={2h-U\delta+\kappa(U^2-v^2)\over v},
\qquad
 \eta={2h+v\delta-\kappa(U^2-v^2)\over U}.
\tag{3.2}
\]
Thus a fixed primitive row has at most one far defect at a given \(h\).
Conversely, for fixed \((\kappa,U,\delta,\eta,h)\), the possible \(v\)'s
satisfy
\[
 \kappa v^2+\eta v+U\delta-\kappa U^2-2h=0
\quad(+),
\tag{3.3}
\]
\[
 \kappa v^2+\delta v+2h-U\eta-\kappa U^2=0
\quad(-),
\tag{3.4}
\]
so there are at most two algebraic choices before the primitive, shell, and
congruence restrictions are imposed.

The endpoint shells and \(g=O(1)\) imply in both charts
\[
 U,\ v\ll 1+{L\over\kappa},\qquad \kappa\ll L.
\tag{3.5}
\]
They also give \(\kappa v\asymp L\) in the plus chart and
\(\kappa gU\asymp L\) in the minus chart, with the analogous companion
relations whenever they are used below.  Shell endpoints can only shorten
the intervals counted below; they do not add multiplicity.

### 3.2. Direct outer count on \(\kappa\ge D\)

In the plus chart, after \((\kappa,U,v)\) is fixed, lower closeness is
\[
 |\kappa(U-v)-2w|\le {D\over g}.
\tag{3.6}
\]
It permits \(O(1+D/g)=O(D)\) integers \(w\).  For each such \(w\),
\[
 0<Sv-Uw<{R_0\over2\kappa g}
\tag{3.7}
\]
confines \(S\) to an interval of length
\[
 {R_0\over2\kappa gv}\ll1
\tag{3.8}
\]
because \(\kappa v\asymp L\).  Hence there are \(O(1)\) values of \(S\).

In the minus chart the roles are transposed.  Lower closeness is
\[
 |\kappa(U-v)+2S|\le {D\over g},
\tag{3.9}
\]
so there are \(O(D)\) values of \(S\).  For each of them,
\[
 0<Uw-vS<{R_0\over2\kappa g}
\tag{3.10}
\]
confines \(w\) to an interval of length
\[
 {R_0\over2\kappa gU}\ll1.
\tag{3.11}
\]
Both orientations therefore contribute
\[
 \ll D\left(1+{L\over\kappa}\right)^2
\tag{3.12}
\]
physical tuples for a fixed \(\kappa\).  Positivity, primitivity, parity,
the far inequality, residual selectors, the \(T\)-branch restrictions, and
all literal endpoint restrictions only delete tuples.  Summing (3.12),
\[
\begin{aligned}
 \sum_{D\le\kappa\ll L}
 D\left(1+{L\over\kappa}\right)^2
 &\ll DL+LD\log(2L)+DL^2\sum_{\kappa\ge D}\kappa^{-2}\\
 &\ll L^2+LD\log(2L)
 \ll L^2,
\end{aligned}
\tag{3.13}
\]
because \(D\asymp L^{1/2}\).  Both orientation charts are already included,
so there is no orientation multiplicity left to restore.

Every literal physical atom has size \(O(X^\varepsilon)\) after the standard
harmless divisor losses.  The exact physical-to-core identities are linear
finite decompositions: terminal and Fejer projections are deletions, while
outer/coprimality flips, carries, endpoint changes, phase changes,
birth/death zero extensions, and the mask commutator replace one atom by
only \(O(X^\varepsilon)\) signed literal event atoms.  Taking absolute values
at this point therefore preserves (3.13).  It does not invoke a scalar mask
after Fourier expansion and it does not separate the two orientations.
This proves the outer estimate (1.3), including one outer real part.

### 3.3. Fixed-packet count and the power ledger

For a fixed projective row and fixed height, primitivity
\((U,v)=1\) makes the plus solutions \(w\) one residue class modulo \(v\)
and the minus solutions \(S\) one residue class modulo \(U\).  Thus the
affine close variable moves in steps \(v\) or \(U\), respectively, both
comparable with \(L/\kappa\) on the relevant endpoint shell.  Therefore the
physical lower-close window has
\[
 O\left(1+{\kappa D\over L}\right)
\tag{3.14}
\]
sites.  There are \(O(Y)\) heights in the packet and, by (2.2),
\(O(uJ/q)\) projective rows.  With all literal bounded weights retained, the
physical row mass is consequently
\[
 \ll Yu\,{J\over q}
       \left(1+{\kappa D\over L}\right)X^\varepsilon.
\tag{3.15}
\]

The live height inequality in (2.1) gives
\[
 Y\ll {L\over\kappa}.
\tag{3.16}
\]
When \(\kappa\ge D\), \(L/\kappa\ll D\ll\kappa\) and \(D^2\asymp L\), hence
\[
 Y\left(1+{\kappa D\over L}\right)
 \ll {L\over\kappa}+D
 \ll\kappa.
\tag{3.17}
\]
The complete anchor Fourier expansion and exact Abel return cost at most
the inherited factor \(q/J\); this cancels the projective-band density
\(J/q\) in (3.15), without deleting a mode or taking an orientation norm.
Consequently (3.15) and (3.17) give
\[
 \ll\kappa uX^\varepsilon
 \le H_B\mathfrak m\kappa uX^\varepsilon.
\tag{3.18}
\]
As in the outer argument, every exact Round-191 event term, the Round-192
core indicator, the physical-mask difference term, conjugation, and zero
extension are bounded by the same deletion-stable atom count.  At \(T=0\)
the full branch is retained; at \(T\ge1\) (2.3) is retained.  This proves
(1.2).

For completeness, the accepted outer restoration is unchanged: the
projective density and \(q/J\) factor have already cancelled at fixed
packet, while the spectral lift coefficient
\(\mathfrak m^{-1}c_q(a)\), the complete anchor aggregate, the
\(J\)-band partition, and the divisor choices
\(\mathfrak mq\mid u\) incur only the already accepted
\(X^\varepsilon\)-losses (including the logarithmic anchor and
\(\tau_3(u)\) ledgers).  Together with either (3.13) or the accepted
fixed-to-outer summation, this yields exactly (1.3).  No \(E\)-sum is needed
for the absolute count; if the dyadic partition (2.19) is inserted, its
\(O(\log L)\) factor is absorbed in \(X^\varepsilon\).

### 3.4. The literal coefficient-vector Gram

The remaining discussion concerns the exact complement \(\kappa<D\).  It is
important first to state the Gram matrix that a successful dispersion
argument would have to bound.

Let \(\lambda_{N,\sigma}(d)\) denote the actual inherited endpoint
coefficient, including its literal Vaaler/profile value and all endpoint
arithmetic and residual selectors; it is set to zero off its true support.
Let
\[
 F_\eta=1-{2\kappa gh_\eta\over R_0},\qquad
 \Psi_\eta^\omega
 =e\!\left(\sigma\sqrt X
    \big(\sqrt{N_1^\omega}-\sqrt{N_0^\omega}\big)\right).
\tag{3.19}
\]
Before the exact event decomposition, the common physical component is
\[
 A_\eta^\omega
 =(-1)^{S_\omega}F_\eta\,
   \lambda_{N_1^\omega,\sigma}(d_1^\omega)
   \overline{\lambda_{N_0^\omega,\sigma}(d_0^\omega)}
   \Psi_\eta^\omega,
\tag{3.20}
\]
where
\[
 S_+={\eta-\alpha\over2},\qquad
 S_-={\delta-\alpha\over2}.
\tag{3.21}
\]
All quantities in (3.20) are actual functions of the primitive row; they
are not arbitrary arrays.

Write the physical masked row as
\[
 W_\omega^P(h)=\sum_t P_2(h,t)(-1)^tB_\omega(h,t).
\tag{3.22}
\]
The transported mask must be opened by the exact identity
\[
 P_hB_h-\chi P_-B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{3.23}
\]
The second term is the physical-mask commutator and cannot be dropped.
After the exact Round-191 decomposition, let
\[
 C_{\eta,e}^\omega(\mathbf r),\qquad
 \mathbf r=(\kappa,g,U,v,\delta),
\tag{3.24}
\]
be the zero-extended literal signed event components.  The label \(e\)
records, without amalgamation, the outer and coprimality flips, carry,
endpoint arithmetic/profile change, phase change, birth or death, mask
commutator, conjugation, cell and crossing data, and the exact Round-192
core selector.  These are the actual values generated from (3.20) and
(3.23).  They include the complete anchor Fourier coefficient and the
Fejer and square-root phases, rather than estimating them first.  Crucially,
the event terms are recombined with their signs before a norm:
\[
 C_\eta^\omega(\mathbf r)=\sum_e C_{\eta,e}^\omega(\mathbf r),\qquad
 V_{\mathbf r,E}^\omega(h)
 =\sum_{\substack{\eta:\ h_\omega(\mathbf r,\eta)=h\\
                   E<g\eta\le2E}}
 C_\eta^\omega(\mathbf r).
\tag{3.24a}
\]
The sum over \(\eta\) in (3.24a) has at most one term by (3.2).

For one far scale \(E\), the required joint two-orientation Gram matrix is
\[
\begin{aligned}
 \Gamma_{(\omega,\mathbf r),(\omega',\mathbf r')}^{(E)}
 &:=\sum_h V_{\mathbf r,E}^\omega(h)
       \overline{V_{\mathbf r',E}^{\omega'}(h)}\\
 &=\sum_{\eta,\eta'}\sum_{e,e'}
 C_{\eta,e}^\omega(\mathbf r)
 \overline{C_{\eta',e'}^{\omega'}(\mathbf r')}
 \mathbf 1_{\{h_\omega(\mathbf r,\eta)
                    =h_{\omega'}(\mathbf r',\eta')\}}
 \mathbf 1_{\substack{E<g\eta\le2E\\
                       E<g'\eta'\le2E}},
\end{aligned}
\tag{3.25}
\]
where
\(\mathbf r'=(\kappa',g',U',v',\delta')\) and
\(\omega,\omega'\in\{+,-\}\).  Thus the full matrix has
\(++,+-,-+,--\) blocks.  Its exact diagonal is
\[
 \Gamma_{(\omega,\mathbf r),(\omega,\mathbf r)}^{(E)}
 =\sum_h\left|V_{\mathbf r,E}^\omega(h)\right|^2
 =\sum_{\substack{\eta\\E<g\eta\le2E}}
   \left|\sum_e C_{\eta,e}^\omega(\mathbf r)\right|^2.
\tag{3.26}
\]
In particular, cross-event interference has not been replaced by an
orthogonal sum.  The cross-orientation blocks are part of the single outer
aggregate.  Taking separate orientation norms would delete
\(\Gamma^{+-}\) and \(\Gamma^{-+}\) and is not an estimate for the assigned
operator.

At the raw common site, (3.25) contains the fixed lower-endpoint factor times
the genuine correlation of the moving upper endpoint coefficients,
square-root phases, Fejer factors, and selectors.  Carries,
birth/death terms, and (3.23) can also produce singleton diagonal
coordinates.  Equation (3.26) is nonnegative, but the available interfaces
give no lower comparison of it with the positive capacity and no
coefficient-sensitive upper saving.  It would be invalid to replace the
actual \(C_{\eta,e}^\omega\) by bounded arbitrary vectors in either
direction.

The determinant collision equations in an off-diagonal block are explicit.
For two plus rows they are
\[
 v\eta+U\delta-\kappa(U^2-v^2)
 =v'\eta'+U'\delta'-\kappa'(U'^2-v'^2).
\tag{3.27}
\]
For two minus rows they are
\[
 U\eta-v\delta+\kappa(U^2-v^2)
 =U'\eta'-v'\delta'+\kappa'(U'^2-v'^2).
\tag{3.28}
\]
The cross equations equate the left side of (3.27) to the left side of
(3.28).  Within the same primitive row, equality of height forces
\(\eta=\eta'\).  Across different rows, (3.27)--(3.28) define the genuine
off-diagonal determinant fibres, but multiplicity alone does not control
their actual coefficient correlations.

With only the available pointwise information, the unconditional
coefficient-uniform off-diagonal estimate is the Gram Cauchy bound
\[
 \left|\Gamma_{(\omega,\mathbf r),(\omega',\mathbf r')}^{(E)}\right|
 \le
 \left(
 \Gamma_{(\omega,\mathbf r),(\omega,\mathbf r)}^{(E)}
 \Gamma_{(\omega',\mathbf r'),(\omega',\mathbf r')}^{(E)}
 \right)^{1/2}.
\tag{3.28a}
\]
Summing (3.28a) is exactly the positive row-capacity estimate; it is
unchanged by character erasure or phase conjugation and supplies no part of
the missing ratio (1.7).

### 3.5. Exact self-return on the small-\(\kappa\) complement

For \(\kappa<D\), (3.14) is \(O(1)\).  Hence the best positive count supplied
by lower closeness is (1.6).  It is target-safe on the further sector
\(Y\ll H_B\mathfrak m\kappa\), but on the complete exact complement it still
misses (1.2) by (1.7).

The determinant fibre does not provide a long one-row averaging variable.
Increasing \(\eta\) by \(2\) preserves parity and changes height by
\[
 h_+(\eta+2)-h_+(\eta)=v,\qquad
 h_-(\eta+2)-h_-(\eta)=U.
\tag{3.29}
\]
By (3.5) and (3.16), \(v,U\asymp L/\kappa\) on the corresponding shells and
the height block has length \(Y\ll L/\kappa\).  Consequently each fixed
primitive row contributes only \(O(1)\) far-defect samples.  Completion in
\(\eta\) within a row therefore has no length from which to recover (1.7).

There is also an exact phase collision.  At fixed row the anchor height
phase is
\[
 z_{\omega,v}^{\,h},\qquad
 z_{\omega,v}=e\!\left({\epsilon_\omega a\overline v_q\over q}\right),
\qquad \epsilon_+=1,\quad\epsilon_-=-1.
\tag{3.30}
\]
For the plus chart, (3.29) gives anchor ratio \(e(a/q)\), while
\((-1)^{S_+}\) flips.  Thus the combined character-anchor ratio is
\[
 -e(a/q).
\tag{3.31}
\]
For the minus chart, (3.29), \(U=\mathfrak mq\), and (3.21) give
\[
 e\!\left(-{a\overline v_qU\over q}\right)=1,
\qquad (-1)^{S_-}\ \hbox{unchanged}.
\tag{3.32}
\]
The combined character-anchor phase is therefore exactly constant along the
entire surviving minus far fibre.  The plus anchor has period \(q\), and the
combined plus factor has period \(2q\) in the parity steps.  These statements
are algebraic; the moving upper endpoint coefficient, square-root phase,
Fejer factor, and masks can still change.  They therefore do not imply a
literal lower bound.  They do prove that anchor orthogonality plus
determinant multiplicity cannot be the missing estimate.

Indeed, after coefficient moduli are taken, an unsigned or
phase-conjugating choice makes the minus anchor frame rank one along each
row.  Any claimed gain based only on support, multiplicity, or (3.30) would
survive that required false control.  Using separate orientation norms also
discards precisely the cross blocks where a compensating signed
commutator could occur.  Thus the first unproved estimate is necessarily a
joint cross-row bound for (3.25) using the actual upper endpoint products,
square-root phases, event vectors, and both orientations.  No such estimate
is present in the permitted interfaces.

## 4. First doubtful or unproved step

The first unproved step is a coefficient-sensitive off-diagonal theorem for
the full Gram matrix (3.25) on
\[
 \kappa<D,\qquad |g\delta|\le D,\qquad g\eta>D,
\tag{4.1}
\]
uniformly in the exact packet and in every dyadic \(E\).  It would have to
recover the factor \(Y/(H_B\mathfrak m\kappa)\) after summing the collision
surfaces (3.27)--(3.28), while retaining:

1. the actual moving endpoint coefficient products in (3.20);
2. Fejer and square-root phase variation;
3. carries, endpoint changes, cells, crossings, births, deaths, and the
   mask-commutator coordinates of (3.23)--(3.24);
4. the \(+-\) and \(-+\) Gram blocks;
5. both \(T\)-branches and the complete anchor aggregate.

The inherited results give neither such a correlation theorem nor a
diagonal estimate with the needed saving.  Fibre multiplicity (3.1)--(3.4)
is insufficient, because the one-row fibre has \(O(1)\) samples and the
minus anchor-character phase has the exact collision (3.32).  This is the
precise seam at which the complete \(P_2\) proof stops.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact_round193_P2_physical_mask | PASS.  The mask in (1.1) is exactly the lower-close/upper-far physical mask. |
| mask_before_Fourier_and_height_difference | PASS.  Counting starts from the physical tuples; (3.22)--(3.23) records the later exact transport. |
| exact_round192_core_and_T_zero_scope | PASS.  The exact core selector is retained; \(T=0\) keeps the full inherited branch. |
| strict_T_positive_Farey_covectors | PASS.  All inequalities (2.3) remain simultaneous deletions. |
| spectral_lift_gcd_vs_physical_cofactor_notation | PASS.  \(\mathfrak m\) and \(m\) are never identified. |
| both_orientation_primitive_charts | PASS.  Equations (2.5)--(2.18) treat both charts. |
| Delta_minus_Delta_plus_identity | PASS.  Equations (2.7)--(2.8) reproduce the plus identity, and (2.14)--(2.15) its signed minus counterpart. |
| lower_close_uniform_g_bound | PASS.  The inherited \(g=O(1)\) consequence is used and not strengthened. |
| upper_failure_positive_far_defect | PASS.  \(\eta\) is defined positively in each orientation and \(g\eta>D\). |
| dyadic_far_defect_partition | PASS.  Equation (2.19) is exact, including the truncated last block. |
| determinant_fibre_multiplicity | PASS.  Multiplicity one, unique \(\eta\) at fixed row and height, and the quadratic two-root bound are (3.1)--(3.4). |
| complete_anchor_Fourier_aggregate | PASS.  It remains inside \(\mathbf C\); only its exact ratios are diagnosed in (3.30)--(3.32). |
| actual_endpoint_coefficient_vectors | PASS.  Equations (3.19)--(3.25) use literal endpoint values, never arbitrary arrays. |
| squarefree_coprimality_and_residual_selectors | PASS.  They remain literal event/support coordinates. |
| unequal_endpoint_translations_and_carries | PASS.  They remain separate coordinates in (3.24). |
| birth_death_zero_extension_vectors | PASS.  They remain separate zero-extended coordinates in (3.24). |
| physical_mask_commutator | PASS.  It is the second term of the exact identity (3.23). |
| Fejer_square_root_phase_cells_crossings | PASS.  They are explicit in (3.19)--(3.24). |
| one_outer_real_part | PASS.  Neither proof nor Gram separates orientations before the real part. |
| TTstar_Gram_before_positive_norms | PASS.  The full four-block Gram (3.25) is formed before any positive norm. |
| Gram_diagonal_and_phase_collisions | PASS.  The exact diagonal is (3.26); the anchor-character collisions are (3.31)--(3.32), without an unsupported lower bound. |
| off_diagonal_determinant_fibres | PASS/OPEN.  Their exact equations are (3.27)--(3.28); the needed coefficient-sensitive estimate is the first open seam. |
| Y_over_HBmfrak_deficit | PASS.  The residual ratio is exactly (1.7). |
| fixed_packet_to_outer_power_ledger | PASS for \(P_{2,\ge D}\), OPEN for \(P_{2,<D}\).  Equations (3.13), (3.15)--(3.18) restore the proved sector; the small-\(\kappa\) deficit is not hidden. |
| original_t1_only_downstream_scope | PASS.  The result concerns only the stated hard-\(M_1\), original-\(t=1\), \(\rho\)-large core submask. |
| exponent_quarantine | PASS.  No theorem endpoint or accepted exponent is changed. |

The required false controls also behave correctly.  The large-\(\kappa\)
proof is an absolute target-safe count and does not claim cancellation.  The
proposed small-\(\kappa\) dispersion fails the unsigned,
character-erased, phase-conjugating, adversarial bounded-coefficient, and
separately normed-orientation controls; this failure is why no complete
\(P_2\) theorem is asserted.

No numerical or symbolic diagnostic was used.  The effort was entirely
analytic and algebraic.

## 6. Dependencies and exact artifacts used

Only the selected-context artifacts were used:

- protocol.md;
- state/proof_obligations.yml at the Round-195 brief's graph hash
  \(815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89\);
- state/active_campaign.yml;
- state/failure_ledger.md;
- strategy/round195_m1_t1_p2_determinant_fibre_vector_dispersion_strategy.md,
  reloaded after the conductor's byte-clean repair;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md;
- rounds/codex-managed/full-proof-round191-193-strategy-literature-review/synthesis.md;
- rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md;
- rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/synthesis.md;
- the assigned Round-195 task brief.

No claimant outside the selected context, sibling report, web source,
diagnostic, or post-Round-195 state artifact was used.

## 7. Recommended state effect

**Promote only after the required independent seam reviews:** record
\(P_{2,\ge D_L}\) as a proved internal target-safe strict sector with
fixed-packet bound (1.2), outer bound (1.3), and the one exact complement
\(P_{2,<D_L}\).

**Retain the owner open:** the complete \(P_2\) claim is not proved.
Record on the exact complement that lower closeness gives capacity
\(YuX^\varepsilon\), leaving \(Y/(H_B\mathfrak m\kappa)\), and that
within-row determinant-fibre/anchor dispersion self-returns by
(3.29)--(3.32).  The next admissible seam is the joint cross-row actual
coefficient-vector Gram estimate identified in Section 4.

Do not change M9-M1, M9, either bridge, the quarter target, or any exponent.
This report is candidate evidence only and makes no authoritative state
change.
