# Round228 conductor complete-frontier review

## 1. Result

GREEN for the complete continuous-component estimate, exact primitive
cuspidal transformation, scalar gamma controls and scoped full-cost
assessment. The entire continuous contribution meets the sufficient raw
target. The entire signed cusp contribution does not yet have that bound.
No complete wave, moment, accepted exponent or quarter theorem improves.
The conductor is not the sole reviewer of its own gamma application.

## 2. Exact statement and hypotheses

Campaign gc-signed-heegner-phase, Round228, conductor review, 2026-09-28.
Starting graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Retain T>=2, every R in [cT,CT], dyadic2<=N<=P<2T^(3/2), actual r2,
fixed real signed Schwartz Psi, A=(1+N/T)^(-J), exact smooth g_N, every
h<2N and alpha_h=1-h/(2N). Write D for the entire cusp term and E for
the entire continuous term, in hyperbolic area and dt/(4pi) normalization.
This notation avoids the reports' differing letters for these components.
The exact reviewed identity is D+E=sum_h alpha_h(C_h-rho_h I_h).
The sufficient full raw target is 2Re(D+E)<=C A^2N^(3/2)T^epsilon.
All estimates here retain their declared closed227 bridge and scalar
kernel premises; those reviewed artifacts are not silently promoted.

## 3. Independent derivation and complete restoration

At i, summing all lattice vectors and removing their gcd gives
E^(1)(i,s)=2F(s)/zeta(2s), F=zeta(s)L(s,chi4). Splitting primitive
rows of E(2z,s) by parity of d gives
E_infinity^(2)=(2^s E(2z,s)-E(z,s))/(2^(2s)-1).
Applying W2 gives E_0^(2)=(2^s E(z,s)-E(2z,s))/(2^(2s)-1).
Both z2=(-1+i)/2 and 2z2 are level-one images of i. Each level-two
value is therefore E^(1)(i,s)/(1+2^s). On Re(s)=1/2 that denominator
has modulus at least sqrt(2)-1. The two equal values remain two cusp
channels: B2=2B1/|1+2^s|^2, where B1=4|F(s)/zeta(2s)|^2.
Residues at1 are3/pi and1/pi respectively, checking the area convention.

The theta-square Mellin integral gives exactly
pi^(-s)Gamma(s)F(s)=(1/4)[1/(s-1)-1/s+
integral_1^infinity(theta(y)^2-1)(y^(s-1)+y^(-s))dy].
It is symmetric under s->1-s, with residues +1/4,-1/4 at1,0.
Shifting the completed Gaussian-smoothed integral crosses the test pole
at0 and the two completed-function poles. The latter contributions are
G(1-s)/(4(1-s)) and G(s)/(4s), with both signs positive before solving
for F. Thus the two AFE sums have the minus polar correction printed in
the report. It is rapidly small on the critical line; it was not dropped
from the exact identity. The dual scalar has modulus1.

For t~U and w=b+iv, b>0 fixed, the uniform gamma modulus estimate gives
|Gamma(1/2+it+b+iv)/Gamma(1/2+it)|
<=C_b U^b(1+|v|)^b exp(pi|v|/2), including t+v near0.
The Gaussian in v is integrable against this bound. After truncating
the two AFE series at L=ceil(U^(1+delta)), their tails are bounded by
U^B L^(1/2+eta-B) and become arbitrarily small for fixed large B.
Direct integration of a fixed Dirichlet polynomial gives mean square
at most (U+L log(2L))sum|b_n|^2 uniformly in the translated t interval.
Separate the moving weight by its Mellin integral, bound its gamma
multiplier first, and apply Minkowski. This proves the claimed mean
U^(1+epsilon) after choosing fixed delta,b,eta sufficiently small.
The moving coefficients have not been placed for free into a fixed
polynomial estimate. Both AFE sums, both tails and both poles are paid.

Leong2405.04869v5 Corollary4's final assertion gives
|1/zeta(1+iv)|<=29.388 log(v) for v>=2, unconditionally. Here v=2|t|;
negative heights use conjugation. Root checked the exact-version official
HTML, Section2.3, and the nonauthor review independently checked the same
assertion. No off-line region or RH is imported. The elementary
3+4cos(x)+cos(2x)>=0 Euler-product argument excludes other zeros on Re1;
at t=0 the inverse zeta factor vanishes. Compact t causes no singularity.
Therefore integral_(U<=|t|<=2U)Bq(t)dt<=C U^(1+epsilon) for both levels.

