# Discovery seam audit of the Round 143 conductor candidate

Campaign: m9-m2-unbalanced-level-four-kuznetsov-matrix-gate

Reviewed artifact:
rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md

Starting graph SHA-256:
7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789

## 1. Result

**Verdict: revise, then promote only the scoped matrix obstruction.**  The
candidate's mathematical kernel is sound.  In particular, the ordinary
Kloosterman convention, the sign and inverse-of-four calculation in
(143.C18), unrestricted gcd scope, exact Fourier return, target-safe
\(h=0\) class, Hilbert--Schmidt and nuclear upper prices, constant-safe
Linnik threshold, complete-frequency capacity, and exponent differences
all pass.

The candidate is not promotion-ready as written for six exact reasons.

1. The generalized sum (143.C17) does not actually display its double
   quotient, translation stabilizers, or fixed-lower-left subset.  The
   missing definition matters in odd weight because quotienting by
   \(-I\) requires the multiplier and cusp phase to be fixed.
2. Formulas (143.C4), (143.C8), and (143.C20) contain literal carriage
   returns where \(\mathrm{odd}\) was intended.
3. The hypotheses (143.C6)--(143.C7) omit the full frozen polytope.  The
   later inequalities use \(\delta<1/2\), \(\ell\ge0\), and
   \(\ell<\delta-1/4\), none of which follows merely from
   \(1/4<\delta-\ell<1/2\).
4. The Blomer--Milićević formula (143.C20) suppresses the definition of
   \(S_{\chi_4}\), the Gauss factor
   \(\tau(\chi_4)=2i\), the summation ranges, and the requirement that the
   same \(\omega\) occur in both levels.  Its architecture is described
   correctly, but the displayed source identity is not self-contained.
5. The sample matrix \(B_g=2nA_g\) and (143.C27) are the conditional
   pure-level-\(4\) cross-cusp normalization.  The source-certified
   standard-cusp route has modulus \(C=4n\) and, in the \(S/C\) Kuznetsov
   normalization, exact samples \(4nA_g\).  The factor does not change any
   exponent, but the two source boundaries must not be conflated.
6. Section 6 gives only generic dependency descriptions, says that no
   arbitrary-array surrogate was used despite using the diagonal control,
   and appends the unrelated global-exponent display (143.C36).  The
   dependencies must be exact, the diagonal's limited role must be stated,
   and the global display should be deleted or explicitly sourced as
   inherited unchanged state.

These are repairable statement, source-boundary, and hygiene defects.  They
do not overturn the scoped conclusion: the currently frozen coefficient
controls do not furnish a common smooth test or a legal vector-valued norm
for the centered \(h\ne0\) matrix, and the automatic positive closure is
far above the accepted envelope.  They do prevent promotion of the
candidate verbatim.

## 2. Exact statement and hypotheses

The promotion-safe statement must begin with the complete frozen region

\[
 X\ge2,\qquad
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,                                    \tag{A.1}
\]

and

\[
 D=X^\delta,\quad L=X^\ell,\quad R=X/D,\quad
 K=XL/D^2,\quad \Delta=R/K=D/L.                             \tag{A.2}
\]

Put \(a=\delta-\ell\), so \(1/4<a<1/2\).  Retain every odd
gcd stratum, the literal profiles and their entries and exits, and the
real-centre phase.  For the matrix, use centered representatives

\[
 -\frac{n-1}{2}\le h\le\frac{n-1}{2}
\]

and zero-pad each row to a common \(|h|\ll R/g\) column set.

There are two distinct arithmetic/spectral routes.

- Internally, with translation stabilizers and the displayed scaling
  matrices fixed exactly, the pure-level-\(4\) cross-cusp arithmetic
  identity is
  \[
   S^{\chi_4}_{\infty0}(4N_0,h;2n)
   =\chi_4(n)S(N_0,h;n),\qquad n\ \mathrm{odd}.              \tag{A.3}
  \]
  This is not a sourced weight-one switched-cusp trace formula.
