# Post-unmask audit of the blind level-four joint-matrix report

Campaign: `m9-m2-unbalanced-level-four-kuznetsov-matrix-gate`

Reviewed task: `blind_joint_matrix_spectral_feasibility`

Review seam: `level_four_embedding`, `trace_formula`, `joint_coefficient`, and `capacity`

Starting graph SHA-256: `7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789`

## 1. Result

**Verdict: revise the spectral normalization, then retain only a scoped
Parseval-interface no-go.**  The blind report independently found the correct
fixed-level algebra:

\[
 S^{\chi _4}_{\infty 0}(4N_0,h;2n)
   =\chi _4(n)S(N_0,h;n),\qquad n\ \text{odd},               \tag{1.1}
\]

for \(\Gamma_0(4)\), cusps \((\infty,0)\), scaling
\(\sigma_0=\left(\begin{smallmatrix}0&-1/2\\2&0\end{smallmatrix}\right)\),
and parity \(\kappa=1\).  Its sign, modulus progression, absence of a
modulus-dependent root, singular-cusp classification, \(h=0\) estimate,
Schatten inequalities, complete-\(h\) positive capacity, exact Fourier
self-return, and full-polytope exponent comparisons all pass after minor
wording or TeX repairs.

The purportedly exact weight-one Kuznetsov block (3.12)--(3.16) does not
pass.  Its transform constants, shifted denominator
\(\cosh \pi(t-i/2)\), opposite-sign kernel, and extra residual terms
\(\mathcal R^\pm\) are neither derived nor sourced.  They do not match the
printed Blomer--Milićević normalization, and the shifted denominator is
singular at the very \(t=0\) term which the report says might occur.  The
claim that residual terms are "all present" is stronger than the available
spectral resolution.  At exact level four the primitive conductor-four
character has no proper-level oldspace, but this fact should be stated; if
one imports the Blomer--Milićević level-four/level-eight residue-class
implementation, its level-eight spectrum does contain level-four oldclasses.

The diagonal matrix control is valid and useful, but it proves exactly this:
row Parseval alone cannot imply a better Schatten-one bound.  It does **not**
prove that the literal inverse-selector matrix saturates that bound, and it
does not rule out a scalar or vector-valued argument exploiting the explicit
inverse, support, and real-centre structure.  Thus the promotable conclusion
is a proof-theoretic insufficiency statement for the frozen inputs, not a
literal-family lower bound and not a universal Kuznetsov no-go.

## 2. Exact statement and hypotheses

Assume the frozen strict residual range

\[
 D=X^\delta,\quad L=X^\ell,\quad R=X/D,\quad
 K=XL/D^2,\quad \Delta=D/L=R/K,
\]

with \(1/4<\delta-\ell<1/2\), and retain the literal \(W\)- and
\(q_L\)-profiles, their entries and exits, every odd gcd stratum \(g\), and
the real-centre phase \(e(\xi j/n)\).  Put

\[
 C_g=N_g=R/g,\qquad J_g=K/g,
\]

and let

\[
 A_g(n,h)=W\!\left(\frac{X}{gnD}\right)
             \widehat\gamma_{g,n}(h),
 \qquad n\asymp C_g,\quad h\bmod n.                         \tag{2.1}
\]

The corrected proposition supported by the blind derivation is as follows.

> **Corrected blind kernel.**  Identity (1.1) holds in the generalized-
> Kloosterman convention fixed in Section 3 below.  The only singular cusps
> for \((\Gamma_0(4),\chi_4)\) are \(\infty\) and \(0\), and the compatible
> parity is \(\kappa=1\).  The degenerate class \(h=0\) contributes
> \(O_\varepsilon(X^\varepsilon)\).  For the nonzero joint matrix, the frozen
> packet gives
> \[
>  \|A_g\|_{S_2}^2\ll (gK)^{-1},\qquad
>  \|A_g\|_{S_1}\ll \frac{\sqrt\Delta}{g},                  \tag{2.2}
> \]
> and, for \(B_g(n,h)=2nA_g(n,h)\),
> \[
>  \|B_g\|_{S_2}\ll\frac{\sqrt{R\Delta}}{g^{3/2}},\qquad
>  \|B_g\|_{S_1}\ll\frac{R\sqrt\Delta}{g^2}.              \tag{2.3}
> \]
> These are upper bounds, sharp over the abstract class of matrices obeying
> only the same row-Parseval hypothesis.  They are not lower bounds for the
> literal matrix.  Consequently no target-saving scalar separation follows
> from row Parseval alone.  A proof using additional arithmetic structure is
> not excluded.

