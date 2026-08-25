# Final discovery audit of the repaired Round 143 conductor candidate

Campaign: m9-m2-unbalanced-level-four-kuznetsov-matrix-gate

Reviewed artifact:
rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md

Starting graph SHA-256:
7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789

## 1. Result

**Verdict: revise in two exact documentary places, then green for promotion
of the scoped obstruction.**  Every mathematical repair required by the
first discovery audit now passes: the fixed-modulus double quotient is
defined; the carriage-return corruption is gone; the full frozen polytope is
present; the Blomer--Milićević identity is self-contained; the conditional
\(2n\) cross-cusp and sourced \(4n\) standard-cusp samples are distinguished;
the literal profile and common zero-padding ledgers are restored; the
diagonal control is given only its valid Parseval-insufficiency meaning; and
the out-of-scope global exponent display has been removed.

Two statement defects remain.  First, Section 6 calls (143.C27) the first gap
for the sourced level-\(4/8\) route even though (143.C27) is explicitly the
conditional \(2n\) cross-cusp sample; the sourced sample is the \(4n\) sample
displayed immediately after it.  Second, the phrase “the named Round-135
source-map artifacts in the task briefs” is not an exact dependency ledger
and does not implement the prior mandatory instruction to list dependencies
by path.  Neither defect changes a bound, normalization, or the scoped
no-go, but they prevent an unqualified green verdict on the present text.

After the two replacements in Section 7 below, the candidate is
promotion-safe only as level_four_spectral_matrix_no_go: it proves an exact
arithmetic embedding and insufficiency of the frozen coefficient controls,
not a lower bound for the literal signed family and not a global theorem.

## 2. Exact statement and hypotheses

The promotion-safe hypotheses are exactly those now printed in
(143.C6)--(143.C7a):

\[
 X\ge2,\qquad D=X^\delta,\quad L=X^\ell,\quad
 R=X/D,\quad K=XL/D^2,\quad \Delta=D/L=R/K,
\]

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\]

Every odd gcd stratum \(r=gn,\ k=gj,\ (j,n)=1\), the real-centre factor
\(e(\xi j/n)\), the literal \(W\)- and \(q_L\)-profiles, their entries and
exits, and \(g\ll K\) remain in the owner.  At fixed \(g\), every row uses
centered representatives and a common zero-padded column set:

\[
 -\frac{n-1}{2}\le h\le\frac{n-1}{2},
 \qquad |h|\ll R/g.
\]

The exact internal arithmetic statement is

\[
 S^{\chi_4}_{\infty0}(4N_0,h;2n)
 =\chi_4(n)S(N_0,h;n),\qquad n\ \operatorname{odd},
\]

with the fixed-modulus quotient (143.C17a) and convention (143.C17).  It is
not promoted as a sourced odd-weight switched-cusp trace formula.  The legal
source route is instead the exact Blomer--Milićević level-\(4\) minus
level-\(8\) standard-cusp formula (143.C20), with \(S_{\chi_4}\) as in
(143.C19a), \(\tau(\chi_4)=2i\), factor
\(\chi_4(M_0)/\tau(\chi_4)\), index \(16uh\), common weight
\(\omega(C/4)\), and the minus sign between \(4\mid C\) and \(8\mid C\).

The scoped conclusion is unchanged: \(h=0\) costs
\(O_\varepsilon(X^\varepsilon)\); for the centered nonzero matrix, the
frozen inputs yield only the Hilbert--Schmidt/nuclear upper prices and the
automatic coefficient-blind closure

\[
 R\sqrt\Delta\,X^\varepsilon
 =\frac{X}{\sqrt{DL}}X^\varepsilon.
\]

No common smooth scalar test, common coefficient sequence, or vector-valued
owner-saving estimate follows from those controls.

## 3. Proof or derivation

The mandatory seams were recomputed as follows.

1. **Fixed-modulus quotient and arithmetic sign.**  Formula (143.C17a)
   fixes \(\Gamma_\infty^+=\langle T\rangle\), both translation quotients,
   and the lower-left entry \(c\).  For
   \[
    \gamma_0=\begin{pmatrix}A&B\\4C&D\end{pmatrix},
    \qquad
    \gamma_0\sigma_0
      =\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix},
   \]
   one has \(c=2n\) with \(n=D\) odd, while
   \(4BC\equiv-1\pmod n\) gives
   \(-C\equiv\overline4\,\overline B\pmod n\).  The phase is therefore
   \(\chi_4(n)S(\overline4M,H;n)\), and \(M=4N_0\) proves (143.C3)
   without assuming \((N_0,n)=1\).  The caveat for quotienting by
   \(\{\pm T^j\}\) correctly prevents an unsupported odd-weight unit.

