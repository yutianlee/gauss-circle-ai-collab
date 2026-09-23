# Round 187 final durable-kernel power and owner-scope review

## 1. Result / verdict

**Verdict: GREEN.**

The durable kernel was frozen before review at SHA-256

b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74,

which equals the expected hash. A hostile replay of (K187.8)--(K187.27)
found no missing \(L,Y,\kappa,g,U,q,Q\), or \(X\) factor, no overlap or
gap in the Fourier partition, no inward movement of the unique real
part, and no illicit use of a deletion-free or arbitrary coefficient.

The theorem proved by the kernel is only the exact transformed
decomposition, the absolute target-safe packet (K187.9), the positive
capacity bound (K187.10), and the centered/energy self-return controls.
The one-sided estimate (K187.11) is not proved. The kernel is suitable
for durable proved-internal status with exactly that strict scope.

## 2. Exact claim and hypotheses

Fix \(X\ge2\), a literal middle or lower residual hard-M1 shell
\(L\ge2\), \(\sigma\in\{+1,-1\}\), and fixed \(B>0\). Put

\[
 R_0=\lceil L\rceil,\qquad
 Q=H_B=\lfloor(\log(2X))^B\rfloor,
\]

and take a nonempty dyadic block \(Y<h\le2Y\) with \(Y>Q\). The outer
carrier is exactly

\[
 \kappa,g,h,U,v>0,\qquad
 \kappa,g,U\ {\rm odd},\qquad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0.
\tag{187.F1}
\]

For each orientation,

\[
 A_{\mathfrak f,\omega}^{\sigma}
 =\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
\]

uses the canonical anchor and positive affine set from the accepted
Round-185 kernel. Every residual selector, squarefree and
allocation-coprimality deletion, profile, floor, star, half-weight, hard
sample, crossing, endpoint, conjugation, Fejer factor, square-root
phase, sign, and zero extension remains inside \(B\).

The exact claim reviewed is

\[
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma+
          \mathscr P_{Y,\le Q}^\sigma+
          \mathscr L_{Y,Q}^{>,\sigma}+
          \mathscr R_{Y,Q}^\sigma\},
\tag{187.F2}
\]

