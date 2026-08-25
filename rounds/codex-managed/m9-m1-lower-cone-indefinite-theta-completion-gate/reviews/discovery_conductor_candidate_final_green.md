# Round 144 repaired conductor-candidate confirmation

## 1. Result

**GREEN.**  The repaired conductor candidate

rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/candidates/conductor_round144_appell_completion_and_cell_reduction.md

passes the final seam audit.  All five requested repairs are present:

1. the inherited \(0<\rho<1/8\) hypothesis and its permitted
   floor-to-cone constant dependence are stated, and (144.C4) carries
   \(O_{\varepsilon,\rho,V}(X^\varepsilon)\);
2. (144.C3a) gives the total
   \(O_\varepsilon((J+\sqrt M+1)X^\varepsilon)\) count, including
   \(J<1\) and \(j_m=0\);
3. (144.C33) now uses \(\gg_V\), not a coefficient-one strict
   inequality;
4. \(L_M\asymp M^{3/4}/R\) is defined before its inverse width is
   used; and
5. both corrupted odd-coset LaTeX tokens are repaired, with no
   carriage-return characters remaining.

The source/blind repairs are also present: the scalar
\(\Gamma_0(4)\) law is described as an internally derived
specialization of the accepted completed Jacobi laws, not as a
verbatim source theorem or a rediscovery of the Round-63 Appell
identity.  No remaining defect was found.

## 2. Exact statement and hypotheses

The candidate now fixes

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 0<\rho<1/8,\qquad
 \mathcal I_M=[M,2M)\cap[1,M_*],\qquad M_*\asymp R^2,
\]

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),
 \qquad
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
 j_m=k_m^2-Nm.
\]

Its repaired displacement statements are

\[
 \#\{m\in\mathcal I_M:0<|j_m|\leq J\}
 \ll_\varepsilon JX^\varepsilon
 \qquad(J\geq1),
\]

\[
 \#\{m\in\mathcal I_M:|j_m|\leq J\}
 \ll_\varepsilon(J+\sqrt M+1)X^\varepsilon
 \qquad(J\geq0),
\]

and

\[
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).
\]

The completed object remains

\[
 \mathcal H(\tau)
 =\frac12\widehat A_4(1/2,-3\tau;2\tau)
 =F(\tau)+\frac14+\sum_{a=0}^3\mathcal R_a(\tau),
\]

\[
 \mathcal H(\gamma\tau)
 =\chi_4(d)(c\tau+d)\mathcal H(\tau)
 \qquad(\gamma\in\Gamma_0(4)).
\]

The Appell specialization is pole-free on \(\mathbb H\), and the
character-Poisson formula is applied only to a smooth
\(C_c^\infty((0,\infty))\) block after global mask restoration.

## 3. Proof and derivation verification

### 3.1 Lattice and scalar completion

The lattice

\[
 L_4=\mathbb Z(1,0)\oplus\mathbb Z(0,4),\qquad
 \operatorname {Gram}(L_4)=
 \begin{pmatrix}0&4\\4&0\end{pmatrix}
\]

has signature \((1,1)\), discriminant order \(16\), and exact level
\(4\).  The signed cosets \((0,1)+L_4\) and \((0,3)+L_4\) encode
\(\chi_4(r)\).  The vectors \((1,-4)\) and \((0,-1)\) give the
sloping and isotropic walls.  The separate \(1/4\) is half the
bilateral Appell zero term; all four \(i/4\) theta--\(R_{\rm Zw}\)
corrections remain compulsory.

For \(\gamma\in\Gamma_0(4)\),

\[
 \widetilde\gamma=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix}\in\Gamma(2),
\]

and the displayed elliptic shifts are integers.  Their variable
exponentials cancel the modular Jacobi exponential, leaving

\[
 (-1)^{(a-1)/2}=\chi_4(a)=\chi_4(d).
\]

Thus the scalar weight-one law and its full-group limitation are
correct.

### 3.2 Repaired displacement proof

The prime-power estimate

\[
 \rho_N(j)\ll_\varepsilon
 N^\varepsilon\sqrt{(N,j)}
\]

is uniform for squareful \(N\).  Reversing the divisor sums gives

\[
 \sum_{1\leq|j|\leq J}\sqrt{(N,j)}
 \ll_\varepsilon JN^\varepsilon.
\]

The active range has \(k_m<N\), and
\(m=(k_m^2-j)/N\) makes the fixed-\(j\) map injective.  For \(j=0\),
writing \(N=Du^2\) gives \(m=Dt^2\); hence a block has
\(O(1+\sqrt M)\) exact radicals.  This proves (144.C3a), including
the case \(J<1\), where the nonzero window is empty.

After the \(M^{-3/4}\tau(m)\) weight, a \(J\)-window costs