- Source-certified Blomer--Milićević instead gives the standard-cusp
  level-\(4\) minus level-\(8\) identity
  \[
  \begin{aligned}
   &\sum_{\substack{n\ge1\\n\ \mathrm{odd}}}
    \chi_4(n)S(N_0,h;n)\omega(n)\\
   &\quad=\frac{\chi_4(M_0)}{\tau(\chi_4)}
   \left\{
    \sum_{\substack{C\ge1\\4\mid C}}
      S_{\chi_4}(M_0,16uh;C)\omega(C/4)
    -
    \sum_{\substack{C\ge1\\8\mid C}}
      S_{\chi_4}(M_0,16uh;C)\omega(C/4)
   \right\},                                                 \tag{A.4}
  \end{aligned}
  \]
  where \(u=2^{v_2(N_0)}\), \(M_0=N_0/u\), and the same common
  \(\omega\) occurs in both sums.

The corrected scoped conclusion is:

> The complete \(h=0\) complement is
> \(O_\varepsilon(X^\varepsilon)\).  For \(h\ne0\), row Parseval gives
> only
> \[
>  \|A_g\|_{S_2}^2\ll_\varepsilon(gK)^{-1}X^\varepsilon,
>  \qquad
>  \|A_g\|_{S_1}\ll_\varepsilon
>       \frac{\sqrt\Delta}{g}X^\varepsilon.                  \tag{A.5}
> \]
> No target-saving common-test, projective--Sobolev, or vector-valued
> estimate follows from these bounds.  The automatic coefficient-blind
> closure is
> \[
>  R\sqrt\Delta\,X^\varepsilon
>  =X^{1-(\delta+\ell)/2+\varepsilon},                       \tag{A.6}
> \]
> which is uniformly worse than both accepted-envelope branches.
> This is an insufficiency result for the frozen controls, not a lower
> bound for the literal signed family.

## 3. Proof or derivation

### Arithmetic normalization and gcd restoration

Put \(\Gamma_\infty^+=\langle T\rangle\).  The exact repair of
(143.C17) is

\[
 \mathcal D_{\infty0}(c)
 :=\left\{[\rho]\in
 \Gamma_\infty^+\backslash
 \sigma_\infty^{-1}\Gamma_0(4)\sigma_0/\Gamma_\infty^+:
 \rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}\right\},          \tag{A.7}
\]

\[
 S^{\chi_4}_{\infty0}(M,H;c)
 :=\sum_{[\rho]\in\mathcal D_{\infty0}(c)}
 \overline{\chi_4}\!\left(D(\rho)\right)
 e\!\left(\frac{Ma+Hd}{c}\right),                           \tag{A.8}
\]

where \(D(\rho)\) is the lower-right entry of an underlying
\(\gamma_0\in\Gamma_0(4)\) satisfying
\(\rho=\sigma_\infty^{-1}\gamma_0\sigma_0\).  Its character value is
invariant under both translation stabilizers.  If a convention quotients
by \(\{\pm T^j\}\), the weight-one multiplier and cusp-\(0\) Fourier phase
must be included simultaneously.

For
\(\gamma_0=\left(\begin{smallmatrix}A&B\\4C&D\end{smallmatrix}\right)\),

\[
 \gamma_0\sigma_0
 =\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix}.
\]

Positive lower-left entry gives \(D=n>0\) odd.  The determinant congruence
gives

\[
 4BC\equiv-1\pmod n,\qquad
 -C\equiv\overline4_n\,\overline B_n\pmod n.
\]

The phase is \(MB-HC\), hence, using the candidate's convention
\(S(a,b;n)=\sum_x^*e_n(a\overline x+bx)\),

\[
 \sum_{B\bmod n}^{*}e_n(MB-HC)
 =S(H\overline4_n,M;n)
 =S(\overline4_nM,H;n).
\]

Multiplication by \(\chi_4(n)\) proves (A.3) at \(M=4N_0\).  Thus
(143.C18) has the correct sign and arguments, with no condition on
\((N_0,n)\).

For the owner, \(g=(r,k)\), \(r=gn\), \(k=gj\), and \((j,n)=1\).
Since \(r\) is odd, both \(g\) and \(n\) are odd.  The identities

\[
 \chi_4(r)=\chi_4(g)\chi_4(n),\qquad
 e(Xj/n)=e(N_0j/n)e(\xi j/n)
\]

and Fourier inversion give (143.C12) and then (143.C4).  The
\(\chi_4(n)\) factor is correctly absorbed into (A.3), while
\(\chi_4(g)\) remains outside.  Every gcd stratum and the real centre are
restored.  The three corrupted oddness conditions are typographical
failures only.

### Zero class and matrix norms

The candidate should insert the profile ledger

