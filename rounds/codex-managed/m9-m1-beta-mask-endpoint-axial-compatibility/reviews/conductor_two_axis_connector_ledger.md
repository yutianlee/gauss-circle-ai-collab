# Conductor two-axis connector ledger

Campaign: `m9-m1-beta-mask-endpoint-axial-compatibility`  
Role: conductor sign and corner audit  
Allocation: 100% analytical/algebraic

## 1. One-axis formula

At fixed \(s,u\), let \(v=x+i\nu\) and

\[
 \Theta(v)=\psi\!\left(t-\frac{\mu+\nu}{2}\right).
\]

For upward verticals and horizontal segments parametrized left-to-right,
positive orientation gives

\[
 V_{b_+}[\Theta Q]=V_{b_-}[\Theta Q]
 +H_+[\Theta Q]-H_-[\Theta Q]
 +2\pi i\operatorname {Res}_{v=0}(\Theta Q)
 -\iint\partial_\nu\Theta\,Q.                     \tag{33.X1}
\]

Because \(\partial_\nu\Theta=-\psi'(\beta)/2\), the last term is
\(+\frac12\iint\psi'(\beta)Q\). It is generally nonzero. The same
formula holds in \(u\), with \(\partial_\mu\Theta=-\psi'(\beta)/2\).

## 2. Sequential shifts

Apply the \(v\)-shift first and then the \(u\)-shift to every resulting
stratum. The second shift acts not only on the terminal vertical and pure
\(v=0\) residue, but also on the \(v\)-horizontals and on the area
connector in (33.X1). Since

\[
 \partial_\mu\partial_\nu\Theta=\frac14\psi''(\beta),
                                                               \tag{33.X2}
\]

the mixed operator contains a two-dimensional connector density, its
finite boundary traces, and the \(u=0\) residue of the first connector.
Pure residues alone are therefore not a complete two-axis ledger.

There are two equivalent corner conventions:

1. list the pure \(u\)- and \(v\)-axis shares with their joint corner
   removed, then add the corner once positively; or
2. use full axis shares and inclusion--exclusion
   \(R_u+R_v-R_{uv}\).

Mixing these conventions double-counts the corner. The Round-33 state
should record only the convention-independent assertion: the complete
sequential Cauchy--Green operator contains the joint corner exactly once,
along with every connector-axis and mixed-connector stratum.

## 3. Scope

The common operation applied identically to \(G,E_1,R_1\) is linear, so
its rho ownership defect vanishes. This does not show that the connector
strata vanish or are target-safe. They form part of the remaining masked
axial vector operator.

No computation or external theorem was used.
