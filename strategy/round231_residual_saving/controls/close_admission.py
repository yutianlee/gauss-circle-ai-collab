"""Close reviewed residual-saving evidence; never mutate accepted mathematics."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, hashlib, datetime, subprocess, sys

root=Path.cwd(); p=root/'strategy/round231_residual_saving'
def read(f): return json.loads(Path(f).read_text(encoding='utf-8-sig'))
def write(f,obj): Path(f).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(f): return hashlib.sha256(Path(f).read_bytes()).hexdigest()
plan=read(p/'plan.json')
assert plan['status']=='in_progress','Already closed; do not rerun.'
expected={
'reports/source_constant_extraction.md':'fb2eda32f5667262f00e4a51e94cdd25d7121659dbdd9578142fcff092a6b954',
'reports/blind_residual_control.md':'c78fa696c881c3068541a38ae807fc1de9a58817c87c30716524e471478a2d2b',
'reports/actual_residual_attack.md':'0d18fa59d915809427e1758ee478ba439303748738e8ec1f86d7e95060dd0bc5',
'conductor_uniform_saving_limit.md':'ffebdca4d1e4ea8ccb1358596626a602c9c53e95226bd3f541c68913ac6187b6',
'conductor_adaptive_factor_cutoff.md':'02727c91e64931a13d3707ca15df021418d3e96510e35894e0d96a70182506fa',
'reviews/review_uniform_control.md':'cfe423ce1503a528e39c0fb96728f052bfe9858762fedf7c800f1d5e4196f872',
'reviews/review_physical_inverse.md':'c6af571bed1e2f82a7aa20e9c5e03a22dc35df5a23c91c3323a6a805e6ff1c32',
'reviews/review_factor_strips.md':'33ca852fc7861847233f901c74df555f4673b39ca08d1a549a26a24914a99b1d'}
for f,h in expected.items(): assert sha(p/f)==h,f
reviews=[f for f in expected if f.startswith('reviews/')]
for f in reviews: assert '**PASS' in (p/f).read_text(encoding='utf-8'),f
assert read(p/'controls/finite_controls.json')['status']=='passed'
assert (p/'conductor_decision.md').is_file()
protected=read(p/'controls/starting_hashes.json')
def check(item):
 f,h=item
 return f if not (root/f).is_file() or sha(root/f)!=h else None
with ThreadPoolExecutor(max_workers=8) as pool:
 changed=[x for x in pool.map(check,protected.items()) if x]
assert not changed,('Unexpected preclosure change',changed)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
meta=['state/next_round_plan.yml','state/current_round.md','state/next_campaign.md','state/project_summary.md','state/failure_ledger.md']
write(p/'controls/preclosure_metadata_snapshot.json',{f:(root/f).read_text(encoding='utf-8') for f in meta})
decision={
'completed_at':now,'status':'not_admitted','analytic_campaign_launched':False,
'packet':'strategy/round231_residual_saving','decision':'strategy/round231_residual_saving/conductor_decision.md',
'mechanism':'Quantified actual signed residual; physical inverse exponents and adaptive actual divisor-factor localization',
'findings':[
'New reviewed adaptive cutoff D_T(x)=T^(-533/5250)x^(29/84) pays every unbalanced actual divisor pair at complete moment29/25, with top-scale cutoff exponent853/3500. Original residual correction, norm head and infinite tail are all paid; central balanced W_* remains open.',
'Fixed alpha11/50 independently gives unbalanced component exponent33787/26250<10beta, without changing the complete bound.',
'Statement-only arithmetic control proves uniform all-polynomial saving kappa<=1/20 for the literal residual, even after any scalar subtraction; independent conductor sequence and source quantifiers imply any valid transferred c<=3/20. This is not a physical-phase impossibility.',
'Actual physical quartic major arcs are empty below explicit thresholds. Any one common degree-d inverse exponent must satisfy C_d>=d, limiting that all-degree ceiling certificate to saving7/72, below1/4-beta.',
'Separate inverse exponents A=3,B=4 would restore complete moment23/18, but those numerical powers remain unproved and are not supplied by the source.',
'Elementary same-character semiprimes keep balanced coefficient energy at least T^(-1/2)/log^2T. This rejects only a coefficient-energy power gain, not a signed-moment gain.',
'Three frozen reports, statement-only independent derivation, three nonauthor reviews including adaptive cutoff, and bounded exact local controls completed.'
],
'scope':'Reviewed component estimates and scoped obstructions; no new complete exponent.',
'graph_effect':'none; no State Patch or promotion',
'required_new_input':'Estimate the actual adaptively balanced W_* signed moment at b<10beta (b<=29/25 for the preferred milestone), or prove sufficiently strong separate physical inverse exponents, with every complete owner paid. The unchanged uniform residual theorem cannot cross its1/20 saving cap.',
'complete_target':'M12<=T^(29/25+epsilon); accepted10beta=1.289663519481... unchanged.'}
nxt=read(root/'state/next_round_plan.yml')
old=nxt.get('latest_admission_check')
if old: nxt.setdefault('admission_check_history',[]).append(old)
nxt['latest_admission_check']=decision
assert nxt['round_index']==231 and nxt['status']=='pending_design' and not nxt['tasks']
write(root/'state/next_round_plan.yml',nxt)
summary="""# Current research status - signed residual saving test closed

