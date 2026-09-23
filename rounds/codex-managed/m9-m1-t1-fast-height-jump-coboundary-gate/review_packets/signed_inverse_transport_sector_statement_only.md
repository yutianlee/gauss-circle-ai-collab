# Statement-only review packet: signed-inverse transport sector

Fix the exact Round-189 fast packet with

\[
 Q=\lfloor(\log(2X))^B\rfloor,\qquad Y<h\le 2Y,\qquad
 U=mq\mid u,\qquad g=u/U,
\]

\[
 U>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,
 \quad (u,v)=1,
\]

and retain every literal selector, endpoint coefficient, phase, affine
site, orientation, and zero extension.  The inherited fixed-row bound is

\[
 |W_{v,\omega}(h)|\ll_\varepsilon \kappa X^\varepsilon,
\]

the literal \(v\)-support has length \(O(u)\), and the exact Fourier
lift is \(c_{mq}(ma)=m^{-1}c_q(a)\), with
\(\sum_{(a,q)=1}|c_q(a)|\ll\log(2q)\).

For each unit \(v\bmod U\), let \(\varrho=\varrho_U(v)\) be the signed
least inverse and define \(\gamma\in\mathbb Z\) by

\[
 \varrho v-\gamma U=1,
 \qquad -(U-1)/2\le\varrho\le(U-1)/2.
\]

The oriented determinant fibres are

\[
 Sv-Uw=h\quad(\omega=+),\qquad Uw-vS=h\quad(\omega=-),
\]

with canonical representatives \(S_{0,\omega}(h)\in[0,U)\) and affine
coordinates \(S=S_{0,\omega}(h)+Ut\).  Put

\[
 \epsilon_+=1,\qquad\epsilon_-=-1,
\]

\[
 \nu_\omega(h)=
 \frac{S_{0,\omega}(h)-\epsilon_\omega\varrho
       -S_{0,\omega}(h-1)}{U}.
\]

Independently verify or refute each of the following proposed claims.

1.  The map
    \((S,w)\mapsto(S-\epsilon_\omega\varrho,
    w-\epsilon_\omega\gamma)\) carries the height-\(h\) fibre exactly
    to height \(h-1\), \(\nu_\omega(h)\in\{-1,0,1\}\), the affine index
    changes by \(t\mapsto t+\nu_\omega(h)\), and the affine parity
    changes by \((-1)^{\nu_\omega(h)}\).

2.  Before the Fourier split, the complete parity
    \((-1)^{S_{0,\omega}(h)+t}=(-1)^S\), using odd \(U\), changes under
    either orientation by the constant \((-1)^\varrho\).  Decide
    whether this constant identity is preserved by one retained Fourier
    mode or only by the complete Fourier reconstruction.

3.  With

    \[
    T_\varrho=\min\{(U-1)/2,\lfloor QmU/Y\rfloor\},
    \]

    the row sector \(0<|\varrho_U(v)|\le T_\varrho\), intersected with
    the exact Round-189 fast packet, is absolutely target-safe at fixed
    \((\kappa,u,m,q,a)\): its complete original row sum is
    \(O_\varepsilon(Qm\kappa uX^\varepsilon)\).  Audit empty and
    saturated cases, the multiplicity of \(v\)-classes, both
    orientations, the \(m^{-1}\) lift, coefficient mass, divisor ledger,
    and the final \(O_{B,\varepsilon}(L^2X^\varepsilon)\) scale.

4.  For the complementary rows, test whether the two terminal changes
    from the interval support in height and the exact Fejer difference
    \(F(h)-F(h-1)=-2\kappa g/\lceil L\rceil\) are individually
    target-safe after the \(q/J\) Abel factor and projective-band count.

5.  Determine whether any of these facts proves cancellation for the
    remaining transported endpoint, mask, carry, affine birth/death, or
    square-root-phase terms.  Locate the first missing estimate and its
    exact power deficit.  Arbitrary bounded arrays may certify only an
    operator-class insufficiency, not a lower bound for the fixed literal
    coefficient.

The review must be statement-only: do not read the Round-191 strategy,
reports, controls, candidate, sibling reviews, proof graph, or proof
draft.  It must give exact hypotheses, derivations, the first doubtful
step, controls, dependencies, and recommended state effect.  Write only
to
`reviews/blind_signed_inverse_transport_sector_review.md`.
