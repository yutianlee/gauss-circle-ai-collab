# Conductor full-partition recombination

Campaign: `m9-m1-beta-mask-endpoint-axial-compatibility`  
Role: conductor exact-algebra review  
Allocation: 100% analytical/algebraic

## 1. Three hierarchical masks

Write

\[
 \Theta_\beta=\psi(\beta),\qquad
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),\qquad
 \Theta_o=(1-\psi(\beta))(1-\psi(\alpha)).          \tag{33.P1}
\]

Then \(\Theta_\beta+\Theta_\alpha+\Theta_o=1\). Along the radial
\(A\)-rectangle, \(\partial_\beta\alpha=1\), and direct differentiation
gives

\[
 \partial_\beta\Theta_\beta
 +\partial_\beta\Theta_\alpha
 +\partial_\beta\Theta_o=0.                        \tag{33.P2}
\]

Hence the three Cauchy--Green area connectors cancel exactly. At the
arithmetic pole \(A=0\), \(\beta=0\), so \(\Theta_\beta=1\) and the two
complements vanish. The full arithmetic residue is owned by the beta
branch. At a general endpoint or artificial pole, the three mask values
sum to one but need not be individually zero or one.

Applying the exact masked endpoint identity to all three branches and
summing therefore yields

\[
 \sum_{\gamma\in\{\beta,\alpha,o\}}
 (T_{\xi,\gamma}+S_{\xi,\gamma}+P_{\xi,\gamma}
   +C_{A,\xi,\gamma})
 =D_\xi-A_\xi.                                     \tag{33.P3}
\]

This is precisely the accepted unmasked endpoint identity. It is (33.P3),
not the beta identity alone, that licenses the proved physical endpoint
module.

## 2. Boundary-first order

The clean exact order is:

1. apply endpoint subtraction and (33.P3) to the global finite operator;
2. cancel the artificial \(E_1/R_1\) residue and recombine the arithmetic
   share into \(R^{\rm ar}[R_1]\);
3. pass the complete unmasked endpoint and arithmetic packages to their
   accepted physical-profile modules;
4. partition only the endpoint-image-free remainder by (33.P1);
5. on its beta branch, perform the finite Cauchy--Green and axial
   displacements with every induced connector and corner retained.

This order gives the exact endpoint-free beta object
\(\Theta_\beta R_1\) without ever estimating a masked endpoint prefix.
It is equivalent to summing all three masked endpoint identities before
removing their common endpoint output. It is not equivalent to deleting
\(D_\xi^\beta\) inside the beta branch alone.

## 3. Axial recombination

At fixed \(s,u\),

\[
 -\partial_\nu\Theta_\gamma
\]

is the Cauchy--Green density for the finite \(v\)-shift. Since the masks
sum to one, these three axial area connectors also sum to zero. On
\(v=0\), their mask values sum to one, so their vector residues recombine
to the unmasked residue. The same holds for \(u=0\). At \(u=v=0\), the
sequential two-axis expansion owns the joint corner once; summing masks
again gives weight one.

Within the beta branch alone the axial mask weights are generally not one,
so its connector-completed axial vector remains a genuine masked operator.
It is not part of the already proved endpoint estimates and requires its
own analytic treatment.

## 4. Ownership conclusion

For the prescribed global-collapse-before-mask order, the endpoint-free
operation is common and linear on \(G,E_1,R_1\). Thus

\[
 {\cal E}_{\rm own}={\cal H}[G-E_1-R_1]=0           \tag{33.P4}
\]

meromorphically, and its fixed-physical-height \(L\)-derivative vanishes
distributionally. The first nonzero survivor is not a rho defect. It is
the connector-completed, masked axial vector on the endpoint-free beta
terminal remainder.

No estimate, height limit, or external theorem is used here.
