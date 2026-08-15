# Round 31 hostile audit: regular finite-part symbol BV

## 1. Result

The frozen requirement is false if “every product-rule derivative” is
estimated separately in the divided-difference \((L,\mu)\) coordinates.
The lawful actual height factor produces a loss of one full power of the
saddle parameter.  This loss is artificial: it cancels only after the
moving section is reparametrized by the physical height variable
\(\nu=L-\mu\), or equivalently after the translation derivative and its
moving endpoint traces are kept signed.

More precisely, on a positive or negative saddle patch
\(|L|\asymp\lambda\), the derivative term
\[
 \frac{f_b'(L-\mu)}
 {\mu\{A(L)+i\mu/2\}},\qquad A(L)=\rho_0-i(L+\beta),
 \tag{31.1}
\]
has absolute \((L,\mu)\)-mass \(\asymp_b\lambda^{-1}\) on an admissible
finite box, whereas the required pre-numerator BV scale is
\(\lambda^{-2}\).  Multiplication by the Round-27 stationary numerator
\((D_j/q)\lambda\) turns this termwise bound into \(D_j/q\), losing a
factor \(\lambda\) against \(D_j/(q\lambda)\).  Thus no proof may take
absolute values term by term after differentiating
\(f_b(L-\mu)\).

There is a narrow true lemma.  After changing back to \((L,\nu)\), if the
complete **recombined** regular kernel satisfies ordinary symbol bounds
\[
 |K(L,\nu)|\ll_b\lambda^{-2}w_b(\nu),\qquad
 |\partial_LK(L,\nu)|\ll_b\lambda^{-3}w_b(\nu),
 \tag{31.2}
\]
with \(w_b\in L^1\), then its finite-section integral has
\[
 \|R\|_\infty+\operatorname{Var}_LR\ll_b\lambda^{-2},
 \tag{31.3}
\]
uniformly through every affine \(U,V\) face.  This preserves the local
\(q^{-2}\) normalization after the stationary numerator.  The
separated \(R_1\) regular two-denominator kernel obeys this mechanism
away from the artificial-\(\rho\) seam.

The authorized evidence does not establish (31.2) for the complete
\(\omega G+(1-\omega)R_1-\omega E_1\) symbol, its axial package, or its
finite radial sides.  Hence the full Round-31 target remains open.

Equivalently, in divided-difference notation the first genuinely missing
complete-symbol derivative is
\[
 \partial_\nu(\partial_L+\partial_\nu)H_{\rm comp}. \tag{31.0}
\]
The directional derivative \(\partial_L+\partial_\nu\), rather than
\(\partial_L\) alone, is forced by holding \(\mu=L-\nu\) fixed.  Formula
(31.0) is the infinitesimal form of the translation cancellation behind
(31.9).  The authorized artifacts give no target-scale bound for it
after all radial pieces, masks, and endpoints are combined.

## 2. Exact statement and hypotheses

Put
\[
 L=\alpha-\beta,\qquad \mu=L-\nu,\qquad
 A(L)=\rho_0-i\alpha=\rho_0-i(L+\beta).
\]
For separated \(R_1\), the top and radial denominators give
\[
 \frac{f_b(L-\mu)}{\mu\{A(L)+i\mu/2\}}.
\]
Removing the constant-numerator Plemelj logarithm leaves the exact
regular integrand
\[
\begin{aligned}
K_{\rm reg}(L,\mu)
={}&-\frac{i f_b(L)}
 {2A(L)\{A(L)+i\mu/2\}}\\
&+\frac{f_b(L-\mu)-f_b(L)}
 {\mu\{A(L)+i\mu/2\}}.                              \tag{31.4}
\end{aligned}
\]
Its section is
\[
 a(L)=\max(-U,L-V),\qquad b(L)=\min(U,L+V).          \tag{31.5}
\]
The top limit has already been taken distributionally; explicit delta
jumps and the \(q^{-4}\) height-face logarithms are not part of
\(K_{\rm reg}\).

For the countercontrol choose a compact interval
\(E\subset(-V,V)\) on which
\[
 \int_E|f_b'(\nu)|\,d\nu>0.                          \tag{31.6}
\]
Such an \(E\) exists for the accepted profile: its analytic Mellin
transform decays at infinity and is not constant.  Choose a saddle cell
\(L\in[c\lambda,C\lambda]\), bounded \(\beta,\rho_0\), and finite
\(U,V,S\) so that \(\nu\in E\) is allowed for every \(L\) in that cell.
Also keep this cell outside the artificial-\(\rho\) support.

For the positive lemma, let
\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U],\qquad
 R(L)=\int_{I_{U,V}(L)}K(L,\nu)\,d\nu.               \tag{31.7}
