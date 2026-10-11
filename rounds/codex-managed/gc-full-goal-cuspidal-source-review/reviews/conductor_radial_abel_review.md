# Round229 conductor review of the isolated radial Abel report

## 1. Result

GREEN for the stated scalar lemmas only. The independent report proves
the full mass, signed integral, differentiated front profile and
compact-spectral obstruction. It supplies no arithmetic estimate.
Conductor, NONBLIND reviewer, 2026-09-29. The conductor's separate
derivation had been frozen before receiving the blind calculation.

## 2. Exact statement and reviewed hypotheses

Reviewed report SHA256:
80b45100f6fb4c3443ac6c514248c2e90448694df668f527d7bc1d7e82792f6f.
Isolated statement SHA256:
2537c3e890373c101d509fe94c602097b2f7fcfe0d4dbf9d36fb2b57841e7ffa.
Both paths are in this campaign: reports/blind_radial_abel_kernel.md and
briefs/blind_radial_abel_statement.md. G is fixed, nonnegative, even,
smooth, supported inside (-1,1), and has integral one; U,L>=2 are
independent. The report uses exactly the packet's Fourier and Abel
normalizations. Its compact-spectral conclusion assumes an even nonzero
smooth compactly supported spectral input; it is not asserted for every
possible smoothing or trace regularization.

## 3. Independent verification

The two time bumps have Fourier transform 2cos(Lt)H(t/U). The negative
bump never enters the half-line Abel integral. Below the positive bump,
integration by parts gives the strictly negative kernel with factor
-1/(2pi sqrt(2)); at r=0 its displayed value follows from
coshs-1=2sinh(s/2)^2. This checks both normalization and the full interior.

For r=L+a/U the exact quotient of cosh differences is
(sinh L)w Q(a,w)/U. Q=1+O(1/U), and all fixed a derivatives admit
uniform bounds on compact intervals when the radius is nonnegative.
The fixed-endpoint w integral has the integrable weight w^(-1/2).
The report's differentiation, domain threshold and stronger all-U
assertion for a in [-b,b] are justified.

Write F(a)=integral G(a+w)w^(-1/2)dw. Its derivative yields the report's
Phi, including the negative constant. For a<-b, integration by parts
gives the negative |a|^(-3/2) tail. Since F tends to zero at both ends,
integral Phi=0. Thus nonvanishing does not rely on Phi(0) or a generic
choice of G. Its positive part is confined to [-b,b].

The report integrates the whole negative interior exactly. The
subtraction (coshs-1)^(-1/2) at the lower endpoint is retained.
The front has pointwise size U^(3/2)/sqrt(sinh L) and weighted width
sinh L/U. For a in [-2,-1] the sign-definite kernel supplies the
matching lower bound for every U,L>=2, including bounded U. These
arguments prove M comparable to sqrt(U sinh L).

Reversing the signed integral gives the inner value
2sqrt(coshs-1), hence J=2cosh(L/2)H(i/(2U)). The sharper formula uses
the exact identity M=2P_positive-J, not a local approximation to an
unbounded interval. On [-b,b], the positive-part map is 1-Lipschitz,
so its front error is O(U^(-1/2)sqrt(sinh L)). The factor
2pi sqrt(U sinh L) norm(Phi)_1 and the negative J correction are correct.

For a compact-spectral even input, composing the two Abel kernels
produces the beta integral pi and the stated inverse factor sqrt(2).
The absolute composition is justified by integral |f'|<infinity.
If the hyperbolic radial L1 norm were finite, the uniformly bounded
inner exponential integral would force exponential time integrability
for every strip width below 1/2. Fourier inversion and holomorphic
uniqueness contradict nonzero compact real spectral support. The
argument proves divergence, rather than merely observing that a
particular upper estimate is insufficient.

## 4. First doubtful or unproved step

None remains in these scalar statements. Any identification with the
complete actual complex spectral multiplier, discrete fixed-CM orbit
measure or arithmetic cancellation remains outside this report.
The conductor's conditional application has a distinct nonauthor reviewer.

## 5. Controls and outcomes

Signs and Fourier constants passed; zero radius and complete negative
interior passed; unrestricted parameter ratios and U=L=2 passed;
differentiation and support-edge flatness passed; absolute versus
signed mass passed; compact-time versus compact-spectral distinction
passed. No experiment or numerical check was used. A scalar absolute
mass lower bound is not a lower bound for the actual arithmetic sum.

## 6. Dependencies and provenance

Read the complete frozen report and isolated statement, with protocol.md
as reporting authority. The report discloses that its initial context
contained only these two authorized inputs and no graph, source or
arithmetic application. The conductor separately had the full context;
this review does not claim the conductor was blind. The new post-freeze
assignment to the blind author is a review of the conductor's different
artifact, not self-review or retroactive alteration of initial isolation.

## 7. Recommended state effect

Retain reviewed scalar evidence. No promotion to the accepted claim
graph, no complete-wave or moment bound, and no exponent change.
All mathematical full-goal owners remain open.
