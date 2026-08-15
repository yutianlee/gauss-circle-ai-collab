# 1. Result

**Final fresh audit: the global nonsaddle signed-section estimate closes;
the middle-cutoff seam does not.** With (47.5c)--(47.5e), the complete
symmetric-limit section is quantitatively determined. The off-diagonal
divided difference supplies two inverse-alpha powers, its
phase-conjugated x derivative supplies one inverse-alpha power, the smooth
shares are smaller, and the exact diagonal limit is smaller still. The
moving finite-section faces are uniformly integrable and vanish under
symmetric exhaustion. Thus the returned inner and outer nonsaddle groups
satisfy the weaker mixed theorem in (47.13), including the true outer
limits and the untouched coefficient/radial ledger.

The decisive x-derivative identity is

\[
 x\partial_x\{G(L)(p(\nu)-p(L))\}
 =-iG(L)\{\eta p(\nu)-\alpha p(L)\}.              \tag{R47.1}
\]

The numerator on the right must remain combined; splitting it before the
nu-tail estimate destroys its cancellation.

One substantive seam remains. The packet explicitly does not identify the
middle subordinate cutoff with the accepted fixed-ratio saddle/entry/exit
cutoffs and does not state a cutoff-invariance theorem. Therefore the
global nonsaddle theorem can be promoted as a scoped lemma, but the full
positive-line localization certificate cannot yet be promoted.

# 2. Exact statement and hypotheses

Interpret the packet's “beta slab” and fixed mask \(\psi\) in the standard
project sense: \(\psi\) has fixed compact support, so
\(R_\beta(\beta)\psi(\beta)\) and its required finite derivatives are
\(O(1)\). Also interpret “rapidly decreasing with the required finite
derivatives” as uniform Schwartz bounds for the finitely many actual
regular profiles. These two conventions should be cited explicitly in any
promoted statement.

Let \(\mathcal P_\infty\) be the phase-removed symmetric limit of the
complete section defined by (47.3)--(47.5e), and let

\[
 \mathcal Q_\infty=e^{-i\Psi}x\partial_x
 (e^{i\Psi}\mathcal P_\infty).
\]

Then, uniformly in the actual indices and on both alpha signs,

\[
 |\mathcal P_\infty|
 \ll P_X\langle\alpha\rangle^{\kappa-2},\qquad
 |\partial_L\mathcal P_\infty|
 \ll P_X\langle\alpha\rangle^{\kappa-3},          \tag{R47.2}
\]

\[
 |\mathcal Q_\infty|
 \ll P_X\langle\alpha\rangle^{\kappa-1},\qquad
 |\partial_L\mathcal Q_\infty|
 \ll P_X\langle\alpha\rangle^{\kappa-2},         \tag{R47.3}
\]

where \(\langle y\rangle=1+|y|\) and
\(P_X\ll\log^C(2X)\). The finite off-diagonal moving-face contributions
to the L derivatives converge to zero in \(L^1(dL)\); for \(T\ge2\),
their singular-top sizes are bounded schematically by

\[
 O(P_XT^{\kappa-2})\quad\text{for }\mathcal P,
 \qquad
 O(P_XT^{\kappa-1})\quad\text{for }\mathcal Q.    \tag{R47.4}
\]

Both tend to zero because \(\kappa<1\). Smooth-face contributions decay
faster than any required power. The diagonal faces converge to the
explicit limit (47.5e) and obey stronger alpha decay.

If \(\eta_{\rm ns}\) is the accepted sum of the inner and outer subordinate
weights, the corresponding normalized amplitude satisfies

\[
 \sup_{1\le x\le N_X}|\mathcal A_{\rm ns}(x)|
 +\int_1^{N_X}|\mathcal A_{\rm ns}'(x)|\,dx
 \ll\log^C(2X).                                   \tag{R47.5}
\]

This statement does not identify or estimate the middle group by the
accepted Round-41 theorem; that interface remains a separate hypothesis.

