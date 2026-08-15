# Conductor mixed-connector sign calculation

Campaign: `m9-m1-beta-complete-axial-connector-ledger`  
Role: conductor sign check  
Allocation: 100% analytical/algebraic

Let \(u=x+i\mu\), \(v=y+i\nu\), and
\(\Theta=\psi(\beta)\) with
\(\beta=t-(\mu+\nu)/2\). The one-axis area density in a positive
rectangle is

\[
 2i\bar\partial_u(\Theta Q)=-\partial_\mu\Theta\,Q,
 \qquad
 2i\bar\partial_v(\Theta Q)=-\partial_\nu\Theta\,Q, \tag{34.M1}
\]

away from the poles of \(Q\). Since

\[
 -\partial_\mu\Theta=-\partial_\nu\Theta
 =\frac12\psi'(\beta),                              \tag{34.M2}
\]

both first connectors have positive one-half sign.

For the product-area term, apply the second Cauchy--Green derivative to
the first density. The mask-only contribution is

\[
 (-\partial_\mu)(-\partial_\nu)\Theta
 =\partial_\mu\partial_\nu\Theta
 =\frac14\psi''(\beta).                            \tag{34.M3}
\]

Thus the mixed mask density has positive \(+1/4\) sign. Terms where the
second derivative hits the meromorphic factor are not ordinary interior
derivatives: distributionally they are the connector-axis residues and
their small-tube boundaries. They must be kept separately rather than
absorbed into (34.M3).

As a scalar diagnostic, if \(Q\equiv1\), integrating (34.M3) over the
imaginary rectangle yields the alternating sum of \(\Theta\) on its four
corners, exactly matching sequential application of the two one-axis
fundamental theorems. This is an algebraic control, not numerical evidence.