\[
 |b_{g,n}(j)|\ll_\varepsilon K^{-1}X^\varepsilon,\qquad
 \sum_j|b_{g,n}(j)|\ll_\varepsilon g^{-1}X^\varepsilon,
 \qquad
 \sum_j|b_{g,n}(j)|^2
 \ll_\varepsilon(gK)^{-1}X^\varepsilon.                    \tag{A.9}
\]

The literal support also forces \(g\ll K\).  Since \(n\asymp R/g\),
normalized Parseval gives

\[
 \sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
 =\frac1n\sum_m|\gamma_{g,n}(m)|^2
 \ll_\varepsilon\frac{X^\varepsilon}{RK}.                  \tag{A.10}
\]

There are \(O(R/g)\) rows, proving the Hilbert--Schmidt part of
(A.5).  Rank at most \(R/g\) then gives its nuclear part.  Multiplication
of row \(n\) by \(2n\asymp R/g\) yields exactly

\[
 \|2nA_g\|_{S_2}\ll_\varepsilon
 \frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,\qquad
 \|2nA_g\|_{S_1}\ll_\varepsilon
 \frac{R\sqrt\Delta}{g^2}X^\varepsilon.                    \tag{A.11}
\]

Thus (143.C23)--(143.C26) are algebraically correct.  The abstract
diagonal matrix shows only that row Parseval alone permits saturation of
the nuclear upper bound.  It gives no lower bound, rank statement, or
literal-family impossibility.

At \(h=0\), (A.9) gives
\[
 |\widehat\gamma_{g,n}(0)|\ll_\varepsilon R^{-1}X^\varepsilon.
\]
Together with
\[
 |S(N_0,0;n)|\le(n,N_0),\qquad
 \sum_{n\asymp R/g}(n,N_0)
 \ll_\varepsilon(R/g)X^\varepsilon,
\]
this costs \(O_\varepsilon(g^{-1}X^\varepsilon)\) at fixed \(g\).
Summing \(g\ll K\) proves the claimed target-safe zero class.  No
coprimality with \(N_0\) is used.

### Source route, sample normalization, and Linnik range

For (A.4), the candidate must define

\[
 S_{\chi_4}(a,b;C)
 =\sum_{d\bmod C}^{*}\chi_4(d)
 e\!\left(\frac{ad+b\overline d}{C}\right),\qquad
 \tau(\chi_4)=\sum_{a\bmod4}\chi_4(a)e(a/4)=2i.             \tag{A.12}
\]

The source boundary otherwise passes.  Kıral--Young's even-character
theorem does not certify the internal odd-character trace formula.
Blomer--Milićević certifies the same-sign standard-cusp route (A.4), with
\(H+M+E\), two singular cusps and no proper oldspace at level \(4\), and
four singular cusps plus level-\(4\) oldclasses at level \(8\).  The
opposite-sign normalization remains conditional and unpromoted.

The candidate must distinguish its sample normalizations.  For the
conditional pure-level-\(4\) cross-cusp modulus \(2n\), an \(S/c\)
geometric formula uses the sample \(2nA_g(n,h)\), so
(143.C26)--(143.C27) are correct in that conditional architecture.  On the
source-certified standard-cusp route, the surviving modulus is \(C=4n\)
and

\[
 \frac{4\pi\sqrt{M_0(16uh)}}{4n}
 =\frac{4\pi\sqrt{N_0h}}n.
\]

In an \(S/C\) normalization its exact sample is \(4nA_g(n,h)\), with
\(\chi_4(M_0)/\tau(\chi_4)\) and the level-\(4\) minus level-\(8\) sign
outside.  This is only twice (A.11), so all displayed powers remain valid,
but the candidate's phrase “the standard scalar trace formula” is
source-ambiguous and must be route-qualified.  If Theorem 1's
\(S/\sqrt C\) normalization is intended instead, its
\(\sqrt C\)-weighted test must be stated rather than (143.C27).

For the source-certified route, the standard modulus is
\(C_{\mathrm{std}}\asymp4R/g\) and the index product is
\(M_0(16uh)=16N_0h\).  The printed Linnik condition therefore reduces
exactly, up to its fixed implied constant, to

\[
 N_0h\ll(R/g)^2,\qquad
 0<h\ll\frac{X}{D^2g^2}=\frac{K}{Lg^2}.                    \tag{A.13}
\]