\[
 O_\varepsilon\!\left(
 M^{-3/4}J+M^{-1/4}\right)X^\varepsilon.
\]

Thus \(J_M=M^{3/4}\) is the maximal polynomial threshold certified by
this absolute method.  The candidate correctly presents it as a
strict arithmetic reduction, not a signed bound.

### 3.3 Poisson, owners, and capacities

The exact character-Poisson formula retains the half-boundary,
harmonic subtraction, and outer \(i/2\).  At the positive stationary
point,

\[
 u_0^{-3/4}|\phi''(u_0)|^{-1/2}=2N^{-1/4},
\]

and negative curvature contributes \(e(-1/8)\).  Therefore

\[
 \frac i2\cdot2N^{-1/4}e(-1/8)
 =e(1/8)N^{-1/4}.
\]

This is exactly inverse to the accepted Round-140
\(e(-1/8)N^{1/4}\) factor.  The candidate correctly limits that
identification to the aggregate owner after all boundary,
negative-alias, collar, entry/exit, profile, and remainder terms are
reassembled.

The cone capacity remains \(M^{1/4+o(1)}\), hence
\(R^{1/2+o(1)}\) at the top block, and the normalized reciprocal
capacity remains \(R\).  The repaired slope statement,

\[
 \left|\frac{k_m}{2m}-\frac{\sqrt N}{2\sqrt m}\right|
 \gg_V\frac1{R^2M^{3/4}},
\]

is correctly compared with
\(L_M^{-1}\asymp R/M^{3/4}\), giving only the ratio \(R^{-3}\) for
the induced slope and no control of arbitrary Farey slopes.

Round 142 remains consistent: the \(4\mid q\) hierarchy matches the
scalar cusp orbit, while denominator-Abel reconstruction returns
\(r_2/4\), not \(C\), and retains the negative-character and
moving-wedge owners.

## 4. First doubtful or unproved step

There is no remaining doubtful seam in the repaired candidate.  The
first unproved estimate is still

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon,
\]

equivalently, after global owner restoration,

\[
 \mathcal S_{\rm recip}^+\ll_{\varepsilon,V}RX^\varepsilon.
\]

Neither real-analytic modularity, the wider cell deletion, nor the
capacity ledger proves these signed estimates.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| inherited \(\rho\) hypothesis | **GREEN.** It is fixed explicitly and the floor-to-cone equivalence records its dependence. |
| total \(J\)-window | **GREEN.** (144.C3a) covers \(J<1\), nonzero residuals, exact radicals, and squareful centres. |
| control characters | **GREEN.** The candidate contains zero embedded carriage returns. |
| lattice/cosets/level | **GREEN.** Signature, signed cosets, walls, discriminant, and level are unchanged and exact. |
| scalar multiplier | **GREEN.** Weight one and \(\chi_4(d)\) hold precisely on \(\Gamma_0(4)\). |
| Appell provenance | **GREEN.** The scalar law is correctly labelled a derived specialization; Round-63 novelty is not reclaimed. |
| Poisson constant | **GREEN.** The full saddle factor is \(e(1/8)N^{-1/4}\), with no factor two or cosine. |
| owner/capacity ledger | **GREEN/no-go.** Aggregate ownership and all three capacities are correctly scoped. |
| Round-142 seam | **GREEN/no-go.** The rational hierarchy is compatible and the Abel owner remains \(r_2/4\). |
| slope repair | **GREEN.** The \(\gg_V\) sign and \(L_M\) definition are present. |
| downstream scope | **GREEN.** No exponent or downstream theorem is promoted. |

No numerical evidence is used.

## 6. Dependencies and exact artifacts used

This confirmation used:

- the repaired conductor candidate;
- reviews/discovery_conductor_candidate_final_audit.md;
- reviews/discovery_post_unmask_blind_cell_and_completion_audit.md;
- reviews/blind_post_unmask_appell_return_and_cell_audit.md;
- reviews/source_post_unmask_completion_and_summation_audit.md; and
- the Round-63 and Round-140--142 accepted interfaces cited there.

No new source theorem was invoked.  The candidate passes
git diff --check, and its text contains no embedded carriage-return
characters.  No state, graph, campaign, synthesis, validation, plan,
or proof-draft file was edited.

## 7. Recommended state effect

Accept the repaired conductor candidate as **GREEN**.

Retain exactly its scoped recommendations:

- promote the derived scalar completion without duplicating Round 63;
- strengthen the arithmetic cell survivor from \(\sqrt M\) to
  \(M^{3/4}\);
- record the completed-Appell/character-Poisson aggregate self-return
  and Round-142 Abel mismatch; and
- leave the new signed survivor, reciprocal estimate, every M1/M2 and
  M9 owner, endpoint uniformity, bridge, internal \(1/3\), Li--Yang,
  quarter, and Gauss-circle claims open.

No further candidate repair is required.
