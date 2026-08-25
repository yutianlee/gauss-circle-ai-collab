# Round 154 hostile terminal review: scope, masks, and implication

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Role: hostile terminal reviewer for scope, mask order, and downstream implication
- Starting graph SHA-256: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Allocation: 100% analytic/algebraic/source checking; 0% numerical experimentation

## 1. Result

The conductor candidate is correct as a **strict logarithmic-collar reduction plus route-scoped obstruction**.  I found no material scope, mask, endpoint, parity, completion, or implication defect in the selected kernel.

Precisely, the following claims survive hostile review:

1. the literal direct large-defect wave has the exact root-defect bijection (154.CA4), including both asymmetric cell endpoints and every parity and factorization of $N$;
2. the post-selection odd-$h$ rows have rank one, whereas the pre-selection ambient rows remain genuinely distinct;
3. the phase linearization is charged only on the selected scalar and has the target-safe error (154.CA6);
4. $J<|j|\le J(\log(2X))^A$ is an owner-complete target-safe collar for each fixed $A>0$, but this is only logarithmic and supplies no positive-power scale enlargement;
5. the exact ambient completion, including the Fourier zero mode and all imprimitive strata, gives (154.CA10);
6. restoring the target-safe exact and small-defect scalars before a **linear** full-cell completion is lawful, and the principal stationary completion self-returns to the accepted reciprocal row; and
7. the resulting no-go is confined to the displayed post-selection Cauchy, termwise DFI, and principal full-cell placements.  The signed outer-$j$ problem and every downstream owner remain open.

## 2. Exact statement and hypotheses audited

Let

\[
N=\lfloor X\rfloor,\qquad R=X^{1/4},\qquad
J=M^{3/4},\qquad K=(NM)^{1/2},\qquad 1\ll M\le R^2,
\]

and work for sufficiently large $X$, with the fixed-dilate, zero-extended actual profile

\[
w_U(n)=n^{-3/4}A_U(n),\qquad
\|w_U\|_\infty+\operatorname {Var}(w_U)
\ll_\varepsilon M^{-3/4}X^\varepsilon.
\]

The audited $Q_U$ is the direct wave (154.CA3), not the small-square-factor presentation from before the Round-153 recombination.  In particular, large-square-factor terms are present in $Q_U$; their separate target-safe ownership is not lost.  The external $B_{1,U}(1)$ remains outside the scalar.

For (154.CA10), $Q_U(V)$ means either signed block $V<\pm j\le2V$, intersected with the literal cell, support, strict mask, and actual profile, with the two signs then added at constant cost.  In the ambient completion $q=4N$, $d=(h,N)$ is necessarily odd, $q'=q/d\equiv0\pmod4$, and the surviving dual frequencies are $b=2dv$.  No claim assumes $N$ odd, prime, squarefree, or coprime to a Fourier frequency.

## 3. Proof and seam derivation

### Cell, converse, and full partition

A tie would imply (4Nn=(2k+1)^2), impossible modulo four.  Squaring the strict nearest-integer inequalities gives exactly

\[
k^2-k+1\le Nn\le k^2+k,\qquad -k\le j=k^2-Nn\le k-1.
\]

The converse follows from the same strict squared inequalities, and the cell gives (k^2-j>0).  The endpoint intervals

\[
I_k=[k^2-k+1,k^2+k]\cap\mathbb Z
\]

satisfy (I_1=[1,2]) and
(min I_{k+1}=max I_k+1).  Thus the full cells really do partition all positive integers, once each.  In particular, (j=-k) is the last point of (I_k), while (j=k-1) is its first point; neither is duplicated or lost.

### Selected rows versus ambient rows

On the selected graph (t=k^2-j=Nn), (n) odd, writing (h=r+4m) gives

\[
e_{4N}(ht)=e(rn/4),\qquad
T_{1+4m}=iQ_U,\qquad T_{3+4m}=-iQ_U.
\]

Consequently normalized $h$-Cauchy is equality and its pair kernel retains every ordered pair.  Before the $h$-sum imposes $N\mid k^2-j$, however,

\[
e_{4N}((r+4m)(k^2-j))
=e_{4N}(r(k^2-j))e_N(m(k^2-j)),
\]

so the ambient rows depend genuinely on $m$.  The candidate never transfers the selected-row collapse to this ambient array.

