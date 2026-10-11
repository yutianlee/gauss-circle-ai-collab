"""Close reviewed admission evidence without altering accepted mathematics."""
from pathlib import Path
import json, hashlib, datetime, subprocess, sys

root=Path.cwd(); p=root/'strategy/round231_local_arithmetic_admission'
def sha(f):return hashlib.sha256(Path(f).read_bytes()).hexdigest()
def read(f):return json.loads(Path(f).read_text(encoding='utf-8'))
def write(f,d):Path(f).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
expected={
 'reports/local_residue_arithmetic.md':'403e2c52c67dd46d033a06ae0d002d308dd695af1018241463f5c91410f67d41',
 'reports/oscillatory_remainder_gate.md':'834954f74200d00a508aeb0d360134a444ea1b3b0b2271d4e3b271ecd95febfe',
 'reports/blind_cell_control.md':'001465ba0e7e73d99f75e0375df449b7cddcc0d2a362cfb5baba06e649e35fec',
 'conductor_cell_obstruction.md':'09548d3a7f039258bdb60e34e6faedcc560f8b76b84b17bfd3cb088ba7ab12f2',
 'reviews/cell_obstruction_seam_review.md':'7fd6d37406c2c9ae42ee3f188da1386274b5d9eda990f982d3529d669d535756',
 'reviews/local_transfer_seam_review.md':'5fa4c9ef117c2e5fd268f21f84f4f4e8e0df1483c4fcaaddd3fd01f1666bb5a0'}
for f,h in expected.items():assert sha(p/f)==h,f
for f in ['reviews/cell_obstruction_seam_review.md','reviews/local_transfer_seam_review.md']:
 assert '**PASS' in (p/f).read_text(encoding='utf-8'),f
