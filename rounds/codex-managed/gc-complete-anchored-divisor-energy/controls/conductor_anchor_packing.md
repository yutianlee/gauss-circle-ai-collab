# Round219 conductor: rational-anchor packing and its complete scope

Campaign gc-complete-anchored-divisor-energy. Conductor control, not a
new accepted graph lemma. Starting graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Analytical derivation only; no mathematical experiments or new imports.

## 1. Result

The nearest/inverse-frequency certificate in the216 anchored scalar
estimate admits a better bound than its separate-divisor row count:

    B_inv <= C JN sqrt(J) + C J^2 D sqrt(N) log(2+T sqrt(N))/T.

For actual high rectangles, this is at most any fixed small multiple of
J^2 v^2 D sqrt(N), plus C_epsilon T^(169/3500+epsilon) JN.
The exponent is below208/2625 by13/420. This pays the exact-zero
minus terms and the inverse-frequency part of the scalar certificate.
The positive-frequency-power term remains unestimated with signs; its
available bound still prevents a complete improvement.

## 2. Exact statement and hypotheses

Use the full216 rectangle definitions: T>=2, N<=T^(3/2), D<=N,
K=N/D, d,e in[D,2D), distinct N^(-1/2)-separated R_j in[T/2,2T].
Let u^- = R_j sqrt(d)-R_l sqrt(e), u^+ = R_j sqrt(d)+R_l sqrt(e).
Define v_K(0)=K and v_K(u)=min(K,sqrt(K)/abs(u)) otherwise.
The certificate is B_inv=sum_(j,l,d,e)[v_K(u^-)+v_K(u^+)].
Bounded physical product weights and their total variations can be
inserted at a fixed multiplicative cost, as checked in216. No chi4 or
sigma cancellation is assumed for this certificate. A bound on it is
not an identity splitting the original signed energy into two terms.

For the high-rectangle consequence, take v>=T^(13/125)/(2L),
L<=C(1+log T)^2, and retain the necessary actual high-value condition
D>=c_eta T^(-13/42-2eta) v^2 N^(29/84). Constants may depend on the
fixed mollifier and arbitrarily small positive exponents.

## 3. Proof

For A>=1, let C(A) count ordered(j,l,d,e) with
abs(u^-)<=A/sqrt(K). Write d=a t,e=b t, gcd(a,b)=1,
H<=max(a,b)<2H dyadically. Since d,e have the same dyadic scale,
a,b are comparable and there are at most C D/H admissible t.

The squared identity gives

    abs(d/e-(R_l/R_j)^2)
    = abs(u^-)*(R_j sqrt(d)+R_l sqrt(e))/(R_j^2 e)
    <= C A/(T sqrt(N)).

For fixed j, the centers (R_l/R_j)^2 are separated by
c/(T sqrt(N)). Reduced fractions a/b of height H are separated
by c/H^2 and number at most C H^2 in the fixed ratio range.
Thus the incidence count at height H is bounded both by
C A H^2 (each fraction meets O(A) centers) and by
C J(1+A H^2/(T sqrt(N))) (spacing inside each center interval).
Multiplying by D/H and summing dyadic H<=2D proves, for each j,

    sum_(l,d,e) 1_(abs(u^-)<=A/sqrt(K))
      <= C D sqrt(JA) + C J A D^2/(T sqrt(N)).

Indeed min(AH^2,J+JAH^2/(T sqrt(N))) is at most
min(AH^2,J)+JAH^2/(T sqrt(N)); the two geometric sums are
C sqrt(JA) and C JA D/(T sqrt(N)). The same bound remains
valid if the transition H=sqrt(J/A) is outside the summation range.
Sum over j. Dyadic summation against K/max(1,A), with
A<=C T sqrt(N), gives

    sum v_K(u^-) <= C JN sqrt(J)
                  + C J^2 D sqrt(N) log(2+T sqrt(N))/T.

