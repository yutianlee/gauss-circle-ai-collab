# Round 34 synthesis: the finite axial ledger closes, but module limits do not yet commute

Campaign: `m9-m1-beta-complete-axial-connector-ledger`  
Round type: complete finite two-axis beta connector ledger  
Graph SHA-256 before patch: `09d4a1cb1664719cb8df255f371d496b5bbcb112f5611d63c742055bf495f193`

## Conductor decision

Round 34 proves the complete two-axis Cauchy--Green ledger at fixed finite
contours and its stratumwise application to the full pre-limit M1 vector.
It does **not** prove that the same operation is defined after the accepted
endpoint, arithmetic, and radial-side modules have taken their physical or
nested limits.

For

\[
 \Theta_\beta(\mu,\nu)=\psi\!\left(t-\frac{\mu+\nu}{2}\right),
 \qquad F_j=L_j+H_{j,+}-H_{j,-},
\]

let \(P_j\) be the coordinate-axis residue and \(A_j\) the positive area
operator. Then the right-to-left transfers satisfy

\[
\boxed{
\begin{aligned}
R_uR_v[\Theta_\beta Q]={}&F_uF_v[\Theta_\beta Q]
 +F_uP_v[\Theta_\beta Q]+P_uF_v[\Theta_\beta Q]
 +P_uP_v[\Theta_\beta Q]\\
&+\frac12F_uA_v[\psi'Q]+\frac12P_uA_v[\psi'Q]
 +\frac12A_uF_v[\psi'Q]+\frac12A_uP_v[\psi'Q]\\
&+\frac14A_uA_v[\psi''Q].
\end{aligned}}
\tag{34.1}
\]

Expanding every \(F_j\) gives exactly sixteen strata. These comprise all
pure boundary products, both pure axis families, both connector-boundary
families, both connector-axis families, one mixed product-area density
\(+\psi''(\beta)/4\), and one joint corner. The independent \(v\)-then-\(u\)
and \(u\)-then-\(v\) derivations agree by finite Fubini, commuting mixed
derivatives, and the common combined-residue convention. The proof keeps
the actual profiles, floors, stars, \(\chi_4\), radial factors, and the
external \(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) normalization unchanged.

The decisive scope correction is that (34.1) acts lawfully on the **full
finite pre-limit vector package**. The endpoint and recombined \(R_1\)
arithmetic estimates are accepted only after physical profile limits, and
the renormalized radial sides vanish only under a prescribed nested
\(S=S(X,U,V)\) exhaustion. No accepted theorem commutes (34.1) with either
operation. Thus the unique post-module endpoint-free axial vector remains
open.

No numerical experiment or external theorem was used.

## Exact finite product identity

On positively oriented finite rectangles, with both horizontal faces
parametrized left-to-right,

\[
 R_j[cQ]=F_j[cQ]+P_j[cQ]-A_j[(\partial_jc)Q].
\tag{34.2}
\]

Because

\[
 \partial_\mu\Theta_\beta=\partial_\nu\Theta_\beta
 =-\frac12\psi'(\beta),\qquad
 \partial_\mu\partial_\nu\Theta_\beta
 =\frac14\psi''(\beta),
\tag{34.3}
\]

the first connectors have positive coefficient \(1/2\) and the mixed
connector has positive coefficient \(1/4\). Applying (34.2) to every
output of the first transfer yields (34.1). In particular, transferring
the first connector necessarily produces its opposite-axis boundary,
opposite-axis residue, and mixed product-area term.

The adopted sequential residue convention assigns

\[
 P_uP_v[\Theta_\beta Q]
 =(2\pi i)^2\psi(t)
 \operatorname*{Res}_{u=0}\operatorname*{Res}_{v=0}Q
\tag{34.4}
\]

once. Equivalently, one may use full-axis inclusion--exclusion
\(P_u^{\rm full}+P_v^{\rm full}-P_{uv}\). Mixing these conventions is
forbidden.

