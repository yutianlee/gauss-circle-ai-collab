# Round 151 final independent reciprocal \(B\)-process candidate review

- Campaign: m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate
- Reviewed artifact: candidates/conductor_round151_character_ranges_and_bprocess_boundary.md, Sections 6--7
- Prior seam review: reviews/independent_bprocess_endpoint_review.md
- Role: terminal reciprocal-transform, endpoint, and scope reviewer
- Starting graph SHA-256: 521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f
- Terminal verdict: **GREEN**

## 1. Result

The repaired conductor candidate incorporates every required repair from
the prior RED review.  Its reciprocal \(B\)-process section is now
source-complete and promotion-safe within its stated scope:

1. the accepted Round-148 compact-smooth actual profile and its
   derivative, middle-buffer, transition, and tail ledger replace the
   false missing-profile obstruction;
2. the literal scalar is
   \(\widetilde S_U=B_{1,U}(1)S_U\), and the pair is
   \(\widetilde S_U\overline{\widetilde S_V}\);
3. self-return is asserted only for the phase and principal stationary
   symbol, with lower symbols, tails, and endpoint transitions retained in
   the accepted boundary ledger;
4. the generic Fejer/Fresnel discussion is separated from the actual
   compact-smooth application, so no every-integer jump obstruction is
   asserted; and
5. the displayed amplitude and coefficient specialize to \(D=d=1\), and
   the pair is the \(L_1=L_2=1\) component, not the full all-\(L\) row.

The phase, congruence classes, amplitude, Gaussian constant, source-complete
transform, and all-\(M\) capacity ledger remain correct.  No repair is
required in Sections 6--7 for this seam.

## 2. Exact statement and hypotheses

All denominator variables in the candidate are positive odd integers by
its global convention.  At the endpoint reviewed here,

\[
 D=d=1,\qquad L=1,\qquad E\asymp M,\qquad
 Q=2\sqrt{N/E}\asymp R^2M^{-1/2}.
\tag{R151.BF1}
\]

The actual sampled profile and scalar are

\[
 w_U(q)=\mathscr A_{1,M,U}\!\left(1,\frac{4N}{q^2}\right),\qquad
 S_U=\sum_{q>0}\chi_4(q)w_U(q)e(N/q),
\tag{R151.BF2}
\]

\[
 \widetilde S_U=B_{1,U}(1)S_U,\qquad
 |B_{1,U}(1)|\ll_\varepsilon X^\varepsilon.
\tag{R151.BF3}
\]

Thus two copies give precisely the
\(D=d=1,L_1=L_2=1\) pair component
\(\widetilde S_U\overline{\widetilde S_V}\).  Equations
(151.C47)--(151.C52b) do not claim a result for any \(L_i>1\).

The accepted actual-profile hypotheses are those of Round 148: the hard
radial-prefix and cone collars have separate prior owners; the retained
amplitude is compact smooth and exact on the retained lattice; bulk
derivatives are bounded; a radial transition has derivative scale
\(M^{1/2}\) on normalized length \(M^{-1/2}\); and a cone transition has
scale \(D^{1/2}\) on length \(D^{-1/2}\).  These facts give

\[
 \|w_U\|_\infty+\operatorname {Var}_{q\asymp Q}w_U
 \ll_\varepsilon X^\varepsilon
\tag{R151.BF4}
\]

and the higher-derivative, stationary-buffer, and tail controls used in
the boundary-complete Round-148 transform.  The exact floor prefix in
\(B_{1,U}(1)\) is independent of \(q\).

## 3. Proof and derivation audit

The character split

\[
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
\tag{R151.BF5}
\]

is exact.  Since the actual sum has positive compact support, its smooth
weight may be extended by zero away from that support for Poisson
summation; no value of \(N/q\) at \(q=0\) is invoked.

For \(f_\sigma(x)=N/x+\sigma x/4\), stationary Poisson frequency \(n\)
has

\[
 \ell=\sigma-4n>0,\qquad
 x_{\sigma,n}=2\sqrt{N/\ell},\qquad
 f_\sigma(x_{\sigma,n})-nx_{\sigma,n}=\sqrt{N\ell},
\tag{R151.BF6}
\]

and

\[
 f_\sigma''(x_{\sigma,n})^{-1/2}
 =2N^{1/4}\ell^{-3/4},\qquad
 \frac{4N}{x_{\sigma,n}^2}=\ell.
\tag{R151.BF7}
\]

The plus branch has \(\ell\equiv1\pmod4\), the minus branch has
\(\ell\equiv-1\pmod4\), and their difference restores
\(\chi_4(\ell)\).  Positive curvature contributes \(e(1/8)\), while
the factor \(1/i\) from branch recombination changes the final unit to
\(e(-1/8)\).  This verifies (151.C52).

More importantly, the candidate no longer treats that interior wave as a
complete endpoint formula.  It explicitly invokes the accepted
per-progression Round-148 identity

\[
 P_U=e(1/8)N^{-1/4}S_U+O_\varepsilon(X^\varepsilon),
\tag{R151.BF8}
\]

where

\[
 P_U=\sum_{\substack{\ell>0\\\ell\ \mathrm{odd}}}
 \chi_4(\ell)\ell^{-3/4}
 \mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell}),
