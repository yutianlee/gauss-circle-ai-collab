from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from math_collab.campaigns import validate_campaign,_brief_text
from math_collab.proof_obligations import load_graph,validate_graph
root=Path.cwd();rel=Path('rounds/codex-managed/gc-signed-sixth-dispersion');b=root/rel
for name in ['briefs','reports','reviews','candidates','controls/prelaunch_state']:(b/name).mkdir(parents=True,exist_ok=True)
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=read(root/'state/active_campaign.yml');assert old['round_index']==234 and old['status']=='complete'
g=load_graph(root/'state/proof_obligations.yml');assert not validate_graph(g,root=root)
gh=sha(root/'state/proof_obligations.yml');assert gh==old['resulting_graph_sha256']
allowed=read(root/'rounds/codex-managed/gc-connected-cumulant-test/plan.json')['artifact_policy']['allowed_workflow_changes']
inventory={p.relative_to(root).as_posix():sha(p) for top in ['state','rounds','proofs/kernels','strategy','manifests'] for p in (root/top).rglob('*') if p.is_file() and b not in p.parents and p.suffix!='.pyc'}
write(b/'controls/starting_hashes.json',inventory)
for name in allowed+['state/proof_obligations.yml','state/best_proof_draft.md']:
 p=root/name
 if p.exists():(b/'controls/prelaunch_state'/p.name).write_bytes(p.read_bytes())