Its fraction of the complete centered range is \(\asymp1/(Dg)\).
The candidate correctly uses
\(g\gg\sqrt{K/L}\), not a sharp \(>\).  Such supported strata exist because
\[
 K/\sqrt{K/L}=\sqrt{KL}
 =X^{(1-2(\delta-\ell))/2}\longrightarrow\infty.
\]
Thus (143.C28)--(143.C29) pass after the fixed-factor explanation is
inserted.

### Capacity, exponent inequalities, and scope

The complete Kloosterman second moment

\[
 \sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n)
\]

holds for every gcd.  Row Cauchy costs \(\sqrt\Delta/g\), and summing
\(O(R/g)\) rows and all \(g\) proves (A.6).  This is an available
coefficient-blind upper closure, not a lower bound and not necessarily the
only conceivable closure.

Under the full hypotheses (A.1), the accepted envelope is

\[
 \min\left(\Delta,\sqrt{KD}+\sqrt{R/L}\right).
\]

Since
\[
 \frac{\sqrt{KD}}{\sqrt{R/L}}=L\ge1,
\]
the second branch has exponent \((1-a)/2\).  For
\(p=1-(\delta+\ell)/2\),

\[
 p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,\qquad
 p-\frac{1-a}{2}=\frac12-\ell>\frac14.
\]

Also \(\delta+\ell<3/4\), so \(p>5/8\).  The computations in
(143.C33)--(143.C35) pass, but the missing full hypotheses must be restored
before they are logically available.

The sentence saying that no arbitrary-array surrogate was used is false
as written: the diagonal array is used as a valid logical control.  It
should say that no arbitrary array is substituted for the literal family,
and that the diagonal is used only to prove insufficiency of row Parseval.
The global exponents and (143.C36) are outside this campaign's frozen owner.
Delete them, or cite them explicitly as inherited unchanged state rather
than as a Round-143 conclusion.

## 4. First doubtful or unproved step

The first promotion-blocking step in the candidate itself is the incomplete
definition (143.C17).  Without (A.7)--(A.8), the sign computation does not
specify the fixed modulus or how the odd multiplier treats \(-I\).  The
underlying algebra is correct, so this is a definition gap rather than a
counterexample.

After that repair, the first analytic gap depends on the route, as the
candidate correctly recognizes.  On the internal pure-level-\(4\) route,
the first gap is the convention-matched weight-one switched-cusp trace
formula itself.  On the source-certified level-\(4/8\) route, the first
project gap is a common smooth test or vector-valued estimate for the
literal centered \(h\ne0\) matrix, including the long frequencies,
exceptional spectrum, both level-\(4\) and all four level-\(8\) continuous
families, and level-\(4\) oldclasses at level \(8\).

The diagonal control does not settle that latter gap for the actual family,
and the positive capacity is not evidence that the signed scalar is large.

## 5. Required control test and outcome

1. **exact_gcd_restored_inverse_first_identity -- pass after mechanical
   repair.**  The factors \(r=gn\), \(k=gj\), \((j,n)=1\),
   \(1/(gj)\), \(e(\xi j/n)\), \(\chi_4(g)\), and every \(g\)-stratum are
   retained.  Replace the three carriage-return corruptions.
2. **chi4_modulus_sign_and_level_four_embedding -- revise definition,
   algebra pass.**  Equations (143.C15)--(143.C18) have the correct sign;
   replace (143.C17) by (A.7)--(A.8).
3. **cusp_modulus_progression_and_root_of_unity -- pass with source
   boundary.**  The internal moduli are \(2n\); the sourced standard-cusp
   route is \(4\mid C\) minus \(8\mid C\).  No modulus-dependent root is
   missing.
4. **joint_gammahat_n_h_coefficient_geometry -- pass as an insufficiency
   result.**  The Schatten powers are correct.  Add the profile ledger
   (A.9) and common zero-padding convention; do not infer literal
   saturation from the diagonal.
5. **real_centre_profile_and_endpoint_ownership -- pass.**
   \(e(\xi j/n)\), \(W\), \(q_L\), the unit condition, and moving support
   remain literal.
6. **Kuznetsov_test_Bessel_transform_hypotheses -- revise normalization.**
   Label \(2nA_g\) as conditional cross-cusp data and add the sourced
   \(4nA_g\) standard-cusp sample.  The common-test obstruction then
   remains unchanged.
