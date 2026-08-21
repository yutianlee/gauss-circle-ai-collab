# Round 90 synthesis

## Objective and outcome

Round 90 tested whether the complete surviving first-band M1 operator
acquires a new loss under the R82--R89 A-process, completion, and local
classifications.  It does not.  The late object is the exact Fejer Gram
lift of the deep Round-82 centered Kloosterman-product correlation, and
the late capacity is the square of the Round-82 capacity at the
corresponding norm level.

This is a square-root equal-capacity barrier, not a proof of the hard
signed estimate and not a linear involution.

## Exact reassembly

For the normalized physical rows, summing distinct ordered unit pairs
gives exactly

\[
 {1\over M^2}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

Its Fejer Gram expansion is the complete four-row symbol used in
Rounds 87--89.  The \(u=0\) coefficient is the whole global diagonal
and is owned once.  On \(u\ne0\), successive complements give a
disjoint partition into the Round-87, Round-88, Round-89, and hard
packages.  Positive same-group squares used as majorants are not
second incidence owners.

Complete prime-power descent is invertible:

\[
 q^{-2}\sum_{u\bmod q}\mathfrak T_q(u)e_q(-ux)
 =(q/p^j)^{-2}\sum_{u'\bmod q/p^j}
 \mathfrak T_{q/p^j}^{\downarrow}(u')e_{q/p^j}(-u'x).
\]

The \(p^{2j}\) trace factor cancels the quotient-square normalization,
and the restricted Fejer shifts retain their total mass.  Hence local
descent and inverse completion create no power saving.

## Square-root capacity identity

Put

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12},\qquad
 \mathsf T_{82}=J^2/T.
\]

The finite Toeplitz/Fejer inequality and Cauchy over \(b\asymp B\)
give

\[
 \left|\sum_bH_{b,D}(0)\right|^2
 \ll_\varepsilon X^\varepsilon {B\over D}\mathcal E_D.
\]

At full directed degree \(\Delta\asymp B^2\),

\[
 \mathsf C_{\rm deep}={D\over B}\mathsf C_{82}^2,
 \qquad
 \mathsf T_{\rm deep}={D\over B}\mathsf T_{82}^2.
\]

Thus

\[
 \Gamma_{\rm deep}=Gamma_{82}^2,
 \qquad
 \Gamma_{82}=B^3J^{-11/30}.
\]

At \(B=J^{3/20}\), the energy gap \(J^{1/6}\) square-roots exactly
to the Round-82 linear gap \(J^{1/12}\).  These are not two losses in
the same norm.

## Canonical hard core

The first open estimate is the signed hard Gram operator retaining:

- \(D_1<|d|<\Delta_b-J^{3/4}\);
- \(R_*>\rho_*\) and shallow reciprocal conductors;
- residual bad-prime and nonunit cells;
- affine/full-phase, projection-only, and aperiodic factors;
- all classes, signs, nonzero modulus multiples, Ramanujan terms, and
  all four actual stationary weights.

The exact \(q=8\) cell retains full directed degree.  This prevents a
strict capacity gain from further local period peeling, but it is not a
signed lower bound.

## State decision

Promote the scoped Gram-level square-root capacity barrier and freeze
the displayed hard operator as the canonical first-band M1 core.
Retain its signed estimate, the complete first band, upper conductor,
axes, cone edges, other radial sectors, endpoint uniformity, M9-M1,
M9-M2, R5-Full, M9, and the global exponent open.

