"""Freeze219 once from the closed218 state; no mathematical experiments."""
import hashlib,json,sys,time
from pathlib import Path
from datetime import datetime,timezone
root=Path.cwd();sys.path.insert(0,str(root))
from math_collab.campaigns import validate_campaign,prepare_campaign
from math_collab.proof_obligations import load_graph,validate_graph
cid='gc-complete-anchored-divisor-energy';base=Path('rounds/codex-managed')/cid
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def put(p,b):
 for i in range(5):
  try:Path(p).write_bytes(b);return
  except OSError:
   if i==4:raise
   time.sleep(.2)
def write(p,o):put(p,(json.dumps(o,indent=2,ensure_ascii=False)+'\n').encode())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=read('state/active_campaign.yml');assert old['round_index']==218 and old['status']=='complete'
archive=read('rounds/codex-managed/gc-complete-signed-radical-kernel/controls/artifact_hashes.json')
assert len(archive)==27
for p,h in archive.items():assert sha(p)==h,p
assert not (base/'plan.json').exists()
g=load_graph(Path('state/proof_obligations.yml'));assert len(g['proof_obligations'])==401 and not validate_graph(g,root=root)
h=sha('state/proof_obligations.yml');assert h==old['closing_assessment']['resulting_graph_sha256']
strategy='strategy/round219_complete_anchored_energy_attack.md';now=datetime.now(timezone.utc).isoformat()
for d in ['briefs','reports','candidates','reviews','controls']:(base/d).mkdir(parents=True,exist_ok=True)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',strategy,
'strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md',
'proofs/kernels/gc_complete_square_root_large_values_moment_bound.md',
'proofs/kernels/gc_complete_distinct_radical_moment_reduction.md',
'rounds/codex-managed/gc-actual-radical-high-values/reports/anchored_divisor_high_values.md',
'rounds/codex-managed/gc-complete-signed-radical-kernel/synthesis.md']
specs=[
('joint_cofactor_dispersion','discovery','selected_context',
'Attack the COMPLETE actual anchored energy inequality (12) of the216 report at rho208/2625. Use a joint cofactor-dispersion or joint Poisson calculation before separate moduli, preserving actual chi4, real high-value signs, the absolute radius and both minus cosine and plus sine terms. Bound every rectangle/major arc and restoration cost, or close this one mechanism at its first unproved estimate. Do not merely repeat216 scalar modulus bounds or218 stationary rank. No experiments. Seven sections and stop; assigned report only.',common+['rounds/codex-managed/gc-complete-signed-radical-kernel/reports/joint_divisor_kernel.md']),
('actual_anchor_incidence','barrier_no_go','selected_context',
'Independently attack or audit the complete actual anchored energy inequality (12) of216 through exact and near multiplicative-anchor incidence arithmetic and chi4 signs. Keep actual sigma_j=sign H(R_j) and the fact these are high points. Test whether character cancellation survives common radical labels, whether a usable signed cluster estimate follows from alignment, and pay all remaining near/plus terms. An arbitrary-sign counterexample is only a control of an enlarged assertion; do not refute actual target with it. Produce complete quantitative bound or scoped limitation with precise first gap. No experiments. Seven sections and stop; assigned report only.',common),
('blind_anchor_classes','blind_rederiver','statement_only',
'Solve only the isolated exact anchored radical-class statement; no arithmetic application or other context. Seven sections, no experiments, assigned report only and stop.',
['protocol.md',base.as_posix()+'/briefs/blind_anchor_statement.md'])]
controls=['actual_coefficients','actual_aligned_high_points','exact_anchor_incidence','near_anchor_incidence','all_plus_minus_terms','every_rectangle_and_tail','full_exponent_restoration','arbitrary_sign_scope','statement_only_control','unbounded_order_goal_scope']
tasks=[]
for ident,role,mode,target,ctx in specs:
 t=dict(id=ident,role=role,access_mode=mode,status='pending',target=target,context_files=ctx,required_controls=controls,required_output=['Seven numbered protocol sections: result; exact hypotheses; proof; first gap; controls; exact dependencies; state effect.','Only assigned report; no shared state, synthesis, siblings or next round.'],report_path=base.as_posix()+'/reports/'+ident+'.md')
 if mode=='statement_only':t['excluded_context']=['All files except protocol and isolated statement; disclose prior-task history if reused.']
 tasks.append(t)
