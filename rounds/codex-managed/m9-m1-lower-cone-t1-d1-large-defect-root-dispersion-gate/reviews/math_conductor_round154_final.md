# Round 154 terminal mathematical review

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Role: independent terminal mathematical reviewer
- Object reviewed: `conductor_round154_root_dispersion_adjudication.md`
- Starting graph SHA-256: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Allocation: 100% analytic/algebraic verification; 0% numerical experimentation

## 1. Result

The conductor candidate is mathematically sound in its stated narrow scope.
I independently recover:

1. the exact nearest-integer bijection, including the asymmetric cell
   \(-k\le j\le k-1\), the converse, positivity, absence of ties, quotient
   parity, support injectivity, and multiplicity one;
2. the exact scalar-level linearization
   \[
   \sqrt{k^2-j}-k=-\frac{j}{2k}
   -\frac{j^2}{2k(k+\sqrt{k^2-j})^2}
   \]
   with total selected-graph error
   \(O_\varepsilon(N^{-1/2}M^{-1/4}X^\varepsilon)\), uniformly even at
   \(|j|\asymp k\);
3. the all-prime-power root bound and, for every fixed \(A>0\), the complete
   target-safe collar
   \[
      M^{3/4}<|j|\le M^{3/4}(\log(2X))^A;
   \]
4. the exact rank-one collapse of the post-selection odd-frequency rows and
   equality in normalized post-selection Cauchy, while the off-congruence
   ambient rows remain genuinely distinct;
5. the even-modulus, imprimitive quadratic Gauss formula, its conversion to
   the Duke--Friedlander--Iwaniec theta Kloosterman sum, and the fully restored
   block estimate
   \[
      |Q_U(V)|\ll_\varepsilon
      \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon;
   \]
6. the principal full-cell stationary phase, including its sign and symbol,
   as the inherited reciprocal-row self-return rather than a new gain; and
7. every relevant power at the owner endpoint
   \(M=R^{780/449}\).

The candidate does not prove the full large-defect estimate and does not
prove a positive-power enlargement of the defect collar.  Its proposed label
`strict_large_defect_root_range` is nevertheless licensed in the literal
owner sense because the polylogarithmic collar is a strict, completely owned
subset of the previously open region.  The label is GREEN only with the
explicit qualifier **fixed/polylogarithmic defect collar only**; it must not
be paraphrased as \(|j|\le J M^\delta\), as a new positive-power \(M\)-range,
or as an improvement of the Round-152 scale boundary.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,\qquad
 1\ll M\le R^2,\qquad J=M^{3/4},\qquad K=\sqrt{NM},
\]

and let the literal zero-extended inherited profile satisfy

\[
 \operatorname{supp}w_U\subset[cM,CM],\qquad
 \|w_U\|_\infty+\operatorname{Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon
\]

on its finitely many actual components, with the inherited half-open
endpoints.  The external factor \(B_{1,U}(1)\) is not part of the scalar and
remains \(O_\varepsilon(X^\varepsilon)\).  Define

\[
 Q_U=\sum_{\substack{n>0,\ n\ \mathrm{odd}}\\
 |k(n)^2-Nn|>J}}
 \chi_4(n)w_U(n)e(\sqrt{Nn}),\qquad
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor .
\]

For fixed \(A>0\), set \(L_A=(\log(2X))^A\).  The statement validated by
this review is

\[
 Q_U=Q_{U,A}+O_{\varepsilon,A}(X^\varepsilon),
\]

where

\[
 Q_{U,A}=\sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 |j|>JL_A,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right).
\]

The same selected sum may replace its last phase by \(e(-j/(2k))\) at
total cost

\[
 O_\varepsilon(K^{-1}M^{1/4}X^\varepsilon)
 =O_\varepsilon(N^{-1/2}M^{-1/4}X^\varepsilon).
\]

The completion statement is blockwise.  For either sign, or for their union,
let \(Q_U(V)\) denote the literal contribution with
\(V<|j|\le2V\), intersected with the exact cells and actual profile, where
\(J\lesssim V\lesssim K\).  Then exact finite completion and DFI Lemma 6.1
give