For fixed \(g\), a source-safe fixed-argument Linnik range covers only

\[
 |h|\ll H_{\mathrm{Lin}}(g)
 :=\frac{C_g^2}{N_0}
 \asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2},
 \qquad
 \frac{H_{\mathrm{Lin}}(g)}{C_g}\asymp\frac1{Dg}.           \tag{2.4}
\]

The full matrix has \(\asymp C_g\) centered frequencies and only Parseval
mass; no localization into (2.4) is available.  For
\(g>\sqrt{K/L}\), (2.4) contains no nonzero integer frequency.  This missing
short-\(h\)/full-\(h\) comparison should be added to the blind report.

No exact switched-cusp spectral formula is certified by the blind packet.
The source-safe qualitative ledger is: odd holomorphic weights
\(k=3,5,\ldots\) in the same-sign formula; the full weight-one Maa\ss
spectrum, including exceptional parameters and any \(t=0\) cusp form; the
continuous spectrum induced from \(\infty\) and \(0\); no cross-cusp
diagonal; and no holomorphic tower in the opposite-sign formula.  Exact
constants, an opposite-sign transform, and any residual contribution require
a separate primary-source or scattering-matrix derivation.

## 3. Proof or derivation

### Exact generalized-Kloosterman convention and sign

Fix

\[
 S(a,b;n)=\sum_{x\bmod n}^{*}
 e\!\left(\frac{a\overline x+bx}{n}\right).                 \tag{3.1}
\]

For

\[
 \gamma=\begin{pmatrix}A&B\\4C&D\end{pmatrix}\in\Gamma_0(4),
 \qquad AD-4BC=1,
\]

one has

\[
 \gamma\sigma_0=
 \begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix}.              \tag{3.2}
\]

Positive lower-left entry therefore gives exactly \(c=2D=2n\) with
\(n>0\) odd.  At fixed \(n\), \(C\) ranges over the units modulo \(n\), and

\[
 B\equiv-(4C)^{-1}\equiv-\overline4_n\,\overline C_n\pmod n.
                                                                    \tag{3.3}
\]

With the blind report's generalized-sum convention, the character factor is
\(\overline{\chi_4(D)}=\chi_4(n)\), and the phase from (3.2) is

\[
 e_n(mB-\nu C)
 =e_n(-m\overline4_n\overline C_n-\nu C).
\]

Hence

\[
 S^{\chi_4}_{\infty0}(m,\nu;2n)
 =\chi_4(n)S(-m\overline4_n,-\nu;n).                         \tag{3.4}
\]

Taking \(m=4N_0\), \(\nu=h\), and substituting \(C\mapsto-C\) gives
(1.1).  If the ordinary Kloosterman convention interchanges the direct and
inverse arguments, its symmetry \(S(a,b;n)=S(b,a;n)\) gives the same result.
Thus the blind sign is correct.  The convention must nevertheless be printed
as in (3.1); otherwise (3.8) is ambiguous rather than wrong.

The singular-cusp calculation also passes.  At \(0\),

\[
 \sigma_0T\sigma_0^{-1}=
 \begin{pmatrix}1&0\\-4&1\end{pmatrix},
\]

whereas for
\(\sigma_{1/2}=\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)\),

\[
 \sigma_{1/2}T\sigma_{1/2}^{-1}
 =\begin{pmatrix}-1&1\\-4&3\end{pmatrix}.
\]

Thus \(\infty\) and \(0\) are singular and \(1/2\) is not, since
\(\chi_4(3)=-1\).  Compatibility with \(-I\) forces
\((-1)^\kappa=\chi_4(-1)=-1\), hence \(\kappa=1\).  Since \(\infty\) and
\(0\) are inequivalent cusps, the cross-cusp formula has no diagonal term.

