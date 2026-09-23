# Round 187 power, literal-scope, and self-return seam review

## 1. Result / verdict

**Verdict: GREEN, for promotion of the reduction only.**

The candidate was hashed before its contents were inspected.  Its frozen
SHA-256 is

`528c137d7da9dc4de2a892513ee2296ad0c25cbc119692db4575415adac15514`.

The hostile audit of (187.K6), (187.K7), (187.K22), and the asserted
complement found no missing factor or illegal cancellation.  The three
transformed packets in (187.K6) are absolutely target-safe after a fresh
epsilon rebudget; the raw Fourier conditions in (187.K3)--(187.K5) are a
disjoint exhaustive partition; (187.K7) retains exactly the expected
positive (Y)-capacity; and the centered-conductor identity (187.K22)
is an exact rewriting before the one outer real part.  In particular,
the prime-(U) identity (187.K23) and the high-mode energy
(187.K24)--(187.K25) correctly show self-return rather than a saving.

The proved result is therefore the scoped reduction

\[
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma+
          \mathscr P_{Y,\le Q}^\sigma+
          \mathscr L_{Y,Q}^{>,\sigma}+
          \mathscr R_{Y,Q}^\sigma\},
\]

with the first three complex packets absolutely
(O_{B,\varepsilon}(L^2X^\varepsilon)), and with
(\Re\mathscr R_{Y,Q}^\sigma\ll L^2X^\varepsilon) still open.  This
GREEN verdict does **not** promote the dyadic high-height target, the
complete original-(t=1) residual, any small-(t) owner, any M1 parent,
or any exponent.

## 2. Exact claim and hypotheses

Fix (X\ge2), one nonempty literal middle or lower residual hard-M1
shell (L\ge2), (\sigma\in\{+1,-1\}), and fixed (B>0).  Put

\[
 R_0=\lceil L\rceil,\qquad
 Q=H_B=\lfloor(\log(2X))^B\rfloor,
\]

and fix a nonempty dyadic integer-height block (Y<h\le2Y) with
(Y>Q).  The outer variables obey exactly

\[
 \kappa,g,h,U,v>0,\qquad \kappa,g,U\ \mathrm{odd},\qquad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0.
\tag{187.R1}
\]

For each orientation (\omega\in\{+,-\}), retain the canonical anchors,
positive affine set, and literal amplitudes of (K185.30)--(K185.35), and
write

\[
 A_{\mathfrak f,\omega}^\sigma
 =\sum_{t\in I_{\mathfrak f,\omega}}
   (-1)^tB_{\mathfrak f,\omega}^\sigma(t),
 \qquad \mathfrak f=(\kappa,g,h,U,v).
\tag{187.R2}
\]

Thus every residual selector, squarefree and allocation-coprimality
deletion, cone and shell predicate, profile, floor, star, half-weight,
hard sample, crossing, endpoint, conjugation, Fejer factor, square-root
phase, sign, and zero extension remains inside (B).  No transformed
packet replaces those fields by an ambient or selector-blind weight.

For (U>1), put (b=[\bar v h]_U\).  Since (187.R1) makes (b) a
unit, the original complex aggregate before its one real part is

\[
 \widetilde{\mathcal S}_Y^\sigma
 =\mathscr U_{1,Y}^\sigma+
 \sum_{\substack{\mathfrak f:\,Y<h\le2Y\\U>1}}
 \{E_U(b)A_{\mathfrak f,+}^\sigma+
   E_U(-b)A_{\mathfrak f,-}^\sigma\},
 \qquad
 \mathcal S_Y^\sigma=\Re\widetilde{\mathcal S}_Y^\sigma.
\tag{187.R3}
\]

Here (\mathscr U_{1,Y}^\sigma) uses the separate (U=1) bases, for
which both anchor signs are (1).  The claims reviewed are precisely:

1. the exact raw Fourier partition (187.K1)--(187.K5);
2. the absolute packet estimate (187.K6);
3. the positive-capacity estimate (187.K7) and the one-sided
   equivalence (187.K8);
4. the centered identities (187.K20)--(187.K23); and
5. the high-mode energy and mechanism boundary (187.K24)--(187.K25),
   with no literal lower-mass conclusion.

## 3. Checks and proof

### 3.1 Anchors, Fourier normalization, and the exact complement

For odd (U>1), finite geometric summation gives

\[
 \widehat E_U(k)
 =\sum_{a=0}^{U-1}(-1)^ae(-ka/U)
 ={2\over1+e(-k/U)},
\]

so, with (c_U(k)=\widehat E_U(k)/U),

\[
 E_U(b)=\sum_{k\bmod U}c_U(k)e(kb/U),\qquad c_U(0)=1/U.
\tag{187.R4}
\]