11 October 2026. Continued Round231 by quantifying the actual residual and strengthening the signed divisor decomposition. New adaptive cutoff D_T(x)=T^(-533/5250)x^(29/84) pays the entire unbalanced owner at M12<=T^(29/25+epsilon). Near n~T it includes every pair with a factor below T^(853/3500), approximately T^0.243714286. The norm head, original approximant correction, endpoints, and infinite tail are paid at the same preferred budget. The exact central balanced wave W_* remains open.

A statement-only arithmetic derivation and nonauthor review show that the unchanged all-polynomial residual theorem cannot have saving kappa>1/20, even after arbitrary scalar centering. Source quantifiers further force any valid epsilon-independent transferred constant c<=3/20. These are uniform-polynomial obstructions, not physical moment lower bounds.

The physical quartic phase has an explicitly empty major-arc range. A separate exact prime-power control forces any single common inverse exponent C_d>=d; its best all-degree ceiling saving7/72 is still insufficient. Separate powers A=3,B=4 would imply complete moment23/18, but those powers remain unproved. Actual same-character semiprimes also preclude a power gain from balanced coefficient energy alone.

Three reports and three nonauthor reviews pass, including the adaptive-cutoff extension. Bounded exact controls were independently reproduced. The accepted complete bound remains M12<=T^(10beta+epsilon), 10beta=1.289663519481... . No new pointwise exponent or quarter theorem is proved.

Analytic Round231 remains pending_design. No State Patch or automatic successor. The graph, proof draft, accepted kernels, validation matrix, closed Round230 manifest, round ledger and all earlier evidence remain unchanged. Next admission needs a quantitative actual signed estimate for W_* or proved adequate separate inverse powers with full restoration. Decision: strategy/round231_residual_saving/conductor_decision.md.
"""
for f in ['state/current_round.md','state/next_campaign.md']:(root/f).write_text(summary,encoding='utf-8')
append="""

## Round231 actual residual-saving admission (2026-10-11)