\[
 |\mathscr U_{1,Y}^\sigma|
 +|\mathscr P_{Y,\le Q}^\sigma|
 +|\mathscr L_{Y,Q}^{>,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon,
\tag{187.F3}
\]

\[
 |\mathscr R_{Y,Q}^\sigma|
 \ll_\varepsilon YL^2X^\varepsilon,
\tag{187.F4}
\]

with \(\Re\mathscr R_{Y,Q}^\sigma\ll L^2X^\varepsilon\) explicitly
open. The centered identities and energy controls in
(K187.23)--(K187.27) are auxiliary exact statements, not estimates of
that open real part.

## 3. Hostile proof replay

### 3.1 Exact complement and one outer real part

For \(U>1\), let \(b=[\bar vh]_U\). The primitive conditions make \(b\)
a unit. The plus anchor is \(S_{0,+}=b\), and the minus anchor is
\(S_{0,-}=[-b]_U=U-b\), so the two anchor factors are exactly
\(E_U(b)\) and \(E_U(-b)\). For \(U=1\), both prescribed bases have
\(S_0=0\) and are correctly kept outside the modular expansion.

Finite Fourier inversion gives

\[
 E_U(b)=\sum_{k\bmod U}c_U(k)e(kb/U),
 \qquad c_U(0)=1/U.
\]

Because \(Q\ge1\), the three mode conditions are disjoint and
exhaustive:

\[
\begin{array}{ll}
q_U(k)\le Q,&\mathcal K_{\le Q}(U),\\
q_U(k)>Q\ \text{and}\ 
 [\,U\le4Q\ \text{or}\ 0<|k|_U\le Q\,],
 &\mathcal K_{\rm edge}(U),\\
U>4Q,\ q_U(k)>Q,\ |k|_U>Q,
 &\mathcal K_{\rm high}(U).
\end{array}
\tag{187.F5}
\]

The zero mode occurs only in the first line. In the last line it is
therefore harmless that the representative is restricted to
\(1\le k<U\). Thus (K187.6) is the exact raw Fourier complement of
(K187.4)--(K187.5), and (K187.8) neither loses nor duplicates a mode,
orientation, primitive row, or affine site.

The expansion changes only the scalar anchor. The factor \((-1)^t\),
the oriented positivity restriction, and the entire literal endpoint
product stay inside \(A_{\mathfrak f,\omega}^{\sigma}\). Equation
(K187.8) has one real part outside every sum. Equation (K187.11) keeps
the same placement. Absolute values are applied only to separately
proved safe packets and to the positive-capacity control (K187.10).
They are never inserted into the open remainder.

Finally, if \(\mathscr T\) denotes the sum of the three safe packets,
then

\[
 \mathcal S_Y^\sigma=\Re(\mathscr T+\mathscr R),
 \qquad |\mathscr T|\ll L^2X^\varepsilon.
\]

Hence the one-sided target for \(\mathcal S_Y^\sigma\) and the
one-sided target for \(\Re\mathscr R\) imply each other after changing
the constant. No lower estimate for a negative dyadic real part is
needed. This verifies the exact-complement assertion following
(K187.10).

### 3.2 Fourier and conductor normalization

For odd \(U\),

\[
 \widehat E_U(k)
 =\sum_{a=0}^{U-1}(-1)^ae(-ka/U)
 ={2\over1+e(-k/U)}.
\]

Therefore

\[
 c_U(k)={e(k/(2U))\over U\cos(\pi k/U)},\qquad
 \sum_k|c_U(k)|\ll\log(2U),\qquad
 \sum_k|c_U(k)|^2=1.
\]

For \(q=U/(k,U)\), the representation

\[
 k={U\over q}a,\qquad q\mid U,\qquad a\in\mathbb U(q)
\]

is unique, including \(k=0\leftrightarrow(q,a)=(1,0)\). Direct
substitution gives

\[
 c_U(k)={q\over U}c_q(a),\qquad
 e(\epsilon_\omega k\bar vh/U)
 =e(\epsilon_\omega a\bar vh/q).
\]

Thus (K187.12)--(K187.16) carry the exact mean, exact conductor, and
orientation sign. There is no missing factor \(q/U\), no second
conductor multiplicity, and no rearrangement issue.

### 3.3 Power ledger for (K187.9)

Put \(u=gU\). On a live literal endpoint,

\[
 \kappa u\asymp L,\qquad \kappa v\asymp L,
\tag{187.F6}
\]

and \(2\kappa gh<R_0\) gives \(h\ll U\). At fixed
\((\kappa,u,U)\), there are \(O(U)\) heights,
\(O(L/\kappa)\) choices of \(v\), and \(O(\kappa)\) affine sites per
row. Both orientations therefore contain \(O(UL)\) atoms. Equivalently,
at fixed \((\kappa,g,h,U)\), the \(v,t,\omega\) mass is
\(O_\varepsilon(LX^\eta)\), for a fresh exponent \(\eta\).

The restored ledger is:

| Packet | Fourier mass at fixed \(U\) | Fixed \((\kappa,u,U)\) cost | Summed cost |
|---|---:|---:|---:|
| \(U=1\) | \(1\) | \(O(LX^\eta)\) | \(O(L^2X^\varepsilon)\) |
| exact \(q\le Q\) | \(O((q/U)\log(2q))\) | \(O(Lq\log(2q)X^\eta)\) | \(O(L^2Q\log^{O(1)}(2LQ)X^\eta)\) |
| \(q>Q,\ U\le4Q\) | \(O(\log(2U))\) | \(O(LU\log(2U)X^\eta)\) | \(O(L^2Q\log^{O(1)}(2LQ)X^\eta)\) |
| \(U>4Q,\ 0<|k|_U\le Q\) | \(O(Q/U)\) | \(O(LQX^\eta)\) | \(O(L^2Q\log^{O(1)}(2L)X^\eta)\) |

For the first row, (K187.17)--(K187.19) give \(L\) per fixed
\((\kappa,g,h)\) and \(O(L\log L)\) outer triples. For the exact
conductor row,

\[
 {q\over U}\sum_{a\in\mathbb U(q)}|c_q(a)|
 \ll {q\over U}\log(2q),
\]

so summing \(q\mid U\mid u\), \(q\le Q\), costs at most

\[
 LQ\log(2Q)X^\eta
 \sum_{\kappa u\asymp L}\tau(u)^2,
\]

which is (K187.21). For \(U\le4Q\), the full Fourier mass and
\(UL\) atom count give the third row. For \(U>4Q\),
\[
 \sum_{0<|k|_U\le Q}|c_U(k)|\ll Q/U
\]
cancels the \(U\) in the atom count and gives the fourth row.

All divisor powers and \(Q=(\log(2X))^B+O(1)\) are absorbed only after
starting with \(\eta<\varepsilon\). On nonzero literal hard-top support
\(L\ll X^{1/4}\); off that inherited range the coefficient is zero.
Thus logarithms of \(L\) are also lawfully rebudgeted. No power of
\(Y\) is suppressed. This proves exactly (K187.9).

### 3.4 Positive remainder ledger for (K187.10)

At fixed \((\kappa,g,h,U)\), use (K187.17) and the full
\(O(\log(2U))\) Fourier mass. Summing
\[
 U\ll {L\over\kappa g}
\]
costs
\[
 O_\varepsilon\!\left(
 {L^2\log(2L)X^\eta\over\kappa g}\right).
\]
Consequently
\[
 |\mathscr R_{Y,Q}^{\sigma}|
 \ll L^2\log(2L)X^\eta
 \sum_{Y<h\le2Y}
 \sum_{\kappa g\ll L/h}{1\over\kappa g}.
\]
For \(A\ge1\),
\[
 \sum_{\kappa g\le A}{1\over\kappa g}\ll\log^2(2A),
\]
so the \(O(Y)\) heights give
\[
 |\mathscr R_{Y,Q}^{\sigma}|
 \ll_\varepsilon YL^2X^\varepsilon.
\]

No \(U\), \(\kappa\), \(g\), endpoint, or divisor multiplicity is
missing. The high-mode restrictions only reduce this positive sum.
Most importantly, the factor \(Y\) remains visible; (K187.10) does not
masquerade as (K187.11).

### 3.5 Centered trace, prime self-return, and high energy

For a unit \(b\bmod q\), primitive-frequency inversion gives

\[
 K_q(b)={1\over q}\sum_{d\mid q}\mu(q/d)dE_d(b).
\tag{187.F7}
\]

Every relevant divisor is odd. For \(d>1\),
\(E_d(-b)=-E_d(b)\), while the \(d=1\) term contributes \(1\).
Adding (187.F7) at \(b\) and \(-b\) proves

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q}.
\]

