# Round 32 hostile audit: complete physical-height kernel

## 1. Result

The frozen complete-kernel bound cannot hold with the radial horizontal
sides included in a single pointwise symbol
\[
 |K_{\rm complete}|\ll\lambda^{-2}w_b(\nu),\qquad
 |\partial_LK_{\rm complete}|\ll\lambda^{-3}w_b(\nu).
 \tag{32.1}
\]
This is a type and normalization obstruction, not merely a missing
estimate.  The terminal vertical \(R_1\) trace, the explicit hard radial
endpoint images \(E_M\), and the radial horizontal-side functionals live
on different contour strata and have different phase variables.  A
horizontal side is an integral over \(\Re w\) at
\(\Im w=\pm S\); after diagonal coordinates it is not a function of the
terminal \(L\)-trace with bounded beta.  Combining it pointwise with
\(K(L,\nu)\) before the finite contour identity changes the operator.

There is also an inherited rigorous obstruction.  Before arbitrary-order
endpoint subtraction, the hard radial side has a genuine endpoint
expansion beginning with \(S^{-1}\), while the degree-two factor on the
left edge has capacity \(S^{1-2\ell}\), \(\ell=1-c'<0\).  Thus its
absolute capacity is \(S^{-2\ell}\), which grows under faster nesting.
No integrable \(w_b(\nu)\) with constants independent of \(S\) can
absorb this into (32.1).

The narrow certification is:

1. on the terminal trace, the common algebraic combination
   \(\omega G+(1-\omega)R_1-\omega E_1\) equals \(R_1\) identically,
   so all \(\rho=0\) Taylor singularities and all cutoff derivatives
   cancel to every order under identical ownership;
2. after the \(v=0\) residue is extracted, the fixed-\(b\) terminal
   height kernel can use the Round-31 physical-height symbol lemma;
3. the renormalized radial sides may be removed only by the separately
   accepted arbitrary-order endpoint-subtraction theorem, while the
   explicit \(E_M\) boundary operator remains a separate ledger.

The accepted Round-22 Cauchy collapse makes this separation more than a
convenience.  Once the explicit endpoint and arithmetic modules have
been collapsed and estimated with their own profiles and signs, they
must not be reinserted into the transition symbol.  The correct
Round-32 local object is therefore the side-collapsed,
endpoint-image-free terminal remainder, with a pointer to the closed
boundary modules.  The literal “finite radial sides inside
\(K_{\rm complete}\)” target is overstrong and risks double counting.

Consequently the common terminal symbol and the side exhaustion must be
two composable lemmas, not one kernel bound.  The complete Round-32
target remains open.

## 2. Exact statement and hypotheses

Let
\[
 G(\rho)=\int_1^N x^{\rho-1}e(\sqrt{Xx})\,dx,
\]
with the harmless fixed \(v\)-dependent power absorbed into \(\rho\).
For the first radial integration by parts put
\[
 E_1(\rho)=C\,\frac{N^\rho e(\sqrt{XN})-e(\sqrt X)}{\rho},
\qquad
 R_1(\rho)=G(\rho)-E_1(\rho),                        \tag{32.2}
\]
with \(C\) denoting the accepted fixed normalization.  The precise
displayed powers in the accepted endpoint formula do not affect the
local argument; the defining identity
\[
 G=E_1+R_1                                             \tag{32.3}
\]
does.

Let \(r=-\Im\rho\), let \(\omega(r)=1\) near zero, and define
\[
 {\cal Q}(\rho)
 =\omega G+(1-\omega)R_1-\omega E_1.                 \tag{32.4}
\]
Every term must have the same beta mask, finite \((U,V,S)\) domain,
top convention, radial endpoint image, face subtraction, and residue
ledger.

On the terminal signed saddle patches put
\[
 L=\alpha-\beta,\qquad \lambda=\frac{\pi q\sqrt{Xx}}{D_j},
\qquad |L|\asymp|\alpha|\asymp\lambda,
\]
and retain physical height \(\nu\).  A terminal common-kernel statement
may be sought only after the combined Plemelj diagonal/log subtraction
is applied linearly to (32.4).

Separately, on a radial horizontal side,
\[
 w=\sigma\pm iS,\qquad \lambda_w=1-c'<0,
\]
the accepted arbitrary-order split is
\[
 G_v(w)=E_{M,v}(w)+R_{M,v}(w).                       \tag{32.5}
\]
Here \(E_M\) is the explicit pair of hard endpoint series and \(R_M\)
is the renormalized remainder.  It is not part of a pointwise terminal
\(L\)-kernel.

## 3. Proof or derivation

### Rho Taylor and cutoff ledger

Although the separate formula for \(E_1\) contains \(1/\rho\), its
numerator vanishes at \(\rho=0\):
\[
 N^\rho e(\sqrt{XN})-e(\sqrt X)
 =c_0+c_1\rho+c_2\rho^2+\cdots .
\]
If \(c_0\ne0\) for the particular endpoint pair, the matching Laurent
coefficient of \(R_1=G-E_1\) is its negative; if \(c_0=0\), both are
already regular.  In either case (32.3) fixes every Laurent/Taylor
coefficient.  More decisively, (32.4) simplifies algebraically:
\[
 {\cal Q}
 =R_1+\omega(G-R_1-E_1)=R_1.                        \tag{32.6}
\]
For every compatible directional derivative \(D\) and integer \(k\),
\[
 D^k{\cal Q}=D^kR_1.                                \tag{32.7}
\]
Indeed every \(\omega^{(j)}\) coefficient is a derivative of the exact
zero \(G-R_1-E_1\).  Thus no \(\rho=0\) residue, \(\omega'\), or
\(\omega''\) term is independently available.  A Taylor proof that
estimates the three pieces before using (32.6) is invalid.

This certification has a strict ownership condition.  If \(E_1\) has
already been moved to a separate endpoint ledger, while \(-\omega E_1\)
is still retained in (32.4), then the three displayed terms no longer
refer to the same operator.  Likewise, applying different diagonal/log
subtractions or endpoint stars breaks the linear cancellation.

### Axial seam

The accepted height transform satisfies
\[
 f_b(\nu)=\frac1{b+i\nu}+r_b(\nu),                   \tag{32.8}
\]
where the first term is the \(v=0\) axial pole.  On \(b>0\),
\[
 \int_{-1}^{1}\frac{d\nu}{|b+i\nu|}
 \asymp\log(1/b),\qquad
 \int_{-1}^{1}\frac{d\nu}{|b+i\nu|^2}
 \asymp b^{-1}.                                     \tag{32.9}
\]
Consequently a claim of polylogarithmic \(b\)-loss is compatible with
an \(L^1\) physical-height weight only after the pole/residue is
extracted and derivatives are arranged so that they do not differentiate
the polar factor in absolute value.  A weighted symbol involving
\(|\partial_\nu f_b|\) has a power \(b^{-1}\), not a logarithm.  The
Round-31 ordinary fixed-\(\nu\) \(L\)-derivative avoids that derivative,
which is precisely why it is the correct interface.  No uniform passage
to \(b=0\) is licensed: the axial residue must be inserted once, with
its top/corner ownership read back before the remainder limit.

### Actual radial-side obstruction

The accepted hard radial cutoff has an endpoint integration-by-parts
expansion on \(w=\sigma\pm iS\) whose first term is
\[
 G_v(\sigma\pm iS)
 =
 \left[\frac{x^{\sigma-3/4-b/2}
 e^{i\Phi_\pm(x)}}{i\Phi_\pm'(x)}\right]_{x=1}^{N}
 +O(S^{-2})
 =O(S^{-1})+O(S^{-2}).                              \tag{32.10}
\]
The endpoint stars do not halve these integration-by-parts
coefficients.  On the forced left edge, the degree-two functional
equation factor has capacity
\[
 O(S^{1-2\lambda_w}).
\]
Hence the elementary absolute side capacity is
\[
 O(S^{-2\lambda_w}),\qquad \lambda_w<0,             \tag{32.11}
\]
which grows.  This is an actual-factor countercontrol to any uniform
common weight in (32.1).  Faster joint nesting worsens (32.11).

The accepted remedy is (32.5): choose \(M>-2\lambda_w\).  Then the
renormalized side \(R_M\) decays sufficiently after a polynomial nested
choice \(S=S(X,U,V)\).  But its constants depend on
\((X,N,M,c,c',b)\), and the full endpoint series \(E_M\) remains.  It
cannot be identified with the single \(E_1\) used in the local
\(\rho=0\) package, nor silently folded into \(K_{\rm complete}(L,\nu)\).
The explicit endpoint operator and its arithmetic residue were handled
in distinct accepted ledgers; any Round-32 use must cite those estimates
rather than reassign them.

In particular, the Round-22 endpoint Cauchy reduction licenses the
following order: perform exact endpoint subtraction, collapse the
explicit endpoint and arithmetic boundary functional into its accepted
module, remove the renormalized side under its nested-height theorem,
and only then define the terminal transition kernel.  Reversing this
order by placing those pieces into \(K_{\rm complete}\) loses the
module's cancellation and can count the same endpoint image both in
\(E_M\) and in the local \(-\omega E_1\) term.

### Physical derivative and q normalization

After (32.6), combined diagonal subtraction, and axial extraction, suppose
the **terminal remainder only** has
\[
 |K_{\rm term}(L,\nu)|\ll X^\varepsilon\lambda^{-2}w_b(\nu),
\quad
 |\partial_LK_{\rm term}(L,\nu)|
 \ll X^\varepsilon\lambda^{-3}w_b(\nu),             \tag{32.12}
\]
with \(\|w_b\|_1\ll(\log X)^C\).  The Round-31 finite-section lemma then
gives \(O(X^\varepsilon\lambda^{-2})\) supremum plus BV.  Multiplying by
the accepted stationary numerator yields
\[
 \frac{D_j}{q}\lambda\cdot\lambda^{-2}
 =\frac{D_j}{q\lambda}
 =\frac{D_j}{q^2\theta_j(x)}.                       \tag{32.13}
\]
This certifies the q ledger only for that terminal post-endpoint
remainder.  The explicit \(E_M\) endpoint operator, axial residue, radial
sides, connector areas, floors, stars, and external
\(-(4/\pi)X^{1/4}\operatorname{Re}\) normalization keep their separately
accepted powers; they do not inherit \(q^{-2}\) from (32.13).

## 4. First doubtful or unproved step

The first definition failure is the demand for one common
\(K_{\rm complete}(L,\nu)\) containing both the terminal trace and
radial horizontal sides.  These pieces are supported on different
finite-contour faces.  The exact finite identity adds their integrals;
it does not identify their pointwise integrands.

After repairing that scope, the first unproved analytic step is (32.12)
for the terminal common remainder with the combined diagonal
subtraction and axial residue actually written.  Identity (32.6)
settles cutoff/Taylor cancellation but supplies no size estimate.
The authorized Round-31 result proves (32.12) only for separated
\(R_1\), away from both seams.

Joint exhaustion is a second independent seam.  Renormalized radial-side
removal permits a nested \(S(X,U,V)\), but the explicit endpoint ledger,
the \(v=0\) remainder, and translated \(U,V\) tails must be estimated
before the orders of limit can be interchanged.

## 5. Control tests and outcomes

1. **Common-kernel ownership.**  The algebraic terminal combination
   equals \(R_1\), but radial horizontal sides are distinct contour
   functionals already routed through side-removal and endpoint-Cauchy
   modules.  Outcome: the side-collapsed endpoint-free terminal kernel
   is meaningful; the frozen all-inclusive kernel is not.
2. **Rho Taylor and residue.**  Every artificial Laurent coefficient
   and every cutoff derivative cancels by (32.6)--(32.7), provided
   ownership is identical.  Outcome: exact cancellation certified, no
   independent artificial residue.
3. **Physical-height derivative.**  Fixed-\(\nu\) differentiation avoids
   the false translation derivative.  The implication
   (32.12)\(\Rightarrow\)BV is accepted, but (32.12) itself is unproved
   for the common axial-subtracted terminal remainder.  Outcome:
   conditional only.
4. **Axial \(b\)-limit.**  The polar \(L^1\) loss is logarithmic, while
   its differentiated absolute norm is \(b^{-1}\).  Extracting the
   \(v=0\) residue once is necessary; no uniform \(b=0\) symbol follows.
   Outcome: finite-\(b\) scope only.
5. **Radial-side exhaustion.**  The raw side obstruction
   (32.10)--(32.11) falsifies direct absolute nesting.  Arbitrary-order
   endpoint subtraction removes only \(R_M\); \(E_M\) remains a
   separate boundary operator.  Outcome: no complete joint exhaustion
   proved in Round 32.
6. **Normalization and q power.**  Equation (32.13) preserves local
   \(q^{-2}\) for the terminal remainder if (32.12) holds.  It gives no
   q power to the endpoint, axial, side, or connector ledgers.  Outcome:
   scoped pass, global failure.

## 6. Dependencies and exact artifacts used

This audit used only protocol.md, state/proof_obligations.yml,
state/active_campaign.yml, the Round-20 diagonal-transition synthesis,
the authorized Round-31 hostile report, and the Round-31 synthesis.  No
Round-32 claimant report, external theorem, web source, or numerical
experiment was used.

## 7. Recommended state effect

**Revise the frozen target.**  Do not require radial horizontal sides or
explicit hard-endpoint operators to satisfy a terminal
\((L,\nu)\)-symbol bound.  Preserve them as separate finite-contour
ledgers and invoke the accepted arbitrary-order side removal and
Round-22 endpoint-Cauchy/arithmetic modules only with their exact
hypotheses.  Define the local symbol only after that collapse; retain
cross-references so the removal is not mistaken for deletion.

**Promote the narrow algebraic control:** under identical ownership,
\({\cal Q}=R_1\) and every \(\rho\)-Taylor, \(\omega'\), and higher cutoff
derivative cancellation is exact.  Retain the Round-31 physical-height
BV implication and the conditional q ledger (32.13) for the
axial-subtracted terminal remainder.

Keep M9-M1-beta-complete-physical-height-symbol-bound,
M9-M1-beta-regular-finite-part-symbol-BV, the beta transition, and joint
height exhaustion open.  Split the next obligation into:

1. the axial-subtracted terminal common-symbol bound (32.12); and
2. a compatibility theorem that adds the already-renormalized radial
   sides and explicit endpoint/residue package after, rather than inside,
   the terminal stationary estimate.

No change to the full \(h,D_j,x\), external \(X^{1/4}\), M9-M1, M9, or
Gauss-circle normalization is licensed.
