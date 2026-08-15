# 1. Result

The global nonsaddle signed-section estimate survives hostile audit after
one normalization repair: use the intrinsic height scale

\[
 R=\langle\alpha\rangle=(1+|\alpha|^2)^{1/2},
\]

not \(\lambda\), in the global gamma-symbol and physical-height
decomposition.  On every subordinate inner or outer cell, for both signs
of \(\alpha\), the complete phase-removed after-Plemelj section satisfies

\[
 |\mathcal P|\ll P_XR^{\kappa-2},\qquad
 |\partial_L\mathcal P|\ll P_XR^{\kappa-3},
\]

\[
 |\mathcal Q|\ll P_XR^{\kappa-1},\qquad
 |\partial_L\mathcal Q|\ll P_XR^{\kappa-2},              \tag{47H.1}
\]

with the corresponding integrated moving-trace estimates.  Here
\(P_X\ll\log^C(2X)\), and the signed diagonal is evaluated as a logarithm
before absolute values.  These estimates imply the required nonsaddle
radial-BV bound and the two true outer boundary limits.

The repaired middle partition is also covered by the accepted
fixed-ratio theorem.  That theorem is invariant under multiplication by
any fixed smooth scaled cutoff with bounded seminorms; because the total
middle cutoff equals one near the saddle, its stationary coefficient is
unchanged.  Thus literal equality with an earlier named cutoff is not
needed.

# 2. Exact statement and hypotheses

Assume exactly the lines, gamma factors, profiles, signed section,
physical endpoints, scale identities, and ownership conventions in the
Round-47 packet.  In particular \(\kappa<1\),
\(p^{(m)}(\nu)\ll P_X(1+|\nu|)^{-3}\) for \(m\le3\), and

\[
 \Psi'(L)=\log(|\alpha|/\lambda),\qquad
 \Psi''(L)=1/\alpha .                                  \tag{47H.2}
\]

All nonsaddle cutoffs are fixed smooth functions of
\(t=|\alpha|/\lambda\).  Their \(L\)-derivatives are
\(O(\lambda^{-1})\), supported where \(R\asymp\lambda\), and their exact
radial derivative is

\[
 x\partial_x c(t)=-\frac t2c'(t)=O(1).                 \tag{47H.3}
\]

The conclusion is (47H.1), including the finite-section upper and lower
traces, uniformly in all actual indices.  It also includes

