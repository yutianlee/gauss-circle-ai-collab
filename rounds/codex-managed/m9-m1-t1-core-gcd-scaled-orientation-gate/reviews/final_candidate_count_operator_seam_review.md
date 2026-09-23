# Round 193 final candidate count/operator seam review

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Reviewed candidate:
  `candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`
- Review scope: primitive multiplicity, all small-variable and (+1)
  terms in (193.C9)--(193.C17), (Y,Q), and Fourier-lift powers,
  masked-core operator semantics, the physical-mask/height-difference
  commutator, deletion stability of every Round-187--Round-192 safe
  source, the exact first-failure complement, and the
  (D_L=\lceil\sqrt L\rceil) power
- Starting graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Status: independent candidate review; no shared-state edit

## 1. Result: REPAIR

**Verdict: REPAIR.**  The theorem, primitive count, square-root power,
safe-source restriction, and exact complement survive.  The first
material issue is the notation in (193.C19): the physical mask depends
on the affine site as well as the height, so (P_hW(h)) cannot literally
mean multiplication of the already summed row (W(h)) by one scalar
(P_h).  The displayed scalar product rule is correct only
coordinatewise, after the current and previous affine sites have been
put in the same transported coordinates.  As written, it can conceal
the (t\mapsto t+\nu_\omega(h)) mask commutator and the unmatched-site
births and deaths.

This is a local formalization defect, not a failed estimate.  Replace
(193.C19) by the transported coordinate identity in Section 4 below.
With that patch, every new (P)-jump remains in the core, while all
accepted safe projections retain their absolute bounds.  Two additional
hygiene repairs should be made at the same time:

1. replace the small-(L) sentence after (193.C13) by a uniform
   (g=O(1)) inequality valid for every (L\ge2); and
2. qualify the general-width statement (193.C24) by (1\le D\le L)
   (or another explicit range in which (g=O(1))).

No change is needed to (193.C7), the two-mask complement, or the
(D_L=\lceil\sqrt L\rceil) conclusion.

## 2. Exact statement and hypotheses audited

The audit treats (P_{\rm cl}) as a diagonal operator on the free
physical-atom space.  A physical atom includes orientation, height,
affine site, ordered lower and upper endpoint allocations, masks,
coefficient, phase, and zero extension.  The operator

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 =\mathscr R_{\rm core}(P_{\rm cl}W)
\tag{193.R1}
\]

means that every Round-187--Round-192 source construction is rerun on
the coordinatewise deleted physical source.  It does not mean
postcomposition of the already formed Abel differences by a scalar
mask.

