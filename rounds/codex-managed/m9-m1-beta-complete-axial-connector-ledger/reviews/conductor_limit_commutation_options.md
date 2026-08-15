# Conductor options for avoiding an unjustified limit commutation

Campaign: `m9-m1-beta-complete-axial-connector-ledger`  
Role: conductor strategy review  
Allocation: 100% analytical/algebraic

## Option A: shift before every limit

Apply the sixteen-term two-axis identity to the full finite split vector
package, including \(E_M\), \(R_M\), radial sides, and the unsplit
arithmetic residue. Then perform endpoint Cauchy collapse, artificial-pole
recombination, and the three-mask endpoint recombination on **each of the
sixteen strata**. Finally take the physical profile and nested radial-side
limits stratum by stratum.

This order is exact at finite height but requires new uniform estimates for
the connector images of every endpoint and side stratum. The existing
endpoint and side theorems do not state those estimates.

## Option B: take boundary limits before outside shifts

First use global endpoint collapse and the accepted physical-profile and
nested-side limits. Then apply outside-axis shifts only to the remaining
terminal beta operator.

This avoids connector images of the removed modules, but it requires an
exact limiting terminal integrand and a theorem permitting finite contour
shifts after the limits. The current graph supplies a physical endpoint
sum and a residual transition operator, but not a single post-limit
meromorphic \((u,v)\) density on a finite rectangle.

## Option C: define an algebraic complement

At finite height, define

\[
 \mathcal V_{\rm ef}^{\rm fin}
 :=\mathcal X_u\mathcal X_v(\mathfrak I^c)
 -\mathcal X_u\mathcal X_v(\mathfrak E_M)
 -\mathcal X_u\mathcal X_v(\mathfrak R^{\rm ar}_{\rm assigned}),
\]

with exact endpoint/artificial/arithmetic ownership. This is a legitimate
finite algebraic complement. One may then formulate, but not assume, the
claim that its nested/physical limit exists and equals the axial vector of
the post-module terminal trace.

Option C is the weakest safe graph interface. It separates:

1. a proved abstract/finite two-axis identity;
2. a defined finite endpoint-free complement;
3. an open module-limit compatibility theorem;
4. a later analytic bound for the limiting axial-subtracted symbol.

The Round-34 synthesis should adopt this separation unless a report proves
one of Options A or B with the actual accepted hypotheses.
