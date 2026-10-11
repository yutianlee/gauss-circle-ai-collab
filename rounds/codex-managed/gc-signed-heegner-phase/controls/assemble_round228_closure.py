"""Assemble final reviewed round228 evidence; no shared-state writes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

base = Path('rounds/codex-managed/gc-signed-heegner-phase')
assert not (base / 'controls/artifact_hashes.json').exists()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, s): Path(p).write_text(s, encoding='utf-8', newline='\n')
def put(p, obj): write(p, json.dumps(obj, indent=2, ensure_ascii=False) + '\n')
now = datetime.now(timezone.utc).isoformat()
attack = base / 'reports/signed_hecke_functional_attack.md'
continuous = base / 'reports/complete_eisenstein_pairing.md'
blind = base / 'reports/blind_gamma_transition.md'
control = base / 'controls/conductor_gamma_application.md'
packet = base / 'briefs/blind_gamma_transition_statement.md'
frozen = {
    attack: 'f0d2507ef603e8ce1dac149994e52feb660ec9ccf27cf070a1ee83079b6d55dd',
    continuous: 'cf92b16e42ad85d900a532a66f1df33cb8aa2be175c7f0f4d8013501a4112d1f',
    blind: '9dcfb60996d011bccde60112c1f8577440b6bf4cc330b808c4e5cc5d2ae4ac4f',
    control: 'f90c8dbbd21e4c881259d7026a16ddeb0a635525f741d89eeb715f3ad7659515',
    packet: 'b801dea99d5db4243f728c7b16b690d237a0a0f758f8d83eb63bebdedad82039',
}
for p, h in frozen.items(): assert sha(p) == h, (p, sha(p))
spec = [
    ('conductor_gamma_transition_review', '/root', '/root/blind_gamma_transition', [blind, packet], 'nonauthor_review_of_isolated_scalar_derivation'),
    ('independent_signed_hecke_review', '/root/complete_eisenstein_pairing', '/root/signed_hecke_functional_attack', [attack], 'post_freeze_nonauthor_transform_and_full_cost_review'),
    ('independent_eisenstein_review', '/root/signed_hecke_functional_attack', '/root/complete_eisenstein_pairing', [continuous], 'post_freeze_nonauthor_complete_component_review'),
    ('independent_gamma_application_review', '/root/blind_gamma_transition', '/root', [control], 'post_isolation_nonauthor_conditional_application_review'),
]
review_paths = []
review_frozen = {
    'independent_signed_hecke_review': '2cc4fa02cf7c76bdb6ef2fede88f7512da6331acf31878f452974e63678ca287',
    'independent_eisenstein_review': '2197f126051957c3671060c5c83ed076b5939c53bef2036df76d9c90e2c7c5bc',
    'independent_gamma_application_review': 'fa22a5d94f2eacd939ff7e4de99d5ab251578f87de52b1afaa4c19a3a0f8bed5',
}
for name, reviewer, claimant, arts, mode in spec:
    p = base / 'reviews' / (name + '.md')
    if name in review_frozen: assert sha(p) == review_frozen[name], p
    s = p.read_text(encoding='utf-8')
    assert all(re.search(rf'^#{{1,2}} {i}\.', s, re.M) for i in range(1, 8)), p
    assert 'GREEN' in s and all(sha(a) in s.lower() for a in arts), p
    review_paths.append(p)
bindings = '\n'.join(f'- {p.as_posix()}: {sha(p)}.' for p in list(frozen) + review_paths)
owner = base / 'reviews/conductor_complete_frontier_review.md'
write(owner, r'''# Round228 conductor complete-frontier review

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

''' + bindings + r'''

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
''')

write(base / 'synthesis.md', r'''# Round228 synthesis: signed Heegner phase and continuous spectrum

## 1. Result

The ENTIRE continuous spectral component meets the sufficient raw bound
A_J(N)^2N^(3/2)T^epsilon. This is reviewed component evidence, with one
remaining ENTIRE cusp owner. The complete wave and quarter theorem remain
unproved; no accepted exponent or moment bound improves.

The resonant Hecke functional equation shortens its dual coefficient
scale to qt/(pi^2L), but leaves a signed spectral phase. The fully restored
positive estimate obtained here is weaker than the original coefficient
cap. A shorter transform or formal pretrace inversion gives no saving.

## 2. Exact statement and hypotheses

Use frozen228 actual r2, signed fixed Schwartz Psi and g_N, every real
R~T, every dyadic2<=N<=P<2T^(3/2), and every h<2N. Write D for the entire
cuspidal component and E for the entire continuous component, so that
D+E=sum_h(1-h/(2N))(C_h-rho_h I_h). This convention reconciles the
two reports' differing component letters. The sufficient full target is
2Re(D+E)<=C A^2N^(3/2)T^epsilon; the new result bounds |E| at that size.
It is conditional only on the explicitly inherited reviewed exact bridge
and scalar-transform interface plus the precisely audited source theorem.

## 3. Derivation and conductor decision

At the actual CM points, the one level-one Eisenstein value is
2zeta(s)L(s,chi4)/zeta(2s), while each of the two level-two values is
that value divided by1+2^s. The local denominator is uniformly separated
from zero on Re(s)=1/2. A theta-derived functional equation and a
Gaussian-smoothed AFE prove the necessary degree-two mean square
O(U^(1+epsilon)). Both polar terms, both series tails, moving weights
and gamma transitions are paid. Leong v5 Corollary4 provides the matched
reciprocal-zeta bound at2|t|>=2; compact heights are handled separately.
The resulting continuous spectral mass is O(U^(1+epsilon)). The exact
stationary kernel and bounded two-adic descendant mass then cost
A^2sqrt(N) per shift, up to small powers. All shifts, both signs, all
three cusps and every tail give the displayed complete component bound.

At the cusp points only even reflection and level-two Fricke-plus modes
survive. The level-one oldspace has weight2/(3+sqrt(2)lambda(2)); it is
not omitted. Primitive conductors remain1 and2, both surviving root
numbers are+. Exact Euler-two depletion handles the odd-index restriction.
For h=dm and L=M/d, the resonant functional equation leaves the small
gamma factor as a cosine transform and produces dual scale qt/(pi^2L).
The large gamma phase combines with the original phase to leave
exp(-i pi/4)(qdR^2/n)^(it), with each descendant's own length and every
local factor retained. Negative-contour decay and the two explicit poles
on a positive contour prove the dual envelope at both large and small n.

With t~U=TM/sqrt(N), the amplitude is A^2sqrt(N)/(U sqrt(d)). The
individual Hecke second moment and point fourth moment give raw full
cusp certificate A^2T^(3/2)N^(5/4)T^epsilon. This still exceeds A^2N^2
through the frozen range. The now paid E lets the original complex
arithmetic identity cap the complete sum of both cusp levels at A^2N^2;
that bound is not assigned separately to each level or band.
At N=T the cap still misses the quarter target by T^(1/2).

The isolated gamma derivation and independently reviewed root application
agree on both transitions, exact small gamma, normalized error derivatives,
phase constants and full-axis modulus. A quadratic-only phase is valid
with small error on the smaller window, not on the entire half window.
The root application stays conditional on actual arithmetic inputs.
The attack and its separate review establish those inputs within scope.

After the complete Fejer restoration the continuous component costs
A^2T^epsilon, but the cusp cap costs A^2N^(1/2+epsilon) in the squared
wave. Singleton, every scale and the original infinite Schwartz tail
restore only complex1/4 and physical3/8, weaker than inherited bounds.
The inherited real beta is not a complex or blockwise estimate.

## 4. First doubtful or unproved step

Prove the complete one-sided cusp inequality
2Re D<=C_epsilon,J A_J(N)^2N^(3/2)T^epsilon, uniformly in all frozen
variables and retaining the exact H_h, two-adic polynomials, both levels,
old/new normalization, every mode and tail. The continuous modulus bound
makes this equivalent to the sufficient full target up to its allowed
error. No discrete spectral cancellation at this scale has been proved.
Pretrace inversion reconstructs the original Fejer quadratic; neither
that identity nor the short dual length estimates it.

## 5. Controls and outcomes

All three reports and the root scalar application have final-hash
nonauthor reviews; the conductor adds a complete-frontier audit.
The initial gamma task was statement-only; subsequent application review
discloses its history. Formatting-only repairs are recorded and rebound.
The continuous proof does not use AH's cusp fourth moment. Its separately
stated moment premises are confined to the failed cusp certificate;
printed collective-sieve defects remain fenced. Upper-cost losses are
not arithmetic lower bounds or a universal spectral impossibility.
Zero mathematical experiments; at least95 percent analytical/algebraic.
All M1/M2/GAR/endpoints, both distribution terms and the sufficient
unbounded fixed even-moment family stay open. Fixed twelfth is not quarter.

## 6. Dependencies and provenance

Frozen228 strategy and complete interface; closed227 exact bridge and
scalar tails; checkpoint226; the September23 strategy; accepted complete
wave/moment kernel; initial reports, separate reviews and conductor
controls. Exact bindings, role histories, sources and repairs are in
the reconciliation and final_evidence_hashes.json. Claimants did not read
current sibling or blind reports before initial freeze. Closed200--227
and both legacy directories remain immutable. Only the conductor owns
the synthesis, validation state and patch; no subagent starts a successor.

## 7. State effect and next design

Identity patch: all401 graph nodes and proof-draft bytes unchanged.
The new full continuous estimate is retained as reviewed component
evidence, not an accepted full-wave gain. No dependency-closed promotion
of the inherited spectral bridge is packaged in this round. Round229
is the mandatory broad strategy/current-primary review, pending design.
It should compare the remaining complete cusp obstacle with all other
full-proof frontiers and test whether another spectral attack has a
concrete new saving mechanism. Repeating a positive norm price is not
progress. No successor is launched in this closure.
''')

interventions = [
    'Frozen all-shift objective unchanged; three fresh fork_none initial roles, with scalar statement-only isolation.',
    'Conductor required actual primitive conductors, root numbers, Euler-two depletion, oldspace weights, full dual tails and restored norm costs.',
    'The entire continuous component retained all three cusps, both signs, every shift and all low/high tails; source and AFE moving-weight hypotheses were checked.',
    'Two initial reports received disclosed byte-only carriage-return repairs; all final reviews bind corrected hashes.',
    'Conductor requested an explicit small-n dual-envelope audit; nonauthor review supplied the positive-contour pole argument as well as stationary-symbol checks.',
    'The root gamma control widened its valid large-pair window to cover bounded t; its final version has a separate nonauthor application review.',
    'The continuous component gain is distinguished from a complete-wave gain; the whole cusp owner and original full coefficient cap are restored.',
    'No source printing defect, formal inversion or upper-certificate loss is treated as an estimate or actual lower bound.',
    'Identity patch only; mandatory review229 remains pending design, with no successor launched.',
]
reason = ('The complete continuous component is reviewed at raw A_J^2 N^(3/2)T^epsilon using exact CM values and a proved degree-two mean square. '
          'The actual cuspidal functional equation has dual scale qt/(pi^2 L) and surviving phase (qdR^2/n)^(it), but its paid positive certificate '
          'A^2 T^(3/2)N^(5/4) does not improve the whole arithmetic cap. The remaining complete signed cusp target is unproved; no complete-wave or exponent gain.')
first = ('Uniformly for actual signed g_N, every R~T, all dyadic2<=N<=P<2T^(3/2), prove '
         '2Re D<=C_epsilon,J A_J(N)^2 N^(3/2)T^epsilon, where D is the ENTIRE exact level1/2 cusp expression in '
         'complete_eisenstein_pairing(5), equivalently signed_hecke_functional_attack(24), with every h<2N, '
         'two-adic descendant, old/new factor, discrete mode and full scalar tail. The entire continuous component is reviewed at the allowed target error.')
decision = dict(round_index=228, campaign_id='gc-signed-heegner-phase', generated_at=now,
    decision='close_bounded_signed_phase_attempt_retain_complete_continuous_evidence_and_full_cusp_owner',
    terminal_label='complete_signed_heegner_no_new_bound', graph_mutation=False,
    complete_frontier_bound_improved=False, complete_moment_bound_improved=False,
    complete_continuous_component_bound_reviewed=True, pointwise_exponent_change=False,
    reason=reason,
    goal_turn_classification='progress_reviewed_complete_continuous_component_and_cusp_reduction_no_complete_wave_gain',
    next_objective='Mandatory broad strategy/current-primary review229 of the full proof goal and all complete alternatives after closed228.',
    next_method='Audit recent primary literature and compare the newly paid entire continuous component, remaining entire cusp inequality, full M1/M2/GAR and sufficient moment alternatives; select one bounded next analytic objective only after the review closes.',
    first_unproved_estimate=first, interventions=interventions)
decision['state_note'] = reason + (' Identity State Patch: all401 nodes and proof-draft bytes unchanged. '
    'Reviewed spectral evidence has not been packaged into a dependency-closed graph promotion. '
    'M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR lower ownership through159, endpoints and sufficient unbounded fixed-order alternatives remain open; fixed twelfth is not quarter. '
    'No actual arithmetic lower bound or all-method no-go. Zero experiments. Mandatory strategy/current-primary review229 pending design. First complete unproved estimate: ') + first
put(base / 'controls/closing_decision.json', decision)
reviews = [dict(path=(base / 'reviews' / (name + '.md')).as_posix(), reviewer=reviewer,
    claimant=claimant, reviewed={p.as_posix(): sha(p) for p in arts}, mode=mode)
    for name, reviewer, claimant, arts, mode in spec]
reviews.append(dict(path=owner.as_posix(), reviewer='/root', mode='conductor_complete_frontier_review',
    reviewed={p.as_posix(): sha(p) for p in [attack, continuous, blind, control] + review_paths},
    limitation='Root-authored scalar application has its separate nonauthor review.'))
put(base / 'controls/review_dispatch_provenance.json', dict(round_index=228, generated_at=now,
    frozen_objective_changed=False, maximum_concurrent_subagents=3,
    mathematical_numerical_experiments=0, original_report_claimants={
        attack.as_posix(): '/root/signed_hecke_functional_attack',
        continuous.as_posix(): '/root/complete_eisenstein_pairing',
        blind.as_posix(): '/root/blind_gamma_transition', control.as_posix(): '/root'},
    reviews=reviews, interventions=interventions,
    isolation='Initial roles fresh fork_none; blind initial context only protocol and isolated statement. Claimants froze before reciprocal reviews. Later application review retained only disclosed own history and the root control.',
    source_policy='At most one additional primary work per nonblind role; the continuous role added exact Leong v5 Corollary4. No broad literature review or silent source repair.'))
write(base / 'reviews/conductor_round228_reconciliation.md', r'''# Round228 conductor reconciliation

## 1. Result

GREEN for scoped signed Heegner and gamma-transition evidence only.
The complete continuous component meets the target; the entire cusp
inequality and full wave remain unproved. No accepted exponent changes.

## 2. Exact statement and hypotheses

Frozen228 objective unchanged: actual r2, real signed fixed Schwartz
weight, every R~T, every dyadic N<=P, all shifts, both cusp levels and
all three continuous cusps. Raw full target A_J^2N^(3/2)T^epsilon.
Inherited real beta stays exclusively a complete real-wave estimate.

## 3. Proof and reconciliation

Three reports and root control have nonauthor final-hash checks. The
continuous CM factors, theta equation, AFE poles, moving-weight mean
square, source range and full tails are paid. The primitive cusp
conductors, oldspace factors and local depletion lead to an exact short
dual transform with surviving spectral oscillation. Its small-n envelope
is justified by crossed poles, not an extrapolated large-n expansion.
The complete positive cusp certificate remains worse than the original
coefficient cap. The root independently reproduces these full costs and
Fejer restoration in its frontier review. Formal inversion is no saving.

## 4. First unproved step

The ENTIRE remaining one-sided cusp bound 2Re D<=C A^2N^(3/2)T^epsilon,
as defined in the continuous report(5) or discrete report(24), remains
unproved with every mode, shift, old/new factor and tail. Paying the
entire continuous complement is useful scoped evidence, not full closure.

## 5. Required controls and outcome

All required mathematical review seams GREEN within scope. Initial blind
derivation remained isolated; root application has a distinct nonauthor
review. Disclosed byte-only repairs were rebound. Zero experiments.
Mechanical closure checks frozen scope, final hashes, graph/campaign
schemas, all732 prior archive entries, identity application and replay,
all401 graph nodes, unchanged draft bytes and protected legacy paths.
No successor starts before closure; review229 remains pending design.

## 6. Dependencies and exact artifact bindings

FINAL_HASH_BINDINGS

Bindings are inserted before shared-state writes. Review provenance
records claimants, reviewers, isolation, sources and conductor interventions.

## 7. Recommended state effect

Identity patch only. Retain reviewed component/transform evidence without
a graph or draft change. No dependency-closed spectral promotion is
packaged here. Close228; leave mandatory strategy/current-primary
review229 pending design. All full proof alternatives remain open.
''')
all_evidence = list(frozen) + review_paths + [owner, base / 'synthesis.md',
    base / 'controls/closing_decision.json', base / 'controls/dispatch_provenance.json',
    base / 'controls/review_dispatch_provenance.json']
put(base / 'controls/final_evidence_hashes.json', {p.as_posix(): sha(p) for p in all_evidence})
print(json.dumps(dict(status='round228_closing_evidence_assembled', evidence_count=len(all_evidence),
                      shared_state_written=False), indent=2))
