# Round 126 hard-TOP parity spectral/operator attack

## 1. Result: a strict noninvertible square-product sector and an exact offset-band inverse theorem

There is a rigorous but partial positive result, followed by a sharp stopping point.

**Square-product projection lemma.** Let
\[
 (A_Lc)(m):=\sum_{\substack{h\in\mathscr H_L\\m\leq h\leq4m}}
 c_h\,a_{\rm end}(h,m)e(J\sqrt{hm}),\qquad J=\sqrt X,
\]
and let $A_L^{\square}$ be the genuinely noninvertible entry projection obtained by inserting $1_{hm\text{ is a square}}$. If
$A_*:=\sup_{h,m}|a_{\rm end}(h,m)|$, then, uniformly for every vector with
$|c_h|\leq1$,
\[
 \boxed{\ \|A_L^{\square}c\|_2^2
       \ll A_*^2L^{3/2}.\ }
\tag{126.1}
\]
In particular, for the actual parity vector $c_h=\chi_4(h)$, this complete entry sector is $L^2X^\varepsilon$-safe (indeed it has a power margin) because $A_*\ll_\varepsilon X^\varepsilon$. No endpoint, star, floor, or support atom is removed inside this projection.

**Signed offset-band inverse theorem.** Write the literal one-orientation correlations as
\[
 K_r:=\sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}
 e\!\left(-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}\right).
\tag{126.2}
\]
Thus
\[
 \mathcal E_L^{\rm top}=\mathcal D_L+2\Re\sum_{r=1}^{N_L}(-1)^rK_r,
 \qquad N_L\ll L.
\tag{126.3}
\]
Let $S_L\leq 1+\lceil\log_2(2+N_L)\rceil$ be the number of nonempty dyadic offset bands
$I_j=[2^j,2^{j+1})\cap[1,N_L]$. If
$\Delta:=\mathcal E_L^{\rm top}-\mathcal D_L>0$, then some complete band $I_j$ obeys
\[
 \boxed{\ \Re\sum_{r\in I_j}(-1)^rK_r
       \geq \frac{\Delta}{2S_L}.\ }
\tag{126.4}
\]
More generally, for every $1\leq R\leq N_L$, some consecutive complete offset interval $I$ of length at most $R$ obeys
\[
 \Re\sum_{r\in I}(-1)^rK_r
 \geq \frac{\Delta}{2\lceil N_L/R\rceil}
 \geq \frac{R\Delta}{4N_L}.
\tag{126.5}
\]
This is a noninvertible, sign-preserving spectral localization: it retains the actual coefficient and all one-count slabs jointly, and takes neither an offsetwise modulus nor both orientations. Consequently every genuine excess above the diagonal can be localized to a strictly smaller complete signed offset family. It is only an inverse theorem; it does not estimate the selected band.

No full actual-vector contraction
$\mathcal E_L^{\rm top}\ll L^2X^\varepsilon$ is proved. The first remaining object is precisely the selected signed actual-symbol band in (126.4) or (126.5). Thus the main hard-TOP lane must still be parked at (126.D2), equivalently at the Round-110 one-sided completed real scalar.

## 2. Exact statement, hypotheses, operators, and capacities

Assume the literal Round-75 hard block from the brief: $X\geq2$, $J=\sqrt X$, $\mathscr H_L$ is the actual finite odd height support of one polynomial intermediate block, all nonzero entries satisfy $h,m\ll L$, $m\leq h\leq4m$, and
$A_*\ll_\varepsilon X^\varepsilon$. These are exactly the support and bounded-entry facts used in (126.D1)--(126.D2). Zero extension is understood everywhere.

The matrix $A_L:\ell^2_h\to\ell^2_m$ has entries
\[
 A_L(m,h)=1_{h\in\mathscr H_L}1_{m\leq h\leq4m}
 a_{\rm end}(h,m)e(J\sqrt{hm}).
\tag{126.6}
\]
For the actual vector $\chi=(\chi_4(h))_{h\in\mathscr H_L}$,
\[
 R=A_L\chi,
 \qquad \mathcal E_L^{\rm top}=\|A_L\chi\|_2^2,
 \qquad \mathcal D_L=\|A_L\|_{\rm HS}^2\ll A_*^2L^2.
\tag{126.7}
\]
The relevant comparison capacities are:

* $\|\chi\|_2^2\ll L$, so the coefficient-blind Hilbert--Schmidt comparison gives only
  \[
  \|A_L\chi\|_2^2\leq\|A_L\|_{\rm HS}^2\|\chi\|_2^2
  \ll A_*^2L^3.
  \tag{126.8}
  \]
  This is the coherent hard-TOP capacity.
* The desired actual scalar is $L^2X^\varepsilon$. A Loewner or operator-norm estimate $A_L^*A_L\ll LX^\varepsilon I$ would imply it, but is a stronger arbitrary-input theorem and is not established.
* For any offset interval $I$, coefficientwise absolute summation in (126.2) has capacity
  \[
  \left|\sum_{r\in I}(-1)^rK_r\right|
  \ll A_*^2|I|L^2,
  \tag{126.9}
  \]
  and the full family has $A_*^2L^3$ capacity. The inverse theorem preserves signs and therefore does not assert (126.9) as an estimate for the actual band.
* In the primitive adjacent-transport notation, the already audited coefficient-blind common-comb capacity is $D_{\rm ray}L^2$, and the available absolute endpoint capacity is $L^2\sqrt\kappa$, with $\kappa=JD_{\rm ray}/(AL)\geq D_{\rm ray}$. Neither norm is invoked here.

For the strict sector define
\[
 A_L^{\square}(m,h):=1_{hm=\square}A_L(m,h),
 \qquad A_L^{\rm ns}:=A_L-A_L^{\square}.
\tag{126.10}
\]
This is an entrywise arithmetic projection and hence is noninvertible. Its exact capacities are
\[
 \|A_L^{\square}\|_{\rm HS}^2\ll A_*^2L\log(2L),
 \qquad
 \|A_L^{\square}c\|_2^2\ll A_*^2L^{3/2}\quad(|c_h|\leq1).
\tag{126.11}
\]
The norm decomposition is used only through
\[
 \|A_L\chi\|_2\leq
 \|A_L^{\square}\chi\|_2+\|A_L^{\rm ns}\chi\|_2.
\tag{126.12}
\]
Thus a bound of target size for the nonsquare complement would imply the full target, while any large violation satisfies the exact inverse lower bound
\[
 \|A_L^{\rm ns}\chi\|_2
 \geq \sqrt{\mathcal E_L^{\rm top}}-O(A_*L^{3/4}).
\tag{126.13}
\]
No false orthogonality between the two entry projections is asserted.

## 3. Proof and derivation

### 3.1 Square-product projection

Write every positive active $m$ uniquely as $m=du^2$, with $d$ squarefree. Then
\[
 hm\text{ is a square}\quad\Longleftrightarrow\quad h=dv^2
\tag{126.14}
\]
for an integer $v$. The hard affine support becomes $u\leq v\leq2u$. Since $h,m\ll L$, for each squarefree $d$ the possible $u$'s and, for any fixed $u$, the possible $v$'s are both
\[
 O\!\left(1+\sqrt{L/d}\right).
\tag{126.15}
\]
Therefore, for arbitrary $|c_h|\leq1$, the triangle inequality is used only inside this sparse projected column and gives
\[
 \begin{aligned}
 \|A_L^{\square}c\|_2^2
 &\leq A_*^2\sum_{\substack{d\leq CL\\d\ {\rm squarefree}}}
 \#\{u\}\left(\sup_u\#\{v:u\leq v\leq2u\}\right)^2\\
 &\ll A_*^2\sum_{d\leq CL}\left(1+\sqrt{L/d}\right)^3\\
 &\ll A_*^2\left(
 L+\sqrt L\sum_{d\leq CL}d^{-1/2}
 +L\sum_{d\leq CL}d^{-1}
 +L^{3/2}\sum_{d\geq1}d^{-3/2}\right)\\
 &\ll A_*^2L^{3/2}.
 \end{aligned}
\tag{126.16}
\]
The same parameterization with two rather than three counting factors gives
$\|A_L^{\square}\|_{\rm HS}^2\ll A_*^2L\log(2L)$. This proves (126.1) and (126.11). Notice that the phase, parity, ceilings, and endpoint values were never altered; discarding their cancellation can only enlarge this already target-safe sparse sector.