### Weight-one transform and spectrum audit

The blind report calls (3.12)--(3.16) an "exact" normalization without a
derivation or an external source.  In the printed Blomer--Milićević
odd-character convention, \(\kappa=1\) and the same-sign transforms are

\[
 \dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},      \tag{3.5}
\]

\[
 \widetilde g(t)=\frac{it}{2\sinh(\pi t)}
 \int_0^\infty\bigl(J_{2it}(x)+J_{-2it}(x)\bigr)
 g(x)\frac{dx}{x},                                          \tag{3.6}
\]

and the Maa\ss and Eisenstein terms carry \(1/\cosh(\pi t)\).  The blind
definitions instead multiply (3.5) by \(4\), multiply (3.6) by \(4\pi\),
and divide the spectral terms by \(\cosh\pi(t-i/2)\).  Its holomorphic
coefficient \(\Gamma(k)\) also cannot be checked because no holomorphic
Fourier normalization is specified.  Alternative normalizations are
possible, but their Fourier coefficients and every prefactor must be
derived together; the Whittaker expansion (3.11) alone does not do this.

There is also an internal endpoint defect:

\[
 \cosh\pi(t-i/2)=-i\sinh(\pi t),                             \tag{3.7}
\]

so the denominator in (3.15)--(3.16) vanishes at \(t=0\), while the report
simultaneously proposes a possible \(t=0\) term and gives no limiting or
cancellation prescription.  Blomer--Milićević place all real \(t\),
including \(t=0\), in the full Maa\ss basis; their holomorphic tower has
\(k>\kappa\) and therefore starts at \(k=3\).  A weight-one \(t=0\) cusp
form is not a second, separately appended residual or holomorphic-limit
term.

The source-safe formula used for comparison has \(H+M+E\) and no separately
printed \(\mathcal R^\pm\).  Thus the blind sentences that residual terms
are present in both signs and may include a holomorphic weight-one limit
must be deleted.  If a different switched-cusp contour is intended, its
scattering matrix must first be computed; one may not add a placeholder
residue to an identity and still call the identity exact.  The precise
opposite-sign weight-one \(K\)-Bessel normalization in (3.14) is likewise
not supplied by the audited sources and must be downgraded to a qualitative
requirement.

There is no proper-divisor oldspace at exact level four with primitive
conductor-four nebentypus: a lower level cannot carry \(\chi_4\).  Full
orthonormal bases at level four therefore suffice.  This should be stated to
meet the owner-complete ledger.  By contrast, if one replaces the direct
switched-cusp identity with the Blomer--Milićević odd-modulus
level-four/level-eight combination, the level-eight side has level-four
oldclasses and they must be retained.

These defects do not destroy the coefficient-interface obstruction.  That
obstruction needs only the existence of a scalar trace formula with a
controlled common modulus test and the qualitative fact that all its
spectral pieces must be bounded; it does not need the incorrect constants in
(3.12)--(3.16).

### Schatten calculations and the logical strength of the diagonal control

There are \(\asymp C_g=R/g\) rows.  The row Parseval estimate gives

\[
 \|A_g\|_{S_2}^2
 =\sum_{n,h}|A_g(n,h)|^2
 \ll\frac{C_g}{RK}=\frac1{gK}.                              \tag{3.8}
\]

Since \(\operatorname{rank}A_g\le C_g\),

\[
 \|A_g\|_{S_1}\le\sqrt{C_g}\,\|A_g\|_{S_2}
 \ll\frac{\sqrt\Delta}{g}.                                 \tag{3.9}
\]

Multiplication of row \(n\) by \(2n\asymp C_g\) gives

\[
 \|B_g\|_{S_2}^2\ll
 \frac{C_g^3}{RK}=\frac{R\Delta}{g^3},
 \qquad
 \|B_g\|_{S_1}\ll\frac{R\sqrt\Delta}{g^2}.              \tag{3.10}
\]