Thus \(K_q^\circ(-b)=-K_q^\circ(b)\). Expanding
\(K_q=K_q^\circ+\mu(q)/q\) in
\[
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b)
\]
leaves the trace
\[
 {1\over U}\sum_{q\mid U}\mu(q)=0
\]
for \(U>1\). This proves (K187.25) before the outer real part:
\[
 E_U(b)A_+ +E_U(-b)A_-
 =\sum_{\substack{q\mid U\\q>1}}{q\over U}
 K_q^\circ(b)(A_+-A_-).
\]

For prime \(U=p\),
\[
 E_p(b)=1/p+K_p(b),\qquad
 K_p^\circ(b)=K_p(b)+1/p=E_p(b),
\]
so the sole centered high conductor is literally the original
prime-\(U\) orientation block. This validates (K187.26) as a
self-return, not a saving.

For odd \(U>4Q\), the two modes \(k=(U\pm1)/2\) have
\[
 q_U(k)=U>Q,\qquad |k|_U=(U-1)/2>Q,
\]
and therefore lie in \(\mathcal K_{\rm high}(U)\). Their magnitudes are
\[
 |c_U(k)|={1\over U\sin(\pi/(2U))}\ge2/\pi.
\]
Hence the retained vector has energy at least \(8/\pi^2\), proving
(K187.27). Positive Fourier, Poisson, conductor, or alias energy cannot
supply a hidden \(U^{-1/2}\), much less the full missing factor \(Y\).

### 3.6 Literal deletions and false controls

The positive atom counts may ignore deletion masks only because deleting
or downweighting atoms cannot enlarge an absolute upper count. No
identity pairs deleted and undeleted endpoints: the masks, both endpoint
allocations, conjugation, profiles, crossings, and phases remain inside
the same \(B\)'s throughout (K187.8)--(K187.27).

