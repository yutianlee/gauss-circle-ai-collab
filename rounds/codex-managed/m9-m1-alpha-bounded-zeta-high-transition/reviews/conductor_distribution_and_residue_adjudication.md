# Round 49 conductor review: distribution and residue adjudication

## 1. Result

The exact statement that survives all three reports is a scoped reduction, not an estimate.  For

\[
 X_\zeta(A)=2(2\pi)^{-A}\Gamma(A)\cos(\pi A/2),
\]

Mellin inversion against any test function in \(C_c^\infty(0,\infty)\) gives

\[
 \frac1{2\pi i}\int_{(c)}X_\zeta(A)\zeta(A)Y^{-A}\,dA
 =\begin{cases}
 \displaystyle\sum_{n\geq1}\delta(Y-n),&c<0,\\
 \displaystyle\sum_{n\geq1}\delta(Y-n)-1
 =2\sum_{h\geq1}\cos(2\pi hY),&c>0.
 \end{cases}
\tag{49.C1}
\]

The change of line crosses the sole arithmetic pole at \(A=0\), with

\[
 \operatorname*{Res}_{A=0}\zeta(1-A)=-1.
\tag{49.C2}
\]

The actual alpha branch is weighted by

\[
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),
\]

so it is a logarithmic Mellin projection of (49.C1), accompanied by every finite Cauchy--Pompeiu connector, outside face, axis, and corner.  It is not the pure comb.  Moreover, because \(\psi=1\) near zero, the mask and its first and mixed connector derivatives vanish at \(A=0\).  The alpha branch therefore owns no new \(A=0\) or \(R_1\) residue.

## 2. Exact statement and hypotheses

Take the common finite \((u,v,s)\) antecedent of the accepted vector identity, put

\[
 A=s-z/2,\qquad B=s+z/2,\qquad
 \beta=\Im A,\quad \alpha=\Im B,
\]

and retain the actual profiles, floors, stars, radial remainder, finite sides, and one external physical factor.  Let \(\psi\in C_c^\infty(\mathbb R)\) equal one on a neighbourhood of zero.  The alpha arithmetic factor is

\[
 X_\zeta(A)\zeta(A)L(1-B,\chi_4).
\]

At finite height, either use a common Abel regularization of \(\zeta(A)\) or pair the recombined product with a compact Mellin test.  Every contour displacement is made on this same antecedent.  If a smooth mask is used, retain its area connector; if a sharp mask is used, retain both oriented strip edges.

For an outside \(u\)- or \(v\)-height transfer, the mask derivative is

\[
 D=\frac12(\partial_\alpha-\partial_\beta),
\]

and hence

\[
 D\Theta_\alpha
 =\frac12\{(1-\psi(\beta))\psi'(\alpha)
 +\psi'(\beta)\psi(\alpha)\},
\tag{49.C3}
\]

\[
 D^2\Theta_\alpha
 =\frac14\{(1-\psi(\beta))\psi''(\alpha)
 +2\psi'(\beta)\psi'(\alpha)-\psi''(\beta)\psi(\alpha)\}.
\tag{49.C4}
\]

These are the canonical outside-axis connector derivatives.  A horizontal \(A\)-shift uses its own fixed-\((u,v)\) derivative and orientation; the formulas must not be conflated.

## 3. Proof or derivation

On \(\Re A<0\), the ordinary series

\[
 \zeta(1-A)=\sum_{n\geq1}n^{A-1}
\]

converges absolutely.  Pairing the inverse Mellin integral with a compact smooth test permits interchange and gives the positive Dirac comb.  Moving the line to \(\Re A>0\) crosses \(A=0\).  Equation (49.C2) therefore subtracts the constant function one.  The classical inverse Mellin formula for \(X_\zeta\), followed by Poisson summation in the test-distribution sense, gives the cosine representation in (49.C1).  The point \(A=1\) contributes no residue because \(X_\zeta(A)\zeta(A)=\zeta(1-A)\) is regular there.

Multiplication by \(1-\psi(\beta)\) becomes convolution in \(\log Y\), so it does not preserve individual Dirac masses.  Nonholomorphic dependence on height also produces the connector terms (49.C3)--(49.C4) and the oriented finite boundary strata.  Only the complete three-mask sum can cancel these derivatives and recover the unmasked identity.

At \(A=0\), one has \(\beta=0\).  Since \(\psi(0)=1\) and all derivatives of \(\psi\) vanish there, direct substitution in \(\Theta_\alpha\), (49.C3), and (49.C4) gives zero.  Thus the residue \(-1\) belongs to the already accepted global \(R_1\) arithmetic routing and cannot be inserted a second time in alpha.

## 4. First doubtful or unproved step

The first unproved step is not (49.C1); it is the passage of that distributional identity through the actual alpha projector, signed top Plemelj operation, radial remainder, profiles, floors, stars, connectors, finite faces, axes, corner, and the joint outside-height limit.  No accepted theorem says that this complete \(X\)-dependent amplitude is a uniform test family for (49.C1), nor that the Abel limit may be exchanged with the signed Plemelj and height limits.

The discovery report gives a plausible full unmasked physical return, but it is non-isolated and its stronger row-level actual-profile identification was not independently reconstructed.  It is therefore evidence for the next exact target, not part of this promoted lemma.

## 5. Required controls and outcomes

- **Branch orientation: pass.**  Bounded \(\alpha\) leaves the high coefficients \(h^{-A}\) unsigned; \(\chi_4\) remains only in the low \(B\)-factor.
- **Common antecedent and connectors: pass at finite level.**  The blind and hostile reports independently require the area or two strip-edge connectors and every finite side.
- **Pole ledger: pass.**  The only arithmetic line-crossing term is the residue \(-1\) at \(A=0\); \(A=1\) is removable; artificial \(\rho=0\) cancellation still requires common \(E_1+R_1\) ownership.
- **Zero alpha residue: pass.**  \(\Theta_\alpha=D\Theta_\alpha=D^2\Theta_\alpha=0\) at \(A=0\).
- **Integer resonance: pass as a falsifier.**  The Abel cosine comb equals \(2r/(1-r)\) at every integer, so coefficientwise uniform cancellation is false.
- **Radial nonstationarity: fails.**  The minus phase has an interior stationary point, so uniform radial integration by parts cannot close the branch.
- **Height limit: open.**  The absolute capacity retains a positive power of the height.
- **Downstream scope: pass.**  No bound for alpha or any wrapper follows.

## 6. Dependencies and exact artifacts used

This review used the Round 49 derivation packet; the clean blind report; the independent hostile report; the non-isolated discovery report only as candidate evidence; and the authoritative graph entries for the finite vector identity, partial functional equation, hierarchy, endpoint prefix, and \(R_1\) module.  No numerical computation or external source was used.

The clean statement-only gate is `reports/blind_alpha_kernel_rederivation.md`.  The independent selected-context seam gate is `reports/alpha_trace_hostile_audit.md`.  The discovery report is explicitly classified as non-isolated because of its disclosed extra reads.

## 7. Recommended state effect

Promote a scoped `M9-M1-alpha-masked-cosine-comb-reduction` containing (49.C1)--(49.C4), the zero \(A=0\) ownership conclusion, and the two elementary falsifiers.  Keep the alpha transition estimate open.  Do not promote the discovery report's full actual-profile equality to GAR until the projected physical operator and its one-count connector ledger are independently derived.