New reviewed adaptive factor cutoff D_T(x)=T^(-533/5250)x^(29/84) pays all actual unbalanced pairs at complete moment29/25, with top-scale cutoff853/3500. The original residual correction, head and tail are paid; the remaining balanced W_* needs a new signed estimate. An independent fixed-alpha11/50 component has exponent33787/26250<10beta. The literal all-polynomial residual saving is now rigorously capped at1/20, surviving arbitrary scalar centering; source quantifiers imply c<=3/20, so mere extraction of the unchanged universal constant cannot meet the complete-ceiling gate. The actual physical quartic major-arc set is empty below explicit thresholds. Common inverse exponents C_d>=d limit that certificate to saving7/72 over fixed degrees. Separate hypothetical A=3,B=4 would yield23/18, but are unproved. Actual same-character semiprimes obstruct coefficient-energy power saving only; no physical moment lower bound follows. Three reports, three nonauthor seams and bounded exact controls completed. Complete10beta unchanged; analytic231 pending_design, no State Patch. Decision: strategy/round231_residual_saving/conductor_decision.md.
"""
for f in ['state/project_summary.md','state/failure_ledger.md']:
 with (root/f).open('ab') as h: h.write(append.encode('utf-8'))
plan['status']='complete'; plan['completed_at']=now
for task in plan['tasks']:
 task['status']='complete'; task['report']='reports/'+task['id']+'.md'; task['report_sha256']=sha(p/task['report'])
plan['reviews']=[{'path':f,'status':'pass','sha256':sha(p/f)} for f in reviews]
plan['conductor_interventions']=[
'Preserved initial statement-only isolation for the important arithmetic residual control.',
'Redirected source investigation from an unspecified uniform saving toward the actual physical phase after the arithmetic obstruction appeared.',
'Required separate inverse exponents, full restoration and a common-exponent finite adversary; checked its all-degree optimization independently.',
'Suggested elementary prime counting and a sign pigeonhole for the actual semiprime energy control.',
"Strengthened the frozen fixed-alpha component result to an adaptive factor cutoff and assigned it within the factor reviewer's same single review cycle.",
'Kept all source numerical premises conditional and all certificate obstructions narrower than the physical moment problem.'
]
plan['decision']='retain_adaptive_signed_component_and_quantified_obstructions_no_complete_gain_not_admitted'
plan['graph_effect']='none; reviewed evidence only'
plan['complete_moment_bound_improved']=False
plan['resource_outcome']={'analytical_minimum_percent':95,'numerical_maximum_percent':5,'description':'Three analytical reports, two conductor derivations, three nonauthor seams and one bounded diagnostic script; one primary source family.'}
write(p/'plan.json',plan)
validation=[]
for module,args in [('math_collab.validate_state_patch',[]),('math_collab.campaigns',['validate'])]:
 r=subprocess.run([sys.executable,'-m',module,*args],capture_output=True,text=True,encoding='utf-8')
 validation.append({'command':[sys.executable,'-m',module,*args],'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 assert r.returncode==0,r.stdout+r.stderr
with ThreadPoolExecutor(max_workers=8) as pool:
 changed=[x for x in pool.map(check,[(f,h) for f,h in protected.items() if f not in meta]) if x]
assert not changed,('Unexpected protected change',changed)
g=read(root/'state/proof_obligations.yml')
closure={'completed_at':now,'decision':decision,'validation':validation,'protected_files_verified':len(protected),'authorized_metadata_changes':meta,'graph_nodes':len(g['proof_obligations']),'graph_sha256':sha(root/'state/proof_obligations.yml'),'proof_draft_sha256':sha(root/'state/best_proof_draft.md'),'active_manifest_sha256':sha(root/'state/active_campaign.yml'),'frozen_evidence_hashes':expected,'status':'passed'}
write(p/'controls/closure_validation.json',closure)
files=[f for f in p.rglob('*') if f.is_file() and f.name!='final_evidence_hashes.json']
write(p/'controls/final_evidence_hashes.json',{f.relative_to(p).as_posix():sha(f) for f in files})
print(json.dumps({'status':'closed','graph_nodes':closure['graph_nodes'],'protected_files':len(protected),'evidence_files':len(files),'graph_sha256':closure['graph_sha256'],'validators':[v['exit_code'] for v in validation]},indent=2))