now=datetime.now(timezone.utc).isoformat()
interface='''# Round235 frozen signed sixth-moment dispersion interface

Starting graph SHA256 '''+gh+'''. This is an exploratory conjectured mechanism, not a granted estimate. Round234 is closed. The user explicitly requests a bounded Round235 on signed cross-tuple cancellation with Wolfram and independent review.

Use the same actual rho,Psi,w,B_T and fixed smooth eta as the reviewed norm-band ledger. Put gamma=13/125, beta=(50sqrt(1717)-297)/13762, X=T^(52/125), Y=T^(99/125), phi(n)=eta(n/X)-eta(n/Y),

 F(R)=sum_n phi(n)r2(n)n^(-3/4)Psi(sqrt(n/T))cos(2pi R sqrt(n)-3pi/4).

All R are real in the fixed radius window. The reviewed exact B=L+F+H decomposition pays both complements at M12<=T^(29/25+epsilon), including the entire high-norm Schwartz tail; ||F||_infinity<=T^(beta+epsilon) comes from this actual decomposition, not an arbitrary-mask claim. Those inputs and their proof status must be audited from the listed files.

Frozen sufficient target: M6(F)<=T^(193/500+epsilon). Its conjectured diagonal/variance scale is T^(1-6gamma)=T^(47/125). We allow an extra T^(1/100); 47/125+1/100=193/500. Interpolation M12(F)<=||F||_infinity^6 M6(F) has exponent6beta+193/500<29/25, with a SMALL exact margin to verify. The complements then give complete29/25 and conditional sharp102/325. No all-order or quarter theorem follows.

Concrete mechanism to try: radial Poisson on each smooth dyadic norm block F_N (a fixed smooth partition on n~N, X/constant<=N<=constant Y). Retain BOTH Bessel terms before summing dual errors. The leading real difference phase is an odd Schwartz sine kernel, not a positive bump. After a quantitatively paid linearization, the prospective form is

 F_N(R)=R^(-1/2) S_N(R^2)+E_N(R),
 S_N(x)=sum_(m>=1)r2(m) K_(T,N)((x-m)/H_N(x)),
 H_N(x)=2sqrt(x)/sqrt(N),
 K_(T,N)(u)=integral_0^infty q_(T,N)(s) sin(2pi u s) ds,
 q_(T,N)(s)=s^(-1)Psi(sqrt(N/T)s)phi(Ns^2)chi(s^2).

Here chi is the chosen smooth dyadic partition function and q has fixed compact support away from zero with uniform derivative bounds. This formula, its constants/sign, errors, zero dual mode, sum phase, full dual tail and radius-dependent width are to be DERIVED or corrected, not assumed.

Conjectured actual arithmetic input (S6), with the exact kernel thus obtained:

 integral w(sqrt(x)/T)|S_N(x)|^6 dx
       <=C_epsilon T^(2+1/100+epsilon)(T/sqrt(N))^3

uniformly for every required N, all real T and all cutoff transition blocks. H is comparable to T^(151/250)..T^(99/125). The Jacobian and R^(-3) factor would give M6(F_N)<=T^(1+1/100+epsilon)N^(-3/2), hence the target after summing the finite logarithmic partition. Every E_N must be priced in the sixth moment before this implication is accepted.

To attack S6, expand the ACTUAL r2(m)=4 sum_(d|m)chi4(d), or its exact hyperbola form retaining both chi4(d) and chi4(m/d) and the square correction. Exploit the compact Fourier support of K to annihilate small-divisor full progressions, then retain the character phases while grouping reciprocal fractions BEFORE taking norms. Test a signed sixth-order dispersion estimate for those grouped fractions at the true center resolution T^(-2). Attempt to pay the diagonal/paired and rational main terms; keep every moving cutoff and character branch. Simple CRT density approximation is not valid unless its modulus and interval errors are paid; a common-center average is not six independent averages. Returning to the original wave or just restating S6 is not a gain.

In parallel, obtain the direct distinct-six-class formulation: define g_d by replacing a_(ds^2) with phi(ds^2)a_(ds^2), over ALL squarefree d. Prove or refute sum_d|g_d|^2<<T^epsilon X^(-1/2); low d has only high harmonics. If valid, accepted233 finite absorption at p6 pays every repeated-class configuration at T X^(-3/2+epsilon). The remaining one-sided distinct-six integral at193/500 is a SIGNED target. No absolute tuple or connected-cluster bound is granted. This lower-order route bypasses the precise order12 tuple-modulus certificate by seeking an actual signed estimate at order6; it does not refute the old barriers.

Scope controls: arbitrary coefficients; constant arithmetic mean; nonzero one-point resonance; even instead of odd kernel; all harmonics; the exact two chi4 branches; changing H(x); both Bessel terms and infinite tails; norm transitions; signed vs absolute tuple sums; all epsilon/fixed-order quantifiers. Do not erase the sole remaining owner via independence, modulus averaging, or formal centering. Previous upper-tail two-attempt reassessment and Round234 obstruction remain in force.

Budget: three initial tasks about12 minutes, one bounded nonauthor review/repair cycle, at least90% analytical/algebraic and at most10% bounded exact diagnostics. Conductor alone uses Wolfram for shared controls; subagents need no extra computational experiment. Each report has seven protocol sections and exact context hashes, writes only its assigned path and stops. No graph/shared-state edit or successor.
'''
(b/'briefs/actual_interface.md').write_text(interface,encoding='utf-8')
blind='''# Statement-only odd bandlimited progression and sixth-tuple controls

Use Fourier convention e(t)=exp(2pi i t), Khat(xi)=integral K(u)e(-u xi)du. Let q be a fixed real smooth compactly supported function on a positive interval[a,b], 0<a<b, and set K(u)=integral q(s)sin(2pi u s)ds. Assume q is not identically zero where needed. For real x, positive H and positive integer d consider full progressions

 P_d(x,H)=sum_(j in Z)K((x-dj)/H),
 Q_d(x,H)=sum_(j in Z)chi4(j)K((x-dj)/H),
 chi4(j)=0 for even j,1 for j=1 mod4,-1 for j=3 mod4.

Derive exact Poisson formulas, signs and constants, Fourier support and the largest simple thresholds d/H below which each progression vanishes identically. Do not presume the same threshold for the two sums. Restore the j>=1 restriction uniformly when x is large compared with H and d; state an explicit tail bound rather than silently deleting negative j. H may be a positive function of x; the identities are pointwise in H, but averaged estimates need their own uniformity.

For a separate control of a proposed sixth-order cancellation method, consider S(x)=sum_(m in Z)K((x-m)/H). The constant coefficient case may cancel exactly by Fourier support. Determine whether oddness/zero integral alone could nevertheless justify replacing a signed sum over six product integrals by the sum of the moduli of those integrals with a Gaussian-order O(L H^3) bound on a long center interval of length L>>H>>1. Prove or refute the corresponding tuple-absolute claim. Specify endpoints or a nonnegative smooth center window. A scoped lower bound from six nearby m values, if valid, must account for oddness and negative contributions outside the chosen center region. Do not treat a positive selected subcollection of a signed total as a lower bound for that signed total.

No arithmetic application is supplied or to be inferred. Give proof or first gap, exact controls, and the seven protocol sections. Read only protocol, this statement and own brief. No graph, manifest, sibling or history. Write only the assigned report, explicit UTF-8; freeze and stop.
'''
(b/'briefs/isolated_packet.md').write_text(blind,encoding='utf-8')
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',(rel/'briefs/actual_interface.md').as_posix(),'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md','proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md','strategy/round231_balanced_cancellation/conductor_combined_owner.md','strategy/round231_balanced_cancellation/reports/blind_hankel_tail.md','rounds/codex-managed/gc-connected-cumulant-test/synthesis.md']
specs=[
('actual_sixth_bridge','formalizer','selected_context','Derive the full actual p6 band/distinct-class reduction and all complete exponent costs. Independently derive/correct the dyadic Hankel odd-packet formula and linearization, with two-term Bessel error summation and M6 error budgets, variable H(x), transitions and all tails. Assess the conjectured S6 implication and seek any unconditional sector estimate. The arithmetic S6 itself is unproved unless you actually derive it. Do not read siblings.',common),
('signed_fraction_dispersion','discovery','selected_context','Attempt S6 by actual r2 divisor/hyperbola expansion, compact-frequency cancellation of small progressions, and signed reciprocal-fraction grouping at center resolution T^(-2). Retain both character branches, square correction, moving endpoints, common-center dependence and full tails. Derive any paid diagonal or main sector and try the remaining sextuple dispersion. Price every CRT approximation/certificate and give exact first gap or scoped no-go if target unattained. Do not count an identity/self-return as a gain. Do not read siblings.',common+['strategy/round231_cross_label_admission/conductor_decision.md']),
('blind_packet_control','blind_rederiver','statement_only','Solve only isolated_packet.md. Exact progression/filter lemma and sixth-order signed-vs-absolute control; about12 minutes and one frozen seven-section report. No application or source search.',['protocol.md',(rel/'briefs/isolated_packet.md').as_posix()])]
controls=['actual_band_and_complements','sixth_variance_and_repeats','hankel_phase_and_two_term_error','moving_width_and_endpoints','two_character_branches','signed_fraction_resolution','constant_mean_and_absolute_control','complete_exponent_margin','wolfram_local_exact','blind_isolation','history_preservation']
tasks=[]
for name,role,mode,target,context in specs:
 t={'id':name,'role':role,'access_mode':mode,'target':target,'context_files':context,'required_controls':controls if mode!='statement_only' else ['two_character_branches','constant_mean_and_absolute_control','blind_isolation'],'required_output':['Seven protocol sections, exact hypotheses/proof/first gap/controls/dependencies/state recommendation, with context hashes.','Write only assigned report, freeze and stop.'],'status':'assigned','report_path':(rel/'reports'/(name+'.md')).as_posix()}
 if mode=='statement_only':t['excluded_context']=['All except protocol.md, isolated_packet.md and own brief. No graph, manifest, application or sibling.']
 tasks.append(t)
