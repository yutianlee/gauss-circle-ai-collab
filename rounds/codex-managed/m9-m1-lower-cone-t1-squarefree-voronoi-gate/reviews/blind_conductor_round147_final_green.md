# Round 147 terminal arithmetic reread

Campaign: `m9-m1-lower-cone-t1-squarefree-voronoi-gate`  
Role: independent terminal arithmetic reviewer  
Candidate: `candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md`

## 1. Result

**GREEN for the repaired arithmetic seam and the scoped `squarefree_H_resonance_no_go`.** No further candidate correction is required by this review.

This verdict approves the exact localization, Euler, convolution, conductor, resonance, exceptional-case, and logical-scope statements. It does not promote the separate (t=1) target: the growing-order Bessel estimate and the signed correlation (147.C44) remain explicitly open.

## 2. Exact statement and hypotheses checked

The reread used the literal squarefree coefficient, strict cone, compact radial profile, physical weight, every half-open prefix, fixed (N=\lfloor X\rfloor), and individual positive phase. The power ledger is now explicitly restricted to

\[
z=i(\tau+t/2),
\]

or to a Perron abscissa (O(1/\log X)). No estimate uniform on a fixed nonzero real strip is claimed.

The finite transformed convolution uses

\[
K_F=\lfloor\sup\operatorname{supp}F\rfloor=O(M)
\]

and retains only (k\le K_F) as physical channels.

## 3. Verification

1. **Cone localization and zero mode:** (147.C12a) gives the hard Perron formula with (4^{-z},dz/z) and explicitly retains the residue at (z=0). Equations (147.C12b)--(147.C12c) correctly give

   \[
   d^{-it}(e/d)^{i\tau}
   =(de)^{-it/2}(e/d)^{i(\tau+t/2)},
   \]

   the radial twist (s^{-it/2}), and external constants (D^{it}4^{-i\tau}). The equivalent (4^{-z}) convention correctly includes (4^{it/2}). The zero Fourier mode is retained.

2. **Euler domains:** (147.C14a) now distinguishes the original absolute domain

   \[
   \Re(w+z)>1,\qquad \Re(w-z)>1
   \]

   from the residual (H)-domain in (147.C18), where both real parts exceed (1/2).

3. **Unitary power restriction:** lines 581--586 explicitly place (147.C40) and hence (147.C6) on the unitary line and record the missing factor (k_0^{|\Re z|}) for a fixed nonzero real part. The repaired power conclusion is exact.

4. **Finite convolution:** (147.C29) uses the finite sums (k\le K_F) in both the polar and dual terms. Lines 461--469 correctly state that any (k>K_F) polar-plus-dual identity is an inseparable zero pair and is not a physical resonance.

5. **Signed survivor:** (147.C44) now has (k\le K_F), includes the actual orders, radial twist, and external constants, and is expressly labeled the missing statement for the separate-(t=1) Voronoi route.

6. **Radical controls:** control 9 explicitly retains (D=1), primes, and even squarefree inputs; (N=sL^2) gives (e(\sqrt{Ns})=1); (N=sL^2+1) gives

   \[
   \sqrt{Ns}=sL+(\sqrt{L^2+1/s}+L)^{-1};
   \]

   and (m=kN) is the exact dual radical. None is promoted to a signed lower bound.

7. **Logical direction:** lines 103--106 state that a separate (t=1) estimate is sufficient for a layerwise proof but not necessary for a proof using cross-(t) cancellation. No later statement reverses that implication.

## 4. First doubtful or unproved step

There is no remaining arithmetic normalization defect. The first open analytic step is exactly the candidate's uniform growing-complex-order, moving-prefix control of all (J/Y/K) regimes following (147.C29). Granting it, the first open arithmetic step is the signed correlation (147.C44). These open steps are correctly stated as barriers, not silently assumed.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| C12a hard cone and (z=0) residue | Green |
| C12b--c constants, radial twist, and orders | Green |
| original and residual Euler domains | Green |
| unitary restriction in C6/C40 | Green |
| finite (K_F) convolution and tail treatment | Green |
| C44 cutoff and normalization | Green |
| route-specific sufficiency wording | Green |
| (D=1), prime, even, exact/slow radical controls | Green |
| upper-capacity versus signed lower bound | Green |
| prior-review byte cleanliness | Green |

The prior review `reviews/blind_conductor_round147_candidate_audit.md` contained fourteen U+200E formatting characters on eleven lines. They were removed with no mathematical change. A complete rescan found no remaining control or Unicode-format characters other than ordinary line endings and tabs.

## 6. Dependencies and artifacts used

This terminal reread used the current conductor candidate, the active-campaign requirements already read for the preceding seam audit, and the preceding independent review. No sibling report, web source, numerical calculation, candidate edit, or shared-state edit was used.

## 7. Recommended state effect

Accept the repaired candidate as arithmetic-green evidence for the narrowly scoped `squarefree_H_resonance_no_go`. Preserve its explicit open seams and its statement that the separate (t=1) estimate is sufficient rather than necessary. Make no promotion of (147.C3), (147.C4), any complete lower scalar, M1/M2, M9, the bridge, or the quarter target on the strength of this review alone.
