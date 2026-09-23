# Count, power, and masked-operator seam review

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Role: independent count/power/operator seam review
- Candidate SHA-256:
  c2cb78666e5396260a6a1951aa77f37356190bad44b423d4f4779b7c744e3819
- Starting graph SHA-256:
  815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89

## 1. Result

**Verdict: PASS.**

The candidate's two positive conclusions are justified:
\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma
        (P_{2,\ge D}W)\right|
 \ll_{B,C_0,\varepsilon}
 H_B\mathfrak m\kappa uX^\varepsilon
\tag{R1}
\]
and
\[
 \left|\mathscr R_{{\rm core},Y,H_B}^\sigma
        (P_{2,\ge D}W)\right|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{R2}
\]
Both orientations give the claimed \(O(D_L)\)-by-\(O(1)\) physical
count.  At fixed packet, endpoint-exact differencing costs at most
\(q/J\), which cancels the \(J/q\) density of the projective rows and
leaves \(O(D_LuX^\varepsilon)\).  The accepted terminal and Fejer terms
cost \(O(\kappa uX^\varepsilon)\), so \(\kappa\ge D_L\) proves (R1).
At outer level, the physical source is counted before Fourier or Abel
expansion and has \(O(L^2)\) atoms.  The accepted Round-187--192 safe
operators are deletion-stable when rerun on this physical mask, so the
exact source-minus-safe identity proves (R2).

No cancellation, arbitrary coefficient replacement, separate-orientation
norm, or unpriced submask is used.  I found no false or unproved step in
the selected large-\(\kappa\) theorem.

Two notational readings should be preserved in any durable kernel copy.
First, the \(P_-\) in candidate (195.C18) means the previous mask evaluated
at the transported site, \(P_{h-1}(t+\nu_\omega(h))\), not the current
mask at the old height.  Second, the sentence after candidate (195.C15)
counts the physical source before Abel expansion; it does not absorb a
\(q/J\) factor into \(X^\varepsilon\).  The candidate already pays that
factor explicitly at fixed-packet level in (195.C16), so neither point
requires a mathematical repair.

## 2. Exact statement and hypotheses

Put
\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 R_0=\lceil L\rceil,\qquad D=D_L=\lceil\sqrt L\rceil.
\tag{R3}
\]
Fix one nonempty inherited dyadic block \(Y<h\le2Y\), with
\(Q\mathfrak m<Y\), and retain the complete Round-192 core.  The exact
carrier hypotheses imported by that phrase include
\[
 u=gU,\qquad U=\mathfrak m q,\qquad
 (u,v)=1,\qquad (U,h)=1,\qquad
 0<2\kappa gh<R_0,
\tag{R4}
\]
together with the inherited oddness and positivity conditions,
\[
 U>4Q,\qquad q>Q,\qquad
 \mathfrak m|a|_q>Q.
\tag{R5}
\]
The spectral lift gcd \(\mathfrak m\) is distinct from the physical
cofactor \(m\).

The physical endpoints satisfy
\[
 N=dm,\qquad N+r=d'm',\qquad
 d,m,d',m'\asymp L,\qquad
 r=2\kappa gh,\quad0<r<R_0,
\tag{R6}
\]
and every atom has size \(O_\eta(X^\eta)\) for a fresh
\(\eta>0\), with every literal selector, endpoint coefficient, profile,
floor, star, half weight, Fejer factor, square-root phase, cell, crossing,
orientation, affine site, conjugation, and zero extension retained.

On the physical source, before Fourier expansion or height differencing,
let
\[
 P_2=\mathbf1_{\{|d-gm|\le D\}}
     \mathbf1_{\{|d'-gm'|>D\}},\qquad
 P=P_{2,\ge D}:=P_2\mathbf1_{\{\kappa\ge D\}}.
\tag{R7}
\]
The complement is exactly
\[
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D\}}.
\tag{R8}
\]

At \(T=0\), \(P_A=0\), the inverse-small set
\(\{0<|\rho|\le T\}\) is empty, and the entire inherited
\(\rho\)-large remainder is present.  At \(T\ge1\), every retained core
row satisfies simultaneously
\[
 |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1).
\tag{R9}
\]
These are row deletions only; neither branch is omitted from (R1) or
(R2).

## 3. Proof and independent derivation