\[
 |Q_U(V)|\ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\]

No assertion is made for \(D>1\), \(L>1\), the growing-\(M\) generic
\(t=1\) sector, any original \(t\ge2\) layer, the Round-138 cross owner,
M2, endpoint assembly, M9, the bridge, the quarter target, or either global
exponent.  The full estimate below the inherited boundary
\(M^{449}\asymp R^{780}\) remains open.

## 3. Independent derivation

**Cell, converse, tie, parity, and injectivity.**  If
\(y=\sqrt{Nn}\) and \(k=\lfloor y+1/2\rfloor\), a tie would imply
\(4Nn=(2k+1)^2\), impossible modulo four.  Hence

\[
 k-\frac12<y<k+\frac12.
\]

After squaring and using integrality,

\[
 k^2-k+1\le Nn\le k^2+k,
 \qquad -k\le j=k^2-Nn\le k-1.
\]

Conversely, the displayed cell implies

\[
 (k-\tfrac12)^2<k^2-j<(k+\tfrac12)^2,
\]

and \(k^2-j\ge k^2-k+1>0\).  Divisibility by \(N\) therefore recovers one
positive quotient and the unique nearest integer.  The parity and sign are
exactly

\[
 \frac{k^2-j}{N}\text{ odd}
 \Longleftrightarrow k^2-j\equiv N\pmod{2N},
\]

\[
 \chi_4\!\left(\frac{k^2-j}{N}\right)=
 \begin{cases}
 +1,&k^2-j\equiv N\pmod{4N},\\
 -1,&k^2-j\equiv3N\pmod{4N}.
 \end{cases}
\]

These statements do not invert \(N\) and therefore lose no even-\(N\)
case.  On the fixed support dilation, \(k\asymp K\), the hull of all
supported \(k\)'s has length \(O(K)<N\), and \(2k<N\) for sufficiently
large \(X\).  Thus one residue class modulo \(N\) occurs at most once in
the supported \(k\)-hull, and a cell of \(2k<N\) consecutive defect values
contains at most one multiple of \(N\).  In particular \(n\mapsto k\) is
injective and \(n\mapsto(k,j)\) is bijective with the displayed pair set.

**Uniform linearization and total error.**  Put
\(s=\sqrt{k^2-j}\).  Rationalization gives the exact identity

\[
 -\frac{j}{k+s}+\frac{j}{2k}
 =-\frac{j^2}{2k(k+s)^2}.
\]

In the exact cell, \(|j|\le k\), \(s\asymp k\), and \(k\asymp K\), so
the phase displacement is \(O(K^{-1})\), including \(j=-k\) and
\(j=k-1\).  The selected graph has at most \(O(M)\) terms and weight
\(O_\varepsilon(M^{-3/4}X^\varepsilon)\).  Since
\(|e(x+u)-e(x)|\le2\pi|u|\), the total displacement is

\[
 O_\varepsilon(M\,M^{-3/4}K^{-1}X^\varepsilon)
 =O_\varepsilon(N^{-1/2}M^{-1/4}X^\varepsilon).
\]

The pricing is on the selected graph.  Pricing it over off-congruence
ambient points would be a different and invalid calculation.

**Prime powers and the logarithmic collar.**  For
\(p^\alpha\Vert N\), put
\(v=\min(v_p(j),\alpha)\).  If \(v<\alpha\) is odd there is no root of
\(x^2\equiv j\pmod{p^\alpha}\).  If \(v=2b<\alpha\), there are at most
\(2p^b\) roots for odd \(p\) and at most \(4p^b\) for \(p=2\).  If
\(v=\alpha\), the zero congruence has \(p^{\lfloor\alpha/2\rfloor}\)
roots.  CRT therefore gives, for \(j\ne0\),

\[
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)}.
\]

Moreover

\[
 \sqrt{(|j|,N)}\le
 \sum_{d\mid(|j|,N)}\sqrt d,
\]

so for \(1\le H<N\), including both signs,

\[
 \sum_{0<|j|\le H}\rho_N(j)
 \ll H\,2^{\omega(N)}\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon HX^\varepsilon.
\]