Set Lambda_h=Rh/sqrt(N). Exact radial coordinates x=h sinh^2(r/2)
give phase2pi R sqrt(h)exp(-r/2), with stationary curvature t/2 and
height t~Lambda_h. The reviewed uniform stationary bound is
|H_h|<=C A^2 sqrt(N/h)/Lambda_h. Each exact Hecke polynomial has
absolute size at most h^(1/2+eta): its descendant square-root masses
form a bounded geometric sum. Consequently one entire stationary
shift costs A^2 sqrt(N) h^eta Lambda_h^eta. All h<2N cost
A^2 N^(3/2)T^epsilon. No shift-density assumption enters this sum.
The low and high dyadic tails cost, per shift,
A^2 sqrt(N)h^eta Lambda_h^(1/2+eta-K), with the compact part bounded
by A^2 sqrt(N)h^eta log(2N)Lambda_h^(-K). Because
Lambda_h>=c T^(1/4), fixed large K pays every summed tail. Smooth zero
extension removes endpoint terms. All three cusps and both spectral
signs are included. This proves the complete continuous modulus bound.

The exact cusp simplification is also consistent. Reflection fixes both
points modulo translation, so odd modes vanish. W2 fixes z2 modulo
translation, so Fricke-minus modes vanish. For a level-one form the
level-two oldspace Gram matrix has diagonals3 and off-diagonal
sqrt(2)lambda(2), from tracing u(2z). Both oldspace point values equal
u(i). The surviving plus vector therefore contributes
2|u(i)|^2/(3+sqrt(2)lambda(2)); the minus vector vanishes.
The fixed prime bound 2^theta+2^(-theta)<3/sqrt(2), theta<1/2, bounds
the reciprocal denominator uniformly. It is not replaced by1.
For primitive level2, zero trace gives lambda(2)=-w/sqrt(2).
The surviving even Fricke-plus forms have root+ and primitive conductor
1 or2, as derived by the Fourier Mellin integral. Odd depletion is the
exact test combination F(m)-lambda(2)F(2m)+1_(q=1)F(4m).
All local lengths, phases and square-root factors remain in that test.

For S=sum lambda(m)m^(it)a(m/L), the exact resonant transform is the
negative-contour integral in attack(12), with the full gamma ratio(13).
The original entire L-function is shifted before the dual expansion,
so no separate spurious gamma residue is inserted in that step.
Near v=0 its large pair contributes
t^(1/2-s)exp(i[2t(log t-1)-pi/4]); the other gamma pair stays exact.
Its Mellin cosine identity supplies the leading coefficient
2sqrt(pi)L/sqrt(qt) and dual scale K=qt/(pi^2 L), with rapid tails.
Combining the original phase yields exp(-i pi/4)(qdR^2/n)^(it).
This remains a genuinely oscillatory discrete spectral pairing.

Here is a uniform check of the coefficient envelope at small as well as
large n, independent of any truncated asymptotic remainder. Put
x=pi^2Ln/q. For even parity shift the individual transform to Re(s)=2.
It crosses s=1 and s=1+2it. Both gamma residues have modulus O(t^(-1/2));
the second has the rapidly decaying factor a-hat(1+2it). Thus their
contributions are O(x/sqrt(t)). On the new line the integral is
O(x^2 t^(-3/2)), by the full-axis gamma bound and Mellin decay, hence
O(x/sqrt(t)) when x<=t. For x>=t use the original negative line,
giving O(t^(1/2+B)x^(-B)). After multiplication by the exact n^(-1)
prefactor these combine into O_B(L/sqrt(t)(1+n/K)^(-B)), renaming B.
This justifies attack(21) without extrapolating large-n decay to zero.
The actual stationary amplitude has uniformly bounded scaled h
derivatives after removal of its phase; the nonauthor review explicitly
checks that parameter assertion and the fixed-order remainders.

For h~M, t~U=TM/sqrt(N), descendant d and length L=M/d, the amplitude
is c<=C A^2 sqrt(N)/(U sqrt(d)). Minkowski and the individual Hecke
second moment give transformed vector norm at most c U^(3/2)T^epsilon.
The point fourth moment adds U, giving c U^(5/2), or
A^2 sqrt(N)U^(3/2)/sqrt(d). Summing d and M gives
A^2T^(3/2)N^(5/4)T^epsilon. These moments retain the separately stated
AH premises already fenced in227; no defective collective sieve is used.
The cost exceeds the original arithmetic A^2N^2 cap on the entire
frozen range, and at N=T exceeds the sufficient target by T^(5/4).
This is a failure of that positive estimate, not an actual lower bound.

Now that E is target-sized, the exact complex identity and the original
arithmetic cap imply |D|<=C A^2N^(2+epsilon) for the sum of BOTH cusp
levels. This does not grant the same cap separately for each level or
band. Dividing the Fejer squared-wave inequality by N^(3/2) makes E
target-sized but leaves A^2N^(1/2) from this cusp cap. Diagonal, density,
bounded Fejer multiplier, singleton, all dyadic scales and the original
infinite Schwartz tail restore only complex exponent1/4 and physical3/8.
That is weaker than inherited benchmarks. The complete real beta is
never assigned to a complex wave or block. A full target-sized D would
instead give complex T^epsilon and physical quarter, but is unproved.
The complete pretrace inverse returns the original Fejer pair-count
quadratic; it supplies no independent cancellation estimate.

## 4. First doubtful or unproved step