### 3.2 Exact parity spectral expansion

Enumerate odd heights as $h=h_0+2t$. Since
$\chi_4(h)=\sigma_0(-1)^t$, the actual vector is the $\pi$-spectral coefficient
\[
 \sum_h\chi_4(h)v_h=\sigma_0\sum_t(-1)^tv_t.
\tag{126.17}
\]
Expanding its squared norm once, with $s=h+2r$, gives exactly (126.3): one $h<s$ orientation, the factor
$\chi_4(h)\chi_4(h+2r)=(-1)^r$, and one outer $2\Re$. The overlap of the two hard affine supports is exactly
$\lceil(h+2r)/4\rceil\leq m\leq h$, which proves (126.2) without changing any one-count seam.

### 3.3 Noninvertible offset localization

Partition $\{1,\ldots,N_L\}$ into the nonempty dyadic $I_j$. Put
$Z_j=\Re\sum_{r\in I_j}(-1)^rK_r$. Equation (126.3) says
\[
 \Delta=2\sum_jZ_j.
\tag{126.18}
\]
If every $Z_j<\Delta/(2S_L)$, their sum would be $<\Delta/2$, a contradiction. This proves (126.4). Partitioning instead into
$K=\lceil N_L/R\rceil$ consecutive intervals of length at most $R$ gives the first bound in (126.5); since $K\leq2N_L/R$, the second follows. This is a pigeonhole argument on signed real correlations, not on their moduli.

### 3.4 Why the proof stops here

The exact Hilbert-space high-pass identity
\[
 2\sum_t(-1)^tv_t=\sum_t(-1)^t(v_t-v_{t+1})
\tag{126.19}
\]
is an identity, not a contraction. For the admissible abstract control
$v_t=(-1)^tv$, its left side is coherent and (126.19) multiplies rather than suppresses the alternating mode. With $O(L)$ rows and
$\|v\|_2^2\asymp L$, the energy is $L^3$. Thus no multiplier argument depending only on parity, hard support, row count, bounded entries, total variation, or a coefficient-blind comparison norm can bridge (126.8) to the target. A successful continuation must estimate the actual kernel (126.2) on the localized band before any slabwise or modewise modulus.

No numerical experiment was used.

## 4. First doubtful or unproved step

There is no doubtful step in (126.1) or (126.4)--(126.5). The first unproved extension is the proposed actual-symbol spectral gap
\[
 \Re\sum_{r\in I}(-1)^rK_r\ll_\varepsilon L^2X^\varepsilon
\tag{126.20}
\]
uniformly for the complete interval $I$ selected by the inverse theorem (or any comparable complete band). Nothing in the permitted context bounds (126.20). Replacing it by an operator norm, by
$\sum_{r\in I}|K_r|$, by fixed-$a$ Gram energy, or by one-count-slab norms is exactly the invalid seam: those comparisons return capacities between $|I|L^2$ and $L^3$.