The supported \(k\)-hull is shorter than \(N\), so this residue count is
also a count of actual candidate pairs.  With \(H=JL_A<N\), multiplication
by \(M^{-3/4}X^\varepsilon\) gives \(L_A X^\varepsilon\), which is
\(O_{\varepsilon,A}(X^\varepsilon)\) after epsilon splitting.  Subtracting
the inherited \(|j|\le J\) owner proves the complete collar.  Replacing
\(L_A\) by \(M^\delta\) leaves the unabsorbed factor \(M^\delta\); neither
this count nor the DFI block estimate licenses a positive-power collar.

**Post-selection equality versus ambient rows.**  For every integer \(t\),

\[
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}\sum_{\substack{h\pmod{4N}\\h\ \mathrm{odd}}}
 \chi_4(h)e_{4N}(ht).
\]

Indeed, writing \(h=r+4m\), \(r\in\{1,3\}\), the \(m\)-sum first imposes
\(N\mid t\), and the two remaining rows give
\(2iN\chi_4(t/N)\), including zero when the quotient is even.  On the
already selected graph \(t=Nn\), \(n\) odd, define the row after removing
only \(\chi_4(n)\) from the coefficient.  Then

\[
 T_{1+4m}=iQ_U,\qquad T_{3+4m}=-iQ_U,
\]

and hence

\[
 \frac1{2N}\sum_{h\ \mathrm{odd}\ (4N)}|T_h|^2=|Q_U|^2.
\]

The Cauchy inequality used with the selector is equality.  Equivalently,
odd-\(h\) orthogonality keeps every pair because
\(N(n_1-n_2)\) is always divisible by \(2N\).  Before selection, however,
the factor \(e_N(m(k^2-j))\) is nonconstant and is precisely what imposes
the congruence.  The ambient rows therefore remain distinct; the selected
rank collapse cannot be used to discard their possible cancellation.

**Even-modulus Gauss evaluation and DFI conversion.**  Put \(q=4N\).  For
odd \(h\), let

\[
 d=(h,q)=(h,N),\qquad h=da,\qquad q_d=q/d.
\]

Then \(d\) is odd, \(q_d\equiv0\pmod4\), and \((a,q_d)=1\).  For

\[
 \mathcal G(h,b;q)=\sum_{x\pmod q}e_q(hx^2+bx),
\]

period splitting and the two-adic pairing give zero unless \(b=2dv\), and
otherwise

\[
 \mathcal G(h,2dv;q)=
 d(1+i)\epsilon_a^{-1}\left(\frac{q_d}{a}\right)
 \sqrt{q_d}\,e_{q_d}(-\bar a v^2),
 \qquad |\mathcal G|=\sqrt{8Nd}.
\]

For a fixed literal defect \(j\), zero-extend its ambient BV row \(B_j\)
to one residue system and write

\[
 \sum_kB_j(k)e_q(hk^2)
 =\frac1q\sum_{b\pmod q}\widehat B_j(b)\mathcal G(h,b;q).
\]

Restoring \(\chi_4(h)e_q(-hj)\), using
\(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\), and summing primitive
\(a\pmod{q_d}\) gives

\[
 \sum_{a\pmod{q_d}}^*
 \chi_4(da)(1+i)\epsilon_a^{-1}
 \left(\frac{q_d}{a}\right)
 e_{q_d}(-aj-\bar av^2)
 =(1+i)\chi_4(d)K(-v^2,-j;q_d).
\]

The mandatory prefactor \(d\sqrt{q_d}\) from the Gauss sum remains outside
this multiplier sum.  Thus the exact completed block has the normalization

\[
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{q_d}
 \sum_{v\ (q_d/2)}
 \widehat B_j(2dv)K(-v^2,-j;q_d),
\]

with the \(d\)-sum understood as the exact gcd strata.  This displayed
factor is essential: the candidate's (154.CA22) is the multiplier
\(a\)-sum, not the whole stratum.

DFI Lemma 6.1 gives