The plus base is (S_{0,+}=b), while the minus base is
(S_{0,-}=[-b]_U=U-b).  Therefore their anchor factors are exactly
(E_U(b)) and (E_U(-b)), respectively.  For (U=1), both prescribed
bases have (S_0=0), which verifies (187.K2) without assigning a false
modular inverse or antisymmetry.

For every (k\bmod U), the pair

\[
 q={U\over(k,U)},\qquad k={U\over q}a,\qquad a\in\mathbb U(q)
\tag{187.R5}
\]

is unique, including (k=0\leftrightarrow(q,a)=(1,0)), and

\[
 c_U(k)={q\over U}c_q(a),\qquad
 e(\pm k\bar vh/U)=e(\pm a\bar vh/q).
\tag{187.R6}
\]

The three conditions used for (U>1) are disjoint and exhaustive:

\[
\begin{array}{ll}
 q\le Q, &\text{(187.K3)},\\
 q>Q\ \text{and}\
   [,U\le4Q\ \text{or}\ 0<|k|_U\le Q,],&\text{(187.K4)},\\
 U>4Q,\ q>Q,\ |k|_U>Q,&\text{(187.K5)}.
\end{array}
\tag{187.R7}
\]

The zero mode lies only in the first line.  Hence (187.K5) is the exact
raw Fourier complement of (187.K3)--(187.K4), while (U=1) is retained
separately.  This is a linear spectral decomposition of every original
literal incidence, not a deletion or a claim that Fourier packets are
disjoint physical incidence sets.

Because the sum of the first three packets is absolutely
(O(L^2X^\varepsilon)),

\[
 \mathcal S_Y^\sigma\ll L^2X^\varepsilon
 \quad\Longleftrightarrow\quad
 \Re\mathscr R_{Y,Q}^\sigma\ll L^2X^\varepsilon
\]

up to a change of the implied constant.  Both implications are
one-sided: subtracting the safe packet costs at most its modulus.  No
lower bound on a negative dyadic real part is introduced.

### 3.2 Literal scope and real-part placement

The Fourier expansion acts only on the scalar anchor
((-1)^{S_{0,\omega}}).  The affine parity ((-1)^t), the oriented
positivity set (I_{\mathfrak f,\omega}), and both endpoint amplitudes
remain in (A_{\mathfrak f,\omega}^\sigma).  In particular, taking an
absolute value to price one of the proved packets does not modify the
identity (187.R3) or license a translation of a selector, deletion mask,
profile, endpoint, or phase.

Equations (187.K1), (187.K8), and (187.K22) are all formed as complex
identities before the unique outer (\Re).  The candidate never takes a
modewise real part, a separate positive orientation norm, or a positive
conductor recombination in the open remainder.  The literal deletion
and endpoint scope, and the one-outer-real-part placement, are therefore
unchanged from (K185.36).

### 3.3 Restored (L,Y,\kappa,g,U,q,Q,X) ledger

Put (u=gU).  On a live endpoint the inherited literal support gives

\[
 \kappa u\asymp L,\qquad \kappa v\asymp L.
\tag{187.R8}
\]

At fixed ((\kappa,u,U)), hence fixed (g=u/U), the shift restriction
and (187.R8) imply (h\ll U).  There are (O(L/\kappa)) possible
(v)'s and (O(1+\kappa)=O(\kappa)) live affine sites per oriented
row.  Thus both orientations together contain

\[
 O(UL)\quad\text{atoms over all allowed heights},\qquad
 O(\min(Y,U)L)\quad\text{atoms on }Y<h\le2Y.
\tag{187.R9}
\]

Equivalently, at fixed ((\kappa,g,h,U)), the (v,t,\omega) mass is
(O(LX^\eta)), as in (187.K13).  The bounds

\[
 U\ll {L\over\kappa g},\qquad
 \kappa g\ll {L\over h}
\tag{187.R10}
\]

restore the same powers in the original variables.  Finally,
(\kappa u\asymp L) has (O(L\log(2L))) ordered labels, and (U\mid u)
introduces only displayed divisor-function powers.

The complete packet ledger is:

| Packet | Coefficient mass at fixed (U) | Price at fixed ((\kappa,u,U)) | Global price |
|---|---:|---:|---:|
| (U=1) | (1) | (O(LX^\eta)) | (O_\varepsilon(L^2X^\varepsilon)) |
| exact conductor (q\le Q) | (O((q/U)\log(2q))) | (O(Lq\log(2q)X^\eta)) | (O(L^2Q\log(2Q)X^\eta\,L^{o(1)})) |
| (q>Q, U\le4Q) | (O(\log(2U))) | (O(LU\log(2U)X^\eta)) | (O(L^2Q\log(2Q)X^\eta\,L^{o(1)})) |
| (U>4Q, 0<|k|_U\le Q) | (O(Q/U)) | (O(LQX^\eta)) | (O(L^2QX^\eta\,L^{o(1)})) |
| raw remainder | (O(\log(2U))) | (O(YL\log(2U)X^\eta)) on the dyadic block | (O(YL^2X^\eta\,L^{o(1)})) |

