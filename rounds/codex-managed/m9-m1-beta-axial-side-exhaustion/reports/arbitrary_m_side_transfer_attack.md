# Round 35 discovery report: support-separated radial-side transfer

Task: `arbitrary_m_side_transfer_attack`  
Role: discovery, conductor-materialized after task timebox  
Allocation: 100% analytical/algebraic; no computation or external theorem

## 1. Result

The actual compact beta mask makes the desired commutation exact, without
an arbitrary-order decay estimate. If

\[
 \psi=1\text{ on }[-B_0,B_0],\qquad
 \operatorname {supp}\psi\subset[-2B_0,2B_0],
\]

then on either reflected radial side every one of the sixteen transferred
strata vanishes identically whenever

\[
 S>\frac{U+V}{2}+2B_0.                             \tag{35.1}
\]

Thus any endpoint-subtraction depth \(M\ge1\) works; one explicit choice is

\[
 M=1,\qquad S=(2+X+U+V+2B_0)^2.                  \tag{35.2}
\]

This proves the radial-side transfer commutator is zero in the frozen beta
branch. It does not address endpoint or arithmetic physical modules.

## 2. Exact statement and hypotheses

Let \(w=\sigma\pm iS\) be the two radial sides and \(s=1-w\), so
\(t=\Im s=\mp S\). On the finite outside rectangles put
\(u=a+i\mu\), \(v=b+i\nu\), with \(|\mu|\le U\),
\(|\nu|\le V\), and

\[
 \beta=t-\frac{\mu+\nu}{2}.
\]

Apply the proved finite sixteen-stratum product Cauchy--Green transfer to
the beta-masked renormalized side \(\psi(\beta)R_{M,v}\), with common
artificial-pole ownership and combined residues at collisions. Retain all
actual profiles, floors, stars, \(\chi_4\), and the external
\(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) factor.

## 3. Proof or derivation

On both radial sides,

\[
 |\beta|\ge S-\frac{U+V}{2}>2B_0.                 \tag{35.3}
\]

Hence \(\psi(\beta)\), \(\psi'(\beta)\), and
\(\psi''(\beta)\) vanish on an open neighborhood of the full product.
The sixteen transferred strata have coefficients as follows:

| class | count | coefficient | value |
|---|---:|---|---:|
| pure boundary products | 4 | \(\psi\) | 0 |
| boundary/axis and joint corner | 5 | restricted \(\psi\) | 0 |
| connector boundaries | 4 | \(\psi'/2\) | 0 |
| connector-axis residues | 2 | restricted \(\psi'/2\) | 0 |
| mixed product area | 1 | \(\psi''/4\) | 0 |

Restrictions to \(u=0\), \(v=0\), or their corner only decrease the
height range. Real-part displacements do not change \(t,\mu,\nu\).
Artificial radial collision requires \(|\nu|=2S>V\), and the moving
arithmetic collision requires \(|\mu+\nu|=2S>U+V\); neither meets the
product. A combined derivative residue cannot revive an identically zero
local germ.

Therefore the upper and lower sides vanish separately before integration,
and

\[
 \mathsf X_{uv}\mathfrak S_{\rm rad}^{(M)}=0       \tag{35.4}
\]

at every sufficiently separated finite stage. The nesting (35.2) also
dominates \(X+U+V\), so it lies inside the accepted radial-side regime.
Taking the nested limit proves both orders give zero.

## 4. First doubtful or unproved step

No step remains open in the beta-masked radial-side lemma. The next open
interface is different: transferring the finite endpoint and recombined
\(R_1\) arithmetic packages through their symmetric physical-profile
limits. Those terms are not supported on \(t=\pm S\), so (35.3) gives no
information about them.

## 5. Required control tests and outcomes

- **Arbitrary-M decay:** not needed; exact localization gives zero and
  \(M=1\) suffices.
- **All sixteen strata:** pass by the displayed coefficient table.
- **Axes, collisions, and corner:** pass by support margin and the collision
  equations above.
- **Nested exhaustion:** pass with the explicit polynomial (35.2).
- **Actual profiles and normalization:** pass because the zero mask
  multiplies the unchanged full density before any simplification.
- **Scope:** pass; no physical endpoint/arithmetic commutation or symbol
  estimate is claimed.

## 6. Dependencies and exact artifacts used

This conductor-materialized report uses `protocol.md`,
`state/proof_obligations.yml`, `state/active_campaign.yml`, the Round-21
radial endpoint-renormalization synthesis and reports, the Round-34 actual
finite ledger and synthesis, the fixed compact mask from Round 26, and the
conductor support/cell audits in this campaign. It uses no numerical test,
web source, or external theorem. The originally assigned discovery task was
terminated at its timebox without a report; this derivation is therefore
not counted as an independent claimant validation.

## 7. Recommended state effect

Promote the compact-support radial-side transfer lemma and close
`M9-M1-beta-axial-transfer-radial-side-exhaustion`. Record that exact
support separation, not arbitrary-order decay, is the mechanism. Retain
the physical-module commutator, its parent compatibility obligation, the
post-module axial ledger, axial-subtracted symbol, beta estimate, M9-M1,
M9, and the target as open.