\[
 |K(-v^2,-j;q_d)|
 \le(v^2,j,q_d)^{1/2}q_d^{1/2}\tau(q_d).
\]

Consequently \(d\sqrt{q_d}\,q_d^{1/2}=dq_d=q\), exactly cancelling the
finite-Fourier factor \(1/q\); there is neither a missing \(d^{1/2}\) loss
nor a fictitious primitive saving.  The BV Fourier bounds are

\[
 |\widehat B_j(0)|\ll_\varepsilon KM^{-3/4}X^\varepsilon,
 \qquad
 |\widehat B_j(b)|\ll_\varepsilon M^{-3/4}X^\varepsilon
 \min\{K,q/|b|_q\}.
\]

For nonzero \(v\), divisor expansion of \((v^2,j,q_d)^{1/2}\) and the
condition
\(c\mid v^2\Rightarrow\prod_{p^e\Vert c}p^{\lceil e/2\rceil}\mid v\)
give

\[
 \sum_{v\ne0}|\widehat B_j(2dv)|(v^2,j,q_d)^{1/2}
 \ll_\varepsilon M^{-3/4}q_dX^\varepsilon.
\]

After \(1/(2N)\) and all \(d\)-strata, this is
\(O_\varepsilon(M^{-3/4}X^\varepsilon)\) per \(j\).  For \(v=0\),

\[
 \sum_{j\in I_V}(j,Q)^{1/2}
 \ll_\varepsilon(V+Q^{1/2})Q^\varepsilon
\]

gives

\[
 M^{-3/4}\frac KN(V+N^{1/2})X^\varepsilon
 \le\left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\]

This restores every \(h,d,v,j\), the Fourier zero mode, both signs, the
actual profile, and the exact cell endpoints, and proves the candidate's
block bound.

**Principal saddle and mask order.**  The inherited Round-152 scalar owners
give \(Q_U=P_U+O_\varepsilon(X^\varepsilon)\) after the exact and small
defects are restored at scalar level.  Full nearest cells then partition all
positive \(t=k^2-j\), so

\[
 P_U=-\frac{i}{2N}\sum_{h\ \mathrm{odd}\ (4N)}\chi_4(h)
 \sum_{t\ge1}w_U(t/N)e\!\left(\sqrt t+\frac{ht}{4N}\right).
\]

For \(h=4N-a\), the stationary point satisfies

\[
 \sqrt t=\frac{2N}{a},\qquad t/N=4N/a^2,\qquad
 e(\sqrt t-at/(4N))=e(N/a).
\]

The selector coefficient is \(i\chi_4(a)/(2N)\); negative curvature gives
\(e(-1/8)2(2N/a)^{3/2}\); and
\(w_U(4N/a^2)=N^{3/4}(2N/a)^{-3/2}A_U(4N/a^2)\).  Their product is exactly

\[
 e(1/8)N^{-1/4}\chi_4(a)A_U(4N/a^2)e(N/a),
\]

the inherited reciprocal principal row.  The Round-152 owner is used only
for its already proved scalar restoration and boundary/error ownership.  No
small-defect mask is deleted inside a correlation, and this self-return is
not a new estimate.

**Complete power ledger.**  Uniformly in the frozen range,

| object or placement | restored size |
|---|---:|
| modulus | \(N\asymp R^4\), \(q=4N\) |
| cutoff and root span | \(J=M^{3/4}\), \(K=N^{1/2}M^{1/2}=R^2M^{1/2}\) |
| reciprocal length | \(H_0=(N/M)^{1/2}=R^2M^{-1/2}\) |
| actual pairs in a \(V\)-block | \(O_\varepsilon(\min\{M,V\}X^\varepsilon)\) |
| weighted absolute block capacity | \(M^{-3/4}\min\{M,V\}X^\varepsilon\) |
| total weighted absolute capacity | \(M^{1/4}X^\varepsilon\) |
| scalar linearization error | \(N^{-1/2}M^{-1/4}X^\varepsilon\) |
| odd selector rows | \(2N\); exact \(d\)-stratum count \(\varphi(4N/d)\) |
| complete Gauss magnitude | \(\sqrt{8Nd}\) |
| termwise incomplete-Gauss block | \(M^{-3/4}V(N^{1/2}+M^{1/2})X^\varepsilon\) |
| DFI-completed block | \((M^{-3/4}V+M^{-1/4})X^\varepsilon\) |
| dense ambient \(h\)-Cauchy scale | \(K^{1/2}M^{-3/4}=N^{1/4}M^{-1/2}\) |
| reciprocal absolute capacity | \(N^{-1/4}H_0=N^{1/4}M^{-1/2}\) |
| positive defect-Cauchy majorant | \(VM^{-3/4}\) for \(V\le M\), \(V^{1/2}M^{-1/4}\) for \(V\ge M\) |