### 3.1 Uniform \(g\), both orientation counts, and multiplicity

Lower closeness and the endpoint shell give
\[
 1\le g\le {d+D\over m}=O(1)
\tag{R10}
\]
uniformly for \(L\ge2\).  Hence summation over \(g\) costs an absolute
constant.

In the plus chart,
\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad
 h=Sv-Uw>0.
\tag{R11}
\]
For fixed \((\kappa,g,U,v)\), lower closeness is
\[
 |\kappa(U-v)-2w|\le D/g,
\tag{R12}
\]
so it permits \(O(D)\) integers \(w\).  For each such \(w\),
\[
 {Uw\over v}<S<
 {Uw\over v}+{R_0\over2\kappa gv}.
\tag{R13}
\]
Since \(\kappa v=m'\asymp L\), (R13) has length \(O(1)\) and
contains \(O(1)\) integers.

In the minus chart,
\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad
 h=Uw-vS>0.
\tag{R14}
\]
Now lower closeness is
\[
 |\kappa(U-v)+2S|\le D/g,
\tag{R15}
\]
so there are \(O(D)\) choices of \(S\).  For each,
\[
 {vS\over U}<w<
 {vS\over U}+{R_0\over2\kappa gU}.
\tag{R16}
\]
Because \(\kappa gU=d'\asymp L\), (R16) again has \(O(1)\)
integer points.

In either chart the selected variables recover the physical tuple
uniquely, subject to the inherited parity, positivity, primitivity, and
literal predicates.  Those predicates only delete candidates.  The two
charts are the two orientation labels already present in the physical
source and cost only an absolute factor.

The endpoint shells imply
\[
 U,v\ll1+{L\over\kappa},\qquad \kappa\ll L.
\tag{R17}
\]
Consequently
\[
\begin{aligned}
 \#\mathcal I_P
 &\ll
 D\sum_{D\le\kappa\ll L}
 \left(1+{L\over\kappa}\right)^2\\
 &\ll
 DL+DL\log(2L)
   +DL^2\sum_{\kappa\ge D}\kappa^{-2}\\
 &\ll L^2+LD\log(2L)
 \ll L^2,
\end{aligned}
\tag{R18}
\]
because \(D\asymp\sqrt L\).  There is no extra \(h\)-factor:
\(h\) is determined by \((U,v,S,w)\), and the proof counted the entire
range \(0<h<R_0/(2\kappa g)\), not only one dyadic block.

### 3.2 Fixed-packet row and anchor ledger

Fix
\[
 p=(\kappa,u,\mathfrak m,q,a,J,\sigma)
\tag{R19}
\]
and one literal projective row \(v\).  The preceding proof gives at most
\(O(D)\) nonzero \(P\)-selected physical atoms over the entire height
block, in each orientation.  For the zero-extended masked row \(W_v^P\),
the elementary total-variation inequality gives
\[
 \sum_h|\Delta^-W_v^P(h)|
 \le2\sum_h|W_v^P(h)|
 \ll_\eta DX^\eta.
\tag{R20}
\]
This includes mask births and deaths: no equality
\(P\Delta W=\Delta(PW)\) is used.

On \(J\le j_q(a,v)<2J\),
\[
 |1-z_{\omega,v}|^{-1}\ll q/J,
\tag{R21}
\]
and the literal projective band contains
\[
 \#\{v:J\le j_q(a,v)<2J\}\ll uJ/q
\tag{R22}
\]
rows.  Combining (R20)--(R22), jointly over both orientations before
the final real part,
\[
 |\mathscr J_{\rm fix}(PW)|
 \ll_\eta
 {q\over J}{uJ\over q}D X^\eta
 \ll_\eta DuX^\eta.
\tag{R23}
\]
Thus the \(q/J\) factor is explicitly paid and exactly cancels the
projective \(J/q\) density.  It is not hidden in an epsilon loss.

For the recomputed masked packet, the accepted Round-191 terminal and
isolated Fejer projections remain positive-deletion stable:
\[
 |\mathscr J_{\rm terminal,fix}(PW)|
 +|\mathscr J_{\rm Fejer,fix}(PW)|
 \ll_\eta\kappa uX^\eta.
\tag{R24}
\]
The inverse-small term has no row in the Round-192 core: it is empty
when \(T=0\), and (R9) puts every \(T\ge1\) core row strictly beyond
its range.  Finally, \(I-P_A\) is a row indicator.  Therefore
\[
\begin{aligned}
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(PW)|
 &\ll_\eta(D+\kappa)uX^\eta\\
 &\ll_\eta\kappa uX^\eta
 \le Q\mathfrak m\kappa uX^\eta
 \qquad(\kappa\ge D).
\end{aligned}
\tag{R25}
\]
Choosing the fresh endpoint allowance \(\eta<\varepsilon\) proves
(R1).  The argument is an absolute estimate for one joint complex packet,
not two separately normed orientation estimates.

### 3.3 Exact masked-operator passage

Let \(t+\nu_\omega(h)\) be the transported predecessor of a common
current site.  With
\[
 P_h=P(x_{\omega,v,h,t}),\qquad
 P_-^{\rm tr}
 =P(x_{\omega,v,h-1,t+\nu_\omega(h)}),
\tag{R26}
\]
the exact identity is
\[
\begin{aligned}
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 &=P_h(B_h-\chi B_-^{\rm tr})\\
 &\quad+\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\end{aligned}
\tag{R27}
\]
The second line is the physical-mask commutator.  It remains in the new
core, together with affine births and deaths, carries, unequal endpoint
translations, endpoint zero extensions, phase changes, cells, and
crossings.  Equation (R20) bounds these terms collectively; none is
silently assigned to an old safe projection.

The accepted deletion mechanisms remain valid on \(PW\):

1. Round 187 uses positive atom counts and the complete Fourier
   \(\ell^1\) mass.
2. Round 188 uses the exact lift weight and a positive atom count.
3. Round 189 uses projective residue sparsity and positive row counting.
4. Round 191 performs exact Abel inversion on the newly masked,
   zero-extended row; its outer terminal and isolated Fejer pieces retain
   their positive bounds, while every new interior mask jump stays in the
   remainder.
5. Round 192 applies a row indicator and positive divisor/row counting;
   selected terminal and Fejer rows are replaced, not duplicated.

This is exactly the deletion-stability interface already certified in the
Round-193 kernel.  It applies to \(P\) because \(P\) is a coordinatewise
physical mask independent of the later Fourier mode.

### 3.4 Outer \(L^2\) power

At outer level one first uses (R18) directly on the physical source.
The literal atom bound \(O_\eta(X^\eta)\) gives
\[
 |\mathscr H_Y^\sigma(PW)|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{R28}
\]
No Abel denominator is introduced in (R28); the source is counted before
Fourier expansion.  Complete Fourier coefficient mass and the finite
literal event partition are at most polylogarithmic and, in any case,
are unnecessary for this direct source estimate.

Rerunning the safe operators as in Section 3.3 gives
\[
 |\mathscr S_{\le192,Y,Q}^\sigma(PW)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{R29}
\]
By the exact accepted linear identity
\[
 \mathscr H_Y^\sigma(PW)
 =\mathscr S_{\le192,Y,Q}^\sigma(PW)
  +\mathscr R_{{\rm core},Y,Q}^\sigma(PW),
\tag{R30}
\]
(R28)--(R30) prove (R2).  The argument is uniform in the dyadic height
block, retains the \(T=0\) and \(T\ge1\) conventions, and takes only the
one inherited outer real part.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the large-\(\kappa\) conclusions
(R1)--(R2).

The first genuinely unproved estimate is outside the proved sector:
\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma
        (P_{2,<D}W)\right|
 \stackrel{?}{\ll}
 Q\mathfrak m\kappa uX^\varepsilon.
\tag{R31}
\]
The one-close physical count reduces its positive fixed-packet capacity
to \(YuX^\varepsilon\), still leaving
\[
 {Y\over Q\mathfrak m\kappa}.
\tag{R32}
\]
Neither nonblind report proves the coefficient-sensitive cross-row
four-block Gram estimate needed to recover (R32), and the candidate does
not claim otherwise.

