# Blind pointwise/transversality feasibility report

## 1. Result: statement-only no-go

**No-go lemma.**  Under only (132.S1)--(132.S10), the Demeter--Wu
bilinear estimates do not imply a bound

\[
 |\mathfrak O_{i,D}^{+}(c)|\ll Y^{27/48-\sigma+\varepsilon}
 \qquad(\sigma>0)
\]

or any other fixed-centre bound having a strict cross-ray power.  There are
three independent obstructions.

1. The literal determinant range is narrow in a ruling coordinate.  In the
   bounded-condition affine normalization of the whole top shell, every
   allowed pair has separation at most \(Y^{-5/48}\) in one hyperbolic
   coordinate, whereas (132.S1) requires separation comparable to one in
   both coordinates.  Same-denominator pairs lie exactly on one ruling.
2. The literal pair coefficient is a matrix depending jointly on the outer
   and inner ray.  A product \(f_1\overline {f_2}\) has a rank-one coefficient
   matrix.  The always-valid row decomposition forces an absolute sum over
   outer rays (or a positive row energy), so it supplies no cross-ray signed
   cancellation and changes the relevant absolute-value placement.
3. A global band-limited evaluation bridge does turn (132.S2) into a
   pointwise estimate for one already-factorized transverse product, but its
   right side is the positive \(L^4\) square function.  No norm for the
   reassembled inner coefficients is supplied.  The refined estimate has the
   additional positive factor \((M_1M_2)^{1/4}\) after taking square roots.

The first invalid inference is therefore

\[
 \det\nabla^2\Phi_i\ne0
 \quad\Longrightarrow\quad
 \text{the determinant-restricted ray pair satisfies (132.S1)}.
\]

It is false: curvature identifies the surface type, not quantitative
two-coordinate separation.

## 2. Exact statement and hypotheses of the legal implication

Put

\[
 q(u,v)=(u,v,u/v),\qquad x_i=(0,0,c/\kappa_i).
\]