The count is audited on both strict opposing orientations of the
accepted even-shift carrier.  No hypothesis (k=(m,m')=1) or
(r\equiv2\pmod4) is used.  The subsidiary involution in candidate
Section 5 is outside the count proof and is not needed here.

The only inherited size facts used in the count are

\[
 d,m,d',m'\asymp L,qquad 0<r=2\kappa gh<R_0,qquad
 |W_x|\ll_\eta X^\eta,
\tag{193.R2}
\]

with fixed implied constants.  All dyadic-height, Round-192 core,
arithmetic, Fourier, and literal predicates are deletions from this
physical carrier.

## 3. Line audit and derivation

### 3.1 Canonical multiplicity in (193.C9)--(193.C10)

On the plus orientation, every live opened tuple recovers its labels by

\[
 \kappa=(d,m'),\qquad g=(d,d'),\qquad
 U={d\over\kappa g},\qquad v={m'\over\kappa},
\tag{193.R3}
\]

\[
 S={d'-d\over2g},\qquad w={m-m'\over2}.
\tag{193.R4}
\]

The accepted primitive coprimalities make the fractions in (193.R3)
canonical, and even (r) with odd (d,d') makes (193.R4) integral.
Strict opposition gives (S,w>0).  Direct expansion then gives

\[
 h=Sv-Uw={r\over2\kappa g}>0.
\tag{193.R5}
\]

Thus the map from a plus tuple to
((\kappa,g,U,v,S,w)) is injective, and the accepted inverse formulas
show surjectivity onto the primitive carrier.  The minus orientation has
the analogous recovery with (kappa=(d',m)) and
(h=Uw-vS>0).  The two strict orientations are disjoint.  Hence the
multiplicity-one assertion in (193.C9)--(193.C10) passes for arbitrary
((m,m')); the subsidiary cofactor-coprime condition is not being used
silently.

### 3.2 Close inequalities, uniform (g), and small variables

Equations (193.C11)--(193.C12) are correct in both orientations.  If

\[
 A=\kappa(U-v)-2w,qquad B=\kappa(U-v)+2S,
\]

then (B-A=2(S+w)), so (|A|,|B|\le D_L/g) gives

\[
 S+w\le D_L/g,qquad
 |\kappa(U-v)|\le D_L/g+2w\le3D_L/g.
\tag{193.R6}
\]

There is no cancellation or parity assumption in this step.

The small-(L) clause after (193.C13) is unnecessary and should be
made uniform.  From the live lower cone, (d/m<16), the lower close
inequality, and (m\ge cL),

\[
 1\le g\le {d\over m}+{D_L\over m}
 \le16+c^{-1}{D_L\over L}\le G_0
 \qquad(L\ge2),
\tag{193.R7}
\]

because (D_L\le2\sqrt L).  Thus the sum over (g) has a fixed
finite multiplicity for every allowed shell, including (L=2).  No
bounded-(L), bounded-(X), or hidden (B)-dependent argument is
needed.

For fixed ((\kappa,g,U,v,w)), the plus determinant condition gives

\[
 {Uw\over v}<S<{Uw\over v}+{R_0\over2\kappa gv}.
\tag{193.R8}
\]

Since (kappa v=m'\asymp L), the interval length is

\[
 {R_0\over2\kappa gv}\ll {1\over g},
\tag{193.R9}
\]

and the number of integral (S)'s is
(O(1+R_0/(\kappa gv))=O(1)).  This explicitly includes intervals of
length below one.  In the minus orientation the interval lies on the
other side of (Uw/v) and has the same length.

### 3.3 Every (+1) term in (193.C15)--(193.C17)

At fixed ((\kappa,g)), the correct statement is: there are
(O(1+L/\kappa)) choices of (U); for each such (U), (193.R6)
leaves (O(1+D_L/\kappa)) choices of (v); for each pair, it leaves
(O(1+D_L)) choices of (w); and (193.R9) leaves (O(1)) choices of
(S).  The factors (g^{-1}) have been harmlessly discarded only
after (193.R7).

Writing (D=D_L), expanding every (+1) before simplifying gives

\[
\begin{aligned}
 &\sum_{\kappa\ll L}(1+L/\kappa)(1+D/\kappa)(1+D)\\
 &\quad\ll
 (1+D)\{L+L\log(2L)+D\log(2L)+LD\}.
\end{aligned}
\tag{193.R10}
\]

For (L\ge2), (1\le D\le2\sqrt L), every term on the last line is

\[
 O\{LD\log(2L)+LD^2\}.
\tag{193.R11}
\]

This proves (193.C16), including the (O(L)) large-(\kappa) tail,
the single-choice (U,v,S) cases, and (D/\kappa<1).  Moreover

\[
 LD_L\log(2L)+LD_L^2
 \ll L^{3/2}\log(2L)+L^2\ll L^2.
\tag{193.R12}
\]

Thus the atom count itself is (O(L^2)), with no epsilon absorption.
Only the literal pointwise coefficient uses a fresh (X^\eta), which
can be renamed inside the final epsilon budget.  The ceiling in (D_L)
causes no additional term.

### 3.4 No hidden (Y,Q), mode, or lift factor

The labels (h,U,v,S,w) are not independent in the physical source:
(h=Sv-Uw) (or (Uw-vS)) is determined after the other four labels
are fixed.  Restricting to (Y<h\le2Y) deletes atoms from the full
range (0<h<R_0/(2\kappa g)).  It contributes neither (Y) nor
(1+Y).

Likewise (q,m_0,a,k), and the projective band (J) are labels created
by the complete anchor Fourier expansion and its unique mode/lift
partitions.  They are not additional copies of a physical atom in
(mathscr H_Y^\sigma(P_{\rm cl}W)).  The physical proof is taken
before Fourier splitting.  When the safe pieces are later estimated,
their accepted coefficient masses, exact (m_0^{-1}) lift, and divisor
ledgers already include all of these unique spectral labels.  Since the
mask is independent of the Fourier mode, coordinate deletion cannot
increase those positive masses.  There is therefore no hidden factor
(Y,Q,m_0,q,J), or number of Fourier modes in (193.C18) or
(193.C20).

### 3.5 Deletion stability of the Round-187--Round-192 safe source

After the coordinate repair in Section 4, each safe source remains
valid:

1. **Round 187:** the (U=1), low-exact-conductor, and ordinary-edge
   estimates use physical atom counts and Fourier (ell^1) mass after
   a modulus.  Deleting physical coordinates cannot enlarge either.
2. **Round 188:** the imprimitive-lift estimate is a positive atom count
   with the exact lift weight.  The mask adds no lift multiplicity.
3. **Round 189:** projectively slow rows are paid by residue-class
   sparsity followed by positive height/site counting.  An arbitrary
   deletion inside a retained row only lowers that count.
4. **Round 191:** on an inverse-small row, endpoint-exact Abel inversion
   is rerun on the finite zero-extended sequence (W^P), so it returns
   that deleted row exactly.  The inverse-class row count is unchanged.
   The outer carrier terminal still occurs at at most the two original
   carrier endpoints, and the isolated Fejer term still contains the
   accepted scalar step.  Interior mask jumps are not assigned to either
   safe projection; they remain in the core.
5. **Round 192:** the Farey union is a row indicator independent of the
   affine site.  It commutes with the physical deletion and retains the
   exact replacement, rather than duplication, of selected terminal and
   Fejer rows.  Its divisor and positive row counts can only decrease.

All these projectors are applied to the masked input.  None is claimed
to commute with a post-Abel scalar multiplier.  A finite sum of their
accepted (O_{B,\varepsilon}(L^2X^\varepsilon)) bounds proves
(193.C20) after the repair.

### 3.6 Exact complement and general-width boundary

The masks in (193.C22) satisfy, pointwise on every opposing physical
atom,

\[
 1=P_{\rm cl}+P_1+P_2,
\tag{193.R13}
\]

and are disjoint in the stated lower-first order.  Linearity on the free
physical-atom space therefore proves (193.C23), including (T=0).
There is no missing (r\bmod4), cofactor-gcd, orientation, mode, or
core-predicate branch.

For the scale statement, the proof of (193.C24) uses (g=O(1)), which
follows uniformly from (193.R7) whenever (1\le D\le L).  The sentence
"for a general close width" is too broad without that range.  Replace
it by

\[
 1\le D\le L:\qquad
 |\mathscr H_Y^\sigma(P_{{\rm cl},D}W)|
 \ll_\eta\{LD\log(2L)+LD^2\}X^\eta.
\tag{193.R14}
\]

In particular, for (D=L^{1/2+\delta}) with
(0\le\delta\le1/2), the (LD^2) term is (L^{2+2\delta}).
The advertised square-root boundary and its positive-capacity loss are
then exact.  The theorem uses only (delta=0).

## 4. First issue and exact proposed patch

The first material issue is (193.C19), after the count has already
passed.  The physical mask is (P(h,t)), not generally one scalar at
height (h).  Replace the paragraph containing (193.C19) by the
following coordinatewise statement.

For each fixed row and orientation, define

\[
 W^P_\omega(h)=
 \sum_{t\in I_\omega(h)}P_\omega(h,t)(-1)^tB_\omega(h,t),
\tag{193.R15}
\]

with the original carrier and zero extension.  Then

\[
 \Delta^-W^P_\omega(h)=W^P_\omega(h)-W^P_\omega(h-1)
\tag{193.R16}
\]

is the sequence used in Abel inversion.  On the transported common
range, with previous index (t+\nu_\omega(h)) and transported affine
sign (\chi_\omega(h)), one has exactly

\[
\begin{aligned}
 &P_h(t)B_h(t)
 -\chi_\omega(h)P_{h-1}(t+\nu)B_{h-1}(t+\nu)\\
 &\quad=P_h(t)
 \{B_h(t)-\chi_\omega(h)B_{h-1}(t+\nu)\}\\
 &\qquad+\chi_\omega(h)
 \{P_h(t)-P_{h-1}(t+\nu)\}B_{h-1}(t+\nu).
\end{aligned}
\tag{193.R17}
\]

The second term is the exact physical-mask commutator and remains in
the new core.  Current sites without transported predecessors and
previous sites without current images remain the usual affine births
and deaths.  No occurrence is dropped or doubled.  Equations
(193.R15)--(193.R17), rather than the scalar shorthand in (193.C19),
make (193.C6), (193.C20), and (193.C21) mechanically exact.

Also replace the final two sentences surrounding (193.C13) and
(193.C24) by (193.R7) and the explicit range (193.R14).  These are
hygiene repairs; they do not change any bound.

## 5. Control outcomes

| Seam | Outcome |
|---|---|
| Primitive plus/minus multiplicity | **PASS.** Canonical recovery is (193.R3)--(193.R5); no (k=1) is used. |
| (S,w,U,v,\kappa) small cases | **PASS.** All interval counts include (1+) terms; (193.R9)--(193.R12) cover sub-unit widths and large (kappa). |
| Uniform small-(L) (g)-bound | **REPAIR.** The result is true uniformly by (193.R7); replace the finite-small-shell sentence. |
| Complete (193.C16) expansion | **PASS.** The omitted intermediate (L), (D\log L), and (D^2\log L) terms are dominated in (193.R10)--(193.R11). |
| (D_L=\lceil\sqrt L\rceil) power | **PASS.** The raw atom count is already (O(L^2)), (193.R12). |
| Hidden dyadic (Y) | **PASS.** Height is a determinant, not a free multiplicity. |
| Hidden (Q,q,m_0,J) or Fourier-mode count | **PASS.** These are unique spectral partitions and their accepted positive masses are already in the safe ledgers. |
| Meaning of (mathscr R_{\rm core}[P]) | **PASS in (193.C6), subject to the C19 repair.** It is evaluation on masked input, not postcomposition. |
| (P\Delta) commutator | **REPAIR.** Replace scalar (193.C19) by the affine-site transported identity (193.R15)--(193.R17). |
| Round-187 safe deletion | **PASS.** Positive atom count and Fourier (ell^1) mass. |
| Round-188 safe deletion | **PASS.** Positive lift-weighted atom count. |
| Round-189 safe deletion | **PASS.** Residue sparsity and positive site count. |
| Round-191 inverse/terminal/Fejer deletion | **PASS after R17.** Recompute on (W^P); keep interior (P)-jumps in the core. |
| Round-192 Farey deletion and no double count | **PASS.** Its row selector commutes with coordinate deletion and retains replacement bookkeeping. |
| Exact first-failure complement | **PASS.** (193.C22)--(193.C23) are exhaustive and disjoint on the opposing source. |
| General (D) statement | **REPAIR.** Add (1\le D\le L); the square-root theorem is unaffected. |
| Literal lower-mass quarantine | **PASS.** All estimates are upper-capacity statements on the selected sector. |

No numerical or external-theorem evidence was used.

## 6. Dependencies and exact artifacts used

This line audit used only:

1. `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`;
2. the exact Round-187--Round-192 operator and positive-ledger statements
   incorporated in that candidate; and
3. the campaign's accepted primitive-coordinate conventions referenced
   explicitly by (193.C9)--(193.C10).

The earlier hostile report was not used as authority for any conclusion.
No sibling review, computation, web source, or unlisted theorem was used.

## 7. Recommended state effect

**Revise the candidate, then replay this seam.**  Do not reject the
strict theorem: the count, target power, deletion-stable safe ledger, and
two-piece complement are correct.  Before promotion:

1. replace (193.C19) with the coordinatewise transported formulas
   (193.R15)--(193.R17);
2. make (g=O(1)) uniform for all (L\ge2) using (193.R7);
3. display the full (+1)-term expansion (193.R10) or an equivalent
   line before (193.C16); and
4. restrict (193.C24) to (1\le D\le L).

After those edits, the expected seam verdict is **PASS** with no change
to (193.C7), (193.C22)--(193.C23), the owner scope, or any exponent.

