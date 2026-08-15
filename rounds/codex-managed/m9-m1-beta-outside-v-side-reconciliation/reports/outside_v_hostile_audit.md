# Round 29 hostile audit: outside-\(v\) side reconciliation

## 1. Result

The proposed finite-height side cancellation is not a valid route to the
scaled \(C^2\) amplitude required by the accepted Fresnel lemma.  A
correctly oriented finite \(v\)-rectangle does not add the complementary
tail \(|\nu|>V\).  It rewrites one vertical contour as the other vertical
contour plus the upper horizontal connector, minus the lower horizontal
connector, and the crossed residue/Cauchy--Green ledger.  Therefore it
represents the same finite operator.  If this identity is interpreted
pointwise in \(L=\alpha-\beta\), its right-hand side must reproduce, not
cancel, the nonzero logarithmic edge of the original vertical.

There is also a scope correction.  The exact finite box has
\[
 |\mu|=|L-\nu|\leq U.
\]
This constraint does not remove the collision at \(L=V,\nu=V\), but the
logarithm is a pointwise edge singularity, not by itself a divergence of
the fully \(L\)-integrated signed operator.  Pairing first in
\(\mu=L-\nu\) gives a uniform Plemelj distributional limit.  Thus Round
28 proves failure of a supremum-\(L\), scaled-\(C^2\) strategy; it does
not prove failure of the target transition operator.

Moreover, the physical top limit is the \(u\)-line limit
\(a=\Re u\downarrow0\).  It does not move the \(v\)-line and hence does
not generate \(v\)-horizontal sides.  Such sides become relevant only if
one independently shifts the \(v\)-contour.  Adding them merely to repair
the \(u\)-Plemelj edge is conceptually unsupported.

The narrow true replacement is: retain the exact oriented rectangle
identity when a \(v\)-shift is actually performed, but take the physical
top limit distributionally against the remaining \(\alpha\)/\(\mu\)
integration.  A new singular-amplitude stationary theorem would then be
needed; the existing \(C^2\) Fresnel lemma cannot be invoked.

## 2. Exact statement and hypotheses

For a genuine \(v\)-shift let \(M(v;u,s)\) be the complete radial/profile
integrand before any nonholomorphic mask or \(\omega\) decomposition.
Assume first that, for fixed \(u,s\), it is meromorphic in
\[
 {\cal R}_{b,V}=\{v:-b\leq\Re v\leq b,\ |\Im v|\leq V\},
\]
with no pole on the boundary.  Define
\[
\begin{aligned}
 I_{\pm b}&=\int_{\pm b-iV}^{\pm b+iV}M(v)\,dv,\\
 T_+&=\int_{-b+iV}^{b+iV}M(v)\,dv,\qquad
 T_-=\int_{-b-iV}^{b-iV}M(v)\,dv ,
\end{aligned}
\]
where both \(T_\pm\) are written left-to-right.  Then
\[
 \boxed{I_b=I_{-b}+T_+-T_-+
 2\pi i\sum_{v_0\in{\cal R}_{b,V}}\operatorname{Res}_{v=v_0}M.}
 \tag{29.1}
\]
If the beta mask is already inserted, the additional term is
\[
 2i\iint_{{\cal R}_{b,V}}\bar\partial_v M\,dA(v),       \tag{29.2}
\]
with the same orientation.  This is part of the accepted
Cauchy--Green connector and cannot be omitted.

The actual finite-box top convolution is more accurately
\[
 C_{a,U,V}(L)=
 \int_{\max(-V,L-U)}^{\min(V,L+U)}
 \frac{H_b(\nu,L)}{a+i(L-\nu)}\,d\nu,                 \tag{29.3}
\]
with the integral zero if its lower endpoint exceeds its upper endpoint.
For the edge obstruction assume \(U>0\), \(H_b\) is \(C^2\) near
\((\nu,L)=(V,V)\), all other poles, including \(\rho=0\), are separated,
and
\[
 H_b(V,V)\ne0.                                       \tag{29.4}
\]
The accepted fixed-\(b>0\) height transform is analytic and not
identically zero, so an admissible \(V\) satisfying (29.4) exists.

## 3. Proof or derivation

Positive orientation around the \(v\)-rectangle is bottom left-to-right,
right upward, top right-to-left, and left downward.  Hence
\[
 T_-+I_b-T_+-I_{-b}=2\pi i\sum\operatorname{Res}M,
\]
which gives (29.1).  Thus the upper side enters with plus sign and the
lower left-to-right side with minus sign.  Moving \(b\) to \(-b\) across
\(v=0\) puts the full \(v=0\) residue on the right of (29.1).  Stopping
on the pole instead requires an explicitly chosen half-residue
convention; it cannot be combined with the full crossing residue.

