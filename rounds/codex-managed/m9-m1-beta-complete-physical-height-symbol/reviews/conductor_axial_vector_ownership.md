# Conductor axial vector ownership ledger

Campaign: `m9-m1-beta-complete-physical-height-symbol`  
Role: conductor finite-contour audit  
Allocation: 100% analytical/algebraic

## 1. Positive outside lines do not yet cross the axial pole

In the accepted finite vector kernel the outside \(u\)- and \(v\)-lines
remain at positive real parts. Hence \(v=0\), \(u=0\), and their joint
corner are not residues of the terminal radial shift itself. If the
\(v\)-line is subsequently moved, the exact height residue is a separate
two-variable vector coefficient

\[
 R_v=\frac{\delta}{(2\pi i)^2}\sum_j\int_u\int_s
 \widehat W_j(u)\left(\frac{D_j}{2\sqrt X}\right)^u
 \left(\frac hq\right)^{u/2}
 G_0(1-s)K_u(1-s)m^{-s}\,ds\,du,                    \tag{32.V1}
\]

with the top residue \(R_u\) and joint corner \(R_{uv}\) separately
defined. The same residue operation must be applied to radial sides and
arithmetic pieces, and finite horizontal height connectors remain.

## 2. Consequence for axial subtraction

Subtracting \((b+i\nu)^{-1}\) locally from the terminal height transform
is not by itself the exact global \(v=0\) residue operation. It becomes
legitimate only after a finite \(v\)-contour displacement that produces:

1. the terminal \(R_v\) share;
2. the matching radial-side and arithmetic shares;
3. both finite \(v\)-horizontal connectors;
4. the \(u=0\) interaction and joint corner exactly once.

Therefore the proposed axial-subtracted terminal kernel is conditional on
an ownership theorem that reconciles all these shares. A local polar
decomposition can diagnose norm loss, but cannot replace this contour
identity.

## 3. Correct Round-32 decomposition

The finite operator should remain the sum of:

- a side-collapsed, endpoint-free terminal beta remainder on \(b>0\);
- the exact finite \(v\)-displacement identity with \(R_v\), connectors,
  arithmetic/side shares, and corner;
- already accepted radial endpoint and arithmetic modules;
- the renormalized-side removal under nested heights.

Only after the second item is proved target-safe may one pass to an
axial-subtracted terminal symbol with polylogarithmic weight.

## 4. Smallest likely survivor

The exact next obstruction is not the elementary norm
\(\|(b+i\nu)^{-1}\|_1\), but the connector-completed finite \(v\)-axis
operator. It couples the terminal transition, radial boundary, and corner
ledgers. The existing proof graph lists it but does not estimate it at the
target scale.

This points to a likely Round-32 no-go/revision: split the literal complete
symbol target into a terminal side-collapsed symbol lemma and an axial
vector compatibility theorem. No target promotion is justified until both
are closed.
