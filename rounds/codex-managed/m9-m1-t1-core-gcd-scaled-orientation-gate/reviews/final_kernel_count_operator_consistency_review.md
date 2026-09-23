# Round 193 final kernel count/operator consistency review

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Durable kernel:
  `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`
- Expected SHA-256:
  `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`
- Observed SHA-256:
  `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`
- Formal candidate SHA-256 recorded by the kernel:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Status: terminal durable-kernel review; no shared-state edit

## 1. Result: PASS

**Verdict: PASS.**  The durable kernel has the exact mathematical body
of the terminal Round-193 candidate.  Sections 1--5 are byte-for-byte
identical; their common body SHA-256 is
`c976c976bdfb0c5f4a97a3a77043ecc96a2ead64748da3fd5139fb94723aa532`.
The count, physical-mask operator, deletion-stability scope, exact
Round-192 \(T\)-branches, first-failure complement, and
\(1\le D\le L\) boundary all recheck.  The kernel-only changes are title
and lifecycle metadata, rooted diagnostic paths, and proof-state-boundary
wording.  None changes a formula, hypothesis, conclusion, dependency
type, or owner scope.

## 2. Exact statement and hypotheses verified

The reviewed theorem remains the strict physical double-close sector

\[
 P_{\rm cl}=mathbf1_{|d-gm|\le D_L}
              \mathbf1_{|d'-gm'|\le D_L},
 \qquad g=(d,d'),\qquad D_L=\lceil\sqrt L\rceil,
\]

on one nonempty hard-M1 shell \(L\ge2\), one dyadic high-height block,
both opposing orientations, and the exact inherited Round-192 core.
The operator notation is still

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 =\mathscr R_{\rm core}(P_{\rm cl}W),
\]

so the mask acts on free physical atoms before Fourier expansion and
height differencing.  The theorem conclusion remains only

\[
 |\mathscr R_{{\rm core},Y,Q}^{\sigma}[P_{\rm cl}]|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\]

