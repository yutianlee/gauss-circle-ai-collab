# Round 172 hostile audit: maximal parity-Fejer transform and endpoints

- Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate
- Task: maximal_fejer_transform_endpoint_hostile_audit
- Role: barrier_no_go
- Graph SHA-256: c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853
- Research allocation: 100% analytical/algebraic, 0% numerical

## 1. Result

### Maximal parity-Fejer positive-transform no-go

The parity projection, integer-scale telescoping, short-shift correction,
doubling tent, doubling-only Haar identity, and final non-doubling endpoint
all pass exactly.  They do not themselves save a factor \(L\).

The independent transform review verifies that discovery equations
(172.D13)--(172.D15) give the exact transform of the complete
**residual** family

\[
 Z_{\rm rem}(\theta)=
 \sum_N c_N^{\rm rem}e(J\sqrt N)e(N\theta)
\tag{172.H1}
\]

uniformly in the common Fejer frequency.  Its character-Poisson constant
is \(i/2\), and after squaring and inserting the two-peak parity projector
the exact bandpass constant is \(1/8\).  The derivation retains the
selected and no-pair rows, both product parities, squarefree and
coprimality holes, hard point values, and all zero, boundary, and
transition modes.

The ordinary-zero sector is target-safe, but only after the **full signed
recombination over all odd character frequencies**.  It is not
target-safe termwise in the character frequency \(k\).  The first open
affirmative seam is therefore the fully signed nonzero
ordinary-frequency aggregate (172.D23), before every positive norm.

The following route-specific no-go is rigorous at that seam.  Let
\(\Delta K=K_{R'}^{(2)}-K_R^{(2)}\), \(R<R'\le 2R\).  Any argument which,
before proving an actual-coefficient saving, replaces the complete signed
dual assembly by a positive dual-mode, opening, endpoint-cell, or
frequency norm has the coefficient-uniform capacity

\[
 \left|\mathfrak E_{R'}^{(2)}-\mathfrak E_R^{(2)}\right|
 \le \mathfrak E_{R'}^{(2)}+\mathfrak E_R^{(2)}
 \le (R'+R)D_L.
\tag{172.H2}
\]

At the maximal link \(R'\asymp M\asymp L^2\), this is
\(L^4X^\varepsilon\), not \(L^3X^\varepsilon\).  A dechirped array on one
absolute parity class attains \(\gg MD_L\), so no coefficient-uniform
phase-only, Parseval-only, generic-Haar, or post-transform positive
inequality can improve (172.H2) by \(L\).

The transform also self-returns at both Fejer peaks.  After centering the
frequency at either \(0\) or \(1/2\), the smooth product phase is

\[
 \Phi_\varphi(u,v)=J\sqrt{uv}+\varphi uv-\xi u-\eta v,
\tag{172.H3}
\]

and

\[
 \det \operatorname {Hess}\Phi_\varphi
 =-\varphi^2-\frac{J\varphi}{2\sqrt{uv}}.
\tag{172.H4}
\]

Thus the Hessian is rank one at the centre \(\varphi=0\) of **each**
parity peak.  There the accepted product collar and its restored positive
capacity reappear.  The bandpass has height comparable to the scale on a
subarc of reciprocal-scale width, so this degeneracy cannot be removed by
deleting one point or by a uniform nondegenerate stationary-phase claim.

Accordingly the hostile terminal recommendation is

\[
 \boxed{\texttt{maximal\_fejer\_dyadic\_character\_poisson\_no\_go}}
\]

for the route “exact transform followed by positive dual/cell control.”
This is not a lower bound for the physical residual coefficient and does
not disprove (165.K26).  A proof of the single fully signed aggregate
(172.D23) remains possible.

## 2. Exact statement and hypotheses

Assume

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M\asymp L^2,
\]

with \(M>R_0\) an integer.  Extend the complete literal coefficient by zero
and put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
\]

No square root is evaluated outside the positive literal support.  Define

\[
 C_r=\sum_Nz_{N+r}\overline {z_N},\qquad A_r=\Re C_r,
\qquad w_R(r)=\left(1-\frac rR\right)_+.
\]

Then, for every positive integer \(R\),

\[
 \mathfrak E_R^{(2)}
 =\int_0^1|Z(\theta)|^2K_R^{(2)}(\theta)\,d\theta
 =D_L+2\sum_{\substack{1\le r<R\\2\mid r}}w_R(r)A_r.
\tag{172.H5}
\]

For the chain \(R_{j+1}=\min(2R_j,M)\), with repetitions removed and
\(R_K=M\), put

\[
 B_{\rm short}
 =\sum_{\substack{1\le r<R_0\\2\mid r}}
 \left(w_M(r)-w_{R_0}(r)\right)A_r
 =\sum_{\substack{1\le r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1M\right)A_r.
\tag{172.H6}
\]

The exact endpoint identity is

\[
 T_{26}
 =\frac12\sum_{j<K}
 \left(\mathfrak E_{R_{j+1}}^{(2)}
       -\mathfrak E_{R_j}^{(2)}\right)-B_{\rm short},
\qquad
 |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{172.H7}
\]

For \(R<S\le2R\), the exact non-doubling weight is

\[
 w_S(r)-w_R(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S,
 \end{cases}
\tag{172.H8}
\]

and its diagonal coefficient is zero.  At \(S=2R\), (172.H8) is the
stated symmetric triangular tent.

For a doubling link, if

\[
 Y_{s,R}^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\ (2)}}z_{s+j},
\]

define the absolute-site-parity Haar detail

\[
 \mathfrak H_R^{(2)}
 =\frac1{2R}\sum_s\sum_{\epsilon=0}^1
 \left|Y_{s,R}^{(\epsilon)}-Y_{s+R,R}^{(\epsilon)}\right|^2.
\tag{172.H9}
\]

Then exactly

\[
 \mathfrak E_{2R}^{(2)}
 =2\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)},\qquad
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
 =\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}.
\tag{172.H10}
\]