protected=read(p/'controls/starting_hashes.json')
protected.update(read(p/'controls/continuation_starting_hashes.json'))
for f,h in protected.items():assert sha(root/f)==h,('preclosure protected change',f)
inherited=read(p/'controls/resume_packet_inventory.json')
for f,h in inherited.items():assert sha(p/f)==h,('inherited changed',f)
validation=[]
for module,args in [('math_collab.validate_state_patch',[]),('math_collab.campaigns',['validate'])]:
 r=subprocess.run([sys.executable,'-m',module,*args],capture_output=True,text=True)
 validation.append({'command':[sys.executable,'-m',module,*args],'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 assert r.returncode==0,r.stdout+r.stderr
write(p/'controls/mechanical_validation.json',validation)
assert read(p/'controls/continuation_exact_controls.json')['status']=='passed'
assert read(p/'controls/local_residue_reproduction.json')['exit_code']==0

decision={
 'completed_at':now,'status':'not_admitted','analytic_campaign_launched':False,
 'packet':'strategy/round231_local_arithmetic_admission',
 'decision':'strategy/round231_local_arithmetic_admission/conductor_decision.md',
 'mechanism':'Actual congruence densities with retained oscillatory remainders; exact-cell information control',
 'findings':[
  'Exact odd/even norm densities and all additive modes are proved. Numerator completion and physical variation leave no new complete estimate.',
  'Polynomial rational demodulation is valid, but the specific absolute short-patch certificate is at least T^(1/6) on an actual required shell; the stated generic head bound cannot remove it at an improved exponent.',
  'Independently proved fixed-cell perturbation lemma; separately reviewed N=T^(4beta) extension preserves actual support, exact cell totals, the full complement and inherited pointwise ceiling, yet one perturbed complete wave has M12>=cT^(10beta).',
  'The latter is a coefficient-class obstruction, not a lower bound for exact r2; multiplicativity and all prefix errors are not preserved.',
  'Both nonauthor seam reviews pass after local positivity/window clarification; all 753 finite residue controls are independently reproduced.'
 ],
 'scope':'Reviewed prelaunch evidence. Specific certificate and information-content obstructions only; no all-method arithmetic impossibility theorem.',
 'graph_effect':'none; no State Patch or promotion',
 'required_new_input':'A new bound for actual signed oscillatory remainders and their rational mains with all shells paid, using additional arithmetic structure or joint signed cancellation. Do not relaunch from residue means or these rejected absolute patch/cell-total certificates.',
 'complete_target':'M12<=T^(29/25+epsilon); accepted10beta=1.289663519481... unchanged.'}
next_path=root/'state/next_round_plan.yml'; nxt=read(next_path)
assert nxt['round_index']==231 and nxt['status']=='pending_design'
prior=nxt.get('latest_admission_check')
if prior:nxt.setdefault('admission_check_history',[]).append(prior)
nxt['latest_admission_check']=decision
write(next_path,nxt)

summary='''# Current research status — local arithmetic admission test closed

11 October 2026. The resumed Round231 local-arithmetic test is complete. Exact norm residue densities and their Fourier modes retain an unestimated oscillatory remainder after all costs are restored. Polynomial rational demodulation is valid, but the specified sum of absolute short-patch bounds is already at least T^(1/6) on an actual required shell; its generic head bound cannot pay that shell at an improved exponent.

The new independently proved cell control is stronger than a coarse-density model: bounded nonnegative perturbations on actual represented-integer locations preserve every total in a sublinear fixed cell partition. The reviewed smaller-shell extension also preserves the complete complement and inherited pointwise ceiling while attaining a complete moment at least T^(10beta). This is a limitation of those data, not a lower bound for the exact r2 wave. Multiplicativity and all prefix discrepancies are not preserved.

The three resumed reports and two nonauthor seam reviews are complete. Uniform positivity and the physical supremum window were clarified before final review. The conductor reproduced all 753 finite residue controls. No new complete bound follows: the retained exponent is 10beta=1.289663519481..., versus the open target 29/25=1.16. The pointwise benchmark and quarter goal remain unchanged.

Analytic Round231 remains pending_design with no analytic tasks launched. Further admission requires a new actual signed remainder estimate, including rational mains and all complementary shells, using additional arithmetic structure or joint cancellation. No automatic successor is launched.

The 401-node graph, proof draft, validation matrix, closed Round230 manifest, round ledger, archived campaigns and previous admission packets are preserved. No State Patch or promotion. Decision: strategy/round231_local_arithmetic_admission/conductor_decision.md. Inherited strategy: strategy/gauss_circle_strategy_checkpoint_round230_2026-10-11.md.
'''
for f in ['state/current_round.md','state/next_campaign.md']:(root/f).write_text(summary,encoding='utf-8')
append='''

## Round231 local-arithmetic admission continuation (2026-10-11)

The resumed bounded test closes without analytic admission. Exact local norm densities retain the full signed remainder and numerator-completion costs. A specific absolute first-order short-patch certificate is >=cT^(1/6) on an actual required shell, which its generic norm-head bound cannot remove at a gain. Separately, an independently proved fixed-cell perturbation lemma and reviewed smaller-shell extension preserve actual represented support, exact finite cell totals, the complete complement and inherited pointwise ceiling while attaining M12>=cT^(10beta). This is an information-content obstruction, not an actual r2 lower bound; multiplicativity and all prefix estimates are outside its preserved data. Both nonauthor reviews pass and 753 finite residue controls were reproduced locally. No complete bound, graph patch, proof-draft change or successor. Next admission needs a new actual signed inequality with rational mains and all shells paid. Full decision: strategy/round231_local_arithmetic_admission/conductor_decision.md.
'''
for f in ['state/project_summary.md','state/failure_ledger.md']:
 with (root/f).open('ab') as h:h.write(append.encode('utf-8'))

plan_path=p/'admission_plan.json';plan=read(plan_path)
plan['status']='complete';plan['completed_at']=now
for t in plan['tasks']:
 t['status']='completed';t['report_sha256']=sha(p/t['report'])
plan['post_report_review']['status']='completed_pass'
plan['reviews']=[{'path':f,'sha256':h} for f,h in expected.items() if f.startswith('reviews/')]
plan['decision']='not_admitted_scoped_local_information_and_patch_certificate_obstructions'
plan['conductor_decision']='conductor_decision.md';plan['graph_effect']='none; reviewed evidence only'
plan['resource_outcome']={'analytical_minimum_percent':95,'numerical_maximum_percent':5,'activity':'Three analytical reports, independent cell proof, two nonauthor reviews, bounded exact residue/finite-control reproduction; no asymptotic simulation or new theorem import.'}
write(plan_path,plan)

for f,h in protected.items():
 if f!='state/next_round_plan.yml':assert sha(root/f)==h,('postclosure protected change',f)
for f,h in inherited.items():assert sha(p/f)==h,('inherited changed after closure',f)
for f,h in expected.items():assert sha(p/f)==h,('frozen evidence changed',f)
graph=read(root/'state/proof_obligations.yml')
checks={'status':'passed','completed_at':now,'phase':'fourth_prelaunch_local_arithmetic_continuation_only',
 'analytic_round231_launched':False,'graph_nodes':len(graph['proof_obligations']),
 'graph_sha256':sha(root/'state/proof_obligations.yml'),'proof_draft_sha256':sha(root/'state/best_proof_draft.md'),
 'protected_files_checked_before_metadata':len(protected),'protected_files_unchanged_after':len(protected)-1,
 'sole_protected_metadata_update':'state/next_round_plan.yml','inherited_packet_files_preserved':len(inherited),
 'three_prior_admission_packets_preserved':True,'closed_rounds_and_round_ledger_preserved':True,
 'graph_validation':'pass','active_closed_campaign_validation':'pass','statement_only_cell_proof':'pass',
 'nonauthor_cell_full_baseline_and_extension_review':'pass','nonauthor_signed_transfer_and_head_review':'pass',
 'exact_residue_controls_reproduced':'753 cases passed','inherited_finite_control_reproduced':'pass; finite-only scope',
 'state_metadata_changed':['state/next_round_plan.yml','state/current_round.md','state/next_campaign.md','state/project_summary.md','state/failure_ledger.md'],
 'state_effect':'No State Patch, graph promotion or complete bound improvement.',
 'scope':'Fixed-cell coefficient-class obstruction and specific actual absolute-patch certificate obstruction; exact signed target remains open.'}
write(p/'controls/closure_validation.json',checks)
exclude={'controls/final_evidence_hashes.json'}
allhash={f.relative_to(p).as_posix():sha(f) for f in p.rglob('*') if f.is_file() and f.relative_to(p).as_posix() not in exclude}
write(p/'controls/final_evidence_hashes.json',allhash)
print(json.dumps({'status':'passed','graph_nodes':checks['graph_nodes'],'protected_files':len(protected),'frozen_packet_files':len(allhash),'decision':plan['decision'],'graph_sha256':checks['graph_sha256']},indent=2))