This orientation already gives a no-go for pointwise cancellation.  If
the transformed right-hand side of (29.1)--(29.2) is claimed to be a
function \({\cal R}_{a,U,V}(L)\) satisfying the exact finite identity,
then
\[
 {\cal R}_{a,U,V}(L)=C_{a,U,V}(L)                    \tag{29.5}
\]
for every \(a>0\).  It follows that a bounded value of the left side at
\(L=V\) is impossible whenever the right side has the actual nonzero edge
coefficient.  If, instead, (29.1) is valid only after the natural sheared
integration, it is an operator/distribution identity and supplies no
pointwise \(C^2\) amplitude.

The horizontal-side geometry confirms the distinction.  On the upper
side \(\nu=V\), the diagonal coordinates give
\[
 L-V=\mu,\qquad u=a+i\mu.
\]
Consequently the side contains the boundary Cauchy kernel
\((a+i(L-V))^{-1}\).  It is not an integral over \(\nu>V\).  It can carry
the logarithm after \(L\)-integration, but before that integration it is
a Plemelj distribution rather than a bounded correction.  Also, no such
side is generated when only \(a\downarrow0\) on the original \(u\)-line.

To retain the exact \(U\)-constraint in the edge calculation, suppose
for simplicity that \(U\leq2V\).  At \(L=V\), (29.3) contains
\(\nu\in[V-U,V]\).  With \(y=V-\nu\),
\[
\begin{aligned}
 C_{a,U,V}(V)
 &=H_b(V,V)\int_0^U\frac{dy}{a+iy}+O_{H,U,V}(1)\\
 &=-iH_b(V,V)\log(1/a)+O_{H,U,V}(1).                 \tag{29.6}
\end{aligned}
\]
At the lower edge the coefficient is
\[
 C_{a,U,V}(-V)=
 +iH_b(-V,-V)\log(1/a)+O_{H,U,V}(1).                 \tag{29.7}
\]
The opposite endpoint signs must not be paired with the same contour
orientation.  Differentiating the frozen-endpoint model gives
\[
\begin{aligned}
 \partial_LC_{a,U,V}(V)
   &=-H_b(V,V)a^{-1}+O(\log(1/a)),\\
 \partial_L^2C_{a,U,V}(V)
   &=+iH_b(V,V)a^{-2}+O(a^{-1}\log(1/a)),             \tag{29.8}
\end{aligned}
\]
and reversed leading signs at \(-V\).  Thus finite-height scaled \(C^2\)
uniformity fails even more strongly than \(C^0\) uniformity.

This failure is nevertheless integrable.  Let \(A(L)\) be a smooth test
amplitude and return to the rectangular variables
\(\mu\in[-U,U]\), \(\nu\in[-V,V]\).  With
\[
 F(\mu,\nu)=A(\mu+\nu)H_b(\nu,\mu+\nu),
\]
Fubini gives
\[
 \int A(L)C_{a,U,V}(L)\,dL
 =\int_{-V}^V\int_{-U}^U
   \frac{F(\mu,\nu)}{a+i\mu}\,d\mu\,d\nu.             \tag{29.9}
\]
Write
\[
 F(\mu,\nu)=F(0,\nu)+\mu G(\mu,\nu).
\]
Then
\[
 \int_{-U}^U\frac{d\mu}{a+i\mu}
 =2\arctan(U/a)\longrightarrow\pi
\]
and
\[
 \frac{\mu}{a+i\mu}\longrightarrow-i,\qquad
 \left|\frac{\mu}{a+i\mu}\right|\leq1.
\]
Dominated convergence therefore proves the uniform signed limit
\[
\begin{aligned}
 \lim_{a\downarrow0}\int A(L)C_{a,U,V}(L)\,dL
 ={}&\pi\int_{-V}^VF(0,\nu)\,d\nu\\
 &-i\int_{-V}^V
 \operatorname{PV}\int_{-U}^U\frac{F(\mu,\nu)}{\mu}
 \,d\mu\,d\nu .                                     \tag{29.10}
\end{aligned}
\]
This is exactly
\[
 (a+ix)^{-1}\longrightarrow
 \pi\delta_0(x)-i\,\operatorname{PV}(1/x).            \tag{29.11}
\]
The logarithm in (29.6) is thus a pointwise Hilbert-transform edge and is
locally integrable in \(L\).  Taking absolute values before the
\(\mu\)-pairing instead costs \(\log(1/a)\), so (29.10) is a genuinely
signed statement.