There is no corresponding rounded identity for a strict
\(R<S<2R\) terminal link; (172.H8) must be used.

The local character transform used in the discovery identity is the
following.  For a lawful zero-extended cardinal interpolation \(g\),

\[
 \sum_{d\in\mathbb Z}\chi_4(d)g(d)e(\beta d)
 =\frac i2\sum_{\substack{k\in\mathbb Z\\k\ {\rm odd}}}
 \chi_4(k)\widehat g(k/4-\beta).
\tag{172.H11}
\]

For one product row in (172.H1), \(\beta=\theta m\).  Discovery equations
(172.D13)--(172.D15) carry out the literal residual recombination and may
be normalized schematically as

\[
 Z_{\rm rem}(\theta)=\frac i2\,\mathcal U_{\rm rem}(\theta),
\qquad
 \mathfrak E_{R'}^{(2)}-\mathfrak E_R^{(2)}
 =\frac18\int_0^1
 \{\Delta F(\theta)+\Delta F(\theta+1/2)\}
 |\mathcal U_{\rm rem}(\theta)|^2\,d\theta,
\tag{172.H11a}
\]

where \(\Delta F=F_{R'}-F_R\) and
\(\mathcal U_{\rm rem}\) is the complete transformed family of
(172.D13)--(172.D15), not a positive majorant.  The constants \(i/2\)
and \(1/8\) are exact.  All residual selectors, multiplicities, arithmetic
holes, endpoints, and both parity peaks remain in
\(\mathcal U_{\rm rem}\).

## 3. Proof or derivation

### 3.1 Parity projection and exact endpoints

The Fejer expansion is

\[
 F_R(\theta)=
 \sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta).
\]

Translation by \(1/2\) multiplies the \(r\)-th Fourier coefficient by
\((-1)^r\).  Hence

\[
 K_R^{(2)}(\theta)
 =\sum_{\substack{|r|<R\\2\mid r}}
 \left(1-\frac{|r|}{R}\right)e(r\theta),
\]

and expansion of \(|Z|^2\) proves (172.H5).  Both peaks are essential;
discarding \(F_R(\theta+1/2)\) restores odd gaps.

For \(R=2S+1\), put \(x_n=z_{2n}\), \(y_n=z_{2n+1}\), and
\(\mathcal E_T(w)=T^{-1}\sum_k|\sum_{j<T}w_{k+j}|^2\).  Directly splitting
even and odd window starts gives

\[
 \mathfrak E_{2S+1}^{(2)}
 =\frac{S+1}{2S+1}
  \{\mathcal E_{S+1}(x)+\mathcal E_{S+1}(y)\}
 +\frac S{2S+1}
  \{\mathcal E_S(x)+\mathcal E_S(y)\}.
\tag{172.H12}
\]

Thus the terminal even gap \(2S=R-1\) has weight \(1/R\), not a rounded
half-scale weight.  At \(R=1\), \(\mathfrak E_1^{(2)}=D_L\).

Telescoping (172.H5) from \(R_0\) to \(M\) gives (172.H7).  Cauchy gives
\(|C_r|\le D_L\), proving the displayed one-time short budget.  Direct
subtraction of \(w_S-w_R\) proves (172.H8).  The parallelogram identity
applied to the two adjacent length-\(R\) blocks, separately for absolute
site parity, proves (172.H10).  Relative-position parity would be wrong
when \(R\) is odd.

### 3.2 Literal multiplicity and the two parity branches

The residual coefficient has the exact opening

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d).
\]

