# Source confirmation of the amended Round 143 conductor candidate

## 1. Result

**Verdict: REVISE-THEN-GREEN.**  The Linnik discreteness repair and the
BM/DI/ABL source-boundary amendments are mathematically correct.  All
substantive source claims now pass.  Two exact textual repairs remain:

1. in (143.C19), replace the literal “qquad” by “\qquad” (or by ordinary
   punctuation and spacing); and
2. in the Deshouillers--Iwaniec hypothesis sentence, add
   \(\varepsilon>0\).

After those two repairs, the source portion is GREEN.

## 2. Exact statement and hypotheses

The amended candidate correctly records:

- Kıral--Young Theorem 2.7 is even-character, weight zero, and does not
  certify the internal odd-character identity (143.C3);
- Blomer--Milićević (2.3) specializes to (143.C20), with
  \(u=(N_0,4^\infty)\), \(M_0=N_0/u\), second argument \(16uh\),
  \(\tau(\chi_4)=2i\), one common \(\omega\), and the level-\(4\) minus
  level-\(8\) sign;
- BM's same-sign transforms are exactly (143.C21)--(143.C22), and its
  printed spectrum is \(H+M+E\);
- level \(4\) has singular cusps \(\infty,0\) and no proper-level
  oldspace, while level \(8\) has
  \(\infty,0,1/2,1/4\) and level-\(4\) oldclasses;
- the BM Linnik estimate has fixed positive arguments, a fixed arithmetic
  weight, one compact smooth test, its normalized Mellin norm, and no
  printed complementary-range uniform theorem;
- DI fixes a cusp, assumes \(T\ge1\), \(N\ge1/2\), and one common
  sequence, with \(Y\ge1\) in Theorem 5; and
- ABL assumes positive \(n,r,s\), \((r,s)=1\), \(M,C,Z\ge1\), one
  sequence, the stated support and all mixed-derivative bounds, and
  \(\sqrt{Mn}/(s\sqrt r\,C)\ll Z\).

The only missing source hypothesis is DI's explicit
\(\varepsilon>0\).

## 3. Verification

The arithmetic and normalization seams are green.  The candidate retains
the exact Gauss factor and level sign, does not turn the internal
pure-level-\(4\) identity into a sourced trace formula, and promotes no
opposite-sign constant or residual term.

The sample distinction is also exact:

\[
 \frac{4\pi\sqrt{(4N_0)h}}{2n}
 =\frac{4\pi\sqrt{M_0(16uh)}}{4n}
 =\frac{4\pi\sqrt{N_0h}}n.
\]

Thus an \(S/c\) cross-cusp formula uses \(2nA_g\), while the sourced
standard-cusp \(S/C\) route uses \(4nA_g\), with the Gauss factor and
level-\(4\) minus level-\(8\) combination retained.

The amended Linnik paragraph is correct: (143.C29) is labeled a continuous
scale ratio, (143.C29a) gives integer coverage
\(\ll1/(Dg)\), asymptotic comparability is restricted to
\(H_{\rm Lin}(g)\gg1\), and the empty-range threshold is
\(g\gg\sqrt{K/L}\) with fixed implied constant.

## 4. First remaining defect

The first remaining defect is mechanical, not mathematical.  The bytes of
line (143.C19) read

“u=(N_0,4^\infty)=2^{v_2(N_0)},qquad M_0=N_0/u.”

There is no backslash before “qquad”; all other occurrences of
“\qquad” in the candidate contain the correct backslash.  Replace that
token exactly.

The only remaining source-card omission is \(\varepsilon>0\) in the DI
Theorem 2 sentence.  No further BM, ABL, Linnik, cusp, oldclass, transform,
or sample repair is required.

## 5. Required controls and outcomes

1. **KY parity:** pass.
2. **BM identity and \(\tau(\chi_4)=2i\):** pass.
3. **Level \(4/8\), singular cusps, and oldclasses:** pass.
4. **Same-sign transforms and \(H+M+E\):** pass.
5. **\(2n\) versus \(4n\) samples:** pass.
6. **Linnik discreteness and complementary range:** pass.
7. **ABL hypotheses and scope disclaimer:** pass.
8. **DI hypotheses:** revise only by adding \(\varepsilon>0\).
9. **C19 TeX/control check:** revise “qquad” to “\qquad”; there are no
   stray control bytes or carriage returns.

## 6. Dependencies and exact artifacts used

This confirmation used, without editing the candidate or shared state:

- candidates/conductor_round143_level_four_matrix_obstruction.md;
- reports/kuznetsov_source_hypothesis_audit.md;
- reviews/source_conductor_candidate_final_audit.md;
- reviews/blind_post_unmask_source_hypothesis_audit.md; and
- reviews/source_post_unmask_spectral_claims_audit.md.

All paths are relative to the Round-143 campaign directory.  The primary
source cards remain Kıral--Young Theorem 2.7 and (2.20);
Blomer--Milićević (2.3)--(2.5), Section 3, (4.1)--(4.11), (5.1), and
Theorem 4; Deshouillers--Iwaniec Theorems 2 and 5; and
Assing--Blomer--Li Theorem 2.4.

## 7. Recommended state effect

**Do not promote the candidate verbatim until the two literal repairs are
made.**  After changing “qquad” to “\qquad” in (143.C19) and adding
\(\varepsilon>0\) to the DI hypothesis sentence, mark the source audit
GREEN and promote only the already scoped source-boundary and joint-matrix
obstruction.  No shared-state, downstream-obligation, or exponent change
follows from this confirmation.
