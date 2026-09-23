# Conductor controls for Round 171

- Campaign: m9-m2-balanced-critical-j1-two-defect-commutator-gate
- Round: 171
- Starting graph:
  4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac
- Allocation: 100% analytic/algebraic; 0% numerical
- Proposed terminal: balanced_two_defect_commutator_no_go

## Exact algebra reproduced by the conductor

For \(h'=h+p,\ k'=k+q\),

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q).
\]

The ordered endpoint-to-increment map has the displayed inverse and
multiplicity one.  If \(p=2s\) and \(h\) is odd, direct mod-\(4\)
calculation gives

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s.
\]

For \(x=2h+2s,\ y=2k+q,\ U=qx,\ V=2sy\), forward shifts give

\[
\begin{array}{c|cc}
 &M_U&M_V\\ \hline
 [D_s,\,\cdot]&2qT_s&2yT_s\\
 [D_q,\,\cdot]&xT_q&2sT_q.
\end{array}
\]

The side-sum normalizations are \(T_q,T_s\).  Direct composition also
reproduces

\[
 [2yT_s,xT_q]=2(2y-x)T_sT_q
\]

and, with \(\widehat T_q=T_q^2\),

\[
 [2yT_s,2x\widehat T_q]=8(y-x)T_s\widehat T_q.
\]

Every fixed-width affine singular strip has three free length-\(L\)
coordinates and hence \(O_{C,\varepsilon}(L^3X^\varepsilon)\) absolute
mass.  Off either strip, division returns a shift, and reindexing against
\((-1)^s\) returns \(-2\) times the original scalar.

For the endpoint swaps on the invariant endpoint rectangle, the coefficient
is real and

\[
 P_{+-}W=P_{-+}W=0.
\]

Self-adjointness of the swaps reproduces

\[
 \langle W,H\rangle_G
 =\langle P_{++}W,P_{++}H\rangle_G
 +\frac1{16}\langle D_hD_kW,D_hD_kH\rangle_G.
\]

The sole \((++)\) complement is not zero.  The nonnegative
erased-structure control shows why positive projection closure can retain
\(L^4X^\varepsilon\) capacity, without implying physical lower mass.

Finally, finite reindexing gives

\[
 \mathcal R_B^{\rm osc}
 =\frac12\sum(-1)^s(q-q_0)D_sD_qF.
\]

If a coefficient-independent first-difference primitive represents the
constant weight on an \(N\)-point interval, coefficient comparison forces
\(c(r)-c(r+1)=1\), and therefore \(\max|c|\ge N/2\).  Ambient balanced
geometric/profile fibres have \(N\asymp L\).

## Restoration and boundary controls

The final kernel uses:

- the invariant endpoint rectangle \(I_h^2\times I_k^2\), expressed in
  shift coordinates by \(h,h+p\in I_h,\ k,k+q\in I_k\);
- piecewise zero extension before evaluating a square root;
- the full reconstructed mod-\(4\) and mod-\(2\) inverse conditions;
- a geometric/profile support indicator \(J\), with both arithmetic
  low-gcd weights retained in the coefficient;
- the exact three-factor edge expansion for \(I=JH^\Delta H^\rho\);
- both strict gates, both axes, both slanted factors, floors, stars,
  crossings, endpoints, and the real centre;
- corner-dependent aliases and lifts only if their accepted expansion is
  opened; and
- the accepted fixed-\(Q\) formulas and ruling scope.

The one-step geometric-support and gate faces have the accepted unweighted
positive ledger \(O_\varepsilon(L^3X^\varepsilon)\).  The forced ramp
restores only the available coefficient-independent positive ledger to
\(L^4X^\varepsilon\); no literal lower bound is asserted.

## Required control matrix

| control | conductor outcome |
|---|---|
| literal critical \(j=1\) owner | GREEN |
| coordinate bijection and multiplicity | GREEN |
| complete character congruences | GREEN |
| \(p=0,q=0\) axes | GREEN at \(L^3X^\varepsilon\) |
| normalized displayed commutators | GREEN as shift tautologies |
| two displayed unnormalized commutators | GREEN after singular-strip pricing |
| undisplayed composite/weighted/nonlocal commutators | OUTSIDE THE NO-GO |
| actual-real endpoint swap | GREEN with one \((++)\) complement |
| local \(q\)-primitive lower bound | GREEN |
| geometric support and gate product rules | GREEN |
| arithmetic gcd holes | RETAINED IN THE COEFFICIENT |
| fixed-\(Q\) rulings | SURVIVE; positive broad--narrow remains parked |
| constant-character/erased-structure controls | FALSIFY COEFFICIENT-UNIFORM CLOSURE ONLY |
| phase-adapted control | CAPACITY DIAGNOSTIC ONLY |
| factor \(L\) before positive norm | FAILS FOR THE AUDITED ROUTE |
| physical target or lower bound | NOT PROVED |
| remaining BAL labels and downstream scope | QUARANTINED |

## Conductor conclusion

The smallest stable result is the route-scoped obstruction in
proofs/kernels/m9_m2_balanced_two_defect_commutator_ramp_obstruction.md.
It licenses a proved-internal obstruction node with no implication edge.
The critical remainder and equivalent energy remain open.  No balanced
parent, M9--M2 parent, M9 node, bridge, theorem, or exponent changes.