The first tempting spectral justification is also invalid. Parity places the vector at frequency $\pi$, but it does not show that the actual Gram spectral measure is small there. Square, Pell, fourth-power, exact-centre, and strict metric configurations prevent a uniform derivative or modulo-one gap, while (126.19) shows that the parity multiplier itself has eigenvalue $2$ on the dangerous mode. The accepted square-ray and exact-centre owners remain valid controls, but they do not estimate the nonsquare signed band (126.20).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| literal_Round75_hard_top_vector | **Pass.** Equations (126.6)--(126.7) are the literal $R_m$ vector with $a_{\rm end}$ and phase $e(J\sqrt{hm})$. |
| one_orientation_and_outer_2Re | **Pass.** Only $h<h+2r$ occurs in (126.2), followed once by $2\Re$ in (126.3). |
| diagonal_one_count_and_target | **Pass.** The diagonal is exactly $\|A_L\|_{\rm HS}^2\ll L^2X^\varepsilon$; the target and the $L^3$ coherent comparison are stated separately. |
| character_inside_vector_before_square | **Pass.** The vector is $A_L\chi$; $(-1)^r$ is derived only after the square is expanded. |
| hard_affine_support_and_zero_extension | **Pass.** Both appear in (126.6), and their exact overlap gives the moving lower ceiling in (126.2). |
| block_energy_vs_offdiagonal_realpart | **Pass.** Equation (126.3) is the exact energy/real-part identity. Round-110 completion is used only as the already accepted target-equivalent parked form. |
| parity_highpass_vector_scope | **Pass/no gain.** Equation (126.19) is retained as a Hilbert-space identity; no total-variation estimate is inferred. |
| actual_vs_adversarial_vectors | **Pass.** The aligned control $v_t=(-1)^tv$ explicitly rejects a coefficient-blind parity contraction. The only uniform bound proved here is on the sparse square-product projection. |
| square_Pell_fourth_power_resonances | **Pass with scope retained.** The new mask controls the direct $hm=\square$ entry sector, including its perfect-power instances. It is not identified with the accepted primitive $ab=\square$ ray owner. Pell, primitive square-ray, fourth-power reciprocal, exact-centre, and metric configurations remain inside the full signed inverse band unless already owned; none is deleted or double-owned. |
| one_count_slabs_retained_jointly | **Pass.** Neither (126.1) nor (126.4) factors into primitive rays, lifts, reciprocal modes, metric modes, or slabs. All such labels remain inside $a_{\rm end}$ and the literal support. |
| capacity_before_and_claimed_gain | **Pass.** Full Hilbert--Schmidt comparison: $L^3$. Target: $L^2$. Square projection: $L^{3/2}$. An offset band of width $R$: coefficient-blind $RL^2$. The inverse theorem claims localization, not an unproved power saving on that band. |
| endpoint_and_prior_owner_scope | **Pass.** Endpoint values, moving ceilings, collars, entries/exits, floors, stars, equality conventions, and all accepted owners are retained. The square mask is proved directly before transformed owner splitting. |
| owner_and_downstream_scope | **Pass.** The result concerns only the literal hard-TOP M2 vector. It proves no BAL, UNBAL, M1, complete M9-M2, endpoint-uniform, M9, or exponent statement. |

## 6. Dependencies and exact artifacts used

The report used only the generated brief and its permitted context:

1. rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/briefs/hard_top_parity_spectral_operator_attack.md;
2. protocol.md;
3. state/proof_obligations.yml;
4. state/active_campaign.yml;
5. strategy/conductor_0821_full_proof_strategy.md;
6. rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md;
7. rounds/codex-managed/m9-m2-global-signed-completed-directional/synthesis.md;
8. rounds/codex-managed/m9-m2-global-signed-completed-directional/reviews/conductor_round110_recombination_and_orientation.md;
9. rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/synthesis.md;
10. rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/derivation_packet.md.

No web source, numerical experiment, external theorem, sibling report, or unlisted artifact was used.

## 7. Recommended state effect

**Recommended effect: retain, with no promotion of the main hard-TOP target.**

After independent seam review, (126.1) may be promoted as a strict complete square-product entry-sector lemma, and (126.4)--(126.5) may be promoted as an exact one-way signed offset-localization reduction. They do not close M9-M2-top-endpoint-density-discrepancy-energy and do not justify changing any downstream blocker.

Park the unresolved lane at the exact vector
$\mathcal E_L^{\rm top}=\|A_L\chi\|_2^2$, equivalently the Round-110 one-sided completed real scalar. The smallest lawful next object is (126.20) on one complete localized band, with the actual coefficient, character, hard affine support, all resonant controls, and every one-count slab left inside the signed real sum. A coefficient-blind multiplier, fixed-$a$ Gram, slabwise modulus, adjacent total variation, scaled-comb norm, or further invertible transform should not be reopened as the claimed gain.