All four calculations are correct.  The abstract diagonal example with one
entry \((RK)^{-1/2}\) in each of \(\asymp C_g\) distinct rows and columns
saturates (3.9)--(3.10), up to support constants.  But it is not the literal
matrix (3.2) of the blind report.  Therefore it proves only the implication

\[
 \text{row Parseval alone}\ \not\Longrightarrow\
 \text{a smaller uniform Schatten-one estimate}.             \tag{3.11}
\]

It does not prove a lower bound on \(\|A_g\|_{S_1}\), a high rank for the
literal family, or failure of an estimate exploiting inverse congruences.
Likewise, the sentence that "any scalar positive estimate" must pay
\(S_1\) is too broad.  The exact statement is that a termwise triangle after
an \(L^2\)-normalized SVD pays \(\sum s_\rho=\|A_g\|_{S_1}\); a simultaneous
vector-valued inequality might pay a different norm, but no such legal
inequality is in the packet.

There is a second, independent separation price.  The required samples
\(B_g(n,h)\) lie at logarithmic spacing \(\asymp C_g^{-1}\).  A canonical
disjoint-bump interpolation has order-\(r\) logarithmic Sobolev cost

\[
 C_g^{r-1}\sum_{n,h}|B_g(n,h)|,
 \qquad
 \sum_{n,h}|B_g(n,h)|
 \ll \frac{C_g^2}{\sqrt{gK}},                               \tag{3.12}
\]

by Cauchy and (3.8).  This is an available upper price for an exact atomic
interpolant, not a lower bound for the literal values.  It makes precise why
an algebraic SVD does not itself provide Bessel/Mellin smoothness.

### Zero class, full-frequency capacity, and self-return

The zero-class calculation passes.  From the literal coefficient bounds,

\[
 |\widehat\gamma_{g,n}(0)|\ll R^{-1},\qquad
 |S(N_0,0;n)|\le(n,N_0).
\]

Since

\[
 \sum_{n\asymp R/g}(n,N_0)\ll (R/g)\tau(N_0),
\]

the fixed-\(g\) contribution is \(O_\varepsilon(g^{-1}X^\varepsilon)\),
and summing \(g\ll K\) proves \(O_\varepsilon(X^\varepsilon)\).

For every gcd \((N_0,n)\), additive orthogonality gives

\[
 \sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n).                 \tag{3.13}
\]

Row Cauchy therefore costs \(\sqrt\Delta/g\); summing the
\(R/g\) rows and then all \(g\) gives

\[
 \sum_{g\ll K}\frac{R\sqrt\Delta}{g^2}
 \ll R\sqrt\Delta
 =\frac{X}{\sqrt{DL}}
 =X^{1-(\delta+\ell)/2}.                                    \tag{3.14}
\]

This is a valid coefficient-blind upper bound and loses both the
\(\chi_4(n)\) and \(\chi_4(g)\) directions when positive norms are taken.
It is not a lower bound for the signed scalar.  Expanding
\(\widehat\gamma\) and summing \(h\) first gives the original reciprocal
row exactly, so the self-return claim also passes.

### Bessel height and polytope comparison

On a dyadic frequency block \(|h|\asymp H\), the Bessel argument has size

\[
 Z(g,H)\asymp\frac{\sqrt{XH}}{C_g}.                          \tag{3.15}
\]

At full frequency \(H\asymp C_g\), the natural scale satisfies
\(T_g^2\asymp Dg\).  At \(g\asymp K\),

\[
 T_K=\sqrt{DK}=\sqrt{XL/D},\qquad
 \frac{R}{T_K}=\sqrt{X/(DL)}.                               \tag{3.16}
\]

These algebraic identities are correct and match the two summands in the
accepted curvature expression.  They do not prove that arbitrary
interpolants are spectrally restricted to height \(T_g\), nor that
\(R/T_K\) is produced by a particular weight-one transform estimate.
The phrase "exactly the two transform-return scales" should therefore be
replaced by "the same two dimensional scales" unless a transform estimate
is supplied.

Let \(a=\delta-\ell\).  The accepted envelope is

