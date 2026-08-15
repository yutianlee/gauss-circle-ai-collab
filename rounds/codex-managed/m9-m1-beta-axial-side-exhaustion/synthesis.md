# Round 35 synthesis: compact beta support kills the transferred radial sides exactly

Campaign: `m9-m1-beta-axial-side-exhaustion`  
Round type: beta axial side-exhaustion commutation  
Graph SHA-256 before patch: `c3528645fda6be30f7a1411c200c96d05d3a9445d2da24fa3f162b60c9d619d1`

## Conductor decision

Round 35 closes the radial-side component of the module-limit commutator.
The mechanism is stronger and simpler than the planned arbitrary-order
decay audit: the fixed compact beta mask separates exactly from both
radial horizontal sides.

The actual mask satisfies

\[
 \psi\in C_c^\infty(\mathbb R),\qquad
 \psi=1\text{ on }[-B_0,B_0],\qquad
 \operatorname {supp}\psi\subset[-2B_0,2B_0].     \tag{35.1}
\]

On \(w=\sigma\pm iS\), reflection gives \(s=1-w\) and
\(t=\Im s=\mp S\). For \(|\mu|\le U\), \(|\nu|\le V\),

\[
 \beta=t-\frac{\mu+\nu}{2},\qquad
 |\beta|\ge S-\frac{U+V}{2}.                     \tag{35.2}
\]

Consequently

\[
 S>\frac{U+V}{2}+2B_0                            \tag{35.3}
\]

makes \(\psi(\beta)\), \(\psi'(\beta)\), and
\(\psi''(\beta)\) identically zero on an open neighborhood of the entire
radial-side product. Every one of the sixteen finite two-axis transfer
strata therefore vanishes separately: pure faces and axes carry \(\psi\),
first connector strata carry \(\psi'/2\), and the mixed area carries
\(\psi''/4\).

Thus for every \(M\ge1\),

\[
 \mathsf X_{uv}\mathfrak S_{\rm rad}^{(M)}=0       \tag{35.4}
\]

at every sufficiently separated finite stage. A concrete witness is

\[
 M=1,qquad S=(2+X+U+V+2B_0)^2.                  \tag{35.5}
\]

No radial remainder, gamma, profile, or integration-volume estimate is
needed. This proves the beta transfer commutes with the accepted nested
deletion of renormalized radial sides. It does not touch the endpoint or
\(R_1\) arithmetic physical-profile commutator.

No numerical experiment or external theorem was used.

## Full stratum and collision audit

The Round-34 grouped cell complex has the exact capacity table

| class | count | mask coefficient | value under (35.3) |
|---|---:|---|---:|
| pure boundary products | 4 | \(\psi\) | 0 |
| boundary/axis terms and joint corner | 5 | restricted \(\psi\) | 0 |
| connector boundary terms | 4 | \(\psi'/2\) | 0 |
| connector-axis residues | 2 | restricted \(\psi'/2\) | 0 |
| mixed product area | 1 | \(\psi''/4\) | 0 |

Real-part displacements do not alter \(t,\mu,\nu\). Restricting to
\(u=0\), \(v=0\), or their corner only improves (35.2). An artificial
radial collision would require \(|\nu|=2S>V\), and the moving arithmetic
collision would require \(|\mu+\nu|=2S>U+V\), so neither divisor meets
the product. More generally, a combined derivative residue cannot revive
an identically zero local germ.

The upper and lower radial-side orientations remain correct but become
irrelevant because each side is zero separately. All actual profiles,
floors, stars, \(\chi_4\), and the external
\(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) multiplier are retained unchanged.

## Global-order interpretation

Round 21 already deletes the unmasked renormalized radial sides under a
nested exhaustion. Round 35 asks whether subsequent beta localization and
two-axis displacement create a missing image of that deleted module. They
do not: the beta-localized image is exactly zero at every sufficiently
large finite stage. Hence the beta component of the diagram commutes
without dominated convergence or a new maximal theorem.

This does not say that the other hierarchical branches vanish. Their sum
with the beta branch reconstructs the unmasked side module already handled
by Round 21. Nor does it provide a shortcut for endpoint/arithmetic terms,
which are not radial-side-supported.

## Evidence assessment

- The statement-only blind report independently derives (35.2), audits all
  sixteen strata, axes, corner, and collisions, and supplies (35.5).
- The hostile audit independently finds the same exact-zero mechanism and
  explicitly rejects extending it to a noncompact mask or physical module.
- The discovery task exceeded its timebox and was terminated. The conductor
  materialized a scoped report from the accepted inputs; it is not counted
  as an independent validation.
- The conductor separately checked the support cell, collision equations,
  and global module-order diagram.

The blind and hostile reports are sufficient independent validation of the
narrow lemma.

## State effect

- promote exact compact-support annihilation of the complete transferred
  renormalized radial-side vector;
- close `M9-M1-beta-axial-transfer-radial-side-exhaustion`, with \(M=1\)
  and (35.5) as an explicit witness;
- retain the parent module-limit compatibility obligation open solely on
  the endpoint/arithmetic physical-module commutator;
- revise the post-module axial ledger and mask compatibility nodes to name
  that single remaining boundary interface;
- reject the need for arbitrary-order side decay in the compact beta
  branch, any extension to noncompact masks, and any inference about the
  physical endpoint/arithmetic modules or terminal symbol;
- retain the beta transition estimate, M9-M1, M9-M2, M9, and the Gauss
  target as open.

Round 36 should attack exactly one object: a common finite representative
for the endpoint and recombined \(R_1\) arithmetic packages on which the
sixteen-stratum transfer can be taken before the symmetric physical limit.
