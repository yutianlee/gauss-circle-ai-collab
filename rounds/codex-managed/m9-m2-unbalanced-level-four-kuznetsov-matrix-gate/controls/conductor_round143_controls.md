# Round 143 conductor controls

Campaign: m9-m2-unbalanced-level-four-kuznetsov-matrix-gate

Starting graph SHA-256:
7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789

Candidate:
candidates/conductor_round143_level_four_matrix_obstruction.md

## 1. Control verdict

All twelve frozen campaign controls pass for the scoped conclusion
level_four_spectral_matrix_no_go.  The exact character-to-level arithmetic
identity, full gcd restoration, target-safe zero class, matrix norm ledger,
source boundary, Linnik range, self-return, and full-polytope capacity are
proved or source-audited.  The round does not prove the target estimate or
a signed lower bound.

The post-unmask reviews required revisions to unsupported spectral
normalizations, route conflation, discrete Linnik counting, and logical
strength.  The final candidate incorporates those repairs.  No numerical
experiment was used; allocation was 100 percent analytical, algebraic, and
source verification.

## 2. Exact algebra controls

### exact_gcd_restored_inverse_first_identity — pass

With \(r=gn\), \(k=gj\), and \((j,n)=1\),

\[
\chi_4(r)=\chi_4(g)\chi_4(n),\qquad
e(Xj/n)=e(N_0j/n)e(\xi j/n).
\]

The literal coefficient retains \(1/(gj)\), \(q_L(4Xj/(gn^2))\), every
support entry and exit, and the real-centre factor.  Normalized Fourier
inversion on \(\mathbb Z/n\mathbb Z\) gives

\[
\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
=\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
\]

for every \((N_0,n)\).  No gcd stratum is dropped.

### chi4_modulus_sign_and_level_four_embedding — pass internally

For

\[
\gamma_0=\begin{pmatrix}A&B\\4C&D\end{pmatrix},\qquad
\gamma_0\sigma_0=
\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix},
\]

positive generalized modulus means \(D=n>0\) odd and \(c=2n\).  The
determinant congruence is

\[
4BC\equiv-1\pmod n,\qquad
-C\equiv\bar4\,\bar B\pmod n.
\]

The fixed translation double quotient therefore gives

\[
S^{\chi_4}_{\infty0}(M,H;2n)
=\chi_4(n)S(\bar4M,H;n),
\]

and \(M=4N_0\) gives the exact identity

\[
S^{\chi_4}_{\infty0}(4N_0,h;2n)
=\chi_4(n)S(N_0,h;n).
\]

This is an internal arithmetic lemma, not an application of the
even-character Kıral--Young theorem.

### cusp_modulus_progression_and_root_of_unity — pass

The internal generalized moduli are exactly \(2n\) with \(n\) odd.  The
cusps \(\infty,0\) are singular and \(1/2\) is nonsingular.  Odd parity
forces \(\kappa=1\).  The fixed convention has no modulus-dependent root;
a different simultaneous slash/Fourier convention can change only one
global unit.

The source-certified alternative is the Blomer--Milićević standard-cusp
level-\(4\) minus level-\(8\) identity, selecting \(C=4n\), \(n\) odd,
with the fixed factor \(\chi_4(M_0)/\tau(\chi_4)\),
\(\tau(\chi_4)=2i\).  The \(2n\) and \(4n\) sample normalizations are kept
distinct.

## 3. Coefficient and transform controls

### joint_gammahat_n_h_coefficient_geometry — pass as an insufficiency result

The inherited profile bounds imply

\[
\sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
\ll_\varepsilon(RK)^{-1}X^\varepsilon,\qquad
\sum_{n,h}|\widehat\gamma_{g,n}(h)|^2
\ll_\varepsilon(gK)^{-1}X^\varepsilon.
\]

After centered zero padding,

\[
\|A_g\|_{S_2}^2\ll_\varepsilon(gK)^{-1}X^\varepsilon,\qquad
\|A_g\|_{S_1}\ll_\varepsilon\frac{\sqrt\Delta}{g}X^\varepsilon.
\]

Multiplication by either \(2n\) or \(4n\) gives, up to fixed constants,

\[
\|B_g\|_{S_2}\ll_\varepsilon
\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,\qquad
\|B_g\|_{S_1}\ll_\varepsilon
\frac{R\sqrt\Delta}{g^2}X^\varepsilon.
\]

An abstract diagonal matrix shows only that row Parseval permits saturation
of the nuclear upper price.  It is not substituted for the literal family
and proves no literal lower bound, rank statement, or universal no-go.

### real_centre_profile_and_endpoint_ownership — pass

The factor \(e(\xi j/n)\), \(W\), \(q_L\), the unit selector, moving
support, every odd \(g\), and all entries and exits remain in
\(\widehat\gamma_{g,n}(h)\).  The campaign is expressly limited to the one
flat-smooth strict-UNBAL owner; no sharp or endpoint owner is absorbed.

### Kuznetsov_test_Bessel_transform_hypotheses — obstruction confirmed

The conditional pure-level-\(4\) cross-cusp route needs controlled samples
\(2nA_g(n,h)\).  The legal Blomer--Milićević standard-cusp route needs
\(4nA_g(n,h)\), or its equivalent \(S/\sqrt C\) normalization, with one
common smooth test at both levels.  Row Parseval supplies no derivative,
Mellin, Bessel-bandwidth, or saving projective control for those samples.
Exact point interpolation has reciprocal-grid derivative cost.  This is a
missing interface, not a proof that every bespoke decomposition fails.

### holomorphic_Maass_Eisenstein_exceptional_ledger — pass