7. **holomorphic_Maass_Eisenstein_exceptional_ledger -- pass.**  The
   candidate retains the level-\(4/8\) \(H+M+E\) terms, four level-\(8\)
   cusps, level-\(4\) oldclasses, exceptional and \(t=0\) Maaß terms, and
   withholds an opposite-sign normalization.
8. **spectral_large_sieve_common_sequence_and_norms -- pass as a no-go
   audit.**  The common-sequence and controlled-smoothness hypotheses are
   not supplied by row Parseval.
9. **full_polytope_D_L_R_K_Delta_capacity -- revise hypotheses, arithmetic
   pass.**  Restore (A.1) and the explicit envelope comparison; then
   (143.C33)--(143.C35) are uniform.
10. **Ramanujan_original_wave_and_spectral_self_return -- pass.**  The
    zero class is target-safe and complete \(h\)-orthogonality returns the
    original row.
11. **actual_character_vs_unsigned_adversary -- pass.**  The positive
    closure is invariant under arbitrary row phases and is not reported as
    character cancellation.
12. **downstream_owner_and_exponent_scope -- revise.**  The exclusions are
    correct, but (143.C36) is extraneous and the inherited exponents lack
    exact dependencies in this candidate.
13. **source and TeX hygiene -- revise.**  Define \(S_{\chi_4}\),
    \(\tau(\chi_4)\), and both sums in (143.C20); replace all lone carriage
    returns; and list exact artifacts rather than “the three reports and
    their reviews.”

All controls were analytical or algebraic.  No numerical experiment was
used.

## 6. Dependencies and exact artifacts used

This review used, without editing the candidate or shared state:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/blind_joint_matrix_spectral_feasibility.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/blind_post_unmask_discovery_seam_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md; and
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/discovery_post_unmask_blind_seam_audit.md.

Primary-source boundaries used are Kıral--Young Definition 2.2,
Theorem 2.7, and (2.20); Blomer--Milićević (2.3)--(2.5), Section 3,
(4.1)--(4.11), (5.1), and Theorem 4; Deshouillers--Iwaniec Theorems 1,
2, and 5; and Assing--Blomer--Li Theorem 2.4.  The exact source cards and
links are recorded in the source-hypothesis report and source post-unmask
review listed above.

## 7. Recommended state effect

**Recommended effect: revise the conductor candidate; after the listed
repairs, promote the scoped obstruction and source-boundary node.**  Apply
these exact repairs before any State Patch:

1. Replace (143.C17) by the fixed-modulus definition (A.7)--(A.8), including
   \(\Gamma_\infty^+\), \(D(\rho)\), and the odd-weight \(-I\) caveat.
2. Replace all three corrupted oddness conditions by
   \(\mathrm{odd}\), add the common centered zero-padding convention, and
   insert the profile bounds (A.9) plus \(g\ll K\).
3. Restore the full parameter region (A.1) and display the accepted
   envelope before invoking (143.C33)--(143.C35).
4. Expand (143.C20) exactly as (A.4), define (A.12), and state that one
   common \(\omega\) is used at levels \(4\) and \(8\).
5. Qualify (143.C26)--(143.C27) as the conditional \(2n\) cross-cusp
   normalization; add the source-certified \(4n\) standard-cusp sample and
   retain the fixed Gauss and Möbius factors.
6. Replace “the only owner-complete closure” by “the automatic
   coefficient-blind closure available from row Parseval and the complete
   second moment,” and replace “the sources do not accept” by the exact
   statement that the frozen coefficient fails their common-test
   hypotheses.
7. Replace the arbitrary-array sentence by the diagonal control's actual
   limited role, list every dependency by path, and delete (143.C36) and
   the unrelated global-exponent sentence unless they are explicitly
   labeled and sourced as inherited unchanged state.

After those repairs, promote only:

- the internal arithmetic identity (143.C3), not a sourced pure-level-\(4\)
  trace formula;
- the exact gcd-restored representation and target-safe \(h=0\) complement;
- the level-\(4/8\) source boundary and complete spectral ledger;
- the automatic matrix norms, same-sign Linnik gap, exact self-return, and
  full-polytope capacity; and
- the scoped conclusion that no target-saving estimate follows from the
  current trace-formula interfaces.

Keep the quarter-bound obligation and every downstream owner open.  Do not
change a global exponent, the candidate, shared state, or the proof graph
from this review.
