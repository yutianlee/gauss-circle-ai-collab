# Conductor Round-197 adjudication

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Starting graph SHA-256:
  `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Final candidate SHA-256:
  `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`
- Durable kernel SHA-256:
  `6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467`
- Numerical theorem evidence: none

## 1. Decision

Round 197 does not prove complete \(P_2\) and does not produce a genuine
target-safe four-corner rectangle on the full Round-195 open packet.
It proves one narrower physical lower-swap sector.

On

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1},
 \qquad d=g\alpha,\quad d'=g\beta,
\]

let \(C_{\rm lit}\) assert equality of the explicit arithmetic/support
and sharp-branch code at the two lower allocations
\((m,g\alpha)\) and \((\alpha,gm)\), and put
\(P_{\rm cc}=P_0C_{\rm lit}\).  The code contains no coefficient value,
selector value, BV-profile value, smooth-factor value, or nonvanishing
test.  It is symmetric under the lower swap.  No nonemptiness, density,
or positive mass is asserted.

The durable kernel proves

\[
 \boxed{
 |\mathscr R_{\rm core,out}^{\sigma}(P_{\rm cc}W)|
 +|\mathscr R_{\rm open,out}^{\sigma}(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\rm sel},\varepsilon}L^2X^\varepsilon.}
\]

The open operator is the exact Round-195 packet region

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

This is a subordinate strict-sector theorem only.

## 2. Proof selected

The valid mechanism is the lower single-swap

\[
 \tau_0(g\alpha,m,g\beta,m')=(gm,\alpha,g\beta,m').
\]

The condition \((m,\beta)=1\) preserves the recomputed gcd \(g\), while
\((\alpha,\beta)=1\) supplies the reverse cross condition.  The products,
shift, Fejer factor, radical phase, and physical defects are unchanged, and
\(\chi_4(\alpha m)=-1\) reverses the character.  Pairing before positive
norms gives the actual coefficient difference

\[
 \lambda_{N,\sigma}(g\alpha)-\lambda_{N,\sigma}(gm).
\]

On a common live code, its exact three-term rule is the smooth difference,
the normalized-BV difference, and the selector commutator.  Lower closeness
and the cone give the uniform accepted bound \(g\le G_0\).  The smooth
piece gains \(D_L/L\); the aggregate BV piece costs \(D_L^2\); and the
selector commutator vanishes for large \(L\), because a changed selected
prime would lie in the fixed finite divisor set of \(g\) while the two
distinct selected primes have logarithmic gap at most
\(K_{\rm sel}L^{-1/2}\).  The remaining bounded shells are absolutely
safe.

The raw outer capacity is

\[
 D_L\sum_{\kappa\ll L}(1+L/\kappa)^2
 \ll D_LL^2X^\varepsilon.
\]

Both the smooth and BV ledgers reduce this to

\[
 D_L^2L X^\varepsilon\le4L^2X^\varepsilon.
\]

Monotone and \(h\le H_B\) orbit exits are subsets of the accepted
Round-185 absolute sector.  The physical mask is inserted before spectral
operations.  The exact Round-193/Round-195 replay retains transported-mask
commutators, affine births and deaths, carries, cells, crossings, both
\(T\)-branches, all anchor/Fourier copies, zero extensions, both physical
orientations, and the single outer real part.  The Round-195 safe packet
union is subtracted only after the complete masked core estimate.

## 3. Exact obstruction and remaining seam

The formal four-corner rectangle has recomputed gcds

\[
 g,\qquad g(m,\beta),\qquad g(\alpha,m'),\qquad g(m,m').
\]

On the full cross-coprime domain its relative character table is
\((1,s_0,s_1,s_0s_1)\).  When \(s_0=s_1=-1\), it yields the desired
alternating mixed difference, but the two primitive charts force the
physical inward gcd \(\kappa=1\).  It therefore cannot cover the open
packets \(2\le\kappa<D_L\), and the simultaneous swap has multiplier
\(+1\).

The exact physical complement of the proved sector is

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\rm lit}
       \ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}.
\]

After the Round-195 packet projection, the remaining \(P_2\) region is

\[
 \{\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}
 \cap(P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}).
\]

The first unproved part is \(P_{\partial\rm lit}\).  The exact identity

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}
\]

shows that a sharp ratio face aligned with ratio \(g\) can be crossed by
every lower-close pair.  The current interface then retains
\(D_LL^2X^\varepsilon\) capacity.  This is a route no-go, not literal
nonvanishing, lower mass, or a disproof of complete \(P_2\).

## 4. Review disposition

The final candidate passed independent blind, power/operator, physical-mask,
provenance, graph-direction, protected-scope, and exponent reviews after the
explicit selector, sharp-code, coefficient-product, Farey-operator, and
finite-\(g\) repairs.  The durable kernel preserves the final mathematical
body and has exact repository-level provenance.  The bounded finite-orbit
control is diagnostic only and is not used in the theorem.

No result was selected by vote.  The single-swap common-cell theorem is the
narrowest statement common to the literal derivation, hostile audit, blind
rederivation, and all seam reviews.  The full four-corner overclaim is
rejected.

## 5. Graph and downstream scope

A valid State Patch may create one subordinate `proved_internal` node for
the common-cell sector.  It may depend on the accepted Round-184, 185, 193,
and 195 interfaces and may be added only to
`M9-M1-hard-top-high-radical-small-t-residual-estimate`, which remains open.
The accepted Round-195 node must remain unchanged; a reverse dependency
would create a cycle.

Complete \(P_2\), \(P_1\), complete original \(t=1\), all original
\(t\ge2\) incidences, the hard small-\(t\) owner, both M1 parents, GAR,
all M2 parents, endpoint uniformity, M9, both bridges, and the Gauss-circle
target remain open or conditional exactly as before.

The strongest internal exponent remains \(1/3\), the accepted external
benchmark remains \(0.3144831759740614\ldots\), and the target remains
\(1/4\).  No exponent improves.

Round 197 closes under the frozen terminal label
`p2_four_corner_orbit_boundary_self_return_no_go`, subject to a mechanically
valid State Patch and reverse/replay audit.  Round 198 is the mandatory
full-proof strategy and current-primary-literature checkpoint.
