"""Prepare224 final conductor artifacts only after final-hash reviews. Never rerun after closure."""
import hashlib,json,re
from pathlib import Path
base=Path('rounds/codex-managed/m9-m1-complete-gar-prime-amplification')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def write(p,o):put(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
assert not (base/'controls/artifact_hashes.json').exists()
attack=base/'reports/complete_signed_prime_attack.md'
profile=base/'reports/actual_prime_profile_control.md'
blind=base/'reports/blind_prime_allocation.md'
control=base/'controls/conductor_grouped_prime_commutator_control.md'
packet=base/'briefs/blind_prime_allocation_statement.md'
review_inputs=[
 ('conductor_finite_allocation_review',[blind,packet]),
 ('independent_complete_attack_review',[attack]),
 ('independent_actual_profile_review',[profile]),
 ('independent_grouped_control_source_review',[control])]
for name,inputs in review_inputs:
 p=base/'reviews'/f'{name}.md';s=p.read_text(encoding='utf-8')
 assert 'GREEN' in s
 assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8)),p
 for a in inputs:assert sha(a) in s.lower(),(p,a)
owner=r'''# Round224 conductor complete-owner review

## 1. Result

GREEN for finite algebra and scoped certificate controls. The complete
signed attack supplies no new bound. Independent final-hash reviews
cover each claimant report and the conductor's grouped control/source.
No complete M1, M2, moment or pointwise exponent improves.

## 2. Exact hypotheses and owners

The real GAR wave uses the actual C_X^*, original-X profiles, literal
D_j=2^(-j)floor(sqrt X), H_j=floor(D_j X^(-1/4)), finite cutoff,
stars and both original signs. Its physical factor is -(4/pi)X^(1/4).
Accepted120 pays the nonlower complement. Every lower scale and later
owner through159 remains. The complete signed baseline is X^(1/12+
epsilon), from the accepted physical total-M1 bound X^(1/3+epsilon).
The desired normalized bound is X^epsilon.

## 3. Independent reconciliation

Inclusion-exclusion of p in the two divisor coordinates subtracts the
overlap exactly once. For split primes the defect is the coefficient
of A(ph,q)+A(h,pq)-2A(h,q), plus the backward coefficient of
A(h,q)-A(ph,pq). The finite adjoint includes the divisibility mask,
p^(3/4), p^(-3/4), phases at X/p and pX, and different exact cutoffs,
while A remains at X. The isolated derivation agrees independently.
At2 only the first-coordinate allocation survives.

Each complete complex main-minus-correction row is exactly twice the
original complex wave. Its real projection is 2G. Thus completed-row
Cauchy has equality, and the full quadratic form is 4k^2G^2. Its
polarization includes both conjugated and nonconjugated channels.
The inherited estimate supplies only k^2 X^(1/6+epsilon). A target
quadratic estimate has not been proved by re-expressing the rows.

Three different positive procedures have separately reviewed controls.
The expanded five-term allocation certificate retains 2A at h=1,
odd q comparable to a fixed small multiple of sqrt X. It costs
X^(1/8) to X^(1/8)log X. The profile report's incidence certificate
has the same scale on the actual h comparable to c X^(1/4),
9h<=q<=10h wedge; A(ph,q)=0, A(h,q)>=3/4 and A(h,pq)<=1.
The source-audited conductor control instead aggregates divisors AND
primes before the coefficient modulus. Distinct split semiprimes ab
in a short fixed relative interval give E_p(ab)>=7/10 for every
amplifier prime satisfying p ab<=s sqrt X. Its finite lower mass is
c v(M)(v(M)-1)M^(-3/2), and fixed-modulus PNT yields
X^(1/8) P^(-1/4)/log^2 X in the stated P<=X^(1/2-eta) range.
These are different certificates, with different scopes. None bounds
the signed radial wave from below. No large-prime loophole improves
the supplied estimates: above floor(16sqrt X) the main is zero and the
defect is exactly -2c_X on the tested support.

The full separately priced main has normalized price at most
X^(1/8+epsilon) times the prime average of p^(-1/4)+p^(-1).
The correction certificate retains its X^(1/8) price. Physical
restoration gives X^(3/8), worse than the inherited X^(1/3). Reusing
the latter within the exact signed identity only returns itself.
This is failure of these specified estimates, not of every possible
coefficient-sensitive amplification argument.

## 4. First unproved step

A complete real signed main-minus-correction bound of k X^epsilon,
or one improving k X^(1/12+epsilon), is still missing. No uniform
arbitrary-vector estimate, changed-centre average or coefficientwise
flattening can be silently substituted. The first gap is analytical,
not an external blocker.

## 5. Controls and ownership

GREEN for finite signs, all prime-power overlaps, prime2, fixed-X
heights, literal stars/floors, all cutoffs, nonlower ownership, complete
lower range, norm restoration, real pairing and actual-versus-certificate
scope. The only external theorem is fixed-modulus PNT for auxiliary
semiprime factors; it is not imported as a GAR estimate. Source and
application review are separate from accepting a theorem in the graph.
Zero mathematical experiments. Total-M1 scope does not discharge
blockwise M1, any M2 parent, endpoint uniformity or the quarter goal.

## 6. Dependencies and final bindings

Conductor, round224, 2026-09-28; claimant of grouped control, whose
mathematical/source verification was assigned to a different agent.
The two application reports were cross-reviewed by nonauthors; the
blind report received a conductor review. Current statement-only
isolation is preserved with prior histories disclosed.

BINDINGS

Authoritative graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Inherited sources are the exact assigned120/121/159 context and the
closed223 checkpoint. The pinned September23 strategy remains intact.

## 7. Recommended state effect

Close224 with an identity State Patch after schema and archive checks.
All401 graph nodes and proof-draft bytes stay unchanged. Retain only
scoped route evidence; no complete analytic progress is claimed.
Do not repeat this scalar self-return or split it into more unestimated
prime sectors. Design225 only from closed224; broad review remains226.
'''
owner_inputs=[attack,profile,blind,control]+[base/'reviews'/f'{n}.md' for n,_ in review_inputs]
owner=owner.replace('BINDINGS','\n'.join(f'- {p.as_posix()}: {sha(p)}.' for p in owner_inputs))
put(base/'reviews/conductor_complete_owner_review.md',owner)
decision=dict(round_index=224,decision='retain_graph_close_bounded_split_prime_attempt',
 terminal_label='complete_gar_amplification_no_new_bound',graph_mutation=False,
 complete_frontier_bound_improved=False,complete_moment_bound_improved=False,pointwise_exponent_change=False,
 reason='Every completed prime row equals twice the original actual wave. Completed-row Cauchy returns the inherited GAR X^(1/12+epsilon) bound. The full positive allocation and incidence certificates cost X^(1/8), hence physical X^(3/8), worse than inherited X^(1/3). A separately reviewed actual grouped-coefficient semiprime control also shows a loss in its stated prime range, but none of these is a signed lower bound. No complete bound improves.',
 goal_turn_classification='no_progress_on_complete_bounds_bounded_mechanism_closed_with_verified_controls',
 mathematical_assessment='no_complete_estimate_or_exponent_gain',
 first_unproved_estimate='Bound the complete fixed-X real main-minus-commutator expression by |Pcal| X^epsilon, or improve its inherited |Pcal| X^(1/12+epsilon) bound, with all original profiles, signs, endpoints and lower owners retained. The exact identity is not a new estimate.',
 next_objective='After224 closure, design225 around one complete signed parent estimate with an identified arithmetic property and a quantitative inequality capable of beating the inherited exponent.',
 next_method='Pending conductor selection after closure. Do not repeat completed-row scalar amplification, an incidence/coefficient triangle, complementary inversion or another unestimated local sector. Any continuation of GAR must estimate its actual radial phases before separate positive norms; a different complete route must retain all of its physical costs and companions. No successor has been frozen or started.',
 state_note='Round224 closes the bounded complete-GAR split-prime attempt with no complete estimate or exponent gain. Exact prime allocation retains every overlap and the original-X profile commutator. Completed rows self-return; their Cauchy estimate has equality. The separately priced expanded/incidence procedures retain normalized X^(1/8) mass, worse than the actual complete baseline X^(1/12). The conductor grouped-coefficient control, independently source-audited, is limited to its explicit semiprime range and still says nothing about signed radial size. Identity State Patch; all401 nodes and proof-draft bytes unchanged. Full M1/M2/GAR, endpoints, the sufficient unbounded fixed-even-moment family and the quarter goal remain open. Round225 pending design; next broad strategy/current-primary review226.',
 interventions=[
 'Kept one complete real GAR objective and one prime-amplifier family; no local-sector completion was treated as a gain.',
 'Clarified that the inherited complete GAR baseline is X^(1/12), not its weaker X^(1/8) coefficient triangle.',
 'Retained the actual fixed-X profile, all repeated-prime overlaps, distinct dilated cutoffs and both real polarization channels.',
 'Preserved current statement-only finite derivation with reused-history disclosure and a nonclaimant review.',
 'Distinguished the expanded allocation, incidence and grouped-coefficient certificates from each other and from the signed wave.',
 'Used the one narrow source audit only for fixed-modulus PNT in the auxiliary semiprime control; no theorem was imported into the proof graph.',
 'Obtained cross-reviews of application reports and independent mathematical/source review of the conductor control.',
 'Stopped the tested scheme after no new complete bound; successor design is deferred until validated closure.'])