2. **CR and TeX hygiene.**  A byte-level scan finds no carriage-return or
   other C0/C1 control byte.  The formerly corrupted conditions now read
   \(g,n\ \operatorname{odd}\) or \(r\ \operatorname{odd}\).  Tags
   (143.C1)--(143.C35), including the inserted “a” tags, are unique, and no
   (143.C36) global display remains.

3. **Full polytope and capacity.**  The restored inequalities imply
   \(a=\delta-\ell\in(1/4,1/2)\) and \(L\ge1\).  Since
   \(\sqrt{KD}/\sqrt{R/L}=L\), the second accepted-envelope branch has
   exponent \((1-a)/2\).  For \(p=1-(\delta+\ell)/2\),
   \[
    p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,\qquad
    p-\frac{1-a}{2}=\frac12-\ell>\frac14.
   \]
   Also \(\delta+\ell<3/4\), hence \(p>5/8\).  The residual-cell
   inequality creates no improving chamber.

4. **BM definition, factors, and spectral boundary.**  Formula (143.C20)
   is the exact \(q=q_1=4\) specialization: the squarefree divisors
   \(d=1,2\) give the level-\(4\) and level-\(8\) terms, while
   \(\mu(4)=0\); \(M_0=N_0/u\), \(u=2^{v_2(N_0)}\), and the shifted
   second index is \(16uh\).  The same \(\omega\) occurs in both sums.
   The candidate keeps the sourced \(H+M+E\) ledger, the two level-\(4\)
   singular cusps, the four level-\(8\) singular cusps, and the level-\(4\)
   oldclasses at level \(8\), while withholding an unsourced odd-weight
   opposite-sign formula.

5. **Profiles, padding, and matrix prices.**  The restored bounds
   \[
    |b_{g,n}(j)|\ll K^{-1}X^\varepsilon,\qquad
    \sum_j|b_{g,n}(j)|\ll g^{-1}X^\varepsilon,\qquad
    \sum_j|b_{g,n}(j)|^2\ll(gK)^{-1}X^\varepsilon
   \]
   give normalized row Parseval
   \(\sum_h|\widehat\gamma_{g,n}(h)|^2
     \ll(RK)^{-1}X^\varepsilon\).
   With \(O(R/g)\) zero-padded rows this yields
   \(\|A_g\|_{S_2}^2\ll(gK)^{-1}X^\varepsilon\) and
   \(\|A_g\|_{S_1}\ll\sqrt\Delta/g\,X^\varepsilon\).
   Multiplying by \(2n\asymp R/g\) or \(4n\asymp R/g\) changes only a
   fixed factor and gives exactly the powers in (143.C26).

6. **The \(2n\)/\(4n\) seam and Linnik threshold.**  The conditional
   cross-cusp \(S/c\) sample is \(2nA_g(n,h)\); the sourced standard-cusp
   sample at \(C=4n\) is \(4nA_g(n,h)\), with the Gauss factor and level
   difference retained.  Moreover
   \[
    M_0(16uh)=16N_0h,\qquad C^2\asymp(4R/g)^2,
   \]
   so the fixed factors cancel and the same-sign Linnik range is exactly
   \[
    0<h\ll\frac{X}{D^2g^2}=\frac{K}{Lg^2}.
   \]
   Its fraction of the centered row is \(\asymp1/(Dg)\), and for
   \(g\gg\sqrt{K/L}\), with a sufficiently large fixed constant, it
   contains no nonzero integer.  Parseval supplies no localization to this
   slice.

7. **Degenerate class, self-return, diagonal wording, and scope.**  The
   \(h=0\) Ramanujan-sum estimate is uniform in \((N_0,n)\) and sums to
   \(O_\varepsilon(X^\varepsilon)\).  Full \(h\)-orthogonality gives the
   original reciprocal row exactly.  The abstract diagonal is used only to
   show that row Parseval cannot by itself improve the nuclear upper price;
   it is not substituted for the literal family and proves no literal lower
   bound or rank assertion.  The final scope paragraph excludes every owner
   outside the one flat-smooth strict-UNBAL packet and derives no global
   exponent.

Thus all mathematical seams pass.  The two remaining defects are the
source-route cross-reference and non-exact inherited-artifact phrase stated
in Section 1.

## 4. First doubtful or unproved step

