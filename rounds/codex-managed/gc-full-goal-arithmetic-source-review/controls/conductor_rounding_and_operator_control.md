# Round220 exact rounding and the scope of an operator certificate

## 1. Result

Exact rounding of squared radii is compatible with the isolated smooth
multiplier lemma. The complete actual amplitude has a bounded smooth
factor and a row interval. Its cost is logarithmic under an ALL-row-vector
operator norm. This removes a technical import obstacle, not the missing
energy estimate. A uniform complex operator certificate that would be
sufficient is false on admissible separated radii. This control does not
refute the actual real sine energy or assert that these radii are high points.

## 2. Exact statement and hypotheses

Use the closed219 normalizations, for real T>=2, 1<=N<=T^(3/2), D<=N,
K=N/D>=1, A=T sqrt(N)/D, b0=D/(sqrt(T) N^(1/4)), R_j in[T/2,2T].
Write R_j^2=M_j+delta_j, with integral M_j and real |delta_j|<=1/2.
For odd a in a fixed constant enlargement of[A, A] (that is, a~A),
the exact transformed row has weight

    omega_(j,a)(k)=sqrt(T/R_j)(K/k) Psi(2R_j k/(a sqrt(T))) s_(j,a)(k),

where s is the stationary interval mask with the inherited half endpoints.
The physical energy is the square of the sum of these weighted REAL sine
rows, with actual sigma_j chi4(a), summed over k~K. Its sufficient target is

    E <= J^2 v^2 T K/256 + C_eta T^(rho+eta) J A K,
    rho=208/2625, v at least T^(13/125) up to the inherited logarithms.

The stronger illustrative certificate below concerns instead the complex
matrix H((j,a),k)=e(M_j k/a), on ALL vectors in the combined row index:

    Lambda^2 <= C_eta [T^(rho+eta) K + J v^2 T K/A].                 (C)

Constants, logarithms and small absorption constants can be paid if a
sufficiently strong version of (C) were true. We disprove even the displayed
power bound for small fixed eta, not the conditional energy implication.

## 3. Derivation

Since K/A=sqrt(N)/T<=T^(-1/4), the exact residual factor e(delta_j k/a)
has bounded smooth multiplier cost. In scaled t=k/K, the smooth part is

    f_(j,a)(t)=sqrt(T/R_j) t^(-1) Psi(c_(j,a) t),
    c_(j,a)=2R_j K/(a sqrt(T)).

For t in[1/4,3], its first two derivatives are uniformly bounded:
the factors c^r Psi^(r)(ct) are bounded for r<=2 by fixed Schwartz
seminorms, as t is bounded away from zero. No row regularity is needed.
The stationary support is the intersection of the original cofactor and
divisor intervals under d_a=4R_j^2 k/a^2, together with the monotone product
constraint d_a k=4R_j^2 k^2/a^2. Each section is an interval in positive k;
coincident endpoint conventions remain the inherited starred mask.
The isolated lemma therefore transfers an all-row bound with O(log(2+K))
cost, separately for either complex phase sign, retaining the exact phase.
Taking imaginary parts then preserves the actual sine identity.

Literal deletion is different. For each row, |e(delta_j k/a)-1|<=C K/A.
There are O(A) denominator terms, so a crude per-j,k error is O(K).
In E this has norm at most C J K^(3/2), hence squared error C J^2 K^3.
Relative to the energy absorption scale J^2 v^2 T K its cost is
K^2/(T v^2), which need not be small. The corresponding physical H(R)
error after summing k and restoring 4 N^(-3/4) b0 is O(K/sqrt(T)).
These are upper estimates for a proposed deletion, not lower bounds.

For the operator control take N~T, D~T^(1/4), so A~T^(5/4), K~T^(3/4),
and v=T^(13/125). Choose an odd a0~A and distinct integers q_j in
[T^2/a0, (6T/5)^2/a0], with J~T^(1/2). There are asymptotically
T^(3/4) available integers, so this is possible. Set M_j=a0 q_j,
R_j=sqrt(M_j), and delta_j=0. Then T<=R_j<=6T/5, and consecutive
selected radii are separated by at least a0/(3T)~T^(1/4), much more
than N^(-1/2). Every column k is integral, so

    H((j,a0),k)=e(q_j k)=1.

The J by n submatrix (n~K) at a0 is all ones. Testing unit constant
vectors on these rows and columns gives Lambda^2>=Jn~JK. But (C),
divided by JK, would give

    1 <= C_eta [T^(rho+eta-1/2) + v^2 T/A]
       <= C'_eta [T^(rho+eta-1/2) + T^(-21/500)],

which tends to zero for eta<1/2-rho. Thus (C) is false uniformly on
this enlarged class, even allowing any fixed logarithmic loss. The same
selected rows of the REAL sine matrix are exactly zero. The actual row
vector includes every a with the prescribed character, while the test
vector is supported only at a0. No actual high-value assertion is made.

## 4. First unproved step

The needed complete real energy estimate remains unproved. Smooth phase
retention and interval masking do not establish the requisite arithmetic
operator norm. A theorem for separate j and a coefficient factors cannot
be enlarged to all combined rows for free. Conversely, failure of (C)
does not exclude an estimate retaining actual sigma_j chi4(a), paired
sine signs, moving weights and the high-point definition.

## 5. Controls and outcomes

- Exact rounding and scaled derivatives: retained, with constant smooth
  cost and a logarithmic interval cost under the stated operator norm.
- Deletion error: explicitly priced; it is not certified negligible.
- Complex aligned submatrix: refutes only (C); the corresponding sine
  rows vanish, which verifies the essential scope distinction.
- Necessary scalar high-point restrictions do not rule out the chosen
  scales: D >= T^(-13/42) v^2 N^(29/84) has right exponent
  13/125*2+1/28 <1/4. The scalar ceiling at N=T permits v of exponent
  13/125<3/28. These are compatibility checks, not existence of highs.
- All computations here are exact algebraic power bookkeeping; zero
  numerical experiments and no assertion of an asymptotic target proof.

## 6. Dependencies and provenance

Conductor, round220, graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Closed219 reports/joint_cofactor_dispersion.md and its independent review;
closed216 reports/anchored_divisor_high_values.md; current isolated packet
briefs/blind_smooth_mask_statement.md and report reports/blind_smooth_mask.md
(SHA256 e27659b89c33da6c8216f5817351edfa1a3fd269ffaeb8d8c1e51e6ce180e33b).
The isolated role had no application context. The complex control was
sent separately to the reciprocal-source role for an independent check;
final-hash review remains required. No source theorem is imported here.

## 7. Recommended state effect

Retain as reviewed application and strategy evidence, with no graph
promotion or complete-bound credit. Abandon the displayed uniform
complex certificate; keep the actual real signed energy and the full
quarter objective open. The multiplier lemma is elementary infrastructure
whose useful scope is explicit; it does not warrant a target status change.