write(base/'controls/closing_decision.json',decision)
synthesis=r'''# Round224 synthesis: complete GAR split-prime amplification

## 1. Result

Terminal: **complete_gar_amplification_no_new_bound**. The complete real
GAR bound remains \(X^{1/12+\epsilon}\), hence physical total M1 remains
\(X^{1/3+\epsilon}\). No complete bound or pointwise exponent improves.
Exact identities and three carefully separated certificate controls
explain the failed estimates. All proof-state changes are the identity.

## 2. Frozen objective and hypotheses

Estimate the complete real angular-divisor wave G_X at X^epsilon for
every real X, with its actual C_X^*, fixed angular profiles, literal
floors/stars and finite cutoff. Test split-prime divisor allocation
before norms, retaining the main-minus-commutator expression. Accepted120
pays the nonlower range; every lower scale and later owner through159
remains. GAR controls total active M1 only.

## 3. Complete derivation and restored costs

The exact split-prime defect is
c_[A(ph,q)+A(h,pq)-2A(h,q)](n)
+1_(p|n)c_[A(h,q)-A(ph,pq)](n/p).
The overlap is compulsory. Radial adjunction retains p^(3/4),
p^(-3/4), divisibility and both shifted cutoffs. The profile stays at X,
even when the wave has parameter X/p or pX.

Each completed row is exactly twice the original wave. The full real
quadratic form, including the nonconjugated channel, is 4k^2G_X^2;
completed-row Cauchy is equality. The inherited estimate gives only
k^2 X^(1/6+epsilon), with no saving in k.

The complete main-term absolute price alone decreases with
p^(-1/4)+p^(-1), but the full correction cannot be deleted. The tested
five-term positive allocation certificate and the independently examined
incidence correction both lie between cX^(1/8) and CX^(1/8)log X.
Their lower controls use actual profiles inside the unpaid lower range.
Physical restoration costs X^(3/8), worse than inherited X^(1/3).
For p above the finite coefficient support, the main is zero and the
correction is exactly -2c_X: choosing larger primes returns the target.

A separate conductor control addresses grouping before the modulus.
For distinct split primes a,b in [M,(1+delta)M] and every amplifier
prime with p ab<=s sqrt X, the actual aggregated defect E_p(ab)>=7/10.
The finite prime-summed coefficient certificate is at least
c v(M)(v(M)-1) M^(-3/2). The sole narrow source import, fixed-modulus
PNT, yields X^(1/8)P^(-1/4)/log^2 X for P<=X^(1/2-eta), fixed eta>0.
This is a lower bound for that grouped coefficient certificate only.
It neither proves a signed lower bound nor excludes all amplification.

All complete owner costs, nonlower payment, transform errors, inactive
bottom, hard/smooth labels and later lower dependencies remain. No
estimate for individual M1 blocks, M2, endpoints or moments follows.

## 4. First unproved step and conductor decision

The complete fixed-X real main-minus-commutator sum still requires
k X^epsilon, or an improvement over k X^(1/12+epsilon). This is the
original analytical difficulty. Exact re-expression, completed-row
Cauchy and positive certificates do not supply the needed inequality.
The bounded attempt stops. Its verified diagnostics do not count as
complete analytic progress under the September23 strategy.

Round225 remains pending design until224 is mechanically closed. Its
method must use an actual signed arithmetic property in a complete
estimate with quantitative room after reconstruction; repeating this
scalar identity or subdividing the correction is not a new strategy.
The full goal stays active; no external blocker is claimed.

## 5. Controls and review outcome

Three seven-section reports, current statement-only finite algebra,
nonclaimant application cross-reviews, independent conductor-control
and fixed-modulus source audit, plus conductor complete-owner review.
All final hashes are checked before closure. Control scopes distinguish
incidence, grouped coefficients and signed radial sums. All prime
valuations, prime2, real pairing, floors/stars and cutoffs are retained.
Zero mathematical experiments; at least95 percent analytical effort.

## 6. Dependencies and provenance

Campaign m9-m1-complete-gar-prime-amplification, round224, 2026-09-28.
Exact inputs and primary citation are in reports and the conductor
control. The only source is Tao's explicit fixed-modulus PNT statement;
its later heuristic exposition is not used as a proof. The independent
review audits both the theorem statement and its limited application.
The pinned September23 review and closed200--223 evidence are unchanged.
Starting graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Final report/review hashes are bound in conductor reconciliation.

## 7. State effect

Identity State Patch: zero creates, updates, corrections or rejections.
All401 nodes and the proof draft remain byte-identical. Close224 only
after all gates, schema/identity replay and605 previous archive entries
pass. Leave225 pending design, with broad strategy/current-primary
review226. All complete proof frontiers and the quarter goal remain open.
'''
put(base/'synthesis.md',synthesis)
judge=r'''# Round224 conductor reconciliation

## 1. Result

GREEN for scoped algebra and certificate evidence only. No complete
analytic or exponent gain. Close the tested split-prime attempt after
mechanical validation; all complete targets remain open.

## 2. Exact scope

The frozen complete real GAR objective retains actual fixed-X profiles,
all signs, overlaps, integer endpoints, lower scales and physical costs.
It is a total-M1 contribution, with every M2 and endpoint still required.

## 3. Reconciliation

Independent finite allocation agrees with both application reports.
Completed rows self-return, so their Cauchy estimate yields no gain.
Full positive closures retain X^(1/8) mass and cost physical X^(3/8),
worse than inherited X^(1/3). The independently audited grouped
semiprime control has its own explicit range and fixed-modulus source.
None of these certificate lower bounds is a signed-wave lower bound.
Application reports were reviewed by their nonauthors. The conductor
reviewed the isolated lemma; a different agent checked the conductor
control and source. All histories and isolation scopes are disclosed.

## 4. First gap

The complete joint signed inequality remains unproved. A new bound,
not another scalar identity or a new name for the same residual, is
needed. No external blocker is asserted.

## 5. Controls

Exact prime2 and prime-power cases, adjoint signs, radial cutoffs,
fixed-centre profiles, hard stars, lower-range buffers, grouped versus
incidence norms, both real channels, source hypotheses and complete
physical restoration were checked. Zero mathematical experiments.
All prior archives and graph/draft bytes must pass closure validation.

## 6. Exact final artifact bindings

FINAL_HASH_BINDINGS

The closure script inserts the final hashes only after all reviews and
scope checks. Starting-state and frozen-packet hashes remain separate.

## 7. Recommended state effect

Identity patch with no graph or proof-draft rewrite. Close224; leave225
pending design and next broad review226. The full goal remains active.
'''
put(base/'reviews/conductor_round224_reconciliation.md',judge)
reviews=[base/'reviews'/f'{n}.md' for n,_ in review_inputs]+[base/'reviews/conductor_complete_owner_review.md']
evidence=[attack,profile,blind,control,packet]+reviews+[base/'controls/dispatch_provenance.json',base/'synthesis.md',base/'controls/closing_decision.json']
write(base/'controls/final_evidence_hashes.json',{p.as_posix():sha(p) for p in evidence})
write(base/'controls/review_dispatch_provenance.json',dict(round_index=224,
 review_roles={'finite_allocation':'conductor','complete_attack':'/root/joint_divisor_kernel','actual_profile':'/root/full_frontier_sources','grouped_control_and_source':'/root/joint_lattice_kernel','complete_owner':'conductor'},
 statement_only_report_frozen_before_application_review=True,source_audits=1,mathematical_numerical_experiments=0,
 scope='Reviews occurred only after task reports froze. No reviewer certifies its own report. Conductor grouped control is independently reviewed.'))
print('Round224 conductor synthesis/decision and final bindings prepared; closure not yet applied.')