For avoidance of two possible misreadings:

- A termwise Abel estimate cannot be charged merely to
  \(X^\varepsilon\); it must pay \(q/J\), as done in (R21)--(R23).
- In the mask identity, the old mask is evaluated at the transported
  predecessor, as made explicit in (R26)--(R27).

With these exact interpretations, no repair to the candidate's
mathematical conclusion is required.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| exact physical \(P_2\) mask and split | PASS.  Equations (R7)--(R8) are imposed before Fourier and form one exact complement. |
| plus-orientation count | PASS.  \(w\) has \(O(D)\) choices and \(S\) has \(O(1)\), by (R12)--(R13). |
| minus-orientation count | PASS.  \(S\) has \(O(D)\) choices and \(w\) has \(O(1)\), by (R15)--(R16). |
| primitive multiplicity and shell endpoints | PASS.  The chart is multiplicity one, \(g=O(1)\), and \(U,v\ll1+L/\kappa\). |
| no hidden height factor | PASS.  The determinant fixes \(h\), and the full Fejer range is counted. |
| fixed-packet physical row count | PASS.  There are \(O(D)\) masked atoms per literal row over the whole block. |
| anchor/Abel \(q/J\) ledger | PASS.  Equations (R21)--(R23) pay \(q/J\) and cancel the \(J/q\) row density exactly. |
| literal endpoint weights | PASS.  Only the accepted \(O_\eta(X^\eta)\) pointwise bound and a fresh epsilon split are used. |
| masked height difference | PASS.  Equation (R27) retains the commutator, births, deaths, and zero extensions. |
| Round-187--192 deletion stability | PASS.  Each accepted proof is rerun on the physical parent mask by its original positive or exact-linear mechanism. |
| \(T=0\) branch | PASS.  \(P_A=0\), inverse-small is empty, and the whole inherited remainder remains. |
| \(T\ge1\) branch | PASS.  All simultaneous strict covectors and the \(|\rho|\) lower bound remain row predicates. |
| one joint orientation aggregate | PASS.  Both orientations are counted jointly up to an absolute factor; no separate norm is used. |
| fixed target | PASS.  \((D+\kappa)u\ll\kappa u\le Q\mathfrak m\kappa u\) on \(\kappa\ge D\). |
| outer \(L^2\) ledger | PASS.  The source and safe aggregate are each \(O(L^2X^\varepsilon)\); no \(Y,q,J,U\), or \(\mathfrak m\) power is hidden. |
| exact complement and scope | PASS.  \(P_{2,<D}\) stays open; no complete \(P_2\), owner, parent, bridge, theorem, or exponent is promoted. |
| computation policy | PASS.  No numerical or symbolic computation was used. |