At the inherited endpoint \(M=R^{780/449}\), these become

\[
 \begin{gathered}
 J=R^{585/449},\qquad K=R^{1288/449},\qquad
 H_0=R^{508/449},\qquad K/N=R^{-508/449},\\
 M^{1/4}=R^{195/449},\qquad
 N^{-1/2}M^{-1/4}=R^{-1093/449},\qquad
 J/H_0=R^{77/449}.
 \end{gathered}
\]

The DFI bound is \(1+R^{-195/449}\) at \(V=J\), but its first term is
\(R^{703/449}\) at \(V=K\).  The termwise incomplete-Gauss bound is already
\(R^2+R^{390/449}\) at \(V=J\) and has leading top-block powers
\(R^{1601/449}\) and \(R^{1093/449}\).  Dense ambient Cauchy and the
reciprocal absolute capacity both leave \(R^{59/449}\); the total selected
absolute capacity is \(R^{195/449}\).  No one of these positive powers is
absorbed by \(X^\varepsilon\).  The endpoint itself is target-safe only by
the inherited Round-152 exponent-pair owner; Round 154 changes neither that
ownership nor its boundary.

## 4. First doubtful or unproved step

There is no doubtful step in the promoted cell, linearization, collar, row
equality, even-Gauss, or fixed-block DFI claims after the mandatory
\(d\sqrt{q_d}\) prefactor is written as above.  The wording "complete
\(a\)-sum" around candidate (154.CA22) must be read as the multiplier sum;
if it were read as the whole gcd stratum it would omit
\(d\sqrt{q_d}\).  The source report and (154.CA21) retain this factor, and
its exact cancellation against \(1/q\) after DFI is what yields
(154.CA10).  Any durable statement should print the full normalized formula
from Section 3 of this review.

The first genuinely unproved continuation is a signed outer-defect estimate
for all \(JL_A\lesssim V\lesssim K\), schematically

\[
 \sum_{V<|j|\le2V}\sum_{d\mid N}\sum_v
 \widehat B_j(2dv)K(-v^2,-j;4N/d),
\]