\]
On a saddle cell of length \(O(\lambda)\), assume (31.2) and assume that
the same weight controls the affine endpoint traces.  These hypotheses
may include a polylogarithmic \(b^{-1}\) loss.  They are not asserted
across \(\rho=0\) unless the three radial pieces have first been
recombined.

## 3. Proof or derivation

### Actual-factor falsifier for the termwise derivative ledger

Differentiate the second line of (31.4) at fixed \(\mu\).  One
product-rule term is exactly (31.1).  On the set
\[
 L\in[c\lambda,C\lambda],\qquad \nu=L-\mu\in E,
\]
one has
\[
 |\mu|\asymp\lambda,\qquad
 |A(L)+i\mu/2|
 =\left|\rho_0-\frac i2(L+2\beta+\nu)\right|
 \asymp\lambda.
\]
Since \(d\mu=-d\nu\),
\[
\begin{aligned}
&\int_{c\lambda}^{C\lambda}\int_{\{L-\mu\in E\}}
 \left|\frac{f_b'(L-\mu)}
 {\mu\{A(L)+i\mu/2\}}\right|d\mu\,dL\\
&\hspace{20mm}\asymp_b
 \lambda\cdot\lambda^{-2}
 \int_E|f_b'(\nu)|d\nu
 \asymp_b\lambda^{-1}.                              \tag{31.8}
\end{aligned}
\]
BV is invariant under the monotone Morse rescaling:
\(\int|\partial_yB|dy=\int|\partial_LB|dL\).  Thus (31.8) is a genuine
factor-\(\lambda\) violation of the desired \(\lambda^{-2}\) bound for
this individual derivative term.  It uses the accepted profile, not an
adversarial replacement.

The complete integral need not have this loss.  If the \(\nu\)-section
is fixed on the chosen cell, then
\[
 \int K_{\rm reg}(L,\mu)d\mu
 =\int K_{\rm reg}(L,L-\nu)d\nu.                    \tag{31.9}
\]
Now \(f_b(\nu)\) is independent of \(L\).  The translation derivative
in (31.1) is cancelled by the coordinate motion and the corresponding
endpoint trace.  In the model leading region the result is
\[
 R(L)=c\,L^{-2}\int_Ef_b(\nu)d\nu+O_b(L^{-3}),
\]
whose variation on a length-\(\lambda\) cell is \(O_b(\lambda^{-2})\).
This proves both the falsifier and the required remedy: cancellation
must occur before absolute BV estimates.

### Narrow finite-section BV lemma

The endpoints of \(I_{U,V}(L)\) are
\[
 p(L)=\max(-V,L-U),\qquad q(L)=\min(V,L+U).
\]
On every affine cell, Leibniz gives
\[
 R'(L)=\int_{p(L)}^{q(L)}\partial_LK(L,\nu)d\nu
q'(L)K(L,q(L))-p'(L)K(L,p(L)).                      \tag{31.10}
\]
The interior term in total variation is, by (31.2),
\[
 \int_{\text{cell}}\int_{I_{U,V}(L)}
 |\partial_LK|\,d\nu\,dL
 \ll_b\lambda\lambda^{-3}\|w_b\|_1
 \ll_b\lambda^{-2}.                                 \tag{31.11}
\]
If an endpoint is the fixed face \(\nu=\pm V\), its derivative is zero.
If it is \(L\mp U\), substitution \(\nu=L\mp U\) gives
\[
 \int |K(L,L\mp U)|dL
 \ll_b\lambda^{-2}\int w_b(L\mp U)dL
 \ll_b\lambda^{-2}\|w_b\|_1.                        \tag{31.12}
\]
There are only finitely many affine switches; section collapse creates
a corner but no jump because the two endpoints coincide.  Equations
(31.10)--(31.12) prove (31.3).  This argument also explains why floors
\(H_j+1\), fixed radial stars, and scale constants do not themselves
create \(L\)-variation: they multiply (31.3) unchanged.

### Omega, axial, and normalization seams

At the unsimplified integrand level,
\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1.
\]
Differentiation gives the coefficient
\[
 \omega'(G-R_1-E_1)=0.                              \tag{31.13}
\]
The cancellation remains exact after finite-section regularization
because that operation is linear, but only if all three terms have the
same beta mask, \((U,V,S)\) domain, endpoint convention, face-log
subtraction, and endpoint-image ledger.  Estimating the three
\(\omega'\) terms separately loses the cancellation.  Removing the
\(E_1\) endpoint image before applying the same regularization also
invalidates (31.13).

The same cancellation persists through two derivatives if the complete
combination is kept intact.  The \(\omega''\)-coefficient is again
\(G-R_1-E_1=0\), while the two product-rule \(\omega'\)-coefficients
combine to
\[
 2\omega'D(G-R_1-E_1)=0
\]
for the relevant directional derivative \(D\).  Thus neither
\(\omega'\) nor \(\omega''\) is a lawful offender.  The first lawful
analytic obligation after recombination is (31.0).  Estimating a single
\(\omega G\), \(R_1\), or \(E_1\) derivative cannot audit it.

Near \(v=0\),
\[
 f_b(\nu)=\frac1{b+i\nu}+O(1).
\]
Its \(L^1\) mass is logarithmic in \(b^{-1}\), while derivative norms
cost powers of \(b^{-1}\).  The \(\nu\)-coordinate lemma uses the former,
which is better, but it is not uniform at \(b=0\).  The \(v=0\) residue
must be extracted once and \(b\asymp1/\log X\) retained until that
ledger is complete.

If (31.3) holds before the stationary numerator, then multiplying by
\((D_j/q)\lambda\) gives
\[
 \frac{D_j}{q}\lambda\cdot\lambda^{-2}
 =\frac{D_j}{q\lambda}
 =\frac{D_j}{q^2\theta_j(x)},\qquad
 \theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j}.               \tag{31.14}
\]
Thus the narrow lemma genuinely preserves the accepted \(q^{-2}\)
power.  It does not prove that the \(G,E_1\), connector, or axial pieces
share the same pre-numerator normalization.

The cubic decay of \(f_b\) makes the separated \(R_1\) \(\nu\)-tail and
the affine endpoint traces summable for fixed \(b>0\).  No authorized
artifact supplies a corresponding joint \(U,V,S\) bound for the
complete recombined symbol.  In particular \(S>(U+V)/2\) couples height
exhaustion to the still-retained radial horizontal sides.

## 4. First doubtful or unproved step

The first invalid step is an absolute product-rule ledger in
\((L,\mu)\) that demands target size from every derivative separately.
Equation (31.8) disproves it for the actual height transform.  The
translation and moving-endpoint terms must first be recombined in
\((L,\nu)\).

After that repair, the first unproved step is an explicit complete
kernel \(K(L,\nu)\) satisfying (31.2).  The authorized formulas give
the separated \(R_1\) two-denominator term, but not a common
regular-symbol formula for \(\omega G\), \((1-\omega)R_1\),
\(-\omega E_1\), beta connectors, axial residue, and radial sides with
identical ownership.  Without that formula, (31.13) cannot be used
inside the BV norm and the \(q\)-power cannot be assigned to the whole
package.

In the equivalent divided-difference ledger, this is exactly the absent
bound for \(\partial_\nu(\partial_L+\partial_\nu)H_{\rm comp}\).
Fixed-\(b\) cubic transform decay controls the separated \(R_1\) tail,
but it does not by itself control this derivative for the endpoint
\(E_1\), the unsplit \(G\) part, or the finite radial sides.  This is the
first lawful height-tail obstruction; no pointwise \(q^{-2}\) estimate
implies it.

## 5. Control tests and outcomes

1. **Product rule and derivative.**  The actual term (31.1) has mass
   \(\asymp_b\lambda^{-1}\), not \(\lambda^{-2}\), when absolutized
   before translation cancellation.  Outcome: the proposed termwise
   proof fails; the recombined \(\nu\)-coordinate lemma passes.
2. **Moving endpoint traces.**  Formula (31.10) includes both traces.
   Moving \(\mu=\pm U\) faces become translated height values whose
   \(L\)-integrals are controlled by \(\|w_b\|_1\); fixed
   \(\nu=\pm V\) faces have zero velocity.  Outcome: narrow lemma
   passes.
3. **Residue and normalization.**  Omega-prime cancellation is exactly
   (31.13); the same identity cancels \(\omega''\) and the paired
   second-derivative \(\omega'\) terms, but only under identical
   ownership.  Equation (31.14)
   verifies \(q^{-2}\) for separated \(R_1\), not the complete package.
   Outcome: algebra passes; global normalization remains open.
4. **Profiles, floors, and stars.**  The actual \(f_b\) supplies the
   falsifier and has the needed fixed-\(b\) integrability.  Floors and
   radial stars are constant in \(L\), but their endpoint contributions
   and scale sums were not estimated.  Outcome: local BV passes;
   complete uniformity open.
5. **Height exhaustion.**  Fixed-\(b\) separated \(R_1\) tails are
   summable.  The \(b\downarrow0\) residue, joint \(U,V,S\) limit, and
   radial horizontal sides have no accepted uniform bound.  Outcome:
   fail for the frozen full target.
6. **Pointwise versus BV.**  Pointwise \(O(\lambda^{-2})\) does not
   control variation, and the termwise derivative bound is too strong.
   The signed reparametrized estimate (31.10) is the correct intermediate
   norm.  Outcome: scoped certification only.

## 6. Dependencies and exact artifacts used

This audit used only protocol.md, state/proof_obligations.yml,
state/active_campaign.yml, the authorized Round-27 hostile
pushforward report, the authorized Round-30 hostile logarithmic report,
and the Round-30 synthesis.  No Round-31 claimant report, external
theorem, web source, or numerical experiment was used.

## 7. Recommended state effect

**Reject the termwise divided-difference derivative strategy.**  Record
(31.8) as a method obstruction: taking absolute values before
translation/endpoint recombination loses one power of \(\lambda\) for
the actual profile.

**Promote only the narrow finite-section BV lemma** (31.2)--(31.3), and
its \(q^{-2}\) consequence (31.14), for the separated \(R_1\) regular
kernel on signed saddle cells away from \(\rho=0\), with fixed
\(b>0\) and the delta/face-log pieces already removed.

Keep M9-M1-beta-regular-finite-part-symbol-BV and the logarithmic beta
kernel open.  The next viable proof must write the complete recombined
kernel in \((L,\nu)\), prove (31.2) after exact omega/endpoint
recombination, then handle the axial residue and joint \(U,V,S\)
exhaustion.  No change to the external \(X^{1/4}\) normalization or to
the full beta, M9-M1, M9, or Gauss target is licensed.