### DFI completion and every restored cost

Finite Fourier inversion and the all-parity Gauss evaluation give, on the $d$-stratum,

\[
\mathcal G(h,2dv;4N)
=d(1+i)\epsilon_a^{-1}\Bigl(\frac{q'}a\Bigr)
\sqrt{q'}e_{q'}(-\bar a v^2).
\]

After multiplication by $\chi_4(h)e_{4N}(-hj)$, the complete unit-$a$ sum is the DFI theta Kloosterman sum
$K(-v^2,-j;q')$.  Lemma 6.1 applies for every $q'\equiv0\pmod4$, including composite $q'$, and yields

\[
|K(-v^2,-j;q')|
\le (v^2,j,q')^{1/2}(q')^{1/2}\tau(q').
\]

The candidate's added normalized identity (154.CA22a) explicitly retains the exterior factor $d\sqrt{q'}$, the selector and Fourier normalizations $(2Nq)^{-1}$, and the exact range $v\bmod(q'/2)$.  After the second $\sqrt{q'}$ from DFI, these factors cancel to the scale $(2N)^{-1}$ before the $d,v,j$ sums.  For nonzero $v$, the BV Fourier estimate and the condition $c\mid v^2\Rightarrow s(c)\mid v$, with $c^{1/2}/s(c)\le1$, give

\[
\sum_{v\ne0}|\widehat B_j(2dv)|(v^2,j,q')^{1/2}
\ll_\varepsilon M^{-3/4}q'X^\varepsilon.
\]

Summing $q'=4N/d$ over all odd $d\mid N$ costs only $X^\varepsilon$, and the outer block of $O(V)$ defects gives $M^{-3/4}V X^\varepsilon$.  The dual zero mode is separate: using

\[
\sum_{j\in I}(j,Q)^{1/2}
\ll_\varepsilon (|I|+Q^{1/2})Q^\varepsilon
\]

and $|\widehat B_j(0)|\ll KM^{-3/4}X^\varepsilon$ gives

\[
M^{-3/4}\frac KN(V+N^{1/2})X^\varepsilon
\ll_\varepsilon (M^{-3/4}V+M^{-1/4})X^\varepsilon.
\]

This verifies (154.CA10) with the zero mode, every gcd stratum, the full two-adic modulus, both signs, the $j$- and $h$-outer sums, the literal endpoints, and the profile variation all restored.

### Scalar restoration and mask order

If $E_U=P_U-Q_U$ is the already owned exact-plus-small-defect scalar, then

\[
E_U=O_\varepsilon(X^\varepsilon),\qquad Q_U=P_U-E_U.
\]

It is therefore lawful to pass to $P_U$ before the linear full-cell Fourier/stationary transform and return to $Q_U$ afterward.  This is not deletion of a mask in a correlation.  In Section 3 of the candidate the strict block mask remains in $B_j$; in Section 4 it is removed only through this scalar identity before completion.  The principal saddle then has $n_*=4N/a^2$, phase $e(N/a)$, and the accepted reciprocal symbol, so the claimed principal self-return is correctly scoped.

## 4. First doubtful or unproved step

The first missing mathematics is still a normalized, mask-preserving signed outer-defect estimate after the exact completion, equivalently a signed cross-fibre estimate for the selected linearized phase.  It must retain the $d\sqrt{q'}/(2Nq)$ completion factors now printed in (154.CA22a), the literal range $v\bmod(q'/2)$, the nonseparable $\widehat B_j(2dv)$, both signs, all cell/profile endpoints, and the strict mask.

Neither the large right side of (154.CA10), a positive Cauchy diagonal, nor a capacity is a lower bound for $Q_U$.  DFI Lemma 6.1 matches each fixed completed Kloosterman sum, not the remaining signed $j$-dispersion.  The absence of a source theorem for that dispersion is method evidence only.  Thus the candidate's no-go is not overstated: a future joint masked $h$-$k$-$j$ argument or selected signed $k$-$j$ theorem remains logically open.

The polylogarithmic collar is genuinely owner-complete because

\[
\sum_{0<|j|\le H}\rho_N(j)\ll_\varepsilon HX^\varepsilon,\qquad
H=J(\log(2X))^A<N,
\]

and multiplication by $M^{-3/4}$ makes its weighted mass polylogarithmic.  Replacing $H$ by $JM^\delta$ leaves $M^\delta$, so this argument gives no fixed positive-power enlargement.  No stronger scale statement should be inferred.

## 5. Hostile controls and counterexample attempts

| Control | Outcome |
|---|---|
| Even $N$ | PASS.  For $N=2$, the two quotient classes are $2,6\pmod8$; odd frequencies have $d=1$ and effective modulus $8$.  The selector gives $+1,-1,0$ on odd, opposite odd, and even quotients exactly. |
| Composite/even $N$ | PASS.  For $N=6$, the exact strata are $d=1,3$, with $q'=24,8$; the two-adic factor is never divided away. |
| Composite nonsquarefree $N$ | PASS.  For $N=9$, $d=1,3,9$ gives $q'=36,12,4$; all are legal DFI moduli and the imprimitive factors in (154.CA21) have the required size. |
| Prime $N=p$ | PASS/hostile obstruction.  With all supported $k<p/2$, $p\mid(k_1-k_2)(k_1+k_2)$ at fixed $j$ forces $k_1=k_2$.  Hence a fixed-$j$ root-cancellation claim fails on this allowed class, exactly as the reports state; the candidate does not use such a claim. |
| Endpoint $j=-k$ | PASS.  It gives $t=k^2+k=\max I_k$, and the next cell starts at $t+1$. |
| Endpoint $j=k-1$ | PASS.  It gives $t=k^2-k+1=\min I_k$, one above the preceding cell. |
| Mask cross terms | PASS.  If $P=L+E$, then $|P|^2=|L|^2+2\Re(L\bar E)+|E|^2$; even $|E|\ll X^\varepsilon$ does not make the mixed term target-safe without a bound for $L$.  The candidate never makes this replacement inside a correlation. |
| Polylog collar | PASS/only logarithmic.  Root counting controls the entire literal collar, including signs and endpoints, but leaves $M^\delta$ for a power collar. |
| Downstream implication | PASS.  Nothing is transferred to $D>1$, $L>1$, growing-$M$ generic $t=1$, an original $t\ge2$ layer, the Round-138 cross owner, the rest of M1, M2, endpoint assembly, M9, the bridge, the quarter target, or either global exponent. |

One sibling-only wording inconsistency is quarantined: the source report's prose says the large-square-factor sector is not put back, while its displayed $Q_U$ and the selected candidate's (154.CA3) do include it.  The candidate uses the correct direct-wave scope, so this sentence must not be copied into state text.  It does not affect the proofs of (154.CA9) or (154.CA10).

## 6. Dependencies and exact artifacts used

This review used:

1. `protocol.md`;
2. `state/active_campaign.yml` and the relevant nodes of `state/proof_obligations.yml`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/barrier_packet.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`;
5. all three Round-154 reports: `large_defect_root_dispersion_attack.md`, `blind_quadratic_root_wave_feasibility.md`, and `quadratic_root_completion_source_audit.md`;
6. the accepted Round-152 and Round-153 conductor adjudications for the scalar-owner and recombination seams; and
7. Duke--Friedlander--Iwaniec, *Weyl Sums for Quadratic Roots*, Section 6, especially the definition (6.3) and Lemma 6.1.

No numerical computation was used.  The finite examples above are exact symbolic controls.

## 7. Recommended state effect and terminal verdict

Promote only the selected kernel exactly as scoped:

- (154.CA4), (154.CA5)--(154.CA6), and the strict logarithmic collar (154.CA8)--(154.CA9);
- the post-selection equality (154.CA18)--(154.CA19);
- the ambient Gauss/theta-Kloosterman conversion, its normalized form (154.CA22a), and complete dyadic upper bound (154.CA20)--(154.CA23), (154.CA10);
- the principal full-cell reciprocal self-return after lawful scalar restoration; and
- the route-scoped obstruction, with the normalized signed outer-$j$ theorem retained as open.

Required corrections before promotion: **none to the conductor candidate**.  The added (154.CA22a) supplies the previously implicit normalization and exact $v$-range.  Do not promote the quarantined sibling prose claiming that the direct $Q_U$ excludes large-square-factor terms.  Make no positive-power, downstream-owner, endpoint, M9, bridge, target, or exponent change.

GREEN