with the normalization, gcd strata, both signs, strict mask, literal
endpoints, zero mode, and stationary reciprocal subfamily retained.  The
coefficient is nonseparable in \(j\) and \(v\).  Termwise DFI produces the
top loss \(N^{1/2}M^{-1/4}\); post-selection \(h\)-Cauchy is equality;
fixed-\(j\) root Cauchy returns capacity (and has only one root for prime
\(N\)); and the principal stationary row self-returns.  Exact phase
collisions off the inherited \(j=0\) ray reduce to equality, but the only
elementary near-collision spacing is of order \(K^{-3}\), which does not
count the near-collision population.  A future proof needs a new signed,
mask-preserving outer-\(j\) correlation theorem or an argument avoiding
that dispersion interface.  Nothing reviewed proves such a theorem, and
nothing reviewed proves it impossible.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| `literal_direct_large_defect_wave` | **GREEN.** The literal \(D=d=L=1\) wave, \(\chi_4\), zero-extended profile, strict mask, and external \(B_{1,U}(1)\) seam are retained. |
| `owned_range_and_mask_order` | **GREEN.** Round-152 exact/small defects are restored only at scalar level before the full-cell self-return; no mask is erased in a correlation. |
| `exact_root_defect_bijection` | **GREEN.** Both directions, positivity, no tie, and multiplicity one are proved. |
| `nearest_cell_endpoints_and_converse` | **GREEN.** The literal endpoints are \(-k\) and \(k-1\); neither is symmetrized away. |
| `support_injectivity_and_unique_residue` | **GREEN.** Fixed dilates and sufficiently large \(X\) give \(2k<N\) and total \(k\)-span below \(N\). |
| `mod4N_quotient_character_completion` | **GREEN.** The sign \(-i\), factor \(1/(2N)\), all odd \(h\), quotient parity, and both parities of \(N\) are exact. |
| `all_parity_two_adic_imprimitive_Gauss` | **GREEN.** \(d=(h,N)\), \(q_d=4N/d\), the condition \(2d\mid b\), magnitude \(\sqrt{8Nd}\), Kronecker multiplier, and zero cases are all retained. |
| `positive_negative_and_dyadic_defects` | **GREEN.** Both signs and every block \(J\lesssim V\lesssim K\) are priced; no formal sign pairing is used. |
| `K_J_N_h_power_ledger` | **GREEN/OBSTRUCTION.** The general and \(M=R^{780/449}\) powers are reproduced above; every all-scale route retains a positive power. |
| `actual_profile_endpoints_and_B11` | **GREEN.** BV composition includes zero-extension jumps, component transitions, cell endpoints, and half-open cuts; the external factor only renames epsilon. |
| `Cauchy_diagonal_and_collision_survival` | **GREEN/OBSTRUCTION.** Selected \(h\)-Cauchy is equality, ambient rows are distinct, prime-modulus fixed-defect fibres have no inner cancellation, and near collisions remain unproved. |
| `completion_remainder_and_outer_sums` | **GREEN.** Finite inversion has no omitted remainder; nonzero modes, zero mode, all \(d,h,v,j\), and the separate termwise incomplete remainder are priced. |
| `source_theorem_quadratic_root_match` | **GREEN/PARTIAL.** The quoted DFI Lemma 6.1 matches the fixed-\(j\) theta Kloosterman sum, not the remaining nonseparable outer-\(j\) sum. |
| `absolute_capacity_vs_signed_sum` | **GREEN.** Raw counts, weighted upper capacities, positive Cauchy diagonals, and the signed scalar are never identified. |
| `D_L_generic_tge2_cross_and_downstream_scope` | **GREEN.** No conclusion is exported to any excluded fibre, layer, owner, endpoint assembly, M2, M9, bridge, target, or global exponent. |

All controls are analytical.  No numerical certification was used.

## 6. Dependencies and exact artifacts used

This review read only:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/large_defect_root_dispersion_attack.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/blind_quadratic_root_wave_feasibility.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/quadratic_root_completion_source_audit.md`; and
7. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`, only for the inherited exact/small-defect scalar owner, reciprocal-row owner, and boundary \(M^{449}\asymp R^{780}\).

No proof graph, proof draft, validation matrix, strategy file, barrier packet,
other candidate, or external webpage was inspected.  The primary-source
hypothesis cards used here are those reproduced in the assigned Round-154
source-audit report.  This review made no computation and no edit outside
its assigned review path.

## 7. Recommended state effect and final verdict

Recommend **promote**, with exact scope:

- promote the exact root-defect bijection and quotient parity formulas;
- promote the selected-graph linearization with its complete total error;
- promote, for each fixed \(A>0\), only the owner-complete collar
  \(J<|j|\le J(\log(2X))^A\);
- record the post-selection Cauchy equality, the full even-modulus
  Gauss/DFI conversion with the explicit \(d\sqrt{q_d}\) prefactor, the
  block bound, and the principal reciprocal self-return as route-scoped
  obstructions;
- retain the signed outer-defect wave beyond the collar as open; and
- make no positive-power scale, inherited owner-boundary, endpoint,
  downstream theorem, or global-exponent change.

The terminal label `strict_large_defect_root_range` is licensed only as a
strict **polylogarithmic defect collar**.  It does not license any statement
with \(M^\delta\), any new range of \(M\), or the full large-defect target.

**Final verdict: GREEN.**