## 6. Exact dependencies and artifacts used

The reviewed candidate and the two nonblind reports were:

1. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md —
   c2cb78666e5396260a6a1951aa77f37356190bad44b423d4f4779b7c744e3819;
2. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reports/literal_p2_determinant_fibre_vector_attack.md —
   c617c18c959792622e3df9fe3eb06f47ba61c6948be77f8617c83bda96302879;
3. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reports/p2_gram_diagonal_collision_hostile_audit.md —
   52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb.

The accepted Round-187--193 dependency chain was checked at:

4. proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md —
   a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2;
5. proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md —
   ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a;
6. proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md —
   31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58;
7. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md —
   7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2;
8. proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md —
   301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325;
9. proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md —
   470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83;
10. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md —
    4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.

Protocol and authoritative context were:

11. protocol.md —
    f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a;
12. state/proof_obligations.yml —
    815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89;
13. state/active_campaign.yml —
    7a6762a4030410bce88305638367821bc9280dc2f88f1b201e3403594e41e00d.

The blind Round-195 report was not used to prove or review the positive
large-\(\kappa\) estimate.  No web source, computation, unlisted
Round-195 report, or post-candidate state mutation was used.

## 7. Recommended state effect

**Pass the candidate through this count/power/masked-operator seam.**
It may advance to the remaining literal-Gram/no-go, blind post-unmask,
candidate-kernel consistency, provenance/scope, and graph-replay reviews.

After all required independent gates, create at most the subordinate
proved-internal strict-sector lemma for \(P_{2,\ge D_L}\), with
\(P_{2,<D_L}\) recorded as its exact open complement.  Do not change the
status of the complete \(P_2\) remainder, the complete original-\(t=1\)
range, the hard-M1 owner, M9-M1, M9, either bridge, the Gauss-circle
target, or any exponent on this review.
