# Round228 conductor review of the isolated gamma derivation

## 1. Result

GREEN for the exact isolated report and its explicitly scalar claims.
The two transition centers, modulus envelope, phase constants, remainder
symbols and quadratic-window falsification are correct. No arithmetic
bound, spectral cancellation or full-goal gain follows from these facts.

## 2. Exact statement and hypotheses

Target: reports/blind_gamma_transition.md, SHA256
9dcfb60996d011bccde60112c1f8577440b6bf4cc330b808c4e5cc5d2ae4ac4f.
Statement packet: briefs/blind_gamma_transition_statement.md, SHA256
b801dea99d5db4243f728c7b16b690d237a0a0f758f8d83eb63bebdedad82039.
Retain eta<=sigma<=1-eta, delta0or1, t>=2, v real, R>0 and the
positive-real logarithm convention. The analytic log-Gamma branch is
fixed on the right half-plane. All constants may depend on eta and
fixed differentiation orders. The claims are not for arbitrary complex
v, varying eta or an external coefficient family.

## 3. Independent derivation and line checks

Substitution into all four gamma arguments gives two pairs with imaginary
magnitudes |v|/2 and |2t-v|/2. Their real parts are positive and bounded
away from zero. This proves the exact factorization and locates exactly
the two regular transition centers. Stirling away from zero and compactness
near zero give a two-sided envelope for each pair with exponent
k=1/2-sigma. The exponential size factors cancel pairwise. At sigma1/2
the numerator and denominator are conjugates, giving exact modulus1.

For the positive large parameter T=t-v/2, subtraction of the two
log-Gamma expansions gives k log T and phase
2T(log T-1)+pi(a+b-1)/2. Since a+b=delta+1/2, the constant is
c_delta=delta pi/2-pi/4. The first log-remainder coefficient is
-i[B2(a)+B2(b)]/(2T), and the second is
[B3(a)-B3(b)]/(6T^2). The signs follow from (iT)^(-1)=-i/T and
(-iT)^(-1)=i/T, with the denominator subtracted. Thus odd inverse
powers have imaginary coefficients and even inverse powers real ones.

An independent polynomial check uses u=sigma-1/2 and
m=delta/2+1/4, so a=m-u/2 and b=m+u/2. For both m=1/4 and3/4,
B2(m)=-1/48 and B3'(m)=-1/16. Therefore
[B2(a)+B2(b)]/2=u^2/4-1/48 and
[B3(a)-B3(b)]/6=u/96-u^3/24
=u sigma(1-sigma)/24. These verify the report's d,h, their lack
of delta dependence, and h=0 on the critical line. Sectorial analytic
Stirling remainders have the stated differentiated symbol bounds by
Cauchy's estimates within a fixed larger sector; no pole is approached.

Writing T=t-v/2 exactly gives
2T(log T-1)=2t(log t-1)-v log t+Psi_t(v).
The prefactor pi and E_R then leave precisely R^(2it),
(pi^2/t)^(iv) and c_delta. Direct differentiation gives
Psi'=-log(1-v/(2t)) and Psi^(j)=(j-2)!/(2t-v)^(j-1) for j>=2.
The quadratic and cubic Taylor coefficients are1/(4t) and1/(24t^2).
The stated derivative bounds follow by the convergent series on
|v|<=2t/3. This common window also covers t^(1/3) for t>=2, including
the small bounded range where t^(1/3)>t/2. Retaining T^k avoids the
larger O(|v|/t) amplitude error from replacing it by t^k.

At v=0 the small gamma quotient is the positive real Gamma(a)/Gamma(b),
so the direct phase and size controls agree with the expansion. At the
critical line d=-1/48, hence the first phase correction is+1/(48t),
consistent with exact unit modulus. At v=t the gamma factors occur in
conjugate pairs, so q_sigma(t) is positive; at sigma1/2 it is exactly1.

Conjugation and the meromorphic identity Q(s)Q(1-s)=1 give the report's
reflected-v formulas. The extra E_R^2 in the reflected identities for
p=E_R q is necessary and correctly present. The second-center expression
is the conjugate large-pair expansion with the small factor G(u) retained,
so its phase signs and all symbol bounds are consistent.

Finally at v=t/2 the cubic-and-higher phase remainder is C t with C>0,
as follows from a convergent positive series. Along the report's real
sequence t_n=(2n+1)pi/C the normalized quadratic-only approximation
has ratio tending to-1. Thus its error fails to tend to zero. The exact
elementary phase formulation resolves this failure without claiming a
global quadratic asymptotic. This is an analytic control, not a numerical
experiment or a lower bound for an arithmetic sum.

## 4. First doubtful or unproved step

No unresolved gap was found in the stated scalar results. The first
invalid extensions are large-argument Stirling through either transition,
quadratic-only uniformity on the half window, or an external cancellation
claim based only on the factorization. None is asserted. The report
contains no application to the actual Hecke coefficient or a dual sum.

## 5. Required controls and outcomes

Exact argument matching, phase constants and correction signs: PASS.
Both delta values and compact sigma range: PASS by the polynomial checks.
Critical-line unit modulus, meromorphic inversion and conjugation: PASS.
Both transitions and v=t positive-real check: PASS. v=0 direct control:
PASS. Derivative symbols and small bounded-t windows: PASS. Large-window
quadratic falsification: PASS. External-sum scope: PASS, no inference
of smallness or lower bound. All work was algebraic or analytical; zero
mathematical experiments.

## 6. Dependencies and provenance

Conductor is not the report author. The initial role was fresh fork_none
and read only protocol.md and its isolated packet, as disclosed in the
report. The conductor independently derived the factorization, phase,
global envelope and conditional application before reading the report;
the report's extra Bernoulli corrections were independently checked here.
A progress message about the centers and cubic order was received after
that root derivation. The root control later enlarged its stated window
to2t/3 to make the bounded-t overlap explicit; this does not affect the
isolation of the original report. This review does not certify the root's
own application, which has a separate nonauthor review.
Protocol SHA256: f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
All paths in Sections1--2 are relative to the current campaign directory.
No new external source theorem was used in this review.

## 7. Recommended state effect

Retain the isolated result as GREEN reviewed scalar evidence. No change
to graph, draft, moments, complete-wave bounds or pointwise exponents
follows from it. The full signed spectral target remains separately open.