\[
 \min\!\left(\Delta,\sqrt{KD}+\sqrt{R/L}\right),
 \qquad \Delta=X^a,\quad \sqrt{KD}=X^{(1-a)/2}.             \tag{3.17}
\]

Because \(L\ge1\), \(\sqrt{KD}\ge\sqrt{R/L}\), so the second branch is
governed by \(X^{(1-a)/2}\).  Both decisive branch sizes exceed
\(X^{1/4}\).  The second summand \(\sqrt{R/L}\) need not itself exceed
\(X^{1/4}\), a distinction the blind wording should make explicit.  If
\(p=1-(\delta+\ell)/2\) is the exponent in (3.14), then

\[
 p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,
 \qquad
 p-\frac{1-a}{2}=\frac12-\ell>\frac14.                      \tag{3.18}
\]

Thus the positive closure is uniformly worse than both envelope branches;
the extra residual-polytope inequality creates no improving chamber.

## 4. First doubtful or unproved step

The first unsupported step in the **blind artifact** is the declaration in
(3.12)--(3.16) of an exact normalized weight-one switched-cusp Kuznetsov
formula.  No source or derivation connects the Whittaker normalization
(3.11) to its factors \(4\), \(2\pi\), \(-8i\), shifted hyperbolic
denominators, holomorphic prefactor, or \(\mathcal R^\pm\).  Equation (3.7)
above exposes an unresolved \(t=0\) singularity.  Those formulas cannot be
used or promoted as written.

After deleting that overclaimed block, the first missing step in the
**proposed spectral route** is exactly the one identified by the blind
report: a theorem controlling the literal \((n,h)\) matrix simultaneously
in a Bessel-compatible projective/vector norm and a modulus Sobolev norm,
uniformly in \(g\), \(\xi\), all profiles, and all endpoints.  It must cover
the long range outside (2.4), both signs, exceptional parameters, both
Eisenstein cusp families, and any auxiliary-level oldclasses.  Row Parseval
does not imply such a theorem.  Conversely, the abstract diagonal example
does not disprove it for the literal matrix.

## 5. Required control test and outcome

1. **`exact_gcd_restored_inverse_first_identity` -- pass.**  The report
   retains every odd \(g\), the unit inverse, and the exact Fourier return.
2. **`chi4_modulus_sign_and_level_four_embedding` -- pass after convention
   insertion.**  Equations (3.1)--(3.4) verify the exact sign and ordinary
   arguments.
3. **`cusp_modulus_progression_and_root_of_unity` -- pass.**  The moduli are
   exactly \(2n\equiv2\pmod4\), the cusps are \((\infty,0)\), and no
   modulus-dependent root occurs.
4. **`joint_gammahat_n_h_coefficient_geometry` -- revise scope.**  The
   Schatten upper bounds pass.  The diagonal control proves insufficiency of
   row Parseval only, not saturation by the literal family.
5. **`real_centre_profile_and_endpoint_ownership` -- pass at the formal
   identity level.**  The factor \(e(\xi j/n)\), \(W\), \(q_L\), moving
   support, and all \(g\)-strata remain inside the coefficient.  No endpoint
   estimate beyond this owner is claimed.
6. **`Kuznetsov_test_Bessel_transform_hypotheses` -- fail as written.**  The
   exact formulas (3.12)--(3.16) are unsupported; the interpolation and
   Bessel-Sobolev obstruction survives qualitatively and is quantified by
   (3.12).
7. **`holomorphic_Maass_Eisenstein_exceptional_ledger` -- revise.**  Keep
   odd \(k\ge3\), all Maa\ss including exceptional and \(t=0\), and both
   singular-cusp Eisenstein families.  Delete the invented residual/weight-one
   limit terms.  State the exact-level-four oldspace fact and the conditional
   level-eight oldclass caveat.
8. **`spectral_large_sieve_common_sequence_and_norms` -- obstruction
   confirmed only from frozen inputs.**  No common smooth test or controlled
   vector-valued substitute follows from the packet.  No universal or
   literal-family impossibility is proved.
9. **`full_polytope_D_L_R_K_Delta_capacity` -- pass after wording repair.**
   Equations (3.14), (3.17), and (3.18) give the exact uniform comparison.