If an axial pole meets an artificial or arithmetic divisor, separate
simple residues are not added. One first uses the common meromorphic
integrand and extracts the single combined iterated or derivative
coefficient. Hence applying the same finite transfer to
\(G=E_1+R_1\) preserves the artificial-pole cancellation on every face,
connector, axis, and corner stratum.

## Actual pre-limit vector

At fixed finite \(U,V,S\), the terminal density contains

\[
\begin{aligned}
 Q_T={}&\mathbf1_{hq=m}\chi_4(q)
 \sum_j\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
 \left(\frac hq\right)^{(u+v)/2}\\
 &\qquad\times G_v(1-s)K_{u+v}(1-s)m^{-s},
\end{aligned}
\tag{34.5}
\]

together with both finite renormalized radial sides, the finite arithmetic
density, and every endpoint/artificial/arithmetic stratum not yet removed
by an exact finite identity. Formula (34.1) applies linearly to each of
these strata. This is the accepted actual pre-limit ledger.

Changing to sheared \((A,v)\) coordinates does not turn the product
rectangle into an independent rectangle. Its slanted images and their
connector traces must be retained. Replacing them by rectangular
\((A,v)\) cutoffs changes the operator.

## First open commutators

Let \({\mathsf X}_{uv}\) denote the complete finite operation (34.1),
\({\mathsf P}_{\rm phys}\) the accepted endpoint/arithmetic physical
module, and \({\mathfrak S}_{\rm rad}^{(M)}\) the renormalized finite
radial sides. The first unproved interfaces are

\[
 {\cal C}_{\rm phys}^{uv}
 =\lim_{\rm phys}{\mathsf X}_{uv}{\mathsf P}_{\rm fin}
  -{\mathsf X}_{uv}\lim_{\rm phys}{\mathsf P}_{\rm fin},
\tag{34.6}
\]

and

\[
 {\cal C}_{\rm side}^{uv}
 =\lim_{\substack{U,V,S\to\infty\\S=S(X,U,V)}}
   {\mathsf X}_{uv}{\mathfrak S}_{\rm rad}^{(M)}
 -{\mathsf X}_{uv}
   \lim_{\substack{U,V,S\to\infty\\S=S(X,U,V)}}
   {\mathfrak S}_{\rm rad}^{(M)}.
\tag{34.7}
\]

Neither is known to vanish. The new shares to control include transferred
horizontals, connector boundaries, connector-axis residues, the mixed
\(\psi''/4\) term, and the filtered corner. Therefore the finite algebraic
complement is defined, but its identification with a post-module physical
operator is conditional on (34.6)--(34.7).

## Evidence assessment

- The statement-only blind derivation independently obtains all sixteen
  terms, both transfer orders, the positive mixed sign, and the one-corner
  convention.
- The discovery report inserts the actual finite terminal, side, and
  arithmetic strata and isolates the two exact limit commutators.
- The hostile audit independently certifies the finite product identity
  and rejects the post-module conclusion without a commutation theorem.
- The conductor rederived the one-axis sign, the product tensor calculus,
  the actual stratum schema, and the limit-order alternatives.

The three reports agree on the promotable scope. The blind report's phrase
“endpoint-free vector application” is read only as a finite algebraic
complement, not as an already side-removed physical kernel.

## State effect

- promote the complete finite sixteen-stratum product Cauchy--Green lemma;
- promote its stratumwise actual pre-limit application, order independence,
  common artificial-pole cancellation, and combined collision convention;
- revise and retain open the post-module complete axial-vector obligation;
- create separate open side-exhaustion and physical-module commutation
  obligations, with a common parent compatibility interface;
- reject automatic commutation of outside-axis transfer with either limit,
  premature deletion of finite endpoint/side strata, and rectangularization
  of the sheared \((A,v)\) domain;
- retain the axial-subtracted terminal symbol, complete beta transition,
  M9-M1, M9-M2, M9, and the Gauss-circle target as open.

The next round attacks only (34.7): whether arbitrary-order radial endpoint
subtraction supplies enough uniform decay for **all sixteen** transferred
side strata under the accepted nested exhaustion.
