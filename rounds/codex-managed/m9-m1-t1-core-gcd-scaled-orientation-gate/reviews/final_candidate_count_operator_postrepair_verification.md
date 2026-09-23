# Round 193 final candidate count/operator post-repair verification

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Candidate: `candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`
- Candidate SHA-256:
  `38646d4dc1826c2475d519f28248a6d9c7b45bbba2f5dcb1f9d3e1da2c124bbf`
- Scope: only the four requested repairs and repair-induced consistency
- Status: independent candidate review; no shared-state edit

## 1. Result: PASS

**Verdict: PASS.**  The repaired candidate now supplies (i) a uniform
all-\(L\) bound for \(g\), (ii) the full expansion of every \((+1)\)
factor in the close-sector count, (iii) the exact affine-site transported
physical-mask commutator, and (iv) the explicit scale range
\(1\le D\le L\).  Direct substitution and expansion reveal no new
mismatch in the adjacent count, operator, complement, or power statements.

## 2. Exact statement and hypotheses verified

The verification is restricted to (193.C13), (193.C16a)--(193.C17),
(193.C19)--(193.C19b), and (193.C24), together with their immediate
interfaces to (193.C6), (193.C20)--(193.C23).  The relevant hypotheses
are

\[
 L\ge2,\qquad D_L=\lceil\sqrt L\rceil,\qquad
 D_L\le2\sqrt L,\qquad m\ge cL,
\]