Since u^+>=cT sqrt(D), direct counting gives the plus contribution
at most C J^2 D sqrt(N)/T. Exact zeros are included in the A=1 bin.
Alternatively exact zeros alone have reduced rational labels and
sum_(l)1/height<=C sqrt(J), giving C JN sqrt(J) directly.

For any fixed delta>0, every nonempty actual high rectangle has
N<=C_delta T^(1+delta). To prove this, use its trivial pair count
abs(H)<=C_M N^(1/4)(1+sqrt(N/T))^(-M). For
N>T^(1+delta), N<=T^(3/2), this is at most
C_M T^(3/8-M delta/2), which is below the required v for
sufficiently large M. Fixed T is absorbed into constants.

Write A0=v^2 D sqrt(N) and use Young's inequality with an arbitrary
small coefficient c>0:

    C JN sqrt(J) <= c A0 J^2 + C_c JN*sqrt(N)/(D v^2).

The high-value restriction implies

    sqrt(N)/(D v^2)
       <= C_eta T^(13/42+2eta) N^(13/84) v^(-4)
       <= C_epsilon T^(13/28-52/125+epsilon)
       = C_epsilon T^(169/3500+epsilon).

Choose eta and delta sufficiently small for any requested epsilon.
The second term of B_inv divided by J^2 v^2 D sqrt(N) is
O(log T/(T v^2)), tending to zero uniformly at the allowed levels.
It can be absorbed with another arbitrary small coefficient. All
small-T cases are covered by enlarging the JN coefficient.

For clarity about the remaining full cost, put kappa=13/55. The
accepted weighted scalar kernel only gives

    abs(K_de(u)) <= T^epsilon min(K,sqrt(K)(abs(u)^kappa+1/abs(u)))

for u nonzero, and K at zero. Since min(K,a+b)<=min(K,a)+min(K,b),
the inverse certificate above is legal. Its other, still unsigned
certificate is bounded by
C T^epsilon J^2 D^2 min(K,sqrt(K)(T sqrt(D))^kappa).
After multiplying by the original Cauchy factor K N^(-3/2), it
costs T^epsilon J^2 min(sqrt(N),T^(13/55) D^(34/55)). The
necessary-condition-compatible scales N~T^(2/3), D~T^(2/15),
v~T^(13/125) have the second branch T^(263/825), smaller than
the cap T^(1/3) but larger than v^2 by T^(457/4125). Thus this
available certificate has no uniform absorption argument. This
scale control does not assert that actual high points occur there.
This is an upper-certificate limitation, not proof that its actual
signed value is large. The full moment stays at the accepted10beta.

## 4. First doubtful or unproved step

The packing proof does not require a missing arithmetic hypothesis.
The remaining gap is a signed estimate of the full oscillatory energy,
including the plus sine terms and nonzero aliases under any further
transform. No bound of that kind follows from rational packing.
The proposed target(12) remains open. This report does not create a
smaller problem and declare the complete target solved.

## 5. Controls and outcomes

Exact common-radical pairs are counted, including j=l,d=e. Reduced
fractions avoid overcounting their gcd multiplicities. Distinct anchors
are essential for the center-spacing bound. Empty and singleton ranges
are included by the +1 in the per-interval count. Character signs,
mollifier signs and actual high-value signs are preserved by the
underlying energy and only discarded for this explicit certificate.
The plus kernel is bounded, not silently dropped. Dyadic bands reach
the full anchored frequency range. No finite numerical test is used.

## 6. Dependencies and exact artifacts

protocol.md; state/proof_obligations.yml at the starting hash;
strategy/round219_complete_anchored_energy_attack.md;
rounds/codex-managed/gc-actual-radical-high-values/reports/anchored_divisor_high_values.md
(equations5--12 and20--22); and
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md.
The packing argument itself is elementary integer-fraction spacing.
The lead was sent to the incidence task for independent line review;
its resulting report must disclose this conductor input.

## 7. Recommended state effect

No change to the graph or proof draft. Retain this sharpened certificate
as evidence only after independent review. It improves a component
cost but supplies no complete moment improvement or new exponent.