m={'schema_version':1,'round_index':235,'round_type':'bounded_signed_sixth_short_interval_dispersion','campaign_id':'gc-signed-sixth-dispersion','title':'Attempt actual signed sixth-moment cancellation through odd short-interval norm packets','status':'active','max_concurrency':3,'coordinator':'Codex','generated_at':now,'user_date':'2026-10-12 Asia/Shanghai','starting_graph_sha256':gh,'prior_upper_tail_attempts_completed':2,'prior_connected_cumulant_attempts_completed':1,'resource_policy':{'analytical_algebraic_minimum_percent':90,'numerical_experimental_maximum_percent':10,'budget':'Three initial tasks about12 minutes; one bounded nonauthor review/repair cycle; shared exact Wolfram/local controls; close before successor.'},'target_obligations':['GC-target','GC-complete-fixed-even-moment-distinct-absorption','GC-complete-distinct-radical-twelfth-reduction'],'frozen_target':{'question':'Can actual signed reciprocal-fraction dispersion prove a sixth-moment norm-band bound strong enough to pay the complete29/25 twelfth target?','reference_formula':'M6(F_(13/125))<=T^(193/500+eps); sufficient actual odd-packet input S6<=T^(2+1/100+eps)(T/sqrt(N))^3; no input presumed proved.','quantities':['Same actual full smooth band and paid complements.','All squarefree classes and harmonics; p6 variance budget T^(47/125+eps).','Character/hyperbola and Hankel errors retained; true center resolution T^(-2).','6beta+193/500<29/25 to be independently checked; fixed p12 consequence is not quarter.']},'completion_criteria':['Three frozen reports, one statement-only important lemma.','Independent nonauthor reviews of actual complete bridge, arithmetic dispersion and control scope.','Exact Wolfram checks independently reproduced locally.','All unproved steps exposed; no complete promotion without proof.','Conductor synthesis, validated State Patch and history preservation; close235 before any successor.'],'controls':controls,'tasks':tasks,'review_seams':[{'id':'actual_bridge','requirement':'Full band, variance, Hankel, two-term errors, moving width and complete costs.'},{'id':'arithmetic_dispersion','requirement':'Both character branches, exact cutoffs, signed grouping, true resolution and no unproved CRT average.'},{'id':'control_scope','requirement':'Statement-only filter, constant/absolute controls, exact margin and first gap.'}],'exit_labels':['signed_sixth_complete_gain_reviewed','signed_sixth_attempt_closed_without_complete_gain'],'conductor_interventions':['User explicitly authorized Round235 on signed cross-tuple cancellation.','Select lower-order actual moment and divisor/reciprocal-fraction dispersion as the concrete new mechanism; no reuse of a tuplewise modulus estimate.','Prior closed234 results remain reviewed evidence, not new accepted graph mathematics.']}
assert not validate_campaign(m,g,root=root)
write(b/'plan.json',{'campaign':m,'provenance':{'graph_path':'state/proof_obligations.yml','graph_sha256':gh,'generated_at':now},'artifact_policy':{'state_owner':'conductor_only','computation':'diagnostic_only','allowed_workflow_changes':allowed,'promotion_rule':'Separate reviewed exact kernel and all green gates required; a conditional target is not a complete gain.'}})
write(root/'state/active_campaign.yml',m)
for t in tasks:(b/'briefs'/(t['id']+'.md')).write_text(_brief_text(m,t,graph_hash=gh,generated_at=now)+'\nWrite ONLY `'+t['report_path']+'`. Freeze and stop.\n',encoding='utf-8')
ledger=read(root/'state/round_ledger.yml');prev=read(b/'controls/prelaunch_state/round_ledger.yml');assert not any(r['round_index']==235 for r in ledger['rounds'])
ledger['active_round']=235;ledger['rounds'].append({'round_index':235,'campaign_id':m['campaign_id'],'type':m['round_type'],'status':'active','objective':m['frozen_target']['question'],'started_at':now,'starting_graph_sha256':gh,'tasks':[{'id':t['id'],'role':t['role'],'status':'assigned'} for t in tasks],'resource_policy':m['resource_policy']});write(root/'state/round_ledger.yml',ledger)
future=read(root/'state/next_round_plan.yml');future.update(round_index=235,status='active',campaign_id=m['campaign_id'],tasks=[t['id'] for t in tasks],starting_graph_sha256=gh,candidate_objective=m['frozen_target']['question'],launch_record={'started_at':now,'campaign':m['campaign_id'],'authorization':'Explicit user request to launch bounded Round235 with Wolfram and independent review.'});write(root/'state/next_round_plan.yml',future)
summary='# Round235 active: signed sixth-moment dispersion\n\nTest the literal norm-band M6 bound at193/500 through actual odd short-interval r2 packets and signed reciprocal-fraction dispersion. Complete29/25 restoration, character branches, errors and controls are part of the task. The target is conjectured, not a proved input. Three bounded tasks and independent review; graph and draft unchanged pending validation. No automatic successor.\n'
for name in ['state/current_round.md','state/next_campaign.md']:(root/name).write_text(summary,encoding='utf-8')
p=root/'state/failure_ledger.md';p.write_bytes((summary+'\nKeep the234 absolute connected-cluster obstruction, old two-attempt upper-tail reassessment, all moving-cutoff errors, and the two character branches. A compact-frequency identity is not a sixth moment estimate.\n\n---\n\n').encode('utf-8')+p.read_bytes())
assert ledger['rounds'][:-1]==prev['rounds'];print(json.dumps({'round':235,'status':'active','tasks':3,'preexisting_files':len(inventory),'graph_sha256':gh}))
