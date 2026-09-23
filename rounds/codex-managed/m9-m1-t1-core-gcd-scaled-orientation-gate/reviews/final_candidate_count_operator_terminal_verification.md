# Round 193 final candidate count/operator terminal verification

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Candidate: `candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`
- Expected SHA-256:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Observed SHA-256:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Status: terminal independent seam verification; no shared-state edit

## 1. Result: PASS

**Verdict: PASS.**  At the exact candidate hash above, the
multiplicity/count region, every \((+1)\) term, the affine-site physical
mask operator, the lower-first exact complement, and the explicit
\(1\le D\le L\) range are mutually consistent.  The final syntax repair
to (193.C10) changes only a TeX separator; it changes no predicate,
inequality, variable, count, or power.  The later spectral-interface and
provenance clarifications introduce no new count or operator mismatch.

## 2. Exact statement and hypotheses verified

The terminal verification covers (193.C3a)--(193.C4a) only at their
interface with the physical count, then directly rechecks
(193.C5)--(193.C24).  The count uses

\[
 L\ge2,\quad D_L=\lceil\sqrt L\rceil,\quad
 d,m,d',m'\asymp L,\quad m\ge cL,
\]

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,
\]

with \(g=(d,d')\), \(S,w>0\), and
\(0<r=2\kappa gh<R_0\).  The general-width statement is read exactly as
written: (193.C24) is an estimate for the full physical source
\(\mathscr H_Y^\sigma(P_{{\rm cl},D}W)\) when \(1\le D\le L\); it is not
silently enlarged into a general-\(D\) core theorem.  The core theorem
(193.C7) continues to use only \(D_L=\lceil\sqrt L\rceil\).

## 3. Proof and consistency derivation

### 3.1 Count, finite \(g\), and all \((+1)\) terms

The two close conditions are still exactly

\[
 |\kappa(U-v)-2w|\le D_L/g,
 \qquad
 |\kappa(U-v)+2S|\le D_L/g.
\]

Their difference gives \(S+w\le D_L/g\), and either inequality then
gives \(|\kappa(U-v)|\le3D_L/g\).  The lower close inequality and live
cone give, uniformly for every \(L\ge2\),

\[
 1\le g\le {d\over m}+{D_L\over m}
 \le16+c^{-1}{D_L\over L}
 \le16+c^{-1}\sqrt2.
\]

Thus the \(g\)-sum has fixed multiplicity, including the smallest
allowed shell.  For fixed \((\kappa,g,U,v,w)\), the repaired (193.C10)
implies

\[
 {Uw\over v}<S<{Uw\over v}+{R_0\over2\kappa gv}.
\]

Since \(\kappa v=m'\asymp L\) and \(R_0\asymp L\), this interval has
\(O(1)\) integral points.  The remaining choices, with all small cases
retained, are

\[
 O(1+L/\kappa),\qquad O(1+D_L/\kappa),\qquad O(1+D_L).
\]

Writing \(D=D_L\), their complete product sum is

\[
\begin{aligned}
 &\sum_{\kappa\ll L}(1+L/\kappa)(1+D/\kappa)(1+D)\\
 &\quad=(1+D)\sum_{\kappa\ll L}
 \left(1+{L+D\over\kappa}+{LD\over\kappa^2}\right)\\
 &\quad\ll(1+D)\{L+L\log(2L)+D\log(2L)+LD\}.
\end{aligned}
\]

After expanding the outer \((1+D)\), the terms are
\(L,LD,L\log(2L),LD\log(2L),D\log(2L),D^2\log(2L),LD,LD^2\).
For \(1\le D=D_L\le L\), each is covered by
\(O(LD\log(2L)+LD^2)\).  Therefore (193.C16)--(193.C17) still include
the large-\(\kappa\) tail, sub-unit windows, and single-choice cases.
The minus orientation is the same determinant count.  Height is fixed by
\((U,v,S,w)\), so no \(Y\) factor appears.

The added Round-192 notation does not add another \(U\)-sum or Fourier
lift factor.  Its \(U=\mathfrak m q\) is the inherited modulus occurring
in the physical chart (193.C9), while \(\mathfrak m\) is explicitly
distinguished from the physical cofactor \(m\).  Fourier rows are
descendants of the counted physical atoms, and their accepted masses
remain in the safe operator ledger rather than in (193.C16).

### 3.2 Affine-site physical-mask operator

The candidate continues to impose \(P_{\rm cl}\) before Fourier
expansion and height differencing and defines

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 =\mathscr R_{\rm core}(P_{\rm cl}W).
\]

For a fixed row and orientation it forms the actually deleted sequence

\[
 W^P_\omega(h)=\sum_{t\in I_\omega(h)}
 P_\omega(h,t)(-1)^tB_\omega(h,t)
\]

on the original zero-extended carrier and applies
\(\Delta^-W^P_\omega(h)=W^P_\omega(h)-W^P_\omega(h-1)\).  On a common
transported site, expansion of (193.C19b) is

\[
\begin{aligned}
 &P_hB_h-\chi P_hB_{h-1}
 +\chi P_hB_{h-1}-\chi P_{h-1}B_{h-1}\\
 &\qquad=P_hB_h-\chi P_{h-1}B_{h-1},
\end{aligned}
\]

where every previous-height term is evaluated at \(t+\nu_\omega(h)\).
The same transported sign occurs in both middle terms, so they cancel
exactly.  The remaining mask-difference term is the physical commutator;
unmatched sites remain affine births and deaths.  Hence no false
\(P\Delta W=\Delta(PW)\) commutation, dropped site, or doubled terminal
is introduced.  The added fixed parameter \(C_0\) appears consistently
in both (193.C7) and the inherited safe bound (193.C20), so (193.C21)
still proves the masked-core estimate by linearity.

### 3.3 Exact first-failure complement

Let

\[
 A=\{|d-gm|\le D_L\},\qquad
 B=\{|d'-gm'|\le D_L\}.
\]

Then the three physical masks in (193.C5) and (193.C22) are
\(A\cap B\), \(A^c\), and \(A\cap B^c\).  They are pairwise disjoint
and their truth-table union is the whole opposing source.  Thus

\[
 1=P_{\rm cl}+P_1+P_2
\]

pointwise, and (193.C23) follows from the same masked-input linearity
verified above, including the \(T=0\) branch.  The order remains exactly
lower-far first, then lower-close/upper-far.  Neither complement is
claimed safe.

### 3.4 General width and square-root power

For \(1\le D\le L\), the same close inequality gives

\[
 g\le16+c^{-1}D/L\le16+c^{-1},
\]

and the full \((1+)\) expansion above remains valid with \(D\) in place
of \(D_L\).  The condition \(D\le L\) is precisely what absorbs
\(D^2\log(2L)\) into \(LD\log(2L)\).  This proves the stated range

\[
 |\mathscr H_Y^\sigma(P_{{\rm cl},D}W)|
 \ll_\eta\{LD\log(2L)+LD^2\}X^\eta.
\]

Both endpoints pass: \(D=1\) retains the singleton terms and \(D=L\)
retains \(g=O(1)\).  At \(D=L^{1/2+\delta}\),
\(0\le\delta\le1/2\), the second term is exactly
\(L^{2+2\delta}\).  In particular, \(D_L\le2\sqrt L\) gives the
unchanged \(O(L^2)\) theorem power.

### 3.5 Terminal syntax repair and adjacent-formula replay

At the verified hash, (193.C10) is

\[
 h=Sv-Uw>0,\qquad r=2\kappa gh<R_0,\qquad S,w>0.
\]

The terminal repair supplies the missing command marker on the second
separator only.  The determinant \(h\), the Fejer inequality for \(r\),
and the positivity of \(S,w\) are unchanged, so (193.C14) and every
downstream count remain identical.  A literal scan finds zero unescaped
`qquad` and zero unescaped standalone `quad` tokens; display delimiters
are balanced \(40/40\), inline delimiters are balanced \(89/89\), and
all 40 displays retain equation tags.  Replaying (193.C11)--(193.C24)
after this repair yields exactly the formulas above.

The other terminal formalization additions are nonconflicting: the exact
\(T=0/T\ge1\) row predicates only delete spectral rows, the
\(B,C_0,\varepsilon\) constants agree across (193.C7) and (193.C20),
and subsidiary definitions (193.C28a)--(193.C31) do not enter the
primary count/operator proof.

## 4. First doubtful or unproved step

None within the assigned terminal seam.  The physical
multiplicity-one chart remains an explicitly accepted input, and every
new deduction from it used here has been re-expanded at the final hash.
No claim outside the double-close sector has been inferred.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact candidate SHA-256 | **PASS:** `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`. |
| Uniform \(g\) bound, including \(L=2\) | **PASS:** fixed finite \(g\)-set with no bounded-shell exception. |
| Full \((+1)\) expansion | **PASS:** all eight expanded terms are dominated in the stated range. |
| Hidden \(Y\), spectral-\(U\), \(\mathfrak m\), or Fourier-copy factor | **PASS:** no new physical multiplicity. |
| Affine-site mask commutator | **PASS:** direct expansion of (193.C19b) is exact at \(t+\nu\). |
| Masked-core operator semantics | **PASS:** evaluation on \(P_{\rm cl}W\), not post-difference multiplication. |
| Exact complement | **PASS:** \(A\cap B,A^c,A\cap B^c\) are disjoint and exhaustive. |
| Width endpoints \(D=1,D=L\) and square-root power | **PASS.** |
| Terminal (193.C10) syntax repair | **PASS:** separator-only; no mathematical token changed. |
| Immediate adjacent-formula replay | **PASS:** no new count, operator, or power mismatch. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The mathematical verification was performed directly on:

1. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md` at the exact hash above;
2. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/final_candidate_count_operator_postrepair_verification.md`, used only as the prior seam checklist, not as proof;
3. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/final_candidate_provenance_owner_scope_final_verification.md` and `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/final_candidate_provenance_owner_scope_terminal_verification.md`, used only to identify and confirm the terminal separator repair;
4. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`, used only to check the inherited spectral-\(U\) interface; and
5. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reports/gcd_scaled_orientation_sector_attack.md`, used only to cross-check the physical/spectral coordinate naming.

No conclusion was deferred to a sibling verdict.  The displayed count,
commutator, complement, and width calculations were independently replayed.

## 7. Recommended state effect

Mark the terminal count/operator seam **PASS** at candidate SHA-256
`274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`.
No further candidate repair is required on this seam.  This review makes
no shared proof-state change and does not replace the remaining campaign
gates or the mechanically valid State Patch.