the inherited lower hard-cone inequality \(d/m<16\), and
\(\kappa\ll L\).  For (193.C24), the width is explicitly restricted to
\(1\le D\le L\).  No condition \((m,m')=1\), restriction
\(r\equiv2\pmod4\), Fourier-mode hypothesis, or dyadic-height
multiplicity is introduced by any repair.

## 3. Verification

### 3.1 Uniform all-\(L\) bound for \(g\)

The lower close inequality gives \(gm\le d+D_L\), hence

\[
 1\le g\le {d\over m}+{D_L\over m}
 \le16+c^{-1}{D_L\over L}
 \le16+c^{-1}\sqrt2=:G_0
 \qquad(L\ge2).
\]

Thus (193.C13) is uniform down to the smallest allowed shell.  The
constant depends only on the fixed literal-shell comparability constant
\(c\); it has no \(X\), \(Y\), \(Q\), or \(B\) dependence.  For the
general width in (193.C24), the same argument gives
\(g\le16+c^{-1}D/L\le16+c^{-1}\), so the fixed finite \(g\)-sum also
remains valid throughout \(1\le D\le L\).

### 3.2 Full \((+1)\) expansion

With \(D=D_L\), the repaired line (193.C16a) is exactly

\[
\begin{aligned}
 &\sum_{\kappa\ll L}(1+L/\kappa)(1+D/\kappa)(1+D)\\
 &\quad=(1+D)\sum_{\kappa\ll L}
 \left(1+{L+D\over\kappa}+{LD\over\kappa^2}\right)\\
 &\quad\ll(1+D)\{L+L\log(2L)+D\log(2L)+LD\}.
\end{aligned}
\]

This includes the large-\(\kappa\) \(O(L)\) tail, both harmonic
single-variable terms, and the \(LD\sum\kappa^{-2}\) term.  Expanding
the outer \((1+D)\) produces

\[
 L,\ LD,\ L\log(2L),\ LD\log(2L),\ D\log(2L),\
 D^2\log(2L),\ LD,\ LD^2.
\]

For \(L\ge2\) and \(1\le D=D_L\le L\), every term is bounded by
\(O(LD\log(2L)+LD^2)\).  Consequently (193.C16) follows without
discarding a small-width or single-choice case.  Since the estimate is
at fixed \((\kappa,g)\) and (193.C13) leaves only \(O(1)\) values of
\(g\), no multiplicity is missing.  At \(D_L\le2\sqrt L\), (193.C17)
has the asserted \(O(L^2)\) power (the smaller term is
\(O(L^{3/2}\log(2L))\)).

### 3.3 Affine-site transported mask commutator

The repair correctly defines the deleted row before differencing,

\[
 W^P_\omega(h)=\sum_{t\in I_\omega(h)}
 P_\omega(h,t)(-1)^tB_\omega(h,t),
 \qquad
 \Delta^-W^P_\omega(h)=W^P_\omega(h)-W^P_\omega(h-1).
\]

On a transported common site, write the previous coordinate as
\(t+\nu_\omega(h)\) and its transported affine sign as \(\chi_\omega(h)\).
Expanding the right side of (193.C19b) gives

\[
 P_hB_h-\chi P_hB_{h-1}
 +\chi P_hB_{h-1}-\chi P_{h-1}B_{h-1}
 =P_hB_h-\chi P_{h-1}B_{h-1},
\]

with every previous-height quantity evaluated at \(t+\nu\).  The middle
terms cancel with the same transported sign; no site is lost or doubled.
The second summand in (193.C19b) is therefore exactly the physical-mask
commutator.  Unmatched current and previous sites remain the stated
births and deaths.  This agrees with (193.C6):
\(\mathscr R_{\rm core}[P]\) is evaluation of the accepted linear
operator on \(PW\), not multiplication of an already formed Abel jump.
The repaired text never invokes the false scalar identity
\(P\Delta W=\Delta(PW)\).

### 3.4 Explicit range \(1\le D\le L\)

In this range the uniform \(g\)-bound above and the same determinant
count yield

\[
 |\mathscr H_Y^\sigma(P_{{\rm cl},D}W)|
 \ll_\eta\{LD\log(2L)+LD^2\}X^\eta,
\]

exactly as stated in (193.C24).  The lower endpoint \(D=1\) is covered
by all displayed \((1+)\) factors; the upper endpoint \(D=L\) keeps
\(g=O(1)\).  Substitution \(D=L^{1/2+\delta}\),
\(0\le\delta\le1/2\), gives \(LD^2=L^{2+2\delta}\), so the stated
square-root target boundary is unchanged.

### 3.5 No repair-induced mismatch

The four edits are mutually consistent.  The all-\(L\) estimate in
(193.C13) supplies precisely the finite \(g\)-sum used in (193.C16a),
and its general-\(D\) version supplies the hypothesis needed by
(193.C24).  The coordinatewise definition (193.C19) preserves the
original carrier and zero extension, while (193.C19b) assigns only the
new interior mask jump to the remainder; it does not alter the accepted
terminal, Fejer, or Farey replacement bookkeeping.  Equations
(193.C22)--(193.C23) still form the same disjoint lower-first
first-failure complement, because the repair changes the transport of
the mask but not its pointwise definition.  No new \(Y\), \(Q\),
Fourier-copy, lift, orientation, or arithmetic-mask factor appears.

## 4. First doubtful or unproved step

None within the assigned post-repair scope.  The first issue identified
by the earlier seam has been removed: (193.C19b) is now a literal
coordinate identity, and the three accompanying count/range hygiene
repairs are uniform at their endpoints.  Claims outside the four named
repairs were not reopened by this verification.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Recompute SHA-256 of the repaired candidate | **PASS:** `38646d4dc1826c2475d519f28248a6d9c7b45bbba2f5dcb1f9d3e1da2c124bbf`. |
| Test the \(g\)-bound at all allowed \(L\), including \(L=2\) | **PASS:** \(D_L/L\le\sqrt2\); no finite-shell exception remains. |
| Expand every factor in (193.C16a) before domination | **PASS:** all eight resulting terms are covered by (193.C16). |
| Expand both sides of the transported identity (193.C19b) | **PASS:** exact cancellation with the same \(\chi_\omega(h)\) and site \(t+\nu\). |
| Check both endpoints \(D=1\) and \(D=L\) in (193.C24) | **PASS:** \((1+)\) terms cover the lower endpoint and \(g=O(1)\) covers the upper endpoint. |
| Replay immediate count/operator/complement interfaces | **PASS:** no repair-induced mismatch found. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This verification used only the repaired candidate

`rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`

at SHA-256
`38646d4dc1826c2475d519f28248a6d9c7b45bbba2f5dcb1f9d3e1da2c124bbf`.
No earlier report or review was used as authority for any conclusion.

## 7. Recommended state effect

Mark the count/operator post-repair seam **PASS**.  The four requested
repairs are discharged and require no further candidate edit.  This
review alone makes no shared proof-state change; promotion remains
conditional on the campaign's other independent gates and a valid
State Patch.