An adversarial bounded weight can align with the anchor, affine parity,
and phase and attain the positive carrier capacity. This falsifies any
coefficient-uniform theorem based only on the Fourier normalization.
It does not give nonvanishing, density, or lower mass for the actual
Vaaler/\(\chi_4\) endpoint coefficient. The kernel states this
quarantine explicitly and never infers failure of (K187.11).

## 4. First doubtful or unproved step

No doubtful step remains inside the claimed durable reduction. The
first unproved relation is exactly

\[
 \boxed{\Re\mathscr R_{Y,Q}^{\sigma}
        \ll_{B,\varepsilon}L^2X^\varepsilon.}
\]

It must recover the complete factor \(Y\) from a jointly signed
property of the actual literal amplitude in \((h,v,t,k)\) before any
positive recombination. Neither the exact trace (K187.25), prime
self-return, constant high-mode energy, raw orientation antisymmetry,
nor the deletion controls prove this estimate.

## 5. Controls and outcomes

| Required control | Outcome |
|---|---|
| frozen durable-kernel hash | **PASS.** It equals the expected b9119e5d... hash. |
| (K187.8) exact complement | **PASS.** The three mode sets and separate \(U=1\) convention are disjoint and exhaustive. |
| one outer real part | **PASS.** It remains outside both orientations, all heights, modes, rows, affine sites, selectors, endpoints, and phases. |
| (K187.9) powers | **PASS.** The \(U=1\), low-conductor, small-\(U\), and edge-mode ledgers are each \(O(L^2X^\varepsilon)\) after only polylogarithmic rebudgeting. |
| (K187.10) powers | **PASS.** Positive recombination returns \(YL^2X^\varepsilon\), with the full \(Y\) explicitly retained. |
| conductor trace and (K187.25) | **PASS.** The trace is \(2\mu(q)/q\) and cancels only in the complete divisor sum for \(U>1\). |
| prime self-return | **PASS.** \(K_p^\circ(b)=E_p(b)\). |
| high-mode energy | **PASS.** The two primitive central modes give at least \(8/\pi^2\). |
| literal deletions and endpoints | **PASS.** They remain inside the zero-extended amplitudes and are used only monotonically in absolute counts. |
| mechanism/no-lower-mass quarantine | **PASS.** Adversarial capacity is not asserted realizable by the literal coefficient. |
| first open relation | **PASS.** (K187.11), not an absolute or separate-orientation surrogate, is identified as first open. |
| \(t=1\)-only scope | **PASS.** Even success at (K187.11) closes only the exact original-\(t=1\) residual through the Round-184/185 connectors. |
| exponent quarantine | **PASS.** Every \(t\ge2\) and large-\(G\) complement, both M1 parents, GAR, all M2 parents, endpoint uniformity, M9, both bridges, the quarter theorem, and every exponent remain open. |

A bounded diagnostic over every odd \(3\le U\le101\), every unit
residue, and \(1\le Q\le5\) tested Fourier inversion, the three-way
partition, Parseval, the centered trace, and prime self-return. The
largest floating error was below \(8\times10^{-14}\). This was
diagnostic only; the exact derivations above are the proof.

## 6. Dependencies and hashes

The reviewed artifacts and hashes are:

1. proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md  
   b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74
2. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md  
   4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160
3. rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md  
   c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89
4. rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/power_literal_scope_self_return_seam_review.md  
   470737a35629b58ae82753f67ce12f26c449619a6e8a6bdc4ea17d2642562d7d
5. rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/power_literal_scope_post_tex_repair_verification.md  
   52c2397a88577001fe54c1541a5c831e89e29522320bdefc4ce9c4b1c37b57f8
6. state/proof_obligations.yml  
   d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a
7. state/active_campaign.yml  
   aadf701b1725cdd0004bb29e1fc625754e391e5475130df3a08a2a2e18d761d3
8. protocol.md  
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a

No external theorem or web source was used. The finite numerical replay
is diagnostic only.

## 7. Recommended state effect

Accept the durable kernel as GREEN evidence for the proved-internal
node M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction,
limited to (K187.8)--(K187.10) and the exact self-return controls
(K187.23)--(K187.27). Retain (K187.11) as the first open signed
estimate.

Do not promote the complete high-height target, the complete
original-\(t=1\) residual, the hard small-\(t\) owner, either M1 parent,
GAR, any M2 parent, endpoint uniformity, M9, a bridge, the quarter
target, or any exponent. This review authorizes no direct graph or
state edit.
