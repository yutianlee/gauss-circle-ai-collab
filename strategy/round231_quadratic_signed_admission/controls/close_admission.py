"""Close reviewed admission evidence; preserve the accepted mathematical state."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, hashlib, datetime, subprocess, sys

root=Path.cwd();p=root/'strategy/round231_quadratic_signed_admission'
def read(x):return json.loads(Path(x).read_text(encoding='utf-8-sig'))
def write(x,d):Path(x).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(x):return hashlib.sha256(Path(x).read_bytes()).hexdigest()
plan=read(p/'plan.json');assert plan['status']=='in_progress','Already closed; do not rerun.'
expected={
 'reports/blind_quadratic_rows.md':'dcf93c50bbc93f8592038c0d1c15e0cddf9ccfe12613be042bfb864908faca6b',
 'reports/quadratic_source_audit.md':'ce861af26fb579ecda5cf5f4a208f28a48ce13ea06744494045030a69c08ff67',
 'reports/quadratic_remainder_attack.md':'abff6860790aba4cda537ad9e81af504c1f175844a2c252479e685077dd1eb24',
 'reviews/conductor_finite_row_review.md':'79b1447291fb80aeb00572ad33fd93f910c3a51098f85f63767dfd56a96086cb',
 'reviews/quadratic_bound_seam_review.md':'d0d25142f4c5bf365d28418d57fb697aad3a964bd674f69b9623f331cee7242b',
 'reviews/source_restoration_seam_review.md':'fdf35ef0fa82b9570fbbcaabf0d5083210e5ccf044d84ffa36c54e2acf38ce66',
 'reviews/type_i_main_and_resonance_review.md':'a47dc8dbfda42b2003282ed0f4d00e9c3815b064df154d445f741adf6c661189',
 'conductor_type_i_main.md':'7b05d13908b116acf2a40320040b4a7614a4f80ec2fcfcde073eb5055957924f'}
for f,h in expected.items():assert sha(p/f)==h,f
reviews=['reviews/conductor_finite_row_review.md','reviews/type_i_main_and_resonance_review.md','reviews/source_restoration_seam_review.md','reviews/quadratic_bound_seam_review.md']
for f in reviews:
 text=(p/f).read_text(encoding='utf-8')
 assert 'PASS' in text,('Missing explicit PASS',f)
assert read(p/'controls/finite_controls.json')['status']=='passed'
protected=read(p/'controls/starting_hashes.json')
def check(item):
 f,h=item
 return f if not (root/f).is_file() or sha(root/f)!=h else None
with ThreadPoolExecutor(max_workers=8) as pool:
 changes=[x for x in pool.map(check,protected.items()) if x]
assert not changes,('Unexpected preclosure changes',changes)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
meta=['state/next_round_plan.yml','state/current_round.md','state/next_campaign.md','state/project_summary.md','state/failure_ledger.md']
write(p/'controls/preclosure_metadata_snapshot.json',{f:(root/f).read_text(encoding='utf-8') for f in meta})
decision={
 'completed_at':now,'status':'not_admitted','analytic_campaign_launched':False,
 'packet':'strategy/round231_quadratic_signed_admission',
 'decision':'strategy/round231_quadratic_signed_admission/conductor_decision.md',
 'mechanism':'Actual quadratic signed twists and higher-uniformity remainder; quartic patches and fully regrouped Type-I approximant',
 'findings':[
  'Proved actual quadratic-twist divisor estimate with arbitrary real linear phase; its short-fibre completion cost does not improve the complete moment.',
  'Statement-only finite quadratic Gram proof and nonauthor review show a dominant common arithmetic component; residual decorrelation does not pay that owner.',
  'Primary2204.03754v4 PropositionA.3 gives actual r2-r2sharp polynomial power savings. Quartic patches repair the length seam throughout the paid norm-head complement.',
  'New independently derived and reviewed component bound: piecewise varying r2sharp, regrouped by divisor without patch-count loss, has supremum T^(5447/52500+epsilon) and M12<=T^(3044/2625+epsilon), below29/25 by1/2625.',
  'The actual residual remains unpaid at a new complete exponent. Its source-based ceiling certificate needs kappa>1/4-beta for strict gain, or kappa>=73/500 for29/25; an unspecified positive source constant certifies neither.',
  'Actual resonant moving quadratic patches refute uniform local square-root cancellation only; no full moment lower bound or polynomial-method impossibility is claimed.',
  'Three nonauthor seams and conductor finite-row review pass;3354 transform and3354 Gram entries and an actual resonant patch reproduced diagnostically.'
 ],
 'scope':'Reviewed component and source evidence only; complete bound unchanged.',
 'graph_effect':'none; no State Patch or promotion',
 'required_new_input':'A quantitative signed estimate for the actual residual after the now-paid Type-I approximant and norm head, using joint or averaged cancellation or a source saving with fully certified strength; preserve complete tails and all real radii.',
 'complete_target':'M12<=T^(29/25+epsilon); accepted10beta=1.289663519481... unchanged.'}
nextp=root/'state/next_round_plan.yml';nxt=read(nextp)
old=nxt.get('latest_admission_check')
if old:nxt.setdefault('admission_check_history',[]).append(old)
nxt['latest_admission_check']=decision
assert nxt['round_index']==231 and nxt['status']=='pending_design' and not nxt['tasks']
write(nextp,nxt)
summary='''# Current research status — signed polynomial admission test closed

11 October 2026. Continued Round231 with an actual quadratic-twist estimate and a newly audited polynomial-uniformity source. The source explicitly estimates r2-r2sharp, and quartic Taylor patches make its short-interval hypothesis valid across the complete complement of the affordable norm head.

A concrete component advance survives independent review: regrouping the patch-dependent Type-I approximant by divisor avoids the patch-count loss. Its complete real wave has supremum T^(5447/52500+epsilon) and twelfth moment T^(3044/2625+epsilon), below the29/25 target by1/2625. Every character fibre, partial endpoint and infinite tail is paid.

The remaining actual signed residual is not proved at an improved complete exponent. The source-based ceiling needs kappa>1/4-beta=0.121033648... for strict moment gain, or kappa>=73/500 for29/25; the source guarantees only an unspecified positive constant. The inherited actual complete bound remains M12<=T^(10beta+epsilon), with10beta=1.289663519481... . No pointwise improvement or quarter theorem follows.

Additional reviewed controls distinguish the raw quadratic rows from their decorrelated residual and exhibit actual resonant short patches. Their scope does not reject joint signed polynomial analysis and gives no lower bound on the actual complete moment. Three reports, three nonauthor seams, a conductor finite-row review and bounded independent controls are complete.

Analytic Round231 remains pending_design. No State Patch, proof-draft change or automatic successor. The graph, accepted kernels, validation matrix, closed Round230 manifest, round ledger, previous admission packets and legacy evidence remain unchanged. Next admission requires a sufficiently strong actual signed residual estimate with every complete owner paid. Decision: strategy/round231_quadratic_signed_admission/conductor_decision.md.
'''
for f in ['state/current_round.md','state/next_campaign.md']:(root/f).write_text(summary,encoding='utf-8')
append='''

## Round231 signed polynomial admission (2026-10-11)

New actual signed inputs were tested. An elementary quadratic-twist divisor bound is valid but its short-fibre completion cost gives no complete gain. Higher uniformity I, arXiv2204.03754v4 PropositionA.3, explicitly supplies polynomial power savings for r2-r2sharp; quartic patches repair its interval-length restriction above the paid norm head. Regrouping the varying approximant by divisor is independently proved and reviewed: its full component has supremum exponent5447/52500 and twelfth-moment exponent3044/2625=29/25-1/2625. The main is paid, but the remaining actual residual is not: the source's unspecified positive saving does not certify kappa>1/4-beta for strict gain or kappa>=73/500 for29/25. Scoped quadratic-row and actual resonant-patch controls forbid specific shortcuts without rejecting joint/averaged signed methods. Reports and nonauthor seams pass, and bounded finite controls were independently reproduced. No accepted complete bound changes; analytic231 stays pending_design with no State Patch. Decision: strategy/round231_quadratic_signed_admission/conductor_decision.md.
'''
for f in ['state/project_summary.md','state/failure_ledger.md']:
 with (root/f).open('ab') as h:h.write(append.encode('utf-8'))
plan['status']='complete';plan['completed_at']=now
for t in plan['tasks']:t['status']='complete'
plan['reviews']=[{'path':f,'status':'pass','sha256':sha(p/f)} for f in reviews]
plan['decision']='retain_new_signed_component_inputs_no_complete_gain_not_admitted'
plan['graph_effect']='none; reviewed evidence only'
plan['resource_outcome']={'analytical_minimum_percent':95,'numerical_maximum_percent':5,'description':'Three analytical reports, independent main proof and three seams, two source applications, finite diagnostic reproduction only.'}
write(p/'plan.json',plan)
validation=[]
for module,args in [('math_collab.validate_state_patch',[]),('math_collab.campaigns',['validate'])]:
 r=subprocess.run([sys.executable,'-m',module,*args],capture_output=True,text=True,encoding='utf-8')
 validation.append({'command':[sys.executable,'-m',module,*args],'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 assert r.returncode==0,r.stdout+r.stderr
with ThreadPoolExecutor(max_workers=8) as pool:
 changes=[x for x in pool.map(check,[(f,h) for f,h in protected.items() if f not in meta]) if x]
assert not changes,('Protected changes after validation',changes)
g=read(root/'state/proof_obligations.yml')
closure={'completed_at':now,'decision':decision,'validation':validation,'protected_files_verified':len(protected),'authorized_metadata_changes':meta,'graph_nodes':len(g['proof_obligations']),'graph_sha256':sha(root/'state/proof_obligations.yml'),'proof_draft_sha256':sha(root/'state/best_proof_draft.md'),'active_manifest_sha256':sha(root/'state/active_campaign.yml'),'review_hashes':{f:sha(p/f) for f in reviews},'status':'passed'}
write(p/'controls/closure_validation.json',closure)
files=[f for f in p.rglob('*') if f.is_file() and f.name!='final_evidence_hashes.json']
write(p/'controls/final_evidence_hashes.json',{str(f.relative_to(p)).replace('\\','/'):sha(f) for f in files})
print(json.dumps({'status':'closed','graph_nodes':closure['graph_nodes'],'protected_files':len(protected),'evidence_files':len(files),'graph_sha256':closure['graph_sha256'],'validators':[x['exit_code'] for x in validation]},indent=2))
