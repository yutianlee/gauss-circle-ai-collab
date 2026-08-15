# Round 31 discovery report: physical-height BV reduction

Task: `regular_symbol_bv_attack`  
Role: discovery; conductor-materialized after the assigned task exceeded its timebox  
Allocation: 100% analytical/algebraic

## 1. Result

The complete Round-31 BV estimate is not proved. The useful discovery is a
coordinate correction and a smaller sufficient lemma.

Estimating every differentiated term separately in
\((L,\mu=L-\nu)\) cannot work: the actual height factor produces a
translation derivative with absolute mass \(\asymp_b\lambda^{-1}\), one
power larger than the desired pre-numerator \(\lambda^{-2}\). Returning
to physical height \((L,\nu)\) combines that derivative with the moving
endpoint traces. On a signed saddle cell, it is sufficient to prove for the
complete recombined regular kernel

\[
 |K(L,\nu)|\ll X^\varepsilon\lambda^{-2}w_b(\nu),
 \qquad
 |\partial_LK(L,\nu)|\ll X^\varepsilon\lambda^{-3}w_b(\nu),  \tag{31.D1}
\]

where \(w_b\in L^1\) also controls translated endpoint traces. Then the
finite-section integral has sup plus BV norm
\(O(X^\varepsilon\lambda^{-2})\), and the accepted numerator
\((D_j/q)\lambda\) preserves local \(q^{-2}\).

The separated fixed-\(b\) \(R_1\) two-denominator kernel satisfies this
mechanism away from \(\rho=0\). The first unproved step is (31.D1) for the
complete omega-recombined package, axial term, and finite radial sides,
uniformly under height exhaustion.

## 2. Exact statement and hypotheses

Let

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U],\qquad
 R(L)=\int_{I_{U,V}(L)}K(L,\nu)\,d\nu.              \tag{31.D2}
\]

Assume a saddle cell has length \(O(\lambda)\), (31.D1) holds, and any
moving trace \(K(L,L\mp U)\) obeys the same integrable weight after the
substitution \(\nu=L\mp U\). Then

\[
 \|R\|_\infty+\operatorname {Var}R
 \ll X^\varepsilon\lambda^{-2}\|w_b\|_1.           \tag{31.D3}
\]

For the actual complete target, \(K\) must be formed after:

1. recombining \(\omega G+(1-\omega)R_1-\omega E_1\) with identical
   masks, domains, and endpoints;
2. taking the signed top Plemelj limit;
3. removing the single combined delta/log diagonal term; and
4. retaining actual profiles, floors, stars, connectors, and radial sides.

## 3. Proof or derivation

On every affine cell write the endpoints of (31.D2) as \(p(L),q(L)\).
Leibniz gives

\[
 R'(L)=\int_p^q\partial_LK(L,\nu)d\nu
 +q'(L)K(L,q(L))-p'(L)K(L,p(L)).                   \tag{31.D4}
\]

The interior variation is

\[
 O(\lambda)\,X^\varepsilon\lambda^{-3}\|w_b\|_1
 =O(X^\varepsilon\lambda^{-2}).                    \tag{31.D5}
\]

Fixed faces \(\nu=\pm V\) have zero velocity. Moving faces
\(\nu=L\mp U\) contribute \(O(X^\varepsilon\lambda^{-2}\|w_b\|_1)\)
by substitution. Affine switches agree in value, and a collapsed section
has zero integral. This proves (31.D3).

For separated \(R_1\), after subtracting the explicit face term the exact
kernel is

\[
 K(L,\nu)=-\frac{i f_b(L)}{2A\{A+i(L-\nu)/2\}}
 +\frac{f_b(\nu)-f_b(L)}{(L-\nu)\{A+i(L-\nu)/2\}},             \tag{31.D6}
\]

with \(|A|\asymp|L|\asymp\lambda\). The accepted decay of
\(f_b,f_b',f_b''\), plus the divided-difference identity at \(\nu=L\),
gives (31.D1) on separated patches. This calculation must not be replaced
by termwise fixed-\(\mu\) estimates.

At the rho cutoff,

\[
 D\{\omega G+(1-\omega)R_1-\omega E_1\}=DR_1,       \tag{31.D7}
\]

and similarly at second order, because all omega-derivative coefficients
are derivatives of \(G-E_1-R_1=0\). This removes the cutoff derivative as
an obstruction, but supplies no bound for the remaining complete
derivative.

## 4. First doubtful or unproved step

The first exact missing estimate is (31.D1) for the complete recombined
kernel. In divided-difference notation it is the target-scale bound for

\[
 \partial_\nu(\partial_L+\partial_\nu)H_{\rm complete}.        \tag{31.D8}
\]

The available formulas control separated \(R_1\), but do not give a common
physical-height symbol for \(G,E_1,R_1\), the axial package, connectors,
and finite radial sides with identical ownership. Joint \(U,V,S\)
exhaustion and \(b\downarrow0\) also remain open.

## 5. Required controls and outcomes

- **Product rule:** termwise fixed-\(\mu\) absolute estimates fail by one
  lambda power; physical-height recombination passes conditionally.
- **Moving endpoints:** both signed traces appear in (31.D4); the narrow
  lemma passes all affine cells.
- **Residues:** omega-prime and omega-double-prime terms cancel exactly,
  but the remaining Taylor coefficients are unbounded by current evidence.
- **Profiles/floors/stars:** the actual height profile proves the separated
  lemma; constant floors and stars do not create L-variation, but their
  endpoint and scale sums remain.
- **Height exhaustion:** fixed-b separated tails pass; axial residue, radial
  sides, and joint exhaustion remain open.
- **Pointwise versus BV:** a pointwise \(q^{-2}\) estimate alone is
  insufficient; (31.D1) is genuinely stronger.

## 6. Dependencies and artifacts used

Used the Round-31 brief and permitted Round-26, Round-27, and Round-30
syntheses and conductor derivative scope. No computation or external
theorem was used. The assigned discovery task exceeded its report timebox;
the conductor materialized this scoped report from the completed algebra
and independently checked it against the blind and hostile ledgers.

## 7. Recommended state effect

Promote only the physical-height finite-section BV implication
(31.D1)--(31.D5), the separated \(R_1\) application (31.D6), and exact
cutoff-derivative cancellation (31.D7). Reject termwise absolute BV in
fixed-\(\mu\) coordinates. Retain the complete symbol BV obligation, beta
transition, M9-M1, M9, and Gauss target as open. The next target is the
common recombined physical-height symbol and estimate (31.D8), including
the axial and radial-side exhaustion ledger.