The source-certified same-sign ledger is exactly \(H+M+E\).  It includes
odd holomorphic weights \(k=3,5,\ldots\), every weight-one Maaß form
including exceptional parameters and \(t=0\) if present, and Eisenstein
integrals over all singular cusps.  Level \(4\) has two singular cusps and
no proper-level oldspace for primitive conductor four; level \(8\) has
four singular cusps and level-\(4\) oldclasses.  No ad hoc residual,
holomorphic weight-one limit, or unsupported opposite-sign transform is
used.

### spectral_large_sieve_common_sequence_and_norms — obstruction confirmed

Blomer--Milićević fixes positive arguments, one arithmetic weight, one
compact smooth archimedean test, and the Linnik range.  Deshouillers--
Iwaniec fixes a cusp and one common sequence in all spectral quadratic
forms.  Assing--Blomer--Li permits one sequence times a jointly smooth
two-variable function satisfying explicit support, derivative, coprimality,
and scale hypotheses.  The frozen coefficient controls prove no
owner-saving representation meeting any of these interfaces.

## 4. Range and capacity controls

### Linnik discreteness — pass after qualification

At modulus scale \(C_g=R/g\),

\[
H_{\rm Lin}(g)\asymp\frac{C_g^2}{N_0}
\asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2}.
\]

The continuous scale ratio is \(H_{\rm Lin}(g)/C_g\asymp1/(Dg)\), while
the actual positive integer coverage is only at most a constant times that
ratio.  It is asymptotic to that ratio only when
\(H_{\rm Lin}(g)\gg1\).  For \(g\gg\sqrt{K/L}\), with fixed dyadic
constants, no nonzero integer remains.  Parseval supplies no localization
into the covered range.

### full_polytope_D_L_R_K_Delta_capacity — pass

The complete second moment

\[
\sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n)
\]

holds for every \((N_0,n)\).  Row Cauchy costs
\(\sqrt\Delta/g\); summing \(O(R/g)\) rows and all \(g\) gives

\[
R\sqrt\Delta\,X^\varepsilon
=X^{1-(\delta+\ell)/2+\varepsilon}.
\]

For \(a=\delta-\ell\), the accepted envelope exponent is
\(\min(a,(1-a)/2)\).  If
\(p=1-(\delta+\ell)/2\), then on the complete frozen region

\[
p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,\qquad
p-\frac{1-a}{2}=\frac12-\ell>\frac14,
\]

and \(p>5/8\).  These are strict pointwise margins; no additional
polytope-uniform margin is claimed.

### Ramanujan_original_wave_and_spectral_self_return — pass

At \(h=0\),

\[
|\widehat\gamma_{g,n}(0)|\ll_\varepsilon R^{-1}X^\varepsilon,\qquad
S(N_0,0;n)=c_n(N_0),
\]

so the full zero class is \(O_\varepsilon(X^\varepsilon)\).  The strict
survivor is the fully gcd-restored \(h\ne0\) matrix.

Expanding \(\widehat\gamma\) and summing all \(h\) gives the original
reciprocal row exactly.  Smooth-first completion gives the accepted
\(\Delta X^\varepsilon\) Ramanujan/additive capacity.  Neither operation
is a new cancellation estimate.

### actual_character_vs_unsigned_adversary — pass

The \(R\sqrt\Delta\) closure remains valid after replacing the character
by arbitrary unit phases.  It is therefore coefficient-blind, not
cross-modulus character cancellation.  No capacity upper bound is used as
a signed lower bound.

### downstream_owner_and_exponent_scope — pass

Only the flat-smooth strict-UNBAL mechanism ledger changes.  Sharp,
clipped, starred, transition, hard-TOP, BAL, all other UNBAL owners,
M9-M2, endpoint uniformity, M9, the conditional bridge, and the target
remain open.  No global exponent changes.

## 5. Source boundary controls

Kıral--Young Theorem 2.7 assumes an even character and cannot certify
\(\chi_4\).  Blomer--Milićević supplies the legal odd-character route via
the exact level-\(4/8\) identity and weight-one same-sign transforms.
Deshouillers--Iwaniec and Assing--Blomer--Li are used only for their exact
interface hypotheses, not as if they were the required odd-weight
\(\chi_4\) matrix theorem.

The source report and two source-oriented reviews record exact theorem
locations, fixed-test hypotheses, singular cusps, oldclasses, exceptional
spectrum, and the absence of a printed complementary Linnik theorem.

## 6. Artifact and hygiene controls

The three task reports have exactly seven numbered top-level sections.
Unsupported exact weight-one switched-cusp constants, shifted hyperbolic
denominators, opposite-sign \(K\)-transform, residual terms, and a
holomorphic weight-one limit term were removed from the blind report.
The discovery report distinguishes the internal pure-level-\(4\) identity
from the sourced level-\(4/8\) route.  The source report was revised to
identify the \(h\ne0\) survivor and to avoid categorical factorization
claims.

The conductor candidate incorporates the post-unmask and final candidate
review repairs: fixed translation quotient, full polytope, common zero
padding, profile ledger, exact Blomer--Milićević formula, \(2n/4n\)
sample distinction, discrete Linnik coverage, complete DI/ABL hypotheses,
limited diagonal role, exact dependencies, and downstream scope.

## 7. Final control effect

Promote one external-source audit and one proved scoped obstruction.
Update the flat UNBAL target and accepted return, curvature-envelope, and
Kloosterman-interface nodes with Round-143 evidence.  Reject all route
overclaims listed in the adjudication.  Keep every target and downstream
obligation open.