For the exact-conductor row, summing (q\le Q), (q\mid U\mid u),
costs at most

\[
 LQ\log(2Q)X^\eta
 \sum_{\kappa u\asymp L}\tau(u)^2,
\]

which is (187.K18).  For (U\le4Q), (187.R9) and the full Fourier
(\ell^1) mass give the third table row.  For (U>4Q), the elementary
bound

\[
 \sum_{0<|k|_U\le Q}|c_U(k)|\ll Q/U
\]

cancels the (U) in (187.R9), giving the fourth row.  These prove every
term of (187.K6).  For the remainder, using the full
(O(\log(2U))) Fourier mass on the dyadic form of (187.R9) gives the
last row, hence (187.K7).  The restrictions (q>Q), (U>4Q), and
(|k|_U>Q) only decrease this positive bound.

All (Q)-powers are fixed powers of (\log(2X)).  On nonzero literal
hard-top support (L\ll X^{1/4}); otherwise the zero extension makes
the aggregate empty.  Starting the endpoint and divisor estimates with
a fresh exponent (\eta<\varepsilon) therefore absorbs (Q), all
displayed logarithms, and the divisor powers into the final
(X^\varepsilon).  No (Y^\delta) is absorbed: (Y) disappears from
the three safe rows and remains explicitly in (187.K7).

### 3.4 Centered (K_q), orientation trace, and prime self-return

For a unit (b\bmod q), primitive-frequency inversion gives

\[
 K_q(b)={1\over q}\sum_{d\mid q}\mu(q/d)dE_d(b),\qquad
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b).
\tag{187.R11}
\]

All relevant (q) are odd.  For (d>1), a unit (b\bmod d) obeys
(E_d(-b)=-E_d(b)), while the (d=1) contribution equals (1).
Adding the two forms of (187.R11) consequently gives

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q}.
\tag{187.R12}
\]

Thus (K_q^\circ=K_q-\mu(q)/q) is odd in (b).  Since
(\sum_{q\mid U}\mu(q)=0) for (U>1), the trace terms cancel before
any real part, and

\[
 E_U(b)A_+ + E_U(-b)A_-
 =\sum_{\substack{q\mid U\\q>1}}{q\over U}
   K_q^\circ(b)(A_+-A_-).
\]

This proves (187.K22) exactly.  If (U=p) is prime, then
(E_p(b)=1/p+K_p(b)) and (\mu(p)=-1), so

\[
 K_p^\circ(b)=K_p(b)+1/p=E_p(b),
\]

which verifies (187.K23): the only centered high conductor is the
original prime-(U) orientation block.  Centering creates no estimate.
This conductor-centered rewriting is distinct from, and does not get
silently identified with, the raw frequency complement (187.K5); both
are exact decompositions of the same full (U>1) aggregate modulo
their stated safe packets.

### 3.5 High-mode energy and mechanism quarantine

For odd (U>4Q), the modes (k=(U\pm1)/2) satisfy

\[
 q_U(k)=U,\qquad |k|_U=(U-1)/2>Q,
\]

so both belong to (187.K5).  Their exact magnitude is

\[
 |c_U(k)|={1\over U\sin(\pi/(2U))}\ge {2\over\pi},
\]

which yields the lower energy (8/\pi^2) in (187.K25).  Full Parseval
also gives (\sum_k|c_U(k)|^2=1).  Consequently Cauchy in frequency,
positive Poisson/alias energy, or positive conductor recombination has
no hidden (U^{-1/2}) gain and cannot remove the (Y) in (187.K7).

The adversarial bounded-amplitude control may align with the anchor,
affine parity, Fourier phase, and endpoint phase and attain the positive
carrier capacity.  This correctly falsifies a coefficient-uniform
mechanism.  The candidate and the hostile report both explicitly state
that such an array need not be the literal Vaaler/(\chi_4) endpoint
product.  Neither the energy lower bound nor the deletion examples are
used as literal nonvanishing, density, lower mass, failure of
(187.K8), or failure of any parent theorem.

## 4. First doubtful or unproved step

There is no doubtful step in the claimed finite Fourier identities or
in the absolute estimates (187.K6)--(187.K7).  The first unproved
relation is exactly