10. **`Ramanujan_original_wave_and_spectral_self_return` -- pass.**  Full
    \(h\)-orthogonality returns the original row; it is not a gain.
11. **`actual_character_vs_unsigned_adversary` -- pass.**  The positive
    closures also prove the unsigned/adversarial analogue and hence cannot
    be advertised as character cancellation.
12. **`downstream_owner_and_exponent_scope` -- pass.**  The report is confined
    to one flat-smooth strict-UNBAL owner and changes no global exponent.
13. **Short-\(h\)/full-\(h\) range control -- omitted, repair required.**
    Add (2.4); Parseval gives no mass concentration in the Linnik range.
14. **TeX and metadata hygiene -- fail, mechanical repair required.**  In
    (2.1) replace `quad` by `\qquad`; in (3.9), (3.10), and the holomorphic
    parity condition replace the embedded carriage-return corruption by
    `\operatorname{odd}`; in (3.22) replace `ll` by `\ll` and
    `X^{,1-(\delta+\ell)/2}` by `X^{1-(\delta+\ell)/2}`; in (3.24) replace
    `qquad` by `\qquad`; and in the diagonal control replace both bare
    `asymp` strings by `\asymp`.  Section 6 should call the role "blind
    rederiver," not "reviewer," and should not list an unsourced exact
    Kuznetsov decomposition as an elementary dependency.

All controls in this review are analytical or algebraic; no numerical
experiment was used.

## 6. Dependencies and exact artifacts used

The review used, without editing shared state:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/blind_joint_matrix_spectral_feasibility.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/conductor_round135_kloosterman_dispersion_adjudication.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md`.

Primary normalization checks used:

- E. M. Kıral and M. P. Young, *Kloosterman sums and Fourier
  coefficients of Eisenstein series*, arXiv:1710.00914, especially
  Proposition 2.6, Theorem 2.7, and (2.20).  The switched-cusp geometric
  formula is relevant, but Theorem 2.7 assumes an even character and does
  not certify the blind weight-one spectral constants.
- V. Blomer and D. Milićević, *Kloosterman sums in residue classes*,
  arXiv:1410.4538, especially (2.4)--(2.5), the choice \(\kappa=1\) in
  Section 3, (4.3)--(4.6), Theorem 4, and the singular-cusp formula (5.1).
  These give the source-safe odd-character transforms and \(H+M+E\)
  architecture used in the comparison, but not the blind report's exact
  opposite-sign switched-cusp constants.

## 7. Recommended state effect

**Recommended effect: `revise`, with selective retention and no target
promotion.**  Retain as candidate/promotable scoped facts:

1. the exact level-four identity (1.1), with convention (3.1), cusps,
   moduli, parity, character factor, and sign;
2. the singular-cusp and no-cross-diagonal conclusions;
3. the \(h=0\) bound;
4. the Hilbert--Schmidt and nuclear upper bounds (2.2)--(2.3), explicitly
   labeled as automatic bounds rather than literal lower bounds;
5. the fixed-argument range obstruction (2.4), complete-frequency capacity
   (3.14), exact Fourier self-return, and polytope inequalities (3.18); and
6. the narrowed conclusion that the frozen row-Parseval data do not supply
   the joint Bessel/Sobolev lemma needed by scalar Kuznetsov or a standard
   spectral large sieve.

Do not promote (3.12)--(3.16) of the blind report, its residual-term
assertions, its exact opposite-sign normalization, or any claim that the
abstract diagonal matrix proves a no-go for the literal inverse-selector
family.  The defensible campaign label remains
`level_four_spectral_matrix_no_go` only when expanded as "no-go from the
currently frozen coefficient controls".  It is not a lower bound for the
signed scalar and not a theorem excluding a new literal-matrix or
vector-valued trace estimate.

Keep `M9-M2-smooth-unbalanced-three-quarter-estimate` open.  No sharp,
clipped, starred, transition, hard-TOP, BAL, complete M9-M2, endpoint, M9,
bridge, or global Gauss-circle state should change on the strength of the
blind report or this review.