Consequently each term in \(C_r\) is represented once by an ordered tuple

\[
 d m=N,\qquad d'm'=N+r,\qquad d,d'\ {\rm odd},
\]

and obeys \(d'm'-dm=r\).  The weights
\(\lambda_N(d)\) and \(\lambda_{N+r}(d')\) still contain the selected or
no-pair status, squarefree masks, coprimality holes, complementary parity,
profile, floor, star, crossing, endpoint value, and zero extension.  This
is multiplicity one at the physical divisor-incidence level.

The later Möbius projector is inclusion-exclusion, not a disjoint
partition.  Its \(Q=[a^2,c]\), \(R=[b^2,c]\) representations must retain
their signs until recombination.  Since the character-bearing divisor is
odd, the first physical factor is odd; the complementary factor may be
odd or even.  The \(p=2\) branch is therefore not optional.

At the second Fejer peak,

\[
 Z(\theta+1/2)
 =Z_{\rm even}(\theta)-Z_{\rm odd}(\theta).
\tag{172.H13}
\]

Together with the first peak, the parallelogram identity cancels
cross-parity correlations and retains both same-parity branches.  It does
not make the odd-product or even-product branch disappear.

### 3.3 Common-frequency transform, zero modes, and boundaries

Formula (172.H11) follows from the exact \(\chi_4\)-Poisson identity and
\(\widehat{g(\cdot)e(\beta\cdot)}(\xi)=\widehat g(\xi-\beta)\).  It has no
character zero frequency because \(k\) is odd.  A subsequent ordinary
Poisson transform in the complementary variable does have an
\(\ell=0\) mode.  Equations (172.D13)--(172.D15) prove that these
rowwise identities recombine to the exact literal residual transform
(172.H11a), with no loss of a selector, endpoint, parity branch, or
point value.

That ordinary zero mode is not the physical \(N=N'\) diagonal of
\(|Z|^2\).  The physical diagonal disappears from a bandpass only after
the **complete** transformed diagonal and off-diagonal, zero and nonzero
frequencies, and boundary pieces recombine.  A dual-diagonal term may
therefore not be set to zero merely because
\(\int_0^1\Delta K=0\).

The discovery zero-mode calculation does prove the complete
ordinary-zero sector target-safe **after summing all odd character
frequencies with their \(\chi_4(k)\) signs and retaining their cross
terms**.  It does not prove a target-safe estimate for a fixed \(k\), for
\(\sum_k|\cdot|\), or for a positive \(k\)-square inserted before that
recombination.  The latter readings would destroy the exact cancellation
which owns the zero sector.

Likewise, an exact cardinal transform keeps hard endpoints, point values,
zero-extension jumps, saddle-edge transitions, nonstationary tails, and
the original finite cells.  In the exact discovery formula these pieces
are retained inside the nonzero ordinary-frequency aggregate (172.D23)
unless explicitly included in the already recombined zero sector.
Replacing them by one favorable global smooth interior weight is not
lawful.  Positive summation over the cardinal cells removes precisely the
recombination which could carry the missing factor \(L\).

### 3.4 The restored \(L^4\) capacity

Since \(K_R^{(2)}\ge0\), window Cauchy gives

\[
 0\le\mathfrak E_R^{(2)}\le RD_L.
\tag{172.H14}
\]

Also \(|\Delta K|\le K_{R'}^{(2)}+K_R^{(2)}\), so every absolute-frequency
majorant, and every dual positive majorant which dominates the exact
transform, returns (172.H2).

This capacity is sharp for the coefficient-uniform interface.  Take
\(M=4P\), support \(z_N=1\) on the \(2P\) even sites in
\([0,M-1]\), and zero elsewhere.  Equivalently, take the diagnostic
coefficient \(c_N=e(-J\sqrt N)\) on that parity class.  Then
\(D_L=2P\), and for \(r=2s\),

\[
 A_{2s}=2P-s.
\]

For the doubling link \(R=2P\), \(R'=4P=M\), restrict the tent to
\(P\le s\le3P/2\).  On this range
\(w_M(2s)-w_R(2s)\ge1/4\) and \(A_{2s}\ge P/2\).  Hence

\[
 \mathfrak E_M^{(2)}-\mathfrak E_{M/2}^{(2)}
 =2\sum_s\{w_M(2s)-w_{M/2}(2s)\}A_{2s}
 \gg P^2\asymp M D_L\asymp L^4.
\tag{172.H15}
\]

This falsifies only coefficient-uniform routes.  It is not the literal
residual coefficient and gives no physical lower bound.

At the opposite extreme, a one-site sequence has
\(\mathfrak E_R^{(2)}=D_L\) for every \(R\), so every increment is exactly
zero.  Thus any transformed calculation which leaves a positive
“diagonal” contribution on this control is missing a compensating zero,
boundary, or dual off-diagonal term.

### 3.5 No-pair control and collar self-return

On a no-pair row whose odd prime factors are all \(1\bmod4\), every
surviving odd divisor has \(\chi_4(d)=1\).  Moreover, on the accepted
cofactor-gcd parametrization the character product is frozen for every
even shift, including the squarefree even-even branch.  Therefore a
proof which attributes the factor \(L\) to termwise character balance
within each product or even-shift row also proves a false positive-sign
analogue.  Any saving must use the complete signed coupling across rows,
frequencies, or cells together with the nonlinear phase.

For a simultaneous smooth transform, differentiating (172.H3) gives
(172.H4).  At \(\varphi=0\), the stationary equations return

\[
 k\ell=XQR,\qquad Q\ell\le Rk\le4Q\ell,
\]

and the accepted collar
\[
 |k\ell-XQR|\ll QRJ/L.
\]

The second peak has the same centred phase after the exact sign
\((-1)^N\) is placed in the odd/even amplitude.  For a top doubling
bandpass, \(\Delta K^{(2)}(0)\asymp M\), and the same holds at \(1/2\);
on sufficiently small arcs of width \(c/M\) the bandpass remains of that
size.  Since \(uv\asymp L^2\), the perturbation
\(\varphi uv\) is only \(O(1)\) on those arcs.  Thus no uniform
integration-by-parts or nondegenerate-Hessian gain occurs there.

The accepted positive smooth-collar ledger is still

\[
 \frac{L^{3/2}}{QR\sqrt J}
 \left(\frac{QRJ}{L}+1\right)X^\varepsilon
 \asymp \sqrt{JL}\,X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\tag{172.H16}
\]

This is a scalar route capacity, distinct from the maximal energy capacity
\(MD_L\asymp L^4X^\varepsilon\).  Neither is physical mass.  They agree
only in the hostile conclusion: positive dual summation supplies no new
factor-\(L\) mechanism.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in the parity, endpoint, telescoping,
tent, Haar, or literal common-frequency transform identities.
Equations (172.D13)--(172.D15) establish the complete transform with exact
constants \(i/2\) and \(1/8\).  Their ordinary-zero sector is target-safe
only as one fully recombined character-frequency expression; no
termwise-\(k\) safety is asserted or needed.

The first unproved affirmative step is exactly the fully signed nonzero
ordinary-frequency aggregate

\[
 \boxed{\mathcal A_{\ne0}^{\rm rem}(\Delta K)
 \ \text{of (172.D23)}
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{172.H17}
\]

It retains every odd character frequency, every nonzero ordinary
frequency, both Fejer peaks, all cross terms, Möbius openings, residual
selectors, boundary and transition cells, and one aggregate real part.
The first rigorous route-specific failure is taking an absolute value or
positive norm over any of those indices or over \(\theta\) before proving
the missing factor \(L\): (172.H2) and (172.H15) then restore \(L^4\).

## 5. Required control tests and outcomes

Here PASS means that the audit accounts for the control.  FAIL means that
the proposed proof gate is not met; it does not mean that the physical
target is false.

| Required control | Outcome |
|---|---|
| literal_residual_coefficient_domain | **PASS.** The physical opening is multiplicity one, and (172.D13)--(172.D15) retain the complete literal residual domain in the transformed family. |
| one_outer_real_part | **PASS through (172.D23); FAIL after premature positivity.** A dual/cell modulus before the estimate of (172.D23) discards the licensed aggregate real part. |
| even_parity_fejer_projection | **PASS.** The average of the two Fejer peaks keeps exactly even gaps with their original weights. |
| integer_doubling_chain_and_final_link | **PASS.** Telescoping is exact; (172.H8), not Haar rounding, owns the terminal non-doubling link. |
| short_shift_correction_once | **PASS.** Equation (172.H6) is the only correction and costs at most \(R_0D_L\ll L^3X^\varepsilon\). |
| triangular_tent_zero_diagonal | **PASS.** Equations (172.H8) and its doubling specialization have zero diagonal. |
| haar_detail_identity_scope | **PASS with scope.** Equation (172.H10) uses absolute-site parity and only an exact doubling link; positivity of \(\mathfrak H_R^{(2)}\) supplies no saving. |
| finite_character_poisson_common_frequency | **PASS exactly.** Equations (172.D13)--(172.D15) give the literal residual common-frequency transform with constants \(i/2\) and \(1/8\). |
| original_zero_boundary_transition_modes | **PASS as an exact ledger; open only inside (172.D23).** The ordinary-zero sector is target-safe after full signed \(k\)-recombination, not termwise in \(k\); all remaining literal boundary and transition modes stay in the nonzero aggregate. |
| dual_off_diagonal_before_positive_sum | **FAIL as the target estimate.** Physical diagonal cancellation is not dual-diagonal cancellation.  The fully signed nonzero ordinary-frequency aggregate (172.D23) is still open. |
| selected_and_no_pair_rows | **PASS in the exact transform; FAIL for a character-only saving.** No-pair positive-character rows survive. |
| squarefree_coprimality_and_two_adic_branches | **PASS in the exact transform; FAIL for a disjoint \(Q,R\) reading.** Möbius openings overlap with signs, and the even complementary factor and \(p=2\) term remain. |
| profile_endpoint_and_zero_extension | **PASS in the exact transform; FAIL for global smooth replacement.** Cardinal endpoints and jumps are retained in (172.D13)--(172.D23) and cannot be discarded. |
| dechirped_phase_aligned_array | **PASS as falsification.** Equation (172.H15) attains \(L^4\) capacity on one parity class. |
| one_site_normalization | **PASS.** Every dyadic increment is exactly zero; an isolated positive transformed diagonal is spurious. |
| no_pair_positive_character_control | **PASS as falsification.** All-\(1\bmod4\) no-pair rows rule out assumed per-row \(\chi_4\) cancellation. |
| global_parseval_RD_L_no_go | **PASS.** Equations (172.H2) and (172.H14) stop at \(RD_L\), which is \(L^4X^\varepsilon\) at the top. |
| collar_self_return_and_restored_power | **PASS as a no-go; FAIL as a target bound.** Both peak centres have rank-one Hessian and return to (172.H16). |
| factor_L_before_positive_norm | **FAIL.** No factor \(L\) is proved before a dual, cell, opening, or frequency positive norm. |
| residual_only_owner_quarantine | **PASS.** Even (165.K26) would close only the complete residual \(t=1\) scalar through its accepted connectors. |
| no_in_round_pivot | **PASS.** No K17a, BAL, other hard-TOP channel, or global owner is substituted. |
| no_status_or_exponent_overpromotion | **PASS.** No target, parent, bridge, theorem, or exponent is promoted. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This report used only the assigned brief and the following permitted
artifacts:

1. protocol.md;
2. state/proof_obligations.yml, parsed at the graph hash displayed above;
3. state/active_campaign.yml;
4. strategy/round172_m2_hard_top_t1_residual_maximal_fejer_dyadic_strategy.md;
5. rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/barrier_packet.md;
6. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
7. rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/short_shift_arithmetic_hostile_audit.md;
8. proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
9. rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/reports/signed_spectral_reciprocity_source_hostile_audit.md;
10. rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/reviews/conductor_round169_adjudication.md; and
11. rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reviews/dependency_power_selection_seam_review.md.

This repaired version additionally adopts the independently reviewed
Round-172 discovery identities (172.D13)--(172.D15) and the exact open
aggregate (172.D23), as supplied in the conductor's local-repair
instruction.  No sibling file was otherwise inspected.  No shared
synthesis, validation matrix, proof draft, web source, or computation was
used.

## 7. Recommended state effect

**Recommended effect: retain the exact dyadic identities and the exact
literal transform (172.D13)--(172.D15) as candidate evidence, record the
scoped positive-control no-go, and make no proof graph change from this
hostile report alone.**

The transform gate itself passes.  Do not promote (172.D23), (165.K26), a
strict spectral sector, the residual scalar, the complete \(t=1\) face,
hard TOP, M9--M2, M9, either bridge, the quarter theorem, or either
exponent.

If the complete signed estimate (172.D23), equivalently (172.H17), is not
proved, close
Round 172 under
\(\texttt{maximal\_fejer\_dyadic\_character\_poisson\_no\_go}\).  Park
only:

- deleting either Fejer peak or the even complementary branch;
- identifying an ordinary dual zero mode with the physical diagonal;
- estimating the target-safe ordinary-zero sector termwise in the odd
  character frequency \(k\), rather than after its full signed
  recombination;
- a uniform nondegenerate-Hessian treatment across either peak centre;
- positive summation over dual modes, Möbius openings, product cells, or
  boundary pieces before the factor-\(L\) saving; and
- a second bare transform or the accepted positive product collar.

The exact open possibility is an actual-coefficient theorem for the single
signed nonzero ordinary-frequency family (172.D23), with an owner-complete
complement and all literal modes retained.  The dechirped, one-site, and
no-pair controls are route diagnostics only and must not be promoted to
physical lower bounds.