m=dict(schema_version=1,round_index=219,round_type='complete_actual_anchored_energy_attack',campaign_id=cid,title='Complete actual anchored divisor-energy attack',status='active',max_concurrency=3,coordinator='Codex',starting_graph_sha256=h,generated_at=now,
resource_policy=dict(analytical_algebraic_minimum_percent=95,numerical_experimental_maximum_percent=5,planned_numerical_percent=0,budget='Three bounded seven-section reports, one mechanism per discovery task and one same-round review cycle; zero planned mathematical experiments.'),
target_obligations=['GC-target','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction'],
frozen_target=dict(question='Can the complete actual aligned anchored divisor energy satisfy inequality(12) at rho208/2625?',reference_formula='O <= J^2 v^2 N^(3/2)/(64K) + C_eta T^(208/2625+eta) JN, uniformly over every actual rectangle and aligned high-point set.',quantities=['Exact real Q and constant diagonal D from216, O=Q-D; all minus cosine and plus sine terms retained.','R_j physical in[T/2,2T], N^(-1/2)-separated maximal high points, sigma_j=sign H(R_j), every rectangle N<=T^(3/2), K=N/D.','v>=T^(13/125)/(2L), L is the total number of dyadic rectangles.','Conditional full high twelfth moment has exponent113/125+42rho/13=29/25; the input is unproved.','Fixed milestone only; full quarter requires a sufficient unbounded-fixed-order family or full alternate parents.']),
completion_criteria=['Three bounded seven-section reports and statement-only exact-anchor rederivation.','All actual signed energy terms and restored costs accounted for; precise scope of any failed enlarged assertion.','Independent final-hash seams, conductor controls, validated patch and219 closure.'],controls=controls,
exit_labels=['complete_anchored_energy_gain_requires_validation','complete_anchored_energy_attempt_no_new_bound'],tasks=tasks,
review_seams=[dict(id='signed_energy_and_character',requirement='Exact characters, real signs, all terms, anchors, integer multiplicities and endpoints.'),dict(id='complete_restoration',requirement='Every rectangle/major arc/tail and full high-value exponent; no arbitrary-sign control promoted as actual counterexample.'),dict(id='isolated_anchor_binding',requirement='Statement-only class derivation and independent actual application.')],
previous_goal_turn_classification='progress_completed_joint_transform_diagnosis_no_complete_moment_gain',scheduled_review='Mandatory broad strategy/current-primary-literature review220 after217--219.')
assert not validate_campaign(m,g,root=root)
write('state/active_campaign.yml',m)
write('state/next_round_plan.yml',dict(round_index=219,status='active',campaign_id=cid,starting_graph_sha256=h,predecessor_round=218,tasks=[t['id'] for t in tasks]))
lp=Path('state/round_ledger.yml');s=lp.read_text(encoding='utf-8');ledger=json.loads(s)
assert ledger['rounds'][-1]['round_index']==218 and ledger['rounds'][-1]['status']=='closed'
entry=dict(round_index=219,campaign_id=cid,type=m['round_type'],status='active',objective=m['frozen_target']['question'],tasks=[{k:t[k] for k in ['id','role','status']} for t in tasks],resource_policy=m['resource_policy'],starting_graph_sha256=h,exit_labels=m['exit_labels'],started_at=now)
marker='\n  ]\n}';head,tail=s.rsplit(marker,1)
new=head+',\n'+'\n'.join('    '+line for line in json.dumps(entry,indent=2).splitlines())+marker+tail
new=new.replace('"active_round": 218','"active_round": 219',1);ledger['active_round']=219;ledger['rounds'].append(entry);assert json.loads(new)==ledger
put(lp,new.encode())
matrix=read('state/validation_matrix.yml');matrix.update(campaign_id=cid,promotion_status='round_219_active_no_promotion',graph_sha256=h,decision_rule='Complete actual anchored energy attack; no new estimate accepted at launch.')
for t in tasks:matrix['gates'].append(dict(id='round219_'+t['id'],status='pending',artifact=t['report_path']))
matrix['gates'].append(dict(id='round219_conductor_reconciliation',status='pending',artifact=base.as_posix()+'/reviews/conductor_round219_reconciliation.md'))
write('state/validation_matrix.yml',matrix)
write(base/'controls/starting_state_hashes.json',{p:sha(p) for p in ['state/proof_obligations.yml','state/best_proof_draft.md','strategy/gauss_circle_strategy_review_2026-09-23.md']})
failure=Path('state/failure_ledger.md');oldbytes=failure.read_bytes();prepare_campaign(m,g,root=root,graph_path=root/'state/proof_obligations.yml')
put(failure,oldbytes+b'\n\n## Round219 complete anchored-energy barriers\n\nThe216 signed energy inequality is unproved; scalar moduli lose D and an unabsorbable term. Round218 stationary transforms do not improve the full moment. Preserve actual aligned signs, both real kernels and every exact/near anchor incidence. A rephased control cannot refute actual high-value energy. Returning known bounds is no complete-bound progress; no new smaller complement is a success.\n')
write(base/'controls/frozen_artifact_hashes.json',{p.as_posix():sha(p) for p in [base/'plan.json',Path(strategy)]+sorted((base/'briefs').glob('*.md'))})
for t in m['tasks']:t['status']='running'
write('state/active_campaign.yml',m);assert not validate_campaign(m,g,root=root)
print('Round219 frozen; closed218 archive27 verified; graph401 unchanged; three briefs ready.')