Then the phase in (132.S7) is exactly
\(e(x_i\cdot(q(r)-q(r')))\).  Let

\[
 Q_R(f)=\sum_\theta\|f_\theta\|_4^2.
\]

For functions satisfying all the support and transversality hypotheses of
(132.S2), its weakest pointwise consequence is

\[
 |f_1(x)\overline {f_2(x)}|
 \ll_\varepsilon R^{\varepsilon/2}
 Q_R(f_1)^{1/2}Q_R(f_2)^{1/2}.                 \tag{B1}
\]

This is valid at every fixed \(x\), but only for a genuine product with
separate coefficient ownership.  If a broad part of the literal coefficient
matrix has a transverse rank-one decomposition

\[
 M^{\rm br}_{r,r'}=\sum_s\alpha_s(r)\overline{\beta_s(r')},
\]

then (B1) and the triangle inequality give only the conditional projective
bound

\[
 |\mathfrak O^{\rm br}_{i,D}(c)|
 \ll_\varepsilon R^{\varepsilon/2}
 \sum_s Q_R(F_{\alpha_s})^{1/2}Q_R(F_{\beta_s})^{1/2}.       \tag{B2}
\]

No bound for the quantity on the right of (B2) is in the packet.  The
always-available decomposition is by rows.  Writing \(G_r\) for the inner
extension function whose coefficients retain the literal \(r\)-dependent
owners, it yields

\[
 |\mathfrak O^{\rm br}_{i,D}(c)|
 \ll_\varepsilon R^{\varepsilon/2}
 \sum_r |A_i(r)|Q_R(F_r)^{1/2}Q_R(G_r)^{1/2}.                \tag{B3}
\]

One may apply Cauchy--Schwarz and (132.S9) to (B3), obtaining

\[
 |\mathfrak O^{\rm br}_{i,D}(c)|
 \ll_\varepsilon R^{\varepsilon/2}(D/L)^{1/2}Y^\varepsilon
 \left(\sum_r Q_R(F_r)Q_R(G_r)\right)^{1/2},                \tag{B4}
\]

but (B4) is a positive row-energy bound, not a signed cross-ray estimate,
and its inner factor is uncontrolled.  Equations (B1)--(B4), subject to an
explicit Fourier thickening, are the weakest legal implications of the
source statement for the target packet.

For (132.S4), even after a valid localized point-evaluation bridge, the
corresponding product bound would be

\[
 |f_1(x)\overline {f_2(x)}|
 \ll_\varepsilon R^{\varepsilon/2}(M_1M_2)^{1/4}
 \prod_{j=1}^2
 \left(\sum_{T\in\mathbb T_j}\|f_T\|_4^4\right)^{1/4}.     \tag{B5}
\]

Thus refinement penalizes high local multiplicity; it does not itself give
a negative cross-ray power.

## 3. Proof and derivation

### 3.1 Exact hyperbolic normalization

The frequency surface is not merely approximately hyperbolic.  If
\(z=u/v\), then it satisfies \(vz=u\).  Fix a shell centre
\((u_0,v_0,z_0)\), put

\[
 s=v-v_0,\quad t=z-z_0,\quad w=u-u_0,
\]

and define

\[
 \xi={s\over D},\qquad
 \eta={t\over L/D},\qquad
 \rho={w-v_0t-z_0s\over L}.
\]

Expanding \((v_0+s)(z_0+t)=u_0+w\) gives
\(w-v_0t-z_0s=st\), hence

\[
 \rho=\xi\eta.                                             \tag{B6}
\]

This is an exact affine map to \(\mathbb H\), with both shell coordinates
bounded.  It verifies the surface type but says nothing about whether two
arithmetic patches are transverse.

### 3.2 The determinant restriction is narrow

For a literal pair,

\[
 |\eta(r)-\eta(r')|
 ={D\over L}\left|{a\over b}-{a'\over b'}\right|
 ={D\over L}{n\over bb'}
 \ll {D\over LW}=Y^{-5/48}.                                \tag{B7}
\]

Thus every nonzero determinant pair is close in the \(\eta\) ruling
coordinate under any bounded-condition normalization of the full shell.
Even if \(|b-b'|\asymp D\), so that the \(\xi\) coordinates are separated,
(132.S1) still fails in \(\eta\).  If \(b=b'\), then \(\xi=\xi'\) exactly,
so both points lie on the affine line obtained by holding \(v\) fixed.  No
affine change of coordinates can turn two points on one ruling into a
transverse pair.

For a determinant band \(n\asymp N\), the small separation is
\(\delta_N\asymp N/(DL)\).  Magnifying it to unit size would require a
pair- or band-dependent anisotropic rescaling by \(\delta_N^{-1}\).  The
packet supplies no resulting Fourier thickness, physical scale, cap
partition, Jacobian, or coefficient reassembly.  At the original shell
scale, merely resolving this separation by \(R^{-1/2}\)-caps would require

\[
 R\gtrsim (DL/N)^2,
\]

ranging from \(Y^{5/24}\) at \(N=D^2/W\) to \(Y^{4/3}\) at \(N=1\).
Cap separation is in any case weaker than the two-coordinate transversality
required by (132.S1).

### 3.3 Fixed-point bridge and coefficient ownership

For normalized transverse functions, the Fourier support of
\(f_1\overline {f_2}\) lies in a fixed bounded set.  Choose a fixed kernel
\(K\) whose Fourier transform equals one on that set.  Then

\[
 |f_1(x)\overline {f_2(x)}|
 \le \|K\|_2\|f_1\overline {f_2}\|_2,
\]

and (132.S2) proves (B1).  This bridge has no negative power: all arithmetic
content has moved into the positive quantities \(Q_R(f_j)\).

The literal coefficient
\(M_{r,r'}=A_i(r)H_{i;r,p}(n)C_{i;r,p}(n)\), including its support and owner,
depends on both indices.  A single product has coefficients
\(\alpha(r)\overline{\beta(r')}\).  Without a controlled rank-one
decomposition, applying (B1) row by row proves only (B3); applying outer
Cauchy proves only (B4).  Neither operation supplies signed cancellation.
For the refined inequality, a local reproducing argument must additionally
be justified inside the chosen set \(X\); after that justification, taking
the square root of (132.S4) gives (B5).

## 4. First doubtful or unproved step

The first false step is the replacement of the hypothesis (132.S1) by the
curvature identity (132.S10).  Formula (B7) directly falsifies that
replacement.  A claimed rescue by determinant-band rescaling would still
have to prove, in this order:

1. an anisotropic Fourier thickening and an \(R^{-1/2}\)-cap map compatible
   with the source's isotropic \(N_{1/R}(\mathbb H)\) hypothesis;
2. a decomposition of the pair-dependent physical coefficient matrix whose
   projective/square-function norm is bounded without moving a modulus or an
   absolute value;
3. the fixed-centre evaluation bridge with its localization norm;
4. a separately priced estimate for the ruling-aligned narrow part.

None of these hypotheses is supplied.  In particular, (132.S2) or
(132.S4) cannot be applied directly to the discrete scalar, and an estimate
for a positive square function cannot be identified with cancellation in
the literal signed scalar.

## 5. Control tests and outcomes

| Control | Exact input and outcome | Implication |
|---|---|---|
| `hyperbolic_surface_normalization` | The affine coordinates above give the exact identity \(\rho=\xi\eta\). | Surface normalization passes; it does not establish transversality or a Fourier thickening. |
| `transversality_in_both_coordinates` | Equation (B7) gives \(|\Delta\eta|\ll Y^{-5/48}\); same denominator gives \(\Delta\xi=0\). | The literal full-shell pair support is narrow, so (132.S1) is unavailable. |
| `Fourier_support_thickness_and_cap_scale` | The arithmetic exponentials are point frequencies, whereas the theorem needs functions supported in \(N_{1/R}(\mathbb H)\).  No \(R\) or bump normalization is supplied.  A standard amplitude-one cap wave packet occupies volume \(\asymp R^2\), so \(\|f_T\|_4^2\asymp R\). | Point evaluation/localization is not free, and no \(Y\)-exponent can be extracted from the stated data. |
| `fixed_centre_scalar_vs_bilinear_L4_integral` | For a factored transverse product the global kernel argument proves (B1).  Conversely, translate two transverse amplitude-one tubes so that they cross at the prescribed point.  Their product there is one for every chosen centre, while each standard packet has \(\|f_T\|_4^2\asymp R\). | The integral theorem permits concentration at the fixed centre and supplies no negative pointwise power. |
| `actual_coefficient_norm_and_absolute_value_direction` | The physical coefficient is a general pair matrix.  Row decomposition gives (B3); outer Cauchy gives the uncontrolled positive energy (B4).  No inner \(\ell^2\), nuclear, or projective norm is supplied. | No coefficient-preserving cross-ray estimate follows. |
| `broad_narrow_ruling_partition` | The whole determinant band is \(\eta\)-narrow in the shell normalization.  Pair-dependent rescaling, even if completed, leaves exact rulings narrow. | A broad estimate cannot be a complete bound without a new narrow theorem. |
| `same_denominator_M1_M2_aligned_packets` | Fix an interior outer ray and use the supplied legal packet with \(b'=b\) and length \(q=D/W=Y^{3/48}\).  It lies on one ruling.  At the legal centre \(c=\kappa_i b^2\), its geometric phases are \(e(c(a-a')/(\kappa_i b))=1\); the packet also has the stated coherent M1/M2 carrier. | Curvature gives no per-ray cancellation.  Termwise narrow pricing costs a factor \(q=Y^{3/48}\).  This is a local hostile control, not a lower bound for the full scalar. |
| `capacity_35_27_24_over_48` | The supplied complete capacity is \(35/48\), the ideal floor is \(27/48\), and the determinant target is \(24/48\).  The source constant is only \(R^\varepsilon\).  The narrow packet's possible triangle cost is \(+3/48\), exactly opposite to the \(-3/48=-1/16\) saving needed from the ideal floor to the determinant target. | The theorem alone does not reach, let alone beat, \(27/48\).  Applying the local narrow factor to an ideal one-term scale would price it at \(30/48\), but no global lower bound is asserted. |
| `no_positive_energy_or_global_promotion` | (B2)--(B5) are positive norm bounds and the narrow term is open. | They are conditional diagnostics only; no global exponent, endpoint, bridge, or quarter claim is promoted. |

The aligned packet uses no adversarial replacement of the physical
coefficients: it tests only the geometric phase and the carrier coherence
explicitly supplied.  Remaining Mobius/Stieltjes cancellation would require
a separate arithmetic result and is not inferred or denied here.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/briefs/blind_pointwise_transversality_feasibility.md`;
- `problems/gauss_circle.md`;
- `state/control_models.md`;
- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/blind_statement.md`.

The Demeter--Wu statements used above are exactly (132.S1)--(132.S4) as
quoted in `blind_statement.md`.  No proof graph, proof draft, strategy,
campaign plan, active-campaign state, nonblind artifact, sibling report,
web source, or numerical experiment was used.

## 7. Recommended state effect

**Retain** this as candidate no-go evidence: reject any claim that
(132.S2) or (132.S4), from the supplied hypotheses alone and with literal
coefficient ownership, yields a fixed-centre strict cross-ray power.
Recommend no shared-state or global-exponent change.  A future attempt would
need a source-checked anisotropic determinant-band theorem, a controlled
factorization norm for the physical coefficient matrix, and an independent
same-ruling narrow estimate.