If both \(u\) and \(v\) are shifted, (29.1) must be applied sequentially
to the complete integrand.  The \(u=0\) residue must be evaluated on
every \(v\)-vertical and \(v\)-side, the \(v=0\) residue on every
\(u\)-piece, and the joint corner occurs exactly once.  The \(v=0\)
residue has \(\nu=0\), hence its top denominator is
\(a+iL\), which is regular at \(L=\pm V\) for \(V>0\); the joint corner
itself lies at \(L=0\).  Neither can cancel the logarithmic edge.  The
\(u=0\) residue is the delta part of (29.11), not a cancellation of its
one-sided PV logarithm.

Finally, \(\omega(-\Im\rho)\) is nonholomorphic in the contour variables.
The accepted algebra
\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1               \tag{29.12}
\]
may be differentiated or shifted termwise only with identical masks,
domains, sides, and all \(\bar\partial\omega\) connectors retained.
Those terms cancel after exact recombination with the same \(E_1\)
ledger.  An isolated artificial-\(\rho\) side residue is therefore not
available as an independent edge cancellation.

## 4. First doubtful or unproved step

The first invalid step is treating the upper and lower real-\(v\)
connectors in (29.1) as the missing \(|\nu|>V\) part of the Hilbert
convolution.  They are different geometric objects, and an exact
rectangle identity preserves the finite operator.  If no \(v\)-shift is
performed, those connectors are absent altogether.

The first genuinely open step is to use (29.10) inside the complete
masked transition operator and prove a stationary estimate for the
resulting PV/delta amplitude, including saddle collisions with the
finite \(t,\mu,\nu\) faces.  The accepted Fresnel lemma assumes an
ordinary scaled \(C^2\) amplitude, so it does not cover this
distributional pairing.

## 5. Control tests and outcomes

1. **Signed versus unsigned.**  The signed pairing (29.10) is uniformly
   finite, whereas the absolute \(\mu\)-integral grows like
   \(\log(1/a)\).  Outcome: pointwise/absolute failure but distributional
   signed survival.
2. **Support and degeneracy.**  The exact condition
   \(|L-\nu|\leq U\) leaves a one-sided interval at \(L=\pm V\), and the
   actual analytic profile has admissible nonzero endpoint values.
   Outcome: the edge calculation survives the missing constraint.
3. **Residue and normalization.**  The correct side signs are
   \(+T_+-T_-\), with a plus full crossed residue.  Axial residues and the
   corner are counted once; full and half-residue conventions may not be
   mixed.  The external \(-(4/\pi)X^{1/4}\operatorname{Re}\)
   normalization changes none of these signs.  Outcome: exact finite
   ledger certified.
4. **Endpoint uniformity.**  Equation (29.8) falsifies the scaled \(C^2\)
   hypothesis at fixed \(V\).  Equation (29.10) shows this is not a
   target-operator divergence.  Outcome: Fresnel route fails as scoped;
   full operator remains open.
5. **Order of limits.**  The top limit can be taken distributionally at
   fixed \(U,V,S\).  Taking \(V\to\infty\) first is only locally plausible
   in \(L\) and forces \(S>(U+V)/2\), invoking the unproved radial-side
   exhaustion.  Outcome: no uniform nested exhaustion certified.
6. **Coefficient adversary.**  Any pointwise exact decomposition must
   reproduce the nonzero coefficient (29.6).  A zero sum is either the
   tautological closed-contour identity, which estimates zero rather
   than the transition term, or has omitted a vertical, area, or residue
   piece.  Outcome: finite-side cancellation falsified.

## 6. Dependencies and exact artifacts used

This audit used only protocol.md, state/proof_obligations.yml,
state/active_campaign.yml, the authorized blind finite-vector report, the
Round-25 partial-functional-equation synthesis, the Round-28
stationary-patching synthesis, and the Round-28 hostile report.  No
Round-29 claimant report, external theorem, web source, or numerical
experiment was used.

## 7. Recommended state effect

**Reject or revise the candidate mechanism, not the target operator.**
Finite horizontal \(v\)-sides do not cancel the finite vertical's
pointwise moving-edge logarithm while preserving the operator, and they
are not generated by physical top inversion.  Therefore they cannot
produce the scaled \(C^2\) input required by the current Fresnel lemma.

**Promote the narrow controls:** the orientation (29.1)--(29.2), the
constraint-aware edge formulas (29.6)--(29.8), the Plemelj sign
(29.11), and the distributional finite-box limit (29.10), with the full
axial/side/corner/\(\omega\) ledger recombined before limits.

Keep M9-M1-beta-outside-v-side-reconciliation,
M9-M1-beta-transition-connector-reduction, and the swept transition
operator open.  The viable next statement is a distribution-first
PV/delta stationary estimate on the original finite box, or a genuinely
uniform height-before-top exhaustion; it is not a finite-\(V\)
pointwise side cancellation.