# 3. Proof or derivation

Stirling's formula on fixed vertical lines gives on either alpha sign

\[
 |R_\alpha(\alpha)|\asymp\langle\alpha\rangle^\kappa,
 \qquad
 |R_\beta(\beta)|\asymp
 \langle\beta\rangle^{3/4-\zeta/2}.              \tag{R47.6}
\]

The first exponent equals

\[
 \frac{1+\sigma+\zeta/2}{2}
 -\frac{2-\sigma-\zeta/2}{2}
 =\frac34+\frac\zeta2=\kappa.
\]

After removal of the exact one-factor phase, logarithmic Stirling
differentiation yields

\[
 |\partial_L^m(e^{-i\Psi}R_\alpha e^{i\omega_LL})|
 \ll\langle\alpha\rangle^{\kappa-m},qquad 0\le m\le2,       \tag{R47.7}
\]

outside a fixed compact alpha collar; the collar is harmless. This is an
unnormalized global estimate. One must not extrapolate boundedness of
(47.9) to the far outer region, where that normalized symbol grows like
\((|\alpha|/\lambda)^\kappa\).

On the fixed beta slab,

\[
 |D(L,\nu)|\asymp1+|\alpha+\nu|.
\]

Put \(A=\langle\alpha\rangle\). Split the nu line into the central region
\(|\nu|\le A/2\), neighborhoods of \(\nu=L\) and
\(\alpha+\nu=0\), and the remaining tails. In the central region the two
denominators in (47.4) are both of size \(A\). Near \(\nu=L\), use

\[
 \frac{p(\nu)-p(L)}{\nu-L}
 =\int_0^1p'(L+t(\nu-L))\,dt.                    \tag{R47.8}
\]

Near \(D=0\), both height values are \(O(P_XA^{-3})\), while
\(|L-\nu|\asymp A\). The far tails have quadratic denominator decay.
Consequently

\[
 \int_{\mathbb R}\left|
 \frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)}\right|d\nu
 \ll P_XA^{-2},                                   \tag{R47.9}
\]

and one L derivative is \(O(P_XA^{-3})\). A possible logarithm near
\(D=0\) occurs only with the smaller size \(A^{-4}\log A\). Multiplying
by (R47.7) proves (R47.2) for the off-diagonal limit.

For the phase-conjugated x derivative, (47.5b) gives (R47.1). Its combined
tail is

\[
 \frac{\eta p(\nu)-\alpha p(L)}{(L-\nu)D(L,\nu)}
 =O\left(\frac{\alpha p(L)}{\nu^2}
         +\frac{p(\nu)}{|\nu|}\right)
 \quad (|\nu|\to\infty).                          \tag{R47.10}
\]

Thus the same split yields

\[
 \int_{\mathbb R}\left|
 \frac{\eta p(\nu)-\alpha p(L)}
 {(L-\nu)D(L,\nu)}\right|d\nu
 \ll P_XA^{-1},                                   \tag{R47.11}
\]

with one L derivative \(O(P_XA^{-2})\). This proves (R47.3) for the
off-diagonal limit. The regular kernels are smaller: the Schwartz factor
\(W(L-\nu)\), height decay of \(p\), and \(D^{-1}\) give the required
powers, while \(|\eta/D|\ll1\) controls their x derivative.

The exact diagonal limit is

\[
 C_\infty[H](L)=i\pi\frac{G(L)p(L)}{A(L)}.         \tag{R47.12}
\]

Since \(|p^{(m)}(L)|\ll P_X\langle L\rangle^{-3}\) for the required
orders and \(L\asymp\alpha\) on the fixed beta slab, (R47.12) is
\(O(P_XA^{\kappa-4})\). Its L derivative is
\(O(P_XA^{\kappa-4})\), which is stronger than (R47.2). Its
phase-conjugated x derivative multiplies the numerator by alpha through
(47.5b), so it and its L derivative are also stronger than (R47.3).
This verifies the diagonal before taking any absolute value of the
original Cauchy section.