\tag{R151.BF9}
\]

and hence

\[
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon).
\tag{R151.BF10}
\]

This is the required source-complete relation.  The error is
row-target-sized, while the signed main wave remains to be estimated.

The self-return wording is also correct.  With
\(\lambda=m+\sigma/4\) and \(g_\sigma(m)=2\sqrt{N\lambda}\), the
second saddle at \(m_p=N/p^2-\sigma/4\) has

\[
 g_\sigma(m_p)-pm_p=\frac Np+\frac{\sigma p}{4}.
\tag{R151.BF11}
\]

The two principal curvature amplitudes multiply to one and their Maslov
units cancel.  The candidate then expressly states that this does not
compose every lower symbol, nonstationary integral, or endpoint
transition.  Thus it proves a principal-transform no-go, not an exact
identity for two complete asymptotic expansions.

Finally, the direct and dual absolute capacities are correctly recorded as

\[
 \min\{R^2M^{-1/2},RM^{1/4}\}X^\varepsilon.
\tag{R151.BF12}
\]

The dual absolute bound is row-target-sized only for bounded \(M\); the
direct length is row-target-sized at \(M\asymp R^2\); a bare second
\(B\)-process gives no intermediate-scale saving.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the repaired endpoint derivation.
The first genuinely unproved mathematical estimate is, as the candidate
now says, the signed main-wave bound

\[
 |P_U|\ll_\varepsilon X^\varepsilon
\tag{R151.BF13}
\]

outside the separately proved strict ranges.  For a unit-scale profile,
this asks for an unweighted square-root-wave bound of size
\(M^{3/4}X^\varepsilon\), a factor \(M^{1/4}\) beyond absolute
summation.  Neither the boundary completion nor iteration of the principal
\(B\)-process proves it.

This open estimate is not a defect in the candidate because the candidate
retains it as open.  It also does not license an all-\(L\), \(D>1\), full
collar, or downstream conclusion.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| actual Round-148 source-complete transform | **GREEN.** Equations (151.C52a)--(151.C52b) insert the accepted compact-smooth profile and complete error ledger. |
| literal \(B_{1,U}(1)\) coefficient | **GREEN.** Equations (151.C47) and the following paragraph define \(\widetilde S_U\) and retain both coefficients in the pair. |
| character, congruence, phase, amplitude, and unit | **GREEN.** Equations (151.C48)--(151.C52) have the correct two residue classes, \(\sqrt{N\ell}\), \(2N^{1/4}\ell^{-3/4}\), and \(e(-1/8)\). |
| generic Fejer/Fresnel versus actual profile | **GREEN.** Generic literal jumps and truncated endpoint factors are described formally; the actual compact-smooth amplitude is handled by Round 148 and is not assigned an every-integer jump obstruction. |
| finite endpoint jumps in the variation partition | **GREEN.** The finite artificial support-component jumps mentioned in Section 5 contribute bounded variation only; they do not contradict the compact-smooth global profile or create the rejected jump seam. |
| boundary-complete error | **GREEN.** The principal wave is separated from (151.C52a)--(151.C52b), whose error is target-safe. |
| phase/principal-symbol-only self-return | **GREEN.** Equations (151.C53)--(151.C55) are followed by the exact lower-symbol and endpoint disclaimer required by the prior review. |
| all-\(M\) capacity | **GREEN.** Equation (151.C56) correctly separates bounded, intermediate, and top scales and is not called a signed lower bound. |
| \(D=d=1,L_1=L_2=1\) scope | **GREEN.** The first argument of \(\mathscr A\), the coefficient \(B_{1,U}(1)\), and the product of two \(L=1\) components make the scope exact.  No all-\(L\) implication is drawn from the \(B\)-process paragraph. |
| controls table consistency | **GREEN.** The decisions for D1_L1_reciprocal_scalar, boundary_complete_B_process, actual_profile_derivative_ledger, dual_self_return_vs_gain, and downstream scope match the proof text. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This terminal seam review used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/candidates/conductor_round151_character_ranges_and_bprocess_boundary.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/independent_bprocess_endpoint_review.md;
5. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md;
6. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md; and
7. the exact-row definitions in the accepted Round-149 and Round-150
   conductor candidates only as needed to confirm the coefficient and pair
   scope.

No sibling Round-151 discovery or source report, web source, computation,
or other review verdict was used.

## 7. Recommended state effect

**Recommended effect: GREEN for the repaired reciprocal-\(B\)-process
component; no remaining repair in this seam.**

The conductor may use (151.C47)--(151.C56) as evidence for:

1. the exact mod-four character split and square-root principal wave;
2. the accepted actual-profile boundary-complete transform;
3. exact phase and principal-symbol self-return as a method-specific
   no-gain result; and
4. the bounded/intermediate/top-\(M\) capacity ledger.

Promotion must preserve the explicit
\(D=d=1,L_1=L_2=1\) component scope and retain the signed estimate for
\(P_U\) outside the candidate's separately proved strict ranges as open.
Nothing in this review promotes a full all-\(L\) collar, \(D>1\), a
\(t\ge2\) layer, the cross owner, M1, M2, M9, the bridge, the quarter
target, or any global exponent.