Neither first-failure complement, the complete rho-large remainder, nor
any parent theorem is asserted safe.  The subsidiary \((m,m')=1\),
\(r\equiv2\pmod4\) involution remains explicitly unnecessary for this
absolute estimate.

## 3. Proof and consistency derivation

### 3.1 Exact candidate-to-kernel body comparison

An exact file comparison gives no difference from `## 1. Statement`
through the end of `## 5. Subsidiary scaled-orientation algebra`.
Consequently every displayed formula (193.C1)--(193.C31), including
(193.C16a), (193.C19a)--(193.C19b), (193.C28a)--(193.C28b), and its
surrounding hypotheses is unchanged.

The complete file differences are confined to:

1. replacing the formal-candidate title by the durable-kernel title;
2. replacing candidate-status metadata by the exact formal-candidate
   hash and kernel lifecycle status;
3. rooting the two diagnostic-control paths at the campaign directory;
4. renaming Section 7 from a proposal to a proof-state boundary and
   changing its introductory lifecycle wording; and
5. changing “proposed terminal label” to “Round-193 terminal label.”

The four state-effect bullets themselves are unchanged.  These edits do
not occur inside the mathematical body and do not widen its conclusion.

### 3.2 Count and every \((+1)\) term

From (193.C11), with

\[
 A_0=\kappa(U-v)-2w,qquad
 B_0=\kappa(U-v)+2S,
\]

the bounds \(|A_0|,|B_0|\le D_L/g\) give

\[
 S+w\le D_L/g,qquad
 |\kappa(U-v)|\le3D_L/g.
\]

The lower close relation, \(d/m<16\), and \(m\ge cL\) give uniformly
for all \(L\ge2\)

\[
 1\le g\le16+c^{-1}D_L/L\le16+c^{-1}\sqrt2.
\]

Thus the \(g\)-sum is fixed.  For fixed
\((\kappa,g,U,v,w)\), (193.C10) gives

\[
 {Uw\over v}<S<{Uw\over v}+{R_0\over2\kappa gv};
\]

because \(\kappa v\asymp L\), this contains \(O(1)\) integers.  The
remaining choice count, including all singleton and sub-unit cases, is

\[
 (1+L/\kappa)(1+D_L/\kappa)(1+D_L).
\]

Writing \(D=D_L\), the complete expansion is

\[
\begin{aligned}
 &\sum_{\kappa\ll L}(1+L/\kappa)(1+D/\kappa)(1+D)\\
 &\quad=(1+D)\sum_{\kappa\ll L}
 \left(1+{L+D\over\kappa}+{LD\over\kappa^2}\right)\\
 &\quad\ll(1+D)\{L+L\log(2L)+D\log(2L)+LD\}.
\end{aligned}
\]

After expanding \((1+D)\), the eight terms
\(L,LD,L\log(2L),LD\log(2L),D\log(2L),D^2\log(2L),LD,LD^2\)
are all covered by \(LD\log(2L)+LD^2\) for
\(1\le D=D_L\le L\).  Hence (193.C16)--(193.C18) retain the exact
\(O(L^2X^\varepsilon)\) power.  The minus orientation is the same
determinant count, and \(h\) is determined by \((U,v,S,w)\), so no
\(Y\), Fourier-copy, or lift multiplicity is introduced.

### 3.3 Affine-site mask operator and deletion-stability scope

The kernel forms the actual masked zero-extended row

\[
 W^P_\omega(h)=\sum_{t\in I_\omega(h)}
 P_\omega(h,t)(-1)^tB_\omega(h,t)
\]

before applying \(\Delta^-\).  On a transported common site, direct
expansion of (193.C19b) gives

\[
\begin{aligned}
 &P_hB_h-\chi P_hB_{h-1}
 +\chi P_hB_{h-1}-\chi P_{h-1}B_{h-1}\\
 &\qquad=P_hB_h-\chi P_{h-1}B_{h-1},
\end{aligned}
\]

with every previous-height term evaluated at \(t+\nu_\omega(h)\).
Thus the mask-difference term is exact, and unmatched sites remain the
usual births and deaths.  No scalar commutation of \(P\) with
\(\Delta^-\) is used.

The deletion-stability claim remains limited to the already accepted
safe sources:

1. Round 187: positive atom counts and Fourier \(\ell^1\) mass;
2. Round 188: positive counting with the exact lift weight;
3. Round 189: residue-class sparsity and positive atom counting;
4. Round 191: exact Abel inversion of the deleted zero-extended row,
   with outer terminals and the isolated Fejer term kept in their
   accepted positive bounds and the new interior \(P\)-jump left in the
   core; and
5. Round 192: a row indicator followed by divisor multiplicity and
   positive row counting, with selected terminal/Fejer rows replaced
   rather than duplicated.

Accordingly (193.C20) bounds only
\(\mathscr S_{\le192}(P_{\rm cl}W)\).  Linearity of the unchanged
identity (193.C4) then yields (193.C21).  The kernel does not claim that
an arbitrary post-Abel mask preserves a safe estimate, nor that either
open complement is deletion-safe.

### 3.4 Exact \(T\)-branches

The kernel preserves the signed inverse, fixed \(C_0\), \(A\), and
primitive covector set.  Its branch convention is exact:

- if \(T=0\), \(P_A\) is identically zero and the core is the whole
  inherited Round-191 rho-large remainder before the physical split;
- if \(T\ge1\), every retained core row satisfies simultaneously

\[
 |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1).
\]

The physical mask is applied inside either branch.  At \(T=0\), the
Round-192 safe projector contributes nothing; at \(T\ge1\), its row
selector only deletes rows.  The \(B,C_0,\varepsilon\) dependence is
the same in (193.C7) and (193.C20), and (193.C21) is valid in both
branches.

### 3.5 Exact complement and \(D\)-boundary

Let

\[
 A=\{|d-gm|\le D_L\},\qquad
 B=\{|d'-gm'|\le D_L\}.
\]

Then \(P_{\rm cl}=A\cap B\), \(P_1=A^c\), and
\(P_2=A\cap B^c\).  They are disjoint and exhaustive, so
\(1=P_{\rm cl}+P_1+P_2\) pointwise and (193.C23) follows from the same
masked-input linearity.  The exact order remains lower-far first and
lower-close/upper-far second; only \(P_{\rm cl}\) is proved safe.

For the separate physical-source capacity statement (193.C24), the
range remains exactly \(1\le D\le L\).  In that range

\[
 g\le16+c^{-1}D/L\le16+c^{-1},
\]

and the complete \((1+)\) expansion above gives

\[
 |\mathscr H_Y^\sigma(P_{{\rm cl},D}W)|
 \ll_\eta\{LD\log(2L)+LD^2\}X^\eta.
\]

The endpoints \(D=1\) and \(D=L\) are covered.  At
\(D=L^{1/2+\delta}\), \(0\le\delta\le1/2\), the second term is
\(L^{2+2\delta}\).  The kernel therefore retains the candidate's exact
square-root target boundary and does not overstate (193.C24) as a
general-\(D\) core theorem.

## 4. First doubtful or unproved step

None within the assigned kernel-consistency seam.  The
multiplicity-one physical chart and Round-187--Round-192 safe estimates
remain typed as accepted dependencies; all new Round-193 deductions from
them were re-expanded above.  Kernel promotion has not widened those
inputs or the strict-sector conclusion.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact durable-kernel SHA-256 | **PASS:** `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`. |
| Recorded formal-candidate SHA-256 | **PASS:** exact terminal candidate hash. |
| Candidate/kernel Sections 1--5 comparison | **PASS:** byte-identical; common body hash `c976c976bdfb0c5f4a97a3a77043ecc96a2ead64748da3fd5139fb94723aa532`. |
| Uniform \(g\) and all \((+1)\) terms | **PASS.** |
| Hidden \(Y\), Fourier, or lift multiplicity | **PASS:** none. |
| Affine-site mask commutator | **PASS:** exact transported-coordinate identity. |
| Round-187--Round-192 deletion scope | **PASS:** limited to accepted positive/exact safe ledgers; new \(P\)-jumps remain core. |
| \(T=0/T\ge1\) branches | **PASS:** exact and disjoint. |
| First-failure complement | **PASS:** disjoint, exhaustive, lower-first. |
| \(1\le D\le L\) range and square-root power | **PASS.** |
| Kernel-only title, metadata, path, and Section-7 changes | **PASS:** no mathematical mismatch. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This review used:

1. `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md` at the exact hash above;
2. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md` at SHA-256 `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`, solely for exact body comparison;
3. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`, solely to replay the inherited \(T=0/T\ge1\) interface; and
4. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/final_candidate_count_operator_terminal_verification.md`, used only as the prior seam checklist, not as proof.

The count, commutator, complement, and width calculations were
independently replayed on the durable kernel.

## 7. Recommended state effect

Mark the durable-kernel count/operator consistency seam **PASS** at
SHA-256
`470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`.
No kernel repair is required on this seam.  This review changes no shared
proof state and does not replace the Round-193 State Patch or its
mechanical graph validation.