\[
 \boxed{\Re\mathscr R_{Y,Q}^\sigma
        \ll_{B,\varepsilon}L^2X^\varepsilon,}
\]

with (\mathscr R_{Y,Q}^\sigma) defined literally by (187.K5).  It
requires the full factor (Y) before a positive recombination.  The
centered identity (187.K22), raw orientation antisymmetry, and Parseval
do not prove it.  Literal arithmetic deletions, oriented rays, endpoint
allocations, profiles, crossings, and phases provide no stated
translation invariance or bounded-variation estimate in (h,v,t), so
no rowwise Abel or residue completion can be inserted at this seam.

## 5. Controls

| Control | Outcome |
|---|---|
| candidate frozen before review | **PASS.** The pre-inspection hash is recorded in Sections 1 and 6. |
| (U=1) convention | **PASS.** It is separate, has anchor (1), and costs (O(L^2X^\varepsilon)). |
| inverse-residue Fourier normalization | **PASS.** The nonzero (1/U) zero mode, exact conductor scaling, (\ell^1), and (\ell^2) powers are retained. |
| exact raw complement | **PASS.** Conditions (187.R7) partition every (U>1) mode once; (U=1) is neither omitted nor duplicated. |
| (L,Y,\kappa,g,U,q,Q,X) powers | **PASS.** The ledger in Section 3.3 reproduces (187.K6) and (187.K7); the only surviving power loss is the explicit (Y) in the open remainder. |
| epsilon rebudgeting | **PASS.** A fresh exponent absorbs only polylogarithms and divisor powers on the inherited live hard-top range; no fixed positive power of (Y) is absorbed. |
| one outer real part | **PASS.** All decompositions and (187.K22) are complex identities before the unique outer (\Re); moduli occur only on proved safe packets or positive-capacity controls. |
| literal deletion and endpoint scope | **PASS.** Every selector, arithmetic mask, profile, floor, star, half-weight, hard sample, crossing, endpoint, phase, conjugation, and zero extension remains inside (B). |
| centered (K_q) identities | **PASS.** The trace is exactly (2\mu(q)/q), and it cancels only after the complete divisor sum for (U>1). |
| prime-(U) self-return | **PASS.** (K_p^\circ(b)=E_p(b)); no centered saving is claimed. |
| high-mode energy | **PASS.** Both primitive modes (k=(U\pm1)/2) lie in the remainder and contribute at least (8/\pi^2) of coefficient energy. |
| mechanism and false controls | **PASS.** Positive norms self-return, while adversarial and deletion controls are quarantined from literal lower-mass claims. |
| downstream owner and exponent scope | **PASS.** (187.K8), complete (t=1), every original (t\ge2) and large-(G) near-resonant incidence, both M1 parents, GAR, every M2 parent, endpoint uniformity, M9, both bridges, the quarter theorem, and every exponent remain open. |

A bounded diagnostic checked every odd (3\le U\le101), every unit
residue, and (1\le Q\le5).  Fourier reconstruction, the three-way raw
partition, (187.K12), (187.K21), prime self-return, and Parseval agreed
to at worst (8\times10^{-14}).  This floating-point check is
diagnostic only; the exact derivations above are the proof.

## 6. Dependencies and hashes

The exact artifacts used, with SHA-256 hashes, are:

1. `protocol.md`  
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/proof_obligations.yml`  
   `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`;
3. `state/active_campaign.yml`  
   `aadf701b1725cdd0004bb29e1fc625754e391e5475130df3a08a2a2e18d761d3`;
4. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`  
   `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`;
5. `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md`  
   `528c137d7da9dc4de2a892513ee2296ad0c25cbc119692db4575415adac15514`;
6. `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/deletion_resonance_capacity_audit.md`  
   `b40a6ca8f1c9aec9c12e5f9feab023c1ad44f294069f22f6c3da585086f43252`.

The proof-state hash equals the Round-187 starting graph hash.  No web
source, external theorem, sibling Round-187 claimant report, or
unlisted proof artifact was used.  The bounded finite calculation was
used only as a diagnostic control and supplies no asymptotic evidence.

## 7. Recommended state effect

Promote the candidate as the proved-internal reduction

`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`,

including (187.K1)--(187.K7) and the exact self-return controls
(187.K20)--(187.K25).  Attach it only as inconclusive reduction evidence
for the still-open hard-M1 small-(t) residual owner, and retain
(187.K8) as its first open signed relation.  The mechanism/no-go content
may be recorded under the declared Round-187 exit scope

`high_h_inverse_residue_deletion_capacity_or_self_return_no_go`.

This review authorizes no direct graph edit.  It authorizes no closure
of the original-(t=1) residual, no implication to any (t\ge2) or
near-resonant incidence, no parent or bridge promotion, and no exponent
change.