\[
 \frac{\eta_{\rm ns}\mathcal P}{\Psi'}\longrightarrow0,
 \qquad
 \frac{\eta_{\rm ns}\mathcal Q}{\Psi'}\longrightarrow0
 \quad (|L|\to\infty),                                \tag{47H.4}
\]

and the normalized radial-BV estimate of the packet.

# 3. Proof or derivation

Signed Stirling on either half-line, with the exact linear
\(e^{i\omega_LL}\) phase retained, gives the global symbol bounds

\[
 \left|\partial_L^m\left{R^{-\kappa}e^{-i\Psi(L)}
 R_\alpha(\alpha)e^{i\omega_LL}\right\}\right|
 \ll R^{-m},\qquad m\le2.                              \tag{47H.5}
\]

On bounded \(R\), this is compact gamma control; on large \(R\), it is
the differentiated gamma-ratio expansion.  The constants are uniform for
both signs.  Repeating the accepted four-region physical-height split
with \(R\) in place of the fixed-ratio scale separates the physical
center, top diagonal, radial ridge, and far tail because
\(y+(2\alpha-y)=2\alpha\).  The endpoint divided differences then give

\[
 \int |K_\Delta|\,d\nu\ll P_XR^{-2},\qquad
 \int |\partial_LK_\Delta|\,d\nu\ll P_XR^{-3},          \tag{47H.6}
\]

after removal of the factor \(R^\kappa\).  The radial ridge contributes
only \(O(P_XR^{-4}\log(2+R))\).  Smooth translated profiles have an
additional inverse power.  The same region split on \(\nu=L\pm U\)
proves the moving-trace bounds; upper faces have positive sign, lower
faces negative sign, affine formulas agree at switches, and collapsed
sections cancel.

The diagonal is never put under an absolute Cauchy integral.  From the
exact logarithmic formula (47.5d), its coefficient is
\(G(L)p(L)/A(L)\).  Since \(p(L)\ll P_XR^{-3}\) and
\(|A(L)|\asymp R\), the diagonal is
\(O(P_XR^{\kappa-4}\log(2+R))\), uniformly over physical finite
sections.  Endpoint differentiation loses at most one of its two spare
powers.  Its symmetric limit is exactly the signed value (47.5e), so no
absolute \(1/|L-\nu|\) divergence is introduced.

The phase-conjugated \(x\)-derivative has exactly one height loss.  With
\(y=L-\nu\), the packet's identities give

\[
 \eta=\alpha-\frac y2,
 \qquad
 \frac{\eta p(\nu)-\alpha p(L)}{y}
 =\alpha\frac{p(\nu)-p(L)}y-\frac12p(\nu).          \tag{47H.7}
\]

Thus it is a multiple of the already controlled endpoint difference plus
one ordinary profile term; no stationary numerator appears.  Equations
(47H.6)--(47H.7) prove the last two bounds in (47H.1), and a further
fixed-\(\nu\) derivative gives \(R^{\kappa-2}\).  The diagonal and smooth
shares are smaller.  Formula (47H.3) accounts for the moving ratio
cutoffs without an extra power.

For the inner cell, (47H.1) and one phase integration by parts are
integrable because \(\kappa-2<-1\); the curvature term has one further
\(R^{-1}\).  For the outer cell, the differentiated \(\mathcal Q\) and
\(\mathcal Q\Psi''\) are both \(O(P_XR^{\kappa-2})\), again integrable.
Moreover \(R^{\kappa-2}/\log(R/\lambda)\to0\) and
\(R^{\kappa-1}/\log(R/\lambda)\to0\), proving (47H.4).  The fixed compact
inner collar is handled directly.

Finally, multiplication of the fixed-ratio product theorem by a smooth
middle cutoff preserves every mixed norm by Leibniz, since its derivatives
are \(O(\lambda^{-m})\).  The exact Morse BV argument is likewise stable
under such multiplication.  Summing the middle cutoffs leaves value one
at the saddle, so the leading Fresnel coefficient is unchanged; the
difference is a fixed-ratio nonsaddle remainder.  This proves cutoff
invariance for the repaired middle partition.

# 4. First doubtful or unproved step

No doubtful analytic step remains inside the frozen Round-47 interface.
The essential correction is that a global proof must normalize and split
at \(R=\langle\alpha\rangle\); extending the fixed-ratio
\(\lambda^{-2}\) norm verbatim to the inner or outer cells would be
false bookkeeping.  Likewise, replacing (47H.7) by the crude bound
\(|\eta|\le |L|+|\nu|\) would discard the endpoint cancellation and would
not prove radial BV.

This report does not re-prove upstream ownership identities or infer the
complete beta-transition, M9-M1, M9, or Gauss-circle theorem.  Those are
downstream graph operations.

# 5. Required control tests and outcomes

1. **Global gamma, both signs: pass.**  Compact control plus signed
   differentiated Stirling gives (47H.5).
2. **Signed Plemelj order: pass.**  The diagonal is evaluated by the
   exact logarithm and symmetric limit before absolute values.
3. **Diagonal/off-diagonal/smooth split: pass.**  The diagonal has two
   spare powers; (47H.6) controls the divided difference; smooth shares
   are smaller.
4. **Exact x derivative: pass.**  Identity (47H.7) shows precisely one
   \(R\)-loss, while (47H.3) includes the ratio-cutoff derivative.
5. **Moving faces and outer limits: pass.**  Endpoint signs, switches,
   collapsed sections, trace norms, and (47H.4) are all controlled.
6. **Inner/outer lambda uniformity: pass.**  \(R\) is the analytic scale;
   cutoff derivatives occur only at \(R\asymp\lambda\).
7. **Middle cutoff interface: pass.**  Smooth-scaled-cutoff invariance
   follows by Leibniz and exact Morse BV, with unchanged total saddle
   value.
8. **Raw ledger: pass.**  The untouched sums
   \(\sum h^{-r}q^{-p}\) converge (also with one logarithm), there are
   \(O(\log X)\) scales, the displayed \(D_j,H_j\) factors are harmless,
   and the radial-BV implication consumes the single \(\sqrt X\) radial
   factor.  Floors, stars, character, equality, collision, and contour
   ownership remain once.  The exterior \(X^{1/4}\) operator is restored
   once, yielding \(O(X^{1/4}\log^C(2X))\) for this physical contribution.
9. **Experiment/source control: pass.**  No numerical experiment,
   computer algebra, web theorem, or unlisted source was used.

# 6. Dependencies and exact artifacts used

This clean replacement used only:

1. `rounds/codex-managed/m9-m1-beta-global-nonsaddle-signed-section/derivation_packet.md`;
2. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/cauchy_tail_hostile_audit.md`;
3. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/reports/product_cell_hostile_audit.md`;
4. `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/synthesis.md`;
5. `rounds/codex-managed/m9-m1-beta-global-nonsaddle-signed-section/briefs/global_section_hostile_audit.md`.

No graph, state file, protocol file, Round-47 claimant/review, Round-46
report, numerical experiment, external source, or other artifact was
read.

# 7. Recommended state effect

**Promote** the global direct nonsaddle signed-section/radial-BV theorem
with the \(R=\langle\alpha\rangle\) normalization, exact phase-conjugated
\(x\)-derivative, finite-section trace controls, outer boundary limits,
and untouched raw ledger.

**Promote** smooth-scaled-cutoff invariance as the precise seam from the
repaired middle aggregate to the accepted fixed-ratio saddle/entry/exit
theorem.  Reject use of a stationary numerator on nonsaddle cells, a
global \(\lambda^{-2}\) symbol norm, pre-Plemelj absolute values, or a
crude independent estimate of \(\eta p(\nu)\) and \(\alpha p(L)\).

Retain only the downstream assembly obligations open.