The remaining complete one-sided inequality is
2Re D<=C_epsilon,J A^2N^(3/2)T^epsilon, for all frozen N,T,R and all
shifts, descendants, primitive modes, oldspace factors and spectral tails.
Since E is now bounded in modulus at that size, this is equivalent to
the full sufficient target up to a target-sized error. The phase
(qdR^2/n)^(it) cannot be integrated by parts over discrete eigenvalues
without a new valid signed estimate. The short dual scale or scalar
unit modulus does not provide it. No all-method no-go is asserted.

## 5. Controls and outcomes

Reciprocal nonauthor reviews are bound to the repaired final report hashes.
The blind initial gamma report used only protocol and its statement packet.
Its later review of the conductor application discloses retained history
and is not statement-only. The application is conditional where actual
functional equations, contours or coefficient bounds are not established
inside that scalar control; the attack and its separate review own those
seams. Exact small gamma, both transitions, full-axis modulus, derivatives
and the failure of a quadratic-only large-window approximation are checked.
Standalone carriage returns in two reports were repaired as formatting
only, with explicit provenance. Zero mathematical experiments; at least
95 percent analytical/algebraic work. All complete M1 HARD/SMOOTH,
M2 TOP/BAL/UNBAL, GAR lower ownership through159 and endpoint obligations
remain. Both accepted distribution terms remain. Fixed twelfth29/25
would give102/325, not quarter; the adequate unbounded sequence of fixed
even moments is still unproved. No hidden complementary sector is closed.

## 6. Dependencies and exact bindings

- rounds/codex-managed/gc-signed-heegner-phase/reports/signed_hecke_functional_attack.md: f0d2507ef603e8ce1dac149994e52feb660ec9ccf27cf070a1ee83079b6d55dd.
- rounds/codex-managed/gc-signed-heegner-phase/reports/complete_eisenstein_pairing.md: cf92b16e42ad85d900a532a66f1df33cb8aa2be175c7f0f4d8013501a4112d1f.
- rounds/codex-managed/gc-signed-heegner-phase/reports/blind_gamma_transition.md: 9dcfb60996d011bccde60112c1f8577440b6bf4cc330b808c4e5cc5d2ae4ac4f.
- rounds/codex-managed/gc-signed-heegner-phase/controls/conductor_gamma_application.md: f90c8dbbd21e4c881259d7026a16ddeb0a635525f741d89eeb715f3ad7659515.
- rounds/codex-managed/gc-signed-heegner-phase/briefs/blind_gamma_transition_statement.md: b801dea99d5db4243f728c7b16b690d237a0a0f758f8d83eb63bebdedad82039.
- rounds/codex-managed/gc-signed-heegner-phase/reviews/conductor_gamma_transition_review.md: 0d1a0b43b025db480c2941865afd896480c2c5af6f99a7fffb1c1a79cac1b57b.
- rounds/codex-managed/gc-signed-heegner-phase/reviews/independent_signed_hecke_review.md: 2cc4fa02cf7c76bdb6ef2fede88f7512da6331acf31878f452974e63678ca287.
- rounds/codex-managed/gc-signed-heegner-phase/reviews/independent_eisenstein_review.md: 2197f126051957c3671060c5c83ed076b5939c53bef2036df76d9c90e2c7c5bc.
- rounds/codex-managed/gc-signed-heegner-phase/reviews/independent_gamma_application_review.md: fa22a5d94f2eacd939ff7e4de99d5ab251578f87de52b1afaa4c19a3a0f8bed5.

Other exact context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round228_signed_heegner_phase.md;
- strategy/gauss_circle_strategy_review_2026-09-23.md;
- strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md;
- rounds/codex-managed/gc-signed-heegner-phase/briefs/complete_signed_heegner_interface.md;
- rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/complete_joint_spectral_interface.md;
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/heegner_joint_norm_audit.md;
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/independent_heegner_norm_review.md;
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/joint_shift_spectral_attack.md;
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/independent_spectral_attack_review.md;
- rounds/codex-managed/gc-complete-joint-spectral-remainder/synthesis.md;
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md.

Leong primary URL:
https://arxiv.org/html/2405.04869v5#S2.SS3.
Its precise theorem card, hypothesis specialization and limited source
audit are in the continuous report and its independent review. AH2607.13518v1
Theorem1.2 and equation(8) remain stated external premises only for the
failed cusp certificate, not inputs to the new continuous mean square.
No claim of independently checking either source's entire proof is made.

## 7. Recommended state effect

Identity State Patch. Retain the complete continuous lemma and the exact
cuspidal transformation as reviewed evidence. Their whole-functional and
scalar inherited interfaces are themselves reviewed archive evidence;
this round does not package a dependency-closed graph promotion. Thus
all401 nodes and proof-draft bytes stay unchanged, and no accepted full
estimate changes. Close228 after mechanical validation. Round229 is the
mandatory broad strategy/current-primary review, pending design; no
successor is launched here. It must assess this paid component and the
unresolved complete cusp estimate against every alternative full frontier.
