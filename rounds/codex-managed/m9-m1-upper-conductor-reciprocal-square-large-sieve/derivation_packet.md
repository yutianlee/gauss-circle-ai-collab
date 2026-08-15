# Round 72 frozen derivation packet

## 1. Accepted input and scope

Let

\[
 J=X^{1/2},\qquad Q=X^{1/5},\qquad T=J/Q=X^{3/10}.
\]

Round 71 proved that the exact order-\(J\) Farey contribution from
\(c\asymp C\) is target-safe for

\[
 T\leq C\leq J^{2/3}.
\]

Only the upper range

\[
 J^{2/3}<C\leq J                                      \tag{72.1}
\]

is in scope.  The frozen target is the fixed-smooth-interior product
wavelet, not the cone edges or the full \(M9\!-!M1\) theorem.

## 2. Exact odd nonaxial stationary row

For one compatible nonzero stationary dual pair put

\[
 k=\rho\sigma,
 \qquad
 A_b=\left(\sqrt{bX}+\frac{\sqrt{k}}{2\sqrt b}\right)^2,
 \qquad b\asymp B:=C/T.                              \tag{72.2}
\]

On the positive compatible branch \(k>0\).  The other orientation and
the two even local classes must be treated with their exact local units;
they may not be inferred by changing a sign in (72.2).

The accepted odd-modulus interior phase is

\[
 e_{4b}(k\bar c)\,e(-A_b/c).                         \tag{72.3}
\]

Write the complete actual row as

\[
 S_{b,k}(C)=
 \sum_{\substack{c\asymp C\\(c,4b)=1}}
 a_{b,c,k}(X)\,e_{4b}(k\bar c)e(-A_b/c),             \tag{72.4}
\]

where \(a_{b,c,k}\) is not arbitrary.  It contains the inherited Farey
neighbor interval, incomplete-Fresnel entry/exit factor, ratio symbol,
dyadic cutoffs, local character/Gaussian unit, and the exact real-center
orientation.  It has the fixed smoothness supplied by the Round-71
stationary construction, apart from its explicitly retained transition
faces.  The finite compatible \((\rho,\sigma)\) family is summed only
after its local restrictions are imposed.

The smooth odd nonaxial contribution has the outer coefficient

\[
 \frac{T}{\sqrt{CJ}}                                  \tag{72.5}
\]

up to fixed constants and \(X^\varepsilon\) losses.  Therefore a
sufficient first-moment estimate is

\[
 \left|\sum_{b\asymp B}S_{b,k}(C)\right|
 \ll_\varepsilon \frac{J\sqrt C}{T}X^\varepsilon.    \tag{72.6}
\]

## 3. Optimally normalized energy target

Define

\[
 \mathcal E_{C,k}:=
 \sum_{b\asymp B}|S_{b,k}(C)|^2.                    \tag{72.7}
\]

Cauchy's inequality in \(b\), with \(B\asymp C/T\), shows that

\[
 \boxed{\mathcal E_{C,k}\ll_\varepsilon
        \frac{J^2}{T}X^\varepsilon}                 \tag{72.8}
\]

is sufficient for (72.6).  The diagonal in (72.7) has size

\[
 BC\asymp C^2/T\leq J^2/T.                          \tag{72.9}
\]

Thus (72.8) is exactly diagonal-scale at \(C=J\).  The stronger estimate
\(\mathcal E_{C,k}\ll BCX^\varepsilon\), or the uniform row estimate
\(|S_{b,k}(C)|\ll C^{1/2}X^\varepsilon\), would close the whole range,
but neither stronger statement is assumed or required.

Expanding the off-diagonal gives the exact arithmetic kernel

\[
 \sum_{b\asymp B}
 \sum_{c_1,c_2\asymp C}
 a_{b,c_1,k}\overline{a_{b,c_2,k}}
 e_{4b}\!\left(k(\bar c_1-\bar c_2)\right)
 e\!\left(-A_b\left(\frac1{c_1}-\frac1{c_2}\right)\right).     \tag{72.10}
\]

Any proof must estimate (72.10) with the actual symbol before taking
absolute values across the variables in which cancellation is claimed.

## 4. Accepted obstruction and forbidden shortcut

Poisson summation in \(c\) modulo \(4b\), followed by the matching
one-variable \(B\)-process in the resulting index, returns exactly to
(72.3) with the adjoint stationary amplitude.  Repeating that loop is
not progress.  Completion of the short numerator also preserves its
dispersion diagonal.

The proof may instead use a genuinely joint \((b,c)\) energy argument,
a phase-specific spectral theorem whose hypotheses are verified, or a
new reciprocity/dispersion step that does not discard the square-root
chirp.  A theorem for arbitrary coefficients is neither needed nor
plausible; the actual stationary symbol must be used.

## 5. Mandatory seams and controls

The round must audit:

1. the derivation of (72.6)--(72.8), including every factor of \(B,C,J,T\);
2. the diagonal and near-diagonal of (72.10);
3. exact-square and fourth-power controls and derivative resonances;
4. \(b=O(1)\), \(b\asymp B\), transition, and Farey-neighbor regimes;
5. the two even local classes, both surviving axes, and gcd factors;
6. the finite \(k\)-sum and all transition/error tails;
7. whether a cited theorem accepts the real twist, inverse twist,
   level four, moving actual symbol, zero indices, and required power;
8. the distinction between this representation's upper-conductor saving
   and the original wavelet's global \(X^{1/20}\) gap.

## 6. Completion and promotion rule

A successful full result proves (72.8), or the sufficient first-moment
bound (72.6), for every dyadic \(J^{2/3}<C\leq J\), then proves target-safe
bounds for the even and axial pieces with the same exact antecedent.
A scoped result may close a strict subrange or one local class if its
boundary and ownership are explicit.  A no-go result must identify a
strictly smaller survivor than the already accepted one-variable
self-return.

No fixed-interior result alone promotes \(M9\!-!M1\), \(M9\), or the
Gauss-circle exponent.

## 7. Report contract

Every report must have exactly these seven semantic sections: Result;
Exact statement and hypotheses; Proof or derivation; First doubtful or
unproved step; Required control test and outcome; Dependencies and exact
artifacts/sources used; Recommended state effect.  Reports must be valid
UTF-8, contain no control bytes, and must not edit shared state.
