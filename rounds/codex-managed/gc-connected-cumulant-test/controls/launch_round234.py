"""Conductor: freeze one bounded connected-correlation test after closed233."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from math_collab.campaigns import validate_campaign,_brief_text
from math_collab.proof_obligations import load_graph,validate_graph
root=Path.cwd(); rel=Path('rounds/codex-managed/gc-connected-cumulant-test'); base=root/rel
for n in ['briefs','reports','candidates','reviews','controls/prelaunch_state']: (base/n).mkdir(parents=True,exist_ok=True)
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
old=read(root/'state/active_campaign.yml'); assert old['round_index']==233 and old['status']=='complete'
g=load_graph(root/'state/proof_obligations.yml'); assert not validate_graph(g,root=root)
gh=sha(root/'state/proof_obligations.yml'); assert gh==old['resulting_graph_sha256']
allowed=read(root/'rounds/codex-managed/gc-fixed-order-moment-absorption/plan.json')['artifact_policy']['allowed_workflow_changes']
inventory={p.relative_to(root).as_posix():sha(p) for top in ['state','rounds','proofs/kernels','strategy','manifests'] for p in (root/top).rglob('*') if p.is_file() and base not in p.parents and p.suffix!='.pyc'}
write(base/'controls/starting_hashes.json',inventory)
for name in allowed+['state/proof_obligations.yml','state/best_proof_draft.md']:
 p=root/name
 if p.exists(): (base/'controls/prelaunch_state'/p.name).write_bytes(p.read_bytes())
now=datetime.now(timezone.utc).isoformat()
actual='''# Round234 actual connected-correlation interface

Starting graph SHA256: '''+gh+'''

Use the literal actual f_d, B_T, Z_Q, E_(p,Q) from accepted233, the same rho, Psi, w, and all harmonics. Freeze p=12 and Q=floor(T^(2/5)); W=integral w>0; probability dnu_T=w(R/T)dR/(TW). For an ordered distinct label tuple d define

 m_S(d)=E_nu product_(j in S) f_(d_j),
 kappa_12(d)=sum_(pi partition[12]) (-1)^(|pi|-1)(|pi|-1)! product_(C in pi) m_C(d),
 K_12=TW sum_d^* kappa_12(d), D_12=I_12-K_12,
 C_conn=TW sum_d^* |kappa_12(d)|.

Proposed mechanism: subtract all lower-order disconnected correlations before estimating the connected aggregate. The exploratory target is K_12<=T^(29/25+epsilon) with D_12 paid at that budget. A hoped-for connected-cluster absolute estimate C_conn<=T^(29/25+epsilon) is a stronger candidate to falsify, NOT a granted hypothesis. Merely rewriting I as K+D is not an estimate.

Concrete tests to attempt: (i) exploit distinct square-root frequencies to show total first- and second-order cross-class means decay faster than every power with smooth radius averaging; (ii) bound the SIGNED sum of each remaining proper partition via independent radius variables, exact collision inclusion-exclusion, uniform square-sums, and accepted actual moments through order9; (iii) test whether cumulant subtraction can materially reduce the known full-harmonic tuple-absolute mass >=c T^(5/2). Keep the original signed target distinct from either certificate.

For the absolute test, a possible coarse block bound to prove or reject is A_q=sum_(distinct labels>Q)|m_[q]| <=T^(max(q/4-1,0)+epsilon), q>=3 fixed; smoothness plus the full Schwartz coefficient tail may give rapid A_1,A_2. If true, each disconnected12 partition is below T^(5/2) after the outer TW. Do NOT assume these bounds or that a coefficient-norm barrier transfers to actual cumulants without proof.

The full-harmonic lower certificate is reviewed admission evidence in strategy/round231_harmonic_admission, not an accepted graph theorem. Re-audit any exact proof used, including squarefree mass, mixed harmonics, and the infinite tail. Complete target restoration may use accepted216: head15/13 and repeated-class error8beta-1/5; target29/25 gives102/325, not quarter. The all-fixed-order233 bridge remains accepted, but no unbounded-order cumulant estimate is supplied by this p12 exercise. Upper-tail A's two-attempt reassessment remains in force; this is a different aggregate mechanism, not a third local packet cutoff.

Budget: 95% analytical/algebraic, at most5% exact diagnostic computation; three initial tasks about10 minutes and one bounded nonauthor review/repair cycle. No next round. Report seven protocol sections, precise limitations and hashes. No graph/draft/shared-state edits.
'''
(base/'briefs/actual_interface.md').write_text(actual,encoding='utf-8')
isolated='''# Isolated multiradius collision lemma: statement only

Do not read the graph, active campaign, sibling reports or application files. This isolated protocol exception is intentional.

Let (Omega,nu) be a probability space and let a finite or countable real measurable family x_d(t) have absolute summability for each t and sufficient domination to justify every integral. Let Z(t)=sum_d x_d(t), V(t)=sum_d x_d(t)^2<=H^2 uniformly, and assume E|Z|^r<=L_r for all integers0<=r<=9 (L_0=1). Partition twelve distinct positions into k>=2 blocks, each block size between3 and9. For each ordered tuple of pairwise distinct labels define the product, over blocks C, of E_nu product_(j in C)x_(d_j).

Prove or refute a bound, independent of the number of labels, for the ABSOLUTE VALUE OF THE SIGNED SUM over all ordered pairwise distinct label tuples of this product. A desired bound depends only on the twelve positions, H, and L_0,...,L_9. It does not put absolute values inside the label-tuple sum. State exact constants or an explicit finite partition bound. Include cases of repeated labels introduced by inclusion-exclusion, mixed powers evaluated at independent radius variables, countable limits, and negative block moments. Identify whether pairwise covariances or lower moments alone would also control the sum of absolute values over tuples, and give a finite control where relevant.

Report the seven protocol sections, proof or first gap, dependencies and exact context hashes. Do not infer any number-theoretic application. Write only your assigned report and stop.
'''
(base/'briefs/isolated_collision.md').write_text(isolated,encoding='utf-8')
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',(rel/'briefs/actual_interface.md').as_posix(),'proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md','proofs/kernels/gc_complete_distinct_radical_moment_reduction.md','proofs/kernels/gc_complete_square_root_large_values_moment_bound.md']
specs=[
('signed_connected_attack','discovery','selected_context','Attempt the actual signed connected aggregate. Prove or refute D12<<T^(1+epsilon) using precise mixed-radius collision algebra and lower actual moments, paying singleton/pair partitions and infinite tails. Then seek a genuinely quantitative bound on K12; state the exact first gap if unavailable. Give complete conditional restoration and controls. Do not read sibling reports.',common),
('connected_certificate_audit','barrier_no_go','selected_context','Test whether C_conn can meet29/25 after all full-harmonic cumulant subtractions. Independently prove requisite absolute block bounds and audit the prior full-harmonic lower-mass proof; derive a scoped actual no-go or locate its gap. Do not mistake it for a lower bound on signed K/I or a theorem rejecting all cumulant methods. Do not read sibling reports.',common+['strategy/round231_harmonic_admission/conductor_harmonic_obstruction.md','strategy/round231_harmonic_admission/reports/blind_harmonic_pooling.md','strategy/round231_harmonic_admission/reviews/harmonic_pooling_seam_review.md']),
('blind_collision_bound','blind_rederiver','statement_only','Solve only isolated_collision.md. About10 minutes; provide independent proof or counterexample, uniformity and domination, exact control, then freeze and stop.',['protocol.md',(rel/'briefs/isolated_collision.md').as_posix()])]
controls=['probability_normalization','actual_full_harmonics','rapid_single_pair','signed_collision_sum','connected_absolute_control','complete_budget','no_signed_lower_bound','wolfram_local_exact','blind_isolation','history_preservation']
tasks=[]
for name,role,mode,target,context in specs:
 t={'id':name,'role':role,'access_mode':mode,'target':target,'context_files':context,'required_controls':controls if mode!='statement_only' else ['signed_collision_sum','blind_isolation'],'required_output':['Seven protocol sections, exact context hashes, proof or first gap, controls and state recommendation.','Write only assigned report, hash and stop; no successor.'],'status':'assigned','report_path':(rel/'reports'/(name+'.md')).as_posix()}
 if mode=='statement_only': t['excluded_context']=['All except protocol.md, isolated_collision.md and own brief; no graph, application or sibling.']
 tasks.append(t)
m={'schema_version':1,'round_index':234,'round_type':'bounded_actual_connected_correlation_test','campaign_id':'gc-connected-cumulant-test','title':'Test connected-correlation subtraction on the actual distinct-class twelfth moment','status':'active','max_concurrency':3,'coordinator':'Codex','generated_at':now,'user_date':'2026-10-12 Asia/Shanghai','starting_graph_sha256':gh,'prior_upper_tail_attempts_completed':2,'resource_policy':{'analytical_algebraic_minimum_percent':95,'numerical_experimental_maximum_percent':5,'budget':'Three bounded initial tasks about10 minutes, one independent review/repair cycle, exact Wolfram/local checks; close before successor.'},'target_obligations':['GC-target','GC-complete-distinct-radical-twelfth-reduction','GC-complete-fixed-even-moment-distinct-absorption'],'frozen_target':{'question':'Does subtracting all disconnected lower correlations yield a quantitatively useful actual signed connected12 estimate at29/25? Test the stronger absolute-cluster mechanism against full-harmonic controls and pay the signed remainder.','reference_formula':'I12=K12+D12; seek D12<<T^(1+eps), K12<=T^(29/25+eps); test C_conn at29/25 rather than assume it.','quantities':['p=12 fixed, Q=floor(T^(2/5)), probability weight w/(TW), all harmonics and signs.','New complete gain requires signed K12 bound, not just paid D12.','No automatic all-order estimate or third old upper-tail packet attempt.']},'completion_criteria':['Three frozen reports including isolated collision derivation.','Nonauthor finite-algebra and full actual certificate/restoration reviews.','Exact Wolfram controls locally reproduced, diagnostic only.','Validated State Patch, graph/history preservation, explicit first gap and terminal decision.'],'controls':controls,'tasks':tasks,'review_seams':[{'id':'signed_remainder','requirement':'Mixed-radius collision algebra, full moment inputs and no absolute-value swap.'},{'id':'certificate_scope','requirement':'Actual lower certificate, every harmonic, Schwartz tail, cumulant correction and scope.'},{'id':'complete_restoration','requirement':'Correct normalized/unnormalized factors, accepted216 costs and open target.'}],'exit_labels':['connected_correlation_complete_gain_reviewed','connected_correlation_test_closed_without_complete_gain'],'conductor_interventions':['Closed233 enables the new fixed-order parent; remaining arithmetic estimate is still open.','Freeze a concrete connected-correlation mechanism and its falsifiable absolute-cluster claim; no premise that cumulants behave independently.']}
assert not validate_campaign(m,g,root=root)
write(base/'plan.json',{'campaign':m,'provenance':{'graph_path':'state/proof_obligations.yml','graph_sha256':gh,'generated_at':now},'artifact_policy':{'state_owner':'conductor_only','computation':'diagnostic_only','allowed_workflow_changes':allowed,'promotion_rule':'No graph promotion without separate reviewed kernel and all green gates.'}})
write(root/'state/active_campaign.yml',m)
for t in tasks:(base/'briefs'/(t['id']+'.md')).write_text(_brief_text(m,t,graph_hash=gh,generated_at=now)+'\nWrite ONLY `'+t['report_path']+'`. Freeze and stop.\n',encoding='utf-8')
ledger=read(root/'state/round_ledger.yml');prev=read(base/'controls/prelaunch_state/round_ledger.yml');assert not any(r['round_index']==234 for r in ledger['rounds'])
ledger['active_round']=234;ledger['rounds'].append({'round_index':234,'campaign_id':m['campaign_id'],'type':m['round_type'],'status':'active','objective':m['frozen_target']['question'],'started_at':now,'starting_graph_sha256':gh,'tasks':[{'id':t['id'],'role':t['role'],'status':'assigned'} for t in tasks],'resource_policy':m['resource_policy']});write(root/'state/round_ledger.yml',ledger)
future=read(root/'state/next_round_plan.yml');future.update(round_index=234,status='active',campaign_id=m['campaign_id'],tasks=[t['id'] for t in tasks],starting_graph_sha256=gh,candidate_objective=m['frozen_target']['question'],launch_record={'started_at':now,'campaign':m['campaign_id'],'authorization':'User keep going with Wolfram after closed233.'});write(root/'state/next_round_plan.yml',future)
summary='# Round234 active: actual connected-correlation test\n\nTest the signed disconnected remainder and the full connected12 aggregate with actual coefficients, all harmonics, independent derivation and controls. A complete gain needs K12 at29/25; an identity alone is insufficient. No graph or proof-draft change. Three bounded tasks and one review cycle; no automatic successor.\n'
for name in ['state/current_round.md','state/next_campaign.md']:(root/name).write_text(summary,encoding='utf-8')
assert ledger['rounds'][:-1]==prev['rounds'];print(json.dumps({'round':234,'status':'active','tasks':3,'protected_files':len(inventory),'graph_sha256':gh}))