It remains to justify the finite faces. For symmetric exhaustion,
(47.5c) becomes

\[
 I_{T,T}(L)=
 \begin{cases}
 [L-T,T],&0\le L\le2T,\\
 [-T,L+T],&-2T\le L\le0,\\
 \varnothing,&|L|>2T.
 \end{cases}                                      \tag{R47.13}
\]

For \(L>0\), the only moving face is \(\nu=L-T\), with
\(L-\nu=T\); the negative side is symmetric. Substitution into (47.4)
and the same three-region split, now in L, gives

\[
 \int_0^{2T}|K_\Delta(L,L-T)|\,dL
 \ll P_X(T^{\kappa-2}+T^{-2}),                    \tag{R47.14}
\]

whereas substitution of the combined numerator (R47.1) gives

\[
 \int_0^{2T}|K_{\Delta,x}^{\rm conj}(L,L-T)|\,dL
 \ll P_X(T^{\kappa-1}+T^{-2}).                    \tag{R47.15}
\]

Both vanish. At smooth moving faces \(W(L-\nu)=W(T)\), so rapid decay
is immediate. Fixed faces have zero L and x velocity, the two affine
descriptions agree at \(L=0\), and the sections collapse at
\(|L|=2T\). Direct differentiation of (47.5d), followed by (47.5e), gives
(R47.12); every face denominator is a displayed \(D\), and the factor
\(p(L)/A(L)\) makes its face terms absolutely integrable. Hence no moving
trace survives the returned limit.

For a subordinate ratio cutoff \(c(t)\),

\[
 t=\frac{|\alpha|}{\lambda},\qquad
 x\partial_xt=-\frac t2,qquad
 \partial_Lt=\frac{\operatorname{sgn}(\alpha)}{\lambda}.    \tag{R47.16}
\]

On transition supports \(t\asymp1\), the x derivative is \(O(1)\) and
the L derivative costs \(O(A^{-1})\). Also
\(D_j\le\sqrt X\), so the actual range has
\(\lambda\ge\pi\). Therefore transition integrals cost at most
\(\lambda^{\kappa-1}\ll1\), uniformly in every lambda regime.

The value contribution is absolutely integrable by (R47.2). For the x
derivative contribution, integrate by parts in L on each nonsaddle sign:

\[
 \int e^{i\Psi}\eta_{\rm ns}\mathcal Q_\infty,dL
 =-\int e^{i\Psi}
 \left{
 \frac{\partial_L(\eta_{\rm ns}\mathcal Q_\infty)}{i\Psi'}
 -\frac{\eta_{\rm ns}\mathcal Q_\infty\Psi''}
 {i(\Psi')^2}
 \right}dL.                                      \tag{R47.17}
\]

Here \(|\Psi'|\ge\log(4/3)\),
\(\mathcal Q_\infty'=O(P_XA^{\kappa-2})\), and
\(\Psi''=1/\alpha\). All terms are integrable because \(\kappa<1\).
The cutoff-derivative terms are controlled by (R47.16). Moreover

\[
 \frac{\eta_{\rm ns}\mathcal P_\infty}{\Psi'}\to0,
 \qquad
 \frac{\eta_{\rm ns}\mathcal Q_\infty}{\Psi'}\to0          \tag{R47.18}
\]

on the true outer ends; the inner group has bounded alpha support for each
lambda. Thus no boundary term remains. The resulting bounds for the value
and \(x\partial_x\) amplitude imply (R47.5), with one extra
\(\log N_X=O(\log X)\) from \(dx/x\).

Finally, \(r,p>1\) close the h and q sums, including the accepted one-log
derivative; (47.2a) gives \(O(\log X)\) scales and bounded scale factors.
Equation (47.2b) then applies to (R47.5). Floors, stars, the character,
collisions, and endpoint coefficients stay attached once, and the exterior
\(X^{1/4}\) physical operator is restored once after the radial estimate.

# 4. First doubtful or unproved step

The first substantive unproved step is no longer global nonsaddle analysis;
it is the **middle-cutoff interface**. The accepted subordinate partition
has a middle weight supported in
\(2/3<|\alpha|/\lambda<3/2\), but the packet supplies neither the literal
Round-41 saddle/entry/exit cutoffs nor a theorem saying that the accepted
fixed-ratio result is invariant under replacement by an arbitrary fixed
smooth subordinate middle partition. Support compatibility alone is not
antecedent equality.

There is one statement-hygiene point before promotion of the scoped global
lemma: the compact support of the beta-slab mask and uniform Schwartz
constants of the regular profiles should be cited rather than left inside
the words “mask”, “beta slab”, and “rapidly decreasing”. This is not a new
analytic obstruction; those are the exact conventions used in the proof
above.

# 5. Required control tests and outcomes

1. **`global_gamma_both_signs`: pass.** Equations (R47.6)--(R47.7) give
   the exact global powers on both signs. The fixed beta-slab convention is
   recorded explicitly in Section 2.
2. **`signed_plemelj_before_absolute`: pass.** The diagonal is evaluated by
   (47.5d)--(47.5e) before absolute estimates, and only the divided
   difference is estimated by ordinary integration.
3. **`diagonal_offdiagonal_smooth_split`: pass.** Equations
   (R47.9)--(R47.12) separately control all three pieces. The diagonal is
   strictly smaller than the target powers.
4. **`phase_conjugated_x_derivative`: pass.** Equation (R47.1) is the exact
   combined numerator, (R47.10) verifies its tail cancellation, and
   (R47.16) includes the ratio-cutoff x derivative.
5. **`moving_faces_and_outer_limits`: pass.** Equations
   (R47.13)--(R47.15) handle the only moving faces; fixed faces, affine
   switches, and collapse are explicit. Equations (R47.12) and (R47.18)
   give the diagonal and oscillatory outer limits.
6. **`inner_outer_lambda_uniformity`: pass.** The phase gap, actual lower
   bound \(\lambda\ge\pi\), and transition cost
   \(\lambda^{\kappa-1}\le1\) are uniform over all actual cells.
7. **`middle_cutoff_interface`: fail.** Neither literal equality nor cutoff
   invariance is present in the statement packet. This is the only
   substantive remaining mathematical seam found by the final audit.
8. **`raw_coefficient_radial_sum`: pass.** The h/q exponents, logarithmic
   scale count, bounded scale factors, normalized BV implication, and
   continuous endpoint coefficients close in the order stated.
9. **`collision_and_external_once`: pass.** The packet assigns the discrete
   and collision modules once, and the exterior operator is restored only
   after (47.2b).

No numerical experiment or external theorem was used. The audit was
entirely analytical.

# 6. Dependencies and exact artifacts used

This was a final fresh statement-only audit after the finite-section repair.
It used only:

- `rounds/codex-managed/m9-m1-beta-global-nonsaddle-signed-section/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-beta-global-nonsaddle-signed-section/briefs/blind_global_section_rederivation.md`.

No proof graph, state file, proof draft, earlier report, synthesis, other
Round-47 artifact, web source, or computational artifact was read. This is
the complete isolation ledger.

# 7. Recommended state effect

**Promote the scoped global nonsaddle signed-section lemma; retain the full
localization certificate as open.** The promoted lemma should state the
beta-slab support and uniform profile conventions explicitly, use the
symmetric-limit section, retain the combined numerator (R47.1), and record
the vanishing moving-face bounds (R47.14)--(R47.15). It yields the inner and
outer normalized radial-BV estimate and the final physical contribution
with the external \(X^{1/4}\) factor applied once.

Do not silently identify the middle group with the accepted fixed-ratio
cells. The next smallest task is either to expose the actual Round-41
cutoffs and verify literal equality, or to prove a cutoff-invariance lemma
whose hypotheses include all cutoff derivatives used by that theorem.
