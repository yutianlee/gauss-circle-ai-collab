"""Assemble reviewed round227 evidence only; no shared-state writes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
base=Path('rounds/codex-managed/gc-complete-joint-spectral-remainder')
assert not (base/'controls/artifact_hashes.json').exists()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def put(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
now=datetime.now(timezone.utc).isoformat()
attack=base/'reports/joint_shift_spectral_attack.md'
profile=base/'reports/heegner_joint_norm_audit.md'
blind=base/'reports/blind_mellin_phase.md'
control=base/'controls/conductor_mellin_phase_application.md'
packet=base/'briefs/blind_mellin_phase_statement.md'
initial={attack:'9df8afa574a54a6d9c7ca587030aeaec00a7daa345594d224116a93e823d3560',
 profile:'cc921c6d04fb7015e68915000badffa82ff284734460e0be57b2260197443909',
 blind:'31553bbee7f049e3b2cbea58f04634854bfe4551ac484fb85d308cbce07d96e2',
 control:'1a519e5624ef72b28544a9762584f88a26b000377b572b308f7100d7f527cef4',
 packet:'8f4f90d6cb580fc9485729690753d76c7bc64b7d79085e5e710e7fbd5f9ae49a'}
for p,h in initial.items():assert sha(p)==h,(p,sha(p))
spec=[
 ('conductor_mellin_phase_review','/root','/root/blind_mellin_phase',[blind,packet],'nonauthor_statement_only_derivation_review'),
 ('independent_spectral_attack_review','/root/heegner_joint_norm_audit','/root/joint_shift_spectral_attack',[attack],'post_freeze_nonauthor_kernel_source_and_cost_review'),
 ('independent_heegner_norm_review','/root/joint_shift_spectral_attack','/root/heegner_joint_norm_audit',[profile],'post_freeze_nonauthor_orbit_norm_and_cost_review'),
 ('independent_mellin_application_review','/root/blind_mellin_phase','/root',[control],'post_isolation_nonauthor_application_review')]
review_paths=[]
for name,reviewer,claimant,arts,mode in spec:
 p=base/'reviews'/f'{name}.md';s=p.read_text(encoding='utf-8')
 assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8)),p
 assert 'GREEN' in s and all(sha(a) in s.lower() for a in arts),p
 review_paths.append(p)
bindings='\n'.join(f'- {p.as_posix()}: {sha(p)}.' for p in [attack,profile,blind,control,packet]+review_paths)
owner=base/'reviews/conductor_complete_frontier_review.md'
write(owner,r'''# Round227 conductor complete-frontier review

## 1. Result

GREEN for the scoped exact spectral interfaces, scalar transforms and
complete norm-cost assessment. No complete wave or moment bound and no
pointwise exponent improves. The original all-shift target (F) is unproved.
The two spectral reports receive reciprocal nonauthor reviews; the isolated
Mellin lemma and conductor application have separate nonauthor reviews.
This conductor review reproduces the normalization and full restoration.

## 2. Exact statement and hypotheses

Use the frozen complete packet: T>=2, every real R in [cT,CT], every dyadic
2<=N<=P<2T^(3/2), actual r2, actual real smooth g_N with signed fixed Psi,
A=(1+N/T)^(-J), and all 1<=h<2N. The sufficient raw target is
2Re sum_h(1-h/(2N))(C_h-rho_h integral W_h)<=A^2 N^(3/2)T^epsilon.
It includes every discrete and continuous overlap. All Schwartz orders
and differentiation counts are fixed after selecting epsilon and tail order.
The inherited beta applies to the complete REAL wave only.

## 3. Independent algebra and analytical restoration

For the first report, Mellin inversion measures n+h. The expression
h^(1-s)/(s-1)=integral_h^infinity y^(-s)dy is exactly the constant-density
transform. On Re(s)=2, the Dirichlet series and its centered atom/density
bracket are absolutely controlled. The atom vanishes only after full
inversion because W_h(0)=0; keeping its finite-contour term is necessary.
Substitution z=it in HKLDW(3.10) gives precisely the report's continuous
coefficient and three-cusp integral. No contour movement or omitted residue
occurs. Its compact-contour spectral sum is taken before the outer limit.

Here is a second elementary derivation of the inverse kernel. Set
a=1/2-it, b=1/2+it. Multiply the beta integrals for
Gamma(s-a)/Gamma(s) and Gamma(s-b)/Gamma(s). Change their product
variable to x=1/(uv)>1 and set v=1/(xu). The resulting Mellin density is
x/[Gamma(a)Gamma(b)] times
integral_0^1 r^(b-1)(1-r)^(a-1)(1+(x-1)r)^(-a)dr.
Euler's integral identifies this as x P_(-1/2+it)(2x-1).
Consequently G(s,it)=integral_1^infinity P(2x-1)x^(-s)dx,
and inversion against q_h gives K_h(t)=h^(-1/2) integral W_h(x)
P(1+2x/h)dx. The powers of h and N therefore agree. This per-mode
identity does not exchange an infinite spectrum with a Mellin limit.

For the second report, the matrix in its (5) has determinant h/4 and
Frobenius square 2(h/4)+n. Thus u(Mi,i)=n/h. Its inverse recovers all
parity-matched quadruples. At odd h, the unhalved matrix has determinant h,
Frobenius square 2h+4n and again u=n/h; the two allowed reductions modulo2
form the conjugate of Gamma0(2). Sign quotienting supplies factor2 in
both cases. Applying the normalized Hecke operator to the smooth radial
automorphic kernel therefore gives the prefactor2sqrt(m), not a borrowed
bound for a disk test. The point stabilizer remains counted by the orbit
sum. The test may be complex by linearity. Its smooth spectral expansion
and all continuous cusps are present before taking any norms.

Independently iterate the pointwise parity recurrence at h=2^k h0. For
k>=2 it gives 2 sum_{a=0}^{k-2}(-1)^a A_{h/2^a}[W_h(2^a x)]
+(-1)^(k-1) S_{h0}[W_h(2^k x)]. In each A term write
m=h/2^(a+2); its radial argument is 2^(a+2)m u=h u.
The final odd term also has argument h u. This proves the common test
and all coefficients in (9), including k=0 and1 separately. The constants
3/pi and1/pi and H_h(i/2)=4pi I_h/h give
48/h sum_{a=0}^{k-2}(-1)^a sigma1(h/2^(a+2))
+8(-1)^(k-1)sigma1(h0)/h.
Using sigma1(2^j h0)=(2^(j+1)-1)sigma1(h0) reduces this to
8(2^(k+1)-3)sigma1(h0)/h for k>=2. At k=1 it is4sigma1(h0)/h0;
for odd h it is8sigma1(h)/h. All are the prescribed rho_h. Conversion
from probability to area-orthonormal eigenfunctions multiplies the stated
point fourth norm by a fixed volume factor, not a growing parameter.

Both formulations give the same scalar Legendre transform. Put
x=h sinh^2(r/2). Then dx/dr=sqrt(x(x+h)), sinh r=2sqrt(x(x+h))/h,
and the physical phase is exactly2pi R sqrt(h)exp(-r/2).
On the overlap r>log3, the r-window has bounded length. The positive
Legendre branch has a stationary point at
t=pi R(sqrt(x+h)-sqrt x), with curvature t/2. Its phase equals
2t+t log(pi^2 R^2 h/t^2). The scalar amplitude is
g(x+h)g(x)sqrt(h sqrt(x(x+h)))/t: the Legendre and stationary
pi/4 factors cancel. This verifies the stated scale t~Rh/sqrt(N).
The exact transform and uniform symbol estimates treat the small-shift
transition; the interior separate-Stirling computation alone cannot.
At t comparable to Lambda_h, |J_h|/sqrt(h)<=A^2 sqrt(N)/Lambda_h.
Nonstationary integration with fixed higher derivatives pays the low and
far spectral tails, including a shrinking smoothly zero-extended overlap.

The isolated Mellin calculation is consistent: log-coordinate curvature
is -L y g_d'(y)>0, where -g_d'>=1/(8y^(3/2)). Its weighted absolute
transform mass costs L^(b+1/2); matching lower order needs a fixed nonzero
interior amplitude. Inverse Fourier reconstruction can instead vanish.
The nonauthor application review records the universal gamma factor -i,
which changes neither critical equations nor the reduced phase. It also
confirms tau-t~Rh^2/N^(3/2); a large tau alone does not justify Stirling
for both numerator gamma factors.

The first report's fixed-contour tails are sufficient independently of
any normalized theta-pairing bound. Integration by parts gives Mellin
tail A^2N^(2+eta)(1+R sqrt(N))^B L^(1-B). At spectral height U>=4L,
gamma decay, normalized Fourier second moments and ordinary Parseval give
an exponentially small tail times fixed powers of L,U,N. Taking
L=T^Q(1+R sqrt(N)), U=4L and fixed large B,Q pays every discarded term.
The retained finite rectangle is not reduced for free to its stationary
part. Ordinary Parseval does not bound the exponentially renormalized
theta pairings; the reversed-limit full Legendre sum stays unasserted.

The whole-functional Heegner formulation bypasses that exchange and the
false coefficientwise point identification. For h~M and U~TM/sqrt(N),
sqrt(m)|H_h|<=A^2 sqrt(N)/U times sqrt(m/h). The geometric sum of the
parity factors is bounded. The stated fixed-point fourth norm is U^(1+eps)
after a square root, and the individual Hecke second norm is U^(1+eps)
because U^2 dominates sqrt(m). Minkowski therefore gives vector norm
A^2 M sqrt(N)T^eps and raw pair price A^2 T M^2 T^eps. The local-Weyl
continuous majorant gives the same price without an invented Eisenstein
fourth moment. The h- and t-dependent vector cannot be inserted into a
fixed-coefficient sieve without paying separation. Even the explicitly
hypothetical fixed-sieve-size norm A^2 sqrt(NM) would cost A^2 T M^(3/2)
in the fourth-moment pairing. Sum all shift bands: respectively
A^2 T N^2 and A^2 T N^(3/2). Neither proves (F).

At M=N the sufficient vector size for this positive method is A^2 N/T,
versus its available upper certificate A^2 N^(3/2). Their ratio is
T sqrt(N), not an actual-vector lower bound. At N=T the hypothetical
sieve still misses a factor T. These observations do not exhaust
phase-sensitive methods or forbid cancellation in the exact signed sum.

Finally the original coefficients cap the full raw remainder by A^2N^(2+eta).
One integration by parts gives |I_h|<=A^2 N^(3/2)/(Th). The normalized
Fejer inequality has multiplier (7N/2-2)/(2N)<2, diagonal A^2N^(-1/2+eta),
density A^2T^(-1)N^eta log(2N), and capped remainder A^2N^(1/2+eta).
Square roots and the complete dyadic sum give complex T^(1/4+epsilon),
including n=1 and the original Schwartz tail above P. Physical restoration
is3/8. The uncapped and hypothetical menus give respectively5/8 and1/2.
All are weaker than the inherited qualified complete REAL benchmark.
If (F) held, the same reconstruction would give complex T^epsilon and
physical1/4; no such estimate is established. The prior complex13/56
certificate is a separate weaker benchmark than the real target, not a
new result here or a per-block beta estimate.

## 4. First doubtful or unproved step

The full signed pairing (10) in the Heegner report, equivalently (25) in
the first report with paid finite truncations, is still unproved at
A^2 N^(3/2)T^epsilon. A named sufficient positive norm requires the
quantified saving above, but that certificate is stronger than necessary.
The next meaningful test must use the actual h^(it) vector together with
the common spectral phase and complete spectra. An exact inversion,
fixed-coefficient sieve with an unpriced twist, or another local sector
does not close this obligation. No all-method impossibility is certified.

## 5. Required controls and outcomes

Final-hash nonauthor reviews are GREEN within scope. Source hypotheses,
zero atoms, constant densities, parity descendants, spectral measures,
all cusps, literal empty overlaps, low/high tails and reconstruction
powers are checked. Source printing defects are not silently corrected.
No current source role read the blind report before freeze; the blind
initial role had only its statement packet and protocol. Its later
application review discloses retained history and does not review itself.
The root application has that separate nonauthor review. Zero mathematical
experiments; at least95 percent analytical/algebraic work. All complete
M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR lower ownership through159 and
endpoint alternatives persist. Both terms of the accepted distribution
bound persist. Fixed twelfth29/25 gives102/325, not quarter; the sufficient
unbounded sequence of fixed even orders remains open.

## 6. Dependencies and exact bindings

'''+bindings+r'''

Root primary checks: HKLDW1705.04771v3 equations(3.7),(3.10) and Lemma3.4;
HKLDW1703.10347v3 Lemma6.1's Fourier bound only; AH2607.13518v1
Theorem1.2 and equation(8); Chamizo2022 Proposition2.2 and its group,
Hecke and density conventions. Exact links and hypothesis cards are in
the reviewed reports. No new external theorem was promoted. AH's
fourth-moment statement is an explicit external premise, not a completed
proof audit of its supporting printed sieve. Source defects do not imply
that separately stated theorem is false. The root independently derived
the algebra and prices above; historical ownership remains graph-controlled.

## 7. Recommended state effect

Identity State Patch only. Retain these exact complete interfaces and
scope-limited norm/phase controls as reviewed evidence. No new accepted
estimate, graph mutation, proof-draft edit or exponent change. Close227
after mechanical validation, leave228 pending design of a bounded actual
signed spectral estimate, and retain broad strategy/current-primary
review229. The full goal remains active.
''')
write(base/'synthesis.md',r'''# Round227 synthesis: complete joint spectral remainder

## 1. Result

The complete signed Fejer target remains open. This round gives two exact
spectral formulations, a reviewed scalar Legendre kernel, an isolated
Mellin-phase derivation, and fully priced norm procedures. It does not
improve any complete wave or moment bound or the pointwise exponent.
The useful new evidence is the complete level-one/level-two Heegner
functional bridge; it removes a proposed coefficient-identification seam
without solving the signed spectral estimate.

## 2. Exact statement and hypotheses

For actual r2, fixed real signed Psi, every R~T and every dyadic
2<=N<=P<2T^(3/2), retain every h<2N in
2Re sum_h(1-h/(2N))[C_h-rho_h integral W_h]. Its sufficient raw upper
target is A_J(N)^2 N^(3/2)T^epsilon. The graph, frozen packet and
checkpoint226 determine all normalizations. The target gives the complete
complex wave and hence quarter only after diagonal, density, singleton,
dyadic partition and infinite Schwartz-tail restoration. None is omitted.

## 3. Derivation and conductor decision

The HKLDW formulation is valid with an explicitly ordered spectral limit
on a finite Mellin contour; both truncations have paid tails. An exact
individual-mode inverse gamma kernel is Legendre. Ordinary L2 of the
regularized theta vector does not justify an exponentially normalized
full spectral interchange. That unproved exchange is explicitly fenced.

The determinant/parity construction independently expresses the entire
actual functional through the two fixed Heegner points at levels1 and2.
All two-adic descendants share the same radial test, and the constant
spectrum reproduces exactly rho_h. Both levels' continuous spectra are
retained. This avoids an unsupported termwise identification at level4;
it does not use a disk smoothing theorem as a uniform growing-test bound.

The exact hyperbolic phase is2pi R sqrt(h)exp(-r/2). The transform is
stationary at t~Rh/sqrt(N), with reduced phase
2t+t log(pi^2 R^2h/t^2). Thus h^(it) is an actual spectral-dependent
twist. The complete fixed-point fourth-moment/Hecke-second-moment norm
price is raw A^2 T N^2. The continuous part is paid with a local-Weyl
majorant. Even an expressly hypothetical free fixed-sieve-size estimate
would leave raw A^2 T N^(3/2). Neither meets the target.

The original coefficient cap A^2N^2 restores complex exponent1/4 and
physical3/8, already weaker than inherited benchmarks. At N=T the
elementary raw cap still needs a T^(1/2) saving for quarter. The named
spectral positive certificate needs T^(3/2); this compares upper bounds,
not actual lower bounds. No universal spectral no-go follows.

The statement-only Mellin derivation and root application agree on
uniform curvature and absolute weighted mass L^(b+1/2), with lower mass
only for fixed nonzero interior data. Signed reconstruction may vanish.
The reviewed interior gamma calculation has a harmless constant -i and
requires tau-t large; the exact Legendre kernel handles its small-shift
transition. No local asymptotic or positive norm is called a full gain.

## 4. First doubtful or unproved step

The actual full signed Heegner pairing, report(10), is unproved at
A^2N^(3/2)T^epsilon, equivalently the other report's paid finite spectral
expression(25). The phase-sensitive spectral sum must preserve the actual
h^(it) vector, the common t phase and every continuous component before
norms. A fixed-coefficient sieve cannot receive a t-dependent vector for
free. A direct level4 discriminant-minus-four point-value transfer also
fails the audited local hypotheses. The whole-functional bridge avoids
that shortcut but establishes no quantitative saving.

## 5. Controls and outcome

Three reports and four nonauthor reviews, plus the conductor complete
review, are frozen and hash-bound. All mathematical checks are analytical;
zero experiments. Source versions and printed restrictions remain literal,
including AH's unusable-as-printed collective-sieve display. Its separately
stated fourth moment is used only as the declared external premise. No
claim is promoted from a source proof typo or a repaired formula.
All M1/M2/GAR/endpoints, both distribution terms, and the sufficient
unbounded family of fixed even moments remain open. Twelfth is not quarter.

## 6. Dependencies and provenance

Frozen round227 packet, strategy, initial reports, root control and final
reviews; closed226 checkpoint and source audit; accepted complete-wave
bridge and moment kernel. Exact bindings and claimant/reviewer provenance
are in the reconciliation and final_evidence_hashes.json. Fresh initial
roles had only their assigned contexts; the blind report was statement-only.
Post-freeze reciprocal reviews disclose their retained initial-role history.
The conductor owns the synthesis and State Patch. Closed200--226 archives
and legacy paths remain immutable; no subagent launched a successor.

## 7. State effect and next design

Identity patch, all401 graph nodes and proof-draft bytes unchanged. No
complete analytic or exponent gain. After227 closes, design228 as one
bounded attempt at the full signed Heegner expression, using its actual
coupled shift/spectral phase and testing any claimed cancellation against
the complete pretrace reconstruction. Do not repeat a positive norm price
or trade the whole target for a new unestimated complement. Next broad
strategy/current-primary review229. Full proof goal remains active.
''')
interventions=[
 'Frozen all-shift objective unchanged; exactly three fresh initial roles with fork_turns none and no sibling reads before freeze.',
 'Conductor independently derived the Mellin curvature and interior joint phase, and flagged the small-shift gamma transition.',
 'Conductor required the arbitrary complex radial orbit/pretrace derivation, matrix/parity normalization and probability-to-area conversion before the Heegner report froze.',
 'Reports retain all discrete/continuous spectra and every atom, density, endpoint and tail; ordinary Parseval does not grant normalized theta growth or a reversed limit.',
 'Claimants froze before reciprocal nonauthor kernel/source/cost reviews; final hashes are bound.',
 'Isolated phase report has conductor nonauthor review; root application has separate nonauthor post-isolation review, including the harmless universal gamma phase -i.',
 'Printed AH collective-sieve defects remain literal; no corrected range, normalization or missing height condition is imported.',
 'Complete norm prices and original coefficient cap are compared only as upper certificates, never arithmetic lower bounds or universal impossibility.',
 'No successor task starts before closure; all other complete owners and the full quarter goal remain open.'
]
reason=('The complete actual remainder has exact ordered HKLDW and whole-functional level1/2 Heegner formulations with paid scalar transforms and tails. '
 'The stated point fourth moment and individual Hecke norm give raw A^2 T N^2; even a hypothetical free fixed-sieve-size twisted norm leaves A^2 T N^(3/2). '
 'The elementary A^2 N^2 cap is still stronger and gives no new complete exponent. The actual signed spectral inequality at A^2 N^(3/2) remains unproved.')
first=('Uniformly for every R~T, dyadic2<=N<=P<2T^(3/2), and actual g_N, prove '
 '2Re{sum_{q=1,2}sum_{j!=0}|u_j(z_q)|^2 V_q(j)+(1/(4pi))sum_{q,cusps}integral |E_cusp(z_q,1/2+it)|^2 V_q_cts(t)dt}'
 '<=C_epsilon,J A_J(N)^2 N^(3/2)T^epsilon, with V_q=sum_{h<2N}(1-h/(2N))L_q,h H_h, exactly as reviewed Heegner report(7)--(10). '
 'Retain all shifts, two-adic factors, continuous spectra and tails; do not replace the signed expression by an unproved sufficient norm.')
decision=dict(round_index=227,campaign_id='gc-complete-joint-spectral-remainder',generated_at=now,
 decision='close_bounded_joint_spectral_attempt_retain_full_signed_target',terminal_label='complete_joint_spectral_remainder_no_new_bound',
 graph_mutation=False,complete_frontier_bound_improved=False,complete_moment_bound_improved=False,pointwise_exponent_change=False,
 reason=reason,goal_turn_classification='progress_reviewed_complete_spectral_interface_changes_next_action_no_complete_analytic_gain',
 next_objective='Bound the COMPLETE actual signed Heegner spectral pairing at raw A_J^2 N^(3/2)T^epsilon or produce a stronger complete restored exponent.',
 next_method='Use the exact level1/2 whole-functional bridge and preserve h^(it) with the common spectral phase before any positive norm. Test phase-sensitive spectral/Hecke summation against complete pretrace reconstruction; quantify every component and tail in one bounded analytic attempt.',
 first_unproved_estimate=first,interventions=interventions)
decision['state_note']=reason+' Identity State Patch: all401 nodes and proof-draft bytes unchanged. '
decision['state_note']+='M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR lower ownership through159, endpoints and sufficient unbounded fixed-order alternatives remain open; fixed twelfth is not quarter. '
decision['state_note']+='No arithmetic lower bound or all-method no-go. Zero mathematical experiments. Round228 pending design; broad strategy/current-primary review229. First complete unproved estimate: '+first
put(base/'controls/closing_decision.json',decision)
reviews=[dict(path=(base/'reviews'/f'{name}.md').as_posix(),reviewer=reviewer,claimant=claimant,
 reviewed={p.as_posix():sha(p) for p in arts},mode=mode) for name,reviewer,claimant,arts,mode in spec]
reviews.append(dict(path=owner.as_posix(),reviewer='/root',reviewed={p.as_posix():sha(p) for p in [attack,profile,blind,control]+review_paths},
 mode='conductor_complete_frontier_reconciliation',limitation='Root-authored phase application has a separate nonauthor review.'))
put(base/'controls/review_dispatch_provenance.json',dict(round_index=227,generated_at=now,frozen_objective_changed=False,
 maximum_concurrent_subagents=3,mathematical_numerical_experiments=0,
 original_report_claimants={attack.as_posix():'/root/joint_shift_spectral_attack',profile.as_posix():'/root/heegner_joint_norm_audit',blind.as_posix():'/root/blind_mellin_phase',control.as_posix():'/root'},
 reviews=reviews,interventions=interventions,
 isolation='Initial roles were fresh fork_none. Blind initial input was only protocol and isolated packet. Initial source roles froze before reciprocal reviews. The blind author later reviewed the root application, disclosing own report history; this is not self-review.',
 source_policy='One additional indispensable exact primary theorem audit per nonblind initial role; no broad new literature review or silent repairs. AH theorem assertion remains an external premise.'))
write(base/'reviews/conductor_round227_reconciliation.md',r'''# Round227 conductor reconciliation

## 1. Result

GREEN for scoped joint spectral and Mellin-phase evidence only.
No complete analytic estimate, moment or exponent improved. The original
full signed Fejer target remains unproved; the complete Heegner functional
is the selected reviewed interface for subsequent bounded design.

## 2. Exact statement and hypotheses

Frozen227 objective unchanged: actual r2, signed fixed mollifier, every
real R~T, all dyadic N<=P, every shift and both spectral decompositions'
continuous terms. Quarter remains the full goal. No complex or blockwise
interpretation of inherited real beta is granted.

## 3. Proof and reconciliation

The three reports, isolated packet and root application have final-hash
nonauthor checks. The root independently reproduced the inverse kernel,
parity and constant densities, joint phase and full norm restoration.
The ordered HKLDW formula has paid finite truncations; its unrestricted
Legendre spectral interchange is not asserted. The independent determinant
construction gives a lawful whole-functional Heegner expression. It is
not a coefficientwise level4 point identity. All norm prices are above
the target, even after an explicitly hypothetical free sieve comparison.
The original coefficient cap remains stronger. No vote, finite identity
or upper-certificate loss is counted as analytic progress or impossibility.

## 4. First unproved step

The full signed Heegner expression(10), equivalently the paid finite
spectral inequality(25), is unproved at A_J^2 N^(3/2)T^epsilon. The actual
h^(it) vector and common spectral phase must remain coupled. No local
stationary estimate or isolated fourth moment closes that full pairing.

## 5. Required controls and outcome

All required mathematical review seams GREEN within scope; zero numerical
experiments. Mechanical closure separately checks schemas, frozen scope,
final hashes, all701 prior archive entries, identity patch application and
replay, all401 nodes, unchanged graph/draft bytes and protected legacy
paths. Source printing defects remain uncorrected and no theorem assertion
is promoted on an unreviewed proof repair. No successor begins before closure.

## 6. Dependencies and exact artifact bindings

FINAL_HASH_BINDINGS

Bindings are inserted before shared-state writes. Claimants, isolation,
reviewers and interventions are recorded in review provenance. Conductor
authorship is not substituted for the independent application review.

## 7. Recommended state effect

Identity patch only; no analytic promotion or proof-draft edit. Close227,
leave228 pending design, retain broad review229 and the active full goal.
All complete M1/M2/GAR/endpoints and sufficient unbounded fixed-order
alternatives remain open. No external blocker is claimed.
''')
all_evidence=[attack,profile,blind,control,packet]+review_paths+[owner,base/'synthesis.md',base/'controls/closing_decision.json',base/'controls/dispatch_provenance.json',base/'controls/review_dispatch_provenance.json']
put(base/'controls/final_evidence_hashes.json',{p.as_posix():sha(p) for p in all_evidence})
print(json.dumps(dict(status='round227_closing_evidence_assembled',evidence_count=len(all_evidence),shared_state_written=False),indent=2))