The first repair-required sentence is in candidate Section 6: “For the
source-certified Blomer--Milićević level-\(4/8\) route, the first project
gap is (143.C27).”  Formula (143.C27) belongs to the conditional
pure-level-\(4\) cross-cusp route.  The mathematical discussion immediately
before it already contains the correct sourced \(4n\) sample, so this is a
cross-reference error, not a normalization error in the derivation.

After that repair, the first actual unproved analytic step is exactly the
one the candidate identifies: a vector-valued trace theorem or a
low-projective-cost decomposition for the literal centered \(h\ne0\) matrix,
with common modulus Sobolev/Bessel control, all moving profiles and
endpoints, the long range outside (143.C28), exceptional spectrum, every
level-\(4/8\) Eisenstein family, and the level-\(8\) oldclasses.  The
diagonal control does not resolve this actual-family question.  On the
internal pure-level-\(4\) route, an earlier independent gap remains the
convention-matched weight-one switched-cusp trace formula itself.

## 5. Required control test and outcome

1. exact_gcd_restored_inverse_first_identity -- **pass**.
2. chi4_modulus_sign_and_level_four_embedding -- **pass** with the fixed
   quotient and odd-weight convention caveat.
3. cusp_modulus_progression_and_root_of_unity -- **pass**: internal \(2n\),
   sourced \(4\mid C\) minus \(8\mid C\), and no hidden
   modulus-dependent unit.
4. joint_gammahat_n_h_coefficient_geometry -- **pass as a scoped
   insufficiency result**; no categorical literal-family no-go is claimed.
5. real_centre_profile_and_endpoint_ownership -- **pass** with the profile
   and zero-padding ledgers restored.
6. Kuznetsov_test_Bessel_transform_hypotheses -- **pass in the body; revise
   one Section-6 cross-reference** from (143.C27) to the sourced \(4n\)
   sample.
7. holomorphic_Maass_Eisenstein_exceptional_ledger -- **pass within the
   stated same-sign source boundary**.
8. spectral_large_sieve_common_sequence_and_norms -- **pass as a no-go
   audit**, not as a signed estimate.
9. full_polytope_D_L_R_K_Delta_capacity -- **pass**.
10. Ramanujan_original_wave_and_spectral_self_return -- **pass**.
11. actual_character_vs_unsigned_adversary -- **pass**: the positive closure
    is not called character cancellation or a signed lower bound.
12. downstream_owner_and_exponent_scope -- **pass**; the global display is
    removed.
13. Exact dependency and source/TeX hygiene -- **revise the dependency
    phrase only**.  CR, tag, formula, and Unicode-name hygiene pass.

All controls were analytical, algebraic, source-comparative, or mechanical
text checks.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used, without editing the candidate or shared state:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/conductor_round135_kloosterman_dispersion_adjudication.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/blind_joint_matrix_spectral_feasibility.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_post_unmask_discovery_seam_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/discovery_post_unmask_blind_seam_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_post_unmask_source_hypothesis_audit.md; and
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/discovery_conductor_candidate_seam_audit.md.

The primary-source boundaries used through the source report are
Kıral--Young Definition 2.2, Theorem 2.7, and (2.20);
Blomer--Milićević (2.3)--(2.5), Section 3, (4.1)--(4.11), (5.1), and
Theorem 4; Deshouillers--Iwaniec Theorems 1, 2, and 5; and
Assing--Blomer--Li Theorem 2.4.

## 7. Recommended state effect

**Revise the candidate in exactly the following two places; then promote the
scoped obstruction and source-boundary node without another mathematical
repair.**

1. Replace the Section-6 sentence assigning the sourced route's gap to
   (143.C27) by:

   > For the source-certified Blomer--Milićević level-\(4/8\) route, the
   > first project gap is to control the literal samples
   > \(4nW(X/(gnD))\widehat\gamma_{g,n}(h)\), with the fixed Gauss factor
   > and level-\(4\) minus level-\(8\) sign retained; (143.C27) is only the
   > conditional pure-level-\(4\) cross-cusp counterpart.

2. Replace “the named Round-135 source-map artifacts in the task briefs” by
   the four exact paths listed in Section 6 above, from
   literal_wave_kloosterman_map_attack.md through the Round-135 synthesis.md.

After those documentary repairs, promote the exact internal arithmetic
identity, the source-certified level-\(4/8\) routing data, the target-safe
zero class, the matrix upper prices, the same-sign Linnik gap, the exact
self-return, and the full-polytope coefficient-blind capacity.  Promote only
the conclusion that the frozen interfaces do not yield an owner-saving
estimate.  Keep the quarter-bound obligation and every downstream owner
open; make no global exponent change.
